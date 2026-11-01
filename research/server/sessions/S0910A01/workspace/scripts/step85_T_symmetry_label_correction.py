#!/usr/bin/env python3
"""
Step 85 correction to Step 84 T-symmetry data.

Step 84 incorrectly labeled the projective sign changes S0,S2 as anti-holomorphic
because it temporarily identified pairs of homogeneous coordinates with real/imag
parts.  In the degree-four del Pezzo pencil they are complex-linear projective
maps of CP^4, hence holomorphic.  They therefore do not reverse the complex
orientation of the all-same-chirality smoothing and do not obstruct the
G-equivariant KE control.
"""
import json
from pathlib import Path

old_path = Path("Sessions/S0910A01/workspace/data/step84_T_symmetry_automorphism.json")
new_path = Path("Sessions/S0910A01/workspace/data/step85_T_symmetry_label_correction.json")
old = json.loads(old_path.read_text())
new = {
    "scope": "correction to Step84 T-symmetry chirality labels",
    "preserved_from_step84": {
        "T_preserves_Q0_maxerr": old["T_preserves_Q0_maxerr"],
        "T_maps_Q1_to_Q0_minus_Q1_maxerr": old["T_maps_Q1_to_Q0_minus_Q1_maxerr"],
        "S0_preserves_Q0_Q1": [old["S0_preserves_Q0_maxerr"], old["S0_preserves_Q1_maxerr"]],
        "S2_preserves_Q0_Q1": [old["S2_preserves_Q0_maxerr"], old["S2_preserves_Q1_maxerr"]],
        "node_orbit_actions": old["node_orbit_actions"],
        "G_transitive_on_nodes": old["G_transitive_on_nodes"],
        "G_invariant_vector_field_dimension": old["G_invariant_vector_field_dimension"],
    },
    "correction": {
        "wrong_step84_statement": old.get("reason_all_same_not_G_inv"),
        "correct_statement": "S0 and S2 are complex-linear homogeneous-coordinate sign changes in CP^4, hence holomorphic projective automorphisms of each fiber. They are not anti-holomorphic on the del Pezzo surface.",
        "all_same_chirality_G_invariant": True,
        "effect_on_matched_KE_control": "The G=<T,S0,S2> equivariant all-same-chirality KE degeneration remains compatible with the algebraic complex smoothing. The verified killing of continuous holomorphic vector fields is therefore useful evidence for an equivariant Spotti/Tian control argument.",
        "effect_on_mixed_chirality": "The mixed-chirality Riemannian construction still uses the separate orientation-reversing L symmetry from Step81; it is not supplied by the complex G-equivariant del Pezzo smoothing."
    },
    "status": "Step84 numerical symmetry and automorphism-kernel results are retained; only the holomorphic/chirality interpretation of S0,S2 is corrected."
}
new_path.write_text(json.dumps(new, indent=2))
print(json.dumps(new, indent=2))
print(f"Wrote {new_path}")
