#!/usr/bin/env python3
"""
Step 99: modewise support check for Step 98 same-chirality zeros.

The Step98 ladder observed B_{++}=B_{--}=0 for tensor sectors.  This script
looks inside the sum: for each implemented tensor-scalar product mode, it checks
whether the receiver chirality functional and source chirality functional are ever
simultaneously nonzero.  If not, the zero is a selection rule of the implemented
jet functionals rather than cancellation among floating spectral terms.
"""
from __future__ import annotations

import importlib.util
import json
import math
import pathlib
import sys

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

_spec = importlib.util.spec_from_file_location("step98", SCRIPT_DIR / "step98_full_chirality_tensor_maps.py")
step98 = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
sys.modules[_spec.name] = step98
_spec.loader.exec_module(step98)


def parse_pair(pair: str):
    return pair[0], pair[1]


def check_pair_sector(pair: str, sector: str, Lmax: int = 20, tol: float = 1e-14) -> dict:
    recA, recB = "N", "N"
    srcA, srcB = parse_pair(pair)
    if sector == "AA":
        T_rec_node, S_rec_node = recA, recB
        T_src_node, S_src_node = srcA, srcB
    else:
        T_rec_node, S_rec_node = recB, recA
        T_src_node, S_src_node = srcB, srcA

    counts = {key: 0 for key in [
        "Rplus", "Rminus", "Splus", "Sminus",
        "Rplus_Splus", "Rminus_Sminus", "Rplus_Sminus", "Rminus_Splus",
    ]}
    max_products = {key: 0.0 for key in ["++", "--", "+-", "-+"]}
    witnesses = {key: None for key in max_products}

    for lt in range(2, Lmax + 1):
        for ls in range(1, Lmax + 1):
            for tm_r in step98.tensor_value_modes(lt, T_rec_node):
                for sm_r in step98.scalar_hessian_modes(ls, S_rec_node):
                    Hrec = step98.tensor_scalar_hessian(tm_r.value, sm_r.hess, sector)
                    Rplus = step98.step96.receiver_matrix(Hrec, "plus")
                    Rminus = step98.step96.receiver_matrix(Hrec, "minus")
                    rp = float(np.max(np.abs(Rplus)))
                    rm = float(np.max(np.abs(Rminus)))
                    if rp > tol: counts["Rplus"] += 1
                    if rm > tol: counts["Rminus"] += 1
                    for tm_s in step98.tensor_value_modes(lt, T_src_node):
                        if tm_s.kind != tm_r.kind or tm_s.seed != tm_r.seed:
                            continue
                        for sm_s in step98.scalar_hessian_modes(ls, S_src_node):
                            if sm_s.mode != sm_r.mode:
                                continue
                            Hsrc = step98.tensor_scalar_hessian(tm_s.value, sm_s.hess, sector)
                            Splus = step98.step96.source_matrix_over_pi2(Hsrc, "plus")
                            Sminus = step98.step96.source_matrix_over_pi2(Hsrc, "minus")
                            sp = float(np.max(np.abs(Splus)))
                            sm = float(np.max(np.abs(Sminus)))
                            if sp > tol: counts["Splus"] += 1
                            if sm > tol: counts["Sminus"] += 1
                            products = {
                                "++": rp * sp,
                                "--": rm * sm,
                                "+-": rp * sm,
                                "-+": rm * sp,
                            }
                            labels = {
                                "++": "Rplus_Splus",
                                "--": "Rminus_Sminus",
                                "+-": "Rplus_Sminus",
                                "-+": "Rminus_Splus",
                            }
                            for key, val in products.items():
                                if val > tol:
                                    counts[labels[key]] += 1
                                if val > max_products[key]:
                                    max_products[key] = val
                                    witnesses[key] = {
                                        "lt": lt, "ls": ls,
                                        "kind": tm_r.kind, "seed": tm_r.seed,
                                        "scalar_mode": sm_r.mode,
                                        "rp": rp, "rm": rm, "sp": sp, "sm": sm,
                                    }
    return {
        "pair": pair,
        "sector": sector,
        "Lmax": Lmax,
        "counts": counts,
        "max_products": max_products,
        "witnesses": witnesses,
        "interpretation": "Support-level max-products only; nonzero same-chirality products show that any B++/B-- zero must come from signed contraction/cancellation, not from absence of pointwise source/receiver support.",
    }


def main():
    results = {"step": 99, "purpose": "modewise selection check for Step98 tensor same-chirality zeros", "checks": []}
    for pair in ["NS", "SN", "SS"]:
        for sector in ["AA", "BB"]:
            results["checks"].append(check_pair_sector(pair, sector, Lmax=30))
    results["summary"] = {
        f"{c['sector']}_{c['pair']}": c["max_products"] for c in results["checks"]
    }
    results["conclusion"] = [
        "This support-level test multiplies max norms of receiver and source matrices; it does not include signed Green contraction/cancellation.",
        "The large nonzero same-chirality products show that B_{++}=B_{--}=0 is NOT a simple support-selection statement for individual tensor-scalar modes.",
        "Use step99_chirality_cancellation_structure.json for the signed grouped-sum check: in the implemented model the same-chirality total cancels at each (lt,ls) group even though individual polarization terms are nonzero.",
        "The result remains restricted to the implemented source functional and product tensor families; it does not prove the full Ozuch distributional source identity or account for deformation/self terms.",
    ]
    out = DATA_DIR / "step99_modewise_selection_check.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps({"summary": results["summary"], "conclusion": results["conclusion"], "output": str(out)}, indent=2))

if __name__ == "__main__":
    main()
