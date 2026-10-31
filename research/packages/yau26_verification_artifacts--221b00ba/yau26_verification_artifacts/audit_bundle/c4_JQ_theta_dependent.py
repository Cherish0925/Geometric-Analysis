#!/usr/bin/env python3
"""
(BUN:JQ) for a theta-DEPENDENT holomorphic quadratic differential on the base collar.
Base collar: dt^2 + b^2 dtheta^2, b = ell cosh t, theta in R/Z. Conformal coordinate
   sigma = gd(t)/ell,  w = sigma + i theta,  g_B = b^2 |dw|^2.
q = Re( exp(2 pi n w) dw^2 )  (n integer) is TT on the base.
Check on G = dt^2 + b^2 dtheta^2 + du^2 + a^2 (ds + z(t) zeta'(u) du)^2, a = a0 cosh u:
  tr_G Q = 0, div_G Q = 0, and DPhi_G(Q) = q(d_t,d_t) * [[v^2/2,(v_t-kv)/2],[.,-v^2/2]] on the fibre block only.
"""
import sympy as sp

t, th, u, s, sig = sp.symbols('t theta u s sigma', real=True)
ell, a0 = sp.symbols('ell a0', positive=True)
nn = sp.Symbol('n', integer=True)
X = [t, th, u, s]; n = 4
a = a0 * sp.cosh(u); b = ell * sp.cosh(t)
z = sp.Function('z')(t); zeta = sp.Function('zeta')(u)
w = z * sp.diff(zeta, u)

G = sp.zeros(4, 4)
G[0, 0] = 1; G[1, 1] = b**2
G[2, 2] = 1 + a**2 * w**2; G[2, 3] = G[3, 2] = a**2 * w; G[3, 3] = a**2

sigma_t = sp.atan(sp.sinh(t)) / ell           # d sigma = dt / b
assert sp.simplify(sp.diff(sigma_t, t) - 1 / b) == 0
amp = sp.exp(2 * sp.pi * nn * sigma_t)
co, si = sp.cos(2 * sp.pi * nn * th), sp.sin(2 * sp.pi * nn * th)
# Re(e^{2 pi n w} dw^2) = amp [ cos (dsigma^2 - dtheta^2) - sin (2 dsigma dtheta) ]
Q = sp.zeros(4, 4)
Q[0, 0] = amp * co / b**2
Q[1, 1] = -amp * co
Q[0, 1] = Q[1, 0] = -amp * si / b

def ricci(g):
    ginv = g.inv()
    Gam = [[[sum(ginv[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                 for l in range(n)) / 2 for k in range(n)] for j in range(n)] for i in range(n)]
    Ric = sp.zeros(n, n)
    for j in range(n):
        for l in range(j, n):
            Ric[j, l] = Ric[l, j] = sum(sp.diff(Gam[i][l][j], X[i]) - sp.diff(Gam[i][i][j], X[l])
                                        + sum(Gam[i][i][m] * Gam[m][l][j] - Gam[i][l][m] * Gam[m][i][j] for m in range(n))
                                        for i in range(n))
    return Ric, Gam, ginv

_, Gam0, Ginv = ricci(G)
print("tr_G Q =", sp.simplify(sum(Ginv[i, j] * Q[i, j] for i in range(n) for j in range(n))))
div = []
for j in range(n):
    s_ = 0
    for i in range(n):
        for kk in range(n):
            nab = sp.diff(Q[kk, j], X[i]) - sum(Gam0[m][i][kk] * Q[m, j] for m in range(n)) \
                  - sum(Gam0[m][i][j] * Q[kk, m] for m in range(n))
            s_ += Ginv[i, kk] * nab
    div.append(sp.simplify(s_))
print("div_G Q =", div)

Ric_s, _, _ = ricci(G + sig * Q)
DPhi = (Ric_s + G + sig * Q).applyfunc(lambda e: sp.diff(e, sig).subs(sig, 0))
E = sp.zeros(4, 4); E[0, 0] = 1; E[1, 1] = 1 / b; E[2, 2] = 1; E[3, 2] = -w; E[3, 3] = 1 / a
DPhiON = (E.T * DPhi * E).applyfunc(sp.simplify)
v = a * sp.diff(zeta, u) * sp.diff(z, t); k = sp.tanh(t)
qtt = Q[0, 0]
claimed = sp.zeros(4, 4)
claimed[2, 2] = qtt * v**2 / 2; claimed[3, 3] = -qtt * v**2 / 2
claimed[2, 3] = claimed[3, 2] = qtt * (sp.diff(v, t) - k * v) / 2
res = (DPhiON - claimed).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))
print("J_G Q (ON) - claimed (BUN:JQ) for Re(e^{2 pi n w} dw^2):")
sp.pprint(res)
