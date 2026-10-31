"""Numerical minimization of the relative cell cost j = J/(2 pi^2) over the
conformal triaxial one-bolt class (inherited eq. (6.10) of
Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md).

Cell: ordinary blowup of the CH ball r <= Rc (Ric = -g normalization,
F_CH = 1 + r^2/6), exceptional bolt at r = r0 (mu = r0^2, area pi mu).
Threshold: a cell with j < 4 would give a balanced-family coefficient below
four via inherited eq. (2.2)-(2.3).

Parametrization, x = (r - r0)/L, L = Rc - r0:
  F   = F_CH(r) - (1-x)^4 (b0 + b1 x + x^2 P_F(x))   (bolt: F(r0)=0, F'(r0)=2/r0)
  w   = x^2 (1-x)^4 P_w(x)
  phi = (1-x)^4 P_phi(x)
P_* are Chebyshev series in (2x-1). Metric is C^3 across r = Rc and exactly CH
beyond, so the defect vanishes there.

Usage: python cell_opt.py --mu 0.1 --Rc 1.0 --deg 14 [--kahler-only] [--nophi]
Outputs JSON lines to stdout and to --out file.
"""
import argparse, json, math, sys, os
import numpy as np
import sympy as sp
import torch

sys.path.insert(0, os.path.dirname(__file__))
from cell_ricci import ricci_exprs, r as rs, Fs, F1, F2, ws, w1, w2, ps, p1, p2

torch.set_default_dtype(torch.float64)

_ex = ricci_exprs()
_tmods = [{'exp': torch.exp, 'sinh': torch.sinh, 'cosh': torch.cosh, 'sqrt': torch.sqrt, 'log': torch.log}]
RIC = [sp.lambdify((rs, Fs, F1, F2, ws, w1, w2, ps, p1, p2), e, modules=_tmods) for e in _ex]


def cheb_basis(x, deg):
    """T_k(2x-1) and first two x-derivatives, k = 0..deg; x tensor (n,)."""
    y = 2 * x - 1
    T = [torch.ones_like(y), y]
    dT = [torch.zeros_like(y), torch.ones_like(y)]
    ddT = [torch.zeros_like(y), torch.zeros_like(y)]
    for k in range(2, deg + 1):
        T.append(2 * y * T[-1] - T[-2])
        dT.append(2 * T[-2] + 2 * y * dT[-1] - dT[-2])
        ddT.append(4 * dT[-2] + 2 * y * ddT[-1] - ddT[-2])
    T = torch.stack(T[:deg + 1], 1)
    dT = 2 * torch.stack(dT[:deg + 1], 1)
    ddT = 4 * torch.stack(ddT[:deg + 1], 1)
    return T, dT, ddT


class Cell:
    def __init__(self, mu, Rc, deg, nq=600, device='cpu', coord='lin'):
        self.mu, self.Rc, self.deg = mu, Rc, deg
        self.r0 = math.sqrt(mu)
        self.coord = coord
        self.ell = math.log(Rc / self.r0)
        self.L = Rc - self.r0
        s, wq = np.polynomial.legendre.leggauss(nq)
        s = (s + 1) / 2; wq = wq / 2
        self.x = torch.tensor(s**2, device=device)
        self.wx = torch.tensor(wq * 2 * s, device=device)  # dx = 2 s ds
        self.B = cheb_basis(self.x, deg)
        x = self.x
        one = 1 - x
        # envelope functions and derivatives in x
        self.env = {}
        def poly_env(c_one, c_x):  # (1-x)^c_one * x^c_x and derivatives
            f = one**c_one * x**c_x
            df = -c_one * one**(c_one - 1) * x**c_x + (c_x * one**c_one * x**(c_x - 1) if c_x > 0 else 0 * x)
            ddf = (c_one * (c_one - 1) * one**(c_one - 2) * x**c_x
                   - (2 * c_one * c_x * one**(c_one - 1) * x**(c_x - 1) if c_x > 0 else 0 * x)
                   + (c_x * (c_x - 1) * one**c_one * x**(c_x - 2) if c_x > 1 else 0 * x))
            return f, df, ddf
        self.e40 = poly_env(4, 0)
        self.e41 = poly_env(4, 1)
        self.e42 = poly_env(4, 2)
        r0, L = self.r0, self.L
        self.b0 = 1 + r0**2 / 6
        if coord == 'lin':
            self.b1 = 4 * self.b0 + L * (r0 / 3 - 2 / r0)
            self.r = r0 + L * x
            self.jac = L * torch.ones_like(x)          # dr/dx
            self.dx1 = torch.ones_like(x) / L          # dx/dr
            self.dx2 = torch.zeros_like(x)             # d2x/dr2
        else:  # x = log(r/r0)/ell
            ell = self.ell
            self.b1 = 4 * self.b0 + r0 * ell * (r0 / 3 - 2 / r0)
            self.r = r0 * torch.exp(ell * x)
            self.jac = ell * self.r
            self.dx1 = 1 / (ell * self.r)
            self.dx2 = -1 / (ell * self.r**2)

    def series(self, c, env):
        T, dT, ddT = self.B
        P, dP, ddP = T @ c, dT @ c, ddT @ c
        f, df, ddf = env
        val = f * P
        d1 = df * P + f * dP
        d2 = ddf * P + 2 * df * dP + f * ddP
        return self.to_r(val, d1, d2)

    def to_r(self, val, d1, d2):
        return val, d1 * self.dx1, d2 * self.dx1**2 + d1 * self.dx2

    def fields(self, cF, cw, cp):
        r, L = self.r, self.L
        # base part of F: F_CH - (1-x)^4 (b0 + b1 x)
        f40, d40, dd40 = self.e40
        f41, d41, dd41 = self.e41
        base, dbase, ddbase = self.to_r(self.b0 * f40 + self.b1 * f41,
                                        self.b0 * d40 + self.b1 * d41,
                                        self.b0 * dd40 + self.b1 * dd41)
        PF = self.series(cF, self.e42)
        F = 1 + r**2 / 6 - base - PF[0]
        Fr = r / 3 - dbase - PF[1]
        Frr = 1 / 3 - ddbase - PF[2]
        w = self.series(cw, self.e42)
        p = self.series(cp, self.e40)
        return (F, Fr, Frr), w, p

    def cost(self, cF, cw, cp, parts=False):
        (F, Fr, Frr), (w, wr, wrr), (p, pr, prr) = self.fields(cF, cw, cp)
        r = self.r
        e2p = torch.exp(2 * p)
        dens = 0
        comps = []
        for k in range(4):
            Rk = RIC[k](r, F, Fr, Frr, w, wr, wrr, p, pr, prr)  # e^{2p} Ric_kk
            Ek = Rk + e2p                                    # e^{2p}(Ric_kk + 1)
            comps.append(Ek)
            dens = dens + Ek**2
        integrand = r**3 * dens  # e^{4p} sum (Ric+1)^2 r^3 = r^3 sum (e^{2p}(Ric+1))^2
        j = torch.sum(self.wx * self.jac * integrand)
        # positivity of F/x
        g = F / (self.x + 1e-300)
        pen = torch.sum(torch.relu(1e-3 - g)**2) * 1e6
        if parts:
            return j, pen, (F, w, p, comps)
        return j, pen


def run(mu, Rc, deg, kahler_only=False, nophi=False, nw=True, iters=3000, seed=0, init_scale=0.0, device='cpu', coord='lin'):
    cell = Cell(mu, Rc, deg, device=device, coord=coord)
    torch.manual_seed(seed)
    n = deg + 1
    cF = (init_scale * torch.randn(n, device=device)).requires_grad_(True)
    cw = (init_scale * torch.randn(n, device=device)).requires_grad_(not kahler_only and nw)
    cp = (init_scale * torch.randn(n, device=device)).requires_grad_(not nophi)
    if kahler_only or not nw:
        cw = torch.zeros(n, device=device)
    if nophi:
        cp = torch.zeros(n, device=device)
    params = [t for t in (cF, cw, cp) if t.requires_grad]
    opt = torch.optim.LBFGS(params, lr=1, max_iter=iters, history_size=50,
                            tolerance_grad=1e-12, tolerance_change=1e-15, line_search_fn='strong_wolfe')
    def closure():
        opt.zero_grad()
        j, pen = cell.cost(cF, cw, cp)
        tot = j + pen
        tot.backward()
        return tot
    opt.step(closure)
    j, pen = cell.cost(cF, cw, cp)
    lowK = (2 + mu)**2 / (1 - mu**2 / Rc**4)
    return dict(mu=mu, Rc=Rc, deg=deg, kahler_only=kahler_only, nophi=nophi, nw=nw, coord=coord,
                j=float(j.detach()), pen=float(pen.detach()), kahler_bound=lowK,
                cF=cF.detach().cpu().tolist(), cw=cw.detach().cpu().tolist(), cp=cp.detach().cpu().tolist())


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--mu', type=float, nargs='+', default=[0.1])
    ap.add_argument('--Rc', type=float, nargs='+', default=[1.0])
    ap.add_argument('--deg', type=int, default=14)
    ap.add_argument('--iters', type=int, default=3000)
    ap.add_argument('--modes', nargs='+', default=['nophi', 'full'])
    ap.add_argument('--seeds', type=int, default=1)
    ap.add_argument('--init', type=float, default=0.0)
    ap.add_argument('--out', default='')
    ap.add_argument('--coord', default='lin')
    a = ap.parse_args()
    fh = open(a.out, 'a') if a.out else None
    for Rc in a.Rc:
        for mu in a.mu:
            for mode in a.modes:
                for sd in range(a.seeds):
                    kw = dict(kahler_only=(mode == 'biaxial'), nophi=(mode in ('nophi', 'biaxial')),
                              nw=(mode != 'phionly'))
                    res = run(mu, Rc, a.deg, iters=a.iters, seed=sd, init_scale=a.init, coord=a.coord, **kw)
                    res['mode'] = mode; res['seed'] = sd
                    line = json.dumps(res)
                    print(json.dumps({k: res[k] for k in ('mode', 'coord', 'deg', 'mu', 'Rc', 'seed', 'j', 'pen', 'kahler_bound')}), flush=True)
                    if fh:
                        fh.write(line + '\n'); fh.flush()
