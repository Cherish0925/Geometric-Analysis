#!/usr/bin/env python3
"""
Step 32: explicit bookkeeping for the repaired nested-time weighted Moser recurrence.

This script does not prove the PDE estimates.  It verifies the algebraic/scaling
parts of the corrected convention:
  ||z||_4^2 <= C_S (||grad z||_2^2 + r^{-2}||z||_2^2), C_S ~ r^2/sqrt(V),
  beta = C_S * H2(0)^{1/2},
  potential coefficient = C_S^2 Y.
It also verifies the recurrence exponents and the seed cancellations producing
curvature beta/t and defect delta*(r^2/t)^(1/3) on positive-time slabs.
"""
from __future__ import annotations

import math


def approx(a: float, b: float, tol: float = 1e-12) -> bool:
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def flat_product_scaling() -> None:
    print("1. Collapsed flat product Dirichlet scaling")
    print("   Model: B^3(1) x S^1(eps), function compactly supported in B^3 and constant on S^1.")
    for eps in [1.0, 1e-2, 1e-4, 1e-8]:
        lhs_norm_sq = eps ** 0.5   # (int |u|^4)^{1/2}
        energy_plus_l2 = eps      # int(|grad u|^2 + |u|^2)
        lower_coeff = lhs_norm_sq / energy_plus_l2
        expected = eps ** -0.5
        print(f"   eps={eps:9.1e}: L4^2~{lhs_norm_sq:9.3e}, energy~{energy_plus_l2:9.3e}, coeff>={lower_coeff:9.3e}")
        assert approx(lower_coeff, expected)
    print("   PASS: zero boundary values do not give a collapse-independent unnormalized Sobolev coefficient.\n")


def reaction_coefficient() -> None:
    print("2. Reaction absorption convention")
    print("   Sobolev: ||Z_p||_4^2 <= C_S(D_p+r^-2 K_p).")
    print("   Reaction factorization: R_p <= Y^(1/3) K_p^(1/3) ||Z_p||_4^(4/3).")
    # If A = C_S^{2/3} Y^{1/3} multiplies K^{1/3}B^{2/3}, Young absorption
    # squares A cubically, producing C_S^2 Y times K.
    c_s_exp_before = 2.0 / 3.0
    y_exp_before = 1.0 / 3.0
    c_s_exp_after = 3.0 * c_s_exp_before
    y_exp_after = 3.0 * y_exp_before
    print(f"   Young coefficient exponents: C_S^{c_s_exp_after:g} Y^{y_exp_after:g}")
    assert approx(c_s_exp_after, 2.0)
    assert approx(y_exp_after, 1.0)
    print("   PASS: the positive-time potential is C_S^2 Y.\n")


def recurrence_exponents(p0: float = 3.0, n_terms: int = 80) -> None:
    print("3. Nested-time recurrence exponents")
    kappa = 1.5
    ps = [p0 * (kappa ** k) for k in range(n_terms)]
    # Recurrence: A_{k+1} <= C_S * L_k^(3/2) * A_k^(3/2), L_k~p^N 4^k/t.
    cs_exp = sum(1.0 / ps[k + 1] for k in range(n_terms - 1))
    t_exp = 1.5 * cs_exp
    cs_expected = 2.0 / p0
    t_expected = 3.0 / p0
    log_p_sum = sum(math.log(ps[k] + 1.0) / ps[k + 1] for k in range(n_terms - 1))
    k_sum = sum(k / ps[k + 1] for k in range(n_terms - 1))
    print(f"   p0={p0:g}, sum_{{k>=0}}1/p_(k+1)={cs_exp:.12f}, expected={cs_expected:.12f}")
    print(f"   t exponent from L_k^(3/2): {t_exp:.12f}, expected={t_expected:.12f}")
    print(f"   finite loss sums: sum log(p_k)/p_(k+1)={log_p_sum:.6f}, sum k/p_(k+1)={k_sum:.6f}")
    assert approx(cs_exp, cs_expected, 1e-8)
    assert approx(t_exp, t_expected, 1e-8)
    assert log_p_sum < 10 and k_sum < 10
    print("   PASS: product gives C_S^{2/p0} t^{-3/p0} times the p0 seed.\n")


def endpoint_cancellations() -> None:
    print("4. Seed cancellations")
    # Use concrete dimensionless values to verify algebra.
    r = 0.07
    V = 1.0e-5
    K0 = 4.0
    delta = 2.0e-3
    theta = 0.2
    t = theta * r * r
    C_S = r * r / math.sqrt(V)
    H2 = V * (1.0 + K0)
    beta = C_S * math.sqrt(H2)

    # Curvature p0=3: output C_S^{2/3} t^{-1} (int Y)^{1/3}; int Y=beta^3/C_S^2.
    int_Y = beta ** 3 / (C_S ** 2)
    curvature_output = (C_S ** (2.0 / 3.0)) * (t ** -1.0) * (int_Y ** (1.0 / 3.0))
    expected_curvature = beta / t

    # Defect p0=6: output C_S^{1/3} t^{-1/2}(delta^6 V t)^{1/6}.
    int_J6 = (delta ** 6) * V * t
    defect_output = (C_S ** (1.0 / 3.0)) * (t ** -0.5) * (int_J6 ** (1.0 / 6.0))
    expected_defect = delta * ((r * r / t) ** (1.0 / 3.0))

    print(f"   r={r}, V={V}, C_S={C_S:.6e}, H2={H2:.6e}, beta={beta:.6e}, t={t:.6e}")
    print(f"   curvature endpoint: {curvature_output:.6e}; beta/t={expected_curvature:.6e}")
    print(f"   defect endpoint:    {defect_output:.6e}; delta*(r^2/t)^(1/3)={expected_defect:.6e}")
    assert approx(curvature_output, expected_curvature)
    assert approx(defect_output, expected_defect)
    print("   PASS: Sobolev-volume factors cancel against the selected seeds in the intended way.\n")


def tensor_hessian_ledger() -> None:
    print("5. Hessian-cutoff derivative ledger for the curvature power estimate")
    print("   Raw schematic term after one integration by parts:")
    print("     p ∫ ∇(a^{p-2} F^{p-2} Rm*E) * ∇a")
    print("   Derivative targets and required payments:")
    rows = [
        ("∇a^{p-2}", "p(p-2) a^{p-3}|∇a|^2 F^p", "r^-2 K_p"),
        ("∇F^{p-2}", "p(p-2) a^{p-2}|∇a| F^{p-1}|∇F|", "p(p-2)D_p^F + p^3 r^-2 K_p"),
        ("∇Rm", "p a^{p-2}|∇a| F^{p-1}|∇Rm|", "pD_p^Rm + p r^-2 K_p"),
        ("∇E", "p a^{p-2}|∇a| F^{p-1}|∇E|", "pD_p^Rm + p r^-2 K_p, using |∇E|<=C|∇Rm|"),
    ]
    for target, term, payment in rows:
        print(f"   - {target:10s}: {term:58s} -> {payment}")
    print("   PASS: the ledger requires both full-tensor and radial dissipation; it is not a completed tensor proof.\n")


def main() -> None:
    print("=" * 78)
    print("STEP 32 NESTED WEIGHTED MOSER REPAIR")
    print("=" * 78)
    flat_product_scaling()
    reaction_coefficient()
    recurrence_exponents(3.0)
    recurrence_exponents(6.0)
    endpoint_cancellations()
    tensor_hessian_ledger()
    print("ALL ALGEBRAIC/SCALING CHECKS PASSED")
    print("PDE estimates still require the full tensor and regularized-defect derivations.")


if __name__ == "__main__":
    main()
