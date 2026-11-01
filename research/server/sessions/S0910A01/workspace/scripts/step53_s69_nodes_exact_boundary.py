"""
Step 53: BCGP §6.9 local-to-global boundary route-control test.

Purpose
-------
The Step 52 Lefschetz scan found for the BCGP K^2=4, G=S5 row (§6.9)
that

    d = dim H^2(X,T_X^0) = dim H^0(Y,Omega^1_Y \\otimes K_Y)^G = 2.

BCGP's theorem gives 8-K^2=4 A1 nodes.  Hence the local-to-global
boundary map beta: C^4 -> H^2(X,T_X^0) has kernel dimension at least two,
so d>0 by itself does not rule out first-order simultaneous smoothing of
all nodes.  This script does two bounded checks:

1. Recompute d=2 for §6.9 using exact cyclotomic arithmetic in Q(zeta_60),
   avoiding the floating roots of unity used in Step 52.
2. Reconstruct the four A1 node orbits from branch stabilizers and record
   their branch-position categories.  This tests whether a simple symmetry
   argument from the product-quotient presentation can force a full-support
   first-order smoothing direction.

Interpretation
--------------
This script does not compute the actual boundary map beta and does not prove
existence of a Q-Gorenstein smoothing.  It supplies route information: the
next load-bearing object, if this front is pursued, is beta (or beta^*) and
not another sufficient-condition scan.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

import sympy as sp

# Reuse the verified group/coset machinery and BCGP row transcription from Step 52.
import sys
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))
import step52_lefschetz_obstruction_dimensions as s52  # noqa: E402

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step53_s69_nodes_exact_boundary.json"


# ---------------------------------------------------------------------------
# Exact cyclotomic arithmetic in Q[z]/Phi_60(z).
# ---------------------------------------------------------------------------

x = sp.Symbol("x")
N = 60
PHI = sp.Poly(sp.cyclotomic_poly(N, x), x, domain=sp.QQ)


class Cyclo:
    """Element of Q(zeta_N), represented modulo Phi_N."""

    __slots__ = ("poly",)

    def __init__(self, value=0):
        if isinstance(value, Cyclo):
            self.poly = value.poly
        elif isinstance(value, sp.Poly):
            self.poly = self._reduce(value)
        else:
            self.poly = self._reduce(sp.Poly(value, x, domain=sp.QQ))

    @staticmethod
    def _reduce(poly: sp.Poly) -> sp.Poly:
        return sp.rem(sp.Poly(poly, x, domain=sp.QQ), PHI)

    @staticmethod
    def zero() -> "Cyclo":
        return Cyclo(0)

    @staticmethod
    def one() -> "Cyclo":
        return Cyclo(1)

    @staticmethod
    def rational(q) -> "Cyclo":
        return Cyclo(sp.Rational(q))

    @staticmethod
    def zeta(k: int) -> "Cyclo":
        return Cyclo(sp.Poly(x ** (k % N), x, domain=sp.QQ))

    def __add__(self, other) -> "Cyclo":
        other = Cyclo(other)
        return Cyclo(self.poly + other.poly)

    __radd__ = __add__

    def __neg__(self) -> "Cyclo":
        return Cyclo(-self.poly)

    def __sub__(self, other) -> "Cyclo":
        return self + (-Cyclo(other))

    def __rsub__(self, other) -> "Cyclo":
        return Cyclo(other) - self

    def __mul__(self, other) -> "Cyclo":
        other = Cyclo(other)
        return Cyclo(self.poly * other.poly)

    __rmul__ = __mul__

    def inv(self) -> "Cyclo":
        inv_poly = sp.invert(self.poly, PHI, domain=sp.QQ)
        return Cyclo(inv_poly)

    def __truediv__(self, other) -> "Cyclo":
        return self * Cyclo(other).inv()

    def __rtruediv__(self, other) -> "Cyclo":
        return Cyclo(other) / self

    def as_rational_if_constant(self) -> Fraction:
        P = self.poly
        coeffs = {monom[0]: coeff for monom, coeff in P.terms()}
        for deg, coeff in coeffs.items():
            if deg != 0 and coeff != 0:
                raise AssertionError(f"cyclotomic element is not rational: {P.as_expr()}")
        q = coeffs.get(0, sp.Rational(0))
        return Fraction(int(q.p), int(q.q))

    def coeff_vector(self) -> List[str]:
        coeffs = [sp.Rational(0)] * PHI.degree()
        for (deg,), coeff in self.poly.terms():
            if deg < len(coeffs):
                coeffs[deg] = coeff
            elif coeff != 0:
                raise AssertionError(f"unexpected degree after reduction: {self.poly}")
        return [str(c) for c in coeffs]

    def __repr__(self) -> str:
        return str(self.poly.as_expr())


def fixed_multiplier_exponents(G: s52.FiniteGroup, branch: Sequence[Any], u: Any, tangent_sign: int = +1) -> List[int]:
    if u == G.identity:
        raise ValueError("identity has non-isolated fixed set on a curve")
    exps: List[int] = []
    for e in branch:
        r = G.order(e)
        if N % r != 0:
            raise AssertionError(f"N={N} is not divisible by branch order {r}")
        H = G.cyclic_subgroup(e)
        power_index = {h: k for k, h in enumerate(H)}
        for a in G.left_coset_reps(H):
            v = G.conjugate_by(a, u)
            if v in power_index and v != G.identity:
                k = power_index[v]
                exps.append((tangent_sign * k * (N // r)) % N)
    return exps


def exact_curve_traces(G: s52.FiniteGroup, curve: s52.CurveData, tangent_sign: int = +1) -> Dict[str, Any]:
    g = s52.genus_from_branch(G, curve.branch)
    one = Cyclo.one()
    chiK: Dict[Any, Cyclo] = {}
    chi2K: Dict[Any, Cyclo] = {}
    for u in G.elements:
        if u == G.identity:
            chiK[u] = Cyclo.rational(g)
            chi2K[u] = Cyclo.rational(3 * g - 3)
        else:
            exps = fixed_multiplier_exponents(G, curve.branch, u, tangent_sign=tangent_sign)
            lambdas = [Cyclo.zeta(e) for e in exps]
            chiK[u] = one + sum((lam / (one - lam) for lam in lambdas), Cyclo.zero())
            chi2K[u] = sum(((lam * lam) / (one - lam) for lam in lambdas), Cyclo.zero())
    avgK = sum(chiK.values(), Cyclo.zero()) / len(G.elements)
    assert avgK.as_rational_if_constant() == 0, f"quotient P1 trace average failed: {avgK}"
    return {"genus": g, "chiK": chiK, "chi2K": chi2K}


def exact_obstruction_dimension(row: s52.RowData) -> Dict[str, Any]:
    G = row.group
    s52.check_branch_system(G, row.C1, row.label)
    s52.check_branch_system(G, row.C2, row.label)
    tr1 = exact_curve_traces(G, row.C1, tangent_sign=+1)
    tr2 = exact_curve_traces(G, row.C2, tangent_sign=+1)
    term21 = sum((tr1["chi2K"][u] * tr2["chiK"][u] for u in G.elements), Cyclo.zero()) / len(G.elements)
    term12 = sum((tr1["chiK"][u] * tr2["chi2K"][u] for u in G.elements), Cyclo.zero()) / len(G.elements)
    total = term21 + term12
    return {
        "term_H0_2K1_tensor_K2_exact": str(term21.as_rational_if_constant()),
        "term_H0_K1_tensor_2K2_exact": str(term12.as_rational_if_constant()),
        "total_d_exact": str(total.as_rational_if_constant()),
        "total_cyclotomic_coeff_vector": total.coeff_vector(),
    }


# ---------------------------------------------------------------------------
# Node reconstruction.
# ---------------------------------------------------------------------------


def elem_str(e: Any) -> str:
    if isinstance(e, tuple) and all(isinstance(v, int) for v in e):
        # permutation tuple or abelian tuple; for §6.9 it is a permutation tuple.
        if sorted(e) == list(range(len(e))):
            seen = [False] * len(e)
            cycles = []
            for i in range(len(e)):
                if not seen[i]:
                    if e[i] == i:
                        seen[i] = True
                        continue
                    cyc = []
                    j = i
                    while not seen[j]:
                        seen[j] = True
                        cyc.append(str(j + 1))
                        j = e[j]
                    cycles.append("(" + "".join(cyc) + ")")
            return "".join(cycles) if cycles else "id"
        return str(e)
    return str(e)


@dataclass(frozen=True)
class BranchPoint:
    branch_index: int
    branch_order: int
    coset: frozenset
    involution: Any


def coset_key(coset: frozenset) -> Tuple[str, ...]:
    return tuple(sorted(elem_str(e) for e in coset))


def branch_points_with_involution(G: s52.FiniteGroup, branch: Sequence[Any]) -> Dict[Tuple[int, frozenset], BranchPoint]:
    out: Dict[Tuple[int, frozenset], BranchPoint] = {}
    for idx, e in enumerate(branch, start=1):
        r = G.order(e)
        if r % 2 != 0:
            continue
        H = G.cyclic_subgroup(e)
        local_inv = G.pow(e, r // 2)
        for a in G.left_coset_reps(H):
            coset = frozenset(G.mul(a, h) for h in H)
            global_inv = G.mul(G.mul(a, local_inv), G.inv(a))
            out[(idx, coset)] = BranchPoint(idx, r, coset, global_inv)
    return out


def act_on_branch_point(G: s52.FiniteGroup, h: Any, bp: BranchPoint, lookup: Dict[Tuple[int, frozenset], BranchPoint]) -> BranchPoint:
    new_coset = frozenset(G.mul(h, a) for a in bp.coset)
    return lookup[(bp.branch_index, new_coset)]


def node_orbits(row: s52.RowData) -> Dict[str, Any]:
    G = row.group
    P1 = branch_points_with_involution(G, row.C1.branch)
    P2 = branch_points_with_involution(G, row.C2.branch)
    pairs = []
    for key1, p in P1.items():
        for key2, q in P2.items():
            if p.involution == q.involution:
                pairs.append((key1, key2))
    pair_set = set(pairs)
    unseen = set(pairs)
    orbits = []
    while unseen:
        start = next(iter(unseen))
        orbit = set()
        frontier = [start]
        while frontier:
            key1, key2 = frontier.pop()
            if (key1, key2) in orbit:
                continue
            orbit.add((key1, key2))
            p = P1[key1]
            q = P2[key2]
            for h in G.elements:
                p2 = act_on_branch_point(G, h, p, P1)
                q2 = act_on_branch_point(G, h, q, P2)
                new_key = ((p2.branch_index, p2.coset), (q2.branch_index, q2.coset))
                if new_key in pair_set and new_key not in orbit:
                    frontier.append(new_key)
        unseen -= orbit
        rep_key1, rep_key2 = sorted(orbit, key=lambda z: (z[0][0], coset_key(z[0][1]), z[1][0], coset_key(z[1][1])))[0]
        rep1, rep2 = P1[rep_key1], P2[rep_key2]
        c1_indices = sorted({P1[k1].branch_index for k1, _ in orbit})
        c2_indices = sorted({P2[k2].branch_index for _, k2 in orbit})
        c1_orders = sorted({P1[k1].branch_order for k1, _ in orbit})
        c2_orders = sorted({P2[k2].branch_order for _, k2 in orbit})
        orbits.append({
            "node_id": len(orbits) + 1,
            "orbit_size_in_prequotient_candidate_pairs": len(orbit),
            "C1_branch_indices": c1_indices,
            "C1_branch_orders": c1_orders,
            "C2_branch_indices": c2_indices,
            "C2_branch_orders": c2_orders,
            "representative_C1_coset": coset_key(rep1.coset),
            "representative_C2_coset": coset_key(rep2.coset),
            "representative_common_involution": elem_str(rep1.involution),
        })
    orbits.sort(key=lambda d: (d["C1_branch_indices"], d["C2_branch_indices"], d["representative_common_involution"]))
    # Normalize node ids after sorting.
    for i, d in enumerate(orbits, start=1):
        d["node_id"] = i
    return {
        "candidate_pair_count_before_G_quotient": len(pairs),
        "node_orbit_count": len(orbits),
        "node_orbits": orbits,
        "branch_category_partition": {
            "by_C1_branch_order": {
                str(order): sum(1 for o in orbits if o["C1_branch_orders"] == [order])
                for order in sorted({o["C1_branch_orders"][0] for o in orbits})
            },
            "by_C1_C2_branch_pair": {
                key: sum(1 for o in orbits if (
                    f"C1#{o['C1_branch_indices'][0]}(order{o['C1_branch_orders'][0]})-"
                    f"C2#{o['C2_branch_indices'][0]}(order{o['C2_branch_orders'][0]})"
                ) == key)
                for key in sorted({
                    f"C1#{o['C1_branch_indices'][0]}(order{o['C1_branch_orders'][0]})-"
                    f"C2#{o['C2_branch_indices'][0]}(order{o['C2_branch_orders'][0]})"
                    for o in orbits
                })
            },
        },
    }


def main():
    row = next(r for r in s52.rows() if r.label == "6.9 K2=4 G=S5")
    float_res = s52.obstruction_dimension(row, tangent_sign=+1)
    exact_res = exact_obstruction_dimension(row)
    nodes = node_orbits(row)
    assert exact_res["total_d_exact"] == "2"
    assert nodes["node_orbit_count"] == 4
    assert nodes["candidate_pair_count_before_G_quotient"] == 240

    # Dimension-only implication for beta: C^4 -> C^2 has kernel dimension at least 2.
    local_dim = nodes["node_orbit_count"]
    obstruction_dim = int(exact_res["total_d_exact"])
    kernel_lower_bound = local_dim - obstruction_dim

    interpretation = {
        "boundary_map": "beta: direct sum of four A1 local smoothing lines -> H^2(X,T_X^0)",
        "dimension_implication": f"rank(beta) <= {obstruction_dim}, so dim ker(beta) >= {kernel_lower_bound}",
        "full_support_not_decided": "A vector smoothing all four nodes exists at first order iff ker(beta) is not contained in the union of the four coordinate hyperplanes; d=2 and node count 4 do not decide this.",
        "symmetry_caution": "The quotient deck group is not an automorphism group of X after taking the diagonal quotient. In the displayed branch presentation all four nodes lie over the order-2 branch value of C1/G and split into two pairs over the two order-6 branch values of C2/G. Because C1/G has branch values of distinct orders (2,4,5) and the strict inner normalizer probe is trivial, this presentation alone does not establish transitivity on all four nodes.",
        "next_object": "Compute the actual boundary map beta, equivalently the dual residue/evaluation map from H^0(Y,Omega^1_Y tensor K_Y)^G to the four local smoothing-dual lines.",
    }

    data = {
        "row": row.label,
        "source_lines": "BCGP object.md lines 1149-1157 for §6.9; lines 169-171 and 347 for node count 8-K^2",
        "float_step52_recheck": {
            "term21": float_res["term_H0_2K1_tensor_K2"],
            "term12": float_res["term_H0_K1_tensor_2K2"],
            "total": float_res["total_obstruction_dual_invariant_dimension"],
        },
        "exact_cyclotomic_Q_zeta_60": exact_res,
        "nodes": nodes,
        "interpretation": interpretation,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")

    print("BCGP §6.9 exact obstruction dimension:")
    print(json.dumps(exact_res, indent=2))
    print("\nNode orbit reconstruction:")
    print(json.dumps(nodes, indent=2))
    print("\nBoundary-map implication:")
    print(json.dumps(interpretation, indent=2))
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
