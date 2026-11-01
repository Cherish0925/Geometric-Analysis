# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/briefing/aligned_research_goal.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Independently check the dossier's central reduction Q_n iff P_n^+ or P_n^- and search for hidden quantifier, scaling, sign, or vacuity issues. Then critically assess what low-dimensional cases are already settled and what a full refutation actually requires. Check especially whether arbitrary intervals can be vacuous, how homothetic rescaling acts on Ricci as a (0,2)-tensor and on the Ricci endomorphism, and whether n=2,3 yield complete positive results under the stated smooth closed connected conventions.

## Output

# Verification Memo: Central Reduction, Scaling, Vacuity, and Low-Dimensional Status

I reworked the dossier's core reduction and the surrounding algebra independently. The mathematics holds. Below I record the verified derivations, one point of algebra worth stating explicitly that the text leaves implicit, the resolution of the vacuity question you raised, and a precise account of what n=2,3 actually deliver and what a full refutation therefore demands.

## 1. Homothetic rescaling: both actions confirmed

For a constant c>0 and g̃ = cg, the Levi–Civita connection is unchanged (Christoffel symbols are invariant under constant rescaling), so the (1,3) Riemann tensor and its contraction are unchanged. Hence

- **as a (0,2)-tensor:** Ric_{cg} = Ric_g (eq. `scale` is correct);
- **as the endomorphism** A_g = g⁻¹Ric_g: A_{cg} = (cg)⁻¹Ric_{cg} = c⁻¹A_g, so every eigenvalue scales by c⁻¹.

This is exactly the asymmetry that makes the problem nontrivial: the eigenvalue band moves under rescaling while the tensor Ric itself does not, so "Ricci small in g̃-norm" carries no Einstein information without a fixed reference. The dossier's §2.4 uses this correctly.

I checked the interval-to-branch normalization numerically and symbolically. For a<b with ab>0, μ=(a+b)/2, g̃=|μ|g, ε=(b−a)/|a+b|, σ=sign μ: the eigenvalue band [a,b] of A_g maps to [a/|μ|, b/|μ|], and this equals [σ−ε, σ+ε] in both sign cases. Worked example (a=−3,b=−1): μ=−2, |μ|=2, band [−3/2,−1/2], σ=−1, ε=1/2, [σ−ε,σ+ε]=[−3/2,−1/2]. ✓ And ε∈(0,1) is forced by ab>0 (since |a+b|>b−a exactly when a,b share sign and are nonzero). ✓

## 2. Proposition (Q_n ⟺ P_n⁺ ∨ P_n⁻): both directions verified

**P⟹Q.** Given P_n^σ with threshold ε, set a=σ−ε, b=σ+ε. Then a<b and ab>0 (for σ=+1, both factors >0 since ε<1; for σ=−1, both <0). The hypothesis ag≤Ric_g≤bg is literally δ_σ(g)≤ε, so Q_n holds with this witness. ✓

**Q⟹P.** The one geometric fact needed is that every nondegenerate interval [a,b] contains a nondegenerate closed subinterval [u,v] with uv>0. I confirmed this in every configuration: if 0<a or b<0 take [u,v]=[a,b]; if a<0<b (or an endpoint is 0) take a half-length piece such as [b/2,b] or [a,a/2] on the side away from 0. Then with μ=(u+v)/2, σ=sign μ, ε=(v−u)/|u+v|∈(0,1), any h with δ_σ(h)≤ε rescales to g=h/|μ| whose A_g eigenvalues lie in [u,v]⊂[a,b], so Q_n applies and yields Ein(M)≠∅, giving P_n^σ for that one σ. ✓

**Quantifier hygiene.** The extracted ε depends only on the fixed witnessing interval of Q_n, hence only on n; it does not depend on M or g. There is no hidden M- or g-dependence. The sign σ is fixed by the chosen subinterval, so Q_n yields one branch, i.e. P_n⁺∨P_n⁻ (not the conjunction). The dossier's table correctly separates ∨ from ∧, and the refutation direction (¬Q_n ⟺ ¬P_n⁺ ∧ ¬P_n⁻ at a single fixed n) is the correct contrapositive. The equivalence is airtight.

**Sign ordering** in the σ=−1 branch, (−1−ε)g ≤ Ric_g ≤ (−1+ε)g, matches δ_−(g)=max|λ+1|≤ε. ✓

## 3. Vacuity: no interval is vacuous — the problem cannot be won cheaply

You asked whether an arbitrary interval can make Q_n's implication vacuously true (no metric satisfies the hypothesis). The answer is that **no admissible interval is vacuous**, and this is worth recording because it removes a route to a trivial affirmative.

- **Positive interval [a,b], 0<a<b:** the round S^n of radius r has A=(n−1)/r²·Id; choosing (n−1)/r²∈[a,b] (possible since the band has positive length) satisfies the hypothesis.
- **Sub-zero interval a<b<0:** a compact hyperbolic n-manifold (exists for all n≥2) with A=−(n−1)/r²·Id fills any value <0 after rescaling.
- **Zero-crossing a<0<b:** any metric on any closed manifold, rescaled by large c, has all eigenvalues c⁻¹λ_i → 0 ∈ (a,b), so the hypothesis is met by every closed manifold.

The first two witnesses are themselves Einstein, so they do not threaten anything; the content is entirely whether a *non-Einstein-admitting* manifold can enter the band. The third case shows precisely why a zero-crossing interval cannot witness Q_n in any dimension where some closed manifold carries no Einstein metric (e.g. #₅ℂP² in n=4): Q_n with such an interval would force *every* closed n-manifold to be Einstein-admitting. The reduction routes around this by extracting a same-sign subinterval, so vacuity/zero-crossing never obstruct the equivalence. This confirms the dossier's §2.4–2.5 reasoning and supplies the explicit statement (absent from the text) that the hypothesis class is always non-empty.

## 4. n=2: complete positive resolution (uniformization)

In 2D, Ric = K·g, so "Ric_h=λh with λ constant" is exactly constant Gauss curvature. Uniformization gives every closed connected surface (orientable or not) a constant-curvature metric. Therefore **Ein(M)≠∅ for every closed surface**, and the implication in Q_2 holds with the conclusion always true — P_2⁺ and P_2⁻ both hold for any ε∈(0,1), independent of any pinching. The dossier's §4.3 warning is correct: existence comes from a *different* constant-curvature metric produced by uniformization, not from misreading the pointwise identity Ric=Kg (K non-constant) as Einstein.

## 5. n=3: both branches hold; I verified the curvature algebra

**σ=+1 branch.** δ_+(g)<1 forces Ric ≥ (1−ε)g > 0, so Hamilton (1982) gives a spherical space form, hence a constant-positive-curvature Einstein metric. The threshold is sharp at 1: the round product S²(1)×S¹ has A-eigenvalues (1,1,0), so δ_+=1 exactly, and any non-space-form 3-manifold (e.g. S²×S¹, which admits no Ric>0 metric) has δ_+(g)≥1 for every metric. Thus Γ_3⁺ = 1 and P_3⁺ holds for every ε<1.

**σ=−1 branch.** I checked the 3D sectional–Ricci algebra fully. In the Ricci eigenframe with eigenvalues r_i, the curvature operator on Λ² is diagonal (its off-diagonal entry ⟨R̂(e_i∧e_j),e_i∧e_k⟩ = R_{jk}(Ricci) = 0 since Ric is diagonalized), with eigenvalues K_{ij}=(r_i+r_j−r_k)/2. With r_i∈[−1−ε,−1+ε] the largest such value is (−1+3ε)/2, so ε<1/3 makes R̂ strictly sub-zero on all of Λ², i.e. sec<0 for *every* 2-plane, not merely the frame planes. Then Cartan–Hadamard ⟹ aspherical, π_1 word-hyperbolic (no ℤ²), and geometrization/hyperbolization ⟹ hyperbolic ⟹ Einstein (λ=−2). Consequently any non-Einstein-admitting closed 3-manifold has δ_−(g)≥1/3 for all metrics, so Γ_3⁻ ≥ 1/3 and P_3⁻ holds for every ε<1/3.

So Q_3 holds — indeed P_3⁺∧P_3⁻ holds. Note the mechanism differs from n=2: it is **not** that every closed 3-manifold is Einstein-admitting (S²×S¹, Nil/Sol manifolds are not); rather, the pinching hypothesis itself forces the manifold to be a space form. The dependence structure is worth flagging for the formalization target: n=2 rests on uniformization, P_3⁺ on Hamilton's Ricci-flow theorem (elementary, and there is a Lean lead at arXiv:2608.21502 to check for equivalence of the formal statement), but P_3⁻ rests on Perelman geometrization, which is not formalized and is a deep ingredient — so even the "settled" low dimensions are large formalization undertakings.

## 6. What a full refutation actually requires

Combining §4–§5 with the reduction: since Q_2 and Q_3 both hold, ¬(∀n≥2 Q_n) forces a **single fixed n≥4** in which *both* P_n⁺ and P_n⁻ are refuted, each meaning (eq. `neg`) a family M_ε (ε↓0) with δ_σ(g_ε)≤ε over the whole manifold and no Einstein metric of any λ. The dossier states the "single dimension, both branches" requirement correctly; the explicit consequence "the smallest candidate dimension is n≥4" is a synthesis the text does not spell out and that I recommend recording.

**The 4D obstruction (Prop. gap) is correct.** I reproduced the arithmetic: with Ricci eigenvalues σ+e_i, |e_i|≤ε, one gets |s|≥4(1−ε), |E|²=Σ(e_i−ē)²≤Σe_i²≤4ε², and dropping the Weyl term in the Gauss–Bonnet/signature identity gives

2χ ± 3τ ≥ (Vol/4π²)[ (2/3)(1−ε)² − 2ε² ] > 0 for ε < 1/(1+√3) ≈ 0.366,

hence 2χ>3|τ| (strict Hitchin–Thorpe), uniformly for σ=±1 since the driving term s²/24 is sign-blind. So any tightly-pinched 4-manifold satisfies strict Hitchin–Thorpe; a candidate 4-manifold that violates or meets equality in Hitchin–Thorpe (e.g. #₅ℂP² with 2χ−3τ=−1) cannot support arbitrarily tight ±1 pinching and is disqualified as a refutation. This is a genuine constraint on the refutation program, and it composes with LeBrun's Seiberg–Witten obstructions (which act beyond χ,τ) — but any usable obstruction must coexist with a genuinely pinched input rather than itself forcing a positive lower bound on δ_σ.

The existence-side evidence points the same way: Hamenstädt–Jäckel's Gromov–Thurston families and Fine–Premoselli's branched-cover constructions show that many pinched sub-zero-curvature manifolds that "look exotic" in fact carry Einstein metrics, so σ=−1 refutation candidates are heavily constrained, and the burden for a refutation is to exhibit tight pinching together with a global exclusion of *all* Einstein metrics of every sign on one fixed smooth manifold at one fixed n≥4.

## 7. Items to make explicit (not corrections — additions)

Everything checked is correct. Three statements are implicit in the dossier and would strengthen the write-up if made explicit: (a) no admissible interval is vacuous, so the affirmative cannot be reached trivially; (b) Q_2 and Q_3 hold, so any refutation lives at a single n≥4; (c) the sharp low-dimensional thresholds Γ_3⁺=1 and Γ_3⁻≥1/3, with the mechanism that pinching forces the space-form structure rather than every 3-manifold being Einstein-admitting. The one unresolved external dependence I cannot settle from the supplied material is the historical wording of the 1982 original versus the reorganized PDF page 77, which affects only the identity of the target statement, not the mathematics of the reduction verified above.