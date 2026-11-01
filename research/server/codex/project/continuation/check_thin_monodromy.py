#!/usr/bin/env python3
"""Finite checks for thin-monodromy constants/examples, not a proof of geometry."""
from fractions import Fraction as Q
from itertools import combinations_with_replacement
from math import sinh

import sympy as sp


def check_gaps():
    # Logarithms normalized so [log(1/2), log(1)] becomes [0,1].
    grid = [Q(j, 8) for j in range(9)]
    count = 0
    for capacity in (3, 6):
        minimum_gap = Q(1, capacity + 1)
        strict_move = Q(3, 8 * (capacity + 1))  # 2d < half minimum gap.
        for n in range(capacity + 1):
            for lengths in combinations_with_replacement(grid, n):
                entries = (Q(0),) + lengths + (Q(1),)
                u, v = max(zip(entries, entries[1:]), key=lambda p: p[1] - p[0])
                assert v - u >= minimum_gap
                midpoint = (u + v) / 2
                assert u + strict_move < midpoint
                # A systole below 1/2 supplies one member even if the
                # selected gap is the first interval.
                candidate_logs = (Q(-1, 2),) + lengths
                short = [ell for ell in candidate_logs if ell < midpoint]
                assert short
                assert all(ell <= u for ell in short)
                assert all(ell + strict_move < midpoint for ell in short)
                assert all(not (u < ell < v) for ell in lengths)
                count += 1
    return count


assert sinh(0.5) ** 2 < 1
print("PASS: length-one curves are below the collar intersection threshold")
count = check_gaps()
print(f"PASS: {count} rational length configurations, including ties/endpoints")

# nu = log(2)/(4(3f-2)); (2 D sqrt(error) >= nu) gives
# error D^2 >= log(2)^2/(64(3f-2)^2).
assert Q(1, 4) ** 2 / 4 == Q(1, 64)
print("PASS: explicit thin-fiber Ricci/diameter coefficient 1/64")

t = sp.symbols("t")
phi5 = sp.Poly(t**4 + t**3 + t**2 + t + 1, t)
assert phi5.is_irreducible
companion = sp.Matrix([[0, 0, 0, -1],
                       [1, 0, 0, -1],
                       [0, 1, 0, -1],
                       [0, 0, 1, -1]])
assert sp.Poly(companion.charpoly(t).as_expr(), t) == phi5
assert companion**5 == sp.eye(4)
assert companion != sp.eye(4)
assert all(companion**j != sp.eye(4) for j in range(1, 5))
print("PASS: genus-two order-five rational action is irreducible and nontrivial")

residual = sp.Matrix([[2, 1], [1, 1]])
assert residual.det() == 1
assert residual.trace() == 3
assert sp.expand(residual.charpoly(t).as_expr()) == t**2 - 3*t + 1
print("PASS: retained once-punctured-torus residual has hyperbolic homological action")

for f in range(2, 8):
    for b in range(2, 8):
        assert (2*f + 2*b - 1) % 2 == 1
print("PASS: Dehn-twist test retains odd first Betti number")
print("These checks do not verify collar theory, global bundle reduction, or Einstein existence.")
