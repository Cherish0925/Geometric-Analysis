#!/usr/bin/env python3
"""
Step 83: coefficient bookkeeping for the all-same KE control path versus the
opposite-corner mixed chirality path.

The point is purely algebraic/combinatorial.  It records which pair types enter
one equal-scale radial projection when local self terms and same-geometry Green
responses are normalized consistently.

If a matched degenerating KE degree-4 del Pezzo family in the same gluing chart
is established, the all-same row supplies the relation
    s + d_same + 2 c_same = 0
for the same radial functional.  The opposite-corner mixed row then has
    s + d_same + 2 c_opposite
so the difference is 2(c_opposite-c_same).  This is conditional on matched
normalization and expansion order; the script proves only the coefficient ledger.
"""

import json
from pathlib import Path

nodes = {
    "NN": (+1, +1),
    "NS": (+1, -1),
    "SN": (-1, +1),
    "SS": (-1, -1),
}

def relation(a, b):
    pa, qa = nodes[a], nodes[b]
    d = int(pa[0] != qa[0]) + int(pa[1] != qa[1])
    if d == 0:
        return "self"
    if d == 1:
        return "adjacent"
    return "diagonal"

def row(chirality):
    out = {}
    for r in nodes:
        terms = []
        # local self response, independent of chirality pattern if the local model
        # and radial insertion direction are matched.
        terms.append({"source": r, "relation": "self", "same_chirality": True, "symbol": "s"})
        for src in nodes:
            if src == r:
                continue
            rel = relation(r, src)
            same = chirality[src] == chirality[r]
            if rel == "diagonal" and same:
                sym = "d_same"
            elif rel == "diagonal" and not same:
                sym = "d_opposite"
            elif rel == "adjacent" and same:
                sym = "c_same"
            elif rel == "adjacent" and not same:
                sym = "c_opposite"
            else:
                raise RuntimeError
            terms.append({"source": src, "relation": rel, "same_chirality": same, "symbol": sym})
        out[r] = terms
    return out

def collect_symbols(terms):
    counts = {}
    for t in terms:
        counts[t["symbol"]] = counts.get(t["symbol"], 0) + 1
    return counts

def expression(counts):
    order = ["s", "d_same", "d_opposite", "c_same", "c_opposite"]
    parts = []
    for k in order:
        n = counts.get(k, 0)
        if n == 0:
            continue
        if n == 1:
            parts.append(k)
        else:
            parts.append(f"{n}*{k}")
    return " + ".join(parts) if parts else "0"

all_same_plus = {n: "+" for n in nodes}
# opposite-corner mixed: diagonal orbits same sign, adjacent nodes opposite sign
opposite_corner = {"NN": "+", "SS": "+", "NS": "-", "SN": "-"}
# single-factor antipodal L: (s1,s2)->(-s1,s2)
def L_node(n):
    s1, s2 = nodes[n]
    target = (-s1, s2)
    for name, pair in nodes.items():
        if pair == target:
            return name
    raise RuntimeError

def transform_assignment(chirality):
    return {L_node(n): chirality[n] for n in nodes}

rows = {
    "all_same_plus": row(all_same_plus),
    "opposite_corner_mixed": row(opposite_corner),
}
receiver = "NN"
all_counts = collect_symbols(rows["all_same_plus"][receiver])
mix_counts = collect_symbols(rows["opposite_corner_mixed"][receiver])

results = {
    "nodes": nodes,
    "L_node_map": {n: L_node(n) for n in nodes},
    "chirality_assignments": {
        "all_same_plus": all_same_plus,
        "opposite_corner_mixed": opposite_corner,
    },
    "L_transformed_assignments_without_orientation_swap": {
        "all_same_plus": transform_assignment(all_same_plus),
        "opposite_corner_mixed": transform_assignment(opposite_corner),
    },
    "orientation_reversal_effect": "L reverses four-dimensional orientation. If chirality labels are tied to SD/ASD orientation, L changes +<->- while exchanging node orbits.",
    "L_compatibility": {
        "all_same_plus": "not preserved as an oriented chirality assignment: orientation reversal turns all + into all -, not the same assignment on a tau=-4 filling",
        "opposite_corner_mixed": "preserved after the orientation-induced chirality swap: NN/SS + are exchanged with NS/SN -",
    },
    "equal_scale_radial_terms_at_receiver_NN": {
        "all_same_plus_terms": rows["all_same_plus"][receiver],
        "opposite_corner_mixed_terms": rows["opposite_corner_mixed"][receiver],
        "all_same_expression": expression(all_counts),
        "mixed_expression": expression(mix_counts),
        "conditional_control_relation": "s + d_same + 2*c_same = 0 if a matched same-normalization all-same KE degeneration supplies a zero of the same radial functional at this expansion layer",
        "conditional_mixed_coefficient_using_control": "2*(c_opposite - c_same)",
    },
    "scope": "This ledger does not prove the matched KE control or compute c_opposite-c_same. It identifies the exact cancellation target for a projected chirality-response calculation.",
}

out = Path("Sessions/S0910A01/workspace/data/step83_chirality_control_ledger.json")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(results, indent=2), encoding="utf-8")
print(json.dumps(results["equal_scale_radial_terms_at_receiver_NN"], indent=2))
print(json.dumps(results["L_compatibility"], indent=2))
print(f"\nWrote {out}")
