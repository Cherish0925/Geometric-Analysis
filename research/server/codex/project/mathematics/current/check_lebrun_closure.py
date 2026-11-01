"""Exact checks of displayed algebra, not validation of the analytic lemma."""

from fractions import Fraction
import sympy as s


def check_zero(name, expression):
    if s.simplify(expression) != 0:
        raise AssertionError((name, expression))
    print("PASS:", name)


x, scalar, alpha, bminus = s.symbols("x scalar alpha bminus", real=True)
check_zero(
    "Chern-Weil lower-bound factorization",
    (4 - 2 * x) ** 2 / 24 - x**2 / 2 - s.Rational(1, 4)
    - (s.Rational(1, 2) - x) * (4 * x + 10) / 12,
)
weyl2 = s.Rational(3, 2) * alpha**2
t = scalar + 24 * alpha
q = -scalar + 3 * alpha
G = (2 * scalar / 3 - 2 * alpha) ** 2 - bminus**2
check_zero("spectral square", t**2 + 18 * G
           - 216 * (scalar**2 / 24 + 2 * weyl2) + 18 * bminus**2)
check_zero("calibration square", 27 * (scalar**2 / 24 + 2 * weyl2)
           - q**2 - t**2 / 8)

P, S2, W2, L = s.symbols("P S2 W2 L", real=True)
R2 = P + S2 / 4
four_pi2_T = S2 / 24 + 2 * W2 - P / 2
check_zero("nonpositive-budget energy identity",
           4 * P + L - (R2 + 12 * W2 - 6 * four_pi2_T + L))
assert s.Rational(245, 2) <= 1215
assert 972 * s.Rational(5, 4) == 1215
assert s.Rational(1, 8) * s.Rational(11, 12) == s.Rational(11, 96)
assert s.Rational(11, 96) < s.Rational(1, 4)
print("PASS: transfer and positive-branch constants")

# The range assertion is proved in the note; this catches indexing errors.
for m in range(2, 102):
    A = 8 * (m - 1)
    k = (A + 2) // 3 - 1
    gap = Fraction(1, 3) - Fraction(k, A)
    assert 0 < gap <= Fraction(1, A)
print("PASS: first 100 threshold examples (finite arithmetic only)")
print("Scope: algebra and indexing; no PDE or SW existence certification.")
