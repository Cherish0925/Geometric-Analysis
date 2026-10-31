"""Direct search in the dangerous positive-q sector of the triaxial cell.

Notation is that of I55 (8.1)--(8.5) and cell_compensation.py:
    q = T_phi - P_w,  M0 = 1 + 2/mu,
    j = J/(2*pi^2).
A subthreshold cell must have q in a positive interval, and a fixed
improvement as mu -> 0 requires q of order 1/mu.  Earlier fixed-N searches
never entered q>0.  This script instead minimizes j with q/M0 fixed.

Two independent continuations are supplied.
  * inner: phi is initialized from a smooth bump in r/sqrt(mu) on [2,3];
    this has T_phi ~ amplitude^2/mu and can reach q~M0 at O(1) amplitude.
  * fixed: phi is initialized from a smooth bump on a fixed physical annulus;
    reaching q~M0 then requires amplitude of order mu^{-1/2}.
Both starts are projected to the exact Chebyshev/collar basis used by Cell.
After initialization F,w,phi are all optimized, so agreement of the two
continuations is a basin-stability check rather than an imposed support
restriction.

The output retains both exact I54 and I55 decomposition residuals.
"""
import argparse
import json
import math
import os
import sys

import torch

sys.path.insert(0, os.path.dirname(__file__))
from cell_opt import Cell
from cell_compensation import diagnostics_tensor, floats

torch.set_default_dtype(torch.float64)


def preopt_kahler(cell, iters=3500):
    """Low-cost w=phi=0 Kahler recovery in the exact bolt/collar class."""
    n = cell.deg + 1
    cF = torch.zeros(n, requires_grad=True)
    cw = torch.zeros(n)
    cp = torch.zeros(n)
    opt = torch.optim.LBFGS([cF], lr=1.0, max_iter=iters, history_size=80,
                            tolerance_grad=1e-12, tolerance_change=1e-15,
                            line_search_fn='strong_wolfe')

    def closure():
        opt.zero_grad()
        d = diagnostics_tensor(cell, cF, cw, cp)
        positivity = torch.relu(2e-3-d['F_min_scaled'])**2*1e7
        loss = d['j'] + positivity
        loss.backward()
        return loss

    opt.step(closure)
    return cF.detach(), cw, cp


def smooth_bump(z):
    """C-infinity bump supported in |z|<1, normalized to max 1."""
    inside = torch.abs(z) < 1
    safe = torch.where(inside, 1-z*z, torch.ones_like(z))
    raw = torch.where(inside, torch.exp(1-1/safe), torch.zeros_like(z))
    return raw


def project_phi(cell, kind, fixed_support=(0.55, 1.05)):
    """Least-squares project a physical or inner-scale bump to Cell's phi basis."""
    r = cell.r
    if kind == 'inner':
        center, half = 2.5*cell.r0, 0.5*cell.r0
    elif kind == 'fixed':
        center = (fixed_support[0]+fixed_support[1])/2
        half = (fixed_support[1]-fixed_support[0])/2
        if fixed_support[1] >= cell.Rc:
            raise ValueError('fixed bump support must lie below Rc')
    elif kind == 'broad':
        # A third check: use the lowest exact-collar basis mode directly.
        out = torch.zeros(cell.deg+1)
        out[0] = 1
        return out
    else:
        raise ValueError(kind)
    target = smooth_bump((r-center)/half)
    T = cell.B[0]
    design = cell.e40[0][:, None]*T
    # Weighted least squares is preferable because the diagnostic uses dr.
    weight = torch.sqrt(cell.wx*cell.jac)
    A = weight[:, None]*design
    b = weight*target
    return torch.linalg.lstsq(A, b[:, None], rcond=1e-12).solution[:, 0]


def scale_phi_to_q(cell, cF, cp_direction, q_target, sign=-1.0):
    """For w=0, q=T_phi is exactly quadratic in the phi coefficients."""
    cw = torch.zeros_like(cp_direction)
    q1 = diagnostics_tensor(cell, cF, cw, cp_direction)['q']
    if float(q1) <= 0:
        raise RuntimeError('projected phi direction has nonpositive T_phi')
    return sign*math.sqrt(q_target/float(q1))*cp_direction


def prepare_init(cell, cF0, family, q_target, sign, wseed=-1, wamp=0.03):
    cpdir = project_phi(cell, family)
    cw = torch.zeros_like(cpdir)
    if wseed >= 0:
        # Break the w -> -w symmetric stationary sector.  Low Chebyshev
        # directions probe smooth inner/transition anisotropy; q is restored
        # exactly after accounting for the induced P_w.
        cw[wseed % len(cw)] = wamp
    Pw = diagnostics_tensor(cell, cF0, cw, torch.zeros_like(cpdir))['Pw']
    cp = scale_phi_to_q(cell, cF0, cpdir, q_target+float(Pw), sign)
    return {'cF': cF0.tolist(), 'cw': cw.tolist(), 'cp': cp.tolist()}


def rescale_warm_phi(cell, init, q_target):
    """Move a previous positive-q solution toward the next q target."""
    cF = torch.tensor(init['cF'])
    cw = torch.tensor(init['cw'])
    cp = torch.tensor(init['cp'])
    q = diagnostics_tensor(cell, cF, cw, cp)['q']
    # Scaling only phi preserves the anisotropy profile and changes T_phi
    # quadratically.  Solve T_new = q_target + P_w exactly.
    Pw = diagnostics_tensor(cell, cF, cw, cp)['Pw']
    T = diagnostics_tensor(cell, cF, cw, cp)['Tphi']
    if float(T) > 1e-14 and float(q_target+Pw) > 0:
        cp = cp*torch.sqrt((q_target+Pw)/T)
    return {'cF': cF.tolist(), 'cw': cw.tolist(), 'cp': cp.tolist()}


def q_constrained_run(cell, qfrac, init, family, sign, wseed=-1,
                      outer=10, inner=1600, rho=300.0):
    M0 = 1+2/cell.mu
    target = torch.as_tensor(qfrac*M0)
    cF = torch.tensor(init['cF'], requires_grad=True)
    cw = torch.tensor(init['cw'], requires_grad=True)
    cp = torch.tensor(init['cp'], requires_grad=True)
    lam = torch.tensor(0.0)
    history = []
    rho_now = rho
    d = diagnostics_tensor(cell, cF, cw, cp)
    init_diag = floats(d)

    for oi in range(outer):
        opt = torch.optim.LBFGS([cF, cw, cp], lr=0.55, max_iter=inner,
                                history_size=80, tolerance_grad=2e-11,
                                tolerance_change=2e-14,
                                line_search_fn='strong_wolfe')

        def closure():
            opt.zero_grad()
            dloc = diagnostics_tensor(cell, cF, cw, cp)
            con = dloc['q']-target
            positivity = torch.relu(2e-3-dloc['F_min_scaled'])**2*1e7
            loss = dloc['j'] + lam*con + rho_now*con*con/2 + positivity
            loss.backward()
            return loss

        opt.step(closure)
        d = diagnostics_tensor(cell, cF, cw, cp)
        con = (d['q']-target).detach()
        lam = (lam+rho_now*con).detach()
        history.append({'outer': oi, 'q_error': float(con), 'j': float(d['j']),
                        'q': float(d['q']), 'F_min_scaled': float(d['F_min_scaled'])})
        if oi >= 2 and abs(float(con)) > abs(history[-2]['q_error'])*0.8:
            rho_now *= 2
        if abs(float(con)) < max(2e-6, 2e-6*float(target)):
            break

    out = floats(diagnostics_tensor(cell, cF, cw, cp))
    out.update(qfrac_target=qfrac, q_target=float(target), family=family,
               sign=sign, wseed=wseed, deg=cell.deg, coord=cell.coord,
               history=history,
               init_j=init_diag['j'], init_q=init_diag['q'],
               cF=cF.detach().tolist(), cw=cw.detach().tolist(),
               cp=cp.detach().tolist())
    return out


def public_summary(res):
    keys = ['mu', 'Rc', 'family', 'sign', 'wseed', 'qfrac_target', 'q_target', 'q',
            'j', 'K', 'deficit', 'proj', 'rx', 'ry', 'rz', 'rv', 'Pw',
            'Tphi', 'nfrac', 'A_pay', 'B_pay', 'scalar_pay',
            'F_min_scaled', 'w_max', 'phi_max', 'radial_identity_error',
            'i54_identity_error']
    return {k: res[k] for k in keys}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--mu', type=float, nargs='+', default=[0.1])
    ap.add_argument('--Rc', type=float, default=2.0)
    ap.add_argument('--deg', type=int, default=24)
    ap.add_argument('--nq', type=int, default=700)
    ap.add_argument('--qfrac', type=float, nargs='+',
                    default=[0.05, 0.15, 0.35, 0.6, 1.0])
    ap.add_argument('--families', nargs='+', default=['inner', 'fixed'])
    ap.add_argument('--signs', type=float, nargs='+', default=[-1.0, 1.0])
    ap.add_argument('--wseeds', type=int, nargs='+', default=[-1, 0, 1])
    ap.add_argument('--wamp', type=float, default=0.03)
    ap.add_argument('--outer', type=int, default=10)
    ap.add_argument('--inner-iters', type=int, default=1600)
    ap.add_argument('--rho', type=float, default=300.0)
    ap.add_argument('--preopt-iters', type=int, default=3500)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    os.makedirs(os.path.dirname(a.out), exist_ok=True)

    with open(a.out, 'w') as fh:
        for mu in a.mu:
            cell = Cell(mu, a.Rc, a.deg, nq=a.nq, coord='log')
            cF0, _, _ = preopt_kahler(cell, a.preopt_iters)
            baseline = floats(diagnostics_tensor(
                cell, cF0, torch.zeros(a.deg+1), torch.zeros(a.deg+1)))
            print(json.dumps({'baseline': public_summary({**baseline,
                  'family': 'kahler', 'sign': 0, 'wseed': -1,
                  'qfrac_target': 0, 'q_target': 0})}), flush=True)
            for family in a.families:
                for sign in a.signs:
                    for wseed in a.wseeds:
                        warm = None
                        for qfrac in sorted(a.qfrac):
                            target = qfrac*(1+2/mu)
                            if warm is None:
                                init = prepare_init(cell, cF0, family, target, sign,
                                                    wseed, a.wamp)
                            else:
                                init = rescale_warm_phi(cell, warm, target)
                            res = q_constrained_run(cell, qfrac, init, family, sign,
                                                    wseed, a.outer,
                                                    a.inner_iters, a.rho)
                            fh.write(json.dumps(res)+'\n'); fh.flush()
                            print(json.dumps(public_summary(res)), flush=True)
                            warm = res


if __name__ == '__main__':
    main()
