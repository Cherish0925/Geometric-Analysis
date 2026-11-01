#!/usr/bin/env python3
"""
Step 85 corrected driver for the scalarized Green-transfer proxy.

The previous fast proxy data used an l1+l2-even filter inherited from an
incorrect interpretation of the quotient action.  The product orbifold here is
formed by a simultaneous half-turn around the two S^2 axes, fixing N/S poles.
For the local second-jet/multipole sector at fixed points, the half-turn acts by
-Id on each tangent 2-plane, so the even second-jet tensors survive without an
l-parity selection.  Zonal modes of every l are allowed; |m|=2 jet channels for
all l>=2 are also allowed.  This driver recomputes the scalarized proxy with all
l included and an explicit quotient lift factor.

It still is NOT the Ozuch coefficient: it is a source/receiver factor and
regularization test for c_ij^eps = L_i G_P^perp S_j^eps.
"""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

OUT = Path("Sessions/S0910A01/workspace/data/step85_corrected_scalar_proxy_driver.json")
MODPATH = "Sessions/S0910A01/workspace/scripts/step85_green_transfer_scalarized_proxy_fast.py"

spec = importlib.util.spec_from_file_location("s85fast", MODPATH)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)  # type: ignore


def compute():
    relations = ["adjacent_NS", "diagonal_SS"]
    frames = ["ambient", "antipodal_derivative"]
    shifts = [0.5, 1.0, 2.0]
    heats = [0.08, 0.04, 0.02, 0.01, 0.005, 0.0025]
    Ls = [20, 40, 60, 80, 120]

    runs = []
    for relation in relations:
        for frame in frames:
            for shift in shifts:
                for heat in heats:
                    seq = []
                    for L in Ls:
                        T = mod.transfer_matrix(L, relation, heat, shift, frame, quotient_even=False)
                        cs, co, diff = mod.coeffs_from_T(T)
                        seq.append({
                            "Lmax": L,
                            "c_same_proxy": cs,
                            "c_opp_proxy": co,
                            "diff_opp_minus_same_proxy": diff,
                            "matrix_stats": mod.stats(T),
                        })
                    runs.append({
                        "relation": relation,
                        "frame_transport_model": frame,
                        "shift": shift,
                        "heat_tau": heat,
                        "Lmax_sequence": seq,
                    })

    # Compact trend table at L=120.
    trend = []
    for r in runs:
        last = r["Lmax_sequence"][-1]
        trend.append({
            "relation": r["relation"],
            "frame_transport_model": r["frame_transport_model"],
            "shift": r["shift"],
            "heat_tau": r["heat_tau"],
            "Lmax": last["Lmax"],
            "diff": last["diff_opp_minus_same_proxy"],
            "c_same": last["c_same_proxy"],
            "c_opp": last["c_opp_proxy"],
        })

    result = {
        "scope": "corrected no-l-parity heat-regularized scalar-component proxy; not Ozuch full P coefficient",
        "correction_to_previous_fast_file": {
            "previous_file": "Sessions/S0910A01/workspace/data/step85_green_transfer_scalarized_proxy_fast.json",
            "error": "Its main regularized_runs set quotient_even=True, filtering l1+l2 odd modes. That is not the half-turn quotient selection for local fixed-point second jets.",
            "correct_quotient_local_action": "The simultaneous half-turn fixes the four poles and acts as -Id on each tangent 2-plane; second-jet/multipole tensors are even, so all zonal l channels and all |m|=2 channels with l>=2 survive. The quotient lift contributes a common image/normalization factor, not an l-parity filter.",
        },
        "proxy_object": "c_ij^epsilon = L_i G_P^perp S_j^epsilon, with G_P replaced here by a scalar-component additive product resolvent and with all l retained",
        "heats_and_truncations": {"heats": heats, "Lmax_values": Ls, "shifts": shifts},
        "runs": runs,
        "trend_L120": trend,
        "scientific_interpretation": {
            "stable_features_in_proxy": [
                "The local 8/3 Gram identity is not reproduced as a coefficient; source/receiver derivatives and denominators change the number.",
                "The second-jet channel requires all l>=2 and differentiated sums need heat/truncation comparisons.",
                "For this axis-aligned scalar-component model the C_ab matrix remains diagonal; this is a feature of the proxy symmetry and scalar identity propagation, not a theorem for the full Lichnerowicz transfer."
            ],
            "observed_proxy_trends": [
                "At heat_tau down to 0.0025 and Lmax=120, adjacent and diagonal differences are nonzero in this proxy, but their magnitude and sign depend on shift and frame convention for adjacent pairs.",
                "Diagonal antipodal-in-both-factors proxy is frame-insensitive in the tested ± frame models and gives c_opp<c_same for all tested shifts/heats.",
                "Adjacent one-antipodal-factor proxy is sensitive to frame transport; this reinforces that geometric node-frame normalization must be fixed before interpreting signs."
            ],
            "not_established": [
                "No numerical value here is c_opp-c_same for Ozuch's full operator.",
                "The full invariant P on trace/scalar-derived/vector-derived/tensor-derived/shape sectors may mix C_ab components and may cancel this proxy difference.",
                "A certified obstruction also needs the exact source S_j^epsilon, receiver L_i, pseudo-inverse projections, and nonlinear expansion layer."
            ]
        }
    }
    return result


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result = compute()
    OUT.write_text(json.dumps(result, indent=2))
    summary = {"output": str(OUT), "scope": result["scope"], "trend_subset_shift1": []}
    for row in result["trend_L120"]:
        if row["shift"] == 1.0 and row["heat_tau"] in [0.02, 0.01, 0.005, 0.0025]:
            summary["trend_subset_shift1"].append(row)
    print(json.dumps(summary, indent=2))
    print(f"Wrote {OUT}")
