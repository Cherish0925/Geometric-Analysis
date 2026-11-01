#!/usr/bin/env python3
"""Selected rerun of A01 Step98/Step96 spectral computations for A02 Step99.

This is a lightweight recomputation from A01's scripts, independent of the
stored A01 JSON data.  It recomputes one tensor ladder rung and selected AB
entries, converts them with the same A02 trace/double-angle decomposition, and
compares against A01's stored JSON.  The purpose is to catch stale JSON/header
or transcription errors before A02 patches its route notes.
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import sys
from typing import Any

import numpy as np

ROOT = pathlib.Path.cwd()
A01_SCRIPTS = ROOT / "Sessions/S0910A01/workspace/scripts"
A01_DATA = ROOT / "Sessions/S0910A01/workspace/data"
A02_DATA = ROOT / "Sessions/S0910A02/workspace/data"
A02_DATA.mkdir(parents=True, exist_ok=True)


def import_from(path: pathlib.Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod

step96 = import_from(A01_SCRIPTS / "step96_kernel_plane_ab_map.py", "a01_step96_ab_for_step99")
step98 = import_from(A01_SCRIPTS / "step98_full_chirality_tensor_maps.py", "a01_step98_tensor_for_step99")


def arr(x: Any) -> np.ndarray:
    return np.asarray(x, dtype=float)


def compact_from_raw4(T: np.ndarray) -> np.ndarray:
    return np.array([
        [T[0, 0, 0, 0], T[0, 0, 1, 1], T[0, 0, 0, 1]],
        [T[1, 1, 0, 0], T[1, 1, 1, 1], T[1, 1, 0, 1]],
        [T[0, 1, 0, 0], T[0, 1, 1, 1], T[0, 1, 0, 1]],
    ])


def trace_double_angle_matrix(K: np.ndarray) -> np.ndarray:
    source_entries_from_xyz = np.array([
        [0.5, 0.5, 0.0],
        [0.5, -0.5, 0.0],
        [0.0, 0.0, 1.0],
    ])
    xyz_from_output_entries = np.array([
        [1.0, 1.0, 0.0],
        [1.0, -1.0, 0.0],
        [0.0, 0.0, 2.0],
    ])
    return xyz_from_output_entries @ K @ source_entries_from_xyz


def pq_from_tda(A: np.ndarray) -> dict[str, float]:
    Ayy, Ayz, Azy, Azz = A[1, 1], A[1, 2], A[2, 1], A[2, 2]
    P = complex((Ayy + Azz) / 4.0, (Azy - Ayz) / 4.0)
    Q = complex((Ayy - Azz) / 4.0, (Azy + Ayz) / 4.0)
    return {"c0_trace": float(A[0, 0]), "isotropic_eigen": float(A[0, 0] / 2),
            "P_abs": float(abs(P)), "Q_abs": float(abs(Q)),
            "P_re": float(P.real), "Q_re": float(Q.real)}


def max_abs(x: Any) -> float:
    a = arr(x)
    return float(np.max(np.abs(a))) if a.size else 0.0


def tensor_summary(entry: dict[str, Any]) -> dict[str, Any]:
    raw = entry["raw_chirality_maps"]
    pp = arr(raw["plus_plus"]["trace_double_angle"])
    pm = arr(raw["plus_minus"]["trace_double_angle"])
    mp = arr(raw["minus_plus"]["trace_double_angle"])
    mm = arr(raw["minus_minus"]["trace_double_angle"])
    return {
        "same_max_abs": max(max_abs(pp), max_abs(mm)),
        "cross_pm_minus_mp": max_abs(pm - mp),
        "plus_minus_PQ": pq_from_tda(pm),
    }


def ab_summary(entry: dict[str, Any]) -> dict[str, Any]:
    raw = entry["raw_chirality_maps"]
    pp = arr(raw["plus_recv__plus_src"])
    pm = arr(raw["plus_recv__minus_src"])
    mp = arr(raw["minus_recv__plus_src"])
    mm = arr(raw["minus_recv__minus_src"])
    tda_pm = trace_double_angle_matrix(compact_from_raw4(pm))
    return {"same_max_abs": max(max_abs(pp), max_abs(mm)),
            "cross_pm_minus_mp": max_abs(pm - mp),
            "plus_minus_tda": np.round(tda_pm, 12).tolist(),
            "plus_minus_PQ": pq_from_tda(tda_pm)}


def main() -> None:
    stored_tensor = json.load(open(A01_DATA / "step98_full_chirality_tensor_maps.json"))
    stored_ab = json.load(open(A01_DATA / "step96_kernel_plane_ab_map.json"))

    tensor_rerun: dict[str, Any] = {}
    max_delta_tensor = 0.0
    # Recompute the cheapest full tensor rung, all pair/sector combinations.
    for pair in ["NS", "SN", "SS"]:
        tensor_rerun[pair] = {}
        for sector in ["AA", "BB"]:
            e = step98.compute_full_chirality(sector, 80, 0.08, pair)
            # Add P/Q only for concise summary; stored data already has it.
            s = tensor_summary(e)
            stored_s = tensor_summary(stored_tensor["tau=0.08_Lmax=80"][pair][sector])
            delta = max_abs(arr(e["raw_chirality_maps"]["plus_minus"]["trace_double_angle"]) -
                            arr(stored_tensor["tau=0.08_Lmax=80"][pair][sector]["raw_chirality_maps"]["plus_minus"]["trace_double_angle"]))
            max_delta_tensor = max(max_delta_tensor, delta)
            tensor_rerun[pair][sector] = {"rerun": s, "stored": stored_s, "max_abs_delta_plus_minus_tda": delta}

    ab_rerun: dict[str, Any] = {}
    max_delta_ab = 0.0
    for pair in ["NS", "SN", "SS"]:
        e = step96.compute_ab_map(180, 0.02, pair)
        s = ab_summary(e)
        stored_entry = next(x for x in stored_ab["pair_compare_tau_0p02_L180"] if x["source"] == pair)
        ss = ab_summary(stored_entry)
        delta = max_abs(arr(s["plus_minus_tda"]) - arr(ss["plus_minus_tda"]))
        max_delta_ab = max(max_delta_ab, delta)
        ab_rerun[pair] = {"rerun": s, "stored": ss, "max_abs_delta_plus_minus_tda": delta}

    result = {
        "step": 99,
        "purpose": "Selected spectral rerun from A01 scripts, independent of A01 stored JSON data.",
        "tensor_rerun_tau0p08_L80": tensor_rerun,
        "AB_rerun_tau0p02_L180": ab_rerun,
        "max_abs_delta_tensor_plus_minus_tda_vs_stored": max_delta_tensor,
        "max_abs_delta_AB_plus_minus_tda_vs_stored": max_delta_ab,
        "pass": max_delta_tensor < 1e-11 and max_delta_ab < 1e-11,
    }
    out = A02_DATA / "step99_selected_spectral_recompute.json"
    with out.open("w") as f:
        json.dump(result, f, indent=2)
    print(json.dumps({
        "wrote": str(out.relative_to(ROOT)),
        "pass": result["pass"],
        "max_abs_delta_tensor": max_delta_tensor,
        "max_abs_delta_AB": max_delta_ab,
        "diag_bal_NS_AA_Q": tensor_rerun["NS"]["AA"]["rerun"]["plus_minus_PQ"]["Q_abs"],
        "adjacent_AB_iso": ab_rerun["NS"]["rerun"]["plus_minus_PQ"]["isotropic_eigen"],
        "diagonal_AB_iso": ab_rerun["SS"]["rerun"]["plus_minus_PQ"]["isotropic_eigen"],
    }, indent=2))


if __name__ == "__main__":
    main()
