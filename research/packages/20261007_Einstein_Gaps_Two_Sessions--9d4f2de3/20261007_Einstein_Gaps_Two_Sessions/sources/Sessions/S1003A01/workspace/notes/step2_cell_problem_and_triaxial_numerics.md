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
