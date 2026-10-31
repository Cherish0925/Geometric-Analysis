# Sheared product-surface gluings beyond surface bundles

21 September 2026.

## 1. The closed objects

Let \(F_{h,b}\) be a compact connected oriented surface with \(b>0\)
boundary circles and negative Euler characteristic, and let \(\Sigma_g\)
be a closed oriented surface of genus \(g\ge2\). The blocks are
\(F_{h,b}\times\Sigma_g\). Boundary identifications have the form
\[
 (\phi,x)\longmapsto(-\phi+u(x),f(x)),
 \qquad u:\Sigma_g\longrightarrow\mathbb R/2\pi\mathbb Z,
 \quad f\in\operatorname{Diff}^+(\Sigma_g).
 \tag{1.1}
\]
The sign is chosen for an oriented gluing. The homotopy class of \(u\)
is an integral cohomology class; write the corresponding homomorphism
\(\pi_1(\Sigma_g)\to\mathbb Z\) by the same letter.

The metric construction in `round11_closed_gluing.md` is a separate
input. The results below identify its actual smooth manifolds and groups;
they do not assume an Einstein metric or a curvature sign.

Two elementary properties hold for every closed oriented assembly:
\[
 \chi(M)=(2-2g)\sum_v\chi(F_v)>0,
 \qquad \tau(M)=0.
 \tag{1.2}
\]
Euler characteristic is additive because each gluing hypersurface has
Euler characteristic zero. Every product block has signature zero: an
orientation-reversing diffeomorphism of its first surface reverses its
orientation. Novikov additivity then applies across the whole closed
three-dimensional gluing hypersurfaces. There are no corners requiring
a Wall nonadditivity term.

Each block and each boundary component is aspherical, and the boundary
fundamental groups inject into the block groups. The universal cover is
a tree of contractible vertex and edge spaces. Thus \(M\) is aspherical,
and its group is the graph of groups prescribed by (1.1).

## 2. A separating gluing is an earlier surface-bundle object

Suppose there are two blocks \(F_{h_1,1}\times\Sigma_g\) and
\(F_{h_2,1}\times\Sigma_g\), joined along their only boundaries by
(1.1). Use \(f^{-1}\) to identify the second copy of the base with the
first. The projection to \(\Sigma_g\) then extends over the gluing.
The result is a smooth bundle
\[
 \Sigma_{h_1+h_2}\longrightarrow M\longrightarrow\Sigma_g.
 \tag{2.1}
\]
For a loop \(\gamma\) in the base its monodromy is
\(D_c^{\pm u(\gamma)}\), where \(c\) is the separating seam.
To see this, locally lift \(u\) to a real angle and absorb that angle
in a collar of the seam. Two lifts differ by an integral full rotation;
the transition on the closed fibre is the corresponding power of the
Dehn twist. This is a rank-one multitwist bundle of the earlier
\(E_D\) type, with the two surface roles interchanged.

This does **not** mean that a nonzero shear extends over a product block.
In fact it does not, as the following group calculation shows.

**Nonextension lemma.** Let \(F\) have negative Euler characteristic,
\(c\) be a boundary loop, and \(u\ne0\). The boundary map (1.1) does
not extend to a diffeomorphism of \(F\times\Sigma_g\).

Write \(\pi_1(F\times\Sigma_g)=A\times\Gamma\), with \(A\) a
nonabelian free group and \(\Gamma=\pi_1(\Sigma_g)\). The centralizer
of \(\{1\}\times\Gamma\) is \(A\times\{1\}\). The boundary shear
maps this subgroup, up to conjugacy, to
\[
 \Gamma_u=\{(c^{u(\gamma)},f_*(\gamma)):\gamma\in\Gamma\}.
\]
Since \(f_*\) is onto and \(u\ne0\), the centralizer of \(\Gamma_u\)
is \(C_A(c^k)\times\{1\}\cong\mathbb Z\), for any nonzero value
\(k\) of \(u\). The centralizer of a nontrivial element of a free group
is cyclic. An automorphism induced by an extension would have to identify
these two centralizers, which is impossible. This also excludes an
extension not preserving the product factors.

## 3. A cyclic gluing which is not any surface bundle over a surface

Take a **single** block
\[
 B=F_{h,2}\times\Sigma_g,\qquad h\ge1,\quad g\ge2,
\]
and identify its two boundary components by (1.1). Denote the resulting
closed manifold by \(M(h,g;u,f)\). Put
\[
 A=\pi_1(F_{h,2})\cong F_{2h+1},\qquad \Gamma=\pi_1(\Sigma_g),
\]
and write \(c_1,c_2\in A\) for the two boundary elements. With suitable
base paths, its fundamental group is the HNN extension
\[
 G=\left\langle A\times\Gamma,t\;\middle|\;
 t c_1t^{-1}=c_2^{-1},\quad
 t\gamma t^{-1}=c_2^{u(\gamma)}f_*(\gamma)
 \ (\gamma\in\Gamma)\right\rangle .
 \tag{3.1}
\]
Changing base paths changes the representatives by conjugacy, not the
statements below. The edge injections are injective, so the vertex group
\(A\times\Gamma\) embeds in \(G\).

**Theorem.** If \(u\ne0\) and \([f_*]\) has infinite order in
\(\operatorname{Out}(\Gamma)\), there is no exact sequence
\[
 1\longrightarrow\pi_1(\Sigma_p)\longrightarrow G
   \longrightarrow\pi_1(\Sigma_q)\longrightarrow1,
 \qquad p,q\ge2.
 \tag{3.2}
\]
Consequently \(M(h,g;u,f)\) is not the total space of an oriented closed
surface bundle over an oriented closed surface.

**Proof.** Suppose \(\psi:G\to\Pi_q\) has kernel \(K\cong\Pi_p\),
where \(\Pi_j\) is a closed hyperbolic surface group. Such groups contain
no \(\mathbb Z^2\); the centralizer of a nonidentity element is cyclic;
and the centralizer of a nonabelian subgroup is trivial.

The subgroups \(\psi(A)\) and \(\psi(\Gamma)\) commute. If neither is
nonabelian, both are cyclic or trivial. Both restrictions then have
nontrivial kernels: a nonabelian free group and a closed hyperbolic
surface group cannot inject into a cyclic group. Choose nonidentity
elements in these two kernels. Their copies in the direct product
generate \(\mathbb Z^2\subset K\), a contradiction. Hence one of the
two images is nonabelian and the other is trivial.

If \(\psi(A)\) is nonabelian, then \(\Gamma\subset K\). Normality of
\(K\), together with the second HNN relation, implies
\(c_2^{u(\gamma)}\in K\) for every \(\gamma\in\Gamma\). Choose
\(\gamma\) for which \(u(\gamma)\ne0\). This nontrivial element of
\(A\) commutes with \(\Gamma\subset K\), again yielding
\(\mathbb Z^2\subset K\).

If \(\psi(\Gamma)\) is nonabelian, then \(A\subset K\). The
restriction \(r=\psi|_\Gamma\) is injective: a nonidentity element of
its kernel would commute with a nonidentity element of \(A\), producing
the same contradiction. An embedded closed hyperbolic surface group in
another closed hyperbolic surface group has finite index. Indeed an
infinite-index subgroup is the group of a noncompact covering surface
and is free, whereas \(\Gamma\) is not free.

Let \(a=\psi(t)\). Since \(\psi(c_2)=1\), (3.1) gives
\[
 a r(\gamma)a^{-1}=r(f_*(\gamma)).
\]
The subgroup \(r(\Gamma)\) is normalized by \(a\) and has finite index.
Some positive power \(a^N\) therefore lies in \(r(\Gamma)\). Iterating
the displayed equation and using injectivity of \(r\) shows that
\(f_*^N\) is inner. This contradicts the hypothesis on \([f_*]\),
and proves (3.2).

For the bundle consequence, (1.2) gives \(\chi(M)>0\). Euler
characteristic multiplicativity eliminates a torus fibre or base and
the opposite-sign sphere/hyperbolic combinations. The only remaining
nonhyperbolic possibility is a sphere bundle over a sphere, inconsistent
with the embedded infinite vertex group. Thus any such bundle would
give (3.2). \(\square\)

This excludes **every** oriented surface-bundle structure on this
manifold, not merely the two projections suggested by its construction.
It does not assert that no finite cover is a surface bundle.

## 4. Fully specified small examples

The theorem requires infinite mapping-class order, not a pseudo-Anosov
mapping class.

For one explicit choice, take \(h=1\), \(g=2\), let \(\alpha\) be a
nonseparating curve in \(\Sigma_2\), take \(f=D_\alpha\), and choose
\(u\) to be the primitive algebraic-intersection functional with
\(\alpha\). This specifies all gluing data in (3.1).

There is also an **even-first-Betti-number** example. Split \(\Sigma_2\)
into two once-holed tori, and on each use a boundary-fixing mapping class
whose homology matrix is
\[
 H=\begin{pmatrix}2&1\\1&1\end{pmatrix}.
\]
Such a map is a product of two Dehn twists with chosen signs. The product
\(f\) of the two disjointly supported maps has homology action
\(F=\operatorname{diag}(H,H)\). It has infinite order, since \(H\) has
an eigenvalue greater than one. Choose any primitive nonzero \(u\).

Here is the abelianization calculation, including the shear. Writing
\(c=[c_2]\), one has \([c_1]=-c\), so the first HNN relation adds no
new abelian relation. The second relation imposes
\[
 (I-f_*)x-u(x)c=0,\qquad x\in H_1(\Sigma_g;\mathbb Z).
 \tag{4.1}
\]
Thus
\[
 H_1(M;\mathbb Z)=\mathbb Z^{2h+1}\oplus
 \frac{\mathbb Z c\oplus H_1(\Sigma_g;\mathbb Z)}
 {\langle (I-f_*)x-u(x)c\rangle}.
 \tag{4.2}
\]
The \(2h+1\) free summands outside the fraction are the \(2h\) handle
generators and the HNN stable letter.

In the first example, \(f_*-I\) has image generated by
\([\alpha]\), with coefficient \(u\). Equation (4.1) eliminates one
primitive combination of \(c\) and \([\alpha]\). In the second example
\(\det(I-F)=1\), so (4.1) eliminates all four surface-homology
generators in favour of \(c\), with no torsion. Consequently:

| Example | \(\chi\) | \(\tau\) | \(b_1\) | \(b_2\) | \(b_2^+=b_2^-\) |
|---|---:|---:|---:|---:|---:|
| Single twist, dual shear | 4 | 0 | 7 | 16 | 8 |
| Two hyperbolic homology blocks, primitive shear | 4 | 0 | 4 | 10 | 5 |

The exact checker `round11_graph_topology_check.py` computes the integral
Smith normal forms of these two presentation matrices. Their nonzero
invariant factors are all one, so neither abelianization has torsion.
It also verifies the displayed Betti numbers and the symplectic condition
on the two homology actions. This check does not replace the group proof
in Section 3.

The second example makes clear that odd Betti-number parity is not the
basis of the nonbundle theorem. Related smooth types may already arise
from cut-and-paste or Luttinger-surgery constructions; no classification
or novelty of these smooth manifolds is asserted.

## 5. Which global obstructions do and do not apply

An Einstein metric on any of these manifolds must have negative Einstein
constant. Positive Ricci curvature would make the fundamental group
finite; Ricci-flatness on a closed manifold would make it virtually
abelian. Both are incompatible with its embedded nonabelian free group.
This is a sign reduction, not negative-Einstein nonexistence.

The familiar higher-graph results cannot be applied by name alone.
Connell--Suarez-Serrato's [Definition 1](https://arxiv.org/pdf/1208.4876)
requires infranil fibres over pinched-negative bases. Our closed
hyperbolic surface fibre is not infranil, and its boundary group
\(\mathbb Z\times\Pi_g\) is nonamenable. In particular their
infranil-fibre collapse and amenable-wall simplicial-volume arguments
do not establish corresponding statements here.

Contreras Peruyero--Suarez-Serrato's
[Theorems 5--6](https://arxiv.org/pdf/2107.14380) concern, respectively,
pieces of geometries \(\mathbb H^3\times\mathbb R\),
\(\widetilde{\mathrm{SL}}_2\times\mathbb R\),
\(\mathbb H^2\times\mathbb R^2\), and higher-graph classes with the
specified collapse hypotheses. Their proof uses \(\chi=\tau=0\).
Our pieces have geometry \(\mathbb H^2\times\mathbb H^2\), and
\(\chi(M)>0\), so that proof does not supply a contradiction.

The separate `round11_kahler.md` establishes a Kähler-group obstruction
using the Bass--Serre action and a primary tree-factorization theorem.
Its finite-cover argument uses the normal finite-index core to preserve
minimality of the action. This is stronger information about complex
geometry, but it still cannot be substituted for an obstruction to
arbitrary negative Einstein metrics.

The exact global problem is now sharper: the closed near-Einstein
construction applies to explicit aspherical manifolds **outside all
oriented surface bundles over surfaces**, not only to a reparametrized
\(E_D\) family. Deciding arbitrary Einstein existence on these same
smooth manifolds remains open in this work. The topology results above
do not silently restrict the potential Einstein metric to preserve the
graph decomposition, either surface factor, or any circle action.
