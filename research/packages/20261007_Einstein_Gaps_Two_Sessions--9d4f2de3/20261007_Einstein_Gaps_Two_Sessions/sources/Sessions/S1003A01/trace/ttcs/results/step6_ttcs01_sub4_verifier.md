# TTCS Independent Branch Record

```json
{
  "step_id": 6,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_localization_and_coupled_filling.md"
  ]
}
```

## Task

Independently examine the corrected perpendicular O11 branch and our new dual-cost/transgression computation. Check: (i) the normalization relation J=P+(1/4)∫(s+24)^2 in the peer's Ric=-6g normalization; (ii) the axis relabeling (new a,b,c)=(old s2,old s3,old s1) and the reported bolt/collar values Y=-1 at the bolt, Y=0 and Pi=X^4? here X=1 gives Pi=9 because CH h=(x,x,x+x^2) and radial normalization; identify the exact general formula in these coordinates; (iii) what the profile x0=.01, P≈1.001996, J≈1.002453, Tmin≈0.0516 says mathematically; and (iv) whether there is a sharper localized boundary/interior identity or inequality that could prove P≥8π² or J≥8π² in the perpendicular diagonal class. Distinguish established algebra from numerical indication and surface any normalization or smoothness errors. Give a direct technical memo with explicit equations and a proposed theorem target.

## Output

# Memo: the perpendicular O11 branch, its normalization, the slice charge, and what could close it

## 0. Main findings

**(i) Normalization.** J = P + ¼∫(s+24)² is exact algebra, and the code implements it correctly. The script's comment that J is scale invariant is wrong. J is fixed only because the collar fixes the scale.

**(ii) Relabeling and collar values.** The relabeling is legitimate, and the bolt value Y = −1 is exact. On the CH collar the exact values are
- Y ≡ 0,
- p₊ ≡ 0,
- Π = T/8π² = 9x², which equals 9X² at the collar slice.

The value is not X⁴. In I54 radius units it is R⁴/4 = 4d/8π². Because Y ends at 0, the zero-flux certificate is vacuous in this branch. The cause is not a singular Y, as Step 5 §5 says.

**(iii) The x₀ = 0.01 profile.** It is a second-order cell for both P and J. Its T_min ≈ 0.052 matches a two-flux superposition T ≈ x₀²/x² + 9x², whose minimum is 6x₀ = 0.06. No slice inside the bubble-to-CH crossover pays 8π². The script's "min_intF_minus_T" is a tautology.

**(iv) Prospects for a proof.** There is no SU(2)-invariant symplectic form, self-dual for a metric conformal to G, that is nondegenerate at the bolt and equals ω_CH on the collar. So the conformal almost-Kähler transfer behind I54 Theorem 1, I54 §6.1 and I55 Prop. 5 has no perpendicular analogue. Any lower-bound argument must be exact at order x₀² log(1/x₀).

**A decisive indication from existing data.** Both branches are consistent with a second-order term −λ x₀² ln(1/x₀) with λ > 0. If this persists at θ = π/2, then P < 8π² for x₀ ≲ 10⁻⁴.

**An inconsistency in the peer note.** Step 8's statement that the aligned control "is the Kähler cell" contradicts the exact Kähler identity.

---

## 1. Normalization (established algebra)

**Ricci decomposition.** With Ric = Ric° + (s/4)g,

  |Ric + 6g|² = |Ric°|² + 4(s/4 + 6)² = |Ric°|² + (s+24)²/4.

Hence J = P + ¼∫(s+24)². The code's `q = Σ(s+24)²W/(32π²)` is exactly this term divided by 8π².

**Rescaling.** Put g′ = 6g. Then Ric(g′) = Ric(g) = −6g = −g′, and

  |Ric+g′|²_{g′} dV_{g′} = 36⁻¹|Ric+6g|²_g · 36 dV_g.

So J_peer = J_I54 and P_peer = P_I54.

**Scale invariance.** P is scale invariant. J is not: under g ↦ λg it becomes ∫|Ric + 6λg|². The comment in `perp_dual_cost.py` should say "invariant once the collar fixes the scale".

**Background values agree with the code.**
- Volume form: dV = π²√(det h/G) dx, which on the collar is π²x dx.
- Ball volume: Vol(x ≤ X) = π²X²/2.
- Scalar term: s² = 576, so S = 288π²X².
- Self-dual Weyl term: |W⁺|² = 24 = 36·(2/3), so W = 12π²X².
- In I54 units: d = 36·π²X²/2 = 18π²X², and 4d/8π² = 9X².

**Relative identities in peer-normalized form.**

  P/8π² − 1 = [∫(4|W⁺|² + s²/12) − 4d]/8π²,
  J/8π² − 1 = [∫𝔉 − 4d]/8π²,
  J − P = ¼∫(s+4)²_{I54} ≥ 0.

So P ≥ 8π² implies J ≥ 8π², and the converse does not hold. J enters the E-coefficient through I54 (2.3); P enters the trace-free functional.

**Docstring mismatch in `o11_perp_cell.py`.**
- The docstring has g = … + F σ₁² + x e^{−w}σ₂² + x e^{w}σ₃², and "x e^{−w} → x/(1+x)".
- The code uses h = diag(F, x, x e^{w}).
- The code is consistent: on the collar, h → diag(x, x, x+x²) and G → x+x². With ρ² = 6x this is dρ²/(1+ρ²/6) + ρ²(σ₁²+σ₂²) + ρ²(1+ρ²/6)σ₃², the Ric = −g CH ball.

## 2. Relabeling, exact slice values, and a two-flux form of T

**The relabeling is an orientation-preserving isometry.** A cyclic, or any signed, permutation of (σ₁,σ₂,σ₃) is induced by right translation by an element of SU(2). That map preserves dσᵢ = 2σⱼ∧σₖ, the orientation, and every slice.

**T is symmetric under all permutations.** Write T̃(slice) for T evaluated on permuted labels. Then T̃ − T is a function of first-order slice data with zero t-derivative along every profile. Such a function is constant, and it vanishes on the flat round slice. So the transgression is unique, and Y² + Π is only one labeling's decomposition of it.

A cheap check of the implementation follows: on interior slices, T computed in the three cyclic labelings must agree.

**General formulas in peer coordinates.** New labels are a = √x, b = √x e^{w/2}, c = √F, with ′ = 2√G d/dx. Put ε := a/b = e^{−w/2}. Then

  p₊ = [e^{w/2}√G − √F + x(1−e^{w})/√F] / (√x e^{w/4}),
  p₋ = [e^{w/2}(1 + x w_x)√G − √F − x(1−e^{w})/√F] / (√x e^{w/4}),
  Y = √G F_x/√F − 2cosh(w/2) + F e^{−w/2}/x + ½p₊p₋,
  Π = e^{−w/2}p₊² + e^{w/2}p₋² − ¼(p₊p₋)².

**Bolt values.** At the bolt F = G = 0, w = 0 and F′G′ = 1. Then c′ → √(F′G′) = 1, cosh(w/2) → 1, z² → 0 and p± = O(t). Hence Y = −1, Π = 0 and T/8π² = 1, which is the correct O(−1) jump.

**Collar values.** On the collar F = x, G = x(1+x), e^{w} = 1+x and w_x = 1/(1+x). This gives exactly

  p₊ ≡ 0, p₋ = 3x(1+x)^{−1/4}, Y ≡ 0, Π = 9x², T/8π² = 9x² = ρ⁴/4 = 4d(x)/8π².

The orientation check in the script ("expected 9") is correct: the reversed CH orientation would give 3X².

**Two-flux identity (exact algebra).** Set Y_⊥ := p₋/√ε. Then

  T/8π² = Y² + Y_⊥² + p₊²(ε − p₋²/4).

- On the collar Y_⊥ = 3x, the same magnitude as the aligned-slot CH flux Y_al = 3x.
- The flux vector (Y, Y_⊥) runs from (−1, 0) at the bolt to (0, 3X) at the collar.
- In the aligned slot the two charges are collinear, so the one-dimensional intermediate value theorem forces a zero-flux slice.
- At θ = π/2 they are orthogonal, and a planar path can avoid the origin. This is the exact sense in which the zero-flux mechanism disappears.

**Correction to Step 5 §5.** In the bolt-adapted labeling Y is regular. The certificate is vacuous because Y_collar = 0, not because Y is singular. Y_collar = 0 is the slice form of ⟨ρ_CH, ζ⟩ = 0 for ζ ⊥ ω_CH, which is the same vanishing as the first-order cost −x₀R⁺(ζ,ζ). This interpretation of Y_⊥ as the CH-direction Ricci flux is unproved for non-Kähler slices. A test: compare Y_⊥ with Y computed in the labeling (old s1, s2, s3), whose c-slot is the CH fibre, on the outer region.

## 3. What the x₀ = 0.01 profile says

**Excesses.**
- P − 1 = 1.996×10⁻³ ≈ 20x₀².
- J − 1 = 2.453×10⁻³ ≈ 24.5x₀².
- J − P = 4.6×10⁻⁴ ≈ 4.6x₀².

The first-order scalar change ΔS/12 ≈ 2x₀ cancels inside ∫(s+4)². So the first-order cancellation at θ = π/2 holds for J as well as P. Since this is the P-optimizer, the J-infimum at this x₀ is at most 1.00245.

**Superposition picture (heuristic).** Take Y ≈ −x₀/x for the Burns flux. In the aligned case this matches Step 5's Y = −μ/r² + r²/2 = 3x − x₀/x. Take Y_⊥ ≈ 3x for the CH flux. Then

  T ≈ x₀²/x² + 9x² ≥ 6x₀, with the minimum at x_* = √(x₀/3) ≈ 0.058.

The observed T_min = 0.0516 lies 14% below 6x₀. The reported x_at_min_T should be compared with 0.058. For a general angle the same picture gives T_min ≈ 6x₀(1 − cos θ), which is 0 when aligned, as Step 5 found numerically.

**The script's certificate quantity is tautological.** By the I54 identity, ∫_in𝔉 − T(ρ) = J_in(ρ) − 8π² exactly. So `min_intF_minus_T` is just min(J_cum − 1), and it is −1 at the bolt. A slice certificate has content only through an independent lower bound on ∫_in𝔉.

**No slice works in the CH-like region.** With 𝔉 ≥ 1, the certificate needs 2.25x² ≥ T(x). Even with the sharper value 𝔉 ≈ 4 (Burns: s ≈ 0, W⁺ = 0; CH: 𝔉 = 4), one gets ∫_in𝔉 − T ≈ 9x² − x₀²/x² − 9x² = −x₀²/x². The reason is that T_CH = 4·Vol exactly.

At the crossover the inner piece pays about 1 − 3x₀. Equivalently, the Burns tail beyond x_* carries about 3x₀ of energy, which is first order, while the total excess is only second order.

**Where the threshold is crossed (heuristic).** With J_out(x) ≈ x₀²/x², the crossing J_cum = 1 occurs near x_c ≈ x₀/√(J−1) ≈ 0.20, independent of x₀. If the reported `threshold_cross_x` agrees, the perpendicular threshold is a property of the macroscopic collar region, not of the bubble.

## 4. Smoothness and consistency issues

1. **Bolt smoothness.** With wpow = 1, w ∝ (x − x₀) ∝ t². The σ₂² − σ₃² anisotropy has charge 4 in the normal angle, so smoothness needs O(t⁴), which is wpow = 2. The wpow = 1 metrics are only C^{1,1}.
   - Chern–Weil and the transgression still hold, since curvature is in L^∞.
   - Theorem C as stated for C² cells does not apply.
   - `perp_dual_cost.py opt` defaults to wpow = 2, which is correct. `eval` inherits the wpow of the record.

2. **Collar regularity.** The cells match CH to C² at x = X, not on an open collar. First-order slice data match, so T(X) = 9X² exactly. I54 Prop. 2 (no smooth critical point) does not literally apply to these profiles.

3. **The aligned control is not Kähler, nor conformally Kähler.**
   - With t = πμ = 6πx₀ and d = 18π²X², I54 (3.2) gives P_K/8π² = (1+3x₀)² + ¼∫(s+4)²/8π² ≥ 1 + 6x₀ + 9x₀².
   - For any metric conformal to a Kähler cell, W⁺ is conformally invariant and S_G ≥ I_K²/v_K. Hence P_G − 8π² ≥ I_K²/(4v_K) − 4d, so P/8π² ≥ 1 + 6x₀ + 10x₀² + O(x₀³).
   - The reported aligned slopes 5.619–5.994 all lie below 6.
   - So these cells are genuinely non-conformally-Kähler (w-anisotropy, N ≠ 0). This is consistent with I54 (6.6), whose P-version minimum is −4d/3 at N = m₀/3.
   - Step 8's phrase "i.e. the Kähler cell" is therefore incorrect, and the sub-6 slope is an anisotropy effect.

4. **Upper bounds.** The θ = π/2 values are line-search-terminated, so they are upper bounds on the infimum.

## 5. Toward a proof, and the decisive asymptotic question

**(a) The conformal almost-Kähler route has no perpendicular analogue (established).**
- SU(2)_L-invariant 2-forms are Σ fᵢ dt∧σᵢ + gᵢ σⱼ∧σₖ, and the condition dα = 0 is gᵢ′ = 2fᵢ.
- Self-duality for a diagonal metric decouples slot by slot. So closed self-dual invariant forms are Σ Cᵢ ω̂ᵢ with gᵢ = exp(2∫aᵢ/(aⱼaₖ)dt).
- Equality with ω_CH on the collar forces C₁ = C₂ = 0. The surviving form ω̂₃ ∝ t dt∧σ₃ + t²σ₁∧σ₂ vanishes on the bolt.
- Self-duality is conformally invariant, so no metric conformal to G carries such an almost-Kähler form.
- Invariant symplectic forms that rotate from the bolt slot to the CH slot do exist; they need (Σgᵢ²)′ ≠ 0. They are compatible only with metrics not conformal to G, which removes the scalar/Weyl transfer behind I54 Theorem 1 and I55 Prop. 5.

**(b) Available exact certificate.** For every slice ρ,

  J − 8π² ≥ ∫_in𝔉 − 8π²[Y² + Y_⊥² + p₊²(ε − p₋²/4)](ρ),

and the same with 𝔉 replaced by 4|W⁺|² + s²/12 for P. By §3, this cannot certify near the crossover. It could only certify at x ~ x_c, after an O(x₀²) interior lower bound on ∫_in𝔉 − 4Vol has been proved. Any Cauchy–Schwarz moment argument that loses O(x₀) is useless here, because the margin is O(x₀²).

**(c) Second-order structure suggested by the data.** Burns has an r⁻² (that is, x₀/x) tail. Interaction terms |h_B|²|Rm_CH|² dV ~ x₀² dx/x integrate over √x₀ ≲ x ≲ X to x₀² ln(1/x₀). This is the complex-dimension-2 logarithm familiar from blow-up gluing with Burns potentials; that correspondence should be checked against the literature.

Fitting the reported numbers with the form c(x₀) = b − λ ln(1/x₀):

| Branch | Quantity | Data points used | Fit |
|---|---|---|---|
| Aligned | x₀⁻²(6x₀ − (P−1)) | 22 (x₀=0.01), 33, 44, 53, 60 (x₀=10⁻⁴) | λ(0) ≈ 9.5, b ≈ −22 |
| Perpendicular | (P−1)/x₀² | 10, 14.4, 20 at x₀ = 10⁻³, 3·10⁻³, 10⁻² | λ(π/2) ≈ 4.3, b ≈ 40 |

- The aligned fit reproduces all six points within about 10%.
- The perpendicular fit predicts 14.8 at the middle point, against 14.4 observed.
- Larger x₀ (21 at 0.03, 15 at 0.1) departs, as expected from higher-order terms.

These are numerical indications from rough fits, not established values. If they persist, P/8π² − 1 changes sign near x₀ ≈ e^{−b/λ} ≈ 10⁻⁴, with minimum depth ≈ λx₀²/2 ~ 10⁻⁸ near x₀ ≈ 6×10⁻⁵. Under-resolution and early line-search termination raise P, so they cannot explain the observed decrease of c(x₀).

**(d) Theorem target.** For SU(2)_L diagonal cells with bolt orientation ζ at angle θ to ω_CH,

  inf P/8π² = 1 + 6x₀cos²θ − λ(θ) x₀² ln(1/x₀) + γ(θ) x₀² + o(x₀²),

with λ(θ) = λ₀ + λ₂P₂(cos θ) + λ₄P₄(cos θ). SO(3)₊-equivariance at second order in R⁺ allows spin up to 4. The coefficients would be computed from the matched overlap √x₀ ≪ x ≪ 1 as one half of the coefficient of the scale-invariant density x₀² dx/x. That density is a quadratic form in the Burns tail tensor and Rm_CH, including the first-order response field. The same statement should be made for J, which enters I54 (2.3).

The dichotomy:
- λ(π/2) > 0: perpendicular SU(2) cells with P < 8π² exist at small x₀. The cell conjecture is then false in this class, and J must be checked separately for the E-coefficient.
- λ(π/2) < 0, or λ(π/2) = 0 with γ(π/2) > 0: the threshold holds asymptotically with an x₀² log margin. A proof would then need an identity exact to that order.

**Inexpensive tests from existing machinery.**
- **Plateau test.** The density x·dP_cum/dx (and the same for J), divided by x₀², should show a plateau in the overlap region if the logarithm is real. Compare x₀ = 0.01, 0.003, 0.001.
- **Small-x₀ cells.** Compute P- and J-optimized perpendicular cells at x₀ = 3×10⁻⁴, 10⁻⁴, 3×10⁻⁵. Polynomial degree must grow with ℓ = ln(X/x₀), and relative precision near 10⁻⁹ is needed. The Chern–Weil residuals of 4×10⁻¹⁰ make this feasible.