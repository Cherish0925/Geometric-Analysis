# TTCS Independent Branch Record

```json
{
  "step_id": 98,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step98_full_matrix_joint_transition.py",
    "Sessions/S0910A03/workspace/scripts/step98_direct_spd_transition.py",
    "Sessions/S0910A03/workspace/data/step98_direct_spd_N16_interior.json",
    "Sessions/S0910A03/workspace/data/step98_center_residual_resolution.json",
    "Sessions/S0910A03/workspace/data/step98_full_matrix_joint_transition_resolution64.json",
    "Sessions/S0910A03/workspace/scripts/step96_koiso_einstein_cauchy_evolution.py",
    "Sessions/S0910A03/workspace/scripts/step94_charged_koiso_separator.py",
    "Sessions/S0910A03/workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md"
  ]
}
```

## Task

Independently verify the mathematical and computational substance of Step 98's full-matrix charged-Koiso matching experiment. Focus on: (i) the Gaussian formulas for all blocks of E=Ric+3g, especially E_nn, E_ni=div K-dH, and E_ij; (ii) whether q=q0^{1/2} exp(X) q0^{1/2} with X_n(0)=±2A and X_nn(0)=2(Rhat+3I) really reproduces q_n=±2K0 and the sign-independent exact Einstein q_nn jet, including noncommutative exponential terms; (iii) invariant norm computation by Cholesky conjugation; (iv) what the low-resolution direct nodal residual decrease actually establishes and what aliasing, endpoint, regularization, underresolution, or overfitting artifacts remain; and (v) propose the most decisive convergence/cross-resolution experiment and residual-projection calculation. Read the actual scripts and JSON evidence. Return corrections with explicit equations, not generic process advice.

## Output

## Verification memo — Step 98 full-matrix charged-Koiso matching

I read `step98_full_matrix_joint_transition.py`, `step98_direct_spd_transition.py`, `step96_koiso_einstein_cauchy_evolution.py`, `step94_charged_koiso_separator.py`, the step96 note, and the four JSON files. Below are the results, with the one modeling point that most changes how the residual numbers should be read.

---

### (i) The three blocks of E = Ric_g + 3g are correct, and the hyperbolic cross-check confirms them

Write g = dn² + q_{ij}(n,s)dy^idy^j, K = ½∂_nq, W = q⁻¹K, H = tr W. The generic radial (non-Einstein) identities are

- **Tangential:** Ric^{(g)}_{ij} = Ric(q)_{ij} − ∂_nK_{ij} − HK_{ij} + 2(Kq⁻¹K)_{ij}, hence
  E_ij = Ric(q) + 3q − K_n − HK + 2Kq⁻¹K.  ← matches `ET`.
- **Normal:** Ric^{(g)}_{nn} = −∂_nH − |W|². Using ∂_nH = tr(q⁻¹K_n) − 2 tr(W²) (from ∂_n q⁻¹ = −2q⁻¹Kq⁻¹) gives
  E_nn = 3 + tr(W²) − tr(q⁻¹K_n).  ← matches `Enn = 3 − tr(q⁻¹Kn) + W2`.
- **Mixed/Codazzi:** E_ni = (div_q K − dH)_i = q^{jk}∇_jK_{ki} − ∂_iH.  ← matches `mom`, with the s-index (j=0) the only differentiating direction and the corrected momentum index order carried over from step96.

The exact check q = e^{2n}I (which is Einstein Ric=−3g) gives K=q, W=I, H=3, Ric(q)=0, K_n=2q, so E_ij = 3q−2q−3q+2q = 0, E_nn = 3−6+3 = 0. The `known_metric` block returns 2.5×10⁻¹¹ at nr=35, confirming both the algebra and that Chebyshev normal differentiation of a smooth exponential is accurate at this nr. The 3-metric `christoffel_and_ricci` uses the standard R_{ij} = ∂_kΓ^k_{ij} − ∂_jΓ^k_{ik} + Γ^k_{ij}Γ^ℓ_{kℓ} − Γ^ℓ_{ik}Γ^k_{jℓ} with only ∂_s active; the curved-slice case is validated indirectly (see (iv), center table). All block formulas are sound.

### (ii) The matrix-exponential jets reproduce q₀, ±2K₀, and the sign-independent Einstein q_nn exactly

Let S = q₀^{1/2}, A = S⁻¹K₀S⁻¹, so SAS = K₀ and S(3I)S = 3q₀. With X(0)=0 and X = Bn + ½Cn² + O(n³) (B = ±2A, C = 2(R̂+3I)):

- q(0) = S·I·S = q₀.  ✓
- Using ∂_n e^X|₀ = X_n(0) (the Duhamel integral ∫e^{sX}X_ne^{(1−s)X} collapses to X_n at X=0), q_n(0) = S(±2A)S = ±2K₀.  ✓
- Expand e^X = I + X + ½X² + …; to O(n²) the only quadratic pieces are ½C and ½B² (the cross term BC is O(n³)), so ∂²_n e^X|₀ = C + B². Then
  q_nn(0) = S(C + B²)S = 2Ric(q₀) + 6q₀ + 4K₀q₀⁻¹K₀ = 2(Ric(q₀) + 3q₀ + 2K₀q₀⁻¹K₀).

This equals the exact Einstein second jet q_nn = 2K_n = 2(Ric+3q−HK+2Kq⁻¹K) **because H=0 at the minimal Koiso center** (step94 verifies tr W = 0 to 2×10⁻¹²). The term is B²=4A², independent of the sign of B, so both the +2A and −2A halves carry the identical exact second jet — exactly the sign-independence the code relies on. The noncommutative correction to e^X enters only at O(n³); it does not touch the prescribed jets. The code's `jet_validation` confirms: q0_exact 2×10⁻¹⁵, analytic_qn0 4×10⁻¹⁵, analytic_qnn0 8.5×10⁻¹⁴. The radial shapes t³(1−t)³ vanish to third order at both ends, so the adjustable θ-fields preserve all endpoint jets and the C² attachments. Construction verified.

### (iii) The Cholesky conjugation is a genuine invariant norm

`eo = L⁻¹EL⁻ᵀ` with g₄ = LLᵀ. The eigenvalues of eo are the generalized eigenvalues of (E, g₄), i.e. the eigenvalues of g₄⁻¹(Ric+3g) = the frame-independent eigenvalues of the (1,1) Einstein-defect tensor. `op = max|eigenvalue|` is therefore the true operator norm of Ric+3g with respect to g, not a Euclidean symmetrization of q⁻¹E. The √2-weighted packing makes the vector Euclidean norm equal the Hilbert–Schmidt norm of the g-orthonormalized defect. The 0.5(eo+eoᵀ) step only cleans roundoff (eo is analytically symmetric). Correct.

### (iv) What the residual decrease establishes — and the artifacts that dominate at ns=16

Two distinct facts must be separated.

1. **The resolution-64 full-matrix JSON did no optimization** (`gn_steps: 0`, all θ = 0, positive/negative_theta_norm = 0). Its baseline operator_sup 970 / 99.6 is purely the tangential Ricci of the naive quintic-in-X interpolant (peak at interior r≈0.91), an ansatz artifact of the initial guess, not evidence about attainable residual.

2. **The direct nodal decrease (`step98_direct_spd_N16_interior.json`) 32.5 → 1.36 and 15.3 → 1.36** is the meaningful reduction, but its floor is not geometric:
   - The final `operator_sup = 1.3634185384213706` on **both** sides equals, to all digits, the ns=16 center value in `step98_center_residual_resolution.json` (1.3634185384213748), reached at `peak_r = 0.0` with `normal_tangential_frobenius = 1.3634…`. The optimizer drove the interior down until the residual is dominated by the **center Codazzi term**, which is fixed by the ns=16 Fourier resolution and cannot be moved by interior X (the center is pinned to exact Koiso data). The center table shows this term is pure aliasing: 1.36 (16) → 0.329 (32) → 0.0121 (64) → 6.8×10⁻⁶ (128), super-algebraic decay, while E_nn and E_ij stay at 10⁻¹⁴. So the reported "final 1.36" is a resolution floor, not a small Einstein defect.
   - The solve is far from converged: `success:false`, `nfev:4`, `optimality:745`/`79.7`, `step_norm≈9`, regularizer weight 10⁻³ active. This is one large regularized Gauss–Newton step, not a minimum. `final_geometric_norm 8.9` is a one-step value at coarse resolution.
   - **Parameter count ≈ residual count:** 864 nodal unknowns vs ≈ (nr−2)·ns·6 = 864 interior geometric components; the H² regularizer is what makes the system solvable. At ns=16 the s-products in the Codazzi/Christoffel terms alias heavily, so the field is partly fitting grid-scale aliased residual. No resolution-independent decrease has been shown.

   **The exterior model is not Einstein — a permanent endpoint defect.** The attachment target is q = e^{2R}q₀ (C² to the exterior e^{2r}q₀). But dr²+e^{2r}h is Einstein (Ric=−3g) only when h is Ricci-flat. The charged Koiso slice has R(q₀) = −6−S ≠ 0, so at r=R,
   E_ij = Ric(e^{2R}q₀) = Ric(q₀) ≠ 0, with invariant size ‖(e^{2R}q₀)⁻¹Ric(q₀)‖ = e^{−2R}‖q₀⁻¹Ric(q₀)‖.
   This is exactly the `end_operator_sup = 1.07` seen at R=1 in the nodal run (and 0.053 at R=2.5 in the full-matrix run, consistent with e^{−2R} shrinkage). Consequence: with this exterior the global object is not a genuine two-end Einstein connector, and the finite-domain residual cannot reach zero even in principle — there is an irreducible O(e^{−2R}‖Ric(q₀)‖) endpoint contribution. A real end must let the orbit shape/charge evolve toward an actual Einstein asymptotic (the step96 note §7 already anticipates "expanding OT ends" with asymptotic orbit shapes; the step98 code has not implemented that, it uses the placeholder cusp). The scripts' interpretation strings are consistent with the evidence ("does not establish an arbitrarily small defect … a persistent residual is not a geometric obstruction"); the numbers do not say more than that.

### (v) The decisive convergence and residual-projection calculation

Three things would actually discriminate feasibility from a finite obstruction, in order of value:

1. **Converged cross-resolution study with the center floor removed.** Run the direct nodal solve to true stationarity (large nfev, gtol→0, reg scaled ↓ with resolution) at ns = 16, 24, 32, 48, 64 and nr = 11, 15, 21, 27, at fixed R. Report the minimized invariant defect restricted to strictly-interior r **and with the known center Codazzi value (from `step98_center_residual_resolution.json`) subtracted or Richardson-extrapolated**, plus the endpoint value tracked separately. The single sharp question: does the interior-only minimized sup converge to a positive number as ns→∞ (finite obstruction at fixed R) or keep decreasing (finite-domain matching feasible)? The current "1.36 on both sides" answers nothing because it is the ns=16 center floor.

2. **Cross-R decay at fixed high resolution.** With ns≥48, vary R = 1.5, 2.5, 4, 6. The endpoint term must fall like e^{−2R}; the step96 redshift heuristic predicts charge/curvature tapers of O(e^{−3R}) and O(e^{−6R}). If the interior floor tracks these exponentials → an approximate long-collar connector exists; if it saturates at a positive value independent of R → the finite obstruction the local K_X test cannot see.

3. **Full-block linearized singular-triplet calculation.** The `svd_analysis` in the full-matrix script already computes range_fraction and the inaccessible residual, but the recorded run used gn_steps=0 so no SVD exists. Assemble the Jacobian of the **complete** residual (E_nn, E_ni, E_ij together — not tangential-only), take its smallest singular value σ_min and left singular field u_min, split by block and by location, and track σ_min vs ns and vs R. A u_min localizing at the center flags the Codazzi resolution artifact; localizing at r=R flags the non-Einstein exterior; spread over the interior with nonzero pairing against the exact center data is the genuine obstruction the note §7 seeks. This is the finite-dimensional shadow of the Douglis–Nirenberg smallest-singular-value computation the step96 note already names as decisive.

---

**Summary of correctness.** The Gaussian block formulas, the matrix-exponential jet construction (including sign-independence and the third-order-only noncommutative term), and the Cholesky invariant norm are all correct and internally cross-validated (hyperbolic exact zero; spectral convergence of the center to Einstein). Two things must reshape the reading of the residual numbers: the reported final "1.36" is the ns=16 center Codazzi aliasing floor rather than an Einstein defect, and the e^{2r}q₀ exterior is not an Einstein end (it injects a fixed Ric(q₀)·e^{−2R} endpoint residual), so the ns=16 nodal decrease is a coarse, under-converged, regularizer-stabilized fit that does not yet carry resolution-independent geometric meaning. The unresolved substance is precisely the converged interior floor as a function of ns and R with the center/endpoint contributions separated out, and the full-block σ_min with its left field's localization.