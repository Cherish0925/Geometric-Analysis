# Step 3: Mixed SW Bound Analysis — A Structural Advance for Yau 26

## Executive Summary

The mixed Seiberg-Witten curvature estimate (Proposition 4, Ishida-LeBrun) yields a 
**dimension-uniform** lower bound on Ricci deviation δ for LeBrun-type no-Einstein 
manifolds, depending only on the ratio k/A = k/c₁²(X), **not on A separately**. This 
eliminates the Step 2 counterexample route (varying manifolds with A→∞ at fixed k/A) 
and confines any surviving negative-branch counterexample to the Einstein-existence 
boundary k/A → 1/3.

## 1. The Mixed SW Estimate

**Proposition 4 (LeBrun, "Weyl curvature, Einstein metrics, and SW theory").**
For any compact oriented 4-manifold M with b₊ ≥ 2 and monopole class a:

$$\frac{1}{4\pi^2}\int_M\left(\frac{s^2}{24} + 2|W_+|^2\right)d\mu \geq \frac{2}{3}(a^+)^2$$

where a⁺ is the self-dual Hodge projection of a.

**Key optimization (Ishida-LeBrun sign trick):** For M = X#k CP̄² with basic classes
a = c₁(X) + Σ εⱼ Eⱼ, choose signs ε̂ⱼ so that ε̂ⱼ · c₁(X)⁺ ≥ 0. Then:

$$(a^+)^2 = (c_1(X)^+ + \sum \hat{E}_j^+)^2 \geq (c_1(X)^+)^2 \geq c_1^2(X) = A$$

This is stronger than the topological square a² = A - k because (a⁻)² ≤ 0.

**Comparison with scalar-only bound:**
- Scalar-only: (1/4π²)∫(s²/24)dμ ≥ A/3 → no Einstein for k > 2A/3
- Mixed: (1/4π²)∫(s²/24 + 2|W₊|²)dμ ≥ 2A/3 → no Einstein for k > A/3

The improvement factor of 2 comes from including |W₊|².

## 2. The Uniform δ Lower Bound

**Setup:** M = X#k CP̄², A = c₁²(X), metric g with δ₋(g) = δ (Ric eigenvalues
in (-(1+δ), -(1+δ))).

**Derivation:** Combining the mixed SW bound with CGB:

(i) (1/4π²)∫(|r̊|²/2)dμ ≥ 2A/3 - (A-k) = k - A/3

(ii) Pointwise: |r̊|² ≤ |Ric - σg|² = |E|² ≤ 4δ² (n=4)

(iii) Volume upper bound from CGB: V ≤ 4π²(A-k)/(2(1-δ)²/3 - 2δ²)

Combining (i)+(ii): V ≥ 2π²(k-A/3)/δ²

With (iii): q'(2(1-δ)²/3 - 2δ²) ≤ 2Bδ² where q' = k-A/3, B = A-k

Since B + q' = 2A/3: q'·2(1-δ)² ≤ 4Aδ²

**Result:**
$$\frac{\delta}{1-\delta} \geq \sqrt{\frac{k/A - 1/3}{2}} \qquad (k/A > 1/3)$$

This depends ONLY on p = k/A. Symbolically verified: the boundary is tight.

## 3. Numerical Values

| p = k/A | δ lower bound | Comment |
|---------|--------------|---------|
| 1/3 + 0.001 | 0.022 | Boundary region |
| 1/3 + 0.01 | 0.066 | Near boundary |
| 0.4 | 0.154 | New no-Einstein range |
| 0.5 | 0.224 | Middle range |
| 0.6 | 0.267 | Approaching old boundary |
| 2/3 | 0.290 = 1/(√6+1) | Old no-Einstein threshold |
| 0.8 | 0.326 | Well above old threshold |
| 0.9 | 0.347 | Near maximum blow-up |

The bound at p = 2/3 is 1/(√6+1) = (√6-1)/5 ≈ 0.290, confirming the Strategist's prediction.

## 4. What This Destroys

**The Step 2 varying-manifold route is killed.** The old analysis gave δ ∼ 1/√A → 0
for varying LeBrun manifolds with fixed k/A > 2/3 and A → ∞. The new bound shows
δ ≥ 1/(√6+1) > 0 for ALL such manifolds, regardless of A.

More generally: for ANY fixed ratio p = k/A > 1/3, the δ lower bound is a positive
constant depending only on p.

## 5. What Survives

**Only the boundary route k/A → 1/3 from above** allows δ → 0.

At k/A = 1/3 exactly: the mixed bound becomes an equality for ASD Einstein metrics
(anti-self-dual, Ric = λg). These are precisely the negative Kähler-Einstein metrics
on complex surfaces. By the Aubin-Yau theorem, minimal surfaces X of general type
DO admit negative KE metrics.

The transition at k/A = 1/3 connects:
- Below: X#k CP̄² with k < A/3 may admit KE metrics (for suitable blow-up configurations)
- Above: X#k CP̄² with k > A/3 cannot admit Einstein metrics (mixed SW bound)

The question: does this transition happen continuously in the Ricci-pinching sense?

If metrics with δ → 0 exist on manifolds with k/A just above 1/3, these would be
near-ASD, near-Einstein metrics on no-Einstein manifolds, providing a counterexample
to P₄⁻ (and hence not refuting Q₄, since Q₄ ⟺ P₄⁺ ∨ P₄⁻).

## 6. Resolution of S0910A02's Basic Class Question

S0910A02 correctly noted that a² = A - k for all basic classes of M = X#k CP̄².
This is the TOPOLOGICAL self-intersection number. However, Proposition 4 uses the
SELF-DUAL PROJECTION (a⁺)², which satisfies:

$$(a^+)^2 = a^2 - (a^-)^2 \geq a^2 = A - k$$

With the sign trick: (a⁺)² ≥ (c₁(X)⁺)² ≥ c₁²(X) = A.

Both statements are correct. The topological square A-k and the projection bound A 
are compatible because (a⁻)² ≤ 0 contributes the difference.

## 7. Topology Corrections

For #_m CP²: χ = m+2, τ = m, so 2χ - 3|τ| = 4 - m.
- m = 3: 2χ-3|τ| = 1 > 0 (HT SATISFIED, not violated!)
- m = 4: equality
- m ≥ 5: HT violated

The Step 2 note had "2-m" which was incorrect.

## 8. Implications for Research Direction

**Negative branch (P₄⁻):** The counterexample search must now focus on the boundary 
k/A ≈ 1/3, where the Einstein-existence transition occurs. The key questions:

(a) Can metrics with δ → 0 be constructed on manifolds with k/A slightly above 1/3?
    This requires building metrics that are nearly ASD and nearly Einstein on blow-ups
    of surfaces of general type.

(b) Does the Kähler-Einstein theory on the base X provide a natural construction?
    For k < A/3, the blow-up X#k CP̄² may admit a negative KE metric. As k increases
    past A/3, the KE structure breaks. The broken KE metric (on manifolds just above 
    k/A = 1/3) might still have small δ.

(c) Are there ADDITIONAL obstructions beyond the mixed SW bound at the boundary?
    If the transition is discontinuous (with an additional gap at k/A = 1/3), the
    entire LeBrun family would have a uniform positive δ bound.

**Positive branch (P₄⁺):** All known no-Einstein 4-manifolds with δ₊ < 1 (i.e., 
admitting positive Ricci) have δ₊ bounded away from 0 by HT violation 
(δ₊ ≥ 1/(1+√3) for m ≥ 5). The case #_3 CP² (HT satisfied) is open.

The Strategist's point about Weyl concentration and orbifold singularities is 
important: even noncollapsed positive Ricci sequences can develop singularities.
The bridge between noncollapse and Einstein existence requires understanding
concentration and topology change, not just volume control.

**Overall:** Evidence tilts toward Q_n TRUE, with the negative branch now much more
constrained. The highest-value directions are:
1. Boundary behavior at k/A = 1/3 (decisive for negative branch)
2. Positive branch existence mechanism (decisive for positive branch)
3. P₃ resolution (achievable classical result)

## Source References
- Ishida-LeBrun: Knowledge/objects/papers/Spin-Manifolds-Einstein-Metrics-and-Differential-Topology--1a2235341441--f19aa00d70c8/object.md
- LeBrun 1996: Knowledge/objects/papers/4-Manifolds-without-Einstein-Metrics--c95911daf050--cd7839b9cc3d/object.md
- Min-Oo 1990: Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md
- Dossier: Skills/qiushi-yau26/references/research/20260910.tex
- Verification script: Sessions/S0910A01/workspace/scripts/mixed_sw_bound_analysis.py
