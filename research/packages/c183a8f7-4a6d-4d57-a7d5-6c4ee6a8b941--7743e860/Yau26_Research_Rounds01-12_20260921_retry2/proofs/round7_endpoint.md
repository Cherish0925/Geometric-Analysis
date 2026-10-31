# Ricci approximation, curvature concentration, and the monopole capacity of resolutions

## 1. The question and the answer obtained here

The marked log-Weyl construction supplies pointwise near-negative-Einstein
metrics on resolutions of many Einstein orbifolds. Can changing the bulk
orbifold, the filling, or its chirality move those same smooth manifolds
into the critical monopole range of the integral rigidity theorem?

There is a general obstruction to this proposed connection. A vanishing-volume
curvature concentration contributes to the topological quantity
`T=2 chi+3 tau` and to the mixed monopole curvature bound in the fixed ratio
**six**. Consequently, adding such concentration cannot move a standard
locally symmetric bulk toward the critical ratio `2/3`. This statement is
not confined to Eguchi--Hanson spaces or A1 singularities.

For negatively Kähler--Einstein bulk in its complex orientation the ratio
is at least one. For all negative locally symmetric four-dimensional bulk
geometries, in either orientation, it is at least `3/4`. These conclusions
use the actual unweighted pointwise approximation and its volume/exterior
properties; they do not assume that weighted gluing errors imply them.

A narrower geometric locus remains after the classical bounds:
non-locally-symmetric Kähler--Einstein bulk viewed in the opposite
orientation. This does not evade the separately proved special-monopole
gap. A necessary condition for approaching the classical bound is that its orbifold Chern
slope approaches `32/11`, together with a specific Weyl-norm concentration
condition. Neither a source satisfying these geometric conditions nor the
required monopole saturation is constructed here. No Yau26 branch is solved.

## 2. Assumptions and invariants

Let `(O,g0)` be a fixed closed oriented Einstein four-orbifold, with finitely
many isolated singularities, normalized by `Ric(g0)=-g0`. Write

\[
 V_0=\operatorname{Vol}(O,g_0),\qquad
 w_0=|W^+_{g_0}|_{\mathrm{HS}},\qquad
 E_0=\int_O w_0^2,
\]

where the Weyl norm is its Hilbert--Schmidt norm as an operator on
`Lambda+`, not the four-index curvature-tensor norm. Define the bulk
curvature quantities

\[
 T_0=\frac1{4\pi^2}\int_O\left(\frac23+2w_0^2\right),
 \qquad
 J_0=\frac1{72\pi^2}\int_O(4+\sqrt6\,w_0)^2.                 \tag{1}
\]

They are defined by orbifold integrals. No identification with the Euler
characteristic of the coarse singular space is being made.

Let `M` be a fixed smooth closed oriented four-manifold with metrics `g_j`
and regions `U_j` such that

\[
 \|g_j^{-1}\operatorname{Ric}(g_j)+I\|_\infty\longrightarrow0,
 \quad V_j\longrightarrow V_0,
 \quad\operatorname{Vol}_{g_j}(U_j)\longrightarrow0.          \tag{2}
\]

Assume that outside `U_j` the first and second Weyl-norm moments converge
to those of the bulk orbifold:

\[
 \int_{M\setminus U_j}|W^+_{g_j}|^p\longrightarrow\int_Ow_0^p,
 \qquad p=1,2.                                            \tag{3}
\]

The actual marked construction satisfies this: its exterior is isometric
to the fixed orbifold minus shrinking node balls, all modifications lie
in `U_j`, and its estimates prove vanishing replacement volume. Mere GH
convergence, or a small weighted Ricci error, is not a replacement for
(2)--(3). No assumption on the topology or metric model inside `U_j` is
needed below.

For `b+(M)>=2`, let `C(M)` be the finite set of real monopole classes and

\[
 \alpha^2(M)=\inf_{H\in\operatorname{Gr}_{b^+}^+}
                    \max_{a\in C(M)}(a_H^+)^2.             \tag{4}
\]

Set this invariant to zero if there are no classes. The convex-hull
invariant `beta^2` and the corresponding special-class invariants are
no larger, so every upper bound below applies to them as well. Ordinary
monopole classes suffice; no generic-perturbation or square assumption
is used in this note.

## 3. A concentration identity and its monopole consequence

**Theorem 1.** Under (2)--(3), with `T=2 chi(M)+3 tau(M)`, the limit

\[
 E=\lim_j\int_{U_j}|W^+_{g_j}|^2
\]

exists and is nonnegative. Moreover

\[
 \boxed{\quad T=T_0+\frac{E}{2\pi^2},\qquad
 \alpha^2(M)\le
 \min\left\{\frac{V_0}{2\pi^2},\ J_0+\frac{E}{12\pi^2}\right\}.
 \quad}                                                   \tag{5}
\]

The theorem is independent of the integral analytic gap developed in
round4: its only gauge-theoretic inputs are classical scalar and mixed
monopole inequalities.

**Proof.** Put `s_j=tr Ric(g_j)` and `r_j=Ric(g_j)-(s_j/4)g_j`.
Equation (2) implies

\[
 \int_Ms_j^2\to16V_0,\qquad\int_M|r_j|^2\to0.
\]

The smooth Chern--Weil formula on the fixed manifold gives

\[
 \int_M|W^+_{g_j}|^2
 =2\pi^2T-\frac1{48}\int_Ms_j^2+\frac14\int_M|r_j|^2
 \longrightarrow2\pi^2T-\frac{V_0}{3}.                    \tag{6}
\]

Subtract (3), with `p=2`. This gives
`E=2 pi^2 T-V0/3-E0>=0` and the first identity in (5).
In particular the total Weyl energy is uniformly bounded. Thus

\[
 \int_{U_j}|W^+_{g_j}|
 \le\operatorname{Vol}(U_j)^{1/2}
                    \left(\int_{U_j}|W^+_{g_j}|^2\right)^{1/2}
 \longrightarrow0.                                      \tag{7}
\]

Using `s_j -> -4` uniformly, (3), (6), and (7),

\[
 \int_M(-s_j+\sqrt6|W^+_{g_j}|)^2
 \longrightarrow72\pi^2J_0+6E.                           \tag{8}
\]

For every monopole class of this same metric the standard inequalities are

\[
 32\pi^2(a^+_{g_j})^2\le\int s_j^2,\qquad
 72\pi^2(a^+_{g_j})^2
       \le\int(s_j-\sqrt6|W^+_{g_j}|)^2.                   \tag{9}
\]

Take the maximum over classes and use that (4) is bounded above by the
value on each metric's positive Hodge plane. Equations (8)--(9) prove
the second statement in (5). QED.

The smooth identities and monopole inequalities, including the all-class
invariants, are recorded in [LeBrun, *Four-Manifolds, Curvature Bounds,
and Convex Geometry*, Theorem A, Sections 2--4 and 5](https://arxiv.org/pdf/math/0611450). The passage from the actual
concentrating sequence to (5) is the argument above.

## 4. Why concentration does not join the critical obstruction

Put

\[
 F_0=\frac1{864\pi^2}\int_O(4-8\sqrt6\,w_0)^2,
 \qquad D=J_0+\frac{E}{12\pi^2}.
\]

Direct completion of the square gives

\[
 T_0-\frac23J_0=F_0,
 \qquad
 \boxed{\quad T-\frac23D=F_0+\frac{4E}{9\pi^2}.\quad}       \tag{10}
\]

Equivalently, the two error sources have exactly the same coefficient:

\[
 T-\frac23D=\frac4{9\pi^2}
       \left[\int_O\left(w_0-\frac1{2\sqrt6}\right)^2+E\right].
                                                               \tag{10a}
\]

Hence, if `alpha^2>0`,

\[
 \frac{T}{\alpha^2}-\frac23
 \ge\frac{F_0+4E/(9\pi^2)}{J_0+E/(12\pi^2)}.              \tag{11}
\]

Equivalently, `T/D` is the weighted average of `T0/J0` and six, with
weights `J0` and `E/(12 pi^2)`. A bubble contribution therefore cannot
lower a bulk ratio below six. In particular, changing chirality is not
a way to purchase a larger monopole lower bound at a smaller topological
cost near `2/3`.

For a family of sources and resolutions, approaching `T/alpha^2=2/3`
requires all of the following:

1. `E/J0 -> 0`;
2. `F0/J0 -> 0`;
3. `alpha^2/D -> 1` (actual monopole saturation).

The second condition is equivalent in this regime to

\[
 \fint_O\left(w_0-\frac1{2\sqrt6}\right)^2\longrightarrow0.
                                                               \tag{12}
\]

Indeed `F0` is a fixed multiple of that square. Cauchy--Schwarz and
`J0 <= C(V0+integral w0^2)` show that `F0/J0 -> 0` forces
`F0/V0 -> 0`; otherwise writing `w0=w_*+(w0-w_*)` bounds `J0` by
`C V0+C F0` and contradicts `F0/J0 -> 0`. Then
`J0/V0 -> 9/(32 pi^2)`. Condition (12) controls only the Weyl modulus,
not its eigenvalues or eigenvectors.

For an A1 resolution with `m` positive EH bolts, the orientation-sensitive
energy is `E=12 pi^2 m`, recovering

\[
 T=T_0+6m,\quad\alpha^2\le\min\{V_0/(2\pi^2),J_0+m\},
 \quad T-\tfrac23(J_0+m)=F_0+\tfrac{16}{3}m.               \tag{13}
\]

Here a negative bolt adds `3/2` to orbifold Euler characteristic and
`-1` to signature, so it adds zero to `T`; a positive bolt adds six.
These are the actual local filling increments, not a smooth
connected-sum classification inferred from an intersection form.

## 5. Entire classes of bulk geometries are separated from the target

**Corollary 2 (Kähler orientation).** If `g0` is negatively
Kähler--Einstein in the chosen orientation and `alpha^2>0`, then

\[
 w_0^2=\frac{s_0^2}{24}=\frac23,\qquad
 T_0=J_0=\frac{V_0}{2\pi^2},\qquad
 \boxed{\quad\frac{T}{\alpha^2}\ge1+\frac{E}{V_0}.\quad}   \tag{14}
\]

The last statement uses the scalar bound in (5), stronger here than the
mixed bound. It does not assume the smooth resolution is Kähler or
symplectic. Any finite quotient for which the local Kähler orientation
descends has the same curvature calculation, even when the Kähler form
itself does not descend.

**Corollary 3 (negative locally symmetric bulk).** In either orientation,
when `alpha^2>0`, every sequence satisfying (2)--(3) over a negative locally symmetric
four-orbifold obeys

\[
                     T/\alpha^2\ge3/4.                   \tag{15}
\]

The three local models and their stronger bulk bounds are:

| Local geometry | Chosen orientation | `T0/J0` | Uniform lower bound after filling |
| --- | --- | --- | --- |
| real hyperbolic four-space | either | `3/4` | `3/4` |
| complex hyperbolic two-space | complex | `1` | `1+E/V0` |
| complex hyperbolic two-space | reversed | `3/4` | `3/4` |
| product of two hyperbolic planes | either | `1` | `1+E/V0` |

For real hyperbolic bulk both Weyl halves vanish. For complex hyperbolic
bulk the complex-oriented half has the Kähler spectrum and the other
half is zero. The product is locally Kähler in both orientations, by
reversing the complex structure on one factor. Formula (5) then proves
the table. These cover the simply connected negative-Einstein symmetric
spaces of real dimension four; Euclidean factors are incompatible with
the normalization and the product's two factors must have the same
Einstein constant.

Thus neither more nodes, different chirality, nor a different Ricci-flat
ALE filling of a standard locally symmetric source can join the existing
`2/3` monopole obstruction, whenever the proposed filling really produces
(2)--(3). This is a restriction on that connection, not a theorem asserting
that every such resolution admits an Einstein metric.

## 6. Opposite-oriented Kähler bulk: a specific remaining target

Let the bulk now be Kähler--Einstein but not assumed locally symmetric.
Assume `alpha^2>0` when forming the ratios below.
Write its orbifold Chern slope as

\[
 \rho=\frac{c_{1,\mathrm{orb}}^2}{c_{2,\mathrm{orb}}},
 \qquad c_{1,\mathrm{orb}}^2=\frac{V_0}{2\pi^2}.
\]

The orbifold Chern--Weil identities, in the complex orientation, give

\[
 \frac1{V_0}\int|W^-|^2=\frac4\rho-\frac43,\qquad
 0<\rho\le3.                                             \tag{16}
\]

For the opposite orientation put

\[
 x=\sqrt{24/\rho-8}.
\]

Cauchy--Schwarz bounds its mixed curvature quantity by
`J0 <= V0(4+x)^2/(72 pi^2)`, while
`T0=V0(x^2+2)/(12 pi^2)`. Since every concentration term has ratio
six, (5) gives the explicit bound

\[
 \boxed{\quad
 \frac{T}{\alpha^2}\ge R(\rho)
 :=\frac{6(x^2+2)}{(x+4)^2}
 =\frac23+\frac{4(2x-1)^2}{3(x+4)^2}.
 \quad}                                                   \tag{17}
\]

The only slope at which this lower bound can approach `2/3` is

\[
                         \rho_* =32/11.                  \tag{18}
\]

This is a necessary selection rule for the proposed opposite-oriented
monopole mechanism, not a claimed new obstruction to all Einstein
metrics. A Chern slope near (18) supplies only an averaged curvature
energy. The route also requires vanishing variance of `|W^-|`,
negligible self-dual filling energy, and enough actual monopole classes
in that orientation to saturate the bound. None follows from geography.

Known symmetric sources miss this target: complex hyperbolic slope three
gives `R=3/4`; hyperbolic products have slope two and give `R=1`.
No non-locally-symmetric source realizing all these requirements has been
established in this work. Merely producing algebraic Chern numbers near
`32/11` is not such an example.

There is a further logical restriction from the previously derived integral
gap. If the actual saturating classes are special monopole classes (or
satisfy its uniform square hypothesis), that gap already forbids a
near-Einstein sequence with `T/alpha^2 -> 2/3`. Thus (18) is a selection
rule for possible geometric near-saturation, not a proposal to obtain a
counterexample by violating the same proved gap. Under its hypotheses,
one of the demanded saturation properties must fail. Ordinary classes
without that square control are a different case. A successful Yau26
counterexample needs an Einstein obstruction compatible with the small
Ricci input, not an obstruction that has already excluded the input itself.

In particular, if unrestricted ordinary classes were to approach this
critical ratio across such constructed sources, the classes supplying
the required positive projection could not have a uniform lower bound
`a^2 >= -C alpha^2` along sufficiently small-defect metrics. Their negative
square would have to escape every such fixed bound. This is not an
existence assertion about those classes.

## 7. Why the bulk Einstein identity does not finish the argument

For harmonic Weyl curvature on an Einstein four-manifold, with the
Laplacian convention `Delta=div grad`,

\[
 \Delta|W^+|^2
 =2|\nabla W^+|^2+s|W^+|^2-36\det W^+.                   \tag{19}
\]

See [Derdziński, *Self-dual Kähler manifolds and Einstein manifolds of
dimension four*](https://www.numdam.org/item/CM_1983__49_3_405_0/),
the Weyl Weitzenböck identity and the local two-eigenvalue structure.
The algebraic bound is `3 sqrt(6)|det W| <= |W|^3`.
At the constant critical modulus `|W|=1/(2 sqrt(6))`, equation (19) gives

\[
 \frac1{16}\le |\nabla W|^2\le\frac5{48}.                 \tag{20}
\]

These are compatible positive values, not a contradiction. Constant norm
does not imply a parallel tensor. If the additional, specific spectrum
`(-1/6,1/12,1/12)` were forced throughout an open set, the harmonic
two-eigenvalue structure and constant norm would imply parallelness,
which contradicts (20). The missing eigenvalue saturation cannot be
inserted into (12). Nor does an averaged limit (12) itself provide
pointwise compactness or derivative estimates.

## 8. Consequence for the research direction

This calculation replaces an indiscriminate search over standard
orbifolds and fillings with a precise constraint. Standard symmetric
bulk and complex-oriented Kähler bulk cannot meet the critical monopole
obstruction through a shrinking-volume pointwise Ricci approximation.
The opposite-oriented non-symmetric Kähler possibility has a concrete
curvature and Chern-slope target, but remains unconstructed and lacks
the needed monopole information.

There are two different legitimate ways beyond this calculation:

* develop an all-Einstein obstruction not controlled by these monopole
  curvature bounds, acting on an actual already-constructed smooth type;
* find a bulk/filling mechanism outside the separated classes and prove
  its full unweighted Ricci estimate and global obstruction on the same
  smooth manifold.

The hyperelliptic product quotient is not a new counterexample candidate:
the earlier manuscript already smooths its double-cover branch divisor
and obtains a negative Kähler--Einstein metric on the same smooth
resolution (`20260912.tex`, the negative-construction filters). Its
reappearance here is a useful check against rediscovering an already
closed positive existence argument.

The established result in this note is a general quantitative
compatibility theorem and its model-class consequences. It is not a
new log-Weyl construction, not a general Einstein nonexistence theorem,
and not a first-priority claim. The symbolic checks in
`round7_endpoint_check.py` verify the coefficient identities, extrema,
and model specializations; the geometric proof is Sections 2--7 above.
