#!/usr/bin/env python3
"""
Step 58 ledger for Yau 26.

This is an Explore/Actuator calculation-and-source ledger, not a proof of Yau 26.
It records three route-changing checks:

1. Biquard arXiv 1105.4904 Section 4, Lemmas 4.1--4.2 give a *raw Ricci*
   approximate-Einstein estimate for Eguchi--Hanson insertion.  After killing
   the first obstruction, the unweighted g_t-operator Ricci defect tends to 0;
   if the first obstruction is not killed, it remains O(1) on the core.

2. Cheeger--Tian epsilon regularity is an Einstein theorem.  The Step-11
   opposite-warping spike gives an explicit C^0-Ricci-pinched non-Einstein
   family with small local L^2 curvature but unbounded pointwise curvature,
   so no collapse-tolerant pointwise epsilon-regularity analogue can be used
   under the Yau-26 input hypothesis.

3. Pure Chern--Weil identities still survive collapse: if Vol -> 0 and
   ||Ric - sigma g||_op -> 0 in dimension four, then both chiral Weyl energies
   are pinned to 2*pi^2*(2 chi +/- 3 tau) up to o(1).  This explains why
   counting arguments do not break the toric/rod adversary; an obstruction
   must find a forced energy defect in limits/transitions, not a missing budget.
"""
from __future__ import annotations

import json
import math
import os
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parents[3]  # .../Sessions/S0910A02 -> user root? wait: script=.../workspace/scripts, parents[2]=S0910A02
SESSION = Path(__file__).resolve().parents[2]
DATA = SESSION / "workspace" / "data"
DATA.mkdir(parents=True, exist_ok=True)


def tpow(t: float, exponent: float) -> float:
    return t ** exponent


def biquard_bounds(t: float, C: float = 1.0) -> dict:
    """Return the Section-4 scaling bounds at core and transition."""
    rho_core = 1.0
    rho_transition = t ** (-0.25)
    # Biquard Lemma 4.2, k=0: |Ric - Lambda g_t - t sum lambda chi o|_eh <= C t^2 rho^2.
    # On EH region g_t ~ t eh, so a (0,2) tensor gives operator size t^{-1} times eh size.
    return {
        "t": t,
        "rho_core": rho_core,
        "rho_transition": rho_transition,
        "raw_eh_remainder_core": C * t**2 * rho_core**2,
        "op_remainder_core": C * t * rho_core**2,
        "raw_eh_remainder_transition": C * t**2 * rho_transition**2,
        "op_remainder_transition": C * t * rho_transition**2,
        "worst_op_remainder": C * math.sqrt(t),
        "naive_remark_4_3_raw_eh": C * t,
        "naive_remark_4_3_op_size": C,
        "nonzero_first_obstruction_op_core_order": "|lambda| * |o|_eh = O(1) on the EH core",
        "killed_first_obstruction_op_order": "O(t^{1/2}) worst, O(t) on core",
        "higher_q_obstruction_op_core": {
            "q=2": t,
            "q=3/2": math.sqrt(t),
            "formula": "a residual term t^q o has core operator size t^(q-1)"
        }
    }


def curvature_block_lambda(block_diag, zeta):
    # The precise universal constant in Biquard/Ozuch lambda_i is irrelevant for
    # zero/nonzero.  This computes the vector R zeta.
    return [block_diag[i] * zeta[i] for i in range(3)]


def mixed_pattern_check(name: str, nodes: int, reversed_count: int, Lambda: float) -> dict:
    """Minimal algebraic check for a genuinely mixed compatible/reversed pattern."""
    R_plus = [Lambda, 0.0, 0.0]
    R_minus = [Lambda, 0.0, 0.0]
    # choose zeta in kernel, e2; bad zeta e1 shows what would fail
    zeta_good = [0.0, 1.0, 0.0]
    zeta_bad = [1.0, 0.0, 0.0]
    compatible = nodes - reversed_count
    rows = []
    for chirality, count, block in [
        ("compatible/tests R_plus", compatible, R_plus),
        ("reversed/tests R_minus", reversed_count, R_minus),
    ]:
        if count <= 0:
            continue
        rows.append({
            "chirality": chirality,
            "count": count,
            "R_block_diag": block,
            "zeta_good": zeta_good,
            "R_zeta_good": curvature_block_lambda(block, zeta_good),
            "good_first_obstruction_killed": curvature_block_lambda(block, zeta_good) == [0.0, 0.0, 0.0],
            "zeta_bad": zeta_bad,
            "R_zeta_bad": curvature_block_lambda(block, zeta_bad),
            "bad_first_obstruction_nonzero": curvature_block_lambda(block, zeta_bad) != [0.0, 0.0, 0.0],
        })
    return {
        "name": name,
        "nodes": nodes,
        "reversed_count": reversed_count,
        "compatible_count": compatible,
        "is_genuinely_mixed": 0 < reversed_count < nodes,
        "R_plus_diag": R_plus,
        "R_minus_diag": R_minus,
        "node_rows": rows,
        "operator_norm_consequence": (
            "Because each active block has a 2D kernel and zeta is chosen in it, "
            "all first obstruction coefficients lambda_i vanish at every node. "
            "Biquard Lemma 4.2 then gives a complete raw Ricci residual with "
            "sup_g_t operator size O(t^{1/2}) for this finite disjoint pattern."
        ),
        "global_inverse_not_used": (
            "No Einstein-modulo-obstruction solve, transversality, AH boundary, or "
            "small-eigenvalue estimate is needed for this near-pinched input metric; "
            "those enter only if one tries to perturb to an exact Einstein metric."
        )
    }


def cgb_chiral_pinning(chi: int, tau: int, volume: float, delta: float, sigma: int = 1) -> dict:
    """Compute topological target chiral Weyl energies and a crude B-term bound."""
    # CGB: A+ + A- + B = 8 pi^2 chi, B=int(s^2/24-|E|^2/2)
    # signature: A+ - A- = 12 pi^2 tau.
    Aplus_top = 2 * math.pi**2 * (2 * chi + 3 * tau)
    Aminus_top = 2 * math.pi**2 * (2 * chi - 3 * tau)
    # If Ric eigenvalues are sigma + a_i, |a_i|<=delta, n=4:
    # |s| <= 4 + 4 delta. |E|^2 <= 16 delta^2 is a deliberately crude pointwise bound.
    B_abs_bound = ((4 + 4 * delta) ** 2 / 24 + 0.5 * 16 * delta**2) * volume
    B_einstein_limit = (2.0/3.0) * volume  # when delta=0, |E|=0, s=4sigma
    return {
        "chi": chi,
        "tau": tau,
        "volume": volume,
        "delta": delta,
        "Aplus_topological_limit": Aplus_top,
        "Aminus_topological_limit": Aminus_top,
        "A_total_topological_limit": Aplus_top + Aminus_top,
        "B_abs_bound_for_error_in_each_chiral_energy": 0.5 * B_abs_bound,
        "B_einstein_term_half": 0.5 * B_einstein_limit,
        "identity": "int|W^±|^2 = 2*pi^2*(2 chi ± 3 tau) - 1/2*int(s^2/24 - |E|^2/2)",
        "collapse_limit": "if volume->0 and delta remains bounded (in particular delta->0), the last term is o(1)"
    }


def connected_sum_s2xs2(k: int) -> dict:
    chi = 2*k + 2
    tau = 0
    pin = cgb_chiral_pinning(chi, tau, volume=0.0, delta=0.0)
    rods = 2*k + 2
    rod_energy_each = 8 * math.pi**2
    return {
        "k": k,
        "manifold": "#_k(S^2 x S^2)",
        "chi": chi,
        "tau": tau,
        "chiral_energy_each_limit": pin["Aplus_topological_limit"],
        "total_weyl_energy_limit": pin["A_total_topological_limit"],
        "rod_count_model": rods,
        "rod_energy_each_model": rod_energy_each,
        "rod_total_model": rods * rod_energy_each,
        "rod_budget_matches_total": abs(rods * rod_energy_each - pin["A_total_topological_limit"]) < 1e-8,
        "interpretation": "rod counting saturates CGB exactly; no contradiction without proving an energy defect"
    }


def fit_step11_exponents() -> dict:
    path = DATA / "step11_cz_hessian_spike.json"
    if not path.exists():
        return {"available": False, "path": str(path)}
    d = json.load(open(path))
    cases = [c for c in d["family"] if c["Lambda"] >= 10 and not math.isnan(c.get("L2_hess_sq", float('nan')))]
    def slope(key):
        xs, ys = [], []
        for c in cases:
            val = c[key]
            if val > 0 and math.isfinite(val):
                xs.append(math.log(c["Lambda"]))
                ys.append(math.log(val))
        if len(xs) < 2:
            return None
        xm, ym = mean(xs), mean(ys)
        return sum((x-xm)*(y-ym) for x,y in zip(xs,ys)) / sum((x-xm)**2 for x in xs)
    return {
        "available": True,
        "path": str(path),
        "theoretical_rates": {
            "ricci_defect": "O(Lambda^{-2/3})",
            "center_curvature": "Omega(Lambda^{1/3})",
            "local_added_L2_curvature": "O(Lambda^{-4/3}) at the Hessian-energy level"
        },
        "empirical_loglog_slopes_from_saved_data": {
            "sup_delta_inner": slope("sup_delta_inner"),
            "Rm_center_lower_bound": slope("Rm_center_lower_bound"),
            "L2_hess_sq": slope("L2_hess_sq"),
        },
        "largest_case": max(d["family"], key=lambda c: c["Lambda"]),
        "regularity_conclusion": (
            "This fixed-manifold sequence has ||Ric-g||_op -> 0 and local L2 curvature -> 0 "
            "but |Rm|(center)->infinity; it falsifies a Cheeger-Tian-style pointwise epsilon "
            "regularity theorem under C0 Ricci pinching, while not affecting the exact Einstein theorem."
        )
    }


sample_ts = [1e-1, 1e-2, 1e-4, 1e-8]
result = {
    "source_anchors": {
        "Biquard_pdf": "Sessions/S0910A02/workspace/data/source_text/biquard_1105_4904.pdf",
        "Biquard_text": "Sessions/S0910A02/workspace/data/source_text/biquard_1105_4904_pdftotext.txt",
        "Biquard_title": "O. Biquard, Désingularisation de métriques d'Einstein. I, arXiv:1105.4904 / Invent. Math. 192 (2013), 197-252",
        "Biquard_relevant_lines": {
            "theorem_0_1_AH_multi_singularities": "pdftotext lines 96-112: AH nondegenerate theorem, simultaneous/subset desingularization",
            "orientation_reversal": "lines 146-153: det R^- handled by opposite-orientation Eguchi-Hanson; kernel line in O(4)/U(2)",
            "local_approx_metric_scope": "lines 1264-1269: Section 4 constructs approximate Einstein metrics modulo EH obstructions, compact or noncompact up to Section 8",
            "lemma_4_1": "lines 1331-1358: on EH_t, |nabla^k(Ric_{eh+th}-t Lambda h_t - t sum lambda o)|_eh <= c_k t^2 rho^{2-k}",
            "matching_cutoff": "lines 1361-1399: beta=1/4 transition, chi_t with derivatives O(t^{k/4}), gluing g_t",
            "lemma_4_2": "lines 1408-1429: raw glued metric estimate |nabla^k(Ric_{g_t}-Lambda g_t - t sum lambda chi_t o)|_eh <= c_k t^2 rho^{2-k}",
            "naive_metric_warning": "lines 1430-1453: simple gluing only gives O(t) in eh norm, i.e. O(1) in g_t operator size"
        },
        "Cheeger_Tian_status": "Original JAMS PDF download failed (AMS 403; several public guesses 404/SSL). Exact theorem statement read from Ge-Jiang 2017 source lines 29-36, not the original paper.",
        "Cheeger_Tian_secondary_statement": "There exist universal epsilon,C: if (M,g,p) is Einstein 4D, Ric=lambda g, |lambda|<=3, and int_{B_r(p)} |Rm|^2 <= epsilon for r<=1, then sup_{B_{r/2}} |Rm| <= C r^{-2}, with no volume assumption.",
        "Step11_spike": "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md and data/step11_cz_hessian_spike.json"
    },
    "biquard_operator_norm_scaling": [biquard_bounds(t) for t in sample_ts],
    "minimal_mixed_patterns": [
        mixed_pattern_check("positive mirror (S^2 x S^2)/Z2, r=1 of 4 reversed", 4, 1, +1.0),
        mixed_pattern_check("negative mirror (Sigma_2 x Sigma_2)/<iota x iota>, r=1 of 36 reversed", 36, 1, -1.0),
    ],
    "cheeger_tian_vs_c0_ricci": fit_step11_exponents(),
    "chern_weil_chiral_pinning": {
        "formula": "A_± := int|W^±|^2 = 2*pi^2*(2 chi ± 3 tau) - 1/2*int(s^2/24 - |E|^2/2)",
        "near_einstein_collapse": "If ||Ric-sigma g||_op -> 0 and Vol -> 0, then the integral term tends to 0; both chiral energies are topologically pinned with no slack.",
        "examples": [connected_sum_s2xs2(k) for k in [1, 2, 3, 10, 50]],
        "sample_error_bound": cgb_chiral_pinning(chi=22, tau=0, volume=1e-3, delta=1e-2)
    },
    "route_consequences": {
        "mixed_wall_conditional_repaired": (
            "For the purpose of producing Yau-26 input metrics, Biquard Section 4 Lemma 4.2 is enough: "
            "once the first vector obstruction is killed at every selected A1 node, the complete unprojected Ricci defect of the glued approximate metric is small in g_t operator norm. "
            "The earlier phrase 'Biquard Section 14' was wrong for this estimate; Section 14 is transversality in the arXiv version."
        ),
        "conditionality_remaining": (
            "The estimate directly covers the local/refined approximate metric. It does not prove that the smooth mixed fillings have no far-away Einstein metric, and it does not provide H4-dual necessity for arbitrary C0-Ricci-pinched degenerations."
        ),
        "positive_collapse_reframing": (
            "Do not test almost-Killing production on symmetric exact Killing examples. The useful task is adversarial: try to globalize twist-spike/local-jet mechanisms into closed collapsing near-pinched families, or identify the obstruction that prevents this."
        ),
        "regularity_ceiling": (
            "Cheeger-Tian is the right Einstein collapse-tolerant epsilon regularity theorem, but Step 11 structurally falsifies its C0-Ricci-pinched pointwise analogue: the missing term is uncontrolled second derivatives of Ricci/metric in the trace-free Hessian channel."
        ),
        "energy_defect_target": (
            "Since Chern-Weil pins both chiral Weyl energies in collapsed tight pinching, counting cannot refute toric/rod collapse. A positive-collapse obstruction must prove forced loss/defect of energy to lower-dimensional limits, transition regions, or nonmaximal nilpotent topology."
        )
    }
}

out = DATA / "step58_biquard_ct_collapse_ledger.json"
with open(out, "w") as f:
    json.dump(result, f, indent=2)

print(json.dumps({
    "status": "ok",
    "output": str(out),
    "Biquard_estimate_section": "arXiv 1105.4904 Section 4, Lemmas 4.1-4.2 (not Section 14)",
    "worst_operator_exponents": [(t, math.sqrt(t)) for t in sample_ts],
    "minimal_patterns": [p["name"] for p in result["minimal_mixed_patterns"]],
    "CT_original_read": False,
    "CT_secondary_statement_used": True,
    "collapse_energy_example_k10_total": connected_sum_s2xs2(10)["total_weyl_energy_limit"],
}, indent=2))
