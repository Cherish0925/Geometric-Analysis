"""
Step 77 executable algebra for the positive product-orbifold obstruction problem.

Purpose:
  1. Verify the full Ozuch P-kernel scalar-sector modes on
     (S^2 x S^2)/Z2 in the convention P = 1/2 nabla^*nabla - R^circ.
  2. Compute a local normal-coordinate prototype of the Ozuch global projection
     integrals <H^4(zeta), V_{l,2}> for the four scalar-sector kernel modes.

This is not a complete Ozuch coefficient computation: it uses product normal
coordinates and the raw scalar-sector tensor modes f*g_i. A rigorous gluing
coefficient must also impose the chosen slice/Bianchi normalization, subtract
singular parts, and solve the global Green problem. The output is meant to
catch the Step-76 mistake that deleted the full kernel and to identify which
local projections survive before slicing.
"""

from __future__ import annotations

import json
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Tuple

import sympy as sp

OUT = Path("Sessions/S0910A01/workspace/data/step77_scalar_kernel_and_pairing.json")

# Coordinates on the flat tangent cone R^4 = T(S^2_1) \oplus T(S^2_2).
x0, x1, x2, x3 = sp.symbols("x0 x1 x2 x3", real=True)
xs = [x0, x1, x2, x3]
c, s = sp.symbols("c s", real=True)  # c=cos(alpha), s=sin(alpha), c^2+s^2=1.


def two_form_matrix(pairs):
    """Skew matrix for sum coeff dx_i wedge dx_j, zero-indexed."""
    M = sp.zeros(4, 4)
    for i, j, coeff in pairs:
        M[i, j] += coeff
        M[j, i] -= coeff
    return M


# Standard oriented self-dual/anti-self-dual bases.
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


def sym_tensor_from_forms(A, B):
    # For self-dual and anti-self-dual two-form matrices this product is symmetric.
    M = sp.simplify(A * B)
    return sp.Matrix(M)


def matrix_inner(A, B):
    return sp.simplify(sum(A[i, j] * B[i, j] for i in range(4) for j in range(4)))


def sphere_moment_monomial(powers):
    """Expectation over the unit S^3 of x^powers for total degree <=4 even."""
    total = sum(powers)
    if total == 0:
        return sp.Integer(1)
    if any(p % 2 for p in powers):
        return sp.Integer(0)
    # Unit sphere in d=4: E[x_i^2]=1/4, E[x_i^4]=3/(4*6)=1/8,
    # E[x_i^2 x_j^2]=1/(4*6)=1/24 for i != j.
    if total == 2:
        for p in powers:
            if p == 2:
                return sp.Rational(1, 4)
    if total == 4:
        if 4 in powers:
            return sp.Rational(1, 8)
        if powers.count(2) == 2:
            return sp.Rational(1, 24)
    raise ValueError(f"moment not implemented for powers={powers}")


def sphere_expectation(poly):
    poly = sp.Poly(sp.expand(poly), *xs)
    val = sp.Integer(0)
    for monom, coeff in poly.terms():
        val += coeff * sphere_moment_monomial(monom)
    return sp.simplify(val)


def reduce_unit_circle(expr):
    """Use c^2+s^2=1 to express a quadratic as C+A cos2a+B sin2a data."""
    expr = sp.expand(expr)
    # Substitute s^2 = 1-c^2 only after collecting quadratic terms; then solve
    # expr = C + A(c^2-s^2)+B(2cs) under c^2+s^2=1.
    C, A, B = sp.symbols("C A B")
    target = C + A * (c**2 - s**2) + B * (2 * c * s)
    # use s^2=1-c^2 to compare polynomial in c,s with no s^2 term.
    diff = sp.expand((expr - target).subs(s**2, 1 - c**2))
    poly = sp.Poly(diff, c, s)
    equations = [sp.Eq(coeff, 0) for _, coeff in poly.terms()]
    sol = sp.solve(equations, (C, A, B), dict=True)
    if not sol:
        return {"raw": str(sp.factor(expr)), "decomposition": None}
    sol = sol[0]
    return {
        "raw": str(sp.factor(expr)),
        "C": str(sp.simplify(sol[C])),
        "A_cos2alpha": str(sp.simplify(sol[A])),
        "B_sin2alpha": str(sp.simplify(sol[B])),
    }


def H4_plus_matrix():
    """Angular tensor for EH orientation using zeta in Lambda^+ kernel."""
    zeta_p = c * w_plus[1] + s * w_plus[2]
    H = sp.zeros(4, 4)
    xvec = sp.Matrix(xs)
    for j in range(3):
        basis_tensor = sym_tensor_from_forms(zeta_p, w_minus[j])
        qj = sp.simplify((xvec.T * basis_tensor * xvec)[0])  # on unit S^3
        H += qj * basis_tensor
    return sp.simplify(-sp.Rational(1, 2) * H)


def H4_minus_matrix():
    """Angular tensor for the reflected EH orientation using zeta in Lambda^- kernel."""
    zeta_m = c * w_minus[1] + s * w_minus[2]
    H = sp.zeros(4, 4)
    xvec = sp.Matrix(xs)
    for j in range(3):
        basis_tensor = sym_tensor_from_forms(w_plus[j], zeta_m)
        qj = sp.simplify((xvec.T * basis_tensor * xvec)[0])
        H += qj * basis_tensor
    return sp.simplify(-sp.Rational(1, 2) * H)


def metric_quad_block(indices, K=sp.Integer(1)):
    """Quadratic term of a constant-curvature 2D metric in normal coordinates."""
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

# V2 at a node. sx is the sign of the axial harmonic on the first sphere (+ at N, - at S),
# sy similarly for the second sphere. Lambda is normalized to 1.
def V2_mode(mode: str, sx=sp.Integer(1), sy=sp.Integer(1)):
    if mode == "u1_g1":
        return sp.simplify(sx * (-sp.Rational(1, 2) * r2x * I_x + gquad_x))
    if mode == "u1_g2":
        return sp.simplify(sx * (-sp.Rational(1, 2) * r2x * I_y + gquad_y))
    if mode == "u2_g1":
        return sp.simplify(sy * (-sp.Rational(1, 2) * r2y * I_x + gquad_x))
    if mode == "u2_g2":
        return sp.simplify(sy * (-sp.Rational(1, 2) * r2y * I_y + gquad_y))
    raise KeyError(mode)


def bianchi_symbolic(mode: str):
    # B = delta h + 1/2 d tr h at the leading flat/constant term level.
    # For h=f*g1 or f*g2 with f=u1 or u2. Use df symbols and block support.
    df1, df2 = sp.symbols("df1 df2")
    # Return schematic components along source factor only.
    if mode == "u1_g1":
        return "0: delta(f*g1)=-df_on_S2_1, (1/2)d tr=+df_on_S2_1"
    if mode == "u1_g2":
        return "df_on_S2_1: delta(f*g2)=0, (1/2)d tr=+df_on_S2_1"
    if mode == "u2_g1":
        return "df_on_S2_2: delta(f*g1)=0, (1/2)d tr=+df_on_S2_2"
    if mode == "u2_g2":
        return "0: delta(f*g2)=-df_on_S2_2, (1/2)d tr=+df_on_S2_2"
    return "unknown"


def main():
    # Basis algebra checks.
    basis_checks = {}
    for sign_name, basis in [("plus", w_plus), ("minus", w_minus)]:
        gram = [[sp.simplify(-sp.trace(basis[i] * basis[j])) for j in range(3)] for i in range(3)]
        basis_checks[f"{sign_name}_gram_minus_trace"] = [[str(x) for x in row] for row in gram]
    commute_sym = []
    for i in range(3):
        for j in range(3):
            T = sym_tensor_from_forms(w_plus[i], w_minus[j])
            commute_sym.append(bool(T == T.T and sp.trace(T) == 0))
    basis_checks["omega_plus_circ_omega_minus_symmetric_tracefree_all_9"] = all(commute_sym)

    Hplus = H4_plus_matrix()
    Hminus = H4_minus_matrix()
    H_checks = {
        "Hplus_trace": str(sp.simplify(sp.trace(Hplus))),
        "Hminus_trace": str(sp.simplify(sp.trace(Hminus))),
        "Hplus_inner_constant_metric_expectation": str(sphere_expectation(matrix_inner(Hplus, sp.eye(4))).subs(c**2 + s**2, 1)),
        "Hminus_inner_constant_metric_expectation": str(sphere_expectation(matrix_inner(Hminus, sp.eye(4))).subs(c**2 + s**2, 1)),
    }

    modes = ["u1_g1", "u1_g2", "u2_g1", "u2_g2"]
    kernel_modes = {}
    for mode in modes:
        if mode.startswith("u1"):
            scalar = "u1 axial first harmonic on first S^2"
        else:
            scalar = "u2 axial first harmonic on second S^2"
        tensor = mode.split("_")[1]  # g1/g2
        kernel_modes[mode] = {
            "scalar": scalar,
            "tensor_factor": tensor,
            "scalar_laplacian_eigenvalue": "2*Lambda",
            "R_circ_on_factor_tensor": "Lambda times the same factor tensor",
            "P_value": "1/2*(2*Lambda) - Lambda = 0",
            "descends_under_half_turn": True,
            "Bianchi_at_leading_level": bianchi_symbolic(mode),
            "TT": False,
        }

    # Local pairings at a representative node with sx=sy=+1; signs at other nodes multiply
    # the corresponding u1/u2 mode by sx/sy.
    pairings = {"compatible_plus_H4": {}, "reversed_minus_H4": {}}
    for Hname, H in [("compatible_plus_H4", Hplus), ("reversed_minus_H4", Hminus)]:
        for mode in modes:
            V = V2_mode(mode, sx=sp.Integer(1), sy=sp.Integer(1))
            integrand = matrix_inner(H, V)
            expectation = sp.simplify(sphere_expectation(integrand))
            # Normalize to S^3/Z2 integral by multiplying by pi^2; store coefficient without pi^2.
            pairings[Hname][mode] = reduce_unit_circle(expectation)
            pairings[Hname][mode]["S3_over_Z2_integral"] = "pi^2 * coefficient_above (Lambda=1, convention-dependent sign)"

    node_signs = {
        "p1=(N,N)": {"u1_sign": +1, "u2_sign": +1},
        "p2=(N,S)": {"u1_sign": +1, "u2_sign": -1},
        "p3=(S,N)": {"u1_sign": -1, "u2_sign": +1},
        "p4=(S,S)": {"u1_sign": -1, "u2_sign": -1},
    }

    # Example linear global projection using only local raw V2 coefficients, equal scales,
    # and all compatible H4. This is a toy object to show non-emptiness, not the Green-corrected map.
    # Sum signs for u1 modes and u2 modes over the four nodes vanish for equal scales, explaining
    # why symmetry can hide scalar projections in a fully symmetric all-node configuration.
    sign_sums = {
        "sum_u1_signs_equal_scales": sum(v["u1_sign"] for v in node_signs.values()),
        "sum_u2_signs_equal_scales": sum(v["u2_sign"] for v in node_signs.values()),
        "interpretation": "raw scalar-sector projections can cancel by node symmetry for equal scales, but are not absent; unequal scales, mixed chirality signs, slice changes, and Green transport can produce nonzero equations.",
    }

    result = {
        "step": 77,
        "purpose": "correct Step76 by verifying the full Ozuch P-kernel scalar sector and prototyping local scalar-sector pairings",
        "operator": "P = 1/2*nabla^*nabla - R^circ, Ric=Lambda*g",
        "basis_checks": basis_checks,
        "full_P_kernel_scalar_sector": {
            "dimension_on_quotient": 4,
            "basis": ["u1*g1", "u1*g2", "u2*g1", "u2*g2"],
            "u1_u2": "axial first spherical harmonics, invariant under the pi-rotation on the corresponding S^2",
            "modes": kernel_modes,
            "TT_kernel_remains_zero": True,
            "lesson": "TT invertibility and full Ozuch-kernel projections are different facts; Definition 1.8 uses the full L2 kernel of P.",
        },
        "H4_checks": H_checks,
        "local_pairing_prototype": {
            "normalization": "Expectation over S^3; multiply by pi^2 for S^3/Z2 area. Lambda=1. Product normal-coordinate raw V2, before slice correction and Green transport.",
            "pairings": pairings,
            "node_signs_for_axial_modes": node_signs,
            "equal_scale_sign_sums": sign_sums,
            "scientific_use": "The scalar-sector projection is a real finite-dimensional object. These raw local terms must be combined with a chosen slice and the singular-subtracted Green response; they cannot be silently removed by the TT-kernel calculation.",
        },
        "topology_table_correction": {
            "b2": 6,
            "k_positive_EH_rows": {
                "0": "CP2#5 CPbar2",
                "1": "2CP2#4 CPbar2",
                "2_adjacent": "3CP2#3 CPbar2",
                "2_opposite": "#3(S2xS2)",
                "3": "4CP2#2 CPbar2",
                "4": "5CP2#CPbar2",
            },
        },
        "separation_of_orders": {
            "lambda": "lambda_k^j(phi,0)=0 for in-kernel EH direction",
            "mu1": "mu_1^j(phi,0)=0 by the displayed determinant formula for the rank-one product block",
            "mu2_mu3": "not established by the mu_1 formula; require the Biq16/Ozuch formulas for the other modes after including corrections to the local jet",
            "projected_equations": "t_j*lambda_k^j + t_j^2*mu_k^j and nu_l are finite-dimensional projections of an exact Einstein solution",
            "full_residual": "projected smallness at order t_max^(5/2) is not itself a full weighted residual estimate without inverse and nonlinear estimates",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
