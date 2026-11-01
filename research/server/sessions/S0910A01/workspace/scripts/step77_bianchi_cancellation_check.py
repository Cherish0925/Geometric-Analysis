"""
Check the TTCS Step-77 correction: the raw normal-coordinate scalar-kernel
pairing -1/18 is canceled by the quadratic Bianchi coordinate correction.

This uses the same flat S^3 tensor conventions as step77_scalar_kernel_and_pairing.py.
It is a local algebraic unit test, not a complete Ozuch coefficient computation.
"""

from __future__ import annotations

import json
from pathlib import Path
import sympy as sp

OUT = Path("Sessions/S0910A01/workspace/data/step77_bianchi_cancellation_check.json")

x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
xs = [x0, x1, x2, x3]
c, s = sp.symbols("c s", real=True)


def two_form_matrix(pairs):
    M = sp.zeros(4, 4)
    for i, j, coeff in pairs:
        M[i, j] += coeff
        M[j, i] -= coeff
    return M

w_plus = [
    two_form_matrix([(0, 1, 1), (2, 3, 1)]),
    two_form_matrix([(0, 2, 1), (1, 3, -1)]),
    two_form_matrix([(0, 3, 1), (1, 2, 1)]),
]
w_minus = [
    two_form_matrix([(0, 1, 1), (2, 3, -1)]),
    two_form_matrix([(0, 2, 1), (1, 3, 1)]),
    two_form_matrix([(0, 3, 1), (1, 2, -1)]),
]

def sym_tensor(A, B):
    return sp.Matrix(A * B)

def matrix_inner(A, B):
    return sp.simplify(sum(A[i, j] * B[i, j] for i in range(4) for j in range(4)))

def moment(powers):
    total = sum(powers)
    if total == 0:
        return sp.Integer(1)
    if any(p % 2 for p in powers):
        return sp.Integer(0)
    if total == 2:
        return sp.Rational(1, 4)
    if total == 4:
        if 4 in powers:
            return sp.Rational(1, 8)
        if powers.count(2) == 2:
            return sp.Rational(1, 24)
    raise ValueError(powers)

def sphere_expectation(expr):
    poly = sp.Poly(sp.expand(expr), *xs)
    val = sp.Integer(0)
    for monom, coeff in poly.terms():
        val += coeff * moment(monom)
    return sp.simplify(val)

def H4_plus():
    zeta_p = c * w_plus[1] + s * w_plus[2]
    H = sp.zeros(4, 4)
    xvec = sp.Matrix(xs)
    for j in range(3):
        T = sym_tensor(zeta_p, w_minus[j])
        q = (xvec.T * T * xvec)[0]
        H += q * T
    return sp.simplify(-sp.Rational(1, 2) * H)

def H4_minus():
    zeta_m = c * w_minus[1] + s * w_minus[2]
    H = sp.zeros(4, 4)
    xvec = sp.Matrix(xs)
    for j in range(3):
        T = sym_tensor(w_plus[j], zeta_m)
        q = (xvec.T * T * xvec)[0]
        H += q * T
    return sp.simplify(-sp.Rational(1, 2) * H)

def metric_quad_block(indices, K=sp.Integer(1)):
    M = sp.zeros(4, 4)
    a, b = indices
    r2 = xs[a] ** 2 + xs[b] ** 2
    for i in indices:
        for j in indices:
            delta = 1 if i == j else 0
            M[i, j] = -K * sp.Rational(1, 3) * (r2 * delta - xs[i] * xs[j])
    return M

I_x = sp.diag(1, 1, 0, 0)
I_y = sp.diag(0, 0, 1, 1)
r2x = x0**2 + x1**2
r2y = x2**2 + x3**2
gquad_x = metric_quad_block([0, 1])
gquad_y = metric_quad_block([2, 3])

def V2_raw(mode):
    if mode == "u1_g1":
        return sp.simplify(-sp.Rational(1, 2) * r2x * I_x + gquad_x), I_x
    if mode == "u1_g2":
        return sp.simplify(-sp.Rational(1, 2) * r2x * I_y + gquad_y), I_y
    if mode == "u2_g1":
        return sp.simplify(-sp.Rational(1, 2) * r2y * I_x + gquad_x), I_x
    if mode == "u2_g2":
        return sp.simplify(-sp.Rational(1, 2) * r2y * I_y + gquad_y), I_y
    raise KeyError(mode)

def lie_X_tensor(G, A):
    # X^a = A r^2 x^a; Euclidean constant tensor G.
    r2 = sum(x*x for x in xs)
    dX = sp.zeros(4, 4)  # dX[i,k] = partial_i X^k
    for i in range(4):
        for k in range(4):
            dX[i, k] = sp.simplify(A * (2 * xs[i] * xs[k] + r2 * (1 if i == k else 0)))
    L = sp.zeros(4, 4)
    for i in range(4):
        for j in range(4):
            L[i, j] = sum(dX[i, k] * G[k, j] + dX[j, k] * G[i, k] for k in range(4))
    return sp.simplify(L)

def reduce(expr):
    return str(sp.factor(sp.expand(expr).subs(s**2, 1-c**2)))

def main():
    modes = ["u1_g1", "u1_g2", "u2_g1", "u2_g2"]
    A = -sp.Rational(1, 18)
    result = {
        "step": 77,
        "vector_field": "X^a = -(1/18) r^2 x^a in Lambda=1 units",
        "purpose": "local check that raw Riemann-normal scalar-kernel pairing is a coordinate artifact at quadratic Bianchi order",
        "pairings": {},
    }
    for Hname, H in [("Hplus", H4_plus()), ("Hminus", H4_minus())]:
        result["pairings"][Hname] = {}
        for mode in modes:
            Vraw, Gconst = V2_raw(mode)
            Lcorr = lie_X_tensor(Gconst, A)
            raw = sphere_expectation(matrix_inner(H, Vraw))
            corr = sphere_expectation(matrix_inner(H, Lcorr))
            total = sp.simplify(raw + corr)
            result["pairings"][Hname][mode] = {
                "raw_expectation": reduce(raw),
                "lie_correction_expectation": reduce(corr),
                "bianchi_corrected_total_expectation": reduce(total),
                "S3_over_Z2_integral_factor": "multiply expectations by pi^2",
            }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
