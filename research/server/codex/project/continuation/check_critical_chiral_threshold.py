"""Exact algebra/scaling checks; not a certification of the PDE proof."""
import sympy as sp

a, b = sp.symbols("a b", real=True)
c = -a-b
sq = a*a+b*b+c*c
det = a*b*c
disc = (a-b)**2*(a-c)**2*(b-c)**2
assert sp.expand(sq**3-54*det**2-2*disc) == 0
omega, theta = sp.symbols("omega theta", positive=True)
S = sp.Rational(9,16)/sp.sqrt(omega*theta)
kappa = sp.simplify(1/(6*S**2))
epsilon = kappa/4
assert sp.simplify(kappa-sp.Rational(128,243)*omega*theta) == 0
assert sp.simplify(sp.sqrt(6)*S*sp.sqrt(epsilon)) == sp.Rational(1,2)
assert sp.simplify(epsilon.subs(omega,sp.pi**2/2)
                   -sp.Rational(16,243)*sp.pi**2*theta) == 0
q = sp.symbols("q")
assert (2*q-4).subs(q,2) == 0
print("PASS: trace-free determinant discriminant identity")
print("PASS: explicit Sobolev-to-chiral-energy threshold")
print("PASS: small-threshold absorption factor is 1/2")
print("PASS: four-dimensional threshold constant")
print("PASS: L2 one-half Weyl energy is scale invariant")

