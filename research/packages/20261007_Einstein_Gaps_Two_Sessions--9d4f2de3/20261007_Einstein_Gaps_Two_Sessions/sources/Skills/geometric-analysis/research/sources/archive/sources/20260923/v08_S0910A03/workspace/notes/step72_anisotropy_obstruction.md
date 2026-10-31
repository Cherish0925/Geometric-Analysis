# Supersession notice (Step 73)

The exact drift-Laplacian and finite-cylinder rigidity below remain valid, but the conclusions that the approximate diagonal `T^2` graph-neck route is blocked, that the mismatch cannot be absorbed by small forcing, and that available forcing is `O(delta log(1/delta))` are withdrawn. For approximate metrics,

\[
\operatorname{div}(e^\sigma\nabla d)=-e^{\sigma+2\phi}(E_x-E_y),
\]

and no geometry-uniform inverse estimate or upper length bound had been proved. `workspace/notes/step73_tail_completion_and_core_entry.md` gives an explicit full-Ricci tail that erases order-one anisotropy with defect `O(K^{-1}+K^{-2}+e^{-2r_0})`, plus a verified adiabatic tail lemma. The remaining issue is entry from a reflection core into a large near-umbilic expanding slice. The ansatz here is diagonal and orthogonally transitive, not every `T^2`-invariant metric.

# Step 72: T²-invariant graph-neck structural obstruction

Session: S0910A03. Agent2/Constructor, Execute.

## Summary of results

This step establishes a structural obstruction to the T²-invariant 
graph-manifold construction for Yau Problem 26 (negative branch).

**Theorem (Anisotropy Amplification).** In the conformal gauge 
g = e^{2φ}(dt²+dz²) + e^{2b}dx² + e^{2c}dy², the orbit anisotropy
δ = b−c satisfies the drift-Laplacian equation Δδ + ∇σ·∇δ = 0 (where
σ = b+c). Near the cusp boundary, the Frobenius analysis shows that
z-oscillation modes are AMPLIFIED:

| Mode n | Center amplitude | Cusp amplitude | Amplification |
|--------|-----------------|----------------|---------------|
| 0 | 1.000 | 1.000 | ×1.000 (exact) |
| 1 | 1.000 | 1.175 | ×1.175 (+17.5%) |
| 2 | 1.000 | 1.813 | ×1.813 (+81.3%) |
| 3 | 1.000 | 3.339 | ×3.339 (+234%) |

**Corollary 1 (Rigidity).** If δ(R,z) = const on the outer boundary
of an exact Einstein half-core, then δ ≡ const everywhere (TTCS verified).

**Corollary 2 (Yamabe obstruction).** On flat T³, the equation 
Δu = (3/4)u⁵ (Yamabe for R=−6) has no positive smooth solution 
(maximum principle: Δu ≤ 0 at max(u) contradicts (3/4)u⁵ > 0).
Therefore there is no R=−6 metric in the flat conformal class on T³.

**Corollary 3 (Structural chain).** Every T²-invariant Koiso center 
on T³ with R_h = −6 must use a non-flat starting metric h₀ = dθ² + 
e^{2f(θ)}dx² + e^{-2f(θ)}dy² with f nonconstant. This gives orbit 
anisotropy d₀(θ) = 2f(θ), which is z-dependent. The drift-Laplacian 
amplifies this oscillation at the cusp boundary. Since hyperbolic cusps 
have constant T² cross-section (flat T³), the oscillation prevents 
matching.

## Detailed derivations

### 1. Conformal gauge ellipticity

The principal symbol of the 3-equation system (E_{tt}+E_{zz}, E_{xx}, 
E_{yy}) in unknowns (φ, b, c) is:

$$
M = \begin{pmatrix} 2k^2 & k^2 & k^2 \\ 0 & k^2 & 0 \\ 0 & 0 & k^2 
\end{pmatrix}, \quad k^2 = \tau^2+\xi^2
$$

det M = 2k⁶ ≠ 0 for k ≠ 0. **Genuinely elliptic.** Verified by SymPy.

This contrasts with the Gaussian gauge, where the lapse function a has 
no θ-diffusion (degenerate principal symbol), explaining why A01's and 
our earlier BVP experiments produced large E_{00}/E_{01} residuals.

### 2. Drift-Laplacian for anisotropy

From E_{xx}/g_{xx} = 3 − e^{−2φ}(b_{tt}+b_{zz}+b_t²+b_tc_t+b_z²+b_zc_z) 
and E_{yy}/g_{yy} similarly:

Subtracting: Δδ + σ_t δ_t + σ_z δ_z = 0, equivalently 
div(e^σ ∇δ) = 0.

**Maximum principle**: On [0,R]×S¹ with δ_t(0,z) = 0 (reflection),
the strong maximum principle + Hopf lemma forces either δ ≡ const or
osc(δ|_{t=R}) > osc(δ|_{t=0}). (TTCS independently verified.)

### 3. Orbit-area subharmonicity (CORRECTED)

From E_{xx}+E_{yy} = 0: Δσ + |∇σ|² = 6e^{2φ}.

Setting ρ = e^σ: **Δρ = 6e^{2φ}ρ > 0 always** (strict subharmonicity).

NOTE: My original claim included a −|∇δ|² term. This was WRONG.
The correct identity has no such term (TTCS correction).

### 4. Frobenius asymptotics at cusp

In conformal gauge, the cusp corresponds to t → 1⁻ with 
σ'(t) = 2/(1−t) → ∞. The n-th Fourier mode of δ satisfies:

a_n'' + [2/(1−t)]a_n' − n²a_n = 0

Setting τ = 1−t: Frobenius indices at τ=0 are p=0 and p=3.
Both solutions are finite. The physical solution (Neumann at t=0)
approaches a nonzero constant C₁(n) at the cusp.

Numerical verification shows C₁(n)/a_n(0) > 1 for all n ≥ 1,
with amplification increasing with n.

### 5. Yamabe on flat T³

The equation −8Δψ = −6ψ⁵ on flat T³ reduces to ψ'' = (3/4)ψ⁵.
At the maximum of ψ: Δψ ≤ 0 contradicts (3/4)ψ⁵ > 0.
No positive smooth solution exists.

Therefore no R=−6 metric lies in the flat conformal class on T³.
Every T²-invariant R=−6 metric requires a non-flat starting metric,
forcing nonconstant orbit anisotropy d = 2f(θ).

### 6. Isotropic impossibility (algebraic)

For isotropic g = dt² + f(t)²h on T³ (3D fiber):
- Normal Einstein: s' + s² = 1  (s = f'/f)
- Tangential Einstein: s' + 3s² = 3
- Subtract: 2s² = 2 → s = ±1, s' = 0
- Reflection center s(0) = 0: CONTRADICTION.

This is independent of the fiber metric h. Only s ≡ 1 (cusp) or 
s ≡ −1 (anti-cusp) solve both equations.

## Consequences for the graph construction

### What is blocked

The T²-invariant reflected half-core construction for graph manifolds
is blocked by the following chain:

1. R_h = −6 forced by Koiso center conditions
2. R = −6 on T³ requires negative-Yamabe conformal class
3. Negative Yamabe requires nonconstant f(θ) → nonconstant d(θ)
4. Drift-Laplacian amplifies d(θ) oscillation at cusp boundary
5. Flat cusp has constant d → oscillation mismatch is O(1)
6. Approximate forcing O(δ·log(1/δ)) → 0, too weak to absorb O(1)

### What is NOT blocked

- **General 4D construction without T² symmetry**: the drift-Laplacian
  argument is specific to T²-invariant metrics.
- **Non-reflected cores**: cores without totally geodesic center avoid
  the R_h = −6 constraint but lose reflection symmetry.
- **Higher-dimensional analogs**: the obstruction chain is specific to
  3D torus fibers and may differ for higher-dimensional fibers.
- **The positive branch**: entirely different geometry.

### Implications for Yau 26

The T²-invariant graph manifold approach was the most developed
counterexample candidate. Its obstruction strengthens the case for a 
positive answer in dimension 4 (gap theorem), but does not prove it.
The remaining viable negative-branch approaches are:
1. Full 4D Einstein PDE without symmetry reduction
2. Alternative topological constructions (surface bundles, etc.)
3. Higher dimensions (n ≥ 5) where the fiber is ≥ 4-dimensional

## Files

- `workspace/scripts/step72_conformal_gauge_einstein.py` → 
  `data/step72_conformal_gauge_system.json` (SymPy computation)
- `workspace/scripts/step72_structural_analysis.py` → 
  `data/step72_structural_analysis.json` (design constraints)
- `workspace/scripts/step72_frobenius_modes.py` → 
  `data/step72_frobenius_analysis.json` (mode amplification)
- `trace/ttcs/results/step72_ttcs01_verifier1_integration.md` 
  (independent verification)
