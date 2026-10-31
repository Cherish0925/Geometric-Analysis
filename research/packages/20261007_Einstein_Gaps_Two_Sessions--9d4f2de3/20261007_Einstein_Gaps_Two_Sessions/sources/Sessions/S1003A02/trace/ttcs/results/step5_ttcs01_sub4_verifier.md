# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step4_O10_localization_and_orbifold_test.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Skills/geometric-analysis/research/paper/sections/variational_geometry.tex",
    "Skills/geometric-analysis/references/conventions-and-literature.md"
  ]
}
```

## Task

Check the proposed h=0 Einstein-gap theorem for minimal Kähler surfaces of general type: alpha=inf E should be zero by orbifold/ALE approximation; alpha is attained exactly when the underlying smooth four-manifold admits some Einstein metric, not necessarily Kähler; if K is ample Aubin-Yau supplies a negative Kähler-Einstein metric, while if K is nef nonample Kähler-Einstein attainment is impossible but non-Kähler Einstein existence may remain. Read the Step 4 Y-test and the actual Ozuch higher-order source. Determine precisely what Ozuch's first and second compact obstructions say for A1/Eguchi-Hanson resolution of a negative Kähler-Einstein orbifold. In particular, check whether the rank-one Kähler-Einstein curvature block automatically satisfies not just det R+=0 but also Ozuch's stronger second obstruction, and hence whether that source excludes or leaves open nearby non-Kähler Einstein metrics. Give a theorem with exact hypotheses and a corrected status of the unresolved part.

## Output

# Memo: the h = 0 Einstein-gap statement for minimal surfaces of general type, checked against Step 4 and Ozuch's higher-order paper (arXiv:2012.13316)

## Summary

- **The gap value.** α = 0 holds for every minimal surface of general type.
- **Attainment.** Attainment is equivalent to the existence of an Einstein metric with nonzero Einstein constant. That equivalence is elementary.
- **The K nef, non-ample case needs correcting.** In the proposal, "Kähler–Einstein attainment is impossible" was proved only for the fixed complex structure J. The underlying smooth manifold can still carry a Kähler–Einstein metric for a different complex structure J′. This happens whenever the canonical model has a smoothing, because the Milnor fibre of an ADE point is diffeomorphic to its minimal resolution.
- **Ozuch's two obstructions at an A₁ point.** At an A₁ point of a Kähler–Einstein orbifold with Λ < 0:
  - The first obstruction excludes the J-holomorphic (Kähler crepant) Eguchi–Hanson direction ζ ∝ ω. It forces ζ to lie in ω^⊥.
  - The second obstruction is then automatically satisfied, for every ζ in ω^⊥.
- **Consequence.** The source neither excludes nor constructs non-Kähler Einstein metrics near the orbifold.

## 1. α = 0 (the orbifold/ALE recovery)

**Setting.** Let (X,J) be minimal of general type and X₀ its canonical model. X₀ has only rational double points, which are C²/Γ with Γ ⊂ SU(2), and K_{X₀} is ample.

**Outside input.** The orbifold Aubin–Yau theorem gives a Kähler–Einstein orbifold metric g₀ with s = −4. This is the standard V-metric theorem of R. Kobayashi type. It is not among the supplied files and should be cited from its source.

**Gluing.** Kronheimer ALE metrics are Kähler for the minimal-resolution complex structure. Glue them in at length scale ε, with cutoff at r ~ ε^{1/2}.

**Correction to the Step 4 volume bookkeeping.** Step 4 says "cores have volume O(ε⁴)". Only the compact core has volume O(ε⁴). The Ricci-flat region inside the cutoff, ε ≲ r ≲ ε^{1/2}, has volume about r⁴ ≈ ε².

On that region Ric = 0, so the integrand is |Ric + g|² = |g|² = 4, not zero. The two error sources are then:

| Region | Volume | Integrand |
|---|---|---|
| Ricci-flat plateau | ~ ε² | \|Ric + g\|² = 4 |
| Transition annulus | ~ ε² | O(1): metric difference is O(r²) + O(ε⁴r⁻⁴) = O(ε), with second derivatives ~ ε/r² = O(1) |

Together they give ∫|Ric + g|² = O(ε²), and hence

  E(g_ε) ≤ ⨍|Ric + g|² = O(ε²) → 0.

The conclusion of Step 4 stands. The same argument works for all ADE types.

**Consequence for J.** The variational section's identity inf J = min{1, α} then gives inf J = 0 as well.

## 2. Attainment equals Einstein existence

Write E = 4 − I²/(VR). Cauchy–Schwarz gives

  I² ≤ V S ≤ 4V R,

with equality in the second step only when P = 0. Therefore E(g) = 0 if and only if Ric° = 0, s is constant and I ≠ 0. That is, g is Einstein with λ ≠ 0. A Ricci-flat metric has E = 4.

For p_g ≥ 1, the canonical-class monopole gives S ≥ 32π²A > 0 for every metric. This excludes R = 0 and forces λ < 0. For p_g = 0 (b⁺ = 1), the same conclusion needs the chamber argument; this should be stated as a separate input.

So "α is attained iff M admits an Einstein metric" is correct, and the Einstein constant is necessarily negative.

## 3. The K nef, non-ample case: the error and its correction

**What is true for the fixed J.** (Y,J) has no Kähler–Einstein metric, because K_Y · E = 0 on every (−2)-curve E.

**Why that does not settle the smooth manifold.** The statement about M also has to consider other complex structures. Suppose X₀ admits a small deformation X_t whose fibres are smooth. Then:

- K_{X_t} is ample, since ampleness is open.
- X_t is diffeomorphic to Y, by Brieskorn–Tyurina: the ADE Milnor fibre is diffeomorphic to the minimal resolution.
- Aubin–Yau gives a Kähler–Einstein metric on X_t, and hence an Einstein metric on the smooth manifold Y.

In that case Y is not a "both outcomes live" test. The Step 4 orbifold-limit test is a genuine test only when no complex structure on M (in either orientation) has ample canonical bundle.

The supplied material exhibits no such M. Whether such M exist is itself part of the open question.

## 4. Ozuch's compact obstructions for A₁ (Eguchi–Hanson) resolution, Λ < 0

**Conventions.** R^± is curvature acting on Λ^±. We have R⁺ = W⁺ + (s/12)·Id and tr R⁺ = s/4 = Λ, consistent with the form diag(0,0,Λ) in Thm 0.2. The bubble eh_{ζ⁺} glued in the complex orientation (ASD curvature, ζ ∈ Λ⁺) is tested against R⁺(p).

**First obstruction (Biq13 / Ozu19b; proof of Thm 0.2, eq. (54)).** The obstruction coefficients are

  λ_k = c⟨R⁺(H₂)ζ, ζ_(k)⟩, k = 1, 2, 3.

Requiring all λ_k = 0 means R⁺(p)ζ_∞ = 0. In words, the limiting gluing direction lies in ker R⁺(p).

**Second obstruction (Lemma 2.14; Thm 0.2; Prop 0.4).** Write the block of R⁺(p) on ζ^⊥ as [[R₂₂, R₂₃], [R₃₂, R₃₃]]. Then

  μ₁ = C · det [[R₂₂, R₂₃], [R₃₂, R₃₃]],

and μ₁ must vanish. For Λ ≠ 0 the diagonal entries satisfy a₂ + a₃ = Λ. So det = a₂(Λ − a₂) vanishes exactly when R⁺(p) = diag(0, 0, Λ). Equivalently, W⁺(p) has eigenvalues (s/6, −s/12, −s/12).

This second obstruction is proved only under extra hypotheses:

- either one singular point and a rigid orbifold (Thm 0.2(2));
- or a transverse sequence (Prop 0.4(1));
- or one singular point and a nondegenerate sequence (Prop 0.4(3)).

Integrable Einstein deformations of g₀ are assumed throughout. For a Kähler–Einstein orbifold with Λ < 0, this amounts to unobstructedness of the orbifold (equisingular) complex deformations.

**Evaluation at a Kähler–Einstein point.** Use the basis (ω̂, Re θ, Im θ) of Λ⁺, where ω̂ is the normalized Kähler form and θ a local holomorphic (2,0)-form. In this basis

- W⁺ = diag(s/6, −s/12, −s/12),
- R⁺ = diag(s/4, 0, 0) = diag(Λ, 0, 0),
- ker R⁺ = ω^⊥, which is two-dimensional.

The two obstructions then act as follows:

- **First obstruction.** It holds if and only if ζ_∞ ⊥ ω.
- **Second obstruction.** For ζ ∈ ω^⊥, write ζ^⊥ = span(ζ′, ω̂) with ζ′ ∈ ker R⁺. The block of R⁺ on ζ^⊥ is diag(0, Λ), whose determinant is 0. So μ₁ = 0 identically, for every admissible ζ. This is Ozuch's remark that form (4) "is typical of Kähler–Einstein metrics".

**Geometric meaning of the gluing direction.** The exceptional sphere of eh_ζ is holomorphic for the complex structure ζ/|ζ|. This follows from the metric on S² in Prop. 1.16(4), which spans a J_ζ-invariant plane.

- *ζ ∝ ω (the J-holomorphic crepant resolution).* Here λ₁ ∝ Λ|ζ| ≠ 0, so the first obstruction already excludes this direction. This is the analytic form of K_Y · E = 0, i.e. of K_Y failing to be ample.
- *ζ ⊥ ω (the admissible directions).* Here the sphere is ω-Lagrangian, which is the vanishing-cycle (smoothing) configuration. The admissible directions form ω^⊥ ≅ C per point, matching the A₁ versal parameter t in xy = z² + t.
- *Dimension count.* This matches Ozuch's count: a two-dimensional kernel gives a two-dimensional set of transverse desingularizations that are Einstein to o(t²), in correspondence with the kernel.

**Consistency check.** Kähler–Einstein metrics on smoothings X_t → X₀ are Einstein sequences on Y. They must satisfy, and do satisfy, both obstructions.

**Reversed orientation.** Gluing Eguchi–Hanson in the opposite orientation is tested by R⁻ = W⁻ + s/12 at p. That gives a different manifold, not Y.

**What the source does not cover:**

- The global orbifold obstructions ν_l (Prop. 2.10, 2.19, Remark 2.20) are not evaluated for Kähler–Einstein orbifolds.
- Only "the first two obstructions of an infinite list" are identified.
- Ozuch explicitly raises whether such limits must be Kähler (abstract; Question 0.8 in the Ricci-flat case).
- A_k with k ≥ 2 involves curvature derivatives (Remark 2.21), and D_k, E_k appear only by remark. Step 4's general A_{k−1} chains are therefore beyond what the read text proves.
- The analysis assumes the bubble is Eguchi–Hanson. Uniqueness of Ricci-flat ALE metrics on R⁴/Z₂ is conjectural (Remark 0.1).

So the source excludes non-Kähler Einstein metrics near X₀ only in the J-holomorphic bubble direction. All smoothing-type directions remain open at the order computed.

## 5. Corrected theorem

**Theorem (h = 0).** Let M be the oriented manifold underlying a minimal compact complex surface of general type with p_g ≥ 1, and put A = c₁² > 0. Then:

1. **Gap value.** α(M) = inf E = inf J = 0.
2. **Attainment.** E(g) = 0 if and only if g is Einstein with λ ≠ 0. Every Einstein metric on M has λ < 0. Hence α is attained if and only if M carries an Einstein metric.
3. **Kähler–Einstein attainment.** α is attained by a Kähler–Einstein metric if and only if some complex structure J′ on M (or on M̄) has ample canonical bundle. This holds when K_J is ample (Aubin–Yau). It also holds when K_J is nef and not ample but the canonical model X₀ admits a smoothing. For the fixed J with K_J non-ample, no J-Kähler–Einstein metric exists.
4. **Local statement near X₀.** Suppose:
   - X₀ has only A₁ points;
   - its Kähler–Einstein orbifold metric g₀ has integrable Einstein deformations;
   - g_n are Einstein metrics on M = Y converging in the Gromov–Hausdorff sense to (X₀, g₀), bubbling Eguchi–Hanson metrics in the complex orientation.

   Then every limiting period direction satisfies ζ_{∞,j} ⊥ ω(p_j). In particular the J-holomorphic resolution direction cannot occur. Ozuch's second obstruction is then automatically satisfied. Under the transverse or nondegenerate hypotheses of Prop. 0.4, it imposes nothing further.

**Open part.**

- **(i) Existence.** Existence of Einstein metrics on such M that admit no ample-K complex structure. Whether such M exist is itself open in the supplied material.
- **(ii) Near X₀.** The higher local obstructions and the global obstructions ν_l for smoothing-type configurations ζ ⊥ ω, including the case where X₀ has no global smoothing. One plausible mechanism, not proved in the source, is that these obstructions reproduce the complex local-to-global (H²(T)) smoothing obstruction.
- **(iii) Away from X₀.** Even complete nonexistence near X₀ would not decide (i). Einstein metrics on M need not be Gromov–Hausdorff close to X₀, and E-minimizing sequences carry no compactness forcing them to be.

**Text in Step 4 §5 to revise:**

- "Y has no Kähler–Einstein metric" should read "(Y,J) has no Kähler–Einstein metric".
- "The leading obstruction is satisfied" should read "the leading obstruction is satisfied exactly for ζ ⊥ ω, and is violated by the Kähler-resolution direction".
- "Both outcomes live" holds only when M admits no ample-K complex structure.