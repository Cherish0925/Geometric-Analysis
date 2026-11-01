"""
Step 53 helper: presentation-compatible inner-symmetry probe for BCGP §6.9.

This is not a computation of Aut(X).  It only checks the most immediate source of
symmetry visible from the displayed S5 spherical systems: inner automorphisms of S5
that preserve the C1 branch system with its distinct orders (2,4,5) and preserve the
C2 branch system while allowing the two order-6 branch values to be exchanged.  Such
a symmetry, if it lifted with suitable base automorphisms, would act on the four A1
nodes.  Absence of such a symmetry does not prove Aut(X) is intransitive, but it
prevents using the simple presentation-level transitivity shortcut.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import step52_lefschetz_obstruction_dimensions as s52  # noqa: E402
import step53_s69_nodes_exact_boundary as s53  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "data" / "step53_s69_symmetry_probe.json"


def subgroup_set(G, e):
    return frozenset(G.cyclic_subgroup(e))


def conj(G, h, e):
    return G.mul(G.mul(h, e), G.inv(h))


def build_node_label(G, C1, C2):
    P1 = s53.branch_points_with_involution(G, C1)
    P2 = s53.branch_points_with_involution(G, C2)
    pairs = []
    for key1, p in P1.items():
        for key2, q in P2.items():
            if p.involution == q.involution:
                pairs.append((key1, key2))
    pair_set = set(pairs)
    node_label = {}
    node_data = []
    unseen = set(pairs)
    label = 0
    while unseen:
        start = next(iter(unseen))
        label += 1
        orbit = set()
        frontier = [start]
        while frontier:
            key1, key2 = frontier.pop()
            if (key1, key2) in orbit:
                continue
            orbit.add((key1, key2))
            p = P1[key1]
            q = P2[key2]
            for g in G.elements:
                p2 = s53.act_on_branch_point(G, g, p, P1)
                q2 = s53.act_on_branch_point(G, g, q, P2)
                nk = ((p2.branch_index, p2.coset), (q2.branch_index, q2.coset))
                if nk in pair_set and nk not in orbit:
                    frontier.append(nk)
        for z in orbit:
            node_label[z] = label
        rep = next(iter(orbit))
        node_data.append({
            "raw_label": label,
            "size": len(orbit),
            "C1_indices": sorted({P1[k1].branch_index for k1, _ in orbit}),
            "C2_indices": sorted({P2[k2].branch_index for _, k2 in orbit}),
            "C1_orders": sorted({P1[k1].branch_order for k1, _ in orbit}),
            "C2_orders": sorted({P2[k2].branch_order for _, k2 in orbit}),
            "sample_involution": s53.elem_str(P1[rep[0]].involution),
        })
        unseen -= orbit
    return P1, P2, pairs, node_label, node_data


def induced_node_permutation(G, h, P1, P2, node_label):
    perm = {}
    for pair, lab in node_label.items():
        p = P1[pair[0]]
        q = P2[pair[1]]
        p2 = s53.act_on_branch_point(G, h, p, P1)
        q2 = s53.act_on_branch_point(G, h, q, P2)
        nk = ((p2.branch_index, p2.coset), (q2.branch_index, q2.coset))
        perm[lab] = node_label[nk]
    return tuple(perm[i] for i in sorted(perm))


def main():
    row = next(r for r in s52.rows() if r.label == "6.9 K2=4 G=S5")
    G = row.group
    S1 = row.C1.branch
    S2 = row.C2.branch
    C1_subs = [subgroup_set(G, e) for e in S1]
    C2_subs = [subgroup_set(G, e) for e in S2]

    # Because C1 branch orders are (2,4,5), a presentation automorphism preserving
    # the orbifold labels must fix the three C1 branch values individually.  For C2
    # of type (3,6,6), it may fix the order-3 value and swap the two order-6 values.
    candidates = []
    for h in G.elements:
        if any(subgroup_set(G, conj(G, h, e)) != H for e, H in zip(S1, C1_subs)):
            continue
        if subgroup_set(G, conj(G, h, S2[0])) != C2_subs[0]:
            continue
        image_6 = {subgroup_set(G, conj(G, h, S2[1])), subgroup_set(G, conj(G, h, S2[2]))}
        if image_6 != {C2_subs[1], C2_subs[2]}:
            continue
        candidates.append(h)

    P1, P2, pairs, node_label, node_data = build_node_label(G, S1, S2)
    candidate_actions = []
    for h in candidates:
        candidate_actions.append({
            "element": s53.elem_str(h),
            "node_permutation_raw_labels": induced_node_permutation(G, h, P1, P2, node_label),
        })

    data = {
        "row": row.label,
        "caution": "This probes only inner automorphisms visible from the S5 quotient presentation, not the full automorphism group of X.",
        "C1_order_pattern": [G.order(e) for e in S1],
        "C2_order_pattern": [G.order(e) for e in S2],
        "node_data_raw_labels": node_data,
        "candidate_count": len(candidates),
        "candidate_actions": candidate_actions,
        "interpretation": (
            "The strict presentation-compatible inner normalizer is trivial if candidate_count=1 "
            "and the only action is the identity permutation. Then the simple node-transitivity "
            "argument cannot be invoked from the displayed quotient data; computing beta remains "
            "the relevant next deformation-theoretic task."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(data, indent=2))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
