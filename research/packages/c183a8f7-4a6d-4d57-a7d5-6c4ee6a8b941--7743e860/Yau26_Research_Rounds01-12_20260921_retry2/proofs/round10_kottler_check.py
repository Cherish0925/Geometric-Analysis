"""Exact Ricci and optical checks for the doubled extremal Kottler family."""

import json
import sympy as s

y, d = s.symbols("y d", positive=True)
k = s.sqrt(3)
r = (1+y)/k
F = y*y*(y+3)/(3*(y+1))


def dr(expr):
    return k*s.diff(expr, y)


def errors(q):
    # Proper radial coordinate satisfies dr/dt=sqrt(q), a=sqrt(F), b=r.
    a_second_over_a = q*dr(dr(F))/(2*F) + dr(q)*dr(F)/(4*F) - q*dr(F)**2/(4*F**2)
    return tuple(s.factor(z) for z in (
        3-a_second_over_a-dr(q)/r,
        3-a_second_over_a-q*dr(F)/(r*F),
        3-1/r**2-dr(q)/(2*r)-q/r**2-q*dr(F)/(2*r*F),
    ))


checks = []
assert errors(F) == (0, 0, 0)
checks.append("exact_extremal_Kottler")
q = F*(1-d*d/(y*y))
expected = (
    -3*d*d/(y*(y+1)**2),
    d*d*(2*y+3)/(y*(y+1)**2),
    d*d*(2*y+3)/(y*(y+1)**2),
)
assert all(s.factor(a-b) == 0 for a, b in zip(errors(q), expected))
checks.append("three_full_Ricci_error_eigenvalues")
u = s.symbols("u", real=True)
smooth_rr = s.factor(((s.diff(r, y)**2)*(y*y-d*d)/q))
assert s.factor(smooth_rr-(y+1)/(y+3)) == 0
checks.append("smooth_even_doubling_radial_coefficient")
assert s.factor(s.diff(expected[1], y) + d*d*(4*y*y+9*y+3)/(y*y*(y+1)**3)) == 0
checks.append("global_error_maximum_at_neck")
w = (y+1)**s.Rational(3,2)/(y*s.sqrt(y+3))
assert s.simplify(s.diff(s.log(w), y)+3/(y*(y+1)*(y+3))) == 0
checks.append("optical_groundstate_maximum")

# The cutoff changes only q; Ricci depends linearly on q and dq/dr.
z, zp = s.symbols("z zp", real=True)
chi = s.Function("chi")(y)
cut_errors = errors(F*(1-d*d*chi/(y*y)))
for expr in cut_errors:
    coefficient = s.cancel(expr/(d*d))
    assert not coefficient.has(d)
    assert not coefficient.has(s.diff(chi, y, 2))
    assert s.denom(coefficient).subs(y, 1) != 0
checks.append("fixed_cutoff_error_exactly_quadratic_in_d")

# Fixed-u parameter differentiation includes dy/d(log d)=y.
def parameter_derivative(expr):
    return d*s.diff(expr, d) + y*s.diff(expr, y)

variation_eigenvalues = (
    2*y/((1+y)*(3+y)),
    2+y/(y+3)-y/(y+1),
    2*y/(1+y),
)
metric_coefficients = ((1+y)/(3+y), F, r*r)
assert all(s.factor(parameter_derivative(a)/a-b) == 0
           for a, b in zip(metric_coefficients, variation_eigenvalues))
checks.append("fixed_u_metric_parameter_variation")
error_multipliers = ((1-y)/(1+y), (y+3)/((2*y+3)*(1+y)))
assert all(s.factor(parameter_derivative(a)-m*a) == 0
           for a, m in zip(expected[:2], error_multipliers))
assert s.factor(2-variation_eigenvalues[1]-2*y/((1+y)*(3+y))) == 0
checks.append("approximate_Jacobi_error_and_nongauge_neck_variation")

# Cotler--Jensen's shrinking torus bottleneck is not small Ricci error.
rho = s.symbols("rho", real=True)
log_a_prime = s.tanh(3*rho/2)
a_second_over_a = s.diff(log_a_prime, rho) + log_a_prime**2
torus_errors = (3-3*a_second_over_a,
                3-a_second_over_a-2*log_a_prime**2)
# Rationalize in exponentials: trigsimp alone leaves a noncanonical zero.
assert all(s.cancel((e-sign*s.Rational(3,2)/s.cosh(3*rho/2)**2).rewrite(s.exp)) == 0
           for e, sign in zip(torus_errors, (-1, 1)))
checks.append("off_shell_torus_bottleneck_defect_stays_three_halves")

print(json.dumps({"passed": len(checks), "checks": checks,
                  "cutoff_error_over_d_squared": [str(s.factor(e/(d*d))) for e in cut_errors]}, indent=2))
