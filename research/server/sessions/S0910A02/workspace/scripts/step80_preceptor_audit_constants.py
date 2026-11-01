#!/usr/bin/env python3
"""Step 80 audit constants for Yau--26 mixed-row review.

This script does not prove geometry.  It records exact Chern--Weil algebra and
simple arithmetic examples showing why the Step-79 ADE energy cap does not
exclude non-ADE/class-T Ricci-flat Kähler ALE ends.
"""
from fractions import Fraction
import json
from pathlib import Path

chi = 8
rows = []
for tau in [-2, 0, 2]:
    q_plus = Fraction(2*chi + 3*tau, 4)   # (int |W+|^2)/(8*pi^2) in collapse limit
    q_minus = Fraction(2*chi - 3*tau, 4)
    rows.append({
        "tau": tau,
        "Wplus_limit_over_pi2": float(8*q_plus),  # since q is units of 8*pi^2
        "Wminus_limit_over_pi2": float(8*q_minus),
        "Qplus_units_8pi2": f"{q_plus.numerator}/{q_plus.denominator}" if q_plus.denominator != 1 else str(q_plus.numerator),
        "Qminus_units_8pi2": f"{q_minus.numerator}/{q_minus.denominator}" if q_minus.denominator != 1 else str(q_minus.numerator),
        "formula": "int|W+|^2 -> 2*pi^2*(2*chi+3*tau), int|W-|^2 -> 2*pi^2*(2*chi-3*tau) when E and scalar-volume terms vanish"
    })

# Exact positive Einstein chi=8,tau=0 algebra in the Ric=lambda g normalization.
# 4 int Wpm^2 + (4/3) lambda^2 V = 8*pi^2(2 chi +/- 3 tau)
# so for tau=0: Wpm/pi^2 = 32 - (lambda^2 V)/(3*pi^2).
positive_einstein_tau0 = {
    "Wpm_formula_over_pi2": "32 - (lambda^2*V)/(3*pi^2)",
    "Bishop_Obata_lambda2V_over_pi2_bound": 24,
    "therefore_Wpm_lower_over_pi2_from_Bishop": 24,
    "CGB_upper_over_pi2": 32,
    "range_nonempty": True,
}

# ADE caps reproduced from Step 79.
ade = []
# A_r r>=1, D_r r>=4, E6,E7,E8
for r in range(1, 9):
    ade.append((f"A{r}", r, r+1))
for r in range(4, 9):
    ade.append((f"D{r}", r, 4*(r-2)))
ade.extend([("E6", 6, 24), ("E7", 7, 48), ("E8", 8, 120)])
ade_rows=[]
for name, rank, order in ade:
    Q = Fraction(rank+1,1) - Fraction(1, order)
    ade_rows.append({"name": name, "rank": rank, "end_order": order, "chi": rank+1, "Q_units_8pi2": f"{Q.numerator}/{Q.denominator}", "fits_total_Q8": Q <= 8, "fits_balanced_chiral_Q4": Q <= 4})
max_ade_order_total = max(row["end_order"] for row in ade_rows if row["fits_total_Q8"])
max_ade_order_chiral = max(row["end_order"] for row in ade_rows if row["fits_balanced_chiral_Q4"])

# Class-T cyclic Ricci-flat Kahler ALE smoothing: singularity 1/(d n^2)(1,d n a -1)
# with Q=d - 1/(d n^2), chi=d, end order=d n^2.  For fixed d<=8, order is unbounded.
classT_examples=[]
for d in [1,2,3,4,5,8]:
    for n in [2,5,20,100]:
        Q = Fraction(d,1) - Fraction(1, d*n*n)
        classT_examples.append({
            "d_chi": d,
            "n": n,
            "end_order": d*n*n,
            "Q_units_8pi2": f"{Q.numerator}/{Q.denominator}",
            "fits_total_Q8": Q <= 8,
            "fits_balanced_chiral_Q4": Q <= 4,
            "epsilon_needed_less_than_AVR": f"< {d*n*n}^-1 to force |Gamma|>{d*n*n}",
        })

summary = {
    "mixed_row_chiral_budgets_chi8": rows,
    "positive_einstein_tau0_range": positive_einstein_tau0,
    "ADE_caps": {
        "max_order_with_total_Q<=8": max_ade_order_total,
        "max_order_with_balanced_chiral_Q<=4": max_ade_order_chiral,
        "rows": ade_rows,
    },
    "classT_loophole": {
        "formula": "Q_T(d,n)=d-1/(d*n^2), chi=d, |Gamma_infty|=d*n^2",
        "meaning": "For any fixed d<=8 (and d<=4 for one balanced chirality), n can grow, so energy and chi budgets do not bound |Gamma| outside the ADE/Kronheimer class.",
        "examples": classT_examples,
    },
    "audit_conclusions": [
        "Step79 total and chiral formulas are correct after using the factor 2*pi^2*(2 chi +/- 3 tau), not 4*pi^2.",
        "The Weyl-energy magnitude inequalities leave nonempty slack and do not obstruct positive Einstein metrics on chi=8,tau=0 rows.",
        "The ADE outermost exclusion is valid only for smooth Kronheimer hyper-Kahler ALE models; class-T/non-SU(2) Ricci-flat Kahler ALE arithmetic can have chi<=8 and arbitrarily large end group.",
        "The Step71 exact Q=4 no-sum result concerns lossless decomposition of the entire chiral budget into half-flat ALE atoms; it does not exclude a single outermost class-T ALE bubble with Q<4 plus residual energy elsewhere."
    ]
}

out = Path("Sessions/S0910A02/workspace/data/step80_preceptor_audit_constants.json")
out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
print(json.dumps({"output": str(out), "max_ade_total": max_ade_order_total, "max_ade_chiral": max_ade_order_chiral, "classT_unbounded_orders_for_d_le_4": True}, indent=2))
