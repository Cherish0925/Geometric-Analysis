# TTCS Independent Branch Record

```json
{
  "step_id": 56,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step47_consolidated_negative_IL_gap_theorem.md",
    "Sessions/S0910A03/workspace/notes/step34_restored_weighted_flow_state_and_exact_obligations.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step44_zero_order_T_seed_repair.md",
    "Sessions/S0910A01/workspace/notes/step44_preceptor_reading_first_exit_terminal_chain.md"
  ]
}
```

## Task

Verify Step 56 Section 6 as the interface between per-datum flow construction and the collapse-uniform first-exit program. Check specifically: H_2 must be unweighted in a; shifted T versus Rm comparability; the exact global-Q decomposition with Q_rest and whether Q_rest is stationary given eta=1 near active supports; and the logical continuation argument that starts each datum separately, obtains uniform first-exit estimates only on its actual lifespan, and uses the positive-time U/T/cutoff-jet hierarchy to rule out an endpoint before theta r^2 without importing high cutoff jets into the uniform estimates. Identify any circularity or support-geometry flaw.

## Output

## Verification memo — Step 56 §6 as interface

I checked §6 against the exact-flow construction in §§1–5 of the same note and against the moment machinery it imports from Steps 34/35/37/38/39/40/44/47. The four requested items hold; the assembled logic is a standard open–closed continuation argument, not a circular one; and I found no support-geometry flaw, though two geometric hypotheses must be carried explicitly and several upstream lemmas are load-bearing.

### 1. H₂ is genuinely unweighted (§6.1)

The hierarchy $H^\alpha_q=\int\eta_\alpha^2 a^{q-2}F_T^q\,d\mu_t$ carries the weight $a^{q-2}$, so at $q=2$ the exponent is $a^0=1$ and $H_2^\alpha=\int\eta_\alpha^2 F_T^2\,d\mu_t$ is unweighted. This is arithmetically forced and is consistent with the definition $H_p=\int a^{p-2}f^p$ used in Step 34 and $K_2=\int\eta^2(1+|{\rm Rm}|^2)$ in Step 47 §5b.

The reason unweightedness matters is correct and worth stating precisely: because the velocity of the exact flow is $-2a(\operatorname{Ric}+g)$, the field is frozen wherever $a=0$, so $F_T$ over the collar $\{a=0\}\cap\{\eta_\alpha=1\}$ is stationary, and the cutoff-derivative reaction terms carry a factor $d\eta_\alpha\cdot(\text{velocity})=d\eta_\alpha\cdot a\cdot(\cdots)=0$ because $a=0$ on $\operatorname{supp}d\eta_\alpha$. Thus $H_2^\alpha$ evolves controllably on the full $\eta_\alpha$ support even though it contains collar regions where $a$ vanishes. An $a$-weighted energy would drop exactly these collars, which is the point of the remark that it "cannot be substituted into the Sobolev absorption." So the unweightedness of $H_2$ and the buffer property $a=d\eta_\alpha=0$ on $\operatorname{supp}d\eta_\alpha$ are jointly required, and they are compatible.

One clarity point: the pointwise curvature endpoint $\|aF_T(t)\|_\infty\le C\gamma/t$ in (6.8) is $a$-weighted and therefore controls curvature only on the $\{a=1\}$ plateau, not on the collar. That is exactly what the terminal step needs (Shi on $\{a=1\}$). It is worth writing that $H_2$ (unweighted, full $\eta$-support) and $\|aF\|_\infty$ (weighted, plateau) play distinct roles; nothing is inconsistent.

### 2. Shifted $T$ versus $\mathrm{Rm}$ comparability (§6.1)

With $T=\operatorname{Rm}+G$, $G=g\owedge g/(2(n-1))$, the tensor $G$ is algebraic in $g,g^{-1}$, so $|G|_g$ is a fixed number $c_n$ depending only on $n$ and not on the point. Hence $|{\rm Rm}|-c_n\le|T|\le|{\rm Rm}|+c_n$, which gives
$$
c^{-1}(1+|{\rm Rm}|^2)\le F_T^2=1+|T|^2\le c\,(1+|{\rm Rm}|^2),
$$
with $c=c(n)$. The maximal-function bound $\int_{B_{7r}}|{\rm Rm}|^2\le\kappa_0^2\operatorname{Vol}B_{7r}$ then yields $H_2^\alpha(0)=\int\eta_\alpha^2 F_T^2\le C(1+\kappa_0^2)\operatorname{Vol}B_{7r}$, and with $\mathcal S_\alpha\le Cr^2/\sqrt{\operatorname{Vol}B_{7r}}$ the volume cancels in $\mathcal S_\alpha H_2^\alpha(0)^{1/2}\le Cr^2\sqrt{1+\kappa_0^2}$. This is the same collapse cancellation as Step 47 §3d, now written for the shifted tensor, and it is correct. (Note the good-set maximal function must be taken up to radius $\ge 7r$ to match the $B_{7r}$ buffers used here; the A01 Step 44 §3 construction does this.)

### 3. Global-$Q$ decomposition and stationarity of $Q_{\rm rest}$ (§6.2)

The partition is exact and its two hypotheses are the ones that must be preserved from the support construction.

- **$0\le\rho\le1$.** With $\rho=\sum_\alpha\eta_\alpha^2$ and the outer supports of the $\eta_\alpha$ pairwise disjoint, at most one summand is nonzero at any point, so $\rho=\eta_\alpha^2\le1$ and $1-\rho\ge0$. This uses disjointness of $\operatorname{supp}\eta_\alpha$, which is stated. Then $Q_{\rm global}=\int\rho|E|^2+\int(1-\rho)|E|^2=\sum_\alpha Q_\alpha+Q_{\rm rest}$ is an identity, and (6.6) is valid.

- **$1-\rho$ supported in $\{a=0\}$.** This needs the nesting $\operatorname{supp}\chi_\alpha\subset\{\eta_\alpha=1\}$: then on $\operatorname{supp}a$ we have $\rho=1$, so $\{\rho<1\}\subset\{a=0\}$. The A01 Step 44 scheme ($\chi_\alpha=1$ on $B_{5r}$, $\operatorname{supp}\chi_\alpha\subset B_{6r}$, $\eta_\alpha=1$ on $B_{6r}$, $\operatorname{supp}\eta_\alpha\subset B_{7r}$) satisfies it; the Step 47 scheme ($B_{4r}/B_{5r}/B_{5r}/B_{6r}$) also does. Step 56 §6 asserts this via "$\eta_\alpha=1$ on a neighborhood of every active support" but does not restate the radii, and the two source notes use different radii. The nesting property is the same in both, so there is no error, but §6 would be self-contained only if it names the buffer nesting it relies on.

- **Stationarity.** The exact flow has $\partial_t g(x)=-2a(x)(\operatorname{Ric}+g)(x)$, which vanishes *pointwise* wherever $a(x)=0$, even though $\operatorname{Ric}$ is a differential operator, because the reaction coefficient $a(x)$ multiplies the entire right side. Hence $g(t,\cdot)=g(0,\cdot)$ on $\{a=0\}$, and on the open interior of $\{a=0\}$ all spatial derivatives, $\operatorname{Ric}$, $E$, and $d\mu$ are frozen. The residual set where $a=0$ pointwise but $a>0$ arbitrarily nearby (transition sphere) is measure zero and does not affect $Q_{\rm rest}=\int(1-\rho)|E|^2d\mu_t$. So $Q_{\rm rest}(t)=Q_{\rm rest}(0)$ is correct. The one thing that must be true is that this is done on the *exact* limiting flow — which §§1–5 now build directly — and not on the $b_\varepsilon=a+\varepsilon^2$ regularization, where the exterior moves by $-2\varepsilon^2(\cdots)$. The Step 47 supersession note flags precisely this earlier error; §6 is written on the exact flow and thereby avoids it.

- **Consequence (6.7).** $Q_{\rm rest}(0)\le Q_{\rm global}(0)\le\delta^2\operatorname{Vol}$, and $\sum_\alpha Q_\alpha(0)=\int\rho|E(0)|^2\le Q_{\rm global}(0)$; the per-support inequality then gives $Q_{\rm global}(t)\le e^{Ct/r^2}Q_{\rm global}(0)$, matching Step 47 (5.7). The statement "selected supports need not cover $M$" is genuine and is the real gain of this decomposition: the uncovered part is inertly carried in $Q_{\rm rest}$. This is correct.

### 4. The continuation logic — circularity check (§6.3)

The argument is: per-datum local existence on $[0,T_i]$ (§4); let $T_i^*$ be the endpoint of a chosen smooth branch; run the collapse-uniform first-exit estimates on $(0,\min\{T_i^*,\theta r^2\})$; if $T_i^*<\theta r^2$, use the finite (datum-dependent) $\|aF_T\|_\infty\le C\gamma/t$ on $[T_i^*/2,T_i^*)$ to run the $(U_m,C_{m+1})/T_m$ hierarchy, obtain a smooth $g(T_i^*)$, and restart, contradicting maximality.

This is sound and is not circular, for the following reasons.

**The two ingredients live on the actual lifespan without assuming the endpoint.** The uniform first-exit estimates are derived by energy/Moser on any subinterval where the doubling conditions ($H_2\le2H_2(0)$, $d(t)<d_0$) hold; they do not presuppose reaching $\theta r^2$. Because they strictly improve those conditions ($H_2(\theta r^2)\le\tfrac32 H_2(0)$ via the choice of $\theta$; $d(\theta r^2)<d_0$ via $\delta\le\delta_0$ in (5.6)), the conditions cannot first equal their thresholds before $\theta r^2$ so long as the field exists. This is the closed step. The open step is the finite-$|U|$ extension: on $[T_i^*/2,T_i^*)$, $\sup|U|=\sup|aT|\le\sup aF_T\le 2C\gamma/T_i^*<\infty$, and the per-datum derivative hierarchy (Steps 40/44) plus the §4 restart extend the field past $T_i^*$. Nonemptiness is $T_i>0$ from §4. Openness + closedness on $[0,\theta r^2)$ is the standard continuity method; the field reaches $\theta r^2$ with the uniform quantities in range.

**The separation of datum-dependent from uniform inputs is genuine, and it rests on the signed-Hessian integration by parts.** The uniform estimates ($H_2$, $J_6$, $Q$, and the Moser endpoints $\|aF\|_\infty$, $\|aE\|_\infty$) contain the coefficient $\nabla^2 a=2\chi\nabla^2\chi+2\nabla\chi\otimes\nabla\chi$, which naively imports the second cutoff jet $\nabla^2\chi$. Step 38/44 convert every such term by one integration by parts into a $|d\chi|^2$-coefficient (Step 44 (2.9)–(2.12): "no pointwise Hessian bound for $\chi$ is used"). Consequently the uniform Grönwall coefficients use only $|d\chi|\lesssim r^{-1}$, $\kappa_0$, $\gamma\le C'r^2$, and $\delta$. The higher cutoff jets $C_{m+1}=\nabla^{m+1}\chi$ enter *only* the continuation hierarchy (Step 40), which is used qualitatively to extend existence, never to set the value of a uniform quantity at $\theta r^2$. So §6.3's central assertion — no high Sobolev norm or higher cutoff jet enters the sequence-uniform Grönwall estimates — is correct, contingent on the signed-Hessian IBP being applied in *every* uniform moment estimate. That contingency is real and should be confirmed lemma by lemma (it is the single mechanism the whole separation depends on).

**The two time powers are used in exactly the right way.** The curvature endpoint $C\gamma/t$ is non-integrable at $0$ but is only used *pointwise* on positive-time slabs (finite $|U|$, plateau Shi), never integrated; §6.3 correctly says it is "finite (although not uniform as $T_i^*\downarrow0$)." The defect endpoint $C\delta(r^2/t)^{1/3}$ has integrable $t^{-1/3}$, which is what makes the drift $d(\theta r^2)\le C\delta\theta^{2/3}r^2$ finite from $t=0$. This distinction is the correction of the earlier reading (flagged in the Step 47 supersession) that treated $C\gamma/t$ as uniform from $t=0$. It is now handled correctly.

**The restart is provided within this note.** Step 44 §5 explicitly left the "transported-coefficient degenerate short-time restart" unproven; §§2–5 of Step 56 (the tame product lemma (2.6), the doubly-regularized parabolic system (1.2), the low-order common interval (4.1)–(4.3), and the $(\varepsilon,\nu)\to0$ smooth limit) construct exactly this per-datum short-time exact flow from any smooth $(g_0,\chi)$. Restarting from the smooth $g(T_i^*)$ with the same $\chi$ therefore extends the field; the interval $T_0$ may be tiny (it depends on high norms of $g(T_i^*)$), but any positive $T_0$ contradicts maximality. So the loop is closed here. The chosen-branch language is appropriate because §5 does not assert uniqueness; the contradiction needs only one smooth branch reaching $\theta r^2$.

I did not find a circularity or a support-geometry flaw in §6.

### 5. Load-bearing upstream items to confirm independently

These are consumed by §6 as inputs; §6's assembly is valid given them, but they are not verifiable from the §6 text.

- **$J_6$ persistence seed for $\|aE\|_\infty$.** Step 34 §4 identifies the central open loop as proving the $J_6$ base energy (4.7) without first invoking a pointwise curvature bound (whose $t^{-1}$ coefficient is non-integrable at $0$). Step 47 §5d asserts this is resolved "unregularized, no $Y$-dependence" (Step 35). Since $\|aE\|_\infty\le C\delta(r^2/t)^{1/3}$ in (6.8) rests on it, and that estimate drives the drift and hence the strict improvement that closes the first-exit induction, the $Y$-independence of the $J_6$ inequality should be checked at the tensor/Kato level (the exact inequality written at the end of Step 34 §4).

- **Per-support $Q_\alpha(t)\le e^{Ct/r^2}Q_\alpha(0)$** on the exact flow with disjoint-support absorption (Step 37 / Step 47 §5g). §6.2 takes it as the hypothesis of (6.7).

- **Signed-Hessian IBP applied uniformly** (Step 38), as noted above.

- **The tame product estimate (2.6)** underlying §4's local existence — its Gagliardo–Nirenberg allocation ("interpolation parameters of factors above order four sum to at most one, after removing the unique $(m+1)$-derivative factor") is the analytic heart of the restart and would repay a direct check that exactly one high $H^m$ norm appears on the right for each surviving product in (2.5).

### 6. Where this places §6 in the overall program

§6 is an internally coherent interface: it correctly routes the unweighted $H_2$ into the collapse-uniform Sobolev absorption, the shifted $F_T$ into comparability with $1+|{\rm Rm}|^2$, the $\rho$-partition into a stationary $Q_{\rm rest}$ plus doubling $Q_\alpha$, and the per-datum finite-$|U|$ hierarchy into a continuity argument that reaches the common observation time $\theta r^2$ without leaking datum-dependent constants into the uniform quantities used by the terminal spectral contradiction (Step 47 §7). Its reach, as §7 states, is the $\lambda<0$ Ishida–LeBrun family in dimension four; it does not address the $\lambda>0$ branch, arbitrary four-manifold topology, $n\ge5$, dimension-only pinching constants, or the full Problem 26 statement, and none of my checks alter that reading. The remaining substantive work sits upstream in the $J_6$ seed and the uniform signed-Hessian bookkeeping, not in the §6 interface itself.