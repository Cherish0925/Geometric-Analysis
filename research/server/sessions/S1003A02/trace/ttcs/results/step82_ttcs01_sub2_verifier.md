# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Skills/geometric-analysis/research/supplements/20261007-einstein-gaps/five_research_problems.tex",
    "Sessions/S1003A02/workspace/notes/step54_k1_ball_quotient_attainment_theorem.md"
  ]
}
```

## Task

Read the final section §24 (and §24.0 L1/L2, §23.6) of Sessions/S1003A02/workspace/notes/theorem_package_v1.md as a research geometer checking every statement against (a) the earlier package sections it cites (§§1, 3.3-3.7, 13-17, 20, 21.10-21.11, 22) and (b) the original problem statements in five_research_problems.tex §§1-3 (Problems 1-3: Einstein existence on X#k CPbar^2 for 1<=k<A/3; exact P_*; a smooth non-Bach-flat global P-minimizer). For each statement in §24 decide whether (i) it is correctly tagged [I]/[P]/[C]/[O], (ii) its quantifiers match the cited source (which X, which k, which metrics, which hypotheses), (iii) the derivation is correct. Specific items to check with care: the L1 equivalence Einstein <=> alpha=0 attained <=> P_*=0 attained on X#kCPbar^2 and what Seiberg-Witten/Yamabe input it needs (b+ conditions); the L2 bound D(g) >= p/(p+3T_+/4) from C_+ = T_+ + p and the derived band bound alpha >= 4(3k-A)/(3k+5A) for A/3<=k<=A; the regime summary in 24.2(4); the Problem-3 discussion: whether k>=A/3 blow-ups really satisfy both hypotheses of Prop. nonbach unconditionally, whether the real-hyperbolic blow-up scalar-flat exclusion argument (no PSC on connected sums with aspherical 4-manifolds + Cheeger-Gromoll) is sound, and whether Theorem H (conditional non-attainment) is quoted correctly; the k=1 conditional dichotomy 'negative Problem 1 => positive Problem 3' from Theorem 54.A including whether A>=9 for ball quotients is right and what configurations remain; the 'three ends' paragraph (does p->0 force approach to the Einstein end of p=q^2(1-delta)^2+L, is q bounded below, and are the aligned/cscK ends correctly described as obstacles to coercive estimates rather than escape routes); the statement that 1/3 is simultaneously the zero of LeBrun's P bound and the sign change of the fixed-Kahler Weyl deficit, and its explanation by KE saturation; and the claim that every known attained alpha-minimizer is Bach-flat. Report concrete corrections with exact replacement wording, any statement that is false or overstated, and any important inherited or proved result from the package that §24 omits but that belongs in a complete statement of Problems 1-3. Do not invent literature; if a claim needs an outside source (e.g. no-PSC for connected sums with aspherical manifolds, LeBrun's Yamabe computation for b+=1), name the exact knowledge_request needed.

## Output

# Verification of §24 (with §24.0 L1–L2 and §23.6) of `theorem_package_v1.md`

## Summary

Most of §24 is correct as written. The following points need repair; each is worked out in the numbered sections below.

1. **KE "saturation" explanation of the 1/3 wall (§24.4).** This explanation is mathematically false, and §3.6–3.7 of the package already contradicts it. Detail in §5.
2. **"C₊ ≥ A would suffice" (§24.1 and §20.7).** The inequality C₊ ≥ A is false for arbitrary metrics. Detail in §2.4.
3. **The k=1 dichotomy (§24.3).** The direction "a nonexistence answer to Problem 1 yields Problem 3" ignores the exotic-cap case, where the minimizer lives on V ≠ M. Detail in §3.4.
4. **Theorem H.** It is quoted with a concentration statement that the source does not prove. Detail in §3.3.
5. **"One unknown" (§24.2(5)).** The capacity Θ\* decides the band question, not open-range positivity. Detail in §2.6.
6. **The "three ends" paragraph.** It is partly tautological. Its obstruction statements are established on products of curves, not on M. Detail in §4.
7. **Seiberg–Witten / Yamabe inputs.** These are used throughout §24 without the b⁺(X)=1 case being sourced. Detail in §1.

Several package results that belong in a complete statement of Problems 1–3 are absent from §24; they are listed in §6.

---

## 1. §24.0 — L1 and L2

### L1: Einstein ⟺ α=0 attained ⟺ P\*=0 attained

**Logic.**
- P = 0 ⟺ Einstein, by the contracted Bianchi identity. So "P\*=0 attained ⟺ Einstein of any sign" needs no input.
- α=0 attained ⟺ Einstein with λ≠0 (§22.4). Ricci-flat metrics have ℰ = 4.
- The chain therefore needs exactly one extra fact: **M carries no Ricci-flat metric.**

L1 uses Y(M) = −4π√(2A) < 0. This is stronger than necessary. It suffices that M has no PSC metric and no Ricci-flat metric. Y < 0 also excludes λ > 0 Einstein metrics, which are irrelevant to L1.

**Inputs and their status.**
- For b⁺(X) ≥ 2, Y(M) < 0 follows from LeBrun's estimate ∫s² ≥ 32π²(c⁺)² for every metric. This uses chamber-independent nonzero invariants of the classes ±K_X ± ΣE_i (§3.6 quantifiers).
- For b⁺(X) = 1 (Godeaux-type surfaces, fake projective planes), the package itself records "b⁺=1 keeps its chamber input" (§3.6, §3.7). §24 never sources that input.
- **knowledge_request:** the exact statement and hypotheses of LeBrun's computation Y(X#kCP̄²) = −4π√(2c₁²(X)) for minimal general-type X with b⁺(X) = 1. Candidate sources: LeBrun, *Kodaira dimension and the Yamabe problem*; LeBrun 2001, Prop. 3.2 and its b⁺=1 discussion. The request should state which theorem covers b⁺=1 and with which chamber argument.

**Replacement tag.** "[P] given Y(M)<0; Y(M)<0 is [I] for b⁺(X)≥2 and [I, pending source] for b⁺(X)=1."

**Missing equivalence.** On these M, positivity of α and positivity of P\* are the same question.
- §1.3 / §22.1 give α ≤ 4𝔭\*/(A+𝔭\*), using the same Y² ≥ 32π²A supply.
- L2 gives α ≥ 𝔭\*/(𝔭\* + ¾T₊) with T₊ = A−k > 0.

Together:

> **α(M)=0 ⟺ P\*(M)=0, and α(M)>0 ⟺ P\*(M)>0, for 1 ≤ k < A.**

This belongs in L1. It says the two functionals share the zero question and the attainment-at-zero question, and differ only in values and in their minimizing conformal classes.

### L2: algebra checked, it is correct

- From the T₊ Chern–Weil identity: (1/2π²)∫|W⁺|² = T₊ − S/(96π²) + 𝔭. Hence C₊ = T₊ + 𝔭.
- Dropping W⁺ ≥ 0 gives S ≤ 96π²(T₊+𝔭). Hence R = P + S/4 ≤ 8π²(4𝔭 + 3T₊).
- Then ℰ ≥ 𝒥 = 4P/R ≥ 𝔭/(𝔭 + ¾T₊). The case R = 0 gives ℰ = 4, consistent with the bound.
- The right side is increasing in 𝔭 for T₊ > 0.

The band bound: inserting 𝔭\* ≥ k − A/3 gives

(k − A/3)/(k/4 + 5A/12) = 4(3k−A)/(3k+5A).

It equals 0 at k = A/3 and 1 at k = A, as stated.

**Tag.** The first inequality is pure Chern–Weil ([P], every closed M with T₊ > 0). The boxed band bound inherits the SW input of LeBrun's 𝔭\* ≥ k − A/3, so it carries the same b⁺ qualification as L1. State this explicitly.

---

## 2. §24.1 and §24.2

### 2.1 Status line for k ≥ A/3

The status line is correct as [I], with the b⁺ qualification of §1.

The N1 window (1/3 − ε)A < k < A/3 is quoted correctly from `five_research_problems.tex` (blowgap)–(threshold). Two quantifier points:
- ε is the N1 constant and is not explicit.
- The window contains an integer k only when εA > 1. This is why the X_d examples require A_d ≥ 2/ε.

### 2.2 Item (1): α ∈ [0,1)

The ADE restriction is unnecessary. Theorem 69.KE gives α < 4k/(A+k) for **every** minimal general-type X, with ADE/Kronheimer localization included (§22.3(a)). Moreover 4k/(A+k) < 1 ⟺ k < A/3.

**Replacement.** "For every minimal X of general type and 1 ≤ k < A/3, 0 ≤ α < 4k/(A+k) < 1 (Theorem 69.KE; uses the per-class supply Y² ≥ 32π²A)."

### 2.3 Item (2): "No topology-only obstruction can work"

This is false as phrased.
- §3.3 is a topology-only (homological entropy) Einstein obstruction on real-hyperbolic blow-ups.
- LeBrun's k ≥ A/3 theorem is topology plus SW.

What 59.KE refutes is narrower: any argument that proves P ≥ 8π²k (a per-class tariff of 8π²). Since P\*(M) < 8π²k, such an argument cannot exist. Nonexistence via P\* > 0 remains possible.

The certified cell enclosure applies only to CH-collared cells, i.e. ball-quotient hosts. It does not apply to every X.

**Replacement.**
> "No per-class tariff P ≥ 8π²k holds for any minimal X of general type and any k ≥ 1 (59.KE). For ball-quotient hosts, CH-collared cells cost 𝔭 ∈ [0.99566273275, 0.99566273278] per class (§4.3). An Einstein obstruction in 1 ≤ k < A/3 must therefore come from the exact equation or the actual fields, not from a per-class charge of 8π²."

### 2.4 Item (3) and "What a solution must control"

**The phrase "on the exceptional classes Eᵢ, |Eᵢ⁻| ≥ 1".** It is true, since |Eᵢ⁻|² = 1 + |Eᵢ⁺|². But it is misattached. Eᵢ is not c₁ of any almost-complex structure, because Eᵢ² = −1 ≠ A−k. The class entering 63.T is a = c₁(J) = ±K_X ± ΣEᵢ.

**Replacement.**
> "for the best-sign class a, |a⁻|² = |a⁺|² − (A−k) ≥ k + Π."

**Stronger statement available.** By §21.9, at an Einstein metric ρ₀ᴶ = B_gΩ = 0. Hence the **harmonic part of t_J⁻ equals 2πh_a⁻ exactly**, not merely ‖t_J⁻‖ ≥ 2π|a⁻|.

**C₊ ≥ A.** Since C₊ = A − k + 𝔭, the inequality C₊ ≥ A is equivalent to P ≥ 8π²k. That is refuted for every X by 59.KE. Saying C₊ ≥ A "would suffice" is therefore false; the same error appears in §20.7.

**Replacement.**
> "The unrestricted inequality C₊ ≥ A is false (equivalent to P ≥ 8π²k, refuted by 59.KE); it holds on Kähler metrics (§3.5). What nonexistence requires is C₊ > T₊ = A−k at every metric, i.e. P > 0."

### 2.5 Items (4)–(5)

**Item (4).** It is correct. The α-reading also needs the two hypotheses of 52.9: a nonzero orbifold Einstein constant and vanishing scalar variance. These are stated in §13 but should be repeated in (4).

**Item (5).** It is correct.

### 2.6 §24.2

**(1) Correct, with hypotheses.** The second-order term is valid only on a P-critical background on B₂ρ(p) (Theorem 59.R). The Φ formula shown is the eigenvector form with optimal corrector (57.Φ).

Replacement for the price formula:
> "𝔭_cell = 1 − x₀R⁺(ζ,ζ) + O(x₀^{6/5}) for every bulk (Theorem F). If the bulk is P-critical near p and ζ is an R⁺_p-eigenvector, then 𝔭_cell = 1 − x₀μ₁ + (Φ/2)x₀²log(1/x₀) + O(x₀²) (59.R, 57.Φ)."

The KE value Φ/2 = −s²/64 matches 59.KE.

**(2) "Realized only by non-Kähler geometry" is overstated.** P\* is not known to be realized at all. K∞ covers only the blow-up complex structure.

Replacement:
> "Every metric with P < 8π²k is non-Kähler for the blow-up complex structure, and for every orientation-compatible complex structure on M if each such structure is a k-fold blow-up of a minimal general-type surface with c₁² = A."

**knowledge_request:** the smooth invariance of the minimal model and of c₁² for complex structures on X#kCP̄². The candidate source is the Friedman–Morgan / SW-basic-class theorem; the request should give the exact statement covering all complex structures with the given orientation.

**(3) Correct.** The "corpus value 4" was the project's own optimality expectation. `five_research_problems.tex` says so, and it is not a published conjecture; the wording should say "expectation".

**(4) Correct.** Note that h ≥ 1 ⟹ α = 1 uses min(T₊, T₋) = T₊, since T₋ ≫ 0 for general type. Add to the band row: "and α < 1 for h < 1/3 + ηβ₀ on deep ball-quotient covers (74.W)."

**(5) "One unknown" is overstated.**
- The band question α < 1 is decided by κ alone: κ > (3k−A)/4 at some Yamabe representative with Y < 0. This was checked from d = 4π²T₊ − 2I₊.
- Positivity of P\* is a two-variable question, via 𝔭 = k − 4κ/3 + υ/3. The Einstein locus is υ = 4κ − 3k, and §22.5 and Theorem 62.A treat it in (κ, υ).
- Θ\* depends on M, not on h alone. "Θ\*(h)" should be "Θ\*(M)" or "Θ\* along a specified family".

Replacement:
> "The band question is the single capacity Θ\*(M) = sup 2κ/A; open-range positivity is the joint (κ, υ) problem, with Einstein metrics on the line υ = 4κ − 3k."

**(6) Correct.**

**Open list.** Add that P\* > 0 at k = A/3 is not known. LeBrun's nonexistence holds there, but his P-bound is 0.

---

## 3. §24.3 (Problem 3)

### 3.1 Prop. nonbach

The proof was rechecked: Bach-flat ⟹ D𝒲 = 0 ⟹ DS = 0 ⟹ Δs = 0 ⟹ s Ric° = 0. It is correct.

### 3.2 First bullet (k ≥ A/3)

"Unconditionally" holds only with the SW / Yamabe inputs of §1. Replace with:
> "for b⁺(X) ≥ 2 [I], and for b⁺(X) = 1 subject to the sourced chamber input."

The Anderson-ledger sentence cites §15, where the result is stated for ball quotients. Its rank-count part generalizes. It uses only:
- 𝔭\* < k (59.KE, all X);
- b⁺(bubble) = 0 via Lemma 54.3 (b⁺(M) ≥ 2);
- PSC caps (H_dec);
- charge (1).

The π₁/Hopf step is not needed. Replacement:
> "[C] for X minimal general type with b⁺(X) ≥ 2, Anderson case (I) with trivial groups, H_lsc, H_dec: Σ_b[4(e_b−1) + 4b₁ + b₂] < k."

### 3.3 Real-hyperbolic bullet

**The scalar-flat exclusion argument is sound modulo one source.**
- With no PSC metric, a scalar-flat metric must be Ricci-flat. Otherwise a conformal or Kazdan–Warner deformation gives PSC.
- Ricci-flat is excluded by Cheeger–Gromoll, since π₁ = π₁(Y) is not virtually abelian.
- For k > 2χ(Y), Hitchin–Thorpe already excludes Ricci-flat.

**knowledge_request:** a theorem stating that Y#N admits no PSC metric for closed aspherical (or enlargeable) 4-manifolds Y and arbitrary closed N, including non-spin N. Candidates are a Chodosh–Li-type "aspherical connected sums in dimensions 4, 5" theorem or the Gromov–Lawson / Schoen–Yau enlargeability theorem in dimension ≤ 7. The request should give the exact hypotheses.

**Theorem H is misquoted.** §3.4 proves non-attainment under 𝒴(X_k) = Y_hyp, and the value 8π²k is approached by Burns sequences. It explicitly says that the allocation of 8π² per class is proved only for Burns sequences. It also states that arbitrary minimizing sequences are only asymptotically half-conformally-flat and Yamabe-extremal.

Replacement:
> "Under 𝒴(Y#kCP̄²) = Y_hyp (which needs both Schoen's conjecture for Y and blow-up invariance), inf P = 8π²k is not attained (Theorem H). These manifolds are then not Problem-3 examples. Burns sequences realize the infimum; whether every minimizing sequence concentrates at Burns bubbles is not proved."

### 3.4 k=1 dichotomy

**A ≥ 9 is correct and sharpens to A = 9χ(𝒪_X).**
- c₁² = 3c₂ and c₁² + c₂ = 12χ(𝒪) give c₂ = 3χ(𝒪).
- Hence A = 9χ(𝒪) ≥ 9 and A/3 = 3χ(𝒪) ≥ 3.
- Fake projective planes are excluded by 54.A, which needs b⁺ ≥ 3. They are not covered.

**The implication needs correction.** 54.A(iii) gives a minimizer g₀ on V with M ≅ V#Σ, Σ a homotopy sphere. g₀ attains P\*(M) on M only if every cap is diffeomorphic to S⁴. The Einstein branch of the dichotomy is about V. So a nonexistence answer to Problem 1 for M implies a non-Bach-flat minimizer only when V ≅ M; otherwise one needs nonexistence on V.

Replacement:
> "Under Anderson Thm 4.10 (with the three soft spots of step54 §0.9), H_sm, H_lsc, H_dec, H_eq, H_rem, and in case (I) with trivial groups: g₀ is a smooth metric on V, V homeomorphic to M, with s < 0 constant, attaining P\*(V). It is Einstein or a non-Bach-flat global minimizer on V. If all caps are standard, V ≅ M and g₀ attains P\*(M). Thus nonexistence of Einstein metrics on every smooth manifold homeomorphic to M of the form M#Σ⁻¹ yields a solution of Problem 3."

**Remaining configurations.** The list is incomplete. It should contain:
1. orbifold absorption (B), (C), conditional on SW_L;
2. collapse in general (case II). Only free-circle regions are excluded, as spin; finite-isotropy and split classes remain open;
3. nonflat bubbles with exotic caps;
4. the analytic residue of H_dec: compact convergence at bubble scales and AE decay of order τ > 0.

Theorem 56.A, the orbifold-category attainment, should be cited as the conditional extension.

### 3.5 α-attainment list

The list is correct.

"Every known attained α-minimizer is Bach-flat" is true for the listed cases:
- Einstein metrics;
- half-conformally-flat metrics, including the conformally flat products S¹×S³/Γ and S¹×H³/Γ and LeBrun's anti-self-dual metrics on #4CP̄².

Add one point. Where T₊, T₋ > 0 and α = 1 (for example X#kCP̄² with h in the band, if inf ∫|W⁺|² ≥ 2π²(A−k)), attainment would require d = L_s = 0 with no ASD condition. No such minimizer is known, so the Bach-flat pattern rests only on the wall cases.

On X#ACP̄², "constant scalar curvature < 0" is forced, because Y < 0 rules out s > 0.

---

## 4. The "three ends" paragraph

**Correct parts.**
- Computing P\* on the constant-scalar slice is correct, given Y < 0 and 66.Y.
- The bound q² = |a⁻|² ≥ k + Π ≥ k needs SW, namely Π ≥ 0 for every metric. That makes q bounded below by √k, not "by topology" alone.
- From 𝔭 = q²(1−δ)² + L with both terms nonnegative, 𝔭 → 0 ⟺ δ → 1 and L → 0.

**The ledger adds no constraint on p→0.** δ → 1 means 𝔉\_ĥ → 0, which already follows from P/2 ≥ 𝔉². The statement is a restatement of 𝔭 → 0, and should be presented as such.

**The obstruction sentences.**
- *Aligned end* (L=0, 0<δ<1). It refutes L ≥ cδ only on manifolds that carry such a structure. 66.R characterizes them (strictly almost-Kähler, J-invariant Ricci, bounded-extension hypothesis at Z(h)), but **no aligned structure is known on M**.
- *cscK end.* The failure of uniform c_K is proved on products of curves (Step 68), not on M. On M, cscK metrics for blow-up structures have P ≥ 8π²k by K∞.

Replacement:
> "The aligned and cscK equality classes do not carry 𝔭 → 0 (there 𝔭 = q²(1−δ)² ≥ … and 𝔭 = q² ≥ k). They mark where natural coercive estimates are not available. An estimate L ≥ cδ would be false on any M carrying an aligned structure, which 66.R describes but which is not known on X#kCP̄². Uniform Kähler-end coercivity is false on products Σ₁×Σ₂ (Step 68), with no blow-up construction."

---

## 5. The 1/3 wall and KE saturation: false as stated

§24.4 says that ∫(s²/24 + 2|W⁺|²) ≥ (8π²/3)A is saturated by KE metrics. A direct computation shows this is wrong.

**At a KE metric.** |W⁺|² = s²/24, so the integrand is s²/8. With ∫s² = 32π²A, the integral equals **4π²A > 8π²A/3**.

**Where the bound is sharp.** Minimize x²/24 + y²/3, where x = |s| and y = √6|W⁺|, under LeBrun's constraint ∫(x+y)² ≥ 72π²A. The minimum is (1/27)·72π²A = 8π²A/3. It is attained at y = x/8, i.e. √6|W⁺| = |s|/8. That is the almost-Kähler profile θ = 1/3, s\* = s/2 of AKΓ (§3.7). It also matches §3.6 Theorem E, which records "contact at ρ = 3/2, not at KE".

**What KE does saturate.** KE saturates ∫s² ≥ 32π²A and ∫(s − √6|W⁺|)² ≥ 72π²A. It does not saturate the derived P-bound.

**Where the two walls come from.** Both walls are T₊ = 2A/3, via two different inequalities with the same constant:
- d = 4π²T₊ − 2I₊ (identity), and on Kähler metrics 2I₊ = S/12 ≥ 8π²A/3 (Hodge index plus KE saturation of S ≥ 32π²A). This gives the Kähler d-wall.
- P/2 = 2I₊ + S/24 − 4π²T₊ ≥ 8π²A/3 − 4π²T₊, from LeBrun's combined estimate, sharp only at the non-Kähler ratio. This gives the P-zero.

In C₊ language, the Kähler class carries (1/2π²)I₊ = (2/3)C₊ with C₊ ≥ A, while LeBrun gives C₊ ≥ (2/3)A = Γ_min·A. Note also that the Kähler P-bound is P ≥ 8π²k, which never vanishes.

**Replacement.**
> "The value h = 1/3 arises twice. On Kähler metrics W⁺ carries exactly 2/3 of C₊, and KE saturation of ∫s² ≥ 32π²A puts the sign change of the Weyl deficit at T₊ = 2A/3. LeBrun's lower constant C₊ ≥ 2A/3 is attained only by the almost-Kähler profile θ = 1/3 (s\* = s/2), not by KE, and puts the zero of his P-bound at the same T₊. The certified cells cross the first wall (74.W); nothing is known to cross the second."

**Other items in §24.4.**
- *Wahl points.* "Interacts only at O(λ⁴)" is not proved. 56.U gives error O(λ²). 56.L shows that the linear-in-tail term has no logarithm. The λ⁴ polarizability is open.
- *Saving channels.* "Only saving channel is Weyl" is consistent with Theorem Y (8π²k − P(ĝ) = 4D_W − 4ΔV). It should name the volume channel as the competing cost.
- *Degeneration.* "Every known minimizing sequence degenerates" should read "every sequence realizing a known infimum (K∞, Theorem H, dumbbell, orbifold resolutions)". In the open range no minimizing sequence is known.

---

## 6. §23.6

The [N]/undecided tag is appropriate.

A rank deficit (91 of 119 rows) with a slowly decreasing residual cannot separate solvability from obstruction. The decisive object is the order-6 analogue: the cokernel of the linearized order-8 map at the order-6 solution, with exact or interval rank, and the reduced quadratic compatibility on that cokernel.

Proposition 80.R also remains numerical. Its residuals are about 10⁻⁷ at coefficient norm about 10³. An interval Newton/Krawczyk enclosure at the gen2 and gen5 jets would turn "79.C false at order 6" into a certified statement.

---

## 7. Package results absent from §24 that belong in Problems 1–3

**Problem 1 / Problem 2 lower side.** These are necessary conditions on any family with P ≤ 8π²ck, c < 1:
- *Theorem N corollary:* Nijenhuis energy ≥ 16π²(1−c)k.
- *Theorem 63.T:* T_J ≥ 2π√k(1−√c) for every J.
- *Theorem K:* ∫dist(W⁺, 𝒦) ≥ √6π²(1−c)k.
- *Cor. Y1:* Y[g] ≤ −4π√(2(A+(1−c)k)).
- *Theorem 62.A* and conditional *62.B*: the conditional k²/A lower law with α ≥ h²(1+O(h)).
- *Theorem 48.LY on ball quotients:* bulk saving vanishes at linear order, so savings must sit in core relative volume or collar mismatch.

**Problem 2 upper side.**
- The §1.3 bridge α = inf 4𝔭/(𝔭 + A + υ).
- The two-sided α–P comparison of §1 above.

**Problem 3.**
- *Theorems 53.D/53.E:* for Y(M) < 0, configuration (I) without isotropy, some bulk component has Y < 0 and a smooth minimizer. This is a general-M route, not only k = 1.
- *Theorem 56.A:* orbifold-category attainment at k = 1.
- *Prop. 54.4 and step54 §5(c):* bubble P-criticality by compact replacement.

**Zero-gap competitors.**
- *Prop. 56.U / Cor. 56.B:* Wahl-point smoothings give P\*(M′) = 0 and an α-reading with hypotheses. They are relevant whenever M′ ≅ X#kCP̄², a topological question not addressed in §24.

---

## 8. Consolidated knowledge_requests

1. LeBrun's Yamabe invariant and k ≥ A/3 nonexistence for minimal general-type X with b⁺(X) = 1: exact theorem and chamber input.
2. No PSC metric on Y#N for closed aspherical (or enlargeable) 4-manifolds Y and arbitrary closed N, non-spin case.
3. Smooth invariance of the minimal model and of c₁² for all orientation-compatible complex structures on X#kCP̄².
4. Exact citation for the one-sided PSC neck-stretching vanishing theorem used in Lemma 54.3. step54 already records this as owed.