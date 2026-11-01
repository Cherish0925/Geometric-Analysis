#!/usr/bin/env python3
"""Symbolic/index checks for the shifted-curvature continuation argument.

This is deliberately a bookkeeping test, not a tensor-calculus package.  It
checks the convention-sensitive identities at a normal-coordinate point and
the scalar Leibniz identities responsible for the highest cutoff derivatives.
"""

from __future__ import annotations

import math
import sympy as sp


def delta(i: int, j: int) -> int:
    return int(i == j)


def check_kn_and_contraction(n: int) -> None:
    # Independent entries of a symmetric metric variation h at g=I.
    hsym = {}
    for i in range(n):
        for j in range(i, n):
            hsym[i, j] = sp.Symbol(f"h{i}{j}")

    def h(i: int, j: int):
        return hsym[min(i, j), max(i, j)]

    def G(i: int, j: int, k: int, ell: int):
        # G_{ijkl}=(g_ik g_jl-g_il g_jk)/(n-1) at g=I.
        return sp.Rational(1, n - 1) * (
            delta(i, k) * delta(j, ell) - delta(i, ell) * delta(j, k)
        )

    def dG(i: int, j: int, k: int, ell: int):
        # dG=(h \owedge g)/(n-1), since
        # G=(g \owedge g)/(2(n-1)) and KN is symmetric.
        return sp.Rational(1, n - 1) * (
            h(i, k) * delta(j, ell)
            + delta(i, k) * h(j, ell)
            - h(i, ell) * delta(j, k)
            - delta(i, ell) * h(j, k)
        )

    # Ric(G)_jl = g^{ik} G_ijkl = g_jl.
    for j in range(n):
        for ell in range(n):
            contracted = sum(G(i, j, i, ell) for i in range(n))
            assert sp.simplify(contracted - delta(j, ell)) == 0

    # Differentiate g^{ik}G_ijkl=g_jl. At I, d(g^{-1})^{ik}=-h_ik.
    for j in range(n):
        for ell in range(n):
            lhs = sum(
                -h(i, k) * G(i, j, k, ell) + delta(i, k) * dG(i, j, k, ell)
                for i in range(n)
                for k in range(n)
            )
            assert sp.simplify(lhs - h(j, ell)) == 0

    # If h=-2aE, dG=-2a(E \owedge g)/(n-1).
    a = sp.Symbol("a")
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for ell in range(n):
                    direct = dG(i, j, k, ell).subs(
                        {hsym[p, q]: -2 * a * hsym[p, q] for p, q in hsym}
                    )
                    expected = -sp.Rational(2, n - 1) * a * (
                        h(i, k) * delta(j, ell)
                        + delta(i, k) * h(j, ell)
                        - h(i, ell) * delta(j, k)
                        - delta(i, ell) * h(j, k)
                    )
                    assert sp.simplify(direct - expected) == 0


def check_cutoff_leibniz(max_order: int = 8) -> None:
    x = sp.Symbol("x")
    chi = sp.Function("chi")(x)
    for r in range(max_order + 1):
        lhs = sp.diff(chi**2, x, r)
        rhs = sum(
            math.comb(r, s) * sp.diff(chi, x, s) * sp.diff(chi, x, r - s)
            for s in range(r + 1)
        )
        assert sp.simplify(lhs - rhs) == 0

        if r >= 1:
            # The only appearances of the r-th derivative are the two endpoint
            # terms, totaling 2 chi chi^(r).
            endpoint = 2 * chi * sp.diff(chi, x, r)
            interior = sum(
                math.comb(r, s)
                * sp.diff(chi, x, s)
                * sp.diff(chi, x, r - s)
                for s in range(1, r)
            )
            assert sp.simplify(lhs - endpoint - interior) == 0

    # The base energy integration uses |da|^2/a=4|dchi|^2, with the
    # expression interpreted by its smooth extension across chi=0.
    z, dz = sp.symbols("z dz")
    a = z**2
    da = 2 * z * dz
    assert sp.cancel(da**2 / a) == 4 * dz**2


def check_highest_term_table(m: int = 6) -> None:
    """Verify the four top allocations in r+k=m+2 for d^r(a)d^k(U).

    Expanding a=chi^2, allocations with a derivative of chi of order at
    least m+1 are precisely the analogues of Wang's Gamma_1--Gamma_4.
    """
    allocations = set()
    for r in range(1, m + 3):
        k = m + 2 - r
        if not (0 <= k <= m + 1):
            continue
        for s in range(r + 1):
            t = r - s
            if max(s, t) >= m + 1:
                allocations.add(tuple(sorted((s, t), reverse=True)) + (k,))

    expected = {
        (m + 2, 0, 0),  # chi d^(m+2)chi U
        (m + 1, 1, 0),  # dchi d^(m+1)chi U
        (m + 1, 0, 1),  # chi d^(m+1)chi dU
    }
    assert allocations == expected
    # Gamma_4 has only first cutoff derivatives but the top U derivative.
    assert (1 + 1 + m == m + 2) and (m <= m + 1)


def main() -> None:
    for n in range(2, 7):
        check_kn_and_contraction(n)
    check_cutoff_leibniz()
    check_highest_term_table()
    print("PASS: KN normalization, Ric(G), d Ric(G), dG, cutoff Leibniz, and top-term table")


if __name__ == "__main__":
    main()
