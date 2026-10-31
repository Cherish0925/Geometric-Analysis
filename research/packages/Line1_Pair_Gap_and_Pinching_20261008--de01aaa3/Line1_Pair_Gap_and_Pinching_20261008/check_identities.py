"""Exact rational checks for the displayed algebra; not a PDE solver."""
from pathlib import Path
import json
import sympy as s

x = s.symbols('x', real=True)
D = 1 + 3*x*x
r1 = -3*(x-1)**2*(21*x**4+18*x**3+12*x**2-2*x-1)/D**3
r2 = -3*(x+1)**2*(21*x**4-18*x**3+12*x**2+2*x-1)/D**3
r3 = 9*(x-1)**2*(x+1)**2*(5*x*x-1)/D**3
checks = {}
def equal(name, lhs, rhs):
    residual = s.factor(lhs-rhs)
    if residual != 0:
        raise AssertionError(f'{name}: nonzero residual {residual}')
    checks[name] = True

equal('trace_Rplus', r1+r2+r3, -3)
equal('r1_minus_r2', r1-r2, 48*x**3/D**2)
equal('r3_minus_r2', r3-r2, 12*(x+1)**2*(3*x-1)*(3*x**3-3*x*x+x+1)/D**3)
equal('r2_derivative', s.diff(r2,x), 72*x*(x-1)**2*(x+1)*(3*x*x-3*x-2)/D**4)
equal('r3_upper_square', s.Rational(1,3)-r3, 4*(7-3*x*x)*(3*x*x-1)**2/(3*D**3))
equal('cubic_positivity', 3*x**3-3*x*x+x+1, 3*(x-s.Rational(1,3))**3+s.Rational(10,9))
z=s.symbols('z', nonnegative=True)
equal('r1_numerator_positive_shift', (21*x**4+18*x**3+12*x*x-2*x-1).subs(x,z+s.Rational(1,3)), 21*z**4+46*z**3+44*z*z+s.Rational(136,9)*z+s.Rational(16,27))
equal('sharp_sectional_upper', (r3.subs(x,1/s.sqrt(3))-1)/2, -s.Rational(1,3))
equal('sectional_infimum', s.limit((r2-1)/2,x,1,dir='-'), -2)
G=4*D/((1-x*x)**2*(9*x*x-1))
A1=4*(3*x-1)*D/(3*(1-x)*(1+x)**2)
A2=4*(3*x+1)*D/(3*(1-x)**2*(1+x))
A3=64*x*x/((1-x*x)*D)
f=64*x*D/(3*(1-x*x)**3)
equal('volume_density_squared', G*A1*A2*A3, f*f)
equal('volume_divergence_coefficient', s.limit(f*(1-x)**3,x,1,dir='-'), s.Rational(32,3))

j=s.symbols('j', real=True)
C=3*(4-j)/(4*(1-j))
equal('Cj_bound_remainder', 3+3*j-C, 3*j*(1-4*j)/(4*(1-j)))
equal('topology_upper_t', (2*C-2)/(C+1), (16+2*j)/(16-7*j))
y=s.symbols('y',nonnegative=True)
projection_remainder = s.factor(9*(3+5*y*y)**2*(s.Rational(1,3)-y*y/3+(1-y*y-4*y)**2/(3+5*y*y)**2-s.Rational(4,9)+2*y))
checks['projection_remainder_polynomial'] = str(projection_remainder)
# Positivity of the above on [0,1/16] using an exact Bernstein representation.
poly=s.Poly(s.expand(projection_remainder.subs(y,z/16)),z)
n=poly.degree()
a=[poly.nth(k) for k in range(n+1)]
bern=[s.factor(sum(a[k]*s.binomial(i,k)/s.binomial(n,k) for k in range(i+1))) for i in range(n+1)]
assert all(b>=0 for b in bern)
checks['projection_remainder_nonnegative_Bernstein_on_0_1over16']= [str(b) for b in bern]
equal('beta_upper_cost', s.Rational(4,3)*y*y+16*y+6*(y+y*y)+72*y, 94*y+s.Rational(22,3)*y*y)
checks['upper_cost_below_100sqrt_d'] = bool(s.Rational(22,3)/16 < 6)
checks['scope'] = 'Checks exact finite algebra. Actual monopole supply, FD2, model completeness, Hodge theory and analytic continuation are explicit inputs in the mathematical text.'
path=Path(__file__).with_name('exact_checks.json')
path.write_text(json.dumps(checks,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(checks,ensure_ascii=False,indent=2))
