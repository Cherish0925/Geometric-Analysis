"""
Step 49: finite bookkeeping for the corrected bi-Kahler wall.

This script is not a differential-geometry proof.  It records the exponent
arithmetic used in the operator-norm estimate for a refined EH replacement
when the first Ozuch obstruction vanishes, and the finite A1 orientation
bookkeeping for product quotients of S^2 x S^2 already isolated in Steps 44--45.
"""
import json, math, os
from fractions import Fraction

script_dir = os.path.dirname(os.path.abspath(__file__))
ws = os.path.dirname(script_dir)
out = os.path.join(ws, "data", "step49_operator_norm_and_enumeration.json")
os.makedirs(os.path.dirname(out), exist_ok=True)

# ---------------------------------------------------------------------------
# Scaling model.
# In bubble coordinates for the refined approximate metric:
#   |Ric(g_t)-Lambda g_t - t lambda o|_{g_cal} <= C t^2 rho^2.
# On the bubble/neck g_t ~ t g_cal, so (0,2)-tensor operator norm gains t^{-1}.
# Region rho <= const: O(t).  Damage zone rho ~ t^{-1/4}: O(t^{1/2}).
# The first obstruction t lambda o becomes O(1) in operator norm on the core.
# A q-th order obstruction t^q mu o has operator norm O(t^{q-1}) and vanishes
# for q > 1.  Therefore only the first obstruction matters for Yau-26 C^0
# operator pinching.
# ---------------------------------------------------------------------------

def scaling_rows(q_values=(1,2,3,4)):
    rows=[]
    for q in q_values:
        rows.append({
            "obstruction_tensor_order_in_gcal_norm": f"t^{q} * obstruction_mode",
            "operator_norm_order_on_bubble_core": f"t^{q-1}",
            "vanishes_as_t_to_0": q > 1,
            "yau26_relevance": "load-bearing: order-one defect if nonzero" if q == 1 else "does not prevent delta(t)->0; blocks only exact Einstein gluing"
        })
    return rows

scaling = {
    "refined_remainder_bound_gcal_norm": "C * t^2 * rho^2 after subtracting first obstruction term",
    "metric_scale_on_bubble": "g_t ~ t * g_cal, so |T|_{op,g_t} ~ t^{-1}|T|_{g_cal} for a (0,2) tensor",
    "regions": [
        {
            "region": "bubble core rho <= O(1)",
            "remainder_operator_norm": "O(t)",
            "first_obstruction_operator_norm_if_lambda_nonzero": "O(1)"
        },
        {
            "region": "intermediate bubble 1 <= rho <= t^(-1/4)",
            "remainder_operator_norm": "O(t*rho^2)",
            "maximum": "O(t^(1/2)) at rho=t^(-1/4)"
        },
        {
            "region": "damage/transition zone rho ~ t^(-1/4)",
            "remainder_operator_norm": "O(t^(1/2)) using Morteza-Viaclovsky/Ozuch refined matching"
        },
        {
            "region": "orbifold exterior outside gluing balls",
            "remainder_operator_norm": "0 if the original orbifold metric is exact Einstein"
        }
    ],
    "uniform_four_bubble_consequence": "For finitely many A1 points with all first obstructions killed, sup |Ric(g_t)-Lambda g_t|_{op,g_t} <= C t^(1/2).",
    "obstruction_order_table": scaling_rows(),
    "critical_correction_to_step48": "Second and higher Ozuch obstructions are not load-bearing for Yau-26 C0 operator pinching. They obstruct exact Einstein desingularization but their residual tensors vanish in operator norm."
}

# ---------------------------------------------------------------------------
# A1 orientation bookkeeping.
# For product quotient orbifold with b+_orb=b-_orb=1 and N A1 singularities,
# an EH bubble compatible with the chosen orientation contributes one negative
# class, while a reversed EH bubble contributes one positive class.
# ---------------------------------------------------------------------------

def a1_orientation_table(case_name, N, source_status):
    rows=[]
    for r in range(N+1):
        bp = 1 + r
        bm = 1 + (N-r)
        tau = bp - bm
        chi = 2 + bp + bm
        c1sq_for_orientation = 2*chi + 3*tau
        # Known positive Einstein rows are only all-compatible or all-reversed,
        # orientation-insensitively the degree = 8-N del Pezzo diffeotype in
        # the two product cases N=4,6.  Mixed rows are not in the del Pezzo list.
        known = r in (0, N)
        if known:
            known_reason = "all one chirality; expected/crepant complex resolution has b_+=1 in one orientation and del Pezzo diffeotype (orientation reversal for r=N)"
        else:
            known_reason = "mixed chirality; not a Del Pezzo diffeotype in either orientation by b_+>1 and b_->1; no known Einstein metric recorded in this session"
        rows.append({
            "r_reversed": r,
            "compatible": N-r,
            "b_plus": bp,
            "b_minus": bm,
            "tau": tau,
            "chi": chi,
            "2chi_plus_3tau_in_chosen_orientation": c1sq_for_orientation,
            "balanced_stress_family_k_if_bplus_eq_bminus": bp if bp == bm else None,
            "known_to_admit_positive_Einstein_in_session_record": known,
            "known_reason_or_gap": known_reason,
            "candidate_yau26_wall_target": (not known)
        })
    return {
        "case": case_name,
        "A1_points": N,
        "source_status": source_status,
        "table": rows,
        "unknown_rows": [r for r in rows if not r["known_to_admit_positive_Einstein_in_session_record"]]
    }

z2 = a1_orientation_table(
    "diagonal half-turn Z2 quotient (S2 x S2)/Z2",
    4,
    "Steps 44-45 source/audit: four A1 points; curvature blocks R_+=R_-=diag(Lambda,0,0); topology parity/smooth type still needs proof for mixed rows."
)
v4 = a1_orientation_table(
    "diagonal V4 product quotient (Step45 audit model)",
    6,
    "Step45 bookkeeping model: six A1 points for a diagonal V4 action; actual group-action/smooth-type details require independent validation."
)

# ---------------------------------------------------------------------------
# Product-graph all-ADE classification heuristic.
# Finite subgroups of SO(3): C_m, D_m, T, O, I.  For graph actions on both
# factors, a stabilizer of order m>2 produces endpoint sign combinations with
# weights (1,a) and (1,-a); both cannot be SU(2) unless 2=0 mod m.  Hence all
# isolated singularities can be ADE only when all nontrivial stabilizers have
# order 2.  Finite rotation groups with only order-2 stabilizers are C2 and D2=V4.
# ---------------------------------------------------------------------------
so3_types = [
    {"type":"C_m", "has_order_gt_2_stabilizer":"m>2", "all_ADE_possible":"only m=2"},
    {"type":"D_m", "has_order_gt_2_stabilizer":"m>2 rotation axis plus order-2 axes", "all_ADE_possible":"only m=2 (D2=V4)"},
    {"type":"T", "has_order_gt_2_stabilizer":"orders 3", "all_ADE_possible":False},
    {"type":"O", "has_order_gt_2_stabilizer":"orders 3 and 4", "all_ADE_possible":False},
    {"type":"I", "has_order_gt_2_stabilizer":"orders 3 and 5", "all_ADE_possible":False},
]
product_graph_classification = {
    "scope": "orientation-preserving product graph actions Gamma -> SO(3)xSO(3) with both projections injective; excludes factor-swap groups, which remain to be enumerated separately",
    "endpoint_weight_test": "For a stabilizer of order m, endpoint choices give local complex weights (1,a) and (1,-a). Requiring both to be ADE/SU(2) gives 1+a=0 and 1-a=0 mod m, hence m divides 2.",
    "conclusion_in_scope": "Only C2 and D2=V4 graph actions can have exclusively A1/ADE isolated singularities in this product-action class.",
    "so3_type_table": so3_types,
    "remaining_out_of_scope": "isometries exchanging the two S2 factors or non-graph actions; these need an Agent3 finite-group enumeration if the product-quotient wall becomes central."
}

results = {
    "purpose": "Correct Step48 allocation: first obstruction is the whole local C0 pinching story; finite product-quotient orientation rows identify known-Einstein calibrations and mixed unknown targets.",
    "scaling": scaling,
    "a1_orientation_cases": [z2, v4],
    "product_graph_all_ADE_classification": product_graph_classification,
    "session_level_conclusions": [
        "If R_epsilon(p) zeta = 0 at every A1 replacement, the refined four-bubble approximate metrics have delta_+(g_t) <= C t^(1/2) -> 0, regardless of higher-order exact-Einstein obstructions.",
        "For (S2 x S2)/Z2, r=0 and r=4 are harmless for Yau-26 because the underlying del Pezzo degree-4 diffeotype is known to admit positive Einstein metrics; r=1,2,3 are concrete mixed-chirality targets, not resolved by current Einstein-existence knowledge.",
        "The balanced r=2 row is not forced; Yau-26 is orientation-free, so every mixed row whose smooth manifold lacks known Einstein metrics matters.",
        "Within product graph actions, the only all-ADE cases are Z2 and V4; factor-swap actions and smooth-type/parity remain open finite checks."
    ]
}

with open(out, "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps({
    "output": out,
    "main_bound": scaling["uniform_four_bubble_consequence"],
    "z2_unknown_r": [row["r_reversed"] for row in z2["unknown_rows"]],
    "v4_unknown_r": [row["r_reversed"] for row in v4["unknown_rows"]],
    "product_graph_all_ADE": product_graph_classification["conclusion_in_scope"]
}, indent=2))
