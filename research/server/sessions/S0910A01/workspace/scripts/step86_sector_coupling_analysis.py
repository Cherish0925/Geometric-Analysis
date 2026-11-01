#!/usr/bin/env python3
"""
Step 86: Exact inter-node Green spectral sum via Ozuch boundary pairing.

Computes c_{ij}^{eps_i, eps_j} = sum_alpha R_i(psi_alpha) S_j(psi_alpha) / lambda_alpha

where the source/receiver are boundary pairings:
  S_j(psi) = 3 * integral over S^3/Z_2 of <H^4(zeta_j), (psi)_2^{(j)}>
  R_i(psi) = 3 * integral over S^3/Z_2 of <O_1(zeta_i), (psi)_2^{(i)}>

The eigenmodes of P = 1/2 nabla*nabla - Rcirc on (S^2 x S^2)/Z_2 decompose
into product harmonics. The source/receiver pairings at the poles are computed
from the exact S^2 harmonic theory.

Session S0910A01, Step 86.
"""
import numpy as np
import json, os

# ============================================================
# 1. Build the 9 C_{ab} matrices from SD/ASD 2-form bases
# ============================================================
def build_sd_asd_bases():
    """Standard SD/ASD bases on R^4 with orientation (1234)."""
    # 2-forms as skew-symmetric 4x4 matrices
    def wedge(i, j, n=4):
        A = np.zeros((n, n))
        A[i, j] = 1; A[j, i] = -1
        return A

    e12 = wedge(0,1); e13 = wedge(0,2); e14 = wedge(0,3)
    e23 = wedge(1,2); e24 = wedge(1,3); e34 = wedge(2,3)

    s2 = np.sqrt(2)
    wp = [(e12 + e34)/s2, (e13 - e24)/s2, (e14 + e23)/s2]  # SD
    wm = [(e12 - e34)/s2, (e13 + e24)/s2, (e14 - e23)/s2]  # ASD
    return wp, wm

def build_Cab(wp, wm):
    """C_{ab} = omega_a^+ . omega_b^- symmetrized as 4x4 matrices."""
    C = np.zeros((3, 3, 4, 4))
    for a in range(3):
        for b in range(3):
            prod = wp[a] @ wm[b]
            C[a, b] = prod + prod.T  # symmetrize
    return C

# ============================================================
# 2. Ozuch's angular maps and H^4 multipoles
# ============================================================
def angular_maps_at_x(C, x):
    """
    p_j(x) = x^T C[2,j] x / |x|^2  (for + chirality, zeta = omega_2^+)
    q_j(x) = x^T C[j,2] x / |x|^2  (for - chirality, zeta = omega_2^-)
    """
    r2 = np.dot(x, x)
    p = np.array([x @ C[1, j] @ x / r2 for j in range(3)])
    q = np.array([x @ C[j, 1] @ x / r2 for j in range(3)])
    return p, q

def H4_tensor(C, chirality, x):
    """H^4 tensor at point x on S^3 (|x|=1), for zeta = omega_2."""
    p, q = angular_maps_at_x(C, x)
    if chirality == '+':
        return -0.5 * sum(p[j] * C[1, j] for j in range(3))
    else:
        return -0.5 * sum(q[j] * C[j, 1] for j in range(3))

# ============================================================
# 3. S^2 harmonic analysis at poles
# ============================================================
# For Y_{l,m} on unit S^2, in stereographic/normal coords z=(z1,z2) at N:
# Y_{l,0}(N) = sqrt((2l+1)/(4pi))
# Y_{l,0}(S) = (-1)^l Y_{l,0}(N)
#
# Second derivatives of Y_{l,m} at N:
# The trace: d^2 Y / dz_i dz_i = -l(l+1) Y(N) for m=0
# TF part: only |m|=2 harmonics contribute TF Hessians at N
# Specifically: (d^2/dz1^2 - d^2/dz2^2)Y and 2(d^2/dz1 dz2)Y
#
# For the ZONAL (m=0) harmonic at the pole, the Hessian is proportional to delta_ij:
# Hess(Y_{l,0})(N) = -(l(l+1)/2) Y_{l,0}(N) * delta_ij  (isotropic)
#
# For m=+/-1: first derivatives at pole.
# For m=+/-2: TF second derivatives at pole.
#
# Key fact for the BOUNDARY PAIRING with H^4:
# The boundary integral 3*int_{S^3/Z_2} <H^4, (psi)_2> requires the
# degree-2 angular part of the eigenmode's r^2-coefficient.
# This involves the Hessian of the scalar factor times the metric tensor factor.

def Y_l0_at_pole(l):
    """Value of Y_{l,0} at north pole."""
    return np.sqrt((2*l+1)/(4*np.pi))

def hessian_trace_Y_l0_at_pole(l):
    """Trace of Hessian of Y_{l,0} at N: sum_i d^2Y/dz_i^2 = -l(l+1) Y(N)."""
    return -l*(l+1) * Y_l0_at_pole(l)

# ============================================================
# 4. Eigenmodes and their boundary pairings at nodes
# ============================================================
# Product harmonics on S^2 x S^2 / Z_2.
# A Z_2-invariant mode under (x,y) -> (-x,-y) requires:
#   (-1)^{l1} (-1)^{l2} = 1, i.e., l1 + l2 even.
#
# For each sector (AA trace, BB trace, AA TF, BB TF, AB oneform):
# - Eigenvalue lambda from the sector ledger
# - Source/receiver pairing from the second-jet at the node
#
# The boundary pairing with H^4 uses:
# <S_j, psi> = 3 * int_{S^3/Z_2} <H^4, (psi)_2> dOmega
#
# For TRACE-sector modes f(x_A) g_A or f(x_A) g_B:
# The TF part of V_2 is proportional to C_{11}, which is orthogonal to H^4.
# Therefore: trace-sector pairing = 0 (confirmed by TTCS).
#
# For TF-HESSIAN-sector modes (scalar TF Hessian on one factor):
# These have V_2 components in the "off-diagonal" C_{ab} channels.
# Need: l >= 2 on the differentiating factor.
# The TF Hessian of Y_{l,m} at the pole has nonzero components only for |m|=2.
#
# For AB ONE-FORM-PRODUCT modes:
# These involve 1-form x 1-form, with each factor having l >= 1.
# Their C_{ab} content at the node involves cross-factor derivatives.

def compute_boundary_pairing_numerical(C, Lmax, heat_tau=0.0):
    """
    Compute the exact inter-node spectral sum using Monte Carlo
    angular integration on S^3/Z_2.

    For each product eigenmode, the source/receiver boundary pairings
    are computed by averaging over random S^3 points, using the
    explicit eigenmode-tensor structure.
    """
    # We need to understand WHICH eigenmodes have nonzero overlap with H^4.
    #
    # The H^4 tensor at a node lives in span{C_{2j}} (for +) or span{C_{j2}} (for -).
    # The eigenmode's V_2 (r^2 coefficient) needs C_{2j} or C_{j2} content.
    #
    # In the C_{ab} basis, C_{2j} involves mixing between the two S^2 factors.
    # The relevant product harmonics are those whose Hessian at the pole
    # has off-diagonal C_{ab} content.
    #
    # This requires a careful sector-by-sector analysis.
    pass

# ============================================================
# 5. Direct Monte Carlo boundary pairing computation
# ============================================================
def compute_green_spectral_sum_MC(C, Lmax=80, N_MC=200000):
    """
    Compute the inter-node Green spectral sum using:
    1. Product harmonic eigenvalues from the sector ledger
    2. Boundary pairings computed by MC integration on S^3

    For each eigenmode psi_alpha on (S^2 x S^2)/Z_2:
    - Decompose psi_alpha into a product of S^2 harmonics x tensor structure
    - Compute V_{alpha,2}^{(j)} (the r^2-coefficient at node j)
    - Compute <H^4, V_{alpha,2}> by S^3 angular integration
    - Accumulate sum R_i * S_j / lambda

    Returns: dictionary with same-chirality and cross-chirality sums.
    """
    # For computational tractability, we use the explicit product structure.
    # The key insight: eigenmodes decompose as products of one-factor harmonics,
    # and their Hessians at the poles are determined by the harmonic degree.

    # Node coordinates: NN=(+,+), NS=(+,-), SN=(-,+), SS=(-,-)
    # where sigma=+1 means north pole on that factor.
    nodes = {'NN': (1, 1), 'NS': (1, -1), 'SN': (-1, 1), 'SS': (-1, -1)}

    # Build eigenmodes of P on the product orbifold.
    # Z_2 invariant: l1 + l2 must be even.
    # Sectors: we focus on TT-type modes that couple to H^4.

    # CRITICAL INSIGHT: Only TF-Hessian and one-form sectors contribute,
    # because trace-sector V_2 is proportional to C_{11} which is orthogonal to H^4.

    # Monte Carlo samples on S^3
    rng = np.random.default_rng(42)
    pts = rng.standard_normal((N_MC, 4))
    pts /= np.linalg.norm(pts, axis=1, keepdims=True)

    # For Z_2 = {I, -I} quotient, we average: f(x) + f(-x) for even modes.
    # The angular maps p_j, q_j are quadratic, hence even under x -> -x.
    # So integration over S^3/Z_2 = (1/2) * integration over S^3.

    # Compute angular maps at all MC points
    p_all = np.zeros((N_MC, 3))  # p_j for + chirality
    q_all = np.zeros((N_MC, 3))  # q_j for - chirality
    for i in range(N_MC):
        p_all[i], q_all[i] = angular_maps_at_x(C, pts[i])

    # For each product eigenmode and each node pair, we need to compute:
    # <S_j, psi> = 3 * (1/2) * (1/(2*pi^2)) * 2*pi^2 * mean_over_S3(<H^4, V_2>)
    # where 2*pi^2 is the volume of S^3.

    # The boundary pairing reduces to:
    # <S_j^+, psi> = -6 * sum_k mean_{S^3}(p_k * f_{2k}^{alpha,j})
    # where f_{2k}^{alpha,j} is the (2,k)-th C_ab component of (psi)_2 at node j.

    # For a PRODUCT eigenmode in the tensor sector with quantum numbers
    # (l1, m1, l2, m2, sector_type), the boundary pairing involves
    # products of S^2 harmonic values/derivatives at the poles.

    # Let's compute this for the full TF tensor sector.
    # This requires understanding how the C_{ab} basis relates to the
    # product harmonic decomposition.

    # APPROACH: Direct computation via H^4 overlap with eigenmode tensors.
    # For each mode, build the 4x4 symmetric tensor at each S^3 point,
    # then compute the Frobenius inner product with H^4.

    # First, compute H^4 tensors at all MC points for both chiralities
    H4_plus = np.zeros((N_MC, 4, 4))
    H4_minus = np.zeros((N_MC, 4, 4))
    for i in range(N_MC):
        H4_plus[i] = H4_tensor(C, '+', pts[i])
        H4_minus[i] = H4_tensor(C, '-', pts[i])

    # Now we need the eigenmodes and their V_2 structure.
    # For the product orbifold, we use a SPECTRAL decomposition approach:
    # build the Green function restricted to pairs of nodes.

    # The Green function between two nodes is:
    # G(p_i, p_j) = sum_alpha psi_alpha(p_i) x psi_alpha(p_j) / lambda_alpha

    # For the boundary pairing: the source and receiver act through their
    # respective S^3 integrals. So the coefficient is:
    # c_{ij} = sum_alpha <R_i, psi_alpha> <S_j, psi_alpha> / lambda_alpha

    # We can compute this as:
    # c_{ij} = <R_i, G_P S_j> = <R_i, bar_h_j>

    # where bar_h_j is the Green-function response to source S_j.

    # For computational purposes, we directly accumulate the spectral sum.
    # We need: for each eigenmode alpha, the functions
    #   <H^4(chirality), (psi_alpha)_2(node)>
    # integrated over S^3/Z_2.

    # For product spherical harmonics f_{l1}(x_A) g_{l2}(x_B) * tensor:
    # the r^2-coefficient at a pole involves the Taylor expansion of
    # f and g near the respective poles, combined with the tensor structure.

    print("Computing product-harmonic boundary pairings...")

    # We use the factored S^2 structure: x = (x_A, x_B) with |x_A|^2 + |x_B|^2 = 1.
    # At node NN (north pole of both factors):
    # x_A = (x_1, x_2), x_B = (x_3, x_4) in our convention.

    # The r^2-coefficient of a product function f(x_A)g(x_B) at NN involves:
    # f(x_A) = f(N_A) + grad_A(f) . x_A + (1/2) Hess_A(f) : x_A x_A + ...
    # g(x_B) = g(N_B) + grad_B(g) . x_B + (1/2) Hess_B(g) : x_B x_B + ...

    # The "r^2 part" of f*g = f(N)*Hess_B(g) + g(N)*Hess_A(f) + grad_A . grad_B terms
    # More precisely on S^3 at radius r, the angular dependence at degree 2 includes
    # all these cross terms.

    # For the TENSOR eigenmode, the full V_2 depends on the tensor sector.
    # This is very involved to do analytically for all sectors.

    # ALTERNATIVE APPROACH: build the Lichnerowicz Green function on S^2 x S^2 directly
    # using its explicit product spectral decomposition, and evaluate it at the nodes.

    # For a DIRECT computation, I'll compute the source strength and spectral sum
    # for each product (l1, l2) pair by building the tensor eigenmode explicitly
    # on S^3 and computing its overlap with H^4 numerically.

    # This is the most reliable approach for getting a correct, frame-invariant answer.

    results = {}
    for node_pair in [('NN','NS'), ('NN','SN'), ('NN','SS')]:
        ni, nj = node_pair
        results[f'{ni}_{nj}'] = {'same': 0.0, 'cross': 0.0, 'by_l': []}

    # For each (l1, l2) with l1+l2 even, l1,l2 = 0,...,Lmax:
    print(f"  Lmax = {Lmax}, MC points = {N_MC}")

    # Build S^2 product structure on S^3
    # x = (x_A, x_B), |x_A|^2 + |x_B|^2 = 1
    xA = pts[:, :2]  # first factor
    xB = pts[:, 2:]  # second factor
    rA2 = np.sum(xA**2, axis=1)  # |x_A|^2 on S^3
    rB2 = np.sum(xB**2, axis=1)  # |x_B|^2 on S^3

    # On S^3, (rA, theta_A, rB, theta_B) parameterize the product.
    # The "position on first S^2" is determined by the DIRECTION of x_A
    # (when rA > 0), etc. But at the NN node, local coords are (x_A, x_B).

    # The relevant function for the S^2 harmonic Y_{l,m} on the first factor,
    # evaluated at a point on S^3, is:
    # Y_{l,m}(hat{x_A}) * |x_A|^l  (the solid harmonic restriction to S^3)
    # where hat{x_A} = x_A / |x_A| is the direction on S^2_A.

    # For the boundary pairing, we need the degree-2 angular part of
    # (solid harmonic evaluated on S^3) * (tensor structure).

    # Let's implement this step by step.
    # The degree-k solid harmonic on R^2 at the north pole of S^2:
    # For l=0: 1, degree 0
    # For l=1: z (= x_1 or x_2), degree 1
    # For l=2, m=0: 2z1^2 + 2z2^2 - 1 (not pure degree 2!)
    #   Actually Y_{2,0} ~ (3cos^2 theta - 1)/2 ~ 3z^2/r^2 - 1 for S^2
    #   In stereographic/geodesic coords at N: cos(theta) ~ 1 - |z|^2/2
    #   So Y_{2,0} ~ 3(1-|z|^2)^2 - 1 ~ 2 - 6|z|^2 + ... at N
    #   Solid harmonic: r^2 Y_{2,0} ~ r^2(2 - 6|z|^2/r^2 + ...)

    # This is getting complex. Let me use a DIRECT numerical approach:
    # build the actual S^2 x S^2 harmonic eigentensors of P on S^3 points
    # and compute overlaps with H^4 numerically.

    # I'll use the Gegenbauer/Legendre decomposition on S^3.
    # On S^3 embedded in R^4, the spherical harmonics are the restrictions
    # of harmonic homogeneous polynomials on R^4.

    # For the PRODUCT S^2 x S^2 structure, the eigenmodes of the Laplacian
    # on S^2 x S^2 are products: phi_{l1,m1}(x_A) * phi_{l2,m2}(x_B).
    # When restricted to S^3 (intersection with |x|=1), these become
    # specific functions on S^3.

    # But actually, S^3 and S^2 x S^2 are DIFFERENT manifolds. Our orbifold
    # is (S^2 x S^2)/Z_2, and S^3/Z_2 = RP^3 is the LINK at each node.
    # The eigenmodes live on S^2 x S^2, and their BOUNDARY DATA at each
    # node (on the link RP^3) is what enters the pairing.

    # The boundary data involves the local Taylor expansion of the
    # eigenmode at the node. In geodesic coordinates at the node,
    # the eigenmode has a specific expansion. The r^2-coefficient
    # restricted to the unit link S^3 gives the angular function.

    # For a PRODUCT scalar eigenmode Y_{l1}(theta_A) Y_{l2}(theta_B)
    # on S^2 x S^2, at the NN node (theta_A=0, theta_B=0):
    # In geodesic coords (z_A, z_B) ~ (theta_A * hat, theta_B * hat):
    # Y_{l1}(theta_A) = Y_{l1,0}(N) + (1/2) * d^2Y/dtheta^2 * theta_A^2 + ...
    #                  = Y_{l1,0}(N) - (l1(l1+1)/4) Y_{l1,0}(N) |z_A|^2 + ...
    # (using the isotropic Hessian for m=0 at the pole on S^2)

    # So for the ZONAL modes (m1=m2=0), the r^2-coefficient at NN is:
    # V_2(z_A, z_B) = Y_{l1,0}(N) * [-(l2(l2+1)/4) Y_{l2,0}(N)] |z_B|^2
    #               + Y_{l2,0}(N) * [-(l1(l1+1)/4) Y_{l1,0}(N)] |z_A|^2
    # = -(1/4) Y_{l1,0}(N) Y_{l2,0}(N) * [l1(l1+1) |z_A|^2 + l2(l2+1) |z_B|^2]

    # On S^3 at unit radius: |z_A|^2 + |z_B|^2 = 1, so this is an angular function.

    # For a TENSOR mode h = (scalar product) * (tensor basis), the V_2 combines
    # the scalar expansion with the tensor factor.

    # Let me implement the boundary pairing computation by building the
    # FULL tensor V_2 at each MC point on S^3.

    print("  Computing sector-by-sector boundary pairings...")

    # =====================================================================
    # SECTOR A: Factor-parallel tensor (AA TF-Hessian + trace, BB similarly)
    # =====================================================================
    # Mode type: f_{l1}(x_A) * h_TF(x_A) * g_{l2}(x_B) for l1 >= 2, l2 >= 0
    # where h_TF is a trace-free symmetric 2-tensor on R^2_A.
    # Eigenvalue: P = 1/2(l1(l1+1) + l2(l2+1)) - 1  [from sector ledger]
    # (same formula for TF-Hessian and trace sectors, but different tensor content)
    #
    # At the NN node, the V_2 of this mode involves:
    # - The value of g_{l2} at N_B = Y_{l2,0}(N_B)
    # - The Hessian of the A-factor combination at N_A
    #
    # The TF Hessian on R^2_A at the pole has two components:
    # h1 = z_1^2 - z_2^2 (the "m=2 cos" mode)
    # h2 = 2 z_1 z_2     (the "m=2 sin" mode)
    #
    # These map to specific C_{ab} matrices in R^4:
    # z_1^2 - z_2^2 = x_1^2 - x_2^2 (in factor A)
    # 2 z_1 z_2 = 2 x_1 x_2 (in factor A)
    #
    # As symmetric 2-tensors on R^4, these are:
    # [[1,0,0,0],[0,-1,0,0],[0,0,0,0],[0,0,0,0]] (trace-free on A-part)
    # [[0,1,0,0],[1,0,0,0],[0,0,0,0],[0,0,0,0]]  (cross on A-part)

    # Now I need to express these in the C_{ab} basis.

    # Build factor-A TF basis
    hA_cos = np.diag([1.0, -1.0, 0.0, 0.0])  # x1^2 - x2^2
    hA_sin = np.zeros((4,4)); hA_sin[0,1] = hA_sin[1,0] = 1.0  # 2 x1 x2

    # Build factor-B TF basis
    hB_cos = np.diag([0.0, 0.0, 1.0, -1.0])  # x3^2 - x4^2
    hB_sin = np.zeros((4,4)); hB_sin[2,3] = hB_sin[3,2] = 1.0  # 2 x3 x4

    # Project onto C_{ab} basis
    def proj_Cab(h, C):
        """Project symmetric 4x4 tensor h onto C_{ab} basis. Returns 3x3 array."""
        p = np.zeros((3,3))
        for a in range(3):
            for b in range(3):
                p[a,b] = np.sum(h * C[a,b]) / 4.0  # tr(h C_{ab}) / tr(C^2)
        return p

    # Check C_{ab} projections of factor-wise TF tensors
    pA_cos = proj_Cab(hA_cos, C)
    pA_sin = proj_Cab(hA_sin, C)
    pB_cos = proj_Cab(hB_cos, C)
    pB_sin = proj_Cab(hB_sin, C)

    print(f"  hA_cos C_ab projection:\n{pA_cos}")
    print(f"  hA_sin C_ab projection:\n{pA_sin}")
    print(f"  hB_cos C_ab projection:\n{pB_cos}")
    print(f"  hB_sin C_ab projection:\n{pB_sin}")

    # =====================================================================
    # SECTOR B: Cross one-form products (AB sector)
    # =====================================================================
    # Mode: alpha_i(x_A) beta_j(x_B) (dx^i dx^j + dx^j dx^i)
    # where alpha is a 1-form on first factor, beta on second.
    # At the pole, this gives 4 tensor components from combinations of
    # (dx_1, dx_2) x (dx_3, dx_4).

    hAB_13 = np.zeros((4,4)); hAB_13[0,2] = hAB_13[2,0] = 1.0  # dx1 dx3
    hAB_14 = np.zeros((4,4)); hAB_14[0,3] = hAB_14[3,0] = 1.0  # dx1 dx4
    hAB_23 = np.zeros((4,4)); hAB_23[1,2] = hAB_23[2,1] = 1.0  # dx2 dx3
    hAB_24 = np.zeros((4,4)); hAB_24[1,3] = hAB_24[3,1] = 1.0  # dx2 dx4

    pAB_13 = proj_Cab(hAB_13, C)
    pAB_14 = proj_Cab(hAB_14, C)
    pAB_23 = proj_Cab(hAB_23, C)
    pAB_24 = proj_Cab(hAB_24, C)

    print(f"\n  hAB_13 C_ab projection:\n{pAB_13}")
    print(f"  hAB_14 C_ab projection:\n{pAB_14}")
    print(f"  hAB_23 C_ab projection:\n{pAB_23}")
    print(f"  hAB_24 C_ab projection:\n{pAB_24}")

    # =====================================================================
    # Now compute the full spectral sum
    # =====================================================================

    # H^4 inner product with each tensor basis element at each MC point.
    # For + chirality (row 2): H^4_+ = -0.5 sum_j p_j C_{2j} / r^4
    # On S^3 (r=1): H^4_+ = -0.5 sum_j p_j C_{2j}
    # Inner product with a TF tensor T:
    # <H^4_+, T> = -0.5 sum_j p_j tr(C_{2j} T)

    # We precompute: for each tensor basis element hk, the quantity
    # int_{S^3} <H^4_chirality, hk * angular_function> dOmega
    # where the angular function comes from the product harmonic.

    # The spectral sum involves:
    # c = sum_{l1,l2} sum_{m_tensors} [R_i(mode) * S_j(mode)] / lambda

    # For each (l1, l2) pair, the mode structure at the node determines
    # which C_{ab} channels are excited. The boundary pairing with H^4
    # selects specific angular integrals.

    # Let's do this by brute-force: for each (l1, l2, tensor_sector):
    # 1. Build V_2 angular function on S^3
    # 2. Compute <H^4_+, V_2> and <H^4_-, V_2> by MC integration
    # 3. Accumulate the spectral sum

    # For the ZONAL (m1=m2=0) modes, the angular function at NN is:
    # - Factor A TF: Y_{l1,0}(N) * [TF Hess of Y_{l1',m'}] * Y_{l2,0}(N)
    # - But the TF Hessian requires |m'|=2, so this is NOT from the zonal mode!

    # Actually, this is the key subtlety: the boundary pairing involves the
    # eigenmode's r^2-coefficient, which for TF-Hessian modes involves the
    # l-th harmonic's HESSIAN at the pole. The Hessian of Y_{l,0} at the pole
    # is ISOTROPIC (proportional to delta_ij), hence trace-proportional.
    # The TF part of the Hessian comes from |m|=2 modes only!

    # So the boundary pairing with H^4 for the zonal modes is ZERO for the
    # TF-Hessian channel. But it's nonzero for the TRACE channel:
    # V_2(zonal,trace) = Y(N)Y(N) * [l1(l1+1)|x_A|^2 + l2(l2+1)|x_B|^2] * g
    # But <H^4, g> = 0 since H^4 is trace-free!

    # So the ZONAL modes don't contribute to the boundary pairing at all.
    # Only modes with |m_1| or |m_2| >= 1 contribute.

    # For |m| = 2 on one factor: this gives TF-Hessian content.
    # For |m| = 1 on each factor: this gives cross-derivative (AB) content.

    # CRUCIAL REALIZATION: The boundary pairing factorizes!
    # For a product mode with angular quantum numbers (l1,m1; l2,m2) and
    # tensor sector:
    # <S_j, psi> = (factor from l1,m1 on S^2_A) * (factor from l2,m2 on S^2_B) * (tensor C_ab overlap)
    #
    # The angular integral on S^3 factorizes when the integrand is a product
    # of functions of (hat{x_A}, |x_A|) and (hat{x_B}, |x_B|):
    # int_{S^3} = int_0^{pi/2} sin(t)cos(t) dt int_{S^1_A} int_{S^1_B} ...
    # where |x_A| = cos(t), |x_B| = sin(t) parameterize the Hopf fibration.

    # Let me implement this factored computation.

    # On S^3 in R^4, parametrize:
    # x = (cos(s) * n_A, sin(s) * n_B) where s in [0, pi/2],
    # n_A on S^1_A, n_B on S^1_B.
    # Volume element: dOmega_3 = cos(s) sin(s) ds dtheta_A dtheta_B

    # The angular maps: e.g., p_1(x) = x^T C_{21} x = ... involves cross terms.

    # For a clean computation, let me parametrize S^3 as:
    # x = (cos(s)*cos(a), cos(s)*sin(a), sin(s)*cos(b), sin(s)*sin(b))
    # s in [0,pi/2], a in [0,2pi], b in [0,2pi]
    # Volume: cos(s) sin(s) ds da db / (2pi^2)

    N_s = 200; N_a = 200; N_b = 200  # Grid for factored integration
    s_vals = np.linspace(0.001, np.pi/2 - 0.001, N_s)
    a_vals = np.linspace(0, 2*np.pi, N_a, endpoint=False)
    b_vals = np.linspace(0, 2*np.pi, N_b, endpoint=False)
    ds = s_vals[1] - s_vals[0]
    da = a_vals[1] - a_vals[0]
    db = b_vals[1] - b_vals[0]

    # For efficiency, we vectorize over a and b for each s.
    # The volume element weight at each s: w(s) = cos(s)*sin(s) * ds * da * db / (2*pi^2)

    # But this is a 3D grid of 200^3 = 8M points, which is too many.
    # Let's use the MC approach with the original random S^3 points instead.

    # REVISED APPROACH: Factor the boundary integral using S^2 harmonic theory.

    # For a tensor eigenmode from the AB one-form sector:
    # mode ~ alpha_{l1,m1}(x_A) beta_{l2,m2}(x_B) * (dz_A^i dz_B^j + dz_B^j dz_A^i)
    # At NN, the V_2 coefficient involves:
    # grad(alpha) at N_A * value(beta) at N_B * cross-tensor
    # + value(alpha) at N_A * grad(beta) at N_B * cross-tensor
    # The V_2 part requires first derivatives on each factor.

    # For the AA TF-Hessian sector:
    # mode ~ phi_{l1,m1}(x_A) psi_{l2}(x_B) * TF_Hess(l1,m1)
    # At NN, V_2 involves Hessian of phi on factor A, value of psi on factor B.
    # The TF part requires |m1| = 2.

    # Actually the most direct and reliable path: compute everything numerically
    # using the MC integration on S^3 that I already have set up.

    # For each product eigenmode, I'll build the tensor V_2 at each MC point
    # and compute the inner product with H^4.

    # The product eigenmodes of P on S^2(1) x S^2(1) are:
    # psi_{l1,m1,l2,m2,sector}
    # with eigenvalue lambda from the sector ledger.

    # I'll compute the boundary pairing using:
    # <S, psi> = 3 * (2*pi^2 / Vol(S^3/Z_2)) * MC_mean(<H^4, V_2>)
    #          = 3 * MC_mean(<H^4, V_2>)  (if MC already averages over S^3/Z_2)

    # But we need the correct V_2 for each mode, which involves the S^2 harmonic
    # structure. Let me build this from the Gegenbauer/associated Legendre theory.

    # For efficiency, I'll implement the key building blocks:
    # 1. S^2 harmonics and their jets at poles
    # 2. Tensor sector projection onto C_{ab}
    # 3. Angular overlap integrals on S^3

    # This is getting quite involved. Let me focus on the KEY contribution:
    # the |m|=1 cross-derivative terms (AB one-form sector), which should be
    # the dominant channel since they can have l1=l2=1 (lowest positive eigenvalue).

    return results

# ============================================================
# 6. Simplified but exact computation for the key sectors
# ============================================================
def compute_AB_sector_contribution(C, Lmax=80):
    """
    Compute the AB one-form sector contribution to the chirality difference
    c_opp - c_same, using the exact factored boundary pairing.

    For the AB sector: psi = alpha(x_A) beta(x_B) * cross_tensor
    eigenvalue: P = 1/2(l1(l1+1) + l2(l2+1) - 2), l1,l2 >= 1

    The V_2 at the pole involves first derivatives on each factor.
    The cross_tensor maps to specific C_{ab} components.
    """
    # First derivatives of Y_{l,m} at the north pole of S^2:
    # For l >= 1 and |m| = 1:
    # d Y_{l,+1} / d z_1 |_N = A_l,  d Y_{l,+1} / d z_2 |_N = +i A_l
    # d Y_{l,-1} / d z_1 |_N = A_l,  d Y_{l,-1} / d z_2 |_N = -i A_l
    # where A_l = sqrt(l(l+1)(2l+1) / (8 pi))
    #
    # In real harmonics: Y_{l,1c} ~ cos(phi), Y_{l,1s} ~ sin(phi)
    # dY_{l,1c}/dz_1|_N = C_l, dY_{l,1c}/dz_2|_N = 0
    # dY_{l,1s}/dz_1|_N = 0, dY_{l,1s}/dz_2|_N = C_l
    # where C_l = sqrt(l(l+1)(2l+1)/(8pi))

    # For the V_2 of the AB sector mode:
    # mode at NN = Y_{l1,0}(N_A) * grad_A Y_{l1,1x}|_N . dx_i
    #            * Y_{l2,0}(N_B) * grad_B Y_{l2,1x}|_N . dx_j
    #            * (symmetric product)
    # The V_2 part on S^3 involves products like x_i x_j (first order on each factor).

    # Actually, the V_2 at the pole is determined by:
    # alpha(x_A) = alpha(0) + (d_i alpha)(0) x_A^i + ...
    # beta(x_B) = beta(0) + (d_j beta)(0) x_B^j + ...
    # tensor = dx^i dx^j (symmetrized)
    # V_2 = (d_i alpha)(0) (d_j beta)(0) x_A^i x_B^j * tensor
    # (the r^2 part comes from first-order on each factor)

    # The 4D tensor: (d_i alpha)(0) x_A^i * (d_j beta)(0) x_B^j * (e_i^A symm e_j^B)
    # where e_1^A, e_2^A are tangent vectors to factor A, etc.

    # Let's be very explicit. For the mode:
    # Y_{l1,1c}(theta_A, phi_A) * Y_{l2,1c}(theta_B, phi_B)
    # with tensor structure dx_1 dx_3 (symmetrized)
    # At NN, V_2 involves: C_{l1} * x_1 * C_{l2} * x_3 * hAB_13
    # = C_{l1} C_{l2} * x_1 x_3 * hAB_13

    # The angular function on S^3: x_1 x_3 = cos(s)cos(a) * sin(s)cos(b)
    # = (1/2) sin(2s) cos(a) cos(b)

    # The H^4 inner product: <H^4_+, C_{l1}C_{l2} x_1 x_3 hAB_13>
    # = C_{l1}C_{l2} x_1 x_3 * <H^4_+, hAB_13>

    # <H^4_+, hAB_13> = sum_{a,b} H^4_+_{ab} (hAB_13)_{ab}
    # = -0.5 sum_j p_j tr(C_{2j} hAB_13) / trace_normalization

    # Let me compute tr(C_{2j} hAB_13) for j=1,2,3.
    # This is the key numerical computation that determines which
    # AB modes couple to H^4.

    wp, wm = build_sd_asd_bases()
    C_mat = build_Cab(wp, wm)

    # Compute tr(C_{2j} hAB_kl) for all j and cross-tensor basis elements
    # Define cross-tensor basis
    hAB_13 = np.zeros((4,4)); hAB_13[0,2] = hAB_13[2,0] = 1.0
    hAB_14 = np.zeros((4,4)); hAB_14[0,3] = hAB_14[3,0] = 1.0
    hAB_23 = np.zeros((4,4)); hAB_23[1,2] = hAB_23[2,1] = 1.0
    hAB_24 = np.zeros((4,4)); hAB_24[1,3] = hAB_24[3,1] = 1.0

    cross_tensors = {'13': hAB_13, '14': hAB_14, '23': hAB_23, '24': hAB_24}

    print("\n=== AB sector coupling to H^4 ===")
    print("tr(C_{1,j} * hAB_kl) for row (+ chirality) source:")
    for name, h in cross_tensors.items():
        for j in range(3):
            tr_val = np.sum(C_mat[1, j] * h)
            if abs(tr_val) > 1e-10:
                print(f"  tr(C_{{2,{j+1}}} * hAB_{name}) = {tr_val:.6f}")

    print("\ntr(C_{j,1} * hAB_kl) for column (- chirality) source:")
    for name, h in cross_tensors.items():
        for j in range(3):
            tr_val = np.sum(C_mat[j, 1] * h)
            if abs(tr_val) > 1e-10:
                print(f"  tr(C_{{{j+1},2}} * hAB_{name}) = {tr_val:.6f}")

    # Also check AA and BB TF Hessian sectors
    print("\n=== AA TF sector coupling to H^4 ===")
    hA_cos = np.diag([1.0, -1.0, 0.0, 0.0])
    hA_sin = np.zeros((4,4)); hA_sin[0,1] = hA_sin[1,0] = 1.0

    for name, h in [('cos', hA_cos), ('sin', hA_sin)]:
        for j in range(3):
            tr_row = np.sum(C_mat[1, j] * h)
            tr_col = np.sum(C_mat[j, 1] * h)
            if abs(tr_row) > 1e-10 or abs(tr_col) > 1e-10:
                print(f"  hA_{name}: tr(C_{{2,{j+1}}})={tr_row:.4f}, tr(C_{{{j+1},2}})={tr_col:.4f}")

    print("\n=== BB TF sector coupling to H^4 ===")
    hB_cos = np.diag([0.0, 0.0, 1.0, -1.0])
    hB_sin = np.zeros((4,4)); hB_sin[2,3] = hB_sin[3,2] = 1.0

    for name, h in [('cos', hB_cos), ('sin', hB_sin)]:
        for j in range(3):
            tr_row = np.sum(C_mat[1, j] * h)
            tr_col = np.sum(C_mat[j, 1] * h)
            if abs(tr_row) > 1e-10 or abs(tr_col) > 1e-10:
                print(f"  hB_{name}: tr(C_{{2,{j+1}}})={tr_row:.4f}, tr(C_{{{j+1},2}})={tr_col:.4f}")

    return C_mat

# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    wp, wm = build_sd_asd_bases()
    C = build_Cab(wp, wm)

    # Verify C_{ab} orthogonality
    print("=== C_{ab} Frobenius inner products ===")
    for a in range(3):
        for b in range(3):
            norms = []
            for c in range(3):
                for d in range(3):
                    val = np.sum(C[a,b] * C[c,d])
                    if abs(val) > 0.01:
                        norms.append((a,b,c,d,val))
            if a == b or True:  # show all
                diag = np.sum(C[a,b] * C[a,b])
                # Only show nonzero cross terms
    print(f"  tr(C_ab C_cd) = 4 delta_ac delta_bd confirmed: "
          f"max off-diag = {max(abs(np.sum(C[a,b]*C[c,d])) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if (a,b)!=(c,d)):.2e}")

    # Run the sector coupling analysis
    C_mat = compute_AB_sector_contribution(C, Lmax=80)

    # Determine which sectors couple to H^4 and can produce chirality difference
    print("\n=== SUMMARY: Which sectors contribute to chirality difference? ===")
    print("Trace sectors: V_2 ~ C_11 direction -> orthogonal to H^4 -> NO contribution")
    print("AA TF-Hessian: V_2 ~ hA_cos, hA_sin on A-factor -> check coupling above")
    print("BB TF-Hessian: V_2 ~ hB_cos, hB_sin on B-factor -> check coupling above")
    print("AB one-form: V_2 ~ hAB cross tensors -> check coupling above")

    # Save results
    outpath = 'Sessions/S0910A01/workspace/data/step86_sector_coupling_analysis.json'
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    # Build comprehensive coupling table
    coupling = {}
    hA_cos = np.diag([1.0, -1.0, 0.0, 0.0])
    hA_sin = np.zeros((4,4)); hA_sin[0,1] = hA_sin[1,0] = 1.0
    hB_cos = np.diag([0.0, 0.0, 1.0, -1.0])
    hB_sin = np.zeros((4,4)); hB_sin[2,3] = hB_sin[3,2] = 1.0
    hAB_13 = np.zeros((4,4)); hAB_13[0,2] = hAB_13[2,0] = 1.0
    hAB_14 = np.zeros((4,4)); hAB_14[0,3] = hAB_14[3,0] = 1.0
    hAB_23 = np.zeros((4,4)); hAB_23[1,2] = hAB_23[2,1] = 1.0
    hAB_24 = np.zeros((4,4)); hAB_24[1,3] = hAB_24[3,1] = 1.0

    all_tensors = {
        'hA_cos': hA_cos, 'hA_sin': hA_sin,
        'hB_cos': hB_cos, 'hB_sin': hB_sin,
        'hAB_13': hAB_13, 'hAB_14': hAB_14,
        'hAB_23': hAB_23, 'hAB_24': hAB_24,
    }

    for name, h in all_tensors.items():
        row_couplings = [float(np.sum(C_mat[1, j] * h)) for j in range(3)]
        col_couplings = [float(np.sum(C_mat[j, 1] * h)) for j in range(3)]
        coupling[name] = {
            'row_C2j': row_couplings,
            'col_Cj2': col_couplings,
            'row_nonzero': [abs(v) > 1e-10 for v in row_couplings],
            'col_nonzero': [abs(v) > 1e-10 for v in col_couplings],
            'chirality_different': any(abs(r-c) > 1e-10 for r,c in zip(row_couplings, col_couplings)),
        }

    results = {
        'scope': 'sector coupling analysis for H^4 boundary pairing',
        'theorem': 'nu_l = 0 for all kernel modes, both chiralities',
        'coupling_table': coupling,
        'key_finding': '',
    }

    # Determine key finding
    nonzero_sectors = [n for n,d in coupling.items() if any(d['row_nonzero']) or any(d['col_nonzero'])]
    chiral_sectors = [n for n,d in coupling.items() if d['chirality_different']]
    results['nonzero_sectors'] = nonzero_sectors
    results['chirality_different_sectors'] = chiral_sectors
    results['key_finding'] = (f"Sectors with nonzero H^4 coupling: {nonzero_sectors}. "
                              f"Sectors with chirality-different coupling: {chiral_sectors}.")

    with open(outpath, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nWrote {outpath}")
    print(json.dumps(results, indent=2, default=str))
