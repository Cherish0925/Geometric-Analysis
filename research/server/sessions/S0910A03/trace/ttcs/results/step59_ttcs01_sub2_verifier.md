# TTCS Independent Branch Record

```json
{
  "step_id": 59,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step59_finite_regularity_continuation_and_common_time.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md"
  ]
}
```

## Task

Verify the finite-regularity continuation bridge in step59_finite_regularity_continuation_and_common_time.md. The theorem claims: on the exact normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed 4-manifold, if the first-exit curvature estimate ||aF_T(t)||_∞ ≤ CΓ/t holds on (0,T*) with T* < ∞, then the flow extends smoothly past T*.

The argument chain is:
(A) W^{1,p} bridge (Kato + Sobolev for p>4) gives |T|_∞ bounded on [τ,T*].
(B) Staggered induction through (U_m, C_{m+1}) for m=2,...,7 and T_m for m=2,...,6, using: (i) IBP of χC_{m+2}*U to lower cutoff jet; (ii) Hölder-Sobolev for the residual χC_{m+1}*U_1 using U_1 ∈ L^4 and current degenerate diffusion; (iii) signed-Hessian for χC_2*U_m; (iv) honest expansion of ∇^r a without false χ factors.
(C) Fixed-background conversion: A = ∇^{g(t)} - ∇^{g(τ)} satisfies a triangular ODE requiring U_1,...,U_7, giving g(t) ∈ H^7.
(D) Restart via Step 56 Theorem 4.3.

Verify specifically:
1. Is the general m induction pattern (Step 40 / A01 Step 55) structurally sound? Does the residual at every level m ≥ 2 genuinely use only U_1 (not U_j with j > 1) in the Hölder-Sobolev step?
2. Is the fixed-background conversion from current-pair L^p bounds to H^{s_0} correct? Does ∂_t(bar-nabla^m A) = g^{-1}*U_{m+1} + lower really hold?
3. Does the common observation time argument correctly separate sequence-uniform first-exit inputs from per-datum continuation inputs?
4. Are there any hidden terms at general level m that would defeat the pattern?

## Output

## Verifier Memo — finite-regularity continuation bridge (Step 59), degenerate χ²-weighted flow

I reconstructed the four requested points independently, working from the evolution structure rather than accepting the schematic assertions. The overall architecture (A)→(D) is coherent, and the central structural mechanism is genuine, not merely asserted. The main pieces that are not settled inside these notes are named explicitly at the end. Details follow.

---

### 0. The controlling structural fact: a derivative budget

Every question here is governed by one arithmetic constraint that I verified is dimensionally forced. The unknown is $U_m=\nabla^mU$ with $U=aT=\chi^2T$, and the diffusion is second order and $a$-weighted. Taking $\nabla^m$ of a second-order operator applied to $\chi^2T$ distributes a total of $m+2$ derivatives over three factors — two cutoff jets (from $\nabla^{m+2}(\chi^2)$) and one curvature factor:
$$
C_\alpha * C_\beta * U_\gamma,\qquad \alpha+\beta+\gamma=m+2,\quad \gamma\le m+1.
$$
This is exactly the constraint written in Step 40 (1.4) and A01 Step 55 (4.1). It is the right budget: the reaction/nonlinear part of the curvature evolution carries no differential order, so its $\nabla^m$-expansion lives at total order $m$ (strictly below $m+2$) and produces only products of two curvature factors of order $\le m$ against bounded coefficients. Only the second-order (diffusion-derived) part reaches order $m+2$. I checked that every allocation permitted by this budget maps onto exactly the terms the notes enumerate — nothing else is admissible.

This single constraint answers Points 1 and 4 cleanly.

---

### 1. Does the residual at every level use only $U_1$? — Yes, and it is forced

Enumerate the budget by the curvature order $\gamma$:

- $\gamma=m+1$: $\alpha+\beta=1$ gives only $\chi C_1*U_{m+1}$. This is the drift inside $\operatorname{div}(a\nabla U_m)$ and stays in the divergence; testing against $|U_m|^{p-2}U_m$ yields $-cD^U_{m,p}$ (I verified $\int \operatorname{div}(a\nabla U_m)\,|U_m|^{p-2}U_m=-\int a|U_m|^{p-2}(|\nabla U_m|^2+\dots)\le -cD$). The A01 correction — keep the divergence grouped rather than isolating $2\chi C_1\!\cdot\!\nabla U_m$ — is correct: peeling the drift and integrating it by parts moves $\nabla$ onto $\nabla a$, producing $\nabla^2a\sim\chi C_2+C_1^2$ against $|U_m|^p$, and $\chi C_2$ is available only in finite $L^q$, so that route manufactures an uncontrolled $\int\chi C_2|U_m|^p$. Keeping the divergence avoids this entirely.

- $\gamma=m$: $\alpha+\beta=2$ gives exactly $\chi C_2*U_m$ (signed Hessian) and $C_1^2*U_m$ (bounded, $C/r^2$). Matches Step 59 §3.1 Terms 2–3.

- $\gamma=1$: the current cutoff jet $C_{m+1}$ can pair with curvature order at most $1$, since $\alpha=m+1\Rightarrow\gamma\le1$. This yields $\chi C_{m+1}*U_1$ — the direct residual — and no higher $U_j$.

- $\gamma=0$: the top jet $C_{m+2}$ appears only as $\chi C_{m+2}*U$; one integration by parts (Step 59 (3.2)) lowers it to $\chi C_{m+1}*U_1$ plus $C_1 C_{m+1}*U$ (bounded coefficients) plus $\nabla P(U_m)*\chi C_{m+1}*U$ (into $\varepsilon D$).

The key point you asked about is therefore **structurally forced, not incidental**: the current jet $C_{m+1}$ and the top jet $C_{m+2}$ carry so much of the $m+2$ budget that the accompanying curvature factor can have order at most $1$. Both the direct term and the integration-by-parts residual are $\chi C_{m+1}*U_1$; no $U_j$ with $j\ge2$ can appear against $C_{m+1}$. I confirmed the same counting for the unweighted $T_m$ stage (Step 59 (3.12)): the residual is $\chi C_{m+1}*T_1$, with $T_1\in L^4$ from the base block. The pattern is genuinely finite-triangular.

I also checked the two analytic estimates that carry the residual:

- Sobolev on $f=\chi|U_m|^{p/2}$: from $|\nabla f|^2\le 2|d\chi|^2|U_m|^p+\tfrac{p^2}{2}\chi^2|U_m|^{p-2}|\nabla U_m|^2$ and $\|f\|_4^2\le C_S(\|\nabla f\|_2^2+r^{-2}\|f\|_2^2)$, one gets $\|f\|_4^2\le C_S(p^2D^U_{m,p}+C_{p,r}\|U_m\|_p^p)$. This reproduces Step 59 (3.4)/A01 (2.11) exactly.
- Hölder exponents $(4,p,4,2p/(p-2))$: $\tfrac14+\tfrac1p+\tfrac14+\tfrac{p-2}{2p}=1$. Correct. The subsequent Young step, using $\|C_{m+1}\|_p^2\|U_m\|_p^{p-2}\le \tfrac2p\|C_{m+1}\|_p^p+\tfrac{p-2}{p}\|U_m\|_p^p$, absorbs into $\varepsilon D+C(1+\|C_{m+1}\|_p^p+\|U_m\|_p^p)$. Correct.

So Point 1 holds at the level of the schematic equation plus these estimates.

---

### 2. The linchpin: complete Leibniz expansion of $\nabla^{m+2}a$

The whole mechanism depends on the fact that a jet of order $m+2$ **always arrives with a $\chi$ partner**, so it can be absorbed into the $\chi^2$-weighted dissipation after one integration by parts. Since
$$
\nabla^{m+2}(\chi^2)=\sum_{s=0}^{m+2}\binom{m+2}{s}C_s*C_{m+2-s},
$$
index $m+2$ occurs only at $s\in\{0,m+2\}$, each producing $C_0=\chi$ as the partner. Every middle summand has both indices $\le m+1$. Hence no *bare* $C_{m+2}$ (without $\chi$) ever meets a gradient — this is Step 40 (1.8) / Step 59 property (iv), and it is correct and indispensable. Step 56 §4 makes the same point at first order: fully expanding $\nabla^3a=2\chi C_3+C_1C_2$ before any integration by parts is what prevents a bare $C_1C_1*T*\nabla(|X|^{p-2}X)$ term; integrating $\nabla^3a$ blindly does not close. I verified this reasoning is exactly right.

---

### 3. Fixed-background conversion (Point 2) — correct, with one imprecision to record

The connection-variation identity is standard and correct: under $\partial_tg=h$,
$$
\partial_t\Gamma^k_{ij}=\tfrac12 g^{kl}(\nabla_ih_{jl}+\nabla_jh_{il}-\nabla_lh_{ij})=g^{-1}*\nabla h,
$$
so with $h=-2aE$, $\partial_tA=\partial_t\Gamma=g^{-1}*\nabla(aE)$. The identification $\nabla(aE)\sim U_1$ is valid up to bounded lower-order terms: $\nabla(aE)=(\nabla a)E+a\nabla E$, and $a\nabla\mathrm{Ric}=U_1-(\nabla a)T$, so $\nabla(aE)=U_1+C_1*(E-T)$ with $E-T=\mathrm{Ric}+g-\mathrm{Rm}-G$ bounded once $|T|_\infty$ is controlled. The extra bounded term sits in the same $L^p$ and does not disturb the Grönwall.

At higher order, applying $\bar\nabla^m$ and converting $\nabla^{g(t)}=\bar\nabla+A$ gives $\partial_tA_m=g^{-1}*U_{m+1}+\dots$ with the top forcing $U_{m+1}$ and no $\bar\nabla^mA$ *inside a derivative*. One point to record: the RHS does contain a term $g^{-1}*A_m*(aE)$ coming from $\bar\nabla^m(g^{-1}*A*(aE))$. This is a linear, zeroth-order (bounded-coefficient) occurrence of the current $A_m$, so the eq. (4.4) description "$P_m(A_{<m};U_{\le m};g^{-1}$)" is slightly incomplete — it should carry a benign $+\,g^{-1}*A_m*(aE)$. This does not disturb anything: the resulting ODE $\partial_tA_m=g^{-1}U_{m+1}+(\text{bdd})A_m+P_m(A_{<m},\dots)$ is linear in $A_m$ with bounded coefficient and $L^p$ forcing, and Grönwall gives $A_m\in L^\infty_tL^p$. (Note that §4 eq. (4.2) at level $0$ *does* correctly include $A$ inside $P_0$; only the general-$m$ statement drops the analogous term.) The passage $\bar\nabla^{m+1}g=A_m*g+\text{lower}$ then gives $g\in W^{s_0,p}$ for all $p$, hence $H^{s_0}$ at $p=2$, requiring $A_m$ for $m\le s_0-1=6$, i.e. $U_1,\dots,U_7$ — consistent with the restart package $(U_k,C_{k+1})$, $k\le7$. The counting $s_0=7>n/2+4=6$ is right.

The terminal-convergence step (§5) is standard: $\|\partial_tg\|_{H^{s_0-2}}=\|2aE\|_{H^{s_0-2}}\le C(1+\sum_{j\le s_0-2}\|U_j\|_2)<\infty$, giving Lipschitz-in-$H^{s_0-2}$ convergence, weak-$*$ recovery of $H^{s_0}$, and positive-definiteness by bilipschitz control. Correct.

---

### 4. Sequence-uniform vs per-datum separation (Point 3) — conceptually valid, contingent on inputs not present here

The organization in §8 is the correct one and is done carefully. The logical role of the continuation is qualitative: it rules out finite-time stopping ($T_i^*<\theta r^2\Rightarrow$ extension $\Rightarrow$ contradiction), and for that it is legitimate for the per-datum constants ($K_\tau=C_0\Gamma/\tau$, the Sobolev constant of $g(\tau)$, $C_\tau$) to depend on the datum and on $\tau$. The quantitative bounds that must be uniform in $i$ come only from the first-exit chain, and the table shows these use only $n=4$, $r$, $|d\chi|$, $H_i(0)$, $\mathcal S_i(0)$, $\gamma_i(0)$, $\delta_i$, $Q_i(0)$, $J_{6,i}(0)$. The removal of $Y_i(0)$ is real and is the substantive Step 58 repair: the direction is reversed — $Y\le C\gamma(D+r^{-2}H)$ (Step 58 (2.4)) is absorbed into the $H$-inequality, giving $H,\int(D+Y)$ from $H(0)$ alone, and $Y(t)\lesssim\Gamma H(0)/t$ only on positive dyadic slabs. The collapse cancellation $\gamma(0)\lesssim r^2\sqrt{K_0}$ (Step 58 (2.9)) is genuinely volume-independent.

What is contingent: the uniform bootstrap actually *closing* (§6(d): $\gamma_i(t)\le\gamma_*$, $V_i\le V_*$) rests on the defect Moser endpoint $\|aE_i(t)\|_\infty\le C\delta_i\phi(t)$ with $\phi$ integrable (6.4). Step 59 §9 states this endpoint "has not been independently written," and the terminal spectral density (Step 43) and core-ball argument (Step 6) are also listed as external. So the conceptual separation is valid, but the closure of the uniform chain is not self-contained in the material provided; it is the conditional Theorem of §7, whose input (iii) is the missing calculation.

---

### 5. Hidden terms at general $m$ (Point 4) — none found under the schematic

Beyond the diffusion-derived terms handled above, I checked the two remaining sources:

- **Commutators $[\partial_t,\nabla^m]U$.** These expand as $\sum_{j}\nabla^j(\partial_t\Gamma)*\nabla^{m-1-j}U$ with $\partial_t\Gamma=g^{-1}*\nabla(aE)$. The top allocation $j=m-1$ gives $\nabla^{m-1}(\partial_t\Gamma)\sim U_m+C_m*(\text{bdd})$ paired with $U_0$ (bounded), i.e. current $U_m$ times a bounded coefficient and current-below $C_m$; the cutoff jet reaches at most $C_m$, never $C_{m+1}$, and the curvature reaches $U_m$ only against $U_0$. All intermediate $j$ give products of two strictly-previous levels. Consistent with the notes' "same ordering."

- **Reaction / normalization / $G$-terms and measure–norm variation.** The reaction $\nabla^m(a\,\mathrm{Rm}*\mathrm{Rm})$ lives at total order $m$: any allocation with a factor at order $m$ forces the partners to order $0$ (bounded) and cutoff $\le C_m$. $\nabla G=0$ introduces no derivative branch. The $\partial_t d\mu$ and metric-contraction variations carry coefficient $\sim|aE|$, bounded, contributing $C\|U_m\|_p^p$.

Under the schematic equation, I find no admissible term that escapes categories 1–7. The budget constraint is strong: any conceivable product must respect total order $m+2$ over $\{C,C,\text{curvature}\}$, and I have exhibited that every such product is either the dissipation, a bounded-coefficient current term, a $\chi C_{m+1}*U_1$/$\chi C_2*U_m$ term with its named estimate, or a strictly-previous-level product.

---

### 6. What remains open in the material as given

These are the pieces the chain rests on that are not carried out inside the supplied notes:

1. **Exact tensor equation with explicit coefficients.** The budget argument strongly constrains the general-$m$ equation, but the derivation with the $G$-tensor, the $+g$ normalization, and all $[\partial_t,\nabla^m]$ commutators written with explicit (not $*$-schematic) coefficients is not present. Step 59 §9 and A01 Step 55 §5 both state this enumeration is the remaining work. My verification raises confidence that no exceptional term exists, but it does not replace that derivation — in particular the precise coefficient of each $C_\alpha C_\beta U_\gamma$ allocation and the confirmation that the $G$/normalization terms do not generate a curvature factor of order $\ge2$ against $C_{m+1}$ have not been written.

2. **The restart (D), Step 56 Theorem 4.3.** The short-time existence from $H^7$ data for the *exact* degenerate flow $\partial_tg=-2\chi^2E$ — whose diffusion vanishes on the open collar $\{\chi=0\}$ — is invoked but not contained here. The supplied Step 56 note establishes the positive-time base pair, not the restart theorem. Because the equation is non-parabolic where $\chi=0$, the delicate content of that theorem is precisely the collar coupling; this is an external dependency of the present bridge.

3. **Defect Moser endpoint (6.4).** Needed to close the uniform bootstrap of §6 and to instantiate input (iii) of the §7 conditional theorem; explicitly noted as not independently written.

4. **Extent of the eventual statement.** Even with 1–3 complete, the assembled object is the §7 conditional Theorem for a specified four-manifold $\lambda=-1$ Ishida–LeBrun family, whose threshold obeys $\delta_0\le c/\sqrt A$ (shrinking with topological complexity), and therefore does not deliver dimension-only constants $c_4,C_4$. The $\lambda>0$ family, general four-manifold topology, $n\ge5$, and the Lean formalization are untouched by this bridge. The notes state this directly (Step 59 §9, §7 Note), and the statement is accurate.

**Net reading.** The finite-regularity continuation mechanism is internally coherent, and its most load-bearing structural feature — that the current cutoff jet $C_{m+1}$ and the top jet $C_{m+2}$ can only meet curvature of order $\le1$, so the residual is always $\chi C_{m+1}*U_1$ — is forced by a derivative-order budget I reconstructed independently, not an unverified assertion. The analytic estimates (Sobolev on $\chi|U_m|^{p/2}$, the four-exponent Hölder, the Young absorption, the divergence-form testing) check out. The fixed-background conversion is the correct connection-variation calculation, with one benign linear $A_m$ term that should be listed in $P_m$ but does not alter the Grönwall closure. The sequence-uniform / per-datum separation is legitimately organized. The remaining substance is the explicit general-$m$ tensor equation, the degenerate restart theorem, and the defect endpoint — all named in the notes — together with the fact that the reachable statement is a conditional four-dimensional $\lambda=-1$ result rather than the dimension-uniform Yau 26 statement.