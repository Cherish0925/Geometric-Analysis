"""
Step 52: Holomorphic Lefschetz computation for product-quotient smoothing obstructions.

Scientific purpose
------------------
For X=(C1 x C2)/G with only rational-double-point singularities, Step 51 proved

    H^2(X,T_X^0)^vee ≅ H^0(C1xC2, Omega^1 ⊗ K)^G

and the latter decomposes as

    (H^0(C1,2K1) ⊗ H^0(C2,K2))^G
      ⊕ (H^0(C1,K1) ⊗ H^0(C2,2K2))^G.

This script computes its dimension by holomorphic Lefschetz traces, without using
Sym^2 H^0(K) and without decomposing into irreducible representations.  Hence it
handles hyperelliptic abelian rows and nonabelian BCGP rows uniformly.

Lefschetz convention
--------------------
For a nonidentity automorphism u of a curve C, with tangent multiplier lambda_p
at each fixed point p and action on forms by pullback,

    Tr(u | H^0(C,K_C))  = 1 + sum_p lambda_p/(1-lambda_p),
    Tr(u | H^0(C,2K_C)) =     sum_p lambda_p^2/(1-lambda_p),

while at identity the traces are g and 3g-3.  Fixed points and multipliers are
reconstructed from the branch stabilizers of the regular G-cover C -> P^1.

Interpretation
--------------
If the averaged tensor character dimension d is zero, Lee--Park globalization
and Step 51's reflexive bridge give a sufficient Q-Gorenstein smoothing mechanism
for all local RDP node smoothings.  If d is positive, the computation only says
this sufficient vanishing route fails; it does not imply absence of a smoothing
or absence of an Einstein metric.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import isclose
import cmath
import json
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Sequence, Tuple, Any

WORKSPACE = Path(__file__).resolve().parents[1]
OUT = WORKSPACE / "data" / "step52_lefschetz_obstruction_dimensions.json"

Complex = complex
TOL = 2e-7


def clean_complex(z: complex, tol: float = 1e-7) -> complex:
    re = 0.0 if abs(z.real) < tol else z.real
    im = 0.0 if abs(z.imag) < tol else z.imag
    return complex(re, im)


def near_int(x: complex, tol: float = 1e-6) -> int:
    if abs(x.imag) > tol:
        raise AssertionError(f"not real: {x}")
    r = round(x.real)
    if abs(x.real - r) > tol:
        raise AssertionError(f"not integral: {x}")
    return int(r)


@dataclass
class FiniteGroup:
    name: str
    elements: List[Any]
    identity: Any
    mul: Callable[[Any, Any], Any]
    inv: Callable[[Any], Any]

    def order(self, a: Any) -> int:
        x = self.identity
        for k in range(1, len(self.elements) + 1):
            x = self.mul(x, a)
            if x == self.identity:
                return k
        raise AssertionError(f"order not found for {a}")

    def pow(self, a: Any, k: int) -> Any:
        if k < 0:
            return self.pow(self.inv(a), -k)
        x = self.identity
        for _ in range(k):
            x = self.mul(x, a)
        return x

    def cyclic_subgroup(self, a: Any) -> List[Any]:
        r = self.order(a)
        return [self.pow(a, k) for k in range(r)]

    def conjugate_by(self, a: Any, u: Any) -> Any:
        # a^{-1} u a
        return self.mul(self.mul(self.inv(a), u), a)

    def subgroup_generated_by(self, gens: Sequence[Any]) -> set:
        elems = {self.identity}
        frontier = [self.identity]
        allgens = list(gens) + [self.inv(g) for g in gens]
        while frontier:
            x = frontier.pop()
            for g in allgens:
                y = self.mul(x, g)
                if y not in elems:
                    elems.add(y)
                    frontier.append(y)
        return elems

    def left_product(self, seq: Sequence[Any]) -> Any:
        # BCGP's permutation multiplication convention is left accumulation for
        # the displayed nonabelian spherical systems: e_r * ... * e_1 in our
        # compose-after convention.  Abelian rows satisfy either convention.
        x = self.identity
        for e in seq:
            x = self.mul(e, x)
        return x

    def left_coset_reps(self, H: Sequence[Any]) -> List[Any]:
        unseen = set(self.elements)
        reps = []
        while unseen:
            a = next(iter(unseen))
            reps.append(a)
            coset = {self.mul(a, h) for h in H}
            unseen -= coset
        return reps


def abelian_group(moduli: Tuple[int, ...], name: str) -> FiniteGroup:
    elems = list(product(*[range(m) for m in moduli]))
    zero = tuple(0 for _ in moduli)

    def add(a, b):
        return tuple((a[i] + b[i]) % moduli[i] for i in range(len(moduli)))

    def neg(a):
        return tuple((-a[i]) % moduli[i] for i in range(len(moduli)))

    return FiniteGroup(name, elems, zero, add, neg)


# Permutations are tuples p with p[i] = image of i, 0-indexed.  Multiplication is
# composition p after q: (p*q)(i)=p(q(i)).
def compose(p: Tuple[int, ...], q: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def invert_perm(p: Tuple[int, ...]) -> Tuple[int, ...]:
    inv = [0] * len(p)
    for i, j in enumerate(p):
        inv[j] = i
    return tuple(inv)


def parse_perm(s: str, n: int) -> Tuple[int, ...]:
    s = s.strip()
    p = tuple(range(n))
    if s in ("", "id", "Id", "1"):
        return p
    # Parse cycle strings like "(1324)(56)". Cycles compose left-to-right as
    # written; disjoint cycles commute, and BCGP entries mostly use disjoint
    # products. For non-disjoint products not used in the listed branch elements,
    # this convention is at least explicit and checked by orders/genera.
    cycles = []
    i = 0
    while i < len(s):
        if s[i].isspace():
            i += 1
            continue
        if s[i] != '(':
            raise ValueError(f"bad cycle string {s!r} at {i}")
        j = s.index(')', i)
        body = s[i + 1:j].strip()
        if not body:
            cyc = []
        elif ' ' in body or ',' in body:
            body2 = body.replace(',', ' ')
            cyc = [int(x) - 1 for x in body2.split()]
        else:
            cyc = [int(ch) - 1 for ch in body]
        cycles.append(cyc)
        i = j + 1
    for cyc in cycles:
        q = list(range(n))
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            q[a] = b
        p = compose(tuple(q), p)
    return p


def perm_group(generators: Sequence[str], n: int, name: str) -> FiniteGroup:
    gens = [parse_perm(s, n) for s in generators]
    ident = tuple(range(n))
    elems = {ident}
    frontier = [ident]
    # Use generators and their inverses for fast closure.
    allgens = gens + [invert_perm(g) for g in gens]
    while frontier:
        x = frontier.pop()
        for g in allgens:
            y = compose(x, g)
            if y not in elems:
                elems.add(y)
                frontier.append(y)
    elems_list = sorted(elems)
    return FiniteGroup(name, elems_list, ident, compose, invert_perm)


@dataclass
class CurveData:
    name: str
    branch: List[Any]
    genus_expected: int | None = None
    signature_expected: List[int] | None = None


@dataclass
class RowData:
    label: str
    K2: int
    group: FiniteGroup
    C1: CurveData
    C2: CurveData
    expected_order: int | None = None
    source: str = "BCGP"


def genus_from_branch(G: FiniteGroup, branch: Sequence[Any]) -> int:
    # Riemann-Hurwitz for regular G-cover of P^1:
    # 2g-2 = |G|(-2 + sum_i(1 - 1/order(e_i))).
    total = -2.0 + sum(1.0 - 1.0 / G.order(e) for e in branch)
    val = 2 + len(G.elements) * total
    g = round(val / 2)
    if abs(val - 2 * g) > 1e-8:
        raise AssertionError((G.name, val, branch))
    return g


def fixed_multipliers(G: FiniteGroup, branch: Sequence[Any], u: Any, tangent_sign: int = +1) -> List[complex]:
    if u == G.identity:
        raise ValueError("identity has whole curve fixed; use identity trace")
    lambdas: List[complex] = []
    for e in branch:
        r = G.order(e)
        H = G.cyclic_subgroup(e)
        power_index = {h: k for k, h in enumerate(H)}
        reps = G.left_coset_reps(H)
        for a in reps:
            v = G.conjugate_by(a, u)  # a^{-1} u a
            if v in power_index and v != G.identity:
                k = power_index[v]
                lambdas.append(cmath.exp(tangent_sign * 2j * cmath.pi * k / r))
    return lambdas


def curve_traces(G: FiniteGroup, curve: CurveData, tangent_sign: int = +1) -> Dict[str, Any]:
    g = genus_from_branch(G, curve.branch)
    if curve.genus_expected is not None and g != curve.genus_expected:
        raise AssertionError(f"{curve.name}: genus {g} != expected {curve.genus_expected}")
    chiK: Dict[Any, complex] = {}
    chi2K: Dict[Any, complex] = {}
    fixed_counts: Dict[str, int] = {}
    for u in G.elements:
        if u == G.identity:
            chiK[u] = complex(g, 0)
            chi2K[u] = complex(3 * g - 3, 0)
            fixed_counts[str(u)] = "identity"  # type: ignore[assignment]
        else:
            lambdas = fixed_multipliers(G, curve.branch, u, tangent_sign=tangent_sign)
            fixed_counts[str(u)] = len(lambdas)  # type: ignore[assignment]
            chiK[u] = 1.0 + sum(lam / (1.0 - lam) for lam in lambdas)
            chi2K[u] = sum((lam * lam) / (1.0 - lam) for lam in lambdas)
    avgK = sum(chiK.values()) / len(G.elements)
    # Quotient is P^1, so H^0(K_C)^G = 0. This is a sensitive check on fixed-point counts.
    if abs(avgK) > 2e-6:
        raise AssertionError(f"{curve.name}: average chiK should be 0 for quotient P1, got {avgK}")
    return {"genus": g, "chiK": chiK, "chi2K": chi2K, "fixed_counts": fixed_counts}


def check_branch_system(G: FiniteGroup, curve: CurveData, row_label: str) -> Dict[str, Any]:
    orders = [G.order(e) for e in curve.branch]
    if curve.signature_expected is not None and orders != curve.signature_expected:
        raise AssertionError(f"{row_label} {curve.name}: orders {orders} != signature {curve.signature_expected}")
    generated = G.subgroup_generated_by(curve.branch)
    if len(generated) != len(G.elements):
        raise AssertionError(f"{row_label} {curve.name}: branch elements generate {len(generated)} of {len(G.elements)} elements")
    if G.left_product(curve.branch) != G.identity:
        raise AssertionError(f"{row_label} {curve.name}: BCGP left-product convention does not give identity")
    return {"orders": orders, "generates_group": True, "left_product_identity": True}


def obstruction_dimension(row: RowData, tangent_sign: int = +1) -> Dict[str, Any]:
    G = row.group
    if row.expected_order is not None and len(G.elements) != row.expected_order:
        raise AssertionError(f"{row.label}: |G|={len(G.elements)} != expected {row.expected_order}")
    branch_check_C1 = check_branch_system(G, row.C1, row.label)
    branch_check_C2 = check_branch_system(G, row.C2, row.label)
    tr1 = curve_traces(G, row.C1, tangent_sign=tangent_sign)
    tr2 = curve_traces(G, row.C2, tangent_sign=tangent_sign)
    term21_complex = sum(tr1["chi2K"][u] * tr2["chiK"][u] for u in G.elements) / len(G.elements)
    term12_complex = sum(tr1["chiK"][u] * tr2["chi2K"][u] for u in G.elements) / len(G.elements)
    total_complex = term21_complex + term12_complex
    term21 = near_int(term21_complex)
    term12 = near_int(term12_complex)
    total = near_int(total_complex)
    return {
        "label": row.label,
        "K2": row.K2,
        "group": G.name,
        "order": len(G.elements),
        "genus_C1": tr1["genus"],
        "genus_C2": tr2["genus"],
        "term_H0_2K1_tensor_K2": term21,
        "term_H0_K1_tensor_2K2": term12,
        "total_obstruction_dual_invariant_dimension": total,
        "complex_raw": {
            "term21": [term21_complex.real, term21_complex.imag],
            "term12": [term12_complex.real, term12_complex.imag],
            "total": [total_complex.real, total_complex.imag],
        },
        "max_fixed_C1_nonidentity": max(v for v in tr1["fixed_counts"].values() if isinstance(v, int)),
        "max_fixed_C2_nonidentity": max(v for v in tr2["fixed_counts"].values() if isinstance(v, int)),
        "branch_check_C1": branch_check_C1,
        "branch_check_C2": branch_check_C2,
    }


def character_decomposition_abelian(row: RowData, which: str, mK: int, tangent_sign: int = +1) -> Dict[Tuple[int, ...], int]:
    # Fourier inversion for abelian tuple groups; used to compare K^2=2 Lefschetz with Step 50.
    G = row.group
    assert isinstance(G.identity, tuple)
    moduli = []
    for coords in zip(*G.elements):
        moduli.append(max(coords) + 1)
    moduli = tuple(moduli)
    curve = row.C1 if which == "C1" else row.C2
    traces = curve_traces(G, curve, tangent_sign=tangent_sign)
    chi = traces["chiK"] if mK == 1 else traces["chi2K"]
    out = {}
    for ch in G.elements:
        acc = 0j
        for u in G.elements:
            phase = sum(ch[i] * u[i] / moduli[i] for i in range(len(moduli)))
            acc += chi[u] * cmath.exp(-2j * cmath.pi * phase)
        mult = near_int(acc / len(G.elements))
        if mult:
            out[ch] = mult
    return out


def rows() -> List[RowData]:
    out: List[RowData] = []
    # BCGP §6.7, K^2=2, Z4^2.
    G44 = abelian_group((4, 4), "Z4^2")
    out.append(RowData(
        "6.7 K2=2 G=Z4^2", 2, G44,
        CurveData("C1", [(1, 3), (1, 0), (2, 1)], 3),
        CurveData("C2", [(3, 2), (0, 1), (1, 1)], 3),
        expected_order=16,
    ))
    # BCGP §6.18, K^2=4, Z4 x Z2.
    G42 = abelian_group((4, 2), "Z4xZ2")
    out.append(RowData(
        "6.18 K2=4 G=Z4xZ2", 4, G42,
        CurveData("C1", [(2, 1), (2, 1), (3, 1), (1, 1)], 3),
        CurveData("C2", [(0, 1), (0, 1), (3, 0), (1, 0)], 3),
        expected_order=8,
    ))
    # BCGP §6.19, K^2=4, Z2^3.
    G222 = abelian_group((2, 2, 2), "Z2^3")
    out.append(RowData(
        "6.19 K2=4 G=Z2^3", 4, G222,
        CurveData("C1", [(0, 0, 1), (0, 1, 1), (0, 0, 1), (1, 1, 1), (1, 0, 0)], 3),
        CurveData("C2", [(1, 0, 0), (1, 0, 1), (0, 1, 0), (1, 1, 0), (1, 0, 1)], 3),
        expected_order=8,
    ))

    # The remaining K^2=4 rows from BCGP §6.9--6.17.  Several section S1/S2
    # orders are reversed relative to Table 2; the genera below are those implied
    # by the actual displayed branch lists in §6.
    k4_specs = [
        ("6.9 K2=4 G=S5", 4, 5, 4, 21,
         ["(25)", "(1435)", "(12534)"],
         ["(132)", "(135)(24)", "(15)(243)"]),
        ("6.10 K2=4 G=A5", 4, 5, 11, 4,
         ["(15)(34)", "(12)(35)", "(354)", "(125)"],
         ["(23)(45)", "(15342)", "(13425)"]),
        ("6.11 K2=4 G=S4xZ2", 4, 6, 13, 3,
         ["(24)", "(24)", "(1324)(56)", "(1423)(56)"],
         ["(13)(56)", "(1342)", "(124)(56)"]),
        ("6.12 K2=4 G=S4xZ2", 4, 6, 13, 3,
         ["(12)(34)(56)", "(34)(56)", "(13)", "(23)", "(13)"],
         ["(13)(56)", "(1342)", "(124)(56)"]),
        ("6.13 K2=4 G=Z2^4_semidirect_Z2", 4, 8, 5, 5,
         ["(24)(68)", "(12)(34)(56)(78)", "(12)(34)", "(24)(5876)"],
         ["(12)(34)(57)(68)", "(56)(78)", "(24)(68)", "(1234)(5876)"]),
        ("6.14 K2=4 G=S4", 4, 4, 7, 3,
         ["(13)", "(14)", "(12)(34)", "(12)", "(14)"],
         ["(132)", "(1432)", "(1342)"]),
        ("6.15 K2=4 G=S3xZ3", 4, 6, 4, 4,
         ["(13)", "(13)", "(123)(456)", "(132)(465)"],
         ["(132)", "(23)(465)", "(12)(456)"]),
        ("6.16 K2=4 G=Z3^2_semidirect_Z2", 4, 6, 4, 4,
         ["(23)(56)", "(23)(45)", "(123)(465)", "(132)"],
         ["(23)(56)", "(12)(46)", "(132)(465)", "(465)"]),
        ("6.17 K2=4 G=D4xZ2", 4, 6, 5, 3,
         ["(56)", "(24)", "(12)(34)", "(12)(34)(56)", "(24)"],
         ["(13)(56)", "(14)(23)(56)", "(13)(24)(56)", "(1234)(56)"]),
    ]
    for label, K2, n, g1, g2, S1, S2 in k4_specs:
        G = perm_group(S1 + S2, n, label.split("G=")[-1])
        expected_order = int(8 * (g1 - 1) * (g2 - 1) / K2)
        out.append(RowData(label, K2, G,
                           CurveData("C1", [parse_perm(s, n) for s in S1], g1),
                           CurveData("C2", [parse_perm(s, n) for s in S2], g2),
                           expected_order=expected_order))

    # Nonabelian K^2=6 rows from BCGP §6.20--6.27.  The common permutation model
    # in each row is generated by the displayed S1 and S2 branch elements.
    nonabelian_specs = [
        ("6.20 K2=6 G=A6", 6, 6, 19, 16,
         ["(16)(34)", "(25436)", "(16452)"],
         ["(156)", "(146)(235)", "(1532)(46)"]),
        ("6.21 K2=6 G=A6", 6, 6, 19, 16,
         ["(16)(34)", "(25436)", "(16452)"],
         ["(123)(456)", "(125)", "(1465)(23)"]),
        ("6.22 K2=6 G=S5xZ2", 6, 7, 11, 19,
         ["(13)(45)(67)", "(1524)(67)", "(153)(24)"],
         ["(25)(67)", "(1432)", "(15234)(67)"]),
        ("6.23 K2=6 G=PSL(2,7)", 6, 7, 19, 8,
         ["(27)(46)", "(1235674)", "(1653742)"],
         ["(157)(234)", "(145)(367)", "(2476)(35)"]),
        ("6.24 K2=6 G=PSL(2,7)", 6, 7, 19, 8,
         ["(27)(46)", "(1235674)", "(1653742)"],
         ["(127)(364)", "(157)(234)", "(1263)(57)"]),
        # In §6.25--6.27 the section's S1/S2 order is the reverse of Table 2's
        # displayed g1/g2 order for the last three rows; use the genera implied
        # by the actual branch lists read from the section.
        ("6.25 K2=6 G=A5", 6, 5, 16, 4,
         ["(13)(24)", "(123)", "(235)", "(254)"],
         ["(23)(45)", "(15342)", "(13425)"]),
        ("6.26 K2=6 G=S4xZ2", 6, 6, 19, 3,
         ["(23)(56)", "(12)(34)(56)", "(13)(56)", "(13)(56)", "(1342)"],
         ["(13)", "(1324)(56)", "(142)(56)"]),
        ("6.27 K2=6 G=D4xZ2", 6, 6, 7, 3,
         ["(56)", "(56)", "(12)(34)(56)", "(13)(56)", "(1432)"],
         ["(24)", "(14)(23)", "(13)(24)(56)", "(1432)(56)"]),
    ]
    for label, K2, n, g1, g2, S1, S2 in nonabelian_specs:
        G = perm_group(S1 + S2, n, label.split("G=")[-1])
        expected_order = int(8 * (g1 - 1) * (g2 - 1) / K2)
        out.append(RowData(label, K2, G,
                           CurveData("C1", [parse_perm(s, n) for s in S1], g1),
                           CurveData("C2", [parse_perm(s, n) for s in S2], g2),
                           expected_order=expected_order))
    return out


def main():
    rows_list = rows()
    results = []
    expected_d = {
        "6.7 K2=2 G=Z4^2": 0,
        "6.18 K2=4 G=Z4xZ2": 4,
        "6.19 K2=4 G=Z2^3": 6,
        "6.9 K2=4 G=S5": 2,
        "6.10 K2=4 G=A5": 3,
        "6.11 K2=4 G=S4xZ2": 3,
        "6.12 K2=4 G=S4xZ2": 4,
        "6.13 K2=4 G=Z2^4_semidirect_Z2": 4,
        "6.14 K2=4 G=S4": 4,
        "6.15 K2=4 G=S3xZ3": 3,
        "6.16 K2=4 G=Z3^2_semidirect_Z2": 4,
        "6.17 K2=4 G=D4xZ2": 5,
        "6.20 K2=6 G=A6": 4,
        "6.21 K2=6 G=A6": 4,
        "6.22 K2=6 G=S5xZ2": 4,
        "6.23 K2=6 G=PSL(2,7)": 4,
        "6.24 K2=6 G=PSL(2,7)": 4,
        "6.25 K2=6 G=A5": 5,
        "6.26 K2=6 G=S4xZ2": 6,
        "6.27 K2=6 G=D4xZ2": 7,
    }
    for row in rows_list:
        res = obstruction_dimension(row, tangent_sign=+1)
        # Reversing the tangent multiplier exponent dualizes characters and must
        # not change the invariant tensor dimension.  This also guards against an
        # orientation convention error in the trace average.
        res_dual = obstruction_dimension(row, tangent_sign=-1)
        assert res_dual["total_obstruction_dual_invariant_dimension"] == res["total_obstruction_dual_invariant_dimension"]
        assert res["total_obstruction_dual_invariant_dimension"] == expected_d[row.label]
        results.append(res)
        print(f"{res['label']}: |G|={res['order']} g=({res['genus_C1']},{res['genus_C2']}) "
              f"term21={res['term_H0_2K1_tensor_K2']} term12={res['term_H0_K1_tensor_2K2']} "
              f"d={res['total_obstruction_dual_invariant_dimension']}")

    # Abelian cross-checks: recover character decompositions from Lefschetz traces.
    abelian_chars = {}
    for row in rows_list[:3]:
        abelian_chars[row.label] = {
            "C1_K": character_decomposition_abelian(row, "C1", 1, tangent_sign=-1),
            "C2_K": character_decomposition_abelian(row, "C2", 1, tangent_sign=-1),
            "C1_2K": character_decomposition_abelian(row, "C1", 2, tangent_sign=-1),
            "C2_2K": character_decomposition_abelian(row, "C2", 2, tangent_sign=-1),
        }
    print("\nAbelian-row Lefschetz Fourier decompositions (dual convention matching Step 50):")
    for row_label, pieces in abelian_chars.items():
        print(row_label)
        for k, v in pieces.items():
            print(" ", k, sorted(v.items()))

    data = {
        "method": "holomorphic_lefschetz_tensor_character_average",
        "formulas": {
            "trace_K_nonidentity": "1 + sum_{p fixed} lambda_p/(1-lambda_p)",
            "trace_2K_nonidentity": "sum_{p fixed} lambda_p^2/(1-lambda_p)",
            "identity_traces": "trace_K=g, trace_2K=3g-3",
            "obstruction_dimension": "|G|^{-1} sum_u (chi_2K,C1(u) chi_K,C2(u) + chi_K,C1(u) chi_2K,C2(u))",
        },
        "interpretation": "d=0 is a sufficient global-smoothing mechanism via Step 51 reflexive bridge and Lee-Park; d>0 is not a no-Einstein or no-smoothing theorem.",
        "results": results,
        "abelian_lefschetz_fourier_decomposition_dual_convention": {
            row_label: {k: {str(ch): mult for ch, mult in v.items()} for k, v in pieces.items()}
            for row_label, pieces in abelian_chars.items()
        },
        "note_on_character_orientation": "The stored Fourier lists use the tangent-sign=-1 dual convention, which matches the Step 50/51 abelian character tables for the K^2=2 row. Reversing the tangent multiplier exponent dualizes all abelian character labels; invariant dimensions are unchanged.",
        "branch_system_check_convention": "For the displayed nonabelian permutation rows, the script checks the spherical-system identity using BCGP's left-product convention relative to the script's compose-after permutation multiplication. Every curve branch list also separately generates the full group and has the expected orders/signature.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
