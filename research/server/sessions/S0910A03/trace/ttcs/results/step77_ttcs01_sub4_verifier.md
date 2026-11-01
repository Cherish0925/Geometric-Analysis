# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md",
    "Sessions/S0910A03/workspace/data/step77_pe_expansion.json",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md"
  ]
}
```

## Task

Verify the following claims about reflected Einstein cores on [0,∞) × T³ with Ric = -3g and S(0) = 0 (totally geodesic T³ center).

1. FEFFERMAN-GRAHAM EXPANSION: In the geodesic defining function gauge with ρ = e^{-r}, the PE expansion g_ρ = γ - Sch(γ)ρ² + g₃ρ³ + O(ρ⁴) (n=3 boundary dimension) gives the shape operator:
   S = I + Sch(γ)♯ e^{-2r} - (3/2)γ⁻¹g₃ e^{-3r} + O(e^{-4r})
with Sch(γ) = Ric_γ - (R_γ/4)γ in dim 3, and g₃ transverse-traceless. Check the signs and coefficients.

2. MEAN CURVATURE: H = 3 + (R_γ/4)e^{-2r} + O(e^{-4r}), so e^{2R}(3-H(R)) → -R_γ/4.

3. NORMAL IDENTITY: From H' = -|S|² + 3 (Riccati for Ric=-3g), d/dr[e^{2r}(3-H)] = e^{2r}|S-I|², hence e^{2R}(3-H(R)) = 3 + ∫₀^R e^{2r}|S-I|²dr. Check whether the Riccati equation H' = -|S|² + 3 is correct for Ric=-3g in dim 4.

4. R_γ < -12: Combining: -R_γ/4 = 3 + ∫₀^∞ e^{2r}|S-I|²dr ≥ 3, so R_γ ≤ -12. Strict inequality because |S(0)-I|² = 3 > 0. Equality requires g = dr² + e^{2r}q₀ with Ric(q₀) = 0 (flat on T³), contradicting R(q₀) = -6.

5. ASD OBSTRUCTION: For an ASD Einstein 4-manifold with Ric=-3g, reflection across a totally geodesic T³ reverses orientation, forcing W⁺ → W⁻. By analyticity, both vanish near T³, giving W=0 and constant sectional curvature -1. T³ cannot embed totally geodesically in H⁴ (Preissmann). Check whether the analyticity argument is correct.

6. THREE-OBJECT DISTINCTION: The center metric q₀ (at S=0, R(q₀)=-6) and conformal infinity γ (at r→∞, R_γ<-12) are at opposite ends. Imposing R(γ)=-6 as done in Step 76 Section 9 is not a necessary condition. The nonlocal datum g₃ (not γ) carries filling information.

Check each claim independently. Identify any sign errors, coefficient errors, or logical gaps.

## Output

# Verification Memo: PE expansion, normal identity, R_γ bound, ASD obstruction, three-object distinction

Session S0910A03 material, Steps 75–77. I independently recomputed each of the six items from the underlying geometry rather than checking internal consistency alone. Summary first, then the derivations and the few places needing a sharper statement.

**Overall:** all six items are correct. The Fefferman–Graham coefficients and signs (item 1), the mean-curvature limit (item 2), the Riccati normal identity (item 3), the R_γ < −12 result (item 4), and the ASD obstruction (item 5) all hold as written. The three-object distinction (item 6) is sound. Three points need more careful phrasing: the pointwise-versus-conformal-representative status of "R_γ < −12," the doubling/analyticity lemma underlying item 5, and one heuristic Taylor coefficient in Step 77 §7B.

---

## Item 1 — Fefferman–Graham shape operator: correct

I reconstructed the shape operator from the expansion. With ρ = e^{−r}, the ambient metric dr² + g_r has g_r = ρ^{−2}g_ρ, so

g_r = e^{2r}γ(I − B₂e^{−2r} + B₃e^{−3r} + O(e^{−4r})),  B₂ = γ^{−1}Sch(γ),  B₃ = γ^{−1}g₃.

Writing g_r = e^{2r}γ·M, the derivative combination 2M + M′ = 2I + 0·e^{−2r} − B₃e^{−3r} (the e^{−2r} term cancels exactly), giving g_r′ = e^{2r}γ(2I − B₃e^{−3r}). Then

S = ½ g_r^{−1}g_r′ = ½ M^{−1}(2I − B₃e^{−3r}) = I + B₂e^{−2r} − (3/2)B₃e^{−3r} + O(e^{−4r}).

This reproduces exactly S = I + Sch(γ)^♯ e^{−2r} − (3/2)γ^{−1}g₃ e^{−3r} + O(e^{−4r}). The signs and the coefficient −3/2 are right. The definition Sch(γ) = Ric_γ − (R_γ/4)γ in dim 3 is the correct Schouten tensor (P = (n−2)^{−1}(Ric − R/(2(n−1))γ) with n = 3 gives exactly this), and g_{(2)} = −Sch matches the standard PE convention where dr² + g_r is Einstein with Ric = −3g (total dim 4, face dim n = 3, so Ric = −ng with n = 3 — internally consistent). For odd face dimension n = 3 the expansion carries no log term and g₃ is the free transverse-traceless datum, consistent with the note's use of g₃ as the free filling datum. The data-file convention (B₂ = γ^{−1}g₂ = −γ^{−1}Sch, so −B₂ = Sch^♯) is internally consistent.

trace(Sch) = R_γ − 3·(R_γ/4) = R_γ/4 — matches the JSON entry.

## Item 2 — Mean curvature limit: correct

H = tr(S) = 3 + tr(Sch^♯)e^{−2r} − (3/2)tr(γ^{−1}g₃)e^{−3r} + O(e^{−4r}). Since tr(Sch^♯) = R_γ/4 and tr(γ^{−1}g₃) = 0 (TT), the e^{−3r} term vanishes and

H = 3 + (R_γ/4)e^{−2r} + O(e^{−4r}),  so e^{2R}(3 − H(R)) → −R_γ/4.

Correct. Note the first correction to H is O(e^{−4r}), so the limit is clean.

## Item 3 — Riccati and the normal identity: correct

For dr² + g_r with shape operator S = ½ g_r^{−1}∂_r g_r, the traced radial equation is H′ + |S|² = −Ric(∂_r,∂_r). With Ric = −3g, Ric(∂_r,∂_r) = −3, so H′ = −|S|² + 3. This uses only that the ambient Einstein constant is −3; it is dimension-robust here. Correct.

The algebra of the identity: |S − I|² = |S|² − 2H + 3 (three-dimensional face, tr I = 3). Then

d/dr[e^{2r}(3 − H)] = e^{2r}(6 − 2H − H′) = e^{2r}(6 − 2H + |S|² − 3) = e^{2r}(|S|² − 2H + 3) = e^{2r}|S − I|².

Integrating from r = 0, where S(0) = 0 gives H(0) = 0 and the starting value e⁰·3 = 3:

e^{2R}(3 − H(R)) = 3 + ∫₀^R e^{2r}|S − I|² dr. Correct.

This meshes with item 2 as an independent cross-check: the value −R_γ/4 comes from the expansion at infinity, while 3 + ∫ comes from integrating the Riccati out from the reflection face; their agreement is a genuine consistency test, both giving −R_γ/4 = 3 + ∫₀^∞ e^{2r}|S−I|² dr.

## Item 4 — R_γ < −12: correct

Convergence of ∫₀^∞ e^{2r}|S−I|² dr holds because near infinity S − I = Sch^♯ e^{−2r} + O(e^{−3r}), so the integrand ~ |Sch^♯|² e^{−2r}. Taking R → ∞: −R_γ/4 = 3 + ∫₀^∞ e^{2r}|S−I|² dr ≥ 3, hence R_γ ≤ −12. Strictness: at r = 0, |S(0) − I|² = |−I|² = tr(I) = 3 > 0, so the integrand is positive there and the integral is strictly positive, giving R_γ < −12.

The equality analysis is also correct. S ≡ I on (0,∞) forces g_r′ = 2g_r, i.e. g = dr² + e^{2r}q₀. For the warped product dr² + f²q₀ with f = e^r on a 3-dimensional face, the tangential Ricci is Ric_face − [ff″ + 2(f′)²]q₀ = Ric(q₀) − 3e^{2r}q₀; setting this equal to −3g = −3e^{2r}q₀ forces Ric(q₀) = 0, hence q₀ flat in dim 3, contradicting R(q₀) = −6. Correct. (This is a secondary confirmation; strictness already follows from |S(0)−I|² = 3.)

## Item 5 — ASD obstruction: correct, with one lemma to cite

The chain is valid. An orientation-reversing isometry exchanges the ±½-eigenspaces of the Hodge star on 2-forms, hence swaps W⁺ ↔ W⁻. The clean way to state the analytic step: form the double R×T³ by reflecting the r ≥ 0 metric across the totally geodesic T³. On r > 0 the ASD hypothesis gives W⁺ = 0; on r < 0 the reflected copy has W⁻ = 0. Because Einstein metrics are real-analytic in harmonic coordinates, W⁺ vanishing on the open half r > 0 forces W⁺ ≡ 0 on the connected double by unique continuation, and likewise W⁻ ≡ 0 from r < 0; together W ≡ 0. So the analyticity is used correctly as unique continuation **from an open set**, not from the T³ hypersurface — the note's phrase "extend to a neighborhood" reads loosely but the underlying mechanism is sound.

Then W = 0 with Ric = −3g in dim 4 gives constant sectional curvature R/(n(n−1)) = −12/12 = −1, so a locally hyperbolic neighborhood. A totally geodesic T³ inherits constant curvature −1 (Gauss equation, S = 0), impossible for π₁ = Z³ by Preissmann. Correct.

Two small notes:
- The Kulkarni–Nomizu statement "Rm = −g⊗∧g" has a factor-of-two convention slip (constant curvature −1 is Rm = −½ g⊗∧g), immaterial to the conclusion.
- The one genuine assumption is that the reflected double is C^∞ (hence analytic) Einstein across the T³ face. This is the standard reflection principle for Einstein metrics with a totally geodesic T³ (S = 0 gives C¹ matching, then elliptic bootstrap in harmonic gauge). It should be cited explicitly, since the entire item rests on it; without the analytic double there is no continuation and no contradiction.

Also worth recording: the item shows a reflected-center Einstein metric with Ric = −3g **must** carry W⁺ ≠ 0 and W⁻ ≠ 0 (non-ASD, non-SD). This is a real structural constraint on any reflected core, and correctly excludes using the Li–Liu ASD metrics directly as a filling. The Gauss-equation value R(q₀) = −6 used throughout also checks: R_face = R_M − 2Ric_M(n,n) = −12 − 2(−3) = −6 for the totally geodesic T³.

## Item 6 — three-object distinction: sound, with a representative subtlety

The conceptual point is correct: q₀ (induced metric on the T³ at r = 0, R = −6) and γ (conformal infinity at r → ∞) are data at opposite ends of the manifold, and the filling information beyond the conformal class is carried by the TT tensor g₃, not by the pointwise scalar curvature of γ. Imposing R(γ) = −6 has no justification. Step 76 §9 does conflate the reflection-face scalar with the conformal-infinity scalar; the Step 77 correction is right to separate them.

One point to state precisely so the argument is not misused. "R_γ < −12" is a statement about the specific representative γ that the center-anchored geodesic defining function ρ = e^{−r} induces (r normalized by S(0) = 0). The normal identity is pointwise along each normal geodesic, so it delivers R_γ(x) = −12 − 4∫₀^∞ e^{2r}|S−I|² dr < −12 pointwise for **that** representative. Scalar curvature is not conformally invariant, so a different conformal representative in [γ] can have a different scalar function. Consequently the sharpest reason Step 76 §9 is misposed is the conceptual one (q₀ and γ are different objects; the filling datum is g₃/[γ], not a scalar match), rather than a direct numerical clash "−6 vs < −12" — the latter is only a genuine contradiction if Li–Liu's q_∂ is literally the center-anchored representative γ, which requires the two defining functions to coincide. If Li–Liu's q_∂ is a different representative of [γ], its scalar could in principle be −6 without contradicting R_γ < −12 for the center-anchored γ. The correction survives either way, but the memo language should lean on the object distinction and the conformal-class/g₃ role, not on the pointwise number.

This also fixes γ's conformal class as one with Yamabe constant below zero (T³ has Yamabe invariant 0, attained only by flat metrics; a representative with scalar everywhere under −12 is non-flat, so the class sits strictly under zero), consistent with the note's "negative-Yamabe" usage.

---

## Minor items checked in passing

- Step 77 §2 remark integral: |S−I|² near r = 0 is 3 − 6r + O(r²) because d/dr|S−I|²|₀ = 2⟨S′(0), −I⟩ = −2 tr(S′(0)) = −2(R(q₀)+9) = −6. The leading contribution 3ε and strict positivity are right; the stated "3ε − 3ε²" is a loose evaluation (the e^{2r} weight actually cancels the linear term, giving 3ε − 2ε³ + …), immaterial to the point.
- Step 77 §7A/§7B: ∫₀^∞ e^{2r}|S−I|² dr = (−R_γ − 12)/4 follows directly from item 4. Correct.
- Step 77 §7B (7.2): |S′(0)|² ≥ 27 is right **given** the center theorem (eigenvalue ≤ −3, trace 3 ⇒ ∑λ² ≥ 9 + 18 = 27), not from Cauchy–Schwarz alone (which gives only ≥ 3). But the r² coefficient 27/2 in the expansion drops the tr(S″(0)) contribution (the true coefficient is |S′(0)|² − tr S″(0)), so that expansion is a heuristic lower estimate, not an inequality, unless tr S″(0) ≤ 0 is established. The note frames it as exploratory, which is appropriate.
- Twist-energy correction (0.1)/(9.5): the ¼p² coefficient being independent of e^{−φ} is the substance of the fix; I did not re-derive the SL(2,R)/SO(2) energy density by hand, and it rests on the script step76_matrix_twist_boundary.py. If this feeds a later stress-matching computation, an independent hand-check of (9.5) from U = e^{−φ/2}[[e^φ+A²,A],[A,1]] with A_z = ½e^φ p would be worth having on record, since it enters the off-diagonal twist channel that §9 opens.

## What remains unresolved (substance, not verification)

The verified identities constrain any reflected core sharply — pointwise R_γ < −12 on the center-anchored representative, the exact shear-integral identity (7.1), the eigenvalue floor λ_min S′(0) ≤ −3, and the exclusion of ASD fillings — but none of these produces or excludes an actual non-ASD, two-PE-ended, Ric = −3g metric on R×T³. The decisive missing object is exactly what Step 77 §7A names: existence (or its impossibility) of such a non-ASD filling whose backward evolution reaches S = 0 at finite distance, i.e. whether Φ:(γ,g₃) ↦ S(0) hits 0. The identities verified here are correct raw material for that intersection question; they do not yet resolve it.