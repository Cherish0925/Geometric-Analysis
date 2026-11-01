#!/usr/bin/env python3
"""
Step 82 executable ledger for the fixed positive-mirror mixed rows.

Purpose: keep the Yau-26 P_4^+ refutation gate honest.  A fixed-row
counterexample requires (i) near-positive Ricci-pinched metrics, already
available in the log-Weyl/EH construction, and (ii) no Einstein metric of any
Einstein-constant sign on the same smooth manifold.  This script records the
pure topological/Chern-Weil arithmetic and the known holonomy-scope filters.
It does not prove any new analytic nonexistence theorem.
"""
import json
import math
from pathlib import Path

PI = math.pi

rows = [
    {"label": "r=1", "b_plus": 2, "b_minus": 4, "chi": 8, "tau": -2, "type": "#2CP2#4CP2bar (homeomorphism type)", "spin": False},
    {"label": "r=2 spin/balanced", "b_plus": 3, "b_minus": 3, "chi": 8, "tau": 0, "type": "#3(S2xS2) homeomorphism type", "spin": True},
    {"label": "r=2 nonspin/balanced", "b_plus": 3, "b_minus": 3, "chi": 8, "tau": 0, "type": "#3CP2#3CP2bar homeomorphism type", "spin": False},
    {"label": "r=3", "b_plus": 4, "b_minus": 2, "chi": 8, "tau": 2, "type": "#4CP2#2CP2bar (homeomorphism type)", "spin": False},
]

# For an Einstein 4-metric Ric=lambda g, s=4 lambda.
# CGB/signature give:
#   8 pi^2 chi = ∫(|W|^2 + s^2/24) dV
#   12 pi^2 tau = ∫(|W+|^2 - |W-|^2) dV
# hence
#   ∫|W±|^2 = 2 pi^2(2 chi ± 3 tau) - (1/3) lambda^2 V.
# For normalized positive/negative Einstein constant |lambda|=3 this is
#   ∫|W±|^2 = 2 pi^2(2 chi ± 3 tau) - 3 V.

def chiral_budget_at_lambda_abs_3(row, volume_symbol="V"):
    return {
        "Wplus_formula": f"{2*(2*row['chi']+3*row['tau'])}*pi^2 - 3*{volume_symbol}",
        "Wminus_formula": f"{2*(2*row['chi']-3*row['tau'])}*pi^2 - 3*{volume_symbol}",
        "Wtotal_formula": f"{8*row['chi']}*pi^2 - 6*{volume_symbol}",
    }

row_table = []
for r in rows:
    p1_Lambda_plus = 2*r["chi"] + 3*r["tau"]
    p1_Lambda_minus = 2*r["chi"] - 3*r["tau"]
    row_table.append({
        **r,
        "strict_HT_margin_2chi_minus_3abstau": 2*r["chi"] - 3*abs(r["tau"]),
        "p1_Lambda_plus_2chi_plus_3tau": p1_Lambda_plus,
        "p1_Lambda_minus_2chi_minus_3tau": p1_Lambda_minus,
        "normalized_abs_lambda_3_chiral_budgets": chiral_budget_at_lambda_abs_3(r),
        "ricci_flat_special_holonomy_exclusion": {
            "flat_holonomy": "excluded by chi=8 (flat compact manifolds have chi=0, and row is simply connected)",
            "reducible_holonomy": "excluded: compact simply connected Ricci-flat factors in dimensions 1,2,3 are flat/nonexistent, so a reducible 4D product cannot realize chi=8",
            "SU2_hyperkahler": "excluded by K3 topological invariants: compact simply connected hyperkahler surface has K3 type with chi=24, tau=-16 up to orientation",
            "generic_SO4": "NOT excluded by known classification; existence of compact irreducible Ricci-flat metrics with generic SO(n) holonomy is an open problem in dimension >=4",
        },
    })

# Balanced row exact numbers at Ric=±3, Bishop volume cap 8pi^2/3.
V_bishop = 8*PI**2/3
balanced = {"chi": 8, "tau": 0}
W_chiral_at_bishop = 2*PI**2*(2*balanced["chi"]) - 3*V_bishop
A_at_bishop = W_chiral_at_bishop / V_bishop

data = {
    "purpose": "Sign-leg and Ricci-flat scope audit for fixed positive-mirror mixed rows as candidate P_4^+ refutation targets.",
    "einstein_4d_chern_weil_formula": {
        "assumption": "Ric = lambda*g on a closed oriented 4-manifold; s=4*lambda",
        "W_total": "∫|W|^2 = 8*pi^2*chi - (2/3)*lambda^2*Vol",
        "W_plus": "∫|W+|^2 = 2*pi^2*(2*chi+3*tau) - (1/3)*lambda^2*Vol",
        "W_minus": "∫|W-|^2 = 2*pi^2*(2*chi-3*tau) - (1/3)*lambda^2*Vol",
        "sign_note": "The formula depends on lambda^2. Positive and negative Einstein constants have the same Chern-Weil budgets after fixing |lambda|; negative lambda does NOT reverse the scalar term sign.",
    },
    "balanced_row_Ric_abs_3_Bishop_calibration": {
        "V_Bishop_for_Ric_3": V_bishop,
        "int_Wplus_sq_at_Bishop": W_chiral_at_bishop,
        "A_equals_intWplus_over_V": A_at_bishop,
        "gursky_lebrun_lower_A": 6.0,
        "alignment_gap_factor_sqrt_A_over_sqrt_6": math.sqrt(A_at_bishop/6),
    },
    "rows": row_table,
    "fixed_row_refutation_logic": {
        "construction_leg": "available under recorded log-Weyl/EH hypotheses: near-positive Ricci-pinched metrics with defect O(1/|log a|) on each fixed A1 filling pattern",
        "nonexistence_leg": "must exclude Einstein metrics for lambda>0, lambda=0, and lambda<0 on the same smooth row",
        "lambda_positive": "alignment/Gram/T-anisotropy could only target this sign because the harmonic SD Weitzenbock lower term is s/6>0; current crude and CLR chains do not close",
        "lambda_zero": "special-holonomy Ricci-flat cases are excluded by chi/pi1, but generic irreducible SO(4) holonomy is not classified; therefore not banked as a theorem",
        "lambda_negative": "no current PSC-compatible obstruction; monopole/Bauer-Furuta routes require inputs absent on the mixed rows and alignment is sign-locked to s>0",
    },
    "source_anchors": [
        "Degen K3 moduli note lines 27-29: classification of closed Ricci-flat 4-manifolds is unsolved; only known examples finitely covered by T4 or K3",
        "Tony 2025 lines 36-39 and 57-61: Ricci-flat=>parallel spinor/special holonomy is open generally; Berger list includes generic SO(n); Question 1.2 remains open in dimension >=4",
        "Tony 2025 lines 84-87: Fischer-Wolf/Cheeger-Gromoll finite cover N x T^q structure for compact Ricci-flat manifolds",
        "Conformal Kahler rigidity source lines 639-643: compact hyperkahler 4-manifolds are flat tori or K3; K3 has Ahat=2",
        "Dai-Wei lines 37-44: Hitchin-Thorpe equality gives flat or universal-cover K3; this is equality-scope, not strict HT classification",
        "Kotschick monopole source lines 131-142 and Step57: simply connected strict-HT mixed rows evade classical and monopole-driven Einstein obstructions",
    ],
}

out = Path("Sessions/S0910A02/workspace/data/step82_sign_leg_and_ricciflat_scope.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({
    "output": str(out),
    "balanced_A_at_Bishop": A_at_bishop,
    "alignment_gap_factor": data["balanced_row_Ric_abs_3_Bishop_calibration"]["alignment_gap_factor_sqrt_A_over_sqrt_6"],
    "lambda0_banked": False,
    "reason": "generic compact irreducible Ricci-flat SO(4) holonomy remains unclassified/open",
}, indent=2))
