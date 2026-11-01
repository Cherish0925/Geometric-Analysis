"""Exact finite algebra for the integral multi-shear balance note.

Run with the scientific Python environment; no network or Session access.
These checks do not certify the global PDE or the covering-space proof.
"""
import json
import sympy as s

passed = []


def zero(name, expression):
    entries = list(expression) if isinstance(expression, s.MatrixBase) else [expression]
    assert all(s.simplify(x) == 0 for x in entries), (name, expression)
    passed.append(name)


def stress(b):
    return b * b.T - (b.dot(b) / 2) * s.eye(2)


x, y, u, v, t = s.symbols("x y u v t", real=True)
w1, w2 = s.symbols("w1 w2", positive=True)
b1, b2 = s.Matrix([x, y]), s.Matrix([u, v])
star = s.Matrix([[0, -1], [1, 0]])
zero("star squared", star * star + s.eye(2))
zero("opposite dual stresses", stress(b1) + stress(star * b1))
zero("stress norm", s.trace(stress(b1) ** 2) - b1.dot(b1) ** 2 / 2)
zero("two-form pairing sign", b1.dot(star * b2) + x * v - y * u)

for sign in (-1, 1):
    residual = s.sqrt(w1) * b1 + sign * s.sqrt(w2) * star * b2
    zero(f"energy-area identity sign {sign}",
         w1 * b1.dot(b1) + w2 * b2.dot(b2)
         - 2 * sign * s.sqrt(w1 * w2) * (x * v - y * u)
         - residual.dot(residual))
    dual = sign * s.sqrt(w1 / w2) * star * b1
    zero(f"weighted balanced stress sign {sign}",
         w1 * stress(b1) + w2 * stress(dual))

q, r = s.symbols("q r", real=True)
Q = s.Matrix([[q, r], [r, -q]])
g = s.eye(2) + t * Q
energy_density = (b1.T * g.inv() * b1)[0] * s.sqrt(g.det())
zero("metric variation is minus TT stress",
     s.diff(energy_density, t).subs(t, 0) + s.trace(stress(b1) * Q))

# z = (u+i v)^2 at a simple branch point.
branch_x = s.Matrix([2 * u, -2 * v])
branch_y = s.Matrix([2 * v, 2 * u])
zero("branched pullback star relation", star * branch_x - branch_y)
zero("branched pullback stress including common zero",
     stress(branch_x) + stress(branch_y))
zero("branched pullback Jacobian",
     s.det(s.Matrix.hstack(branch_x, branch_y)) - 4 * (u * u + v * v))

a, zprime, bnorm = s.symbols("a zprime bnorm", positive=True)
zero("scalar integral circle factor",
     2 * s.pi * a * (-s.Rational(1, 2) * a * a * zprime ** 2 * bnorm)
     + s.pi * a ** 3 * zprime ** 2 * bnorm)

# Regression: isotropic stress cancellation and a genuine one-form source
# are different tests. Wrong proportional rather than star-related inputs
# must be rejected, and unequal weights must not accidentally pass.
negative_tests = {
    "proportional nonzero forms": stress(s.Matrix([1, 0])) * 2,
    "unequal weights": stress(s.Matrix([1, 0])) + 2 * stress(s.Matrix([0, 1])),
    "generic pair": stress(s.Matrix([1, 2])) + stress(s.Matrix([3, 4])),
}
for name, tensor in negative_tests.items():
    assert tensor != s.zeros(2), f"Wrong cancellation accepted: {name}"

# Explicit Euler product for B_{r,4} times a genus-two fiber.
zero("closed two-shear Euler characteristic", (2 - 2 * r - 4) * (-2) - (4 * r + 4))

print(json.dumps({"exact_checks": passed,
                  "wrong_balance_inputs_rejected": list(negative_tests),
                  "scope": "finite local algebra; global proofs are in the note"}, indent=2))
