"""Exact algebra only; not a validation of compactness or PDE input."""
import sympy as s

A, P, Wm, p = s.symbols("A P Wm p", real=True)
S = 32*s.pi**2*A + 12*P - 48*Wm
Wp = (4*s.pi**2*A - S/24 + P/2)/2
D2 = s.Rational(3, 2)*(S + 12*Wp) - 72*s.pi**2*p
assert s.simplify(D2 + 72*s.pi**2*(p-A) + 54*Wm - 18*P) == 0
assert s.simplify(S/24 + 2*Wm - P/2 - 4*s.pi**2*A/3) == 0
assert s.simplify(D2.subs({P: 0, Wm: 0, p: A})) == 0
print("PASS: two exact balances and complex-hyperbolic equality calibration")
