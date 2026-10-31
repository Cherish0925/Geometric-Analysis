# Step 9 consolidated research status (historical; corrected by Step 10)

The Taub–NUT–AdS assessment in sections 3, 10, and the final error-log line is superseded by `step10_multiscale_cover_and_diffuse_pontryagin.tex`. In particular, all-radius curvature means are not bounded once balls reach the NUT, and a smaller buffered domain chosen before taking its cover does unwrap the short circle.

## New results this step

### 1. Weitzenböck gradient energy (verified)
Using Besse's Theorem 1.155 (Convention B: q(R)(ω)_{ij} = Ric_{ik}ω_{kj} + Ric_{jk}ω_{ik} - 2R_{ikjl}ω_{kl}),
the gradient energy of harmonic SD 2-forms on a 4D Einstein metric with Ric = -g is:

| Eigenform | W⁺ eigenvalue | R̃ eigenvalue μ | ∫|∇H|²/∫|H|² |
|-----------|--------------|----------------|----------------|
| σ₁ (simple) | -1/6 | -1/2 | **1** |
| σ₂ (double) | 1/12 | -1/4 | **3/2** |
| σ₃ (double) | 1/12 | -1/4 | **3/2** |

All forms have POSITIVE gradient energy. Forms are NOT nearly parallel.
This is consistent with the Strategist's claimed formula.
Verified against KE model (parallel Kähler form gives q(R)=0 ✓) and K3 (parallel ✓).

Script: `workspace/scripts/verify_weitzenbock_clean.py`

### 2. Maximal-function dual selection (new framework)
On the fixed critical Ishida-LeBrun manifold with δ_i → 0:
- Hardy-Littlewood maximal inequality (uses only doubling from Ric ≥ -3g)
- Good set G_i = {M₁|Rm|² ≤ K₀} ∩ {M₁ F ≤ ε_i→0} has Vol ≥ V_∞/2
- Normal-cover mean transport preserves both bounds
- This is strictly stronger than having small deficit at one radius

Note: `workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex`

### 3. Taub–NUT–AdS only refutes a fixed oversized-cover inference
The family has bounded curvature means on annular balls not reaching the NUT and remains collapsed in the cover of a larger domain containing the NUT. It does not have bounded means on all radii through the core. A smaller fixed buffered domain avoiding the NUT unwraps the circle, and its lifted limit is hyperbolic with calibrated deficit 16. Exact correction and replacement scripts are in Step 10.

### 4. Form-based rank analysis (from TTCS)
- Flat rank ≥ 2: EXCLUDED by definite-pair mechanism (closedness + constant amplitude → parallel → contradicts gradient energy)
- Flat rank 3: EXCLUDED by definite-triple (requires locally nondegenerate Gram)
- Rank 1: NOT excluded (single form reduces to weighted harmonic 1-form on 3D base)
- Nil-twisted: NOT excluded (Heisenberg structure can produce constant-length SD forms with O(1) gradient)
- Three forms with local Gram nondegeneracy: WOULD exclude, but Walsh estimates give only L¹ orthogonality

### 5. Pontryagin localization mechanism
p₁(Λ²₊) = 2χ + 3τ ≠ 0 on critical manifolds.
On basic-form collapse regions (SD forms pulled from base), p₁ vanishes (base dim ≤ 3).
So nonzero p₁ must localize on: non-basic regions, nil/bundle twist, singular fibers, or 4D cores.

## What is established (cumulative)

1. Quantifier/scaling reduction: Q_n ⟺ P_n⁺ ∨ P_n⁻
2. Low dimensions: n=2 (uniformization), n=3 (Hamilton)
3. 4D near-saturation energy/period profile for critical Ishida-LeBrun
4. Weyl profile L² concentration: ∫(|W⁺|-1/(2√6))² = O(Aδ²)
5. Projector obstruction: calibrated W⁺ spectrum impossible on Einstein local limit
6. Non-collapsed regular patches excluded (→ everywhere collapsed at unit scale)
7. Normal-cover mean transport lemma (sheet-number-free)
8. Maximal-function dual selection of curvature + deficit good points
9. Orbit-volume equations for exact symmetric models (abelian circle excluded, nil³ circle excluded, interval cusps exist)
10. A fixed oversized cover can remain collapsed because its domain contains a contraction core; adjustable-buffer calibrated accessibility remains open (Step 10 correction)
11. Weitzenböck gradient energy: forms are NOT nearly parallel (coefficient 1 and 3/2)
12. Form-based rank analysis: flat rank ≥ 2 excluded, rank 1 and nil not excluded

## What remains open

1. **The closed-manifold NUT problem**: Can the collapsing on a closed critical Ishida-LeBrun manifold be entirely composed of NUT-type contractible fibers, cusps, and singular strata? Global topology constraints may prevent this.

2. **Pontryagin energy budget**: Does the p₁ localization + ∫|Rm|² budget force a positive volume of accessible (non-NUT) collapse?

3. **Local Gram nondegeneracy**: Can the monopole near-saturation structure be used to prove local nondegeneracy of the Gram matrix of near-harmonic forms?

4. **Positive branch**: Noncollapsed finiteness (S0910A02) is conditional on uniform noncollapse, which is the single remaining gap.

5. **Higher dimensions and Lean formalization**: Not started.

## Error log
- Retracted: pure W⁺ lower bound (Step 2-3)
- Retracted: "all known no-Einstein families have uniform gap" (Step 3)
- Retracted: cover degree drop in deficit transport (Step 7-8)
- Retracted: capacity inequality (Step 7)
- Retracted: "complete regular collapse exclusion" (Step 7-8)
- A01 nil³ sign error corrected: v''=(3-μ)v not (3+μ)v (Step 7)
- **Step 10 correction**: Taub–NUT–AdS does not satisfy the selected all-radius curvature-mean input and does not obstruct a smaller cover chosen before including the NUT.
