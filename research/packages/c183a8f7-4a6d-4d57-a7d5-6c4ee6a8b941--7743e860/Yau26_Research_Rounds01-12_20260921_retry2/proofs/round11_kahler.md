# A virtual Kähler obstruction for the closed sheared gluings

21 September 2026.

## 1. Statement and geometric consequence

Let \(M=M(h,g;u,f)\) be obtained from
\(F_{h,2}\times\Sigma_g\), \(h\ge1\), \(g\ge2\), by identifying
its two boundary components by
\[
 (\phi,x)\longmapsto(-\phi+u(x),f(x)).
\]
Here \(f\) is orientation preserving and \(u:\Sigma_g\to S^1\)
has nonzero integral cohomology class. No order condition on \([f]\)
is needed in this note.

**Theorem.** No finite-index subgroup of \(\pi_1(M)\) is a Kähler
group. In particular, no finite cover of \(M\), with either orientation,
admits any Kähler structure.

Combined with [the closed construction](round11_closed_gluing.md), this
gives fixed closed aspherical four-manifolds with uniformly bounded
curvature and all fixed curvature derivatives, with
\[
 \|G_\ell^{-1}\operatorname{Ric}_{G_\ell}+3I\|_\infty\longrightarrow0,
 \qquad \operatorname{Vol}(G_\ell)=\frac{4\pi^2}{9}\chi(M),
\]
but with no Kähler structure even after passage to a finite cover. If
\([f]\) has infinite order, the separate
[group argument](round11_graph_topology.md#3-a-cyclic-gluing-which-is-not-any-surface-bundle-over-a-surface)
also excludes every oriented closed surface-bundle structure on \(M\).
These are different conclusions, proved by different arguments.

The Kähler obstruction does not exclude an arbitrary negative Einstein
metric. It removes a concrete class of global existence mechanisms;
it does not impose complex structure on a hypothetical Einstein metric.

## 2. The tree and its kernel

Set \(A=\pi_1(F_{h,2})\), \(\Gamma=\pi_1(\Sigma_g)\), and
\(V=A\times\Gamma\). Write \(c_1,c_2\in A\) for the boundary
elements. The group is
\[
 G=\left\langle V,t\ \middle|\
 tc_1t^{-1}=c_2^{-1},\quad
 t\gamma t^{-1}=c_2^{u(\gamma)}f_*(\gamma),\ \gamma\in\Gamma
 \right\rangle .                                      \tag{1}
\]
Both edge injections are injective. Let \(T\) be the Bass--Serre tree
and \(v\) the vertex stabilized by \(V\). One adjacent edge has
stabilizer \(E_1=\langle c_1\rangle\times\Gamma\). The other
embedding also has image \(E_2=\langle c_2\rangle\times\Gamma\):
the powers of \(c_2\) already belong to the edge group and remove the
shear in its second factor.

Both \(E_i\) have infinite index in \(V\). Hence \(T\) is not a
line. The action is minimal. One direct verification is that the stable
letter has an axis through \(v\); every nonempty invariant subtree
contains this axis and therefore, by vertex transitivity, every vertex.
There is no fixed end: if \(V\) fixed an end, it would fix the first
edge of the unique ray from \(v\) to that end. This would put \(V\)
inside a proper adjacent edge stabilizer.

Let \(C=\ker(G\curvearrowright T)\). Since it fixes every edge,
\[
 C\subseteq\bigcap_{a\in A}aE_1a^{-1}=\Gamma.             \tag{2}
\]
Indeed the normal core of a peripheral cyclic subgroup in the
nonabelian free group \(A\) is trivial. This follows, for example,
by choosing an element outside its cyclic normalizer and intersecting
the two conjugates. Boundary elements in this surface group are not
proper powers.

The kernel \(C\) is normal in \(G\). For \(\gamma\in C\), (1)
and (2) give
\[
 c_2^{u(\gamma)}f_*(\gamma)=t\gamma t^{-1}\in C\subseteq\Gamma.
\]
The two direct factors of \(V\) intersect trivially, and \(c_2\)
has infinite order. Consequently
\[
                 C\subseteq\Gamma\cap\ker u.             \tag{3}
\]
We do not need to identify \(C\) exactly. It may be infinitely
generated; replacing it by a surface group would be incorrect.

## 3. The Kähler-group input

The tree factorization theorem of Gromov--Schoen, in the precise form
stated in [Nicolás, Theorem 25 and Lemma 24, p. 10 of the PDF](https://arxiv.org/pdf/2102.01128),
has the following consequence. If a compact Kähler group acts minimally
on a tree other than a point or a line, without fixing an end, there is
an exact sequence
\[
 1\longrightarrow N\longrightarrow H
   \longrightarrow\Pi^{\rm orb}\longrightarrow1,          \tag{4}
\]
where \(\Pi^{\rm orb}\) is a closed hyperbolic orbifold group,
\(N\) is finitely generated, and \(N\) acts trivially on the tree.
Finite generation follows because \(N\) is the image of the
fundamental group of the compact generic fibre of the associated
holomorphic map. The result applies without assuming a faithful
tree action. The original source is
[Gromov--Schoen, Publ. Math. IHÉS 76 (1992), 165--246](https://numdam.org/item/PMIHES_1992__76__165_0/).

We also use the following elementary surface-group fact: a nontrivial
finitely generated normal subgroup of a closed hyperbolic surface group
has finite index. In the covering-surface description, a finitely
generated infinite-index subgroup is free and has a finite compact
core. A nontrivial normal subgroup cannot have such a proper compact
core: equivalently its limit set, invariant under the whole cocompact
surface group, is the entire boundary circle, whereas an infinite-index
finitely generated subgroup has proper limit set. A cyclic normal
subgroup is already excluded by cyclic centralizers.

## 4. Proof for every finite cover

Let \(H<G\) have finite index and suppose it is a Kähler group.
We first check the tree hypotheses for \(H\), rather than assume
they pass to finite index without proof.

Let \(H_0\) be the normal finite-index core of \(H\) in \(G\).
A positive power of \(t\) belongs to \(H_0\), so \(H_0\) contains
a hyperbolic tree isometry. Its minimal subtree exists and is unique,
being the convex hull of its hyperbolic axes. Normality makes this
subtree \(G\)-invariant. Minimality of \(G\) therefore makes it
all of \(T\). Thus \(H\) acts minimally as well.

If \(H\) fixed an end, \(H\cap V\) would stabilize the first edge
of the ray from \(v\). This is impossible: \(H\cap V\) has finite
index in \(V\), whereas every adjacent edge stabilizer has infinite
index in \(V\). The tree is still not a point or a line.

Apply (4). The group \(N\) lies in
\[
 \ker(H\curvearrowright T)=H\cap C
       \subseteq (H\cap\Gamma)\cap\ker u.                 \tag{5}
\]
Set \(\Gamma_H=H\cap\Gamma\), a finite-index closed surface
subgroup of \(\Gamma\). The group \(N\) is normal in
\(\Gamma_H\), because it is normal in \(H\). It is finitely
generated, so it is either trivial or finite index in \(\Gamma_H\).
The second case is impossible. A nonzero homomorphism
\(u:\Gamma\to\mathbb Z\) remains nonzero on every finite-index
subgroup: for any element on which it is nonzero, a positive power
belongs to that subgroup. Equation (5) says instead that it vanishes
on \(N\).

Therefore \(N=1\). Equation (4) would identify \(H\) with a
hyperbolic orbifold group. But \(V=A\times\Gamma\) contains
\(\mathbb Z^2\), generated by a nonidentity element in each factor.
Its intersection with \(H\) is finite index in \(\mathbb Z^2\).
A cocompact Fuchsian orbifold group contains no \(\mathbb Z^2\).
This contradiction proves the theorem. \(\square\)

## 5. What a hypothetical Einstein metric would have to be

The construction and obstruction apply, in particular, to the explicit
example in `round11_graph_topology.md` with
\[
 \chi(M)=4,\quad\tau(M)=0,\quad b_1(M)=4,\quad b_2^+=b_2^-=5.
\]
Thus the complex-geometric obstruction is not merely odd parity of
\(b_1\).

Any Einstein metric on this \(M\) would have negative Einstein
constant. The positive case is excluded by Myers' theorem and the
infinite fundamental group. The Ricci-flat case is excluded by the
virtually abelian fundamental group theorem for closed nonnegative-Ricci
manifolds: \(G\) contains a nonabelian free subgroup. Neither inference
places restrictions on the unknown negative Einstein metric.

The theorem also excludes every Einstein metric becoming Kähler on a
finite cover. In particular the usual locally symmetric alternatives
are unavailable: a closed real-hyperbolic metric would contradict the
embedded \(\mathbb Z^2\); a complex-hyperbolic metric has a Kähler
finite cover; and a metric locally isometric to
\(\mathbb H^2\times\mathbb H^2\) has a finite cover preserving both
factor orientations, hence a parallel product complex structure.

The unresolved alternative is a genuinely non-Kähler negative Einstein
metric, not necessarily close to the constructed family, not necessarily
respecting its cutting hypersurfaces, and not necessarily having
nonpositive sectional curvature. Excluding such metrics requires a
further argument. If even one of the explicit examples admits no such
metric, its constructed sequence supplies a negative-sign Yau26
counterexample. This alone would not negate the project's unrestricted
interval formulation, which also requires failure of the positive sign
in the same dimension.

The useful new connection is that a shrinking-circle shear costs
arbitrarily little Ricci error but has a permanent effect on the
fundamental group: it traps the kernel of the tree action in an
infinite-index surface subgroup. That is the link between the metric
construction and the virtual Kähler obstruction.
