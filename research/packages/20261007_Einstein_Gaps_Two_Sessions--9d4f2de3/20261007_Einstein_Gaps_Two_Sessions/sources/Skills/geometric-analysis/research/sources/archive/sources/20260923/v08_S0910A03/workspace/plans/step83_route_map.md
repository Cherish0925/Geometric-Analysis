# Step 83 route map: corrected K-production and structural reduction

> **SUPERSEDED by Step 85.** The Bochner route assessment here is wrong. Step 85's corrected Bochner comparison gives a complete exact obstruction. See `workspace/notes/step85_bochner_comparison_theorem.md`.

## Current position: a genuine mathematical fork

### What is established

**Structural reduction (A02 #599)**:
- For n ≥ 3, Yau-26 false in dimension n ONLY IF a closed n-manifold without any Einstein metric exists in that dimension.
- For n ≥ 5: no such manifold is currently certified; refutation impossible with existing knowledge.
- For n = 4: extended graph manifolds (Di Cerbo) provide no-Einstein examples; refutation is a live possibility.
- The L² variational route is closed: inf ∫|E|² = 0 on near-pinched families.
- The C⁰ operator norm is the unique sharp norm for any obstruction.

**Negative branch (graph-manifold connector)**:
- All-Einstein exclusion on extended graph manifolds ✓
- Explicit expanding tail with vanishing defect ✓
- Universal center contraction ⟨u'(0)⟩_ρ = -3, K''(0) ≥ 72 ✓
- VII₀ collapse barrier for fixed-helical subclass ✓
- Full OT K-production framework with corrected sign structure ✓
- **TTCS generator: no known monotone functional excludes the K-drop in the full OT system**
- **Bakry-Émery Ric^σ_B has universal -1 eigenvalue in r-direction; Bochner fails**
- **Connector problem is genuinely open**: neither construction nor obstruction achieved

**Positive branch (A01 #598)**:
- K-symmetry cross-parity elimination and K-odd spectral positivity
- Reduction to off-diagonal odd-odd Green kernel at distinct nodes
- Sign of this kernel not yet determined

### The core mathematical fork

The graph-manifold connector problem is:

*Given a reflected scalar-minus-six T²-invariant center, can the exact Einstein evolution (or a small-defect approximation) reach a slice compatible with the expanding tail (K ≤ 6+O(δ))?*

Our analysis shows:
- The K-production equation K'+2xK = Φ has only ONE proven-positive contribution (the IBP orbit-velocity term).
- All other terms (covariance, tension, circle geometry) are indefinite.
- No monotone quantity, Lyapunov function, Bochner estimate, or finite-moment closure excludes the K-drop.
- The exact Koiso germ exists locally; the question is global continuation.
- The difficulty is the same as A02's "Burns core tension": tight pinching and Einstein obstruction resist coexistence.

### Highest-value next work

1. **Full non-diagonal OT numerical evolution**: Solve the exact reflected Einstein system from constant-speed-loop centers using method-of-lines (FFT in z, RK4 in r). Track all K-production terms. This would either reveal a K-drop mechanism or quantify the failure mode.

2. **Positive-branch Green kernel sign**: A01's K-symmetry reduces to a specific finite smooth quantity. Independent numerical/analytical evaluation of this kernel would advance the positive branch. (A01's domain.)

3. **Alternative 4D approaches**: Consider whether the Ricci flow or other analytic continuation methods can bridge the graph-manifold connector, bypassing the direct Koiso evolution.

4. **Higher-dimensional prerequisite**: For n ≥ 5, the question reduces to finding a closed manifold without any Einstein metric. Literature search for this fundamental question would clarify whether all-dimensional Yau-26 is currently accessible.

### Scope relative to Yau 26

Even a complete resolution of the 4D graph-manifold connector would only settle one branch of the 4D problem. The full Yau-26 requires:
- Dimension 4: both positive and negative branches
- Dimension ≥ 5: the no-Einstein manifold prerequisite

## Reproducible files

- `workspace/notes/step83_corrected_K_production_and_bakry_emery.md`
- `workspace/scripts/step83_integrating_factor_analysis.py`
- `workspace/scripts/step83_corrected_budget_and_bakry_emery.py`
- `workspace/data/step83_integrating_factor.json`
- `workspace/data/step83_corrected_budget.json`
- `trace/ttcs/results/step83_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step83_ttcs01_generator1_integration.md`
