#!/usr/bin/env python3
"""Exact scaling checks only; these do not verify the compactness/PDE proof."""

from fractions import Fraction


def curvature_mass_exponent(dimension: int, exponent: Fraction) -> Fraction:
    # For g_hat = rho^-2 g: |Rm_hat| = rho^2 |Rm| and dV_hat = rho^-n dV.
    return 2 * exponent - dimension


def main() -> None:
    for q in [Fraction(3, 2), Fraction(2), Fraction(201, 100), Fraction(3), Fraction(9)]:
        power = curvature_mass_exponent(4, q)
        assert (power > 0) == (q > 2)
        assert (power == 0) == (q == 2)
    assert curvature_mass_exponent(4, Fraction(2)) == 0
    print("PASS: one-sided supercritical decay and critical full-energy invariance")

    # Curvature-(0,4) scales as c and its norm uses four inverse metrics.
    tensor_norm_squared_c_power = 2 - 4
    assert tensor_norm_squared_c_power == -2
    rho_norm_power = Fraction(-2) * tensor_norm_squared_c_power / 2
    assert rho_norm_power == 2
    assert 2 * rho_norm_power - 4 == 0
    print("PASS: curvature tensor norm scales by rho^2 under rho^-2 metric scaling")

    # Scalar monopole lower bound: 32*pi^2*A <= 16*(1+delta)^2*V.
    volume_coefficient = Fraction(32, 16) / (1 + Fraction(1, 2)) ** 2
    assert volume_coefficient == Fraction(8, 9)
    print("PASS: gauge budget gives V >= (8/9)*pi^2*A for delta <= 1/2")

    wrong_power = 4 - 2 * Fraction(3)
    assert wrong_power < 0  # The reversed scaling would not force ASD at blow-up.
    assert curvature_mass_exponent(4, Fraction(2)) != 2
    print("PASS: reversed scaling and false critical decay are rejected")


if __name__ == "__main__":
    main()
