"""ITEM F: Bianchi VII_0 helical class
   g = dr^2 + a(r)^2 dz^2 + b(r)^2 w1^2 + c(r)^2 w2^2,
   w1 = cos(kz)dx + sin(kz)dy,  w2 = -sin(kz)dx + cos(kz)dy.
(1) exact 2-jet check (random jets of a,b,c; random k,z) of the full orthonormal Ricci tensor
    against the paper's formulas, incl. vanishing of all off-diagonal (Codazzi) terms;
(2) symbolic check of the auxiliary identities of eq:helical-ode;
(3) numerical stress test of the invariant region of Proposition prop:helical.
"""
import functools
import numpy as np
import sympy as sp
from itemE_jets_numeric_lib import ricci_from_jets

print = functools.partial(print, flush=True)
rng = np.random.default_rng(2026)

# ---------------------------------------------------------------- (1) jets
rho, z, k = sp.symbols('rho z k', real=True)
aj = sp.symbols('a0 a1 a2'); bj = sp.symbols('b0 b1 b2'); cj = sp.symbols('c0 c1 c2')
a = aj[0] + aj[1] * rho + aj[2] * rho**2 / 2
b = bj[0] + bj[1] * rho + bj[2] * rho**2 / 2
c = cj[0] + cj[1] * rho + cj[2] * rho**2 / 2
co, si = sp.cos(k * z), sp.sin(k * z)
theta = sp.Matrix([[1, 0, 0, 0], [0, a, 0, 0], [0, 0, b * co, b * si], [0, 0, -c * si, c * co]])
g = theta.T * theta
X = [rho, z, sp.Symbol('x'), sp.Symbol('y')]
dg = [[[sp.diff(g[i, j], X[m]) for j in range(4)] for i in range(4)] for m in range(4)]
ddg = [[[[sp.diff(g[i, j], X[m], X[n]) for j in range(4)] for i in range(4)] for n in range(4)] for m in range(4)]
args = list(aj) + list(bj) + list(cj) + [k, z, rho]
f_g = sp.lambdify(args, g, 'numpy')
f_dg = sp.lambdify(args, sp.Array(dg), 'numpy')
f_ddg = sp.lambdify(args, sp.Array(ddg), 'numpy')
f_th = sp.lambdify(args, theta, 'numpy')

worst = 0.0
for t in range(300):
    A = rng.uniform(0.4, 2.5, 3); A1 = rng.normal(size=3); A2 = rng.normal(size=3)
    vals = [A[0], A1[0], A2[0], A[1], A1[1], A2[1], A[2], A1[2], A2[2], float(rng.integers(1, 4)), rng.uniform(0, 6.28), 0.0]
    G = np.array(f_g(*vals), dtype=float); DG = np.array(f_dg(*vals), dtype=float); DDG = np.array(f_ddg(*vals), dtype=float)
    Ric, _ = ricci_from_jets(G, DG, DDG)
    fr = np.linalg.inv(np.array(f_th(*vals), dtype=float))
    RicON = fr.T @ Ric @ fr
    a0, a1, a2, b0, b1, b2, c0, c1, c2, kk = vals[:10]
    u, v, w = a1 / a0, b1 / b0, c1 / c0
    up, vp, wp = a2 / a0 - u**2, b2 / b0 - v**2, c2 / c0 - w**2
    H = u + v + w; Hp = up + vp + wp
    d = np.log(b0 / c0)
    Kc = 2 * kk**2 / a0**2 * np.sinh(d)**2
    Lc = kk**2 / a0**2 * np.sinh(2 * d)
    paper = np.diag([-Hp - (u**2 + v**2 + w**2), -Kc - up - H * u, Lc - vp - H * v, -Lc - wp - H * w])
    worst = max(worst, np.abs(RicON - paper).max() / (1 + np.abs(paper).max()))
print("(1) 300 random jets: worst relative |Ric_ON - paper| (all 16 entries, incl. mixed) =", worst)

# ---------------------------------------------------------------- (2) identities
d_, a_ = sp.symbols('d a', positive=True)
Kc = 2 * k**2 / a_**2 * sp.sinh(d_)**2
Lc = k**2 / a_**2 * sp.sinh(2 * d_)
print("(2) 2K coth d - 2L =", sp.simplify((2 * Kc * sp.cosh(d_) / sp.sinh(d_) - 2 * Lc).rewrite(sp.exp)))
print("    L/K - coth d   =", sp.simplify((Lc / Kc - sp.cosh(d_) / sp.sinh(d_)).rewrite(sp.exp)))
rr = sp.Symbol('r')
af, df = sp.Function('a')(rr), sp.Function('d')(rr)
KK = 2 * k**2 / af**2 * sp.sinh(df)**2
print("    (log K)' - (-2u + 2p coth d) =",
      sp.simplify(sp.diff(sp.log(KK), rr) - (-2 * af.diff(rr) / af + 2 * df.diff(rr) * sp.cosh(df) / sp.sinh(df))))
# Milnor-frame cross-check of slice curvature: lambda_2 = k b/(a c), lambda_3 = k c/(a b), lambda_1 = 0
b_, c_ = sp.symbols('b c', positive=True)
l1, l2, l3 = 0, k * b_ / (a_ * c_), k * c_ / (a_ * b_)
mu = [(l1 + l2 + l3) / 2 - l for l in (l1, l2, l3)]
ric = [2 * mu[1] * mu[2], 2 * mu[0] * mu[2], 2 * mu[0] * mu[1]]
dd = sp.log(b_ / c_)
tgt = [-2 * k**2 / a_**2 * sp.sinh(dd)**2, k**2 / a_**2 * sp.sinh(2 * dd), -k**2 / a_**2 * sp.sinh(2 * dd)]
print("    Milnor Ricci - diag(-K, L, -L) =", [sp.simplify((x1 - x2).rewrite(sp.exp)) for x1, x2 in zip(ric, tgt)])

# ---------------------------------------------------------------- (3) stress test
print("(3) invariant-region stress test, eps = 3/5, random residuals |e_i| <= eps")


def run(eps, kk=1.0, a_init=1.0, Rmax=3.0, n=6000):
    ph = rng.uniform(0, 2 * np.pi, size=(4, 3)); fq = rng.uniform(0.5, 25, size=(4, 3)); am = rng.dirichlet([1, 1, 1], size=4)
    sg = rng.choice([-1.0, 1.0], size=4)

    def e(i, x):
        # bounded by eps; with probability 1/2 start at the extreme value sg*eps at the centre
        return eps * np.sum(am[i] * np.cos(fq[i] * x)) * sg[i] if ph[i, 0] < np.pi else eps * np.sum(am[i] * np.sin(fq[i] * x + ph[i]))
    K00 = 6 + e(0, 0) - e(1, 0) - e(2, 0) - e(3, 0)
    d0 = np.arcsinh(np.sqrt(K00 * a_init**2 / (2 * kk**2)))
    st = np.array([np.log(a_init), d0, 0.0, 0.0, 0.0])
    h = Rmax / n

    def rhs(x, s):
        la, dd, uu, vv, ww = s
        Hh = uu + vv + ww
        Kc = 2 * kk**2 * np.exp(-2 * la) * np.sinh(dd)**2
        Lc = kk**2 * np.exp(-2 * la) * np.sinh(2 * dd)
        return np.array([uu, vv - ww, -Hh * uu + 3 - Kc - e(1, x), -Hh * vv + 3 + Lc - e(2, x), -Hh * ww + 3 - Lc - e(3, x)])
    Kprev = K00; x = 0.0; steps = 0
    for i in range(n):
        k1 = rhs(x, st); k2 = rhs(x + h / 2, st + h / 2 * k1); k3 = rhs(x + h / 2, st + h / 2 * k2); k4 = rhs(x + h, st + h * k3)
        st = st + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4); x += h; steps += 1
        if not np.all(np.isfinite(st)) or abs(st[1]) > 50 or np.abs(st).max() > 1e6:
            break
        Kc = 2 * kk**2 * np.exp(-2 * st[0]) * np.sinh(st[1])**2
        if not (st[2] < 0 and st[3] - st[4] > 0 and Kc > Kprev * (1 - 1e-12)):
            return False, x, K00
        Kprev = Kc
    return True, x, K00


bad = 0; minK0 = 1e9; rends = []
for t in range(300):
    ok, rend, K00 = run(0.6, kk=float(rng.choice([1.0, 2.0, 5.0])), a_init=rng.uniform(0.3, 3.0))
    bad += (not ok); minK0 = min(minK0, K00); rends.append(rend)
print("    300 random runs: violations of {u<0, p>0, K increasing} =", bad,
      "; min K(0) =", round(minK0, 4), "(>= 6-4eps = 3.6); median integration length =", np.median(rends))
