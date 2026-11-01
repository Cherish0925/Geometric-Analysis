# TTCS Independent Branch Record

```json
{
  "step_id": 7,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step7_local_vs_global_rigidity.md",
    "Sessions/S0910A01/workspace/notes/step5_curvature_ratio_and_rigidity.md",
    "Sessions/S0910A01/workspace/notes/step4_near_equality_and_boundary_calibration.md"
  ]
}
```

## Task

For Yau Problem 26 (negative branch, dimension 4): we have established that a hypothetical near-pinching sequence on LeBrun blow-ups M_i = X#k_i C̄P² with δ_i→0 and k_i/A_i→1/3 satisfies:
- ∫(s+8√6|W+|)² ≤ 864π²D_a with D_a/A→0
- The local analysis on smooth Einstein pointed limits gives conformally Kähler geometry, but this does NOT contradict the calibrated Weyl profile locally
- The argument is inherently global: on compact manifolds, Stokes forces the conformal factor to be constant, giving a Kähler contradiction

The gap: making the global argument quantitative on the original compact M_i. The obstacles:
(a) The Taubes exceptional-sphere area argument requires an exact symplectic structure, not an approximate one
(b) The SW spinor defines an approximate almost-Kähler form, but dω_i ≠ 0 in general
(c) The Gromov energy quantum may degenerate as the geometry degenerates

Generate promising approaches to close this gap. Consider:
- Direct quantitative versions of LeBrun's equality exclusion (Prop 3.2) that work for near-equality
- Integer-invariant stability arguments (c₁·E_j is topological, independent of metric)
- Ricci flow approaches starting from the near-Einstein metric
- Chern-Weil identities that constrain the exceptional class areas from below
- Alternative global mechanisms that don't pass through symplectic geometry
- Whether the problem admits a counterexample construction instead

Which approach has the best chance of resolving the negative branch, and what specific mathematical steps would be needed?

## Output

## Reframing that sharpens where the real difficulty sits

Two structural points change how I read the whole program.

**The universal constants may be chosen tight, so the target is a fixed pinching band, not a limit.** Yau 26 asks only for the *existence* of some $c_n<C_n$. Choosing a tight band around $-1$, say $c_4 g\le \operatorname{Ric}\le C_4 g$ with $c_4=-(1+\delta_4),\,C_4=-(1-\delta_4)$, gives a valid instance: the band itself pins $\operatorname{Ric}$ pointwise within $\delta_4$ of $-g$, no rescaling needed. So the Ric$\approx-g$ statement to prove is: *there exists a fixed $\delta_4>0$ such that any closed $M^4$ carrying a metric with $|\operatorname{Ric}+g|\le\delta_4$ admits an Einstein metric.* Its negation is exactly a sequence $(M_i,g_i)$ with $M_i$ Einstein-free and $\delta_i\to0$. The $\delta\to0$ analysis in the step notes is therefore not an artifact — it is the precise content.

**The functional deficit $D_a$ can be driven to zero on blow-ups without any pinching, so the fight localizes to the cores.** LeBrun's $I(g)\ge\tfrac23(a^+)^2$ has the same infimum on $X$ and on $X\#k\overline{\mathbb{CP}}^2$ (birational invariance of the curvature functional): one spreads exceptional curvature thinly. Metrics achieving $D_a/A\to0$ therefore already exist on Einstein-free blow-ups — but they do so by forming thin high-curvature cores where $|\operatorname{Ric}+g|=O(1)$. The pinching hypothesis forbids exactly those cores. So the entire question is:

> *Can the exceptional topology (a $-1$ class) be supported in a region while $|\operatorname{Ric}+g|\le\delta$ there, uniformly as $\delta\to0$?*

This localization is more useful than the cohomological pairing, because at the level of cohomology the near-equality is fully self-consistent: $[\omega_i]$ is (approximately) self-dual, $[\omega_i]\cdot E_j=\langle[\omega_i],E_j^+\rangle$, and $(1/A)\sum_j(E_j^+)^2\to0$ only *upper*-bounds these pairings. No lower bound, hence no tension, lives in cohomology. The tension is between the topological pairing $\approx 0$ and the *area of an actual (pseudo)holomorphic representative* $\ge\hbar$. That is where the symplectic route stalls, and it is worth abandoning cohomological bookkeeping for a geometric mechanism at the cores.

## Leading approach: the gravitational-instanton parity obstruction

This is the strongest and most original mechanism I can offer, and it bypasses symplectic geometry entirely.

Take an Einstein-free $M_i=X\#k_i\overline{\mathbb{CP}}^2$ (fixed $M$ first) with $|\operatorname{Ric}+g_i|\le\delta_i\to0$. Since $|\operatorname{Ric}_{g_i}|\le 1+\delta_i\le 2$ is uniformly bounded and $\int|W|^2$ is bounded by $\chi,\tau$ and the volume (via Chern–Gauss–Bonnet plus signature), the sequence falls under Anderson–Cheeger–Naber codimension-four theory. Where curvature does not concentrate and volume does not collapse, one gets $C^{1,\alpha}$/harmonic-radius control and, by the $W^{2,p}$ bootstrap already in Step 7, a smooth Einstein limit; where curvature concentrates, rescaling by $\lambda_i\to\infty$ at the concentration point gives $\operatorname{Ric}=\lambda_i^{-2}(\approx-g)\to0$, so the pointed limit is a **complete Ricci-flat ALE/ALF space** (a gravitational instanton). The smooth compact part limits to a **compact Einstein orbifold** with isolated singular points.

Now track where the class $E_j$ (with $E_j^2=-1$) can go. By Mayer–Vietoris across the small-topology necks (Anderson bubbling), $E_j$ is carried either by the compact orbifold limit or by a bubble. This produces a trichotomy in which every branch meets an obstruction:

**(a) $E_j$ survives to the compact Einstein orbifold limit.** The orbifold is compact, so the global Stokes step in Step 7 §2 applies verbatim: the calibrated profile forces locally conformally Kähler with $\Delta f=-f/2$, integration over the compact orbifold forces $f\equiv$ const, hence Kähler–Einstein, hence $|W^+|^2=s^2/24=2/3$. But the curvature-ratio remainder forces $|W^+|^2\to 1/24$. These disagree — the same contradiction that excludes smooth limits, now available on orbifolds because compactness restores Stokes. This is exactly the compact/noncompact wall of Step 7, and orbifold limits fall on the *compact* side.

**(b) $E_j$ is carried by a bubble.** The bubble is a complete Ricci-flat gravitational instanton containing an embedded $-1$ sphere. This cannot happen:
- The intersection lattices of Ricci-flat ALE spaces (Kronheimer's ADE hyperkähler resolutions; Bando–Kasue–Nakajima) are the ADE root lattices — **even**. Multi-Taub-NUT ($A_k$) and Cherkis–Hitchin ($D_k$) ALF instantons likewise carry only $-2$ spheres and even forms. A $-1$ sphere has odd self-intersection and cannot embed in an even lattice.
- For the specific blow-up bubble the argument is even sharper: $\mathrm{Bl}_0\mathbb{C}^2=\mathcal{O}(-1)$ is asymptotic to $\mathbb{R}^4$ ($S^3$ at infinity, trivial group), and a Ricci-flat ALE metric asymptotic to $\mathbb{R}^4$ is flat by the BKN/positive-mass rigidity — but $\mathcal{O}(-1)\ne\mathbb{R}^4$ (it has $H^2=\mathbb{Z}$). So **no Ricci-flat ALE metric supports a $-1$ curve at all.**

Hence curvature cannot concentrate along an exceptional $-1$ class: parity of self-intersection is preserved under bubbling, but Ricci-flat instantons carry only even classes.

**(c) The region collapses.** Handled by the classification below.

This trichotomy is a nearly complete argument for a *fixed* Einstein-free blow-up. The pieces that need to be made airtight, and the exact input each requires:
1. **Neck topology / parity conservation** — that $E_j$'s self-intersection is genuinely inherited by whichever piece absorbs it (Anderson–Cheeger–Naber neck analysis; the odd/even splitting of the intersection form under connected-sum-at-infinity of instantons).
2. **Orbifold conformally-Kähler rigidity** — the Derdziński/Armstrong statement extended to compact Einstein orbifolds with the two-eigenvalue $W^+$ profile. This is a genuine but plausible extension: Stokes and the maximum principle survive on orbifolds with isolated quotient singularities.
3. **Even-form persistence for ALF/ALG limits** — confirm that collapsed (lower-volume-growth) Ricci-flat limits also exclude $-1$ classes. Search: Cherkis–Kapustin, Cherkis–Hitchin ALF $D_k$; Chen–Chen ALG/ALH classification; Minerbe multi-Taub-NUT rigidity.

The decisive character of this route: it replaces the fragile Gromov energy quantum (which degenerates precisely inside bubbles) with a **discrete parity invariant that cannot degenerate**. The energy quantum vanishing in a shrinking bubble is real, but the parity of the bubble's intersection form is not something a limit can smear.

## Cleanest immediate closure: the collapse classification

The collapsing branch is a finite, exact computation and should close quickly.

Under $\operatorname{Ric}\approx-g$ and volume collapse with bounded curvature, Cheeger–Fukaya–Gromov / Naber–Tian give an $\mathcal{N}$-structure and a lower-dimensional Einstein-type quotient; the local model along the collapsing fibers is a homogeneous or nil/solv geometry. The calibrated filter is decisive because:
- **Every homogeneous Einstein $4$-space with $\operatorname{Ric}=-g$ is symmetric**: $\mathbb{R}H^4$ (with $W^+=0$) or $\mathbb{C}H^2$ (with $|W^+|^2=2/3$). Neither equals the target $|W^+|^2=1/24$.
- The known collapse models ($\Sigma_g\times\Sigma_{g'}$ with a degenerating factor, $\mathbb{C}H^2$ quotients, Sol/Nil-fibered mapping tori) all return Weyl norms in $\{0,\,2/\sqrt6\}$, none near $1/(2\sqrt6)$ (S0910A03's check).

The concrete program: enumerate the $4$-dimensional Thurston/Bianchi geometries admitting an $\operatorname{Ric}=-g$ scaling limit compatible with an $\mathcal{N}$-structure, compute $|W^+|$ and the $W^+$-eigenvalue triple exactly for each (these are homogeneous, so closed-form), and confirm none realizes the two-eigenvalue profile $(-1/6,1/12,1/12)$ with $|\nabla W^+|^2=1/24$. Because $|\nabla W^+|^2=1/24>0$, the profile is *not* locally symmetric, so it cannot be any homogeneous collapse model at all — this single Bochner value may kill the entire homogeneous branch in one line, leaving only genuinely inhomogeneous collapse to check against the local conformally-Kähler constraint $\Delta f=-f/2$ with an oscillating $f$ along the collapse direction.

## Why the symplectic/integer-invariant routes are the weakest as stand-alones

I would not stake the resolution on making Taubes quantitative.

- **Taming positivity needs an actual $J$-curve.** $\int_{\Sigma_j}\omega_i\ge (1-o(1))\,\mathrm{area}(\Sigma_j)$ holds only if $\Sigma_j$ is (near-)$J_i$-holomorphic; producing such a representative in class $E_j$ is Taubes' theorem, which needs a genuine symplectic form. The approximate $\omega_i$ has $\|d\omega_i\|_{L^2}=O(\sqrt{D_a})\to0$, but Moser stability does not upgrade a small $L^2$ closedness defect to an exact symplectic form when curvature concentrates.
- **The integer-invariant pairing needs anti-self-dual curvature control it does not have.** $\int_{E_j}F_A/2\pi=c_1(L)\cdot E_j=1$ is topological, but splitting $F_A=F_A^++F_A^-$ shows the useful $F_A^+$ (aligned with $\omega_i$) is only recovered if $\int_{E_j}F_A^-$ is small, and the SW estimate leaves $F_A^-$ free. So the "stable integer" does not by itself pin the geometric area.
- **The energy quantum degenerates exactly where the topology hides.** Gromov monotonicity $\hbar\gtrsim 1/\sup|\mathrm{curv}|$ collapses in the bubble carrying $E_j$. This is not a technicality — it is the same phenomenon the parity obstruction handles cleanly.

If the symplectic route is used at all, it should be confined to the noncollapsed non-bubbling part (where $J_i$ converges), realized through the SW spinor zero-set as a $J$-holomorphic current with monotonicity taken away from concentration — and even there the orbifold-Armstrong argument of route (a) is more direct.

## The genuine frontier: uniformity as topology grows, and the fixed-scale AdS-cap scenario

The trichotomy above, if completed, shows each *fixed* Einstein-free blow-up has its own $\delta(M)>0$. Yau 26 needs $\inf_M\delta(M)>0$. The uniformity is tested by sequences with $A_i\to\infty$, $k_i\sim A_i/3$, i.e. **many exceptional cores at once**. Here one scenario is not yet obstructed by anything above:

*Assemble $k_i$ fixed-scale $\operatorname{Ric}=-g$ caps of Taub–Bolt–AdS type (bounded curvature, definite volume — so no bubble forms and the parity obstruction is silent) into a calibrated-profile bulk, with the transition Ricci deviation $\to0$.*

The step-4 calibration already shows these caps exist as *exact* $\operatorname{Ric}=-g$ fillings of $\mathcal{O}(-1)$. The two decisive computations that would settle truth versus falsity of the $\lambda<0$ regime:

1. **Cap–neck matching.** The $U(2)$-invariant $\operatorname{Ric}=-g$ caps (Taub–Bolt/Taub–NUT–AdS, the full cohomogeneity-one family) present a *squashed* Berger $S^3$ collar with $b/a\lesssim0.4$, never round. A geodesic sphere in a calibrated-profile bulk is nearly round ($b/a\approx1$). Determine whether the squashing can be interpolated to round over a collar while holding $|\operatorname{Ric}+g|\to0$ — i.e. whether an unsquashing transition incurs an irreducible Ricci deviation. A linearized-Einstein obstruction computation on the collar (the cokernel of $\operatorname{Ric}'+g$ acting on $U(2)$-invariant collar deformations, with fixed cap-side and round bulk-side data) would decide this. A nonzero obstruction that is bounded below independent of the cap parameter closes the scenario and yields the uniform $\delta_4$; a vanishing obstruction is a concrete route toward a construction.
2. **Existence of a complete calibrated model.** Whether a *complete* (no conformal infinity, since it must arise as a pointed limit of closed manifolds) $\operatorname{Ric}=-g$ $4$-manifold with the two-eigenvalue profile $|W^+|^2=1/24$, $|\nabla W^+|^2=1/24$, locally conformally Kähler with oscillating $f$, and carrying a $-1$ class, can exist. If none exists, the many-cap assembly has no target to converge to and the uniform constant follows; if one exists, it is the seed of a counterexample.

I would run both from the two sides at once — the same computation that obstructs the construction proves the theorem, and its sign is what is actually unknown.

## Ranking and the single most informative next step

Best chance to resolve the $\operatorname{Ric}\approx-g$ regime: the **gravitational-instanton parity obstruction** (route b) combined with **orbifold conformally-Kähler rigidity** (route a) and the **collapse classification** (route c). Together they close the *fixed-manifold* statement without symplectic geometry, converting the degenerate Taubes area into a non-degenerate parity invariant. The symplectic/integer routes are backups at best.

The single computation that would most change the judgment is the **collar unsquashing obstruction** for $\operatorname{Ric}=-g$ caps (frontier item 1): it is the one place where a bounded-geometry, non-bubbling, non-collapsing counterexample could still live, and it is a finite linearized-operator cokernel computation on a cohomogeneity-one collar — cheap relative to its power to decide uniformity, hence truth or falsity of the whole $\lambda<0$ regime. Its outcome distinguishes: a bounded-below obstruction $\Rightarrow$ uniform $\delta_4$ and a proof; a vanishing obstruction $\Rightarrow$ explicit many-cap construction and refutation.

Supporting literature to pull (named topics, not invented): Bando–Kasue–Nakajima decay/rigidity of ALE Einstein $4$-manifolds; Kronheimer ALE hyperkähler classification and ADE lattices; Anderson and Cheeger–Naber $\varepsilon$-regularity and orbifold-limit bubbling under bounded Ricci; Naber–Tian collapse with bounded Ricci and $\mathcal{N}$-structures; Cherkis–Hitchin / Cherkis–Kapustin ALF $D_k$ and Chen–Chen ALG/ALH gravitational-instanton classification; Derdziński and Apostolov–Armstrong–Drăghici conformally-Kähler/almost-Kähler rigidity (for the orbifold extension); Akbar–Woolgar Taub–Bolt–AdS cohomogeneity-one families (for the collar computation).