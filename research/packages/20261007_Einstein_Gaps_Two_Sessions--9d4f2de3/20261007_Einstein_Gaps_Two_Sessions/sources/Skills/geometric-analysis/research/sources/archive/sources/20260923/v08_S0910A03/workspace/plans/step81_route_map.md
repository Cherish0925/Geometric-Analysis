# Step 81 route map: the collapse mechanism and what it leaves open

## Current mathematical position

The negative graph-manifold route has three solved components:
1. **All-Einstein exclusion** (Di Cerbo): certain extended graph 4-manifolds admit no Einstein metric.
2. **Expanding tail** (Step 73): order-one orbit anisotropy can be flattened at defect O(K⁻¹+e⁻²ʳ⁰).
3. **VII₀ barrier** (Steps 78, 81): rigorous finite-distance collapse for all z-independent reflected centers.

The missing component is a **finite connector** from a reflected center to the tail interface.

## What Step 81 established

1. **Exact S'(0) spectrum**: {-3, 3±√(3(k²+12))} for the rotating-loop family.
2. **Angular-slip preserves only energy trace**: orbit Ricci changes at O(ε).
3. **Volume-weighted ⟨u'(0)⟩_ρ = -3 universally**: independent of area profile.
4. **VII₀ collapse is rigorous**: finite-time blowup for all winding numbers.
5. **Collapse does NOT generalize to z-dependent OT**: the orbit equation has flux redistribution.

## Decisive open question

Does the full coupled (γ_B, σ, M) system on the first O(1) physical layer
(r ∈ [0, 0.5]) admit a reflected approximately-Einstein solution with:
- Vanishing full Ricci defect ||E||_∞ → 0
- All five Einstein components controlled
- Exit data compatible with Step 73 tail

The VII₀ barrier eliminates the simplest ansatz but leaves genuinely
z-dependent matrix transport unexplored. The orbit equation
div(ρ M⁻¹∇M) = 0 has flux-redistribution freedom that could potentially
avoid the scalar monotone cascade.

## Three candidate next investigations (ranked by value)

### A. Monotone quantity for the full OT system (highest value)
Search for a weighted scalar or matrix functional on the coupled (γ_B, σ, M)
system that inherits the VII₀ positive-feedback mechanism. If found, this
would close the full OT class and strengthen the O(1) defect lower bound
from VII₀ to all T²-invariant reflected connectors.

Natural candidates:
- The convex distance integral F = ∫ ρ d²_{H²}(U, P) dz
- The total orbit energy ∫ ρ e_{H²} dz
- The Noether current Q(r) = ∫ ρ M⁻¹M_r dz (= 0 for exact, forced for approximate)

### B. z-dependent finite-mode connector construction (complementary)
Build the full reflected inner-layer system with mode coupling:
- Rotating loop d=d*, θ=kz as base
- Angular-slip perturbation at modes q < k
- All zero-mode and 2q backreaction in σ and γ_B
- Free outgoing data on inner domain [0, 0.6]

This tests whether spatial redistribution can overcome the VII₀ barrier
computationally before attempting the analytical obstruction.

### C. Non-reflected metrics (alternative escape)
Metrics with S(0) ≠ 0 are not covered by the universal -3 result.
If H(0) > 0 (initially expanding slices), the collapse cascade doesn't start.
This changes the problem from a reflected BVP to a Cauchy problem with
prescribed initial data—genuinely different from all current work.

## Positive branch status

A02's three-leg audit (λ>0, λ=0, λ<0) correctly identifies that:
- λ>0: alignment mechanism with theta_max=1/2 needs A≥24
- λ=0: special holonomy excluded on chi=8 rows, generic SO(4) open
- λ<0: no current tool; alignment vacuous for s≤0

A01's chirality Green response found a live low-eigenvalue channel (corrected
in #583) but not the full c_opp-c_same coefficient. The near-pinched A1
construction (A02 #584) gives ||Ric-σg||_op ≤ C/|log a| but is only a
positive-input construction, not Einstein existence or nonexistence.

## Files

- `workspace/notes/step81_collapse_and_contraction.md`
- `workspace/data/step81_geodesic_loop_center.json`
- `workspace/data/step81_evolution.json`
- `workspace/data/step81_contraction_analysis.json`
- `trace/ttcs/results/step81_ttcs01_verifier1_integration.md`
