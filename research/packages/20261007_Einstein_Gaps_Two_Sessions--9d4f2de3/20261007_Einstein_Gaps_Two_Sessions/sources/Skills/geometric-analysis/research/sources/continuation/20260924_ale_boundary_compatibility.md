# Removing the Weyl hypothesis by the topology of ALE embeddings

24 September 2026. This note supplies the previously missing input in the
[compact-regime realization proof](20260923_compact_realization.md).
The stronger ALE nonembedding theorem is **an existing result**, not a new
classification discovered here: it is Zhang's theorem with the noncompact
extension stated explicitly by Bamler--Chen. Its application changes the
scope of the project's realization theorem substantially.

In particular, the residual possibility recorded in
[the preceding topology note](20260923_topological_core_scope.md), namely a
mixed-chirality rational-ball bubble in the universal cover, can now be
excluded. No classification of arbitrary Ricci-flat ALE metrics is assumed.

## 1. The classical input that closes the remaining bubble alternative

**ALE nonembedding lemma (Zhang; Bamler--Chen).** Let \(N\) be a smooth
four-manifold, possibly noncompact, with
\[
 H_2(N;\mathbb Z)=0,\qquad H_1(N;\mathbb Z)\text{ torsion-free}.
 \tag{1}
\]
No compact smooth domain \(B\subset N\) has interior diffeomorphic to a
nonflat complete Ricci-flat ALE four-manifold.

The precise noncompact formulation is
[Bamler--Chen, Lemma 4.35, p. 41](https://arxiv.org/pdf/2305.03154),
which cites [Zhang, Theorem 6.1 and Lemmas 6.2--6.5,
pp. 378--382](https://msp.org/pjm/2019/303-1/pjm-v303-n1-p14-s.pdf).
In the published version of Bamler--Chen, the statement is still Lemma 4.35:
[DOI 10.1002/cpa.70024](https://doi.org/10.1002/cpa.70024).
The isolated \(H_1(M)\) in its printed statement denotes the ambient
\(H_1(N)\), as its following proof makes explicit. We use the lemma only
when this group is zero.

Here is the mechanism, to distinguish this input from the unavailable
classification of all Ricci-flat ALE spaces. In an ambient with
\(H_1=H_2=0\), write \(Y=\partial B=S^3/\Gamma\) and
\(C=N\setminus\operatorname{int}B\). Integral Mayer--Vietoris gives
\[
 H_2(B;\mathbb Z)=0,\qquad
 H_1(Y;\mathbb Z)\simeq H_1(B;\mathbb Z)\oplus H_1(C;\mathbb Z).
 \tag{2}
\]
The ALE fundamental group is finite, and the end group surjects onto it.
Thus \(H_1(B,Y;\mathbb Z)=0\). Duality and the universal coefficient
theorem identify the kernel of \(H_1(Y)\to H_1(B)\) with a group
isomorphic to \(H_1(B)\). The splitting in (2) respects this projection,
so
\[
                  H_1(Y)\simeq G\oplus G.               \tag{3}
\]
This is stronger than merely requiring that \(|H_1(Y)|\) be a square.

Zhang's spherical-space-form calculation reduces the nontrivial possibilities
in (3) to binary dihedral groups of order \(8n\), \(n\ge1\), and the
binary icosahedral group. His representation lemma and eta calculation give,
up to orientation,
\[
 |\eta(Y)|=\frac{8n^2+1}{12n}\quad\text{or}\quad\frac{361}{180},
 \qquad\text{respectively}.                            \tag{4}
\]
Both exceed \(2/3\). On the other hand, \(b_2(B)=0\), finite first
homology, connected boundary and duality give \(\chi(B)=1\), \(\tau(B)=0\).
Ricci-flat Chern--Gauss--Bonnet and APS signature, in curvature-operator
norms, imply
\[
 \begin{split}
 E_++E_-&=8\pi^2\left(1-|\Gamma|^{-1}\right),\\
 E_+-E_-&=12\pi^2\eta(Y),\qquad
 E_\pm=\int|W^\pm|^2\ge0.
 \end{split}                                           \tag{5}
\]
Consequently
\[
 |\eta(Y)|\le\frac23\left(1-|\Gamma|^{-1}\right)<\frac23,
 \tag{6}
\]
contradicting (4). The trivial end group gives zero total curvature in
(5), hence flatness. This explains why a mixed-chirality rational ball
does not evade the argument: nonnegativity of **both** energies is already
incompatible with its boundary data. The argument does not set either
Weyl half to zero.

For the quaternion test \(\Gamma=Q_8\), (3) is indeed possible: the
boundary has \(H_1=(\mathbb Z/2)^2\). It is (6), not this group
calculation alone, that excludes a Ricci-flat rational-ball filling:
\(3/4>7/12\). This separates the topological and geometric restrictions.

## 2. Vanishing second homotopy suffices; torsion in the first is allowed

**Theorem 1 (all-ALE-core exclusion).** Let \(M\) be a connected smooth
oriented four-manifold with \(\pi_2(M)=0\). No large compact core of a
nonflat complete smooth Ricci-flat ALE four-manifold embeds smoothly in
\(M\). No torsion-free assumption on \(\pi_1(M)\) is needed.

**Proof.** Let \(i:B\hookrightarrow M\) be such an embedding and let
\(p:\widetilde M\to M\) be the universal cover. Hurewicz gives
\[
 H_1(\widetilde M;\mathbb Z)=H_2(\widetilde M;\mathbb Z)=0.
 \tag{7}
\]
The fundamental group of a Ricci-flat ALE space is finite. A component
\(\widehat B\) of \(p^{-1}(i(B))\) is therefore a **finite** cover of
\(B\): its degree is the order of the finite image of
\(i_*:\pi_1(B)\to\pi_1(M)\). In particular, it is a compact smooth
domain in \(\widetilde M\). This step neither assumes that the core
fundamental group injects nor that its image is trivial.

The interior of \(\widehat B\) carries the lifted complete Ricci-flat
metric. A finite cover of an ALE space has finitely many lifted ALE ends
and Euclidean volume growth. It has only one end: if it had two, the
nonnegative-Ricci splitting theorem would split it as a line times a
compact manifold, contradicting Euclidean four-dimensional volume growth.
Thus the lifted space is itself nonflat Ricci-flat ALE. Apply the classical
lemma to its compact domain \(\widehat B\subset\widetilde M\), using
(7), to obtain a contradiction. \(\square\)

For completeness, finiteness of the ALE fundamental group can also be
seen directly from the end: take the cover corresponding to the image
of \(\pi_1(Y)\to\pi_1(B)\). This subgroup is finite. If its index
were greater than one, one lifted end has degree one and is separated
from the rest by a compact cross-section. The complete lifted metric
would have at least two ends and Euclidean lower volume growth, again
contradicting splitting. Therefore the end group surjects onto the full
fundamental group. This reasoning uses Ricci-flatness and the ALE end,
not any holonomy classification. The same end-cover/splitting argument
appears in [Wright, Section 3 and Proposition 1](https://arxiv.org/html/1102.2442);
only that argument is used, not the paper's half-flat classification.

The conclusion is strictly broader in topology than the previous condition
\(\pi_1\) torsion-free, \(\pi_2=0\). For example,
\(L(p,q)\times S^1\) has vanishing \(\pi_2\) and fundamental group
\((\mathbb Z/p)\times\mathbb Z\); homotopy four-spheres also have
vanishing \(\pi_2\). These illustrate the topological scope, not a claim
that every example has the near-Einstein inputs of the next theorem.

## 3. Bounded-geometry realization without gauge saturation or Weyl bounds

**Theorem 2 (harmonic compactness).** Fix \(K,D,v>0\) and
\(0<\alpha<1\). Closed connected smooth oriented four-manifolds with
\[
 \pi_2(M)=0,\qquad
 \|\operatorname{Ric}^{\sharp}\|_{\infty,\mathrm{op}}\le K,
 \qquad\operatorname{diam}(g)\le D,\qquad V_g\ge v
 \tag{8}
\]
have a uniformly positive \(C^{1,\alpha}\) harmonic radius. They are
precompact modulo diffeomorphisms in \(C^{1,\beta}\), \(\beta<1\), and
weak \(W^{2,p}\), \(p<\infty\), and have finitely many smooth types.

**Proof.** The analytic argument of
[compact realization, Sections 3--4](20260923_compact_realization.md)
is used up to, but not including, its one-half Weyl step. Bishop--Gromov
gives uniform noncollapse on fixed scales and a total-volume upper bound.
Jiang--Naber supplies the full curvature-energy bound. If the minimum
harmonic radius \(\rho_j\) tends to zero, rescale by \(\rho_j^{-2}\).
The normalized harmonic atlases converge, Ricci tends uniformly to zero,
and the harmonic-coordinate metric equation upgrades convergence locally
to strong \(W^{2,p}\) for finite \(p\). The limit is smooth Ricci-flat.
Recovery of harmonic charts with strict margins excludes a flat limit.

Euclidean volume growth and finite curvature energy make this limit ALE
by Bando--Kasue--Nakajima. Only positive-order ALE asymptotics are needed;
no optimal decay-order assertion is used. Its smooth compact core embeds
in each sufficiently late \(M_j\), contradicting Theorem 1. There is
**no need to force \(W^+\) or \(W^-\) to vanish**. The remaining
finite-atlas compactness argument is unchanged. \(\square\)

**Theorem 3 (same-smooth-type realization).** Fix \(D,v>0\). There is
\(\varepsilon(D,v)>0\), uniform over smooth types and
\(\sigma\in\{-1,+1\}\), such that
\[
 \begin{gathered}
 \pi_2(M)=0,\qquad \operatorname{diam}(g)\le D,\qquad V_g\ge v,\\
 \delta_\sigma(g):=
 \|\operatorname{Ric}^{\sharp}_g-\sigma I\|_{\infty,\mathrm{op}}
          <\varepsilon(D,v)
 \end{gathered}
 \quad\Longrightarrow\quad
 \exists h\text{ on }M:\ \operatorname{Ric}_h=\sigma h.
 \tag{9}
\]

**Proof.** Otherwise take counterexamples with the fixed data and
\(\delta_{\sigma_j}(g_j)\to0\). Pass to a subsequence with constant
sign. Theorem 2 applies with \(K=2\) to late terms and identifies them
with a fixed smooth manifold. In harmonic coordinates the limiting
metric satisfies \(\operatorname{Ric}=\sigma g\) weakly. Elliptic
regularity makes it smooth. Pull it back to the original smooth manifolds,
contradicting their defining absence of such an Einstein metric.
\(\square\)

In the positive case, \(\delta_+<1/2\) gives
\(\operatorname{Ric}\ge g/2\); Bonnet--Myers supplies
\(\operatorname{diam}\le\pi\sqrt6\). Thus for each \(v>0\),
\(\pi_2=0\), \(V_g\ge v\), and sufficiently small \(\delta_+\)
already imply a positive Einstein metric, with threshold depending only
on \(v\). This still retains the noncollapse input.

On the negative side an actual conformally solvable monopole class with
\((a_g^+)^2\ge A_0>0\) gives
\[
 V_g\ge\frac{2\pi^2 A_0}{(1+\delta_-(g))^2}
       \ge\frac{8\pi^2 A_0}{9}\quad(\delta_-\le1/2).
 \tag{10}
\]
Hence (9) yields a threshold \(\varepsilon(D,A_0)\) from this actual
class input and diameter alone. Unlike the preceding KE realization
theorem, **no smallness of \(\mathfrak D_2/V\) is required**. The
conclusion is negative Einstein, not necessarily Kähler--Einstein.
That already satisfies the existence output of the adopted Yau26 problem.

## 4. What is resolved, and what is not

This closes the entire compact, noncollapsed bubble alternative on
\(\pi_2=0\) topology. A hypothetical negative-side Yau26 counterexample
sequence in that class, with uniform positive actual projection budget,
must have diameters tending to infinity: any bounded-diameter subsequence
would contradict (9)--(10). No near-saturation is necessary for this
escape conclusion.

On the positive side, if \(\pi_2(M_j)=0\), no \(M_j\) admits any
Einstein metric, and \(\delta_+(g_j)\to0\), then necessarily
\(V_{g_j}\to0\). Otherwise a subsequence has \(V_{g_j}\ge v>0\),
and Myers plus Theorem 3 produces a positive Einstein metric on every
sufficiently late member of that subsequence. Thus, within the
\(\pi_2=0\) topology, the two signs have different remaining escape
mechanisms: positive candidates must collapse in total volume; negative
candidates with a positive actual projection budget must escape in
diameter.

The original dimension-only problem still allows diameter escape,
collapse without a supplied volume budget, and topology with nonzero
\(\pi_2\). Those are not excluded here. The theorem does not decide
whether the fixed non-Kähler shear examples admit general Einstein metrics:
their known approximating sequence has diverging diameter.

The old near-saturation theorem retains its independent stronger geometric
output: its actual forms recover a global parallel form and hence KE.
For **general Einstein existence** in the compact regime, however,
saturation and the one-sided Weyl assumptions are now unnecessary.

The mathematical increment in this note is the explicit composition of
the full ALE nonembedding input, the finite-cover lift, and the preserved
almost-Einstein compactness argument. Zhang's boundary/eta obstruction and
Bamler--Chen's noncompact formulation are credited as existing results.
No assertion of world-first priority for the resulting compact-regime
corollary, or classification of all Ricci-flat ALE spaces, is made.

For the historical comparison, [Anderson's survey, Corollary 5.8](https://www.math.stonybrook.edu/~anderson/einsurv.pdf)
already gives exclusion of the orbifold boundary of the exact Einstein
moduli space under vanishing \(H_2(M;\mathbf F)\) for every field.
Bamler--Chen explicitly credit Anderson's earlier work for the
nonembedding idea. The composition here uses the later explicit
noncompact lemma, the finite-cover lift under \(\pi_2=0\), and
bounded-Ricci harmonic compactness to handle varying smooth types and
pointwise approximate Einstein inputs. This distinguishes the statements
being used; it does not establish that this composed corollary was absent
from the literature.
