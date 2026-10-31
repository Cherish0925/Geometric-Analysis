"""Finite-collar and nonlinear-receiver algebra for round6_construction.md.

Run: python round6_construction_check.py

These exact identities check the stated scales and the non-Jacobi gauge
coefficient. They do not replace the analytic weighted inverse, the
Sobolev estimates, or the geometric marking argument in the notes.
"""

import sympy as s


t, u, beta, eps, margin = s.symbols(
    "t u beta eps margin", positive=True
)

# The collar half-width W satisfies sinh(W) sinh(beta/2)=1.
# Write beta=4u and exp(-W)=tanh(u). This avoids branch choices.
exp_minus_W = s.tanh(u)
sinh_W = (1 / exp_minus_W - exp_minus_W) / 2
assert s.simplify(sinh_W - 1 / s.sinh(2 * u)) == 0
assert s.simplify(s.diff(s.atan(s.sinh(t)), t) - s.sech(t)) == 0

# For L=W-margin, the two discarded receiver tails are at most
# 4 exp(-L)=4 exp(margin) tanh(beta/4)=O(beta).
tail_bound = 4 * s.exp(margin) * s.tanh(beta / 4)
assert s.limit(tail_bound / beta, beta, 0, dir="+") == s.exp(margin)
cutoff_L2 = s.sqrt(tail_bound.subs(beta, eps**2))
assert s.simplify(
    s.limit(cutoff_L2 / eps, eps, 0, dir="+") - s.exp(margin / 2)
) == 0
print("PASS: receiver tail is O(beta), and the cutoff forcing is O(a epsilon)")

# Circle Poincare gives beta^2 cosh(t)^2; its receiver integral on
# [-L,L] is <= beta^2 integral_{-W}^W cosh(t) dt.
angular_bound = 2 * beta**2 / s.sinh(beta / 2)
assert s.limit(angular_bound / beta, beta, 0, dir="+") == 4
print("PASS: the nonzero angular response has scale O(beta a^2)")


# Actual Ricci calculation testing the non-Jacobi gauge identity.
# Background g=dt^2+exp(2t)dy^2 is hyperbolic. The vector field X=partial_t
# has flow t -> t+s. Use a genuinely non-Jacobi diagonal variation V.
ss = s.symbols("ss", real=True)
base = s.Matrix([1, s.exp(2 * t)])
variation = s.Matrix([t, s.exp(2 * t) * t**2])


def einstein_diagonal(metric):
    """Ric(g)+g for g=A(t)dt^2+B(t)dy^2, as two diagonal entries."""
    A, B = metric
    ric_tt = (
        -s.diff(B, t, 2) / (2 * B)
        + s.diff(B, t)**2 / (4 * B**2)
        + s.diff(A, t) * s.diff(B, t) / (4 * A * B)
    )
    ric_yy = (
        -s.diff(B, t, 2) / (2 * A)
        + s.diff(A, t) * s.diff(B, t) / (4 * A**2)
        + s.diff(B, t)**2 / (4 * A * B)
    )
    return s.Matrix([ric_tt + A, ric_yy + B])


def derivative(direction, order):
    return einstein_diagonal(base + ss * direction).diff(
        ss, order
    ).subs(ss, 0).applyfunc(s.simplify)


assert einstein_diagonal(base).applyfunc(s.simplify) == s.zeros(2, 1)
H = variation + base.diff(t)
W = 2 * variation.diff(t) + base.diff(t, 2)
F = derivative(variation, 1)
assert F != s.zeros(2, 1)
gauge_identity = (
    derivative(H, 2)
    - derivative(variation, 2)
    + derivative(W, 1)
    - 2 * F.diff(t)
)
assert gauge_identity.applyfunc(s.simplify) == s.zeros(2, 1)
assert F.diff(t).applyfunc(s.simplify) != s.zeros(2, 1)
print("PASS: actual Ricci variation retains the nonzero 2 Lie_X(F) gauge term")


# Exact ledger substitution beta=epsilon^2, a=c epsilon and
# delta=d epsilon^3. The displayed constants concern the polynomial
# ledger itself; analytic estimate constants remain unspecified.
c, d = s.symbols("c d", nonnegative=True)
a = c * eps
delta = d * eps**3
eta = delta + eps**2 + eps * a + a**2
ledger = (
    eps**2 * a
    + a * eta
    + eta**2
    + (eps + eps**2) * a**2
    + a**3
)
linear_coefficient = s.limit(ledger / eps**3, eps, 0, dir="+")
assert s.expand(linear_coefficient - (2 * c + 2 * c**2 + 2 * c**3)) == 0
assert s.limit(linear_coefficient, c, 0, dir="+") == 0
print("PASS: the fixed linear-radius error is O(c+c^2+c^3), not o(1) at fixed c")

# A slowly vanishing relative radius tests o(epsilon), beyond the
# fixed-power examples: epsilon=exp(-z), a=epsilon/z.
z = s.symbols("z", positive=True)
slow_ledger = ledger.subs({eps: s.exp(-z), c: 1 / z}) / s.exp(-3 * z)
assert s.limit(slow_ledger, z, s.oo) == 0
for exponent in (s.Rational(6, 5), s.Rational(3, 2), s.Rational(7, 4)):
    polynomial_ledger = ledger.subs(c, eps ** (exponent - 1))
    assert s.limit(polynomial_ledger / eps**3, eps, 0, dir="+") == 0
print("PASS: polynomial and logarithmically slow o(epsilon) radii give o(epsilon^3) errors")

# Source / nuclear norm duality reproduces the inherited coefficient.
p = s.symbols("p", integer=True, positive=True)
c0 = 1 / (2 * s.pi**2)
M0 = 8 * s.pi**2 * (p - 1)
assert s.simplify(c0 / M0 - 1 / (16 * s.pi**4 * (p - 1))) == 0
print("PASS: the o(epsilon) lower-defect coefficient is 1/(16 pi^4 (p-1))")

print("All round-six finite-collar algebra checks passed.")
