"""
Step 50: exact bookkeeping for the load-bearing positive-branch reduction.

This is a reproducible arithmetic/provenance record, not a substitute for the
analytic desingularization estimates.  It encodes:
  * the operator-norm exponent conversion for a refined EH replacement;
  * why reversed EH has the same estimate but tests R_- instead of R_+;
  * the finite Z2 mixed rows and what Yau-26 P4+ would imply for them;
  * which standard obstructions vanish or are inapplicable at this level.
"""
import json, os
from fractions import Fraction

# Convention: epsilon is length scale, t=epsilon^2 is the metric scale in the
# bubble metric g_t ~ t*g_EH.  Ozuch's zeta parameter is the metric-scale size
# of the EH deformation; for exponent bookkeeping call it t.

regions = []
for name, rho_power in [
    ("core rho=O(1)", Fraction(0,1)),
    ("transition rho=t^(-1/4)", Fraction(-1,4)),
]:
    # Refined residual in EH norm: t^2*rho^2. Operator norm in t*g_EH: multiply t^-1.
    residual_exp = Fraction(2,1) + 2*rho_power - 1
    first_exp = Fraction(1,1) - 1  # t*lambda*o raised by t^-1.
    second_exp = Fraction(2,1) - 1
    regions.append({
        "region": name,
        "rho_as_t_power": str(rho_power),
        "refined_residual_operator_exponent": str(residual_exp),
        "first_obstruction_operator_exponent": str(first_exp),
        "second_obstruction_operator_exponent": str(second_exp),
        "refined_residual_tends_to_zero": residual_exp > 0,
        "first_obstruction_tends_to_zero_if_nonzero": first_exp > 0,
        "second_obstruction_tends_to_zero": second_exp > 0,
    })

# Diagonal Z2 rows.  The quotient is simply connected by Armstrong because the
# nontrivial group element has fixed points; each EH disk-bundle fill is simply
# connected and kills the RP3 meridian in the van Kampen picture.
rows=[]
for r in range(5):
    bp=1+r
    bm=5-r
    tau=bp-bm
    chi=2+bp+bm
    scalar_positive_for_delta_lt_1 = True # Ric in [(1-delta),(1+delta)]g in dimension 4.
    if r in [1,2,3]:
        yau26_implication = "If P4+ is true, this fixed smooth mixed-resolution manifold must carry some Einstein metric. Current session has no theorem proving existence or nonexistence."
        sw_status = "b_+>1 and positive scalar curvature metrics imply ordinary SW invariants vanish / SW moduli empty for generic PSC metrics; SW-based LeBrun obstructions cannot be applied directly."
    else:
        yau26_implication = "Endpoint one-chirality row is a known-Einstein calibration at the diffeotype level, not a counterexample target."
        sw_status = "b_+=1 in one orientation; chamber/perturbed SW theory has special behavior, but endpoint is not used as a no-Einstein target."
    if r == 2:
        spin_status = "undetermined by current boundary data; if even then homeomorphic to #3(S2xS2), if odd then I_{3,3}; exact smooth type not needed for the conditional-hardness statement."
    elif r in [1,3]:
        spin_status = "non-spin/odd if smooth simply connected, since even unimodular signature would need divisibility not satisfied."
    else:
        spin_status = "endpoint del Pezzo orientation is non-spin/odd."
    rows.append({
        "r_reversed": r,
        "b_plus": bp,
        "b_minus": bm,
        "chi": chi,
        "tau": tau,
        "strict_Hitchin_Thorpe": 2*chi > 3*abs(tau),
        "positive_scalar_curvature_from_pinching_for_delta_lt_1": scalar_positive_for_delta_lt_1,
        "spin_status": spin_status,
        "ordinary_SW_status": sw_status,
        "yau26_P4plus_implication": yau26_implication,
        "mixed_wall_target": r in [1,2,3]
    })

out={
    "purpose":"Verify Step50 load-bearing estimate and conditional-hardness reduction for diagonal Z2 product quotient mixed rows.",
    "scale_convention": {
        "epsilon":"length scale of excised orbifold ball / EH core",
        "t":"metric-scale gluing parameter, t=epsilon^2; local bubble metric comparable to t*g_EH",
        "refined_metric_core":"t*(g_EH + t*h2 + ...); h2 solves linearized Ricci equation modulo first obstruction",
    },
    "estimate_sources": [
        "Ozuch higher-obstruction source lines 372-376: negatively oriented EH is isometric to |zeta|*EH and has opposite orientation.",
        "Ozuch lines 496-514: h2(zeta^±), h4(zeta^±) exist and lambda_k(zeta^±)=c< R^±(H2) zeta^±, zeta_(k)^± >.",
        "Ozuch lines 715-726 and 783-789: approximate Einstein modulo obstructions and four-dimensional EH/gluing estimates, citing Biquard Section 14.",
        "MV Calabi lines 456-514: model exponent t^2*rho^2 and transition rho=t^-1/4; used only as exponent calibration."
    ],
    "reversed_bubble_check": {
        "metric_estimate_transfer":"The underlying Riemannian EH metric for zeta^- is isometric/homothetic to zeta^+ EH, so local pointwise and weighted estimates transfer verbatim.",
        "what_changes":"The attaching map reverses the orientation on the RP3 link and the first obstruction coefficient uses the opposite chiral block R^- instead of R^+.",
        "product_quotient_reason_mixed_rows_exist":"For S2xS2 product quotient, R_+=R_-=diag(Lambda,0,0); choosing zeta in the two-dimensional kernel kills the vector first obstruction for either chirality at each A1 point.",
        "leading_order_interaction":"At first refined order the four A1 replacements are local and independent; inter-point/global Kuranishi terms occur at higher order and do not affect C0 operator pinching once first local obstructions vanish."
    },
    "exponent_table": regions,
    "main_bound":"For any fixed finite orientation assignment with all zeta_j in ker R_{epsilon_j}(p_j), sup ||Ric(g_t)-Lambda g_t||_op <= C*t^(1/2) in the clean model, or with a small beta-loss under Ozuch weighted norms; in either case it tends to zero.",
    "z2_rows": rows,
    "hardness_reduction":"For any actual mixed-resolution smooth manifold M_r (r=1,2,3) obtained by the diagonal Z2 construction, P4+ would imply that M_r admits some Einstein metric. Current tools in the session neither prove nor disprove such an Einstein metric; SW obstructions vanish under PSC/b_+>1, and Hitchin-Thorpe is satisfied.",
    "not_settled":"This does not settle positive collapse, negative branch, dimensions n>=5, exact smooth diffeomorphism type of mixed rows, or Lean formalization. A01's Q-Gorenstein smoothing mechanism is a live existence route but has not been verified here for mixed real rows."
}
ws=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_path=os.path.join(ws,"data","step50_reversed_bubble_estimate_and_reduction.json")
os.makedirs(os.path.dirname(out_path),exist_ok=True)
with open(out_path,"w") as f: json.dump(out,f,indent=2)
print(json.dumps({
    "exponents": regions,
    "mixed_rows":[{k:row[k] for k in ["r_reversed","b_plus","b_minus","tau","strict_Hitchin_Thorpe"]} for row in rows if row["mixed_wall_target"]],
    "main_bound": out["main_bound"],
    "reduction": out["hardness_reduction"]
}, indent=2))
