#!/usr/bin/env python3
"""
Step 84: Detailed chirality H^4 difference algebra and
obstruction projection analysis.

The key finding from step84_chirality_angular_difference.py is that
H^4(zeta^+) != H^4(zeta^-). This script:
1. Derives the exact formula for Delta = H4_+ - H4_-
2. Checks whether Delta survives the Ozuch obstruction projection
3. Computes the angular integrals relevant for inter-node response

Session S0910A01. Agent2 / Constructor.
"""
import numpy as np
import json

# Standard 2-form bases
def e_wedge(i, j, n=4):
    A = np.zeros((n, n))
    A[i, j] = 1.0; A[j, i] = -1.0
    return A

e12=e_wedge(0,1); e13=e_wedge(0,2); e14=e_wedge(0,3)
e23=e_wedge(1,2); e24=e_wedge(1,3); e34=e_wedge(2,3)

wp = [e12+e34, e13-e24, e14+e23]  # omega^+
wm = [e12-e34, e13+e24, e14-e23]  # omega^-

# Cross-composition matrix C[j,k] = omega_j^+ . omega_k^-
C = np.zeros((3, 3, 4, 4))
for j in range(3):
    for k in range(3):
        C[j,k] = wp[j] @ wm[k]

results = {}

# ===========================================================
# 1. The antisymmetric part: A[j,k] = C[j,k] - C[k,j]
# ===========================================================
# H4_+ = -sum_j rho_j C[zeta_idx, j]   (zeta = omega_2, so idx=1)
# H4_- = -sum_j rho_j C[j, zeta_idx]
# Delta = -sum_j rho_j * A[1, j]  where A[j,k] = C[j,k] - C[k,j]
# A[1,1] = 0, so only j=0 and j=2 contribute.

A01 = C[0,1] - C[1,0]  # asymmetry for omega_1^+omega_2^- vs omega_2^+omega_1^-
A21 = C[2,1] - C[1,2]  # asymmetry for omega_3^+omega_2^- vs omega_2^+omega_3^-

# Delta = rho_1 * (C[1,0]-C[0,1]) + rho_3 * (C[1,2]-C[2,1])
#       = -rho_1 * A01 - rho_3 * A21

results["A01_matrix"] = A01.tolist()
results["A21_matrix"] = A21.tolist()

# Verify these are symmetric (important for H^4 as sym 2-tensor)
results["A01_symmetric_error"] = float(np.max(np.abs(A01 - A01.T)))
results["A21_symmetric_error"] = float(np.max(np.abs(A21 - A21.T)))
results["A01_trace"] = float(np.trace(A01))
results["A21_trace"] = float(np.trace(A21))

# Explicit entries:
# A01 = C[0,1]-C[1,0] = (omega_1^+ omega_2^-) - (omega_2^+ omega_1^-)
print("A01 = C[0,1]-C[1,0]:")
print(A01)
print("A21 = C[2,1]-C[1,2]:")
print(A21)

# ===========================================================
# 2. Express Delta in the cross-composition basis
# ===========================================================
# The 9 matrices C[j,k] form a basis of S^2_0(R^4).
# Let's verify they're linearly independent and trace-free.
basis = C.reshape(9, 16)
rank = np.linalg.matrix_rank(basis, tol=1e-10)
results["cross_basis_rank"] = int(rank)  # should be 9

# Check Delta is in the span of these basis elements
# Delta(x) = -rho_1(x) A01 - rho_3(x) A21
# A01 = C[0,1] - C[1,0]
# A21 = C[2,1] - C[1,2]
# So Delta = -rho_1(C[0,1]-C[1,0]) - rho_3(C[2,1]-C[1,2])
# = -rho_1 C[0,1] + rho_1 C[1,0] - rho_3 C[2,1] + rho_3 C[1,2]

# ===========================================================
# 3. Obstruction mode analysis
# ===========================================================
# The radial obstruction mode at a +chirality node is O_1^4 = -theta_1^- . theta_1^+ / r^4
# In our coordinates, for insertion zeta = omega_2:
# theta_1^- = rho(zeta)^- / |rho| (first ASD basis after rotation)
# theta_1^+ = zeta^+ / |zeta| = omega_2^+ (first SD basis)
#
# But rho depends on x, so the obstruction mode also depends on x!
# O_1^4(x) = -rho_x^-/|rho| . omega_2^+/|omega_2| / r^4  [for +chirality]
# For -chirality: O_1^4(x) = -rho_x^+/|rho| . omega_2^-/|omega_2| / r^4

# The PROJECTION of Delta onto O_1^4 involves:
# <Delta, O_1^4>_{S^3} = integral over S^3 of trace(Delta(x) . O_1^4(x))

# Let's compute trace(Delta . O_1) at each point x
# For +chirality receiver: O_1^+ ~ sum_j (rho_j/|rho|) C[j, 1] = (rho^- . omega_2^+)

# Wait, O_k^4 = -theta_1^- . theta_k^+ / r^4 (from Ozuch, line 347)
# For general zeta: O_k(zeta^+) = zeta_{(k)}^+ . rho(zeta)^- / r^4  (line 369)
# So O_1 for zeta=omega_2 is (omega_2^+/|omega_2|) . rho^-/|rho|? No...
# From line 369: o_k(zeta^+) = zeta_{(k)}^+ . rho(zeta)^- / r^4
# where zeta_{(1)}^+ = zeta^+/|zeta|, and zeta_{(2)}, zeta_{(3)} complete the basis.
# So o_1(omega_2^+) = omega_2^+ . rho(omega_2)^- / r^4
# = sum_j rho_j * (omega_2^+ . omega_j^-) / r^4 = sum_j rho_j C[1,j] / r^4

# Which is -H^4_+! (up to a factor of 2) [Remark 1.19 says O_1^4 = 2 H^4]

# The key is: the projection of H^4 from a SOURCE at another node
# against O_1 at the RECEIVER is:
# <H^4_source, O_1_receiver>_{pointwise}

# For same chirality (source +, receiver +):
# H^4_source = sum_j rho_j C[1,j], O_1_receiver = sum_k rho_k C[1,k]
# Inner product = sum_{j,k} rho_j rho_k tr(C[1,j] C[1,k])

# For opp chirality (source -, receiver +):
# H^4_source = sum_j rho_j C[j,1], O_1_receiver = sum_k rho_k C[1,k]
# Inner product = sum_{j,k} rho_j rho_k tr(C[j,1] C[1,k])

# The chirality difference in the pointwise inner product:
# sum_{j,k} rho_j rho_k [tr(C[1,j]C[1,k]) - tr(C[j,1]C[1,k])]

# Let's compute the Gram matrices
Gram_same = np.zeros((3, 3))  # tr(C[1,j] C[1,k])
Gram_cross = np.zeros((3, 3))  # tr(C[j,1] C[1,k])

for j in range(3):
    for k in range(3):
        Gram_same[j, k] = np.trace(C[1,j] @ C[1,k])
        Gram_cross[j, k] = np.trace(C[j,1] @ C[1,k])

Gram_diff = Gram_same - Gram_cross

results["Gram_same_chirality"] = Gram_same.tolist()
results["Gram_cross_chirality"] = Gram_cross.tolist()
results["Gram_difference"] = Gram_diff.tolist()
results["Gram_diff_is_zero"] = bool(np.max(np.abs(Gram_diff)) < 1e-14)

print("\nGram matrix for same chirality tr(C[1,j]C[1,k]):")
print(Gram_same)
print("\nGram matrix for cross chirality tr(C[j,1]C[1,k]):")
print(Gram_cross)
print("\nDifference:")
print(Gram_diff)

# ===========================================================
# 4. Angular integral of the pointwise inner product
# ===========================================================
# The chirality-difference contribution to the inter-node response is:
# integral_{S^3} sum_{j,k} rho_j(x) rho_k(x) * Gram_diff[j,k] * K(x) dsigma
# where K(x) encodes the Green kernel angular dependence.

# If Gram_diff = 0, then the chirality difference vanishes AT THE LEVEL
# of the pointwise H^4 . O_1 inner product, regardless of K(x).

# If Gram_diff != 0, we need to know which rho_j rho_k moments survive.
# rho_j are quadratic on S^3, so rho_j rho_k are quartic (ell=0,2,4).
# The ell=0 (average) part:
# <rho_j rho_k>_{S^3} = integral of rho_j rho_k over S^3 / Vol(S^3)

np.random.seed(84)
N = 200000
raw = np.random.randn(N, 4)
pts = raw / np.linalg.norm(raw, axis=1, keepdims=True)

def rho_vec(x):
    r2 = np.dot(x, x)
    rho1 = -2*(x[0]*x[3]+x[1]*x[2])/r2
    rho2 = -(x[0]**2-x[1]**2+x[2]**2-x[3]**2)/r2
    rho3 = 2*(x[0]*x[1]-x[2]*x[3])/r2
    return np.array([rho1, rho2, rho3])

rhos = np.array([rho_vec(x) for x in pts])

# Compute <rho_j rho_k> (mean over S^3)
rho_corr = np.zeros((3, 3))
for j in range(3):
    for k in range(3):
        rho_corr[j, k] = np.mean(rhos[:, j] * rhos[:, k])

results["rho_correlation_matrix_S3_mean"] = rho_corr.tolist()

# The ell=0 chirality difference contribution:
# sum_{j,k} <rho_j rho_k> * Gram_diff[j,k]
ell0_chirality_diff = np.sum(rho_corr * Gram_diff)
results["ell0_chirality_difference"] = float(ell0_chirality_diff)

print(f"\nRho correlation matrix (mean over S^3):")
print(rho_corr)
print(f"\nell=0 chirality difference: {ell0_chirality_diff:.6e}")

# ===========================================================
# 5. Full L^2 norm of Delta
# ===========================================================
# ||Delta||^2_{L^2(S^3)} = integral |Delta(x)|^2 dsigma
# Delta = -rho_1 A01 - rho_3 A21
# |Delta|^2 = rho_1^2 |A01|^2 + rho_3^2 |A21|^2 + 2 rho_1 rho_3 tr(A01 A21)

norm_A01_sq = np.sum(A01**2)
norm_A21_sq = np.sum(A21**2)
cross_A = np.trace(A01 @ A21) + np.trace(A01.T @ A21)  # Frobenius inner product
# Actually Frobenius inner = sum_{ij} A01_{ij} A21_{ij} = tr(A01^T A21)
cross_A_correct = np.sum(A01 * A21)

results["norm_A01_squared"] = float(norm_A01_sq)
results["norm_A21_squared"] = float(norm_A21_sq)
results["A01_A21_inner"] = float(cross_A_correct)

# <|Delta|^2>_{S^3} = <rho_1^2> |A01|^2 + <rho_3^2> |A21|^2 + 2<rho_1 rho_3> (A01.A21)
mean_Delta_sq = (rho_corr[0,0] * norm_A01_sq + rho_corr[2,2] * norm_A21_sq
                 + 2 * rho_corr[0,2] * cross_A_correct)
results["mean_Delta_sq_analytic"] = float(mean_Delta_sq)
results["mean_Delta_sq_numerical"] = float(np.mean([np.sum(
    (-rhos[i,0]*A01 - rhos[i,2]*A21)**2) for i in range(min(N, 50000))]))

# ===========================================================
# 6. Key conclusion about chirality coupling at the obstruction level
# ===========================================================
if np.max(np.abs(Gram_diff)) < 1e-10:
    obs_conclusion = (
        "SURPRISING: Despite H4_+ != H4_- as tensors, their pointwise inner "
        "product with O_1 (the radial obstruction mode) is IDENTICAL for both "
        "chiralities. This means the chirality difference is INVISIBLE to the "
        "radial obstruction projection. The leading-order inter-node response "
        "is chirality-independent, and c_opp = c_same at the H^4 angular level."
    )
    results["chirality_decoupling_at_obstruction"] = True
else:
    obs_conclusion = (
        "The Gram difference is nonzero: same-chirality and cross-chirality "
        "inner products with O_1 are different. The chirality difference IS "
        "visible at the obstruction level."
    )
    results["chirality_decoupling_at_obstruction"] = False

results["obstruction_level_conclusion"] = obs_conclusion

# ===========================================================
# 7. Additional check: transverse obstruction modes O_2, O_3
# ===========================================================
# O_2 and O_3 are the transverse modes (already eliminated by J-parity in Steps 78-80)
# But let's check if they see the chirality difference.
# O_2(zeta^+) = zeta_{(2)}^+ . rho^- / r^4 = sum_j rho_j C[2_perp, j]
# where zeta_{(2)}^+ is perpendicular to zeta^+/|zeta| = omega_2^+
# For zeta = omega_2, choose zeta_{(2)}^+ = omega_1^+, zeta_{(3)}^+ = omega_3^+

# O_2 corresponds to index 0 (omega_1^+), O_3 to index 2 (omega_3^+)
Gram_O2_same = np.zeros((3, 3))
Gram_O2_cross = np.zeros((3, 3))
for j in range(3):
    for k in range(3):
        Gram_O2_same[j, k] = np.trace(C[1,j] @ C[0,k])  # H4_+ vs O_2
        Gram_O2_cross[j, k] = np.trace(C[j,1] @ C[0,k])  # H4_- vs O_2

Gram_O2_diff = Gram_O2_same - Gram_O2_cross
results["Gram_O2_diff"] = Gram_O2_diff.tolist()
results["Gram_O2_diff_maxabs"] = float(np.max(np.abs(Gram_O2_diff)))

# O_3
Gram_O3_same = np.zeros((3, 3))
Gram_O3_cross = np.zeros((3, 3))
for j in range(3):
    for k in range(3):
        Gram_O3_same[j, k] = np.trace(C[1,j] @ C[2,k])
        Gram_O3_cross[j, k] = np.trace(C[j,1] @ C[2,k])

Gram_O3_diff = Gram_O3_same - Gram_O3_cross
results["Gram_O3_diff"] = Gram_O3_diff.tolist()
results["Gram_O3_diff_maxabs"] = float(np.max(np.abs(Gram_O3_diff)))

print(f"\nGram O2 difference max: {np.max(np.abs(Gram_O2_diff)):.6e}")
print(f"Gram O3 difference max: {np.max(np.abs(Gram_O3_diff)):.6e}")

# Save
outpath = "Sessions/S0910A01/workspace/data/step84_chirality_obstruction_projection.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2, default=str)
print(f"\nWrote {outpath}")
print(f"\nFinal conclusion: {obs_conclusion}")
