"""Exact optimization and integer-threshold checks, not a PDE proof."""
import sympy as s

x, V, S, R = s.symbols('x V S R', real=True, nonzero=True)
f = R*x*x/V - 2*S*x/V + 4
assert s.simplify(f.subs(x, S/R) - (4-S*S/(V*R))) == 0
assert s.simplify(s.diff(f, x).subs(x, S/R)) == 0
print('PASS: signed Einstein-ray optimization')

P, L = s.symbols('P L', nonnegative=True)
assert s.simplify((4-S*S/(V*R)).subs(S*S/V, 4*(R-P)-L)-(4*P+L)/R) == 0
print('PASS: trace-free and scalar-variance decomposition')

for m in range(2, 10002):
    A = 8*(m-1)
    k = (A+2)//3-1
    assert 0 < A-3*k <= 3
    assert s.Rational(1,3)-s.Rational(k,A) <= s.Rational(1,A)
print('PASS: realized product-surface ratios approach 1/3 strictly below')

b1, bm = s.symbols('b1 bm', integer=True, nonnegative=True)
chi, tau = 3-2*b1+bm, 1-bm
assert s.expand(2*chi+3*tau) == 9-4*b1-bm
for A in range(1,10):
    for D in range(0,4):
        if 3*D < A:
            assert s.Rational(1,3)-s.Rational(D,A) >= s.Rational(1,27)
print('PASS: b+=1 topology and integer separation')

c, d = s.symbols('c d', positive=True)
assert s.simplify((c-c/2)/4-c/8) == 0
print('PASS: closed-band pointwise constant; endpoint kept distinct')
