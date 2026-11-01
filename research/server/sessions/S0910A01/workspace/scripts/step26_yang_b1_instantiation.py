#!/usr/bin/env python3
"""
Step 26: instantiate Yang Appendix B.1 for the weighted defect velocity.

Yang B.1 (notation adapted) in dimension n=4 gives, for p0=q=6,

  |chi^2 f|(x,t) <= C S^(1/3) [t^-1 + alpha]^(1/2)
                    ( int_{time slab} int chi^8 f^6 )^(1/6)

where S is the Sobolev coefficient in ||u||_4^2 <= S(||grad u||_2^2+B/S||u||_2^2),
alpha = |dchi|^2 + S^2 mu^3 + S^{-1}B, and
mu^3 controls int chi^2 F^3 for the curvature potential.

Inputs from the support-local route:
  S <= C_S r^2 V^{-1/2}
  J6(s)=int chi^8 |E|^6 <= C delta^6 V
  S^2 Y(s)=S^2 int chi^2 F^3 <= C beta^3/t on the slab [t/2,t]
  |dchi|^2 + S^{-1}B <= C r^-2.

This script checks the exponents only.
"""
import sympy as sp

r, V, t, delta, beta = sp.symbols("r V t delta beta", positive=True)
S = r**2 * V ** sp.Rational(-1, 2)
J6_time = t * delta**6 * V
# Yang prefactor ignoring constants and exp(C alpha t), with t^-1 dominating r^-2 on t<=theta r^2.
yang_prefactor = S ** sp.Rational(1, 3) * (t ** -1) ** sp.Rational(1, 2) * J6_time ** sp.Rational(1, 6)
expected = delta * r ** sp.Rational(2, 3) * t ** sp.Rational(-1, 3)
print("Yang B.1 n=4,p0=q=6 exponent check")
print("S ~", S)
print("J6_time^(1/6) ~", sp.simplify(J6_time ** sp.Rational(1, 6)))
print("prefactor ~", sp.simplify(yang_prefactor))
print("expected  ~", expected)
assert sp.simplify(yang_prefactor / expected - 1) == 0

# Curvature potential alpha from q=6.  If S^2 Y <= beta^3/t then S^2 mu^3 <= beta^3/t.
alpha_potential = beta**3 / t
alpha_times_t = sp.simplify(alpha_potential * t)
print("potential alpha contribution S^2 mu^3 <=", alpha_potential)
print("(S^2 mu^3)*t <=", alpha_times_t, "(small when beta is small)")

# On t<=theta r^2, the geometric terms r^-2 are controlled by theta/t.
theta = sp.symbols("theta", positive=True)
geom_alpha_t_at_end = sp.simplify((r**-2) * (theta * r**2))
print("r^-2 * (theta r^2) =", geom_alpha_t_at_end)

# Integrability from 0 to theta*r^2.
integral = sp.integrate(expected, (t, 0, theta*r**2))
print("Integral of delta*r^(2/3)*t^(-1/3) to theta*r^2 =", sp.simplify(integral))
assert sp.simplify(integral - sp.Rational(3, 2)*delta*theta**sp.Rational(2, 3)*r**2) == 0

print("PASS: Yang B.1 instantiation produces support-wide |aE| <= C delta (r^2/t)^(1/3) with integrable drift, assuming the stated J6 and Y inputs.")
