#!/usr/bin/env python3
"""
Step 97: interpret the Step 96 AB-sector map on the physical Eguchi--Hanson
scale-angle parameter space.

The Step 96 AB map is a linear map Sym^2(K_source) -> Sym^2(K_receiver).
Physical bubble data do not fill all of Sym^2(K): they have the form
    M_j = t_j^2 u_j u_j^T,  |u_j|=1,
so in trace/double-angle coordinates x=tr(M), y=M22-M33, z=2M23 one has
    x>0 and y^2+z^2=x^2
for every nonzero insertion.  This script converts the compact AB matrices from
Step 96 into those coordinates and evaluates the induced receiver radial/angular
components.
"""
from __future__ import annotations

import json
import math
import pathlib
import random
from typing import Dict, List

import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

AB_PATH = DATA_DIR / "step96_kernel_plane_ab_map.json"

# Node order and checkerboard chirality from Step 91.
NODES = ["NN", "NS", "SN", "SS"]
EPS = {"NN": 1, "NS": -1, "SN": -1, "SS": 1}


def load_step96_adjacent_map() -> dict:
    with open(AB_PATH) as f:
        data = json.load(f)
    target = None
    for entry in data["adjacent_NS_ladder"]:
        if entry["source"] == "NS" and entry["Lmax"] == 260 and abs(entry["tau"] - 0.01) < 1e-14:
            target = entry
            break
    if target is None:
        raise RuntimeError("Could not find Step96 adjacent NS tau=0.01 Lmax=260 entry")
    return target


def compact_to_trace_double_angle(K: np.ndarray) -> np.ndarray:
    """Convert 3x3 compact map from [M22,M33,M23] to [tr,diff,2off].

    Step96 compact maps use receiver rows [A22,A33,A23] and source columns
    [M22,M33,M23].  Trace/double-angle coordinates are
        source: [x,y,z]=[M22+M33, M22-M33, 2M23]
        output: [X,Y,Z]=[A22+A33, A22-A33, 2A23].
    """
    source_entries_from_xyz = np.array([
        [0.5, 0.5, 0.0],   # M22
        [0.5, -0.5, 0.0],  # M33
        [0.0, 0.0, 1.0],   # compact third coordinate is 2*M23 = z
    ])
    xyz_from_output_entries = np.array([
        [1.0, 1.0, 0.0],   # trace
        [1.0, -1.0, 0.0],  # diff
        [0.0, 0.0, 2.0],   # 2off
    ])
    return xyz_from_output_entries @ K @ source_entries_from_xyz


def matrix_entries_from_scale_angle(t: float, theta: float) -> np.ndarray:
    c = math.cos(theta)
    s = math.sin(theta)
    return t * t * np.array([c * c, s * s, c * s], dtype=float)


def compact_input_from_scale_angle(t: float, theta: float) -> np.ndarray:
    c = math.cos(theta)
    s = math.sin(theta)
    # Step96 compact maps store the coefficient T[...,0,1]; a symmetric matrix
    # contributes T[...,0,1]M01+T[...,1,0]M10 = 2*T[...,0,1]M01.
    return t * t * np.array([c * c, s * s, 2.0 * c * s], dtype=float)


def source_xyz_from_scale_angle(t: float, theta: float) -> np.ndarray:
    return np.array([t * t, t * t * math.cos(2 * theta), t * t * math.sin(2 * theta)], dtype=float)


def block_from_compact_output(v: np.ndarray) -> np.ndarray:
    return np.array([[v[0], v[2]], [v[2], v[1]]], dtype=float)


def receiver_components(A: np.ndarray, theta: float) -> dict:
    u = np.array([math.cos(theta), math.sin(theta)], dtype=float)
    up = np.array([-math.sin(theta), math.cos(theta)], dtype=float)
    Au = A @ u
    return {
        "radial_uTAu": float(u @ Au),
        "angular_uperpTAu": float(up @ Au),
        "vector_Au": Au.tolist(),
    }


def map_eval_compact(K: np.ndarray, t_src: float, theta_src: float) -> np.ndarray:
    return K @ compact_input_from_scale_angle(t_src, theta_src)


def sample_physical_evaluations(Kodd: np.ndarray, Keven: np.ndarray, a: float) -> List[dict]:
    rng = random.Random(9701)
    rows = []
    for _ in range(8):
        t_src = 0.2 + 1.7 * rng.random()
        th_src = 2 * math.pi * rng.random()
        th_recv = 2 * math.pi * rng.random()
        M_entries = matrix_entries_from_scale_angle(t_src, th_src)
        xyz = source_xyz_from_scale_angle(t_src, th_src)
        odd_block = block_from_compact_output(map_eval_compact(Kodd, t_src, th_src))
        even_block = block_from_compact_output(map_eval_compact(Keven, t_src, th_src))
        odd_comp = receiver_components(odd_block, th_recv)
        even_comp = receiver_components(even_block, th_recv)
        rows.append({
            "t_source": t_src,
            "theta_source": th_src,
            "theta_receiver": th_recv,
            "source_matrix_entries_[M22,M33,M23]": M_entries.tolist(),
            "compact_input_[M22,M33,2M23]": compact_input_from_scale_angle(t_src, th_src).tolist(),
            "source_trace_double_angle_[x,y,z]": xyz.tolist(),
            "cone_residual_y2_plus_z2_minus_x2": float(xyz[1] ** 2 + xyz[2] ** 2 - xyz[0] ** 2),
            "odd_block": odd_block.tolist(),
            "odd_radial": odd_comp["radial_uTAu"],
            "odd_angular": odd_comp["angular_uperpTAu"],
            "odd_radial_minus_expected_-a_t2": float(odd_comp["radial_uTAu"] - (-a * t_src * t_src)),
            "odd_angular_abs": abs(odd_comp["angular_uperpTAu"]),
            "even_block": even_block.tolist(),
            "even_radial_minus_expected_+a_t2": float(even_comp["radial_uTAu"] - (a * t_src * t_src)),
            "even_angular_abs": abs(even_comp["angular_uperpTAu"]),
        })
    return rows


def adjacent_sources(node: str) -> List[str]:
    return [m for m in NODES if sum(a != b for a, b in zip(node, m)) == 1]


def checkerboard_relative_ab_row_formula(a: float) -> dict:
    # Uses the Step91 node-frame normalized adjacent identification.  The AB odd map
    # for an adjacent pair is A_ij(M_j) = -a tr(M_j) I.  The mixed-minus-all-same
    # coefficient multiplies it by eps_i eps_j - 1.
    formulas = {}
    numeric_sample_scales = {"NN": 1.0, "NS": 1.3, "SN": 0.7, "SS": 1.1}
    sample = {}
    for i in NODES:
        terms = []
        radial_coeff = 0.0
        for j in NODES:
            factor = EPS[i] * EPS[j] - 1
            if factor == 0:
                continue
            if j not in adjacent_sources(i):
                raise RuntimeError(f"unexpected surviving non-adjacent pair {i}<-{j}")
            # Relative vector contribution at receiver: t_i * factor * (-a t_j^2) u_i.
            terms.append({
                "source": j,
                "epsilon_i_epsilon_j_minus_1": factor,
                "block_contribution": f"{(-factor)*a:.12g} t_{j}^2 I_K",
                "radial_term": f"{(-factor)*a:.12g} t_{i} t_{j}^2",
                "angular_term": "0",
            })
            radial_coeff += (-factor) * a * numeric_sample_scales[i] * numeric_sample_scales[j] ** 2
        formulas[i] = {
            "terms": terms,
            "assembled_relative_AB_vector": f"{2*a:.12g} t_{i} sum_adjacent(j) t_j^2 * u_{i}",
            "radial_component": f"{2*a:.12g} t_{i} sum_adjacent(j) t_j^2",
            "angular_component": "0",
            "equal_scale_radial_component": f"{4*a:.12g} t^3",
        }
        sample[i] = radial_coeff
    return {
        "node_order": NODES,
        "epsilon_checkerboard": [EPS[n] for n in NODES],
        "assumption": "only the AB odd/odd adjacent map from Step96 is inserted; all other sectors and row-calibration terms are left out",
        "adjacent_pair_formula": "A_ij^AB,odd(M_j) = -a tr(M_j) I_K with a=-K_adj^AB>0",
        "per_receiver_formulas": formulas,
        "numeric_sample_scales": numeric_sample_scales,
        "numeric_sample_radial_components": sample,
    }


def main() -> None:
    adj = load_step96_adjacent_map()
    maps = adj["combo_compact_maps_basis"]["maps"]
    Kodd = np.array(maps["odd_odd"], dtype=float)
    Keven = np.array(maps["even_even"], dtype=float)
    a = -float(Kodd[0, 0])

    Kodd_xyz = compact_to_trace_double_angle(Kodd)
    Keven_xyz = compact_to_trace_double_angle(Keven)

    # Exact-rank interpretation in floating form.
    expected_odd_xyz = np.array([[-2 * a, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]])
    expected_even_xyz = -expected_odd_xyz

    rows = sample_physical_evaluations(Kodd, Keven, a)
    max_odd_radial_error = max(abs(r["odd_radial_minus_expected_-a_t2"]) for r in rows)
    max_odd_angular = max(r["odd_angular_abs"] for r in rows)
    max_even_radial_error = max(abs(r["even_radial_minus_expected_+a_t2"]) for r in rows)
    max_even_angular = max(r["even_angular_abs"] for r in rows)

    results = {
        "step": 97,
        "scope": "physical scale-angle interpretation of the Step96 AB-sector map",
        "source_file": str(AB_PATH),
        "adjacent_entry_used": {"receiver": adj["receiver"], "source": adj["source"], "tau": adj["tau"], "Lmax": adj["Lmax"]},
        "a_positive_defined_by_minus_Kadj_AB": a,
        "compact_odd_odd_map_rows_R22_R33_R23_cols_M22_M33_M23": Kodd.tolist(),
        "compact_even_even_map_rows_R22_R33_R23_cols_M22_M33_M23": Keven.tolist(),
        "trace_double_angle_coordinates": {
            "source": "x=tr(M)=M22+M33, y=M22-M33, z=2M23",
            "receiver": "X=tr(A)=A22+A33, Y=A22-A33, Z=2A23",
            "physical_cone": "M=t^2 u u^T, |u|=1, so x=t^2>0 and y^2+z^2=x^2 for t>0",
            "odd_odd_matrix_[X,Y,Z]_<-[x,y,z]": Kodd_xyz.tolist(),
            "even_even_matrix_[X,Y,Z]_<-[x,y,z]": Keven_xyz.tolist(),
            "expected_odd_odd_matrix": expected_odd_xyz.tolist(),
            "expected_even_even_matrix": expected_even_xyz.tolist(),
            "max_abs_odd_matrix_error": float(np.max(np.abs(Kodd_xyz - expected_odd_xyz))),
            "max_abs_even_matrix_error": float(np.max(np.abs(Keven_xyz - expected_even_xyz))),
        },
        "physical_cone_consequence": {
            "odd_block_formula": "A_odd(M) = -a tr(M) I_K",
            "even_block_formula": "A_even(M) = +a tr(M) I_K",
            "unrestricted_kernel": "tr(M)=0, a two-dimensional traceless subspace inside Sym^2(K)",
            "physical_kernel_intersection": "If M=t^2 u u^T is positive semidefinite rank one, tr(M)=t^2; hence A_odd(M)=0 iff t=0.",
            "angular_blindness": "For every receiver unit u_i, u_i_perp^T A_odd(M_j) u_i = 0; the AB sector supplies no angular alignment equation.",
            "radial_response": "u_i^T A_odd(M_j) u_i = -a t_j^2, independent of source and receiver angles.",
        },
        "random_physical_evaluations": rows,
        "max_random_errors": {
            "cone_residual_abs": max(abs(r["cone_residual_y2_plus_z2_minus_x2"]) for r in rows),
            "odd_radial_error_abs": max_odd_radial_error,
            "odd_angular_abs": max_odd_angular,
            "even_radial_error_abs": max_even_radial_error,
            "even_angular_abs": max_even_angular,
        },
        "checkerboard_relative_AB_row_under_adjacent_identification": checkerboard_relative_ab_row_formula(a),
        "interpretation": [
            "The AB-sector rank-one map is not evidence that a physical bubble can choose an angular source lying in the map kernel; the kernel is traceless and contains no nonzero positive semidefinite rank-one source.",
            "In a reduced equation, a receiver block A_i should be applied to the receiver direction u_i. The scalar radial entry is u_i^T A_i u_i and the angular entry is u_i_perp^T A_i u_i.",
            "For the Step96 adjacent AB odd map, the radial entry is angle-independent and the angular entry vanishes. Thus this sector controls scale balance only; angular selection must come from AA/BB tensor sectors, frame transport, self/opposite-corner terms, deformation variables, or higher-order effects.",
            "This computation uses only the AB one-form sector and the Step91 adjacent exchange normalization. It is not a complete product-orbifold desingularization result and has no direct bearing on the full Yau-26 proposition without the remaining gluing analysis.",
        ],
    }

    out = DATA_DIR / "step97_ab_physical_cone_row.json"
    with open(out, "w") as f:
        json.dump(results, f, indent=2)
    print(json.dumps(results, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
