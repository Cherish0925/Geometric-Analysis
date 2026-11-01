# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step10_execute_pivot_volume_gap_and_epsilon_regularization.md",
    "Sessions/S0910A02/workspace/plans/step8_projection_bridge_target.md",
    "Sessions/S0910A02/workspace/notes/step8_preceptor_review_positive_branch.md",
    "Knowledge/objects/papers/1707.05511-ε-regularity-for-shrinking-Ricci-solitons-and-Ricci-flows--77d745e7dfc7--9e2e179bf3bc/object.md",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step10.md",
    "Sessions/S0910A03/workspace/notes/step8_cover_mean_transport_and_model_scope_corrections.md"
  ]
}
```

## Task

Given the Step 10 pivot, propose concrete Execute-level mathematical attacks on the true pinched regularity bottleneck for Yau Problem 26. The goal is not final writing but actionable research: how to refute or salvage a Cheeger--Tian-style pointwise epsilon-regularity theorem under only ||Ric-g||_{L∞}≤δ; how to use high-frequency transverse-traceless/Weyl packet perturbations as counterexample probes; how to extract a weaker Li/Cheeger--Tian scale-selection or smoothing theorem; and how to connect any surviving regularity to the simply-connected volume gap and the A01/A03 accessible-cover bridge. Give a prioritized set of candidate lemmas/probes with assumptions, expected calculations, failure modes, and what evidence would change the route.

## Output

## Orientation: what the pinching actually locks together

Before proposing probes, one computation reorganizes the whole question and should be done first because it is cheap and decisive.

**The defect and the Weyl energy are locked at fixed scale.** Take a positive Einstein background $(M^4,g_0)$, $\operatorname{Ric}(g_0)=g_0$ (round $S^4$ is enough), and perturb $g=g_0+h$ with $h$ transverse-traceless. Then

$$
\operatorname{Ric}(g)-g \;=\; \tfrac12\Delta_L h - h + Q(h),\qquad
D\!\operatorname{Rm}(h)\sim \nabla^2 h .
$$

For a packet of spatial frequency $k$ and amplitude $\epsilon A$, $\Delta_L h=\nabla^*\nabla h+(\text{bounded})\sim k^2 h$, so

$$
\|\operatorname{Ric}(g)-g\|_{L^\infty}\sim \bigl(\tfrac12 k^2-1\bigr)\epsilon A,\qquad
\|W(g)-W(g_0)\|_{L^\infty}\sim k^2\epsilon A .
$$

Both scale as $k^2\epsilon A$. To hold $\|\operatorname{Ric}-g\|_{L^\infty}\le\delta$ one is forced to $\epsilon A\lesssim \delta/k^2$, and then the Weyl perturbation is $\lesssim\delta$ as well. High frequency on a *fixed noncollapsed background cannot decouple large Weyl from a large Ricci defect.* The only tunable exception is $h$ landing in the infinitesimal-Einstein eigenspace $\tfrac12\Delta_L h=h$, a fixed finite-dimensional space with no high-frequency members.

The immediate consequence: **any $C^0$-Ricci-pinched metric with large local $|W|$ and small local curvature energy must degenerate the background itself** — i.e. concentrate/collapse so that the effective reference scale $t_i\to0$. This is why the whole regularity question is a collapse question, and it tells you exactly where to spend effort. It also tells you the naive Weyl-packet refutation of pointwise regularity will not work; I record it below as a probe precisely because a clean null result here removes a whole branch of speculation.

A second scaling fact makes the salvage side sharp. Blow up $g_i$ (with $\operatorname{Ric}(g_i)=g_i+E_i$, $|E_i|\le\delta_i$) at rate $t_i\to0$: $\tilde g_i=t_i^{-2}g_i$ has $\operatorname{Ric}(\tilde g_i)=g_i+E_i=t_i^2\tilde g_i+E_i$, so as a tensor measured in $\tilde g_i$,

$$
|\operatorname{Ric}(\tilde g_i)|_{\tilde g_i}=t_i^2\,|\operatorname{Ric}(g_i)|_{g_i}\le C t_i^2\to0 .
$$

**Any bubble is asymptotically Ricci-flat.** The Einstein-constant term and the $O(\delta)$ defect both scale away. On the bubble, Cheeger–Tian $\epsilon$-regularity *does* apply (it is a Ricci-flat ALE/ALF/ALG limit), so bubbles carry quantized energy bounded below. This is the mechanism that salvages a usable regularity statement without ever bounding $|\operatorname{Rm}(g_i)|$ pointwise.

With these two facts the Execute targets organize cleanly.

---

## P1 (highest value, salvage). Energy-quantization no-bubble lemma at unwrapped scale

**Mechanism.** Under two-sided pinching the defect vanishes under blow-up, so a curvature concentration point produces, after rescaling and (where needed) passing to a local cover, a complete Ricci-flat ALE/ALF/ALG space of dimension four. Such spaces have $\int|\operatorname{Rm}|^2\ge\epsilon_0>0$ (Eguchi–Hanson $=12\pi^2$; general gravitational instantons bounded below). Hence *small curvature energy at a definite unwrapped scale forbids concentration.*

**Target statement to build.** There exist $\epsilon_4(n{=}4)>0$, $C$ such that if $(B_2(p),g)$ has $\|\operatorname{Ric}_g-g\|_{L^\infty}\le\delta\le\delta_0$, the unit ball is unwrapped at a definite scale (an accessible normal cover $\widehat B$ with lower harmonic radius, in the sense of Naber–Zhang Prop 6.4), and $\int_{\widehat B}|\operatorname{Rm}|^2<\epsilon_4$, then $|\operatorname{Rm}|\le C$ on the corresponding smaller cover ball.

**Expected calculation.** (i) Blow-up analysis: rescaled limit is Ricci-flat by the $t_i^2$ scaling above; (ii) Bando–Kasue–Nakajima / Anderson removable-singularity and the ALE energy lower bound; (iii) contradiction with $\int|\operatorname{Rm}|^2<\epsilon_4$. The Ricci-flatness of the blow-up is the step that replaces the missing $|\nabla\operatorname{Ric}|$ control demanded by Naber–Zhang Prop 6.5 — you never differentiate the defect; you let it scale away.

**What defeats it.** The unwrapping hypothesis. If no definite-scale accessible cover exists (rank drop, degenerating model noncollapsing radius $r_c\to0$, residual four-dimensional core), the blow-up base is not fixed and the argument stalls. This is the honest residual, shared verbatim with A01/A03's accessible-cover residual.

**Evidence that changes the route.** If the ALF/ALG (Taub–NUT, Ooguri–Vafa) bubbles that Lott flags for K3 collapse can appear with energy *below* the ALE quantum in the two-sided-pinched setting, the single constant $\epsilon_4$ must become a finite table indexed by instanton type; retrieving the ALF/ALG energy lower bounds (Minerbe, Chen–Chen) settles this and is worth a source request.

---

## P2 (highest value, bypass). Harmonic-radius $\Rightarrow$ smooth Einstein germ, with no pointwise curvature bound

**Mechanism.** For the *existence* question we do not need $|\operatorname{Rm}(g_i)|$ bounded; we need a smooth Einstein limit germ. On accessible covers Naber–Zhang Prop 6.4 gives $r_h(\tilde q)\ge h_0>0$. In harmonic coordinates,

$$
g_i^{ab}\partial_a\partial_b (g_i)_{jk}=-2(\operatorname{Ric}_{g_i})_{jk}+Q_{jk}(g_i^{-1},\partial g_i),
\qquad \operatorname{Ric}_{g_i}=g_i+o_{L^\infty}(1).
$$

Uniform $C^{1,\alpha}\cap W^{2,p}$ control gives $g_i\to g_\infty$ with $\operatorname{Ric}_{g_\infty}=g_\infty$ weakly, hence smooth Einstein by elliptic bootstrap *on the limit* (where Ricci is exactly $g_\infty$, so all derivative bounds are free). Naber–Zhang Prop 6.5 is thereby made unnecessary for producing the germ: it is needed only if one insists on curvature bounds for the pre-limit $g_i$, which the existence program does not require.

**Target statement to build.** Precise lemma: accessible-cover hypotheses $\Rightarrow$ local smooth Einstein germ $\operatorname{Ric}=g_\infty$ on a fixed-size chart of the cover, with the deck group acting by isometries on the germ, so the germ descends to a smooth Einstein orbifold chart downstairs.

**Expected calculation.** Standard harmonic-coordinate compactness (Anderson) plus the elliptic equation; the one new bookkeeping item is that the defect enters only as an $L^\infty$ right-hand side that converges to zero, so no derivative-of-defect term ever appears. Confirm the deck-equivariance passes to the limit (it does, being an isometric action with uniformly bounded displacement on the cover ball).

**What defeats it.** Same accessible-cover residual as P1. Also: assembling the local Einstein orbifold germs into a *global* Einstein metric on $M$ is a separate desingularization/obstruction problem (this is where the projection-bridge material in `step8_projection_bridge_target.md` re-enters). The germ lemma is a genuine advance but is not existence.

**Evidence that changes the route.** If one can show the singular set of the limit is codimension $\ge4$ with isolated ALE/orbifold singularities (via P1's energy quantization controlling the number of concentration points), then germ-assembly reduces to the finite orbifold desingularization literature (LeBrun–Ozuch admissibility), and the route becomes "control the number and type of singular points," which is quantitative and attackable.

---

## P3 (probe, potentially decisive). Positive-branch orbit-volume equation for collapse-with-curvature

**Mechanism.** A03 derived, for exact adapted abelian collapse, $\Delta_B v=(\tfrac14|F|^2-\lambda N)v$, and for $\mathrm{nil}^3$ cohomogeneity-one, $v''=(3-\rho/2)v$, both in the $\lambda<0$ branch. The positive branch ($\lambda>0$, $\operatorname{Ric}\approx +g$) flips the sign of the $\lambda N$ term. Test whether tight positive pinching is *compatible* with a collapsing fiber whose Ricci stays $\approx1$.

**Expected calculation.** For a constant-length circle collapse with connection curvature $F$, O'Neill gives fiber Ricci $\sim\tfrac14\ell^2|F|^2$ and horizontal sectional corrections $\sim\ell^2|F|^2$. Tight positive pinching forces fiber Ricci $\to1$, hence $\ell^2|F|^2\to c>0$, hence $|F|\sim 1/\ell$ but *bounded curvature* — no concentration. To get $|\operatorname{Rm}|\to\infty$ one must vary $\ell$, producing a term $-\ell''/\ell$ in the fiber Ricci; write the resulting orbit-volume ODE in the $\lambda>0$ normalization and read off whether a positive-Ricci-pinched profile can close up on a circle base or reach a finite-distance endpoint with $v\to0$. Compare directly with A03's corrected $v''=(3-\rho/2)v$, being careful that the constant "$3$" there carried $|\lambda|=1$; in the positive branch the sign of that constant is what decides convexity of $v$ and hence periodic/endpoint compatibility.

**What defeats it.** Rank-drop and singular strata are not adapted-action models, so an ODE exclusion of *smooth* fibered collapse leaves the singular loci — exactly the loci where P1/P2 also need the accessible cover. Also the exact-adapted-action hypothesis is stronger than an approximate F-structure; a Cheeger–Fukaya–Gromov near-model must be justified before the ODE is used for the true metric.

**Evidence that changes the route.** If the positive-branch ODE forbids all smooth adapted collapse (as the $\mathrm{nil}^3$ circle-base case already does in A03's $\lambda<0$ computation), then simply-connected positive collapse is confined entirely to singular/rank-drop strata, and the volume-gap question (P4) reduces to bounding the volume proportion of those strata — a finite, energy-controlled quantity via P1.

---

## P4 (the linchpin the positive branch actually needs). Simply-connected volume gap through the Euler/F-structure obstruction plus singular-strata control

**Mechanism.** Lens spaces show positive-Ricci collapse comes from large $\pi_1$ acting on a noncollapsed cover; the universal cover stays noncollapsed. Conjecture: a simply-connected closed $4$-manifold with $\|\operatorname{Ric}-g\|_{L^\infty}\le\delta_0$ has $\operatorname{Vol}\ge v_0>0$. Two ingredients combine:

1. **Regular part.** A positive-rank F-structure forces $\chi=0$ on its support (fixed-point-free torus symmetry). But tight positive pinching gives $\operatorname{Ric}>0$, Bochner $b_1=0$, so $\chi(M)=2+b_2\ge2$. Regular free collapse over positive volume proportion is therefore obstructed by Euler characteristic — the Step 8 observation, now used as the regular-part half of a volume gap.
2. **Singular part.** The rank-drop / singular-fiber loci carry the topology that regular collapse cannot, and by P1 each concentration site costs $\ge\epsilon_4$ of curvature energy. The Chern–Gauss–Bonnet budget $\int|W|^2\le 8\pi^2\chi + O(\operatorname{Vol})$ then bounds the *number* of singular sites, and each site's collapsed neighborhood has controlled volume via Bishop only if it is noncollapsed after unwrapping.

**Target statement to build.** A conditional volume gap: simply-connected + tight positive pinching + (every singular site is unwrappable at a definite scale) $\Rightarrow$ $\operatorname{Vol}\ge v_0$. Then Proposition 1.1's finite-cover reduction promotes this to a universal volume gap over all closed connected $M^4$, hence finite diffeomorphism types, hence (with P2 germ + assembly) the collapse side of $P_4^+$.

**Expected calculation.** Combine: Bochner $b_1=0$; the F-structure $\chi=0$ statement on the regular part; CGB lower bound $\int|W|^2\ge 8\pi^2[\chi-2((1+\delta)/(1-\delta))^2]$ (Step 8, verified) to force curvature energy proportional to $\chi$; P1 to convert energy into a finite number of unwrappable sites; Bishop on the unwrapped covers to recover a definite volume.

**What defeats it.** A simply-connected sequence whose volume vanishes while *all* topology hides in non-unwrappable singular strata (degenerating $r_c$, four-dimensional residual cores). This is the same residual as P1/P2 — the three targets share one honest unknown, which is itself strong evidence that this is the true center of the problem.

**Evidence that changes the route.** An explicit simply-connected $\operatorname{Ric}\approx g$ collapsing example would refute the gap and, through Proposition 1.1 run backwards, would refute $P_4^+$. Serious effort at constructing one (P3 shows the sign obstruction blocks the smooth adapted models) is the cheapest way to test the gap's plausibility.

---

## P5 (probe, cheap, expected null). High-frequency and two-scale packet refutation attempts

**Mechanism.** Directly attempt to refute pointwise $\epsilon$-regularity for $C^0$-Ricci-pinched metrics by (a) high-frequency TT packets on a fixed Einstein background, and (b) two-scale ansätze $g_t=g_{\text{orb}}+t\,h_{\text{EH}}$ interpolating an orbifold and an Eguchi–Hanson core.

**Expected calculation.** (a) is settled negatively by the Orientation computation: defect and Weyl both scale as $k^2\epsilon A$; no decoupling. Record this as a clean null result that removes the "hidden oscillation" scenario. (b) A single EH core carries $\int|\operatorname{Rm}|^2=12\pi^2$, not small; verify by the model expansion that the neck $L^2$ energy cannot be made $o(1)$ while $|W|_{\max}\to\infty$, confirming P1's quantization from the construction side rather than by abstract removable-singularity theory.

**What defeats it (as a refutation).** Precisely the collapsed rank-drop mechanism that P1–P4 quarantine; if one *could* build small-energy large-Weyl there under positive pinching, P5(b) would succeed. The O'Neill computation in P3 indicates the positive branch resists this via sign incompatibility between collapsing-fiber Ricci and instanton energy.

**Evidence that changes the route.** If a two-scale positive-pinched construction with $o(1)$ neck energy and diverging $|W|$ is found, the salvage program (P1) is false and the entire route must pivot to a purely $L^2$/weak-projection theory (the Pohozaev/Komar identity of `step8_projection_bridge_target.md`), never using pointwise curvature.

---

## How the pieces fit, and the one shared unknown

The Orientation computation shows the pinching locks defect and Weyl at fixed scale, so all curvature concentration is a collapse phenomenon. P1 converts the blow-up Ricci-flatness into an energy-quantization no-bubble lemma at unwrapped scale. P2 shows that the *existence* program needs only a smooth Einstein germ, obtainable from accessible-cover harmonic radius without any pointwise curvature bound — this is the correct reading of the Naber–Zhang Prop 6.4/6.5 pair, and it makes the missing $|\nabla\operatorname{Ric}|$ control irrelevant to producing germs. P3 tests whether positive pinching forbids smooth collapse outright. P4 assembles Euler-characteristic obstruction, CGB energy budget, and P1's site-counting into the simply-connected volume gap, which via Proposition 1.1 is the master key for $P_4^+$ collapse. P5 is the cheap null-check that keeps the salvage route honest.

All five converge on a single residual object: **points where no definite-scale accessible cover exists** — rank drop, degenerating model noncollapsing radius $r_c\to0$, or a residual four-dimensional core. This is identical to the residual in A01's `route_assessment_step10.md` and A03's `NZ-exclusion` statement, which is strong evidence that this is the genuine mathematical center of Yau 26 in dimension four, not an artifact of any one route. The most decisive single computation to attempt next is P4's quantitative chain (Bochner $\to$ F-structure $\chi=0$ $\to$ CGB energy $\to$ P1 site count $\to$ Bishop volume), because it either yields the volume gap conditional on unwrappability or exposes exactly which non-unwrappable stratum can carry vanishing volume with unbounded topology.

Two source needs would materially sharpen the route: the ALF/ALG gravitational-instanton energy lower bounds (to decide whether P1's $\epsilon_4$ is a single constant or a type-indexed table), and the precise Naber–Zhang Example 3.3–3.5 and §6.3 sharpness statements (to characterize exactly how maximal fibered rank can hold while $r_c\to0$, which is the non-unwrappable stratum every target must eventually confront).

One dimensional caution runs through all five: the CGB/Euler budget in P4 and the four-dimensional Ricci-flat ALE quantization in P1 have no direct analogue for $n\ge5$; Ge–Jiang Theorem 1.6 explicitly shows pointwise $\epsilon$-regularity fails for $n\ge5$ Einstein metrics, so the salvage in P1 is genuinely four-dimensional and the all-dimensional statement needs a different obstruction functional (the renormalized-volume/Weyl-contraction object of Yao type) rather than an extension of these lemmas.