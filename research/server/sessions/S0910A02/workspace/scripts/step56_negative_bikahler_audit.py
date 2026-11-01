#!/usr/bin/env python3
"""
Step 56 audit ledger for the negative bi-Kähler mixed A1 wall.

This records finite arithmetic and route-control consequences.  It is not a
proof of Einstein nonexistence or of the full Yau--26 proposition.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "workspace" / "data"
DATA.mkdir(parents=True, exist_ok=True)

CHI = 56
NODES = 36
TAU0 = -36
B2 = CHI - 2


def row(r: int) -> dict:
    tau = TAU0 + 2*r
    bplus = (B2 + tau)//2
    bminus = (B2 - tau)//2
    c1sq_orig = 2*CHI + 3*tau
    c1sq_rev = 2*CHI - 3*tau
    noether_sum_orig = c1sq_orig + CHI  # c1^2+c2 = 3(chi+tau)
    noether_sum_rev = c1sq_rev + CHI
    chi_h_orig = (CHI + tau)/4
    chi_h_rev = (CHI - tau)/4
    noether_integral_orig = (noether_sum_orig % 12 == 0)
    noether_integral_rev = (noether_sum_rev % 12 == 0)
    bmy_orig = c1sq_orig >= 0 and c1sq_orig <= 9*chi_h_orig
    bmy_rev = c1sq_rev >= 0 and c1sq_rev <= 9*chi_h_rev
    return {
        "r_reversed_nodes": r,
        "orientation_partner_36_minus_r": NODES-r,
        "representative_after_orientation_symmetry": min(r, NODES-r),
        "chi": CHI,
        "tau": tau,
        "b_plus": bplus,
        "b_minus": bminus,
        "strict_Hitchin_Thorpe": 2*CHI > 3*abs(tau),
        "HT_margin_2chi_minus_3abstau": 2*CHI - 3*abs(tau),
        "contains_plus2_sphere_in_original_orientation": r > 0,
        "contains_plus2_sphere_in_reverse_orientation": r < NODES,
        "plus2_spheres_both_orientations": 0 < r < NODES,
        "ordinary_simple_type_SW_basic_classes_killed_both_orientations_if_source_hypotheses": (0 < r < NODES and bplus > 1 and bminus > 1),
        "c1sq_original_orientation_2chi_plus_3tau": c1sq_orig,
        "chi_h_original_orientation": chi_h_orig,
        "noether_c1sq_plus_c2_original": noether_sum_orig,
        "noether_integrality_original": noether_integral_orig,
        "BMY_numerically_possible_original": bmy_orig if noether_integral_orig else False,
        "c1sq_reverse_orientation_2chi_minus_3tau": c1sq_rev,
        "chi_h_reverse_orientation": chi_h_rev,
        "noether_c1sq_plus_c2_reverse": noether_sum_rev,
        "noether_integrality_reverse": noether_integral_rev,
        "BMY_numerically_possible_reverse": bmy_rev if noether_integral_rev else False,
        "complex_structure_excluded_by_noether_both_orientations": (not noether_integral_orig and not noether_integral_rev),
    }

rows = [row(r) for r in range(NODES+1)]

result = {
    "model": {
        "orbifold": "O=(Sigma_2 x Sigma_2)/<iota x iota>, with both curves hyperbolic and iota hyperelliptic",
        "nodes": NODES,
        "curvature_blocks": "R_+=R_-=diag(-1,0,0); each block has a 2-dimensional kernel for Ozuch/Biquard A1 vector obstruction",
        "construction_half": "For any fixed node orientation pattern S, choose each zeta in the appropriate kernel R_+ or R_-; Step 49/50 refined EH estimate gives ||Ric+g||_op -> 0 on the filled smooth manifold, conditional only on the explicit gluing-estimate package, not on the unproved general H4-dual necessity theorem.",
    },
    "orientation_reversing_symmetry": {
        "source_geometry": "If Sigma_2 is realized over R, complex conjugation c is orientation-reversing and commutes with the hyperelliptic involution; c x id descends to an orientation-reversing orbifold diffeomorphism.",
        "pattern_statement": "For a subset S of reversed nodes, orientation reversal sends the filled manifold to the pattern whose reversed set is the complement of c(S). Consequently the count r is paired with 36-r; row arithmetic depends only on r, but smooth type may still depend on the subset S.",
        "count_reduction": "Up to orientation and node permutation, only representatives r=0,...,18 need be considered at the row-arithmetic level.",
        "endpoint_einstein": "M_0 is the holomorphic/smoothable double-cover row; M_36 is orientation-reverse to M_0 and therefore carries the same Einstein metric as an unoriented smooth manifold.",
    },
    "double_cover_and_pi1": {
        "M0_double_cover": "M_0 is identified with the smooth double cover of P1 x P1 branched over a smoothed bidegree (6,6) curve; K=pi^*O(1,1), K^2=4, chi=56, tau=-36, and Aubin-Yau gives Ric<0 KE.",
        "simple_connectivity_support": "Catanese-type proposition in the local source: a cyclic cover of simply connected Y branched along a smooth flexible divisor is simply connected. A smooth (6,6) divisor on P1 x P1 is connected/flexible in the intended construction.",
        "same_pi1_for_all_sign_patterns_argument": "All A1 fillings, with Euler +/-2 disk bundles over S^2, are simply connected and have boundary RP3; the boundary pi1=Z/2 maps trivially into either filling. Van Kampen therefore quotients the same boundary images independent of the sign. Since the all-compatible filling M0 is simply connected, every sign-pattern filling should have trivial pi1. This is a proof sketch needing a clean topology write-up, but it is much stronger than the previous rational-b1-only ledger.",
        "simplicial_volume_consequence": "If the preceding pi1 argument is accepted, every mixed row has amenable/trivial fundamental group, hence zero simplicial volume. Gromov-norm/Sambusetti-type obstructions depending on nonzero simplicial volume cannot obstruct these rows.",
    },
    "rows": rows,
    "summary_counts": {
        "live_count_representatives_after_orientation": list(range(1,19)),
        "odd_rows_no_complex_structure_either_orientation": [r for r in range(1,36,2) if rows[r]["complex_structure_excluded_by_noether_both_orientations"]],
        "even_live_rows_complex_numerically_possible_original_orientation": [r for r in range(2,19,2) if rows[r]["BMY_numerically_possible_original"]],
        "even_live_rows_complex_numerically_possible_reverse_orientation": [r for r in range(2,19,2) if rows[r]["BMY_numerically_possible_reverse"]],
        "rows_with_plus2_spheres_both_orientations": [r for r in range(1,36)],
    },
    "obstruction_status": {
        "ordinary_SW_LeBrun": "For 1<=r<=35, +2 spheres occur in both orientations; under b_+>1, simple type, non-torsion hypotheses, the adjunction inequality kills ordinary numerical SW basic classes in both orientations. This blocks the standard LeBrun/Ishida-LeBrun mechanism, but it is not a theorem about every monopole or Bauer-Furuta class.",
        "Bauer_Furuta": "Still a live source question: Kotschick records that Bauer-Furuta stable cohomotopy detects generic monopole classes of positive formal dimension and can survive connected sums. The present sources do not prove that a +2 sphere kills all such classes.",
        "Gromov_norm": "For this specific product-quotient family, the route appears closed if the pi1 sketch is made rigorous: simply connected/amenable pi1 implies simplicial volume zero. A Sambusetti/BCG inequality could matter only for a different mixed-row construction with nonamenable/rationally essential fundamental group or for an obstruction not requiring nonzero simplicial volume.",
        "not_a_refutation": "No row is known to lack Einstein metrics. Odd rows are outside complex-surface existence machines by Noether parity, but topology alone plus strict Hitchin-Thorpe and SW-dead status is only a hardness wall, not a no-Einstein theorem.",
    },
}

out = DATA / "step56_negative_bikahler_audit.json"
out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({
    "status": "ok",
    "output": str(out.relative_to(ROOT)),
    "live_representatives": result["summary_counts"]["live_count_representatives_after_orientation"],
    "odd_no_complex": result["summary_counts"]["odd_rows_no_complex_structure_either_orientation"],
    "sample_rows": [rows[i] for i in [0,1,2,9,10,18,36]],
    "gromov_norm_status": result["obstruction_status"]["Gromov_norm"],
}, indent=2))
