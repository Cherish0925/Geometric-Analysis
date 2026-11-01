# TTCS Independent Branch Record

```json
{
  "step_id": 42,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step39_complete_conditional_defect_gap_theorem.md",
    "Sessions/S0910A01/workspace/notes/step35_tensor_variation_and_hessian_a.md",
    "Sessions/S0910A01/workspace/notes/step34_integrated_potential_q3_and_defect.md",
    "Sessions/S0910A03/workspace/notes/step38_hessian_ibp_and_conditional_moser_repair.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A03/workspace/notes/step41_continuation_criterion_and_first_exit_assembly.md",
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Critically verify and repair the connected first-exit and terminal-chart proof for the near-critical Ishida–LeBrun negative four-dimensional route. Focus on three exact interfaces raised by the strategist. (1) A01's first-exit equation (4.13) contains an additive C0*T term that may dominate a shrinking support energy. Determine from the index-level curvature identity whether the correct q=2 inequality is homogeneous relative to K2=∫η²(1+|Rm|²), or whether a nonhomogeneous term remains; give a precise relative self-improvement estimate valid componentwise under collapse. (2) Determine whether the support construction needs a sequence-uniform Hessian bound for χ. Use the signed Hessian-a integration mechanism and distinguish zero-order smoothing estimates from per-datum continuation. (3) Repair the terminal chart passage: give a precise buffered-center construction and a rigorous route from positive-time plateau estimates to strong curvature convergence on exponential pullback charts. Check whether standard interior normalized Ricci-flow derivative estimates apply when χ=1 on a larger plateau, and state required radius/time margins. Also identify any remaining load-bearing issue in passing the explicit spectral density G to the limit. Do not accept either note's theorem status; reason from the equations and files.

## Output

# Verification Memo: Connected First‑Exit and Terminal‑Chart Argument (Ishida–LeBrun $\operatorname{Ric}=-g$ near‑critical family)

## Framing

The connected argument (A01 step39 + A03 step38/40/41 + A01 step28 + A03 step16/6) proves, by contradiction, that a near‑critical Ishida–LeBrun sequence $M_i=X_i\#k_i\overline{\mathbb{CP}}^2$ with $A_i\to\infty$, $k_i/A_i\to1/3$ admits no metrics with $\|g_i^{-1}\operatorname{Ric}_{g_i}+I\|_\infty\to0$. Structure: run the fixed‑cutoff flow $\partial_t g=-2\chi^2(\operatorname{Ric}+g)$ on macro‑disjoint good supports; the smoothing chain $K_2\Rightarrow Y\Rightarrow\|aF\|_\infty$ and $K_2\Rightarrow J_6\Rightarrow\|aE\|_\infty$ produces bounded‑curvature plateaux while global $Q=\int|E|^2$ is preserved; terminal recalibration + exponential‑pullback selection yields an Einstein germ with calibrated $W^+$‑spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$, which Derdziński forbids.

I reason from the equations. Below I resolve the three interfaces and then list what is genuinely still load‑bearing. I do not treat either note's theorem as established.

---

## Interface 1 — the $q=2$ energy is homogeneous; the additive $C_0T_*$ in A01 (4.4)/(4.13) is spurious

Take $K_2^\eta=\int\eta^2 F^2\,d\mu_t$, $F^2=1+|\operatorname{Rm}|^2$. Differentiate exactly:
$$
\frac{d}{dt}\int\eta^2F^2\,d\mu
=\int\eta^2\,\partial_t|\operatorname{Rm}|^2\,d\mu
+\int\eta^2 F^2\,(-a\tau)\,d\mu ,\qquad \tau=\operatorname{tr}E=s+4 .
$$
The constant "1" in $F^2$ has no time derivative and appears **only** through the measure term. Split it:
$$
\Big|\int\eta^2\cdot 1\cdot a\tau\,d\mu\Big|\le C\int\eta^2 aF\,d\mu\le C\int\eta^2 F^2\,d\mu=CK_2^\eta,
$$
using $|\tau|\le C|E|\le CF$, $a\le1$, and $F\ge1\Rightarrow F\le F^2$. The $|\operatorname{Rm}|^2$ part of the same measure term is $\le C\int\eta^2 aF^3=CY$. The reaction (Hamilton quadratic, normalization from $+g$, cf. A01 step35 (2.6)) is pointwise $\le CaF^3$ and tested against $\eta^2$ gives again $\le CY$. Diffusion integrates by parts to dissipation; the gradient‑cutoff term $|\nabla a|F|\nabla\operatorname{Rm}|$ gives $\varepsilon D_2^\eta+Cr^{-2}K_2^\eta$. Every piece is proportional to $K_2^\eta$, $Y$, or the dissipation. Hence the exact index‑level inequality is
$$
(K_2^\eta)'+cD_2^\eta\le CY+Cr^{-2}K_2^\eta ,
$$
which is precisely A03 step38 (4.3) and A01 step34 (3.1) — **with no $E$‑independent additive constant**. Absorbing $Y\le C\gamma(D_2^\eta+r^{-2}K_2^\eta)$ (valid because $\gamma\le\gamma_*$) leaves the homogeneous
$$
\boxed{(K_2^\eta)'\le C(1+r^{-2})K_2^\eta .}
$$

Consequently A01 step39 (4.4) $(K_2^\eta)'\le C(\cdots)K_2^\eta+C_0$ and (4.13) $\dots+C_0T_*$ carry a term that is **not** present at the index level. Its origin is treating the "$1$" in $F^2$ as an unweighted volume source; A01 step34 already flags this ("bounded by $C(r^{-2}+1)K_p$, not by a separate unweighted volume constant"). The $C_0T_*$ should be deleted.

**Precise relative self‑improvement, valid componentwise under collapse.** Per support $\alpha$, with $T_*\le\theta r^2$, $r\le r_0$, and $B(T_*)\le C\gamma_*^3$,
$$
K_2^{\eta_\alpha}(T_*)\le\exp\!\Big(C\!\int_0^{T_*}(1+r^{-2})\,dt+CB(T_*)\Big)K_2^{\eta_\alpha}(0)
\le e^{C\theta(1+r_0^2)+C\gamma_*^3}\,K_2^{\eta_\alpha}(0)<2K_2^{\eta_\alpha}(0)
$$
for $\theta,\gamma_*$ small. This is multiplicative, so it holds no matter how small $\operatorname{Vol}(\operatorname{supp}\eta_\alpha)$ and $K_2^{\eta_\alpha}(0)$ become under collapse — exactly the regime where a fixed additive $C_0T_*$ would have dominated. So the strategist's worry is resolved not by controlling $C_0$ but by recognizing it does not occur; the true (F1) self‑improvement is genuinely relative.

---

## Interface 2 — no sequence‑uniform $\nabla^2\chi$ bound is needed; Lemma 3.1(a) overstates one

Two things must be kept separate.

**(i) Zero‑order smoothing estimates (the sequence‑uniform chain) use only $\|d\chi\|_\infty\le C/r$.** Every Hessian‑of‑$a$ contribution enters the energy inequalities in the signed form $\int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)$ (A01 step35 §3.3, A03 step38 §1). The signed integration by parts (step38 (1.3)–(1.5)) moves one derivative off $\nabla^2\chi$ and yields
$$
|J|\le\varepsilon\!\int\!\chi^2|\nabla V|^2|V|^{p-2}+C_{p,\varepsilon}\|d\chi\|_\infty^2\!\int|V|^p ,
$$
using $|\nabla B_{\rm curv}|\le CF|\nabla\operatorname{Rm}|$ and $|\nabla B_{\rm def}|\le Cs^{1/2}|\nabla E|$. **Only the first‑order quantity $\|d\chi\|_\infty$ appears.** If $\chi=\psi(d_{g_i}(\cdot,x_\alpha)/r)$ for a fixed profile $\psi$, then $|d\chi|_{g_i}=|\psi'|/r$ pointwise (the distance function has unit gradient), so $\|d\chi\|_\infty\le C/r$ **sequence‑uniformly**, needing only metric equivalence. No use of $\nabla^2\chi$ occurs anywhere in $K_2\Rightarrow Y\Rightarrow\|aF\|_\infty$, $J_6$ persistence, the general‑$p$ Moser ladder, the metric drift $\int\|aE\|_\infty$, or the global $Q$ propagation (all cutoff factors there are $r^{-2}=\|d\chi\|_\infty^2$).

This matters because $\nabla^2_{g_i}\chi$ is genuinely **not** sequence‑uniformly bounded under collapse: it involves $\nabla^2 d_{g_i}$ (Hessian of distance = shape operator of distance spheres), whose upper bound needs a two‑sided sectional bound on the buffer. The hypotheses supply only $\operatorname{Ric}\ge-2g$ (Bishop–Gromov), which does not bound $\nabla^2 d$ from above. **Therefore Lemma 3.1(a)'s assertion $\|\nabla^2\chi_\alpha\|_\infty\le C/r^2$ is not justified sequence‑uniformly and should be removed** (or marked per‑datum). The proof does not need it, precisely because of the signed mechanism; this is a concrete repair, not merely cosmetic.

**(ii) Per‑datum continuation uses full jets $\nabla^m\chi$, but only their finiteness.** The staggered induction (A03 step40) and the extension statement (A03 step41 Theorem 3.1) carry $C_{m+1}=\nabla^{m+1}\chi$ at every order with constants "depending on $K$, the initial metric, and the cutoff." On a fixed smooth $(M_i,g_i,\chi)$ all $\nabla^m\chi$ are finite; these bounds are per‑datum and are used only to prove the flow exists smoothly up to the fixed time $\theta r^2$ for each $i$. They enter the contradiction only through the existence of a smooth terminal metric — not through any quantitative constant. This is a clean division and is internally consistent.

---

## Interface 3 — terminal chart: buffered centers, interior Shi on the $\chi\equiv1$ plateau, $C^\infty$ pullback convergence, and the $G$ passage

**Buffered‑center construction and margins.** On $\{a=1\}=B_{2r}(x_\alpha)$ the fixed‑cutoff flow is the honest normalized Ricci flow $\partial_t g=-2(\operatorname{Ric}+g)$. The Moser endpoint gives, on the plateau,
$$
|\operatorname{Rm}(t)|=|aF|/\!\inf a+C\le C\gamma/t+C\le C_F:=\tfrac{2C\gamma_*}{\theta r^2}+C\quad(t\in[T/2,T]),
$$
a **sequence‑uniform** bound ($\gamma\le C r^2\sqrt{\overline K_0}$ from the maximal‑function good support, step34 (1.5); $r,\theta,\overline K_0$ fixed). For the exponential pullback to sit inside the normalized‑RF region one must:

- select centers in the **inner** plateau $p_i\in B_r(x_\alpha)$ (not the full $B_{2r}$); the coverage $\sum\operatorname{Vol}(B_r(x_\alpha))\ge\alpha_0' A_i$ follows from Lemma 3.1(e) by Bishop–Gromov comparison of $B_r$ to $B_{2r}$. **Lemma 3.1(e) as stated (using $B_{2r}$) should be re‑expressed for $B_r$.**
- take pullback radius $\rho<r$ so that $\exp_{p_i}(B_\rho(0))\subset B_{r+\rho}(x_\alpha)\subset B_{2r}(x_\alpha)=\{a=1\}$; the spatial Shi margin is then $r-\rho>0$.
- take $\rho<\pi/(2\sqrt{C_F})$ so Rauch gives no radial conjugate points and a Jacobian lower bound $J_p(t,\xi)\ge s_{C_F}(t)^3$; because $C_F$ is a fixed constant, such a fixed $\rho$ exists.
- account for (F2): balls are distorted by $e^{\Lambda/2}$ between $g_i(0)$ and $g_i(T)$; measure $\rho$ in $g_i(T)$ and shrink $r$ accordingly.

**Interior Shi applies and is sequence‑uniform.** With $\chi\equiv1$ on $B_{2r}(x_\alpha)$, the local (interior) Shi estimate for the normalized flow — the $+g$ term is a bounded zeroth‑order perturbation — uses only the parabolic curvature bound $|\operatorname{Rm}|\le C_F$ on $B_{g(t)}(x_\alpha,s)\times[T/2,T]$ with $s\sim re^{-\Lambda/2}$ and time margin $T/2=\theta r^2/2$. It gives
$$
\|\nabla^m\operatorname{Rm}(T)\|_\infty\le C_m(C_F,r,\theta)\quad\text{on }B_r(x_\alpha),
$$
**with constants depending only on the sequence‑uniform $C_F$, $r$, $\theta$** — not on the ambient (collapsing) global geometry, and not on the per‑datum continuation constants. This is the key structural point: existence to $\theta r^2$ is per‑datum, but the terminal derivative bounds on the plateau are sequence‑uniform because interior Shi is genuinely local. It also resolves the tension flagged in A03 step41 §6: the per‑datum $\|\nabla^m U\|_\infty$ from step40 secure smoothness; the quantitative terminal geometry then comes from Shi.

**$C^\infty$ pullback convergence.** The pullback $\widetilde g_i=(\exp_{p_i})^*g_i(T)$ on $B_\rho(0)$ inherits: sequence‑uniform $\|\nabla^m\operatorname{Rm}\|_\infty$ (from Shi + curvature‑bounded change of frame) and non‑collapse $\operatorname{Vol}_{\widetilde g_i}B_\rho(0)\ge\omega_3\int_0^\rho s_{C_F}(t)^3\,dt>0$ (Rauch). By Cheeger–Gromov/harmonic‑coordinate compactness with all‑order bounds, a subsequence converges in $C^\infty_{\rm loc}$ to a smooth $\widetilde g_\infty$. **This replaces the $W^{2,p}$/"smoothly or at least strongly $W^{2,p}$" hedge in step28 §3 and step16 §3 by genuine $C^\infty$ convergence** — the correct, and cleaner, statement, and it is what the $G$ passage needs.

**Passing the spectral density $G$ to the limit — the load‑bearing points.** With $\fint_{B_\rho(0)}\mathfrak D(\exp_{p_i}v)\,dv\to0$ (selection via step28 (2.4), driven by $Q(T)/A_i\to0$) and $C^\infty$ convergence of $\operatorname{Rm}$:
- $|W^+|$ and the lowest eigenvalue $w$ of $W^+$ are Lipschitz in $\operatorname{Rm}$ (symmetric‑matrix eigenvalues are Lipschitz in operator norm, including through the double‑eigenvalue crossing that the calibrated spectrum exhibits), so $G=f^2-(b_-)^2$ is a continuous functional of the metric 2‑jet. Uniform convergence of $\operatorname{Rm}$ gives $G_i\to G_\infty$ uniformly; $\int G_i\to0\Rightarrow G_\infty\equiv0$ on $B_\rho(0)$. Without the Shi‑based smooth limit this would be only an a.e. statement requiring an extra bootstrap; the Shi route removes that dependency.
- The extraction is rigid and forced. With $E_\infty=0$ (Einstein), $s_\infty=-4$, $|W^+_\infty|^2=\tfrac1{24}$: $f_\infty=\tfrac23(-4)-2\sqrt{2/3}\cdot\tfrac1{2\sqrt6}=-\tfrac83-\tfrac13=-3$, so $G_\infty=0$ forces $b_{\infty,-}=3$, i.e. $b_\infty=-3$ (so $b_\infty\le0$ is compelled, not assumed), giving $w_\infty=-\tfrac16$; trace‑freeness $\alpha+\beta=\tfrac16$ and $\alpha^2+\beta^2=\tfrac1{24}-\tfrac1{36}=\tfrac1{72}$ have discriminant $0$, hence $\alpha=\beta=\tfrac1{12}$. Spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$, contradicting Derdziński/step6.

**One item to pin down.** The pointwise nonnegativity $G=f^2-(b_-)^2\ge0$ (step39 (2.9)) is asserted as a spectral‑gap identity. I can confirm the equality‑case arithmetic above, but the general pointwise $G\ge0$ (needed for $\int G\le48\pi^2 D$ to be a genuine one‑sided bound on every terminal metric, not only near calibration) rests on the step5/8 completion‑of‑squares algebra, which is not fully in the supplied files. This algebraic fact — $|f|\ge b_-$ for arbitrary $W^+$ eigenvalue orderings under the SW constraint — should be exhibited explicitly, since it is what makes $\int_{M_i}G_T\le6Q(T)$ (step28 (1.5)) a legitimate bound for the terminal metric $g_i(T)$ rather than only the initial one.

---

## Remaining load‑bearing items (from the equations, not accepting theorem status)

1. **A01 §7 and A03 §9 disagree on the terminal passage.** A01 step39 §7 presents the terminal recalibration → pullback → Derdziński contradiction as complete; A03 step41 §9 obligation 1 states the "terminal geometric passage (Layer E) … has not been connected on the actual controlled terminal metric." The material above shows how to connect it (inner centers, $\rho<r$, interior Shi, $C^\infty$ compactness), but until that connected passage is written on the flowed $g_i(T)$ with the sequence‑uniform Shi bounds, the argument's endpoint is assembled here in the memo, not in the notes. This inconsistency should be reconciled explicitly.

2. **Short‑time existence and restart (Step 37 / (H1)) is cited, not verified in these files.** A03 step41 §8 "discharges" (H1) by referencing step37 ("adapting Yang's Theorem 8.2, normalization as bounded zeroth order"); step37 is not among the supplied files. A01 step39 §8 itself calls it "plausible but not yet independently verified." The transported‑coefficient degenerate‑parabolic existence with restart from an arbitrary smooth terminal metric remains the analytic input on which the extension statement (step41 Theorem 3.1) depends.

3. **The all‑order staggered induction (step40) is "TTCS‑verified but schematic at high orders."** The $m=2$ case is written in full (step41 §3 Step B cites a companion note); the general‑$m$ closure (2.9),(2.11),(3.6) is presented with schematic $*$‑notation and a finite‑exponent counting argument. This is what secures per‑datum smoothness; its full write‑up is still outstanding by the notes' own statement.

4. **Reach.** Even fully assembled, the argument concerns only the near‑critical Ishida–LeBrun $\operatorname{Ric}=-g$ four‑dimensional family. It does not touch the $\operatorname{Ric}=+g$ side, arbitrary four‑manifold topology, $n\ge5$ (no $W^+$/SW/Derdziński analogue), the dimension‑only constants demanded by Yau 26, or Lean formalization. The $\varepsilon_4$ produced depends on $\overline K_0$, hence on the topological family through $\operatorname{Vol}_i/A_i\ge c$, not on dimension alone.

## Net assessment of the three interfaces

- (1) The $q=2$ inequality is homogeneous; the $C_0T_*$ term is an error and its removal strengthens (F1) exactly in the collapsing regime. Repair: delete $C_0$; state self‑improvement as $K_2^\eta(T_*)\le e^{C\theta(1+r_0^2)}K_2^\eta(0)$.
- (2) No sequence‑uniform $\nabla^2\chi$ bound is needed or available; the signed Hessian‑$a$ IBP carries all cutoff terms with $\|d\chi\|_\infty\le C/r$. Repair: remove the $\|\nabla^2\chi\|_\infty\le C/r^2$ assertion in Lemma 3.1(a).
- (3) The terminal chart is repairable and can be made sequence‑uniform via interior Shi on the $\chi\equiv1$ plateau, provided centers are taken in $B_r(x_\alpha)$ with $\rho<\min(r,\pi/2\sqrt{C_F})$ and Lemma 3.1(e) is restated for $B_r$. The $G$ passage then transfers by uniform curvature convergence, contingent on the explicit pointwise $G\ge0$ algebra being supplied and on items 1–3 above being closed.