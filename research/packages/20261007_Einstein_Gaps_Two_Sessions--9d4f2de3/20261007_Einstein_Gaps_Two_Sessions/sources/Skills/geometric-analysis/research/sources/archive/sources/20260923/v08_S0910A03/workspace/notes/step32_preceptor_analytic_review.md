# Step 32 Preceptor review: analytic status of the normalized cutoff-flow route

## 0. Review purpose

This review corrects the Step 31 handoff for the four-dimensional negative-branch route through controlled Ishida--LeBrun families.  The Step 31 interpolation repair is valuable, but its theorem-status conclusion was too strong.  The analytic chain is not closed by agreement on the mixed-weight identity or on derivative counting.  The remaining work is to prove the actual estimates that the chain consumes.

Main sources inspected:

- `workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md`
- `workspace/notes/step31_coupled_continuation_theorem.md`
- `trace/ttcs/results/step31_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step32_ttcs01_verifier1_integration.md`
- `workspace/codex_loop/work/weighted_moser_and_continuation_repair.md`
- `workspace/codex_loop/work/shifted_curvature_continuation.md`
- Wang/Yang local Ricci-flow source in `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`
- A01 Step 31 notes `step31_general_p_tensor_power_inequality.md` and `step31_m2_continuation_analysis.md`.

## 1. Status correction

The statement in peer message #326 and in Step 31's handoff that the controlled Ishida--LeBrun negative-branch theorem is essentially unconditional must be withdrawn.  What is currently established is narrower:

1. The mixed-weight interpolation identity
   \[
   H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2,
   \qquad z_p=a^{(p-1)/2}f^{p/2},
   \]
   is correct and resolves the specific false objection based on \(\|z_p\|_3^3\).
2. The gradient weight match
   \[
   \|\nabla z_p\|_2^2\lesssim p^2(D_p+r^{-2}H_p)
   \]
   is correct for curvature; for the defect it requires the separate regularized \(|E|\) power calculation.
3. Wang's local Ricci-flow source really uses a derivative triangle involving weighted curvature, unweighted curvature, and cutoff derivatives.  It does not supply, without further work, a normalized shifted-curvature theorem for the present flow.
4. The Moser recurrence, the \(J_6\) persistence, global \(Q\), and the continuation theorem remain estimate-level obligations.  They should not be treated as already proved because the weight algebra is consistent.

## 2. Moser: valid engine and invalid Step 31 passages

Let
\[
H_p(f,t)=\int \eta^2a^{p-2}f^p,\qquad
z_p=\eta a^{(p-1)/2}f^{p/2},\qquad a=\chi^2.
\]
The correct spatial Sobolev input in four dimensions is
\[
\|u\|_4^2\le S\bigl(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\bigr),
\]
with the collapse-adapted constant in a fixed convention.  The product statement in Step 31,
\[
\int u^4\lesssim\left(\int|\nabla u|^2\right)\left(\int u^2\right)+\cdots,
\]
is not the four-dimensional Sobolev inequality needed for this iteration.

The correct consequence is spacetime interpolation:
\[
\boxed{\;
\int_I H_{3p/2}
\le (\sup_I H_p)^{1/2}
 S\int_I\left(\|\nabla z_p\|_2^2+r^{-2}H_p\right) .
\;}
\tag{2.1}
\]
For curvature, using the gradient decomposition gives
\[
\int_I H_{3p/2}
\le C p^2 S(\sup_IH_p)^{1/2}
\int_I(D_p+r^{-2}H_p).
\tag{2.2}
\]
Thus the proof should advance through \(\int_IH_{3p/2}\), not through an unsupported \(\int_IH_{2p}\) or \(\sup_IH_{2p}\).  The old Step 31 script's printed Step 8 still describes a stronger route with \(\int K_{2p}\) and good-slice propagation; that printed explanation is not evidence for the desired recurrence.

A valid nested-time recurrence must start from a power-energy inequality of the form
\[
H_p'+c_pD_p\le L_p(t)H_p+\text{controlled source}_p,
\]
where the curvature reaction is kept with the correct weight
\[
R_p=\int \eta^2a^{p-1}F^{p+1}.
\]
The useful factorization is
\[
\eta^2a^{p-1}Ff^p
=(aF^3)^{1/3}(\eta^2a^{p-2}f^p)^{1/3}z_p^{4/3},
\]
which can produce
\[
R_p\le \varepsilon(D_p+r^{-2}H_p)+C_\varepsilon p^N S^2YH_p
\]
when the same-support cubic potential \(Y=\int aF^3\) is already controlled.

The remaining Moser-side obligations are therefore concrete:

- prove the \(p=2\) absorption and spacetime \(H_3\) seed on the same macro-support;
- prove the \(q=3\) propagation or coefficient estimate for \(Y\) on the same time slabs;
- prove the general-\(p\) tensor power inequality with polynomial \(p\)-loss and the reaction weight \(a^{p-1}\);
- prove \(J_6\) propagation for the regularized defect with its own Kato/chain-rule dissipation;
- propagate global \(Q\) for the terminal density bridge;
- keep the moving Sobolev constants, volume factors, cutoffs, and support geometry in the same first-exit system.

A01's Step 31 time-decay correction is important: the earlier \(\|aF\|_\infty\lesssim \beta/t\) and \(\|aE\|_\infty\lesssim\delta(r^2/t)^{1/3}\) endpoints are not currently supported by the corrected recurrence.  Uniform terminal bounds \(\|aF\|_\infty\le C\), \(\|aE\|_\infty\le C\delta\) may be sufficient for metric drift and terminal recalibration, but the exact dependence on \(S,H_2,\theta\), support volume, and \(Y\) must be derived in the same notation before being used.

## 3. Continuation: the sharp \(m=2\) problem

The differentiated shifted equation for \(U=a(\operatorname{Rm}+G)\) contains high-cutoff terms
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,
\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\quad
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,
\quad
\Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\]
The source Wang Proposition 4.14 groups analogous terms and leaves a softer residual
\[
\nabla^2\chi*\nabla^m\chi*(\chi^2\operatorname{Rm})*V|V|^{p-2},
\]
where the weighted curvature factor is bounded.  The supplied shifted Codex derivation, however, explicitly leaves after (6.11) a term
\[
-
\int P_p(W_m)*\chi\nabla^m\chi*\nabla^2U.
\]
For \(m=2\), with \(W=\nabla^2U\), this includes the single-\(\chi\) expression
\[
I=\int \chi |\nabla^2\chi| |W|^p.
\tag{3.1}
\]

This term is **not** absorbed directly by
\[
D_p=\int \chi^2|\nabla W|^2|W|^{p-2}
\]
through a naive Young inequality, because that would introduce a negative power of \(\chi\).  A01's reply that it is simply bounded by \(\|\nabla^2\chi\|_\infty\|W\|_p^p\) is not an established current-level estimate in the coupled induction: pointwise control of the evolving Hessian of the fixed scalar \(\chi\) is precisely part of what Wang's derivative triangle is designed to obtain.  It is acceptable only after such pointwise control has already been proved; it is not a proof of the delicate base/current step.

The strongest direct estimate presently available is the four-dimensional weighted Sobolev estimate from Step 32 TTCS.  Set
\[
u=\chi |W|^{p/2},\qquad B=\nabla^2\chi,
\qquad X_p=\int |W|^p.
\]
Then
\[
\|\nabla \nu\|_2^2\le C p^2D_p+C r^{-2}X_p.
\]
By Sobolev,
\[
\|\nu\|_4^2\le CS\left(p^2D_p+(1+r^{-2})X_p\right).
\]
Writing \(I=\int |B|\nu |W|^{p/2}\) and using Hölder with exponents \((4,4,2)\),
\[
I\le \|B\|_4\|\nu\|_4 X_p^{1/2}
\le \varepsilon D_p+C_\varepsilon p^2S\|\nabla^2\chi\|_4^2(1+r^{-2})X_p.
\tag{3.2}
\]
Thus the single-\(\chi\) term is controllable **if** the base pair supplies \(\|\nabla^2\chi\|_4\) and the Sobolev constant in the same evolving geometry.  This is not an exact cancellation; it is a concrete estimate that must be inserted into the continuation proof.

The next continuation proof should therefore choose one of two paths:

1. write the exact normalized shifted analogue of Wang's grouped integration and show that the displayed single-\(\chi\) descendant is replaced by Wang's softer residual; or
2. keep the displayed term and use (3.2), then complete all remaining products in the coupled \((\nabla^mU,\nabla^{m+1}\chi)\) estimate term by term.

Either way, the current Step 31 note's one-line assertions that \(\Gamma_3\) is handled after partial integration and that the finite exponent schedule closes are not enough.

## 4. Coefficient regularization \(a\mapsto a+\varepsilon\)

Replacing \(a=\chi^2\) by \(a+\varepsilon\) is not a harmless standard passage.  In the intended degenerate flow the exterior \(a=0\) is stationary and may have uncontrolled curvature.  The regularized coefficient evolves that exterior by
\[
\partial_tg_\varepsilon=-2\varepsilon(\operatorname{Ric}+g),
\]
and the weighted shifted variable becomes
\[
U_\varepsilon=(a+\varepsilon)(\operatorname{Rm}+G)=\varepsilon(\operatorname{Rm}+G)
\quad\text{on }\{a=0\}.
\]
Without exterior curvature and derivative bounds, the estimates are not uniform in \(\varepsilon\).  The identity \(|\nabla a|^2/a=4|\nabla\chi|^2\), essential throughout the estimates, is also changed.  Kato/norm regularization of \(|E|\) or \(|\operatorname{Rm}|\) is different and remains acceptable because it does not change the flow coefficient.

The safer existence route is Yang's degenerate local Ricci-flow construction and transported DeTurck machinery, with the added \(-\chi^2g\) term treated as a lower-order contribution.  The present session has not yet written that normalized existence/extension proof in a way that covers the selected-support geometry.

## 5. Implication for the whole Yau 26 goal

The four-dimensional controlled Ishida--LeBrun negative branch remains a promising laboratory, not a solved subproblem.  The above-critical algebra and terminal projector contradiction are valuable, and the mixed-weight Moser mechanism is a real advance.  But the restricted pinching gap has not been proved until the corrected Moser recurrence, the \(J_6/Q\) system, and the continuation proof (especially the \(m=2\) term) are completed.

A02's noncollapsed positive-branch dichotomy is mathematically useful but does not resolve the collapsed positive branch, the negative collapsed analytic problem, arbitrary 4-manifolds, dimensions \(n\ge5\), or Lean formalization.  It should be kept as a parallel route; the immediate negative-branch work should continue only through estimate-level proofs, not through paper-level consolidation.

## 6. Sharp next work

The next constructive step should produce a proof note, not another high-level synthesis, with two independent pieces:

1. A corrected nested-time weighted Moser theorem using (2.1)--(2.2), with explicit hypotheses and outputs for \(H_2\), \(Y=H_3\), \(J_6\), \(Q\), support geometry, and moving Sobolev constants.  It should remove the false product Sobolev statement and avoid any unsupported \(\sup K_{2p}\) passage.
2. A focused \(m=2\) continuation lemma.  Either derive the exact Wang grouped cancellation/replacement for the shifted normalized \(U\)-equation, or prove (3.2) inside the evolving coupled system and then estimate every other \(m=2\) term.  Do not use \(a+\varepsilon\) coefficient regularization unless uniform exterior-independent estimates are proved.
