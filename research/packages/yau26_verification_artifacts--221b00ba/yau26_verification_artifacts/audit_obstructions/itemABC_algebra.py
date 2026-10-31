"""Audit of Items A, B, C: pointwise algebra over the Ricci-eigenvalue box,
the Seiberg-Witten window Phi(r), and the BCG degree-two threshold.
"""
import itertools
import numpy as np
import sympy as sp

print("=" * 70)
print("ITEM A: F = s^2/24 - |E|^2/2 over the box rho_i in [1-e, 1+e]")
e = sp.symbols('e', positive=True)
rho = sp.symbols('rho1:5', real=True)
s = sum(rho)
E2 = sum(r**2 for r in rho) - s**2 / 4
F = sp.expand(s**2 / 24 - E2 / 2)
print("F == s^2/6 - |Ric|^2/2 :", sp.simplify(F - (s**2 / 6 - sum(r**2 for r in rho) / 2)) == 0)
# concavity in each variable separately
print("d^2F/drho_i^2 =", [sp.diff(F, r, 2) for r in rho])
vals = {}
for m in range(5):
    sub = {rho[i]: (1 + e if i < m else 1 - e) for i in range(4)}
    vals[m] = sp.factor(F.subs(sub))
    print(f"  vertex with m={m} high eigenvalues: F =", vals[m])
paper = sp.Rational(2, 3) * (1 - e)**2 - 2 * e**2
print("paper bracket   :", sp.expand(paper), " root:", sp.solve(paper, e))
print("paper bracket <= true min (m=1)?  diff =", sp.factor(vals[1] - paper), "(>=0)")
print("paper bracket <= m=0 value?      diff =", sp.factor(vals[0] - paper), "(>=0)")
print("true min switches from m=0 to m=1 at e =", sp.solve(sp.Eq(vals[0], vals[1]), e))
print("sharp pointwise threshold (m=1 root):", sp.solve(vals[1], e))
print("1/(1+sqrt3) =", float(1 / (1 + sp.sqrt(3))))

# brute-force numerical confirmation
rng = np.random.default_rng(0)
for eps in [0.1, 0.3, 0.36, 0.45]:
    x = 1 + eps * (2 * rng.random((400000, 4)) - 1)
    # add vertices
    verts = np.array(list(itertools.product([1 - eps, 1 + eps], repeat=4)))
    x = np.vstack([x, verts])
    S = x.sum(1)
    Fv = S**2 / 6 - (x**2).sum(1) / 2
    exact = min(2 / 3 * (1 - eps)**2, 2 / 3 * (1 + eps) * (1 - 2 * eps))
    print(f"  eps={eps}: numeric min F={Fv.min():.6f}, formula={exact:.6f}, paper lower bd={2/3*(1-eps)**2-2*eps**2:.6f}")

# normalisation check of the Chern-Gauss-Bonnet formula on model spaces
print("CGB normalisation checks:")
print("  S^4 (sec=1): chi =", sp.Rational(1, 8) / sp.pi**2 * sp.Rational(144, 24) * sp.Rational(8, 3) * sp.pi**2)
# CP^2 Fubini-Study: Ric=6g, s=24, Vol=pi^2/2, |W+|^2=s^2/24, W-=0, E=0
print("  CP^2: 2chi+3tau =", (2 * sp.Rational(24**2, 24) + sp.Rational(24**2, 24)) * sp.pi**2 / 2 / (4 * sp.pi**2))
# S^2(1) x Sigma_g(-1): s=0, W=0, |E|^2=4, Vol=4pi*4pi(g-1)
g_ = sp.symbols('g')
print("  S^2 x Sigma_g: chi =", sp.simplify((-sp.Rational(4, 2)) * 16 * sp.pi**2 * (g_ - 1) / (8 * sp.pi**2)), " expected", sp.expand(2 * (2 - 2 * g_)))

print("=" * 70)
print("ITEM B: |E|^2/s^2 over the box and Phi(r)")
d = sp.symbols('delta', positive=True)
for m in range(5):
    y = [(1 + d) if i < m else (1 - d) for i in range(4)]
    val = sp.factor(sum(v**2 for v in y) / sum(y)**2 - sp.Rational(1, 4))
    print(f"  m={m}: |E|^2/s^2 =", val)
A1 = d**2 / 4
A2 = 3 * d**2 / (4 * (2 - d)**2)
print("  crossover A1=A2 at delta =", sp.solve(sp.Eq(A1, A2), d), " (2-sqrt3 =", float(2 - sp.sqrt(3)), ")")
r = sp.symbols('r', positive=True)
print("  invert r=8*A1:", sp.solve(sp.Eq(r, 8 * A1), d))
print("  invert r=8*A2:", [sp.simplify(sol) for sol in sp.solve(sp.Eq(r, 8 * A2), d)])
r0 = 2 * (2 - sp.sqrt(3))**2
Phi1 = sp.sqrt(r / 2)
Phi2 = 2 * sp.sqrt(r) / (sp.sqrt(6) + sp.sqrt(r))
print("  breakpoint r0 =", sp.nsimplify(sp.expand(r0)), "=", float(r0))
print("  Phi1(r0) - (2-sqrt3) =", sp.simplify(Phi1.subs(r, r0) - (2 - sp.sqrt(3))))
print("  Phi2(r0) - (2-sqrt3) =", sp.simplify(Phi2.subs(r, r0) - (2 - sp.sqrt(3))))
print("  Phi2(2/3) =", sp.simplify(Phi2.subs(r, sp.Rational(2, 3))))
# numeric: maximum of |E|^2/s^2 over box vs A(delta)
for dd in [0.1, 0.2, 2 - 3**0.5, 0.3, 0.45]:
    y = 1 + dd * (2 * rng.random((400000, 4)) - 1)
    y = np.vstack([y, np.array(list(itertools.product([1 - dd, 1 + dd], repeat=4)))])
    q = (y**2).sum(1) / y.sum(1)**2 - 0.25
    Aform = max(dd**2 / 4, 3 * dd**2 / (4 * (2 - dd)**2))
    print(f"  delta={dd:.4f}: numeric max={q.max():.8f}, A(delta)={Aform:.8f}")
# the ratio step:  E/I >= 3r  given  E>=8pi^2 c r,  I=4pi^2 T+E/2,  T=c(2/3-r)
c, Ecal = sp.symbols('c Ecal', positive=True)
T = c * (sp.Rational(2, 3) - r)
ratio = Ecal / (4 * sp.pi**2 * T + Ecal / 2)
print("  d(ratio)/dEcal =", sp.simplify(sp.diff(ratio, Ecal)), " (sign = sign of T)")
print("  ratio at Ecal=8pi^2 c r :", sp.simplify(ratio.subs(Ecal, 8 * sp.pi**2 * c * r)))
# example
m_ = sp.symbols('m', positive=True, integer=True)
cc = 24 * m_
K = 8 * m_ + 1
rr = sp.simplify(K / cc - sp.Rational(1, 3))
print("  example: r =", rr, " Phi =", sp.simplify(sp.sqrt(rr / 2)), " vs 1/sqrt(48m)")

print("=" * 70)
print("ITEM C: BCG degree-two threshold")
x = sp.symbols('x1:5', real=True)
Fc = sp.Rational(3, 2) * (sum(x)**2 - 3 * sum(v**2 for v in x))
ricc = [-3 * v for v in x]
sC = sum(ricc)
E2C = sum(v**2 for v in ricc) - sC**2 / 4
print("  identity s^2/24-|E|^2/2 == (3/2)[(sum x)^2-3 sum x^2]:", sp.simplify(sC**2 / 24 - E2C / 2 - Fc) == 0)
for m in range(5):
    sub = {x[i]: (1 + e if i < m else 1 - e) for i in range(4)}
    print(f"  m={m}:", sp.factor(Fc.subs(sub)))
chi = sp.symbols('chi', positive=True)
VN = 4 * sp.pi**2 / 3 * chi
lower = 2 * VN / (1 + e)**2
upper = 8 * sp.pi**2 * (2 * chi - 2) / (6 * (1 - e)**2)
print("  upper == 2V_N(1-1/chi)/(1-e)^2 :", sp.simplify(upper - 2 * VN * (1 - 1 / chi) / (1 - e)**2) == 0)
qq = sp.sqrt(1 - 1 / chi)
eps_chi = (1 - qq) / (1 + qq)
print("  at eps_chi: lower-upper =", sp.simplify((lower - upper).subs(e, eps_chi)))
print("  series:", sp.series(eps_chi.subs(chi, 1 / r), r, 0, 3))
for cn in [2, 4, 10, 16]:
    print(f"  chi_N={cn}: eps_chi = {float(eps_chi.subs(chi, cn)):.9f}")
print("  3-2sqrt2 =", float(3 - 2 * sp.sqrt(2)))
