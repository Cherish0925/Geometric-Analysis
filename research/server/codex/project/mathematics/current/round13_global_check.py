#!/usr/bin/env python3
"""Exact algebra supporting the volume/continuation argument, not a PDE proof."""

import sympy as s


def main():
    n, lam, vp = s.symbols("n lam vp")
    # d int(s) along fixed-Ric Einstein metrics is (n-2)*lambda*V'.
    assert s.expand(n * lam * vp - (n - 2) * lam * vp) == 2 * lam * vp

    chi, pi = s.symbols("chi pi", positive=True)
    vstar = 4 * pi**2 * chi / 9
    qtop = 2 * chi
    assert s.simplify(144 * vstar - 32 * pi**2 * qtop) == 0
    assert s.simplify(9 * vstar - 4 * pi**2 * chi) == 0

    epsilon = s.symbols("epsilon", nonnegative=True)
    # Four eigenvalues 1+epsilon give dmu ratio (1+epsilon)^2.
    assert s.sqrt((1 + epsilon)**4) == (1 + epsilon)**2

    B, r, K = s.symbols("B r K", positive=True)
    rho = 2 * B * r
    qnewton = 2 * B**2 * K * r
    image = B * r + B * K * rho**2 / 2
    assert s.simplify(image / rho - (1 + qnewton) / 2) == 0
    assert s.simplify(B * K * rho - qnewton) == 0

    t = s.symbols("t", real=True)
    wenergy = 4 * pi**2 * chi - 3 * t * vstar
    assert s.simplify(wenergy.subs(t, 3)) == 0
    assert s.simplify(144 * t * vstar / (32 * pi**2) - qtop
                      - qtop * (t - 1)) == 0
    print("PASS: 8 exact normalization, variation, determinant, and Newton checks")


if __name__ == "__main__":
    main()
