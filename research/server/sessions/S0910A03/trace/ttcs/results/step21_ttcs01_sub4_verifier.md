# TTCS Independent Branch Record

```json
{
  "step_id": 21,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step21_derivative_free_first_exit_and_plateau_regularity.md",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md",
    "Sessions/S0910A03/workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md",
    "Sessions/S0910A03/workspace/scripts/verify_step21_derivative_free_first_exit.py"
  ]
}
```

## Task

Verify the following mathematical chain for the 4D negative-branch cutoff-flow program on a critical Ishida-LeBrun manifold M.

(1) NORMALIZATION LOWER-ORDER: Under dt g = -2 chi^2 (Ric+g), the normalization -2 chi^2 g changes the curvature evolution by: (a) volume form -a(s+4)dmu with |s+4| ≤ 4 delta; (b) curvature: -(nabla^2 a) ☐ g + O(|nabla a||Rm|), which is lower order than the critical cubic reaction a|Rm|^2 in H_q. Verify that the critical parameter beta = A_0^2 ||Rm||_2 is unchanged, and that the normalization contributes only an exponential Gronwall factor e^{CT_0}.

(2) INTERIOR REGULARITY ON PLATEAU: After the first-exit gives |chi^2 Rm| ≤ C gamma/t uniformly on [0, T_0], on the plateau {chi=1} the flow becomes dt g = -2(Ric+g), a normalized Ricci flow. Since a=1 there, |Rm| ≤ C gamma/t. Standard Shi interior estimates on [T_0/2, T_0] x B_{rho/32}(p) should give |nabla^k Rm| ≤ C_k (T_0/2)^{-k/2}. Verify: (a) Does the normalized Ricci flow (with the -2g term) satisfy standard Shi estimates? (b) Are the Shi constants independent of the sequence index? (c) Does this give smooth compactness on the exponential chart?

(3) EXPONENTIAL CHART TO CONTRADICTION: For the limit h_inf on B_{R/2}(0) from Arzela-Ascoli: (a) Does |E_i(T_0)| → 0 follow from |chi^2 E| ≤ C delta_i (r^2/T_0)^{1/3}? (b) Does the 7/24 calibration inequality transfer through the flow and chart, giving |W+| = 1/(2sqrt6) on the limit? (c) Is the projector obstruction (simple eigenform → parallel → nabla W+ = 0 vs |nabla W+|^2 = 1/16) correctly stated?

(4) POTENTIAL GAPS: Are there any gaps in the chain from the first-exit output to the projector contradiction? In particular: does metric comparability correctly transfer the global Q control through the exponential chart? Does the good-center selection correctly provide nontrivial monopole data on the limit? Does the chart pullback preserve the all-derivative bounds from Shi?

## Output

## Verification Memo: 4D negative-branch cutoff-flow chain (Steps 16, 20, 21)

I checked the four points against the equations and the surrounding notes, redid the algebra where it is decisive, and separated what verifies cleanly from what rests on the still-unwritten weighted Moser recurrence.

---

### (1) Normalization as a lower-order modification

**Verified pieces.**
- Volume evolution: $\partial_t d\mu=\tfrac12\operatorname{tr}_g(\partial_t g)\,d\mu=-a\,\operatorname{tr}(E)\,d\mu$ with $\operatorname{tr}E=s+4$. Pointwise pinching gives $|s+4|=|\operatorname{tr}E|\lesssim\delta$, so the growth factor $e^{O(\delta T_0)}\to1$. The stated constant $4\delta$ is order-correct (Cauchy–Schwarz gives $|\operatorname{tr}E|\le 2|E|_g$ in $n=4$, so the sharp constant is $2\delta$; the loosening is harmless).
- The identity $|da|^2/a=4|d\chi|^2$ is exactly right ($a=\chi^2\Rightarrow da=2\chi\,d\chi$). This is the structurally important point: choosing the square weight $a=\chi^2$ removes the intrinsic $1/\chi$ singularity from the transition annulus. This is a genuine and correct observation, and it is what makes the degenerate energy inequalities even plausible.
- The velocity increment from the $-2ag$ term contributes $-(\nabla^2 a)\owedge g+O(|\nabla a||\operatorname{Rm}|)$ to $\partial_t\operatorname{Rm}$, since $\nabla g=0$ forces the added second-order symbol to sit entirely on $\nabla^2 a$. This is correct.
- $\beta=A_0^2\|\operatorname{Rm}\|_2$ is manifestly a function of the initial slice only; it is unchanged by the evolution equation. True but nearly tautological — the operative quantity along the flow is not $\beta$ but the persisting $A_0(t)^2\|\operatorname{Rm}(t)\|_2$ controlled by (F2)+(F3), which is where the real work sits.

**Where the order-counting is asserted rather than derived.** The note states the normalization adds a multiplicative $C\,H_q$ plus an additive $C\,\mathrm{Vol}/r^{2q}$ to (2.1). Tracking the $\nabla^2 a$ source through $\frac{d}{dt}\int a^{q-2}\eta^2F^q$ and integrating by parts once produces terms of the form $\int a^{q-2}\eta^2F^{q-1}|\nabla a||\nabla F|$ and $\int a^{q-3}\eta^2F^q|\nabla a|^2$. After the $|da|^2/a=4|d\chi|^2$ reduction and Young splitting against the dissipation $\int a\eta^2F^{q-2}|\nabla F|^2$, the residual additive piece scales like $\mathrm{Vol}\cdot r^{-2}$ (with $a$-weights), **not** $r^{-2q}$ as written. The exponent $2q$ in the note is not what the by-parts computation yields; this is a bookkeeping slip in the additive scaling. It does not break the conclusion (a bounded additive source over finite time and a multiplicative Grönwall factor are both absorbable), but the precise additive term should be recomputed rather than quoted. The qualitative statement — normalization is one curvature/derivative order below the critical cubic $H_{q+1}$ and enters by Grönwall, not by critical Sobolev absorption — is sound.

---

### (2) Interior regularity on the plateau

**(a) Does $\partial_t g=-2(\operatorname{Ric}+g)$ carry Shi estimates?** Yes. Set $g(t)=e^{-2t}\hat g(\tau)$, $\tau=(e^{2t}-1)/2$; then $\hat g$ solves unnormalized Ricci flow $\partial_\tau\hat g=-2\operatorname{Ric}(\hat g)$. (Check: $\partial_t g=-2e^{-2t}\hat g+e^{-2t}\hat g'\tau'=-2g-2\operatorname{Ric}(\hat g)=-2(\operatorname{Ric}(g)+g)$, using scale-invariance of $\operatorname{Ric}$.) The $-2g$ term is a pure time-dependent constant rescaling, and Shi's local interior estimates are scaling-covariant; over $[T_0/2,T_0]$ with $T_0=\theta r^2$ small the factor $e^{2t}\approx1$. So Shi applies. One point worth stating explicitly: $\chi$ is a **fixed spatial function**, so $\{\chi=1\}$ is a fixed set and $a\equiv1$ there for all time — the plateau equation is genuinely the normalized Ricci flow, and the interior ball $B_{\rho/32}(p)$ stays inside $\{\chi=1\}$ throughout. Infinite propagation speed (correctly flagged in Step 16 §1) does not obstruct this: Shi needs only a curvature bound on the parabolic cylinder, which (F4) supplies, not spatial confinement of information.

**(b) Sequence-independence of the Shi constants — this is the pivotal dependency.** The Shi bound at $t=T_0$ reads
$$
|\nabla^k\operatorname{Rm}|(p,T_0)\le C_k\,K\,(T_0/2)^{-k/2},\qquad K=2C\gamma/T_0.
$$
Two different things must both be uniform in $i$:
- The curvature magnitude $K=2C\gamma/T_0=2C\sqrt{1+K_0}/\theta$ (using $\gamma\lesssim r^2\sqrt{1+K_0}$, $T_0=\theta r^2$). The $r^2$ cancels, so **$K$ is $r$-independent** — good.
- The derivative prefactor $(T_0/2)^{-k/2}=(\theta r^2/2)^{-k/2}$, which for $k\ge1$ **blows up as $r\to0$**.

So the derivative bounds are uniform only if the working scale $r$ is bounded below. Now $r$ is an $\varepsilon$-regularity scale ($r=(\varepsilon_{\mathrm{Li}}/K_0)^{1/4}$ in the script), fixed only when the **local** $L^2$-curvature density $K_0$ is uniformly bounded. The Chern–Weil bound controls only the **total** $\int_M|\operatorname{Rm}|^2$ (topological). For a near-Einstein sequence, curvature can concentrate (instanton bubbling in the collapse), making $r_i\to0$, $T_{0,i}\to0$, and $(T_0/2)^{-k/2}\to\infty$. The script's Part 3 uses a single fixed $r\approx0.19$ and therefore does not exhibit this — it silently assumes the uniformity it needs to prove. Step 20 §5 itself records that the required per-component/finite-neighbor local energy budget $\int_{B_{10r}}F^2\le K_0\mathrm{Vol}(B_{10r})$ is not established. **Conclusion: (b) holds only modulo a uniform lower bound on the $\varepsilon$-regularity scale, i.e. a uniform local $L^2$-curvature density — the same input the notes leave open.** This is not cosmetic; it is the collapse-with-concentration scenario that the whole compactness step must survive, and it is where the good-center selection must be shown to land away from concentration on a positive-volume set.

**(c) Smooth compactness on the exponential chart.** Given uniform $|\nabla^k\operatorname{Rm}|$ (i.e. granting (b)), the pullback $h_i=\exp_{p_i}^*g_i(T_0)$ on $B_R(0)$ with $R<\pi/(2\sqrt K)$ (below the conjugate radius) is a diffeomorphism onto its image; covariant derivatives pull back to covariant derivatives, so $|\nabla^k\operatorname{Rm}_{h_i}|\le C_k$ transfers exactly (no loss here). Rauch gives $\mathrm{Vol}(B_R,h_i)\ge c_4R^4$ from the two-sided sectional bound (which follows from the $|\operatorname{Rm}|$ bound), independent of global injectivity radius or collapse — the pullback unwraps short geodesic loops. Uniform $C^k$ control of the metric coefficients in exponential coordinates then follows, and Arzelà–Ascoli yields $C^\infty$ convergence on $B_{R/2}$. This step is correct **once (b) is granted**. Its uniformity inherits the $r$-lower-bound dependency of (b).

---

### (3) Exponential chart to the projector contradiction

**(a) $|E_i(T_0)|\to0$.** On the plateau $\chi=1$, so $|E_i(T_0)|\le C\delta_i(r^2/T_0)^{1/3}=C\delta_i\theta^{-1/3}\to0$. With $h_i\to h_\infty$ in $C^\infty$, $\operatorname{Ric}_{h_i}\to\operatorname{Ric}_{h_\infty}$ and $|E_i|\to0$ uniformly, giving $\operatorname{Ric}_{h_\infty}=-h_\infty$ on $B_{R/2}$ — a **local** Einstein germ, which is exactly what the pointwise obstruction needs. Correct.

**(b) 7/24 transfer.** The inequality $\int_M(|W^+|-\tfrac1{2\sqrt6})^2\,d\mu\le\tfrac7{24}\int_M|E|^2\,d\mu$ is a metric-by-metric global statement, hence valid at $g_i(T_0)$. With $Q(T_0)\le2Q(0)\le2\delta_i^2\mathrm{Vol}\to0$ (the factor $Q(T_0)\le2Q(0)$ is itself the triangular energy statement (4.1)–(4.2), part of the conditional package), $|W^+|\to\tfrac1{2\sqrt6}$ in $L^2(M,g_i(T_0))$. The pushforward to a chart is done correctly by the exponential-pullback averaging lemma (Step 16 §3): bundling all nonnegative densities into $\mathcal D_i$ and applying (A) to $F=\mathcal D_i$ selects one center where the chart-average of the entire sum tends to zero. I verified the lemma's Rauch/Liouville proof structure; it is valid and genuinely collapse- and sheet-independent.

One quantitative point to secure: the selection uses
$$
\min_{p\in P_{\mathrm{inner}}}\ \fint_{B_R}\mathcal D_i\ \le\ \frac{C\int_M\mathcal D_i}{\mathrm{Vol}(P_{\mathrm{inner}})},
$$
so a good center exists only if $\int_M\mathcal D_i=o(\mathrm{Vol}(P_{\mathrm{inner}}))$. Since $\int_M\mathcal D_i\sim\delta_i^2\mathrm{Vol}(M)$ and $\mathrm{Vol}(P_{\mathrm{inner}})$ is a fraction of $\mathrm{Vol}(M)$, the ratio is $\sim\delta_i^2\to0$ **provided $\mathrm{Vol}_{g_i}(P_{\mathrm{inner}})/\mathrm{Vol}_{g_i}(M)$ stays bounded below**. If curvature/volume concentrates outside the plateau this fraction can degenerate. This is the same local-volume-comparison need as (2b); it should be tracked explicitly.

**(c) Projector obstruction — verified algebra.** I checked this in detail and it is the strongest link.

- The monopole saturation $\langle\mathscr A_\infty H_\infty,H_\infty\rangle=0$ with $\mathscr A=W^++\sqrt{2/3}\,|W^+|\,I$ forces two things at once. For any trace-free symmetric $W^+$ on $\Lambda^+$, the lowest eigenvalue satisfies $w_1\ge-\sqrt{2/3}\,|W^+|$, with equality **iff** the spectrum has the shape $(-2\mu,\mu,\mu)$ (check: $|W^+|^2=6\mu^2$, $\sqrt{2/3}\,|W^+|=2\mu=-w_1$). So $\mathscr A\ge0$ always, and kernel-saturation forces both the double-eigenvalue shape and $H_\infty$ = lowest eigenform. This is self-contained; no separate third condition is needed.
- Combining with $|W^+_\infty|^2=1/24$: $\mu=1/12$, so $\operatorname{Spec}(W^+_\infty)=(-1/6,1/12,1/12)$. I reconfirmed independently: sum $=0$, $\tfrac1{36}+\tfrac2{144}=\tfrac1{24}$. Correct and unique given the saturation.
- Internal consistency of the calibration value: $q=\sqrt6|W^+|-s=9/2$ with $s=-4$ gives $\sqrt6|W^+|=1/2$, i.e. $|W^+|=\tfrac1{2\sqrt6}$, matching the calibration target. So the §4 monopole weight and the 7/24 value agree. (Whether the constant $9/2$ is the correct LeBrun/Seiberg–Witten saturation for the Ishida–LeBrun family is a source-grounding matter I cannot settle from these notes; it should be traced to the cited estimate.)

- The contradiction. A parallel simple eigenform is a parallel self-dual 2-form of constant norm, forcing holonomy in $U(2)$, i.e. Kähler. A Kähler–Einstein 4-manifold has $\operatorname{Spec}(W^+)=(s/6,-s/12,-s/12)$ with $|W^+|^2=s^2/24$. For $s=-4$ this is $|W^+|^2=2/3$, whereas the limit has $|W^+|^2=1/24$. These are incompatible — **this is a clean, fully verifiable contradiction** (note both spectra share the $(-2\mu,\mu,\mu)$ shape, so they differ only in overall scale, exactly the norm). 

  The note instead packages the contradiction as "$\nabla W^+=0$ vs $|\nabla W^+|^2=1/16$." I could not reproduce the pointwise number $1/16$ from the material supplied (a pointwise $|\nabla W^+|^2$ value does not follow from the integral Weitzenböck formula, and the Step 6 computation is not in these files). The two framings should coincide; I recommend reconciling the $1/16$ against the Step 6 derivation, or simply replacing it with the transparent Kähler-norm contradiction $2/3\ne1/24$, which needs no additional identity. Also, the Derdziński-type step "simple eigenvalue of constant multiplicity $\Rightarrow$ eigenform parallel" is standard but is the one analytic input in this block that is invoked rather than reproduced here; it should be stated with its actual hypotheses (constant eigenvalue multiplicity + Einstein + divergence-free $W^+$).

---

### (4) Gaps in the chain, in order of weight

1. **The zero-order engine (U1–U3) is entirely unproven.** Everything downstream — (F4), the defect bound $|\chi^2E|\le C\delta(r^2/t)^{1/3}$, the triangular $Q(T_0)\le2Q(0)$, and hence the first-exit closure to time $T_0$ — rests on deriving (11.1): the nested finite-neighbor time–space energy recurrence with evolving measure and regularization at $a=0$. The infinite-product scaling (§10–11) and the endpoint exponents check out arithmetically (I confirm $\sum 1/q_j=3/q_0$ and the convergence of $\sum(j+\log q_j)/q_j$, and the endpoint substitutions $M_2\Rightarrow\gamma/t$, $M_6\Rightarrow\delta(r^2/t)^{1/3}$), but these verify only that a correct recurrence *would* produce the right outputs. The recurrence itself is not written. This is the load-bearing open problem, correctly identified as such in the notes.

2. **Uniformity of the working scale $r$ (points 2b, 3b).** The conversion of the topological Chern–Weil bound into a *uniform local* $L^2$-curvature density — equivalently a uniform lower bound on $r_i$ and hence uniform Shi derivative prefactors $(T_0/2)^{-k/2}$ and a non-degenerate good-center volume fraction — is the second pivotal open input. Without it, the smooth compactness in (2c) and the center selection in (3b) are not uniform in $i$.

3. **Global $Q$ through the chart.** Metric comparability (F1) does correctly transfer $\int_M|E|^2$ between $d\mu_{g(t)}$ and $d\mu_{g_0}$ up to a bounded factor, so the $Q\to0$ conclusion survives the bilipschitz change. The remaining need is the volume-fraction lower bound in (3b); with it, the averaging lemma transfers the vanishing $L^2$ defect to the chart correctly.

4. **Nontrivial monopole data on the limit.** The Seiberg–Witten basic class is a smooth invariant, nonzero for the Ishida–LeBrun manifolds at every metric — so a nonzero $g_i(T_0)$-monopole exists. The positive-part repair $r_i=q_i^+$ and the bundled amplitude density correctly force $|H_\infty|=\tfrac3{4\sqrt2\pi}>0$ on the chart, provided the deficit estimates (H),(L) hold and the amplitude density is a genuine pointwise-transferable lower bound (not merely an $L^2$-small deficit). The notes flag the SW existence input and the analytic passage to the chart limit as not yet written; the algebra of the deficit decomposition is script-verified, the analysis is not.

5. **No genuine gap in the chart pullback of derivative bounds (point 4 last part).** As in (2c), $\exp_{p_i}$ within the conjugate radius transfers $|\nabla^k\operatorname{Rm}|$ exactly. This step is clean.

---

### Synthesis

The **local obstruction machinery is correct and independently checkable**: the operator inequality $\mathscr A\ge0$ with its saturation, the forced spectrum $(-1/6,1/12,1/12)$, and the parallel-eigenform-vs-Kähler-norm contradiction all verify by direct algebra. The **structural reduction** — moving all derivative control to positive-time interior Shi estimates on the fixed plateau and thereby eliminating any time-zero Bernstein or connection-drift estimate — is logically sound and is a real simplification of the program.

The two things that are genuinely not established, and on which the entire conditional result depends, are: (i) the nested weighted Moser recurrence (U1–U3), and (ii) the uniform local $L^2$-curvature density / uniform $r$ that makes both the Shi constants and the good-center volume fraction uniform along the pinching sequence. These are exactly the items the notes themselves list as open. Two smaller technical items to settle: recompute the additive normalization source in (2.1) (the stated $r^{-2q}$ power is not what the by-parts computation gives), and reconcile the $|\nabla W^+|^2=1/16$ number with the Step 6 derivation (or replace it with the $2/3\ne1/24$ Kähler-norm contradiction, which I verified directly).

Everything here concerns the fixed critical Ishida–LeBrun 4-manifold negative branch; the unrestricted negative branch, the positive branch, $n\ge5$, the dimension-only quantifiers of Problem 26, and the Lean formalization are untouched by this chain, consistent with the notes' own statement of what a completed U1–U3 would yield.