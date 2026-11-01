#!/usr/bin/env python3
"""
Step 29 superseded script: half-power observation and Step 30 correction.

The original version of this script proposed an ordinary unweighted Moser
iteration on U=a(Rm+G).  Step 30 withdrew that proposal: the operator remains
a*Delta and testing U controls only a-weighted gradients; the shifted quadratic
reaction is U*U, not a*U*U.  This script now preserves the useful algebraic
observation and points to the repaired weighted mixed Holder-Sobolev route.
"""
from fractions import Fraction

print("=" * 70)
print("STEP 29 WEIGHT-GAP OBSERVATION -- SUPERSEDED BY STEP 30")
print("=" * 70)

for p0 in [3, 4, 6, 9, 12]:
    p = Fraction(p0, 1)
    z3_exp = Fraction(3, 2) * (p - 1)
    Hnext_exp = Fraction(3, 2) * p - 2
    mixed_exp = (p - 2) / 2 + (p - 1)
    print(f"p={p0:2d}: ||z_p||_3^3 exponent={z3_exp}, H_(3p/2) exponent={Hnext_exp}, gap={z3_exp-Hnext_exp}")
    assert z3_exp - Hnext_exp == Fraction(1, 2)
    assert mixed_exp == Hnext_exp

print("\nDirect ||z_p||_3^3 comparison has the wrong direction because a<=1.")
print("But the actual weighted recurrence uses:")
print("  H_{3p/2} = integral (a^{p-2} f^p)^{1/2} z_p^2 <= H_p^{1/2} ||z_p||_4^2")
print("and Sobolev controls ||z_p||_4^2 by weighted dissipation plus r^{-2}H_p.")
print("\nThe ordinary unweighted U/aE Moser shortcut is NOT verified and is withdrawn.")
print("Use workspace/scripts/step30_weighted_moser_family_repair.py for the active check.")
print("PASS: superseded script no longer endorses the unweighted-U route.")
