"""Exact checks for global.md; these are algebraic data, never metric certificates."""
import sympy as s

x, t, eps, kappa = s.symbols("x t eps kappa", positive=True)
a = s.sqrt(1 - 11*t*t)
mean_square_amplitude = (a*a + 11*t*t)/12
assert s.simplify(mean_square_amplitude - s.Rational(1, 12)) == 0
spectral = 2*((s.Rational(8, 3) + 2*a)**2/12
              + 11*(s.Rational(8, 3) + 2*t)**2/12)
expected_spectral = (134 + 16*(a + 11*t))/9
assert s.simplify(spectral - expected_spectral) == 0
mixed = 2*((4 + s.sqrt(12)*a)**2/12
           + 11*(4 + s.sqrt(12)*t)**2/12)
expected_mixed = 34 + s.Rational(8, 3)*s.sqrt(3)*(a + 11*t)
assert s.simplify(mixed - expected_mixed) == 0
assert s.simplify(spectral.subs(t, 0) - s.Rational(50, 3)) == 0
assert s.simplify(432 - 18*spectral.subs(t, 0) - 132) == 0
F = 4*s.sqrt(x) + s.sqrt(6 - 2*x)
# Exact derivative signs prove concavity throughout 0<x<3.
expected_second = -1/x**s.Rational(3, 2) - (6 - 2*x)**s.Rational(-3, 2)
assert s.simplify(s.diff(F, x, 2) - expected_second) == 0
assert s.simplify(F.subs(x, 1) - 6) == 0
gap = s.sqrt(1 + 3*kappa) - 1
assert s.simplify(8*gap + 4*gap*gap - 12*kappa) == 0
# Graph model: scalar=-12, traceless Ricci squared=4 eps^2.
ricci_cgb = s.Rational(144, 24) - 2*eps*eps
weyl_mean = 2*eps*eps
assert s.simplify(ricci_cgb + weyl_mean - 6) == 0
spike_fraction = eps*eps/8
assert s.simplify(spike_fraction * 16 - weyl_mean) == 0
assert s.simplify(2*weyl_mean - 4*eps*eps) == 0
for point in (s.Rational(101, 100), s.Rational(3, 2), 2,
              s.Rational(9, 4), s.Rational(299, 100)):
    assert float((F*F).subs(x, point)) > 36
generic_t = s.Rational(1, 100)
assert float(spectral.subs(t, generic_t)) > 16
assert float(mixed.subs(t, generic_t)) > 36
assert float((a - s.Rational(1, 3)).subs(t, generic_t)) > 0
print("Exact algebraic checks passed.")
print("E_D x=2 generic witness spectral integral/V*:",
      s.N(spectral.subs(t, generic_t), 14))
print("E_D x=2 generic witness mixed integral/V*:",
      s.N(mixed.subs(t, generic_t), 14))
print("Witnesses are algebraic curvature distributions, not metrics.")
