# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/briefing/aligned_research_goal.md",
    "Skills/qiushi-yau26/references/research/20260910.tex",
    "Sessions/S0910A03/staging/acquired/arXiv_2505_08384v1__math_DG__13_May_2025_0074baa44fdc638a/part_001.md"
  ]
}
```

## Task

Seek high-value routes to the full Yau 26 problem beyond local stability. Compare (i) a global uniform-gap theorem modulo degeneration, (ii) flexibility/convex-integration constructions for Ricci tensor, (iii) orbifold/ALE smoothing counterexamples, and (iv) topological operations/products that transfer one branch failure to the other in the same dimension. Work explicitly with P_n^+ or P_n^- and the requirement that a counterexample manifold exclude every Einstein metric of every sign. Generate precise candidate lemmas or constructions, explain why each could cross the central gap, and test likely contradictions from Chern–Weil, Myers, Bochner, simplicial volume, spin/index, Seiberg–Witten, or products.

## Output

For fixed \(n\), write
\[
P_n^\sigma:\quad \exists \varepsilon_n^\sigma>0\ \text{such that}\ 
\delta_\sigma(g)\le \varepsilon_n^\sigma \Rightarrow \Ein(M)\ne\varnothing,
\qquad \sigma=\pm1 .
\]
A counterexample to \(P_n^\sigma\) is not just an almost \(\sigma\)-Einstein metric; it requires a closed smooth \(M^n\) with \(\Ein(M)=\varnothing\), meaning no Einstein metric with \(\lambda>0\), \(\lambda=0\), or \(\lambda<0\). This all-sign exclusion is the central bottleneck in every counterexample route.

A useful asymmetry is already visible:

- \(P_n^+\): \(\Ric_g\ge(1-\varepsilon)g\) gives Myers diameter control, finite \(\pi_1\), \(b_1=0\), positive scalar curvature, and in dimension four the strict Chern–Weil consequence
  \[
  2\chi(M)>3|\tau(M)|.
  \]
  Thus plus-branch counterexamples cannot use enlargeability, spin index, ordinary Seiberg–Witten monopole classes, positive simplicial volume, infinite \(\pi_1\), or Hitchin–Thorpe equality/violation as their all-sign obstruction, because those either forbid the input metric itself or are contradicted by tight plus pinching.

- \(P_n^-\): \(\Ric_g\approx -g\) has no Myers compactness. Volume and diameter may diverge, so integral topological obstructions can be diluted. This makes the minus branch much more compatible with LeBrun-type four-dimensional no-Einstein mechanisms and with Lohkamp-style Ricci flexibility.

## (i) Global uniform gap modulo degeneration

A high-value proof route for \(P_n^+\) is an equivariant degeneration theorem rather than local stability near a fixed Einstein metric.

**Candidate lemma U\(_+\): equivariant positive degeneration absorption.**  
There exist \(\varepsilon(n),v(n)>0\) such that if \(\delta_+(g_i)\to0\), then after lifting to universal covers and passing to finite deck groups, every collapsing or singular degeneration is modeled by one of the following:
1. finite quotient collapse of a smooth Einstein cover;
2. orbifold Einstein degeneration with smoothable local models;
3. a Ricci-flat bubble tree whose topological energy contribution is incompatible with \(\delta_+(g_i)\to0\) unless the corresponding smoothing actually carries an Einstein metric.

The output should be an Einstein metric on the original quotient, not only on a cover. Since the lifted input metric is deck-invariant, the DeTurck or variational correction can be run in deck-invariant tensor spaces if the estimates are made on the cover.

Why this crosses the central gap: it would convert “almost plus-Einstein” into either an actual Einstein metric or a topological contradiction. It also handles lens-space type collapse correctly: the base may collapse, but the cover is round and the quotient metric descends.

Tests and likely mechanisms:

- **Myers/Bochner.** Any plus degeneration with local torus or nilpotent directions should produce almost parallel \(1\)-forms on suitable local covers. A Bochner estimate with \(\Ric\ge(1-\varepsilon)g\) should suppress such forms unless the collapse is finite-quotient collapse.
- **Four-dimensional Chern–Weil.** For \(\delta_+(g)\le\varepsilon\),
  \[
  2\chi\pm3\tau
  \ge
  \frac{\Vol_g(M)}{4\pi^2}
  \left[\frac23(1-\varepsilon)^2-2\varepsilon^2\right].
  \]
  Thus any plus counterexample must lie strictly inside the Hitchin–Thorpe chamber. Resolutions sitting on the wall, e.g. rational surfaces at equality, cannot produce \(\delta_+\to0\).
- **Finite group collapse.** Spherical space forms show injectivity radius and volume of the base are irrelevant; the equivariant cover is the right object.
- **Singular Fano/orbifold models.** Positive Einstein orbifold degenerations occur in complex geometry. The desired theorem must not rule them out; it must either find the known smooth Einstein metrics on resolutions or identify a topological energy obstruction to tight pinching.

For \(P_n^-\), the analogous global gap theorem is structurally weaker because volume can diverge. A four-dimensional LeBrun obstruction gives an integral lower bound for the trace-free Ricci energy of an exact Einstein candidate, but if normalized volume grows, a pointwise bound \(|E|\le\varepsilon\) only gives
\[
\int |E|^2\,dV \le C\varepsilon^2\Vol(M,g),
\]
so a fixed topological obstruction can coexist with \(\varepsilon\to0\) when \(\Vol\to\infty\). This is the main reason the minus branch is a natural counterexample target.

## (ii) Ricci flexibility and mixed convex integration

The scalar mixed convex integration paper is directly relevant as a model, but full Ricci is much more rigid at the principal-symbol level.

For the Ricci operator at a flat background,
\[
(D\Ric)(h)_{ij}
=
\frac12\bigl(
-\Delta h_{ij}-\partial_i\partial_j\tr h
+\partial_i(\operatorname{div}h)_j+\partial_j(\operatorname{div}h)_i
\bigr).
\]
For a rank-one phase \(\theta\), the principal symbol has image only in tensors transverse to \(\theta\), and its kernel is essentially the pure-gauge symbol \(h=\theta\odot v\). Therefore a scalar-curvature corrugation that cancels only the trace-level \(O(N)\) term will generally leave \(O(N)\) Ricci components. A full Ricci construction must use gauge-kernel first oscillations plus second-order corrections, and the decisive object is the averaged quadratic Ricci cone generated by those oscillations.

**Candidate calculation C: Ricci corrugation cone.**  
On \(\mathbb R^n\), take
\[
g_N=g_0+\frac1N\gamma(x,N\theta\cdot x)+\frac1{N^2}\delta(x,N\theta\cdot x),
\]
with \(\gamma\) in the Ricci-symbol kernel for direction \(\theta\), zero phase average, and \(\delta\) chosen to cancel the remaining affine second-order part. Compute the phase-averaged \(O(1)\) Ricci increment
\[
\mathcal Q_\theta(\gamma,\delta)
\]
and its convex hull over finitely many directions \(\theta_\alpha\). The key question is whether \(-\operatorname{Id}\) lies in the interior of the generated cone, while \(+\operatorname{Id}\) likely does not.

A simple one-phase warped-product computation already predicts the sign asymmetry. For
\[
g=dt^2+G_{ab}(t)dy^ady^b,\qquad K=\frac12G^{-1}G',
\]
one has schematically
\[
\Ric_{tt}=-\operatorname{tr}K'-\operatorname{tr}(K^2),
\]
so the phase average in the oscillation direction is
\[
\langle \Ric_{tt}\rangle=-\langle \operatorname{tr}(K^2)\rangle\le0.
\]
This is exactly the Lohkamp-type direction: oscillations naturally push Ricci downward. It explains why a minus-branch flexibility theorem is plausible, while a plus-branch one would have to overcome Myers and global topology.

**Candidate lemma R\(_-\): isotropic Lohkamp theorem.**  
For every closed smooth \(M^n\), \(n\ge3\), every background metric \(g_0\), and every \(L\to\infty\), there are smooth metrics \(g_L\) such that
\[
\|\Ric_{g_L}+L g_L\|_{g_L,\op}\le \eta(L)L,
\qquad \eta(L)\to0.
\]
Then \(\bar g_L=L g_L\) satisfies
\[
\delta_-(\bar g_L)\le\eta(L).
\]

Why this crosses the central gap: if one chooses a four-manifold \(M\) already known by LeBrun-type Seiberg–Witten curvature inequalities to admit no Einstein metric of any sign, then R\(_-\) gives a direct counterexample sequence to \(P_4^-\). The normalized volumes grow like \(L^{n/2}\), so four-dimensional integral obstructions are not contradicted.

A concrete four-dimensional target family is:
\[
M=X\# k\,\overline{\mathbb{CP}}^{\,2},
\]
where \(X\) is a minimal complex surface of general type with \(b_2^+>1\), and \(k\) is chosen in the LeBrun no-Einstein range while keeping \(2\chi>3|\tau|\). Such \(M\) cannot serve the plus branch because monopole methods also obstruct positive scalar curvature, but it is well aligned with \(P_4^-\).

For \(P_n^+\), an analogous high-frequency local theorem would imply \(\Ric\approx +L g\) before rescaling. Myers would force diameter \(O(L^{-1/2})\). Thus any plus flexibility mechanism must be global from the start and restricted to finite-\(\pi_1\), positive-scalar-compatible topologies. It cannot be a direct Lohkamp analogue on arbitrary manifolds.

## (iii) Orbifold/ALE smoothing counterexamples

The strongest orbifold route is not “weighted residual small near a tiny bubble”; the original problem uses uniform operator pinching. A raw Ricci-flat ALE core has Ricci operator \(0\), so it is not uniformly close to \(\pm\operatorname{Id}\). The local model must be corrected at the bubble scale.

**Candidate lemma O\(_\sigma\): cosmological ALE cap.**  
Let \(Y\) be a Ricci-flat ALE resolution of \(\mathbb R^4/\Gamma\). For small \(t\), construct on a truncated region a metric \(h_t\) satisfying
\[
\Ric_{h_t}=t^2\sigma h_t+O(t^q)
\]
in unweighted operator norm on the ALE scale, with asymptotics matching the order-\(t\) expansion of a \(\sigma\)-Einstein orbifold metric near the singular point. Then \(g_t=t^2h_t\) has
\[
\Ric_{g_t}=\sigma g_t+O(t^q)
\]
in the normalized operator sense.

This removes the common core-residual problem: after scaling back, the cap can be uniformly almost \(\sigma\)-Einstein.

However, local nonexistence near a singular Einstein orbifold is not enough for a Yau 26 counterexample. One still needs \(\Ein(M)=\varnothing\) globally.

Two ways such a construction could become decisive:

1. **Topological all-sign exclusion plus approximate smoothing.**  
   Find compact Einstein orbifolds \(O_j\) with ALE-resolvable singularities such that their smooth resolutions \(M_j\) satisfy a LeBrun-type theorem excluding all Einstein metrics, while cosmological ALE caps give \(\delta_-(g_j)\to0\).  
   Chern–Weil compatibility demands either large normalized volume or an obstruction margin tending to zero relative to volume. Large covers of orbifolds with only controlled local surgery are especially attractive.

2. **Global pinning to the singular model.**  
   Prove that any Einstein metric on \(M_j\), after scaling if \(\lambda<0\), must converge to the same orbifold \(O_j\). Then Biquard/Ozuch/Yao local nonexistence near the singularity excludes all Einstein metrics.  
   This needs strong input beyond local gluing: simplicial volume or Besson–Courtois–Gallot entropy could exclude \(\lambda\ge0\) and force \(\lambda<0\) candidates toward the locally symmetric orbifold, but one also needs an upper control or equality mechanism preventing a far-away large-volume Einstein metric.

For plus-branch orbifold smoothing, the tests are harsher:

- Myers forces finite \(\pi_1\).
- Ordinary Seiberg–Witten and spin-index obstructions cannot be used, since they obstruct the plus input itself.
- In dimension four, \(2\chi>3|\tau|\) is mandatory.
- Weighted projective or rational-surface resolutions must be compared with Page, Chen–LeBrun–Weber, and del Pezzo Kähler–Einstein examples; many apparent no-Einstein candidates actually have known Einstein metrics.

A useful search target is therefore: positive Einstein orbifolds with ALE-resolvable singularities whose smooth resolutions have finite \(\pi_1\), positive scalar curvature metrics, strict Hitchin–Thorpe, and an all-metric Einstein exclusion not derived from psc obstruction. This is a narrow but scientifically sharp class.

## (iv) Products and topological operations transferring branch behavior

Plain products transfer same-sign pinching but do not solve all-sign exclusion.

If \(g_i\) on \(M_i\) satisfies \(\delta_-(g_i)\to0\) and \(h\) on \(N\) is exact \(\Ric_h=-h\), then \(g_i\oplus h\) on \(M_i\times N\) also satisfies \(\delta_-\to0\). But \(M_i\times N\) might admit an irreducible Einstein metric unrelated to either factor. All-sign exclusion does not automatically multiply.

Cross-sign transfer by products is essentially blocked. A product of a minus-pinched factor and a plus-Einstein factor has mixed Ricci spectrum; no scaling makes all eigenvalues close to \(+1\) or all close to \(-1\). If the minus seed has infinite \(\pi_1\) or positive simplicial volume, Myers already forbids any plus-pinched metric on the product.

The main product/operation tests are:

- **Myers/Bochner.** A plus-branch counterexample must have finite \(\pi_1\) and \(b_1=0\). Any operation retaining an aspherical factor, an \(S^1\) factor, or large first Betti number cannot transfer to \(P_n^+\).
- **Spin/index.** If an operation preserves a nonzero \(\alpha\)-invariant or \(\hat A\)-type psc obstruction, it also blocks the plus input metric.
- **Simplicial volume.** Positive simplicial volume excludes \(\lambda\ge0\) Einstein metrics but also conflicts with plus pinching through finite \(\pi_1\). It is useful for minus all-sign exclusion, not for plus.
- **Seiberg–Witten.** Four-dimensional monopole classes are powerful for \(P_4^-\), but ordinary monopole obstructions are incompatible with \(P_4^+\).

More promising than products are sign-changing geometric constructions in fixed dimension:

**Candidate operation F: fat-bundle Ricci sign conversion.**  
Start with a minus-pinched base \(B\) and build a sphere or projective bundle \(E\to B\) with a connection metric. O’Neill terms from a fat connection can add positive horizontal Ricci contributions, while small positively curved fibers add positive vertical Ricci. The algebraic tuning problem is:
\[
\Ric_E^{\mathrm{hor}}\approx +g_E^{\mathrm{hor}},
\qquad
\Ric_E^{\mathrm{ver}}\approx +g_E^{\mathrm{ver}}.
\]
This could produce plus-pinched metrics from minus geometry without using a direct product. The hard part is preserving an all-sign no-Einstein invariant on \(E\). Characteristic numbers, Kreck–Stolz-type invariants, or refined smooth-structure invariants are possible sources, but each must be shown compatible with the existence of the plus input.

**Candidate operation S: cohomogeneity-one connected-sum isotropization.**  
Known positive Ricci connected-sum constructions could be used as starting metrics on psc-compatible no-Einstein manifolds. A high-frequency or ODE correction would try to improve Ricci eigenvalues from merely positive to
\[
\Ric\in[(1-\varepsilon)g,(1+\varepsilon)g].
\]
This is a plausible plus counterexample route only if one first identifies finite-\(\pi_1\), psc-compatible smooth manifolds with strict Hitchin–Thorpe and no Einstein metric of any sign. The precise source search is: four-dimensional psc-compatible Einstein nonexistence beyond Hitchin–Thorpe, especially rational or connected-sum smooth structures not ruled out by positive scalar curvature.

## Most decisive near-term mathematical objects

1. **Ricci corrugation cone computation.**  
   Compute the averaged \(O(1)\) Ricci tensor produced by symbol-kernel oscillations in flat space. If \(-\operatorname{Id}\) lies in the interior of the multi-direction cone, R\(_-\) becomes a concrete program. If \(+\operatorname{Id}\) is outside, that explains the plus/minus asymmetry rigorously.

2. **Isotropic Lohkamp theorem.**  
   Strengthen Ricci \(<0\) flexibility to
   \[
   \Ric_{g_L}=-L g_L+o(L)
   \]
   in operator norm. Combined with LeBrun four-manifolds, this would give \(P_4^-\) counterexamples.

3. **Positive-branch degeneration theorem.**  
   Prove that plus pinching admits only finite-quotient collapse and smoothable Einstein orbifold degeneration. Chern–Weil, Myers, Bochner, and equivariant elliptic correction are the key mechanisms.

4. **Plus-compatible no-Einstein topologies.**  
   Search specifically for finite-\(\pi_1\), psc-compatible manifolds with strict four-dimensional Hitchin–Thorpe and an all-sign Einstein exclusion. Without such topologies, plus counterexamples are structurally much harder than minus ones.

5. **Cosmological ALE smoothing with unweighted residual.**  
   Verify whether Biquard/Ozuch/Yao-style approximate metrics can be upgraded to uniform operator pinching on the whole smoothed manifold. The raw ALE core is insufficient; the \(t^2\sigma\)-Einstein correction on the ALE scale is essential.