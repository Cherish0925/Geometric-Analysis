#!/usr/bin/env python3
"""Exact algebra checks only; no numerical certification of PDE arguments."""
import json
import sympy as s

phi, dp, u, du, pot = s.symbols("phi dp u du pot", real=True)
# q(phi*u)-<L*u,phi**2*u> after integration by parts.
lhs = s.Rational(1, 2) * (dp*u + phi*du)**2 + pot*phi**2*u**2
rhs = s.Rational(1, 2) * du * (2*phi*dp*u + phi**2*du) + pot*phi**2*u**2
assert s.expand(lhs-rhs-s.Rational(1, 2)*dp**2*u**2) == 0

lam, a = s.Rational(1, 4), s.Rational(1, 2)
assert lam-a*a/2 == s.Rational(1, 8)
H, gap = s.symbols("H gap", positive=True)
assert s.expand(8*(gap-(H/2)**2/2)) == 8*gap-H**2

z = s.symbols("z", positive=True)
# sum (j+2) z**j = z/(1-z)**2+2/(1-z).
assert s.factor(z/(1-z)**2+2/(1-z)-(2-z)/(1-z)**2) == 0

t, c, V = s.symbols("t c V", positive=True)
scale = s.exp(2*t*c)
# E=(scale-1)h; tensor norm rescales scale^-2 and volume scale^2.
energy = 4*(scale-1)**2/scale**2 * scale**2 * V
assert s.simplify(energy-4*(scale-1)**2*V) == 0
assert s.limit(energy/t**2, t, 0) == 16*c**2*V

print(json.dumps({
    "scope": "exact algebra only, not PDE or topology verification",
    "checks_passed": 5,
    "weighted_absorption": "lambda-a^2/2",
    "growth_compatibility": "H^2<8 lambda",
    "cyclic_family_absorption": "1/8",
    "linear_growth_sum": "(2-exp(-1))/(1-exp(-1))^2",
    "constant_conformal_cell_energy": "4*(exp(2*t*c)-1)^2*V"
}, indent=2))
