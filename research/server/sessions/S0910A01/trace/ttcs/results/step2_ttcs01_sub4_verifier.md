# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step2_mechanisms_analysis.md",
    "Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md",
    "Knowledge/objects/papers/4-Manifolds-without-Einstein-Metrics--c95911daf050--cd7839b9cc3d/object.md"
  ]
}
```

## Task

Verify the following quantitative analysis for Yau Problem 26:

1. MIN-OO CORRECTION: The condition in Min-Oo 1990 (JDG 32, 457-472) is d²·max|K| < Λ² (diameter-curvature product, scale-invariant), NOT r⁻²·max|K|. Check this against the OCR source: §3 normalization reads 'max|K(0)| = 1, d(0) < Λ'. Under g→λg: d²K → d²K (invariant) vs r⁻²K → λ(r⁻²K) (not invariant).

2. POSITIVE BRANCH BOUND: For M = X#k CP̄² (LeBrun no-Einstein, 2A/3 < k < A, A=c₁²(X)), combining: (i) LeBrun ∫s²dV ≥ 32π²A, (ii) CGB(+): 4π²(A-k) = ∫[2|W⁺|² + s²/24 - |E|²/2]dV, (iii) Bishop-Gromov V ≤ 24π²/(1-δ)² for σ=+1 gives 12δ²/(1-δ)² ≥ k-2A/3, hence δ_+ ≥ 1/7 uniformly. But stronger: non-trivial SW on LeBrun manifolds prevents s > 0, so δ_+ ≥ 1.

3. NEGATIVE BRANCH: Same integral bound gives δ² ≥ (k-2A/3)/(3(A-k)) using V ≤ 4π²(A-k)/f(δ) from CGB. For varying manifolds with A→∞, this → 0. Check the derivation chain and whether the constants are correct.

4. Verify that the structural asymmetry (positive has Myers+BG+SW control, negative has none) is correctly stated and that no additional constraint on the negative branch has been overlooked.

## Output

# Verification Memo: Quantitative Pinching Estimates for Yau 26 (dimension 4)

I checked the four items against the two supplied source papers (Min-Oo, JDG 32, 457–472; LeBrun, dg-ga/9511015) and re-derived every constant. All four are essentially sound. Three load-bearing facts are used implicitly and should be written into the argument explicitly, and one attribution needs correcting. Details below.

---

## Item 1 — Min-Oo hypothesis reads d²·max|K| < Λ² (verified)

The source text defines the admissible class by "(i) r < 0, (ii) rf 2max|iί:|<Λ 2". The token `rf` is the OCR image of the diameter symbol `d`: §3 normalizes with "max|K(0)| = 1, d(0) < Λ" (rendered "rf(0) < A"), which is condition (ii) evaluated at the initial metric, giving d²·max|K| = d² < Λ². The symbol `r` in condition (i) is the *average scalar curvature* `r = ∫R/∫1`, defined a paragraph earlier, not a radius. So the pinching class is indexed by the diameter–curvature product d²·max|K|, exactly as stated.

The scale check is correct and worth recording as the independent confirmation. Under g → λg (λ>0): lengths scale by √λ, so d² → λd²; sectional curvature has dimension length⁻², so max|K| → λ⁻¹max|K|; the product d²·max|K| is invariant. For the alternative reading r⁻²·max|K|: r scales like scalar curvature (λ⁻¹r), so r⁻² → λ²r⁻² and r⁻²·max|K| → λ·(r⁻²·max|K|), not invariant. Since the Min-Oo pinching theorem is a statement about a scale-invariant class (ε(n,Λ) depends only on n and the dimensionless Λ), only the diameter–curvature reading is dimensionally consistent. The correction stands.

One structural point relevant to Yau 26: Min-Oo requires membership in J⁻(n,Λ) for a *fixed* Λ, i.e. a two-sided grip on d²·max|K| including the full sectional curvature and diameter, plus r < 0 and the pinching `max|nρ/r − 1| < ε`. This is strictly more input than the pure Ricci two-sided pinch of Yau 26. A sequence with Ricci pinch tending to zero that leaves every J⁻(n,Λ) (via max|K|→∞ or d→∞) is not reached by this theorem — the theorem gives no Einstein metric there. That is the correct reading of what Min-Oo does and does not deliver, and it is the mechanism the σ=−1 discussion exploits.

---

## Item 2 — σ=+1 estimate 12δ²/(1−δ)² ≥ k−2A/3 (verified) and δ₊ ≥ 1/7 (verified, but rests on integrality)

I reproduce the chain. Write E = r₀ (trace-free Ricci), A = c₁²(X).

Chern–Gauss–Bonnet on M = X#k C̄P² with 2χ+3τ = c₁²(M) = A − k:
$$4\pi^2(A-k)=\int\Big(2|W^+|^2+\tfrac{s^2}{24}-\tfrac{|E|^2}{2}\Big)\,d\mu .$$
Dropping 2|W⁺|² ≥ 0 and inserting LeBrun's ∫s² ≥ 32π²A (his Thm 2 with 2χ+3τ+k = A):
$$\tfrac{1}{2}\!\int|E|^2 \;\ge\; \tfrac{1}{24}\!\int s^2 - 4\pi^2(A-k)\;\ge\;\tfrac{4\pi^2 A}{3}-4\pi^2(A-k)=4\pi^2\big(k-\tfrac{2A}{3}\big),$$
so ∫|E|² ≥ 8π²(k−2A/3). This matches the memo's line (A).

Pointwise, if the Ricci eigenvalues lie in [1−δ, 1+δ] the trace-free part has eigenvalues of zero mean inside an interval of width 2δ; the extremal (two-up/two-down) configuration gives Σ(dev)² = 4δ², so |E|² ≤ 4δ² and ∫|E|² ≤ 4δ²V. Combining, δ²V ≥ 2π²(k−2A/3).

Bishop–Gromov for σ=+1: δ<1 forces Ric ≥ (1−δ)g > 0. Myers gives diam ≤ π√(3/(1−δ)); the volume comparison to S⁴ of radius √(3/(1−δ)) gives V ≤ (8π²/3)·(3/(1−δ))² = 24π²/(1−δ)². I confirm both constants. This upper bound is **independent of A** — the key structural fact.

Then δ² ≥ 2π²(k−2A/3)/V ≥ 2π²(k−2A/3)(1−δ)²/(24π²), i.e.
$$\boxed{\;12\,\frac{\delta^2}{(1-\delta)^2}\ \ge\ k-\tfrac{2A}{3}\;}$$
exactly as stated.

**The step to δ₊ ≥ 1/7 needs an intermediate fact that is not written down but is true.** Both A = c₁²(X) and k are integers with 3k > 2A (LeBrun's non-Einstein condition k > 2A/3), so k − 2A/3 = (3k−2A)/3 with 3k−2A a positive integer, giving
$$k-\tfrac{2A}{3}\ \ge\ \tfrac13\qquad(\text{uniformly in }A,k).$$
Feeding 1/3 into the boxed inequality: δ²/(1−δ)² ≥ 1/36 ⟹ δ/(1−δ) ≥ 1/6 ⟹ 7δ ≥ 1 ⟹ **δ₊ ≥ 1/7**. So the uniform 1/7 is correct, but it is the *conjunction* of two facts — the A-independent Bishop–Gromov ceiling and the arithmetic k−2A/3 ≥ 1/3 — that produces it. I recommend stating k−2A/3 ≥ 1/3 explicitly, because it is exactly the ingredient that the σ=−1 branch lacks a substitute for (see Item 3). Also note the quantitative route is vacuous at the endpoint k = 2A/3 (possible when 3|A), where k−2A/3 = 0; that endpoint is covered only by the Seiberg–Witten route.

**Attribution correction for "δ₊ ≥ 1".** LeBrun's ∫s² ≥ 32π²A does *not* by itself forbid s>0 (a metric with large positive s satisfies it). The statement "δ₊ < 1 ⟹ Ric>0 ⟹ s>0, impossible" needs the separate Witten-type vanishing: a non-zero Seiberg–Witten invariant obstructs metrics of positive scalar curvature. That obstruction holds for these X#k C̄P² when b⁺ > 1 (the Fermat family used in LeBrun's Theorem A has p_g > 0, b⁺ ≥ 3, so it applies; the b⁺=1 case needs the chamber sign condition). So δ₊ ≥ 1 is correct for the standard family, but should be credited to SW no-positive-scalar-curvature, not to the ∫s² lower bound. Once granted, δ₊ ≥ 1 subsumes the 1/7 route and also covers the k=2A/3 endpoint.

---

## Item 3 — σ=−1 estimate δ² ≥ (k−2A/3)/(3(A−k)) (verified; validity δ<1/(1+√3))

Here the same CGB identity and the same LeBrun ∫s² ≥ 32π²A hold (both are metric-independent). Now s = tr Ric ∈ [−4(1+δ), −4(1−δ)], so s² ≥ 16(1−δ)² and ∫s²/24 ≥ (2/3)(1−δ)²V, while ∫|E|²/2 ≤ 2δ²V. From CGB with 2|W⁺|² ≥ 0:
$$4\pi^2(A-k)\ \ge\ \tfrac{2}{3}(1-\delta)^2 V - 2\delta^2 V\ =\ V\Big[\tfrac{2(1-\delta)^2}{3}-2\delta^2\Big],$$
so
$$V\ \le\ \frac{4\pi^2(A-k)}{\tfrac{2(1-\delta)^2}{3}-2\delta^2},$$
matching line (B). **This is valid only while the bracket is positive**, i.e. (1−δ)² > 3δ² ⟺ δ < 1/(1+√3) ≈ 0.366. Since one is chasing δ→0 this is fine, but the validity condition δ < 1/(1+√3) should be written alongside the bound (it is the same threshold appearing in the Hitchin–Thorpe proposition in the mechanisms note, which is reassuring internal consistency).

Combining ∫|E|² ≥ 8π²(k−2A/3), ∫|E|² ≤ 4δ²V, and the V ceiling:
$$8\pi^2\big(k-\tfrac{2A}{3}\big)\le 4\delta^2 V\le \frac{16\pi^2\delta^2(A-k)}{\tfrac{2(1-\delta)^2}{3}-2\delta^2}.$$
As δ→0 the bracket → 2/3, giving δ² ≥ (k−2A/3)·(2/3)/(2(A−k)) = **(k−2A/3)/(3(A−k))**, exactly as stated. The two numerical anchors check out: A=100, k=67 → (0.333)/(3·33)=3.37×10⁻³, δ≥0.058; A=10⁴, k=6668 → (1.333)/(3·3332)=1.33×10⁻⁴, δ≥0.0116 ≈ 0.012.

**The decisive contrast with Item 2** is now transparent and correctly reported: the σ=+1 volume ceiling is the constant 24π²/(1−δ)², so δ² ≥ (const)·(k−2A/3) ≥ (const)/3; the σ=−1 volume ceiling is ≈ 6π²(A−k), which grows like A. With k−2A/3 held at its arithmetic minimum ~O(1) and A−k ~ A/3, the σ=−1 lower bound is δ² ≳ O(1)/A → 0, i.e. δ_− ≥ C/√A. The claim of no uniform positive lower bound on the σ=−1 branch from these inequalities is correct.

One remark reinforcing that no positive constant is hiding: LeBrun's ∫s²≥32π²A together with s² ≤ 16(1+δ)² also forces V ≥ 2π²A/(1+δ)². So on the σ=−1 branch V ~ 2π²A both from above and below — self-consistent, no contradiction is generated, and hence no hidden obstruction that would rescue a uniform δ_−. This is a useful independent confirmation that the branch is genuinely open rather than merely unproven by the chosen route.

---

## Item 4 — Structural asymmetry (correctly stated, with two refinements)

The asymmetry as reported is accurate:

- **σ=+1:** δ<1 ⟹ Ric>0 activates Myers (diameter), Bishop–Gromov (A-independent volume ceiling), and — separately — SW no-positive-scalar-curvature. Any one of the last two forces δ₊ away from 0 on LeBrun manifolds.
- **σ=−1:** Ric ≈ −g. Myers is inapplicable (needs Ric>0). Bishop–Gromov with a lower Ricci bound of the wrong sign yields exponential/hyperbolic volume growth, not a useful ceiling; the only volume ceiling available comes from CGB itself and is A-dependent. SW obstructs positive, not sign-(−1), scalar curvature, so it is inert here. All three controls are absent, precisely as stated.

Two refinements so the asymmetry is not read as more than it is:

1. **"σ=+1 protected" is protection against the *known* constructions, not a theorem.** The uniform δ₊ bound is established for the two families that currently generate non-Einstein 4-manifolds (Hitchin–Thorpe-violating connected sums, and SW/LeBrun manifolds). Whether some other closed 4-manifold carries Ric>0 metrics yet no Einstein metric of any sign is the open question B2. The mechanisms note does hedge this ("likely true", B2 open); the summary sentence in Item 4 should carry the same qualifier so the σ=+1 statement is understood as "no known construction survives", not "proven for all M⁴".

2. **No additional σ=−1 constraint appears to have been missed among the tools in play.** I checked: Hitchin–Thorpe (sign-independent, and satisfied strictly by these manifolds — that is the point of LeBrun), the ∫s² lower bound (used, gives only the A-growing volume ceiling), and the trace-free eigenvalue bound (used). A genuinely different lever would have to control W or ∇Ric — which is exactly the input Jäckel's theorem needs (negative sectional curvature + bounded ∇Ric) and which pure Ricci pinching does not supply. So the identification of B1 (constructing metrics with δ_− → 0 on non-Einstein manifolds) as the undetermined pivot is consistent with what these inequalities can and cannot reach.

---

## Summary of what to record

- Item 1: correct; `rf` = diameter `d`; scale-invariance argument is the right confirmation.
- Item 2: boxed inequality correct; δ₊ ≥ 1/7 correct **once k−2A/3 ≥ 1/3 (integrality) is stated**; the A-independence of the Bishop–Gromov ceiling is the other essential half; the "δ₊ ≥ 1" statement should be attributed to SW no-positive-scalar-curvature (with b⁺>1), not to ∫s².
- Item 3: chain and all constants correct; add the validity condition δ < 1/(1+√3) under which the CGB volume ceiling is meaningful; δ_− ≥ C/√A → 0 confirmed, and independently V ~ 2π²A shows no hidden obstruction.
- Item 4: asymmetry correct; phrase σ=+1 as protection against known constructions (B2 open), and the absence of a further σ=−1 lever is consistent with needing Weyl or ∇Ric control that Ricci pinching does not give.

Everything numerical and algebraic reproduces cleanly; the only substantive edits are making k−2A/3 ≥ 1/3 explicit, attaching the SW mechanism to δ₊ ≥ 1, attaching δ < 1/(1+√3) to the σ=−1 volume ceiling, and qualifying "σ=+1 protected" as relative to currently known non-Einstein 4-manifolds.