# Fixed near-Einstein surface bundles with controlled rank-one representation loss

21 September 2026.

## 1. Statement and relation to the existing construction

Fix fibre and base genera `p,q>=2`. Choose `r` curves from a standard
nonseparating cut system on the fibre, where
`1<=r<=min(p,q)`, and let `D_i` be their single positive Dehn twists.
On the base choose `r` curves from a nonseparating cut system. The
primitive dual homomorphisms `u_i:Pi_q -> Z` define the fixed bundle

\[
 E_{p,q,r}\longrightarrow\Sigma_q,\qquad
 \rho(\gamma)=\prod_{i=1}^r D_i^{u_i(\gamma)}.              \tag{1}
\]

All twists, markings, cut curves and the smooth bundle are fixed.
Only the base hyperbolic metrics and interpolating fibre metrics
vary below. Set `V0=16 pi²(p-1)(q-1)` and

\[
 \delta_-(G)=\|G^{-1}\operatorname{Ric}_G+I\|_{L^\infty,\mathrm{op}}.
\]

**Theorem.** This same closed smooth four-manifold carries metrics
`G_L`, for `L -> infinity`, satisfying

\[
 \delta_-(G_L)\le C/L,
 \quad\operatorname{Vol}(G_L)=V_0,
 \quad\|\nabla^m\operatorname{Rm}_{G_L}\|_\infty\le C_m,
 \quad\|\nabla^m(\operatorname{Ric}_{G_L}+G_L)\|_\infty\le C_m/L.
                                                               \tag{2}
\]

The constants may depend on the fixed topological and geometric
data, but not on `L`. For every representation into `PSL(2,R)`,
all `r` twisting curves are killed. Moreover,

\[
 \boxed{\quad
 \sup_{\varrho:\pi_1(E_{p,q,r})\to\operatorname{PSL}(2,\mathbb R)^2}
 |\operatorname{Vol}(\varrho)|
 =16\pi^2\max(p-r-1,0)(q-1).
 \quad}                                                       \tag{3}
\]

Thus `r=p-1` already makes every product-hyperbolic representation
volume zero; `r=p` does so as well. For every fibre genus this gives
an actual fixed smooth near-Einstein input with zero representation
volume, choosing `q>=max(2,p-1)` and `r=p-1`.

The metric mechanism is **inherited**, not a newly discovered
generalization: the Skill's `20260912.tex`, immediately after
`BUN:slow-geometric`, and `20260916_global.tex`, `sec:bundle-input`,
already allow monodromy through a geometric free-group quotient,
including noncommuting mapping classes. The new synthesis here is
the exact representation calculation for concrete members of that
construction class, together with an explicit full-Ricci proof
on those same members. It does not establish Einstein nonexistence.

## 2. Fixed gluing data and simultaneous long base collars

Use standard base generators `A_j,B_j`, with relation
`product [A_j,B_j]=1`. The chosen cut curves represent `A_1,...,A_r`;
their dual homomorphisms have `u_i(B_j)=delta_ij` and
`u_i(A_j)=0`. In particular, each separate twist `D_i`, not just a
power or a product of twists, is realized by a based loop `B_i`.

Extend the base cut system to a pants decomposition. Prescribe length
`ell` to its first `r` curves and keep all remaining length/twist
parameters fixed. Hyperbolic pairs of pants and their boundary
gluings yield a marked hyperbolic metric on the same base. The collar
lemma provides disjoint embedded collars of half-width

\[
 w(\ell)=\operatorname{arsinh}(1/\sinh(\ell/2))\longrightarrow\infty.
\]

Use their inner halves, `L=w(ell)/2`, with coordinates
`-L<=t<=L`, `theta in R/Z`, and metric

\[
 dt^2+b(t)^2d\theta^2,\qquad b(t)=\ell\cosh t.              \tag{4}
\]

The classical collar construction and its disjointness are the only
surface-geometry input; see [Keen, *Collars on Riemann Surfaces*](https://www.degruyterbrill.com/document/doi/10.1515/9781400881642-021/html)
and [Buser, *Geometry and Spectra of Compact Riemann Surfaces*,
the collar and pants-coordinate chapters](https://link.springer.com/book/10.1007/978-0-8176-4992-0).

Cut the base along these curves and put the trivial fibre product
over its complement. Restore the `i`th handle with a cylinder
whose left boundary is glued by the identity and whose right
boundary is glued by `D_i`. This realizes exactly (1), independently
of `ell`. The common fixed point outside the finite union of twist
supports gives a section and the split group extension

\[
 \pi_1(E_{p,q,r})=\Pi_p\rtimes_\rho\Pi_q.                  \tag{5}
\]

There is no requirement that a cylinder's two boundary fibre
metrics coincide in its trivialization. The right boundary metric
is `D_i^*h0`, precisely the pullback needed for gluing to the outside
metric `h0` by `D_i`.

## 3. Fixed hyperbolic fibre paths with exact endpoint matching

Fix one hyperbolic metric `h0` on the fibre. Around the geodesic
representative of the `i`th cut curve choose a fixed embedded collar

\[
 h_0=du^2+a(u)^2ds^2,\qquad a(u)=a_{0,i}\cosh u,
 \qquad s\in\mathbb R/\mathbb Z.
\]

Take a smooth `zeta_i(u)` equal to zero and one near the two
boundary components. The twist is
`D_i(u,s)=(u,s+zeta_i(u))`. It is the identity near both boundaries
because `s` has period one. Define, for `0<=z<=1`,

\[
 h_{i,z}=du^2+a^2(ds+z\zeta_i'\,du)^2                     \tag{6}
\]

inside this collar and use `h0` outside. Since `zeta_i'=0` near both
ends, this defines a smooth global metric. Locally the coordinate
change `s -> s+z zeta_i(u)` identifies (6) with `h0`, so

\[
 K_{h_{i,z}}=-1,\qquad dA_{h_{i,z}}=dA_{h_0},\qquad
 h_{i,0}=h_0,\quad h_{i,1}=D_i^*h_0.                      \tag{7}
\]

The local coordinate changes for nonintegral `z` are not asserted
to extend to a global isotopy of the fibre. This is why (6) can
represent a nontrivial path in marked hyperbolic metrics.

Choose `eta:[-1,1]->[0,1]` smooth, zero near `-1` and one near `1`.
On the `i`th base cylinder set

\[
 G_L=dt^2+b^2d\theta^2+h_{i,\eta(t/L)}.                    \tag{8}
\]

Outside all cylinders use the hyperbolic product. At each seam,
`eta` is constant in an open neighborhood. The metric and every
derivative therefore match the product metric after the actual
identity or `D_i` transition. Base cylinders are disjoint, so no
point has two independent interpolation parameters. The resulting
metric is positive definite and smooth on the fixed bundle.

## 4. Full pointwise Ricci estimate, including the shrinking circle

On one active fibre/base collar pair use the orthonormal coframe

\[
 \omega^0=dt,\quad\omega^1=b\,d\theta,\quad\omega^2=du,
 \quad\omega^3=a(ds+z\zeta'\,du),\qquad z=\eta(t/L).
\]

Write `j=a'/a=tanh u`, `k=b'/b=tanh t`, `Q=a zeta'`, and `v=Q z'`.
The structure equations are

\[
 d\omega^1=k\omega^0\wedge\omega^1,\qquad
 d\omega^3=j\omega^2\wedge\omega^3+v\omega^0\wedge\omega^2.
                                                               \tag{9}
\]

Koszul's formula and `j_u=1-j²`, `k_t=1-k²` give the complete
Ricci-endomorphism defect matrix

\[
 (\operatorname{Ric}_{G_L}+G_L)_{\mathrm{ON}}=
 \begin{pmatrix}
 -v^2/2&0&0&(v_u+2jv)/2\\
 0&0&0&0\\
 0&0&-v^2/2&-(v_t+kv)/2\\
 (v_u+2jv)/2&0&-(v_t+kv)/2&v^2/2
 \end{pmatrix}.                                             \tag{10}
\]

The checker independently recomputes all sixteen entries directly
from (9), retaining the moving-frame quadratic terms. The
off-diagonal matrix has eigenvalues `0,0,+sqrt(x²+y²),-sqrt(x²+y²)`
for the two displayed off-diagonal entries `x,y`. Define

\[
 A_{0,i}=\|Q_i\|_\infty,\quad
 A_{1,i}=\|Q_i'+2j_iQ_i\|_\infty,\quad
 M_m=\|\eta^{(m)}\|_\infty.
\]

Equation (10) gives the continuous pointwise bound

\[
 \delta_-(G_L)\le\max_i\left\{
 \frac{A_{0,i}^2M_1^2}{2L^2}
 +\frac1{2L}
 \sqrt{A_{1,i}^2M_1^2+A_{0,i}^2(M_1+M_2/L)^2}\right\}.
                                                               \tag{11}
\]

This is a maximum, not a sum over `r`: active base cylinders do
not overlap. Their number is fixed. The estimate is in the actual
metric's unweighted operator norm over the entire closed manifold.
It is not a finite sampling estimate or an integrated small-volume
argument.

There is no hidden `ell^{-1}`. All coefficient functions in (9)
are independent of `theta`; the unit angular derivative annihilates
them. Its connection coefficients contain only `b'/b=k`, whose
derivatives are bounded independently of `ell`. The other angular
direction similarly annihilates all coefficients. Repeated
orthonormal covariant differentiation thus involves only bounded
coefficients `j,k` and their derivatives, fixed fibre-profile
derivatives, and derivatives of `v=Q eta'(t/L)/L`. Every defect
term and all its fixed-order derivatives retain a factor `L^{-1}`.
The curvature itself and its fixed-order derivatives are uniformly
bounded. A finite atlas covers the unchanged fibre; outside active
regions the metric is locally the symmetric hyperbolic product.
This proves the derivative claims in (2) without any injectivity
radius lower bound.

The shear determinant is one, so the total volume is exactly the
product of the two hyperbolic surface areas, namely `V0`. The scalar
curvature is `-4-v²/2` in active regions. Some mixed sectional
curvatures equal `v²/4>0`, so the metrics are not negatively
sectionally curved. None of these estimates asserts the existence
of an Einstein correction.

## 5. Killing independent twisting curves

Use fibre generators `a_i,b_i`, with
`product_{i=1}^p[a_i,b_i]=1`, so

\[
 D_i(b_i)=b_i a_i,\qquad D_i(a_i)=a_i,
 \qquad D_i(a_j)=a_j,\ D_i(b_j)=b_j\quad(j\ne i).           \tag{12}
\]

The chosen base loop `B_i` conjugates the fibre group by exactly
`D_i`. In any target with abelian centralizer of every nonidentity
element, the curve-killing proof from `round8_construction.md`
applies to this relation separately. Explicitly, write `T` for the
image of `B_i`. If `T=1`, the twist relation kills `a_i`. Otherwise
all other handles lie in the abelian centralizer of `T`, so their
commutators vanish. The surface relation implies that the images
of `a_i,b_i` commute. If `a_i` had nonidentity image, its abelian
centralizer would contain `T,b_i`, again contradicting the twist
relation. Thus every `a_i`, `1<=i<=r`, is killed.

The quotient is

\[
 \pi_1(E_{p,q,r})/\langle\!\langle a_1,\ldots,a_r\rangle\!\rangle
 \cong(\Pi_{p-r}*F_r)\times\Pi_q.                         \tag{13}
\]

Here `F_r` consists of the surviving `b_1,...,b_r`. When `p-r=0`,
`Pi_0` denotes the trivial group and its classifying space is a
point, **not a two-sphere**. The quotient (13) follows from the
actual split extension (5), not from abelianizing its presentation.

For `PSL(2,R)` the centralizer hypothesis holds for all nonidentity
elements, including elliptic order two. After (13), commuting
nontrivial images of both factors lie in one abelian centralizer
and have zero real Euler class. Otherwise a representation factors
through one of the factors. The fibre-side factor has only the
second cohomology of `Sigma_{p-r}` when `p-r>=1`, and none when
`p-r=0`; free factors add no second cohomology. Milnor--Wood gives
fibre-side Euler coefficient at most `2 max(p-r-1,0)` in absolute
value, and the base coefficient at most `2q-2`.

When `p-r>=1`, the quotient fibre map has degree one on the residual
surface class. Thus its degree-two generator `alpha` and the base
generator `beta` obey `alpha²=beta²=0` and
`<alpha beta,[E]>=1`. Therefore the largest Euler product is
`4 max(p-r-1,0)(q-1)`. For residual genus at least two, equality is
obtained by killing the free factor and taking extremal Fuchsian
representations of both surface factors. For residual genus zero
or one all Euler products vanish. Since product-hyperbolic volume
equals `4 pi²<e_1 e_2,[E]>`, this proves (3). The Euler bound and
extremal representations are classical [Goldman](https://www.math.umd.edu/~wmg/TopologicalComponents.pdf).

In particular, the disappearance of product representation volume
does not imply collapse of the actual metric's total volume: (2)
keeps it equal to the positive constant `V0`. A representation
volume is a different invariant from metric volume or simplicial
volume.

## 6. A stronger noncommuting example: every rank-one representation loses the entire fibre

Suppose `q>=2p`. Use `2p` disjoint base collars and prescribe their
monodromies to be the single twists about **all** standard fibre
curves `a_1,b_1,...,a_p,b_p`. Fibre supports now intersect. This
causes no conflict: only one base collar is active at a given point,
and each uses its own fixed hyperbolic fibre path (6). There are
only finitely many such paths. The monodromy factors through the
free quotient of `Pi_q` sending `A_j` to `1` and the first `2p`
generators `B_j` to those twists; the base relator holds without
any commutativity assumption. Actual diffeomorphism representatives
can all fix one base point outside their finite collection of
annular supports.

Consequently exactly the same global gluing and bounds (2) apply
to this new fixed bundle, denoted `E_full`. For a twist about `b_i`,
one may use the based automorphism

\[
 a_i\longmapsto a_i b_i^{-1},\qquad b_i\longmapsto b_i,
 \qquad [a_i b_i^{-1},b_i]=[a_i,b_i].                        \tag{14}
\]

The same centralizer argument now kills `b_i`. The separate twists
about `a_i` kill `a_i`. Thus

\[
 \boxed{\quad
 \text{every }\pi_1(E_{\rm full})\to\operatorname{PSL}(2,\mathbb R)
 \text{ factors through }\pi_1(\Sigma_q).
 \quad}                                                       \tag{15}
\]

Every real Euler class is therefore a multiple of the same base
class `beta`, and every `PSL(2,R)^2` representation volume is zero.
This is stronger than merely killing a cut system: the whole fibre
group is invisible to every such representation. The metric still
has globally vanishing Ricci defect and exactly positive volume
`V0`. No arbitrary Einstein metric is inferred from, or excluded
by, (15).

## 7. Topology, distinctions from the single-twist object, and scope

For all these geometric-free-quotient bundles,

\[
 \chi=4(p-1)(q-1),\qquad\tau=0.                             \tag{16}
\]

The first identity is multiplicativity of Euler characteristic.
For the second, the base quotient extends over a genus-`q`
three-dimensional handlebody. The actual diffeomorphism monodromies
therefore define a five-dimensional surface bundle bounding the
given oriented total space, whose signature is zero.

The section splits first homology. For the disjoint rank-`r` family,
the independent transvections kill exactly `a_1,...,a_r` in the
fibre coinvariants, giving

\[
 b_1(E_{p,q,r})=2p+2q-r.
\]

For `E_full` the twists about both members of every symplectic pair
kill all fibre coinvariants, and `b_1(E_full)=2q`. In particular,
the odd-Betti-number argument for the original single-twist example
does not automatically transfer to these new examples. Neither do
its finite-cover conclusions merely by analogy.

All twists used here preserve the fixed hyperbolic area form. That
area form descends from the flat product to a closed vertical
two-form. Adding or subtracting a base area form gives symplectic
forms for both orientations. The hypotheses for the standard
nonnegative-Einstein exclusion are satisfied explicitly:
`tau=0` and

\[
 b^+=\chi/2+b_1-1>1,\qquad
 c_1(K)^2=2\chi+3\tau=2\chi>0.
\]

Taubes' nonvanishing theorem gives a nonzero Seiberg--Witten
invariant for the symplectic canonical class (equivalently its
negative, with the corresponding convention). This precludes a
positive-scalar-curvature metric, hence any Einstein metric with
positive constant. For every metric `g`, the monopole scalar bound
also gives

\[
 \int_E s_g^2\,d\mu_g
 \ge32\pi^2(c_1(K)^+_g)^2
 \ge32\pi^2c_1(K)^2
 =32\pi^2(2\chi)>0,
\]

which excludes Ricci-flat metrics. The square bound alone would
not exclude positive scalar curvature; that case uses the separate
Seiberg--Witten obstruction. See [LeBrun, *Ricci Curvature, Minimal
Volumes, and Seiberg--Witten Theory*, the scalar estimate in the
Introduction and the Seiberg--Witten discussion in Section 2](https://arxiv.org/pdf/math/0003068).
Consequently any Einstein metric on these actual bundles would
have negative Einstein constant. No new exclusion of that
remaining case is proved here. The metrics in (2) and the
representation statements concern the **same fixed smooth objects**.

Single twists and the independent geometric base generators are
essential in the representation proofs. A twist power only forces
the corresponding curve image to have bounded finite order in
`PSL(2,R)`; passing to arbitrary finite covers requires a fresh
presentation. The target is the orientation- and factor-preserving
`PSL(2,R)^2`, not every isometry of the product and not `PSL(2,C)`.

The contribution is a concrete construction--invariant combination:
existing pointwise near-Einstein flexibility realizes whole fixed
topological families for which a proposed linear-representation
route loses a quantitatively specified amount of fibre geometry,
or loses all of it. It is not a new slow-interpolation mechanism,
not a Yau26 branch counterexample, and not a proof that other global
methods cannot work. No literature-priority claim is made.
