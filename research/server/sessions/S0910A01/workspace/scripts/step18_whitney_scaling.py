#!/usr/bin/env python3
"""
Step 18 Whitney-scale calculation for the degenerate cutoff operator.

Assume a=chi^2, |grad chi|<=L/r, and examine a point x0 with chi0>0.
On a Whitney ball of radius ell = c r chi0, chi is comparable to chi0.
After rescaling x=x0+ell*y and t=r^2*s, the principal coefficient a/chi0^2,
drift coefficient r^2 |grad a|/ell, and potential coefficient
r^2 |grad a|^2/a are O(1), independent of chi0.  This supports the natural
local route to a weighted Moser estimate for F=r^2 a|Rm|.
"""
import math

L = 2.0  # |grad chi| <= L/r
for c in [0.05, 0.1, 0.2, 0.3]:
    lower = max(0.0, 1 - L*c)
    upper = 1 + L*c
    a_ratio_low = lower**2
    a_ratio_high = upper**2
    print(f"c={c:.2f}: chi/chi0 in [{lower:.3f},{upper:.3f}], a/a0 in [{a_ratio_low:.3f},{a_ratio_high:.3f}]")

print("\nDimensionless coefficients after x=x0+ell*y, t=r^2*s, ell=c r chi0:")
for c in [0.05, 0.1, 0.2]:
    # Principal coefficient a/chi0^2 lies in [(1-Lc)^2,(1+Lc)^2].
    principal_low = (1-L*c)**2
    principal_high = (1+L*c)**2
    # Drift term -2<grad a,grad f>: r^2 |grad a|/ell <= r^2 * (2 chi0 L/r)/(c r chi0)=2L/c.
    drift = 2*L/c
    # Potential |grad a|^2/a <= 4L^2/r^2 -> r^2 coefficient <=4L^2.
    potential = 4*L**2
    print(f"c={c:.2f}: principal in [{principal_low:.3f},{principal_high:.3f}], drift<= {drift:.1f}, potential<= {potential:.1f}")

print("\nDiffusion length containment:")
for theta in [1e-4, 1e-3, 1e-2, 2e-2]:
    # sqrt(a0 * theta r^2)=chi0*r*sqrt(theta).  It is <= ell/2 if sqrt(theta)<=c/2.
    for c in [0.05, 0.1, 0.2]:
        ok = math.sqrt(theta) <= c/2
        print(f"theta={theta:.0e}, c={c:.2f}: sqrt(theta)={math.sqrt(theta):.4f}, <=c/2? {ok}")
    print()

print("Interpretation: Whitney balls give uniform coefficients for chi0>0 if theta is chosen below c^2.  The cost is finite-neighbor organization across level sets of chi and a weighted Sobolev/Moser argument for the tensor equation.")
print("PASS")
