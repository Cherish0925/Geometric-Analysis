"""Symbolic checks for the Step 16 q^+ rescaled-monopole repair.

This checks only the finite-dimensional/integral algebra.  It does not check
existence of Seiberg--Witten solutions or analytic compactness.
"""
import sympy as sp

# Formal nonnegative scalar integral variables.
Ep, I, eps, V, Hinv = sp.symbols("Ep I eps V Hinv", nonnegative=True)
F = Ep + 2 * eps * I + eps**2 * V
G = Ep - eps * I + eps**2 * V - eps**3 * Hinv
weighted_amgm = sp.expand(F / 3 + 2 * G / 3)
expected = Ep + eps**2 * V - sp.Rational(2, 3) * eps**3 * Hinv
assert sp.simplify(weighted_amgm - expected) == 0
print("PASS 1: (F/3 + 2G/3) = Ep + eps^2 V - (2/3) eps^3 int(1/(r+eps)).")

# Pointwise polynomial division behind G:
r = sp.symbols("r", nonnegative=True)
identity = sp.simplify(r**3 / (r + eps) - (r**2 - eps*r + eps**2 - eps**3/(r+eps)))
assert identity == 0
print("PASS 2: r^3/(r+eps) polynomial-division identity.")

# Corrected exact deficit decomposition.
# X, A, z are positive; Z=z^3.  P,N,H1,H2,J are nonnegative.
X, A, z = sp.symbols("X A z", positive=True)
P, N, H1, H2, J, beta = sp.symbols("P N H1 H2 J beta", nonnegative=True)
Z = z**3
# H1 = X Z^(2/3) - int r u^2 and int r u^2 = Z+P+N.
relation_X = sp.Eq(X*z**2, Z + P + N + H1)
# H2 = A Z^(2/3) - C and C=beta+18J.
relation_A = sp.Eq(A*z**2, beta + 18*J + H2)
# L^+ = A X^2. Substitute X=(z^3+P+N+H1)/z^2 and
# A=(beta+18J+H2)/z^2, then compare with proposed formula.
X_expr = (z**3 + P + N + H1) / z**2
A_expr = (beta + 18*J + H2) / z**2
lhs = sp.expand(A_expr * X_expr**2 - beta)
coefficient = A_expr * (X_expr + z) / z**2
rhs = sp.expand(18*J + H2 + coefficient * (P + N + H1))
assert sp.simplify(lhs-rhs) == 0
print("PASS 3: L_f^+ - beta corrected decomposition, with favorable N=int q^- u^2.")

# Negative-part control: if beta <= Ep and Ep+En-beta <= C Q,
# then En <= total deficit algebraically.
En, total_def = sp.symbols("En total_def", nonnegative=True)
# total_def = Ep+En-beta; rearrange En = total_def-(Ep-beta).
assert sp.simplify(En - (total_def - (Ep-beta))).subs(total_def, Ep+En-beta) == 0
print("PASS 4: beta <= Ep implies ||q^-||_2^2 <= int q^2-beta.")

# Calibrated amplitude constant from |2pi H| = (9/2)/(3 sqrt 2).
amp = sp.simplify((sp.Rational(9,2)/(3*sp.sqrt(2)))/(2*sp.pi))
assert sp.simplify(amp - 3/(4*sp.sqrt(2)*sp.pi)) == 0
print("PASS 5: limiting |H| = 3/(4 sqrt(2) pi).")

print("All q^+ repair algebra checks passed.")
