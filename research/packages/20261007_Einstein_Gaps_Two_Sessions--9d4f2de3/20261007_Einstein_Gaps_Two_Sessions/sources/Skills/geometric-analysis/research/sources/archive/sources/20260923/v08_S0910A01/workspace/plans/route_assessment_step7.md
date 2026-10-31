# Yau Problem 26: Route Assessment After Step 7

## Key Advance: Noncollapsed Exclusion for Negative Branch

### What was established
A 9-step argument excluding noncollapsed smooth regions in any hypothetical
near-boundary LeBrun sequence (δ → 0, k/A → 1/3):

1. Near-equality D_a/A → 0
2. Cauchy-Schwarz remainder → s → -4, |W⁺| → 1/(2√6) in A-normalized L²
3. Tensor slack ∫ξ(Q+P) ≤ 24π²D_a where ξ = w + √(2/3)|W⁺| ≥ 0
4. Volume-random basepoint: typical balls have vanishing ξ
5. Cheeger-Naber Thm 1.13: measure-theoretic harmonic radius control
6. W²,p convergence on harmonic charts → smooth Einstein limit
7. Pointwise passage: |W⁺| = 1/(2√6) constant, ξ = 0 on limit
8. Derdziński: two-eigenvalue W⁺ + constant |W⁺| + Einstein → Kähler
   (conformal factor |w|^{1/3} = const)
9. Kähler + Ric = -g → |W⁺|² = 2/3 ≠ 1/24. CONTRADICTION.

### What remains
The sequence must be entirely collapsed: Vol(B₁(p)) → 0 for all p.

**Collapse constraints under Ric ≈ -g in dim 4:**
- Total volume Vol(M) ≥ cA from CGB → large-volume, thin-fiber geometry
- No diameter upper bound (no Myers for negative pinching)
- Product surface collapse (Σ_g × Σ_{g'}) has |W⁺| = 2/√6 → excluded by Weyl filter
- Free S¹ collapse has χ = 0 but tight negative pinching gives χ > 0 (4D CGB)
- All currently known collapse models under Ric = -g are excluded

**Open question:** Are there unknown collapse modes under Ric ≈ -g with
calibrated Weyl profile |W⁺| ≈ 1/(2√6)?

### What needs primary-source verification
- Derdziński 1983 (Compositio 49): the conformal factor formula g_K = C|w|^{2/3}g
- This is the linchpin of step 8; if the factor is not |w|^{1/3}, the local
  argument fails and the route reverts to the global Armstrong mechanism

## Updated Route Comparison

### Negative branch (four-dimensional)
**Status:** Noncollapsed case resolved (conditionally on Derdziński factor).
Collapsed case open but strongly constrained by Weyl profile + Euler filters.

**Next work:**
1. Verify the Derdziński conformal factor from primary source
2. Classify possible collapse geometries under Ric ≈ -g with calibrated W⁺
3. Use Naber-Zhang collapsed regularity on local covers
4. Develop Euler characteristic constraint: χ(M) = A-k → χ ≈ 2A/3 → incompatible
   with known collapsed topology?

### Positive branch (all dimensions)
**Status:** S0910A02 has the precompactness theorem (all n) and the Bochner
obstruction for constant-fiber S¹ collapse (4D). Noncollapsed case needs |Rm| ≤ K
for convergence. Two open gaps: curvature concentration and general collapse.

**Next work (S0910A02):**
1. Rewound noncollapse: prove simply connected manifolds don't collapse under Ric ≈ +g
2. Orbifold desingularization for curvature concentration
3. Extend free-circle χ obstruction to general collapse models

### Cross-branch
Either sign branch suffices for the original proposition Q_n. The negative branch
has deeper structure (Seiberg-Witten + Weyl profile) but faces the harder collapse
question. The positive branch has better compactness (Myers) but the same collapse
difficulty. Independent resolution of either completes the four-dimensional case.

### Lean formalization
Mathlib lacks Ricci tensor and curvature (S0910A02 scoping). Full formalization
requires building the differential geometry stack from scratch. This is a separate
long-term project.

## Priority for next step
1. PRIMARY-SOURCE VERIFICATION of Derdziński conformal factor (critical)
2. Collapse classification under calibrated Weyl profile (main mathematical work)
3. Euler characteristic constraint for collapse modes
