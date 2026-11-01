#!/usr/bin/env python3
"""Step 97 concise channel summary from AB and tensor odd maps."""
from __future__ import annotations
import json, pathlib
import numpy as np

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
WS = SCRIPT_DIR.parent
DATA_DIR = WS / "data"

with open(DATA_DIR / "step97_ab_physical_cone_row.json") as f:
    ab = json.load(f)
with open(DATA_DIR / "step97_tensor_odd_physical_map.json") as f:
    ten = json.load(f)

c_adj_ab = -ab["a_positive_defined_by_minus_Kadj_AB"]
a = -c_adj_ab
# Tensor NS AA at final ladder.  Compact R22<-M22 is -b, so q_NS=-b in one local convention.
final = ten["final_tau_0p01_L260_summary"]
NS = np.array(final["NS_AA_plus_BB_compact"], dtype=float)
SN = np.array(final["SN_AA_plus_BB_compact"], dtype=float)
b_NS = -float(NS[0,0])
b_SN = -float(SN[0,0])
old_scalar_e2_entry_NS = c_adj_ab - b_NS  # P+Q at source/receiver angle e2 in NS convention

summary = {
    "step": 97,
    "purpose": "Separate the adjacent odd response into P-channel trace and Q-channel traceless pieces in A01 conventions.",
    "source_files": {
        "AB": "workspace/data/step97_ab_physical_cone_row.json",
        "tensor": "workspace/data/step97_tensor_odd_physical_map.json",
        "Step94_old_scalar": "workspace/data/step94_corrected_aabb_principal_response.json"
    },
    "AB_adjacent_P_channel": {
        "c_adj_AB": c_adj_ab,
        "a=-c_adj_AB": a,
        "map": "A_AB(M) = c_adj_AB * tr(M) I_K; Q=0",
        "trace_double_angle_matrix": ab["trace_double_angle_coordinates"]["odd_odd_matrix_[X,Y,Z]_<-[x,y,z]"],
        "physical_effect": "radial u^T A u = c_adj_AB * t_source^2; angular u_perp^T A u = 0"
    },
    "tensor_adjacent_Q_channel_odd_sector": {
        "NS_b_magnitude": b_NS,
        "SN_b_magnitude": b_SN,
        "NS_map_compact": NS.tolist(),
        "SN_map_compact": SN.tolist(),
        "NS_trace_double_angle": final["NS_AA_plus_BB_trace_double_angle"],
        "SN_trace_double_angle": final["SN_AA_plus_BB_trace_double_angle"],
        "map_description": "Trace output is zero. In local trace/double-angle coordinates, NS sends (x,y,z) to (0,-2b*y,+2b*z), SN sends (x,y,z) to (0,-2b*y,-2b*z). Thus it is a Q-channel/traceless contribution, not a P-channel trace term.",
        "physical_effect": "radial and angular components depend on relative source/receiver angles; this is the first computed angular-alignment channel. Precise q_adj phase still depends on node-frame transport conventions."
    },
    "old_scalar_entry_decomposition": {
        "R22_from_M22_total_NS_P_plus_Q": old_scalar_e2_entry_NS,
        "explanation": "The old scalar entry for e2 source and e2 receiver adds the AB P contribution c_adj_AB and the tensor Q contribution -b_NS. Treating their sum as a pure P-channel coefficient is not justified after the source-compatible map reconstruction."
    },
    "relation_to_A02_step96": {
        "agreement": "A02's determinantal framework P*xi+Q*conj(xi) is the right way to read the reduced equation; the AB rank-one trace block is a P-channel and the tensor traceless block is a Q-channel candidate.",
        "A01_correction_to_peer_wording": "The previously quoted total K_adj≈-0.03544499598 is not purely P in A01's map decomposition; c_adj_AB≈-0.03144249732 is the computed AB P-channel, while q_adj has at least the tensor odd-sector magnitude ≈0.00400249866 before full even/self/transport/remainder work."
    }
}

out = DATA_DIR / "step97_channel_summary.json"
with open(out, "w") as f:
    json.dump(summary, f, indent=2)
print(json.dumps(summary, indent=2))
print(f"Wrote {out}")
