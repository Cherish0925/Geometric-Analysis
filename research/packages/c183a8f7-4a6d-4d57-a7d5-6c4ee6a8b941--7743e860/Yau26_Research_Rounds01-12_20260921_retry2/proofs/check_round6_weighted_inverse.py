"""Exact identities behind the receiver-weighted inverse; not a PDE solver."""

import json
import sympy as s

t = s.symbols("t", real=True)
lam = s.symbols("lam", nonnegative=True)
z = s.Function("z")(t)
k = s.tanh(t)
f = 1 / s.cosh(t) ** 2
w = 1 / s.cosh(t)


def reduce(expr):
    return s.simplify(s.expand_trig(expr).rewrite(s.exp))


def check(name, expr):
    assert reduce(expr) == 0, (name, expr)
    passed.append(name)


def d1(u):
    return s.diff(u, t) + 2 * k * u


def d2(u):
    return -s.diff(u, t) + k * u


def d1star(u):
    return -s.diff(u, t) + 3 * k * u


def minus_p(u):
    return -s.diff(u, t, 2) - k * s.diff(u, t)


passed = []
check("horizontal factorization", d2(d1(z)) - minus_p(z) - (2 - 4 * f) * z)
check("coercive partner", d1(d2(z)) - minus_p(z) - (2 - f) * z)
check("first-order closed-range gap", d1(d1star(z)) + s.diff(z, t, 2)
      - k * s.diff(z, t) - (6 - 3 * f) * z)
check("horizontal kernel", d1(f))
check("vertical transfer kernel", minus_p(s.atan(s.sinh(t))))
check("weighted scalar real part", -s.diff(s.diff(w, t) - w * k, t) / (2 * w)
      - (2 * f - 1))
check("horizontal adjoint constant", -s.diff(w, t, 2) + s.diff(k * w, t)
      + (2 - 4 * f) * w)
check("collar Dirichlet conjugation",
      s.sqrt(s.cosh(t)) * minus_p(z / s.sqrt(s.cosh(t)))
      + s.diff(z, t, 2) - (s.Rational(1, 4) + f / 4) * z)

# The partner identity is also checked on a deliberately incorrect potential.
assert reduce(d1(d2(z)) - minus_p(z) - (2 - 2 * f) * z) != 0

# The derivative of J and the elementary receiver integral give -pi/8.
check("transfer derivative", s.diff(s.atan(s.sinh(t)), t) - w)
x = s.symbols("x", real=True)
receiver_integral = s.integrate(s.sqrt(1 - x**2), (x, -1, 1))
assert receiver_integral == s.pi / 2
receiver_coefficient = -receiver_integral / 4
assert receiver_coefficient == -s.pi / 8

print(json.dumps({
    "status": "passed",
    "exact_identities": passed,
    "receiver_coefficient": str(receiver_coefficient),
    "wrong_partner_potential_rejected": True,
    "scope": "operator algebra and receiver integral; analytic inverse is proved in the note",
}, indent=2))
