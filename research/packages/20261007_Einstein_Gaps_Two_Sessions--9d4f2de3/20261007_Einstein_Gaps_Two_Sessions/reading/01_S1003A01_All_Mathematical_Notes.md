# S1003A01 complete mathematical notes

Original notes follow in numerical step order. Later corrections are retained in their original locations. The current synthesis and correction table are the reading entry points.

- [step2_cell_problem_and_triaxial_numerics.md](../sources/Sessions/S1003A01/workspace/notes/step2_cell_problem_and_triaxial_numerics.md)
- [step3_coupled_compensation_and_route_reassessment.md](../sources/Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md)
- [step4_positive_q_and_recovered_volume.md](../sources/Sessions/S1003A01/workspace/notes/step4_positive_q_and_recovered_volume.md)
- [step5_slice_charge_and_zero_flux.md](../sources/Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md)
- [step6_perpendicular_dual_cost_and_relative_calibration.md](../sources/Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md)
- [step7_perpendicular_verification_and_endpoint_map.md](../sources/Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md)
- [step8_kahler_period_law_and_Rplus_response.md](../sources/Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md)
- [step9_subthreshold_cell_verification.md](../sources/Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md)
- [step10_rigorous_subthreshold_cell_and_O11.md](../sources/Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md)
- [step11_independent_review_O11_and_mixed_cost.md](../sources/Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md)
- [step13_pair_overlap_interaction.md](../sources/Sessions/S1003A01/workspace/notes/step13_pair_overlap_interaction.md)
- [step14_large_collar_resistance_and_cluster_budget.md](../sources/Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md)
- [step15_bolt_neutral_transport_and_area_branch.md](../sources/Sessions/S1003A01/workspace/notes/step15_bolt_neutral_transport_and_area_branch.md)
- [step16_joint_dual_calibration_and_exact_bolt_chirality.md](../sources/Sessions/S1003A01/workspace/notes/step16_joint_dual_calibration_and_exact_bolt_chirality.md)
- [step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md](../sources/Sessions/S1003A01/workspace/notes/step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md)
- [step18_corrected_riccati_and_H4_comparison.md](../sources/Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md)
- [step19_exterior_null_line_LM_stationary_cells.md](../sources/Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md)
- [step21_conformal_selection_su2_stability_constrained_HJ.md](../sources/Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md)
- [step22_exact_CH_conformal_reduction.md](../sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md)
- [step23_scalar_relaxed_j1_CR_pinning_and_certification.md](../sources/Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md)
- [step24_normalized_gauge_resolved_j1.md](../sources/Sessions/S1003A01/workspace/notes/step24_normalized_gauge_resolved_j1.md)
- [step25_degeneration_matching_and_charge.md](../sources/Sessions/S1003A01/workspace/notes/step25_degeneration_matching_and_charge.md)
- [step26_action_budget_matching.md](../sources/Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md)
- [step26_step_summary.md](../sources/Sessions/S1003A01/workspace/notes/step26_step_summary.md)
- [step28_AK_gap_identity_nijenhuis_transport.md](../sources/Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md)
- [step29_boundary_corrected_AK_exterior_and_contact_capacity.md](../sources/Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md)
- [step31_ramified_KE_transfer_and_interface_simplification.md](../sources/Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md)
- [step33_surgery_slope_law_and_ASD_retention.md](../sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md)
- [step35_cap_transfer_neutrality_and_cap_cells.md](../sources/Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md)
- [step36_perpendicular_cap_transplant.md](../sources/Sessions/S1003A01/workspace/notes/step36_perpendicular_cap_transplant.md)
- [step37_cap_congruence_transport.md](../sources/Sessions/S1003A01/workspace/notes/step37_cap_congruence_transport.md)
- [step38_curvature_conditioned_cap_response.md](../sources/Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md)


---

## Source step2_cell_problem_and_triaxial_numerics.md

Original: [sources/Sessions/S1003A01/workspace/notes/step2_cell_problem_and_triaxial_numerics.md](../sources/Sessions/S1003A01/workspace/notes/step2_cell_problem_and_triaxial_numerics.md)

# Step 2 (Agent2, Explore): the cell problem as the local heart of O11

Session S1003A01, 4 Oct 2026. Builds on the inherited relative-cell theory
(`Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md`, "I54",
and `.../20260928_localization_and_coupled_filling.md`, "I55"). Normalization: Ric = -g on the
complex-hyperbolic (CH) background, operator norm on W^+, J = ∫|Ric+g|^2, j = J/(2π^2).

## 1. All-metric global identity and the Weyl-deficit form of coefficient four

Let M be a closed member of the balanced family, 2χ+3τ = A - Q, Q = k + 4ℓ, A = c_1^2(X), and let
the inherited supplier (I03) give a monopole class with (c^+)^2 ≥ A for the metric considered.
Chern–Weil, 4π^2(2χ+3τ) = ∫(2|W^+|^2 + s^2/24 - |Ric°|^2/2), and |Ric+g|^2 = |Ric°|^2 + (s+4)^2/4 give,
for every smooth metric g on M (no normalization of the optimal λ assumed),

    ∫|Ric+g|^2 - 8π^2 Q = 4 𝒲 + 𝒮,
    𝒲 = ∫|W^+|^2 - (4π^2/3) A,
    𝒮 = ∫((s+3)^2/3 + 1) dV - (8π^2/3) A = ∫(s^2/12 + (s+4)^2/4) dV - (8π^2/3) A.

LeBrun's estimate S = ∫s^2 ≥ 32π^2 (c^+)^2 ≥ 32π^2 A gives 𝒮 ≥ (S - 32π^2A)/12 ≥ 0 for *every* metric.
Hence the only term that can make the cost per surgery unit fall below 8π^2 is a **self-dual Weyl deficit**
𝒲 < 0, i.e. ∫|W^+|^2 below its Kähler–Einstein value (4π^2/3)A, and it must beat the scalar
excess 𝒮 by a factor 4. (For the Ric=-g scaling with optimal λ, α ≈ ∫|Ric+g|^2/(2π^2 A), so
coefficient four ⇔ 4𝒲 + 𝒮 ≥ -o(Q) along near-minimizers.)  The localized version is exactly I54 (1.2);
the sharpness of each piece: 𝒮 = 0 iff s ≡ -4 and S = 32π^2A; 𝒲 = 0 at KE.

Corollaries recorded (elementary, all-metric):
* If |W^+|^2 ≥ s^2/24 pointwise (true for all Kähler metrics, s ≤ 0 or not), then
  F = ∫(s^2/24 + 2|W^+|^2) ≥ S/8 ≥ 4π^2 A, and P = ∫|Ric°|^2 = 2F - 8π^2(A-Q) ≥ 8π^2 Q exactly:
  coefficient four holds with no error term in the whole "W^+ at least Kähler-sized" class.
* The two SW estimates alone (∫s^2 ≥ 32π^2A, ∫(-s+√6|W^+|)^2 ≥ 72π^2A) only give
  4𝒲 + 𝒮 ≥ -(4/3)Vol(X) = -(8π^2/3)A (global analog of the cell bound J ≥ 8π^2q - 4d/3, I54 (7.2));
  their joint minimizer has √6‖W^+‖ = ‖s‖/8, a W^+ one quarter of the Kähler ratio. The missing
  information is differential (how W^+ can be depleted on an actual metric), not algebraic.
* The strategist's B_{1/6} remark: B_{1/6} = ∫|W|^2_tensor + ∫s^2/6 = 2P + 32π^2χ. A Weyl-energy decrease
  à la Malchiodi–Malizia lowers 𝒲 (if it lowers the W^+ part) and must be weighed against 𝒮 of the
  same metric (Yamabe-negative representative); per-site saving must be order one at fixed neck scale.

## 2. Cell conjecture

Cell = blowup (and/or handle) of a CH ball D with exact CH collar (I54 §1); j-threshold 4 per blowup.
I54 (2.2)–(2.3): a single cell with J < 8π^2 q gives a balanced coefficient below 4 on the actual
family (single-blowup cell J_1 < 8π^2 already gives 28/9 + J_1/(9π^2) < 4). So

  **Coefficient four ⟹ Cell conjecture:** every smooth cell satisfies J(C) ≥ 8π^2 q.

Conversely I55 Theorem 1 handles arbitrary interiors once a CH bulk is present; O11 then splits into
(i) the cell conjecture (finite energy O(1) per cell), and (ii) bulk extraction from near-minimizers
(energy O(A), precision o(Q)). Part (i) is a finite-energy problem — a structural advantage over the
global ideal-minimizer route, where o(Q) precision from O(A) energy is the known obstruction.

### 2.1 Numerical evidence in the conformal triaxial (SU(2)-diagonal) class

Scripts (all in `workspace/scripts/`):
* `cell_ricci.py` — sympy Bianchi-IX Ricci of G = e^{2φ}K, K = dr²/F + r²(e^{2w}σ1² + e^{-2w}σ2²) + r²Fσ3².
  Output agrees symbol-by-symbol with I54 (6.10) (D_0, D_3, D_H+c checked by hand).
* `cell_opt.py` — Chebyshev parametrization in x = log(r/r0)/log(Rc/r0) with exact bolt conditions
  F(r0)=0, F'(r0)=2/r0, w = O((r-r0)^2), φ free at the bolt, and exact CH beyond Rc (C^3 matching);
  Gauss–Legendre quadrature with √x clustering; torch float64 + L-BFGS.
* `check_kahler_identity.py` — verifies the exact Kähler identity j = (2+μ)^2 + ½∫(s+4)^2 r^3 dr
  (I54 (3.2)) on random profiles to 1e-13 relative, both coordinates.
* `sweep1.sh` (data `data/cell_sweep1/`, 224 runs: Rc ∈ {0.8,1.2,2,3}, μ ∈ {0.001,…,0.6}, modes
  conformal-biaxial and full (F,w,φ), 2 inits × 2 seeds, degree 18).
* `cell_stage2.py`, `sweep2.sh` (data `data/cell_stage2/`): degree 24, optimize (F,φ) at w=0, full Hessian
  by autograd, w-block eigenvalues, then 12 kicked full restarts (lowest w-eigenvector and random
  directions, amplitudes 0.05, 0.3, 1).
* `plot_cells.py` → `figures/cell_cost_vs_bound.png`.

Results:
* No subthreshold cell: min over all runs of j - 4 is 0.0040 (μ = 0.001); j_best - 4 ≈ 4μ + μ^2.
* Every optimum lies above the conformally-Kähler bound of I54 Theorem 1,
  j ≥ (2+μ)^2/(1 - μ^2/R^4); min excess 2.8e-6. For large R and small μ the optimum is within
  1e-4 of that bound (R = 4: μ=0.01 → 4.04015 vs 4.04010; μ=0.1 → 4.41232 vs 4.41017).
* The w-Hessian at the conformal-biaxial optimum is positive semidefinite (smallest eigenvalues
  1e-9–1e-7 are near-null basis directions, largest 60–5000); kicked restarts lower j only by ≤ 1e-2
  and only in high-cost cells (e.g. μ=0.3,R=1: 11.455 → 11.445), never below the bound.
  (This matches I54 §6.2: triaxial descent exists for expensive cells but does not cross threshold.)

Interpretation (numerical, within the computed finite-dimensional class, not a proof):

  **Conjecture C1.** For every smooth conformal triaxial one-bolt cell with CH collar of radius R,
  J/(2π^2) ≥ (2+μ)^2 R^4/(R^4 - μ^2), i.e. I54 Theorem 1 extends from the conformally Kähler class to
  the whole conformal almost-Kähler diagonal class. The bound appears asymptotically sharp as R → ∞.

C1 would close I55 §8's open window (8.4) in this class. Its proof needs a coupling between the
nonintegrability budget N, the Weyl remainder B_0 (triaxial anisotropy splits the repeated W^+ eigenvalue)
and the scalar variance, as in I54 (6.11). The numerics say the optimizer never uses N: the anisotropy cost
in B_0 seems to dominate the formal window gain.

### 2.2 A conditional proof route for the cell conjecture (finite-energy bubbling)

Fix D and topology q. Let J_inf = inf J over cells. Facts:
(a) I54 Prop. 2: no smooth cell is stationary for J under compactly supported variations
    (scalar test gives s = -4, then E = Ric+g solves an elliptic system and vanishes by unique
    continuation; analyticity contradicts the topology).
(b) Bubble cost: an AE metric on O(-1) (χ=2, τ=-1, flat end, 2(χ-1)+3τ = -1) has
    P = ∫|Ric°|^2 = 8π^2 + 2∫(2|W^+|^2 + s^2/24) ≥ 8π^2 (equality iff W^+=0, s=0: Burns), so
    ∫|Ric|^2 = P + S/4 ≥ 8π^2; the AE core of a handle
    costs ≥ 32π^2 (2(χ-1)+3τ = -4). Whole marked AE cores cost 8π^2 per exceptional class (inherited).
(c) Lower semicontinuity plus "energy identity" along a minimizing sequence, if it converges smoothly
    away from finitely many points to a cell C_∞ with bubble tree B:
    J_inf ≥ J(C_∞) + Σ cost(B).
Then: if the topology stays in C_∞, C_∞ is a minimizer, hence stationary, contradicting (a); otherwise
the bubbles carry the classes and J_inf ≥ 8π^2 q. **So the cell conjecture follows from compactness modulo
AE bubble trees (and exclusion of interior collapse) for J-minimizing sequences of cells.**
The analytic gap: ∫|Ric+g|^2 is critical (L^2 Ricci in dimension 4) and gives no ε-regularity for
non-critical sequences. Natural regularization (Sacks–Uhlenbeck type): J_ε = J + ε∫|Rm|^p, p > 2, or
+ε∫|∇Ric|^2; minimizers of J_ε are smooth critical points; one needs ε-regularity uniform in ε and an
energy identity as ε → 0, plus exclusion of collapse (I54 (7.2) gives 4d/9 < Vol < 4d for subthreshold
cells, a volume window but not noncollapse). This is a genuine theorem to prove, with literature
counterparts (Tian–Viaclovsky ε-regularity for critical metrics of quadratic functionals; Sacks–Uhlenbeck;
Anderson/Petersen–Wei L^p-curvature compactness for p > 2).

## 3. Assessment

* The fixed-scale construction route (MM gluing, triaxial or conformal cells) is the only way to change
  the coefficient; within the whole SU(2)-diagonal conformal class it fails numerically and the infimum
  appears to be the Kähler-area value (2+μ)^2 → 4, approached only as the bolt shrinks: the cell problem
  is non-attaining, consistent with I54 Prop. 2.
* Remaining construction candidates must leave the cohomogeneity-one diagonal class: non-diagonal SU(2)
  metrics, U(1)-invariant (Gibbons–Hawking-type with Bogomolny–Kähler cancellation lost), or genuinely
  non-symmetric MM-type necks with orientation chosen to deplete W^+ (𝒲 < 0).
* The lower-bound route has a clean finite-energy target (2.2) and a clean global form (§1).



---

## Source step3_coupled_compensation_and_route_reassessment.md

Original: [sources/Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md](../sources/Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md)

# Step 3 — Coupled compensation in the triaxial cell and route reassessment

Session S1003A01, 4 Oct 2026. This note corrects and sharpens the Step-2 interpretation of O11. Notation follows I54 (`20260928_relative_cell_cost.md`) and I55 (`20260928_localization_and_coupled_filling.md`). The metric on a one-bolt cell is

\[
G=e^{2\phi}K,
\qquad K=\frac{dr^2}{F}+r^2(e^{2w}\sigma_1^2+e^{-2w}\sigma_2^2)+r^2F\sigma_3^2,
\]

with \(r_0^2=\mu\), exact complex-hyperbolic germ on a collar through radius \(R\), and
\(j=J/(2\pi^2)\), \(J=\int|\operatorname{Ric}_G+G|^2\).

## 1. The exact C1 deficit

For a general \(k\)-point conformal almost-Kähler cell, I54 uses

\[
v_K=d-\frac{T_2}{2},\qquad m_0=4d+4\pi T_1,
\qquad N=\frac12\int|\nabla\omega|^2.
\]

The scalar-free part of its conformally Kähler lower bound is

\[
\mathcal K=8\pi^2k+8\pi T_1+2T_2+
 \frac{(2\pi T_1+T_2)^2}{v_K}
 =8\pi^2k-4d+\frac{m_0^2}{4v_K}.
\]

Expanding the first two quadratic terms in I54 (6.6) gives the **exact** identity

\[
\boxed{
J(G)-\mathcal K
=\frac{A_0}{12}+4B_0+\frac14L_G
-\frac{N(2m_0-3N)}{4v_K},
}\tag{1}
\]

where \(L_G=\int(s_G+4)^2\). Thus the conjectured extension C1,
\(J\ge\mathcal K\), is equivalent to

\[
\boxed{
\frac{A_0}{12}+4B_0+\frac14L_G
\ge \frac{N(2m_0-3N)}{4v_K}.
}\tag{2}
\]

Only \(0<N<2m_0/3\) needs new information. This corrects the Step-2 suggestion that one should seek a bound on \(B_0\) alone: scalar transfer \(A_0\), self-dual Weyl anisotropy \(B_0\), and scalar variance \(L_G\) can and generally must pay jointly. Also, C1 is weaker than extending the *full* Theorem-1 remainder \(\mathcal K+L_G/4\), which would require (2) without the \(L_G/4\) term.

For one bolt in the radial normalization,

\[
d=\frac{\pi^2R^4}{2},\quad v_K=\frac{\pi^2}{2}(R^4-\mu^2),\quad
m_0=2\pi^2(R^4+2\mu),
\]

and therefore

\[
\frac{\mathcal K}{2\pi^2}=rac{(2+\mu)^2R^4}{R^4-\mu^2}.
\]

There is no hidden conformal-factor error: I54 writes \(K=u^2G\), I55 writes \(G=e^{2\phi}K\), so \(u=e^{-\phi}\); the conformal gradient term is part of \(A_0\). The exceptional period \(t_E=\pi\mu\) is measured by the canonical almost-Kähler metric \(K\), not directly by \(G\).

## 2. Exact radial form of the same problem

I55 defines

\[
I_R=\frac14(\mu^{-2}-R^{-4}),\quad
P_w=\int\left\{\frac{2F(w')^2}{r}+
\frac{8(\cosh2w-1)}{r^3}+
\frac{8\sinh^2(2w)}{r^3F}\right\}dr,
\]

\[
T_\phi=2\int\frac{F(\phi')^2}{r}dr,
\quad q=T_\phi-P_w,
\quad M_0=1+\frac2\mu,\quad M=M_0-q.
\]

Its Proposition 5 says

\[
j=\frac{M^2}{4I_R}+\mathscr R_{\rm rad},
\]

where

\[
\mathscr R_{\rm rad}=\frac14\int r^3\left(X-\frac{M}{I_Rr^4}\right)^2
+\frac14\int r^3Y^2+\frac12\int r^3Z^2+2\int r^3V_w^2.
\]

Since \(M_0^2/(4I_R)=\mathcal K/(2\pi^2)\), C1 is equivalently

\[
\boxed{
\mathscr R_{\rm rad}\ge
\frac{q(2M_0-q)}{4I_R}
\quad\text{when }0<q<2M_0.
}\tag{3}
\]

This is not a new theorem; it is the sharp profile-level target. It retains all actual variables and all residuals. The scalar mean identity

\[
L_Y=\int r^3Y=4B_\phi-\mu^2-2\mu-n-6G_\phi
\]

and its variance decomposition should be used inside (3), not optimized separately. The I55 zero-moment test shows why: a bolt-scale conformal profile can have \(M=0\) while keeping bounded total cost, and the payment then moves into the \(X,Y,Z\) squares. A scalar zeroth moment or a lower bound on \(|M|\) cannot close the problem.

A second warning is essential. If \(n=N/(2\pi^2)\), then

\[
n=2\int r^3F\left(w'+\frac{2\sinh2w}{rF}\right)^2dr,
\]

whereas \(P_w\) uses inverse radial weights. They are not interchangeable. After integrating its cross term, \(n\) even contains a negative \(-8\int r(\cosh2w-1)\) contribution. Equations (2) and (3) are equivalent global decompositions, but their apparent dangerous variables \(N\) and \(q\) encode different profile moments.

## 3. New computational instrument: measure compensation, not another unconstrained minimum

`workspace/scripts/cell_compensation.py` augments the verified Ricci code with both exact decompositions. For every actual Chebyshev profile it computes

- \(j\), the C1 constant \(K\), and \(j-K\);
- \(N/(2\pi^2)\), \(P_w,T_\phi,q,M\);
- the four radial payments \(R_X,R_Y,R_Z,R_V\);
- \(A_0/(2\pi^2)\), and \(B_0/(2\pi^2)\) inferred from the exact I54 identity;
- the formal gain \(n(2m-3n)/(4v)\);
- exact residuals of I54 and I55 as internal checks.

Pilot runs satisfy the radial decomposition to about \(10^{-13}\) and the I54 decomposition to machine precision. This simultaneously checks the normalizations and avoids implementing a second, unverified self-dual curvature operator merely to evaluate \(B_0\).

The script performs an augmented-Lagrangian minimization of \(j\) at prescribed \(N/m_0\), initialized from an optimized biaxial conformal cell and then seeded in low triaxial modes. This asks the correct scientific question: at a given formal nonintegrability gain, which actual remainder pays, and can their sum fall below it? Early moderate targets (for example \(\mu=0.1,R=2,N/m_0\approx0.05\) or \(0.15\)) are extremely expensive, with \(j\) of order \(20\) or \(60\), rather than near \(K\approx4.413\). Most payment appears in the inferred \(B_0\) and in \(V_w\), while the exact decomposition remains satisfied. These pilot values are numerical behavior of a finite-dimensional constrained optimizer, not lower bounds; they show that the earlier generic searches stayed close to \(N=0\) for a structural reason, but do not settle small \(N\) or finite-amplitude escape.

A broader small-to-middle-\(N\) sweep is running in `data/cell_compensation/sweep_mu01_R2.jsonl` (task reference `s3_t20_tool1`). The highest-value interpretation is the scaling as \(N\downarrow0\): if the minimum excess payment is linear or superlinear compared with the formal gain, that identifies the candidate coercive modulus. Repeating unconstrained optimization above four would add little.

## 4. What outside almost-Kähler identities do and do not give

The retrieved paper `Knowledge/objects/papers/Almost-Kähler-four-manifolds-with-harmonic-self-dual-Weyl-curvature--e2ac226d605a--8b3f793203ff/object.md` records the pointwise algebraic inequality

\[
|W^+|^2-|W^+(\omega)^\perp|^2\ge \frac38[W^+(\omega,\omega)]^2
\]

and, under the additional differential equation \(\delta W^+=0\), a LeBrun integral identity yielding \(\int s^2/24\ge\int|W^+|^2\), with equality only for cscK metrics. This explains how harmonic-Weyl criticality can convert Weyl anisotropy into scalar payment. It does **not** apply to arbitrary cell competitors: neither \(K\) nor \(G\) is assumed to satisfy \(\delta W^+=0\). Therefore the missing estimate is not already present in that literature. A productive inheritance would be to derive a *defect version* in which the failure of \(\delta W^+=0\) is paired with the actual Ricci residuals \(X,Z,V_w\), precisely the terms already visible in (3). This is a more plausible route than importing the harmonic-Weyl theorem verbatim.

## 5. Correction to the general bubbling route

The Step-2 implication “smooth minimizer or all topology paid for by AE bubbles” was too strong. Even after one proves compactness and an energy identity, a minimizing sequence can have an orbifold base, quotient-ended ALE levels, and marked topology distributed across the tree. A quotient-ended Ricci-flat ALE bubble can carry nontrivial \(H_2\) while paying zero \(\int|\operatorname{Ric}|^2\); Gauss–Bonnet and APS signature charges include \(1/|\Gamma|\) and \(\eta(S^3/\Gamma)\), so an individual terminal bubble has no universal \(8\pi^2\) Ricci charge. The smooth no-critical-cell proposition only forces a smooth stationary limit to be CH; it does not rule out a locally CH orbifold base resolved by Ricci-flat ALE pieces. Handles may enter collapsed necks rather than isolated \(H_2\)-bubbles.

Thus a lower-bound proof by degeneration requires, in addition to analytic compactness:

1. the limiting Euler–Lagrange equation on the regular base and classification/exclusion of residual locally CH orbifold geometries compatible with the fixed outer germ;
2. relative Chern–Weil/APS bookkeeping across every interface;
3. preservation and decomposition of the marked primitive exceptional/handle classes;
4. a whole-tree theorem that the **combined** base and bubble configuration pays \(8\pi^2q\).

The relevant charge belongs to a whole marked AE filling, not to each terminal bubble or homology generator. This makes general regularization much broader than C1 and not the best immediate main route.

## 6. Route judgment after the sharpening

The strongest immediate O11 line is the exact diagonal cell problem, but now as a coupled coercivity problem, not more unconstrained minimization:

- derive an inner-scale inequality after \(r=\sqrt\mu\,x\) coupling the inverse-weight conformal moment to \(Z\) and \(V_w\);
- combine it with an outer terminal-value estimate from the exact CH collar and the scalar mean/variance split for \(Y\);
- use constrained profiles to discover the correct coefficient and equality/degeneration mechanism;
- separately retain fixed-scale non-diagonal/MM constructions as the falsification route, because a subthreshold cell would immediately change the balanced first coefficient.

The desired lemma is exactly (3), or at minimum the weaker threshold version \(\mathscr R_{\rm rad}\ge4-M^2/(4I_R)\). The global cell conjecture and all-competitor balanced coefficient still require work outside this symmetric class. O10 and the fixed bundle \(E_D\) remain independent central branches; nothing in this note changes their status.

## 7. Fixed-exterior rigidity removes one major orbifold alternative

The broad warning about orbifold bases can be sharpened substantially for this *fixed-collar* problem. Let \(X=\mathbb{CH}^2/\Gamma\) be the original closed smooth CH surface, with volume \(V\), and choose the cell ball \(D\) with \(d=\operatorname{Vol}(D)<V/2\). Suppose a noncollapsed critical degeneration, after the unchanged exterior is glued back, has a compact connected orbifold base \(\mathcal O\) which is locally CH and contains the original exterior \(U=X\setminus D^\circ\) isometrically. Then \(\mathcal O\) is actually the original smooth CH surface.

Indeed, a complete locally CH orbifold is \(\mathbb{CH}^2/\Gamma'\) for a discrete cocompact isometry group \(\Gamma'\). Since deleting a four-ball does not change the fundamental group, \(\pi_1(U)=\Gamma\). Equality of the CH germ makes the holonomy of the embedded exterior the original faithful lattice representation, so after conjugation \(\Gamma<\Gamma'\). A lattice contained in a discrete group has finite index, and

\[
\operatorname{Vol}(\mathcal O)=\frac{V}{[\Gamma':\Gamma]}.
\]

On the other hand the embedded exterior has volume \(V-d\), hence

\[
V-d\le\frac{V}{[\Gamma':\Gamma]}.
\]

Because \(d<V/2\), the index is strictly below two and must equal one. Thus \(\Gamma'=\Gamma\), which is torsion-free, so \(\mathcal O\cong X\) smoothly and isometrically.

The local Euler–Lagrange equation supplies the locally CH hypothesis without integrating across orbifold points. On the regular base, compactly supported conformal variations give

\[
\Delta_+s+s+4=0.
\]

Since \(s=-4\) on the unchanged open collar, scalar unique continuation gives \(s\equiv-4\) on the connected regular set. The tensor equation then reduces to the I54 equation for \(E=\operatorname{Ric}+g\); because \(E=0\) on the collar, elliptic unique continuation gives \(E=0\). Einstein analyticity and continuation of the CH curvature type make the regular base locally CH, and this statement lifts through each orbifold chart.

Consequences for the bubbling route are precise. Under a noncollapsed orbifold compactness theorem with enough convergence to preserve the full exterior and to pass stationarity to the regular base, **orbifold base singularities are excluded by the exterior-volume argument**. Any bubble tree is attached to a smooth CH base point, so its root has trivial outer end group. Quotient end groups and eta terms may still appear at deeper levels, but they must cancel inside a whole tree whose external interface is \(S^3\). The remaining topological theorem is therefore narrower than stated in Section 5: establish the \(8\pi^2q\) cost for each complete critical whole-tree filling with trivial outer end and the inherited marked relative classes. Collapse and noncritical minimizing sequences remain separate analytic difficulties. This fixed-exterior rigidity does not by itself prove compactness or the cell conjecture, but it removes the most dangerous residual base geometry rather than merely listing it.

## 8. Stronger consequence: the noncollapsed stationary orbifold branch already obeys the threshold

Independent verification sharpened Section 7 in two ways.

First, the volume-smallness assumption is unnecessary once the exterior is a **smooth injective local isometry**, not merely a metric-space image. A precise statement is:

> Let \(X=\mathbb{CH}^2/\Gamma\) be closed and smooth, and let \(D\) be one embedded closed four-ball, or finitely many disjoint such balls, with connected exterior \(U=X\setminus D^\circ\). If a compact connected effective boundaryless locally CH orbifold \(\mathcal O\) admits a smooth injective local isometry \(U\to\mathcal O\), then \(\mathcal O\) is smooth and globally isometric to \(X\), with the global isometry extending the given exterior map.

The proof must use developing maps. The exterior inclusion gives, after conjugacy, \(\Gamma<\Gamma'\) for \(\mathcal O=\mathbb{CH}^2/\Gamma'\). If \(g\in\Gamma'\setminus\Gamma\), injectivity of \(U\to\mathcal O\) forces \(g\widetilde U\cap\widetilde U=\varnothing\). Hence the connected unbounded set \(g\widetilde U\) lies in one bounded lifted ball, impossible. Therefore \(\Gamma'=\Gamma\). Compactness/effectiveness/completeness and the smooth local-isometry hypothesis are essential; equality of a small collar germ alone would not establish the lattice inclusion.

Second, once this rigidity holds, the relative density (I54 (1.2)) makes whole-tree APS accounting unnecessary for the *threshold*. Let

\[
F(g)=\frac{(s+3)^2}{3}+1+4|W^+|^2\ge0.
\]

On CH, \(F=4\). If a fixed-collar sequence converges in \(C^2_{\rm loc}\) off finitely many points to a stationary orbifold base, Sections 7--8 show that the base is the original CH ball. For compact sets \(K\Subset D\setminus S\),

\[
\int_KF(g_i)\longrightarrow4\operatorname{Vol}(K).
\]

The exact relative identity

\[
J_i-8\pi^2q=\int_CF(g_i)-4d
\]

and nonnegativity on the omitted bubble/neck region give, after \(K\uparrow D\setminus S\),

\[
\boxed{\liminf_iJ_i\ge8\pi^2q.}
\]

Thus stationary noncollapsed finite-point orbifold degeneration cannot be a subthreshold mechanism, regardless of how quotient-ended ALE levels and marked topology are distributed. The remaining cell problem has become more sharply localized: a subthreshold sequence must evade this branch through collapse, failure of stationary/regular convergence, a non-orbifold or multi-fold completion, non-finite concentration, or a genuine smooth finite-amplitude competitor. The analytic compactness theorem remains hard, but the feared base/bubble charge classification is not needed merely to reach the threshold once the fixed exterior survives.

## 9. Result of the fixed-\(N\) compensation sweep

The managed sweep completed 32 constrained optimizations at \(\mu=0.1,R=2\), degree 14, with four low-mode starts at each target \(N/m_0\in\{5\cdot10^{-4},10^{-3},0.003,0.01,0.03,0.1,0.3,0.55\}\). Data are in `workspace/data/cell_compensation/sweep_mu01_R2.jsonl`; the complete execution record is in `workspace/tasks/s3_t20_tool1/`.

Every run stayed above C1, and both exact decompositions closed at roughly \(10^{-14}\). Representative best values are

| target \(N/m_0\) | attained | best \(j-K\) | formal gain | dominant payment |
|---:|---:|---:|---:|---|
| 0.0005 | 0.000507 | 0.1844 | 0.01663 | \(4B_0\approx0.198\), \(R_V\approx0.153\) |
| 0.001 | 0.001005 | 0.3432 | 0.03294 | \(4B_0\approx0.372\), \(R_V\approx0.303\) |
| 0.003 | 0.002998 | 0.9804 | 0.09796 | \(4B_0\approx1.073\), \(R_V\approx0.901\) |
| 0.01 | 0.010000 | 3.236 | 0.3233 | \(4B_0\approx3.547\), \(R_V\approx3.005\) |

At larger targets the separation grows rapidly (best observed \(j-K\approx9.89,36.05,139.41,323.02\) at target fractions \(0.03,0.1,0.3,0.55\)). In all optimized profiles \(q=T_\phi-P_w<0\), so the radial projection term itself lies *above* the C1 value; the constrained solver did not enter I55's dangerous \(q>0\) window. This is evidence of a specific mechanism rather than a theorem: low-cost ways to create almost-Kähler nonintegrability also create enough inverse-weight anisotropy \(P_w\) that conformal transfer cannot compensate it, with \(V_w\) and the self-dual Weyl remainder recording the same obstruction in the two decompositions. The near-linear small-target ratios \((j-K)/(N/m_0)\approx 369,343,327,324\) suggest a positive first-order coercive modulus in this discretization, but the smallest target is still contaminated by the nonzero finite-degree biaxial baseline and constrained optimization error. A rigorous proof should target an inequality linking \(N\) to \(P_w-T_\phi\), \(V_w\), and the scalar residuals, not infer a constant from these values.



---

## Source step4_positive_q_and_recovered_volume.md

Original: [sources/Sessions/S1003A01/workspace/notes/step4_positive_q_and_recovered_volume.md](../sources/Sessions/S1003A01/workspace/notes/step4_positive_q_and_recovered_volume.md)

# Step 4 — Direct positive-q cells, inner-scale coercivity, and quantitative fixed-exterior loss

Session S1003A01, Step 4. Notation follows I54/I55 and `step3_coupled_compensation_and_route_reassessment.md`. The cell metric is

\[
G=e^{2\phi}\left\{\frac{dr^2}{F}+r^2(e^{2w}\sigma_1^2+e^{-2w}\sigma_2^2)+r^2F\sigma_3^2\right\},
\]

with \(r_0^2=\mu\), exact CH outer collar, and \(j=J/(2\pi^2)\). Define

\[
I_R=\frac14(\mu^{-2}-R^{-4}),\quad M_0=1+\frac2\mu,
\quad q=T_\phi-P_w,
\]

so I55 gives

\[
j=\frac{(M_0-q)^2}{4I_R}+R_X+R_Y+R_Z+R_V. \tag{1}
\]

This Step tested the previously unvisited signed sector \(q>0\), corrected the fixed-exterior stationarity argument at the free/fixed interface, and extracted the natural inner-scale inequality that now organizes the diagonal route.

## 1. Direct positive-q instrument

`workspace/scripts/cell_qsearch.py` minimizes \(j\) while constraining \(q=fM_0\). It uses the exact bolt/collar basis of `cell_opt.py` and reports all terms in (1). Three conformal initializations were compared:

- `inner`: a smooth bump in \(r/\sqrt\mu\) initially supported on \(2<r/\sqrt\mu<3\);
- `fixed`: a bump on a fixed physical annulus \(0.55<r<1.05\);
- `broad`: the lowest exact-collar Chebyshev mode.

Both signs of \(\phi\) and zero/nonzero low-mode triaxial seeds were used. After initialization, all variables are free, so these labels describe continuation basins, not a preserved support condition. Raw data are

- `workspace/data/cell_qsearch/main_mu01.jsonl` for \(\mu=.1\), degree 22, 650 Gauss nodes;
- `workspace/data/cell_qsearch_small/musmall.jsonl` for \(\mu=.03,.01\), degree 22, 750 nodes;
- the selected robust profiles are in `workspace/data/cell_qsearch/qsearch_best.csv`.

The direct Ricci integral and I55 square decomposition agree to at worst \(7.3\times10^{-11}\) over all runs, and usually \(10^{-13}\). The I54 `B0` value is inferred from its exact identity, so its machine-zero closure is bookkeeping, not an independent Weyl implementation.

### 1.1 The search actually enters the necessary signed sector

A subthreshold cell must satisfy I55 (8.4). Its positive lower endpoint is

\[
\delta_{\mu,R}=1+\frac2\mu\left(1-\sqrt{1-\mu^2/R^4}\right),
\]

which is approximately \(1.0063,1.0019,1.0006\) at \(R=2\), \(\mu=.1,.03,.01\). The smallest searched targets were \(q=1.05,6.77,20.1\), respectively, and hence all cross this necessary lower endpoint. The previous fixed-\(N\) runs never entered this regime; this one does.

No profile had \(j<4\), or even \(j<K\). The best robust records were:

| \(\mu\) | \(f=q/M_0\) | \(j\) | \(K\) | projection | \(R_X\) | \(R_Y\) | \(R_Z\) |
|---:|---:|---:|---:|---:|---:|---:|---:|
| .10 | .05 | 7.1723 | 4.4128 | 3.9825 | 1.0549 | .5347 | 1.6002 |
| .10 | .15 | 11.8396 | 4.4128 | 3.1882 | 3.8527 | 1.0230 | 3.7758 |
| .03 | .10 | 8.6603 | 4.1211 | 3.3381 | 2.0308 | .7062 | 2.5852 |
| .01 | .10 | 8.4084 | 4.0401 | 3.2725 | 1.9414 | .6719 | 2.5226 |
| .01 | .35 | 16.0987 | 4.0401 | 1.7070 | 9.5245 | .7138 | 4.1534 |

These minima are numerical competitors, not certified constrained minima. The augmented-Lagrangian stopping check enforces the q constraint but does not certify the full KKT system or rule out negative Hessian modes.

### 1.2 What mechanism the data do and do not test

The cheapest profiles return to \(w=0\), so they are in the already-proved conformally Kähler class. In seeded runs the final amplitudes are commonly \(10^{-4}\)–\(10^{-3}\), with tiny \(P_w,N,R_V\). Thus the computation resolves the conformal payment in the signed dangerous sector but does **not** exclude an unknown finite-amplitude \(w\ne0\) escape. The unsearched half \(M_0<q<2M_0\) must also remain open: the projection is symmetric around \(q=M_0\), but the residual system is not.

For the low-cost branch, forcing \(q\) positive lowers the projection term exactly as intended, but the payment moves into \(R_X\) and \(R_Z\), with \(R_Y\) becoming significant nearer \(M=0\). At \(\mu=.01,f=.1\), the formal projection saves \(K-3.2725=.7676\), while the residuals total \(5.1359\), giving \(j=8.4084\). At \(f=1\), the projection nearly vanishes but the total cost is about \(35.45\) in the lowest recorded basin. This is the numerical realization of I55's zero-moment warning: killing \(M\) does not kill the metric residual.

A second, high-cost continuation basin was found from the fixed physical bump. At fixed \(f\), its cost scales approximately as \(j\sim C_f/\mu\), and \(\phi_{\max}\sim C_f'/\sqrt\mu\); for example at \(f=.1\), \(\mu j\) is about 10.84 at \(\mu=.03\) and 10.42 at \(\mu=.01\). The low-cost broad branch remains \(O(1)\). Because support is not preserved by the optimization, this is evidence for two basins rather than a theorem separating scales. At high \(q\), many runs approach the soft positivity floor for \(F\), so only records with `F_min_scaled>0.05` were used in the robust summary.

The independent SU(2)_L relative-orientation computation in peer Session S1003A02 provides complementary evidence outside this diagonal fixed-eigenframe parameterization. Its rotated Bianchi-IX cells show a positive first-order orientation penalty: at \(x_0=.003\), the slope \((P/(8\pi^2)-1)/x_0\) rises from 5.90 at aligned angle to 15.20 at \(\pi/2\), with both \(4\Delta W^+\) and \(\Delta S/12\) positive. Files are `Sessions/S1003A02/workspace/scripts/o11_rotated_cell.py` and `.../data/o11rot/summary.csv`. Some nonzero-angle optimizations ended at iteration/line-search limits, so these remain competitor values, but they show that rotating the Burns and CH Weyl axes does not expose the desired same-metric negative cost; the misalignment is paid at the same first order as the exceptional scale.

## 2. Inner-scale limit and the next proof object

Put \(r=\sqrt\mu x\), and suppose a low-cost branch has

\[
F_\mu(\sqrt\mu x)\to\mathcal F(x),\quad
w_\mu(\sqrt\mu x)\to W(x),\quad
\phi_\mu(\sqrt\mu x)\to\Phi(x),
\]

with bolt conditions

\[
\mathcal F(1)=0,\quad \dot{\mathcal F}(1)=2,\quad
W(1)=\dot W(1)=0,
\]

and terminal behavior \((\mathcal F,W,\Phi)\to(1,0,0)\) as \(x\to\infty\). If

\[
\vartheta=\lim_{\mu\downarrow0}\mu q,
\]

then \(q=fM_0\) corresponds to \(\vartheta=2f\). The signed moment becomes

\[
\vartheta=\widehat T-\widehat P,
\]

\[
\widehat T=2\int_1^\infty\frac{\mathcal F\dot\Phi^2}{x}\,dx,
\]

\[
\widehat P=\int_1^\infty\left[
\frac{2\mathcal F\dot W^2}{x}
+\frac{8(\cosh2W-1)}{x^3}
+\frac{8\sinh^2(2W)}{x^3\mathcal F}\right]dx.
\]

The rescaled radial identity is

\[
\int_1^\infty\frac{\widehat X}{x}\,dx=2-\vartheta,
\]

and the limiting energy has the exact formal structure

\[
\mathcal J_\infty=(2-\vartheta)^2+\widehat{\mathscr R}, \tag{2}
\]

where

\[
\begin{aligned}
\widehat{\mathscr R}={}&\frac14\int_1^\infty x^3
\left(\widehat X-\frac{4(2-\vartheta)}{x^4}\right)^2dx
+\frac14\int_1^\infty x^3\widehat Y^2dx\\
&+\frac12\int_1^\infty x^3\widehat Z^2dx
+2\int_1^\infty x^3\widehat V^2dx.
\end{aligned}
\]

The scale-correct diagonal theorem to prove is therefore

\[
\boxed{\widehat{\mathscr R}\ge \vartheta(4-\vartheta),
\qquad 0<\vartheta<4,} \tag{3}
\]

which is equivalent to \(\mathcal J_\infty\ge4\). It is sharp at \(\vartheta=0\): \(\mathcal F=1-x^{-2},W=\Phi=0\) gives \(\widehat X=8x^{-4}\), all other residuals zero, and energy 4. The present data cover only \(0<\vartheta\le2\), predominantly with \(W=0\); the genuinely new theorem is (3) for finite-amplitude \(W\ne0\) over the full interval.

A useful logarithmic formulation takes \(s=\log x\), \(A=x\dot\Phi\), \(B=x\dot W\). The exact \(Z,V\) identities become a coupled Riccati/transport system schematically

\[
\partial_sA-2A-A^2=-B^2+\frac{4\sinh^2(2W)}{\mathcal F^2}
-\frac{x^2\widehat Z}{2\mathcal F},
\]

\[
x^2\widehat V=-\mathcal F\partial_sB-(\partial_s\mathcal F)B
-2\mathcal F B-2\mathcal F AB
+\frac{4\sinh4W}{\mathcal F}-4\sinh2W.
\]

This identifies the analytic content missing from a moment-only argument: the \(e^{-2s}\)-weighted gain in \(\widehat T-\widehat P\) must be paid through the weighted squares of the radial Riccati and anisotropy transport residuals, together with \(\widehat X,\widehat Y\). Proving (3), rather than bounding \(T_\phi\) or \(P_w\) separately, is the strongest next diagonal route.

## 3. Fixed exterior: what minimality gives, and the interface defect

Let \(\mathcal A\) be smooth cell metrics equal to CH on a fixed open outer collar and let \(g_i\in\mathcal A\) be a true minimizing sequence, \(J(g_i)\to J_*\). Suppose marked, single-sheeted \(C^2\) convergence holds on compact subsets of a regular free-interior region. If \(h\) is compactly supported there, transport it to \(h_i\). Then, for fixed small \(t\),

\[
J(g_i+t h_i)-J(g_i)\ge J_*-J(g_i)=o(1).
\]

The local difference converges under \(C^2\), so

\[
J_K(g_\infty+t h)\ge J_K(g_\infty).
\]

Using both signs yields local stationarity and stability. This avoids passing a higher-order regularizer's equation. It is valid only away from singular, multi-sheeted, and fixed-collar regions and does not itself supply regularity beyond the local variational equation.

The previous Step overextended this to the collar interface. Compactly supported free-interior variations give

\[
(\Delta_++1)(s+4)=0
\]

and, after establishing \(s=-4\), an elliptic system for \(E=\operatorname{Ric}+g\). But \(C^2\) matching to CH gives only \(E|_\Sigma=0\). Extending \(E\) by zero across the fixed/free interface produces distributionally a possible term

\[
(\Delta E-AE)_{\rm dist}
=\pm(\nabla_\nu E)_{\rm free}\,\delta_\Sigma. \tag{4}
\]

Allowed variations vanish on the fixed open collar and do not detect this interface stress. Thus local stationarity does not prove the tensor equation across \(\Sigma\), and Dirichlet data alone do not imply \(E=0\).

Sufficient repairs include: fixed-coordinate \(C^3\) convergence across the interface; a global weak equation with no interface measure; an actual CH open set lying inside the free PDE region; or a separate coercive Dirichlet theorem for the trace-free Einstein operator. Once (4) vanishes, unique continuation gives \(E=0\); Einstein analyticity and the retained CH germ then imply that the regular base is locally CH. This is the exact missing input before the developing-map rigidity of Step 3 can be used.

## 4. Quantitative recovered-volume theorem

Let \(D\) be the original CH ball of background volume \(d\), and define

\[
\mathcal F(g)=\frac{(s+3)^2}{3}+1+4|W^+|^2\ge0.
\]

On CH, \(\mathcal F=4\). The relative identity is

\[
J(g_i)-8\pi^2Q_{\rm cell}=\int_C\mathcal F(g_i)-4d. \tag{5}
\]

Suppose a single-sheeted marked region \(\mathcal R\subset D\) is recovered in \(C^2_{\rm loc}\) as the original CH background. On compact exhaustions of \(\mathcal R\), the integral tends to four times CH volume; nonnegativity controls everything omitted. Therefore

\[
\liminf_iJ(g_i)\ge8\pi^2Q_{\rm cell}-4v_{\rm miss},\qquad
v_{\rm miss}=d-\operatorname{Vol}_{\rm CH}(\mathcal R). \tag{6}
\]

In particular,

\[
\boxed{\limsup_iJ(g_i)\le8\pi^2Q_{\rm cell}-\delta
\quad\Longrightarrow\quad v_{\rm miss}\ge\delta/4.} \tag{7}
\]

For \(j\le4-\epsilon\) in a one-blowup cell, \(\delta=2\pi^2\epsilon\), so \(v_{\rm miss}\ge\pi^2\epsilon/2\). A finite set of concentration points has zero CH volume and cannot itself create a strict deficit. A subthreshold degeneration must lose positive background volume, fail single-valued regular recovery, or leave the orbifold framework; bubbles and collapse matter only insofar as they cause such loss.

Equation (6) is conditional on constructing the recovery regions. It does not identify missing CH background volume with actual replacement volume under \(g_i\), and no stronger coefficient follows merely from the pointwise bound \(\mathcal F\ge1\).

## 5. Locally symmetric extension and its scope

The developing-map argument extends from CH to any complete locally real-hyperbolic base under the same hypotheses. If \(X=\mathbb H^4_{-1/3}/\Gamma\) is closed smooth, \(U=X\setminus\cup D_a^\circ\) is connected, and a connected effective boundaryless complete locally real-hyperbolic orbifold \(\mathcal O=\mathbb H^4_{-1/3}/\Gamma'\) contains \(U\) by a smooth injective local isometry, then \(\Gamma<\Gamma'\). Any extra deck transformation would send the connected unbounded lift of \(U\) disjointly into a bounded lifted ball, impossible. Hence \(\Gamma'=\Gamma\), so \(\mathcal O=X\) smoothly.

This does not apply to a merely negative Einstein, \(W^+\)-flat base: in four dimensions \(W^+=0\) fixes only one curvature-operator block; real hyperbolicity also requires \(W^-=0\). If an Einstein regular base contains a genuine real-hyperbolic open set and the interface stress has been removed, analyticity propagates the full constant-curvature tensor and the argument can then start. Otherwise half-conformal flatness is not a substitute for a real-hyperbolic developing structure.

Likewise, the O11 developing-map argument does not directly exclude a general non-Kähler Einstein orbifold with Ricci-flat ALE fillers. It first requires the local CH conclusion, which is precisely what (4) obstructs at present. Once single-sheeted CH recovery covers all but zero background volume, however, the threshold follows already from (6), regardless of how the ALE tree distributes topology. This distinction is important for both O11 and the peer O10 degeneration programme.

## 6. Route assessment

The Step-3 handoff was scientifically useful: direct q targeting revealed a low-cost positive-q basin and identified its payments. But it also showed that continuing the same optimizer will not settle C1: the best profiles collapse back to the proved \(w=0\) class, while high-q runs approach the positivity floor. The finite-amplitude diagonal unknown should now be attacked through the inner-limit inequality (3), preferably by deriving a weighted Hardy/Riccati estimate and using numerical searches only to test its sharp sublemmas or find a finite-amplitude counterprofile. The peer rotated-cell result independently shows that the most natural non-diagonal relative-orientation modulus is penalized at first order, strengthening the case for a lower mechanism without proving all-cell optimality.

The compactness route is now quantitatively clearer. It need not charge each bubble. It must either construct CH recovery regions whose missed volume tends to zero, yielding the threshold from (6), or explain a positive-volume loss/multi-sheet/collapse mechanism. Local comparison minimality supplies the free-interior equation, but removing the interface stress (4) is a separate analytic theorem and should not be hidden inside the word stationarity.



---

## Source step5_slice_charge_and_zero_flux.md

Original: [sources/Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md](../sources/Sessions/S1003A01/workspace/notes/step5_slice_charge_and_zero_flux.md)

# Step 5 — The slice charge of Bianchi-IX cells, the zero-flux certificate, and the inner AE threshold

Session S1003A01, Step 5 (Agent2, Explore). Conventions: I54/I55 cell normalization (CH collar \(F_{CH}=1+r^2/6\), \(\mathrm{Ric}_{CH}=-g\), \(s_{CH}=-4\)); \(|W^+|^2\) is the LeBrun/operator norm (CH value \(2/3\)); orientation is the complex one, \(\tau(\mathcal O(-1))=-1\). Cell density
\[
\mathfrak F=\frac{(s+3)^2}{3}+1+4|W^+|^2\ \ (\mathfrak F_{CH}=4),\qquad |\mathrm{Ric}+g|^2=\mathfrak F-8\pi^2(2e+3p)
\]
pointwise, where \(\chi=\int e\), \(\tau=\int p\) (pure Chern–Weil algebra; it gives I54's \(J-8\pi^2q=\int\mathfrak F-4d\)).

Scripts: `scripts/bianchi_transgression.py` (Cartan curvature, Euler + Pontryagin forms, exact antiderivative), `transgression_values.py`, `transgression_cell.py`, `transgression_sign.py`, `transgression_triaxial.py`, `transgression_structure.py`, `transgression_closed_form_check.py`, `profile_charge.py`, `plot_slice_charge.py`, `kahler_flux_check.py`. Data: `data/transgression/` (`G_formula.txt`, `triaxial_Qstar.txt`, `profile_charge_lines.jsonl`, `zero_flux_summary.json`). Figure: `figures/slice_charge_profiles.png`.

## 1. Exact slice charge for every diagonal Bianchi-IX metric

Let \(g=dt^2+a^2\sigma_1^2+b^2\sigma_2^2+c^2\sigma_3^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\), ' = d/dt. Put \(e^{2w}=a/b\), \(z=c/\sqrt{ab}\),
\[
p_+=\frac{b a'-c+(a^2-b^2)/c}{\sqrt{ab}},\qquad p_-=\frac{a b'-c-(a^2-b^2)/c}{\sqrt{ab}} .
\]
**Theorem A (slice charge).** For slices \(t_1<t_2\),
\(8\pi^2\int_{t_1<t<t_2}(2e+3p)\,dV=\mathcal T(t_2)-\mathcal T(t_1)\), where
\[
\boxed{\frac{\mathcal T}{8\pi^2}=Y^2+\Pi,\quad
Y=c'-2\cosh2w+z^2+\tfrac12p_+p_-,\quad
\Pi=e^{2w}p_+^2+e^{-2w}p_-^2-\tfrac14(p_+p_-)^2 .}
\]
\(\mathcal T\) depends only on first-order slice data and is scale invariant.

Verification: the antiderivative was obtained symbolically from the Cartan curvature and checked identically (`check = 0`); the closed form agrees with it to \(9\times10^{-14}\) on \(10^5\) random slices. Values: flat round slice \(0\); smooth \(\mathcal O(-1)\) bolt \(8\pi^2\) (so \(\mathcal T(\text{bolt})-\mathcal T(\text{flat})=8\pi^2\) = the \(2\chi+3\tau=-1\) jump); the opposite orientation gives \(-40\pi^2\) (\(\mathcal O(+1)\), \(2\chi+3\tau=5\)); CH collar \(\mathcal T=2\pi^2R^4=4d\) exactly; Taub–NUT/ALF slices (\(c\to\)const, \(a'=b'=1\)) give \(32\pi^2\), matching \(\chi=1,\ \tau\)-density \(=\tfrac23\) of the self-dual Taub–NUT; flat-cone Berger slices \(c=t/k\) give \(8\pi^2(k-1)^2(4k^2+5k+2)/k^4\). As an independent test against the Ricci code: for every conformally Kähler numerical cell (\(w=0\)), \(d\mathcal T/dr+|\mathrm{Ric}+g|^2dV/dr=[(s_G+3)^2/3+1]dV_G/dr+(s_K^2/6)dV_K/dr\) holds with finite-difference relative error \(\le1.2\times10^{-3}\) (typically \(10^{-5}\)).

Meaning of the pieces. \(p_+=p_-=0\) iff the slice is Kähler for \(\omega=c\,dt\wedge\sigma_3+ab\,\sigma_1\wedge\sigma_2\) (\(p_++p_-=2\delta\), \(\delta\) the closure defect \((ab)'/2\sqrt{ab}-z\); \(p_+-p_-=2\kappa\), \(\kappa\) the integrability defect). For U(2)-Kähler slices, \(Y=-A\) where the Ricci form is \(\rho=d(A\sigma_3)\) (`kahler_flux_check.py`: \(A/Y=-1\) identically). Thus **\(\mathcal T=8\pi^2(\text{Ricci-form flux})^2+8\pi^2\cdot(\text{Kähler defect})\)**: the Chern–Weil charge of a Kähler slice is the square of its \(c_1\)-flux, which is the \(c_1^2=2\chi+3\tau\) transgression. \(\Pi\ge0\) whenever \(|p_+p_-|\le8\) (AM–GM); \(\mathcal T\) is unbounded below only for strongly non-Kähler slices (\(|p_+p_-|>8\)).

## 2. Localized identities

For any slice \(\Sigma_\rho\) of a cell \(C\) with exact CH collar:
\[
\int_{\rm in}|\mathrm{Ric}+g|^2=8\pi^2+\int_{\rm in}\mathfrak F-\mathcal T(\rho),\qquad
\int_{\rm out}|\mathrm{Ric}+g|^2=\int_{\rm out}\mathfrak F-4d+\mathcal T(\rho).
\]
Since \(\mathfrak F\ge1\), every slice certifies
\[
J-8\pi^2\ \ge\ \mathrm{Vol}_G(\mathrm{in}_\rho)-\mathcal T(\rho)\quad\text{and more sharply}\quad J-8\pi^2\ge\int_{\rm in}\mathfrak F-\mathcal T(\rho). \tag{2.1}
\]
(The second form is trivial if \(\int_{\rm in}\mathfrak F\) is unknown; the content is that \(\mathcal T\) is an explicit function of slice data.)

## 3. The zero-flux certificate

\(Y(\text{bolt})=-1\) (bolt: \(z\to0,\ c'\to1,\ w\to0,\ p_\pm\to0\)) and \(Y(\text{collar})=R^2/2>0\). By continuity there is a slice \(t_*\) with \(Y(t_*)=0\), at which \(\mathcal T=8\pi^2\Pi\).

**Theorem C (zero-flux threshold).** For every \(C^2\) diagonal one-bolt cell in which the collapsing bolt circle is the \(\sigma_3\) slot of the CH Kähler fibre (this is the I54/I55 triaxial conformal class, any \(w,\phi\)), and every zero \(t_*\) of \(Y\),
\[
J\ \ge\ 8\pi^2+\int_{\mathrm{in}(t_*)}\mathfrak F\,dV-8\pi^2\Pi(t_*)\ \ge\ 8\pi^2+\mathrm{Vol}_G(\mathrm{in}(t_*))-8\pi^2\Pi(t_*).
\]
Corollaries. (i) If \(G\) is itself Kähler (\(\Pi\equiv0\)), \(J\ge8\pi^2+\mathrm{Vol}(\mathrm{in}(t_*))>8\pi^2\) — an elementary one-line threshold (weaker than I54 Theorem 1's \(K\), but local). For the U(2) Kähler family \(Y=-\mu/r^2+r^2/2+\dots\), zero at \(r_*\approx(2\mu)^{1/4}\). (ii) A subthreshold cell must have \(8\pi^2\Pi(t_*)>\int_{\rm in}\mathfrak F\ge \mathrm{Vol}\) at **every** zero of the flux: each zero-flux slice must be non-Kähler by an amount exceeding the interior energy.

Numerics (122 cells: 108 positive-q runs of Step 4 and 14 near-optimal sweep1 runs; `zero_flux_summary.json`). Every cell except one unconverged \(\mu=.6,R=.8\) run (\(j\approx8\times10^4\), zero in the excluded endpoint layer) has zero-flux slices; at the best zero, \(8\pi^2\Pi/\int_{\rm in}\mathfrak F\le0.58\), so Theorem C certifies \(J\ge8\pi^2\) for all of them. The **first** zero does not always suffice (2 high-cost oscillating profiles have ratio 1.03, 1.02 there). Near-optimal cells place \(\mathcal T\approx0\) (\(\le2\times10^{-4}\cdot8\pi^2\)) at \(r\approx(2\mu)^{1/4}\) even at \(\mu=0.1\): they split into an inner piece paying the whole \(8\pi^2\) and a CH-like outer piece.

**Conjecture Z (diagonal, aligned slot).** Every diagonal filling of an \(\mathcal O(-1)\) bolt has a zero-flux slice with \(8\pi^2\Pi(t_*)\le\int_{\rm in}\mathfrak F\). This localizes and implies the diagonal-class cell conjecture \(j\ge4\) for all \(\mu,R\) (not C1). Its content is a boundary-to-interior inequality: Kähler defect of the slice controlled by interior \(4|W^+|^2+(s+3)^2/3+1\). Candidate mechanism: for \(G=e^{2\phi}K\), \(\delta=\sqrt F\,r\phi'\) and \(\kappa=\kappa_K\); interior \((s+3)^2\) controls \(\Delta\phi\) (Hardy type, \(\phi=0\) at the bolt), interior \(W^+\) controls \(\kappa\).

## 4. Inner AE threshold in the diagonal class (Step-4 (3) closed)

Rescale \(r=\sqrt\mu x\). On \([1,X]\), the pure-Ricci form of §2 is exact:
\(\int_{1}^{X}|\mathrm{Ric}|^2dV=8\pi^2+\int_1^X(\hat s^2/3+4|\hat W^+|^2)dV-\mathcal T(X)\).
If the profile has finite \(\int|\mathrm{Rm}|^2\) and terminal limits \((\mathcal F,W,\Phi)\to(1,0,\Phi_\infty)\), then \(\mathcal T(X_k)\to0\) along a sequence: \(a''/a,b''/b,c''/c\) are sectional curvatures, so \(d(a',b',c')/d\log t\in L^2(d\log t)\); the terminal values force the averages of \(a',b',c'\) on \([X,2X]\) to 1, hence slice data \(\to\) flat round and \(\mathcal T\to0\). Therefore
\[
\mathcal J_\infty=4+\frac1{2\pi^2}\int(\hat s^2/3+4|\hat W^+|^2)\,dV\ \ge4,
\]
i.e. \(\widehat{\mathscr R}-\vartheta(4-\vartheta)=\frac1{2\pi^2}\int(\hat s^2/3+4|\hat W^+|^2)\ge0\) for all finite-amplitude \(W\) and all \(\vartheta\). This is the manuscript's `webvar:ae-cost` (\(P=8\pi^2b_2+4W^++S/12\)) realized with an explicit end term. If instead the end is ALF (Hopf fibre of bounded length), \(\mathcal T_{\rm end}=32\pi^2\) and the core identity reads \(\int|\mathrm{Ric}|^2=-24\pi^2+\int(\hat s^2/3+4|\hat W^+|^2)\): collapse of the fibre moves four charges of transgression across the neck, the explicit form of the "topology distributed across levels" phenomenon in this class. With a cell (fixed collar), the threshold as \(\mu\to0\) needs only a neck slice with \(\mathcal T\le o(1)\); no AE decay of the limit is needed, since (2.1) is exact at finite \(\mu\).

## 5. Scope, and the peer correction (message #746)

All of §3 assumes the bolt circle and the CH Kähler fibre occupy the same slot (\(\sigma_3\)). S1003A02's corrected fixed-slot computation finds that the relative orientation \(\zeta\perp\omega_{CH}\) has **zero first-order cost** (\(P/8\pi^2-1\approx0.044x_0\), margin only \(O(x_0^2)\), with \(4\Delta W^+/x_0\approx2(3\cos^2\theta-1)\), \(\Delta S/12x_0\approx2\)). Our diagonal searches (Steps 2–4) are entirely in the aligned slot \(\theta=0\), the most expensive orientation; they did not test the dangerous direction. In a perpendicular-slot diagonal cell (bolt collapsing \(\sigma_1\), CH fibre \(\sigma_3\)), \(\mathcal T(\text{bolt})=8\pi^2\) still (cyclic symmetry), but \(Y\) is singular at the bolt (\(e^{2w}=a/b\to0\)), so the zero-flux IVT is unavailable: **the zero-flux certificate is precisely a \(c_1(\omega_{CH})\)-flux argument and is evaded by the orientation that is first-order free.** The general certificate (2.1), \(J-8\pi^2\ge\mathrm{Vol}(\mathrm{in}_\rho)-\mathcal T(\rho)\), still applies to any diagonal slot assignment and should be evaluated on the peer's \(\zeta\perp\omega\) profiles (`Sessions/S1003A02/workspace/scripts/o11_perp_cell.py`).

Non-symmetric extension (route). For an arbitrary cell and separating hypersurface \(\Sigma\), \(J\ge8\pi^2+\int_{\rm in}\mathfrak F-\mathcal T(\Sigma)\) with \(\mathcal T\) the Chern–Gauss–Bonnet boundary term plus the Chern–Simons term of \(2\chi+3\tau\). In the Kähler case \(\mathcal T\) is the squared \(c_1\)-flux; for general metrics the Seiberg–Witten curvature \(iF_A/2\pi\) represents \(c_1(L)\) for every metric, suggesting a flux-square transgression with an actual-field substitute for \(\rho\). Whether the \(\zeta\perp\omega\) direction makes the monopole flux and the CH Ricci flux decouple is the natural test.

## 6. What this changes

- Step-4 inner inequality (3): proved in the diagonal class, with the end term made explicit (flat 0, ALF \(32\pi^2\)).
- Diagonal aligned-slot cell conjecture reduced to Conjecture Z (a boundary Kähler-defect vs interior energy inequality), numerically certified on all 120 analyzed cells with ratio \(\le0.58\).
- The decisive open direction for O11 is now the perpendicular orientation \(\zeta\perp\omega_{CH}\) at finite \(x_0\sim0.03\)–\(0.3\), where both first-order terms cancel and our flux mechanism is absent. A negative cell must live there (or outside SU(2)).



---

## Source step6_perpendicular_dual_cost_and_relative_calibration.md

Original: [sources/Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md](../sources/Sessions/S1003A01/workspace/notes/step6_perpendicular_dual_cost_and_relative_calibration.md)

# Step 6 — Perpendicular O11 cells: distinct P/J costs, bolt-adapted transgression, and a relative calibration

Session S1003A01, Step 6, Execute. The peer correction in S1003A02 Step 8 invalidated the earlier orientation-penalty interpretation: a fixed-slot blow-up with Burns direction perpendicular to the CH Kähler form cancels the order-\(x_0\) trace-free Ricci cost. This step reconstructs that branch independently, separates the trace-free cost from the Einstein cell cost, and joins it to the slice transgression of Step 5.

## 1. Two costs in the peer normalization

The peer code uses the complex-hyperbolic normalization
\[
\operatorname{Ric}_{g_{CH}}=-6g_{CH},\qquad s_{CH}=-24.
\]
Put
\[
P(g)=\int |\operatorname{Ric}^{\circ}_g|^2dV_g,
\qquad J_6(g)=\int |\operatorname{Ric}_g+6g|^2dV_g.
\]
The orthogonal splitting of Ricci gives the exact relation
\[
\boxed{J_6=P+\frac14\int(s+24)^2dV.}\tag{1.1}
\]
If \(\widetilde g=6g\), then \(J_6(g)=J_1(\widetilde g)\), so this is exactly the I54/I55 cell cost after rescaling to \(\operatorname{Ric}=-g\). The fixed-parameter expression \(J_6\) is not itself invariant under arbitrary scaling with 6 held fixed; it is covariant under simultaneous rescaling of the Einstein constant.

This distinction is consequential. A fixed cell with \(J_6<8\pi^2\) enters the direct I54 finite-cell transfer. A profile with only \(P<8\pi^2\) can still matter through the inherited global \(\inf P\) reduction, but its scalar/conformal selection has to be handled separately. Therefore `scripts/perp_dual_cost.py` optimizes and records both costs.

## 2. Fixed-slot perpendicular ansatz and regular bolt-adapted axes

The implemented metric is
\[
g=\frac{dx^2}{4G(x)}+F(x)\sigma_1^2+x\sigma_2^2+xe^{w(x)}\sigma_3^2,
\quad x_0\le x\le X=1.\tag{2.1}
\]
The bolt collapses in the old \(\sigma_1\)-slot; the CH fibre is old \(\sigma_3\). The smooth bolt mode has \(w=O((x-x_0)^2)=O(t^4)\); this is the peer option `wpow=2`. The earlier statement that the transgression variable is singular in the perpendicular branch was coordinate-dependent. Use the orientation-preserving cyclic relabeling
\[
(a,b,c)=(\sqrt{x},\sqrt{xe^w},\sqrt F),
\qquad dt=\frac{dx}{2\sqrt G},\tag{2.2}
\]
so that \(c\) is again the collapsing distinguished slot. Then the Step-5 decomposition is regular and
\[
Y_{bolt}=-1,\quad \Pi_{bolt}=0,\quad \mathcal T_{bolt}=8\pi^2.\tag{2.3}
\]
On the exact CH collar \(F=x, G=x(1+x), e^w=1+x\), direct substitution gives
\[
p_+=0,\quad p_-=3x(1+x)^{-1/4},\quad Y=0,\quad
\Pi=9x^2,\quad \frac{\mathcal T}{8\pi^2}=9x^2.\tag{2.4}
\]
Writing the I54 radius as \(R^2=6x\), this is \(\Pi=R^4/4\), exactly the Strategist substitution. At the script's \(X=1\), the collar charge is \(9\cdot8\pi^2\); after rescaling to Ric=-g it is again \(4d\). Thus charge has not disappeared; it transfers from the scalar flux \(Y\) to the Kähler-defect term \(\Pi\). Choosing the bolt's own flux therefore does not restore an obligatory zero-charge crossing.

`perp_dual_cost.py` independently evaluates this transgression on the peer profile. For the peer's smooth \(x_0=.01\) P-optimized profile it finds
\[
P/(8\pi^2)=1.001996388,
\quad J/(8\pi^2)=1.002453337,
\quad (J-P)/(8\pi^2)=4.56948\times10^{-4}.\tag{2.5}
\]
The charge dips to \(\mathcal T/(8\pi^2)=0.0515617\) near \(x=0.06095\), then grows entirely through \(\Pi\) to 9 at the collar. The same profile has \(Y\to0,\Pi\to9\) at the collar to numerical precision. This verifies the axis conversion and the two-cost distinction on an actual near-minimizer. It does not prove positivity of the infimum.

## 3. New dual optimization results

`scripts/run_perp_dual_sweep.py` reoptimizes the same smooth fixed-slot ansatz separately for \(P\) and \(J\), at degrees 6 and 8, using 400–500 Gauss nodes. The final data are in `data/perp_dual/`; each record contains the full coefficients, independent scalar term, optimization termination, and bolt-adapted transgression profile. The sweep completed all sixteen degree/target cases; the canonical table is `data/perp_dual/summary.csv`.

The degree-8 results already returned were:

| \(x_0\) | target | \(P/8\pi^2\) | \(J/8\pi^2\) | scalar deviation | \(\min \mathcal T/8\pi^2\) |
|---:|:---:|---:|---:|---:|---:|
| .003 | P | 1.000121440 | 1.000198631 | 7.72e-5 | .01705 |
| .003 | J | 1.000121630 | 1.000130599 | 8.97e-6 | .01698 |
| .01 | P | 1.001936966 | 1.002381323 | 4.44e-4 | .05146 |
| .01 | J | 1.001855826 | 1.001939414 | 8.36e-5 | .05152 |
| .03 | P | 1.017890798 | 1.021006185 | 3.12e-3 | .11848 |
| .03 | J | 1.018432695 | 1.019029297 | 5.97e-4 | .12032 |
| .1 | P | 1.149762740 | 1.220934254 | 7.12e-2 | .21663 |
| .1 | J | 1.162214888 | 1.170416666 | 8.20e-3 | .22182 |

All returned competitors remain above both thresholds. Optimizing \(J\) does not merely repeat P optimization: it sharply reduces scalar deviation and changes the profile, e.g. at \(x_0=.01\), while leaving a positive margin. Conversely P optimization accepts a larger scalar deviation to reduce trace-free Ricci cost. These are upper bounds on class infima, not certified minimizers; some `success=true` records still have gradients of order 1e-4 because L-BFGS stopped on function reduction. Degree-10/12 continuation and two random restarts per degree were completed for \(x_0=.01\) in `scripts/perp_degrees.py`. The best J-target profile had \(J/(8\pi^2)=1.001895793\), \(P/(8\pi^2)=1.001831515\); the best P-target profile had \(P/(8\pi^2)=1.001866502\). These results remain above threshold and differ from the degree-8 values by at most \(4.4\times10^{-5}\) on the optimized target. Gradient norms remain \(10^{-4}\)–\(10^{-3}\), so this is useful stability evidence rather than a resolved infinite-dimensional minimum.

The values support the peer's vanishing first-order coefficient, but they do not yet determine whether the leading residual is \(c x_0^2\), \(x_0^2\log(1/x_0)\), or another second-order law. No subthreshold cell was found.

## 4. Chern–Simons connection variables

The bolt-adapted transgression has a more revealing symmetric form. Define
\[
u_1=e^{\varpi}p_+,
\quad u_2=e^{-\varpi}p_-,
\quad u_3=Y-\frac12p_+p_-,
\qquad e^{2\varpi}=a/b.\tag{4.1}
\]
Equivalently, cyclically in \((i,j,k)\),
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.\tag{4.2}
\]
Then the charge is the cubic Chern–Simons polynomial
\[
\boxed{C(u):=\frac{\mathcal T}{8\pi^2}
=u_1^2+u_2^2+u_3^2+u_1u_2u_3.}\tag{4.3}
\]
The endpoint states are
\[
u_{bolt}=(0,0,-1),\qquad u_{CH}=(0,3x,0).\tag{4.4}
\]
Thus the perpendicular cell transports charge from the \(u_3\)-axis to the \(u_2\)-axis through a nearly uncharged neck. This is a heteroclinic transfer problem rather than a scalar sign-crossing problem.

Set
\[
H_i=u_i+\frac12u_ju_k,
\qquad \lambda_i=\frac{a_ja_k}{a_i}.\tag{4.5}
\]
A direct invariant-curvature computation yields
\[
\frac{P}{8\pi^2}=\int\sum_i\frac{\lambda_i}{4}
\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt.\tag{4.6}
\]
Subtract the outgoing CH charge and use the relative calibration
\[
\Phi=C-u_2^2=u_1^2+u_3^2+u_1u_2u_3,
\quad \Phi_{bolt}=1,\ \Phi_{CH}=0.\tag{4.7}
\]
Completing squares gives
\[
\boxed{\begin{aligned}
\frac{P}{8\pi^2}-1=\int\Bigg[&
\frac{\lambda_1}{4}\left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}\left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}\left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}\Bigg]dt.
\end{aligned}}\tag{4.8}
\]
Everything except one cubic interaction is nonnegative. In particular,
\[
u_1u_2u_3\ge0\ \hbox{pointwise}\quad\Longrightarrow\quad
P\ge8\pi^2\quad\hbox{and}\quad J\ge8\pi^2.\tag{4.9}
\]
But the actual \(x_0=.01\) near-minimizer spends 85.5% of the sampled logarithmic interval in the negative chamber. `scripts/perp_spin_diagnostics.py` evaluates every term in (4.8) and independently matches the JAX curvature integral to \(1.4\times10^{-9}\):
\[
S_1=0.00113124,\quad S_2=0.000217907,\quad S_3=0.00207890,
\quad C_{cubic}=-0.00143166,\tag{4.10}
\]
so
\[
S_1+S_2+S_3+C_{cubic}=0.0019963874=P/(8\pi^2)-1.\tag{4.11}
\]
The negative cubic is not a negligible perturbation: it cancels about 42% of the three positive relative-flow squares. The positive threshold margin is a genuine coupled compensation, precisely of the kind sought in Steps 3–4.

For \(J\), the exact additional term is
\[
\frac{J-P}{8\pi^2}=\frac14\int abc\left[
\sum_i\left(\frac{\dot u_i}{a_i}+\frac{2H_i}{a_ja_k}\right)-12
\right]^2dt.\tag{4.12}
\]
This independently matches the scalar deviation in (2.5) to \(2.1\times10^{-12}\). Consequently a proof for J may succeed even if P admits a lower competitor; the two theorem targets must remain separate.

## 5. The analytic problem isolated by the computation

Equation (4.8) turns the full fixed-slot P threshold into the exact inequality
\[
\int(S_1+S_2+S_3)dt\ge
2\int\frac{(-u_1u_2u_3)_+}{\lambda_2}dt.\tag{5.1}
\]
Treating the outgoing \(u_2\) channel as background and \(\eta=(u_1,u_3)^T\), the transverse part is a 2×2 weighted Sturm/Hardy form. On an exact CH segment, after diagonalizing with \(v_\pm=u_1\pm u_3\), one obtains
\[
\mathcal Q_+=\int\left[\frac{x(1+x)}4(v_+')^2+
\frac{4+18x+15x^2}{16x(1+x)}v_+^2\right]dx,\tag{5.2}
\]
\[
\mathcal Q_-=\int\left[\frac{x(1+x)}4(v_-')^2+
\frac{4-18x+3x^2}{16x(1+x)}v_-^2\right]dx.\tag{5.3}
\]
Only the minus channel has a sign-changing potential. Pointwise positivity is therefore false and unnecessary; the natural theorem is positivity of the weighted Sturm operator with the bolt-to-collar endpoint behavior, or a positive matrix Riccati supersolution through the transition region.

An alternative Hamilton–Jacobi route searches for a scale-invariant calibration \(B(a,u)\) with \(B_{bolt}=1, B_{CH}=0\) and nonnegative residual after square completion. The zeroth approximation is \(B_0=C-u_2^2\). Its only residual is the cubic in (4.8). The correction
\[
\psi=-\frac{a_2^2}{a_1a_3}u_1u_3\tag{5.4}
\]
has an \(a_2\)-transport term that cancels the bare cubic. `scripts/perp_relative_checks.py` verifies the relative completion symbolically and computes the full residual for \(B_0+\psi\). That residual is not manifestly nonnegative—it contains mixed quadratic, cubic and quartic terms—so (5.4) is only a concrete first Hamilton–Jacobi correction, not a theorem. It must be localized or repaired at endpoints and combined with further terms if this route is to close.

For J, the scalar square (4.12) adds rank-one coercivity to the same Sturm system. This is likely the easier direct finite-cell theorem. For P, the result would be stronger and feed the global inf-P route directly.

## 6. Implementation cautions and present mathematical status

- The peer file's docstring mentions \(xe^{-w}\), but the implemented fixed-slot metric is exactly (2.1), \(\operatorname{diag}(F,x,xe^w)\). All calculations here follow the implementation.
- `wpow=1` gives only \(w=O(t^2)\) and is not the smooth charge-four transverse mode. All new main optimizations use `wpow=2`; the rough peer profiles are used only as initial coefficients before imposing the smooth envelope.
- The polynomial envelopes match the CH metric through the derivatives needed by the integrated curvature calculation, but are not literally equal on an open collar. A flat terminal cutoff gives smooth exact-collar approximants with convergent L2-curvature cost; the numerical profile itself should be called a matched cell rather than an exact-collar metric.
- The charge minima are sampled values, not interval-arithmetic bounds.
- Optimization gives explicit upper competitors and local stationarity evidence, not lower bounds for the infinite-dimensional class.
- No profile found here has \(P<8\pi^2\) or \(J<8\pi^2\). The all-profile perpendicular inequality, the aligned Conjecture Z, the full cell conjecture, and the unrestricted balanced coefficient remain open.

The research advance is a sharper mechanism. The perpendicular branch is now simultaneously (i) the only tested direction with order-x0 cancellation, (ii) a genuine P/J bifurcation, and (iii) an exact relative-calibration problem with one signed cubic. The immediate next mathematical work is to establish or disprove the matrix Hardy/Riccati inequality underlying (5.1), using the stored profiles to test proposed weights and the high-degree runs to resolve the second-order sign.



---

## Source step7_perpendicular_verification_and_endpoint_map.md

Original: [sources/Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md](../sources/Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md)

# Step 7 — Verification of the perpendicular relative calibration and the exact CH endpoint map

Session S1003A01, Step 7, Agent4, Execute. This note checks the most load-bearing formulas from Step 6, replaces the apparent sign-changing CH obstruction by an exact endpoint operator, verifies the smooth geometric status of the numerical cells, and records the scope correction forced by the peer's positive-curvature bulk test.

## 1. Exact Cartan derivation of the spin formulation

Use
\[
g=dt^2+a^2\sigma_1^2+b^2\sigma_2^2+c^2\sigma_3^2,
\qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
\qquad \int_{S^3}\sigma_1\sigma_2\sigma_3=2\pi^2.
\]
Put \(a_1=a,a_2=b,a_3=c\), cyclically define
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},
\quad H_i=u_i+\frac12u_ju_k,
\quad \lambda_i=\frac{a_ja_k}{a_i},
\]
and
\[
r_i=\frac{\dot u_i}{a_i},\qquad
v_i=\frac{2H_i}{a_ja_k},\qquad
C(u)=u_1^2+u_2^2+u_3^2+u_1u_2u_3.
\]

`scripts/perp_cartan_verify.py` derives the Levi--Civita connection and curvature directly from Cartan's equations, with independent first and second radial jets. SymPy reduces the following identities exactly to zero:
\[
|\operatorname{Ric}^{\circ}|^2=\sum_i(r_i-v_i)^2,
\qquad
s=-2\sum_i(r_i+v_i),                                      \tag{1.1}
\]
\[
\dot C=2\sum_iH_i\dot u_i=abc\sum_i r_iv_i,                \tag{1.2}
\]
\[
\frac{abc}{4}|\operatorname{Ric}^{\circ}|^2
=\sum_i\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2.           \tag{1.3}
\]
Since the orbit volume is \(2\pi^2abc\,dt\),
\[
\frac{P}{8\pi^2}=\int\sum_i\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt.         \tag{1.4}
\]
Thus the normalization and curvature-to-\(u\) formulas no longer depend only on agreement with a numerical coordinate-curvature implementation.

For
\[
\Phi=C-u_2^2=u_1^2+u_3^2+u_1u_2u_3,
\]
the purely algebraic checker `scripts/perp_relative_checks.py` verifies
\[
\boxed{\begin{aligned}
\frac{P}{8\pi^2}-1=\int\Big[&
\frac{\lambda_1}{4}\left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}\left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}\left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}\Big]dt .
\end{aligned}}                                                \tag{1.5}
\]
The cubic has the **plus** sign shown here. It is a signed contribution. Replacing it by its negative part gives only a stronger sufficient inequality and loses favorable regions.

In the fixed perpendicular slot,
\[
(a,b,c)=(\sqrt x,\sqrt{xe^w},\sqrt F),
\]
and the endpoint states are
\[
u_{\rm bolt}=(0,0,-1),\qquad u_{\rm CH}=(0,3x,0).          \tag{1.6}
\]
Hence \(\Phi\) drops from 1 to 0 even though the total charge \(C\) grows to \(9x^2\) on CH.

## 2. Exact-CH quadratic forms and positive zero modes

On CH,
\[
a=c=\sqrt x,\quad b=\sqrt{x(1+x)},\quad
\lambda_1=\lambda_3=\sqrt{x(1+x)},\quad
\lambda_2=\sqrt{\frac{x}{1+x}},\quad dt=\frac{dx}{2\sqrt{x(1+x)}}.
\]
For transverse perturbations \(\xi=\delta u_1\), \(\zeta=\delta u_3\), let \(v_\pm=\xi\pm\zeta\). The quadratic CH part of (1.5), after one integration by parts, is
\[
\mathcal A_{CH}^{(2)}=Q_+[v_+]+Q_-[v_-]
 +[\beta_+v_+^2+\beta_-v_-^2]_{\rho}^{1},                    \tag{2.1}
\]
where
\[
p=\frac{x(1+x)}4,\qquad \beta_\pm=\frac{2\pm3x}{8},
\]
\[
Q_\pm[v]=\int_\rho^1\{p(v')^2+V_\pm v^2\}\,dx,             \tag{2.2}
\]
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)}.                              \tag{2.3}
\]
The signed cubic in (1.5) contributes
\[
3\xi\zeta\,dx=\frac34(v_+^2-v_-^2)\,dx,                     \tag{2.4}
\]
so it is already fully included in (2.1)--(2.3).

`scripts/perp_ground_state_check.py` verifies the exact positive zero modes
\[
f_+(x)=x\sqrt{1+x},\qquad
f_-(x)=\frac{x}{(1+x)^{5/2}},                                 \tag{2.5}
\]
\[
-(pf_\pm')'+V_\pm f_\pm=0,\qquad
p\frac{f_\pm'}{f_\pm}=\beta_\pm.                             \tag{2.6}
\]
The rational Riccati forms of both identities were separately checked in Lean; see `proofs/PerpGroundState.lean` and dependency certificate `proofs/perp-ground-state-check.json`. The named minus theorem depends only on `propext`, `Classical.choice`, and `Quot.sound` in the configured Mathlib project.

For every smooth \(v\),
\[
\boxed{Q_\pm[v]=\int_\rho^1pf_\pm^2
 \left((v/f_\pm)'\right)^2dx+[\beta_\pm v^2]_\rho^1.}        \tag{2.7}
\]
Therefore the sign-changing \(V_-\) does not create a negative compactly supported bulk mode on exact CH. With \(v(1)=0\), however, the lower boundary flux remains.

## 3. Sharp CH Dirichlet-to-Neumann map

Let
\[
R_\pm(\rho)=\int_\rho^1\frac{dx}{p f_\pm^2}.
\]
For fixed \(v(\rho)=V\), \(v(1)=0\), weighted Cauchy--Schwarz in (2.7) is sharp and gives
\[
Q_\pm[v]\ge \kappa_\pm(\rho)V^2,
\qquad
\kappa_\pm=\frac1{f_\pm(\rho)^2R_\pm(\rho)}-\beta_\pm(\rho).\tag{3.1}
\]
The extremizer is
\[
v_{\pm,*}(x)=V\frac{f_\pm(x)}{f_\pm(\rho)}
 \frac{R_\pm(x)}{R_\pm(\rho)},\qquad
R_\pm(x)=\int_x^1\frac{ds}{pf_\pm^2}.                        \tag{3.2}
\]
Define
\[
\Delta_-(\rho)=1+8\rho-12\rho^2\log\rho-8\rho^3-\rho^4,
\]
\[
\Delta_+(\rho)=1-3\rho-2\rho^2+4\rho^3
 +6\rho^2(1+\rho)\log\frac{1+\rho}{2\rho}.
\]
Direct integration gives
\[
\kappa_- =\frac{(1+\rho)^5}{2\Delta_-}-\frac{2-3\rho}{8},
\qquad
\kappa_+=\frac1{2\Delta_+}-\frac{2+3\rho}{8}.                \tag{3.3}
\]

Equation (2.1) contains a second copy of the trace coefficient, produced when the unintegrated quadratic action is put into Sturm form. Thus, for terminal matching \(v_\pm(1)=0\), the **full CH quadratic action** obeys
\[
\boxed{\mathcal A_{CH}^{(2)}\ge
 d_+(\rho)V_+^2+d_-(\rho)V_-^2,}                              \tag{3.4}
\]
where
\[
d_+=\frac1{2\Delta_+}-\frac{2+3\rho}{4},
\qquad
d_-=\frac{(1+\rho)^5}{2\Delta_-}-\frac{2-3\rho}{4}.  \tag{3.5}
\]
As \(\rho\downarrow0\),
\[
d_+=\frac34\rho+O(\rho^2|\log\rho|),\qquad
 d_-=-\frac34\rho+O(\rho^2|\log\rho|).                      \tag{3.6}
\]
These asymptotics and the numerical values below were also independently checked from the closed formulas; they do not come from a fit to the cell profiles.
At \(\rho=.1\), \(d_+\approx .05274\), \(d_-\approx-.03565\). The transition must therefore supply the signed trace payment
\[
\boxed{\mathcal A_{tr}^{(2)}
 +d_+(\rho)V_+^2+d_-(\rho)V_-^2\ge0.}                        \tag{3.7}
\]
This is the precise inner-to-CH comparison, much narrower than asking for positivity of an unrestricted sign-changing potential.

## 4. What torsion-free reconstruction adds

The radii and spin variables are not independent:
\[
\dot a_i=u_i+\gamma_i(a),\qquad
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.                   \tag{4.1}
\]
Exactly,
\[
\frac d{dt}\log\frac ac=
\frac{u_1}{a}-\frac{u_3}{c}+\frac{2(c^2-a^2)}{abc}.           \tag{4.2}
\]
Linearize on CH, write \(\theta=\delta\log(a/c)\). Then
\[
\boxed{\frac d{dx}\left[\left(\frac{x}{1+x}\right)^2\theta\right]
 =\frac12f_-(x)v_-(x).}                                      \tag{4.3}
\]
The same \(f_-\) selected by the Sturm factorization is therefore the natural adjoint weight of the metric evolution. With \(\theta(1)=0\),
\[
\int_\rho^1f_-v_-\,dx
=-2\left(\frac{\rho}{1+\rho}\right)^2\theta(\rho).         \tag{4.4}
\]
This moment relation adds an explicit nonnegative square to the sharp minus-channel endpoint problem, but it is not alone sufficient: the transition value \(\theta(\rho)\) can align to make that square vanish. The remaining quadratic theorem is a joint trace inequality in \((V_+,V_-,\theta)\), under regular bolt data and the longitudinal endpoint relations. The full finite-amplitude theorem is its variable-coefficient nonlinear analogue along (4.1), with the signed cubic retained.

Smoothness also does not make the cubic favorable. If
\[
a=A+\alpha t^2+O(t^4),\quad b=A+\alpha t^2+O(t^4),\quad
c=t+\gamma t^3+O(t^5),
\]
then
\[
u_1=u_2=\left(2\alpha-A^{-1}\right)t+O(t^3),\qquad
u_3=-1+O(t^2),
\]
so
\[
\frac{2u_1u_2u_3}{\lambda_2}
=-2(2\alpha-A^{-1})^2t+O(t^3).                               \tag{4.5}
\]
The adverse chamber is generic next to the bolt; compensation must be integrated.

## 5. Geometric validity of the computed competitors

For the implemented fixed-slot profile
\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\]
ordinary bolt smoothness requires
\[
F'(x_0)G'(x_0)=1,\qquad w=O((x-x_0)^2)=O(t^4).                \tag{5.1}
\]
The coefficient shift in the scripts enforces the first condition, and all main runs use `wpow=2`, which enforces the second. `wpow=1` is generally not smooth.

The stored polynomial profiles are not literally CH on an open collar, but they match
\[
F_0=x,\quad G_0=x(1+x),\quad w_0=\log(1+x)
\]
through their second \(x\)-jets at \(X\). If \(q=(F-F_0,G-G_0,w-w_0)\) and
\[
|\partial_x^jq|\le A(X-x)^{3-j},\qquad j=0,1,2,3,
\]
then multiplying \(q\) by a smooth cutoff that is one on \(x\le X-2\varepsilon\) and zero on \(x\ge X-\varepsilon\) gives an exact-CH-collar metric with
\[
|\Delta P|+|\Delta J_6|\le CA^2\varepsilon^3.                \tag{5.2}
\]
This follows because the cutoff metric two-jet differs from CH by \(O(A\varepsilon)\) on an interval of length \(O(\varepsilon)\), while both defect curvatures vanish on CH. The actual envelopes vanish cubically at \(X\), so (5.2) applies profile by profile. Thus their reported costs are limits of genuine smooth exact-collar costs.

## 6. Numerical interpretation after exact factorization

`scripts/perp_transition_analysis.py` evaluates the signed relative action and the exact-CH comparison on the degree-8 \(x_0=.01\) P- and J-target records. For the J-target profile,
\[
P/(8\pi^2)-1=.0018558270
=.0034706397-.0016148127,                                    \tag{6.1}
\]
where the last two numbers are relative squares and the full cubic. The cubic itself splits as
\[
C_+=2.7244\times10^{-5},\qquad C_-=-.0016420567.              \tag{6.2}
\]
Thus positive-cubic regions are small here but real; they must not be discarded in the theorem. At a cut near \(x=.1\), the profile is still about 5--10% away from exact CH in its radii/weights, so the exact operator is a comparison endpoint, not an identity for that non-CH outer portion.

The peer's exported smooth \(x_0=.03\), degree-10 profile was independently evaluated only from \(G,h\) and their first two derivatives in `scripts/perp_export_spin_eval.py`; see `data/perp_dual/peer_export_x003_spin.json`. The coordinate-free positive-square reconstruction gives \(P/(8\pi^2)=1.01857832\), within \(1.75\times10^{-5}\) of the peer curvature value. The relative identity gives
\[
1+.0206129103-.0020170647=1.0185958456,                       \tag{6.3}
\]
reproducing the peer value to the grid accuracy. Here
\[
C_+=.0005819731,
\qquad C_-=-.0025990378,                                     \tag{6.4}
\]
and the independently evaluated scalar square is .0044287927, giving \(J_6/(8\pi^2)\approx1.02300711\). The charge minimum is .118394 near \(x=.107755\). No subthreshold perpendicular profile has been found.

## 7. Scope correction from the signed complex-space-form experiment

Peer S1003A02 proposed the general first-order response
\[
\frac{P(g_a)-P(g;B_a)}{8\pi^2}
=1-a^2\mathcal R_p^+(\zeta,\zeta)+o(a^2),
\qquad \mathcal R^+=W^++\frac{s}{12}I,                        \tag{7.1}
\]
whose proof still requires the full matrix-valued Burns ALE boundary transgression. This Session independently reran the aligned complex-space-form specialization with
\[
K_{bulk}=x+\kappa x^2,
\qquad s=-24\kappa,
\qquad x_0=a^2=.001,
\qquad X=.25.
\]
The outputs are `data/perp_dual/general_bulk_FS_x0001.json` and `general_bulk_CH_x0001.json`:
\[
\kappa=-1:\quad P/(8\pi^2)=.9941059313,
\quad (P/(8\pi^2)-1)/x_0=-5.89407,                            \tag{7.2}
\]
\[
\kappa=+1:\quad P/(8\pi^2)=1.0060581122,
\quad (P/(8\pi^2)-1)/x_0=+6.05811.                            \tag{7.3}
\]
These are direct same-metric \(P\)-integrals with optimizer gradients about \(3\times10^{-7}\), and they exhibit the predicted sign reversal. In particular, a universal statement that every blow-up cell on every Einstein or complex-space-form background costs at least \(8\pi^2\) is false: positive Kähler--Einstein curvature has an explicit U(2)-symmetric subthreshold \(P\) cell. This does **not** contradict the balanced CH problem, whose bulk has the opposite sign; it shows that any general lower theory must retain the background curvature operator, and that the CH coefficient-four problem is a second-order kernel-direction problem rather than a universal local topological charge theorem.

The FS computation concerns \(P\), not the CH-normalized Einstein cost \(J_6\), and it lies outside the negative-KE balanced-family hypotheses. It is nevertheless decisive for the proposed unified theory: the local cell response is curvature-sensitive.

## 8. Present conclusion and next theorem target

The Step-6 relative calibration is correct, including factors, orientation, endpoint term, and cubic sign. The sign-changing exact-CH potential is no longer the unresolved bulk problem: both channels possess positive ground states, and their sharp outgoing Dirichlet-to-Neumann forms are explicit. Exact collar replacement is mathematically valid for the stored smooth profiles. The load-bearing unresolved inequality is now the inner transition payment (3.7), strengthened by the torsion-free moment relation (4.4), first at quadratic order and then at finite amplitude. For \(J_6\), the scalar square supplies additional rank-one coercivity and should be analyzed separately rather than inferred from \(P\).

This remains a theorem target only for the diagonal perpendicular CH class. Even a proof there would not establish the unrestricted cell conjecture or the balanced all-metric coefficient. Beyond symmetry, the natural problem is the gauge-fixed spectral/relative-calibration analogue. Across backgrounds, (7.1) suggests a deeper classification: positive eigenvalues of \(\mathcal R^+\) create first-order cheap cells, negative eigenvalues make aligned cells costly, and kernel directions force a second-order interaction theory.

A small implementation error was also repaired during this review: `perp_dual_cost.py eval` previously read the dual record's degree only from `degU` and therefore silently treated a degree-8 dual record as degree 6. It now reads `deg` first and reproduces the stored degree-8 J-target value \(P/(8\pi^2)=1.0018558257\), \(J_6/(8\pi^2)=1.0019394136\). This did not affect the earlier sweeps, which constructed their cells directly, but it matters for reproducible re-evaluation.



---

## Source step8_kahler_period_law_and_Rplus_response.md

Original: [sources/Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md](../sources/Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md)

# Step 8 — Kähler period law, signed blow-up cells, and the first-order response \(1-\tfrac{t}{\pi}R^+(\hat\zeta,\hat\zeta)\)

Session S1003A01, Step 8, Agent2, Execute. Conventions: \(d\sigma_i=2\sigma_j\wedge\sigma_k\), \(\int_{S^3}\sigma_{123}=2\pi^2\); \(P=\int|\operatorname{Ric}^\circ|^2\) (tensor norm), \(J_\lambda=\int|\operatorname{Ric}-\lambda g|^2=P+\tfrac14\int(s-4\lambda)^2\); a *cell* is a metric on the blow-up of a ball that coincides with an Einstein background \(\operatorname{Ric}=\lambda g\) on a collar; its cost is the integral over the cell (the background contributes zero). In peer/cell coordinates the complex-space-form collar is \(K=x+\kappa x^2\) with \(\lambda=-6\kappa\) (\(\kappa=1\): complex hyperbolic, \(\kappa=-1\): Fubini–Study), the bolt sits at \(x=x_0\), and the exceptional area is \(t=\pi x_0\).

## 1. The Kähler period law (no symmetry assumed)

**Theorem 1.** Let \((C,J,\omega)\) be a Kähler cell: the one-point complex blow-up of a ball in a Kähler–Einstein surface with \(\operatorname{Ric}=\lambda g\), with \(\omega\) equal to the background on a collar. Let \(t=\int_E\omega\) and \(L=\int_C(s-4\lambda)^2\). Then
\[
\boxed{P=2(2\pi-\lambda t)^2+\tfrac14L,\qquad J_\lambda=2(2\pi-\lambda t)^2+\tfrac12L.}
\]
*Proof.* \(\psi=\rho-\lambda\omega\) is closed, of type (1,1), and vanishes on the collar, so it defines a compactly supported class. Relative to the background, \([\rho]\) changes by \(-2\pi\,\mathrm{PD}(E)\) and \([\omega]\) by \(-t\,\mathrm{PD}(E)\); with \(E^2=-1\), \(\int\psi\wedge\psi=-(2\pi-\lambda t)^2\). Since \(\psi^+=\tfrac14(s-4\lambda)\omega\) and \(\psi^-=\rho_0\), \(\int|\rho_0|^2=(2\pi-\lambda t)^2+L/8\) in form norms, and \(|\operatorname{Ric}^\circ|^2=2|\rho_0|^2\). \(\square\)
This is the signed version of I54 (3.2) (\(\lambda=-1\)).

**Corollaries.** (a) Every Kähler cell has \(P>2(2\pi-\lambda t)^2\) unless \(\lambda t=2\pi\): equality forces \(s\equiv4\lambda\), so \(\psi\) is a compactly supported closed anti-self-dual, hence harmonic, form; unique continuation from the collar gives \(\psi=0\), contradicting the nonzero period. The bound is not attained. (b) For \(\lambda<0\) all Kähler cells cost more than \(8\pi^2\) (inherited). (c) For \(\lambda>0\) the topological term is \(8\pi^2(1-\lambda t/2\pi)^2<8\pi^2\): Kähler blow-up cells in positive Kähler–Einstein backgrounds are cheaper than the flat charge \(8\pi^2\) whenever \(L=o(t)\). In cell coordinates the topological term is \(8\pi^2(1+3\kappa x_0)^2\).
(d) Global form: for a Kähler metric on a compact surface, \(P=\tfrac14\int s^2-8\pi^2c_1^2\ge8\pi^2[(c_1\cdot\omega)^2/\omega^2-c_1^2]\) (Hodge index/Cauchy–Schwarz). On \(\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\) with \([\omega]=H-\varepsilon E\) this is \(8\pi^2(1-3\varepsilon)^2/(1-\varepsilon^2)\); its localization at small \(\varepsilon=x_0\) is exactly the cell term \((1+3\kappa x_0)^2\), \(\kappa=-1\). The cell constant \(8\pi^2\) is the local Hodge-index defect of one exceptional class.

## 2. U(2) Kähler cells: exact identity and exact infimum

For \(g=dx^2/(4K)+x(\sigma_1^2+\sigma_2^2)+K\sigma_3^2\) (Kähler for every \(K\); ordinary bolt \(K(x_0)=0,\ K'(x_0)=1\)), `scripts/kahler_period_cell.py` derives from the Cartan-verified spin formulas:
\[
s=\frac{4(2-(xK)'')}{x},\qquad
\frac{P}{8\pi^2}=(1+3\kappa x_0)^2+\frac12\int_{x_0}^{X}\frac{u''^2}{x}\,dx,\qquad
\frac{J}{8\pi^2}=(1+3\kappa x_0)^2+\int_{x_0}^{X}\frac{u''^2}{x}\,dx,
\]
with \(u=xK-x^2-\kappa x^3\). The density identity is exact: \(P\)-density \(-\tfrac12u''^2/x=B'(x)\), \(B=-(K+xK'-3\kappa x^2)(K+xK'-3\kappa x^2-4x)/x^2\), \(B(\text{collar})-B(\text{bolt})=(1+3\kappa x_0)^2\); only \(C^1\) matching enters. Burns (\(K=x-x_0\), flat collar at infinity) has \(P\)-density \(2x_0^2/x^3\), total \(8\pi^2\).

The constraints are \(\int u''=x_0+3\kappa x_0^2\), \(\int xu''=2\kappa x_0^3\). Weighted Cauchy–Schwarz gives the **exact infimum over U(2) Kähler cells with collar radius \(X\)**:
\[
\inf\frac{P}{8\pi^2}=(1+3\kappa x_0)^2+\tfrac12m^TG^{-1}m,\qquad G_{ij}=\int_{x_0}^Xx^{1+i+j}dx,
\]
approached by Calabi-extremal profiles \(u''=x(A+Bx)\) (scalar curvature affine in the moment coordinate). The extremal profile has a scalar-curvature jump at \(X\); smooth cells approach but do not attain the infimum. Series: \(m^TG^{-1}m=18x_0^2(1+6\kappa x_0)/X^2+O(x_0^4)\).

Independent check (`scripts/kahler_crosscheck_peer.py`, `data/kahler_cells/peer_crosscheck.json`): the peer coordinate-curvature code evaluated on the extremal profile agrees with the identity to \(3\times10^{-14}\) for \(P\) and \(J\) in four cases, e.g. \(x_0=.001,X=.25,\kappa=-1\): \(P=0.99415216083\). Exact infima are in `data/kahler_cells/extremal_inf.json`.

## 3. Explicit smooth countercells in a Fubini–Study collar

**Theorem 2.** There are smooth U(2)-invariant Kähler metrics on the blow-up of a ball, equal to the Fubini–Study metric (\(\operatorname{Ric}=6g\)) on a collar, with \(P<8\pi^2\) and \(J_6<8\pi^2\). Explicitly take \(\kappa=-1\) and
\[
K=x-x^2+(1-\chi)\Big(-x_0+3x_0^2-\frac{2x_0^3}{x}\Big),
\]
with \(\chi\) the standard \(C^\infty\) step from 0 at \(a\) to 1 at \(X\). For \(x<a\) this is the exact constant-scalar-curvature profile \(K=x_0(y-1)[1-x_0(y-1)(y+2)/y]\), \(y=x/x_0\), with \(K(x_0)=0,K'(x_0)=1\); for \(x\ge X\) it is Fubini–Study. With \((x_0,a,X)=(0.01,0.1,0.5)\): \(P/8\pi^2=0.949823\), \(J/8\pi^2=0.958747\), \(\min K/(x-x_0)=0.5102\) (`scripts/kahler_smooth_countercell.py`, 30-digit quadrature, `data/kahler_cells/smooth_fs_countercells.json`). For fixed \(a,X\), \(P/8\pi^2=1-6x_0+O(x_0^2)\). Since the Fubini–Study collar extends to the line at infinity (\(K'(1)=-1\)), this also gives explicit Kähler metrics on \(\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\) with \(\int|\operatorname{Ric}-6g|^2<8\pi^2\).

The peer's numerical sign reversal is therefore a theorem. Its source is the relative Chern-class/Einstein-constant pairing \(2\pi-\lambda t\), not an \(O(x_0)\) analytical correction.

## 4. All U(2) (conformally Kähler) cells: relative identity and second-order relaxation

Every biaxial U(2) metric \(g=dx^2/(4G)+x(\sigma_1^2+\sigma_2^2)+F\sigma_3^2\) is conformally Kähler (I54 §5). With Gauss–Bonnet and signature relative to the ball (\(\Delta\chi=1,\ \Delta\tau=-1\), identical collars):
\[
P=8\pi^2+4\Delta W^++\tfrac1{12}\Delta S,\qquad \Delta W^+=\tfrac1{24}\big(S_K-S_K^{\rm bulk}\big)\ \text{for } G=w^2K,
\]
with \(K\) the Kähler representative. For \(K\) of constant scalar curvature, the conformal Yamabe-type quotient \((\int6|dw|^2+s_Kw^2)^2/\int w^4\) is stationary at \(w=1\). Hence conformal relaxation away from Kähler gains only at second order. Numerically (`scripts/u2_general_cell.py`, Fubini–Study, \(X=.25\)), the general U(2) infimum lies below the Kähler infimum by \(6\times10^{-5}\approx60x_0^2\) at \(x_0=.001\) and by \(4.1\times10^{-4}\approx46x_0^2\) at \(x_0=.003\). The first-order term is unchanged.

## 5. Real space-form backgrounds: universal scalar response

\(H^4\) and \(S^4\) with \(\operatorname{Ric}=-6kg\) are \(F=x,\ G=x+2kx^2\) (verified Einstein symbolically in `u2_general_cell.py verify`). Write such a background as \(w^2g_{\rm flat}\), \(w=2/(1+cy)\), \(c=\lambda/3\). Insert a flat-collar Kähler cell \(K=y-y_0(1-\chi)\) with \(G=w^2K\). Since \(dV_K=\pi^2y\,dy\) does not depend on \(K\), \(s_GdV_G=(-6w\Delta_Kw+s_Kw^2)dV_K\). Integrating by parts, the cutoff-dependent term is \(\int y(1-\chi)(2ww''-4w'^2)\), and it vanishes identically for the space-form factor. Hence
\[
\Delta\!\int s_G\,dV_G=-4\pi t_G+O(t_G^2),\qquad t_G=\pi y_0w(y_0)^2,
\]
which is exactly the Kähler topological value (`scripts/spaceform_scalar_response.py`, symbolic). Also \(S_K=O(t^2)\) (Burns is anti-self-dual), \(\Delta V=O(t^2)\), and \(\int(s_G-4\lambda)^2=O(t^2\log t^{-1})\). Thus \(\Delta S=-32\pi\lambda t_G+o(t)\) and
\[
\frac{P}{8\pi^2}\le1-\frac{\lambda}{3}x_0+o(x_0)\qquad\text{in every orientation (isotropy).}
\]
Numerical infima of the general U(2) class (`data/u2_general/`, degree 10, \(X=.25\)) at \(x_0=3\times10^{-5}\) have slopes \((P/8\pi^2-1)/x_0=+2.0048\) (\(H^4\), prediction \(+2\)) and \(-1.9977\) (\(S^4\), prediction \(-2\)), against \(+6.0003\) and \(-5.9981\) for the complex space forms (prediction \(\pm6\)). The slopes converge as \(x_0\downarrow0\): \(H^4\) gives 2.0158, 2.0475, 2.4340, 3.2484 at \(x_0=10^{-4},3\cdot10^{-4},3\cdot10^{-3},10^{-2}\).

## 6. The first-order response law

For a background metric with curvature \(\mathrm{Rm}_p\) at the blow-up point, a Burns cell of area \(t=\pi a^2\) is oriented by its asymptotic Kähler form \(\hat\zeta\in\Lambda^+_p\), \(|\hat\zeta|=1\). The rescaled background is flat plus \(a^2\mathrm{Rm}_p\). The first-order response is therefore a linear functional \(\mathcal L(\mathrm{Rm}_p)\), invariant under the stabilizer \(U(2)_{\hat\zeta}=(U(1)_+\times SU(2)_-)/\pm1\). Since \(SU(2)_-\) acts irreducibly on \(\Lambda^-\), \(\Lambda^+\otimes\Lambda^-\) (traceless Ricci) and \(\mathrm{Sym}^2_0\Lambda^-\) (\(W^-\)) contain no invariants. The invariants are spanned by \(s\) and \(W^+(\hat\zeta,\hat\zeta)\). The two exact computations fix both coefficients:

* Kähler–Einstein, aligned: \(s=4\lambda\), \(W^+(\hat\omega,\hat\omega)=2\lambda/3\), slope \(-\lambda\) (Theorem 1);
* real space form: \(W^+=0\), slope \(-\lambda/3=-s/12\) (§5).

Therefore
\[
\boxed{\frac{P_{\rm cell}}{8\pi^2}=1-\frac t\pi\Big(W^+(\hat\zeta,\hat\zeta)+\frac s{12}\Big)+o(t)=1-\frac t\pi R^+(\hat\zeta,\hat\zeta)+o(t).}
\]
A third, independent datum confirms it. For the perpendicular orientation in a Kähler–Einstein background, \(R^+(\hat\zeta_\perp,\hat\zeta_\perp)=-s/12+s/12=0\), and the CH perpendicular cells indeed have no linear term (Steps 6–7, peer Step 8). Scope: Theorem 1 gives the exact topological term for all aligned Kähler cells. §5 gives an upper construction in all orientations of space forms. The law for the cell *infimum* in a general background still assumes that the infimum's first-order term is the linear response of the glued Burns tail. Numerically, relaxations enter only at \(O(t^2)\) in all four backgrounds; this has not been proved.

## 7. Consequences for the Einstein-gap programme

1. **The \(8\pi^2\) blow-up charge is a flat-background value.** In a background it is shifted by \(-8\pi tR^+(\hat\zeta,\hat\zeta)\). A cell is cheaper than \(8\pi^2\) to first order exactly when the oriented self-dual curvature operator has a positive eigenvalue at the insertion point.
2. **The balanced complex-hyperbolic family is critical.** For negative Kähler–Einstein metrics, \(\operatorname{spec}R^+=\{s/4,0,0\}\le0\), with a two-dimensional kernel \(\omega^\perp\). No orientation gains at first order, and the kernel is precisely the perpendicular slot. The coefficient-four question therefore sits at a degenerate point of the first-order law, and only the second-order term can decide it. This explains structurally why the perpendicular branch has no linear term and why its observed margin is \(O(x_0^2)\).
3. **Real hyperbolic backgrounds are strictly first-order rigid.** There \(R^+=(s/12)\mathrm{Id}<0\), so every orientation pays \(+2x_0\) (in \(\operatorname{Ric}=-6g\) units). Surgery families over real-hyperbolic pieces have a first-order cell cost strictly above \(8\pi^2\).
4. **For general negative backgrounds**, first-order saving requires \(w^+_{\max}>|s|/12\). The background is a free variable in the global problem, but an Einstein metric agreeing with complex hyperbolic space on a collar is complex hyperbolic (unique continuation). Creating \(R^+>0\) near a cell therefore costs \(\int|\operatorname{Ric}^\circ|^2\sim\delta^2\) against a gain \(\sim x_0\delta\), a net effect of order \(x_0^2\). This is the same order as the perpendicular margin. The second-order problem consists of the perpendicular cell together with its optimal background response (the Green operator of the linearized Einstein operator on CH with the collar condition). It is monotone in the collar radius \(X\), because a collar-\(X\) cell is admissible for every \(X'>X\). The X-scan of the perpendicular cell (`scripts/perp_collar_scan.py`, `data/perp_collar/`) tests exactly this channel.

## 8. Files

`scripts/kahler_period_cell.py`, `kahler_cell_infimum.py`, `kahler_crosscheck_peer.py`, `kahler_smooth_countercell.py`, `spaceform_scalar_response.py`, `u2_general_cell.py`, `u2_general_sweep.sh`, `perp_collar_scan.py`; data `data/kahler_cells/`, `data/u2_general/`, `data/perp_collar/`.



---

## Source step9_subthreshold_cell_verification.md

Original: [sources/Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md](../sources/Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md)

# Step 9 — Verification state of the finite-scale perpendicular subthreshold cell

Session S1003A01, Step 9, Agent3, Execute.

## 1. Fixed witness and the quantity that matters

Keep the Step-8 degree-eight coefficient vector fixed; no stationarity or numerical infimum is used.  It is stored in

`workspace/data/perp_collar/x0.01_X8_J_d8.json`.

The cell is in the `Ric_CH=-6g` normalization and has

\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\qquad x_0=10^{-2},\quad X=8.
\]

The target is

\[
 J_6=\int|\operatorname{Ric}+6g|^2
 =P+\frac14\int(s+24)^2,
 \qquad P=\int|\operatorname{Ric}^\circ|^2.
\]

Under the simultaneous rescaling \(\widetilde g=6g\), the background satisfies
\(\operatorname{Ric}_{\widetilde g}=-\widetilde g\), and scale invariance of the dimension-four integral gives

\[
 \int|\operatorname{Ric}_{\widetilde g}+\widetilde g|_{\widetilde g}^2dV_{\widetilde g}
 =J_6(g).
\]

Thus `J` in the record is exactly the single-blowup cell cost \(J_1/(8\pi^2)\) in I54 §2.

## 2. Independent numerical reconstruction

The local verifier `workspace/scripts/perp_collar_verify.py` uses two formula sets:

1. the coordinate-curvature implementation inherited from `o11_perp_cell.py`;
2. the independently Cartan-verified spin formula, integrated in logarithmic radius with split Gauss quadrature.

For the frozen \(X=8\) record it gives

\[
 \frac{P}{8\pi^2}=0.99910870273352,\qquad
 \frac{J_6}{8\pi^2}=0.99911624313525.
\]

The coordinate implementation at 600, 1200 and 2400 nodes gives \(J=0.9991162433,0.9991163627,0.9991163780\), while the split spin computation at 1200 and 3000 gives identical values to about \(6\times10^{-14}\).  The slight coordinate drift at high unsplit order is numerical conditioning near the bolt, not a sign change.

The peer independently reconstructed the metric in a new local script importing neither `DualCell` nor this Session's spin code.  Their 200/400/800 split orders gave

\[
 P/(8\pi^2)=0.99910870273359,
 \quad (J-P)/(8\pi^2)=7.54040173166\times10^{-6},
 \quad J/(8\pi^2)=0.99911624313532,
\]

and their positive-square and relative-calibration formulas agreed to \(4\times10^{-15}\).  This is peer message 756.

A second fixed witness with a larger margin is
`workspace/data/perp_collar/x00.01_X16_J_d8.json`.  Its independent local output is

\[
 P/(8\pi^2)=0.99887845250601,
 \qquad J/(8\pi^2)=0.99890294371985,
\]

in `workspace/data/perp_collar/verify_x0.01_X16_J_d8.json`.  This has a deficit about \(1.10\times10^{-3}\), but requires a larger embedded ball.  The \(X=8\) witness is retained as the smaller geometric construction.

## 3. Smoothness and exact-collar structure

The profile is built from entire functions of

\[
 u=\frac{\log(x/x_0)}{\log(X/x_0)}
\]

on the closed interval.  At the bolt, putting \(y=x-x_0\),

\[
 F=f_1y+O(y^2),\qquad G=g_1y+O(y^2),\qquad f_1g_1=1,
 \qquad w=O(y^2).
\]

The stored witness has \(f_1=0.9688603622\), \(g_1=1.0321404807\).  These are the standard no-cone bolt relation and the weight-four anisotropy condition for the \(s_1\)-collapsing slot.  The peer independently checked
\(F=G=w=0\), \(F'G'=1\), \(w'=0\) at the bolt.

The implemented factors `(1-u)^3` imply exact agreement of values and first two \(x\)-derivatives with the complex-hyperbolic profile at \(x=X\).  It is therefore a \(C^2\) metric after direct attachment to an exact collar, with zero curvature jump but not yet literally \(C^\infty\).  The Step-7 cutoff lemma applies: because the deviations vanish to third order at the attachment, replacing them by a flat cutoff in a collar of width \(\delta\) changes \(P\) and \(J_6\) by \(O(\delta^3)\) for this fixed witness.  Since the computed deficit is fixed, a sufficiently small \(\delta\) preserves \(J_6<8\pi^2\).  A quantitative derivative bound for a specified cutoff remains to be written if a fully explicit margin is desired.

Positivity is actually analytic, not merely sampled.  The smoothstep satisfies \(0\le S(u)\le1\), and the profile formula gives
\[
 F=(x-x_0)e^{q_F}+x_0S(u)>0,
 \qquad
 G=[(x-x_0)+(x^2+x_0)S(u)]e^{q_G}>0
\]
for \(x_0<x\le X\), while \(h_2=x>0\) and \(h_3=xe^w>0\).  The 20,001-point values
\[
 \min\frac{F}{x-x_0}=0.9661766585,
 \qquad
 \min\frac{G}{x-x_0}=1.0321421993
\]
are useful conditioning measurements, not the proof.  An Arb subdivision attempt also enclosed positive normalized \(F,G\), but the direct raw spin interval integrand suffered severe dependency inflation and did not enclose the energy sharply.  The files `workspace/scripts/perp_interval_certificate.py`, `perp_ball_integrate_fast.py`, and `workspace/data/perp_collar/interval_*` record this unsuccessful route; none is a valid energy certificate.

## 4. Mechanism, not just the total

The exact relative calibration gives

\[
 \frac{P}{8\pi^2}-1=S_1+S_2+S_3+C_3.
\]

For the \(X=8\) witness,

\[
 (S_1,S_2,S_3)=(0.0015972917,0.0005224470,0.0010902866),
 \qquad C_3=-0.0041013225.
\]

Only about \(1.14\times10^{-6}\) of the cubic integral is positive.  Hence the cubic compensation exceeds the three flow squares by \(8.91\times10^{-4}\); the scalar square adds only \(7.54\times10^{-6}\).  A 20,001-point mechanism run shows that the relative-plus-scalar density is negative over much of \(0.016\lesssim u\lesssim0.835\).  Contributions over the five logarithmic ranges are approximately

\[
(-8.65,-77.78,-77.39,+48.45,+27.00)\times10^{-5}
\]

for \(u\in(0,.1),(.1,.3),(.3,.6),(.6,.9),(.9,1)\).  The cumulative deficit reaches \(-1.91\times10^{-3}\) near \(u=.513\), and part is paid back before the collar, leaving \(-8.84\times10^{-4}\).  This is a finite-scale core-to-background interaction, not an AE shrinking-core effect.

The Step-8 continuation task adds corroboration.  At \(X=8\), subthreshold values occur for \(x_0=.003,.01,.03\), though the \(x_0=.001\) J-target restart remained slightly above one.  At \(x_0=.01\), the degree-12 restart stays below one, and \(X=16,32\) remain below one.  These runs support a basin, but the theorem needs only one fixed witness.

## 5. Global transfer on a suitably chosen balanced sequence

I54 §2 proves for one blow-up cell of cost \(J_1\), with the handle surgeries made by the standard shrinking construction,

\[
 \limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
 \le \frac{28}{9}+\frac{J_1}{9\pi^2}.
\]

Writing \(J_1=8\pi^2(1-\varepsilon_0)\), this is

\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le4-\frac{8\varepsilon_0}{9}.
\]

For the numerical \(X=8\) witness, \(\varepsilon_0\approx8.83757\times10^{-4}\), so the indicated coefficient is approximately

\[
 3.9992144389.
\]

The large fixed ball does not require a uniform injectivity-radius theorem for arbitrary covers.  Let \(p\in\mathbb{CH}^2\) and choose a buffered radius \(r\) containing the fixed cell and smoothing collar.  Only finitely many nonidentity lattice elements satisfy \(d(p,\gamma p)\le2r\).  Residual finiteness supplies a finite-index subgroup avoiding this finite set, hence a compact finite cover \(X_*\) with the required embedded ball.  Taking further covers inside this subgroup produces disjoint lifts with number proportional to the degree, hence proportional to \(A_j\).  Since the balanced family uses only \(Q_j=o(A_j)\) surgeries and only \(k_j\sim(2/9)Q_j\) copies of this one-blowup cell, the selected large-ball lifts suffice.  A subsequence can still be chosen with \(A_j\ge j^4\), exactly as in the inherited residual-finiteness construction.  This proves availability for an existential balanced sequence; it does not retrofit every previously fixed cover sequence.

The radial relation in the peer coordinates is \(r_{-6}=\operatorname{arsinh}\sqrt X\); after scaling to `Ric=-g`, \(r_{-1}=\sqrt6\,r_{-6}\).  At \(X=8\), \(r_{-1}\approx4.32\), plus a fixed smoothing buffer.

## 6. What is and is not established

The following parts are now independently supported:

* exact algebraic identities for \(P\), \(J_6\), and the relative calibration;
* two independent numerical reconstructions of the frozen profile;
* positive metric analytically from the profile formula, with a wide sampled conditioning margin;
* exact bolt jets and second-jet CH matching;
* a qualitative smooth-collar perturbation preserving a strict gap;
* the residual-finiteness large-ball supply and I54 transfer formula.

The missing part for a fully rigorous explicit upper witness is a sharp validated enclosure of the frozen integral together with positivity on the whole interval and a numerical bound for the chosen smoothing cutoff.  The first Arb implementation exposed the difficulty: raw spin variables near the bolt contain cancelling terms and interval dependency grows catastrophically.  The next verified route should use analytic bolt Taylor series on a short initial interval and a compiled Arb/MPFI evaluator of the already simplified relative density on the remainder, or exact rational-polynomial bounds after replacing exponentials by Taylor models.  The available floating margin is \(8.84\times10^{-4}\) at \(X=8\), or \(1.10\times10^{-3}\) at \(X=16\).

Accordingly, O11 has not yet been declared solved in this note.  The evidence has, however, changed its likely answer: the universal coefficient four is now threatened by an explicit finite-scale perpendicular cell, while all earlier AE and shrinking-core lower mechanisms can remain valid in their stated regimes.



---

## Source step10_rigorous_subthreshold_cell_and_O11.md

Original: [sources/Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md](../sources/Sessions/S1003A01/workspace/notes/step10_rigorous_subthreshold_cell_and_O11.md)

# Step 10 — Rigorous subthreshold perpendicular cell; the balanced coefficient four is not sharp

Session S1003A01, Step 10, Agent2, Execute.  Builds on Step 7 (Cartan verification, bolt jets), Step 8 (collar scan), Step 9 (frozen witness, transfer chain).

## 1. Statement

**Theorem (finite-scale subthreshold cell).** Let \(x_0=1/100\), \(X=8\), and let \(z\in\mathbb Q^{24}\) be the 24 binary doubles stored in
`workspace/data/perp_collar/x0.01_X8_J_d8.json`.  Define on \(x_0\le x\le X\), with \(u=\log(x/x_0)/\ell\), \(\ell=\log(X/x_0)\), \(S(u)=10u^3-15u^4+6u^5\), \(T_k\) Chebyshev polynomials of \(2u-1\),

\[
\begin{aligned}
q_F&=(1-u)^3\textstyle\sum_{k<8}z_kT_k,\qquad q_G=(1-u)^3\sum_{k<8}\tilde z_{8+k}T_k,\\
F&=(x-x_0)e^{q_F}+x_0S,\qquad G=\big(x-x_0+(x^2+x_0)S\big)e^{q_G},\\
w&=\log(1+x)\,S+u^2(1-u)^3\textstyle\sum_{k<8}z_{16+k}T_k,
\end{aligned}
\]

where \(\tilde z\) equals \(z\) except \(\tilde z_8=z_8-\sum_k(-1)^k(z_k+z_{8+k})\) (so \(q_F(0)+q_G(0)=0\)).  The metric

\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^{w}\sigma_3^2,\qquad d\sigma_1=2\sigma_2\wedge\sigma_3\ \text{(cyclic)},
\]

closed by the exceptional sphere at \(x=x_0\) and continued by the exact complex-hyperbolic metric (\(F=x,\ G=x+x^2,\ e^w=1+x\), \(\operatorname{Ric}=-6g\)) for \(x\ge X\), is a \(C^2\) metric on a ball of \(\mathbb{CH}^2\) blown up once, \(D\#\overline{\mathbb{CP}}^2\), and

\[
\boxed{\frac{1}{8\pi^2}\int|\operatorname{Ric}+6g|^2\,dV\in[0.99911624314\pm7.0\times10^{-12}],}
\]
\[
\frac{1}{8\pi^2}\int|\operatorname{Ric}^\circ|^2\in[0.99910870273\pm5.8\times10^{-12}],\qquad
\frac{1}{8\pi^2}\cdot\frac14\int(s+24)^2\in[7.54040\times10^{-6}\pm3.6\times10^{-12}].
\]

Thus \(J_6/(8\pi^2)\le1-\eta\) with \(\eta=8.8375686\times10^{-4}\) certified.  The second frozen profile `x00.01_X16_J_d8.json` (\(X=16\)) gives \(J_6/(8\pi^2)\in[0.99890294372\pm2.4\times10^{-12}]\), \(\eta_{16}=1.0970563\times10^{-3}\).

**Corollary (O11, negative answer).** There is a smooth single-blowup cell with exact CH collar and \(J_1\le 8\pi^2(1-\eta/2)\) (in the I54 normalization \(\operatorname{Ric}_D=-g\)).  Consequently there is a balanced surgery sequence \(M_j\) (same proportions \(k_j/Q_j\to2/9\), \(\ell_j/Q_j\to7/36\) as the inherited family, over a suitably chosen tower of covers) with

\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}\le \frac{28}{9}+\frac{J_1}{9\pi^2}\le 4-\frac{4\eta}{9},
\]

and, letting the smoothing width tend to zero (one sequence per width), for every \(\epsilon>0\) a sequence with \(\limsup\alpha/h\le 4-\tfrac{8\eta}{9}+\epsilon\).  With the \(X=16\) witness: \(4-8\eta_{16}/9=3.99902484\).  **The coefficient four is not the optimal first-order coefficient of the balanced family over all admissible metrics.**

## 2. The cancellation-free representation (why the Step-9 Arb attempt failed and this one works)

Step 9 evaluated raw spin variables; near the bolt they contain \(y^{-1/2}\), \(y^{-1}\) pieces whose cancellation destroys interval arithmetic.  Here the orthonormal Ricci of \(dt^2+\sum a_i^2\sigma_i^2\) is used in the classical form

\[
R_{00}=-\sum_i\frac{\ddot a_i}{a_i},\qquad
R_{ii}=-\frac{\ddot a_i}{a_i}-\frac{\dot a_i}{a_i}\Big(\frac{\dot a_j}{a_j}+\frac{\dot a_k}{a_k}\Big)+\frac{2\big(a_i^4-(a_j^2-a_k^2)^2\big)}{a_i^2a_j^2a_k^2},
\]

(checked against the Cartan derivation of `perp_cartan_verify.py` by `check_bianchi_ricci_closed_form.py`), with \(h_i=a_i^2\), \(d/dt=2\sqrt G\,d/dx\).  Only products of the form \(\dot a_i\dot a_j/(a_ia_j)=G h_i'h_j'/(h_ih_j)\) and \(\ddot a_i/a_i=G'h_i'/h_i+2Gh_i''/h_i-Gh_i'^2/h_i^2\) occur — never \(\dot a_1^2/a_1^2\) alone.  Writing

\[
y=x-x_0=x_0\ell u\,\varphi(\ell u),\quad \varphi(z)=\frac{e^z-1}{z},\qquad
F=y\hat F,\ G=y\hat G,\ w=y^2\hat w,
\]
\[
\hat F=e^{q_F}+\frac{u^2(10-15u+6u^2)}{\ell\varphi},\quad
\hat G=\Big(1+\frac{(x^2+x_0)u^2(10-15u+6u^2)}{x_0\ell\varphi}\Big)e^{q_G},\quad
\hat w=\frac{\log(1+x)u(10-15u+6u^2)+(1-u)^3C_w}{(x_0\ell\varphi)^2},
\]

all three are entire-type functions of \(u\), positive on \([0,1]\).  The only bolt-singular combinations become regular identities:

\[
\frac{\ddot a_1}{a_1}=2\frac{\hat G}{\hat F}h_1''+h_1'\frac{\hat G'\hat F-\hat G\hat F'}{\hat F^2},\qquad
\frac{\dot a_1\dot a_j}{a_1a_j}=\frac{\hat G}{\hat F}\frac{h_1'h_j'}{h_j},
\]
\[
\frac{(h_2-h_3)^2}{h_1h_2h_3}=\frac{y^3\hat w^2\varphi(w)^2}{\hat F e^w},\qquad
\frac{2(h_2^2-(h_3-h_1)^2)}{h_1h_2h_3}=-\frac{4y\hat w\,\mathrm{shc}(w)}{\hat F}+\frac4x-\frac{2h_1}{x^2e^w},
\]
and the analogue for \(i=3\) (\(\mathrm{shc}(w)=\sinh w/w\)).  The density
\[
\frac{dJ_6}{8\pi^2\,du}=\frac18\,x\,e^{w/2}\sqrt{\hat F/\hat G}\;\sum_a(R_{aa}+6)^2\;\ell x
\]
is therefore holomorphic on a complex neighbourhood of \([0,1]\).  Volume normalization: \(dV=\pi^2\sqrt{h_1h_2h_3/G}\,dx\) (\(\int\sigma_{123}=2\pi^2\)).

**Rigorous integration.** `workspace/scripts/perp_rigorous_enclosure.py` evaluates this density with second-order jets over complex balls (python-flint `acb`), with \(\varphi,\varphi',\varphi''\) from the closed form for \(|z|>1\) and from the Taylor series with explicit tail bound \(r^N/N!\,(1-r/(N+1))^{-1}\) for \(|z|\le1\); \(\sqrt{\cdot}\) and \(\log\) are called with the analytic flag, and division by a ball containing zero returns a non-finite value.  Hence the function satisfies the holomorphic-enclosure contract of Arb's `acb_calc_integrate` (Petras-type Gauss–Legendre with error bounds from the complex ellipse), and `acb.integral` returns a rigorous enclosure.  Runs at 128/192/256 bits and tolerances \(10^{-6}\)–\(10^{-13}\) all give nested enclosures; the loose \(10^{-6}\) run already certified \(J<1\) ([0.9991 ± 3.4e-5]).  Outputs: `workspace/data/perp_collar/rigorous_x0.01_X8_J_d8.json`, `rigorous_x00.01_X16_J_d8.json` (include pointwise checks: at \(u=1\) all \(R_{aa}=-6\) to \(10^{-14}\); at \(u=0\) the values are finite with \(R_{00}=R_{11}=-206.2910940\), \(R_{22}=R_{33}=193.5719039\), the symmetry expected at a smooth bolt).  Consistency: \(J-P\) agrees with the scalar ball; the floating values of three independent codes (local coordinate curvature, local spin formula, peer's import-free reconstruction 0.9991162431353) lie inside the ball.

## 3. Admissibility of the frozen profile

* *Positivity:* \(1-S=(1-u)^3(1+3u+6u^2)\) and \(10-15u+6u^2>0\), so \(0\le S\le1\) on \([0,1]\); hence \(\hat F\ge e^{q_F}>0\), \(\hat G>0\), \(h_2=x>0\), \(h_3>0\).
* *Bolt:* \(t=\int dx/(2\sqrt G)\) gives \(y=\hat G(0)t^2+O(t^4)\), \(a_1^2=yF̂=\hat F(0)\hat G(0)t^2+\dots=t^2+O(t^4)\) because \(q_F(0)+q_G(0)=0\) exactly; \(a_2^2,a_3^2\) are smooth in \(t^2\) and \(a_2^2-a_3^2=x(1-e^w)=O(t^4)\) times a smooth function of \(t^2\), the weight-four condition for the \(\sigma_2,\sigma_3\) plane under the Hopf circle.  All profile functions are real-analytic in \(y\) near \(0\) (through \(u=\ell^{-1}\log(1+y/x_0)\)).  These are the standard smoothness conditions at a Hopf bolt with full fibre period (\(a_1'(0)=1\)); the Step 7 bolt expansion confirmed them.
* *Topology/orientation:* the circle generated by the \(\sigma_1\)-dual field is conjugate in \(SU(2)\) to the \(\sigma_3\) one by right translation, which is isotopic to the identity on \(S^3\).  Hence the perpendicular cell is oriented-diffeomorphic rel boundary to the aligned Burns blow-up \(D\#\overline{\mathbb{CP}}^2\): \(k=1,\ell=0,q=1\) in I54 (1.1)–(2.3).
* *Collar:* each deviation \(d_F=F-x=(x-x_0)(e^{q_F}-1)-x_0(1-S)\), \(d_G=G-(x+x^2)=(x+x^2)(e^{q_G}-1)-(x^2+x_0)(1-S)e^{q_G}\), \(d_w=w-\log(1+x)=-\log(1+x)(1-S)+u^2(1-u)^3C_w\) is analytic on a neighbourhood of \([x_0,X]\) and vanishes to order three at \(X\).
* *Normalization:* \(\tilde g=6g\) has \(\operatorname{Ric}=-\tilde g\) on the collar and \(\int|\operatorname{Ric}_{\tilde g}+\tilde g|^2_{\tilde g}dV_{\tilde g}=J_6(g)\).  The collar radius in \(\operatorname{Ric}=-g\) units is \(\sqrt6\,\operatorname{arsinh}\sqrt X\approx4.32\).

## 4. Smoothing lemma (analytic; no second interval computation needed)

Fix \(\chi\in C^\infty(\mathbb R)\), \(\chi=1\) on \([1,\infty)\), \(\chi=0\) on \((-\infty,1/2]\), and for \(0<\delta<(X-x_0)/2\) put \(\chi_\delta(x)=\chi((X-x)/\delta)\).  Let \(g_\delta\) be defined by \(F_\delta=x+\chi_\delta d_F\), \(G_\delta=x+x^2+\chi_\delta d_G\), \(w_\delta=\log(1+x)+\chi_\delta d_w\).  Then:

1. \(g_\delta=g\) for \(x\le X-\delta\) (bolt unchanged) and \(g_\delta\) is exactly CH for \(x\ge X-\delta/2\); \(g_\delta\) is \(C^\infty\) everywhere (analytic data times a smooth cutoff on \((x_0,X)\), exact CH beyond).
2. On \(B_\delta=[X-\delta,X]\): \(|d^{(k)}|\le C(X-x)^{3-k}\le C\delta^{3-k}\) and \(|\chi_\delta^{(k)}|\le C_\chi\delta^{-k}\), so \(\|g_\delta-g_{CH}\|_{C^2(B_\delta)}+\|g-g_{CH}\|_{C^2(B_\delta)}\le C'\delta\).  For \(\delta\) small, \(F_\delta,G_\delta,h_{3,\delta}\ge X/2\) on \(B_\delta\) (positivity), and since \(\operatorname{Ric}+6g\) is a smooth function of the 2-jet vanishing at the CH jet, \(|\operatorname{Ric}+6g|\le C''\delta\) on \(B_\delta\) for both metrics.
3. Therefore \(|J_6(g_\delta)-J_6(g)|\le 2C''^2\delta^2\operatorname{Vol}(B_\delta)=O(\delta^3)\to0\).

Choose \(\delta\) with this error \(\le 8\pi^2\eta/2\): \(J_6(g_\delta)\le8\pi^2(1-\eta/2)\).  Constants depend only on the frozen profile.  (Directly attaching the \(C^2\) profile is also already a \(W^{2,\infty}\) metric with the stated energy; the smoothing is only needed for the smooth class \(\mathscr G(M)\).)

## 5. Global transfer

I54 §2: inserting the single-blowup cell in \(k\)-sites and treating the \(\ell\) handle surgeries by the inherited shrinking construction gives, with \(k_j/Q_j\to2/9\), \(4\ell_j/Q_j\to7/9\),
\[
\mathcal E(g_j)/h_j\to \frac{2}{9}\frac{J_1}{2\pi^2}+\frac79\cdot\frac{8\pi^2}{2\pi^2}=\frac{28}9+\frac{J_1}{9\pi^2},
\]
and \(J_1=8\pi^2(1-\epsilon_0)\) gives \(4-8\epsilon_0/9\).  The fixed buffered ball of radius \(r\) (\(\approx4.32\) plus buffer) is supplied as in Step 9: in a lattice \(\Gamma\) only finitely many \(\gamma\ne1\) have \(d(p,\gamma p)\le 2r\); residual finiteness gives finite index \(\Gamma_*\) avoiding them; covers inside \(\Gamma_*\) contain a number of disjoint lifts proportional to \(A_j\gg Q_j\).  The statement is existential: a balanced sequence over a suitably chosen tower, not every preassigned cover tower.

## 6. Meaning inside the programme

* The inherited all-metric lower theory is unaffected: the whole-AE threshold (Step 5) and aligned diagonal/Kähler cell bounds hold in their regimes; the new cell is a fixed-scale core–background interaction in the \(\omega^\perp\) kernel of \(R^+\) for a negative Kähler–Einstein background (Step 8 response law: first-order critical, second-order cubic compensation, enhanced by a large collar).
* O11 is now reformulated: the optimal (all-metric, best-sequence) balanced first coefficient \(c_*=\inf\limsup\alpha_j/h_j\) satisfies \(c_{\rm inh}\le c_*<4\), where \(c_{\rm inh}>0\) is the inherited actual-field lower constant.  The single-blowup-plus-separated-handle route has the form \(28/9+8\kappa_1/9\), where \(\kappa_1=\inf J_1/(8\pi^2)\) over single-blowup exact-CH cells.  The inherited exact handle-only theorem implies that every pure-handle exact-CH cell satisfies \(J\ge32\pi^2\ell\), with infimum \(32\pi^2\ell\); isolated handle improvement is therefore impossible.  The distinct collective question is whether a mixed \((k,\ell)\) cell is strictly cheaper than its blow-up and pure-handle parts.  For the balanced block this asks whether \(\mathfrak J_{8,7}<8\mathfrak J_{1,0}+224\pi^2\), while a cell coefficient is \(\mathfrak J_{8,7}/(72\pi^2)\).  Open: the single- and multi-blowup infima, mixed-cell nonadditivity, complete large-collar limits, matching lower bounds, and unrestricted global competitors.
* Lower bound side for the general first coefficient remains: \(c\,h\le\alpha\) with inherited \(c\); the positive gap for these families is untouched.

Step 11 independently reviewed the proof, replaced the float-mediated \(\phi\)-tail radius by a pure-Arb bound, and reran the strict certificate.  The review and corrected cost formulation are in `workspace/notes/step11_independent_review_O11_and_mixed_cost.md`; the canonical local certificate is `workspace/data/perp_collar/strict_rigorous_x0.01_X8_J_d8.json`.

## 7. Symbolic verification record

`check_bianchi_ricci_closed_form.py` (task output `workspace/tasks/s10_t11_tool1/stdout.log`): closed-form Ricci minus Cartan Ricci = [0,0,0,0] (exact `sympy.cancel`), and the desingularized rewrites of \(D_1\), \(A_1,A_2,A_3\) have residual 0.  Together with the rigorous `acb.integral` enclosure this makes the energy statement of §1 a computer-assisted theorem whose remaining trust base is (i) Arb/acb_calc_integrate correctness, (ii) the holomorphic-enclosure contract of the integrand code (reviewable, ~150 lines), and (iii) the transcription of the profile formula from `o11_perp_cell.PerpCell` (wpow=2, perpendicular, beta0=0), which is corroborated by agreement with the three floating implementations to \(10^{-11}\).



---

## Source step11_independent_review_O11_and_mixed_cost.md

Original: [sources/Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md](../sources/Sessions/S1003A01/workspace/notes/step11_independent_review_O11_and_mixed_cost.md)

# Step 11 — Independent review of the subthreshold cell and the corrected next cost problem

Session S1003A01, Agent4, Execute.

## 1. Review conclusion

The finite-scale perpendicular-cell theorem survives independent review.  For the explicit metric

\[
 g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
 \qquad x_0=10^{-2},\quad X=8,
\]

whose 24 coefficient entries are the exact dyadic rationals represented by the binary64 numbers stored in
`workspace/data/perp_collar/x0.01_X8_J_d8.json`, the strict Arb implementation
`workspace/scripts/perp_rigorous_enclosure.py` now proves

\[
 \frac{J_6(g)}{8\pi^2}
 =\frac1{8\pi^2}\int|\operatorname{Ric}_g+6g|^2dV_g
 \in[0.999116243135324311\pm2.24\times10^{-19}].
\]

The local strict output is
`workspace/data/perp_collar/strict_rigorous_x0.01_X8_J_d8.json`.
It also encloses

\[
 \frac{P}{8\pi^2}=[0.999108702733592648\pm4.57\times10^{-19}],
 \qquad
 \frac{J_6-P}{8\pi^2}=[7.540401731663\times10^{-6}\pm3.79\times10^{-19}],
\]

and the exact decomposition \(J_6=P+(J_6-P)\) is reproduced at a separately split 320-bit integration to radius about \(5.1\times10^{-24}\).

No step of this review found a mathematical defect in the desingularized Ricci formula, the volume normalization, the bolt expansion, the exact-collar smoothing, the topological identification, or the global transfer.  Thus there is a smooth exact-CH-collar ordinary blow-up cell with
\[
 J_1<8\pi^2,
\]
and a balanced sequence over a suitable tower of covers with
\[
 \limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}<4.
\]
This gives a rigorous negative answer to the inherited coefficient-four question O11 in its universal-optimality form.  It does **not** determine the sharp first coefficient.

## 2. What was independently checked

### 2.1 Profile transcription and the strict enclosure

The executable perpendicular profile with `wpow=2`, `beta0=0` is
\[
\begin{aligned}
F&=(x-x_0)e^{q_F}+x_0S(u),\\
G&=\bigl(x-x_0+(x^2+x_0)S(u)\bigr)e^{q_G},\\
w&=\log(1+x)S(u)+u^2(1-u)^3C_w(u),
\end{aligned}
\]
where \(u=\log(x/x_0)/\ell\), \(S=10u^3-15u^4+6u^5\), and \(q_F,q_G\) use degree-seven Chebyshev expansions times \((1-u)^3\).  The derived shift of the constant term in \(q_G\) enforces \(q_F(0)+q_G(0)=0\) exactly.  Direct pointwise comparison against the independent peer reconstruction gave profile differences at five interior points between \(10^{-18}\) and \(3\times10^{-14}\), consistent with binary64 evaluation.

The Step-10 code's only avoidable trust-base caveat was that the Taylor-tail radius for
\(\phi(z)=(e^z-1)/z\) passed through a Python float.  Following the peer stress test, this was replaced locally by a pure-Arb implementation using `abs(z).lower()` and `abs(z).upper()`.  If the ball is separated from zero, the exact quotient formulas are used; otherwise the entire series is used with a rigorous geometric tail, increasing the truncation order if necessary so \(r/(N+1)<1\).  The local rerun exactly reproduced the peer strict result above.  All logarithms and square roots forward Arb's `analytic` flag; division by a ball containing zero returns a nonfinite enclosure and forces subdivision.  Hence the callback satisfies the `acb_calc_integrate` holomorphy contract.

The original JSON `P` and `J` fields are low-order optimization quadrature metadata and do not lie in the final narrow balls.  They play no role in the theorem.  The proof object is the Arb ball string in the strict output.  Similarly, JSON `lower`, `upper`, and `eta_certified` are binary64 convenience fields; rigorous citation should use the ball itself.

There is a documentation error in the header of the peer's `o11_perp_cell.py`: it mentions an extra \(xe^{-w}\) slot.  The executable code, frozen theorem, local enclosure, and independent reconstruction all use precisely \(F,x,xe^w\), as displayed above.

### 2.2 Curvature algebra and normalization

For a diagonal Bianchi-IX metric \(dt^2+\sum a_i^2\sigma_i^2\), with
\(d\sigma_i=2\sigma_j\wedge\sigma_k\), the enclosure uses
\[
 R_{00}=-\sum_i\frac{\ddot a_i}{a_i},\qquad
 R_{ii}=-\frac{\ddot a_i}{a_i}
 -\frac{\dot a_i}{a_i}\left(\frac{\dot a_j}{a_j}+\frac{\dot a_k}{a_k}\right)
 +\frac{2(a_i^4-(a_j^2-a_k^2)^2)}{a_i^2a_j^2a_k^2}.
\]
The symbolic comparison to the independently Cartan-derived tensor gives four zero residuals, and the bolt rewrites \(D_1,A_1,A_2,A_3\) likewise reduce exactly to zero.  Factoring
\[
 y=x-x_0,\qquad F=y\widehat F,\quad G=y\widehat G,\quad w=y^2\widehat w
\]
removes every apparent division by the collapsing direction.  The code then evaluates a holomorphic extension of the real density rather than a non-holomorphic absolute square.

With \(\int\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2\),
\[
 dV=\pi^2 x e^{w/2}\sqrt{\widehat F/\widehat G}\,dx,
\]
so the coded factor
\[
 \frac18xe^{w/2}\sqrt{\widehat F/\widehat G}\,\ell x\,du
\]
is exactly \(dV/(8\pi^2)\).  Thus the enclosed quantity is \(J_6/(8\pi^2)\), not a surrogate.

### 2.3 Bolt, topology, and smoothing

At the bolt,
\[
 F=f_1y+O(y^2),\quad G=g_1y+O(y^2),\quad f_1g_1=1,\quad w=O(y^2).
\]
For \(dt=dx/(2\sqrt G)\), this gives
\[
 F=t^2+O(t^4),\qquad x-xe^w=O(t^4).
\]
Under the chosen Maurer–Cartan normalization the collapsing Hopf circle has period \(2\pi\), so the first equation is the full-period no-cone condition.  The normal two-plane has isotropy weight two and its traceless quadratic part weight four, making the \(O(t^4)\) anisotropy exactly the smoothness condition.  The bolt is an ordinary \((-1)\)-sphere.

The circles dual to \(\sigma_1\) and \(\sigma_3\) are conjugate Hopf circles of the same handedness.  A conjugating rotation near the bolt can be deformed to the identity through the free-orbit region, producing an orientation-preserving diffeomorphism that is the identity on the outer collar.  Hence the perpendicular cell is
\[
 D\#\overline{\mathbb{CP}}^{\,2}
\]
rel outer boundary; it is not an oppositely oriented \(\mathbb{CP}^2\) cell.

At \(X\), each deviation from CH vanishes to third order.  If a width-\(\delta\) flat cutoff is applied, its two-jet differs from CH by \(O(\delta)\) on a region of volume \(O(\delta)\).  Since \(\operatorname{Ric}+6g\) vanishes at the CH two-jet,
\[
 |J_6(g_\delta)-J_6(g)|=O(\delta^3).
\]
For sufficiently small fixed \(\delta\), the metric is positive, smooth, unchanged near the bolt, and exactly CH on an outer collar.  The strict frozen margin is therefore preserved.  No second interval integration is needed.

### 2.4 Scaling, covers, and transfer

For \(\widetilde g=6g\),
\[
 \operatorname{Ric}_{\widetilde g}=-\widetilde g\quad\text{on the collar},
 \qquad
 \int|\operatorname{Ric}_{\widetilde g}+\widetilde g|^2dV_{\widetilde g}=J_6(g),
\]
because a covariant two-tensor norm contributes \(6^{-2}\) and four-dimensional volume contributes \(6^2\).

Residual finiteness supplies a finite cover with the fixed radius-\(\sqrt6\operatorname{arsinh}\sqrt8\) ball and buffer embedded: only finitely many lattice elements move a chosen lift by at most twice that radius, and a finite-index subgroup can avoid all of them.  Any further cover contains a number of disjoint lifted balls proportional to its degree and hence to \(A_j\).  Since \(Q_j=o(A_j)\), this supplies all surgery sites for an existential balanced sequence.

With \(k_j/Q_j\to2/9\) and \(\ell_j/Q_j\to7/36\), the I54 accounting gives
\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le \frac{28}{9}+\frac{J_1}{9\pi^2}.
\]
For the strict X=8 frozen value \(\eta_8=1-J_6/(8\pi^2)>0.0008837568646756\), a fixed sufficiently small smoothing gives some strict number below four; letting the smoothing widths tend to zero diagonally gives
\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le 4-\frac{8\eta_8}{9}
 <3.999214438342511.
\]
A fixed-width conservative form is \(4-4\eta_8/9<4\).  This statement applies to a suitably chosen cover tower, not every preassigned tower.

## 3. Pure handles are rigid at the local exact-CH level

Step 10 proposed searching for a pure handle cell below \(32\pi^2\ell\).  This is already impossible.

Let
\[
 C=D\#\ell(S^1\times S^3)
\]
carry any smooth metric equal to the \(\operatorname{Ric}=-g\) CH metric on its full outer collar, and put
\[
 J(C)=\int_C|\operatorname{Ric}+g|^2.
\]
Insert one fixed copy into arbitrarily large finite covers with \(c_1^2=A\).  The resulting handle-only manifold has \(h_A=4\ell/A\), and the exact cell formula yields
\[
 \frac{\mathcal E(g_A)}{h_A}\longrightarrow\frac{J(C)}{8\pi^2\ell}.
\]
The inherited all-metric theorem gives
\[
 \alpha(M_A)=\frac{4h_A}{1+h_A},
\]
and \(\alpha(M_A)\le\mathcal E(g_A)\).  Hence
\[
 \frac{J(C)}{8\pi^2\ell}\ge4,
\qquad\boxed{J(C)\ge32\pi^2\ell}.
\]
The inherited equality theory makes the inequality strict for each fixed smooth \(\ell>0\) cell, while shrinking handle cores approach the value.  Thus
\[
 \inf J(C)=32\pi^2\ell
\]
and the infimum is not attained for \(\ell>0\).

An equivalent relative identity is
\[
 J(C)-32\pi^2\ell
 =\frac{S_C-16d}{12}+4B_C+\frac14\int_C(s+4)^2,
\]
where \(S_C=\int_Cs^2\), \(B_C=\int_C|W^-|^2\), and \(d=\operatorname{Vol}(D)\).  Gluing the cell into a CH cover and applying the inherited metricwise scalar inequality gives \(S_C\ge16d\), so every term on the right is nonnegative.

Consequently, the \(28/9\) floor of a construction that treats all handles in separate pure-handle cells is not removable by a better isolated handle ansatz.

## 4. The distinct mixed-cell problem

For
\[
 C=D\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
\qquad q=k+4\ell,
\]
define the unrestricted exact-CH cell cost
\[
 \mathfrak J_{k,\ell}=\inf_C\int_C|\operatorname{Ric}+g|^2,
\]
allowing the outer CH ball radius to vary.  The established facts include
\[
 \mathfrak J_{0,\ell}=32\pi^2\ell,
 \qquad
 \mathfrak J_{1,0}<8\pi^2.
\]
Pure-handle rigidity does **not** imply
\[
 \mathfrak J_{k,\ell}\ge\mathfrak J_{k,0}+32\pi^2\ell.
\]
A connected mixed cell need not split along exact CH collars, and the scalar and Weyl terms belong to the whole metric.

The common relative identity can be written
\[
 J-8\pi^2q
 =\frac{S_C-16d}{12}+\frac14\int_C(s+4)^2
 -4\left(\frac{2d}{3}-W_C\right),
\]
with
\[
 \frac{2d}{3}-W_C=12\pi^2k-B_C\le12\pi^2k.
\]
Thus handles add topological cost but supply no independent positive self-dual-Weyl-depletion budget; only blow-ups do.  A mixed saving, if present, must arise because handle topology changes how the same metric uses the blow-up-funded Weyl depletion and pays its scalar/Ricci cost.  This is collective nonadditivity, not isolated handle improvement.

For the balanced proportions the smallest integer mixed block is \((k,\ell,q)=(8,7,36)\).  Its coefficient is
\[
 c_{\rm mix}=\frac{\mathfrak J_{8,7}}{72\pi^2}.
\]
The separated construction costs
\[
 \mathfrak J_{\rm sep}=8\mathfrak J_{1,0}+224\pi^2.
\]
The interaction question is therefore
\[
 \boxed{\mathfrak J_{8,7}<8\mathfrak J_{1,0}+224\pi^2\ ?}
\]
More generally one should study subadditivity and the large-block limit of \(\mathfrak J_{k,\ell}\).  To beat the separated construction's absolute \(28/9\) floor one would need the much stronger inequality
\[
 \mathfrak J_{8,7}<224\pi^2.
\]
This remains distinct from both the single-blow-up infimum \(\mathfrak J_{1,0}\) and unrestricted global competitors not assembled from fixed exact-CH cells.

## 5. Corrections to the Step-10 synthesis

1. The statement “can handle cells be improved below \(32\pi^2\)” must be deleted as an open route.  The answer is no for every pure-handle exact-CH cell.
2. The original float-based Taylor radius has been replaced in the local proof script by a pure-Arb radius; the strict output is now the canonical certificate.
3. The frozen profile is an exact dyadic-coefficient metric, not an exact-decimal-rational metric.
4. The narrow Arb ball does not contain the low-order `P` and `J` metadata stored by the optimizer; those numbers are not proof inputs.
5. The peer high-precision output reruns the regularized enclosure implementation.  Genuine formula independence comes from the peer JAX spin/transgression reconstruction, which matches the strict center to about \(10^{-15}\).
6. The O11 result changes the sharp question rather than completing the broader Einstein-gap programme.  Matching lower bounds, mixed-cell cost, multi-blow-up interaction, unrestricted competitors, degeneration, O10, and fixed-manifold attainment remain active.



---

## Source step13_pair_overlap_interaction.md

Original: [sources/Sessions/S1003A01/workspace/notes/step13_pair_overlap_interaction.md](../sources/Sessions/S1003A01/workspace/notes/step13_pair_overlap_interaction.md)

# Step 13 — Two certified cells with overlapping CH tails: a phase-locked weight-two interaction

Session S1003A01, Agent2, Execute.  Builds on the certified frozen perpendicular cell
(`data/perp_collar/x0.01_X8_J_d8.json`, strict enclosure `strict_rigorous_x0.01_X8_J_d8.json`,
\(J_6/(8\pi^2)=0.999116243135324311\ldots\)) and the Step-12 two-blow-up programme
\(\mathfrak J_{8,7}\le 4\mathfrak J_{2,0}+224\pi^2\).

## 1. The trial metric and the exact localisation identity

Normalisation \(\operatorname{Ric}_{CH}=-6g\) (holomorphic sectional curvature \(-4\)); ball model
\(g_B=\operatorname{Re}\big[|dz|^2/(1-|z|^2)+|\langle dz,z\rangle|^2/(1-|z|^2)^2\big]\), so
\(r(0,z)=\operatorname{artanh}|z|\).  The frozen cell lives on \(x_0\le x\le X=8\), \(x=\sinh^2 r\), and
on the region \(x>x_0\) it is written over CH as \(g_1=g_B+h_1\) with \(h_1\) diagonal in the CH
orthonormal coframe \((dr,\ \sinh r\,\sigma_{\rm bolt},\ \sinh r\,\sigma_{\rm contact},\ \sinh r\cosh r\,\sigma_{\rm fibre})\):
\[
 g_1=\sum_s\lambda_s(r)\,(\hat e^s)^2,\qquad
 \lambda=\Big(\frac{x+x^2}{G},\ \frac{F}{x},\ 1,\ \frac{e^{w}}{1+x}\Big),
\]
and \(h_1=0\) for \(r\ge\rho=\operatorname{asinh}\sqrt X=1.762747\).  In ball coordinates the cell
frame at \(z\) is \((z,\ jz,\ kz,\ iz)\) (quaternionic \(C^2=\mathbb H\)), the fibre being \(J\nu=iz\).
The second cell is \(g_2=(\varphi_a\circ L_\theta)^*\)-transport of the same cell, \(\varphi_a\) the
holomorphic involution exchanging \(0\) and \(a=(\tanh d,0)\) (the geodesic symmetry of the midpoint)
and \(L_\theta z=e^{i\theta}z\), which rotates the cell's contact frame by \(2\theta\).  Modulo the
symmetries of the two cells, \((d,\theta)\) parametrise all relative placements.

Trial metric: \(g_{12}=g_B+h_1+h_2\).  If \(d\ge\rho+r_0+\) margin, \(r_0=\operatorname{asinh}\sqrt{x_0}\),
each tail vanishes near the other bolt, so \(g_{12}\) is a \(C^{2,1}\) metric on \(D\#2\overline{\mathbf{CP}}{}^2\)
with an exact CH exterior; the Step-10 \(O(\delta^3)\) cutoff lemma applies verbatim near each sphere
piece (the second tail is smooth there), so smoothing changes \(J\) by \(o(1)\).  Outside the lens
\(L=B_\rho(0)\cap B_\rho(a)\) the metric coincides with one cell or with CH, hence exactly
\[
 J(g_{12})-J(g_1)-J(g_2)=\int_L\Big(|E(g_{12})|^2dV_{g_{12}}-|E(g_1)|^2dV_{g_1}-|E(g_2)|^2dV_{g_2}\Big),
 \qquad E=\operatorname{Ric}+6g,
\]
with quadratic part \(2\int_L\langle E(g_1),E(g_2)\rangle_{g_B}dV_B\) and a remainder that is cubic
in the tail data.  Overlap depth \(w=2\rho-d\); the admissible range is \(0<w<\rho-r_0\approx1.66\).

## 2. Phase structure (exact at quadratic order)

The cell defect is diagonal, \(E={\rm diag}(E_0,E_1,E_2,E_3)\) (radial, bolt slot, contact slot,
fibre).  Under \(L_\theta\) only the contact block moves; writing \(m=(E_1+E_2)/2\), \(d=(E_1-E_2)/2\),
the traceless part \(d\) has weight two in the rotation angle \(2\theta\), i.e. weight four in \(\theta\).
Hence the quadratic interaction is exactly
\[
 I(w,\theta)=I_0(w)+\operatorname{Re}\big(I_4(w)e^{4i\theta}\big),\qquad
 \min_\theta I=I_0-|I_4|,
\]
and \(I_0\) is the pairing with the phase average (\(U(2)\)-invariant part) of the second defect.
So a strict saving exists for some phase as soon as \(|I_4|>I_0\), whatever the sign of \(I_0\).

## 3. Computation

`scripts/pair_overlap_trial.py` builds \(g_B,h_1,h_2\) explicitly in \(\mathbb R^4\) and computes all
Ricci tensors by forward-mode autodiff of the coordinate metric (no symmetry used).
`scripts/pair_overlap_check.py`: \(|\operatorname{Ric}(g_B)+6g_B|\le5\times10^{-15}\); the autodiff
\(|E(g_1)|^2\) equals the Bianchi-IX value \(\sum_a(R_{aa}+6)^2\) of `FrozenCell` at
\(r=0.3,\dots,1.75\) to 12–14 digits (e.g. 26.14499751412 vs 26.14499751412 at \(r=0.3\)).  Lens
integrals use scrambled Sobol points (\(2^{15}\) per run) in cell-1 polar coordinates; two seeds
at \(w=1.5\) differ by 0.5%.  Data: `data/pair_overlap/sweep_X8/w*_s0.json`, table
`data/pair_profile/pair_overlap_table_X8.csv`, figure `figures/pair_overlap_interaction_X8.png`.

| \(w\) | \(\Delta J/8\pi^2\), \(\theta=0\) | \(\theta=\pi/8\) | \(\theta=\pi/4\) | best saving | \(\int_L|E_1|^2/8\pi^2\) | max \(|\Delta J-{\rm quad}|\) |
|---|---|---|---|---|---|---|
| 0.1 | \(3.74\times10^{-10}\) | \(1.70\times10^{-10}\) | \(-3.26\times10^{-11}\) | \(3.3\times10^{-11}\) | \(3.4\times10^{-10}\) | \(3\times10^{-15}\) |
| 0.4 | \(4.43\times10^{-8}\) | \(-3.7\times10^{-9}\) | \(-5.17\times10^{-8}\) | \(5.2\times10^{-8}\) | \(5.8\times10^{-8}\) | \(9\times10^{-12}\) |
| 0.6 | \(1.446\times10^{-7}\) | \(-1.0\times10^{-9}\) | \(-1.467\times10^{-7}\) | \(1.5\times10^{-7}\) | \(2.1\times10^{-7}\) | \(3\times10^{-10}\) |
| 0.8 | \(1.59\times10^{-7}\) | \(1.0\times10^{-8}\) | \(-1.39\times10^{-7}\) | \(1.4\times10^{-7}\) | \(6.2\times10^{-7}\) | \(3\times10^{-9}\) |
| 1.0 | \(-2.95\times10^{-7}\) | \(-2\times10^{-9}\) | \(2.95\times10^{-7}\) | \(3.0\times10^{-7}\) | \(2.8\times10^{-6}\) | \(7\times10^{-9}\) |
| 1.2 | \(-1.75\times10^{-6}\) | \(1.9\times10^{-8}\) | \(1.80\times10^{-6}\) | \(1.8\times10^{-6}\) | \(1.8\times10^{-5}\) | \(2\times10^{-8}\) |
| 1.4 | \(-5.29\times10^{-6}\) | \(5.6\times10^{-8}\) | \(5.43\times10^{-6}\) | \(5.3\times10^{-6}\) | \(1.7\times10^{-4}\) | \(5\times10^{-8}\) |
| 1.6 | \(-1.2455\times10^{-5}\) | \(9.6\times10^{-8}\) | \(1.283\times10^{-5}\) | \(1.25\times10^{-5}\) | \(6.1\times10^{-3}\) | \(6\times10^{-8}\) |

The trial metric stayed positive (smallest coordinate eigenvalue 0.62 at \(w=1.6\)).

## 4. What the numbers say

1. **The interaction is almost purely weight-two.**  \(I_0\approx\Delta J(\pi/8)\) is \(10^{-2}\) of the
   amplitude; \(\Delta J(0)\approx-\Delta J(\pi/4)\).  The reason is visible in the radial
   decomposition (`scripts/pair_defect_profile.py`, `data/pair_profile/defect_profile_X8*`,
   `figures/pair_defect_profile_X8.png`): for \(r>1\) the weight-two energy \(2\int d^2\) is
   \(1.80\times10^{-4}\) against \(1.87\times10^{-5}\) for the invariant part.  The optimised cell's
   tail defect is a perpendicular-plane anisotropy — the \(\omega^\perp\) channel of Steps 7–8 —
   and the scalar/fibre components are nearly paid off.
2. **The preferred phase flips with depth.**  \(d(r)\) changes sign once, at \(r=1.297\).  The lens
   is centred near \(r=\rho-w/2\), which crosses \(1.297\) at \(w\approx0.93\); the observed switch of
   \(\operatorname{Re}I_4\) between \(w=0.8\) and \(1.0\) matches.
3. **Near tangency the pair repels.**  `scripts/pair_boundary_jet.py`
   (`data/pair_overlap/boundary_jet_X8.json`): the one-sided collar jet of \(E\) is
   \(e=(0.04889,\,0.09456,\,0,\,-0.04566)\) per unit geodesic depth (the contact slot vanishes because
   \(h_2\equiv x\)).  As \(w\to0\), \(I\sim 2\langle e,R_\theta e\rangle\int_L(\rho-r_1)(\rho-r_2)\sim c\,w^{9/2}\),
   with \(\min_\theta\langle e,R_\theta e\rangle=e_0^2+e_3^2+2e_1e_2=0.00448>0\), and the cubic remainder is
   \(O(w^{15/2})\).  So the collective saving comes from the interior structure of the tail, not from
   the collar jet; the crossover lies below \(w=0.1\).
4. **Size.**  The best saving, \(1.25\times10^{-5}\cdot8\pi^2\) at \(w=1.6\), is 1.4% of the certified
   single-cell deficit \(\eta_8=8.84\times10^{-4}\) and 0.2% of the Cauchy–Schwarz scale
   \(\int_L|E_1|^2\).  The nonlinear remainder is \(<0.5\%\) of the saving.  If certified it would give
   \(J_{20}\le2\overline J_{10}-1.2\times10^{-5}\cdot8\pi^2\) and lower the balanced coefficient by
   \(\frac49\times1.2\times10^{-5}\approx5\times10^{-6}\) through
   \(\mathfrak J_{8,7}\le4\mathfrak J_{2,0}+224\pi^2\).  The \(X=8\to16\) single-cell improvement
   (\(\Delta\eta=2.1\times10^{-4}\)) is seventeen times larger.

## 5. Status and consequences

* **Status.**  Numerical: QMC lens integrals of autodiff curvature, double precision, seed variation
  0.5%, sign margin about 200 standard errors at \(w\ge1.2\).  Not a certificate.  A certificate would
  need (i) a validated 4D lens integral of the quadratic term, which involves only the two radial
  defect profiles (already Arb-enclosable) and explicit CH frame-transport algebra, and (ii) an explicit
  pointwise bound for the cubic remainder in terms of \(|h|,|\nabla h|,|\nabla^2h|\) on \(L\).
* **Strict non-additivity of explicit constructions is real** in negative curvature, and its channel
  is identified: phase-locking of the weight-two perpendicular anisotropy of the tails.  The sum
  \(I_0\) (the orientation-averaged interaction) is essentially zero, so a random-phase cluster is
  additive to \(10^{-7}\); only phase-aligned neighbours save.
* **Quasi-additivity mechanism.**  An optimised cell puts \(>99.9\%\) of its defect inside \(r<0.8\);
  frozen-tail interaction is bounded by the tail energies and is tiny.  Collective savings comparable to
  \(\eta\) therefore require (a) many phase-aligned neighbours per cell (hyperbolic packing at
  \(d\approx1.9\) allows many; frustration of the phase field around triangles is the open
  question), (b) a jointly relaxed exterior, or (c) genuine core–core cooperation at distances below
  \(\rho+r_0\), where the tail representation breaks and a cohomogeneity-two (e.g. toric, two
  iterated blow-ups at a \(T^2\)-fixed point) ansatz is needed.
* The single-cell infimum \(\kappa_1=\mathfrak J_{1,0}/8\pi^2\) remains the dominant lever for the
  upper bound; S1003A02's Step-13 finding (diagonal \(SU(2)\) Einstein fillings of
  \(D\#\overline{\mathbf{CP}}{}^2\) are ACH with Rossi-sphere infinity, ratio \(\ge2.196\), never
  standard) bears directly on whether \(\kappa_1\) is bounded away from zero in the class.



---

## Source step14_large_collar_resistance_and_cluster_budget.md

Original: [sources/Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md](../sources/Sessions/S1003A01/workspace/notes/step14_large_collar_resistance_and_cluster_budget.md)

# Step 14 — Large-collar continuation, quantitative resistance, and a many-cell energy ceiling

## 1. What was tested

The pair-tail experiment from Step 13 is a genuine numerical interaction between two **fixed witnesses**, but its deepest continuation is not to multiply its best pair value by a coordination number. Two questions were separated:

1. How much cost can any cluster remove while geometrically protected cores remain unchanged?
2. Does increasing the exact-CH collar radius reveal an inexpensive long drift toward the perpendicular ACH Einstein trajectory, or a finite positive resistance to the standard conformal infinity?

The functional is in the \(\operatorname{Ric}=-6g\) normalization,
\[
 J_6(g)=\int |\operatorname{Ric}+6g|^2,\qquad
 P(g)=\int |\operatorname{Ric}^{\circ}|^2,
\]
reported in units of \(8\pi^2\).

## 2. A cluster bound that precedes packing

Let \(g_i\) be isolated exact-collar cells and choose pairwise disjoint protected cores \(C_i\), on which a cluster metric is required to agree with \(g_i\). Positivity of the defect density gives the exact inequality
\[
 J(g_{\rm cluster})\ge \sum_i J(g_i;C_i).
\]
Therefore
\[
 \boxed{\sum_iJ(g_i)-J(g_{\rm cluster})
 \le \sum_i J(g_i;M_i\setminus C_i).}\tag{2.1}
\]
This bound counts each adjustable exterior once, independent of how many neighbours it meets. At quadratic order the same fact is
\[
 \int\Big|\sum_iAh_i\Big|^2\ge0,
\]
so one cannot minimize every pair cross term independently and add the minima.

`scripts/cell_exterior_budget.py` computes the right side for the frozen radial cells. For the certified \(X=8\) witness, choosing the largest Step-13 overlap \(w=1.6\) protects only
\[
 r<\rho-w=0.16275,
\]
not the weak tail \(r<1\). The adjustable one-cell energy is
\[
 J(r>0.16275)/(8\pi^2)=0.15106,
\]
whereas the observed pair saving is only \(1.25\times10^{-5}\). For a pair, (2.1) therefore permits as much as \(0.30213\); it is far too weak to constrain ordinary finite-coordination packing in this deep-overlap geometry. Thus the \(r>1\) value \(1.99\times10^{-4}\) cannot be used to dismiss that experiment, but neither may the pair saving be multiplied freely. If instead one explicitly protects \(r<1\), the adjustable energy is \(1.99\times10^{-4}\) per cell.

The bound is deliberately geometric: its force depends on where the cores are frozen. It supplies a universal ceiling for frozen-core clustering but says nothing comparable once core regions are jointly reoptimized. The tabulated exterior values are numerical radial quadratures (the \(X=8\) total differs from the stored cost by \(2.21\times10^{-7}\)); the inequality itself is exact.

## 3. The pair effect weakens for the better \(X=16\) cell

A second 4D autodiff run used the independently validated \(X=16\) profile. At overlap depths \(w=1.2,1.4,1.6\), the best phases gave
\[
 \Delta J/(8\pi^2)=-1.91\times10^{-7},\ -6.11\times10^{-7},\ -1.54\times10^{-6},
\]
respectively (`data/pair_overlap/sweep_X16_check.json`). The weight-four phase law persists, but the \(w=1.6\) saving is eight times smaller than for \(X=8\). The nonlinear difference from the quadratic term remains about \(10^{-8}\), and the sampled metrics remain positive.

This confirms the structural interaction but changes its role: optimizing a larger single cell suppresses separated frozen-tail cooperation rather than amplifying it. Certification of the pair sign would be mathematically reusable, but is not the principal lever on the upper coefficient.

## 4. Physical continuation to larger collars

The old `perp_collar_scan.py` starts from zero and stretches the transition across the whole logarithmic interval. To test the true monotone cell problem, `scripts/perp_collar_continue.py` was introduced. It first extends the previous optimized cell by an exact CH annulus, projects that same physical metric into a higher-degree Chebyshev basis on the larger interval, and then optimizes. The projection is not energy preserving at finite degree, so it is only an initialization; the final profile is evaluated and enclosed independently by the cancellation-free Arb code.

The continuation produced:

| outer \(X\) | degree | \(J_6/(8\pi^2)\), rigorous enclosure | certified \(\eta=1-J\) |
|---|---:|---:|---:|
| 8 | 8 | \(0.999116243135324311\pm2.24\times10^{-19}\) | \(0.0008837568646756\) |
| 16 | 8 | \(0.99890294372\) (prior enclosure) | \(\approx0.0010970563\) |
| 32 | 12 | \(0.99873676987\pm7.43\times10^{-12}\) | \(0.0012632301285\) |
| 64 | 16 | \(0.99870276448\pm6.15\times10^{-12}\) | \(0.0012972355165\) |

The new authoritative outputs are:

- `data/perp_collar/continued_X16_to_X32_J_d12.json`
- `data/perp_collar/rigorous_continued_X16_to_X32_J_d12.json`
- `data/perp_collar/continued_X32_to_X64_J_d16.json`
- `data/perp_collar/rigorous_continued_X32_to_X64_J_d16.json`.

The corresponding \(P\) values are rigorously below one as well:
\[
 P_{32}/(8\pi^2)=0.99873214738\pm8.39\times10^{-12},\qquad
 P_{64}/(8\pi^2)=0.99870008590\pm7.30\times10^{-12}.
\]
The same analytic positivity, bolt smoothness and exact-collar smoothing argument used for the \(X=8\) witness applies to these profiles. Hence the \(X=64\) cell improves the existential balanced-sequence construction to
\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le 4-\frac{8\eta_{64}}9+\varepsilon
 <3.998846902+\varepsilon,
\]
for arbitrarily small smoothing loss \(\varepsilon>0\). This remains an upper construction, not the unrestricted optimum.

The improvement increments in \(\eta\) are approximately \(2.13,1.66,0.34\times10^{-4}\) from \(8\to16\to32\to64\). This is evidence of saturation near a positive cost, not proof of the limit or of optimality within the ansatz. The \(X=64\) optimizer stopped with gradient infinity norm \(3.2\times10^{-3}\), so further basis/optimization work could still lower it.

## 5. Fixed-radius geometry suggests a complete asymptotic profile

`scripts/large_collar_profile_compare.py` compares the metrics at fixed physical CH radii. For \(X=8,16,32,64\), the ratios of the four diagonal coefficients to CH and the defect shell densities stabilize on compact radii. Representative examples:

- At \(r=0.3\), the radial ratio is about \(1.095,1.093,1.092,1.092\), while the collapsing-slot ratio is about \(0.862,0.861,0.860,0.860\).
- At \(r=1.0\), the radial ratio is about \(1.0166,1.0165,1.0168,1.0171\), and the two nontrivial tangential ratios are near \(0.98\)--\(0.99\).
- At \(r=1.6\), the \(X=32,64\) ratios differ only at roughly \(10^{-4}\), and the shell energy is \(5.48\times10^{-5}\) versus \(4.77\times10^{-5}\).

The data are in `data/perp_collar/large_collar_profile_compare.json`. They support compact convergence toward a complete finite-energy diagonal CH-asymptotic metric rather than a transition that simply runs outward. This remains numerical: coercive compactness and the asymptotic mode are not yet proved.

The tail decomposition also changes systematically. For the \(X=32\) and \(X=64\) profiles, the energy beyond \(r=1\) is dominated by the perpendicular weight-two mode:
\[
 (E_{\rm inv},E_{\rm wt2})_{r>1}
 =(1.21\times10^{-5},3.03\times10^{-4}),
 \quad(8.95\times10^{-6},2.65\times10^{-4}).
\]
Thus the same channel responsible for pair phase-locking is the slowly decaying single-cell mode, but its integrated cost stays finite.

## 6. The Rossi neutral mode has finite positive ACH resistance

The peer Einstein shooting gives perpendicular ACH Einstein fillings with Rossi ratio \(\rho\gtrsim2.196\), while exact CH has \(\rho=1\). Put
\[
 q=\log(a_2/a_3),\qquad \Delta=\log(2.196)=0.7866375.
\]
Near an ACH trajectory the neutral mode satisfies schematically
\[
 q''+4q'=f,
\]
where \(f\) is forced by trace-free Ricci defect. The essential point for a calibration inequality is the weight. In a noncollapsed ACH end, orbit volume grows like \(e^{4t}\), so the reduced action is
\[
 \mathcal A_T(q)=\int_0^T e^{4t}(q''+4q')^2dt,
\quad q(0)=0,\ q(T)=\Delta,\ q'(0)=q'(T)=0.\tag{6.1}
\]
`scripts/neutral_mode_resistance.py` solves this exactly. The minimum is exactly
\[
 \inf\mathcal A_T=
 \frac{\Delta^2}{(1-e^{-4T})/64-T^2e^{-4T}/[4(1-e^{-4T})]}
 \longrightarrow64\Delta^2=39.6031,\tag{6.2}
\]
already within \(2.3\%\) at \(T=2\) and \(3\times10^{-5}\) at \(T=4\). In contrast, the same problem **without** the ACH weight has minimum tending to zero (numerically \(0.639\) by \(T=16\), with \(\sim T^{-1}\) behavior). The exact output is `data/perp_collar/neutral_mode_resistance.json`. The script's field `resistance` is the compliance \(\Delta^2/\mathcal A_T\to1/64\); the energetic coefficient is \(64\).

The quantity directly differentiated by the forcing is the flux-corrected mode
\[
 \Phi=q+\frac14q',\qquad \Phi'=\frac14(q''+4q').
\]
The clamped endpoint conditions make \(\Delta\Phi=\Delta q\), but a free entrance slope changes this conclusion: \(q(t)=\Delta(1-e^{-4t})\) solves the homogeneous equation with zero action and nonzero initial slope. Hence a long noncollapsed ACH transition does not destroy resistance only when the volume normalization and the relevant boundary flux are controlled. A quantitative cell lower bound can fail through collapse of the orbit-volume coefficient, departure from the ACH regime, concentration in another mode, or loss of entrance-slope control. This is the precise missing content in an invariant estimate
\[
 |\Delta\Phi|^2\le \frac{P}{8\pi^2}R_\Phi.
\]
The endpoint ratio mismatch alone is not enough; one needs a uniform **upper** bound on the actual compliance \(R_\Phi\), or equivalently a lower comparison of the true action with (6.1), together with a nonzero flux-corrected mismatch.

## 7. What this changes

The evidence now joins three previously separate facts:

1. Exact diagonal Einstein fillings miss standard CH infinity by a finite Rossi displacement (peer computation).
2. Larger exact-collar competitors appear to converge on compact sets and their costs saturate near \(J/(8\pi^2)\approx0.9987\), rather than tending rapidly toward zero.
3. The reduced neutral mode has a finite positive action for arbitrarily long ACH transitions because of the \(e^{4t}\) volume weight.

Together they support a quantitative diagonal coercivity programme: prove that every low-cost cell enters a uniformly noncollapsed ACH tube; compare its neutral-mode forcing with \(|\operatorname{Ric}^{\circ}|\); control the entrance flux; then use the Rossi endpoint separation and the weighted action. For an actual diagonal metric, if \(W=a_1a_2a_3\) and \(q=\log(a_2/a_3)\), subtracting the \(22\) and \(33\) Ricci equations yields
\[
 (Wq')'=W(V-E),\qquad
 V=\frac{4(a_2^2-a_3^2)(a_2^2+a_3^2-a_1^2)}{W^2},
\]
where \(E=(\operatorname{Ric}^{\circ})_{22}-(\operatorname{Ric}^{\circ})_{33}\) and \(|\operatorname{Ric}^{\circ}|^2\ge E^2/2\). Thus the nonlinear calibration must also control the potential term \(V\), not merely replace \(W'/W\) by four. What is still missing is decisive and explicit: low-cost compactness into the tube, a uniform orbit-volume comparison, bounds for this potential contribution, entrance-flux control, and rigorous separation of the Einstein filling map from \(\rho=1\). Without these, the numerical Einstein nonexistence statement does not imply a positive least defect.

The pair interaction remains a reusable phase mechanism, but the large-collar/resistance connection now bears more directly on a matching lower theory for \(\mathfrak J_{1,0}\) and on degeneration of minimizing cells.



---

## Source step15_bolt_neutral_transport_and_area_branch.md

Original: [sources/Sessions/S1003A01/workspace/notes/step15_bolt_neutral_transport_and_area_branch.md](../sources/Sessions/S1003A01/workspace/notes/step15_bolt_neutral_transport_and_area_branch.md)

# Step 15 — Bolt-carried neutral transport, the bolt-area branch, and a 3.4× larger certified deficit

Session S1003A01, Agent2, Execute. Normalization \(\operatorname{Ric}_{CH}=-6g\); costs are in units of \(8\pi^2\);
\(J_6=\int|\operatorname{Ric}+6g|^2\), \(P=\int|\operatorname{Ric}^\circ|^2\). Diagonal Bianchi IX,
\(g=dt^2+\sum a_i^2\sigma_i^2\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\), \(\int\sigma_{123}=2\pi^2\).
Cell convention (FrozenCell): \(a_1^2=F\) collapses at the bolt \(x=x_0\), \(a_2^2=x\), \(a_3^2=xe^w\) is the CH Kähler
direction, \(dt=dx/(2\sqrt G)\); \(b^2=a_2(0)^2=x_0\). (Peer S1003A02 labels: their \(a_3\) = our \(a_1\), their \(a_1\) = our \(a_3\).)

## 1. The neutral mode is a scalar-Laplacian mode; its Green representation closes at the bolt

Since \(\operatorname{Ric}_{ii}=-(WL_i)'/W+\mathrm{alg}_i\) with \(L_i=a_i'/a_i\), \(W=a_1a_2a_3\),
\(\mathrm{alg}_i=2(a_i^4-(a_j^2-a_k^2)^2)/W^2\), the field \(q=\log(a_2/a_1)\) satisfies exactly
\[
(Wq')'=W(V-E),\qquad V=\frac{4(a_2^2-a_1^2)(a_1^2+a_2^2-a_3^2)}{W^2},\qquad E=\operatorname{Ric}_{22}-\operatorname{Ric}_{11}.
\]
Because \(W\,dt=dV_g/(2\pi^2)\), this is \(\Delta_g q=V-E\) for the radial scalar Laplacian. Symbolic check against the
Cartan-derived Ricci tensor: `scripts/check_neutral_identity.py` (residual 0; the companion pair \(\log(a_3/a_2)\) also checks).

Bolt regularity (\(a_1=t+O(t^3)\), \(a_2,a_3=b+O(t^2)\)) gives \(W=b^2t+O(t^3)\), \(q=\log(b/t)+O(t^2)\),
\(Wq'\to-b^2\). With the Dirichlet radial Green function \(G(t)=\int_t^TW^{-1}=b^{-2}\log(b/t)+\gamma+o(1)\),
\(\Phi_G=q+GWq'\) has \(\Phi_G'=GW(V-E)\), \(\Phi_G(0)=-b^2\gamma\), \(\Phi_G(T)=0\) for an exact CH collar. Hence the two
intrinsic identities (no entrance slice, no entrance slope):
\[
\text{(I1)}\ \int_0^TW(V-E)\,dt=b^2,\qquad \text{(IG)}\ \int_0^TGW(V-E)\,dt=b^2\gamma .
\]
These are the only two neutral observables: \(\psi=\alpha+\beta G\) spans the kernel of \(\psi\mapsto(W\psi')'\).
Since \(P/(8\pi^2)=\tfrac14\int W|\operatorname{Ric}^\circ|^2dt\ge\tfrac18\int WE^2dt\),
\[
\frac{P}{8\pi^2}\ \ge\ \frac{\big(\int GWV-b^2\gamma\big)^2}{8R_G},\qquad R_G=\int_0^TG^2W\,dt .
\]
`scripts/neutral_flux_bolt.py` evaluates every term (the finite part \(\gamma\) is computed with the bolt logarithm removed
analytically; an early version offset \(t\) by evaluating at \(v=10^{-7}\) and gave a non-convergent \(\gamma\) — repaired).
(I1) and (IG) hold to \(10^{-10}\)–\(10^{-9}\) on all cells and the pointwise ODE residual is \(1.4\times10^{-4}\) (finite differences).

| cell | \(x_0\) | \(X\) | \(P\) | E-channel share of \(P\) | \(\int GWV\) | \(b^2\gamma\) | \(R_G\) | \((\int GWE)^2/(8R_G)\) |
|---|---|---|---|---|---|---|---|---|
| certified X=8 | .01 | 8 | .99911 | .510 | 1.5052 | −.0353 | .6728 | .4409 |
| continued | .01 | 64 | .99870 | .511 | 1.5097 | −.0354 | .6751 | .4421 |
| area branch | .003 | 64 | .99980 | .503 | 1.5900 | −.0124 | .8398 | .3822 |
| area branch | .015 | 64 | .99777 | .516 | 1.4623 | −.0498 | .6172 | .4631 |
| area branch | .02 | 64 | .99694 | .522 | 1.4194 | −.0631 | .5753 | .4776 |
| area branch | .03 | 64 | .99585 | .531 | 1.3419 | −.0874 | .5154 | .4954 |
| area branch | .05 | 64 | .99675 | .542 | 1.2102 | −.1286 | .4392 | .5101 |
| area branch | .1 | 64 | 1.01643 | .555 | .9763 | −.2091 | .3374 | .5205 |

Data: `data/neutral_flux/nf_*.json`. Probes show that \(\int GWE\), like \(P\) itself, is paid in the core: for the
X=8 cell 66% of \(\int GWE\) and 75% of \(P\) by \(t=0.1\), 97% and 99.4% by \(t=0.4\). The ratio \(a_2/a_1\) is already
\(1.04\) at \(t=0.4\) and \(1.0001\) at \(t=1.6\): the cheap cells do **not** shadow the peer's ACH Einstein fillings
(Rossi ratio \(\ge2.19\)); beyond the core they are small perturbations of CH.

**Scale regimes.** The compliance grows logarithmically as the bolt shrinks: a fit gives
\(R_G\approx0.144\log(1/x_0)+0.010\) (figure right panel). This is the four-dimensional logarithmic capacity of a small
sphere: in the flat annulus \(b\ll t\ll1\), \(W\approx t^3\), \(G\approx1/(2t^2)\), \(G^2W\approx1/(4t)\), whence
\(R_G\approx\tfrac14\log(1/b)=\tfrac18\log(1/x_0)\) (observed slope .144 includes CH curvature corrections). The numerator
\(\int GWE\) is invariant under the core rescaling \(t=b\tau\), \(W=b^3\widehat W\), \(G=b^{-2}\widehat G\), and stays \(\approx1.6\).
So the neutral observable certifies a share \(\sim c/\log(1/b)\to0\) as \(b\to0\): it is effective at moderate bolt scale,
and the small-bolt regime must be paid by the Chern–Weil whole-AE threshold instead (consistent with the data:
\(x_0=.001\) gives \(J=1.00002\), \(x_0=.003\) gives \(J\approx.9998\)).

**What this does and does not prove.** The displayed inequality is an identity-plus-Cauchy–Schwarz; it becomes a lower
bound only with independent control of the mismatch \(\int GWV-b^2\gamma\) for every competitor. For these cells the
mismatch is dominated by the potential transport \(\int GWV\), not by the finite part. Since \(a_3\) enters \(V\) and \(W\)
algebraically and the neutral equation is one second-order relation among three profiles, we expect (not yet shown)
that \(E\equiv0\) can be imposed on non-Einstein competitors by solving for \(a_3\), so the neutral observable alone
cannot prove a gap: it must be combined with the spin calibration / Chern–Weil charge which controls the remaining
49% of \(P\). The useful quantitative information is the regime map above.

## 2. Bolt area is a decisive variable: the area branch

All earlier continuation fixed \(x_0=0.01\). `scripts/run_area_branch.sh` and `run_area_branch2.sh` (with
`perp_collar_continue.py` now keeping the seed's \(x_0\)) optimize the same degree-\(d\) perpendicular ansatz at
\(x_0\in\{.003,.01,.015,.02,.03,.05,.07,.1,.15\}\) and continue physically \(X=8\to16\to32\to64\to128\to256\).
Table `data/perp_area/area_table.csv`, figure `figures/area_branch.png` (left). Selected \(J_6/(8\pi^2)\):

| \(x_0\) | X=8 | 16 | 32 | 64 | 128 | 256 |
|---|---|---|---|---|---|---|
| .003 | .99986 | .99982 | .99981 | .99980 | | |
| .01 | .99912 | .99890 | .99874 | .99870 | | |
| .015 | .99871 | .99824 | .99789 | .99777 | | |
| .02 | .99852 | .99757 | .99715 | .99694 | .99686 | .99680 |
| .03 | .99917 | .99726 | .99628 | **.99585** | .99567 | .99560 |
| .05 | 1.00404 | .99987 | .99774 | .99677 | .99630 | .99611 |
| .07 | 1.01386 | 1.00671 | 1.00357 | 1.00194 | 1.00122 | 1.00092 |
| .1 | 1.03606 | 1.02507 | 1.01927 | 1.01667 | 1.01549 | 1.01526 |
| .15 | 1.08803 | 1.06874 | 1.05961 | 1.05540 | 1.05342 | 1.05281 |

Increments in \(X\) decrease geometrically on each fixed-area row, so each row saturates; the optimum area moves outward
with \(X\) and settles near \(x_0\approx0.03\) (bolt geodesic radius \(\approx0.17\)), with an apparent limiting value
\(J_6/(8\pi^2)\approx0.9955\). Large bolts are strongly penalized (\(x_0=.15\): \(\approx1.053\)). Thus within this
diagonal ansatz the evidence points to an **interior** optimal bolt scale and saturation in the collar radius —
attainment-type behavior, neither bolt shrinking (excluded asymptotically by the AE threshold) nor bolt growth.
Degree-20 restart at \(x_0=.01,X=64\) changed \(J\) only by \(2\times10^{-7}\); the large-\(X\) optimizers stop with
gradient norms \(10^{-3}\)–\(10^{-2}\), so the table values are upper bounds for the ansatz, not converged minima.

**Certified.** `perp_rigorous_enclosure.py` now accepts an exact rational `--x0`. For \(x_0=3/100\), \(X=64\), degree 16
(`data/perp_area/rigorous_x00.03_X64_d16.json`, 192-bit Arb):
\[
\frac{J_6}{8\pi^2}\in[0.99585469086\pm6.7\times10^{-12}],\qquad \frac{P}{8\pi^2}\in[0.99584840759\pm5.5\times10^{-12}],
\]
\(\eta>0.0041453091430\), with \(\operatorname{Ric}=-6\) at the collar to \(3\times10^{-14}\) and finite bolt values. The
admissibility chain (explicit positivity of \(F,G\), \(f_1g_1=1\), \(w=O(y^2)\), perpendicular-slot \(D\#\overline{\mathbf{CP}}{}^2\)
topology, third-order CH contact, \(O(\delta^3)\) smoothing, \(g\mapsto6g\)) is independent of \(x_0>0\). The I54
transfer therefore gives, on an existential balanced cover sequence,
\[
\limsup_j\frac{\alpha(M_j)}{h_j}\le4-\frac{8\eta}{9}+\varepsilon<3.9963153+\varepsilon ,
\]
improving the Step-14 value \(3.998846902\) (deficit \(4-\text{coef}\) multiplied by \(3.2\)).
The \(X=128\), degree-20 cell (`data/perp_area/rigorous_x00.03_X128_d20.json`, 128-bit Arb, tol \(10^{-9}\)) gives
\(J_6/(8\pi^2)\in[0.9956689792,\,0.9956710815]\), \(P/(8\pi^2)\in[0.9956621671,\,0.9956632985]\), hence
\(\eta_{128}>0.0043289184910\) and
\[
\limsup_j\alpha(M_j)/h_j<4-8\eta_{128}/9+\varepsilon<3.9961521+\varepsilon .
\]
The \(X=256\) enclosure (`rigorous_x00.03_X256_d24.json`, task s15_t32_tool1) was still running at the end of Step 15;
a 192-bit, tol \(10^{-14}\) attempt timed out after 1500 s, so high degree/large \(X\) makes Arb integration slow.

## 3. Independent check of the peer ACH Einstein family

`scripts/einstein_shoot_independent.py` re-derives the bolt-regular series from scratch (free data \(b\) and \(r_4\);
\(p_3=-2/(3b^2)\), \(q_2=r_2=(3b^2+2)/(2b)\)) and bisects the AH/ACH separatrix. Results (`data/einstein_shoot/indep.json`):
at \(b=0.8\), \(|q_4-r_4|^*=0.286993\) (peer \(d^*=0.286979\)), Rossi plateau ratio \(a_2/a_1\approx2.195\) (min on plateau
\(2.192\)); \(b=0.7\): 2.201; \(0.9\): 2.219; \(1.1\): 2.323; \(2.0\): 3.176. This independently confirms
\(\rho_{\min}\approx2.19\) near \(b\approx0.8\). (My \(d\)-scan did not bracket the small-\(b\) separatrices \(b=.29,.55\).)

## 4. Consequences for the research line

1. The upper construction is governed by the bolt scale at least as much as by the collar radius; the next explicit
   improvements come from joint \((x_0,X)\) optimization with better stationarity, not from pair interactions.
2. The diagonal infimum appears to be attained at an interior bolt scale by a complete CH-asymptotic metric whose
   defect is concentrated in a core of radius \(\sim0.3\). A proof would combine: the Chern–Weil AE threshold for
   \(b\to0\); a large-bolt penalty (to be derived, e.g. from the aligned/perpendicular period response at large \(t\));
   and compactness in the middle regime with the neutral Green observable supplying a nondegenerate mismatch there.
3. The cheapest cells live far from the ACH Einstein fillings, so the ACH resistance mechanism of Step 14 is not where
   these cells pay; the core is.



---

## Source step16_joint_dual_calibration_and_exact_bolt_chirality.md

Original: [sources/Sessions/S1003A01/workspace/notes/step16_joint_dual_calibration_and_exact_bolt_chirality.md](../sources/Sessions/S1003A01/workspace/notes/step16_joint_dual_calibration_and_exact_bolt_chirality.md)

# Step 16 — Joint diagonal dual calibration and exact ACH-bolt chirality

Normalization throughout the cell calculation is \(\operatorname{Ric}_{CH}=-6g\), and
\(P/(8\pi^2)=\frac14\int W|\operatorname{Ric}^{\circ}|^2dt\) for diagonal Bianchi IX,
where \(W=a_1a_2a_3\).

## 1. The full diagonal Ricci variable

For the spin variables
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},\qquad
H_i=u_i+\frac12u_ju_k,
\]
put
\[
z_i=\frac{\dot u_i}{a_i}-\frac{2H_i}{a_ja_k}.
\]
The Cartan calculation of Steps 6--7 says
\[
|\operatorname{Ric}^{\circ}|^2=|z|^2.
\]
If \(e_0,e_1,e_2,e_3\) are the diagonal entries of \(\operatorname{Ric}^{\circ}\), then
\[
z_i=-(e_0+e_i).
\]
Thus the three-vector \(z\), not a single Ricci difference, is the complete trace-free diagonal
Ricci variable.  For every test field \(\beta(t)\in\mathbb R^3\),
\[
\boxed{\quad \frac{P}{8\pi^2}\ge
 \frac12\int Wz\cdot\beta\,dt-\frac14\int W|\beta|^2dt.\quad} \tag{1}
\]
For a finite family \(B_A\), the optimized right side is
\[
\frac14m^TG^{-1}m,\qquad
m_A=\int Wz\cdot B_A,
\quad G_{AB}=\int WB_A\cdot B_B.
\]
The full Gram matrix is used once, so correlated Green and spin directions are not added as
independent energy contributions.  `proofs/JointDualGram.lean` checks the scalar/eigenchannel
square completion, and `proofs/joint-dual-gram-check.json` dependency-checks the named theorem.

`scripts/check_joint_dual_identities.py` checks, in the Cartan algebra, the spin boundary
identity for
\[
\Phi=C-u_2^2,
\qquad \nabla_u\Phi=(2H_1,u_1u_3,2H_3):
\]
\[
\int Wz\cdot\frac{\nabla_u\Phi}{a}\,dt
 =\Phi(T)-\Phi(0)-2\int\sum_i\frac{(\partial_i\Phi)H_i}{\lambda_i}\,dt. \tag{2}
\]
For an \(O(-1)\) cell, \(\Phi(0)=1\), \(\Phi(T)=0\).  The correct test field in (1) is
\[
 B_i^\Phi=\frac{a_i}{W}\,\partial_{u_i}\Phi
          =\frac{\partial_{u_i}\Phi}{a_ja_k},
\]
because then \(Wz\cdot B^\Phi=\sum_i(\partial_i\Phi)a_iz_i\).  This field is weighted-\(L^2\)
regular at the collapsing bolt.  The first implementation incorrectly used
\((\partial_i\Phi)/a_i\) and then removed the fixed boundary term from the Gram moment.  TTCS
caught both errors; the script and all data below were regenerated with the correct field and the
full raw moment.  The two orbit-shape equations provide the constant and radial Green fields in
the two independent traceless diagonal directions.  Their fixed bolt fluxes and potential terms
are what must eventually make the moments in (1) competitor-independent.

## 2. Joint Gram experiment on the certified area branch

`scripts/joint_dual_calibration.py` evaluates the finite basis
\[
\{1,G\}\otimes\{(-1,0,1),(1,-1,0)\}
\quad\text{together with}\quad a^{-1}\nabla_u\Phi.
\]
The tensor directions are converted to the sign convention of the shape equations before
forming the Gram matrix.  The resulting numbers are numerical dual lower bounds for the
**fixed witnesses**.  They are not yet uniform lower bounds over all cells, because the
potential moments and Gram entries still depend on the metric.

Canonical table: `data/joint_dual/summary.csv`.

| \(x_0\) | \(P/(8\pi^2)\) | two Green shape fields | joint Green+spin | joint share of \(P\) |
|---:|---:|---:|---:|---:|
| .003 | .999795 | .506490 | .999523 | .99973 |
| .01 | .998700 | .581363 | .996023 | .99732 |
| .015 | .997766 | .606897 | .992008 | .99423 |
| .02 | .996937 | .623521 | .987480 | .99051 |
| .03 | .995848 | .643403 | .977335 | .98141 |
| .05 | .996753 | .658934 | .956338 | .95945 |
| .10 | 1.016431 | .666364 | .918929 | .90407 |

The corrected result is much stronger than the preliminary implementation.  At the inexpensive
\(x_0=.03\) cell the two shape Green fields see \(64.6\%\), while the single correct spin field
already sees \(97.2\%\); optimizing all five fields together sees \(98.14\%\) of \(P\).  As
\(x_0\to0\), the spin projection approaches the complete cost (joint share \(99.97\%\) at
\(.003\)), exactly as expected from the whole-AE/Chern--Weil calibration.  Its share decreases
for large bolts, while the two Green channels grow relatively more important.  This is the sought
complementarity rather than double counting.

A representation test in `scripts/full_diagonal_projection.py` multiplied the corrected geometric
directions by cubic polynomials in normalized geodesic radius.  It spans \(99.969\%\) of \(P\)
at \(x_0=.03\), but the Gram matrix is poorly conditioned and its localized moments are not fixed
by the two elementary Green identities.  The remaining difficulty is therefore no longer finding
a tensor direction that represents the core energy: it is converting the nearly complete spin
projection into a competitor-independent moment estimate and controlling localized corrections.

## 3. Scalar-channel cancellation is an escape only at enormous full cost

`scripts/test_Ezero_reconstruction.py` freezes \(F,G\) of the \(x_0=.03,X=64\) witness and
varies only \(w\), trying to suppress one Ricci-difference energy.  Unregularized optimization
reduces that channel from \(0.13210\) to \(0.00632\), but drives the coefficients to size
hundreds and raises \(P/(8\pi^2)\) to \(2.46\times10^5\).  With quadratic coefficient penalties
\(\mu=10^{-1},10^{-2},10^{-3},10^{-4}\), the outcomes are:
\[
(E\text{-cost},P)=(.13198,.99586),(.13094,.99721),(.12218,1.10475),(.08775,4.77986).
\]
Files: `data/joint_dual/Ezero_mu*.json` and `Ezero_x003_X64.json`.

So a single shape channel can be nearly cancelled as an underdetermined scalar equation, but in
this controlled slice doing so transfers large cost to the other shape/radial components.  This
supports the Strategist's warning: failure of one scalar observable does not identify a genuine
low-energy escape.  A lower argument must control the full three-vector \(z\).

## 4. What the joint experiment changes for a lower theorem

The finite Gram representation suggests a concrete middle-scale theorem target.  On
\(b\in[b_-,b_+]\) and for a controlled class of diagonal cells, seek transport identities for
both shape Green fields and one corrected spin field such that:

1. their moment vector is separated from zero by bolt flux plus the relative charge;
2. the potential terms can be bounded in terms of the same moment vector and geometric state,
   without assuming the desired Ricci estimate;
3. the Gram matrix has a uniform upper spectral bound;
4. localized residual directions are absorbed by a positive spin/Hamilton--Jacobi remainder.

The corrected five-field basis is already numerically near-sharp on the observed interior cell:
\(0.977335\) against \(P=0.995848\), and the spin direction alone gives \(0.967757\).  Thus a
competitor-independent control of the full spin moment and norm could produce a quantitatively
serious diagonal lower bound.  Near equality is not automatic: the moment contains the nonlinear
potential integral in (2), and the test norm is metric-dependent.  The remaining \(1.86\%\) at
\(x_0=.03\) can be represented by localized corrections, but deriving their moments from geometry
without assuming the desired estimate is the actual problem.

For \(b\to0\), the data are consistent with a two-scale dichotomy rather than an automatic AE
limit: either the marked rescaled core has controlled end transgression and the whole-AE identity
pays the charge, or a fixed CH-scale outer transition retains the missing charge/energy.  The
large-b side likewise still needs a genuine penalty estimate; numerical growth alone is not one.

## 5. Exact bolt chirality for the peer's validated ACH Einstein filling

Peer S1003A02 proved a complete real-analytic \(\operatorname{Ric}=-6g\) ACH filling at
\(b=4/5\).  Its validated Fuchsian series gives, in their bolt-slot-3 convention,
\[
a_1=a_2=\frac45+\frac{49}{20}t^2+O(t^4),\qquad
 a_3=t-\frac{25}{24}t^3+O(t^5).
\]
`scripts/ach_bolt_weyl_exact.py` inserts this exact two-jet into the Cartan curvature operator and
projects to the two chiral \(\Lambda^2\) blocks used by `o11_rotated_cell.py`.  At the bolt,
\[
s=-24,
\]
\[
W_A=\operatorname{diag}\!\left(-\frac{41}{16},-\frac{41}{16},\frac{41}{8}\right),
\quad |W_A|_{op}^2=\frac{5043}{128},
\]
\[
W_B=\operatorname{diag}\!\left(-\frac{91}{16},-\frac{91}{16},\frac{91}{8}\right),
\quad |W_B|_{op}^2=\frac{24843}{128}.
\]
Both halves are nonzero exactly.  Therefore the validated ACH Einstein metric is neither
self-dual nor anti-self-dual.  The first exact script version accidentally reused the symbol `b`
for the bolt radius and Cartan radius variable, causing sequential SymPy substitution to corrupt
the inserted two-jet; TTCS identified the inconsistency.  The repaired script uses a `Dummy` bolt
radius and now agrees with `scripts/ach_bolt_weyl_coordinate_check.py`, which gives chiral operator
norms tending to \(39.3985\) and \(194.083\).  In the four-index tensor convention these norms are
four times larger.  Each block has the Kähler-type eigenvalue multiplicity \((2,1)\), so the
peer's proposed exclusion by "three distinct eigenvalues" does not apply to the corrected blocks.
(Correction, Step 17.)  A Kähler structure is nevertheless excluded for either orientation by the
norm: the metric is Einstein, so a compatible Kähler structure would make it Kähler--Einstein,
and then the Kähler-side Weyl block is \(\operatorname{diag}(s/6,-s/12,-s/12)=(-4,2,2)\) with
\(|W|^2_{op}=s^2/24=24\).  The two blocks have norms \(5043/128\approx39.40\) and
\(24843/128\approx194.08\), and neither spectrum is \(\pm(-4,2,2)\).  Correction sent to the peer
as message 771.  The labels \(A,B\) must be
mapped to \(W^+,W^-\) according to orientation before assigning a sign.

## 6. Status

The certified cell upper theorem remains the current global construction result; this step did
not treat another decimal as the main goal.  The new substance is a complete three-component
diagonal Ricci representation, a non-double-counted finite Gram combination of the two shape
transports with the spin charge direction, an explicit demonstration of what remains invisible,
and an exact chirality conclusion for the independently validated ACH Einstein filling.
The diagonal lower theory, small-b outer-transition alternative, large-b penalty, unrestricted
cell infimum, and mixed blow-up--handle costs remain open.



---

## Source step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md

Original: [sources/Sessions/S1003A01/workspace/notes/step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md](../sources/Sessions/S1003A01/workspace/notes/step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md)

# Step 17 — Hamilton–Jacobi structure of the diagonal cell problem, the Kähler manifold \(N\), and where the relative Chern–Simons calibration loses control

Normalization: perpendicular diagonal Bianchi IX cells, slots \((a_1,a_2,a_3)=(\sqrt x,\sqrt{xe^w},\sqrt F)\) (Step 7), \(a_3\) collapsing at the bolt, \(a_2\) the CH Kähler direction. \(P/(8\pi^2)=\int L\,dt\), \(L=\tfrac14W|z|^2\), \(W=a_1a_2a_3\), \(z\) the complete diagonal trace-free Ricci variable of Step 16. Every identity below is checked symbolically in `scripts/hj_structure.py` (output `data/hj/hj_structure_check.txt`, all residuals 0) and `scripts/check_variable_seed.py`.

## 1. The cell problem as an optimal-control problem

With \(\gamma_i=(a_j^2+a_k^2-a_i^2)/(a_ja_k)\), \(u_i=\dot a_i-\gamma_i\), \(H_i=u_i+\tfrac12u_ju_k\), \(\lambda_i=a_ja_k/a_i\), the exact equations are
\[
\dot a_i=u_i+\gamma_i(a),\qquad \dot u_i=\frac{2H_i}{\lambda_i}+a_iz_i ,
\]
so a diagonal cell is a controlled trajectory in the six-dimensional state space \((a,u)\), with control \(z\) and running cost \(L\). The \(u_i\) are the components of the \(\Lambda^+\) spin connection in the invariant frame, \(H_i\) its curvature, and \(C=\sum u_i^2+u_1u_2u_3\) its Chern–Simons function (Step 7, (1.2)). Zero control means \(\operatorname{Ric}^\circ=0\): the free flow \(D_0\) is the Einstein flow of every sign of Einstein constant.

**(H1) Square completion.** For every state function \(S(a,u)\),
\[
L-\frac{dS}{dt}=\frac W4\sum_i\Big(z_i-\frac{2a_iS_{u_i}}W\Big)^2-\mathcal H_S,\qquad
\mathcal H_S=D_0S+\frac1W\sum_ia_i^2S_{u_i}^2 .
\]
Hence \(\mathcal H_S\le0\) along a cell gives \(P/(8\pi^2)\ge S(\text{out})-S(\text{bolt})\). This is the Strategist's formula, now verified. \(\mathcal H_S=\mathrm{Ham}(a,u,\nabla S)\) for the Pontryagin Hamiltonian
\(\mathrm{Ham}=p_a\cdot(u+\gamma)+p_u\cdot(2H/\lambda)+W^{-1}\sum a_i^2p_{u_i}^2\) (maximizing control \(z=2a\,p_u/W\)). The value function \(V\) (least cost to reach the CH curve) gives the exact subsolution \(S=-V\) with \(\mathcal H_S=0\); the diagonal cell infimum is \(V(\text{bolt})\).

**(H2) Seed.** For \(\Phi=C-u_2^2\), \(\mathcal H_{-\Phi}=-2u_1u_2u_3/\lambda_2\), which is the relative calibration (1.5) of Step 7. For \(S=-c\Phi\),
\[
-\mathcal H_{-c\Phi}=c(1-c)Q+c\kappa,\qquad Q=\frac1W\sum_ia_i^2\Phi_{u_i}^2\ge0,\quad \kappa=\frac{2u_1u_2u_3}{\lambda_2},
\]
and exactly \(P/(8\pi^2)=c+\int\frac W4|z+2c\,a\nabla_u\Phi/W|^2+\int[c(1-c)Q+c\kappa]\). The quartic parts of \(D_0\Phi\) and \(Q\) cancel identically, so \(\Phi\) is an exact calibration up to the cubic.

**(H3) Hamiltonian constraint.** \(\Lambda=-8\sum_ia_iH_i/W\) \((=2s-4\operatorname{Ric}_{00}=-4G_{00})\) is a first integral of \(D_0\), and \(s=\Lambda-2\sum_iz_i\). Its controlled derivative is linear in \(z\) (contracted Bianchi identity; formula in the check output). A function of \(\Lambda\) alone has \(\mathcal H\ge0\) and cannot calibrate.

**(H4) Scaling charge.** \(\sum_ia_i\partial_{a_i}\mathrm{Ham}=-(\mathrm{Ham}-p_a\cdot(u+\gamma))\), hence \(\frac d{dt}\sum_ia_ip_{a_i}=\mathrm{Ham}\) along extremals. Because \(P\) is scale invariant and the CH end set is scale invariant for \(P\), optimal extremals have \(\mathrm{Ham}=0\) and conserve \(\sum a_ip_{a_i}\). In particular the bolt scale \(b\) is a gauge for \(P\): in scale-reduced variables the bolt is the single point \((a_3/a_1,a_2/a_1,u)=(0,1,(0,0,-1))\), the CH collar is the curve \(\{a_1=a_3,\ u_1=u_3=0,\ u_2=3(a_2^2/a_1^2-1)\}\), and the observed interior optimum \(x_0\approx.03\) is a property of where the optimal reduced trajectory meets that curve relative to the collar curvature. (For \(J_6\) the scalar term breaks scaling, but only at the \(10^{-5}\) level on the good cells.)

**(H5)** For scale-invariant \(S\), \(\mathcal H_S\) is homogeneous of degree \(-1\) in \(a\), so the subsolution inequality lives on the five-dimensional reduced state space.

**Collar extension and the Gram obstruction.** The Strategist is right that the Step-16 target "uniform upper spectral bound on \(G\)" is false: appending an exact CH annulus leaves \(P\) unchanged while the constant shape fields have \(\|B\|^2\propto\int W\,dt\to\infty\). Only the invariant \(m^TG^\dagger m\) (which is what Step 16 computed) or the HJ form is meaningful. In the HJ form the issue disappears: \(\Phi\) and \(\nabla_u\Phi\) vanish on the whole CH curve, so any \(S=-\Phi+\psi\) with \(\psi\) and \(\nabla_u\psi\) vanishing there is constant on CH and insensitive to collar extension.

## 2. The Kähler manifold \(N=\{u_1=u_3=0\}\)

(H6–H7) \(N\) is invariant under \(D_0\); \(\Phi\) and \(\nabla_u\Phi\) vanish on \(N\); and on \(N\), \(\frac d{dt}(a_1a_3)=2a_2\), i.e. \(\omega_2=a_2\,dt\wedge\sigma_2+a_3a_1\sigma_3\wedge\sigma_1\) is closed. \(N\) is the set where the \(\Lambda^+\) connection reduces to \(U(1)\) (only \(u_2\) survives), i.e. the states of metrics Kähler for \(\omega_2\) — the complex structure of CH. CH is the Kähler–Einstein trajectory in \(N\). Thus \(\Phi=CS(A)-u_2^2\) is the Chern–Simons function of \(A\) relative to its \(U(1)\)-reduction, and the calibration is exact on Kähler states. Note \(a_1=a_3\) is invariant inside \(N\) (since \(\frac d{dt}(a_1^2-a_3^2)=2W^{-1}(a_1^2-a_3^2)(a_2^2-a_1^2-a_3^2)\) there), but \(N\) also contains triaxial Kähler states.

Near \(N\), with \(\xi=(u_1,u_3)\) and \(v_\pm=(u_1\pm u_3)/\sqrt2\),
\[
\Phi=\Big(1+\frac{u_2}2\Big)v_+^2+\Big(1-\frac{u_2}2\Big)v_-^2\qquad(\text{exactly}).
\]
\(\Phi\) is the transverse Chern–Simons Hessian at the reducible connection \(u_2\sigma_2\). Its \(v_-\) eigenvalue crosses zero at \(u_2=2\) (on CH: \(x=2/3\)) — a spectral-flow crossing of the transverse Hessian. Write the transverse Hessian of a candidate as
\[
S=\tfrac12\xi^TK\xi+O(|\xi|^3),\qquad
A=\begin{pmatrix}2&u_2\\u_2&2\end{pmatrix},\qquad
D=\operatorname{diag}(a_1^2,a_3^2)/W.
\]
The quadratic Hamiltonian inequality is
\[
\tfrac12D_0K+\tfrac12(KDA+ADK)+KDK\le0.                  \tag{2.1}
\]
After the shifted variable \(Y=K+A/2\), and only after this shift, it becomes
\[
\tfrac12D_0Y+YDY\le\tfrac14\big(ADA+D_0A\big),\qquad
D_0A=\frac{2u_2}{\lambda_2}\begin{pmatrix}0&1\\1&0\end{pmatrix}. \tag{2.2}
\]
Thus the relative seed \(S=-\Phi=-\tfrac12\xi^TA\xi\) has \(K=-A\) and \(Y=-A/2\), whereas the identically zero function has \(K=0\) and \(Y=A/2\). The earlier version of this note incorrectly inserted the shifted variable into the ansatz and then identified \(Y=0\) with \(S=0\); that convention is superseded by (2.1)--(2.2).

At \(u_2=2\), \(A\) loses one eigenvalue. This shows failure of the particular relative primitive \(-c\Phi\) in the \(v_-\) channel; it is not evidence for a negative compactly supported CH mode, since the Step-7 positive ground states control the latter. The mathematical issue is whether bolt-side Hessian data can be transported to a valid outgoing graph. A pole in \(K\) or \(Y\) may only be failure of that graph chart; the associated linear Hamiltonian/Jacobi system must be followed before concluding that no piecewise or nonsmooth calibration exists.

## 3. What the certified cells do in this picture

`scripts/hj_witness_analysis.py` (data `data/hj/witness_seed.json`) and `scripts/hj_failure_locus.py` (data `data/hj/cs_hessian_failure.json`):

* The identity of (H2) holds numerically to \(10^{-8}\) for \(c=1,\frac12\).
* The cubic \(\kappa\) is negative essentially along the whole transition: \(\int\kappa_+\le8\times10^{-5}\) against \(\int\kappa_-=-6.1\times10^{-4},-5.3\times10^{-3},-3.25\times10^{-2},-1.35\times10^{-1}\) for \(x_0=.003,.01,.03,.1\) at \(X=64\).
* The set \(F_0=\{Q+\kappa<0\}\), where no \(c\in(0,1]\) works pointwise, is the same band on every cell: \(t\in[0.53,1.18]\), \(u_2\in[1.07,6.55]\), with the transverse displacement more than \(90\%\) in \(v_-\) and the state within \(0.012\)–\(0.24\) of \(N\). It straddles the spectral crossing \(u_2=2\). Only \(5\)–\(10\%\) of \(\int\kappa_-\) lies in \(F_0\). Hence \(c_{\max}<0\) for every witness: even restricted to the witness's own trajectory, the seed family fails pointwise.
* **Costate.** Equality in (H1) gives the value-function gradient \(p_u=Wz/(2a)\). In the control metric \(a_i^2/W\), \(p_u\) projects onto \(-\nabla_u\Phi\) with coefficient \(0.9852\) and share \(97.2\%\) at \(x_0=.03\), and \(0.99894\) and \(99.96\%\) at \(x_0=.003\). Pointwise (`scripts/hj_local_f.py`, `data/hj/local_f_*.csv`), in the core \(t\le0.3\), where 92% of \(P\) is paid, the cosine with \(-\nabla\Phi\) exceeds \(0.99\) and the local coefficient is \(f\approx0.985\)–\(0.99\). It rises above \(1\) for \(0.3<t<0.6\) as \(\Phi\to0\), and alignment is lost in the band \(F_0\) (cosine \(\to0\) near \(u_2\approx2\)–\(3.4\)). Beyond the band, \(f\) varies freely while \(\Phi\approx0\).

Interpretation. The near-optimal value function is, to about one percent, the relative Chern–Simons charge with a slowly varying coefficient: \(V\approx f(a,u_2)\,\Phi\). For the variable seed (checked symbolically),
\[
\mathcal H_{-f\Phi}=-f\big[(1-f)Q+\kappa\big]-\Phi\,D_0f+\frac{a_2^2\Phi f_{u_2}}W\big(2f\Phi_{u_2}+\Phi f_{u_2}\big).
\]
Near the bolt \(f<1\) lets \(-f(1-f)Q\) absorb the cubic. The rise of \(f\) above 1 outward is paid by \(-\Phi D_0f<0\) while \(\Phi>0\). Across the band \(F_0\), \(\Phi\) changes sign (\(u_2>2\) makes the \(v_-\) coefficient negative), so a decreasing \(f\) there helps rather than costs. Along one fixed trajectory, ignoring \(f_{u_2}\), \(\mathcal H=0\) is a Bernoulli equation. With \(g=1/f\) it becomes linear,
\(\dot g=g(Q+\kappa)/\Phi-Q/\Phi\), and the bounded solution gives
\(g(0)=\int_0^\infty\frac Q\Phi\exp\!\big(-\int_0^s\frac{Q+\kappa}\Phi\big)ds\). Negative \(\kappa\) forces \(g>1\), i.e. \(f(\text{bolt})<1\). This is the one-dimensional shadow of the saving mechanism. It is not a uniform bound, because a certificate needs \(\mathcal H\le0\) off the trajectory as well.

## 4. Failed formulation preserved

`scripts/hj_socp.py` poses the subsolution problem as a convex second-order-cone program in the coefficients of \(S=-c\Phi+\sum\theta_kb_k(q,w,y)m_k(u_1,u_3)\), with \(\mathcal H_S\le0\) on sampled states. With samples only on the witness trajectory the problem is degenerate: \(S\) is unconstrained off the curve, coefficients blow up, Clarabel fails, and SCS returns `optimal_inaccurate` with \(\max\mathcal H>0\) on the samples. The values \(0.9966\) and \(1.0039\) are meaningless. A usable version needs (i) a tube of states with bolt-regular perturbations, (ii) an orthogonalized basis adapted to \(N\) (transverse quadratic forms in \(v_\pm\) with coefficients in \((u_2,a\text{-shape})\)), and (iii) separate treatment of the bolt chart, where \(a_1/(a_2a_3)\to\infty\) forces \(S_{u_1}\to0\). No number from this script may be used.

## 5. Consequences for the lower theory

1. The diagonal infimum is the value \(V(\text{bolt})\) of a point-to-curve control problem on a five-dimensional reduced state space. A lower theorem is a subsolution of \(\mathcal H_S\le0\). The near-optimal \(S\) is \(-f\Phi\) with \(f\approx0.99\) on the bolt side.
2. The only place where the tested \(u\)-only relative primitive fails pointwise is a neighbourhood of the Kähler manifold \(N\) around the zero of its \(v_-\) Hessian at \(u_2=2\). The required correction is a transverse quadratic form governed by (2.1), or equivalently the shifted equation (2.2) with the corrected boundary data \(Y=-A/2\) for the seed and \(Y=A/2\) for the zero function. The associated linear Hamiltonian/Jacobi system, rather than a Riccati graph alone, decides whether bolt-side data can be connected through this region.
3. The cheap mechanism of the certified cells has a geometric description: they leave the bolt carrying almost the full relative charge \(\Phi\), shed it in the core with near-exact calibration, and approach the Kähler manifold of the CH complex structure through the band where the transverse Chern–Simons Hessian degenerates. There the signed cubic can be negative at second order in the distance to \(N\).
4. Step 16's "uniform Gram bound" is replaced by HJ constancy on the CH curve. The small-\(b\) alternative becomes a statement about trajectories passing near the flat fixed point \(u=0,\ a_1=a_2=a_3\) (the AE regime), where \(\Phi\) is exact up to \(\kappa\) and \(Q\) dominates. Large \(b\) corresponds to reduced trajectories that reach \(N\) far out along the CH curve.

Everything here is internal to the diagonal perpendicular class. It does not bound unrestricted cells or the all-metric balanced coefficient.

## 6. Cross-session points recorded this step

* Peer S1003A02 (message 772) proposes a first-order Burns response for an arbitrary closed bulk, \(P(\hat g)=P(g)+8\pi^2(1-x_0R^+_p(\zeta,\zeta))+O(x_0^{6/5})\). Our Step-8 U(2) infima (`data/u2_general/`) independently give the same slopes in all four tested backgrounds: \(H^4\) \(+2.0048\), \(S^4\) \(-1.9977\), aligned CH and FS \(\pm6\). They do not re-derive the peer's transgression matrices. For \(H^4\) the slope grows with \(x_0\) at small collar (\(2.016\to3.248\) for \(x_0=10^{-4}\to10^{-2}\), \(X=.25\)). Whether a large collar opens a finite-scale saving below \(8\pi^2\) over \(H^4\), as it did for perpendicular CH, is open. That test needs the relative charge rebuilt for the \(H^4\) end connection \(u_i=\cosh t-1\), which has no reducible \(U(1)\) structure and a positive cubic. Reply: message 773.
* Corrected bolt-chirality values sent as message 771; the peer integrated them (message 772). Non-Kähler for either orientation follows from the Kähler–Einstein spectrum \((-4,2,2)\).
* The \(x_0=3/100\), \(X=256\) Arb enclosure (task s15_t32_tool1) hit its 7200 s limit. `data/perp_area/rigorous_x00.03_X256_d24.json` is an empty file and is not a certificate. The certified record remains \(X=128\): \(J_6/(8\pi^2)\le0.9956710815\).



---

## Source step18_corrected_riccati_and_H4_comparison.md

Original: [sources/Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md](../sources/Sessions/S1003A01/workspace/notes/step18_corrected_riccati_and_H4_comparison.md)

# Step 18 — Corrected transverse Riccati variables, exact CH benchmark, and real-hyperbolic comparison

## 1. The quadratic HJ variable has been repaired

Near the invariant Kähler manifold \(N=\{u_1=u_3=0\}\), set \(\xi=(u_1,u_3)\) and
\[
\Phi=\frac12\xi^TA\xi,
\qquad
A=\begin{pmatrix}2&u_2\\u_2&2\end{pmatrix},
\qquad
D=\frac1W\operatorname{diag}(a_1^2,a_3^2).
\]
For an actual transverse Hessian
\[
S=\frac12\xi^TK\xi+O(|\xi|^3),
\]
the quadratic term in \(\mathcal H_S\) is
\[
\frac12D_0K+\frac12(KDA+ADK)+KDK.                 \tag{1.1}
\]
The shifted variable is
\[
Y=K+\frac A2,
\]
and only this shifted variable obeys
\[
\frac12D_0Y+YDY\le\frac14(ADA+D_0A).             \tag{1.2}
\]
Consequently
\[
S=-\Phi:\quad (K,Y)=(-A,-A/2),
\qquad
S=0:\quad (K,Y)=(0,A/2).                         \tag{1.3}
\]
The Step-17 note had combined the ansatz \(S=-\Phi+\frac12\xi^TY\xi\) with the shifted equation and then identified \(Y=0\) with \(S=0\). That was wrong. `notes/step17_hamilton_jacobi_kahler_manifold_and_cs_hessian.md` has been corrected in place.

## 2. Exact CH scalar Riccati solutions are the Step-7 ground states

On exact complex hyperbolic space,
\[
a_1=a_3=\sqrt x,
\quad a_2=\sqrt{x(1+x)},
\quad u_2=3x.
\]
In the eigenchannels \(v_\pm\), (1.1) becomes
\[
K_\pm'+\frac{K_\pm(K_\pm+2\pm3x)}{x(1+x)}=0.     \tag{2.1}
\]
For the hard outgoing condition at \(x=1\), the exact Dirichlet-to-Neumann solutions are
\[
K_+(x)=-\frac{2}{\Delta_+(x)},
\qquad
K_-(x)=-\frac{2(1+x)^5}{\Delta_-(x)},             \tag{2.2}
\]
where \(\Delta_\pm\) are the closed expressions from Step 7. SymPy reduces both residuals in (2.1) to zero in `scripts/riccati_ch_benchmark.py`; results are in `data/hj/riccati_ch_benchmark.json`.

If \(z=1/K\), then
\[
z'-\frac{2\pm3x}{x(1+x)}z=\frac1{x(1+x)}.       \tag{2.3}
\]
Its positive homogeneous multipliers are exactly
\[
f_+^2=x^2(1+x),
\qquad
f_-^2=\frac{x^2}{(1+x)^5},                        \tag{2.4}
\]
the squares of the positive zero modes previously proved in Step 7; in the conventional linear-ODE terminology, the integrating factors multiplying (2.3) are \(f_\pm^{-2}\). Thus the Riccati and Sturm descriptions are the same linear Hamiltonian/Jacobi system in different charts.

Numerical propagation of seed-like entrance Hessians \(K_\pm(\rho)=-c(2\pm3\rho)\) illustrates why poles must not be interpreted as negative CH modes. In the minus channel, \(c=1\) gives graph poles at
\[
\rho=.003:.05252,
\quad .01:.10826,
\quad .03:.22632,
\quad .1:.59560.
\]
For \(c=.985\), no pole appears before the numerical cutoff \(x=20\) at \(\rho=.003\), while the first poles occur at \(.51947,.29736,.64553\) for \(\rho=.01,.03,.1\). The `null` field in the data means only absence before that cutoff; the explicit Jacobi formula can still place a later pole. These poles are zeros of the graph block in the Jacobi evolution; the Lagrangian plane remains defined. They retain focal/Maslov information and can obstruct one smooth quadratic graph, but they do not imply a singular Jacobi evolution or a negative compactly supported CH mode. The meaningful matching problem is whether the bolt-side Lagrangian data lie on the admissible side of the outgoing DtN plane, possibly represented through more than one graph chart.

This already changes the proposed experiment: integrate the linear Jacobi/Lagrangian system, or use (2.2) as the outgoing benchmark for the hard target \(x=1\), rather than declaring bulk instability when one Riccati graph develops a pole. For a general terminal point \(X\), the outgoing plane is
\[
K_\pm^X(\rho)=-\left[f_\pm(\rho)^2\int_\rho^X\frac{ds}{s(1+s)f_\pm(s)^2}\right]^{-1},
\]
As \(X\to\infty\), the minus-channel integral diverges and \(K_-^X(\rho)\to0\): the free transverse minus mode alone has vanishing asymptotic DtN cost. The full cell relation must therefore carry the longitudinal torsion-free variable \(\theta=\delta\log(a_1/a_3)\), whose Step-7 moment relation couples back to \(v_-\). This explains why the positive compactly supported CH operator is insufficient for a large-collar lower bound.

## 3. Correctly normalized \(H^4\) comparison

The round profile \(a_i=\sinh t\) has \(\operatorname{Ric}=-3g\). In the common \(\operatorname{Ric}=-6g\) normalization it is
\[
a_i(t)=\frac1{\sqrt2}\sinh(\sqrt2t).             \tag{3.1}
\]
The coordinate used by the cell code is \(x=a^2\); hence an exact real-hyperbolic collar is
\[
F=x,
\qquad G=x+2x^2,
\qquad w=0.                                       \tag{3.2}
\]
The symbolic check in `scripts/u2_general_cell.py verify` gives \(s=-24\) and \(P\)-density zero for this collar.

I built `scripts/h4_perp_cell.py`, the triaxial analogue of the certified CH perpendicular ansatz, with an ordinary \(O(-1)\) bolt and exact collar (3.2). An initial base profile had the wrong bolt derivative for \(G\); it was repaired so that the unexponentiated base has \(F'(x_0)=G'(x_0)=1\), and the coefficient shift enforces \(q_F(0)+q_G(0)=0\). The main \(X=64\) files prefixed `corrected_`, and the later `biaxial_` and `random{1,2}_` files, use the repaired profile. Earlier unprefixed `perp_` files are superseded and must not be used.

Floating-point optimized \(P/(8\pi^2)\) values at \(X=64\), degree 16, are
\[
\begin{array}{c|c|c|c}
x_0&P/(8\pi^2)&J_6/(8\pi^2)&\max|w|\\\hline
.003&1.0060563827&1.0061852180&4.4\times10^{-5}\\
.01&1.0204668804&1.0216523289&6.5\times10^{-5}\\
.03&1.0630695665&1.0721494158&3.6\times10^{-5}
\end{array}                                                     \tag{3.3}
\]
The corresponding files are `data/h4_cells/corrected_perp_x0.{003,01,03}_X64_P_d16.json`. For \(x_0=.01\), the seeded larger-collar run changed \(P\) from \(1.0205588060\) at \((X,\deg,n_q)=(8,12,800)\) to \(1.0204668804\) at \((64,16,1000)\), and every tested cell remained above the topological threshold. Because the basis and quadrature also changed, this is not a one-parameter collar comparison. The older biaxial code independently found \(P=1.0647909208\) at \((x_0,X)=(.03,4)\). The optimized \(\|w\|_\infty\) is extremely small. Two additional degree-12, \(X=8\), \(x_0=.01\) random anisotropic starts converged to \(P=1.0205583805\) and \(1.0205583791\), while the exactly biaxial run gave \(1.0205615593\). Thus a tiny symmetry-breaking improvement of about \(3.18\times10^{-6}\) is reproducible within this ansatz, but it is four orders of magnitude smaller than the positive excess. `scripts/h4_anisotropy_hessian.py` evaluated the degree-12 \(w\)-sector at the biaxial optimum: all Hessian eigenvalues are positive, from \(3.24\times10^{-5}\) to \(.734\), and the quadratic Newton gain \(2.97\times10^{-6}\) agrees with the direct optimization. The nonzero \(w\)-gradient \(2.57\times10^{-4}\) indicates that the chosen \(w=0\) slice is not stationary in this slot parametrization; the metric is numerically near-biaxial, not exactly forced to be biaxial.

These runs are numerical constructions, not a proof that \(P_{1,0}^{H^4}=8\pi^2\). The gradients remain around \(10^{-5}\); only two random anisotropic restarts were made at one parameter point, and no systematic degree/quadrature refinement or interval enclosure was performed. They do provide a useful contrast: in the tested finite-dimensional diagonal class, no large-collar subthreshold mechanism was detected. The excesses satisfy \((P-1)/x_0\approx2.02,2.05,2.10\) at \(x_0=.003,.01,.03\), consistent with the first-order response from \(R^+=(s/12)I=-2I\). This supports the curvature-response picture that \(H^4\) charges every Burns direction at first order, while CH has a perpendicular kernel enabling a second-order signed interaction.

## 4. Consequences

1. The CH bulk question remains controlled by the exact positive ground states. The zero of the relative primitive at \(u_2=2\) concerns matching a bolt-side calibration to outgoing data, not a compactly supported instability.
2. The corrected boundary data are \(Y=-A/2\) for the seed and \(Y=A/2\) for zero. Any tube calculation or subsolution optimization must use these values.
3. A continuous restricted lower result would require a uniform Hamiltonian inequality on a specified tube and an independent estimate for diagonal trajectories leaving it. Sampled near-optimal values alone do not do this.
4. The next lower-theory calculation should transport a Lagrangian subspace through the core and compare it with the exact outgoing planes (2.2), while adding the longitudinal torsion-free state. This can survive Riccati chart changes and is the appropriate linear precursor to a nonlinear HJ construction.
5. The \(H^4\) result should remain a comparison branch. It suggests, but does not establish, that the sign/kernel structure of \(R^+\) separates first-order rigidity from finite-scale CH saving.

## 5. Independent and formal checks

Two independent TTCS readings found the \(K/Y\) algebra, CH Riccati equations, DtN factors, \(H^4\) normalization, bolt smoothness, collar two-jet contact, and energy normalization consistent. They prompted the clarified terminology and scope above: \(f_\pm^2\) are homogeneous multipliers rather than the conventional integrating factors; `null` records a bounded integration window; the displayed DtN formulas use the hard target \(x=1\); and graph-chart continuation does not remove the endpoint order needed for a valid subsolution. The integrations are saved under `trace/ttcs/results/step18_ttcs01_verifier1_integration.md` and `step18_ttcs01_verifier2_integration.md`.

The scalar shift identity and its seed/zero boundary translations are formalized in `workspace/proofs/RiccatiShift.lean`. `workspace/proofs/riccati-shift-check.json` dependency-checks `RiccatiShift.qiushi_scalar_shift` using only the configured allowed Mathlib axioms. This formal check certifies the algebraic shift, not the geometric derivation of the transverse HJ system.



---

## Source step19_exterior_null_line_LM_stationary_cells.md

Original: [sources/Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md](../sources/Sessions/S1003A01/workspace/notes/step19_exterior_null_line_LM_stationary_cells.md)

# Step 19 — Exact CH exterior response, stationary large-collar cells, and the far-field charge λ

Normalization: Ric_CH = −6g, values of P and J₆ divided by 8π² (threshold 1).
Fixed perpendicular slot g = dx²/(4G) + F σ₁² + x σ₂² + x e^w σ₃², Step-7 axes
(a₁,a₂,a₃) = (√x, √(x e^w), √F), CH: F = x, G = x(1+x), w = log(1+x), u = (0,3x,0).

## 1. Exact linearized Einstein modes of CH in the diagonal class

`scripts/ch_linear_einstein_modes.py`, `ch_linear_mode_solve.py`, `check_xgauge_mass_mode.py`,
`calabi_ke_check.py` (all SymPy, zero residuals).

* The exchange a₁↔a₃ splits the linearization. In the antisymmetric sector (θ = δlog(a₁/a₃),
  v₋ = δu₁ − δu₃) the linear scalar curvature vanishes identically, and the Step-7 torsion relation
  d/dx[(x/(1+x))²θ] = ½ f₋ v₋, f₋ = x/(1+x)^{5/2}, is an identity (it *defines* v₋ from θ).
  The linearized trace-free Ricci is (2/(x(1+x)))·L[θ] (z₁ = −z₃, z₂ = 0) with
  L[θ] = x²(1+x)²θ'' + x(1+x)(3x+2)θ' + 2(x−1)θ.
* Its kernel is exactly the two-parameter family θ = k⁻¹[C + (c/2)∫₀ˣ f₋²], k = (x/(1+x))².
  C is the non-decaying squashing of the conformal infinity (v₋ = 0, θ → C).
  The decaying member is the **antisymmetric Einstein mass mode**
  v₋ = c f₋,  θ = −c(6x²+4x+1)/(24x²(1+x)²) ~ −c/(4x²),
  which is linearized Einstein (dz = 0, ds = 0), singular at the centre, and in the x-gauge reads
  F = x e^{−2θ}, δw = −θ(1+2x)/(1+x), δG = θx + 2x²(1+x)θ'.  ∫₀^∞ f₋² = 1/12.
* U(2)-invariant sector: besides the gauge mode and a non-decaying squashing mode
  σ = (8x²+4x−1)/(16x²), β = (8x²+1)/(8x²), the Calabi family
  a₁ = a₃ = √x, a₂² = G = x + x² + m/x is **exactly** Kähler–Einstein (Ric = −6g) for every m,
  with u = (0,3x,0) unchanged. A smooth O(−1) bolt needs F'G' = 1 at G(x₀) = 0, but this family
  has G'(x₀) = 2 + 3x₀: the cone angle is forced, consistent with the Kähler period obstruction.

## 2. Exact exterior response (the null line)

The raw quadratic P of the minus channel on CH is (Step 7 re-derived from the squares)
  E[v₋] = ∫ μ (w')² dx,  w = v₋/f₋,  μ = x(1+x)f₋²/4 = x³/(4(1+x)⁴).
The transverse sector does not see radius perturbations at quadratic order (H₁ = H₃ = 0 on CH).
With entrance data w(ρ) = w₀, θ(ρ) = Θ and an infinite CH collar (θ → 0), minimizing E subject to
the torsion constraint gives
  **E_ext(ρ; w₀, Θ) = δ²/I(ρ)**,  δ = −2k(ρ)Θ − w₀ G(ρ),  G(x) = ∫ₓ^∞ f₋² = (6x²+4x+1)/(12(1+x)⁴),
  I(ρ) = ∫_ρ^∞ G²/μ  (I(10) = 0.0042304).
The null line δ = 0 is the Einstein mass mode (zero cost; this is the Strategist's relation).
Off the null line the optimal exterior is μw' = −λG with constant λ = −δ/I, i.e.
  w(x) = w₀ − λ[2log(x/ρ) − (4/3)(1/x − 1/ρ) − (1/6)(1/x² − 1/ρ²)]:
v₋ decays like x^{−3/2}log x and the exterior carries a nonzero constant λ, the costate conjugate to
the cyclic variable θ of the quadratic exterior problem. The finite-X exact-collar version
(w(X) = θ(X) = 0) is solved in closed form in `scripts/exterior_null_line.py`; for fixed entrance data
its excess over E_ext behaves like (log X)²/X².

## 3. Stationary large-collar cells: the old terminal gradients were an optimizer artifact

`scripts/perp_lm.py` minimizes J₆ as a sum of squares of the exact Cartan spin residuals
(z/2, (s+24)/4)·√(weight) with a trust-region least-squares Jacobian method. Its residual sum agrees
with the independent DualCell curvature evaluation to 1e−7–2e−6 for X ≤ 512 (to 1e−5 at X = 1024,
where float cancellation at large x becomes visible; X = 1024 values are not used).
Converged in seconds from the earlier L-BFGS records (gradients 1e−6–1e−8 instead of 3e−3–8e−3):

| x₀ | X | deg | J₆ (float) | earlier L-BFGS |
|---|---|---|---|---|
| .03 | 64 | 16 | 0.9957372 | 0.9958547 |
| .03 | 128 | 24 | 0.9955740 | 0.9956702 (certified ≤0.9956711) |
| .03 | 256 | 24 | 0.9955188 | 0.9956012 |
| .03 | 512 | 28 | 0.9955003 | — |
| .038 | 128 | 24 | 0.9952870 | — |
| .038 | 256 | 24 | 0.9952045 | — |
| .038 | 512 | 28 | 0.9951812 | — |

Bolt-area scan at X = 256 (`data/perp_tail/area/`): x₀ = .015 → .99767, .02 → .99677,
.025 → .99604, .033 → .99532, .035 → .99524, .037 → .99521, .038 → .99520, .039 → .99521,
.04 → .99523, .043 → .99536, .046 → .99558, .05 → .99603, .07 → 1.00079.
At X = 512: .036 → .995196, .038 → .995181, .04 → .995210, .042 → .995274.
The optimal bolt area moved from ≈.03 (an artifact of unconverged optimization) to x₀ ≈ .038.

Exact autodiff Hessian at x₀ = .038, X = 256 (`scripts/cell_hessian.py`,
`data/perp_tail/hess_x00.038_X256_d24.json`): one exact null eigenvalue (the overwritten
coefficient cG[0], a parametrization redundancy), all others positive, the smallest 1.9e−6 and
3.8e−6, then 1.8e−4. The full Newton step predicts a further decrease of only 4×10⁻¹⁰. The record is
a strict local minimizer within the 72-parameter ansatz (modulo the redundancy).

Arb certification of the LM records is running (tasks s19_t25_tool1, s19_t32_tool1; outputs under
`data/perp_tail/rig/` and `rig038/`). Until those complete, the numbers above are floating values.

## 4. The far field of the stationary cells is the exact exterior response

`scripts/tail_mode_decomposition.py` computes the gauge-invariant θ = log(a₁/a₃), v₋, v₊,
u₂ − 3a₁a₃ along the cells. For the LM cells, v₋/f₋ is *not* a plateau but grows logarithmically,
and `exterior_null_line.py` shows that it is exactly the off-null exterior response:

| cell | λ fitted on [4, X/8] | λ = −δ/I from the trace at ρ = 10 | predicted cost beyond 10 | actual J beyond 10 |
|---|---|---|---|---|
| x₀=.03, X=512 | 0.1508 | 0.1498 | 1.030e−4 | 1.017e−4 |
| x₀=.038, X=512 | 0.1833 | 0.1827 | 1.531e−4 | 1.500e−4 |

(The sign convention is that λ_fit multiplies −L(x).) Beyond x = 10 the whole cost is the linear
antisymmetric exterior response to 1–2%; the symmetric sector and scalar curvature are negligible
there (|v₊| ≲ 4e−5, J − P ≈ 3e−8). The entrance trace is about 21% off the null line
(δ = −7.7e−4 against null moment −3.7e−3 for x₀ = .038). The core chooses to pay 1.4e−4 in the
exterior. The minimizer does **not** become asymptotically Einstein at the mass order: it carries the
constant far-field charge λ ≈ 0.18.

Finite-collar convergence follows from the same formula. For the x₀ = .03 trace the predicted
fixed-trace excesses are 9.45e−5, 2.70e−5, 8.0e−6 at X = 128, 256, 512. The predicted differences
j(256) − j(512) = 1.89e−5 match the observed 1.85e−5. The 128→256 prediction of 6.8e−5 is reduced to
the observed 5.5e−5 by core readjustment. For x₀ = .038 the excess at X = 512 is 1.2e−5.
Extrapolated infinite-collar diagonal value at x₀ ≈ .038: **j∞ ≈ 0.99517**
(η∞ ≈ 0.0048, balanced upper coefficient 4 − 8η/9 ≈ 3.99573). This is an extrapolation, not a
certified value.

## 5. Consequences

1. *Construction.* Converged diagonal cells improve the explicit deficit from η = .00433
   (certified X = 128, x₀ = .03) to ≈ .00480 (float, x₀ = .038, X = 512). Pending certification, the
   balanced coefficient is ≈ 3.9957 + ε. Earlier statements that large-collar profiles had
   "non-small terminal gradients" are superseded: the stationarity problem inside the ansatz is
   solved, and the Hessian is positive.
2. *Structure of the infinite-collar minimizer.* It is asymptotically CH with an anisotropic,
   contact-plane (weight-two, a₁↔a₃-odd) far field v₋ ≈ f₋(A − 2λ log x), θ ~ x⁻², at the ρ⁴ order of
   ACH asymptotics, with a nonzero conserved exterior charge λ. This is the far field that produced
   the phase-locked weight-four pair interaction of Steps 13–14; the interaction of two cells is
   therefore governed by λ and A, and the shared-exterior problem of Step 12 reduces in the minus
   channel to the explicit μ, G, I kernels above.
3. *Lower theory.* For the diagonal problem the unbounded collar can be replaced by the exact
   transparent condition E_ext = δ²/I(ρ), plus quadratic symmetric terms and nonlinear corrections.
   The minimization becomes a compact problem on [bolt, ρ] with a known terminal penalty, which is
   the finite-interface core problem needed for an HJ subsolution with a terminal cost.
   The terminal penalty is only justified for competitors that are in the linear regime at ρ. A
   lower theorem still needs an exterior bound for traces far from CH. A competitor ending far from
   CH at ρ is not penalized by this formula, and P_core with free end can vanish (local Einstein
   bolt solutions), so the global exterior estimate remains the essential missing piece.
4. *Where the saving is.* The x₀ = .038 split (X = 512) is J_core(x ≤ 5) = 0.99466,
   J(5 < x ≤ 10) = 3.7e−4, J(x > 10) = 1.5e−4. Essentially the whole deficit is made at x ≲ 5, where
   the Step-17 failure band of the Chern–Simons primitive lies (u₂ ≈ 2 around x ≈ 2/3).



---

## Source step21_conformal_selection_su2_stability_constrained_HJ.md

Original: [sources/Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md](../sources/Sessions/S1003A01/workspace/notes/step21_conformal_selection_su2_stability_constrained_HJ.md)

# Step 21 — Conformal selection identity, SU(2) symmetry-breaking stability, and the scalar-constrained HJ problem

Normalization: Ric_CH = −6g, s_CH = −24, e = s+24, Δ = div grad (nonpositive), costs in units of 8π² unless stated.
All curvature integrals in four dimensions.

## 1. An exact conformal identity and the conformal-selection theorem

**Pointwise scalar identity (any u>0, no equation).** For ĝ = u²g in dimension four,
ŝ = u^{-3}(−6Δu + s u) and dV̂ = u⁴dV, hence

  ŝ² dV̂ = (s − 6Δu/u)² dV.                                            (1.1)

Combining (1.1) with pointwise conformal invariance of |W|²dV and the Gauss–Bonnet formula
P = ½∫|W|² + (1/12)∫s² − 16π²χ (closed case; on a cell the Pfaffian changes by an exact
transgression), one gets for any positive u

  P(ĝ) − P(g) = ∫[ −sΔu/u + 3(Δu/u)² ] dV_g  (+ boundary/transgression terms).          (1.2)

**Theorem 1 (exact Yamabe gap).** Let ĝ = u²g have constant scalar curvature −κ, κ>0, i.e.
s = −κu² + 6Δu/u. If boundary terms vanish (closed M, or the decay below), then

  P(g) − P(ĝ) = κ∫|∇u|²_g dV_g + 3∫(Δu/u)² dV_g ≥ 0,                                  (1.3)

and for κ = 24, with J₆ = P + ¼∫e²,

  J₆(g) − J₆(ĝ) = ∫[ 3(Δu/u)² + 24|∇u|² + e²/4 ] dV_g,   J₆(ĝ) = P(ĝ).                 (1.4)

Equivalently 3(Δu/u)² = (e + 24(u²−1))²/12. Equality holds iff u ≡ 1. Proof: insert
s = −κu² + 6Δu/u into (1.2) and integrate −κ∫uΔu = κ∫|∇u|². ∎

Consequences.
* On a closed manifold with negative Yamabe class this is an exact form of the inherited fact
  δ = S(g) − S(ĝ) ≥ 0 (conventions file, line 57; source
  `Skills/geometric-analysis/research/sources/continuation/20260927_conformal_separation_and_zero_end.md` §3):
  in the inherited s=−4 normalization δ = 48∫|∇u|² + 36∫(Δu/u)². Inherited (3.10) gives
  δ/R ≤ 3(E−α)/(1−α) for every E-minimizing sequence; with (1.3) this now forces
  ∫|∇u|²/R → 0 and ∫(Δu/u)²/R → 0 for the conformal factors to the Yamabe metrics, a quantitative
  conformal-factor control that the inherited text records as not supplied (it still gives no
  geometric compactness).
* The constant-scalar representative is the **unique minimizer of both J₆ and P in its conformal
  class** (apply (1.3)/(1.4) to any g in the class with u the factor to ĝ).

**Theorem 2 (cell version).** Let g be a complete metric on a cell, equal to (or exponentially
asymptotic to) CH outside a compact set K, with s<0 everywhere. Then there is a positive solution
of −6Δu + su + 24u³ = 0 with u → 1, and u − 1 = O(e^{−(2+2√3)r}) with derivatives; (1.4) holds.
Sketch: s ≤ −c < 0 globally (s = −24 off K), so u₋ = (c/24)^{1/2} ≤ 1 and u₊ = (max(−s)/24)^{1/2} ≥ 1 are
constant sub/supersolutions; Dirichlet problems on exhausting balls with u = 1 give a locally
convergent sequence. Off K, v = u−1 solves −6Δv + 24u(u+1)v = 0 with positive potential; barriers give
exponential decay, and once v → 0 the potential tends to 48, giving the rate m with m²+4m−8=0,
m = 2+2√3 > 2 (CH volume growth e^{4r}). The Pfaffian transgression and ∮u∂_νu on S_r are
O(e^{(4−2m)r}) → 0. Truncating ĝ back to an exact CH collar at radius R costs O(e^{(4−2m)R}) → 0 because
J₆ is quadratic at the Einstein background. Hence

  inf_{s<0 cells} J₆ = inf{ P(ĝ) : ĝ complete, CH-asymptotic with the above decay, s_ĝ ≡ −24 }.

The radial factor preserves diagonal (and SU(2)-invariant) Bianchi IX metrics, so the same holds
inside those ansätze. For small e the solution also follows from the implicit function theorem
(linearization −6Δ+48 is invertible). Cells with s ≥ 0 somewhere are not covered; note
6λ₀(CH²) + s_CH = 6·4 − 24 = 0, so the conformal Laplacian of CH sits exactly at the bottom of its
spectrum, and existence with u → 1 needs an argument there. (This is the infinite-ended version of
the Strategist's flow identity dJ₆/dτ = −4∫(|∇s|²+6e²).)

**Numerical check of (1.4)** — `workspace/scripts/yamabe_cell_check.py`, data `workspace/data/yamabe/`.
The radial BVP is solved by Newton on a log-x finite-volume grid out to 10⁴X with zero flux at the bolt;
J₆(ĝ) is computed *directly* from Ric_ĝ = Ric − 2(Hess f − df²) − (Δf + 2|df|²)g, f = log u
(second derivative of f from the equation), so agreement tests the integrated identity.

| cell | grid N | J₆(g)−J₆(ĝ) direct | RHS of (1.4) | P(g)−P(ĝ) direct | 3∫(Δu/u)²+24∫|∇u|² |
|---|---|---|---|---|---|
| x₀=.038, X=128 | 3·10⁴ | 4.5837e−7 | 4.5839e−7 | 1.1252e−7 | 1.1255e−7 |
| x₀=.038, X=128 | 1.5·10⁵ | 4.5844e−7 | 4.5843e−7 | 1.1260e−7 | 1.1258e−7 |
| x₀=.038, X=512 | 1.5·10⁵ | 4.430e−8 | 4.444e−8 | 1.081e−8 | 1.095e−8 |

u ∈ [0.999972, 1.0000001] (X=128), u(X) − 1 ≈ 10⁻⁹. The Yamabe metrics give complete s ≡ −24 metrics with
J₆ = P ≈ 0.9952872585 (X=128) and ≈ 0.9951781423 (X=512) (stored J minus the gain). The gain is
≈ 1.33 × the scalar energy, the upper end of the linear prediction ratio ∈ (1, 4/3), confirming that the
residual scalar defect of the spectral cells is high-frequency (also seen in Step 20's Le_sup ≫ e_sup).
These are tiny upper-bound improvements; the value of Theorem 2 is structural: the scalar channel is
removed from the infinite-ended cell problem for all competitors with s<0, not just diagonal ones.

## 2. Non-diagonal SU(2)-invariant second variation: the diagonal optimum is stable

`workspace/scripts/su2_offdiag_hessian.py`, `su2_offdiag_spectrum.py`; data `workspace/data/su2_offdiag/`.
General SU(2)-invariant metrics dx²/(4G) + h_ij(x)σ_iσ_j; full coordinate curvature by autodiff (peer
`curvature_scalars`, Euler-angle coordinates), valid for non-diagonal h. Perturbations of the converged
x₀=.038 cells:
* k_ij = N_ij u²(1−u)³ Σ c_m T_m(2u−1), N₁₂ = x, N₁₃ = N₂₃ = x√(1+x). u² ∝ r⁴ at the bolt is exactly the
  order required for smoothness of the σ₁σ_{2,3} cross terms (circle weight 2) and of the σ₂σ₃
  anisotropy (weight 4); (1−u)³ gives C² contact with the collar.
* bolt rotations (the remaining smooth directions): exact rotation by ψχ(u), χ = (1−u)³(1+3u+6u²) = 1+O(u³),
  implemented as the isometric rotation by ψ(χ−1) (a global rotation is right translation), which avoids
  float cancellation at the collapsed fibre. A first attempt with the *linearized* rotation [Ψ,h] gave
  −1.4×10⁷: that path makes h indefinite at the bolt (11-entry 0, off-diagonal x₀ψ) and is inadmissible; it is
  superseded.

Results (J₆ Hessian; consistent J₀ = 0.99528772 (X=128), 0.99517819 (X=512); gradient ≤ 2×10⁻¹¹; off-block
entries ≤ 10⁻¹³, confirming that the three sign-flip characters of Z₂×Z₂ ⊂ Aut(su(2)) decouple the channels and
kill the first variation):
* Generalized eigenvalue in the norm ∫(k_ij/N_ij)²du, X=512: μ_min(h₁₂,h₁₃,h₂₃) =
  83.5/262.7/476.8 (n=6), 80.37/261.4/462.4 (10), 80.15/260.9/462.3 (14), 80.134/260.68/462.25 (20),
  80.129/260.65/462.25 (26); identical at nq=2000. Converged and strictly positive. X=128: 68.9/222.7/394.6.
* Bolt rotation toward the CH fibre slot (h₁₃): Schur complement 0.6053 (X=512; n=10,16,24, nq=1200/2400 stable),
  0.6046 (X=128) — a genuine positive twist stiffness.
* Bolt rotation in the (1,2) plane: Schur 3.2e−5 → 2.0e−6 → 1.1e−6 (n=10,16,24) → 0, the exact U(1) zero mode
  (constant rotation in a plane where the collar has a₁ = a₂; this is the phase θ of the Step-13 pair interaction).

So, within SU(2)-invariant metrics, the diagonal perpendicular optimum is a strict local minimum modulo the U(1)
symmetry. Breaking diagonality without breaking SU(2) does not lower the cell cost at second order. Any
symmetry-breaking improvement must use non-SU(2)-invariant (e.g. U(1)×U(1) or no symmetry) perturbations; the
natural next object is the Peter–Weyl decomposition of the J₆ Hessian into SU(2)-isotypic ODE systems (with the
diffeomorphism gauge quotiented), starting with the lowest nontrivial isotypes.

## 3. The scalar-constrained Hamilton–Jacobi problem

By Theorem 2 the diagonal lower problem may be posed on s ≡ −24, where J₆ = P. In the Step-17 control
formulation s = Λ − 2Σz with Λ = −8Σa_iH_i/W (`hj_structure.py`, H3), so admissible controls satisfy the
state-dependent affine constraint Σz_i = c(a,u) := (Λ+24)/2. Square completion on that plane gives

  W|z|²/4 − dS/dt ≥ (W/12)(c − Σζ_i)² − H_S,   ζ_i = 2a_iS_{u_i}/W,

so the subsolution requirement weakens from H_S ≤ 0 to H_S ≤ σ_S := (W/12)(c − Σζ)². For the seed S = −kΦ along the
X=128 witness (`hj_scalar_constraint.py`, `data/hj/scalar_constraint_seed_X128.json`): the negative part of the
pointwise margin shrinks from −4.75e−2 to −4.74e−2 (k=1), −2.58e−3 → −1.83e−3 (k=.5), −2.2e−4 → −1.0e−6 (k=.1), but it
never disappears, and small k gives only a small bound. Since σ_S vanishes on the hypersurface c = Σζ, a seed failing on
an open state set still fails there; the constraint helps only after S is redesigned (e.g. with Λ-dependence that keeps
c − Σζ away from zero on the failure band). Thus the constrained HJ problem is the correct, strictly weaker target, but
no certificate follows yet. dΛ/dt is linear in z (printed by `hj_structure.py`), so Λ can also be used as an extra state
coordinate.

## 4. What changed

* The infinite-ended cell problem with s<0 is now exactly a P-minimization over complete s ≡ −24 CH-asymptotic metrics,
  for all metrics, with an exact formula for what Yamabe normalization saves.
* Within SU(2)-invariant metrics the diagonal branch is locally optimal (strict modulo U(1)); further constructive
  progress on 𝔍₁,₀ must break SU(2).
* The diagonal HJ certificate should be sought in the scalar-constrained form.

Open: non-SU(2) second variation (isotypic decomposition), existence for cells with s ≥ 0 somewhere (CH conformal
Laplacian is critical), the finite-interface nonlinear terminal response, the unrestricted 𝔍₁,₀, mixed cells, global
branches. The managed Arb tasks s19_t25_tool1 and s19_t32_tool1 were still running at this note's writing.



---

## Source step22_exact_CH_conformal_reduction.md

Original: [sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md](../sources/Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md)

# Step 22 — Conformal reduction for every smooth exact-CH-ended cell

Normalization: the complex-hyperbolic end has \(\operatorname{Ric}=-6g\), scalar curvature \(s=-24\), and
\[
J_6(g)=\int |\operatorname{Ric}_g+6g|^2=P(g)+\frac14\int(s_g+24)^2.
\]
The Laplacian is \(\Delta=\operatorname{div}\nabla\), so \(\int f\Delta f=-\int|df|^2\) and on \(\mathbf{CH}^2\), for distance from a point,
\[
\Delta r=3\coth r+\tanh r\ge4.
\]

## Theorem

Let \((C,g)\) be a smooth complete connected four-dimensional cell whose marked end is isometric to the exterior distance-sphere end of normalized \(\mathbf{CH}^2\) (or the corresponding finite spherical quotient) outside a compact set. No sign condition on \(s_g\) is imposed. Then:

1. There is a unique smooth positive function \(u\) such that
   \[
   -6\Delta_g u+s_gu+24u^3=0,\qquad u\longrightarrow1
   \]
   on the CH end. Thus \(\widehat g=u^2g\) is complete, asymptotic to the same normalized CH metric, and \(s_{\widehat g}=-24\).
2. For every \(m\) with
   \[
   4<m<2+2\sqrt3,
   \]
   the solution satisfies \(|\nabla^k(u-1)|=O(e^{-mr})\) for every fixed \(k\).
3. The noncompact conformal energy identities have no limiting boundary term:
   \[
   P(g)-P(\widehat g)=24\int_C|\nabla u|^2+3\int_C(\Delta u/u)^2,
   \]
   \[
   J_6(g)-J_6(\widehat g)=\int_C\left[24|\nabla u|^2+3(\Delta u/u)^2+\frac{(s_g+24)^2}{4}\right].
   \]
   Since \(s_{\widehat g}=-24\), \(J_6(\widehat g)=P(\widehat g)\). Equality in the second identity forces \(u=1\) and \(s_g=-24\). In the first identity, constant rescalings give equality on closed manifolds; the end normalization \(u\to1\) removes that freedom here.
4. Let \({\cal C}_{\mathrm{exact}}\) be the smooth exact-CH-ended cell class. For fixed \(\mu>2\), let \({\cal C}_{-24}^{\mathrm{aCH},\mu}\) consist of complete metrics \(h\) on the same marked cell such that \(s_h=-24\) and \(|\nabla_{\mathrm{CH}}^k(h-g_{\mathrm{CH}})|=O(e^{-\mu r})\) for every fixed \(k\). Then
   \[
   \inf_{g\in{\cal C}_{\mathrm{exact}}}P(g)
   =\inf_{g\in{\cal C}_{\mathrm{exact}}}J_6(g)
   =\inf_{h\in{\cal C}_{-24}^{\mathrm{aCH},\mu}}P(h),
   \qquad 2<\mu<2+2\sqrt3.
   \]
   The result is not restricted to an SU(2), diagonal, or Kähler ansatz. The stronger rate \(m>4\) is used to remove the linear transgression in the selection identity for the normalized image of an exact-ended metric; only \(\mu>2\) is needed for direct splicing because its squared residual decays as \(e^{(4-2\mu)R}\). The observed \(r e^{-4r}\) tail belongs to every such class with \(2<\mu<4\). Equality of the infima does not imply attainment. Equality for a class defined by \(\mu\ge2+2\sqrt3\), or for arbitrary \(\mu>2\) without the upper qualification, needs an additional scalar-curvature-preserving gluing or improved decay theorem and is not asserted.

The same existence and selection statement applies inside a symmetry class when the symmetry group preserves the input metric and the CH end: uniqueness makes \(u\) invariant.

## Proof

### 1. Ordered global weak barriers

Choose \(R\) beyond the arbitrary compact core, so \(g\) is exactly CH for \(r\ge R\). Fix any \(a\in(0,4)\). Since \(s_g\) is bounded below on the compact core, choose \(M\ge1\) such that
\[
s_g+24M^2\ge0
\]
everywhere. Define continuous piecewise smooth functions
\[
u_-=\begin{cases}0,&r\le R,\\1-e^{-a(r-R)},&r\ge R,\end{cases}
\qquad
u_+=\begin{cases}M,&r\le R,\\1+(M-1)e^{-a(r-R)},&r\ge R.\end{cases}
\]
They satisfy \(0\le u_-\le u_+\), and both tend to one. Put
\[
F(v)=-6\Delta v+s_gv+24v^3.
\]
On the CH end, writing \(H=\Delta r\ge4\),
\[
\Delta(1-e^{-at})=a(H-a)e^{-at}\ge0,
\]
so
\[
F(u_-)=-6a(H-a)e^{-at}+24u_-(u_-^2-1)\le0.
\]
Similarly
\[
\Delta(1+(M-1)e^{-at})=a(a-H)(M-1)e^{-at}\le0,
\]
and both terms in
\[
F(u_+)=-6\Delta u_++24u_+(u_+^2-1)
\]
are nonnegative. On the core, \(F(u_-)=0\) and \(F(u_+)=M(s_g+24M^2)\ge0\). At \(r=R\), the outward normal derivative of \(u_-\) jumps from \(0\) to \(a\), so the singular part of \(-6\Delta u_-\) is nonpositive. The derivative of \(u_+\) jumps from \(0\) to \(-a(M-1)\), so the singular part of \(-6\Delta u_+\) is nonnegative. Hence these are ordered weak sub- and supersolutions.

On the exhaustion \(\Omega_L=\{r<L\}\), impose \(u=1\) at \(r=L\). Standard ordered sub/supersolution iteration applies after adding a fixed large multiple of \(u\) to make the scalar nonlinearity monotone on \([0,M]\). It gives a smooth solution \(u_L\) with \(u_-\le u_L\le u_+\). Interior elliptic estimates and a diagonal subsequence give a smooth global solution \(u\) with the same bounds. Thus \(u\to1\). It is not identically zero because it is positive on the end. Since it is a nonnegative solution of the linear equation
\[
-6\Delta u+(s_g+24u^2)u=0
\]
with bounded coefficient, the strong maximum principle/Harnack theorem propagates strict positivity through the compact core.

This argument is why the spectral threshold of \(-6\Delta+s_g\) at the zero solution is not an obstruction: the lower barrier is zero only on the compact core and becomes strictly positive on the end.

### 2. Decay and derivatives

Put \(v=u-1\). On the exact CH end,
\[
-6\Delta v+48v+72v^2+24v^3=0.
\]
The first barriers give \(v=O(e^{-ar})\) for each initially chosen \(a<4\). Once \(|v|\) is small, compare with \(Ce^{-mr}\). Since
\[
(-6\Delta+48)e^{-mr}
=6\bigl[-m^2+m(3\coth r+\tanh r)+8\bigr]e^{-mr},
\]
the coefficient is eventually positive for every \(m<2+2\sqrt3\), the positive root of \(m^2-4m-8=0\). A two-sided maximum-principle comparison for the equation with potential \(48+72v+24v^2\) therefore improves the decay to \(|v|=O(e^{-mr})\) for every such \(m\). Interior Schauder estimates on uniformly controlled CH annuli then give \(|\nabla^k v|=O(e^{-mr})\) for every fixed \(k\).

We deliberately use only \(4<m<2+2\sqrt3\). No sharp endpoint asymptotic is needed.

### 3. Boundary terms and exact energy identities

For \(\widehat g=u^2g\) in dimension four,
\[
s_{\widehat g}^2dV_{\widehat g}=(s_g-6\Delta u/u)^2dV_g.
\]
Conformal invariance of \(|W|^2dV\), together with the Chern–Gauss–Bonnet identity on \(C_R\), gives the finite-domain conformal comparison used in Step 21, with a boundary Pfaffian transgression. The difference of the Levi-Civita connections is \(O(|\nabla\log u|)=O(e^{-mr})\), while both background curvature and the second fundamental form of CH coordinate spheres are bounded. The transgression is therefore \(O(e^{-mr})\) pointwise. CH sphere area grows as \(O(e^{4r})\), so its integral is \(O(e^{(4-m)r})\to0\).

The integration-by-parts term \(\int u\Delta u\) has boundary contribution \(\int_{S_r}u\partial_\nu u\), also \(O(e^{(4-m)r})\to0\). Terms quadratic in \(u-1\) or its derivatives decay faster, as \(O(e^{(4-2m)r})\). Letting \(r\to\infty\) in the finite-domain identity proves the two displayed energy formulas. This corrects the overly optimistic Step-21 statement that every boundary term is quadratic: some are linear and require \(m>4\).

The final quadratic energy integrals are already finite for \(m>2\); the stronger choice \(m>4\) is used to remove the linear finite-domain boundary and transgression terms.

### 4. Uniqueness

If \(u_1^2g\) and \(u_2^2g\) both have scalar curvature \(-24\) and \(u_i\to1\), put \(w=u_1/u_2\). Relative to \(g_2=u_2^2g\),
\[
-6\Delta_{g_2}w-24w+24w^3=0,
\qquad w\to1.
\]
If \(w\) has a maximum larger than one, it is achieved in a compact set and at that point both \(-6\Delta w\) and \(24w(w^2-1)\) are positive, a contradiction. A minimum below one gives the opposite contradiction. Thus \(w\equiv1\).

### 5. Equality of infima and exact-collar truncation

The energy identity maps every exact-CH-ended metric to a scalar-normalized complete metric with no greater cost. Conversely, for \(\widehat g=u^2g\) produced above, choose a cutoff \(u_R\) equal to \(u\) inside \(r\le R\) and one outside \(r\ge R+1\), with derivatives uniformly controlled by those of \(u-1\). Then \(g_R=u_R^2g\) is exactly CH outside a compact set, and direct evaluation of the squared Einstein residual gives
\[
J_6(g_R)=P(\widehat g)+O(e^{(4-2m)R}).
\]
No Pfaffian transgression is needed for this cutoff estimate. More intrinsically, for any \(h\in{\cal C}_{-24}^{\mathrm{aCH}}\), splice \(h\) to \(g_{\mathrm{CH}}\) across \([R,R+1]\). The curvature residual in the annulus and discarded tail is \(O(e^{-\mu R})\), so the exact-ended spliced metric has \(J_6=P(h)+O(e^{(4-2\mu)R})\). The selection image of every exact-ended metric decays at every rate \(m<2+2\sqrt3\), so it lies in each fixed class \({\cal C}_{-24}^{\mathrm{aCH},\mu}\) with \(2<\mu<2+2\sqrt3\). Conversely, direct splicing works for every fixed \(\mu>2\). These two directions give equality with the normalized class exactly in the stated range \(2<\mu<2+2\sqrt3\). For larger \(\mu\), splicing still gives only
\(\inf_{{\cal C}_{\mathrm{exact}}}P\le\inf_{{\cal C}_{-24}^{\mathrm{aCH},\mu}}P\); class inclusion does not reverse this inequality. Finally, \(P\le J_6\) on exact-ended metrics, while conformal normalization followed by exact-collar recovery converts any exact-ended \(P\)-competitor into exact-ended metrics with \(J_6\to P(\widehat g)\le P(g)\). Hence the two exact-ended infima are equal.

## Consequences for the Einstein-gap programme

* The scalar channel is eliminated for **all** smooth exact-CH-ended cells, including cells whose scalar curvature is positive somewhere and nonsymmetric cells. The earlier pointwise hypothesis \(s<0\) is unnecessary.
* The unrestricted local upper/lower problem can therefore be posed as minimizing \(P\) on the nonlinear hypersurface \(s=-24\), without assuming diagonal or SU(2) symmetry. A rigorous exact-ended \(P\)-saving is now sufficient for the \(J_6\) transfer after normalization and exact-collar recovery.
* This is an infimum reduction, not existence of a minimizer and not a lower bound for the unrestricted cell value. It does not turn the diagonal numerical value into the global optimum.
* For asymptotically, rather than exactly, CH input metrics, one must additionally state decay of the metric and of the scalar forcing \(s+24\); the theorem above does not silently cover that larger class.



---

## Source step23_scalar_relaxed_j1_CR_pinning_and_certification.md

Original: [sources/Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md](../sources/Sessions/S1003A01/workspace/notes/step23_scalar_relaxed_j1_CR_pinning_and_certification.md)

# Step 23 — Scalar-relaxed angular construction, CR pinning, and long-cell certification

## 1. Exact-ended objective after conformal normalization

The sign-free exact-CH conformal theorem has the stronger consequence
\[
\inf_{{\cal C}_{\rm exact}}P
=\inf_{{\cal C}_{\rm exact}}J_6
=\inf_{{\cal C}^{\rm aCH,\mu}_{-24}}P\qquad(2<\mu<2+2\sqrt3).
\]
Indeed, \(P\le J_6\) on exact-ended metrics. Conversely, normalize any exact-ended \(P\)-competitor to \(\widehat g=u^2g\), so \(P(\widehat g)\le P(g)\) and \(J_6(\widehat g)=P(\widehat g)\), and splice \(\widehat g\) back to an exact collar. The squared residual on the splice is \(O(e^{(4-2\mu)R})\), so \(\mu>2\) suffices for this direction. The reverse comparison with the normalized decay class uses the proved normalization decay only below \(2+2\sqrt3\); equality for arbitrary larger \(\mu\) is not established. The stronger \(m>4\) in the conformal theorem is used to remove the linear Chern--Gauss--Bonnet transgression and integration-by-parts flux in the *selection identity*. In particular, the observed \(r e^{-4r}\) tail belongs to every normalized class with \(2<\mu<4\), but not to the endpoint \(O(e^{-4r})\). The theorem note `step22_exact_CH_conformal_reduction.md` has been corrected accordingly.

This changes the upper-construction standard: a rigorously controlled exact-ended \(P<8\pi^2\) cell is enough for the \(J_6\) transfer after the normalization-and-recovery construction. It does not establish attainment.

## 2. Scalar-relaxed \(j=1\) angular block

Script: `workspace/scripts/angular_isotype_conformal.py`.

The script extends the Step-22 globally smooth angular probe in two ways. Its higher-order runs use the single coefficient \(\sqrt3\,\mathrm{Ad}(q)_{00}\); because the anisotropic base is not right-SU(2)-invariant, that is a compression of the full fixed-left-row \(j=1\) tensor space, which also contains \(\mathrm{Ad}_{01}\) and \(\mathrm{Ad}_{02}\). A `--fullmult` option now includes all three and was run at radial order two.

1. The metric perturbation uses a radial Chebyshev basis multiplied by \(u^2(1-u)^3\), all six off-diagonal orthonormal-frame tensors, and three diagonal differences. The pure trace metric direction is deliberately omitted because it is first-order redundant with the conformal variable.
2. A simultaneous angular conformal field in the same single angular coefficient
   \[
   \phi=\sqrt3\,\mathrm{Ad}(q)_{00}\,u^2(1-u)^4\sum b_nT_n(2u-1)
   \]
   is included. The Schur complement in the \(b_n\) block approximates the optimal scalar response. The script also computes the kernel of the sampled scalar-coupling matrix \(H_{\phi h}\), which approximates tangency to \(Ds[h]=0\).

The Haar mean and Gram matrix are exact to approximately \(2\times10^{-16}\), and the base value at 192 radial nodes is
\[
J_6/(8\pi^2)=0.995178186608463,
\]
within \(5.7\times10^{-13}\) of the independently evaluated stored value.

Canonical data:

- `data/angular_isotype/j1_fullmult_tf_conformal_r2p8_q128.json` (all three fixed-left-row multiplicity components at radial order two)
- `data/angular_isotype/j1_tf_conformal_r2p10_q160.json`
- `data/angular_isotype/j1_tf_conformal_r4p12_q160.json`
- `data/angular_isotype/j1_tf_conformal_r6p16_q192.json`

The full-multiplicity order-two calculation has the expected threefold spectrum and the same minima as the single-coefficient calculation: raw \(0.8957496\), relaxed \(0.8750491\), with positive two-sided line tests. Thus the original single-coefficient pilot did not miss a lower order-two multiplicity direction. The lowest generalized values in the higher-order single-coefficient trace-free basis are:

| radial order | raw | scalar-relaxed | sampled scalar-kernel |
|---:|---:|---:|---:|
| 2 | 0.8957496 | 0.7499216 | 0.8957496 |
| 4 | 0.1782308 | 0.1782308 | 0.1782308 |
| 6 | 0.1209451 | 0.1209451 | 0.1209451 |

All are positive. Here “tested \(j=1\) space” means the full multiplicity only at radial order two and the single-coefficient compression at orders four and six. Two-sided actual-metric line tests at amplitudes \(10^{-3},5\cdot10^{-4},2.5\cdot10^{-4},1.25\cdot10^{-4}\) reproduce the Hessian values; for the order-six lowest direction, the even quotients are about \(0.12094\) and both signs raise \(J_6\). No negative construction direction appears in this tested \(j=1\) space.

In the single-coefficient order-two calculation with a larger conformal basis, scalar relaxation lowers a coupled branch enough that it becomes the new ground branch at \(0.74992\); it does **not** lower the original raw ground eigenvector from \(0.89575\). In the matched full-multiplicity \(n_\phi=8\) calculation the corresponding relaxed triplet is \(0.8750491\). The scalar-coupling matrix detects only orthogonality against the sampled conformal test space, not the pointwise equation \(Ds[h]=0\). At orders four and six the compressed global minimum is numerically in this sampled coupling kernel and has negligible optimal conformal coefficients, but other relaxed levels (notably \(0.28253\) and \(0.14447\)) descend strongly. Thus no negative direction is seen, while the coupled scalar-relaxed sector remains scientifically important.

The decreasing sequence \(0.8957,0.1782,0.1209\) is important: these are finite compression values, not a proof of a positive spectral lower bound. They do not yet cover the full \(j=1\) multiplicity, and the conformal space vanishes at the finite collar rather than carrying the exact decaying exterior solution of \((-6\Delta+48)v=-Ds[h]\). More radial order with all three \(\mathrm{Ad}_{0b}\) coefficients for tensors and scalars, a direct scalar residual solve with transparent exterior response, a better-conditioned localized basis, exact Lie-derivative modes, and geometric gauge quotient are still required. In particular, positive finite blocks do not establish unrestricted local minimality. The two-sided paths are finite first-order conformal responses, not exactly scalar-normalized nonlinear paths; a genuine construction must solve the Yamabe equation for each amplitude and evaluate \(P=J_6\).

A false near-zero branch appeared when the pure trace tensor was allowed simultaneously with the conformal factor. Its metric coefficients were equal in all four diagonal slots and the conformal coefficient cancelled them pointwise. This was parameter redundancy, not a geometric mode; omitting pure trace repaired it. This illustrates why scalar elimination must be formulated geometrically rather than by stacking redundant fields.

## 3. CR-pinning identity checked independently

The peer identity in `S1003A02/workspace/scripts/cr_pinning_check.py` was rerun. With
\[
\widetilde\Phi=q+\frac14(y_g-y_h)-\zeta\sinh q,
\]
the symbolic controlled system gives exactly
\[
\widetilde\Phi'=\zeta^2G-\frac14(e_g-e_h)
=\zeta^2G-\frac14(\mathrm{Ric}^\circ_{gg}-\mathrm{Ric}^\circ_{hh}).
\]
The CH and real-hyperbolic substitutions have zero residual, and a randomly forced numerical solution satisfies the integrated identity to \(6.97\times10^{-16}\). The CH volume factor check gives \(We^{-4t}\to1/16\), so \(\int_T^\infty dt/W\sim4e^{-4T}\). Combining these facts with Cauchy--Schwarz reproduces the peer's sharp pinning scale \(\widehat P\gtrsim\frac12e^{4T}(\Delta\widetilde\Phi)^2\) when the drift is controlled.

This observable is the nonlinear counterpart of the same antisymmetric channel controlled by the Step-19 exterior response. In the linearized CH variables, the interior Rossi mismatch is \(C_{\rm CR}^{\rm int}=k\Theta+\tfrac12w_0G=-\delta/2\), so \(E_{\rm ext}=4(C_{\rm CR}^{\rm int})^2/I\) has the same asymptotic constant \(\tfrac12e^{4T}\) as sharp CR pinning. A unified terminal map should retain the finite-radius canonical port (metric/first jet or \((w_0,\Theta)\)) and may record its derived CR projection, with the nonlinear drift integral accounting for departure from the ACH curve. The two bounds must not be added as independent penalties, since that would count the same antisymmetric mismatch twice. This identification is currently diagonal and antisymmetric; it does not yet control general angular CR deformations.

## 4. Why the corrected long-cell Arb integrations fail

Script: `workspace/scripts/arb_piece_diagnose.py`. Data:

- `data/perp_tail/arb_diag_x0038_X256_p32.json`
- `data/perp_tail/arb_diag_x003_X64_p32.json`

The failure is not a single isolated physical subinterval. Direct complex-box evaluation with equal real and imaginary half-width \(1/64\) makes the Chebyshev exponentials in the spectral representation explode. For the corrected degree-24 \(x_0=.038,X=256\) profile every one of 32 boxes loses denominator separation; \(GH\) and \(G\) enclosures become infinite or cross zero. Even the previously certifiable degree-16 \(x_0=.03,X=64\) profile fails this crude box test at the same width, showing that the test is deliberately much harsher than Arb's adaptive ellipses. Nevertheless it explains why merely splitting the integration interval while retaining global high-degree Chebyshev profiles does not cure the long-cell enclosure: complex growth of the global basis, not loss of positivity on the real metric, dominates the interval dependency.

The constructive repair should change representation rather than increase precision or repeat equal pieces. The profile should be converted into physical-radius subdomains with local low-degree Chebyshev/Taylor expansions, each accompanied by interval remainders and real positivity bounds for \(F,G,e^w\). The already certified \(x_0=.03,X=128\) value remains the transfer input until this local representation is implemented.

## 5. Mathematical interpretation

Scalar elimination is now structurally incorporated into the angular construction search. Within the tested fixed-row \(j=1\) block, it finds no lowering direction after pure-trace redundancy is removed, but the finite Ritz values are still falling with radial order. The next informative angular computation is therefore not another single bump; it is a higher-order full-multiplicity, localized and better-conditioned radial basis plus the exact scalar solve/exterior response, exact Lie-derivative projection, and Ward identities. Independently, CR pinning narrows the diagonal degeneration problem to standard-CR noncollapse, collapsed connectors, large bolts, and other non-Euclidean necks. The unrestricted Einstein-gap problem remains much broader than this cell branch, but these calculations sharpen which local and degeneration mechanisms remain viable.



---

## Source step24_normalized_gauge_resolved_j1.md

Original: [sources/Sessions/S1003A01/workspace/notes/step24_normalized_gauge_resolved_j1.md](../sources/Sessions/S1003A01/workspace/notes/step24_normalized_gauge_resolved_j1.md)

# Step 24: j=1 angular second variation after Yamabe normalization and gauge resolution

Script: `workspace/scripts/angular_normalized_gauge.py`; check: `workspace/scripts/check_bianchi_delta.py`.
Base: `data/perp_direct/lm3_x00.038_X512_d28.json` (x0=.038, X=512). Data: `data/angular_isotype/ng*_*.json`.

## 1. Exact normalized second variation
At a base with s=-24, B=-Δ, σ=Ds[h], the Yamabe-normalized path (u→1 on the CH end) has
Qn(h)=Q_J(h)-D(h), D=(2/3)<σ,(B+6)(B+8)^{-1}σ>=(2/3)(|σ|²-2<σ,(B+8)^{-1}σ>), v=-(1/6)(B+8)^{-1}σ, tangent T=h+2vg.
Bounds: Q_J-(2/3)|σ|² ≤ Qn ≤ Q_J-(1/2)|σ|².
(B+8)^{-1} is solved per angular column by P2 finite elements on the cell plus an exact-CH extension to 100X
(G=x+x², h=diag(x,x,x(1+x)); coefficients continuous at X to 1e-9). σ is exactly in span{F_b} (residual 2e-14).

Checks: pure-trace modes φg have Qn/Q_J ≈ 1e-5 (r4, nel48 nq8) — exact zero expected; v(KX)=divX/4 for
KX=L_Xg-½divX g with median relative error 0.4–0.7% (large relative errors only on modes with divX≈0);
δ and Bianchi map verified: δ(φg)=-dφ and β(L_Xg)=-ΔX-Ric X to 1e-14.
Negative Qn on some KX modes (up to -5) are cancellation errors of 1e-5–6e-4 relative to Q_J≈D≈1e5 on
radial-vector gauge modes with large divX; they are not physical.

## 2. Correction of the angular multiplicity (affects Steps 22–23)
In the euler_E/ad_row0 convention left-invariant vector fields act on the ROW index of R=Rz(ψ)Ry(θ)Rz(φ).
A fixed row is one irreducible copy of the left j=1 representation (angular Laplacian scalar on it: all three
entries gave -0.0078277=-4(2+x)/(x(1+x)) at x=512; σ of row-built seeds has 42% outside the row span).
The genuine multiplicity space is a fixed COLUMN (Laplacian diagonal with distinct entries, e.g. at x=10:
-0.4366,-0.4387,-0.8022, matching CH values 4(2+x)/(x(1+x)) and 8/x). The Step-22/23 'fullmult' runs were
compressions to one copy; their threefold spectra are Schur multiplicity. With columns the spectra are no longer tripled.

## 3. Results (trace-free seeds, 9 tensors × 3 columns × nrad localized C^∞ bumps, u-support [0,0.9])
| nrad | raw min | normalized min | finite-gauge quotient | Bianchi-kernel Ritz |
|---|---|---|---|---|
| 2 | 0.1771 | 0.1379 | 0.380 | 92.6 |
| 4 | 0.0823 | 0.0589 | 0.147 | 192.5 |
| 6 | 0.0474 | 0.0350 | 0.095 (0.105 with nvec 9) | 305.6 |
| 8 | 0.0319 | 0.0253 | 0.076 | 453.1 |
| 10 (nvec 6) | — | 0.0204 | 0.090 | — |

All Qn eigenvalues in every tested space are positive: no descending normalized j=1 direction exists in these spaces.
The falling low values are gauge-dominated: Bianchi ratio |β(T)|²/|T|² of the lowest modes ≈10–15, the same
order as genuine gauge tangents (14–26), while the tf span contains essentially Bianchi-free tensors (ratio ~1e-3);
GT-overlap of lowest modes with the finite K X span 65–98%. The Bianchi-kernel Ritz values grow with nrad, so they are
fine-scale artifacts of the numerical kernel, not a converged physical gap. The physical slice bottom is therefore
not determined (bracketed only loosely). The strategist bounds are not decisive here: |σ|² ≫ Q_J for frame-tensor
seeds (lower bound strongly negative), while the upper bound stays positive.

## 4. Remaining
A converged physical j=1 bottom needs a slice-adapted basis (e.g. parametrize TT/Bianchi-free tensors directly by
solving the radial constraint ODE, or a gauge-fixed operator Qn+c|β|² with c chosen above the lifted gauge band and
convergence in nrad), plus higher isotypes j≥2 and the Ward term of the nearly stationary base. None of this changes
the unrestricted Einstein-gap problem: the cell branch is locally free of tested angular instabilities only.



---

## Source step25_degeneration_matching_and_charge.md

Original: [sources/Sessions/S1003A01/workspace/notes/step25_degeneration_matching_and_charge.md](../sources/Sessions/S1003A01/workspace/notes/step25_degeneration_matching_and_charge.md)

# Step 25 — Controlled collapse charge and bolt matching

## Verified algebra
The peer's controlled scale-free collapse uses
\(x=\log(a_f/a_g)\), \(z=(a_h/a_g)^{1/3}\), \(p=r(\log r)'\), \(\chi=rx'\), \(\eta=rq'\), with \(r=(a_fa_ga_h)^{1/3}\) and \(q=\log(a_g/a_h)\). Under
\[
x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad\chi=Cz+o(z),\quad\eta=Nz+o(z),
\]
the exact spin variables satisfy
\[
u_f=P+\frac23C+\frac13N+2X,\quad u_g=P-\frac13C+\frac13N-2X,\quad u_h=-2.
\]
Therefore
\[
b_+^{\rm end}=2-\sum u_i^2-u_fu_gu_h=-2-(C+4X)^2,
\]
and, with the corrected opposite orientation algebraic normalization,
\[
b_-^{\rm end}=2+(C-4X)^2.
\]
Both are independent of \(P,N\). The consequence is a first-jet charge statement: decollapse to a round orbit costs at least \(4+(C+4X)^2\) in normalized \(\widehat P=P/(8\pi^2)\). This is exact only for the stated controlled jet class; it does not classify arbitrary collapsed first jets.

Independent execution of `Sessions/S1003A02/workspace/scripts/collapse_chiral_charge_limit.py` returned exactly the above limits. TTCS also checked the derivation and found that the source's earlier opposite-charge expression was not geometrically normalized; the corrected form is the one recorded here.

## Smooth bolt matching: what is and is not implied
For the regular Ric=-6 O(-1) bolt (collapsing slot 3), the series source gives
\[
a_f=b+c_2t^2+p_4t^4+\cdots,\quad a_g=b+c_2t^2+q_4t^4+\cdots,\quad a_h=t+r_3t^3+\cdots,
\]
with \(c_2=(3b^2+2)/(2b)\), \(r_3=-2/(3b^2)\), and free anisotropy \(d=p_4-q_4\). Setting \(z=(a_h/a_g)^{1/3}\) gives at fixed \(b>0\)
\[
x=b^3d\,z^{12}+O_b(z^{18}),\qquad\chi=4b^3d\,z^{10}+O_b(z^{16}),
\]
\[
p=\frac1{3z^2}+O_b(z^4),\qquad \eta=-\frac1{z^2}+O_b(z^4).
\]
Thus the local bolt limit has \(b_+\to1\), as required for the bolt charge, and is not the controlled Berger endpoint \(b_+\to-2\). The finite-order series is not uniform as \(b\to0\); it cannot by itself propagate to a scale-one section.

At a scale-one collapsed section with \(a_g\to L>0\), \(a_h/a_g=z^3\to0\), the controlled assumptions \(x=O(z^3)\), \(p,\chi,\eta=O(z)\) are extra global matching information, equivalent to bounded first logarithmic jets / second fundamental form at the section. Smooth bolt regularity alone does not imply them. The scale-one matched Einstein orbit must be analyzed through the full ODE in the overlap region \(t/b\to\infty\), controlling the free parameter \(d(b)\); no relation such as \(C+4X=0\) follows from the bolt series.

The label “finite curvature” for the \(z^3\) class is too strong. For fixed base size, full orbit curvature boundedness requires at least \(x=O(z^6)\), and mixed curvature gives stronger radial control such as \(\chi=O(z^4)\), hence \(X,C\to0\) and charge \(-2\). The \(z^3\) class should be called controlled first-jet / finite-charge. Slot labels must be kept explicit: the bolt collapses slot 3, while `ach_projected.py`'s `f=0` refers to a different fiber slot after cyclic relabeling.

## Collapse warnings from the new data
The raw fixed \(\eta=-8\) entry at \(\varepsilon=1/16\) has \(b_+=1.45193684\), so any omitted prefix from the bolt to that section already costs at least \(0.45193684\) by the chiral annular inequality. With the independently reconstructed prefix plus connector the total is \(\ge1.0264\), so the apparent 0.5454 collocation value is not a regular-cell competitor. At \(\varepsilon=1/32\), the same raw perturbation costs 2.9425. Controlled regular perturbations (including the kernel \(C+4X=0\)) trend toward the charge-four value rather than below the certified 0.99585 cell.

The beta-pinning estimate retains the actual denominator \(\int dt/W\) on a general connector. The exact CH formula \(I(T)\) may only be substituted after proving a pointwise lower comparison for \(W\). The peer's threshold at \(T=.70\) is \(C_*=0.370125\) under that CH-tail comparison.

## Research consequence
The collapsed branch is now split cleanly: (i) controlled first-jet decollapse, where the chiral charge supplies a direct cost (at least 4, or more with shear); (ii) ordinary post-Rossi Berger/ALF connectors, excluded by Euler flux; and (iii) uncontrolled high-shear/raw contact-shear entries, which require an independent prefix/matching estimate. The next theorem-level target is therefore a global small-bolt matching estimate, not another finite-scale raw-entry optimization. The unrestricted lower bound, large-bolt branch, high-shear connectors, non-diagonal collapse, and global closed-manifold transfer remain unresolved.

Artifacts: `workspace/scripts/step25_bolt_matching_orders.py`, `workspace/data/step25_bolt_matching_orders.json`; peer sources `Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md` and `trace/ttcs/results/step30_ttcs01_verifier1_integration.md`.


---

## Source step26_action_budget_matching.md

Original: [sources/Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md](../sources/Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md)

# Step 26 — Action-budget matching for small bolts

## 1. Two different small-bolt limits

The small-bolt question has two mathematically distinct inputs.

### Exact-Einstein degeneration

For a sequence of diagonal Einstein metrics with `Ric = -6 g` and bolt scale `b_j -> 0`, the rescaling `g_j^# = b_j^{-2} g_j` preserves the Einstein equation with rescaled Einstein constant `-6 b_j^2`. A smooth pointed limit can therefore be Ricci-flat. The Taub-bolt / collapsed Lambda–Taub–NUT matching and its unstable triaxial mode are relevant to this sequence, provided the rescaling, convergence, and end extraction are proved.

### Near-minimizing scalar-normalized cells

For a general exact-CH-ended competitor, scalar normalization gives `s(g_j)=-24`, but the cell functional is
\[
\widehat P(g)=\frac{1}{8\pi^2}\int|\operatorname{Ric}^{\circ}|^2.
\]
If `b_j` is the bolt scale and `g_j^#=b_j^{-2}g_j`, then in dimension four
\[
\widehat P(g_j^\#)=\widehat P(g_j),\qquad s(g_j^\#)=-24b_j^2\longrightarrow0.
\]
Consequently a smooth rescaled limit is scalar-flat, but it need not be Ricci-flat when only `\widehat P(g_j)\le c<1` is known. The Einstein bolt series imposes Ricci equations and fixes jets that a general scalar-normalized competitor does not satisfy. Refining its free anisotropy parameter can settle the exact-Einstein branch, but cannot by itself exclude a scalar-flat finite-action core from the cell infimum.

The correct matching problem must therefore retain both possibilities: a Ricci-flat Taub-bolt limit when the defect tends to zero, and a potentially non-Einstein scalar-flat core for a merely subthreshold sequence.

## 2. Exact chiral action budget on a bolt-to-section prefix

For a diagonal annulus the independently verified chiral identities are
\[
\widehat P(C)=\Delta \mathfrak b_+ + \frac{1}{2\pi^2}\int_C|W^+|^2
 +\frac{1}{96\pi^2}\int_Cs^2,
\]
and the same formula with `+` replaced by `-`. All terms after the charge difference are nonnegative.

A smooth `O(-1)` bolt has
\[
\mathfrak b_+=1,\qquad \mathfrak b_-=7.
\]
Therefore, for every diagonal prefix from the bolt to a section `\Sigma`,
\[
\boxed{
\widehat P([\mathrm{bolt},\Sigma])\ge
\max\{0,\mathfrak b_+(\Sigma)-1,\mathfrak b_-(\Sigma)-7\}.
}
\tag{2.1}
\]
The two chiral lower bounds refer to the same prefix energy and must not be added. This statement is exact for the diagonal annulus and does not require the prefix to be Einstein or scalar-flat.

At a controlled collapsed section, with
\[
x=Xz^3+o(z^3),\quad p=Pz+o(z),\quad
\chi=Cz+o(z),\quad \eta=Nz+o(z),
\]
the exact charge limit is
\[
\mathfrak b_+=-2-(C+4X)^2,\qquad
\mathfrak b_-=2+(C-4X)^2.
\]
Thus (2.1) gives
\[
\boxed{
\liminf\widehat P([\mathrm{bolt},\Sigma_j])
\ge \max\{0,(C-4X)^2-5\}.
}
\tag{2.2}
\]
The plus channel is nonpositive at this endpoint and supplies no positive bound; the opposite channel is the useful one.

If the whole competitor has `\widehat P\le c+o(1)`, then every controlled section reached by that competitor satisfies
\[
(C-4X)^2\le c+5.
\tag{2.3}
\]
On the plus-charge kernel `C+4X=0`, this becomes
\[
64X^2\le c+5,
\qquad |X|\le\frac{\sqrt{c+5}}8.
\tag{2.4}
\]
For illustration, if `c=0.99585` (the peer's Step-31 numerical scale; the current Session's authoritative certified transfer remains `0.995671...`), this gives `|X|<0.3061` on the kernel. In particular an order-one kernel entry such as `(X,C)=(1,-4)` cannot be reached within a total action below one. This is a finite-action obstruction to the most favorable normalized kernel search; it does not prove that every bolt sequence enters the controlled class.

## 3. The action-budget matching alternative

Let `\Sigma_j` be the first section at which a collapsing bolt sequence enters a controlled finite-charge class. Then the chiral budget supplies the explicit prefix cost (2.2). There are only two ways for a low-action sequence to avoid this bound:

1. it reaches a controlled section, in which case (2.2)--(2.4) constrain the normalized shear parameters; or
2. no such section occurs before the geometry leaves the collapsed regime, so the sequence remains outside controlled first-jet compactness. The missing estimate is then a direct action bound for the departure from the controlled class, not an Einstein matching statement.

A useful theorem target is therefore an action-budget alternative of the form
\[
\widehat P([\mathrm{bolt},\Sigma])
\ge \Psi(\mathcal D_\Sigma,W_\Sigma),
\]
where `\mathcal D_\Sigma` measures failure of the controlled scale-free expansion and `W_\Sigma=a_fa_ga_h` records the volume weight. The charge identities give the part of `\Psi` depending on `C-4X`; they are blind to the radial variable `P`, the volume/shear variable `N`, and the uncontrolled raw contact rate. The Ricci equations, scalar constraint, and an actual `W^{-1}` estimate must supply these missing terms.

The fibre/base pinning identity has the complementary form
\[
\widetilde B'=F_\beta-\frac14E,
\qquad
\widehat P\ge\frac16\int W E^2\,dt,
\]
so
\[
\left|\Delta\widetilde B-\int F_\beta dt\right|
\le\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2}.
\]
On an exact CH tail the denominator is explicit, but on a general connector it must remain the actual `\int W^{-1}dt`. This identity can price the part invisible to the chiral charges only after the drift `F_\beta` and volume degeneration have been controlled.

## 4. Consequences for the research route

The diagonal degeneration route should now be separated into:

* the exact-Einstein branch, where rigorous Taub-bolt / Lambda–Taub–NUT matching can describe a Ricci-flat rescaled limit;
* the scalar-flat finite-action branch, where nonzero trace-free Ricci energy remains possible and must be included in the compactness statement;
* the raw high-shear branch, where neither controlled charge limits nor the Einstein bolt series apply automatically.

The chiral budget has already removed the order-one plus-kernel entry from the low-action controlled class. The decisive remaining work is a quantitative estimate for the third branch, ideally combining the normalized Ricci equations, the scalar constraint, and fibre/base pinning with the exact chiral budget. This would connect collapse analysis to the unrestricted cell infimum rather than classifying only the zero-defect Einstein family.

## 5. Independent verification and a D-channel pinning identity

The peer's Lemma N was independently re-derived in `workspace/scripts/step26_independent_constraint_and_D_pin.py`; output is `data/step26_independent_constraint_and_D_pin.json`. All five symbolic residuals vanish: the Hamiltonian residual satisfies
\[
\mathcal C=\frac{e_0-e_f-e_g-e_h}{2},
\]
its Bianchi propagation is
\[
\mathcal C'=-2S\mathcal C-\sum_i(S-y_i)e_i,
\]
constant scalar `-24` gives `C=Ric^\circ_{00}` and
\[
S'=18-S^2+R^{(3)}+\mathcal C.
\]
The independent calculation also verifies the exact anisotropy equation
\[
(Wq')'=W(P_g-P_h-D),\qquad q=\log(a_g/a_h),\quad D=e_g-e_h,
\]
with
\[
P_g-P_h=-8z\sinh q+\frac{8z^2}{\kappa^2}\sinh(2q).
\]

For an interval `[T_0,T_1]`, define
\[
K(t)=\int_t^{T_1}\frac{du}{W(u)},\qquad K(T_1)=0,
\]
and
\[
M=q(T_1)-q(T_0)-W(T_0)q'(T_0)K(T_0)
-\int_{T_0}^{T_1}W(P_g-P_h)K\,dt.
\]
Then the exact Green identity is
\[
M=-\int_{T_0}^{T_1}WDK\,dt,
\]
and hence
\[
\boxed{\widehat P_{[T_0,T_1]}\ge
\frac{M^2}{8\int_{T_0}^{T_1}WK^2dt}.}
\]
This is a rigorous D-channel pinning bound for prescribed endpoint data, but it does not become a universal positive lower bound until the Einstein drift `P_g-P_h`, the volume `W`, and the endpoint momentum are controlled.

If on the interval `W(t)\ge W_0e^{\sigma(t-T_0)}` and an upper comparison is also available for the Green denominator, the model exponential weight gives
\[
\int WK^2dt=\frac{1-e^{-2\sigma L}-2\sigma L e^{-\sigma L}}{W_0\sigma^3},\qquad L=T_1-T_0,
\]
so a drift-corrected anisotropy mismatch of order one at volume `W_0` costs order `W_0\sigma^3` unless the Einstein drift itself supplies the change. In a bounded AH/ACH block, the exact drift formula gives the conditional estimate
\[
|P_g-P_h|\le 8z|\sinh q|+8z^2\kappa^{-2}|\sinh(2q)|,
\]
which can be integrated against `WK` and subtracted from the endpoint mismatch. This is the natural D analogue of the volume comparison: it isolates the only zero-cost route (the controlled Einstein drift) and prices all residual q-opening by the full Ricci-defect action.

## 6. Verification correction to Lemma W

The scalar-normalized constraint identities are exact. The proof of Lemma W is valid after stating its bootstrap carefully. Set `E(t)=\int_T^t|\mathcal C|du`. For any first point where `S+E` would fall below `m=min(S(T),A)`, the boundary value satisfies `S=m-E\le A`, so `A^2-S^2\ge0` and `S'+E'\ge0`; thus `S+E\ge m`. While `S\ge\sigma_0`, `W\ge W(T)e^{\sigma_0(t-T)}` and
\[
E(t)\le\left(\int_T^tW\mathcal C^2du\right)^{1/2}
\left(\int_T^tW^{-1}du\right)^{1/2}
\le\left(\frac{3\widehat P_{[T,T_1]}}{\sigma_0W(T)}\right)^{1/2}.
\]
The stated hypothesis closes the bootstrap and yields
\[
S\ge\sigma_0,\quad W(t)\ge W(T)e^{\sigma_0(t-T)},\quad
\int_T^{T_1}W^{-1}dt\le(\sigma_0W(T))^{-1}.
\]
The argument needs `R^(3)\ge-\rho_0` and `A^2=18-\rho_0>0`; no Einstein condition is used. The phrase `while |S|\le A` should be replaced by the first-barrier argument above, since `S(T)` may exceed `A`.

## 7. Charge variation strengthens raw-shear exclusion

The peer's Step-31 Lemma V adds a pathwise form of the chiral budget. Since each chiral identity is pointwise in the orbit parameter,
\[
\frac{W}{4}|\Ric^\circ|^2\ge \max\{0,\mathfrak b_+',\mathfrak b_- '\}
\]
(pointwise derivatives), and therefore
\[
\widehat P([T_0,T_1])\ge\int_{T_0}^{T_1}\max\{0,\mathfrak b_+',\mathfrak b_- '\}\,dt.
\]
In particular, for an `O(-1)` bolt,
\[
\widehat P\ge\sup_t\max\{\mathfrak b_+(t)-1,\mathfrak b_-(t)-7\},
\]
and the positive variation of either charge gives a stronger path-sensitive bound. The raw `\Delta\eta=-8` entry has `\mathfrak b_-=8.54957`, so its bolt prefix alone costs at least `1.54957`, independently of the connector reconstruction. This removes that numerical escape below the certified cell even more decisively than the earlier prefix-plus-connector estimate.

The charge-variation bound still does not price late opening when the charges decrease or remain low. The constrained optimal-control runs with `\mathfrak b_+\le-1` have costs around `6.44--6.62`, while the charge-variation contribution is only about `1.5`; the remaining cost is mainly the `D` channel. Thus the Green identity above is the appropriate next analytic object: it prices residual contact-slot anisotropy after subtracting its geometric drift, whereas the chiral charge prices only characteristic upward motion.

## 8. Status of the main theorem target

The strongest current statement is an action-budget alternative for the diagonal scalar-normalized class, not a completed unrestricted lower bound. A sequence with bounded total `\widehat P` and a controlled collapsed section obeys the exact charge limit and the kernel restriction. A raw high-shear section that raises either chiral charge above the bolt budget is excluded directly by Lemma V. The remaining branch—non-round late opening with low/decreasing charges—must be controlled by the scalar constraint, volume bootstrap, and D-channel Green pinning. The exact equations now separate:

* `C`, the Hamiltonian constraint residual, with pointwise penalty `\int W C^2/3`;
* `D`, the contact-slot anisotropy residual, with the exact Green pinning estimate;
* `E`, the fibre/base residual, controlled by the established `\widetilde B` identity;
* chiral positive variation, which prices upward topology/shape charge changes.

This decomposition identifies the missing lower estimate without assuming that an Einstein separatrix describes every near-minimizer. The exact-Einstein Taub-bolt matching remains relevant only to the defect-to-zero branch; finite-action scalar-flat rescaled cores remain admissible in the subthreshold cell problem.

## 9. A conditional D-analogue of the volume comparison

The exact D Green estimate becomes explicit in an expanding AH/ACH block. Let `[T_0,T_1]` satisfy the separate expanding-block hypotheses
\[
B(t):=y_g+y_h\ge\sigma>0,
\qquad S(t):=y_f+y_g+y_h\ge\sigma>0,
\qquad |q(t)|\le Q,
\qquad \kappa(t)\ge\kappa_0>0.
\]
(The first condition controls the collapsed ratio; the second controls volume.) Since `z'=-Bz`,
\[
z(t)\le z_0e^{-\sigma(t-T_0)},
\quad |P_g-P_h|\le A_Q z_0e^{-\sigma(t-T_0)}+B_Qz_0^2e^{-2\sigma(t-T_0)},
\]
where
\[
A_Q=8\sinh Q,\qquad B_Q=8\kappa_0^{-2}\sinh(2Q).
\]
The volume hypothesis gives `W(t)\ge W_0e^{\sigma(t-T_0)}`. Therefore
\[
K(t)\le\frac{1}{\sigma W(t)},\qquad
\int_{T_0}^{T_1}WK^2dt\le\frac1{\sigma^3W_0},
\]
and the drift term obeys
\[
\left|\int_{T_0}^{T_1}W(P_g-P_h)Kdt\right|
\le \frac{A_Qz_0}{\sigma^2}+\frac{B_Qz_0^2}{2\sigma^2}.
\]
Consequently the following conditional lower estimate is rigorous:
\[
\widehat P_{[T_0,T_1]}
\ge \frac{\sigma^3W_0}{8}
\left(
\left|q_1-q_0-W_0q'_0K_0\right|
-\frac{A_Qz_0}{\sigma^2}-\frac{B_Qz_0^2}{2\sigma^2}
\right)_+^2.
\tag{9.1}
\]
Here `K_0` is the actual Green tail `int_{T0}^{T1}W^{-1}` and `q_1=q(T_1)`. A simpler endpoint version replaces `|W_0q'_0K_0|` by `|q'_0|/sigma`. This is a genuine D-channel counterpart to Lemma W: it prices a residual contact-slot mismatch at initial volume `W_0`, after subtracting the explicit Einstein drift. It applies only after a controlled expanding block has been established; it does not price the initial collapsed or raw high-shear region, where `q` may be unbounded or `kappa` may degenerate.

The bound exposes the research bottleneck sharply. To close non-round late opening, one needs either (i) an expanding block with `sigma`, `Q`, and `kappa_0` uniform and a mismatch exceeding the drift/error budget, or (ii) a separate action estimate for the interval before those hypotheses hold. The first is now a concrete interval-enclosure task rather than a vague D-channel assertion.

## 10. Momentum-renormalized late-opening alternative

A clean two-stage form removes the free incoming `D`-momentum from the one-interval estimate. Let `T_-<T_0<T_1`, `J=Wq'`, and on `[T_0,T_1]` let
\[
K(t)=\int_t^{T_1}W(u)^{-1}du,
\quad K_0=K(T_0),
\quad \Pi=P_g-P_h.
\]
Set
\[
J_-=J(T_-),\quad R_- =\int_{T_-}^{T_0}W\Pi\,dt,
\quad R_+=\int_{T_0}^{T_1}W\Pi K\,dt.
\]
The exact equation `J'=W(Pi-D)` gives
\[
M:=q(T_1)-q(T_0)-(J_-+R_-)K_0-R_+
=-K_0\int_{T_-}^{T_0}WD\,dt-
\int_{T_0}^{T_1}WDK\,dt.
\]
Therefore
\[
\boxed{
\widehat P_{[T_-,T_1]}\ge
\frac{M^2}{8\left(K_0^2\int_{T_-}^{T_0}Wdt+\int_{T_0}^{T_1}WK^2dt\right)}.}
\tag{10.1}
\]
This is stronger than treating `J(T_0)` as an arbitrary endpoint datum: only the flux entering at `T_-` is free, while momentum created inside the preceding interval is charged by the same `D` action.

On `[T_0,T_1]`, assume
\[
R^{(3)}\ge-\rho,
\quad A^2=18-\rho>0,
\quad B=y_g+y_h\ge\mu>0,
\quad S\ge\sigma>0,
\quad |q|\le Q,
\quad \kappa\ge\kappa_0>0.
\]
Let `m=min(S(T0),A)` and choose `0<sigma<m`. The corrected Hamiltonian barrier gives the alternative
\[
S\ge\sigma\quad\text{or}\quad
\widehat P_{[T_0,T_1]}\ge L_C:=\frac{\sigma W(T_0)}3(m-\sigma)^2.
\]
On the expanding branch,
\[
K_0\le(\sigma W_0)^{-1},\qquad
\int_{T_0}^{T_1}WK^2dt\le(\sigma^3W_0)^{-1},
\]
and with `zeta=1/(a_ga_h)`, `zeta'=-B zeta`,
\[
|R_+|\le
\frac{8\zeta_0\sinh Q}{\sigma\mu}
+\frac{4\zeta_0^2\sinh(2Q)}{\sigma\mu\kappa_0^2}.
\]
If `Xi_- = ∫_{T_-}^{T0}W|Pi|dt` and `W_- = ∫_{T_-}^{T0}Wdt`, then
\[
|M|\ge\left(|q(T_1)-q(T_0)|-
\frac{|J_-|+\Xi_-}{\sigma W_0}-\Lambda_+\right)_+,
\]
with `Lambda_+` the displayed drift bound, while the Green denominator is at most
\[
H=\frac{W_-}{\sigma^2W_0^2}+\frac1{\sigma^3W_0}.
\]
Hence
\[
\boxed{
\widehat P_{[T_-,T_1]}
\ge\min\left\{L_C,\frac{\Delta_q^2}{8H}\right\}.}
\tag{10.2}
\]
The estimate is conditional and reusable: it prices a residual contact-slot change after explicitly subtracting inherited momentum and Einstein drift. It does not assert a universal positive late-opening constant, because exact Einstein arcs can carry arbitrary incoming anisotropy momentum with zero defect action. The correct global statement is an alternative: upward chiral variation, Hamiltonian loss of expansion, or a momentum-renormalized `D` mismatch must occur, unless the trajectory follows a globally compatible Einstein mode.

This also explains the peer's numerical `D`-dominated non-round opening. Charge variation sees only the upward part of characteristic flux; the residual opening is supplied by `D` after subtracting `J_-` and `Pi`. A theorem for all near-minimizers must bound the incoming flux from the bolt or prove that producing it already consumes the action. Exact-Einstein matching alone cannot supply that bound for scalar-normalized competitors.



---

## Source step26_step_summary.md

Original: [sources/Sessions/S1003A01/workspace/notes/step26_step_summary.md](../sources/Sessions/S1003A01/workspace/notes/step26_step_summary.md)

# Step 26 summary — action-budget matching, constraint pinning, and late opening

The small-bolt route was rebuilt around a distinction that prevents an invalid Einstein reduction. For exact Einstein metrics with bolt scale b→0, rescaling by b^{-2} gives Ric=-6b²g# and any sufficiently smooth pointed limit is Ricci-flat. For scalar-normalized near-minimizers with only P-hat≤c<1, the same rescaling leaves P-hat invariant and sends s=-24 to -24b², so a smooth limit is only scalar-flat; nonzero trace-free Ricci action can remain. The regular Einstein bolt series therefore studies only the exact-Einstein branch, not the full cell infimum.

The verified chiral identities imply an exact bolt-to-section budget. For an O(-1) bolt, b+=(1), b-=7, and every diagonal prefix obeys
P-hat_prefix ≥ max{0,b+(Σ)-1,b-(Σ)-7}; retaining the common scalar term gives the stronger max{0,b+-1+SΣ,b--7+SΣ}, where SΣ=(96π²)^{-1}∫s². The two chiral estimates are for the same action and must not be added. Controlled collapsed first jets x=Xz³, p=Pz, chi=Cz, eta=Nz have b+=-2-(C+4X)² and b-=2+(C-4X)². Thus a bounded total action c forces (C-4X)²≤c+5. On the plus kernel C+4X=0, 64X²≤c+5; at c=.99585 this gives |X|≤.306081, so (X,C)=(1,-4) would cost at least 59 in the minus channel. This is an asymptotic controlled-section result, not an all-sequence matching theorem. The raw eta=-8 numerical entry is excluded even more strongly: its b-=8.54957, so its bolt prefix costs at least 1.54957.

I independently re-derived the peer's scalar-normalized constraint equations with zero symbolic residuals in `scripts/step26_independent_constraint_and_D_pin.py`, output `data/step26_independent_constraint_and_D_pin.json`. The Hamiltonian residual C=(e0−Σei)/2 equals Ric°00 at s=-24, propagates by C'=-2SC−Σ(S−yi)ei, and S'=18−S²+R3+C. I independently derived the exact contact-slot equation
(Wq')'=W(Pg−Ph−D), q=log(ag/ah), D=eg−eh,
with Pg−Ph=−8z sinh q+8z²kappa^{-2}sinh(2q). A Green identity gives a drift-corrected D pinning bound P-hat≥M²/[8∫WK²], but only after controlling endpoint momentum, volume, and geometric drift.

A first-barrier correction makes Lemma W sound: if R3≥−rho0, A²=18−rho0>0, m=min{S(T),A}, and the stated C-action smallness holds, then S≥sigma, W grows at least exponentially, and ∫W^{-1}≤(sigma W(T))^{-1}. The proof must use the first point at which S reaches sigma; it does not require S(T)≤A.

A stronger two-stage Green identity now removes the free momentum at the beginning of an expanding block. For T−<T0<T1, J=Wq', K(t)=∫_t^{T1}W^{-1}, and Pi=Pg−Ph, the renormalized mismatch
M=q(T1)−q(T0)−(J(T−)+∫_{T−}^{T0}W Pi)K(T0)−∫_{T0}^{T1}WPiK
satisfies
M=−K(T0)∫_{T−}^{T0}WD−∫_{T0}^{T1}WDK.
Therefore P-hat over both intervals is bounded below by M² divided by 8 times the corresponding Green denominator. In an expanding block with S≥sigma, B=yg+yh≥mu, |q|≤Q, kappa≥kappa0, one obtains explicit bounds on K and Pi drift; if expansion fails, the Hamiltonian residual already costs sigma W(T0)(m−sigma)²/3. The resulting alternative is: upward chiral charge variation, Hamiltonian loss of expansion, or a momentum-renormalized D mismatch. Exact Einstein arcs show why no hypothesis-free positive late-opening cost can follow from q change and a one-sided charge cap alone.

This step materially advances the central lower-bound route but does not close it. The remaining theorem-level work is to establish a global entry/exit estimate for the expanding-block hypotheses and the incoming flux produced before them, while retaining scalar-flat non-Einstein rescaled cores. The D pinning script and the exact chiral budgets are reusable tools for that task. Large-bolt face asymptotics remain numerical; the certified global construction is unchanged.



---

## Source step28_AK_gap_identity_nijenhuis_transport.md

Original: [sources/Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md](../sources/Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md)

# Step 28 — The canonical almost-Kähler gap identity for perpendicular cells

Scope: smooth diagonal Bianchi-IX \(O(-1)\) cells with an exact CH collar (perpendicular class:
the collapsing slot \(h\) is not the CH fibre \(f\)). Units: \(\widehat P=P/(8\pi^2)\), volumes in
\(\int W\,dt\) units, \(W=a_fa_ga_h\), \(d\sigma_i=2\sigma_j\wedge\sigma_k\). Everything below is
exact (symbolic) unless stated as numerical. Scripts: `scripts/step27_flux_laws.py`,
`step27_cell_flux_budget.py`, `step28_ak_hatted_structure.py`, `step28_ak_nu_structure.py`,
`step28_ak_gap_identity.py`; data in `data/step27/`, `data/step28/`.

## 0. Step-27 results carried forward (consolidated)

* Orthogonal channels: \(|\mathrm{Ric}^\circ|^2=\tfrac43C^2+\tfrac23E^2+\tfrac12D^2\), so
  \(\widehat P=\int W(C^2/3+E^2/6+D^2/8)dt\); \(C=\mathrm{Ric}^\circ_{00}\), \(E=e_f-(e_g+e_h)/2\), \(D=e_g-e_h\).
* Bolt-anchored flux laws: \((Wq')'=W(\Pi_q-D)\), \((W\beta')'=W(\Pi_\beta-E)\),
  \(q=\log(a_g/a_h)\), \(\beta=\log(a_f/\sqrt{a_ga_h})\); at a smooth bolt \(Wq'\to-b^2\), \(W\beta'\to-b^2/2\);
  on CH \(Wq'=0\), \(W\beta'=\sinh^4R\). Hence \(\int WD=\int W\Pi_q-b^2\), \(\int WE=\int W\Pi_\beta-X^2-b^2/2\).
  Closed drifts \(W\Pi_q=4(a_g^2-a_h^2)(a_g^2+a_h^2-a_f^2)/W\),
  \(W\Pi_\beta=[4a_f^4-2a_f^2(a_g^2+a_h^2)-2(a_g^2-a_h^2)^2]/W\).
* Coupled Bianchi: \((W^{4/3}C)'=W^{4/3}[\tfrac23\beta'E+\tfrac12q'D+s'/4]\).
* Relative Weyl–volume identities (all exact-CH \(O(-1)\) cells):
  \(1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc}\), \(\widehat P=-5+\int W|W^-|^2+12V_{\rm exc}+S_{\rm exc}\),
  \(D_+=\int W(24-|W^+|^2)\), \(S_{\rm exc}=\int W(s^2/48-12)\).
* Sign correction: \(b_+=2-|v|^2-v_1v_2v_3\), \(v_i=a_i'-\gamma_i\),
  \(\gamma_i=(a_j^2+a_k^2-a_i^2)/(a_ja_k)\); self-dual curvature
  \(R^+_{ii}=-v_i'/(2a_i)+(-v_i-v_jv_k/2)/(a_ja_k)\) (diagonal in \((e^{0i}+e^{jk})/\sqrt2\)).
  Pointwise \(|W^+|^2\) values computed from the opposite product sign are superseded.

| \(x_0\) (X) | \(\widehat P\) | \(C\) | \(E\) | \(D\) | \(V_{\rm exc}\) | \(D_+\) |
|---|---|---|---|---|---|---|
| .015 (256) | .99767 | .317 | .166 | .515 | .00230 | .0913 |
| .038 (128) | .99529 | .299 | .164 | .532 | .00677 | .2586 |
| .07 (256) | 1.00076 | .291 | .161 | .549 | .01347 | .4951 |

## 1. Every diagonal cell is conformal to a diagonal almost-Kähler metric

Let \(\omega=d(\mathcal P\sigma_f)\), \(\mathcal P'/\mathcal P=2a_f/(a_ga_h)\), normalized by \(\mathcal P=a_ga_h\) on the CH
collar (this is \(2\Omega\) for the AAD-normalized form \(|\Omega|^2_{\hat g}=2\); the script's \(\phi\) equals this \(\mathcal P\));
\(\mathcal P\sim Ct^2\) at the bolt. Put \(u^2=\mathcal P/(a_ga_h)\) (=1 on CH), \(\hat g=u^2g\). \(\hat g\) is almost-Kähler on the
complement of the bolt only; at the bolt \(u^2\sim ct\), \(T\sim\tfrac23\sqrt c\,t^{3/2}\), \(A_f,A_g\asymp T^{1/3}\), \(A_h\asymp T\): an
anisotropic power-law singular end (not a cone), across which all densities and Stokes fluxes are integrable/vanishing.
Then \(\hat g=dT^2+\sum A_i^2\sigma_i^2\) with \(dT=u\,dt\), \(A_i=ua_i\), is again diagonal and
\(|\omega|_{\hat g}\) is constant exactly when

\[
A_f=\tfrac12\,(A_gA_h)_T .\qquad\text{(AK constraint)}
\]

Write \(A_g=\sqrt{\mathcal P}e^{q/2}\), \(A_h=\sqrt{\mathcal P}e^{-q/2}\), \(A_f=\mathcal P_T/2\) (note \(q\) is
conformally invariant). Symbolic computation (`step28_ak_hatted_structure.py`,
`step28_ak_nu_structure.py`) gives, for every such metric:

* the two rotating self-dual connection coefficients obey \(A_hv_g=-A_gv_h\); the **Nijenhuis
  scalar** is
  \[
  \nu=\frac{v_h}{A_h}=-\frac{v_g}{A_g}=-\frac12\Big(q_T+\frac{4\sinh q}{A_f}\Big),\qquad
  \kappa-\hat s=6\nu^2 ,
  \]
  (\(\kappa=6\widehat W^+_{\omega\omega}\) the conformal scalar curvature, AAD (10): \(\kappa-s=6|a|^2\)).
  So \(\hat g\) is Kähler iff \(q\) follows the Kähler squashing flow \(q_T=-4\sinh q/A_f\);
* \(W_3^+\) eigenvalue \(\lambda=(\widehat W^+_{gg}-\widehat W^+_{hh})/2\) satisfies the **linear transport law**
  \[
  \lambda=\tfrac12\nu_T+\beta\nu,\qquad \beta=-\frac{(A_f)_T}{2A_f}+\frac{2\cosh q}{A_f};
  \]
  (the \(|a|^2\) term of AAD (13) cancels in this gauge); \(W_2^+=0\) by symmetry;
* \(J\)-anti-invariant Ricci of \(\hat g\):
  \(\widehat D=2\nu_T+\nu(2A_f'/A_f-8\cosh q/A_f+4A_f/(A_gA_h))\),
  \(\widehat{\mathrm{Ric}}_{00}-\widehat{\mathrm{Ric}}_{ff}=-2\nu^2-8\nu\sinh q/A_f\); both vanish iff \(\nu=0\);
* **Chern identity as an exact Stokes formula** (`step28_chern_stokes_check.py`, residual 0): the Hermitian/Chern scalar
  \(s^\nabla=(\hat s+\hat s_{\rm star})/2=\hat s+2\nu^2\) (the usual star scalar is \(\hat s+4\nu^2\); below \(\hat s^*\) means \(s^\nabla\)) and
  \[
  \hat s^*\,A_fA_gA_h=\frac{d}{dT}\Big[4\mathcal P\cosh q-\mathcal P\mathcal P_{TT}-\tfrac12\mathcal P_T^2\Big].
  \]
  The bracket vanishes at the bolt (\(A_gA_h\sim t^2\), \(A_gA_hA_f'\sim t\)) and equals \(-6X^2\) on CH,
  so \(\int\hat s^*d\hat V=-6X^2=-24V_{\rm CH}\) exactly: the conical bolt contributes nothing.
  Pinning is the Stokes formula \(\int d\hat V=[\mathcal P^2/4]=V_{\rm CH}\).

## 2. The exact gap identity

Define \(H=\int(u^2-1)^2W\), \(G=\int u'^2W\), \(N=\int4\nu^2d\hat V\), \(Q_A=\int4\lambda^2d\hat V\),
\(Q_\delta=\int(\widehat W^+_{\omega\omega}+4)^2d\hat V\), \(d\hat V=u^4W\,dt\).

**Theorem A.** For every smooth diagonal exact-CH perpendicular \(O(-1)\) cell,
\[
\boxed{\widehat P-1=12H+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N+\Sigma},\qquad
\Sigma=\int W(s+24)(u^2-1)+\int W\frac{(s+24)^2}{48},
\]
and \(V_{\rm exc}=H+G/2+N/24+\frac1{12}\int(s+24)u^2W\). For \(s\equiv-24\), \(\Sigma=0\).
Since \(12(u^2-1)^2+(s+24)(u^2-1)+(s+24)^2/48=12(u^2+s/24)^2\), the identity holds **for every \(s\)** in the form
\[
\widehat P-1=12H_s+6G+\tfrac32Q_\delta+\tfrac12Q_A-\tfrac32N,\qquad H_s=\int W\,(u^2+s/24)^2dt ,
\]
so \(-\tfrac32N\) is the only negative term without any scalar normalization.

Proof. (i) \(|W^+|^2=\tfrac32W_{\omega\omega}^2+\tfrac12(W_{gg}-W_{hh})^2\) (diagonal, traceless) and
conformal invariance of \(|W^+|^2dV\) give \(D_+=24V_{\rm exc}+12\int\delta\,d\hat V-\tfrac32Q_\delta-\tfrac12Q_A\)
with \(\delta=\widehat W_{\omega\omega}+4\). (ii) \(\kappa/6=\hat s^*/6+\tfrac23\nu^2\) and the Chern identity give
\(\int\delta\,d\hat V=N/6\). (iii) \(\int\hat s\,d\hat V=6G+\int su^2W\) (boundary terms vanish: \(uu'W\to0\) at
the bolt, \(u'=0\) on CH) and \(\int\hat s\,d\hat V=-24V_{\rm CH}-N/2\) give the volume formula. (iv) Insert in
\(1-\widehat P=D_+-36V_{\rm exc}-S_{\rm exc}\). ∎

Numerical confirmation (`data/step28/gap_*.json`; \(s\) not exactly \(-24\) in these records):

| \(x_0\) (X) | \(\widehat P-1\) | 12H | 6G | 1.5Qδ | 0.5QA | −1.5N | Σ | residual |
|---|---|---|---|---|---|---|---|---|
| .015 (256) | −.002333 | .00074 | .02215 | .00020 | .00705 | −.03250 | .00003 | 5e−11 |
| .038 (128) | −.004713 | .00333 | .05563 | .00113 | .03286 | −.09766 | −.000005 | 2e−10 |
| .038 (512) | −.004822 | | | | | | | 3e−10 |
| .07 (256) | +.000757 | .00829 | .10094 | .00351 | .08011 | −.19150 | −.00060 | 6e−10 |

Interpretation. All terms are nonnegative except \(-\tfrac32N\). **The entire subthreshold saving is
nonintegrability of the canonical almost-complex structure**, paid for by the conformal factor
(\(H,G\)), the \(J\)-type Weyl variance \(Q_\delta\), and the \(W_3^+\) energy \(Q_A\). A cell whose
canonical structure were integrable would satisfy \(\widehat P\ge1+12H>1\); for perpendicular
cells this is impossible (§3), which is precisely why the perpendicular branch, unlike the aligned
Kähler branch, can go below threshold. The volume formula is the quantitative form of the volume
floor (the strategist's SW argument gives \(V\ge V_{\rm CH}\) without symmetry; here the excess is
identified as \(H+G/2+N/24\)). Positive volume excess does not contradict loss of recoverable CH
background (different quantity).

Exact regrouping: \(\nu\mp(\log u^{-1})_T=-v_g/(ua_g),\ v_h/(ua_h)\), hence
\(6G-\tfrac32N=6\int u^2a_fv_gv_h\,dt\) (checked to 1e−16). Thus
\(\widehat P-1=12H+\tfrac32Q_\delta+\tfrac12Q_A+6\int u^2a_fv_gv_h\,dt+\Sigma\): the sign-indefinite
remainder is the same cubic-type spin interaction (\(v_gv_h\) is part of \(v_1v_2v_3\) in \(b_+\)) that
was identified in Step 7 as the source of the signed compensation.

## 3. Bolt Nijenhuis charge and its transport

Near the bolt \(q=\log(b/t)+\dots\), \(q'+4\sinh q/a_f\simeq1/t\), so \(\nu\simeq-1/(2ut)\sim t^{-3/2}\):
the perpendicular bolt **forces** nonintegrability. With \(\mu=\exp\int2\beta\,dT
=(ua_f)^{-1}\exp\int4\cosh q/a_f\,dt\) (\(\mu\sim t^{3/2}\) at the bolt), the transport law integrates to the
exact charge law (\(\nu\equiv0\) on the exact collar)
\[
K:=\lim_{\rm bolt}\mu\nu=-2\int_{\rm cell}\mu\lambda\,dT\neq0 .
\]
Numerically (μ normalized to \(1/(ua_f)\) at \(X\)): \(K=-0.0072590,-0.0174759,-0.0292342\) for
\(x_0=.015,.038,.07\), law satisfied to \(10^{-12}\). The forced charge must be unwound by \(W_3^+\)
before the CH collar; this is the cost term \(\tfrac12Q_A\).

At leading order at the bolt \((\log u^{-1})_T\simeq\nu\), so the densities of \(6G\) and \(\tfrac32N\)
coincide (both \(\to\tfrac32cb^2\)); the bolt zone itself is neutral. Cumulative profile at
\(x_0=.038\) (`gap_lm3_x00.038_X128_d24.json`): \(6G+\tfrac32(-N)\) stays \(\approx0\) for \(t<0.05\),
the net gain is generated in \(0.1\lesssim t\lesssim0.7\), and the far zone is a net cost.

## 4. Far-field Hardy positivity

From \(\nu_T=2\lambda-2\beta\nu\): \((\nu^2w)_T=4\nu\lambda w+\nu^2w\Lambda\), \(w=A_fA_gA_h\),
\(\Lambda=w_T/w-4\beta\). On \([T_0,\infty)\) with \(\Lambda\ge c>0\) and \(\nu=0\) at the collar,
\[
c\!\int_{T_0}\!\nu^2w+\nu^2w(T_0)\le4\Big(\int\nu^2w\Big)^{1/2}\Big(\int\lambda^2w\Big)^{1/2}
\Rightarrow \int_{T_0}\nu^2w\le\frac{16}{c^2}\int_{T_0}\lambda^2w .
\]
Hence the Nijenhuis sector \(2\int\lambda^2-6\int\nu^2\ge0\) on any **terminal** interval (ending in the exact
collar, \(\nu=0\) there) on which \(\Lambda\ge4\sqrt3\). (Sharp version: sign of the weighted form
\(\int\rho(\tfrac12\psi_T^2-6\psi^2)\), \(\psi=\mu\nu\), \(\rho=w/\mu^2\).)
On CH, \(\Lambda=(8x-3)/\sqrt{x(1+x)}\to8\) (\(x=\sinh^2R\)), and \(\Lambda=4\sqrt3\) at
\(x_H=3+\tfrac34\sqrt{15}\approx5.905\). On actual cells the last crossing is at
\(x_*\approx5.94\)–\(5.99\) (\(t_*\approx1.6\)), the far sector is positive
(.00114/.00588/.01508) and \(\int\nu^2/\int\lambda^2\approx0.18<1/3\) there. For this optimized family all
Nijenhuis gain is generated before the final crossing \(x\approx6\) (a numerical statement about these
cells; \(x\) is the cell coordinate, intrinsic \(\sinh^2R\) only on the collar), where the conformal sector (.0231/.0601/.1127) nearly balances the
near Nijenhuis sector (−.0266/−.0707/−.1265).

## 5. What this changes and what remains

1. The diagonal lower-bound problem is now: minimize
   \(\mathcal F=12H+6G+\tfrac32Q_\delta+2\!\int\!\lambda^2d\hat V-6\!\int\!\nu^2d\hat V\) over diagonal AK metrics
   \(\hat g\) with conical bolt, where \(v=u^{-1}\) solves the Yamabe equation \(6\hat\Delta v+\hat sv+24v^3=0\),
   \(v\to1\) on CH. The only negative term is controlled by the forced charge \(K\), the transport law,
   and Hardy positivity outside \(x_H\). A sharp bound needs a near-zone inequality coupling
   \(\nu\) to \(u\) (bolt cancellation) and to \(\lambda\) (transport) for \(x\lesssim6\).
2. Non-diagonal cells (conditional programme): the canonical object is the closed SD form extending the CH Kähler form
   (unique when it exists, because the collar-relative intersection form is negative definite; existence with a
   prescribed collar germ is an overdetermined problem and is not automatic); \(a(g)=\int_E\omega\) is a geometric modulus (zero in the
   perpendicular diagonal class, positive for aligned Kähler cells, where a boundary flux makes
   \(a\ne0\) possible). Its zero set is generically 1-dimensional (near-symplectic geometry), so
   the general identity requires Taubes-type control of the zero locus and an \(a\)-dependent Chern
   term; the U(2) splitting adds \(2|W_2^+|^2\). This is the natural unified aligned/perpendicular
   formulation. Conjectural general identity (TTCS step28 generator, eqs. (20)–(28)): with \(|\Omega|^2=2\),
   \(a=\int_E\Omega\), \(k=c_1(J)\cdot E\), \(\zeta\) the \(W_2^+\) off-block vector,
   \(\widehat P-1=\frac{9a^2}{\pi^2}+\frac{6ka}{\pi}+12H_s+6G+\tfrac32Q_\delta+\frac1{2\pi^2}\int(2|\zeta|^2+|W_3^+|^2)d\hat V-\tfrac32N
   -\frac{3\mathcal R_Z}{2\pi^2}\), \(\mathcal R_Z\) a zero-circle Chern-circulation term. Consistency check: for an aligned
   Kähler cell (\(k=1\), \(u=1\), \(N=0\)) it reproduces exactly \(P=2(2\pi+6a)^2+L/4\). Pinning becomes
   \(V_{\hat g}-V_{\rm CH}=-a^2/2\).
3. Contact closure (TTCS generator): \(y=\tanh(q/2)\) obeys \(y_T+4y/A_f=-\nu(1-y^2)\); with \(\eta_T=4\eta/A_f\),
   \(\int\eta\nu(1-y^2)dT=\eta(\text{bolt})>0\) (\(y=1\) at bolt, 0 on CH). Since \(\nu<0\) near the bolt, \(\nu\) must change
   sign: a second global moment constraint beside \(K\). Two-constraint capacity bound for \(Q_A\) to be tested.
4. Collapse corollary: since \(-\tfrac32N\) is the only negative term, any sequence of perpendicular diagonal cells
   with \(N\to0\) has \(\liminf\widehat P\ge1\); subthreshold collapsed sequences must retain nonintegrability energy.
5. Collapsed branch: the identity applies to any smooth diagonal competitor; a collapsed
   Taub-bolt-like prefix must be evaluated in these terms (H, G, N, \(Q_A\), \(Q_\delta\)), not only by charges.

## 6. Verification record and caveats

* Independent TTCS verification (`trace/ttcs/results/step28_ttcs01_verifier1_integration.md`) confirmed Theorem A
  and all coefficients, and supplied the corrections incorporated above: the \(\Omega\) vs \(2\Omega\) normalization;
  \(A_hv_g=-A_gv_h\) (not \(A_gv_g=-A_hv_h\)); \(\hat s+2\nu^2\) is the Hermitian/Chern scalar; the \(H_s\) square
  completion; Hardy positivity only on terminal intervals; non-diagonal statements conditional. It also notes that
  Theorem A is an exact repackaging of the inherited relative identity; the new content is the AK structure
  (pinning, Chern–Stokes flux, transport, forced charge, bolt cancellation, tail positivity).
* In `step28_ak_gap_identity.py` the JSON fields `law_residual` (hard-coded 0) and `transport_rel_residual_max`
  (gradient taken against a surrogate coordinate) are not evidence; the meaningful numerical check of the transport
  is `law_residual_from_i30` (\(\sim10^{-12}\)); the transport law itself is symbolic (`ak_nu_structure.json`).
* Peer S1003A02 Step 34: \(b_+\) is already an exact HJ calibration (\(\sup(\dot b_+-L)=0\) identically); decorations
  \(\phi(q,\eta)\) give zero gain. The missing cost must come from the Nijenhuis/conformal/transport near-zone
  structure identified here.



---

## Source step29_boundary_corrected_AK_exterior_and_contact_capacity.md

Original: [sources/Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md](../sources/Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md)

# Step 29 — Boundary-corrected AK exterior response and nonlinear contact constraints

## 1. Scope and purpose

The object remains the unrestricted Einstein-gap problem, with the certified perpendicular cell providing an actual closed-family upper construction rather than a substitute for the all-metric problem. This note resolves a mathematical dependency between two representations of the same diagonal exterior response:

* the raw antisymmetric complex-hyperbolic (CH) Ricci action from Step 19;
* the local almost-Kähler (AK) action from Step 28.

It also tests the nonlinear contact-closure constraint on actual low-cost profiles. The capacity numbers below are frozen-profile computations and are not asserted uniformly over all diagonal cells, still less over all metrics.

Normalization: \(\operatorname{Ric}_{CH}=-6g\), \(\widehat P=P/(8\pi^2)\), and \(Wdt\) is the normalized volume density.

## 2. Full local identity with interface flux

Let
\[
\mathcal F=4\mathcal P\cosh q-\mathcal P\mathcal P_{TT}-\frac12\mathcal P_T^2
\]
be the Chern–Stokes bracket of Step 28, and let \(L_{AK}\) denote the complete all-scalar Theorem-A density
\[
L_{AK}=12W\left(u^2+\frac{s}{24}\right)^2+6Wu'^2
 +\frac32\delta^2\,d\widehat V/dt+2\lambda^2\,d\widehat V/dt
 -6\nu^2\,d\widehat V/dt.
\]
The local relation is
\[
\boxed{\widehat P[t_0,t_1]=\int_{t_0}^{t_1}L_{AK}\,dt+B(t_1)-B(t_0)},
\]
\[
\boxed{B=b_+-3\mathcal F-9\mathcal P^2-6Wuu'},
\]
where the prime on \(u\) is the original arclength derivative. The smooth perpendicular bolt has \(B\to1\); exact CH has \(B=2\). Hence the whole-cell formula gives \(\widehat P=1+\int L_{AK}\), but on a terminal interval ending in CH,
\[
\boxed{\int_{\rm tail}L_{AK}=\widehat P_{\rm tail}+B(\text{entry})-2.}
\]
The AK tail integral is therefore not the raw tail Ricci action.

`scripts/step29_local_AK_flux.py` evaluates every term directly on the \(x_0=.038,X=128\) optimized cell. At the exact collar it finds \(B=2-5.8\times10^{-11}\). For entries \(x=.1,.2,.5,1,2,5,10,20,50\), the local identity residual is \(5.4\times10^{-11}\)–\(6.3\times10^{-11}\). Representative tail data are:

| entry \(x\) | raw \(\widehat P_{tail}\) | \(\int L_{AK}\) | \(B(entry)-2\) |
|---:|---:|---:|---:|
| 0.5 | 0.01636263 | 0.01195842 | -0.00440421 |
| 2 | 0.00230694 | 0.00365499 | +0.00134805 |
| 5 | 0.00050020 | 0.00599201 | +0.00549181 |
| 10 | 0.00015309 | 0.00450865 | +0.00435556 |
| 20 | 0.00007147 | 0.00222222 | +0.00215075 |

At \(x=10\), more than 96% of the positive AK tail number is the interface conversion: the raw action is \(1.53\times10^{-4}\), whereas \(B(entry)-2=4.36\times10^{-3}\). Adding the AK tail number to the Step-19 exterior response would therefore duplicate the same quantity at incompatible splittings.

Artifact: `data/step29/local_AK_flux_x0038_X128.json`.

## 3. Exact linear CH bridge

Use the exact Step-19 antisymmetric variables
\[
q=\theta,\qquad v_-=f_-w,\qquad
f_-=\frac{x}{(1+x)^{5/2}},\qquad
(k\theta)'=\frac12f_-^2w,
\quad k=\left(\frac{x}{1+x}\right)^2.
\]
On CH the AK variables are
\[
\boxed{\nu=-\frac{v_-}{2\sqrt x}=-\frac{\sqrt x}{2(1+x)^{5/2}}w},
\]
\[
\boxed{\lambda=-\frac{x(1+x)w'+(2-3x)w}{2(1+x)^3}}.
\]
Direct symbolic expansion (`scripts/step29_ak_exterior_bridge.py`) gives the exact identity
\[
\boxed{
\frac{x}{2}(2\lambda^2-6\nu^2)
=\mu(w')^2+\frac{d}{dx}\bigl(A(x)w^2\bigr),
}
\]
where
\[
\mu=\frac{x^3}{4(1+x)^4},\qquad
\boxed{A(x)=-\frac{x^2(3x-2)}{4(1+x)^5}}.
\]
The symbolic residual is zero. This is the linearized form of the full \(B\)-conversion.

The Step-19 exterior functional is exactly
\[
E_{ext}=\int_\rho^\infty\mu(w')^2dx=\frac{\delta^2}{I(\rho)},
\qquad
\delta=-2k(\rho)\Theta-w_0G(\rho),
\]
with its existing mass null line \(\delta=0\). Thus the AK expression induces no second positive tail response:
\[
\int_\rho^\infty L_{AK}^{(2)}dx=E_{ext}-A(\rho)w_0^2.
\]
For the exact outgoing Einstein mass mode \(w\equiv1\), raw action is zero but at \(\rho=10\)
\[
\int_{10}^\infty L_{AK}^{(2)}dx=-A(10)=0.004346449261414086,
\]
which is canceled exactly by the entrance flux \(A(10)=-0.004346449261414086\). This supplies the required Einstein benchmark and preserves the same mass null direction.

On the nonlinear \(x_0=.038,X=128\) profile beyond \(\rho=10\), reconstructing \(w\) and evaluating the **CH quadratic bridge** gives:

* reconstructed CH-quadratic raw tail: \(1.47497210\times10^{-4}\);
* reconstructed CH-quadratic AK tail: \(4.56894793\times10^{-3}\);
* interface change: \(4.42145057\times10^{-3}\);
* bridge residual: \(1.49\times10^{-10}\).

These are not the exact nonlinear values in §2; the differences are finite nonlinear/off-CH corrections (the exact nonlinear raw tail at \(x=10\) is \(1.53090270\times10^{-4}\), and the exact nonlinear AK tail is \(4.50865207\times10^{-3}\)). For the same entrance trace, the exact finite-\(X\) Step-19 quadratic minimizer has raw cost \(1.435700999\times10^{-4}\), giving boundary-converted quadratic AK value \(4.565020671\times10^{-3}\), within \(3.93\times10^{-6}\) of the reconstructed profile's quadratic AK value. The mismatch measures that the optimized finite tail is close to, but not exactly, the frozen-trace linear minimizer; it is not a missing positive action.

Artifact: `data/step29/ak_exterior_bridge_x0038_X128_rho10.json`.

## 4. Contact closure is the old torsion/reconstruction relation

Set \(y=\tanh(q/2)\). The definition of \(\nu\) gives
\[
\boxed{y_T+\frac4{A_f}y=-\nu(1-y^2)}.
\]
With \(\eta_T=4\eta/A_f\),
\[
(\eta y)_T=-\eta\nu(1-y^2).
\]
On the linear CH tail, \(y=q/2+O(q^3)\), \(\eta\) is proportional to the existing contact integrating factor \(k=(x/(1+x))^2\), and \(\nu=-v_-/(2\sqrt x)\). Therefore this relation is the Step-19 torsion equation \((k\theta)'=f_-v_-/2\) in AK variables, not a new independent terminal condition.

`scripts/step29_capacity_contact.py` verifies the nonlinear contact equation on the actual \(x_0=.015,.038,.07\) profiles, with maximum bulk residual \(0.6\times10^{-6}\)–\(1.3\times10^{-6}\), and confirms a sign change of \(\nu\) in all three. The weights, integrating factors, and moments all come from the same metric.

## 5. Frozen-profile transport capacity does not close the lower problem

Put \(h=\mu\nu\), \(\rho=\widehat W/\mu^2\). Then
\[
\frac12Q_A=\frac12\int\rho h_T^2dT.
\]
For each actual profile, I computed:

1. the minimum with the actual endpoint values of \(h\);
2. the minimum after additionally imposing the actual linear contact moment \(\int c(T)h(T)dT\), with \(c=\eta(1-y^2)/\mu\), while freezing \(\rho,c\) from that metric.

| \(x_0\) | observed \(Q_A/2\) | endpoint capacity | endpoint + contact capacity | fractions |
|---:|---:|---:|---:|---:|
| .015 | .0070468 | .0010298 | .0018579 | .146, .264 |
| .038 | .0328566 | .0058549 | .0106619 | .178, .324 |
| .07 | .0801134 | .0167547 | .0311244 | .209, .389 |

The nonlinear contact identity is real and it materially raises the frozen capacity, but even the two-constraint number explains only 26–39% of the observed \(W_3\) transport energy. It is therefore not near saturation and cannot by itself reduce the lower problem to two scalar moments. More importantly, these coefficients are generated by the same metric and have no presently derived uniform comparison over the full diagonal class. The next lower-bound step must retain nonlinear evolution of \((A_f,\mathcal P,q,u)\), or an equivalent full Ricci-control/Hamilton–Jacobi system, with the existing boundary-converted exterior value attached.

Artifacts: `data/step29/capacity_x0015_X256.json`, `capacity_x0038_X128.json`, `capacity_x007_X256.json`.

## 6. Consequences for the construction and global programme

1. **No second tail theory is needed in the antisymmetric sector.** The Step-19 exterior response \(\delta^2/I\), including its Einstein mass null direction, is the correct raw terminal value. The AK tail expression is the same response plus the explicit interface conversion. A matrix Riccati construction that assigns a new positive price to the mass mode would be wrong.
2. **The saving mechanism is genuinely intermediate and nonlinear.** In the far linear CH sector, the AK and raw formulations differ only by flux. The negative net contribution must be produced before this linear response, where bolt-forced nonintegrability, conformal response, contact closure, and terminal trace evolve on one metric.
3. **The interface \(B\) is a useful matching observable.** Unlike the enormous individual CH values of \(b_+\), \(\mathcal F\), and \(9\mathcal P^2\), their combination is exactly 2. It converts local AK decompositions into raw action without cancellation ambiguity at the mathematical level. Numerically the local identity is stable to \(10^{-10}\) on the tested profile.
4. **Applicability beyond one profile.** The full nonlinear \(B\)-identity holds for every smooth diagonal perpendicular exact-CH cell, whereas the explicit \(A(x)w^2\) bridge is its linear CH specialization. The latter can be used at any section where a competitor is quantitatively close to CH. Uniform entry into such a section remains part of the global lower problem.
5. **Construction transfer.** The strict cell saving is already reproducible on suitable CH cover towers through exact collar insertion; the certified theorem-level source remains `data/perp_area/rigorous_x00.03_X128_d20.json`, not the floating \(x_0=.038\) record. The interface analysis explains its exterior compatibility but does not change the certified coefficient \(<3.9961521+\varepsilon\).
6. **Beyond fixed symmetric profiles.** The immediate transferable object is not a numerical capacity weight but the geometric package: a closed self-dual form, its Nijenhuis transport, the conformal selector, and the Chern/interface flux. Extending that package to nonsymmetric cells requires actual existence of the relative self-dual form and treatment of its zero set. The global all-metric O11 lower value, mixed blow-up–handle cells, O10, and fixed-manifold Einstein attainment remain open.

## 7. Independent verification corrections

A two-branch TTCS verification (`trace/ttcs/results/step29_ttcs01_verifier1_integration.md`) re-derived the nonlinear local identity, the linear CH bridge, the mass-null cancellation, and the capacity Euler problem. It found and repaired two presentation issues:

* the correct displayed formula is \(\lambda=-[x(1+x)w'+(2-3x)w]/[2(1+x)^3]\); the original draft had an extra factor of \(x\) in front of \(w'\), while the SymPy script and computed identity already used the correct coefficient;
* the bridge script's profile block evaluates the CH quadratic reconstruction from a nonlinear tail, whereas the exact nonlinear raw and AK tail values are those of `step29_local_AK_flux.py`.

With those corrections, the verifier confirmed that the interface accounts for 96.6% of the exact positive AK tail integral at \(x=10\), that the finite-\(X\) and infinite mass-null responses retain the Step-19 sign conventions, and that the two-constraint capacity formula has the correct Green representer and factor \(1/2\). The corrected note and script labels now distinguish exact nonlinear values from CH-quadratic reconstructions.

## 8. The theorem-level cell obeys the same interface mechanism

The nonlinear local calculation was also run on the actual frozen profile underlying the authoritative Arb enclosure, `data/perp_area/x00.03_X128_d20.json` (whose separate rigorous record gives \(J_6/(8\pi^2)\le0.9956710815089548\)). The interface identity again holds at all nine sections with residuals \(5.0\times10^{-11}\)–\(5.8\times10^{-11}\). At \(x=10\), the exact nonlinear tail values are
\[
\widehat P_{tail}=1.14618031\times10^{-4},\qquad
\int L_{AK}=2.87473373\times10^{-3},\qquad
B(entry)-2=2.76011570\times10^{-3}.
\]
Thus the same geometric conversion is present in the theorem-level realizable construction, not only in the improved floating branch. The new local calculations are ordinary floating checks; the certified global energy remains supplied by `data/perp_area/rigorous_x00.03_X128_d20.json`. Artifacts: `data/step29/local_AK_flux_certified_x003_X128.json` and `ak_exterior_bridge_certified_x003_X128_rho10.json`.

A cutoff-sensitivity check on the \(x_0=.038\) capacity used inner computational parameters \(u_{min}=10^{-4},10^{-5},3\times10^{-6}\). The endpoint-only fractions were \(0.178240,0.178196,0.178193\), and the endpoint-plus-contact fractions were \(0.324581,0.324498,0.324491\). Thus the conclusion that the two frozen constraints account for about 32.45% is stable against the singular-bolt cutoff at the displayed accuracy. Artifacts: `capacity_x0038_X128_eps1e4.json`, `capacity_x0038_X128.json`, `capacity_x0038_X128_eps3e6.json`.



---

## Source step31_ramified_KE_transfer_and_interface_simplification.md

Original: [sources/Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md](../sources/Sessions/S1003A01/workspace/notes/step31_ramified_KE_transfer_and_interface_simplification.md)

# Step 31 — Transfer to ramified compact Kähler–Einstein surfaces and the simplified interface

## 1. A new closed family carrying the certified saving

Use the normalization \(\operatorname{Ric}=-g\). Let
\[
X^\circ=\Gamma\backslash\mathbb B^2,\qquad (\bar X,D)
\]
be a smooth toroidal compactification of a neat arithmetic nonuniform ball quotient, and put
\[
L=K_{\bar X}+D.
\]
First pass to a sufficiently deep **principal congruence** subgroup of \(\Gamma\): because the intersection of principal congruence subgroups is trivial, one can exclude the finite set of nonidentity elements moving a chosen lift by at most twice the required marked radius. This produces an embedded marked complex-hyperbolic ball and keeps the later high-ramification covers inside the preliminary cover. For the certified \(x_0=.03,X=128\) cell, the outer radius in the \(\operatorname{Ric}=-g\) normalization is
\[
R_{128}=\sqrt6\,\operatorname{arsinh}\sqrt{128}
       =7.64512629467772\ldots,
\]
not \(4.32\) (the latter belongs to the older \(X=8\) witness). Fix a ball of radius \(R_{128}\) plus a fixed annular buffer. A cofinal sequence of further congruence covers with cusp ramification orders \(v_{m,\lambda}\to\infty\) suffices; literal nesting is not used.

Biquard--Guenancia prove local smooth convergence of the conical Kähler--Einstein metrics to the complex-hyperbolic metric on every fixed compact subset of \(X^\circ\), and §4.3 shows that for
\[
\beta_{m,\lambda}=v_{m,\lambda}^{-1}
\]
the pullback to the ramified compactification \(\bar X_m\) is a smooth metric \(g_m\) with \(\operatorname{Ric}_{g_m}=-g_m\) \cite{biquard2022degenerating}. If \(d_m\) is the covering degree, the fixed marked ball has \(d_m\) disjoint lifts, and all lifted metrics have the same \(C^2\) discrepancy
\[
\varepsilon_m=\|g_m-g_{CH}\|_{C^2(K)}\longrightarrow0
\]
on the fixed compact marked region \(K\). Thus no thick-part volume estimate is needed.

### Topology of the compactifications

Hurwitz gives
\[
K_{\bar X_m}=\pi_m^*\left(L-\sum_\lambda\beta_{m,\lambda}D_\lambda\right).
\]
The boundary elliptic curves are disjoint and adjunction gives \(L\cdot D_\lambda=0\). Hence, with
\[
A_m=K_{\bar X_m}^2,
\]
we have
\[
\frac{A_m}{d_m}=L^2+\sum_\lambda\beta_{m,\lambda}^2D_\lambda^2\longrightarrow L^2>0.
\]
Because the boundary elliptic curves have Euler characteristic zero and log proportionality gives \(L^2=3\chi(X^\circ)\),
\[
\chi(\bar X_m)=d_m\chi(X^\circ)=\frac{d_mL^2}{3}.
\]
Therefore
\[
\Delta_m:=3\chi(\bar X_m)-A_m
=-d_m\sum_\lambda\beta_{m,\lambda}^2D_\lambda^2>0,
\qquad \frac{\Delta_m}{A_m}\to0.
\]
In particular \(d_m\asymp A_m\), so the lifted marked balls occur with positive density relative to \(A_m\). The strict inequality \(A_m<3\chi(\bar X_m)\) also shows that these compact surfaces are not compact ball quotients.

The smooth negative Kähler--Einstein metric satisfies \([\omega_m]=2\pi c_1(K_{\bar X_m})\), so the canonical class is Kähler and hence ample by Kodaira. Thus \(\bar X_m\) is a smooth minimal surface of general type. Its canonical Seiberg--Witten structure is nonzero in the canonical chamber. LeBrun's polarized blow-up construction, including the \(b^+=1\) chamber selection when it occurs and the degree-one holonomy insertions for the \(S^1\times S^3\) summands, then gives for every metric a polarization-adapted actual class after choosing the exceptional signs \cite{lebrun2001ricci}. This is the precise field supply used below, not merely the existence of a cohomology class.

### Surgery parameters and the lower order

Choose \(Q_m\to\infty\) with \(Q_m=o(A_m)\), and suppose more generally that
\[
\frac{\Delta_m}{Q_m}\longrightarrow r,\qquad 0\le r<1.
\]
(The old coefficient is the case \(r=0\); it requires only \(\Delta_m=o(Q_m)\), not \(1\ll\Delta_m\).) Put
\[
M_m=\bar X_m\#k_m\overline{\mathbb{CP}}^{\,2}
\#\ell_m(S^1\times S^3),
\quad Q_m=k_m+4\ell_m,
\quad h_m=Q_m/A_m.
\]
Writing \(\Delta=3\chi-A\), direct characteristic-number calculation gives
\[
T_+=A-k-4\ell,
\qquad
T_-=\frac A3+\frac{4\Delta}{3}+5k-4\ell.
\]
Choose \((k_m,\ell_m)\) by rounding the real solution
\[
k_m=\frac{2(Q_m-\Delta_m)}9,
\qquad
\ell_m=\frac{7Q_m}{36}+\frac{\Delta_m}{18},
\]
so that \(16\ell_m-14k_m=4\Delta_m+O(1)\). Then
\[
\frac{k_m}{Q_m}\to\frac{2(1-r)}9,
\qquad
\frac{\ell_m}{Q_m}\to\frac{7+2r}{36}.
\]
Moreover
\[
T_{-,m}=\frac{A_m+Q_m}{3}+O(1),
\qquad
U_{\mathrm{top},m}=\frac{3\min(T_{+,m},T_{-,m})}{A_m}
=1+h_m+O(A_m^{-1})=1+h_m+o(h_m).
\]
The last equality uses \(Q_m\to\infty\). The canonical field has \(p\ge A_m\) and selected square \(a^2=A_m-k_m\ge T_{+,m}=A_m-Q_m\). The inherited linear-window theorem therefore yields
\[
\inf_g\mathcal E(g)\ge c h_m
\]
for all large \(m\) (and likewise for \(\mathcal J\)); its actual equations separately exclude Ricci-flat metrics.

For \(r=0\), one may always take
\(Q_m\asymp\sqrt{A_m\max\{\Delta_m,1\}}\), rounded to integers. For prescribed \(0<r<1\), the same conclusion applies to any chosen ramified tower with \(\Delta_m\to\infty\), by taking \(Q_m\sim\Delta_m/r\). Such towers are not hypothetical: for principal congruence Picard modular surfaces, the index has degree-eight level growth while the toroidal boundary self-intersection has the index divided by the square of the cusp-width parameter, so \(\Delta_m\to\infty\) and \(\Delta_m/A_m\to0\) \cite{dambi2014invariants}. If \(\Delta_m\) stays bounded, only \(r=0\) is compatible with \(Q_m\to\infty\). The symbolic algebra is reproduced in `workspace/scripts/step31_topology_window.py` and `workspace/scripts/step32_ramified_transfer_law.py`.

### Upper construction

The exact-CH-collar cell can be inserted into any selected lifted marked ball. Use the fixed buffer to append an exact CH annulus to the cell and choose a fixed cutoff \(\chi\). In the marked tensor coordinates set
\[
g_{m,\mathrm{ann}}=g_{CH}+\chi\,(g_m-g_{CH}).
\]
On the inner subannulus this is the cell's exact CH continuation; on the outer subannulus it is \(g_m\). Uniform ellipticity and the fixed cutoff show that \(g_{m,\mathrm{ann}}\) is positive for large \(m\), differs from CH by \(O(\varepsilon_m)\) in \(C^2\), and has
\[
\operatorname{Ric}(g_{m,\mathrm{ann}})+g_{m,\mathrm{ann}}=O(\varepsilon_m).
\]
Hence its raw annular defect is \(O(\varepsilon_m^2)\), while its volume and total-scalar increments relative to the marked CH annulus are \(O(\varepsilon_m)\) per site. Across \(k_m=O(Q_m)\) sites, these errors are respectively \(o(Q_m)\) and \(o(Q_m)\). The untouched background is exactly Einstein, so there is no error proportional to its full volume.

Treat the handles by the inherited shrinking construction, choosing their scale on the \(m\)-th manifold so their aggregate volume, scalar-moment, and defect errors are \(o(Q_m)\). Let the certified cell's exact-collar smoothing width tend to zero along the sequence. If
\[
\frac{J_1}{8\pi^2}\le1-\eta,
\]
then the complete-cell expansion gives
\[
\frac{\alpha(M_m)}{h_m}
\le 4(1-\eta)\frac{k_m}{Q_m}
   +16\frac{\ell_m}{Q_m}+o(1),
\]
and therefore
\[
\boxed{\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}(1-r).}
\]
Using the rigorous \(x_0=.03,X=128\) enclosure
\[
\frac{J_1}{8\pi^2}\le0.9956710815089548,
\qquad \eta=0.004328918491045219,
\]
from `workspace/data/perp_area/rigorous_x00.03_X128_d20.json`, the \(r=0\) specialization is
\[
\boxed{\limsup_m\frac{\alpha(M_m)}{h_m}
\le4-\frac{8\eta}{9}<3.996152073.}
\]
For every fixed \(0<r<1\) the saving remains strict, but is reduced by the exceptional-site fraction \(1-r\). This is a construction law for the chosen topology and separated handle geometry, not an optimality result and not a transition theorem at \(r=1\). A fixed smoothing width or fixed nonsymmetric perturbation gives the same formulas with a smaller uniform margin \(\eta'<\eta\); the displayed certified endpoint uses a diagonal sequence of smoothing widths tending to zero.

## 2. Why the saving transfers

The ingredients used by the upper construction are local and geometric:

1. a fixed marked region close in \(C^2\) to CH at the cell's physical scale;
2. a negative Einstein background, so the exterior contributes zero raw defect;
3. the perpendicular compatible field inside the cell, where self-dual Weyl depletion, scalar response, contact closure and Nijenhuis transport coexist on one metric;
4. an exact CH collar on the cell, which makes the splice error quadratic in the background discrepancy for the raw Ricci defect;
5. enough disjoint marked regions relative to the surgery count.

Global local symmetry of the closed background is not used. The ramified family supplies these ingredients while changing its Chern slope away from equality.

## 3. Nonsymmetric openness

Fix a smooth exact-collar subthreshold cell \(g_c\), with a compact set \(K\) disjoint from the bolt and the exact collar. For every smooth symmetric tensor \(h\) supported in \(K\), positivity and continuity of the Ricci map as a function of the metric two-jet imply
\[
\|h\|_{C^2}<\epsilon
\quad\Longrightarrow\quad
J_6(g_c+h)<8\pi^2
\]
for sufficiently small \(\epsilon\). The bolt, marking, topology and exact collar are unchanged. Choosing non-\(SU(2)\)-invariant \(h\) gives an open family of genuinely nonsymmetric subthreshold cells. Replication of any fixed compact family with a uniform reduced margin produces a strict sub-four coefficient; preserving the sharper certified coefficient instead uses perturbations and smoothing losses tending to zero.

## 4. Simplified \(B-b_+\) relation

The Step-30 formula simplifies exactly because its bracket is
\[
u_f=a_f'-\gamma_f.
\]
Hence
\[
\boxed{B-b_+=6\phi u_f-9\phi^2,}
\]
and, if \(b_+=2-\mathcal C(u)\),
\[
\boxed{B=2-[\mathcal C(u)-u_f^2]-(u_f-3\phi)^2.}
\]
The separately large ratios in the first expansion cancel. The revised `workspace/scripts/step29_local_AK_flux.py` evaluates this formula on the improved and certified-profile cells. In `workspace/data/step31/Bsimple_x0038_X128.json` and `Bsimple_certifiedprofile_x003_X128.json`, the residual between the direct and simplified formulas ranges from about \(10^{-16}\) in the core to \(4\times10^{-12}\) near the far collar.

This also corrects the Step-30 collapse interpretation. The moment \(\phi\) has a multiplicative normalization fixed by the outer marking:
\[
\phi(s)=\phi(T_c)\exp\left(-\int_s^{T_c}\frac{2a_f}{a_ga_h}\,dt\right).
\]
It cannot be normalized from a collapsed entry alone. If a complete marked collapsed trajectory has bounded \(u_f\) and collar-normalized \(\phi(s)\to0\), then \(B(s)-b_+(s)\to0\); no estimate of \(\phi\cosh q\) is needed. The A02 scale-free calibrated leaves omit the absolute radial scale and this outer normalization, so their existing records do not yet decide whether \(B(s)\) remains controlled. The next collapse calculation must reconstruct a complete marked trajectory or evolve \(\phi\) from the actual outer collar.


---

## Source step33_surgery_slope_law_and_ASD_retention.md

Original: [sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md](../sources/Sessions/S1003A01/workspace/notes/step33_surgery_slope_law_and_ASD_retention.md)

# Step 33 — The two-parameter surgery law over ramified Kähler–Einstein towers, the sharpened certified cell, and anti-self-dual retention

Conventions as in the corpus (`paper/sections/linear_coercivity.tex`, `variational_geometry.tex`):
\(\mathcal E(g)=\inf_{\lambda\ne0}\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)\), \(\alpha(M)=\inf_{\mathscr G(M)}\mathcal E\),
\(R=\int|\mathrm{Ric}|^2\), \(P=\int|\mathrm{Ric}^\circ|^2\), \(S=\int s^2\), \(B=\int|W^-|^2\), \(L_s=\int(s-\bar s)^2\).
Scripts/data: `scripts/step33_fraction_window.py` → `data/step33/fraction_window.json`;
`scripts/perp_rigorous_enclosure.py` (Step-33 exact-endpoint output) → `data/step33/rigorous_x00.03_X128_d20_{J,P,S}_exact.json`.

## 0. Families

Fix the post-preliminary arithmetic base and Galois ramified tower of Steps 31–32
(`notes/step31_ramified_KE_transfer_and_interface_simplification.md`): smooth compact
Kähler–Einstein surfaces \(\bar X_m\), \(\mathrm{Ric}=-g\), \(A_m=c_1^2\), Chern defect
\(\Delta_m=3\chi(\bar X_m)-A_m>0\), \(d_m\asymp A_m\) disjoint lifts of one fixed marked ball of
radius \(\sqrt6\,\mathrm{arsinh}\sqrt{128}=7.6451262946\ldots\) plus buffer, uniformly \(C^2\)
\(\varepsilon_m\)-close to CH. Put
\[
M_m=\bar X_m\#k_m\overline{\mathbf{CP}}^2\#\ell_m(S^1\times S^3),\quad
Q_m=k_m+4\ell_m,\quad h_m=\frac{Q_m}{A_m},\quad
\theta_m=\frac{k_m}{Q_m},\quad r_m=\frac{\Delta_m}{Q_m},
\]
and the **topological chiral slope**
\[
\boxed{\sigma_m=4r_m+18\theta_m=\frac{4\Delta_m+18k_m}{Q_m}.}
\]
No balancing is imposed. Any integers are allowed; all statements below are written in
the exact values \(\theta_m,r_m,\sigma_m\), so rounding never enters. (To realize prescribed limits
\(\theta,r\) choose \(\widehat Q_m\), \(k_m=\lceil\theta\widehat Q_m\rceil\),
\(\ell_m=\lfloor(1-\theta)\widehat Q_m/4\rfloor\).)

Exact characteristic numbers (SymPy, `fraction_window.json`):
\(T_+=2\chi+3\tau=A-Q=A(1-h)\) exactly, and
\[
\frac{3T_-}{A}=\frac{3(2\chi-3\tau)}{A}=1+(\sigma-3)h .
\]
Hence \(U_{\rm top}=\min\{3-3h,\,1+(\sigma-3)h\}=1+(\sigma-3)h\) exactly when \(\sigma h\le2\), in
particular for all large \(m\) when \(Q_m=o(A_m)\) and \(\sigma_m\) stays bounded.

## 1. All-metric lower theory depends only on the slope \(\sigma\)

Actual-field input (LeBrun polarized connected sums, verified in Step 32): for every metric,
\(p\ge A\), selected determinant class \(a=c-\sum\pm E_i\) with \(a^2=A-k\ge A-Q=T_+\); the
handle summands are absorbed by holonomy insertions; \(0<h\le1/3\). Two independent inequalities
then hold **for every smooth metric** on \(M_m\):

**(L1) Linear window** (thm:linear-window, with \(\mathcal E\ge\mathcal J\)). With \(L_h=1+(1+c_0)h\),
\[
\mathcal E(g)\ \ge\ \frac{(L_h-U_{\rm top})_+}{L_h+U_{\rm top}/18}
=\frac{(4+c_0-\sigma)_+\,h}{L_h+U_{\rm top}/18}.
\]

**(L2) \(\Delta\)-corrected scalar–Weyl identity.** The signature formula with the background
\(\tau(\bar X)=(A-2\Delta)/9\) gives \(\int|W^+|^2=B+12\pi^2\tau(M)\) and
\(P=4\int|W^+|^2+S/12-8\pi^2T_+\). Writing \(\theta_0=(4\ell-5k)/A=h(1-6\theta)\),
\(S_0=32\pi^2A\) and
\[
B_\Delta:=\tfrac{8\pi^2}{3}\Delta ,
\]
one has the exact identity (verified symbolically)
\[
P=\frac{S-S_0}{12}+4(B-B_\Delta)+8\pi^2A\,\theta_0 .
\tag{1.1}
\]
Equivalently, with \(\theta_\Delta=\theta_0-\tfrac{4\Delta}{3A}=h\,\frac{3-\sigma}{3}\),
\(P=(S-S_0)/12+4B+8\pi^2A\theta_\Delta\), and the corpus proof of
prop:vg-handle-identity applies verbatim:
\[
\mathcal E-\frac{4\theta_\Delta}{1+\theta_\Delta}
=\frac{(1-3\theta_\Delta)(S-S_0)/3+16B+(1+\theta_\Delta)L_s}{(1+\theta_\Delta)R}\ \ge 0
\qquad(0\le\theta_\Delta\le\tfrac13),
\]
using only the monopole scalar budget \(S\ge32\pi^2p\ge S_0\).

**Theorem A (slope law for the lower order).** On \(M_m\), for all large \(m\),
\[
\frac{\alpha(M_m)}{h_m}\ \ge\ \max\Bigl\{\tfrac43(3-\sigma_m)_+\,\frac{1}{1+\theta_\Delta},\;
\frac{(4+c_0-\sigma_m)_+}{L_h+U_{\rm top}/18}\Bigr\},
\qquad
\liminf\frac{\alpha}{h}\ge \max\Bigl\{\tfrac43(3-\sigma)_+,\ \tfrac{18}{19}(4+c_0-\sigma)_+\Bigr\}.
\]
The first branch is completely explicit; the second has the nonexplicit universal \(c_0>0\).
Consistency with the exact pure-handle theorem (\(\sigma=0\), value \(4\)) forces \(c_0\le 2/9\).
Both lower mechanisms see the surgery and the background **only through \(\sigma\)**.

## 2. Upper law depends only on the blow-up fraction \(\theta\)

**Theorem B.** Insert \(k_m\) copies of the certified exact-collar cell into distinct lifted marked
balls and \(\ell_m\) shrinking standard handles in separated regions. With
\(D=\int|\mathrm{Ric}+g|^2\), \(T=\int s+4V\),
\(\mathcal E=(4D-T^2/V)/(4V+D-2T)\), \(V=2\pi^2A+O(Q)\), \(T=O(Q)\),
\(D=kJ_1+32\pi^2\ell+O(Q\varepsilon_m^2)+o(Q)\), hence
\[
\limsup\frac{\alpha(M_m)}{h_m}\le 4(1-\eta\theta),\qquad
\eta\ \ge\ \eta_{\rm cert}=0.004329969644869361\ldots\ (\text{§4}).
\]
The background Chern defect does not enter: the KE background contributes \(D=0\) exactly and its
\(W^-\) energy \(B_\Delta\) costs nothing in \(D\).

## 3. Consequences

* **Coexistence region.** Every realizable limit pair with \(0<\theta\le1\) and \(\sigma<4+c_0\) has
  a positive all-metric linear gap and a strictly sub-four construction. The explicit
  (\(c_0\)-free) subregion is \(\sigma<3\), where
  \[
  \tfrac43(3-\sigma)\ \le\ \liminf\alpha/h\ \le\ \limsup\alpha/h\ \le\ 4-4\eta\theta .
  \]
  Examples: \(r=0,\theta=1/9\): \([4/3,\;4-0.0019244]\); \(r=1/2,\theta=1/36\): \([2/3,\;4-0.00048]\).
* **Beyond \(r=1\).** For \(1\le r<1+c_0/4\), every \(0<\theta<(4+c_0-4r)/18\) is admissible;
  the vanishing of the *balanced* saving \(8\eta(1-r)/9\) at \(r=1\) is an artifact of the
  balanced slice \(\sigma=4\), not an existence barrier.
* **Realizability of every \(r\).** In the inert-prime-power Picard tower (Džambić,
  \cite{dambi2014invariants}), \(A_n\asymp p^{8n}\), \(\Delta_n=-T_n^2\asymp p^{6n}\). For \(r\in(0,\infty)\) take
  \(Q_n\sim\Delta_n/r\): then \(Q_n/A_n\asymp p^{-2n}\to0\). For \(r=0\) take
  \(Q_n=\lceil p^{n}\Delta_n\rceil\), still \(o(A_n)\). So the whole half-line of \(r\) is
  geometrically supplied with linearly many CH-close sites.
* **Where the lower theory stops.** For \(\sigma\ge4+c_0\) (in particular every \(\theta\) once
  \(r\ge1+c_0/4\)), neither L1 nor L2 gives anything, and Einstein metrics on \(M_m\) are not
  excluded by these actual-field Chern–Weil arguments (an Einstein metric needs \(L_h\le U_{\rm top}\),
  i.e. \(\sigma\ge4+c_0\)). The extreme \(Q=o(\Delta)\) contains the unsurgered background, where
  \(\alpha=0\) is attained by the KE metric; the topological window must therefore close somewhere,
  but the present upper constructions remain at \(4h(1-\eta\theta)\) uniformly in \(r\).

## 4. Anti-self-dual retention: the exact meaning of the \(r\)-loss

Identity (1.1) shows exactly what the \(r\)-dependence of the lower theory measures. For the KE
background, \(|W^+|^2=s^2/24\) and the signature formula give
\(\int_{\bar X}|W^-|^2=B_\Delta=8\pi^2\Delta/3\) exactly (checked in the script). Rewriting with the
\(\Delta\)-free parameter \(\theta_0=h(1-6\theta)\):
\[
\mathcal E-\frac{4\theta_0}{1+\theta_0}
=\frac{(1-3\theta_0)(S-S_0)/3+16(B-B_\Delta)+(1+\theta_0)L_s}{(1+\theta_0)R}.
\tag{4.1}
\]
Consequently:

* **Retention ⇒ \(r\)-free lower bound.** On any class of metrics with
  \(B\ge B_\Delta-o(Q)\), one has \(\mathcal E\ge 4h(1-6\theta)+o(h)\), independent of \(r\).
  All present constructions (KE exterior untouched, cells and handles adding their own \(W^-\))
  lie in this class.
* **Beating the \(r\)-free bound requires depletion.** A metric family with
  \(\mathcal E/h<4(1-6\theta)\) must have \(B<B_\Delta-cQ\): it must remove a positive fraction of
  the background anti-self-dual energy at the scale of the surgery budget. Since \(|W^-|^2\ge0\)
  pointwise, the reduction must occur where \(W^-_{KE}\) lives, i.e. where the KE metric is not
  locally symmetric. In the exact cusp-closing model below, all of \(B_\Delta\) lies in unit
  neighbourhoods of the ramification curves \(D'_\lambda\).
* **Why \(r=0\) is sharp and \(r>0\) is not, in the same identity.** By the signature formula,
  \(B-B_\Delta=12\pi^2k-\delta_+\), where \(\delta_+=\tfrac{4\pi^2}{3}A-\int|W^+_g|^2\) is the
  self-dual Weyl deficit relative to the KE level. On a ball quotient \(B_\Delta=0\) and
  \(B\ge0\) caps \(\delta_+\le12\pi^2k\): self-dual depletion beyond what the exceptional cells
  supply is impossible, which is exactly why the pure-handle value \(4\) is sharp. For \(r>0\) the
  background reservoir \(B_\Delta\) permits \(\delta_+\) up to \(B_\Delta+12\pi^2k\). LeBrun's
  monopole estimate prices \(\delta_+\le (S-S_0)/12\), i.e. at rate \(4\) in the numerator of (4.1)
  against a gain of \(16\); so no presently available inequality excludes the trade.
* **Localization by relative signature.** If \(g\) agrees with \(g_{KE}\) near \(\partial N\) of a
  region \(N\), the APS boundary terms coincide and
  \(\int_N(|W^+_g|^2-|W^-_g|^2)=\int_N(|W^+_{KE}|^2-|W^-_{KE}|^2)\). Depleting \(W^-\) in a
  ramification neighbourhood therefore depletes \(W^+\) there by the same amount: it is the
  **same non-Kähler self-dual depletion mechanism that produces the certified blow-up saving**,
  now acting on the background's ramification geometry instead of on an exceptional sphere.

**Exact location of the reservoir \(B_\Delta\) (computed).** `scripts/step33_cusp_closing_Wminus.py`
(→ `data/step33/cusp_closing_Wminus.json`, full SymPy Riemann/Weyl computation) treats the exact
cusp-closing Kähler–Einstein model: the Calabi ansatz over a flat torus,
\[
g=\tau(dx^2+dy^2)+\frac{d\tau^2}{\Theta}+\Theta\,\eta^2,\quad d\eta=dx\wedge dy,\qquad
\mathrm{Ric}=-g\iff\Theta=\tfrac23\tau^2-\frac{c}{\tau}.
\]
\(c=0\) is the complex-hyperbolic cusp. For \(c>0\) the circle closes at \(\tau_0=(3c/2)^{1/3}\) with
\(\Theta'(\tau_0)=2\tau_0\); with \(\psi\)-period \(2\pi/\tau_0\) the closing is smooth, the zero
section is an elliptic curve of self-intersection \(-e\), \(e=a\tau_0/2\pi\) (\(a\) = coordinate torus area).
The output is exact:
\[
s=-4,\qquad |W^+|^2=\tfrac23,\qquad |W^-|^2=\frac{6c^2}{\tau^6},\qquad
\int_{\tau\ge\tau_0}|W^-|^2\,d\mu=\frac{8\pi^2}{3}\,e .
\]
Since \(\Delta_m=\sum_{\rm components}e_c\) (Hurwitz/adjunction, Step 31), the model reproduces
\(B_\Delta=8\pi^2\Delta/3\) **exactly and entirely inside the cusp-closing neighbourhoods**. The
reservoir sits at unit curvature scale: \(|W^-|^2=8/3\) on \(D'\) (independent of \(c\)) and
\(|W^-|^2\sim C\,e^{-2\sqrt6\,d}\) at large distance \(d\) from \(D'\). Each \(D'_c\) is a flat-ish torus
of area \(2\pi e_c\) (in these units), so a positive-\(r\) tower offers \(\asymp\Delta=rQ\)
disjoint unit-size sites where the Kähler–Einstein background has \(O(1)\) anti-self-dual curvature
and is genuinely not CH. (Whether Biquard–Guenancia's metrics are \(C^2\)-close to this model on the
whole unit neighbourhood of \(D'\), as their construction strongly suggests, should be read off
their §4 model metric; the topological identity \(B_\Delta=8\pi^2\Delta/3\) itself is exact for any KE metric.)

This turns the \(r\)-question into a concrete local problem: **the cost of a blow-up (or handle)
cell placed in the cusp-closing model near \(D'\), with \(O(1)\) background \(W^-\)**. If it is below
the CH-site cost \(8\pi^2(1-\eta)\), the upper law improves with \(r\); if retention holds there, the
\(r\)-loss of the lower theory is an artefact.

The topology dependence of the optimal coefficient is therefore equivalent to a concrete geometric
question: **can surgery-scale energy deplete the anti-self-dual Weyl energy of the ramification
neighbourhoods at a favourable exchange rate?**

**Separated depletion is unfavourable (structure, partial proof).** On the unsurgered background,
\(\mathcal E\ge0\) and (4.1) with \(\theta_0=0\) give, for every metric on \(\bar X\),
\[
S-S_0\ \ge\ 48\,(B_\Delta-B)-3L_s ,
\]
so on \(\bar X\) itself depletion costs scalar excess at rate \(48\), not the rate \(12\) of the bare
monopole estimate (KE is the global minimizer, and Einstein metrics are critical for each
\(\int|W^\pm|^2\)). Now let \(g\) on \(M_m\) coincide with \(g_{KE}\) outside (i) the surgery regions,
placed where \(g_{KE}\) is \(\varepsilon\)-close to CH, and (ii) a disjoint modification region \(N\),
with exact-KE annuli in between. Restoring \(N\) to KE gives \(g_1\); modifying only \(N\) on
\(\bar X\) gives \(g'\). Then \(S,B\) are additive, \(\int|\mathrm{Ric}+g|^2\) is additive, and
\[
\mathcal N(g)=\mathcal N(g_1)+\bigl[\mathcal N_{\bar X}(g')-L_s(g')\bigr]
-\theta_0\Delta S_N+(1+\theta_0)\bigl(L_s(g)-L_s(g_1)\bigr),
\]
where \(\mathcal N\) is the numerator of (4.1) and \(\mathcal N_{\bar X}(g')\ge0\). For \(g_1\),
\(B(g_1)\ge B_\Delta-O(\varepsilon^2Q)\) because the cells replace regions with
\(|W^-_{KE}|=O(\varepsilon)\) by regions with \(|W^-|^2\ge0\); hence
\(\mathcal E(g_1)\ge4h(1-6\theta)-o(h)\) independently of \(r\). The remaining terms are the
scalar-variance comparison \(L_s(g)\) versus \(L_s(g_1)+L_s(g')\) and the \(O(h)\cdot\Delta S_N\)
correction; controlling them (both are lower order when \(s\) stays near \(-4\)) would prove that
**depletion separated from the surgery never improves the coefficient**. The \(r\)-dependence of the
true coefficient can therefore arise only from surgery cells that *interact* with the
non-locally-symmetric part of the KE background (cells placed in, or overlapping, ramification
neighbourhoods), not from the global count \(\Delta\). In the additive regime the true coefficient is
governed by local cell costs in CH-close regions and is \(r\)-independent.

By (1.1), lowering \(B\) by \(\delta\) lowers
\(P\) by \(4\delta\) at fixed \(S\); the monopole budget only forces \(S\ge S_0\), so no current
global estimate prices this exchange. A positive answer would give constructions beating \(4(1-6\theta)h\)
for large \(r\) by cells interacting with ramification geometry; a negative answer (an ASD-retention inequality \(B\ge B_\Delta-C(P+L_s+S-S_0)-o(Q)\))
would extend the positive linear gap to every \(r\) and every \(\theta<1/6\).

**Correction (Steps 34–35).** The variance obstacle above is removed by retaining the global
\(L_s(g)\ge0\) (Step 34), which proves the floor \(\mathcal E/h\ge4(1-6\theta)-o(1)\) in the separated class. That
floor does not give \(\mathcal E(g)\ge\mathcal E(g_1)-o(h)\); hence the sentence that separated depletion
"never improves the coefficient" and the claim that the coefficient is \(r\)-independent in the additive
regime are not established. The precise remaining local statement is a retention inequality
\(B_N\ge B_N^0-C_NP_N\) (see `step35_cap_transfer_neutrality_and_cap_cells.md`, §0). The statement that a
positive-\(r\) tower offers \(\asymp\Delta\) unit cap sites is not implied by divisor area; it now rests on
Theorem T (analytic slab transfer) and Proposition P (Heisenberg systole) of the Step-35 note, the latter
still requiring an explicit lattice write-up.

## 5. Background response of the cell

* **Exact first-order neutrality.** For the fixed certified cell glued into a background
  \(g_{CH}+\kappa\) on the exact-CH collar annulus, the first variation of
  \(\int|\mathrm{Ric}+g|^2\) in \(\kappa\) is \(2\int\langle\mathrm{Ric}+g,\,D(\mathrm{Ric}+g)[\chi\kappa]\rangle=0\),
  because \(\mathrm{Ric}+g=0\) wherever \(\chi\kappa\ne0\) at zeroth order. Hence background
  effects on a fixed cell are \(O(\|\kappa\|_{C^2}^2)\), the Step-31 estimate.
* **KE rigidity of \(R^+\).** For any KE background with \(\mathrm{Ric}=-g\), \(R^+=W^++s/12\) has
  spectrum \(\{-1,0,0\}\) pointwise, identical to CH. KE environments differ from CH only through
  \(W^-\) and covariant derivatives. Heuristic supplement (not yet a proof): the cell symmetry
  \(SU(2)_L\) is the \(\mathbf C\)-linear \(SU(2)\subset U(2)\) of the CH ball, so it acts trivially on
  \(\Lambda^+\) and irreducibly on \(\Lambda^-\); even after re-optimizing an \(SU(2)_L\)-symmetric core, a
  linear coupling can only see the \(SU(2)_L\)-invariant part of the background deviation, and a
  pointwise \(W^-\in S^2_0\Lambda^-\) has none (Schur). The expected leading coupling is quadratic in
  \(W^-\); symmetry-broken cells could couple linearly, but then pay their own second-order cost.
* Consequence: within KE towers, a larger first-order saving cannot come from the local background;
  it must come from the unrestricted cell problem itself (re-optimized nonlinear cores and tails),
  from non-Kähler Einstein environments where \(R^+\) acquires a positive eigenvalue
  (the first-order response principle of Step 8), or from the global \(W^-\)-depletion of §4.

## 6. Sharpened certificate for the authoritative cell

Profile `data/perp_area/x00.03_X128_d20.json` (degree 20, \(x_0=3/100\), \(X=128\), coefficients
the exact binary doubles; bolt shift \(q_F(0)+q_G(0)=0\) imposed exactly). Arb, 128 bits,
`acb_calc_integrate`, tol \(10^{-14}\), one piece, exact dyadic endpoints printed outwardly:
\[
\frac{J_6}{8\pi^2}\in[0.995670030344086466\ldots,\ 0.995670030355130639\ldots],
\]
\[
\frac{P}{8\pi^2}\in[0.995662732753254,\ 0.995662732771115],\qquad
\frac{\int(s+24)^2/4}{8\pi^2}\in[7.29759\times10^{-6}\pm6.4\times10^{-12}],
\]
and the independent reconstruction \(P+S\) overlaps \(J\) (interval \([0.995670030336849,0.995670030362368]\)).
Pointwise checks: \(\mathrm{Ric}=-6\) at the collar to \(3\times10^{-14}\), finite bolt values.
The new ball lies inside the Step-15 ball \([0.9956689792,0.9956710815]\) (that run reported a
much coarser radius). Hence
\[
\eta_{\rm cert}\ge0.004329969644869361,\qquad 4-\tfrac{8}{9}\eta_{\rm cert}\le 3.996151138093450 .
\]
The balanced (\(r=0\)) coefficient is now \(\limsup\alpha/h<3.9961512\) (after arbitrarily small
smoothing loss), superseding \(3.9961521\). The admissibility chain (positivity \(0\le S\le1\),
\(\hat F,\hat G>0\), ordinary \((-1)\) Hopf bolt with \(q_F(0)+q_G(0)=0\), weight-four anisotropy,
perpendicular topology \(D\#\overline{\mathbf{CP}}^2\), third-order CH contact, \(O(\delta^3)\) smoothing,
\(g\mapsto6g\)) is proved for every \(x_0>0\) and degree in
`Skills/.../20261004/step10_rigorous_subthreshold_cell_and_O11.md` §3–4 and therefore applies to this
exact profile; only the collar radius changes to \(7.6451\ldots\) in \(\mathrm{Ric}=-g\) units.

## 7. What this changes

The construction law and the lower law are governed by different variables: the upper bound by the
geometric blow-up fraction \(\theta\), the lower bound by the topological slope \(\sigma=4r+18\theta\).
At \(\sigma=0\) they meet (pure handles, exact value \(4\)). Along \(\theta\) the lower slope is
\(-24\) (explicit) or \(-18\cdot18/19\) while the upper slope is \(-4\eta\): the all-metric blow-up
tariff is the dominant unknown. Along \(r\) the lower bound decays with slope \(-16/3\) while the
upper is flat; by (4.1) this gap is precisely the question of anti-self-dual retention near the
ramification curves. Open: the true blow-up tariff (unrestricted cell infimum and its all-metric
counterpart), ASD retention/depletion, mixed blow-up–handle cells, density-free O10, collapse, and
fixed-manifold attainment.



---

## Source step35_cap_transfer_neutrality_and_cap_cells.md

Original: [sources/Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md](../sources/Sessions/S1003A01/workspace/notes/step35_cap_transfer_neutrality_and_cap_cells.md)

# Step 35 — Ramification caps: exact chiral curvature, quadratic environment neutrality of the cell infimum, the analytic and arithmetic cap transfer, and the admissible cap-cell problem

Conventions: \(\operatorname{Ric}=-g\) (so \(s=-4\)) unless stated; \(D(g)=\int|\operatorname{Ric}+g|^2\) is the
closed-family defect entering \(\mathcal E=(4D-T^2/V)/(4V+D-2T)\) (Step 32); \(B=\int|W^-|^2\),
\(B_\Delta=8\pi^2\Delta/3\), \(t=h(1-6\theta)\). Cap model (Steps 33–34):
\[
g_C=u(dX^2+dY^2)+\frac{du^2}{q(u)}+q(u)\,(d\Psi+X\,dY)^2,\qquad q(u)=\tfrac23(u^2-u^{-1}),\ u\ge1 .
\]

## 0. The separated theorem, with its correct reach

Step 34 proved, for surgery in \(U\), a topology-preserving modification in a disjoint \(N\), exact KE matching
annuli, metricwise actual-field scalar supply, \(0\le t\le 1/3\), \(B_U^0=o(Q)\), \(\Delta/A\to0\):
\[
\mathcal N(g)\ \ge\ -16B_U^0-48tB_N^0+\tfrac{1-3t}{3}\bigl(S(g_1)-S_0\bigr)+4(1-3t)P_N+(1+t)L_s(g),
\qquad \mathcal E(g)\ge 4h(1-6\theta)-o(h).
\]
What this proves is the floor \(4(1-6\theta)\) for \(\mathcal E/h\) in the separated class. At \(\theta=0\) it meets the
upper coefficient \(4\); for \(0<\theta<1/6\) it lies far below the construction \(4(1-\eta\theta)\). It does **not**
prove \(\mathcal E(g)\ge\mathcal E(g_1)-o(h)\), and therefore does not exclude a first-order \(r\)-dependent
improvement by separated modifications. The exact obstruction is visible in the decomposition
\[
\mathcal N(g)=\mathcal N_0(g_1)+\bigl[4(1-3t)P_N+48t\,\delta B_N\bigr]+(1+t)L_s(g),
\qquad \mathcal N_0(g_1)=\tfrac{1-3t}{3}(S(g_1)-S_0)+16(B(g_1)-B_\Delta),
\]
which uses only \(P_N=\delta S_N/12+4\delta B_N\). A separated modification can lower the numerator only if
\(48t|\delta B_N|>4(1-3t)P_N\), i.e. it must strip anti-self-dual energy at Ricci cost \(P_N<12t|\delta B_N|/(1-3t)\),
which tends to zero with \(h\). A local retention inequality \(B_N\ge B_N^0-C_NP_N\) with \(C_N\) uniform over sites
would close this (no gain whenever \(t\le 1/(3+12C_N)\)); it is not proved. By the relative identity it is
equivalent to a relative volume bound \(\delta V_N\le(3/4+3C_N)P_N\) at \(s=-4\). This is recorded as the precise open
local statement of the separated class, not as an established exclusion.

## 1. Exact chiral curvature of the cap (computed)

`scripts/step34_cap_weyl_operator.py` (bug fixed: integer zero had no `.subs`) →
`data/step34/cap_weyl_operator.json`. Orthonormal coframe \(e^0=d\tau/\sqrt\Theta,\ e^1=\sqrt\tau dx,\ e^2=\sqrt\tau dy,\
e^3=\sqrt\Theta(d\psi+x\,dy)\), orientation \(e^{0123}\), \(\omega=e^{03}+e^{12}\in\Lambda^+\). Exact output, with
\(\Theta=\tfrac23\tau^2-c/\tau\):
\[
\operatorname{Ric}=-g,\quad
W^+=\operatorname{diag}\!\left(-\tfrac23,\tfrac13,\tfrac13\right),\quad
W^-=\frac{c}{\tau^3}\operatorname{diag}(2,-1,-1),
\]
in the bases \(\{(e^{03}\pm e^{12}),(e^{01}\pm e^{23}),(e^{02}\mp e^{13})\}/\sqrt2\). Hence \(|W^-|^2=6c^2/\tau^6=8/(3u^6)\)
(agreeing with Step 33) and, at the divisor \(u=1\),
\[
W^-=\tfrac23\operatorname{diag}(2,-1,-1),\qquad R^-=W^-+\tfrac{s}{12}=\operatorname{diag}(1,-1,-1),\qquad R^+=\operatorname{diag}(-1,0,0).
\]
Consequences. (i) \(W^+\) and \(s\) are pointwise identical to CH, and \(\nabla W^+=0\) since \(\nabla\omega=0\); the cap
differs from CH **only** through \(W^-\). (ii) \(W^-\) is type D with simple positive eigenvector
\(\bar\omega=e^{03}-e^{12}\) (normal area minus divisor area); by Derdziński the cap is conformally Kähler for the
reversed complex structure with factor \(|W^-|^{2/3}\propto u^{-2}\), i.e. it is ambi-Kähler. (iii) The anti-self-dual
curvature operator has a **positive** eigenvalue \(+1\) at \(D'\), where CH has \(R^-=-\tfrac13\mathrm{Id}\). (iv) Both the
normal plane \(e^{03}\) and the divisor plane \(e^{12}\) have sectional curvature \((R^+_{11}+R^-_{11})/2=0\) at \(D'\); mixed
planes have \(-\tfrac12\).

Scale. Distance from \(D'\) is \(d(u)=\int_1^u dv/\sqrt{q(v)}\):
\(d=0.447,0.994,1.388,1.904,2.536\) at \(u=1.1,1.5,2,3,5\); the reservoir fraction inside is
\(0.317,0.802,0.9375,0.988,0.9984\). On the certified \(x_0=.03,X=128\) cell
(`data/step29/local_AK_flux_certified_x003_X128.json`), the raw action beyond physical radius
\(r=\sqrt6\operatorname{arsinh}\sqrt x\) is \(0.119,\,0.0040,\,0.00033\) at \(r=0.76,2.16,3.78\). The cell's action core and the
cap reservoir therefore live on the **same** \(O(1)\) scale (not a small-cell or small-background regime); a cap cell
is a genuinely nonlinear object.

## 2. The blow-up chiral ledger in any Einstein environment

**Step-36 correction.** The formulas in this section are exact, but the exclusion inferred from them below is not. For one blow-up,
\[
\delta S=12P+480\pi^2-48b.
\]
Thus net \(W^-\)-depletion is accompanied by a large scalar-square contribution, but a bound such as \(P\le8\pi^2\) does not by itself force the previously stated inequality \(\delta S>576\pi^2\): \(\delta S\) is the change in \(\int s^2\), not the nonnegative residual \(\int(s+4)^2\), and volume/scalar-moment compensation is still possible. Treat the ledger as a payment identity, not as an exclusion of cap interaction.

For a modification of a region with fixed outer germ which adds \(k\) blow-ups and \(\ell\) handles, relative Euler
and signature give, with \(a=\delta\!\int|W^+|^2,\ b=\delta\!\int|W^-|^2\),
\[
b=a+12\pi^2k,\qquad P=8\pi^2(k+4\ell)+4a+\frac{\delta S}{12}.
\]
(Check: Burns in flat space, \(a=\delta S=0\), gives \(b=12\pi^2\), \(P=8\pi^2\).) When a particular cell has \(|a|\ll12\pi^2\), as the certified CH cell does, the identity says that this cell adds about \(12\pi^2\) of anti-self-dual energy relative to its own background. This fact about that cell is not a general consequence of being near the \(P\)-tariff, because \(\delta S\) can compensate a large negative \(a\). Net \(W^-\) depletion by a blow-up cell (\(b<0\)) forces \(a<-12\pi^2\), while the exact rearrangement is \(\delta S=12P+480\pi^2-48b\). This records a large scalar-square payment but, because \(\delta S\) is relative and includes scalar-moment and volume exchange, it does not exclude compensation or determine the cap-cell cost. The cap can enter through finite-amplitude geometry, changing the attainable coupled \(W^+\), scalar, volume, and \(W^-\) channels. The ledger preserves that payment rather than deciding its sign.

## 3. Buffered Einstein-environment transfer (correction to the former Theorem N)

**Step-36 correction.** The construction below does not belong to the stated target class: it equals \(g_2\) only on a smaller outer collar, whereas \(j_{g_2}(R)\) prescribes \(g_2\) on the entire annulus \(A\). Therefore the same-class conclusion \(|j_{g_1}(R)-j_{g_2}(R)|\le C\varepsilon^2\) and the claimed exclusion of first-order adapted core responses are withdrawn. What the cutoff proves is a useful buffered comparison: after adding transition space, or after shrinking the prescribed target collar, a given competitor transfers with \(O(\varepsilon^2)\) defect. Moving the transition inward while preserving the whole same annulus needs further collar space or control depending on the competitor.

**Setting of the former statement.** Let \(B_R\) be a ball with annulus \(A=B_R\setminus B_{R-1}\). For an Einstein metric \(g_b\) (\(\operatorname{Ric}=-g_b\))
on a neighbourhood of \(\bar B_R\), let \(j_{g_b}(R)=\inf D(g)\) over smooth metrics \(g\) on
\(B_R\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) (fixed marking) with \(g=g_b\) on \(A\). Let \(g_1,g_2\) be two such
Einstein metrics with \(\|g_1-g_2\|_{C^2(A,g_2)}\le\varepsilon\le\varepsilon_0\).

**Statement.** \(|j_{g_1}(R)-j_{g_2}(R)|\le C\varepsilon^2\), with \(C\) depending only on \(R\), a cutoff, and \(C^2\) bounds of
\(g_2\) on \(A\); it is uniform over all competitors.

**Proof.** Given a competitor \(g\) for \(g_1\), define \(G=g\) on \(B_{R-1}\), \(G=g_2+\chi(g_1-g_2)\) on \(A\) with
\(\chi=1\) near the inner and \(0\) near the outer boundary, and \(G=g_2\) outside. \(G\) is smooth and positive. Since
\(g=g_1\) is Einstein on \(A\), \(D(g)=\int_{B_{R-1}}|\operatorname{Ric}(g)+g|^2\). On \(A\), with \(k=g_1-g_2\),
\(\operatorname{Ric}(G)+G=\mathcal L_{g_2}[\chi k]+O(|k|^2_{C^2})\), \(\mathcal L=D(\operatorname{Ric}+g)\); and
\(\mathcal L_{g_2}[k]=O(|k|_{C^2}^2)\) because both metrics are Einstein, so
\(\mathcal L_{g_2}[\chi k]=\chi\mathcal L_{g_2}[k]+O(|\nabla\chi||k|_{C^1}+|\nabla^2\chi||k|)=O(\varepsilon)\). Hence
\(D(G)\le D(g)+C\varepsilon^2\). Exchange the roles. \(\square\)

**Valid consequence after correction.** If a construction supplies a fixed buffer in which the prescribed collar may be shrunk, the displayed interpolation gives an \(O(\varepsilon^2)\) added defect for that competitor. This remains useful for transferring a known exact-model cell into a nearby closed Einstein background, because the marked ball construction already includes a buffer. It does not establish flatness of the same exact-collar infimum, and does not constrain a core adapted to the nearby environment when no such buffer is part of the comparison class.

## 4. Theorem T (analytic cap transfer on fixed normalized slabs)

**Inputs (Biquard–Guenancia \cite{biquard2022degenerating}, §4).** On the fixed holomorphic disc-bundle neighbourhood
\(U\) of a cusp divisor, the model \(\omega_\beta\) is the exact Calabi-ansatz KE cone metric (its potential solves
\((i\partial\bar\partial\psi_\beta)^2=e^{\psi_\beta}\Omega\wedge\bar\Omega\)), the actual conic KE metric \(\hat\omega_\beta\)
satisfies \(\operatorname{Ric}=-\hat\omega_\beta\), and Lemma 4.4 gives \((1-\varepsilon_\beta)\omega_\beta\le\hat\omega_\beta
\le(1+\varepsilon_\beta)\omega_\beta\) on \(U^*\) with \(\varepsilon_\beta\to0\); they note \(dd^cF_\beta=\hat\omega_\beta-\omega_\beta\) for
\(F_\beta=\log(\hat\omega_\beta^2/\omega_\beta^2)\). The §4.3 ramified congruence covers \(\bar\pi_m\) have ramification
\(v_{m,\lambda}=1/\beta_{m,\lambda}\) along \(D\), so \(\omega_m=\bar\pi_m^*\hat\omega_{\beta_m}\) is smooth KE on \(\bar X_m\) and
\(\bar\pi_m^*\omega_{\beta_m}\) is the smooth Calabi cap \(g_C\) (Step 34 normalization) on \(\bar\pi_m^{-1}(U)\).

**Lemma C (local KE comparison).** Let \(\omega_0,\omega_1\) be Kähler on a holomorphic ball \(B_{2\rho}\) with
\(\operatorname{Ric}=-\omega_i\), \(\omega_0\) with \(C^{k+3}\) bounds \(\Lambda\) in the chart, and
\((1-\varepsilon)\omega_0\le\omega_1\le(1+\varepsilon)\omega_0\), \(\varepsilon\le1/2\). Then
\(\|\omega_1-\omega_0\|_{C^{k,\alpha}(B_\rho)}\le C(k,\rho,\Lambda)\,\varepsilon\).

*Proof.* \(F=\log(\omega_1^2/\omega_0^2)\) satisfies \(|F|\le3\varepsilon\), \(dd^cF=\omega_1-\omega_0\), \(|dd^cF|_{\omega_0}\le2\varepsilon\),
and \((\omega_0+dd^cF)^2=e^F\omega_0^2\). The complex Hessian of \(F\) is bounded and the equation is concave and uniformly
elliptic; the interior complex Evans–Krylov estimate (bounded complex Hessian suffices; e.g. Tosatti–Wang–Weinkove–Yang,
citation to be registered) gives \(\|F\|_{C^{2,\alpha}(B_{3\rho/2})}\le C\). In dimension two
\((\omega_0+\beta)^2/\omega_0^2=1+\operatorname{tr}\beta+\det\beta\), so
\(\Delta_{\omega_0}F-F=(e^F-1-F)-\det_{\omega_0}(dd^cF)=:N\) with \(\|N\|_{C^\alpha}\le C\varepsilon\). Schauder gives
\(\|F\|_{C^{2,\alpha}(B_{5\rho/4})}\le C\varepsilon\); differentiating the equation and bootstrapping gives
\(\|F\|_{C^{k+2,\alpha}(B_\rho)}\le C_k\varepsilon\). \(\square\)

**Theorem T.** For every \(L\ge1\), \(k\ge0\) there is \(C(k,L)\) such that on every lifted slab
\(\Sigma_{L}=\{1\le u\le L\}\subset\bar\pi_m^{-1}(U)\),
\[
\sup_{\Sigma_L}\bigl|\nabla^j_{g_C}(g_m-g_C)\bigr|_{g_C}\le C(k,L)\,\varepsilon_{\beta_m}\qquad(j\le k).
\]
*Proof.* Pull back the Lemma 4.4 inequality (pullback by the local branched cover preserves it on the complement of the
divisor; both lifted metrics are smooth, so it extends across \(D_m\)). For \(\beta\) small, \(\{u\le L+1\}\) corresponds to
\(\beta t\le-c(L)<0\) and lies in \(U\). Apply Lemma C on holomorphic balls of fixed \(g_C\)-size in the horizontal
universal cover of \(\{u\le L+1\}\): the universal pointed model is homogeneous along \(D'\), smooth up to \(u=1\), and has
uniform holomorphic charts, independent of \(m\) and of the horizontal lattice. Estimates are local, so they descend. \(\square\)

**Corollary (concentration).** Uniform \(C^2\) convergence on slabs and the exact model fraction give
\(\sum_c\int_{\Sigma_{L,c}}|W^-(g_m)|^2=(1-L^{-4})B_\Delta(1+O(\varepsilon_{\beta_m}))\); since the total is exactly
\(B_\Delta\) for any KE metric, the complement carries at most \((L^{-4}+O(\varepsilon_{\beta_m}))B_\Delta\). If \(\Delta/Q\) grows,
choose \(L\) with \(\Delta L^{-4}=o(Q)\).

The derivative upgrade needs only that both metrics are KE with the same constant and that BG's comparison is ratio-one
in \(C^0\); it does not need their remark on global derivative control of the degenerating family.

## 5. Proposition P (packing via the Heisenberg lattice) — arithmetic part, with its checks

For a cusp component \(D_c\) of \(\bar X_m\), the normalized horizontal metric on \(D_c\) is flat of area \(2\pi e_c\),
\(e_c=-D_c^2\). A normalized cap ball of radius \(\rho\) about \(p\in D_c\) embeds when the normalized horizontal systole
exceeds \(2\rho\) (central elements are the \(\Psi\)-rotations, which fix \(D_c\)). If the horizontal lattice is similar to a
fixed lattice up to bounded index (shape-bounded), then \(\mathrm{sys}^2_{\rm norm}\ge c_0\,e_c\).

For principal congruence of level \(\mathfrak a=p^nO_K\), \(p\) inert, in a Picard group: the horizontal projection of the
cusp lattice lies between \(\mathfrak a\mathfrak b_1\Lambda_0\) and \(\mathfrak a\mathfrak b_2^{-1}\Lambda_0\) for fixed
\(\mathfrak b_i\), so it is shape-bounded; horizontal covolume grows by \(N(\mathfrak a)=p^{2n}\) and the central period by
\(\asymp\vartheta_{\mathfrak a}=p^n\), so \(e_c\asymp p^{n}\). Cross-check with Džambić \cite{dambi2014invariants},
\((T\cdot T)=-h_K\eta_K\vartheta_{\mathfrak a}^{-2}[\Gamma_K:\Gamma_K(\mathfrak a)]\asymp p^{6n}\): it gives
\(\#\text{cusps}\asymp p^{5n}\), matching \([\Gamma_K:\Gamma_K(\mathfrak a)]/[\Gamma_P:\Gamma_P(\mathfrak a)]\asymp p^{8n}/p^{3n}\)
(the parabolic image is the 3-dimensional unipotent radical; the Levi part of \(\Gamma_P\) is finite). Hence
\(\mathrm{sys}_{\rm norm}\asymp p^{n/2}\to\infty\), each component holds \(\asymp e_c/\rho^2\) disjoint embedded normalized cap
balls, and the tower holds \(\asymp\Delta\) of them. Status: consistent derivation from the Heisenberg structure and an
independent count; the lattice inclusions and the central index should still be written out explicitly from Hill's or
Holzapfel's description before the proposition is quoted as a theorem.

With Theorem T, the buffered transfer estimate above, and the still-to-be-completed Proposition P, any fixed cap cell with an exact Calabi collar and an additional marked buffer can be transferred to the positive-\(r\) towers with total error \(o(Q)\), as in the CH-cell insertion. This statement uses the buffer and is not the withdrawn same-class comparison.

## 6. The admissible cap-cell problem

**Local symmetry at the divisor.** In the symmetric gauge \(\Psi'=\Psi+XY/2\),
\(g_C=u(dX^2+dY^2)+du^2/q+q(d\Psi'+\tfrac12(X\,dY-Y\,dX))^2\), so the isotropy of \(p=(0,0,u{=}1)\) in the universal model
contains \(T^2=U(1)_{\rm rot}\times U(1)_{\Psi'}\), with weights \((1,0)\) on the divisor plane and \((0,1)\) on the normal
plane: locally the cap is a toric KE corner. \(T^2\) contains \(U(1)_+\) (weights \((1,1)\), rotating \(\omega^\perp\subset\Lambda^+\)) and
\(U(1)_-\) (weights \((1,-1)\), trivial on \(\Lambda^+\), fixing \(\bar\omega\in\Lambda^-\)).

**Two genuinely different trial classes.**
1. *Toric (cohomogeneity two).* The \(T^2\)-equivariant blow-up of the corner. Its exceptional sphere is \(T^2\)-invariant,
   so at its poles the tangent plane is a weight plane and its \(\Lambda^+\) part is parallel to \(\omega\): this is the
   **aligned** branch. Kähler competitors are expected to obey the inherited period law \(P=2(2\pi+t)^2+L/4>8\pi^2\) (derived for
   Kähler cells with Einstein collar and \(\lambda=-1\); its use with the Calabi collar should be rechecked), and
   A02's closed Kähler tariff \(P>8\pi^2k\) points the same way, so a successful toric cell must be non-Kähler; it tests whether the positive \(R^-\) at \(D'\) changes the aligned first-order
   cost through finite-amplitude or higher-order coupling. The positive cap eigenvalue lies in \(R^-\), whereas the inherited glued-Burns first variation uses \(R^+(\hat\zeta,\hat\zeta)\). At the aligned cap direction \(R^+=-1\), so the linear term is unfavorable; the Fubini–Study analogy does not apply at first order.
2. *Perpendicular (cohomogeneity three, \(U(1)_-\)-invariant).* The certified mechanism needs the exceptional
   \(\Lambda^+\) direction \(\perp\omega\); the only part of the cap isotropy compatible with it is \(U(1)_-\). A cap
   perpendicular cell is therefore a \(U(1)_-\)-invariant metric on \(B_\rho(p)\#\overline{\mathbb{CP}}^2\) equal to \(g_C\) on the
   collar. A direct transplant of the certified perpendicular core, including its complete interpolation to the Calabi collar, is the first realizable probe; no same-class neutrality theorem rules it out.

**Decision quantity.** For either class, compute the full \(D=\int|\operatorname{Ric}+g|^2\), with \(\delta V\), \(\delta\!\int s\), and the
ledger \(a,b\) of §2 as checks (\(b-a=12\pi^2k\) exactly). Compare with the certified CH value
\(8\pi^2\times0.995670030355131\). A first, inexpensive, decisive object is a finite block in the toric class: a
\(T^2\)-invariant blow-up family with regular corner/edge expansions, exact cap outside \(B_\rho\), a few response
amplitudes, and direct evaluation of \(D\); no stationary base or continuum Jacobi inverse is assumed.

## 7. State

Established in Step 35 and retained after Step-36 corrections: exact cap \(W^\pm\) (§1); the chiral ledger formulas (§2); a buffered cutoff transfer, not same-class infimum flatness; Lemma C and Theorem T with proof modulo the cited complex Evans–Krylov estimate; concentration corollary. Derived with explicit
checks still to write: Proposition P. Open: local retention for the separated class (§0); the toric and \(U(1)_-\) cap cells
(§6); the unrestricted blow-up tariff, mixed cells, non-diagonal collapse, density-free O10, Dehn-twist attainment.



---

## Source step36_perpendicular_cap_transplant.md

Original: [sources/Sessions/S1003A01/workspace/notes/step36_perpendicular_cap_transplant.md](../sources/Sessions/S1003A01/workspace/notes/step36_perpendicular_cap_transplant.md)

# Step 36 — A realizable perpendicular-core transplant into the Calabi cap

Conventions: closed-family scale `Ric=-g`,
\[
D(g)=\int|\operatorname{Ric}+g|^2,
\qquad P(g)=\int|\operatorname{Ric}^{\circ}|^2,
\qquad D=P+\frac14\int(s+4)^2.
\]
The authoritative CH cell has
\[
D/(8\pi^2)\le 0.995670030355131.
\]
This note records a finite-amplitude construction experiment, not an infimum or lower theorem.

## 1. Corrections to Step 35

Three statements from `step35_cap_transfer_neutrality_and_cap_cells.md` were corrected in that file.

1. The cutoff used in the former Theorem N equals the target Einstein metric only on a smaller outer collar, not on the entire prescribed annulus. It proves an \(O(\varepsilon^2)\) **buffered transfer** for a given competitor; it does not compare the two same-annulus cell infima and does not exclude a first-order environment-adapted response.
2. The positive cap eigenvalue lies in \(R^-\). The glued-Burns first variation uses \(R^+(\hat\zeta,\hat\zeta)\). At the aligned cap direction \(R^+=-1\), so the first-order term is unfavorable. Any toric benefit must be nonlinear or higher order; chirality reversal would be a different signed-surgery problem.
3. The exact ledger
   \[
   b=a+12\pi^2,
   \qquad P=8\pi^2+4a+\frac{\delta S}{12},
   \qquad \delta S=12P+480\pi^2-48b
   \]
   is a payment identity. Because \(\delta S\) is the change in \(\int s^2\), not the nonnegative residual \(\int(s+4)^2\), it does not exclude scalar-moment and volume compensation. The incorrect \(576\pi^2\) inference was removed.

The cap construction remains valuable because it tests a new actual geometry, not because these corrected statements eliminate alternatives.

## 2. Construction

`scripts/step36_cap_perp_transplant.py` transports the certified perpendicular core into the exact universal Calabi cap.

### 2.1 Perpendicular core in a common marking

The stored cell has `Ric=-6g` and radial coordinate \(x\). Scale by six. In the CH exponential marking \(\xi=rv\in\mathbb R^4\),
\[
x=\sinh^2(r/\sqrt6).
\]
If the old diagonal orbit matrix is \(h=\operatorname{diag}(h_1,h_2,h_3)\), its scaled exponential-coordinate eigenvalues are
\[
\frac{x(1+x)}G,
\quad \frac{6h_1}{r^2},
\quad \frac{6h_2}{r^2},
\quad \frac{6h_3}{r^2}
\]
in the radial, perpendicular-bolt, companion, and Hopf directions. This reproduces scaled CH exactly when
\(G=x(1+x)\), \(h=(x,x,x(1+x))\). The bolt and the old core metric are unchanged.

### 2.2 Exact cap in proper normal coordinates

Use divisor coordinates \((X,Y)\) and proper normal polar coordinates \((n,\Psi)\), written Cartesian as \((Z,W)\), \(n^2=Z^2+W^2\). Then
\[
u(n)=\cosh(\sqrt{3/2}\,n)^{2/3},
\qquad q(u)=\frac23(u^2-u^{-1}),
\qquad du/dn=\sqrt q,
\]
and
\[
g_C=u(dX^2+dY^2)+dn^2+q\left(d\Psi+\frac12(XdY-YdX)\right)^2.
\]
The script evaluates the exact Cartesian matrix; its generic coordinate-Ricci routine gives `Ric+g` residuals between \(9\times10^{-16}\) and \(3\times10^{-15}\) at test points.

### 2.3 Full transition and response modes

For \(a<r<b\), put
\[
H(t)=t^4(35-84t+70t^2-20t^3),
\qquad t=\frac{r-a}{b-a},
\]
\[
g_0=(1-H)g_{\rm cell}+Hg_C.
\]
Since \(H' =140t^3(1-t)^3\), \(0\le H\le1\), so the baseline is positive. Three compactly supported modes with
\(F(t)=256t^4(1-t)^4\) vary the interpolation path, conformal scale, and horizontal-normal trace-free splitting:
\[
F(g_C-g_{\rm cell}),\qquad Fg_0,
\qquad \frac F2(g_0S+Sg_0),\quad S=\operatorname{diag}(-1,-1,1,1).
\]
The metric is literally \(C^3\) at the two joins, which is enough for ordinary continuous Ricci curvature; it can be smoothed in thin collars with arbitrarily small change in all reported integrals. It should therefore be called a smoothable trial, not already \(C^\infty\).

The core is integrated in the old exact radial coordinates. The whole transition is integrated by Sobol quadrature in \(\mathbb R^4\), using JAX automatic differentiation of the full coordinate metric and no symmetry formula for Ricci. The exact cap outside contributes zero defect.

## 3. Numerical results

The first pilot used incompatible algebraic radial charts and cost \(12.78\); it was superseded after both geometries were placed in the markings above (`data/step36_cap_perp_pilot.json` is retained only as a failed attempt).

### 3.1 Baseline scans

`data/step36/cap_perp_baseline_scan.json` and `cap_perp_width_scan.json` scan several \((a,b)\). The best tested pair was \((0.5,1.5)\):
\[
D/(8\pi^2)=2.44057,
\qquad P/(8\pi^2)=1.68279.
\]
The core to \(a=0.5\), where \(x_a=0.0422486\), contributes only
\[
D_{\rm core}/(8\pi^2)=0.459454,
\]
while the transition contributes \(1.98112\). Wider or later transitions were more expensive. For example \((a,b)=(0.6,1.8)\) gives \(D/(8\pi^2)\simeq3.09\), while \((1.2,2.1)\) gives about \(23.9\). The large growth means that this radial identification accumulates substantial profile/marking mismatch when it is extended farther out.

### 3.2 Three-mode response

The three response coefficients were fitted on 128 fixed Sobol points at \((a,b)=(0.5,1.5)\):
\[
(c_0,c_1,c_2)=(0.1122072,-0.0048520,-0.0118740).
\]
The in-sample value \(2.20827\) is optimistic. On three independent 512-point samples (`cap_perp_response_validation.json`),
\[
D/(8\pi^2)=2.25792,\ 2.26806,\ 2.26950,
\]
with mean \(2.26516\). The minimum sampled coordinate eigenvalue is \(0.272\)--\(0.279\), so positivity is numerically strong but not certified over the full annulus. The response recovers roughly \(0.18\) from the baseline but leaves the transition dominant.

At validation seed 1,
\[
P/(8\pi^2)=1.57336,
\quad \delta V=-1.06969,
\quad a/(8\pi^2)=0.07113,
\quad b/(8\pi^2)=1.57113.
\]
The ledger values are reconstructed from relative Chern--Weil; `b-a=12pi^2` is therefore automatic rather than an independent numerical check.

### 3.3 Same-pipeline CH control

The identical core truncation, interpolation, quadrature, and response family were rerun with exact CH as the outer metric (`ch_perp_same_pipeline.json`, `ch_perp_response_validation.json`). At \((0.5,1.5)\), the baseline gives
\[
D_{\rm CH-control}/(8\pi^2)=1.581\text{--}1.589,
\]
and independently validated response coefficients give
\[
D_{\rm CH-control}/(8\pi^2)=1.534,\ 1.541.
\]
Thus about \(0.73\) of the optimized cap trial's normalized cost is cap-specific within this same radial three-mode pipeline, but about \(0.54\) above the certified threshold is already caused by truncating the successful cell at \(a=0.5\) and rebuilding its long optimal CH transition with only three modes. The experiment therefore separates two effects:

- the chosen radial cap identification is genuinely costly relative to the CH control;
- the trial space is too thin even to recover the known CH construction.

It would be wrong to interpret \(2.265\) as the cap-cell infimum, or the cap--CH difference as an intrinsic invariant of the cap.

## 4. Verification and interpretation

TTCS independently checked the scaling, exponential CH reconstruction, exact cap Cartesian matrix, Ricci and norm contractions, shell Jacobian, core/annulus matching, scalar moments, and ledger in `trace/ttcs/results/step36_ttcs01_verifier1_integration.md`. No normalization error capable of moving the values near one was found. It identified the \(C^3\) versus \(C^\infty\) point, sampled rather than uniform positivity, the automatic ledger check, and the need for the same-pipeline CH control; the first three are recorded above and the CH control was then computed.

The result changes the constructive judgment without excluding cap benefit. A direct radial transplant of an early perpendicular core into the cap is a poor construction. The cost is generated mainly in the transition and, after subtraction of the CH control, remains substantially cap-dependent. The positive \(R^-\) eigenvalue does not automatically rescue this metric. But the control also shows that most of the successful CH transition has been thrown away: the certified cell is exact CH only at physical radius about \(7.65\), while the trial cuts it at \(0.5\) and reaches the cap by \(1.5\). Richer \(U(1)_-\) modes, an optimized diffeomorphism/marking, a cap-adapted core, or a matched short-collar solution remain open and could change the sign.

The next constructive step should therefore optimize the **transition itself** in the common cap chart and demand simultaneous success on the CH control. A useful response family must first reduce the CH control from \(1.54\) toward the known \(0.99567\); only then does its cap--CH comparison isolate the nonlinear \(W^-\) response rather than lack of representation. A toric non-Kähler trial remains complementary, but the cap's \(R^-\) sign supplies no favorable aligned first-order prediction.

## 5. Analytic cap transfer

The external regularity source is now registered: Tosatti--Wang--Weinkove--Yang prove a local \(C^{2,\alpha}\) estimate for equations \(F(S+T(D^2u,x),x)=f\) under uniform ellipticity, concavity, Hölder coefficients and source, a matrix-range condition, and an \(L^\infty\) bound on \(u\) \cite{tosatti2015alpha}. Their complex Monge--Ampère application uses the \(J\)-invariant projection of the real Hessian; it does not assume a bound on the full real Hessian. This supports Step 35's local derivative upgrade only after verifying uniformly, on the reciprocal-angle lifted charts, the chart size, smooth reference coefficients, potential normalization/oscillation, ellipticity, and source Hölder bounds. Biquard--Guenancia's ratio-one metric comparison supplies the complex-Hessian range and ellipticity. The remaining uniform-potential normalization and chart-constant bookkeeping should be written explicitly before Theorem T is quoted in a final theorem.

Wolfram was checked again and is unavailable because the local Engine license has expired; the exact and automatic-differentiation work used SymPy/JAX.



---

## Source step37_cap_congruence_transport.md

Original: [sources/Sessions/S1003A01/workspace/notes/step37_cap_congruence_transport.md](../sources/Sessions/S1003A01/workspace/notes/step37_cap_congruence_transport.md)

# Step 37 — Congruence transport of the full certified cell into the Calabi cap

Conventions: closed-family scale `Ric=-g`, \(D=\int|\operatorname{Ric}+g|^2\), \(P=\int|\operatorname{Ric}^\circ|^2\), values reported as \(D/(8\pi^2)\). The certified CH cell has \(D/(8\pi^2)\le0.995670030355131\) (`data/step33/rigorous_x00.03_X128_d20_J_exact.json`). Everything below is floating (scrambled Sobol, stratified radial shells) evidence for a construction question, not an enclosure or a lower bound.

## 1. Construction

Let \(g_*\) be the certified \(x_0=.03,\ X=128\) perpendicular cell, scaled by 6 and written in the CH exponential chart \(\xi\in\mathbb R^4\) at its centre (`step36` marking, \(x=\sinh^2(r/\sqrt6)\)). Off the bolt, \(g_*\) and \(g_{\rm CH}\) are diagonal in the same Euclidean-orthonormal equivariant frame \(v_0=z,\ v_1=(-\bar z_2,\bar z_1),\ v_2=iv_1,\ v_3=iz\), so
\[
L=(g_{\rm CH}^{-1}g_*)^{1/2}=\sum_k\sqrt{\lambda_k/\lambda_k^{\rm CH}}\;v_kv_k^{T}
\]
is explicit. With the \(C^3\) smoother \(H\) on \(a<r<b\) and \(\bar g=(1-H)g_{\rm CH}+Hg_{\rm out}\),
\[
G=L\,\bar g\,L\quad(r\ge a),\qquad G=g_*\quad(r<a).
\]
\(G\) is positive by congruence; it equals \(g_*\) identically when \(g_{\rm out}=g_{\rm CH}\) (any \(a,b\)); it equals \(g_{\rm out}\) for \(r\ge R_{\rm cell}=\sqrt6\operatorname{arsinh}\sqrt{128}=7.6451\), because the profile is exactly CH there. Bolt, topology, rel-boundary marking and the exact exterior are those of the certified cell. A variant tapers the deformation, \(L_{\rm taper}=L^{1-H((r-c)/(d-c))}\). Script: `scripts/step37_cap_congruence_transport.py`; core \(r<a\) is integrated radially exactly (step36 `core_integrals`), the rest in 4D.

**Pipeline check.** With \(g_{\rm out}=g_{\rm CH}\), the 4D shells plus the radial core give \(0.99568\) (\(2^9\) points/shell, `data/step37/ch_control_a05_b15_n9.json`) and \(0.99565\pm0.0019\) (\(2^{11}\), `data/step37/base/base_ch_s1.json`), reproducing the certified value. The CH control is therefore exact by construction, removing the representation loss of Step 36 (which gave 1.54 for its CH control).

## 2. Cap results in the step-36 (Fermi-type) chart

The cap \(g_C\) is written in \((X,Y)\) flat divisor coordinates and \((Z,W)\) proper normal exponential coordinates; this is a Fermi-type chart about \(D'\), not the cap's exponential chart at \(p\).

| construction | \(D/(8\pi^2)\) | file |
|---|---|---|
| \(a=.5,b=1.5\), full cell | 2.330 | `cap_a05_b15_n9.json` |
| \(a=.45,b=.7\), full cell | 1.916 ± 0.010 (two seeds 1.9165, 1.9157) | `base/base_cap_s{1,2}.json` |
| \(a=.43,b=.6\) | 1.880 ± 0.010 | `base/base_cap_a043_b06_s1.json` |
| \(a=.45,b=.7\), taper 2:4 (CH same: 1.145) | 1.383 | `scan/` |
| \(a=.45,b=.7\), taper 2.5:6 (CH same: 1.014) | 1.410 | `scan/` |
| wider/later bands, e.g. \(a=.5,b=3\) | 6.26 | `scan/` |

The excess over CH is positive in every radial shell. Angular binning (`scripts/step37_excess_angular.py`, `data/step37/angular/excess_angular.json`, \(2^{13}\) points/shell) by \(c_2=(|z_1|^2-|z_2|^2)/r^2\) (\(+1\): divisor directions, \(-1\): normal directions) localizes it:

- near-bolt band \(0.45<r<0.7\): excess \(0.155\), largest in the most normal bin (0.053 of it);
- \(0.7<r<2\): small (0.025);
- tail \(2<r<7.65\): excess \(0.74\), concentrated in intermediate normal-leaning directions \(c_2\in[-0.75,-0.25]\) and nearly zero along \(D'\).

Since the far cap is locally almost CH (\(|W^-|^2=8/(3u^6)\)), a tail excess concentrated away from \(D'\) indicates that most of it is caused by the marking, i.e. by comparing a CH-exponential object with a Fermi-type cap chart, rather than by \(W^-\) itself.

## 3. Response optimization (Fermi chart)

`scripts/step37_cap_response_opt.py` adds 350 compactly supported \(U(1)_-\)-invariant modes: 7 radial \(C^3\) bumps from 0.45 to 6.6, angular functions \(1,c_2,c_2^2,\operatorname{Re}(z_1z_2)/r^2,\operatorname{Im}(z_1z_2)/r^2\), and all 10 symmetric products of the transported orthonormal coframe. L-BFGS used 20 shells × \(2^{10}\) nodes, then was validated on two fresh \(2^{12}\)-per-shell seeds (`data/step37/opt1/`):

| run | base | optimized, validated |
|---|---|---|
| cap, full cell | 1.9152 | 1.8961, 1.8955 |
| cap, taper 2.5:6 | 1.4006 | 1.3828, 1.3825 |
| CH, full cell | 0.995674 | 0.995676, 0.995676 |
| CH, taper 2.5:6 | 1.01428 | 1.00178, 1.00178 |

In-sample and validation values agree, so there is no overfitting. However, the coefficients stayed below \(1.3\times10^{-3}\) after 200 iterations: the modes are badly scaled, because the large-volume outer bumps dominate the gradient. These numbers therefore bound what this optimizer achieved; they do not measure the response infimum. Two facts are nevertheless robust:

1. The certified CH cell shows no descent in this nonsymmetric \(U(1)_-\) space; the in-sample change was \(-4\times10^{-6}\) and validation shows none.
2. With the same modes, about 0.0125 of the CH taper loss is recovered, but the cap's excess of about 0.9 does not move appreciably.

## 4. Cap in its own geodesic normal coordinates

`scripts/step37_cap_expmap_transport.py` pulls the cap back by its exponential map at \(p\in D'\), \(\phi(\xi)=\gamma_\xi(1)\). It uses 64-step RK4 for the geodesic equation, with all derivatives taken by JAX through the discrete flow, and the cap metric is rewritten to be analytic at \(D'\) using series for \(u,q/n^2\). Checks (`data/step37/expmap/smoke.json`):

- Gauss lemma \(g_{\rm exp}\xi=\xi\) to \(10^{-12}\)–\(10^{-5}\) for \(r=.5\)–\(7.6\);
- the same ODE exponential map applied to the Bergman metric reproduces the analytic CH chart to \(3\times10^{-11}\)–\(10^{-5}\);
- \(\det D\phi>0\) at the sampled radii, with no conjugate point;
- relative cap–CH metric difference \(0.03,0.20,0.63,0.17,0.17\) at \(r=.5,1.5,3,5,7.6\), versus a ratio of order 10 in the Fermi chart at large \(r\).

This is the geometrically correct marking for the Strategist's congruence transport.

**Results** (`data/step37/expmap/runs/`, 16 quadratic shells × \(2^9\), compared on identical edges with the CH control `ch_control_expedges_s1.json`, whose value is 0.99562):

| run | \(D/(8\pi^2)\) | total shell excess over CH |
|---|---|---|
| \(a=.45,b=.7\), seed 1 | 1.0522 ± 0.008 | +0.0566 |
| \(a=.45,b=.7\), seed 2 | 1.0632 ± 0.008 | +0.0676 |
| \(a=.43,b=.6\), seed 1 | 1.0571 ± 0.011 | — |
| \(a=.45,b=.7\), taper 2.5:6 | 1.0666 ± 0.008 | (taper loss included) |

Changing the marking from Fermi-type to exponential lowers the cap value from **1.916 to about 1.057**. The Fermi-chart tail excess of 0.74 was almost entirely marking. The remaining excess, about \(+0.06\pm0.01\), separates into two parts:

- **Interpolation band** \(0.48<r<0.70\): \(+0.047\) to \(+0.057\). This is the cost of switching from \(g_{\rm CH}\) to \(g_C\) under \(L\) near the bolt, where \(g_C-g_{\rm CH}\approx-\frac13W^-(\xi,\cdot,\xi,\cdot)=O(0.03)\). It is an artifact of the trial's interpolation; the true cost of re-adapting the core is not known.
- **Intrinsic tail interaction** \(0.7<r<7.65\): \(+0.0100\) (seed 1) and \(+0.0100\) (seed 2), spread smoothly with no interpolation. Here \(G=L g_{\rm exp}L\) and \(g_{\rm exp}\) is exactly Einstein, so this is the response of the unchanged certified deformation to the cap's \(W^-\) geometry. Its sign is **positive**.

Symmetry explains why there is no favorable linear term at the centre. The transported cell is invariant under the standard \(SU(2)\subset U(2)\), which acts on \(\Lambda^-\) as \(SO(3)\). The constant part of \(W^-(p)\) has spin 2 in \(\Lambda^-\), so its first-order pairing with the cell vanishes. Linear pairings with the cell first arise from the \(SU(2)\)-invariant part of the four-jet of \(W^-\) (\(\nabla^4W^-\)) and from terms quadratic in \(W^-\). Neither has a sign that makes the cap favorable here.

**Distance from the divisor** (partial, `data/step37/expmap/runs_n0/`, still running). The cell centre is placed at normal distance \(n_0\) from \(D'\), using an exponential chart with orthonormal frame \(\operatorname{diag}(u^{-1/2},u^{-1/2},1,n_0/\sqrt q)\), which preserves the complex orientation. The band shell \(0.48<r<0.56\) has CH value 0.28147. The cap values are

| \(n_0\) | band shell value | excess |
|---|---|---|
| 0 | 0.3008, 0.3050 | +0.019 to +0.024 |
| 0.5 | 0.2915 | +0.010 |
| 1 | 0.2832 | +0.0017 |
| 2 | 0.28145 | ≈0 |
| 3 | 0.28148 | ≈0 |

The decay is fast, consistent with \(|W^-|\propto u^{-3}\). The tail shells for \(n_0>0\), where the cell's long collar reaches back toward \(D'\), were still being computed when the Step closed. With 64 steps, Gauss-lemma residuals reach \(10^{-3}\) at \(r=7.6\) for \(n_0>0\); increase `--nstep` for final numbers.

## 5. Current understanding

1. The Strategist's congruence transport realizes the full successful CH cell inside an exact Calabi cap with exact outer geometry, unchanged bolt, and exact CH control. Under the correct exponential marking, the cap version of the certified cell costs \(D/(8\pi^2)\approx1.057\). That is about 6% above the CH cell, not the factor 2 seen in Step 36.
2. No tested ingredient gives a cap advantage:
   - band placement;
   - taper;
   - 350 nonsymmetric \(U(1)_-\) response modes, which were badly scaled (Fermi chart);
   - distance from the divisor (band part).
   The only intrinsic piece measured cleanly, the tail interaction of the unchanged deformation with \(W^-\), is \(+0.010\).
3. The Step-36 conclusion that the cap is "intrinsically" much more expensive was a marking effect. Comparisons of cells across environments must use exponential (geodesic normal) charts at the centre. Fermi-type charts produce O(1) spurious costs at the 7.6 collar scale.
4. The certified CH cell showed no descent along 350 compactly supported \(U(1)_-\)-invariant nonsymmetric modes (validated change \(<3\times10^{-6}\)). This is weak evidence of stationarity beyond the diagonal sector, limited by the mode scaling.
5. Orientation reversal identifies CH's \(\omega\) with the cap's \(\bar\omega\). That would place the cell in a Kähler-type positive \(W^+_{\rm eff}=\operatorname{diag}(4/3,-2/3,-2/3)\) environment, analogous to Fubini–Study, which lowered Kähler cells in Step 8. It would also turn the blow-up into a \(\mathbb{CP}^2\) summand relative to the background orientation. This is a different signed-surgery problem with different Seiberg–Witten field supply, and it is not pursued in the current problem.

**Remaining constructive questions.**
- Re-optimize the core in the cap using exponential-chart responses concentrated on \(0.43<r<1.5\), with modes scaled by local volume. The question is whether the +0.05 band loss is mostly removable, and whether the residual is of order \(|W^-|^2\) and positive.
- Finish the \(n_0\) sweep, including the tail. This gives the sign and the decay of the full environment effect.
- Compute the far-regime linear coefficient. Expect it to vanish at leading order by the \(SU(2)\) spin argument above.



---

## Source step38_curvature_conditioned_cap_response.md

Original: [sources/Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md](../sources/Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md)

# Step 38 — Curvature-conditioned response of the transported cell

Conventions: \(\operatorname{Ric}=-g\),
\[
D(g)=\int|\operatorname{Ric}+g|^2,\qquad D/(8\pi^2)
\]
is the reported local cost.  All new values are floating JAX/Sobol calculations, not interval bounds.  The certified CH reference remains
\[
D(g_*)/(8\pi^2)\in[0.995670030344086,0.995670030355131].
\]

## 1. Purpose and representation

Step 37 showed that putting the full certified cell into the Calabi cap by the cap exponential chart reduces the apparent penalty from about \(0.92\) in the Fermi marking to about \(0.06\).  The remaining test had two numerical weaknesses: total-action sampling was noisy compared with the certified saving, and the 350 raw modes were poorly conditioned in a fourth-order objective.

`scripts/step38_expmap_gn_response.py` implements the two requested repairs.

* The base is the Step-37 congruence transport in the cap's geodesic normal chart.
* A response is a sum of compactly supported radial/angular symmetric-coframe tensors, with the nonlinear representation
  \[
  g(c)=B(c)^Tg_0B(c),\qquad B=I+\tfrac12g_0^{-1}h(c).
  \]
  Its first variation at zero is exactly \(h\), since \(B^Tg_0B=g_0+h+\frac14h g_0^{-1}h\). It is positive whenever \(B\) is nonsingular; the sampled minimum eigenvalues are positive but do not prove nonsingularity at every continuum point. The trial used here has support \(0.45<r<0.78\), so it leaves a whole bolt neighbourhood and all bolt jets unchanged.
* At the fitting nodes, the residual is the ten-component Cholesky-frame tensor \(\operatorname{Ric}(g)+g\), weighted so the Euclidean square is the quadrature approximation to \(D/(8\pi^2)\). If \(J\) is the derivative of this complete weighted residual, the singular-value decomposition of \(J\) removes weak directions and the map \(T=V\Sigma^{-1}\) makes \(JT\) orthonormal. Thus optimization uses the discrete Gauss--Newton form of the full moving-frame, moving-volume residual map. At a non-Einstein base this includes derivatives of the frame and volume as well as \(D(\operatorname{Ric}+g)[h]\); it is not the intrinsic frozen-weight Einstein-operator norm. This is nevertheless the directly relevant conditioning for the nonlinear least-squares objective.
* Validation uses paired samples.  On each common point it subtracts the CH cell density including its own volume factor.  More importantly for the response itself it also subtracts the unmodified cap base density.  The resulting differences are much less noisy than either total.

## 2. CH control

The well-sampled CH run is `data/step38/ch_band_gn1_fit32.json`: one radial bump, ten symmetric tensor components, 32 Sobol nodes in each of three fitting shells.  All ten curvature-residual singular directions were retained; their singular values range from \(13.676\) to \(0.0734\).  In whitened units the full linear least-squares direction has norm only
\[
6.60\times10^{-4}.
\]
The nonlinear one-step line test changes the fitted support cost from \(0.68057087199\) to \(0.68057044577\).  Four independent paired validation replicates give a mean partial change
\[
(-5.89\pm9.10)\times10^{-7}
\]
(the uncertainty here is across scrambled replicates).  Therefore this conditioned radial response space sees no material descent of the certified CH cell.  This is a clean statement about these ten modes, not unrestricted stationarity.

## 3. Cap response: what the coarse and refined fits show

The first coarse fit `data/step38/cap_band_gn1_cv.json` used only four nodes per fitting shell. The whitened direction appeared large (norm \(9.36\times10^{-2}\)) and lowered the in-sample support cost by \(0.00992\), but paired validation found it **increased** the response-region action by
\[
+0.00870\pm0.00109.
\]
This is a direct demonstration that curvature-residual whitening repairs coefficient scaling but cannot replace adequate spatial sampling: a high-leverage anisotropic direction can still fit four nodes and fail off-sample. The failure is localized: the two inner validation shells improve by about \(-0.0115\), while the outer shell \(0.597<r<0.78\) rises by roughly \(+0.019\) to \(+0.022\), reversing the net sign. In the JSON the field named `response_improvement` is actually \(D_{\rm opt}-D_{\rm base}\), so positive means worse.

The refined cap calculation `data/step38/cap_band_gn1_fit32.json` uses the same ten-mode family with 32 Sobol fitting nodes per shell and independent paired validation. Its managed task was still running when this note was written, so no result from it is used yet. The scientific comparison to make after terminal delivery is:

1. the whitened linear-response norm versus \(6.60\times10^{-4}\) in CH;
2. the paired response improvement \(D(g_{\rm opt})-D(g_{\rm base})\) on \(0.45<r<0.78\);
3. the remaining paired cap-minus-CH excess in that band;
4. positivity and stability across scrambled replicates.

Even if the refined fixed-bolt response stays positive, it speaks only about the transported certified deformation and this responsive family. It does not determine a cap-cell infimum, exclude cap-adapted bolt area/jets, exclude mixed topology, or imply a background-independent lower principle. The paired cap-minus-CH values here cover only the response band; they cannot be added to the certified total as though they were the full cap correction. Only the paired opt-minus-base integral is complete for the response because the response vanishes outside the band.

## 4. Centre displacement

The Step-37 background task `s37_t34_tool2` is still running. It computes full long-collar cells at normal offsets \(n_0=0,0.5,1,2,3\). Partial shells now extend to \(r\approx2.25\). Their anisotropy decreases as the centre leaves the divisor, but because the cell extends to radius \(7.645\), inward directions can still return to the strong cap region. These data locate useful constructions; they do not isolate a uniform weak-environment expansion in powers of \(|W^-|\). Representative reruns with 128 RK4 steps are still needed if full long-radius values are used quantitatively. The current response calculation uses a 16-step discrete exponential map; JAX differentiates that discrete map exactly, but its marking should be checked against 32/64/128 steps before quantitative interpretation.

## 5. Relation to the paired-field work

Peer messages 805--806 and
`Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md`,
`step43_w0_cotton_quadratic_law_and_debts.md` change the global interpretation.

* On a closed blow-up with the stated basic-class hypotheses, a nowhere-zero self-dual harmonic form cannot have zero exceptional period.  The local perpendicular cell is consistent because its canonical closed self-dual form degenerates at the bolt.  The transported-cell calculation therefore does **not** realize the excluded closed symplectic common mode.
* The cap and CH have the same \(R^+\) seen by the first Burns response.  No existing flux, monopole, or transgression identity fixes the sign of the \(SU(2)\)-invariant \(O(|W^-|^2)\) environment term.  The Step-37 positive \(+0.010\) tail is construction evidence for one unchanged deformation and marking, not an intrinsic cap tariff.
* The corrected model tensor is \(W_0=(\rho^2/4)(I/3-nn)\), and for closed almost-Kähler first jets
  \[
  |\delta W_0|^2=\tfrac13|d(\rho^2/4)|^2+\tfrac{\rho^4}{32}|\nabla n|^2.
  \]
  The missing global estimate is differential: Cotton supplies \(\nabla\operatorname{Ric}^\circ\), not a quantity controlled linearly by \(P=\int|\operatorname{Ric}^\circ|^2\).  A completed integration-by-parts route naturally gives a conditional quadratic scale \(P\gtrsim R^2/A\), unless additional perturbative spectral structure is available.

These results separate the two most informative next directions.  On the construction side, vary bolt area or a small number of bolt-compatible jets if the refined fixed-bolt band remains expensive; shell modes supported outside \(r=.45\) cannot test that freedom.  On the global side, pursue either a cover-uniform perturbative Armstrong estimate near the KE host or a closed approximate common mode that records exceptional areas/zero sets, amplitude, \(W^+-W_0\), Nijenhuis energy, and the AK\(\Gamma\) defect.  A zero-period nowhere-vanishing almost-Kähler model is topologically unavailable.

