"""Exact arithmetic for Teicher Y_0(7,4); not a geometric existence proof."""

from fractions import Fraction
from math import factorial


def verify_teicher_control():
    a, b, k = 7, 4, 0
    n = 2 * a * b + k * b**2
    ek = -2 * a - 2 * b - k * b
    branch = 3 * n + ek
    canonical_coefficient = Fraction(branch, 2) - 3

    # Theorem 5.2, with c1^2(F_0)=8 and c2(F_0)=4.
    c1_coefficient = Fraction(
        ek**2 + 6 * n * ek + 9 * n**2 - 12 * ek - 36 * n + 36, 4
    )
    c2_coefficient = Fraction(
        72 - 10 * 8 - 54 * ek - 114 * n + 27 * n**2
        + 14 * 4 + 3 * ek**2 + 18 * n * ek,
        24,
    )

    # Corollary 5.4 is an independent displayed specialization to F_0.
    c1_specialized = (3 * a * b - a - b - 3) ** 2
    c2_specialized = Fraction(
        4 + 9 * a + 9 * b - 17 * a * b + a**2 + b**2
        + 9 * a**2 * b**2 - 6 * a**2 * b - 6 * a * b**2,
        2,
    )
    assert (n, ek, branch, canonical_coefficient) == (56, -22, 146, 70)
    assert c1_coefficient == c1_specialized == canonical_coefficient**2 == 4900
    assert c2_coefficient == c2_specialized == 2450
    assert c1_coefficient == 2 * c2_coefficient

    degree = factorial(n)
    c1sq = c1_coefficient * degree
    euler = c2_coefficient * degree
    rank_h = (euler - 2) / 2
    assert rank_h == 1225 * degree - 1
    assert rank_h.denominator == 1 and int(rank_h) % 2 == 1
    assert c1sq == 4 * (rank_h + 1)
    assert (c1sq + euler) % 12 == 0
    print("PASS: n=56, branch degree=146, K=70 f*H, K^2=4900*56!, c2=2450*56!")
    print("PASS: signature=0, hyperbolic rank=1225*56!-1 (odd), Noether integrality")


if __name__ == "__main__":
    verify_teicher_control()
