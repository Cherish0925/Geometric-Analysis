"""Independent symbolic check of the exact hyperbolic-neck kernel."""

import sympy as sp

t, eps = sp.symbols("t eps", real=True)
k, c = sp.symbols("k c", positive=True)
a = c * sp.cosh(k * t)
f = sp.sech(k * t) ** 2

# For A(t)dt²+C(t)dphi², Gaussian curvature is
# -(2 sqrt(A*C))^{-1} d/dt(C'/sqrt(A*C)).
# Differentiate its factors at eps=0 without assuming anything about f.
u = sp.Function("u")(t)
A0, C0 = sp.Integer(1), a * a
dA, dC = u, -a * a * u
sqrt_det = a
d_sqrt_det = sp.simplify((dA * C0 + A0 * dC) / (2 * sqrt_det))
assert d_sqrt_det == 0
dK = sp.simplify(-sp.diff(sp.diff(dC, t) / a, t) / (2 * a))
good_dK = sp.simplify(dK.subs(u, f).doit().rewrite(sp.cosh))
assert good_dK == 0, good_dK
divergence = sp.simplify(-sp.diff(f, t) - 2 * sp.diff(a, t) / a * f)
assert divergence == 0
assert sp.simplify(-sp.diff(a, t, 2) / a + k * k) == 0

# K=-k² and DK=0 imply D(Ric+k²g)[H]=0 on the base;
# the second hyperbolic factor is unchanged. Trace and divergence zero
# remove the Bianchi-gauge addition.
bad_f = sp.sech(k * t)
bad_dK = sp.simplify(dK.subs(u, bad_f).doit())
assert sp.simplify(bad_dK.subs(t, 0) - k * k / 2) == 0
bad_div = sp.simplify(-sp.diff(bad_f, t) - 2 * sp.diff(a, t) / a * bad_f)
assert sp.simplify(bad_div.subs(t, 1 / k)) != 0

# Independently compare finite-parameter curvature differentiation at t=0.
A = 1 + eps * f
C = a * a * (1 - eps * f)
K = -sp.diff(sp.diff(C, t) / sp.sqrt(A * C), t) / (2 * sp.sqrt(A * C))
assert sp.simplify(sp.diff(K, eps).subs({eps: 0, t: 0})) == 0

# Actual electric-shear forcing density after integration over circle:
# <E,H>=-f*a²*zprime²*betanorm² and dmu=a dt dphi dmu_F.
zp, beta2 = sp.symbols("zp beta2", real=True)
pairing_density = -2 * sp.pi * f * a**3 * zp**2 * beta2
assert sp.simplify(pairing_density + 2 * sp.pi * c**3 * sp.cosh(k*t) * zp**2 * beta2) == 0
print("PASS: trace, divergence, exact product curvature, linearized Einstein kernel")
print("PASS: wrong sech profile rejected by curvature and divergence")
print("PASS: independent finite-parameter curvature differentiation at the waist")
print("PASS: exact electric-shear residual pairing density")
