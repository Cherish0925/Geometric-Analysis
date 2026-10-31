# Route assessment after Step 23 (superseded by Step 24 support-local correction)

> **Step 24 correction.** The dissipation-locality observation remains valid. The maximal-net covering repair is conditional only: it assumes all centers in the net have small critical product, which the selected maximal-function good-support construction does not provide. Use `workspace/notes/step24_buffered_support_energy_test.md` for the current selected-support route.

## Main advance

The structural gap from Step 22 — passage from summed absorption to
componentwise energy control — is resolved by two findings:

1. **Dissipation locality (ε = 0).** The exact tensor inequality for the
   normalized cutoff flow ∂_t g = -2χ²(Ric+g) produces no neighbor
   dissipation coupling. The Sobolev variable v = η_α χ F has compact
   support in U_α, so its gradient decomposes into D_{2,α} plus
   r⁻² H-type localization within U_α. TTCS independently confirmed
   this for all five geometric variation terms (inverse metric, measure,
   Hessian-a, normalization, localization).

2. **Covering subordination.** The old ball family (centers 10r, supports
   B_{5r}) did NOT satisfy ∫_{U_α} F² ≤ C Σ H_{2,β}: the annulus
   B_{5r}\B_{4r} was uncovered. The fix: use a maximal r-net, giving
   Σ η_β² ≥ 1 everywhere and hence ∫_{U_α} F² ≤ Σ_{β~α} H_{2,β}.

Together: the componentwise vector inequality is

   S' + cZ ≤ (b/r²) B S,    no εBZ term

with B having bounded row sums L = N C_A⁴. Standard cooperative comparison:

   S_α(t) ≤ e^{bLθ} Γ(0)²,   ∫₀ᵀ Z_α ≤ C Γ(0)²

Both independent of the number of components.

## Nash refutation (A03 #304)

A03's Hardy-potential counterexample (V = κ/|x|² in R⁴, κ < 1) refutes
the abstract Nash L²→L^∞ shortcut: heat kernel has r^{-σ} singularity.
Consequence: the explicit finite-exponent route (q=2 → parabolic Sobolev
→ q=3 → Moser) is ESSENTIAL for the critical H₂→H₃ upgrade. Once H₃ is
available (subcritical, p=3 > n/2=2), standard Moser with convergent
constants closes.

## What is now established (conditional on exact tensor inequality)

1. Componentwise energy persistence: S_α(T) ≤ C Γ(0)²
2. Componentwise integrated dissipation: ∫₀ᵀ Z_α ≤ C Γ(0)²
3. Cubic potential: A⁴ H₃(t) ≤ C Γ³/t on [T/2, T]
4. Unweighted Q: cooperative triangular, Q(T)/A → 0
5. Fixed J₆: cooperative persistence, J₆(T) ≤ C J₆(0)
6. Covering subordination: maximal r-net closes the geometry

## What remains

**(T1) Exact tensor inequality.** The schematic derivation from Step 20
must be made precise with all coefficients. The structural feature (ε=0)
is forced by the support geometry and does not depend on the coefficients.

**(T2) Critical H₂→H₃ step.** The single load-bearing PDE task:
  - q=2 energy + parabolic Sobolev → spacetime L³
  - q=3 with time cutoff → time-uniform spatial H₃
  This is Stage 1 of the two-stage architecture.

**(T3) Weighted Moser endpoint.** Stage 2: from H₃ (subcritical),
A03's q→3q/2 product gives |aRm| ≤ CΓ/t.

**(T4) First-exit loop closure.** Metric comparability, Sobolev
persistence, and the self-improvement of Γ(t) ≤ Γ* on [0, θr²].

**(T5) Plateau connection.** Bounded curvature on plateau buffers at
positive time + exponential-pullback averaging → controlled local
geometry → calibrated Derdziński contradiction.

**(T6) Full joint density.** Monopole limit + eigenline saturation
for the self-dual Weyl spectrum, not just |W⁺| modulus.

## Positive branch and higher dimensions

A02 #303: KK construction shows codimension-1 positive collapse is
Einstein-compatible in n ≥ 5 (L(q,1)×Nᵈ, Ric = g, fiber t→0).
Only n = 4 has the Bochner obstruction (Ric_{S¹} = g impossible).
This means P₄⁺ remains the sharp test; n ≥ 5 positive branch may
actually fail (counterexamples possible).

## Scope

Even if T1-T6 are proved, the result covers only the critical 4D
negative Ishida-LeBrun laboratory. Positive branch, arbitrary 4D
no-Einstein manifolds, n ≥ 5, the full Yau 26 proposition, and
Lean formalization remain open.

## Files

- Theorem note: `workspace/notes/step23_cooperative_persistence_theorem.md`
- Cooperative verification: `workspace/scripts/step23_cooperative_persistence.py`
- Covering verification: `workspace/scripts/step23_corrected_covering.py`
- TTCS: `trace/ttcs/results/step23_ttcs01_verifier1_integration.md`
- Parent: `workspace/notes/step22_current_energy_formulation.md`
