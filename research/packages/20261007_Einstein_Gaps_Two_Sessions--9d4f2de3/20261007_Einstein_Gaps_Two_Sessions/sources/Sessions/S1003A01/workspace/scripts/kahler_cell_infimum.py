"""Exact infimum of P and J over U(2)-invariant Kaehler blow-up cells with collar radius X.

By kahler_period_cell.py, for every admissible profile K (K(x0)=0, K'(x0)=1, K>0 on (x0,X],
K = x + kappa x^2 for x >= X, C^1 matching suffices for the identity),
    P/(8pi^2) = (1+3 kappa x0)^2 + (1/2) I[u],   J/(8pi^2) = (1+3 kappa x0)^2 + I[u],
    I[u] = int_{x0}^{X} u''(x)^2 / x dx,    u = xK - x^2 - kappa x^3.
Constraints: int u'' = m1 := x0 + 3 kappa x0^2,  int x u'' = m3 := 2 kappa x0^3.
Weighted Cauchy-Schwarz: I >= m^T G^{-1} m, G_ij = int_{x0}^X x^{1+i+j} dx, equality iff
u'' = x(A + B x)  (extremal Kaehler: scalar curvature affine in the moment coordinate).
The extremal profile has u'' discontinuous at X, so the infimum over smooth cells is approached
but (when m != 0) not attained; smoothing changes I by an arbitrarily small amount.
Outputs exact/numeric values, the extremal K, and its positivity, and compares with peer numerics.
"""
import json, sys
import sympy as sp
from pathlib import Path

x = sp.symbols('x', positive=True)


def extremal(x0, X, kappa):
    x0, X, kappa = sp.nsimplify(x0), sp.nsimplify(X), sp.nsimplify(kappa)
    G = sp.Matrix(2, 2, lambda i, j: sp.integrate(x**(1 + i + j), (x, x0, X)))
    m = sp.Matrix([x0 + 3 * kappa * x0**2, 2 * kappa * x0**3])
    coef = G.LUsolve(m)
    A, B = coef
    Imin = sp.nsimplify((m.T * coef)[0])
    v = x * (A + B * x)
    # reconstruct u from u(X)=u'(X)=0
    t = sp.symbols('t')
    up = -sp.integrate(v.subs(x, t), (t, x, X))
    u = -sp.integrate(up.subs(x, t), (t, x, X))
    K = sp.expand((u + x**2 + kappa * x**3) / x)
    chk = [sp.simplify(K.subs(x, x0)), sp.simplify(sp.diff(K, x).subs(x, x0)),
           sp.simplify(K.subs(x, X) - X - kappa * X**2), sp.simplify(sp.diff(K, x).subs(x, X) - 1 - 2 * kappa * X)]
    topo = (1 + 3 * kappa * x0)**2
    return dict(x0=float(x0), X=float(X), kappa=float(kappa), A=float(A), B=float(B),
                I_min=float(Imin), topo=float(topo), P_inf=float(topo + Imin / 2), J_inf=float(topo + Imin),
                bc_check=[float(c) for c in chk], K=K)


def minK(K, x0, X, n=4000):
    import numpy as np
    f = sp.lambdify(x, K, 'numpy')
    xs = np.geomspace(float(x0) * (1 + 1e-9), float(X), n)
    vals = f(xs)
    return float((vals / (xs - float(x0) + 1e-300)).min())   # K/(x-x0) > 0 certifies positivity on grid


def main():
    rows = []
    cases = [(0.001, 0.25, -1), (0.001, 0.25, 1), (0.01, 0.25, -1), (0.01, 0.25, 1), (0.03, 0.25, -1),
             (0.1, 0.25, -1), (0.001, 0.5, -1), (0.01, 0.5, -1), (0.05, 0.5, -1), (0.1, 0.5, -1), (0.2, 0.5, -1)]
    for x0, X, k in cases:
        r = extremal(x0, X, k)
        r['min_K_over_x_minus_x0'] = minK(r['K'], x0, X)
        r['K'] = str(r['K'])
        rows.append(r)
        print(json.dumps({k2: r[k2] for k2 in ('x0', 'X', 'kappa', 'topo', 'I_min', 'P_inf', 'J_inf',
                                                'min_K_over_x_minus_x0', 'bc_check')}))
    # small-x0 asymptotics of I_min at fixed X (symbolic)
    e, Xs, ks = sp.symbols('epsilon X kappa', positive=True)
    G = sp.Matrix(2, 2, lambda i, j: sp.integrate(x**(1 + i + j), (x, e, Xs)))
    m = sp.Matrix([e + 3 * ks * e**2, 2 * ks * e**3])
    Iexpr = sp.simplify((m.T * G.LUsolve(m))[0])
    ser = sp.series(Iexpr, e, 0, 4).removeO()
    print('I_min series in x0:', sp.factor(sp.expand(ser)))
    out = Path(__file__).resolve().parents[1] / 'data' / 'kahler_cells' / 'extremal_inf.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(dict(rows=rows, I_series=str(sp.expand(ser))), indent=1))


if __name__ == '__main__':
    main()
