"""Exact algebra for the spectral application, not a PDE proof."""
import sympy as s

t, b, theta, h = s.symbols('t b theta h', real=True)
l1, l2, l3 = -4*t/3, 2*t/3-b/2, 2*t/3+b/2
norm = s.expand(l1*l1+l2*l2+l3*l3)
checks = {
    'trace': l1+l2+l3,
    'norm': norm-(s.Rational(8,3)*t*t+b*b/2),
    'lowest_gap': l2-l1-(2*t-b/2),
    'weyl_reaction': -s.Rational(3,4)*(2*l1+6*l1*l1-2*norm)
                       -(2*t-4*t*t+s.Rational(3,4)*b*b),
    'relative_reaction': (2*t-4*t*t+s.Rational(3,4)*b*b).subs(b,4*theta*t)
                       -(2*t-4*(1-3*theta**2)*t*t),
    'maximum_barrier': (2*t-4*(1-3*theta**2)*t*t).subs(
                       t, 1/(2*(1-3*theta**2))),
    'chern_weil_ke': s.Rational(1,3)+norm.subs({t:s.Rational(1,2),b:0})-1,
    'topological_rearrangement': s.Rational(8,3)*(s.Rational(1,4)-t*t)-b*b/2
                       -(s.Rational(2,3)-norm),
    'ke_endpoint': norm.subs({t:s.Rational(1,2),b:0})-s.Rational(2,3),
}
for name, expression in checks.items():
    assert s.simplify(expression) == 0, name
    print('PASS', name)

# A deliberate sign error in the eigenvalue reaction must be detected.
wrong = -s.Rational(3,4)*(2*l1+6*l1*l1-2*norm) - (2*t-4*t*t-b*b*3/4)
assert s.simplify(wrong) != 0
print('PASS rejects_wrong_splitting_sign')
print(f'{len(checks)+1} exact checks passed; no PDE certification claimed.')
