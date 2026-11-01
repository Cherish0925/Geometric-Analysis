# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/notes/step4_weyl_profile_and_bubble_restriction.tex",
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Knowledge/objects/papers/Conformal-Kähler-rigidity-of-Einstein-four-manifolds--ee41ec8c511e--4518ab125268/object.md",
    "Knowledge/objects/papers/Einstein-metrics-via-Derdziński-duality--f7ddbaf86999--f2cdc1a49708/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md"
  ]
}
```

## Task

Analyze the proposed local-limit route for the fixed critical Ishida–LeBrun sequence. Starting from the exact quantitative deficit decomposition and Weyl norm profile, determine precisely what convergence on a harmonic-radius patch yields for (i) the selected Seiberg–Witten 2-form/eigenline, (ii) the W+ eigenvalue multiplicities, and (iii) the limiting Einstein metric. Check whether the nonnegative eigenvalue defect plus amplitude/Hodge projection control forces the limiting spectrum (-1/6,1/12,1/12) on a regular patch. Then check the Derdzinski consequence carefully: is this spectrum locally impossible at Ric=-g, or does it give a locally conformally Kähler noncompact model? Resolve conventions, conformal factor, scalar curvature, and Bochner formula, and identify the strongest true theorem.

## Output

## Verifier memo: the local-limit route for the fixed critical Ishida–LeBrun manifold

I checked the algebra, the eigenvalue-defect logic, the Derdziński/Catino–Dameno step, the conformal-factor equation, and the Bochner computation against the three supplied sources (LeBrun 2001, Catino–Dameno, Oliveira–Sena-Dias) and the two working notes. The central architecture is correct, one number in Step 7 is wrong, and the decisive scientific point — whether the profile is locally forbidden — resolves cleanly in favor of "not locally forbidden; obstructed only globally." Details below.

### 1. Conventions, all mutually consistent

For Ric = −g in dimension four, s = 4λ = −4. The genuine estimate ∫(s−√6w)² ≥ 72π²(a⁺)² is the (3/2)-rescaling of LeBrun Theorem 2.3: (3/2)(⅔s − 2√(2/3)|W⁺|) = s − √6w, and (3/2)²·32π² = 72π². This is correct.

Saturation of the completion identity (18) — which I verified expands exactly:
27(s²/24+2w²) − (s−√6w)² = ⅛(s+8√6w)² — forces s = −8√6 w, hence at s=−4, w = |W⁺| = 1/(2√6), |W⁺|² = 1/24.

With the almost-Kähler form ω in the lowest eigenspace and the two upper eigenvalues equal (LeBrun Prop. 2.4 plus the W⁺-invariance for equality in (10)), the spectrum is
(α,β,γ) = (1/12, 1/12, −1/6),  |W⁺|² = 6·(1/12)² = 1/24. ✓

Key structural identification: this is ρ := β/α = 1, i.e. the **largest** eigenvalue is double and the **simple** eigenvalue is the most sub-zero one. This is precisely the Weyl spectrum of a Kähler metric with s̃<0 (for Kähler, W⁺ = (s̃/6, −s̃/12, −s̃/12); when s̃<0 the simple eigenvalue s̃/6 is the least, the double −s̃/12 the greatest). So the calibrated profile is the "minus-scalar Kähler-type" Weyl structure, not the positive one.

I also confirmed detW⁺ = (1/12)(1/12)(−1/6) = −1/864, and
detW⁺/|W⁺|³ = (−1/864)·48√6 = −√6/18 = −1/(3√6) **exactly**.
This is the extreme value F(1) in Catino–Dameno (1.1). The profile sits at the threshold ρ=1, not strictly below it.

### 2. What the harmonic-radius patch yields (i)–(iii)

On a noncollapsed patch with uniform C^{2,α} harmonic radius, the chain in Step 7 §3 (Cheeger–Naber → W^{2,p} in harmonic charts → interior Schauder → C^{2,α} subsequential limit) gives a smooth limit g_∞ with Ric(g_∞) = −g_∞, hence s_∞ = −4. The deficit bounds (13)–(14) send D_amp, D_quad, D_Hodge, D_eig → 0 for the selected sign as δ→0 at fixed A, and Step 4 (A1) sends ∫(w−1/(2√6))² → 0.

(i) **SW 2-form / eigenline.** The rescaled φ_i = σ(Φ_i) is controlled in L² by (16)–(17) (‖iF_A⁺ − 2πH_a‖₂² ≤ Δ_a/18). On a patch where |Φ_i| stays bounded away from 0, C^{2,α} convergence gives a nonzero self-dual limit form φ_∞ = σ(Φ_∞) of constant length spanning the **lowest** W⁺-eigenline. The one genuine gap here, correctly flagged in Step 4 §6–§7, is the zero set of |Φ|: (16)–(17) are L² statements and do not by themselves exclude a small-measure set where the form degenerates. The C⁰ upgrade (41) plus noncollapse is what would close this.

(ii) **Multiplicities.** D_eig → 0 forces the sharp trace-free equality γ = −√(2/3)|W⁺|, which holds iff the two upper eigenvalues coincide and γ = −2α. I verified this is the algebraic content: for (α,α,−2α), √(2/3)|W⁺| = √(2/3)·√6·α = 2α = −γ. Together with |W⁺|² → 1/24 and s → −4 this pins the spectrum uniquely to (1/12, 1/12, −1/6). So yes: the eigenvalue defect plus amplitude/Hodge control does force the spectrum (−1/6, 1/12, 1/12) on a regular patch. This part is sound.

(iii) **Limiting metric.** g_∞ is Einstein, Ric = −g_∞, s = −4, with constant |W⁺|² = 1/24 and non-parallel W⁺ (see §5 below). It is not any of the standard bulks: CH² (KE, s=−4) has |W⁺|² = 2/3; real-hyperbolic has W⁺ = 0. Both are excluded by the profile (Step 4 Cor. B1, confirmed: |W⁺|_KE = √6/3 = 4·(1/(2√6))).

### 3. The Derdziński consequence — corrected reading

The direct Catino–Dameno positive-scalar conclusion **does not apply here**, and it is important not to invoke it. Their Theorem 1.4 / Cor. 1.3 require the largest eigenvalue simple (β ≤ ρ₀α, ρ₀<1), i.e. detW⁺/|W⁺|³ strictly above −1/(3√6). The profile is exactly ρ=1, the value they identify as sharp and explicitly exclude (their §7 examples with α_h=β_h are Ricci-flat K3 and tetrahedral Gibbons–Hawking, not Ric=−g). Their Corollary 1.7 (compact Einstein, s≤0, W⁺≢0 ⟹ sup ρ = 1) is instead **consistent** with the profile.

The correct local statement is Derdziński's ≤2-eigenvalue theorem in the branch where the **simple** eigenvalue is the sub-zero one (γ<0). Then g_∞ is (locally, after at worst a double cover) conformal to a Kähler metric g̃ = f²g_∞ whose scalar curvature s̃ < 0. Note detW⁺ < 0 here, so the specific det>0 normalization h = (24)^{1/3}|W⁺|^{2/3}g (Oliveira–Sena-Dias Thm C.1) is not the relevant gauge; the relevant conformal factor is built from the simple, sub-zero eigendirection.

**Conformal factor, resolved.** Using LeBrun's conformal law (his Lemma 2.2 form) s_{g̃} = f^{-3}(6∇*∇_g f + s_g f) with s_g = −4, and s̃ = −f^{-2} (from f²s̃ = −1, the constant-|W⁺| condition |W⁺_g|² = f⁴s̃²/24 = 1/24):

−f^{-2} = f^{-3}(6∇*∇f − 4f) ⟹ 6∇*∇f = 3f ⟹ **∇*∇f = f/2**,

with ∇*∇ = d*d the sign-plus (nonnegative-spectrum) Laplacian; equivalently Δf = −f/2 for the analyst's Δ = div grad, matching Step 7. I verified the sign both ways.

### 4. Compact impossibility vs. noncompact model — the decisive point

**Compact:** on a closed manifold ∫_M ∇*∇f dμ = ⟨df, d1⟩ = 0. But ∇*∇f = f/2 with f>0 gives ∫∇*∇f = ½∫f > 0. Contradiction. Equivalently f would be a positive eigenfunction of d*d for eigenvalue ½ > 0, which cannot be sign-definite. So there is **no** closed Einstein realization of the calibrated profile. Combined with LeBrun Prop. 2.4 + Armstrong (Cor. 2.5): a closed Einstein saturating metric would be Kähler-Einstein with |W⁺|² = s²/24 = 2/3 ≠ 1/24. This is the genuine rigidity, and Step 4 Cor. C states it correctly (as a conditional on smooth convergence). The Step 4 s* computation supporting it is right: with ω in the lowest eigenspace, W⁺(ω,ω) = 2γ = −1/3, s* = s/3 + 2W⁺(ω,ω) = −4/3 − 2/3 = −2 ≠ s = −4, so the saturating almost-Kähler metric is strictly non-integrable, and s+s* = −6 = (4/3)(s−√6w) checks.

**Noncompact:** on a complete noncompact (Poincaré-Einstein-type) manifold, positive eigenfunctions for positive eigenvalues of d*d exist, so ∇*∇f = f/2 with f>0 is solvable and the conformally-Kähler ρ=1 model is locally/noncompactly admissible. **Therefore the spectrum (−1/6, 1/12, 1/12) at Ric=−g is not locally impossible; it is a locally (and noncompactly) realizable conformally-Kähler model of the s̃<0 branch.** This is exactly Step 7's central finding, and it is correct: the Derdziński/Catino–Dameno route yields no purely local contradiction, and the exclusion is inherently global (Stokes on a closed M, or the connected-sum symplectic obstruction in the strictness argument). The conformally-Kähler-to-minus-scalar-Kähler constructions in Oliveira–Sena-Dias (Poincaré-Einstein fillings, and "beyond Derdziński" metrics conformal to scalar-flat Kähler) are the natural habitat for such models; whether any complete model carries the exact **constant** |W⁺|² = 1/24 profile in a rescaling limit is the substantive open question (see §6).

### 5. A concrete correction: Step 7 §1 Bochner coefficients and |∇W⁺|²

The Bochner formula written in Step 7 is
½Δ|W⁺|² = |∇W⁺|² + (s/3)|W⁺|² − 4 tr(W⁺)³.
The coefficients are off. Contracting the operator Weitzenböck ∇*∇W⁺ = −(s/2)W⁺ + 6W⁺∘W⁺ − 2|W⁺|²I (Catino–Dameno Lemma 2.5 with δW⁺=0, which I verified on CH²: 0 = 2λ + 6λ² − 4/3 holds at λ = 1/3 and λ = −2/3) with W⁺, using tr(W⁺³) = 3detW⁺, gives

½Δ|W⁺|² = |∇W⁺|² + (s/2)|W⁺|² − 18 detW⁺   (i.e. Δ|W⁺|² = 2|∇W⁺|² + s|W⁺|² − 36 detW⁺).

So the correct constant-|W⁺|² value at the target is
|∇W⁺|² = −(s/2)|W⁺|² + 18 detW⁺ = 1/12 − 18/864 = 1/12 − 1/48 = **1/16**, not 1/24.
At a=0 (eigenvalues (ε,−ε,0)) the correct value is 1/12, not 1/18, and the corrected family formula is
|∇W⁺|²(a) = 1/12 + (3/4)a − 144a³ on |a| ≤ 1/12
(I checked endpoints: 1/16 at a=1/12, 5/48 at a=−1/12, 1/12 at a=0; all positive). CH² still returns 0 with the corrected constants, as it must. The qualitative conclusions Step 7 draws — W⁺ non-parallel, metric not locally symmetric, |∇W⁺|² > 0 with no sub-trivial zero — all survive; only the numbers 1/24, 1/18, and the cubic −96a³ + a/2 + 1/18 must be replaced. Any later step that fed the value 1/24 into a quantitative estimate should be recomputed with 1/16. The coincidence that the wrong value 1/24 equals |W⁺|² is what made it look self-consistent.

### 6. Strongest true theorem, and what remains open

The strongest statement the local route actually establishes on a fixed critical Ishida–LeBrun manifold M (m=2 or 3, D=A/3) is a compactness-conditional exclusion / dichotomy:

- If some sequence g_i with δ_i = ‖g_i^{-1}(Ric+g)‖_∞ → 0 has a uniform C^{2,α} harmonic-radius lower bound and a uniform diameter upper bound, then a subsequence C^{2,α}-converges to a smooth Einstein g_∞ on M with Ric = −g_∞; near-equality forces the saturating profile (1/12,1/12,−1/6), |W⁺|²=1/24; LeBrun Prop. 2.4 + Armstrong force g_∞ Kähler-Einstein with |W⁺|²=2/3, a contradiction (equivalently, g_∞ would carry the symplectic/almost-complex structure the connected-sum topology forbids). Hence no such sequence exists: every pinched sequence must collapse (r_h → 0) or run to infinite diameter.

- The accompanying true local statement: the profile is not locally obstructed. On a regular patch it is the s̃<0 conformally-Kähler model with ∇*∇f = f/2, solvable on complete noncompact models, unsolvable on closed manifolds. The exclusion is global.

What is genuinely unresolved, and cannot be closed by the local/Derdziński analysis alone:

1. Whether the uniform harmonic radius + diameter hypotheses can be denied a priori from the pinching δ_i→0 (i.e. whether some Sobolev/noncollapse input follows from Ric-pinching plus the calibrated volume O(A)). Without this the dichotomy is conditional.
2. Whether a **complete** Einstein metric with Ric=−g and constant |W⁺|²=1/24 (the calibrated model, necessarily conformally Kähler to an s̃<0 Kähler metric with s̃ = −f^{-2}, f solving ∇*∇f=f/2) exists as a rescaling limit. This is the exotic model the profile permits and every known bulk excludes; it is the true content of the gap, and the Oliveira–Sena-Dias conformally-Kähler Einstein families are the concrete place to test its existence or nonexistence.
3. The nonvanishing of |Φ| (equivalently the C⁰ upgrade (41)) needed to promote the L² eigenline control of §2(i) to a global almost-complex structure; the zero set's codimension under Ricci-pinching alone is not settled.

These three are the substance that would turn the conditional exclusion into an unconditional one; the local conformal-Kähler machinery, correctly read, contributes the eigenvalue rigidity and the compact Stokes obstruction but does not reach them.