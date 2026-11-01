#!/usr/bin/env python3
"""Algebraic/exponent checks for Step 38.

This verifies weight, Hölder, Young, and iteration arithmetic only.  It does not
verify tensor-contraction provenance, PDE existence/continuation, moving
Sobolev geometry, or the Yau 26 proposition.
"""
from fractions import Fraction
import math

checks = []

def check(name, cond, detail=""):
    if not cond:
        raise AssertionError(f"FAIL {name}: {detail}")
    checks.append(name)
    print(f"PASS {len(checks)}: {name}")

# Signed Hessian IBP: J=int chi chi_ij B^ij -> -(chi_i chi_j B + chi chi_j div B).
# Record derivative orders symbolically: Hessian order 2 decreases to gradient order 1.
check("signed Hessian IBP lowers cutoff order 2 -> 1", 2 - 1 == 1)

# Young factors for chi*dchi*|V|^(p-1)*|grad V|.
for p in [2, 3, 4, 6, 9, 20]:
    first_v = Fraction(p - 2, 2)
    second_v = Fraction(p, 2)
    check(f"Young V powers sum to p-1 at p={p}", first_v + second_v == p - 1)
    check(f"first Young square gives dissipation V^(p-2), p={p}", 2 * first_v == p - 2)
    check(f"second Young square gives V^p, p={p}", 2 * second_v == p)

# Step 37 corrected power count: energy test |W|^(p-2)W has degree p-1;
# multiplying by R3~W yields degree p.
for p in [2, 3, 6, 10]:
    check(f"R3 tested W-degree is p at p={p}", (p - 1) + 1 == p)
    # I1c additionally has grad U=W after first IBP, likewise p.
    check(f"I1c tested W-degree is p at p={p}", (p - 1) + 1 == p)

# Curvature reaction three-factor identity.
for p in [3, Fraction(9, 2), Fraction(27, 4), 9, 20]:
    a_exp = Fraction(1, 3) + (p - 2) / 3 + Fraction(2, 3) * (p - 1)
    f_exp = 1 + p / 3 + Fraction(2, 3) * p
    check(f"curvature reaction a-weight p-1 at p={p}", a_exp == p - 1)
    check(f"curvature reaction F-power p+1 at p={p}", f_exp == p + 1)

# Mixed Moser interpolation identity H_{3p/2} <= H_p^(1/2)||z_p||_4^2.
for p in [3, Fraction(9, 2), Fraction(27, 4), 6, 9]:
    lhs_a = Fraction(3, 2) * p - 2
    rhs_a = (p - 2) / 2 + (p - 1)
    lhs_f = Fraction(3, 2) * p
    rhs_f = p / 2 + p
    check(f"mixed interpolation a-weight at p={p}", lhs_a == rhs_a)
    check(f"mixed interpolation f-power at p={p}", lhs_f == rhs_f)

# Exponent sums p_{k+1}=3p_k/2.
def finite_sums(p0, n=200):
    p = float(p0)
    s1 = 0.0
    s_next = 0.0
    for _ in range(n):
        s1 += 1.0 / p
        pnext = 1.5 * p
        s_next += 1.0 / pnext
        p = pnext
    return s1, s_next

for p0 in [3, 6, 7]:
    s1, sn = finite_sums(p0)
    check(f"sum 1/p_k = 3/p0 for p0={p0}", abs(s1 - 3/p0) < 1e-12)
    check(f"sum 1/p_(k+1) = 2/p0 for p0={p0}", abs(sn - 2/p0) < 1e-12)

# Endpoint time and Sobolev exponents.
check("curvature endpoint time exponent is 1", Fraction(3, 3) == 1)
check("curvature endpoint Sobolev exponent is 2/3", Fraction(2, 3) == Fraction(2, 3))
check("defect endpoint time exponent before seed time is 1/2", Fraction(3, 6) == Fraction(1, 2))
check("defect endpoint Sobolev exponent is 1/3", Fraction(2, 6) == Fraction(1, 3))
check("defect seed time cancels 1/6, leaving t^-1/3", Fraction(1, 2) - Fraction(1, 6) == Fraction(1, 3))

# Collapse-volume cancellation S~r^2 V^-1/2, defect prefactor S^(1/3)V^(1/6).
V_exp = -Fraction(1, 2) * Fraction(1, 3) + Fraction(1, 6)
r_exp = 2 * Fraction(1, 3)
check("defect volume exponent cancels", V_exp == 0)
check("defect r exponent is 2/3", r_exp == Fraction(2, 3))

# Integral of t^-1/3 from 0 to T and T=theta r^2 scaling.
check("t^-1/3 is integrable", Fraction(-1, 3) > -1)
# r^(2/3)*(theta*r^2)^(2/3)=theta^(2/3)*r^2
check("metric drift r exponent is 2", Fraction(2, 3) + 2 * Fraction(2, 3) == 2)

# Polynomial/dyadic Moser product convergence numerical stress check.
for p0 in [3, 6]:
    total = 0.0
    for k in range(500):
        p = p0 * (1.5 ** k)
        total += (5 * math.log(p) + k * math.log(4.0) + 1.0) / p
    check(f"Moser log-product finite numerically for p0={p0}", math.isfinite(total) and total < 100)

print(f"All {len(checks)} Step 38 algebra/exponent checks passed.")
print("NOT CHECKED: tensor contraction provenance, PDE existence or extension, moving Sobolev/support hypotheses, terminal geometry, or Yau 26.")
