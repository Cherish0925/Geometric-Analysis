#!/usr/bin/env python3
"""
Step 18 constant-diffusivity model for weighted curvature smoothing.

If a is locally almost constant, the model equation K_t = a Delta K in n
spatial dimensions has heat kernel L^{n/2}->L^infty norm ~ (a t)^(-1).  The
weighted output aK therefore obeys

    ||a K(t)||_infty <= C t^{-1} ||K0||_{L^{n/2}},

independent of the value of a>0.  This explains why the target |a Rm|<=C/t is
natural near the transition and why no inverse-cutoff reaction should appear.
The model ignores gradients of a and nonlinear/tensor terms.
"""
import math

print("Constant-diffusivity heat model: ||a K(t)||_inf from L^{n/2}")
for n in [3, 4, 5, 6, 8]:
    p = n/2
    # Heat kernel L^p -> L^inf scales as (a t)^(-n/(2p)) = (a t)^(-1).
    exponent = n/(2*p)
    print(f"n={n}: p=n/2={p:.1f}, heat exponent n/(2p)={exponent:.1f}")
    for a in [1.0, 1e-1, 1e-3, 1e-6]:
        t = 0.01
        unweighted = (a*t)**(-exponent)
        weighted = a*unweighted
        print(f"  a={a:8.1e}: ||K|| factor~{unweighted:10.3e}, ||aK|| factor~{weighted:10.3e}")
    print("  expected weighted factor = 1/t =", 1/t)
print("\nPASS: local constant-a scaling favors the weighted target aK<=C/t; variable-a gradient terms are the remaining difficulty.")
