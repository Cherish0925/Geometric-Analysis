"""Exact algebra checks for the resolution concentration theorem.

Run: qiushi-yau26 env numeric python round7_endpoint_check.py
This checks coefficients and model specializations, not geometric existence.
"""

import sympy as s


def equal(actual, expected, label):
    residual = s.simplify(actual - expected)
    assert residual == 0, (label, residual)
    print(f"PASS {label}")


w, V, E, m = s.symbols("w V E m", nonnegative=True)
pi = s.pi
T_density = (s.Rational(2, 3) + 2*w**2)/(4*pi**2)
J_density = (4+s.sqrt(6)*w)**2/(72*pi**2)
F_density = (4-8*s.sqrt(6)*w)**2/(864*pi**2)
equal(T_density-s.Rational(2, 3)*J_density, F_density,
      "bulk square completion with denominator 864")
equal(F_density, 4*(w-1/(2*s.sqrt(6)))**2/(9*pi**2),
      "identical bulk-variance and concentration coefficients")
assert s.simplify(T_density-s.Rational(2, 3)*J_density
                  -2*F_density) != 0
print("PASS deliberate denominator-432 mutation rejected")

equal(E/(2*pi**2)-s.Rational(2, 3)*E/(12*pi**2),
      4*E/(9*pi**2), "concentration coefficient")
equal((4*E/(9*pi**2)).subs(E, 12*pi**2*m),
      16*m/3, "A1 chirality specialization")
equal(T_density.subs(w, 0)/J_density.subs(w, 0),
      s.Rational(3, 4), "real hyperbolic ratio")
equal(T_density.subs(w, s.sqrt(s.Rational(2, 3))),
      1/(2*pi**2), "Kahler topology density")
equal(J_density.subs(w, s.sqrt(s.Rational(2, 3))),
      1/(2*pi**2), "Kahler monopole density")

x = s.symbols("x", nonnegative=True)
R = 6*(x**2+2)/(x+4)**2
equal(R-s.Rational(2, 3), 4*(2*x-1)**2/(3*(x+4)**2),
      "opposite Kahler exact critical remainder")
equal(s.diff(R, x), 24*(2*x-1)/(x+4)**3,
      "unique critical value")
equal(24/(s.Rational(1, 2)**2+8), s.Rational(32, 11),
      "critical Chern slope")
equal(R.subs(x, 0), s.Rational(3, 4), "CH2 reversed")
equal(R.subs(x, 2), 1, "H2 times H2 reversed")

w_star = 1/(2*s.sqrt(6))
det_bound = s.simplify(w_star**3/(3*s.sqrt(6)))
equal(det_bound, s.Rational(1, 864), "critical determinant bound")
equal(2*w_star**2-18*det_bound, s.Rational(1, 16),
      "Weitzenbock lower gradient value")
equal(2*w_star**2+18*det_bound, s.Rational(5, 48),
      "Weitzenbock upper gradient value")
equal(J_density.subs(w, w_star), s.Rational(9, 32)/pi**2,
      "critical monopole capacity density")

print("All exact checks passed. No Einstein existence or novelty is certified.")
