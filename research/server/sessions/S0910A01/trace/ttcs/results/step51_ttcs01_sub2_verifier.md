# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step51_reflexive_bridge_einstein_existence_proof.md",
    "Sessions/S0910A01/workspace/scripts/step51_reflexive_bridge_verify.py",
    "Sessions/S0910A01/workspace/notes/step50_global_smoothing_evidence_campedelli_front.md"
  ]
}
```

## Task

Verify the complete mathematical chain in the proof note for Einstein existence on the BCGP Z₄² K²=2 product-quotient resolution. The chain is: (1) T_X⁰ ≅ (π_*T_Y)^G by reflexive extension, where π: Y=C₁×C₂ → X=Y/G and X has six isolated A₁ singularities. The argument is: both sheaves are reflexive, they agree on the étale locus U = X\Sing(X) (codim-2 complement), and reflexive extension is unique on a normal surface. (2) H²(X, T_X⁰) = H²(Y, T_Y)^G via Reynolds splitting + Leray (finite pushforward). (3) H²(Y, T_Y)^G = 0 via equivariant Serre duality giving H⁰(Y, Ω¹_Y ⊗ K_Y)^G, then Künneth decomposition, then character computation (already verified by script: both invariant dimensions are zero). (4) Lee-Park Proposition 2.4(2): H²(T_X⁰)=0 implies global QG smoothing of all 6 A₁ nodes. (5) Ampleness persistence + Aubin-Yau on smooth fibers. (6) Milnor fiber bridge: S ≅_diff X_t. Check each step for hidden hypotheses, incorrect categorical claims, missing conditions, or logical gaps. In particular: (a) Is T_X⁰ = Hom(Ω¹_X, O_X) indeed reflexive on a normal surface with A₁ singularities? (b) Is (π_*T_Y)^G reflexive? (c) Does the Reynolds splitting work at the sheaf level (not just cohomology)? (d) Is the Serre duality trace map G-equivariant? (e) Does Lee-Park's proposition apply to RDP (du Val) singularities specifically, or only to T-singularities more generally? (f) Is the Milnor fiber for A₁ really diffeomorphic to the resolution neighborhood?

## Output

## Verification memo: BCGP Z₄² K²=2 Einstein-existence chain

**Overall.** The six-step chain is mathematically sound in its logical skeleton, and the arithmetic core (the character computation feeding the vanishing) is correct. Three things need attention: one written justification that is stated through an incorrect general principle but whose conclusion is true; one hidden hypothesis carried silently from the product-quotient setup; and one step whose written reason is logically insufficient although the underlying fact is true and provable by a different short argument. The passage from A₁ singularities to the smooth Einstein manifold works *precisely because* every singular point is a du Val (RDP) A₁ point, and the note is correct to lean on that; the same chain would break for general T-singularities. Details below, keyed to your questions (a)–(f).

---

### Step 1 — reflexive extension T_X⁰ ≅ (π_*T_Y)^G

**(a) Is T_X⁰ = ℋom(Ω¹_X, O_X) reflexive?** Yes, the conclusion is correct, but the reason given in §2.1(a) is not the right one. The note argues "a torsion-free sheaf of rank n on a normal surface is reflexive iff it is locally free outside a codimension-2 set." That equivalence is false as a general statement — reflexive sheaves on a normal surface can fail to be locally free exactly at the singular points, and torsion-free-plus-locally-free-in-codimension-1 does not force reflexivity. The correct and cleaner reason: on a normal integral scheme the dual ℋom(F, O_X) of *any* coherent F is reflexive (Hartshorne, *Stable reflexive sheaves*, Cor. 1.2). Since T_X⁰ is a dual sheaf, it is reflexive. Replace the stated reason; the object is fine.

**(b) Is (π_*T_Y)^G reflexive?** Yes. The clean argument: T_Y is locally free (Y smooth), hence S2; π finite preserves S2 under pushforward with X normal; taking G-invariants in characteristic 0 is a Reynolds direct summand, so the invariant subsheaf is S2 and torsion-free, hence reflexive on the normal surface X. Equivalently this is the standard identity "reflexive tangent of a quotient singularity = invariants of the tangent upstairs." Correct.

**Hidden hypothesis (load-bearing).** The étale-locus comparison §2.1(b) needs π⁻¹(U) → U to be finite *étale*, and needs Sing(X) to consist of exactly the six A₁ points. Both require that G act **freely in codimension one** on Y (no element fixes a curve — no pseudo-reflections). If some g fixed a curve, or if some stabilizer produced a smooth quotient point or a worse singularity, the étale identification and the "six A₁" statement would change. This is a standing assumption of the BCGP product-quotient construction and is presumably satisfied here, but the note never states it and the script never re-derives the singularity census — it imports "six A₁" from BCGP §6.7 and encodes it only as the bookkeeping identity `6 = 8 - K²`. This is the right place to record explicitly that the fixed-point analysis of the diagonal Z₄² action yields exactly six Z/2-stabilizer orbits, each an A₁, and nothing else.

### Step 2 — H²(X, T_X⁰) = H²(Y, T_Y)^G

**(c) Does Reynolds split at the sheaf level?** Yes. Each g acts as an O_X-linear endomorphism of π_*T_Y (because π∘g = π, so G fixes O_X pointwise), so R = (1/|G|)Σg* is an O_X-linear idempotent and π_*T_Y = (π_*T_Y)^G ⊕ ker R as O_X-modules. Cohomology respects the summand, giving Hⁱ(X,(π_*T_Y)^G) = Hⁱ(X, π_*T_Y)^G. The Leray step is correct: π finite ⟹ affine ⟹ Rʲπ_* = 0 (j>0) ⟹ Hⁱ(X, π_*T_Y) = Hⁱ(Y, T_Y). Combined, Step 2 holds.

### Step 3 — H²(Y,T_Y)^G = 0 via Serre duality + Künneth + characters

**(d) Is the Serre-duality trace G-equivariant?** Yes. G acts by holomorphic automorphisms, which act trivially on H²(Y, K_Y) ≅ ℂ (the Grothendieck trace to Spec ℂ is intrinsic and functorial for the G-invariant structure map). Hence the cup-product pairing is G-equivariant, and H²(T_Y)^G ≅ (H⁰(Ω¹_Y⊗K_Y)^∨)^G ≅ (H⁰(Ω¹_Y⊗K_Y)^G)^∨ using (W^∨)^G ≅ (W^G)^∨ in characteristic 0. Correct. The Künneth split Ω¹_Y⊗K_Y = 2K₁⊠K₂ ⊕ K₁⊠2K₂ and the H⁰ decomposition are standard.

**Character arithmetic.** The Chevalley–Weil formula used in the script is the correct one: for a nontrivial character χ of the abelian cover of ℙ¹ branched at three points with monodromy e_i of order 4, dim H⁰(K_C)_χ = Σᵢ⟨χ(eᵢ)⟩ − 1 = (Σ pair(χ,eᵢ) − 4)/4, well-defined because Σeᵢ = 0 forces Σ pair ≡ 0 (mod 4). Genus sums to 3 on each curve; the character sets {(2,3),(3,0),(3,1)} and {(0,3),(1,2),(3,3)} and both invariant dimensions = 0 are internally consistent and match the hand table. I checked the structure of the formula and the summation logic; this part is reliable.

**One logically insufficient reason (repairable, and the fact is true).** The identification H⁰(2K_{Cᵢ}) = Sym²H⁰(K_{Cᵢ}), used to obtain the H⁰(2K) characters, holds iff C_i is non-hyperelliptic (for hyperelliptic genus 3 the multiplication map Sym²H⁰(K) → H⁰(2K) has one-dimensional kernel, so the image is 5-dimensional while both spaces are 6-dimensional, and the character decomposition of the true H⁰(2K) would differ). This step is therefore load-bearing. The note's stated reason — "every order-2 element of G fixes at most 4 points, whereas a genus-3 hyperelliptic involution has 8 fixed points" — only excludes the *G*-involutions from being the hyperelliptic involution; it does not exclude a hyperelliptic involution ι lying **outside** G. That reason is insufficient as written.

The fact itself is true and admits a clean proof: the hyperelliptic involution ι of a hyperelliptic C is unique, hence central in Aut(C); G ↪ Aut(C) then maps injectively into Aut(C)/⟨ι⟩ ⊂ PGL₂(ℂ) (injective because ι ∉ G — otherwise G/⟨ι⟩, of order 8, would be a non-cyclic non-(ℤ/2)² abelian subgroup of PGL₂(ℂ), which do not exist). But then Z₄² itself embeds in PGL₂(ℂ); finite abelian subgroups of PGL₂(ℂ) are cyclic or (ℤ/2)², and ℤ/4×ℤ/4 is neither. Contradiction, so C is non-hyperelliptic. Substituting this argument (or, alternatively, computing H⁰(2K_{Cᵢ}) directly by Chevalley–Weil for the bicanonical representation, which sidesteps Sym² entirely and would independently confirm the character sets) closes the one genuine hole in Step 3.

### Step 4 — Lee–Park globalization

**(e) RDP vs general T-singularity.** A₁ is simultaneously an RDP and an index-1 T-singularity, so it lies inside the KSB/Hacking–Wahl class Lee–Park work with; the proposition applies. The deformation bookkeeping is correct: T¹ supported at the six A₁ nodes has H⁰(T_X¹) = ℂ⁶ (T¹ of A_n is ℂⁿ, so ℂ for A₁), and the local-to-global sequence H¹(T_X⁰) → T¹_{QG}(X) → H⁰(T_X¹) → H²(T_X⁰) with H²(T_X⁰)=0 makes the middle map surject, so the all-nodes-smoothing direction (1,…,1) is realized to first order; H²(T_X⁰)=0 also gives unobstructedness so it integrates to an actual family with smooth generic fiber. Two things to confirm at the source rather than assert: that the cited Proposition 2.4(2) is stated for the singularity class including RDPs (it should be — RDPs are the mildest case, cf. Burns–Wahl local-to-global for RDP deformations), and that the surjectivity is used to hit the *simultaneous* smoothing direction (not merely a proper subspace). The mathematics is standard; the source text should be matched to these two points.

### Step 5 — ampleness persistence + Aubin–Yau

K_X ample on the canonical model (Bombieri, minimal general type, p_g=q=0, K²=2>0). K²_{X_t}=K²_X=2 is locally constant in the flat family, and ampleness is open, so K_{X_t} ample for small t≠0. X_t is a smooth projective surface with ample K_{X_t} (it is its own canonical model, no (−2)-curves), so Aubin–Yau applies directly, no orbifold subtlety: unique Kähler–Einstein ω with Ric(ω) = −ω, hence Riemannian h with Ric_h = −h. Sound. (The Riemannian Einstein constant of a Kähler–Einstein metric equals its Kähler-form constant, so λ = −1 as a Riemannian statement is correct.)

### Step 6 — Milnor-fiber identification

**(f) Is the A₁ Milnor fiber diffeomorphic to the resolution region?** Yes, and this is exactly where the RDP nature is essential. The A₁ minimal-resolution region is the O(−2) disk bundle over S² (self-intersection −2 of the exceptional ℂℙ¹), and the Milnor fiber of {u²+v²+w²=t} is T*S², whose zero section also has self-intersection −(χ(S²)) = −2. Both are the unique oriented rank-2 disk bundle of Euler number −2 over S², sharing the ℝℙ³ = L(2,1) link. So the two fillings agree over their common ℝℙ³ region and S ≅_diff X_t. This equality of Milnor fiber and resolution is special to du Val (ADE) points; for a general T-singularity the Milnor fiber differs from the resolution (this is the mechanism of rational blowdowns), and the identification would not hold. The note is correct to restrict to A₁ and to invoke this only there. The rigorous family-level statement is Brieskorn simultaneous resolution together with Ehresmann in this specific family; §7 treats it as classical, which is accurate for ADE, though a precise citation to simultaneous resolution would tighten it. The self-intersection/Euler-number arithmetic in the script (e=10, τ=−6, b⁺=1, b⁻=7, 12χ(O)=K²+e ⟹ e=10, strict Hitchin–Thorpe 2e−3|τ|=2>0) is internally consistent and matches a numerical Campedelli surface.

---

### Internal consistency across the two notes

The step50 note lists as unresolved "verify H⁰(Ω¹_S⊗K_S) ≅ … for the minimal resolution S," but step51 works entirely on the *singular* X with the reflexive T_X⁰. This is the correct object for Q-Gorenstein deformation theory (deformations of X, not S), and S enters only through the diffeomorphism X_t ≅ S. So step51's choice supersedes the step50 concern rather than leaving it open — worth stating explicitly so the resolution-vs-quotient framing is not read as a second unresolved item. The §10 Ishida–LeBrun scaling remark and §5/§10 peer-message flow corrections are unrelated to this six-step chain and do not bear on the Einstein-existence conclusion.

### Relation to the top research problem

This chain establishes, essentially unconditionally (modulo the two source confirmations and the non-hyperelliptic repair above), that one specific compact smooth 4-manifold carries an Einstein metric with λ=−1. Relative to Yau 26, note what this does and does not do: Yau 26 asks whether a two-sided Ricci pinching c_n g ≤ Ric_g ≤ C_n g on *some* metric forces existence of *some* Einstein metric. Producing an Einstein manifold does not by itself engage the pinching hypothesis (any Einstein metric trivially satisfies the pinching with its own constant, so such a manifold can never be a counterexample and is automatically consistent with the statement). The value here is as a member of a controlled family of Einstein manifolds and as confirmation that the complex-smoothing/Aubin–Yau route yields exact Einstein metrics on nodal-resolution 4-manifolds — a useful structural fact, and the note frames it correctly as an existence laboratory rather than a resolution of Yau 26. To connect this construction to the pinching implication one would additionally need either metrics on these manifolds that satisfy the pinching without manifest Einstein structure, or a mechanism relating the pinching hypothesis to landing in this deformation class.

### Summary of concrete items

1. Replace the reflexivity reason in §2.1(a) with the dual-sheaf fact (conclusion unchanged).
2. State the "free in codimension one" hypothesis and record the fixed-point derivation of "exactly six A₁," rather than importing it only as `6 = 8 − K²`.
3. Replace the non-hyperelliptic justification with the PGL₂(ℂ)-embedding argument (or compute H⁰(2K) directly by bicanonical Chevalley–Weil); this is the one load-bearing point whose written reason is insufficient, though the fact is true.
4. Confirm at the Lee–Park source that Proposition 2.4(2) covers RDPs and that surjectivity is invoked for the simultaneous all-node smoothing direction with unobstructed integration.
5. Optionally cite Brieskorn simultaneous resolution for the family-level ℝℙ³-matched diffeomorphism in §7.

The character computation, the Reynolds/Leray reduction, the equivariant Serre duality, the ampleness-persistence/Aubin–Yau step, and the A₁-specific Milnor-fiber identification are all correct as given.