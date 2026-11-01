# TTCS Independent Branch Record

```json
{
  "step_id": 66,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/briefing/original_research_goal.md",
    "Sessions/S0910A01/workspace/notes/step66_route_reorientation_after_IL_bridge.md",
    "Sessions/S0910A01/workspace/notes/step65_per_datum_existence_theorem.md",
    "Skills/qiushi-yau26/references/research/20260910.tex"
  ]
}
```

## Task

The active goal is the sign-unrestricted Yau Problem 26 proposition: in each dimension, decide whether some dimension-only Ricci interval forces the same closed smooth manifold to carry an Einstein metric, or rigorously refute it. Read the route reorientation note and the goal. Generate serious, high-value mathematical routes after the restricted four-dimensional Ishida--LeBrun negative-gap analytic bridge has been completed. Do not propose final writing. Focus on mechanisms that could actually solve or refute the full proposition: positive branch, arbitrary four-dimensional topology, higher dimensions, collapse, topology, calibration-free methods, or new invariants. Distinguish what evidence would make each route promising or eliminate it.

## Output

## Central reduction that reorganizes the whole problem

The single most consequential observation available right now is that pure two‑sided Ricci pinching already triggers the harmonic‑radius compactness machinery, and this converts Yau 26 into a *collapse* problem. Let me make this precise, because it changes which fronts are worth fighting.

Fix the sign‑$+1$ normalization and suppose $P_n^+$ were false. Then there is a sequence of closed smooth $M_i^n$ with metrics $g_i$, $\delta_+(g_i)\to0$ (operator eigenvalues of $A_{g_i}=g_i^{-1}\mathrm{Ric}_{g_i}$ all $\to1$), each $M_i$ carrying no Einstein metric. Two facts hold for free:

- **Myers.** $\mathrm{diam}(M_i,g_i)\le \pi\sqrt{(n-1)/(1-\delta_+)}\le D_n$ and $\pi_1$ finite. The diameter is bounded by a dimensional constant.
- **Two‑sided $C^0$ Ricci bound.** $\|\mathrm{Ric}_{g_i}\|\le (1+\delta_+)$ in operator norm.

Now the Anderson harmonic‑radius estimate (Anderson, *Convergence and rigidity of manifolds under Ricci curvature bounds*, Invent. 1990; Anderson–Cheeger $C^\alpha$ theory) says: a two‑sided $L^\infty$ Ricci bound **plus a unit‑scale volume lower bound** $\mathrm{Vol}(B_1(x))\ge v>0$ forces a uniform harmonic radius. In harmonic charts $\Delta g_{ij}=-2\mathrm{Ric}_{ij}+Q(\partial g)$, so $\mathrm{Ric}\in L^\infty$ gives $g\in W^{2,p}\hookrightarrow C^{1,\alpha}$ **with no bound on the full curvature required**. Consequently, on the non‑collapsed subsequence one gets $C^{1,\alpha}$ convergence to a limit metric $g_\infty$ satisfying $\mathrm{Ric}_{g_\infty}=g_\infty$ weakly; elliptic bootstrap in harmonic coordinates upgrades $g_\infty$ to $C^\infty$ (indeed $C^\omega$) Einstein. Finiteness of diffeomorphism type plus $C^{1,\alpha}$ convergence gives $M_i\cong M_\infty$ for large $i$, so $M_i$ carries the pulled‑back Einstein metric — contradicting no‑Einstein.

Two things deserve emphasis. First, this argument survives *arbitrarily large Weyl curvature along the sequence*: the harmonic radius needs only the Ricci bound and non‑collapse, so second derivatives of $g_i$ may be unbounded in $L^\infty$ while $C^{1,\alpha}$ convergence and the smooth Einstein limit persist. Second, the argument uses no calibration, no Seiberg–Witten input, and no dimension restriction. Therefore:

> **Any counterexample sequence to the positive branch, in any dimension, must collapse:** $\inf_x \mathrm{Vol}(B_1(x,g_i))\to0$ at unit diameter scale.

This is the crisp statement to carry forward. It has an immediate strategic corollary tied to the branch reduction $Q_n\Leftrightarrow(P_n^+\vee P_n^-)$ proved in the dossier: **proving $P_n^+$ alone settles $Q_n$ affirmatively.** One does not need the $\sigma=-1$ branch for an affirmative solution. And $P_2^+, P_3^+$ are already known (uniformization; Hamilton), so the live target is $n\ge4$, and it is entirely inside the collapsed regime.

## What "collapse" actually contains — and the corrected structural conjecture

A tempting shortcut is "tight isotropic Ricci pinching prevents collapse." This is **false**, and the reason is instructive. Round space‑form quotients $S^n/\Gamma_i$ with $|\Gamma_i|\to\infty$ (e.g. lens spaces $S^3/\mathbb Z_k$) have $\mathrm{Ric}=(n-1)g$ *exactly* ($\delta_+=0$), yet $\mathrm{Vol}\to0$ and injectivity radius $\to0$: genuine collapse with perfect isotropic pinching. But these manifolds *do* carry Einstein metrics — they are the round quotients themselves. So collapse is not the enemy; **collapse onto a smooth type that carries no Einstein metric** is.

Contrast this with anisotropic collapse. In a canonical‑variation / Berger collapse (fiber scaled by $t\to0$), O'Neill's formulas drive the Ricci eigenvalues apart: for shrinking Hopf $S^1\subset S^3$ the Ricci operator eigenvalues run to $(2t^2,\,2-t^2,\,2-t^2)$, so $\delta_+$ stays bounded away from $0$. For a shrinking flat‑torus fiber the vertical Ricci $\to0$ while horizontal Ricci tends to the base Ricci — again strong anisotropy. So the mechanism that produces most collapse examples is *incompatible* with tight isotropic Ricci pinching.

The correct structural conjecture is therefore a dichotomy:

> **(Collapse dichotomy.)** A collapsing family with $\delta_+(g_i)\to0$ is, up to bounded geometry structure, modeled on *isometric quotients / homogeneous fibrations of a fixed Einstein space* — the isotropy‑preserving type exemplified by space‑form quotients — rather than on anisotropic fiber‑shrinking. In particular the collapsed $M_i$ carries an Einstein metric.

If this holds, combined with the harmonic‑radius reduction it **proves $P_n^+$ for all $n$, hence solves Yau 26 affirmatively in every dimension.** The tools to attack it are exactly the bounded‑Ricci collapse theory: Naber–Zhang *Topology and $\varepsilon$-regularity on collapsed manifolds with Ricci bounds* (Geom. Topol. 2016) gives local nilpotent structure and $\varepsilon$‑regularity under two‑sided Ricci bounds even with unbounded full curvature; Kapovitch–Wilking's generalized Margulis lemma gives almost‑nilpotent local $\pi_1$ from a Ricci *lower* bound alone; Cheeger–Fukaya–Gromov N‑structures cover the bounded‑curvature part. The new content needed is the *isotropy obstruction*: showing that a nontrivial nilpotent/torus collapse direction forces a definite Ricci anisotropy $\delta_+\ge c_n>0$, so the only surviving collapse is the homogeneous‑quotient type.

**What would confirm or eliminate this route.** Two decisive computations:
1. *Anisotropy lower bound.* On a principal‑$T^k$ (or nil‑) bundle with a collapsing connection metric, compute the Ricci operator eigenvalue spread via O'Neill/submersion formulas and prove $\delta_+\ge c(n,\text{bundle})>0$ uniformly as the fiber shrinks, or exhibit a bundle where the spread $\to0$. A vanishing spread on a total space with no Einstein metric would be a genuine refutation candidate; a uniform positive spread across all nontrivial N‑structures essentially proves the dichotomy's hard half.
2. *Search for isotropic collapse off the homogeneous list.* Look for any $\delta_+\to0$ collapsing family whose collapsed limit is not an isometric quotient of a symmetric Einstein space and whose total space is provably no‑Einstein. Its non‑existence (structural) closes the affirmative solution; its existence refutes $P_n^+$ and then demands attacking $P_n^-$ in the same dimension for a full refutation.

## The $\sigma=-1$ branch as an independent affirmative route

Even though $P_n^+$ suffices, the $\sigma=-1$ branch is a parallel affirmative attack and it interacts differently with the reduction. Here Myers gives no diameter bound, so one uses a thick–thin decomposition. On the thick part $\mathrm{Vol}(B_1)\ge v$ the same harmonic‑radius argument gives $C^{1,\alpha}$ convergence to smooth pieces with $\mathrm{Ric}=-g$. The thin part is controlled by the Kapovitch–Wilking generalized Margulis lemma, which needs only $\mathrm{Ric}\ge-(n-1)$ — a hypothesis tight pinching supplies — and yields almost‑nilpotent thin‑part topology (cusps/tubes). This is precisely the architecture of the Hamenstädt–Jäckel / Jäckel effective‑hyperbolization results, but those inputs assume a *sectional* pinching $\sec\le-K$ and a Margulis‑scale thin part with $\sec\equiv-1$. The genuine research target is to reconstruct the thin‑part model and the gluing‑to‑closed step from pure two‑sided Ricci pinching, replacing the sectional hypothesis by the Ricci‑only Margulis structure. This is calibration‑free and, if achieved, gives $P_n^-$ as a second independent affirmative proof. The distinguishing question: can the thin‑part collar geometry (which sectional pinching pins down as a hyperbolic cusp) be forced by Ricci pinching plus the Kapovitch–Wilking nilpotent structure, or does Ricci pinching permit exotic collar geometries that block gluing?

## Obstruction–pinching incompatibility as a unifying theorem shape

The Chern–Gauss–Bonnet computation in the dossier (tight $\pm1$ pinching $\Rightarrow$ strict $2\chi>3|\tau|$) and the completed four‑dimensional Ishida–LeBrun analysis are two instances of one principle worth isolating and pushing:

> Every curvature‑integral obstruction to Einstein metrics that has the form "$\int F(\mathrm{Rm})\ge0$ forced by topology, with the trace‑free‑Ricci part of $F$ enterable with a definite sign" is *incompatible with tight Ricci pinching*, because pinching drives the $E=\mathrm{Ric}-\tfrac{s}{n}g$ contribution small ($|E|^2\le n\,\delta_\sigma^2$) and pushes the topological quantity into the Einstein‑allowed region.

In dimension four this is testable against the entire LeBrun obstruction catalogue (Seiberg–Witten Weyl functional estimates, the $2\chi\pm3\tau$ and its refinements). If the whole four‑dimensional obstruction list turns out to conflict with tight pinching, then the pinchable smooth types in dimension four are contained in the "no known obstruction" region, and any refutation there would require a *new* obstruction on a strict‑Hitchin–Thorpe, non‑Seiberg–Witten‑obstructed manifold. Surveying whether such obstruction‑free no‑Einstein four‑manifolds even exist is itself a decisive input: their absence is strong affirmative evidence, their presence is a concrete refutation nursery. This does not by itself prove existence (that is the harmonic‑radius/collapse program above), but it tells the core agent exactly where a four‑dimensional counterexample could possibly live.

## Higher dimensions: where refutation is starved of obstructions

For $n\ge5$ there is no Chern–Gauss–Bonnet‑strength pinching barrier — the Gauss–Bonnet integrand is not sign‑definite and does not bound curvature by pinching. Naively this opens refutation space. But refutation needs a *provably no‑Einstein* smooth type, and high dimensions are obstruction‑poor: most candidate no‑Einstein constructions (connected sums $\#_k(S^2\times S^{n-2})$, certain fibre bundles carrying positive Ricci à la Sha–Yang / Reiser / Perelman) have *unknown* Einstein status, and the few obstructions (Hitchin's $\hat A$/Dirac for special holonomy, entropy rigidity, simplicial volume) either require extra structure or, in the entropy/Besson–Courtois–Gallot direction, produce rigidity for locally symmetric targets rather than non‑existence on arbitrary types. So the honest picture is symmetric: high‑dimensional refutation is blocked by the same scarcity of obstructions that blocks direct existence proofs. The productive move is not to hunt a high‑dimensional counterexample blindly but to run the positive‑branch collapse program (which is dimension‑independent) and, in parallel, to identify a *single* dimension‑only obstruction invariant — a curvature‑integral or entropy quantity that is (a) forced into the Einstein‑allowed region by tight pinching and (b) nontrivial on some no‑Einstein type. Absent such an invariant, the affirmative collapse route is the only one with a visible finish.

## An elimination the core agent should internalize

Several superficially independent refutation ideas collapse into the same corner, and recognizing this saves effort:

- *"Build tightly pinched metrics with wild, spiking Weyl on a forbidden topology."* Eliminated in the non‑collapsed case by the harmonic‑radius argument: $C^{1,\alpha}$ convergence to a smooth Einstein limit holds regardless of Weyl spikes, so a non‑collapsed Weyl‑spike family gives Einstein existence, not a counterexample.
- *"Approximate critical point of the Einstein–Hilbert functional need not have a nearby critical point."* The trace‑free Ricci $E$ is exactly the $L^2$ gradient of the normalized total scalar curvature on the unit‑volume slice, and tight pinching makes $\|E\|_{C^0}$ small *and* fixes the scale via $s\approx n\sigma$. So Yau 26 is a "small‑gradient $\Rightarrow$ genuine critical point on the same manifold" question. But the compactness that a Łojasiewicz–Simon or min‑max argument needs is again destroyed only by collapse/bubbling, and bubbling is exactly what harmonic radius rules out under non‑collapse.

Both funnel to the identical residual issue: **collapse onto a no‑Einstein smooth type.** This is the sole surviving obstacle across the refutation and the affirmative variational routes alike, which is why the collapse dichotomy of the section above is the true center of gravity.

## Concrete work that would move the key judgment

1. **Re‑derive the Anderson $C^{1,\alpha}$ compactness statement in the exact form needed** (two‑sided $C^0$ Ricci $+$ unit‑scale volume lower bound $+$ diameter bound $\Rightarrow$ subsequential $C^{1,\alpha}$ convergence to a smooth Einstein manifold with eventual diffeomorphism), from Anderson 1990 and Anderson–Cheeger, so the non‑collapse reduction stands on cited, verified ground rather than folklore.
2. **The submersion‑Ricci anisotropy computation** on collapsing $T^k$‑ and nil‑bundles: prove a uniform eigenvalue‑spread lower bound $\delta_+\ge c_n$, or find the bundle that breaks it. Wolfram/symbolic O'Neill‑formula computation is the right first pass; the outcome directly decides the collapse dichotomy.
3. **Import Naber–Zhang and Kapovitch–Wilking as the collapse structure engine**, and formulate the precise proposition "$\delta_+\le\varepsilon_n$ $\Rightarrow$ the collapse N‑structure is isometric‑quotient type $\Rightarrow$ $M$ carries Einstein." This is the theorem whose proof would solve Yau 26 affirmatively.
4. **Catalogue the four‑dimensional obstruction list against tight pinching** to test whether obstructed and pinchable are disjoint, locating (or excluding) obstruction‑free no‑Einstein four‑manifolds.
5. **Formulate the pure‑Ricci thin‑part model** for the $\sigma=-1$ branch using the Ricci‑only Margulis lemma, as an independent affirmative route and a cross‑check on the positive‑branch conclusion.

The through‑line for the core agent: the completed four‑dimensional $\sigma=-1$ analytic bridge is one calibration‑bound instance, but the affirmative solution of the *full* proposition most plausibly runs through $P_n^+$ via harmonic‑radius compactness plus a collapse‑structure theorem, and every serious refutation attempt is forced into the same collapse regime, where the space‑form‑quotient example shows the real question is not whether collapse happens but whether collapse can land on a genuinely no‑Einstein smooth type.