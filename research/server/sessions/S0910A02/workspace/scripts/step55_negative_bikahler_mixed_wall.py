#!/usr/bin/env python3
"""
Step 55 finite ledger for the negative bi-Kähler product-quotient wall.

This script records arithmetic/topological checks; it does not prove a gluing
or Einstein nonexistence theorem.

Model:
  P = Sigma_2 x Sigma_2 with both factors carrying curvature -1.
  tau = (hyperelliptic involution, hyperelliptic involution).
  O = P/<tau> is a negative Einstein orbifold with 36 A1 points.
  Replacing an A1 point by an Eguchi-Hanson/A1 disk bundle in the compatible
  orientation contributes a (-2)-sphere; replacing it in the reversed orientation
  contributes a (+2)-sphere relative to the global orientation.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "workspace" / "data"
DATA.mkdir(parents=True, exist_ok=True)


def product_curve_invariants(g1: int = 2, g2: int = 2) -> dict:
    chi1 = 2 - 2 * g1
    chi2 = 2 - 2 * g2
    chi_prod = chi1 * chi2
    signature_prod = 0
    # For a product of curves, K^2 = 8(g1-1)(g2-1).
    K2_prod = 8 * (g1 - 1) * (g2 - 1)
    fixed_each = 2 * g1 + 2  # for genus 2 this is 6; keep formula only in equal genus case
    if g1 != g2:
        fixed_total = (2 * g1 + 2) * (2 * g2 + 2)
    else:
        fixed_total = fixed_each * fixed_each
    return {
        "genera": [g1, g2],
        "chi_factors": [chi1, chi2],
        "chi_product": chi_prod,
        "signature_product": signature_prod,
        "K2_product": K2_prod,
        "hyperelliptic_fixed_points_each_factor": [2 * g1 + 2, 2 * g2 + 2],
        "fixed_points_product_action": fixed_total,
    }


def quotient_and_resolution_rows(num_nodes: int = 36) -> dict:
    # Burnside topological Euler characteristic of the underlying quotient |P/tau|.
    chi_prod = 4
    chi_underlying_quotient = (chi_prod + num_nodes) // 2
    # Satake/orbifold Euler for a global quotient in CGB is chi(P)/|G|.
    chi_orbifold_satake = chi_prod / 2
    # Replacing a cone neighbourhood of each isolated quotient point (Euler 1)
    # by an A1 disk bundle over S^2 (Euler 2) increases chi by 1 per node.
    chi_smooth = chi_underlying_quotient + num_nodes
    b1_rational = 0  # H^1(P;Q)^tau=0 because hyperelliptic involution acts by -1 on H^1 of each factor.
    b2_smooth = chi_smooth - 2 + 2 * b1_rational
    # K^2 of quotient canonical model: K_P^2 / 2 because the action is free in codimension one.
    K2_orbifold = 4
    # All-compatible crepant resolution has 2 chi + 3 tau = K^2.
    tau_all_compatible = (K2_orbifold - 2 * chi_smooth) // 3
    assert tau_all_compatible == -36

    rows = []
    for r in range(num_nodes + 1):
        tau = tau_all_compatible + 2 * r
        bplus = (b2_smooth + tau) // 2
        bminus = (b2_smooth - tau) // 2
        ht_left = 2 * chi_smooth
        ht_right = 3 * abs(tau)
        rows.append({
            "reversed_nodes_r": r,
            "chi": chi_smooth,
            "tau": tau,
            "b1_rational_assumption": b1_rational,
            "b2_rational": b2_smooth,
            "b_plus_rational": bplus,
            "b_minus_rational": bminus,
            "strict_Hitchin_Thorpe": ht_left > ht_right,
            "HT_margin_2chi_minus_3abstau": ht_left - ht_right,
            "contains_plus_2_sphere_if_r_positive": r > 0,
            "ordinary_SW_simple_type_killed_by_plus_2_sphere_if_r_positive": r > 0,
        })
    return {
        "underlying_quotient_chi_Burnside": chi_underlying_quotient,
        "orbifold_chi_Satake_for_CGB": chi_orbifold_satake,
        "num_A1_nodes": num_nodes,
        "smooth_resolution_chi_any_orientation_assignment": chi_smooth,
        "rational_b1_reason": "H^1(Sigma_2 x Sigma_2;Q)^tau=0 since the hyperelliptic involution acts as -1 on H^1 of each factor; isolated A1 fillings do not add rational H1.",
        "smooth_resolution_b2_rational": b2_smooth,
        "K2_orbifold_all_compatible_crepant": K2_orbifold,
        "tau_all_compatible_from_2chi_plus_3tau_equals_K2": tau_all_compatible,
        "row_formula": "chi=56, tau=-36+2r, b_+=9+r, b_-=45-r for r reversed A1 fillings, assuming b1(Q)=0 rationally.",
        "rows": rows,
    }


def double_cover_smoothing_record() -> dict:
    # The diagonal quotient (C x C)/<(iota,iota)> maps 2-to-1 to
    # (C/iota) x (C/iota)=P1 x P1.  The branch divisor is the union of
    # the six vertical and six horizontal branch fibres, of total bidegree (6,6).
    # Smoothing inside |O(6,6)| gives a smooth branch curve B of genus
    # (6-1)(6-1)=25.  For a double cover pi:S->P1xP1 branched over B,
    # K_S=pi^*(K_Y + B/2)=pi^*O(1,1), K^2=2*(1,1)^2=4,
    # e(S)=2e(Y)-e(B)=8-(2-2*25)=56.
    genus_branch = (6 - 1) * (6 - 1)
    e_base = 4
    e_branch = 2 - 2 * genus_branch
    e_smooth = 2 * e_base - e_branch
    K2 = 2 * 2
    tau = (K2 - 2 * e_smooth) // 3
    return {
        "map": "(Sigma_2 x Sigma_2)/<iota x iota> is a double cover of P1 x P1",
        "branch_divisor_singular": "six vertical fibres plus six horizontal fibres, total bidegree (6,6), with 36 normal-crossing points",
        "local_nodes": "At each crossing the double cover has local equation z^2=xy, i.e. an A1 singularity.",
        "smoothing": "Smoothing the branch divisor inside the base-point-free |O(6,6)| gives a smooth double cover diffeomorphic to the minimal resolution by the cyclic-cover/HKK local theorem.",
        "smooth_branch_genus": genus_branch,
        "smooth_double_cover_chi": e_smooth,
        "smooth_double_cover_K2": K2,
        "smooth_double_cover_tau": tau,
        "canonical_bundle": "K=pi^*O(1,1), ample for the smooth cover; Aubin-Yau gives a negative Kähler-Einstein metric.",
        "consequence": "The all-compatible holomorphic A1 row is smooth-category harmless: its minimal resolution is diffeomorphic to an ample-canonical smooth surface carrying Ric<0 KE.",
    }


def curvature_block_record(lambda_einstein: int = -1) -> dict:
    return {
        "metric": "product of two equal-curvature hyperbolic genus-2 surfaces, each with sectional curvature -1",
        "Einstein_constant_Lambda": lambda_einstein,
        "curvature_operator_nonzero_entries": "K(e12)=K(e34)=Lambda, mixed planes zero",
        "R_plus_eigenvalues": [lambda_einstein, 0, 0],
        "R_minus_eigenvalues": [lambda_einstein, 0, 0],
        "kernel_dimension_each_block": 2,
        "vector_obstruction_status": "For either chirality, Ozuch/Biquard first obstruction R_±(p) zeta=0 is killed by choosing zeta in the 2-dimensional kernel, not by arbitrary zeta.",
    }


def adjunction_scope_record() -> dict:
    return {
        "source_supported_statement": "For a compact oriented smooth 4-manifold of simple type with b_+>1 and nonzero numerical SW invariant, the adjunction inequality for a positive-genus surface gives |<c(s),[S]>|+[S]^2 <= 2g-2. If a non-torsion class is represented by a sphere, add a handle to get a genus-1 representative of the same class; hence |<c,[S]>|+[S]^2 <= 0, so [S]^2>0 is impossible for any nonzero numerical SW basic class.",
        "application_to_reversed_A1": "A reversed A1/EH filling contributes an embedded sphere of square +2. If its class is non-torsion and b_+>1, ordinary simple-type numerical SW invariants vanish. This blocks the SW input used by standard LeBrun/Ishida-LeBrun nonexistence theorems.",
        "not_fully_source_closed_here": "The stronger slogan 'all monopole classes vanish' was not fully source-closed in this step. Kotschick/Kronheimer sources cover monopole classes and positive-genus/trivial-normal adjunction plus generic/non-torsion PSC obstructions, but the exact +2-sphere vanishing theorem for all monopole/Bauer-Furuta classes should be checked before using it as a theorem.",
        "zero_or_torsion_caveat": "The zero class can be a monopole class on spin manifolds and is not an Einstein obstruction by itself; LeBrun estimates need nonzero/generic classes with positive projection.",
    }


result = {
    "product_curve_orbifold": product_curve_invariants(),
    "quotient_resolution_rows": quotient_and_resolution_rows(),
    "double_cover_smoothing": double_cover_smoothing_record(),
    "curvature_blocks": curvature_block_record(),
    "adjunction_and_SW_scope": adjunction_scope_record(),
    "yau26_interpretation": {
        "reduction_shape": "For each actual mixed row with r>=1 reversed fillings, the Step-49/50 sign-agnostic refined EH estimate plus R_- kernel degeneracy gives metrics with ||Ric+g||_op -> 0 on the resulting smooth 4-manifold. If P4^- holds, each such smooth manifold must carry some Einstein metric.",
        "not_refutation": "No smooth no-Einstein theorem for these mixed rows is proved. Hitchin-Thorpe is strict for every r, ordinary SW/LeBrun obstructions are threatened or killed by +2 spheres, and all-compatible holomorphic/ADE cases may be harmless by smoothing/Aubin-Yau.",
        "necessity_gap": "The explicit construction side is stronger than the general compactness necessity side: H4-dual transfer from arbitrary C0 Ricci-pinched degeneration to R_± zeta=0 remains unproved.",
    },
}

out = DATA / "step55_negative_bikahler_mixed_wall.json"
out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({
    "status": "ok",
    "output": str(out.relative_to(ROOT)),
    "nodes": result["product_curve_orbifold"]["fixed_points_product_action"],
    "row_formula": result["quotient_resolution_rows"]["row_formula"],
    "sample_rows": [result["quotient_resolution_rows"]["rows"][i] for i in [0, 1, 18, 36]],
    "R_plus": result["curvature_blocks"]["R_plus_eigenvalues"],
    "R_minus": result["curvature_blocks"]["R_minus_eigenvalues"],
}, indent=2))
