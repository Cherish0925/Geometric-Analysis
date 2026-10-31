#!/usr/bin/env python3
"""Exact finite-dimensional identities used in round12_global.md.

Run: python round12_global_check.py
Requires SymPy; does not verify gauge theory, adjunction or the neck sequence.
"""

import json

import sympy as s


def main():
    chi = s.symbols("chi", positive=True)
    q = s.symbols("Q", positive=True)
    t = s.symbols("t", real=True, nonzero=True)
    plane_gram = s.Matrix([[0, chi], [chi, 0]])
    canonical_change = s.Matrix([[1, 1], [1, -1]])
    assert canonical_change * plane_gram * canonical_change.T == s.diag(2*chi, -2*chi)

    # c = t a + r, a^2 = c^2 = Q, r^2 = 0.
    a_dot_r = q * (1 - t**2) / (2*t)
    assert s.simplify(t**2*q + 2*t*a_dot_r - q) == 0
    a_dot_c = t*q + a_dot_r
    assert s.simplify(a_dot_c - q*(t + 1/t)/2) == 0
    positive_square = q**2 * (t**2 - 1)**2 / (4*t**2)
    assert s.factor(a_dot_c**2 - q**2 - positive_square) == 0
    assert s.solve(t**2 - 1, t) == [-1, 1]
    assert all(s.simplify(a_dot_r.subs(t, sign)) == 0 for sign in [-1, 1])

    h = s.Matrix([[2, 1], [1, 1]])
    f = s.diag(h, h)
    shear = s.Matrix([1, 0, 0, 0])
    neck_image = (s.eye(4) - f.T).row_join(shear)
    assert (s.eye(4) - f).det() == 1
    assert neck_image.rank() == 4
    assert 5 - neck_image.rank() == 1
    print(json.dumps({
        "passed": True,
        "canonical_gram": "diag(2 chi, -2 chi)",
        "square_excess": str(positive_square),
        "equality_parameters": [-1, 1],
        "example_neck_dimension": 1,
        "scope": "Exact algebra and rank only; analytic and topological hypotheses remain in the proof."
    }, indent=2))


if __name__ == "__main__":
    main()
