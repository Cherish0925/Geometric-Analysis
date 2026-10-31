#!/usr/bin/env python3
"""
Independent check of (C1): BUN:slow / BUN:ricci-matrix / BUN:slow-bound
in 20260912.tex (chapter BUN:chapter).

Metric (on base-collar x fiber-collar):
    G = dt^2 + b(t)^2 dtheta^2 + du^2 + a(u)^2 ( ds + z(t) zeta'(u) du )^2
Coordinates (t, theta, u, s).  Generic functions a,b,z,zeta.  The curvature is
computed FROM THE COORDINATE METRIC (Christoffel -> Riemann -> Ricci), not from
structure equations, and only afterwards expressed in the orthonormal frame
    e_0 = d_t, e_1 = b^{-1} d_theta, e_2 = d_u - z zeta' d_s, e_3 = a^{-1} d_s
dual to (dt, b dtheta, du, a(ds + z zeta' du)).

Checks performed
  1. h_z is hyperbolic (K=-1) for EVERY z when a''=a; area form independent of z.
  2. Full 4x4 matrix Phi = Ric + G in the ON frame, with a''=a, b''=b imposed,
     equals the manuscript's boxed matrix (including both mixed entries).
  3. Without imposing a''=a, b''=b: the generic defect (so we see exactly where the
     normalisation K_F = K_B = -1 enters).
  4. scalar curvature = -4 - v^2/2 ; sectional curvature K(e0,e3) = v^2/4.
  5. Eigenvalues / operator norm of the defect matrix; triangle-inequality bound.
  6. Numerical sup of the exact operator norm for an explicit compactly-supported
     profile pair (zeta, eta) and several L, compared with the claimed bound
     (BUN:slow-bound) and with the 1/L scaling.
"""
import sympy as sp
import numpy as np

t, th, u, s = sp.symbols('t theta u s', real=True)
X = [t, th, u, s]
a = sp.Function('a')(u)
b = sp.Function('b')(t)
z = sp.Function('z')(t)
zeta = sp.Function('zeta')(u)

w = z * sp.diff(zeta, u)         # the coefficient in (ds + w du)

# coordinate metric
g = sp.zeros(4, 4)
g[0, 0] = 1
g[1, 1] = b**2
g[2, 2] = 1 + a**2 * w**2
g[2, 3] = g[3, 2] = a**2 * w
g[3, 3] = a**2
ginv = sp.simplify(g.inv())
n = 4


def christoffel(g, ginv):
    Gam = [[[0] * n for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                Gam[i][j][k] = sp.simplify(sum(
                    ginv[i, l] * (sp.diff(g[l, j], X[k]) + sp.diff(g[l, k], X[j]) - sp.diff(g[j, k], X[l]))
                    for l in range(n)) / 2)
    return Gam


def riemann(Gam):
    # R^i_{jkl} = d_k Gam^i_{lj} - d_l Gam^i_{kj} + Gam^i_{km} Gam^m_{lj} - Gam^i_{lm} Gam^m_{kj}
    R = [[[[0] * n for _ in range(n)] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    R[i][j][k][l] = sp.diff(Gam[i][l][j], X[k]) - sp.diff(Gam[i][k][j], X[l]) + sum(
                        Gam[i][k][m] * Gam[m][l][j] - Gam[i][l][m] * Gam[m][k][j] for m in range(n))
    return R


Gam = christoffel(g, ginv)
Rm = riemann(Gam)
Ric = sp.zeros(4, 4)
for j in range(n):
    for l in range(n):
        Ric[j, l] = sp.simplify(sum(Rm[i][j][i][l] for i in range(n)))

# orthonormal frame vectors (columns = components in coordinate basis)
E = sp.zeros(4, 4)
E[0, 0] = 1
E[1, 1] = 1 / b
E[2, 2] = 1
E[3, 2] = -w
E[3, 3] = 1 / a
assert sp.simplify(E.T * g * E - sp.eye(4)) == sp.zeros(4, 4), "frame not orthonormal"

RicON = sp.simplify(E.T * Ric * E)
PhiON_generic = sp.simplify(RicON + sp.eye(4))

# ------------------------------------------------------------------ check 1
hz = sp.Matrix([[1 + a**2 * w**2, a**2 * w], [a**2 * w, a**2]])
print("det h_z =", sp.simplify(hz.det()), " (z-independent => dA_{h_z}=dA_{h_0})")
# Gaussian curvature of 2-metric h_z at frozen z: use Brioschi via a quick 2D Riemann computation
zz = sp.Symbol('z0', real=True)
h2 = hz.subs(z, zz)
Y = [u, s]
h2inv = sp.simplify(h2.inv())
G2 = [[[sp.simplify(sum(h2inv[i, l] * (sp.diff(h2[l, j], Y[k]) + sp.diff(h2[l, k], Y[j]) - sp.diff(h2[j, k], Y[l]))
                        for l in range(2)) / 2) for k in range(2)] for j in range(2)] for i in range(2)]
def R2(i, j, k, l):
    return sp.diff(G2[i][l][j], Y[k]) - sp.diff(G2[i][k][j], Y[l]) + sum(
        G2[i][k][m] * G2[m][l][j] - G2[i][l][m] * G2[m][k][j] for m in range(2))
R_usus = sum(h2[0, i] * R2(i, 1, 0, 1) for i in range(2))   # R_{u s u s}
Kgauss = sp.simplify(R_usus / h2.det())
print("Gauss curvature of h_z (generic a):", Kgauss, " -> equals -a''/a")
print("   with a = a0 cosh u:", sp.simplify(Kgauss.subs(a, sp.Symbol('a0') * sp.cosh(u)).doit()))

# ------------------------------------------------------------------ check 2
ap, app = sp.diff(a, u), sp.diff(a, u, 2)
bp, bpp = sp.diff(b, t), sp.diff(b, t, 2)
Q = a * sp.diff(zeta, u)
v = Q * sp.diff(z, t)
j = ap / a
k = bp / b
claimed = sp.Matrix([
    [-v**2 / 2, 0, 0, (sp.diff(v, u) + 2 * j * v) / 2],
    [0, 0, 0, 0],
    [0, 0, -v**2 / 2, -(sp.diff(v, t) + k * v) / 2],
    [(sp.diff(v, u) + 2 * j * v) / 2, 0, -(sp.diff(v, t) + k * v) / 2, v**2 / 2]])

# impose a''=a, a'''=a', b''=b (curvature -1 on both factors)
def impose(expr):
    expr = expr.subs(sp.Derivative(a, (u, 3)), ap).subs(sp.Derivative(a, (u, 2)), a)
    expr = expr.subs(sp.Derivative(b, (t, 3)), bp).subs(sp.Derivative(b, (t, 2)), b)
    return sp.simplify(expr)

diff_mat = (PhiON_generic - claimed).applyfunc(impose)
print("\n[check 2] Phi_ON(computed from coordinates) - claimed matrix, with a''=a, b''=b:")
sp.pprint(diff_mat)
assert diff_mat == sp.zeros(4, 4)

# ------------------------------------------------------------------ check 3
print("\n[check 3] generic defect minus claimed matrix (NO normalisation imposed):")
sp.pprint(sp.simplify(PhiON_generic - claimed))

# ------------------------------------------------------------------ check 4
scal = impose(sp.simplify(RicON.trace()))
print("\n[check 4] scalar curvature + 4 + v^2/2 =", sp.simplify(scal + 4 + v**2 / 2))
# sectional curvature K(e0,e3) = R(e0,e3,e3,e0)
Rlow = lambda i_, j_, k_, l_: sum(g[i_, m] * Rm[m][j_][k_][l_] for m in range(n))
def Rfr(A, B, C, D_):
    return sum(E[i_, A] * E[j_, B] * E[k_, C] * E[l_, D_] * Rlow(i_, j_, k_, l_)
               for i_ in range(n) for j_ in range(n) for k_ in range(n) for l_ in range(n))
K03 = impose(sp.simplify(Rfr(0, 3, 0, 3)))   # <R(e0,e3)e3,e0> with this index convention = R_{0303}
print("K(e0,e3) - v^2/4 =", sp.simplify(K03 - v**2 / 4), "   (sign convention check: K(e0,e1) =",
      impose(sp.simplify(Rfr(0, 1, 0, 1))), ")")
K02 = impose(sp.simplify(Rfr(0, 2, 0, 2)))
print("K(e0,e2) =", sp.factor(K02))
K23 = impose(sp.simplify(Rfr(2, 3, 2, 3)))
print("K(e2,e3) =", sp.factor(K23))

# ------------------------------------------------------------------ check 5
V, A_, B_ = sp.symbols('V alpha beta', real=True)
M = sp.Matrix([[-V**2 / 2, 0, 0, A_], [0, 0, 0, 0], [0, 0, -V**2 / 2, -B_], [A_, 0, -B_, V**2 / 2]])
print("\n[check 5] eigenvalues of defect matrix:", M.eigenvals())
Moff = sp.Matrix([[0, 0, 0, A_], [0, 0, 0, 0], [0, 0, 0, -B_], [A_, 0, -B_, 0]])
print("          eigenvalues of off-diagonal part:", Moff.eigenvals())
# exact op norm = max |eig| = max( V^2/2 , sqrt(V^4/4 + A^2 + B^2) ) = sqrt(V^4/4+A^2+B^2)
# claimed bound V^2/2 + sqrt(A^2+B^2) >= sqrt(V^4/4 + A^2+B^2)  (true since (x+y)^2 >= x^2+y^2 for x,y>=0)

# ------------------------------------------------------------------ check 6 (numerics)
def smoothstep(x):
    """C^infty step: 0 for x<=0, 1 for x>=1, with derivatives (numerically, via sympy)."""
    X_ = sp.Symbol('X_')
    f = sp.exp(-1 / X_)
    st = f / (f + f.subs(X_, 1 - X_))
    return st, X_

st, X_ = smoothstep(None)
st1 = sp.diff(st, X_); st2 = sp.diff(st, X_, 2)
f0 = sp.lambdify(X_, st, 'mpmath'); f1 = sp.lambdify(X_, st1, 'mpmath'); f2 = sp.lambdify(X_, st2, 'mpmath')
import mpmath as mp
def S(x, order=0):
    x = float(x)
    if x <= 1e-3 or x >= 1 - 1e-3:
        return (0.0 if x <= 0.5 else 1.0) if order == 0 else 0.0
    return float([f0, f1, f2][order](mp.mpf(x)))

# fibre data: a0 fixed, R0 fixed, zeta(u) = S((u+R0*0.8)/(1.6 R0))  (constant near both ends)
a0, R0 = 1.0, 1.5
def zeta_d(uu, order):   # order 1,2 : zeta', zeta''
    c = 1.6 * R0
    return S((uu + 0.8 * R0) / c, order) / c**order
def eta_d(x, order):     # eta on [-1,1], constant near the ends: eta = S((x+0.8)/1.6)
    return S((x + 0.8) / 1.6, order) / 1.6**order

# constants A0, A1, M1, M2 on fine grids
ug = np.linspace(-R0, R0, 4001)
Qg = np.array([a0 * np.cosh(x) * zeta_d(x, 1) for x in ug])
Qpg = np.array([a0 * np.sinh(x) * zeta_d(x, 1) + a0 * np.cosh(x) * zeta_d(x, 2) for x in ug])
jg = np.tanh(ug)
A0 = np.max(np.abs(Qg)); A1 = np.max(np.abs(Qpg + 2 * jg * Qg))
xg = np.linspace(-1, 1, 4001)
M1 = max(abs(eta_d(x, 1)) for x in xg); M2 = max(abs(eta_d(x, 2)) for x in xg)
print("\n[check 6] A0=%.4f A1=%.4f M1=%.4f M2=%.4f" % (A0, A1, M1, M2))
print("   L       sup|Phi|_op (exact matrix)   claimed bound     L*sup")
for L in [5, 10, 20, 40, 80, 160, 320]:
    tg = np.linspace(-L, L, 2001)
    best = 0.0
    zp = np.array([eta_d(tt / L, 1) / L for tt in tg]); zpp = np.array([eta_d(tt / L, 2) / L**2 for tt in tg])
    kk = np.tanh(tg)
    for iu in range(0, len(ug), 10):
        Qv, Qpv, jv = Qg[iu], Qpg[iu], jg[iu]
        vv = Qv * zp
        al = (Qpv + 2 * jv * Qv) * zp / 2
        be = Qv * (zpp + kk * zp) / 2
        opn = np.sqrt(vv**4 / 4 + al**2 + be**2)
        best = max(best, opn.max())
    bound = A0**2 * M1**2 / (2 * L**2) + np.sqrt((A1 * M1)**2 + A0**2 * (M1 + M2 / L)**2) / (2 * L)
    print("  %4d     %.6e               %.6e     %.4f" % (L, best, bound, L * best))
    assert best <= bound * (1 + 1e-9)
print("All C1 checks passed.")
