# TTCS Independent Branch Record

```json
{
  "step_id": 56,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step40_m2_coupled_continuation_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A03/workspace/notes/step45_coordinate_tensor_ledger_and_regularized_closure.md",
    "Sessions/S0910A01/workspace/notes/step43_H_WU_resolution_weighted_evolution.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Attack the earliest positive-time continuation interface for the exact cutoff flow, not the start theorem. On a fixed smooth terminal slab [tau,T*) assume sup|U|<K, metric bilipschitz equivalence, fixed smooth chi, and finite initial norms at tau, where T=Rm+g∧g/(2(n−1)), U=chi^2 T. Verify in detail the m=1 coupled pair (U_1=∇U,C_2=∇²chi), then the unweighted T_1=∇T estimate. List every highest-order term, especially chi C_3 U, chi C_2 U_1, dchi C_2 U, ∇³a T, and connection variation; perform the needed signed integrations by parts and state exact L^p inequalities. Determine whether any estimate divides by chi, needs unweighted pointwise T, introduces a ratio of regularization parameters, or fails near the small-chi collar. Ground the answer in the attached Step 40/44/45 notes and correct them if needed.

## Output

# Verification Memo — m=1 continuation layer for the exact cutoff flow

Prepared in a clean context. I reconstructed the m=1 pair $(U_1,C_2)$ and the subsequent $T_1=\nabla T$ estimate independently from the flow definition, then compared line‑by‑line with Steps 40, 44, 45 (and A01's Step 43). The m=1 layer as I reconstruct it holds, and it avoids each of the four pitfalls you named. Below are the exact term-by-term inequalities, the mechanism that makes each pitfall disappear, and several places where the notes should be made sharper for a self-contained m=1 argument.

Throughout: $a=\chi^2$, $E=\operatorname{Ric}+g$, $T=\operatorname{Rm}+G$, $U=aT$, $\partial_t g=-2aE=-2\operatorname{Ric}(U)$, $C_k=\nabla^k\chi$, $U_j=\nabla^jU$, $T_j=\nabla^jT$. Standing hypotheses: $\sup_{M\times[\tau,T_*)}|U|\le K$, bilipschitz metrics, fixed smooth $\chi$ (so $C_1=d\chi\in L^\infty$ and all $\|C_k\|_\infty$ are finite data), finite norms at $\tau$, $T_*<\infty$. The seed $T=T_0\in L^q$ for every finite $q$ is Step 44's estimate, which I also checked (see §5).

---

## 1. Two identities that carry the whole argument

Both are exact and division‑free; every apparent division by $\chi$ collapses through them.

**(I) Perfect‑square gradient identity.** $\nabla a=2\chi C_1$, hence
$$\frac{|\nabla a|^2}{a}=\frac{4\chi^2|C_1|^2}{\chi^2}=4|d\chi|^2 ,$$
bounded on all of $M$ including where $\chi\to0$. The $\chi^2$ in the denominator is exactly cancelled by the $\chi^2$ carried by $|\nabla a|^2$ because $a$ is a square.

**(II) Weighted‑to‑current conversion.** From $U=\chi^2T$,
$$U_1=\nabla(\chi^2 T)=2\chi C_1\,T+\chi^2 T_1\ \Longrightarrow\ \boxed{\ \chi^2 T_1=U_1-2\chi C_1\,T\ }.$$
Both right‑hand pieces are usable: $U_1=V$ is the current unknown, and $\chi C_1\,T$ has bounded coefficient $\chi C_1$ times $T\in L^q$. **No formation of $T=U/\chi^2$ occurs.** This is the $\chi^2/b=1$ specialization of Step 45 (4.4)/(2.2); keeping the coefficient in $B$-notation until allocation is exactly what preserves the cancelling $\chi^2$.

These two identities are the reason no estimate below divides by $\chi$.

---

## 2. The m=1 weighted pair $(U_1,C_2)$

Set $V=U_1$, $Z=C_2$, $P(V)=|V|^{p-2}V$, $D^U_{1,p}=\int\chi^2|\nabla V|^2|V|^{p-2}$. Differentiating the division‑free $U$-equation (Step 45 (2.3)) once, the highest‑order families at $m=1$ are $B_1U_2$, $B_2V$, $B_3U$, $B_1B_1T_1$, $B_2B_1T_0$, $U*V$, the spatial commutator $a\nabla\!\operatorname{Rm}*U$, the curvature commutator $a\operatorname{Rm}*V$, and connection variation $U_1*U$. Term-by-term:

**(a) Principal and first‑cutoff drift** (from $a\Delta U_1$ integrated once, plus $B_1U_2=2\chi C_1*\nabla V$):
$$\Big|\int \chi C_1\,\nabla V\,P(V)\Big|\le\varepsilon D^U_{1,p}+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p,$$
using identity (I). Collar‑stable: the $\chi$ pairs into $\chi^2|\nabla V|^2$.

**(b) $\chi C_3\,U$ (the top cutoff jet, $=\nabla^3a$ top piece $\times U$).** With $C_3=\nabla C_2$, one signed integration by parts gives exactly three descendants:
$$\int P(V)\,\chi C_3\,U=-\!\int \nabla P(V)\,\chi C_2 U-\!\int P(V)\,d\chi\,C_2 U-\!\int P(V)\,\chi C_2\,V,$$
because $\nabla U=U_1=V$. Then
- $\displaystyle\Big|\int\nabla P(V)\,\chi C_2 U\Big|\le\varepsilon D^U_{1,p}+C_{p,\varepsilon}K^2\!\int|Z|^2|V|^{p-2}\le \varepsilon D^U_{1,p}+C_{p,K}(\|Z\|_p^p+\|V\|_p^p)$;
- $\displaystyle\Big|\int P(V)\,d\chi\,C_2 U\Big|\le K\|d\chi\|_\infty\!\int|Z||V|^{p-1}\le C_{p,K,r}(\|Z\|_p^p+\|V\|_p^p)$;
- the third is the term you listed as $\chi C_2 U_1$ (here $U_1=V$), treated in **(c)**.

Every appearance of the current jet $Z$ here is at exponent $p$ only. No $\|Z\|_{2p}$ is invoked — this is the point where Step 39's exponent ascent is removed.

**(c) $\chi C_2\,V$ = signed Hessian** (arises both as the third descendant of (b) and directly from $B_2V$). This is $\int\chi(\nabla_i\nabla_j\chi)B^{ij}(V)$ with $|B(V)|\le C_p|V|^p$, $|\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|$. The decisive step is a **second** integration by parts writing $C_2=\nabla C_1$:
$$\int\chi(\nabla_iC_1{}_j)B^{ij}(V)=-\!\int (d\chi)(d\chi)B(V)-\!\int\chi\,(d\chi)\,\nabla B(V),$$
$$\Big|\cdots\Big|\le \varepsilon D^U_{1,p}+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.$$
This converts the current unknown $C_2=Z$ into $C_1=d\chi\in L^\infty$ (fixed data) plus dissipation. **$\|C_2\|$ is not used at any exponent in this term.** Collar‑stable.

**(d) $B_1B_1T_1$.** By identity (II), $B_1B_1T_1=4C_1C_1(\chi^2T_1)=4C_1C_1\big(U_1-2\chi C_1 T\big)$. First piece: bounded coefficient $4|C_1|^2$ times current $V$. Second piece: bounded coefficient $8\chi|C_1|^3$ times $T\in L^p$, giving $\le C\|T\|_p\|V\|_p^{p-1}$. This is where $T_1$ would appear naively; identity (II) removes it, so the pair needs only $T_0$.

**(e) $B_2B_1T_0$ (=(U3) with $t=0$).** Top piece $4\chi^2C_2C_1T=4C_2C_1U$ (using $\chi^2T=U$, bounded); coefficient $4C_1U$ bounded times current $Z$: $\le C_{p,K}(\|Z\|_p^p+\|V\|_p^p)$.

**(f) Spatial commutator $a\nabla\!\operatorname{Rm}*U=\chi^2T_1*U$.** Identity (II) again $\to(U_1-2\chi C_1T)*U$: current $V$ and $T\in L^p$, both with bounded coefficient. **This is the crucial no‑circularity point**: the only place $T_1$ would enter the pair is converted to $U_1$ and $T_0$.

**(g) $a\operatorname{Rm}*V=(U-\chi^2G)*V$, $U*V$, connection variation $U_1*U$**: bounded coefficient ($|U|\le K$, $|\chi^2G|\le C$) times current $V$, all $\le C\|V\|_p^p$.

**Cutoff‑jet evolution.** $\partial_t\Gamma=-g^{-1}\nabla\operatorname{Ric}(U)=g^{-1}\!*\operatorname{Ric}(U_1)$ (since $\nabla$ commutes with the metric trace), so $\partial_tC_2=-\partial_t\Gamma*C_1=g^{-1}*V*C_1$; the fixed scalar's raw jet only sees the current $V$ and bounded $C_1$. Norm/measure variation contributes bounded coefficient $\operatorname{Ric}(U)$. Testing against $|Z|^{p-2}Z$:
$$\frac{d}{dt}\|Z\|_p^p\le C\|d\chi\|_\infty\|V\|_p\|Z\|_p^{p-1}+CK\|Z\|_p^p\le C_p(1+\|V\|_p^p+\|Z\|_p^p).$$
No $C_3$ enters. 

**Closure.** Adding,
$$\frac{d}{dt}\big(\|V\|_p^p+\|Z\|_p^p\big)+cD^U_{1,p}\le C_p\big(1+\|V\|_p^p+\|Z\|_p^p\big),$$
Grönwall on the finite slab $[\tau,T_*)$ gives $U_1,C_2\in L^p$ for every finite $p$. Constants depend on $K$, $\|d\chi\|_\infty$, $\|\chi\|_{C^3}$, metric equivalence, volume, and $\|T\|_{L^q(\tau)}$, all finite for the datum.

---

## 3. The subsequent unweighted $T_1=\nabla T$

Set $X=T_1$, $D^T_{1,p}=\int\chi^2|\nabla X|^2|X|^{p-2}$ (the energy $\int|X|^p$ is unweighted, its dissipation is $a$‑weighted — the correct degenerate‑parabolic pairing). Inputs, all already completed: $T_0,C_2,U_1\in L^{2p}$ and $|U|\le K$. Differentiating the $T$-equation $\partial_tT=a\Delta T+B_1\nabla T+B_2T+a(T*T+T+1)$:

**Principal drift:** $\le\varepsilon D^T_{1,p}+C\|d\chi\|_\infty^2\|X\|_p^p$ (identity (I)).

**$\nabla^3a\,T$ (the term you flagged).** Expand *first*: $\nabla^3a=2\chi C_3+6C_1C_2$. Integrate by parts **only** the $2\chi C_3$ piece ($C_3=\nabla C_2$); keep $6C_1C_2T$ as a bounded‑coefficient product $\le C\|C_2\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}$. The IBP of $\chi C_3T$ gives, since $\nabla T=X$:
$$-\!\int d\chi\,C_2\,T\,P(X)-\!\int\chi C_2\,X\,P(X)-\!\int\chi C_2\,T\,\nabla P(X),$$
with
- first $\le\|d\chi\|_\infty\|C_2\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}$;
- second = signed Hessian in $X$ (second IBP, $C_2\to d\chi$) $\le\varepsilon D^T_{1,p}+C\|d\chi\|_\infty^2\|X\|_p^p$;
- third $\le\varepsilon D^T_{1,p}+C\!\int|C_2|^2|T|^2|X|^{p-2}\le\varepsilon D^T_{1,p}+C\|C_2\|_{2p}^2\|T\|_{2p}^2\|X\|_p^{p-2}\le\varepsilon D^T_{1,p}+C(1+\|X\|_p^p)$.

**$B_2X=(2\chi C_2+2C_1C_1)X$**: signed Hessian $+$ bounded coefficient.

**Reaction $aT*X=U*X$**: bounded coefficient $|U|\le K$ times current, $\le K\|X\|_p^p$. This uses the structural fact that the quadratic curvature reaction always carries the weight $a$, so $aT=U$ is bounded — not $T$.

**$B_1T^2=2\chi C_1T^2$**: $\le C\|T\|_{2p}^2\|X\|_p^{p-1}$.

**Connection variation $\nabla U*T=U_1*T$** (time commutator $\partial_t\Gamma*T$): $\le\|U_1\|_{2p}\|T\|_{2p}\|X\|_p^{p-1}$.

**Closure:** $\dfrac{d}{dt}\|X\|_p^p+cD^T_{1,p}\le C_p(1+\|X\|_p^p)$, Grönwall gives $T_1\in L^p$ for every finite $p$.

The §4A warning in Step 40's companion note is correct and should be foregrounded: if one integrated the whole $\nabla(\nabla^2a)$ instead of expanding, the piece $2C_1C_1\,T\,\nabla P(X)$ would land with no $\chi$ factor and would demand $\varepsilon\int|\nabla X|^2|X|^{p-2}$ (unweighted), which the $\chi^2$‑weighted $D^T_{1,p}$ cannot supply as $\chi\to0$. Expanding first and integrating only the $\chi C_3$ piece is what keeps the term collar‑stable.

---

## 4. Direct answers to the four questions

**Division by $\chi$:** none. Every candidate — $T=U/\chi^2$, $|\nabla a|^2/a$, $\chi E=\operatorname{Ric}(U)/\chi$ — is removed by identity (I) ($|\nabla a|^2/a=4|d\chi|^2$) or identity (II) ($\chi^2T_1=U_1-2\chi C_1T$, and $\chi^2T=U$, $\chi^2\operatorname{Rm}=U-\chi^2G$ all kept as bounded weighted combinations). The signed Hessian second IBP converts current $C_2$ into $d\chi\in L^\infty$, never dividing.

**Unweighted pointwise $T$:** not needed. Only $T\in L^q$ (finite $q$) from the seed is used, always as $\int|C_2|^2|T|^2|X|^{p-2}$, $\|T\|_{2p}$, etc. Wherever curvature appears as a coefficient it is the weighted $aT=U$ (bounded) or $a\operatorname{Rm}=U-aG$ (bounded), never $\|T\|_\infty$.

**Regularization‑parameter ratio:** none for the exact flow ($a=\chi^2$, no parameter present). In the regularized presentation $b=\chi^2+\varepsilon^2$ (Step 45) every constant uses only $\chi^2/b\le1$ and $|B_1|^2/b\le4|C_1|^2$, uniformly bounded, with no negative power of $\varepsilon$ and no $\varepsilon/\nu$ ratio. The scalar viscosity $\nu$ of Step 56 belongs to the start construction and does not enter this continuation layer.

**Behavior at the small‑$\chi$ collar:** stable. Each term that would need unweighted $\int|\nabla V|^2$ instead carries a compensating $\chi$: the top jets are $2\chi C_3\,U$ and $2\chi C_3\,T$, and every Young step against dissipation produces $\varepsilon\int\chi^2|\nabla(\cdot)|^2$. Terms without dissipation ($\int|C_2|^2|T|^2|X|^{p-2}$, $\|d\chi\|_\infty^2\|V\|_p^p$, etc.) are pure finite global $L^p$ products with bounded $d\chi$ — finite on all of $M$. A01's Step 43 §7 states the structural reason correctly: a *bare* $C_{m+2}$ (without $\chi$) would leave $\int|C_{m+1}||aE||V|^{p-2}|\nabla V|$ needing $\varepsilon|\nabla V|^2\le\varepsilon\chi^2|\nabla V|^2$, which loses control as $\chi\to0$. The provenance result that all $C_{m+2}$ jets carry $\chi$ is what makes this not happen; I confirm it at $m=1$ (top jet $2\chi C_3$ in $\nabla^3a$).

---

## 5. The $T_0$ seed (Step 44), on which everything above rests

I checked it because the whole layer is contingent on it. The reaction $a|T|^{p+1}=|U||T|^p\le K|T|^p$ (weight $a$ on every quadratic term), the drift bound via $|\nabla a|^2/a=4|d\chi|^2$, and the Hessian‑$a$ term integrated once with $|\nabla\mathcal B|\le C|T||\nabla T|$ all close to
$$\frac{d}{dt}\mathcal T_p+c\mathcal D_p\le C(K+1+\|d\chi\|_\infty^2)\mathcal T_p+C'(K+1)\operatorname{Vol}(g(t)),\qquad \mathcal D_p=\int\chi^2|T|^{p-2}|\nabla T|^2,$$
and Grönwall gives $\sup_{[\tau,T_*)}\|T\|_p<\infty$. The seed is sound and collar‑stable. Note the additive volume term makes it a finiteness statement (per‑datum), which is what the continuation interface uses; it is not the homogeneous collapse‑uniform estimate of the first‑exit argument, and the note is explicit about this. The earlier initialization "bounded $U$ + finite total curvature $\Rightarrow T\in L^q$" is genuinely false (where $\chi$ is small, $\chi^2T$ can be bounded while $T$ grows); Step 44's replacement by an energy estimate is the correct repair.

---

## 6. Refinements the notes should incorporate

1. **One time convention.** Step 40 works in a metric‑compatible/post‑conversion form; Step 45 in coordinate time with $B_r=\nabla^r(\chi^2)$ kept unexpanded. Both give the same $m=1$ result, but they are being cited together. Step 45's coordinate‑time convention with the raw jet law $\partial_tC_{m+1}=\sum_{r+s=m-1}U_{r+1}C_{s+1}$ (for $m=1$: $U_1C_1$) is the cleaner one and should be the single stated convention; Step 40's schematic $U_0*C_{m+1}$ as a "raw" term is only the energy's norm/measure variation, and reading it as an evolution term invites confusion.

2. **Foreground the second IBP.** The signed Hessian step is the linchpin at $m=1$: it is where the current jet $C_2$ is eliminated in favor of $d\chi\in L^\infty$. The notes reference "the Step 38 lemma" without displaying that the output is $\|d\chi\|_\infty$ (not any $\|C_2\|$). Writing the two lines of the second IBP explicitly makes the whole exponent‑ascent removal visible and self‑contained.

3. **State the no‑circularity fact.** The $(U_1,C_2)$ pair needs only $T_0$, not $T_1$: the sole places $T_1$ would appear ($B_1B_1T_1$ and the spatial commutator $\chi^2T_1*U$) are removed by identity (II). This should be stated outright, because the companion note lists "$\nabla T\in L^q$" among base inputs and a reader may infer a circular dependence in the order $T_0\to(U_1,C_2)\to T_1$. There is none.

4. **Endorse the $\nabla^3a$ expansion warning.** Expand $\nabla^3a=2\chi C_3+6C_1C_2$ and integrate only $\chi C_3$. This is essential, correct, and worth stating as a rule for every order, since the $C_1C_2$/$C_1C_1$ pieces must never be routed through the $\chi^2$‑weighted dissipation.

---

## 7. What this layer does and does not settle

The m=1 pair and $T_1$ estimate are internally consistent, division‑free, collar‑stable, use only the $T_0$ seed and bounded $U$, and produce the stated exact $L^p$ inequalities. This is the first genuine rung of the staggered derivative propagation on the fixed slab. It does not by itself produce the smooth terminal metric (that needs the full ladder $m\ge2$ closed the same way, then Sobolev with $p>n$), the restart, or anything beyond the derivative‑propagation half of the continuation implication. It is one analytic ingredient of the restricted four‑dimensional Ishida–LeBrun route and touches neither the positive sign branch, arbitrary four‑manifold topology, $n\ge5$, dimension‑only pinching constants, nor the Lean formalization required by Problem 26.

One item I could not fully close from the supplied text: the curvature‑commutator remainders $\mathcal R_{\mathrm{com}}$ from reordering covariant derivatives contain bare $\operatorname{Rm}=T-G$ (controlled only in $L^q$, not $L^\infty$). At $m=1$ these are low‑order and pair with $T\in L^q$, so they close on the finite slab; but the general‑$m$ note asserts they are "covered by (1.7) together with $T_j,\,j<m$" without displaying the exponent bookkeeping for the bare‑curvature factor. For the $m=1$ verification this is fine; for the arbitrary‑order induction it is the one place I would want the exponent allocation for the bare‑$\operatorname{Rm}$ commutator factor written explicitly rather than asserted.