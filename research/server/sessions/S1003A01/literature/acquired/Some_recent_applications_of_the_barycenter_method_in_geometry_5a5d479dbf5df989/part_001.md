---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Some recent applications of the barycenter method in geometry]

# Some recent applications of the barycenter method in geometry

> Source: https://www.math.uchicago.edu/~farb/papers/georgia.pdf
> Fetched: 2026-10-13 23:12
> Method: FULLTEXT_HTML_FIRECRAWL|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

---

## Verified object metadata

```json
{
  "object_type": "web",
  "identifier": "",
  "identifiers": {},
  "identifier_aliases": {},
  "version": "",
  "published_at": "",
  "updated_at": "",
  "license": "",
  "language": "",
  "source": "tavily",
  "source_url": "https://www.math.uchicago.edu/~farb/papers/georgia.pdf",
  "metadata": {
    "provenance_urls": [
      "https://www.math.uchicago.edu/~farb/papers/georgia.pdf",
      "http://www.math.uchicago.edu/~farb/papers/georgia.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Besson Courtois Gallot barycenter method degree theorem complex hyperbolic target dimension 2"
      }
    ],
    "_knowledge_contract_obligation_ids": [
      "semantic-002"
    ]
  },
  "declared_files": []
}
```

## Source description

Now suppose that, in addition to being negatively curved, M is also locally symmetric with metric gloc. In this case Besson-Courtois-Gallot were able to give a precise estimate on the Jacobian | Jac F|, proving Theorem 2. To state things precisely, it will be useful to ﬁx a parameter s > h(g), where g is the metric on N and h(g) is the volume growth entropy of g. [...] Theorem 18 (Volume Theorem [BCS]). Let (M, g) and (Mo, go) be two oriented complete ﬁnite volume Riemannian manifolds of the same dimen-sion n ≥3 and suppose that Ricg ≥−(n −1)g, and −a ≤Kgo ≤−1.
Then for all proper continuous maps f : M − →Mo, Vol(M, g) ≥|deg(f)| Vol(Mo, go), and equality holds if and only if M and Mo are hyperbolic and f is proper homotopic to a Riemannian covering.
When M and Mo are compact, Theorem 18 follows from a real Schwarz lemma proved by Besson, Courtois, and Gallot in [BCG5]. As in the case of all noncompact situations, to apply the method of [BCG1] and [BCG5], the fundamental diﬃculty is proving the properness of the natural map.
Theorem 18 implies the following.
25 Corollary 19. Under the hypotheses of Theorem 18, Minvol(M) ≥deg(f) Vol(Mo). [...] Some recent applications of the barycenter method in geometry Christopher Connell and Benson Farb ∗ Department of Mathematics University of Chicago July 26, 2002 Contents 1 The Entropy Rigidity Conjecture 3 1.1 The main conjecture . . . . . . . . . . . . . . . . . . . . . . .
3 1.2 Progress . . . . . . . . . . . . . . . . . . . . . . . . 

## Retrieved source content

# Some recent applications of the barycenter method in geometry

Christopher Connell and Benson Farb<sup>⁄</sup>
Department of Mathematics
University of Chicago

July 26, 2002

## Contents

1 The Entropy Rigidity Conjecture 3
1.1 The main conjecture....................... 3
1.2 Progress.. .... ........................ 5
1.3 The Besson-Courtois-Gallot map................ 6
1.4 The degree theorem....................... 7
1.5 A related conjecture.... ................... 9
1.6 Some consequences of the Degree Theorem. ......... 9
2 The Douady-Earle-Besson-Courtois-Gallot map 11
2.1 The construction...... ................... 11
2.2 Patterson-Sullivan measures . . ................. 12
2.3 The barycenter functional. ................... 13
3 Bounding the Jacobian 15
3.1 Existence of some bound . .. .................. 15
3.2 The perfect bound in rank one. ................ 18
4 Negative results in various settings 18
4.1 Finsler metrics.......................... 18
4.2 Magnetic field flows....................... 21
4.3 Metric entropy.. ........................ 22
<sup>⁄</sup>Both authors are supported in part by the NSF. This paper grew out of talks given by
the first and second authors at the Cornell and Georgia Topology conferences, respectively.

---

5 Positive results in various settings 22
5.1 Finsler metrics.......................... 22
5.2 Foliations... .......................... 23
5.3 Finite volume manifolds..................... 25
5.4 Quasifuchsian representations.................. 27
5.5 Alexandroff Spaces........................ 27
5.5.1 Convex Cores ...... ................. 29
5.5.2 Application to Cone Manifolds............. 30
6 Cautionary examples 31
6.1 An example in H² *£* H². ............ ... ..... 32
6.2 An example in SL₃(R)*=*SO₃(R) . ....... ......... 33
6.3 An example in SL₄(R)*=*SO₄(R) . ....... ......... 34

---

## 1 The Entropy Rigidity Conjecture

In this paper we describe some recent applications of the barycenter method
in geometry. This method was first used by Douady-Earle and later greatly
extended by Besson-Courtois-Gallot in their solution of a number of longstanding problems, in particular in their proof of entropy rigidity for closed,
negatively curved locally symmetric manifolds. Since there are already a
number of surveys describing this work (see [BCG2, BCG3, Pa, Ga]), we will
concentrate here only on advances that have occurred after these surveys
appeared. While most of this paper is a report on results appearing in
other papers, some of the material here is new (e.g. Proposition 12 and the
examples in Section 6).

## 1.1 The main conjecture

The *volume entropy* of a closed Riemannian *n*-manifold (*M; g*), denoted by
*h*(*g*), is defined to be

where *B*(*x; R*) is the ball of radius *R* around a fixed point *x* in the universal
cover *X*. The number *h*(*g*) is independent of the choice of *x*, and equals the
topological entropy of the geodesic flow on (*M; g*) when the curvature *K*(*g*)
satisfies *K*(*g*) *•* 0 (see [Ma]). Note that while neither the volume Vol(*M; g*)
nor the entropy *h*(*g*) is invariant under scaling the metric *g*, the *normalized*
*entropy*
ent(g) = h(g)<sup>n</sup> Vol(M; g)

is scale invariant.

Now let *M* be a closed *n*-manifold that admits a locally symmetric Riemannian metric g<sub>loc</sub> of nonpositive sectional curvature. When (M; g<sub>loc</sub>) is
not locally isometric to a product then g<sub>loc</sub> is unique up to homothety (i.e.
multiplying the metric by a number). When *M* is locally a product, one
may show using Lagrange multipliers that there is a unique (up to homothety) locally symmetric metric on *M* which minimizes ent(*g*); see [CF1].
Henceforth we will abuse notation and denote this metric by g<sub>loc</sub>, and call
it *the* locally symmetric metric.

The *Entropy Rigidity Conjecture*, stated in various forms by Katok, Gromov, and Besson-Courtois-Gallot (see, e.g., [BCG2], Open Question 5), has
two components. The purely metric component posits that for most *M*, the
metric g<sub>loc</sub> minimizes the functional ent(g) over the space of all Riemannian metrics on *M*, and in fact *uniquely* minimizes ent(*g*) (up to homothety).
This property would characterize the locally symmetric metric by essentially a single number. The topological component of the conjecture is an
extension of this statement from manifolds to maps.

Conjecture 1 (Entropy Rigidity Conjecture). *Let M be a closed man-*
ifold which admits a locally symmetric Riemannian metric g<sub>loc</sub> with nonpositive sectional curvature. Assume that (M; g<sub>loc</sub>) has no local factors isometric
*to* R*. Let* (*N; g*) *be any closed Riemannian manifold, and let f* : *N ¡! M*
*be any continuous map. Then*

(1)

*with equality if and only if f is homothetic to a Riemannian covering.*

## Remarks:

1. The case when *f* is a homeomorphism, or even the identity map, gives
that g<sub>loc</sub> uniquely minimizes ent(g).

2. Easy examples show that the restrictions to *M* with no local R factors
is necessary.

3. Conjecture 1 easily implies Mostow Rigidity; the argument is the same
as in the case when *M* is negatively curved, which is given in [BCG2].

Conjecture 1 may be extended to a variety of other contexts, for example
to finite volume metrics, Finsler metrics, foliations with locally symmetric
leaves, contact flows, and magnetic flows. To be more precise, the table
below shows some natural choices for the volume and entropy in various
metric settings. In the table we have adopted the following conventions:

*†* represents a contact 1-form

† h<sub>m</sub> is metric entropy, i.e. the measure theoretic entropy for the Liouville measure

† h<sub>top</sub> represents the topological entropy of the geodesic flow

† h<sub>vol</sub> is the volume growth entropy

† dim<sub>H</sub>(Λ(Γ)) is the Hausdorff dimension of the limit set Λ(Γ) of a discrete group Γ of hyperbolic isometries

*† M* = *Y =*Γ

These extensions are discussed in greater depth in Sections 4 and 5.

---

| Setting | Volume Vol( M ) | entropy h ( d ) |
| --- | --- | --- |
| Riemannian metrics on closed M | Riem. volume | h vol R |
| Finite vol. metrics on noncompact M | Riem. volume Z | ¡sd (p;y) inf fs : e dg ( y ) &lt; 1g Y |
| Contact flows | n¡ 1 ^ ( d ) M | h top |
| Finsler metrics | Finsler Volume | h top |
| Magnetic field flows | Euler-Lagrange Volume | h top ¶ Z |
| Foliations on M | d Vol £d Vol( L ): g L leafwise volume £ transverse volume | 1 =n 1 n h ( g ) d Vol L Vol( M ) M |
| Geometrically finite M | Volume of core | dim (Λ(Γ)) H |

Figure 1: Some natural choices for the volume and entropy in different
settings. The functional being minimized is ent := h(d)<sup>n</sup> Vol(M).

## 1.2 Progress

The main evidence for Conjecture 1 is given by the following theorem.

Theorem 2 (Besson-Courtois-Gallot [BCG1]). *Conjecture 1 is true*
when (M; g<sub>loc</sub>) has R-rank one, i.e. when (M; g<sub>loc</sub>) is negatively curved.

This result and its proof have a number of corollaries, including solutions
to long-standing problems on geodesic flows, asymptotic harmonicity, and
Gromov’s Minvol invariant; these are described in [BCG2].

In higher rank very little is known. The following was announced in
[BCG2] and later in [BCG3], and was proved in [CF1] (in the finite volume
case as well).

Theorem 3. Conjecture 1 is true when (M; g<sub>loc</sub>) is locally (but not neces-
*sarily globally) isometric to a product of negatively curved locally symmetric*
*spaces.*

It seems that a significantly new idea is needed to prove Conjecture 1.
See, however, *x*1.4 below.

---

## 1.3 The Besson-Courtois-Gallot map

Building on earlier work of Douady-Earle, Besson-Courtois-Gallot constructed
a remarkable map *F* in every homotopy class of maps *f* : *N!M* from an
arbitrary closed manifold *N* to any closed manifold *M* of negative sectional
curvature. This map is a kind of replacement for, and has several advantages over, the harmonic map in the homotopy class of *f*; in particular, it
can often be differentiated explicitly. The map *F* is a key ingredient in the
proof of Theorem 2.

Now suppose that, in addition to being negatively curved, *M* is also
locally symmetric with metric g<sub>loc</sub>. In this case Besson-Courtois-Gallot were
able to give a precise estimate on the Jacobian *j*Jac *F j*, proving Theorem
2. To state things precisely, it will be useful to fix a parameter *s > h*(*g*),
where *g* is the metric on *N* and *h*(*g*) is the volume growth entropy of *g*.
When (M; g<sub>loc</sub>) has R-rank one, that is when it is negatively curved, Besson-
Courtois-Gallot proved that, given any continuous *f* : *N ¡! M*, there
exists a smooth map F<sub>s</sub>: N ¡! M homotopic to f with the following two
important properties:

Universal Jacobian bound: For all *s > h*(*g*) and all *y 2 N* we have:
¶<sub>n</sub>

(2)

Infinitesimal rigidity: There is equality in equation (2) at the point
y 2 N if and only if D<sub>y</sub>F<sub>s</sub> is a homothety.

Before explaining how to construct such an F<sub>s</sub> (which we do in x2), let
us deduce some consequences of its existence.

The existence of any F<sub>s</sub> satisfying the two properties above implies Conjecture 1 by an elementary degree argument, as follows. Since for *s > h*(*g*),
the map F<sub>s</sub> is a C¹ map, we may simply compute:

---

Letting *s ¡! h*(*g*) gives the inequality in Conjecture 1. In the case when
h(g)
equality is achieved, after scaling the metric g by the constant<sub>)</sub>, we
<sub>h</sub><sub>(</sub><sub>g</sub>*loc*
have h(g) = h(g<sub>loc</sub>) and Vol(N) = jdeg(f)j Vol(M).

## 1.4 The degree theorem

It is useful for us to restate the inequality (1) of the Entropy Rigidity Conjecture as
<u>Vol(</u><u>N</u><u>)</u>

(3)

‡ ·<sub>n</sub>
h(g)
where *C* =. In particular, provin<u>g</u> the inequality (3<u>)</u> with this
<sub>h</sub><sub>(</sub>*g*0)
precise value of C gives that the locally symmetric metric g<sub>loc</sub> minimizes
ent(*g*) among all metrics *g* on *N*.

When the inequality (3) holds for *some* (universal) *C*, perhaps bigger
‡ ·<sub>n</sub>
h(g<u>)</u>
than, then the degree argument given in *x*1.3 gives a universal
h(g0)
bound on the degree of any map of any manifold into *N*. This can be
viewed as the topological part of Conjecture 1. When *N* is negatively curved,
Gromov proved this fundamental relationship between degree and volume
in his paper [Gr] (see his Volume Comparison Theorem).

We note that by *universal* we mean that *C* depends only on the dimension
of the manifolds *M; N* and on their smallest Ricci curvatures. Scaling the
metrics shows that these dependencies are necessary.

When the sectional curvatures of *N* are not necessarily negative but
only nonpositive, the situation is more complicated. Since the *n*-dimensional
torus has flat metrics and also has self-maps of arbitrary degree, one needs at
least to assume that *N* has no local R factors in order that (3) be true. Using
the barycenter technique (see below), we proved the following in [CF2].

Theorem 4 (The Degree Theorem). *Let M be a closed, locally symmet-*
*ric n-manifold with nonpositive sectional curvatures. Assume that M has no*
*local direct factors locally isometric to* R*;*H²*, or* SL₃(R)*=*SO₃(R)*. Then for*
*any closed Riemannian manifold N and any continuous map f* : *N ¡! M,*

*where C >* 0 *depends only on n and the smallest Ricci curvatures of N and*
*M.*

While the “no local R factors” assumption is necessary, we believe that
Theorem 4 should hold in all other cases. The case when *M* is locally modelled on SL<sub>n</sub>(R)=SO<sub>n</sub>(R); n ‚ 2 also follows from work of Savage [Sa];
see *x*1.5 below.

Theorem 4 follows immediately from the degree argument given above
(in *x*1.3) together with the following theorem, which is the main theorem of
[CF2], and which we believe is of independent interest.

Theorem 5 (Universal Jacobian bound). *Any continuous map f* : *N !*
*M between closed n-manifolds, with M nonpositively curved and locally sym-*
*metric (barring the exceptions of Theorem 4), is homotopic to a C¹ map F*
*with*
jJac F j • C

*for some constant C depending only on n and on the smallest Ricci curva-*
*tures of M and N.*

The map *F* is the extension to nonpositively curved locally symmetric
manifolds of the Besson-Courtois-Gallot map; we discuss this below.

As we will discuss in *x*3, the universal bound for *j*Jac *F j* is obtained by
reducing the problem to a minimization problem over a space of measures on
a certain Lie group. The Lie group appears because the natural boundary
attached to symmetric spaces may be described *algebraically*. For general
nonpositively curved manifolds no such description is available. But the
following still seems possible.

Conjecture 6 (Degree Conjecture in nonpositive curvature). *Let M*
*be a closed n-manifold with nonpositive sectional curvature, negative Ricci*
*curvature, and no local* R *factors. Then for any closed Riemannian manifold*
*N and any continuous map f* : *N ¡! M,*

*where C >* 0 *depends only on n and the smallest Ricci curvatures of N and*
*M.*

The evidence for Conjecture 6 is that it is true when *M* has negative
sectional curvature (Gromov [Gr]), and (almost always) when *M* is locally
symmetric (by Theorem 4, since for locally symmetric manifolds of nonpositive sectional curvature, no local R factors implies negative Ricci curvature
). The “negative Ricci curvature” hypothesis in Conjecture 6 is necessary,
as the following example (see [BGS]) shows.

---

Example 7. Let *S* be a negatively curved surface with one boundary component *C*. While keeping *S* nonpositively curved we may smooth a neighborhood of C into a cylinder which is metrically [0; †) £ S<sup>1</sup>, where C is
identified to f0g £ S<sup>1</sup>. Call the resulting surface T.

Now take two copies *X₁* and *X₂* of the manifold *T £ S¹* and glue *X₁* to
*X₂* by identifying [0*; †=*3] *£ S¹ £ S¹ ‰ X₁* and [0*; †=*3] *£ S¹ £ S¹ ‰ X₂* by the
map (*t; x; y*) *7!* (*†=*3 *¡ t; y; x*). The resulting 3-manifold *X* has no flats, but
has some zero curvature at every point and even has an open subset of zero
curvature, namely the subset *Z‰X* formed from the union of the images
of [0; †) £ S¹ in each X<sub>i</sub>.

We note that the two overlapping pieces, (*X₁n Z*) *[* (*†=*2*; †*)*£ S¹£ S¹* and
(X₁ n Z) [ (†=2; †)£ S¹ £ S<sup>1</sup>, each carry an S¹ action that is coherent with a
torus action on *Z* which acts the same in each factor. Therefore, the whole
of *X* carries an *F -structure* in the sense of Cheeger and Gromov [CG]. This
implies via [PaPe, CG] that Minvol(*X*) = 0 (see below for the definition of
Minvol(*X*)); in particular, the conclusion of Conjecture 6 cannot hold for
*X*, even when *f* is the identity map.

Note that *X* has no local direct factors locally isomorphic to R, but that
*X* does have some points with some direction of zero Ricci curvature.

## 1.5 A related conjecture

Gromov has made the following:

Conjecture 8 (Positivity of Gromov norm). *The Gromov norm of a*
*closed, nonpositively curved, locally symmetric manifold M with no local* R
*factors is positive.*

Conjecture 8 was proven by Savage [Sa] when *M* is locally isometric
to SL<sub>n</sub>(R)=SO<sub>n</sub>(R). While we do not see how positivity of Gromov norm
for *M* directly implies the inequality (3), Savage’s proof does imply this
inequality. The key point is that Savage proves that any simplex in *M*
can be “straightened” to a simplex with universally bounded volume. This
should hold for all symmetric spaces of noncompact type, but as far as we
know this is still an open question.

## 1.6 Some consequences of the Degree Theorem

We end this section by recalling some consequences, given in [CF2], of Theorem 4.

---

The Minvol invariant. One of the basic invariants associated to a smooth,
closed manifold *M* is its *minimal volume*:

where *g* ranges over all smooth metrics on *M* and *K*(*g*) denotes the sectional
curvature of *g*. The basic questions about Minvol(*M*) are: for which *M* is
Minvol(*M*) *>* 0? when is Minvol(*M*) realized by some metric *g*?

When a closed, nonpositively curved manifold *M* has a local direct factor
locally isometric to R, then *M* has some finite cover *M⁰* with *S¹* as a direct
factor. This in turn implies that *M⁰* has positive degree self-maps and that
Minvol(M<sup>0</sup>) = 0. On the other hand, in the statement of Theorem 4 we may
take *f* to be the identity map for an *M* which admits a locally symmetric
metric and allow only the metric *g* on *M* to vary. Theorem 4 then shows
Minvol(*M*) *>* 0 for locally symmetric *M*, barring the possible exceptional
cases listed in Theorem 4. However, positivity was already known more
generally, by the following result of Gromov (see also [Sa] for the case of *M*
locally isometric to the symmetric space for SL(*n;* R)).

Corollary 9 (Positivity of Minvol). *Let M be a closed, locally sym-*
*metric manifold with nonpositive curvature and no local* R *factors. Then*
Minvol(*M*) *>* 0*:*

When *M* is real hyperbolic, Besson-Courtois-Gallot [BCG1] proved that
Minvol(*M*) is *uniquely* realized by the locally symmetric metric.

Problem 10. *Compute* Minvol(*M*) *for all closed M which admit a locally*
*symmetric metric of nonpositive curvature, with no local* R *factors. Is*
Minvol(*M*) *always realized by the locally symmetric metric? Is it realized*
*uniquely?*

Self maps and the co-Hopf property. As deg(f<sup>n</sup>) = deg(f)<sup>n</sup>, an
immediate corollary of Theorem 4 is the following.

Corollary 11 (Self maps). *Let M be a closed, locally symmetric manifold*
*as in Theorem 4. Then M admits no self-maps of degree >* 1*. In particular,*
…<sub>1</sub>(M) is co-Hopfian: every injective endomorphism of …<sub>1</sub>(M) is surjective.

Note that Corollary 11 may also be deduced from Margulis’ Superrigidity
theorem (for higher rank *M*). The co-Hopf property for lattices was first
proved by Prasad [Pr].

---

## 2 The Douady-Earle-Besson-Courtois-Gallot map

## 2.1 The construction

In this section we describe the canonical map *F* discussed above. This construction is due to Douady-Earle for the hyperbolic plane, was extended
by Besson-Courtois-Gallot [BCG4] to negatively curved targets, and was
extended to symmetric spaces of noncompact type in [CF1, CF2]. In this
section we will extend this construction further to nonpositively curved targets with negative Ricci curvature. For background on nonpositively curved
manifolds and symmetric spaces, see for example [BGS, Eb].

As above, let *M; N* be closed, Riemannian *n*-manifolds with *M* nonpositively curved, and let *f* : *N ¡! M* be any continuous map. Denote by
*Y* (resp. *X*) the universal cover of *N* (resp. *M*). Denote by *@X* the visual
boundary of *X*; that is, the set of equivalence classes of geodesic rays in *X*,
endowed with the cone topology. Hence *X [ @X* is a compactification of *X*
which is homeomorphic to a closed ball; see, e.g. [BGS].

Idea of the main construction. Let *`* denote the lift to universal
covers of *f* with basepoint *p 2 Y* (resp. *f* (*p*) *2 X*), i.e. *`* = *f*e : *Y ¡! X*.
We first construct a map *F*e : *Y ¡! X* by “averaging” *`* as follows: first
embed *Y* into a space of measures on *Y*, then push forward each measure
via *`*, then smooth out the measure onto *@X* by convolving with a canonical
measure on *@X*, and finally take the “barycenter” of the resulting measure.
An essential feature of each of these steps is that they are *canonical*, i.e.
they are equivariant with respect to the actions of fundamental groups on
each of the spaces involved. It follows from this that *F*e descends to a map
*F* : *N ¡! M*.

Now to define *F*e precisely. Actually, it is useful to fix a parameter *s >*
h(g) for which we define a map Fe<sub>s</sub>. We denote the Riemannian metric and
corresponding volume form on universal cover *Y* by *g* and *dg* respectively.

Let *M*(*Z*) denote the space of probability measures on the set *Z*. Following the method of [BCG1], we define a map Fe<sub>s</sub>: Y ¡! X as a composition

where the individual maps are defined as follows:

---

† The inclusion Y ¡! M(Y), denoted y 7! „<sup>sy</sup>, is given by localizing
the Riemannian volume form *dg* on *Y* and normalizing it to be a
probability measure; that is, „<sup>sy</sup> is the probability measure on Y in the
Lebesgue class with density given by

Note that each „<sup>sy</sup>; y 2 Y is well-defined by the choice of s.

*†* The map *`*<sub>⁄</sub>is the push forward of measures.

† The symbol ~”<sub>z</sub> indicates the operation of convolution with the Patterson-
Sullivan measures f”<sub>x</sub>g<sub>x2X</sub> corresponding to …<sub>1</sub>(M) < Isom(X) (see
*x*2.2). In other words, the resulting measure*ys*is defined on a Borel
set *U ‰ @X* by
Z

Since k”<sub>z</sub>k = 1, we have

† The map bar is the barycenter of the measure <sub>ys</sub>, which is defined as
the unique minimum of a certain functional on *X*, depending on the
measure (see *x*2.3). The map bar is not always defined; when it is
defined its domain of definition often must be restricted.

We now describe the last two maps in more detail. For full details in the
current context we refer the reader to [CF2].

## 2.2 Patterson-Sullivan measures

Let Γ be a discrete group of isometries of a connected, simply-connected,
complete, nonpositively curved manifold *X* with no Euclidean direct factors.
Fix a basepoint *p 2 X*.

Generalizing work of Patterson and Sullivan, a number of authors, including Coornaert, Margulis (unpublished), Albuquerque, and Knieper constructed a remarkable family f”<sub>x</sub>g of probability measures on @X. These
measures, called *Patterson-Sullivan measures*, are meant to encode the density of an orbit Γ *¢ p* at infinity as viewed from *y 2 Y*, giving the Patterson-
Sullivan measure ”<sub>y</sub> on @<sub>1</sub>Y. See [Al] and [Kn] for the construction of
Patterson-Sullivan measures in nonpositive curvature.

---

The key properties of Patterson-Sullivan measures ”<sub>x</sub> are:

1. No atoms: Each ”<sub>x</sub> has no atoms.

2. Equivariance: ”<sub>x</sub> =⁄”<sub>x</sub> for all 2 Γ.

3. Explicit Radon-Nikodym derivative: For all *x; y 2 X*, the measure ”<sub>y</sub> is absolutely continuous with respect to ”<sub>x</sub>. In fact the Radon-
Nikodym derivative is given explicitly by:

(4)

where *B*(*x; y; »*) is the *Busemann function* on *X*. For points *x; y 2 X*
and *» 2 @X*, the function *B* : *X£X£ @X !* R is defined by

where*»*is the unique geodesic ray with (0) = *x* and (*1*) = *»*.

4. Support(Knieper [Kn], Albuquerque [Al]): Each ”<sub>x</sub> is supported on
a specific Γ-orbit in @<sub>1</sub>X.

The importance of property (3) is that it makes possible a reasonably
explicit computation of the Jacobian of the map F<sub>s</sub>; see below.

Property (4) is the most difficult of the properties to prove (see [Al]
for the locally symmetric case and [Kn] for the geometric rank one case).
Its importance is that when *X* is a symmetric space of noncompact type,
the support of each ”<sub>x</sub> lies in a specific copy of the Furstenberg boundary
@<sub>F</sub> X, and thus may be identified algebraically. This allows one to convert
a geometry problem into an algebra problem; see *x*3.1 below.

## 2.3 The barycenter functional

For a probability measure on *@X*, one can try to define its *barycenter*, or
*center of mass*, as follows. One first defines a map

via where *B* is the Busemann function on *X*, based at a fixed basepoint. Since
*X* has nonpositive sectional curvatures, the distance function *d* on *X* is
convex, and hence so is the Busemann function *B*. It follows that for any
fixed measure *‚ 2 M*(*@X*), the function *B*(*¢; ‚*) is a convex function on
*X*. While *B*(*¢; ‚*) is not in general strictly convex (for example when *X* is
Euclidean, it is in many important cases.

Proposition 12 (strict convexity). *Suppose that X has nonpositive sec-*
*tional curvature, negative Ricci curvature uniformly bounded away from* 0*,*
*and no local* R *factors. Let ‚ 2 M*(*@X*) *be a fixed measure. Suppose that*
*either*

*† X is a symmetric space of noncompact type and* supp(*‚*) *is the Fursten-*
*berg boundary of X, or*

*† X has geometric rank one and supp*(*‚*) = *@X.*

*Then the function B*(*¢; ‚*) *is strictly convex on X.*

We note that in both cases of Proposition 12 the hypotheses are satisfied
when *‚* is Patterson-Sullivan measure.

Proof. The case when *X* is a symmetric space of noncompact type is
Proposition 3.1 of [CF2]. Hence we assume that *X* has geometric rank one
and negative Ricci curvature (say bounded by *¡a²*). We also fix a basepoint
*p* for the Busemann function *B* on *X*.

As the Busemann *B* function is convex, the functional
Z

is convex, being an integral of convex functions. We must prove that *B*(*¢; ‚*)
is strictly convex on *X*.

To see this, we first note that while the Hessian of *B*(*¢; p; »*) is only semidefinite for fixed *»*, after taking the integral it becomes positive definite
provided that D<sub>v</sub>d<sub>y</sub>B does not have a common 0 direction w 2 S<sub>y</sub>Y for each
v 2 S<sub>y</sub>Y which lies in the support of ‚. Since the support of ‚ is all of @X,
we must show that the tensors D<sub>v</sub>d<sub>y</sub>B do not have a common zero w.

Now we have the decomposition

where *U* (*v*) is the second fundamental form of the horosphere through *v*.
In particular the Ricatti equations imply that *U* (*v*) is a semi-definite tensor on the subspace of T<sub>y</sub>Y orthogonal to v. Therefore w must lie in < v >
'kerU (v) for all v 2 S<sub>y</sub>Y, or for all v 6= §w we have w¡ < w; v > v 2
ker*U* (*v*).

Consider such a *w 6*= *v*. Let *J*(*t*) be the unique Jacobi field *J*(*t*) along
the geodesic *v*(*t*) with *v⁰*(0) = *v* satisfying *J*(0) = *w* and *J*(*t*) bounded for
all t > 0. Then J also satisfies J<sup>0</sup>(0) = 0, that is J(t) is parallel along v at
*t* = 0. In particular the Ricatti equation then implies that *R*(*v; w; v; w*) = 0.
Since this is true for all v 2 S<sub>y</sub>Y with v 6= w then R<sub>w</sub>:= R(w; ¢; w; ¢) is
the zero tensor, but we assumed that the Ricci curvature trR<sub>w</sub> at w was
nonzero, and we are done. *ƒ*

Note that Example 7 on page 9 shows that the negativity condition on
the Ricci curvature is necessary.

Suppose that *X* satisfies the hypotheses of Proposition 12. Since we also
know that the strictly convex function *B*(*y; ‚*) goes to infinity as *x* goes to
infinity we can define:

We can now define *F*e : *Y ¡! X* by

as described above. From the equivariance properties described above, it follows that Fe is equivariant with respect to the homomorphism f : …<sub>1</sub>(N) ¡!
⁄
…<sub>1</sub>(M), so that Fe descends to a map F : N ¡! M.

## 3 Bounding the Jacobian

The power of the map *F* comes from the fact that one can often obtain
explicit estimates on its Jacobian. As we saw in *x*1.3, such estimates are the
key to all applications of the barycenter method. In this section, we sketch
how estimates on *j*Jac(*F*)*j* have been obtained in some cases.

## 3.1 Existence of some bound

Let = fe („<sup>sx</sup>) ~ ”<sub>x</sub>. Now F<sub>s</sub> is defined by the implicit vector equation:
*ys* ⁄
Z

(5)

---

b
n
PSfrag replacements
bar(„)
„ on @X

Figure 2: The barycenter of a measure.

Differentiating (5) and applying the Implicit Function Theorem then
gives a formula for jJacF<sub>s</sub>j. An application of Ḧolder’s inequality and some
further estimates then give:

(6)

Note that all of this works as long as F<sub>s</sub> is well-defined.

We wish to bound the right hand side of (6). In order to do this we first
convert the problem to a Lie groups problem. This is where we use crucially
the assumption that *M* is locally symmetric. An easy argument allows us to assume that the universal cover of *M* is irreducible, which we now do.

Recall Property (4) of Patterson-Sullivan measures, which states that in
the locally symmetric case, the support of each Patterson-Sullivan is contained in a specific Γ-orbit which may also be identified with the *Furstenberg*
*boundary* corresponding to the Lie group *G* = Isom(*M*f) of isometries of the
symmetric space *M*f. From this one can deduce the following:

Key fact: The expression @<sub>1</sub>X in (6) can be replaced by the maximal
compact subgroup *K‰G* = Isom(*X*).

To further simplify the right hand side of (6), we combine :

*†* Eigenvalue estimates on *DdB*, and

P
† The fact that, for M<sub>i</sub> positive semidefinite, det( M<sub>i</sub>) is a nondecreasing homogeneous polynomial in eigenvalues of the M<sub>i</sub>.

to obtain

(7)

where *I* is the identity matrix of size *n¡*rank(*X*), the matrix *O* is an element
of *K*, and the constant *C* depends only on *n* and on the Ricci curvatures
of *M; N*. We remark that the eigenvalues of *DdB* are determined purely by
algebraic data attached to the Lie algebra of *G*.

The strategy now is to bound the right hand side of (7) *over all probability*
*measures* on *K*. In some sense this is the weakness of the barycenter method:
without knowing additional constraints on the measure <sub>y</sub>, one does not
always obtain a bound as needed to prove Theorem 4, much less Conjecture
1, at least for certain locally symmetric manifolds; such examples which
show that the method can fail are given in *x*6 below.

Some bounds on the right hand side of (7) are possible in most cases,
however; the main technique is called “eigenvalue matching” in [CF2]. The
idea is that for each small eigenvalue in the denominator, one tries to find two
comparably small eigenvalues in the numerator. The hard part is to make
“comparably small” independent of the measure. This involves a detailed
analysis of action of the maximal compact subgroup *K* on subspaces of Lie
algebra of *G* = Isom(*X*) (a simple Lie group). For details see [CF2].

The first basic fact used here is that the kernel of the operator in the
numerator of the right hand side of (7) contains the cokernel of the operator in the denominator. The second main ingredient is the following proposition,
which gives a *K*-invariant subspace perpendicular to *K*-orbit of a flat, and
of twice the dimension of the flat (=rank(*X*)). This fact is precisely where
the hypothesis that *G 6*= SL(3*;*R) is used.

Proposition 13 (Eigenspace matching). *There is a constant C, de-*
pending only on dim X such that for any subspace V ‰ T<sub>x</sub>X with dimV •
rank(*X*) *there is a subspace V⁰ ‰ V<sup>?</sup> of dimension* 2 *¢* dim*V satisfying*

*for all O 2 K.*

## 3.2 The perfect bound in rank one

When *M* has real-rank one, i.e. when *M* is negatively curved, Besson-
Courtois-Gallot are able to obtain the infinitesimal rigidity described on
page 6 (and hence a proof of the entropy rigidity conjecture) because of the
following remarkable phenomenon. It is possible to write the operator in
the denominator of the right hand side of the inequality (7) explicitly in
terms of the operator in the numerator and the complex structure on the
symmetric space; see [BCG2] for details. For example, for the case when
*M* is real-hyperbolic, the denominator operator is the identity minus the
numerator. They are then able to solve the minimization problem explicitly
by using (quite nontrivial) linear algebra.

## 4 Negative results in various settings

In this section we describe in greater detail some negative results in the
settings given in the table on page 5

## 4.1 Finsler metrics

Given a manifold, M, if we equip each tangent space T<sub>x</sub>M with a norm F<sub>x</sub>
which depends smoothly on *x* then this gives rise to a Finsler metric by
taking the distance between two points *x* and *y* to be the infimum of lengths
of curves connecting *x* to *y* where length is measured using the norm on
their tangent vectors. For our purposes we shall assume that the unit ball
in each T<sub>x</sub>M given by the norm is strictly convex with C² boundary. This
is a common assumption since it allows us to form a positive definite inner p
w
k
v
a

Figure 3: Eigenvalue matching.

product, g<sub>u</sub>, for each u 2 T<sub>x</sub>M whose matrix in local coordinates (x<sub>i</sub>; ẋ<sub>i</sub>) for
*T M* is given by entries

As expected, when F comes from a Riemannian inner product then the g<sub>u</sub>
all equal the inner product on T<sub>x</sub>M. The notion of a geodesic flow makes
sense for *F* as it does for the Riemannian case, and therefore we have a
dynamical notion of topological entropy.

Let B<sub>x</sub><sup>F</sup> (R) be the ball of radius R in T<sub>x</sub>M in the norm F. For any
Riemannian metric g on T M we can similarly define B<sub>x</sub><sup>g</sup>(R). Then the volume form for *F* is defined at each point *x* to be,

which is independent of the choice of inner product *g*. In particular, the
quantities Vol<sub>F</sub> (M) and h<sub>Vol</sub>(F) make sense.

For deformations of a single Finsler metric, we can keep *dF* fixed by
simply keeping the Vol<sub>g</sub> B<sub>x</sub><sup>F</sup> (1) fixed for each x relative to a fixed inner
product *g*. Keeping the topological entropy constant as well is more subtle.
P. V´erovic ([Ve]) has shown for any volume-preserving deformation F<sub>t</sub> for
*t 2* (*¡†; †*) of a compact hyperbolic manifold through Finsler metrics where
*F₀* is a hyperbolic Riemannian metric,
fl

For surfaces he shows the same result for deformations which preserve the
Liouville volume of each unit tangent sphere. Moreover, there exist oneparameter families F<sub>t</sub> where topological entropy can be held constant; in
particular the rigidity part of Theorem 2 does not hold when the class of
metrics is extended to Finsler metrics.

In higher rank things get worse: V´erovic also proved in [Ve] that for
compact higher rank symmetric spaces (*M; g₀*), there exists a Finsler metric
F₀ (invariant under all local isometries) with Vol<sub>F</sub><sub>0</sub>(M) = Vol<sub>g</sub><sub>0</sub>(M) and
h<sub>Vol</sub>(F₀) < h<sub>Vol</sub>(g₀); that is, the locally symmetric metric on a higher rank
manifold does *not* minimize normalized entropy among Finsler metrics.

Any invariant Finsler metric is determined by its values on a single maximal flat *A*. In fact, if a is the corresponding maximal abelian subalgebra
and Λ<sup>+</sup> is a set of positive roots fi each with multiplicity m<sub>fi</sub> then F₀ is
given by

for each *H 2* a.

In [BCG3] Besson, Courtois and Gallot asked the following intriguing
question.

Question 14. *Does V´erovic’s Finsler metric F₀ minimize normalized en-*
*tropy among all Finsler metrics?*

---

## 4.2 Magnetic field flows

Let (*M; g*) be a Riemannian manifold, let *…* : *T M ¡! M* be natural projection from the tangent bundle *T M* of *M*. The metric *g* determines an
isomorphism of *T M* with the cotangent bundle; let*!₀* be the symplectic
2-form on *T M* formed by pulling back the canonical symplectic form on
⁄
*T M* by this isomorphism. Now consider any closed 2-form Ω on *M*. Then
for any *‚ ‚* 0 it is easy to verify that

is also a symplectic form on *T M*.

Consider the usual Hamiltonian

and define the *‚-magnetic flow* of the pair (*g;* Ω), denoted *`*<sub>‚</sub>, to be the
Hamiltonian flow of *H* with respect to*!*<sub>‚</sub>. Consider the bundle map *Y* :
*T M ¡! T M* given implicitly by

Then for *v 2 T M* the curve *t 7! `<sup>t‚</sup>* (*v*) = ( (*t*)*;* ˙ (*t*)) is characterized by the
fact that
*r* ˙ (*t*) = *Y* ˙ (*t*)*;*

where r is the connection for the metric g; in particular `<sup>t</sup><sub>0</sub> is just the
geodesic flow for *g*.

Now we consider the case where *M* admits an Anosov geodesic flow. For
instance we could take *M* to be any negatively curved compact manifold. In
[PaPa1] and [PaPa2], G. and M. Paternain show that for Ω 6= 0 the function
h<sub>top</sub>(`‚) is strictly decreasing for ‚ ‚ 0 in the (nonempty) interval containing
*‚* = 0 for which *`*<sub>‚</sub>is an Anosov flow. K. Burns and G. P. Paternain further
show that h<sub>top</sub>(`‚) is decreasing between ”Anosov intervals” (see [BP]). In
this paper the authors also give an example of a higher genus surface *M*,
with a certain choice of Ω, where h<sub>top</sub>(`‚) increases for ‚ in between disjoint
intervals where *`*<sub>‚</sub>is Anosov. Therefore, while metrics corresponding to
local maxima and minima for h<sub>top</sub>(`‚) may be special, no standard entropy
rigidity exists for such flows.

---

## 4.3 Metric entropy

Lastly, we mention the work of L. Flaminio in [Fl]. The *metric entropy* is
the measure-theoretic entropy of the Liouville measure on the unit tangent
bundle of *M*. The measure-theoretic entropy of the Bowen-Margulis measure is the same as the topological entropy, which in turn is the same as
the volume entropy. Hence for hyperbolic metrics, for instance, the metric
entropy and volume entropy coincide. In general the topological entropy is
always greater than or equal to the metric entropy. Flaminio shows that the
metric entropy for volume preserving deformations of a hyperbolic metric
on a 3-manifold *M* does not have a local maximum at the hyperbolic metric.
This is in contrast to the two dimensional case where A. Katok [Ka] showed
that the metric entropy does have a local maximum there.

## 5 Positive results in various settings

In this section we describe some known cases where a locally symmetric
metric structure minimizes *h*(*g*) for a suitable normalization.

## 5.1 Finsler metrics

Recall the definition of a Finsler metric given above. We call a Finsler metric
*F reversible* if it satisfies *F* (*¡v*) = *F* (*v*) for all *v 2 T M*. Moreover we define
an *eccentricity factor N*(*F*) for a Finsler metric *F* on a manifold *X* to be

where S<sub>x</sub><sup>F</sup> (1) and S<sub>x</sub><sup>g</sup><sup>u</sup>(1) are the unit spheres in the norms F and g<sub>u</sub> respectively. For this setting we redefine the volume entropy functional ent to
be
ent(F) := N (F)h(F)<sup>n</sup> Vol (X)

where *n* is the dimension of *X*.

To each direction in T<sub>x</sub>X we may ascribe a Riemannian metric, and
consider the corresponding curvature tensor. These are the flag curvatures
(see [BaCS]). With this notation, J. Boland and F. Newberger [BN] proved
the following theorem.

Theorem 15 (Finsler entropy rigidity). *Let* (*X; g₀*) *be a compact, n-*
*dimensional, locally symmetric Riemannian manifold of negative curvature*

---

(*n ‚* 3) *and* (*Y; F*) *a compact, reversible, Finsler manifold of negative flag*
*curvature that is homotopy equivalent to* (*X; g₀*)*. Then*

*with equality if and only if F is homothetic to g₀*

Notice that if *F* is Riemannian then *N* (*F*) = *N* (*g₀*)=1 and so this
reduces to the usual entropy rigidity theorem for the case of maps homotopic
to the identity.

## 5.2 Foliations

Let *N* and *M* be compact topological manifolds supporting continuous foliations *FN* and *FM* by leaves which are smooth Riemannian manifolds,
and such that the metrics on the leaves vary continuously in the transverse
direction. We suppose that the leaves of *FM* are locally isometric to *n*-
dimensional symmetric spaces of negative curvature, *n ‚* 3; by continuity
of the metrics these are all locally homothetic to a fixed symmetric space
(X; g e <sub>o</sub>).

For any leaf (L; g<sub>L</sub>), we may define

where *B*(*x; R*) is the ball of radius *R* in the universal cover *L*e of *L*. Similarly
we can define h(g<sub>L</sub>) using the lim infR¡!1. These numbers do not depend
on the choice of x. We then define the volume growth entropy h(g<sub>L</sub>) to be
‰ flZ

where *S*(*x; t*) is the sphere of radius *t* about *x* in the universal cover *L*e of
*L*. This quantity is independent of *x 2 L*. Hence we can define a function
f : N ¡! [0; 1] by letting f (x) be h(g<sub>L</sub>) for the leaf L containing x. Of
course *f* is constant on each leaf.

The function *f* is also measurable. This follows from the fact that the
transverse continuity of the leafwise metrics implies that for each *R*, the
function
Z
R is continuous on *N*. On (*M; FM*) the entropy is constant and we denote it
by h(g<sub>o</sub>). From the definition of h(g<sub>L</sub>) it follows almost immediately that

For the foliation (N; FN) we assume that the leaves (L; g<sub>L</sub>) are strictly
negatively curved, and satisfy the stronger condition that for all *x; y 2 L*
there is a – < h(g<sub>L</sub>) such that

(8)

where *S*(*x; R*) is the sphere of radius *R* in *L*. Such a leaf will be called a
*Patterson-Sullivan manifold*.

Finally, assume we have a leaf-preserving homeomorphism

which is leafwise *C¹* with transversally continuous leafwise derivatives, but
not necessarily transversally differentiable. Equip the foliation (*N; FN*) with
any choice of finite, transverse, holonomy quasi-invariant measure *”* (see
Hurder [Hu] or Zimmer [Zi] for the definition and existence). Holonomy
quasi-invariance simply means that the push forward of *”* under any holonomy map is in the same measure class as *”*. This measure *”* provides us
with a global finite measure „<sub>N</sub> on N which is locally a product of ” with
the Riemannian volumes dvol<sub>L</sub> of the leaves L. In this setting J. Boland
and the first author ([BC]) showed the following.

Theorem 16 (Foliated entropy rigidity, I). *Let* (*N; FN*) *be a contin-*
*uous foliation of the compact manifold N such that ”-almost every leaf is*
*a Patterson-Sullivan manifold. Suppose that f* : (*N; FN*) *¡!* (*M; FM*) *is*
*a foliation-preserving homeomorphism, leafwise C¹ with transversally con-*
*tinuous leafwise derivatives, and that f*<sub>⁄</sub>*”-almost every leaf of* (*M; FM*) *is*
a rank one locally symmetric space. Then there exists a finite measure „<sub>M</sub>
on M which is locally the product of dvol<sub>o</sub> with a transverse quasi-invariant
measure ”<sub>o</sub> such that
Z Z

and equality holds if and only if ”-almost every leaf (L; g<sub>L</sub>) is homothetic to
its image (f (L); g<sub>o</sub>).

---

When the foliation admits a holonomy-invariant measure *”* then we may
take ”<sub>o</sub> = f⁄”. When ” is just holonomy quasi-invariant however, then ”<sub>o</sub> is
the push forward of *”* under the natural map *F* defined below.

When the foliation (*N; FN*) is ergodic with respect to *”*, then the entropy
function h(g<sub>L</sub>) = h(g) is constant on N, and we get the following (see [BC]).

Corollary 17 (Foliated entropy rigidity, II). *Under the same assump-*
tions as in the main theorem, if (N; FN) is ergodic, then h(g<sub>o</sub>)<sup>n</sup> Vol(M; „M) •
h(g)<sup>n</sup> Vol(N; „N) with equality if and only if ”-almost every leaf (L; g<sub>L</sub>) is
homothetic to (f (L); g<sub>o</sub>).

Remark. If (*N; FN*) and (*M; FM*) are foliations such that almost every leaf
is compact or simply connected, then the requirement that the homeomorphism *f* be leafwise *C¹* can be dropped. In particular if the foliations have
just one leaf and dim *N 6*= 3*;*4, any homotopy equivalence induces a homeomorphism between *N* and *M* (see [FJ]). Therefore, when dim*N* 6= 3*;*4,
Corollary 17 recovers Theorem 2.

Of course one can also ask for foliated versions of Conjecture 1 as well.

## 5.3 Finite volume manifolds

For the case of finite volume manifolds J. Boland, J. Souto and the second
author showed the following analogue of the Real Schwarz Lemma.

Theorem 18 (Volume Theorem [BCS]). Let (M; g) and (M<sub>o</sub>; g<sub>o</sub>) be two
*oriented complete finite volume Riemannian manifolds of the same dimen-*
*sion n ‚* 3 *and suppose that*

Then for all proper continuous maps f : M ¡! M<sub>o</sub>,

and equality holds if and only if M and M<sub>o</sub> are hyperbolic and f is proper
*homotopic to a Riemannian covering.*

When M and M<sub>o</sub> are compact, Theorem 18 follows from a real Schwarz
lemma proved by Besson, Courtois, and Gallot in [BCG5]. As in the case of
all noncompact situations, to apply the method of [BCG1] and [BCG5], the
fundamental difficulty is proving the properness of the natural map.

Theorem 18 implies the following.

---

Corollary 19. *Under the hypotheses of Theorem 18,*

Now restrict *f* to be degree 1, and consider what happens when Minvol(*M*) =
Vol(M<sub>o</sub>): Bessi`eres proved in [Be1] that if there is a degree 1 map f : M ¡!
M<sub>o</sub> from the compact n-dimensional M to the compact n-dimensional real
hyperbolic manifold M<sub>o</sub> such that Minvol(M) = Vol(M<sub>o</sub>), then M and M<sub>o</sub>
are diffeomorphic. He also gave examples in [Be2] of a finite volume manifold
M with the same simplicial volume as a hyperbolic manifold M<sub>o</sub> such that
there is a degree 1 map from M to M<sub>o</sub> and Minvol(M) • Vol(M<sub>o</sub>) but M
and M<sub>o</sub> are not even homeomorphic. By the above corollary, Minvol(M) =
Vol(M<sub>o</sub>). Despite such examples, our next result ([BCS]) shows that the
pointed Lipschitz limit of some subsequence of any sequence of metrics whose
volumes achieve Minvol(M) is isometric to M<sub>o</sub>.

Theorem 20 (Hyperbolic Minvol rigidity, finite volume case). *Let*
M and M<sub>o</sub> be finite volume manifolds of the same dimension n ‚ 3, M<sub>o</sub>
real hyperbolic, and f : M ¡! M<sub>o</sub> a continuous, proper, degree 1 map. If
Minvol(M) = Vol(M<sub>o</sub>), then for any sequence of metrics g<sub>i</sub> realizing the
minimal volume of M, there are p<sub>i</sub> 2 M and a subsequence g<sub>i</sub>jsuch that
(M; p<sub>i</sub><sub>j</sub>; g<sub>i</sub><sub>j</sub>) converges in the pointed Lipschitz topology to a Riemannian
manifold isometric to M<sub>o</sub>.

In particular, the topology of the limit manifold changes to that of M<sub>o</sub>.
The last main result of [BCS] is the finite volume version of the entropy
rigidity result found in [BCG1].

Theorem 21 (Rank one entropy rigidity, finite volume case). *Let*
(*M; g*) *be an n-dimensional finite volume manifold of nonpositive sectional*
curvature, n ‚ 3, and h(g) its volume growth entropy. Let (M<sub>o</sub>; g<sub>o</sub>) be an
n-dimensional finite volume rank one locally symmetric manifold and h(g<sub>o</sub>)
its volume growth entropy. If f : M ¡! M<sub>o</sub> is a continuous, proper map of
*degree* deg(*f*) *>* 0*, then*

*and equality holds if and only if f is proper homotopic to a Riemannian*
*covering.*

As in [BCG2], this gives a quick proof of the Mostow rigidity theorem
for finite volume negatively curved locally symmetric manifolds.

---

## 5.4 Quasifuchsian representations

The barycenter method has recently been applied by Besson-Courtois-Gallot
[BCG5] to convex cocompact (infinite covolume) representations, generalizing Bowen’s rigidity theorem about quasifuchsian groups. We now describe
one of the several results in [BCG5] along these lines.

Let *X* be a negatively curved manifold. A faithful representation *‰* :
Γ *¡!* Isom(*X*) is *convex cocompact* if *‰*(Γ) acts cocompactly on the convex
hull of its limit set Λ(*‰*(Γ)). Attached to each *‰* is a number, namely the
Hausdorff dimension dim<sub>H</sub>(‰(Λ(Γ))). Amazingly, this single number can be
used to characterize the *totally geodesic* representations, i.e. those representations leaving invariant a totally geodesic submanifold. The following
theorem was originally proved by Pansu, Bourdon, and Yue, generalizing
an earlier theorem of Bowen. Besson-Courtois-Gallot gave another proof in
[BCG5] using the barycenter method.

Theorem 22 (Quasifuchsian rigidity). *Let* Γ *be the fundamental group of*
*a closed, hyperbolic n-manifold, and let X be a connected, simply-connected*
*manifold with sectional curvature • ¡*1*. Then*

*with equality if and only if ‰ is totally geodesic.*

There is also a version for complex hyperbolic manifolds (see [BCG5]).
The idea of the proof is to define the barycenter map as we discussed above,
and to bound the Jacobian of this map; Theorem 22 then follows reasonably
quickly. The main difficulty is that the dimensions of the domain and target
spaces are different. To repair this one notes that *‰* gives a quasi-isometric
embedding between negatively curved spaces, hence a homeomorphic embedding of one boundary at infinity into another. The general technique
can then be carried out once one finds the right notion of volume.

## 5.5 Alexandroff Spaces

In this section we report on recent work of P. Storm, who extended some
of the results of [BCG1] to certain Alexandroff space domains within the
same bilipschitz class as a fixed hyperbolic manifold. All of the results can
be found in [St].

In brief, an Alexandroff space *X* with curvature bounded below by *¡*1
is any complete, locally compact metric space of finite Hausdorff dimension,
such that every point *x 2 X* has a neighborhood containing a geodesic triangle such that the comparison triangle in H² with the same side lengths
has the property that the distance form any vertex of the triangle to any
point on the opposite side is shorter than the corresponding distance on the
triangle in *X*. Storm’s main result in [St] is the following.

Theorem 23 (Alexandroff domain). *Let* (*X; d*) *be an Alexandroff space*
*with curvature bounded below by ¡*1*, and Y a closed, hyperbolic n-manifold,*
*n ‚* 3*. If there is a bilipschitz homeomorphism between X and Y, then*

The proof of this theorem is at first glance unrelated to the method
of Besson, Courtois, and Gallot as outlined in the opening sections of this
paper. Nevertheless, it is actually of the same vein. The main technique is
to extend the idea of *Spherical Volume* as presented in [BCG1] to this new
setting. Instead of going through the (perhaps insurmountable) difficulty of
forming a barycenter map from *X* to *Y*, one can in a sense stop “half-way”
and attempt to do the analysis in *M*(*X*) and *M*(*Y*). Since the embedding
via measures is in essence an *L¹* approach it is preferable to modify this to
an *L²* approach which leaves us working in a Hilbert space.

More precisely, one embeds Xe into L²(Xe) in a …<sub>1</sub>-equivariant way via
the map
s=2d(x;¢)
Φ (*x*) := *e*

for any s > h(X), and then projects this to the unit Hilbert sphere S<sup>1</sup>(Xe).
We recall that this is the embedding achieved by using the square root of
the Radon-Nikodym derivatives of the un-normalized <sub>ys</sub>, which are in L² by
definition of the volume growth entropy *h*(*X*). If *f* : *Y*e *¡! X*e represents a
bilipschitz …<sub>1</sub>-equivariant map given by the hypotheses of the theorem, then
the map
*I*e : *L₂*(*X*e) *¡! L₂*(*Y*e)

given by

is a …<sub>1</sub>-equivariant isometry. Hence it restricts to I : S¹Xe ¡! S¹Ye. The
composition
Fe := I – Φ – f : Ye ¡! S¹Ye

descends to a map F : Y ¡! S<sup>1</sup>(Y) with image in the positive orthant.

For such maps there is a notion of volume, and without defining it, we
simply point out that spherical volume is the infimum of the volume of such maps. In particular

The last equality was proven by Besson-Courtois-Gallot in [BCG1].

Since Alexandroff spaces are in a sense Riemannian manifolds off of a
measure zero set, and *Y* is a Riemannian manifold, Storm can use standard
integration theory. Of course we now come to the difficult (and omitted)
part of the proof of Theorem 23, which is to show
¶

It then follows that

The final step is to apply a result of Burago-Gromov-Perel’man which states
that for Alexandroff spaces with curvature bounded below by *¡*1, *h*(*X*) *•*
*n ¡* 1; Theorem 23 then follows.

The main applications of Theorem 23 are to two important classes of
Alexandroff spaces which arise naturally in the study of hyperbolic manifolds: doublings of convex cores and cone manifolds.

## 5.5.1 Convex Cores

The *(metric) double DCM* of the convex core *CM* of a convex cocompact
manifold *M* is the result of identifying the boundaries of two copies of *CM*
and then extending the induced metric on each copy of *CM* to the whole.
While as a topological manifold *DCM* can always be smoothed (e.g. by
taking the double a neighborhood of *CM*), the point is that any Riemannian
metric on the resulting smooth manifold cannot agree with the metric on
each copy of *CM* as a subspace, unless these had totally geodesic boundaries
to begin with. On the other hand, *DCM* naturally carries the structure of
an Alexandroff space with Alexandroff curvature bounded below by *¡*1 and
Theorem 23 applies.

Let CC(*N*) be the space of complete convex cocompact hyperbolic manifolds diffeomorphic to the *interior* of smooth compact *n*-manifold *N*. In
analogy with the volume entropy results discussed in this paper, one wants
to know that the topological invariant is minimized for certain special hyperbolic manifolds.

It is consequence of Thurston’s work together with Mostow Rigidity that
a 3-manifold *N* is acylindrical if and only if there exists unique *M₀ 2* CC(*N*)
such that *@CM₀* is totally geodesic (see [Th2]). Combining this with Theorem
23, Storm obtains the following.

Corollary 24.*. Let N be an acylindrical compact irreducible* 3*-manifold*
*such that CC*(*N*) *is nonempty. Then there exists a unique M₀ 2 CC*(*N*)
*such that V*(*N*) = *Vol*(*CM₀*)*. Moreover, @CM₀ is totally geodesic.*

In fact he shows that any *CM₀* with totally geodesic boundary is the
unique minimizer of Vol(*CN*) among hyperbolic *N* homotopy equivalent to
*M₀*. (Note we are using that *M₀* is tame). We should also mention that
Bonahon had previously shown in [Bon] that *M₀* is a strict local minimum
of Vol(*CN*).

Remark. Storm is able to also obtain results giving exact relations between the Gromov norm of such *DCN* and covers in terms of *V*(*N*).

## 5.5.2 Application to Cone Manifolds

Theorem 23 may also be applied to cone-manifolds with all cone angles *•* 2*…*.

Definition ([CHK], page 53). An *n-dimensional cone-manifold* is a topological manifold, *M*, which admits a triangulation giving it the structure of
a PL manifold and *M* is equipped with a complete path metric such that the
restriction of the metric to each simplex is isometric to a geodesic simplex
of constant curvature *K*. The singular locus Σ consists of the points with
no neighborhood isometric to a ball in a Riemannian manifold.

It follows that

*† Sigma* is a union of totally geodesic closed simplices of dimension *n¡*2.

*†* At each point of Σ in an open (*n ¡* 2)-simplex, there is a *cone angle*
which is the sum of dihedral angles of *n*-simplices containing the point.

Notice that cone-manifolds whose singular locus has vertices are allowed.

Lemma 25 ([BGP], page 7). *If all cone angles of n-dimensional cone-*
*manifold M are •* 2*…, and K ‚ ¡*1*, then M is an Alexandroff space with*
*curvature bounded below by ¡*1*.*

---

An *n*-dimensional cone-manifold clearly has Hausdorff dimension *n*. Therefore Theorem 23 implies the following.

Corollary 26. *Let M be an* 3*-dimensional cone-manifold with all cone an-*
*gles •* 2*… and K ‚ ¡*1*. Let M₀ be a closed hyperbolic* 3*-manifold. If M and*
*M₀ are homeomorphic then*

All of these corollaries have only slightly weaker generalizations to any
dimension greater than 2. We refer the reader to [St]. There are other
results whose methods follow along these lines; in particular we would like
to point out the work relating to Einstein metrics, the Gromov norm, and
simplicial volume for manifolds and covers carried out by A. Sambusetti
(e.g. [Sam1, Sam2]). However, these recent results have already been well
surveyed in [BCG5].

## 6 Cautionary examples

Our proof in [CF2] of the Degree Theorem (Theorem 4) can be viewed as
a step towards the Entropy Rigidity Conjecture (Conjecture 1), or at least
the inequality of that conjecture; to do this one “only” needs to prove the
‡ ·<sub>n</sub>
h(g)
inequality (3) on page 7 with the lowest possible *C*, namely *C* =.
h(g0)

While the value of *C* which comes out of the proof (see [CF2]) of inequality (3) can be explicitly computed, finding the best *C* seems much harder. In
fact, it soon became clear to us that the barycenter method applied without
*a priori* constraints on the types of measures considered is not sufficiently
precise to obtain the rigidity aspect of the theory, or even to prove that
the locally symmetric metric minimizes entropy. In this section we describe
some explicit examples which demonstrate some of the problems.

The Jacobian estimates on the Besson-Courtois-Gallot map *F* are obtained by bounding the right hand side of (7), that is, bounding
¶ ¶

independently of the measure. In other words, no special property of the
measure d<sub>y</sub> is used. This is also the case in the proof of Entropy Rigidity
in rank one (see [BCG2]).

---

We recall that in a symmetric space of noncompact type, the Furstenberg
boundary is the space of Hausdorff equivalence classes of (maximal) Weyl
chambers; this space can be identified with *G=P*, where *P* is a minimal
parabolic subgroup of *G*. This in turn is naturally homeomorphic to *K=M*
where *K* is the maximal compact subgroup of *G* and *M* is the centralizer
of a in K. Since K is isomorphic to K<sub>p</sub>, isotropy subgroup of p 2 X, and
M is isomorphic to M<sub>p</sub>, the centralizer of a Weyl chamber in F<sub>p</sub>, we may
interpret the Furstenberg boundary geometrically. Namely it is naturally
identified to any G-orbit of a regular point in @X. We will denote by @<sub>F</sub> X
the particular orbit of the point at infinity corresponding to the normalized
barycenter b<sup>+</sup> of positive root vectors. By the above, @<sub>F</sub> X projects to the
unit tangent sphere S<sub>p</sub>X as the orbit of b<sup>+</sup> by K<sub>p</sub>.

Hence if we write *J*(*„*) for the square of the right hand side of the
expression (6) with*ys*replaced by *„*, then we would like for it to be uniquely
maximized when *„* is the projection of Haar measure on *K*. Here we only
care about maximizing over the space of M<sub>p</sub>-invariant „ supported on K<sub>p</sub>.

## 6.1 An example in H² £ H²

In the case of X = H² £ H² the Furstenberg boundary @<sub>F</sub> X is simply the
torus S¹ £ S<sup>1</sup>. We will parameterize this by (e<sup>it</sup><sup>1</sup>; e<sup>it</sup><sup>2</sup>). Let M be a compact
quotient of *X* and let *f* : *M ¡! M* a continuous map. We first consider the
case *f* = Id and the simple two-parameter family of probability measures
„<sub>a;b</sub> for a; b > 0 on @<sub>F</sub> X given by

where „<sub>0</sub> the unit Haar measure on the torus. Note that „<sub>0;0</sub> is Haar measure. For this family, by integrating over the torus we can compute the
expression for
*J₀*(*„*) := *J*(*„*)*=J*(Haar)

to be

Note that the measures „<sub>0;b</sub> are distinct, but that J(„<sub>0;b</sub>)=J(„<sub>0;0</sub>) = 1
identically. In particular the Haar measure does not uniquely minimize this
quantity. This may not be that surprising in light of the fact that H² does
not have a unique minimizer either, nor is there a entropy rigidity theorem
for *X*, at least not for reducible lattices.

---

1
0.9
20
JHmL
0.8
0.7
15
0.6
00 10
b
22
PSfrag replacements 44
5
J(„<sub>a;b</sub>) 66
aa
88
10 100

Figure 4: Graph of J(„<sub>a;b</sub>)=J(Haar) for several values of a and b.

## 6.2 An example in SL₃(R)=SO₃(R)

Now we examine the case of *X* = SL(3*;*R)*=*SO(3). Suppose for a single flat
F<sub>x</sub> and a sequence of y<sub>i</sub> 2 F<sub>x</sub>, the measuresystend to the sum of Dirac
*i*
measures
<u>1</u> X

where the b<sup>+</sup><sub>i</sub> are all the images of b<sup>+</sup> under the Weyl group in F<sub>x</sub>. Hence
there is one atom for each Weyl chamber at *x* and they are symmetrically
placed making *x* the barycenter of *„*. Then we claim that if *N* = *M* and *f*e
induces the identity map on @F<sub>x</sub> then JacF<sub>s</sub>(y<sub>i</sub>) ¡! 1.

The hypotheses that N = M and that fe is identity on @F<sub>x</sub>, which
contains the support of „, implies that JacF<sub>s</sub>(y<sub>i</sub>) is identical in the limit
*i ¡! 1* to the estimate on the right-hand side of (6) with*ys*replaced by
*„*. Therefore it remains to show that this right-hand side is unbounded.

---

First note that the sum

has only a 3-dimensional kernel, while

has a 2-dimensional kernel. Furthermore the numerator and denominator
Z Z

degenerate homogeneously. In particular, the quantity det(*Q₁*)*=*det(*Q₂*)² is
unbounded. This can be easily verified explicitly in the case of a sum of
eight Dirac measures for which both integrals are nonsingular degenerating
to the sum of the six Dirac measures given above.

## 6.3 An example in SL₄(R)=SO₄(R)

In the case when *X* = SL(4*;*R)*=*SO(4), Theorem 4 holds and the quantity
(6) is bounded independently of <sub>ys</sub>. Nevertheless, here we present a smooth
(with respect to Haar) probability measure *„* on SO(4)*=M* such that *J₀*(*„*)
is strictly larger than 1. In fact, „ will be very close to the Haar measure „<sub>0</sub>
only differing by the addition of a few very small and sharp “thorns” and
removal of a few “drillings.” What we mean by this will become evident
from the final construction.

Our procedure is to consider second derivatives of the Jacobian
¶

with respect to a parameter *t* where *„* is an arbitrary signed measure. In
fact, if we can find such a *„* for which the second derivative at zero is positive
then we will show how one can obtain such an example where *„* is a smooth
(with respect to „<sub>0</sub>) positive probability measure.

One can verify directly that, for general *X*, which for SL(4*;*R) works out to be

Hence, after clearing the denominator of the measures, we can rewrite
‡ ·

Taking the derivative of the log we have

Hence the second derivative is
h

For an invertible matrix *M* we have the operator identities

Applying these identities we directly obtain

Similarly,

Since *f*(0) = 1 and we see that @<sub>t</sub>j<sub>t</sub>=0f (t) = 0 and

Now we consider the Cartan splitting SL(4*;*R)*=K* = *KP* where *P* are the
positive definite symmetric matrices with determinant 1 and we identify *K*
with the stabilizer of F<sub>s</sub>(y). P is naturally identified with the 9-dimensional
subspace p of traceless symmetric matrices in sl(4*;*R). We also have the
natural representation of *K* in SO(p) induced by the action of *K* on *P* by
conjugation.

By lifting @<sub>F</sub> X to K we may treat the integration over K and it is convenient to parameterize *K* by R⁶ *·* s the subalgebra of skew-symmetric
matrices in sl(4*;*R). We can choose a domain of integration *D ‰* R⁶,
and integrate over this space. For *2 D* let O() *2* SO(p) be the corresponding element. If *A* is the constant diagonal matrix with diagonal
(1*;* 0*;* 0*;* 0*;* 0*;* 0*;* 0*;* 0*;*0) and *B* is the diagonal matrix with diagonal
r r r r r r

then relative to the appropriate choice of coordinates on TF<sub>s</sub><sub>(y)</sub>X we may
write
*dB* = *O*( )*AO*( )<sup>⁄</sup>

and

p1
Note that the metric we are using is times the one most commonly used
2
by re*p*resentation theorists.

With these notations, the expression above for @<sub>t</sub>@<sub>t</sub>j<sub>t</sub>=0f (t) becomes
Z Z

where

In particular, we may treat @<sub>t</sub>@<sub>t</sub>j<sub>t</sub>=0f (t) as a symmetric 2-form Ω(¢; ¢) on
the space of signed measures.

---

¡
In fact, the function q is equivariant, so q(; ¿) can be written as g(<sup>1</sup>¿) :=
¡ ¡
q(1; <sup>1</sup>¿) and one can easily check that g() = g(<sup>1</sup>).

Three representative graphs of *g*() over two-parameter subspaces spanned
by (respectively) *e₁* and *e₂*, *e₃* and *e₄*, and *e₅* and *e₆*, are given below. We see
that the function is mostly negative but there are smaller positive regions
as well.

0
J
-10
2
-20
0
t
-2-2
00
-2
ss
22

Figure 5: Graph of *g*(*se₁* + *te₂*)

Now we can take „<sub>1</sub> to be the sum of the atomic measures at the 55 points
of @<sub>F</sub> X corresponding to the following rational parameters in D. Namely
the points are of the form K<sub>i</sub> ¢ b<sup>+</sup> where b<sup>+</sup> is the barycenter of a set of
positive roots (note that any two choices will produce equivalent measures
differing by a push forward by an isometry in the Weyl group) and that K<sub>i</sub>
is the element of K h SO(4) acting on b<sup>+</sup> by conjugation corresponding to
the element 0 1
0 *s*1 *s*4 *s*6

*p p*
For example, one such choice for b<sup>+</sup> has coordinates (2= 5; 1= 5;0) in the

---

10
0
J
-10
2
-20
0
t
-2-2
00
-2
ss
22

Figure 6: Graph of *g*(*se₃* + *te₄*)

canonical flat with the most common choice of coordinates in *SL*(4). The
corresponding values of the s₁; : : : ; s₆ for K<sub>i</sub> may be read across the i-th row
from the following table:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| (-2.1763 | -1.1507 | -2.04369 | 0.44192 | 0.348006 | -0.0873793) |
| (1.10122 | -1.30303 | -1.07559 | 1.69668 | -0.537171 | -0.790495) |
| (-2.66081 | -2.51729 | 0.874064 | 0.0170786 | 2.76331 | 0.918491) |
| (3.06666 | -1.20383 | 3.10876 | -1.8274 | 1.33181 | 1.36971) |
| (2.14346 | 2.46489 | 0.233902 | -2.2138 | -1.34613 | -0.589322) |
| (2.27427 | 2.23082 | 2.87105 | 0.855587 | -0.33015 | -0.120273) |
| (2.39027 | 0.231281 | 1.93738 | 3.00424 | 2.76855 | 2.45438) |
| (2.01231 | 1.06647 | 2.80138 | 1.14019 | -2.46108 | 2.83835) |
| (-2.48367 | 1.81689 | 0.446606 | 1.91056 | 2.00405 | -0.735379) |
| (1.31393 | 2.82133 | 2.2746 | 1.55063 | -1.49752 | -0.199991) |
| (3.02592 | -1.82225 | -0.293302 | -0.0626386 | -2.88422 | -1.13504) |
| (0.835977 | 2.01248 | -2.54401 | 0.866367 | 0.15547 | 2.31572) |
| (3.08126 | 2.19107 | 2.85046 | -2.73643 | -2.06439 | -0.215145) |
| (-1.60506 | -2.41617 | -1.19739 | 1.37582 | 3.03405 | 0.925416) |
| (-1.08172 | 0.0564745 | 0.185755 | -2.15354 | -1.3391 | -1.95008) |
| (2.49137 | -1.02443 | -1.93669 | 0.325143 | -0.805692 | -0.198555) |
| (-1.87635 | 1.27567 | -0.514556 | -0.603716 | -2.95356 | -1.65078) |
| (-2.05109 | -1.32914 | 1.38543 | 0.114991 | -1.94354 | 0.887035) |
| (-0.674438 | -3.08308 | 1.0123 | -0.10102 | -2.47693 | 2.0086) |
| (1.66252 | -2.21819 | 2.60135 | -1.45814 | -0.67338 | 1.12196) |
| (1.33611 | 0.407789 | 2.98277 | -1.41592 | 1.14807 | -1.08302) |
| (1.89226 | 3.05482 | 2.90424 | 1.94358 | 0.694209 | -0.973808) |
| (0.437082 | 1.88506 | 2.8235 | 2.26881 | -0.227581 | 3.01805) |
| (-1.98061 | 1.3454 | 0.31266 | 1.3346 | 1.83436 | -2.91815) |
| (2.11814 | -2.21478 | 1.99318 | 1.63935 | -2.17152 | 2.00983) |
| (-3.04067 | 1.72613 | -1.93417 | -3.07534 | -0.593287 | -0.441659) |

---

| J | t | s |
| --- | --- | --- |
| 0 | 0 | -2 |
| -10 | 0 | -2 |
| -20 | 0 | -2 |
| -30 | 0 | -2 |

Figure 7: Graph of *g*(*se₅* + *te₆*)

|  | -1.81881 | -0.275197 | 0.431129 | -2.14367 | -1.69527) |
| --- | --- | --- | --- | --- | --- |
| (0.770342 | -1.81881 | -0.275197 | 0.431129 | -2.14367 | -1.69527) |
| (-1.43618 | 2.22732 | 0.685263 | 0.111728 | -0.128947 | 2.00388) |
| (1.70871 | -0.815082 | 1.01946 | -2.77706 | 0.738644 | 0.316677) |
| (0.918539 | -1.36159 | -0.46878 | 0.250422 | -1.62977 | 2.22166) |
| (1.90247 | -1.07237 | 1.78702 | -1.35106 | 0.904547 | -2.51869) |
| (0.0816078 | -0.436794 | -2.92231 | 0.511173 | -2.93104 | 0.700914) |
| (-1.48943 | -1.81534 | -0.808906 | 0.336383 | 0.913519 | 1.00958) |
| (1.41415 | -1.44362 | -1.75929 | -2.38244 | -0.0976769 | -0.52368) |
| (-0.520171 | 1.83152 | 1.25689 | -2.31421 | 1.71687 | 1.20862) |
| (-1.96631 | 1.26418 | 1.49759 | -2.44414 | -2.17686 | -2.57833) |
| (-0.154573 | 2.51279 | 1.77364 | 0.226881 | 2.0735 | -1.63838) |
| (-2.7821 | -1.4711 | 0.6912 | -2.39754 | 0.457165 | 2.19418) |
| (-1.93022 | -1.08747 | 2.34186 | 1.36679 | -0.505503 | 0.8455) |
| (1.16658 | -3.03898 | 1.1385 | 0.148052 | 0.201847 | 2.68094) |
| (-1.84852 | 0.776858 | 1.5698 | -0.687528 | -0.780427 | -0.72635) |
| (1.21031 | -2.35802 | 1.66997 | -1.4704 | -2.38844 | -1.41061) |
| (0.458594 | 2.75866 | -1.58872 | 0.364191 | -2.1775 | -1.22843) |
| (0.386299 | 0.261576 | -0.174403 | 1.76511 | -2.95714 | 0.722224) |
| (-1.46748 | -2.15334 | -1.38535 | -1.73184 | 2.45454 | 1.7146) |
| (0.545927 | -2.51541 | -2.35701 | 0.0434106 | -0.207223 | 2.03679) |
| (0.325985 | 0.426342 | -1.7601 | -1.46899 | -0.638112 | -1.48682) |
| (0.995193 | 1.41102 | 2.67788 | -0.110336 | 0.810741 | -2.45279) |
| (1.00377 | -1.09859 | -0.9455 | 2.42064 | 1.69081 | 0.328404) |
| (1.65017 | 1.79446 | 0.906236 | -2.8566 | -1.2842 | 2.89926) |
| (-2.56134 | -0.141348 | -2.6657 | 1.22666 | 1.21836 | -1.79612) |
| (-0.519297 | 2.95723 | 1.68207 | 1.45581 | 1.81155 | 2.26842) |
| (-2.46329 | -0.587199 | -0.384539 | 2.98937 | -1.01251 | 2.22599) |
| (1.10689 | -1.94668 | 1.22285 | 1.941 | -0.7505 | -1.70434) |
| (0.642599 | -1.05925 | -1.2264 | 0.210594 | 2.56583 | -2.40472). |

Each of the 55 atoms is weighted by the one of the three following corre- sponding vector of weights: