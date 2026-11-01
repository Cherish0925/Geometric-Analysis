#!/usr/bin/env python3
"""Step 78: explicit quadratic form of the 15 order-6 residual AKE conditions at a fixed torsion jet H2,
and its real solvability.

Psi15(y) = c + J y + Q(y),  y in R^{117} (admissible H4 after orders 2,4; H6 eliminated linearly),
Q_i(y) = y^T H_i y / 2.  Analysis:
  (a) exactness of the quadratic model at random y;
  (b) certificate SDP: max t s.t. [[l.c, l.J/2],[l.J^T/2, l.H/2]] >= t I, |l|<=1  (t>0 => no real solution);
  (c) many-start Levenberg-Marquardt on the explicit polynomial system (numpy, cheap);
  (d) homogeneous test: Q restricted to ker J hitting -c.
Output: workspace/data/step78/quad6_<tag>.json, quad6_<tag>.npz (c, J, H)
"""
import json, sys, time
from pathlib import Path
import numpy as np
import torch
sys.path.insert(0, str(Path(__file__).resolve().parent))
from step77_gn_germ import dev, dt, jet_coords
from step78_real_tower import Tower, load_h2_from_d6
from step78_certificate import random_quadric_H2
from step78_reduced_order6 import Reduced

OUT = Path(__file__).resolve().parents[1] / 'data' / 'step78'


def extract(R):
    y0 = torch.zeros(R.ny, dtype=dt, device=dev)
    J0 = torch.func.jacfwd(R.Psi)(y0)
    U, s, Vh = torch.linalg.svd(J0, full_matrices=False)
    r = int((s > 1e-9 * s[0]).sum())
    Ur = U[:, :r]
    P = lambda y: Ur.T @ R.Psi(y)
    c = P(y0); J = Ur.T @ J0
    # Psi is exactly quadratic: D Psi(e_a) - D Psi(0) = H[:, :, a]
    cols = []
    for a in range(R.ny):
        ea = torch.zeros(R.ny, dtype=dt, device=dev); ea[a] = 1.0
        cols.append((Ur.T @ torch.func.jacfwd(R.Psi)(ea)) - J)
    H = torch.stack(cols, dim=2)
    H = 0.5 * (H + H.transpose(1, 2))
    return c.cpu().numpy(), J.cpu().numpy(), H.cpu().numpy(), r, P


def model(c, J, H, y):
    return c + J @ y + 0.5 * np.einsum('iab,a,b->i', H, y, y)


def lm(c, J, H, y, iters=300):
    mu = 1e-3
    f = model(c, J, H, y); nf = np.linalg.norm(f)
    for it in range(iters):
        Jy = J + np.einsum('iab,b->ia', H, y)
        g = Jy.T @ f
        A = Jy.T @ Jy
        while True:
            step = -np.linalg.solve(A + mu * np.eye(len(y)), g)
            fn = model(c, J, H, y + step); nn = np.linalg.norm(fn)
            if nn < nf:
                y, f, nf = y + step, fn, nn; mu = max(mu / 3, 1e-15); break
            mu *= 4
            if mu > 1e12:
                return y, nf, it
        if nf < 1e-13:
            break
    return y, nf, it


def sdp(c, J, H):
    import cvxpy as cp
    m, n = J.shape
    l = cp.Variable(m); t = cp.Variable()
    top = cp.reshape(c @ l, (1, 1), order='C')
    lin = cp.reshape(J.T @ l / 2, (n, 1), order='C')
    Q = sum(l[i] * (H[i] / 2) for i in range(m))
    M = cp.bmat([[top, lin.T], [lin, Q]])
    prob = cp.Problem(cp.Maximize(t), [(M + M.T) / 2 - t * np.eye(n + 1) >> 0, cp.norm(l, 2) <= 1])
    prob.solve(solver='CLARABEL')
    lv = l.value
    Mv = np.block([[np.array([[c @ lv]]), (J.T @ lv / 2)[None]], [(J.T @ lv / 2)[:, None], np.tensordot(lv, H, 1) / 2]])
    ev = np.linalg.eigvalsh((Mv + Mv.T) / 2)
    return {'status': prob.status, 't': float(t.value), 'eig_min': float(ev[0]), 'l': lv.tolist()}


def main(lam=-3.0, h2='random', seed=0, nh2=3, scale=1.0, nstarts=200, tag=None):
    rng = np.random.default_rng(seed); torch.manual_seed(seed)
    T = Tower(6, lam)
    out = {'lam': lam, 'seed': seed, 'scale': scale, 'runs': []}
    tag = tag or f'lam{lam}_{h2}_s{seed}_sc{scale}'
    for a in range(nh2):
        if h2 == 'd6':
            H2 = load_h2_from_d6(OUT.parent / 'step77_gn_D6_even_lam-3.0_s0.pt', T)[2]
        else:
            H2, _ = random_quadric_H2(T, lam, rng, scale)
        zero = {d: torch.zeros(T.size[d], dtype=dt, device=dev) for d in T.degs if d != 2}
        jc = jet_coords(T.torsion({2: H2, **zero}))
        tn = float(np.sqrt(4 * jc['c2'] + 2 * jc['S2'] + 2 * jc['A2']))
        R = Reduced(T, H2)
        c, J, H, r, P = extract(R)
        # (a) exactness
        errs = []
        for _ in range(3):
            y = rng.standard_normal(R.ny)
            exact = P(torch.tensor(y, dtype=dt, device=dev)).cpu().numpy()
            errs.append(float(np.linalg.norm(exact - model(c, J, H, y)) / np.linalg.norm(exact)))
        rec = {'h2_index': a, 'jet': jc, 'lam_over_torsion': lam / tn, 'n_cond': r, 'ny': int(R.ny), 'quad_model_relerr': errs,
               '|c|': float(np.linalg.norm(c)), 'svJ': np.linalg.svd(J, compute_uv=False).tolist()}
        # (c) LM starts
        finals = []
        best = None
        for s in range(nstarts):
            sc = 10 ** rng.uniform(-2, 1.5)
            y, nf, it = lm(c, J, H, sc * rng.standard_normal(R.ny))
            finals.append(nf)
            if best is None or nf < best[0]:
                best = (nf, y)
        finals = np.array(finals)
        rec['lm_min'] = float(finals.min()); rec['lm_median'] = float(np.median(finals))
        rec['lm_frac_solved'] = float((finals < 1e-10).mean())
        y = best[1]
        Jy = J + np.einsum('iab,b->ia', H, y)
        rec['best_y_norm'] = float(np.linalg.norm(y)); rec['best_sv_min'] = float(np.linalg.svd(Jy, compute_uv=False)[-1])
        if rec['lm_min'] < 1e-10:
            # verify against the full nonlinear system
            exact = P(torch.tensor(y, dtype=dt, device=dev)).cpu().numpy()
            rec['verify_full_Psi'] = float(np.linalg.norm(exact))
            rec['verify_lower_orders'] = float(R.full(torch.tensor(y, dtype=dt, device=dev)).norm())
            torch.save({2: H2.cpu(), 4: R.H4of(torch.tensor(y, dtype=dt, device=dev)).cpu(),
                        6: R.H6of(torch.tensor(y, dtype=dt, device=dev)).cpu()}, OUT / f'quad6_sol_{tag}_h{a}.pt')
        # (b) SDP certificate
        try:
            rec['sdp'] = sdp(c, J, H)
        except Exception as e:
            rec['sdp'] = {'error': str(e)}
        print('H2', a, 'lam/tors %.3f c2 %.3g S2 %.3g A2 %.3g' % (rec['lam_over_torsion'], jc['c2'], jc['S2'], jc['A2']),
              'ncond', r, 'quad err %.1e' % max(errs), 'LM min %.2e med %.2e solved %.2f' % (rec['lm_min'], rec['lm_median'], rec['lm_frac_solved']),
              'sdp t', rec['sdp'].get('t'), rec.get('verify_full_Psi'), rec.get('verify_lower_orders'), flush=True)
        np.savez(OUT / f'quad6_{tag}_h{a}.npz', c=c, J=J, H=H, H2=H2.cpu().numpy())
        out['runs'].append(rec)
    (OUT / f'quad6_{tag}.json').write_text(json.dumps(out, indent=1) + '\n')


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument('--lam', type=float, default=-3.0)
    ap.add_argument('--h2', default='random')
    ap.add_argument('--seed', type=int, default=0)
    ap.add_argument('--nh2', type=int, default=3)
    ap.add_argument('--scale', type=float, default=1.0)
    ap.add_argument('--nstarts', type=int, default=200)
    a = ap.parse_args()
    main(a.lam, a.h2, a.seed, a.nh2, a.scale, a.nstarts)
