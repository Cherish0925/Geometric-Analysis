# Step 17: Normalized cutoff flow with automatic defect preservation and volume-independent constants

> **Step 18 replacement notice.** The unconditional language in this note is superseded by `workspace/notes/step18_simultaneous_bootstrap_and_fixed_p_defect.md`. The coupled L² inequalities are a lemma inside a simultaneous first-exit argument and assume provisional metric/Sobolev/cover/energy control. A bound `|a Rm| <= C/t` does **not** preserve the initial defect through the maximum principle because `∫_0^T dt/t` diverges. Metric comparability must instead come from an integrable weighted-defect estimate `|aE| <= C_p δ(r²/t)^(2/p)`, `p>2`. The topology-uniformity sentence using BMY also had the inequality in the wrong direction; for minimal general-type summands the correct upper bound comes from Noether plus `b_+(N)=0`.

## 0. Purpose and advance

This historical Step 17 note attempted a transition-inclusive normalized cutoff-flow theorem for the four-dimensional negative-branch program. Step 18 showed that pointwise defect is not automatically preserved by the maximum principle and that all integral estimates belong inside a simultaneous first-exit bootstrap. The valid ingredients retained here are the exact defect identity and collapse-volume cancellation; use the Step 18 replacement note for the current construction.

Building on:
- Step 14: cutoff flow homogeneity and the `C_a(E)` formula
- Step 15: the 7/24 L² completion-square chain (valid, metric-independent)
- Step 16: withdrawal of the plateau localization, exponential-chart averaging lemma, q⁺ monopole repair

## 1. The maximum principle for the Einstein defect

Consider the normalized cutoff flow on a closed 4-manifold $(M,g_0)$:
$$
\partial_t g = -2a E, \qquad a = \chi^2, \quad E = \operatorname{Ric} + g.
$$

From Step 14, the defect evolution is:
$$
\partial_t E = a(\Delta_L E - 2E) + \mathcal{C}_a(E)
$$
where $\mathcal{C}_a(0) = 0$ (homogeneity). For the squared norm:
$$
\partial_t |E|^2 = 2\langle E, a(\Delta_L E - 2E)\rangle + 2\langle E, \mathcal{C}_a(E)\rangle.
$$

**TTCS CORRECTION (Step 17 turn 4).** The original version claimed a residual $-4a\operatorname{tr}(E^3)$ cubic term. Independent TTCS verification found this is incorrect: the inverse-metric variation $\partial_t g^{ij} = 2aE^{ij}$ contributes an additional $+4a\operatorname{tr}(E^3)$ that **exactly cancels** the Lichnerowicz residual. The correct evolution is:

$$
(\partial_t - a\Delta)|E|^2 = -2a|\nabla E|^2 + 4a\operatorname{Rm}(E,E) + 2\langle E, \mathcal{C}_a(E)\rangle.
\tag{*}
$$

**Derivation.** Since $|E|^2 = g^{ia}g^{jb}E_{ij}E_{ab}$ and $\partial_t g^{ij} = 2aE^{ij}$:
$$
\partial_t|E|^2 = 2\langle E, \partial_t E\rangle + 4a\operatorname{tr}(E^3).
$$

The Lichnerowicz contribution gives:
$$
2a\langle E, \Delta_L E\rangle = a\Delta|E|^2 - 2a|\nabla E|^2 + 4a\operatorname{Rm}(E,E) - 4a\operatorname{Ric}(E,E).
$$

Since $\operatorname{Ric} = E - g$, $\operatorname{Ric}(E,E) = \operatorname{tr}(E^3) - |E|^2$. The $-2E$ damping gives $-4a|E|^2$. Combining:
$$
-4a\operatorname{Ric}(E,E) - 4a|E|^2 = -4a\operatorname{tr}(E^3) + 4a|E|^2 - 4a|E|^2 = -4a\operatorname{tr}(E^3).
$$

Adding the inverse-metric contribution $+4a\operatorname{tr}(E^3)$: **total cubic = 0**. This yields $(*)$, which is actually the same identity as Step 14 (consistent check). The reaction is $4a\operatorname{Rm}(E,E)$ plus cutoff terms — no explicit $|E|^3$ or $|E|^2$ reaction beyond what $\operatorname{Rm}$ and cutoff derivatives provide.

For the cutoff terms, using $|da|^2/a = 4|d\chi|^2$ and Young's inequality:
$$
|2\langle E, \mathcal{C}_a(E)\rangle| \le \varepsilon a|\nabla E|^2 + C_\varepsilon\left(|\nabla^2 a| + \frac{|\nabla a|^2}{a}\right)|E|^2.
$$

**Defect maximum principle (corrected scope).** At a maximum point of $|E|^2$ in $\{a > 0\}$:
$$
\frac{d}{dt}\sup|E|^2 \le B(t)\sup|E|^2, \qquad B(t) = C\left(\|a\operatorname{Rm}(g(t))\|_\infty + \|\nabla^2_{g(t)}a\|_\infty + \frac{|\nabla a|^2}{a}\right).
\tag{MP}
$$

The cutoff terms $|\nabla a|^2/a = 4|\nabla\chi|^2 \le Cr^{-2}$ and $|\nabla^2 a| \le C r^{-2}$ are controlled by the smooth fixed cutoff. **However**, $\|a\operatorname{Rm}(g(t))\|_\infty$ depends on the curvature at time $t$, which is not controlled by the initial data alone: $C^0$ metric closeness does not bound second-order quantities.

**Corrected Proposition 1.** *If* $\|a\operatorname{Rm}(g(t))\|_\infty \le K(t)$ with $\int_0^T K(t)dt < \infty$, then:
$$
\|E(t)\|_\infty \le \delta \exp\left(\int_0^t B(s)ds\right).
$$
If $K(t)=C/t$, the integral from zero diverges. Starting at a positive auxiliary time only gives a factor `(t/t_0)^C`, which is not uniform as `t_0 -> 0`; therefore this maximum principle does not preserve an `O(δ)` defect from the initial slice.

The maximum principle is useful only when its full coefficient is integrable from the initial slice. A `C/t` weighted curvature bound does not meet this requirement, and the evolving cutoff Hessian also remains coupled.

## 2. Withdrawn automatic metric-equivalence argument

Since $\partial_t g = -2aE$ with $|E(t)| \le \sqrt{2}\,\delta$:
$$
\left|\frac{d}{dt}\log|v|_{g(t)}^2\right| \le 2|E(t)| \le 2\sqrt{2}\,\delta.
$$

Over time $\theta r^2$:
$$
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right| \le 2\sqrt{2}\,\delta\theta r^2 \to 0 \text{ as } \delta \to 0.
\tag{ME}
$$

In particular, for $\delta\theta r^2 \le 1/10$: $g(t)$ and $g_0$ are within factor $2$. Consequently:
- Sobolev constants are preserved within factor $C$.
- Volume is preserved within factor $C$.
- Ball comparability from Bishop–Gromov persists.

This calculation is conditional on the unproved persistence `|E(t)| <= sqrt(2)δ`; it is not a consequence of the initial defect alone. Step 18 replaces it by an integrable estimate for `aE`.

## 3. Volume cancellation in the 4D Li estimate

The Li smoothing radius $r_*$ is determined by the all-centres dimensionless curvature energy:
$$
\varepsilon(r,x) = \frac{r^4}{\operatorname{Vol}(B_r(x))}\int_{B_r(x)}|\operatorname{Rm}|^2.
$$

In 4D, the local Sobolev constant $A(B_r) \sim C r^2/\operatorname{Vol}(B_r)^{1/2}$ (Gallot, from $\operatorname{Ric} \ge -3g$). Li's Corollary 3.5 gives, for the defect subsolution:
$$
|E(x,t)| \le C\cdot A^{2/3}\cdot t^{-2/3}\cdot\left(\int_{B_{3r}}|E_0|^3\right)^{1/3}.
$$

Substituting:
$$
A^{2/3}\left(\int_{B_{3r}}|E_0|^3\right)^{1/3}
\le C\left(\frac{r^2}{\operatorname{Vol}^{1/2}}\right)^{2/3}\cdot\delta\cdot\operatorname{Vol}_{3r}^{1/3}
= C\,r^{4/3}\cdot\operatorname{Vol}^{-1/3}\cdot\delta\cdot\operatorname{Vol}_{3r}^{1/3}.
$$

By Bishop–Gromov: $\operatorname{Vol}_{3r}/\operatorname{Vol}_r \le C(n, Kr^2)$ is universal. Therefore:
$$
\boxed{|E(x,t)| \le C\delta\left(\frac{r^2}{t}\right)^{2/3}}
$$
with $C$ depending **only on dimension and the Ricci bound**, not on the collapsed volume. This is the critical 4D volume cancellation.

## 4. Good-set selection and cutoff construction

On $(M^4, g_i)$ with $|E_i| \le \delta_i$, define the mean curvature energy:
$$
\bar K_i = \frac{1}{\operatorname{Vol}(g_i)}\int_M|\operatorname{Rm}(g_i)|^2.
$$

The Hardy–Littlewood maximal function with Ricci-doubling gives the good set:
$$
G_i = \{p \in M : \mathcal{M}_r(|\operatorname{Rm}|^2)(p) \le 2\bar K_i\},
\qquad \operatorname{Vol}(G_i) \ge \frac12\operatorname{Vol}(M).
$$

At every $p \in G_i$ and every scale $s \le r$:
$$
\frac{r^4}{\operatorname{Vol}(B_r(p))}\int_{B_r(p)}|\operatorname{Rm}|^2 \le r^4\cdot 2\bar K_i.
$$

Choosing $r_* = (\varepsilon_{\mathrm{Li}}/(2\bar K_i))^{1/4}$ makes the dimensionless energy $\le \varepsilon_{\mathrm{Li}}$ on $G_i$.

**Crucial observation: $\bar K_i$ is uniformly bounded under bounded $\chi/A$.**

By Chern–Gauss–Bonnet and the near-Einstein profile:
$$
\int|\operatorname{Rm}|^2 \le 8\pi^2\chi + C\delta^2\operatorname{Vol} + C\operatorname{Vol},
$$
and $\operatorname{Vol} \to 32\pi^2 A/9$. So:
$$
\bar K_i = \frac{\int|\operatorname{Rm}|^2}{\operatorname{Vol}} \le \frac{9\chi}{4A} + C.
$$

A uniform **upper** bound on `χ(M)/A` is needed here. BMY gives a lower bound in the wrong direction. For minimal general-type summands, Step 18 instead derives `c₂(X_j) <= 5c₁²(X_j)+36` from Noether and combines it with the standard `b_+(N)=0` hypothesis and `D=A/3`, yielding `χ(M)/A <= 65/6`. This uniformity does not automatically cover arbitrary symplectic summands.

**Cutoff construction.** Choose $\chi_i$ supported on $G_i^{-D}$ (the good set eroded by $D = 5r_*$) with:
- $\chi_i = 1$ on $G_i^{-2D}$ (eroded by $10r_*$)
- $|\nabla\chi_i| \le C/D$, $|\nabla^2\chi_i| \le C/D^2$

The wide buffer $D \gg r_*$ ensures that for every $x \in \{\chi = 1\}$ and every covering center $y \in B_{3r_*/2}(x)$, the ball $B_{r_*}(y)$ lies entirely within $G_i$. The Li all-centres condition is satisfied on the buffered plateau.

The plateau volume: $\operatorname{Vol}(\{\chi_i = 1\}) \ge \operatorname{Vol}(M)/2 - C\cdot D\cdot(\text{boundary measure})$. Under Ric $\ge -3g$, the isoperimetric profile gives $\operatorname{Vol}(\{\chi = 1\}) \ge \theta\operatorname{Vol}(M)$ with $\theta > 0$ depending only on $\bar K$, $r_*$, and the Ricci bound.

## 5. The complete flow argument

**Theorem (Conditional).** Fix dimensional constants. Let $(M^4, g_0)$ be a closed 4-manifold with $\operatorname{Ric}_{g_0} \ge -3g_0$ and $|E_0| = |\operatorname{Ric} + g_0| \le \delta$. Let $\bar K = \operatorname{Vol}^{-1}\int|\operatorname{Rm}|^2$, and let $\chi$ be the cutoff from Section 4. Then for the normalized cutoff flow $\partial_t g = -2\chi^2 E$ with $g(0) = g_0$:

(a) **Defect preservation** (Proposition 1): $|E(t)| \le \sqrt{2}\,\delta$ for $t \in [0, \theta r_*^2]$.

(b) **Metric equivalence** (Section 2): $e^{-C\delta\theta r_*^2}g_0 \le g(t) \le e^{C\delta\theta r_*^2}g_0$.

(c) **Plateau curvature smoothing**: On $\{\chi = 1\}$, genuine normalized Ricci flow gives $|\operatorname{Rm}(t)| \le C/t$ by Li's Theorem 3.4, using the good-set energy condition and preserved Sobolev/metric constants.

(d) **Plateau defect decay**: On $\{\chi = 1\}$, Li's Corollary 3.5 gives $|E(t)| \le C\delta(r_*^2/t)^{2/3}$.

(e) **Global L² preservation**: $Q(t) = \int_M|E(t)|^2 \le C\cdot Q(0)$, where $C$ depends only on $\bar K$, $r_*$, and the dimension.

(f) **L² calibration**: For every evolved metric $g(t)$ on the critical Ishida–LeBrun manifold:
$$
\int_M\left(|W^+(g(t))| - \frac{1}{2\sqrt{6}}\right)^2 d\mu_{g(t)} \le \frac{7}{24}\int_M|E(t)|^2 d\mu_{g(t)} \le \frac{7C}{24}Q(0).
$$

All constants in (a)–(f) depend only on dimension and $\bar K$, not on $\operatorname{Vol}(M)$ or the specific topology.

## 6. Curvature energy propagation for the normalized flow

On the plateau $\{\chi = 1\}$, the flow is the standard normalized Ricci flow $\partial_tg = -2(\operatorname{Ric}+g)$. The curvature evolution includes the normalization term:
$$
\partial_t\operatorname{Rm} = \Delta\operatorname{Rm} + \operatorname{Rm}^2 - 2\operatorname{Rm} + [\nabla^2(g)]_{\text{correction}}.
$$

The last term arises because the normalization $-2g$ changes the Christoffel symbols by:
$$
\delta\Gamma^k_{ij}|_{-2g} = g^{kl}(-\partial_i g_{jl} - \partial_j g_{il} + \partial_l g_{ij}) = 0.
$$

**Christoffel symbols are unchanged by a constant conformal shift** (since $\nabla g = 0$). Hence $\delta R^k_{\ lij}|_{-2g} = 0$, and the (4,0)-tensor changes only through the metric lowering: $\delta R_{ijkl}|_{-2g} = -2R_{ijkl}$.

On the plateau, the curvature energy evolution is:
$$
\frac{d}{dt}\int_{\text{plateau}}|\operatorname{Rm}|^2 = (\text{standard RF terms}) + 4\int|\operatorname{Rm}|^2 + 4\int|\operatorname{Rm}|^2\cdot(\text{vol change})
$$

The extra $4\int|\operatorname{Rm}|^2$ and volume change $n\int|\operatorname{Rm}|^2$ give a Gronwall factor $e^{Ct}$, absorbed over time $\theta r_*^2$ by adjustment of $\theta$.

On the transition ($0 < \chi < 1$), the localized conformal term $-2\chi^2 g$ changes Christoffel symbols by:
$$
\delta\Gamma^k_{ij}|_{-2\chi^2g} = -(\partial_i\chi^2)\delta^k_j - (\partial_j\chi^2)\delta^k_i + g_{ij}\partial^k\chi^2
$$
which is $O(r_*^{-1})$. The induced Riemann change is $O(r_*^{-2})$ (from $\nabla^2\chi^2$). For the energy:
$$
\left|\frac{d}{dt}\int|\operatorname{Rm}|^2\right|_{\text{transition}}
\le C r_*^{-2}\int|\operatorname{Rm}| + C\int|\operatorname{Rm}|^2.
$$

By Young: $r_*^{-2}\int|\operatorname{Rm}| \le \varepsilon\int|\operatorname{Rm}|^2 + C/(\varepsilon r_*^4)$. In normalized form $F = r_*^4/V\int|\operatorname{Rm}|^2$, the additive term is $C\theta r_*^4\bar K^{1/2}$, which is $O(\theta r_*^4)$ for bounded $\bar K$ — negligible compared to the Li threshold $\varepsilon_{\rm Li}$.

## 7. THE KEY NEW RESULT: the coupled L² energy system closes

Independent TTCS verification confirmed that the coupled energy system from Step 16 (equations (E)+(R)) **closes at the L² level** via the 4D Sobolev-energy cancellation. This is the strongest analytical result established in this step.

**Theorem (Coupled L² energy propagation).** Under the hypotheses of Section 5, define normalized local energies on a finite-overlap cover $\{U_\alpha\}$ of the active support:
$$
R_\alpha = \frac{r^4}{V_\alpha}\int_{\eta_\alpha^2}|\operatorname{Rm}|^2, \qquad
P_\alpha = \frac{r^4}{V_\alpha}\int_{\eta_\alpha^2}|E|^2,
$$
with gradient dissipations $X_\alpha, Y_\alpha$ defined analogously. Then:

$$
\begin{aligned}
\dot R_\alpha + cX_\alpha &\le Cr^{-2}\sum_{\beta\sim\alpha}(R_\beta + P_\beta) + \epsilon_1 Y_\alpha, \\
\dot P_\alpha + cY_\alpha &\le Cr^{-2}\sum_{\beta\sim\alpha}P_\beta.
\end{aligned}
\tag{C}
$$

**Proof of the critical absorption.** The dangerous term $\int\eta^2 a|\operatorname{Rm}||E|^2$ is controlled by:
$$
\int a|\operatorname{Rm}||E|^2 \le \|\operatorname{Rm}\|_{L^2(U_\alpha)} \cdot \|\eta\sqrt{a}E\|_{L^4}^2
\le C\sqrt{R_\alpha/r^4} \cdot C_S \cdot (Y_\alpha + r^{-2}P_\alpha).
$$

The 4D volume cancellation gives: $C_S \cdot \|\operatorname{Rm}\|_{L^2} \sim (r^4/V)^{1/2} \cdot (V\bar K)^{1/2} = r^2\bar K^{1/2}$, which equals $\sqrt{\varepsilon_*/r^4} \cdot r^2 = \sqrt{\varepsilon_*}$. For $\varepsilon_*$ small, this absorbs the $Y_\alpha$ term. The cubic curvature term $\int\eta^2 a|\operatorname{Rm}|^3$ is absorbed identically.

The cross term $\int|\nabla a||\nabla E||\operatorname{Rm}|$ from the cutoff Hessian is handled by integrating by parts (removing $\nabla^2 a$ in favor of products of first derivatives) and applying Young:
$$
\int|\nabla a||\nabla E||\operatorname{Rm}| \le \epsilon Y_\alpha + C_\epsilon r^{-2}\sum_{\beta\sim\alpha}R_\beta.
$$

For the combined energy $H_\alpha = R_\alpha + \kappa P_\alpha$ with $\kappa$ large:
$$
\dot H_\alpha + c'(X_\alpha + Y_\alpha) \le Cr^{-2}\sum_{\beta\sim\alpha}H_\beta.
$$

With bounded overlap $N$, Gronwall gives $H_*(t) = \sup_\alpha H_\alpha(t) \le e^{CN\theta}H_*(0)$ for $t \le \theta r^2$. For $\theta$ small: $\sup_\alpha R_\alpha(t) \le 2\varepsilon_*$.

Conditionally on the provisional evolving metric, relative Sobolev, cover, cutoff, and neighboring-energy bounds, this improves the local energy threshold with constants independent of collapsed volume. It is a bootstrap lemma, not an independent continuation theorem.

## 8. The continuation argument: precise remaining gap

The coupled L² energy system (Section 7) closes the integral layer. The maximum principle (Section 1, corrected) closes the defect→metric direction conditionally on curvature input. The hierarchy of what is established vs. what remains:

**Available only inside the simultaneous first-exit hypotheses unless explicitly stated otherwise:**
1. Coupled L² energy propagation: $\sup_\alpha R_\alpha(t) \le 2\varepsilon_*$ for $t \le \theta r^2$.
2. Defect maximum principle: $\|E(t)\|_\infty \le \delta\exp(\int_0^t B(s)ds)$, conditional on $B(t)$ being integrable.
3. `|a Rm| <= C/t` alone does not propagate `|E(0)| <= δ`, because its coefficient is nonintegrable at zero. Metric equivalence instead requires the integrable weighted-defect estimate developed in Step 18.
4. On the plateau ($a = 1$): Li's theorem gives $|\operatorname{Rm}| \le C/t$ from the L² energy smallness.

**Remaining coupled problem:** simultaneously improve metric comparability, relative Sobolev/cover geometry, local energies, weighted curvature-potential regularity, weighted defect, and connection/cutoff derivative control. Step 18 obtains a fixed-supercritical `L^p` bound for `aE` conditionally inside this system, but the degenerate curvature-potential and continuation estimates remain open.

On the **plateau** ($a = 1$), this is exactly Li's Theorem 3.4 (standard Moser iteration from L² to L^∞). On the **transition** ($0 < a < 1$), the operator degenerates and Li's theorem does not directly apply. The weighted bound $|a\operatorname{Rm}| \le C/t$ is the natural object because the effective diffusion scale at $\chi \ll 1$ is $\chi^2 t$, not $t$.

**The correct proof order** (from TTCS):
1. L² energy propagation: established by (C) system.
2. Degenerate Moser iteration: $R_\alpha \le \varepsilon_* \implies \|a\operatorname{Rm}\|_\infty \le C/t$.
3. Defect L^p→L^∞: $\|aE(t)\|_\infty \le C_p\delta(r^2/t)^{2/p}$, $p > 2$ (integrable exponent).
4. Metric drift: $\int_0^T \|aE\|_\infty dt \le C\delta r^2$ (integrable).
5. Continuation: weighted curvature + local higher-order estimates complete the flow.

The previously identified continuation circle was:
- Need metric equivalence to preserve Sobolev → need curvature bound → need Li bootstrap → need Sobolev → need metric equivalence.

For the **normalized** cutoff flow, this circle is broken at the first step:

This paragraph is withdrawn. Metric equivalence is provisionally assumed up to a first exit time and must be improved by the integrable `p>2` estimate for `aE`; neither the initial curvature nor a `C/t` bound closes the maximum-principle argument from time zero.

With metric equivalence in hand, the curvature energy propagation runs on the plateau exactly as in Li's proof: the all-centres condition is initially satisfied (from good-set selection), the critical absorption works (4D volume cancellation), and the Gronwall factor from the normalization is bounded. This gives $|\operatorname{Rm}| \le C/t$ on the plateau, and then Corollary 3.5 gives defect decay.

For the **global** L² estimate: the defect energy inequality with $\eta = 1$ gives:
$$
\frac{d}{dt}Q \le C(r_*^{-2} + K_0)Q
$$
The following old argument is invalid: metric closeness does not bound transition curvature, and `C/t` is not integrable at zero:
$$
Q(\theta r_*^2) \le Q(0)\exp\left(C\theta + C\int_0^{\theta r_*^2}\frac{dt}{t}\right) \le Q(0)\exp(C\theta + C\log(\theta r_*^2/\varepsilon))
$$

The logarithmic divergence requires a lower time cutoff: start the L² estimate at time $t_0 = \varepsilon^2$. For $t \in [\varepsilon^2, \theta r_*^2]$: 
$$
Q(t) \le Q(\varepsilon^2)\exp(C\theta + C\log(\theta r_*^2/\varepsilon^2)) \le Q(\varepsilon^2)\cdot C'
$$

And $Q(\varepsilon^2) \le C Q(0)$ by the initial Gronwall with bounded $K_0$. So $Q(t) \le C'' Q(0)$.

**Remark.** The 1/t growth factor on the plateau does not obstruct the L² estimate because the defect on the plateau decays faster than the curvature grows: $|E(t)| \le C\delta(r^2/t)^{2/3}$, so the plateau contribution to Q actually *decreases* with time.

## 8. Volume-normalized form and varying topology

The Strategist's key observation: the exponential chart lemma (Step 16) converts the volume-normalized defect $Q/\operatorname{Vol}$ into a chart-averaged defect. The argument needs $Q(t)/\operatorname{Vol}(g(t)) \to 0$, not $Q(t) \to 0$ absolutely.

Since $Q(t) \le CQ(0) = C\delta^2\operatorname{Vol}$ and volume is preserved to within factor 2:
$$
\frac{Q(t)}{\operatorname{Vol}(g(t))} \le C'\delta^2 \to 0.
$$

For the exponential chart selection: with plateau set $P$ having $\operatorname{Vol}(P) \ge \theta\operatorname{Vol}(M)$:
$$
\operatorname{avg}_{\text{chart}}(\mathcal{D}_i) \le \frac{C(n,K,r_*)}{\theta}\cdot\frac{\int\mathcal{D}_i}{\operatorname{Vol}(M)} \le \frac{C}{\theta}\cdot\delta_i^2 \to 0.
$$

Here $\mathcal{D}$ is the joint density from Step 16 Section 4:
$$
\mathcal{D} = |E|^2 + (q^+ - 9/2)^2 + \text{(amplitude error)} + 2\langle\mathscr{A}H, H\rangle.
$$

**This does not require fixed topology.** The constants depend on:
- $\bar K$ (uniformly bounded when $\chi/A$ is bounded)
- $r_*$ (determined by $\bar K$ and $\varepsilon_{\rm Li}$)
- $\theta$ (positive volume proportion, determined by $\bar K$ and the Ricci bound)
- Dimensional constants

**Theorem (Uniform gap for bounded $\chi/A$ critical families).** Let $\{M_j\}$ be a family of critical Ishida–LeBrun 4-manifolds with $D_j = A_j/3$ and $\chi(M_j)/A_j \le \Lambda$. If the cutoff-flow construction (Sections 5–7) is valid, then there exists $\delta_0 = \delta_0(\Lambda) > 0$ such that for every $j$ and every smooth metric $g$ on $M_j$:
$$
\|\operatorname{Ric}_g + g\|_\infty \ge \delta_0.
$$

This remains conditional on the unresolved simultaneous flow theorem. For minimal general-type summands, the needed upper bound is automatic only after using Noether and the standard `b_+(N)=0` hypothesis; Step 18 obtains `χ(M)/A <= 65/6`. BMY alone does not do this.

## 9. Status of the analytic bridge

The maximum-principle evolution formula is valid, but metric equivalence is not proved merely from flow existence. The remaining analytic inputs must be improved together in a first-exit argument:

**(A) Short-time existence** of the normalized cutoff flow on a closed manifold. The equation $\partial_tg = -2\chi^2(\operatorname{Ric}+g)$ is a degenerate parabolic system: it degenerates at $\{\chi = 0\}$ but is smoothly parabolic on $\{a > 0\}$. Yang's framework (extended by Wang) establishes short-time existence for the unnormalized local Ricci flow $\partial_tg = -2\chi^2\operatorname{Ric}$ on closed manifolds. The extra $-2\chi^2g$ term has bounded coefficients and does not affect the parabolic type. **This input is standard.**

**(B) Li's curvature bootstrap on the plateau.** Li's Theorem 3.4 uses the bootstrap variable $e_0 = \sup_{x \in M}(\int_{B_r(x)}f^2)^{1/2}$. On the plateau $\{\chi = 1\}$ with genuine normalized Ricci flow, all covering centres stay inside the good set (by the buffer construction in Section 4). On the frozen exterior $\{\chi = 0\}$: $f = |\operatorname{Rm}(g_0)|$, unchanged. The bootstrap works on both regions: on the plateau by the standard Li argument, on the frozen exterior trivially.

**The remaining genuine issue** is the transition region $0 < \chi < 1$, where the evolution is degenerate and Li's theorem does not directly apply. The curvature there is controlled at time 0 (good set), and the metric barely drifts, but the $\nabla^2\chi^2$ terms can seed curvature growth.

From Section 6: the curvature energy growth from transition terms is $O(\theta r_*^4\bar K^{1/2})$, which is negligible for small $\theta$. **But the transition curvature evolution is a full tensorial PDE, and the energy argument must be closed self-consistently.** The coupled system from Step 16 (equations (E)+(R)) provides the right framework; the maximum principle for $E$ breaks the circle at the metric-equivalence step, but the self-consistent curvature energy propagation in the transition region remains the precise open construction.

**Summary of what is established vs. what remains (TTCS-corrected):**

| Component | Status |
|-----------|--------|
| Coupled L² energy propagation | Bootstrap lemma under provisional evolving geometry/energy assumptions |
| Defect evolution identity (*) | **Proved** (cubic fully cancels) |
| Defect max principle (conditional) | **Proved** given $\|a\operatorname{Rm}\|_\infty$ integrable |
| 7/24 L² calibration | **Proved** (Step 15) |
| Li smoothing on plateau | Conditional on a full-support continuation argument controlling adjacent regions |
| Exponential chart lemma | **Proved** (Step 16) |
| q⁺ monopole repair | **Proved** (Step 16) |
| Joint chart selection density | **Proved** (Step 16) |
| Projector/Derdziński contradiction | **Proved** (Step 6) |
| Volume cancellation in fixed-energy reactions | Algebraically valid; continuation still open |
| Sequence-uniform lifespan/continuation | Not supplied by bare smooth short-time existence |
| Simultaneous weighted curvature/defect/connection/energy continuation | OPEN |

## 10. Path to completion

If the simultaneous first-exit package in Step 18 is established—including an integrable weighted-defect estimate, not only weighted curvature regularity—the downstream chain becomes:

1. Good-set selection with $r_* = (\varepsilon/(2\bar K))^{1/4}$, uniform when $\bar K$ bounded.
2. Vitali/thinning for disjoint supports (A01 Section 1.2).
3. Cutoff flow on the closed manifold.
4. Coupled L² energy propagation (Section 7).
5. Fixed-supercritical tensor propagation plus weighted curvature-potential regularity → `|aE| <= C_p δ(r²/t)^(2/p)`, `p>2`.
6. Integrate `aE` to improve metric equivalence while simultaneously improving energies, Sobolev/cover geometry, and cutoff/connection control.
7. Smooth the plateau and obtain terminal global unweighted defect control.
4. Defect decay on the plateau by Li Cor. 3.5.
5. Global $L^2$ defect preservation → topological calibration via 7/24 chain.
6. Exponential chart selection with joint amplitude/eigenline density.
7. Smooth local Einstein limit with calibrated $W^+$ spectrum.
8. Step 6 projector contradiction.
9. $\implies \inf_g \|\operatorname{Ric}_g + g\|_\infty \ge \delta_0 > 0$, uniform for bounded $\chi/A$.

Even this would settle only the negative branch for 4D critical Ishida–LeBrun families. The positive branch, $n \ge 5$, and Lean formalization remain open.

## Evidence paths

- Maximum principle: `workspace/scripts/verify_normalized_cutoff_maximum_principle.py`
- Cutoff defect identity: `workspace/scripts/verify_cutoff_defect_energy.py`
- L² chain: `workspace/scripts/verify_L2_completion_square_chain.py`, `verify_improved_constant.py`
- Step 16 exponential chart/monopole: `workspace/notes/step16_preceptor_correction_exponential_chart_and_cutoff_targets.md`
- Li source: `Knowledge/objects/papers/0911.3104...object.md`, citation `\cite{lismoothing}`
- Wang source: `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow...object.md`, citation `\cite{wang2009pseudolocality}`
