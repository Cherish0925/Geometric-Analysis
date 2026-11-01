#!/usr/bin/env python3
"""Exact finite algebra for the signed harmonic-Weyl balance.

This does not mechanically verify global PDE or bundle arguments.
"""
import json
import sympy as s

z, t, u, u0, b, eps = s.symbols('z t u u0 b eps', positive=True)
rho = -s.Rational(1, 2) + s.Rational(3, 2)*z
k = (1-rho)/(2+rho)
checks = {}

def eq(name, lhs, rhs):
    assert s.simplify(lhs-rhs) == 0, name
    checks[name] = True

eq('normalized_connection_ratio', k, (1-z)/(1+z))
gradient = 2*(1+k*k)
exterior = (1-k)**2
potential_gradient = 3*exterior + gradient/2 - 4*(rho-(1+rho)*k*k)
eq('signed_gradient_coefficient', potential_gradient/gradient,
   s.Rational(3,2)*(1-z*z)/(1+z*z))
eq('closedness_ratio', exterior/gradient, z*z/(1+z*z))
a1,a2,a3,a4 = s.symbols('a1 a2 a3 a4', real=True)
c1,c2,c3,c4 = -k*a2,k*a1,-k*a4,k*a3
first_row = s.Matrix([-a4,-a3,a2,a1])*(1-rho) + s.Matrix([-c3,c4,c1,-c2])*(2+rho)
assert first_row.applyfunc(s.simplify) == s.zeros(4,1)
checks['signed_first_order_row'] = True
dw = (a1-c2)**2+(a2+c1)**2+(a3-c4)**2+(a4+c3)**2
eq('exterior_coframe_coefficients', dw, (1-k)**2*(a1*a1+a2*a2+a3*a3+a4*a4))
alpha = -s.Rational(4,3)*u
F = -s.Rational(3,4)/u
eq('signed_weight_normalization', F*alpha, 1)
h = 4*u**3*z
eq('conformal_potential_power', -8*alpha*(rho+s.Rational(1,2))**2*u**4,
   s.Rational(3,2)*u**-1*h*h)
eigenvalues = [-s.Rational(4,3)*t, s.Rational(2,3)*t-2*t*z,
               s.Rational(2,3)*t+2*t*z]
eq('trace_free', sum(eigenvalues), 0)
eq('relative_splitting', (eigenvalues[2]-eigenvalues[1])/(4*t), z)
eq('lowest_eigenvalue_gap', eigenvalues[1]-eigenvalues[0], 2*t*(1-z))
eq('residual_norm', (-2*t*z)**2+(2*t*z)**2,
   (eigenvalues[2]-eigenvalues[1])**2/2)
V = u*(u**3-u0**3)*(u-u0)
eq('restoring_potential_factorization', V,
   u*(u*u+u*u0+u0*u0)*(u-u0)**2)
eq('scalar_error_ratio', u*u*(u-u0)**2/V, u/(u*u+u*u0+u0*u0))
eq('scalar_error_ratio_upper_bound_numerator',
   (u*u+u*u0+u0*u0)-3*u*u0, (u-u0)**2)
eq('test_derivative', s.diff((u-u0)/u, u), u0/u**2)
W0 = s.diag(-s.Rational(2,3), s.Rational(1,3), s.Rational(1,3))
B = s.diag(0,b,-b)
W = W0+eps*B
reaction = -2*W-6*W*W+2*s.trace(W*W)*s.eye(3)
assert reaction.subs(eps, 0) == s.zeros(3)
checks['KE_reaction_zero'] = True
assert reaction.diff(eps).subs(eps,0) == -6*B
checks['splitting_reaction_negative_mass'] = True

mutations = {
    'wrong_positive_potential_sign':
        8*alpha*(rho+s.Rational(1,2))**2*u**4
        -s.Rational(3,2)*u**-1*h*h,
    'wrong_conformal_volume_power':
        -8*alpha*(rho+s.Rational(1,2))**2*u**2
        -s.Rational(3,2)*u**-1*h*h,
    'wrong_closedness_coefficient':
        exterior/gradient-z*z,
}
for name, expression in mutations.items():
    assert s.simplify(expression) != 0, name
print(json.dumps({'exact_checks': checks, 'count': len(checks),
                  'rejected_mutations': list(mutations),
                  'scope': 'finite symbolic identities, not a PDE proof'}, indent=2))
