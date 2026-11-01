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
    "Sessions/S1003A01/workspace/notes/step82_goldberg_levelset_SW_and_symmetric_closures.md",
    "Sessions/S1003A01/workspace/scripts/step82_sw_bochner_algebra.py",
    "Sessions/S1003A01/workspace/scripts/step82_sw_model.py",
    "Sessions/S1003A01/workspace/data/step82/sw_model.json",
    "Sessions/S1003A01/workspace/notes/step80_regularized_torsion_transport.md",
    "Sessions/S1003A01/workspace/notes/step81_normalized_sections_and_ddc_canonical_pairing.md",
    "Sessions/S1003A01/workspace/notes/step77_goldberg_first_tier_collapse_and_canonical_curve_identity.md"
  ]
}
```

## Task

Verify the new mathematics in Step 82 of a research programme on the closed negative-scalar Goldberg conjecture in dimension four: a closed almost-Kähler Einstein 4-manifold with s<0, is it Kähler? Read step82 note first; Steps 77, 80 and 81 supply the conventions. Check four things.

(1) Identity (82.1): X=dq/8−ReY, and the level-set identity (LS). Is it exactly equivalent to F(t)−16∫⟨X,n⟩=∫_{q<t}ρ? Is the family (82.2) correct, including the checked f=q identity? Is the claim correct that the trace equation fixes only div Y, with the trace-free ∇Y free through ∂_Dv?

(2) The exact identity (82.B), obtained by combining the Bochner identity, the f=q identity and the AAD balance. Check its dimensional restoration from the s=−1 computation.

(3) Section 3. Is LeBrun's Seiberg–Witten Weyl estimate ∫(s−√6|W⁺|)²≥72π²(c₁⁺)² correctly stated and applicable here? State precisely its hypotheses (b⁺>1, monopole class c₁, conventions for |W⁺|) and whether a different normalization of |W⁺| changes the conclusion. Check the reduction to ∫ψ₀≥18‖Hγ⁻‖², the forced multiplier λ=36, the null direction and second-order analysis, and the interpretation of the model value ∫ψ₀=520.13 against the slack bound 96.

(4) Proposition 82.H, the exclusion of cohomogeneity-one-type closures with locally homogeneous class-A principal orbits for closed negative Einstein metrics. Check the Euler-characteristic argument, the smoothness analysis at strata (free circle actions only, Seifert fibre for SL2R, the Nil/Sol/E(2) cases, SU(2) nuts and bolts with Bochner's Killing-field theorem), and whether the hypotheses are stated precisely enough. Mention any missing case, such as non-diagonal metrics, collapse of a 2-torus, or principal orbits that are only locally homogeneous with nontrivial holonomy.

Give a direct scientific memo: what is correct, what must be corrected, and the corrected statements.

## Output

# Verification memo on Step 82: level-set identity, identity (82.B), the Seiberg–Witten Weyl test, and Proposition 82.H

## Summary

- **Exact as stated:** (82.1), (LS), the family (82.2), the (80.S) and f=q specialisations, identity (82.B), and every algebraic step of §3.
- **Needs correction:**
  - the β level-set weight in §1;
  - the phrase "(82.2) is the complete content of the trace equation";
  - the dimensional form of the multiplier behind (82.B);
  - the hypotheses of Proposition 82.H.
- **New exact facts found while checking:**
  - ρ = −8Z_s.
  - The f=Heaviside member needs ∫ρ=0.
  - ψ₀+36Z_s has linear part 18v.
  - At second order the Seiberg–Witten inequality holds with margin 27Q₂/16 + 18B₂ − 9Q₂/16 > 0 even against the largest possible harmonic term.
  - Proposition 82.H carries real content only when no isometry group acts.

## 1. Identity (82.1), (LS), the family (82.2), and the trace equation

**(82.1) is correct.**
- Since s is constant, ∂r = ∂q/4, so ηα = ∂q/4 − Y.
- For real q, Re ∂q = dq/2, hence X = dq/8 − Re Y.
- For a (1,0)-form, Re Y and Im Y are J-rotations of one another with equal length, so |Re Y|² = |Y|²/2.
- This reproduces |dq − 8X|² = 64|Re Y|² = 32|Y|², consistent with Step 80.

**(LS) is exactly the flux identity.**
- Expanding |dq−8X|² gives |dq|² − 16⟨dq,X⟩ = 32|Y|² − 64|X|² = 32|Y|² − 16qe.
- On a regular level {q=t}, the outward normal of {q<t} is ∇q/|∇q|.
- So F(t) − 16∫⟨X,n⟩ = ∫_{q<t}ρ is a pointwise rewriting of the same flux, not an additional relation.

**A useful exact simplification:**

  ρ = 8e + 8v − |s|q/2 + 3q²/4 = −8Z_s,

so with (82.1) the trace equation reads

  div(16 Re Y − dq) = −8Z_s.

**Family (82.2) is correct.** Multiplying by f(q) and integrating by parts gives

  ∫fρ = −∫f′⟨dq, 16Re Y − dq⟩ = −∫f′(32|Y|² − 16qe).

- f = −1/h, with f′ = 1/h², gives (80.S) term by term.
- f = q gives 32∫|Y|² = ∫[8qe − 8qv + |s|q²/2 − 3q³/4], as written.
- The Heaviside member needs one correction. With f = H(q−t) one obtains ∫_{q<t}ρ − ∫_Mρ. So (LS) follows from it only together with ∫ρ = −8∫Z_s = 0 (the AAD balance), or by taking f = −H(t−q). Both choices are legitimate on a closed manifold and on the model, where ∫Z_s ≈ 3×10⁻³¹.

**Model values not reproducible from the supplied files.**
- The value 224.3047… = 32·736/105 for the f=q check is not produced by either Step-82 script. `step82_sw_model.py` computes no Y-quantity.
- One available ingredient: ∫|s|q²/2 = 6·170.667 = 1024 at s = −12.
- Reproducing the check also needs ∫qe, ∫qv and ∫q³.

**"The trace equation fixes div Y" must be corrected.**
- What the scalar equation fixes is the single combination 2 div Re Y − Δq/8 = −Z_s.
- It says nothing about div Im Y. On an almost-Kähler manifold, div(J·θ) is the ω-trace of dθ, and that is not supplied.
- (82.2) is not the complete content of the equation. It is the equation tested against functions of q only, i.e. its level-set averages.
- Testing against a general φ gives ∫φρ = −∫⟨dφ, 16Re Y − dq⟩. For dφ not parallel to dq this involves ⟨dφ, Re Y⟩, which is not of the form f′|Y|².

Corrected sentence: *(82.2) is the full content of the trace equation against test functions constant on the level sets of q; the pointwise equation is div(16Re Y − dq) = −8Z_s.*

**Trace-free ∇Y is free relative to E1′, E2 and the trace equation.** This is plausible and consistent with the jet analysis of Step 81:
- ∇Y contains Hess q;
- it contains ∂̄η, which E2 ties to ∂_Dv;
- it contains ∇α, whose symmetric part S is free.

However, it is a statement about the first-order system only. The second-order prolongation of δW⁺=0 together with the Einstein condition was not checked for further constraints on these jets. The assertion should say "not determined by E1′, E2 and (80.3)".

**The β level-set weight is wrong.** Let θ = d^c u be proportional to |∇u|(Jn)^♭. On the level set, take the orthonormal frame (Jn, e, Je) with e ⊥_ℂ n. Then θ∧β restricts to |∇u|·β(e, Je): it is β on the complementary J-plane span(n,Jn)^⊥, not β(n,Jn).

With P4 (β^{1,1} rank one, equal to q/4 on ℓ_α^⊥), complex-orthonormality gives |⟨n,w⟩|² + |⟨e,w⟩|² = 1. Hence

  ∫_{u<t} dd^c u∧β = ±∫_{u=t} |∇u|·(q/4)|n_α|² dA,

where n_α is the component of n in ℓ_α.

This agrees with P5. Since Δu = L(ℓ_α) + L(ℓ_α^⊥),

  Θ_u∧β = (q/8)Δu + 2⟨du,X⟩ − (q/8)(L(ℓ_α^⊥) − L(ℓ_α)) = (q/4)L_u(ℓ_α) + 2⟨du,X⟩.

So the interior integrand sees ℓ_α and the Stokes term sees n_α. Consequences:
- The split should read "(t/4)F_α(t) expressed through P5", not F_⊥.
- The consequence at a nondegenerate maximum, L_q(ℓ_α) ≤ 0, is unchanged.
- The conclusion that this adds no restriction on a closed manifold is also unchanged.

## 2. Identity (82.B)

**Inputs agree with Step 77.** Expanding Bo = −(s/2)|W⁺|² + 18 det W⁺:
- det(−r/2·I + V) = r²/4 − v/2, and adj = −r/2·I − V, which gives det W⁺ = r³/4 − rv/2 + re/2 + x;
- this reproduces Step 77's integrand (9/8)r²q + (s/2+9q/4)e + (−2s−9q/4)v + 18x;
- Bo vanishes at the Kähler point, as integrability on the model requires.

**Recomputation with |s| restored.**

| Term | Contribution |
|---|---|
| (9/8)r²q | s²q/32 − 3|s|q²/32 + 9q³/128 |
| −5|Y|², via the f=q identity | −5|s|q²/64 − (5/4)qe + (5/4)qv + 15q³/128 |
| −(\|s\|/2)Z_s | −s²q/32 + (\|s\|/2)(e+v) + 3\|s\|q²/64 |

Summing gives

  ∫[(5|s|/2)v + 18x + qe − qv − |s|q²/8 + 3q³/16].

This is exactly the right side of (82.B).

**Dimensional correction.** The subtracted multiple is (|s|/2)Z_s, not Z_s/2. Z_s has curvature dimension 2 and Bo has dimension 3. The coefficient is forced uniquely by cancelling the s²q term.

**Inherited inputs.**
- The left side rests on the Step-79 decomposition |∇W⁺|² = 5|Y|² + 10|∂v|² + 2|∂̄v+ηᾱ|², which is used as input here.
- The model value 339.81 comes from Step 79. The right side of (82.B) is not evaluated in any Step-82 artifact. It needs ∫x, ∫qe, ∫qv and ∫q³; for reference, (5·12/2)∫v = 480 at s = −12.
- The description of (82.B) as a consolidation that also holds on the model is correct: all densities vanish at the Kähler point and decay at the ACH end.

## 3. The Seiberg–Witten Weyl estimate

**Statement and hypotheses (LeBrun, Ricci curvature, minimal volumes and Seiberg–Witten theory, 2001).**
- M is closed and oriented with b⁺ ≥ 2.
- a is a monopole class, i.e. c₁ of a spin^c structure with nonzero Seiberg–Witten invariant.
- Then every metric satisfies ∫(s − √6|W⁺|)² ≥ 72π²(a⁺)², where a⁺ is the g-self-dual part of the harmonic representative.
- For symplectic M, Taubes makes ±c₁(J) a monopole class, and (a⁺)² is insensitive to the sign.
- For b⁺ = 1 a chamber condition is needed. It is irrelevant here because b⁺ > 1 is assumed.
- The original form is ∫((2/3)s − 2√(2/3)|W⁺|)² ≥ 32π²(a⁺)², identical after multiplying by 9/4.
- No source file is supplied, so the precise theorem number should be fixed from the paper.

**Normalization of |W⁺|.**
- |W⁺| is the norm of W⁺ as an endomorphism of Λ⁺. The constant √6 comes from λ_max ≤ √(2/3)|W⁺| for trace-free symmetric 3×3 matrices.
- The frame expression 3r²/2 + 2e + v is exactly this norm.
- Check: for Kähler–Einstein metrics |W⁺|² = s²/24, so s − √6|W⁺| = 3s/2 and ∫ = (9/4)s²V = 72π²c₁². This is the known equality case.
- A tensor norm Σ W_{ijkl}² is 4 times the endomorphism norm and would require replacing √6 by √6/2. The Kähler–Einstein equality fixes the constant uniquely, so the conclusions do not depend on the choice once it is consistent.

**Reduction is correct.**
- 72π²c₁² = (9/4)(s²V − 16T_AK).
- (c₁⁺)² = c₁² + |(c₁⁻)²|.
- With T_AK = ∫(v + 3q²/32), this gives ∫ψ₀ ≥ 72π²|(c₁⁻)²| = 18‖(Hγ)⁻‖².
- For closed γ, ⟨γ⁻, h⁻⟩ = ⟨Hγ, h⁻⟩ for every harmonic ASD form h⁻. So (Hγ)⁻ is the L²-projection of γ⁻ onto ℋ⁻, and ‖(Hγ)⁻‖² ≤ ‖γ⁻‖² = ∫q²/32.

**Linear parts and the forced multiplier.**
- With dW2 = −dq/8 + 2de + dv at the Kähler point and A = √(6W2) = 1/2 there, dψ₀ = 3dA + 36dv = −(9/4)dq + 36de + 54dv. The table entries are correct.
- Nonnegativity on the orthant q, e, v ≥ 0 forces λ ≥ 36 from the q-coefficient and λ ≤ 36 from the e-coefficient, so λ = 36.
- Additional fact: ψ₀ + 36Z_s has linear part exactly 18v. It is degenerate on the whole (q,e)-plane, not only along e = |s|q/16.
- The model data show this: ψ₀(0.99) < 0 while ψ₀+36Z_s(0.99) > 0. Near the end ψ₀ ≈ −9q, because e/q → 1/2 and v ≪ q at |s| = 12; the observed ratio is −7.9.

**Second order (recomputed by hand).** Take e = q/16 + aq², v = bq², x = cq² at s = −1.
- The linear term of W2 cancels: W2 = 1/24 + (3/32 + 2a + b)q².
- Hence ψ₀ ≈ (81/16 + 36a + 54b)q², Z_s = −(a + b + 3/32)q², and Bo ≈ (3/64 − a/2 + 2b + 18c)q².
- Eliminating ∫aq² with ∫Z_s = 0 gives ∫ψ₀ ≈ 27Q₂/16 + 18B₂.
- The Bochner condition ∫Bo ≥ 5∫|Y|² ≈ 5Q₂/32 becomes (5/2)B₂ + 18C₂ ≥ Q₂/16. Both statements in the note are correct.
- The note says only that 27Q₂/16 + 18B₂ ≥ 0. More holds: since 18‖(Hγ)⁻‖² ≤ 9Q₂/16 < 27Q₂/16, the inequality is satisfied against the largest possible harmonic term. In the small-torsion regime the SW Weyl estimate is therefore never active.
- The expansion assumes the pointwise state is near the null ray with a, b, c = O(1). It is a perturbative statement, as the note indicates.

**Model numbers are internally consistent.**
- ∫Z_s ≈ 0.
- T_AK = 16 + 3·170.667/32 = 32, matching ∫(|W⁺|² − s²/24) = −32.
- The largest harmonic term is 18·170.667/32 = 96.
- ∫ψ₀ = 520.13 equals ∫(ψ₀+36Z_s), as it must.
- The measure behaves like t⁻³dt and ψ₀ like t³ at the end, so the integral converges.
- The complex type of the mpmath output has zero imaginary part and is harmless.

**Interpretation.** It is correct that the inequality, evaluated on the model's densities, is satisfied with margin 424, and that perturbatively it has margin 18Q₂/16 + 18B₂. Two further points:
- The model is not closed, so this comparison is a density-transfer test, not an application of the theorem.
- The √(2/3)|W⁺| bound is an eigenvalue estimate. Replacing it by the actual W⁺-pairing with the canonical spinor brings one back to LeBrun's δW⁺ identity, which Proposition 77.1 already shows is (★). So no sharper SW Weyl variant along those lines is expected to add information.

## 4. Proposition 82.H

**The Euler characteristic argument is sound.**
- With orbit space [0,T], M is a union of two disk bundles over the singular strata B₁ and B₂, glued along N. Since χ(N) = 0, χ(M) = χ(B₁) + χ(B₂).
- If the orbit space is a circle, M is a mapping torus and χ(M) = 0.
- If one end is an exceptional 3-dimensional quotient N/ℤ₂ (an omitted case), it contributes 0.
- For Einstein metrics, 8π²χ = ∫(|W|² + s²/24) > 0 when λ ≠ 0. So χ ≤ 0 is already incompatible with λ < 0; "flat" is correct but more than needed.

**Smoothness at a stratum.**
- The normal sphere of a stratum of dimension 2, 1 or 0 is S¹, S² or S³ respectively.
- A 2-torus can never collapse smoothly, because T² is not a normal sphere. This settles the T²-collapse question for Nil, Sol, Ẽ(2) and ℝ³.
- A curve stratum forces N to fibre over S¹ with fibre S², which is not a quotient of a class-A group.

**Circle collapse.**
- The kernel of the limiting left-invariant form is a left-invariant field ξ. It descends to Γ\G, and its flow is right multiplication by exp(tξ).
- For a smooth bolt the flow must be free with a common period T. That requires g·exp(Tξ)·g⁻¹ ∈ Γ for all g, and since Γ is discrete, exp(Tξ) ∈ Z(G) ∩ Γ.
- Exceptional fibres produce cyclic quotient singularities ℂ²/ℤ_p.

This one uniform statement covers all the case work:
- **\widetilde{SL}₂:** the elliptic direction, with exp(2πξ) central. A cocompact Γ meets the centre in an infinite subgroup, so this is the Seifert fibration. Freeness requires the Fuchsian image to be torsion-free, and then χ(base) < 0. Hyperbolic and parabolic flows are not periodic.
- **Nil:** only the central direction; the base is T².
- **Sol and Ẽ(2):** Ad_g moves the abelian directions continuously, so no circle collapses, unless Ẽ(2) has trivial rotation part, which reduces to ℝ³.
- **ℝ³:** bases T² or Klein bottles.
- **SU(2):** every element of a finite Γ lies in a conjugate of the circle, so freeness forces Γ ⊂ {±1}, as the note states. Left multiplication then descends and preserves every g_t. The resulting isometries of the dense open set extend to M, because strata of codimension ≥ 2 do not change the length metric and Myers–Steenrod gives smoothness. Bochner's theorem then excludes λ < 0. This part is correct.

**Precision of the hypotheses.** The following should be stated explicitly:
1. Γ ⊂ G is a lattice acting on the left, and every g_t is left-invariant.
2. The identification of slices along normal geodesics carries left-invariant metrics to left-invariant metrics. The form dt² + g_t, with no shift term, is an assumption, not automatic for a locally homogeneous foliation.
3. M∖U is a union of closed submanifolds whose tubular neighbourhoods are mapping cylinders of fibrations N → B.

Non-diagonal metrics need no separate treatment: the argument uses only left-invariance.

**Genuine group actions are trivial for this result.** Whenever a compact group of positive dimension acts isometrically with cohomogeneity one, Bochner excludes λ < 0 immediately. The real content of 82.H is therefore the χ argument in the purely locally homogeneous case, such as Bianchi VIII, where no isometry group acts.

**Missing cases: N = Γ\X with Γ ⊂ Isom(X) not contained in G.**
- Examples include flat 3-manifolds with nontrivial holonomy, hyperbolic N, H²×ℝ geometry, S²×ℝ geometry, and lens spaces L(k,1) realised with Γ acting on the right.
- The χ argument extends unchanged. χ(M) > 0 needs a nut (N = S³) or a bolt S² or ℝP² (N a circle bundle over it). This forces S³ or S²×ℝ geometry. Every other geometry, including H³ warped products, which have no circle collapse, gives χ(M) ≤ 0.
- **S²×ℝ:** the slice metrics a(t)·g_{S²} + b(t)dz² are SO(3)-invariant, and the centralizer of Γ contains SO(3) or the ℝ-translations. So Killing fields exist.
- **S³ geometry, L(k,1) bolts:** freeness forces Γ to act through right isometries. That makes g_t right-U(1)-invariant (Berger), and SU(2)_L descends.
- **Not settled:** circle-bundle quotients S³/Γ over ℝP², or any other spherical N, carrying a Γ-invariant left-invariant metric whose centralizer in Isom₀ is finite. Closing this needs the explicit list of free circle actions on spherical space forms that are compatible with such metrics.

**Corrected statement.** Let M be closed with Ric = λg, λ < 0. Suppose an open dense U ≅ I×N carries g = dt² + g_t, with N compact and g_t locally homogeneous of a fixed Thurston type, and M∖U a union of smooth strata with mapping-cylinder neighbourhoods. Then such M does not exist if:
- the geometry is not S³ or S²×ℝ (by the χ argument); or
- it is S²×ℝ, or S³ with Γ ⊂ Z(SU(2)) or Γ acting through right isometries (by Bochner).

The remaining spherical subcase is as described in the last bullet above. The Bianchi-VIII and all class-A, Γ ⊂ G statements of the note are correct under hypotheses 1–3.