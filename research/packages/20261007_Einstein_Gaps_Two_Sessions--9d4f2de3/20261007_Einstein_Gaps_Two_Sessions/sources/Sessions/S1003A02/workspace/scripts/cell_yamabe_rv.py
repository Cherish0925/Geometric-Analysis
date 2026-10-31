"""Constant-scalar conformal representative and renormalized volume of marked cells.

Mathematical content (Step 23).  Let (U,g) be a complete cell which is exactly the
Ric=-6 model (H4 with K=-2, or CH2 with holomorphic curvature -4) outside a compact
set, sigma = s+24.  Let ghat = u^2 g be the complete conformal metric with
shat = -24 and u -> 1 at infinity (Loewner-Nirenberg / Aviles-McOwen solution),
i.e.  6 Lap_g u = s u + 24 u^3 .  Writing u = 1+w,

    6 Lap w = sigma (1+w) + 24 (1+w)(2w+w^2).

Multiplying by u and integrating gives the exact relative identity (all integrals
w.r.t. g, B the comparison model ball, U_int the region where g differs)

  int_{U_int} s^2/12 - 48 Vol(B)  =  48 RV(ghat) + (1/12) int (sigma+24(u^2-1))^2
                                     + 24 int |grad u|^2 ,                     (Y)
  RV(ghat) = [Vol_g(U_int) - Vol(B)] + int (u^4-1) dmu_g .

Together with P_cell - 8pi^2 = 4 Delta W+ + [int s^2/12 - 48 Vol B] this splits a
cell's cost into Weyl, renormalized-volume and two nonnegative channels.

This script evaluates every term for diagonal Bianchi-IX cells
  g = dx^2/(4G) + h1 s1^2 + h2 s2^2 + h3 s3^2 ,
solving the radial equation by a conservative finite-volume Newton scheme in
z = log x (unknown w, no cancellation), from the bolt (zero flux) to x = Xmax
(Dirichlet w=0; decay is w ~ c x^{-p}, p=2 for H4, p=1+sqrt3 for CH).
All integrals are reported divided by 8 pi^2 (cell normalization).

Inputs : H4 records from S1003A01 h4_perp_cell.py (Cell), or the CH FrozenCell
         record (perp_rigorous_enclosure.py).
Output : JSON written to --out.
Usage  : python cell_yamabe_rv.py h4 REC.json [REC2 ...] --out OUT.json [--N 3000]
         python cell_yamabe_rv.py ch REC.json --x0 3/100 --out OUT.json [--N 1500]
"""
from pathlib import Path
from fractions import Fraction
import argparse, json, sys
import numpy as np
import scipy.sparse as sps
from scipy.linalg import solve_banded

WS = Path(__file__).resolve().parents[1]
PEER = WS.parents[1] / 'S1003A01' / 'workspace'
sys.path.insert(0, str(PEER / 'scripts'))


def exterior(bg):
    if bg == 'h4':
        v = lambda x: x / (8 * np.sqrt(1 + 2 * x)); G = lambda x: x + 2 * x * x
        VB = lambda X: np.sqrt(1 + 2 * X) ** 3 / 48 - np.sqrt(1 + 2 * X) / 16 + 1 / 24
        p = 2.0
    else:
        v = lambda x: x / 8; G = lambda x: x + x * x; VB = lambda X: X * X / 16
        p = 1 + np.sqrt(3)
    return v, G, VB, p


def qgrid(N):
    return np.linspace(0, 1, N + 1)


def fill_bolt(cell, keys=('s', 'v', 'pdens')):
    """Replace node-0 (bolt, u=0) values, where the H4 formulas have a removable
    0/0, by quadratic extrapolation in u=q^2 from nodes 1..3; G vanishes there."""
    u = cell['q'][1:4] ** 2
    for k in keys:
        cell[k][0] = np.polyval(np.polyfit(u, cell[k][1:4], 2), 0.0)
    cell['G'][0] = 0.0
    return cell


def h4_interior(path, N):
    import jax; jax.config.update('jax_enable_x64', True)
    import jax.numpy as jnp
    from h4_perp_cell import Cell
    r = json.loads(Path(path).read_text())
    x0, X, deg = float(r['x0']), float(r['X']), int(r['deg'])
    c = Cell(x0, X, deg, 8)
    q = qgrid(N); u = q * q; u[0] = u[1]   # node 0 overwritten by fill_bolt
    c.u = jnp.asarray(u); c.wq = jnp.ones_like(c.u)
    pd, sd, s, dx, F, G, w = c.fields(jnp.asarray(r['z']))
    u[0] = 0.0; x = x0 * np.exp(c.ell * u)
    F, G, w, s, pd = (np.array(t) for t in (F, G, w, s, pd))
    v = np.sqrt(F) * x * np.exp(w / 2) / (8 * np.sqrt(G))
    jac = c.ell * x * 2 * q            # dx/dq
    return fill_bolt(dict(bg='h4', x0=x0, X=X, q=q, x=x, v=v, G=G, s=s, pdens=pd, jac=jac,
                source=str(path), P_record=r.get('P')))


def ch_interior(path, x0s, N):
    from flint import arb, acb, ctx
    from perp_rigorous_enclosure import FrozenCell
    ctx.prec = 96
    r = json.loads(Path(path).read_text())
    c = FrozenCell(r); fr = Fraction(x0s)
    c.x0 = arb(fr.numerator) / fr.denominator; c.ell = (c.X / c.x0).log()
    q = qgrid(N); u = q * q
    xs, vs, Gs, ss, ps = [], [], [], [], []
    ell = float(c.ell.mid()); x0 = float(fr)
    for uu in u:
        R, vol, prof = c.ricci(acb(arb(float(uu))), want_profile=True)
        Rr = [float(t.real.mid()) for t in R]; sc = sum(Rr)
        x = float(prof['x'].real.mid()); vdu = float(vol.real.mid())
        xs.append(x); vs.append(vdu / (ell * x)); Gs.append(float(prof['G'].real.mid()))
        ss.append(sc); ps.append(vdu / (ell * x) * sum((t - sc / 4) ** 2 for t in Rr))
    x = np.array(xs)
    return dict(bg='ch', x0=x0, X=float(r['X']), q=q, x=x, v=np.array(vs), G=np.array(Gs),
                s=np.array(ss), pdens=np.array(ps), jac=ell * x * 2 * q, source=str(path),
                P_record=r.get('P'))


def trap(f, t):
    return float(np.sum((f[1:] + f[:-1]) * np.diff(t)) / 2)


def simpson(f, q):
    """Composite Simpson on a uniform grid with an even number of intervals."""
    h = q[1] - q[0]; assert (len(q) - 1) % 2 == 0
    return float(h / 3 * (f[0] + f[-1] + 4 * f[1:-1:2].sum() + 2 * f[2:-1:2].sum()))


def solve(cell, Xmax=1e12, hz=0.01, tol=1e-15):
    vE, GE, VB, p = exterior(cell['bg'])
    xi = cell['x']; X = cell['X']
    ze = np.arange(np.log(X), np.log(Xmax) + hz, hz)[1:]
    z = np.r_[np.log(xi), ze]; x = np.exp(z)
    v = np.r_[cell['v'], vE(x[len(xi):])]; G = np.r_[cell['G'], GE(x[len(xi):])]
    sig = np.r_[cell['s'] + 24, np.zeros(len(ze))]
    A = v * 4 * G / x; vx = v * x
    h = np.diff(z); Am = (A[1:] + A[:-1]) / 2
    D = np.zeros_like(z); D[:-1] += h / 2; D[1:] += h / 2
    n = len(z); w = np.zeros(n)
    f = lambda w: sig * (1 + w) + 24 * (1 + w) * (2 * w + w * w)
    fp = lambda w: sig + 24 * (2 + 6 * w + 3 * w * w)
    for it in range(60):
        flux = 6 * Am * np.diff(w) / h
        Rz = np.zeros(n); Rz[:-1] += flux; Rz[1:] -= flux
        Rz -= vx * D * f(w)
        Rz[-1] = w[-1]
        c = 6 * Am / h
        main = np.zeros(n); main[:-1] -= c; main[1:] -= c; main -= vx * D * fp(w)
        lo = c.copy(); up = c.copy(); lo[-1] = 0.0; main[-1] = 1.0
        # row scaling: the coefficients grow like x^2 (CH) or x^1.5 (H4)
        sc = 1.0 / np.abs(main)
        ab = np.zeros((3, n)); ab[0, 1:] = up * sc[:-1]; ab[1] = main * sc; ab[2, :-1] = lo * sc[1:]
        dw = solve_banded((1, 1), ab, -Rz * sc); w += dw
        if np.max(np.abs(dw)) < tol: break
    u2m1 = 2 * w + w * w; u4m1 = 4 * w + 6 * w ** 2 + 4 * w ** 3 + w ** 4
    nI = len(xi)
    def full(g):   # g = integrand per dx on the full grid; Simpson inside, trapezoid outside
        return simpson(g[:nI] * cell['jac'], cell['q']) + trap((g * x)[nI - 1:], z[nI - 1:])
    I4 = full(v * u4m1)
    grad = float(np.sum(Am * np.diff(w) ** 2 / h))
    Q1 = full(v * (sig + 24 * u2m1) ** 2) / 12
    qq, jac = cell['q'], cell['jac']
    vB = vE(xi)                     # model-ball density at the same x
    dV = simpson((cell['v'] - vB) * jac, qq)
    RVg = dV - VB(cell['x0'])       # Vol_g(U_int) - Vol(B), B = {0<=x<=X}
    Sc = simpson((cell['v'] * cell['s'] ** 2 / 12 - 48 * vB) * jac, qq) - 48 * VB(cell['x0'])
    Prec = simpson(cell['pdens'] * jac, qq)
    RVh = RVg + I4
    rhs = 48 * RVh + Q1 + 24 * grad
    k = np.searchsorted(x, 1e6)
    return dict(source=cell['source'], background=cell['bg'], x0=cell['x0'], X=X,
                newton_iterations=it + 1, P=Prec, P_record=cell['P_record'],
                scalar_channel=Sc, RV_g=RVg, int_u4m1=I4, RV_hat=RVh,
                Q_square=Q1, Q_grad=24 * grad, identity_rhs=rhs, identity_residual=Sc - rhs,
                fourWplus_rel=Prec - 1 - Sc, w_bolt=float(w[0]), w_min=float(w.min()),
                w_max=float(w.max()), decay_coeff_c=float(w[k] * x[k] ** p), decay_power=p,
                sigma_min=float(sig[:nI].min()), sigma_max=float(sig[:nI].max()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('bg', choices=['h4', 'ch']); ap.add_argument('paths', nargs='+')
    ap.add_argument('--out', required=True); ap.add_argument('--N', type=int, default=3000)
    ap.add_argument('--x0', default='3/100')
    a = ap.parse_args(); rows = []
    for pth in a.paths:
        for N in (a.N, 2 * a.N):
            cell = h4_interior(pth, N) if a.bg == 'h4' else ch_interior(pth, a.x0, N)
            r = solve(cell); r['N'] = N; rows.append(r)
            print(json.dumps({k: r[k] for k in ['source', 'N', 'P', 'scalar_channel', 'RV_g', 'RV_hat',
                                               'Q_square', 'Q_grad', 'identity_residual',
                                               'fourWplus_rel', 'w_bolt', 'decay_coeff_c']}), flush=True)
    Path(a.out).write_text(json.dumps(dict(normalization='Ric=-6 cell scale; integrals / 8pi^2',
                                           rows=rows), indent=1) + '\n')


if __name__ == '__main__':
    main()
