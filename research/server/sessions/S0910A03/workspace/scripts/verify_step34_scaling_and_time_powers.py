#!/usr/bin/env python3
"""Exact algebra checks for Step 34.

This script checks only exponent/scaling identities. It deliberately does not
encode geometric or PDE premises as unconditional booleans.
"""
from fractions import Fraction as Q
import sympy as sp

r, V, K0, delta, t, theta = sp.symbols(
    "r V K0 delta t theta", positive=True
)

# Sobolev coefficient in ||u||_4^2 <= S_cal E(u).
S_cal = r**2 / sp.sqrt(V)
H2 = K0 * V
gamma = sp.simplify(S_cal * sp.sqrt(H2))
assert sp.simplify(gamma - r**2 * sp.sqrt(K0)) == 0

# Equivalent unsquared convention: ||u||_4 <= S E(u)^(1/2).
S_unsq = sp.sqrt(S_cal)
assert sp.simplify(S_unsq**2 - S_cal) == 0

# Curvature potential coefficient on a dyadic slab.
Y = gamma * H2 / t
potential = sp.simplify(S_cal**2 * Y)
assert sp.simplify(potential - gamma**3 / t) == 0

# General endpoint exponents for p_k=(3/2)^k p0.
def geometric_sum_inv(p0):
    # sum_k 1/p_k = (1/p0)/(1-2/3)=3/p0
    return Q(3, p0)

assert geometric_sum_inv(3) == 1
assert geometric_sum_inv(6) == Q(1, 2)

# Endpoint formula: S_cal^(2/p0) t^(-3/p0) (integral H_p0)^(1/p0).
# Defect seed integral <= delta^6 V t, p0=6.
defect_endpoint = sp.simplify(
    S_cal**Q(1, 3) * t**Q(-1, 2) * (delta**6 * V * t)**Q(1, 6)
)
expected_defect = delta * (r**2 / t)**Q(1, 3)
assert sp.simplify(defect_endpoint / expected_defect) == 1
assert not defect_endpoint.has(V)

# Integral of the predicted defect endpoint over [0,T].
s = sp.symbols("s", positive=True)
T = theta * r**2
drift = sp.integrate(delta * (r**2 / s)**Q(1, 3), (s, 0, T))
expected_drift = Q(3, 2) * delta * theta**Q(2, 3) * r**2
assert sp.simplify(drift - expected_drift) == 0

# Curvature p0=3 endpoint using only a slab H3 mass <= gamma H2.
curv_endpoint = sp.simplify(
    S_cal**Q(2, 3) * t**(-1) * (gamma * H2)**Q(1, 3)
)
assert sp.simplify(curv_endpoint / (gamma / t)) == 1

# Weight identities in mixed interpolation.
p = sp.symbols("p", positive=True)
assert sp.simplify((p - 2) / 2 + (p - 1) - (3*p/2 - 2)) == 0

print("PASS: Step 34 convention, volume cancellation, and time exponents")
print(f"Sobolev absorption gamma = {gamma}")
print(f"Defect endpoint scaling = {defect_endpoint}")
print(f"Integrated defect drift = {drift}")
print(f"Curvature endpoint from spacetime H3 seed = {curv_endpoint}")
print("No geometric compactness or PDE existence premise was asserted by this script.")
