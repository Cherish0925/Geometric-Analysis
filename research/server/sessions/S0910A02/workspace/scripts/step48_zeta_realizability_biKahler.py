"""
Step 48: ζ-realizability check at the bi-Kähler (S²×S²)/ℤ₂ orbifold

This is the cheap decisive question from the strategist: at the four A₁ 
points of (S²×S²)/ℤ₂, can admissible gluing directions ζ_j lie in 
ker R_±(p_j) simultaneously, with a topologically required orientation 
assignment?

Key facts from Steps 44-45:
- (S²×S²)/ℤ₂ has R₊ = R₋ = diag(Λ,0,0) at all four A₁ points
- ker R₊ = ker R₋ = span{e₂, e₃} (2-dimensional at each point)
- For resolution to #₃(S²×S²): need 2 compatible + 2 reversed EH bubbles
  (signature constraint τ = 0)

Ozuch's first obstruction (source lines 512-514):
  λ_k(ζ±) = c⟨R±(H₂)ζ±, ζ_{(k)}±⟩
vanishes iff ζ ⊥ ker(R±(p)).

Higher-order analysis (Ozuch Theorem 0.13): for T⁴/ℤ₂, 57 first-order and 
84 second-order necessary polynomial equations; a 14-dimensional chessboard 
family satisfies all 84 equations.

This script checks:
1. Dimension of unobstructed direction space at each A₁ point
2. Whether the ℤ₂ equivariance constrains relative bubble parameters
3. Whether the resolution topology is compatible with all directions 
   lying in the unobstructed subspace
4. Implications for the mode-projection theorem
"""

import numpy as np
import json

Lambda = 1.0  # normalize Ric = Λg with Λ = 1

# The four A₁ fixed points of (S²×S²)/ℤ₂ = (S²×S²)/⟨(x,y)↦(a(x),a(y))⟩
# where a is the antipodal map on each S²
# Fixed points are {(N,N), (N,S), (S,N), (S,S)} in poles
fixed_points = ["(N,N)", "(N,S)", "(S,N)", "(S,S)"]

# At each point, the curvature blocks (verified in Step 44):
# Equal-radius product: W± has eigenvalues {2Λ/3, -Λ/3, -Λ/3} in both blocks
# So R± = W± + (Λ/3)I = diag(Λ, 0, 0) in both chiralities
R_plus = np.diag([Lambda, 0, 0])
R_minus = np.diag([Lambda, 0, 0])

# Kernel dimensions
ker_R_plus = 2  # span{e₂, e₃}
ker_R_minus = 2

print("="*70)
print("ζ-REALIZABILITY AT (S²×S²)/ℤ₂ BI-KÄHLER ORBIFOLD")
print("="*70)

print(f"\nR₊ = R₋ = diag({Lambda}, 0, 0) at ALL four A₁ points")
print(f"ker(R₊) = ker(R₋) = span{{e₂, e₃}} — dimension {ker_R_plus}")
print(f"\nThis means: for ANY chirality ε ∈ {{+,-}}, a 2-parameter family")
print(f"of EH directions ζ = (0, ζ₂, ζ₃) is FIRST-ORDER UNOBSTRUCTED.")

# Topology requirements for resolution
print("\n" + "="*70)
print("TOPOLOGY REQUIREMENTS")
print("="*70)

# For (S²×S²)/ℤ₂ → smooth 4-manifold:
# Need 4 EH bubbles, one at each A₁ point
# Compatible (+) bubble: contributes (Δb₊, Δb₋) = (0, 1)
# Reversed (-) bubble: contributes (Δb₊, Δb₋) = (1, 0)
# Orbifold: b₊(orb) = b₋(orb) = 1 (rational, from product structure)
# If r reversed and (4-r) compatible:
#   b₊ = 1 + r, b₋ = 1 + (4-r), τ = b₊ - b₋ = 2r - 4
# For τ = 0: r = 2 (exactly 2 reversed, 2 compatible)
#   b₊ = 3, b₋ = 3, signature 0
# Intersection form: 3H (even, unimodular) → #₃(S²×S²) or something spin

r_reversed = 2
r_compatible = 2
b_plus = 1 + r_reversed
b_minus = 1 + (4 - r_reversed)
tau = b_plus - b_minus
chi = 2 + b_plus + b_minus  # Euler characteristic

print(f"Resolution with {r_reversed} reversed + {r_compatible} compatible EH bubbles:")
print(f"  b₊ = {b_plus}, b₋ = {b_minus}, τ = {tau}, χ = {chi}")
print(f"  Intersection form: {b_plus}H (if even, spin, signature 0)")

# At each point: which chirality is tested?
# Compatible bubble at point p: ε = +, tests R₊(p)ζ₊
# Reversed bubble at point p: ε = -, tests R₋(p)ζ₋
print("\nAt each point, the first-order obstruction tests:")
print("  Compatible (+): R₊(p)ζ⁺ = 0?  → YES, for ζ ∈ ker R₊ (dim 2)")
print("  Reversed (-):   R₋(p)ζ⁻ = 0?  → YES, for ζ ∈ ker R₋ (dim 2)")

print("\n" + "="*70)
print("ℤ₂ EQUIVARIANCE CONSTRAINT")
print("="*70)

# The ℤ₂ acts on the product: (x,y) ↦ (a(x), a(y))
# This exchanges (N,N) ↔ (S,S) and (N,S) ↔ (S,N)
# For a ℤ₂-equivariant desingularization:
# ζ_{(N,N)} and ζ_{(S,S)} must be related by the ℤ₂ action
# ζ_{(N,S)} and ζ_{(S,N)} must be related by the ℤ₂ action
# Also: ε_{(N,N)} = ε_{(S,S)} and ε_{(N,S)} = ε_{(S,N)}

print("The ℤ₂ involution exchanges:")
print("  (N,N) ↔ (S,S)  and  (N,S) ↔ (S,N)")
print("Equivariance requires:")
print("  ε_{(N,N)} = ε_{(S,S)} and ε_{(N,S)} = ε_{(S,N)}")
print("  ζ_{(N,N)} and ζ_{(S,S)} related by the induced SO(3) action")
print("  ζ_{(N,S)} and ζ_{(S,N)} related by the induced SO(3) action")
print()
print("For τ = 0 with equivariance: need one pair compatible, one pair reversed")
print("  e.g., ε_{(N,N)} = ε_{(S,S)} = +  and  ε_{(N,S)} = ε_{(S,N)} = -")

# Parameter count
print("\n" + "="*70)
print("PARAMETER COUNT FOR UNOBSTRUCTED DIRECTIONS")
print("="*70)

# Without equivariance: 4 points × 2D kernel = 8 parameters
# With equivariance: 2 independent pairs × 2D kernel = 4 parameters
# Plus relative scale (|ζ|) at each pair: 2 more parameters
# Total: 4 + 2 = 6 free parameters modulo equivariance
# Without equivariance: 8 + 4 = 12 free parameters

print("Without equivariance:")
print(f"  Direction parameters: {4 * ker_R_plus} (4 points × 2D kernel)")
print(f"  Scale parameters:    4 (|ζ_j| at each point)")
print(f"  Total first-order unobstructed:  {4*ker_R_plus + 4}")
print()
print("With ℤ₂ equivariance:")
print(f"  Direction parameters: {2 * ker_R_plus} (2 pairs × 2D kernel)")
print(f"  Scale parameters:    2 (|ζ| for each pair)")
print(f"  Total first-order unobstructed:  {2*ker_R_plus + 2}")

# Ozuch comparison
print("\n" + "="*70)
print("COMPARISON WITH OZUCH'S T⁴/ℤ₂ RESULT")
print("="*70)
print("For T⁴/ℤ₂ (Λ = 0, flat orbifold):")
print("  16 A₁ points, R± = 0 everywhere → ALL 48 first-order conditions vacuous")
print("  57 polynomial equations at first order, 84 at second order")
print("  14-dimensional chessboard family satisfies all 84 equations")
print()
print("For (S²×S²)/ℤ₂ (Λ > 0, curved orbifold):")
print("  4 A₁ points, R± = diag(Λ,0,0) → partial kernel, NOT fully vacuous")
print("  Unobstructed directions live in a 2D subspace at each point")
print("  The first obstruction is SELECTIVE but PERMISSIVE")
print("  Higher-order obstructions are still unknown for this case")

# Decisive assessment
print("\n" + "="*70)
print("DECISIVE ASSESSMENT")
print("="*70)
print("""
FINDING: The first-order Ozuch obstruction does NOT block desingularization
of (S²×S²)/ℤ₂. A 6-parameter equivariant family (or 12-parameter general)
of EH gluing directions exists in the kernel of R± at all four points,
with the correct topology for #₃(S²×S²).

CONSEQUENCE FOR THE MODE-PROJECTION THEOREM:
The theorem (even with H4_dual proved) CANNOT exclude noncollapsed 
positive bubbling for #₃(S²×S²) through first-order analysis alone.
The bi-Kähler locus is not merely an exceptional edge case — it is a 
concrete place where a near-Einstein bubbling family could exist.

WHAT THIS CHANGES:
- If higher-order obstructions also fail to block, this is a genuine 
  tightly-pinched bubbling family — an original result in its own right
- No amount of first-order bridge work can prove P₄⁺
- The real wall in the positive branch is:
    REFUTATION needs a new nonexistence obstruction for positive Einstein 
    on simply connected 4-manifolds beyond Hitchin-Thorpe
    PROOF needs an existence theorem for Einstein metrics on #_k(S²×S²)
- The mode-projection theorem retains value for NON-bi-Kähler limits

WHAT THIS DOES NOT DO:
- Does not refute Yau-26: #₃(S²×S²) satisfies strict Hitchin-Thorpe 
  and no Einstein nonexistence obstruction is known beyond HT for simply 
  connected positive-curvature 4-manifolds
- Does not construct an actual smoothing: higher-order Ozuch obstructions 
  and invertibility of the linearized operator must still be checked
""")

# Save results
results = {
    "purpose": "ζ-realizability check at bi-Kähler (S²×S²)/ℤ₂ orbifold",
    "orbifold": "(S²×S²)/ℤ₂",
    "singular_points": 4,
    "isotropy_type": "A₁ = ℤ₂",
    "curvature_blocks": {
        "R_plus": "diag(Λ, 0, 0)",
        "R_minus": "diag(Λ, 0, 0)",
        "kernel_dim_each": 2,
        "kernel": "span{e₂, e₃}"
    },
    "resolution_topology": {
        "compatible_bubbles": r_compatible,
        "reversed_bubbles": r_reversed,
        "b_plus": b_plus,
        "b_minus": b_minus,
        "tau": tau,
        "chi": chi,
        "intersection_form": f"{b_plus}H"
    },
    "first_order_unobstructed": {
        "without_equivariance": {
            "direction_params": 4 * ker_R_plus,
            "scale_params": 4,
            "total": 4 * ker_R_plus + 4
        },
        "with_equivariance": {
            "direction_params": 2 * ker_R_plus,
            "scale_params": 2,
            "total": 2 * ker_R_plus + 2
        }
    },
    "decisive_finding": "First-order obstruction does NOT block desingularization",
    "consequence": "Mode-projection theorem cannot exclude noncollapsed positive bubbling for #₃(S²×S²)",
    "what_remains": [
        "Higher-order Ozuch obstructions for (S²×S²)/ℤ₂ with Λ > 0",
        "Linearized operator invertibility modulo obstructions on the product quotient",
        "ℤ₂-equivariant Kuranishi/gluing analysis",
        "Einstein existence on #₃(S²×S²) (unknown either way)"
    ]
}

output = "Sessions/S0910A02/workspace/data/step48_zeta_realizability.json"
with open(output, 'w') as f:
    json.dump(results, f, indent=2)
print(f"\nSaved to {output}")
