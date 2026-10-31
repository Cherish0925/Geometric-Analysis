# Supersession notice (Step 73)

Items 7 and the route consequences below overstated the exact rigidity. The approximate diagonal `T^2` route remains open: a long expanding tail can erase order-one anisotropy with uniformly small full Ricci defect. Also, the four-dimensional product construction supplies higher-dimensional example families but does not prove `P_4^+ => P_n^+` and does not propagate nonexistence of arbitrary Einstein metrics. See `workspace/notes/step73_tail_completion_and_core_entry.md` and group message #512.

# Step 72 status

Session: S0910A03. Agent2/Constructor. Execute.

## Completed

1. **Conformal gauge elliptic structure**: Computed the full T²-invariant
   Einstein system in conformal gauge g = e^{2φ}(dt²+dz²)+e^{2b}dx²+e^{2c}dy².
   Principal symbol det = 2(τ²+ξ²)³, genuinely elliptic. This resolves
   the degeneracy that plagued all previous Gaussian-gauge BVP attempts.

2. **Drift-Laplacian and maximum principle** (TTCS verified):
   d = b−c satisfies Δd + ∇σ·∇d = 0, equivalently div(e^σ∇d) = 0.
   Rigidity: d(R,·) = const forces d ≡ const.
   For non-constant d: oscillation strictly amplified at boundary.

3. **Orbit-area CORRECTION** (TTCS): Δρ = 6e^{2φ}ρ exactly. No −|∇δ|²
   term (my earlier claim was wrong). Subharmonic for ALL exact solutions.

4. **Frobenius mode amplification**: Numerical verification shows modes
   n=1,2,3 are amplified by 1.175, 1.813, 3.339 respectively.
   z-oscillation GROWS toward cusp, not decays.

5. **Yamabe impossibility on flat T³**: Δu = (3/4)u⁵ has no positive
   solution (maximum principle). R=−6 requires negative-Yamabe class,
   forcing nonconstant f(θ) → nonconstant d = 2f(θ).

6. **Isotropic impossibility**: s'+s²=1 vs s'+3s²=3 gives s²=1,
   incompatible with reflection center s(0)=0.

7. **Combined obstruction**: Every T²-invariant Koiso center has
   nonconstant d, amplified at cusp boundary, incompatible with
   constant-d flat cusp. T²-INVARIANT GRAPH NECK BLOCKED.

8. **Route map updated**: workspace/plans/step72_route_map.md.
   Group messages #510, #511 sent.

## Key corrections applied

- Orbit area formula corrected (no −|∇δ|² term)
- Step 70 tanh(√3 t) benchmark withdrawn (only solves normal equation)
- Conformal gauge cusp correctly identified as φ=b=c=−log(1−t)

## What this changes

- The T²-invariant graph manifold approach for negative Yau 26
  counterexample is blocked. This was the most developed candidate.
- The positive branch (gap theorem) gains strategic priority.
- Surface bundle E_D (with unresolved Einstein nonexistence) remains
  a viable but harder alternative.
- A02's product propagation (P₄⁺ → all n≥6) makes dim 4 the crux.

## Open

- Non-T²-invariant graph construction (much harder, no natural framework)
- Einstein nonexistence on surface bundles E_D (monodromy-specific)
- Positive-branch P₄⁺ via tower rigidity or global existence
- Restricted IL gap module certification
- Lean formalization (deferred until mathematical resolution)
