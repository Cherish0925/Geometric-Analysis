#!/usr/bin/env python3
"""Finite symbolic checks for round14_global.md; no PDE validation."""

import sympy as s

t, k, ell, B = s.symbols("t k ell B", positive=True)
q, w = s.symbols("q w")


def check(name, residual):
    result = s.simplify(s.expand(residual))
    if result != 0:
        raise AssertionError(f"{name}: residual {result}")
    print(f"PASS {name}")


profile = s.sech(k*t)**3
check("Maxwell profile",
      s.diff(profile, t) + 3*k*s.tanh(k*t)*profile)
wrong_profile = s.sech(k*t)**2
if s.simplify(s.diff(wrong_profile, t)
              + 3*k*s.tanh(k*t)*wrong_profile) == 0:
    raise AssertionError("Incorrect sech^2 Maxwell profile accepted")
print("PASS wrong profile rejected")

diagonal = [-q, q, -q, 0]
check("Scalar trace", sum(diagonal) + q)
tracefree = [entry + q/4 for entry in diagonal]
check("Tracefree trace", sum(tracefree))
check("Tracefree norm", sum(entry**2 for entry in tracefree) - 11*q**2/4)

# y=tanh(kt) transforms sech^m(kt) dt to
# k^{-1}(1-y^2)^{m/2-1}dy, whose beta integral is B(1/2,m/2).
def full_integral(m):
    return s.gamma(s.Rational(1, 2))*s.gamma(s.Rational(m, 2))/(
        k*s.gamma(s.Rational(m+1, 2)))

J3 = full_integral(3)
J7 = full_integral(7)
check("Integral sech^3", J3 - s.pi/(2*k))
check("Integral sech^7", J7 - 5*s.pi/(16*k))
c = ell/(2*s.pi)
check("Scalar loss coefficient",
      s.pi*c**3*B/J3 - k*B*ell**3/(4*s.pi**3))
check("Tracefree Ricci coefficient",
      s.Rational(11, 4)*s.pi*c**5*J7/(2*J3**4)
      - 55*k**3*ell**5/(256*s.pi**7))

# Subtract the scalar equation at v=1. D denotes Delta(w).
D = s.symbols("D")
expanded_equation = -6*D-(12+q)*(1+w)+12*(1+w)**3
stated_equation = -6*D+24*w-q*(1+w)+36*w**2+12*w**3
check("Scalar equation expansion", expanded_equation-stated_equation)

# Integrated symbols: p=int Q, p1=int Qw, rj=int w^j.
p, p1, r1, r2, r3, r4 = s.symbols("p p1 r1 r2 r3 r4")
integral_r1 = (p+p1-36*r2-12*r3)/24
volume = (4*r1+6*r2+4*r3+r4).subs(r1, integral_r1)
check("Exact volume cancellation",
      volume-(p/s.Integer(6)+p1/s.Integer(6)+2*r3+r4))

# A constant scalar loss gives v=sqrt(1+q/12); test the pointwise
# integrated identity at this exact constant solution.
v = s.sqrt(1+q/12)
check("Constant-loss scalar equation", -(12+q)*v+12*v**3)
check("Constant-loss volume identity",
      v**4-1-q/6-q*(v-1)/6-2*(v-1)**3-(v-1)**4)

chi = s.symbols("chi", positive=True)
Vstar = 4*s.pi**2*chi/9
check("Yamabe normalization", -12*s.sqrt(Vstar)+8*s.pi*s.sqrt(chi))
check("Yamabe deficit coefficient",
      6/s.sqrt(Vstar)*(k*B*ell**3/(24*s.pi**3))
      - k*B*ell**3/(4*s.pi**3*s.sqrt(Vstar)))
e = s.symbols("e", positive=True)
lam = s.symbols("lam", real=True, nonzero=True)
defect = (e+4*(lam+3)**2)/lam**2
lam_star = -3-e/12
check("Relative integral defect stationary scale",
      s.diff(defect, lam).subs(lam, lam_star))
check("Relative integral defect minimum",
      defect.subs(lam, lam_star)-4*e/(36+e))
check("Relative integral defect completed square",
      defect-4*e/(36+e)
      -(36+e)*(1/lam+12/(36+e))**2)
A_F, c_symbol = s.symbols("A_F c", positive=True)
H_norm_sq = 4*s.pi*A_F*c_symbol*J3
check("Receiver squared norm coefficient",
      H_norm_sq-2*s.pi**2*A_F*c_symbol/k)
check("Integral defect lower coefficient",
      (3*k*B*c_symbol**3)**2/H_norm_sq
      -9*k**3*B**2*c_symbol**5/(2*s.pi**2*A_F))
print("All 19 exact identities and one intentional wrong profile passed.")
