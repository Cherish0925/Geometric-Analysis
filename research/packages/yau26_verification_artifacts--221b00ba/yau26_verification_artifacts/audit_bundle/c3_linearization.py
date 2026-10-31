#!/usr/bin/env python3
"""
Check of (C3): BUN:three-equations, BUN:B-solution, BUN:bianchi and auxiliary identities.

Background g0 = dt^2 + cosh^2 t dy^2 + du^2 + cosh^2 u dx^2  (Ric = -g0).
Perturbation K = A(t,u) g1 + B(u) f T1 + C(t,u) T2,  f = sech^2 t,
     T1 = dt^2 - cosh^2 t dy^2, T2 = du^2 - cosh^2 u dx^2.
We compute  DPhi_{g0}(K) = d/d eta|_0 [Ric(g0+eta K) + g0 + eta K]  DIRECTLY from the coordinate
Ricci tensor (no use of the Lichnerowicz formula), then add delta^*(bK) computed independently
(bK = -div K + (1/2) d tr K) to obtain  L K = DPhi(K) + delta^* b K, and compare with
     (1/2)[ H_A A g1 + (-P_u B) f T1 + H_C C T2 ].
"""
import sympy as sp

t, y, u, x, eta = sp.symbols('t y u x eta', real=True)
X = [t, y, u, x]
n = 4
A = sp.Function('A')(t, u); B = sp.Function('B')(u); C = sp.Function('C')(t, u)
f = sp.sech(t)**2; r = sp.sech(u)**2

g0 = sp.diag(1, sp.cosh(t)**2, 1, sp.cosh(u)**2)
K = sp.diag(A + B * f, (A - B * f) * sp.cosh(t)**2, C, -C * sp.cosh(u)**2)
g = g0 + eta * K


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


Ric_eta, _ = ricci(g)
Phi_eta = Ric_eta + g
DPhi = Phi_eta.applyfunc(lambda e: sp.diff(e, eta).subs(eta, 0))
DPhi = DPhi.applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))
# sanity: Phi(g0)=0
assert Phi_eta.subs(eta, 0).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp))) == sp.zeros(n, n)

# ---- Bianchi operator on background g0
g0inv = g0.inv()
_, Gam0 = ricci(g0)
def cov_div(h):
    # (div h)_j = g^{ik} nabla_i h_{kj}
    out = []
    for j in range(n):
        s_ = 0
        for i in range(n):
            for k in range(n):
                nab = sp.diff(h[k, j], X[i]) - sum(Gam0[m][i][k] * h[m, j] for m in range(n)) \
                      - sum(Gam0[m][i][j] * h[k, m] for m in range(n))
                s_ += g0inv[i, k] * nab
        out.append(s_)
    return out
trK = sum(g0inv[i, i] * K[i, i] for i in range(n))
divK = cov_div(K)
bK = [sp.simplify((-divK[j] + sp.diff(trK, X[j]) / 2).rewrite(sp.exp)) for j in range(n)]
claimed_bK = [0, 0, sp.diff(A, u) - sp.diff(C, u) - 2 * sp.tanh(u) * C, 0]
print("bK - claimed:", [sp.simplify((bK[j] - claimed_bK[j]).rewrite(sp.exp)) for j in range(n)])

# delta^* omega = sym nabla omega
def delta_star(om):
    M = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            ni = sp.diff(om[j], X[i]) - sum(Gam0[m][i][j] * om[m] for m in range(n))
            nj = sp.diff(om[i], X[j]) - sum(Gam0[m][j][i] * om[m] for m in range(n))
            M[i, j] = (ni + nj) / 2
    return M
LK = (DPhi + delta_star(bK)).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))

# ---- claimed form
Pt = lambda F: sp.diff(F, t, 2) + sp.tanh(t) * sp.diff(F, t)
Pu = lambda F: sp.diff(F, u, 2) + sp.tanh(u) * sp.diff(F, u)
HA = lambda F: -Pt(F) - Pu(F) + 2 * F
HC = lambda F: -Pt(F) - Pu(F) + 2 * F - 4 * r * F
H1 = lambda F: -Pt(F) - Pu(F) + 2 * F - r * F
claimed_LK = sp.Rational(1, 2) * sp.diag(HA(A) + f * (-Pu(B)), (HA(A) - f * (-Pu(B))) * sp.cosh(t)**2,
                                         HC(C), -HC(C) * sp.cosh(u)**2)
res = (LK - claimed_LK).applyfunc(lambda e: sp.simplify(e.rewrite(sp.exp)))
print("L K - (1/2)[H_A A g1 + (-P_u B) f T1 + H_C C T2] =")
sp.pprint(res)
assert res == sp.zeros(n, n)

# ---- B solution and T solution
c0 = sp.Symbol('c0', positive=True)
gd = sp.atan(sp.sinh(u))
Bsol = c0**2 / 8 * (sp.sech(u)**2 + sp.pi**2 / 4 - gd**2)
print("-P_u B - c0^2 r^2/2 =", sp.simplify((-Pu(Bsol) - c0**2 * r**2 / 2).rewrite(sp.exp)))
Tsol = sp.Rational(1, 2) * (sp.pi**2 / 4 - sp.atan(sp.sinh(t))**2)
print("-P_t T - f =", sp.simplify((-Pt(Tsol) - f).rewrite(sp.exp)))
print("H_A(T r) - (f r + 4 T r^2) =", sp.simplify((HA(Tsol * r) - (f * r + 4 * Tsol * r**2)).rewrite(sp.exp)))
print("H_C(T r) - f r =", sp.simplify((HC(Tsol * r) - f * r).rewrite(sp.exp)))
print("H_A(f B) - (c0^2 f r^2/2 + 4 f^2 B) =", sp.simplify((HA(f * Bsol) - (c0**2 * f * r**2 / 2 + 4 * f**2 * Bsol)).rewrite(sp.exp)))
print("(-P_u + 2 - 4r) r =", sp.simplify((-Pu(r) + 2 * r - 4 * r**2).rewrite(sp.exp)))

# ---- commutation identities
F = sp.Function('F')(t, u)
Du = lambda G_: sp.diff(G_, u) + 2 * sp.tanh(u) * G_
print("D_u H_C F - H_1 D_u F =", sp.simplify((Du(HC(F)) - H1(Du(F))).rewrite(sp.exp)))
print("d_u H_A F - H_1 d_u F =", sp.simplify((sp.diff(HA(F), u) - H1(sp.diff(F, u))).rewrite(sp.exp)))
print("D_u(c0^2 f r^2) - d_u(c0^2 f r^2/2) =", sp.simplify((Du(c0**2 * f * r**2) - sp.diff(c0**2 * f * r**2 / 2, u)).rewrite(sp.exp)))

# ---- b D = 0 for D = (c0^2 f r^2/2) diag(-1,0,-1,1) (ON frame)
Dm = c0**2 * f * r**2 / 2 * sp.diag(-1, 0, -1, sp.cosh(u)**2)
trD = sum(g0inv[i, i] * Dm[i, i] for i in range(n))
divD = cov_div(Dm)
print("b D =", [sp.simplify((-divD[j] + sp.diff(trD, X[j]) / 2).rewrite(sp.exp)) for j in range(n)])

# ---- fluxes
print("[cosh u B']_{-oo}^{oo} =", sp.limit(sp.cosh(u) * sp.diff(Bsol, u), u, sp.oo) - sp.limit(sp.cosh(u) * sp.diff(Bsol, u), u, -sp.oo),
      "  claimed -c0^2 pi/4")
import mpmath as mp
print("int sech^5 =", mp.quad(lambda y_: mp.sech(y_)**5, [-mp.inf, 0, mp.inf]), " 3 pi/8 =", 3*mp.pi/8)
