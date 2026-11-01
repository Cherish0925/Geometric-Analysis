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

Here are route ideas that bypass the current invariant program and attack the real load-bearing issue: whether Ricci pinching itself forces an exact Einstein metric, or whether approximate Einstein metrics can live on smooth manifolds with no Einstein metric.

## 0. Scaling/sign reformulation

If \(c<0<C\), then after scaling any fixed metric by a large factor, all Ricci eigenvalues relative to the scaled metric lie in \((c,C)\). Thus for \(n\ge 3\), any viable pair must be one-sided, or touch zero from one side. The true counterexample target is therefore:

\[
\forall \varepsilon>0,\quad \exists M^n \text{ with no Einstein metric and } g_\varepsilon
\text{ such that }
\|\operatorname{Ric}_{g_\varepsilon}-\lambda g_\varepsilon\|_{op}
<\varepsilon |\lambda|
\]

for \(\lambda>0\) and also for \(\lambda<0\). Scaling then places the Ricci spectrum inside any prescribed one-sided interval.

Dimension \(3\) is special: if one chooses \(c_3>0\), Hamilton’s Ricci flow theorem takes positive Ricci to a spherical space form, hence to an Einstein metric. Dimension \(4\) is the decisive terrain for refutation or for a genuinely new existence principle.

---

## 1. Orbifold-resolution engine for counterexamples

The most direct new counterexample mechanism is not a toric polygon collapse, but a compact Einstein orbifold with isolated quotient points, smoothed by ALE gravitational instantons. The smooth resolution can carry metrics with arbitrarily small Einstein defect even when the resolved smooth manifold is topologically barred from carrying any Einstein metric.

Let \((\mathcal O^4,g_{\mathcal O})\) be a compact Einstein orbifold,

\[
\operatorname{Ric}_{g_{\mathcal O}}=\lambda g_{\mathcal O},
\]

with isolated singularities modeled on \(\mathbb R^4/\Gamma_i\), \(\Gamma_i\subset SO(4)\) acting freely on \(S^3\). Replace each singular cone by a scaled ALE space \(X_{\Gamma_i}\). The important technical point is that a raw Ricci-flat ALE core is not enough in operator norm: on the unscaled core, \(\operatorname{Ric}=0\) is not close to \(\lambda g\). One needs the usual cosmological ALE expansion

\[
\widehat g_t
=
g_{\mathrm{ALE}}+t^2 k_2+t^4 k_4+\cdots+t^N k_N
\]

solving, on the rescaled cap,

\[
\operatorname{Ric}_{\widehat g_t}
=
\lambda t^2 \widehat g_t+O_{\widehat g_t}(t^N).
\]

After unscaling \(g_t=t^2\widehat g_t\), the operator defect is

\[
\|\operatorname{Ric}_{g_t}-\lambda g_t\|_{g_t,op}
=
O(t^{N-2}),
\]

so any \(N>2\) gives true \(C^0\)-Ricci pinching. On the matching annulus, the cone expansion of the orbifold metric and the ALE asymptotics give competing terms of the form

\[
r^2,\qquad t^4 r^{-6},
\]

so choosing \(r=t^{1/2}\) gives a model residual \(O(t)\). Higher-order matching should improve this.

The topological part is then four-dimensional and sharp: every closed oriented Einstein four-manifold satisfies Hitchin–Thorpe,

\[
2\chi(M)\ge 3|\tau(M)|.
\]

Thus an Einstein orbifold whose smooth resolution has

\[
2\chi(M)<3|\tau(M)|
\]

would give a full counterexample sequence.

Scientific source families to inspect:

- compact Kähler–Einstein log del Pezzo orbifolds with quotient singularities whose minimal resolutions are rational surfaces \(\mathbb{CP}^2\# k\overline{\mathbb{CP}}^2\) with \(k\ge 10\);
- compact hyperbolic or complex-hyperbolic four-orbifolds with isolated quotient points and ALE resolutions with large signature contribution;
- Biquard–Rollin–Ozuch Einstein orbifold desingularization estimates, specifically the norm in which the approximate metric satisfies \(\operatorname{Ric}-\lambda g=o(1)\);
- Kronheimer ADE ALE spaces and the exact \((\chi,\tau)\) contribution of each resolution.

A useful toy model is \(S^4/\Gamma\), viewed as the suspension of \(S^3/\Gamma\), with two isolated cone points. Resolving the two points by ADE ALE spaces likely gives signature cancellation in the simplest orientation arrangement, so it may produce manifolds of \(S^2\times S^2\)-type rather than a Hitchin–Thorpe contradiction. Still, it is an excellent model for testing the operator-norm Einstein defect and the small Lichnerowicz modes created by the gluing parameter.

What would break this route: the approximate desingularization may only be small in a weighted rescaled norm, while the unscaled operator norm remains \(O(1)\) on the ALE core unless the cosmological correction is carried far enough. This is a concrete calculation, not a philosophical issue.

---

## 2. Ricci flow as an existence mechanism, not merely smoothing

A different route is to treat a pinched metric as initial data for normalized Ricci flow and ask whether small traceless Ricci is dynamically attracted to zero.

Let

\[
E=\operatorname{Ric}-\frac{s}{n}g.
\]

For normalized Ricci flow, the schematic evolution is

\[
(\partial_t-\Delta)E
=
2W*E
+
E*E
+
sE
+
\text{normalization terms}.
\]

The dangerous term is \(W*E\). The CZ spike shows that \(W\) can be pointwise large while \(E\) is tiny, so a maximum-principle proof for \(|E|\) alone is not available. But an integral route remains plausible:

\[
\left|\int W(E,E)\right|
\le
\|W\|_{L^2}\|E\|_{L^4}^2
\]

in dimension four. Positive scalar lower bounds give a Yamabe-type Sobolev inequality, and if \(\|W\|_{L^2}\) is locally quantized rather than spread everywhere, one can imagine a flow decomposition:

- on low-energy regions, \(E\) decays;
- near energy concentrations, bubbles form;
- each bubble is ALE or orbifold-modeled;
- exact Einstein existence reduces to whether the bubble tree can be corrected.

This would merge Ricci flow with the orbifold-resolution picture rather than with global torus symmetry.

Observable distinctions:

- CZ spike on \(S^2\times S^2\): \(W\) is large at tiny scale but the topology already has an Einstein metric. The flow should smooth the spike and return toward the product.
- Obstructed orbifold resolutions: if the smooth manifold violates Hitchin–Thorpe, normalized flow cannot converge to an Einstein metric; it must develop singular behavior or move the metric out of the near-Einstein region.
- Separated SdS/Nariai germs: the conical mode should appear as a slow Lichnerowicz direction under flow.

Load-bearing assumption: a localized \(L^2\)-energy Ricci-flow estimate in which small \(E\) survives long enough for the flow to reveal the bubble tree. This is stronger than Li smoothing but weaker than pointwise curvature control at time zero.

---

## 3. Direct low-regularity Einstein correction

Instead of flowing, one can try to solve the Einstein equation directly from a \(C^0\)-Ricci-small approximate solution.

Use DeTurck gauge:

\[
\Phi(h)
=
\operatorname{Ric}_h-\lambda h+\delta_h^*B_g(h).
\]

At \(h=g\),

\[
\Phi(g)=\operatorname{Ric}_g-\lambda g.
\]

The linearization is essentially

\[
L_g
=
\frac12(\Delta_L-2\lambda)
+
\text{lower-order gauge terms}.
\]

The CZ spike says \(g\) need not have bounded curvature, but harmonic-coordinate theory gives \(W^{2,p}\) regularity for all finite \(p\) under bounded Ricci and harmonic radius control. Thus the direct PDE route would work if one had:

\[
\|u\|_{W^{2,p}}
\le
K\|L_gu\|_{L^p}
\]

with \(K\) depending only on dimension and the pinching constants, after removing genuine Einstein moduli.

Then Newton iteration gives an exact Einstein metric whenever

\[
K\|\operatorname{Ric}_g-\lambda g\|_{L^p}
\]

is sufficiently small.

Where the geometry enters: \(K\) blows up near orbifold degenerations, ALE necks, and approximate kernel directions. Thus the inverse problem would reveal exactly the same finite-dimensional quantities as Biquard–Ozuch gluing: curvature operator at the orbifold point, ALE harmonic tensors, and the projection of the Einstein defect onto small Lichnerowicz modes.

A decisive computation would be the first small eigenvalue of the gauged Einstein operator on:

\[
S^4/\Gamma \text{ resolutions},\qquad
\text{ADE doubles},\qquad
\text{SdS/Nariai separated caps}.
\]

If the smallest eigenvalue is \(t^\alpha\) and the residual is \(t^\beta\), then \(\beta>\alpha\) suggests correction to an exact Einstein metric, while \(\beta\le\alpha\) leaves a finite-dimensional obstruction.

---

## 4. Variational formulation: anisotropy gap over topology

Define a scale-invariant Ricci anisotropy for the positive side:

\[
\mathcal A_+(M)
=
\inf_{\operatorname{Ric}>0}
\frac{
\|\operatorname{Ric}-\frac{s}{n}g\|_{L^\infty,op}
}{
\inf_M s/n
}.
\]

Similarly define \(\mathcal A_-(M)\) over metrics with \(\operatorname{Ric}<0\), using \(|s|/n\). A one-sided Yau-26 pair is equivalent to a dimension-only gap:

\[
\inf_{M\ \text{with no Einstein metric}}\mathcal A_\pm(M)>0.
\]

Thus the problem can be recast as a global variational gap problem for the Einstein defect.

A smoother version uses

\[
\mathcal F(g)=\int_M |\operatorname{Ric}^\circ|^2\,dV,
\]

possibly under fixed volume and scalar normalization. In dimension four,

\[
8\pi^2\chi
=
\int_M
\left(
|W|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24}
\right)dV,
\]

\[
12\pi^2\tau
=
\int_M(|W^+|^2-|W^-|^2)dV.
\]

Therefore a sequence with \(\mathcal F\to0\) but no Einstein metric must push its topology into Weyl energy and bubble concentrations. This is exactly where orbifold compactness, ALE energy quantization, and Hitchin–Thorpe interact.

This route gives a clean comparison figure: for each proposed bubble tree, plot

\[
3|\tau|-2\chi
\]

against the gluing residual rate. Bubble trees that violate Hitchin–Thorpe yet admit residual \(o(1)\) are counterexample engines; bubble trees whose residual has a fixed nonzero projection are evidence for an anisotropy gap.

---

## 5. Lohkamp / Ricci-flexibility route for \(\lambda<0\)

There is a possible refutation route on the \(\lambda<0\) side using Ricci flexibility. Lohkamp-type theorems show enormous freedom for constructing metrics with \(\operatorname{Ric}<0\) on arbitrary manifolds. The missing strengthening is two-sided relative squeezing:

\[
-(1+\varepsilon)g
\le
\operatorname{Ric}_g
\le
-(1-\varepsilon)g.
\]

If such a theorem exists for every closed \(n\ge3\) manifold, then any closed manifold with no Einstein metric immediately defeats every interval with \(c<C<0\).

The scientific mechanism would have to overcome the tensorial Bianchi constraint. The conformal formula

\[
\operatorname{Ric}_{e^{2u}g}
=
\operatorname{Ric}_g
-(n-2)(\nabla^2u-du\otimes du)
-
(\Delta u+(n-2)|\nabla u|^2)g
\]

shows why naive oscillation creates anisotropy. The CZ spike suggests a more subtle microstructure: large trace-free Hessian can be hidden in Weyl curvature while Ricci sees only controlled traces, if multiple warp factors are arranged with opposite signs.

A local model to test is a diagonal multi-warped metric on a cube,

\[
g=\sum_i e^{2u_i(x)}(dx^i)^2,
\qquad
\sum_i u_i\approx 0,
\]

with the \(u_i\) chosen so Hessian traces add isotropically while trace-free parts cancel in Ricci. One then asks whether the cell can be periodically closed and patched onto arbitrary manifolds while preserving

\[
\operatorname{Ric}= -g+O(\varepsilon).
\]

Source families to search: Lohkamp’s Ricci-flexibility papers, DeTurck’s prescribed Ricci tensor work, and later local deformation results for Ricci curvature under compact support.

---

## 6. Positive-side neck convexity and handle exclusion

The positive side may be rigid for a geometric reason unrelated to torus actions: ordinary connected-sum necks are incompatible with near-positive-Einstein Ricci.

For a warped neck

\[
g=dr^2+f(r)^2\gamma_{S^{n-1}},
\]

one has

\[
\operatorname{Ric}_{rr}=-(n-1)\frac{f''}{f},
\]

\[
\operatorname{Ric}_{T}
=
\frac{(n-2)(1-(f')^2)-ff''}{f^2}.
\]

At a neck minimum, \(f''\ge0\), so \(\operatorname{Ric}_{rr}\le0\), incompatible with \(\operatorname{Ric}\approx \lambda g\), \(\lambda>0\). In general form, the Riccati equation for hypersurface mean curvature is

\[
H'=-|II|^2-\operatorname{Ric}(\nu,\nu).
\]

If \(\operatorname{Ric}(\nu,\nu)\approx\lambda>0\), then \(H\) must strictly decrease along normal flow. A tube cannot behave like a standard handle without focal concentration.

This suggests a strong structural picture: positive near-Einstein topology cannot be carried by codimension-one necks; it must appear through codimension-four orbifold/ALE bubbles. That connects the positive branch directly to Einstein orbifold compactness and desingularization, without first finding a torus action.

What can break this picture: topology may hide in codimension-two or codimension-four regions where no stable hypersurface detects it, exactly as in ALE resolution bubbles. The right observable is not just a minimal hypersurface, but the full bubble-tree topology.

---

## 7. Kaluza–Klein and bundle algebra as a near-Einstein laboratory

Principal bundles over Einstein bases give a non-toric, computable class of Ricci-pinched metrics. For a connection metric

\[
g_t=\pi^*g_B+t^2\langle\theta,\theta\rangle
\]

on a principal \(G\)-bundle, O’Neill formulas give schematically

\[
\operatorname{Ric}^H
=
\operatorname{Ric}_{B}
-\frac{t^2}{2}\sum_\alpha
\langle i_XF_\alpha,i_YF_\alpha\rangle,
\]

\[
\operatorname{Ric}^V_{\alpha\beta}
=
\frac{t^2}{4}\langle F_\alpha,F_\beta\rangle
+\operatorname{Ric}_{G,\alpha\beta}.
\]

Almost Einstein becomes an algebraic moment-map problem: the curvature forms \(F_\alpha\) must behave like a tight frame in \(\Lambda^2B\), and the vertical Ricci matrix must match the horizontal eigenvalue.

This gives two possible outcomes.

1. If integral lattice data can approximate the tight-frame equations arbitrarily well while the total space has no Einstein metric, this yields counterexamples.

2. If near-solutions are forced to exact algebraic solutions by bundle topology, this becomes a positive existence route for a large non-symmetric class.

Concrete families: circle bundles and \(SU(2)\)-bundles over Kähler–Einstein surfaces, quaternionic Kähler bases, and orbifold bases with large Chern class. The distinguishing calculation is entirely explicit: compute the horizontal and vertical Ricci eigenvalues, the Chern/Pontryagin numbers of the total space, and known Einstein obstructions.

---

## 8. High-dimensional transfer

A four-dimensional counterexample is already enough to refute the all-\(n\) statement. Still, higher-dimensional transfer is scientifically useful.

If \(M^4\) carries \(g_j\) with

\[
\operatorname{Ric}_{g_j}=\lambda g_j+o(1),
\]

and \(N^{n-4}\) is Einstein with the same \(\lambda\), then

\[
(M^4\times N^{n-4},\, g_j\oplus g_N)
\]

is again almost Einstein. The hard part is proving the product has no Einstein metric even if \(M^4\) has none. Hitchin–Thorpe does not directly transfer.

Possible source families for product no-Einstein results:

- Kotschick–LeBrun smooth-structure obstructions;
- simplicial-volume/minimal-volume inequalities for \(\lambda<0\);
- spinorial obstructions when scalar sign permits them;
- characteristic-number inequalities for Einstein metrics in dimensions \(4k\).

This is secondary if dimension four produces a full refutation, but essential if one wants a dimension-by-dimension picture.

---

## Most decisive scientific fork

The richest fork is the orbifold-resolution one:

- If compact Einstein orbifolds exist whose smooth ALE resolutions violate Hitchin–Thorpe and still admit \(C^0\)-small Einstein defect, Yau-26 is refuted in dimension four.
- If every such attempted resolution has an operator-norm defect bounded below by a dimension-only amount, then the missing mechanism is a finite-dimensional Einstein obstruction visible already at the approximate level.
- If the defect can be made small but the smooth resolution unexpectedly carries another Einstein metric, then Ricci pinching may be detecting an Einstein metric far from the initial approximate one; that would be a genuinely new existence phenomenon.

This route directly tests Bridge 3 without symmetry, bounded sectional curvature, or finite diffeomorphism reduction.