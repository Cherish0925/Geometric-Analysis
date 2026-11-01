# Step 57 — The kernel-direction second-order Burns coefficient in an arbitrary background

Agent2, Execute. Status: **formal coefficient computed and cross-checked (Step 57); D = 6 fit, density-independence
check and eight independent product-background tests completed in Step 58 (§6), all agreeing with 57.Φ to 10⁻¹⁴;
independently reproduced for KE backgrounds by A01 (#830). Rigorous remainder (two-scale factorization in a
nonhomogeneous background) not yet written.**

Scripts: `workspace/scripts/step57_kernel_log_coefficient.py` (core: jet-based |Ric°|² density, Burns tail, S³ quadrature,
K bases), `step57_run_CH.py` (CH tests), `step57_general_form.py` (20×20 curvature form; args D nu_pts nphi [ell]),
`step57_fit_invariants.py` (U(2)_ζ-invariant fit), `step57_norm_check.py`, `step57_checks.py`.
Data: `workspace/data/step57_general_form_D2.json` (q6×16, includes the ℓ(C) and N(R) computation),
`step57_general_form_D2_q8_24.json`, `..._D2_q10_32.json`, `..._D4_q8_24.json`, `..._D4_q10_32.json` and `*_invfit.json`.

## 1. The formal problem

Near p write the background as g0 = δ + νB + ν²C (+ odd degree-3 part), the Burns metric exactly as δ + εA with
A = ∂∂̄ log|z|² for the constant complex structure J_ζ (normalised so ∂∂̄|z|² = δ; then g_B is exactly Burns, linear in ε,
ε = Area(E)/π, and its Kähler form ζ ∈ Λ⁺ with the complex orientation), and a free degree-0 correction εν K. With the
two-parameter homogeneity r^{-4}(ε/r²)^a (μr)^m of the density, the only scale-invariant (log) terms at second order are
a = 2, m = 4. Hence

P(g̃)/8π² = P(g0)/8π² + 1 − ε R⁺_p(ζ,ζ) + (Φ/2) ε² log(1/ε) + O(ε²)   (formal),

Φ = (8π²)^{-1} ∫_{S³} [ε²ν² coefficient of |Ric°|² dμ at r = 1], minimised over K. Φ is the sum of
c_AABB(B,B) + c_AAC(C) + c_ABK(B,K) + c_KK(K); c_KK = |Ric°_lin(K)|² is background independent (its restriction to the
SU(2)_-‑invariant diagonal squash reproduces 16|d|² − 5(Σd)² of supplement Ch. 5).

**Lemma 57.1 (no ∇Rm, no ∇²Rm).** (i) ∇Rm cannot enter (odd parity under −1 ∈ U(1)_ζ; ∇Rm² is m = 6).
(ii) The C-linear term is ∂_c of the ε² part of F(δ+εA+cC) = ⟨∇P(δ+εA),C⟩ + div V. The Burns family is P-critical for all
ε, so the term is a divergence of a homogeneous degree −3 field and has zero log coefficient. Numerically ‖ℓ‖ = 5·10⁻¹⁵ on
all 350 quartic jets. Hence **Φ depends only on Rm_p**, and no P-criticality of g0 is needed for the log coefficient.

## 2. Checks

- Burns δ+εA is scalar flat (|s| ~ 10⁻¹⁵) and not Ricci flat; CH in potential −log(1−|x|²) has Ric = −6g exactly.
- CH perpendicular (J_CH = J2 ⊥ J_ζ in Λ⁺): Φ = −18.000000000000 with the 10-dim SU(2)_- invariant K, with general
  polynomial K of degree D = 2 (100 fields) and D = 4 (350). The Ch. 5 constant-mode minimiser is therefore optimal among
  all degree-0 corrections. Optimal invariant K: dr²: −2, σ1²: 1/2, σ2²: 5/2, σ3²: −1 (gauge-equivalent to c_*).
- CH parallel (ζ = ω_CH): Φ = −18 as well (first order nonzero there).
- Gauge independence: CH evaluated with normal-coordinate B instead of Bergman coordinates gives −18 again.
- Quadrature converged (q6×16, q8×24, q10×32 identical to 10⁻¹⁴).

## 3. Result: the invariant form

U(2)_ζ = U(1)_+ × SU(2)_- decomposition: s, w = W⁺(ζ,ζ), W⁺_{ζ⊥} (charge 2), W⁺_⊥⊥ = trace-free part of W⁺ on ζ^⊥
(charge 4), W⁻ (spin 2), Ric°_ζ (J_ζ-Hermitian part, spin 1), Ric°_⊥ (J_ζ-anti-Hermitian). Norms: operator Frobenius on Λ²
(session convention, |W⁺|² = s²/24 for Kähler); Ric° block B with |Ric°|²_tensor = 4|B|²_op.

Fits (relative residual ≤ 6·10⁻¹⁵):

| coefficient of | K = 0 | D = 2 | D = 4 (q8×24 and q10×32) |
|---|---|---|---|
| s² | 1/144 | 1/288 | 1/288 |
| s w | −5/24 | −1/24 | −1/24 |
| w² | 2 | −1 | −1 |
| |W⁺_⊥⊥|² | −5/9 | −1 | −1 |
| |W⁻|² | 7/30 | 7/80 | **0** |
| |B_ζ|² | 5/27 | 2/15 | **0** |
| |B_⊥|² | 10/27 | 4/45 | **0** |
| |W⁺_{ζ⊥}|² | 14/9 | (leak) | (leak) |

The W⁺_{ζ⊥} direction has a b-component in ker Q (the constant-K frame rotation): when ζ is not an R⁺-eigenvector the
first-order term can be lowered by rotating the frame, so this entry is not a log coefficient; at a first-order-stationary
frame W⁺_{ζ⊥} = 0.

**Theorem 57.Φ (formal kernel coefficient).** Let ζ be an eigenvector of R⁺_p = W⁺_p + s_p/12 with eigenvalue μ1, other
eigenvalues μ2, μ3. Then
Φ = −(w + s/12)(w − s/24) − |W⁺_⊥⊥|² = −μ1(μ1 − μ2 − μ3)/2 − (μ2 − μ3)²/2.
In the kernel direction μ1 = 0:
**Φ = −(μ2 − μ3)²/2 ≤ 0**, independent of W⁻, Ric°, ∇Rm, ∇²Rm.

[Superseded by §7 item 1: the argument below is invalid as stated; the chiral-square argument replaces it.]
Why W⁻ and Ric° drop out (independent argument): for every metric P(g̃) − P(g) − 8π² = Δ(4∫|W⁺|² + ∫s²/12) (Chern–Weil).
If W⁺_p = 0, s_p = 0 the right side is ≥ 0 up to O(ε²) for any local ASD scalar-flat representative of the jet, so the
W⁻/Ric° coefficients are ≥ 0; D = 4 attains 0. Consistency: scalar-flat Kähler blow-ups have exactly topological cost.
Kähler parallel case: Φ = −s²/32, while cscK blow-ups have analytic P in the class parameter. Both are consistent,
because the −s²/32 saving uses non-Kähler K.

CH: μ = (0, s/4, 0), s = −24, Φ = −18. ✓

## 4. Consequences (formal; rigorous version needs §5)

1. **Every Kähler–Einstein background saves.** R⁺ = diag(s/4, 0, 0). The kernel circle ζ ⊥ ω gives Φ = −s²/32 < 0 at
   **every** point, whatever W⁻ is. So p_*(X#kCP̄²) < 8π²k for every compact KE surface (K ample), using k disjoint cells.
   For canonical models with ADE points, add Kronheimer resolutions at zero cost. This is the category-wide strict
   inequality on all minimal general-type surfaces asked for in Problem 2. The scale-invariant saving per cell is
   (s²/64) ε² log(1/ε), i.e. λ²ε²log(1/ε)/4 for Ric = λg. The earlier D = 2 estimate, which suggested a W⁻ penalty and a
   c₁²/c₂ > 21/37 condition, is withdrawn.
2. **Minimizer rigidity (with Theorem 53.B, conditional on the Anderson ledger).** A P-critical bulk carrying a
   Burns-type bubble must satisfy, at every point: R⁺ ≤ 0, and if λ_max(R⁺) = 0 then the other two eigenvalues are equal.
   In particular no bulk point can be Kähler–Einstein-like (eigenvalues (s/4, 0, 0) with s ≠ 0). This strengthens Cor. 53.C
   ("no exact CH region") to all KE and Kähler-type degenerate R⁺. It is not an exclusion of Burns bubbling: R⁺ < 0
   everywhere (λ_max(W⁺) < |s|/12) is untouched, because there the first order already costs.
3. Strategist #72's hypothesis "negative on the whole cone R⁺ ≤ 0" is answered: second order is relevant only on the
   boundary of the cone, where it is ≤ 0 and vanishes exactly at μ2 = μ3. The interior is decided at first order (cost
   −εμ1 > 0). W⁻ enters neither linearly (SU(2)_- invariance) nor quadratically.

## 5. Remaining work on this line

- D = 6 run (`s57_t21_tool2`, `step57_general_form_D6_q8_24.json`): confirm s², sw, w², W⁺_⊥⊥ unchanged. The W⁻/Ric° zeros
  are protected below by §3.
- Code check prepared but not yet run: `density_Fplus_from_jet` (4|W⁺|² + s²/12) must give identical M, b, Meff (it
  differs from |Ric°|² by a local divergence).
- Rigorous theorem: extend the Ch. 5 two-scale factorization (z = ε/t², t, ω on S³) to an analytic background with
  angular dependence. a = 1 terms are divergences or average to zero, a = 2, m < 4 terms are matched to the core, and the
  first-order inner flux is exactly −εR⁺(ζ,ζ). This requires an explicit K (extract the D = 4 minimiser) and the claim
  O_R(ε²) uniformly. Theorem F's O(ε^{6/5}) is not adequate. Coordinate with A01, whose Ch. 5 machinery is the template.
- Batch gluing and moving backgrounds, for Problem 2's matching law on balanced families.

## 6. Step 58 completion of the computation

**(a) D = 6 invariant fit** (`step57_general_form_D6_q8_24_invfit` printed by `step57_fit_invariants.py`): s² 1/288,
sw −1/24, w² −1, |W⁺_⊥⊥|² −1, W⁻ 0 (7·10⁻¹⁷), Ric°_ζ 0 (10⁻¹⁵), Ric°_⊥ 0 (3·10⁻¹⁶), residual 5·10⁻¹⁵.
Identical to D = 4. The W⁺_{ζ⊥} entry moves with D (−0.185, −0.081, −0.353 at D = 2, 4, 6), confirming that it is a
kernel-leak (frame-rotation) artefact and not a coefficient.

**(b) Density independence.** With `STEP57_DENSITY=fplus` the driver integrates (4|W⁺|² + s²/12)dμ instead of
|Ric°|²dμ (`step57_general_form_D{2,4}_q8_24_fplus.json`). Raw M agrees to 5.6·10⁻¹⁶, M_eff to 1.7·10⁻¹⁴ (D = 2) and
7.9·10⁻¹⁵ (D = 4), the leak to 10⁻¹⁵, Φ_CH = −18 in both. This is the numerical form of the fact that the two densities
differ by Chern–Weil densities, whose ε²ν² parts are divergences of degree −3 homogeneous fields (zero flux
difference between spheres), so they carry no log coefficient. It also checks the session's operator-norm
convention for W⁺ against the tensor computation of Ric°.

**(c) Independent product backgrounds** (`workspace/scripts/step58_product_tests.py`, batch
`step58_product_batch.sh`, data `workspace/data/step58_products/`). Background Σ₁(K₁)×Σ₂(K₂) in *conformal*
coordinates (not normal coordinates), with nonzero quartic jet C, Ric° ≠ 0 when K₁ ≠ K₂, W⁻ ≠ 0. Products are
Kähler with R⁺ = diag(s/4,0,0), s = 2(K₁+K₂); 'par' puts ζ on the product Kähler form (μ₁ = s/4), 'perp' puts ζ in the
kernel (μ = (0, s/4, 0)). Prediction −s²/32 in both layouts.

| layout | (K₁,K₂) | D = 4 | D = 6 | prediction |
|---|---|---|---|---|
| par | (−1,−1) KE | −0.3781 | −0.5000000000000 | −1/2 |
| par | (−1,−3) | −1.5124 | −2.0000000000000 | −2 |
| par | (−1,1) scalar-flat | 0 | 0 | 0 |
| perp | (−1,−1) KE | −0.4314 | −0.5000000000000 | −1/2 |
| perp | (−1,−3) | −1.7257 | −2.0000000000000 | −2 |
| perp | (−1,1) scalar-flat | 0 | 0 | 0 |
| perp | (−2,1/2) | −0.2427 | −0.2812500000000 | −9/32 |
| perp | (1,2) positive | −0.9707 | −1.1250000000000 | −9/8 |

All D = 6 errors ≤ 3·10⁻¹⁵, kernel leak ≤ 10⁻¹⁵. Lessons: (i) Ric° (up to |K₁−K₂| = 2.5 here) and W⁻ are
genuinely invisible, now with a background that is not in the normal-coordinate gauge of the fit; (ii) the
scalar-flat Kähler product H²×S², which has large Ric°, gives exactly 0, the predicted topological cost;
(iii) **convergence in corrector space depends on the gauge of the background jet**: in normal coordinates D = 4
already converged, in conformal coordinates D = 6 is needed (the D = 4 values lie above the truth, as a
minimization over a smaller space must). The verifier question 'do degree-0 correctors exhaust the log coefficient'
is therefore also a question about this gauge freedom; see the Step-58 TTCS record.

**(d) Independent reproduction by A01 (#830, `Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md`).**
A01 reduces F to the CGB form 4|W⁺|² + s²/12, shows W⁻ enters only through a completed square with the explicit
corrector k₀^W = (3/2)sym(h_W k_B) − (1/4)tr(h_W k_B)δ, h_W = −(1/3)W⁻_{ikjl}x^kx^l, k_B = σ₁²+σ₂² (exact sympy), and
obtains F_KE = −18 at s = −24 on every negative KE surface in the kernel orientation; in Ric = −g units
P/8π² = 1 − (1/4)x²log(1/x). Our Φ = −s²/32 gives (Φ/2) = −s²/64, which is −9 at s = −24 and −1/4 at s = −4. Agreement in both normalizations.
A01's statement that the Ric° coefficients are "nonnegative minimized squares" is consistent with our finding that
their minimized value is exactly 0.

**(e) Two readings.**
1. *Unification with Theorem H.* Real-hyperbolic bulks have R⁺ = (s/12)I < 0 strictly, so every Burns cell pays
   −εμ₁ = ε|s|/12 > 0 at first order: the cost 8π²k is approached from above, which is exactly Theorem H's
   regime (conditional on its Yamabe hypothesis). KE and CH bulks have a kernel circle with anisotropic ζ^⊥, so
   they save at second order, so 8π²k is strictly beaten (p_* < 8π²k); the insertion family itself is then not
   minimizing and says nothing about attainment of p_*. The two known regimes are the
   interior and the boundary of the cone R⁺ ≤ 0. That 'Burns bubbling is not excluded where R⁺ < 0' is the correct
   description of the hyperbolic phenomenon, not a gap.
2. *Strict pointwise Weyl bound at minimizers carrying Burns bubbles* (conditional on 53.B and the ledger, and on
   57.Φ becoming rigorous). R⁺ ≤ 0 with tr R⁺ = s/4 < 0 means the eigenvalues of W⁺ are ≤ c = |s|/12; the maximum of
   |W⁺|² on {λ_i ≤ c, Σλ_i = 0} is attained only at (c, c, −2c), i.e. KE type, value s²/24. 57.Φ excludes exactly
   that type (double top eigenvalue ⇒ kernel anisotropic). Hence |W⁺|² < s²/24 **at every point**, and the allowed
   boundary type is W⁺ = (|s|/12)(1, −1/2, −1/2), |W⁺|² = s²/96. Integrated: C₊(V) < ∫s²/(32π²). This is strict but
   not quantitative; it does not contradict LeBrun's direction and gives no global estimate by itself. (If s = 0,
   R⁺ ≤ 0 forces W⁺ = 0 and the strict inequality is false; the statement is for s < 0.)

## 7. Step-58 verification (`trace/ttcs/results/step58_ttcs01_verifier1_integration.md`) and exhaustive minimization

**Confirmed.** The invariant algebra (fit ⇔ eigenvalue form), the normalization (Φ/2)ε²log(1/ε) (log annulus from
r ~ √ε, so ∫dr/r = ½ log(1/ε)), CH = −18 ⇒ −9ε²log, all product predictions, Lemma 57.1's mechanism, the strict
bound |W⁺|² < s²/24 (proof: t_i = c − w_i ≥ 0, Σt_i = 3c, |W⁺|² = Σt_i² − 3c² ≤ 6c², equality only at (c,c,−2c)),
and the KE/hyperbolic table. Real-hyperbolic points have Φ = s²/288 > 0, irrelevant behind the first-order cost.

**Repairs adopted.**
1. *W⁻/Ric° nonnegativity.* The pointwise Chern–Weil argument of §3 was invalid (vanishing of W⁺, s at p does not
   make F₊(g̃) − F₊(g) ≥ 0). Replacement (chiral square): with 𝒞(g) = (2W⁺, s/√12), F₊ = ∫|𝒞|². Burns has 𝒞 ≡ 0, and
   D𝒞_δ[B] = 0 for B in the W⁻ ⊕ Ric° sector, so 𝒞(g_{ε,ν}) = εν(𝒜_B + D𝒞_δ[K]) + … and the ε²ν² coefficient of the
   F₊ density is |𝒜_B + D𝒞_δ[K]|² ≥ 0. Zero is attained iff D𝒞_δ[K] = −𝒜_B is solvable; A01's explicit k₀^W solves
   it for W⁻ exactly; for Ric° the solvability is supported numerically (D = 4, 6 zeros) but no closed-form corrector
   is yet written. U(2)_ζ-equivariance removes cross terms between sectors.
2. *Lemma 57.1 wording.* The ε²C part of the first-variation field is homogeneous of degree −3, its radial flux is
   r-independent, so its divergence has zero spherical average (no log). Simpler: W⁺ = s = 0 on Burns, so the first
   variation of the F₊ density vanishes pointwise. ∇²Rm and the curvature-quadratic part of the quartic jet may still
   enter the regular O(ε²) term.
3. *Scope of the coefficient.* Φ is the coefficient of the matched ansatz (Burns core + degree-0 corrector). If
   E_P(g)(p) ≠ 0, singular tails ε²χr⁻⁴T on ε^α < r < R pair linearly with E_P at order ε²log(1/ε); that is a
   lowering of the background, not a bubble effect. At P-critical bulks (KE; minimizer bulks) this freedom has no
   linear contribution. Higher-homogeneity terms such as εRm²H₂ can sit in the same corner; they vanish by Burns
   criticality, not by power counting.
4. *Gauge and D.* D is angular polynomial complexity of degree-0 tensors. A cubic coordinate change X₃ shifts
   K ↦ K + ℒ_{X₃}A (degree 0, higher angular complexity), which explains why conformal-coordinate products need
   D = 6 while normal coordinates converge at D = 4.
5. *KE scope.* Ricci-flat KE (s = 0) has Φ = 0. For minimal general-type surfaces with (−2)-curves, use the KE
   canonical orbifold, Burns cells at regular points, Kronheimer resolutions at ADE points with scales chosen after
   the Burns scales. Strictness then needs only the KE-cell remainder o(ε²log) and zero-energy resolution gluing.
6. *Open boundary case.* At R⁺ = (0, s/8, s/8) both displayed terms vanish; the next object is the regular O(ε²)
   coefficient.

**Exhaustive minimization in the (s, W⁺) sector (new, `workspace/scripts/step58_invariant_exhaustive.py` →
`workspace/data/step58_invariant_exhaustive.json`).** For curvature with only s and W⁺, the normal-coordinate jet and
the Burns tail are SU(2)_−-invariant; averaging K over SU(2)_− keeps b(K) and does not increase Q(K) (convexity), and
SU(2)_− acts simply transitively on S³, so the 10-dimensional invariant space Sym²⟨dr, σ₁, σ₂, σ₃⟩ contains the
minimizer over **all** degree-0 correctors. Result (q8×24, residual 2.4·10⁻¹⁵): s² 1/288, sw −1/24, w² −1,
|W⁺_⊥⊥|² −1, CH = −18.0000000000003; the W⁺_{ζ⊥} directions leak into ker Q (1.414), the frame-rotation null
direction. So in the (s, W⁺) sector 57.Φ is the exact optimum over all angular modes, not a truncation artefact.
Together with item 1, the formal coefficient is now established in every sector except for a closed-form Ric°
corrector.
