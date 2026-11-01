#!/usr/bin/env python3
"""
Step 18 scaling model for full-support cutoff-flow energy terms.

The script records the dimensionless scaling behind the coupled estimates

  R' + X <= r^{-2}(R+P) + absorbable reactions,
  P' + Y <= r^{-2}P       + absorbable curvature-defect reaction.

It is not a PDE proof.  It verifies that the Sobolev factors and cutoff-gradient
terms have the expected powers of r and that collapsed volume cancels in the
four-dimensional L2 absorption.
"""
import sympy as sp

r, V, K0, eps = sp.symbols('r V K0 eps', positive=True)

# Relative Sobolev coefficient in dimension four and curvature L2 norm under
# average_U K^2 <= K0.
A = r**2 / sp.sqrt(V)
K_L2 = sp.sqrt(K0 * V)
prod = sp.simplify(A * K_L2)
print("A_U * ||K||_2 =", prod)
assert sp.simplify(prod - sp.sqrt(K0)*r**2) == 0

# Cutoff a=chi^2: |grad a|^2/a <= C/r^2.
cutoff_factor = r**(-2)
print("|grad a|^2/a scales as", cutoff_factor)

# Young model for |grad a| |grad E| K.
# Put X = sqrt(a)|grad E| and Y=(|grad a|/sqrt(a))K.  Then Y^2 scales r^-2 K^2.
X, Y = sp.symbols('X Y', positive=True)
young_gap = sp.simplify(eps*X**2 + Y**2/eps - 2*X*Y)
print("Young square residual:", sp.factor(young_gap - (eps*X - Y)**2/eps))
assert sp.simplify(young_gap - (eps*X - Y)**2/eps) == 0

# Normalized quantities in dimension four:
# R = r^4/V int K^2, P = r^4/V int E^2, X = r^4/V int a|grad K|^2.
# A cutoff-gradient remainder int r^-2 K^2 becomes r^-2 R after multiplying r^4/V.
normalized_cutoff_remainder = sp.simplify((r**4/V) * (r**(-2)) * (V/r**4))
print("Normalized cutoff remainder coefficient scales as", normalized_cutoff_remainder)
assert sp.simplify(normalized_cutoff_remainder - r**(-2)) == 0

# Reaction absorption schematic:
# int a K^3 <= ||K||_2 ||chi K||_4^2 <= prod * [int a|grad K|^2 + r^-2 int K^2].
# After normalization: prod * (X + r^-2 R).
print("Cubic curvature term normalizes to")
print("  (sqrt(K0) r^2) * (X + r^-2 R)")
print("Curvature-defect terms with chi E or chi K have the same small factor.")

# General dimension formula for the critical norm.
n = sp.symbols('n', positive=True)
A_n = r**2 / V**(sp.Rational(2,1)/n)
Kcrit = (K0*V)**(sp.Rational(2,1)/n)
prod_n = sp.simplify(A_n*Kcrit)
print("General dimension critical product:", prod_n)

print("PASS")
