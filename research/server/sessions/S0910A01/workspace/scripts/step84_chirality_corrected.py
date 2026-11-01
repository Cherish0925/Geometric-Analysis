#!/usr/bin/env python3
"""
Step 84 (corrected): Chirality angular maps with SEPARATE p_j and q_j
as required by Ozuch's formulas and TTCS verification.

For + chirality: p_j(x) = x^T C[2,j] x / |x|^2  (C[zeta_idx, j])
For - chirality: q_j(x) = x^T C[j,2] x / |x|^2  (C[j, zeta_idx])

The Gram matrices and 8/3 result are confirmed to survive this repair.
This script independently verifies them with correct angular maps.

Session S0910A01. Agent2 / Constructor.
"""
import numpy as np
import json

# 2-form bases
def e_wedge(i, j, n=4):
    A = np.zeros((n, n))
    A[i, j] = 1.0; A[j, i] = -1.0
    return A

e12=e_wedge(0,1); e13=e_wedge(0,2); e14=e_wedge(0,3)
e23=e_wedge(1,2); e24=e_wedge(1,3); e34=e_wedge(2,3)
wp = [e12+e34, e13-e24, e14+e23]
wm = [e12-e34, e13+e24, e14-e23]

C = np.zeros((3, 3, 4, 4))
for j in range(3):
    for k in range(3):
        C[j,k] = wp[j] @ wm[k]

results = {}
zeta_idx = 1  # omega_2

# ============================================================
# 1. Separate angular maps p and q
# ============================================================
def p_vec(x, zeta_idx=1):
    """Angular map for + chirality: p_j = x^T C[zeta_idx, j] x / |x|^2"""
    r2 = np.dot(x, x)
    return np.array([x @ C[zeta_idx, j] @ x / r2 for j in range(3)])

def q_vec(x, zeta_idx=1):
    """Angular map for - chirality: q_j = x^T C[j, zeta_idx] x / |x|^2"""
    r2 = np.dot(x, x)
    return np.array([x @ C[j, zeta_idx] @ x / r2 for j in range(3)])

# Sample S^3
np.random.seed(84)
N = 100000
raw = np.random.randn(N, 4)
pts = raw / np.linalg.norm(raw, axis=1, keepdims=True)

ps = np.array([p_vec(x) for x in pts])
qs = np.array([q_vec(x) for x in pts])

# ============================================================
# 2. Verify p != q but |p| = |q| and p_2 = q_2
# ============================================================
p_norm_sq = np.sum(ps**2, axis=1)
q_norm_sq = np.sum(qs**2, axis=1)
results["norm_p_sq_mean"] = float(np.mean(p_norm_sq))  # should be 1
results["norm_q_sq_mean"] = float(np.mean(q_norm_sq))  # should be 1
results["norm_p_minus_q_max"] = float(np.max(np.abs(p_norm_sq - q_norm_sq)))

# Check p_2 = q_2
results["p2_minus_q2_max"] = float(np.max(np.abs(ps[:, 1] - qs[:, 1])))

# Check p != q
pq_diff = np.max(np.abs(ps - qs), axis=1)
results["p_minus_q_max_over_S3"] = float(np.max(pq_diff))
results["p_minus_q_mean_over_S3"] = float(np.mean(pq_diff))

# Explicit check at (1,1,1,1)/2
x0 = np.array([0.5, 0.5, 0.5, 0.5])
p0 = p_vec(x0)
q0 = q_vec(x0)
results["at_1111"] = {"p": p0.tolist(), "q": q0.tolist(), "diff": (p0-q0).tolist()}

# ============================================================
# 3. Verify Gram matrices with correct angular maps
# ============================================================
# Same chirality: source is H4_+ ~ sum_j p_j C[1,j], receiver is O_1 ~ sum_k p_k C[1,k]
# Cross chirality: source is H4_- ~ sum_j q_j C[j,1], receiver is O_1 ~ sum_k p_k C[1,k]

# The analytical Gram matrices (independent of p, q):
Gram_same_analytic = np.zeros((3, 3))
Gram_cross_analytic = np.zeros((3, 3))
for j in range(3):
    for k in range(3):
        Gram_same_analytic[j, k] = np.trace(C[1,j] @ C[1,k])
        Gram_cross_analytic[j, k] = np.trace(C[j,1] @ C[1,k])

results["Gram_same"] = Gram_same_analytic.tolist()
results["Gram_cross"] = Gram_cross_analytic.tolist()
results["Gram_diff"] = (Gram_same_analytic - Gram_cross_analytic).tolist()

# The chirality difference in the pointwise obstruction overlap:
# Same: sum_{jk} p_j p_k Gram_same[j,k] = 4(p1^2+p2^2+p3^2) = 4|p|^2 = 4
# Cross: sum_{jk} q_j p_k Gram_cross[j,k] = 4*q_2*p_2 = 4*p_2^2 (since q_2=p_2)
# Difference: 4 - 4*p_2^2 = 4*(1-p_2^2) = 4*(p_1^2+p_3^2)

same_overlap = np.array([4*np.sum(ps[i]**2) for i in range(N)])
cross_overlap = np.array([4*qs[i,1]*ps[i,1] for i in range(N)])
chirality_diff = same_overlap - cross_overlap

results["same_overlap_mean"] = float(np.mean(same_overlap))  # should be 4
results["cross_overlap_mean"] = float(np.mean(cross_overlap))  # should be 4/3
results["chirality_diff_mean"] = float(np.mean(chirality_diff))  # should be 8/3
results["chirality_diff_std"] = float(np.std(chirality_diff))
results["chirality_diff_min"] = float(np.min(chirality_diff))  # min is 0
results["chirality_diff_max"] = float(np.max(chirality_diff))  # max is 4

# Analytic values
results["analytic_same_overlap"] = 4.0
results["analytic_cross_overlap"] = "4/3 (from <p_2^2> = 1/3)"
results["analytic_chirality_diff"] = "8/3"
results["analytic_chirality_diff_numerical"] = 8/3

# ============================================================
# 4. Verify with correct H^4 tensors
# ============================================================
def H4_plus(x):
    """H^4(zeta^+) = -sum_j p_j(x) C[1,j] / 2"""
    p = p_vec(x)
    return -0.5 * sum(p[j] * C[1,j] for j in range(3))

def H4_minus(x):
    """H^4(zeta^-) = -sum_j q_j(x) C[j,1] / 2"""
    q = q_vec(x)
    return -0.5 * sum(q[j] * C[j,1] for j in range(3))

def O1_plus(x):
    """O_1(zeta^+) = sum_j p_j(x) C[1,j] (proportional to -2H4_+)"""
    p = p_vec(x)
    return sum(p[j] * C[1,j] for j in range(3))

# Verify the corrected Delta = H4_+ - H4_- at sample points
h4_diffs = []
for i in range(min(N, 20000)):
    h4p = H4_plus(pts[i])
    h4m = H4_minus(pts[i])
    h4_diffs.append(np.sqrt(np.sum((h4p - h4m)**2)))

results["corrected_Delta_Frobenius_max"] = float(np.max(h4_diffs))
results["corrected_Delta_Frobenius_mean"] = float(np.mean(h4_diffs))
results["corrected_Delta_Frobenius_min"] = float(np.min(h4_diffs))

# Cross-check: <H4_+, O1> and <H4_-, O1> at a specific point
x_test = np.array([0.5, 0.5, 0.5, 0.5])
h4p_test = H4_plus(x_test)
h4m_test = H4_minus(x_test)
o1_test = O1_plus(x_test)
overlap_same = np.sum(h4p_test * o1_test)  # Frobenius inner product
overlap_cross = np.sum(h4m_test * o1_test)
results["crosscheck_at_1111"] = {
    "H4_plus_O1_overlap": float(overlap_same),
    "H4_minus_O1_overlap": float(overlap_cross),
    "difference": float(overlap_same - overlap_cross),
    "predicted_from_Gram": float(4*(1 - p_vec(x_test)[1]**2)),
}

# ============================================================
# 5. Summary with TTCS corrections incorporated
# ============================================================
results["summary"] = {
    "key_identity": "tr(C_{ab}C_{cd}) = 4*delta_{ac}*delta_{bd}",
    "Gram_same_chirality": "4*I_3 (all rho components couple equally)",
    "Gram_cross_chirality": "diag(0,4,0) (only axial rho_2 survives)",
    "Gram_difference": "diag(4,0,4) (rho_1 and rho_3 distinguish chirality)",
    "pointwise_chirality_diff": "4*(1 - p_2^2) = 4*(p_1^2 + p_3^2), always >= 0",
    "S3_mean_chirality_diff": "8/3 (exact, from <p_j^2> = 1/3 on S^3)",
    "TTCS_caveat": (
        "This is a LOCAL identity-pairing angular difference, not the globally "
        "Green-projected inter-node coefficient c_opp - c_same. The full "
        "source-to-receiver transfer matrix includes Bianchi correction, "
        "kernel projection, product spectral pseudo-inverse, node-frame "
        "transport, and radial extraction. Cancellation in the Green "
        "projection is mathematically possible but not proved or disproved."
    ),
    "what_is_established": (
        "H^4_+(zeta) and H^4_-(zeta) are generically different symmetric "
        "2-tensors. Their radial obstruction overlap differs by 4(1-p_2^2), "
        "which has definite sign >= 0 and mean 8/3 on S^3. This is a "
        "necessary INPUT to the inter-node Green response computation but "
        "not its OUTPUT."
    ),
    "decisive_remaining_computation": (
        "Compute the full product Lichnerowicz Green transfer from source "
        "node to receiver node in the C_{ab} basis, including all 9 tensor "
        "components, Bianchi/gauge correction, kernel projection, and "
        "evaluate c_opp - c_same as a single real number."
    ),
}

outpath = "Sessions/S0910A01/workspace/data/step84_chirality_corrected.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2, default=str)

print(json.dumps(results, indent=2, default=str))
print(f"\nWrote {outpath}")
