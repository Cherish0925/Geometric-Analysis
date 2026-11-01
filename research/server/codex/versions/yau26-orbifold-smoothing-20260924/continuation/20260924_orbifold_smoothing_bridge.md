# Gauge saturation, orbifold compactification, and marked smoothing realization

24 September 2026. A continuation of the
[actual-form composition](../mathematics/current/line1_composed_application.md)
and [compact KE realization](20260923_gauge_saturation_ke.md).
This note removes the assumption that the second homotopy group vanishes
from the **compactification** conclusion. Smooth realization is then obtained
under a separate, explicit algebraic and relative-diffeomorphism condition.
It does not assert that these latter conditions follow from Ricci pinching.

The contribution here is a composition of the inherited actual-form estimates
with classical bounded-Ricci orbifold compactness and algebraic smoothing.
The compactness, ALE classifications, deformation criterion and negative KE
existence theorem retain their classical attributions. No priority claim is
made for the composition.

## 1. Original input and compactification theorem

All manifolds are connected, closed, smooth and oriented of real dimension
four. Ricci uses the tensor norm except in the definition of the pointwise
operator defect. Two-forms use exterior-algebra norms and Weyl curvature
uses the Hilbert--Schmidt norm as an endomorphism of two-forms. Write
\[
 \delta_j=\|\operatorname{Ric}_{g_j}^{\sharp}+I\|_{\infty,\mathrm{op}},
 \quad V_j=\operatorname{Vol}(M_j,g_j),\quad
 p_j=(a_j^+)^2,
\]
\[
 q_j=\frac{\mathfrak D_2(g_j,a_j)}{V_j},\qquad
 \mathfrak D_2(g,a)=\frac32\int_M(s^2+12|W^+|^2)-72\pi^2(a^+)^2.
 \tag{1}
\]
An **actual conformally solvable class** means the Chern class of a
Spin\(^c\) structure whose unperturbed monopole equations are solvable for
every metric in the conformal class of the specified metric. The structure
may vary with \(j\), but is fixed when its auxiliary positive weights vary.

**Theorem A (negative KE orbifold compactification).** Suppose that, for
fixed \(D,A_0>0\),
\[
 \operatorname{diam}(M_j,g_j)\le D,\qquad p_j\ge A_0,
 \qquad \delta_j+q_j\longrightarrow0,                 \tag{2}
\]
and each \(a_j\) is an actual conformally solvable class. No hypothesis is
made on \(\pi_1(M_j)\) or \(\pi_2(M_j)\). A subsequence converges in the
Gromov--Hausdorff topology to a compact oriented orbifold \((X,h)\) with
finitely many isolated quotient singularities, and
\[
              \operatorname{Ric}_h=-h.
\]
There is a **global orbifold Kähler structure** \(J\) on \(X\), with its
given orientation. On every compact subset of \(X_{\mathrm{reg}}\), the
convergence is realized by smooth embeddings and is \(C^{1,\alpha}\) for
every \(\alpha<1\) and strong \(W^{2,p}\) for every finite \(p\).
The limiting metric and complex structure are smooth in orbifold charts.

No covering space is required to define \(J\). No negative-square cost,
Ricci-derivative bound, curvature-energy assumption, or initially given
complex structure on \(M_j\) is added to (2). This is not smooth compactness
on all of \(M_j\): topology may be carried by the neighborhoods that shrink
to the singular points.

### Proof: the bounded-Ricci compactness input really applies

Put \(r_j=\fint|\operatorname{Ric}_{g_j}+g_j|^2\) and
\(\kappa_j=r_j+q_j\). For large \(j\), \(\delta_j\le1/2\), so
\[
 |\operatorname{Ric}_{g_j}|\le3,\qquad
 -6\le s_j\le-2,\qquad r_j\le4\delta_j^2.
\]
The actual monopole scalar inequality gives
\[
 32\pi^2A_0\le\int s_{j,-}^2
       \le16(1+\delta_j)^2V_j,\qquad
 V_j\ge\frac{8\pi^2A_0}{9}=:v_0.                     \tag{3}
\]
Bishop--Gromov comparison using the diameter bound provides an upper
volume bound \(V_j\le V_0(D)\) and, at every point, lower ball-volume
bounds \(\operatorname{Vol}B_\rho\ge c(D,A_0)\rho^4\) for
\(0<\rho\le1\). Applying the local Jiang--Naber \(L^2\)-curvature
bound on a uniformly finite fixed-scale cover yields
\[
                    \int_{M_j}|\operatorname{Rm}|^2\le E(D,A_0).
 \tag{4}
\]

Use **bounded-Ricci orbifold compactness**, not an Einstein-only bubble
theorem: two-sided Ricci bounds, noncollapse, bounded diameter and bounded
critical curvature energy give an orbifold subsequential limit with
\(C^{1,\alpha}\), weak \(W^{2,p}\) orbifold metric and regular-locus
convergence. Anderson explicitly distinguishes this result from the
earlier Einstein theorem in the introduction of [A04], referring to [A90].
The varying-manifold version uses (4). The same bounded-Ricci conclusion is
used explicitly in Honda--Mondino [HM25], proof of Theorem 2, p. 452.
The Ricci lower bound gives ordinary, irreducible quotient neighborhoods,
not a union of several cones at one vertex; see [A04], Remark 2.1(i).

On regular harmonic charts the metric equation is
\[
 g_j^{ab}\partial_a\partial_b(g_j)_{uv}
    =-2(\operatorname{Ric}_{g_j})_{uv}
                +Q_{uv}(g_j,\partial g_j).             \tag{5}
\]
The Ricci error itself tends uniformly to zero. The limiting equation is
\(\operatorname{Ric}_h=-h\); elliptic bootstrapping makes \(h\) smooth
on the regular locus. Applying interior estimates to the difference of
(5) and its limiting equation gives strong \(W^{2,p}\) convergence on
smaller charts. The right-hand side converges strongly; no derivative of
the Ricci error is needed. The limit already has \(W^{2,p}\) regularity
in local orbifold covers by the compactness theorem. Its Einstein equation
holds almost everywhere there (a point has zero measure); harmonic-coordinate
regularity and elliptic bootstrapping therefore make \(h\) a smooth
Einstein orbifold metric at the singular points as well.

### Proof: saturation selects a global complex structure

The inherited actual-form theorem supplies smooth self-dual \(\omega_j\)
and choices \(\eta_j\downarrow0\) with
\[
 \|\omega_j\|_\infty\le2\sqrt3,\qquad
 \fint(|\omega_j|^2-2)^2\le720\kappa_j+\eta_j,
\]
\[
 \fint|\nabla\omega_j|^2
       \le13\kappa_j+4\sqrt{2\kappa_j}+\eta_j.          \tag{6}
\]
Only the first-order part of that theorem is used. In particular its
additional second-order estimate and square-cost hypothesis are not used.
Because \(V_j\le V_0\), the unnormalized derivative and amplitude errors
in (6) tend to zero. Pull back to the same regular-locus embeddings as the
metrics. Rellich compactness on an exhaustion and a diagonal subsequence
give a global weak limit \(\omega_\infty\). It satisfies
\[
 \nabla^h\omega_\infty=0,\qquad
 *_h\omega_\infty=\omega_\infty,\qquad
 |\omega_\infty|^2=2.                                  \tag{7}
\]
The norm assertion follows from strong local \(L^2\) convergence, the
uniform amplitude bound and (6); it is not inferred merely from nonzero
total mass. The regular locus is connected. The form is one global limit
of global forms, rather than locally chosen eigenvectors.

In a uniformizing ball at a singular point, lift (7) to the punctured ball.
The smooth extended metric has bounded connection coefficients. The parallel
equation, constant norm and short paths imply that the lift has a unique
continuous limit at the origin. Its first-order parallel equation then
gives smooth extension. The extension is invariant under the finite chart
group because the form was invariant on the punctured ball. Thus (7) holds
on the whole orbifold. The relation
\(\omega_\infty(u,v)=h(Ju,v)\) defines a parallel orthogonal complex
structure: a self-dual two-form of norm \(\sqrt2\) in dimension four
squares to \(-I\) in this relation. Parallelism gives integrability and
closedness. This proves Theorem A. \(\square\)

## 2. What the small-scale fillings do, and do not, inherit

There is a useful conclusion stronger than an unconstrained Ricci-flat
blow-up. Set \(w_j=\sqrt6|W^+_{g_j}|\). The classical completed-square
estimate used in the actual-form proof gives
\[
 \fint(w_j-2)^2\le2\kappa_j,\qquad
 \int_E|W^+_{g_j}|^2\le\frac43\operatorname{Vol}(E)
                          +\frac23\kappa_jV_j         \tag{8}
\]
for every measurable subset \(E\subset M_j\).

**Proposition B (chirality of smooth ALE bubbles).** Any smooth complete
nonflat pointed limit obtained by harmonic-radius blow-up at scales
\(\rho_j\to0\), with convergence on compact subsets, is Ricci-flat and
anti-self-dual in the inherited orientation. With the Euclidean growth and
finite energy supplied by (3)--(4), it is ALE.

Indeed \(|\operatorname{Ric}_{\rho_j^{-2}g_j}|\le3\rho_j^2\).
On each rescaled ball of fixed radius \(R\), (8), scale invariance of
four-dimensional Weyl energy and the unscaled upper ball-volume bound give
\[
 \int_{B_R}|W^+_{\rho_j^{-2}g_j}|^2
       \le C\rho_j^4R^4+\frac23\kappa_jV_0\longrightarrow0.
\]
Harmonic-coordinate convergence as in (5) is strong enough to pass curvature
in \(L^2\). The limit has \(W^+=0\). Bando--Kasue--Nakajima's asymptotic
theorem applies to this **exact smooth Ricci-flat limit**, not to the input
metrics. This proves the proposition.

Wright's classification [W11], Theorem A, now applies legitimately: a
non-simply-connected nonflat bubble is a finite cyclic quotient of a
Gibbons--Hawking space and is Kähler; simply connected bubbles are the
hyperkähler ALE spaces. Şuvaina's [S11], Theorem B, relates the resulting
Ricci-flat Kähler complex surface to a **minimal resolution of a fiber**
of a local Q-Gorenstein deformation. The theorem does not say that the
particular complex structure of every bubble is already a smooth Milnor
fiber. Nor has the chosen bubble complex structure been identified with
the limiting complex marking at the outer orbifold link.

In particular, Proposition B is not a classification of the entire compact
region removed from \(M_j\) at a singular point. Such a region can involve
several scales and intermediate orbifold levels. No bubble-tree energy
identity or assertion that its topology equals one terminal bubble is used
below. The realization condition is imposed on the **whole actual filling**.

A concrete distinction is the quotient singularity
\(\mathbb C^2/\frac14(1,1)\). Its minimal resolution has a single
\((-4)\)-sphere, so a compact resolution neighborhood has \(b_2=1\).
Its Q-Gorenstein Milnor fiber is instead a rational ball with
\(b_2=0\) and \(\pi_1=\mathbb Z_2\). They fill the same oriented
quotient link but are not diffeomorphic. This classical example already
prevents identifying a smoothing filling from the link alone. It is not
claimed that both fillings arise from sequences satisfying (2).

## 3. A marked smoothing criterion returning to the original smooth type

Let \((X,h,J)\) be the limit in Theorem A, with singular points
\(x_1,\ldots,x_N\). Choose small disjoint quotient neighborhoods \(U_\nu\)
with smooth links \(Y_\nu\), and put
\[
                    K=X\setminus\bigcup_\nu\operatorname{int}U_\nu.
\]
Regular-locus convergence gives oriented smooth embeddings
\(\iota_j:K\hookrightarrow M_j\), including collars of the boundary.
Let \(B_j\) be the closure of their complement. The condition below
includes that \(B_j\) has exactly one connected filling \(B_{\nu,j}\)
at each boundary component, so no unproved topological separation statement
is hidden in the notation.

A **projective Q-Gorenstein smoothing** is a proper flat projective family
\(\pi:\mathcal X\to\Delta\) with central fiber \(X\), smooth fibers
\(X_t\) for sufficiently small \(t\ne0\), and relative canonical divisor
\(K_{\mathcal X/\Delta}\) Q-Cartier. Use the complex structure \(J\)
just produced, not an unrelated complex structure on the underlying space.
After shrinking \(\Delta\), the exterior is differentiably trivial by
Ehresmann's theorem with boundary. Its identification with \(K\) equips
each local Milnor fiber \(F_{\nu,t}\) with a specified boundary marking
by \(Y_\nu\).

**Theorem C (marked Q-Gorenstein realization).** Suppose \(X\) admits
such a smoothing. For an index \(j\), assume that for some small regular
parameter \(t_j\ne0\) each whole filling admits an orientation-preserving
diffeomorphism
\[
                    f_{\nu,j}:B_{\nu,j}\longrightarrow F_{\nu,t_j}
 \tag{9}
\]
whose boundary restriction agrees, up to isotopy, with the marking induced
by \(\iota_j\) and the exterior trivialization. Then the same oriented
smooth manifold \(M_j\) admits a negative KE metric. If (9) holds for all
sufficiently large indices of the extracted subsequence, the conclusion
holds for all of those indices.

**Proof.** An isotopy on a boundary extends across its collar. Modify the
maps (9) there so that they agree exactly with the exterior identification.
Collar-compatible gluing then gives an oriented diffeomorphism
\[
                           M_j\cong X_{t_j}.           \tag{10}
\]
The KE orbifold has positive canonical orbifold bundle: the curvature form
of its canonical Hermitian metric is \(-\rho_h=\omega_h>0\). A divisible
power of the canonical bundle descends to the quotient space, and the
orbifold Kodaira embedding theorem makes \(K_X\) ample as a Q-divisor.
Equivalently this is the usual canonical polarization of a negative KE
orbifold with quotient singularities.

Choose an index \(m\) such that \(mK_{\mathcal X/\Delta}\) is Cartier.
Its restriction to \(X\) is ample. Openness of relative ampleness, after
shrinking the base, makes \(K_{X_t}\) ample on each nearby smooth fiber.
The Aubin--Yau theorem gives a smooth Kähler metric \(h_t\) with
\(\operatorname{Ric}_{h_t}=-h_t\) on \(X_t\). Pulling it back through
(10) proves the claim. \(\square\)

Thus the output meets the Yau26 existence requirement on the covered smooth
types. It need not be close to \(g_j\), and no invertibility or integrability
assumption on a tensor Einstein gluing operator is needed. The analytic
compactification and the marked smooth-type matching remain different steps.

The relative condition (9) is finite local topology plus gluing data. It is
not replaceable by equality of fundamental groups, Betti numbers, links or
intersection forms. It is also not inferred from the ALE classification.
Once the marked data are known, however, no global diffeomorphism or complex
structure on \(M_j\) has to be assumed: (10) constructs the former and
pulls back the latter.

## 4. An algebraically checkable smoothing input

For quotient surface singularities, the local Q-Gorenstein smoothable
types are the rational double points and the cyclic singularities
\[
                  \frac1{dn^2}(1,dna-1),\qquad
                 d>0,\quad n\ge2,\quad (a,n)=1.       \tag{11}
\]
These are the class T singularities of Kollár--Shepherd-Barron. A local
smoothing at each singularity does not itself supply a global smoothing.

**Corollary D (cohomological realization test).** In Theorem C the global
smoothing assumption is satisfied if the normal projective surface \(X\)
has only class T singularities and its minimal resolution
\(r:Z\to X\), with reduced exceptional divisor \(E\), satisfies
\[
                         H^2(Z,T_Z(-\log E))=0.        \tag{12}
\]
Consequently (11), (12) and the marked filling condition (9) imply negative
KE existence on the original \(M_j\).

This is exactly the globalization criterion of Lee--Park [LP07], Theorem
2.1; their proof passes from (12) to vanishing of the global obstruction
sheaf cohomology, then globalizes the local Q-Gorenstein deformations.
We use its projective family, not an arbitrary first-order deformation.
Condition (12) is sufficient, not necessary, and is not claimed to follow
from the Ricci or gauge estimates.

For rational double points the standard Milnor filling is diffeomorphic to
the ADE resolution plumbing. For the cyclic types the Milnor filling,
not generally the full exceptional plumbing, is the relevant object; the
case \(d=1\) is the usual rational-ball replacement. Răsdeaconu--Şuvaina
[RS09], Proposition 2.6 and Remark 2.9, give the classical algebraic
rational-blowdown interpretation. To apply this interpretation to an
arbitrary \(M_j\), its actual exterior and boundary marking must still
match the algebraic surgery. Theorem C expresses precisely that requirement.

**Concrete ADE specialization.** Suppose the limit complex surface is a
degree \(d\ge5\) hypersurface in \(\mathbb{CP}^3\) with only nodes.
A generic pencil \(F_0+tG=0\), after restricting to a small disk, is a
global Gorenstein smoothing; adjunction gives
\(K_{X_t}=\mathcal O_{X_t}(d-4)\), which is ample. Each local Milnor
fiber has the oriented smooth type of the \((-2)\)-disk bundle over
\(S^2\). If the actual complementary pieces are these bundles with the
Milnor boundary markings, Theorem C applies. This specialization needs no
verification of (12), because the global smoothing is written explicitly.
It is a classical family illustrating a nonempty, checkable matching test,
not a newly constructed family of Einstein manifolds. In particular a
vanishing \(\pi_2\) condition is absent, not reintroduced under another name.

## 5. Precise scope and the remaining implication

The conclusions established from the raw data alone are
\[
 \boxed{\text{(2)}\ \Longrightarrow\ \text{negative KE orbifold limit}}
\]
and the anti-self-duality of its smooth Ricci-flat ALE blow-ups. With the
additional global smoothing and marked filling inputs, they become
\[
 \boxed{\text{negative KE orbifold}
       +\text{global QG smoothing}
       +\text{marked Milnor fillings}
       \Longrightarrow\text{negative KE on the original smooth type}.}
\]
These statements handle a genuine alternative to excluding all bubbles:
allow singular limits and recover the smooth type by algebraic realization.

There is no proof here that (2) forces all singularities to be class T in
their limiting complex representation, that their local smoothings
globalize, or that each entire geometric filling has the correct relative
Milnor type. Classifying terminal ALE spaces does not prove those three
claims. Resolving them, or supplying a counterexample to one, is the actual
remaining issue for unconditional realization without the topological
no-bubble hypothesis. Neither a full energy identity nor a new numerical
gap constant substitutes for this missing information.

## Primary references and exact roles

- [A90] M. T. Anderson, *Convergence and rigidity of manifolds under Ricci
  curvature bounds*, Inventiones Mathematicae 102 (1990), 429--445.
  [Original publication](https://doi.org/10.1007/BF01233434).
- [A04] M. T. Anderson, *Orbifold compactness for spaces of Riemannian metrics
  and applications*, 2004 version. Introduction after (1.2), Remark 2.1(i),
  and Remark 2.11 specify the bounded-Ricci scope used here.
  [Author manuscript](https://arxiv.org/html/math/0312111).
- [JN21] W. Jiang and A. Naber, *L2 curvature bounds on manifolds with bounded
  Ricci curvature*, Annals of Mathematics 193 (2021).
  [Original publication](https://annals.math.princeton.edu/2021/193-1/p02).
- [HM25] S. Honda and A. Mondino, *Poincaré inequality for one-forms on four
  manifolds with bounded Ricci curvature*, Archiv der Mathematik 124 (2025),
  449--455. Proof of Theorem 2 independently records the exact orbifold
  compactness regularity, not a new source for the original theorem.
  [Published paper](https://d-nb.info/1367095026/34).
- [BKN89] S. Bando, A. Kasue and H. Nakajima, *On a construction of coordinates
  at infinity on manifolds with fast curvature decay and maximal volume
  growth*, Inventiones Mathematicae 97 (1989), 313--349, Theorem 1.5.
  [Original publication](https://doi.org/10.1007/BF01389045).
- [W11] E. P. Wright, *Quotients of gravitational instantons*, Theorem A.
  [Author manuscript](https://arxiv.org/html/1102.2442).
- [S11] I. Şuvaina, *ALE Ricci-flat Kähler metrics and deformations of quotient
  surface singularities*, Theorems A, B and 2.2.
  [Author manuscript](https://arxiv.org/html/1102.2672).
- [LP07] Y. Lee and J. Park, *A simply connected surface of general type with
  p_g=0 and K²=2*, Inventiones Mathematicae 170 (2007), 483--505, Theorem 2.1.
  [Author manuscript](https://arxiv.org/pdf/math/0609072).
- [RS09] R. Răsdeaconu and I. Şuvaina, *The algebraic rational blow-down*,
  Propositions 2.6--2.7 and Remark 2.9.
  [Author manuscript](https://math.vanderbilt.edu/rasdear/rbdarxiv.pdf).
- [Bai57] W. L. Baily, *On the imbedding of V-manifolds in projective space*,
  American Journal of Mathematics 79 (1957), 403--430.
  [Original publication](https://doi.org/10.2307/2372689).
- [AY] T. Aubin's and S.-T. Yau's negative first-Chern-class KE existence
  theorem; S.-T. Yau, *On the Ricci curvature of a compact Kähler manifold
  and the complex Monge--Ampère equation, I*, CPAM 31 (1978), 339--411.
  [Original publication](https://doi.org/10.1002/cpa.3160310304).

Theorems A and C use only the parts of these results specified in their
proofs. Baily and Aubin--Yau are invoked as classical existence/embedding
theorems, not reproved here. The first-line actual-form estimates remain
an inherited proof dependency, not an external literature theorem.
