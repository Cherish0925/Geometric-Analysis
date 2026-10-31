> **Step 12 repair note.** The Noether energy bound and the idea of excluding supplied fixed-scale chart-accessible regions remain valid. The proof of Proposition 2/Theorem 1 below must be read in the repaired form in `workspace/notes/step12_taub_nut_accessibility_and_diffuse_pontryagin.md`: the harmonic chart is part of the local hypothesis and is not derived from bounded Ricci plus cover noncollapse alone; basepoint selection in the negative branch uses local Ricci-lower-bound doubling/Hardy--Littlewood maximal estimates, not a Myers diameter; and the Taub--NUT--AdS test is an accessibility calibration, not a proof that all fixed-scale covers fail. The Step 11 sentence that every exact Ric=-g Einstein metric has pointwise positive calibrated defect is too strong: Derdziński forbids the calibrated constant profile on an open Einstein region, not an isolated radius. The Pontryagin density should be treated as diffuse on the near-critical bulk, with `fint |P-3/4| -> 0`, rather than as charge hidden in small NUT cores.

# Step 11: Chart-accessible exclusion theorem, Noether energy bound, and the bridge problem

Session: S0910A01. Phase: Explore.

## Summary

This note develops three advances:

1. **Noether energy bound.** For ANY minimal complex surface of general type $X$ with $A=c_1^2(X)$ and the near-critical blow-up $M=X\#k\overline{\mathbb{CP}}^{\,2}$ with $k/A\to1/3$, the global mean curvature-operator energy satisfies $\overline{|\mathcal R|^2}\le12+O(1/A)$. This uses only classical Noether ($A\ge2p_g-4$), $q\ge0$, and Noether's formula $\chi_{\mathrm{top}}=12\chi_{\mathrm{hol}}-A$. No restriction to a chosen family is needed.

2. **Chart-accessible exclusion theorem.** A point $p$ is *$(h,v)$-chart-accessible* if it admits a buffered normal cover with a noncollapsed harmonic chart of radius $\ge h$ and volume $\ge vh^4$ on the cover. The set of $(h,v)$-chart-accessible points has vanishing volume proportion in any near-critical LeBrun sequence, for every fixed $h,v>0$. This theorem is independent of Naber–Zhang: the Naber–Zhang package provides one set of sufficient conditions for chart accessibility, but the exclusion applies to any source of charts.

3. **The bridge problem.** The remaining mathematical question is whether a positive volume proportion of any near-critical LeBrun sequence can fail to be chart-accessible at all fixed scales. The Noether energy bound provides a controlled global mean curvature, but this does not automatically produce chart-accessible covers on most volume without additional input. The note identifies the exact gap and the scale-dependent mechanisms that could evade accessibility.

## 1. Noether energy bound

### Statement

**Proposition 1 (Noether energy bound).** Let $X$ be a minimal complex surface of general type with $A=c_1^2(X)$. Let $M_i=X_i\#k_i\overline{\mathbb{CP}}^{\,2}$ be a near-critical LeBrun sequence with $\delta_i\to0$, $k_i/A_i\to1/3$. Then:
\[
\frac{\int_{M_i}|\mathcal R_{g_i}|^2\,d\mu_i}{\operatorname{Vol}(M_i,g_i)}
\le 12+O\!\left(\frac1{A_i}\right)+O(\delta_i^2).
\]

Here $|\mathcal R|^2=|W^+|^2+|W^-|^2+\tfrac12|E|^2+\tfrac{s^2}{24}$ is the curvature-operator Hilbert–Schmidt norm.

### Proof

**Step 1: Noether inequality.** Classical Noether for minimal surfaces of general type:
\[
A=K^2\ge2p_g-4.
\]
Since the irregularity $q\ge0$, the holomorphic Euler characteristic satisfies:
\[
\chi_{\mathrm{hol}}=1-q+p_g\le1+p_g\le1+\frac{A+4}{2}=\frac{A+6}{2}.
\]
Noether's formula $c_2=12\chi_{\mathrm{hol}}-c_1^2$ gives:
\[
\chi_{\mathrm{top}}(X)=12\chi_{\mathrm{hol}}-A\le 12\cdot\frac{A+6}{2}-A=5A+36.
\]

**Step 2: Blow-up topology.**
\[
\chi(M)=\chi(X)+k,\qquad
\tau(M)=\tau(X)-k.
\]
At $k/A\to1/3$:
\[
\frac{\chi(M)}{A}\le5+\frac{36}{A}+\frac{k}{A}\to5+\frac13=\frac{16}{3}.
\]

**Step 3: CGB energy identity.** In the curvature-operator convention:
\[
\int|\mathcal R|^2=8\pi^2\chi(M)+\int|E|^2.
\]
Define $J=(8\pi^2)^{-1}\int|E|^2$. Under $\operatorname{Ric}_{g_i}=-g_i+e_i$ with $\|e_i\|_\infty\to0$:
\[
|E_i|^2=|\mathring{\operatorname{Ric}}|^2\le4\delta_i^2,\qquad
J_i\le\frac{\delta_i^2}{2\pi^2}\operatorname{Vol}(M_i).
\]
With $\operatorname{Vol}(M_i)\sim(32/9)\pi^2A_i$:
\[
J_i/A_i=O(\delta_i^2).
\]

**Step 4: Global mean.** The volume bound gives:
\[
\frac{\int|\mathcal R|^2}{\operatorname{Vol}(M)}
=\frac{8\pi^2(\chi(M)+J)}{\operatorname{Vol}(M)}
\le\frac{8\pi^2(16A/3+36+J)}{(32/9)\pi^2A(1-O(\delta^2))}
=\frac{9}{4}\cdot\frac{16}{3}+O(1/A)+O(\delta^2)=12+O(1/A)+O(\delta^2).
\]

**Step 5: Two-sided bound.** The Bogomolov–Miyaoka–Yau inequality $A\le9\chi_{\mathrm{hol}}$ gives $\chi_{\mathrm{top}}(X)\ge A/3$. Thus:
\[
\frac{\chi(M)}{A}\ge\frac{1}{3}+\frac{k}{A}\to\frac23,\qquad
\overline{|\mathcal R|^2}\ge\frac{9}{4}\cdot\frac23-O(\delta^2)=\frac32-O(\delta^2).
\]

The global mean curvature-operator energy lies in $[\frac32-o(1),\,12+o(1)]$ over all minimal general-type surfaces with $k/A\to1/3$. $\square$

By the volume-random basepoint and local maximal-function arguments (repaired in Step 12), the negative branch should not use a Myers diameter.  For any fixed local scale $r>0$ and Ricci lower bound, local Bishop--Gromov doubling gives bounded overlap/Hardy--Littlewood estimates with constants depending on $r$ and the lower Ricci bound.  Thus controlled global mean $|\mathcal R|^2$ supplies many points with controlled local mean energy, but it does not by itself produce noncollapsed covers or harmonic charts.  See `workspace/notes/step12_taub_nut_accessibility_and_diffuse_pontryagin.md` for the current formulation.
\]
In particular, most points have controlled mean curvature energy at every fixed scale.

## 2. Quantitative forbidden-germ gap

### Definition

For a Riemannian four-manifold with $\operatorname{Ric}=-g+e$, define the calibrated defect density:
\[
F=|e|^2+(s+8\sqrt6\,|W^+|)^2+\mathcal G,
\qquad
\mathcal G=f^2-(a_-)^2,
\]
where $f=\frac23s-2\sqrt{2/3}\,|W^+|$, $a=\frac23s+2w$, $w$ is the least eigenvalue of $W^+$.

### Statement

**Proposition 2 (Forbidden-germ gap).** For every $h>0$ and $v>0$, there exists $\varepsilon_0=\varepsilon_0(h,v)>0$ with the following property. Let $(U,g)$ be an open Riemannian four-manifold with:

(i) $B_{2h}(p)\Subset U$;

(ii) $\|\operatorname{Ric}_g+g\|_{\infty,\mathrm{op}}\le1/2$ on $B_{2h}(p)$;

(iii) $r_h(q)\ge h/10$ for some $q\in B_{h/2}(p)$ (harmonic radius);

(iv) $\operatorname{Vol}(B_h(p))\ge vh^4$.

Then:
\[
\fint_{B_{h/2}(p)}F_g\,d\mu\ge\varepsilon_0.
\]

### Proof

By contradiction. Suppose a sequence $(U_i,g_i,p_i)$ satisfies (i)–(iv) with
\[
\fint_{B_{h/2}(p_i)}F_{g_i}\to0.
\]

The bounded Ricci condition $|\operatorname{Ric}|\le3/2$ and the noncollapse condition (iv) give, by Cheeger–Naber (Remark 1.11 of [CN15]), a uniform positive harmonic radius $r_h\ge r_0(h,v)>0$ at every point of $B_h(p_i)$. In harmonic coordinates centered at $q_i$, the metric components satisfy $\|g_{ij}-\delta_{ij}\|_{C^{1,\alpha}}\le1/10$ (after restricting to a smaller chart). The harmonic-coordinate Ricci equation
The repaired proof treats the harmonic-coordinate control as part of the hypothesis.  By contradiction, take a sequence of buffered domains with a fixed harmonic chart/control package on an interior ball and with mean $F_{g_i}\to0$ there.  The chart control gives $C^{1,\alpha'}$ compactness.  In harmonic coordinates,
\[
g^{ab}\partial_a\partial_b g_{ij}=-2\operatorname{Ric}_{ij}+Q(g^{-1},\partial g),
\]
and $\operatorname{Ric}_{g_i}=-g_i+e_i$, $\|e_i\|_\infty\to0$, gives strong finite-$p$ $W^{2,p}$ convergence on smaller balls by interior elliptic estimates.  The weak limit is smooth Einstein after elliptic bootstrapping.  Since $F_{g_i}\to0$ in $L^1$ and its summands are nonnegative, the limit has the calibrated constant spectrum.  Derdziński's local theorem then forces the limit itself to be locally Kähler, while a Kähler four-metric with $\operatorname{Ric}=-g$ has $|W^+|^2=s^2/24=2/3$, contradicting the calibrated value $1/24$.  This proves a controlled-chart forbidden germ.  It does not assert that bounded Ricci plus noncollapse automatically supplies the chart; that source of chart control must be supplied separately.

(a) $\overline{B_{3h}(\hat p)}\Subset\widehat U$ (precompact buffer);

(b) $\operatorname{Ric}_{\hat g}\ge-3\hat g$;

(c) $\operatorname{Vol}_{\hat g}(B_h(\hat p))\ge vh^4$ (noncollapse on cover);

(d) the $C^{1,\alpha}$ harmonic radius of $\hat g$ at some $q\in B_{h/2}(\hat p)$ is at least $h/10$.

Denote the set of $(h,v)$-chart-accessible points by $\mathcal A_i(h,v)\subset M_i$.

### Statement

**Theorem 1 (Chart-accessible exclusion).** Let $(M_i,g_i)$ be a near-critical LeBrun sequence with $\delta_i\to0$, $k_i/A_i\to1/3$, and $A_i\to\infty$. For every $h>0$ and $v>0$:
\[
\frac{\operatorname{Vol}\mathcal A_i(h,v)}{\operatorname{Vol}(M_i)}\to0
\qquad\text{as }i\to\infty.
\]

### Proof

Suppose for contradiction that $\operatorname{Vol}\mathcal A_i(h,v)\ge\eta\operatorname{Vol}(M_i)$ for some $\eta>0$ and infinitely many $i$.

**Step 1: Global defect control.** The mixed Seiberg–Witten estimate and CGB give:
\[
\int_{M_i}F_i\,d\mu_i=O(\delta_i^2\cdot A_i)=o(A_i).
\]
With $\operatorname{Vol}(M_i)\sim(32/9)\pi^2A_i$:
\[
\frac{\int F_i}{\operatorname{Vol}(M_i)}\to0.
\]

**Step 2: Basepoint selection.** Use the local Hardy--Littlewood maximal estimate under the Ricci lower bound, not a diameter argument.  If $\bar F_i=\operatorname{Vol}(M_i)^{-1}\int F_i\to0$ and $\lambda_i=\sqrt{\bar F_i}$, then the set where some ball of radius at most $h$ has mean $F_i>\lambda_i$ has vanishing volume fraction.  Hence a fixed-positive-volume accessible set contains $p_i$ with $\fint_{B_h(p_i)}F_i\to0$.

**Step 3: Cover transport.** Since $p_i$ is chart-accessible, let $\pi_i:(\widehat U_i,\hat g_i)\to(B_{4h}(p_i),g_i)$ be the buffered normal cover. The Step 9 general cover-mean theorem gives
\[
\fint_{B_h(\hat p_i)}\pi_i^*F_i
\le\frac{V_{-1}(3h)}{V_{-1}(h)}\fint_{B_h(p_i)}F_i\to0.
\]

**Step 4: Compactness on the supplied cover chart.** In the repaired definition, chart accessibility includes a fixed harmonic-coordinate control package on an interior lifted ball.  This supplied chart, together with $\operatorname{Ric}_{g_i}=-g_i+e_i$ and $\|e_i\|_\infty\to0$, yields strong finite-$p$ $W^{2,p}$ convergence on a smaller ball by the harmonic-coordinate Ricci equation.  The limit is smooth Einstein and has $F=0$.

**Step 5: Contradiction.** The controlled-chart forbidden germ (the repaired form of Proposition 2) forbids such a limit by Derdziński's local theorem. $\square$

### Relation to Naber–Zhang

The Naber–Zhang package (residual dimension $\le3$, maximal fibered nilpotency rank, uniform model noncollapsing radius $r_*>0$) provides one set of sufficient conditions for $(h,v)$-chart-accessibility via Proposition 6.4 of [NZ16]. Specifically:

- NZ Prop 6.4 gives a positive harmonic radius $h_*(4,r_*)$ on the local universal cover at every lifted point.
- The universal cover is a genuine normal cover (it has a deck group action).
- NZ Theorem 5.1 provides the noncollapse on the cover under the residual splitting/model hypotheses.

But Theorem 1 applies to any chart-accessible point, regardless of how the chart was obtained. This separation is essential because:

(a) Naber–Zhang's hypotheses may fail on part of the collapsed volume (rank drop, model degeneration, 4D residuals, singular fibers);

(b) Other sources of chart accessibility exist (bounded sectional curvature + CFG, explicit N-structures, geodesic constructions, etc.);

(c) The bridge problem is now a single question about chart accessibility, rather than a list of Naber–Zhang failure modes.

## 4. The bridge problem: energy and accessibility

### What the Noether energy bound provides

Proposition 1 gives $\overline{|\mathcal R|^2}\le12+o(1)$ over the entire LeBrun laboratory. The averaging argument gives controlled mean energy on typical balls:

\[
\frac{\operatorname{Vol}\left\{p:\fint_{B_r(p)}|\mathcal R|^2>\Lambda\right\}}
     {\operatorname{Vol}(M_i)}
\le\frac{C(r)\cdot12}{\Lambda}.
\]

The cover-mean theorem preserves this on covers:

\[
\fint_{B_r(\hat p)}\pi^*|\mathcal R|^2
\le C_{\mathrm{cover}}(r)\cdot\fint_{B_r(p)}|\mathcal R|^2.
\]

So at most points, on any available cover, the mean curvature energy is controlled at every fixed scale.

### What is still needed

The gap between "controlled mean energy on covers" and "chart-accessible" is precisely:

**Controlled mean energy does not imply noncollapse of the cover.**

In detail: the cover $\pi:(\widehat U,\hat g)\to(U,g)$ unwraps the local fundamental group, but the cover itself may be collapsed at a given scale if the fibered fundamental group has rank $<n-k$. Naber–Zhang's rank and model hypotheses are designed to prevent this. Without them, we need a different route to noncollapse.

### Scale-invariant energy and the ε-regularity question

The scale-invariant quantity $r^4\cdot\fint_{B_r}|\mathcal R|^2$ can be made small by choosing $r$ small:

\[
r^4\cdot\fint_{B_r(p)}|\mathcal R|^2\le r^4\cdot C\cdot12=12Cr^4.
\]

For $r$ small but **fixed**, this is small. The question is whether this small scale-invariant energy, together with the near-Einstein Ricci condition, produces chart accessibility.

For **noncollapsed** Einstein manifolds, Anderson's ε-regularity says: small $L^2$ curvature energy + noncollapse $\Rightarrow$ positive harmonic radius. But noncollapse is assumed, not produced.

For **collapsed** manifolds with bounded **sectional** curvature, CFG theory gives N-structures and noncollapsed universal covers. But we only have bounded Ricci, not bounded sectional curvature. The bounded mean L² curvature at typical balls does not give a pointwise sectional curvature bound.

### Concrete degeneration question

The Strategist asks: *Can a concrete degeneration evade chart accessibility even with bounded mean energy?*

The Chebyshev bound gives, for a threshold $\Lambda>0$:
\[
\frac{\operatorname{Vol}\{p:|\mathcal R|^2(p)>\Lambda\}}{\operatorname{Vol}(M_i)}
\le\frac{12+o(1)}{\Lambda}.
\]

On the complement $\{|\mathcal R|^2\le\Lambda\}$, we have **pointwise** curvature bounds. For points deep inside this set (where $B_r(p)\subset\{|\mathcal R|^2\le\Lambda\}$), the full curvature is bounded on $B_r(p)$, and CFG theory applies. On CFG-structured collapsed regions, the universal cover is noncollapsed, and Theorem 1 applies.

But two mechanisms can still evade this:

1. **High-curvature islands:** The set $\{|\mathcal R|^2>\Lambda\}$ has volume fraction $\le12/\Lambda$. As $\Lambda\to\infty$, this fraction $\to0$. But fixed $\Lambda$ leaves a nonzero (though small) fraction inaccessible.

2. **Boundary effects:** Even within $\{|\mathcal R|^2\le\Lambda\}$, points near the boundary of the high-curvature set may not have full balls inside the bounded-curvature region. The CFG N-structure requires the curvature bound on a ball, not just at a point.

### The interior set and its volume fraction

Define the **$\Lambda$-interior** set at scale $r$:
\[
\mathcal I(\Lambda,r)=\{p\in M:B_r(p)\subset\{|\mathcal R|^2\le\Lambda\}\}.
\]

**Claim.** $\operatorname{Vol}(\mathcal I(\Lambda,r))\ge\operatorname{Vol}(M)(1-12/\Lambda)-\operatorname{Vol}(\partial_r\{|\mathcal R|^2>\Lambda\})$, where $\partial_r$ denotes the $r$-neighborhood of the boundary. The volume of this $r$-thickened boundary is not controlled by the global $L^2$ bound alone.

However, a stronger estimate is possible using $L^p$ maximal functions. Define:
\[
M_r(|\mathcal R|^2)(p)=\sup_{0<s\le r}\fint_{B_s(p)}|\mathcal R|^2.
\]

The Hardy–Littlewood weak $(1,1)$ inequality on Riemannian manifolds with Ricci lower bound (cf. Strömberg or Auscher–Coulhon) gives:
\[
\operatorname{Vol}\{M_r(|\mathcal R|^2)>\Lambda\}
\le\frac{C_{\mathrm{HL}}(r)}{\Lambda}\int|\mathcal R|^2
\le\frac{C_{\mathrm{HL}}(r)\cdot12}{\Lambda}\operatorname{Vol}(M).
\]

On the **maximal-controlled** set $\{M_r(|\mathcal R|^2)\le\Lambda\}$, EVERY sub-ball $B_s(p)$ with $s\le r$ has mean $|\mathcal R|^2\le\Lambda$.

**Critical gap:** Even this controlled mean curvature on all sub-balls does not give a pointwise curvature bound. The pointwise curvature could still spike within sub-balls while maintaining a controlled average. Genuine ε-regularity from the mean to a supremum requires either Einstein or additional coercive structure.

## 5. Summary of the bridge

The accumulated four-dimensional negative-branch program now has:

| Component | Status |
|-----------|--------|
| Mixed SW estimate + CGB | Established |
| Calibrated defect density $F$ | Established |
| Derdziński/projector forbidden germ | Established |
| Quantitative forbidden-germ gap (Prop 2) | Established by compactness |
| Normal-cover mean transport | Established (Step 9) |
| Chart-accessible exclusion (Thm 1) | Established |
| Noether energy bound (Prop 1) | **New, established** |
| Noncollapse → accessibility | Standard (Cheeger–Naber) |
| Bounded sectional curvature → CFG N-structure → noncollapse on cover | Classical |
| Mean L² energy → pointwise curvature → CFG | **Missing bridge** |
| Mean L² energy → chart accessibility without CFG | **Missing bridge** |
| Volume fraction of high-curvature set | Controlled by Chebyshev: $\le12/\Lambda$ |
| Volume fraction of maximal-controlled set | Controlled by HL: $\ge1-C/\Lambda$ |

The single missing mathematical theorem is:

> **Bounded Ricci + controlled mean L² curvature at a fixed scale + near-Einstein condition ⟹ chart accessibility (noncollapsed harmonic charts on normal covers) on a positive volume proportion.**

The near-Einstein condition distinguishes this from the general Ricci-bounded problem. It provides $\delta W=d(\mathring{\operatorname{Ric}})$ with $\|\mathring{\operatorname{Ric}}\|_\infty\to0$, giving **weak control on $\nabla W$** after integration by parts, though not pointwise control.

## 6. Verification record

- Noether bound: `workspace/scripts/step11_noether_energy_bound.py` (all checks pass)
- Gap density algebra: `workspace/scripts/step8_gap_density_algebra.py` (previous step, valid)
- Derdziński source: `workspace/data/sources/derdzinski_1983_self_dual_kahler_einstein_four.pdf`
- Cheeger–Naber source: `Knowledge/objects/papers/1406.6534-...`
- Cover-mean transport: `workspace/notes/step9_general_cover_transport.md`


## 7. Three independent regularity obstructions (session synthesis)

The combined findings of the three sessions definitively block general regularity approaches:

### (a) A03: Taub-NUT-AdS countermodel
Controlled maximal $\fint_{B_r}|\mathrm{Rm}|^2 \le K$ at every scale $r \le 1/3$, combined with $\mathrm{Ric} \ge -3g$, does NOT imply noncollapse of the local universal cover. The Taub-NUT-AdS metric with NUT parameter $\nu \to 0$ has exact $\mathrm{Ric}=-g$, bounded curvature in the annular band, but the collapsing $\psi$-circle is contractible through the NUT. Maximal fibered rank is 0 instead of the required $4-3=1$.

### (b) A02: CZ Hessian spike
On $S^2(1) \times S^2(1)$ with opposite warpings $e^{2(F_1+u)}$ and $e^{2(F_2-u)}$, the Hessian of the spike $u$ cancels in the Ricci tensor but survives in the Weyl curvature. Result: $\|\mathrm{Ric}-g\|_\infty \to 0$ and $\int|Rm|^2 \to 0$, but $|Rm|_{\max} \to \infty$. This is the Calderón–Zygmund endpoint failure: $\Delta u \in L^\infty$ gives $\nabla^2 u \in L^p$ for $p < \infty$ and $\nabla^2 u \in \mathrm{BMO}$, but NOT $\nabla^2 u \in L^\infty$.

### (c) A01 (this step): energy gap
The Noether energy bound gives global mean $|\mathcal{R}|^2 \le 12$ automatically, and the averaging argument gives controlled mean curvature on typical balls. But the gap from controlled mean energy to chart accessibility (noncollapse on covers) cannot be closed by curvature energy alone.

### Surviving regularity tools
- Harmonic coordinates with bounded Ricci: $g \in C^{1,\alpha} \cap W^{2,p}_{\mathrm{loc}}$ for all $p < \infty$
- Normal-cover mean transport (sheet-independent)
- Li smoothing (changes the metric, bounded curvature on the smoothed complement)
- Distributional/test-field formulations (avoid differentiating $\mathrm{Ric}$)
- Closed-manifold topology: Pontryagin localization, monopole structure, Weitzenböck rotation

## 8. The Pontryagin obstruction to basic collapse

**Step 12 repaired statement.** On the calibrated bulk of a near-critical LeBrun sequence,

$$
\fint\left|{1\over4\pi^2}\left(2|W^+|^2+{s^2\over24}-{1\over2}|E|^2\right)-{3\over16\pi^2}\right|\to0.
$$

Thus $p_1(\Lambda^2_+)$ mass follows volume up to a global $o(A)$ error.  Basic $\Lambda^2_+$ collapse is still impossible on a positive-volume calibrated bulk, because a connection pulled back from a base of dimension at most three has zero Chern--Weil four-form.  But the mass should not be treated as hidden in tiny NUT residues: standard Taub--NUT--AdS has divergent mean curvature energy on core-containing fixed balls, while smaller annular domains unwrap and converge to hyperbolic space with macroscopic calibrated defect.  The live problem is diffuse non-basic mixed $\Lambda^2_+$ connection curvature, not a single F-per-NUT ratio.
