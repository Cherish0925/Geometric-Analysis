"""Independent exact checks for the E_D base-TT deformation calculation.

Run with the local scientific Python. No network or research-data mutation.
The variables are x=tanh(t), f=sech(t)^2, and s=deformation amplitude.
"""

import json
import sympy as sp

x, s = sp.symbols("x s", real=True)
f = 1 - x**2


def dt(expr):
    return sp.diff(expr, x) * f


def check(name, expression):
    reduced = sp.simplify(expression)
    assert reduced == 0, (name, reduced)
    return {"check": name, "result": "exact zero"}


results = []
# b_s = (1+s f) dt^2 + (cosh(t)^2-s) dy^2 = b_0+s Q.
# For E dt^2+H dy^2, K=-(2 sqrt(E H))^-1 d_t(H'/sqrt(E H)).
E, H = 1 + s * f, 1 / f - s
D = 1 - s**2 * f**2
inv_sqrt_EH = sp.sqrt(f) / sp.sqrt(D)
K = -sp.Rational(1, 2) * inv_sqrt_EH * dt(dt(H) * inv_sqrt_EH)
K_closed = (-1 + s**2 * f**2 * (1 + 2 * x**2)) / D**2
results.append(check("exact Gaussian curvature of straight TT path", K - K_closed))
K2 = f**2 * (1 - 2 * f)
results.append(check("curvature first variation", sp.diff(K_closed, s).subs(s, 0)))
results.append(check("curvature quadratic coefficient", sp.diff(K_closed, s, 2).subs(s, 0) / 2 - K2))
# <b_s,Q>_{b_0}=2s f^2, so the scalar residual projected against Q is cubic.
projection = 2 * s * f**2 * (K_closed + 1)
results.append(check("pointwise quadratic TT projection vanishes", sp.diff(projection, s, 2).subs(s, 0)))
results.append(check("cubic projected coefficient", sp.diff(projection, s, 3).subs(s, 0) / 6 - 2 * f**4 * (1 - 2 * f)))


def sech_integral(power):
    """Integral of sech(t)^power on the real line (positive powers)."""
    return sp.sqrt(sp.pi) * sp.gamma(sp.Rational(power, 2)) / sp.gamma(sp.Rational(power + 1, 2))


cubic_integral = sp.simplify(2 * (sech_integral(7) - 2 * sech_integral(9)))
assert cubic_integral == -15 * sp.pi / 32
results.append({"check": "integrated cubic coefficient per unit angular/fibre volume", "value": str(cubic_integral)})

# Exact hyperbolic path: T_s=t+(s/2)tanh(t), angular length factor exp(-s/2).
# Pullback of dT^2+exp(-s) cosh(T)^2 dy^2 has curvature exactly -1.
t = sp.symbols("t", real=True)
T = t + s * sp.tanh(t) / 2
E_hyp = sp.diff(T, t) ** 2
H_hyp = sp.exp(-s) * sp.cosh(T) ** 2
results.append(check("hyperbolic path radial tangent", sp.diff(E_hyp, s).subs(s, 0) - sp.sech(t)**2))
results.append(check("hyperbolic path angular tangent", sp.diff(H_hyp, s).subs(s, 0) + 1))
results.append(check("hyperbolic path radial acceleration", sp.diff(E_hyp, s, 2).subs(s, 0) - sp.sech(t)**4 / 2))
results.append(check("hyperbolic path angular acceleration", sp.diff(H_hyp, s, 2).subs(s, 0) - (1 + sp.sech(t)**2) / 2))

# Independent check of the larger vertical response model in the long manuscript.
c0 = 2 / sp.pi**2
phi_y = -c0 * x * sp.sqrt(f) / 2
phi_w = -c0 * x * f ** sp.Rational(3, 2)
results.append(check("J0 Y=W on the vertical TT response", -(dt(dt(phi_y)) + x * dt(phi_y)) / 2 - phi_w))
WY = sp.simplify(c0**2 * (sech_integral(3) - sech_integral(5)) * sech_integral(3))
assert WY == 1 / (4 * sp.pi**2)
results.append({"check": "vertical response pairing", "value": str(WY)})
schur_restricted = sp.simplify(3 / (8 * sp.pi**2) - WY)
assert schur_restricted == 1 / (8 * sp.pi**2)
results.append({"check": "restricted optimized corrected quadratic form", "value": str(schur_restricted), "scope": "only the specified angularly invariant vertical response class"})

print(json.dumps({"checks": results, "status": "PASS"}, indent=2))
