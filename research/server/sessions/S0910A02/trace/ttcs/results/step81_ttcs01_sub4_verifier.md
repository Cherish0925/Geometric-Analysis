# TTCS Independent Branch Record

```json
{
  "step_id": 81,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step81_alignment_mechanism_definitive.md",
    "Sessions/S0910A02/workspace/data/step81_alignment_chain_exact.json",
    "Sessions/S0910A02/workspace/data/step81_spectral_analysis.json",
    "Sessions/S0910A02/workspace/notes/step79_alignment_closure_and_collapse_transition.md"
  ]
}
```

## Task

Verify and extend the following analysis of the harmonic-form alignment mechanism for positive Einstein 4-manifolds.

The key result: the summed Weitzenböck chain for b_+ independent harmonic self-dual forms on a positive Einstein 4-manifold reduces, after Cauchy-Schwarz with θ=0 (rank-1 T) and κ=1 (constant trT), to EXACTLY the Gursky-LeBrun inequality ∫|W+|² ≥ ∫s²/24, independent of b_+. The margin for χ=8, τ=0 rows is exactly √(3/2) ≈ 22.5%.

Three questions to verify and check for errors or missed opportunities:

1. Is the b_+ cancellation correct? The chain is: (s/3)b_+ ≤ 2√(2/3)(∫|W+|²)^{1/2}(∫(trT)²)^{1/2}, and with Q-orthonormal forms, ∫trT = b_+, κ=1 gives (∫(trT)²)^{1/2} = b_+/√V, so b_+ cancels. Is this the sharpest possible use of the Weitzenböck formula, or is there a better way to exploit b_+ ≥ 3 that doesn't go through the crude α·trT bound?

2. The degeneracy defect: on b_+ ≥ 2 Einstein, β ≠ -α/2 somewhere (otherwise Kähler, b_+=1). Does any known result quantify the measure or depth of this deviation? Does the refined Kato |∇W+|² ≥ (5/3)|∇|W+||² (Gursky-LeBrun) combine with a Sobolev inequality to give a quantitative strict inequality for b_+ ≥ 2?

3. The CLR/spectral reformulation: the Weitzenböck operator L = ∇*∇ - 2W+ + (s/3) has b_+ zero modes. On Kähler (b_+=1): potential V = diag(0,6,6) ≥ 0, one zero mode with zero potential. For b_+ = 3: need 3 zero modes, forcing more negative potential. Does this give a b_+-dependent Weyl bound through any known spectral inequality (CLR, Li-Yau, Berezin, or other)?

## Output

## Verification memo: harmonic-form alignment for positive Einstein 4-manifolds

**Bottom line.** The arithmetic of the summed Weitzenböck chain is correct and I reproduce every displayed number (b₊ cancellation, A ≥ 6 = Gursky–LeBrun, A = 9 and factor √(3/2) at Bishop volume, the CP²/S⁴ calibrations). The three questions each identify a real structural obstruction. Below I sharpen each one, correct one premise in the spectral discussion, and locate a single common cause together with two concrete devices that the current chain discards.

---

### Q1 — The b₊ cancellation and whether the crude bound is the sharpest use

**Cancellation is correct.** Summing the harmonic Weitzenböck identity over an L²-orthonormal (= Q-orthonormal, since for self-dual harmonic forms the intersection form equals the L² pairing) basis gives
$$\int|\nabla\Omega|^2 + \tfrac{s}{3}b_+ = 2\int\langle W^+,T\rangle,\qquad \int\operatorname{tr}T=b_+ .$$
Dropping the gradient term and Cauchy–Schwarz at κ = 1 make b₊ cancel exactly, leaving $A\ge s^2/24$. Verified against CP² (equality) and the χ=8, τ=0 identity ∫|W⁺|² = 32π²−3V, giving A = 9 at V = 8π²/3 and the factor √(9/6)=√(3/2). All consistent.

**Sharpest algebraic form.** The two-step estimate (Ky Fan reduction to α·trT, then α ≤ √(2/3)|W⁺|) is equivalent to one clean pointwise inequality. Since W⁺ is trace-free, ⟨W⁺,T⟩ = ⟨W⁺,T₀⟩ with T₀ the trace-free part of T, so
$$\langle W^+,T\rangle \le |W^+|_{\mathrm{HS}}\,|T_0|_{\mathrm{HS}},\qquad |T_0|^2=\operatorname{tr}(T^2)-\tfrac13(\operatorname{tr}T)^2 .$$
For rank-1 T, |T₀| = √(2/3)·trT, recovering C₀ = √(2/3). This is the extremal (least restrictive) configuration, and it is exactly the Kähler eigenvalue pattern — which is why the chain collapses onto Gursky–LeBrun, whose equality case *is* Kähler. **b₊ enters this chain only as the normalization ∫trT = b₊ and is algebraically removed against the κ-scaling of ∫(trT)².** No purely algebraic manipulation of (i) gradient nonnegativity, (ii) the trace pairing, and (iii) L²-orthonormality can retain b₊, because all three are saturated (up to the isotropy factor) by the formal Kähler configuration.

**The one lever the chain throws away.** The improvement over rank-1 requires |T₀| small relative to trT, i.e. T nearly isotropic in L². The route that makes this unattainable is the three-lump configuration: three forms L²-orthonormal but each dominant on a separate region, giving T nearly rank-1 in the L² sense while remaining rank ≥ 2 a.e. Two points worth pressing:

- **Rank ≥ 2 a.e. gives positivity of t₂ but no size.** The Aronszajn/unique-continuation argument correctly forces t₂ > 0 almost everywhere, hence strict inequality — but t₂ can be arbitrarily small off the transition regions, so it yields no margin. This matches the note.
- **Large isotropy defect forces large gradient — and the gradient term was dropped.** A near-rank-1 L² profile requires each ωₐ to be concentrated where the others are small (so that ∫⟨ωₐ,ω_b⟩ = 0 through spatial separation). Concentration of an L²-normalized harmonic form into a region of linear size ℓ makes ∫|∇ωₐ|² grow like ℓ⁻² (Poincaré/Faber–Krahn). Since the manifold has diam ≤ π (Myers, Ric = 3g), the concentration scale is not free. **A coupled inequality that keeps ∫|∇Ω|² and bounds it below by the very concentration that drives |T₀| toward its maximum is the concrete unexplored device.** Whether the compensation reaches the 22.5% deficit depends on effective Sobolev/Faber–Krahn constants on Ric = 3g geometry — the same family of constants that appear in Q3.

So Q1's assessment (the chain cannot retain b₊, three-lump defeats isotropy) is correct; the additional content is that the discarded gradient term is not a neutral loss — it is precisely the quantity that the three-lump activates, and it, plus elliptic regularity on Myers-bounded geometry (which limits how peaked a harmonic form can be given fixed local L²), is the only lever that penalizes concentration inside this chain.

---

### Q2 — The degeneracy defect: measure, depth, and refined Kato

**Measure of the degeneracy set.** Einstein metrics are real-analytic in harmonic coordinates (DeTurck–Kazdan), so W⁺ is real-analytic and the two smallest eigenvalues coincide on a real-analytic subvariety. Either β = −α/2 a.e. — which by Derdziński forces conformally Kähler where W⁺ ≠ 0, hence b₊ = 1 — or the set {β = −α/2} has measure zero. **On b₊ ≥ 2 the degeneracy set is therefore measure-zero, giving α < √(2/3)|W⁺| a.e. and strict inequality in Gursky–LeBrun.** This upgrades "strict but unquantified" to a clean structural reason, but it produces no margin: √(2/3)|W⁺| − α can be uniformly small on a set of nearly full measure.

**Depth.** I know of no quantitative stability form of Derdziński's theorem in the literature. Derdziński is a rigidity (equality) statement; a bound of the shape "‖β+α/2‖ small ⇒ g close to conformally Kähler" would itself be a new theorem about positive Einstein 4-manifolds. The note's statement that depth is uncontrolled is accurate.

**Refined Kato + Sobolev does not carry b₊.** The refined Kato inequality |∇W⁺|² ≥ (5/3)|∇|W⁺||² (constant verified: 5/3 for the δW⁺ = 0 self-dual Weyl system) combined with the Bochner formula for W⁺ and the Yamabe/Sobolev inequality is *exactly* the machine that proves Gursky–LeBrun ∫|W⁺|² ≥ ∫s²/24. It is a statement about the curvature section W⁺ alone; b₊ is the dimension of harmonic sections of a different bundle (Λ⁺-valued forms). The two couple only through the pointwise pairing ⟨W⁺,T⟩ — i.e. through the very chain of Q1. So refined Kato + Sobolev reproduces the b₊-independent bound and cannot by itself generate b₊ dependence. A genuine improvement would require a *coupled* Bochner identity linking the harmonic-form data to the W⁺ equation, which neither ingredient supplies.

---

### Q3 — The spectral reformulation (this is where I diverge from the note)

**The reformulation is rigorous and exact.** L = ∇*∇ − 2W⁺ + s/3 on Γ(Λ⁺) has ker L = harmonic self-dual forms, so dim ker L = b₊. Good. The potential Π = −2W⁺ + (s/3)Id has eigenvalues 4 − 2α, 4 − 2β, 4 − 2γ (s = 12); only the α-direction can drop below zero, when α > s/6 = 2. The calibrations are right: Kähler gives Π = diag(0,6,6); S⁴ gives Π = 4·Id.

**A semiclassical near-miss — and why it does not decide the count.** The leading phase-space (CLR/Weyl) count of modes below zero in dimension 4 uses L₄^cl = 1/(32π²):
$$N_{<0}^{\rm cl}=\frac{1}{32\pi^2}\int(2\alpha-4)_+^2\,dV.$$
Using (2α−4)²₊ ≤ 4α² on {α>2}, then α² ≤ (2/3)|W⁺|², then ∫|W⁺|² = 32π² − 3V:
$$N_{<0}^{\rm cl}\le \frac{1}{32\pi^2}\cdot 4\cdot\frac23(32\pi^2-3V)=\frac{32\pi^2-3V}{12\pi^2}\le \frac{8}{3}\approx 2.67<3,$$
with value exactly 2 at Bishop volume, for **every** admissible V ∈ (0, 8π²/3]. Taken naively this looks like exclusion of b₊ = 3, and it is a genuine reason the target sits *just* above the leading semiclassical count — a factor ~1.1, not the factor ~300 that "5.9 vs 0.019" suggests. This is worth recording.

**But the count is of the wrong quantity, and I correct the note's premise here.** The phase-space integral counts modes strictly below zero; b₊ counts modes *at* zero. On Kähler–Einstein (Ric = 3g) α ≡ 2 exactly, so Π = diag(0,6,6) never drops below zero, the phase-space count is 0, yet b₊ = 1 (the parallel Kähler form is a zero mode of L riding the α ≡ 2 threshold). **Thus zero/threshold modes are systematically invisible to the leading count, and they are precisely the b₊ we want to bound.** This also corrects the note's stated premise "three zero modes require more attractive potential budget": the Kähler example shows a zero mode can sit at zero potential. Three near-threshold zero modes on a χ=8, τ=0 metric would need α ≈ 2 over enough volume and enough independent directions of Λ⁺, not deep attractive potential — and CGB, which bounds ∫α² but permits α ≈ 2 at zero potential cost over large regions, cannot forbid that.

**Why rigorous compact CLR does not substitute.** The pure CLR bound N₀ ≤ C∫Π₋² is false on a compact manifold: a uniform potential Π = −ε produces a mode below zero (from the constants/kernel of ∇*∇ where it exists) while ∫Π₋² = ε²V → 0. On Λ⁺ the escape is that ∇*∇ has no parallel self-dual sections in the non-Kähler case, so it has a spectral gap λ₁(∇*∇|_{Λ⁺}) > 0; a CLR bound *relative to that gap* would be the correct rigorous object. But CGB does not supply a lower bound on λ₁(∇*∇|_{Λ⁺}). The rigorous heat-trace route (b₊ ≤ tr e^{−tL}, via Hess–Schrader–Uhlenbrock diamagnetic + a Li–Yau on-diagonal heat-kernel bound available on Ric = 3g) is valid but must be optimized at finite t (L has modes below zero, so the trace grows as t → ∞), and it contains ∫ e^{2tα} dV — exponentially sensitive to concentration of α, hence defeated by the three-lump exactly as in Q1.

**Net for Q3:** the reformulation is exact and the semiclassical count is a real near-miss, but it counts strictly-sub-zero modes and misses the threshold zero-modes that constitute b₊ (Kähler counterexample). The two rigorous replacements are either concentration-sensitive (heat trace) or need a Lichnerowicz-type lower bound λ₁(∇*∇|_{Λ⁺}) ≥ c > 0 for non-Kähler positive Einstein — a plausible independent theorem not contained in CGB. This is a sharper localization than "constant unknown."

---

### The single common cause

All three routes are undone because the exact Weyl-integral identity ∫|W⁺|² = 32π² − 3V controls an L² integral of curvature but not:

1. **pointwise concentration** — which defeats the harmonic-form chain (isotropy → 0) and the heat-trace count (∫e^{2tα}); and
2. **the threshold/zero-mode structure** — which defeats leading phase-space counting (Kähler: b₊ = 1 modes at zero potential).

The two devices that *do* penalize concentration — the dropped gradient term ∫|∇Ω|² (via Faber–Krahn on Myers-bounded geometry) and the spectral gap of ∇*∇ on Λ⁺ — are exactly the ones discarded. This is the same object seen from two sides: the gradient term is the quadratic form of ∇*∇, and λ₁(∇*∇|_{Λ⁺}) > 0 is what would forbid a harmonic form from concentrating at zero gradient cost.

### Concrete extensions worth attempting

- **Retain ∫|∇Ω|² and couple it to the isotropy defect.** Establish a Poincaré/Faber–Krahn estimate on Ric = 3g, diam ≤ π geometry showing that ∫|T₀|² near its rank-1 maximum forces ∫|∇Ω|² ≳ (some explicit multiple of the deficit). The target is to convert the discarded gradient term into recovery of the 22.5%. The pass/discard question here is whether the effective Sobolev constant on Ric = 3g is strong enough.
- **A Lichnerowicz-type lower bound λ₁(∇*∇|_{Λ⁺}) ≥ c > 0 for non-Kähler positive Einstein.** This would make the relative-CLR rigorous and, combined with the semiclassical count sitting at ≈ 2 < 3, could produce an actual exclusion of b₊ = 3. This is the highest-value single sub-result: it is exactly the input the spectral route needs and is plausibly a theorem in its own right.
- **A rigorous finite-t heat-trace evaluation** with the Li–Yau on-diagonal bound and the exact Π-eigenvalues, to see how far ∫e^{2tα} can be pushed by concentration inside the CGB budget — this quantifies the three-lump obstruction and would either close or definitively locate the barrier.

### Minor points in the surrounding material

- The Kähler counterexample above indicates the sentence in step81 §2.4 ("For b₊ = 3: three zero modes require more negative potential budget") should be read as heuristic only; the potential can vanish at a zero mode.
- step81 §2.2 states T has rank ≥ 2 a.e. This is right for pairwise independence; note that for three genuinely independent analytic sections of the rank-3 bundle Λ⁺, T is positive-definite (rank 3) a.e. unless the three are everywhere linearly dependent (an analytic condition). The distinction does not affect the conclusion but the stronger statement is available.
- step79 §4 "Hol = SU(2) ⇒ χ = 24" is correct for compact simply-connected Ricci-flat Kähler (K3); the surrounding λ = 0 discussion for χ = 8 is sound in excluding Kähler Ricci-flat and correctly flags that non-Kähler Ricci-flat (Hol ⊄ SU(2)) is not excluded.
- The CGB, Bishop (V ≤ 8π²/3), refined-Kato constant (5/3), |W⁺|² ≥ (3/2)α² with equality at β = γ = −α/2, and the CP²/S⁴ calibration numbers all check out.