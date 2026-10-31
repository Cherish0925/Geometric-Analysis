# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md",
    "Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md",
    "Sessions/S1003A02/workspace/data/o11perp/profile_perp_smooth_x0.03.csv",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md"
  ]
}
```

## Task

Analyze the exact relative calibration and transgression results from peer Session S1003A01 together with the perpendicular cell profile and the active Einstein-gap goal. Explain whether the decomposition P/(8π²)-1 = three nonnegative squares + ∫2u1u2u3/λ2 can plausibly yield a general lower bound in the perpendicular SU(2)-invariant sector, what matrix Hardy/Riccati inequality would be needed, and how the first-order cancellation R^+ζ=0 enters. Compare its mathematical value to brute-force Hessian computations. Identify a concrete inequality or transformed variable that could control the cubic term by the endpoint data and squares without losing an O(x0) term.

## Output

# Memo: the relative calibration (4.8) in the perpendicular SU(2) sector — sharpness, the resonance hidden in the cubic, and what a lower bound would need

## 0. Summary

**What is solid.** The decomposition (4.8) is exact and tight at both ends:

- the Burns bolt region and the exact CH collar each annihilate all three squares and the cubic;
- no O(x₀) term can arise, which is the Bianchi-IX form of R⁺ζ = 0.

**What changes the picture.** The cubic is not a perturbation to be absorbed by a Hardy inequality. It contains a **resonant source**: W := u₂u₃ is the product of the decaying Burns tail and the growing CH mode, and it is scale-invariant (constant) across the neck. A one-line re-completion turns (4.8) into an identity with an explicitly subtractive term −∫W²(λ₁+λ₂)/λ₂² dt. In a flat neck nothing in the remaining squares is forced to pay for it.

**What the reduction predicts.** In the perpendicular diagonal sector,

  inf P/8π² − 1 ≈ −9x₀²(log(1/x₀) − c),

with a similar coefficient (≈ −7.5 to −7.9) for J. If this is right, (5.1) cannot hold uniformly in x₀ and the cell threshold breaks at small x₀.

**Status.** This is a derived prediction from (4.6) under explicit approximations (§3). It is not established. The existing numerics are consistent with an under-resolved version of it. A cheap one-parameter computation (§6) decides it.

## 1. Algebraic check and endpoint tightness

**Completion.** With H_i = u_i + ½u_ju_k = ½∂_iC:

- channels 1 and 3 are completed with "+", producing −2u̇_iH_i;
- channel 2 is completed around (2u₂ − u₁u₃), producing −u̇₂u₁u₃ + 2u₁u₂u₃/λ₂.

The cross terms sum to −dΦ/dt with Φ = u₁² + u₃² + u₁u₂u₃. Since Φ_bolt = 1 and Φ_CH = 0, (4.8) follows exactly. The re-derivation confirms the sign: the cubic is **+2u₁u₂u₃/λ₂**.

**Burns end.** Take u₁ = u₂ = 0, a² = b² = ρ, c² = ρ − ρ₀ (in x-units ρ = x, ρ₀ = x₀).

- The scalar-flat condition gives exactly u₃ = −x₀/x. This is the Burns metric dr²/(1−m/r²) + r²(1−m/r²)σ₃² + r²(σ₁²+σ₂²).
- The original channel-3 density is λ₃/4(u̇₃ − 2u₃/λ₃)² dt = 2x₀² dx/x³, which integrates from x₀ to ∞ to exactly 1.
- The calibrated channel-3 square vanishes identically.

So the threshold "1" in (4.8) is precisely the Burns energy, and Burns makes every term of (4.8) zero.

**CH collar.** Take u₁ = u₃ = 0, u₂ = 3x, λ₂ = √(x/(1+x)), dt = dx/(2√(x(1+x))).

- Then u̇₂ = 6√(x(1+x)) = 2u₂/λ₂, so the channel-2 square vanishes.
- H₁ = H₃ = 0, and the cubic is zero.

The identity is therefore sharp on both model geometries. This is real value: any lower bound proved from it would be optimal at both ends.

## 2. How R⁺ζ = 0 enters

The three diagonal channels are the three self-dual directions ω_i:

- the CH Kähler form occupies channel 2 (u₂ = 3x carries s/4);
- the Burns form ζ occupies channel 3.

**Aligned case.** Both modes sit in the same channel, u₃ = 3x − x₀/x. The charge C = u₃² acquires the cross term −6x₀. This is the first-order cost 6x₀cos²θ = −x₀R⁺(ζ,ζ).

**Perpendicular case.** The two modes live in different channels. Each satisfies its own square:

- the growing mode satisfies u' = u (in log x);
- the decaying mode satisfies u' = −u.

No same-channel cross term exists. The only coupling is through the so(3) structure terms ½u_ju_k, and those are quadratic in the amplitudes. This is why every term of (4.8) is O(x₀²).

**The surviving interaction.** It is W = u₂u₃, which enters H₁. It is the Bianchi-IX realization of the bracket (s/4)·(ω_CH × ζ): it is nonzero exactly when R⁺ζ = 0 and ζ ⊥ ω, and for a tilt it scales like sin θ.

**Scaling.** In the neck x₀ ≪ x ≪ 1:

  W ≈ 3x·(−x₀/(x√(1+x))) → −3x₀,

a constant. This is the standard 4D resonance: decaying mode r⁻² times growing mode r² gives a source r⁰. It resonates with the scale-invariant squashing mode, so the energy accumulates per unit log x. The x₀² log(1/x₀) scale follows.

## 3. Neck reduction

Use s = log x. In the neck all λ_i ≈ √x and dt = (λ/2) ds. Per unit s, the terms of (4.8) become:

- S₁ = ½(u₁' + u₁ + W/2)²
- cubic = u₁W
- S₃ = ½(u₃' + u₃ + (3x/2)u₁)²
- S₂ = ½(u₂' − u₂ + ½u₁u₃)²

**The u_i are independent.** Three functions (G, F, w) correspond to three u's, obtained by integrating ȧ_i = u_i + f_i(a). An explicit check with constants η:

  G → x(1+η), F → x(1−η/2), e^w → 1−η/2

shifts u₁ by η and leaves u₂ and u₃ unchanged to first order. This deformation is polynomial and admissible: w(x₀) = 0 is kept by ramping η on away from the bolt.

**W is fixed by the endpoint data.** Writing u₃ = W/(3x), the calibrated S₃ = (1/18x²)(W' + 4.5x²u₁)². The 1/x² weight makes W rigid through the neck. Its value is set by the Burns mass (bolt at x₀) times the CH coefficient 3. No square pays for W itself, because the Burns tail is a zero mode of S₃.

**Exact re-completion.** Complete channel 1 around the shifted target. Then

  P/8π² − 1 = ∫[ λ₁/4·(u̇₁ + 2H₁/λ₁ + 2u₂u₃/λ₂)² + S₂ + S₃ ] dt
       − ∫ (u₂u₃)²(λ₁+λ₂)/λ₂² dt
       + ∫ u₁·d/dt(λ₁u₂u₃/λ₂) dt.   (E)

The end term [u₁λ₁u₂u₃/λ₂] vanishes because u₁ = 0 at the bolt and at the collar. Every term in (E) is O(x₀²), and no O(x₀) term has been discarded.

**The sign-definite term.** In the neck the middle term is −∫W² ds = −9x₀²(log(1/x₀) + O(1)). The last term carries dW, so it contributes only O(x₀²) without a log, from the core and collar transitions.

**Attainability.** The modified channel-1 square vanishes for u₁ = −3W/2 ≈ 4.5x₀. With this choice:

- S₃ = ½(6.75x₀x)², which integrates to O(x₀²) with no log;
- S₂ = O(x₀⁴/x²);
- switching u₁ on and off costs O(x₀²).

Equivalently, at fixed W the reduced density ½v² + 1.5vW + W²/8 is an indefinite form in (v, W) with determinant −½. Its minimum over constant v is −W².

**Naive superposition, for contrast.** Take F = x − x₀, e^w = 1+x, G = (x−x₀)(1+x). This competitor needs correction at the bolt: e^{w(x₀)} = 1+x₀ and √(G'F')(x₀) = √(1+x₀). Its closed-form values are:

- u₁ = −x₀√x/√((1+x)(x−x₀))
- u₂ = √x(3x−2x₀)/√(x−x₀)
- u₃ = −x₀/(x√(1+x))

This gives u₁ ≈ −x₀ and a density of about +6x₀² per unit s, i.e. a log of the opposite sign. The sign of the x₀² log term is therefore set entirely by the u₁ response. That is why fixed-basis optimizers can report either sign.

**J version.** From (4.12), the scalar bracket in the neck is (2/x)Σ(u_i' + H_i), so J − P = ½Σ² per unit s.

- With u₁ = v and the CH amplitude fixed, Σ ⊃ v + W/2.
- Optimizing with δ₂ (and optionally δ₃) absorbing part of the scalar defect gives a J density of −7.5x₀² to −7.9x₀² per unit s.

The scalar square does not remove the deficit.

**P versus J.** For P, any growing mode u₂ = κx is a zero mode of S₂; varying κ costs only ½(κ'x)² per unit s. So the CH curvature amplitude seen by the bubble is almost free in P. J pins it via a scalar density 2x²(κ−3)². This confirms that P and J must remain separate targets, and that J is the better-posed cell problem.

## 4. Consistency with the stored data

**CSV check** (S1003A02 profile_perp_smooth_x0.03, row x = 0.10039; a = √x, b = √h₃₃, c = √h₁₁):

| quantity | value | comparison |
|---|---|---|
| u₁ | +0.0145 ≈ 0.48x₀ | chamber u₁u₂u₃ < 0, as reported |
| u₂ | 0.217 | 3x = 0.301 |
| u₃ | −0.271 | Burns-tail value −0.286 |
| W | −0.059 ≈ −2.0x₀ | |
| C | 0.120 | consistent with the reported min 𝒯/8π² ≈ 0.118 |
| target u₁ = −3W/2 | ≈ 2.9x₀ | the profile's u₁ is about 16% of it |

At x₀ = 0.03 there is essentially no neck (x/x₀ ≈ 3), so this is not an asymptotic test. It does show the response is only partially excited.

**Excess coefficients** (P/8π² − 1)/x₀², all upper bounds:

| x₀ | 0.1 | 0.03 | 0.01 | 0.003 | 0.001 |
|---|---|---|---|---|---|
| coefficient | 15.4 | ≈21 | 19.4 (18.7 at degree 10–12) | 13.5 | 10 |

From x₀ = 0.03 down, the coefficient decreases by roughly 3–4 per e-fold of log(1/x₀). This trend is consistent with an emerging −κ log(1/x₀) term (predicted κ = 9 at full response). It is not consistent with a law +c·x₀².

**Convergence.** Gradients stayed at 10⁻⁴–10⁻³, and L-BFGS stopped on function reduction. A global polynomial basis in x resolves a log-uniform plateau of u₁ on [Kx₀, x₁] poorly.

## 5. The matrix Hardy/Riccati inequality that would be needed, and why it cannot close

**Why Q₊/Q₋ are not enough.** The forms (5.2)/(5.3) are homogeneous Hessians on exact CH. In log x their small-x limit is ¼(v'² + v²) per unit s, which is positive, so Hardy positivity holds. But in the cell the transverse vector is η = η_B + ξ, where η_B is the Burns tail fixed by the bolt. Then

  Q[η_B + ξ] = Q_reg[η_B] + 2B(η_B, ξ) + Q[ξ],

and B ∝ (3x)·u₁·u₃^B ≈ 3x₀u₁ is a constant linear source. The quantity that decides the sign is the Schur complement ⟨B, Q⁻¹B⟩ against Q_reg[η_B], which is zero in the calibrated form. Positivity of Q± is necessary and irrelevant to the sign.

**Riccati certificate.** A certificate must have the form 𝔅 = ½ξᵀK(s)ξ + kᵀξ + m(s), with ℓ + d𝔅/ds ≥ 0 and 𝔅 bounded at the ends.

- For the u₁ block, the quadratic coefficient condition admits K ∈ [−2, 0].
- With k = W (constant), this produces exactly the completion (E) and forces m' = −W².
- So m drifts by 9x₀² log(1/x₀).

The end budget in (4.8) is zero. No bounded calibration exists for small x₀, and the Hamilton–Jacobi corrections B₀ + ψ cannot repair this. The proposed ψ ≈ −u₁u₃ in the neck is a partial version of the k-term above.

**Sharp form of (5.1).** The inequality reduces to

  ∫(S̃₁ + S₂ + S₃) ≥ ∫W²(λ₁+λ₂)/λ₂² dt − ∫u₁ d(λ₁W/λ₂),

where S̃₁ is the modified channel-1 square in (E). The left side can be driven to O(x₀²) while the right side is about 9x₀² log(1/x₀).

**Transformed variable to use.** The answer to "control the cubic without losing O(x₀)" is the shifted channel-1 variable

  ũ := u̇₁ + 2H₁/λ₁ + 2u₂u₃/λ₂.

It removes the cubic exactly, introduces no end term, and isolates the obstruction as −∫W² plus a dW-transport term.

**What (E) gives rigorously.** Since S̃₁, S₂, S₃ ≥ 0,

  P/8π² − 1 ≥ −∫(u₂u₃)²(λ₁+λ₂)/λ₂² dt + ∫u₁ d(λ₁u₂u₃/λ₂)

holds for every diagonal perpendicular cell. Combined with a priori pointwise bounds |u₂u₃| ≲ x₀ and |u₁| ≲ x₀, it would yield P ≥ 8π²(1 − Cx₀² log(1/x₀)). That is the best positive statement this route can deliver.

## 6. The computation that settles the prediction

Take the stored near-minimizers at x₀ = 10⁻³ to 10⁻⁵, using a log-x quadrature. Add the deformation

  G·(1+η), F·(1−η/2), e^w·(1−η/2), with η = η₀χ(log x),

where χ is a cutoff equal to 1 on [Kx₀, x₁] and supported away from the bolt and the collar. Evaluate P and J with the existing curvature code (verified to 10⁻⁹).

- (E) predicts a convex quadratic in η₀ with minimum near u₁ + η₀ ≈ −3W/2.
- At the minimum, the per-log slope of the excess should move toward −9 (P) and −7.5 (J).
- Evaluating ∫W² ds and the dW term on the stored profiles checks (E) term by term at no extra cost.

**Consequences if confirmed.** The "+O(x₀²) margin" at ζ ⊥ ω is replaced by a deficit, and the cell threshold j ≥ 4 breaks at small x₀ in the SU(2) sector. Off-diagonal modes can only lower it further.

## 7. Value compared with brute-force Hessians

**Hessians.** The rotation Hessians and θ² Schur complements are local second variations around ansatz-dependent profiles. The diabatic artifact of Step 6 shows they can be wrong in sign structure. They give no certificate. In fixed polynomial bases they under-resolve log-uniform responses, so they cannot detect this resonance.

**The calibration (4.8) with (E).**

- It is exact and tight at both ends.
- It explains the first-order cancellation structurally (channel separation, i.e. R⁺ζ = 0).
- It names the single second-order invariant, W = (Burns mass) × (CH curvature), the ω_CH × ζ bracket.
- It yields a closed-form asymptotic prediction with a definite coefficient.

Its main mathematical contribution is likely to be the opposite of the intended lower bound: a mechanism, and an explicit competitor direction, for sub-threshold perpendicular cells.

## 8. What remains unresolved

1. Whether the O(x₀²) constants from the core and collar transitions push the crossover below accessible x₀. The table in §4 suggests a crossover somewhere below 10⁻³.
2. Whether (4.6) itself holds in the neck regime at the level used. It was verified on near-minimizers, but not term by term in the asymptotic neck.
3. The exact J coefficient. This needs the full (4.12) bracket with λ_i corrections.
4. The global effect on α. A per-blow-up deficit of order x₀² log(1/x₀) tends to 0, but it makes the cell infimum strictly below 8π². This changes strict-inequality statements built on coefficient 4.