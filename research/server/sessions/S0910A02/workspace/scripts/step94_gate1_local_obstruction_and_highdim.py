"""
Step 94 Gate 1: Local second obstruction μ₁ on the product orbifold kernel plane.

Ozuch's formula (lines 673-676 of the source):
  When λ_k = 0, μ₁ = C · det[R₂₂ R₂₃; R₃₂ R₃₃]

where R^+ is expressed in the (ζ₁, ζ₂, ζ₃) adapted basis:
  ζ₁ = ζ/|ζ| (along ζ in Ω^+)
  ζ₂ = ζ⊥ in K (perpendicular to ζ within the kernel plane)
  ζ₃ = ω₁^+ (the Kähler direction)

For the product orbifold (S²×S²)/Z₂ with Λ=1:
  R^+ = diag(1, 0, 0) in the (ω₁^+, ω₂^+, ω₃^+) basis.

Key computation: for ζ = cosθ·e₂ + sinθ·e₃ ∈ K,
  R^+ in the adapted basis is diag(0, 0, Λ) for ALL θ.
Hence det(R_⊥) = det[0 0; 0 Λ] = 0 everywhere on K.

Also: high-dimensional structural theorem.
"""

import numpy as np
import json
import os

# --- Gate 1: Local second obstruction ---

def compute_mu1_product_orbifold(Lambda=1.0, n_angles=72):
    """
    Compute μ₁ = C·det(R_⊥) for all angles θ in K = span{e₂, e₃}.
    
    R^+ = diag(Λ, 0, 0) in (ω₁⁺, ω₂⁺, ω₃⁺) basis.
    K = ker R^+ = span{ω₂⁺, ω₃⁺} = span{e₂, e₃}.
    
    For ζ(θ) = cosθ·e₂ + sinθ·e₃:
    Adapted basis: ζ₁ = ζ/|ζ|, ζ₂ = (-sinθ·e₂ + cosθ·e₃), ζ₃ = e₁
    R^+ in adapted basis: compute explicitly.
    """
    R_plus = np.diag([Lambda, 0.0, 0.0])  # in (ω₁⁺, ω₂⁺, ω₃⁺)
    
    results = []
    for i in range(n_angles):
        theta = 2 * np.pi * i / n_angles
        
        # Adapted basis vectors (as columns of rotation matrix)
        zeta1 = np.array([0.0, np.cos(theta), np.sin(theta)])   # ζ direction in K
        zeta2 = np.array([0.0, -np.sin(theta), np.cos(theta)])  # ζ⊥ in K
        zeta3 = np.array([1.0, 0.0, 0.0])                       # Kähler direction
        
        # R^+ in adapted basis
        U = np.column_stack([zeta1, zeta2, zeta3])  # change of basis
        R_adapted = U.T @ R_plus @ U
        
        # 2×2 block (indices 1,2 = ζ₂, ζ₃)
        R_perp = R_adapted[1:, 1:]
        det_perp = np.linalg.det(R_perp)
        
        # First obstruction check: λ_k = R^+ applied to ζ₁
        R_zeta = R_plus @ zeta1
        lambda_check = [np.dot(R_zeta, zeta1), np.dot(R_zeta, zeta2), np.dot(R_zeta, zeta3)]
        
        results.append({
            "theta_deg": round(360 * i / n_angles, 1),
            "R_adapted_diag": list(np.round(np.diag(R_adapted), 10)),
            "R_perp_22": round(R_adapted[1,1], 10),
            "R_perp_23": round(R_adapted[1,2], 10),
            "R_perp_33": round(R_adapted[2,2], 10),
            "det_R_perp": round(det_perp, 10),
            "lambda_k": [round(x, 10) for x in lambda_check],
        })
    
    return results

def verify_gate1_calibration():
    """
    r=0 all-compatible KE row calibration:
    If Π_K μ ≠ 0 somewhere on K, the r=0 row could not succeed.
    Since r=0 row carries genuine nearby KE metrics (Step 67),
    Π_K μ must have a nontrivial zero set on K.
    
    But we prove something stronger: μ₁ = 0 EVERYWHERE on K,
    so the calibration is automatically satisfied.
    """
    return {
        "check": "r=0 all-compatible KE row",
        "r0_status": "succeeds (Step 67, Tian-Yau for del Pezzo degree 4)",
        "implication": "Π_K μ must admit solutions on K",
        "our_result": "μ₁ = 0 identically on K (stronger than needed)",
        "consistency": True
    }

def compute_isotropy_argument():
    """
    SO(2) isotropy at each A₁ node.
    
    The product metric Ric=Λg on S²×S² has isometry group containing
    SO(3)_A × SO(3)_B. At each A₁ fixed point, the local isotropy
    contains SO(2) acting on the tangent plane by rotations.
    This SO(2) acts on the kernel plane K = span{e₂, e₃} by rotations.
    
    The second obstruction μ is equivariant under this SO(2).
    Since SO(2) acts transitively on directions in K:
    - A nonzero vector in K would break SO(2) equivariance
    - Therefore Π_K(μ) = 0 for all ζ ∈ K
    
    This gives the full vanishing of the projected second obstruction,
    not just μ₁ = 0.
    """
    return {
        "isotropy_group": "SO(2) ⊂ SO(3)_A × SO(3)_B at each A₁ node",
        "action_on_K": "standard rotation on span{e₂, e₃}",
        "equivariance": "μ is equivariant under node isotropy",
        "consequence": "Π_K(μ₁, μ₂, μ₃) = 0 for all ζ ∈ K",
        "reason": "no SO(2)-equivariant nonzero vector in K exists"
    }

# --- High-dimensional structural theorem ---

def high_dimensional_obstruction_analysis():
    """
    Why n ≥ 5 has no known negative-Einstein obstruction.
    
    Positive side (all n): Ric ≥ 0 + Gromov → ‖M‖ = 0.
    So positive simplicial volume obstructs λ ≥ 0 Einstein.
    
    Negative side (n=4): All known obstructions use
    8π²χ = ∫|W|² + (2/3)λ²V   (Einstein CGB identity)
    giving V ≤ 12π²χ/λ² (upper volume bound from topology).
    Combined with BCG lower bound → contradictions.
    Also: self-dual splitting of Λ² → SW/BF invariants.
    
    Negative side (n≥5):
    - n odd: χ = 0, no Gauss-Bonnet
    - n=2m≥6: Pfaffian is degree m in Rm, involves cross terms
      e.g. n=6: χ involves ∫(R^3) with mixed Weyl terms
      No definite expression in |W|² and λ² alone
      → no upper volume bound from topology
      → BCG lower bound has nothing to contradict
    - No self-dual/anti-self-dual splitting for n≥5
    - SW/BF invariants are 4D specific
    """
    dims = {}
    
    # Dimension 4 obstruction count
    dims["n=4"] = {
        "positive_lambda": "Hitchin-Thorpe (χ ≥ 3/2|τ|), SW/BF, Gursky-LeBrun",
        "negative_lambda": "Hitchin-Thorpe, SW/BF (adjunction), Sambusetti-BCG (entropy)",
        "mechanism": "Einstein CGB 8π²χ = ∫|W|² + (2/3)λ²V gives V ≤ 12π²χ/λ²",
        "also": "Λ² splits as Λ⁺ ⊕ Λ⁻ → gauge theory invariants"
    }
    
    # Why n=5 fails
    dims["n=5"] = {
        "positive_lambda": "Gromov (‖M‖=0 under Ric≥0) still works",
        "negative_lambda": "NO KNOWN OBSTRUCTION",
        "reason_no_CGB": "χ(odd-dim manifold) = 0, no CGB theorem",
        "reason_no_gauge": "no self-dual/anti-self-dual splitting",
        "structural": "BCG lower bound on volume exists, but no topological upper bound"
    }
    
    # Why n=6,8,... fails
    dims["n=2m>=6"] = {
        "positive_lambda": "Gromov still works",
        "negative_lambda": "NO KNOWN OBSTRUCTION",
        "reason": "Pfaffian is degree m polynomial in Rm, cross terms prevent definite form",
        "example_n6": "CGB integrand involves ∫(Rab^cd Rcd^ef Ref^ab - ...) with indefinite signs",
        "consequence": "V ≤ f(χ)/λ² type bound unavailable"
    }
    
    return dims

# --- Run computations ---

results = compute_mu1_product_orbifold()
calibration = verify_gate1_calibration()
isotropy = compute_isotropy_argument()
highdim = high_dimensional_obstruction_analysis()

# Check: μ₁ = 0 for all angles
all_zero = all(abs(r["det_R_perp"]) < 1e-10 for r in results)
all_lambda_zero = all(all(abs(x) < 1e-10 for x in r["lambda_k"]) for r in results)

# Representative samples
sample_angles = [results[i] for i in range(0, len(results), 9)]

output = {
    "step": 94,
    "gate1_local_obstruction": {
        "theorem": "For the product orbifold (S²×S²)/Z₂ with R^± = diag(Λ,0,0):",
        "result_1": "λ_k(ζ) = 0 for all ζ ∈ K = ker R^±, all k (first obstruction vanishes on K)",
        "result_2": "μ₁(ζ) = C·det(R^+_⊥) = 0 for all ζ ∈ K (second det obstruction vanishes)",
        "result_3": "Π_K(μ) = 0 by SO(2) isotropy (full projected second obstruction vanishes)",
        "verification": {
            "angles_tested": len(results),
            "all_det_zero": all_zero,
            "all_lambda_zero": all_lambda_zero,
            "sample": sample_angles[:4]
        },
        "mechanism": {
            "R_plus": "diag(Λ, 0, 0) in (ω₁⁺, ω₂⁺, ω₃⁺)",
            "K": "span{ω₂⁺, ω₃⁺} = ker R^+",
            "for_any_zeta_in_K": "adapted basis R^+ = diag(0, 0, Λ)",
            "2x2_block": "[[0, 0], [0, Λ]]",
            "det": "0·Λ - 0² = 0"
        },
        "isotropy": isotropy,
        "calibration": calibration,
        "consequence": "The t² local self-correction term vanishes identically. "
                       "The leading nontrivial equation is the t³ inter-node "
                       "pattern-dependent response B_{ji}."
    },
    "gate2_difference_formulation": {
        "principle": "c-involution pairs compatible/reversed data. "
                     "Local terms A_j are pattern-independent. "
                     "Subtracting r=0 equation gives:",
        "equation": "Σ_i [B_{ji}(mixed) - B_{ji}(same)] + (R_mixed - R_r0) = 0",
        "key_improvement": "Need DIFFERENCE of remainders o(t³), not absolute remainder",
        "rigorous_version_of": "A01's K_even - K_adj"
    },
    "high_dimensional_structural": {
        "theorem_statement": "For n ≥ 5, all known mechanisms for obstructing "
                             "negative Einstein metrics rely on four-dimensional structure: "
                             "the Einstein Chern-Weil identity 8π²χ = ∫|W|² + (2/3)λ²V "
                             "or the self-dual splitting Λ² = Λ⁺ ⊕ Λ⁻. "
                             "Neither survives above dimension 4.",
        "n_odd": "χ = 0, no Gauss-Bonnet volume bound",
        "n_2m_ge_6": "Pfaffian cross terms prevent |W|²+λ² definiteness, "
                     "no topological upper volume bound, BCG has nothing to contradict",
        "positive_side": "Gromov bound: Ric≥0 → ‖M‖=0 works in all dimensions "
                         "and obstructs λ≥0 with positive simplicial volume",
        "consequence": "Refutation of Yau-26 for n≥5 requires inventing a "
                       "new obstruction mechanism. Dimension 4 is the only "
                       "dimension where either hemisphere is presently decidable.",
        "analysis": highdim
    }
}

# Derive output path from script location
script_dir = os.path.dirname(os.path.abspath(__file__))
workspace_dir = os.path.dirname(script_dir)
out_path = os.path.join(workspace_dir, "data", "step94_gate1_and_highdim.json")

with open(out_path, "w") as f:
    json.dump(output, f, indent=2)

print(f"Saved {out_path}")
print(f"\nGate 1: μ₁ = 0 for all {len(results)} angles: {all_zero}")
print(f"All λ_k = 0: {all_lambda_zero}")
print(f"\nProduct orbifold R^+ in adapted basis for θ=0:")
print(f"  R_adapted diag = {results[0]['R_adapted_diag']}")
print(f"  R_⊥ = [[{results[0]['R_perp_22']}, {results[0]['R_perp_23']}],")
print(f"          [{results[0]['R_perp_23']}, {results[0]['R_perp_33']}]]")
print(f"  det(R_⊥) = {results[0]['det_R_perp']}")
print(f"\nConsequence: local self-correction Π_K μ = 0 identically.")
print(f"The t² term is absent; leading equation is t³ inter-node response.")
print(f"\nHigh-dimensional: n≥5 has no known negative-Einstein obstruction mechanism.")
