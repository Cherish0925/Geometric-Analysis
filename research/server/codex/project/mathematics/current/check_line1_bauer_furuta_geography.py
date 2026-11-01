#!/usr/bin/env python3
"""Exact finite checks for the BF geography application, not a PDE proof."""

from fractions import Fraction as Q
from itertools import product

import sympy as s


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    h0, f0, u0 = Q(19, 300), Q(961, 900), Q(105, 89)
    x0, y0 = Q(781, 180225), Q(42533, 2883600)
    require(x0 + 4 * y0 == h0, "surgery balance")
    require(u0 + 15 * x0 - 12 * y0 == f0, "chirality balance")
    require(Q(9, 89) - x0 == Q(196, 2025), "positive signature")
    require(Q(1, 3) - h0 == Q(27, 100) > Q(1, 4), "old-band slack")
    require((1 - 3 * h0) == Q(9, 10) ** 2, "rational root")
    require((4 - Q(9, 10)) ** 2 / 9 == f0, "envelope endpoint")
    require(0 < Q(31, 27) < 2, "derivative comparison")

    n, k, m, r, A = s.symbols("n k m r A", integer=True)
    euler, signature = 124 * n - 2 + k - 2 * m, 36 * n - k
    require(s.expand(2 * euler + 3 * signature)
            == 356 * n - 4 - k - 4 * m, "positive topology")
    require(s.expand(2 * euler - 3 * signature)
            == 140 * n - 4 + 5 * k - 4 * m, "negative topology")
    require(s.expand((A-k) - (A-4*(r-1)-k-4*m))
            == 4 * (r - 1 + m), "virtual-dimension budget")
    require(s.expand(euler - (2 - 2*m + (80*n-2) + (44*n-2+k)))
            == 0, "Betti Euler identity")
    require(s.expand(signature - ((80*n-2) - (44*n-2+k))) == 0,
            "Betti signature identity")

    # Vertices certify extrema of each affine function on [0,2]^2.
    corrections = [-15*a + 12*b + 36 for a,b in product((0,2), repeat=2)]
    losses = [a + 4*b + 12 for a,b in product((0,2), repeat=2)]
    require(min(corrections) == 6 and max(corrections) == 60,
            "uniform affine correction bounds")
    require(min(losses) == 12 and max(losses) == 22, "h loss bounds")
    require(60 + 2*22 == 104, "envelope difference bound")

    # Exact rational samples validate the implementation of floors and parity.
    # The proof for all n uses the affine bounds above, not this sample.
    for j in (1, 2, 10, 100, 1000, 10000, 10**7):
        budget = 356 * j
        kj = 2 * (x0 * budget // 2)
        mj = 2 * (y0 * budget // 2) - 4
        alpha = x0*budget - kj
        beta = y0*budget - mj - 4
        hj = Q(4+kj+4*mj, budget)
        uj = Q(3*(140*j-4+5*kj-4*mj), budget)
        require(0 <= alpha < 2 and 0 <= beta < 2, "floor remainder")
        require(hj == h0-(alpha+4*beta+12)/budget, "exact h identity")
        require(uj == f0+(-15*alpha+12*beta+36)/budget,
                "exact U identity")
        require(kj % 2 == mj % 2 == 0, "even surgery counts")
        bplus, bminus = 80*j-2, 44*j-2+kj
        require((1-mj+bplus) % 2 == (1-mj+bminus) % 2 == 1,
                "two-orientation almost-complex obstruction")
        if hj > 0:
            # Squaring positive quantities gives a rational check F(hj)<Uj.
            # F(h)<u iff sqrt(1-3h)>4-3sqrt(u) is less convenient;
            # monotonicity suffices: hj<h0 and uj>F(h0).
            require(hj < h0 and uj > f0, "classical-envelope slack")
        require(Q(36*j-kj,budget) > 0, "positive signature floor check")

    # Sensitivity checks: the BF join costs four, not zero; each handle
    # subtracts four from both T signs, and a blowup adds five to T_minus.
    wrong_plus = 356*n-k-4*m
    wrong_minus = 140*n-4+5*k+4*m
    require(s.expand(wrong_plus-(2*euler+3*signature)) == 4,
            "missing BF join must be detected")
    require(s.expand(wrong_minus-(2*euler-3*signature)) == 8*m,
            "wrong handle sign must be detected")
    print("PASS: 9 rational balances; 5 topology identities; affine bounds;")
    print("      7 exact floor/parity samples; 2 wrong-formula sensitivity checks.")
    print("Scope: exact algebra only; BF, geography and PDE inputs are cited proofs.")


if __name__ == "__main__":
    main()
