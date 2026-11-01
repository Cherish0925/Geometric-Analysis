#!/usr/bin/env python3
"""
Step 85: Make the inter-node Green-response object executable without
collapsing it to the scalar-pole recipe.

This script does NOT compute Ozuch's full coefficient c_opp-c_same.  It builds
an explicit scalarized quadrupole-to-quadratic-jet transfer model for the object

    c_ij^eps = L_i G_P^perp S_j^eps,

where the H^4 source is represented by its degree-2 multipole tensor and the
receiver radial functional by a second-jet tensor.  The model uses the exact
product S^2 x S^2 scalar resolvent with additive denominators and simultaneous
antipodal invariant projection.  Tensor components are propagated as scalar
components with a common algebraic shift; this is a validation/proxy block, not
Ozuch's full Lichnerowicz operator on scalar/vector/tensor sectors.

Scientific purposes:
  * derive source and receiver factors from multipole and second-jet data;
  * show that |m|=2/second-jet channels from all ell>=2 are present;
  * test convergence/regularization behavior of differentiated inter-node sums;
  * expose whether a scalarized transfer matrix is diagonal in the C_ab basis
    (it is not generally diagonal under point separation/frame transport);
  * provide a harness into which the real sectorwise Lichnerowicz blocks can be
    inserted later.

Session S0910A01.  Agent3 / Actuator.  Phase Execute.
"""
from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

OUT = Path("Sessions/S0910A01/workspace/data/step85_green_transfer_scalarized_proxy.json")

# -----------------------------------------------------------------------------
# SD/ASD basis and C_ab = omega_a^+ omega_b^- symmetric tracefree matrices
# -----------------------------------------------------------------------------

def wedge(i: int, j: int, n: int = 4) -> np.ndarray:
    A = np.zeros((n, n), dtype=float)
    A[i, j] = 1.0
    A[j, i] = -1.0
    return A

# Zero-based coordinates: first S^2 tangent = (0,1), second S^2 tangent = (2,3)
e12 = wedge(0, 1)
e13 = wedge(0, 2)
e14 = wedge(0, 3)
e23 = wedge(1, 2)
e24 = wedge(1, 3)
e34 = wedge(2, 3)

omega_plus = [e12 + e34, e13 - e24, e14 + e23]
omega_minus = [e12 - e34, e13 + e24, e14 - e23]
C = np.array([[omega_plus[a] @ omega_minus[b] for b in range(3)] for a in range(3)])

# Insertion direction omega_2 in one-based notation; zero-based index 1.
zeta = 1
receiver_family = [C[zeta, k] for k in range(3)]      # C_{2k}: O_1^+ receiver factors
source_same_family = [C[zeta, j] for j in range(3)]   # C_{2j}: H^4(zeta^+) source factors
source_opp_family = [C[j, zeta] for j in range(3)]    # C_{j2}: H^4(zeta^-) source factors

# -----------------------------------------------------------------------------
# Sparse polynomial arithmetic for one-factor Legendre expansions near pole pairs
# variables for one factor: receiver u0,u1 and source v0,v1.
# -----------------------------------------------------------------------------
Exp4 = Tuple[int, int, int, int]
Poly4 = Dict[Exp4, float]
Exp8 = Tuple[int, int, int, int, int, int, int, int]
Poly8 = Dict[Exp8, float]


def poly_add(p: Poly4, q: Poly4, scale: float = 1.0) -> Poly4:
    out = dict(p)
    for e, c in q.items():
        out[e] = out.get(e, 0.0) + scale * c
        if abs(out[e]) < 1e-15:
            out.pop(e, None)
    return out


def poly_scale(p: Poly4, a: float) -> Poly4:
    if a == 0:
        return {}
    return {e: a * c for e, c in p.items() if abs(a * c) > 1e-15}


def poly_mul(p: Poly4, q: Poly4, max_total: int = 4) -> Poly4:
    out: Poly4 = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(e1[i] + e2[i] for i in range(4))  # type: ignore
            if sum(e) <= max_total and max(e) <= 4:
                out[e] = out.get(e, 0.0) + c1 * c2
    return {e: c for e, c in out.items() if abs(c) > 1e-15}


def mon4(exp: Exp4, coeff: float) -> Poly4:
    return {exp: coeff} if abs(coeff) > 1e-15 else {}


def legendre_endpoint_values(l: int, endpoint_sign: int) -> Tuple[float, float, float]:
    """P_l(s), P_l'(s), P_l''(s) for s=±1."""
    assert endpoint_sign in (1, -1)
    p0 = 1.0 if endpoint_sign == 1 else float((-1) ** l)
    d1_at_1 = 0.5 * l * (l + 1)
    if endpoint_sign == 1:
        p1 = d1_at_1
    else:
        p1 = float((-1) ** (l + 1)) * d1_at_1
    if l < 2:
        d2_at_1 = 0.0
    else:
        d2_at_1 = (l + 2) * (l + 1) * l * (l - 1) / 8.0
    p2 = d2_at_1 if endpoint_sign == 1 else float((-1) ** l) * d2_at_1
    return p0, p1, p2


def one_factor_poly(l: int, endpoint_sign: int, A_tuple: Tuple[float, float, float, float]) -> Poly4:
    """Expansion to total degree 4 of P_l(z(u,v)) at a pole pair.

    endpoint_sign = base_x dot base_y = +1 for same pole, -1 for antipodal.
    A is the 2x2 tangent dot-product matrix between receiver and source frames:
         u^T A v.
    """
    A = np.array(A_tuple, dtype=float).reshape(2, 2)
    s = float(endpoint_sign)
    p0, p1, p2 = legendre_endpoint_values(l, endpoint_sign)

    # delta_2 = -s/2(|u|^2+|v|^2) + u^T A v
    d2: Poly4 = {}
    for i in range(2):
        eu = [0, 0, 0, 0]
        eu[i] = 2
        d2 = poly_add(d2, mon4(tuple(eu), -0.5 * s))
        ev = [0, 0, 0, 0]
        ev[2 + i] = 2
        d2 = poly_add(d2, mon4(tuple(ev), -0.5 * s))
    for i in range(2):
        for j in range(2):
            e = [0, 0, 0, 0]
            e[i] = 1
            e[2 + j] = 1
            d2 = poly_add(d2, mon4(tuple(e), float(A[i, j])))

    # delta_4 = s/4 |u|^2 |v|^2 + s/24(|u|^4+|v|^4) - (u^T A v)(|u|^2+|v|^2)/6
    d4: Poly4 = {}
    # |u|^2 |v|^2
    for i in range(2):
        for j in range(2):
            e = [0, 0, 0, 0]
            e[i] += 2
            e[2 + j] += 2
            d4 = poly_add(d4, mon4(tuple(e), 0.25 * s))
    # |u|^4 and |v|^4 terms
    for i in range(2):
        e = [0, 0, 0, 0]
        e[i] = 4
        d4 = poly_add(d4, mon4(tuple(e), s / 24.0))
        e = [0, 0, 0, 0]
        e[2 + i] = 4
        d4 = poly_add(d4, mon4(tuple(e), s / 24.0))
    # cross square pieces 2 u0^2 u1^2 and 2 v0^2 v1^2
    d4 = poly_add(d4, mon4((2, 2, 0, 0), s / 12.0))
    d4 = poly_add(d4, mon4((0, 0, 2, 2), s / 12.0))
    # -(uAv)(|u|^2 + |v|^2)/6
    for i in range(2):
        for j in range(2):
            for k in range(2):
                e = [0, 0, 0, 0]
                e[i] += 1
                e[2 + j] += 1
                e[k] += 2
                d4 = poly_add(d4, mon4(tuple(e), -float(A[i, j]) / 6.0))
                e = [0, 0, 0, 0]
                e[i] += 1
                e[2 + j] += 1
                e[2 + k] += 2
                d4 = poly_add(d4, mon4(tuple(e), -float(A[i, j]) / 6.0))

    poly: Poly4 = {(0, 0, 0, 0): p0}
    poly = poly_add(poly, poly_scale(d2, p1))
    poly = poly_add(poly, poly_scale(d4, p1))
    poly = poly_add(poly, poly_scale(poly_mul(d2, d2), 0.5 * p2))
    # Keep only terms with degree <=2 in receiver variables and <=2 in source variables,
    # because D_R^x D_Q^y uses exactly two x and two y derivatives in the full product.
    filtered = {}
    for e, c in poly.items():
        if e[0] <= 2 and e[1] <= 2 and e[2] <= 2 and e[3] <= 2:
            filtered[e] = c
    return filtered


@lru_cache(maxsize=None)
def one_factor_poly_cached(l: int, endpoint_sign: int, A_tuple: Tuple[float, float, float, float]) -> Tuple[Tuple[Exp4, float], ...]:
    p = one_factor_poly(l, endpoint_sign, A_tuple)
    return tuple(sorted(p.items()))


def embed_factor_poly(poly_items: Tuple[Tuple[Exp4, float], ...], factor: int) -> Poly8:
    """Embed one-factor variables into full product variables.

    Full variables: receiver x0,x1,x2,x3, source y0,y1,y2,y3.
    factor=0 uses x0,x1,y0,y1; factor=1 uses x2,x3,y2,y3.
    """
    out: Poly8 = {}
    for e4, c in poly_items:
        e8 = [0] * 8
        if factor == 0:
            e8[0], e8[1], e8[4], e8[5] = e4
        else:
            e8[2], e8[3], e8[6], e8[7] = e4
        out[tuple(e8)] = c
    return out


def poly8_mul(p: Poly8, q: Poly8) -> Poly8:
    out: Poly8 = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(e1[i] + e2[i] for i in range(8))  # type: ignore
            # Full derivative needs total x-degree <=2 and total y-degree <=2.
            if sum(e[:4]) <= 2 and sum(e[4:]) <= 2:
                out[e] = out.get(e, 0.0) + c1 * c2
    return {e: c for e, c in out.items() if abs(c) > 1e-12}


def factorial_multi(e: Tuple[int, ...]) -> int:
    prod = 1
    for a in e:
        prod *= math.factorial(a)
    return prod


def derivative_contraction(l1: int, l2: int, relation: str, R: np.ndarray, Q: np.ndarray,
                           frame_choice: str = "ambient") -> float:
    """Compute D_R^receiver D_Q^source [P_l1(z1) P_l2(z2)] at nodes.

    relation:
      adjacent_NS: receiver NN, source NS (same first factor, antipodal second)
      diagonal_SS: receiver NN, source SS (antipodal in both factors)
      same_NN: receiver NN, source NN (singular; used only for algebra tests)

    frame_choice controls the tangent dot matrix A at antipodal factor.  'ambient'
    uses the same ambient e1,e2 at N and S, so A=I.  'antipodal_derivative'
    uses A=-I for antipodal factors.  The true Ozuch coefficient must fix this
    by geometric chart transport; this script reports sensitivity.
    """
    I = (1.0, 0.0, 0.0, 1.0)
    minusI = (-1.0, 0.0, 0.0, -1.0)
    A_same = I
    A_anti = I if frame_choice == "ambient" else minusI

    if relation == "adjacent_NS":
        s1, A1 = 1, A_same
        s2, A2 = -1, A_anti
    elif relation == "diagonal_SS":
        s1, A1 = -1, A_anti
        s2, A2 = -1, A_anti
    elif relation == "same_NN":
        s1, A1 = 1, A_same
        s2, A2 = 1, A_same
    else:
        raise ValueError(relation)

    p1 = embed_factor_poly(one_factor_poly_cached(l1, s1, A1), 0)
    p2 = embed_factor_poly(one_factor_poly_cached(l2, s2, A2), 1)
    prod = poly8_mul(p1, p2)

    total = 0.0
    # Sum over ordered indices: R_ab Q_cd ∂_{x_a x_b y_c y_d}.
    for a in range(4):
        for b in range(4):
            Rab = R[a, b]
            if abs(Rab) < 1e-15:
                continue
            for c in range(4):
                for d in range(4):
                    Qcd = Q[c, d]
                    if abs(Qcd) < 1e-15:
                        continue
                    e = [0] * 8
                    e[a] += 1
                    e[b] += 1
                    e[4 + c] += 1
                    e[4 + d] += 1
                    et = tuple(e)
                    coeff = prod.get(et, 0.0)
                    if coeff:
                        total += Rab * Qcd * coeff * factorial_multi(et)
    return float(total)


def transfer_matrix_scalarized(Lmax: int, relation: str, heat_tau: float, shift: float,
                               frame_choice: str = "ambient", quotient_even: bool = True,
                               half_rough_laplacian: bool = True) -> np.ndarray:
    """9x9 scalarized transfer matrix from C_ab source to C_cd receiver.

    Entry [(cd),(ab)] is <C_cd, C_ab>_component times derivative transfer
    D_{C_cd,C_ab} of the scalar product resolvent.  This deliberately keeps
    derivative and tensor-component factors separate; it is the first bridge
    beyond the Step84 identity Gram.
    """
    mats = [C[a, b] for a in range(3) for b in range(3)]
    T = np.zeros((9, 9), dtype=float)
    for l1 in range(Lmax + 1):
        lam1 = l1 * (l1 + 1)
        for l2 in range(Lmax + 1):
            if quotient_even and ((l1 + l2) % 2 == 1):
                continue
            lam2 = l2 * (l2 + 1)
            rough = 0.5 * (lam1 + lam2) if half_rough_laplacian else (lam1 + lam2)
            denom = rough + shift
            if abs(denom) < 1e-12:
                continue
            heat = math.exp(-heat_tau * (lam1 + lam2))
            # Lifted invariant quotient kernel: K_Q = K_cover(p,q)+K_cover(Ap,q)
            inv_factor = 2.0 if quotient_even else 1.0
            coeff = inv_factor * ((2 * l1 + 1) * (2 * l2 + 1)) / (16.0 * math.pi ** 2) * heat / denom
            if abs(coeff) < 1e-18:
                continue
            # Precompute derivative contractions for all R,Q at this l-pair.
            D = np.zeros((9, 9), dtype=float)
            for r, R in enumerate(mats):
                for q, Q in enumerate(mats):
                    D[r, q] = derivative_contraction(l1, l2, relation, R, Q, frame_choice=frame_choice)
            # Component propagation under scalarized identity on tensor components.
            Gcomp = np.array([[float(np.trace(mats[r] @ mats[q])) for q in range(9)] for r in range(9)])
            T += coeff * Gcomp * D
    return T


def family_coefficient(T: np.ndarray, source_family, receiver_family) -> float:
    mats = [C[a, b] for a in range(3) for b in range(3)]
    index = {(a, b): 3 * a + b for a in range(3) for b in range(3)}
    # identify matrices by exact trace against basis: C_ab orthogonal norm 4.
    def mat_index(M):
        vals = [np.trace(M @ B) for B in mats]
        return int(np.argmax(np.abs(vals)))
    rec_idx = [mat_index(M) for M in receiver_family]
    src_idx = [mat_index(M) for M in source_family]
    val = 0.0
    for r in rec_idx:
        for q in src_idx:
            val += T[r, q]
    return float(val)


def offdiag_stats(T: np.ndarray) -> dict:
    diag = np.diag(T)
    off = T - np.diag(diag)
    return {
        "fro_norm": float(np.linalg.norm(T)),
        "diag_fro_norm": float(np.linalg.norm(diag)),
        "offdiag_fro_norm": float(np.linalg.norm(off)),
        "offdiag_over_total": float(np.linalg.norm(off) / np.linalg.norm(T)) if np.linalg.norm(T) else None,
        "max_abs": float(np.max(np.abs(T))),
        "max_offdiag_abs": float(np.max(np.abs(off))),
    }


def compute_suite():
    # Basic algebra checks
    gram = np.array([[np.trace(C[a, b] @ C[c, d]) for c in range(3) for d in range(3)] for a in range(3) for b in range(3)])
    algebra = {
        "C_basis_gram_max_offdiag": float(np.max(np.abs(gram - np.diag(np.diag(gram))))),
        "C_basis_diag_values": sorted(set(round(float(x), 12) for x in np.diag(gram))),
        "C_basis_rank": int(np.linalg.matrix_rank(np.array([C[a, b].reshape(-1) for a in range(3) for b in range(3)]))),
    }

    # Report which l channels survive for a pure within-factor quadrupole at same/antipodal pole.
    # This reproduces A02's warning that second jets at a pole see every l>=2.
    second_jet_channels = []
    Q_within = np.diag([1.0, -1.0, 0.0, 0.0])
    R_within = Q_within.copy()
    for l in range(0, 13):
        val_same = derivative_contraction(l, 0, "same_NN", R_within, Q_within, frame_choice="ambient")
        # one-factor test: use l on factor1 and l2=0; singular full relation only as derivative-channel algebra.
        second_jet_channels.append({"l": l, "same_pole_factor_second_jet_value_l2_0": val_same})

    runs = []
    # Heat regularization and truncation grid.  These are pilots, not certified tails.
    Lmax_values = [8, 12, 16, 24, 32]
    heat_values = [0.08, 0.04, 0.02, 0.01]
    shifts = [0.5, 1.0, 2.0]
    relations = ["adjacent_NS", "diagonal_SS"]
    frames = ["ambient", "antipodal_derivative"]
    for relation in relations:
        for frame in frames:
            for shift in shifts:
                for heat_tau in heat_values:
                    # Use Lmax large enough relative to heat; report convergence by several Lmax values.
                    vals = []
                    for Lmax in Lmax_values:
                        T = transfer_matrix_scalarized(Lmax, relation, heat_tau, shift, frame_choice=frame)
                        cs = family_coefficient(T, source_same_family, receiver_family)
                        co = family_coefficient(T, source_opp_family, receiver_family)
                        vals.append({
                            "Lmax": Lmax,
                            "c_same_proxy": cs,
                            "c_opp_proxy": co,
                            "diff_opp_minus_same_proxy": co - cs,
                            "transfer_stats": offdiag_stats(T),
                        })
                    runs.append({
                        "relation": relation,
                        "frame_choice": frame,
                        "operator_model": "scalar component resolvent with additive denominator 1/(0.5*(l1(l1+1)+l2(l2+1))+shift)",
                        "shift": shift,
                        "heat_tau": heat_tau,
                        "Lmax_sequence": vals,
                    })

    # One representative transfer matrix for inspection.
    T_rep = transfer_matrix_scalarized(24, "adjacent_NS", 0.02, 1.0, frame_choice="ambient")
    labels = [f"C{a+1}{b+1}" for a in range(3) for b in range(3)]
    rep_entries = []
    for i in range(9):
        for j in range(9):
            if abs(T_rep[i, j]) > 1e-8:
                rep_entries.append({"receiver": labels[i], "source": labels[j], "value": float(T_rep[i, j])})
    rep_entries_sorted = sorted(rep_entries, key=lambda x: -abs(x["value"]))[:30]

    result = {
        "scope": "scalarized quadrupole-to-second-jet transfer proxy; not the Ozuch coefficient",
        "object_made_explicit": "c_ij^epsilon = L_i G_P^perp S_j^epsilon; this script models S and L as H^4 quadrupole/receiver radial C_ab tensors and G_P as scalar-component product resolvent",
        "source_receiver_factors": {
            "receiver_plus_radial_family": "R_k=N_k=C_{2k}, k=1..3 (zero-based row zeta=1)",
            "same_chirality_source_family": "Q_j=M_j=C_{2j}",
            "opposite_chirality_source_family": "Q_j=M_j=C_{j2}",
            "coefficient_formula_in_model": "sum_{k,j} tr(N_k M_j) * D_{R_k,Q_j} G_scalar_product",
            "why_not_scalar_pole_recipe": "D_{R,Q} differentiates the product Green kernel twice at source and receiver; modes with zero value at a pole can contribute through gradients/Hessians, and the transfer matrix need not be diagonal in C_ab.",
        },
        "algebra": algebra,
        "second_jet_channel_probe": {
            "description": "A pure factor second-jet derivative sees l>=2 channels; values grow with l, so pole values alone are insufficient.",
            "channels_l_0_to_12": second_jet_channels,
        },
        "representative_transfer_matrix_adjacent_heat002_shift1_L24": {
            "stats": offdiag_stats(T_rep),
            "largest_entries": rep_entries_sorted,
        },
        "regularized_runs": runs,
        "interpretation": {
            "established": [
                "The source/receiver bridge can be written as a fourth-derivative product spectral sum with additive denominators.",
                "The scalarized transfer matrix is not generally diagonal in the C_ab basis after inter-node propagation and frame choices.",
                "Heat regularization and truncation materially affect differentiated sums; no l<=20 sufficiency is supported by these data.",
                "The Step84 8/3 local Gram identity is reproduced only if the Green transfer is replaced by an identity/local pairing; it is not the computed transfer coefficient."
            ],
            "not_established": [
                "No value here is c_opp-c_same for Ozuch's full P operator.",
                "Scalar, vector, derived tensor, zero/negative mode, Bianchi and kernel-projection blocks are not yet included.",
                "Frame transport and normalization are reported as sensitivity parameters, not fixed geometric conventions."
            ],
            "next_mathematical_insertions": [
                "Replace scalar-component denominator by the full product Lichnerowicz sector blocks on trace/scalar-derived, vector-derived, TT-derived and shape sectors.",
                "Project away invariant zero modes and treat the negative shape eigenmode in the pseudo-inverse before summing.",
                "Derive the exact Bianchi-corrected source S_j^epsilon=P(chi O^4 + corrections) as a distributional multipole and the exact radial receiver functional L_i from Ozuch's curvature-jet formula."
            ]
        }
    }
    return result


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result = compute_suite()
    OUT.write_text(json.dumps(result, indent=2))
    # Print a compact summary for terminal logs.
    rep = result["representative_transfer_matrix_adjacent_heat002_shift1_L24"]
    print(json.dumps({
        "output": str(OUT),
        "scope": result["scope"],
        "C_basis_rank": result["algebra"]["C_basis_rank"],
        "representative_stats": rep["stats"],
        "sample_run_last_values": [
            {
                "relation": r["relation"],
                "frame": r["frame_choice"],
                "shift": r["shift"],
                "heat_tau": r["heat_tau"],
                "last": r["Lmax_sequence"][-1],
            }
            for r in result["regularized_runs"]
            if r["shift"] == 1.0 and r["heat_tau"] in (0.04, 0.02) and r["frame_choice"] == "ambient"
        ][:4],
    }, indent=2))
    print(f"Wrote {OUT}")
