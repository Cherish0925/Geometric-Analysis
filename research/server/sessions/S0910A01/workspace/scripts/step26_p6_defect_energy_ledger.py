#!/usr/bin/env python3
"""
Step 26: p=6 weighted defect energy term ledger.

The goal is to avoid a hidden smoothness issue in a^(p-2) at chi=0 by using an
integer exponent p=6.  The script verifies the weights produced by the p-energy
calculation for

    J6 = int eta^2 a^4 |E|^6,
    Z6 = int eta^2 a^5 |E|^4 |nabla E|^2,
    z6 = eta a^(5/2) |E|^3.

It is an exponent ledger, not a proof of the geometric PDE inequality.
"""
import sympy as sp

# exponents are tracked as (a_power, E_power, gradE_power, F_power, da_power)

def young_remainder(term, diss):
    """Return the power left when term is absorbed against diss by Young.

    term has one gradE and one da; diss has gradE^2.  If
    term = a^A E^B da gradE and diss = a^D E^G gradE^2, then the remainder is
    a^(2A-D) E^(2B-G) da^2.
    """
    A, B, _, _, da = term
    D, G, _, _, _ = diss
    assert term[2] == 1 and da == 1
    return (2*A-D, 2*B-G, 0, 0, 2)

p = 6
J6 = (4, 6, 0, 0, 0)        # a^4 |E|^6
Z6 = (5, 4, 2, 0, 0)        # a^5 |E|^4 |gradE|^2
potential = (5, 6, 0, 1, 0) # a^5 F |E|^6 = F z6^2
z6sq = (5, 6, 0, 0, 0)
assert potential[:3] == z6sq[:3] and potential[3] == 1

# Principal cutoff from - int grad(eta^2 a^(p-1)) grad(|E|^p)
principal_cutoff = (4, 5, 1, 0, 1)  # a^4 |E|^5 da gradE
rem = young_remainder(principal_cutoff, Z6)
# rem = a^3 |E|^6 da^2 = 4 a^4 |dchi|^2 |E|^6 = r^-2 J6
assert rem == (3, 6, 0, 0, 2)

# Direct (da)*nablaE term from C_a(E), weighted by a^(p-2)|E|^(p-1)
direct_da = (4, 5, 1, 0, 1)
assert young_remainder(direct_da, Z6) == rem

# Hessian-a after IBP: derivative hits |E|^6 or a^4.
hess_hit_E = (4, 5, 1, 0, 1)
hess_hit_weight = (3, 6, 0, 0, 2)
assert young_remainder(hess_hit_E, Z6) == rem
assert hess_hit_weight == rem

# Substitute da^2 = 4 a |dchi|^2.
# a^3 E^6 da^2 -> a^4 E^6 |dchi|^2 = J6 * |dchi|^2.
rem_after_square_cutoff = (rem[0] + 1, rem[1], rem[2], rem[3], 0)
assert rem_after_square_cutoff == J6

# Weighted velocity relation: |aE|^6 = a^6 E^6 = a^2 J6 density <= J6 density.
velocity6 = (6, 6, 0, 0, 0)
assert velocity6[0] - J6[0] == 2 and velocity6[1] == J6[1]

print("STEP 26 p=6 DEFECT ENERGY LEDGER")
print("J6 density              : a^4 |E|^6")
print("Z6 dissipation          : a^5 |E|^4 |nabla E|^2")
print("potential               : a^5 F |E|^6 = F*(a^(5/2)|E|^3)^2")
print("principal/direct da rem : a^3 |E|^6 |da|^2 = 4|dchi|^2 J6")
print("weighted velocity       : |aE|^6 = a^2 * J6_density <= J6_density")
print("regularization          : a^4=chi^8 is smooth; z6=chi^5|E|^3 is handled in W^{1,2} via (|E|^2+eps)^(3/2)")
print("PASS: p=6 weighted defect energy has the transition powers needed for support-wide velocity.")
