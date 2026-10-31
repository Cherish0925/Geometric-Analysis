"""Exact algebra in the positive-branch corollary; no PDE certification."""

import sympy as s

x = s.symbols('x', real=True)
lower = (4 - 2*x)**2 / 24 - x**2 / 2
assert s.expand(lower - s.Rational(1, 4)
                - (s.Rational(1, 2)-x)*(4*x+10)/12) == 0
upper = s.Rational(1, 4)/2 * (s.Rational(2, 3)+s.Rational(1, 4))
assert upper == s.Rational(11, 96) < s.Rational(1, 4)
print('PASS: positive-branch scalar and Chern--Weil bounds are incompatible')

lam, V, R2 = s.symbols('lam V R2', positive=True)
S = s.symbols('S', nonzero=True, real=True)
energy = R2/(V*lam**2) - 2*S/(V*lam) + 4
critical = R2/S
assert s.simplify(s.diff(energy, lam).subs(lam, critical)) == 0
assert s.simplify(energy.subs(lam, critical) - (4-S**2/(V*R2))) == 0
assert s.simplify(s.diff(energy, lam, 2).subs(lam, critical)
                  - 2*S**4/(V*R2**3)) == 0
assert s.simplify(energy - (4-S**2/(V*R2))
                  - R2/V*(1/lam-S/R2)**2) == 0
print('PASS: exact global optimization over nonzero signed normalization')

P, svar = s.symbols('P svar', nonnegative=True)
ric_energy = P + (svar+S**2/V)/4
assert s.simplify((4-S**2/(V*ric_energy))
                  -(4*P+svar)/ric_energy) == 0
print('PASS: optimized defect is the trace-free/scalar-variation energy fraction')
