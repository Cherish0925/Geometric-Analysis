# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Knowledge/objects/papers/math-0111228-Curvature-Connected-Sums-and-Seiberg-Witten-Theory--84e6ef833958--5b74c8864d85/object.md"
  ]
}
```

## Task

Verify Step 62 (workspace/notes/step62_weyl_channel_reduction.md) line by line. Setting: X minimal general type, A=c1^2(X), b+>=2, SW(X)!=0, M=X#kCP2bar, sign family a_eps=K+sum eps_i E_i are monopole classes, P=int|Ric°|^2, p=P/8pi^2. Check: (1) Identity 62.1 p(g~)=(k-kappa)+(upsilon-kappa)/3 with kappa=A/2-(3/8pi^2)int|W+|^2, upsilon=Y^2/(32pi^2)-A, via Chern-Weil 2chi+3tau=(1/4pi^2)int(2|W+|^2+s^2/24-|Ric°|^2/2), and P(g)>=P(g~) for the s=-4 Yamabe representative; check against the certified cell numbers in step48 note §2 (omega=4*0.018784, upsilon=4*0.053096 per class gives p≈0.99566). (2) The envelope 62.2 2sqrt(A+upsilon)+sqrt(A-2kappa)>=3sqrt(A+Pi) from LeBrun Prop 4 (Knowledge LeBrun object lines 145-149) and Cauchy-Schwarz; whether max_eps (a_eps^+)^2>=A is correct and Pi>=|K^-|^2+sum|E_i^+|^2. (3) Theorem 62.A L_A(k,kappa)=(k-kappa)+(1/2)(A-kappa-sqrt(A^2-2A kappa)) for kappa<=4A/9, including the elimination algebra, monotonicity, and the k-A/3 regime. (4) Kähler metrics have kappa<=0 (Hodge index on the Kähler cone of blow-ups), recovering the Kähler tariff. (5) Formal common mode expansions (kappa=k-k^3/4A^2, upsilon=k+3k^2/4A+k^3/2A^2, p=k^2/4A+k^3/2A^2) and that it lies on the equality locus to O(k^3/A^2). (6) Corollary 62.C equivalences and the resulting k^2/((4+4beta)A) bound and tariff k/(gamma+1). (7) The ASD reformulation for ball quotients (inf int|W-|^2 >= 28pi^2 k/3) and the tariff c=1-(9/2)(1-lambda). (8) The Gursky analogy (b+>0, Y>0 => int|W+|^2>=(4pi^2/3)(2chi+3tau)) and its per-point reading, and whether Conjecture 62.G is contradicted by anything standard (e.g. Taubes ASD metrics, known ASD metrics with b+>0, LeBrun estimates). (9) The claim that near a negative KE metric on X, KE is a local maximum of kappa among conformal classes (because negative KE is a local minimizer of int|W|^2 via the TT second variation of the Weyl functional), so the coupled inequality kappa<=beta p holds locally on X; state what formula for the second variation of int|W|^2 at Einstein metrics is needed. Report errors with corrected statements and say precisely what is new versus a direct rewriting of LeBrun's estimates.

## Output

# Verification memo: Step 62 (Weyl-channel reduction)

The mathematics of Step 62 is almost entirely correct. There are four substantive corrections:

- The restriction κ ≤ 4A/9 in Theorem 62.A is unnecessary.
- "L_A is decreasing for κ < 2A" is false.
- Corollary 62.D asserts more than the inequalities give.
- The KE-local-maximum statement in item (9) does not follow from the spectral facts supplied.

Two results are stronger than stated:

- The formal common mode lies **exactly** on the LeBrun envelope, not just to O(k³/A²).
- The local coupled inequality near a ball-quotient KE metric can be proved with an explicit constant, whatever the sign of the Weyl Hessian.

---

## 1. Identity 62.1 and the cell check

**Chern–Weil.** The formula 2χ+3τ = (1/4π²)∫(2|W⁺|² + s²/24 − |Ric°|²/2) gives P = 4∫|W⁺|² + (1/12)∫s² − 8π²(2χ+3τ). Each CP̄² summand changes χ by +1 and τ by −1, so (2χ+3τ)(M) = A − k. At g̃ (s ≡ −4) we have ∫s² = 16V = Y², so ∫s² = 32π²(A+υ) and υ = (V − 2π²A)/2π².

**Typo.** The intermediate line "p = (1/6)(A−2κ) + …" is wrong. The coefficient is 4·(4π²/3)/(8π²) = **2/3**. The correct computation is

  p = (2/3)(A−2κ) + (A+υ)/3 − A + k = k − 4κ/3 + υ/3,

so the boxed identity is right.

**P(g) ≥ P(g̃).** ∫|W⁺|² is conformally invariant and χ, τ are topological, so P(g) − P(g̃) = (∫s²_g − Y²)/12. The inequality ∫s²_g ≥ Y² in a class with Y < 0 is the Besson–Courtois–Gallot/LeBrun fact quoted in Ishida–LeBrun Prop. 12: constant-s metrics minimise the L² norm of s in such a class.

**Cell numbers.** These are consistent with Step 48 §2:

- δW = 0.018784·8π² gives κ = 3δW/8π² = 0.056352, and ω = 4κ/3 = 0.075136.
- υ = ΔV/2π² = 4·0.053096 = 0.212384.
- p = 1 − 0.075136 + 0.070795 = 0.995659.
- Step 48 gives 1 − P(ĝ)/8π² = 0.0043391, i.e. p = 0.9956609. The quoted "interval value" 0.9956627 differs from this by 1.8·10⁻⁶. Both are within the ±2·10⁻⁶ that comes from 6-digit inputs multiplied by 4.
- Step 48's (Y0) in these variables reads 1 − p = 4κ/3 − υ/3, which is 62.1 at k = 1. The two notes agree.

## 2. Envelope 62.2

**Sign family.** The minimum of the averaged quantity in Corollary 11 is achieved. Averaging over ε gives

  E_ε |a_ε⁻|² = |K⁻|² + Σ|E_i⁻|²  and  |E_i⁻|² = 1 + |E_i⁺|²   (from E_i² = −1).

With a_ε² = A − k this yields max_ε (a_ε⁺)² ≥ A + |K⁻|² + Σ|E_i⁺|². So Π ≥ |K_X⁻|² + Σ|E_i⁺|² is correct, and Corollary 11's (a⁺)² ≥ A is recovered. The inputs are b⁺ ≥ 2, SW(X) ≠ 0 and the blow-up formula.

**Prop. 2.** At g̃, Prop. 2 gives 32π²(A+υ) ≥ 32π²(A+Π), i.e. υ ≥ Π.

**Prop. 4.** The step used is the pointwise inequality |s − √6|W⁺|| ≤ |s| + √6|W⁺| followed by Minkowski. This holds for any metric; "s < 0 somewhere" plays no role. At g̃:

- ‖s‖₂ = √(32π²(A+υ)),
- √6‖W⁺‖₂ = √(8π²(A−2κ)),
- √(72π²(A+Π)) on the right.

Dividing by √(8π²) gives 62.2 exactly.

**Equality.** It requires Prop. 4 equality, Minkowski equality (|W⁺| ∝ |s| a.e., hence |W⁺| constant at g̃) and Π = 0. M is symplectic, so Prop. 4's strictness clause does not exclude this.

## 3. Theorem 62.A

**Elimination algebra.** It is correct. Using y² = 1 − 2κ/A:

- υ_L = A[((3−y)/2)² − 1] = (3A/2)(1−y) − κ/2;
- p ≥ k − 4κ/3 + υ_L/3 = k − 3κ/2 + (A/2)(1−y) = L_A.

The expansion is υ_L = κ + 3κ²/4A + **3κ³/4A²** + …; the cubic coefficient is needed in §5 below.

**Monotonicity (correction).** The derivative is ∂_κ L_A = −3/2 + 1/(2y). So L_A **decreases for κ < 4A/9 (y > 1/3) and increases on [4A/9, A/2]**. The domain is κ ≤ A/2, because ∫|W⁺|² ≥ 0. The statement in 62.C that "L_A is decreasing in κ for κ < 2A" is false and should read "for κ ≤ 4A/9".

**Hypothesis κ ≤ 4A/9 (correction).** The derivation never uses it, so **Theorem 62.A holds for all κ ≤ A/2**. Its global minimum is L_A(k, 4A/9) = k − A/3, LeBrun's unconditional bound, and on [4A/9, A/2] the theorem is stronger than k − A/3 (L_A = k − A/4 at κ = A/2).

**A cleaner universal corollary.** Since A − κ − Ay ≥ 0 ⇔ κ² ≥ 0,

  **p(g) ≥ k − κ[g] for every metric** (with κ²/4A + κ³/4A² + … to spare).

This is the form all later corollaries actually use.

**Cell check (b).** It reproduces: L_A ≈ 0.9437, the slack is p − (k−κ) = 0.0520, the efficiency is κ/υ = 0.265, and the ratio of spent to required Yamabe excess is 3.77.

## 4. Kähler metrics: κ ≤ 0

The argument is right, with one repair: the push-forward of a Kähler class need not be Kähler.

- **Setting.** By Seiberg–Witten invariance of the minimal model, a complex structure on M is a blow-up of a minimal general-type X′ with c₁²(X′) = A. Write [ω] = π*β − Σe_iE_i with e_i = ω·E_i > 0.
- **Repair.** Here β = π_*[ω] is only known to satisfy β² = ω² + Σe_i² > 0 and β·C > 0 on curves. Hodge index needs only β² > 0, together with K·β > 0 (K nef and big, same light-cone component).
- **Inequality chain.** K_M·ω = K·β + Σe_i ≥ K·β > 0 and ω² ≤ β². Hence

  (K·ω)²/ω² ≥ (K·β)²/β² ≥ K² = A,

  so ∫|W⁺|² = ∫s²/24 ≥ (4π²/3)A, i.e. κ ≤ 0.
- **Simplification.** The Kähler tariff then needs only 62.1 and υ ≥ 0: p(g̃) = k − 4κ/3 + υ/3 ≥ k. Prop. 4 is not used.
- **cscK identity.** For a cscK metric (its own Yamabe representative), |W⁺|² = s²/24 gives κ = −υ/2 exactly, so **p = k + υ** with υ = (K·ω)²/ω² − A. This makes the Arezzo–Pacard recovery p → k as e_i → 0, β → K quantitative.
- **Corollary.** Scalar-flat Kähler (ASD) metrics cannot exist on these blow-ups, since ∫s = 4π c₁·ω < 0. ASD metrics here must be non-Kähler, which is relevant to item (8).

## 5. Formal common mode: exact, not asymptotic

With h = k/A, the exact values are:

- **Weyl deficit:** κ = 4Ah(1−h)/(2−h)² = k − k³/(2A−k)².
- **Yamabe excess:** υ = Ah(4−h)/(2−h)² = k + 3k²/4A + k³/2A² + ….
- **Einstein defect:** p = Ah²(1+h)/(2−h)² = **k²(A+k)/(2A−k)²**. This agrees with Step 48's 1 − p/k = (4−5h)/(2−h)².

Both √ terms of 62.2 are exact: 2√(A+υ) = 4√A/(2−h) and √(A−2κ) = √A(2−3h)/(2−h). Their sum is

  √A(6−3h)/(2−h) = 3√A.

So **62.2 holds with equality for all h, with Π = 0**, hence υ = υ_L(κ) and p = L_A(k,κ) exactly. The O(k³/A²) matching of the note is an artefact of truncation; the cubic coefficients (−1/4 + 3/4 = 1/2) confirm it at that order.

Also κ_formal < k strictly. In 62.C the formal mode therefore satisfies (i) with β = 0 strictly, with slack k³/(2A−k)². It does not saturate it. L_A(k,k) < p_formal, as the note says.

## 6. Corollaries 62.B, 62.C, 62.D

**62.B.** It is correct but needs **k ≤ 4A/9** for the monotonicity step. For larger k the bound is k − A/3. The tariff statement "κ_* ≤ (1−c)k ⇒ p ≥ ck" follows from p ≥ k − κ, for every k.

**62.C.**

- **Equivalences.** κ = (3k − 3p + υ)/4 from 62.1. Then (i) ⇔ (ii) with γ = 3 + 4β. Using ∫|W⁺|² = (4π²/3)(A − 2κ), (i) ⇔ (iii). Throughout, p and P mean p(g̃) and P(g̃).
- **Coupled bound.** p ≥ −βp + (k+βp)²/4A ≥ −βp + k²/4A, giving p ≥ k²/(4(1+β)A). This requires k + βp ≤ 4A/9.
- **Linear version.** It is correct via p ≥ k − κ: p(1 + (γ−3)/4) ≥ k/4 ⇒ p ≥ k/(γ+1).

**62.D (correction).** The inequalities force only κ ≥ k − p, i.e. liminf κ/k ≥ 1. They do not force κ/k → 1.

- If κ > k, then L_A = (k−κ) + κ²/4A + … can vanish (for instance at κ ≈ k + k²/4A when k ≪ A) or become as low as k − A/3. So p/k → 0 is compatible with κ/k bounded away from 1 above.
- The decomposition 62.1 has two nonnegative terms only when κ ≤ k. Only on that branch do υ − κ ≤ 3p and (linearising 62.2) Π ≲ (2/3)(υ − υ_L) ≤ 2p follow.

The correct statement is a dichotomy. A family with p/k → 0 either

- has κ > k, removing more than 8π²/3 of W⁺-energy per summand; or
- satisfies κ = k − O(p), υ − κ ≤ 3p and Π = O(p), the LeBrun-extremal structure.

The Taubes period obstruction addresses only the second branch. Lemma T is not in the supplied files and cannot be checked here.

## 7. ASD reformulation

- **Hypothesis.** With ∫|W⁺|² − ∫|W⁻|² = 12π²(τ_X − k), the hypothesis of 62.B becomes ∫|W⁻|² ≥ (4π²/3)(A − 9τ_X) + (28π²/3)k.
- **Ball quotients.** For them τ = (c₁² − 2c₂)/3 = A/9, so the bound is (28π²/3)k = (7/9)·12π²k.
- **Tariff.** ∫|W⁻|² ≥ 12π²λk gives δW ≤ 12π²(1−λ)k, so κ ≤ (9/2)(1−λ)k and c = 1 − (9/2)(1−λ). Thus c > 0 exactly when λ > 7/9; the phrase "λ > 7/9 + (something)" should be dropped.
- **Trivial signature bound.** λ = 0 gives κ ≤ 9k/2.
- **Per-class values.**
  - FS CP̄² and Burns: 12π², since Burns compactifies conformally to CP̄².
  - Certified cell: (12 − 0.150)π², because δW = 0.15027π².
  - Formal mode: 28π²/3 to leading order.

## 8. Gursky analogy and Conjecture 62.G

**Normalisation.** With b⁺ > 0 and Y > 0, ∫|W⁺|² ≥ (4π²/3)(2χ+3τ). This normalisation is consistent: positive KE has ∫|W⁺|² = ∫s²/24 = (4π²/3)(2χ+3τ). The per-summand allowance is 4π²/3, which is half of the 8π²/3 required.

**"Nearly sharp" (correction).** This reading is not supported by the cited examples. On CP²#kCP̄², 2χ+3τ = 9 − k, so Gursky's bound is vacuous for k ≥ 9. The Kim–LeBrun–Pontecorvo and Rollin–Singer scalar-flat Kähler metrics have **Y = 0**, so they lie outside Gursky's hypothesis. ASD metrics with Y > 0 cannot exist there at all, since b⁺ = 1. These examples show only that ∫|W⁺|² reaches 0 near k ≈ 9–10, consistent with the per-point count 12π²/(4π²/3) = 9. They do not test Gursky's constant in the Y > 0 class.

**Status of 62.G and 62.W.** Nothing standard contradicts them.

- **Taubes.** M#nCP̄² admits ASD metrics for n ≥ n₀(M), with n₀ not explicit. The conjectures predict n₀ ≥ A (62.G) or n₀ ≥ A/2 (62.W) for these X.
- **Kähler metrics.** κ ≤ 0 and no Kähler ASD metrics (§4).
- **LeBrun's Prop. 4 at W⁺ = 0.** It gives only ∫s² ≥ 72π²A, hence P ≥ 8π²(k − A/4). This is compatible with ASD metrics existing.
- **Ishida–LeBrun Theorem C.** Gluing KE X to an ASD summand gives κ → 0, which is consistent.

Taubes' theorem with SW ≠ 0 shows that no k-independent pure-W⁺ bound can come from Seiberg–Witten. That supports the note's structural point. A further consequence: if 62.G holds, even approximate realisation of the formal mode, whose κ ≈ k exceeds k/2, is excluded. Under 62.W alone it is not.

## 9. Local behaviour near the KE metric on X (k = 0)

### Hessian formula

On TT tensors at an Einstein metric with Ric = λg, two facts hold in tensor norms:

- 32π²χ = ∫(|W|² − 2|Ric°|² + s²/6);
- s′ = 0 and (Ric°)′ = ½(Δ_L − 2λ)h.

The Hessians of the two remaining terms are:

- Hess∫|Ric°|² = ½‖(Δ_L − 2λ)h‖²;
- Hess∫s²dμ = −4λ⟨(Δ_L − 2λ)h, h⟩. The gradient of ∫s² is 2∇²s − 2(Δs)g − 2s Ric + (s²/2)g; linearising it at Einstein gives −4λ(Δ_L − 2λ)h.

Combining them:

  **Hess∫|W|²(h,h) = ∫⟨(Δ_L − 2λ)(Δ_L − 4λ/3)h, h⟩**, and Hess∫|W⁺|² = ½·Hess∫|W|² (τ is topological).

**Check on hyperbolic 4-manifolds** (λ = −3). The Codazzi identity ‖∇h‖² = ‖d^∇h‖² − λ‖h‖² + ⟨R̊h,h⟩ on TT gives ∇*∇ ≥ 4. The formula becomes (∇*∇ − 2)(∇*∇ − 4) ≥ 0, vanishing exactly on Codazzi TT tensors. These are the infinitesimal conformally flat deformations, as W ≡ 0 requires.

**General form.** Using R̊ = W̊ − λ/3 on traceless tensors, ⟨(Δ_L − 4λ/3)h, h⟩ = ‖d^∇h‖² − ⟨W̊h, h⟩.

### Ball quotient X₀

Take Ric = −6 and L = ½(Δ_L + 12) as in Step 48. Then Δ_L − 2λ = 2L, Δ_L − 4λ/3 = 2L − 4, and Hess∫|W|² = 4⟨L(L−2)h, h⟩.

A direct computation with holomorphic curvature −4 gives:

- R̊ = 4 on J-anti-invariant traceless tensors (e.g. h = e₁² − e₂², R̊h(e₁,e₁) = −sec(e₁,Je₁) = 4);
- R̊ = −2 on J-invariant ones.

Consequences by sector:

- **J-invariant TT** corresponds to (1,1)-forms, Δ_L ↔ Δ_d ≥ 0, so L ≥ 6 and the Hessian is positive.
- **J-anti TT** (complex-structure directions): 2L = ‖d^∇h‖²/‖h‖² + 2, so the Hessian is negative exactly on eigentensors with 1 ≤ L < 2.

Prop. 48.3 gives only L ≥ 1. **KE is a local maximum of κ among conformal classes iff L ≥ 2 on J-anti TT**, equivalently ‖d^∇h‖² ≥ 2‖h‖² there. This is a Calabi–Vesentini-type spectral gap for the Θ-valued ∂̄-Laplacian, and it is not established by the supplied material.

For general-type KE with H¹(Θ) ≠ 0, the Hessian vanishes along Einstein deformations. Any J-anti eigenvalue 0 < 2L < 4 makes κ > 0 nearby, so local maximality fails unless that gap holds. Statement (9) as written is therefore unproved.

### Coupled inequality, independent of the sign

To second order on the TT slice (switching to LeBrun's Λ²-norm, |W|²_tensor = 4|W|²_End):

- κ = (3/32π²)⟨L(2 − L)h, h⟩;
- p = ‖Lh‖²/8π² (P(g̃) − P(g) = O(h⁴));
- υ = (3/4π²)⟨Lh, h⟩, from Hess∫s² = 48⟨Lh,h⟩.

These satisfy 62.1 with k = 0 identically, and are consistent with υ ≥ 0 and υ ≥ υ_L. Since ⟨Lh,h⟩ ≤ ‖Lh‖² when L ≥ 1,

  **κ ≤ (3/4)p + O(‖h‖³)** near the KE ball quotient, with p ≳ ‖h‖² by the Koiso gap.

This proves 62.C(i) locally on X with β = 3/4, which answers §6(b) of the note. It strengthens to κ ≤ 0 exactly when L ≥ 2 on J-anti TT. Extending this to M = X#kCP̄² needs the cell analysis and is not addressed.

## 10. What is new and what is a rewriting of LeBrun

**Direct rewritings.**

- 62.1 is Chern–Weil plus definitions; it is Step 48's (Y0) in the variables (κ, υ).
- 62.2 is Prop. 4 + Minkowski, with Π from Corollary 11's averaging and υ ≥ Π from Prop. 2.
- Theorem 62.A is the optimal consequence of Props. 2 and 4 at fixed κ. Its global minimum is LeBrun's k − A/3, and its content is p ≥ k − κ.
- The Kähler case (§4) does not need Prop. 4.

**Genuinely new.**

- κ_* is identified as the single conformal invariant governing the open-range lower bound (62.B/C, with the corrected ranges).
- The formal mode is exactly LeBrun-extremal, with closed form p = k²(A+k)/(2A−k)².
- The cscK identity p = k + υ.
- The corrected dichotomy in 62.D.
- The ASD restatement with λ > 7/9 for ball quotients.
- Conjectures 62.G/62.W, which are consistent with all standard results and predict explicit Taubes thresholds.
- The second-order KE computation: κ ≤ (3/4)p locally, and local maximality of κ reduced to the gap L ≥ 2 on J-anti TT.

**Not checkable from the supplied files.** Step 61's envelope, Step 36's t = c/9, Lemma T, and the "(5/6)" constant of §6.2.