"""
Step 48: Second-order Ozuch obstruction at the bi-Kähler locus

Verify that the second-order obstruction μ₁ also vanishes for 
directions ζ in ker R± at the (S²×S²)/ℤ₂ orbifold.

Key Ozuch formula (source lines 667-684):
When λ_k = 0 for all k (first obstruction vanishes), R± has the form
  R = [[0, 0, 0], [0, R₂₂, R₂₃], [0, R₃₂, R₃₃]]
in the frame where ζ_{(1)} = ζ/|ζ| is the first basis vector.
Then μ₁ = C · det([[R₂₂, R₂₃], [R₃₂, R₃₃]]).

For Ricci-flat orbifolds: det ≤ 0 with equality iff R⁺ = 0.
For our Λ > 0 KE orbifold: the sign is not constrained.
"""

import numpy as np
import json

Lambda = 1.0

# R_+ = R_- = diag(Lambda, 0, 0) at each A₁ point
# For bubble direction ζ = (0, ζ₂, ζ₃) in ker R:

# Frame adapted to ζ = (0, 1, 0):
# ζ_{(1)} = (0,1,0), ζ_{(2)} = (1,0,0), ζ_{(3)} = (0,0,1)
# 
# In this frame, R_+ acts as: R·e₁ = Λe₁, R·e₂ = 0, R·e₃ = 0
# So the components are:
# ⟨R·ζ_{(1)}, ζ_{(k)}⟩ = ⟨R·e₂, ζ_{(k)}⟩ = 0 for all k  ✓ (λ_k=0)
#
# Remaining block in (ζ_{(2)}, ζ_{(3)}) = (e₁, e₃) frame:
R_22 = Lambda  # ⟨R·e₁, e₁⟩
R_23 = 0.0     # ⟨R·e₁, e₃⟩ 
R_32 = 0.0     # ⟨R·e₃, e₁⟩
R_33 = 0.0     # ⟨R·e₃, e₃⟩

det_block = R_22 * R_33 - R_23 * R_32
mu_1_prop = det_block  # μ₁ = C · det

print("="*70)
print("SECOND-ORDER OZUCH OBSTRUCTION AT BI-KÄHLER LOCUS")
print("="*70)

print(f"\nFor ζ = (0,1,0) in ker R_+ = ker R_- at a product A₁ point:")
print(f"  Remaining curvature block:")
print(f"    R₂₂ = ⟨R·e₁,e₁⟩ = {R_22}")
print(f"    R₂₃ = ⟨R·e₁,e₃⟩ = {R_23}")
print(f"    R₃₂ = ⟨R·e₃,e₁⟩ = {R_32}")
print(f"    R₃₃ = ⟨R·e₃,e₃⟩ = {R_33}")
print(f"  det = {det_block}")
print(f"  μ₁ ∝ det = 0")

# Now try ζ = (0, cos θ, sin θ) for general angle
print(f"\nFor general ζ = (0, cos θ, sin θ) in ker R:")
print("  Frame: ζ_{(1)} = (0, cos θ, sin θ)")
# Choose ζ_{(2)} = (1, 0, 0), ζ_{(3)} = (0, -sin θ, cos θ)
# R·ζ_{(2)} = R·e₁ = Λe₁ = Λ ζ_{(2)}
# R·ζ_{(3)} = R·(0,-sin θ, cos θ) = 0 (since R is diag(Λ,0,0))
print("  ζ_{(2)} = (1, 0, 0), ζ_{(3)} = (0, -sin θ, cos θ)")
print(f"  R·ζ_(2) = Λ ζ_(2) → R_22 = Λ = {Lambda}")
print(f"  R·ζ_(3) = 0      → R_33 = 0, R_23 = 0")
print(f"  det = Λ · 0 - 0 · 0 = 0 for ALL angles θ")
print(f"\n  → μ₁ = 0 for ALL directions in ker R_±")

# What about the OTHER second-order obstructions μ₂, μ₃?
print("\n" + "="*70)
print("HIGHER OBSTRUCTION STRUCTURE")
print("="*70)
print("""
Ozuch's Theorem 0.13 and Corollary 2.12 give a rich structure:
- 57 first-order polynomial equations (for general orbifold/ALE)
- 84 second-order polynomial equations  
- The T⁴/ℤ₂ chessboard has 14D family satisfying ALL 84

At (S²×S²)/ℤ₂ with R = diag(Λ,0,0):
  First order: λ_k = 0 for ζ ∈ ker R (2D at each point) — VACUOUS
  Second order: μ₁ = C·det(remaining block) = 0 — ALSO VACUOUS
  
The vanishing of μ₁ is structural: R = diag(Λ,0,0) has RANK 1, 
so after removing the first row/column (which is zero in the ζ-frame),
the remaining block has one nonzero row and one zero row → det = 0.

The rank-1 structure means: BOTH first and second Ozuch obstructions
are vacuous for EH directions in the 2D kernel at each A₁ point.
This is the strongest possible first/second order permissiveness.

Comparison with the chiral argument:
- Step 42: "det R_± = 0" at KE points → first order vacuous
- Step 47: "R_±·ζ = 0 is vectorial" → first order correctly stated  
- Step 48: ALSO μ₁ = 0 → second order ALSO vacuous
- The rank-1 property of R = diag(Λ,0,0) cascades through both orders

What remains unknown:
1. Higher-order (third, fourth...) Ozuch obstructions
2. The linearized operator L invertibility modulo obstructions
3. Whether Corollary 2.12 (linking first and second variations) 
   gives additional constraints at this specific orbifold
4. The actual gluing-perturbation existence theorem for Λ > 0 
   curved orbifolds (Ozuch's proofs use flat T⁴/ℤ₂)
""")

# Save
results = {
    "purpose": "Second-order Ozuch obstruction at bi-Kähler locus",
    "curvature_block": "R_± = diag(Λ, 0, 0), rank 1",
    "first_order": {
        "status": "VACUOUS for ζ ∈ ker R (2D)",
        "reason": "R·ζ = 0 by definition of kernel"
    },
    "second_order": {
        "mu_1": 0,
        "det_remaining_block": 0,
        "status": "VACUOUS for all ζ ∈ ker R",
        "reason": "rank-1 R gives one zero row in remaining block → det = 0",
        "angle_independent": True
    },
    "implication": "Bi-Kähler (S²×S²)/ℤ₂ is first AND second order unobstructed for EH bubbles in the 2D kernel direction",
    "comparison_T4_Z2": "T⁴/ℤ₂ with R=0 is fully unobstructed through order 2; here R≠0 but rank 1 still kills order-2 obstruction for kernel directions"
}

output = "Sessions/S0910A02/workspace/data/step48_second_order_obstruction.json"
with open(output, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {output}")
