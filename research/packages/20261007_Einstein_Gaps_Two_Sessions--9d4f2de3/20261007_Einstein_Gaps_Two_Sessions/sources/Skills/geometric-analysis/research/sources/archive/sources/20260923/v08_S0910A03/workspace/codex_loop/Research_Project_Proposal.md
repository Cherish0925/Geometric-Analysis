# Research Project Proposal

## Research Objective
Repair or refute the remaining analytic core of the four-dimensional negative Ricci-pinching route for Yau Problem 26. The immediate issue is whether the normalized fixed-cutoff flow
\[
\partial_t g=-2a(\operatorname{Ric}+g),\qquad a=\chi^2,
\]
admits a weight-consistent Moser estimate for the genuinely weighted geometric variables
\[
T=\operatorname{Rm}+G,\quad G=(g\owedge g)/(2(n-1)),\quad U=aT,\quad V=aE=a(\operatorname{Ric}+g),
\]
and a rigorous smooth-extension induction.

## Current Progress
A TTCS check found a fatal half-power mismatch in the old moments K_p=\int a^{p-2}\Phi^p: the Sobolev output has an extra a^{1/2} and cannot control K_{3p/2}. A proposed repair is ordinary unweighted L^p Moser on |U| and |V|, seeded by H_3=\int aF^3 and J_6=\int a^4|E|^6. This repair has not been derived from the actual tensor equations and may hide unweighted cutoff-derivative or unweighted-curvature terms. Separately, the high-order continuation proof must couple \nabla^mU with \nabla^{m+1}\chi; Wang's printed Proposition 4.14 omits a surviving term if it claims dependence only through cutoff order m.

## Important Files
- Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md
- Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md
- Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md
- Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md
- Sessions/S0910A01/workspace/notes/step29_simultaneous_support_theorem.md
- Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md
- Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md

## Task For Codex
1. Derive the exact/schematic evolution and weak power-energy inequalities for U=aT and V=aE, treating them as unweighted tensor variables. Track all da, Hess(a), moving norm, moving measure, G-linear, and curvature reaction terms. Do not divide by a. Determine whether standard parabolic Moser on \int|U|^p and \int|V|^p genuinely closes from the existing positive-time H_3 and time-zero J_6 seeds, with volume-independent endpoints |U|<=C beta/t and |V|<=C delta(r^2/t)^(1/3). If it fails, exhibit the exact unmatched term and propose the strongest valid replacement.
2. Repair the smooth-extension proof by writing the current-order coupled estimate for (\nabla^mU,\nabla^{m+1}\chi), including expanded Gamma_1--Gamma_4 integrations and a finite Hölder exponent schedule. Then estimate \nabla^mT. Do not inherit Wang's omitted term or claim cutoff order m suffices.
3. Record any implications for a common flow on a union of disjoint macro-supports.

## Expected Output
Write a detailed mathematical memo under Sessions/S0910A03/workspace/codex_loop/work/ and update Research_Report.md. Include explicit equations, inequalities, failure points, and any small symbolic verification scripts. Distinguish proved calculations from source-dependent steps.