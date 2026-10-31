# Research Project Proposal

## Research Objective
Derive and check the exact local tensor energy inequalities needed for the Step 24 buffered selected-support cutoff-flow route in the Yau Problem 26 project.

## Current Progress
The main session is studying a four-dimensional negative LeBrun/Ishida-LeBrun counterexample laboratory for Yau 26. The current analytic bridge uses the normalized cutoff flow

\[
\partial_t g=-2a(\operatorname{Ric}+g),\qquad a=\chi^2,
\]

on a selected maximal-function good support. Step 24 separates the physical cutoff `chi` from an auxiliary energy cutoff `eta`, with `supp chi` strictly inside `{eta=1}` and `supp grad eta` in a collar where `a=0`. This removes the all-center/bad-center smallness problem. The remaining load-bearing question is the exact tensor calculus behind the schematic inequalities:

1. q=2 curvature energy:
\[
H_2'+cD_2 \le C\int \eta^2 aF^3+C r^{-2}H_2,
\]
where `F=(1+|Rm|^2)^{1/2}`, `H_2=int eta^2 F^2`, `D_2=int eta^2 a |nabla Rm|^2`.

2. q=3 weighted curvature energy:
\[
Y'+cD_3 \le C r^{-2}Y+C\int \eta^2a^2F^4,
\]
where `Y=int eta^2 aF^3`, `D_3=int eta^2a^2F |nabla Rm|^2`.

3. triangular defect energy:
\[
Q'+cX \le C r^{-2}Q+C\int \eta^2aF|E|^2,
\]
where `E=Ric+g`, `Q=int eta^2 |E|^2`, `X=int eta^2a|nabla E|^2`.

The main session has monomial/scaling checks but not an index-level derivation. It is important to avoid any curvature-only source in the defect equation and to confirm how Hessian-a terms integrate by parts.

## Important Files
- Sessions/S0910A01/workspace/notes/step24_buffered_support_energy_test.md
- Sessions/S0910A01/workspace/scripts/step24_buffered_support_algebra.py
- Sessions/S0910A01/workspace/scripts/step24_support_tensor_monomials.py
- Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md
- Sessions/S0910A01/workspace/notes/step16_preceptor_review_smoothing_architecture.md
- Sessions/S0910A03/workspace/notes/step22_critical_energy_lemma_formulation.md
- Sessions/S0910A03/workspace/scripts/verify_cutoff_defect_energy.py

## Task For Codex
Work inside `Sessions/S0910A01/workspace/codex_loop/work/`. Produce an independent mathematical derivation memo, not final paper prose.

Focus on the exact tensor variation formulas for a general metric variation `partial_t g = -2aE` with `E=Ric+g` in dimension four. Derive enough to decide whether the three inequalities above have the stated weights and no missing terms. In particular:

1. Write the index-level formula for `partial_t Rm` under `h=-2aE`, separating principal `a Delta Rm`, cubic/algebraic curvature terms, `nabla a * nabla E`, and `nabla^2 a * E` terms.
2. Show how testing the `q=2` regularized curvature energy with `eta^2` and using `supp grad eta subset {a=0}` yields the stated inequality, or identify exact extra terms.
3. Show the `q=3` weighted energy for `Y=int eta^2 aF^3` and confirm the dissipation weight `a^2 F |nabla Rm|^2`; check whether `I4=int eta^2 a^2F^4` is the right reaction.
4. Derive the evolution of `E=Ric+g` under the same flow and test against `eta^2E`. Confirm whether every term is homogeneous in `E` or `nabla E`, with no independent `(nabla^2 a)*g` source after the Ricci and normalization terms are combined.
5. State exactly which assumptions are needed for evolving Sobolev constants and cutoff-gradient bounds; do not assume pointwise curvature bounds unless they are separately justified.

Use symbolic/index algebra or small scripts only if useful. Save any scripts or notes under the `work/` directory.

## Expected Output
- `Sessions/S0910A01/workspace/codex_loop/work/tensor_energy_derivation.md`: an explicit derivation/check memo with equations and conclusions.
- Optional scripts under `work/` if they help verify algebraic contractions.
- `Sessions/S0910A01/workspace/codex_loop/Research_Report.md`: concise report stating whether the three inequalities are supported, what repairs are needed, and exact next mathematical tasks.
