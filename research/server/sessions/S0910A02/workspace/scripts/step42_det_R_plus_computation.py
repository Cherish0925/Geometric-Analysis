#!/usr/bin/env python3
"""Step 42 Part 2: det R_+ computation for key positive Einstein 4-manifolds/orbifolds.

Determines where the Ozuch obstruction (det R = 0) is satisfied vs violated,
mapping the reach of Route A.
"""

import json
import numpy as np
import os

results = {}

# =============================================================================
# The curvature operator decomposition for Einstein 4-manifolds
# =============================================================================
# For Ric = Lambda*g, the curvature operator on Lambda^2_+ is:
#   R_+ = W_+ + (s/12)*Id = W_+ + (Lambda/3)*Id
# where s = 4*Lambda is the scalar curvature.
#
# The Weyl tensor W_+ is traceless (tr W_+ = 0), so if its eigenvalues are
# w1, w2, w3 with w1+w2+w3 = 0, then:
#   R_+ has eigenvalues w_i + Lambda/3
#   det R_+ = prod_i (w_i + Lambda/3)

Lambda = 1  # normalize

# --- Case 1: Round S^4 ---
# Conformally flat: W = 0
w_S4 = [0, 0, 0]
R_plus_S4 = [w + Lambda/3 for w in w_S4]
det_R_S4 = np.prod(R_plus_S4)
results["S4_round"] = {
    "manifold": "S^4 (round)",
    "W_plus_eigenvalues": w_S4,
    "R_plus_eigenvalues": R_plus_S4,
    "det_R_plus": round(det_R_S4, 10),
    "det_nonzero": det_R_S4 != 0,
    "consequence": "NO EH desingularization possible near round geometry. Noncollapsed near-Einstein on S^4 converges smoothly."
}

# --- Case 2: CP^2 (Fubini-Study) ---
# Kähler-Einstein: W_+ = diag(2Lambda/3, -Lambda/3, -Lambda/3) in the (omega, Sigma_+) basis
w_CP2 = [2*Lambda/3, -Lambda/3, -Lambda/3]
R_plus_CP2 = [w + Lambda/3 for w in w_CP2]
det_R_CP2 = np.prod(R_plus_CP2)
results["CP2"] = {
    "manifold": "CP^2 (Fubini-Study)",
    "W_plus_eigenvalues": [round(w, 6) for w in w_CP2],
    "R_plus_eigenvalues": [round(r, 6) for r in R_plus_CP2],
    "det_R_plus": round(det_R_CP2, 10),
    "det_nonzero": abs(det_R_CP2) > 1e-12,
    "kernel_dimension": 2,
    "consequence": "det R_+ = 0, kernel is 2-dimensional (Lambda^2_+,0 space). EH desingularization possible."
}

# --- Case 3: S^2 x S^2 (product) ---
# The product metric has W_+ eigenvalues (2Lambda/3, -Lambda/3, -Lambda/3) (same as CP^2!)
# This is because both are self-dual Einstein 4-manifolds with the same Weyl invariants at this level.
w_S2S2 = [2*Lambda/3, -Lambda/3, -Lambda/3]
R_plus_S2S2 = [w + Lambda/3 for w in w_S2S2]
det_R_S2S2 = np.prod(R_plus_S2S2)
results["S2xS2"] = {
    "manifold": "S^2 x S^2 (product Einstein)",
    "W_plus_eigenvalues": [round(w, 6) for w in w_S2S2],
    "R_plus_eigenvalues": [round(r, 6) for r in R_plus_S2S2],
    "det_R_plus": round(det_R_S2S2, 10),
    "det_nonzero": abs(det_R_S2S2) > 1e-12,
    "kernel_dimension": 2,
    "consequence": "det R_+ = 0. This is consistent: S^2 x S^2 orbifolds CAN be desingularized (and S^2 x S^2 itself IS Einstein)."
}

# --- Case 4: General Kähler-Einstein surface ---
# For ANY Kähler-Einstein 4-manifold with Ric = Lambda*g:
# The Kähler form omega spans a 1D subspace of Lambda^2_+.
# W_+ omega = (s/6) omega = (2Lambda/3) omega
# W_+|_{Lambda^2_+,0} = -(s/12) Id = -(Lambda/3) Id on the 2D complement
# Therefore: R_+ = diag(Lambda, 0, 0) and det R_+ = 0 ALWAYS.
results["general_KE"] = {
    "manifold": "Any Kähler-Einstein 4-manifold (Ric = Lambda*g)",
    "W_plus_eigenvalues": ["2Lambda/3", "-Lambda/3", "-Lambda/3"],
    "R_plus_eigenvalues": ["Lambda", "0", "0"],
    "det_R_plus": 0.0,
    "det_nonzero": False,
    "consequence": "det R_+ = 0 for ALL positive Kähler-Einstein surfaces. This includes CP^2, S^2xS^2, toric KE dP_3-dP_8.",
    "universal_statement": "The Ozuch obstruction is ALWAYS satisfied for KE orbifolds — they can always be desingularized in principle."
}

# --- Case 5: Round S^4/Gamma quotients ---
# Quotients of S^4 inherit the same curvature: W = 0, det R_+ = (Lambda/3)^3 > 0
results["S4_quotient"] = {
    "manifold": "S^4/Gamma (quotient of round sphere)",
    "W_plus_eigenvalues": [0, 0, 0],
    "R_plus_eigenvalues": [Lambda/3, Lambda/3, Lambda/3],
    "det_R_plus": round((Lambda/3)**3, 10),
    "det_nonzero": True,
    "consequence": "det R_+ != 0 at EVERY point. No desingularization by EH. Noncollapsed sequences converging to S^4/Gamma must be smooth."
}

# --- Case 6: Negative Einstein (Lambda < 0) ---
# For Lambda < 0: R_+ = W_+ + Lambda/3 * Id
# For hyperbolic orbifold (conformally flat): W = 0, R_+ = (Lambda/3)Id with Lambda < 0
# det R_+ = (Lambda/3)^3 < 0, so det R_+ != 0
results["hyperbolic"] = {
    "manifold": "Hyperbolic orbifold (constant negative curvature)",
    "W_plus_eigenvalues": [0, 0, 0],
    "R_plus_eigenvalues": ["Lambda/3 < 0", "Lambda/3 < 0", "Lambda/3 < 0"],
    "det_R_plus": "nonzero (negative)",
    "det_nonzero": True,
    "consequence": "Hyperbolic orbifolds cannot be desingularized. This is consistent with hyperbolic rigidity."
}

# =============================================================================
# Summary: Route A reach
# =============================================================================

route_A_reach = {
    "obstruction_effective": {
        "S4_and_quotients": "det R_+ = (Lambda/3)^3 > 0: Route A gives smooth convergence",
        "hyperbolic": "det R_+ != 0: no desingularization (but this is negative sign, not our case)"
    },
    "obstruction_trivial": {
        "all_KE_surfaces": "det R_+ = 0 always: obstruction satisfied, desingularization possible in principle",
        "includes": ["CP^2", "S^2 x S^2", "Page (if conformally Kähler orbifold limit)", "CLW", "toric KE dP_3-dP_8"]
    },
    "implication_for_route_A": {
        "strong_case": "If the GH limit of a noncollapsed near-Einstein sequence is close to a ROUND orbifold (S^4/Gamma type), Route A gives Einstein existence via smooth convergence.",
        "weak_case": "If the GH limit has KE-type singular points, det R_+ = 0 is automatically satisfied and the obstruction is not effective. Further analysis (second-order, topology, LeBrun-Ozuch classification) is needed.",
        "summary": "Route A eliminates the 'near-round' degeneration scenario but does not address the KE orbifold scenario without additional input."
    },
    "connection_to_stress_family": {
        "#_k(S2xS2)": {
            "noncollapsed_limit_candidates": [
                "S^4/Gamma (near-round): excluded by det R_+ != 0 -> limit must be smooth -> Einstein on M",
                "KE orbifold: det R_+ = 0, not excluded by first obstruction",
                "But LeBrun-Ozuch (conditional on Hermitian/admissible): b_+ >= 2 excluded from Del Pezzo classification",
                "So: EITHER the limit is smooth (Einstein exists on M) OR the limit has non-Hermitian singularities"
            ],
            "gap": "The gap is: can noncollapsed near-Einstein metrics on #_k(S^2xS^2) degenerate to a NON-Hermitian orbifold with Z_2 singularities and det R_+ = 0?"
        }
    }
}
results["route_A_reach"] = route_A_reach

# Save
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(script_dir)  # workspace
output_path = os.path.join(workspace_dir, "data", "step42_det_R_plus_computation.json")
with open(output_path, 'w') as f:
    json.dump(results, f, indent=2, default=str)
print(f"Saved to {output_path}")

# Print summary
print("\n=== det R_+ COMPUTATION SUMMARY ===")
for key, val in results.items():
    if isinstance(val, dict) and 'manifold' in val:
        print(f"\n  {val['manifold']}:")
        print(f"    W_+ eigenvalues: {val['W_plus_eigenvalues']}")
        print(f"    R_+ eigenvalues: {val['R_plus_eigenvalues']}")
        print(f"    det R_+: {val['det_R_plus']}")
        print(f"    Nonzero: {val['det_nonzero']}")
        print(f"    => {val['consequence']}")

print("\n=== ROUTE A REACH ===")
print("  STRONG: Near-round orbifold limits -> det R_+ != 0 -> smooth convergence -> Einstein exists")
print("  WEAK: KE orbifold limits -> det R_+ = 0 always -> first obstruction trivial")
print("  GAP: Can #_k(S^2xS^2) degenerate to non-Hermitian orbifold with Z_2 and det R_+ = 0?")
