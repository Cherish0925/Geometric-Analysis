# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step2_mechanisms_analysis.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

Yau Problem 26 asks whether for each dimension n, there exist dimension-only constants c_n < C_n such that any closed connected smooth Riemannian n-manifold (M,g) with c_n g ≤ Ric_g ≤ C_n g admits an Einstein metric h on M. The problem decomposes into positive and negative branches P_n^+ and P_n^-. Through quantitative Chern-Weil analysis combined with Seiberg-Witten theory, the positive branch in dimension 4 is strongly protected: all known no-Einstein 4-manifolds have δ_+ bounded away from 0 (HT-violating: δ_+ ≥ 0.366; LeBrun SW-obstructed: δ_+ ≥ 1 since no positive scalar curvature). The NEGATIVE branch is the live territory. For LeBrun manifolds M = X#k CPbar² with A = c₁²(X), combining LeBrun's ∫s²dV ≥ 32π²A with CGB volume bounds gives δ_- ≥ C/√A for varying manifolds with A→∞, which tends to 0. So varying-manifold counterexamples are not ruled out by current integral bounds. The central unsolved problems are: (A) Can tight two-sided negative Ricci pinching (Ric ≈ -g in operator norm) be constructed on manifolds with no Einstein metric? Lohkamp gives one-sided Ric < 0 flexibility and h-principle for open relations, but not two-sided bounds. DeTurck prescribed-Ricci is local. Min-Oo/Jäckel need additional conditions (d²max|K| bounded or sec < 0). (B) Alternatively, can a new existence theorem work with ONLY Ricci pinching, without full curvature/derivative/diameter control? All known existence theorems require more than Ricci. Propose genuinely new mathematical mechanisms, constructions, or proof strategies that could resolve either direction. For a counterexample mechanism: how could one construct a metric with all Ricci eigenvalues in (-1-ε, -1+ε) on a LeBrun manifold with the Weyl curvature free? For an existence mechanism: what new analytic, variational, or topological principle could extract Einstein existence from pure Ricci pinching, possibly through a new flow, functional, or topological constraint?

## Output

# Generator Memo — Yau 26: Branch asymmetry from a dimension-4 curvature-energy identity, and where the decisive mathematics actually sits

I want to reopen the space around this task with one structural observation that ties the two directions together, and then develop the constructions and existence mechanisms that follow from it. The organizing fact is that in dimension 4 the total Weyl energy is controlled by topology, and this single identity explains why the two branches behave so differently — and it relocates the decisive unknowns to places the current notes underweight.

## 1. A dimension-4 curvature-energy identity that both branches must obey

Take the two Gauss–Bonnet/signature identities
$$
2\chi\pm 3\tau=\frac1{4\pi^2}\int_M\Big(2|W^\pm|^2+\tfrac{s^2}{24}-\tfrac{|E|^2}{2}\Big)dV.
$$
Solve for the Weyl energy:
$$
\int_M|W^\pm|^2\,dV \;=\;2\pi^2(2\chi\pm3\tau)\;-\;\frac1{48}\int_M s^2\,dV\;+\;\frac14\int_M|E|^2\,dV.
$$
Now impose $\delta_\sigma(g)\le\varepsilon$ pointwise. Writing Ricci eigenvalues $\sigma+e_i$ with $|e_i|\le\varepsilon$: $|E|^2=\sum_i(e_i-\bar e)^2\le 4\varepsilon^2$ pointwise, and $s^2\ge 16(1-\varepsilon)^2$ pointwise. Hence
$$
0\le\int_M|W^\pm|^2\,dV\;\le\;2\pi^2(2\chi\pm3\tau)\;-\;\mathrm{Vol}(M,g)\Big[\tfrac{(1-\varepsilon)^2}{3}-\varepsilon^2\Big].
$$
Two consequences that I think are underused in the current picture:

**(a) A volume ceiling in *both* branches.** For $\varepsilon$ small the bracket is near $1/3$, so
$$
\mathrm{Vol}(M,g)\le \frac{2\pi^2(2\chi\pm3\tau)}{(1-\varepsilon)^2/3-\varepsilon^2}\approx 6\pi^2\,(2\chi\pm3\tau).
$$
This holds regardless of the sign of $s$. The step-2 note states that the $\sigma=-1$ branch has "no volume upper bound"; that is correct for Bishop–Gromov (which needs a lower Ricci bound of the productive sign) but it is **not** correct once Chern–Gauss–Bonnet is used. In dimension 4, tight two-sided Ricci pinching of either sign forces $\mathrm{Vol}\le 6\pi^2\min(2\chi+3\tau,\,2\chi-3\tau)$. This is a sharpening worth propagating: any $\sigma=-1$ counterexample sequence has volume growing only as fast as its topology $2\chi\pm3\tau$, not freely.

**(b) The total Weyl energy is topologically capped.** $\int|W|^2=\int|W^+|^2+\int|W^-|^2\le 2\pi^2\big[(2\chi+3\tau)+(2\chi-3\tau)\big]=8\pi^2\chi$ (minus a positive volume term). So under tight Ricci pinching the *entire* curvature tensor has $L^2$-energy bounded by the Euler characteristic. Weyl is free *pointwise* but its integral is not free. This is the dimension-4 miracle, and it is exactly the input for $\varepsilon$-regularity and orbifold compactness.

## 2. The mechanism that explains the branch asymmetry

Put (a) and (b) together with the sign structure.

**σ = +1.** Myers already bounds the diameter, CGB caps the volume, and (b) caps the curvature energy for *fixed topology*. So a sequence with $\delta_+\to0$ on a *fixed* smooth type has bounded diameter, bounded volume, and bounded $\int|Rm|^2$. Away from finitely many curvature-concentration points it converges (Anderson/Cheeger–Naber orbifold compactness) to a limit whose regular part is Einstein with $\mathrm{Ric}=+g$. The freedom to escape is only through **collapse** (volume $\to0$), which Myers does not prevent.

**σ = −1.** Here the story genuinely differs, but not through volume: it differs because the *topology grows*. On LeBrun manifolds $X\#k\overline{\mathbb{CP}}^2$ the Seiberg–Witten estimate $\int s^2\ge 32\pi^2 A$ (with $A=c_1^2(X)$) forces, via $s^2\approx16$, a volume *floor* $\mathrm{Vol}\gtrsim 2\pi^2 A$. Combined with the ceiling $\mathrm{Vol}\le 6\pi^2(2\chi+3\tau)=6\pi^2(A-k)$, one gets a per-manifold pinching floor. Writing $\eta=k/A-2/3$, compatibility of floor and ceiling forces
$$
\delta_-(g)\;\gtrsim\;\tfrac32\,\eta\qquad\text{for every metric }g\text{ on a fixed LeBrun manifold.}
$$
So **each fixed LeBrun manifold has a strictly positive pinching floor** — it cannot be tightly $\sigma=-1$ pinched. The floor degenerates to zero only along the *family* $k/A\to2/3$, which needs $A\to\infty$ (integrality forces $\eta\gtrsim1/A$). The Weyl budget grows with $A$ because the topological cap $2\pi^2(A-k)$ grows. This is the precise sense in which the $\sigma=-1$ branch "escapes": not through one manifold with large volume, but through a family with growing $\chi,\tau$ and correspondingly growing curvature-energy budget.

**The unifying statement.** The same free datum — the Weyl tensor — is (i) the object a $\sigma=-1$ counterexample must spend, and (ii) the object that any existence proof cannot control. In the $+1$ branch, fixed topology caps that budget and pushes toward existence; in the $-1$ branch, growing topology reopens it and pushes toward construction. I recommend making this the backbone of the analysis rather than treating the branches as parallel.

## 3. What a σ = −1 counterexample metric must look like — a concrete construction target

The identity pins down the *shape* of any counterexample metric on $X\#k\overline{\mathbb{CP}}^2$:

- Volume $\approx 2\pi^2 A(1+O(\varepsilon))$, near the SW floor.
- $\int|W^+|^2$ squeezed near zero. Indeed, plugging $\mathrm{Vol}\approx2\pi^2A$ and $2\chi+3\tau=A-k$ into the identity leaves almost no room: the metric must be **approximately anti-self-dual**, $W^+\approx0$. A Kähler metric is disqualified because Kähler forces $|W^+|^2=s^2/24$, giving $\int|W^+|^2\approx \tfrac23\mathrm{Vol}$, far above the cap when $k>2A/3$.

So the counterexample, if it exists, is a **near-anti-self-dual, Ricci-pinched metric on a blow-up**, far from Kähler. This is a specific and well-studied geometric arena, not a wilderness:

- **Taubes**: $M\#k\overline{\mathbb{CP}}^2$ admits anti-self-dual metrics for $k$ large. These already kill $W^+$, matching the CGB requirement.
- **LeBrun's explicit self-dual / scalar-flat Kähler ALE and hyperbolic-ansatz metrics** on blow-ups give controlled building blocks.
- The remaining task is to arrange $\mathrm{Ric}\approx-g$ on top of near-ASD structure — an approximate solution of the ASD–Einstein system with $\lambda<0$. An *exact* ASD–Einstein solution would be Einstein (contradiction on LeBrun manifolds), so the construction must stop at controlled two-sided pinching, spending $W^+$ down to the CGB floor but not to zero.

Sources to retrieve and read at theorem level: Taubes, "The existence of anti-self-dual conformal structures," J. Diff. Geom. 36 (1992); LeBrun's scalar-flat Kähler and explicit self-dual constructions on blow-ups (e.g., "Explicit self-dual metrics on $\mathbb{CP}^2\#\cdots\#\mathbb{CP}^2$," and the Weyl-functional papers). The distinguishing computation to run: on a candidate LeBrun manifold, verify numerically that a near-ASD building-block gluing can hold $\int|W^+|^2$ at the CGB floor while $\int|E|^2/\mathrm{Vol}\le 4\varepsilon^2$ — i.e., check the two budgets are simultaneously satisfiable at the target $A,k$.

## 4. The relative Lohkamp route, and the exact statement that decides it

An independent construction avenue is Lohkamp's flexibility for $\mathrm{Ric}<0$. The decisive unknown is whether it delivers *two-sided operator-norm* pinching, not merely one-sided sign control.

Concretely: is there, on the complement of a ball in $\overline{\mathbb{CP}}^2$ (a "cap" for the blow-up connect-sum), a metric with $\mathrm{Ric}\in(-(n-1)-\varepsilon,\,-(n-1)+\varepsilon)\,g$ in operator norm, with a hyperbolic-funnel collar (constant curvature $-1$) along the separating $S^3$? If yes, one glues arbitrarily many such caps onto a closed hyperbolic 4-manifold $H$ to build $H\#k\overline{\mathbb{CP}}^2$ with tight $\sigma=-1$ pinching — refuting $P_4^-$, and by taking products/warped stabilizations, informing higher $n$.

The subtlety that must be extracted from the actual theorems: Lohkamp's constructions ("Metrics of negative Ricci curvature," Ann. Math. 140 (1994); "Curvature h-principles," Ann. Math. 142 (1995)) produce metrics whose Ricci tensor $C^0$-approximates a target, but the wrinkling can make $g$ itself degenerate in the directions being controlled. Whether $\delta_-(g)\to0$ depends on whether the approximation is "$\mathrm{Ric}_g-T$ small as tensors while $g$ stays uniformly comparable to a fixed background" or "small only after $g$ collapses." The former yields operator-norm pinching; the latter does not. This distinction is the single most decisive thing to read out of Lohkamp precisely, together with whether the construction admits a *relative* version with a prescribed cylindrical collar. I would treat "extract the exact prescription statement and its uniform metric comparability" as the highest-value source action for the $\sigma=-1$ direction.

## 5. The positive-branch existence route — and why it, not the σ = −1 construction, is the path to answering Q₄

A logical point that should reshape priorities: $Q_n\Leftrightarrow P_n^+\vee P_n^-$. To *refute* $Q_4$ one must break **both** branches in dimension 4. But §2 shows $P_4^+$ is strongly structured toward existence. So a complete $\sigma=-1$ counterexample sequence on LeBrun manifolds, however deep, would **not** refute $Q_4$ — the $+1$ branch would still supply the constants $a=1-\varepsilon$, $b=1+\varepsilon$. Conversely, *proving* $P_4^+$ settles $Q_4$ affirmatively regardless of the $-1$ branch. The disjunction structure means one gets to choose the more tractable branch in each dimension — and in dimension 4 that is the $+1$ branch. This makes an existence theorem for tight positive Ricci pinching the actual route to an answer, and I think it deserves at least equal weight to the counterexample hunt.

Here is a concrete route to $P_4^+$, built entirely on §1:

Suppose $P_4^+$ is false. Then there is a sequence $(M_j,g_j)$ with $\delta_+(g_j)\to0$ and $\mathrm{Ein}(M_j)=\varnothing$.

- **Non-collapsed subcase.** If $\mathrm{Vol}(M_j)\ge v>0$ (with diameter bounded by Myers and volume bounded by CGB), then by (b) $\int|Rm_{g_j}|^2$ is bounded, so orbifold compactness (Anderson; Bando–Kasue–Nakajima; Cheeger–Naber) gives GH convergence to a compact Einstein orbifold $X_\infty$ with $\mathrm{Ric}=g$, finitely many isolated singularities, and anti-self-dual/scalar-flat ALE bubbles. For $j$ large $M_j$ is diffeomorphic to a resolution of $X_\infty$. Now invoke the *classification of these limits*: LeBrun–Ozuch 2026 (arXiv:2601.19215, Theorem B) constrains the positive-Einstein orbifold limits and their bubbles; the admissible smooth resolutions are essentially del Pezzo–type rational surfaces, all of which carry Einstein metrics (Tian; Chen–Donaldson–Sun; Chen–LeBrun–Weber). This contradicts $\mathrm{Ein}(M_j)=\varnothing$. So the non-collapsed positive subcase looks *provable* by assembling existing 2020s results — this is a genuinely reachable theorem, not a wish.

- **Collapsed subcase — the decisive locus.** If $\mathrm{Vol}(M_j)\to0$, the structure is bounded-two-sided-Ricci collapse in dimension 4 (Naber–Zhang, "Topology and $\varepsilon$-regularity theorems on collapsed manifolds with Ricci curvature bounds," Geom. Topol. 2016), where the collapsing directions carry nilpotent/torus structure. Positive Ricci collapse produces candidates like Berger-type $S^3$-bundles, $T^2$- or $S^1$-bundles over surfaces, spherical space-form families. **Either** every such collapsed positively-pinched 4-manifold carries an Einstein metric — which would complete $P_4^+$ and prove $Q_4$ — **or** one of them does not, which would be a $\sigma=+1$ counterexample. This collapsed positive case is therefore doubly decisive and, in my judgment, the single most valuable object of study for $Q_4$: it is simultaneously the last step of a possible affirmative proof and the only place a positive-branch counterexample can hide. The current notes leave it almost untouched.

Sources to retrieve and read at theorem level: Naber–Zhang 2016 (collapsed structure under two-sided Ricci bounds); LeBrun–Ozuch 2026 Theorem B (limit classification); and Anderson's 1989 Corollary B(4) (which the dossier flags as unread) — the latter likely already contains a non-collapsed version and should be read to see exactly which auxiliary hypotheses it uses beyond $\mathrm{Ric}$.

## 6. A variational reframing that indicates which way each branch falls

Define, on a fixed $M$ at fixed scale, the Einstein-deviation energy $\mathcal F_\sigma(g)=\sup_x\|A_g(x)-\sigma\,\mathrm{Id}\|_{\mathrm{op}}=\delta_\sigma(g)$, and $\Gamma_n^\sigma=\inf_M\inf_g\delta_\sigma(g)$ over no-Einstein $M$. $P_n^\sigma\Leftrightarrow\Gamma_n^\sigma>0$. Two mechanistic readings:

- **Why the linearized existence template cannot run on pure Ricci pinching.** In the contraction template $F(g+h)=r+Lh+N(h)$, the linearization $L$ is the Lichnerowicz-type operator $\Delta_L h=\nabla^*\nabla h-2\mathring{Rm}(h)+\dots$, whose zeroth-order term contains the *full* curvature $\mathring{Rm}$, hence Weyl. Under pure Ricci pinching Weyl can concentrate, driving a small eigenvalue of $\Delta_L$ and $\|L^{-1}\|\to\infty$. So no a priori invertibility estimate can be extracted from $\|\mathrm{Ric}+g\|$ alone. This is not a soft remark: it says any existence proof *must* route through a global mechanism (compactness + classification, as in §5) rather than through a direct implicit-function argument. It also explains, mechanistically, why Min-Oo, Jäckel, Hamenstädt–Jäckel all import $\sec<0$ or $\nabla\mathrm{Ric}$ bounds — those are exactly what tame $\mathring{Rm}$ and keep $\|L^{-1}\|$ bounded.

- **Where the flow interpretation points.** The $\lambda$-normalized flow $\partial_t g=-2(\mathrm{Ric}+ (n-1) g)$ has Einstein metrics as its only fixed points. On a no-Einstein $M$ it cannot converge; the pinched set is therefore not flow-invariant, confirming that tight pinching is a non-equilibrium condition that pure Ricci dynamics does not preserve. Farrell–Ontaneda's non-convergence examples are consistent with this. The productive reading: an existence proof should not seek a flow that preserves pinching, but a compactness statement about the *set* of pinched metrics.

The combined message: the integral evidence (no uniform floor in $\sigma=-1$; per-manifold floors degenerating along $A\to\infty$) plus the linearization obstruction leans toward $P_n^-$ being false via varying-manifold construction, while the $\sigma=+1$ compactness structure leans toward $P_4^+$ being true. That asymmetric expectation is itself a research orientation.

## 7. The high-dimension wilderness and what new invariant is needed

Everything in §1 is dimension-4 special: Chern–Gauss–Bonnet caps Weyl energy only because $\dim=4$. In $\dim\ge5$ the Gauss–Bonnet integrand is the Pfaffian of the full curvature and Pontryagin integrands involve all of $Rm$; under Ricci bounds alone none of these caps a Weyl-type energy. So the $\sigma=+1$ compactness route of §5 has no analogue, and simultaneously no closed no-Einstein $n$-manifold ($n\ge5$) is known to refute either branch. Both directions lack tools.

Two openings worth stating as targets:
- **A substitute for the dimension-4 Weyl-energy cap.** Is there, in specific higher dimensions or under spin/holonomy hypotheses, any curvature $L^{p}$-energy bounded by a topological or index-theoretic quantity when $\mathrm{Ric}$ is pinched? Index theory gives sign obstructions (positive scalar $\Rightarrow$ $\hat A=0$ for spin) but not energy caps. Finding even one dimension $\ge5$ with such a cap would transplant the entire §5 mechanism.
- **The disjunction favors provability.** Because $Q_n$ needs only one branch, and because refuting $Q_n$ needs both branches broken in a single fixed $n$ where no-Einstein manifolds must be exhibited, the structural odds favor $Q_n$ being *true and eventually provable* through whichever branch is more tractable in each dimension — dimension 3 already illustrates this (Hamilton for $+$, geometrization for $-$). The high-dimensional content is then: identify the tractable branch per dimension and its enabling structure, rather than hunt symmetric counterexamples.

## 8. Compact list of decisive computations and source retrievals

- Recompute the per-manifold floor $\delta_-\gtrsim c\,\eta$ ($\eta=k/A-2/3$) with LeBrun's exact SW constant for $\int s^2$; pin the power ($c\,\eta$ vs the step-2 $\sqrt\eta$). The conclusion (no uniform floor; floor degenerates only as $A\to\infty$) is robust either way, but the exact rate informs how large $A$ a construction needs.
- Verify the simultaneous satisfiability of the two budgets (Weyl energy at the CGB floor, $\int|E|^2/\mathrm{Vol}\le4\varepsilon^2$) at target $(A,k)$ using near-anti-self-dual building blocks — a symbolic/numeric check that tells you whether the near-ASD construction of §3 is even arithmetically possible before attempting gluing.
- Read Lohkamp 1994/1995 for the exact prescription statement: is $\mathrm{Ric}_g-T$ controlled in $C^0$ *with $g$ uniformly comparable to a fixed background*, and is there a relative (collar) version? This decides the §4 route.
- Read Naber–Zhang 2016 and LeBrun–Ozuch 2026 Theorem B to determine whether §5's non-collapsed step is completable now and what exactly the collapsed positive 4-manifolds are.
- Read Anderson 1989 Corollary B(4) at theorem level to see which auxiliary hypotheses the classical non-collapsed positive result already assumes.

The through-line I would keep visible: in dimension 4 the Weyl energy is topologically capped, and this one fact both routes the affirmative answer (through positive-branch compactness whose last open step is collapsed positive Ricci) and dictates the exact shape of any $\sigma=-1$ counterexample (near-anti-self-dual, near the SW volume floor, only along families with $A\to\infty$). The collapsed positively-pinched 4-manifolds are the pivot: they either complete $Q_4$ or hide the only possible positive-branch counterexample.