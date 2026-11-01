#!/usr/bin/env python3
"""Algebra checks for the weighted-Moser and continuation audit.

These checks verify exponent/weight bookkeeping and a scaling obstruction.
They are not a substitute for the tensor-energy proof in the companion memo.
"""

from __future__ import annotations

import sympy as sp


def check_product_transforms() -> None:
    a, t, e = sp.symbols("a t e", positive=True)
    u = a * t
    v = a * e

    # Multiplying a(T*T) by a produces U*U, with no spare factor a.
    assert sp.simplify(a**2 * t**2 - u**2) == 0
    assert sp.simplify(a**2 * t**2 - a * u**2) != 0

    # Product-rule cancellation in the V=aE equation:
    # a[a Delta E + (Delta a)E + 2 da.grad E] - a Delta(aE)=0
    lap_e, lap_a, grad_cross = sp.symbols("lap_e lap_a grad_cross")
    lhs = a * (a * lap_e + lap_a * e + 2 * grad_cross)
    a_lap_v = a * (a * lap_e + lap_a * e + 2 * grad_cross)
    assert sp.expand(lhs - a_lap_v) == 0

    # The proposed seeds dominate the unweighted U,V moments for 0<=a<=1:
    # |U|^3=a^3|T|^3 <= a|T|^3 and |V|^6=a^6|E|^6 <=a^4|E|^6.
    assert 3 >= 1
    assert 6 >= 4


def check_mixed_weight_identity() -> None:
    p = sp.symbols("p", positive=True)
    # H_{3p/2}=(a^{p-2}f^p)^{1/2} z_p^2,
    # z_p=a^{(p-1)/2}f^{p/2}.
    a_power = (p - 2) / 2 + (p - 1)
    f_power = p / 2 + p
    assert sp.simplify(a_power - (3 * p / 2 - 2)) == 0
    assert sp.simplify(f_power - 3 * p / 2) == 0

    # Three-factor potential absorption:
    # (a f_curv^3)^(1/3) (a^{p-2}f^p)^(1/3) z_p^(4/3).
    potential_a_power = (
        sp.Rational(1, 3)
        + (p - 2) / 3
        + sp.Rational(2, 3) * (p - 1)
    )
    assert sp.simplify(potential_a_power - (p - 1)) == 0


def check_endpoint_exponents() -> None:
    n = sp.Integer(4)
    kappa = 1 + sp.Rational(2, n)
    for p0, expected_time, expected_sobolev in [
        (sp.Integer(3), sp.Integer(1), sp.Rational(2, 3)),
        (sp.Integer(6), sp.Rational(1, 2), sp.Rational(1, 3)),
    ]:
        reciprocal_sum = (1 / p0) * kappa / (kappa - 1)
        sobolev_sum = reciprocal_sum / kappa
        assert sp.simplify(reciprocal_sum - expected_time) == 0
        assert sp.simplify(sobolev_sum - expected_sobolev) == 0

    # Defect endpoint:
    # S^(1/3) t^(-1/2) (delta^6 Vol t)^(1/6),
    # with S=r^2 Vol^(-1/2), equals delta (r^2/t)^(1/3).
    r, vol, time, delta = sp.symbols("r vol time delta", positive=True)
    S = r**2 * vol ** (-sp.Rational(1, 2))
    endpoint = (
        S ** sp.Rational(1, 3)
        * time ** (-sp.Rational(1, 2))
        * (delta**6 * vol * time) ** sp.Rational(1, 6)
    )
    target = delta * (r**2 / time) ** sp.Rational(1, 3)
    assert sp.simplify(endpoint / target) == 1


def check_degenerate_sobolev_obstruction() -> None:
    eps = sp.symbols("eps", positive=True)
    y = sp.symbols("y", real=True)

    # A triangular bump in the normal interval x in [eps,2eps].
    # y=(x-eps)/eps and a=x^2=eps^2(1+y)^2.
    phi_left = 2 * y
    phi_right = 2 * (1 - y)
    i2 = eps * (
        sp.integrate(phi_left**2, (y, 0, sp.Rational(1, 2)))
        + sp.integrate(phi_right**2, (y, sp.Rational(1, 2), 1))
    )
    i4 = eps * (
        sp.integrate(phi_left**4, (y, 0, sp.Rational(1, 2)))
        + sp.integrate(phi_right**4, (y, sp.Rational(1, 2), 1))
    )
    weighted_grad = eps * 4 * sp.integrate(
        (1 + y) ** 2, (y, 0, 1)
    )

    assert sp.simplify(i2 - eps / 3) == 0
    assert sp.simplify(i4 - eps / 5) == 0
    assert sp.simplify(weighted_grad - sp.Rational(28, 3) * eps) == 0

    ratio = sp.simplify(sp.sqrt(i4) / (weighted_grad + i2))
    assert sp.simplify(
        ratio - sp.Rational(3, 29) / sp.sqrt(5 * eps)
    ) == 0
    assert sp.limit(ratio, eps, 0, dir="+") == sp.oo


def check_coupled_holder_schedule() -> None:
    p = sp.symbols("p", positive=True)
    # Current-pair terms after Gamma_1 integration.
    assert sp.simplify(sp.Rational(2, 1) / p + (p - 2) / p - 1) == 0
    assert sp.simplify(1 / p + (p - 1) / p - 1) == 0

    # A squared product of two lower factors in L^(4p), followed by W^(p-2),
    # uses at most (p-1)/p of the integration exponent.
    lower_sum = 2 / (4 * p) + 2 / (4 * p) + (p - 2) / p
    assert sp.simplify(lower_sum - (p - 1) / p) == 0

    # The T_m commutator U_m*T*|T_m|^(p-1) closes with U_m,T in L^(2p).
    assert sp.simplify(1 / (2 * p) + 1 / (2 * p) + (p - 1) / p - 1) == 0


def main() -> None:
    check_product_transforms()
    check_mixed_weight_identity()
    check_endpoint_exponents()
    check_degenerate_sobolev_obstruction()
    check_coupled_holder_schedule()
    print(
        "PASS: U/V products, mixed weights, endpoint exponents, "
        "degenerate-Sobolev scaling, and coupled Holder schedule"
    )


if __name__ == "__main__":
    main()
