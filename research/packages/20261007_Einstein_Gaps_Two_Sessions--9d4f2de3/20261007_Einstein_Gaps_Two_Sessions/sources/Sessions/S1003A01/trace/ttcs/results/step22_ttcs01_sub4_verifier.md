# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md",
    "Sessions/S1003A01/workspace/scripts/su2_offdiag_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian.py",
    "Sessions/S1003A02/workspace/scripts/o11_full_hessian2.py",
    "Sessions/S1003A02/workspace/notes/step9_universal_cell_response_and_spectral_pressure.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

Read the existing angular/SU(2) Hessian artifacts and formulate the smallest scientifically useful non-SU(2) construction probe on the current x0=.038, X=512 scalar-normalized/near-normalized cell. Check which claims from the SU(2) Galerkin Hessian are actually supported, how to construct globally smooth low SU(2)-isotype symmetric-2-tensor modes (rather than raw Euler trigonometric functions), and how to distinguish a geometric descent from a Lie-derivative or nonstationary-base artifact. Give explicit perturbation formulas or an executable finite-dimensional design if possible, while keeping numerical evidence distinct from a theorem.

## Output

# Non-SU(2) second variation of the x₀ = .038, X = 512 perpendicular cell: supported SU(2) results, smooth isotypic modes, and separating geometry from gauge

## Summary

- **SU(2) results.** The Z₂×Z₂ decoupling, the exact U(1) zero mode, and the sign of the twist stiffness rest on symmetry or first principles. The positive off-diagonal blocks are converged Rayleigh–Ritz upper bounds, not lower bounds.
- **Diagonal block.** The diagonal SU(2) block at this base is not among the reported data. "Strict local minimum among SU(2)-invariant metrics" therefore currently rests on the optimizer having converged within its ansatz.
- **Existing non-SU(2) prototypes.** They carry no geometric information. Their angular functions are not continuous on S³, their angular box excludes all half-integer isotypes, and their angular quadrature is not exact.
- **Proposed probe.** Use the j = ½ isotype first, then j = 1. Build modes from the blow-down chart of the bolt with a charge rule for the radial vanishing order. Use exact angular quadrature on S³ spherical designs, and an explicit gauge space that includes the CH transvections.
- **Separating artifacts.** All contamination by Lie derivatives and by a nonstationary base flows through one identity, H[k, ℒ_ξg] = −⟨∇J, ℒ_ξk⟩. This gives quantitative tests that distinguish a geometric descent from an artifact.

---

## 1. What the SU(2) artifacts establish

### 1a. Decoupling and vanishing first variation: exact

Right translation by the lifts of the π-rotations about the three axes normalizes U(1)₁. It therefore acts smoothly on the cell, fixes every diagonal h, and multiplies h₁₂, h₁₃, h₂₃ by three distinct nontrivial characters of Z₂×Z₂.

J₆ is diffeomorphism invariant. Hence the first variation in each off-diagonal channel vanishes, and the Hessian is block diagonal. The measured off-block entries of 10⁻¹³ confirm the implementation.

The reported "gradient ≤ 2×10⁻¹¹" is computed only in off-diagonal coefficients, where it is forced to zero by these characters. It says nothing about whether the base is stationary in diagonal directions. That stationarity matters for every j ≠ 0 block (§4).

### 1b. The SU(2) slice is complete in function content

- SU(2)-invariant symmetric tensors G dx² + 2N_i dx σ_i + h_ijσ_iσ_j have 10 radial functions.
- SU(2)-invariant vector fields f∂_x + f_iE_i have 4.
- ℒ_{f_iE_i} rotates h by f_i and creates the shift N ∝ f_i′h. The slice N = 0 therefore fixes f_i up to constants. Those constants are exactly the bolt-rotation moduli.

So the diagonal channels, the off-diagonal channels and the two bolt rotations exhaust SU(2)-invariant geometry, with x-reparametrization still to be quotiented in the diagonal block.

The diagonal block's Hessian on that quotient is not in the shown artifacts for this base. Recall that in Step 9 the A02 radial Hessian at 6 and 8 modes showed raw eigenvalues below zero tied to a large projected gradient. "Strict local minimum within SU(2)" therefore needs this one additional computed block.

### 1c. The u² envelope is the exact smoothness order

This follows from the charge rule of §3: Q = 3 for σ₁σ_{2,3} and Q = 4 for the σ₂σ₃ anisotropy, with u ∝ ρ² at the bolt. The off-diagonal Chebyshev spaces are therefore complete among smooth perturbations.

The plateau μ_min = 80.134 → 80.129 (n = 20 → 26), stable at nq = 2000, is strong evidence that the block infimum is near 80. It remains an upper bound; a lower bound needs an inclusion method (Temple or Lehmann–Goerisch) or a Riccati/Hardy certificate.

The norm ∫(k/N)²du is not geometric. The magnitudes 80/261/462 and the X = 128 values are therefore not comparable across blocks or across X. A common Gram ∫|k|²_g dV_g/(8π²) should be used whenever blocks are compared.

### 1d. Twist stiffness has the predicted sign and order

- The CH form has R⁺ eigenvalues (−6, 0, 0) in the normalization s = −24.
- The first-order cell law P/8π² = 1 − x₀R⁺(ζ,ζ) gives 6x₀cos²θ near θ = π/2 + ψ.
- A rotation in the (σ₁,σ₃) plane rotates Λ⁺ by the same angle.

The prediction is d²J/dψ² = 12x₀ = 0.456. The measured 0.6053 (and 0.6046 at X = 128) agrees in sign and order, with a 33% excess from O(x₀²) terms.

A scan at x₀ ∈ {.005, .01, .02, .038} should give S/x₀ → 12. That single computation tests both the rotation implementation and the angular part of the first-order law, which Step 9 verified only in the aligned case.

The rotation curve R(ψ(χ−1))hRᵀ has a diagonal second-order part. Its second derivative therefore contains ⟨∇J_diag, ∂²_ψ g⟩. As a statement along an admissible curve it is fine; reading it as a quadratic form requires diagonal stationarity.

### 1e. The (1,2) zero mode is exact

The collar has a₁ = a₂. Rotation about the CH fibre is a collar isometry, so the configuration is isometric to a global rotation. The slow Galerkin decay (3.2e−5 → 1.1e−6) reflects the basis approximating the compensating off-diagonal profile.

### 1f. The rejected linearized rotation illustrates a general admissibility rule

[Ψ,h]₁₂ = ψ(h₂₂ − h₁₁) ≈ ψx₀ at the bolt, while h₁₁ → 0. In an orthonormal frame the coefficient is ψx₀/√h₁₁ → ∞, so |k|_g is unbounded.

Rule: admissible linear directions need |k|_g ∈ L^∞ near the bolt, plus the vanishing orders of §3.

### 1g. What the inference "progress must break SU(2)" covers

It is a second-order statement at this base. It does not exclude SU(2)-invariant branches far from the diagonal one. It does not bear on the lower-bound (HJ) side.

## 2. Why the existing non-SU(2) prototypes carry no geometric information

- **Non-smooth modes.** `o11_full_hessian.py` uses coordinate components dψ, dθ, dφ with Euler trig functions; these degenerate on the Euler axis. `o11_full_hessian2.py` fixes the frame (coframe components) but keeps cos ψ and sin ψ, which are discontinuous on S³ along θ ∈ {0, π}. The H² energy of such modes concentrates on a set the autodiff sampling never sees, so the computed Hessian entries are not second variations of any metric family.
- **Missing half-integer isotypes.** The angular box ψ ∈ [0, 2π] covers SU(2)/{±1}. This is harmless for invariant integrands but omits all half-integer isotypes. The Burns cell's principal orbit is S³ (blow-up of a point in C²), and j = ½ is its lowest nontrivial isotype; it contains the bubble-translation directions.
- **Inexact quadrature.** nqa = 2 Gauss points per Euler angle do not integrate products of two j = 1 modes.
- **Weak regularity.** The bubble (u(1−u))² ~ ρ⁴ makes raw σ₁σ₁ components only C¹.
- **No gauge treatment, nonstationary base.** There is no gauge quotient, and the base was nonstationary.

Step 9 already reads these numbers as undecided. The analysis above identifies the causes.

## 3. Globally smooth low-isotype modes

### 3.1 Isotype reduction

The base is left-SU(2)-invariant, so by Schur the Hessian on left-isotype j acts as Id_{V_j} ⊗ H_W. Here W collects the right index, the 10 tensor components and the radial functions.

Fix the left row (left weight m₀ = j ≠ 0). For real modes Re(λv), λ ∈ {1, i}, the real quadratic form equals ½H_C. The reasons:

- Invariant complex-bilinear pairings couple left weight m only to −m.
- So B(v,v) = 0 when m₀ ≠ 0.
- Each eigenvalue therefore appears exactly twice.

**Built-in check:** the doubling must appear, and switching to the other left row must reproduce the spectrum.

### 3.2 Blow-down chart and charges

Notation:
- E₁ is the bolt generator (dual to σ₁).
- u_± are unit eigenvectors of E₁ in the 2×2 representation.
- ρ(x) = ∫_{x₀}^x dx/(2√G) is the geodesic distance to the bolt.

The normal exponential chart of the bolt is

  z = ρ(x) · g u₊ ∈ C².

It is smooth because the normal geodesics are the x-lines and the unit normals at a bolt point form the U(1)₁ orbit. With g⁻¹dg expressed in the coframe,

  dz_a = (gu₊)_a Θ + c ρ (gu₋)_a σ₊,  Θ = dρ + iκρσ₁.

This identity *defines* the signs of Θ and σ₊ and the constant κ. Here κ = lim √h₁₁/ρ, read off the base, and is ½ in the convention g⁻¹dg = (i/2)(σ₁τ_z + σ₂τ_x + σ₃τ_y). Compute dz by autodiff and decompose it in the coframe; this removes all convention risk.

Charges:
- right-weight functions: (gu_±)_a carry ±1;
- forms: Θ carries −1, Θ̄ carries +1, σ_± carry ±2.

These are fixed by requiring z_a ∝ ρ and dz_a to be smooth.

**Rule.** For F of right charge w_R and a monomial μ in {θ, θ̄, ϑ₊, ϑ₋}, set Q = w_R + w(μ). Then Re[c(ρ)Fμ] is smooth iff c = ρ^{|Q|} f(ρ²).

This is the polar fact for c(r)e^{iQφ}. One may use the base orthonormal frame θ = ê⁰ + iê¹ and ϑ_± = ê² ± iê³ in place of Θ and σ_±. The frame correction (Θ_g − Θ ∝ ρ²(Θ − Θ̄), and √h₂₂ − √h₃₃ = O(ρ⁴)) shifts Q by ±2 or ±4 while supplying ρ² or ρ⁴, which preserves the rule. Since u ∝ ρ²(1 + O(ρ²)), one may replace ρ by s := √u.

**Consistency with known orders (j = 0):**
- h₁₂, h₁₃ ∝ σ₁σ_± = (θ − θ̄)ϑ_±/(iρ) has Q ∈ {1, 3}, so the coefficient is ~ρ⁴ = u².
- h₂₃ and h₂₂ − h₃₃ have Q = 4, so ~u².
- θθ̄ has Q = 0, so a bolt value is allowed.

These match Step 21.

### 3.3 Mode families

- **j = ½:** F ∈ {(gu₊)₁, (gu₋)₁}, with w_R = ±1.
- **j = 1:** F ∈ {(gu₊)₁², (gu₊)₁(gu₋)₁, (gu₋)₁²}, with w_R = 2, 0, −2. These are symmetric in the left index, so the det = 1 piece is excluded.
- **Monomials μ:** θ², θθ̄, θ̄², θϑ_±, θ̄ϑ_±, ϑ₊², ϑ₊ϑ₋, ϑ₋² (10 complex).

The modes are

  k_{F,μ,m,λ} = Re[ λ s^{|Q|} T_m(2u−1)(1−u)³ F μ ].

The factor (1−u)³ gives C² contact with the exact CH collar, as in Step 21. Their sizes are 40 n_r real modes for j = ½ and 60 n_r for j = 1.

Examples:
- Re(λz₁)·(dρ² + κ²ρ²σ₁²) (j = ½, Q = 1) is a linear function times the normal metric.
- (gu₋)₁ϑ₊² has Q = 3, so it needs s³.

A uniform over-vanishing envelope such as u³ would be admissible, but the |Q| = 1 pieces would then be reachable only through logarithmic cutoffs; the H² capacity of the gradient at a point is logarithmic. The Galerkin spectrum would then appear converged while it is not. For j = ½ the exact orders are therefore essential, not cosmetic.

### 3.4 Exact angular quadrature

At fixed x the Hessian density is a quadratic form in the jets of k. Its coefficients are left-invariant, and E_i acting on degree-2j polynomials in g preserves degree. The density is therefore a polynomial of degree 4j on S³ ⊂ R⁴. Hence:

| Isotype | Integrand degree | Design | Points | Exactness |
|---|---|---|---|---|
| j = ½ | 2 | cross-polytope | 8 | 3-design |
| j = 1 | 4 | 24-cell | 24 | 5-design |
| check | – | 600-cell | 120 | 11-design |

Left-translate the design by a fixed generic unit quaternion a. This is a base isometry that moves points off the Euler singular set used by `curvature_scalars`. The weights are |S³|/N, calibrated so that k = 0 reproduces J₀ = 0.99517819.

Agreement between 24-cell and 600-cell to rounding is an internal proof of angular exactness.

Radially, use Gauss–Legendre in s = √u (du = 2s ds), because odd |Q| makes integrands smooth in s, not in u. Use n_s ≈ 400 and check 800.

## 4. Gauge and nonstationary base

### 4.1 Exact identities

Let φ_s be the flow of any ξ whose flow preserves the cell with its collar data. Two cases qualify: ξ compactly supported (vanishing for u ≥ 1), and ξ Killing on the exact CH collar. Then J(φ_s^*γ) = J(γ) for all γ. Differentiating gives

  H_g[k, ℒ_ξg] = −⟨∇J(g), ℒ_ξk⟩,  H_g[ℒ_ξg, ℒ_ξg] = −⟨∇J(g), ℒ_ξ²g⟩.

This is the functional form of Ozuch's reparametrization identity (Prop. 1.3, Ric⁽²⁾(h, ℒ_Xg) + Ric⁽¹⁾(ℒ_Xh) = ℒ_X Ric⁽¹⁾(h)).

∇J(g) is left-invariant (j = 0), while ℒ_ξk for ξ, k of isotype j contains a j = 0 part. Consequently, in every j-block, gauge null directions and their coupling to geometric modes are both O(‖∇J‖).

The Step 9 projected-gradient test cannot be reused here, because the projection of ∇J onto any j ≠ 0 block vanishes identically. The gauge block itself is the measure.

A quantitative scale for ‖∇J‖ in the conformal channel is the Yamabe gain 4.4×10⁻⁸ ≈ ½⟨∇J, H_c⁻¹∇J⟩. The note's ratio of 1.33 relative to the scalar energy shows that the residual is high-frequency, which is exactly what feeds gauge directions with oscillatory ξ.

Use the linear parametrization g + Σc_ak_a. Nonlinear parametrizations add ⟨∇J, ∂²g/∂c_a∂c_b⟩, whose j = 0 parts survive in every block.

### 4.2 Exact moduli to expect

- **j = 0:** the U(1) phase (§1e).
- **j = ½: the four CH transvections.** In the collar's ball chart w = tanh(r_CH(x))·g v (v the E₃-eigenvector; holomorphic curvature −4 gives |w| = tanh r), the transvections are V_b = 2Re[(b − ⟨w,b⟩w)∂_w], b ∈ C². Set ξ_b = (1 − φ(u))V_b with φ ≡ 1 near the bolt. Then ℒ_{ξ_b}g vanishes on the collar and is a compactly supported tensor. It is not in the span of compactly supported gauge, yet it is an exact zero of J: moving the bubble relative to a homogeneous bulk.
- **j = 1:** no exact moduli, since left su(2) acts isometrically.

This matches Ozuch's obstruction picture: translations are excluded only for Γ ≠ {1}. For a Burns bubble (Γ = {1}) the translation pairing is the position gradient of −a²R⁺(ζ,ζ), which vanishes on CH. The analogy is structural: Burns is scalar-flat Kähler, not Ricci-flat ALE.

### 4.3 Where a descent could live

P″[k,k] = 2∫|(Ric°)′k|² + (terms each containing a factor Ric° of the base). On the Einstein collar P″ ≥ 0.

The indefinite part is therefore weighted by Ric°, which is concentrated in the core and neck (u ≲ 0.35 here). Angular gradients enter the positive term at order j⁴ but the indefinite term only at order j². This is heuristic, but it ranks j = ½ and j = 1 first. In gauge-like directions the positive term is weak, which is why §4.1 matters.

J₆ rather than P is the right functional. By Theorem 2 it equals P after Yamabe normalization, and the conformal channel is positive by (1.3)/(1.4). Small perturbations keep s < 0, so Theorem 2's hypothesis holds. Using the ansatz base g instead of ĝ changes the Hessian by O(max|u−1|) ≈ 3×10⁻⁵ relative, and it avoids differentiating a grid solution twice.

### 4.4 Tests that separate a geometric descent from artifacts

| Test | What a geometric descent shows | What an artifact shows |
|---|---|---|
| (i) Gauge block: H on Z = span{ℒ_ξg} (compact ξ of the same isotype, built as in §3.3 with ν ∈ {θ, θ̄, ϑ_±}, 16 n_r real for j = ½) plus the 4 transvections | – | entries should be O(‖∇J‖) and decrease when the base is re-optimized |
| (ii) Quotient spectrum: eigenvalues of H on the G-orthogonal complement of Z in span(modes ∪ Z) | small overlap ‖P_Zv‖/‖v‖ before projection | eigenvector concentrated on Z |
| (iii) Base offset g_ε = g + εv₀ (v₀ a fixed SU(2)-diagonal bump), ε ∈ {0, ±1, ±2}×10⁻³ | λ_min smooth in ε, |λ| ≫ C·‖∇J‖ | eigenvalue linear in ε through ≈ 0 |
| (iv) Line test J(g + sk*) with ‖sk*‖_{L^∞(g)} ≤ 10⁻³ | follows ½λs²‖k*‖²; for j = ½ exactly even in s (odd orders integrate odd polynomials on S³) | departure from s² behaviour or from evenness |
| (v) Convergence | stable in n_r ∈ {4,6,8,10}, n_s, X ∈ {128, 512}, design order | drifts with resolution or X |
| (vi) Isotype checks | Re/Im doubling and row independence hold | doubling or row independence broken |

## 5. Minimal executable design

1. **Base and functional.** Use the X = 512 DualCell record from `su2_offdiag_hessian.py` and J₆/(8π²) with density r₀ + (s+24)²/4.
2. **Calibrations.**
   - Reproduce J₀.
   - Re-express the Step 21 k₁₂ basis in the new code and match the Hessian entries.
   - Recompute the j = 0 off-diagonal and diagonal blocks in the L²(g) Gram.
3. **Smooth frame.** Autodiff z = ρ·gu₊ to fix κ, Θ and σ₊.
4. **j = ½ block.**
   - 40 n_r real modes, 16 n_r compact gauge directions and 4 transvections.
   - Cross-polytope × n_s Gauss points (≈ 3200 points).
   - H via `jax.jacfwd(jax.grad(J))` as in the existing script: about 230 real parameters at n_r = 4 and 340 at n_r = 6.
5. **j = 1 block.** The same with 24 design points, 60 n_r modes and 24 n_r gauge directions.
6. **Report per j.**
   - lowest 5 quotient eigenvalues;
   - norm of the gauge block;
   - the number of near-zero quotient eigenvalues for j = ½, to be compared with the projection of the four ℒ_{ξ_b}g onto the reduced basis;
   - dλ/dε;
   - line-test data for any λ < 0.

## 6. How the outcomes relate to theorems

- **A quotient eigenvalue below zero passing §4.4.** This yields an explicit smooth metric g + sk* with J₆ < J₀. That single inequality can be certified, by bounding the quadrature error or by an Arb evaluation of the explicit finite-parameter metric. It then becomes a theorem-level upper-bound improvement breaking SU(2).
- **All quotient eigenvalues positive and converged.** These are Rayleigh–Ritz upper bounds in a basis complete near the bolt. They are numerical evidence of second-order stability in that isotype for this cell, not a proof. A proof needs isotype-wise lower bounds: a Lehmann–Goerisch inclusion from residuals, or a weighted Hardy/Riccati inequality per isotype extending the Step 9 matrix Riccati certificate. The j⁴-versus-j² structure of §4.3 is the natural route to large j.
- **Zero-mode count for j = ½.** Extra near-zero modes beyond the transvections would signal either unremoved gauge or a new modulus. Either one would change the picture of the perpendicular cell.