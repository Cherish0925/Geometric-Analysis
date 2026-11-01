#!/usr/bin/env python3
"""
Step 96: source-compatible kernel-plane AB-sector map for the product-orbifold
Eguchi--Hanson desingularization problem.

Purpose
-------
After the Step 95 correction, the object to compute is not a scalar "K_adj" but a
map
    source Sym^2(K_source)  -->  receiver Sym^2(K_receiver)
for each ordered node pair and chirality pair.  This script reconstructs the
actual Ozuch H^4 boundary source at the algebraic level
    H^4(zeta^+) = -1/2 sum_b (C_{zeta,b})_{ij}(C_{zeta,b})_{pq} x_p x_q,
with the RP^3 boundary factor included, and propagates it through the product
AB one-form spectral sector.

It deliberately keeps same-chirality, opposite-chirality, even and odd maps
separate.  The old scalar K_adj is recovered only as the odd/odd e2->e2
diagonal component, a check against Step 91.  The output is therefore a finite
piece of the reduced map, not a mixed-row obstruction theorem.
"""
from __future__ import annotations

import json
import math
import pathlib
from dataclasses import dataclass
from typing import Literal

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

Node = Literal["N", "S"]
Kind = Literal["exact", "coexact"]
Chir = Literal["plus", "minus"]

KIDX = [1, 2]  # 0-based indices corresponding to Ozuch e2,e3 kernel plane
J2 = np.array([[0.0, -1.0], [1.0, 0.0]])


def wedge(i: int, j: int, n: int = 4) -> np.ndarray:
    A = np.zeros((n, n), dtype=float)
    A[i, j] = 1.0
    A[j, i] = -1.0
    return A


def build_forms_and_C():
    e01 = wedge(0, 1); e02 = wedge(0, 2); e03 = wedge(0, 3)
    e12 = wedge(1, 2); e13 = wedge(1, 3); e23 = wedge(2, 3)
    rt2 = math.sqrt(2.0)
    wp = [(e01 + e23)/rt2, (e02 - e13)/rt2, (e03 + e12)/rt2]
    wm = [(e01 - e23)/rt2, (e02 + e13)/rt2, (e03 - e12)/rt2]
    # raw unnormalized forms, useful for curvature block normalization
    wp_raw = [e01 + e23, e02 - e13, e03 + e12]
    wm_raw = [e01 - e23, e02 + e13, e03 - e12]
    C = np.zeros((3, 3, 4, 4), dtype=float)
    for a in range(3):
        for b in range(3):
            prod = wp[a] @ wm[b]
            C[a, b] = prod + prod.T
    C_round = np.rint(C)
    if np.max(np.abs(C - C_round)) > 1e-12:
        raise RuntimeError("C_ab matrices are not integral in this convention")
    return wp_raw, wm_raw, C_round.astype(float)


WP_RAW, WM_RAW, C = build_forms_and_C()


def curvature_block_coeff(rawA: np.ndarray, rawB: np.ndarray) -> np.ndarray:
    """Coefficient tensor L with R_block(H)=sum L_ijpq H_ijpq.

    block_entry uses normalized 2-forms omega/sqrt(2):
        <rawA/sqrt2, R(rawB/sqrt2)> = (rawA R rawB)/8.
    R_abcd(H)=1/2(H_ad,bc+H_bc,ad-H_ac,bd-H_bd,ac).
    """
    L = np.zeros((4, 4, 4, 4), dtype=float)
    for a in range(4):
        for b in range(4):
            ca = rawA[a, b]
            if ca == 0:
                continue
            for c in range(4):
                for d in range(4):
                    cb = rawB[c, d]
                    if cb == 0:
                        continue
                    fac = ca * cb / 16.0  # 1/8 block normalization times 1/2 Riemann variation
                    L[a, d, b, c] += fac
                    L[b, c, a, d] += fac
                    L[a, c, b, d] -= fac
                    L[b, d, a, c] -= fac
    return L


# Receiver curvature block coefficient tensors restricted to the kernel plane.
RCOEFF = {"plus": np.zeros((2, 2, 4, 4, 4, 4)), "minus": np.zeros((2, 2, 4, 4, 4, 4))}
for ia, a in enumerate(KIDX):
    for ib, b in enumerate(KIDX):
        RCOEFF["plus"][ia, ib] = curvature_block_coeff(WP_RAW[a], WP_RAW[b])
        RCOEFF["minus"][ia, ib] = curvature_block_coeff(WM_RAW[a], WM_RAW[b])


# Ozuch H^4 boundary source coefficient tensors.  These return B(H)/pi^2, where
# B=3 int_RP3 <H^4(zeta), V2> and V2=(1/2)H_ijpq x_p x_q.  For plus chirality:
#   B_+(zeta)/pi^2 = -1/16 sum_b (C_{zeta,b})_ij (C_{zeta,b})_pq H_ijpq.
# For minus chirality plus/minus roles are swapped:
#   B_-(zeta)/pi^2 = -1/16 sum_b (C_{b,zeta})_ij (C_{b,zeta})_pq H_ijpq.
SCOEFF = {"plus": np.zeros((2, 2, 4, 4, 4, 4)), "minus": np.zeros((2, 2, 4, 4, 4, 4))}
for ia, a in enumerate(KIDX):
    for ic, c in enumerate(KIDX):
        Tplus = np.zeros((4, 4, 4, 4), dtype=float)
        Tminus = np.zeros((4, 4, 4, 4), dtype=float)
        for b in range(3):
            Tplus += np.einsum("ij,pq->ijpq", C[a, b], C[c, b])
            Tminus += np.einsum("ij,pq->ijpq", C[b, a], C[b, c])
        SCOEFF["plus"][ia, ic] = -Tplus / 16.0
        SCOEFF["minus"][ia, ic] = -Tminus / 16.0


@dataclass(frozen=True)
class OneFormJet:
    ell: int
    mode: str
    kind: Kind
    node: Node
    deriv: np.ndarray
    mu: float


def scalar_hessian_coefficients(ell: int, node: Node):
    lam = ell * (ell + 1)
    out: list[tuple[str, np.ndarray]] = []
    C0 = math.sqrt((2 * ell + 1) / (4 * math.pi))
    H0_N = -(C0 * lam / 2.0) * np.eye(2)
    sign0 = 1.0 if node == "N" else ((-1.0) ** ell)
    out.append(("m0", sign0 * H0_N))

    if ell >= 2:
        log_ratio = math.lgamma(ell + 3) - math.lgamma(ell - 1)
        A2 = math.exp(log_ratio) / 8.0
        Nl2 = math.sqrt((2 * ell + 1) / (4 * math.pi) * math.exp(math.lgamma(ell - 1) - math.lgamma(ell + 3)))
        b = math.sqrt(2.0) * Nl2 * A2
        Hc_N = np.array([[2 * b, 0.0], [0.0, -2 * b]])
        Hs_N = np.array([[0.0, 2 * b], [2 * b, 0.0]])
        sign_c = 1.0 if node == "N" else ((-1.0) ** ell)
        # South oriented frame is (X,-Y), so sin(2phi) changes by an extra minus.
        sign_s = 1.0 if node == "N" else (-((-1.0) ** ell))
        out.append(("c2", sign_c * Hc_N))
        out.append(("s2", sign_s * Hs_N))
    return out


def oneform_jets(ell: int, node: Node) -> list[OneFormJet]:
    m = ell * (ell + 1)
    jets: list[OneFormJet] = []
    for mode, H in scalar_hessian_coefficients(ell, node):
        jets.append(OneFormJet(ell, mode, "exact", node, H.copy(), float(m)))
        jets.append(OneFormJet(ell, mode, "coexact", node, J2 @ H, float(m)))
    return jets


def ab_hessian(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Hessian H=d_p d_q h_ij for h=alpha_A sym beta_B.

    A[a,p]=d_p alpha_a in factor A local coordinates; B[mu,q]=d_q beta_mu in
    factor B.  Global coordinates are A=(0,1), B=(2,3).
    """
    H = np.zeros((4, 4, 4, 4), dtype=float)
    for a in range(2):
        for mu in range(2):
            i = a
            j = 2 + mu
            for p in range(2):
                for q in range(2):
                    val = A[a, p] * B[mu, q]
                    if val == 0.0:
                        continue
                    H[i, j, p, 2 + q] += val
                    H[j, i, p, 2 + q] += val
                    H[i, j, 2 + q, p] += val
                    H[j, i, 2 + q, p] += val
    return H


def receiver_matrix(H: np.ndarray, chir: Chir) -> np.ndarray:
    return np.einsum("abijpq,ijpq->ab", RCOEFF[chir], H)


def source_matrix_over_pi2(H: np.ndarray, chir: Chir) -> np.ndarray:
    return np.einsum("acijpq,ijpq->ac", SCOEFF[chir], H)


def mu(ell: int) -> int:
    return ell * (ell + 1)


def compute_ab_map(Lmax: int, tau: float, src_pair: str) -> dict:
    # receiver fixed at NN; source pair is NN, NS, SN, or SS.
    recA, recB = "N", "N"
    if src_pair == "NN":
        srcA, srcB = "N", "N"
    elif src_pair == "NS":
        srcA, srcB = "N", "S"
    elif src_pair == "SN":
        srcA, srcB = "S", "N"
    elif src_pair == "SS":
        srcA, srcB = "S", "S"
    else:
        raise ValueError(src_pair)

    jets = {(ell, node): oneform_jets(ell, node) for ell in range(1, Lmax + 1) for node in ["N", "S"]}
    # response[receiver chir][source chir][receiver a,b][source c,d]
    response = {rc: {sc: np.zeros((2, 2, 2, 2), dtype=float) for sc in ["plus", "minus"]} for rc in ["plus", "minus"]}

    shell_norms = []
    axial_check = 0.0
    for ellA in range(1, Lmax + 1):
        shell_abs = 0.0
        for ellB in range(1, Lmax + 1):
            P = 0.5 * (mu(ellA) + mu(ellB)) - 1.0
            heat = math.exp(-tau * P)
            norm_quot = mu(ellA) * mu(ellB)
            pref = heat / (P * norm_quot)
            for ja_r in jets[(ellA, recA)]:
                for jb_r in jets[(ellB, recB)]:
                    Hrec_zero = False
                    Rmats = None
                    for ja_s in jets[(ellA, srcA)]:
                        if ja_s.mode != ja_r.mode or ja_s.kind != ja_r.kind:
                            continue
                        for jb_s in jets[(ellB, srcB)]:
                            if jb_s.mode != jb_r.mode or jb_s.kind != jb_r.kind:
                                continue
                            if Rmats is None:
                                Hrec = ab_hessian(ja_r.deriv, jb_r.deriv)
                                Rmats = {rc: receiver_matrix(Hrec, rc) for rc in ["plus", "minus"]}
                                if max(np.max(np.abs(Rmats["plus"])), np.max(np.abs(Rmats["minus"]))) < 1e-15:
                                    Hrec_zero = True
                            if Hrec_zero:
                                continue
                            Hsrc = ab_hessian(ja_s.deriv, jb_s.deriv)
                            Smats = {sc: source_matrix_over_pi2(Hsrc, sc) for sc in ["plus", "minus"]}
                            if max(np.max(np.abs(Smats["plus"])), np.max(np.abs(Smats["minus"]))) < 1e-15:
                                continue
                            for rc in ["plus", "minus"]:
                                for sc in ["plus", "minus"]:
                                    term = (math.pi ** 2) * pref * np.einsum("ab,cd->abcd", Rmats[rc], Smats[sc])
                                    response[rc][sc] += term
                                    shell_abs += float(np.sum(np.abs(term)))
                            # Reproduce the old Step91 odd/odd diagonal axial contribution.
                            if (ellA == 1 and ellB == 1 and ja_r.mode == "m0" and jb_r.mode == "m0"
                                    and ja_r.kind == "coexact" and jb_r.kind == "coexact"):
                                Rodd_rec = 0.5 * (Rmats["plus"][0, 0] - Rmats["minus"][0, 0])
                                Sodd_src = 0.5 * math.pi ** 2 * (Smats["plus"][0, 0] - Smats["minus"][0, 0])
                                axial_check += pref * Rodd_rec * Sodd_src
        shell_norms.append(shell_abs)

    # Derived even/odd combinations, using receiver and source half-sums/differences.
    Kpp = response["plus"]["plus"]
    Kpm = response["plus"]["minus"]
    Kmp = response["minus"]["plus"]
    Kmm = response["minus"]["minus"]
    combos = {
        "even_even": 0.25 * (Kpp + Kpm + Kmp + Kmm),
        "even_odd": 0.25 * (Kpp - Kpm + Kmp - Kmm),
        "odd_even": 0.25 * (Kpp + Kpm - Kmp - Kmm),
        "odd_odd": 0.25 * (Kpp - Kpm - Kmp + Kmm),
    }

    def arr(A):
        return np.asarray(A).round(12).tolist()

    # A compact 3x3 representation: receiver basis [22,33,23sym] versus source matrix entries [22,33,23].
    # A source direction z=(x,y) uses entries M22*x^2 + 2*M23*x*y + M33*y^2; the 23 column below is the matrix
    # off-diagonal coefficient K[...,0,1]=K[...,1,0], so multiply by 2xy when evaluating.
    def compact(T: np.ndarray) -> np.ndarray:
        return np.array([
            [T[0, 0, 0, 0], T[0, 0, 1, 1], T[0, 0, 0, 1]],
            [T[1, 1, 0, 0], T[1, 1, 1, 1], T[1, 1, 0, 1]],
            [T[0, 1, 0, 0], T[0, 1, 1, 1], T[0, 1, 0, 1]],
        ])

    compact_maps = {name: arr(compact(T)) for name, T in combos.items()}
    raw_maps = {rc + "_recv__" + sc + "_src": arr(response[rc][sc]) for rc in ["plus", "minus"] for sc in ["plus", "minus"]}

    odd_diag = combos["odd_odd"][0, 0, 0, 0]
    even_diag = combos["even_even"][0, 0, 0, 0]
    odd_off_source_e3_to_recv_e2 = combos["odd_odd"][0, 0, 1, 1]
    odd_cross = combos["odd_odd"][0, 1, 0, 1]

    return {
        "receiver": "NN",
        "source": src_pair,
        "Lmax": Lmax,
        "tau": tau,
        "raw_chirality_maps_shape": "[receiver chirality][source chirality][receiver 2x2 block][source Sym^2 2x2 matrix]",
        "raw_chirality_maps": raw_maps,
        "combo_compact_maps_basis": {
            "receiver_rows": ["R22", "R33", "R23"],
            "source_cols": ["zeta2^2", "zeta3^2", "zeta2*zeta3 matrix-entry (evaluate with 2 zeta2 zeta3)"],
            "maps": compact_maps,
        },
        "old_scalar_checks": {
            "odd_odd_R22_source22": odd_diag,
            "even_even_R22_source22": even_diag,
            "odd_odd_R22_source33": odd_off_source_e3_to_recv_e2,
            "odd_odd_R23_source23": odd_cross,
            "axial_l1_odd_odd_R22_source22": axial_check,
            "expected_step91_AB_adjacent": -0.03144249732 if src_pair in ["NS", "SN"] else None,
            "expected_axial_adjacent_limit": -9.0/128.0 if src_pair in ["NS", "SN"] else None,
        },
        "tail_indicator_last_10_ellA_abs_sum": float(sum(shell_norms[-10:])) if len(shell_norms) >= 10 else None,
        "interpretation_warning": "AB one-form sector only, heat regularized. This is the actual H^4 quadratic boundary source in this sector, but not the full Ozuch reduced map: AA/BB, self terms, global kernel/deformation variables, frame/projector motion, and sharper remainders are not included.",
    }


def local_source_receiver_algebra_summary() -> dict:
    """Check the exact H^4 quadratic source against physical Sym^2(K) receiver blocks."""
    pairs = [(i, j) for i in range(4) for j in range(i, 4)]
    entry_names = ["22", "33", "23sym"]

    def basis_H(ij, pq):
        i, j = ij; p, q = pq
        H = np.zeros((4, 4, 4, 4), dtype=float)
        for a, b in ([(i, j)] if i == j else [(i, j), (j, i)]):
            for c, d in ([(p, q)] if p == q else [(p, q), (q, p)]):
                H[a, b, c, d] = 1.0
        return H

    def mat_entry(M, name):
        if name == "22":
            return M[0, 0]
        if name == "33":
            return M[1, 1]
        if name == "23sym":
            return 0.5 * (M[0, 1] + M[1, 0])
        raise ValueError(name)

    # Physical Sym^2(K) identity: the off-diagonal coefficient is symmetrized.
    identity_by_entry = {}
    max_err = 0.0
    for name in entry_names:
        vals = []
        for ij in pairs:
            for pq in pairs:
                H = basis_H(ij, pq)
                Sodd = 0.5 * (mat_entry(source_matrix_over_pi2(H, "plus"), name) - mat_entry(source_matrix_over_pi2(H, "minus"), name))
                Rodd = 0.5 * (mat_entry(receiver_matrix(H, "plus"), name) - mat_entry(receiver_matrix(H, "minus"), name))
                vals.append(Sodd - 0.5 * Rodd)
        vals = np.array(vals)
        identity_by_entry[name] = {
            "max_abs_residual_on_basis": float(np.max(np.abs(vals))),
            "residual_l2_coordinate_basis": float(np.linalg.norm(vals)),
        }
        max_err = max(max_err, float(np.max(np.abs(vals))))

    # Ordered 23/32 comparison from the first run is recorded as a warning: it is not the physical coefficient.
    ordered_artifact = []
    for ordered in [(0, 1), (1, 0)]:
        vals = []
        for ij in pairs:
            for pq in pairs:
                H = basis_H(ij, pq)
                Sodd = 0.5 * (source_matrix_over_pi2(H, "plus")[ordered] - source_matrix_over_pi2(H, "minus")[ordered])
                Rodd = 0.5 * (receiver_matrix(H, "plus")[ordered] - receiver_matrix(H, "minus")[ordered])
                vals.append(Sodd - 0.5 * Rodd)
        vals = np.array(vals)
        ordered_artifact.append({"ordered_entry": f"{ordered[0]+2}{ordered[1]+2}", "max_abs_ordered_residual": float(np.max(np.abs(vals)))})

    # Check whether individual plus/minus sources equal simple receiver blocks; record residual norms.
    rows = []
    for chir in ["plus", "minus"]:
        for name in entry_names:
            svec = []
            rpvec = []
            rmvec = []
            for ij in pairs:
                for pq in pairs:
                    H = basis_H(ij, pq)
                    svec.append(mat_entry(source_matrix_over_pi2(H, chir), name))
                    rpvec.append(mat_entry(receiver_matrix(H, "plus"), name))
                    rmvec.append(mat_entry(receiver_matrix(H, "minus"), name))
            svec = np.array(svec); rpvec = np.array(rpvec); rmvec = np.array(rmvec)
            A = np.vstack([rpvec, rmvec]).T
            coef, *_ = np.linalg.lstsq(A, svec, rcond=None)
            resid = svec - A @ coef
            rows.append({
                "source_chirality": chir,
                "kernel_entry": name,
                "least_squares_against_same_entries_[Rplus,Rminus]": coef.round(12).tolist(),
                "residual_l2_coordinate_basis": float(np.linalg.norm(resid)),
                "source_l2_coordinate_basis": float(np.linalg.norm(svec)),
                "residual_relative_coordinate_basis": float(np.linalg.norm(resid) / (np.linalg.norm(svec) + 1e-30)),
                "max_abs_residual_on_basis": float(np.max(np.abs(resid))),
            })
    return {
          "H4_source_formula": "B_+(zeta)/pi^2=-1/16 sum_b <C_{zeta,b} tensor C_{zeta,b}, H>; B_-(zeta)/pi^2=-1/16 sum_b <C_{b,zeta} tensor C_{b,zeta}, H>",
          "odd_identity_physical_Sym2K": {
              "statement": "After 23/32 symmetrization, (B_+ - B_-)/(2*pi^2) = (1/2)*(R^+ - R^-)/2 on all physical Sym^2(K) entries.",
              "identity_by_entry": identity_by_entry,
              "max_abs_residual_all_entries": max_err,
          },
          "ordered_23_artifact_from_first_run": ordered_artifact,
          "individual_source_not_identical_to_simple_receiver_block": rows,
          "meaning": "The physical odd half-difference of the H4 source is one half of the odd receiver adjoint on Sym^2(K). Individual chiral and even sources still have additional components; the gauge lemma alone does not identify the complete source with the sparse receiver adjoint.",
    }


def main():
    # Moderate ladders; Step91 already computed the high-precision scalar AB value.  Here the new object is the map.
    ladders = []
    for tau, L in [(0.10, 80), (0.05, 120), (0.02, 180), (0.01, 260)]:
        ladders.append(compute_ab_map(L, tau, "NS"))

    pair_compare = [compute_ab_map(180, 0.02, p) for p in ["NS", "SN", "SS"]]

    results = {
        "step": 96,
        "scope": "kernel-plane source-compatible AB-sector response map after Step95 correction",
        "local_algebra": local_source_receiver_algebra_summary(),
        "adjacent_NS_ladder": ladders,
        "pair_compare_tau_0p02_L180": pair_compare,
        "main_lessons": [
            "The actual H^4 boundary source is quadratic in the insertion direction zeta; the finite-dimensional response is a map Sym^2(K_source)->Sym^2(K_receiver), not a scalar bilinear form in zeta.",
            "After physical 23/32 symmetrization the odd half-difference H^4 source satisfies the exact Step89-type adjoint identity on all Sym^2(K) entries: S_odd=(1/2)R_odd for 22, 33, and 23sym. Ordered 23 or 32 failures are coordinate artifacts.",
            "The old K_adj^AB is recovered as the trace/radial entry of a rank-one AB-sector map. In trace/double-angle variables it is blind to angular anisotropy: M maps to a multiple of tr(M) times the identity block, with no R23 output.",
            "Physical sources are constrained rank-one positive semidefinite matrices M=t_j^2 u_j u_j^T, so tr(M)>0 for every nonzero insertion and the traceless kernel of the AB rank-one map contains no physical bubble source.",
            "Same-chirality and opposite-chirality maps are retained separately; no all-compatible KE calibration or pairwise deletion is imposed in this computation.",
        ],
    }
    out = DATA_DIR / "step96_kernel_plane_ab_map.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
