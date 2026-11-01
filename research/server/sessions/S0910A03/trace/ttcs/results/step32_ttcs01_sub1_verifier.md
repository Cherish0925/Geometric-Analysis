# TTCS Independent Branch Record

```json
{
  "step_id": 32,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step31_weighted_moser_interpolation_and_first_exit.md",
    "Sessions/S0910A03/workspace/notes/step31_coupled_continuation_theorem.md",
    "Sessions/S0910A03/trace/ttcs/results/step31_ttcs01_verifier1_integration.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

For the four-dimensional normalized cutoff flow route toward the Ishida-LeBrun negative Ricci-pinching gap, critically verify the two remaining analytic points, using the supplied files rather than assuming the previous synthesis. (1) Moser: keep the valid mixed-weight identity H_{3p/2} <= H_p^{1/2}||z_p||_4^2, but check that the correct nested-time recurrence follows only from the direct spacetime interpolation int_I H_{3p/2} <= (sup_I H_p)^{1/2} S int_I(|nabla z_p|^2+r^{-2}H_p); identify exactly what upstream estimates (H3/Y, J6, Q, same-support bootstrap) are still needed. (2) Continuation: inspect the m=2 version of Codex equations (6.11)-(6.13), where a term schematically looks like int chi |nabla^2 chi| |nabla^2 U|^p. Decide whether the exact Wang grouped integrations cancel/replace this single-chi term, whether an available weighted Sobolev estimate controls it, or whether the induction must be changed. Also comment on why replacing a by a+epsilon is not automatically harmless when outside supports have uncontrolled curvature. Return a direct mathematical memo naming valid pieces, invalid steps, and the sharp next proof obligation; do not decide final writing readiness.

## Output

# Mathematical verification memo

## 1. Weighted Moser recurrence

Write the four-dimensional Sobolev constant as \(\mathcal S\) in the form
\[
\|u\|_{L^4}^2\le \mathcal S\bigl(\|\nabla u\|_{L^2}^2+r^{-2}\|u\|_{L^2}^2\bigr).
\]
For
\[
H_p(f)=\int \eta^2 a^{p-2}f^p,\qquad 
z_p=\eta\,a^{(p-1)/2}f^{p/2},
\]
the mixed-weight interpolation is correct:
\[
H_{3p/2}(f)
\le H_p(f)^{1/2}\|z_p\|_{L^4}^2.
\]
The weight identity is
\[
\frac{p-2}{2}+(p-1)=\frac{3p}{2}-2,
\]
so the earlier \(\|z_p\|_3^3\) computation is not the object needed by the iteration.

The gradient estimate is also correct for \(f=F=(1+|\mathrm{Rm}|^2)^{1/2}\):
\[
\|\nabla z_p\|_2^2
\le C p^2\bigl(D_p+r^{-2}H_p\bigr),
\qquad
D_p=\int \eta^2 a^{p-1}F^{p-2}|\nabla \mathrm{Rm}|^2,
\]
with additional harmless \(|\nabla\eta|^2H_p\) terms if nested spatial cutoffs are used. The cutoff term uses
\[
a^{p-3}|\nabla a|^2
=4a^{p-2}|\nabla\chi|^2.
\]

The correct spacetime step is therefore
\[
\boxed{
\int_I H_{3p/2}(f)\,dt
\le
\bigl(\sup_I H_p(f)\bigr)^{1/2}
\mathcal S
\int_I\bigl(\|\nabla z_p\|_2^2+r^{-2}H_p(f)\bigr)\,dt .
}
\]
This gives an integral recurrence, not a direct \(\sup H_{2p}\) recurrence. The line in `step31_weighted_moser_interpolation_and_first_exit.md` that speaks of first obtaining \(\int K_{2p}\) or \(\sup K_{2p}\) is not justified by the displayed Sobolev inequality. The valid recurrence must pass through \(\int H_{3p/2}\).

With nested time intervals \(I_k=[\tau_k,t]\), \(p_{k+1}=3p_k/2\), and a time cutoff supported in \(I_k\), the needed energy input has the form
\[
\sup_{I_{k+1}}H_{p_k}
+\int_{I_{k+1}}\bigl(\|\nabla z_{p_k}\|_2^2+r^{-2}H_{p_k}\bigr)
\le
C p_k^N L_k \int_{I_k}H_{p_k}.
\]
Then the spacetime interpolation gives
\[
\int_{I_{k+1}}H_{p_{k+1}}
\le
C\,\mathcal S\,p_k^N L_k^{3/2}
\left(\int_{I_k}H_{p_k}\right)^{3/2}.
\]
This is the right four-dimensional parabolic recurrence. Since
\[
\sum_k \frac1{p_k}=\frac3{p_0},\qquad
\sum_k \frac1{p_{k+1}}=\frac2{p_0},
\]
the endpoint has the form
\[
\|af(t)\|_\infty
\le
C\,\mathcal S^{2/p_0} t^{-3/p_0}
\left(\int_{t/2}^t H_{p_0}(s)\,ds\right)^{1/p_0},
\]
provided \(L_k\sim 2^k t^{-1}+r^{-2}\) up to polynomial \(p_k\)-loss. The endpoint is indeed \(\|af\|_\infty\), because
\[
H_p^{1/p}=\|\eta^{2/p}a^{1-2/p}f\|_{L^p}\to \|af\|_\infty
\]
on the active region.

### Upstream estimates still required for the Moser route

The recurrence above is usable only after several same-support inputs are in place.

1. **Weighted \(H_p\) energy with correct reaction weight.**  
   For curvature,
   \[
   H_p'(F)+c\|\nabla z_p\|_2^2
   \le
   C p^N r^{-2}H_p(F)+Cp\,R_p,
   \]
   with
   \[
   R_p=\int \eta^2 a^{p-1}F^{p+1}.
   \]
   The weight \(a^{p-1}\) must be retained. Enlarging it to \(a^{p-2}\) destroys the Hölder factorization.

2. **Same-support \(Y=H_3(F)\) control strong enough for high \(p\).**  
   The reaction can be estimated by
   \[
   R_p
   \le
   \varepsilon\bigl(\|\nabla z_p\|_2^2+r^{-2}H_p\bigr)
   +C_\varepsilon p^N \mathcal S^2 Y\,H_p,
   \qquad
   Y(t)=\int \eta^2 aF^3 .
   \]
   For the high-\(p\) recurrence, it is not enough to know only \(\int Y\) unless one has an argument converting
   \(\int YH_p\) into \(L_k\int H_p\) with polynomial \(p\)-loss. A pointwise same-support bound such as
   \[
   \mathcal S^2Y(s)\le C\beta^3 s^{-1}
   \]
   on the nested time intervals is sufficient. The files indicate this should come from the \(p=2\) critical step, a good time slice, and \(p=3\) propagation, but that chain must be written with the same spatial cutoff and the same Sobolev constant.

3. **Critical \(H_2\to H_3\) seed.**  
   The absorption step is
   \[
   H_3
   \le H_2^{1/2}H_4^{1/2}
   \le C\mathcal S H_2^{1/2}\bigl(D_2+r^{-2}H_2\bigr).
   \]
   Thus the small parameter is
   \[
   \gamma=\mathcal S H_2^{1/2}.
   \]
   The good-center volume cancellation must give \(\gamma\) small on the same component where the later iteration runs.

4. **Defect seed \(J_6\).**  
   For \(f=|E|\), the endpoint uses \(p_0=6\):
   \[
   J_6(t)=H_6(|E|)=\int \eta^2 a^4|E|^6.
   \]
   The route needs a propagated same-support \(J_6\) bound on \([t/2,t]\). After the curvature endpoint gives
   \[
   |aF|(s)\le C\beta s^{-1},
   \]
   the homogeneous defect equation has reaction coefficient controlled by \(aF\), so the \(E\)-iteration yields
   \[
   \|aE(t)\|_\infty
   \le
   C\delta (r^2/t)^{1/3}
   \]
   from \(J_6\). The regularized norm near \(E=0\) must be included in the energy derivation.

5. **Global \(Q\) evolution.**  
   The scalar recurrence itself does not use \(Q=\int |E|^2\). The terminal density bridge and topology-normalized smallness do. The needed input is the homogeneous evolution
   \[
   Q(t)\le e^{C\theta}Q(0),
   \]
   with constants compatible with the same metric-comparison bootstrap.

6. **Same-support bootstrap.**  
   The local Sobolev constant, volume factor, \(H_2\), \(Y\), and \(J_6\) must all be attached to the same macro-component and nested collars. The metric drift estimate from \(|aE|\) must keep the Sobolev and volume comparisons valid until the first-exit time. Without this same-support organization, the volume cancellation in \(\mathcal S^{2/p_0}\) and the \(J_6\) endpoint do not follow from the displayed formulas alone.

## 2. Continuation: the \(m=2\) single-\(\chi\) term

In `weighted_moser_and_continuation_repair.md`, equations (6.11)–(6.13) arise from the term
\[
\int P_p(W_m)*\chi \nabla^{m+1}\chi*\nabla U,
\qquad
W_m=\nabla^mU.
\]
After integrating one derivative off \(\nabla^{m+1}\chi\), the last line is
\[
-\int P_p(W_m)*\chi\nabla^m\chi*\nabla^2U.
\]
For \(m=2\), this contains
\[
I=\int \chi\,|\nabla^2\chi|\,|\nabla^2U|^p.
\]
Let
\[
W=\nabla^2U,\qquad B=\nabla^2\chi,\qquad
X_p=\int |W|^p,\qquad
D_p=\int \chi^2|\nabla W|^2|W|^{p-2}.
\]
This term is not controlled by plain Hölder from \(B\in L^q\) and \(W\in L^p\). It would ask for a higher unweighted \(L^{p q/(q-1)}\) norm of \(W\).

However, in dimension four it is controlled by the available weighted Sobolev estimate, if one inserts the missing interpolation step. Set
\[
u=\chi |W|^{p/2}.
\]
Then
\[
\|u\|_4^2
\le
C\mathcal S\bigl(p^2D_p+(1+r^{-2})X_p\bigr).
\]
Using \(B\in L^4\), supplied from the previous \((\nabla U,\nabla^2\chi)\) level,
\[
\begin{aligned}
I
&\le \|B\|_4
\left(\int \chi^{4/3}|W|^{4p/3}\right)^{3/4} \\
&\le \|B\|_4
X_p^{1/2}
\left(\int \chi^4|W|^{2p}\right)^{1/4} \\
&=
\|B\|_4 X_p^{1/2}\|u\|_4 \\
&\le
C\mathcal S^{1/2}\|B\|_4 X_p^{1/2}
\bigl(p^2D_p+(1+r^{-2})X_p\bigr)^{1/2} \\
&\le
\varepsilon D_p
+
C_{\varepsilon}\mathcal S p^2\|B\|_4^2(1+r^{-2})X_p .
\end{aligned}
\]
Thus the single-\(\chi\) term is not an obstruction at \(m=2\), but the proof must explicitly use this four-dimensional weighted interpolation. Equation (6.13) alone, without the displayed interpolation between \(X_p\) and \(\int \chi^4|W|^{2p}\), does not justify the estimate.

Wang’s Proposition 4.14 in the supplied paper states a different grouped outcome for the original local Ricci flow variable: after integrating the \(\Gamma_1,\Gamma_2,\Gamma_3\) group, the remaining exceptional term is
\[
\int |\nabla^m(\chi^2\mathrm{Rm})|^{p-2}
\left\langle
\nabla^m(\chi^2\mathrm{Rm}),
\,
\nabla^2\chi*\nabla^m\chi*\chi^2\mathrm{Ric}
\right\rangle .
\]
For \(m=2\), this is softer:
\[
\int |\nabla^2\chi|^2\,|U|\,|W|^{p-1},
\]
which closes by Hölder and Young using \(\|U\|_\infty\) and previous \(L^{2p}\) bounds for \(\nabla^2\chi\). This source passage indicates that the fully grouped Wang integration may replace the single-\(\chi\) expression. But the normalized shifted \(U\)-calculation in the supplied Codex file does not write the coefficient-level grouped identity. Therefore the self-contained continuation proof should either supply that grouped identity for the normalized \(U\)-equation, or retain the single-\(\chi\) term and estimate it by the four-dimensional interpolation above.

The induction does not need a new current unknown at \(m=2\) if this interpolation is inserted. The dependence remains on previous-level \(\nabla^2\chi\in L^4\), current \(W=\nabla^2U\in L^p\), and the weighted dissipation \(D_p\). There is no use of \(\nabla^3\chi\) outside the coupled \((\nabla^2U,\nabla^3\chi)\) pair.

## 3. Why \(a\mapsto a+\varepsilon\) is not automatic

Replacing \(a\) by \(a+\varepsilon\) changes the geometric problem in regions where \(a=0\). In the degenerate flow,
\[
\partial_tg=-2aE,
\]
those exterior collars are stationary. The weighted curvature variable
\[
U=a(\mathrm{Rm}+G)
\]
vanishes there, so large exterior curvature does not enter the weighted \(U\)-estimates.

For
\[
a_\varepsilon=a+\varepsilon,
\qquad
U_\varepsilon=a_\varepsilon(\mathrm{Rm}+G),
\]
one instead has
\[
U_\varepsilon=\varepsilon(\mathrm{Rm}+G)
\]
where \(a=0\). Uniform estimates for \(U_\varepsilon\) then require information on \(\varepsilon\,\mathrm{Rm}\) and its derivatives in the exterior region. Along the Ishida–LeBrun family, the route is designed to avoid any uniform exterior curvature input. A fixed \(\varepsilon>0\) also activates the flow everywhere:
\[
\partial_t\mathrm{Rm}
\sim
\varepsilon\Delta\mathrm{Rm}
+\varepsilon\,\mathrm{Rm}*\mathrm{Rm}
+\cdots
\]
outside the chosen supports. If \(|\mathrm{Rm}|\) is very large there, the factor \(\varepsilon\) does not by itself give a uniform bound for \(\varepsilon|\mathrm{Rm}|^2\), nor for higher derivative terms.

Thus strict parabolic regularization can be used only after proving estimates independent of \(\varepsilon\) and independent of exterior curvature quantities not present in the degenerate problem. The supplied files do not yet contain such estimates. A proof based on \(a+\varepsilon\) must show that the exterior terms either remain uniformly bounded, vanish in the \(\varepsilon\to0\) passage, or are separated from the active supports by estimates that do not depend on uncontrolled exterior curvature.

## 4. Sharp mathematical obligations still present

For the Moser part, the essential missing item is a same-support parabolic recurrence proof:
\[
\sup_{I_{k+1}}H_{p_k}
+\int_{I_{k+1}}\bigl(\|\nabla z_{p_k}\|_2^2+r^{-2}H_{p_k}\bigr)
\le
C p_k^N L_k\int_{I_k}H_{p_k},
\]
with \(L_k\) containing only dyadic time, \(r^{-2}\), and already-proved \(Y\)-bounds, not any term causing exponential-in-\(p_k\) growth. This must be paired with the \(H_3/Y\), \(J_6\), \(Q\), and metric-comparison inputs on the same supports.

For the continuation part, the \(m=2\) single-\(\chi\) expression can be handled by the displayed four-dimensional interpolation, or replaced by an exact Wang grouped identity if that identity is written for the normalized shifted \(U\)-equation. The regularization \(a+\varepsilon\) requires a separate uniform exterior-curvature argument; it is not supplied by the existing weighted estimates.