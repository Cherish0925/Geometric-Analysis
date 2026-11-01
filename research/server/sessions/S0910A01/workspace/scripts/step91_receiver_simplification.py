#!/usr/bin/env python3
"""
Step 91: product-background receiver simplification for the chirality-odd
radial curvature functional.

Purpose.
  The previous notes left open possible V0/frame/background-curvature corrections
  in the receiver L_i.  The Strategist observed that at the product background
  R0 omega_2^+ = R0 omega_2^- = 0 and that the odd receiver selects only a
  four-distinct product-index curvature component.  This script checks the
  resulting exact algebra in product normal coordinates.

Conventions.
  Tangent frame at a node: A-factor indices 0,1 and B-factor indices 2,3.
  Raw 2-forms: omega_2^+ = e02 - e13, omega_2^- = e02 + e13.  Normalized
  curvature-operator entries use the same /8 raw contraction as Step 89.

What is verified.
  1. The product curvature R0 annihilates omega_2^+ and omega_2^- as curvature
     operator vectors.  Therefore first-order changes of frame or normalization
     have no contribution to the radial contraction.
  2. The linear odd receiver for arbitrary symmetric second jet H is exactly the
     sparse Step-89 expression
        R_odd(H)=1/2(H_01,23 - H_03,12 - H_12,03 + H_23,01),
     with no dependence on V0 or V1.
  3. All possible background curvature times h0 terms in the four-distinct odd
     component vanish for the product curvature support.  This is reported as a
     support check rather than a convention-dependent formula for every index sign.
  4. For the l=1 coexact-coexact modes, the axial *dZ_A sym *dZ_B mode is the
     only one with nonzero odd receiver in this sparse principal receiver.  The
     V0-nonzero equatorial modes have zero odd receiver here; their remaining
     issue is source/normalization matching, not an extra receiver correction.
"""
from __future__ import annotations

import json
import math
import pathlib
from fractions import Fraction
from itertools import product

import numpy as np
import sympy as sp

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)


def wedge(i: int, j: int, n: int = 4) -> np.ndarray:
    A = np.zeros((n, n), dtype=int)
    A[i, j] = 1
    A[j, i] = -1
    return A


# Raw SD/ASD basis used in Step 89; normalized by dividing by sqrt(2).
wp_raw = [wedge(0, 1) + wedge(2, 3), wedge(0, 2) - wedge(1, 3), wedge(0, 3) + wedge(1, 2)]
wm_raw = [wedge(0, 1) - wedge(2, 3), wedge(0, 2) + wedge(1, 3), wedge(0, 3) - wedge(1, 2)]
omega_p = wp_raw[1]
omega_m = wm_raw[1]


def product_curvature_R0() -> np.ndarray:
    """Round S2xS2 product curvature with R0101=R2323=1 convention."""
    R = np.zeros((4, 4, 4, 4), dtype=int)
    for a, b in [(0, 1), (2, 3)]:
        # R_abab = 1 and symmetries.
        R[a, b, a, b] = 1
        R[b, a, b, a] = 1
        R[a, b, b, a] = -1
        R[b, a, a, b] = -1
    return R


R0 = product_curvature_R0()


def curvature_operator_on_twoform(R: np.ndarray, Omega: np.ndarray) -> np.ndarray:
    # (R Omega)_{ij} = 1/2 R_{ij kl} Omega_{kl} in raw 2-form coordinates.
    out = np.zeros((4, 4), dtype=Fraction)
    for i, j, k, l in product(range(4), repeat=4):
        if R[i, j, k, l] and Omega[k, l]:
            out[i, j] += Fraction(int(R[i, j, k, l]) * int(Omega[k, l]), 2)
    return out


R0_omega_p = curvature_operator_on_twoform(R0, omega_p)
R0_omega_m = curvature_operator_on_twoform(R0, omega_m)


def block_entry_raw(R: np.ndarray, rawA: np.ndarray, rawB: np.ndarray) -> Fraction:
    """Curvature operator matrix entry for normalized raw/sqrt(2) 2-forms.

    This is the Step-89 convention: raw contraction divided by 8.
    """
    total = Fraction(0, 1)
    for i, j, k, l in product(range(4), repeat=4):
        if rawA[i, j] and rawB[k, l]:
            total += Fraction(int(rawA[i, j]) * int(rawB[k, l]), 1) * Fraction(R[i, j, k, l])
    return total / 8


def riemann_from_H(H: np.ndarray) -> np.ndarray:
    """Linearized lower-index Riemann in fixed product normal coordinates.

    H[a,b,p,q] = partial_p partial_q h_ab(0), symmetric in ab and pq.
    The formula matches Step 89.
    """
    R = np.empty((4, 4, 4, 4), dtype=object)
    for a, b, c, d in product(range(4), repeat=4):
        R[a, b, c, d] = Fraction(H[a, d, b, c] + H[b, c, a, d] - H[a, c, b, d] - H[b, d, a, c], 2)
    return R


def receiver_odd_from_H(H: np.ndarray) -> Fraction:
    dR = riemann_from_H(H)
    Rp22 = block_entry_raw(dR, omega_p, omega_p)
    Rm22 = block_entry_raw(dR, omega_m, omega_m)
    return (Rp22 - Rm22) / 2


def sparse_receiver(H: np.ndarray) -> Fraction:
    return Fraction(
        H[0, 1, 2, 3] - H[0, 3, 1, 2] - H[1, 2, 0, 3] + H[2, 3, 0, 1],
        2,
    )


def sym_hessian_basis_element(ij: tuple[int, int], pq: tuple[int, int]) -> np.ndarray:
    i, j = ij
    p, q = pq
    H = np.zeros((4, 4, 4, 4), dtype=int)
    tensor_pairs = [(i, j)] if i == j else [(i, j), (j, i)]
    deriv_pairs = [(p, q)] if p == q else [(p, q), (q, p)]
    for a, b in tensor_pairs:
        for c, d in deriv_pairs:
            H[a, b, c, d] = 1
    return H


pairs = [(i, j) for i in range(4) for j in range(i, 4)]
receiver_failures = []
nonzero_basis = []
for ij in pairs:
    for pq in pairs:
        H = sym_hessian_basis_element(ij, pq)
        Rodd = receiver_odd_from_H(H)
        S = sparse_receiver(H)
        if Rodd != S:
            receiver_failures.append({"ij": ij, "pq": pq, "receiver_odd": str(Rodd), "sparse": str(S)})
        if Rodd:
            nonzero_basis.append({"ij": ij, "pq": pq, "receiver_odd": str(Rodd)})

# Check all raw 2-form basis pairings with R0 omega_2^pm vanish, not just self-pairing.
twoform_basis = [wedge(i, j) for i in range(4) for j in range(i + 1, 4)]
R0_annihilation = {
    "omega_plus_operator_entries": [str(block_entry_raw(R0, omega_p, B)) for B in twoform_basis],
    "omega_minus_operator_entries": [str(block_entry_raw(R0, omega_m, B)) for B in twoform_basis],
    "R0_omega_plus_max_abs_num": max(abs(x.numerator) for x in R0_omega_p.reshape(-1)),
    "R0_omega_minus_max_abs_num": max(abs(x.numerator) for x in R0_omega_m.reshape(-1)),
}

# Curvature-times-h0 support check.  Any standard h0 correction to a curvature
# operator entry is a linear combination of terms obtained by replacing one index
# of a background product curvature component by an h0 contraction.  For the odd
# receiver the relevant base components involve the mixed 2-form pair (02,13).
# The product curvature is supported only on the pairs 01 and 23, hence every
# component containing one index from A and one from B in the same antisymmetric
# pair vanishes.  We verify this support statement for the relevant mixed pairs.
relevant_antisym_pairs = [(0, 2, 1, 3), (1, 3, 0, 2), (0, 2, 0, 2), (1, 3, 1, 3)]
support_terms = []
for a, b, c, d in relevant_antisym_pairs:
    # Try every replacement of one index by a dummy p.  If a background term
    # R0[..., p, ...] could be nonzero for some p, record it.
    possible = []
    for slot in range(4):
        for p in range(4):
            inds = [a, b, c, d]
            inds[slot] = p
            val = R0[tuple(inds)]
            if val:
                possible.append({"slot": slot, "p": p, "R0_value": int(val), "component": tuple(inds)})
    support_terms.append({"base_component": (a, b, c, d), "possible_R0_after_one_replacement": possible})

# l=1 coexact-coexact modes near NN, including V0-nonzero equatorial modes.
def trunc(poly, vars, maxdeg=2):
    P = sp.Poly(sp.expand(poly), *vars)
    out = 0
    for mon, coeff in P.terms():
        if sum(mon) <= maxdeg:
            term = coeff
            for v, e in zip(vars, mon):
                term *= v ** e
            out += term
    return sp.expand(out)


def sphere_coexact_forms(prefix: str):
    x, y = sp.symbols(f"{prefix}0 {prefix}1")
    vars2 = (x, y)
    r2 = x*x + y*y
    X = x - x*r2/6
    Y = y - y*r2/6
    Z = 1 - r2/2
    ginv = sp.Matrix([[1 + r2/3 - x*x/3, -x*y/3], [-x*y/3, 1 + r2/3 - y*y/3]])
    sqrtg = 1 - r2/6
    # Same convention as Step87: *dx=dy, *dy=-dx at the origin.
    star_mat = sqrtg * sp.Matrix([[-ginv[0, 1], -ginv[1, 1]], [ginv[0, 0], ginv[0, 1]]])
    out = {}
    for name, u in [("X", X), ("Y", Y), ("Z", Z)]:
        du = sp.Matrix([sp.diff(u, x), sp.diff(u, y)])
        sd = star_mat * du
        out[name] = [trunc(sd[0], vars2, 2), trunc(sd[1], vars2, 2)]
    return vars2, out


def hessian_from_polynomial_matrix(polys, vars4):
    H = np.zeros((4, 4, 4, 4), dtype=int)
    V0 = False
    V1 = False
    for i in range(4):
        for j in range(4):
            P = sp.Poly(sp.expand(polys[i][j]), *vars4)
            for mon, coeff in P.terms():
                deg = sum(mon)
                if deg == 0 and coeff:
                    V0 = True
                if deg == 1 and coeff:
                    V1 = True
                if deg == 2 and coeff:
                    inds = []
                    for k, e in enumerate(mon):
                        inds.extend([k] * e)
                    p, q = inds
                    # If p != q, polynomial coefficient c x_p x_q corresponds
                    # to Hessian entries H_pq=H_qp=c. If p=q, coefficient c x_p^2
                    # corresponds to H_pp=2c.
                    if p == q:
                        val = int(2 * coeff)
                        H[i, j, p, q] += val
                    else:
                        val = int(coeff)
                        H[i, j, p, q] += val
                        H[i, j, q, p] += val
    return H, V0, V1


def sym_product_polys(formA, formB, varsA, varsB):
    vars4 = (*varsA, *varsB)
    alpha = [formA[0], formA[1], 0, 0]
    beta = [0, 0, formB[0], formB[1]]
    polys = [[0 for _ in range(4)] for __ in range(4)]
    for i, j in product(range(4), repeat=2):
        polys[i][j] = sp.expand(alpha[i] * beta[j] + beta[i] * alpha[j])
    return polys, vars4


varsA, FA = sphere_coexact_forms("x")
varsB, FB = sphere_coexact_forms("y")
l1_receiver = []
for a in ["X", "Y", "Z"]:
    for b in ["X", "Y", "Z"]:
        polys, vars4 = sym_product_polys(FA[a], FB[b], varsA, varsB)
        H, V0, V1 = hessian_from_polynomial_matrix(polys, vars4)
        Rodd = receiver_odd_from_H(H)
        l1_receiver.append({
            "mode": f"star_d{a}_A_sym_star_d{b}_B",
            "V0_nonzero": V0,
            "V1_nonzero": V1,
            "receiver_odd": str(Rodd),
            "receiver_odd_float": float(Rodd),
            "nonzero": bool(Rodd),
        })

results = {
    "step": 91,
    "scope": "receiver simplification at product background for chirality-odd radial functional",
    "R0_annihilates_radial_forms": R0_annihilation,
    "frame_and_length_variation": {
        "statement": "First-order variation of the insertion frame, Hodge splitting, or normalization contributes 2<delta omega, R0 omega_2^pm>; all such terms vanish because R0 omega_2^pm=0.",
        "verified_operator_zero": R0_annihilation["R0_omega_plus_max_abs_num"] == 0 and R0_annihilation["R0_omega_minus_max_abs_num"] == 0,
    },
    "receiver_sparse_identity": {
        "formula": "R_odd(H)=1/2(H_01,23 - H_03,12 - H_12,03 + H_23,01)",
        "basis_dimension_symmetric_H": len(pairs) * len(pairs),
        "failures_count": len(receiver_failures),
        "failures": receiver_failures[:10],
        "nonzero_basis_entries": nonzero_basis,
        "depends_on_V0_or_V1": False,
    },
    "background_curvature_times_h0_support": {
        "statement": "Every possible one-index h0 correction to the odd mixed curvature components requires a product-curvature component with a mixed A/B antisymmetric pair; product curvature has only 01 and 23 support, so these corrections vanish.",
        "support_terms": support_terms,
        "all_possible_lists_empty": all(len(row["possible_R0_after_one_replacement"]) == 0 for row in support_terms),
    },
    "l1_coexact_receiver_census_NN": l1_receiver,
    "interpretation": [
        "The full linear chirality-odd receiver at the product background is exactly the Step-89 sparse second-jet functional in product normal coordinates.",
        "V0-nonzero eigentensors do not require an additional receiver frame/background correction in this odd component; if they contribute, it must enter through the singular source/normalization side or through a different layer, not through L_i's linear odd receiver.",
        "Among l=1 coexact-coexact product modes in this adapted NN frame, only star_dZ_A_sym_star_dZ_B has nonzero odd receiver; this preserves the axial unit test but does not compute the full Green coefficient.",
    ],
}

outpath = DATA_DIR / "step91_receiver_simplification.json"
with open(outpath, "w") as f:
    json.dump(results, f, indent=2, default=str)

print(json.dumps(results, indent=2, default=str))
print(f"Wrote {outpath}")
