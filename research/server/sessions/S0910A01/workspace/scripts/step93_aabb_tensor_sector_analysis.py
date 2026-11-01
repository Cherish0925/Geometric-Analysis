#!/usr/bin/env python3
"""
Step 93: AA/BB trace-free tensor sector analysis for the product-orbifold
chirality-odd Green coefficient.

STEP 94 CORRECTION: the divergence interpretation from this script is superseded.
The script divides the full-Lie magnetic tensor, with pole amplitude 4b, by the
electric norm mu(mu-2)/2 instead of the correct four-times-larger norm. Use
step94_corrected_aabb_principal_response.py for the corrected principal response.

The AA-sector modes on S^2(1) x S^2(1) are h = phi(x_B) T(x_A), where T is
a trace-free symmetric 2-tensor on S^2_A and phi is a scalar on S^2_B.  The
BB-sector is the same with A and B exchanged.

On the unit S^2, trace-free symmetric 2-tensors decompose into:
  * "electric" (scalar TF Hessian): T = Hess_A f - (1/2)(Delta_A f) g_A,
    l >= 2, eigenvalue of rough Laplacian = l(l+1)-4, so Rcirc = -1
    gives P_factor = l(l+1)/2 - 1 for the Lichnerowicz contribution.
  * "magnetic" (vector TF): T = L_X g_A for a divergence-free vector field
    X (equiv. coexact 1-form), l >= 2, same rough eigenvalue.

Product Lichnerowicz eigenvalue for an AA mode with factor degree l_A and
other-factor scalar degree l_B:
    P = (l_A(l_A+1) + l_B(l_B+1))/2 - 1.

The chirality-odd receiver is R_odd(H) = (1/2)(H_{01,23} - H_{03,12} -
H_{12,03} + H_{23,01}).  For an AA mode with tensor indices in {0,1}:
  H_{03,12} = 0, H_{12,03} = 0, H_{23,01} = 0.
So R_odd = (1/2) H_{01,23} = (1/2)(d_2 d_3 phi_B)(0) * T_{01}(0).

For a BB mode with tensor indices in {2,3}:
  H_{01,23} = 0, H_{03,12} = 0, H_{12,03} = 0.
So R_odd = (1/2) H_{23,01} = (1/2)(d_0 d_1 phi_A)(0) * T_{23}(0).
By factor-exchange symmetry, BB contributes with the same structure as AA
with A<->B swapped.

This script:
  1. Verifies the sparse receiver selection for AA and BB modes.
  2. Builds the pole jet for trace-free tensors (electric and magnetic).
  3. Computes the heat-regularized adjacent Green transfer in the AA+BB sector.
  4. Checks for m=2 polarization structure and cancellation patterns.
"""
from __future__ import annotations

import json
import math
import pathlib
from typing import Literal

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


# ─── Receiver verification ────────────────────────────────────────────────
def verify_receiver_selection():
    """Check which H_{ij,pq} terms survive for AA vs BB modes."""
    results = {}
    # AA: tensor indices in {0,1}, scalar on B in {2,3}
    aa_terms = {
        "H_01_23": "d2 d3 phi_B * T_01(0)  -- CAN be nonzero",
        "H_03_12": "0 because h_{03}=0 for AA",
        "H_12_03": "0 because h_{12}=0 for AA",
        "H_23_01": "0 because h_{23}=0 for AA",
    }
    results["AA_receiver"] = {
        "formula": "R_odd = (1/2) H_{01,23} = (1/2)(d2 d3 phi_B)(0) * T_01(0)",
        "surviving_terms": aa_terms,
        "number_nonzero": 1,
    }
    # BB: tensor indices in {2,3}, scalar on A in {0,1}
    bb_terms = {
        "H_01_23": "0 because h_{01}=0 for BB",
        "H_03_12": "0 because h_{03}=0 for BB",
        "H_12_03": "0 because h_{12}=0 for BB",
        "H_23_01": "d0 d1 phi_A * T_23(0)  -- CAN be nonzero",
    }
    results["BB_receiver"] = {
        "formula": "R_odd = (1/2) H_{23,01} = (1/2)(d0 d1 phi_A)(0) * T_23(0)",
        "surviving_terms": bb_terms,
        "number_nonzero": 1,
    }
    return results


# ─── Trace-free tensor pole jets ──────────────────────────────────────────
def electric_tf_jet(ell: int, m_mode: str, node: str):
    """Electric (scalar TF Hessian) trace-free tensor at a pole of S^2.

    T = Hess f - (1/2)(Delta f) g in normal coords.  At a pole,
    (Hess f)_{ab} = d_a d_b f and Delta f = d_0^2 f + d_1^2 f.
    So T_{01} = d_0 d_1 f - 0 = d_0 d_1 f  (off-diagonal of Hess minus
    trace is just the off-diagonal).  And T_{00} = d_0^2 f - (1/2)(d_0^2 f + d_1^2 f).

    For the odd receiver we only need T_{01}(0) = (Hess f)_{01}(0).

    Scalar harmonic pole Hessians:
    m=0: Hess = -(lam/2) C0 * I  => off-diagonal = 0 => T_{01}=0
    m=2 cos: Hess = 2b * diag(1,-1) => off-diagonal = 0 => T_{01}=0
    m=2 sin: Hess = 2b * [[0,1],[1,0]] => T_{01} = 2b

    So electric T_{01}(0) is nonzero ONLY for m=2 sin modes.
    """
    lam = ell * (ell + 1)
    if m_mode == "m0":
        return 0.0  # T_01 = 0 for m=0 modes

    if ell < 2:
        return 0.0  # no TF modes for l<2

    # m=2 sin Hessian off-diagonal
    log_ratio = math.lgamma(ell + 3) - math.lgamma(ell - 1)
    A2 = math.exp(log_ratio) / 8.0
    Nl2 = math.sqrt((2 * ell + 1) / (4 * math.pi) *
                     math.exp(math.lgamma(ell - 1) - math.lgamma(ell + 3)))
    b = math.sqrt(2.0) * Nl2 * A2

    if m_mode == "s2":
        # Hess_{01} = 2b at N.  At S, sin(2phi) picks up -(-1)^l sign.
        sign = 1.0 if node == "N" else (-((-1.0) ** ell))
        return sign * 2 * b
    elif m_mode == "c2":
        # cos(2phi) Hessian is diagonal => off-diagonal = 0
        return 0.0
    return 0.0


def magnetic_tf_jet(ell: int, m_mode: str, node: str):
    """Magnetic (vector TF) trace-free tensor at a pole.

    T = L_X g = sym(nabla X) for a divergence-free vector field X on S^2.
    In normal coords at a pole, (L_X g)_{01} = d_0 X_1 + d_1 X_0.

    A coexact 1-form X = *df has components X_a = J_{ab} d_b f.
    Then d_c X_a = J_{ab} d_c d_b f.  So:
    (L_X g)_{01} = d_0 X_1 + d_1 X_0
                 = J_{1b} d_0 d_b f + J_{0b} d_1 d_b f
                 = (-d_0 d_0 f + d_1 d_1 f) + (-d_1 d_0 f + ... wait
    Let me be precise.  J = [[0,-1],[1,0]], so X_0 = -d_1 f, X_1 = d_0 f.
    d_0 X_1 = d_0 d_0 f,  d_1 X_0 = -d_1 d_1 f.
    (L_X g)_{01} = d_0^2 f - d_1^2 f.

    For m=0: Hess = -(lam/2) I, so d_0^2 f = d_1^2 f => T_{01} = 0.
    For m=2 cos: Hess = 2b diag(1,-1), d_0^2 f - d_1^2 f = 4b.
    For m=2 sin: Hess = 2b [[0,1],[1,0]], d_0^2 f - d_1^2 f = 0.
    """
    if ell < 2:
        return 0.0

    lam = ell * (ell + 1)
    log_ratio = math.lgamma(ell + 3) - math.lgamma(ell - 1)
    A2 = math.exp(log_ratio) / 8.0
    Nl2 = math.sqrt((2 * ell + 1) / (4 * math.pi) *
                     math.exp(math.lgamma(ell - 1) - math.lgamma(ell + 3)))
    b = math.sqrt(2.0) * Nl2 * A2

    if m_mode == "c2":
        # d_0^2 f - d_1^2 f = 4b
        sign = 1.0 if node == "N" else ((-1.0) ** ell)
        return sign * 4 * b
    elif m_mode == "s2":
        return 0.0
    elif m_mode == "m0":
        return 0.0
    return 0.0


def scalar_mixed_hessian(ell: int, m_mode: str, node: str):
    """Return d_0 d_1 phi(0) for a scalar harmonic on the other factor.

    The receiver for AA needs d_2 d_3 phi_B(0), and for BB needs d_0 d_1 phi_A(0).
    Both are the off-diagonal Hessian entry of a scalar at a pole.

    m=0: Hess = -(lam/2) I => off-diag = 0
    m=2 cos: diag => off-diag = 0
    m=2 sin: 2b => nonzero
    """
    if m_mode != "s2" or ell < 2:
        return 0.0

    lam = ell * (ell + 1)
    log_ratio = math.lgamma(ell + 3) - math.lgamma(ell - 1)
    A2 = math.exp(log_ratio) / 8.0
    Nl2 = math.sqrt((2 * ell + 1) / (4 * math.pi) *
                     math.exp(math.lgamma(ell - 1) - math.lgamma(ell + 3)))
    b = math.sqrt(2.0) * Nl2 * A2
    sign = 1.0 if node == "N" else (-((-1.0) ** ell))
    return sign * 2 * b


# ─── Receiver value for each sector mode ──────────────────────────────────
def receiver_aa(T01_at_pole, scalar_d2d3_at_pole):
    """R_odd for AA mode = (1/2) * scalar_d2d3 * T_01."""
    return 0.5 * scalar_d2d3_at_pole * T01_at_pole


def receiver_bb(T23_at_pole, scalar_d0d1_at_pole):
    """R_odd for BB mode = (1/2) * scalar_d0d1 * T_23."""
    return 0.5 * scalar_d0d1_at_pole * T23_at_pole


# ─── Quotient norms ───────────────────────────────────────────────────────
def tf_norm_sq(ell_factor: int, ell_other: int):
    """L2 norm squared of an AA or BB mode phi * T on quotient.

    ||T||^2 on S^2: for both electric and magnetic at degree l,
    ||T||^2 = 1 with L2-normalized scalar generating function.
    ||phi||^2 on S^2: 1 for L2-normalized scalar.
    Product: 1.  Quotient by Z_2: factor 2.
    So quotient norm^2 = 1/2.

    Actually we need to be more careful.  The L2-normalized TF tensor
    from a normalized scalar has ||T||^2 proportional to (l(l+1)-2)*(l(l+1))
    times ||f||^2.  Let me use the convention that gives a consistent
    normalization with the AB sector.

    For the AB sector, ||alpha_A sym beta_B||^2_quot = l_A(l_A+1)*l_B(l_B+1).
    The product normalization includes factors from the spherical harmonic
    norms.

    For TF tensors, the natural norm is determined by the rough Laplacian
    eigenvalue.  An electric TF tensor T = Hess f - (1/2)(Delta f)g has
    ||T||^2 = (1/2)l(l+1)(l(l+1)-2)||f||^2 on unit S^2.

    We'll keep track of the actual pole amplitudes and eigenvalues, and
    normalize consistently.
    """
    # This is a placeholder; the actual computation uses the explicit pole
    # jet values and their mode-by-mode structure.
    return 1.0  # placeholder


# ─── Heat-regularized spectral sum ────────────────────────────────────────
def compute_aabb_sector(Lmax: int, tau: float, pair: str):
    """Compute the AA+BB sector contribution to the odd adjacent Green transfer.

    For AA: receiver at NN needs T_{01}(0) from electric/magnetic tensor on A,
    and d_2 d_3 phi_B(0) from scalar on B.  Source at NS or SN involves the
    same harmonic evaluated at the adjacent pole.

    For BB: receiver at NN needs T_{23}(0) from tensor on B, and d_0 d_1 phi_A(0)
    from scalar on A.  Source at NS or SN is at adjacent pole.
    """
    recA_node = "N"  # receiver always at NN
    recB_node = "N"

    if pair == "NS":
        srcA_node, srcB_node = "N", "S"
    elif pair == "SN":
        srcA_node, srcB_node = "S", "N"
    elif pair == "SS":
        srcA_node, srcB_node = "S", "S"
    elif pair == "NN":
        srcA_node, srcB_node = "N", "N"
    else:
        raise ValueError(pair)

    total_aa = 0.0
    total_bb = 0.0
    details = []

    # For the receiver, only m=2 sin scalar and certain tensor types survive.
    # Electric: m=2 sin has T_{01} != 0 at pole
    # Magnetic: m=2 cos has T_{01} != 0 at pole (from the Lie derivative)

    for sector_label, tensor_jet_fn, scalar_jet_fn in [
        ("AA_electric", electric_tf_jet, scalar_mixed_hessian),
        ("AA_magnetic", magnetic_tf_jet, scalar_mixed_hessian),
    ]:
        # AA sector: tensor on A (degree l_A >= 2), scalar on B (degree l_B >= 2 for m=2)
        for l_A in range(2, Lmax + 1):
            lam_A = l_A * (l_A + 1)
            for l_B in range(2, Lmax + 1):
                lam_B = l_B * (l_B + 1)
                P_val = 0.5 * (lam_A + lam_B) - 1.0

                heat = math.exp(-tau * P_val)

                # Electric T: only s2 tensor mode has T_{01}!=0
                # Magnetic T: only c2 tensor mode has T_{01}!=0
                if "electric" in sector_label:
                    t_mode = "s2"
                else:
                    t_mode = "c2"

                # Scalar on B: only s2 has d_2 d_3 != 0
                s_mode = "s2"

                # Check m-parity for quotient descent:
                # tensor m=2 and scalar m=2 => m_A + m_B = 4, even => descends
                # (This is always even for our modes)

                # Receiver at NN
                T01_rec = tensor_jet_fn(l_A, t_mode, recA_node)
                dB_rec = scalar_mixed_hessian(l_B, s_mode, recB_node)
                R_rec = 0.5 * dB_rec * T01_rec

                if abs(R_rec) < 1e-20:
                    continue

                # Source at source node
                T01_src = tensor_jet_fn(l_A, t_mode, srcA_node)
                dB_src = scalar_mixed_hessian(l_B, s_mode, srcB_node)
                R_src = 0.5 * dB_src * T01_src

                if abs(R_src) < 1e-20:
                    continue

                # Norm: use the actual quadratic amplitudes.
                # For electric TF: ||T||^2 = (1/2)l(l+1)(l(l+1)-2) for unit-normalized f
                # For magnetic TF: same eigenvalue structure
                # Scalar on other factor: ||phi||^2 = 1
                # We need to normalize by the actual eigenmode norm on the quotient.
                # The natural object is R_rec * R_src / (P * ||mode||^2_quot).
                # ||mode||^2_{S^2 x S^2} = ||T||^2_{S^2_A} * ||phi||^2_{S^2_B}
                # Quotient halves: ||mode||^2_quot = ||mode||^2 / 2

                # STEP 94 CORRECTION: this is correct for electric tensors, but
                # the full-Lie magnetic tensor has four times this norm. Keeping
                # the common value below is the source of the superseded Step 93
                # divergence interpretation.
                tf_norm_A = 0.5 * lam_A * (lam_A - 2)
                scalar_norm_B = 1.0  # L2-normalized
                product_norm = tf_norm_A * scalar_norm_B
                quotient_norm = product_norm / 2.0  # Z_2 quotient

                if quotient_norm < 1e-20:
                    continue

                val = heat * R_rec * R_src / (P_val * quotient_norm)
                total_aa += val

                if l_A <= 4 and l_B <= 4:
                    details.append({
                        "sector": sector_label,
                        "l_A": l_A, "l_B": l_B,
                        "P": P_val,
                        "R_rec": R_rec, "R_src": R_src,
                        "quotient_norm": quotient_norm,
                        "contribution": val,
                    })

    # BB sector: tensor on B (indices {2,3}), scalar on A.
    # By A<->B exchange symmetry, the structure is identical with l_A<->l_B
    # roles for scalar and tensor, and the receiver picks up T_{23} * d_0 d_1 phi_A.
    # At the pole, T_{23} for a TF tensor on B is the same as T_{01} on A
    # in the local adapted frame.  The calculation is symmetric.
    for sector_label, tensor_jet_fn in [
        ("BB_electric", electric_tf_jet),
        ("BB_magnetic", magnetic_tf_jet),
    ]:
        for l_B_tensor in range(2, Lmax + 1):
            lam_B_t = l_B_tensor * (l_B_tensor + 1)
            for l_A_scalar in range(2, Lmax + 1):
                lam_A_s = l_A_scalar * (l_A_scalar + 1)
                P_val = 0.5 * (lam_A_s + lam_B_t) - 1.0

                heat = math.exp(-tau * P_val)

                if "electric" in sector_label:
                    t_mode = "s2"
                else:
                    t_mode = "c2"
                s_mode = "s2"

                # Receiver at NN: T_{23} at B-pole, d_0 d_1 phi at A-pole
                T23_rec = tensor_jet_fn(l_B_tensor, t_mode, recB_node)
                dA_rec = scalar_mixed_hessian(l_A_scalar, s_mode, recA_node)
                R_rec = 0.5 * dA_rec * T23_rec

                if abs(R_rec) < 1e-20:
                    continue

                # Source: adjust nodes for the pair
                if pair == "NS":
                    src_B_t_node, src_A_s_node = "S", "N"
                elif pair == "SN":
                    src_B_t_node, src_A_s_node = "N", "S"
                elif pair == "SS":
                    src_B_t_node, src_A_s_node = "S", "S"
                elif pair == "NN":
                    src_B_t_node, src_A_s_node = "N", "N"
                else:
                    raise ValueError(pair)

                T23_src = tensor_jet_fn(l_B_tensor, t_mode, src_B_t_node)
                dA_src = scalar_mixed_hessian(l_A_scalar, s_mode, src_A_s_node)
                R_src = 0.5 * dA_src * T23_src

                if abs(R_src) < 1e-20:
                    continue

                # STEP 94 CORRECTION: for full-Lie magnetic tensors this should
                # be 4 * 0.5 * lam_B_t * (lam_B_t - 2).
                tf_norm_B = 0.5 * lam_B_t * (lam_B_t - 2)
                scalar_norm_A = 1.0
                quotient_norm = tf_norm_B * scalar_norm_A / 2.0

                if quotient_norm < 1e-20:
                    continue

                val = heat * R_rec * R_src / (P_val * quotient_norm)
                total_bb += val

                if l_B_tensor <= 4 and l_A_scalar <= 4:
                    details.append({
                        "sector": sector_label,
                        "l_tensor": l_B_tensor, "l_scalar": l_A_scalar,
                        "P": P_val,
                        "R_rec": R_rec, "R_src": R_src,
                        "quotient_norm": quotient_norm,
                        "contribution": val,
                    })

    return {
        "pair": pair,
        "Lmax": Lmax,
        "tau": tau,
        "K_AA": total_aa,
        "K_BB": total_bb,
        "K_AABB_total": total_aa + total_bb,
        "low_degree_details": details[:30],
    }


# ─── Analytic structure analysis ──────────────────────────────────────────
def analyze_sign_structure():
    """Analyze the sign pattern of the AA/BB sector.

    For an adjacent pair NS (receiver NN, source NS):
    - Tensor on A at rec=N and src=N: same pole, so T01 sign is identical.
    - Scalar on B at rec=N and src=S: opposite poles.

    For electric s2 tensor on A:
        T01(N) = 2b_A,  T01(N) = 2b_A  [source A-pole doesn't change for NS]
    For scalar s2 on B:
        d23(N) = 2b_B,  d23(S) = -(-1)^{l_B} * 2b_B

    So the receiver-source product is:
        R_rec * R_src = (1/4) * (2b_A)^2 * (2b_B) * (-(-1)^{l_B} * 2b_B)
                      = (1/4) * 4b_A^2 * (-(-1)^{l_B}) * 4b_B^2
                      = -(-1)^{l_B} * 4 b_A^2 b_B^2

    For the SN pair (B stays, A changes poles):
        T01(N) * T01(S) for electric s2:
        At S, sign = -(-1)^{l_A} * 2b_A
        So T01_rec * T01_src = 2b_A * (-(-1)^{l_A}) * 2b_A = -(-1)^{l_A} * 4b_A^2
        Scalar B stays at N: d23(N)^2 = 4b_B^2

        R_rec * R_src = -(-1)^{l_A} * b_A^2 * b_B^2

    So NS pair sign: -(-1)^{l_B}
       SN pair sign: -(-1)^{l_A}

    For the magnetic c2 tensor on A:
        T01(N) = 4b_A for magnetic
        At S for c2: sign_c = (-1)^{l_A}
        So for SN pair: T01_rec * T01_src = 4b_A * (-1)^{l_A} * 4b_A = (-1)^{l_A} * 16 b_A^2
        For NS pair: A stays at N, so T01 is same => 16 b_A^2
        NS sign for magnetic: -(-1)^{l_B}  (same as electric, because B-scalar is unchanged)
        SN sign for magnetic: (-1)^{l_A} * (-1)  ???  wait, need to check

    Let me just compute this directly.
    """
    # Check a few specific cases
    cases = []
    for pair, sA, sB in [("NS", "N", "S"), ("SN", "S", "N")]:
        for l_A in [2, 3, 4]:
            for l_B in [2, 3, 4]:
                for sector, tfn in [("elec", electric_tf_jet), ("mag", magnetic_tf_jet)]:
                    t_mode = "s2" if sector == "elec" else "c2"
                    T_rec = tfn(l_A, t_mode, "N")
                    T_src = tfn(l_A, t_mode, sA)
                    d_rec = scalar_mixed_hessian(l_B, "s2", "N")
                    d_src = scalar_mixed_hessian(l_B, "s2", sB)
                    if abs(T_rec) < 1e-20 or abs(d_rec) < 1e-20:
                        continue
                    prod = (T_rec * d_rec) * (T_src * d_src)
                    sign = 1 if prod > 0 else -1
                    cases.append({
                        "pair": pair, "sector": sector,
                        "l_A": l_A, "l_B": l_B,
                        "sign_pattern": sign,
                        "product_value": prod,
                        "parity_check_lA": (-1)**l_A,
                        "parity_check_lB": (-1)**l_B,
                    })
    return cases


def main():
    # 1. Receiver verification
    recv_check = verify_receiver_selection()

    # 2. Sign structure analysis
    sign_cases = analyze_sign_structure()

    # 3. Heat-regularized spectral sums
    ladder_NS = []
    ladder_SN = []
    for tau, L in [(0.1, 60), (0.05, 80), (0.02, 120), (0.01, 180), (0.005, 280)]:
        ladder_NS.append(compute_aabb_sector(L, tau, "NS"))
        ladder_SN.append(compute_aabb_sector(L, tau, "SN"))

    # 4. Pair comparison at fixed tau
    class_tau = 0.01
    class_L = 200
    pair_comparison = {
        p: compute_aabb_sector(class_L, class_tau, p)
        for p in ["NS", "SN", "SS"]
    }

    results = {
        "step": 93,
        "scope": "AA/BB trace-free tensor sector analysis for product-orbifold chirality-odd Green coefficient",
        "receiver_verification": recv_check,
        "sign_structure_cases": sign_cases[:20],
        "adjacent_NS_ladder": [{k: v for k, v in r.items() if k != "low_degree_details"}
                                for r in ladder_NS],
        "adjacent_SN_ladder": [{k: v for k, v in r.items() if k != "low_degree_details"}
                                for r in ladder_SN],
        "pair_comparison_tau_0p01": {
            p: {k: v for k, v in d.items() if k != "low_degree_details"}
            for p, d in pair_comparison.items()
        },
        "low_degree_NS": ladder_NS[-1].get("low_degree_details", [])[:15] if ladder_NS else [],
        "interpretation": [
            "AA/BB trace-free tensor sectors DO enter the odd receiver, through a single surviving term.",
            "For AA: only H_{01,23} is nonzero, requiring both T_{01}!=0 (tensor factor) and d2d3 phi!=0 (scalar factor).",
            "Both electric and magnetic TF modes contribute, but with different m-type selection: electric via s2, magnetic via c2.",
            "The l-parity alternating sign comes from the scalar harmonic evaluated at the antipodal pole.",
            "This is still in the Step89/91 principal normalization and is not the full Ozuch coefficient.",
        ],
    }

    outpath = DATA_DIR / "step93_aabb_tensor_sector_analysis.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(json.dumps(results, indent=2, default=str))
    print(f"Wrote {outpath}")


if __name__ == "__main__":
    main()
