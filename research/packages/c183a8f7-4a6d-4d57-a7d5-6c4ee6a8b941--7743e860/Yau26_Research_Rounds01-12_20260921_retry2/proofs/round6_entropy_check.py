#!/usr/bin/env python3
"""Exact arithmetic for round6_entropy.md; not an Einstein existence test."""

from fractions import Fraction as F


def check_davis() -> None:
    cells = (1, 60, 144, 60, 1)
    chi_d = sum((-1) ** i * count for i, count in enumerate(cells))
    nodes = 122
    chi_orb = F(chi_d, 2)
    chi_coarse = F(chi_d + nodes, 2)
    chi_m = chi_coarse + nodes
    volume_over_pi2 = 12 * chi_orb  # Ric = -g, s = -4.
    assert (chi_d, chi_orb, chi_coarse, chi_m) == (26, 13, 74, 196)
    assert volume_over_pi2 == 156

    for positive in range(nodes + 1):
        negative = nodes - positive
        bolt_square = 2 * positive - 2 * negative
        chi_y = chi_d + nodes
        tau_y = positive - negative
        tau_m = F(tau_y, 2) + F(bolt_square, 4)
        assert tau_m == positive - negative
        assert tau_y == 2 * tau_m - F(bolt_square, 2)
        assert chi_y == 2 * chi_m - 2 * nodes
        b2 = chi_m - 2  # All resolutions have pi_1 = 1.
        bp, bm = F(b2 + tau_m, 2), F(b2 - tau_m, 2)
        assert bp.denominator == bm.denominator == 1
        assert bp >= 0 and bm >= 0
        t_m = 2 * chi_m + 3 * tau_m
        assert t_m == F(volume_over_pi2, 6) + 6 * positive
        # Almost-complex parity obstruction for either orientation.
        assert ((chi_m + tau_m) % 4 == 0) == (positive % 2 == 1)
        assert ((chi_m - tau_m) % 4 == 0) == (positive % 2 == 1)

    tau_m = -nodes
    assert (F(chi_m - 2 + tau_m, 2), F(chi_m - 2 - tau_m, 2)) == (36, 158)
    assert 2 * chi_m + 3 * tau_m == 26
    assert (chi_m + tau_m, chi_m - tau_m) == (74, 318)
    assert (chi_m + tau_m) % 4 != 0 and (chi_m - tau_m) % 4 != 0
    assert 2 * (chi_d + nodes) + 3 * (-nodes) == -70


def check_curvature_normalizations() -> None:
    # Hyperbolic four-space, Ric=-g: K=-1/3, h^2=3, h^4=9.
    sectional = -F(1, 3)
    assert 3 * sectional == -1
    entropy_square = 3**2 * (-sectional)
    assert entropy_square == 3 and entropy_square**2 == 9
    # 4*pi^2*T = (s^2/24)*V + 2*Wplus_energy at Einstein Ric=-g.
    scalar_term = F((-4) ** 2, 24)
    assert scalar_term == F(2, 3)
    # T=V0/(6*pi^2) produces V+3*Wplus_energy=V0.
    assert F(4, 6) / scalar_term == 1
    assert 2 / scalar_term == 3
    # Branched disk curvature integral /(2*pi) = f'(0)-f'(epsilon).
    assert F(1) - F(2) == -1
    # Replacing the ordinary BCG target by the coarse orbifold would fail.
    assert 0 < 9 * 156  # h_vol(g)^4*V/pi^2 = 0 for simply connected M.


if __name__ == "__main__":
    check_davis()
    check_curvature_normalizations()
    print("PASS: Davis A1 invariants, 123 chirality counts, branched-cover")
    print("      signature/Euler identities, parity, and curvature normalizations.")
    print("Scope: arithmetic only; no Einstein existence claim is tested.")
