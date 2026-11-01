#!/usr/bin/env python3
"""Step 71 follow-up: include non-SU(2) Ricci-flat Kahler ALE class-T quanta.

Suvaina/Wright classification of ALE Ricci-flat Kahler surfaces includes
non-simply-connected quotients of A-type hyperkahler ALE spaces.  For the
cyclic class-T singularity 1/(d n^2)(1,d n m - 1), n>=2, the smoothing has
chi=d and end group order d n^2, hence

    Q_T(d,n) = d - 1/(d n^2).

This script gives an efficient exact case analysis for the chiral target Q=4
when these class-T half-flat ALE atoms are added to the ADE atoms.  It avoids a
large combinations search by using the integer part S=sum chi: if sum Q = T is
integer, then sum reciprocal end terms is S-T and each end term is bounded by
chi/4.
"""
from fractions import Fraction
import json
from pathlib import Path

# Atom types relevant to chiral target Q<=4.  We keep symbolic families for class T.
ade_atoms = [
    {"name": "A1", "chi": 2, "r": Fraction(1, 2), "Q": Fraction(3, 2)},
    {"name": "A2", "chi": 3, "r": Fraction(1, 3), "Q": Fraction(8, 3)},
    {"name": "A3", "chi": 4, "r": Fraction(1, 4), "Q": Fraction(15, 4)},
]

# Case proof for Q=4.
q4_case_analysis = [
    {"integer_parts": "4+1", "max_reciprocal": "1/2", "needed": "1", "status": "impossible"},
    {"integer_parts": "3+2", "max_reciprocal": "5/6", "needed": "1", "status": "impossible"},
    {"integer_parts": "3+1+1", "max_reciprocal": "5/6", "needed": "1", "status": "impossible"},
    {"integer_parts": "2+2+1", "max_reciprocal": "5/4", "needed": "1",
     "refinement": "If both chi=2 atoms are A1, reciprocal contribution already 1 and the chi=1 atom is positive; if at most one A1, max reciprocal <= 1/2+1/8+1/4=7/8.", "status": "impossible"},
    {"integer_parts": "2+1+1+1", "max_reciprocal": "5/4", "needed": "1",
     "refinement": "Only possible large chi=2 atom is A1. Then need three inverse squares to sum 1/2. With one 1/4 left need two squares sum 1/4, impossible; with no 1/4 max is 1/3.", "status": "impossible"},
    {"integer_parts": "1+1+1+1+1", "max_reciprocal": "5/4", "needed": "1",
     "refinement": "Need five integers n_i>=2 with sum 1/n_i^2=1. Fewer than four n_i=2 gives <=3/4+2/9<1; four n_i=2 already sum 1 with a fifth positive, contradiction.", "status": "impossible"},
]

integer_q_le4 = {
    "Q=1": [],
    "Q=2": [],
    "Q=3": [
        {"pattern": "2*A1", "reciprocal_sum": "1", "Q": "3"},
        {"pattern": "A1 + 2*T(d=1,n=2)", "reciprocal_sum": "1/2+1/4+1/4=1", "Q": "3"},
        {"pattern": "4*T(d=1,n=2)", "reciprocal_sum": "4*(1/4)=1", "Q": "3"},
    ],
    "Q=4": [],
}

result = {
    "formula": "Q_T(d,n)=d-1/(d*n^2) for cyclic class-T Ricci-flat Kahler ALE smoothing 1/(d n^2)(1,d n m-1), n>=2",
    "source_anchors": [
        "Knowledge/objects/papers/ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210/object.md, Theorem B and Theorem 2.2",
        "Knowledge/objects/papers/Desingularizations-of-Conformally-Kaehler-Einstein-Orbifolds--8fe1aa31deb8--5b19d560b771/object.md lines 80-88",
        "Knowledge/objects/papers/On-the-classification-of-ALE-Kähler-manifolds--e1a7b4c34fa6--1e136e81370c/object.md lines 29-33",
    ],
    "ADE_atoms_relevant_to_Q_le_4": [
        {"name": a["name"], "chi": a["chi"], "reciprocal": f"{a['r'].numerator}/{a['r'].denominator}", "Q": f"{a['Q'].numerator}/{a['Q'].denominator}"}
        for a in ade_atoms
    ],
    "exact_Q4_with_ADE_plus_classT_half_flat_ALE": {
        "solutions": [],
        "proof": [
            "Every atom has Q=chi-r with chi a positive integer and 0<r<=chi/4.",
            "If the sum is the integer T=4, then R=sum r=S-4, where S=sum chi. The bound R<=S/4 gives S<=16/3, hence S=5.",
            "The listed partitions of S=5 exhaust all possibilities and each is impossible by elementary reciprocal-square bounds.",
        ],
        "case_analysis": q4_case_analysis,
    },
    "integer_half_flat_ALE_totals_le_4_when_ALF_integer_quanta_are_allowed": integer_q_le4,
    "interpretation": [
        "Adding Suvaina/Wright cyclic class-T U(2) Ricci-flat Kahler ALE atoms does not create a half-flat ALE chiral quantum Q=4.",
        "Therefore the Step-71 pure half-flat ALE chiral impossibility survives the largest missing non-SU(2) ALE caveat, provided the concentration models are still Ricci-flat Kahler/half-conformally-flat and atomically assigned to one Weyl half.",
        "When standard half-flat ALF integer quanta are allowed, the ALE part of one chiral half can be 0 or 3 (not only the old ADE pattern 2*A1; class-T patterns also give Q=3), then ALF supplies the remaining 4 or 1 units.",
        "This is still an arithmetic compatibility gate, not a collapse theorem: non-half-flat Ricci-flat bubbles, transition energy, ALG/ALH regions, and topology/attachment remain open.",
    ],
}

out = Path("Sessions/S0910A02/workspace/data/step71_u2_ale_quantum_probe.json")
out.write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({
    "output": str(out),
    "Q4_solutions_ADE_plus_classT": 0,
    "integer_ALE_totals_le4": {k: len(v) for k,v in integer_q_le4.items()},
}, indent=2))
