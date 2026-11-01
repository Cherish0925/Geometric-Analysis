#!/usr/bin/env python3
"""Step 99 A02 audit of A01 Step98 trace-obstruction data.

This script does not rerun the full spectral sums.  It parses A01's raw JSON
outputs and independently recomputes the derived assertions needed by A02:

* raw same-chirality cancellation for AB and AA/BB sectors;
* cross-parity and chirality-equality checks in the AA/BB tensor data;
* conversion of AB raw maps to trace/double-angle variables;
* separation of the angle-independent trace/isotropic channel from traceless
  P/Q channels;
* leading-order pattern consequences for the diagonal-balanced and
  adjacent-balanced rows for arbitrary positive bubble-scale squares.

The output is an audit record, not a theorem-grade Ozuch gluing proof.  It
records which conclusions are supported by the raw inter-node data and which
still require a full Lyapunov--Schmidt/remainder argument.
"""
from __future__ import annotations

import json
import math
import pathlib
import re
from typing import Any

import numpy as np

HERE = pathlib.Path(__file__).resolve()
ROOT = pathlib.Path.cwd() if (pathlib.Path.cwd() / "Sessions").exists() else HERE.parents[4]
A01_DATA = ROOT / "Sessions/S0910A01/workspace/data"
A02_DATA = ROOT / "Sessions/S0910A02/workspace/data"
A02_DATA.mkdir(parents=True, exist_ok=True)

TENSOR_PATH = A01_DATA / "step98_full_chirality_tensor_maps.json"
AB_PATH = A01_DATA / "step96_kernel_plane_ab_map.json"
STEP96_PATTERN_PATH = ROOT / "Sessions/S0910A02/workspace/data/step96_corrected_selection_determinantal.json"


def load(path: pathlib.Path) -> Any:
    with path.open() as f:
        return json.load(f)


def asarr(x: Any) -> np.ndarray:
    return np.asarray(x, dtype=float)


def max_abs(x: Any) -> float:
    a = asarr(x)
    if a.size == 0:
        return 0.0
    return float(np.max(np.abs(a)))


def compact_from_raw4(T: np.ndarray) -> np.ndarray:
    """Receiver [22,33,23] versus source [22,33,23-matrix-entry]."""
    return np.array([
        [T[0, 0, 0, 0], T[0, 0, 1, 1], T[0, 0, 0, 1]],
        [T[1, 1, 0, 0], T[1, 1, 1, 1], T[1, 1, 0, 1]],
        [T[0, 1, 0, 0], T[0, 1, 1, 1], T[0, 1, 0, 1]],
    ], dtype=float)


def trace_double_angle_matrix(K: np.ndarray) -> np.ndarray:
    """Same convention as A01 Step98: rows/cols [trace,diff,2offdiag]."""
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


def pq_from_tda(Axyz: np.ndarray) -> dict[str, float]:
    """Traceless complex P/Q decomposition plus trace coefficient.

    c0_trace is the coefficient mapping source trace to output trace.  The
    isotropic eigenvalue coefficient for a unit-trace source is c0_trace/2.
    P/Q are the traceless complex-linear/anti-linear coefficients.
    """
    Ayy = Axyz[1, 1]
    Ayz = Axyz[1, 2]
    Azy = Axyz[2, 1]
    Azz = Axyz[2, 2]
    P = complex((Ayy + Azz) / 4.0, (Azy - Ayz) / 4.0)
    Q = complex((Ayy - Azz) / 4.0, (Azy + Ayz) / 4.0)
    return {
        "c0_trace": float(Axyz[0, 0]),
        "isotropic_eigen_coeff": float(Axyz[0, 0] / 2.0),
        "P_re": float(P.real),
        "P_im": float(P.imag),
        "P_abs": float(abs(P)),
        "Q_re": float(Q.real),
        "Q_im": float(Q.imag),
        "Q_abs": float(abs(Q)),
        "trace_angle_mixing_max_abs": float(max(abs(Axyz[0, 1]), abs(Axyz[0, 2]), abs(Axyz[1, 0]), abs(Axyz[2, 0]))),
    }


def rung_key_sort(key: str) -> tuple[float, int]:
    m = re.match(r"tau=([0-9.]+)_Lmax=(\d+)", key)
    if not m:
        return (math.inf, -1)
    return (float(m.group(1)), int(m.group(2)))


def audit_tensor(tensor: dict[str, Any]) -> dict[str, Any]:
    rung_keys = sorted([k for k in tensor if k.startswith("tau=")], key=rung_key_sort, reverse=True)
    pairs = ["NS", "SN", "SS"]
    sectors = ["AA", "BB"]
    per_rung = []
    global_max_same = 0.0
    global_max_same_eq = 0.0
    global_max_cross_eq = 0.0
    global_max_cross_parity = 0.0
    global_max_trace_in_tensor = 0.0
    for rk in rung_keys:
        rung = tensor[rk]
        entry_summary = {"rung": rk, "pairs": {}}
        for pair in pairs:
            entry_summary["pairs"][pair] = {}
            for sector in sectors:
                e = rung[pair][sector]
                raw = e["raw_chirality_maps"]
                pp = asarr(raw["plus_plus"]["trace_double_angle"])
                pm = asarr(raw["plus_minus"]["trace_double_angle"])
                mp = asarr(raw["minus_plus"]["trace_double_angle"])
                mm = asarr(raw["minus_minus"]["trace_double_angle"])
                same = max(max_abs(pp), max_abs(mm))
                same_eq = max_abs(pp - mm)
                cross_eq = max_abs(pm - mp)
                cp = e["even_odd_decomposition"]["cross_parity_vanishing_check"]
                cross_parity = max(abs(cp["max_abs_even_odd"]), abs(cp["max_abs_odd_even"]))
                pq_pm = pq_from_tda(pm)
                pq_pp = pq_from_tda(pp)
                global_max_same = max(global_max_same, same)
                global_max_same_eq = max(global_max_same_eq, same_eq)
                global_max_cross_eq = max(global_max_cross_eq, cross_eq)
                global_max_cross_parity = max(global_max_cross_parity, cross_parity)
                global_max_trace_in_tensor = max(global_max_trace_in_tensor, abs(pq_pm["c0_trace"]), abs(pq_pp["c0_trace"]))
                entry_summary["pairs"][pair][sector] = {
                    "same_chirality_max_abs_tda": same,
                    "B++_minus_B--_max_abs_tda": same_eq,
                    "B+-_minus_B-+_max_abs_tda": cross_eq,
                    "cross_parity_max_abs": cross_parity,
                    "plus_minus_PQ": pq_pm,
                }
        per_rung.append(entry_summary)
    finest_key = sorted([k for k in tensor if k.startswith("tau=")], key=rung_key_sort)[0]
    # The sort above puts smallest tau first, finest in this finite ladder.
    finest = tensor[finest_key]
    pair_coeffs = {}
    for pair in pairs:
        pair_coeffs[pair] = {}
        combined_pm = np.zeros((3, 3))
        for sector in sectors:
            pm = asarr(finest[pair][sector]["raw_chirality_maps"]["plus_minus"]["trace_double_angle"])
            combined_pm += pm
            pair_coeffs[pair][sector] = pq_from_tda(pm)
        pair_coeffs[pair]["AA_plus_BB"] = pq_from_tda(combined_pm)
    return {
        "rung_keys": rung_keys,
        "per_rung_checks": per_rung,
        "global_checks": {
            "tensor_raw_same_chirality_max_abs": global_max_same,
            "tensor_B++_minus_B--_max_abs": global_max_same_eq,
            "tensor_B+-_minus_B-+_max_abs": global_max_cross_eq,
            "tensor_cross_parity_max_abs": global_max_cross_parity,
            "tensor_trace_channel_max_abs": global_max_trace_in_tensor,
            "pass_at_1e-10": all(x < 1e-10 for x in [global_max_same, global_max_same_eq, global_max_cross_eq, global_max_cross_parity, global_max_trace_in_tensor]),
        },
        "finest_rung": finest_key,
        "finest_pair_coefficients_AA_BB": pair_coeffs,
    }


def audit_ab(ab: dict[str, Any]) -> dict[str, Any]:
    entries = []
    for e in ab.get("adjacent_NS_ladder", []):
        entries.append((f"ladder_NS_tau={e['tau']}_L={e['Lmax']}", e))
    for e in ab.get("pair_compare_tau_0p02_L180", []):
        entries.append((f"pair_{e['source']}_tau={e['tau']}_L={e['Lmax']}", e))
    global_same = 0.0
    global_cross_eq = 0.0
    global_traceless = 0.0
    per_entry = []
    pair_coeffs = {}
    for label, e in entries:
        raw = e["raw_chirality_maps"]
        pp = asarr(raw["plus_recv__plus_src"])
        pm = asarr(raw["plus_recv__minus_src"])
        mp = asarr(raw["minus_recv__plus_src"])
        mm = asarr(raw["minus_recv__minus_src"])
        same = max(max_abs(pp), max_abs(mm))
        cross_eq = max_abs(pm - mp)
        tda_pm = trace_double_angle_matrix(compact_from_raw4(pm))
        pq_pm = pq_from_tda(tda_pm)
        global_same = max(global_same, same)
        global_cross_eq = max(global_cross_eq, cross_eq)
        global_traceless = max(global_traceless, pq_pm["P_abs"], pq_pm["Q_abs"], pq_pm["trace_angle_mixing_max_abs"])
        rec = {
            "label": label,
            "source": e["source"],
            "Lmax": e["Lmax"],
            "tau": e["tau"],
            "same_chirality_raw_max_abs": same,
            "cross_B+-_minus_B-+_max_abs": cross_eq,
            "plus_minus_trace_double_angle": np.round(tda_pm, 12).tolist(),
            "plus_minus_decomposition": pq_pm,
        }
        per_entry.append(rec)
        if label.startswith("pair_"):
            pair_coeffs[e["source"]] = pq_pm
    return {
        "per_entry_checks": per_entry,
        "global_checks": {
            "AB_raw_same_chirality_max_abs": global_same,
            "AB_B+-_minus_B-+_max_abs": global_cross_eq,
            "AB_traceless_or_trace_mixing_max_abs": global_traceless,
            "pass_at_1e-10": all(x < 1e-10 for x in [global_same, global_cross_eq, global_traceless]),
        },
        "pair_coefficients_tau0p02_L180": pair_coeffs,
    }


def pair_type(a: str, b: str) -> str:
    dist = sum(x != y for x, y in zip(a, b))
    if dist == 1:
        return "adjacent"
    if dist == 2:
        return "diagonal"
    raise ValueError((a, b))


def pattern_analysis(ab_audit: dict[str, Any], tensor_audit: dict[str, Any], patterns: dict[str, Any]) -> dict[str, Any]:
    ab_pairs = ab_audit["pair_coefficients_tau0p02_L180"]
    tensor_pairs = tensor_audit["finest_pair_coefficients_AA_BB"]
    # Positive-product physical cross-chirality coefficients at receiver NN.
    c_adj = (ab_pairs["NS"]["isotropic_eigen_coeff"] + ab_pairs["SN"]["isotropic_eigen_coeff"]) / 2.0
    c_diag = ab_pairs["SS"]["isotropic_eigen_coeff"]
    q_adj_NS = max(tensor_pairs["NS"]["AA_plus_BB"]["P_abs"], tensor_pairs["NS"]["AA_plus_BB"]["Q_abs"])
    q_adj_SN = max(tensor_pairs["SN"]["AA_plus_BB"]["P_abs"], tensor_pairs["SN"]["AA_plus_BB"]["Q_abs"])
    q_adj = max(q_adj_NS, q_adj_SN)
    q_diag = max(tensor_pairs["SS"]["AA_plus_BB"]["P_abs"], tensor_pairs["SS"]["AA_plus_BB"]["Q_abs"])
    coeffs = {
        "cross_adjacent": {
            "c0_trace": float((ab_pairs["NS"]["c0_trace"] + ab_pairs["SN"]["c0_trace"]) / 2.0),
            "isotropic_eigen_coeff": float(c_adj),
            "traceless_bound_coeff": float(q_adj),
            "margin_isotropic_minus_traceless": float(c_adj - q_adj),
        },
        "cross_diagonal": {
            "c0_trace": float(ab_pairs["SS"]["c0_trace"]),
            "isotropic_eigen_coeff": float(c_diag),
            "traceless_bound_coeff": float(q_diag),
        },
        "same_chirality_all_pair_types": {
            "coefficient_status": "zero in the parsed AB and AA/BB raw maps at every available rung; this is a physical chirality statement (epsilon_i=epsilon_j), not the older parity-odd coefficient.",
        },
    }

    nodes = ["NN", "NS", "SN", "SS"]
    pattern_outputs: dict[str, Any] = {}
    # Use the named patterns from Step96 plus a compact all-reversed row.
    for pname in ["all_compatible", "diagonal_balanced", "adjacent_balanced_AB", "all_reversed"]:
        if pname not in patterns:
            continue
        eps = {n: patterns[pname][n]["chirality"] for n in nodes}
        receivers = {}
        for r in nodes:
            iso_terms = []
            tr_terms = []
            same_terms = []
            for s in nodes:
                if s == r:
                    continue
                typ = pair_type(r, s)
                if eps[r] == eps[s]:
                    same_terms.append({"source": s, "pair_type": typ, "coefficient": 0.0})
                else:
                    if typ == "adjacent":
                        iso_terms.append({"source": s, "pair_type": typ, "coefficient": float(c_adj)})
                        tr_terms.append({"source": s, "pair_type": typ, "abs_bound_coeff": float(q_adj)})
                    else:
                        iso_terms.append({"source": s, "pair_type": typ, "coefficient": float(c_diag)})
                        # q_diag currently zero in raw cross data.
                        tr_terms.append({"source": s, "pair_type": typ, "abs_bound_coeff": float(q_diag)})
            receivers[r] = {"chirality": eps[r], "isotropic_terms": iso_terms, "traceless_bound_terms": tr_terms, "same_chirality_zero_terms": same_terms}
        pattern_outputs[pname] = {"eps": eps, "receiver_formulas": receivers}

    diag_margin = c_adj - q_adj
    # Adjacent-balanced possible kernel ratios for a receiver with one adjacent and one diagonal opposite source.
    ratio_zero = c_adj / abs(c_diag) if c_diag != 0 else math.inf
    ratio_low = (c_adj - q_adj) / abs(c_diag) if c_diag != 0 else math.inf
    ratio_high = (c_adj + q_adj) / abs(c_diag) if c_diag != 0 else math.inf

    criteria = {
        "diagonal_balanced": {
            "opposite_partners_per_receiver": "two adjacent cross-chirality partners and one same-chirality diagonal partner; same terms vanish",
            "matrix_bound": "A_j = c_adj*(u_adj1+u_adj2) I + traceless, ||traceless|| <= q_adj*(u_adj1+u_adj2)",
            "uniform_positive_definite_for_positive_scales": bool(diag_margin > 0),
            "margin_per_unit_opposite_adjacent_scale": float(diag_margin),
            "interpretation": "In the raw inter-node model every receiver equation is invertible/positive definite for four positive scales; this verifies A01's leading diagonal-balanced trace obstruction, subject to LS and remainder caveats.",
        },
        "adjacent_balanced_AB": {
            "opposite_partners_per_receiver": "one adjacent and one diagonal cross-chirality partner (up to square symmetry), plus one same-chirality zero partner",
            "representative_equation": "|c_adj*u_adj + c_diag*u_diag| = q_adj*u_adj is possible because c_adj>0 and c_diag<0",
            "P_zero_ratio_u_diag_over_u_adj": float(ratio_zero),
            "kernel_equality_ratios_u_diag_over_u_adj": [float(ratio_low), float(ratio_high)],
            "uniform_obstruction_from_raw_pair_table": False,
            "interpretation": "The leading raw pair table leaves scale-ratio windows where the determinant condition can be met; it does not prove existence of a coupled critical point, but it invalidates a uniform trace obstruction for the adjacent-balanced row.",
        },
    }
    return {"coefficients": coeffs, "patterns": pattern_outputs, "criteria": criteria}


def main() -> None:
    tensor = load(TENSOR_PATH)
    ab = load(AB_PATH)
    pattern_file = load(STEP96_PATTERN_PATH)
    tensor_audit = audit_tensor(tensor)
    ab_audit = audit_ab(ab)
    pat = pattern_analysis(ab_audit, tensor_audit, pattern_file["patterns"])

    result = {
        "step": 99,
        "purpose": "A02 independent audit of A01 Step98 raw chirality trace-obstruction data and pattern consequences.",
        "input_files": {
            "A01_tensor": str(TENSOR_PATH.relative_to(ROOT)),
            "A01_AB": str(AB_PATH.relative_to(ROOT)),
            "A02_pattern_data": str(STEP96_PATTERN_PATH.relative_to(ROOT)),
        },
        "tensor_AA_BB_audit": tensor_audit,
        "AB_audit": ab_audit,
        "combined_cross_chirality_and_pattern_analysis": pat,
        "main_conclusions": [
            "At every available rung, raw same-chirality maps B++ and B-- vanish in AB and AA/BB tensor sectors; cross-parity vanishes and B+-=B-+ in the tensor data. This supports A01's same-chirality leading inter-node vanishing and cross-verifies the compatible KE calibration at the raw spectral level.",
            "The old A02/A01 parity coefficients c_adj=-0.03144 and c_diag=+0.01773 are not physical same-chirality pair coefficients. The physical cross-chirality AB trace coefficients at receiver NN are c0=+0.12576998928 for adjacent pairs and c0=-0.070907042884 for the diagonal pair, i.e. isotropic eigen coefficients +0.06288499464 and -0.035453521442.",
            "AA/BB tensor cross-chirality maps are traceless: adjacent NS carries a Q-type coefficient about 0.0080049973185, adjacent SN carries a P-type coefficient of the same magnitude, and the diagonal tensor cross coefficient is zero in the available data.",
            "For the diagonal-balanced pattern eps=(+,-,-,+), each receiver sees two opposite-chirality adjacent sources and a same-chirality diagonal source. Since 0.06288499464 > 0.00800499732, the raw inter-node matrix is uniformly positive definite/invertible for arbitrary positive scales and phases. This verifies the leading inter-node obstruction candidate for that row.",
            "For the adjacent-balanced pattern eps=(+,+,-,-), each receiver sees one cross adjacent source and one cross diagonal source. Because the isotropic coefficients have opposite signs, determinant equality is possible for positive scale-square ratios u_diag/u_adj near 1.55 or 2.00 (P zero near 1.77). Thus the raw pair table does not uniformly obstruct this row and may split the two balanced topologies.",
            "None of these conclusions is yet a full Ozuch obstruction theorem: a calibrated LS reduction, self/complement/frame/global term accounting, and relative o(t^3) remainder are still required; even then the result is local near this orbifold and does not prove global no-Einstein for Yau 26.",
        ],
    }
    out = A02_DATA / "step99_a01_trace_obstruction_audit.json"
    with out.open("w") as f:
        json.dump(result, f, indent=2)
    brief = {
        "wrote": str(out.relative_to(ROOT)),
        "same_chirality_tensor_pass": tensor_audit["global_checks"]["pass_at_1e-10"],
        "same_chirality_AB_pass": ab_audit["global_checks"]["pass_at_1e-10"],
        "cross_adjacent_isotropic_eigen": pat["coefficients"]["cross_adjacent"]["isotropic_eigen_coeff"],
        "cross_adjacent_traceless_bound": pat["coefficients"]["cross_adjacent"]["traceless_bound_coeff"],
        "cross_diagonal_isotropic_eigen": pat["coefficients"]["cross_diagonal"]["isotropic_eigen_coeff"],
        "diagonal_balanced_margin": pat["criteria"]["diagonal_balanced"]["margin_per_unit_opposite_adjacent_scale"],
        "adjacent_balanced_kernel_ratio_interval": pat["criteria"]["adjacent_balanced_AB"]["kernel_equality_ratios_u_diag_over_u_adj"],
    }
    print(json.dumps(brief, indent=2))


if __name__ == "__main__":
    main()
