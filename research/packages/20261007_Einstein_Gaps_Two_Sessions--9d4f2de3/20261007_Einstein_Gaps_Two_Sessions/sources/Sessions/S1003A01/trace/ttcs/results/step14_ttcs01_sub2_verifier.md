# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md",
    "Sessions/S1003A01/workspace/scripts/neutral_mode_resistance.py",
    "Sessions/S1003A01/workspace/data/perp_collar/neutral_mode_resistance.json",
    "Sessions/S1003A01/workspace/data/pair_profile/exterior_budget_X8.json",
    "Sessions/S1003A01/workspace/data/perp_collar/rigorous_continued_X16_to_X32_J_d12.json",
    "Sessions/S1003A01/workspace/data/perp_collar/rigorous_continued_X32_to_X64_J_d16.json",
    "Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md"
  ]
}
```

## Task

Independently examine the Step-14 mathematical synthesis. Check especially: (i) the frozen-core cluster saving inequality and its interpretation at overlap depth w=1.6; (ii) whether the exact one-dimensional minimization for A_T(q)=∫_0^T e^{4t}(q''+4q')^2 with clamped endpoint data really tends to 64 Delta^2; (iii) whether that reduced result justifies only a conditional route to diagonal coercivity rather than a lower bound for the full cell problem; and (iv) what the new rigorous X=32 and X=64 cell enclosures establish. Identify any mathematical or interpretive correction that should be made, and state the strongest sound implication for the Einstein-gap programme.

## Output

# Verification memo: Step-14 synthesis (cluster budget, neutral-mode resistance, large-collar enclosures)

## Summary

- **Correct as stated:**
  - the cluster inequality (2.1);
  - the closed-form solution of the reduced problem (6.1), including the limit 64Δ²;
  - the rigorous upper enclosures at X = 32 and X = 64.
- **Interpretation of §6 to correct:**
  - The constant 64Δ² comes from two features of the model: the clamp q′(0) = 0 at the inner end, and the normalisation of the weight at that end.
  - Length of the transition is not the mechanism. With a free entrance velocity, the reduced cost tends to zero.
  - The invariant that carries resistance is Φ = q + q′/4, not q.
- **Exact replacement for the schematic model:** the diagonal Bianchi IX equations give an exact nonlinear identity that turns "|ΔΦ|² ≤ (P/8π²) R_Φ" into a theorem for diagonal metrics. That theorem has an explicit potential term which the schematic model omits.

## 1. Frozen-core cluster inequality

**Derivation.** The cores Cᵢ are pairwise disjoint and the cluster metric equals gᵢ on Cᵢ. Since |Ric + 6g|² ≥ 0, J(g_cluster) ≥ Σᵢ J(gᵢ; Cᵢ). Subtracting from Σᵢ J(gᵢ) gives (2.1).

- The isolated configuration has exact CH between cells, so it contributes zero. Any cluster metric there contributes at least zero, so nothing is lost outside the cells.
- Disjointness at depth w holds. Centres sit at distance 2ρ − w and core radii are ρ − w, so the cores are separated by w.
- The value ρ = 1.762747 equals arccosh 3 (cosh r = 3 at the cell edge).
- The quadratic form of the same fact is ∫|ΣAhᵢ|² ≥ 0. It bounds the sum of all cross terms below by −Σᵢ∫|Ahᵢ|². So the ceiling is per cell, not per pair, as stated.

**Interpretation at w = 1.6.**

- The protected core r < 0.16275 holds J/(8π²) = 0.84805 of the cell's 0.99912 (`exterior_budget_X8.json`).
- The adjustable exterior energy is 0.15106. The measured pair saving is 1.25×10⁻⁵, about 1.2×10⁴ times smaller. At this depth the inequality is correct but carries no quantitative information about the experiment.
- It becomes informative only if the neighbour's perturbation is confined to r > 1 (ceiling 1.99×10⁻⁴ per cell), and the w = 1.6 geometry does not do that.

**Precision of the pair numbers.**

- The X = 16 savings are 1.9×10⁻⁷ at w = 1.2 and 6.1×10⁻⁷ at w = 1.4. These sit at the level of the 2.2×10⁻⁷ discrepancy between the budget script's grid quadrature and the recorded J.
- The 4D autodiff pair code is a different code path. Still, the w = 1.2 and w = 1.4 savings at X = 16 have no stated error bound and are not yet distinguishable from quadrature error.
- The X = 8 and X = 16 values at w = 1.6 (1.25×10⁻⁵ and 1.54×10⁻⁶) are well above that level. Their ratio is 8.1, as stated.

## 2. The reduced minimisation (6.1)

**Exact solution.** Put v = q′ and f = v′ + 4v. The endpoint data v(0) = v(T) = 0 and q(T) − q(0) = Δ are equivalent to two linear constraints:

∫₀ᵀ e^{4s} f ds = 0,  ∫₀ᵀ f ds = 4Δ.

The second follows from ∫v = ∫f(s)(1 − e^{4(s−T)})/4 ds together with the first. Minimising ∫e^{4s}f² under these constraints gives f = A e^{−4s} + B. With ε = e^{−4T}:

inf 𝒜_T = 16Δ²/K(T),  K(T) = (1−ε)/4 − 4T²ε/(1−ε).

**Check against the JSON:**

| T | 0.25/K(T) | JSON `energy_over_limit` |
|---|---|---|
| 2 | 1.02230 | 1.022299 |
| 4 | 1 + 2.89×10⁻⁵ | 1.0000289 |
| 8 | 1 + 1.3×10⁻¹¹ | 1 + 1.3×10⁻¹¹ |

K increases to 1/4, so inf 𝒜_T decreases monotonically to **64Δ² = 39.6031**. The problem is a convex quadratic on an affine space, so the critical point is the global minimum. The script's closed form is correct.

**Unweighted control.** The JSON resistances are exactly 7/32, 15/32 and 31/32 at T = 4, 8, 16. That means the energy is 32Δ²/(2T − 1) ~ 16Δ²/T, confirming the T⁻¹ decay.

**Structural reason.** Let Φ = q + q′/4. Then Φ′ = f/4 identically. Cauchy–Schwarz gives

(ΔΦ)² ≤ (1/16) ∫e^{−4t} dt · ∫e^{4t} f² ≤ (e^{−4t₀}/64) 𝒜.

This holds for every T and every profile. The 1/64 in the JSON (resistance → 0.015625) is this constant.

**Interpretive corrections to §6.**

1. **The clamp q′(0) = 0 carries the whole effect.**
   - With free entrance velocity v₀, the constraints become ∫f = 4Δ − v₀ and ∫e^{4s}f = −v₀.
   - As T → ∞ the infimum is 64(Δ − v₀/4)².
   - At v₀ = 4Δ an admissible f = A + Be^{−4s} costs ≈ 64Δ²e^{−4T}, which tends to 0.
   - The reason: the homogeneous mode q = c e^{−4t} moves q by v₀/4 at zero defect. Hence the conserved quantity is Φ, and q alone can relax for free.
   - The endpoint mismatch that matters is the jump of Φ between the entrance of the ACH region and CH infinity.
2. **The minimiser concentrates at the inner end.**
   - The optimal forcing is f ≈ 16Δ e^{−4t}, so the cost is set by the weight at the entrance.
   - Shifting t₀ multiplies the bound by e^{4t₀}, so 64Δ² has no meaning without the orbit-volume normalisation there.
   - The sentence "a long noncollapsed ACH transition does not by itself destroy resistance" is true but beside the point. The weighted problem never wants a long transition; it pushes the jump inward, toward where the ACH comparison ends.
3. **The missing items in §6 should include Φ at the entrance.** That quantity is generated by the core and is distinct from orbit-volume collapse or mode concentration.

## 3. Conditional route: an exact diagonal identity

For diagonal Bianchi IX the orthonormal Ricci tensor is diagonal. With W = a₁a₂a₃, q = log(a₂/a₃) (Kähler slot 1, bolt in slot 3) and the Step-13 formulas:

**(W q′)′ = W (V − E)**, where

- E = Ric°₂₂ − Ric°₃₃ (the −6g and scalar parts cancel);
- V = Pot₂ − Pot₃ = 4(a₂² − a₃²)(a₂² + a₃² − a₁²)/W².

This holds with no ACH assumption. The ACH model is the special case W ∝ e^{4t}, V = 0.

**Pointwise and integrated bounds.** For a trace-free diagonal tensor, |Ric°|² ≥ E²/2, and this is sharp. The orbit volume is 2π²W. Hence

P/(8π²) ≥ (1/8) ∫E² W dt.

**Calibration.** Let G(t) = ∫ₜ^∞ W⁻¹ and Φ_G = q + G W q′. Then Φ_G′ = GW(V − E) exactly. On an exact CH collar q ≡ 0, so Φ_G(∞) = 0, and

| Φ_G(t₁) + ∫_{t₁}^∞ GWV | ≤ (∫E²W)^{1/2} R(t₁)^{1/2},  R(t₁) = ∫_{t₁}^∞ G²W dt.

This gives (Φ_G(t₁) + ∫GWV)² ≤ 8R(t₁) · P/(8π²), which is the Step-14 inequality with R_Φ = 8R.

- On CH, W = sinh³t cosh t and **G(t) = ½csch²t − log coth t**. This tends to 4e^{−4t}, giving R(t₁) ≈ e^{−4t₁}/4.

**The potential term the schematic model drops.** Linearising V about CH with Kähler slot 1 (a₁ = sinh·cosh, a₂ = a₃ = sinh) gives V ≈ k(t)q with

k(t) = 8(1 − sinh²t)/(sinh²t cosh²t).

- k > 0 for t < arcsinh 1 = 0.881, so curvature pushes q away from 0 there at zero defect.
- k ≈ −32e^{−2t} at large t, which is restoring.
- The sharp linear calibration therefore replaces G by the decaying solution ψ of (Wψ′)′ = Wkψ, normalised so that −Wψ′ → 1. The flux is W(ψq′ − ψ′q), with error ∫ψW(V − kq) and resistance ∫ψ²W.
- This is a 1D linear ODE whose constants can be enclosed rigorously.

**Where the cells' energy actually sits.**

- About 85% of J lies in r < 0.163, near the bolt at r = 0.0998. Only about 2×10⁻⁴ lies beyond r = 1.
- If the full Rossi mismatch ΔΦ = 0.787 were still present at t₁ = 1, the bound with W(1) = 2.13 would force P/(8π²) ≳ 8 · 2.13 · 0.62 ≈ 10.
- So low-cost cells must resolve almost all of the mismatch inside r ≲ 1, where neither the ACH weight nor V ≈ 0 holds.
- The tube calibration therefore controls transport of a small residual Φ outward. The coercive content lives in the core.
- The X = 32 and X = 64 profiles allow a direct test: compute Φ_ψ(t₁) and ∫_{t₁}E²W and check how close the inequality is to equality.

**What remains open for a diagonal lower bound.**

- (a) Low-cost compactness on the bolt side, including the regime of small bolt parameter b. For b < 0.29 the Step-13 separatrix does not approach ACH, and its Einstein fillings are uncharacterised.
- (b) A lower bound on W, or equivalently an upper bound on R, at a controlled entrance radius.
- (c) Control of ∫ψW(V − kq).
- (d) A rigorous lower bound on |log ρ| over the ACH filling family. Currently 2.196 is a shooting minimum over sampled b.

**What this route can and cannot deliver.**

- It addresses positivity of the diagonal cell constant, i.e. that cost cannot tend to 0.
- It would give some positive constant. Nothing in it points toward a value near the numerical 0.9987.
- Non-diagonal and non-invariant competitors are untouched by any part of it.

## 4. The X = 32 and X = 64 enclosures

**What they establish rigorously.**

- They enclose J₆ for two explicit Chebyshev metrics. Assuming the Arb integrand is the correct curvature expression and the metrics are admissible:
  - bolt regularity is built into the ansatz;
  - Ricci is continuous at the collar junction (u = 0.999999 matches u = 1 to about 10⁻⁸).
- They give the explicit upper bound **𝔍_{1,0} ≤ 0.9987027644836** in units of 8π² for diagonal exact-collar cells.
- The certified η values match (1 − upper) exactly.

**Consistency checks.**

- J − P equals 4.6×10⁻⁶ at X = 32 and 2.7×10⁻⁶ at X = 64. So S ≈ −24 almost everywhere, and P ≈ J. This bears directly on how ΔS enters the Chern–Weil decomposition.
- The float records lie outside the balls: by 1.8×10⁻¹¹ at X = 32 and 1.1×10⁻¹⁰ at X = 64. This is float quadrature error and does not affect any conclusion, but only the ball values should be quoted.

**What they do not establish: convergence in X, and therefore the infimum.**

- The increments 2.13, 1.66, 0.34 ×10⁻⁴ change abruptly at the last step.
- That step coincides with a degree change from 12 to 16 and an unconverged optimiser (gradient ∞-norm 3.2×10⁻³).
- The fall from 1.66 to 0.34 is therefore not yet evidence of saturation.

## 5. Strongest sound implication

**Rigorously established:**

- an explicit diagonal cell with J₆ ≤ 0.99870276449 · 8π²;
- an exact per-cell ceiling on frozen-core cluster savings;
- an exact Φ-calibration for diagonal Bianchi IX metrics, in which the cost needed to shift the Rossi invariant Φ is controlled by ∫|Ric°|² and an explicit resistance R or ∫ψ²W.

**Numerical:**

- ACH Einstein fillings realise only ρ ≳ 2.2;
- large-collar cells converge on compact sets, and their cost stays near 0.9987·8π².

**Reduction obtained:** positivity of the least defect within diagonal cells is reduced to an inner statement. Every low-cost cell must reach an entrance radius with bounded resistance while still carrying a Φ value near log ρ of some Einstein filling.

**Not yet established:** any lower bound for the full cell problem, or for α, beyond what Step 13 already had.