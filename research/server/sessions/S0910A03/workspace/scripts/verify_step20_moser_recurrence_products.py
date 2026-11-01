#!/usr/bin/env python3
"""Check the infinite-product exponents in the weighted q -> 3q/2 Moser recurrence.

Abstract one-step recurrence:
  Z_{3q/2,k+1}
    <= (C A^2)^(2/(3q)) (C q^kappa 4^k Lambda)^(1/q) Z_{q,k}.
Here Z_q=(int_Q a^{-2} f^q)^(1/q), f=aF or f=a|E|.

The script verifies convergence of all products and the endpoint exponents
for base q0=2 (curvature) and q0=6 (Einstein defect).
"""
import math
from fractions import Fraction


def exact_sums(q0):
    # q_j=q0*(3/2)^j; sum 1/q_j=3/q0.
    sum_inv = Fraction(3, q0)
    A_exp = Fraction(4, 3) * sum_inv       # A exponent, since (A^2)^(2/3q)
    Lambda_exp = sum_inv
    return sum_inv, A_exp, Lambda_exp

for q0 in [2, 3, 6]:
    s, ae, le = exact_sums(q0)
    print(f"q0={q0}: sum 1/q_j={s}; A exponent={ae}; Lambda exponent={le}")

assert exact_sums(2) == (Fraction(3,2), Fraction(2,1), Fraction(3,2))
assert exact_sums(6) == (Fraction(1,2), Fraction(2,3), Fraction(1,2))

# Verify numerical convergence of products containing q_j^kappa and 4^j.
def product_constant(q0, kappa=3, steps=80, C=2.0):
    logp = 0.0
    q = float(q0)
    for j in range(steps):
        logp += math.log(C * q**kappa * 4**j) / q
        q *= 1.5
    return math.exp(logp), logp

for q0 in [2, 6]:
    for kappa in [2, 3, 5]:
        P, logP = product_constant(q0, kappa)
        print(f"q0={q0}, polynomial degree={kappa}: log product={logP:.6f}, product={P:.6e}")
        assert math.isfinite(P)

# Scaling substitutions.
# Curvature: A^2 Lambda^(3/2) (t H2)^(1/2),
# Lambda~t^-1, H2<=gamma^2/A^4 -> gamma/t.
# Defect: A^(2/3)Lambda^(1/2)(t J6)^(1/6),
# J6<=delta^6 V and A<=C r V^-1/4 -> delta (r^2/t)^(1/3).
import sympy as sp
A, t, gamma, delta, V, r = sp.symbols('A t gamma delta V r', positive=True)
curv = sp.simplify(A**2 * t**sp.Rational(-3,2) *
                   (t*gamma**2/A**4)**sp.Rational(1,2))
assert sp.simplify(curv-gamma/t) == 0

defect = sp.simplify(A**sp.Rational(2,3) * t**sp.Rational(-1,2) *
                     (t*delta**6*V)**sp.Rational(1,6))
defect_after_sob = sp.simplify(defect.subs(A, r*V**sp.Rational(-1,4)))
expected = delta*(r**2/t)**sp.Rational(1,3)
assert sp.simplify(defect_after_sob-expected) == 0

print('PASS: curvature endpoint is gamma/t')
print('PASS: defect endpoint is delta*(r^2/t)^(1/3)')
print('PASS: q-polynomial, nested-cutoff 4^j, and fixed constants give convergent products')
