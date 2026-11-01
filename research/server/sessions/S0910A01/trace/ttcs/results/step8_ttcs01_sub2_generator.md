# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Using the Step 8 measure-local theorem and the Naber-Zhang collapsed regularity framework, propose the strongest mathematically precise next route for extending the Derdziński contradiction through local unwrapping of collapsed neighborhoods. Focus on what hypotheses would let small mean LeBrun deficits transfer to noncollapsed local covers with bounded multiplicity or controlled measure distortion, how maximal nilpotency-rank assumptions enter, and what collapse mechanisms remain outside such a route. Do not claim a full collapse classification; give testable lemmas or reductions that could materially advance Yau 26.

## Output

## Reframing the transfer problem: which deficits are pointwise and which are only integral

The whole unwrapping question changes character once the three parts of the Step 8 density $F_i$ are separated by how strongly they are small.

**Covering transfer identity.** Let $\pi:(\tilde B_2(\tilde p),\tilde p)\to (B_2(p),p)$ be a normal Riemannian covering with deck group $G$ acting freely by isometries; $\pi$ is a local isometry. For any $F\ge 0$ on the base with lift $\tilde F=F\circ\pi$,
$$
\int_{\tilde B_r(\tilde p)}\tilde F\,d\tilde\mu=\int_{B_r(p)}F(x)\,N_r(x)\,d\mu(x),
\qquad N_r(x)=\#\{g\in G: d(g\tilde x_0,\tilde p)<r\},
$$
and $\operatorname{Vol}\tilde B_r(\tilde p)=\int_{B_r(p)}N_r\,d\mu$. Hence the cover mean is an $N_r$-weighted base mean:
$$
\frac{1}{\operatorname{Vol}\tilde B_{r}(\tilde p)}\int_{\tilde B_{r}}\tilde F\;\le\;
\Big(\tfrac{\sup_{B_r}N_r}{\inf_{B_r}N_r}\Big)\cdot
\frac{1}{\operatorname{Vol}B_{r}(p)}\int_{B_{r}}F .
\tag{$\star$}
$$
So transfer of a *mean-small* nonnegative density is controlled entirely by the multiplicity oscillation $\sup N_r/\inf N_r$.

**The deficit dichotomy.** In the near-extremal LeBrun sequence the first part is pointwise controlled:
$$
\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty}=\delta_i\to 0
\;\Longrightarrow\;
\|\operatorname{Ric}_{\tilde g_i}+\tilde g_i\|_{L^\infty}=\delta_i\to0
\ \text{on every cover.}
$$
Therefore any noncollapsed smooth limit of the covers is Einstein with $\operatorname{Ric}=-g_\infty$, hence $s_\infty=-4$, *for free* — no measure transfer is used. The Weyl balance
$$
\int_{M_i}(s_i+8\sqrt6\,|W_i^+|)^2\,d\mu_i=o(A_i),\qquad
\int_{M_i}\xi_i(Q_i+P_i)\,d\mu_i\le 24\pi^2 D_i=o(A_i)
$$
is only an integral (mean) statement. These two are exactly the densities whose passage to a cover chart requires ($\star$). This is the precise content that must be moved: **the Seiberg–Witten scalar–Weyl balance, not the Einstein condition.**

Consequently the Derdziński contradiction on a cover reduces to one analytic input — bounded multiplicity oscillation on the base ball where the balance density lives.

## The multiplicity oscillation lemma and where maximal rank enters

Maximal nilpotency rank enters twice: once to make the cover noncollapsed (Naber–Zhang Prop. 5.9), and once, more subtly, to control $N_r$ in ($\star$).

**Lemma M (multiplicity oscillation from transitivity).** *Let $\operatorname{Ric}_{g_i}\ge-(n-1)$, $d_{GH}(B_2(p_i),B_2(0^{k-\ell},z^\ell))\to0$ with $\ell\le 3$, and $\operatorname{rank}\Gamma_{\delta_i}(p_i)=n-k$ (maximal). Then there are $r_0(n),C(n)>0$ with*
$$
\frac{\sup_{B_{r_0}(p_i)}N_{r_0}}{\inf_{B_{r_0}(p_i)}N_{r_0}}\le C(n)+o(1).
$$

*Mechanism.* By NZ Prop. 5.4/5.7 the maximal-rank hypothesis forces the equivariant limit $(\tilde B_i,G_i,\tilde p_i)\to(\mathbb R^{n-\ell}\times C(\hat Z),G_\infty,\tilde p_\infty)$ in which $G_\infty$ acts **transitively** on each fiber of the limiting submetry over the Euclidean factor. Transitivity gives, for any limit points $\tilde x_\infty,\tilde y_\infty$ in one fiber, an isometry $g_\infty$ with $g_\infty\tilde x_\infty=\tilde y_\infty$; at finite $i$ this is approximate to error $o(1)$ (the graded short generators of NZ Lemma 4.24 move base points by $\le K\delta_i r_0$). Composing the deck displacement-counting set for $x$ with such $g$ maps it into that for $y$ up to $o(1)$ dilation of scale, and the counting function $N_R$ is doubling in $R$ (polynomial growth of the almost-nilpotent $G$). Together these give the two-sided bound. The transitivity that produces uniform disintegration of $\tilde\mu$ over the base is *precisely* the maximal-rank output; sub-maximal rank yields an $\mathbb R$-factor deficit on the cover and no uniform fiber measure.

**Lemma T (deficit transfer).** Combining Lemma M with ($\star$) and the averaging estimate of Step 8 §2 (volume-random balls carry small local mean of $F_i$),
$$
\frac{1}{\operatorname{Vol}\tilde B_{r_0}(\tilde p_i)}\int_{\tilde B_{r_0}}\big(s_i+8\sqrt6|W_i^+|\big)^2\circ\pi\;\longrightarrow\;0 .
$$
Passing through the finite-$W^{2,p}$ argument of Step 8 §4 on the noncollapsed cover (harmonic radius $\ge h_0$ by NZ Prop. 6.4), the smooth Einstein cover limit satisfies
$$
\operatorname{Ric}=-g_\infty,\quad s_\infty=-4,\quad s_\infty+8\sqrt6|W_\infty^+|=0
\ \Rightarrow\ |W_\infty^+|^2=\tfrac1{24}.
$$

**Lemma D (local Derdziński on the cover, robust to non-Euclidean limits).** The cover limit need not be $\mathbb R^4$. On any open set of a smooth complete Einstein four-manifold with $\operatorname{Ric}=-g_\infty$ and $|W_\infty^+|^2=1/24$: $\delta W^+_\infty=0$ and $\#\operatorname{spec}W^+_\infty\le2$ (from the calibrated spectrum $(\tfrac1{12},\tfrac1{12},-\tfrac16)$), so Derdziński Prop. 5 applies, the factor $(24|W^+_\infty|^2)^{1/3}$ is constant, $g_\infty$ is locally Kähler, whence a Kähler–Einstein metric with $\operatorname{Ric}=-g$ has $|W^+|^2=2/3\ne1/24$. Since $|W^+_\infty|^2=1/24\ne0$ everywhere, $W^+_\infty\ne0$ everywhere and the contradiction is global on the cover chart. This robustness matters: unwrapping a collapsed ball need not produce Euclidean space; a complete Einstein ALE-type limit is equally destroyed.

The chain is therefore closed under a **single hypothesis**: maximal rank on a definite volume proportion. Everything else (noncollapse, harmonic radius, deficit transfer, contradiction) follows.

## Reduction to the regular collapsed stratum

The volume-proportion theorem states $\operatorname{Vol}E_i(v)/\operatorname{Vol}M_i\to0$ for every $v$, so the measured Ricci-limit $(X,d,\nu)$ carries no mass on the four-regular part; its Colding–Naber dimension is $m\le 3$. At $\nu$-a.e. point $X$ is $m$-regular with tangent $\mathbb R^m$, and by quantitative differentiation there is a definite scale $r$ at which base balls are GH-close to $\mathbb R^m$ (so $k=m,\ \ell=0$, and $\ell\le3$ automatically). The intersection of "small local mean" (full measure, Step 8 §2) with "$m$-regular" (full measure) is full measure.

**Reduction A.** *If $\operatorname{rank}\Gamma_{\delta_i}=n-m$ (maximal) on a set of definite volume proportion of $m$-regular collapsed points, then Lemmas M, T, D give a contradiction; hence a near-extremal LeBrun sequence must concentrate its rank-deficiency on a set of full volume proportion.* This turns the collapse problem from classification into a localized statement about the rank-deficient stratum.

## The Seiberg–Witten budget as a curvature-concentration control

There is a second, independent line that constrains where rank can drop.

Because $s_i\approx-4$ is bounded while $|W_i^+|$ is not,
$$
(s_i+8\sqrt6|W_i^+|)^2=384\big(|W_i^+|-\tfrac1{2\sqrt6}\big)^2+\text{(bounded remainder)},
$$
so $\int(s_i+8\sqrt6|W_i^+|)^2=o(A_i)$ forces $|W_i^+|$ to sit at $1/(2\sqrt6)$ in $L^2$-mean and forbids concentration: any curvature-concentration core carrying self-dual Weyl energy $\ge c_0$ contributes $\ge 384\,c_0'$ to this integral, so the number of unit-energy cores is $o(A_i)$.

**Reduction C (energy budget vs. topology).** The self-dual Weyl energy is spread ($\int|W^+_i|^2\approx\tfrac1{24}\operatorname{Vol}\sim A_i$, distributed), while the topology satisfies $2\chi+3\tau=A_i-k_i\approx\tfrac23A_i$ and $\chi=\chi(X_i)+k_i$. Test whether the Gauss–Bonnet/signature identities for Einstein four-manifolds,
$$
\chi=\tfrac1{8\pi^2}\!\int\!\big(|W^+|^2+|W^-|^2+\tfrac1{24}s^2\big),\qquad
\tau=\tfrac1{12\pi^2}\!\int\!\big(|W^+|^2-|W^-|^2\big),
$$
are realizable with $\int(s+8\sqrt6|W^+|)^2=o(A_i)$ *and* with all curvature concentration confined to an $o(A_i)$-deficit, $o(\operatorname{Vol})$-measure set. A quantitative incompatibility here would remove bubbling directly and leave only Reduction A. The concrete inequality to check: is the required $|W^-|$ distribution (fixed by $\chi,\tau$ once $\int|W^+|^2$ is pinned near $A_i/24$) compatible with $\overset{\circ}{\operatorname{Ric}}\approx0$ and mean-balanced $|W^+|$, or does it force a definite deviation set that the $o(A_i)$ budget cannot pay for?

## Collapse mechanisms that stay outside this route

These are the honest residual regimes; each comes with a testable sub-lemma.

1. **Sub-maximal rank without Weyl concentration.** Collapse with bounded curvature where the fibered fundamental group has rank $<n-m$ — the NZ Example 6.1 model ($N_k^3\to\mathbb R^1_+$, rank drops to $1$ near a fixed-type stratum) and the Anderson codimension-one model (Example 3.1, rank $0$). Here the cover does not become noncollapsed and Lemma M has no transitive fiber. This is the sharp residual: the SW budget (Reduction C) does *not* touch it because no Weyl energy concentrates. Target sub-lemma: bound the volume proportion of the rank-deficient collapsed stratum, or show that on it the LeBrun scalar–Weyl balance still forces a lower-dimensional Einstein–Weyl structure that is itself contradictory.

2. **Residual four-dimensional cover behavior.** Only if a once-unwrapped cover collapses again could an Eguchi–Hanson-type residual factor appear (NZ Rem. 1.3 sharpness at $\dim Z=4$). Maximal rank on the base excludes re-collapse of the cover; the test is whether one unwrapping always reaches noncollapse in the pure four-dimensional problem (it does under maximal rank, since $\ell\le3<4$ on the base is automatic once the four-regular part has vanishing proportion).

3. **Singular fibers / fixed strata.** The K3 model's Kodaira $I_1$ fibers (rank $1$ instead of $2$) show that fibered rank can drop on a lower-dimensional set carrying curvature and Euler contribution. Here Reduction C is the relevant control: quantify the $\chi$-density concentrated on such strata and match it against the SW budget.

4. **Multiplicity concentration.** If the fiber is an inhomogeneous almost-nilmanifold whose orbit counting $N_r$ is non-uniform, ($\star$) leaks. Lemma M asserts this cannot happen under maximal rank (transitivity ⟹ uniform disintegration); the residual is exactly the coincidence of non-uniform fiber with rank drop.

## Testable lemmas and decisive computations

- **Confirm the deficit dichotomy (cheap, decisive).** Verify on explicit near-extremal LeBrun data that $(s+8\sqrt6|W^+|)^2$ is *not* pointwise $L^\infty$-small (only mean-small). If it were secretly pointwise-small, multiplicity would be unnecessary and the route simplifies drastically; if not (expected, since $|W^+|$ is Ricci-uncontrolled), Lemma M is indispensable.

- **Lemma M on model collapses (numerical/analytic).** Compute $N_r(x)$ oscillation for flat torus-bundle and Heisenberg-nilmanifold collapse (maximal rank) versus the $N_k^3$ fixed-stratum model (rank drop). Confirm bounded oscillation exactly in the maximal-rank case; this isolates the transitivity mechanism.

- **Bubble limits also carry the contradiction.** Check whether known complete $\lambda\le0$ Einstein/Ricci-flat ALE four-manifolds (Eguchi–Hanson: hyperkähler, $W^+=0$, $|W^+|^2=0$; and $\lambda<0$ analogues) ever attain $|W^+|^2=1/24$. If none do, then even the concentration cores yield a Derdziński contradiction at their natural scale, upgrading Reduction C.

- **Reduction C inequality.** With $\operatorname{Vol}\sim\tfrac{32\pi^2}{9}A_i$, $\int|W^+|^2\sim\tfrac{4\pi^2}{27}A_i$, $2\chi+3\tau\approx\tfrac23A_i$, solve for the forced $\int|W^-|^2$ and its minimal concentration; test whether an $o(A_i)$-deficit set can host it.

- **Lemma D normalization recheck.** Confirm the eigenvalue arithmetic: calibrated LeBrun spectrum $(\tfrac1{12},\tfrac1{12},-\tfrac16)$ gives $|W^+|^2=1/24$; Kähler–Einstein $\operatorname{Ric}=-g$ gives spectrum $(\tfrac13,\tfrac13,-\tfrac23)$, $|W^+|^2=2/3$. The $2/3\ne1/24$ separation is the entire contradiction and should be locked as a standalone verified identity.

The strongest single next target is Reduction A together with Lemma M: *establish maximal fibered rank on a definite volume proportion of the $m$-regular collapsed stratum, with bounded multiplicity oscillation*. Under that one input the Einstein structure transfers for free, the Seiberg–Witten balance transfers through ($\star$), and Derdziński closes the contradiction on the cover — reducing the minus-branch LeBrun sub-problem to controlling the rank-deficient collapsed stratum, which Reduction C constrains through the Weyl-energy budget.