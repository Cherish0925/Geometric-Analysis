"""Exact scalar checks; no claim to verify the cited geometric theorems."""

import sympy as s

delta, A, B, D, h = s.symbols("delta A B D h", nonnegative=True)
pi = s.pi

# Holo-sectional curvature -4: Ric=-6g, entropy=4. Rescale by six.
entropy_fourth = s.Rational(4**4, 6**2)
assert entropy_fourth == s.Rational(64, 9)
bishop_fourth = 9 * (1 + delta) ** 2
target_volume = 2 * pi**2 * B
entropy_volume = entropy_fourth * D * target_volume / bishop_fourth
monopole_volume = 2 * pi**2 * A / (1 + delta) ** 2
assert s.simplify(entropy_volume / monopole_volume) == 64 * B * D / (81 * A)

# D*B<=A means the maximal target-derived bound is 64/81 of the SW bound.
ratio = s.simplify((entropy_volume / monopole_volume).subs(B * D, A))
assert ratio == s.Rational(64, 81) < 1
assert s.Rational(1) - ratio == s.Rational(17, 81)

# Einstein: U=6(chi-3|tau|/2)/A and B=3 chi(Y).
chi_y = s.symbols("chi_y", positive=True)
kotschick_lower_U = s.Rational(6) / A * s.Rational(32, 81) * D * chi_y
assert s.simplify(kotschick_lower_U - (64 * B * D / (81 * A)).subs(B, 3 * chi_y)) == 0

# Classical R >= 8pi²(2A-T), with T=A(1-h), gives e>=1+h.
assert s.simplify((2 * A - A * (1 - h)) / A) == 1 + h

# Parametrize h by z=sqrt(1-3h): the classical envelope exceeds 1+h.
z = s.symbols("z", positive=True)
h_z = (1 - z**2) / 3
F_z = (4 - z) ** 2 / 9
assert s.factor(F_z - (1 + h_z)) == 4 * (z - 1) ** 2 / 9
assert s.simplify(F_z - (1 + h_z) - 4 * h_z**2 / (1 + z) ** 2) == 0

# Mutation checks prevent mistaking a lower bound for an upper budget,
# or using real-hyperbolic normalization for a complex-hyperbolic target.
assert entropy_fourth != 9
assert s.simplify(entropy_volume / monopole_volume) != 81 * B * D / (64 * A)
print("PASS: normalization, volume domination, energy and topology coefficients; all exact assertions and mutation checks")
