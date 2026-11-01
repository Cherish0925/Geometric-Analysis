#!/usr/bin/env python3
"""
Step 85: Three computations that close open questions.

1. L^2 SIZE OF NEAR-PINCHED FAMILY.
   The fixed-A1 construction has modification in 4 balls of radius R=a^{1/4},
   with pointwise |E|_op <= C / (|log a|/4 + O(1)).
   Volume of each ball: omega_4 R^4 = omega_4 a.
   So int |E|^2 = O(a / |log a|^2), polynomially small.
   This proves the family is a genuine degenerating minimizer of Z=int|E|^2,
   disabling the direct variational method and all L^p instruments with p>=2.

2. ALL-DIMENSIONAL INTERVAL PREREQUISITE.
   For n>=3, Lohkamp gives Ric<0 on every closed n-manifold.
   After rescaling, every manifold enters the hypothesis class [c,0].
   Hence Yau-26 false => some closed n-manifold has no Einstein metric.
   For n>=5 no such manifold is known.

3. LEBRUN NEGATIVE-BRANCH SEQUENCE.
   The stable-gap bound delta/(1-delta) >= sqrt((p-1/3)/2) degenerates
   at p=1/3 while LeBrun nonexistence still holds (k>=A/3).
   Can we construct negatively pinched metrics with delta -> 0 on
   LeBrun manifolds with p -> 1/3+?

Author: Agent2, Step 85.
"""

import json, math
from pathlib import Path

out_path = Path("Sessions/S0910A02/workspace/data/step85_L2_variational_closure.json")
out_path.parent.mkdir(parents=True, exist_ok=True)

# === 1. L^2 size of the near-pinched family ===
# Parameters:  b = a^{1/2},  R = a^{1/4},  L = log(R/(8b)) = (1/4)|log a| + O(1)
# In each modification ball of radius R:
#   - pointwise |E|_op <= C/L   (from the O(1/|log a|) construction theorem)
#   - volume of ball ~ omega_4 R^4 = (pi^2/2) a  (omega_4 = pi^2/2 for unit 4-ball)
# Four disjoint balls, so:
#   int |E|^2 <= 4 * (C/L)^2 * omega_4 * a = O(a / |log a|^2)

omega_4 = math.pi**2 / 2  # volume of unit 4-ball

# Tabulate for several values of a
a_values = [1e-4, 1e-8, 1e-16, 1e-32, 1e-64]
l2_table = []
for a in a_values:
    R = a**0.25
    b = a**0.5
    L = 0.25 * abs(math.log(a))  # leading term
    Cop_defect = 1.0 / L  # C^0 operator defect ~ 1/L (with C=1 for scaling)
    ball_vol = omega_4 * a  # volume of one modification ball
    int_E2 = 4 * Cop_defect**2 * ball_vol  # upper bound on int |E|^2
    l2_table.append({
        "a": a,
        "R": R,
        "b": b,
        "L_leading": L,
        "Cop_defect": Cop_defect,
        "single_ball_volume": ball_vol,
        "int_E_squared_upper_bound": int_E2,
        "ratio_intE2_over_a": int_E2 / a if a > 0 else None,
    })

# The ratio int|E|^2 / a = 4 * omega_4 / L^2 -> 0 as a -> 0.
# More precisely, int|E|^2 = O(a / |log a|^2).
# The C^0 defect is 1/L = O(1/|log a|), while L^2 norm is sqrt(int|E|^2) = O(a^{1/2}/|log a|).
# For any p >= 2: (int |E|^p)^{1/p} <= C^{(p-2)/p}_op * (int|E|^2)^{1/p} 
#                                     = O(L^{-(p-2)/p}) * O((a/L^2)^{1/p})
#                                     = O(a^{1/p} / L)   (polynomially vanishing for p >= 2).

# === 2. All-dimensional interval prerequisite ===
# Argument: For n >= 3, fix any c < 0. By Lohkamp, every closed n-manifold M
# admits a metric g with Ric_g < 0. Say eigenvalues of Ric_g (as endomorphism)
# lie in [lambda_min, lambda_max] with lambda_max < 0.
# Set alpha = |lambda_min| / (2|c|). Then g' = alpha * g satisfies:
#   Ric_{g'} = Ric_g  (the (0,2) Ricci tensor is scaling-invariant)
#   c * g' = c * alpha * g
# The endomorphism eigenvalues of Ric relative to g' are:
#   (g')^{-1} Ric = alpha^{-1} g^{-1} Ric = alpha^{-1} lambda_i
# So the condition c g' <= Ric_{g'} <= 0 as (0,2)-tensors means:
#   c alpha g(v,v) <= Ric_g(v,v) <= 0  for all v
# i.e., c alpha <= lambda_i for all i (and lambda_i <= 0 is automatic).
# Since c alpha = c |lambda_min| / (2|c|) = -|lambda_min|/2 <= lambda_min <= lambda_i,
# the lower bound holds.
#
# Hence every closed n-manifold (n>=3) satisfies the hypothesis of [c, 0].
# If Yau-26 is true for this interval, EVERY closed n-manifold admits Einstein.
# Contrapositive: Yau-26 false => some closed n-manifold has no Einstein metric.

interval_theorem = {
    "statement": (
        "For n >= 3: Yau-26 is false in dimension n ONLY IF there exists "
        "a closed connected smooth n-manifold carrying no Einstein metric "
        "of any sign lambda."
    ),
    "proof_sketch": (
        "By Lohkamp, every closed n-manifold (n>=3) admits g with Ric_g < 0. "
        "After constant rescaling, c g' <= Ric_{g'} <= 0 for any c < 0. "
        "So the hypothesis class of interval [c, 0] equals ALL closed n-manifolds. "
        "If Yau-26 is false, this interval fails, so some manifold in the class "
        "has no Einstein metric."
    ),
    "dimensional_consequences": {
        "n=2": "Every surface admits constant curvature (uniformization). Yau-26 trivially true.",
        "n=3": "Yau-26 true by Hamilton: positive Ricci pinching gives space-form Einstein. "
               "Also, Sol/Nil manifolds have no Einstein (constant-curvature) metric, "
               "but the positive branch bypasses them.",
        "n=4": "Plenty of no-Einstein manifolds (chi <= 0 by CGB; S1xS3; LeBrun families). "
               "Yau-26 reduces to strict branches P_4^+(delta) and P_4^-(delta).",
        "n>=5": "NO certified closed n-manifold without an Einstein metric is known. "
                "This is the minimal prerequisite for any refutation. "
                "Either every closed n-manifold admits Einstein (making Yau-26 trivially true), "
                "or a new obstruction theorem in higher-dimensional geometry is required."
    }
}

# === 3. LeBrun negative-branch sequence ===
# LeBrun: M = X # k CP-bar^2 has no Einstein metric for k >= A/3 = c_1^2(X)/3.
# Stable-gap: delta/(1-delta) >= sqrt((p-1/3)/2), p = k/A.
# At p = 1/3: bound gives delta >= 0. At p = 1/3 + eta: delta_min ~ sqrt(eta/2).
# Question: can we construct metrics with ||Ric + g|| <= delta on M with delta -> 0
# as p -> 1/3+?

# Burns core obstruction: the (-1)-blowup core has Ric != 0 (not crepant).
# The Burns metric on O(-1) -> CP^1 has Ricci of order 1 relative to the metric,
# giving a raised-index operator-norm defect of O(1), not O(1/|log a|).
# This is fundamentally different from the A_1 (Eguchi-Hanson) core,
# which is Ricci-flat and gives only logarithmic defect.

# Tabulate the stable-gap bound degeneracy
lebrun_table = []
for eta in [0.5, 0.2, 0.1, 0.05, 0.01, 0.001, 0.0001]:
    p = 1/3 + eta
    rhs = math.sqrt((p - 1/3) / 2)
    delta_min = rhs / (1 + rhs)
    lebrun_table.append({
        "eta": eta,
        "p": p,
        "sqrt_rhs": rhs,
        "delta_min": delta_min,
        "note": "delta_min -> 0 as eta -> 0"
    })

lebrun_sequence_question = {
    "statement": (
        "Does there exist a sequence of minimal complex surfaces X_i of general type "
        "with A_i = c_1^2(X_i) -> infinity, integers k_i >= A_i/3 with "
        "p_i = k_i/A_i -> 1/3, and metrics g_i on M_i = X_i # k_i CP-bar^2 "
        "with ||Ric_{g_i} + g_i||_op -> 0?"
    ),
    "significance": (
        "If yes: every strict negative interval is defeated, and dimension-four "
        "refutation reduces to the positive branch P_4^+ alone."
    ),
    "burns_core_tension": (
        "The ordinary Burns (-1)-blowup core on Bl_1(C^2) = O(-1) is NOT Ricci-flat: "
        "its Ricci endomorphism has eigenvalues of order 1, giving operator-norm "
        "defect O(1), not O(1/|log a|). Naive local gluing cannot produce tight "
        "negative pinching. By contrast, the A_1 (Eguchi-Hanson) core is Ricci-flat, "
        "and only the Weyl transition produces the O(1/|log a|) defect."
    ),
    "pinching_monopole_incompatibility": (
        "The manifolds that CAN be tightly pinched (A_1 mixed rows) are SW-void "
        "and hence outside the LeBrun reservoir. The manifolds WITH LeBrun "
        "obstruction require (-1)-blowups, which resist tight pinching. "
        "This is a structural tension, not a coincidence."
    ),
    "possible_escape": (
        "A non-local construction (e.g., Ricci flow, conformal deformation, "
        "Kähler-edge methods) might avoid the Burns core. Alternatively, "
        "a different no-Einstein reservoir not requiring (-1)-blowups could "
        "provide the negative-branch sequence."
    )
}

# === Assemble output ===
data = {
    "purpose": "Step 85: variational closure, all-dimensional interval theorem, and LeBrun sequence question.",
    "L2_closure": {
        "formula": "int |E|^2 <= 4 * C^2 * omega_4 * a / L^2 = O(a / |log a|^2)",
        "omega_4_unit_ball": omega_4,
        "table": l2_table,
        "consequence": (
            "The near-pinched family is a genuine degenerating minimizer of Z=int|E|^2 "
            "with inf Z = 0. No L^p instrument with p >= 2 can obstruct these rows. "
            "The direct variational method is disabled: the infimum is attained only "
            "in the degenerate limit (orbifold + Eguchi-Hanson bubbles)."
        ),
        "variational_route_closed": True,
        "reason": (
            "The explicit family g_a satisfies Z(g_a) = O(a/|log a|^2) -> 0 "
            "while degenerating. Any almost-critical compactness/epsilon-regularity "
            "theory must handle this polynomial-vs-logarithmic mismatch. "
            "The unweighted C^0 operator norm is the sharp norm for the problem, "
            "exactly as the ell=2 classification implies."
        )
    },
    "all_dimensional_interval_theorem": interval_theorem,
    "lebrun_negative_branch": {
        "question": lebrun_sequence_question,
        "stable_gap_degeneracy_table": lebrun_table,
    }
}

out_path.write_text(json.dumps(data, indent=2, default=str))
print(json.dumps({
    "output": str(out_path),
    "L2_values_sample": {
        "a=1e-16": f"int|E|^2 <= {l2_table[2]['int_E_squared_upper_bound']:.2e}",
        "a=1e-32": f"int|E|^2 <= {l2_table[3]['int_E_squared_upper_bound']:.2e}",
    },
    "all_dimensional_theorem": True,
    "lebrun_question_formulated": True,
}, indent=2))
