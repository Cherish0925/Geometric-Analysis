#!/usr/bin/env python3
"""Exact finite checks for line1_period_inertia.md; no PDE certification."""

import sympy as s


def zero(label, expression):
    result = s.simplify(expression)
    expected = s.zeros(*result.shape) if isinstance(result, s.MatrixBase) else 0
    assert result == expected, (label, result)
    print("PASS", label)


def true(label, condition):
    assert bool(condition), (label, condition)
    print("PASS", label)


x, y, z, t, h, a, b = s.symbols("x y z t h a b", real=True)
u, v = s.Matrix([x, y, z]), s.Matrix([a, b, h])


def tensor_q(vector):
    return vector * vector.T - (vector.dot(vector) / 3) * s.eye(3)


diff = tensor_q(u) - tensor_q(v)
aa, bb, hh = u.dot(u), v.dot(v), u.dot(v)
zero("trace-free rank-one distance", s.trace(diff.T * diff)
     - s.Rational(2, 3) * (aa - bb) ** 2 - 2 * (aa * bb - hh ** 2))

# These polynomial identities prove the inequalities used in the two cases
# a+b>=1 and a+b<1; nonnegative factors are identified in the proof.
F = s.Rational(2, 3) * (a - b) ** 2 + 2 * (a * b - h ** 2)
zero("distance numerator", (a + b - 2 * h) * (a + b + 2 * h)
     - ((a - b) ** 2 + 4 * (a * b - h ** 2)))
zero("large amplitude numerator domination", 2 * F
     - ((a - b) ** 2 + 4 * (a * b - h ** 2))
     - s.Rational(1, 3) * (a - b) ** 2)
zero("small amplitude first bound", 2 * ((a - 1) ** 2 + (b - 1) ** 2)
     - (a + b - 2) ** 2 - (a - b) ** 2)
zero("small amplitude second bound", (t - 2) ** 2 - t - (t - 1) * (t - 4))
zero("phase squared triangle remainder", 2 * (z - 1) ** 2
     + 2 * z ** 2 * (1 - t) ** 2 - (z * t - 1) ** 2
     - ((z - 1) + z * (1 - t)) ** 2)
zero("angular phase comparison", 2 * z ** 2 * (1 - t ** 2)
     - 2 * z ** 2 * (1 - t) ** 2 - 4 * z ** 2 * t * (1 - t))
zero("binary sign variance comparison", 2 * (1 - t ** 2)
     - 2 * (1 - t) - 2 * t * (1 - t))

true("projective form error", 2 * (180 + 180) + 2 * 2880 == 6480)
true("scalar phase error", 2 * (180 + 180) + 2880 == 3600)
true("scalar gradient coefficient", 12 * (s.Rational(1, 2) + s.Rational(1, 2)) == 12)
zero("form error square root", (36 * s.sqrt(5)) ** 2 - 6480)
zero("phase error square root", (120 * s.sqrt(3)) ** 2 - 12 * 3600)
true("rational upper bounds for radicals", s.Rational(3, 2) ** 2 > 2
     and s.Rational(9, 4) ** 2 > 5 and s.Rational(26, 15) ** 2 > 3)
true("coefficient below 300", 7 * s.Rational(3, 2)
     + 36 * s.Rational(9, 4) + 120 * s.Rational(26, 15) < 300)

# At kappa=1/2880, sqrt(180 kappa)=1/4 and 7 sqrt(kappa/2)<1/10.
# The lower square is > (sqrt(3)/2-1/10)^2 >1/2.
# The upper square is < (sqrt(5)/2+1/10)^2 <3/2.
true("alignment amplitude correction", s.Rational(49, 5760) < s.Rational(1, 100))
true("positive norm lower endpoint", (s.sqrt(3) / 2 - s.Rational(1, 10)) ** 2 > s.Rational(1, 2))
true("positive norm upper endpoint", (s.sqrt(5) / 2 + s.Rational(1, 10)) ** 2 < s.Rational(3, 2))

# Explicit exact Gram example: nonzero positive remainder and uncontrolled
# negative Gram. The decomposition is the theorem's structural output.
columns = s.Matrix([[1, -1, 1], [0, s.Rational(1, 10), 0],
                    [0, 0, s.Rational(1, 5)]])
positive = columns.T * columns
alpha = s.Matrix([1, -1, 1])
remainder = positive - alpha * alpha.T
negative = s.diag(2, 3, 5)
cup = positive - negative
zero("positive/negative Gram decomposition", cup -
     (alpha * alpha.T + remainder - negative))
true("remainder trace", s.trace(remainder) == s.Rational(1, 20))
true("remainder PSD", all(value >= 0 for value in remainder.eigenvals()))
true("negative Gram PSD", all(value >= 0 for value in negative.eigenvals()))
for vector in (s.Matrix([1, 1, 0]), s.Matrix([-1, 0, 1])):
    zero("constant-sign kernel", vector.dot(alpha))
    true("cup upper bound on sign kernel", (vector.T * cup * vector)[0]
         <= s.trace(remainder) * vector.dot(vector))

# An exact aligned positive Gram does not determine the full cup matrix.
ones = s.ones(3, 1)
abstract_cup = ones * ones.T - 4 * s.eye(3)
true("negative information cannot be erased", sorted(abstract_cup.eigenvals()) == [-4, -1])
true("spectral dichotomy constant", (2 * 12) ** 2 == 576)
true("spectral small-error threshold", (2 * 300) ** 2 == 360000)
zero("common-functional period coefficient", 2 * s.pi ** 2 / (72 * s.pi ** 2)
     - s.Rational(1, 36))
zero("signed polarization", (u - v).dot(u - v) - (aa + bb - 2 * hh))
print("All exact period-inertia checks passed; analytic and gauge inputs remain explicit.")
