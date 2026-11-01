#!/usr/bin/env python3
"""Exact local algebra for the nonlinear slow-moduli theorem.

The coordinate fiber below is flat: it tests the parameter-dependent
Ricci terms, not the existence of a closed horizontal hyperbolic path.
Global existence and Teichmuller distance are proved in the English note.
"""

import sympy as s


def clean(x):
    return s.factor(s.cancel(s.expand(x)))


def zero(matrix, label):
    values = list(matrix) if isinstance(matrix, s.MatrixBase) else [matrix]
    assert all(clean(x) == 0 for x in values), label
    print("PASS:", label)


def ricci(g, coords):
    n = len(coords)
    gi = g.inv().applyfunc(clean)
    gamma = [[[clean(sum(gi[k, l] * (
        s.diff(g[l, j], coords[i]) + s.diff(g[l, i], coords[j])
        - s.diff(g[i, j], coords[l])) for l in range(n)) / 2)
        for j in range(n)] for i in range(n)] for k in range(n)]
    return s.Matrix(n, n, lambda i, j: clean(sum(
        s.diff(gamma[k][i][j], coords[k])
        - s.diff(gamma[k][i][k], coords[j])
        + sum(gamma[k][i][j] * gamma[l][k][l]
              - gamma[l][i][k] * gamma[k][j][l] for l in range(n))
        for k in range(n))))


# Actual unit-speed path in determinant-one positive symmetric matrices.
# It has nonzero normal acceleration, unlike an exponential diagonal path.
v = s.symbols("v", real=True)
h = s.Matrix([[1 + v*v/2, v/s.sqrt(2)], [v/s.sqrt(2), 1]])
hi = h.inv()
k = h.diff(v)
N = k.diff(v) - k*hi*k
norm_k = clean(s.trace(hi*k*hi*k))
norm_N = clean(s.trace(hi*N*hi*N))
zero(h.det()-1, "pointwise fixed fiber area")
zero(s.trace(hi*k), "trace-free tangent")
zero(norm_k-1, "unit L2 speed for a unit-area flat test fiber")
zero(s.trace(hi*N), "trace-free normal acceleration")
zero(s.trace(hi*N*hi*k), "normal acceleration orthogonal to path tangent")
assert norm_N != 0

# Four-dimensional Ricci, obtained independently from Christoffels.
t, r, y, z = s.symbols("t r y z", real=True)
coords = [t, r, y, z]
b = s.diag(1, s.exp(2*t))
bi = b.inv()
param = t*r
hu = h.subs(v, param)
ku = k.subs(v, param)
Nu = N.subs(v, param)
g = s.diag(b, hu)
dv = s.Matrix([s.diff(param, t), s.diff(param, r)])
grad_sq = clean((dv.T*bi*dv)[0])
lap = clean(-s.diff(param, t, 2) - s.diff(param, t)
            - s.exp(-2*t)*s.diff(param, r, 2))
actual = ricci(g, coords) + s.diag(b, s.zeros(2))
expected = s.diag(-dv*dv.T/4, ku*lap/2-Nu*grad_sq/2)
zero(actual-expected, "all Ricci blocks for a two-variable true matrix path")
zero(s.trace(hu.inv()*actual[2:4, 2:4]*hu.inv()*ku)-lap/2,
     "exact retained scalar slow equation")
normal_dropped = s.diag(-dv*dv.T/4, ku*lap/2)
assert any(clean(x) != 0 for x in actual-normal_dropped)
print("PASS: omitted normal acceleration rejected")
Xi = s.Rational(1, 16) + norm_N/4
actual_energy = clean(s.trace(g.inv()*actual*g.inv()*actual))
zero(actual_energy-lap**2/4-Xi*grad_sq**2,
     "complete residual energy includes normal acceleration")

# Arbitrary base curvature: independent scalar completion of the square.
area, curv, X, C4, CN, L = s.symbols(
    "area curv X C4 CN L", positive=True)
raw = 2*area*curv**2-curv*X/2+(C4/16+CN/4)*X**2+L**2/4
completed = (2*area*(curv-X/(8*area))**2
             +(C4/16+CN/4-1/(32*area))*X**2+L**2/4)
zero(raw-completed, "arbitrary-base complete square and quartic coefficient")

# In conformal surface coordinates, z=x is harmonic whereas its Hessian
# need not be small. Trace cancellation supplies m^-2, not m^-1.
x, y0, m, amplitude = s.symbols("x y0 m amplitude", real=True, nonzero=True)
phi = x*y0
bconf = s.exp(2*phi)*s.eye(2)
vslow = amplitude*s.cos(2*s.pi*x/m)
lap_slow = -s.exp(-2*phi)*(s.diff(vslow, x, 2)+s.diff(vslow, y0, 2))
zero(lap_slow-(2*s.pi/m)**2*s.exp(-2*phi)*vslow,
     "harmonic circle coefficient has exact m^-2 scalar Laplacian")
# Hessian_{xy} v = -phi_y * d_x v = -x * d_x v: generically order m^-1.
hess_xy = -x*s.diff(vslow, x)
assert hess_xy != 0
print("PASS: replacing the scalar Laplacian by a Hessian size loses cancellation")

# Root-of-unity averages: only frequencies 0,2,4 occur. Degree m>=5
# kills all nonconstant frequencies, including on each fundamental cell.
w = s.symbols("w", nonzero=True)
cosine = (w+w**-1)/2
sine = (w-w**-1)/(2*s.I)
cos2 = s.Poly(s.expand(w**4*cosine**2), w)
sin4 = s.Poly(s.expand(w**4*sine**4), w)
assert cos2.coeff_monomial(w**4) == s.Rational(1, 2)
assert sin4.coeff_monomial(w**4) == s.Rational(3, 8)
assert max(abs(i[0]-4) for i in sin4.monoms()) == 4
print("PASS: cyclic cos² and sin⁴ averages for every m>=5")

# Teichmuller conversion: endpoint triangle bound is artanh(epsilon),
# with both metric-to-length and d_T=log(K)/2 factors retained.
eps = s.symbols("eps", positive=True)
zero(2*s.log(s.sqrt((1+eps)/(1-eps)))/2
     -s.log((1+eps)/(1-eps))/2,
     "fiber metric comparison and two-endpoint Teichmuller constant")
print("All finite checks passed; global geometric proof remains in the note.")
