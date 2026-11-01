# TTCS Independent Branch Record

```json
{
  "step_id": 77,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step77_internode_kernel_block_framework.md",
    "Sessions/S0910A02/workspace/data/step77_scalar_decoupling_and_mu_vanishing.json",
    "Sessions/S0910A01/workspace/notes/step78_equivariant_diagonal_reduction.md",
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md"
  ]
}
```

## Task

Verify the following structural theorem about the Ozuch desingularization obstruction on the product orbifold (S²×S²)/Z₂ with Ric=Λg, Λ>0.

CLAIM: All local Ozuch second obstruction coefficients μ_k(ζ^ε) = 0 (k=1,2,3) at every A₁ node, for both chiralities ε, in every chirality pattern.

PROOF SKETCH:
1. The degree-4 del Pezzo Bl₄CP² admits KE metrics (Tian 1990). These approach the product orbifold along comparable-scale nondegenerate sequences with compatible (Kähler) EH insertions. Ozuch's necessary conditions t²μ_k = O(t^{5/2}) at comparable scales force μ_k = 0 (since μ_k is t-independent).
2. The reflection c(z,w)=(z̄,w) is an isometry fixing every A₁ node and exchanging chiralities. Since R⁺=R⁻ and ∇Rm≡0, local μ_k are c-equivariant, giving μ_k(ζ⁻) = μ_k(ζ⁺) = 0.
3. D₈ symmetry and ∇Rm≡0 give node independence.

POTENTIAL ISSUES TO CHECK:
(a) Does the del Pezzo KE desingularization truly approach the product orbifold at comparable scales? The four A₁ points have Z₂-permutation symmetry; does the family preserve this?
(b) Is μ_k truly t-independent in Ozuch's framework? The h₂ and h₄ equations (eqs (22)-(23)) define μ_k from the source Λ·eh - Q^(2)(h₂,h₂), which depends on the orbifold geometry and EH direction but not the scale t. Verify.
(c) Does the c-equivariance argument correctly identify μ_k(ζ⁻) with μ_k(ζ⁺)? The key point is that c maps the SD kernel basis to the ASD kernel basis while preserving the local curvature structure (since R⁺=R⁻).
(d) Is there any gap between 'existence of KE desingularization' and 'Ozuch's necessary conditions vanish'? Ozuch's equations are necessary for any nearby Einstein metric; the KE metrics exist; so the equations must be satisfied. But check whether the KE metrics are nondegenerate in Ozuch's sense (Definition 1.26).

## Output

## Verification memo: μ_k = 0 on (S²×S²)/Z₂ via the Kähler–Einstein degeneration argument

### 1. What actually carries the theorem, and what does not

The result μ₁ = 0 and the result μ₂ = μ₃ = 0 rest on **different** arguments, and this distinction should be kept sharp because the notes sometimes blur them.

**μ₁ = 0** is a clean algebraic fact. Lemma 2.14 / Biq16 Lemme 9 gives μ₁ = C·det(R restricted to ker R^ε). For R^± = diag(Λ,0,0) the kernel block is the zero 2×2 matrix, so det = 0. This is self-contained and I regard it as sound (assuming the cited lemma is transcribed correctly).

**μ₂ = μ₃ = 0 does not follow from the rank-one structure.** Your own step78 material makes this explicit and correct: the Eguchi–Hanson curvature modification d_e R⁻(H⁴) = 12 π_tr(ρ⊗ρ)/r⁶ is nonzero *inside* the kernel plane. I checked this matrix directly for ρ(ζ)⁻ = (0,c,s):
$$12(\rho\otimes\rho - \tfrac13 I)=\begin{pmatrix}-4&0&0\\0&12c^2-4&12cs\\0&12cs&12s^2-4\end{pmatrix},$$
whose kernel-block eigenvalues are 8 and −4, both nonzero. So R^− ρ(ζ)^− = 0 (leading term vanishes) but the deformation dR^− does live in the kernel plane and can feed μ₂, μ₃ through the full Biq16 expression. Step78 §5.3 states this correctly; the rank-one orthogonality is necessary and not sufficient. Consequently the **only** offered proof of μ₂ = μ₃ = 0 is the A02 Kähler–Einstein-existence argument. Everything hinges on that chain.

Note the internal tension the core agent must reconcile: A01/step78 §8 lists "verify μ₂ = μ₃ = 0 from the complete Biq16 formulas" as unresolved, while A02/step77 treats it as proven. These are not logically contradictory — they are two independent routes — but if the A02 route is valid it settles the matter regardless of Biq16. The reconciliation is: is the A02 route valid? That is the substance below.

### 2. The load-bearing chain (issues a, d)

The argument is: KE metrics on the smooth degree-4 del Pezzo degenerate to the orbifold KE metric on (CP¹×CP¹)/Z₂ with four compatible EH bubbles at comparable scales; Ozuch's necessary condition t²μ_k = O(t^{5/2}) then forces |μ_k| ≤ Ct^{1/2}; since μ_k is t-independent, μ_k = 0. This is a valid deduction **only if four separate links hold**, and two of them are asserted rather than established.

**Link A — the degeneration exists with the required structure.** This is geometrically plausible and I believe true, but it is not proven in the material. Supporting facts I can confirm: σ(z,w) = (−z,−w) is a holomorphic involution of CP¹×CP¹ with four isolated fixed points, so (CP¹×CP¹)/Z₂ is a complex orbifold with four A₁ points; the round product metric is KE, Z₂-invariant, and descends to an orbifold KE metric; the minimal resolution has χ = 4 + 4 = 8, b₂ = 6, K² = 4, i.e. a degree-4 del Pezzo (diffeomorphic to CP²#5C̄P²), which admits KE metrics (Tian). By Bando–Mabuchi uniqueness the symmetric member's KE metric inherits the full symmetry, forcing the four EH scales to coincide, so comparable scales (t_min/t_max = 1) is automatic *for the symmetric member*. By Odaka–Spotti–Sun-type compactification of del Pezzo KE moduli, K-polystable orbifolds appear as Gromov–Hausdorff limits, and A₁ bubbling produces exactly the Ricci-flat ALE space EH. So the picture is coherent. What is missing is an explicit statement, with citation, that this specific orbifold is a genuine KE degeneration limit of *smooth* degree-4 del Pezzo KE metrics. Until that is pinned, Link A is an educated expectation, not a theorem.

**Link D — Ozuch's necessary condition applies to this sequence.** This is the least-verified point. Ozuch Theorem 0.2 with remainder O(t^{5/2}) is a statement about degenerating Einstein sequences under a nondegeneracy hypothesis (Definition 1.26) and, crucially, under whatever assumptions his theorem places on the bubble configuration. The argument needs the theorem to hold for a **simultaneous four-node, comparable-scale** degeneration. The framework note invokes the multi-singularity extension (eq. (39)/(42)), which suggests multi-node is treated, but you must confirm that (i) comparable-scale multi-node degenerations fall inside the stated hypotheses of Theorem 0.2, and (ii) the symmetric KE degeneration meets Definition 1.26. If Definition 1.26 excludes exactly the highly-symmetric limits (a real possibility, since maximal symmetry sometimes coincides with degenerate spectral behaviour), the estimate would not apply and the deduction would not go through. This single point should be read off Ozuch's Definition 1.26 and the exact hypotheses of Theorem 0.2 verbatim before treating μ₂ = μ₃ = 0 as established.

**Link (compatible direction is in-kernel).** The deduction constrains only the EH direction that the KE degeneration actually realizes. The chain then relies on that direction lying in ker R⁺ = span{ω₂,ω₃}, so that (i) the KE existence forces μ_k = 0 there and (ii) the SO(2)-covariance argument (step78 §6) spreads vanishing to all in-kernel angles. The notes assert compatible ⟺ ζ⁺ ∈ ker R⁺ (step77_internode §2.1: a self-dual ζ⁺ shifts R⁻, orthogonal to a compatible receiver's block). This identification is internally consistent across the notes but should be confirmed against Ozuch's own definition of the Kähler-compatible insertion, since the whole spreading argument depends on it. The SO(2)-covariance itself is reasonable given ∇Rm ≡ 0 (the only local datum is the parallel R, invariant under rotation in span{ω₂,ω₃}), so μ₂,μ₃ form an SO(2)-covariant vector of constant magnitude — either identically zero or nowhere zero. The KE input then picks the zero alternative at one angle, giving all angles.

**Issue (b) — is μ_k t-independent?** Yes. In Ozuch's expansion the insertion is ζ = tφ, and λ_k(φ), μ_k(φ) are the coefficients of t and t² respectively, functions of the orbifold curvature at the node and of the unit direction φ, not of t. The source Λ·eh − Q^(2)(h₂,h₂) that defines the h₂/h₄ system depends on orbifold geometry and φ only. So the step "|μ_k| ≤ Ct^{1/2}, take t→0" legitimately forces the fixed number μ_k(φ_∞) to vanish. This link is sound.

**Issue (c) — c-equivariance to reversed chirality.** This is solid, and robust. c(z,w) = (z̄,w) is conjugation on the first factor: an orientation-reversing isometry of round S² (reflection across the equator), fixing the two poles; it fixes all four nodes, commutes with σ (cσ = σc = (−z̄,−w)), descends to the orbifold, and reverses total orientation, hence exchanges Λ⁺↔Λ⁻ and SD↔ASD. Since μ_k is an isometry invariant and c_*ζ⁺ is a reversed direction, μ_k(c_*ζ⁺) = μ_k(ζ⁺). Even if orientation reversal introduced a sign into μ_k, the conclusion is a vanishing, and ±0 = 0, so the extension to reversed chirality is unaffected by any orientation-sign subtlety. This link needs no further work.

### 3. Computational substrate — verified correct

I re-derived the SD/ASD tensor algebra used throughout. With factor 1 = coordinates (1,2), factor 2 = (3,4):
- ω₁⁺∘ω₁⁻ = diag(−1,−1,1,1) = −(g₁−g₂), factor traces (−2,+2), not factor-traceless. Matches the JSON exactly.
- ω₂⁺∘ω₂⁻ = diag(−1,1,−1,1), factor-traceless. Recomputed entry-by-entry; matches JSON.
- ω₃⁺∘ω₃⁻ = diag(−1,1,1,−1), factor-traceless. Matches.
- The curvature modification matrix in step78 §5.1 is reproduced exactly by π_tr(ρ⊗ρ) with ρ = (0,c,s).

So the factor-tracelessness of the in-kernel H⁴ (Theorem 3.1) and the scalar-decoupling conclusion are on firm algebraic footing, and the 37-angle numerical check (max factor trace 5.5×10⁻¹⁷) is consistent. The out-of-kernel ω₁ direction being the scalar-sector g₁−g₂ mode is also correct and confirms that scalar decoupling is specific to in-kernel directions.

### 4. Internal inconsistencies to fix (they affect credibility, not necessarily truth)

1. **Del Pezzo identification.** The degree-4 del Pezzo is Bl₅CP² (χ = 8, K² = 4, ≅ CP²#5C̄P²), not "Bl₄CP²" as written in step77_internode §1 and the JSON. Bl₄CP² is the degree-5 del Pezzo (χ = 7). The χ = 8 count of the resolution and the repair-note topology table (k=0 → CP²#5C̄P²) both point to Bl₅CP². This should be corrected; it is the surface the KE-existence argument actually relies on.

2. **Parameter count.** "4 complex smoothing parameters modulo (C*)², a 4-real-dimensional family" does not match the actual KE moduli of degree-4 del Pezzos, which is 2 complex (pencils of quadrics in P⁴ ≈ 5 points on P¹ mod PGL₂), i.e. 4 real. The real dimension coincides by accident, but the description is not derived. The argument does not need this count — one symmetric degeneration suffices — so I would drop the parameter bookkeeping rather than defend it.

3. **Two contradictory "Corollary 3.2" in step78.** One version states the full non-scalar spectral gap is Λ (mixed 1-form sector αᵢ⊙βⱼ has eigenvalue Λ, "TTCS correction"); the duplicated version and §7 state 3Λ/2. These cannot both stand. The value matters for the weighted inverse estimate; resolve which sector sets the gap.

4. **"Positive-definite non-scalar sector" is inaccurate.** The shape mode g₁−g₂ is trace-free, divergence-free, parallel — i.e. TT — with P(g₁−g₂) = −Λ(g₁−g₂), an eigenvalue below zero. Your own A_symmetry_check confirms it is A-even and "survives A-restriction." So on the A-invariant non-scalar sector, P is **not** positive-definite; it carries the unstable shape direction with eigenvalue −Λ (the classical instability of the product Einstein metric on S²×S²). The correct statement for the analytical continuation is **bounded invertibility** (spectrum away from zero, |−Λ| = Λ), not positive-definiteness. This is analytically adequate for an implicit-function argument, but the shape mode is a genuine deformation direction (relative sizing of the two spheres) that the construction must carry as a parameter or otherwise account for; the current summary that reduces everything to "positive-definite sector plus contraction" passes over it. This is a substantive point for whoever attempts the PDE continuation, not merely wording.

### 5. Relation to the top research goal

Both notes state plainly that this establishes at most that the product quotient is an unobstructed candidate at the controlled orders, and does not prove P₄⁺ or Yau-26. I concur, and I would add that the pattern-dependent inter-node coupling sits at order t³, below Ozuch's resolved O(t^{5/2}), so the finite-dimensional system is genuinely silent about which chirality patterns admit Einstein desingularizations. The μ_k = 0 result — even if fully secured — is a statement about local necessary conditions at one orbifold degeneration, and the sign-unrestricted, all-dimensional proposition remains untouched by it.

### 6. What would settle μ₂ = μ₃ = 0 definitively

Two independent routes, either of which closes the matter:

- **Secure Link D and Link A.** Read Ozuch Definition 1.26 and the exact hypotheses of Theorem 0.2, confirm that a symmetric four-node comparable-scale KE degeneration satisfies them, and cite (or prove) that (CP¹×CP¹)/Z₂ with its product orbifold KE metric is a Gromov–Hausdorff limit of smooth degree-4 del Pezzo KE metrics with EH bubbling and compatible in-kernel insertions. Then the deduction is rigorous.

- **Direct Biq16 evaluation of μ₂, μ₃.** This is self-contained and does not depend on the degeneration/nondegeneracy chain. Given the verified SD/ASD algebra and the explicit dR⁻ kernel block above, this appears computable in closed form at one angle (SO(2)-covariance then covers all angles, c-equivariance covers reversed chirality). Because it is independent of Links A and D, it is the more reliable of the two, and it is exactly the "decisive computation" your step78 §8 already names.

The strongest position combines them: the Biq16 computation as the primary proof, with the KE-existence argument as an independent confirmation once Links A and D are pinned to Ozuch's stated hypotheses.