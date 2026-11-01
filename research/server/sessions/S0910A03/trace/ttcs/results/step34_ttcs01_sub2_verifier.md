# TTCS Independent Branch Record

```json
{
  "step_id": 34,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step32_preceptor_analytic_review.md",
    "Sessions/S0910A01/workspace/notes/step31_general_p_tensor_power_inequality.md",
    "Sessions/S0910A03/workspace/codex_loop/work/weighted_moser_and_continuation_repair.md",
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md"
  ]
}
```

## Task

Independently verify the restored weighted-flow analysis in Step 34. Focus on four load-bearing points: (i) whether the Sobolev convention and collapse cancellation are now correct; (ii) whether the nested-time mixed recurrence and endpoint time powers in equations (4.2)-(4.9) follow from the cited energy structure, identifying any missing factors or circular use of Y, J6, or moving Sobolev control; (iii) whether direct J6 absorption via the unweighted L2 curvature coefficient in (4.10) is mathematically plausible from the exact defect equation, and what exact tensor/Kato calculation remains; (iv) whether the evolving cutoff-Hessian discussion and proposed base coupled estimate correctly isolate the m=2 continuation issue. Give corrected formulas where needed and sharply distinguish derived consequences from open estimates. Do not infer any pinching-gap theorem.

## Output

# Verification Memo: Step 34 Restored Weighted-Flow Analysis

## (i) Sobolev Convention and Collapse Cancellation

**Convention is now self-consistent.** The single Sobolev constant
$$\mathcal S = C(4,Kr^2)\,\frac{r^2}{\sqrt V}$$
used in the squared-norm form $\|u\|_4^2 \le \mathcal S(\|\nabla u\|_2^2 + r^{-2}\|u\|_2^2)$ matches the Maheux–Saloff-Coste inequality in dimension 4, where the critical embedding is $W^{1,2}\hookrightarrow L^4$. Step 33's separate symbol $S$ with the scaling of $\mathcal S^{1/2}$, subsequently squared to $S^2$, produced a spurious extra power; that error is corrected.

**Absorption number.** The identity $z_2 = \chi F$ gives
$$K_3 \le K_2^{1/2}\|z_2\|_4^2 \le C\mathcal S\,K_2^{1/2}(D_2+r^{-2}K_2),$$
so $\gamma = \mathcal S\,K_2^{1/2}$. At a good center, $K_2 = \int F^2 \le K_0 V$, hence
$$\gamma \le C\,\frac{r^2}{\sqrt V}\sqrt{K_0 V} = Cr^2\sqrt{K_0}.$$
The ball volume $V$ cancels exactly. This is the collapse-independent mechanism asserted in Section 1.

**Countermodel (Section 1.2) is valid.** Products $(\Sigma, q_i)\times(\Sigma, q_0)$ with a degenerating hyperbolic metric $q_i$ satisfy $\operatorname{Ric}=-g$ (Einstein), $\operatorname{Vol}=4\pi|\chi(\Sigma)|\cdot\operatorname{Vol}(\Sigma,q_0)$ (constant by Gauss–Bonnet), fixed topology, and $\operatorname{diam}\to\infty$. This refutes Step 33's inference $\operatorname{Ric}\ge -Kg + \operatorname{Vol}\le C + \text{fixed topology}\Rightarrow\operatorname{diam}\le C'$.

**Remaining obligation.** The moving Sobolev constant $\mathcal S(t)$ changes with the metric. Its control on $[0,T]$ enters the first-exit bootstrap (Section 5, Condition 1) and requires that the metric drift $\int_0^T\|aE\|_\infty\,dt$ be below the bilipschitz threshold. This coupling is correctly identified but not yet derived.

---

## (ii) Nested-Time Recurrence and Endpoint Time Powers

### Verification of (4.1)–(4.2)

**Mixed interpolation.** By Cauchy–Schwarz applied to $a^{3p/2-2}F^{3p/2}=(a^{(p-2)/2}F^{p/2})\,z_p^2$:
$$K_{3p/2}\le K_p^{1/2}\|z_p\|_4^2, \qquad z_p = a^{(p-1)/2}F^{p/2}.$$
Weight check: $(p-2)/2+(p-1)=3p/2-2$; $F$-power: $p/2+p=3p/2$. Correct.

**Gradient bound.** Since $\nabla(a^{(p-1)/2})=\tfrac{p-1}{2}\chi^{p-2}\nabla\chi\cdot(\text{sign})$ and $|\nabla\chi|\le C/r$:
$$|\nabla z_p|^2 \le Cp^2\bigl(a^{p-1}F^{p-2}|\nabla F|^2 + a^{p-2}r^{-2}F^p\bigr),$$
so $\|\nabla z_p\|_2^2 \le Cp^2(D_p+r^{-2}K_p)$, using $a^{p-2}\le a^{p-1}$ only where $a\ge1$; since $a\le1$, the correct domination is $a^{p-2}\ge a^{p-1}$, but both terms appear naturally and $\|z_p\|_2^2=\int a^{p-1}F^p\le K_p$. Correct.

**One-step spacetime bound.** From the energy inequality with time cutoff $\zeta$ on $I=(\tau,t)$:
$$\sup_{I'}K_p + c\int_{I'}D_p \;\le\; L_p\int_I K_p, \qquad L_p = Cp^N\bigl((\tau'-\tau)^{-1}+r^{-2}+1+\mathcal S^2\bar Y\bigr),$$
where $\bar Y$ is the time-averaged $Y$ on $I$. Combining with the Sobolev bound:
$$\int_{I'}K_{3p/2} \le (\sup K_p)^{1/2}\cdot C\mathcal S\,p^2\int_{I'}(D_p+r^{-2}K_p) \le Cp^N\mathcal S\,[L_p\!\int_I K_p]^{3/2}.$$
The exponent $3/2$ arises because $(\sup K_p)^{1/2}\cdot\int(D_p+r^{-2}K_p)$ consumes one factor of $A=L_p\int K_p$ at power $1/2$ and one at power $1$. Equation (4.2) is correct.

### Moser product and time exponents

Define $p_k=(3/2)^k p_0$ and $m_k=(\int_{I_k}K_{p_k})^{1/p_k}$. At each step:
$$m_{k+1} = (C_k\mathcal S)^{1/p_{k+1}}\,L_k^{1/p_k}\,m_k.$$
The accumulated $\mathcal S$-power is
$$\sum_{k=0}^\infty \frac{1}{p_{k+1}}=\sum_{k=1}^\infty\frac{1}{p_k}=\frac{3}{p_0}-\frac{1}{p_0}=\frac{2}{p_0},$$
giving $\mathcal S^{2/p_0}$. The time-cutoff factors $L_k\sim 4^k/t$ accumulate to
$$\prod_k L_k^{1/p_k}\sim t^{-\sum 1/p_k}=t^{-3/p_0},$$
since $\sum_{k=0}^\infty 1/p_k = p_0^{-1}\cdot(1-2/3)^{-1}=3/p_0$. Therefore
$$\|af(t)\|_\infty \le C(\gamma,\theta)\,\mathcal S^{2/p_0}\,t^{-3/p_0}\Bigl(\int_{t/2}^t H_{p_0}\Bigr)^{1/p_0}.\tag{4.5}$$

For curvature ($p_0=3$): $t^{-1}$. For defect ($p_0=6$): $t^{-1/2}$.

**Correction of A01 Step 31.** A01's Section 8 states that the Moser output is time-uniform, attributing the $1/t$ behavior purely to the coefficient $\mathcal S^2 Y(t)$. This is incorrect. The $t^{-3/p_0}$ factor arises from the nested time cutoffs and is a genuine feature of the parabolic Moser iteration on a slab of length $\sim t$. The coefficient's $1/t$ behavior contributes only a bounded constant after integration: $\int_{t/2}^t\mathcal S^2 Y(s)\,ds\le C\gamma^3\log2$. Step 34's restoration of the time-singular endpoint is correct.

### Endpoint verification

**Curvature.** Seed: $\int_{t/2}^t K_3\le C\gamma K_2(0)$ (from $q=2$ spacetime + interpolation, non-circular since the $q=2$ energy does not use $Y$). Then
$$\|aF(t)\|_\infty \le C\mathcal S^{2/3}\,t^{-1}\,(\gamma K_2(0))^{1/3}=C\gamma/t,$$
using $\gamma = \mathcal S K_2(0)^{1/2}$. Equation (4.6) is correct.

**Defect.** Assuming (4.7) $J_6(s)\le C\delta^6 V$:
$$\|aE(t)\|_\infty \le C\mathcal S^{1/3}t^{-1/2}(\delta^6 Vt)^{1/6}=C\delta(r^2/t)^{1/3},$$
since $\mathcal S^{1/3}=Cr^{2/3}/V^{1/6}$ and the $V^{1/6}$ cancels with $V^{1/6}$ from $(\delta^6 V)^{1/6}$. Equation (4.8) is correct.

**Drift.** $\int_0^T\|aE\|_\infty\,dt\le C\delta r^{2/3}\cdot\frac{3}{2}T^{2/3}=C\delta\theta^{2/3}r^2$ for $T=\theta r^2$. The $t^{-1/3}$ singularity is integrable at zero. Equation (4.9) is correct.

### Circularity analysis

The logical chain is strictly triangular:

| Estimate | Inputs used | Does not use |
|---|---|---|
| $K_2$ persistence (3.1) | $\gamma<c_2/2$, initial $K_2(0)$ | $Y$, $J_6$ |
| Spacetime $K_3$ (3.2) | $K_2$ persistence + interpolation | pointwise curvature |
| $K_3(t)$ forward (3.3) | Good slice from (3.2), $q=3$ energy with $\gamma$ absorption | pointwise curvature |
| Curvature endpoint (4.6) | (3.2) as Moser seed | $J_6$, defect |
| $J_6$ persistence (4.7) | Direct $\gamma$ absorption (4.10), needs exact tensor calculation | pointwise curvature |
| Defect endpoint (4.8) | (4.7) as Moser seed, curvature coefficient from (3.3) | — |
| Metric drift (4.9) | (4.8) integrated | — |

No circular dependency is present. The open loop is (4.7), proved independently of the curvature endpoint.

---

## (iii) Direct $J_6$ Absorption via Unweighted $L^2$ Curvature

### Structural verification of (4.10)

The proposed absorption is
$$\int F\,z_6^2 \le C\gamma(X_6+r^{-2}J_6), \qquad z_6=a^{5/2}|E|^3.$$

**Step 1: Cauchy–Schwarz.** Since $Fz_6^2=F\cdot z_6\cdot z_6$, apply Cauchy–Schwarz $\int fg^2\le\|f\|_2\|g\|_4^2$ to get
$$\int Fz_6^2 \le K_2^{1/2}\,\|z_6\|_4^2.$$
Here $K_2=\int F^2$ is the unweighted $L^2$ curvature energy. Correct.

**Step 2: Gradient of $z_6$.** Write $z_6=\chi^5|E|^3$ explicitly (since $a^{5/2}=\chi^5$):
$$\nabla z_6 = 5\chi^4\nabla\chi\,|E|^3 + 3\chi^5|E|^2\nabla|E|.$$
Therefore $|\nabla z_6|^2 \le C(\chi^8|\nabla\chi|^2|E|^6+\chi^{10}|E|^4|\nabla E|^2)=C(a^4r^{-2}|E|^6+a^5|E|^4|\nabla E|^2)$.

Note the power $\chi^8=a^4$, **not** $a^3$. Since $J_6=\int a^4|E|^6$:
$$\|\nabla z_6\|_2^2 \le C(r^{-2}J_6+X_6).$$
The weight algebra is exact; no uncontrolled $a^{-1}$ factor appears.

**Step 3: Sobolev + assembly.** $\|z_6\|_2^2=\int a^5|E|^6\le J_6$ (since $a^5\le a^4$ for $a\le1$). Hence
$$\|z_6\|_4^2 \le C\mathcal S(X_6+r^{-2}J_6),$$
and $\int Fz_6^2\le K_2^{1/2}\cdot C\mathcal S(X_6+r^{-2}J_6)=C\gamma(X_6+r^{-2}J_6)$. **(4.10) is verified.**

### Why this avoids the nonintegrable coefficient

If one instead bounds $\int Fz_6^2\le\|aF\|_\infty J_6$, the coefficient is $\|aF(t)\|_\infty\le C\gamma/t$, producing $J_6'\le C(\gamma/t)J_6$, whose Gronwall factor $\exp(\int_0^T\gamma/t\,dt)$ diverges at $t=0$. By contrast, (4.10) absorbs the reaction directly into the dissipation $X_6$ with a constant coefficient $\gamma$, giving
$$J_6'+\tfrac{c}{2}X_6\le C(1+\gamma)r^{-2}J_6,$$
hence $J_6(t)\le e^{C\theta}J_6(0)=e^{C\theta}\delta^6 V$. The $1/t$ curvature singularity is never integrated from zero.

### Exact tensor calculation still needed

The defect energy inequality that leads to (4.10) requires:

1. **Bochner identity for $|E|^2$ under $\partial_tg=-2aE$.** From the weighted defect equation (2.11 in the Codex repair), the reaction in $\frac{1}{2}\partial_t|E|^2$ has the form $a\langle\Delta_L E,E\rangle-a|\nabla E|^2+O(|U||E|^2+|E|^3+a|E|^2)$, where $|U|\le C(aF+a)$. Testing against $a^{m-2}|E|^{m-2}$ produces the curvature potential $\int a^{m-1}F|E|^m=\int Fz_m^2$. The $|E|^3$ contribution is dominated by $CaF|E|^2\le CF|E|^2$ on $\operatorname{supp}(a)$, giving the same structure.

2. **Kato regularization.** Replace $|E|$ by $|E|_\varepsilon=(|E|^2+\varepsilon)^{1/2}$. The inequality $|\nabla|E|_\varepsilon|\le|\nabla E|$ holds pointwise. The regularized power integral produces extra terms of size $O(\varepsilon)\to0$. This passage is standard for smooth solutions.

3. **Hessian-$a$ terms.** As in Step 23 Section 2, integration by parts converts $\nabla^2a*E$ terms into $da$ terms without introducing negative cutoff powers, because $|da|^2/a=4|\nabla\chi|^2$ is bounded and $\eta=1$ on $\operatorname{supp}(a)$ kills boundary terms.

These three calculations have not been written out as a single complete derivation. Each step is individually standard, but their composition for the specific normalized flow $\partial_tg=-2aE$ (not $-2a\operatorname{Ric}$) and the $J_6$ weight requires an explicit document. **This is the principal remaining analytic obligation for the defect side.**

---

## (iv) Evolving Cutoff Hessian and the $m=2$ Continuation

### Core observation

The covariant Hessian $\nabla^2_{g(t)}\chi$ depends on $\Gamma(g(t))$, so bilipschitz metric equivalence ($C^{-1}g_0\le g(t)\le Cg_0$) does **not** directly control $\|\nabla^2\chi(t)\|_p$. The evolution is
$$\partial_t(\nabla_i\nabla_j\chi)=-(\partial_t\Gamma^k_{ij})\nabla_k\chi,$$
where $\partial_t\Gamma^k_{ij}=\frac{1}{2}g^{kl}(\nabla_i h_{jl}+\nabla_j h_{il}-\nabla_l h_{ij})$ with $h=-2V=-2aE$. Schematically:
$$\partial_t\nabla^2\chi = g^{-1}*\nabla(aE)*\nabla\chi.$$
The leading-order term involves $\nabla U$ (since $aE=\operatorname{Ric}(U)$ and $\nabla(aE)$ contains $g^{-1}*\nabla U$ through the Bianchi identity). This creates a coupling: $\nabla^2\chi$ evolves via $\nabla U$, while the $\nabla U$ equation contains $\nabla^2\chi$ through the Hessian-of-$a$ terms.

### The $m=2$ critical term

At continuation level $m=2$, integrating by parts the $\chi\nabla^4\chi*U$ term produces (after one descent):
$$I=\int\chi|\nabla^2\chi|\,|W_2|^p, \qquad W_2=\nabla^2 U.$$

Step 34's estimate (6.6) is correct: with $u=\chi|W_2|^{p/2}$ and Hölder exponents $(4,4,2)$:
$$I\le\|\nabla^2\chi\|_4\,\|u\|_4\,\|W_2\|_p^{p/2}\le\varepsilon D_{2,p}+C_{\varepsilon,p}\mathcal S\|\nabla^2\chi\|_4^2(1+r^{-2})\|W_2\|_p^p.$$
This closes **only after** $\|\nabla^2\chi\|_4$ is already finite, which is exactly what the base coupled estimate provides.

### Consistency with Wang's framework

Wang's Lemma 4.11 proves exactly the coupled bound on $(\nabla(\chi^2\operatorname{Rm}), \nabla^2\chi)$ at the base level, and Proposition 4.14 uses it at higher levels. The residual term noted in Wang's proof of Proposition 4.14 (eq. after the displayed $\Gamma_1,\ldots,\Gamma_4$) is:
$$\int|\nabla^m(\chi^2\operatorname{Rm})|^{p-2}\langle\nabla^m(\chi^2\operatorname{Rm}),\;\nabla^2\chi*\nabla^m\chi*\chi^2\operatorname{Rm}\rangle,$$
which requires $\|\nabla^2\chi\|_q$ in every finite $q$ from the base pair. Wang states this dependency explicitly ("this is why we should bound $|\nabla^2\chi|_q$ first").

Step 34 correctly reformulates this for the shifted variable $U=a(\operatorname{Rm}+G)$: the base pair is $(W_1,C_2)=(\nabla U,\nabla^2\chi)$, and the coupled Gronwall (6.7) is
$$\frac{d}{dt}(\mathcal X_{1,p}+\mathcal Z_{2,p})\le C_{1,p}(1+\mathcal X_{1,p}+\mathcal Z_{2,p}),$$
closing under the terminal hypothesis $\|U\|_\infty<K$. The coefficient $C_{1,p}$ depends on $\|U\|_\infty$, lower-order norms, and the metric (all bounded under the terminal hypothesis).

### Differences from the local Ricci flow

For the **normalized** cutoff flow $\partial_tg=-2a(\operatorname{Ric}+g)$, two modifications appear relative to Wang's local Ricci flow $\partial_tg=-2\chi^2\operatorname{Ric}$:

1. **Conformal term.** The $-2ag$ contribution to $\partial_t\Gamma$ produces lower-order terms proportional to $\nabla a$ and $a$, which are bounded. These do not change the derivative-counting or coupling structure.

2. **Shifted variable.** $U=a(\operatorname{Rm}+G)$ has the quadratic reaction $U*U$ (no spare factor of $a$), as verified in the Codex repair equation (2.6). Wang's $\chi^2\operatorname{Rm}$ has the same reaction structure $(\chi^2\operatorname{Rm})*(\chi^2\operatorname{Rm})$, which for $a=\chi^2$ is $U*U$ (identifying $G$-terms as lower-order). The derivative-counting argument carries over.

### What remains

The base coupled estimate (6.7) is correctly formulated. The following have not been written:

- The explicit $L^p$ energy inequality for $W_1=\nabla U$, including all terms from the differentiated shifted equation, with the $\nabla^2\chi$ terms estimated in the form $\|\nabla^2\chi\|_p\|W_1\|_p^{p-1}+\|\nabla^2\chi\|_p^2\|W_1\|_p^{p-2}$.
- The corresponding $L^p$ inequality for $C_2=\nabla^2\chi$ from the evolution $\partial_t(\nabla^2\chi)=g^{-1}*\nabla V*\nabla\chi$, with $\nabla V$ decomposed via the base-level $W_1$.
- Verification that no curvature commutator at the base level ($m=1$) requires a norm of $\nabla^2 U$ that is not yet available.

These are term-by-term computations under the terminal hypothesis, not conceptual obstacles.

---

## Summary: Derived Consequences vs. Open Estimates

**Derived (modulo the provisional first-exit framework):**

| Result | Equation | Status |
|---|---|---|
| Collapse-independent $\gamma\asymp r^2\sqrt{K_0}$ | (1.4) | Verified |
| Countermodel refuting Step 33's compactness inference | §1.2 | Verified |
| Mixed interpolation $K_{3p/2}\le K_p^{1/2}\|z_p\|_4^2$ | (4.1) | Weight algebra checked |
| Spacetime recurrence with ratio $3/2$ | (4.2) | Structure checked |
| Curvature endpoint $\|aF(t)\|_\infty\le C\gamma/t$ | (4.6) | Non-circular; $t^{-1}$ is genuine |
| Defect endpoint $\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}$ | (4.8) | Volume cancellation exact |
| Integrable drift $\int_0^T\|aE\|\le C\delta\theta^{2/3}r^2$ | (4.9) | Correct |
| $J_6$ absorption via $\gamma$, not $\|aF\|_\infty$ | (4.10) | Weight algebra checked |
| Continuation base pair $(W_1,C_2)$ closes by Gronwall | (6.7) | Structure correct |

**Open estimates (required to close the program):**

1. **Exact defect tensor evolution**: write the complete Bochner identity for $|E|_\varepsilon^m$ under $\partial_tg=-2aE$, with Kato regularization, Hessian-$a$ IBP, and volume variation, producing $J_m'+cX_m\le Cr^{-2}J_m+C\int Fz_m^2$ with no uncontrolled terms.

2. **Moving Sobolev constant**: derive $\mathcal S(t)\le 2\mathcal S(0)$ from the metric drift bound within the first-exit bootstrap, completing the coupled argument in Section 5.

3. **Base coupled $L^p$ estimate**: write the explicit term-by-term energy inequality for $(W_1,C_2)=(\nabla U,\nabla^2\chi)$ under the terminal hypothesis, confirming no base-level curvature commutator escapes control.

4. **First-exit bootstrap closure**: verify that small $\delta$ (hence small drift) quantitatively improves all four provisional conditions, so the maximal provisional time equals $T=\theta r^2$.

No pinching-gap theorem is inferred from the above.