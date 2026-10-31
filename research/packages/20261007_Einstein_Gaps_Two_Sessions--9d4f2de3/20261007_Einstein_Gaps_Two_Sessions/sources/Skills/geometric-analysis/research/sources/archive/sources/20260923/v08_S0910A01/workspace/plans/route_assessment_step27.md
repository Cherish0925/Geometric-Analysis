# Route assessment after Step 27

## Critical convergence

Three independent sessions (A01, A03, and partially A02) now converge on
the same analytic endpoint for the four-dimensional negative-branch LeBrun/
Ishida-LeBrun route.  The conditional gap chain is:

1. **Initial Sobolev** (A03, Maheux-Saloff-Coste): S = Cr²Vol^{-1/2},
   no noncollapse needed.  RESOLVED.

2. **General-p power-energy inequality** (A03, §3): polynomial p³ growth,
   both for F and |E|, with Kato regularization for |E|.  RESOLVED
   (script-verified, A03 §3.1-3.4).

3. **Three-factor absorption** (A01, §3): replaces direct critical absorption
   by positive-time curvature potential Y; gives Gronwall coefficient
   Λ_p = C_p r⁻² + C_p'S²Y(t) with Y entering linearly.

4. **Unified Moser iteration** (A01 §4-6, A03 §5): one template serves both:
   - Curvature: p₀=3, ||aF|| ≤ Cβ/t  [S cancels exactly]
   - Defect: p₀=6, ||aE|| ≤ Cδ(r²/t)^{1/3}  [V cancels exactly]
   Both volume cancellations verified symbolically.

5. **Normalized continuation** (A03, §2-7 and Codex artifact, shifted curvature T = Rm + G):
   Yang short-time + Wang extension via joint induction on U=aT and cutoff jets.
   The shift prevents treating normalization as a vague lower-order term and
   restores Wang's derivative mechanism.  Step 28 TTCS supports this at the
   schematic/Wang-mechanism level, but a fully expanded Wang Proposition 4.14
   grouping, staggered Hölder exponents, and Yang degenerate restart details are
   still needed for an independently written proof.

6. **First-exit closure** (A03 §6.2, A01 §3.1): metric drift
   (3/2)Cδθ^{2/3}r² → 0 self-improves the support metric comparison if the
   simultaneous selected-support estimates hold.  Splicing
   max{K₀, Cβ/t₀} < ∞ handles t=0 divergence.  This is a conditional analytic
   package, not a global theorem for arbitrary supports.

7. **Global defect identity** (Step 25): Q_global(t) ≤ e^{Cθ}Q_global(0)
   from disjoint stationary collars remains a load-bearing estimate to preserve
   in the simultaneous multi-support flow.

## TTCS corrections incorporated

- Theorem 1.1: ε-regularization withdrawn; Yang direct degenerate construction
  referenced instead.
- Theorem 2.1: ∇g = 0 resolves one concern, but A03's shifted-curvature
  formulation properly handles the ∇^{m+2}a and evolving cutoff jets.
- Theorem 3.1: explicit splicing bound added.
- Moser sum: sum 1/p_k = (n+2)/(2p₀), with each Sobolev step contributing
  S^{1/(κp_k)}, so the net Sobolev power is S^{n/(2p₀)}.  Final volume
  cancellations remain correct.
- source_p: for curvature, the C₀ Vol source from F² = 1+|Rm|² is absorbed
  into Cr⁻²H_p because F ≥ 1.

## Remaining downstream issues

Even with all six analytic pieces above, the conditional gap chain has two
remaining downstream issues (identified by TTCS):

### A. Terminal calibration reapplication

The mixed SW and tensor-gap inequalities from Steps 3-8 must be reapplied to
the TERMINAL metric g(θr²), not transported by C⁰ comparison.  This is
structurally correct because:
- The Seiberg-Witten inequality is topological (applies to any metric on M)
- The Chern-Gauss-Bonnet identity holds for g(T)
- The completion-square remainder is derived algebraically from s and |W⁺|

The global defect identity gives Q(T)/A → 0, so the nonneg deficit densities
have vanishing normalized averages on any set of positive measure, including
the bounded-curvature plateau fraction.

### B. Downstream local geometry superseded by exponential pullback

Step 28 replaces the proposed F-structure/Euler-density route.  If the analytic
selected-support theorem produces a set of inner plateau centers with
`Vol(P_i) >= alpha A_i` and sequence-uniform `(rho,K)` bounded-curvature
buffers, the Step 16 exponential-pullback averaging lemma selects a tangent
space ball with vanishing terminal deficit mean.  Rauch comparison supplies the
noncollapsed local geometry on the pulled-back tangent domain even when the
base plateau is collapsed.  Thus no Euler-density localization is needed for
this downstream selection.  The real remaining upstream task is to prove that
such a quantitative plateau family and global `Q(T)/A -> 0` are produced by the
same selected-support flow.

### C. Higher dimensions, positive branch, full proposition

- A02 Step 27: H3 positive-branch analysis excludes ordinary diagonal
  closures under Lambda > 0 but not all possible models.
- Dimensions n ≥ 5: no analogous mechanism; positive collapse can be
  Einstein-compatible.
- Full Yau 26 proposition and Lean formalization: not started.

## Scope of the conditional result

If the simultaneous selected-support estimates, shifted-curvature continuation,
global `Q` propagation, and Step 28 terminal pullback selection are all written
as complete proofs, the result would be:

> **Conditional 4D negative gap theorem.** There exist dimension constants
> c₄ < 0 < C₄ such that no closed smooth four-manifold in the critical
> Ishida-LeBrun family carries a metric with c₄ g ≤ Ric ≤ C₄ g.

This excludes one specific counterexample family, not all four-manifolds.
It is a necessary condition for a full negative-branch proof in dimension four.

## Files

- Unified Moser iteration: `workspace/notes/step27_unified_weak_moser_iteration.md`
- Continuation theorem: `workspace/notes/step27_normalized_continuation_theorem.md`
  (corrected, referencing A03 shifted-curvature formulation)
- Three-factor verification: `workspace/scripts/step27_three_factor_absorption.py`
- A03 general-p: `Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md`
- A03 continuation: `Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md`
