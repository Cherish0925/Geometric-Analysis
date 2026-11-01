#!/usr/bin/env python3
"""Exact symbolic checks for Step 3 Ishida--LeBrun boundary constants."""
import sympy as sp

A, d = sp.symbols('A d', positive=True)
q = 3*d**2/(1-d)**2
T = sp.Rational(2, 3)*A
Rmax = sp.simplify(q*T/(1-q))
print('q(delta) =', q)
print('Rmax normalized CGB variable =', sp.factor(Rmax))

# S,W solve I=2A/3, and square saturation K=A.
# With x=-s approximately 4 and y=|W+| approximately constant, square saturation
# enforces x=8 sqrt(6)y. Thus Wvar=(1/(4pi2))*2 int y^2 = S/8.
S, W = sp.symbols('S W')
sol = sp.solve([sp.Eq(S+W, T), sp.Eq(W, S/8)], [S, W], dict=True)[0]
print('S =', sol[S], 'W =', sol[W])

# Volume from S=(1/(4pi^2))*int s^2/24 and s^2 -> 16.
# Hence S = Vol/(6 pi^2).
vol_over_pi2 = sp.simplify(6*sol[S])
print('Vol/pi^2 =', vol_over_pi2)
# int |W+|^2 / pi^2 = 2 W
print('int|W+|^2/pi^2 =', sp.simplify(2*sol[W]))
# int |Ric|^2 = int (s^2/4+|Ric0|^2); Ric0->0; int s^2=96 pi^2 S.
print('int|Ric|^2/pi^2 =', sp.simplify(24*sol[S]))
# Boundary integral infimum I_r = 8 pi^2(A+D), D=A/3.
print('I_r infimum/pi^2 =', sp.simplify(8*(A+A/3)))

# Pointwise completion-square identity, variables s,w.
s, w = sp.symbols('s w', real=True)
L = s**2/sp.Integer(24) + 2*w**2
Kraw = (s-sp.sqrt(6)*w)**2
identity = sp.expand(27*L-Kraw-(s+8*sp.sqrt(6)*w)**2/sp.Integer(8))
print('completion-square residual =', sp.simplify(identity))

# Full GB coefficient: 8pi2 chi = int(|W|^2+s^2/24-|Ric0|^2/2)
# under |s|>=4(1-d), |Ric0|^2<=4d^2.
b = sp.simplify(sp.Rational(2,3)*(1-d)**2-2*d**2)
print('full GB volume coefficient b(delta) =', sp.expand(b))
assert sp.simplify(identity) == 0
assert sol[S] == sp.Rational(16,27)*A
assert sol[W] == sp.Rational(2,27)*A
assert vol_over_pi2 == sp.Rational(32,9)*A
print('ALL SYMBOLIC CHECKS PASSED')
