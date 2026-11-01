#!/usr/bin/env python3
"""Finite algebra checks only: not verification of global geometry or PDE."""
import sympy as s

a, z, q, zdot = s.symbols("a z q zdot", real=True)
metric = s.Matrix([[1 + a**2 * z**2 * q**2, a**2 * z * q],
                   [a**2 * z * q, a**2]])
assert s.simplify(metric.det() - a**2) == 0
variation = s.simplify(metric.inv() * metric.diff(z) * zdot)
assert s.simplify(s.trace(variation)) == 0
assert s.simplify(variation**2 - a**2 * q**2 * zdot**2 * s.eye(2)) == s.zeros(2)
shape = -variation / 2
assert s.simplify(s.trace(shape**2) - a**2*q**2*zdot**2/2) == 0

# For the diagonal test path h_t=diag(exp(2ct),exp(-2ct)),
# A^0 has operator norm 2|c| and J=|c|, equal to (log K)/2.
c, t = s.symbols("c t", positive=True)
diagonal = s.diag(s.exp(2*c*t), s.exp(-2*c*t))
assert s.simplify(diagonal.inv() * diagonal.diff(t)) == s.diag(2*c, -2*c)
assert s.integrate(c, (t, 0, 1)) == c

# A nonseparating twist is a rank-one symplectic transvection.
twist = s.Matrix([[1, 1], [0, 1]])
assert (twist - s.eye(2)).rank() == 1
symplectic = s.Matrix([[0, 1], [-1, 0]])
assert twist.T * symplectic * twist == symplectic
for genus in range(2, 9):
    action = s.diag(twist, s.eye(2*genus-2))
    assert 2*genus - (action-s.eye(2*genus)).rank() == 2*genus-1

# Bilateral deficit bound at V=2*pi^2*A and p >= A.
delta = s.symbols("delta", nonnegative=True)
bound = s.Rational(9, 2) * (4*(1+delta)**2 - 4)
assert s.expand(bound - (36*delta+18*delta**2)) == 0

# Fixed-support pinching profile Q=lambda*chi/C has no hidden inverse lambda.
lam, chi, cap = s.symbols("lam chi cap", positive=True)
u = s.symbols("u", real=True)
profile = chi/(cap*s.cosh(u))
assert s.simplify(lam*s.cosh(u)*profile - lam*chi/cap) == 0

print("PASS: determinant, trace-free shape, exact QC factor, transvection rank, "
      "bilateral budget, and pinching-profile cancellation.")
print("Scope: finite algebra only; no computational claim about theorem proofs.")
