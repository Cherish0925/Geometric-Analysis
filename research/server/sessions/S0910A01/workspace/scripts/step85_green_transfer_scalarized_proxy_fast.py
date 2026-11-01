#!/usr/bin/env python3
"""
Step 85 fast execution of a scalarized Green-transfer proxy for the product
orbifold (S^2 x S^2)/Z2.

This is NOT Ozuch's full c_opp-c_same.  It is an executable bridge from the
local H^4 angular algebra to the correct global form

    c_ij^eps = L_i G_P^perp S_j^eps,

using a scalar-component product resolvent as a controlled proxy.  It derives
source and receiver factors as quadrupole/second-jet tensors, uses additive
product denominators, keeps |m|=2 second-jet channels, and reports heat/truncation
sensitivity.  It deliberately does not collapse the problem to scalar pole values
or an identity Gram matrix.
"""
from __future__ import annotations

import json
import math
from functools import lru_cache
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

OUT = Path("Sessions/S0910A01/workspace/data/step85_green_transfer_scalarized_proxy_fast.json")

# -----------------------------------------------------------------------------
# SD/ASD basis and C_ab = omega_a^+ omega_b^-.
# -----------------------------------------------------------------------------

def wedge(i: int, j: int, n: int = 4) -> np.ndarray:
    A = np.zeros((n, n), dtype=float)
    A[i, j] = 1.0
    A[j, i] = -1.0
    return A

E12, E13, E14 = wedge(0, 1), wedge(0, 2), wedge(0, 3)
E23, E24, E34 = wedge(1, 2), wedge(1, 3), wedge(2, 3)
omega_plus = [E12 + E34, E13 - E24, E14 + E23]
omega_minus = [E12 - E34, E13 + E24, E14 - E23]
C = np.array([[omega_plus[a] @ omega_minus[b] for b in range(3)] for a in range(3)])
MATS = np.array([C[a, b] for a in range(3) for b in range(3)])  # (9,4,4)
LABELS = [f"C{a+1}{b+1}" for a in range(3) for b in range(3)]
GCOMP = np.einsum("rab,qba->rq", MATS, MATS)  # Frobenius inner products; symmetric C so okay

zeta = 1  # omega_2 in one-based notation
RECEIVER_IDX = [3 * zeta + k for k in range(3)]  # C_2k
SAME_SRC_IDX = [3 * zeta + j for j in range(3)]  # C_2j
OPP_SRC_IDX = [3 * j + zeta for j in range(3)]   # C_j2

# -----------------------------------------------------------------------------
# One-factor Taylor derivatives at a pair of poles.
# F[e0,e1,e2,e3] = partial_{u0^e0 u1^e1 v0^e2 v1^e3} P_l(x(u).y(v)) at 0,
# for exponents <=2 and total receiver/source order <=2.
# -----------------------------------------------------------------------------
Exp4 = Tuple[int, int, int, int]
Poly = Dict[Exp4, float]


def add(p: Poly, e: Exp4, c: float) -> None:
    if abs(c) > 1e-15:
        p[e] = p.get(e, 0.0) + c
        if abs(p[e]) < 1e-14:
            p.pop(e, None)


def mul(p: Poly, q: Poly) -> Poly:
    out: Poly = {}
    for e1, c1 in p.items():
        for e2, c2 in q.items():
            e = tuple(e1[i] + e2[i] for i in range(4))  # type: ignore
            if e[0] <= 2 and e[1] <= 2 and e[2] <= 2 and e[3] <= 2 and sum(e[:2]) <= 2 and sum(e[2:]) <= 2:
                add(out, e, c1 * c2)
    return out


def legendre_values(l: int, s: int) -> Tuple[float, float, float]:
    p0 = 1.0 if s == 1 else float((-1) ** l)
    d1 = 0.5 * l * (l + 1)
    p1 = d1 if s == 1 else float((-1) ** (l + 1)) * d1
    d2 = 0.0 if l < 2 else (l + 2) * (l + 1) * l * (l - 1) / 8.0
    p2 = d2 if s == 1 else float((-1) ** l) * d2
    return p0, p1, p2


@lru_cache(maxsize=None)
def one_factor_derivatives(l: int, s: int, frame_sign: int) -> np.ndarray:
    """Return derivative array for one S^2 factor.

    s = +1 same pole, -1 antipodal.  frame_sign=+1 means source and receiver
    tangent frames are identified by the ambient coordinate frame at antipodal
    points; frame_sign=-1 models the derivative of the antipodal map on tangent
    frames.  This sensitivity is reported because the geometric chart transport
    still has to be fixed in the true Ozuch coefficient.
    """
    A = np.eye(2) if frame_sign == 1 else -np.eye(2)
    # For same-pole relation the sign choice is irrelevant; keep A=I there.
    if s == 1:
        A = np.eye(2)
    p0, p1, p2 = legendre_values(l, s)

    d2: Poly = {}
    for i in range(2):
        e = [0, 0, 0, 0]
        e[i] = 2
        add(d2, tuple(e), -0.5 * s)
        e = [0, 0, 0, 0]
        e[2 + i] = 2
        add(d2, tuple(e), -0.5 * s)
    for i in range(2):
        for j in range(2):
            e = [0, 0, 0, 0]
            e[i] = 1
            e[2 + j] = 1
            add(d2, tuple(e), float(A[i, j]))

    d4: Poly = {}
    # s/4 |u|^2 |v|^2
    for i in range(2):
        for j in range(2):
            e = [0, 0, 0, 0]
            e[i] += 2
            e[2 + j] += 2
            add(d4, tuple(e), 0.25 * s)
    # s/24 (|u|^4+|v|^4)
    add(d4, (4, 0, 0, 0), s / 24.0)
    add(d4, (0, 4, 0, 0), s / 24.0)
    add(d4, (0, 0, 4, 0), s / 24.0)
    add(d4, (0, 0, 0, 4), s / 24.0)
    add(d4, (2, 2, 0, 0), s / 12.0)
    add(d4, (0, 0, 2, 2), s / 12.0)
    # -(uAv)(|u|^2+|v|^2)/6
    for i in range(2):
        for j in range(2):
            aij = float(A[i, j])
            for k in range(2):
                e = [0, 0, 0, 0]
                e[i] += 1
                e[2 + j] += 1
                e[k] += 2
                if max(e) <= 2 and sum(e[:2]) <= 2 and sum(e[2:]) <= 2:
                    add(d4, tuple(e), -aij / 6.0)
                e = [0, 0, 0, 0]
                e[i] += 1
                e[2 + j] += 1
                e[2 + k] += 2
                if max(e) <= 2 and sum(e[:2]) <= 2 and sum(e[2:]) <= 2:
                    add(d4, tuple(e), -aij / 6.0)

    poly: Poly = {(0, 0, 0, 0): p0}
    for e, c in d2.items():
        add(poly, e, p1 * c)
    for e, c in d4.items():
        add(poly, e, p1 * c)
    d2sq = mul(d2, d2)
    for e, c in d2sq.items():
        add(poly, e, 0.5 * p2 * c)

    F = np.zeros((3, 3, 3, 3), dtype=float)
    for e, coeff in poly.items():
        if e[0] <= 2 and e[1] <= 2 and e[2] <= 2 and e[3] <= 2 and sum(e[:2]) <= 2 and sum(e[2:]) <= 2:
            fac = math.factorial(e[0]) * math.factorial(e[1]) * math.factorial(e[2]) * math.factorial(e[3])
            F[e] = coeff * fac
    return F


def signs_for_relation(relation: str, frame: str) -> Tuple[int, int, int, int]:
    """(s1, frame_sign1, s2, frame_sign2)."""
    anti_frame = 1 if frame == "ambient" else -1
    if relation == "adjacent_NS":
        return 1, 1, -1, anti_frame
    if relation == "diagonal_SS":
        return -1, anti_frame, -1, anti_frame
    if relation == "same_NN":
        return 1, 1, 1, 1
    raise ValueError(relation)


def K_tensor(l1: int, l2: int, relation: str, frame: str) -> np.ndarray:
    s1, f1, s2, f2 = signs_for_relation(relation, frame)
    F1 = one_factor_derivatives(l1, s1, f1)
    F2 = one_factor_derivatives(l2, s2, f2)
    K = np.zeros((4, 4, 4, 4), dtype=float)
    # ordered derivatives x_a,x_b,y_c,y_d
    for a in range(4):
        for b in range(4):
            for c in range(4):
                for d in range(4):
                    e1 = [0, 0, 0, 0]
                    e2 = [0, 0, 0, 0]
                    for idx in (a, b):
                        if idx < 2:
                            e1[idx] += 1
                        else:
                            e2[idx - 2] += 1
                    for idx in (c, d):
                        if idx < 2:
                            e1[2 + idx] += 1
                        else:
                            e2[2 + idx - 2] += 1
                    if max(e1) <= 2 and max(e2) <= 2:
                        K[a, b, c, d] = F1[tuple(e1)] * F2[tuple(e2)]
    return K


def derivative_matrix(l1: int, l2: int, relation: str, frame: str) -> np.ndarray:
    K = K_tensor(l1, l2, relation, frame)
    return np.einsum("rab,qcd,abcd->rq", MATS, MATS, K, optimize=True)


def transfer_matrix(Lmax: int, relation: str, heat_tau: float, shift: float, frame: str,
                    quotient_even: bool = True) -> np.ndarray:
    T = np.zeros((9, 9), dtype=float)
    for l1 in range(Lmax + 1):
        lam1 = l1 * (l1 + 1)
        for l2 in range(Lmax + 1):
            if quotient_even and ((l1 + l2) & 1):
                continue
            lam2 = l2 * (l2 + 1)
            denom = 0.5 * (lam1 + lam2) + shift
            if abs(denom) < 1e-14:
                continue
            # Product scalar kernel coefficient on S^2 x S^2.  Invariant quotient
            # lift doubles the even modes in this normalization.  This factor cancels
            # in many comparisons but is retained explicitly.
            coeff = 2.0 * (2 * l1 + 1) * (2 * l2 + 1) / (16.0 * math.pi ** 2)
            coeff *= math.exp(-heat_tau * (lam1 + lam2)) / denom
            D = derivative_matrix(l1, l2, relation, frame)
            T += coeff * GCOMP * D
    return T


def coeffs_from_T(T: np.ndarray) -> Tuple[float, float, float]:
    # Sum over receiver radial family and source H4 family.  Normalizing signs/factors
    # are omitted consistently; only relative behavior matters in this proxy.
    csame = float(T[np.ix_(RECEIVER_IDX, SAME_SRC_IDX)].sum())
    copp = float(T[np.ix_(RECEIVER_IDX, OPP_SRC_IDX)].sum())
    return csame, copp, copp - csame


def stats(T: np.ndarray) -> dict:
    off = T - np.diag(np.diag(T))
    norm = np.linalg.norm(T)
    return {
        "fro_norm": float(norm),
        "diag_fro_norm": float(np.linalg.norm(np.diag(T))),
        "offdiag_fro_norm": float(np.linalg.norm(off)),
        "offdiag_over_total": None if norm == 0 else float(np.linalg.norm(off) / norm),
        "max_abs": float(np.max(np.abs(T))),
        "max_offdiag_abs": float(np.max(np.abs(off))),
    }


def channel_probe() -> list:
    Q = np.diag([1.0, -1.0, 0.0, 0.0])
    # one-factor second derivative of P_l at same pole in x0x0-y0y0 minus trace style
    rows = []
    for l in range(13):
        # D on full product with l on factor 1 and constant l2=0, singular relation used only as channel algebra.
        D = derivative_matrix(l, 0, "same_NN", "ambient")
        # C22 is within-factor quadrupole containing x0^2-x1^2 on both factors; use a representative nonzero entry.
        rows.append({
            "l": l,
            "nonzero_second_jet_channel": bool(abs(D[4, 4]) > 1e-12),
            "sample_D_C22_C22_l2_0": float(D[4, 4]),
            "P_l_second_derivative_at_1": 0.0 if l < 2 else float((l + 2) * (l + 1) * l * (l - 1) / 8.0),
        })
    return rows


def top_entries(T: np.ndarray, n: int = 25) -> list:
    entries = []
    for i in range(9):
        for j in range(9):
            v = float(T[i, j])
            if abs(v) > 1e-8:
                entries.append({"receiver": LABELS[i], "source": LABELS[j], "value": v})
    return sorted(entries, key=lambda x: -abs(x["value"]))[:n]


def main() -> dict:
    gram = GCOMP
    algebra = {
        "C_basis_rank": int(np.linalg.matrix_rank(MATS.reshape(9, 16))),
        "C_gram_diagonal_values": sorted(set(round(float(x), 12) for x in np.diag(gram))),
        "C_gram_max_offdiag_abs": float(np.max(np.abs(gram - np.diag(np.diag(gram))))),
        "local_step84_same_gram": [[float(np.trace(C[zeta, j] @ C[zeta, k])) for k in range(3)] for j in range(3)],
        "local_step84_cross_gram": [[float(np.trace(C[j, zeta] @ C[zeta, k])) for k in range(3)] for j in range(3)],
    }

    runs = []
    Ls = [6, 10, 14, 20, 28]
    heats = [0.08, 0.04, 0.02, 0.01, 0.005]
    shifts = [0.5, 1.0, 2.0]
    for relation in ["adjacent_NS", "diagonal_SS"]:
        for frame in ["ambient", "antipodal_derivative"]:
            for shift in shifts:
                for heat in heats:
                    seq = []
                    for L in Ls:
                        T = transfer_matrix(L, relation, heat, shift, frame)
                        cs, co, diff = coeffs_from_T(T)
                        seq.append({
                            "Lmax": L,
                            "c_same_proxy": cs,
                            "c_opp_proxy": co,
                            "diff_opp_minus_same_proxy": diff,
                            "matrix_stats": stats(T),
                        })
                    runs.append({
                        "relation": relation,
                        "frame_transport_model": frame,
                        "heat_tau": heat,
                        "shift": shift,
                        "Lmax_sequence": seq,
                    })

    rep = transfer_matrix(20, "adjacent_NS", 0.02, 1.0, "ambient")
    rep2 = transfer_matrix(20, "diagonal_SS", 0.02, 1.0, "ambient")

    result = {
        "scope": "heat-regularized scalar-component proxy, not Ozuch full P coefficient",
        "failed_predecessor": "step85_green_transfer_scalarized_proxy.py timed out at 600s; this fast script replaces it by caching one-factor derivative tensors and vectorizing C_ab contractions.",
        "explicit_object": "c_ij^epsilon = L_i G_P^perp S_j^epsilon",
        "proxy_realization": {
            "S_j_same": "H^4(zeta^+) represented by source quadrupole family C_{2j} and tensor components C_{2j}",
            "S_j_opp": "H^4(zeta^-) represented by source quadrupole family C_{j2} and tensor components C_{j2}",
            "L_i": "receiver radial curvature-jet proxy represented by second derivative family C_{2k} and tensor components C_{2k}",
            "G_P": "scalar component product resolvent on S^2 x S^2 with denominator 1/(0.5(l1(l1+1)+l2(l2+1))+shift); invariant quotient projection keeps l1+l2 even modes",
            "omitted_from_true_problem": "Bianchi-corrected Ozuch source, scalar/vector/tensor Lichnerowicz block mixing, invariant zero-mode projection, negative shape mode treatment, exact frame transport, and nonlinear normalization",
        },
        "algebra": algebra,
        "second_jet_channel_probe": {
            "meaning": "second-jet/multipole functionals see l>=2 channels; scalar pole values and m=0 selection are insufficient",
            "rows": channel_probe(),
        },
        "representative_matrices": {
            "adjacent_NS_heat002_shift1_L20_ambient": {"coeffs": coeffs_from_T(rep), "stats": stats(rep), "top_entries": top_entries(rep)},
            "diagonal_SS_heat002_shift1_L20_ambient": {"coeffs": coeffs_from_T(rep2), "stats": stats(rep2), "top_entries": top_entries(rep2)},
        },
        "regularized_runs": runs,
        "scientific_reading": {
            "what_changed": "The executable numerator is now a source-to-receiver fourth-derivative spectral sum, not a pointwise angular inner product.  The proxy demonstrates non-diagonal transfer and strong sensitivity to regularization/truncation/frame choices, so the Step84 8/3 local Gram value cannot be promoted to c_opp-c_same.",
            "evidence_against_simplified_handoff": [
                "Off-diagonal entries in representative transfer matrices are substantial.",
                "The second-jet channel probe has nonzero l>=2 contributions, matching A02's pole-second-jet warning.",
                "Heat parameter changes the differentiated sums at fixed truncation; no l<=20 convergence assertion is supported."
            ],
            "next_full_computation": [
                "Derive the Bianchi-compatible distributional source S_j^epsilon from P(chi O^4 + correction), not just H^4 itself.",
                "Build the product Lichnerowicz operator blocks on scalar-derived, vector-derived, TT-derived, trace, and shape sectors of S^2 x S^2.",
                "Separate invariant zero modes and the negative shape mode before applying a pseudo-inverse.",
                "Evaluate heat-regularized sectorwise sums for adjacent and diagonal node pairs and compare same/opposite chirality only after normalization and frame transport are fixed."
            ],
        },
    }
    return result


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result = main()
    OUT.write_text(json.dumps(result, indent=2))
    compact = {
        "output": str(OUT),
        "scope": result["scope"],
        "C_basis_rank": result["algebra"]["C_basis_rank"],
        "second_jet_nonzero_l": [r["l"] for r in result["second_jet_channel_probe"]["rows"] if r["nonzero_second_jet_channel"]],
        "adjacent_rep": result["representative_matrices"]["adjacent_NS_heat002_shift1_L20_ambient"],
        "diagonal_rep": result["representative_matrices"]["diagonal_SS_heat002_shift1_L20_ambient"],
    }
    print(json.dumps(compact, indent=2))
    print(f"Wrote {OUT}")
