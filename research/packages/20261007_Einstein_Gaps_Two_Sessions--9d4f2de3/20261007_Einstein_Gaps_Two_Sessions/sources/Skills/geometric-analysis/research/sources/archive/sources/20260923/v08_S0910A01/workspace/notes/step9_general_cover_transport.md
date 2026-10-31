# Step 9: general normal-cover mean lemma (core valid; later exclusion theorem refined)

**Step 10 refinement.** The core mean-transport lemma in §1 is valid, but later use of it is refined in `workspace/notes/step10_accessible_cover_reassessment.md`. The buffer condition should be read as a precompact interior condition such as `closure(B_{3r}^{\widehat U}(\hat p))` compactly contained in the covering domain, or as a cover over a larger base ball while using only an interior core. The measurable section should be obtained by an abstract Borel selection/enumeration of the countable deck group, not by assuming smooth equidistant tie hypersurfaces. Numerical hyperbolic volume constants in Remark 2 are not used. The §3 cover-noncollapsed exclusion theorem is a useful template but is superseded by the Step 10 measurable fixed-scale accessible-cover theorem, which explicitly supplies harmonic-radius control via Naber--Zhang or an equivalent hypothesis.

---

Session: S0910A01. Phase: Execute.

## Purpose

This note proves a general normal-cover transport lemma that removes the need for model-specific lattice-counting, nilpotent coordinates, or structural hypotheses on the deck group. The proof uses only the normal covering structure, the free deck action, and Bishop–Gromov comparison. The sheet count cancels entirely from the final estimate.

This replaces the model-specific approach in `step8_model_deck_transport.md` (flat torus §2, principal circle §3, nilpotent §4) and removes "deck-counting estimate" as a separate hypothesis from the conditional lemma (§5 of that note). The model proofs become corollaries.

## 1. General normal-cover transport lemma

**Lemma (Normal-Cover Transport).** Let $(M^n,g)$ be a Riemannian manifold with $\operatorname{Ric}\ge-(n-1)Kg$ for some $K\ge0$. Let $p\in M$, $r>0$, and let $\pi:(\widehat U,\hat g)\to(U,g|_U)$ be a normal Riemannian covering with deck group $\Gamma$, where $U\supset B_r(p)$ is open. Fix $\hat p\in\pi^{-1}(p)$ and assume

$$
B_{3r}(\hat p)\subset\widehat U
\tag{Buffer}
$$

(the buffer domain condition). Then for every nonnegative measurable $\varphi$ on $B_r(p)$,

$$
\fint_{B_r(\hat p)}\pi^*\varphi\,d\hat\mu
\;\le\;
\frac{V_K(3r)}{V_K(r)}\cdot
\fint_{B_r(p)}\varphi\,d\mu,
\tag{$\star$}
$$

where $V_K(r)$ is the volume of a ball of radius $r$ in the $n$-dimensional space form of constant sectional curvature $-K$.

The constant $C(n,K,r):=V_K(3r)/V_K(r)$ depends only on dimension, Ricci lower bound, and radius. It is independent of the sheet count, collapse rate, deck group structure, nilpotency rank, and fiber model.

**Proof.** The argument has four steps.

*Step 1 (Geodesic lifting).* For any $x\in B_r(p)$, let $\sigma:[0,L]\to M$ be a unit-speed minimizing geodesic from $p$ to $x$, with $L=d(p,x)<r$. Since $d(p,\sigma(t))\le t<r$ for all $t\in[0,L]$, the geodesic $\sigma$ lies entirely in $B_r(p)\subset U$. Its unique lift $\hat\sigma$ starting at $\hat p$ has the same length $L<r$, so $\hat\sigma(L)\in B_r(\hat p)$ is a lift of $x$. In particular, every point of $B_r(p)$ has at least one lift in $B_r(\hat p)$.

*Step 2 (Multiplicity bound).* Let $N(2r):=\#\{\gamma\in\Gamma:d(\hat p,\gamma\hat p)<2r\}$. For a fixed $x\in B_r(p)$, choose any reference lift $\hat x_1\in\pi^{-1}(x)\cap B_r(\hat p)$. Every other lift $\hat x=\gamma\hat x_1$ in $B_r(\hat p)$ satisfies

$$
d(\hat p,\gamma\hat p)
\le d(\hat p,\gamma\hat x_1)+d(\gamma\hat x_1,\gamma\hat p)
= d(\hat p,\hat x)+d(\hat x_1,\hat p)
<r+r=2r.
$$

The map $\hat x\mapsto\gamma$ is injective by the free deck action. Hence the multiplicity

$$
m_r(x):=\#(\pi^{-1}(x)\cap B_r(\hat p))\le N(2r).
$$

*Step 3 (Volume bound via disjoint translates).* For each $x\in B_r(p)$, define $s(x)\in B_r(\hat p)$ to be the lift closest to $\hat p$ (breaking ties on a measure-zero equidistant set). Set $S:=\{s(x):x\in B_r(p)\}$.

Properties of $S$:

- $\pi\circ s=\operatorname{id}_{B_r(p)}$, so $\pi|_S:S\to B_r(p)$ is bijective.
- Since $\pi$ is a local isometry and $\pi|_S$ is injective, $\operatorname{Vol}(S)=\operatorname{Vol}(B_r(p))$.
- For each $\gamma\in\Gamma$ with $d(\hat p,\gamma\hat p)<2r$, the translate $\gamma S\subset B_{3r}(\hat p)$: if $s(x)\in S$ then

$$d(\gamma s(x),\hat p)\le d(\gamma s(x),\gamma\hat p)+d(\gamma\hat p,\hat p)=d(s(x),\hat p)+d(\gamma\hat p,\hat p)<r+2r=3r.$$

- The translates $\{\gamma S\}$ are pairwise disjoint: if $\gamma_1 s(x_1)=\gamma_2 s(x_2)$ then $\pi$ gives $x_1=x_2$, and then $\gamma_1=\gamma_2$ by the free action.

Therefore

$$
N(2r)\cdot\operatorname{Vol}(B_r(p))
= \sum_\gamma\operatorname{Vol}(\gamma S)
= \operatorname{Vol}\!\left(\bigsqcup_\gamma\gamma S\right)
\le \operatorname{Vol}(B_{3r}(\hat p)).
\tag{1}
$$

*Step 4 (Combining with Bishop–Gromov).* The local-isometry multiplicity identity gives

$$
\int_{B_r(\hat p)}\pi^*\varphi\,d\hat\mu
=
\int_{B_r(p)}m_r(x)\,\varphi(x)\,d\mu(x)
\le N(2r)\int_{B_r(p)}\varphi\,d\mu.
$$

Dividing by $\operatorname{Vol}(B_r(\hat p))$ and using (1):

$$
\fint_{B_r(\hat p)}\pi^*\varphi
\le
\frac{N(2r)\cdot\operatorname{Vol}(B_r(p))}{\operatorname{Vol}(B_r(\hat p))}\cdot\fint_{B_r(p)}\varphi
\le
\frac{\operatorname{Vol}(B_{3r}(\hat p))}{\operatorname{Vol}(B_r(\hat p))}\cdot\fint_{B_r(p)}\varphi.
$$

Since $\hat g=\pi^*g$ has $\operatorname{Ric}_{\hat g}\ge-(n-1)K\hat g$, Bishop–Gromov gives

$$
\frac{\operatorname{Vol}(B_{3r}(\hat p))}{\operatorname{Vol}(B_r(\hat p))}
\le\frac{V_K(3r)}{V_K(r)}
=:C(n,K,r).
\qquad\square
$$

**Remark 1 (Sheet count cancellation).** The proof shows that $N(2r)$ appears in both the numerator (multiplicity) and the denominator (via the disjoint-translates volume bound). Bishop–Gromov replaces the intermediate ratio $\operatorname{Vol}(B_{3r})/\operatorname{Vol}(B_r)$ by a universal constant. No information about the deck group $\Gamma$—its size, generators, nilpotency rank, lattice geometry, or growth rate—enters the final bound.

**Remark 2 (Numerical values).** For $n=4$, $K=1$, $r=1$ (our main application with $\operatorname{Ric}\ge-3g$):

$$
C(4,1,1)=\frac{V_{-1}^{(4)}(3)}{V_{-1}^{(4)}(1)}\approx949.5.
$$

For $r=1/2$: $C(4,1,1/2)\approx156.3$. These are large but universal; they do not grow with the collapse rate.

**Remark 3 (Measurability of the section).** The section $s$ is measurable because: (i) for each $\gamma\in\Gamma$, the set $\{x:d(\hat p,\gamma\hat x_1(x))=d(\hat p,s(x))\}$ (the equidistant set between $\gamma$ and $\operatorname{id}$) is a codimension-one submanifold in the smooth part, hence measure zero; (ii) the countable union of equidistant sets has measure zero; (iii) on the complement, $s$ is the unique closest-lift map, which is continuous on each Voronoi cell. This is a standard Voronoi construction for discrete group actions.

**Remark 4 (Buffer domain).** The buffer condition $B_{3r}(\hat p)\subset\widehat U$ is used in Step 3 to ensure that translates $\gamma S$ lie in the covering domain. For the universal cover of $B_{4r}(p)$ (which is always available when $B_{4r}(p)\subset M$), the buffer is automatic. For a normal subcover (e.g., a Naber–Zhang local cover), the buffer must be verified from the covering construction.

## 2. Subsumption of model proofs

The flat torus, principal circle, and nilpotent models from `step8_model_deck_transport.md` are all corollaries:

- **Flat torus** ($\mathbb{R}^n/\varepsilon\mathbb{Z}^m$): the constant is $C=3^n=81$ for $n=4$, matching the near-flat BG ratio. The previous lattice-counting proof gave the same result with more work.

- **Principal circle** ($S^1$-bundle with fiber $\rho$): the previous proof computed $N(2r)\approx Cr/\rho$ and $\operatorname{Vol}(B_{3r}(\hat p))/\operatorname{Vol}(B_r(\hat p))=3^n$ in the model, recovering $(\star)$. The general lemma avoids the warping/mean-curvature hypotheses.

- **Nilpotent collapse**: the previous proof needed a polynomial counting estimate (5) for lattice points in nilpotent balls, related to Mal'cev coordinates and Naber–Zhang graded generators. The general lemma shows this was unnecessary: the counting bound is absorbed by Bishop–Gromov regardless of group growth rate.

The only hypothesis in $(\star)$ beyond the covering structure is the Ricci lower bound (inherited from the base by local isometry) and the buffer domain. No nilpotency rank, generator control, bilipschitz model geometry, or deck-counting estimate is needed for the transport itself.

## 3. Strengthened exclusion theorem

Combining the transport lemma with the chain from `step8_derdzinski_measure_local_theorem.md`:

**Theorem (Cover-Noncollapsed Exclusion).** Let $(M_i,g_i)$ be a LeBrun near-boundary negative-pinching sequence:

- $\operatorname{Ric}_{g_i}\ge-3g_i$ eventually,
- $\delta_i=\|g_i^{-1}\operatorname{Ric}_{g_i}+I\|_\infty\to0$,
- the mixed-SW bookkeeping applies with $D_i/A_i\to0$ and $\operatorname{Vol}(M_i)/A_i\asymp1$.

Suppose for some fixed $r>0$, $v>0$, $\eta>0$, and infinitely many $i$, the set

$$
\mathcal{N}_i(r,v):=\left\{p\in M_i:\exists\text{ normal cover }\pi:(\widehat U,\hat g)\to(B_{4r}(p),g_i)\text{ with }\hat p\in\pi^{-1}(p),\; B_{3r}(\hat p)\subset\widehat U,\;\operatorname{Vol}(B_r(\hat p))\ge v\right\}
$$

satisfies $\operatorname{Vol}(\mathcal{N}_i(r,v))\ge\eta\operatorname{Vol}(M_i)$.

Then the sequence reaches a contradiction.

**Proof.** The explicit deficit density $F_i=|\operatorname{Ric}_{g_i}+g_i|^2+(s_i+8\sqrt{6}|W_i^+|)^2+\mathcal{G}_i$ satisfies

$$
\frac{1}{\operatorname{Vol}(M_i)}\int_{M_i}F_i\,d\mu_i\to0.
$$

By the volume-random basepoint lemma (Step 8, §3; Fubini + Bishop–Gromov doubling), for a uniformly random $p_i\in\mathcal{N}_i(r,v)$,

$$
\mathbb{E}\left[\fint_{B_r(p_i)}F_i\right]
\le\frac{C(4,1,r)}{\eta}\cdot\frac{1}{\operatorname{Vol}(M_i)}\int_{M_i}F_i\to0.
$$

Choose $p_i$ achieving the expectation bound. By hypothesis, there exists a normal cover with $\operatorname{Vol}(B_r(\hat p_i))\ge v$ and the buffer condition. The transport lemma gives

$$
\fint_{B_r(\hat p_i)}\pi^*F_i
\le C(4,1,r)\cdot\fint_{B_r(p_i)}F_i\to0.
$$

On the cover ball $B_r(\hat p_i)$ with volume $\ge v$, Cheeger–Naber Theorem 1.13 provides a positive-measure set with harmonic radius $\ge r_0(v)$ (see Step 8, §5). Select $q_i\in B_{r/2}(\hat p_i)$ with $r_h(q_i)\ge r_0$. On the harmonic chart around $q_i$:

- $C^{1,\beta}$ convergence holds from Arzelà–Ascoli and bounded harmonic radius.
- The harmonic-coordinate equation $g^{ab}\partial_a\partial_b g_{jk}=-2\operatorname{Ric}_{jk}+Q_{jk}(g^{-1},\partial g)$ has right-hand side converging strongly in $L^q$ (since $\operatorname{Ric}+g\to0$ in $L^\infty$ and $Q$ converges from $C^0$ metric convergence).
- Interior elliptic estimates give strong $W^{2,q}$ convergence for large finite $q$.
- The limit satisfies $\operatorname{Ric}=-g$ weakly, hence smoothly by elliptic regularity.

Strong $W^{2,q}$ convergence for $q>2$ in dimension 4 passes $W^+$, $s$, eigenvalues, and $\mathcal{G}$ in $L^1$. Since $\int F_i\to0$ on the chart, the limit satisfies

$$
s_\infty=-4,\quad s_\infty+8\sqrt{6}|W_\infty^+|=0,\quad \mathcal{G}_\infty=0.
$$

The explicit gap density forces $\operatorname{spec}(W_\infty^+)=(-1/6,1/12,1/12)$. Since $g_\infty$ is Einstein, $\delta W_\infty^+=0$. The two-eigenvalue constant-eigenvalue profile contradicts the Derdziński conformal factor (constant $\Rightarrow$ locally Kähler $\Rightarrow$ $|W^+|^2=2/3\neq1/24$) and independently contradicts the projector identity ($\nabla W_\infty^+=0$ versus $|\nabla W^+|^2=1/16$). $\square$

**Corollary (Noncollapsed + cover-noncollapsed exclusion).** In a LeBrun near-boundary sequence, for every fixed $v>0$, the volume proportion of points $p$ where EITHER $\operatorname{Vol}(B_1(p))\ge v$ (direct noncollapse) OR some normal cover provides a noncollapsed ball (in the sense of the theorem) tends to zero.

## 4. Precise remaining gap

The theorem excludes every collapsed region where a noncollapsed cover ball exists at a fixed scale. The genuinely open problem is whether the remaining scenario can occur:

**Scenario (Inaccessible collapse).** A near-boundary LeBrun sequence where, for almost all points, every normal cover of every fixed-scale neighborhood has Vol(cover ball) → 0.

This means: collapse at all scales, including all finite covers and the universal cover. The covering geometry cannot restore noncollapse at any fixed scale.

This scenario is constrained but not excluded by current tools:

1. **Naber–Zhang maximal-rank regularity.** Under maximal nilpotency rank and controlled model geometry, Naber–Zhang provides a cover with bounded harmonic radius. This cover is noncollapsed by construction. Thus inaccessible collapse can only occur when Naber–Zhang hypotheses fail: rank drop, singular fibers, degenerating lower-dimensional models, or vanishing model noncollapsing radius.

2. **Euler characteristic.** For the LeBrun blow-ups, $\chi(M_i)=\chi(X_i)+k_i$ and $2\chi+3\tau=A_i-k_i\approx2A_i/3$. The Chern–Gauss–Bonnet representative of $\chi$ is a curvature integral. If collapse is total, the Euler density must concentrate on singular/exceptional strata. Whether it can do so while maintaining Ric ≈ -g and the near-equality energy budget is an open question.

3. **Rescaling.** If the only accessible cover appears at scale $r_i\to0$, rescaling by $r_i^{-2}$ sends $\operatorname{Ric}\to0$ (Ricci-flat). The calibrated profile $|W^+|^2=1/24$ with $\operatorname{Ric}=-g$ loses its Seiberg–Witten support; the Derdziński contradiction does not apply at Ricci-flat scale. Therefore shrinking-scale covers do not extend the argument.

4. **Volume proportion vs. absolute.** For fixed critical $k/A$ (same manifold, $A$ fixed), absolute deficit vanishing gives $\sup_p\operatorname{Vol}B_1(p)\to0$ by the same argument. For varying $A_i\to\infty$, only volume proportion tends to zero; $o(\operatorname{Vol}M_i)$ noncollapsed islands may persist. The inaccessible-collapse scenario concerns the complementary volume proportion.

## 5. Scope correction: P₄⁺ and #_k(S² × S²)

The Strategist correctly notes: $P_4^+$ would not automatically produce Einstein metrics on every $\#_k(S^2\times S^2)$. The implication requires metrics satisfying the unknown pinching threshold $\delta<\varepsilon_4$, i.e., an arbitrarily tight positive-pinching sequence. Sha–Yang gives $\operatorname{Ric}>0$ on all $\#_k(S^2\times S^2)$, but this is qualitative positive Ricci, not quantitative pinching. The open attainability question—whether $\inf_g\delta_+(g)\to0$ on these manifolds—is a separate problem from the abstract $P_4^+$ statement. Keep this as a calibration question rather than an established implication.

## 6. Files and verification

- Script: `workspace/scripts/step9_normal_cover_transport.py` (computes BG constants, verifies cancellation, tests flat models)
- This note supersedes the model-specific §§2–5 of `workspace/notes/step8_model_deck_transport.md`
- The measure-local theorem in `workspace/notes/step8_derdzinski_measure_local_theorem.md` remains valid; the transport lemma strengthens its §7 conditional mechanism
