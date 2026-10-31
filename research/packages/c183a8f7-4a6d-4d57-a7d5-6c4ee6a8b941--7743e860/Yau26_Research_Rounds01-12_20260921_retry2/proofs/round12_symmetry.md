# Global topology forces complete local symmetry breaking

21 September 2026.

## 1. Statement

Let \(M=M(h,g;u,f)\) be the closed self-gluing from
[Round 11](round11_graph_topology.md), with \(h\ge1\), \(g\ge2\),
and nonzero integral shear \(u\). There is no order assumption on the
mapping class of \(f\).

**Theorem.** For every smooth Riemannian metric \(g\) on \(M\), the
isometry group of its Riemannian universal cover is discrete. For every
Einstein metric on \(M\), the vector space of germs of local Killing
fields at every point is zero.

Thus an Einstein metric, if one exists, cannot have a circle-invariant
neck, an open product region, or any other open region with a nonzero
local Killing field. This holds without a closeness assumption,
without a prescribed foliation or orbit-radius function, and without
requiring the local symmetry to descend to a global action on \(M\).
The same conclusion holds on every finite cover.

This is a consequence of the specific group obstruction proved in
Round 11 and classical universal-cover rigidity and analytic
continuation. It is not a new general rigidity theorem, and it does
not assert that an Einstein metric without local symmetries is
impossible.

## 2. No normal abelian subgroup

Write
\[
G=\pi_1(M),\qquad V=A\times\Gamma,
\quad A=\pi_1(F_{h,2}),\quad\Gamma=\pi_1(\Sigma_g).
\]
The Bass--Serre action on the tree \(T\) is minimal and \(T\) is
neither a point nor a line. The vertex stabilizers are conjugates of
\(V\), as proved in [the tree calculation](round11_kahler.md).

Suppose \(N\triangleleft G\) is abelian. Then \(N\cap V\) is an
abelian normal subgroup of \(V\). Its projections to \(A\) and
\(\Gamma\) are abelian normal subgroups of those factors. Neither
a nonabelian free group nor a closed hyperbolic surface group has a
nontrivial abelian normal subgroup: nontrivial abelian subgroups are
cyclic, whereas their normalizers are virtually cyclic and cannot be
the entire group. Hence \(N\cap V=1\).

Normality gives the same conclusion at every vertex stabilizer.
Consequently every nonidentity element of \(N\) acts hyperbolically
on \(T\). If such an element \(n\) exists, every element commuting
with \(n\) preserves its axis. Every nonidentity element of \(N\)
has that same axis. Since \(N\) is normal in \(G\), the common
axis is \(G\)-invariant. This contradicts minimality and the fact
that \(T\) is not a line. Therefore
\[
                  G\text{ has no nontrivial normal abelian subgroup}.
\tag{1}
\]
No finite-generation assumption on \(N\) was used.

## 3. Smooth irreducibility

Round 11 establishes that \(M\) is aspherical,
\(\chi(M)=4h(g-1)>0\), and no finite cover of \(M\) is Kähler.
Suppose a finite cover were diffeomorphic to a nontrivial product of
closed positive-dimensional smooth manifolds. Each factor is
aspherical, since all its higher homotopy groups are direct summands
of those of the product.

In dimension four, a product with a one-dimensional factor has zero
Euler characteristic, contrary to multiplicativity under finite
covers. The only remaining dimension partition is \(2+2\). After
taking orientation covers of the factors, the product is a product
of closed orientable aspherical surfaces. It admits a product complex
structure and a Kähler metric. This would give a Kähler finite cover
of \(M\), also impossible. Hence \(M\) is smoothly irreducible in
the sense that no finite cover is a nontrivial smooth product.

## 4. Universal-cover rigidity

[Farb--Weinberger, Theorem 1.3](https://math.uchicago.edu/~farb/papers/isoms.pdf)
applies to closed aspherical smoothly irreducible manifolds whose
fundamental group has no nontrivial normal abelian subgroup. If the
universal-cover isometry group is nondiscrete, the metric must be
irreducible locally symmetric of nonpositive sectional curvature.
The hypotheses have just been proved for every choice of metric on
our fixed \(M\).

The possible four-dimensional symmetric universal covers without a
Euclidean factor are
\[
\mathbb H^4,\qquad\mathbb{CH}^2,
\qquad\mathbb H^2\times\mathbb H^2,
\tag{2}
\]
allowing rescaling of irreducible factors. A symmetric space with a
Euclidean factor has zero Euler curvature density in dimension four;
its compact quotient would have \(\chi=0\), which is excluded here.
None of (2) can occur:

* \(G\) contains \(\mathbb Z^2\), from the embedded vertex group
  \(A\times\Gamma\); a closed real-hyperbolic manifold group does
  not.
* Complex hyperbolic quotients have a finite cover preserving their
  parallel complex structure and are then Kähler.
* A bidisk quotient has a finite cover preserving the factor
  orientations and the product complex structure and is also Kähler.

The last two alternatives contradict the finite-cover obstruction.
Thus \(\operatorname{Isom}(\widetilde M,\widetilde g)\) is discrete
for every \(g\). This part does not use the Einstein equation.

## 5. Einstein analyticity converts this into a local statement

Assume now that \(g\) is Einstein. By
[DeTurck--Kazdan, Theorem 5.2](https://www.numdam.org/article/ASENS_1981_4_14_3_249_0.pdf),
the metric is real analytic in harmonic coordinates. Lift a putative
nonzero local Killing field to the complete simply connected
Riemannian universal cover. Nomizu's extension theorem extends it
to a global Killing field there; see
[Nomizu, *On Local and Global Existence of Killing Vector Fields*](https://doi.org/10.2307/1970148)
and the author's [original announcement, abstract 564-9](https://www.ams.org/journals/notices/195912/195912FullIssue.pdf).

On a complete Riemannian manifold a global Killing field is complete.
Indeed its speed is constant along each of its own integral curves;
a finite-time curve remains in a bounded metric ball, so completeness
and Hopf--Rinow permit extension. Its flow therefore gives a
nontrivial one-parameter group of global isometries. This contradicts
Section 4 and proves the theorem.

For an arbitrary metric on a finite cover, rather than just the lift
of a metric on \(M\), repeat the argument with its finite-index
subgroup \(H<G\). Its action on \(T\) remains minimal, as proved
in Round 11. If \(N\triangleleft H\) is abelian, the projections
of \(N\cap(H\cap V)\) are normal abelian subgroups of the
finite-index projections of \(H\cap V\) to the two surface factors.
They are trivial, and the common-axis argument again excludes \(N\).
Positive Euler characteristic, smooth irreducibility, the embedded
\(\mathbb Z^2\), and the virtual Kähler obstruction all persist.
Farb--Weinberger and analytic continuation therefore apply directly
to every metric of the appropriate kind on the finite cover.

## 6. Consequence for the constructed metrics and the actual research target

The smooth near-Einstein metrics \(G_\ell\) have genuine local circle
symmetry on their collars and exact locally product pieces. These
symmetries do not extend globally on the universal cover: the metrics
are not Einstein or globally analytic. Thus Section 4 does not
contradict their construction.

For exact repair, the conclusion is stronger than merely requiring
a spatially varying orbit radius or a nonzero connection. Keeping
**any** local circle action is impossible for a closed Einstein
completion on this \(M\). The quantitative
[collar calculation](round12_repair.md) remains useful independently:
it measures boundary backreaction on an abstract collar and applies
without this closed topology. The global argument here eliminates
all locally symmetric repair sectors for the specific closed family.

This still allows arbitrarily small but nonzero symmetry-breaking
corrections. The theorem gives no lower bound on their size and no
compactness statement. Nor does it exclude a distant Einstein metric.
The next full equation must therefore allow all angular modes and
the coupled quotient geometry, or obtain a quantitative theorem
forcing a genuine local symmetry from the near-product regime.
Topology alone in the present argument does not supply that theorem.

The geometric phenomenon is precise: the family approaches
\(\mathbb H^2\times\mathbb H^2\) locally, while any exact Einstein
metric on the same closed smooth manifold must have no continuous
local symmetry anywhere. Local product limits and globally
homogeneous exact outputs are distinct possibilities.
