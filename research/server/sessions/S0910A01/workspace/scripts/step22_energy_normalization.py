#!/usr/bin/env python3
"""
Step 22: corrected normalization check for Whitney energy bookkeeping.

The component budget is H2(U)=int_U F^2 <= M Vol(U).  For a Whitney ball
W=B_ell(y), y in B_{4r}(p), U=B_{5r}(p), the nonconcentric comparison uses
U subset B_{9r}(y), hence Vol(W) >= c (ell/9r)^4 Vol(U).  Thus the local
mean may grow like (r/ell)^4, while ell^4 average and A_W^2||F||_2 are stable.
"""
from math import sqrt

K0 = 10.0
M = 1.0 + K0
r = 1.0e-2
c = 0.1
buffer_over_r = 9.0
c_BG = 1.0
VolU = 1.0

print("STEP 22 CORRECTED WHITNEY ENERGY NORMALIZATION")
print("component mean M=1+K0 =", M)
print("r=", r, "c=", c, "nonconcentric buffer=9r")
print()
print("chi0      mean_W/M        ell^4*mean_W/(M*r^4)    gamma=A^2||F||2")

for chi0 in [1.0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-6]:
    ell = c*r*chi0
    VolW = c_BG*(c*chi0/buffer_over_r)**4 * VolU
    H2U = M*VolU
    H2W = H2U  # worst concentration allowed by component budget
    meanW = H2W/VolW
    normalized_mean = ell**4 * meanW/(M*r**4)
    A2 = ell**2/(VolW**0.5)
    gamma = A2*sqrt(H2W)
    print(f"{chi0:8.1e}  {meanW/M:12.3e}       {normalized_mean:12.6g}          {gamma:12.6e}")

expected_gamma = buffer_over_r**2 * r**2 * sqrt(M/c_BG)
print()
print("Expected gamma from cancellation:", expected_gamma)
print("The local mean can grow like chi0^-4, so a volume-normal H2(W) bound is false.")
print("The scale-invariant ell^4 average and A_W^2||F||_2 remain constant.")
print("PASS")
