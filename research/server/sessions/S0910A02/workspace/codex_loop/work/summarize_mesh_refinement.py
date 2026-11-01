#!/usr/bin/env python3
"""Consolidate the precomputed subdivision 2/3/4 toy-flow runs."""
from __future__ import annotations

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent
INPUTS = {
    2: ROOT / "refinement" / "subdiv2" / "toy_flow_results.json",
    3: ROOT / "toy_flow_results.json",
    4: ROOT / "refinement" / "subdiv4" / "toy_flow_results.json",
}
OUTPUT = ROOT / "mesh_refinement_summary.json"


def first_below(run: dict, metric: str, threshold: float) -> float | None:
    for time, value in zip(run["times"], run["metrics"][metric]):
        if value <= threshold:
            return float(time)
    return None


def main() -> None:
    records = []
    for subdivision, path in INPUTS.items():
        data = json.loads(path.read_text())
        record = {
            "subdivision": subdivision,
            "vertices": data["mesh"]["vertices"],
            "v4_reduced_variables": data["mesh"]["v4_reduced_variables"],
            "reference_direct_literal_einstein_floor": data["mesh"]["reference_direct_literal_einstein_floor"],
            "control_pass": data["control_pass"],
            "runs": {},
        }
        for kind in ("control", "mixed"):
            run = data["runs"][kind]
            record["runs"][kind] = {
                "mechanism": run["interpreted_mechanism"],
                "final_model_defect_sup": run["metrics"]["model_defect_sup"][-1],
                "final_direct_einstein_sup": run["metrics"]["direct_einstein_sup"][-1],
                "final_direct_target_relative_sup": run["metrics"]["direct_target_relative_sup"][-1],
                "time_direct_target_relative_below_0.03": first_below(run, "direct_target_relative_sup", 0.03),
                "initial_seam_area_ratio_min": run["metrics"]["seam_area_ratio_min"][0],
                "final_seam_area_ratio_min": run["metrics"]["seam_area_ratio_min"][-1],
                "max_interior_abs_curvature": max(run["metrics"]["interior_abs_curvature_max"]),
                "max_symmetry_error_sup": max(run["metrics"]["symmetry_error_sup"]),
                "liouville_energy_upward_steps_above_1e-8": run["variational_audit"]["upward_saved_steps_above_1e-8"],
            }
        records.append(record)

    floors = [record["reference_direct_literal_einstein_floor"] for record in records]
    observed_orders = [math.log(floors[i] / floors[i + 1], 2.0) for i in range(len(floors) - 1)]
    checks = {
        "all_control_gates_pass": all(record["control_pass"] for record in records),
        "all_runs_classified_converged": all(
            record["runs"][kind]["mechanism"] == "converged"
            for record in records
            for kind in ("control", "mixed")
        ),
        "literal_direct_round_floor_strictly_decreases": all(a > b for a, b in zip(floors, floors[1:])),
        "all_mesh_calibrated_direct_final_below_1e-7": all(
            record["runs"][kind]["final_direct_target_relative_sup"] < 1.0e-7
            for record in records
            for kind in ("control", "mixed")
        ),
        "exact_v4_symmetry_at_saved_times": all(
            record["runs"][kind]["max_symmetry_error_sup"] == 0.0
            for record in records
            for kind in ("control", "mixed")
        ),
        "liouville_energy_nonincreasing_at_1e-8_tolerance": all(
            record["runs"][kind]["liouville_energy_upward_steps_above_1e-8"] == 0
            for record in records
            for kind in ("control", "mixed")
        ),
    }
    output = {
        "status": "pass" if all(checks.values()) else "check_failed",
        "scope": "Resolution consistency check for the 2D V4 toy only.",
        "records": records,
        "direct_round_floor_observed_orders_under_edge_halving": observed_orders,
        "checks": checks,
    }
    OUTPUT.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
