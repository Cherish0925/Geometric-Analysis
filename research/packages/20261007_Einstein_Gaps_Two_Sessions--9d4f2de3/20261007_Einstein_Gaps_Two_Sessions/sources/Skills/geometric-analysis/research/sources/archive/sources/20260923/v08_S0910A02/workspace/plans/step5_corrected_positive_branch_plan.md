> **STEP 6 ADDENDUM / PARTIAL SUPERSESSION.** The fixed-connection O'Neill catalogue and the proposed S^4 volume target in this plan are partially obsolete. See `Sessions/S0910A02/workspace/notes/step6_positive_collapse_regularity_probes.md`. The pinching-compatible circle-collapse scaling is Kaluza--Klein with `phi=tF=O(1)`, not fixed connection curvature, and smooth free S^1 collapse in dimension 4 is Bochner/Euler obstructed for small δ. The correct S^4 Ric=g comparison volume is `24π²≈236.87`, not the unit-radius `8π²/3≈26.32`; a cheap rotational ansatz search only found the near-constant-curvature rescaling endpoint, not volume collapse. The remaining positive-collapse issue is singular/orbifold/fixed-stratum compatibility plus approximate-pinching regularity, not global collapse impossibility.

# Step 5 Research Plan: Corrected Positive-Branch Program and Strategy Portfolio

Session: S0910A02. Agent2/Constructor. Phase: Explore.

## Status after corrections

The positive-branch program (step5_positive_branch_all_dimensions.md + erratum)
established:

**Valid:**
- Precompactness (Theorem 1): diam, Vol upper bounds, b₁ = 0, π₁ finite (all n)
- Low dimensions: P₂⁺ (uniformization), P₃⁺ (Hamilton)
- 4D CGB accounting (Theorem 3): β(δ)Vol + ∫|W|² ≤ 8π²χ
- 4D topological filter: PSC excludes SW no-Einstein from positive branch
- Lean scoping: Mathlib lacks Ricci/Einstein; formalization is multi-year

**Retracted → corrected:**
- Theorem 2 → Theorem 2': needs |Rm| ≤ K, giving ε(n,v,K)
- Gap: TWO open gaps, not one: (II) curvature concentration, (III) collapse

## The three regimes and their strategies

### Regime (I): Noncollapsed + bounded curvature — SOLVED

Theorem 2' with ε(n,v,K). The proof chain:
|Rm| ≤ K → Cheeger inj bound → harmonic radius → C^{1,α} convergence →
Einstein limit → smooth → diffeomorphism → Einstein on M.

### Regime (II): Noncollapsed + curvature concentration — OPEN

**What happens:** Weyl concentrates at points (dim 4: isolated orbifold
singularities by Cheeger-Naber). Limit = Einstein orbifold + ALE bubbles.
M_i may not be diffeomorphic to any smooth Einstein manifold.

**Strategy A: Obstruction-amplitude principle.**
If tight Ric pinching forces vanishing of all gluing obstruction
coefficients at each bubble, then desingularization succeeds and the
orbifold limit can be smoothed to an Einstein metric on M_i.

Source: Step 1 showed that non-zero Calabi first obstruction stays
order 1 in g_t-operator norm. If this extends to ALL obstruction
orders, then:
- δ → 0 forces first obstruction → 0
- Integrable deformation → exact Einstein on smooth topology
This is a conditional but highly testable approach.

**Strategy B: Energy quantization + topological accounting.**
In dim 4, Ricci-flat ALE bubbles carry the orbifold Gauss--Bonnet defect
\[
  \frac{1}{8\pi^2}\int |Rm|^2=\chi(X)-\frac1{|\Gamma|}.
\]
Thus the Eguchi--Hanson bubble has energy \(12\pi^2\), not \(8\pi^2\).
Bubble counting should use this defect for the actual ALE model rather than
a universal per-bubble constant; the total energy is constrained by the
4D CGB budget. The topology of \(M_i\) is recovered from the orbifold base
by replacing singular points with smooth ALE caps. If the resulting topology
always carries Einstein metrics, or if obstruction-amplitude vanishing forces
Einstein gluing on that topology, regime (II) is resolved.

**Strategy C: Spectral/variational approach.**
Use the gauged Einstein operator D Φ near the almost-Einstein input.
If the kernel is controlled and the Kuranishi obstruction map can be
solved, exact Einstein follows from the inverse function theorem.
Need: uniform bounds on the kernel dimension and cokernel, plus
a degree/sign argument for the obstruction map.

### Regime (III): Collapsed — OPEN

**What happens:** Vol → 0, diam ≤ D(n). GH limit is lower-dimensional.
Without sectional bounds, CFG theory doesn't apply.

**Strategy D: Rewound noncollapse (TTCS top recommendation).**
Prove: simply connected + Ric ≈ +g prevents collapse.
If true: all collapse = M̃/Γ with M̃ noncollapsed.
Then equivariant Einstein construction on M̃ → descent to M.

Test case: can S⁴ have metrics with Ric ≈ g and Vol → 0?
CGB alone doesn't prevent this. Need:
- Bochner + spectral arguments on simply connected manifolds
- Perhaps: Ric ≈ g + simply connected → strong sectional pinching?
  (This would be a sphere-theorem-type result)

**Strategy E: O'Neill obstruction to genuine fiber shrinking.**
For fibered collapse F → M → B: O'Neill curvature formula gives
vertical Ric = O(t²) while horizontal Ric is order 1, forcing
δ_+ → 1 unless the algebraic Einstein balance conditions hold.
Combined with: fibered collapse under bounded Ricci automatically
produces approximate submersion data.

Test: compute exact δ_+ minimization for Hopf fibrations, principal
T^k-bundles, and Berger-type metrics as a function of fiber scale.

**Strategy F: Ricci flow smoothing.**
Normalized Ricci flow starting from Ric ≈ g might smooth curvature
concentrations and prevent collapse simultaneously:
- The traceless Ricci S is small initially
- If flow converges → Einstein
- If flow develops singularity → rescaled limit has S = 0 → Ricci-flat
  or Einstein, contradicting?

Problem: Weyl*S coupling may amplify small S before diffusion.
Need: pseudolocal estimates depending on Ricci defect.

## Prioritized next actions

1. **Concrete test: simply connected collapse under Ric ≈ g.**
   Construct or prove impossibility of metrics on S⁴ with δ_+ ≤ 0.1
   and Vol(S⁴) ≤ 10. This is a concrete computation/construction task.

2. **O'Neill δ_+ computation for canonical bundles.**
   Compute exact δ_+ as function of fiber scale for:
   - Berger spheres (already done; δ_+ → 1 for fiber shrinkage)
   - Principal S¹-bundles over CP^{n-1} with varying connection
   - Torus bundles over surfaces
   This tests whether all fibered collapse forces δ_+ ≥ c_n.

3. **Obstruction-amplitude in dim 4 orbifold desingularization.**
   Source-check: does tight Ric pinching (operator norm) force first
   obstruction to zero in Ozuch's framework? What about higher orders?

4. **Rewound noncollapse: theoretical investigation.**
   Under what conditions on M^n, g with Ric ≈ g:
   - Can π_1-covering volumes be bounded below?
   - Does b₁(M̃) = 0 prevent torus-fibered collapse upstairs?
   - Is simply connected positive near-Einstein enough for Rm control?

5. **4D topological accounting for regime (II).**
   When orbifold limit has k isolated singularities with ALE bubbles:
   - Number of bubbles ≤ χ - 1
   - Base orbifold topology constraints
   - Does every resulting smooth topology carry Einstein metrics?

## Coordination with session group

- **A02 (this session):** Positive branch existence, regime (II) and (III),
  all-dimensional strategies, Lean scoping
- **A01:** Negative boundary near-equality, boundary data matching,
  curvature ratio analysis, SW-based tools
- **A03:** Weyl profile, phase separation, cap matching, boundary
  structures, collapse models

## Files

- Main note: `step5_positive_branch_all_dimensions.md` (with erratum header)
- Erratum: `step5_erratum_theorem2_correction.md`
- Constants script: `workspace/scripts/step5_positive_branch_constants.py`
- Data: `workspace/data/step5_positive_branch_constants.txt`
- TTCS results: `trace/ttcs/results/step5_ttcs01_*`
