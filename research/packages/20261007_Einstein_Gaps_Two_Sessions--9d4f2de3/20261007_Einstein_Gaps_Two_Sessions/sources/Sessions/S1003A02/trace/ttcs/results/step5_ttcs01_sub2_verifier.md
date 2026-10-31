# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step4_O10_localization_and_orbifold_test.md",
    "Sessions/S1003A02/workspace/scripts/o10_localization.py",
    "Sessions/S1003A02/workspace/data/o10_localization.json",
    "Skills/geometric-analysis/research/paper/sections/finite_density_endpoint.tex",
    "Skills/geometric-analysis/research/paper/sections/single_parameter_statement.tex",
    "Skills/geometric-analysis/references/results-and-questions.md",
    "Skills/geometric-analysis/references/conventions-and-literature.md"
  ]
}
```

## Task

Independently check the proposed density-free endpoint Theorem L and Corollary K in the Step 4 note. Verify the exact rewriting of V kappa_beta; all inequality directions; the optimized gamma and coefficient a(theta,beta); the discriminant and thresholds theta=2/3, beta=8, theta=3/4; and, crucially, close the proof for every original metric by using the actual conformal-monopole hypotheses, Yamabe normalization, conformal transfer, and the finite-parameter theorem with its true b=(-a^2)_+/V factor. State an exact corrected theorem and proof if valid, and flag any quantifier/constant flaw. Also verify the Kähler blow-up corollary's p>=A, a^2=T_+, Noether density calculation and universal constant under its stated p_g hypothesis.

## Output

# Verification of Theorem L and Corollary K (Step 4 note)

## Summary

- **Algebra.** Every algebraic step of Theorem L is correct: the rewriting, the inequality directions, the optimal γ, the coefficient a(θ,β), the discriminant, and the three thresholds.
- **The open step closes.** The bounded-β branch on arbitrary metrics follows from the corpus conformal transfer (§2 below). The transfer costs only a factor 2 and a cap 1/16.
- **A stronger theorem holds.** For θ < 3/4 the factor (β−2)²/β² is not needed: κ_β ≥ c(θ) > 0 uniformly in β ≥ 2, with an explicit c(θ).
- **Weaker hypotheses suffice.** The hypothesis a² ≥ T₊ enters only through the finite-parameter theorem. It is not needed at all for θ < 2/3, and it can be replaced by a bound on (−a²)₊/A.
- **Corollary K is correct** as stated, with c_K = min{c_L(0.7), c(B=41.3)}.

## 1. The algebra, checked line by line

**Rewriting (1.1).**
- |Ric+g|² = |Ric°|² + |(s/4+1)g|² = |Ric°|² + (s+4)²/4.
- Inserting P = S/12 + 4W − 8π²T₊ (from 4π²T₊ = S/24 + 2W − P/2) gives these coefficients:
  - S: 1/12 + 1 + 1/β = 13/12 + 1/β;
  - W: 4 + 6(β+1) = 6β + 10;
  - −8π²T₊ and −72π²p.
- These are correct and match the JSON.

**Input (1.2).**
- LeBrun's estimate ∫(s − √6|W⁺|)² ≥ 72π²p uses the operator HS norm, i.e. LeBrun's 32π²(c₁⁺)² form multiplied by 9/4.
- For each metric g it needs solutions for the metrics conformal to g. That is exactly the actual-conformal-supply hypothesis of `thm:finite-density-endpoint`.
- Then (s−√6|W⁺|)² ≤ (|s|+√6|W⁺|)² ≤ (1+γ⁻¹)s² + 6(1+γ)|W⁺|². The directions are correct.

**Use of T₊ ≤ θA.**
- If T₊ ≥ 0, then θ ≥ 0 and T₊ ≤ θA ≤ θp, using p ≥ A.
- This gives −8π²T₊ − 72π²p ≥ −72π²λp with λ = 1 + θ/9. Correct.
- Only T₊ ≤ θp is used. That condition is conformally invariant; A matters only for uniformity across classes.

**Optimal γ.**
- The W-coefficient is (6β+10) − 6λ(1+γ). It vanishes at 1+γ = (9β+15)/(9+θ), i.e. γ_max = (9β+6−θ)/(9+θ) > 0.
- Any γ ≤ γ_max keeps W ≥ 0 harmless. Since 1+γ⁻¹ decreases in γ, γ_max maximizes the S-coefficient, so this choice is optimal within the method.

**Coefficient a(θ,β).**
- Recomputing gives a = 13/12 + 1/β − (9+θ)(3β+5)/(3(9β+6−θ)).
- Over β(9β+6−θ) the numerator is N = (3/4−θ)β² + (1/2 − 11θ/4)β + 6 − θ. This matches.
- The pointwise minimum of as² + (s+4)²/4 is attained at s = −4/(4a+1) and equals 16a/(4a+1). The JSON expression `pointwise_min_bound(a)` equals 16N/[(12−4θ)β² + (8−12θ)β + 24 − 4θ], the same quantity.

**Discriminant and thresholds.**
- disc = (1/2 − 11θ/4)² − 4(3/4−θ)(6−θ) = 57θ²/16 + 97θ/4 − 71/4 = (57/16)(θ−2/3)(θ+142/19). Verified.
- At θ = 2/3, N = (β−8)²/12.
- N(8) = 58 − 87θ = 87(2/3−θ), so β = 8 lies in the interval where N < 0 for every θ > 2/3.
- At θ = 0.74 the roots are 3.505 and 149.995.
- The constants a∞ = 1/12 − θ/9 and c∞ ∈ {1, 0.4, 1/7, 0.0177} are all verified.
- D₈ = 108π²(T₊ − 2p/3) + 27P/2 is verified by substituting W = 2π²T₊ − S/48 + P/4.

**A cleaner description of what the method sees.** N is affine in θ, so the elementary bound is positive at parameter β exactly when T₊/p < θ_c(β), where

  θ_c(β) = (3β² + 2β + 24)/(4β² + 11β + 4).

- θ_c(2) = 20/21.
- θ_c(8) = 2/3, the global minimum, which is the double root.
- θ_c(∞) = 3/4.
- At fixed θ < 3/4 the bad set {θ_c(β) ≤ θ} is a compact β-interval, empty for θ < 2/3.

The scan column `beta0_first_positive` in the JSON reports 2.01 for every θ. It never detects the interval (β₋, β₊) where a < 0, so it carries no information. The roots β± would be the informative output.

**β = ∞ numerology (§3).**
- P/V → 0, s → −4 and W/V → 0. Choosing γ → ∞ slowly in (1.2) gives S − 72π²p = o(V).
- Hence p/V → 2/(9π²), T₊/V → (2/3)/(4π²) = 1/(6π²), and T₊/p → 3/4 = θ_c(∞).
- The Euler identity gives 8π²χ/V → 2/3 + ⨍|W⁻|².
- All of this is consistent with eq. (finite-density-characteristic-limit).

## 2. The bounded-β branch on an arbitrary metric: closed

The note's chain κ_β ≥ (P + D_β/β)/V ≥ c_par(β−2)²/β⁴ is applied to g, but `thm:single-parameter` is stated only on the s = −4 representative ĝ. The transfer goes as follows.

**Setting up ĝ.**
- Conformal supply with p > 0 forces Yamabe constant < 0, so ĝ exists.
- On ĝ: one smooth unperturbed solution exists by supply, and p is conformally invariant.

**Removing the factor (1+b).**
- If T₊ > 0 and a² ≥ T₊, then a² > 0 and b = (−a²)₊/V̂ = 0 exactly, so no "after reducing the constant" step is needed.
- In general, 16V̂ = S(ĝ) ≥ 32π²p ≥ 32π²A gives b ≤ (−a²)₊/(2π²A).

**Transfer inequality.** With δ = S(g) − S(ĝ) ≥ 0:
- P̂ = P − δ/12 and D̂_β = D_β − (1+β⁻¹)δ ≥ 0, the latter by LeBrun on ĝ. Hence δ ≤ D_β ≤ κ_βV.
- Write e = s_g + 4. Then ∫e² ≤ 4κV and ∫e ≤ 2√κ V.
- So 16V̂ = 16V − 8∫e + ∫e² − δ ≥ 16V(1 − √κ − κ/16).
- The numerator P̂ + D̂ ≤ P + D ≤ κV.
- These reproduce eq. (finite-density-yamabe-transfer).

**Consequence.** If κ_β(g) ≤ 1/16, the denominator is at least 0.746, so κ̂ ≤ 2κ. Therefore, for every g in the class,

  κ_β(g) ≥ min{1/16, ½ κ̂_β(ĝ)},  with κ̂_β ≥ (P̂ + D̂_β/β)/V̂ ≥ c_par(β−2)²/β⁴ / (1+b).

The note's form survives with constant min{1/16, c_par/(8β₊²)}·(β−2)²/β², using (β−2)²/β² ≤ 1. The elementary branch needs no transfer, because LeBrun's inequality holds for each metric of the class.

## 3. Corrected and strengthened statement

**Theorem L′.** Let a fixed Spin^c structure with determinant class a admit an actual unperturbed monopole for every metric of a conformal class. Let p = (a⁺)² ≥ A > 0.

(i) **T₊ ≤ 0.** For every metric g in the class and every β ≥ 2, κ_β(g) ≥ 1. This uses no hypothesis on a².

(ii) **0 < T₊ ≤ θA with θ < 2/3.** κ_β(g) ≥ c_el(θ) := inf_{β≥2} 16a/(4a+1) > 0 for all β ≥ 2 and all g. This uses no hypothesis on a² and no c_par.

(iii) **0 < T₊ ≤ θA with θ < 3/4, and (−a²)₊ ≤ ΛA.** The case a² ≥ T₊ gives Λ = 0. Then for all β ≥ 2 and all g,

  κ_β(g) ≥ c(θ,Λ) := min{ 1/16, (16/27)(3/4−θ), c_par(3/4−θ)² / [92(1 + Λ/2π²)] }.

In particular, κ_β ≥ c(θ,Λ)(β−2)²/β², which is the note's Theorem L.

**Proof of (i).** Drop −8π²T₊ ≥ 0 and set θ = 0. Then a(0,β) = (β²/4 + β/6 + 2)/(β(3β+2)) ≥ 1/12, since 12·numerator − β(3β+2) = 24. Hence κ ≥ 16a/(4a+1) ≥ 1.

**Proof of (ii).** N > 0 for all β ≥ 2 and a → a∞ > 0, so the infimum is positive.

**Proof of (iii).** Take θ ≥ 0 and split β ≥ 2 into three regions.

- **R1, β ∈ [2,3].** N decreases in θ, so N ≥ 21/4 − 25β/16 ≥ 9/16. The denominator satisfies β(9β+6−θ) ≤ 99. Hence a ≥ 1/176 and κ ≥ 4/45 > 1/16.
- **R3, β ≥ L := 25/(8(3/4−θ)).** Since 11θ/4 − 1/2 < 25/16 and 6 − θ > 0, we have N ≥ β[(3/4−θ)β − 25/16] ≥ (3/4−θ)β²/2. Also β(9β+6) ≤ 12β². Hence a ≥ (3/4−θ)/24 ≤ 1/32, and κ ≥ (128/9)a ≥ (16/27)(3/4−θ).
- **R2, β ∈ [3,L].** Note L ≥ 25/6. The function f = (β−2)²/β⁴ has f′ ∝ (β−2)(4−β), so its minimum on R2 is at an endpoint.
  - f(3) = 1/81.
  - f(L) ≥ (13/25)²/L² ≥ (3/4−θ)²/37.
  - Both are at least (3/4−θ)²/46.
  - Applying §2 gives the third entry of c(θ,Λ).

**Remarks on the statement.**
- **Sources of the window.** The window 2/3 ≤ θ < 3/4 genuinely needs `thm:single-parameter` on the compact interval {θ_c(β) ≤ θ}. That interval sits inside (3, 25/(8(3/4−θ))) because the vertex of N lies at β ≥ 8 and N(3) = (57−73θ)/4 > 0.
- **Root bound.** β₊ < 25/(16(3/4−θ)) follows from √disc < 25/16.
- **Why the β → 2 decay drops out.** The decay (β−2)²/β² of `thm:finite-density-endpoint` is forced by Kähler–Einstein metrics, where κ_β = 4(β−2)²/β and T₊/p = 1. For θ < 3/4, Theorem L′ shows the decay is absent; at β = 2 alone the elementary bound already works up to θ < 20/21.
- **Rate.** The quadratic rate (3/4−θ)² comes from the window growing like (3/4−θ)⁻¹ while the parameter estimate decays like β⁻². The material does not decide whether a linear rate holds.

## 4. Quantifier and constant points in the note

1. **Statement vs. proof coverage.** The note's Theorem L ("every metric", c depending only on θ) is true, but its written proof only covers the s = −4 representative on the interval [2, 2β₊]. §2 above supplies the missing step and changes the constant to min{1/16, ·/2}.
2. **Branch to which a² ≥ T₊ belongs.** The note writes "since a² ≥ T₊ ≥ 0, b = 0". That is correct only inside the case T₊ ≥ 0, which is the case where the window is used. For T₊ < 0 the parameter branch is never invoked. The hypothesis a² ≥ T₊ should be listed as needed only for θ ∈ [2/3, 3/4).
3. **c_par is imported, not reproved.** The proof relies on the corpus constant c_par, which I did not re-derive. It is absolute and holds simultaneously for all β.
4. **Constants as θ → 2/3 and θ → 3/4.** In (ii), c_el(θ) → 0 as θ ↑ 2/3, because a(θ,8) = 87(2/3−θ)/(8(78−θ)). Version (iii) is uniform over θ ≤ θ₀ < 3/4.

## 5. Corollary K

**Supply.**
- For a minimal surface X of general type with p_g ≥ 1, we have b₊ = 2p_g + 1 ≥ 3.
- On M = X#k(CP²)‾ the blow-up formula makes every K_X + Σεᵢ Eᵢ a basic class, giving solutions for every metric.
- Choose the signs εᵢ inductively so that each cross term 2εᵢ Eᵢ⁺·(K⁺ + Σ_{j<i} εⱼ Eⱼ⁺) ≥ 0. Then p ≥ (K_X⁺)² ≥ K_X² = A.
- The choice depends only on harmonic projections, which are conformally invariant, so one structure serves each conformal class. A is common to all classes.

**Squares.**
- a² = K_X² − k.
- T₊(M) = c₁²(X) + k(2 − 3) = A − k.
- Hence a² = T₊.

**Case split.**
- **k ≥ 0.3A.** Then T₊ ≤ 0.7A. Theorem L′(iii) applies with θ = 0.7 and Λ = 0, or L′(i) if k ≥ A.
- **k < 0.3A.** Noether gives p_g ≤ K²/2 + 2. Hence c₂ = 12(1 − q + p_g) − K² ≤ 5K² + 36 − 12q. Then χ(M)/A = (c₂ + k)/A < 5.3 + 36/A ≤ 41.3, using A ≥ 1. `thm:finite-density-endpoint` applies with B = 41.3.

**Constant.** c_K = min{c(θ=0.7, Λ=0), c(41.3)} is universal. Any θ₀ ∈ [2/3, 3/4) works in place of 0.7, with B = 6 − θ₀ + 36/A.

**Range of the corollary.** The (β−2)² factor must remain in Corollary K, because k = 0 with K_X ample is Kähler–Einstein. p_g ≥ 1 is exactly b₊ > 1 for Kähler surfaces. The statement covers this family only, not all Kähler surfaces.

**Braungardt–Kotschick window.** The arithmetic is correct:
- b₊ = 2χ_h − 1;
- Taubes gives SW(K) ≠ 0;
- p ≥ a² = T₊ = c₁², so θ = 1;
- χ/A → ∞.

I did not read the cited Theorem 4 itself.

## 6. Other parts of the note: proved vs. conditional

- **§4 quantitative Hitchin–Thorpe.** Correct. If T₊ ≤ 0 then P ≥ S/12, so 𝒥 ≥ 1. The product S²×Σ_g gives ℰ = 4 − 2(K₁+K₂)²/(K₁²+K₂²) > 2, tending to 2.
- **§5 Kähler–Einstein values.** |W⁺|² = 2/3, p = V/2π², and κ_β = 4(β−2)²/β are correct.
- **§5 rank of 𝐑⁺.** 𝐑⁺ = diag(s/4, 0, 0) has rank one; correct. The Kronheimer cores have W⁺ = 0 in the complex orientation, which is the orientation used.
- **§5 convergence p(g_ε) → K_Y².** This uses convergence of harmonic projections under gluing. It is standard but not written out.
- **§6 "orbifold bulks are excluded".** This rests on an orbifold version of `thm:finite-density-endpoint` that is not proved in the material. It is a conditional statement, not a consequence of Theorem L′.
- **What Theorem L′ shows about O10.** A density-free counterexample sequence must have T₊/p → 3/4 from above, so T₊/A ≥ 3/4 − o(1). This is the precise content Theorem L′ adds to the O10 description in §3.