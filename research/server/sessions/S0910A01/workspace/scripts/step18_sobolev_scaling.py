#!/usr/bin/env python3
"""
Step 18 scaling check for collapse-compatible Sobolev absorption.

For a ball/support U of radius r and volume V in dimension n, the relative
Sobolev coefficient in the critical W^{1,2}->L^{2n/(n-2)} inequality scales as

    A_U ~ r^2 / V^{2/n}.

The reaction relevant to curvature smoothing uses the critical curvature norm
||Rm||_{L^{n/2}(U)}.  If average_U |Rm|^{n/2} <= K0, then

    ||Rm||_{L^{n/2}} = (K0 V)^{2/n}

and therefore

    A_U ||Rm||_{L^{n/2}} ~ K0^{2/n} r^2,

so collapsed volume cancels in every dimension for the critical norm.  In the
LeBrun route n=4, this is exactly the L^2 curvature energy supplied by
Chern-Weil/Noether.  In higher dimensions it would require an L^{n/2} input not
available from the present four-dimensional topology.
"""
import math

K0 = 15100.0
r = 0.003
volumes = [10.0**(-k) for k in range(0, 25, 4)]

print("Collapse-compatible critical Sobolev product")
print(f"K0={K0}, r={r}")
print()
for n in [3, 4, 5, 6, 8, 10]:
    predicted = (K0 ** (2.0/n)) * r**2
    print(f"n={n}: predicted product K0^(2/n) r^2 = {predicted:.6e}")
    vals = []
    for V in volumes:
        A_U = r**2 / (V ** (2.0/n))
        Rm_crit = (K0 * V) ** (2.0/n)
        vals.append(A_U * Rm_crit)
    spread = max(vals) / min(vals)
    print(f"  products over V={volumes[0]:.0e}..{volumes[-1]:.0e}: min={min(vals):.6e}, max={max(vals):.6e}, spread={spread:.6f}")
    assert abs(spread - 1.0) < 1e-10

print("\nFor n=4 this product is K0^(1/2) r^2, using the available L^2 curvature energy.")
print("For n>4 the same cancellation would need L^{n/2} curvature control, not just L^2.")
print("PASS")
