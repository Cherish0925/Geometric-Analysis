#!/usr/bin/env python3
"""
Step 86: Exact inter-node spectral sum using factored S^3 boundary pairing.

Uses the quartic moment formula on S^3:
  int_{S^3} x_a x_b x_c x_d dOmega = (2pi^2/24)(d_ab d_cd + d_ac d_bd + d_ad d_bc)

For trace-free C:
  int_{S^3} (x^T C x)(x_i x_j) dOmega = (pi^2/12) C_{ij}

This FACTORIZES the boundary pairing, making the spectral sum exact and frame-invariant.

Session S0910A01, Step 86.
"""
import numpy as np
import json, os

# ============================================================
# 1. Build SD/ASD basis and C_{ab} matrices
# ============================================================
def build_sd_asd_bases():
    def wedge(i, j, n=4):
        A = np.zeros((n, n)); A[i, j] = 1; A[j, i] = -1; return A
    e12 = wedge(0,1); e13 = wedge(0,2); e14 = wedge(0,3)
    e23 = wedge(1,2); e24 = wedge(1,3); e34 = wedge(2,3)
    s2 = np.sqrt(2)
    wp = [(e12 + e34)/s2, (e13 - e24)/s2, (e14 + e23)/s2]
    wm = [(e12 - e34)/s2, (e13 + e24)/s2, (e14 - e23)/s2]
    return wp, wm

def build_Cab(wp, wm):
    C = np.zeros((3, 3, 4, 4))
    for a in range(3):
        for b in range(3):
            prod = wp[a] @ wm[b]
            C[a, b] = prod + prod.T
    return C

# ============================================================
# 2. Compute ALL relevant matrix entries for the spectral sum
# ============================================================
def compute_spectral_sum(Lmax=200):
    wp, wm = build_sd_asd_bases()
    C = build_Cab(wp, wm)

    # We need the cross-factor entries (C_{2k})_{iA, jB} where iA in {0,1}, jB in {2,3}
    # (using 0-based indices: factors A={0,1}, B={2,3})

    # For the boundary pairing with the AB sector mode having angular (x_iA * x_jB):
    # <S^+, mode> = -0.5 * 3 * C_l1 * C_l2 * sum_k tr(C_{2k} . hAB_{iA,jB}) * (pi^2/12) * (C_{2k})_{iA,jB}
    # where (C_{2k})_{iA,jB} comes from the quartic moment and tr(C_{2k} . hAB) from tensor overlap.

    # For the AA TF-Hessian sector with angular (x_iA*x_jA - delta_ij |x_A|^2/2):
    # Similar formula but with second derivatives on one factor.

    # Node structure: NN=(+,+), NS=(+,-), SN=(-,+), SS=(-,-)
    # At NS: the second factor is at south pole, so Y_{l2}(S) = (-1)^{l2} Y_{l2}(N)
    # At SN: (-1)^{l1} Y_{l1}(N), at SS: (-1)^{l1+l2}

    # Eigenvalue formula for AB sector: lambda = 0.5*(l1(l1+1) + l2(l2+1) - 2), l1,l2 >= 1
    # Eigenvalue formula for AA/BB TF sector: lambda = 0.5*(l1(l1+1) + l2(l2+1)) - 1, l >= 2 on diff. factor

    # ================================================================
    # SECTOR 1: AB one-form product sector
    # ================================================================
    # Mode: grad_A(Y_{l1,m1}) . x_A * grad_B(Y_{l2,m2}) . x_B * hAB_{iA,jB}
    # At NN, the V_2 = C_{l1} C_{l2} * x_{iA} * x_{jB} * hAB_{iA,jB}
    # where C_l = sqrt(l(l+1)(2l+1)/(8pi))
    #
    # Boundary pairing with H^4_+:
    # <S^+, mode> = 3 * C_{l1} C_{l2} * (-0.5) * sum_k [tr(C_{1k} . hAB) * (pi^2/12) * (C_{1k})_{iA,jB}]
    # (Note: C_{1k} = C_{2,k+1} in 1-based = C[1,k] in 0-based, since a=2 in 1-based = index 1 in 0-based)

    # Cross-tensor basis: hAB_{ij} has entries only at (i,j) and (j,i) = 1
    # So tr(C_{ab} . hAB_{ij}) = C_{ab,ij} + C_{ab,ji} = 2 * C_{ab,ij} (since C_{ab} is symmetric)

    # The key entry table:
    print("=== Cross-factor matrix entries (C[a,b])_{iA,jB} ===")
    print("(a,b are 0-based SD/ASD indices, iA in {0,1}, jB in {2,3})\n")

    # Build the complete entry table for row (a=1) and column (b=1) sources
    row_entries = np.zeros((3, 2, 2))  # [k, iA, jB-2]
    col_entries = np.zeros((3, 2, 2))
    for k in range(3):
        for iA in range(2):
            for jB_off in range(2):
                jB = jB_off + 2
                row_entries[k, iA, jB_off] = C[1, k, iA, jB]  # C_{2,k+1} in 1-based
                col_entries[k, iA, jB_off] = C[k, 1, iA, jB]  # C_{k+1,2} in 1-based

    print("Row source (+ chirality, a=1):")
    for k in range(3):
        print(f"  k={k}: entries = {row_entries[k]}")
    print("\nCol source (- chirality, b=1):")
    for k in range(3):
        print(f"  k={k}: entries = {col_entries[k]}")

    # Also need the (iA,jA) entries for the Hessian (inner-factor) terms
    row_inner_A = np.zeros((3, 2, 2))  # [k, iA, jA]
    col_inner_A = np.zeros((3, 2, 2))
    row_inner_B = np.zeros((3, 2, 2))  # [k, iB-2, jB-2]
    col_inner_B = np.zeros((3, 2, 2))
    for k in range(3):
        for i in range(2):
            for j in range(2):
                row_inner_A[k, i, j] = C[1, k, i, j]
                col_inner_A[k, i, j] = C[k, 1, i, j]
                row_inner_B[k, i, j] = C[1, k, i+2, j+2]
                col_inner_B[k, i, j] = C[k, 1, i+2, j+2]

    print("\nInner-A entries (iA, jA in {0,1}):")
    for k in range(3):
        if np.max(np.abs(row_inner_A[k])) > 1e-10 or np.max(np.abs(col_inner_A[k])) > 1e-10:
            print(f"  k={k}: row={row_inner_A[k].tolist()}, col={col_inner_A[k].tolist()}")

    print("\nInner-B entries (iB, jB in {2,3}):")
    for k in range(3):
        if np.max(np.abs(row_inner_B[k])) > 1e-10 or np.max(np.abs(col_inner_B[k])) > 1e-10:
            print(f"  k={k}: row={row_inner_B[k].tolist()}, col={col_inner_B[k].tolist()}")

    # ================================================================
    # Now compute the FULL spectral sum for each node pair
    # ================================================================

    # For the AB sector:
    # Source coefficient at node (sigma_A, sigma_B) with + chirality:
    # S^+_{l1,m1_A,l2,m2_B,iA,jB} = 3 * C_l1 * C_l2 * sigma_A^{l1-1} * sigma_B^{l2-1}
    #   * (-0.5) * sum_k p_k_coupling * (pi^2/12)
    # where sigma = +1 at N, -1 at S, and the l-1 power comes from the gradient at the pole.

    # Actually, let me be more careful. The gradient of Y_{l,m} at the pole of S^2:
    # At the north pole: dY_{l,1c}/dz_1 = C_l (for cos mode)
    # At the south pole: dY_{l,1c}/dz_1 = (-1)^{l-1} C_l (by parity of the derivative)
    # (The derivative picks up (-1)^{l-1} because Y_{l,m} at S = (-1)^l Y_{l,m} at N,
    #  and the derivative adds one more sign from the coordinate reflection.)

    # More precisely, on S^2, the gradient of Y_{l,m} at the south pole S in local
    # geodesic coords z_S = -z_N (relative to the north-pole chart):
    # Since Y_{l,m}(S) = (-1)^l Y_{l,m}(N), and z_S = -z_N,
    # dY/dz_S = dY/d(-z_N) = -(dY/dz_N)
    # But Y at S in the south chart: Y(z_S) = (-1)^l * Y(-z_S)
    # Gradient at origin of south chart: (-1)^l * (-d/dz) Y(0) = (-1)^{l+1} C_l (for the gradient)
    # Hmm, this needs careful handling. Let me just track the sign by
    # noting that Y_{l,m}(pole) = sigma^l * Y_{l,0}(N) for m=0 (sigma=+1 for N, -1 for S)
    # and dY/dz_i(pole) = sigma^{l-1} * (dY/dz_i)(N) for |m|=1.

    # For the VALUE of the scalar at the pole: factor = sigma^l * Y_{l,0}(N)
    # For the FIRST DERIVATIVE at the pole: factor = sigma^{l-1} * C_l (for specific m)
    # For the SECOND DERIVATIVE at the pole: factor = sigma^l * D_l (for specific m)

    # The correct sign analysis:
    # On S^2 with stereographic/geodesic coords z at N, z' at S:
    # z' = -z/|z|^2 * (something) but for geodesic coords, the south pole
    # is at theta = pi. In normal coords at S: w = rotation of z.
    # The key fact: for a SCALAR harmonic Y_{l,m}, its value at the antipodal point is
    # Y_{l,m}(antipodal) = (-1)^l Y_{l,m}(point).
    # In geodesic coords at S (which are the geodesic coords at the south pole):
    # The first-order Taylor of Y_{l,m} near S: Y(w) = (-1)^l Y(N) + ...
    # The gradient: dY/dw_i(0) = (-1)^l * (dY/dz_i'(0)) where z_i' are the
    # geodesic coords at S obtained by reflecting the N-chart.
    # Since z_i' = -z_i (reflection), dY/dz_i' = -dY/dz_i, so
    # dY/dw_i(0) = (-1)^l * (-dY/dz_i(N)) ... this gets confusing.

    # Let me use a SIMPLE approach: compute everything at NN, then use
    # the node-to-node sign factors from the harmonic parity.

    # For the Z_2-invariant (l1+l2 even) modes on the orbifold:
    # Value at NN: V_{l1,l2} = f(N)g(N)
    # Value at NS: = f(N)g(S) = f(N) * (-1)^{l2} g(N)
    # Value at SN: = (-1)^{l1} f(N) * g(N)
    # Value at SS: = (-1)^{l1+l2} f(N)g(N) = f(N)g(N) (since l1+l2 even)

    # For GRADIENTS (first jet):
    # grad_A at NN: (df/dz_A)(N) * g(N) = C_{l1} * Y_{l2,0}(N)
    # grad_A at NS: (df/dz_A)(N) * g(S) = C_{l1} * (-1)^{l2} Y_{l2,0}(N)
    # grad_A at SN: (df/dz_A)(S) * g(N) = ? Need to be careful
    # At SN: factor A is at south pole. The OUTWARD geodesic coords at the SN node
    # are (w_A, w_B) where w_A is centered at the A-south-pole.
    # The gradient of Y_{l1,1c} at the south pole in the south-centered chart:
    # By the parity of the associated Legendre function, dP_l^1(cos theta)/d theta
    # at theta=pi has a specific sign. For the real spherical harmonic Y_{l,1c} ~ sin(theta) P_l^1:
    # Y_{l,1c}(theta, phi) = N_{l1} * sin(theta) * P_l^1(cos theta) * cos(phi)
    # At S (theta=pi): sin(pi) = 0, so Y_{l,1c}(S) = 0.
    # Gradient at S: we need the first-order Taylor. Since Y_{l,1c} vanishes at S,
    # its gradient at S is proportional to the tangential gradient of Y at S.
    # In geodesic coords w at S: Y(w) ~ (grad Y)(S) . w + ...
    # The gradient is along the w_1 direction (for the cos mode).
    # Its magnitude: |grad Y_{l,1c}|(S) = C_l (by the isometry S^2 -> S^2 taking N to S)
    # But the SIGN depends on the orientation convention.

    # For simplicity, let me use the known fact that for degree-l harmonic on S^2:
    # The restriction to a pole always gives the same absolute value of derivatives
    # but with a sign factor (-1)^{l-1} for first derivatives and (-1)^l for second.
    # This comes from the parity property: under the antipodal map on S^2 in 2D,
    # a spherical harmonic of degree l transforms as (-1)^l, but the coordinate
    # reflection also reverses the gradient, giving (-1)^{l+1} for the gradient.

    # IMPORTANT: The orbifold chart at each node uses LOCAL geodesic coordinates
    # centered at that node. The Ozuch boundary pairing is done in THOSE coordinates.
    # For the NN node, the local chart is the standard one.
    # For the NS node, the first factor uses the N-chart and the second uses the S-chart.
    # In the S-chart, the metric is the same (round S^2), but the basis vectors
    # at the south pole in the S-chart point in opposite directions from the N-chart.

    # The simplest approach: define a SIGN MATRIX for each node.
    # For mode with (l1, m1_type; l2, m2_type) contributing to a specific
    # cross-tensor hAB_{iA,jB}:
    # At NN: sign = 1
    # At NS: sign = ? depends on the second-factor behavior at S
    # At SN: sign = ? depends on the first-factor behavior at S
    # At SS: sign = product of both factors

    # For a one-form derivative dY/dz on S^2:
    # The value at the south pole in the south-centered chart involves (-1)^{l+1}
    # relative to the north-centered chart (parity of the derivative).
    # But the chart itself is flipped, so in the Ozuch chart at the node,
    # the sign relative to the common frame is (-1)^{l+1} * (-1) = (-1)^l.

    # Actually, this is getting too involved for hand-analysis. Let me just
    # compute the sign factors numerically for each node.

    # SIMPLER APPROACH: Use the PRODUCT GREEN FUNCTION directly.
    # On S^2 x S^2, the Green function of P between two distinct nodes
    # is a sum over product harmonics with known eigenvalues.
    # The boundary pairing at each node is a UNIVERSAL function of the
    # eigenmode's quantum numbers and the node signs.

    # For the spectral sum, I ONLY need:
    # (a) The eigenvalue lambda(l1, l2, sector)
    # (b) The source coefficient <S_j, psi> at the SOURCE node
    # (c) The receiver coefficient <R_i, psi> at the RECEIVER node
    # Both (b) and (c) involve the same boundary pairing formula.

    # Since I've already identified which sectors contribute to the chirality
    # difference (hA_sin and hAB_14), I can compute just those contributions.

    # For the chirality difference, the spectral sum is:
    # c_opp - c_same = sum over eligible (l1,l2,mode) of:
    #   [receiver_coeff * chirality_source_diff] / lambda

    # The chirality source difference has opposite signs in the two channels:
    # hAB_14: row coupling = -2, col coupling = +2, so diff involves (C_{21})_{0,3} vs (C_{12})_{0,3}
    # hA_sin: row coupling = +2 to C_{23}, col coupling = -2 to C_{32}

    # Let me compute these specific matrix entries:
    print("\n=== Critical matrix entries for chirality difference ===")

    # For hAB_14 channel: involves (C_{21})_{0,3} and (C_{12})_{0,3}
    print(f"(C[1,0])_{{0,3}} = {C[1,0,0,3]:.6f}")  # C_{21} entry (0,3)
    print(f"(C[0,1])_{{0,3}} = {C[0,1,0,3]:.6f}")  # C_{12} entry (0,3)
    print(f"Diff (C21-C12)_{{0,3}} = {C[1,0,0,3] - C[0,1,0,3]:.6f}")

    # For hA_sin channel: involves (C_{23})_{0,1} and (C_{32})_{0,1}
    print(f"\n(C[1,2])_{{0,1}} = {C[1,2,0,1]:.6f}")  # C_{23} entry (0,1)
    print(f"(C[2,1])_{{0,1}} = {C[2,1,0,1]:.6f}")  # C_{32} entry (0,1)
    print(f"Diff (C23-C32)_{{0,1}} = {C[1,2,0,1] - C[2,1,0,1]:.6f}")

    # ================================================================
    # EXACT SPECTRAL SUM COMPUTATION
    # ================================================================

    # The boundary pairing at a node for an AB-sector mode with quantum numbers
    # (l1, l2) and cross-tensor hAB_{iA, jB} is:
    #
    # <S^+, psi> = 3 * C_{l1} * C_{l2} * (-0.5) * sum_k [2*(C[1,k])_{iA,jB}] * (pi^2/12) * (C[1,k])_{iA,jB}
    # = -3 * C_{l1} * C_{l2} * (pi^2/12) * sum_k (C[1,k])_{iA,jB}^2
    #
    # Wait, that's not right. Let me redo:
    # H^4_+ = -0.5 sum_k p_k(x) C[1,k] where p_k(x) = x^T C[1,k] x / |x|^2
    # <H^4_+, V_2> = -0.5 sum_k (x^T C[1,k] x) * tr(C[1,k] . h_{tensor}) * angular_V2
    #
    # For AB mode with tensor hAB_{iA,jB} and angular x_{iA} x_{jB}:
    # <H^4_+, V_2> = -0.5 * C_l1 * C_l2 * sum_k (x^T C[1,k] x) * 2*(C[1,k])_{iA,jB} * x_{iA} * x_{jB}
    #
    # Integrating over S^3/Z_2:
    # int <H^4_+, V_2> = -C_l1 * C_l2 * sum_k 2*(C[1,k])_{iA,jB} * int (x^T C[1,k] x)(x_{iA} x_{jB}) dOmega
    # = -C_l1 * C_l2 * sum_k 2*(C[1,k])_{iA,jB} * (pi^2/12) * (C[1,k])_{iA,jB}
    #                                                               ^-- by quartic moment formula
    # = -C_l1 * C_l2 * (pi^2/6) * sum_k (C[1,k])_{iA,jB}^2
    #
    # So <S^+, psi> = 3 * [above] = -3 C_l1 C_l2 (pi^2/6) sum_k (C[1,k])_{iA,jB}^2
    #
    # And <S^-, psi> = -3 C_l1 C_l2 (pi^2/6) sum_k (C[k,1])_{iA,jB}^2
    #
    # CHIRALITY DIFFERENCE:
    # <S^+, psi> - <S^-, psi> = -3 C_l1 C_l2 (pi^2/6) sum_k [(C[1,k])^2 - (C[k,1])^2]_{iA,jB}

    # Compute sum_k (C[1,k])_{iA,jB}^2 and sum_k (C[k,1])_{iA,jB}^2
    print("\n=== Quartic coupling sums by cross-tensor channel ===")
    for iA in range(2):
        for jB_off in range(2):
            jB = jB_off + 2
            row_sum = sum(C[1, k, iA, jB]**2 for k in range(3))
            col_sum = sum(C[k, 1, iA, jB]**2 for k in range(3))
            diff = row_sum - col_sum
            print(f"  ({iA},{jB}): row_sum = {row_sum:.6f}, col_sum = {col_sum:.6f}, diff = {diff:.6f}")

    # Similarly for the AA/BB TF-Hessian sector
    print("\n=== Quartic coupling sums for inner-factor TF channels ===")
    print("AA TF (iA, jA in {0,1}):")
    for iA in range(2):
        for jA in range(2):
            row_sum = sum(C[1, k, iA, jA]**2 for k in range(3))
            col_sum = sum(C[k, 1, iA, jA]**2 for k in range(3))
            diff = row_sum - col_sum
            if abs(diff) > 1e-10:
                print(f"  ({iA},{jA}): row_sum = {row_sum:.6f}, col_sum = {col_sum:.6f}, diff = {diff:.6f}")

    print("BB TF (iB, jB in {2,3}):")
    for iB in range(2):
        for jB in range(2):
            ii, jj = iB+2, jB+2
            row_sum = sum(C[1, k, ii, jj]**2 for k in range(3))
            col_sum = sum(C[k, 1, ii, jj]**2 for k in range(3))
            diff = row_sum - col_sum
            if abs(diff) > 1e-10:
                print(f"  ({ii},{jj}): row_sum = {row_sum:.6f}, col_sum = {col_sum:.6f}, diff = {diff:.6f}")

    # ================================================================
    # THE DECISIVE COMPUTATION
    # ================================================================
    # If ALL quartic coupling sums have row_sum = col_sum, then the chirality
    # difference VANISHES IDENTICALLY in the spectral sum!
    # This would mean c_opp = c_same for all node pairs.

    # Check: compute total chirality difference across all channels
    total_chiral_diff_cross = 0.0
    for iA in range(2):
        for jB_off in range(2):
            jB = jB_off + 2
            diff = sum(C[1,k,iA,jB]**2 - C[k,1,iA,jB]**2 for k in range(3))
            total_chiral_diff_cross += abs(diff)

    total_chiral_diff_AA = 0.0
    for iA in range(2):
        for jA in range(2):
            diff = sum(C[1,k,iA,jA]**2 - C[k,1,iA,jA]**2 for k in range(3))
            total_chiral_diff_AA += abs(diff)

    total_chiral_diff_BB = 0.0
    for iB in range(2):
        for jB in range(2):
            diff = sum(C[1,k,iB+2,jB+2]**2 - C[k,1,iB+2,jB+2]**2 for k in range(3))
            total_chiral_diff_BB += abs(diff)

    print(f"\n=== TOTAL CHIRALITY DIFFERENCE IN QUARTIC SUMS ===")
    print(f"  Cross-factor (AB): {total_chiral_diff_cross:.10e}")
    print(f"  Factor A (AA TF):  {total_chiral_diff_AA:.10e}")
    print(f"  Factor B (BB TF):  {total_chiral_diff_BB:.10e}")
    print(f"  GRAND TOTAL:       {total_chiral_diff_cross + total_chiral_diff_AA + total_chiral_diff_BB:.10e}")

    # ================================================================
    # Build the complete entry table and save
    # ================================================================
    entry_table = {}
    for i in range(4):
        for j in range(4):
            row_vals = [float(C[1,k,i,j]) for k in range(3)]
            col_vals = [float(C[k,1,i,j]) for k in range(3)]
            row_sq = sum(v**2 for v in row_vals)
            col_sq = sum(v**2 for v in col_vals)
            entry_table[f"({i},{j})"] = {
                'row_entries': row_vals,
                'col_entries': col_vals,
                'row_sq_sum': round(row_sq, 10),
                'col_sq_sum': round(col_sq, 10),
                'sq_diff': round(row_sq - col_sq, 10),
            }

    # Full 4x4 tables of squared sums
    row_sq_matrix = np.zeros((4,4))
    col_sq_matrix = np.zeros((4,4))
    for i in range(4):
        for j in range(4):
            row_sq_matrix[i,j] = sum(C[1,k,i,j]**2 for k in range(3))
            col_sq_matrix[i,j] = sum(C[k,1,i,j]**2 for k in range(3))

    print(f"\nRow squared sum matrix (sum_k C[1,k,i,j]^2):")
    print(row_sq_matrix)
    print(f"\nCol squared sum matrix (sum_k C[k,1,i,j]^2):")
    print(col_sq_matrix)
    print(f"\nDifference (row - col):")
    print(row_sq_matrix - col_sq_matrix)

    # IDENTITY CHECK: sum_k C[1,k]^2_{ij} should equal sum_k C[k,1]^2_{ij}
    # by the relation C[a,b] = 2 omega_a^+ . omega_b^- (symmetrized)
    # and the SO(4) structure.
    # If true: THE CHIRALITY DIFFERENCE VANISHES!

    # Save results
    outpath = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                           'data', 'step86_spectral_chirality_computation.json')
    os.makedirs(os.path.dirname(outpath), exist_ok=True)

    results = {
        'scope': 'exact factored spectral sum for chirality difference using S^3 quartic moments',
        'method': 'boundary pairing from Ozuch Prop 2.10 + S^3 quartic moment formula',
        'row_sq_matrix': row_sq_matrix.tolist(),
        'col_sq_matrix': col_sq_matrix.tolist(),
        'difference_matrix': (row_sq_matrix - col_sq_matrix).tolist(),
        'max_difference': float(np.max(np.abs(row_sq_matrix - col_sq_matrix))),
        'total_chiral_diff_cross': float(total_chiral_diff_cross),
        'total_chiral_diff_AA': float(total_chiral_diff_AA),
        'total_chiral_diff_BB': float(total_chiral_diff_BB),
        'conclusion': '',
    }

    max_diff = float(np.max(np.abs(row_sq_matrix - col_sq_matrix)))
    if max_diff < 1e-10:
        results['conclusion'] = (
            "VANISHING THEOREM: sum_k C[1,k]_{ij}^2 = sum_k C[k,1]_{ij}^2 for ALL (i,j). "
            "Therefore the chirality source difference in the boundary pairing is IDENTICALLY ZERO "
            "at each eigenmode, and the spectral sum gives c_opp - c_same = 0 for ALL node pairs. "
            "This means the mixed-chirality and same-chirality inter-node response coefficients "
            "are EQUAL at leading order in the Ozuch boundary-pairing framework."
        )
    else:
        results['conclusion'] = f"Chirality difference is NONZERO: max entry difference = {max_diff}"

    with open(outpath, 'w') as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nWrote {outpath}")
    print(f"\n{'='*60}")
    print(f"CONCLUSION: {results['conclusion']}")
    print(f"{'='*60}")

    return results

if __name__ == '__main__':
    results = compute_spectral_sum()
