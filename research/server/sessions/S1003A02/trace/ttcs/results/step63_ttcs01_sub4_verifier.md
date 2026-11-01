# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md"
  ]
}
```

## Task

Verify the Step-62/63 derivations on M = X#kCP̄² (X minimal general type, A = c1²(X), P = ∫|Ric°|², p = P/8π²). Check each with explicit conventions (AAD: |Ω|²=2, ∇Ω = a⊗φ − Ja⊗Jφ, s*−s=|∇Ω|²=4|a|², κ_J = s+6u with u=|a|², W2 = ½(ρ*''⊗Ω+Ω⊗ρ*''), γ_J = R(Ω) − a∧Ja). (1) Identity 62.1 and Theorem 62.A (step62 note §1–3). (2) Theorem 63.T: the general Gauss formula γ_J = R(Ω)+α∧β for an arbitrary orthogonal J with ∇Ω = α⊗φ+β⊗Jφ (sign, factor, gauge independence, that it represents 2πc1(J)), that R(Ω)^- = ρ0 with |ρ0|² ≤ |Ric°|²/2, the Hodge step ‖γ^-‖ ≥ 2π|c1^-|, the choice of class a_ε with |a_ε^-|² ≥ k+Π and existence of J with c1(J)=a_ε (Wu), and the Kähler-tariff reduction. (3) Proposition 63.AK: P = 2‖γ^-‖² + ∫u(5u+s) + 2∫|ρ*''|² + 4∫|W3|², including norms |W1|²=κ²/24, |W2|²=|ρ*''|², and the Sekigawa consistency check and the AK-Einstein consequences. (4) §3 emptiness of the 62.A equality locus: does LeBrun's Prop 2.4 equality plus Cauchy–Schwarz really force u constant; is N a section of a bundle with c2 = c2+2c1² = 5χ+6τ, and is 5χ+6τ = c2(X)+2A−k on M; the Taubes/Li–Liu period argument. (5) §4 model numbers: constant-torsion bound p ≥ (A−k)(2−3u)²/(u(4−3u)); the variance–slack relation ∫(u−ū)² = 8π²σ; the ASD-patch saturating configuration (υ=5k, patch volume 18π², ½∫u² = 4π²k, p=0) and the \overline{FPP} numerology; the two-ended AE neck bound P ≥ 32π². Report every error with the corrected statement, and say which conclusions survive.

## Output

# Verification memo: Steps 62–63 on M = X#kCP̄²

Conventions throughout are those of AAD: 2-form norm with |e¹∧e²| = 1 and |Ω|² = 2; Chern–Weil in the form P = 4∫|W⁺|² + ∫s²/12 − 8π²(2χ+3τ), which is LeBrun's (1) rearranged; and (2χ+3τ)(M) = A − k.

**What survives.**
- Identity 62.1, Theorem 62.A, Theorem 63.T, Proposition 63.AK and the §3 emptiness argument are correct. Only intermediate typos and one monotonicity range need fixing.
- The constant-torsion formula in 63 §4(A) is wrong. Its qualitative use survives once corrected.
- The ASD-patch numerology is internally exact. However, the saturating configuration is excluded outright by known rigidity, and the reason it is excluded points to a concrete wall identity.

---

## 1. Identity 62.1 and Theorem 62.A

**Identity 62.1.** At g̃ (s ≡ −4) we have ∫s² = 16V = 32π²(A+υ) and ∫|W⁺|² = (4π²/3)(A−2κ). Hence

P/8π² = **(2/3)**(A−2κ) + (A+υ)/3 − (A−k) = k − 4κ/3 + υ/3.

- The note writes "(1/6)(A−2κ)" as the first term. That is a typo: with 1/6 the sum does not produce the stated result. The final identity is correct.
- p(g) ≥ p(g̃) holds because W⁺ and the topological term are conformally invariant and ∫s² ≥ Y² in a class with Y < 0.
- Y < 0 holds because SW ≠ 0 with c₁⁺ ≠ 0 excludes Y ≥ 0.
- Cell check: κ = 3ω/4 = 0.056352, and 1 − 0.075136 + 0.070795 = 0.995659 ✓.

**(62.2).** Multiplying LeBrun's (10) by 9/4 gives ∫(s − √6|W⁺|)² ≥ 72π²(c₁⁺)².
- At s ≡ −4 the cross term is +2√6∫|s||W⁺|, so the Cauchy–Schwarz upper bound applies.
- With ‖s‖ = √(32π²(A+υ)) and √6‖W⁺‖ = √(8π²(A−2κ)), dividing by √(8π²) gives exactly 2√(A+υ) + √(A−2κ) ≥ 3√(A+Π) ✓.
- Expansion: with t = κ/A, y = √(1−2t) = 1 − t − t²/2 − t³/2 − …, one gets ((3−y)/2)² = 1 + t + 3t²/4 + …, so υ_L = κ + 3κ²/4A ✓.

**Theorem 62.A.**
- Direct substitution: (A/3)[((3−y)/2)² − 1] = A(1−y)/2 − κ/6. Hence p ≥ k − 3κ/2 + A(1−y)/2, which equals the stated L_A ✓.
- The expansion κ²/4A + κ³/4A² ✓.
- dL_A/dκ = −3/2 + 1/(2y), which vanishes at y = 1/3, i.e. κ = 4A/9. The value there is k − A/3 ✓. Since κ ≤ A/2 always, L_A is defined on the whole range.

**Checks (a)–(c).**
- (a) Kähler. Write ω = π*ω′ − Σe_iE_i. Then
  - c₁(M)·ω = c₁(X)·ω′ − Σe_i, so (c₁·ω)² = (K·ω′ + Σe_i)²;
  - K·ω′ ≥ 0 because K is nef and π*K·ω ≥ 0;
  - ω′² = ω² + Σe_i² > 0, so Hodge index gives (K·ω′)² ≥ Aω′² ≥ Aω².
  
  Hence κ ≤ 0. For κ < 0, (A−κ)² > A² − 2Aκ gives L_A > k ✓.
  
  Comparing complex structures (all have minimal model with c₁² = A) uses SW/Kodaira-dimension invariance. That is not needed for one fixed complex structure.
- (b) Cell: bound 0.9436 plus slack 0.052 gives 0.9956 ✓.
- (c) Formal mode: I re-expanded (2−3h)²/(2−h)² = 1 − 2h + h³/2, giving κ = k − k³/4A², υ = k + 3k²/4A + k³/2A², and p = k²/4A + k³/2A² = L_A(k,κ) through O(k³/A²) ✓.

**Correction in Cor. 62.B.** The note says "L_A is decreasing in κ for κ < 2A". The correct range is κ < 4A/9, because the sign of dL/dκ flips at y = 1/3. So 62.B needs k ≤ 4A/9 (κ_* ≤ k ≤ 4A/9). It then gives α ≥ 4π²(A − k − √(A²−2Ak)) ✓.

**Remaining §4–§5 algebra in Step 62.**
- 62.C: κ = (3k−3p+υ)/4, the equivalences (i)⇔(ii)⇔(iii), p ≥ k²/(4(1+β)A), and p ≥ k/(γ+1) all check.
- §5: the W⁻ reformulation (28/3), τ_ball = A/9, and the tariff c = 1 − (9/2)(1−λ) all check.
- Taubes thresholds: 62.G (κ_* ≤ k/2) forces k₀ ≥ A; 62.W forces k₀ ≥ A/2 ✓.

## 2. Theorem 63.T

**Frame equations.** Since |Ω| is constant, ∇Ω ∈ T*⊗Ω^⊥, so ∇Ω = α⊗φ + β⊗Jφ.
- Pairing ∇φ with Ω gives ⟨∇φ, Ω⟩ = −2α, so ∇φ = −α⊗Ω + b⊗Jφ ✓.
- Likewise ∇(Jφ) = −β⊗Ω − b⊗φ. At α = a, β = −Ja this is AAD (22) ✓.

**Curvature.** Use d^∇(θs) = dθ s − θ∧∇s. The Jφ-component of d^∇∇φ is then db + α∧β.
- The curvature side, i.e. the Jφ-component of [φ, R_{XY}], is purely algebraic in the oriented frame of Λ⁺. It is the same object AAD evaluate as −R(Ω) in (24); their derivation of that component never uses dΩ = 0.
- Hence −db = R(Ω) + α∧β, and at α = a, β = −Ja this reproduces AAD (25) ✓.

**Gauge independence.** Under φ′ = cosθ φ + sinθ Jφ:
- (α′, β′) = (cosθ α + sinθ β, −sinθ α + cosθ β), so α′∧β′ = α∧β;
- b′ = b + dθ, so db is unchanged.

**Chern class.** (Ω^⊥, J) ≅ K_J^{−1} under AAD's J-action on [[Λ^{0,2}]]. A U(1) connection with ∇e = i b e has curvature i db, so [−db] = 2πc₁(J) ✓.

**ASD part of R(Ω).**
- R(Ω)⁻ = ½Ric̃₀(Ω). Ric₀″ anticommutes with J (J Ric″ J = Ric″), so it drops out, and R(Ω)⁻ = Ric₀′∘J = ρ₀.
- The 2-form norm is half the tensor norm, so |ρ₀|² = ½|Ric₀′|² ≤ ½|Ric°|² ✓.

**Twist estimate.** Decomposable forms have |ψ^±| = |ψ|/√2. Also |∇Ω|² = 2(|α|² + |β|²) ≥ 4|α||β|. Hence |(α∧β)⁻| ≤ |∇Ω|²/(4√2), and 𝒯_J ≤ (1/4√2)‖∇Ω‖²_{L⁴}. This bound is scale-invariant ✓.

**Hodge step.** Pointwise ⟨ψ⁻, χ⁻⟩dμ = ½(⟨ψ,χ⟩dμ − ψ∧χ). Both integrals vanish for (H, dθ). So ‖γ⁻‖² ≥ 4π²|c₁⁻|². Combined with the triangle inequality and P ≥ ∫|Ric₀′|² ≥ 2‖ρ₀‖², this gives the theorem ✓.

**Choice of class.**
- a_ε² = A − k = (2χ+3τ)(M), and a_ε ≡ w₂ mod 2. By Hirzebruch–Hopf/Wu, a_ε = c₁(J) for an almost complex structure, which can be homotoped to be g-orthogonal.
- Averaging over ε kills the cross terms, so max_ε(a_ε⁺)² ≥ A + |c₁(X)⁻|² + Σ|E_i⁺|².
- With Π defined as that maximum minus A, |a_ε⁻|² = k + Π holds with equality.

**Readings.**
- (i) Kähler tariff: correct. Here J is the Kähler J, with c₁ = c₁X − ΣE_i, and Hodge index as in §1(a) gives (c₁⁺)² ≥ A directly. SW enters only if one quantifies over all complex structures.
- (iii) Cell: 2π(1 − √0.995663) = 0.01364 ✓.

**Addition to (iv): what the twist is.**
- 2α∧β is the pullback, under the section Ω: M → S²_{√2} ⊂ Λ⁺, of the vertical area form.
- So (63.1) is the twistor formula c₁(J) = [R(Ω)] + [vertical area]. 𝒯_J is the ASD part of the area swept by the Gauss map of J.
- Consequence: a rotation of Ω inside a fixed 2-plane of Λ⁺ (the Burns collar, ω → ζ) sweeps no area to leading order. In a near-parallel background, α∥β there, so α∧β = O(background ∇).
- The collar estimate 𝒯² ≲ (log 1/ε)^{−3} is therefore an upper bound that is not even approached. The flux must be carried by genuinely two-parameter rotations of J.

## 3. Proposition 63.AK

**Weyl norms.** W₁ has eigenvalues (κ/6, −κ/12, −κ/12), so |W₁|² = κ²/24. For Kähler metrics (κ = s) this matches LeBrun's s²/24 ✓. For W₂, W₂(Ω/√2) = (|ρ″|/√2)·ê, giving |W₂|² = |ρ_*″|² ✓.

**Self-dual part of γ_J.**
- R(Ω)⁺ = (κ/6 + s/12)Ω + ρ_*″.
- (a∧Ja)⁺ = (u/2)Ω, since a∧Ja is (1,1) with |a∧Ja| = u.
- Hence γ⁺ = (s/4 + u/2)Ω + ρ″ = ((s+s*)/8)Ω + ρ″.
- Sign check: ∫⟨γ⁺, Ω⟩ = 2πc₁·[Ω] reproduces Blair's ∫(s+s*)/2 = 4πc₁·[Ω]. The opposite sign would not.
- |γ⁺|² = (s+2u)²/8 + |ρ″|² ✓.

**The identity.** Substituting 8π²c₁² = 2‖γ⁺‖² − 2‖γ⁻‖² into Chern–Weil, and using the pointwise identity (s+6u)²/6 + s²/12 − (s+2u)²/4 = su + 5u² (re-expanded: the s² coefficient vanishes), gives (63.3) exactly ✓.

**Sekigawa.** At P = 0 and s ≥ 0 every term in (63.3) is nonnegative, so u ≡ 0 ✓. This is a valid four-line proof in dimension 4. Its novelty against Armstrong/Drăghici's integral formulas is still unchecked.

**AK Einstein.**
- |(a∧Ja)⁻|² = u²/2, so ‖γ⁻‖² = ½∫u².
- This gives ∫u(|s| − 6u) = 2∫|ρ″|² + 4∫|W₃|² and ∫|∇Ω|⁴ = 16∫u² ≥ 128π²|c₁⁻|² ✓.

**LeBrun barrier, now verified.** Take s = −4 and W₂ = W₃ = 0.
- Chern–Weil gives P = ∫(6u² − 8u + 4) − 8π²(A−k).
- (63.3) gives 2‖γ⁻‖² = ∫(2−u)² − 8π²(A−k).
- With ‖γ⁻‖² ≥ 4π²(k+Π) for c₁(J) in the best class, eliminating the volume gives p ≥ k + A·u(5u−4)/(2−u)². The minimum is at u = |s|/8 = 1/2, with value k − A/3 exactly.
- A sharper structural fact: since (s − √6|W⁺|)² = (6−3u)² = 9(2−u)², **LeBrun's Prop. 4 in this model is literally the Hodge flux bound ‖γ_J⁻‖² ≥ 4π²|c₁⁻|².**

## 4. §3: the 62.A equality locus is empty

**Equality forces u constant.**
- Equality requires equality in (10) at g̃. By LeBrun's Prop. 2.4, Ω then lies in the lowest eigenspace and W⁺ is J-invariant.
- J-invariance means W⁺ commutes with the J-rotation of Ω^⊥, so W₂ = W₃ = 0 and W⁺ = W₁.
- Cauchy–Schwarz equality makes |W⁺| = |κ_J|/√24 constant. With κ_J ≤ 0 and continuity, κ_J is constant.
- Since s is constant, u = (κ_J − s)/6 is constant ✓.

**Argument (a): Chern classes.**
- ∇Ω is a section of [[Λ^{0,1}⊗Λ^{0,2}]] ≅ T^{1,0}⊗K^{−1}. Conjugation does not change c₂.
- c₂(V⊗L) = c₂(V) + c₁(V)c₁(L) + c₁(L)², which gives c₂ + 2c₁² = 5χ + 6τ ✓ (consistent with AAD Lemma 2).
- On M: χ = c₂X + k and τ = (A − 2c₂X)/3 − k, so 5χ + 6τ = c₂(X) + 2A − k > 0 ✓.

**Argument (b): periods.** This is verbatim the last paragraph of LeBrun's Prop. 3.2.
- SW(a_ε ± 2E_i) ≠ 0 with b⁺ ≥ 2, so Taubes' SW ⇒ Gr gives a J-holomorphic sphere in ±E_i.
- Its area ±E_i·[Ω] is positive, which contradicts E_i⁺ = 0.
- Argument (b) alone suffices and does not need u constant.

Both arguments are correct. As the note says, they say nothing about stability.

## 5. §4 model numbers

**(A) The constant-torsion formula is wrong.** Model: AK, s = −4, W₂ = W₃ = 0, constant ū, B = A + υ. The exact relations are:
- p = B(3ū² − 4ū + 2)/2 − (A−k) (Chern–Weil);
- ‖γ⁻‖² = π²[B(2−ū)² − 4(A−k)] ((63.3));
- 𝒯² = π²Bū².

The flux bound gives B(2−ū)² ≥ 4(A+Π). Since p increases with B, the minimum is p_min = k + Aū(5ū−4)/(2−ū)². The twist adds p ≥ ¼(√(B(2−ū)² − 4(A−k)) − ū√B)₊².

The note's (A+υ)ū(4−3ū) ≥ 4(A−k) is not derivable from these relations. Its consequence p ≳ (A−k)/ū as ū → 0 contradicts the cscK blow-ups (Arezzo–Pacard), which have ū = 0 and p → k.

**Correct values.**
- At ū = 2/3 (ASD): p = B/3 − (A−k) with B ≥ 9A/4. So p = 0 is possible exactly when k ≤ A/4, at B = 3(A−k). There ‖γ⁻‖ = 𝒯, so ρ₀ = 0 is allowed. This is LeBrun's Thm 3.8 threshold.
- Formal mode: the torsion is ū = (2κ+υ)/(3A) ≈ k/A, not 2k/3A, which ignores the Yamabe excess. At LeBrun-extremal B the corrected model reproduces p = k²/4A + k³/2A² exactly.
- 63.T then gives p ≥ (√k − k/(2√A))² = k(1 − ½√(k/A))².

**So the exclusion of the diffuse formal mode as a p ≪ k AK state survives, with the constant ½ in place of ⅓.**

**(B) Patch configuration.** I rechecked all the numbers:
- ½∫u² = 4π²k;
- 36V − 20V_p = 72π²A gives υ = 5k;
- Chern–Weil gives P = 4V − (8/3)V_p − 8π²(A−k) = 0;
- κ = 2k;
- (63.3) gives ‖γ⁻‖² = 4π²k with ρ₀ = 0.

The variance relation ∫(u−ū)² = 8π²σ is just the definition σ = ¼A·Var(u). Its coefficient as the 62.A slack is not derived. A direct computation shows that ∫κ_J²/6 alone carries (3/2)B·Var(u) in p-units at fixed ū. The two must be reconciled by stating what is held fixed.

**The \overline{FPP} numerology is exact:** χ = 3, τ = −1, W⁺ = 0, Vol = 18π² at s = −4, form ⟨−1⟩. But two facts change its reading.

1. **The p = 0 configuration cannot be a smooth AK metric.**
   - With W₂ = 0 everywhere, Ω is an eigenform of W. At p = 0 the metric is Einstein, so Armstrong's theorem (LeBrun Cor. 2.5) makes it Kähler. That contradicts W⁺ = 0 on the patches.
   - More locally: if W₂ = W₃ = Ric″ = 0 and s is constant, then dρ = *(JδRic″) = 0, so A_Z = 0. AAD Cor. 1 (37) then reduces to d^J(κ − s) = 0, i.e. **du = 0**.
   - Any variation of torsion is therefore paid for by ρ_*″ or W₃ (which appear in (63.3)) or by Ric″ (which appears in P).
   - Equation (37) is the concrete local identity for question (Q1): it prices the u: 0 → |s|/6 wall.

2. **Where the joining cost is hidden.** The budget gives the Kähler region volume 2π²(A − 4k), i.e. Euler–signature A − 4k. A closed KE copy of X needs A. The missing 4 per class is exactly the connected-sum defect (2χ+3τ)(X#Y) = Σ − 4.
   - The two-ended AE neck bound is correct: 8π²(χ − 2) = ∫(|W|² + s²/24 − |Ric°|²/2) gives P ≥ 32π², i.e. 4 units of p. The η-term of round S³ vanishes, so there is no signature correction.
   - A degenerate X ⊔ k·\overline{FPP} with Euclidean necks therefore costs p ≥ 4k, which is worse than the Kähler tariff.
   - The integral model shows only that rational-cohomology inequalities alone cannot price the summand. Any low-cost competitor must be a fat, non-separated transition. Equation (37) shows such a transition necessarily switches on W₃, ρ_*″ or Ric″.

**Open source questions.**
- The SW connected-sum formula for b₁ = 0 negative-definite summands (needed for X#k\overline{FPP}) is plausible but uncited.
- Whether the bounds from 63.AK for AK Einstein metrics are new relative to Armstrong and Drăghici is unchecked.