"""
Step 95: T^2 stabilizer selection rules for the product-orbifold kernel-plane
obstruction problem.

This script is not a numerical Green-function computation.  It audits the
representation-theoretic gates that control which local and pair terms can
appear in the finite-dimensional Ozuch/Biquard equations for the four A1 nodes
of (S^2 x S^2)/<r_pi,r_pi>.

It verifies:
  1. Under independent rotations of the two S^2 factors, omega_1^+ and omega_1^-
     are invariant while the kernel planes K^+, K^- have weights alpha+beta and
     alpha-beta respectively.  The beta=0 subcircle acts with ordinary weight 1
     on every K^epsilon.
  2. There is no homogeneous quadratic equivariant local map K -> K under this
     subcircle, so the projected local O(t^2) vector obstruction vanishes by
     weight, not by the invalid 'no equivariant vector' argument.
  3. A pair term linear in the receiver variable z_j and quadratic in a source
     variable z_i has exactly the allowed monomial types described in the Step 95
     strategist correction: |z_i|^2 z_j for all pairs, and z_i^2 \bar z_j only
     for same-chirality pairs.
  4. In the diagonal balanced pattern each node has exactly two opposite-chirality
     adjacent neighbours and one same-chirality diagonal neighbour, so subtracting
     the all-compatible row leaves only adjacent pair coefficient differences.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Dict, List, Tuple

import sympy as sp


def two_form_matrix(i: int, j: int) -> sp.Matrix:
    """Skew matrix for e^i wedge e^j, 0-indexed."""
    M = sp.zeros(4, 4)
    M[i, j] = 1
    M[j, i] = -1
    return M


def inner2(A: sp.Matrix, B: sp.Matrix) -> sp.Expr:
    """Inner product of two-form matrices: coefficient dot product."""
    return sp.simplify(sp.trace(A.T * B) / 2)


def basis_coeffs(A: sp.Matrix, basis: List[sp.Matrix]) -> List[sp.Expr]:
    # Our bases below are orthogonal with norm^2=2, since we avoid sqrt(2).
    return [sp.simplify(inner2(A, B) / inner2(B, B)) for B in basis]


def rotation_matrix(alpha: sp.Symbol, beta: sp.Symbol) -> sp.Matrix:
    ca, sa = sp.cos(alpha), sp.sin(alpha)
    cb, sb = sp.cos(beta), sp.sin(beta)
    RA = sp.Matrix([[ca, -sa], [sa, ca]])
    RB = sp.Matrix([[cb, -sb], [sb, cb]])
    D = sp.zeros(4, 4)
    D[:2, :2] = RA
    D[2:, 2:] = RB
    return D


def transform_two_form(A: sp.Matrix, D: sp.Matrix) -> sp.Matrix:
    # Pullback by the orthogonal transformation D in the chosen tangent frame.
    return sp.simplify(D.T * A * D)


def compute_chiral_blocks() -> Dict[str, object]:
    alpha, beta = sp.symbols("alpha beta", real=True)
    D = rotation_matrix(alpha, beta)

    e12 = two_form_matrix(0, 1)
    e34 = two_form_matrix(2, 3)
    e13 = two_form_matrix(0, 2)
    e14 = two_form_matrix(0, 3)
    e23 = two_form_matrix(1, 2)
    e24 = two_form_matrix(1, 3)

    # One standard orientation convention.  Signs in the kernel plane change only
    # orientation of the complex coordinate; the weights alpha +/- beta are invariant.
    w1p = e12 + e34
    w2p = e13 - e24
    w3p = e14 + e23

    w1m = e12 - e34
    w2m = e13 + e24
    w3m = e14 - e23

    plus_basis = [w1p, w2p, w3p]
    minus_basis = [w1m, w2m, w3m]

    def block_expr(basis: List[sp.Matrix]) -> sp.Matrix:
        cols = []
        for B in basis:
            T = transform_two_form(B, D)
            cols.append(basis_coeffs(T, basis))
        # Matrix columns are images of basis vectors.
        return sp.Matrix.hstack(*[sp.Matrix(c) for c in cols])

    plus_block_expr = block_expr(plus_basis)
    minus_block_expr = block_expr(minus_basis)
    plus_block = [[str(sp.trigsimp(plus_block_expr[i, j])) for j in range(3)] for i in range(3)]
    minus_block = [[str(sp.trigsimp(minus_block_expr[i, j])) for j in range(3)] for i in range(3)]

    # beta=0 subcircle blocks on K=(omega2,omega3)
    plus_beta0 = [[str(sp.trigsimp(plus_block_expr[i, j].subs(beta, 0))) for j in range(1, 3)] for i in range(1, 3)]
    minus_beta0 = [[str(sp.trigsimp(minus_block_expr[i, j].subs(beta, 0))) for j in range(1, 3)] for i in range(1, 3)]

    return {
        "basis_convention": {
            "omega1_plus": "e12+e34",
            "omega2_plus": "e13-e24",
            "omega3_plus": "e14+e23",
            "omega1_minus": "e12-e34",
            "omega2_minus": "e13+e24",
            "omega3_minus": "e14-e23",
        },
        "T2_pullback_block_plus_basis_columns": plus_block,
        "T2_pullback_block_minus_basis_columns": minus_block,
        "kernel_weight_summary": {
            "K_plus": "rotation by alpha+beta up to the displayed orientation convention",
            "K_minus": "rotation by alpha-beta up to the displayed orientation convention",
            "beta_equals_0_subcircle": "both K_plus and K_minus rotate with ordinary weight 1",
        },
        "beta0_kernel_block_plus": plus_beta0,
        "beta0_kernel_block_minus": minus_beta0,
    }


def enumerate_local_quadratic() -> List[Dict[str, object]]:
    """Degree-2 monomials z^a zbar^b that could map K->K under beta=0."""
    out = []
    for a in range(3):
        b = 2 - a
        weight = a - b
        allowed = weight == 1  # output K has beta=0 weight +1
        out.append({"monomial": f"z^{a} zbar^{b}", "a": a, "b": b, "weight": weight, "allowed_for_K_to_K": allowed})
    return out


def enumerate_pair_monomials(eps_i: int, eps_j: int) -> List[Dict[str, object]]:
    """Enumerate z_i^a zbar_i^b z_j^c zbar_j^d, degree_i=2, degree_j=1.

    T^2 weights are vectors w_epsilon=(1, epsilon) for z; conjugates carry the
    negative vector.  The receiver obstruction vector lies in K_j, so target
    weight is w_j.
    """
    w_i = (1, eps_i)
    w_j = (1, eps_j)
    target = w_j
    rows = []
    for a in range(3):
        b = 2 - a
        for c in range(2):
            d = 1 - c
            wt = ((a - b) * w_i[0] + (c - d) * w_j[0], (a - b) * w_i[1] + (c - d) * w_j[1])
            allowed = wt == target
            name_parts = []
            if a:
                name_parts.append("z_i" if a == 1 else f"z_i^{a}")
            if b:
                name_parts.append("zbar_i" if b == 1 else f"zbar_i^{b}")
            if c:
                name_parts.append("z_j" if c == 1 else f"z_j^{c}")
            if d:
                name_parts.append("zbar_j" if d == 1 else f"zbar_j^{d}")
            rows.append({
                "monomial": " ".join(name_parts) or "1",
                "exponents_a_b_c_d": [a, b, c, d],
                "weight": wt,
                "target_weight": target,
                "allowed": allowed,
            })
    return rows


def allowed_pair_summary() -> Dict[str, object]:
    summary = {}
    for eps_i, eps_j, label in [(1, 1, "same_plus"), (-1, -1, "same_minus"), (1, -1, "opposite_i_plus_j_minus"), (-1, 1, "opposite_i_minus_j_plus")]:
        rows = enumerate_pair_monomials(eps_i, eps_j)
        summary[label] = {
            "eps_i": eps_i,
            "eps_j": eps_j,
            "allowed_monomials": [r for r in rows if r["allowed"]],
            "all_monomials": rows,
        }
    return summary


def four_node_pattern_counts() -> Dict[str, object]:
    nodes = {
        "NN": (1, 1),
        "NS": (1, -1),
        "SN": (-1, 1),
        "SS": (-1, -1),
    }
    diagonal_balanced = {"NN": 1, "SS": 1, "NS": -1, "SN": -1}
    all_same = {k: 1 for k in nodes}

    def geom(a: str, b: str) -> str:
        xa, ya = nodes[a]
        xb, yb = nodes[b]
        diff = (xa != xb) + (ya != yb)
        return "adjacent" if diff == 1 else "diagonal" if diff == 2 else "self"

    def counts(pattern: Dict[str, int]) -> Dict[str, object]:
        result = {}
        for j in nodes:
            rows = []
            for i in nodes:
                if i == j:
                    continue
                rows.append({
                    "source": i,
                    "receiver": j,
                    "geometry": geom(i, j),
                    "source_chirality": pattern[i],
                    "receiver_chirality": pattern[j],
                    "pair_chirality": "same" if pattern[i] == pattern[j] else "opposite",
                })
            result[j] = rows
        return result

    diag_counts = counts(diagonal_balanced)
    all_counts = counts(all_same)

    compressed = {}
    for j, rows in diag_counts.items():
        d = {}
        for r in rows:
            key = f"{r['geometry']}_{r['pair_chirality']}"
            d[key] = d.get(key, 0) + 1
        compressed[j] = d

    return {
        "nodes": nodes,
        "diagonal_balanced_chiralities": diagonal_balanced,
        "all_compatible_chiralities": all_same,
        "diagonal_balanced_ordered_pairs": diag_counts,
        "diagonal_balanced_counts_by_receiver": compressed,
        "all_compatible_ordered_pairs": all_counts,
        "difference_formula_equal_scale_unit_norm": (
            "For each receiver in the diagonal balanced pattern: mixed-minus-all-compatible "
            "keeps only two adjacent pairs, giving 2*(B_adj_opp - B_adj_same). "
            "The same-chirality diagonal pair is identical in both rows and cancels. "
            "By T^2 selection, B_adj_opp is isotropic; B_adj_same may have isotropic "
            "and anisotropic z_i^2 zbar_j parts."
        ),
    }


def main() -> None:
    out_path = Path("Sessions/S0910A02/workspace/data/step95_t2_selection_rules.json")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    result = {
        "purpose": "Repair Gate 1 proof using actual T^2 stabilizer and derive Gate 3 monomial selection rules.",
        "chiral_T2_blocks": compute_chiral_blocks(),
        "local_quadratic_K_to_K_under_beta0": enumerate_local_quadratic(),
        "local_gate1_conclusion": "No degree-2 monomial has beta=0 weight +1, so a T^2-equivariant projected local quadratic map K_j->K_j is zero. This repairs the invalid SO(2)-transitivity argument.",
        "pair_monomial_selection": allowed_pair_summary(),
        "pair_selection_conclusion": {
            "opposite_chirality": "Only |z_i|^2 z_j is allowed; the pair response is isotropic on K_j.",
            "same_chirality": "Two types are allowed: |z_i|^2 z_j (isotropic) and z_i^2 zbar_j (anisotropic).",
            "scope": "This is a representation selection rule. It does not compute the scalar coefficients or prove the analytic o(t^3) remainder.",
        },
        "four_node_diagonal_balanced": four_node_pattern_counts(),
        "global_coupling_filter": {
            "T2_invariant_modes_only": "A T^2-symmetric configuration can excite only T^2-weight-zero orbifold kernel/deformation modes.",
            "source_quadratic_invariant": "The only source-quadratic invariant is |z_i|^2; z_i^2 and zbar_i^2 have nonzero T^2 weights.",
            "scalar_kernel_status": "The four Ozuch scalar zero modes u_A g_A, u_A g_B, u_B g_A, u_B g_B are T^2-invariant, so T^2 alone does not remove them. Existing A-symmetry and factor-traceless/Bianchi-corrected H^4 calculations support their leading pairing vanishing in the diagonal symmetric problem, but a full Ozuch-gauge Delta-nu check remains a separate verification.",
        },
    }
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"Saved {out_path}")
    print(result["chiral_T2_blocks"]["kernel_weight_summary"])
    print("Local quadratic allowed:", [r for r in result["local_quadratic_K_to_K_under_beta0"] if r["allowed_for_K_to_K"]])
    for label, block in result["pair_monomial_selection"].items():
        print(label, "allowed", [r["monomial"] for r in block["allowed_monomials"]])
    print("Diagonal balanced counts:", result["four_node_diagonal_balanced"]["diagonal_balanced_counts_by_receiver"])


if __name__ == "__main__":
    main()
