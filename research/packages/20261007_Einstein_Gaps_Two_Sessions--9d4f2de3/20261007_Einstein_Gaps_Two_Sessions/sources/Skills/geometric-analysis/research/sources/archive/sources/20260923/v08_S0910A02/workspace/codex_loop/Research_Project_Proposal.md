# Research Project Proposal

## Research Objective
Build a small, checkable Lean 4 artifact that advances the faithful formalization path for Yau Problem 26 by formalizing constant scaling of Riemannian metrics and the associated Ricci-pinching interval normalization as far as the locked Mathlib curvature infrastructure honestly permits.

This is not a request for another synthetic Yau-26 axiom shell. The target is a contentful curvature-library step: expose the exact mathematical lemma `Ric (c • g) = Ric g` as a `(0,2)` tensor for constant `c > 0`, together with the quadratic-form comparison transformation used in the interval reductions. If Mathlib still lacks enough Levi-Civita/Riemann/Ricci API, build the smallest honest local interface whose assumptions are precisely the real missing constructions, and prove the scaling/inequality algebra inside that interface without `sorry` or hidden axioms.

## Current Progress
Qiushi has already established mathematically that for a constant rescaling `g' = α g`, the Ricci `(0,2)` tensor is invariant while the metric quadratic form scales by `α`. This carries the interval classification and normalized branch reduction in `Sessions/S0910A02/workspace/notes/step85_yau26_established_reduction.md`, especially Sections 1 and 3. A previous Codex run produced `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/CurvatureInterfacePrototype.lean`, which honestly found that Mathlib v4.33.1 has connection and Riemannian metric substrates but no canonical Levi-Civita/Riemann/Ricci stack.

The new task should build on that prototype, not merely repeat the scan. The desired result is a compiling Lean file proving the constant-scale Ricci/pinching algebra in an honest interface whose hypotheses match the missing geometry. If possible, use actual Mathlib connection APIs for torsion/metric compatibility; if not possible within the bounded task, keep the interface explicit and small.

## Important Files
- `Sessions/S0910A02/workspace/notes/step85_yau26_established_reduction.md`
- `Sessions/S0910A02/workspace/codex_loop/Research_Report.md`
- `Sessions/S0910A02/workspace/codex_loop/work/lean_curvature_interface_step73/CurvatureInterfacePrototype.lean`
- `Skills/qiushi-lean-proof/SKILL.md`

## Task For Codex
1. Inspect the existing prototype and Mathlib APIs enough to avoid duplicate work.
2. Create a new work directory under `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/`.
3. Write one or more Lean files that compile with no `sorry`, `admit`, or source-declared axioms. The central file should formalize:
   - a faithful local interface for a smooth Riemannian metric, its Levi-Civita connection, curvature, and Ricci `(0,2)` tensor, with missing Mathlib constructions exposed as fields rather than hidden;
   - constant metric scaling by `c > 0`;
   - the geometric scaling law `Ric(c • g) = Ric(g)` either from a proven connection/curvature scaling argument if feasible, or as an explicitly named interface law that is then used to prove the pinching-normalization algebra;
   - quadratic-form pinching predicates and the transformation from `c0 g ≤ Ric_g ≤ C0 g` in a strict positive interval to `||Ric_{αg} - σ(αg)|| ≤ δ` or the equivalent pair of order inequalities, preserving signs and constants.
4. Run `Skills/qiushi-lean-proof/scripts/lean_check` on the resulting files and, if there is a named theorem, run `qiushi-yau26 lean <file> --declaration <name> --output <audit.json>`.
5. Write `Research_Report.md` explaining exactly what was formalized, what remains an interface assumption, what compiled, what audit found, and how the result maps to the mathematical interval theorem.

## Expected Output
Save artifacts under `Sessions/S0910A02/workspace/codex_loop/work/lean_metric_scaling_step86/`:
- Lean source files, preferably with a named theorem for the pinching normalization algebra;
- compile/audit JSON outputs;
- a concise report file inside that work directory, and update the top-level `Research_Report.md`.

The result must not claim a faithful formal proof of Yau Problem 26. It should honestly advance the Lean path by making the constant-scaling lemma and interval algebra checkable modulo explicitly exposed geometry infrastructure.