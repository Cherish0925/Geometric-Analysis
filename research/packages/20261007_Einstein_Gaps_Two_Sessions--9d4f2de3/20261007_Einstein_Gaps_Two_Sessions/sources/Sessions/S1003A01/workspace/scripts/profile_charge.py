"""Slice-charge profile T(r) along numerical cells, and an independent check of the
transgression formula against the Ricci code for conformally Kaehler (w=0) cells.

For w = 0, K = e^{-2 phi} G is U(2) Kaehler, so 4|W^+|^2_G dV_G = (s_K^2/6) dV_K
(conformal invariance of |W^+|^2 dV; Kaehler |W^+|^2 = s^2/24).  Then pointwise
  dT/dr + |Ric_G+G|^2 dV_G/dr = [ (s_G+3)^2/3 + 1 ] dV_G/dr + (s_K^2/6) dV_K/dr,
with dV/dr including the factor 2 pi^2.  We test this by finite differences of T.

Input: jsonl records with keys mu, Rc, deg, coord, cF, cw, cp.
Output: data/transgression/profile_charge.json (per record: residual of the check,
        min over r of T, min over r of T - Vol_inside, values at the collar).
Usage: python profile_charge.py FILE [FILE...] [--max N]
"""
import json, math, os, sys
import numpy as np
import torch
import sympy as sp
import cell_opt as co
import transgression_values as tv

torch.set_default_dtype(torch.float64)
here = os.path.dirname(os.path.abspath(__file__))
G = tv.load()[1]
syms = [tv.loc[k] for k in ('x', 'y', 'z', 'a1', 'b1', 'c1')]
Gf = sp.lambdify(syms, G, 'numpy')


class GridCell(co.Cell):
    def __init__(self, mu, Rc, deg, xs, coord='log'):
        super().__init__(mu, Rc, deg, nq=8, coord=coord)
        x = torch.tensor(xs)
        self.x = x
        self.B = co.cheb_basis(x, deg)
        one = 1 - x

        def poly_env(c_one, c_x):
            f = one**c_one * x**c_x
            df = -c_one * one**(c_one - 1) * x**c_x + (c_x * one**c_one * x**(c_x - 1) if c_x > 0 else 0 * x)
            ddf = (c_one * (c_one - 1) * one**(c_one - 2) * x**c_x
                   - (2 * c_one * c_x * one**(c_one - 1) * x**(c_x - 1) if c_x > 0 else 0 * x)
                   + (c_x * (c_x - 1) * one**c_one * x**(c_x - 2) if c_x > 1 else 0 * x))
            return f, df, ddf
        self.e40, self.e41, self.e42 = poly_env(4, 0), poly_env(4, 1), poly_env(4, 2)
        r0, L = self.r0, self.L
        if coord == 'lin':
            self.r = r0 + L * x
            self.dx1 = torch.ones_like(x) / L
            self.dx2 = torch.zeros_like(x)
        else:
            ell = self.ell
            self.r = r0 * torch.exp(ell * x)
            self.dx1 = 1 / (ell * self.r)
            self.dx2 = -1 / (ell * self.r**2)


def analyse(rec, npts=6001):
    xs = np.linspace(0, 1, npts)
    xs[0] = 1e-9
    cell = GridCell(rec['mu'], rec['Rc'], rec['deg'], xs, coord=rec.get('coord', 'log'))
    cF, cw, cp = [torch.tensor(rec[k]) for k in ('cF', 'cw', 'cp')]
    (F, Fr, Frr), (w, wr, wrr), (p, pr, prr) = cell.fields(cF, cw, cp)
    r = cell.r
    ric = [co.RIC[k](r, F, Fr, Frr, w, wr, wrr, p, pr, prr) for k in range(4)]
    e2p = torch.exp(2 * p)
    sG = sum(ric) / e2p
    E2 = sum((R + e2p)**2 for R in ric) / e2p**2           # |Ric+G|^2
    dVG = 2 * math.pi**2 * torch.exp(4 * p) * r**3          # dV_G/dr
    dVK = 2 * math.pi**2 * r**3
    z0 = torch.zeros_like(r)
    ricK = [co.RIC[k](r, F, Fr, Frr, z0, z0, z0, z0, z0, z0) for k in range(4)]
    sK = sum(ricK)
    u, v, pp = r * pr, r * wr, r * Fr / 2
    sq = torch.sqrt(torch.clamp(F, min=0))
    args = [torch.exp(w), torch.exp(-w), sq, sq * torch.exp(w) * (1 + u + v),
            sq * torch.exp(-w) * (1 + u - v), F * (1 + u) + pp]
    args = [a.numpy() for a in args]
    T = 2 * math.pi**2 * (Gf(*args) + 32)
    rn = r.numpy()
    dT = np.gradient(T, rn)
    lhs = dT + (E2 * dVG).numpy()
    rhs_base = (((sG + 3)**2 / 3 + 1) * dVG).numpy()
    out = {k: rec[k] for k in ('mu', 'Rc', 'j') if k in rec}
    out['w_max'] = float(w.abs().max())
    # cumulative quantities
    vol = np.concatenate([[0], np.cumsum(0.5 * (dVG.numpy()[1:] + dVG.numpy()[:-1]) * np.diff(rn))])
    H = np.concatenate([[0], np.cumsum(0.5 * ((E2 * dVG).numpy()[1:] + (E2 * dVG).numpy()[:-1]) * np.diff(rn))])
    out['T_bolt'] = float(T[1]); out['T_collar'] = float(T[-1]); out['4d'] = float(2 * math.pi**2 * rec['Rc']**4)
    out['J_from_grid'] = float(H[-1]); out['j_grid'] = float(H[-1] / (2 * math.pi**2))
    inner = slice(5, -5)
    out['min_T_over_8pi2'] = float(T[inner].min() / (8 * math.pi**2))
    out['r_at_minT'] = float(rn[inner][np.argmin(T[inner])])
    out['min_(T-Vol)_over_8pi2'] = float((T - vol)[inner].min() / (8 * math.pi**2))
    # inferred int F up to r:  H - 8pi^2 + T ; check monotone >= Vol
    intF = H - 8 * math.pi**2 + T
    out['min_d(intF)-dVol_rel'] = float(np.min(np.gradient(intF, rn)[inner] - dVG.numpy()[inner]) / float(dVG.max()))
    # zero-flux slices: Y = c' - 2cosh2w + z^2 + p+p-/2,  Pi = e^{2w}p+^2+e^{-2w}p-^2-(p+p-)^2/4
    xa, ya, za, a1, b1, c1 = args
    s_ = np.sqrt(xa * ya)
    with np.errstate(divide='ignore', invalid='ignore'):
        ppl = (ya * a1 - za + (xa**2 - ya**2) / za) / s_
        pmi = (xa * b1 - za - (xa**2 - ya**2) / za) / s_
    e2w = xa / ya
    Y = c1 - (e2w + 1 / e2w) + za**2 / (xa * ya) + ppl * pmi / 2
    Pi = e2w * ppl**2 + pmi**2 / e2w - (ppl * pmi)**2 / 4
    zs = [i for i in range(5, len(Y) - 5) if np.sign(Y[i]) != np.sign(Y[i + 1])]
    out['closed_form_err'] = float(np.nanmax(np.abs((Y**2 + Pi)[inner] * 8 * math.pi**2 - T[inner])) / (8 * math.pi**2))
    zl = []
    for i in zs:
        zl.append({'r': float(rn[i]), 'Pi': float(Pi[i]), 'Vol_over_8pi2': float(vol[i] / (8 * math.pi**2)),
                   'intF_over_8pi2': float(intF[i] / (8 * math.pi**2))})
    out['zero_flux'] = zl
    if out['w_max'] < 1e-12:
        rhs = rhs_base + ((sK**2 / 6) * dVK).numpy()
        res = (lhs - rhs)[inner]
        out['kahler_check_max_rel'] = float(np.abs(res).max() / np.abs(rhs[inner]).max())
    return out, (rn, T, H, vol)


def main():
    argv = sys.argv[1:]
    nmax = 10**9
    if '--max' in argv:
        k = argv.index('--max'); nmax = int(argv[k + 1]); argv = argv[:k] + argv[k + 2:]
    files = argv
    res = []
    for f in files:
        for i, line in enumerate(open(f)):
            if i >= nmax:
                break
            rec = json.loads(line)
            if 'cF' not in rec:
                continue
            o, _ = analyse(rec)
            o['file'] = os.path.basename(f); o['idx'] = i
            res.append(o)
            print(json.dumps(o), flush=True)
    od = os.path.join(here, '..', 'data', 'transgression')
    os.makedirs(od, exist_ok=True)
    with open(os.path.join(od, 'profile_charge.json'), 'w') as fh:
        json.dump(res, fh, indent=1)


if __name__ == '__main__':
    main()
