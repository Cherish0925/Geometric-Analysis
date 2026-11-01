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
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md",
    "Sessions/S1003A01/workspace/scripts/step62_zero_prolong.py",
    "Sessions/S1003A01/workspace/scripts/step62_phi_identity.py",
    "Sessions/S1003A01/workspace/scripts/step62_det_formula.py",
    "Sessions/S1003A01/workspace/data/step62b/phi_prediction.json",
    "Sessions/S1003A01/workspace/data/step62/linear.json",
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md",
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md"
  ]
}
```

## Task

Verify Theorem 62.A and Corollaries 62.B/62.C in the attached note (closed negative Goldberg problem, four-dimensional Einstein almost-Kahler geometry). Check carefully: (1) the Weitzenbock identity for a harmonic self-dual 2-form of constant length |Omega|^2=2 and q=4<W+u,u>-2s/3; (2) the Derdzinski/Einstein Weitzenbock formula nabla^*nabla W+ = -(s/2)W+ + 6(W+)^2 - 2 tr((W+)^2) Id in the endomorphism normalization where a Kahler surface has W+ spectrum (s/6,-s/12,-s/12) (confirm by testing on Kahler and on the integrated identity int|nabla W+|^2 + (s/2)|W+|^2 - 18 det W+ = 0); (3) the computation at a torsion zero giving |nabla^2 Omega|^2 = 4 trV^2 - 12|eta|^2, including the claim that nabla^2 Omega(p) takes values in Omega^perp inside Lambda^+; (4) the translation into the first-jet parametrization f=cz+(S+A)zbar, the cone ||A||^2=8|c|^2+||S||^2 (using the numerically determined proportionalities |eta|^2=|m_c|^2/8, trV^2=|m_A|^2/4, |m|^2/2=|nabla^2 Omega|^2, Frobenius ratios 4|c|^2:2||A||^2:2||S||^2), and the index bound det_R Df >= 25|c|^4 via |det S|<=||S||^2/2. Assess whether 'every nondegenerate torsion zero has index +1' follows rigorously, and whether the numerical continuation evidence (section 3) is consistent with the cone being the complete first nonlinear compatibility. Point out any sign/normalization error or hidden assumption (e.g. orientation of E, identification of c with eta, whether the S/A split used in the determinant matches the U(2) split used numerically). Also say whether this identity or index law appears to be known (Armstrong, AAD, Kim) as far as the supplied sources show; do not invent literature.

## Output

# Verification memo on Step 62: Theorem 62.A, Corollaries 62.B and 62.C, and the D=4 continuation evidence

## Summary

- **Theorem 62.A is correct.** Every constant can be traced independently: the round S⁴, the Kähler test, and the exact Gibbons–Hawking germ.
- **Corollaries 62.B and 62.C follow** from 62.A once two data are in place:
  - A02's kernel structure for the first jet;
  - two U(2)-equivariant proportionality constants.
- **The proportionality constants.** Schur's lemma makes them exist. Their values are currently fixed by floating-point linear algebra, agreeing to about 10⁻¹⁶. The Gibbons–Hawking germ certifies the A-versus-S constant exactly. The c-constant (η) is certified only numerically, by the D=4 continuations. It is not certified by the Gibbons–Hawking germ, contrary to the note's wording in §3.
- **The index law needs only necessity of the cone.** Necessity follows from 62.A. The D=4 statement that the cone is the *complete* compatibility is numerical, and it is not needed for index +1.

## 1. Weitzenböck identity for Ω

- On Λ⁺ one has Δ = ∇*∇ − 2W⁺ + s/3.
- **The s/3 term.** On the unit S⁴ (s=12), the 2-form Weitzenböck term is p(n−p)=4=s/3.
- **The factor 2 is tied to the spectrum convention.** A parallel Kähler form forces 2W⁺ω=(s/3)ω, so W⁺ω=(s/6)ω. This matches (s/6, −s/12, −s/12).
- **Derivation of q.** Harmonicity gives ∇*∇Ω = 2W⁺Ω − (s/3)Ω. Because |Ω|² is constant, ⟨∇*∇Ω,Ω⟩ = |∇Ω|². Hence q = 2⟨W⁺Ω,Ω⟩ − (s/3)·2 = 4r − 2s/3.
- **At a zero:** r = s/6.
- **Agreement with AAD:** |∇Ω|² = 4|a|², from ∇Ω = a⊗φ − Ja⊗Jφ with |φ|²=2.

## 2. The Derdziński formula ∇*∇W⁺ = −(s/2)W⁺ + 6(W⁺)² − 2tr(W⁺²)Id

Write the formula in general form, aW⁺·s + b((W⁺)² − ⅓tr(W⁺²)Id).

- **Kähler test (constant s, W⁺ parallel).** The left side vanishes. On the right, the uu-entry is a·s·(s/6) + b·s²/72 = 0, so a = −b/12.
  - With b=6: −(s²/24)diag(2,−1,−1) + (s²/24)diag(4,1,1) − (s²/12)Id = 0. ✓
- **Integrated form.** Pair with W⁺ and use tr(W⁺)³ = 3det W⁺ for trace-free 3×3. This gives ∫|∇W⁺|² + (s/2)|W⁺|² − 18det W⁺ = 0 in the endomorphism norm, which is the standard form. The Kähler test alone fixes only the ratio a/b.
- **Scale b, fixed exactly by Gibbons–Hawking.** Keeping b free, the computation at a zero gives
  −2|∇²Ω|² = 4[(b/3 + 4)|η|² − (b/3)trV²].
  The Gibbons–Hawking germ has |∇²Ω|² = 8 (half_norm), W₃=(1,0), so trV² = 2, and η = 0. Then 16 = 8b/3, so b = 6. ✓
  This test is independent of literature normalizations.
- **Role of Einstein.** Here it enters only through δW⁺=0, the vanishing of the Ric₀ coupling in the Λ⁺-bundle curvature, and constant s.

## 3. Computation at the zero

- **Algebra.** (W⁺²)_uu = s²/36 + |η|² and tr W⁺² = s²/24 + 2|η|² + trV² (the cross term −r·trV vanishes). Hence ⟨∇*∇W⁺u,u⟩ = 2|η|² − 2trV². ✓
- **Product rule.** ∇*∇⟨W⁺u,u⟩ also contains −4Σ⟨(∇ᵢW⁺)∇ᵢu,u⟩ − 2Σ⟨W⁺∇ᵢu,∇ᵢu⟩. Both vanish at p. The remaining term is 2⟨W⁺(2W⁺u − (s/3)u),u⟩ = 4|η|². ✓
- **Laplacian of q.** ∇*∇q(p) = 2⟨∇*∇∇Ω,∇Ω⟩ − 2|∇²Ω|² = −2|∇²Ω|². ✓
- **Result:** |∇²Ω|² = 4trV² − 12|η|². ✓ The λ-cancellation is genuine.
- **∇²Ω(p) ∈ Ω^⊥ ∩ Λ⁺.**
  - Differentiating ⟨∇_lΩ,Ω⟩ = 0 gives ⟨∇_k∇_lΩ,Ω⟩ = −⟨∇_lΩ,∇_kΩ⟩ = 0 at p.
  - ∇ preserves Λ⁺.
  - The numerical value Nomega_max_on_K ≈ 8·10⁻¹⁶ agrees.
  - The proof of 62.A does not use this fact. The normalization |∇²Ω|² = |m|²/2 does use it: with ∇_k∇_lΩ = (N^φ φ + N^ψ ψ)/2 and |φ|² = |ψ|² = 2, one gets |∇²Ω|² = (|N^φ|² + |N^ψ|²)/2. ✓
- **Corollary 62.B, items 2 and 3.** These follow from 62.A directly, with no parametrization:
  - W₃⁺(p)=0 forces trV²=0, hence |∇²Ω|² + 12|η|² = 0.
  - |W⁺|² − s²/24 = 2|η|² + trV² follows from the trace computation.
- **Corollary 62.B, item 1.** "A ≠ 0" needs trV² > 0 at a zero with nonzero first jet. This holds because trV² = |∇²Ω|²/4 + 3|η|². It also needs injectivity of A ↦ W₃⁺, which holds: trV² eigenvalues on the A sector are 0.25, 0.25.

## 4. Translation to f = cz + (S+A)z̄ and the index bound

**Sector identification is forced by representation theory.**
- Under z ↦ Uz, B transforms by congruence, B ↦ ŪBUᵀ. So symmetric versus antisymmetric is a U(2)-invariant splitting into Sym² (complex rank 3) and Λ² (rank 1).
- An equivariant curvature map must therefore kill S and be injective on A. This is consistent with the numerics: dim S = 6, dim A = 2, and the kernel of (η, W₃) in L_anti is 6-dimensional.
- The 2-dimensional C-linear block is the only 2-dimensional piece of L. Hence the scalar c is matched to η regardless of the linear/antilinear conventions.
- The code's J-commuting part of F (map v ↦ ∇_v a) corresponds to the z̄-type part of α = a + iJa or its opposite, depending on convention. The dimension count 2+8 removes the ambiguity.

**Common Frobenius constant.**
- m relates to the real Jacobian of f through a fixed C-linear or C-antilinear conformal map on the target, so all sector norms carry one common factor.
- |N^ψ| = |N^φ| identically, since N^ψ is the J-rotation of N^φ.
- The ratios 4|c|² : 2‖A‖² : 2‖S‖² are exact (sympy, `step62_det_formula.py`).
- Hence Φ = 2|m_c|² − ½|m_A|² + ½|m_S|², which is proportional to 8|c|² − ‖A‖² + ‖S‖².
- Note that `phi_prediction.json` evaluates the predicted quadratic form on the numerical G. It confirms the arithmetic of the translation, not the identity itself.

**Orientation.**
- Complex conjugation on C² has real determinant +1, so on complex rank 2:
  - every C-linear or C-antilinear identification preserves orientation;
  - J and −J give the same orientation, e₀e₁e₂e₃ = Ω²/2.
- Twisting by Λ^{0,2} is C-linear. So sign det(∇a) in Ω-oriented frames is the local index of T in E = Λ^{0,1}⊗Λ^{0,2} with its complex orientation.
- The global count also checks. The roots of E are 2x₁+x₂ and x₁+2x₂, so c₂(E) = 2c₁² + c₂ = 5χ + 6τ. ✓

**Determinant.**
- det B = det S + a², since (s₂+a)(s₂−a) = s₂² − a².
- On the cone, det = 9|c|⁴ + |det B|².
- For complex symmetric 2×2, |det S| = σ₁σ₂ ≤ ‖S‖²/2.
- |a|² = 4|c|² + ‖S‖²/2, so |det B| ≥ 4|c|² and det ≥ 25|c|⁴. ✓
- **Degenerate stratum:** c = 0, σ₁ = σ₂, det S = −a². ✓
- **A shorter route.** The cone gives ‖S‖² − ‖A‖² = −8|c|² ≤ 0. This violates A02's necessary condition for index −1 in Proposition 75.I, namely ‖S‖² − ‖A‖² ≥ 2|det B|.

**Rigor of "index +1 at every nondegenerate zero."**
The argument chain is:
1. 62.A, which is proved.
2. The first jet lies in ker σ(𝒫). This uses A02's Theorem 75.H, which needs Ric''=0. At a zero, the quadratic |a|² term in (75.2) vanishes to second order.
3. |η|² = κ_η|c|² and trV² = κ_V‖A‖², with a common Frobenius factor μ.

The existence of κ_η and κ_V follows from Schur's lemma. Their values (1/8 and 1/4 in m-units) come from SVD and pseudoinverse at about 10⁻¹⁶.
- The Gibbons–Hawking germ certifies κ_V/μ exactly, through the A-versus-S balance at c=0.
- κ_η is certified only by the on-cone c+A continuations, which converge to about 10⁻³⁰ for both seeds and both λ, together with the non-convergence of off-cone pure-c targets.
- The note's sentence that the Gibbons–Hawking germ is "an independent check of every constant in Theorem 62.A" is inaccurate: it does not test the −12|η|² coefficient.

A rational recomputation of G removes the remaining floating-point dependence. This means evaluating the degree-2 jet map to (η, W₃) in sympy, which is a small linear system. Alternatively, a hand derivation from the Ω- and Λ^{0,2}-components of (75.2) would do. Either upgrades 62.B(1) and 62.C to fully exact status.

**Proof-text issues.**
- `step62_zero_prolong.py` docstring. It says Mmat = ⟨∇∇Ω, φ⟩/2 = ∇_k a_l. The code computes the form inner product, which equals 2∇_k a_l. This is harmless for signs and the cone, but the docstring is wrong.
- **η normalization differs from Step 59.** Step 62 uses the matrix entry, |η|² = X₁X₂(w₁−w₂)². Step 59 uses |η|² = 2X₁X₂(w₁−w₂)². By contrast, Step-62 trV² equals Step-59 |W₃⁺|²_HS exactly: the u^⊥ eigenvalues are ±(X₂w₁+X₁w₂−w₃)/2. Any combination of 62.A with the AAD balance (|η|² + 2|W₃⁺|² + …) must convert η by a factor of 2.
- **AAD balance statement.** The note says the integral of the Laplacian identity is "the familiar AAD torsion balance." No computation supplied here shows this. Integrating the full expression for ∇*∇q away from Z gives some integral identity; matching it term by term to AAD's balance remains to be done. The exact Step-59 pair would test it.
- **Gibbons–Hawking degeneracy.** That the GH zero lies on the degenerate stratum (det S = −a² exactly) is asserted. The determinant value in `gh_D4.json` is not among the supplied files. The supplied data show only c ≈ 0 and |m_A| = |m_S|, which is consistent with but weaker than degeneracy.

## 5. The continuation evidence (§3)

- **D=4 is the right order.** E3 to degree 2 contains the second derivatives of curvature, that is, the 4-jet of g. This is exactly where ∇*∇W⁺(p) and Hess q(p) appear.
- **Pattern is consistent with a single quadratic obstruction Φ:**
  - every on-cone target converges to about 10⁻³⁰, including generic c+A+S with det > 0 at λ = −1 and λ = 0;
  - every off-cone target stalls at 10⁻⁵ to 10⁻³;
  - res² scales as t⁴ (8.2·10⁻⁶ to 1.2·10⁻⁴ from t=0.2 to 0.4, ratio 14.6 versus 16).
- **What is not shown.** Stalling under Levenberg–Marquardt with 60 iterations is not a proof of inconsistency.
- **An exact certificate of "the cone is the complete compatibility at D=4"** would consist of:
  - (a) the cokernel of the linearized degree-≤4 system at the Kähler germ, restricted to equations involving degree-4 unknowns, is 1-dimensional;
  - (b) contracting the quadratic terms with that left null vector gives a multiple of Φ;
  - (c) on the cone, the remaining system is solvable. Here the continuation data serve as evidence.
- **Higher orders are open.** Restrictions on the first jet arising at D ≥ 5 are not excluded. The D=5 runs are still pending.
- **Logical independence.** The index law uses only necessity, which is 62.A. So it does not depend on any of the above.

## 6. Substance still open for the global problem

- **Scope of the local law.** It covers nondegenerate zeros only. Degenerate isolated zeros (c = 0, equal singular values) and zeros of order ≥ 2 can carry other local degrees. The order-≥2 family is f_i = z_i h_{m−1}(z̄) + g_i(z̄). Purely antiholomorphic leading terms give positive degree; mixed ones need not.
- **Consistency with the global count.** Since 5χ + 6τ > 0, the sum Σ ind = 5χ + 6τ is consistent with all zeros being +1. The law removes index-(−1) cancellation, but it gives no contradiction by itself.
- **No sign of λ.** λ is absent from 62.A, so the identity holds equally for λ ≥ 0. Any λ < 0 mechanism must come from higher jets or global input.
- **The next-order analogue.** The analogue of 62.A for zeros with vanishing first jet comes from ∇*∇ applied twice, or from the degree-3 Hessian trace. This is the natural object for the degenerate strata.

## 7. Literature position (supplied sources only)

- **AAD**, as summarized in A02 Step 75: the Weitzenböck formulas, the U(2) curvature decomposition, the integral balance, and the identity κ − s = 6|a|². No supplied passage contains a pointwise identity at a torsion zero or an index law.
- **Armstrong (2002):** only publisher metadata was retrievable (Step 59 §4), so no comparison is possible.
- **Kim:** no supplied source.
- **Inside the sessions:**
  - the determinant formula (75.5) and the index-(−1) necessary condition are A02 Step 75;
  - the cone ‖A‖² = 8|c|² + ‖S‖² and its consequence det ≥ 25|c|⁴ appear first in this note.
- Whether either is known in the wider literature cannot be decided from the supplied material.