"""Finite algebra checks only. These are not PDE or global-proof verification."""
from __future__ import annotations
import json
from pathlib import Path
import sympy as s

eps, lam = s.symbols('eps lam', positive=True)
x, y = s.symbols('x y', positive=True)
e = s.symbols('e', positive=True)
rho = s.Rational(4, 3)
m = s.Rational(128, 81)
results: dict[str, object] = {}
results['spectral_integral_to_infinity'] = str(s.integrate(lam**2/(1+eps*lam)**2, (eps, 0, s.oo)))
assert results['spectral_integral_to_infinity'] == 'lam'
T = lambda z: z/(1+z)
expr = s.factor((T(x)-T(y))*(x-y) - (x-y)**2/((1+x)*(1+y)))
assert expr == 0
results['covariance_identity_residual'] = str(expr)
coefficient = s.Rational(9,8)*rho**6/(2*m)
assert coefficient == 2
results['fit_cancellation_coefficient'] = str(coefficient)
results['fifth_line_squared_amplitude'] = str(4*rho*m**3)
results['determinant_square_density_times_pi_squared'] = str(s.Rational(25,6))
gamma = e/(1+e)
rate_margin = s.factor(e/(2*(2+e)) - gamma/8)
results['deweighting_rate_minus_gamma_over_8'] = str(rate_margin)
assert s.simplify(rate_margin - e*(3*e+2)/(8*(e+1)*(e+2))) == 0
# eta^gamma/(...) tail and torsion mass rate used in the proof.
Mexp = 1/(4*(1+e))
assert s.simplify(s.Rational(1,4)-Mexp - gamma/4) == 0
assert s.simplify(e*Mexp - gamma/4) == 0
results['mass_truncation_two_exponents'] = 'both gamma/4 for squared L2 error'
results['scope'] = 'scalar identities and exponent comparisons; no certification of analytic estimates'
out = Path(__file__).with_name('finite_algebra_checks.json')
out.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(results, ensure_ascii=False, indent=2))
