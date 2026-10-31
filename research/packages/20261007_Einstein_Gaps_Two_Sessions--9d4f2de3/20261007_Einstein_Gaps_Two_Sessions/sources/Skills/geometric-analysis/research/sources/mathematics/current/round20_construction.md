# A signature barrier to enlarging the slow-collar construction

22 September 2026.

## 1. Result and its scope

The proposed extension to arbitrary representations of a free quotient is
already contained in [Round 11](round11_closed_gluing.md), with zero circle
shear. The standard geometric free quotients were already treated in the
[earlier analysis](skill/research/20260912.tex), immediately before
`BUN:WP-signature`. This includes noncommuting and pseudo-Anosov monodromy.
No new smooth near-Einstein family is obtained by repeating that argument.

There is, however, a quantitative obstruction to extending the same
hyperbolic-base, hyperbolic-fibre, minimal-fibre construction to surface
bundles with nonzero signature. Let

\[
 \Sigma_p\longrightarrow M\stackrel\pi\longrightarrow\Sigma_q,
 \qquad p,q\ge2,\qquad \chi=4(p-1)(q-1),\quad \tau=\tau(M).
 \tag{1}
\]

Suppose \(g\) makes \(\pi\) a Riemannian submersion, every fibre has
intrinsic curvature \(-\kappa\), the base has curvature \(-\kappa\),
and every fibre is minimal, for a fixed \(\kappa>0\). There is no
restriction on base or fibre injectivity radii, connection curvature, or
monodromy. Then

\[
 \boxed{\quad
 \frac{\|g^{-1}\operatorname{Ric}_g+\kappa I\|_{\infty,\mathrm{op}}}
      {\kappa}
 \ \ge\ \frac{3|\tau|}{2\chi}.
 \quad}                                                        \tag{2}
\]

In particular, if \(\tau\ne0\), none of these metrics can form a
pointwise near-Einstein sequence on the fixed bundle. A flat connection
does not remove the obstruction. Area-preserving flat surface bundles of
nonzero signature actually exist, by Kotschick--Morita, Theorem 1 of
[*Signatures of foliated surface bundles and the symplectomorphism groups
of surfaces*](https://arxiv.org/pdf/math/0305182).

This is a theorem about the stated submersion geometry, not nonexistence
of Einstein metrics on \(M\). Kodaira fibrations already give nonzero
signature examples with negative Kähler--Einstein metrics; these were
explicitly retained in [Round 10](round10_bundle.md). The new deduction
here is the explicit linear signature cost for the minimal hyperbolic
submersion class, obtained by combining earlier moduli-energy and Ricci
identities, rather than a construction or a literature-priority claim.
The moduli-energy obstruction itself was already proved in
`BUN:WP-signature`; the submersion blocks and stronger exact rigidity
were already proved in `SUB:blocks`, `SUB:integrable`, and `SUB:basic`
of the earlier analysis. They are retained below as inputs, with their
conventions made explicit.

[Round 18](round18_twisted_operator.md) concerns finite-monodromy exact
quotients and does not enlarge the slow-collar topological class to
nonzero signature. Section 7 gives a short direct proof of an inherited
rigidity corollary identifying the exact metrics in the present class.

## 2. Why all free-quotient examples were already included

Fix \(\rho=\bar\rho\circ r\), where
\(r:\pi_1(\Sigma_q)\twoheadrightarrow F_s\) and
\(\bar\rho:F_s\to\operatorname{Mod}(\Sigma_p)\) is arbitrary. Realize
\(r\) by a map from the base to a rose. Choose one regular interior
point on each edge. Its inverse image is a disjoint multicurve; each
complementary component maps into the tree obtained by cutting the rose
at these points. The monodromy on each complementary component is
therefore trivial. Inessential and parallel curves can be removed or
their adjacent disc/annular product regions absorbed. The remaining
base pieces have negative Euler characteristic. The bundle is assembled
from product pieces by fixed fibre diffeomorphisms on the seams.

Equivalently, free quotients are represented geometrically by systems of
disjoint cooriented curves; see Marzantowicz--Michalak,
[*Relations between Reeb graphs, systems of hypersurfaces and epimorphisms
onto free groups*](https://arxiv.org/abs/2002.02388). The construction above
only needs triviality of the restrictions. For genus at least two,
contractibility of \(\operatorname{Diff}_0\) identifies these bundles
with their mapping-class monodromy, so no extra two-dimensional clutching
class has been omitted.

Set \(u_e=0\) in Round 11, formula (1), and choose its fibre paths from
\(h_v\) to \(f_e^*h_w\). All its complete Ricci estimates apply unchanged.
No commutativity, finite order or common invariant hyperbolic metric is
needed. The resulting fixed bundle has

\[
 \|\operatorname{Ric}_{g_\ell}+\kappa g_\ell\|_{g_\ell,\mathrm{op}}
 \longrightarrow0,
 \qquad \operatorname{Vol}(g_\ell)=\frac{4\pi^2\chi}{\kappa^2}.
 \tag{3}
\]

Its signature is zero. This follows either from Novikov additivity of
the product pieces or from \(H^2(F_s;\mathbb R)=0\) and the signature
characteristic class. Having noncommuting monodromy alone is therefore
not a test for leaving the inherited family.

## 3. A normalization-independent moduli-energy calculation

This is the inherited `BUN:WP-signature` calculation in an explicit
real-tensor normalization, not a new signature or energy formula.

It is useful to specify the metric normalization instead of silently
mixing conventions for the Weil--Petersson metric. On Teichmüller space
use the real tensor \(L^2\) metric

\[
 \mathsf G_T(k,l)=\int_F\langle k,l\rangle_{\bar h}\,dA_{\bar h},
 \quad K_{\bar h}=-1,
 \quad \operatorname{tr}_{\bar h}k=\operatorname{div}_{\bar h}k=0,
 \tag{4}
\]

and its Kähler form \(\Omega_T(k,l)=\mathsf G_T(Jk,l)\). Here \(k,l\)
are actual derivatives of the hyperbolic metric, not quadratic
differentials rescaled by an unstated constant. This is the convention
in Guillarmou--Moroianu, equations (24)--(27) and Lemma 26 of
[*Chern--Simons line bundle on Teichmüller space*](https://arxiv.org/pdf/1102.1981).
With this convention,

\[
 [\Omega_T]=8\pi^2\kappa_1,
 \qquad \kappa_1=\pi_*e(T_vM)^2.
 \tag{5}
\]

One can check the factor directly from the same vertical connection.
For unit-curvature fibre TT derivatives \(A=\bar h^{-1}k\) and
\(B=\bar h^{-1}l\), its horizontal curvature is
\(-[A,B]/4\), mixed curvature vanishes at the chosen horizontal
point, and fibre curvature is the unit rotation. Consequently
\(\int_F\operatorname{tr}(R\wedge R)=-\Omega_T\).
Since \(p_1(T_v)=-\operatorname{tr}(R\wedge R)/(8\pi^2)=e(T_v)^2\),
(5) follows. This also avoids relying on a convention for a complex
Beltrami inner product. The Chern--Weil computation concerns a universal
fibre connection and does not assume that the physical bundle connection
in (2) is the TT connection.

Let \(f\) be the equivariant fibre-moduli map on the universal cover of
the base. Its invariant tensors descend to the base; equivalently use
the moduli orbifold, keeping stabilizers. The tangent splitting
\(TM=T_vM\oplus\pi^*TB\), together with \(e(TB)^2=0\), gives

\[
 3\tau=\langle e(T_vM)^2,[M]\rangle,
 \qquad \int_B f^*\Omega_T=24\pi^2\tau.
 \tag{6}
\]

For every oriented base metric, Kähler Cauchy--Schwarz gives

\[
 |f^*\Omega_T(e_1,e_2)|
 \le\tfrac12\bigl(|df(e_1)|_T^2+|df(e_2)|_T^2\bigr),
 \quad
 \boxed{\int_B|df|_T^2\,dA_B\ge48\pi^2|\tau|.}             \tag{7}
\]

No compact-moduli or noncollapse estimate enters this bound. If the
moduli map is constant off disjoint collars and depends on only the
collar distance within each, it has rank at most one everywhere.
Then \(f^*\Omega_T=0\) and necessarily \(\tau=0\). Thus a nonzero
surface-relation class cannot be carried solely by these one-dimensional
paths. Rank-two variation must remain somewhere, even if the base
degenerates. This is the precise obstruction, not an assertion that
every zero-signature representation factors through a free group.

## 4. All Ricci blocks in the flat, area-preserving model

These specialize the earlier `SUB:blocks` and `SUB:vv-integrable` formulas.

First suppose the connection is flat and preserves a fibre area form.
In its flat charts write

\[
 g=b_{ab}(y)dy^a dy^b+h_{ij}(y,x)dx^i dx^j,
 \qquad S_a=\tfrac12h^{-1}\partial_a h,
 \quad H_a=\operatorname{tr}S_a=0.
 \tag{8}
\]

The last equality means that the area form of \(h\) is preserved in
the horizontal directions, not merely that every fibre has the same
total area. Put \(E=\operatorname{Ric}+\kappa g\). With base and
fibre both of curvature \(-\kappa\), the full Ricci defect is

\[
 \boxed{\begin{aligned}
 E_{ab}&=-\operatorname{tr}(S_aS_b),\\
 E_{ai}&=(\operatorname{div}_h S_a)_i,\\
 (E_{VV})^\sharp&=-b^{ab}D_aS_b.
 \end{aligned}}                                               \tag{9}
\]

Here \(D_aS_b=\partial_aS_b+[S_a,S_b]-\Gamma^c_{ab}S_c\) is the
covariant derivative using the metric-compatible vertical connection
and the base connection. The commutator contracts to zero but is
retained to specify the tensor derivative correctly. The remaining
entries are the symmetric transposes. These are Gauss--Codazzi formulas
in two horizontal directions. In particular

\[
 -\operatorname{tr}_H E=Q:=\sum_{a=1}^2\operatorname{tr}(S_a^2)\ge0,
 \quad \operatorname{tr}_V E=0,
 \quad s_g=-4\kappa-Q.                                     \tag{10}
\]

The mixed and vertical blocks must also tend to zero in a successful
construction. Their possible cancellation never removes the definite
horizontal block. A bound on the norm of the whole endomorphism bounds
the norm of each horizontal compression.

These models exist on the actual Kotschick--Morita bundles: fix one of
their area-preserving flat representations, and hence fix its total
space. Choose any smooth vertical metric, uniformize fibrewise to
curvature \(-\kappa\), and apply the fibrewise parametric Moser
construction to match the invariant area form, normalized to
\(4\pi(p-1)/\kappa\). All operations are smooth over the compact
base and the resulting metric family has the fixed marking. The
flat horizontal distribution then gives (8). The original existence
theorem does not specify explicit monodromy words; none are fabricated
here. Fixing any bundle supplied by that theorem is sufficient for
the stated nonvacuous obstruction.

## 5. Proof of the quantitative gap, including nonflat connections

For a general submersion let \(S_X\) be the fibre shape operator in a
horizontal direction \(X\), defined by
\(\mathcal L_Xh=2h(S_X\cdot,\cdot)\). Let
\(A_XY=\tfrac12[X,Y]^V\), with \(X,Y\) basic horizontal lifts.
Write \(|A|^2=\sum_{a,b}|A_{e_a}e_b|^2\). The minimal-fibre
horizontal Ricci identity is

\[
 E(X,Y)=-\operatorname{tr}(S_XS_Y)
          -2\sum_b\langle A_Xe_b,A_Ye_b\rangle,
 \quad -\operatorname{tr}_H E=Q+2|A|^2.                     \tag{11}
\]

For completeness, its coefficients follow from the sectional
submersion identities of O'Neill,
[*The fundamental equations of a submersion*](https://doi.org/10.1307/mmj/1028999604):
horizontal planes contribute
\(K_B-3|A_XY|^2\); summing mixed planes contributes
\(|A_X|^2-|S_X|^2\), plus the derivative of the mean-curvature
vector, which vanishes for minimal fibres. Thus the net coefficient
of the horizontal \(A\)-norm is \(-2\). Only (11) is needed for
the general-connection obstruction; (9) supplies every Ricci block
for the actual flat comparison objects.

The TT projection is orthogonal in the tensor \(L^2\) metric.
For \(\bar h=\kappa h\), the horizontal derivative has
\(|\partial_X\bar h|_{\bar h}^2=4|S_X|_h^2\) and
\(dA_{\bar h}=\kappa dA_h\). Moduli variation is its TT projection,
so the same bound holds for any connection. In a local trivialization,
a horizontal lift differentiates the fibre metric as
\(\partial_Xh+\mathcal L_Vh\). The Lie derivative is orthogonal to
every TT tensor, so its TT projection is unchanged. This is a
directionwise derivative and does not require an integral horizontal
chart when the connection is nonflat. Consequently

\[
 |df(X)|_T^2\le4\kappa\int_{F_y}|S_X|^2\,dA_h.
 \tag{12}
\]

Fibre integration of (12), followed by (7), yields

\[
 \int_M Q\,dV_g\ge\frac{12\pi^2|\tau|}{\kappa}.          \tag{13}
\]

Let \(\delta=\|g^{-1}E\|_{\infty,\mathrm{op}}\).
Equation (11) gives \(Q+2|A|^2\le2\delta\). Gauss--Bonnet and
the submersion volume form give

\[
 V=\frac{4\pi^2\chi}{\kappa^2},\qquad
 2\delta V\ge\frac{12\pi^2|\tau|}{\kappa}.
 \tag{14}
\]

This proves (2). All constants are independent of the degeneration
parameter, and the proof controls the norm in the actual four-metric.
Connection curvature only strengthens this particular obstruction.

## 6. What a possible extension must change

The base-curvature hypothesis has a useful exact replacement. Keep
minimal hyperbolic fibres of curvature \(-\kappa\), but let the
base metric be arbitrary with Gaussian curvature \(K_B\). Then

\[
 \operatorname{tr}_H E=2(K_B+\kappa)-Q-2|A|^2.
 \tag{15}
\]

The fibre area is still \(4\pi(p-1)/\kappa\). Integrating (15),
using Gauss--Bonnet on the base and (13), proves the tradeoff

\[
 \boxed{\quad
  (1+\delta/\kappa)\,\frac{V}{V_0}
       \ge1+\frac{3|\tau|}{2\chi},
  \qquad V_0=\frac{4\pi^2\chi}{\kappa^2}.
 \quad}                                                       \tag{16}
\]

Thus merely stretching more disjoint collars, while retaining the
product-normalized volume and minimal hyperbolic fibres, cannot work.
An extension must change at least one of these constraints: retain
a volume/base-curvature contribution of the size in (16), admit
nonminimal fibres and control their mean-curvature terms, change the
intrinsic fibre equation, or leave this submersion geometry entirely.
None of these alternatives has been solved here. In particular,
nonzero signature does not obstruct small Ricci defect on arbitrary
metrics: the exact Kodaira controls show the contrary.

For comparison, the earlier `BUNTOP:signature-volume` consequence of
the monopole scalar estimate applies without the submersion ansatz,
under its two-orientation symplectic and \(b_2^\pm>1\) hypotheses:
\((1+\delta/\kappa)^2V/V_0\ge1+3|\tau|/(2\chi)\).
At \(V=V_0\) it gives the square-root gap. Equation (16) has a single
power and hence the linear gap (2), but uses the additional minimal
hyperbolic-fibre geometry. The stronger constant is not a removal of
those geometric hypotheses.

For a fixed surface relation of signature zero which does not factor
through a free group, (7) gives no positive lower bound. This note
does not claim its metric construction or its impossibility. That is
a distinct next topology test, rather than a consequence of
noncommutativity or of this signature argument.

## 7. An inherited exact-rigidity corollary and a direct proof

The earlier `SUB:basic` theorem already treats every negative Einstein
surface submersion with basic fibre mean curvature, including minimal
fibres, without imposing intrinsic fibre curvature. The following is
its narrower corollary, not a new classification. Its direct proof
illustrates the role of the same vertical and mixed blocks.

**Corollary.** Suppose an Einstein metric \(\operatorname{Ric}_g=-\kappa g\)
on (1) makes \(\pi\) a Riemannian submersion with minimal fibres whose
intrinsic curvature is \(-\kappa\). No curvature condition is imposed
on the base. Then \(g\) is locally the product of two surfaces of
curvature \(-\kappa\), and the bundle has finite isometry monodromy.
Conversely finite-monodromy bundles admit such product-quotient metrics.

**Proof.** For minimal fibres, the scalar submersion identity is

\[
 s_g=2K_B-2\kappa-|A|^2-Q.
 \tag{17}
\]

See also Lott, equation (2.1) of
[*Remark about scalar curvature and Riemannian submersions*](https://arxiv.org/pdf/math/0504421),
with the fibre mean-curvature vector zero. Subtract the horizontal
Ricci trace, which is \(2K_B-Q-2|A|^2\) by (11). This gives the
pointwise identity

\[
 \operatorname{tr}_V\operatorname{Ric}_g=-2\kappa+|A|^2.
 \tag{18}
\]

The Einstein equation forces \(A=0\). The horizontal distribution is
therefore integrable, and its flat local trivializations put the metric
in (8). Minimality gives \(\operatorname{tr}S_X=0\), and the mixed
Einstein equation in (9) gives \(\operatorname{div}_hS_X=0\). For a
fixed base tangent vector \(X\), the symmetric tensor
\(h(S_X\cdot,\cdot)\) is thus the real part of a holomorphic quadratic
differential on the closed fibre. The horizontal Einstein equation says

\[
 \operatorname{tr}(S_X^2)=K_B+\kappa
 \quad\text{for every unit }X.
 \tag{19}
\]

Its right side is constant along the fibre. A nonzero holomorphic
quadratic differential on a closed genus-\(p\ge2\) surface has zeros,
since its zero divisor has degree \(4p-4>0\). Its norm cannot be a
nonzero constant. Hence (19) forces \(S_X=0\) for every \(X\), and
then \(K_B=-\kappa\). The fibres are totally geodesic and their metric
is parallel in the flat connection. Parallel transport therefore has
image in the finite orientation-preserving isometry group of a fixed
closed hyperbolic fibre. Passing to the finite cover killing that
holonomy gives an actual product metric. The converse is the classical
finite-group product quotient, using an invariant hyperbolic fibre
metric. This proves the theorem.

This inherited exact statement also follows directly from classical
submersion identities and the surface TT description. It excludes an exact adapted solution even
for the zero-signature infinite-monodromy examples of Round 11. It is
compatible with their approximate metrics: neither small mixed Ricci
error nor degenerating fibre geometry has been upgraded to the exact
TT/constant-norm equations used in the proof. It also does not make
the existence problem for arbitrary metrics on those smooth manifolds
an adapted-submersion problem.

## 8. Finite verification

`round20_construction_check.py` recomputes the full coordinate Ricci
matrix for a two-base-variable hyperbolic fibre family of fixed area,
checks all blocks of (9), rejects a missing mixed block and a missing
horizontal quadratic term, and checks the finite matrix normalization
behind (5) and the arithmetic of (14)--(16). The two fibre directions
in that local model are diffeomorphism variations; it is a tensor
identity test, not a model with nonzero moduli energy or signature.
Global topology, the signature formula, and the TT projection argument
are the mathematical proof above and are not certified by that script.

## 9. A fixed zero-signature target with faithful Torelli monodromy

The signature-zero remainder is not empty. The following construction
uses established subgroup theorems to specify an actual smooth bundle
whose chosen monodromy cannot factor through any free group. It does
not supply near-Einstein metrics, and it does not classify all other
decompositions of its total space.

**Target theorem.** There is a smooth area-preserving representation

\[
 \widetilde\rho:\pi_1(\Sigma_2)\longrightarrow
        \operatorname{Symp}(\Sigma_6,\omega;D)
 \tag{20}
\]

whose diffeomorphisms fix a disk \(D\) pointwise, and whose projection
\(\rho\) to \(\operatorname{Mod}(\Sigma_6)\) is injective with image
in the subgroup generated by separating twists, hence in Torelli.
Its suspension

\[
 M_\rho=(\widetilde\Sigma_2\times\Sigma_6)/\pi_1(\Sigma_2)
       \longrightarrow\Sigma_2
 \tag{21}
\]

is a closed oriented smooth flat surface bundle, with a section of
self-intersection zero and

\[
 \chi(M_\rho)=20,\qquad \tau(M_\rho)=0,\qquad
 b_1=16,\qquad b_2=50,\qquad b_2^+=b_2^-=25.
 \tag{22}
\]

The monodromy of this projection, and of every finite base-cover
pullback, cannot factor through a free group.

**Five separating curves.** Start with a disk containing five small
inner disks, arranged at the vertices of a pentagon, and remove their
interiors. Attach a once-punctured torus to each of the six boundary
components, including the outer one. The result is a closed genus-six
surface. For \(i\in\mathbb Z/5\), let \(c_i\) enclose the two inner
holes \(i,i+1\) and a narrow strip along the corresponding pentagon
edge. After the tori are attached, \(c_i\) separates a genus-two side
from a genus-four side. Curves from nonadjacent pentagon edges have
disjoint representatives, chosen simultaneously using narrow strips.

Curves from adjacent edges cannot be isotoped disjoint: their
genus-two sides contain overlapping, nonnested sets of the independent
torus homology summands. If two separating curves were disjoint, their
chosen sides would be nested, disjoint, or together exhaust the surface.
Each alternative contradicts those homology subspaces; the last also
contradicts their dimensions. Thus the disjointness graph \(\Gamma\)
of the five curves is the complement of a pentagon, which is again
\(C_5\). The genus-one summand attached to the outer boundary contains
a common fixed disk disjoint from all twist supports.

**An actual lifted group action.** Let \(A(\Gamma)\) denote the
right-angled Artin group with one generator \(v_i\) per curve and
commutation exactly for disjoint pairs. Koberda's Theorem 1.1 in
[*Right-angled Artin groups and a generalized isomorphism problem for
finitely generated subgroups of mapping class groups*](https://arxiv.org/pdf/1007.1118)
gives \(N_0\) such that, for each fixed \(N\ge N_0\),

\[
 v_i\longmapsto T_{c_i}^{N}
 \quad\text{embeds }A(\Gamma)\text{ into }
       \operatorname{Mod}(\Sigma_6).
 \tag{23}
\]

Fix such an integer \(N\) once; it is part of the topology data, not
a metric-degeneration parameter. Choose annular, area-preserving
representatives of the five twists for one fixed area form \(\omega\).
For disjoint curves their annular supports are disjoint, so the
representatives commute as diffeomorphisms, not only up to isotopy.
The defining relations of \(A(\Gamma)\) therefore give a homomorphism
to \(\operatorname{Symp}(\Sigma_6,\omega;D)\), and it is injective
because its mapping-class projection (23) is injective. Separating
twists act trivially on integral first homology.

Crisp--Wiest's explicit genus-two dissection in §4, Figure 2, of
[*Embeddings of graph braid and surface groups in right-angled Artin
groups and braid groups*](https://arxiv.org/pdf/math/0303217)
gives an embedding
\(j:\pi_1(\Sigma_2)\hookrightarrow A(C_5)\): their labelled cubical
map to the Salvetti complex is a local isometry. Identify their
pentagon with \(\Gamma\), fix this \(j\), and compose with the
actual diffeomorphism representation above. This proves (20).
In particular, the surface relation is an exact identity of
diffeomorphisms; there is no unproved Nielsen-realization step.

**Topology and the free-quotient obstruction.** The fixed disk supplies
the trivial disk subbundle \(\Sigma_2\times D\), so its central
section has trivial normal bundle. Its section also splits the
fundamental-group extension. Since the action on fibre first homology
is trivial, abelianization gives
\(H_1(M_\rho;\mathbb Z)=\mathbb Z^{12}\oplus\mathbb Z^4\).
Euler characteristic is multiplicative. The signature vanishes by
the Chern--Hirzebruch--Serre signature-multiplicativity theorem, since
the action on all fibre cohomology is trivial; see
[*On the index of a fibered manifold*](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/chs.pdf).
Poincaré duality then proves the remaining numbers in (22).

If \(\rho\) factored through a free group, its injectivity would force
an embedding of \(\pi_1(\Sigma_2)\) in that free group. Subgroups of
free groups are free, whereas a closed hyperbolic surface group is not
free. The same proof applies after a finite base cover, whose group
is still a closed hyperbolic surface group and on which \(\rho\)
remains injective. Thus the free-quotient construction of Section 2
does not apply to this marked bundle projection, even virtually.

**Precisely what remains open.** The result specifies a flat,
zero-signature, faithful-monodromy target; the signature gap (2)
vanishes on it. An exact minimal-fibre Einstein metric adapted to
this projection is excluded by the inherited rigidity in Section 7.
Existence of a pointwise near-Einstein sequence on its fixed smooth
total space is not proved here. Nor is it proved that \(M_\rho\)
cannot admit a different surface fibration or a product-block
decomposition of the general sheared Round-11 type. The faithful
monodromy argument controls the specified projection only. Establishing
that stronger diffeomorphism-type distinction is a separate topology
problem; without it this must not be called a new smooth class outside
Round 11.

The finite check also verifies the five-curve incidence graph and the
arithmetic in (22). The faithful subgroup and smooth lift are proved
above using the cited group theorems; a graph computation alone would
not verify either assertion.
