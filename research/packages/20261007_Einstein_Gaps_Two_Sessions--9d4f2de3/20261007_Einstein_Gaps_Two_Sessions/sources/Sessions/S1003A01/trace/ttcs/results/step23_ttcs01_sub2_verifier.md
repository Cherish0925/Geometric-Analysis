# TTCS Independent Branch Record

```json
{
  "step_id": 23,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/angular_isotype_conformal.py",
    "Sessions/S1003A01/workspace/data/angular_isotype/j1_tf_conformal_r2p10_q160.json",
    "Sessions/S1003A01/workspace/data/angular_isotype/j1_tf_conformal_r4p12_q160.json",
    "Sessions/S1003A01/workspace/data/angular_isotype/j1_tf_conformal_r6p16_q192.json",
    "Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md",
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md"
  ]
}
```

## Task

Read the scalar-relaxed j=1 angular construction result as a geometric analyst. Check whether the conformal Schur-complement experiment, pure-trace redundancy repair, finite-basis interpretation, two-sided line tests, and conclusions are mathematically and numerically consistent. Identify any substantive error in formulas or interpretation, especially whether positivity of the finite blocks says only what the note says and whether an actual scalar-normalized construction would require further work. Ground the answer in the actual script, canonical JSON outputs, and synthesis note; give concrete repairs or next decisive computation if needed.

## Output

# Verification memo: scalar-relaxed j=1 angular block (Step 23 §2, `angular_isotype_conformal.py`, three canonical JSONs)

## Summary

The conformal Schur-complement construction is mathematically correct. Its optimal-φ equation matches an exact second-variation identity, and the pure-trace repair is valid.

Three defects change what the numbers mean:

1. **The angular space is not a j=1 isotype.** It fixes the right (multiplicity) index of Ad(q) as well as the left one. It is a fixed one-third compression that the Hessian does not preserve.
2. **The note's scalar-relaxation conclusion compares eigenvalues from different symmetry sectors.** In the one sector where the conformal field actually couples, relaxation lowers the bottom by about two orders of magnitude, and the value is still falling.
3. **The line tests are not independent evidence.** They re-evaluate the same discretized functional whose AD Hessian was already computed.

Positivity of the finite blocks therefore says less than the note states. Details and repairs follow.

---

## 1. The Schur complement: correct, and what it actually computes

At a base with s ≡ −24 and compactly supported perturbations, the second variation can be computed directly. Use J₆ = P + ¼∫(s+24)², with P = 2∫|W|² + (1/12)∫s² − 16π²χ (no flux terms for compact support).

For φ with ĝ = e^{2φ}g, I used s_ĝ²dV_ĝ = (−6Δu/u + s)² dV with u = e^φ, and s_ĝ + 24 ≈ (−6Δ+48)φ. This gives, at second order (J ≈ J₀ + Q):

- **Conformal block:** Q_φφ = 12⟨φ, (−Δ+6)(−Δ+8)φ⟩.
- **Mixed block:** Q_hφ = 4⟨Ds[h], (−Δ+6)φ⟩. The P-part comes from P′(φ) = −∫sΔφ dV. Its h-derivative at s = −24 is −∫Ds[h]Δφ, because ∫Δ_gφ dV_g = 0 for every g.
- **Optimal φ:** minimizing over φ gives exactly (−6Δ+48)φ = −Ds[h], the equation in the docstring.

So the first-order variation k = h + 2φ_h g satisfies Ds[k] = 0. The relaxed form equals P″(k) on the tangent space of {s = −24}. Because P′ vanishes on conformal directions, the Lagrange multiplier is zero, so this is the correct second variation for the Step-22 reformulation. Explicitly:

  relaxed(h) = P″(h,h) − (1/12)⟨Ds h, (−Δ)(−Δ+8)⁻¹ Ds h⟩.

This is never larger than P″(h,h). It is the second-order form of "normalization lowers P".

Two structural facts follow.

- **The Schur step adds no new sign information.** With H_bb > 0, Schur > 0 is equivalent to the full (a,b) block being positive definite.
- **Finite b is a Ritz upper bound for the true relaxation.** By Step-22 uniqueness, the normalization of v²g equals that of g. Hence J₆(v²g) ≥ J₆(ĝ) for every v → 1, and adding φ-modes can only lower the relaxed values. Truncation in the metric modes is likewise an upper bound. A relaxed value below zero would therefore already be a genuine descent at second order. Positive values exclude nothing beyond the span.

**Pure-trace repair.** It is valid. With trace in both a and b, k = h + 2φg is nearly non-injective, and the Gram matrix counts only a, which produces the spurious near-zero branch. After removing trace, k = 0 forces h = 0 and φ = 0.

The script's comment that H_ab "comes entirely from the scalar residual" should read "entirely through Ds[h]". Both the (s+24)² term and P contribute, through Gauss–Bonnet.

**Cheap check not yet done.** The generalized eigenvalues of H_bb against a φ-Gram should be at least 2·12·(6+μ)(8+μ) ≥ 1152, where μ is the lowest Dirichlet eigenvalue of −Δ on F₀·radial, in the c^T H c = 2Q convention. The reported `conformal_hessian_min` of 2.5×10⁻⁴ is in raw coefficient units and says nothing. This check tests both the conformal block and the scalar normalization of the base.

## 2. The angular space fixes the multiplicity index (substantive error)

The docstring says F = √3 Ad(q)₀₀ is "one member of the multiplet (the other two copies are equivalent by left SU(2))".

- Under left translation, Ad(gq) = Ad(g)Ad(q) rotates the **first** index a. Fixing a = 0 is legitimate by Schur's lemma.
- The second index b is a multiplicity index. It is acted on by right translations, which are not isometries of the anisotropic base.
- Left-invariant frame derivatives generate right translations, so e_i Ad₀₀ ∈ span{Ad₀₁, Ad₀₂}.

So the j=1 left isotype of Sym²-valued functions is span{Ad₀ᵦ·H}, with 3 × 10 = 30 functions per radial function. The script uses the 10 with b = 0. The Hessian maps this 10-dimensional space out of itself, so the computation is a compression, not an isotypic block.

**Klein-sector decomposition.** The base is diagonal in the σ-frame (`L` uses `sqrt(diag(h))`), so the right Klein group of π-rotations is a symmetry. Write χ_b for the character of F_b = Ad₀ᵦ. The tensors carry characters χ(dxσ_b) = χ_b and χ(σ_cσ_d) = χ_b for {b,c,d} = {1,2,3}. Per radial function:

| sector | full j=1 content | script content | j=1 scalar | gauge ξ |
|---|---|---|---|---|
| trivial | F_b⊗{dxσ_b, σ_cσ_d}, b = 0,1,2 (6) | b = 0 only (2) | none | F_b e_b (3) |
| χ₁ | F₀⊗diag (4), F₁⊗{dxσ₃, σ₁σ₂}, F₂⊗{dxσ₂, σ₁σ₃} (8) | 3 diag differences (+ trace via φ) | F₀φ (present) | F₀∂ₓ, F₁e₃, F₂e₂ |
| χ₂ | 8 | F₀⊗{dxσ₃, σ₁σ₂} (2) | F₁φ (**absent**) | 3 |
| χ₃ | 8 | F₀⊗{dxσ₂, σ₁σ₃} (2) | F₂φ (**absent**) | 3 |

The JSON eigenvectors confirm this block structure. Off-pattern coefficients are 10⁻¹¹ to 10⁻¹². The r4/r6 minimizers occupy indices (0,1) and (2,3) of each radial block, which is the trivial sector. The r2 relaxed minimizer occupies the diagonal-difference slots, which is χ₁.

Consequences:

**(a) "Lowest mode already in the scalar kernel, conformal coefficients at numerical zero" is a symmetry identity, not a dynamical result.** No j=1 scalar has trivial Klein character, so Ds[h] ≡ 0 in the trivial sector.

**(b) The scalar relaxation is incomplete in χ₂ and χ₃.**
- Ds[F₀⊗dxσ₂] ∝ Ad₀₂ · (radial function), which is generically nonzero.
- Ds[F₀⊗dxσ₃] ∝ Ad₀₁ · (radial function), likewise.
- The script's φ ∝ F₀ cannot cancel either.

These modes sit in ker H_ab^T only because H_ab vanishes by symmetry. Their "relaxed = raw" values still contain the uncompensated ¼∫(Ds h)² penalty. The scalar ansatz for F₀ alone is complete for the b = 0 scalar, because Δ(Ad₀ᵦφ(x)) stays in the b-channel on a diagonal base. What is missing is Σ_b Ad₀ᵦ φ_b(x).

**(c) "Sampled scalar kernel" is not the scalar-preserving tangent space.** The kernel {H_ba a = 0, b = 0} is the set of trace-free h with Ds h ⊥ (−Δ+6)V_φ. When n_φ is at least the number of coupled metric modes, it is overconstrained: it has dimension 0 at r2 and r4, and 2 at r6, with values 96 and 173. Its dimension also depends on an SVD cutoff; the r6 singular values reach 1.3×10⁻⁷ against a tolerance of 2.6×10⁻⁸. The tangent space is correctly parametrized by h ↦ h + 2φ_h g, which is exactly the relaxed computation.

## 3. The numbers re-read by sector

Separating raw values that are unchanged by relaxation (these are exactly the scalar-kernel lists) from those that change gives:

| order (n_rad / n_φ) | scalar-decoupled bottom | χ₁ raw bottom | χ₁ relaxed bottom |
|---|---|---|---|
| 2 / 10 | 0.89575 | 14.849 | **0.74992** |
| 4 / 12 | 0.17823 | 13.026 | **0.28253** |
| 6 / 16 | 0.12095 | 12.849 | **0.14447** |

Corrections to the note:

- **The r2 lowering is 14.85 → 0.750, not 0.896 → 0.750.** The value 0.8957496 belongs to a decoupled sector and reappears unchanged as the second relaxed eigenvalue. The script's `scalar_lowering = eraw[0] − erel[0]` subtracts eigenvalues of different modes. Its values (0.146, ~10⁻¹⁵, ~10⁻¹⁴) are not a measure of scalar lowering.
- **Scalar relaxation is the strongest effect in the data.** In the coupled sector it reduces the bottom by a factor of about 90, and the relaxed value falls faster with refinement than the decoupled one. Ratios: 2.65 then 1.96 for χ₁, against 5.0 then 1.47 for the decoupled sector. At r6, 0.1445 is already close to 0.1209. The statement "integrating out scalar response does not destabilize" has no support. The data are consistent with the χ₁ relaxed bottom continuing toward or past the decoupled one.
- **Metric and conformal refinement are confounded.** n_rad and n_φ change together, so the table cannot separate the two convergences. Since the relaxed value is monotone in n_φ (§1), a run at fixed n_rad with n_φ = 10, 16, 24, 32 isolates the φ-convergence directly.

## 4. Gauge: the unquotiented isotype bottom is zero

The full j=1 isotype contains exact Lie-derivative directions. The cleanest is the radial twist ξ = f(x)R₀, with R₀ = Σ_b Ad₀ᵦ e_b the right-invariant (Killing) field:

  L_ξ g = 2f′(x) Σ_b Ad₀ᵦ h_b sym(dx⊗σ_b).

This lies in the trivial sector and uses all three values of b. Its second variation is −J′(g)[L_ξL_ξ g]. That is zero at a j=0-critical base, and exactly zero wherever ξ is supported in the exact-CH collar, since there E(g) = 0 and the Hessian density is |E′(k)|².

Implications:

- The true j=1 bottom (L²-normalized, no gauge quotient) is at most 0. A positive "spectral lower bound in this isotype" cannot exist without a slice. The note's wording ("not a proof of a positive spectral lower bound") is accurate but understates this.
- The current trivial-sector minimizer is dominated by the dxσ₁ coefficient (2.42, 2.91, 2.39 at r4; −3.95, −5.99, −5.13 at r6). That is the b = 0 projection of this twist.
- Falling positive Ritz values are expected even for a perfectly stable cell. They become informative only on a gauge slice, for example L²-orthogonal to {L_ξ g : ξ = Ad₀ᵦ(f_b∂ₓ + f_{bc}e_c)}, which is 12 radial functions with 3 per Klein sector.
- No exact gauge mode lies inside the script's span, because every j=1 gauge family needs two b-values. The current compression can therefore neither reproduce nor quotient them.

## 5. Line tests and quadrature

- **Line tests.** `oj` is the same quadrature functional as `hj`. The even quotients converge to cᵀHc by construction, so they check the AD Hessian and show that quartic terms are small at ε ≤ 10⁻³. The odd quotients (~10⁻⁹) vanish by left-SU(2) equivariance: J′(g) is invariant, so its pairing with j=1 is exactly zero whether or not the base is critical. "Both signs raise J₆" adds nothing beyond H > 0. The path also uses the first-order optimal b rather than the solution of the nonlinear scalar equation, so it does not test normalization.
- **Angular quadrature.** n_qa = 3 is exact for the Hessian. The integrand is a product of two row-0 j=1 functions; ψ and φ frequencies are at most 2, and after averaging the θ-part is a polynomial of degree at most 2 in cos θ. It is not exact at finite amplitude: F⁴ terms contain frequency 4, which aliases on 3 points. Any finite-ε nonlinear construction needs at least 2p+1 points for degree-p products.
- **Haar check.** The reported `haar_mean`/`haar_gram` use `ad_row0` in Hopf coordinates with η = ½arccos c, not the Euler-coordinate `ad00` actually used. Analytically, ⟨ad00²⟩ = ½·⅓·½ + ¼ = ⅓, so the √3 normalization is correct. The certificate, however, should be computed for √3·Ad₀ᵦ in the Euler quadrature.
- **Base gradient.** Base criticality in j=0 is not reported. It enters the curve-dependent second-order terms J′(g)[4φh + 2φ²g + …] and the Ward identity in §4. The quantity needed is the residual gradient in a richer j=0 basis than degree 28. The base itself, x₀ = 0.038, X = 512, is not Arb-certified (Step 23 §4).

## 6. What an actual scalar-normalized construction requires

Suppose a relaxed eigenvalue below zero appears in the complete gauge-sliced isotype. Then:

1. Step 22 applies to the perturbed exact-ended metric g + εh. Its normalization satisfies J₆ = P(ĝ_ε) ≤ J₆(e^{2εφ}(g+εh)) = J₀ + ½ε²λ_rel‖h‖² + O(ε³). The first-order term vanishes exactly.
2. The comparison is meaningful only if the j=0 residual gradient is small compared with |λ_rel|ε². Otherwise the descent is a j=0 improvement in disguise.
3. Transfer requires a rigorous enclosure at finite ε. That needs nonlinear evaluation with adequate angular quadrature, plus either a local Taylor/Chebyshev representation of the profile for Arb or a certified bound on the Yamabe solve.

Positive finite blocks yield none of this. They show only the absence of second-order descent in a 9-dimensional angular compression, with partial scalar compensation in one Klein sector.

## 7. The decisive computation

- **Basis.** Use the full row: metric k = Σ_b Ad₀ᵦ Σ_A H_A k_{bA}(x) with all 10 H, including trace, and conformal φ = Σ_b Ad₀ᵦ φ_b(x). Block by Klein sector (dimensions 6, 8, 8, 8 per radial function).
- **Ward identity.** Compute the 12 gauge modes. Hess(L_ξ g, ·) ≈ 0 measures base criticality and discretization error.
- **Gauge-sliced relaxed spectrum.** Solve the generalized eigenproblem on the gauge-orthogonal complement. Do this per sector, with metric and conformal refinements separated and a localized radial basis in physical r (B-splines) replacing envelope × Chebyshev (Gram condition number is already 1.5×10⁶ at r6).
- **Independent continuum check.** For the lowest χ₁ relaxed h, solve the radial ODE (−6Δ+48)φ = −Ds[h] directly and compare P″(h + 2φ_h g) with the Schur value.

The sector to watch is χ₁ and its χ₂/χ₃ analogues once their scalars are added. That is where the data already show a large and unconverged scalar-driven decrease.