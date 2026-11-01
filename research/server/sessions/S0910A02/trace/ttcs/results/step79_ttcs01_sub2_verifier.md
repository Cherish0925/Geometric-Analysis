# TTCS Independent Branch Record

```json
{
  "step_id": 79,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step79_alignment_closure_and_collapse_transition.md",
    "Sessions/S0910A02/workspace/data/step79_ale_exclusion.json",
    "Sessions/S0910A02/workspace/data/step79_transition_constants_verify.json",
    "Sessions/S0910A02/workspace/notes/step71_collapse_quantum_and_lean_scope.md"
  ]
}
```

## Task

Verify the following two mathematical results for the four-dimensional positive branch of Yau's Problem 26.

RESULT 1 (Transition-Scale Theorem): For a collapsing sequence of closed Riemannian 4-manifolds with Ric >= (n-1)κg (κ > 0) and Vol → 0, define the transition scale ρ_ε(x) = sup{r : Vol(B(x,r))/V_κ(r) >= ε}. Choose p_i maximizing ρ_ε and rescale by ρ_i^{-2}. Then: (a) the rescaled sequence is noncollapsed at unit scale, (b) Euclidean volume ratio ≤ ε at all larger scales, (c) Ric → 0, (d) any pointed GH limit has AVR ≤ ε, (e) if the limit is ALE with group Γ, then |Γ| ≥ 1/ε.

RESULT 2 (ALE Exclusion): For χ = 8, using the Hitchin-Nakajima CGB formula int|W|² = 8π²(χ_top - 1/|Γ|) for ALE resolutions of C²/Γ: the outermost ALE bubble must satisfy rank ≤ 7 (since energy ≤ 64π²). The maximum |Γ| among all ADE groups with rank ≤ 7 is 48 (E_7, energy ≈ 63.83π²). E_8 (|Γ|=120, energy ≈ 71.93π²) exceeds the budget. Therefore for ε < 1/48, NO hyper-Kähler ALE 4-manifold can be the outermost collapse model.

Check: (1) Is the transition-scale proof correct? Pay attention to the volume comparison rescaling and the claim that ρ_i → 0. (2) Is the Hitchin-Nakajima CGB-ALE formula stated correctly? Source-check against the standard literature. (3) Is the ALE exclusion argument complete — are there non-ADE ALE Ricci-flat 4-manifolds that could evade the bound? (4) Does the conclusion correctly follow: outermost model must be ALF/ALG/ALH for ε < 1/48?

## Output

# Verification Memo: Transition-Scale Theorem and ALE Exclusion (P₄⁺, Yau 26)

## Summary judgment

Result 1 (Transition-Scale Theorem) is mathematically sound as a Bishop–Gromov + Cheeger–Colding rescaling argument; parts (a)–(e) follow, with two small wording items and one hypothesis dependency in (c) worth recording. Result 2 is correct and complete **for hyper-Kähler ALE models** — the CGB defect formula, the ADE arithmetic, and the |Γ| ≤ 48 cap all check out. The one place where the written text reaches past what is proven is the "Consequence" sentence in §3.3 that turns the hyper-Kähler proposition into "outermost must be non-ALE." That step needs an additional input (a classification statement for non-hyper-Kähler Ricci-flat ALE, or a general topological inequality linking χ and |Γ|), and the note itself half-records this in "missing steps" #2 but the Consequence text drops the qualifier.

---

## 1. Transition-Scale Theorem — line-by-line

**ρᵢ → 0.** Correct. Since Θ(x,·) is nonincreasing with Θ(x,0⁺)=1>ε, the set {r : Θ≥ε} is a down-interval, so for c<ρᵢ one has Θ(pᵢ,c)≥ε and hence Vol(M_i) ≥ Vol(B(pᵢ,c)) ≥ ε V_{n,κ}(c) > 0, contradicting Vol→0. The argument uses only that V_{n,κ}(c) is a fixed positive number for fixed c>0 and κ. Sound.

**Part (a).** Correct. At r=ρᵢ, Θ(pᵢ,ρᵢ)=ε by continuity, and V_{n,κ}(ρᵢ) = ω_n ρᵢⁿ(1 − c_n κ ρᵢ² + …) with c_n>0, giving Vol_{g̃}(B(pᵢ,1)) ≥ ε ω_n(1 − c_n κ ρᵢ²) → ε ω_n. Noncollapsing with ε′→ε holds, and ε′ ≥ ε/2 uniformly for large i.

**Part (b).** Logically valid, with a sign remark. For R>1, Rρᵢ>ρᵢ gives Θ(pᵢ,Rρᵢ)≤ε, and the conversion is right. The true model factor is V_{n,κ}(Rρᵢ)/(ω_n(Rρᵢ)ⁿ) = 1 − c_n κ(Rρᵢ)² + … which is **below 1** for κ>0, so the sharp statement is ≤ ε(1 − c_n κ ρᵢ²R²) ≤ ε. The note writes ≤ ε(1 + C_n κ ρᵢ²R²); this is a weaker true upper bound (the actual value is ≤ ε), so nothing downstream breaks, but the written O-term carries the opposite sign from the sphere expansion. Purely cosmetic.

**Part (c).** The identity Ric_{g̃} = Ric_g as a (0,2)-tensor is correct (constant rescaling leaves Christoffel symbols, the (1,3)-Riemann tensor, and the contracted Ricci tensor unchanged), so Ric_{g̃} ≥ (n−1)κρᵢ² g̃ → 0. Note that only the **lower** bound Ric→0⁺ follows from the stated hypothesis Ric ≥ (n−1)κg. The two-sided statement "Ric_{g̃} = (n−1)κρᵢ²g̃ + O(ρᵢ²)" uses the near-Einstein upper bound Ric ≤ Λg, which is an extra hypothesis (present in the intended application, absent from the bare theorem statement). Fine as long as the two-sided version is invoked only in the near-Einstein setting.

**Part (d).** Correct. The rescaled sequence has Ric_{g̃ᵢ} ≥ (n−1)κρᵢ²g̃ᵢ ≥ 0 (a lower bound tending to 0 from above) and Vol(B(pᵢ,1)) ≥ ε′ω_n>0, so Cheeger–Colding gives a pointed-GH limit that is a complete noncollapsed RCD(0,n) space. Colding volume continuity plus part (b) evaluated at each fixed R (with ρᵢ→0 killing the error term) yields Vol(B(p_∞,R)) ≤ ε ω_n Rⁿ for every R≥1, hence AVR ≤ ε. Since ρᵢ→0 while diam(g_i) ≤ π/√κ stays fixed (Bonnet–Myers), the rescaled diameters diverge and the limit is complete noncompact — as needed for a bubble. Also worth noting: AVR ≤ ε < 1 forces the limit to be non-flat (flat ℝⁿ has AVR=1), so the theorem genuinely produces a singular/collapsed-at-infinity model, not trivial Euclidean space. That is the real content and it is correctly obtained.

**Part (e).** Correct and standard: an ALE end asymptotic to ℝ⁴/Γ has AVR = 1/|Γ|, so AVR ≤ ε gives |Γ| ≥ 1/ε. Observe the statement here allows **Γ ⊂ SO(4)**, i.e. any finite group, which is more general than the SU(2)/ADE family used in Result 2. Keep this in mind — it is exactly the source of the coverage question below.

**Maximality corollary.** Correct: ρ_ε(y) ≤ ρᵢ for all y translates to transition scale ≤ 1 in g̃ᵢ, so every point is ε-collapsed at scale ≥1 and pᵢ is the most noncollapsed (outermost) point.

One minor formal point: the maximizer pᵢ need not be attained if ρ_ε is not continuous, but choosing pᵢ with ρ_ε(pᵢ) ≥ sup − 1/i suffices and changes nothing.

**Overall:** Result 1 is a valid theorem. It is close to standard "rescale to the collapse-transition scale" technology; its value here is that it hands the P₄⁺ collapse analysis a clean, complete-noncompact, AVR ≤ ε outermost model with a definite noncollapsed unit-scale volume — which is precisely the controlled-annulus ingredient §2 sets out to supply.

---

## 2. Hitchin–Nakajima CGB-ALE formula — source check

The formula
$$\frac{1}{8\pi^2}\int_X |W|^2 = \chi(X) - \frac{1}{|\Gamma|}\qquad(\text{Ricci-flat ALE, end }\mathbb{R}^4/\Gamma)$$
is correct. Derivation: for Ricci-flat metrics s=0 and E=0, so the Gauss–Bonnet integrand reduces to |W|² (equal to |Rm|² here), and the Chern–Gauss–Bonnet theorem on a complete ALE space picks up a defect term at the end equal to 1/|Γ| (the transgression at infinity is that of flat ℝ⁴, value 1, divided by |Γ| for the quotient cone). Checks against Eguchi–Hanson (A₁: |Γ|=2, χ=2) → energy 8π²(2−½)=12π²; against A₇ (|Γ|=8, χ=8) → 63π²; against E₇ (|Γ|=48, χ=8) → 63.83π²; against E₈ (|Γ|=120, χ=9) → 71.93π². All match the JSON.

Attribution remark: the "Hitchin–Nakajima" label is loose. The ALE Gauss–Bonnet defect and the Q_ALE = χ − 1/|Γ| accounting are due to Nakajima / Kronheimer for the hyper-Kähler ALE family and, in the general Einstein-with-conical-end setting, to Atiyah–LeBrun ("Curvature, cones, and characteristic numbers") — which is the source object the Step-71 note already anchors to. The mathematical content is standard and correct; only the name tag is imprecise.

**ADE table and arithmetic.** All (rank, |Γ|, χ_top, energy) rows verify:
A_r: |Γ|=r+1, χ=r+1; D_r: |Γ|=4(r−2), χ=r+1; E₆/E₇/E₈: 24/48/120, χ=7/8/9. The constraint χ_top − 1/|Γ| ≤ 8 forces χ_top ≤ 8 (integer, since 9−1/|Γ|>8), hence rank ≤ 7, and the maximum |Γ| among rank-≤7 ADE groups is 48 (E₇). For ε<1/48 the theorem gives |Γ| ≥ 1/ε > 48, exceeding every feasible ADE order. **Within the hyper-Kähler class this is a correct and complete exclusion.**

---

## 3. The coverage question: non-hyper-Kähler Ricci-flat ALE

This is the one place where the written conclusion outruns the proof.

- The **Proposition** (§3.3, first block) is stated for "hyper-Kähler ALE." There the Kronheimer classification is complete: hyper-Kähler ALE 4-manifolds ⟺ resolutions of ℂ²/Γ, Γ ⊂ SU(2) (ADE). The (χ,|Γ|) pairs are exactly the table, and the |Γ| ≤ 48 cap is airtight. No issue.

- The **Consequence** (§3.3, "the outermost model … must be non-ALE") drops the hyper-Kähler qualifier. To reach "non-ALE," one must exclude **all** Ricci-flat ALE, and the |Γ| ≤ 48 cap does not transfer. Here is the exact reason. The CGB energy formula 8π²(χ − 1/|Γ|) holds for **any** Ricci-flat ALE (it is Gauss–Bonnet with the end-defect, no hyper-Kähler needed), so the energy budget still forces χ ≤ 8. But the cap |Γ| ≤ 48 came from the ADE-specific linkage between χ and |Γ|. For general Γ ⊂ SO(4) that linkage is not the ADE one, and a Ricci-flat ALE with **χ ≤ 8 and |Γ| > 48 would satisfy both the 64π² budget and the |Γ| ≥ 1/ε requirement**, i.e. it would not be excluded.

- Such spaces are not vacuous a priori. Non-hyper-Kähler Ricci-flat ALE 4-manifolds exist (Ricci-flat Kähler ALE with Γ ⊂ U(2) not in SU(2) — Şuvaina, Wright — and, more generally, free isometric quotients of ADE spaces). The structural mechanism to watch: a free isometric quotient of a hyper-Kähler ALE by a finite group of order m sends |Γ| ↦ m|Γ| and χ ↦ χ/m, while the energy 8π²(χ−1/|Γ|) simply divides by m — consistent with CGB. This is precisely the move that decouples "large |Γ|" from "large χ." Whether a concrete Ricci-flat ALE realizes (χ ≤ 8, |Γ| > 48) is itself the question that must be settled; note that crepant-resolution constraints do block many cyclic non-SU(2) cases, so the answer is not obviously "yes" either. The point is that **the present argument neither produces nor precludes such a model**, so it does not by itself deliver "non-ALE."

- Two clean ways to close it, either of which would upgrade the Consequence to a theorem:
 1. A classification input stating that every Ricci-flat ALE 4-manifold with AVR = 1/|Γ| ≤ ε and χ ≤ 8 is one of the ADE hyper-Kähler spaces (equivalently, that no non-ADE Ricci-flat ALE realizes χ ≤ 8 with |Γ| > 48); or
 2. A general topological inequality χ(X) ≥ h(|Γ|) valid for all Ricci-flat ALE with h(|Γ|) > 8 once |Γ| > 48. (The only universal relation the CGB gives is χ ≥ 1/|Γ|, which is far too weak.)

The note's §3.4 "missing steps" #2 (holonomy: is the outermost model hyper-Kähler?) is the same issue, correctly identified there — so the substance is on record; only the §3.3 Consequence sentence states it without the qualifier.

---

## 4. A sharpening available for the hyper-Kähler part

The exclusion uses the **total** budget ∫|W|² ≤ 64π². A hyper-Kähler ALE is (anti-)self-dual, so all of its Weyl energy sits in one chirality. On the balanced χ=8, τ=0 row each chirality carries 32π² in the limit. If the bubble's self-dual orientation aligns with a fixed chirality of the ambient row, the sharp constraint is 8π²(χ − 1/|Γ|) ≤ 32π², i.e. χ ≤ 4, capping |Γ| at 4 (A₃) and excluding hyper-Kähler ALE already for ε < 1/4. Using 64π² is the looser but valid choice (a single bubble's total energy is ≤ the total energy, by lower-semicontinuity of ∫|W|² under the rescaled convergence), so the stated result stands; the chiral refinement would strengthen it but depends on the orientation/chirality bookkeeping that Step 71 flags as unresolved (the "Q=4 per chirality" arithmetic). Worth recording as an available strengthening rather than a correction.

Note also: the "single bubble energy ≤ 64π²" step tacitly uses lower-semicontinuity of Weyl energy across the blow-up (no energy created in the limit). That is legitimate for the outermost bubble via Fatou, and does not require the full no-energy-loss neck identity — but the *distribution* of residual energy to inner bubbles (§3.4 #4) does require that identity.

---

## 5. What is established vs. what remains

Established, and independently reproducible from the given data:
- Transition-Scale Theorem (a)–(e), as a Bishop–Gromov/Cheeger–Colding statement — correct.
- The CGB defect formula and ADE arithmetic — correct.
- Exclusion of **hyper-Kähler** ALE outermost models for ε < 1/48 — correct and complete.

Open, and needed before "outermost must be ALF/ALG/ALH" is a theorem:
- Ruling out non-hyper-Kähler Ricci-flat ALE with χ ≤ 8, |Γ| > 48 (classification input or a χ-vs-|Γ| inequality), as in §3.
- Regularity: identifying the RCD(0,4) limit of §2 as a *smooth* Ricci-flat manifold, so that "ALE/ALF/ALG/ALH" is even the right menu (this is the two-sided |Ric_{g̃}| ≤ Cρᵢ² input in §3.4 #1, itself requiring the near-Einstein upper bound).
- Holonomy identification of the model, which is what would let the ADE/ALF quantum formulas apply at all.

None of these unsettle Results 1 and 2 as stated with their proper qualifiers; they mark exactly the additional mathematics that separates the present hyper-Kähler exclusion from the desired ALE-free dichotomy for the collapse front of P₄⁺.