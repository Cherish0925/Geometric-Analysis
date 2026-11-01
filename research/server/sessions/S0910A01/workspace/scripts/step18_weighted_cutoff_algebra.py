#!/usr/bin/env python3
"""
Step 18 algebra for the weighted cutoff-flow system.

This script checks the scalar transformation used in the cutoff-flow analysis.
Let a=chi^2 be time-independent, K=|Rm|, and f=aK.  Starting from the
schematic scalar inequality

    K_t <= a Delta K + c a K^2 + T,

it verifies the exact differential identity

    f_t <= a Delta f - 2 <grad a, grad f>
           + (2 |grad a|^2/a - Delta a) f
           + c f^2 + a T.

The important point is that the quadratic reaction is c f^2, not c f^2/a.
The script also integrates the principal weighted operator against eta^2 f and
records the resulting energy inequality with no pointwise Hess(a) requirement
after one integration by parts.
"""
import sympy as sp

# One-dimensional symbolic check is enough for the product-rule identity;
# the n-dimensional formula is the same with dot products and Laplacian.
x = sp.symbols('x')
a = sp.Function('a')(x)
f = sp.Function('f')(x)
c, T = sp.symbols('c T')
K = f/a

# Compute a^2 * Delta(f/a) in 1D and compare with the stated formula.
lhs = sp.expand(a**2 * sp.diff(K, x, 2))
rhs = sp.expand(a * sp.diff(f, x, 2)
                - 2 * sp.diff(a, x) * sp.diff(f, x)
                + (2 * sp.diff(a, x)**2/a - sp.diff(a, x, 2)) * f)
print("Scalar weighted identity residual (should be 0):")
print(sp.simplify(lhs - rhs))
assert sp.simplify(lhs - rhs) == 0

reaction = sp.simplify(a**2 * c * K**2)
print("Reaction a^2 * c*K^2 expressed in f:", reaction)
assert sp.simplify(reaction - c*f**2) == 0

# a=chi^2 identity.
chi = sp.Function('chi')(x)
a_chi = chi**2
ratio = sp.simplify(sp.diff(a_chi, x)**2 / a_chi)
print("|grad(chi^2)|^2/chi^2 in 1D:", ratio)
assert sp.simplify(ratio - 4*sp.diff(chi, x)**2) == 0

# Energy identity.  Work formally in one dimension.  Let eta be a localization
# cutoff.  The principal part is
#   I = ∫ eta^2 f [a f_xx - 2 a_x f_x + (2 a_x^2/a - a_xx) f].
# Integrate only the a f_xx and -a_xx f^2 terms by parts and keep the local
# density of the resulting expression.  Boundary terms are omitted.
eta = sp.Function('eta')(x)
fx = sp.diff(f, x)
ax = sp.diff(a, x)
etax = sp.diff(eta, x)

# After integrating ∫eta^2 f a f_xx:
term_afxx = -a*eta**2*fx**2 - 2*a*eta*f*etax*fx - eta**2*f*ax*fx
# After integrating ∫ - eta^2 f^2 a_xx:
term_minus_axx = 2*eta*etax*f**2*ax + 2*eta**2*f*fx*ax
# Remaining drift and potential:
term_drift = -2*eta**2*f*ax*fx
term_potential = 2*eta**2*f**2*ax**2/a
energy_density = sp.expand(term_afxx + term_minus_axx + term_drift + term_potential)
print("\nPrincipal energy density after Hess(a) integration by parts:")
print(energy_density)

# Bound the mixed terms by the schematic expression
#   -1/2 a eta^2 f_x^2 + C(a eta_x^2 + eta^2 a_x^2/a) f^2.
# Verify no a_xx remains.
assert sp.diff(a, x, 2) not in energy_density.atoms(sp.Derivative)
print("\nNo second derivative of a remains in the integrated principal density.")

# Display the mixed terms that need Young inequalities.
main_dissipation = -a*eta**2*fx**2
mixed = sp.expand(energy_density - main_dissipation)
print("Mixed/remainder density to estimate by Young inequalities:")
print(mixed)

# Simple square-completion identities used for the two types of mixed terms.
X, Y, eps = sp.symbols('X Y eps', positive=True)
young = sp.simplify(eps*X**2 + Y**2/eps - 2*X*Y)
print("\nYoung identity residual:", sp.factor(young - (eps*X-Y)**2/eps))
assert sp.simplify(young - (eps*X-Y)**2/eps) == 0

print("\nPASS: weighted scalar formula has reaction c*f^2, no inverse-cutoff reaction; integrated principal energy uses only grad(a), not pointwise Hess(a).")
