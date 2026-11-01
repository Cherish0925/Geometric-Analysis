# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step4_near_equality_and_boundary_calibration.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/math-0111228-Curvature-Connected-Sums-and-Seiberg-Witten-Theory--84e6ef833958--5b74c8864d85/object.md",
    "Knowledge/objects/papers/Classical-boundary-value-problem-in-Riemannian-quantum-gravity-and-Taub--f07b76fb28c1--60f59311428a/object.md",
    "Knowledge/objects/papers/1712.08861-Partition-functions-on-3d-circle-bundles-and-their-gravity-du--7a54cfd2f253--29a9259ebb8d/object.md",
    "Sessions/S0910A01/workspace/data/step4_taub_bolt_ads_summary.json",
    "Sessions/S0910A01/workspace/scripts/step4_taub_bolt_boundary_probe.py"
  ]
}
```

## Task

Check the Step 4 mathematical correction and route reorientation for Yau Problem 26. Ground your answer in the provided files. In particular: (1) verify or correct the derivation D_a=I-(2/3)(a^+)^2 <= J-q with I-J=A-k and q=k-A/3, and the conclusion D_a/A->0 when delta_->0 and k/A->1/3; (2) verify the source-based equality mechanism of LeBrun's mixed Seiberg-Witten estimate (almost-Kähler structure, lowest W_+ eigenspace, s+s* constant, exact blow-up equality obstruction), distinguishing it from the withdrawn Weyl-only/harmonic-F_A+ argument; (3) check the corrected interpretation of bare ALE cores versus corrected gluing; (4) assess whether the Taub-Bolt-AdS boundary sampler supports only the stated conclusion that exact zero-defect fillings exist for attained boundary Cauchy data, not a general cap lower bound. Give a direct scientific memo identifying any mistakes, missing assumptions, and the most consequential next mathematical/computational test.

## Output

## Verifier memo — Step 4 correction and reorientation (Yau 26, four-dimensional negative branch)

I checked the Step 4 note against LeBrun 2001 (Prop. 2.1, 2.4, 3.1, 3.2, Thm. 4.3), Ishida–LeBrun (Prop. 4, Thm. D), Akbar's Taub–Bolt–AdS construction, and the sampler script/JSON. The algebra and the source-provenance are correct. The most important thing to record is not an error but a mismatch between what the estimate controls (an integral of trace-free Ricci energy) and what Yau 26 asks for (a pointwise, dimension-only two-sided Ricci window). The note actually navigates this correctly, and I make the reason explicit below.

### (1) The deficit inequality is correct; the volume step and the pointwise-vs-integral logic should be stated

Chern–Gauss–Bonnet gives `(2χ+3τ)(M)=I−J`, and for `M=X#kCP̄²` with `A=c₁²(X)` one has `(2χ+3τ)(M)=A−k`, so `I−J=A−k`. With `(a⁺)²≥A` (LeBrun Prop. 3.2 monopole/sign construction) and `I≥(2/3)(a⁺)²` (Prop. 3.1),

- `D_a=I−(2/3)(a⁺)²=J+(A−k)−(2/3)(a⁺)²≤J+(A−k)−(2/3)A=J−q`, `q=k−A/3`.

This is right. The averaging identity `2^{-k}Σ_ε(a_ε⁺)²=(c₁(X)⁺)²+Σ_j(E_j⁺)²` also checks out (cross terms `2^{-k}Σ_ε ε_j=0`, `2^{-k}Σ_ε ε_jε_l=δ_{jl}`), and yields `J≥q+(2/3)Σ_j(E_j⁺)²`, hence `A^{-1}Σ_j(E_j⁺)²→0` under `δ→0`, `q/A→0`. The note's remark that this is a statement about the self-dual parts *of the pinched metrics* (the exceptional classes become nearly anti-self-dual), not an intersection-form identity, is the correct reading.

Two points to make explicit:

- **The pointwise pinching hypothesis is what makes this bite.** `J=(1/4π²)∫|r̊|²/2` is scale-invariant and, for `k>A/3`, is bounded *below* by `q>0`. By itself an integral floor is compatible with metrics that are nearly Einstein except on a small-volume region where `|r̊|` concentrates — precisely LeBrun's own Thm. 4.3 sequences, which "have huge amounts of Ricci curvature concentrated near the blow-ups." The note escapes this because it feeds in the *pointwise* pinching bound `|r̊|²≤4δ²` (correctly derived: writing eigenvalues of `g⁻¹Ric` as `−1+ε_i`, `|ε_i|≤δ`, the trace-free variance `Σ(ε_i−ε̄)²=Σε_i²−4ε̄²≤4δ²`). Pointwise `|r̊|²≤4δ²` converts the floor into a genuine obstruction.

- **The volume bound is used but not spelled out.** `J/A=O(δ²)` needs `Vol=O(A)`. This follows because, under `Ric≈−g`, `s≈−4` so `s²/24` is bounded below by a positive constant `c`; then `(c/4π²)Vol≤I=(A−k)+J≤(A−k)+(2δ²/4π²)Vol`, giving `Vol≤4π²(A−k)/(c−2δ²)=O(A)` near `k/A=1/3`, hence `J/A≤2δ²`. Worth writing this line out; it is the only non-formal link in the chain.

A clean consequence the note states and I confirm: for `k/A≥1/3+η`, `D_a≥0` forces `2δ²≥J/A≥q/A≥η`, so `δ≥√(η/2)`. No pointwise δ-pinched metric with `δ<√(η/2)` exists on such `M`. This is a real quantitative pointwise obstruction that degenerates exactly at `k/A=1/3`, which correctly motivates the interest in the threshold.

### (2) The equality mechanism and its provenance are faithful to LeBrun

The reconstructed chain matches the paper: SW spinor Weitzenböck `0=4∇*∇Φ+sΦ+|Φ|²Φ`, the self-dual 2-form Weitzenböck, `ψ=σ(Φ)=−iF_A⁺` with `|σ(Φ)|²=|Φ|⁴/8` and `|∇σ(Φ)|²≤½|Φ|²|∇Φ|²`, the `L³` estimate (Prop. 2.1) in the lowest `W⁺` eigenvalue `w`, the conformal rescaling making `s+3w` constant (Lemma 2.2), and finally `w≥−√(2/3)|W⁺|`. The displayed `∫((2/3)s−2√(2/3)|W⁺|)²≥32π²(a⁺)²` is Thm. 2.3, and the `2/3` estimate (Prop. 3.1) follows by the triangle inequality plus Cauchy–Schwarz in `ℝ²`. Nowhere is `F_A⁺` assumed harmonic and nowhere is a Weyl-only lower bound invoked; the note's disavowal of the withdrawn argument is justified by the actual proof structure.

The equality characterization (Prop. 2.4) is transcribed correctly: almost-Kähler `ω` in the lowest `W⁺` eigenspace pointwise; `s+s*` a non-positive constant with `s*=s/3+2W⁺(ω,ω)`; `c₁` of `(M,ω)` of type `(1,1)` equal to `c₁(L)`; and, at equality in (10), `W⁺` is `J`-invariant. Corollary 2.5 (Einstein + saturation ⟹ Kähler–Einstein, via Armstrong) and the Prop. 3.2 blow-up obstruction (equality forces `[ω]·E_j=0`, contradicted by Taubes' positive-area pseudo-holomorphic sphere) are stated accurately.

One substantive point: the passage from *exact* equality (Prop. 2.4/3.2) to *near* equality is at present a program, not a theorem. Prop. 2.1 is a Hölder/`L³→L²` chain and Lemma 2.2 is a conformal minimization; neither comes with a quantitative stability statement. The five slack terms the note lists are the right objects, but converting `D_a/A≤ε` into an honest approximate almost-Kähler structure with a controlled `ω` is unproven and is the load-bearing analytic step (see the recommended test).

### (3) The ALE-core correction is elementary and correct

For a Ricci-flat core, `Ric=0` so `g^{-1}(Ric+g)=Id`, operator norm `1`, and this is scale-invariant because `Ric(t²g)=Ric(g)` and the endomorphism `(t²g)^{-1}Ric=t^{-2}g^{-1}Ric` keeps `0` at `0`. So a bare uncorrected core cannot be a small-defect region for the `Ric=−g` target — correct, and it only excludes the bare core. The heuristic that an `O(t²)` relative correction on a core of size `~t` produces an order-one change in the Ricci endomorphism at original scale is sound: linearized Ricci `≈Δh` carries two derivatives, `t^{-2}·O(t²)=O(1)`. The note rightly leaves open whether a first-obstruction-zero corrected gluing can simultaneously supply `−Id`, match the exterior data, and keep the unweighted defect small — this is a solvability-plus-matching problem, not settled by the bare-core computation.

### (4) The Taub–Bolt–AdS sampler supports only the existence statement, and has confinements worth recording

I reproduced the script's formulas against Akbar: `Δ` with `Λ=−1`, regularity `0<L²≤(2−√3)/4≈0.0669873`, `ρ_bolt=(1±√(1+16L⁴−16L²))/(4L)`, `M` from `Δ(ρ_bolt)=0`, `a²=ρ²−L²`, `b²=4L²Δ/(ρ²−L²)`, `dt/dρ=a/√Δ`, and the two mean-curvature ratios. All correct. The `ricci_defect_sup=0.0` is exact by construction (the family solves `Ric=−g`), not verified from the sampled metric. Given that the companion polynomial transcription already misbehaved, a cheap independent confirmation — recompute `Ric` from the sampled metric symbolically/numerically and confirm `‖Ric+g‖=0` — would close any transcription risk in `Δ`. The mean-curvature values `≈√3` at large `a` pass the asymptotically-hyperbolic sanity check (`Ric=−g` in dim 4 ⇒ ambient curvature `−1/3`, trace `3/√3=√3`).

The logical reading is correct: the family exhibits exact zero-defect exceptional-handle caps for their attained induced `S³` data, so a residual-infimum-over-caps argument cannot produce an obstruction; any obstruction must be in matching or global topology. Three confinements to record:

- The attained squashing is confined. Asymptotically `b/a→2L/√3≤2√((2−√3)/4)/√3≈0.30`; the sampler's numerical maximum `≈0.397` occurs only in the degenerate small-`L`, tiny-cap corner (`L=2×10^{-4}`, `a≈5×10^{-4}`, mean curvature `≈3211`). For non-degenerate large caps, `b/a≲0.30`. So the exact-Einstein caps only fill `S³` interfaces that are strongly squashed along the fiber.

- The JSON's "nearest zero-defect examples" for target `b/a=0.5,1,2,4` all return the same point `b/a=0.397`; these targets are simply not attained. In particular the round `S³` (`b/a=1`) is not in the attained set for the `p=1` period. This sits in apparent tension with Akbar's counting statement that any biaxial `S³` admits regular Taub–Bolt–AdS infillings; the resolution is likely that the asymptotic conformal `S³` of `Taub–Bolt–AdS` has a squashing ceiling set by `L`, so the "infilling of any `(a,b)`" is at a finite interior radius with a different induced geometry than a large round sphere. This should be reconciled before the attained-data set is used quantitatively in a matching argument, because the usable data set is exactly `b/a≲0.3` with `A,B` ratios `≈0.58` and trace `≈√3`.

- Topology reading (`O(−1)→S²` ≈ `CP̄²` minus a ball, a neighborhood of a `(−1)`-sphere) is apt for the exceptional handles of `X#kCP̄²`.

### The reorientation is sound but the target regime should be named precisely

Two framings deserve to be pinned down, because they determine what a resolution would even mean:

- **Pointwise, not integral.** Yau 26 asks for a pointwise two-sided window `c_n g≤Ric≤C_n g` with `c_n,C_n` depending only on `n`. Every fixed smooth metric on a compact manifold already satisfies *some* two-sided Ricci bound (eigenvalues of `g^{-1}Ric` are continuous on a compact space); the entire content is the *universality* of the window. After rescaling (which shifts the whole window), the invariant that matters for a fixed-sign Ricci is the achievable pointwise pinching ratio. The Step 4 machinery lives at ratio `→1` (`δ→0`); Yau 26 is stated for a fixed universal window, which may be wide. The `δ→0` analysis therefore addresses the hardest sub-case (tightest pinching) at the single corner `k/A=1/3`; it says nothing yet about wide windows or about dimensions `≥5`.

- **The threshold is where the floor vanishes.** For `k/A≥1/3+η` the note's own inequality forbids tight pinching. At `k/A=1/3` the floor `q=0` disappears, so a `δ→0` pointwise-pinched no-Einstein sequence is *not* excluded by the estimate. That threshold family is the genuine refutation candidate for a narrow window, and the near-equality rigidity is the genuine proof candidate.

### Most consequential next test

The sampler settled the cap half (local exact-Einstein models exist for a confined `b/a≲0.3` data set). The decisive undone half is the interface-matching half:

1. **(Lower cost, decisive fork.)** Compute the induced hypersurface data — the pair `(a,b)` and the two second-fundamental-form ratios — on natural separating spheres in the candidate negative-Einstein exteriors used in LeBrun's own Thm. 4.3 gluing (Kähler–Einstein orbifold model minus a ball; complex-hyperbolic quotient regions), and test whether that data set overlaps the bolt-attained set (`b/a≲0.30`, ratios `≈0.58`, trace `≈√3`), or can be joined to it by a short path in Cauchy-data space with pointwise `‖g^{-1}(Ric+g)‖` small across the transition. A robust overlap points toward a threshold refutation construction; a definite gap (e.g. the exterior forcing `b/a` near `1` at its natural radius against the bolt ceiling `≈0.30`) shows the exact-Einstein cap cannot be attached without a defect-producing neck, pushing toward rigidity. This is the mathematically sharp version of "matching or global topology," and it is close to the sampler already written.

2. **(Higher cost, higher value.)** Establish quantitative stability of LeBrun Prop. 2.1: show `D_a/A≤ε` forces `σ(Φ)` to be `L²`-close to a constant-norm nearly self-dual harmonic form, yielding an approximately symplectic `ω_ε` with a positive lower area bound on `E_j`, contradicting the derived `A^{-1}Σ_j(E_j⁺)²→0`. This is the make-or-break input for the near-equality route; without it, sections 3 and 5 of the note remain a skeleton.

### Items to reconcile

- The reference "Ishida–LeBrun Theorem 7" with "`k+4=A/3` or `k+8=A/3`" cannot be verified from the provided files: Theorem 7 in math/0111228 is Bauer's smash-product statement, not a no-Einstein threshold family. The relevant thresholds in the provided sources are `k≥A/3` (LeBrun 2001 Cor. 3.4, blow-ups) and the `/12` conditions of Ishida–LeBrun Cor. 17 (K3 / `S¹×S³` sums). These distinct thresholds should not be merged; the specific threshold family cited should be checked against the actual Spin-Manifolds paper.
- State the `Vol=O(A)` step explicitly (§(1) above), and recompute `Ric` from the sampled Taub–Bolt–AdS metric once to confirm the `Δ` transcription (§(4) above).