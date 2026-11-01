# TTCS Independent Branch Record

```json
{
  "step_id": 63,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step63_SU2_nut_and_clean_zero_surface.md",
    "Sessions/S1003A01/workspace/scripts/step63_bianchiIX_nut_series.py",
    "Sessions/S1003A01/workspace/scripts/step63_nut_component.py",
    "Sessions/S1003A01/workspace/scripts/step63_nut_q.py",
    "Sessions/S1003A01/workspace/data/step63/bix_nut_series_order5.json",
    "Sessions/S1003A01/workspace/data/step63/bix_nut_component.out",
    "Sessions/S1003A01/workspace/notes/step62_torsion_zero_prolongation.md"
  ]
}
```

## Task

Independently check the Step-63 diagonal Bianchi-IX regular-nut calculation and its mathematical interpretation for the closed negative-scalar Goldberg problem. Read the note and exact scripts/data. Verify: (i) the u=t^2 Einstein and closure equations and regular-nut parameter count; (ii) whether the exact L1,...,L5 ideal and Singular localization really exclude all interior three-weight, genuinely triaxial branches through this order; (iii) whether the three associated components are exactly permutations of the stated complex-hyperbolic Kähler branch, including the closed-form sinh identification and q=0; (iv) what is proved versus only suggested about all-order formal or analytic branches. Identify any normalization, smoothness, ideal-theoretic, or overinterpretation errors and give corrected theorem wording.

## Output

# Verification memo: Step 63 diagonal Bianchi-IX regular nut

## Summary

The main conclusion of the Step-63 note is correct, and in one direction it is stronger than the note states. Three corrections are needed:

1. The full ideal has dimension **one**, not two. The value reported as dimension two comes from the auxiliary Rabinowitsch variable `z`.
2. The minimal associated primes are three **affine lines**, not three points. Only the nonnegative real part of each line is the stated vertex.
3. The form direction aligns with the **simple** eigenvalue of W⁺(p), not with a repeated eigenspace.

The obstruction is not limited to "through this order." The conditions L₁,…,L₅ are necessary at every order, so the conclusion holds for all smooth germs in the ansatz. The restriction to diagonal metrics can very probably also be removed by an equivariance argument, given in §5.

## 1. The u = t² equations and the parameter count

**Einstein system.** I rederived it independently.

- Take g = dt² + Σ aᵢ²σᵢ² with dσᵢ = 2σⱼ∧σₖ. This normalization is forced by aᵢ′(0) = 1, because then dt² + t²Σσᵢ² is flat.
- The orthonormal Ricci component is
  Ric(eᵢ,eᵢ) = −aᵢ″/aᵢ − (aᵢ′/aᵢ)(aⱼ′/aⱼ + aₖ′/aₖ) + 2[aᵢ⁴ − (aⱼ² − aₖ²)²]/(aᵢ²aⱼ²aₖ²).
- Multiply by t² and use t²aᵢ″/aᵢ = tHᵢ′ − Hᵢ + Hᵢ² together with t d/dt = 2u d/du.
- This gives exactly 2uHᵢ′ − Hᵢ + HᵢΣH − 2[Zᵢ² − (Zⱼ − Zₖ)²] − 3u = 0 for λ = −3.
- The identities t²aᵢ²/(aⱼ²aₖ²) = Zᵢ² and t²(aⱼ² − aₖ²)²/(aᵢ²aⱼ²aₖ²) = (Zⱼ − Zₖ)² hold.

**Closure.** For Ω = Σxᵢ(aᵢ dt∧σᵢ + aⱼaₖ σⱼ∧σₖ):

- dΩ = 0 is equivalent to (xᵢaⱼaₖ)′ = 2xᵢaᵢ.
- This gives t xᵢ′ = xᵢ(2Zᵢ − Hⱼ − Hₖ), hence uXᵢ′ = MᵢXᵢ. ✓
- |ωᵢ|² = 2, so |Ω|² = 2 is equivalent to ΣXᵢ ≡ 1. ✓

**Generality of the form ansatz.** At the nut the isotropy SU(2) fixes exactly one half of Λ²T_p, namely the span of the ωᵢ. It acts on the other half by SO(3), which has no fixed vectors.

- A smooth invariant Ω of constant nonzero length therefore lies in span{ωᵢ} at p.
- Since Ω is self-dual for its own orientation, it lies in span{ωᵢ} everywhere.
- So Σxᵢωᵢ is the general invariant Ω.

**Order-one check.** The script never checks the order-u¹ equations. I did this by hand, with Aᵢ the cubic coefficients and S = ΣAᵢ:

- Einstein, order u: the coefficient is 6S − 3 for every i, independent of the individual Aᵢ. Hence S = 1/2 and two parameters are free. ✓
- Hamiltonian constraint, order u: 4S − 2S + 4S − 3 = 6S − 3. ✓
- Mᵢ = (6dᵢ − 1)u + O(u²), which matches `X_coeffs[1]`.

**Recurrence for k ≥ 2.** At order k the linearization in b_k is αI + βJ, with constant coefficients:

- α = 4(k+2)(k−1) on the trace-free part;
- α + 3β = (k+2)(4k+2) on the trace.

Consequences:

- At k = 1 the trace-free eigenvalue vanishes. This is the 2-parameter freedom (d₁, d₂), matching the trace-free W⁺(p) at the nut. W on the other half vanishes there by isotropy.
- For k ≥ 2 the operator is invertible with a d-independent determinant, so no special d is resonant.
- The formal germ is therefore unique for each (d₁, d₂). Briot–Bouquet theory gives convergence.

**Exact cross-check.** The closed form aᵢ = (sinh√2 t/√2, √2 sinh(t/√2), √2 sinh(t/√2)) reproduces the stored b₂ values 1/30 and 1/480.

## 2. The ideal and the Singular output

**Interior localization.** J = I + (1 − z·R₁R₂R₃·disc) has standard basis {1}. The factors (2d₁ + d₂) = d₁ − d₃ and (d₁ + 2d₂) = d₂ − d₃ correctly encode pairwise distinctness. This proves, over ℂ, that L₁ = … = L₅ = 0 has no solution with all Rᵢ ≠ 0 and dᵢ pairwise distinct. ✓

**Dimension.** `GI = std(I)` was computed in the ring (R₁, R₂, d₁, d₂, z), and I does not involve z. The reported dim = 2 is therefore 1 + dim in (R₁, R₂, d₁, d₂). The correct dimension is **1**.

**Components.** Reducing Singular's unreduced generators (for component [3], set d₂ = −1/12 and solve the other two generators, giving d₁ = 1/6 and R₁ = 1) yields three lines:

- ℓ₁: d = (1/6, −1/12, −1/12), R₁ = 1, R₂ + R₃ = 0 (Singular's [3]);
- ℓ₂: d = (−1/12, 1/6, −1/12), R₂ = 1, R₁ + R₃ = 0 ([1]);
- ℓ₃: d = (−1/12, −1/12, 1/6), R₃ = 1, R₁ + R₂ = 0 ([2]).

The mechanism behind the lines: on the Kähler point for axis 1, M₁ ≡ 0 and M₂ = M₃ ≢ 0. Then ΣX = R₁ + (R₂ + R₃)g(u) with g nonconstant, so only R₂ + R₃ = 0 is forced algebraically. Direct substitution confirms L₁ = 0 on ℓ₁. Rᵢ = xᵢ(0)² ≥ 0 then cuts each line to its vertex.

**The decomposition is stronger than the localization.** Every complex solution has d at a Kähler point. This also excludes triaxial metrics with one or two nonzero weights, so the discriminant localization is redundant. The "119 least-squares solutions" are consistent with sampling along these lines.

## 3. The surviving branch

- **Metric.** The closed form satisfies the Einstein equations. The recurrence is unique for k ≥ 2, so the germ with d = (1/6, −1/12, −1/12) *is* this metric to all orders, not only through u⁵. Its expansions f₁ = Σ(2u)ⁿ/(2n+1)! and f₂ = Σ(u/2)ⁿ/(2n+1)! match the listed coefficients. ✓
- **Identification.** Rescaling the CH² metric with Ric = −6 by 2 and setting t = √2 r gives exactly these aᵢ. So the branch is CH² with Ric = −3g and holomorphic sectional curvature −2.
- **Normalization.** The note's phrase "up to structure-constant normalization" can be dropped. The normalization dσᵢ = 2σⱼ∧σₖ is fixed by the nut condition.
- **Form.** (a₂a₃)′ = (2 sinh²(t/√2))′ = √2 sinh(√2 t) = 2a₁ holds exactly. So x₁ ≡ 1 is closed, and X₂ = X₃ ≡ 0 because Xᵢ = Rᵢ exp∫₀ᵘ Mᵢ/v dv.
- **q = 0.** This follows directly from Ω = ω₁ being the Kähler form, so ∇Ω ≡ 0. The output of `step63_nut_q.py` is consistent with this. That script uses the earlier q-formula without re-deriving it, and its series is accurate through u⁴.
- **Which eigenvalue.** The selected axis is the **simple** W⁺ eigenvalue s/6. The repeated pair −s/12 is orthogonal to Ω. The note's §4 phrase "repeated metric-curvature eigenspace" is inverted.

## 4. What is proved for all orders

L₁,…,L₅ are polynomial identities in the Taylor coefficients, and every smooth invariant germ satisfies them. Three facts make the result an all-order theorem rather than a truncation statement:

- Smooth nut metrics have aᵢ = t fᵢ(t²) with fᵢ smooth even functions.
- Einstein metrics are real-analytic.
- The recurrence uniquely determines the germ from d.

The note's phrase "no solution through this order" understates what has been proved.

## 5. Removing the diagonal restriction (derivation; one step still to be written out)

Take a general invariant nut metric dt² + h(t), with h = t²(I + uB + u²B₂ + …) and the σᵢ fixed.

- The order-k linearization depends only on h₀ = I.
- It is equivariant under Ad SO(3) = Aut(su(2)).
- On Sym²₀(ℝ³), which is irreducible of real type, it is therefore scalar by Schur. So it equals 4(k+2)(k−1), the value computed on the diagonal trace-free part, and is invertible for k ≥ 2.

The germ map B ↦ (B₂, B₃, …) is then unique and equivariant. Rotate B to diagonal form. The Klein group diag(±1, ±1, ±1) ∩ SO(3) fixes B, and its fixed set in Sym² is exactly the diagonal matrices. So every Bₖ is diagonal.

What remains is to write out the six spatial Ricci equations for non-diagonal class-A metrics and confirm two things: that the momentum constraints propagate, and that they impose nothing at order 1. If confirmed, the theorem covers every SU(2)-invariant metric with a nut.

The genuinely uncovered cases are germs without full SU(2) symmetry, and the unrestricted Step-62 jets.

## 6. Corrected wording

**Theorem 63.B.** Let (g, Ω) be a smooth SU(2)-invariant cohomogeneity-one germ at a nut. Here g = dt² + Σaᵢ²σᵢ² with dσᵢ = 2σⱼ∧σₖ, Ric = −3g, and Ω is closed, invariant, and of constant length |Ω|² = 2. (Diagonality is assumed; by §5 it is expected to be automatic.) Then, after a permutation of axes and Ω ↦ −Ω, g is the complex-hyperbolic metric with holomorphic sectional curvature −2 and Ω = ω₁ is its Kähler form. In particular ∇Ω ≡ 0, and no strict almost-Kähler germ with an isolated torsion zero arises at such a nut.

*Proof sketch.*
- The constant-length conditions L₁,…,L₅ cut {ΣRᵢ = 1} in the three lines ℓₖ (exact primary decomposition).
- Rᵢ ≥ 0 selects the vertex of each line.
- d at a Kähler point determines g uniquely, hence g = CH².
- Rⱼ = 0 forces Xⱼ ≡ 0, and x₁ ≡ 1 is closed.

The **ideal-theoretic fact** to state is that V(L₁,…,L₅) ∩ {ΣR = 1} = ℓ₁ ∪ ℓ₂ ∪ ℓ₃, which is one-dimensional. This replaces "dimension two" and "the primes are the points (1,0,0)."

**§4 interpretation.** Revise the sentence to say that the form aligns with the simple W⁺ eigenline.

## 7. Section 1 (brief consistency check only)

On C one has a = 0 and η = 0. With r = s/6, this gives R(Ω) = W⁺Ω + (s/12)Ω = (s/4)Ω. Hence c₁[C] = s·Area/(8π) and deg K⁻²|_C = s·Area/(4π), which agrees with the note.

The kernel of z ↦ Bz̄ is the J-line conj(ker B). ✓

I did not independently re-derive the sign convention by which γ_J represents 2πc₁.