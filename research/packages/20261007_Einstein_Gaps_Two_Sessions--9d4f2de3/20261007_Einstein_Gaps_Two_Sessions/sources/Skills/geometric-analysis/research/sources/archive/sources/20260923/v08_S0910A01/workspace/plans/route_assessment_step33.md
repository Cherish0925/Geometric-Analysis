# Route assessment after Step 33

**Step 34 superseding notice.**  Use
`workspace/notes/step34_integrated_potential_q3_and_defect.md` and
`workspace/plans/route_assessment_step34.md` for the current fixed-exponent layer.
Step 34 corrects the p=2 localization to \(K_2^\eta\), repairs the curvature
volume term and the pre-absorption dissipation coefficient, derives q=3
propagation by integrated-potential good-slice/Gronwall, and replaces the
regularized three-factor \(J_6\) route by A03 Step 35's unregularized two-factor
absorption.  The Step 33 table is useful historical context but not the current
mathematical state.

## Key advances

1. **Explicit curvature power inequality** (3.1) with term-by-term IBP tracking.
   The Hessian-of-a term has two correct routes (TTCS-corrected): either
   direct pointwise bound assuming evolving cutoff-Hessian control, or honest
   tensor IBP consuming ε D_p^Rm.  The original "IBP of |∇²a|" was invalid.

2. **J_6 persistence from time zero** (4.7) by bounded integrated Gronwall.
   The integrated curvature seed ∫₀ᵀ Y ≤ C γ K₂(0) gives
   ∫₀ᵀ S² Y ≤ C γ³ directly, without smoothness-at-zero patching or
   initial-interval replacement.  This is the simplest correct argument for
   defect persistence and avoids the nonintegrable 1/t singularity.

3. **Defect power inequality** (4.4) with the same S² Y Gronwall coefficient
   as curvature.  The three-factor identity with Hölder (3,3,3) — not
   (3,3,3/2) — applies to both curvature (F^{p+1}) and defect (F f^p)
   reactions.

4. **Regularization source clarification.** The C₀'p source vanishes as
   ε → 0 because the unregularized defect equation is homogeneous in E.
   The final J_6 estimate has no additive curvature-only term.

## TTCS corrections incorporated

- IBP of absolute-value Hessian is invalid; replaced by two correct routes
- Hölder exponents corrected from (3,3,3/2) to (3,3,3)
- Smoothness-at-zero Gronwall patching replaced by integrated seed
- Regularization source must be shown to vanish as ε → 0

## Conditional chain status (within first-exit regime)

| Step | Status | Evidence |
|------|--------|----------|
| K_p power inequality | Conditional (Route A or B) | step33 note §2-3 |
| J_p defect inequality | Conditional, same coefficient | step33 note §4 |
| H_2 persistence | Conditional on q=2 | Step 25 |
| γ control | From selected good center | Step 24/32 |
| ∫ Y ≤ Cγ K_2 | Conditional (q=3 propagation) | Step 34 eq 3.2 |
| Y(t) ≤ Cγ K_2/t | Conditional (q=3 forward prop) | Step 34 eq 3.3 |
| ‖aF(t)‖ ≤ Cγ/t | Conditional (curvature Moser) | step33 eq 5.1 |
| J_6 persistence | **NEW: bounded Gronwall** | step33 §4.1 |
| ‖aE(t)‖ ≤ Cδ(r²/t)^{1/3} | Conditional (defect Moser) | step33 eq 5.2 |
| V(T) → 0 | Conditional (integrable drift) | step33 eq 5.3 |
| Metric comparison | Conditional on V(T) | Standard |
| Moving Sobolev | Conditional on metric comparison | Standard |
| Continuation | Open (cutoff-jet induction) | A03 Step 34 §6 |

## Remaining decisive estimates

1. **q=3 same-support propagation**: prove ∫₀ᵗ Y ≤ C γ K₂ and
   Y(t) ≤ C γ K₂/t using the H₂ → H₃ absorption and forward energy.

2. **Moving Sobolev first-exit closure**: prove S(t) ≤ 2S(0) within
   the metric drift interval, then close the bootstrap.

3. **Cutoff-jet continuation**: the coupled (∇U, ∇²χ) base pair from
   A03 Step 34 §6, required for either Hessian Route A or the shifted-
   curvature extension.

4. **Macro-disjoint support construction**: retain a fixed A-proportional
   plateau fraction with buffers for terminal exponential geodesics.

## Relation to full Yau 26

Even completed, this covers only the restricted 4D negative Ishida-LeBrun
near-critical family.  The positive branch (A02's noncollapsed dichotomy),
arbitrary 4D topology, n ≥ 5, and Lean formalization remain open.

## Files

- Curvature power inequality: `workspace/notes/step33_curvature_power_inequality.md`
- Verification: `workspace/scripts/step33_curvature_power_verification.py`
- TTCS: `trace/ttcs/results/step33_ttcs01_verifier1_integration.md`
- Patched Step 32 note: `workspace/notes/step32_nested_moser_and_tensor_audit.md`
