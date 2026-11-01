# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex",
    "Sessions/S0910A03/workspace/notes/step6_collapsed_unwrapping_route.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/step9_general_cover_transport.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md"
  ]
}
```

## Task

Independently verify and sharpen the proposed local mean transfer bridge for the fixed-topology critical Ishida–LeBrun sequence. Read the cited working notes and the Naber–Zhang source. Focus on: (i) whether the A01 normal-cover lemma is actually correct for local normal covers, including the closest-lift measurable section, disjoint translates, domain/buffer, and whether its RHS should use B_r(p) or a larger ball; (ii) whether combining that lemma with small base-ball means and Naber–Zhang Proposition 6.4 gives a fixed-scale harmonic chart on the cover for merely bounded Ricci; (iii) whether small mean of the full calibrated deficit on the cover is enough to force the forbidden Einstein germ through finite W^{2,p} convergence, including possible mismatch between the point selected for low mean and the point/scale where Naber–Zhang produces regularity. State a precise conditional theorem that is genuinely supported, and identify the exact unresolved hypothesis needed to apply it to almost all collapsed points. Do not assume Cheeger–Tian curvature decomposition or exact symmetric collapse models.

## Output

## Verification memo: local mean transfer bridge for the fixed critical Ishida–LeBrun sequence

I read the A03 note (step6), the A01 notes (step8, step9), and the Naber–Zhang source. Overall the chain is much more solid than most such constructions: the transport lemma is correct, the local rigidity is airtight, and the notes are careful to use only a harmonic‑radius consequence of Naber–Zhang (not a curvature bound and not exact symmetric models), which respects the constraints you set. The genuine open point is a single volume‑proportion statement about where Naber–Zhang's hypotheses actually hold. Below I check each requested link and then state exactly what is supported and what is missing.

---

### (i) The A01 normal‑cover transport lemma is correct, and the base ball is $B_r(p)$

Reading the four steps against the free proper isometric deck action:

- **Geodesic lifting.** For $x\in B_r(p)$ a minimizing base geodesic from $p$ has $d(p,\sigma(t))=t<r$, so $\sigma\subset B_r(p)\subset U$; its lift from $\hat p$ has the same length and lands in the intrinsic ball $B_r(\hat p)\subset\widehat U$. Every base point thus has a lift in $B_r(\hat p)$. Correct.
- **Multiplicity $\le N(2r)$.** For any two lifts $\hat x=\gamma\hat x_1,\hat x_1\in B_r(\hat p)$, $d(\hat p,\gamma\hat p)\le d(\hat p,\hat x)+d(\hat x_1,\hat p)<2r$; $\hat x\mapsto\gamma$ is injective by freeness. Since the deck group acts properly discontinuously, $N(2r)<\infty$. Correct.
- **Closest‑lift section and disjoint translates.** The Voronoi/closest‑lift map $s$ is measurable off a countable union of equidistant sets (Remark 3 is a standard construction); $\pi|_S$ is an injective local isometry so $\operatorname{Vol}(S)=\operatorname{Vol}(B_r(p))$; each $s(x)\in B_r(\hat p)$ because a lift in $B_r(\hat p)$ already exists. For $d(\hat p,\gamma\hat p)<2r$, $\gamma S\subset B_{3r}(\hat p)$, and the $N(2r)$ translates are pairwise disjoint (project to $x_1=x_2$, then $\gamma_1=\gamma_2$). Hence $N(2r)\operatorname{Vol}(B_r(p))\le\operatorname{Vol}(B_{3r}(\hat p))$. Correct.
- **Combination.** The exact multiplicity identity $\int_{B_r(\hat p)}\pi^*\varphi=\int_{B_r(p)}m_r(x)\varphi\,d\mu$ plus $m_r\le N(2r)$ plus the volume bound plus Bishop–Gromov on the cover (Ricci lower bound inherited by local isometry) give
$$\fint_{B_r(\hat p)}\pi^*\varphi\le \frac{V_K(3r)}{V_K(r)}\,\fint_{B_r(p)}\varphi.$$

The lemma holds as stated, and the sheet count genuinely cancels. The numerical constant is right in order: hyperbolic $V_{-1}^{(4)}(r)=\omega_3\int_0^r\sinh^3$, and $V_{-1}^{(4)}(3)/V_{-1}^{(4)}(1)\approx 949$, large but universal.

**Answer to the RHS question.** The base ball on the right is correctly $B_r(p)$, *not* a larger ball. The projection is distance‑nonincreasing, so $\pi(B_r(\hat p))\subseteq B_r(p)$, and the multiplicity identity is supported exactly on $B_r(p)$. The enlargement to $3r$ appears only on the *cover*, through Bishop–Gromov, and is the reason the domain must satisfy $U\supseteq B_{3r}(p)$ with the buffer $B_{3r}(\hat p)\subset\widehat U$. So the only real domain condition is: **the cover must be a normal cover of a ball of radius $\ge 3r$.** This is a scale constraint, addressed next; it is not an error in the RHS.

---

### (ii) Combining with small base means and Naber–Zhang Prop. 6.4 — coherent under one scale choice, subject to hypotheses

**Bounded‑Ricci output is available.** NZ Prop. 6.4 states precisely: $|\mathrm{Ric}|\le n-1$ + GH‑closeness to $\mathbb R^{k-\ell}\times Z^\ell$ ($\ell\le3$) + **maximal rank** $\operatorname{rank}\Gamma_\delta(p)=n-k$ $\Rightarrow$ weak harmonic radius $r_h(\tilde q)\ge h_0>0$ on the universal cover. The curvature bound (Prop. 6.5) needs Einstein or $|\nabla\mathrm{Ric}|$; the notes correctly use only the harmonic‑radius part. A harmonic‑radius lower bound with $\mathrm{Ric}\in L^\infty$ gives, via the harmonic‑coordinate equation $g^{ab}\partial_a\partial_b g_{jk}=-2\mathrm{Ric}_{jk}+Q(g,\partial g)$ and $L^p$ elliptic theory, uniform $C^{1,\alpha}\cap W^{2,p}$ metric bounds. So the harmonic‑radius input is exactly what the finite‑$W^{2,p}$ passage needs; no curvature bound is smuggled in.

**Scale alignment (a real bookkeeping point, resolvable).** NZ produce noncollapse $\operatorname{Vol}(B_{1/2}(\tilde q))\ge v_0$ and $r_h\ge h_0$ on the universal cover of $B_1(q)$ (domain radius $1$). The transport lemma at radius $r$ needs buffer $3r\le$ (domain radius). Taking $\widehat U=$ universal cover of $B_1(q)$, $U=B_1(q)$, and $r\le 1/3$ makes $B_{3r}(\hat p)\subset\widehat U$ automatic, the universal cover is normal with free $\pi_1$ action, and $B_r(\hat p)$ is noncollapsed by Bishop–Gromov from $\operatorname{Vol}(B_{1/2}(\tilde q))\ge v_0$. **Use $r=1/3$; then transport, buffer, and NZ regularity are mutually consistent.** The earlier informal use of $r=1$ against a $B_1$/$B_2$ domain does not satisfy the buffer; this is fixed by shrinking $r$, not by enlarging the base ball.

**The point/scale mismatch is resolvable, and it pins down the real requirement.** The low‑mean base point (from volume‑random averaging) and the maximal‑rank point where NZ acts must be the same. This is achieved by **restricting the averaging to the set $\mathcal R_i$ where NZ hypotheses hold**: if $\operatorname{Vol}(\mathcal R_i)\ge\eta\operatorname{Vol}(M)$, then some $p_i\in\mathcal R_i$ has $\fint_{B_r(p_i)}F_i\le\frac{C}{\eta}\cdot\frac{1}{\operatorname{Vol}M}\int_MF_i\to0$. Within the cover, the harmonic chart of radius $r_0\le r/2$ around $\tilde p_i$ sits inside $B_r(\hat p_i)$, and since $\operatorname{Vol}(B_{r_0}(\tilde p_i))\ge c(v_0)>0$ by Bishop–Gromov, transport of the mean gives $\fint_{\text{chart}}\pi^*F_i\to0$. So the intra‑cover mismatch closes. **The one thing this needs is that $\mathcal R_i$ has definite volume proportion $\eta>0$** — a single NZ‑good point does not suffice, because a base ball $B_r(p_i)$ may itself be collapsed (small volume) and then its mean of $F_i$ need not be small even though $\int_MF_i\to0$.

---

### (iii) Small cover mean of the full calibrated deficit does force the forbidden germ

Given the fixed‑size harmonic chart with $\fint_{\text{chart}}\pi^*F_i\to0$:

- On the cover $\|\mathrm{Ric}_{\hat g_i}+\hat g_i\|_{L^\infty}=\delta_i\to0$ (local isometry preserves the sup norm; this term is uniformly small, not merely small in mean). The Weyl/scalar deficits $(s+8\sqrt6|W^+|)^2$ and $\mathcal G$ are only integrally small; transport is what carries their integral smallness to the chart. This is exactly the role of the lemma.
- The harmonic‑coordinate elliptic passage gives $C^{1,\beta}$ and strong $W^{2,q}_{\rm loc}$ convergence of $\hat g_i$ to a **smooth open** Einstein germ with $\mathrm{Ric}=-g_\infty$ (weak $\to$ smooth by elliptic regularity of the Einstein equation in harmonic coordinates). No $C^{2,\alpha}$ control of the approximants is used. Correct.
- Curvature $=\partial^2g+(\partial g)^2$ converges in $L^q$; since $s,|W^+|,$ eigenvalues, $a_-$ are Lipschitz functions of curvature, the densities converge in $L^{q/2}$. The chart integrals tending to zero then force pointwise, on the smooth limit, $s_\infty=-4$, $s_\infty+8\sqrt6|W^+_\infty|=0$, $\mathcal G_\infty=0$.

The algebra behind $\mathcal G$ checks out. I verified the completion identity
$$\tfrac{s^2}{24}+2u^2=\tfrac1{12}f^2+\tfrac1{216}(s+8\sqrt6u)^2,\qquad f=\tfrac23s-2\alpha u,\ \alpha=\sqrt{2/3},$$
term by term ($s^2$: $\tfrac1{27}+\tfrac1{216}=\tfrac1{24}$; $su$: $-\tfrac29\alpha+\tfrac{2\sqrt6}{27}=0$; $u^2$: $\tfrac29+\tfrac{16}9=2$). At $s=-4,u=1/(2\sqrt6)$ one gets $f=-3$ and $\mathcal G=4\xi(3-\xi)$ with $\xi=w+\sqrt{2/3}\,|W^+|\ge0$; the eigenvalue bound $w\ge-\sqrt{2/3}\sqrt{\sum\lambda_i^2}$ (extremal at $(-2a,a,a)$) is exactly the nonnegativity of $\xi$, and $\mathcal G=0$ forces $\xi=0$, $w=-1/6$, spectrum $(-1/6,1/12,1/12)$, $|W^+|^2=\tfrac32w^2=1/24$.

The local exclusion is the strongest link and is fully correct:

- **Projector lemma.** With $\delta W^+_\infty=0$ (Einstein $\Rightarrow$ second Bianchi), two distinct constant eigenvalues, and a smooth simple eigenform $\omega$ ($\lambda\ne\mu$), retaining both product terms gives $\nabla^a\omega_{ab}=0$, then $\omega_{ab}\nabla^a\omega_{cd}=0$; nondegeneracy of the self‑dual 2‑form ($\omega_a{}^c\omega_c{}^b=-\delta_a^b$) forces $\nabla\omega=0$, hence $\nabla W^+_\infty=0$. Sign‑independent, as stated.
- **Einstein–Weyl.** $\Delta|W^+|^2=2|\nabla W^+|^2+s|W^+|^2-36\det W^+$ with $\det W^+=-1/864$ gives, if $|W^+|^2$ is constant, $2|\nabla W^+|^2=-(-4)(1/24)+36(1/864)=\tfrac16-\tfrac1{24}=\tfrac18$, i.e. $|\nabla W^+|^2=1/16\ne0$. Contradiction with the projector lemma.
- **Derdziński route agrees.** The conformal factor $(24|W^+|^2)^{1/3}=1$ makes $g_\infty$ itself locally Kähler, but a Kähler–Einstein metric with $s=-4$ has $\operatorname{spec}(W^+)=(-2/3,1/3,1/3)$, $|W^+|^2=s^2/24=2/3\ne1/24$.

Both routes are local and need no completeness, so they apply to the open germ. Part (iii) is genuinely supported.

---

### Precise conditional theorem that is supported

**Theorem (supported).** Let $(M^4,g_i)$ be a fixed critical Ishida–LeBrun sequence with $\delta_i\to0$, so $\|\mathrm{Ric}_{g_i}+g_i\|_{L^\infty}\to0$, $\mathrm{Ric}_{g_i}\ge-3g_i$ eventually, and $\int_M F_i\to0$ for the nonnegative density $F_i=|\mathrm{Ric}+g|^2+(s+8\sqrt6|W^+|)^2+\mathcal G$. Fix $r\in(0,1/3]$, $v_0>0$, $r_0>0$. Suppose there is $\eta>0$ and infinitely many $i$ with a set $\mathcal R_i\subseteq M$, $\operatorname{Vol}(\mathcal R_i)\ge\eta\operatorname{Vol}(M)$, such that at every $p\in\mathcal R_i$:
1. $B_2(p)$ is $\epsilon_0$‑GH close to some $\mathbb R^{k-\ell}\times Z^\ell$ with $\ell\le3$ and model noncollapsing radius $r_c(z^\ell)\ge r_0$, and
2. $\operatorname{rank}\Gamma_\delta(p)=4-k$ (maximal).

Then for large $i$ a contradiction arises. Consequently the maximal‑rank/uniform‑model set has $\operatorname{Vol}(\mathcal R_i)/\operatorname{Vol}(M)\to0$.

*Proof structure.* NZ Prop. 5.9/6.4 give $\operatorname{Vol}(B_{1/2}(\tilde p))\ge v_0(r_0)$ and $r_h(\tilde p)\ge h_0(r_0)$ uniformly on the universal cover of $B_1(p)$. Restrict the volume‑random averaging to $\mathcal R_i$ to select $p_i\in\mathcal R_i$ with $\fint_{B_r(p_i)}F_i\to0$. Apply the transport lemma with $U=B_1(p_i)$, $\widehat U$ the universal cover, $r=1/3$ (buffer automatic). Then $\fint_{\text{chart}}\pi^*F_i\to0$ on a fixed‑size harmonic chart in $B_r(\hat p_i)$; finite $W^{2,q}$ convergence produces a smooth open Einstein germ with the calibrated spectrum, excluded by the projector/Einstein–Weyl (or Derdziński) rigidity. ∎

This uses no Cheeger–Tian curvature decomposition and no exact symmetric collapse model — only the model‑free transport lemma and NZ's harmonic‑radius statement.

---

### The exact unresolved hypothesis, and where it can break

To reach *almost all* collapsed points (and hence exclude the whole fixed critical sequence), the missing input is precisely:

> **(H)** All but $o(\operatorname{Vol}M_i)$ of the volume consists of points $p$ where $B_2(p)$ is GH‑close to some $\mathbb R^{k-\ell}\times Z^\ell$ with $\ell\le3$ and *uniform* model noncollapsing radius $r_c\ge r_0>0$, **and** the fibered fundamental group has maximal nilpotency rank $\operatorname{rank}\Gamma_\delta(p)=4-k$.

Equivalently: the complementary set — rank drop, singular fibers, degenerating low‑dimensional models ($r_c\to0$), or residual four‑dimensional bubbles ($\ell=4$) — has vanishing volume proportion. Three concrete points make (H) genuinely open rather than technical:

- **NZ's own examples show the complement is real and carries the interesting geometry.** The K3 singular fibration has rank drop with curvature concentration exactly on the $I_1$ (rank‑one) fibers; Eguchi–Hanson gives an $\ell=4$ residual factor where NZ is sharp (Remark 1.3) and no harmonic‑radius bound holds. LeBrun‑type sequences plausibly develop precisely such ALE/bubble regions.
- **Uniform model constants are indispensable.** NZ constants depend on $Z^\ell$ through $r_c(z^\ell)$; if the low‑dimensional models degenerate, $h_0\to0$ and no fixed‑scale chart survives even at maximal rank. (H) must include $r_c\ge r_0$ uniformly.
- **Topology localization is untouched by this bridge.** For these manifolds $2\chi+3\tau=A_i-k_i\approx 2A/3$, and the Chern–Gauss–Bonnet Euler density integrates to $\chi$. If regular maximal‑rank collapse held on nearly all volume, the Euler/signature content would have to be carried on the vanishing‑proportion complement; whether that is geometrically possible while keeping $\mathrm{Ric}\approx-g$ is exactly what the transport bridge does not decide.

---

### Distinctions worth keeping precise

- **Direct base noncollapse gives a supremum statement; cover noncollapse gives only a proportion statement.** If some base ball $B_1(p_i)$ is noncollapsed, its mean $\fint_{B_r(p_i)}F_i\le \int_MF_i/\operatorname{Vol}B_r(p_i)\to0$ from a single point (Bishop–Gromov lower‑bounds $\operatorname{Vol}B_r(p_i)$), so $\sup_p\operatorname{Vol}B_1(p)\to0$ for fixed topology. For *cover* noncollapse the base ball may be collapsed, so a single point does not give a small base mean; one needs a definite‑proportion set to run the averaging. The A01 step9 theorem correctly demands $\operatorname{Vol}(\mathcal N_i)\ge\eta\operatorname{Vol}(M)$; the A03 boxed $\sup_p\operatorname{Vol}B_1(p)\to0$ is the direct statement and should not be conflated with the cover‑noncollapse conclusion.
- **Fixed vs. varying topology.** All of the above is absolute only because $A$ is fixed. For $A_i\to\infty$ the deficits are normalized, so even the direct statement weakens to volume proportion, and $o(\operatorname{Vol}M_i)$ noncollapsed or concentrated regions may persist. The bridge does not transfer to the varying‑$A_i$ pinching question.

### Two smaller items to pin down against sources
- The Cheeger–Naber "Theorem 1.13 / Remark 1.11" harmonic‑radius estimate is cited but not present in the supplied files; the qualitative content (noncollapsed + bounded Ricci $\Rightarrow$ harmonic radius bounded below off a small set) is standard, and in the $r=1/3$ NZ route it can be replaced entirely by NZ Prop. 6.4. It would be worth confirming the exact statement/constants against the Cheeger–Naber paper, or dropping it in favor of Prop. 6.4.
- The connectivity/normality of the relevant cover: NZ deliver noncollapse on the universal cover of $B_1(p)$; taking that as $\widehat U$ with $U=B_1(p)$ and $r=1/3$ is clean, but if one instead wants a connected component of $\pi^{-1}$ of a smaller ball as the normal cover, NZ Lemma 5.3 (nonlocalness of rank) is the tool to verify the deck group descends. The $r=1/3$ universal‑cover choice avoids this and is the simplest supported route.