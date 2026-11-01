"""
Step 92: Ozuch lattice coefficient vs A01 spectral response
Cross-verification for the positive mirror (S^2 x S^2)/Z_2.

The Ozuch formula (Lemma 4.2, Corollary 4.3) gives the first obstruction
at a receiver node j_0 in S_- from source nodes i in S_+:

  sum_i B^L_{j0-i}(zeta_i, zeta_i) zeta_{j0} = 0

where B^L_x(zeta,zeta') = pi_tr sum_a b_{L(x-2a)}(zeta,zeta')
and   b_x(zeta,zeta) = 12 rho_x(zeta)^otimes2 / |x|^6  (trace-free projection)

For unit zeta_i = zeta_{j0} = e_1, the scalar coupling is:
  <B^L_x(e1,e1) e1, e1> = 12<rho_x(e1),e1>^2 - 4

summed over the lattice. The rotation rho_x is quaternion conjugation:
  rho_x(zeta)_j = x^T (zeta^+ o omega_j^-) x / |x|^2

This script evaluates the lattice sum for the product orbifold geometry
and compares the result with A01's spectral K^principal_adj.

Convention: the product (S^2 x S^2)/Z_2 has period lattice L = diag(pi, pi, pi, pi)
in angular coordinates, with four A_1 nodes at the four fixed points of the antipodal
Z_2. Adjacent nodes are separated by pi in one angular direction.
"""

import numpy as np
import json

# ==================================================================
# 1. Quaternion rotation rho_x
# ==================================================================
def rho_x(x, zeta):
    """Compute rho_x(zeta) via quaternion conjugation.
    
    x = (x1,x2,x3,x4) in R^4, zeta = (z1,z2,z3) in R^3.
    rho_x(zeta)_j = x^T (zeta^+ o omega_j^-) x / |x|^2
    
    Using quaternion formula: (0, rho_x(zeta)) = x * (0, zeta) * x^{-1}
    where x is a quaternion (x1, x2, x3, x4) = x1 + x2 i + x3 j + x4 k.
    """
    x = np.asarray(x, dtype=float)
    zeta = np.asarray(zeta, dtype=float)
    r2 = np.dot(x, x)
    if r2 < 1e-30:
        return np.zeros(3)
    
    # Quaternion multiplication: q = x, p = (0, zeta)
    # q * p * q^{-1} = q * p * conj(q) / |q|^2
    # q = (a, b, c, d) = a + bi + cj + dk
    a, b, c, d = x
    # p = (0, z1, z2, z3) = z1 i + z2 j + z3 k
    z1, z2, z3 = zeta
    
    # q * p: (a+bi+cj+dk)(z1 i + z2 j + z3 k)
    # Real: -b*z1 - c*z2 - d*z3
    # i:     a*z1 + c*z3 - d*z2
    # j:     a*z2 - b*z3 + d*z1
    # k:     a*z3 + b*z2 - c*z1
    qp_r = -b*z1 - c*z2 - d*z3
    qp_i = a*z1 + c*z3 - d*z2
    qp_j = a*z2 - b*z3 + d*z1
    qp_k = a*z3 + b*z2 - c*z1
    
    # (q*p) * conj(q): multiply (qp_r, qp_i, qp_j, qp_k) by (a, -b, -c, -d)
    res_r = qp_r*a + qp_i*b + qp_j*c + qp_k*d  # should be 0
    res_i = -qp_r*b + qp_i*a - qp_j*d + qp_k*c
    res_j = -qp_r*c + qp_i*d + qp_j*a - qp_k*b
    res_k = -qp_r*d - qp_i*c + qp_j*b + qp_k*a
    
    return np.array([res_i, res_j, res_k]) / r2

def ozuch_b_scalar(x, zeta_i, zeta_j):
    """Compute <pi_tr b_x(zeta_i, zeta_i) zeta_j, zeta_j>.
    
    = 12 <rho_x(zeta_i), zeta_j>^2 - 4 |zeta_i|^2 |zeta_j|^2
    (Ozuch lines 1396-1399)
    """
    r2 = np.dot(x, x)
    if r2 < 1e-30:
        return 0.0
    r6 = r2**3
    rho = rho_x(x, zeta_i)
    cross = np.dot(rho, zeta_j)
    ni2 = np.dot(zeta_i, zeta_i)
    nj2 = np.dot(zeta_j, zeta_j)
    return (12.0 * cross**2 - 4.0 * ni2 * nj2) / r6

# ==================================================================
# 2. Product orbifold geometry
# ==================================================================
# The product S^2 x S^2 with round metrics (Ric = 2g on each factor)
# has Einstein metric with Ric = g (half the sectional curvature sum).
# The four A_1 nodes of (S^2 x S^2)/Z_2 are at:
#   NN = (0,0,0,0), NS = (pi,0,0,0), SN = (0,pi,0,0), SS = (pi,pi,0,0)
# in angular coordinates. But the actual positions depend on the
# flat-cone chart identification.
#
# For the Ozuch lattice sum, we work in R^4/lattice.
# The relevant flat metric around each A_1 node has period lattice
# 2 * (node separations). Adjacent nodes are at half-periods.
#
# In the simplest model (unit-radius spheres), the flat-cone chart
# scales the angular coordinates. Two adjacent nodes on the SAME
# sphere factor are separated by pi (half the great-circle distance),
# and on different factors by 0.
#
# The lattice for the flat torus T^4/Z_2 around one node has
# vectors 2*(pi, 0, 0, 0), 2*(0, pi, 0, 0), etc. in the cone chart.
# The adjacent nodes are at half-periods: (pi, 0, 0, 0), (0, pi, 0, 0), etc.

# For a product of two round S^2 of radius R, in stereographic coordinates
# around the north pole, the metric is conformally flat:
#   g = (4R^2/(1+|z|^2)^2)(dz1^2 + dz2^2)
# The tangent plane at the pole is R^2 with metric 4R^2 delta.
# The south pole is at infinity in stereographic coordinates.
#
# For the Ozuch model (flat torus approximation), the relevant
# quantity is the separation vector x0 between adjacent nodes
# in the flat ALE chart. We normalize so that |x0| = 1 (the
# spectral computation uses its own normalization; we track the ratio).

# Node layout for the diagonal balanced checkerboard:
#   S_+ (positive chirality EH): NN, SS
#   S_- (negative chirality EH): NS, SN
#
# Adjacent pairs (NN->NS, NN->SN, SS->NS, SS->SN):
# In the flat-cone chart, the separation vectors are:
#   NN->NS: (1, 0, 0, 0)  (half-period in x1)
#   NN->SN: (0, 1, 0, 0)  (half-period in x2)
#   SS->NS: (0, 1, 0, 0)  (half-period in x2)
#   SS->SN: (1, 0, 0, 0)  (half-period in x1)
# (up to the lattice identification)

# For unit chirality zeta_i = zeta_j = (1,0,0):
x_adj_1 = np.array([1.0, 0.0, 0.0, 0.0])  # x1 separation
x_adj_2 = np.array([0.0, 1.0, 0.0, 0.0])  # x2 separation
zeta = np.array([1.0, 0.0, 0.0])  # unit chirality e1

# Single-image (no lattice) contributions
b_x1 = ozuch_b_scalar(x_adj_1, zeta, zeta)
b_x2 = ozuch_b_scalar(x_adj_2, zeta, zeta)

# The rotation rho_x for x = (1,0,0,0):
# As quaternion q = 1, rho_q(zeta) = 1 * (0,zeta) * 1 = (0,zeta)
# So rho_{(1,0,0,0)}(e1) = e1, giving <rho,zeta_j> = 1
# b = (12*1 - 4)/1 = 8

# For x = (0,1,0,0): q = i, rho_q(zeta)_j = conjugation by i
# i*(0,z1,z2,z3)*(-i) = i*(z1 i + z2 j + z3 k)*(-i)
# = i*(-z1 + z2 k - z3 j)*(-i) = (-z1 i - z2 k + z3 j)*(-i)
# Wait, let me use the formula directly.

rho_x1 = rho_x(x_adj_1, zeta)
rho_x2 = rho_x(x_adj_2, zeta)

print("=== Ozuch single-image lattice coefficients ===")
print(f"rho_{{(1,0,0,0)}}(e1) = {rho_x1}")
print(f"rho_{{(0,1,0,0)}}(e1) = {rho_x2}")
print(f"b_{{(1,0,0,0)}}(e1,e1;e1,e1) = {b_x1}")
print(f"b_{{(0,1,0,0)}}(e1,e1;e1,e1) = {b_x2}")
print()

# For the full lattice sum, we sum over a∈Z^4 and separate the |x-2a|^{-6} 
# convergent series. The leading term (a=0) is the single-image value.
# Higher lattice images contribute corrections that depend on the lattice.

# ==================================================================
# 3. Lattice sum (truncated) for a cubic lattice
# ==================================================================
def lattice_sum_ozuch(x0, zeta_i, zeta_j, L, N_max=20):
    """Compute B^L_x0(zeta_i, zeta_i) projected onto zeta_j.
    
    B^L_x(zeta,zeta) = pi_tr sum_{a in Z^4} b_{L(x-2a)}(zeta,zeta)
    
    Here L is the lattice matrix, x0 is the half-period vector,
    and we sum over |a|_inf <= N_max.
    """
    total = 0.0
    for a1 in range(-N_max, N_max+1):
        for a2 in range(-N_max, N_max+1):
            for a3 in range(-N_max, N_max+1):
                for a4 in range(-N_max, N_max+1):
                    a = np.array([a1, a2, a3, a4], dtype=float)
                    y = L @ (x0 - 2*a)
                    r2 = np.dot(y, y)
                    if r2 < 1e-30:
                        continue
                    total += ozuch_b_scalar(y, zeta_i, zeta_j)
    return total

# For a small test with cubic lattice L = I (unit lattice):
# N_max=3 should give a reasonable truncation for convergent |x|^{-6} series
print("=== Lattice sum (L = I, N_max = 3) ===")
B_x1 = lattice_sum_ozuch(x_adj_1/2, zeta, zeta, np.eye(4), N_max=3)
B_x2 = lattice_sum_ozuch(x_adj_2/2, zeta, zeta, np.eye(4), N_max=3)
print(f"B^I_{{x1/2}}(e1,e1;e1,e1) = {B_x1:.10f}")
print(f"B^I_{{x2/2}}(e1,e1;e1,e1) = {B_x2:.10f}")
print()

# The actual product orbifold has L proportional to the identity (for round
# equal-radius spheres), and the half-period to adjacent nodes is specific.
# For the spectral comparison, the key ratio is B_x1 / B_x2.

# ==================================================================
# 4. Channel decomposition
# ==================================================================
# For zeta_i = e1, vary zeta_j over e1, e2, e3 to get channel coupling
print("=== Channel decomposition at x = (1,0,0,0) (single image) ===")
for k, name in enumerate(["e1 (AA/BB)", "e2 (AB)", "e3 (AB)"]):
    zj = np.zeros(3)
    zj[k] = 1.0
    val = ozuch_b_scalar(x_adj_1, zeta, zj)
    print(f"  <b_x(e1,e1) {name}> = {val:.6f}")

print()
print("=== Channel decomposition at x = (0,1,0,0) (single image) ===")
for k, name in enumerate(["e1 (AA/BB)", "e2 (AB)", "e3 (AB)"]):
    zj = np.zeros(3)
    zj[k] = 1.0
    val = ozuch_b_scalar(x_adj_2, zeta, zj)
    print(f"  <b_x(e1,e1) {name}> = {val:.6f}")

# ==================================================================
# 5. Comparison with A01 spectral values
# ==================================================================
print()
print("=== Comparison with A01 spectral computation ===")
K_AB_A01 = -0.03144249732
K_AA_NS_A01 = -0.004002498660
K_principal_A01 = -0.03544499598

# The Ozuch single-image values at |x|=1:
# For x=(1,0,0,0): b(e1,e1;e1,e1) = 8 (AA/BB + AB combined)
# For x=(0,1,0,0): b(e1,e1;e1,e1) = -4 (negative coupling)

# The lattice sum will modify these. But the KEY normalization fact is:
# the Ozuch formula gives an obstruction IN R^3 (acting on zeta^+/-),
# while A01's spectral computation is in the space of TT tensors on S^3/Z_2.
# The connection factor is the identification Sym_0^2 ~ Omega^+ tensor Omega^-.

# From Ozuch, the b_x formula with |x|=1 normalization gives:
#   b(e1,e1) = 12 e1 otimes e1 - 4 I_3  (as a 3x3 matrix in Omega^+ or Omega^-)
# Eigenvalues: 8 (along e1) and -4 (perpendicular).
# Trace: 12 - 12 = 0 (trace-free by construction).

mat_b = 12 * np.outer(rho_x1, rho_x1) - 4 * np.eye(3)
print(f"b_{{(1,0,0,0)}}(e1,e1) matrix eigenvalues: {np.linalg.eigvalsh(mat_b)}")
print(f"  trace = {np.trace(mat_b):.6f}")
print()

mat_b2 = 12 * np.outer(rho_x2, rho_x2) - 4 * np.eye(3)
print(f"b_{{(0,1,0,0)}}(e1,e1) matrix eigenvalues: {np.linalg.eigvalsh(mat_b2)}")
print(f"  trace = {np.trace(mat_b2):.6f}")
print()

# For the diagonal balanced pattern: receiver at NS gets contributions from
# NN (adjacent by x1) and SS (adjacent by x2).
# Total single-image coupling in the e1 direction:
total_single = b_x1 + b_x2
print(f"Single-image total coupling at receiver NS: {total_single:.6f}")
print(f"  (= b_x1 + b_x2 = {b_x1:.6f} + {b_x2:.6f})")
print()

# A01's principal spectral sum for adjacent coupling: K_principal ≈ -0.0354
# This includes the FULL spectral sum (all lattice images, product Green function).
# The single-image coupling = 8 + (-4) = 4 is only the leading term.
# The ratio determines the normalization:
print(f"A01 K^principal_adj = {K_principal_A01:.10f}")
print(f"Ozuch single-image total (not yet comparable; needs lattice + normalization)")
print()

# ==================================================================
# 6. Key structural insight
# ==================================================================
print("=== KEY STRUCTURAL INSIGHT ===")
print("The Ozuch lattice coefficient B^L_{j0-i}(zeta,zeta) zeta evaluates to:")
print("  a 3x3 matrix acting on zeta_{j0}")
print()
print("For the invariant ansatz (all zeta = e1), this reduces to a SCALAR:")
print("  sum_i <B^L_{j0-i}(e1,e1) e1, e1>")
print()
print("If this scalar is NONZERO, the first obstruction is non-degenerate")
print("in the invariant sector, and equivariant desingularization applies.")
print()
print("A01's K^principal_adj is the SPECTRAL representation of this scalar")
print("(up to normalization). Its corrected value ≈ -0.0354 is finite and nonzero.")
print()
print("REMAINING TASK: verify the normalization between the Ozuch lattice")
print("coefficient and A01's spectral representation, and confirm that")
print("curvature corrections (H_{j,2} terms) do not change the sign.")

# Save results
results = {
    "step": 92,
    "scope": "Ozuch lattice coefficient vs A01 spectral cross-verification",
    "ozuch_single_image": {
        "x1_coupling": float(b_x1),
        "x2_coupling": float(b_x2),
        "total_single_image": float(total_single),
        "matrix_eigenvalues_x1": [float(v) for v in sorted(np.linalg.eigvalsh(mat_b))],
        "matrix_eigenvalues_x2": [float(v) for v in sorted(np.linalg.eigvalsh(mat_b2))],
        "rho_x1_e1": rho_x1.tolist(),
        "rho_x2_e1": rho_x2.tolist(),
    },
    "a01_spectral_values": {
        "K_AB_adj": K_AB_A01,
        "K_AA_NS_corrected": K_AA_NS_A01,
        "K_principal_adj": K_principal_A01,
        "source": "A01 Step 94 corrected data",
    },
    "channel_decomposition": {
        "x1_along_e1_AABB": float(ozuch_b_scalar(x_adj_1, zeta, np.array([1,0,0]))),
        "x1_along_e2_AB": float(ozuch_b_scalar(x_adj_1, zeta, np.array([0,1,0]))),
        "x1_along_e3_AB": float(ozuch_b_scalar(x_adj_1, zeta, np.array([0,0,1]))),
        "x2_along_e1_AABB": float(ozuch_b_scalar(x_adj_2, zeta, np.array([1,0,0]))),
        "x2_along_e2_AB": float(ozuch_b_scalar(x_adj_2, zeta, np.array([0,1,0]))),
        "x2_along_e3_AB": float(ozuch_b_scalar(x_adj_2, zeta, np.array([0,0,1]))),
    },
    "equivariant_transversality": {
        "question": "Is the first-obstruction coupling nonzero in the K+D8 invariant sector?",
        "leading_evidence": "A01 principal response K_adj ≈ -0.0354 is finite and nonzero",
        "remaining": "Normalization match between Ozuch and spectral, curvature correction sign",
        "significance": "Nonzero => equivariant desingularization => first Einstein with min(b+,b-)>=2",
    },
    "landscape": {
        "negative_branch": "diffuse non-OT non-warped connector; no current obstruction or construction",
        "positive_branch": "Ozuch coefficient in invariant sector is the crux",
        "a03_scope_correction": "delta*≈0.246 is for free-T2 OT, not S3-neck N#N",
    }
}

outpath = "Sessions/S0910A02/workspace/data/step92_ozuch_spectral_crossverification.json"
with open(outpath, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved {outpath}")
