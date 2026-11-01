#!/usr/bin/env python3
"""Step 91: checkerboard relative radial equation reduction.

For the mixed diagonal assignment eps=(+,-,-,+) in node order NN,NS,SN,SS,
the relative mixed-minus-all-same linear pairwise radial equation is
    Delta_i = t_i sum_j t_j^2 (eps_i eps_j - 1) K_ij^{11}.
This script records exactly which node pairs survive and the reduction to one
adjacent coefficient after applying node-frame normalized exchange symmetries.
"""
from __future__ import annotations

import json
import pathlib

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

nodes = ["NN", "NS", "SN", "SS"]
eps = {"NN": 1, "NS": -1, "SN": -1, "SS": 1}

def differ_one_factor(a: str, b: str) -> bool:
    return sum(aa != bb for aa, bb in zip(a, b)) == 1

def same_orbit_companion(a: str, b: str) -> bool:
    return sum(aa != bb for aa, bb in zip(a, b)) == 2

pair_table = []
radial_terms = {}
for i in nodes:
    terms = []
    for j in nodes:
        factor = eps[i] * eps[j] - 1
        row = {
            "receiver": i,
            "source": j,
            "epsilon_i_epsilon_j_minus_1": factor,
            "self": i == j,
            "adjacent_one_factor_difference": differ_one_factor(i, j),
            "same_orbit_diagonal_companion_two_factor_difference": same_orbit_companion(i, j),
            "survives": factor != 0,
        }
        pair_table.append(row)
        if factor:
            terms.append({"source": j, "coefficient": factor, "monomial": f"t_{i} t_{j}^2 K_{i},{j}"})
    radial_terms[i] = terms

# If frame-normalized exchange symmetries identify all adjacent K_ij with K_adj,
# then Delta_i=-2 t_i sum_{j~i} t_j^2 K_adj.
radial_reduced = {i: f"Delta_{i} = -2 t_{i} ({' + '.join('t_'+j+'^2' for j in nodes if differ_one_factor(i,j))}) K_adj" for i in nodes}

# Equal scale specialization is not the full radial system, but records the common value.
equal_scale = {i: "Delta_i = -4 t^3 K_adj" for i in nodes}

results = {
    "step": 91,
    "scope": "checkerboard mixed-minus-all-same per-receiver radial equation reduction",
    "nodes": nodes,
    "epsilon_checkerboard": [eps[n] for n in nodes],
    "formula": "Delta_i=t_i sum_j t_j^2 (epsilon_i epsilon_j - 1) K_ij^{11}",
    "pair_table": pair_table,
    "radial_terms_before_exchange_symmetry": radial_terms,
    "surviving_pairs": [r for r in pair_table if r["survives"]],
    "vanishing_reason": {
        "self_terms": "epsilon_i^2-1=0",
        "same_orbit_diagonal_companions": "NN-SS and NS-SN have equal epsilon product +1, so epsilon_i epsilon_j-1=0",
        "only_adjacent_pairs_survive": True,
    },
    "after_frame_normalized_exchange_symmetries": {
        "hypothesis": "L, factor exchange, and node-frame normalizations identify all adjacent K_ij^{11} with one coefficient K_adj; this identification must be applied before replacing the radial system by one scalar.",
        "reduced_per_receiver_equations": radial_reduced,
        "equal_scale_specialization": equal_scale,
        "warning": "The sum over receivers is not automatically equivalent to solving the radial system; the per-receiver equations are the geometric objects.",
    },
}

outpath = DATA_DIR / "step91_checkerboard_radial_reduction.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2)

print(json.dumps(results, indent=2))
print(f"Wrote {outpath}")
