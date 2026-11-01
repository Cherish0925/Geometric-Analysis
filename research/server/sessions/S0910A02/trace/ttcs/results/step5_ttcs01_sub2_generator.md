# TTCS Independent Branch Record

```json
{
  "step_id": 5,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step5_positive_branch_all_dimensions.md",
    "Sessions/S0910A02/workspace/notes/step4_preceptor_energy_accounting_and_route_review.md",
    "Sessions/S0910A02/workspace/notes/step1_initial_resolution_and_routes.md",
    "Sessions/S0910A02/workspace/briefing/aligned_research_goal.md"
  ]
}
```

## Task

Generate genuinely different strategies to prove P_n^+ (positive-branch existence) for Yau Problem 26 in ALL dimensions, focusing specifically on closing the collapse gap. The setup: for closed M^n with Ric≈+g, Myers gives bounded diameter, Bishop gives bounded volume, b_1=0, π_1 finite, and GH-precompactness. Noncollapsed subsequences converge to Einstein (Theorem 2 in the note). The ONLY remaining obstacle is collapse: Vol(M_i,g_i)→0 while diam≤D(n). The question is: must the collapsing topology always carry some Einstein metric? Known: (a) Einstein collapse exists (lens spaces S^3/Z_m with Ric=g, Vol→0); (b) Cheeger-Fukaya-Gromov requires sectional bounds we don't have; (c) in dim 4, CGB forces curvature concentration in collapse; (d) π_1 finite constrains fibered structure; (e) b_1=0 means no torus fibers. Generate at least 5 substantially different approaches to proving P_n^+ by addressing collapse. Consider: (i) volume gap from Ricci pinching (can tight Ric≈+g prevent collapse without sectional bounds?); (ii) classification of Einstein-compatible collapse (what topologies can collapse with positive Ricci?); (iii) Ricci flow (does Perelman-type or Hamilton-type flow resolve collapse?); (iv) representation-theoretic or topological constraints from PSC + finite π_1; (v) localized CGB/transgression in dim 4; (vi) entirely new ideas. For each approach, state the key mechanism, what it would need to work, and how it could fail.

## Output

## Central reframing: two physically distinct collapse mechanisms, only one of which survives tight positive pinching

Before listing routes, here is a structural observation that reorganizes "the collapse gap" and sharpens every approach below. The lens-space example and the Berger-sphere example look superficially similar (both shrink a Hopf circle, both have GH limit a lower-dimensional sphere), but they are opposite phenomena for this problem.

**Isometric-quotient collapse.** $L(m,1)=S^3/\mathbb Z_m$ carries the *round* metric. Locally it is isometric to $S^3$, so $\operatorname{Ric}\equiv 2g$ *exactly*; $\delta_+\equiv 0$ along the whole family. The Hopf circle shrinks only because the deck group $\mathbb Z_m\subset S^1$ shortens the global orbit; the pointwise metric never changes. This requires $|\pi_1|=m\to\infty$.

**Metric-distortion collapse.** The Berger sphere $g_\lambda=\lambda^2\eta\otimes\eta+g_{\mathrm{horiz}}$ shrinks the fiber by deforming the metric. Compute O'Neill honestly: the unit vertical field is $U=\lambda^{-1}\partial_{\mathrm{fiber}}$, the integrability tensor obeys $(A_XY,U)_{g_\lambda}=\tfrac12\,d\eta(X,Y)\cdot\lambda$, so $|A_XU|\sim\lambda$ and, with totally geodesic flat-torus fibers ($\operatorname{Ric}^F=0$),
$$
\operatorname{Ric}(U,U)=\textstyle\sum_i|A_{X_i}U|^2\sim\lambda^2\to 0,\qquad
\operatorname{Ric}(X,X)=\operatorname{Ric}^B(X,X)-2\textstyle\sum|A_XU|^2\to\operatorname{Ric}^B.
$$
The vertical Ricci runs to $0$ while horizontal Ricci stays at the base value, so $\delta_+\to 1$: **metric-distortion collapse destroys tight pinching.** To keep vertical Ricci at $+1$ while $\lambda\to0$ one would need the connection curvature to blow up like $\lambda^{-1}$, which drives horizontal Ricci to $-\infty$ through the $-2|A|^2$ term, again breaking the upper pinch.

The consequence is a clean conjecture that converts the collapse gap into two sharper statements:

> **Under $\delta_+\to 0$, positive-dimensional collapse can only be of isometric-quotient type**: the local metric is essentially undistorted (an emergent local isometric torus action), and the volume drop is carried by $|\pi_1|\to\infty$, not by local shrinking. Metric-distortion collapse (Berger, non-abelian nilmanifold fibers) is forbidden because it forces order-one Ricci anisotropy.

Non-abelian nilmanifold fibers are excluded independently: any left-invariant metric on a non-abelian nilpotent group has Ricci of mixed sign (Milnor), incompatible with $\operatorname{Ric}\approx+g$. So the only admissible fiber is a torus, and $b_1(M)=0$ forces the torus bundle to have nontrivial Euler/curvature class (Hopf-type), not a product. This is exactly the Boothby-Wang / Sasakian geometry class. The upshot: **the collapse gap reduces to understanding isometric-quotient collapse of near-Einstein manifolds along emergent torus symmetries.** Everything below is organized around this.

---

## Approach A — Noncollapse of the universal cover as the crux lemma

**Mechanism.** Pass to universal covers. Since $\operatorname{Ric}\approx+g$ lifts, $(\tilde M_i,\tilde g_i)$ are closed, simply connected, with $\delta_+\to0$, Myers diameter bound, Bishop volume ceiling. On a *simply connected* manifold there is no deck group to shorten orbits, so isometric-quotient collapse is impossible; and metric-distortion collapse is forbidden by the reframing above. Therefore:
$$
\text{(Conjectured crux lemma)}\quad \exists\,v(n)>0:\ \ M \text{ simply connected},\ \delta_+(g)\le\varepsilon(n)\ \Longrightarrow\ \operatorname{Vol}(M,g)\ge v(n).
$$
If true, $\tilde M_i$ is noncollapsed, converges in $C^{1,\alpha}$ to a simply connected positive Einstein manifold $N$ (Theorem 2's engine applied upstairs), and $\tilde M_i\cong N$ for large $i$. The entire collapse of $M_i$ is then $M_i=N/\Gamma_i$ with $|\Gamma_i|\to\infty$ — pure isometric-quotient collapse, exactly as predicted.

**What it needs.** A regularity theory for two-sided-Ricci collapse establishing that the collapse is an approximate torus fibration on which the O'Neill obstruction applies. Cheeger–Colding gives limit structure and a fibration on the regular set; Kapovitch–Wilking's generalized Margulis lemma gives virtually nilpotent local groups; Naber–Zhang $\varepsilon$-regularity gives local control under bounded Ricci. The task is to combine these so that, on a simply connected manifold, the only surviving fiber (abelian torus, undistorted) has nowhere to shrink, forcing a definite volume ratio at a definite scale.

**Where it could break down.** Without $|Rm|$ bounds the collapse fibration can be rough or singular, and the O'Neill computation is only heuristic on the regular set; the fiber could a priori be a torus that shrinks in a way not captured by the smooth model. A simply connected homogeneous counterexample would kill it — so a decisive low-cost check is to scan compact simply connected homogeneous spaces $G/H$ for families of (not necessarily invariant) metrics with $\delta_+\to0$ and $\mathrm{Vol}\to0$. The reframing predicts none exist; finding one would overturn the whole program.

---

## Approach B — Deck-group linearization and rigidity of compact group actions (resolves the rigid-limit case outright)

**Mechanism.** Granting Approach A, $M_i=\tilde M_i/\Gamma_i$ with $\tilde M_i\to(N,g_{\mathrm{Ein}})$ in $C^{1,\alpha}$ and $\Gamma_i\subset\mathrm{Isom}(\tilde g_i)$ acting freely, $|\Gamma_i|\to\infty$. By equivariant GH convergence (Fukaya–Yamaguchi), $\Gamma_i$ subconverges to a closed positive-dimensional $G\subset\mathrm{Isom}(N,g_{\mathrm{Ein}})$; $G$ contains a torus $T^k$ acting isometrically on the Einstein limit. Now use **structural stability of compact group actions**: an almost-isometric finite action that is $C^{1,\alpha}$-close to an isometric action can be averaged to an exact action (Grove–Karcher center-of-mass) and conjugated to a subgroup of $\mathrm{Isom}(g_{\mathrm{Ein}})$ (Palais, Montgomery–Zippin rigidity of nearby compact-group actions). Then $M_i=N/\Gamma_i$ carries the *exact* Einstein metric descended from $g_{\mathrm{Ein}}$, because a finite subgroup of $\mathrm{Isom}$ of an Einstein metric yields an Einstein quotient.

**What it needs.** The conjugation step is rigorous and complete when $N$ is a *rigid* Einstein space — round $S^n$, or a symmetric space where nearby compact actions are conjugate to isometric ones. This settles $P_n^+$ for every sequence whose universal-cover limit is round or symmetric. In particular any collapse whose noncollapsed cover limit is the round sphere is Einstein-compatible, with no residual analysis.

**Where it could break down.** When $N$ is a *non-symmetric* positive Einstein manifold with only a torus (not a large group) of isometries, the finite $\Gamma_i$ need not be conjugate into $\mathrm{Isom}(g_{\mathrm{Ein}})$ — they might be near it only in the collapsing directions. Then descent produces an approximately-Einstein, not exactly-Einstein, metric on $M_i$, and one must actually solve the Einstein equation on the quotient (Approach C, D, or H). This is the genuine residue, and it is exactly the Wang–Ziller torus-bundle regime discussed in the decisive test below.

---

## Approach C — Direct Einstein construction on the surviving fibration topologies (Boothby–Wang / Wang–Ziller / Bérard-Bergery)

**Mechanism.** Instead of perturbing, build Einstein metrics on the collapse-limit topologies from scratch. The reframing says the collapsing $M$ is a principal-torus bundle (or Seifert-type orbifold bundle) over a lower-dimensional positive Einstein orbifold base $B$ with nontrivial curvature class. For $k=1$ and $B$ Fano Kähler–Einstein, the Boothby–Wang circle bundle carries a Sasaki–Einstein metric — an explicit positive Einstein metric on the exact collapsing topology. For higher-rank torus bundles, Wang–Ziller give existence of Einstein metrics on principal $T^k$-bundles over products of Kähler–Einstein–Fano factors under an explicit algebraic condition on the Euler classes. If every admissible collapse total space falls into this constructible list, $P_n^+$ holds by direct existence.

**What it needs.** (i) The collapse limit $B$ must be a *smooth* (or mildly orbifold) positive Kähler–Einstein/Fano base — this requires the two-sided-Ricci collapse-limit regularity theory to output a smooth Einstein orbifold, and K-stability/Fano existence to furnish its KE metric. (ii) The bundle data must satisfy the Wang–Ziller positivity/rationality condition.

**Where it could break down.** Wang–Ziller themselves exhibit principal torus bundles admitting *no* invariant Einstein metric. If such a bundle also arises as a $\delta_+\to0$ collapse total space and admits no Einstein metric at all, this route (and $P_n^+$) breaks — see the decisive test.

---

## Approach D — Equivariant normalized Ricci flow on the universal cover with descent

**Mechanism.** Run normalized Ricci flow on $\tilde M_i$ (noncollapsed by Approach A), $\Gamma_i$-equivariantly (Ricci flow commutes with isometries, so $\Gamma_i$ stays isometric along the flow, and the flow descends to $M_i$). Starting $C^{1,\alpha}$-close to the Einstein limit $g_{\mathrm{Ein}}$, if $g_{\mathrm{Ein}}$ is a *linearly stable* fixed point of normalized Ricci flow (Ye/Kröncke dynamical stability: the Einstein operator's relevant part has the right sign, no destabilizing directions), the flow converges to an Einstein metric near $g_{\mathrm{Ein}}$, still $\Gamma_i$-invariant, descending to an Einstein metric on $M_i$. Perelman's $\kappa$-noncollapsing and monotonicity of $\lambda$/$\nu$-entropy provide the scale-invariant control that classical short-time estimates lack.

**What it needs.** Dynamical stability of the limit Einstein metric under normalized Ricci flow modulo the moduli of Einstein deformations, and equivariance preservation (automatic). This turns "near-Einstein $\Rightarrow$ Einstein" into a convergence theorem rather than an implicit-function argument.

**Where it could break down.** Positive Einstein metrics are frequently *unstable* under Ricci flow (the round sphere is stable, but many Fano KE and homogeneous Einstein metrics are not). On an unstable limit the flow can run away from $g_{\mathrm{Ein}}$ — though it might still converge to a *different* Einstein metric, which is enough for existence. The real pressure point: whether short-time flow even exists uniformly when $|Rm|$ is unbounded (curvature concentration in the pre-limit). Working upstairs on the noncollapsed cover, where $|Rm|$ is controlled by the $C^{1,\alpha}$ convergence, sidesteps this.

---

## Approach E — Synthetic "two-sided-Ricci" (Einstein-RCD) limit and lifting

**Mechanism.** Independently of smooth fibration, $\delta_+\to0$ gives measured-GH limits that are $\mathrm{RCD}(n-1,n)$ spaces, and the *two-sided* pinch should force a synthetic Einstein rigidity: the limit is an "Einstein RCD" space. Recent structure theory (Mondino–Naber rectifiability, Brué–Naber–Semola on the structure of RCD spaces, Honda's spectral convergence) should upgrade a two-sided-pinched collapse limit to a *smooth* Einstein orbifold $X^k$ of dimension $k<n$, with the collapse realized as a submetry $M_i\to X$ whose fibers carry the emergent torus symmetry. The topology of $M_i$ is reconstructed as a torus bundle over $X$, feeding Approach C.

**What it needs.** A regularity theorem: two-sided synthetic Ricci bounds on a (dimension-dropping) collapse limit imply smooth Einstein orbifold structure. This is stronger than current one-sided RCD structure theory but is the natural synthetic analogue of the smooth two-sided-Ricci regularity (Cheeger–Naber codimension-4). The advantage over Approach A is that RCD produces the fibration/base without assuming smoothness of the collapse a priori.

**Where it could break down.** The synthetic Einstein rigidity for *collapsed* limits is not established; measures renormalize and the "dimension" is the essential/Hausdorff dimension of the limit, and matching the fiber structure to the measure decomposition is unproven. This is a genuine research frontier, valuable precisely because success would handle all dimensions uniformly.

---

## Approach F — Curvature-concentration bubble accounting in dimension 4, generalized by the Pfaffian in even dimension

**Mechanism.** In dim 4, CGB forces $\int|W|^2\to 8\pi^2\chi$ under $\delta_+\to0$, $\mathrm{Vol}\to0$: all curvature energy concentrates in the Weyl tensor at concentration points. Rescaling at those points, $\operatorname{Ric}\to0$, so the bubbles are Ricci-flat ALE/ALF spaces — hyperkähler gravitational instantons, classified (Kronheimer) as resolutions of $\mathbb C^2/\Gamma$. The pre-limit topology is then base (collapse limit) plus glued hyperkähler bubbles: a resolution of a positive Einstein orbifold. On the positive branch, positive scalar curvature is automatic, so the Seiberg–Witten obstruction that blocks Einstein metrics in the LeBrun general-type constructions is *absent* — Fano/KE existence is available, and the resolved space is typically Einstein (Fubini–Study, Page, Chen–LeBrun–Weber lie exactly here). In even dimension $2m$, the Gauss–Bonnet–Chern integrand is the Pfaffian of curvature; tight pinching bounds its "Ricci part," forcing the "Weyl part" to concentrate, with an analogous (less completely classified) bubble tree.

**What it needs.** The quantized-energy bubble-tree decomposition under *bounded Ricci* collapse (Anderson–Bando–Kasue–Nakajima and Cheeger–Naber-type accounting), together with the statement that every resolution of a positive Einstein orbifold arising this way admits an Einstein metric — a Fano/K-stability existence input.

**Where it could break down.** The bubble-tree theory is cleanest for *noncollapsed* Einstein limits; adapting it to genuinely collapsing near-Einstein sequences with $|Rm|\to\infty$ is delicate, and matching the bubble neck to preserve *unweighted* pointwise Ricci pinching (not merely $L^p$-small residual, per the Ozuch/Morteza–Viaclovsky scaling analysis already in the notes) is the same hard gluing issue that blocks the minus-branch constructions. But here the direction is favorable: one wants existence, and PSC removes the main obstruction.

---

## Approach G — Emergent Killing fields from tight pinching (Bochner rigidity)

**Mechanism.** Rather than importing symmetry from limits, produce it directly. On $\operatorname{Ric}\approx\lambda g$, the collapsing short directions correspond to small eigenvalues of the connection/Hodge Laplacian. The Bochner identity $\Delta_H\alpha=\nabla^*\nabla\alpha+\operatorname{Ric}(\alpha)$ and the Einstein Killing equation ($X$ Killing on $\operatorname{Ric}=\lambda g$ $\Leftrightarrow$ $\Delta X=-\lambda X$, $\operatorname{div}X=0$) suggest that under $\delta_+\to0$ the collapsing directions become *almost-Killing* fields with quantitatively small deviation. A rigidity/quantization theorem would upgrade these to *exact* Killing fields of a nearby metric, producing a genuine $T^k$ isometric action on $M_i$ for large $i$. One then reduces to the cohomogeneity-$(n-k)$ Einstein problem — an ODE/algebraic system on the orbit space, frequently solvable explicitly, and where invariant existence results (Böhm, Wang–Ziller) apply.

**What it needs.** A pinching-to-Killing estimate: $\delta_+\le\varepsilon$ plus collapse produces fields with $\|\mathcal L_Xg\|$ controlled by $\varepsilon$ and the collapse scale, and a mechanism (averaging over the emergent torus, then solving the invariant Einstein equation) to reach an exact solution.

**Where it could break down.** Almost-Killing does not imply Killing without a spectral gap that could close under collapse; the emergent torus can have fixed-point sets (orbifold singularities) where the reduction degenerates; and an invariant metric produced by averaging need not be Einstein — one still solves the reduced equation, which can be obstructed.

---

## Approach H — Koiso integrability / implicit function theorem around the limit Einstein metric

**Mechanism.** Treat $\tilde g_i$ as an approximate zero of the (gauge-fixed) Einstein operator near $g_{\mathrm{Ein}}$. If $g_{\mathrm{Ein}}$ is infinitesimally rigid (the Lichnerowicz Laplacian on transverse-traceless tensors has no kernel modulo the moduli, i.e., Einstein deformations are unobstructed and isolated), the implicit function theorem produces an exact Einstein metric near $\tilde g_i$, done $\Gamma_i$-equivariantly and descended to $M_i$. This is the positive-branch analogue of Min-Oo's minus-branch stability, but built on the noncollapsed cover so that the required elliptic estimates hold with constants from the $C^{1,\alpha}$ limit rather than from an uncontrolled $d^2\max|K|$.

**What it needs.** Invertibility of the linearized gauged Einstein operator at $g_{\mathrm{Ein}}$ modulo the Einstein moduli, i.e., integrability of infinitesimal Einstein deformations (Koiso's theory). For rigid limits (round sphere, $\mathbb{CP}^n$ Fubini–Study, many symmetric spaces) this holds.

**Where it could break down.** Non-integrable or obstructed Einstein deformations (Koiso's examples exist) invalidate the naive IFT; then one needs a Kuranishi/finite-dimensional reduction, and the approximate solution must project into the unobstructed part of moduli.

---

## The decisive alternative: $P_n^+$ could be false — the sharpest test

The generator should keep this space open. The one scenario that would refute $P_n^+$ is a $\delta_+\to0$ sequence whose (post-reduction) total space is a torus bundle over a Fano/KE base that admits **no Einstein metric at all**. Wang–Ziller exhibited principal torus bundles carrying **no invariant** Einstein metric. The decisive, relatively low-cost computation is:

1. Take a Wang–Ziller torus bundle $M$ with no invariant Einstein metric over a product of Fano KE bases. Compute, over the space of *natural* (submersion/Kaluza–Klein) metrics with shrinking fibers, the infimum of $\delta_+$. If $\inf_g\delta_+(g)=0$ is achievable along a collapsing family (fibers shrunk while horizontal curvature is tuned), $M$ is a candidate collapse input.
2. Determine whether $M$ admits *any* Einstein metric (not just invariant). If it provably admits none, and step 1 gives $\delta_+\to0$, then $P_n^+$ is false in that dimension — a strict refutation of the whole proposition's positive-branch, forcing the full problem to be decided by whether the minus branch can also be defeated on the same manifold.

The reframing predicts step 1 fails (shrinking the fiber metrically breaks pinching via the O'Neill mechanism, so $\inf\delta_+>0$ on non-isometric-quotient families, and $M$ has finite $\pi_1$ so no isometric-quotient route). If that prediction holds for all Wang–Ziller no-invariant-Einstein bundles, it is strong evidence for $P_n^+$; if a single bundle achieves $\delta_+\to0$ by some non-obvious (non-invariant) family, it is the counterexample. This single computation — comparing "which torus bundles can be tightly Ricci-pinched" against "which torus bundles are Einstein" — is the highest-value experiment in the entire positive-branch program, because it directly tests whether the isometric-quotient/metric-distortion dichotomy is the *complete* story of tightly-pinched collapse.

---

## Source families worth targeting in ordinary language

Equivariant Gromov–Hausdorff convergence and structural stability of compact group actions (Fukaya–Yamaguchi; Grove–Karcher center-of-mass; Palais/Montgomery–Zippin conjugacy of nearby actions) for Approach B. Generalized Margulis lemma under Ricci lower bounds (Kapovitch–Wilking) and $\varepsilon$-regularity for collapsed bounded-Ricci spaces (Naber–Zhang) for Approaches A and E. Existence of Einstein metrics on principal torus bundles (Wang–Ziller; Boothby–Wang / Sasaki–Einstein over Fano KE; Bérard-Bergery) for Approaches C and the decisive test — including the explicit Wang–Ziller examples lacking invariant Einstein metrics. Dynamical stability of Einstein metrics under normalized Ricci flow (Ye; Kröncke) and Perelman entropy monotonicity for Approach D. RCD structure theory (Mondino–Naber; Brué–Naber–Semola; Honda spectral convergence) for Approach E. Hyperkähler ALE classification (Kronheimer) and bounded-Ricci bubble accounting (Anderson–Bando–Kasue–Nakajima; Cheeger–Naber codimension-4) for Approach F. Koiso's infinitesimal Einstein deformation and integrability theory for Approach H.