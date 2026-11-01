#!/usr/bin/env python3
"""Weight audit for a Whitney-cylinder Bernstein estimate.

At x with chi(x)=lambda, set a0=lambda^2 and ell=c*r*lambda.  Rescale
space by ell and time by a0.  The script records powers of lambda in the
expected curvature/defect derivative estimates and the dangerous term
chi*a*nabla(Rm)*U in the differentiated U equation.

This is an exponent audit, not a PDE proof.
"""
import sympy as sp

lam, c, r, t, delta = sp.symbols('lam c r t delta', positive=True)
a0 = lam**2
ell = c*r*lam
tau = a0*t

# Natural nondegenerate parabolic estimates in original variables:
# |Rm| <= C/tau, |nabla Rm| <= C/tau^(3/2), because spatial metric is not rescaled,
# but interior scale imposes ell.  Equivalently positive-time Shi gives these dimensions.
Rm = tau**-1
gradRm = tau**sp.Rational(-3,2)

# Desired U=aE and W=chi grad U estimates from p=6.
U = delta*(r**2/t)**sp.Rational(1,3)
W = delta*t**sp.Rational(-1,2)*(r**2/t)**sp.Rational(1,3)

# Dangerous source S=chi*a*nabla Rm*U.
S = sp.simplify(lam*a0*gradRm*U)
ratio_to_W_over_t = sp.simplify(S/(W/t))

# If instead one has the weighted curvature derivative a^(3/2)|nabla Rm|<=C t^-3/2,
# it is exactly lambda-independent.
weighted_gradRm = sp.simplify(a0**sp.Rational(3,2)*gradRm)

# Desired W is chi grad U.  A standard gradient estimate on diffusion coefficient a0 is
# |grad U| <= (a0*t)^-1/2 sup|U|, hence chi|grad U| <= t^-1/2 sup|U|.
standard_W = sp.simplify(lam*tau**sp.Rational(-1,2)*U)
assert sp.simplify(standard_W-W) == 0
assert sp.simplify(weighted_gradRm - t**sp.Rational(-3,2)) == 0
assert sp.simplify(ratio_to_W_over_t - 1) == 0

# Spatial cutoff terms after rescaling: a0/ell^2 = 1/(c^2 r^2).
cutoff_scale = sp.simplify(a0/ell**2)
assert cutoff_scale == 1/(c**2*r**2)

# Effective time / spatial radius squared.
time_radius_ratio = sp.simplify(tau/ell**2)
assert time_radius_ratio == t/(c**2*r**2)

print('PASS: chi*(a0 t)^(-1/2) U equals desired W, no lambda loss')
print('PASS: a0^(3/2)|nabla Rm| from Shi scaling equals t^(-3/2)')
print('PASS: chi*a0*nablaRm*U has exactly W/t scaling, no lambda loss')
print('PASS: a0/ell^2 =', cutoff_scale, 'and tau/ell^2 =', time_radius_ratio)
print('Interpretation: the dangerous derivative source is scale-critical, not cutoff-singular.')
print('A rigorous Bernstein estimate still needs coupled cancellation or time-cylinder regularity;')
print('a bare Gronwall coefficient 1/t is nonintegrable from zero.')
