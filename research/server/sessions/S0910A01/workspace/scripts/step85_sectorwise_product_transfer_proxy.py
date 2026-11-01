#!/usr/bin/env python3
"""
Step 85: sectorwise product-operator Green-transfer proxy.

This is a stronger executable bridge than the scalarized shift model.  It still
is not Ozuch's coefficient c_opp-c_same, because the Bianchi-corrected source,
exact receiver functional, full gauge slice and nonlinear layer are not derived.
But it inserts the actual product P=1/2∇*∇-R° denominators for the elementary
product sectors of S^2 x S^2:
  * AA/BB symmetric-tensor sectors: P eigenvalue = 0.5*(λ_A+λ_B)-1
    for trace and trace-free tensor sectors (after valid one-factor restrictions);
  * AB one-form x one-form sector: P eigenvalue = 0.5*(λ_A+λ_B-2), valid lA,lB>=1.
Zero modes are skipped as pseudo-inverse kernel; negative constant trace modes
are retained, matching the full invariant operator warning.
"""
from __future__ import annotations

import importlib.util
import json
import math
from pathlib import Path

import numpy as np

OUT = Path("Sessions/S0910A01/workspace/data/step85_sectorwise_product_transfer_proxy.json")
MODPATH = "Sessions/S0910A01/workspace/scripts/step85_green_transfer_scalarized_proxy_fast.py"
spec = importlib.util.spec_from_file_location("s85fast", MODPATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore

MATS = mod.MATS
LABELS = mod.LABELS
RECEIVER_IDX = mod.RECEIVER_IDX
SAME_SRC_IDX = mod.SAME_SRC_IDX
OPP_SRC_IDX = mod.OPP_SRC_IDX


def proj_diag(M):
    P = np.zeros_like(M)
    P[:2, :2] = M[:2, :2]
    P[2:, 2:] = M[2:, 2:]
    return P


def proj_ab(M):
    P = np.zeros_like(M)
    P[:2, 2:] = M[:2, 2:]
    P[2:, :2] = M[2:, :2]
    return P

W_DIAG = np.array([[float(np.sum(proj_diag(MATS[i]) * proj_diag(MATS[j]))) for j in range(9)] for i in range(9)])
W_AB = np.array([[float(np.sum(proj_ab(MATS[i]) * proj_ab(MATS[j]))) for j in range(9)] for i in range(9)])
W_TOTAL = W_DIAG + W_AB


def transfer_sectorwise(Lmax: int, relation: str, heat_tau: float, frame: str,
                        quotient_lift_factor: float = 1.0) -> tuple[np.ndarray, dict]:
    T = np.zeros((9, 9), dtype=float)
    skipped_zero = []
    negative_terms = []
    for l1 in range(Lmax + 1):
        lam1 = l1 * (l1 + 1)
        for l2 in range(Lmax + 1):
            lam2 = l2 * (l2 + 1)
            heat = math.exp(-heat_tau * (lam1 + lam2))
            base = quotient_lift_factor * (2 * l1 + 1) * (2 * l2 + 1) / (16.0 * math.pi ** 2) * heat
            D = mod.derivative_matrix(l1, l2, relation, frame)

            denom_diag = 0.5 * (lam1 + lam2) - 1.0
            if abs(denom_diag) < 1e-12:
                skipped_zero.append({"sector": "AA/BB", "l1": l1, "l2": l2})
            else:
                if denom_diag < 0:
                    negative_terms.append({"sector": "AA/BB", "l1": l1, "l2": l2, "denom": denom_diag})
                T += base * D * (W_DIAG / denom_diag)

            if l1 >= 1 and l2 >= 1:
                denom_ab = 0.5 * (lam1 + lam2 - 2.0)
                if abs(denom_ab) < 1e-12:
                    skipped_zero.append({"sector": "AB", "l1": l1, "l2": l2})
                else:
                    T += base * D * (W_AB / denom_ab)
    ledger = {"skipped_zero_modes": skipped_zero, "negative_denominator_modes": negative_terms}
    return T, ledger


def coeffs(T):
    cs = float(T[np.ix_(RECEIVER_IDX, SAME_SRC_IDX)].sum())
    co = float(T[np.ix_(RECEIVER_IDX, OPP_SRC_IDX)].sum())
    return cs, co, co - cs


def stats(T): return mod.stats(T)


def top_entries(T, n=20):
    out = []
    for i in range(9):
        for j in range(9):
            v = float(T[i, j])
            if abs(v) > 1e-8:
                out.append({"receiver": LABELS[i], "source": LABELS[j], "value": v})
    return sorted(out, key=lambda x: -abs(x["value"]))[:n]


def main():
    runs = []
    heats = [0.08, 0.04, 0.02, 0.01, 0.005, 0.0025]
    Ls = [20, 40, 80, 120]
    first_ledger = None
    for relation in ["adjacent_NS", "diagonal_SS"]:
        for frame in ["ambient", "antipodal_derivative"]:
            for heat in heats:
                seq = []
                for L in Ls:
                    T, ledger = transfer_sectorwise(L, relation, heat, frame)
                    if first_ledger is None:
                        first_ledger = ledger
                    cs, co, diff = coeffs(T)
                    seq.append({"Lmax": L, "c_same_proxy": cs, "c_opp_proxy": co, "diff_opp_minus_same_proxy": diff, "matrix_stats": stats(T)})
                runs.append({"relation": relation, "frame_transport_model": frame, "heat_tau": heat, "Lmax_sequence": seq})

    rep, rep_ledger = transfer_sectorwise(120, "adjacent_NS", 0.01, "ambient")
    repd, _ = transfer_sectorwise(120, "diagonal_SS", 0.01, "ambient")
    trend = []
    for r in runs:
        last = r["Lmax_sequence"][-1]
        trend.append({"relation": r["relation"], "frame": r["frame_transport_model"], "heat_tau": r["heat_tau"], "Lmax": last["Lmax"], "c_same": last["c_same_proxy"], "c_opp": last["c_opp_proxy"], "diff": last["diff_opp_minus_same_proxy"]})

    result = {
        "scope": "sectorwise product P denominator proxy; not Ozuch full coefficient",
        "sector_weights": {
            "W_diag_matrix": W_DIAG.tolist(),
            "W_AB_matrix": W_AB.tolist(),
            "W_total_equals_C_gram_maxerr": float(np.max(np.abs(W_TOTAL - np.einsum('iab,jab->ij', MATS, MATS)))),
            "pure_sector_classification": {LABELS[i]: ("AB" if np.linalg.norm(proj_ab(MATS[i])) > 1e-12 and np.linalg.norm(proj_diag(MATS[i])) < 1e-12 else "AA/BB" if np.linalg.norm(proj_diag(MATS[i])) > 1e-12 and np.linalg.norm(proj_ab(MATS[i])) < 1e-12 else "mixed") for i in range(9)},
        },
        "denominator_model": {
            "AA_BB": "0.5*(l1(l1+1)+l2(l2+1))-1; zero modes (1,0),(0,1) skipped; (0,0) negative retained",
            "AB": "0.5*(l1(l1+1)+l2(l2+1)-2), l1,l2>=1",
            "source_receiver_derivative": "same quadrupole/second-jet derivative tensor as scalar proxy; only component propagation denominators changed",
        },
        "mode_ledger_example": rep_ledger,
        "representative": {
            "adjacent_NS_heat001_L120_ambient": {"coeffs": coeffs(rep), "stats": stats(rep), "top_entries": top_entries(rep)},
            "diagonal_SS_heat001_L120_ambient": {"coeffs": coeffs(repd), "stats": stats(repd), "top_entries": top_entries(repd)},
        },
        "runs": runs,
        "trend_L120": trend,
        "scientific_interpretation": {
            "established_by_this_proxy": [
                "The full product operator already separates C_ab components into AA/BB and AB sectors with different denominators; scalar-pole and common-shift recipes suppress this information.",
                "The four scalar kernel modes appear exactly as AA/BB trace l=1 with one factor constant and are removed by pseudo-inverse skipping; the negative constant trace modes are retained.",
                "The mixed one-form AB l1=l2=1 denominator is 1, matching the corrected spectral gap for the product mixed sector.",
                "The tested sectorwise proxy still gives a nonzero same/opposite difference, but the values remain regularization- and frame-sensitive, especially for adjacent pairs."
            ],
            "not_established": [
                "The Bianchi-corrected source S_j^epsilon may have scalar/vector-derived content not equal to the raw H^4 sector decomposition.",
                "The true receiver L_i is a curvature-jet/radial functional, not merely the same second-jet tensor family used here.",
                "Inter-sector coupling through gauge fixing, kernel projection, and local singular subtraction is not represented."
            ],
        }
    }
    return result

if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result = main()
    OUT.write_text(json.dumps(result, indent=2))
    print(json.dumps({"output": str(OUT), "scope": result["scope"], "representative": result["representative"], "trend_L120": result["trend_L120"]}, indent=2))
    print(f"Wrote {OUT}")
