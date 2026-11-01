# TTCS Independent Branch Record

```json
{
  "step_id": 61,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step59_chiral_completion_and_zero_charge.md",
    "Sessions/S1003A01/workspace/notes/step56_soldered_instanton_and_SU2_AKE.md",
    "Sessions/S1003A02/workspace/notes/step75_Q4_half_twistor_torsion_and_zero_index.md",
    "Sessions/S1003A02/workspace/notes/step76_Q4_chern_weil_density_and_prolongation.md"
  ]
}
```

## Task

Independently check A02's new zero-index algebra and its relevance to the closed negative Goldberg problem. Starting with the exact soldered equation and a nondegenerate torsion zero f(z)=c z+B bar(z), B=S+A with S complex symmetric and A complex antisymmetric, verify the real Jacobian determinant formula det_R Df=|c|^4-|c|^2(||S||^2-||A||^2)+|det B|^2 under the stated norm conventions. Derive the sharp implications for negative versus positive local index, test the examples f=z, f=A bar(z), and f=(z1+2 bar z1,z2), and explain which pure modes are scientifically decisive for the first nonlinear prolongation. Also assess whether any pointwise Weyl localization or Chern–Weil density currently constrains these indices. Ground the reading in the A01/A02 notes; do not infer existence of a full Einstein germ from principal-symbol algebra.

## Output

# Memo: the zero-index algebra of the soldered torsion equation and its bearing on the closed Goldberg problem for Einstein constant λ < 0

## 1. The linear model is the full first-order kernel

At a torsion zero with nondegenerate linear part, A01's homogeneous solution of the principal soldered system (Step 59 §3), at m = 1, is

f_i = z_i h_0 + g_i^{(1)}(z̄),

so f(z) = cz + B z̄, with c ∈ ℂ and B ∈ M₂(ℂ) arbitrary.

This has 1 + 4 = 5 complex parameters. That matches dim_ℂ K = 5 in A02's Theorem 75.H(d).

The Darboux count in Step 76 §2 is consistent with this:
- The linear torsion has 16 real parameters.
- The primitive (1,1) part 𝒫α ≅ Ric″ removes 6 of them.
- 10 real parameters remain, which is K.

So for an Einstein structure, the linear torsion at a zero lies exactly in {cz + B z̄}. At the zero the quadratic |a|² term in the W₃⁺ identification vanishes (q(p) = 0). The identifications are therefore pointwise and linear:
- c ∝ η(p), the W₂⁺ component, through d_b*α = 2η;
- the antisymmetric part A of B corresponds to W₃⁺(p);
- the symmetric part S of B is not seen by any curvature component (Step 59; Step 75 (c)).

**Orientation.** The index is sign det_ℝ Df, with the J-orientation on both source and target (Step 76 §2). Both orientations agree with the Ω² orientation. Conjugating the fibre structure (the AAD Λ^{1,0} versus A01 Λ^{0,1} conventions) composes with a map of real determinant +1 on ℂ². The index is therefore convention-independent, and it sums to ⟨e(E),[M]⟩ = ⟨c₂(E),[M]⟩ = 5χ + 6τ.

## 2. Verification of the determinant formula

View L(z) = cz + B z̄ as an ℝ-linear map of ℂ². In the basis (z, z̄) its complexified matrix is

M = [[cI, B], [B̄, c̄I]].

det_ℝ L = det_ℂ M, because the change of basis to real coordinates is a fixed conjugation.

For c ≠ 0, the Schur complement gives

det M = c² · det(c̄I − c⁻¹B̄B) = det(|c|²I − B̄B).

This extends to c = 0 by continuity, where it equals det(B̄B) = |det B|². For a 2×2 matrix,

det(xI − N) = x² − (tr N)x + det N, with N = B̄B and det N = |det B|².

The trace term splits as follows. With B = S + A, B_ji = S_ij − A_ij, so

tr(B̄B) = Σ_ij B̄_ij B_ji = Σ(S̄_ij + Ā_ij)(S_ij − A_ij) = ‖S‖² − ‖A‖² + Σ(Ā_ij S_ij − S̄_ij A_ij).

The cross sums vanish because they contract a symmetric array against an antisymmetric one. Hence, with Frobenius norms ‖X‖² = Σ|X_ij|²,

**det_ℝ Df = |c|⁴ − |c|²(‖S‖² − ‖A‖²) + |det B|².**

This confirms (75.5).

Explicitly, write A = [[0, a], [−a, 0]] and S = (s_ij). Then:
- ‖A‖² = 2|a|²;
- det B = det S + a², so |det B|² = |det S + a²|².

D is invariant under the phase rotation (c, B) ↦ e^{iθ}(c, B). It is also invariant under unitary changes acting by B ↦ UBUᵀ or B ↦ ŪBU⁻¹, since each replaces B̄B by a similar matrix.

## 3. Sharp sign characterization

Put x = |c|², t = ‖S‖² − ‖A‖² and d = |det B|². Then D = x² − tx + d.

**Index −1 holds if and only if both of the following hold:**
- t > 2|det B| (strict inequality);
- |c|² lies in the open interval (x₋, x₊), where x_± = ½(t ± √(t² − 4d)).

Equivalently, using the theorem that real eigenvalues of B̄B that are less than zero occur with even multiplicity, the following holds. D < 0 if and only if B̄B has two distinct nonnegative eigenvalues μ₂ < μ₁ (squared coneigenvalues of B) with μ₂ < |c|² < μ₁. If instead B̄B has a complex-conjugate pair, or a repeated eigenvalue below zero, then D = |x − λ|² > 0.

**Clean special case A = 0.** Takagi factorization S = UΣUᵀ gives S̄S = Ū Σ² Ū⁻¹, so

D = (|c|² − σ₁²)(|c|² − σ₂²).

The index is −1 exactly when |c| lies strictly between the two Takagi values of S.

**Comparison with A02's Proposition 75.I.**
- The three listed sufficient conditions for index +1 are correct:
  - c = 0 gives D = |det B|²;
  - S = 0 gives D = (|c|² + |a|²)²;
  - ‖S‖ ≤ ‖A‖ gives t ≤ 0.
- The necessary condition for −1 must read t > 2|det B|, with strict inequality. At t = 2√d one has D = (x − t/2)² ≥ 0.
- The necessary conditions are not sufficient without the window on |c|². In particular c ≠ 0 is forced, and the zero is degenerate when |c|² = x_±.
- The phrase "positive-index zeros are the generic case of the kernel" has no content as stated. Both the index +1 set and the index −1 set are open and nonempty in K. The c = 0 slice is a positive-codimension subset, not a generic one.

## 4. Examples

| Model | Parameters | D | Index |
|---|---|---|---|
| f = z | c = 1, B = 0 | 1 | +1 |
| f = A z̄ | c = 0 | \|a\|⁴ | +1 if a ≠ 0 (complex-linear map composed with conjugation of ℂ², both of real determinant ≥ 0) |
| f = (z₁ + 2z̄₁, z₂) | c = 1, S = diag(2, 0), A = 0; t = 4, d = 0, window (0, 4) ∋ 1 | 1 − 4 = −3 | −1 |
| f = S z̄ (pure S-mode) | c = 0 | \|det S\|² | +1 if det S ≠ 0 |

Direct check of the third row: f₁ = 3x₁ − iy₁ has real Jacobian −3, and f₂ = z₂ has Jacobian 1. Product −3. ✓

**All three pure modes (c, A, S) carry index +1.** Index −1 lives only in the mixed c–S region.

## 5. Does pointwise Weyl data constrain the index? No, except at η(p) = 0

Fix any η(p) ≠ 0 (so c ≠ 0) and any W₃⁺(p) (so any a). Choose S = diag(R, −a²/R). Then:
- det B = det S + a² = 0;
- t = R² + |a|⁴/R² − 2|a|² = (R − |a|²/R)².

For R large, |c|² lies in the window (0, t), so the index is −1. Choosing S = 0 instead gives +1.

Hence the pointwise W⁺(p) data (Ω-eigenvalue s/6 at a zero, η(p), W₃⁺(p)) fixes the index only when η(p) = 0, where it forces +1. W⁻ does not enter the first-order system at all, and neither does the sign of λ.

The free S is exactly Step 56 §4's undetermined Sym₀∇²Ω component. A Weyl localization of the index needs an equation tying S to curvature or to its derivatives. Such an equation can only come from prolongation.

## 6. Chern–Weil densities

Neither density currently constrains the local index.

**Levi-Civita density.** 15 + (9/2)|W⁺|² + ½|W⁻|² > 0 pointwise.

**Canonical density (76.3).** 42 − (27/8)q + (9/4)|η|² + ½|W⁻|².
- At a torsion zero q = 0, so it equals 42 + (9/4)|η(p)|² + ½|W⁻|² > 0, irrespective of ind_p.
- On A01's complete pair it ranges over [6, 42]/(4π²).

Both are smooth representatives. They yield only the global number 5χ + 6τ, never a decomposition into local degrees. A strictly positive density is compatible with any mixture of ±1 zeros summing to 5χ + 6τ. Step 75 §3(ii) adds that norm-weighted singular weights see only |det Df|, not its sign.

An index-localizing representative must be built from the section itself. Examples are the Mathai–Quillen form of tT as t → ∞, or a connection induced through the opposite structure I off Z. Its local contribution at p is sign D(c, A, S), and that depends on S.

## 7. Which modes are decisive for the first nonlinear prolongation

Step 76 §2 places the first nonlinear compatibilities at order 2. They take the form ⟨ℓ, Q(H₂) − λH₂⟩ = 0, quadratic in the 2-jet H₂, which contains the linear torsion. The same order is the first at which λ appears.

**Consequences.**

**(i) Pure modes are not enough.** Restricted to K (after eliminating the curvature part of H₂), the conditions are quadratic forms in (c, A, S) and may have cross terms c·S, c·A and A·S. Testing the pure c- and A-modes alone cannot exclude mixed jets. Moreover, the index −1 region lies entirely in the c–S cross sector.

**(ii) The S-mode belongs on the list.** A02 proposes the c-mode and the A-mode. The pure S-mode (det S ≠ 0) is index +1 and has η(p) = W₃⁺(p) = 0, a Kähler-type W⁺(p), with a nondegenerate zero. It is the mode least constrained by curvature, and so the hardest case for a nonexistence argument. Any local theorem "no strict germ with a torsion zero" (Step 75 route 2) must exclude it.

**(iii) The decisive computation.** It is the variety cut out by the order-2 compatibility on K × (remaining 2-jet), projected to K. The informative outcomes are:
- empty, or contained in {D = 0}: this excludes nondegenerate zeros;
- containing only index +1 jets: this is a local sign theorem;
- nonempty in both index regions: topology and second-order algebra do not close the problem.

**(iv) Built-in control with λ = 0.** Step 56 reproduced strict Ricci-flat almost-Kähler metrics of Gibbons–Hawking type. If any such metric has a torsion zero, then exclusion for λ < 0 must use the λH₂ term explicitly. Exact torsion-zero data in these λ = 0 metrics would therefore calibrate the order-2 computation.

## 8. What remains unresolved

None of the above produces an Einstein germ. The cz + B z̄ models solve only the frozen principal system, and the index algebra is identical for every λ.

Three questions stay open:
- whether any (c, A, S) survives the order-2 quadratic conditions with H₂ completed by Einstein curvature;
- whether S becomes determined by curvature at that order;
- whether a zero-localized index density (Mathai–Quillen form, or the I-connection) admits a sign once such relations are known.

The order-2 output referenced in Step 76 §3 (`step76_prolong_order2.json`) is not yet reported in the notes. That output is the object on which these questions turn.