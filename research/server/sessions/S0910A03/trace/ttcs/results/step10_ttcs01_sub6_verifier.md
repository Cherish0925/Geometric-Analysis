# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/scripts/verify_taub_nut_ads.py",
    "Sessions/S0910A03/workspace/scripts/compute_taub_nut_ads_curvature.py",
    "Sessions/S0910A03/workspace/scripts/analyze_taub_nut_ads_multiscale.py",
    "Sessions/S0910A03/staging/acquired/gr-qc_0202073__Classical_Boundary-value_Problem_in_Riemannian_Q_b30651e52bda5fb0/content.md",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Check and correct the Step-10 reassessment of Taub–NUT–AdS and scaling. Independently verify from the metric and the supplied symbolic scripts: (i) the exact |W|^2 formula, its value near the NUT, cumulative Weyl energy and all-radius curvature-mean behavior; (ii) whether a smaller fixed buffered domain around a point at distance 1/2 unwraps the short circle for all small nu; (iii) the locally unwrapped annular limit and its calibrated deficit; (iv) the correct homothetic scaling of Ricci endomorphism, Weyl endomorphism spectrum, |W|, and the forbidden calibrated Einstein germ. Decide precisely what Taub–NUT–AdS refutes and what it does not. Also flag orientation/factor-of-four convention issues between full Weyl and W+ before conclusions are used.

## Output

## Verifier memo: Taub–NUT–AdS as a collapse model, and the scaling of the calibrated germ

I reconstructed the metric, its invariants, the covering/unwrapping picture, and the homothety behavior independently from the supplied metric and cross-checked against Akbar–D'Eath (gr-qc/0202073). Summary first, then the pieces.

**Bottom line.** The exact-Einstein and Weyl computations are essentially correct, and the model does establish one thing cleanly: controlled normalized $\int|\mathrm{Rm}|^2$ together with $\mathrm{Ric}\ge -3g$ does not by itself produce volume noncollapse. But two structural statements in `step9_regularity_false_and_new_direction.tex` are stated too broadly and are corrected below: (a) a small domain around $p_\nu$ (radius $<1/2$) **does** unwrap the short Hopf circle and its local universal cover **is** noncollapsed; (b) the unwrapped noncollapsed limit is hyperbolic $H^4$ with $W^+\to 0$, so the model evades the calibrated-germ contradiction not by staying collapsed but by having calibrated deficit $\to 16$, not $\to 0$. There is also a factor‑2 error in the volume element and a factor‑4 conflation between the full Weyl tensor norm and the $W^+$ endomorphism norm.

---

### 0. Parameter dictionary and $\mathrm{Ric}=-g$

With $\rho=r$, $L=\nu$, and Akbar–D'Eath's $\Delta=(\rho-L)^2+\tfrac13\lambda(\rho+3L)(\rho-L)^3$, one has exactly
$$F_\nu=\frac{\Delta}{r^2-\nu^2}=\frac{r-\nu}{r+\nu}\Big(1+\tfrac{\lambda}{3}(r-\nu)(r+3\nu)\Big),$$
so $\ell^2=3\Leftrightarrow\lambda=1\Leftrightarrow\Lambda=-1$, giving $\mathrm{Ric}_{g_\nu}=\Lambda g=-g_\nu$. The symbolic script's `Ric+g` check confirms this. The self-dual (half-flat Weyl) condition is $M=\nu(1+\tfrac43\Lambda\nu^2)=\nu(1-\tfrac43\nu^2)$.

---

### 1. Exact $|W|^2$, NUT value, cumulative Weyl energy, all-radius mean

The script's invariant is the tensor norm $W_{abcd}W^{abcd}=\mathrm{Kretsch}-\tfrac83$ (correct for an Einstein 4-metric with $s=-4$, since $|\mathrm{Rm}|^2=|W|^2+2|\mathring{\mathrm{Ric}}|^2+\tfrac16 s^2$ and $\tfrac16\cdot16=\tfrac83$). I confirm
$$|W|^2_{\text{tensor}}=\frac{32\,\nu^2(4\nu^2-3)^2}{3\,(r+\nu)^6}.$$
Three independent internal checks pass:
- $\nu\to 0$ at fixed $r$: $|W|^2\sim 96\nu^2/r^6\to 0$ (the $H^4$ limit is conformally flat). **In the annular band $r\in[\nu+\tfrac16,\nu+\tfrac56]$ the Weyl part does not merely stay bounded — it vanishes**, so $|\mathrm{Rm}|^2\to \tfrac83$. The note's "curvature bounded uniformly in $\nu$" is true and in fact sharpenable.
- NUT value $r=\nu$: $|W|^2=(4\nu^2-3)^2/(6\nu^4)\sim \tfrac{3}{2}\nu^{-4}$ — a genuine $\nu^{-4}$ concentration at the NUT.
- $|W|^2\propto(4\nu^2-3)^2$ vanishes identically at $\nu^2=3/4$, which is exactly where $M=\nu(1-\tfrac43\nu^2)=0$; the metric is then conformally flat. Weyl $\leftrightarrow$ mass vanishing together is a strong correctness signal for the overall constant.

**Volume element (factor‑2 correction).** $\det g=4\nu^2(r^2-\nu^2)^2\sin^2\theta$, so $\sqrt{\det g}=2\nu(r^2-\nu^2)\sin\theta$; with $\int\sin\theta\,d\theta=2$, $\phi\in[0,2\pi)$, $\psi\in[0,4\pi)$ the angular factor is $16\pi^2$ and
$$\frac{dV}{dr}=32\pi^2\,\nu(r^2-\nu^2).$$
Integrating gives $\tfrac{32}{3}\pi^2\nu(\rho-\nu)^2(\rho+2\nu)$, **matching Akbar–D'Eath's closed-form volume exactly**. The scripts `compute_taub_nut_ads_curvature.py` and `analyze_taub_nut_ads_multiscale.py` use `64*pi**2*nu*(r**2-nu**2)` — twice the correct density.

**Cumulative Weyl energy.** With the correct measure,
$$\int_\nu^\infty |W|^2\,dV=\frac{32\pi^2(4\nu^2-3)^2}{9}\xrightarrow{\nu\to0}32\pi^2\ \ (\text{finite}).$$
So the Weyl energy is finite; what diverges is $\int|\mathrm{Rm}|^2=\int|W|^2+\tfrac83\,\mathrm{Vol}$, driven by the $\mathrm{Vol}\to\infty$ growth of the Einstein background as $r\to\infty$. The note's phrase "total curvature energy of Taub–NUT–AdS is infinite" is correct for $|\mathrm{Rm}|^2$ but should not be read as Weyl-energy divergence. The script's reported Weyl-energy-to-infinity is $64\pi^2$; the correct tensor value is $32\pi^2$.

**All-radius mean.** The factor‑2 cancels in every mean $\fint|W|^2$ = energy/volume, so the multiscale statements are qualitatively right: near-NUT ($r=\nu x$, $x=O(1)$) mean $\sim\nu^{-4}$; fixed physical radius mean $\sim\nu^{-1}$; the "critical magnitude" transition sits at a thin shell $r\sim\nu^{1/3}$, not a fixed-scale bulk. Only the leading constant of that shell is affected — see §2.

---

### 2. Full Weyl vs $W^+$ endomorphism: the factor‑4

step6/step9 use $|W^+|^2:=\sum_i w_i^2$ (endomorphism norm on $\Lambda^+$): the calibrated spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$ gives $|W^+|^2=\tfrac1{24}$, and $s=-8\sqrt6\,|W^+|$ reproduces $s=-4$. The script's $|W|^2$ is the tensor norm. Writing $W^+$ in an orthonormal eigenbasis of $\Lambda^+$ (with $\langle\alpha,\beta\rangle=\tfrac12\alpha_{ab}\beta^{ab}$, $|e_i|_{\text{comp}}^2=2$):
$$W^+_{abcd}W^{+abcd}=4\sum_i w_i^2=4\,|W^+|^2_{\text{end}}\quad\Rightarrow\quad |W|^2_{\text{tensor}}=4\big(|W^+|^2_{\text{end}}+|W^-|^2_{\text{end}}\big).$$
Since Taub–NUT–AdS is self-dual ($W^-=0$), $|W^+|^2_{\text{end}}=\tfrac14|W|^2_{\text{tensor}}$.

Consequences to flag before any conclusion uses these numbers:
- The calibrated germ has $|W^+|^2_{\text{end}}=\tfrac1{24}$, i.e. tensor value $W_{abcd}W^{abcd}=\tfrac16$, **not** $\tfrac1{24}$.
- The multiscale script solves `W2 = 1/24` for the "critical magnitude $1/(2\sqrt6)$", treating the tensor $W2$ as if it were $|W^+|^2_{\text{end}}$. The correct target is $W2=\tfrac16$, shifting the transition constant from $(2304)^{1/6}\nu^{1/3}$ to $(576)^{1/6}\nu^{1/3}$ (smaller by $4^{1/6}\approx1.26$). The $\nu^{1/3}$ scaling is unaffected.
- The annular conclusion in §3 is robust to this convention because $|W^+|\to 0$ regardless of normalization; the factor only matters where one compares a nonzero $|W^+|$ to the calibrated value.
- If Weyl energy is ever compared to a topological integral $\int|W^+|^2$, note that the script's tensor energy is off from the endomorphism-normalized topological quantity by $2\times4=8$ (factor‑2 volume $\times$ factor‑4 norm).

---

### 3. Does a smaller buffered domain unwrap the short circle? (Correction)

This is the point where `step9_regularity_false` needs revision. The note's null-homotopy argument (sweep the $\psi$-circle radially into the NUT at distance $1/2$) is valid **only for a domain that reaches the NUT**, i.e. radius $\gtrsim 1/2$. For such a ball $B_1(p_\nu)$: the region $\{r\in[\nu,r_{\max}]\}$ is a topological 4-ball capped smoothly at the NUT, hence simply connected, its own local universal cover, and collapsed ($\mathrm{Vol}=O(\nu)$). That much is correct.

But at the scales that the regularity question actually invokes ($r\le \tfrac13$), the relevant domain $B_s(p_\nu)$ with $s<1/2$ **does not contain the NUT** and does not span the $S^2$ base (which has radius $\approx r\approx1/2$, diameter $\approx\pi/2$). Over such a small base patch the Hopf bundle is trivial, the $\psi$-fiber is **essential**, and the local universal cover unwraps it: $\widetilde{B_s(p_\nu)}\approx D^3_s\times\mathbb{R}_\psi$. Because the unwrapped fiber is now a genuine line of unbounded proper length (moving proper distance $s$ needs $\Delta\psi\sim s/(2\nu\sqrt F)\to\infty$, allowed on $\mathbb{R}$), a ball $B_{r_*}(\tilde p_\nu)$ in the cover has proper extent $r_*$ in all four directions and $\mathrm{Vol}\ge c\,r_*^4$: **the cover is noncollapsed.** This is exactly the flat-torus phenomenon ($\mathbb{R}^2/(\mathbb{Z}\oplus\varepsilon\mathbb{Z})$ collapses; $\mathbb{R}^2$ does not), not the Berger-sphere phenomenon (where the fiber is contractible in $S^3$ and cannot be undone).

So the "fibered rank $=0$" and "cover still collapsed" statements are **scale-dependent**: rank $0$ (contractible fiber, collapsed cover) holds only for $s\gtrsim1/2$; for $s<1/2$ the fiber has rank $1$, Naber–Zhang-type unwrapping applies, and the cover is noncollapsed. The clean dichotomy is at $s\approx1/2$. The model therefore does **not** refute the unwrap-to-noncollapse step of the strategy.

---

### 4. The unwrapped annular limit and its calibrated deficit

Take $s<1/2$ fixed and $\nu\to0$. In the annulus $|W|^2\to0$, and the pointed cover converges to a ball in real hyperbolic space $H^4$ scaled to $\mathrm{Ric}=-g$ (sectional curvature $-\tfrac13$; this is precisely Akbar–D'Eath's $L\to0$ limit). Thus the noncollapsed unwrapped limit is Einstein with $s=-4$, $W^+=0$, and
$$\big(s+8\sqrt6\,|W^+|\big)^2\longrightarrow(-4+0)^2=16.$$
The multiscale script's "annular completed-square defect limit $=16$" is correct. This is the decisive fact: the model reaches a noncollapsed harmonic chart, but the limit is conformally flat, so it is **not** the forbidden calibrated germ, and the step6 projector obstruction is never triggered. What saves the theorem here is that the calibrated deficit does not vanish, not that the cover stays collapsed.

---

### 5. Homothetic scaling of the endomorphisms and the germ

Under $\tilde g=c^2g$ (take $c=1/r$, $c^{-2}=r^2$):
- $\mathrm{Ric}$ as a $(0,2)$-tensor is invariant; the Ricci **endomorphism** eigenvalues scale by $c^{-2}=r^2$, so an Einstein constant $\lambda=-1$ becomes $\tilde\lambda=-r^2$.
- $s\to r^2 s=-4r^2$; $|W^+|_{\text{end}}\to r^2|W^+|$; $W_{abcd}W^{abcd}\to r^4(\cdots)$.
- The literal eigenvalue triple $(-\tfrac16,\tfrac1{12},\tfrac1{12})$ therefore does **not** stay fixed under homothety; it scales by $r^2$. What is scale-invariant is (i) the **shape** (ratios) of the $W^+$ spectrum and (ii) the calibration relation $s+8\sqrt6|W^+|=0$, since both sides carry the same weight. The note's phrase "$W^+$ is conformally invariant … the spectrum is unchanged" should be read as invariance of the spectral shape / calibration ratio, not of the numerical eigenvalues.
- The step6 obstruction is scale-covariant: $|\nabla W^+|^2$ scales as $c^{-6}=r^6$ on both sides of the Weitzenböck scalar identity, while $\nabla W^+=0$ is scale-invariant. Hence the contradiction (constant calibrated spectrum $\Rightarrow \nabla W^+=0$, versus $|\nabla W^+|^2\ne0$) persists for every fixed $r>0$ and degenerates only as $r\to0$ (Einstein constant $\to0$). The note's conclusion "only $r\to0$ kills the contradiction" is correct; only its justification wording needs the amendment above.

Taub–NUT–AdS is consistent with all of this: its noncollapsed small-ball limit is $H^4$ with deficit $16\ne0$, so it never enters the calibrated germ at any scale.

---

### 6. What the model settles and what it does not

Refutes:
- The pure implication "$\fint_{B_r}|\mathrm{Rm}|^2\le K$ for all $r\le\tfrac13$ plus $\mathrm{Ric}\ge-3g$ $\Rightarrow$ noncollapse at a fixed scale." A ball around $p_\nu$ has $\mathrm{Ric}=-g$, $|\mathrm{Rm}|^2\to\tfrac83$ in the annulus, yet $\mathrm{Vol}(B_{r_*}(p_\nu))=O(\nu)\to0$. Curvature-energy control alone does not prevent collapse.

Does not settle / does not refute:
- It does not exhibit collapse carrying the near-saturation input: its collapsing regions have calibrated deficit $\to16$, the opposite of $F_i\to0$. The closed-manifold reduction crucially transports $F_i\to0$ to the cover; the model supplies no analogue.
- It does not refute the unwrap-to-noncollapse step (§3) nor Naber–Zhang: at scales below the NUT distance the cover is noncollapsed.
- It is noncompact, has no Seiberg–Witten monopole classes, and $\int|\mathrm{Rm}|^2=\infty$ (volume-driven), so none of the topological energy accounting of the Ishida–LeBrun setting applies.

Precise reading for the strategy: the model demonstrates that noncollapse cannot be extracted from curvature energy alone; the small deficit $F_i\to0$ and its transport to the cover are the essential extra ingredient that must force either noncollapse-with-calibrated-germ (contradiction) or a deficit-carrying collapse. The model is a sharp demonstration that the deficit input is indispensable, not an obstacle to the overall program.

---

### 7. Concrete corrections to fold into the notes

1. Volume density $32\pi^2\nu(r^2-\nu^2)$, not $64\pi^2$ (verified against Akbar–D'Eath volume). Correct Weyl-energy-to-infinity is $32\pi^2$, not $64\pi^2$.
2. State $W_{abcd}W^{abcd}=4|W^+|^2_{\text{end}}$; the calibrated tensor value is $\tfrac16$, and the "critical shell" target should be $W2=\tfrac16$ (constant $(576)^{1/6}\nu^{1/3}$), not $W2=\tfrac1{24}$.
3. Replace "the local universal cover does not unwrap … cover still collapsed / fibered rank 0" with the scale dichotomy at $s\approx1/2$: for $s<1/2$ the fiber is essential, the cover unwraps and is noncollapsed with limit $H^4$; for $s\gtrsim1/2$ the fiber is contractible and the ball is its own collapsed cover.
4. Record that the reason the model is harmless to the closed-manifold argument is calibrated deficit $\to16$ (equivalently $|W^+|\to0$, conformally flat limit), not persistent collapse.
5. In the scaling discussion, state homothety-covariance of the calibration relation and spectral shape rather than invariance of the literal eigenvalues.

One item I did not independently recompute symbolically: the overall numerical constant $32/3$ in $|W|^2$. Its three consistency checks (vanishing as $\nu\to0$, $\nu^{-4}$ at the NUT, and simultaneous vanishing of $|W|^2$ and $M$ at $\nu^2=3/4$) all pass, and the volume normalization is pinned against the published formula, so I regard the formula as reliable; a full re-run of the Kretschmann contraction would remove the last residual uncertainty.