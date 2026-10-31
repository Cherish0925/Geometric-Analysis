# Route Assessment — Step 80

Session `S0910A01`. Updated after J-symmetry theorem and TTCS corrections.

## Status of the three active branches

### 1. Restricted IL negative-gap theorem (mature, research-level)

**Status:** Most mature branch. All 9 modular proof notes written and verified (Steps 67–72). Not a dimension-only theorem; covers the specific four-dimensional Ishida–LeBrun geography with q ≥ 0 and complex general-type blocks.

**Next work needed:** Independent verification of analytic passages; regularization-to-degenerate-flow interface; Lean formalization (distant).

**Value for Yau-26:** Establishes a family-uniform negative pinching gap for one geography. Does not by itself refute the full proposition (a positive-branch counterexample would also be needed).

### 2. Positive mixed-row desingularization (this step)

**Status:** The J-symmetry theorem (Step 80) proves:
- ALL transverse obstruction projections vanish at every resolved order (exact symmetry)
- Radial μ₁ = 0 at second order (determinant)
- Scalar kernel modes eliminated (A-symmetry)

**TTCS correction:** Higher-order radial terms (order t³: self-response, inter-node Green interaction) are NOT eliminated. The surviving problem is a genuine 2×2 system.

**Key structural facts:**
- Product orbifold: (S²×S²)/⟨(r_π,r_π)⟩ with σ tangent action -I₄ (confirmed by manuscript)
- Symmetry group: ⟨σ, A, J⟩ ≅ Z₂³, with J = simultaneous conjugation
- Shape mode g₁-g₂: eigenvalue -Λ, survives A+J, makes P indefinite on complement
- The system is balanced but balanced ≠ existence: leading cubic B(t₁²,t₂²) = 0 might have only trivial solution if B is invertible

**Next work needed:**
1. Compute the radial self-response and inter-node response at order t³
2. Determine the leading cubic coefficient matrix B
3. Check whether B has a nontrivial kernel or sign structure allowing positive-scale solutions
4. If B = 0, go to next order; if B has a positive zero, pursue nonlinear estimates
5. Address inverse operator estimates with the -Λ negative mode

**A02's Gursky/LeBrun direction:** Complementary. If Weitzenbock-Weyl gives a topological obstruction to positive Einstein on mixed rows (b⁺,b⁻ ≥ 2, χ=8), that would be decisive and make the desingularization question moot. If no obstruction is found, the desingularization construction is the natural follow-up.

### 3. Graph-neck negative laboratory (ongoing, A03-led)

**Status:** A03 (Steps 74–76) sharpened the center theorem: for Koiso R=-6 centers on T³, λ_min ≤ -3+3δ, conserved flux Q=0, and energy transported by covariance pairing F. Umbilic finite exit is obstructed by conformal flatness. Full five-component searches have not yielded sub-O(1) residuals.

**Value for Yau-26:** If a small-defect graph manifold with no Einstein metric is constructed, it provides a negative-branch counterexample candidate. Currently, neither the center construction nor the cusp matching is complete.

## Priority ranking

1. **A02 Gursky/LeBrun test** — if it yields a topological obstruction to positive Einstein on mixed rows, the whole positive branch's scope changes. Cheapest decisive gate.

2. **Step 80 radial system computation** — compute the order-t³ self-response and inter-node interaction in the A+J symmetric family. This is the next concrete calculation for the desingularization route.

3. **IL assembly independent verification** — the most mature branch but requires careful analytic checking.

4. **Graph-neck full-constraint continuation** — A03's ongoing work. Numerical evidence of sub-O(1) residuals would change the landscape.

## What is NOT resolved

- Full sign-unrestricted Yau-26 proposition (neither proved nor refuted)
- Positive branch for arbitrary four-manifolds
- Dimensions n ≥ 5
- Lean formalization of any branch
- Whether the balanced 2×2 system has positive-scale solutions
