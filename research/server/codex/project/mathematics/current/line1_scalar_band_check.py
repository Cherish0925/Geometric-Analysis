"""Exact finite algebra for line1_scalar_band_remainder.md.

This verifies identities and calibration examples, not weighted-monopole
existence, elliptic regularity, or the global analytic argument.
Run: python line1_scalar_band_check.py (requires SymPy).
"""

import sympy as sp


def zero(expression, name):
    value = sp.factor(sp.expand(expression))
    assert value == 0, (name, value)
    print(f"PASS: {name}")


s, w, rho, p, volume = sp.symbols("s w rho p V", real=True)
q, t = -s + w, s + 2 * w
zero(s**2 / 24 + w**2 / 12 - q**2 / 36 - t**2 / 72,
     "LeBrun energy square split")

a, b, c, d, e = sp.symbols("a b c d e", real=True)
weyl = sp.Matrix([[a, c, d], [c, b, e], [d, e, -a - b]])
psi = sp.Matrix([rho, 0, 0])
model = rho**2 * sp.eye(3) / 8 - sp.Rational(3, 8) * psi * psi.T
weyl_norm2 = sp.trace(weyl * weyl)
fit_norm2 = sp.trace((weyl - model) * (weyl - model))
eigen_defect = (psi.T * weyl * psi)[0] + w * rho**2 / 3
fit_remainder = sp.expand(
    fit_norm2 - (w - sp.Rational(3, 4) * rho**2)**2 / 6
    - sp.Rational(3, 4) * eigen_defect
)
zero(fit_remainder.subs(w**2, 6 * weyl_norm2),
     "full symmetric Weyl-matrix polynomial fit")

u = sp.Rational(3, 2) * rho
a0 = q - u**2
zero(w - sp.Rational(3, 4) * rho**2 - (t + a0) / 3,
     "amplitude and scalar-Weyl mismatch relation")
zero(s - (t / 3 - sp.Rational(3, 2) * rho**2
          - sp.Rational(2, 3) * a0),
     "scalar decomposition for Poincare estimate")

R, grad_phi2, grad_psi2, drho2, curvature_pair = sp.symbols(
    "R grad_phi2 grad_psi2 drho2 curvature_pair", real=True
)
d_amp = 2 * drho2
d_quad = 4 * rho * grad_phi2 - grad_psi2
d_hodge = grad_psi2 + s * rho**2 / 3 - 2 * curvature_pair
d_eigen = 2 * curvature_pair + 2 * w * rho**2 / 3
zero(d_hodge + d_eigen - t * rho**2 / 3 - grad_psi2,
     "joint Hodge-eigen defect gradient identity")
# The integrated spinor identity gives
# 2 drho2 + 4 rho grad_phi2 + s rho^2 + R = 0,
# with R denoting the integral f rho^3 in this linear formal check.
retained = d_amp + d_quad + d_hodge + d_eigen
zero(retained - (2 * q * rho**2 / 3 - R)
     - (2 * drho2 + 4 * rho * grad_phi2 + s * rho**2 + R),
     "four-defect identity from the two Weitzenbock identities")
zero(sp.Rational(27, 8) * (2 * q * rho**2 / 3 - R)
     - (q * u**2 - sp.Rational(27, 8) * R),
     "normalization P = 27 D0 / 8")

C0, K2, lam = sp.symbols("C0 K2 lambda", positive=True)
zero(3 * sp.Rational(3, 2)**2 * 8 * K2 / (27 * lam)
     - 2 * K2 / lam, "scalar variance Poincare coefficient")
zero(3 * sp.Rational(2, 3)**2 * C0 - 4 * C0 / 3,
     "scalar variance amplitude coefficient")

alpha, beta = sp.symbols("alpha beta", positive=True)
prod_s = -2 * (alpha + beta)
prod_w = alpha + beta
prod_p = (alpha + beta)**2 * volume / (8 * sp.pi**2)
prod_defect = (prod_s**2 / 24 + prod_w**2 / 12) * volume / (
    4 * sp.pi**2) - prod_p / 2
zero(prod_defect, "unequal hyperbolic product LeBrun equality")
prod_ric0 = 2 * (-alpha - prod_s / 4)**2 + 2 * (
    -beta - prod_s / 4)**2
zero(prod_ric0 - (alpha - beta)**2,
     "unequal product trace-free Ricci does not vanish")
relative_einstein_defect = 4 - prod_s**2 / (2 * (alpha**2 + beta**2))
zero(relative_einstein_defect - 2 * (alpha - beta)**2 / (
    alpha**2 + beta**2), "unequal product relative Einstein defect")

omega = sp.sqrt(3) * psi / 2
allowed_model = ((omega.T * omega)[0] * sp.eye(3) / 3
                 - omega * omega.T) / 2
assert sp.simplify(model - allowed_model) == sp.zeros(3)
print("PASS: normalized form has the allowed KE Weyl model")
zero((omega.T * omega)[0] - 2
     - (t / 6 - (s + 4) / 2 - a0 / 3),
     "normalized form amplitude error")
zero(2 * sp.Rational(13, 108) + 10 * C0 / 27
     + sp.Rational(1, 18) - (10 * C0 + 8) / 27,
     "combined calibration defect constant")

print("All 15 exact finite checks passed; no PDE certification is claimed.")
