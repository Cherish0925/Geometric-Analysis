#!/usr/bin/env python3
"""
Step 96: local source--receiver decomposition for the product-orbifold kernel plane.

This corrected version incorporates TTCS Step96: physical Sym^2(K) coefficients
must use the symmetric matrix entries, i.e. the 23 entry is
    (Q_23 + Q_32)/2,
not the ordered Q_23 coefficient alone.  With this correction, the chirality-odd
Ozuch H^4 boundary source equals one half of the sparse odd receiver adjoint on
all physical Sym^2(K) entries (22, 33, 23sym).  The even source and individual
plus/minus sources still contain residual components not represented by the
simple receiver span.

The actual Ozuch H^4 boundary source is
    S^+(zeta,zeta)/pi^2 = -1/16 sum_b C_{zeta,b} tensor C_{zeta,b},
    S^-(zeta,zeta)/pi^2 = -1/16 sum_b C_{b,zeta} tensor C_{b,zeta}.
"""
from __future__ import annotations

import json
import pathlib
import sys

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(SCRIPT_DIR))

import step96_kernel_plane_ab_map as base  # noqa: E402

PAIRS = [(i, j) for i in range(4) for j in range(i, 4)]
ENTRY_NAMES = ["22", "33", "23sym"]


def basis_H(ij, pq):
    i, j = ij; p, q = pq
    H = np.zeros((4, 4, 4, 4), dtype=float)
    for a, b in ([(i, j)] if i == j else [(i, j), (j, i)]):
        for c, d in ([(p, q)] if p == q else [(p, q), (q, p)]):
            H[a, b, c, d] = 1.0
    return H


BASIS = [basis_H(ij, pq) for ij in PAIRS for pq in PAIRS]
BASIS_LABELS = [(ij, pq) for ij in PAIRS for pq in PAIRS]


def mat_entry(M: np.ndarray, name: str) -> float:
    if name == "22":
        return float(M[0, 0])
    if name == "33":
        return float(M[1, 1])
    if name == "23sym":
        return float(0.5 * (M[0, 1] + M[1, 0]))
    raise ValueError(name)


def vec_source(chir: str, name: str) -> np.ndarray:
    return np.array([mat_entry(base.source_matrix_over_pi2(H, chir), name) for H in BASIS], dtype=float)


def vec_receiver(chir: str, name: str) -> np.ndarray:
    return np.array([mat_entry(base.receiver_matrix(H, chir), name) for H in BASIS], dtype=float)


def combo_vectors():
    out = {"source": {}, "receiver": {}}
    for comb in ["plus", "minus", "even", "odd"]:
        out["source"][comb] = {}
        out["receiver"][comb] = {}
    for name in ENTRY_NAMES:
        Sp = vec_source("plus", name)
        Sm = vec_source("minus", name)
        Rp = vec_receiver("plus", name)
        Rm = vec_receiver("minus", name)
        out["source"]["plus"][name] = Sp
        out["source"]["minus"][name] = Sm
        out["source"]["even"][name] = 0.5 * (Sp + Sm)
        out["source"]["odd"][name] = 0.5 * (Sp - Sm)
        out["receiver"]["plus"][name] = Rp
        out["receiver"]["minus"][name] = Rm
        out["receiver"]["even"][name] = 0.5 * (Rp + Rm)
        out["receiver"]["odd"][name] = 0.5 * (Rp - Rm)
    return out


V = combo_vectors()


def solve_span(target: np.ndarray, columns: list[np.ndarray], names: list[str]):
    A = np.vstack(columns).T
    coef, *_ = np.linalg.lstsq(A, target, rcond=None)
    resid = target - A @ coef
    nz = np.where(np.abs(resid) > 1e-10)[0]
    examples = []
    for idx in nz[:8]:
        examples.append({
            "basis": str(BASIS_LABELS[idx]),
            "target": float(target[idx]),
            "fitted": float((A @ coef)[idx]),
            "residual": float(resid[idx]),
        })
    return {
        "coefficients": {names[i]: float(coef[i]) for i in range(len(names)) if abs(coef[i]) > 1e-12},
        "residual_l2_coordinate_basis": float(np.linalg.norm(resid)),
        "target_l2_coordinate_basis": float(np.linalg.norm(target)),
        "residual_relative_coordinate_basis": float(np.linalg.norm(resid) / (np.linalg.norm(target) + 1e-30)),
        "max_abs_residual_on_basis": float(np.max(np.abs(resid))),
        "nonzero_residual_count": int(len(nz)),
        "residual_examples": examples,
        "basis_norm_warning": "L2 numbers use the chosen coordinate Hessian basis; exact zero/nonzero and max coordinate residual are the invariantly meaningful checks here.",
    }


def receiver_columns(which: str):
    cols = []
    names = []
    if which == "same_combo_even":
        combos = ["even"]
    elif which == "same_combo_odd":
        combos = ["odd"]
    elif which == "all_even_odd":
        combos = ["even", "odd"]
    elif which == "all_plus_minus":
        combos = ["plus", "minus"]
    else:
        raise ValueError(which)
    for comb in combos:
        for nm in ENTRY_NAMES:
            cols.append(V["receiver"][comb][nm])
            names.append(f"R{comb}_{nm}")
    return cols, names


def decompose_sources():
    rows = []
    for comb in ["even", "odd", "plus", "minus"]:
        for nm in ENTRY_NAMES:
            target = V["source"][comb][nm]
            row = {"source": f"S{comb}_{nm}"}
            for span in ["same_combo_even", "same_combo_odd", "all_even_odd", "all_plus_minus"]:
                if span == "same_combo_even" and comb != "even":
                    continue
                if span == "same_combo_odd" and comb != "odd":
                    continue
                cols, names = receiver_columns(span)
                row[f"fit_in_{span}"] = solve_span(target, cols, names)
            rows.append(row)
    return rows


def odd_identity_by_entry():
    rows = []
    max_err = 0.0
    for nm in ENTRY_NAMES:
        target = V["source"]["odd"][nm]
        rhs = 0.5 * V["receiver"]["odd"][nm]
        resid = target - rhs
        err = float(np.max(np.abs(resid)))
        max_err = max(max_err, err)
        nz = np.where(np.abs(resid) > 1e-10)[0]
        rows.append({
            "entry": nm,
            "identity": f"Sodd_{nm} = (1/2) Rodd_{nm}",
            "max_abs_residual_on_basis": err,
            "residual_l2_coordinate_basis": float(np.linalg.norm(resid)),
            "nonzero_residual_count": int(len(nz)),
        })
    return {"entries": rows, "max_abs_residual_all_entries": max_err}


def ordered_offdiag_artifact():
    # Reproduce the previous erroneous ordered comparison to make the correction transparent.
    ordered_rows = []
    for ordered in [(0, 1), (1, 0)]:
        vals = []
        for H in BASIS:
            Sodd = 0.5 * (base.source_matrix_over_pi2(H, "plus")[ordered] - base.source_matrix_over_pi2(H, "minus")[ordered])
            Rodd = 0.5 * (base.receiver_matrix(H, "plus")[ordered] - base.receiver_matrix(H, "minus")[ordered])
            vals.append(Sodd - 0.5 * Rodd)
        vals = np.array(vals)
        ordered_rows.append({
            "ordered_entry": f"{ordered[0]+2}{ordered[1]+2}",
            "max_abs_ordered_residual": float(np.max(np.abs(vals))),
            "residual_l2_coordinate_basis": float(np.linalg.norm(vals)),
        })
    sym_vals = []
    for H in BASIS:
        Sp = base.source_matrix_over_pi2(H, "plus")
        Sm = base.source_matrix_over_pi2(H, "minus")
        Rp = base.receiver_matrix(H, "plus")
        Rm = base.receiver_matrix(H, "minus")
        Sodd_sym = 0.5 * (0.5*(Sp[0,1]+Sp[1,0]) - 0.5*(Sm[0,1]+Sm[1,0]))
        Rodd_sym = 0.5 * (0.5*(Rp[0,1]+Rp[1,0]) - 0.5*(Rm[0,1]+Rm[1,0]))
        sym_vals.append(Sodd_sym - 0.5 * Rodd_sym)
    sym_vals = np.array(sym_vals)
    return {
        "previous_error": "Step96 first run compared ordered 23 but physical Sym^2(K) uses (23+32)/2.",
        "ordered_residuals": ordered_rows,
        "symmetrized_23_residual_max": float(np.max(np.abs(sym_vals))),
        "symmetrized_23_residual_l2": float(np.linalg.norm(sym_vals)),
    }


def best_single_receiver_identities():
    identities = []
    for comb in ["even", "odd"]:
        for sname in ENTRY_NAMES:
            target = V["source"][comb][sname]
            best = None
            for rcomb in ["even", "odd"]:
                for rname in ENTRY_NAMES:
                    R = V["receiver"][rcomb][rname]
                    denom = float(np.dot(R, R))
                    if denom < 1e-14:
                        continue
                    coef = float(np.dot(target, R) / denom)
                    resid = target - coef * R
                    item = {
                        "source": f"S{comb}_{sname}",
                        "receiver": f"R{rcomb}_{rname}",
                        "coef": coef,
                        "max_abs_residual_on_basis": float(np.max(np.abs(resid))),
                        "residual_l2_coordinate_basis": float(np.linalg.norm(resid)),
                    }
                    if best is None or item["residual_l2_coordinate_basis"] < best["residual_l2_coordinate_basis"]:
                        best = item
            identities.append(best)
    return identities


def main():
    results = {
        "step": 96,
        "scope": "corrected local decomposition of Ozuch H4 source against kernel-plane receivers",
        "basis": "100-dimensional coordinate basis of symmetric Hessians H_ij,pq at a node; V2=(1/2)H x x",
        "kernel_plane_entries": ENTRY_NAMES,
        "symmetrization_correction": ordered_offdiag_artifact(),
        "odd_identity_physical_Sym2K": odd_identity_by_entry(),
        "decomposition": decompose_sources(),
        "best_single_receiver_identities": best_single_receiver_identities(),
        "interpretation": [
            "After physical 23/32 symmetrization, the chirality-odd H4 source equals one half of the odd receiver adjoint on all Sym^2(K) entries.",
            "This does not restore the Step95 scalar obstruction model: the even H4 source and individual plus/minus sources still contain residual components outside the simple receiver span.",
            "Gauge invariance of R_odd(L_X g0) removes smooth pure-gauge ambiguity in odd receiver values, but it does not eliminate the even-source residuals or prove the full projected global Green block.",
            "A source-compatible reduced map must propagate the full H4 source. The AB-sector map in step96_kernel_plane_ab_map.py is one restricted propagated sample; AA/BB, self terms, frame/projector motion, global kernel/deformation variables, and sharper remainders remain open.",
        ],
    }
    out = DATA_DIR / "step96_source_receiver_decomposition.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
