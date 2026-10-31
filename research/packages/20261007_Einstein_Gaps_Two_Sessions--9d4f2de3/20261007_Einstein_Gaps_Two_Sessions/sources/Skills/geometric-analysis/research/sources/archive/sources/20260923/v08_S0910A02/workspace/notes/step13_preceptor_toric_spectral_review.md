# Step 13: Preceptor review of the toric determinant route

Session S0910A02, Agent4/Preceptor, Execute.

## 0. Scope relative to Yau Problem 26

The active goal remains the full sign-unrestricted Yau-26 proposition: for each
closed connected smooth dimension, dimension-only two-sided Ricci pinching should
force the underlying smooth manifold to admit some Einstein metric, or else the
statement must be strictly refuted.  The toric computation below is **not** a
proof of the proposition and not even Proposition A's simply connected volume-gap
hypothesis.  It is a reduced four-dimensional positive-branch laboratory: if a
simply connected collapsing positive-pinched sequence can be reduced, even
approximately, to a torus-invariant orbit-space problem with degeneration
boundary, the determinant identity gives a scale obstruction without needing
pointwise curvature regularity.

The main Step-13 correction is that Step 12 underestimated its own determinant
identity.  Orthogonal transitivity is important for using the diagonal reduced
system, but it is **not** needed for the basic spectral scale pinning.  Twist
appears as a nonnegative potential in a Schrödinger operator and can only raise
the weighted energy, not destroy the Dirichlet eigenvalue bound.

## 1. What survives independent verification

Step 12 computed, for a local \(T^2\)-invariant four-metric
\[
 g=g_B+h_{IJ}(d\phi^I+A^I)(d\phi^J+A^J),\qquad w=\sqrt{\det h},
\]
in normalized base/vertical gauge,
\[
 \operatorname{tr}_h\operatorname{Ric}^{V}
 =-{\Delta_B w\over w}+{1\over2}|F|_h^2. \tag{1}
\]
The saved data
`workspace/data/step12_toric_vertical_trace_symbolic.json` records the raw
identity
\[
\operatorname{tr}_h\operatorname{Ric}^{V}+\Delta_Bw=(f_1^2+f_2^2)/2
\]
at \(h=I,w=1\), which is exactly (1).  The mixed Ricci calculation in
`workspace/data/step12_toric_mixed_gauge_compare.json` also records
\[
 \operatorname{Ric}_{xI}=\frac12\partial_y(wh_{IJ}f_J),\qquad
 \operatorname{Ric}_{yI}=-\frac12\partial_x(wh_{IJ}f_J),            \tag{2}
\]
i.e. the twist conservation equation
\[
 d\bigl(w h_{IJ}*_B F^J\bigr)=0
\]
when the metric is exactly Einstein.

The sign and factor in (1) pass two independent anchors.

* If \(\operatorname{Ric}=\lambda g\), then the vertical trace is \(2\lambda\),
  hence
  \[
  \boxed{\left(-\Delta_B+{1\over2}|F|_h^2\right)w=2\lambda w.}       \tag{3}
  \]
  Since \(w>0\) in the regular orbit space and \(w=0\) on a degeneration
  boundary, \(2\lambda\) is the Dirichlet ground-state eigenvalue of the
  Schrödinger operator \(-\Delta_B+|F|^2/2\).  The potential is nonnegative, so
  \[
  \lambda_1^{\mathrm{Dir}}(\Omega,g_B)\le 2\lambda.                \tag{4}
  \]
  In particular, a compact Einstein metric with a \(T^2\)-degeneration boundary
  cannot have \(\lambda\le0\).  This agrees with the classical Bochner
  obstruction: compact Ricci-flat Killing fields are parallel and therefore
  zero-free, while compact negative Ricci manifolds have no nonzero Killing
  fields.

* The round \(S^4\) normalized by \(\operatorname{Ric}=g\) has radius
  \(\sqrt3\).  Under the standard \(T^2\)-rotation, the orbit space is a quarter
  of \(S^2(\sqrt3)\), and \(w=r_1r_2\) is the restriction of a degree-2 spherical
  harmonic.  Thus
  \[
  \Delta w=-{6\over3}w=-2w.
  \]
  The anchor script `workspace/scripts/step13_toric_spectral_anchors.py` saved
  `workspace/data/step13_toric_spectral_anchors.json`; it records
  \(\int_\Omega w=6\), \(\operatorname{Vol}(S^4)=4\pi^2\cdot6=24\pi^2\), and
  the boundary flux \(2\int w=12\), matching the two fixed two-spheres of area
  \(12\pi\) after multiplying by the surviving \(2\pi\)-circle period.

These tests would fail under the opposite sign or a missing factor of two.

## 2. The pinched version is already available from the same identity

For the positive normalized branch
\[
 \|g^{-1}\operatorname{Ric}-I\|_{op}\le\delta,
\]
the vertical trace over the two orbit directions satisfies
\[
\operatorname{tr}_h\operatorname{Ric}^{V}\le2(1+\delta).
\]
Multiplying (1) by \(w^2\), integrating by parts, and using the Dirichlet
boundary behavior gives the Rayleigh inequality
\[
 {\int_\Omega |\nabla w|^2+{1\over2}\int_\Omega |F|^2w^2
  \over \int_\Omega w^2}
 = {\int_\Omega (\operatorname{tr}_h\operatorname{Ric}^{V})w^2
  \over \int_\Omega w^2}
 \le 2(1+\delta).                                                \tag{5}
\]
Consequently
\[
 \boxed{\lambda_1^{\mathrm{Dir}}(\Omega,g_B)\le2(1+\delta).}       \tag{6}
\]
No approximate orthogonal transitivity, no derivative of the Ricci defect, and
no pointwise curvature regularity is needed for (6).  This is the first clean
realization in this session of the Step-8 projection principle: the Killing
fields supply smooth test data, and the Ricci error is used only in operator
norm against those data.

What (6) does **not** prove by itself: it is an upper bound for a two-dimensional
Dirichlet eigenvalue, not a volume lower bound for the four-manifold.  A full
invariant volume gap still needs to combine this spectral scale with boundary
closure, Gauss--Bonnet/corner constraints, and weighted curvature/energy control.
On a general Riemannian disk, a Dirichlet eigenvalue upper bound alone does not
preclude all thin or high-curvature degenerations.

## 3. Source-scoped exact Einstein inputs

A useful source located during this step is
`Knowledge/objects/papers/Toric-Einstein-4-manifolds-with-non-negative-sectional-curvature--24d1f88fe098--1315c2a6cd67/object.md`
(arXiv:2311.04840).  Although its main theorem assumes nonnegative sectional
curvature, several preliminary facts are stated without that assumption.

* Lines 66--68 state that on the relevant closed simply connected four-manifolds
  a \(T^2\)-invariant metric induces a curved polygonal quotient with geodesic
  edges and right-angle corners, and Theorem 1.2 says an isometric \(T^2\)-action
  on a closed simply connected Einstein four-manifold is geometrically polar.

* Lines 84--87 review Orlik--Raymond topology: the principal stratum descends to
  the polygon interior, codimension-two strata to edges, and fixed points to
  vertices; the same lines state that an invariant metric gives a curved polygon
  whose angles are right angles and whose edges are geodesics.

* Lines 181--210 prove the polar/orthogonal-transitivity statement in the exact
  simply connected Einstein case.  The mixed Ricci equations force the twist
  scalars \(\alpha,\beta\) to be constant on the principal stratum; smoothness
  makes them vanish along singular strata, hence everywhere.  This is the
  sourced version of Step 12's expected twist-vanishing lemma.  It is now not the
  first bottleneck for scale pinning, but it remains valuable for reducing exact
  Einstein toric metrics to the diagonal/geometrically polar equations.

* Lines 233--247 give the exact polar orbit-volume theorem: for a geometrically
  polar \(T^2\)-invariant Einstein metric, the orbit-volume function \(\phi\)
  satisfies
  \[
  -\Delta_\Sigma\phi=2\Lambda\phi.
  \]
  This matches (3) when twist has vanished.

This source does **not** close the C^0-pinched case, and it does not justify
turning an arbitrary collapsing positive-pinched sequence into an invariant one.
It only removes unnecessary uncertainty about the exact toric Einstein
subproblem.

## 4. Gauss--Bonnet with right-angle corners: a global signed constraint

For a smooth invariant metric in the closed simply connected toric setting, the
quotient \(\Omega=M/T^2\) is a disk-like polygon with geodesic edges and
right-angle corners.  Applying two-dimensional Gauss--Bonnet with corners gives
\[
 \int_\Omega K_B\,dA +\sum_{j=1}^m (\pi-\alpha_j)=2\pi,
 \qquad \alpha_j={\pi\over2},
\]
so
\[
 \boxed{\int_\Omega K_B\,dA=2\pi-{\pi\over2}m.}                  \tag{7}
\]
Here \(m\) is the number of vertices/fixed points; in the usual toric
four-manifold setting this equals \(\chi(M)\).  The anchor data file records the
checks
\[
S^4: m=2,\ \int K=\pi;
\quad \mathbb{CP}^2: m=3,\ \int K=\pi/2;
\quad S^2\times S^2: m=4,\ \int K=0;
\]
and for \(\mathbb{CP}^2\#2\overline{\mathbb{CP}}^{2}\) one would get
\(m=5\), \(\int K=-\pi/2\).  Thus the orbit base need not have nonnegative
curvature: known positive Einstein examples such as Page and Chen--LeBrun--Weber
must be accommodated by any proposed gap theorem.

This is exactly the global meaning of the Step-12 edge coefficient.  In the edge
expansion
\[
 g_B=dr^2+a(r,s)^2ds^2,
 \qquad a=1+{a_2(s)\over2}r^2+\cdots,
\]
we have \(K_B|_{edge}=-a_2\), and the saved edge computation gives
\[
 Q''+(1+2a_2)Q=0.                                                \tag{8}
\]
The fixed two-sphere over that edge has metric \(ds^2+Q(s)^2d\phi^2\), so its
intrinsic curvature is
\[
 K_\Sigma=-{Q''\over Q}=1+2a_2=1-2K_B|_{edge}.                  \tag{9}
\]
A toric volume collapse would force the total fixed-sphere area to collapse;
then Gauss--Bonnet on each fixed sphere forces large positive intrinsic curvature
somewhere along the rods.  Thus the uncontrolled \(a_2\) is not a vague Weyl
freedom: it is the exact edge curvature variable that must carry any invariant
collapse.

For exact Einstein metrics with possible twist, integrating (3) yields
\[
 -\int_{\partial\Omega}\partial_{\nu_{out}}w
 =2\int_\Omega w-{1\over2}\int_\Omega |F|^2w.                  \tag{10}
\]
The left side is the fixed-sphere area divided by \(2\pi\).  Hence
\[
 \operatorname{Vol}_4=4\pi^2\int_\Omega w
 =\pi\,\operatorname{Area}(M^{S^1}_{2d})+
   \pi^2\int_\Omega |F|^2w
 \ge \pi\,\operatorname{Area}(M^{S^1}_{2d}).                    \tag{11}
\]
In the polar case \(F=0\), this is an equality.  A volume gap is therefore
morally equivalent, in the invariant class, to a lower bound for total rod area;
by (9), collapse is equivalent to unbounded positive intrinsic curvature on the
fixed spheres.

## 5. What is now the real invariant-class gap?

The strongest invariant route is no longer:

1. prove twist vanishing;
2. prove an approximate twist-free C^0 equation;
3. then seek a volume gap.

Instead it is:

1. use the determinant identity directly to obtain the Schrödinger/Dirichlet
   eigenvalue bound (exact and C^0-pinched);
2. combine it with unit primitive closure and the corner Gauss--Bonnet identity;
3. control or exploit the edge curvature \(a_2\) via the weighted four-dimensional
   energy budget.

The prospective contradiction for an invariant positive-pinched collapse is now
sharper.  If \(\operatorname{Vol}\to0\), then the fixed-sphere areas also tend to
zero (at least in the exact Einstein/polar limit, and with an analogous one-sided
estimate in pinched data).  By Gauss--Bonnet on rods, \(K_\Sigma\) becomes large,
so \(a_2\) becomes large positive and \(K_B\) large negative near some edge.  The
Dirichlet eigenvalue bound \(\lambda_1\le2(1+\delta)\) keeps the orbit space from
shrinking uniformly; collapse must occur mainly in the torus fibers.  Unit slope
closure of a collapsing circle length then forces rapid turnover near the edge,
which should produce a high-curvature strip.  The four-dimensional CGB/Ricci
pinching budget weights base curvature by the orbit area density \(w\); a strip
where circle lengths are \(O(\varepsilon)\) can hide curvature only if its base
measure/edge length is correspondingly small.  The intended endgame is an
isoperimetric or weighted-energy inequality excluding a disk of bounded Dirichlet
scale and vanishing perimeter/rod area.

The real weakness is also clear: (7) controls only the signed total of \(K_B\),
not \(\int K_B^-\), and high negative base curvature can in principle be balanced
elsewhere.  Therefore a valid proof must use a second input, probably the
weighted Chern--Gauss--Bonnet energy budget or an isoperimetric inequality with
control of \(K^+\).  If the theorem is false in the invariant class, this is where
an explicit large-\(a_2\) reduced solution sequence should appear.

## 6. Known examples and consistency boundaries

The source lines 41--42 list the currently known positive toric Einstein examples:
round \(S^4\), Fubini--Study \(\mathbb{CP}^2\), product \(S^2\times S^2\), the
Page metric on \(\mathbb{CP}^2\#\overline{\mathbb{CP}}^2\), the
Chen--LeBrun--Weber metric on
\(\mathbb{CP}^2\#2\overline{\mathbb{CP}}^2\), and the Kähler--Einstein metric on
\(\mathbb{CP}^2\#3\overline{\mathbb{CP}}^2\).  LeBrun's Hermitian Einstein
classification source (`On-Einstein-Hermitian-4-Manifolds`, lines 23--24 and
40--60) independently confirms the Page and CLW exceptional metrics and that
their isometry group contains a two-torus.

These examples are consistency tests, not obstructions.  In particular:

* a proposed invariant volume-gap proof must allow negative total base curvature
  when \(m\ge5\), as in the CLW topology;
* it cannot assume \(K_B\ge0\), constant \(a_2\), rectangular orbit space, or a
  product/diagonal rod pattern;
* it should recover the exact anchors \(S^4\), \(\mathbb{CP}^2\), and
  \(S^2\times S^2\), while treating Page/CLW as nontrivial rod-curvature tests
  once explicit coordinates are sourced or derived.

## 7. Higher-dimensional determinant trace

The same algebra has a dimension-general form.  For a \(T^k\)-invariant metric
over an \(m=n-k\)-dimensional orbit space,
\[
 g=g_B+h_{IJ}(d\phi^I+A^I)(d\phi^J+A^J),\qquad w=\sqrt{\det h},
\]
the vertical trace should take the form
\[
 \operatorname{tr}_h\operatorname{Ric}^V=-{\Delta_Bw\over w}+{1\over2}|F|_h^2,
\]
with the same convention for the connection-curvature norm.  Therefore exact
\(\operatorname{Ric}=\lambda g\) gives
\[
 \left(-\Delta_B+{1\over2}|F|_h^2\right)w=k\lambda w,
 \qquad
 \lambda_1^{Dir}(\Omega)\le k\lambda.                           \tag{12}
\]
For \(C^0\)-positive pinching, the same Rayleigh argument gives
\[
 \lambda_1^{Dir}(\Omega)\le k(1+\delta).                         \tag{13}
\]
I made only a limited executable check here: `workspace/scripts/step13_tk_trace_diagonal_symbolic.py` verifies for twist-free diagonal metrics
\(g=dx^2+dy^2+\sum_{i=1}^k p_i^2d\theta_i^2\), with \(k=1,2,3\), that
\[
 \operatorname{tr}_h\operatorname{Ric}^{V}=-{\Delta(\prod_i p_i)\over \prod_i p_i},
\]
and saved the result in `workspace/data/step13_tk_trace_diagonal_symbolic.json`.
The arbitrary-base, non-diagonal, twisted \(T^k\) formula still needs a clean
coordinate-free or symbolic proof before it can be used outside the four-dimensional
calculation already verified in Step 12.  It matters because exact positive
Einstein collapse in higher dimensions can be free (lens/Sasaki), but a
degeneration-boundary torus action would again carry a Dirichlet determinant
scale.  This remains the only mechanism in the current record with a plausible
route beyond dimension four, but the full Yau-26 all-dimensional proposition is
far outside what has been proved.

## 8. Preceptor judgment

The Step-12 formulas are fit to use, with the corrections above.  The route
should not spend its next effort proving exact orthogonal transitivity: a source
already gives it in the simply connected closed Einstein case, and spectral
pinning does not require it.  Nor should it pursue pointwise or even finite-\(p\)
regularity as the main route unless the reduction from general collapse to
invariant orbit geometry demands it.

The load-bearing open obligations are now:

1. **Invariant volume gap.**  Prove or disprove, inside the smooth toric
   positive-pinched class with degeneration boundary, that (6), primitive unit
   closure, right-angle geodesic polygon topology, and the weighted CGB/Ricci
   budget imply \(\int_\Omega w\ge v>0\).  This should be attacked as a concrete
   two-dimensional weighted inequality or by constructing a large-\(a_2\) reduced
   counterexample.

2. **General-to-invariant reduction.**  Even a complete invariant volume gap
   would not prove Proposition A.  One still needs a rigorous way to extract an
   invariant/collapsed model from an arbitrary simply connected positive-pinched
   collapse without using the false pointwise \(C^0\)-Ricci regularity.  Naber--
   Zhang accessible covers, weak harmonic coordinates, and group-action limits
   are the likely tools; this must remain an open reduction, not a formality.

3. **Known-example calibration.**  The Page and Chen--LeBrun--Weber metrics must
   be used as tests for any edge-curvature or isoperimetric claim.  A proof that
   accidentally excludes them is false.

4. **Dimension-general trace.**  Verify the \(T^k\) determinant trace in a clean
   symbolic or coordinate-free calculation while the \(k=2\) computation is fresh.
   This may provide the first credible bridge from the four-dimensional toric
   laboratory to the all-dimensional Yau-26 problem.

The negative-branch peer updates (#256--#257) are consistent with this judgment:
standard NUT residue counting has been replaced by diffuse twist/anisotropy
mechanisms, and A03's corrected circle reduction emphasizes a survival/death
dichotomy for fibers.  Those results should inform the general-to-invariant
collapse reduction, but they do not change the positive toric spectral review.
