#!/usr/bin/env python3
"""
Step 84: Compute the chirality-dependent angular difference between
H^4(zeta^+) and H^4(zeta^-) for the product orbifold (S^2 x S^2)/Z_2.

This script computes:
1. The exact angular vectors rho_x(omega_2^+) and rho_x(omega_2^-)
2. Verifies |rho^+|^2 = |rho^-|^2 (scalar H^4 is chirality-independent)
3. Computes the tensor difference H^4_+ - H^4_- as a 4x4 symmetric matrix
4. Decomposes the angular difference in S^3 harmonics
5. Evaluates the inter-node angular projection relevant for Green response

Session S0910A01. Agent2 / Constructor.
"""
import numpy as np
import json
from scipy.special import sph_harm
from numpy.linalg import norm

# ============================================================
# Standard SD/ASD 2-form bases on R^4
# ============================================================
def make_2form(i, j, n=4):
    """Skew matrix for e_i wedge e_j (0-indexed)."""
    A = np.zeros((n, n))
    A[i, j] = 1.0
    A[j, i] = -1.0
    return A

e12 = make_2form(0, 1)
e13 = make_2form(0, 2)
e14 = make_2form(0, 3)
e23 = make_2form(1, 2)
e24 = make_2form(1, 3)
e34 = make_2form(2, 3)

# Self-dual: omega_k^+
omega_plus = [e12 + e34, e13 - e24, e14 + e23]
# Anti-self-dual: omega_k^-
omega_minus = [e12 - e34, e13 + e24, e14 - e23]

def rho_vector(zeta_plus, omega_mp, x):
    """
    Compute Ozuch angular vector rho_x(zeta) in the dual (mp) basis.
    zeta_plus: 4x4 skew matrix (SD 2-form)
    omega_mp: list of 3 dual basis 4x4 skew matrices (ASD 2-forms)
    x: point in R^4 (unit vector on S^3)
    Returns: 3-vector rho.
    """
    r2 = np.dot(x, x)
    rho = np.zeros(3)
    for j in range(3):
        comp = zeta_plus @ omega_mp[j]  # composition as 4x4 matrices
        rho[j] = x @ comp @ x / r2
    return rho

# ============================================================
# 1. Compute rho for both chiralities at zeta = omega_2
# ============================================================
# For +chirality: zeta^+ = omega_2^+, dual basis = omega^-
# rho_x(zeta)_j = x^T (zeta^+ . omega_j^-) x / |x|^2

# For -chirality: zeta^- = omega_2^-, dual basis = omega^+
# rho_x(zeta)_j = x^T (zeta^- . omega_j^+) x / |x|^2
# But Ozuch defines rho using zeta^+ always (Def 1.14)!
# For -chirality EH, H^4(zeta^-) = -zeta^- . rho(zeta)^+ / (2r^4)
# where rho is computed FROM zeta^+ not zeta^-.
# Let me re-read: the map rho_x in Def 1.14 maps R^3 -> R^3 via
# rho_x(zeta)_j = x^T(zeta^+ . omega_j^-) x / |x|^2
# where zeta^+ = sum_k zeta_k omega_k^+

# For the NEGATIVE chirality (Section 1.2.3, eq before Prop 1.16):
# eh_{zeta^-} = e - zeta^- . rho(zeta)^+ / (2r^4) + O(...)
# Here rho(zeta)^+ = sum_j rho_j omega_j^+ where rho_j are the SAME
# as computed by Def 1.14 (using zeta^+).

# So both chiralities use the SAME rho vector from Def 1.14.
# The difference is in how rho and zeta combine:
# H^4(+) = -rho^- . zeta^+ / (2r^4)  (ASD rho composed with SD zeta)
# H^4(-) = -zeta^- . rho^+ / (2r^4)  (ASD zeta composed with SD rho)

# Wait, let me re-read:
# Prop 1.16(1): eh_{zeta^+} = e - rho(zeta)^- . zeta^+ / (2r^4) + O(...)
# Section 1.2.3: eh_{zeta^-} = e - zeta^- . rho(zeta)^+ / (2r^4) + O(...)

# So H^4(zeta^+) = -rho(zeta)^- . zeta^+ / (2r^4)
# And H^4(zeta^-) = -zeta^- . rho(zeta)^+ / (2r^4)

# These are the same rho but composed differently with zeta.

results = {}

# For zeta = (0,1,0), i.e. omega_2:
zeta_coeffs = np.array([0.0, 1.0, 0.0])
zeta_plus_mat = sum(c * w for c, w in zip(zeta_coeffs, omega_plus))  # omega_2^+
zeta_minus_mat = sum(c * w for c, w in zip(zeta_coeffs, omega_minus))  # omega_2^-

# Sample S^3 points
np.random.seed(84)
N_samples = 50000
raw = np.random.randn(N_samples, 4)
pts = raw / norm(raw, axis=1, keepdims=True)

# Compute rho at each point (same for both chiralities)
rhos = np.array([rho_vector(zeta_plus_mat, omega_minus, x) for x in pts])

# Construct rho as SD and ASD 2-forms at each point
def rho_as_form(rho_vec, basis):
    """Convert 3-vector rho to a 4x4 skew matrix using the given basis."""
    return sum(rho_vec[j] * basis[j] for j in range(3))

# H^4(zeta^+) = -(rho^- . zeta^+) / (2r^4)  as 4x4 symmetric matrix
# H^4(zeta^-) = -(zeta^- . rho^+) / (2r^4)

def compute_H4_plus(rho_vec, x):
    """H^4 for +chirality at point x (ignoring 1/(2r^4) factor)."""
    rho_m = rho_as_form(rho_vec, omega_minus)
    return -(rho_m @ zeta_plus_mat)  # ASD . SD composition -> symmetric

def compute_H4_minus(rho_vec, x):
    """H^4 for -chirality at point x (ignoring 1/(2r^4) factor)."""
    rho_p = rho_as_form(rho_vec, omega_plus)
    return -(zeta_minus_mat @ rho_p)  # ASD . SD composition -> symmetric

# ============================================================
# 2. Verify |rho^+|^2 = |rho^-|^2 (both use the same rho)
# ============================================================
# Actually, this is trivially true since both chiralities use the SAME
# rho vector from Def 1.14. The angular norm is identical.
# What differs is the TENSOR structure of H^4.

# But let me verify the norm of H^4 itself
norms_plus = np.zeros(N_samples)
norms_minus = np.zeros(N_samples)
traces_plus = np.zeros(N_samples)
traces_minus = np.zeros(N_samples)
diff_norms = np.zeros(N_samples)

for i in range(N_samples):
    h4p = compute_H4_plus(rhos[i], pts[i])
    h4m = compute_H4_minus(rhos[i], pts[i])
    # Check symmetry
    norms_plus[i] = np.sqrt(np.sum(h4p**2))
    norms_minus[i] = np.sqrt(np.sum(h4m**2))
    traces_plus[i] = np.trace(h4p)
    traces_minus[i] = np.trace(h4m)
    diff_norms[i] = np.sqrt(np.sum((h4p - h4m)**2))

results["H4_norm_difference_max"] = float(np.max(np.abs(norms_plus - norms_minus)))
results["H4_norm_difference_mean"] = float(np.mean(np.abs(norms_plus - norms_minus)))
results["H4_trace_plus_max"] = float(np.max(np.abs(traces_plus)))
results["H4_trace_minus_max"] = float(np.max(np.abs(traces_minus)))
results["H4_tensor_difference_norm_max"] = float(np.max(diff_norms))
results["H4_tensor_difference_norm_mean"] = float(np.mean(diff_norms))
results["H4_norms_are_equal"] = bool(np.max(np.abs(norms_plus - norms_minus)) < 1e-12)

# ============================================================
# 3. Compute the chirality difference tensor Delta = H4_+ - H4_-
# ============================================================
# At each point x, Delta(x) is a symmetric 4x4 matrix.
# Examine its eigenvalue structure.

Delta_eigenvalues = np.zeros((N_samples, 4))
for i in range(min(N_samples, 5000)):  # subsample for eigenvalues
    h4p = compute_H4_plus(rhos[i], pts[i])
    h4m = compute_H4_minus(rhos[i], pts[i])
    Delta = h4p - h4m
    evals = np.sort(np.linalg.eigvalsh(Delta))
    Delta_eigenvalues[i] = evals

results["Delta_eigenvalue_ranges"] = {
    f"eval_{k}": [float(np.min(Delta_eigenvalues[:5000, k])),
                  float(np.max(Delta_eigenvalues[:5000, k]))]
    for k in range(4)
}

# ============================================================
# 4. Angular harmonic decomposition of the difference
# ============================================================
# On S^3, functions can be expanded in homogeneous polynomials.
# The rho functions are quadratic (ell=2 in S^3 harmonics).
# H^4 involves products like rho . zeta, which are also quadratic.
# The difference H4_+ - H4_- involves specific combinations.

# Let's check: does the difference vanish on average over S^3?
Delta_mean = np.zeros((4, 4))
for i in range(N_samples):
    h4p = compute_H4_plus(rhos[i], pts[i])
    h4m = compute_H4_minus(rhos[i], pts[i])
    Delta_mean += (h4p - h4m)
Delta_mean /= N_samples

results["Delta_mean_over_S3"] = {
    "max_abs_entry": float(np.max(np.abs(Delta_mean))),
    "matrix": Delta_mean.tolist()
}

# Check: does the SQUARED difference (proxy for energy) vanish?
Delta_sq_mean = np.mean(diff_norms**2)
results["Delta_squared_norm_mean"] = float(Delta_sq_mean)

# ============================================================
# 5. Product Green-projected inter-node angular difference
# ============================================================
# For the obstruction integral, we need the angular integral of
# Delta . K(angle) where K encodes the Green kernel evaluated
# between source and receiver nodes.
#
# On S^2 x S^2 with round metric, the nodes are at:
# NN = (N,N), SS = (S,S), NS = (N,S), SN = (S,N)
# In R^4 tangent coordinates centered at NN, the other nodes are at
# distance pi (for SS) or pi/sqrt(2) (for NS, SN) -- but the exact
# geometry depends on the product metric normalization.
#
# The key quantity is: does Delta(x) have DIFFERENT angular projections
# at different nodes?
#
# Near node NN: the S^3 link has x-coordinates (x0,x1,x2,x3)
# Near node NS: the S^3 link has shifted coordinates
#
# For a FIRST diagnostic, we evaluate the angular "chirality tensor"
# at specific reference points on S^3 that correspond to the
# directions toward other nodes.

# Direction from NN toward NS: in product coordinates,
# NN = (0,0)_1 x (0,0)_2 (north of both)
# NS = (0,0)_1 x (pi,0)_2 (north of first, south of second)
# In the tangent plane of the product at NN, the direction toward NS
# is along the second factor's pole direction.
# In R^4: (x0,x1) ~ first S^2, (x2,x3) ~ second S^2
# Direction toward NS: x2-axis, i.e. (0,0,1,0)

x_toward_NS = np.array([0.0, 0.0, 1.0, 0.0])
x_toward_SN = np.array([1.0, 0.0, 0.0, 0.0])
x_toward_SS = np.array([1.0, 0.0, 1.0, 0.0]) / np.sqrt(2)

# Also try generic directions
x_generic1 = np.array([1.0, 1.0, 1.0, 1.0]) / 2.0
x_generic2 = np.array([1.0, 0.0, 0.0, 1.0]) / np.sqrt(2)

test_directions = {
    "toward_NS": x_toward_NS,
    "toward_SN": x_toward_SN,
    "toward_SS": x_toward_SS,
    "generic1": x_generic1,
    "generic2": x_generic2,
}

direction_results = {}
for name, x in test_directions.items():
    rho = rho_vector(zeta_plus_mat, omega_minus, x)
    h4p = compute_H4_plus(rho, x)
    h4m = compute_H4_minus(rho, x)
    Delta = h4p - h4m
    direction_results[name] = {
        "rho": rho.tolist(),
        "H4_plus_trace": float(np.trace(h4p)),
        "H4_minus_trace": float(np.trace(h4m)),
        "Delta_Frobenius_norm": float(np.sqrt(np.sum(Delta**2))),
        "Delta_eigenvalues": np.sort(np.linalg.eigvalsh(Delta)).tolist(),
        "Delta_matrix": Delta.tolist(),
    }

results["directional_Delta"] = direction_results

# ============================================================
# 6. Curvature-level chirality difference
# ============================================================
# The curvature difference enters through:
# d_e R^-(H^4(zeta^+)) = 12 pi_tr(rho^- (x) rho^-) / r^6  [in End(Omega^-)]
# d_e R^+(H^4(zeta^-)) = 12 pi_tr(rho^+ (x) rho^+) / r^6  [in End(Omega^+)]
#
# But rho expressed in the - vs + basis gives the SAME coefficients!
# rho^- = sum rho_j omega_j^- and rho^+ = sum rho_j omega_j^+
# So pi_tr(rho^- (x) rho^-) and pi_tr(rho^+ (x) rho^+) have
# IDENTICAL 3x3 matrix entries (just in different basis 2-forms).
#
# This means: the curvature perturbation has the SAME pattern in both
# sectors! The chirality difference enters through how the Lichnerowicz
# Green kernel COUPLES the source sector to the receiver sector.
#
# Same chirality: Omega^- source -> Omega^- obstruction (intra-sector)
# Opp chirality: Omega^+ source -> Omega^- obstruction (cross-sector)

# On the product S^2 x S^2 (Einstein with Rm = R^+ + R^- + scalar):
# The Lichnerowicz operator on S^2(T*M) couples different 2-form sectors.
# Let's check whether the product structure creates cross-sector coupling.

# Compute the composition omega_j^+ . omega_k^- for all j,k
# These are symmetric 4x4 matrices (the mixed compositions)
cross_compositions = np.zeros((3, 3, 4, 4))
for j in range(3):
    for k in range(3):
        cross_compositions[j, k] = omega_plus[j] @ omega_minus[k]

# Check: are omega_j^+ omega_k^- = omega_k^- omega_j^+ (commutativity)?
max_comm_err = 0.0
for j in range(3):
    for k in range(3):
        fwd = omega_plus[j] @ omega_minus[k]
        bwd = omega_minus[k] @ omega_plus[j]
        max_comm_err = max(max_comm_err, np.max(np.abs(fwd - bwd)))
results["SD_ASD_commutation_error"] = float(max_comm_err)

# The 9 compositions omega_j^+ omega_k^- form a basis of S^2_0(R^4)
# (traceless symmetric 2-tensors). Their traces:
comp_traces = np.zeros((3, 3))
for j in range(3):
    for k in range(3):
        comp_traces[j, k] = np.trace(cross_compositions[j, k])
results["cross_composition_traces"] = comp_traces.tolist()
# Should all be zero (SD and ASD 2-forms are orthogonal)

# Now: H^4(zeta^+) at zeta = omega_2, in the cross-composition basis:
# H^4(+) = -(rho^- . omega_2^+) = -sum_j rho_j (omega_j^- . omega_2^+)
# = -sum_j rho_j (omega_2^+ . omega_j^-)  [by commutativity]
# = -sum_j rho_j * cross_compositions[1][j]  (using 0-indexed: omega_2^+ = index 1)

# H^4(-) = -(omega_2^- . rho^+) = -sum_j rho_j (omega_2^- . omega_j^+)
# = -sum_j rho_j (omega_j^+ . omega_2^-)  [by commutativity]
# = -sum_j rho_j * cross_compositions[j][1]

# So: H4_+ = -sum_j rho_j * C[1,j] and H4_- = -sum_j rho_j * C[j,1]
# where C[j,k] = omega_j^+ . omega_k^-

# The difference: Delta = H4_+ - H4_- = -sum_j rho_j * (C[1,j] - C[j,1])

# Check: is C[j,k] = C[k,j]? i.e. omega_j^+ omega_k^- = omega_k^+ omega_j^-?
C_symmetry = np.zeros((3, 3))
for j in range(3):
    for k in range(3):
        C_symmetry[j, k] = np.max(np.abs(cross_compositions[j, k] - cross_compositions[k, j]))
results["cross_composition_jk_vs_kj_maxdiff"] = float(np.max(C_symmetry))
results["C_jk_equals_C_kj"] = bool(np.max(C_symmetry) < 1e-14)

# If C[j,k] = C[k,j], then Delta = 0 and H4_+ = H4_-!
# If C[j,k] != C[k,j], then the chirality difference is nonzero.

# Let's print the actual matrices
C_diff = {}
for j in range(3):
    for k in range(3):
        diff = cross_compositions[j, k] - cross_compositions[k, j]
        if np.max(np.abs(diff)) > 1e-14:
            C_diff[f"C[{j},{k}]-C[{k},{j}]"] = diff.tolist()

results["nonzero_C_asymmetries"] = C_diff if C_diff else "ALL ZERO - H4_+ = H4_-"

# ============================================================
# 7. Decisive conclusion
# ============================================================
if np.max(C_symmetry) < 1e-14:
    conclusion = (
        "CRITICAL FINDING: omega_j^+ . omega_k^- = omega_k^+ . omega_j^- "
        "for all j,k (as 4x4 symmetric matrices). This means "
        "H^4(zeta^+) = H^4(zeta^-) for any zeta! "
        "The +chirality and -chirality EH bubbles produce IDENTICAL H^4 tensors. "
        "Therefore c_opp = c_same and the chirality difference vanishes at "
        "the H^4 level. The obstruction at order t^3 is chirality-INDEPENDENT. "
        "If the same-chirality coefficient vanishes (from KE control), "
        "the mixed-chirality coefficient vanishes too."
    )
else:
    conclusion = (
        "H^4(zeta^+) != H^4(zeta^-) in general. "
        "The chirality difference is nonzero at the H^4 level."
    )

results["conclusion"] = conclusion

# Also verify with explicit numerical check
h4_diff_max = 0.0
for i in range(min(N_samples, 10000)):
    h4p = compute_H4_plus(rhos[i], pts[i])
    h4m = compute_H4_minus(rhos[i], pts[i])
    h4_diff_max = max(h4_diff_max, np.max(np.abs(h4p - h4m)))
results["H4_plus_minus_H4_minus_maxdiff_numerical"] = float(h4_diff_max)

# Save
outpath = "Sessions/S0910A01/workspace/data/step84_chirality_angular_difference.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2, default=str)
print(json.dumps(results, indent=2, default=str))
print(f"\nWrote {outpath}")
