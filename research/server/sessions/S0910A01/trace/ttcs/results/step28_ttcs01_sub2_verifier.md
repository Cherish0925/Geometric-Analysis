# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md",
    "Sessions/S0910A03/workspace/codex_loop/Research_Report.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A01/workspace/notes/step16_exponential_pullback_averaging_review.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/scripts/step28_terminal_pullback_constants.py",
    "Sessions/S0910A01/workspace/scripts/step28_moser_recurrence_verify.py"
  ]
}
```

## Task

Verify the Step 28 consolidation of the restricted four-dimensional negative LeBrun/Ishida-LeBrun route. Read the A01 terminal recalibration/pullback note, the patched A01 weak-Moser note, A03's general-p note, A03's shifted-curvature continuation theorem and Codex report/artifact, plus the Step 16 pullback and Step 8 Derdzinski/gap notes. Please check three scientific points: (1) whether the corrected Moser recurrence (using A03 Sections 5.2-5.3, fixed J6 from time zero, polynomial p-dependence inside the time-cutoff recurrence) avoids the exponent/Gronwall errors; (2) whether the shifted curvature U=a(Rm+G) continuation proof really removes the normalization/cutoff-jet obstacle at the schematic proof level; (3) whether terminal recalibration plus exponential-pullback selection legitimately bypasses plateau noncollapse and Euler-density localization, assuming the analytic selected-support theorem produces a positive-volume bounded-curvature plateau set and Q(T)/A -> 0. Identify any remaining logical gaps or corrections without lowering the all-dimensional Yau-26 goal.

## Output

# Verification memo: Step 28 consolidation of the restricted four-dimensional $\lambda<0$ LeBrun/Ishida–LeBrun route

I read the A01 terminal-recalibration/pullback note, the A01 unified weak-Moser note, A03's general-$p$ note, A03's shifted-curvature continuation theorem with its Codex report and derivation artifact, and the Step 16 pullback and Step 8 Derdziński/gap notes. I independently recomputed the load-bearing algebra. The three requested points hold at the schematic-proof level, with the specific unresolved objects named below. None of this reaches the all-dimensional Yau‑26 statement, and I have not treated it as if it did.

## Point 1 — the corrected Moser recurrence

**The exponent correction is real, necessary, and correct.** I recomputed the two bookkeeping quantities. With $\kappa=1+2/n=3/2$ and $p_k=p_0\kappa^k$ in $n=4$:

- reciprocal-exponent sum $\sum_k 1/p_k=\frac{1}{p_0}\frac{\kappa}{\kappa-1}=3/p_0=(n+2)/(2p_0)$;
- net Sobolev power $\frac1\kappa\sum_k1/p_k=\frac23\cdot\frac3{p_0}=2/p_0=n/(2p_0)$.

These match `step28_moser_recurrence_verify.py` and A03 §5.2 (its $(C\mathsf S)^{(2/3)\sum 1/p_j}=(C\mathsf S)^{2/p_0}$ agrees). The two sessions concur on the same corrected value, which raises confidence.

**This correction is load-bearing, not cosmetic.** I checked the volume cancellation both ways. With the correct $S^{n/(2p_0)}$:
- curvature ($p_0=3$): $S^{2/3}\cdot t^{-1}\cdot(\beta/S^{2/3})=C\beta/t$ — the $S=r^2/V^{1/2}$ factor cancels exactly;
- defect ($p_0=6$): $S^{1/3}V^{1/6}=(r^2/V^{1/2})^{1/3}V^{1/6}=r^{2/3}$, giving $C\delta(r^2/t)^{1/3}$.

If one had instead used $(n+2)/(2p_0)$ as the Sobolev power (the earlier mistake), the curvature output would carry an uncancelled $V^{-1/6}$ and diverge under collapse ($V\to0$). So the entire "independent of collapsed volume" property rests on this exponent being $n/(2p_0)$. It is.

**The Gronwall error is genuinely avoided by the right mechanism.** The coefficient $\Lambda_p(t)=C_p'r^{-2}+C_p''S^2Y(t)$ is fed into a *time-cutoff energy estimate on nested slabs* (4.2)–(4.5), producing the prefactor $L_k=Cp_k^N4^k(t^{-1}+r^{-2})$ that enters the product as $L_k^{1/p_k}$. It is **not** exponentiated per exponent. I confirmed why the exponentiated form is fatal: $\exp\!\big(\int_{t/2}^t\Lambda_p\big)$ carries $\exp(c\,p^N)$, and $\sum_k p_k^N/p_k=\sum_k p_k^{N-1}$ diverges for $N\ge1$, whereas $\sum_k(\log L_k)/p_k<\infty$ because $\log L_k\sim N\log p_k+k\log4$ grows sub-geometrically against $p_k$. The three-factor Hölder step ($a^{p-1}Ff^p=(aF^3)^{1/3}(a^{p-2}f^p)^{1/3}z_p^{4/3}$, exponents summing to $p-1,1,p$) is exact, and Young's inequality places $Y$ linearly as a coefficient rather than a $p$-deteriorating threshold. I also checked the parabolic Sobolev step: $Z_p^4=a^{2p-2}f^{2p}$ gives $K_{2p}=\|Z_p\|_4^4$, and $K_{3p/2}=\int a^{(3p-4)/2}f^{3p/2}\le K_p^{1/2}K_{2p}^{1/2}$ by Cauchy–Schwarz, so (4.4)'s exponent $\kappa=3/2$ is the correct $1+2/n$.

**Dependencies for Point 1 (completion, not error):**
1. The power-energy inequality (2.3)/(3.1) with genuinely polynomial $p$-power (the claimed $N=3$). A03 §3 gives an index-level derivation for $\Phi=F$ and the regularized $\Phi=(|E|^2+\varepsilon^2)^{1/2}$, with the favorable structural fact that the defect equation has *no curvature-only source* (all terms carry $E,\nabla E$, or traces), so the reaction is $CaF\Phi^p$ not $CaF^2\Phi^{p-1}$. The exact constant $N$ and the first several $p_k$ still need to be pinned to a computation rather than the schematic $*$-ledger.
2. The $q=2\to q=3$ potential chain (1.1) $S^2Y(t)\le C\beta^3/t$. This is where the positive-time cubic potential is born; the three-factor method is claimed to also drive the $q=2$ estimate with a $\beta_0$/$Y(0)$ seed feeding back into $Y(t)$. The absence of circularity in that feedback is worth an explicit statement.

## Point 2 — the shifted curvature $U=a(\mathrm{Rm}+G)$ continuation

**The central identity that removes the normalization obstacle is correct.** I verified $\operatorname{Ric}(G)=g$ for $G=\frac{1}{2(n-1)}g\owedge g$: $g^{ik}G_{ijkl}=\frac1{n-1}(ng_{jl}-g_{jl})=g_{jl}$. Hence $\operatorname{Ric}(\widetilde R)=\operatorname{Ric}+g=E$ and, since $\operatorname{Ric}$ is linear and $a$ scalar, $\partial_tg=-2aE=-2\operatorname{Ric}(U)$. This is the decisive step: the connection variation becomes $\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)=\nabla U$ schematically, exactly Wang's weighted structure. The earlier treatment of $-2ag$ as "lower order" was insufficient precisely because the raw velocity variation contains $\nabla^2a*E$; here that term reads $\nabla^2a*\operatorname{Ric}(\widetilde R)=\nabla^2a*\widetilde R$, which carries a $\widetilde R$ factor and therefore has **no independent $\nabla^2a*G$ source**. The consistency check is stringent and passes: at $\widetilde R=0$ the metric is hyperbolic, $E=0$, and the flow is stationary for any fixed cutoff, so every right-hand term of (3.6) must vanish — and each does.

**The induction transfer is credible because $\nabla G=0$.** Since $\nabla^r\widetilde R=\nabla^r\operatorname{Rm}$ for $r\ge1$, the high-derivative cutoff structure of $\nabla^m U$ is combinatorially identical to Wang's $\nabla^m(\chi^2\operatorname{Rm})$; $G$ enters only undifferentiated, giving the bounded algebraic terms $\mathcal N_m$ estimated in (7.13)–(7.14) with no derivative to absorb. I traced the dependency ordering and it is genuinely well-founded: $A_{m-1}\to C_m\to B_{m-1}\to A_m\to C_{m+1}\to\cdots$, with the base $(A_1,C_2)$ pair coupled by a joint Gronwall (7.4)–(7.5). I checked that the residual top-cutoff term (7.11) $\nabla^2\chi*\nabla^m\chi*U*V|V|^{p-2}$ has cutoff orders $2$ and $m$, both $\le m$ for $m\ge2$, so the weighted estimate $A_m$ uses cutoff only through $C_m$ despite the raw equation (4.1) exhibiting $\nabla^{m+2}\chi$ and $\nabla^{m+1}U$; the $\Gamma_4$ term $\chi\nabla\chi*\nabla^{m+1}U$ is absorbed by the weighted diffusion $D_m=\int a|\nabla^{m+1}U|^2|V|^{p-2}$ because its $\chi^2=a$ weight matches. Because only finite $p$ is needed at each fixed derivative level (Sobolev embedding, not $p\to\infty$), the growing $C_p$ constants cause no exponent blow-up here.

**Remaining items for Point 2:**
1. The grouped integration by parts on $\Gamma_1+\Gamma_2+\Gamma_3$ (Wang Prop 4.14), reducing the $(m+2)$- and $(m+1)$-order cutoff derivatives down to exactly (7.11) plus diffusion-absorbable pieces, is invoked "verbatim" rather than re-derived. This is the single most load-bearing unverified computation of the continuation argument. A full index-level check at $m=2$ would confirm the residual is precisely (7.11) and nothing of order $m+1$ survives.
2. The DeTurck restart (8.4)–(8.6) with the transported coefficient and the added zeroth-order $-2\hat a\hat g$: the claim that Yang's degenerate ($a=\chi^2$ vanishing) local construction still applies with this term preserving its regularized-limit estimates rests on Yang §8 and should be confirmed against that source's actual hypotheses. At the schematic level (zeroth order, unchanged principal symbol) it is plausible.
3. The extension constants depend on the individual $(g_0,\chi,T)$, not on the sequence. This is compatible with its use — in the first-exit argument (A03 §6.2, §8) the theorem only contradicts maximality of $T_{\max}^{(i)}$ for each fixed member — provided every *sequence-uniform* quantity ($\bar\beta$, metric comparison, $\alpha,\rho,K$) comes from the Moser/energy estimates and never from the per-member extension constant. That separation is stated; it should remain explicit at the interface, since it is what keeps the qualitative continuation from contaminating the quantitative near-critical closure. I found no hidden dependence, and the bootstrap is a proper continuity argument (the $t=0$ singularity of $\|a\operatorname{Rm}\|\le C\beta/t$ is irrelevant to extension across positive $T_{\max}$, since short-time existence covers $[0,T_{\max}/2]$ and the bound covers $[T_{\max}/2,T_{\max})$).

## Point 3 — terminal recalibration plus exponential-pullback selection

**The terminal recalibration algebra is correct and conceptually sound.** I verified the orthogonal decomposition $\mathcal E=\operatorname{Ric}^\circ+\frac{s+4}{4}g$ with $|\mathcal E|^2=|\operatorname{Ric}^\circ|^2+\frac{(s+4)^2}{4}$, hence $\int(s+4)^2\le4Q$ and $\int|\operatorname{Ric}^\circ|^2\le Q$. Following $D_{a_i}\le J_i\le Q/(8\pi^2)$ through (1.4)–(1.5): $864\pi^2\cdot Q/(8\pi^2)=108Q$ and $48\pi^2\cdot Q/(8\pi^2)=6Q$, so $\int\mathfrak D\le(1+4+108+6)Q=119Q$, matching the script. The important structural point is correct: the Seiberg–Witten/Chern–Gauss–Bonnet calibration deficits are **regenerated on the terminal metric from topology** (the smooth manifold is unchanged by the flow), not transported from the initial curvature by $C^0$ comparison. (The $\mathfrak D$ density double-counts $(s+4)^2$ partially, since $|\mathcal E|^2$ already contains $\frac{(s+4)^2}{4}$; this only enlarges a nonnegative density and is harmless — the script's alternative $115$ confirms robustness.)

**The exponential-pullback lemma is proved correctly and the bypass is legitimate.** I checked the Step 16 proof: Rauch under $\sec\le K$ gives $J_p(t,\xi)\ge s_K(t)^{n-1}$ (denominator lower bound) and under $\sec\ge-K$ gives $J_p\le s_{-K}(t)^{n-1}$ (numerator upper bound); Liouville invariance of the geodesic flow on $SM$ supplies $\int_M\int_{S_pM}D(\exp_p(t\xi))\,d\xi\,d\mu=|S^{n-1}|\int_M D\,d\mu$ for each fixed $t$; integrating against $s_{-K}^{n-1}dt$ yields $\int_{P_i}A_\rho D\le C(n,K,\rho)\int_M D$ with $C=\frac{\int_0^\rho s_{-K}^{n-1}}{\int_0^\rho s_K^{n-1}}$. The condition $K\rho^2<\pi^2/4$ gives $\rho<\pi/(2\sqrt K)$, comfortably inside the first-conjugate distance $\pi/\sqrt K$, so $s_K>0$ on $(0,\rho]$ and $C$ is finite; multiple base visits are harmless since $D\ge0$; no base injectivity radius enters. Applied to $\mathfrak D_i$ with (1.9) and $\operatorname{Vol}(P_i)\ge\alpha A_i$, (2.4) gives a selected center $p_i$ with $A_\rho\mathfrak D_i(p_i)\to0$ simultaneously for all four nonnegative components. This is a genuine replacement for Euler-density localization: noncollapse is obtained in the tangent space, where the pullback metric ball is exactly the Euclidean ball (radial rays are $\hat g$-geodesics) and its $\hat g$-volume $\ge|S^{n-1}|\int_0^\rho s_K^{n-1}>0$ by Rauch. Because geodesics through the origin are the radial rays, $\operatorname{inj}_{\hat g}(0)\ge\rho$.

**The limit and Derdziński contradiction check out numerically.** From $\mathfrak D_\infty\equiv0$: $\operatorname{Ric}_\infty=-g_\infty$, $s=-4$, and $8\sqrt6|W^+|=4\Rightarrow|W^+|^2=1/24$. I re-derived the calibrated spectrum: $f=\frac23(-4)-2\sqrt{2/3}\cdot\frac1{2\sqrt6}=-\frac83-\frac13=-3$; $\mathcal G=4\xi(3-\xi)=0$ with $0\le\xi\le1/6$ forces $\xi=0$, hence lowest eigenvalue $w=-\sqrt{2/3}|W^+|=-1/6$; trace-free with $|W^+|^2=1/24$ then gives discriminant zero and eigenvalues $(-1/6,1/12,1/12)$. Derdziński's factor $(24|W^+|^2)^{1/3}=1$, so the limit is locally Kähler, contradicting the Kähler–Einstein value $|W^+|^2=s^2/24=2/3$. The contradiction is real given the conditional inputs.

**The central unresolved object of Point 3.** The bypass mechanism is valid, but the whole of §2–§3 is conditional on the *selected-support theorem* delivering, with sequence-uniform constants:
- $\operatorname{Vol}(P_i)\ge\alpha A_i$ for a fixed $\alpha>0$ (positive volume fraction of plateau centers);
- a fixed buffer radius $\rho>0$ and $K<\infty$ with $|\sec|\le K$ on all length-$\rho$ radial geodesics from $P_i$;
- $Q_i(T)\le e^{C\theta}Q_i(0)$.

Of these, $K$ is genuinely produced by the Moser output: on $\{a=1\}$, $|\operatorname{Rm}(T)|\le C\beta/(\theta r^2)$ with $\beta\le Cr^2\sqrt{1+K_0}$ gives $|\operatorname{Rm}|\le C\sqrt{1+K_0}/\theta$, sequence-uniform. And $Q_i(0)/A_i\le C\delta_i^2\to0$ (near $\operatorname{Ric}=-g$, with $\operatorname{Vol}/A=O(1)$), so (1.8) closes (1.9). But the sequence-uniform **volume fraction $\alpha$** and **buffer width $\rho$** are not delivered by anything in these notes; they are the open analytic core, correctly flagged in both A01 §4 and the two notes' closing sections. Everything downstream of (2.1)–(2.2) is a valid conditional consequence.

**One presentation item in §3 noncollapse.** Rauch delivers the volume lower bound at the *center* $0$; harmonic-coordinate compactness on $B_{\rho'}(0)$ (not merely at $0$) additionally needs the injectivity/harmonic radius bounded below on a neighborhood. This follows from the Cheeger–Gromov–Taylor injectivity estimate at $0$ (from $|\sec|\le K$ plus the center volume bound) together with near-continuity of injectivity radius under bounded curvature for points within $B_{\rho'}$, $\rho'\ll\operatorname{inj}(0)$. This is standard, but the note states it in one clause; making the center-to-neighborhood step explicit would keep the noncollapse claim watertight.

## Two smaller bookkeeping remarks

- The metric-drift exponent $V(\theta r^2)\le\frac32C\delta\theta^{2/3}r^2$ (A01 §6.6) is used as a small dimensionless exponent in $e^{\pm2V}g_0$. With the Li radius $r=r_*(n,K_0,\varepsilon)$ fixed and bounded, $V\to0$ is driven by $\delta\to0$, so the near-critical conclusion is sound; a full write-up should state the scale normalization explicitly so the "$r^2$ in an exponent" reads unambiguously.
- The coefficient $\beta^3/t$ inside (4.2) is smaller than the recorded $L_k=Cp_k^N4^k(t^{-1}+r^{-2})$ only because $\beta\le\beta_*\ll1$; this is used silently and is fine, but the critical smallness of $\beta$ is what keeps that term inside $t^{-1}$.

## Consolidated list of what remains open (without lowering the full goal)

1. Full index-level power-energy inequality (2.3)/(3.1) with pinned polynomial $p$-power, and the $q=2\to q=3$ potential feedback closing without circularity.
2. Index-level confirmation (at least $m=2$) that Wang's grouped integration by parts transfers to $U=a(\mathrm{Rm}+G)$ with residual exactly (7.11); source-level confirmation that Yang's degenerate DeTurck construction accommodates the added $-2\hat a\hat g$ term.
3. The selected-support construction producing sequence-uniform $\alpha>0$ and $\rho>0$ (and the buffer geometry) — the genuinely open analytic heart on which Point 3's contradiction depends.
4. The global defect propagation (1.8)/Step 25, referenced rather than reproduced here.

Even with all four resolved, the argument settles only the restricted four-dimensional $\lambda<0$ LeBrun/Ishida–LeBrun laboratory. The $\lambda>0$ branch, arbitrary four-manifold topology, $n\ge5$ (where volume collapse can be Einstein-compatible), the dimension-only interval quantifiers of Yau‑26, and the Lean 4 formalization remain entirely untouched. The three verified pieces are internally consistent and interlock correctly through the first-exit bootstrap; the two sessions' agreement on the corrected Moser exponent and on the shifted-curvature mechanism is a meaningful cross-check. The mathematics I could recompute independently — exponents, volume cancellation, terminal constants, calibrated Weyl spectrum, Derdziński norms, the Step 16 comparison constant — all confirm as stated.