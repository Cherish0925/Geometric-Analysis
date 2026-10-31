#!/usr/bin/env python3
"""Exact abelianizations for the two closed sheared-gluing examples.

Run: python round11_graph_topology_check.py
Requires SymPy. Checks integral presentation matrices and Smith normal
forms, not the Bass--Serre or Kähler-group theorems.
"""

import json

import sympy as s
from sympy.matrices.normalforms import smith_normal_form


def check_case(name, monodromy, shear, expected_b1, expected_b2):
    h, g = 1, 2
    identity = s.eye(2 * g)
    j2 = s.Matrix([[0, 1], [-1, 0]])
    symplectic_form = s.diag(j2, j2)
    assert monodromy.T * symplectic_form * monodromy == symplectic_form
    assert monodromy.det() == 1
    assert s.gcd_list(list(shear)) == 1

    # Columns are relations in H_1(Sigma_g) + Z c:
    #       (I - f_*) x - u(x) c = 0.
    presentation = (identity - monodromy).col_join(-shear)
    smith = smith_normal_form(presentation, domain=s.ZZ)
    diagonal = [abs(int(smith[i, i])) for i in range(min(smith.shape))]
    nonzero = [d for d in diagonal if d]
    assert all(d == 1 for d in nonzero), "Unexpected integral torsion"
    rank = presentation.rank()
    assert rank == len(nonzero)
    free_rank = presentation.rows - rank
    # The 2h handle generators and HNN letter are independent.
    b1 = 2 * h + 1 + free_rank
    chi = (-2 * h) * (2 - 2 * g)
    signature = 0
    b2 = chi - 2 + 2 * b1
    assert (chi, signature, b1, b2) == (4, 0, expected_b1, expected_b2)
    assert b2 % 2 == 0
    return {
        "case": name,
        "relation_matrix": [list(map(int, row)) for row in presentation.tolist()],
        "smith_diagonal": diagonal,
        "torsion": [],
        "chi": chi,
        "signature": signature,
        "b1": b1,
        "b2": b2,
        "b2_plus": b2 // 2,
        "b2_minus": b2 // 2,
    }


def main():
    # A nonseparating twist: b_1 -> b_1 + a_1. The shear is
    # algebraic intersection with a_1, up to the orientation convention.
    twist = s.eye(4)
    twist[0, 1] = 1
    dual_shear = s.Matrix([[0, 1, 0, 0]])
    first = check_case("single twist and dual shear", twist, dual_shear, 7, 16)
    assert first["smith_diagonal"] == [1, 0, 0, 0]

    hyperbolic = s.Matrix([[2, 1], [1, 1]])
    doubled = s.diag(hyperbolic, hyperbolic)
    assert hyperbolic.trace() == 3  # SL(2,Z), infinite order.
    assert (s.eye(4) - doubled).det() == 1
    second = check_case(
        "two hyperbolic homology blocks and primitive shear",
        doubled,
        s.Matrix([[1, 0, 0, 0]]),
        4,
        10,
    )
    assert second["smith_diagonal"] == [1, 1, 1, 1]
    print(json.dumps({"passed": True, "cases": [first, second]}, indent=2))


if __name__ == "__main__":
    main()
