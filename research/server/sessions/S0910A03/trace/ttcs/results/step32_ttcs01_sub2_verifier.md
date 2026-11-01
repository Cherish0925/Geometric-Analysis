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

# Memo: two analytic points in the 4D normalized cutoff route

## Summary of what holds and what does not

- The mixed-weight identity and the spacetime interpolation engine in Part 1 are algebraically correct. The recurrence variable is the spacetime integral $\int_I H_{p}$, and it advances by the power $3/2$ per step with polynomial $p$-loss. This engine is sound. Its conclusion is contingent on several upstream quantities that the supplied files cite but do not derive.
- In Part 2, the $m=2$ term $\int \chi|\nabla^2\chi|\,|\nabla^2U|^p$ is genuinely different from the residual term Wang removes, and the grouped Wang integrations do **not** cancel it. It is nonetheless controllable, but only through the weighted 4D Sobolev estimate, not through the "coefficient times $\chi|W_2|^p$" reading printed in the Codex memo, which silently needs $\|\nabla^2\chi\|_\infty$ (unavailable). The induction does not need restructuring; its written justification for this single term does.
- The substitution $a\mapsto a+\varepsilon$ is not automatically harmless: it activates a full-strength Ricci-type flow on the frozen exterior where curvature is uncontrolled, and no uniform-in-$\varepsilon$ control exists there.

---

## Part 1. The Moser recurrence engine

### The chain that is valid

With $H_p=\int \eta^2 a^{p-2}\Phi^p$, $z_p=\eta\, a^{(p-1)/2}\Phi^{p/2}$, the following are correct term by term.

1. **Weight identity.** $z_p^2=a^{p-1}\Phi^p$ and $(a^{p-2}\Phi^p)^{1/2}=a^{(p-2)/2}\Phi^{p/2}$ multiply to $a^{(3p-4)/2}\Phi^{3p/2}$, whose $a$-exponent is exactly $3p/2-2$. Hence by Cauchy–Schwarz
$$
H_{3p/2}\le H_p^{1/2}\,\|z_p\|_4^2 .
$$

2. **Correct 4D embedding.** In dimension four $2n/(n-2)=4$, so the valid inequality is
$$
\|z_p\|_4^2\le S\big(\|\nabla z_p\|_2^2+r^{-2}\|z_p\|_2^2\big),
$$
not the two-dimensional Ladyzhenskaya product $\int u^4\lesssim(\int|\nabla u|^2)(\int u^2)$ that appears in the step31 interpolation note §6. Since $a\le1$, $\|z_p\|_2^2\le H_p$.

3. **Spacetime interpolation.** Combining these at each time slice and pulling $\sup_I H_p^{1/2}$ out of the time integral gives exactly the form named in the task,
$$
\int_I H_{3p/2}\le (\sup_I H_p)^{1/2}\,S\int_I\big(\|\nabla z_p\|_2^2+r^{-2}H_p\big),
$$
and with $\|\nabla z_p\|_2^2\le Cp^2(D_p+r^{-2}H_p)$, $D_p=\int a^{p-1}\Phi^{p-2}|\nabla\Phi|^2$,
$$
\int_I H_{3p/2}\le (\sup_I H_p)^{1/2}\,Cp^2 S\int_I\big(D_p+r^{-2}H_p\big).
$$

4. **Closure into a $3/2$-recurrence.** The energy inequality (Codex 5.5) supplies $\sup_I H_p$ and $\int_I D_p$ in terms of $\int_{I'}H_p$ once the reaction is absorbed, so
$$
\int_I H_{3p/2}\lesssim L\,\big(\int_{I'}H_p\big)^{3/2}.
$$
For $p_k=3(3/2)^k$ the product of per-step constants converges because $\sum_k(\log p_k)/p_k<\infty$ (with $p_k\sim(3/2)^k$ this is $\sum_k k(2/3)^k$), so the $p$-loss is polynomial and the iteration reaches $L^\infty$.

5. **Endpoint.** $K_p^{1/p}=\big(\int(a^{1-2/p}\Phi)^p\big)^{1/p}\to\|a\Phi\|_\infty$. This is the weighted supremum $\|aF\|_\infty\sim|a\operatorname{Rm}|_\infty$ that the route needs. The "$\|a^{1/2}\Phi\|_\infty$" written in the step31 note §7.5 was the wrong exponent; the Codex memo's $\|a\Phi\|_\infty$ is right.

This engine is correct. The earlier "half-power" concern is an artifact of comparing $\|z_p\|_3^3$; the recurrence never uses that object.

### Upstream inputs the engine still consumes

The recurrence is valid **given** the following, none of which are derived in the supplied files:

- **Reaction coefficient.** Absorption of $R_p=\int a^{p-1}F^{p+1}$ uses the decomposition $R_p\le\varepsilon(D_p+r^{-2}H_p)+C_\varepsilon p^N S^2Y\,H_p$ with $Y=\int aF^3$. This needs $S^2Y$ small at every level, i.e. the good-center selection giving $\hat H_2\le \operatorname{Vol}\cdot\Lambda\bar K$ and a uniform mean-curvature energy $\bar K$. The one remaining valid reaction form is with the $a^{p-1}$ weight kept; enlarging via $a\le1$ to $a^{p-2}F^{p+1}$ destroys the Hölder split (the produced weight $a^{p-1}$ cannot control the lighter $a^{p-2}$).
- **Curvature seed.** The $p_0=3$ same-support positive-time bound $S^2H_3(s)\le C\beta^3/s$ (giving $\|aF\|_\infty\le C\beta/t$). Cited, not proved here.
- **Defect route.** For $\Phi=|E|$ the step $|\nabla\Phi|\le|\nabla\operatorname{Rm}|/\Phi\le|\nabla\operatorname{Rm}|$ printed in the step31 note §4 does not hold; the defect iteration requires its own dissipation $\int a^{p-1}|E|^{p-2}|\nabla E|^2$, a Kato inequality, and regularization near $\{E=0\}$. With that in place, $p_0=6$ needs the $J_6\le C\delta^6\operatorname{Vol}$ persistence, and the metric-comparison endpoint needs $Q=\int|E|^2$ evolving homogeneously.
- **Uniform collapse-adapted Sobolev.** $S\asymp r^4/\operatorname{Vol}(B_r)$ must hold uniformly over $I$ under the moving metric $g(t)$; this itself rests on metric equivalence, which rests on $|aE|\in L^1_t$ — the first-exit bootstrap closing on itself.

Sharp obligation for Part 1: the recurrence engine is complete; the remaining work is the $H_3$/$Y$ seed with uniform smallness of $S^2Y$, the correct defect dissipation/Kato identity, and $J_6$/$Q$ persistence — the engine does not manufacture these.

---

## Part 2. The continuation induction at $m=2$

### The single-$\chi$ term is not a Wang cancellation term

At $m=2$ the descendant in Codex (6.11), the last line, is
$$
\int P_p(W_2)*\chi\,\nabla^2\chi*\nabla^2U,\qquad W_2=\nabla^2U,\ \nabla^2U=W_2,
$$
so its integrand is $\chi\,\nabla^2\chi\,|W_2|^p$. Contrast with the residual Wang eliminates in Proposition 4.14, which is $\int|\nabla^m(\chi^2\mathrm{Rm})|^{p-2}\langle\cdots,\nabla^2\chi*\nabla^m\chi*\chi^2\mathrm{Rm}\rangle$: there the top-order factor enters to power $p-1$ and the last factor $\chi^2\mathrm{Rm}$ is an $L^\infty$-bounded low-order quantity, so plain Hölder with two cutoff derivatives in $L^q$ closes. In the shifted variable the "curvature" factor is $\nabla^2U=W_2$ itself, entering to the full power $p$, and there is only one cutoff derivative $\nabla^2\chi$ to spare. Wang's grouped integrations therefore do not remove or replace this term; it is structurally new.

### It is controllable by the weighted Sobolev, not by an $L^\infty$ coefficient

The Codex phrase "for $m=2$, it is a coefficient times $\chi|W_2|^p$" implicitly asks for $\|\nabla^2\chi\|_\infty$, which the coupled induction deliberately does not carry. Plain Hölder $\int|\nabla^2\chi||W_2|^p\le\|\nabla^2\chi\|_s\|W_2\|_{ps'}^p$ forces $s'=1$, $s=\infty$, and does not go through.

The correct control uses (6.13) with $w=\chi|W_2|^{p/2}$, where $\|\nabla w\|_2^2\le C(\|\nabla\chi\|_\infty^2\|W_2\|_p^p+p^2\mathcal D_{2,p})$ (only the base $\|\nabla\chi\|_\infty$ enters), hence
$$
\|w\|_4^2\le CSp^2\big(\mathcal D_{2,p}+(1+r^{-2})\|W_2\|_p^p\big),\qquad \mathcal D_{2,p}=\int\chi^2|\nabla W_2|^2|W_2|^{p-2}.
$$
Writing $\chi|W_2|^p=w\,|W_2|^{p/2}$ and applying Hölder with exponents $(4,4,2)$,
$$
\int\chi\,\nabla^2\chi\,|W_2|^p=\int \nabla^2\chi\, w\, |W_2|^{p/2}\le \|\nabla^2\chi\|_4\,\|w\|_4\,\|W_2\|_p^{p/2}.
$$
Young then gives
$$
\int\chi\,\nabla^2\chi\,|W_2|^p\le \varepsilon\,\mathcal D_{2,p}+C\,p^2 S\,\|\nabla^2\chi\|_4^2\,\|W_2\|_p^p ,
$$
which is exactly the Grönwall form. The cutoff exponent is the fixed number $4$, so no $p$-dependent exponent regression appears, and $\|\nabla^2\chi\|_4$ is time-uniformly finite from the previous induction level $(\nabla U,\nabla^2\chi)$. 

The higher orders $m\ge3$ are easier: there $\nabla^2U$ is a **lower**-order quantity, bounded in $L^\infty$ by earlier levels, and $\nabla^m\chi$ sits one order below the current cutoff $\nabla^{m+1}\chi$, so the term reduces to $\int\chi\nabla^m\chi\,\nabla^2U\,|W_m|^{p-1}\le C\|\nabla^m\chi\|_p\|\nabla^2U\|_\infty\|W_m\|_p^{p-1}$, closing by plain Hölder. Thus $m=2$ is the unique delicate order, exactly as the task suspected.

Conclusion for Part 2: the induction structure is intact and does not need to be changed; the written justification of this single $m=2$ term must be replaced by the weighted-Sobolev + $L^4$-Hölder + Young argument above. Note this resolves only the specific term the task names; the full coupled estimate still requires the complete term-by-term accounting flagged by the step31 integration memo (products such as $\nabla^{m+1}\chi*\nabla U*|W_m|^{p-1}$ each need explicit treatment), and my resolution of one term does not by itself close the coupled Grönwall.

### Why $a\mapsto a+\varepsilon$ is not automatically harmless

With $a_\varepsilon=\chi^2+\varepsilon>0$ everywhere, the flow $\partial_t g_\varepsilon=-2a_\varepsilon(\operatorname{Ric}_\varepsilon+g_\varepsilon)$ becomes active on the **entire** manifold, including the exterior $\{\chi=0\}$ where the intended degenerate flow is frozen. The route's control of curvature lives only on the macro-supports $B_{6r}(p_j)\subset\operatorname{supp}\chi$ (good-center selection, $H_3$, $J_6$ seeds). Off the supports the initial curvature is uncontrolled — precisely the regime where Ishida–LeBrun geometries carry large concentrations.

Two consequences:

- The exterior now runs a genuine Ricci-type flow at speed $\varepsilon$ driven by uncontrolled $\operatorname{Ric}$. The Moser machinery (which needs the local seeds and the small-$S^2Y$ absorption) cannot be run there, so the $\varepsilon$-solutions may develop large curvature or become singular in the exterior before $T$, leaving nothing to pass to the limit.
- Even where solutions persist, the reaction $\int a_\varepsilon^{p-1}F^{p+1}$ over the exterior is $\varepsilon^{p-1}\int_{\mathrm{ext}}F^{p+1}$, and the $\varepsilon\to0$ estimate degenerates exactly at $\{\chi=0\}$, where $a_\varepsilon\Delta-a\Delta=\varepsilon\Delta$ is a full-strength operator changing the character of the solution on the frozen region.

So the "standard porous-medium regularization" reading understates the situation: porous-medium regularization is standard when degeneracy of the principal operator is the only issue and the data is globally controlled; here the exterior data is globally uncontrolled by design. The structure-respecting existence route is the degenerate one that keeps the exterior frozen — Yang's LRF short-time existence for $\partial_t g=-2\chi^2\operatorname{Ric}$, with the normalization $-2\chi^2 g$ entering only as a bounded zeroth-order change (as continuation §8 argues), so no $a+\varepsilon$ is needed. The sharp obligation is to invoke and verify that degenerate existence directly, or to prove uniform-in-$\varepsilon$ exterior control, which does not hold in general.

---

## Sharp next proof obligations

1. **Part 1 (engine complete, seeds open).** Supply the same-support positive-time $H_3$/$Y$ seed with uniform $S^2Y$ smallness through the good-center selection and uniform $\bar K$; supply the correct $\Phi=|E|$ dissipation/Kato identity together with $J_6$ persistence and $Q$ evolution; and confirm the collapse-adapted Sobolev constant is uniform over $I$ under $g(t)$ via the metric-equivalence bootstrap.

2. **Part 2 (term controllable, wording and existence open).** Replace the "coefficient times $\chi|W_2|^p$" reading with the weighted-Sobolev estimate above for the $m=2$ term, then complete the full term-by-term coupled $(X_p,Z_p)$ accounting (the resolution of this one term does not close the coupled Grönwall); and establish short-time existence keeping the exterior frozen (degenerate LRF plus bounded normalization) rather than through $a+\varepsilon$, or prove uniform-in-$\varepsilon$ exterior curvature control.

These are the two points where the analytic chain currently rests on inputs not present in the supplied files. The Moser interpolation identity, the spacetime recurrence, the endpoint $\|a\Phi\|_\infty$, the highest-order connection-change count, and the $m=2$ term's controllability are the pieces that are correct as they stand.