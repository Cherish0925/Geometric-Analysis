# TTCS Independent Branch Record

```json
{
  "step_id": 17,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step17_rigidity_Tk_identity_and_route_assessment.md",
    "Sessions/S0910A02/workspace/notes/step11_cz_spike_and_proposition_A.md",
    "Sessions/S0910A02/workspace/notes/step14_faberkrahn_reduced_system_and_fork.md",
    "Sessions/S0910A02/workspace/notes/step15_boundary_bubble_relaxation_and_edge_germ.md"
  ]
}
```

## Task

Yau Problem 26 asks: for each n≥2, do there exist dimension-only constants c_n < C_n such that any closed connected smooth n-manifold carrying a Riemannian metric g with c_n g ≤ Ric_g ≤ C_n g also admits some Einstein metric h? After 17 steps, the session has: (1) CZ spike showing C⁰ Ricci pinching does NOT control pointwise curvature; (2) T^k determinant identity: tr_h Ric^V = −Δ_B w/w, giving eigenvalue bound k(1−δ) ≤ λ₁^Dir ≤ k(1+δ); (3) Separated Einstein rigidity (SdS/Nariai: two S² bolts force A=0); (4) Conditional finite-cover amplifier (Proposition A); (5) Partial negative-branch smoothing architecture (localized Li bootstrap still open). THREE OPEN BRIDGES block every current route to the full proposition: Bridge 1 (general-to-invariant): no way to produce global T^k structure from C⁰ Ricci pinching after CZ killed regularity; Bridge 2 (polygon gap): multi-rod toric closure vs. edge-cone obstruction; Bridge 3 (finiteness-to-existence): finite diffeomorphism type does not yield Einstein metrics. The session needs either: (a) a mechanism to cross Bridge 1 without bounded sectional curvature; (b) a FUNDAMENTALLY DIFFERENT approach to Yau-26 that bypasses symmetry reduction entirely; (c) a counterexample strategy identifying closed manifolds without Einstein metrics that can carry Ric≈±g; or (d) new structural insight connecting Ricci pinching to Einstein existence without going through compactness/collapse. Generate genuinely different route ideas with their load-bearing assumptions and failure paths. Focus on mechanisms the session has not explored: Ricci flow approaches to existence (not just smoothing), min-max or variational methods for Einstein metrics, direct PDE existence from Ricci pinching, topological obstructions to Einstein metrics in higher dimensions, or connections to other areas of geometry.

## Output

## Framing this memo

I take the target as the full sign-unrestricted statement, and I lead with a structural reduction that, if the core agent adopts it, reorganizes the entire route map. Everything below is mechanism, not instruction; each possibility carries its load-bearing assumption and where it can break.

---

## 1. The scaling reduction: the working band must be sign-definite

The single most consequential fact about this problem, and one the notes never state, is that **the prover's choice of $[c_n,C_n]$ is not free — a band straddling zero is instantly defeated, for elementary reasons.**

Let $(M,g_0)$ be any closed $n$-manifold with any metric. The Ricci tensor is scale-invariant: $\operatorname{Ric}_{sg_0}=\operatorname{Ric}_{g_0}$ as a $(0,2)$-tensor. On compact $M$ the eigenvalues of $\operatorname{Ric}_{g_0}$ relative to $g_0$ lie in some finite window $[-\Lambda,\Lambda]$. For $g=sg_0$ the pinching condition becomes $c_n s\le \mu_i(x)\le C_n s$ for all Ricci eigenvalues $\mu_i$. If $c_n<0<C_n$, choose $s\ge \Lambda\max(1/C_n,\,1/|c_n|)$; then the upper request $\mu_i\le C_n s$ and the lower request $\mu_i\ge c_n s$ both hold. **Hence a straddling band is satisfied by every closed $n$-manifold with a suitably rescaled copy of any metric.** Yau-26 with such a band would force every closed $n$-manifold to be Einstein-admitting, which is false for $n\ge4$: $\#_5\mathbb{CP}^2$ has $\chi=7$, $\tau=5$, so $\chi=7<\tfrac32|\tau|=7.5$ violates Hitchin–Thorpe and carries no Einstein metric.

The identical computation shows the sign-definite bands are the genuine ones. For $[c_n,C_n]\subset(0,\infty)$ the class is "admits $\operatorname{Ric}>0$ pinched within ratio $C_n/c_n$"; for $[c_n,C_n]\subset(-\infty,0)$ it is "admits $\operatorname{Ric}\prec0$ within ratio $c_n/C_n$"; the degenerate ends give $\operatorname{Ric}\ge0$ or $\operatorname{Ric}\le0$.

**Consequence for the whole program.** Yau-26 is TRUE iff *some* sign-definite band works, and it is most plausibly the positive one (Myers forces $\pi_1$ finite, positive scalar excludes $\hat A\ne0$ spin manifolds, etc., so the positive-pinched class is rigid). Yau-26 is FALSE iff *every* sign-definite band fails. This means the session's concentration on $\operatorname{Ric}\approx g$ was the right instinct, but it should be *justified* by the reduction above, and — decisively — the refutation direction has a second, largely unexplored lever in the sub-zero band (Section 3). This reduction costs nothing to prove and it eliminates a large family of would-be routes.

---

## 2. Schur reformulation: Yau-26 as a gap-plus-attainability theorem for the pinching functional

Define, for the positive branch, $\rho(M)=\inf\{\sup_x \lambda_{\max}(\operatorname{Ric}_g)/\lambda_{\min}(\operatorname{Ric}_g): \operatorname{Ric}_g>0\}$. Schur's lemma ($n\ge3$: pointwise $\operatorname{Ric}=\phi(x)g$ forces $\phi$ constant, since the contracted second Bianchi identity gives $(1-\tfrac n2)d\phi=0$) says that **an attained value $\rho(M)=1$ is exactly the existence of an Einstein metric.** So the positive branch of Yau-26 is precisely:

> There is $\rho_n>1$ with no manifold in the band $1<\rho(M)<\rho_n$ *and* attainment of the infimum at value $1$ whenever $\rho(M)=1$.

This isolates the true enemy: a manifold whose pinching functional has infimum $1$ (or just below $\rho_n$) that is **not attained** — a sequence $g_j$ with pinching ratio $\to1$ degenerating so that no Einstein limit survives on $M$. That is an Anderson-type bubbling/attainability question, not a symmetry question.

One sharp technical point that clarifies why the session's $\|\operatorname{Ric}-g\|_{op}\le\delta$ model is faithful. The *ratio* $\to1$ is strictly weaker than the *absolute* band: writing $\operatorname{Ric}=\phi g+E$ with $|E|_{op}=o(1)$, the same Bianchi computation gives $d\phi=\tfrac{2}{n-2}(\operatorname{div}E-\tfrac12 d\,\mathrm{tr}E)$, which involves **first derivatives of $E$** — uncontrolled under $C^0$ pinching (this is the CZ spike again). So ratio-pinching alone does not make $\phi$ nearly constant and does not make the metric $C^0$-close to any single Einstein value. But the *absolute* band $[c_n,C_n]$ pins every eigenvalue into a fixed window, so after normalizing the window center to $1$ it genuinely gives $\|\operatorname{Ric}-g\|_{op}\le\delta$ with $\delta=(C_n-c_n)/2$, and this $\delta$ is **not** removable by rescaling. The session's formulation is therefore correct; the useful refinement is that $C^0$ Einstein-defect $\delta$ is available, but no derivative of the defect is.

---

## 3. The sub-zero branch: Lohkamp / Gromov–Thurston flexibility as the sharpest refutation lever

This is the most underexplored high-value direction, and it exploits a genuine **asymmetry between the plus and minus branches.**

On the plus side, tight *sectional* pinching triggers the differentiable sphere theorem (Brendle–Schoen): $1/4$-pinched positive sectional curvature forces a space form, which is Einstein. So a plus-branch counterexample cannot come from tight sectional pinching; it must live in the Ricci-pinched-but-not-sectional-pinched regime the CZ spike opened. This is exactly why the plus branch is hard to refute.

On the minus side, there is **no analogue of the sphere theorem** — Gromov–Thurston produced closed manifolds in dimension $\ge4$ with sectional curvature confined to $[-1-\epsilon,-1+\epsilon]$ (hence Ricci pinched within ratio $\to1$ around a fixed sub-zero value) that carry **no metric of constant curvature.** These are ramified covers of hyperbolic manifolds. The load-bearing question that would refute *every* sub-zero band is:

> Do Gromov–Thurston manifolds (or Lohkamp-type $\operatorname{Ric}\prec0$ constructions with controlled pinching ratio) admit **no Einstein metric of any sign**?

If a Gromov–Thurston manifold in a fixed dimension admits no Einstein metric, then it lies in the sub-zero pinched class for a band as tight as one likes yet is not Einstein-admitting, killing all sub-zero bands. The distinguishing computation is an Einstein-obstruction on these manifolds. In dimension $4$ the tool is LeBrun's Seiberg–Witten curvature inequalities (the $c_1^2$-refined Hitchin–Thorpe), which can obstruct Einstein metrics on manifolds admitting near-hyperbolic pinching; whether a specific Gromov–Thurston $4$-manifold triggers it is a concrete, decidable calculation from its $\chi$, $\tau$, and basic classes. A complementary softer route is Lohkamp's h-principle for $\operatorname{Ric}\prec0$: if his flexibility can realize a *dimension-only bounded* pinching ratio on *every* closed $n$-manifold ($n\ge3$), then the sub-zero band is satisfied universally and every non-Einstein manifold refutes it directly. The open point is precisely whether Lohkamp's constructions keep the ratio bounded independent of topology, or whether the ratio must blow up with complexity — a question worth extracting from the sources (Lohkamp, *Metrics of negative Ricci curvature*, Ann. Math. 140 (1994); his curvature h-principle papers).

Why this matters strategically: even a full success here refutes only the sub-zero and straddling bands, so it does **not by itself** refute Yau-26 (the plus band could still work, which would make the theorem true). But it collapses the problem to a clean dichotomy — **Yau-26 stands or falls entirely on the plus band** — and it tells the refutation project exactly where its remaining work is (defeat the plus band too). It also tells the *proof* project that the minus band is a dead end and no effort should go there.

---

## 4. Dimension 4: a symmetry-free Bridge-1 bypass via $L^2$-curvature orbifold compactness

Bridge 1 (produce global symmetry from $C^0$ Ricci pinching) may be unnecessary in dimension $4$, because the correct compactness engine there needs only $L^2$ curvature, volume noncollapse, and a $C^0$ Ricci bound — all symmetry-free.

For a $\delta$-pinched closed $4$-manifold, Chern–Gauss–Bonnet gives $\int_M(|W|^2+\tfrac{s^2}{24}-\tfrac12|\mathring{\operatorname{Ric}}|^2)=8\pi^2\chi$, and the pinching bounds $s$ and $\mathring{\operatorname{Ric}}$ pointwise, so $\int|W|^2$ — hence $\int|Rm|^2$ — is bounded by $8\pi^2\chi+C\mathrm{Vol}$. With volume noncollapse (the session's volume-gap target) and $\|\operatorname{Ric}-g\|_{C^0}\le\delta$, the Anderson / Bando–Kasue–Nakajima orbifold-compactness picture applies: a $\delta_j\to0$ sequence subconverges in Gromov–Hausdorff to an Einstein orbifold $X_\infty$ ($\operatorname{Ric}=g$) with finitely many points where Ricci-flat ALE spaces bubble off, and $M$ is a resolution of $X_\infty$.

The attainability question of Section 2 becomes concrete and derivative-free: **if no bubbles form, $X_\infty$ is a smooth Einstein manifold diffeomorphic to $M$, so $M$ is Einstein-admitting and Yau-26's positive band holds in dimension 4.** If bubbles form, $M$ is a Biquard–Ozuch-style desingularization of $X_\infty$, and Bridge 3 reappears as the desingularization-Einstein question — but now sitting on a *general* $4$-manifold rather than a toric one, with the invariant edge-cone work of Steps 14–15 as the model calculation rather than the whole story. The load-bearing input is exactly the noncollapse (volume gap) that the session already targets, plus $\epsilon$-regularity in the $L^2$-curvature/$C^0$-Ricci setting, which the CZ spike does not obstruct (it only forbids $L^\infty$ curvature control, and orbifold compactness needs $L^2$). This is a cleaner statement of what the session's positive branch is really trying to do, and it removes the need to manufacture a global torus.

The remaining break path: verifying that $C^0$ Ricci defect $\delta$ (not $L^{n/2}$ Einstein defect $\to0$) is enough for the $\epsilon$-regularity used by Anderson/BKN. Since $\|\operatorname{Ric}-g\|_{C^0}\le\delta$ is *stronger* than $L^2$ Einstein defect small, this is favorable; the point to nail down is the harmonic-radius lower bound under $C^0$ Ricci pinching alone, which Naber–Zhang-type estimates should supply once noncollapse is in hand.

---

## 5. Variational route via the $\sigma$-invariant, and why the two branches split

Einstein metrics are critical points of the normalized total scalar curvature; the sign of $\lambda$ controls whether they are minimizers or saddles, and this dictates whether a variational existence argument can succeed.

For the **minus branch**, if $\sigma(M)<0$ (Schoen–Yamabe invariant / $\sigma$-constant), an Einstein metric with $\lambda<0$ is a *minimizer* realizing $\sigma(M)$; existence and near-uniqueness become genuine variational statements (Anderson, LeBrun). Pinching $\operatorname{Ric}\prec0$ forces $s<0$ hence $\sigma(M)\le0$, placing us in this regime. Existence of a metric attaining $\sigma(M)<0$ that is smoothly Einstein is not automatic in $n\ge5$, and Besson–Courtois–Gallot entropy rigidity gives it only near the hyperbolic/locally-symmetric locus — which is exactly where Gromov–Thurston says the pinched class is *larger* than the Einstein-admitting one. So the variational picture predicts the sub-zero band should fail, coherent with Section 3.

For the **plus branch**, positive Ricci pinching gives $s>0$, so $\sigma(M)>0$ (admits positive scalar). But positive Einstein metrics do **not** realize $\sigma(M)$ — they are saddle points (unstable in the conformal direction, min in the transverse). A direct min-max would have to be a mountain-pass over the transverse-traceless directions of Perelman's $\nu$-entropy (positive Einstein = shrinking soliton = critical point of $\nu$). This explains, at the level of mechanism, why the plus branch resists variational treatment while the minus branch does not, and it points to the $\nu$-functional (not the Einstein–Hilbert functional) as the correct object if a variational plus-branch existence is attempted. The load-bearing difficulty is Palais–Smale compactness for $\nu$ under $C^0$ Ricci pinching, which is again the bubbling/attainability wall of Sections 2 and 4.

---

## 6. Ricci flow to existence via dynamical stability, not preservation of pinching

The notes treat Ricci flow only as a smoother. A genuinely different use is **flow-to-a-fixed-point via stability of Einstein metrics.**

Pinching cones are *not* preserved under Ricci flow in $n\ge4$ (Weyl can grow — the same phenomenon as the CZ spike), so a Böhm–Wilking / Brendle–Schoen "preserve the cone, converge to a space form" argument does not transfer to Ricci pinching. But there is a different mechanism: normalized Ricci–DeTurck flow has Einstein metrics as fixed points, and dynamically stable Einstein metrics attract a $C^\infty$-neighborhood (Kröncke, Sesum, Haslhofer–Müller). The chain would be: (i) run the flow from the $\delta$-pinched $g$ for a short time to gain curvature bounds — the flow smooths instantly, converting $C^0$ Ricci control into $C^k$ control at time $t>0$, at the cost of some pinching degradation; (ii) show the smoothed metric lands in the stability basin of an actual Einstein metric; (iii) let the flow converge to it.

Load-bearing pieces and where they break: step (i) is the session's smoothing estimate — the open question is bounding how much pinching degrades in the smoothing time (the localized Li bootstrap), and this is genuinely delicate because the CZ spike shows curvature can be large before smoothing. Step (ii) is circular unless a nearby Einstein metric is produced first (so this route is most powerful *after* Section 4 supplies an Einstein orbifold limit, whose smooth locus one flows toward). The value of the reframing is that it converts "existence" from a compactness/gluing problem into a **dynamical stability** problem: instead of asking whether the limit is Einstein, ask whether the smoothed pinched metric is inside a stability basin, which is a spectral condition (positivity of the Einstein operator / linear stability) that can be studied on model bubbles independently.

---

## 7. Prescribed-Ricci fixed points and Ricci iteration as a fresh PDE existence engine

A direct PDE mechanism the session has not touched: the map $g\mapsto \mathcal{R}(g)$ defined by solving $\operatorname{Ric}_{\mathcal{R}(g)}=g$ (Rubinstein's Ricci iteration; well-posed via DeTurck's local solvability of prescribed Ricci, with global solvability the hard input). Einstein metrics are exactly its fixed points. The pinching hypothesis says $g$ is a near-fixed-point: $\operatorname{Ric}_g=g+E$, $|E|\le\delta$. The question is whether the iteration (or a Newton/implicit-function step around it) contracts to a genuine fixed point.

Load-bearing: (a) global solvability of $\operatorname{Ric}_h=T$ for the positive-definite tensors $T$ arising along the iteration — this is subtle and can break (prescribed Ricci is not globally solvable in general; DeLellis–Kadanoff-type constraints and the underdetermined-elliptic nature of $\operatorname{Ric}$ modulo diffeomorphism matter), and (b) invertibility of the linearized operator $D\operatorname{Ric}$ modulo gauge, which is exactly the linear stability spectrum of Section 6. The attractive feature is that this is a self-contained analytic route to *existence* that never passes through compactness or symmetry, so it engages Bridge 3 head-on. The natural place to test it cheaply is on the near-Einstein model where $E$ is a small transverse-traceless perturbation of a known Einstein metric, computing whether the linearized prescribed-Ricci operator is invertible there — a spectral calculation that also feeds Sections 5 and 6.

---

## 8. Where a counterexample is and is not feasible, and what to consult

Refuting the plus band requires, for every ratio $\rho$, a $\rho$-pinched positive-Ricci manifold with no Einstein metric. In $n\ge5$ the obstruction desert (only positive-scalar obstructions like $\hat A$, enlargeability, minimal-hypersurface) makes *certifying* Einstein-nonexistence extremely hard, so a high-dimensional plus-branch counterexample is unlikely to be provable even if it exists. In dimension $4$ the Hitchin–Thorpe / LeBrun–Seiberg–Witten obstructions are the only realistic certifiers, but positive-Ricci pinched-within-fixed-ratio is far more restrictive than psc, and it is open whether e.g. $\#_k(S^2\times S^2)$ (which satisfy Hitchin–Thorpe and are candidate Sha–Yang positive-Ricci manifolds) carry Einstein metrics for $k\ge2$. So the plus-branch refutation hinges on two things worth pinning down from the literature: whether Sha–Yang / Wraith positive-Ricci constructions on infinite families ($\#_k(S^2\times S^2)$, $\#_k(S^p\times S^q)$) have a $k$-uniform pinching ratio, and whether any such family has a member with a provable Einstein obstruction. If a family is uniformly pinched but Einstein-existence is open, the plus band is neither confirmed nor refuted — which is the true state of the problem and the reason Bridge 3 is load-bearing.

Sources whose exact content would move the judgment: Lohkamp's negative-Ricci flexibility and any pinching-ratio control therein; Gromov–Thurston branched-cover manifolds and any Einstein (non)existence results on them; Anderson and Bando–Kasue–Nakajima $L^2$-curvature orbifold compactness in dimension $4$ (for Section 4); LeBrun's Seiberg–Witten Einstein obstructions; Sha–Yang and Wraith positive-Ricci connected-sum constructions with attention to pinching ratios; Kröncke / Sesum linear and dynamical stability of Einstein metrics under Ricci flow (for Sections 6–7); Rubinstein's Ricci iteration and DeTurck's prescribed-Ricci solvability.

---

## 9. The few computations that would most change the picture

Three low-cost calculations would each redirect judgment. First, write out and verify the scaling-plus-Schur reduction of Section 1–2 as formal statements; this alone reorganizes the route map and rules out straddling and ratio-only formulations. Second, compute the Seiberg–Witten / Hitchin–Thorpe Einstein-obstruction numbers ($\chi$, $\tau$, and $c_1^2$-type quantities) for a specific low-dimensional Gromov–Thurston manifold, to see whether the sub-zero band is refutable outright (Section 3). Third, compute the linearized prescribed-Ricci / Einstein-operator spectrum on a transverse-traceless perturbation of a model Einstein metric and on the Ricci-flat ALE bubble models, which simultaneously tests the Ricci-iteration contraction (Section 7), the Ricci-flow stability basin (Section 6), and the desingularization obstruction (Section 4). These three sit at the intersection of the routes above and would tell the core agent which branch and which existence engine is actually load-bearing.