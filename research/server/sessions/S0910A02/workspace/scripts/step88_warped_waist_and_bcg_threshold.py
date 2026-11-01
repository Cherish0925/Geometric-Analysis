"""
Step 88: Warped-product waist obstruction and BCG pinching threshold.

Part 1: For g = dr^2 + f(r)^2 g_F on I x F^3, with Ric_F = 2k g_F,
Ricci endomorphism eigenvalues at a waist (f'=0, f''>=0):
  lambda_r = -3 f''/f = -3 alpha
  lambda_F = 2k/f^2 - f''/f = beta - alpha

For Ric approx -3g, defects:
  delta_r = |lambda_r + 3| = 3|1 - alpha|
  delta_F = |lambda_F + 3| = |beta - alpha + 3|

Minimize max(delta_r, delta_F) over alpha >= 0, beta >= 0 (k >= 0).

Part 2: BCG/CGB pinching threshold for N#N.
"""

import json
import numpy as np

results = {}

# ============================================================
# Part 1: Warped-product waist obstruction
# ============================================================

def waist_defect(alpha, beta):
    """Max Ricci defect from -3 at a waist with alpha=f''/f, beta=2k/f^2."""
    dr = 3 * abs(1 - alpha)
    dF = abs(beta - alpha + 3)
    return max(dr, dF)

# For k=0 (flat T^3 fiber): beta = 0
# Optimal: equalize 3|1-alpha| = |3-alpha| for alpha in [0, inf)
# Case alpha <= 1: 3(1-alpha) = 3-alpha -> alpha=0, delta=3
# Case 1 <= alpha <= 3: 3(alpha-1) = 3-alpha -> 4alpha=6 -> alpha=3/2, delta=3/2
# Case alpha >= 3: 3(alpha-1) = alpha-3 -> 2alpha=0, impossible
alpha_opt_k0 = 1.5
beta_opt_k0 = 0.0
delta_k0 = waist_defect(alpha_opt_k0, beta_opt_k0)

# Numerical verification: scan alpha in [0, 5] with beta=0
alpha_grid = np.linspace(0, 5, 10001)
defects_k0 = [waist_defect(a, 0) for a in alpha_grid]
delta_k0_num = min(defects_k0)
alpha_k0_num = alpha_grid[np.argmin(defects_k0)]

results["k0_flat_fiber"] = {
    "alpha_optimal": alpha_opt_k0,
    "beta_optimal": beta_opt_k0,
    "delta_exact": 1.5,
    "delta_numeric": round(delta_k0_num, 10),
    "alpha_numeric": round(alpha_k0_num, 6),
    "match": abs(delta_k0 - 1.5) < 1e-12 and abs(delta_k0_num - 1.5) < 1e-4,
}

# For k=1 (round S^3 fiber): beta = 2/f_0^2 > 0
# Equalize 3(alpha-1) = beta - alpha + 3 -> alpha = (beta+6)/4
# delta = 3((beta+6)/4 - 1) = 3(beta+2)/4
# As f_0 -> inf: beta -> 0, delta -> 3/2 from above
f0_values = [1, 2, 5, 10, 50, 100, 1e6]
k1_data = []
for f0 in f0_values:
    beta = 2.0 / f0**2
    alpha = (beta + 6) / 4
    delta = 3 * (beta + 2) / 4
    # Numeric check
    defects_k1 = [waist_defect(a, beta) for a in alpha_grid]
    delta_num = min(defects_k1)
    k1_data.append({
        "f0": f0, "beta": round(beta, 12),
        "alpha_opt": round(alpha, 10), "delta_exact": round(delta, 10),
        "delta_numeric": round(delta_num, 10),
        "delta_exceeds_1.5": delta > 1.5,
    })
results["k1_round_fiber"] = {
    "formula": "delta = 3(2/f0^2 + 2)/4 = 3/2 + 3/(2 f0^2)",
    "limit_f0_to_inf": 1.5,
    "samples": k1_data,
}

# For k=-1 (hyperbolic H^3 fiber): beta = -2/f_0^2 < 0
# Check H^4 equidistant from H^3: f(r) = cosh(r), at r=0: alpha=1, beta=-2
# lambda_r = -3, lambda_F = -2-1 = -3. Defect = 0.
alpha_H4 = 1.0
beta_H4 = -2.0
delta_H4 = waist_defect(alpha_H4, beta_H4)
results["km1_hyperbolic_fiber"] = {
    "H4_equidistant": {
        "f_0": 1, "alpha": alpha_H4, "beta": beta_H4,
        "delta": delta_H4,
        "note": "H4 equidistant from H3, zero defect",
    },
    "conclusion": "Negatively curved fiber permits defect-free waist; "
                   "this is the H4 metric itself, hence Einstein.",
}

# Summary
results["waist_summary"] = {
    "theorem": (
        "For a warped product g = dr^2 + f(r)^2 g_F on R x F^3 with "
        "Ric_F = 2k g_F: at any waist (f'=0, f''>=0), the Ricci "
        "endomorphism defect from -3 satisfies delta >= 3/2 when k >= 0 "
        "(flat or positively curved fiber). Equality holds when k=0 and "
        "f''/f = 3/2. For k < 0, zero defect is achieved by the "
        "hyperbolic metric. Connected sums N#N have S^3 waists (k=1), "
        "giving delta > 3/2 at every warped-product turnaround."
    ),
    "delta_flat_T3": 1.5,
    "delta_round_S3_any_radius": "> 1.5",
    "delta_hyperbolic_H3_optimal": 0.0,
    "implication": (
        "The warped-product class cannot produce near-negative-pinched "
        "metrics on connected sums or graph manifolds with positively "
        "curved or flat cross-sections. This is a pointwise obstruction, "
        "not an energy obstruction, and cannot be amortized over volume."
    ),
}

# ============================================================
# Part 2: BCG/CGB pinching threshold for N#N
# ============================================================

# CGB integrand lower bound under two-sided negative Ricci pinching
# Ric eigenvalues r_i = -3 x_i, x_i in [1-eps, 1+eps]
# s^2/6 - |Ric|^2/2 = (3/2)[(sum x_i)^2 - 3 sum x_i^2]
# NOTE: A01's intermediate formula (3/2)[(sum x)^2/3 - sum x^2] is WRONG
# by a factor of 3 in the first term. Correct is (3/2)[(sum x)^2 - 3 sum x^2].
# However, the final answer 6(1-eps)^2 is correct because all same-sign
# vertex gives sum x = 4(1-eps), sum x^2 = 4(1-eps)^2,
# so (3/2)[16(1-eps)^2 - 12(1-eps)^2] = (3/2)*4*(1-eps)^2 = 6(1-eps)^2.

def cgb_integrand_lower(eps):
    """CGB integrand s^2/6 - |Ric|^2/2 minimum for Ric eigs in [-3(1+eps), -3(1-eps)]."""
    # Minimum at all x_i = 1-eps (for eps < 1/2)
    S = 4 * (1 - eps)
    Q = 4 * (1 - eps)**2
    return 1.5 * (S**2 - 3 * Q)

# Verify at eps=0: should give 6
assert abs(cgb_integrand_lower(0) - 6.0) < 1e-12

# Cross-check the intermediate formula error
def a01_intermediate(eps):
    """A01's intermediate: (3/2)[(sum x)^2/3 - sum x^2] at all x=1-eps."""
    S = 4 * (1 - eps)
    Q = 4 * (1 - eps)**2
    return 1.5 * (S**2 / 3 - Q)

# At eps=0: A01 gives (3/2)[16/3 - 4] = (3/2)(4/3) = 2, not 6
a01_check = a01_intermediate(0)
correct_check = cgb_integrand_lower(0)

results["cgb_formula_check"] = {
    "correct_formula": "(3/2)[(sum x_i)^2 - 3 sum x_i^2]",
    "a01_intermediate": "(3/2)[(sum x_i)^2/3 - sum x_i^2]",
    "at_eps_0_correct": correct_check,
    "at_eps_0_a01": a01_check,
    "a01_intermediate_has_factor_3_error": True,
    "a01_final_answer_6_1_minus_eps_sq_is_correct": True,
    "note": "A01 got the right final answer despite wrong intermediate."
}

# Pinching threshold: incompatibility when
# (1-eps)^2/(1+eps)^2 > 1 - 1/chi(N)
# eps < eps_chi = (1 - sqrt(1-1/chi))/(1 + sqrt(1-1/chi))
chi_values = [2, 3, 5, 10, 20, 50, 100, 500, 1000]
threshold_data = []
for chi in chi_values:
    sq = np.sqrt(1 - 1.0/chi)
    eps_chi = (1 - sq) / (1 + sq)
    delta_chi = 3 * eps_chi  # operator norm threshold
    # Leading order: eps ~ 1/(4*chi), delta ~ 3/(4*chi)
    eps_leading = 1.0 / (4 * chi)
    delta_leading = 3.0 / (4 * chi)
    threshold_data.append({
        "chi_N": chi, "eps_chi": round(eps_chi, 10),
        "delta_chi": round(delta_chi, 10),
        "eps_leading": round(eps_leading, 10),
        "delta_leading": round(delta_leading, 10),
        "ratio_to_leading": round(eps_chi / eps_leading, 6) if eps_leading > 0 else None,
    })

results["bcg_cgb_threshold"] = {
    "formula": "eps_chi = (1 - sqrt(1-1/chi))/(1 + sqrt(1-1/chi))",
    "operator_norm": "delta = 3*eps, threshold delta < 3/(4*chi) + O(chi^{-2})",
    "additive_certificate": True,
    "note": (
        "The volume deficit arises from chi(N#N) = 2*chi(N)-2, "
        "a fixed additive constant 8*pi^2/3. No additive certificate "
        "can produce a uniform delta_0 independent of N. Hence this "
        "obstruction prices the refutation at O(1/chi) but cannot "
        "close the negative branch."
    ),
    "data": threshold_data,
}

# At critical rate, Weyl energy constraint
# Vol ~ 2*Vol(N), CGB: 8*pi^2*(2*chi-2) = int(|W|^2 + 6)*Vol + O(delta)
# So int |W|^2 = 8*pi^2*(2*chi-2) - 6*Vol + O(delta*Vol)
# = 8*pi^2*(2*chi-2) - 6*2*(4*pi^2/3)*chi + O(delta*Vol)
# = 16*pi^2*chi - 16*pi^2 - 16*pi^2*chi + O(delta*Vol)
# = -16*pi^2 + O(delta*Vol) = O(1)
results["weyl_budget_at_critical_rate"] = {
    "note": (
        "At the critical pinching rate delta ~ 1/chi, with Vol ~ 2*Vol(N), "
        "the Weyl curvature integral is int|W|^2 = O(1), an extremely "
        "tight scale-invariant budget for any candidate metric."
    ),
}

# ============================================================
# Part 3: Gauss equation for minimal separating hypersurface
# ============================================================
# For minimal Sigma^3 in (M^4, g) with Ric ~ -3g:
# Scal_Sigma = Scal_M - 2*Ric(nu,nu) - |A|^2  (minimal: H=0)
# = (-12 + O(delta)) - 2*(-3 + O(delta)) - |A|^2
# = -6 - |A|^2 + O(delta)
# This is not a contradiction since any closed 3-manifold admits
# metrics with very negative scalar curvature.
results["gauss_equation_minimal"] = {
    "formula": "Scal_Sigma = -6 - |A|^2 + O(delta)",
    "note": "No contradiction from Gauss alone; non-warped waists remain open."
}

# Save
outpath = "Sessions/S0910A02/workspace/data/step88_warped_waist_and_bcg_threshold.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2, default=str)

print(f"Saved to {outpath}")
print(f"\nWarped waist k=0 delta = {delta_k0}")
print(f"CGB correct at eps=0: {correct_check}, A01 intermediate: {a01_check}")
print(f"Threshold at chi=100: eps={threshold_data[7]['eps_chi']}, delta={threshold_data[7]['delta_chi']}")
print(f"H4 equidistant defect: {delta_H4}")
