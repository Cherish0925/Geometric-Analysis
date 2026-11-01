#!/usr/bin/env python3
"""Step 71: Diophantine audit for localized Gauss--Bonnet collapse energy.

For the spin balanced row #_3(S^2 x S^2), chi=8 and tau=0.  If a
positive Ricci-pinched sequence collapses with Vol -> 0, bounded-curvature
regions contribute o(1) to Chern--Gauss--Bonnet, so concentration regions must
carry total curvature quantum chi=8.  For an ALE Ricci-flat bubble asymptotic
to S^3/Gamma, CGB with boundary gives

    Q_ALE = (1/8pi^2) int |Rm|^2 = chi(ALE) - 1/|Gamma|.

For ALF gravitational instantons with the usual decay/finite topological type,
the boundary term vanishes and the corresponding quantum is

    Q_ALF = chi(ALF),

as source-checked in the local Knowledge note around Curvature-cones lines
400--417.  This script enumerates ADE/Kronheimer ALE quanta with Q <= 8 and
checks exact multiset sums to the total quantum 8 and one chiral half quantum 4.
The chiral check matters because hyperkaehler ALE/ALF curvature sits in one Weyl
half after orientation choice; ambient tau=0 forces 4 units in each half.
"""
from fractions import Fraction
from itertools import combinations_with_replacement
import json
from pathlib import Path

# ADE data for nontrivial finite subgroups of SU(2), using Dynkin rank r,
# chi = r + 1 for the minimal resolution / Kronheimer ALE, and group order.
types = []
for m in range(2, 9):  # A_{m-1}; Q<=8 iff m<=8
    types.append({
        "name": f"A{m-1}", "family": "A", "Gamma_order": m,
        "rank": m-1, "chi": m, "Q": Fraction(m, 1) - Fraction(1, m),
    })
for k in range(4, 8):  # D_k; Q<=8 iff k<=7
    order = 4 * (k - 2)
    types.append({
        "name": f"D{k}", "family": "D", "Gamma_order": order,
        "rank": k, "chi": k + 1, "Q": Fraction(k + 1, 1) - Fraction(1, order),
    })
for name, order, rank in [("E6", 24, 6), ("E7", 48, 7), ("E8", 120, 8)]:
    Q = Fraction(rank + 1, 1) - Fraction(1, order)
    if Q <= 8:
        types.append({"name": name, "family": "E", "Gamma_order": order,
                      "rank": rank, "chi": rank + 1, "Q": Q})

types.sort(key=lambda d: (d["Q"], d["name"]))

def fmt(fr: Fraction) -> str:
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)

def exact_solutions(target: Fraction, max_total=None):
    if max_total is None:
        max_total = target
    minQ = min(d["Q"] for d in types)
    max_len = int(max_total // minQ) + 2
    sols = []
    for r in range(1, max_len + 1):
        for combo in combinations_with_replacement(range(len(types)), r):
            Qsum = sum(types[i]["Q"] for i in combo)
            if Qsum == target:
                chisum = sum(types[i]["chi"] for i in combo)
                recip = sum(Fraction(1, types[i]["Gamma_order"]) for i in combo)
                sols.append({
                    "combo": [types[i]["name"] for i in combo],
                    "length": r,
                    "chi_sum": chisum,
                    "reciprocal_order_sum": fmt(recip),
                    "integrality_check": recip.denominator == 1 and recip == chisum - target,
                })
    return sols

def nearest_sums(target: Fraction, max_total=Fraction(10), limit=20):
    minQ = min(d["Q"] for d in types)
    max_len = int(max_total // minQ) + 2
    near = []
    for r in range(1, max_len + 1):
        for combo in combinations_with_replacement(range(len(types)), r):
            Qsum = sum(types[i]["Q"] for i in combo)
            if Fraction(0) < Qsum <= max_total:
                near.append((abs(Qsum-target), Qsum, combo))
    near = sorted(set(near), key=lambda x: (x[0], x[1], x[2]))[:limit]
    out = []
    for _diff, Qsum, combo in near:
        out.append({
            "combo": [types[i]["name"] for i in combo],
            "Qsum": fmt(Qsum),
            "difference_from_target": fmt(Qsum-target),
            "chi_sum": sum(types[i]["chi"] for i in combo),
            "reciprocal_order_sum": fmt(sum(Fraction(1, types[i]["Gamma_order"]) for i in combo)),
        })
    return out

def integer_ALE_contributions_up_to(target: Fraction):
    """ADE ALE contributions that can be completed to target by ALF integer quanta."""
    minQ = min(d["Q"] for d in types)
    max_len = int(target // minQ) + 2
    out = [{"ALE_combo": [], "ALE_Q": "0", "ALF_integer_needed": fmt(target)}]
    seen = set()
    for r in range(1, max_len + 1):
        for combo in combinations_with_replacement(range(len(types)), r):
            Qsum = sum(types[i]["Q"] for i in combo)
            if Qsum <= target and Qsum.denominator == 1:
                key = (Qsum, combo)
                if key in seen:
                    continue
                seen.add(key)
                out.append({
                    "ALE_combo": [types[i]["name"] for i in combo],
                    "ALE_Q": fmt(Qsum),
                    "ALF_integer_needed": fmt(target - Qsum),
                    "reciprocal_order_sum": fmt(sum(Fraction(1, types[i]["Gamma_order"]) for i in combo)),
                })
    return out

# Basic row ledger.  For #_k(S2xS2), chi=2k+2; here k=3.
k = 3
chi = 2*k + 2
tau = 0
total_quantum = Fraction(chi, 1)          # int |W|^2 / (8 pi^2) in Vol->0 Ric≈g collapse
chiral_quantum_each = Fraction(chi, 2)    # tau=0, so each Weyl half has 4 units

total_solutions = exact_solutions(total_quantum)
chiral_solutions = exact_solutions(chiral_quantum_each)
chiral_ALE_plus_ALF = integer_ALE_contributions_up_to(chiral_quantum_each)

result = {
    "target_manifold": "#_3(S^2 x S^2) spin balanced row (homeomorphism type; diffeotype of glued row not certified)",
    "correct_topology": {"k": k, "chi": chi, "tau": tau, "b_plus": 3, "b_minus": 3},
    "corrected_energy_ledger": {
        "CGB_identity": "8*pi^2*chi = int(|W|^2 + s^2/24 - |E|^2/2)",
        "collapse_Ric_approx_g_Vol_to_0": "bounded-curvature regions contribute o(1); total concentration quantum equals chi",
        "total_int_abs_W_sq": "64*pi^2",
        "total_quantum_int_abs_W_sq_over_8pi2": fmt(total_quantum),
        "signature_tau_zero_chiral_each": "int|W+|^2 = int|W-|^2 = 32*pi^2 asymptotically, i.e. 4 units of 8*pi^2 each",
        "strategist_correction": "24*pi^2 was wrong; chi(#_3(S^2xS^2))=8, so 8*pi^2*chi=64*pi^2",
    },
    "source_checked_quantum_formulas": {
        "ALE": "Q_ALE = chi(ALE) - 1/|Gamma|",
        "ALF": "Q_ALF = chi(ALF) (boundary term tends to zero)",
        "source_anchor": "Knowledge/objects/papers/Curvature-cones-and-characteristic-numbers--8d08033cf0c7--47e3a363f7a4/object.md lines 400-417",
    },
    "integrality_obstruction_ALE_part": "Because ALF quanta are integers, any ALE part in a fixed Weyl half must have integer total quantum to be completed to the chiral target 4.",
    "ADE_types_with_Q_le_8": [
        {**{k:v for k,v in d.items() if k != "Q"}, "Q": fmt(d['Q']), "Q_float": float(d['Q'])}
        for d in types
    ],
    "exact_ADE_multiset_solutions_total_Q_8": total_solutions,
    "number_exact_ADE_total_solutions": len(total_solutions),
    "exact_ADE_multiset_solutions_one_chiral_half_Q_4": chiral_solutions,
    "number_exact_ADE_chiral_half_solutions": len(chiral_solutions),
    "allowed_ADE_ALE_contributions_to_one_chiral_half_when_ALF_integer_quanta_allowed": chiral_ALE_plus_ALF,
    "nearest_ADE_multiset_sums_to_total_8": nearest_sums(total_quantum),
    "nearest_ADE_multiset_sums_to_chiral_4": nearest_sums(chiral_quantum_each, max_total=Fraction(6), limit=12),
    "interpretation": [
        "The corrected total energy ledger is 64*pi^2, not 24*pi^2.",
        "The all-ADE total quantum has exactly one small solution: three A2 bubbles, since 3*(3-1/3)=8.",
        "But tau=0 imposes a chiral split of 4 units in each Weyl half. No all-ADE multiset has quantum 4; in particular 3*A2 cannot be split into two chiral groups of total 4.",
        "Allowing ALF integer quanta, the only ADE ALE contributions to a single chiral half that can be completed to 4 are none, or two A1 bubbles plus one ALF unit. This is a concrete compatibility gate for collapsed concentration models.",
        "This still is not a collapse contradiction: one must prove which concentration geometries occur (ALE vs ALF/ALG/collapsed), their Weyl chirality assignment, and whether the permitted ALF/A1 patterns are topologically/analytically compatible with the #3(S2xS2) collapse limit.",
    ]
}

out = Path("Sessions/S0910A02/workspace/data/step71_collapse_quantum_diophantine.json")
out.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({
    "output": str(out),
    "chi": chi,
    "total_weyl_energy": "64*pi^2",
    "exact_ADE_total_solutions": len(total_solutions),
    "total_solutions": total_solutions,
    "exact_ADE_chiral_half_solutions": len(chiral_solutions),
    "chiral_ALE_plus_ALF_allowed": chiral_ALE_plus_ALF,
}, indent=2))
