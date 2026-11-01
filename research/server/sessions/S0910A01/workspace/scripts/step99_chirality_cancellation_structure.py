#!/usr/bin/env python3
"""
Step 99: locate the cancellation producing Step98 same-chirality zeros.

A misleading first support test showed that same-chirality receiver/source factors are
individually nonzero in the implemented tensor-scalar family.  This script sums the
actual signed Green terms in increasingly fine groups to determine whether B_{++}=0
is modewise, polarization-wise, or only after a larger electric/magnetic and scalar
polarization cancellation.
"""
from __future__ import annotations

import importlib.util
import json
import math
import pathlib
import sys
from collections import defaultdict

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


def frob(A):
    return float(np.linalg.norm(A.reshape(-1)))


def compute_grouped(sector: str, pair: str, Lmax: int = 12, tau: float = 0.08) -> dict:
    recA, recB = "N", "N"
    srcA, srcB = parse_pair(pair)
    if sector == "AA":
        T_rec_node, S_rec_node = recA, recB
        T_src_node, S_src_node = srcA, srcB
    else:
        T_rec_node, S_rec_node = recB, recA
        T_src_node, S_src_node = srcB, srcA

    raw = {ck: np.zeros((2,2,2,2), dtype=float) for ck in ["++", "+-", "-+", "--"]}
    groups = {
        "by_lt_ls": defaultdict(lambda: {ck: np.zeros((2,2,2,2), dtype=float) for ck in raw}),
        "by_lt_ls_kind": defaultdict(lambda: {ck: np.zeros((2,2,2,2), dtype=float) for ck in raw}),
        "by_lt_ls_kind_seed": defaultdict(lambda: {ck: np.zeros((2,2,2,2), dtype=float) for ck in raw}),
        "by_lt_ls_kind_seed_mode": defaultdict(lambda: {ck: np.zeros((2,2,2,2), dtype=float) for ck in raw}),
    }
    term_counts = 0
    nonzero_same_factors = 0

    for lt in range(2, Lmax+1):
        for ls in range(1, Lmax+1):
            P = 0.5*(step98.mu(lt)+step98.mu(ls))-1.0
            heat = math.exp(-tau*P)
            for tm_r in step98.tensor_value_modes(lt, T_rec_node):
                for sm_r in step98.scalar_hessian_modes(ls, S_rec_node):
                    Hrec = step98.tensor_scalar_hessian(tm_r.value, sm_r.hess, sector)
                    Rplus = step98.step96.receiver_matrix(Hrec, "plus")
                    Rminus = step98.step96.receiver_matrix(Hrec, "minus")
                    for tm_s in step98.tensor_value_modes(lt, T_src_node):
                        if tm_s.kind != tm_r.kind or tm_s.seed != tm_r.seed:
                            continue
                        for sm_s in step98.scalar_hessian_modes(ls, S_src_node):
                            if sm_s.mode != sm_r.mode:
                                continue
                            Hsrc = step98.tensor_scalar_hessian(tm_s.value, sm_s.hess, sector)
                            Splus = step98.step96.source_matrix_over_pi2(Hsrc, "plus")
                            Sminus = step98.step96.source_matrix_over_pi2(Hsrc, "minus")
                            norm_quot = tm_r.norm/2.0
                            pref = (math.pi**2)*heat/(P*norm_quot)
                            terms = {
                                "++": pref*np.einsum("ab,cd->abcd", Rplus, Splus),
                                "+-": pref*np.einsum("ab,cd->abcd", Rplus, Sminus),
                                "-+": pref*np.einsum("ab,cd->abcd", Rminus, Splus),
                                "--": pref*np.einsum("ab,cd->abcd", Rminus, Sminus),
                            }
                            term_counts += 1
                            if frob(terms["++"]) > 1e-14 or frob(terms["--"]) > 1e-14:
                                nonzero_same_factors += 1
                            keys = {
                                "by_lt_ls": (lt, ls),
                                "by_lt_ls_kind": (lt, ls, tm_r.kind),
                                "by_lt_ls_kind_seed": (lt, ls, tm_r.kind, tm_r.seed),
                                "by_lt_ls_kind_seed_mode": (lt, ls, tm_r.kind, tm_r.seed, sm_r.mode),
                            }
                            for ck, val in terms.items():
                                raw[ck] += val
                                for gname, gkey in keys.items():
                                    groups[gname][gkey][ck] += val

    def summarize_group(gdict):
        max_norm = {ck: 0.0 for ck in raw}
        max_witness = {ck: None for ck in raw}
        nonzero_groups = {ck: 0 for ck in raw}
        for key, vals in gdict.items():
            for ck, A in vals.items():
                n = frob(A)
                if n > 1e-12:
                    nonzero_groups[ck] += 1
                if n > max_norm[ck]:
                    max_norm[ck] = n
                    max_witness[ck] = repr(key)
        return {"max_norm": max_norm, "max_witness": max_witness, "nonzero_groups": nonzero_groups}

    return {
        "sector": sector,
        "pair": pair,
        "Lmax": Lmax,
        "tau": tau,
        "total_raw_norms": {ck: frob(A) for ck, A in raw.items()},
        "total_raw_max_abs": {ck: float(np.max(np.abs(A))) for ck, A in raw.items()},
        "term_counts": term_counts,
        "nonzero_individual_same_chirality_terms": nonzero_same_factors,
        "group_summaries": {gname: summarize_group(gdict) for gname, gdict in groups.items()},
    }


def main():
    results = {"step": 99, "purpose": "cancellation structure behind Step98 same-chirality zeros", "checks": []}
    for pair in ["NS", "SN", "SS"]:
        for sector in ["AA", "BB"]:
            results["checks"].append(compute_grouped(sector, pair, Lmax=16, tau=0.08))
    results["summary"] = {f"{c['sector']}_{c['pair']}": {
        "total_raw_norms": c["total_raw_norms"],
        "nonzero_individual_same_chirality_terms": c["nonzero_individual_same_chirality_terms"],
        "finest_group_nonzero_same": c["group_summaries"]["by_lt_ls_kind_seed_mode"]["nonzero_groups"],
        "ltls_group_max_same": {
            "++": c["group_summaries"]["by_lt_ls"]["max_norm"]["++"],
            "--": c["group_summaries"]["by_lt_ls"]["max_norm"]["--"],
        },
    } for c in results["checks"]}
    results["conclusion"] = [
        "Within the implemented tensor-scalar model, same-chirality factors are individually nonzero. Therefore B_{++}=B_{--}=0 is not a support-selection statement for single modes.",
        "The total same-chirality zero arises from signed cancellation in the complete electric/magnetic and scalar-polarization sum at fixed spectral truncation; this needs a structural identity, not just mode support bookkeeping.",
        "The Step98 note should state this as an observed exact cancellation in the implemented spectral model until such an identity is proved.",
    ]
    out = DATA_DIR / "step99_chirality_cancellation_structure.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps({"summary": results["summary"], "conclusion": results["conclusion"], "output": str(out)}, indent=2))

if __name__ == "__main__":
    main()
