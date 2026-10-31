"""ITEM G: orthogonally transitive T^2 class  g = gamma_B + e^sigma M_ab dxi^a dxi^b, det M = 1.
(1) exact random-jet check of the reduced Ricci equations used in the proof of thm:OT:
      horizontal:  Ric_B - Hess(sigma) - (1/2) dsigma^2 - (1/2) U^*h  =  Ric_g|_B          (=> N = 4)
      vertical  :  tr_G Ric_fib = -L sigma,   |tau_sigma(U)|^2 = 2 |(G^{-1}Ric_fib)_0|^2_HS
(2) symbolic check of R_Sigma = -2h_s - (3/2)h^2 - (1/2)|U_s|^2 for Sigma = ds^2 + rho(s) M(s);
(3) Riccati/Fisher bound, Beta-function constant, quadratic inequality and the root eps_*;
(4) sharpness illustration on H^2 x H^2 (Ric = -3g): sup e = 6 = B(0).
"""
import functools
import numpy as np
import sympy as sp
from itemE_jets_numeric_lib import ricci_from_jets
from ricci_tools import ricci

print = functools.partial(print, flush=True)
rng = np.random.default_rng(99)

# ------------------------------------------------------------------ (1)
t, z = sp.symbols('t z', real=True)
names = ['phi', 'sig', 'X', 'Y']
J = {n: sp.symbols(f'{n}_0 {n}_t {n}_z {n}_tt {n}_tz {n}_zz') for n in names}


def poly(n):
    c = J[n]
    return c[0] + c[1] * t + c[2] * z + c[3] * t**2 / 2 + c[4] * t * z + c[5] * z**2 / 2


phi, sig, Xf, Yf = [poly(n) for n in names]
M = sp.Matrix([[1, Xf], [Xf, Xf**2 + Yf**2]]) / Yf
g = sp.zeros(4, 4)
g[0, 0] = g[1, 1] = sp.exp(2 * phi)
g[2:, 2:] = sp.exp(sig) * M
coords = [t, z, sp.Symbol('xi1'), sp.Symbol('xi2')]
dg = sp.Array([[[sp.diff(g[i, j], coords[m]) for j in range(4)] for i in range(4)] for m in range(4)])
ddg = sp.Array([[[[sp.diff(g[i, j], coords[m], coords[n]) for j in range(4)] for i in range(4)] for n in range(4)] for m in range(4)])
allsyms = [s for n in names for s in J[n]]
sub0 = {t: 0, z: 0}
f_g = sp.lambdify(allsyms, g.subs(sub0), 'numpy')
f_dg = sp.lambdify(allsyms, dg.subs(sub0), 'numpy')
f_ddg = sp.lambdify(allsyms, ddg.subs(sub0), 'numpy')

worst_h = worst_v = worst_F = 0.0
for trial in range(300):
    v = {n: rng.normal(size=6) for n in names}
    v['Y'][0] = rng.uniform(0.5, 2.0)
    vals = [x for n in names for x in v[n]]
    G4 = np.array(f_g(*vals), float); DG = np.array(f_dg(*vals), float); DDG = np.array(f_ddg(*vals), float)
    Ric4, _ = ricci_from_jets(G4, DG, DDG)
    # base geometry
    gB = G4[:2, :2]; RicB, GamB = ricci_from_jets(gB, DG[:2, :2, :2], DDG[:2, :2, :2, :2])
    gBi = np.linalg.inv(gB)

    def grad(n):
        return np.array([v[n][1], v[n][2]])

    def hess(n):
        d2 = np.array([[v[n][3], v[n][4]], [v[n][4], v[n][5]]])
        return d2 - np.einsum('kij,k->ij', GamB, grad(n))

    def lap(n):
        return np.einsum('ij,ij->', gBi, hess(n))

    def ip(n1, n2):
        return grad(n1) @ gBi @ grad(n2)
    Y0 = v['Y'][0]
    Uh = (np.outer(grad('X'), grad('X')) + np.outer(grad('Y'), grad('Y'))) / Y0**2      # U^* h_{H^2}
    horiz = RicB - hess('sig') - 0.5 * np.outer(grad('sig'), grad('sig')) - 0.5 * Uh
    worst_h = max(worst_h, np.abs(horiz - Ric4[:2, :2]).max() / (1 + np.abs(Ric4).max()))
    worst_h = max(worst_h, np.abs(Ric4[:2, 2:]).max())                                   # mixed block vanishes
    # vertical
    Gf = G4[2:, 2:]; P = np.linalg.inv(Gf) @ Ric4[2:, 2:]
    Lsig = lap('sig') + ip('sig', 'sig')
    worst_v = max(worst_v, abs(np.trace(P) + Lsig) / (1 + abs(Lsig)))
    # weighted tension field of U=(X,Y) into H^2 (curvature -1)
    LX = lap('X') + ip('sig', 'X'); LY = lap('Y') + ip('sig', 'Y')
    tauX = LX - 2 / Y0 * ip('X', 'Y'); tauY = LY + (ip('X', 'X') - ip('Y', 'Y')) / Y0
    F2 = (tauX**2 + tauY**2) / Y0**2
    P0 = P - np.trace(P) / 2 * np.eye(2)
    worst_F = max(worst_F, abs(F2 - 2 * np.trace(P0 @ P0)) / (1 + F2))
print("(1) random jets (300 trials):")
print("    horizontal identity  Ric_B - Hess sigma - dsigma^2/2 - U^*h/2 = Ric_g|_B : worst rel. err", worst_h)
print("    vertical trace       tr(G^-1 Ric_fib) = -L sigma                        : worst rel. err", worst_v)
print("    |tau_sigma(U)|^2 = 2 |(G^-1 Ric_fib)_0|_HS^2                             : worst rel. err", worst_F)
print("    => with eigenvalues of E|_fib in [-eps,eps]: |F|^2 = (mu1-mu2)^2 <= 4 eps^2, i.e. |F| <= 2 eps")
print("    Bakry-Emery: Ric_f^N = Ric + Hess f - df^2/(N-n), f=-sigma, n=2; coefficient 1/2 <=> N-n=2 <=> N=4")

# target metric normalisation: (1/2) tr (M^-1 dM)^2 = (dX^2+dY^2)/Y^2
Xs, Ys, dX, dY = sp.symbols('X Y dX dY', real=True)
Ms = sp.Matrix([[1, Xs], [Xs, Xs**2 + Ys**2]]) / Ys
dM = Ms.diff(Xs) * dX + Ms.diff(Ys) * dY
print("    (1/2)tr(M^-1 dM M^-1 dM) =", sp.simplify((Ms.inv() * dM * Ms.inv() * dM).trace() / 2))

# ------------------------------------------------------------------ (2)
s = sp.Symbol('s', real=True)
rho = sp.Function('rho', positive=True)(s); Xc = sp.Function('X')(s); Yc = sp.Function('Y', positive=True)(s)
Mc = sp.Matrix([[1, Xc], [Xc, Xc**2 + Yc**2]]) / Yc
q3 = sp.zeros(3, 3); q3[0, 0] = 1; q3[1:, 1:] = rho * Mc
R3 = sp.simplify((q3.inv() * ricci(q3, [s, sp.Symbol('xi1'), sp.Symbol('xi2')])).trace())
h = sp.diff(sp.log(rho), s)
Us2 = (Xc.diff(s)**2 + Yc.diff(s)**2) / Yc**2
print("(2) R_Sigma - (-2h_s - 3h^2/2 - |U_s|^2/2) =", sp.simplify(R3 - (-2 * h.diff(s) - sp.Rational(3, 2) * h**2 - Us2 / 2)))

# ------------------------------------------------------------------ (3)
N_, K_, tt = sp.symbols('N K t', positive=True)
Jsol = N_ * K_ / (1 - sp.exp(-2 * K_ * tt))
print("(3) Riccati: J' - (2K J - 2J^2/N) =", sp.simplify(sp.diff(Jsol, tt) - (2 * K_ * Jsol - 2 * Jsol**2 / N_)))
print("    B(1,1/2) =", sp.beta(1, sp.Rational(1, 2)).evalf(), "; sqrt(NK)/(2K)*B(1,1/2) with N=4 ->", sp.simplify(sp.sqrt(4 * K_) / (2 * K_) * 2))
from scipy import integrate, optimize  # noqa: E402
for Kv in [3.0, 3.25]:
    val, _ = integrate.quad(lambda x: np.exp(-2 * Kv * x) * np.sqrt(4 * Kv / (1 - np.exp(-2 * Kv * x))), 0, np.inf)
    print(f"    K={Kv}: int_0^inf e^(-2K t) sqrt(NK/(1-e^(-2Kt))) dt = {val:.10f}  vs 2/sqrt(K) = {2/np.sqrt(Kv):.10f}")


def Bfun(e):
    return (4 * e / np.sqrt(3 + e) + np.sqrt(2 * (3 + e) + 20 * e**2 / (3 + e)))**2


def quad_root(e):
    al = 2 * (3 + e) + 4 * e**2 / (3 + e); be = 8 * e / np.sqrt(3 + e)
    return ((be + np.sqrt(be**2 + 4 * al)) / 2)**2


print("    closed form of quadratic root equals paper's B(eps)? max diff on grid:",
      max(abs(Bfun(e) - quad_root(e)) for e in np.linspace(0, 2, 201)))
eps_star = optimize.brentq(lambda e: 12 - 8 * e - Bfun(e), 0, 1, xtol=1e-14)
print(f"    eps_* = {eps_star:.10f}   (paper: 0.24625);  in the Ric~-g normalisation: {eps_star/3:.10f}")
print("    B(0) =", Bfun(0.0), "; B increasing on grid:", bool(np.all(np.diff([Bfun(e) for e in np.linspace(0, 3, 301)]) > 0)))

# ------------------------------------------------------------------ (4)
th, ph = sp.symbols('theta phi', real=True)
psi = sp.log(sp.cosh(th) / sp.cosh(ph))
e_H2H2 = sp.simplify(3 * (sp.diff(psi, th)**2 + sp.diff(psi, ph)**2))
print("(4) H^2xH^2 scaled to Ric=-3g: e = |dU|^2 =", e_H2H2, " -> sup = 6 = B(0) (upper bound sharp at eps=0)")
