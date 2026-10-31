#!/usr/bin/env python3
"""
Checks for (C4): BUN:global-pairings, BUN:JQ (used for ||J_G Q||_1), BUN:critical-pairing ingredients.

1. For G = dt^2 + b^2 dtheta^2 + du^2 + a^2(ds + z zeta' du)^2 (a''=a, b''=b) and the pulled-back
   base tensors  Q1 = (kappa/b^2)(dt^2 - b^2 dtheta^2),  Q2 = (kappa/b^2)(dt (b dtheta) + (b dtheta) dt)
   (= Re, Im of the theta-independent holomorphic quadratic differential on the collar):
   - tr_G Q = 0 and div_G Q = 0 on the SHEARED background;
   - DPhi_G(Q) = d/dsigma Phi(G + sigma Q) (computed from coordinates) equals the manuscript's
     (BUN:JQ):  q_tt * [[v^2/2,(v_t-kv)/2],[(v_t-kv)/2,-v^2/2]] on the fibre block, zero elsewhere.
2. Constants in (BUN:global-pairings) by quadrature.
"""
import sympy as sp
import mpmath as mp

t, th, u, s, sig, kappa = sp.symbols('t theta u s sigma kappa', real=True)
X = [t, th, u, s]; n = 4
a = sp.Function('a')(u); b = sp.Function('b')(t); z = sp.Function('z')(t); zeta = sp.Function('zeta')(u)
w = z * sp.diff(zeta, u)

def metric():
    g = sp.zeros(4, 4)
    g[0, 0] = 1; g[1, 1] = b**2
    g[2, 2] = 1 + a**2 * w**2; g[2, 3] = g[3, 2] = a**2 * w; g[3, 3] = a**2
    return g

def ricci(g):
    ginv = g.inv()
    Gam = [[[sum(ginv[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                 for l in range(n)) / 2 for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n, n)
    for j in range(n):
        for l in range(j, n):
            val = sum(sp.diff(Gam[i][l][j], X[i]) - sp.diff(Gam[i][i][j], X[l])
                      + sum(Gam[i][i][m] * Gam[m][l][j] - Gam[i][l][m] * Gam[m][i][j] for m in range(n))
                      for i in range(n))
            Ric[j, l] = Ric[l, j] = val
    return Ric, Gam

ap = sp.diff(a, u); bp = sp.diff(b, t)
def impose(expr):
    expr = expr.subs(sp.Derivative(a, (u, 4)), a).subs(sp.Derivative(a, (u, 3)), ap).subs(sp.Derivative(a, (u, 2)), a)
    expr = expr.subs(sp.Derivative(b, (t, 4)), b).subs(sp.Derivative(b, (t, 3)), bp).subs(sp.Derivative(b, (t, 2)), b)
    return sp.simplify(expr)

G = metric()
E = sp.zeros(4, 4); E[0, 0] = 1; E[1, 1] = 1 / b; E[2, 2] = 1; E[3, 2] = -w; E[3, 3] = 1 / a
Ginv = sp.simplify(G.inv())
_, Gam0 = ricci(G)

Q1 = sp.zeros(4, 4); Q1[0, 0] = kappa / b**2; Q1[1, 1] = -kappa
Q2 = sp.zeros(4, 4); Q2[0, 1] = Q2[1, 0] = kappa / b

v = a * sp.diff(zeta, u) * sp.diff(z, t); k = bp / b
for name, Q, qtt in [("Q1 (Re)", Q1, kappa / b**2), ("Q2 (Im)", Q2, 0)]:
    tr = sp.simplify(sum(Ginv[i, j] * Q[i, j] for i in range(n) for j in range(n)))
    div = []
    for j in range(n):
        s_ = 0
        for i in range(n):
            for kk in range(n):
                nab = sp.diff(Q[kk, j], X[i]) - sum(Gam0[m][i][kk] * Q[m, j] for m in range(n)) \
                      - sum(Gam0[m][i][j] * Q[kk, m] for m in range(n))
                s_ += Ginv[i, kk] * nab
        div.append(impose(sp.simplify(s_)))
    print(name, ": tr_G Q =", tr, "  div_G Q =", div)
    Ric_s, _ = ricci(G + sig * Q)
    DPhi = (Ric_s + G + sig * Q).applyfunc(lambda e: sp.diff(e, sig).subs(sig, 0))
    DPhiON = (E.T * DPhi * E).applyfunc(lambda e: impose(sp.simplify(e)))
    claimed = sp.zeros(4, 4)
    claimed[2, 2] = qtt * v**2 / 2; claimed[3, 3] = -qtt * v**2 / 2
    claimed[2, 3] = claimed[3, 2] = qtt * (sp.diff(v, t) - k * v) / 2
    res = (DPhiON - claimed).applyfunc(lambda e: impose(sp.simplify(e)))
    print("   J_G Q (ON) - claimed (BUN:JQ):"); sp.pprint(res)

# ---------------- constants
S1 = mp.quad(lambda y: mp.sech(y), [-mp.inf, 0, mp.inf]); S3 = mp.quad(lambda y: mp.sech(y)**3, [-mp.inf, 0, mp.inf])
print("\nint |Q|_* dV /(beta (p-1))      = 4 pi * 2 * int sech =", 4 * mp.pi * 2 * S1, "  claimed 8 pi^2 =", 8 * mp.pi**2)
print("||Q||_2^2 /(beta (p-1))         = 4 pi * 2 * int sech^3 =", 4 * mp.pi * 2 * S3, "  claimed 4 pi^2 =", 4 * mp.pi**2)
c = 1 / ((mp.pi / 2) * mp.pi)
print("int <Phi,Q> /(eps^3 beta)       = -(1/2) c^2 (int sech^3)^2 =", -c**2 * S3**2 / 2, "  claimed -1/(2 pi^2) =", -1 / (2 * mp.pi**2))
print("sharp lower constant (p-1)*liminf delta/eps^3 =", (1 / (2 * mp.pi**2)) / (8 * mp.pi**2), "  claimed 1/(16 pi^4) =", 1 / (16 * mp.pi**4))
