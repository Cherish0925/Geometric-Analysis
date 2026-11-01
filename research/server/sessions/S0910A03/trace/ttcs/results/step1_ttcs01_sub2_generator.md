# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A03/workspace/briefing/Session.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

The active goal is to prove or refute the dimensionwise existence of a nondegenerate Ricci pinching interval forcing the underlying closed smooth manifold to admit some Einstein metric. Develop the strongest serious counterexample mechanisms suggested by Einstein-orbifold resolution/gluing. In particular, derive carefully whether the refined approximate metrics in Morteza–Viaclovsky can have unweighted operator norm |g_t^{-1}(Ric(g_t)-Lambda g_t)| tending to zero after all scalings, including the ALE core, transition annulus, and obstruction term. Then identify what topology/global theorem would be needed to exclude every Einstein metric, not just nearby ones. Explore concrete orbifold/resolution choices and compute chi,tau where feasible. Do not assume the route works; expose exact fatal points and possible repairs.

## Output

## Framing: what a resolution/gluing counterexample must actually beat

The statement asserts existence of a fixed pair $c_n<C_n$. Refutation must defeat *every* pair. Two reductions sharpen where the resolution route can bite.

**Mixed-sign windows are already settled by scaling.** For any candidate window with $c_n<0<C_n$, take any closed $M^n$ with any metric $g_0$; since $g_0^{-1}\mathrm{Ric}_{g_0}$ has bounded eigenvalues $\subset[-K,K]$, the rescaling $g=sg_0$ has $\mathrm{Ric}_g=\mathrm{Ric}_{g_0}$ and eigenvalues of $g^{-1}\mathrm{Ric}_g$ still in $[-K,K]$, so $c_ng\le\mathrm{Ric}_g\le C_ng$ holds once $s\ge\max(K/C_n,K/|c_n|)$. Every closed $M^n$ then satisfies the hypothesis, so a mixed-sign window would force *every* closed manifold to be Einstein — refuted by any manifold outside the Einstein class. Hence a would-be prover is forced onto **same-sign windows**, and the real content is: does a *fixed-sign* Ricci pinching ratio close to $1$ force Einstein-admissibility. Because $\mathrm{Ric}$ is scale-invariant, the only invariant that matters is the pointwise eigenvalue ratio
$$\rho(M):=\inf_{g:\ \mathrm{Ric}_g>0}\ \sup_{p}\frac{\lambda_{\max}\big(g^{-1}\mathrm{Ric}_g\big)(p)}{\lambda_{\min}\big(g^{-1}\mathrm{Ric}_g\big)(p)},$$
and the positive part of Yau 26 is equivalent to $\inf\{\rho(M):M\text{ admits no Einstein metric}\}>1$. The resolution program is an attempt to make $\rho(M)$ near $1$ on a non-Einstein $M$.

## Mechanism 1: exact unweighted operator norm of the Morteza–Viaclovsky refined metric

Write $E_t:=g_t^{-1}\big(\mathrm{Ric}(g_t)-\Lambda g_t\big)$; the eigenvalues of $g_t^{-1}\mathrm{Ric}(g_t)$ are $\Lambda+\mathrm{spec}(E_t)$, so the pinching interval of $g_t$ is $[\Lambda+\min\mathrm{spec}\,E_t,\ \Lambda+\max\mathrm{spec}\,E_t]$. Compute $|E_t|_{\mathrm{op}}$ region by region using MV Lemmas 4.1–4.2.

- **Orbifold body** ($g_t=g_0$, $\mathrm{Ric}(g_0)=\Lambda g_0$): $E_t\equiv0$. Eigenvalue ratio exactly $1$ here.
- **ALE core** ($g_t=t\,h_t$, $h_t=g_{\mathrm{cal}}+th$): by Lemma 4.1, $\mathrm{Ric}(h_t)=t\Lambda h_t+t\lambda\,o+O(t^2\rho^2)$ in $g_{\mathrm{cal}}$-norm. Scale-invariance gives $\mathrm{Ric}(g_t)-\Lambda g_t=t\lambda\,o+O(t^2\rho^2)$, and $g_t^{-1}=t^{-1}g_{\mathrm{cal}}^{-1}(1+O(t))$. Therefore
$$E_t=\lambda\,g_{\mathrm{cal}}^{-1}o+O(t\rho^2),\qquad |E_t|_{\mathrm{op}}=|\lambda|\,\frac{n-1}{1+r^{2n}}+O(t^{1/2}).$$
The $g_{\mathrm{cal}}^{-1}o$ eigenvalues are, from $o=\tfrac{1}{1+r^{2n}}(-g_{\mathrm{cal}}+n\,d\bar r^2+n\,\bar\theta^2)$, equal to $\tfrac{n-1}{1+r^{2n}}$ (two directions) and $\tfrac{-1}{1+r^{2n}}$ ($2n-2$ directions). At the zero-section $r=0$ this is $O(1)$: the deviation does **not** decay.
- **Transition/damage zone** ($\rho\sim t^{-1/4}$, $g_t\approx t\,g_{\mathrm{euc}}$): here $|o|_{g_{\mathrm{cal}}}\sim\rho^{-2n}\sim t^{n/2}$, so $|E_t|_{\mathrm{op}}\sim|\lambda|\,t^{n/2}+O(t^{1/2})\to0$.

**Consequence.** The unweighted deviation is concentrated at the bubble core, with $\max_M|E_t|_{\mathrm{op}}\to (n-1)|\lambda|$. The pinching interval of $g_t$ converges to
$$\big[\,\Lambda-|\lambda|,\ \Lambda+(n-1)|\lambda|\,\big],\qquad \rho(g_t)\to\frac{\Lambda+(n-1)|\lambda|}{\Lambda-|\lambda|}=1+\frac{n|\lambda|}{\Lambda}+O\!\big((|\lambda|/\Lambda)^2\big).$$
This is the precise answer to the derivation requested: **the unweighted operator norm tends to $0$ if and only if $\lambda=0$.** The weighted MV norms hide this because they measure $\mathrm{Ric}-\Lambda g_t$ against the *unscaled* $g_{\mathrm{cal}}$ with decay weights, whereas the pinching test measures against the scale-$t$ core metric $g_t$, converting the harmless $t\lambda o$ into an $O(1)$ endomorphism.

## Mechanism 2: the obstruction and the pinching defect are the same quantity

By Proposition 3.5, $\displaystyle \lambda=\frac{1}{\|o\|_{L^2}}\frac{\omega_{2n-1}}{n}\Big(\tfrac{2-n}{2}\Lambda-\tfrac18\langle\mathcal R(\omega),\omega\rangle\Big)(p_0)$, evaluated from the *body* curvature at the singular point. This same $\lambda$ is (i) the coefficient whose non-vanishing gives MV Theorem 1.1 non-existence of Einstein metrics near $g_t$, and (ii) the coefficient controlling the bubble-core pinching defect in Mechanism 1. So there is a rigid dichotomy:

- $\lambda\ne0$ (nonzero body curvature at $p_0$, e.g. spherical/Kähler–Einstein bodies, MV Non-examples 1.3–1.4; robust for the Calabi $\Gamma_n\subset SU(n)$ core with $n\ge3$ since Lemma 1.1 removes the rotational freedom that could cancel it in the Eguchi–Hanson $n=2$ case): the metric is not desingularizable near $g_t$, but $\rho(g_t)$ is bounded away from $1$ by $\sim n|\lambda|/\Lambda$.
- $\lambda=0$: from Lemma 4.1 the core residual drops to $O(t^2\rho^2)$, giving $|E_t|_{\mathrm{op}}\lesssim t^{1/2}\to0$, i.e. $\rho(g_t)\to1$ — but $\lambda=0$ is exactly the wall where nearby Einstein metrics tend to exist (MV Theorem 1.2 in the AHE case; the Kummer/flat-body case MV Example 1.2 produces a genuine Calabi–Yau metric).

**Fatal point.** The first-order MV route cannot simultaneously deliver tight pinching and local non-existence: the two are proportional through one curvature functional. Any refutation must break this proportionality.

## Mechanism 3: the global gap, made concrete with $\chi,\tau$

Even granting a tightly pinched non-desingularizable $g_t$, refuting Yau 26 needs $M$ to carry **no** Einstein metric at all, whereas MV Theorem 1.1 / Ozuch (Integrability, Thm 0.9) give only "none near $g_t$" / "not a GH limit of Einstein metrics." These are strictly weaker. The gap is genuine:

- **Football.** $S^4/\mathbb Z_2$ (the involution $\mathrm{diag}(1,-1,-1,-1,-1)$, two $\mathbb R^4/\mathbb Z_2$ points) is $\Sigma\mathbb{RP}^3$; resolving both nodes by Eguchi–Hanson $T^*S^2$ gives, by inclusion–exclusion, $\chi=\chi(\Sigma\mathbb{RP}^3)-2+2\chi(T^*S^2)=2-2+4=4$, $\pi_1=1\ (\text{van Kampen, }\mathbb Z_2\to1)$. The resolved manifold is the double of the even ($e=-2$) disk bundle over $S^2$, i.e. $S^2\times S^2$: $\tau=0$, intersection form $H$, the exceptional $(-2)$-sphere is the primitive class $(1,-1)$. Hitchin–Thorpe $2\chi=8\ge3|\tau|=0$ is satisfied with room, and $S^2\times S^2$ **carries a product Einstein metric.** The non-desingularizable orbifold sits on a manifold that is Einstein far away.
- **Kummer.** $T^4/\mathbb Z_2$, sixteen $A_1$ points resolved, is K3: $\chi=24$, $\tau=-16$, HT **equality** $48=48$, and K3 is Calabi–Yau (Einstein). Here $\lambda=0$ everywhere (flat body) — again consistent with Mechanism 2.
- **Resolution trend.** Each $A_1$/Eguchi–Hanson resolution contributes $\Delta\chi=+1,\ \Delta\tau=\mp1$ (anti-self-dual orientation), so $\Delta(2\chi-3|\tau|)=-1$: aligned bubbles erode HT slack toward K3-type saturation. But keeping $\rho\to1$ demands $\lambda=0$ at each point (Mechanism 2), which forces the body curvature to vanish there — pushing the construction toward flat/Calabi–Yau data where HT saturates and Einstein metrics *exist*. HT is never pushed strictly across.

## Mechanism 4: tight positive pinching structurally suppresses every known global obstruction

This is the deepest barrier and worth isolating. For closed $(M^4,g)$,
$$2\chi\pm3\tau=\frac{1}{4\pi^2}\int_M\Big(2|W^\pm|^2+\tfrac{R^2}{24}-\tfrac12|\mathring{\mathrm{Ric}}|^2\Big)\,dv.$$
If $g^{-1}\mathrm{Ric}$ has eigenvalues in $[\Lambda-a,\Lambda+b]$ (fixed sign, $\Lambda>a$), then pointwise $|\mathring{\mathrm{Ric}}|^2\le(a+b)^2$ and $R\ge4(\Lambda-a)$, so
$$\tfrac{R^2}{24}-\tfrac12|\mathring{\mathrm{Ric}}|^2\ \ge\ \tfrac{2}{3}(\Lambda-a)^2-\tfrac12(a+b)^2\ \xrightarrow[a,b\ll\Lambda]{}\ \tfrac23\Lambda^2>0.$$
Hence **tightly, positively pinched 4-manifolds satisfy Hitchin–Thorpe strictly, with slack**: HT can never be the obstruction that forbids Einstein in the regime the resolution route needs. Moreover positive Ricci $\Rightarrow$ positive scalar $\Rightarrow$ no Seiberg–Witten basic classes, so the LeBrun-type SW obstructions (the only known way to forbid Einstein on HT-satisfying 4-manifolds) are also inactive. The $\Lambda<0$ analogue is no better: tight pinching there makes $g$ nearly Einstein of that sign, and existence/rigidity phenomena (Mostow-type for space forms, LeBrun SW estimates $c_1^2\le\ldots$ for the aspherical case) again align with, rather than against, existence. In dimension $\ge5$ the situation is even more adverse to refutation: there are essentially no topological obstructions to Einstein metrics, so a non-Einstein $M$ that is also tightly pinched is correspondingly harder to exhibit; and the Calabi core keeps $\lambda\ne0$ rigid (Lemma 1.1), so Mechanism 2 persists in every even dimension.

**Net structural reading.** The topological facts that could forbid Einstein metrics are precisely the ones suppressed by tight same-sign Ricci pinching. This is real evidence — not proof — that Yau 26 is *true* for tight positive windows, and that any counterexample must come from a mechanism outside orbifold resolution.

## Where the route could still be pushed, and the exact theorem shape needed

**Repair R1 (decouple pinching from non-existence via higher-order obstructions).** Arrange the *first* obstruction $\lambda=0$ (tight pinching, Mechanism 1/2) but a *higher* obstruction non-vanishing. In MV's completion the residual solvability constant behaves like $\lambda(t,u)=tu+O(t^{3/2-\delta})$; after the optimal $k_1$-correction the leading core residual is $\sim t^{a}o$ with $a>1$, so $|E_t|_{\mathrm{op}}\sim t^{a-1}\to0$ while local non-existence is retained. This yields tightly pinched, non-locally-desingularizable metrics. The concrete question is whether compact orbifolds with $\lambda=0$ but a genuine higher obstruction exist and what their resolutions are — the source to mine is Ozuch, *Higher order obstructions to the desingularization of Einstein metrics* (arXiv:2012.13316) and the higher-obstruction quantities of the Integrability paper (Remark 0.7, Question 0.8). Even a full success here leaves the global gap open.

**Repair R2 (supply the missing global theorem).** What is needed is a diffeomorphism invariant $I(M^n)$ such that (a) $I(M)\ne0$ forbids *all* Einstein metrics on $M$, and (b) $I(M)\ne0$ is *compatible* with a same-sign Ricci window of ratio arbitrarily near $1$. Mechanism 4 shows $I=$ HT or $I=$ SW fail (b). A candidate direction is an integral obstruction insensitive to scalar-curvature sign — e.g. Ozuch's Taub-type preserved quantities $\mathcal T^\Sigma_X(h,h)$ and the reduced-volume identity (Integrability paper, Thm 0.4/Remark 0.5): $\Lambda\,\mathcal V(\mathbf g_b)+Q(W^+_{\mathbf g_b},W^-_{\mathbf g_o})+Q(W^-_{\mathbf g_b},W^+_{\mathbf g_o})=0$. Note this obstruction is again driven by the body Weyl curvature $W_{\mathbf g_o}$ at the singular point, i.e. by the same data as $\lambda$ — so it too must be tested against Mechanism 2 before it can serve as a genuinely *global*, pinching-compatible obstruction. Whether any such invariant survives tight pinching is the decisive unknown; a proof that none can (a quantitative "tight pinching $\Rightarrow$ approximate HT and vanishing SW $\Rightarrow$ Einstein-admissibility") would essentially settle the positive case of Yau 26 affirmatively.

**Exact fatal points to keep in front.** (1) $\lambda\ne0$ ruins unweighted pinching at the bubble core at $O(1)$; $\lambda=0$ tends to restore genuine Einstein existence — one functional controls both. (2) Local/GH non-existence is not manifold-level non-existence; the football resolution is $S^2\times S^2$-type and Einstein. (3) HT and SW, the only global tools in dimension $4$, are quantitatively incompatible with tight same-sign pinching. Any repair must break at least one of these three simultaneously, and (2)+(3) are the ones with no current instrument.