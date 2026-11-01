# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Independently analyze the proposed exponential-pullback chart averaging lemma in dimension four. Let (M,g) be closed with |sec_g|<=K on a buffered region U, fix 0<r<min(buffer, pi/(2 sqrt K)) so exp_p^*g is nonsingular on B_r(0) subset T_pM for every p in a positive-volume set P whose r-geodesics remain in U. For nonnegative measurable F supported in U, determine whether one can prove

∫_P [Vol_{exp_p^*g}(B_r(0))^{-1} ∫_{B_r(0)} F(exp_p v) dμ_{exp_p^*g}(v)] dμ_g(p) <= C(n,K,r) ∫_U F dμ_g,

with no injectivity-radius or sheet-number assumption. Give a rigorous derivation or counterexample. Track polar-coordinate Jacobians, the v=0 singularity, conjugate-radius assumptions, Liouville/geodesic-flow invariance, and normalization of pullback-ball volume. Also explain what curvature-derivative bounds are needed for smooth compactness of these exponential charts. This is for a collapsed near-Einstein four-manifold route; do not assume CFG or local covers.

## Output

## Verifier memo — exponential-pullback chart averaging lemma in dimension four

**Bottom line.** The inequality is **true**, in every dimension including $n=4$, with an explicit constant
$$
C(n,K,r)=\frac{\omega_{-K}(r)}{\omega_{K}(r)},
$$
the ratio of the volumes of an $r$-ball in the constant-curvature model of curvature $-K$ (Bishop upper model) and of curvature $+K$ (Günther lower model). No injectivity-radius and no sheet-number hypothesis on $M$ enters. On flat collapse ($K=0$) the constant is $1$ and is attained, so the estimate is sharp there. The reason the estimate survives arbitrary collapse is a genuine cancellation: the same geodesic multiplicity that could blow up the numerator is exactly the multiplicity that inflates the normalizing pullback-ball volume, and the two cancel after a geodesic-reversal symmetry.

Below is the derivation with each tracked object addressed, then the compactness input, then how this sits in the collapsed near-Einstein route.

---

### 1. Immersion and the pullback ball as a genuine normal ball

With $|\sec_g|\le K$ on the buffered region and $r<\pi/(2\sqrt K)$, Rauch comparison gives first conjugate point at distance $\ge\pi/\sqrt K>r$ along every geodesic. Hence $\exp_p|_{B_r(0)}$ is a nonsingular immersion and $\exp_p^*g$ is a bona fide metric (matching the hypothesis).

$\exp_p:(B_r(0),\exp_p^*g)\to(M,g)$ is by construction a **local isometry**: radial lines $t\mapsto tv$ push forward to unit-scaled geodesics, so they are geodesics of the pullback metric and $\exp_0^{\exp_p^*g}=\mathrm{id}_{B_r(0)}$. Being the identity, this pullback exponential is injective on $B_r(0)$; combined with the absence of conjugate points this makes $B_r(0)$ a **normal geodesic ball of radius $r$ whose center has injectivity radius $\ge r$** in the pullback metric. This is the key structural point: the domain ball is "unwrapped," and its center is noncollapsed *regardless of how collapsed $M$ is at $p$*.

**The $v=0$ singularity is not present.** The worry about the polar Jacobian $\theta(t,\xi)\sim t^{n-1}$ vanishing at the origin is a coordinate artifact of geodesic polar coordinates. The argument never uses polar coordinates; it uses the intrinsic volume form $d\mu_{\exp_p^*g}=\exp_p^*d\mu_g$, which is smooth and nondegenerate at $v=0$ because $d\exp_p|_0=\mathrm{id}$. Where polar coordinates would enter, Günther/Bishop are precisely the two-sided bounds on the radial density $\theta(t,\xi)/t^{n-1}$ between the $(\mathrm{sn}_K t/t)^{n-1}$ and $(\mathrm{sn}_{-K}t/t)^{n-1}$ profiles, all integrable across $t=0$.

### 2. Comparison bound on the pullback-ball volume (both sides)

Set $V(p)=\mathrm{Vol}_{\exp_p^*g}(B_r(0))$. Since $(B_r(0),\exp_p^*g)$ has $|\sec|\le K$ (local isometry preserves curvature) and is a normal ball of radius $r<$ conjugate radius with center injectivity radius $\ge r$:

- Günther (upper sectional bound $K$, valid for $r<\pi/\sqrt K$): $\;V(p)\ge \omega_K(r)>0$;
- Bishop absolute upper bound (from $\mathrm{Ric}\ge-(n-1)K$, ball inside cut locus): $\;V(p)\le \omega_{-K}(r)<\infty$.

Both depend only on $n,K,r$. **This is the mechanism that defeats collapse:** $V(p)$ counts geodesic multiplicity (in the flat collapsing torus $\exp_p$ wraps $\sim r/\varepsilon$ times), yet $V(p)$ stays pinned between $\omega_K(r)$ and $\omega_{-K}(r)$ because the *unwrapped* domain ball is honestly a bounded-curvature ball of radius $r$ with a definite center injectivity radius.

The comparison bounds require $|\sec|\le K$ along the $r$-geodesics emanating from the center. For $p\in P$ this is the stated hypothesis; for the second use below (centers $y\in\mathrm{supp}\,F\subset U$) it is guaranteed by the buffer, which is exactly why $r<\text{buffer}$ is imposed. The volume *identity* $V(y)=\int_M N_r(y,q)\,d\mu_g(q)$ is unconditional; only the numerical bound $V(y)\le\omega_{-K}(r)$ needs the buffer.

### 3. Area formula, multiplicity, and reduction to a kernel bound

Because $\exp_p$ is a local diffeomorphism with unit Jacobian relative to $(\exp_p^*g,g)$, the area formula gives, for measurable $F\ge0$,
$$
\int_{B_r(0)}F(\exp_p v)\,d\mu_{\exp_p^*g}(v)=\int_M F(y)\,N_r(p,y)\,d\mu_g(y),\qquad
N_r(p,y):=\#\{v\in B_r(0):\exp_p v=y\},
$$
the number of geodesics from $p$ to $y$ of length $<r$ (finite for all $y$: $\overline{B_r(0)}$ compact, $\exp_p$ an immersion, so preimages are isolated). Taking $F\equiv1$ recovers $V(p)=\int_M N_r(p,y)\,d\mu_g(y)$, confirming that the normalizer itself is the multiplicity-weighted mass — **not** the image volume $\mathrm{Vol}_g(B_r(p))$.

Insert into the target integral and apply Tonelli ($F\ge0$, $M$ compact):
$$
I=\int_P\frac{1}{V(p)}\int_M F(y)N_r(p,y)\,d\mu_g(y)\,d\mu_g(p)
=\int_M F(y)\,W(y)\,d\mu_g(y),\qquad
W(y):=\int_P\frac{N_r(p,y)}{V(p)}\,d\mu_g(p).
$$

### 4. Geodesic-reversal (Liouville) symmetry closes the bound

Bound $V(p)\ge\omega_K(r)$ and enlarge $P$ to $M$:
$$
W(y)\le \frac{1}{\omega_K(r)}\int_M N_r(p,y)\,d\mu_g(p).
$$
Reversal is an involution: a geodesic $\gamma$ from $p$ to $y$ with $\gamma'(0)=v\in B_r(0)$ maps bijectively to the geodesic $s\mapsto\gamma(1-s)$ from $y$ to $p$ with initial vector $-\gamma'(1)$ of equal length. Hence $N_r(p,y)=N_r(y,p)$. Equivalently, the map $(p,v)\mapsto(\exp_p v,-\dot\gamma(1))$ preserves the Liouville measure $d\mu_g(p)\wedge d\mathcal L_{T_pM}(v)$ on $\{|v|<r\}$, which is what makes the double fibration symmetric. Therefore
$$
\int_M N_r(p,y)\,d\mu_g(p)=\int_M N_r(y,p)\,d\mu_g(p)=V(y)\le\omega_{-K}(r),
$$
so $W(y)\le \omega_{-K}(r)/\omega_K(r)=C(n,K,r)$ for a.e. $y\in U$, and
$$
I\le C(n,K,r)\int_M F\,d\mu_g=C(n,K,r)\int_U F\,d\mu_g,
$$
using $\mathrm{supp}\,F\subset U$. $\qquad\blacksquare$

### 5. Why the normalization choice is not optional

The estimate is true **because** the normalizer is the pullback-ball volume $V(p)$. If one instead normalized by the image-ball volume $\mathrm{Vol}_g(B_r(p))$, the estimate is **false** under collapse. Flat torus $T^2=\mathbb R^2/(\mathbb Z\times\varepsilon\mathbb Z)$, $K=0$, fixed $r$: image volume $\sim 2r\varepsilon$, pullback integral $\sim \pi r^2\bar F$, so the inner quantity $\sim \pi r\bar F/(2\varepsilon)\to\infty$, and $\int_P(\cdots)\sim \pi r\bar F/2$ while $\int_U F\sim \varepsilon\bar F\to0$ — the ratio diverges. With the correct pullback normalization the same example gives $W\equiv1$, $C=1$, and equality up to the equidistribution error. This flat check both confirms sharpness at $K=0$ and isolates the exact reason a naïvely similar statement would break.

### 6. Curvature-derivative input for smooth compactness of the charts

The averaging estimate itself needs only the $C^0$ curvature bound $|\sec|\le K$. Smooth compactness of the family $\{(B_{r'}(0),\exp_p^*g)\}$ ($r'<r$) needs more, and here is the clean accounting for the near-Einstein setting:

- **Two-sided $C^0$ metric control** is automatic from $|\sec|\le K$: Jacobi-field comparison pinches $\exp_p^*g$ between the $\mathrm{sn}_{K}$ and $\mathrm{sn}_{-K}$ model metrics on $B_{r'}(0)$.
- **Center noncollapsing** is automatic: injectivity radius at $0$ is $\ge r$ (Section 1), *without any assumption on $M$*. This is the property collapse would otherwise destroy.
- **$C^{1,\alpha}\cap W^{2,p}$ precompactness** then follows from a bounded Ricci tensor via a definite harmonic radius (Anderson/Jost–Karcher): in harmonic coordinates $g^{ab}\partial_a\partial_b g_{ij}=-2\mathrm{Ric}_{ij}+Q(g,\partial g)$, and a lower harmonic-radius bound follows from $\|\mathrm{Ric}\|_\infty\le\Lambda$ together with the $C^0$ metric pinch and center injectivity radius $\ge r$. In the route $\mathrm{Ric}_g=-g+O(\delta)$ is uniformly bounded, so this holds with $\Lambda\approx n$.
- **$C^{k,\alpha}$ / smooth precompactness** in general requires $|\nabla^j\mathrm{Rm}|\le K_j$ for $0\le j\le k-1$ (Cheeger–Gromov–Anderson): each derivative bound upgrades the normal-coordinate expansion $g_{ij}=\delta_{ij}-\tfrac13R_{ikjl}v^kv^l+\cdots$ one order. If only the $C^0$ curvature bound and bounded Ricci are available, one does **not** get $C^{2,\alpha}$ control of the approximants — consistent with the statement in `step6_...tex` that only $W^{2,p}_{\mathrm{loc}}$/$C^{1,\beta}_{\mathrm{loc}}$ convergence of the $g_i$ is asserted.
- **Smoothness of the limit** is nonetheless obtained by bootstrap: the harmonic-coordinate limit satisfies $\mathrm{Ric}_\infty=-g_\infty$ weakly, and Einstein metrics in harmonic coordinates are analytic; elliptic regularity promotes $g_\infty$ to $C^\infty$. This is exactly the bootstrap used in `step6` Section "Regular-patch transfer," and it does not need $C^{2,\alpha}$ bounds on the sequence.

So: the averaging lemma needs $|\sec|\le K$ only; extracting a limit chart needs, in addition, a Ricci bound (present) plus the automatic center injectivity radius; extracting a *smooth* limit uses the Einstein bootstrap, while $C^\infty$ control of the *approximants* would need $|\nabla^j\mathrm{Rm}|$ bounds that are not assumed and not required for the limit.

### 7. What this delivers for the collapsed route, and what it does not

Applied with $F=|\mathrm{Ric}_g+g|^2$ (or any nonnegative LeBrun/Weyl integrand density), the lemma transports the global $L^2$ defect $\int_U|E|^2$ to the unwrapped chart family with total mass controlled by $C(n,K,r)\int_U|E|^2$. Combined with $\mu_g(P)>0$ and Chebyshev,
$$
\frac{1}{\mu_g(P)}\int_P\Big[\text{chart-average of }F\Big]\,d\mu_g(p)\le \frac{C(n,K,r)}{\mu_g(P)}\int_U F,
$$
so a definite fraction of centers $p\in P$ yield unwrapped charts on which the pulled-back defect average is $\le \frac{2C}{\mu_g(P)}\int_U F$. This is precisely the "controlled unwrapping preserving small pulled-back deficit" that `step6` flags as the next needed piece, and it is achieved here **without CFG and without local covers** — the noncollapsing is supplied intrinsically by the center-injectivity-radius-$\ge r$ property of the pullback ball. This directly serves Demand B / the collapsed branch of `step15` (transport of $\int_M|E|^2$-type densities).

Two things the lemma does **not** by itself supply, which the route still owes:

1. **Norm strength.** The estimate controls $L^1$ of the transported density. To force the chart limit into the calibrated Einstein/Weyl model one needs the pulled-back defect small in a norm strong enough for the equations used in `step6` (7)–(9). Applying the lemma with $F=|E|^2$ transports the $L^2$ defect, which is the natural input; whether that plus bounded Ricci yields the required $C^0$ or spectral convergence of $|W^+|$ on the selected chart is a separate elliptic/monopole passage, not a consequence of the averaging estimate.
2. **Which center is good.** The lemma gives many good centers on average but does not by itself pin the *geometry* of the selected chart (e.g. that its harmonic radius stays bounded below along the sequence, or that the pulled-back monopole form stays nonzero). The center-injectivity-$\ge r$ property gives the harmonic radius lower bound; the nonvanishing harmonic self-dual form still relies on the unique-continuation input recorded in `step15` §6, which the averaging estimate does not address.

### 8. Consistency notes on the surrounding session material

- The `step15` L² chain constant $7/24$ and Theorem 1 are logically independent of this lemma; the lemma is a transport tool, not a source of the calibration. No conflict.
- The `step6` sentence "the next valuable question is whether typical collapsed balls can be locally unwrapped to noncollapsed harmonic charts while preserving small pulled-back LeBrun deficit" is answered affirmatively at the averaging level by this lemma, with the explicit constant $\omega_{-K}(r)/\omega_K(r)$ and no reliance on maximal-rank collapse models. This is a concrete strengthening of that note's open question.
- The `step6` caution that varying topology ($A_i\to\infty$) only affords $o(A_i)$ errors is orthogonal: the present lemma is metric-analytic and holds for fixed $K,r$ regardless of $A$; it does not resolve the varying-topology transport of the defect, only the fixed-curvature-scale chart averaging.

**Unresolved item requiring explicit input.** The single quantitative point that must be checked before using $C(n,K,r)$ downstream is the buffer arithmetic: the second-use bound $V(y)\le\omega_{-K}(r)$ needs $|\sec|\le K$ along all $r$-geodesics from every $y\in\mathrm{supp}\,F$, i.e. the buffer must contain an $r$-neighborhood of $\mathrm{supp}\,F$, not merely of $P$. If $\mathrm{supp}\,F$ reaches within $r$ of the region where the curvature bound lapses, $W(y)$ for those $y$ is uncontrolled and the constant degrades. Stating the hypothesis as "$|\sec|\le K$ on the $r$-neighborhood of $\mathrm{supp}\,F\cup P$" removes this gap cleanly.