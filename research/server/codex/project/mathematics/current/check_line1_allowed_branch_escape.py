"""Exact normalization checks only; compactness/topology are in the proof."""
import sympy as s

t, z, theta, T, V, chi = s.symbols("t z theta T V chi", positive=True)
b = 4 * t * z
lam = [-4*t/3, 2*t/3-b/2, 2*t/3+b/2]
assert s.simplify(sum(lam)) == 0
assert s.simplify(sum(x*x for x in lam) - (s.Rational(8,3)*t*t+b*b/2)) == 0
tmax = 1/(2*(1-3*theta*theta))
assert s.simplify(2*tmax - 4*(1-3*theta*theta)*tmax*tmax) == 0

# Einstein Chern--Weil: 4 pi^2 T = (2/3)V + 2 int|W+|^2.
wavg = 2*s.pi**2*T/V - s.Rational(1,3)
assert s.simplify(4*s.pi**2*T - (s.Rational(2,3)*V + 2*V*wavg)) == 0
assert s.simplify(wavg.subs(V, 2*s.pi**2*T) - s.Rational(2,3)) == 0

# Exact KE spectral normalization and the zero of the older h^2 bound.
assert [x.subs({t:s.Rational(1,2), z:0}) for x in lam] == [-s.Rational(2,3), s.Rational(1,3), s.Rational(1,3)]
assert s.simplify((1-T/T)**2) == 0

# Shear chi=4, T=8: lower monopole volume and upper CGB volume differ by 3.
assert s.simplify((12*s.pi**2*chi)/(2*s.pi**2*(2*chi))) == 3

# Deliberate mistakes in endpoint normalization and maximum-principle sign.
assert s.simplify(wavg.subs(V, s.pi**2*T) - s.Rational(2,3)) != 0
assert s.simplify(2*tmax + 4*(1-3*theta*theta)*tmax*tmax) != 0
print("8 exact normalization checks and 2 deliberate-error checks passed")
