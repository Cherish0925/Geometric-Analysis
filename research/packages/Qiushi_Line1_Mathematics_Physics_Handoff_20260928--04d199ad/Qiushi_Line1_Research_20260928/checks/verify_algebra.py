#!/usr/bin/env python3
"""Exact finite-algebra checks for the Qiushi Line 1 handoff.

Run with Python 3 and SymPy: python checks/verify_algebra.py
These identities do NOT verify I40/I41, any geometric existence theorem,
or the novelty of proposed physics results. No floating-point tolerances.
"""
from __future__ import annotations

import sys

try:
    import sympy as sp
except ImportError:
    raise SystemExit("SymPy is required. Install it with: python -m pip install sympy")


def check_zero(name: str, expression: sp.Expr) -> None:
    residual = sp.simplify(sp.expand(expression))
    if residual != 0:
        raise AssertionError(f"{name}: nonzero residual {residual}")
    print(f"PASS: {name}")


def main() -> int:
    P, D, C, V, S1, S2, lam = sp.symbols("P D C V S1 S2 lam", real=True)
    R = P + S2 / 4
    check_zero(
        "E = J + scalar variance / R (R != 0, V > 0)",
        4 - S1**2 / (V * R) - (4 * P + S2 - S1**2 / V) / R,
    )

    z = sp.symbols("z", real=True)  # z = 1/lambda
    residual_polynomial = R * z**2 / V - 2 * S1 * z / V + 4
    z_opt = S1 / R
    check_zero("Einstein residual quadratic minimization", sp.diff(residual_polynomial, z).subs(z, z_opt))
    check_zero("Einstein residual infimum value", residual_polynomial.subs(z, z_opt) - (4 - S1**2 / (V * R)))

    q1, q2, q3 = sp.symbols("q1 q2 q3", real=True)
    q4 = -(q1 + q2 + q3)
    B2 = sum((q1 + qi)**2 / 4 for qi in (q2, q3, q4))
    check_zero("Chiral curvature block |B|^2 = |Ric0|^2/4", B2 - (q1**2 + q2**2 + q3**2 + q4**2) / 4)

    # Generic real two-form, orientation e1^e2^e3^e4; norm=sum_{i<j} F_ij^2.
    a, b, c, d, e, f = sp.symbols("a b c d e f", real=True)
    x = sp.Matrix([a, b, c, d, e, f])
    star_x = sp.Matrix([f, -e, d, c, -b, a])
    F = sp.Matrix([[0, a, b, c], [-a, 0, d, e], [-b, -d, 0, f], [-c, -e, -f, 0]])
    norm_F2 = (x.T * x)[0]
    T = F * F.T - sp.eye(4) * norm_F2 / 2
    plus2 = ((x + star_x).T * (x + star_x))[0] / 4
    minus2 = ((x - star_x).T * (x - star_x))[0] / 4
    norm_T2 = sum(T[i, j]**2 for i in range(4) for j in range(4))
    check_zero("Maxwell stress is trace-free", sp.trace(T))
    check_zero("Generic Euclidean Maxwell |T|^2=4|F+|^2|F-|^2", norm_T2 - 4 * plus2 * minus2)

    KC = sp.Rational(9, 2) + sp.Rational(9, 8) * C
    sharper_rhs = sp.Rational(9, 2) * P + sp.Rational(9, 8) * C * (P + D) - D
    check_zero("Gap bound slack equals (11/2)D >= 0", KC * (P + D) - sharper_rhs - sp.Rational(11, 2) * D)

    eps, X = sp.symbols("eps X", real=True)
    # X = Lambda^2 V > 0; equality in 4P/(P+4X) >= eps gives this threshold.
    P_threshold = 4 * eps * X / (4 - eps)
    check_zero("Trace-free matter threshold P/(Lambda^2 V)", 4 * P_threshold / (P_threshold + 4 * X) - eps)

    apr = sp.symbols("alpha_prime", real=True)
    beta_loss = apr**2 * R - 2 * apr * lam * S1 + 4 * lam**2 * V
    lam_opt = apr * S1 / (4 * V)
    check_zero("One-loop RG: projection away from uniform scale", beta_loss.subs(lam, lam_opt) - apr**2 * (P + (S2 - S1**2 / V) / 4))

    r = sp.symbols("r", positive=True)
    for power in (0, 1, 2, 3):
        check_zero(f"Four-dimensional curvature power {power} scaling", r**4 * (r**-2)**power - r**(4 - 2 * power))
    print("All finite algebra checks passed. Analytic/geometric statements require their original proofs.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except AssertionError as error:
        print(f"FAIL: {error}", file=sys.stderr)
        sys.exit(1)
