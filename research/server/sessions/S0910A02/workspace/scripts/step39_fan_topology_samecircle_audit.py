#!/usr/bin/env python3
"""Step 39 addendum: topology + same-circle audit for known toric calibration fans.

Checks that the known m=6 toric KE hexagon is topologically dP3 (odd form,
signature -2) whereas the alternating spin m=6 fan is consistent with
#2(S^2 x S^2) (even unimodular, signature 0).  This prevents confusing the
known dP3 hexagon calibration with the unknown spin hexagon stress test.
"""
import json, math, os
from collections import defaultdict
import sympy as sp
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
WORKSPACE = os.path.dirname(HERE)
OUT = os.path.join(WORKSPACE, "data", "step39_fan_topology_samecircle_audit.json")
os.makedirs(os.path.dirname(OUT), exist_ok=True)


def det2(u, v):
    return int(u[0] * v[1] - u[1] * v[0])


def canonical_pm(v):
    a, b = v
    g = math.gcd(abs(a), abs(b)) or 1
    a, b = a // g, b // g
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return (a, b)


def same_classes(labels):
    d = defaultdict(list)
    for i, v in enumerate(labels):
        d[canonical_pm(v)].append(i + 1)
    return {str(k): inds for k, inds in d.items() if len(inds) > 1}


def build_Q(lams):
    m = len(lams)
    Q = sp.zeros(m)
    for i in range(m):
        j = (i + 1) % m
        d = det2(lams[i], lams[j])
        if abs(d) != 1:
            raise ValueError(f"non-unimodular adjacent pair {i},{j}: det={d}")
        Q[i, j] = Q[j, i] = sp.Rational(1, d)
    q = sp.symbols(f"q0:{m}")
    for i in range(m):
        Q[i, i] = q[i]
    eqs = []
    for a in range(2):
        row = sp.Matrix([lams[i][a] for i in range(m)]).T
        eqs += list(row * Q)
    sol = sp.solve(eqs, q, dict=True)
    if not sol:
        raise ValueError("no self-intersection solution")
    return sp.Matrix(Q.subs(sol[0]))


def eliminate_basis(lams):
    m = len(lams)
    pair = None
    for i in range(m):
        for j in range(i + 1, m):
            if abs(det2(lams[i], lams[j])) == 1:
                pair = (i, j)
                break
        if pair:
            break
    free = [r for r in range(m) if r not in pair]
    return pair, free


def inertia(B):
    A = np.array([[float(sp.N(B[i, j], 40)) for j in range(B.cols)] for i in range(B.rows)])
    A = (A + A.T) / 2.0
    vals = np.linalg.eigvalsh(A)
    pos = int(np.sum(vals > 1e-8)); neg = int(np.sum(vals < -1e-8)); zero = len(vals) - pos - neg
    return pos, neg, zero, vals.tolist()


def topology_report(name, labels, expected):
    Q = build_Q(labels)
    pair, free = eliminate_basis(labels)
    B = sp.Matrix([[Q[i, j] for j in free] for i in free])
    pos, neg, zero, eigs = inertia(B)
    even = all(int(B[i, i]) % 2 == 0 for i in range(B.rows))
    det_abs = abs(int(B.det())) if B.rows else 1
    signature = pos - neg
    if det_abs == 1 and even and signature == 0:
        identified = f"even unimodular indefinite rank {B.rows}: consistent with #{B.rows//2}(S2xS2)"
    elif det_abs == 1 and not even:
        identified = f"odd unimodular form with b+={pos}, b-={neg}: connected sum of {pos} CP2 and {neg} CPbar (orientation convention)"
    else:
        identified = "not identified by simple unimodular form test"
    return {
        "name": name,
        "expected": expected,
        "labels": labels,
        "m": len(labels),
        "adjacent_dets": [det2(labels[i], labels[(i + 1) % len(labels)]) for i in range(len(labels))],
        "same_unoriented_classes": same_classes(labels),
        "max_same_circle_count": max(len(v) for v in (lambda dd: dd)(defaultdict(list)).values()) if False else max([1] + [len(v) for v in same_classes(labels).values()]),
        "eliminated_pair": pair,
        "free_indices": free,
        "intersection_matrix": [[str(B[i, j]) for j in range(B.cols)] for i in range(B.rows)],
        "rank": int(B.rank()),
        "det_abs": det_abs,
        "even_form": even,
        "b_plus": pos,
        "b_minus": neg,
        "signature": signature,
        "eigenvalues_numeric": eigs,
        "identified_form": identified,
    }


def main():
    cases = [
        ("CP2 FS", [(1, 0), (0, 1), (-1, -1)], "CP2"),
        ("S2xS2 product rectangle", [(1, 0), (0, 1), (-1, 0), (0, -1)], "#1(S2xS2)"),
        ("F1 Page fan", [(1, 0), (0, 1), (-1, 1), (0, -1)], "CP2#CPbar"),
        ("dP2 CLW fan", [(1, 0), (0, 1), (-1, 0), (-1, -1), (0, -1)], "CP2#2CPbar"),
        ("dP3 toric KE hexagon", [(1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1)], "CP2#3CPbar, known KE"),
        ("alternating spin hexagon", [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 0), (0, 1)], "#2(S2xS2) candidate, unknown Einstein"),
    ]
    reports = [topology_report(*case) for case in cases]
    out = {
        "title": "Step 39 fan topology and same-circle audit",
        "scope": "Calibration for compact toric period-defect route; not a metric construction.",
        "reports": reports,
        "key_distinction": "The known m=6 toric KE hexagon dP3 has three repeated classes of size 2 and an odd form/signature -2; the alternating spin m=6 fan has two classes of size 3 and an even signature-zero form consistent with #2(S2xS2).",
    }
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({
        "output": OUT,
        "summary": [{"name": r["name"], "same": r["same_unoriented_classes"], "form": r["identified_form"], "signature": r["signature"]} for r in reports]
    }, indent=2))

if __name__ == "__main__":
    main()
