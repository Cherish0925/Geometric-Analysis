# Product limits, Sol cusp groups, and a cohomological exclusion

22 September 2026.

## 1. The question and the new conclusion

Let \(M\) be a closed oriented shear manifold assembled from finitely
many blocks \(B_v\times F_v\), where \(B_v\) is a compact connected
oriented surface with nonempty boundary and negative Euler
characteristic, and \(F_v\) is a closed oriented hyperbolic surface.
The boundary identifications are those of
[Round 11](round11_graph_topology.md):
\[
 (\phi,x)\longmapsto(-\phi+u_e(x),f_e(x)).                 \tag{1}
\]
Write \(G=\pi_1(M)\). The metric construction is not assumed in the
group statements below. The graph-of-spaces proof in Round 11 shows
that \(M\) is aspherical; in particular \(G\) is torsion-free.

For the members carrying the actual monopoles used in
[Round 15](round15_rigidity.md), a sequence
\[
 \operatorname{Ric}_{g_j}=-3g_j,\qquad
 \operatorname{Vol}(M,g_j)\longrightarrow
 V_*:=4\pi^2\chi(M)/9                                    \tag{2}
\]
has bounded curvature of every fixed derivative order. Its smooth
noncollapsed pointed limits are complete finite-volume product
quotients, with universal cover
\(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\), and with globally
oriented parallel factor planes. For the non-Kähler smooth types these
limits are noncompact.

**Main conclusion.** No such pointed limit can be a noncompact
irreducible product quotient. For the specified non-Kähler smooth
types, every limit supplied by Round 15 must instead have a reducible
lattice. Consequently it has a finite cover
which is a product of two finite-area hyperbolic surfaces, at least one
of them noncompact.

This conclusion does not identify the limit with an original product
block. Its proof does not assume that the fundamental group of an
embedded limit core injects into \(G\). In fact the group argument
forces the opposite for an irreducible candidate: every map from that
core to \(M\) is nullhomotopic. A compactly supported intersection
pairing then rules out the core embedding itself.

## 2. The tree action and its two-edge stabilizers

The Bass--Serre tree \(T\) has vertex stabilizers
\[
 V_v=A_v\times\Gamma_v,\qquad
 A_v=\pi_1(B_v),\quad \Gamma_v=\pi_1(F_v),                 \tag{3}
\]
where \(A_v\) is nonabelian free. An incident edge stabilizer, viewed
inside \(V_v\), is
\(a\langle c\rangle a^{-1}\times\Gamma_v\), where \(c\) is a
boundary element of \(A_v\). The shear changes the identification
between edge groups, not this full image: its integral circle shift
can be absorbed by the free circle coordinate in the edge group.

Boundary cyclic subgroups of \(A_v\) are maximal cyclic and
malnormal, and distinct boundary components give nonconjugate such
subgroups. These assertions can be seen directly in the universal
cover of a negatively curved surface with geodesic boundary: a
nontrivial common element would have the same axis, forcing the same
boundary lift. Therefore, for two distinct edges incident at a vertex,
\[
 G_{e_1}\cap G_{e_2}=\Gamma_v
 \quad\hbox{inside the corresponding conjugate of }V_v.   \tag{4}
\]
In particular this intersection contains no \(\mathbb Z^2\). The
tree action is without inversions. No acylindricity assertion is
needed; stabilizers of longer segments may still be nontrivial.

## 3. A Sol group cannot survive in the shear group

For \(A\in\mathrm{SL}(2,\mathbb Z)\) with
\(|\operatorname{tr}A|>2\), set
\[
 L_A=\mathbb Z^2\rtimes_A\mathbb Z
   =\langle K,t\mid tvt^{-1}=Av\ (v\in K)\rangle.         \tag{5}
\]

**Proposition 1.** Every homomorphism \(q:L_A\to G\) kills
\(K=\mathbb Z^2\). In particular \(G\) contains no Sol torus-bundle
group.

**Proof.** Since \(G\) is torsion-free, \(q(K)\) is free abelian of
rank zero, one or two. Rank one is impossible: the kernel of
\(K\to q(K)\) would be an \(A\)-invariant rational line, and the
induced automorphism on \(q(K)\cong\mathbb Z\) would have eigenvalue
\(+1\) or \(-1\). Neither is an eigenvalue of a hyperbolic matrix
\(A\in\mathrm{SL}(2,\mathbb Z)\). If its image has rank two, then
\(q|_K\) is injective. In this case \(q\) itself is injective: a
kernel element \(vt^m\) would centralize the image of \(K\), forcing
\(A^m=I\), hence \(m=0\) and \(v=0\).

It remains to exclude an embedded \(L_A\). Consider its action on
\(T\). If \(K\) contains a hyperbolic tree isometry, its centralizer
preserves its axis and acts there by translations. Thus there is a
nonzero translation homomorphism \(\ell:K\to\mathbb Z\). Normality
of \(K\) makes \(t\) preserve that axis, so
\(\ell\circ A=\ell\) or \(-\ell\), again impossible.

Hence every element of \(K\) is elliptic. The two commuting
generators have a common fixed point, so the subtree \(T^K\) is
nonempty and is invariant under \(t\). As a simplicial tree
isometry, \(t\) either fixes a vertex of \(T^K\), or translates along
an axis in \(T^K\). In the second case \(K\) fixes that axis
pointwise and lies in the intersection of two incident edge
stabilizers, contradicting (4).

In the first case the whole \(L_A\) fixes a vertex and lies in
\(A_v\times\Gamma_v\). Each projection of \(K\) to either factor
is cyclic or trivial. The corresponding projection of \(t\)
normalizes that cyclic group. The normalizer of a nontrivial cyclic
subgroup in a torsion-free free or closed hyperbolic surface group is
cyclic; thus conjugation is trivial. Each projection consequently
kills \((A-I)K\), a finite-index subgroup of \(K\). Torsion-freeness
then makes both projections trivial, a contradiction. This proves
the proposition. \(\square\)

The argument for the invariant fixed subtree is important. It does
not use the false general statement that every finitely generated
solvable tree action fixes a vertex or a line. Here the particular
normal abelian subgroup is finitely generated and has a nonempty
fixed subtree; an ascending Baumslag--Solitar argument cannot replace
this step.

**Corollary 2.** If a Sol cusp cross-section, or a finite cover of one,
is mapped into \(M\), both directions of its torus fibre are killed
in \(\pi_1(M)\). This applies to maps obtained by restricting smooth
pointed-convergence embeddings. It requires no incompressibility
assumption on those embeddings.

## 4. Irreducible product lattices have no nontrivial maps into G

We use two precise classical inputs.

1. A nonuniform irreducible lattice in
   \(\mathrm{PSL}(2,\mathbb R)^2\) is, up to conjugation and
   commensurability, a Hilbert modular group over a real quadratic
   field. The \(\mathrm{SL}(2,\mathbb R)^n\) version is stated in
   [Hee Oh, *On a problem concerning arithmeticity of discrete groups
   acting on \(H^n\)*, Theorem 1.1](https://bpb-us-w2.wpmucdn.com/campuspress.yale.edu/dist/5/5177/files/2025/11/little.pdf).
   Lifting to the finite central cover passes between the two versions.
2. An infinite normal subgroup of an irreducible lattice in the
   center-free real-rank-two group
   \(\mathrm{PSL}(2,\mathbb R)^2\) has finite index. This is the
   Margulis normal subgroup theorem; see Margulis, *Discrete
   Subgroups of Semisimple Lie Groups*, Chapter IV, Theorem 4.9.
   Its precise higher-rank form, including the absence of a property
   (T) hypothesis, is recalled in
   [Bader--Gelander--Levit, Theorem 1.1 and the following paragraph](https://arxiv.org/pdf/2411.07033).

A Hilbert modular cusp has, after a finite cover, fundamental group
\(L_A\) with \(|\operatorname{tr}A|>2\). In the number-field
description it is a rank-two additive lattice acted on by a nontrivial
totally positive unit of norm one. Its real eigenvalues are
\(\lambda,\lambda^{-1}\), \(\lambda>1\). The cusp group and this
description are given in
[McReynolds, Sections 2.1, 3.3 and 5](https://arxiv.org/pdf/0706.3580).

**Proposition 3.** Let \(\Lambda\) be a torsion-free nonuniform
irreducible lattice in \(\mathrm{PSL}(2,\mathbb R)^2\). Every
homomorphism \(\Lambda\to G\) is trivial.

**Proof.** Restrict a homomorphism to a finite-index torus-bundle
subgroup of one cusp. Proposition 1 kills its infinite normal
\(\mathbb Z^2\). The kernel in \(\Lambda\) is therefore infinite,
so the normal subgroup theorem makes its index finite. Its image in
the torsion-free \(G\) is a finite group and hence trivial.
\(\square\)

If \(N\) is the corresponding smooth finite-volume quotient, a
sufficiently large compact cusp truncation \(C\subset N\) is a
deformation retract. Thus every continuous \(C\to M\) is
nullhomotopic: Proposition 3 kills its fundamental-group map, which
lifts the map to the contractible universal cover of \(M\). Every
cohomology class of positive degree on \(M\), including the first
Chern class of any determinant line, pulls back to zero on \(C\).

## 5. A compactly supported test for the limiting Kähler form

The following calculation supplies the information that an abstract
group nonembedding argument alone would miss.

On \(\mathbb H^2_{-3}\times\mathbb H^2_{-3}\) write
\[
 g=\frac{dx_1^2+dy_1^2}{3y_1^2}
   +\frac{dx_2^2+dy_2^2}{3y_2^2},\qquad
 \omega=\frac{dx_1\wedge dy_1}{3y_1^2}
       +\frac{dx_2\wedge dy_2}{3y_2^2}.                 \tag{6}
\]
Changing the orientation of a factor changes the appropriate sign;
choose them so that \(\omega\) is the Kähler form of the limiting
nonzero self-dual parallel form. Then
\(\omega^2=2\,d\mu\).

On each Hilbert modular cusp,
\[
 \eta=\frac{dx_1}{3y_1}+\frac{dx_2}{3y_2},\qquad
 d\eta=\omega,\qquad |\eta|^2=\frac23.                \tag{7}
\]
The form is invariant under translations and positive diagonal
dilations in the upper triangular cusp group: both \(dx_i\) and
\(y_i\) have the same scale factor. It therefore descends to the
cusp. If a finite cusp cover was used, average the primitive over
the finite deck group; its derivative remains \(\omega\) and its
norm remains bounded.

The coordinate
\(t=(\log y_1+\log y_2)/\sqrt6\) has unit gradient. The area of a
compact Sol horosection \(t=T\) is \(O(e^{-\sqrt6 T})\). One may
check this directly: with \(r=\log(y_1y_2)\) and
\(s=\log(y_1/y_2)\), the four-volume density is
\(e^{-r}dx_1dx_2drds/18\); the unit action makes the \(s\) direction
periodic on the Sol quotient. In particular the boundary areas tend
to zero.

Choose smooth functions \(\chi\) on the disjoint cusps, zero near
the compact part and one sufficiently far out. Extend \(\chi\eta\)
by zero and define
\[
 \zeta=\omega-d(\chi\eta)\in\Omega^2_c(N),\qquad d\zeta=0.
                                                               \tag{8}
\]
On cusp truncations \(N_T\), Stokes' formula and (7) give
\[
 \int_N\omega\wedge\zeta
 =\lim_{T\to\infty}
  \left(\int_{N_T}\omega^2
        -\int_{\partial N_T}\omega\wedge\eta\right)
 =2\operatorname{Vol}(N)>0.                              \tag{9}
\]
The boundary term tends to zero because the two forms are bounded and
the boundary area tends to zero. Thus the Kähler form is detected by
a smooth compactly supported closed two-form. No assertion that an
arbitrary primitive of \(\omega\) is bounded is made or needed.

Since \(\zeta\) is compactly supported and closed, one also has
\[
 \int_N\zeta^2=\int_N\omega\wedge\zeta
              -\int_N d(\chi\eta)\wedge\zeta
             =2\operatorname{Vol}(N)>0.                 \tag{10}
\]
The second term is the integral of a compactly supported exact
four-form. This identifies a nonzero intersection pairing on a
compact cusp core, not only a nonzero ordinary cohomology class.

## 6. The compact-core embedding is already impossible

**Theorem 4.** A sufficiently large compact cusp core of a smooth
finite-volume noncompact irreducible
\(\mathbb H^2\times\mathbb H^2\) quotient by a subgroup of
\(\mathrm{PSL}(2,\mathbb R)^2\) cannot embed as a
codimension-zero submanifold of \(M\).

**Proof.** Work with the oriented factor-preserving quotient and
the compactly supported \(\zeta\) constructed above. Take a compact
cusp core \(C\) containing its support in the interior. Suppose
\(\iota:C\hookrightarrow M\) is a smooth embedding. It is
nullhomotopic by Proposition 3 and the asphericity of \(M\).
Transport \(\zeta\) to \(\iota(C)\) and extend it by zero to a
smooth closed two-form \(\widehat\zeta\) on \(M\). Nullhomotopy
gives
\(\iota^*[\widehat\zeta]=0\), so \(\zeta=d\theta\) on \(C\).
Stokes' formula, using that \(\zeta\) vanishes near \(\partial C\),
would then give
\[
 0=\int_Cd(\theta\wedge\zeta)=\int_C\zeta^2
   =2\operatorname{Vol}(N)>0.                           \tag{11}
\]
This contradiction proves the theorem. \(\square\)

The factor-preserving hypothesis is automatic in the application,
because Round 15 supplies globally oriented parallel factor planes.
The theorem itself is a topological obstruction to a core embedding;
it requires no Einstein equation on the target metric.

**Corollary 5.** Under the hypotheses of Section 1, if \(M\) is one
of the specified non-Kähler smooth types, every complete smooth
noncollapsed pointed limit of (2) has reducible lattice.

**Proof.** If the lattice were irreducible, the noncompact finite-
volume limit would be a Hilbert modular quotient by Section 4.
Smooth pointed convergence would embed each fixed compact core in
\(M\) for all sufficiently large \(j\), contrary to Theorem 4.
\(\square\)

Here the finite-product description of a reducible quotient is a
classical lattice fact, not a new splitting theorem for \(M\).
For completeness, let \(\Lambda<H\times H\),
\(H=\mathrm{PSL}(2,\mathbb R)\), be the limit lattice. Borel density
and the classification of proper nondiscrete closed subgroups of
\(H\) show that a projection is either discrete or dense: a proper
nondiscrete closed subgroup normalizes a nonzero proper Lie
subalgebra, and so cannot be Zariski dense. If both projections are
dense the lattice is irreducible. Otherwise, interchange factors so
that \(\Delta_1=\operatorname{pr}_1\Lambda\) is discrete. Haar
disintegration in the quotient then shows that \(\Delta_1\) and
\(\Delta_2=\Lambda\cap(\{1\}\times H)\) are lattices in their
respective factors. The second projection normalizes \(\Delta_2\).
Its normalizer is discrete: a sequence of normalizing elements
approaching the identity eventually centralizes two noncommuting
elements of \(\Delta_2\), and hence is the identity. Finite
covolume now implies
\([N_H(\Delta_2):\Delta_2]<\infty\).
The kernel of
\(\Lambda\to N_H(\Delta_2)/\Delta_2\) is consequently finite index
and equals \(\Delta'_1\times\Delta_2\): multiply an element whose
second component is in \(\Delta_2\) by that component's inverse.
Both factors are torsion-free because \(\Lambda\) is. This gives
the claimed finite cover by two finite-area surfaces. Noncompactness
of the quotient makes at least one surface noncompact. The density
input is Borel, *Density properties for certain subgroups of
semi-simple groups without compact components*, Annals of Mathematics
72 (1960), 179--188; the general finite-index lattice decomposition
is Raghunathan, *Discrete Subgroups of Lie Groups*, Theorem 5.22.

### A second proof using the actual monopole curvature

The following gives a useful analytic version of the same obstruction
when one has cohomological pullback information but not a
codimension-zero extension argument.

Use the actual monopoles in the positive orientation on \((M,g_j)\).
Regard their determinant curvatures as real two-forms \(\mathcal F_j\)
(divide the unitary curvature by \(i\), with a consistent sign).
They are closed and represent \(2\pi a_j\). The Seiberg--Witten
equation identifies their self-dual part with a fixed nonzero multiple
of the quadratic spinor form \(\psi_j\); in the normalization of
Round 15 the magnitude of that multiple is \(1/(2\sqrt2)\).
The estimates in that round give
\[
 \|\mathcal F_j^-\|_{L^2(M)}^2\leq2D_j\longrightarrow0,
 \quad \|\nabla\psi_j\|_{L^2(M)}\longrightarrow0,
 \quad \||\psi_j|-12\|_{L^2(M)}\longrightarrow0.          \tag{12}
\]
Pull the forms back by the pointed-convergence embeddings. On every
fixed compact subset of \(N\), local Rellich compactness makes
\(\psi_j\) converge strongly in \(L^2\) to a nonzero parallel
self-dual two-form. On the product cover its only parallel self-dual
line is generated by \(\omega\). After choosing its sign,
\[
 \mathcal F_j\longrightarrow c\omega
 \quad\hbox{in }L^2_{\mathrm{loc}}(N),\qquad |c|=3.       \tag{13}
\]
Indeed \(|\psi_\infty|=12\), \(|\omega|=\sqrt2\), and
\(12/(2\sqrt2\sqrt2)=3\). This uses the full curvature, including
the disappearing anti-self-dual part, not merely a nonclosed model
form.

Choose a compact cusp truncation \(C\) with
\(\operatorname{supp}\zeta\subset\operatorname{int}C\), and choose
the convergence embeddings \(\iota_j:C\to M\) for large \(j\).
Each \(\iota_j\) is nullhomotopic by Proposition 3 and asphericity.
Therefore \([\iota_j^*\mathcal F_j]=0\) in
\(H^2_{\mathrm{dR}}(C)\), even if the classes \(a_j\) vary with
\(j\). Write \(\iota_j^*\mathcal F_j=d\theta_j\) on \(C\).
Because \(d\zeta=0\) and its support avoids the boundary,
\[
 \int_C\iota_j^*\mathcal F_j\wedge\zeta=0.               \tag{14}
\]
There is no need to bound the primitives \(\theta_j\). Strong local
\(L^2\) convergence suffices to pass to the limit in (14), giving
\[
 0=c\int_N\omega\wedge\zeta
   =2c\operatorname{Vol}(N),                            \tag{15}
\]
contrary to (9) and \(c\ne0\). \(\square\)

Neither proof identifies \(\pi_1(N)\) with a subgroup of \(G\).

## 7. What remains compatible: an actual reducible limit

The exclusion cannot be extended to reducible product limits by the
same argument. There is a direct geometric reason, already present in
the closed construction.

Take one block \(B=F_{h,2}\times F_g\), keep the internal
Fenchel--Nielsen parameters of the first factor fixed, and let its two
geodesic boundary lengths tend to zero. It converges on compact sets
to a complete finite-area surface \(B_0\) with two cusps. In the
Round 11 near-Einstein metrics, the supports of both the mapping-class
interpolation and the integer shear recede to infinite distance from
a basepoint in the thick part. Consequently
\[
 (M,G_\ell,p)\longrightarrow
 (B_0\times F_g,b_0+h_F,p_\infty)                         \tag{16}
\]
smoothly on every compact set. Its entire volume equals the limiting
closed volume:
\[
 \operatorname{Vol}(B_0\times F_g)
 =\frac{4\pi h}{3}\frac{4\pi(g-1)}3
 =\frac{4\pi^2\chi(M)}9=V_*.                             \tag{17}
\]
The cusp cross-sections are \(S^1\times F_g\), not Sol manifolds.
Their groups \(\mathbb Z\times\pi_1(F_g)\) are the original
injective edge groups. Thus no nullhomotopy conclusion like
Proposition 3 is available. The limiting fibre area form has nonzero
period on \(\{b\}\times F_g\), and the corresponding cycle survives
in the vertex subgroup of \(G\).

This is a sequence of approximate, not exact, Einstein metrics. It
shows that bounded curvature, finite-volume product limits, total
volume tending to \(V_*\), and the original non-Kähler topology are
jointly compatible. The unresolved exact problem is now restricted
to reducible limiting geometries and the matching through their
collapsing regions; it is not eliminated by a lattice classification.

## 8. Relation to the previous global restrictions

Round 13 excluded a continuous normalized Einstein branch reaching
\(V_*\). Round 15 showed that a remaining sequence must have bounded
curvature, unbounded diameter, and a complete finite-volume product
limit. Theorem 4 further excludes the irreducible arithmetic
alternative without assuming survival of its fundamental group.

No positive volume gap \(\operatorname{Vol}(g)-V_*\geq\epsilon(M)\)
has yet been established: the reducible alternative in Section 7 is
not contradicted by these arguments. Nor is there a classification of
all larger-volume Einstein metrics on \(M\). The additional input
needed for a volume-gap theorem must control the actual Einstein
matching between reducible pieces, not merely repeat that the
original closed group is not a product lattice.
