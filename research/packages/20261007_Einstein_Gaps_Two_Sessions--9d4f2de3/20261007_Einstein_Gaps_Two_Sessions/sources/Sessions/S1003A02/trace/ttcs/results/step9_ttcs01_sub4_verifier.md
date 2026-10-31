# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/scripts/o11_general_bulk_cell.py",
    "Sessions/S1003A02/workspace/scripts/o11_radial_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian2.py",
    "Sessions/S1003A02/workspace/data/o11perp/radial_hessian_x0.03_n6b.json",
    "Sessions/S1003A02/workspace/data/o11perp/radial_hessian_x0.03_n8.json",
    "Sessions/S1003A02/workspace/data/o11perp/perp_smooth_hi_x0.03.json",
    "Sessions/S1003A02/workspace/notes/step8_first_order_cell_law_ASD_Qprinciple.md"
  ]
}
```

## Task

Read the attached O11 computation artifacts as a geometric analyst and assess what is scientifically established by the new Fubini–Study versus complex-hyperbolic sign experiment and by the attempted Hessian tests. Check normalizations and the inference that P/(8π²)=1-x0 R^+(ζ,ζ)+O(x0²): in the code the complex-space-form collar is K=x+kappa x² with s=-24kappa and aligned R^+(ω,ω)=-6kappa. Determine whether P<1 for kappa=-1 is a genuine same-metric cell result, whether the finite outer radius or interpolation can mimic the sign, and what asymptotic extrapolation is justified by x0=.001,.003. Then evaluate the second-variation design: full radial symmetric-h Hessian and non-invariant coordinate/coframe Hessians, their quadrature consistency, base stationarity, diffeomorphism modes, and why negative numerical eigenvalues accompanied by two-sided energy rise are not yet negative directions. Recommend one mathematically decisive executable next check that stays focused on the spectral problem modulo diffeomorphisms.

## Output

# Memo: O11 sign experiment (Fubini–Study vs complex hyperbolic) and the Hessian tests

## Summary

- **The aligned (θ=0) first-order law is a theorem, not only a fit.** For Kähler cells it follows from relative Chern–Weil plus Cauchy–Schwarz. This explains the slope 6κ, forces the sign flip under κ→−κ, and puts every finite-X and interpolation effect at order x₀² or higher.
- **P<1 for κ=−1 is predicted analytically** by an explicit Kähler cell. No κ=−1 output file was attached, so the numerical value itself is unverified here.
- **The κ=−1 run cannot test the general R⁺(ζ,ζ) law.** On complex space forms, s and W⁺ change sign together.
- **The radial Hessian's sub-zero eigenvalues are not established descent directions.** They are confounded by four things:
  - the base metric is not critical in the enlarged space;
  - the exponential parametrization of G;
  - the radial diffeomorphism orbit;
  - non-convergence as the basis is refined.

  The sampled energy curves are too coarse to resolve the quadratic regime.
- **Both non-invariant Hessian scripts have quadrature or smoothness defects** that are larger than the effect being measured.

## 1. Normalizations

In `g = dx²/(4K) + x(σ₁²+σ₂²) + Kσ₃²`:

- **Coordinates and frame.** K=x is flat with x=r². The σᵢ are the halved left-invariant forms (unit S³ ↔ σ₁²+σ₂²+σ₃²), and the volume form is π² x dx for every Kähler profile.
- **Bolt smoothness.** The rows of `kahler_K_signed` impose K(x₀)=0 and K′(x₀)=1. This is exactly smoothness of an O(−1) bolt with ψ-period 4π. Burns is K=x−x₀.
- **Meaning of x₀.** x₀ = Area(E)/π, so x₀R⁺ is a natural dimensionless pairing.
- **Background forms.** K=x−x² is Fubini–Study with Ric=6g (s=24). K=x+x² is complex hyperbolic with s=−24.
- **Scalar curvature.** For U(2)-invariant Kähler profiles, s = −4((xK)″−2)/x. This is the Hwang–Singer form, with constants fixed by the flat and space-form cases. Hence s_bulk = −24κ.
- **Interpolant.** It is Calabi-extremal with s = −24α − 12c₁x. It matches the bulk only C¹ at X, so s jumps there. This is harmless because transgression terms involve K and K′ only.
- **Self-dual curvature.** R⁺ = W⁺ + s/12 = diag(s/4,0,0) in (ω, ω₂, ω₃). So R⁺(ω,ω) = −6κ, W⁺(ζ,ζ) = (s/12)(3cos²θ−1), and R⁺(ζ,ζ) = −6κcos²θ.
- **Agreement with the Step-8 table.** The table's 4ΔW₊/x₀ ≈ 2(3cos²θ−1) and ΔS/(12x₀) ≈ 2 are exactly −W⁺(ζ,ζ) and −s/12 at κ=1.

## 2. The aligned law is a theorem in the Kähler sector

### Exact identities

Take a Kähler cell agreeing with the bulk (C¹) near x=X, with E-area πx₀. Then:

- **Relative P.** From P = ∫s²/4 − 2∫ρ∧ρ and Δc₁² = −1:
  P_cell = 8π² + (S_cell − S_ball)/4.
- **Total scalar curvature.** ∫s dV = π²∫s x dx = −4π²[(xK)′ − 2x] evaluated between x₀ and X. This equals π²(−12κX² − 4x₀), versus −12κπ²X² for the ball. This is the cohomological shift 4π·Δ(c₁·[ω]) = −4π²x₀.
- **Volume.** V = π²(X² − x₀²)/2.

### Lower bound and its expansion

Cauchy–Schwarz S ≥ (∫s)²/V gives, for every such Kähler cell:

  **P/8π² ≥ 1 + (3κX² + x₀)²/(X² − x₀²) − 9X² = 1 + 6κx₀ + (9 + X⁻²)x₀² + O(x₀³).**

The argument uses only Stokes and the class constraint, so it extends to non-U(2) Kähler cells with the same collar.

The extremal interpolant has s − s_bulk = O(x₀/X²) on a region of volume ~X⁴. So it realizes the bound up to O(x₀²).

### Consequences

1. **The sign flip under κ→−κ is forced.** The first-order term is −8π²x₀·s̄/4, so its sign is the sign of −s. Neither the outer radius nor the C¹ interpolation can produce an O(x₀) effect. They enter at x₀²/X² (Kähler sector) and through a log(X/x₀) in the relaxation term (point 2).

2. **The optimized aligned CH cells are non-Kähler.** Compare the Step-8 aligned slopes with the exact Kähler bound slope at X=1:

   | x₀ | 0.03 | 0.01 | 0.003 | 0.001 | 3e-4 | 1e-4 |
   |---|---|---|---|---|---|---|
   | Kähler bound slope | 6.306 | 6.101 | 6.030 | 6.010 | 6.003 | 6.001 |
   | numerical slope | 5.619 | 5.779 | 5.900 | 5.956 | 5.984 | 5.994 |
   | gain/(x₀ log(1/x₀)) | 6.5 | 7.0 | 7.5 | 7.8 | 7.8 | 7.6 |

   The relaxation below the Kähler bound is about 7.7·x₀² log(1/x₀). The log presumably comes from the annulus x₀ ≪ x ≪ X, where the Burns tail O(x₀/x) meets the background curvature. Its coefficient should be computable from an ODE on that annulus. The first-order coefficient 6 is untouched.

3. **What the κ experiment does and does not test.** On complex space forms, W⁺ = diag(s/6, −s/12, −s/12) is slaved to s. So flipping κ flips both response channels together, and the aligned κ=−1 run cannot separate the W⁺ coefficient from the s/12 coefficient.

   Its value is threefold:
   - it checks that the code handles the signed bulk;
   - it shows the 8π² per-blow-up threshold needs R⁺ ≤ 0;
   - it identifies the cell inequality's structure as P ≥ 8π²(1 − x₀R⁺(ζ,ζ)) + O(x₀²).

   Separating the two coefficients needs a background with W⁺ and s independent. For example, the round S⁴ or H⁴ ball has R⁺ = (s/12)I, predicting P = 1 − x₀s/12 independent of θ.

4. **The first-order law for θ≠0 is still numerical.** For general θ the cells are non-Kähler and no identity applies. A full lower bound over all metrics at order x₀ is also not proved; only the Kähler-sector bound above is.

## 3. Is "P<1 at κ=−1" a same-metric cell result?

### What the code computes

`o11_general_bulk_cell.py` integrates |Ric°|² of a single optimized metric over [x₀,X]. Outside X the metric is Fubini–Study, which is Einstein and contributes zero. No reference ball is subtracted, and `Cell.report` (with its hard-coded CH scalar/Weyl ball) is avoided.

Gluing the cell into CP² (requires X<1) gives an explicit metric on CP²#CP²bar with ∫|Ric°|² = 8π²P. P<1 there contradicts nothing, since CP²#CP²bar carries the Einstein Page metric.

### Unverified points

- **No κ=−1 output was supplied.** The numbers, min_K, and grad_inf cannot be checked from this material.
- **Possible hidden CH dependence.** The docstring says `Cell` hard-codes CH data in `report`. Whether `fields` and the profile parametrization use the passed K everywhere is not visible.

The sharp test is the z=0 value. With no profile variation, the code's P must equal the closed form

  1 + (1/32)[∫_{x₀}^{X} (24α + 12c₁x)² x dx − 288κ²X²],

with α and c₁ from the 4×4 solve. If the code agrees with this to quadrature accuracy, the signed bulk is implemented correctly. After optimization, P only decreases, so P<1 holds whenever the z=0 value is already below 1. The Kähler bound guarantees that z=0 value is below 1 for small x₀ at fixed X<1.

For κ=−1, X should stay well inside (0,1), for example ≤ 0.5. As X→1, K = x − x² degenerates at the line at infinity.

## 4. Extrapolation from x₀ = 0.001, 0.003

- **Model of the corrections.** The κ=1 sequence shows the slope's leading correction is x₀ log(1/x₀)-type, not x₀.
- **Two-point estimate of the first-order coefficient.** A linear fit in x₀ through the two points recovers it to about 0.2%. With slope = 6 − 7.7x₀ log(1/x₀), the two-point linear extrapolation gives about 5.99. The subleading form cannot be determined from two points.
- **Cleaner use of paired runs.** Compare P(κ=+1) and P(κ=−1) at the same x₀ and the same X:
  - Kähler odd part: 6κx₀X²/(X² − x₀²).
  - Relaxation from first-order forcing: quadratic in the forcing, hence even in κ.
  - So [P(+) − P(−)]/(2x₀) = 6 + O(x₀²), with the x₀² log term cancelled. This is a sharp test of the coefficient.
  - [P(+) + P(−)]/2 − 1 isolates the even second-order law. Two x₀ values exactly determine b and c in b·x₀² + c·x₀² log(X/x₀), but leave nothing to check the model.

This pairing requires equal X in both runs. At X=1, the κ=−1 interpolant is not admissible.

## 5. Second-variation tests

### Radial symmetric-h Hessian (`o11_radial_hessian.py`)

**Quadrature.** Consistent: P at nq=400 matches the cell value at nq=500 to 3.7×10⁻¹⁰. The Gram matrix is correct: dG/G weight 1, tr(h⁻¹δh h⁻¹δh) for h, volume π²√(det h/G).

**The sign is real but its meaning is not.** By Sylvester's law of inertia, the count of sub-zero eigenvalues (1 at n6, 2 at n8) belongs to the raw discrete H. It does not depend on the L²-Gram choice. What it means is the open question, and four confounders stand in the way.

1. **The base is not critical.**
   - The base `perp_smooth_hi_x0.03` stopped with L-BFGS `ABNORMAL` inside the PerpCell family (2 profile functions, no rotation modes: len(z)=30=2·10+10).
   - The radial sector modulo gauge has more physical functions. Its Gram-dual gradient norm is 5.2 at n6 and 12.6 at n8. It grows with the basis, so this is a real first-order descent.
   - The gradient is automatically orthogonal to gauge directions, because dP(L_ξg)=0.
   - Hence the θ=π/2 value P−1 = 0.0186 ≈ 20.7x₀² is an upper bound that can still be lowered within SU(2)-invariant metrics. The O11 second-order coefficient is therefore not yet determined.

2. **The parametrization contaminates the Hessian.** G is varied as G·eᵈ. At a non-critical point the Hessian picks up the term ⟨∂P/∂log G, d_a d_b⟩, which is proportional to the gradient. The lowest modes are G-dominated: n6 coefficients reach ~2×10³ and n8 coefficients ~1.2×10⁴, with alternating Chebyshev signs.

3. **Diffeomorphisms.**
   - Radial ξ(x)∂ₓ acts by d = ξG′/G − 2ξ′ and δh = ξh′.
   - Differentiating P(φₜ*g) = P(g) twice gives H(L_ξg, L_ξg) = −dP(L_ξL_ξ g). This vanishes only when dP=0.
   - At this base, near-gauge directions can therefore take either sign, with size ~‖grad‖. That is the same order as the eigenvalues observed.
   - An oscillatory ξ (large ξ′, small ξ) produces exactly the observed pattern: large d components, small δh.
   - The off-diagonal blocks of the modes vanish (~10⁻¹²) by the reflection symmetry of the diagonal base. So these modes live in the diagonal (G, h₁₁, h₂₂, h₃₃) sector, where radial gauge is the only gauge.

4. **No convergence.** λ_min goes from −1.63 (n6) to −23.2 (n8), and a second sub-zero eigenvalue appears at n8. A genuine instability would stabilize under refinement; this behaves like a mode living at the finest resolvable scale.

### Why the energy rises on both sides

Split P(tv) − P₀ into even and odd parts in t (v is Gram-unit).

**n6:**
- Even part: 5.3×10⁻⁵, 1.14×10⁻³, 2.2×10⁻² at t = 0.005, 0.01, 0.02. This fits λt²/2 + c₄t⁴ with λ = −1.63 and c₄ ≈ 1.2×10⁵.
- Odd part gives a linear coefficient ≈ −0.003.

**n8:**
- Even part: c₄ ≈ 1.7×10⁶ with λ = −23.2.
- Odd part gives a linear coefficient ≈ +0.09.

**Interpretation:**
- In both cases the quadratic regime is |t| ≲ (|λ|/2c₄)^{1/2} ≈ 2.6×10⁻³. That is below the smallest sampled step of 0.005.
- The quartic dominates because a Gram-unit vector has enormous raw amplitude where the volume weight is small, near the bolt. So t = 0.005 is already a large metric change.
- The fitted model predicts a real decrease of order 10⁻⁵ (n6) to 10⁻⁴ (n8) at |t| ~ 10⁻³. This is dominated by the linear term, i.e. by non-stationarity.
- The two-sided rise therefore neither confirms nor refutes a second-order descent. A descent along v at a non-critical base is first-order anyway, not evidence of instability.

### Coordinate-basis Hessian (`o11_full_hessian.py`)

- **Singular modes.** Constant Euler-coordinate tensor components violate regularity at θ=0,π. In the continuum they have infinite curvature energy. The 3-point quadrature avoids the poles and hides this.
- **Quadrature in ψ and φ.** Gauss–Legendre on [0,2π] is not exact for trigonometric polynomials. With 3 points, ∫cos²ψ comes out as 1.53π instead of π.
- **Docstring mismatch.** The docstring describes a DeTurck penalty that the code never adds.

### Coframe Hessian (`o11_full_hessian2.py`)

- **Volume quadrature.** With nqa=2, Gauss–Legendre in θ of the sinθ density gives 1.936 instead of 2. So P_quad ≈ 0.968·P_cell. The 3% error exceeds the whole excess P−1 = 0.019, contradicting the docstring's statement that the quadrature reproduces the cell P.
- **Smoothness of angular modes.** cos ψ and sin ψ are not smooth on S³: cos ψ = Re(z₁z₂)/|z₁z₂| is singular on the Hopf circles. sinθ·cosψ is the smooth version.
- **The 'constant' angular set is not non-invariant.** It is the SU(2)-invariant sector plus dx–σ shifts. The shifts are gauge, generated by x-dependent right translations.
- **Basis size.** nr=1 is too small to resolve anything.

### Non-invariant sectors at a critical base

By symmetric criticality, dP vanishes on non-invariant modes once the invariant base is critical. Before that, gauge directions in every isotypic sector are contaminated via dP(L_ξ²g), because the square of a representation contains the trivial one.

The appropriate design at a critical base is:
- left-equivariant Wigner-D modes times coframe tensors;
- block diagonalization by spin j;
- exact angular integrals (trapezoid in ψ, φ with enough points, or analytic).

## 6. The decisive spectral computation

**Setup: the full SU(2)-invariant, shift-free radial sector in a radial-gauge slice.**
- Keep all six h_ij(x).
- Fix d to a single length mode d = λd̂. This slice is exactly transversal, for two reasons:
  - The equation ξG′/G − 2ξ′ = 0 forces ξ ∝ √G, which has no compact support.
  - Any d can be moved into the slice except for its proper-length moment ∫d/√G dx.
- After shifts are removed, no other invariant gauge remains.

**Steps.**
1. Reach a true critical point with a trust-region Newton method (about 50–100 degrees of freedom; exact jax Hessian). Require a Gram-dual gradient ≤ 10⁻⁸, starting from the x₀=0.03 perpendicular cell.
2. Compute the slice Hessian's lowest eigenvalues. Check convergence at N = 8, 10, 12, 16 and nq = 400, 800.
3. Validate the code in the unsliced basis. The identity H(L_ξg, L_ξg) + dP(L_ξ²g) = 0 must hold. At the critical point the representable L_ξg must become near-null.
4. Sample P along any persisting lowest mode at log-spaced t from 10⁻⁶ to 10⁻², fitted by parity.

**What each outcome means.**
- The sign of the slice Hessian at a critical point is independent of the slice choice and of the Gram (inertia).
- A converged sub-zero eigenvalue would therefore be a genuine SU(2)-invariant descent direction modulo diffeomorphisms.
- A converged positive spectrum would give strict local minimality in that sector.
- The critical value itself sharpens the θ=π/2 second-order coefficient (currently ≤ 20.7 at x₀=0.03). That number is what decides whether a sub-threshold cell P<1 exists within SU(2) symmetry.