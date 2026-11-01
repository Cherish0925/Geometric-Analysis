# TTCS Independent Branch Record

```json
{
  "step_id": 20,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A03/workspace/notes/step19_p4_threshold_and_degenerate_moser.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/scripts/verify_step20_weighted_moment_hierarchy.py"
  ]
}
```

## Task

Test a potentially decisive simplification of the Step-20 cutoff-flow first-exit. Given the weighted curvature moments H_q and defect moments J_m in the supplied note, determine whether any pointwise connection or Hessian-a control is actually needed for the zero-order smoothing theorem and metric comparability. Specifically: all Hess(a) terms in the q=2,3 and high-exponent weak estimates are integrated by parts to leave only |da|^2/a and localization gradients; relative Sobolev and fixed-domain overlap then depend only on metric comparability, while metric comparability follows from the integrable pointwise aE estimate. If this is sound, the prior target |chi nabla(aE)| may be unnecessary for the first-exit itself. Check every place it could re-enter: local critical-energy persistence, H_2-to-H_3, curvature and defect Moser recurrences, triangular unweighted Q, preservation of cutoff-gradient bounds, moving volume/balls, and smooth continuation of the normalized cutoff flow. Read Wang Theorem 4.1/Proposition 4.9 and decide whether a terminal bound on |a Rm| (plus fixed smooth cutoff) extends to the normalized flow with -2ag, or what extra qualitative—not dimension-uniform quantitative—derivative input is actually needed. Also derive the curvature high-exponent recurrence from H_3 to |aRm| and verify its scaling C gamma/t. Give a rigorous mathematical memo; do not assume full finite-neighbor implementation or conclude Yau 26.

## Output

## Verifier memo — is the quantitative $|\chi\nabla(aE)|$ control actually load-bearing for the zero-order cutoff-flow first-exit?

### Summary judgment

Working through the seven places where a derivative estimate could re-enter, I find the tested simplification **sound as a structural statement**: given the two *zero-order* pointwise inputs — the localized curvature regularity $|a\operatorname{Rm}|\le C\gamma/t$ and the defect bound (3.3) $|aE|\le C\delta(1+r^2/t)^{1/3}$ — the entire quantitative first-exit closes using only metric comparability and Sobolev persistence, both of which follow from the *time-integrability of $|aE|$*. The prior $\delta$-linear, dimension-uniform Bernstein/connection-drift statement $|\chi\nabla(aE)|\le C_p\delta t^{-1/2}(r^2/t)^{2/p}$ (Step 19 $D_p$, "Step 5") does **not** re-enter any of the quantitative estimates. The one genuinely required derivative input is *qualitative* smooth continuation of the flow, which is Wang's Theorem 4.1 bootstrap adapted to the extra $-2ag$ term; its constants need only be finite, not dimension-uniform or $\delta$-linear.

Two remaining unproved inputs are both *zero-order* parabolic regularity statements, not the removed derivative estimate. I do not assume the finite-neighbor implementation and draw no conclusion about Yau 26.

---

### 1. The comparability mechanism is genuinely first-order-free

The metric drift is
$$
\Big|\log\frac{g_t(v,v)}{g_0(v,v)}\Big|\le 2\int_0^t |aE|_{g_s}(v)\,ds .
$$
With (3.3), $\int_0^{\theta r^2}|aE|\,ds\le \tfrac32 C\delta\,\theta^{2/3}r^2$ (finite because the time exponent $1/3<1$), matching Step 19 eq. (1) at $p=6$. This is the only integral needed for
$$
e^{-\epsilon}g_0\le g_t\le e^{\epsilon}g_0,\qquad \epsilon = C\delta\theta^{2/3}.
$$
Everything downstream that "sees" the flow only through the metric is then transported by this bi-Lipschitz equivalence:

- $|\nabla_{g_t}\chi|^2=g_t^{ij}\partial_i\chi\,\partial_j\chi\le e^{2\epsilon}|\nabla_{g_0}\chi|^2\le e^{2\epsilon}L^2/r^2$ — a **first-order** cutoff quantity, controlled by comparability plus the fixed $\chi$. No connection enters because $\chi$ is a scalar; only $g_t^{ij}$ appears.
- The relative Sobolev inequality $\|f\|_{L^4}\le A(\|\nabla f\|_2+r^{-1}\|f\|_2)$ transports with $A_t\le e^{Cn\epsilon}A_0$; it does **not** require $\operatorname{Ric}_{g(t)}\ge-3g_t$ to persist, only the $t=0$ inequality plus comparability, since it is a metric statement distorted by bounded factors.
- Fixed-cover overlap and volume ratios are bi-Lipschitz invariants.

This is exactly the mechanism of Wang's Prop. 3.12 (`2\int_0^{t_0}|\chi^2\operatorname{Ric}|_\infty\le\epsilon/2 \Rightarrow d_{TL}\le\epsilon/2`) and Prop. 4.9 ("the metrics $g(t)$ are uniformly equivalent"). The self-consistency is the usual first-exit ordering: provisionally assume comparability with constant $e^\epsilon$, obtain $|aE|\le C\delta(\cdot)$, integrate to a log-drift $<\epsilon/2$, strictly improving the provisional constant. No circularity.

---

### 2. The seven re-entry points, each checked

**(i) Weak curvature/defect estimates never carry $\operatorname{Hess}_{g_t}\chi$ pointwise.** Every $\nabla^2a$ source — $(\nabla^2a)*E$ in the curvature variation (A01 §4) and in the defect equation (7.1) — is integrated by parts once on the closed support (no surface term). The residue is
$$
\int\eta^2|\nabla a|\,F^{q-1}|\nabla H|\le \varepsilon\!\int\!\eta^2 aF^{q-2}|\nabla H|^2+C_\varepsilon\!\int\!\eta^2\tfrac{|\nabla a|^2}{a}F^q,
\qquad \tfrac{|\nabla a|^2}{a}=4|\nabla\chi|^2 .
$$
The weight in the Young split is exact: $|\nabla a|F^{q-1}|\nabla H|=(a^{1/2}F^{(q-2)/2}|\nabla H|)(a^{-1/2}|\nabla a|F^{q/2})$, first factor squared $=aF^{q-2}|\nabla H|^2$ (the dissipation from $a\Delta H$), second $=\tfrac{|\nabla a|^2}{a}F^q$. Thus only the **first-order** fixed quantity $4|\nabla\chi|^2$ survives. The $\nabla E$, $\nabla F$ produced by the same integration by parts are absorbed by the same dissipation via the geometric contraction $\nabla E=\operatorname{contr}(\nabla\operatorname{Rm})$, $|\nabla F|\le|\nabla H|$ (this uses $\nabla g=0$, so it is exact, not a persistence hypothesis). **Consequence:** the pointwise cutoff-Hessian and hence the connection drift are not used here. This is the decisive structural point and it holds.

**(ii) $H_2\!\to\!H_3$.** $\int F v_2^2=\int\eta^2aF^3=H_3$; Sobolev gives $H_3\le C\gamma(\int|\nabla v_2|^2+r^{-2}H_2)$. Integrating the $q=2$ inequality and absorbing for small $\gamma$ yields $\int_0^tH_3\,ds\le C\gamma H_2(0)$ — Sobolev + fixed cutoff only.

**(iii) Curvature and defect Moser recurrences.** Purely energy-type: dissipation $\int a|\nabla H|^2$, fixed cutoff remainders, curvature reaction absorbed by $\gamma$-smallness. The evolving measure enters as the bounded multiplier $\partial_t d\mu=-\operatorname{tr}(aE)d\mu$, $|\operatorname{tr}(aE)|\le C|aE|$ — a **zero-order** factor, not a derivative. The weighted cubic Hölder is exact: $Fz_m^2=(aF^3)^{1/3}(a^{-1/3}z_m^2)$, and the $3/2$-power of the second factor is $\eta^2a^{3m/2-2}|E|^{3m/2}=J_{3m/2}$, with $J_{3m/2}\le J_m^{1/2}J_{2m}^{1/2}$ (Cauchy–Schwarz, checked directly). The Young step $\int Fz_m^2=(A^4H_3J_m)^{1/3}X_m^{2/3}\le\varepsilon X_m+C\varepsilon^{-2}A^4H_3J_m$ matches the script's AM–GM and (3.2). No $\nabla U$ input.

**(iv) Triangular unweighted $Q=\int_M|E|^2$.** (7.2)–(7.5): the potential $a|\operatorname{Rm}|\,|E|^2$ is absorbed by critical Sobolev with $\beta_\ell=S_\ell\|F\|_2$ small, itself supplied by the critical-energy persistence (item i). This uses $\|\operatorname{Rm}\|_2=O(\sqrt\varepsilon)$, a zero-order energy quantity, not a derivative. The correction over the discarded additive $\varepsilon\!\int a|\nabla\operatorname{Rm}|^2$ form is well taken: the integrated dissipation can be $O(A)$, so a triangular finite-neighbor Grönwall is the correct route to preserve $Q(T)/A\to0$.

**(v) Cutoff-gradient preservation.** Only $|\nabla_{g_t}\chi|$ is used, transported by comparability (item 1). $\operatorname{Hess}_{g_t}\chi$ would require $|\Gamma(t)-\Gamma(0)|\le\int_0^t|\nabla U|$ — but it is never used pointwise (item i). So the Step-19 cutoff-Hessian drift bound (3) is no longer a needed input.

**(vi) Moving volumes/balls.** Bi-Lipschitz distance comparison $B^{g_0}_{e^{-\epsilon}r}\subset B^{g_t}_r\subset B^{g_0}_{e^{\epsilon}r}$ and $\operatorname{Vol}_{g_t}\approx\operatorname{Vol}_{g_0}$; Whitney radii $\ell=cr\chi_0$ are defined by fixed $\chi$. Comparability only.

**(vii) Smooth continuation.** Treated in §3.

Every point resolves through zero-order pointwise bounds + comparability + fixed cutoffs. None reintroduces the quantitative Bernstein estimate.

---

### 3. Wang Theorem 4.1 / Prop. 4.9 for the normalized velocity $-2aE$

Wang's Theorem 4.1 is precisely the statement that the **zero-order** bound $|\chi^2\operatorname{Rm}|_\infty\le C$ suffices for smooth continuation; the derivative bounds $|\nabla^m(\chi^2\operatorname{Rm})|_\infty$ (Lemmas 4.10–4.11, Props. 4.13–4.14) are *generated* by the parabolic bootstrap, not assumed. Prop. 4.9 derives $|\nabla\chi|_\infty$ and the Sobolev constant from metric equivalence alone.

Extending to $-2aE=-2\chi^2\operatorname{Ric}-2\chi^2 g$: the extra $-2ag$ term linearizes to
$$
D\operatorname{Rm}(-2ag)\sim(\nabla^2 a)\owedge g+a\,\operatorname{Rm},
$$
so the curvature-evolution bootstrap gains a source of type $(\nabla^{m+2}a)\owedge g$ — a **curvature-free, lower-order** term. In the $L^p$ energy for $\nabla^m\operatorname{Rm}$ it contributes $C|\nabla^m\operatorname{Rm}|_p^{p-1}|\nabla^{m+2}\chi^2|_p$, and Wang's cutoff-derivative chain (Lemma 4.6, generalized to $\chi^2E$) already controls $|\nabla^k\chi|_p$ for all $k$ through a benign self-coupling $\nabla^k(\chi^2 g)=(\nabla^k\chi^2)g$. The Grönwall/induction of §4 therefore still closes. Two points to keep in view, both routine:

- Apply the extension on $[t_0,T)$ with $t_0>0$: the input $|a\operatorname{Rm}|\le C\gamma/t_0$ is finite there; $[0,t_0]$ is covered by short-time existence of the local Ricci flow perturbed by the smooth bounded reaction $-2\chi^2 g$ (a Lipschitz zeroth-order perturbation of Deane Yang's LRF, so short-time existence is unaffected).
- A01 §2's insistence on keeping the *full* velocity $-2aE$ (rather than splitting $\operatorname{Ric}$ and $g$) is the correct bookkeeping: the source $(\nabla^2a)*E$ then vanishes at an exact negative-Einstein metric ($E=0$ stationary even where $\nabla a,\nabla^2 a\ne0$), whereas the split creates artificial $(\nabla^2a)*g$ pieces.

**Conclusion for the task's direct question:** a terminal $|a\operatorname{Rm}|$ bound plus a fixed smooth $\chi$ *does* extend to the normalized flow. The extra required input is only the *qualitative* self-generated derivative regularity of Wang's bootstrap (constants may depend on $T$, $t_0$, initial data, $|\nabla^k\chi|$). It is not the $\delta$-linear, dimension-uniform Bernstein estimate, and it does not feed the quantitative first-exit.

---

### 4. The $H_3\to|a\operatorname{Rm}|$ recurrence and the $C\gamma/t$ scaling

**Launch integrability.** With $v_q=\eta a^{(q-1)/2}F^{q/2}$, the exponent identities $v_q^4=\eta^4a^{2q-2}F^{2q}$ and $Fv_q^2=\eta^2a^{q-1}F^{q+1}$ hold (script `verify_step20_weighted_moment_hierarchy.py`, reproduced by hand). At $q=2$, absorbing the Sobolev reaction for small $\gamma=A^2\|F\|_2$ gives $\int_0^tH_3\le C\gamma H_2(0)$. At $q=3$, the reaction is $H_4=\int Fv_3^2$, absorbed to $H_3'\le Cr^{-2}H_3$. Mean-value over $[t/2,t]$:
$$
H_3(t)\le \frac{2e^{C\theta}}{t}\int_0^tH_3\le \frac{C\gamma H_2(0)}{t}.
$$
Since $A^4H_2(0)\le A^4\|F\|_2^2=\gamma^2$, this gives the boxed $A^4H_3(t)\le C\gamma^3/t$ (2.3). I confirm each step.

**Doubling to $L^\infty$.** From the absorbed inequality
$$
\frac{d}{dt}H_q+c\!\int|\nabla v_q|^2\le Cq^2r^{-2}H_q ,
$$
the spatial $L^4$ Sobolev output $\|v_q\|_{L^4}^2\ge H_{2q}^{1/2}$ combined with $\sup_{[t/2,t]}$ and a $1/t$ factor per level runs the parabolic Moser doubling $H_q\to H_{2q}$. As $q\to\infty$, $(a^{q-2}F^q)^{1/q}\to aF$, so the iteration outputs $\|aF\|_{L^\infty(t/2,t)}$. The terminal scaling is
$$
|a\operatorname{Rm}|\le \frac{C\,\gamma}{t}\quad(\text{single power of }t^{-1}),
$$
which coincides *structurally* with Wang's Theorem 6.3, $|\chi^2\operatorname{Rm}|_\infty\le \bar C\,t^{-1}[t|\nabla\chi|_\infty^2+1]^{4/n+2}\beta$ under the exact identification $\beta=A^2\|\operatorname{Rm}\|_{n/2}=\gamma$ ($n=4$, $L^2$ critical). The launch moment also matches Wang p.98–102: his $\int\chi^2|\operatorname{Rm}|^{n/2+1}\le CA^{-n}t^{-1}(\cdot)^2$ is in $n=4$ exactly $\int\chi^2|\operatorname{Rm}|^3\le CA^{-4}t^{-1}$, i.e. the note's $H_3\le C\gamma^3A^{-4}/t$ up to the extra smallness factor $\gamma^3$. The robust, cross-checked feature is the $1/t$ power and the proportionality to $\gamma$; the precise power of $\gamma$ (the note's launch carries $\gamma^3$, Wang's terminal carries $\gamma^1$) affects only constants and, since $\gamma\ll1$, does not alter the bound $|a\operatorname{Rm}|\le C\gamma/t$.

---

### 5. What genuinely remains unresolved, and one place to watch

The derivative-independence is a *conditional structural* result: it removes the Bernstein estimate from the required inputs, leaving two **zero-order** parabolic regularity statements as the substance still to be proved (both flagged in the notes, neither a corollary of Wang or Li as published):

1. Localized degenerate curvature regularity $|a\operatorname{Rm}|\le C\gamma/t$ from small relative $L^2$ energy under $\partial_t-\chi^2\Delta$ on the finite-neighbor family — the localized analogue of Wang Thm 6.3. A01 §6 correctly notes the all-exponent critical absorption threshold $C(q)\beta_\ell<c$ worsens with $q$, so a fixed supercritical $q_0$ followed by a De Giorgi/Moser mean value (Li's structure: $L^2$ persistence $\to L^3$ potential $\to$ linear step) is the sound route; this remains a zero-order statement.
2. The localized zero-order defect Moser giving (3.3), still conditional on writing the nested finite-neighbor recurrence with the evolving geometry.

One place a reader should verify carefully: the comparability integral uses $|aE|_{g_s}$ measured in the *evolving* metric, and (3.3) is a $g_s$-relative bound. The first-exit self-consistency (provisional $e^\epsilon$ comparability $\to$ (3.3) $\to$ improved comparability) is correct, but it depends on (3.3) holding uniformly on $[0,T_*)$ with a constant independent of the provisional comparability constant except through $e^{Cn\epsilon}$ factors in $A_t$. The two zero-order targets must be stated with constants tracking exactly this dependence (finite-neighbor count $N$, doubling ratio $C_V$, cutoff constants $L,c$, tensor type), as the notes acknowledge. Nothing here requires $|\chi\nabla(aE)|$.

**Net scientific value:** the tested reduction is correct — the quantitative connection/Hessian derivative estimate is eliminable from the first-exit, replaced by (a) comparability from integrable $|aE|$, (b) integration by parts of every $\nabla^2a$, and (c) Wang's qualitative bootstrap for smooth continuation of the $-2aE$ flow. The unfinished mathematics is concentrated in two localized zero-order parabolic theorems and the finite-neighbor bookkeeping, which I have not assumed proved.