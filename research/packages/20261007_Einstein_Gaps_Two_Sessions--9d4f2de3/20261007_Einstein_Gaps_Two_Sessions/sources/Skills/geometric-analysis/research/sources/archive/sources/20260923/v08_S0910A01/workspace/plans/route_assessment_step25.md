# Route assessment after Step 25

## Main advance

The q=2 curvature energy inequality, the triangular defect energy inequality,
and the global defect preservation identity are now derived at the schematic
tensor level, with all terms classified, Young absorptions verified, and the
buffered-support cancellations confirmed.

**A03 normalization correction incorporated:** the -2a Rm tensor damping from
the conformal part of h = -2a(Ric+g) is exactly cancelled by the 4
inverse-metric variations when computing |Rm|².  For F² = 1+|Rm|², only a
bounded source C₀ = O(Vol) remains.  Consistency: pure conformal flow
dg/dt = -2g gives d/dt ∫|Rm|²dμ = 0.

**TTCS corrections incorporated:**
1. Hessian formula corrected to tensor ∇²a = 2dχ⊗dχ + 2χ∇²χ
2. Inequality (2.11) restated as absolute-value upper bound
3. First-exit Approach A withdrawn: good-center gives L² curvature, not L^∞
4. Interior plateau regularity (standard Shi for the non-degenerate normalized
   Ricci flow on {a=1}) is the correct route for (F3)

## Conditional gap theorem status (A03 formulation adopted)

The six PDE obligations are:

| Task | Status |
|------|--------|
| T1: q=2 tensor inequality | Derived schematically (Step 25); index-level Bianchi not written |
| T2: q=3 tensor inequality | Same mechanism, different test function (Step 24) |
| T3: Defect inequality | Derived schematically (Step 25); homogeneity verified |
| T4: Interior Shi on plateau | Standard, non-degenerate (A03) |
| T5: Smooth existence | Open; degenerate cutoff flow |
| T6: Topology/geometry chain | Conditional on T1-T5; Steps 5-8 |

## What is NOT settled

- Full index-level tensor derivation with Bianchi simplification (the schematic
  derivation correctly classifies all terms, but the exact Bianchi cancellation
  producing the Lichnerowicz Laplacian is cited from Hamilton, not re-derived)
- Smooth existence for the degenerate cutoff flow (T5)
- The Moser iteration on the plateau from H₃ to |Rm| ≤ C/t (standard but not
  written)
- Positive branch, n ≥ 5, full Yau 26, Lean formalization

## Peer status

- A02 Step 25: Toric BREAK verdict — integral identities alone cannot obstruct
  tight positive pinching on #_k(S²×S²). A BUILD theorem would need a global
  PDE solvability obstruction. Positive branch P4+ remains the sharpest open
  test.
- A03 Step 24: Normalization correction and conditional gap formulation adopted.
  Six-task decomposition (T1-T6) is the shared roadmap.

## Files

- `workspace/notes/step25_tensor_energy_derivation.md` (corrected)
- `workspace/notes/step25_first_exit_formulation.md` (corrected)
- `workspace/scripts/step25_tensor_energy_verification.py` (all checks pass)
- `workspace/plans/route_assessment_step25.md` (this file)
- TTCS: `trace/ttcs/results/step25_ttcs01_verifier1_integration.md`
