#!/usr/bin/env python3
"""Step 95: exact transfer algebra, ADE-to-diagonal lattice screen, and D-block thresholds.

Scientific purpose
------------------
This script independently checks the algebra in Step 94 and performs a
finite, exact search for simple-root embeddings into the norm-two roots of
the standard positive diagonal lattice I_k (equivalently into -I_k after
changing sign).  It also enumerates every partition of 2 <= k <= 40 into
D-block ranks and computes the exact finite-A threshold imposed by the
transferred mixed-curvature inequality.

The root search uses only integer vectors with exactly two nonzero entries,
each equal to +/-1.  These are all norm-two vectors of I_k.  Coordinates are
introduced canonically: because the Dynkin graph is connected and nodes are
added away from a chosen central node, a new simple root can introduce at
most one new coordinate; that coordinate is assigned the next label and its
first sign is fixed.  Thus a negative result is exhaustive modulo signed
coordinate permutations, not a random search.

Run from the user root:
  qiushi-geometry env core python \
    Sessions/S1003A02/workspace/scripts/step95_filler_lattice_screen.py

Output:
  Sessions/S1003A02/workspace/data/step95/filler_lattice_screen.json
"""
from __future__ import annotations

import hashlib
import json
import math
import platform
import sys
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import sympy as sp


# ---------------------------------------------------------------------------
# Exact symbolic transfer algebra
# ---------------------------------------------------------------------------

def symbolic_checks():
    x, T, A, k, c2, Cp, Cm, kb, Scx, Srev = sp.symbols(
        "x T A k c2 Cp Cm kb Scx Srev", nonnegative=True
    )
    F = (sp.sqrt(8 * x) + sp.sqrt(T - x)) ** 2
    tangent_gap = 9 * x + 3 * T - F
    square_gap = 2 * (sp.sqrt(T - x) - sp.sqrt(2 * x)) ** 2

    # T_+ = A-k+C_+, T_- = 4c2-A+5k+C_-.
    host_expr = sp.expand(9 * (4 * c2 - A + 5 * k + Cm)
                          + 3 * (A - k + Cp) - (6 * A + Cp))
    host_target = 9 * Cm + 2 * Cp + 42 * k + 12 * (3 * c2 - A)

    # Ball-quotient budget after C_-=-4[(k-k_b)+S_cx], C_+=-4S_rev.
    ball_screen = sp.expand(
        9 * (-4 * ((k - kb) + Scx)) + 2 * (-4 * Srev) + 42 * k
    )
    ball_screen_target = 6 * k + 36 * kb - 36 * Scx - 8 * Srev

    # Simplify beta using y=sqrt(1-3k/A).
    y = sp.symbols("y", nonnegative=True)
    beta_y_raw = sp.simplify(
        ((A / 3 + k) - A * (4 - y) ** 2 / 27) / 4
    ).subs(A, 3 * k / (1 - y ** 2))
    beta_y = sp.factor(beta_y_raw)
    beta_target = k * (5 * y + 1) / (18 * (1 + y))

    # Series in A^{-1}; use t=k/A.
    t = sp.symbols("t")
    beta_over_k = (5 * sp.sqrt(1 - 3 * t) + 1) / (
        18 * (1 + sp.sqrt(1 - 3 * t))
    )
    beta_series = sp.series(beta_over_k, t, 0, 5)

    checks = {
        "tangent_square_identity": sp.simplify(tangent_gap - square_gap) == 0,
        "host_coefficient_identity": sp.simplify(host_expr - host_target) == 0,
        "ball_budget_identity": sp.simplify(ball_screen - ball_screen_target) == 0,
        "beta_y_identity": sp.simplify(beta_y - beta_target) == 0,
    }
    assert all(checks.values()), checks

    return {
        "checks": checks,
        "F_expanded": str(sp.expand(F)),
        "supporting_plane_exact_identity":
            "9*x + 3*T - F(x,T) = 2*(sqrt(T-x)-sqrt(2*x))^2",
        "supporting_plane_equality": "T=3*x (inside 0<=x<=T)",
        "host_expansion": str(host_expr),
        "host_target": str(host_target),
        "ball_budget_expansion": str(ball_screen),
        "ball_budget_equivalent":
            "Scx + (2/9)*Srev <= k/6 + kb",
        "beta_y_simplified": str(beta_y),
        "beta_series_over_k_t_equals_k_over_A": str(beta_series),
    }


# ---------------------------------------------------------------------------
# Exact roots and deterministic exhaustive embedding search
# ---------------------------------------------------------------------------

def dot(u, v):
    """Dot product of sparse roots represented as sorted ((index, sign),...)."""
    du = dict(u)
    return sum(s * du.get(i, 0) for i, s in v)


def dense(root, n):
    out = [0] * n
    for i, s in root:
        out[i] = s
    return out


def dynkin_star(arm_lengths):
    """Tree with central node 0 and paths of the specified positive lengths."""
    adj = [set()]
    order = [0]
    arms = []
    for length in arm_lengths:
        prev = 0
        arm = []
        for _ in range(length):
            node = len(adj)
            adj.append(set())
            adj[prev].add(node)
            adj[node].add(prev)
            arm.append(node)
            prev = node
        arms.append(arm)
    # Breadth by distance keeps each new node attached to the assigned set.
    for depth in range(max(arm_lengths)):
        for arm in arms:
            if depth < len(arm):
                order.append(arm[depth])
    return adj, order


def dynkin_A(rank):
    # Choose an interior node as root when possible, then BFS.
    adj = [set() for _ in range(rank)]
    for i in range(rank - 1):
        adj[i].add(i + 1)
        adj[i + 1].add(i)
    root = rank // 2
    order = []
    queue = [root]
    seen = {root}
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in sorted(adj[u]):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return adj, order


def adj_order_from_gram(gram):
    n = len(gram)
    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if gram[i][j] == -1:
                adj[i].add(j)
                adj[j].add(i)
            elif gram[i][j] != 0:
                raise ValueError("not a simply-laced Gram matrix")
    root = max(range(n), key=lambda i: len(adj[i]))
    order, queue, seen = [], [root], {root}
    while queue:
        u = queue.pop(0)
        order.append(u)
        for v in sorted(adj[u]):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return adj, order


def dynkin_D(rank):
    if rank == 2:
        return [set(), set()], [0, 1]
    if rank == 3:
        return dynkin_A(3)
    rows = explicit_D_witness(rank)
    gram = [[sum(a * b for a, b in zip(rows[i], rows[j]))
             for j in range(rank)] for i in range(rank)]
    return adj_order_from_gram(gram)


def dynkin_E(rank):
    assert rank in (6, 7, 8)
    # Arms from the trivalent node: E6=(2,2,1), E7=(3,2,1), E8=(4,2,1).
    return dynkin_star([1, 2, rank - 4])


def cartan_from_adj(adj):
    n = len(adj)
    return [[2 if i == j else (-1 if j in adj[i] else 0)
             for j in range(n)] for i in range(n)]


def candidate_roots(used, max_coords):
    """Roots on used coordinates, optionally introducing coordinate `used`.

    A newly introduced coordinate has sign +1, quotienting its independent
    sign flip.  Since candidate roots are adjacent to the assigned connected
    set, no root with two new coordinates can occur.
    """
    top = used + (1 if used < max_coords else 0)
    for i in range(top):
        for j in range(i + 1, top):
            introduces = (j == used)  # i<j and there is only one new label.
            for si in (-1, 1):
                for sj in (-1, 1):
                    if introduces and sj != 1:
                        continue
                    yield ((i, si), (j, sj)), introduces


def embedding_search(adj, order, max_coords, stop_after_first=True):
    """Exact canonical DFS for a simple-root Gram embedding in I_max_coords."""
    n = len(adj)
    assert order[0] in range(n)
    assigned = {order[0]: ((0, 1), (1, -1))}
    counters = {
        "dfs_nodes": 0,
        "candidate_roots_tested": 0,
        "gram_compatible_candidates": 0,
        "complete_solutions": 0,
        "max_used_coordinates": 2,
    }
    first_solution = None

    def dfs(pos, used):
        nonlocal first_solution
        counters["dfs_nodes"] += 1
        counters["max_used_coordinates"] = max(counters["max_used_coordinates"], used)
        if pos == n:
            counters["complete_solutions"] += 1
            if first_solution is None:
                first_solution = {i: assigned[i] for i in range(n)}
            return stop_after_first

        node = order[pos]
        # Connected BFS order guarantees at least one assigned neighbour.
        assert any(v in assigned for v in adj[node])
        for root, introduces in candidate_roots(used, max_coords):
            counters["candidate_roots_tested"] += 1
            ok = True
            for other, other_root in assigned.items():
                wanted = -1 if other in adj[node] else 0
                if dot(root, other_root) != wanted:
                    ok = False
                    break
            if not ok:
                continue
            counters["gram_compatible_candidates"] += 1
            assigned[node] = root
            should_stop = dfs(pos + 1, used + int(introduces))
            del assigned[node]
            if should_stop:
                return True
        return False

    dfs(1, 2)
    if first_solution is not None:
        matrix = [dense(first_solution[i], max_coords) for i in range(n)]
        gram = [[sum(a * b for a, b in zip(matrix[i], matrix[j]))
                 for j in range(n)] for i in range(n)]
        assert gram == cartan_from_adj(adj)
    else:
        matrix = None
        gram = None
    return {
        "max_coordinates": max_coords,
        "order": order,
        "found": first_solution is not None,
        "counters": counters,
        "simple_roots_rows": matrix,
        "verified_gram": gram,
    }


def explicit_D_witness(rank):
    """Standard D_r simple roots in r coordinates; D2/D3 conventions included."""
    if rank == 2:
        return [[1, -1], [1, 1]]
    if rank == 3:
        # A3=D3, standard A3 chain in three-coordinate D3 form.
        return [[1, -1, 0], [0, 1, -1], [-1, -1, 0]]
    rows = []
    for i in range(rank - 1):
        row = [0] * rank
        row[i] = 1
        row[i + 1] = -1
        rows.append(row)
    row = [0] * rank
    row[rank - 2] = 1
    row[rank - 1] = 1
    rows.append(row)
    return rows


def root_embedding_checks():
    out = {
        "search_method": (
            "deterministic canonical DFS over all norm-two roots +/-e_i+/-e_j; "
            "first simple root fixed by a signed permutation; each new coordinate "
            "gets the next label and positive first sign"
        ),
        "irreducible_tests": {},
        "explicit_D_witnesses": {},
    }

    # A3 is the unique irreducible A_r compression to r coordinates.  Test
    # A_r in r coordinates through rank 12, plus existence in r+1 coordinates.
    for r in range(2, 13):
        adj, order = dynkin_A(r)
        same_rank = embedding_search(adj, order, r)
        natural = embedding_search(adj, order, r + 1)
        key = f"A{r}"
        out["irreducible_tests"][key] = {
            "in_I_rank": same_rank,
            "in_I_rank_plus_1": natural,
            "expected_min_slots": 3 if r in (2, 3) else r + 1,
        }
        # A2 naturally also needs 3; A3 compresses to 3.
        assert natural["found"]
        if r == 3:
            assert same_rank["found"]
        else:
            assert not same_rank["found"]

    # D_r uses exactly r coordinates.
    for r in range(2, 13):
        rows = explicit_D_witness(r)
        gram = [[sum(a * b for a, b in zip(rows[i], rows[j]))
                 for j in range(r)] for i in range(r)]
        adj, _ = dynkin_D(r)
        assert gram == cartan_from_adj(adj)
        out["explicit_D_witnesses"][f"D{r}"] = {
            "simple_roots_rows": rows,
            "verified_gram": gram,
        }

    # Any connected rank-r embedding uses at most r+1 coordinates under a
    # connected node ordering, so these searches cover every ambient I_k.
    for r in (6, 7, 8):
        adj, order = dynkin_E(r)
        search = embedding_search(adj, order, r + 1, stop_after_first=True)
        assert not search["found"]
        out["irreducible_tests"][f"E{r}"] = {
            "all_ambient_dimensions_reduced_to": r + 1,
            "search": search,
            "conclusion": "no isometric root-lattice embedding into any I_k",
        }

    # Stable digest makes accidental changes to the finite certificate visible.
    digest_input = json.dumps(out, sort_keys=True, separators=(",", ":")).encode()
    out["sha256_before_digest_field"] = hashlib.sha256(digest_input).hexdigest()
    return out


# ---------------------------------------------------------------------------
# D-block partition enumeration and exact threshold formula
# ---------------------------------------------------------------------------

def d_cost(a):
    if a == 2:
        return Fraction(1, 1)       # two A1/EH blocks sharing two slots
    if a == 3:
        return Fraction(3, 4)       # A3=D3, |Gamma|=4
    assert a >= 4
    return Fraction(4 * a - 9, 4 * a - 8)  # 1 - 1/[4(a-2)]


def partitions_min_part(n, min_part=2):
    """Nondecreasing integer partitions of n with all parts >= min_part."""
    def rec(rem, lo, prefix):
        if rem == 0:
            yield tuple(prefix)
            return
        for a in range(lo, rem + 1):
            prefix.append(a)
            yield from rec(rem - a, a, prefix)
            prefix.pop()
    yield from rec(n, min_part, [])


def frac_obj(q):
    return {
        "numerator": q.numerator,
        "denominator": q.denominator,
        "decimal": float(q),
        "str": str(q),
    }


def ceil_fraction(q):
    return -((-q.numerator) // q.denominator)


def first_multiple_9_for_open_range(k, Acrit):
    """Smallest 9Z value satisfying A>3k and A>=Acrit."""
    n = max(ceil_fraction(Acrit / 9), (3 * k) // 9 + 1)
    A = 9 * n
    assert A > 3 * k and Fraction(A, 1) >= Acrit
    return A


def threshold_for_cost(k, cost):
    asym = Fraction(k, 6)
    wall = Fraction(k, 18)
    if cost >= asym:
        return {
            "finite_A_possible": False,
            "reason": "cost >= k/6 while beta(k,A) < k/6 for finite A",
            "asymptotic_equality": cost == asym,
        }
    if cost <= wall:
        Acrit = Fraction(3 * k, 1)
        ycrit = Fraction(0, 1)
        regime = "already allowed at the wall limit"
    else:
        rratio = Fraction(18, k) * cost
        # beta = k(5y+1)/[18(1+y)], y=sqrt(1-3k/A).
        ycrit = (rratio - 1) / (5 - rratio)
        assert 0 < ycrit < 1
        Acrit = Fraction(3 * k, 1) / (1 - ycrit * ycrit)
        regime = "unique threshold in A>3k"
    return {
        "finite_A_possible": True,
        "regime": regime,
        "ycrit": frac_obj(ycrit),
        "Acrit": frac_obj(Acrit),
        "smallest_A_multiple_of_9": first_multiple_9_for_open_range(k, Acrit),
    }


def d_partition_thresholds(kmax=40):
    all_viable = []
    summaries = {}
    exhaustive_counts = {}

    for k in range(2, kmax + 1):
        total = 0
        viable = []
        rejected_gt = 0
        rejected_eq = 0
        for part in partitions_min_part(k):
            total += 1
            cost = sum((d_cost(a) for a in part), Fraction(0, 1))
            th = threshold_for_cost(k, cost)
            if not th["finite_A_possible"]:
                if th["asymptotic_equality"]:
                    rejected_eq += 1
                else:
                    rejected_gt += 1
                continue
            row = {
                "k": k,
                "blocks": list(part),
                "cost": frac_obj(cost),
                "surplus_k_over_6_minus_cost": frac_obj(Fraction(k, 6) - cost),
                "threshold": th,
                "contains_small_block_D2_to_D5": any(a <= 5 for a in part),
                "mixed": len(part) > 1,
            }
            viable.append(row)
            all_viable.append(row)

        viable.sort(key=lambda z: (
            Fraction(z["threshold"]["Acrit"]["numerator"],
                     z["threshold"]["Acrit"]["denominator"]),
            z["blocks"],
        ))
        exhaustive_counts[str(k)] = {
            "all_partitions": total,
            "finite_A_viable": len(viable),
            "rejected_cost_gt_k_over_6": rejected_gt,
            "rejected_cost_eq_k_over_6": rejected_eq,
        }
        summaries[str(k)] = {
            "first_five_by_real_threshold": viable[:5],
            "last_five_by_real_threshold": viable[-5:] if viable else [],
        }

    first_viable_k = min(row["k"] for row in all_viable)
    first_mixed_k = min(row["k"] for row in all_viable if row["mixed"])
    first_with_small = {}
    for a in range(2, 6):
        rows = [r for r in all_viable if a in r["blocks"]]
        if rows:
            mk = min(r["k"] for r in rows)
            first_with_small[f"D{a}"] = [r for r in rows if r["k"] == mk]

    singled = {}
    for a in range(6, min(kmax, 12) + 1):
        rows = [r for r in all_viable if r["blocks"] == [a]]
        assert len(rows) == 1
        singled[f"D{a}"] = rows[0]

    first_mixed = [r for r in all_viable if r["mixed"] and r["k"] == first_mixed_k]

    # The theorem "some block has rank >=6" is checked termwise.
    small_block_differences = {
        f"D{a}": frac_obj(d_cost(a) - Fraction(a, 6)) for a in range(2, 6)
    }
    assert all(d_cost(a) > Fraction(a, 6) for a in range(2, 6))

    # Save all finite-A survivors.  The generator itself covers every rejected row.
    all_viable.sort(key=lambda z: (z["k"], z["blocks"]))
    return {
        "kmax": kmax,
        "cost_definition": {
            "D2": "1 (two A1/Eguchi-Hanson components in a D2 slot)",
            "D3": "3/4 (A3=D3)",
            "Da_a_ge_4": "1 - 1/[4(a-2)]",
        },
        "beta_exact_reparameterization":
            "beta=k(5y+1)/[18(1+y)], y=sqrt(1-3k/A)",
        "threshold_solution":
            "r=18*cost/k; ycrit=(r-1)/(5-r); Acrit=3k/(1-ycrit^2)",
        "small_block_cost_minus_rank_over_6": small_block_differences,
        "first_viable_k": first_viable_k,
        "first_mixed_k": first_mixed_k,
        "first_mixed_rows": first_mixed,
        "first_viable_rows_containing_each_small_block": first_with_small,
        "single_block_D6_through_D12": singled,
        "exhaustive_counts": exhaustive_counts,
        "per_k_extremal_rows": summaries,
        "all_finite_A_viable_partitions": all_viable,
    }


def main():
    result = {
        "metadata": {
            "script": str(Path(__file__).as_posix()),
            "python": sys.version,
            "platform": platform.platform(),
            "arithmetic": "SymPy exact symbolic algebra and Python Fraction",
            "scope": (
                "Necessary curvature/lattice arithmetic only; no surviving row "
                "constructs a compact orbifold or an Einstein metric."
            ),
        },
        "symbolic_transfer": symbolic_checks(),
        "root_lattice_screen": root_embedding_checks(),
        "D_block_thresholds": d_partition_thresholds(40),
    }
    out = Path(__file__).resolve().parents[1] / "data" / "step95" / "filler_lattice_screen.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(out),
        "size_bytes": out.stat().st_size,
        "symbolic_checks": result["symbolic_transfer"]["checks"],
        "root_digest": result["root_lattice_screen"]["sha256_before_digest_field"],
        "first_viable_k": result["D_block_thresholds"]["first_viable_k"],
        "first_mixed_k": result["D_block_thresholds"]["first_mixed_k"],
        "viable_partition_count": len(result["D_block_thresholds"]["all_finite_A_viable_partitions"]),
    }, indent=2))


if __name__ == "__main__":
    main()
