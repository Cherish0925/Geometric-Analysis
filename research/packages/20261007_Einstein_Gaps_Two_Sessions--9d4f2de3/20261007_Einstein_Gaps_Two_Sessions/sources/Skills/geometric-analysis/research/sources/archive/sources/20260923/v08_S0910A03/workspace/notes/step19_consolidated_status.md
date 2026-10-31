# Step 19 Consolidated Status

> **Step 20 update.** Preserve the volume-independent critical parameter and p>4 derivative-drift threshold. Replace the transition use of an unweighted Li potential by the weighted Wang hierarchy in `step20_weighted_wang_hierarchy_and_whitney_correction.md`; replace automatic global defect preservation by its triangular small-energy form.

## Established results

1. **Volume-independent β (proved):** In 4D, Wang's critical curvature parameter β = A²·‖Rm‖₂ = C²r²√K₀ is independent of collapsed volume. With the Li radius, β = C√ε_Li. The same 4D Sobolev-energy cancellation mechanism drives both β and the coupled L² system.

2. **p > 4 connection-drift threshold (proved):** If |χ∇(χ²E)| ~ δt^{-1/2}(r²/t)^{2/p}, the connection drift is time-integrable iff p > 4 (vs p > 2 for metric). For p = 6: metric drift ~ δθ^{2/3}r², connection drift ~ δθ^{1/6}. The Hessian-a drift also requires p > 4 and is O(δ) dimensionless.

3. **Conditional first-exit architecture (formulated):** A simultaneous first-exit with no circularity: small energy → curvature decay → defect decay → derivative decay → metric + connection + Hessian drift O(δ) → all provisional bounds improved. Requires two new PDE results.

## Remaining PDE targets

**Target 1 (refined in Step 20):** implement the fixed q=2,3 weighted Wang hierarchy on the evolving finite-neighbor system to establish the transition cubic potential A⁴∫χ²F³ ≤ Cγ³/t and then the nested zero-order recurrence. The weight is essential; an unweighted Li potential is unavailable in the transition.

**Step 20 replacement for Target 2:** quantitative weighted Bernstein is not required for a zero-order first-exit. Complete the nested H_q/J_m recurrences, then adapt Wang's qualitative smooth-extension induction to the normalized cutoff flow. The term χa∇Rm·U remains an obstruction only if quantitative C¹ control is separately sought.

The current load-bearing work is the finite-neighbor weighted recurrence and normalized smooth-extension adaptation. Volume cancellation removes the collapsed-volume obstruction, while the Wang powers handle transition degeneracy without converting the potential to an unweighted Li norm.

## Scope clarification

Even if both targets are proved and the first-exit closes:
- This yields the fixed-topology gap inf_g ‖Ric+g‖_∞ > 0 for critical Ishida-LeBrun 4-manifolds
- The Noether bound χ/A ≤ 65/6 would make it uniform across the standard subclass
- It does NOT settle: unrestricted negative branch, positive branch, n ≥ 5, full Yau 26, Lean formalization

## Files

- Main note: `workspace/notes/step19_p4_threshold_and_degenerate_moser.md`
- Scripts: `workspace/scripts/verify_step19_p4_threshold_and_bernstein.py`, `verify_step19_volume_independent_beta.py`
- TTCS: `trace/ttcs/results/step19_ttcs01_verifier1_integration.md`
- Session group: messages #288, #289
