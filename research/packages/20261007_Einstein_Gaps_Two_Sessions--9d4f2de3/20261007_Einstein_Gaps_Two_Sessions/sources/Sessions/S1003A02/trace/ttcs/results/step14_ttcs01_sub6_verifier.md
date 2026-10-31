# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 3,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/o11_cell_einstein_shadow.py",
    "Sessions/S1003A02/workspace/data/o11_cell_einstein_shadow.json",
    "Sessions/S1003A02/workspace/figures/o11_cell_einstein_shadow.png",
    "Sessions/S1003A02/workspace/scripts/o11_collar_independent_verify.py",
    "Sessions/S1003A01/workspace/data/perp_collar/x0.01_X8_J_d8.json",
    "Sessions/S1003A02/workspace/notes/step13_einstein_fillings_blown_up_ball.md"
  ]
}
```

## Task

Critically read the empirical comparison between the certified X=8 subthreshold cell and the Einstein bolt flow. The profile reconstructs geodesic state, estimates a bolt anisotropy d_fit≈-0.462, and shows the same-bolt Einstein trajectory becomes singular at t≈0.297 while 99% of the positive P action of the cell is accumulated by t≈0.319 (90% by t≈0.150). State what scientific conclusion about the 'shadow Einstein separatrix then pay a late CR layer' picture is warranted. Check slot/sign conventions and whether d_fit instability invalidates the comparison. Relate this to the exact control-action identity shared by the peer: P/(8π²)=∫Σ λ_i/4 (u_i'−2H_i/λ_i)^2 dt. Suggest the strongest next mathematical object this evidence supports: local bolt action/calibration, compactness contradiction, or another formulation.

## Output

# Memo: the certified X=8 cell compared with the same-bolt Einstein flow (b = 0.1)

## 1. Summary

The supplied data do not support the picture "the cell shadows an Einstein separatrix, then pays in a late CR-correction layer" for this cell. They support a different and sharper statement.

**The certified cell is a Burns bubble of scale b grafted into CH².** Three things follow from this:

- **Jet.** Its bolt jet is the Burns (scalar-flat Kähler) jet, not the Einstein jet.
- **Distribution of action.** Its positive action follows the exact Burns density, with total ≈ 8π².
- **Location of the saving.** The subthreshold saving is only 8.9·x0² ≈ 9×10⁻⁴ of 8π². That is about ten times smaller than the Burns tail beyond t ≈ 3b. The cumulative-P plot therefore cannot show where the saving lives.

The Einstein comparison at b = 0.1 cannot test shadowing for either of two independent reasons:

- The two flows differ already at second order at the bolt.
- By Step 13, no ACH separatrix exists for b ≲ 0.29.

## 2. The bolt jets differ at second order, so d plays no role

**Cell jet.** The cell profile has G(x) = (x−x0)e^{qG} + O(u³). Here qF(x0) = −qG(x0) is forced by the shift, which gives F′G′ = 1 at the bolt.

From the stored coefficients, using T_k(−1) = (−1)^k:

- Σ c_F,k (−1)^k ≈ −0.0316.
- Hence G′(x0) = e^{0.0316} ≈ 1.032.

With x = x0 + q² and q = √G′ t + O(t³), the slot-1 axis is a₁ = √x ≈ b + G′t²/(2b). So

- p₂^cell = G′/(2b) ≈ 5.16 at b = 0.1.

**Einstein jet.** The Einstein series of Step 13 forces

- p₂^Ein = (3b²+2)/(2b) = 10.15.

**Interpretation.** p₂ = 1/(2b) is exactly the Burns value, since Burns has a₁ = √(t²+x0). The Einstein value is about 1/b. This factor of 2 is the whole content of the recorded distances:

- At t = 0.02: y₁^cell ≈ G′t/b² ≈ 2.06 versus y₁^Ein ≈ 2p₂t/b ≈ 4.06, with the same gap in y₂. This reproduces y_distance = 3.59.
- By t = 0.1 = b, the log-axis distance is 0.48, a 60% axis discrepancy inside the core.

**Consequence for d.** The anisotropy d enters a₁ − a₂ at order t⁴ and y at order t³. The mismatch is fixed at order t² by b alone. No choice of d, and no refinement of d_fit, makes this Einstein orbit shadow the cell.

## 3. d_fit is exact for this record but structurally fragile

The fit can be checked analytically:

- In the cell, a₁ − a₂ ≈ −√x · w/2.
- Near the bolt, w ≈ C_w u², with u ≈ G′t²/(x0 ℓ), ℓ = log(X/x0) = 6.685, and C_w = Σ c_w,k (−1)^k.
- Hence d = −C_w G′²/(2 b³ ℓ²).

From the record, C_w ≈ 0.039, which gives d ≈ −0.465. This matches d_fit = −0.4623.

So the polynomial fit is reliable even though the t² and t⁴ correction terms reach the size of d at t = 0.02. The ratio c₁b² ≈ −11 is natural in the rescaled variable s = t/b.

**Where the fragility lies.** C_w ≈ 0.039 is a cancellation of coefficients of size about 10. The optimizer's gradient tolerance, 6×10⁻⁵, therefore leaves d poorly determined as a property of the minimizer.

**Where d does matter.** The rescaled anisotropy d̂ = d b³ ≈ −4.6×10⁻⁴ is tiny, so the core is essentially U(2). Step 13(A) reports that the U(2) Einstein orbit at b = 0.1 (d = 0) is AH. The singular exit at t = 0.297 ≈ 2.97b therefore reflects the triaxial instability amplifying d̂. The exit time is sensitive to d. The non-tracking is not, because it is fixed by p₂ in Section 2.

## 4. The action is exactly the Burns density

The peer's control identity can be evaluated on Burns, a₁ = a₂ = √(t²+x0), a₃ = t:

- u₁ = u₂ = 0 and u₃ = −x0/(t²+x0).
- λ₃ = (t²+x0)/t, H₃ = u₃.
- The density is (λ₃/4)(u₃′ − 2H₃/λ₃)² = 4x0² t/(t²+x0)³.

This integrates to exactly 1 in units of 8π². The cumulative fraction is 1 − x0²/(t²+x0)², which is approximately 1 − (x0/x)² in the cell coordinate.

**Comparison with the recorded quantiles.**

| x (recorded quantile point) | Predicted fraction 1 − (x0/x)² | Recorded fraction |
|---|---|---|
| 0.01058 | 0.107 | 0.10 |
| 0.01435 | 0.514 | 0.50 |
| 0.02055 | 0.763 | 0.75 |
| 0.0333 | 0.910 | 0.90 |
| 0.119 | 0.993 | 0.99 |

The tabulated recorded fractions are the nominal quantile levels at which the script reports x. The agreement is 1–3% across the whole distribution, so the cell's |Ric°|² distribution is Burns.

**Structural reading of the identity.** The bolt endpoint fixes u₃(0) = a₃′ − (a₁²+a₂²−a₃²)/(a₁a₂) = 1 − 2 = −1, and u₁(0) = u₂(0) = 0. In the exact CH collar with Kähler slot 2:

- u₁ = u₃ = 0.
- u₂ = 3 sinh²t.

The primitive u₁² + u₃² + u₁u₂u₃ in `density_x` is therefore 1 at the bolt and 0 at the collar. This gives

P/(8π²) = 1 + S₁ + S₂ + S₃ + ∫ 2u₁u₂u₃/λ₂ dt.

Here S₁, S₃ ≥ 0 are re-completed squares and S₂ ≥ 0 is the original square. The "1" is the bolt charge u₃(0)², the control-variable form of the exceptional-curve Chern–Weil term. **A cell can go below 8π² only through the cubic cross term**, the interaction of the bubble field u₃ ≈ −x0/r² with the CH field u₂ ≈ 3r², mediated by the perpendicular mode u₁. This is why perpendicularity matters. The quadrature output of `o11_collar_independent_verify.py` already contains S₁, S₂, S₃ and cubic, and is the direct measurement of this split.

## 5. Why no Einstein orbit can shadow a small-b cell

Rescale a_i = b â_i(t/b). With Ric = −6g, the rescaled cosmological constant is −6b² → 0. The rescaled Einstein bolt flow therefore converges to the Ricci-flat O(−1) bolt flow.

By Bishop–Gromov rigidity, a Ricci-flat ALE manifold asymptotic to R⁴ with trivial group is flat, so it cannot contain the bolt. No Ricci-flat O(−1) bolt is asymptotically R⁴, which is what the bubble of a cell must be. This explains three things at once:

- the Einstein exit at t/b ≈ 3;
- the Step 13 observation that the separatrix stops approaching ACH below b ≈ 0.29;
- why a P-bounded cell with small bolt must use a non-Einstein bubble.

**The bubble floor.** For an ALE metric on Bl₀C² with flat infinity, the inputs are χ = 2, τ = −1, Gauss–Bonnet correction 1/|Γ| = 1 and η(S³) = 0. The two Chern–Weil formulas give

∫|Ric°|² = 8π² + 4∫|W₊|² + ∫S²/12 ≥ 8π²,

with equality iff W₊ = 0 and S = 0, which the Burns metric attains. This is the bubble form of the peer's P = 8π² + 4ΔW₊ + ΔS/12. The 8π² cost of the cell is topological at the bubble scale. Only an O(b⁴) background interaction can lower it.

## 6. A quantitative coincidence that locates the saving

Suppose the saving is the CH integrand 4|W₊|² + S²/12 removed from an excised volume equal to a symplectic cut of weight b. The bolt area is πb², and the excised ball has volume π²b⁴/2. For Kähler–Einstein CH² with Ric = −6g:

- S = −24 and |W₊|² = S²/24 = 24.
- The integrand is 96 + 48 = 144.

This predicts

P/(8π²) − 1 ≈ −144 · (π²b⁴/2) / (8π²) = −9 x0².

The recorded margins are −8.91 x0² for P and −8.84 x0² for J.

This is not yet a derivation. The cell is perpendicular, so the core's Kähler form ω₃ is not CH's ω₂, and W₊ need not equal S²/24 in the transition region. It is, however, a sharp and testable prediction. Two cheap computations decide it:

- **Volume and W₊ split.** Compute ΔVol = Vol(cell) − Vol(CH ball, x ≤ X), and ∫(|W₊|² − 24), separately from the stored record. The prediction is ΔVol ≈ −π²x0²/2.
- **Dependence on x0 and X.** Run the margin over x0 at fixed X, and over X at fixed x0. A core effect predicts a limit of −9 with no log x0 term and no X-dependence. A late collar layer would show X-dependence instead.

## 7. Slot, sign and orientation conventions: these are consistent

| Check | Result |
|---|---|
| Bolt slot | Bolt in slot 3: a₃ = √F, with a₃′(0) = √(F′G′) = 1 matching Bolt(1). |
| Collar Kähler slot | Slot 2: a₂² = X(1+X), a₁² = a₃² = X. |
| κ₂ at collar | √(9/8) = 1.0607, which is coth t. |
| ρ₂ at collar | 1. |
| Collar dev | 0.0859 at exact CH. |
| Configuration | Perpendicular. |

**Slot exchange.** Step 13 uses Kähler slot 1. The swap 1 ↔ 2 combined with σ₃ → −σ₃ preserves the structure equations and the orientation dt∧σ₁∧σ₂∧σ₃. It maps d → −d and ρ = a₂/a₃ → a₁/a₃, which is CR-equivalent to the script's a₃/a₁.

**Sign of d.** d < 0 means a₂ > a₁ near the bolt, so the CH slot 2 grows first. This is the correct sign.

**"dev" is not a CR quantity.** It is nonzero (0.086) for exact CH at X = 8 because it is dominated by e^{−2t} terms. ρ and the asymptotic value of κ are the CR quantities.

## 8. Defects in the figure and JSON that mislead

- **Extrapolated Einstein values.** `sol.sol` is evaluated beyond `ein_tend = 0.297`. Every Einstein value for t > 0.297 is polynomial extrapolation of the dense output, not dynamics. This covers the 10¹⁰⁵–10¹¹³ plateaus in panels 1–2 and the table rows at t ≥ 0.4, including the Infinity/NaN entries, which are also invalid JSON. These should be masked at `ein_tend`.
- **Compressed axes.** The log scales then compress all meaningful cell information against the bottom axis.
- **Panel 3 shows the bulk, not the saving.** It displays the 8π² Burns bulk, not the 9×10⁻⁴ saving. The informative curves are:
  - the cumulative integral of (P-density − 4x0²t/(t²+x0)³);
  - the cumulative cubic term.

  Plotting these against t/b would show where the saving accumulates.

## 9. Mathematical objects the evidence supports

**(a) Small-bolt expansion with a local calibration.** The identity P/(8π²) = 1 + S₁ + S₂ + S₃ + ∫2u₁u₂u₃/λ₂ is exact. In the Burns-scaled core, u₃ = −x0/r² + …, u₂ = 3r² + …, and u₁ is generated linearly by their coupling.

Minimizing S₁ + ∫cubic over u₁ at fixed Burns u₃ and CH u₂ is a quadratic problem. It should produce the coefficient of b⁴ in closed form; Section 6 predicts −9. The resulting statement would be:

inf P_cell(b)/(8π²) = 1 − c b⁴ + o(b⁴), with c determined explicitly.

The upper bound would come from an explicit Burns-plus-correction metric. The lower bound would come from Cauchy–Schwarz on the cubic term against S₁ and S₃. This would replace the certified numerics with an analytic theorem: subthreshold cells exist for all small b, and the depth of the dip is sharp.

**(b) Compactness through the bubble.** Take an SU(2) sequence with P ≤ (1 − δ)8π².

- Sections 4–5 show b → 0 is impossible: the rescaled limit is an ALE bubble on Bl₀C² with ∫|Ric°|² ≥ 8π², and the background correction is O(b⁴).
- b → ∞ needs a separate rescaling argument.
- With b in a compact range, ODE compactness on the bolt side applies. The remaining question is where the defect sits as the outer radius varies.

A total-depletion limit 𝔓_{1,0} = 0 would then have to be a complete Einstein ACH filling with b ≳ 0.29 and standard CR infinity. Step 13 finds only ρ ≳ 2.2 in that range. The rigorous missing piece is the interval-enclosure of ρ(b) described in Step 13 §6.

**(c) Where the shadow picture can be tested.** The picture is meaningful only for b ≳ 0.29, where a perpendicular ACH Einstein separatrix with ρ(b) ≥ 2.2 exists. Testing it requires optimized cells at, for example, b = 0.4, 0.8 and 1.5, compared with the separatrix orbit d*(b) rather than the same-d orbit. Two quantities to measure:

- whether the cell's (a, y) tracks the separatrix up to some t_*;
- whether the excess action concentrates where the cell's ρ is bent from ρ(b) to 1.

If it does, the neutral mode L₂ − L₃ provides the Lyapunov functional proposed in Step 13 §6.3. At b = 0.1 the present comparison is uninformative on this question. That is a consequence of Section 5, not of numerics.