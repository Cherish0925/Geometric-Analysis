# Step 5 Erratum: Theorem 2 correction and revised gap identification

Session: S0910A02. Agent2/Constructor. Phase: Explore.

## Erratum for `step5_positive_branch_all_dimensions.md`

### 1. Theorem 2 is retracted as stated

**Theorem 2** claimed: for each n ≥ 2 and v > 0, there exists ε(n,v) > 0
such that δ_+(g) ≤ ε and Vol(M,g) ≥ v implies M admits an Einstein metric.

The proof has a critical gap at **Step 2.1** (harmonic radius lower bound).
Two-sided Ricci bounds + volume noncollapse + bounded diameter give only a
positive volume ratio for small balls, NOT a harmonic radius lower bound.
The reason: Weyl curvature can concentrate even under noncollapse (this is
the mechanism behind Einstein orbifold degeneration in dimension 4).

The harmonic-coordinate PDE argument in Step 2.1 is circular: it assumes
the existence of harmonic coordinates of definite size, which is precisely
the harmonic radius bound it claims to derive.

**Verified by TTCS:** both independent branches confirmed this gap. The
standard harmonic-radius theorems require at least one of:
- injectivity radius lower bound (Cheeger's lemma, needs sectional bounds)
- almost-Euclidean volume ratios (Anderson's ε-regularity)
- full curvature bounds |Rm| ≤ K
- direct harmonic radius assumption

None of these follows from Ricci bounds + noncollapse alone in dim ≥ 4.

### 2. Corrected theorem

**Theorem 2'.** For each n ≥ 2, v > 0, K > 0, there exists ε(n,v,K) > 0
such that if (M^n, g) is a closed connected smooth Riemannian n-manifold with

    δ_+(g) ≤ ε,    Vol(M,g) ≥ v,    |Rm_g| ≤ K,

then M admits a smooth Einstein metric h with Ric_h = λh, λ > 0.

*Proof.* Cheeger's lemma: |Rm| ≤ K and Vol ≥ v give inj(M,g) ≥ i_0(n,K,v,D).
Anderson's harmonic radius estimate then gives r_h ≥ r_0(n,K,v,D,i_0).
Steps 2.2–2.7 of the original proof follow. □

### 3. Corrected gap identification (three gaps, not one)

The original note claimed: "P_n^+ ⟺ collapse is Einstein-compatible."
This is wrong. The correct trichotomy for sequences with δ_+(g_i) → 0:

**(I) Noncollapsed, bounded curvature:** Vol ≥ v > 0, |Rm| ≤ K.
→ Theorem 2' gives Einstein on the same smooth manifold. **Solved.**

**(II) Noncollapsed, curvature concentration:** Vol ≥ v > 0, |Rm| → ∞.
→ GH limit is a singular space (Einstein orbifold with ALE bubbles in dim 4).
→ Need desingularization/gluing to recover Einstein on M_i. **Open.**

**(III) Collapsed:** Vol → 0, diam ≤ D(n).
→ GH limit is lower-dimensional. Need collapse structure + Einstein
compatibility. **Open.**

If P_n^+ fails, a counterexample sequence must lie in (II) or (III):
Theorem 2' excludes (I). Both (II) and (III) are genuine open gaps.

### 4. Additional corrections

**π_1 bound:** Theorem 1(d) erroneously stated that |π_1(M)| has a
dimension-only bound. This is false: round lens spaces S^3/Z_m have
Ric = g (so δ_+ = 0) but |π_1| = m → ∞. Myers only gives π_1 finite.
A quantitative bound |π_1| ≤ V_n(δ)/v requires the volume lower bound.

**b_1 = 0 and collapse:** The claim that b_1 = 0 prevents torus fibers in
collapse is misleading. Collapsed loops may represent torsion (as in lens
spaces), not free homology. b_1 = 0 only prevents free abelian directions.

### 5. What survives

- **Theorem 1 (precompactness):** Still valid for all n, with the π_1
  correction above.
- **Low-dimensional resolution:** n = 2 (uniformization), n = 3 (Hamilton)
  still valid because Ricci determines full curvature in these dimensions.
- **4D CGB accounting (Theorem 3):** Still valid. In dim 4, both gaps (II)
  and (III) involve curvature concentration filling the 8π²χ budget.
- **Topological filter:** Still valid. PSC excludes SW no-Einstein families
  from the positive branch.
- **Lean scoping:** Still valid.
- **Asymmetry positive vs negative:** Still valid but the positive branch
  now has TWO gaps (concentration + collapse), not one. The negative branch
  has THREE (diameter + concentration + collapse).

### 6. Revised program for P_n^+

The clean architecture from the TTCS generator, adapted:

**Regime (I):** Solved by Theorem 2'.

**Regime (II) approach:** In dim 4, Cheeger-Naber give codim-4 singular set
(isolated orbifold points). The limit is an Einstein orbifold with Ricci-flat
ALE bubbles. The question: can the desingularization (gluing back the
bubbles into a smooth Einstein manifold on M_i) be done? This is exactly the
Ozuch/Morteza-Viaclovsky territory, but for the positive branch (not negative).
Alternatively: can the orbifold singularities be shown to NOT form under
tight positive pinching? A quantitative obstruction-amplitude principle
(from the Calabi/gluing analysis of Step 1) might show that tight pinching
forces all first obstruction coefficients to zero.

**Regime (III) approach (generator's best strategy):** "Rewound noncollapse."
Seek a theorem that the universal cover does not collapse:
- Universal cover M̃ has Ric ≈ +g̃, π_1(M̃) = 1
- If Vol(M̃, g̃) ≥ ṽ > 0, apply Theorem 2' to M̃ (after controlling
  curvature on the cover)
- Einstein metric on M̃ may descend to M = M̃/Γ if the construction
  is Γ-equivariant (e.g., Ricci flow preserves isometries)

The central test: does simply connected positive near-Einstein ALWAYS
give noncollapse? Lens spaces show non-simply-connected collapse is
possible, but their covers (S^3) are noncollapsed.

## Files

- Original note: `workspace/notes/step5_positive_branch_all_dimensions.md`
  (to be read with this erratum)
- This erratum: `workspace/notes/step5_erratum_theorem2_correction.md`
- TTCS verifier branches:
  `trace/ttcs/results/step5_ttcs01_sub3_verifier.md`
  `trace/ttcs/results/step5_ttcs01_sub4_verifier.md`
- TTCS generator integration:
  `trace/ttcs/results/step5_ttcs01_generator1_integration.md`
