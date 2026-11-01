---
retention_scope: session
part: 1
total_parts: 6
---

[Part 1/6 of: EGUCHI-HANSON]

# EGUCHI-HANSON

> Source: https://math.berkeley.edu/~appleton/version1.pdf
> Fetched: 2026-10-10 20:30
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
  "source": "web",
  "source_url": "https://math.berkeley.edu/~appleton/version1.pdf",
  "metadata": {
    "provenance_urls": [
      "https://math.berkeley.edu/~appleton/version1.pdf"
    ],
    "search_origins": [
      {
        "source": "duckduckgo",
        "query": "Eguchi Hanson Choose"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

Eguchi-Hansonand a family of Type II singularities 11.TheEguchi-Hansonspace is dieomorphic to the cotangent bundle of the two-sphere and asymptotic to the at cone R4/Z2.

## Retrieved source content

# EGUCHI-HANSON SINGULARITIES IN U(2)-INVARIANT RICCI FLOW

ALEXANDER APPLETON

Abstract. We show that a Ricci flow in four dimensions can develop singularities modeled on the Eguchi-Hanson space. In particular, we prove that starting
from a class of asymptotically cylindrical U(2)-invariant initial metrics on TS<sup>2</sup>, a
Type II singularity modeled on the Eguchi-Hanson space develops in finite time.
Furthermore, we show that for these Ricci flows the only possible blow-up limits
are (i) the Eguchi-Hanson space, (ii) the flat R<sup>4</sup>/Z<sub>2</sub> orbifold, (iii) the 4d Bryant
soliton quotiented by Z<sub>2</sub>, and (iv) the shrinking cylinder R×RP <sup>3</sup>. As a byproduct
of our work, we also prove the existence of a new family of Type II singularities
caused by the collapse of a two-sphere of self-intersection *|k|≥* 3.

$$
U(2)
$$

$$
TS^{2}
$$

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

$$
\mathbb{Z}_2
$$

$$
\mathbb{R}\times\mathbb{R}P^{3}
$$

$$
\left|\tilde{k}\right|\geq3.
$$

## Contents

1. Introduction
1.1. Background
1.2. Overview of setup
1.3. Overview of results
1.4. Precise statement of results
1.5. Outline of paper and proofs
1.6. Further questions and conjectures
1.7. Acknowledgments
2. Preliminaries
2.1. Notation

2
3
4
6
7
9
16
17
17
17

2.2. The manifold and metric 18
2.3. The connection, Laplacian and curvature tensor 20
2.4. The Ricci flow equation 22

2.5. Recap of blow-up limits of singularities

24

3. The maximum principle 25
4. K¨ahler quantities and the Eguchi-Hanson space 31
5. Some preserved conditions 33

6. Exclusion of shrinking solitons
7. Curvature bound
8. Compactness properties
9. Ancient Ricci flows Part I

40
45
53
62

10. Eguchi-Hanson and a family of Type II singularities 66

11. Ancient Ricci flows Part II: *k* = 2 case

72

---

11.1. Outline of Proof
11.2. Evolution equations
11.3. Construction of f<sub>θ</sub>, θ ∈ (0,1]
11.4. Non-negativity of W<sub>θ</sub>
11.5. Proof of main theorem
11.6. Proof of technical lemmas
12. Discussion of blow-up limits in *k* = 2 case
12.1. Outline of proof
12.2. Proof of main theorem
Appendix A
y
Evolution equations of a<sub>s</sub>, b<sub>s</sub>, Qb<sub>s</sub>, x, y and
Q
Evolution equation of *H*<sub>±</sub>
Evolution equation of f<sub>θ</sub>(Q)
Evolution equation of Z<sub>θ</sub>
Evolution equation of *Z<sub>1</sub>*
Evolution equations when *Q* = 1
Appendix B: Removable singularity
References

73
75
77
79
81
84
92
92
94
107
108
108
109
110
112
112
114
125

$$
f_{\theta},
$$

$$
\theta\in(0,1]
$$

$$
W_{\theta}
$$

$$
a_{s},b_{s},Q b_{s},x,
$$

$$
\frac{y}{Q}
$$

$$
H_{\pm}
$$

$$
f_{\theta}(Q)
$$

$$
Z_{\theta}
$$

$$
Z_{1}
$$

## 1. Introduction

The main result of this paper is to show

*A Ricci flow on a four dimensional non-compact manifold may develop a Type II singularity modeled on the Eguchi-Hanson space in
finite time.*

$$
de-
$$

The Eguchi-Hanson space is diffeomorphic to the cotangent bundle of the two-sphere
and asymptotic to the flat cone R<sup>4</sup>/Z<sub>2</sub>. It is the simplest example of a Ricci flat
asymptotically locally euclidean (ALE) manifold and in the physics literature known
as a gravitational instanton. The Eguchi-Hanson singularities constructed in this
paper are the first examples of orbifold singularities in Ricci flow, and are also the
first examples of singularities with Ricci flat blow-up limits. As a byproduct of our
work we also show that

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

*A Ricci flow on a four dimensional non-compact manifold may
collapse an embedded two-dimensional sphere with self-intersection
k ∈* Z *to a point in finite time and thereby produce a singularity.*

$$
k\in\mathbb{Z}
$$

The singularities we construct when *|k|≥* 3 are of Type II and the author conjectures
that their blow-up limits are homothetic to the steady Ricci solitons found in [A17].

$$
\left|k\right|\geq3
$$

---

1.1. Background. A family of time-dependent metrics *g(t*) on a manifold *M* is
called a Ricci flow if it solves the equation

$$
g(t)
$$

$$
\partial_{t}g(t)=-2R i c_{g(t)}.
$$

(1.1)

Here Ric<sub>g(t)</sub> is the Ricci tensor of the metric g(t). In local coordinates the Ricci
flow equation can be written as a coupled system of second order non-linear parabolic equations. Heuristically speaking, the Ricci flow smoothens the metric g(t),
while simultaneously shrinking positively curved and expanding negatively curved
directions at each point of the manifold.

$$
R i c_{g(t)}
$$

$$
g(t)
$$

$$
g(t)
$$

Ricci flow was introduced by Hamilton [Ham82] in 1982 to prove that a closed
three dimensional manifold admitting a metric of positive Ricci curvature also admits a metric of constant positive sectional curvature. This success demonstrated
the power of Ricci flow and ignited much research in this area, culminating in Perelman’s proof of the Poincaŕe and Geometrization Conjectures for three dimensional
manifolds.

Even though every complete Riemannian manifold *(M,g)* of bounded curvature
admits a short-time Ricci flow starting from *g,* singularities may develop in finite
time. Understanding their geometry is central to the study of Ricci flow and has
topological implications. For instance, Perelman proved the Geometrization Conjecture by analyzing the singularity formation in three dimensional Ricci flow and
showing that a Ricci flow nearing its singular time exhibits one of the following two
behaviors:

$$
(M,g)
$$

*•* Extinction: The manifold becomes asymptotically round before shrinking to
a point

*•* (Degenerate or non-degenerate) Neckpinch: A region of the shape of a small
cylinder R *× S<sup>2</sup>* develops

$$
\mathbb{R}\times S^{2}
$$

Based on this knowledge Perelman was able to construct a Ricci flow with surgery,
which performs the decomposition of a three manifold into pieces corresponding to
the eight Thurston geometries, yielding a proof of the Geometrization Conjecture.

In order to understand the formation of singularities in Ricci flow it is very useful to take blow-up limits. Roughly speaking one zooms into the region in which
the singularity is forming by parabolically rescaling space and time. The resulting
blow-up limit is an ancient Ricci flow called the singularity model. It encapsulates
most of the geometric information of the singularity. Note that a Ricci flow is called
ancient if it can be extended infinitely into the past. To date all known singularity
models are either shrinking or steady Ricci solitons. These are self-similar solutions to the Ricci flow equation that, up to diffeomorphism, homothetically shrink
or remain steady, and can be understood as a generalization of Einstein manifolds
of positive or zero scalar curvature, respectively. Hamilton distinguishes between
Type I and Type II singularities, depending on the rate at which the curvature
blows up to infinity as one approaches the singular time. It has been proven that
Type I singularities are modeled on shrinking Ricci solitons [EMT11], however it is unknown whether all Type II singularity models are steady Ricci solitons. In three
dimensions the only Type I singularity models are S<sup>3</sup>, R × S<sup>2</sup> and their quotients.

$$
S^{3},\mathbb{R}\times S^{2}
$$

As three dimensional singularity formation is now well understood the next step is
to analyze the four dimensional case, where currently very little is known other than
that the possibilities are far more numerous. Below we list all Type I singularity
models known in four dimensions:

(1) *S<sup>3</sup> ×* R and its quotients

$$
S^{3}\times\mathbb{R}
$$

(2) *S<sup>2</sup> ×* R<sup>2</sup> and its quotients

$$
S^{2}\times\mathbb{R}^{2}
$$

(3) Einstein manifolds of positive scalar curvature (e.g. S<sup>4</sup>, CP <sup>2</sup>, etc.)

$$
(\mathrm{e.g.}S^{4},\mathbb{C}P^{2},\mathrm{etc.})
$$

(4) Compact gradient shrinking Ricci solitons that are not Einstein

(5) The FIK shrinker [FIK03]

Note that (1) and (2) are just products of a three dimensional Type I singularity
model with the real line. As Einstein manifolds in four dimensions remain to be
classified, list item (3) may contain a very large set of manifolds. As for (4), to date
only few examples of compact shrinking Ricci solitons are known and a list of these
can be found in Cao’s survey [Cao10]. The FIK shrinker is a non-compact U(2)-
invariant shrinking K¨ahler-Ricci soliton, which is diffeomorphic to the blow-up of
C<sup>2</sup> at the origin. It is an open question whether there are other non-flat one-ended
shrinking Ricci solitons in four dimensions. Maximo proved that Type I singularities
modeled on the FIK shrinker may occur in U(2)-invariant K¨ahler-Ricci flow [M14].

$$
\mathbb{C}^2
$$

The FIK shrinker models an interesting singularity in four dimensional Ricci flow
— namely the collapse of an embedded two-dimensional sphere with non-trivial
normal bundle. Topologically, real rank 2 vector bundles over the two-dimensional
sphere are classified by their Euler class, which is an integer multiple of the generator of H<sup>2</sup>(S<sup>2</sup>,Z). We call this multiple the twisting number and denote it by k.
Recall that the self-intersection of an embedded two-dimensional sphere in a fourdimensional manifold is equal to the twisting number of its normal bundle. Unlike
in K¨ahler geometry, where there is a canonical choice for the generator of H<sup>2</sup>(S<sup>2</sup>,Z)
and the sign of the self-intersection number is crucial, in the Riemannian case only
its absolute value affects the geometry and behavior of embedded two-spheres under
Ricci flow. Heuristically speaking, the larger *|k|*, the more negative curvature there
is in the vicinity of the sphere and the less likely it collapses to a point. In the list
above *S<sup>2</sup> ×* R<sup>2</sup> and the FIK shrinker model the collapse of two dimensional spheres
with self-intersection equal to 0 and −1, respectively. The main goal of this paper is
to show that embedded spheres of self-intersection number *|k|≥* 2 may also collapse
in finite time. To explain this in greater detail we give an overview of our setup
below.

$$
H^{2}(S^{2},\mathbb{Z})
$$

$$
H^{2}(S^{2},\mathbb{Z})
$$

$$
S^{2}\times\mathbb{R}^{2}
$$

$$
|k|\geq2
$$

1.2. Overview of setup. Let M<sub>k</sub>, k ≥ 1, be diffeomorphic to the blow-up of
C<sup>2</sup>/Z<sub>k</sub> at the origin, and denote by S<sup>2</sup><sub>o</sub> the two-sphere stemming from the blow-up.
Alternatively one can also view M<sub>k</sub> as a plane bundle over S<sub>o</sub><sup>2</sup>. Fix an arbitrary
point o, for ’origin’, on S<sub>o</sub><sup>2</sup>. Note that S<sub>o</sub><sup>2</sup>, with respect to the orientation inherited
from C<sup>2</sup>, has self-intersection −k. Then equip M<sub>k</sub> with an U(2)-invariant metric g.

$$
M_{k},\ k\ \geq\ 1
$$

$$
\mathbb{C}^2/\mathbb{Z}_k
$$

$$
S_{o}^{2}
$$

$$
M_{k}
$$

$$
S_{o}^{2}.
$$

$$
S_{o}^{2}
$$

$$
S_{o}^{2},
$$

$$
\mathbb{C}^2
$$

$$
M_{k}
$$

$$
U(2)
$$

---

It turns out that with help of the Hopf fibration

$$
\pi:S^{3}/\mathbb{Z}_{k}\rightarrow S^{2}
$$

such U(2)-invariant metrics can be conveniently written as a warped product metric
of the form

$$
U(2)
$$

(1.2)

$$
g=d s^{2}+a^{2}(s)\omega\otimes\omega+b^{2}(s)\pi^{*}g_{S^{2}(\frac{1}{2})},
$$

on the open dense subset R>0× S<sup>3</sup>/Z<sub>k</sub> ⊂ M<sub>k</sub>. ω is the 1-form dual to the vertical
directions of the Hopf fibration and *s* is a parametrisation of the R>0factor. Note
that g pulls back to a Berger sphere metric on the cross-sections S<sup>3</sup>/Z<sub>k</sub>. One can
complete g to a smooth metric on all of M<sub>k</sub> by requiring

$$
\mathbb{R}_{>0}\times S^{3}/\mathbb{Z}_{k}\subset M_{k}
$$

$$
\mathbb{R}_{>0}
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
M_{k}
$$

(0) = 0(1.3)

$$
\begin{aligned}a(0)&=0,\\a_{s}(0)&=k,\\b(0)&>0.\end{aligned}
$$

and that *a(s*) and *b(s*) can be extended to an odd and even function around *s* = 0,
respectively. Via the boundary condition a<sub>s</sub>(0) = k is how topology enters the
analysis of the Ricci flow equation. We would like to mention here that throughout
this paper we often take the warping functions *a* and *b* to be functions of points
*(p,t)* in spacetime rather than of (*s,t).* This will always be clear from context.

$$
a(s)
$$

$$
b(s)
$$

$$
s=0
$$

$$
a_{s}(0)\;=\;k
$$

$$
(p,t)
$$

$$
(s,t)
$$

An upshot of writing the metric *g* in the form (1.2) is that the Ricci flow equation
(1.1) reduces to a (1 + 1)-dimensional system of parabolic equations for the warping
functions *a* and *b,* which simplifies the analysis greatly. In addition to this, both the
FIK shrinker, which is diffeomorphic to *M<sub>1</sub>,* and the Eguchi-Hanson space, which is
diffeomorphic to *M<sub>2</sub>,* are U(2)-invariant, and therefore their metrics can be written
in the form (1.2). In this paper we only study Riemannian manifolds diffeomorphic
to M<sub>k</sub>, k ∈ N, equipped with a U(2)-invariant metric of the form (1.2).

$$
M_{1}
$$

$$
M_{2}
$$

$$
U(2)
$$

$$
M_{k},k\in\mathbb{N}
$$

We will consider numerous *scale-invariant* quantities, the most fundamental and
important of which we introduce here:
<u><em>a</em></u>

$$
\begin{aligned}Q&:=\frac{a}{b}\\x&:=a_{s}+Q^{2}-2\\y&:=b_{s}-Q\end{aligned}
$$

The quantity Q measures the ‘roundness’ of the cross-sectional S<sup>3</sup>/Z<sub>k</sub>. That is,
when *Q* = 1 the metric on the cross-section is round. The quantities *x* and *y* are
more interesting, as they measure the deviation of the metric *g* from being K¨ahler.
In particular, when
*y* = 0

$$
Q
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
Q=1
$$

$$
y
$$

$$
g
$$

$$
y=0
$$

the manifold (M<sub>k</sub>,g), k ≥ 1, is K¨ahler with respect to the standard complex structure induced from C<sup>2</sup>. Moreover, when

$$
(M_k,g),k\geq1
$$

$$
\mathbb{C}^2
$$

$$
x=y=0
$$ the manifold (M<sub>k</sub>,g) is hyperk¨ahler, and as we show in section 4, homothetic to the
Eguchi-Hanson space.

$$
\left(M_{k},g\right)
$$

### 1.3. Overview of results. The first main result of this paper is to show that

*For a large class of* U(2)-*invariant asymptotically cylindrical initial*
metrics on M<sub>k</sub>, k ≥ 2, the Ricci flow develops a Type II singularity
in finite time, as the area of S<sup>2</sup><sub>o</sub> decreases to zero. When k = 2 the
*blow-up limit of the singularity is homothetic to the Eguchi-Hanson*
*space.*

$$
M_{k},k\geq2
$$

$$
S_{o}^{2}
$$

We define the class of metrics for which this result holds in subsection 1.4. Note
that in the *k* = 2 case the Eguchi-Hanson space is the first example of a Ricci
flat singularity model. Based on numerical simulations the author believes that the
Type II singularities in the *k ≥* 3 case are modeled on the steady solitons found in
[A17]. A paper on the numerical results is in preparation.

$$
k=2
$$

$$
k\geq3
$$

The above result should be contrasted with the behavior of a Ricci flow starting
from a K¨ahler metric. It is well known that the K¨ahler condition is preserved by
Ricci flow, and that for such a flow the area of a complex submanifold evolves in
a fixed manner. In particular, if *(M,g)* is a K¨ahler manifold with K¨ahler form *ω,*
then under Ricci flow the K¨ahler class evolves by

$$
(M,g)
$$

$$
\omega,
$$

$$
\left[\omega(t)\right]=\left[\omega(0)\right]-4\pi t c_{1}(M),
$$

where *c<sub>1</sub>(M*) is the first Chern class of *M.* If we integrate the above equation over
a complex curve Σ in *M* then one sees that

$$
c_{1}(M)
$$

$$
\Sigma
$$

$$
|\Sigma|_{t}=|\Sigma|_{0}-4\pi t\langle c_{1}(M),[\Sigma]\rangle,
$$

where |Σ|<sub>t</sub> denotes the area of Σ at time t. In the case that M ∼= M<sub>k</sub>, Σ = S<sup>2</sup><sub>o</sub> and
*g* is K¨ahler, it was shown in [FIK03, Proof of Lemma 1.2] that

$$
|\Sigma|_{t}
$$

$$
\Sigma
$$

$$
M\cong M_{k},\Sigma=S_{o}^{2}
$$

$$
g
$$

$$
\langle c_{1}(M_{k}),[S_{o}^{2}]\rangle=2-k
$$

and hence

(1.4)

$$
|S_{o}^{2}|_{t}=|S_{o}^{2}|_{0}-4\pi t\left(2-k\right).
$$

This shows that for a K¨ahler-Ricci flow (M<sub>k</sub>,g(t)), k ∈ N the two sphere S<sup>2</sup><sub>o</sub> can only
collapse to a point when k = 1. In fact, when k = 2 the area of S<sup>2</sup><sub>o</sub> is stationary and
for *k ≥* 3 increasing. Maximo in [M14] uses the K¨ahler condition and (1.4) to show
that an embedded sphere of self-intersection *−1* may collapse to a point in finite
time under Ricci flow. Note that in our construction the metrics are not assumed
to be K¨ahler and hence we cannot rely on (1.4).

$$
(M_{k},g(t)),k\in\mathbb{N}
$$

$$
S_{o}^{2}
$$

$$
k\geq3
$$

$$
S_{o}^{2}
$$

$$
k=2
$$

The second main result of this paper is the classification of all possible blow-up
limits in the *k* = 2 case, including those at larger distance scales from the tip of *M<sub>2</sub>.*
In particular, we show that

$$
M_{2}
$$

---

*For a large class of* U(2)-*invariant asymptotically cylindrical initial
metrics on M<sub>2</sub> any sequence of blow-ups subsequentially converges
to one of the following spaces:*

$$
M_{2}
$$

*(i) The Eguchi-Hanson space*

*(ii) The flat* R<sup>4</sup>/Z<sub>2</sub> *orbifold*

*(iii) The 4d Bryant soliton quotiented by* Z<sub>2</sub>

$$
\mathbb{Z}_2
$$

*(iv) The shrinking cylinder* R *× RP<sup>3</sup>*

$$
\mathbb{R}\times\mathbb{R}P^{3}
$$

The blow-up limits (ii) and (iii) show that the Eguchi-Hanson singularity results
in the formation of an orbifold point, which to our knowledge the first concrete
example of such in four dimensional Ricci flow.

We expect that many of our methods generalize to the analysis of Ricci flow on
other cohomogeneity one manifolds. These are manifolds that admit an action by
isometries of a compact Lie group *G* for which the quotient is one dimensional. The
author believes that this work could contribute towards a complete picture of Ricci
solitons and ancient Ricci flows on cohomogeneity one manifolds in four dimensions.

1.4. Precise statement of results. Before presenting the main theorems of this
paper, we list the definition of a class *I* of metrics needed to state our results.

Definition 7.2. *For K* > 0 *let IK be the set of all complete* bounded curvature
metrics of the form (1.2) on M<sub>k</sub>, k ≥ 1, with positive injectivity radius that satisfy
*the following scale-invariant inequalities:*

$$
K>0
$$

$$
\mathcal{I}_{K}
$$

$$
M_{k},\;k\geq1
$$

$$
\begin{aligned}{Q}&{{}\leq1}\\ {a_{s},b_{s}}&{{}\geq0}\\ {y}&{{}\leq0}\\ {\operatorname*{s u p}a_{s}}&{{}<K}\\ {\operatorname*{s u p}|b b_{s s}|}&{{}<K.}\\ \end{aligned}
$$

*Denote by I the set of metrics g such that for sufficiently large K* > 0 *we have
g ∈IK.*

$$
K>0
$$

$$
g\in\mathcal{I}_{K}
$$

For any k ∈ N the set I of metrics on M<sub>k</sub> is non-empty, as for example the metric
on M<sub>k</sub> defined by

$$
k\in\mathbb{N}
$$

$$
M_{k}
$$

$$
\mathcal{I}
$$

$$
M_{k}
$$

$$
a(s)=Q=\tanh(ks)
$$

$$
b(s)=1
$$

is contained in *I.* Moreover, as we prove in Lemma 7.9, the class *IK* of metrics is
preserved by the Ricci flow for sufficiently large *K* > 0. In our paper we will mainly
consider Ricci flows (M<sub>k</sub>,g(t)), t ∈ [0,T), starting from an initial metric g(0) ∈I.

$$
\mathcal{I}_{K}
$$

$$
K>0
$$

$$
(M_{k},g(t)),t\in[0,T)
$$

$$
g(0)\in\mathcal{I}
$$

Now we list the precise statements of the main results of this paper.

---

Theorem 9.1 (Type II singularities). *Let* (*M*
*from an initial metric* g(0) *∈I (see Definition 7.2) with*

<sub>k</sub>,g(t)), k ≥ 2, be a Ricci flow starting

$$
\left(M_{k},g(t)\right),k\geq2
$$

$$
g(0)\in\mathcal{I}
$$

$$
\operatorname*{s u p}_{p\in M_{2}}b(p,0)<\infty.
$$

Then g(t) encounters a Type II curvature singularity in finite time T<sub>sing</sub> > 0 and

$$
g(t)
$$

$$
T_{\textit{s i n g}}>0
$$

$$
\sup_{0\leq t<T_{\mathrm{sing}}}\left(T_{\mathrm{sing}}-t\right)b^{-2}(o,t)=\infty.
$$

*Furthermore, there exists a sequence of times t
holds: Consider the rescaled metrics*
() [

<sub>i</sub> → T

<sub>sing</sub> such that the following
)

$$
t_{i}\rightarrow T_{sign}
$$

$$
g_{i}(t)=\frac{1}{b^{2}(o,t_{i})}g\left(t_{i}+b^{2}(o,t_{i})t\right),\quad t\in\big[-b(o,t_{i})^{-2}t_{i},b(o,t_{i})^{-2}\left(T_{s i n g}-t_{i}\right)\big).
$$

Then (M<sub>k</sub>,g<sub>i</sub>(t),o) subsequentially converges, in the pointed Gromov-Cheeger sense,
to an eternal Ricci flow (M<sub>k</sub>,g∞(t),o), t ∈ (−∞, ∞). When k = 2 the metric g∞(t)
*is stationary and homothetic to the Eguchi-Hanson metric.*

$$
(M_{k},g_{i}(t),o)
$$

$$
\left(M_{k},g_{\infty}(t),o\right),t\in(-\infty,\infty)
$$

$$
g_{\infty}(t)
$$

*Remark* 1.1. We would like to make the following remarks:

(1) In Theorem 9.1, case *k* = 2, we only prove that there exists a blow-up
sequence which converges to the Eguchi-Hanson space. In Theorem 12.1
below we extend this result and show that in fact any blow-up around the
tip of *M<sub>2</sub>* is homothetic to the Eguchi-Hanson space.

$$
M_{2}
$$

(2) The initial metric g(0) *∈I* with sup<sub>p∈M</sub>*b(p,0*) < *∞* is asymptotic to R *×*
S<sup>3</sup>/Z<sub>k</sub>, where S<sup>3</sup>/Z<sub>k</sub> is equipped with a squashed Berger sphere metric. This
is because metrics in I satisfy a<sub>s</sub>,b<sub>s</sub> ≥ 0 and Q ≤ 1.

$$
g(0)\in\mathcal{I}
$$

$$
\mathbb{R}\times
\sup_{p\in M}b(p,0)<\infty
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
a_{s},b_{s}\geq0
$$

$$
Q\leq1
$$

The second main result of our paper is the classification of all possible blow-up
limits in the *k* = 2 case:

Theorem 12.1 (Blow-up limits). Let (M<sub>2</sub>,g(t)), t ∈ [0,T<sub>sing</sub>), be a Ricci flow
*starting from an initial metric* g(0) *∈I (see Definition 7.2) with* sup<sup>p∈M</sup>*b(p,0*) <
2
∞. Let (p<sub>i</sub>,t<sub>i</sub>) be a sequence of points in spacetime with b(p<sub>i</sub>,t<sub>i</sub>) → 0. Passing to a
*subsequence, we may assume that we are in one of the four cases listed below.*

$$
(M_{2},g(t)),\;t\in[0,T_{\mathrm{sing}})
$$

$$
g(0)\in\mathcal{I}
$$

$$
7.2)
$$

$$
\sup_{p\in M_{2}}b(p,0)<
$$

$$
(p_{i},t_{i})
$$

$$
b(p_{i},t_{i})\rightarrow0
$$

*(i)* lim<sub>i→∞</sub>
(ii) lim

<u><em>b(p ,ti</em></u> <u>i)</u>
< *∞
b(o,t*<sub>i</sub>)
<u><em>b(p ,t</em></u><u>)</u>
= ∞ and

$$
\operatorname*{l i m}_{i\to\infty}\frac{b(p_{i},t_{i})}{b(o,t_{i})}<\infty
$$

$$
\lim_{i\to\infty}\frac{b(p_i,t_i)}{b(o,t_i)}=\infty and\lim_{i\to\infty}b_s(p_i,t_i)=1
$$

$$
\begin{array}{l}\lim_{i\rightarrow\infty}\frac{b\left(p_{i},t_{i}\right)}{b\left(o,t_{i}\right)}=\infty\text{and}\lim_{i\rightarrow\infty}b_{s}\left(p_{i},t_{i}\right)\in(0,1)\end{array}
$$

$$
\begin{array}{l}\lim_{i\rightarrow\infty}\frac{b\left(p_{i},t_{i}\right)}{b\left(o,t_{i}\right)}=\infty\text{and}\lim_{i\rightarrow\infty}b_{s}\left(p_{i},t_{i}\right)=0\end{array}
$$

*Consider the dilated Ricci flows*

$$
g_{i}(t)=\frac{1}{b^{2}(p_{i},t_{i})}g\left(t_{i}+b^{2}(p_{i},t_{i})t\right),\quad t\in[-b(p_{i},t_{i})^{-2}t_{i},0].
$$

---

Then (M<sub>2</sub>,g<sub>i</sub>(t),p<sub>i</sub>), t ∈ [−b(p<sub>i</sub>,t<sub>i</sub>)<sup>−2</sup>t<sub>i</sub>,0], subsequentially converges, in the Cheeger-
*Gromov sense, to an ancient Ricci flow* (*M*<sub>∞</sub>*,g*<sub>∞</sub>(*t),p*<sub>∞</sub>*), t ∈* (*−∞,0]. Depending*
on the limiting property of the sequence (p<sub>i</sub>,t<sub>i</sub>) we have:

$$
(M_{2},g_{i}(t),p_{i}),\;t\in[-b(p_{i},t_{i})^{-2}t_{i},0]
$$

$$
\left(M_{\infty},g_{\infty}(t),p_{\infty}\right),t\in(-\infty,0]
$$

$$
(p_{i},t_{i})
$$

∼
*(i) M*<sub>∞</sub>= *M<sub>2</sub> and g*<sub>∞</sub>(t) *is stationary and homothetic to the Eguchi-Hanson
metric*

$$
M_{\infty}\cong M_{2}
$$

$$
g_{\infty}(t)
$$

∼
*(ii) M*<sub>∞</sub>= R<sup>4</sup>*\{0}/Z<sub>2</sub> and g*<sub>∞</sub>(t) *can be extended to a smooth orbifold Ricci flow
on* R<sup>4</sup>/Z<sub>2</sub> *that is stationary and isometric to the flat orbifold* R<sup>4</sup>/Z<sub>2</sub>

$$
M_{\infty}\cong\mathbb{R}^{4}\backslash\{0\}/\mathbb{Z}_{2}
$$

$$
g_{\infty}(t)
$$

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

∼
*(iii) M*<sub>∞</sub>= R<sup>4</sup>*\{0}/Z<sub>2</sub> and g*<sub>∞</sub>(t) *can be extended to a smooth orbifold Ricci flow*

$$
M_{\infty}\cong\mathbb{R}^{4}\backslash\{0\}/\mathbb{Z}_{2}
$$

$$
g_{\infty}(t)
$$

*on* R<sup>4</sup>/Z<sub>2</sub> *that is homothetic to the 4d Bryant soliton quotiented by* Z<sub>2</sub>

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

$$
\mathbb{Z}_2
$$

∼
*(iv) M*<sub>∞</sub>= R *× RP<sup>3</sup> and g*<sub>∞</sub>(t) *is homothetic to a shrinking cylinder*

$$
M_{\infty}\cong\mathbb{R}\times\mathbb{R}P^{3}
$$

$$
g_{\infty}(t)
$$

*Remark* 1.2. Note that in Theorem 12.1 we do not prove that all blow-up limits (i)-
(iv) occur. In fact, it may turn out that the Eguchi-Hanson singularity is isolated,
in which case we would only see blow-up limits (i) and (ii).

As a byproduct of our work we also prove the following two theorems, which are
of independent interest. Firstly, we exclude shrinking Ricci solitons in a large class
of metrics.

Theorem 6.1 (No shrinker). On M<sub>k</sub>, k ≥ 2, there does not exists a complete U(2)-
*invariant shrinking Ricci soliton of bounded curvature satisfying the conditions*

$$
U(2)
$$

$$
M_{k},k\geq2
$$

(1) supp∈M|b<sub>s</sub>|<∞
k
*(2) T<sub>1</sub>* = *a* + *2Q<sup>2</sup> −* 2

$$
\sup_{p\in M_{k}}\left|b_{s}\right|<\infty
$$

$$
T_{1}=a_{s}+2Q^{2}-2>0\;\mathrm{for}\;s>0
$$

a
*(3) Q* = *≤* 1
*b*

$$
Q=\frac{a}{b}\leq1
$$

As we show in section 5 the inequalities *T<sub>1</sub>* > 0 for *s* > 0 and *Q ≤* 1 are preserved
by a Ricci flow (M<sub>k</sub>,g(t)), k ≥ 2, with g(t) ∈I. For this reason Theorem 6.1 can
be used to exclude Type I singularities for such flows.

$$
T_{1}>0
$$

$$
s>0
$$

$$
Q\leq1
$$

$$
(M_{k},g(t)),\;k\geq2
$$

$$
g(t)\in\mathcal{I}
$$

Secondly, we prove a uniqueness result for ancient Ricci flows on *M<sub>2</sub>.*

$$
M_{2}
$$

Theorem 11.1 (Unique ancient flow). *Let κ* > 0 *and* (*M<sub>2</sub>,g(t)), t ∈ (−∞,0], be
an ancient Ricci flow that is κ-non-collapsed at all scales and g(t) ∈I, t ∈* (*−∞,0*]
*(see Definition 7.2). Then g(t*) *is stationary and homothetic to the Eguchi-Hanson
metric.*

$$
\kappa>0
$$

$$
\left(M_{2},g(t)\right)
$$

$$
t\in(-\infty,0]
$$

$$
g(t)\in\mathcal{I},t\in(-\infty,0]
$$

$$
g(t)
$$

We rely heavily on this result when we investigate all possible blow-up limits of
a Ricci flow (M<sub>2</sub>,g(t)) encountering a singularity at S<sub>o</sub><sup>2</sup>.

$$
\left(M_{2},g(t)\right)
$$

$$
S_{o}^{2}
$$

1.5. Outline of paper and proofs. Our paper is organized by sections. Section
2 is preliminary and its goal is to set up in more detail the manifolds and metrics
considered in this paper. Here we also derive the full curvature tensor and Ricci
flow equation for U(2)-invariant metrics. In section 3 we prove a maximum principle
for degenerate parabolic differential equations on M<sub>k</sub>. Beginning from section 4 we

$$
M_{k}
$$ present new results. Below we outline the main results of those sections and their
proofs.

Outline of section 4. A key ingredient in our paper are the scale-invariant quantities
x = a + Q<sup>2</sup> − 2

$$
x=a_{s}+Q^{2}-2
$$

and

$$
y=b_{s}-Q,
$$

that measure the deviation of a U(2)-invariant metric from being K¨ahler with respect
to two fixed complex structures J<sub>1</sub> and J<sub>2</sub> on M<sub>k</sub>, k ≥ 1 (see section 4 for the precise
definition of *J<sub>1</sub>* and *J<sub>2</sub>).* In particular, a metric is K¨ahler with respect to *J<sub>1</sub>* whenever
*y* = 0 and with respect to *J<sub>2</sub>* whenever *x* = *y* = 0.

$$
U(2)
$$

$$
J_{1}
$$

$$
J_{2}
$$

$$
M_{k},k\geq1
$$

$$
J_{1}
$$

$$
J_{2})
$$

$$
J_{1}
$$

$$
J_{2}
$$

$$
x=y=0
$$

$$
y=0
$$

Interestingly, a U(2)-invariant metric of the form (1.2) is K¨ahler with respect to
*J<sub>2</sub>* if, and only if, the underlying manifold is diffeomorphic to *M<sub>2</sub>* and the metric is
homothetic to the Eguchi-Hanson metric, as we show in Lemma 4.1. Therefore the
quantities *x* and *y* can be used to measure how much a metric on *M<sub>2</sub>* deviates from
the Eguchi-Hanson metric — a tool that is indispensable to our analysis. In the
later sections we develop methods to control the behavior of *x* and *y* under the Ricci
flow. This will allow us to prove that certain singularities of Ricci flows *(M<sub>2</sub>,g(t))*
are modeled on the Eguchi-Hanson space.

$$
U(2)
$$

$$
J_{2}
$$

$$
M_{2}
$$

$$
x
$$

$$
M_{2}
$$

$$
\left(M_{2},g(t)\right)
$$

In Lemma 4.2 of this section we also derive various properties of the Eguchi-
Hanson metric. These are frequently used throughout the paper.

Outline of section 5. The goal of this section is to derive various *scale-invariant*
inequalities that are conserved by Ricci flow. We say that on a Riemannian manifold
(M,g) a geometric quantity T<sub>g</sub>: M → R is scale-invariant if for every point p ∈ M,
we have T<sub>g</sub>(p) = T<sub>λg</sub>(p) for all λ > 0. The scale-invariance of the inequalities derived
is crucial, as it ensures that they pass to blow-up limits and thus also constrain their
geometry.

$$
(M,g)
$$

$$
T_{g}:M\rightarrow\mathbb{R}
$$

$$
p\in M
$$

$$
T_{g}(p)=T_{\lambda g}(p)
$$

$$
\lambda>0.
$$

We construct these inequalities from the scale-invariant quantities a<sub>s</sub>, b<sub>s</sub> and Q :=
<sup>a</sup><sub>b</sub>, where a and b are the warping functions of the metric g of the form (1.2). Note
that subscript *s* denotes the derivative with respect to *s.* The key observation is
that the evolution equation of the *scale-invariant* quantity

$$
a_{s},b_{s}
$$

$$
Q:=
\frac{a}{b}
$$

$$
T_{(\alpha,\beta,\gamma)}=\alpha a_{s}+\beta Q b_{s}+\gamma Q^{2},\quad\alpha,\beta,\gamma\in\mathbb{R},
$$

can be written in the form
[

$$
\partial_{t}T_{(\alpha,\beta,\gamma)}=\left[T_{(\alpha,\beta,\gamma)}\right]_{s s}+\left(2\frac{b_{s}}{b}-\frac{a_{s}}{a}\right)\left[T_{(\alpha,\beta,\gamma)}\right]_{s}+\frac{1}{b^{2}}C_{(\alpha,\beta,\gamma)},
$$

where C<sub>(α,β,γ)</sub> is a function of a<sub>s</sub>, b<sub>s</sub> and Q. For certain choices of α, β, γ and δ ∈ R
one can determine the sign of C<sub>(α,β,γ)</sub> at a local extremum at which T<sub>(α,β,γ)</sub> = δ.
Depending on the sign, this allows one to prove, via the maximum principle, that
either
*T ≥ δ*

$$
C_{(\alpha,\beta,\gamma)}
$$

$$
a_{s},b_{s}
$$

$$
\alpha,\beta,\gamma
$$

$$
Q
$$

$$
\delta\in\mathbb{R}
$$

$$
T_{(\alpha,\beta,\gamma)}=\delta
$$

$$
C_{(\alpha,\beta,\gamma)}
$$

$$
T_{(\alpha,\beta,\gamma)}\geq\delta
$$ or

$$
T_{(\alpha,\beta,\gamma)}\leq\delta
$$

is a conserved inequality. One of the conserved inequalities of this form is

$$
x\leq0,
$$

however we derive many others.

In this section we also find conserved inequalities not of the above form. For
instance, we show that each of the inequalities listed below are conserved by the
Ricci flow:

$$
\bullet Q\leq1
$$

$$
\bullet y\leq0
$$

$$
\bullet a_{s},b_{s}\geq0
$$

The proof is carried out by applying the maximum principle to their evolution
equations or, in the case of a<sub>s</sub>,b<sub>s</sub> ≥ 0, to their system of evolution equations. The
conserved inequalities Q ≤ 1, y ≤ 0 and a<sub>s</sub>,b<sub>s</sub> ≥ 0 are especially important, as they
are part of the definition of the class of metrics *I* mentioned above, and constitute
the first step in showing that *I* is preserved by the Ricci flow.

$$
a_{s},b_{s}\geq0
$$

$$
Q\leq1,y\leq0
$$

$$
a_{s},b_{s}\geq0
$$

Outline of section 6. The main result of section 6 is Theorem 6.1, which rules
out shrinking solitons on M<sub>k</sub>, k ≥ 2, within a large class of U(2)-invariant metrics.
Before we outline the proof, note that from the evolution equation (2.12) of *b* under
Ricci flow it follows by an application of L’Ĥopital’s rule that at *s* = 0

$$
M_{k},k\geq2
$$

$$
s=0
$$

(1.5)

$$
\partial_{t}b(0,t)^{2}=4\left(b y_{s}+k-2\right).
$$

This formula is a generalization of (1.4) to the non-K¨ahler case, as the area of S<sup>2</sup><sub>o</sub>
at time *t* equals *b(o,t)<sup>2</sup>π.* Hence a shrinking soliton must satisfy

$$
S_{o}^{2}
$$

$$
b(o,t)^{2}\pi
$$

$$
\partial_{t}b(0,t)^{2}<0,
$$

which for k ≥ 2 implies that y<sub>s</sub> < 0 at s = 0.

$$
k\geq2
$$

$$
y_{s}<0
$$

$$
s=0
$$

For the proof of Theorem 6.1 we have to rely on the inequality

$$
T_{1}=a_{s}+2Q^{2}-2\geq0,
$$

which by Lemma 5.8 is conserved by the Ricci flow. In particular, we show that
amongst metrics of the form (1.2) on M<sub>k</sub>, k ≥ 2, satisfying Q ≤ 1, T<sub>1</sub> > 0 when
s > 0, and supp∈M|b<sub>s</sub>|<∞ there are no shrinking solitons. We briefly sketch the
k
proof here: First we show in Lemma 6.4 that Q<sub>s</sub> ≥ 0 for shrinking solitons. This
follows from the Ricci soliton equation, which for metrics of the form (1.2) reduces to
a system of ordinary differential equations. Then we consider the evolution equation
<u><em>a y</em></u>

$$
M_{k},\;k\geq2
$$

$$
Q\leq1,T_1>0
$$

$$
s>0
$$

$$
\sup_{p\in M_{k}}\left|b_{s}\right|<\infty
$$

$$
Q_{s}\geq0
$$

(1.6)

$$
\partial_{t}y=y_{s s}+\frac{a_{s}}{a}y-\frac{y}{a^{2}}G,
$$

of y, where G is a function of a<sub>s</sub>, b<sub>s</sub> and Q. In Lemma 6.5 we show that whenever
Q<sub>s</sub>,T<sub>1</sub> > 0 we have G > 0. This shows that under Ricci flow satisfying these
inequalities a negative minimum of *y* is strictly increasing and a positive maximum
is strictly decreasing. However, since *y* is a scale-invariant quantity, and a shrinking

$$
y,
$$

$$
a_{s},\;b_{s}
$$

$$
Q.
$$

$$
Q_{s},T_{1}\;>\;0
$$

$$
G>0
$$

---

Ricci soliton, up to diffeomorphism, homothetically shrinks under Ricci flow, we see
that the maximum or minimum of *y* must remain constant throughout the flow.
We conclude that *y* = 0 everywhere, excluding a shrinking soliton. In the proof of
Theorem 6.1, rather than working with the evolution equation (1.6) of *y,* we use the
corresponding ordinary differential equation on a Ricci soliton background.

$$
y
$$

$$
y=0
$$

$$
y,
$$

Outline of section 7. The goal of this section is to prove Theorem 7.5, which states
that for a Ricci flow (M<sub>k</sub>,g(t)), k ≥ 1, starting from an initial metric g(0) ∈I with
supp∈Mb(p,0) < *∞* there exists a *C<sub>1</sub>* > 0 such that the curvature bound
*k*
C<sub>1</sub>

$$
\left(M_{k},g(t)\right),k\geq1
$$

$$
g(0)\in\mathcal{I}
$$

$$
\sup_{p\in M_{k}}b(p,0)<\infty
$$

$$
C_{1}>0
$$

$$
|R m_{g(t)}|_{g(t)}\leq\frac{C_{1}}{b^{2}}
$$

holds. The proof is carried out by a contradiction/blow-up argument: Assume there
exists a sequence of numbers D<sub>i</sub> →∞ and points (p<sub>i</sub>,t<sub>i</sub>) in spacetime such that
D

$$
D_{i}\rightarrow\infty
$$

$$
(p_{i},t_{i})
$$

$$
K_{i}:=|R m_{g(t_{i})}|_{g(t_{i})}(p_{i})=\frac{D_{i}}{b(p_{i},t_{i})^{2}}.
$$

Consider the rescaled metrics

$$
g_{i}(t)=K_{i}g\left(t_{i}+\frac{t}{K_{i}}\right),\quad t\in[-K_{i}t_{i},0],
$$

normalized such that |Rm<sub>g</sub> <sub>(0)</sub>|<sub>g</sub> <sub>(0)</sub>(p<sub>i</sub>) = 1. Then Perelman’s no-local-collapsing
i i
theorem shows that (M<sub>k</sub>,g<sub>i</sub>(t),p<sub>i</sub>) subconverges to an ancient non-collapsed Ricci
flow (M∞,g∞(t),p∞), t ≤ 0. As D<sub>i</sub> →∞ the warping functions b<sub>i</sub> corresponding
to the metrics g<sub>i</sub>(t) satisfy b<sub>i</sub>(p<sub>i</sub>,0) → ∞. Recalling that the warping function b
describes the size of the base manifold S<sup>2</sup> in the Hopf fibration of the S<sup>3</sup>/Z<sub>k</sub> crosssections, one can see that (*M*<sub>∞</sub>*,g*<sub>∞</sub>(t)) splits as *M*<sub>∞</sub>= R<sup>2</sup>× *N,* where R<sup>2</sup> is equipped
with the flat euclidean metric and the restriction of *g*<sub>∞</sub>(t) to *N* is a 2d non-compact
*κ*-solution. However, the only *κ*-solutions in 2d are either the shrinking sphere or
its Z<sub>2</sub> quotient, both of which are compact. This is a contradiction and the proof of
the curvature bound follows.

$$
\left|R m_{g_{i}(0)}\right|_{g_{i}(0)}(p_{i})=1
$$

$$
(M_{k},g_{i}(t),p_{i})
$$

$$
\left(M_{\infty},g_{\infty}(t),p_{\infty}\right),t\leq0
$$

$$
b_{i}
$$

$$
D_{i}\rightarrow\infty
$$

$$
g_{i}(t)
$$

$$
b_{i}(p_{i},0)\to\infty
$$

$$
S^{2}
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
\left(M_{\infty},g_{\infty}(t)\right)
$$

$$
M_{\infty}=\mathbb{R}^2\times N
$$

$$
\mathbb{R}^2
$$

$$
g_{\infty}(t)
$$

$$
\mathbb{Z}_2
$$

In Corollary 7.6 we show that ancient Ricci flows in *I,* which are *κ*-non-collapsed
at all scales, also satisfy the curvature bound

$$
|{R m}_{g(t)}|_{g(t)}\leq\frac{C_{1}}{b^{2}}.
$$

This curvature bound will be important in section 11.

Outline of section 8. In this section we prove various local and global compactness
results for U(2)-invariant Ricci flows in the class of metrics *I.* To state the results
we need to first introduce the following notation for a U(2)-invariant Riemannian
manifold (*M,g):*

$$
U(2)
$$

$$
(M,g)
$$

• Let Σ<sub>p</sub> ⊂ M denote the orbit of p under the U(2)-action.
{ ∣}

$$
\Sigma_{p}\subset M
$$

*•* Let

$$
C_{g}(p,r):=\left\{q\in M\;\middle|\;d_{g}(q,\Sigma_{p})<r\right\}
$$

---

One sees that C<sub>g</sub>(p,r) is the tubular neighborhood of ‘radial width’ r of the orbit
Σ<sub>p</sub> of p under the U(2)-action. See Definition 2.1 for more details.

$$
C_{g}(p,r)
$$

$$
r
$$

$$
\Sigma_{p}
$$

$$
U(2)
$$

$$
p
$$

The main result of this section is Theorem 8.1, which states under which conditions a sequence of U(2)-invariant Ricci flows of the form (C<sub>g</sub> <sub>(0)</sub>(p<sub>i</sub>,r),g<sub>i</sub>(t),p<sub>i</sub>),
i
*t ∈* [−∆t,0], *∆t* > *0,r* > 0, subsequentially converges, in the Cheeger-Gromov
sense, to a limiting U(2)-invariant Ricci flow (*C*<sub>∞</sub>*,g*<sub>∞</sub>(*t),p*<sub>∞</sub>), *t ∈* [−∆,0]. Amongst
other conditions, we require that g<sub>i</sub>(t) is

$$
\left(C_{g_{i}(0)}(p_{i},r),g_{i}(t),p_{i}\right)
$$

$$
t\in[-\Delta t,0],\Delta t>0,r>0
$$

$$
U(2)_{\mathrm{I}}
$$

$$
\left(\mathcal{C}_{\infty},g_{\infty}(t),p_{\infty}\right),t\in[-\Delta,0]
$$

$$
g_{i}(t)
$$

• κ-non-collapsed at some scale ρ > 0 at the point (p<sub>i</sub>,0) in spacetime

$$
\rho>0
$$

$$
(p_{i},0)
$$

*•* In the class *I*

$$
\mathcal{I}
$$

• Normalized such that b(p<sub>i</sub>,0) = 1

$$
b(p_{i},0)=1
$$

• Of uniformly bounded curvature in C<sub>g</sub> <sub>(0)</sub>(p<sub>i</sub>,r) × [−∆t,0]
i

$$
C_{g_{i}(0)}(p_{i},r)\times[-\Delta t,0]
$$

We also show that after choosing suitable coordinates the warping functions of the
metrics g<sub>i</sub>(t) subsequentially converge to the corresponding warping functions of
*g*<sub>∞</sub>(t). The compactness result of Theorem 8.1 is used frequently throughout the
paper, especially its variation, stated in Proposition 8.3.

$$
g_{i}(t)
$$

$$
g_{\infty}(t)
$$

Outline of section 9. The main goal of this section is to constrain the geometry of
ancient Ricci flows (M<sub>k</sub>,g(t)), k ∈ N, t ∈ (−∞,0] in the class of metrics I that are
*κ*-non-collapsed at all scales. This is achieved by proving that various scale-invariant
inequalities hold. For instance, in Theorem 9.1 we prove that three inequalities of
the form T<sub>(α,β,γ)</sub> ≥ 0, as in introduced in the outline of section 5 above, hold on such
ancient flows. Furthermore, we prove in Theorem 9.2 that an ancient Ricci flow on
*M<sub>2</sub>* in *I* which is K¨ahler with respect to *J<sub>1</sub>,* i.e. *y* = 0 everywhere, is stationary
and homothetic to the Eguchi-Hanson space. This result will be used in section 10,
where we construct an eternal blow-up limit of a Ricci flow on *M<sub>2</sub>* that is homothetic
to the Eguchi-Hanson space.

$$
\left(M_{k},g(t)\right),k\in\mathbb{N},t\in(-\infty,0]
$$

$$
T_{(\alpha,\beta,\gamma)}\geq0
$$

$$
9.2
$$

$$
J_{1},
$$

$$
M_{2}
$$

$$
y=0
$$

$$
M_{2}
$$

The proof of these theorems is via a contradiction/compactness argument
frequently employed throughout the paper. We briefly sketch the method here:
Assume we want to prove that a scale-invariant inequality T ≥ 0 holds on M<sub>k</sub> ×
(−∞,0]. We argue by contradiction and assume that

$$
T\geq0
$$

$$
M_{k}\times
(-\infty,0]
$$

$$
\iota:=\operatorname*{i n f}_{M_{k}\times(-\infty,0]}T<0.
$$

We then take a sequence of points (p<sub>i</sub>,t
*i →∞,* and consider the dilated metrics
(

<sub>i</sub>) in spacetime such that T (p<sub>i</sub>,t<sub>i</sub>) → ι as
)

$$
(p_{i},t_{i})
$$

$$
T(p_{i},t_{i})\rightarrow\iota
$$

$$
i\to\infty
$$

$$
g_{i}(t)=\frac{1}{b(p_{i},t_{i})^{2}}g\left(t+t_{i}b(p_{i},t_{i})^{2}\right),\quad t\in[-\Delta t,0],
$$

0. By the
Ricci flows (*C*
(*C*<sub>∞</sub>*,g*<sub>∞</sub>(*t),p*<sub>∞</sub>

on the tubular neighborhoods C<sub>g</sub> <sub>(0)</sub>(p<sub>i</sub>,
i
compactness results of
<sub>g</sub> <sub>(0)</sub>(p<sub>i</sub>, <sub>2</sub><sup>1</sup>),g<sub>i</sub>(t),p<sub>i</sub>), [−∆t,
i
), [−∆t,0], where

<sub>2</sub><sup>1</sup>) (see Definition 2.1) for some small ∆t >
section 8, in particular Proposition 8.3, the
0], subsequentially converges to a Ricci flow

$$
C_{g_i(0)}(p_i,\frac{1}{2})
$$

$$
\Delta t>
$$

$$
\left(C_{g_{i}(0)}\left(p_{i},\frac{1}{2}\right),g_{i}(t),p_{i}\right),[-\Delta t,0]
$$

$$
\left(\mathcal{C}_{\infty},g_{\infty}(t),p_{\infty}\right),\left[-\Delta t,0\right]
$$

$$
T(p_{\infty},0)=\inf_{\mathcal{C}_{\infty}\times[-\Delta t,0]}T=\iota<0
$$ by the scale invariance of *T.* If, however, the evolution equation of *T* precludes
a negative infimum from being attained, we have arrived at a contradiction and
proven the desired result.

Outline of section 10. The goal of this section is to prove Theorem 10.1, which
states that a Ricci flow (M<sub>k</sub>,g(t)), k ≥ 2, starting from an initial metric g(0) ∈I
with sup<sup>p∈M</sup>*b(p,0*) < *∞* encounters a Type II singularity in finite time at the
k
tip of M<sub>k</sub> as the area of S<sup>2</sup><sub>o</sub> decreases to zero. In the k = 2 case we show that
such a singularity possesses a blow-up limit that is stationary and homothetic to
the Eguchi-Hanson space. We do not further investigate the *k ≥* 3 case, however
the author conjectures that their blow-up limits are homothetic to the steady Ricci
solitons found in [A17].

$$
(M_{k},g(t)),k\geq2
$$

$$
g(0)\in\mathcal{I}
$$

$$
\mathrm{p}_{p\in M_k}b(p,0)<\infty
$$

$$
k=2
$$

$$
S_{o}^{2}
$$

$$
M_{k}
$$

$$
k\geq3
$$

The proof is carried out in multiple steps. First we show in Lemma 10.5 that *g(t*)
encounters a singularity in finite time T<sub>sing</sub> ∈ (0, ∞) and b(o,t) → 0 as t → T<sub>sing</sub>.
This shows that the two-sphere S<sup>2</sup><sub>o</sub> at the tip of M<sub>k</sub> collapses to a point in finite
time and thereby produces a singularity.

$$
g(t)
$$

$$
T_{s i n g}\in(0,\infty)
$$

$$
b(o,t)\to0
$$

$$
t\rightarrow T_{s i n g}.
$$

$$
M_{k}
$$

$$
S_{o}^{2}
$$

In the second step, we rely on the results of section 6 to show that a blow-up
limit around o ∈ S<sup>2</sup><sub>o</sub> cannot be a shrinking Ricci soliton when k ≥ 2. As all Type I
singularities are modeled on shrinking Ricci solitons we deduce that the singularity
is of Type II.

$$
o\in S_{o}^{2}
$$

$$
k\geq2
$$

In the third step we borrow a trick due to Hamilton to pick a sequence of times
t<sub>i</sub> → T<sub>sing</sub> such that the following holds: Take the rescaled metrics
() [)

$$
t_{i}\rightarrow T_{\textit{s i n g}}
$$

$$
g_{i}(t)=\frac{1}{b(o,t_{i})^{2}}g\left(t_{i}+b^{2}(o,t_{i})t\right),\quad t\in\big[-b(o,t_{i})^{-2}t_{i},b(o,t_{i})^{-2}\left(T_{s i n g}-t_{i}\right)\big),
$$

where we recall that *o ∈ S*
eternal Ricci flow (*M*<sub>∞</sub>*,g*<sub>∞</sub>(

<sub>o</sub><sup>2</sup>. Then (M<sub>k</sub>,g<sub>i</sub>(t),o) subsequentially converges to an
t),o), t ∈ (−∞, ∞), where M∞is diffeomorphic to M<sub>k</sub>.

$$
o\in S_{o}^{2}.
$$

$$
(M_{k},g_{i}(t),o)
$$

$$
\left(M_{\infty},g_{\infty}(t),o\right),t\in\left(-\infty,\infty\right)
$$

$$
M_{\infty}
$$

$$
M_{k}
$$

In the final step we analyze the geometry of *M*<sub>∞</sub>when *k* = 2. It turns out that
for the choice of times t<sub>i</sub> it follows that

$$
M_{\infty}
$$

$$
t_{i}
$$

$$
k=2
$$

$$
\partial_{t}b(o,0)=\bar{0}
$$

on *M*<sub>∞</sub>background. By the evolution equation (1.5) of *b* at *o* this implies

$$
M_{\infty}
$$

$$
y_{s}(o,0)=0.
$$

Applying a strong maximum principle we deduce that *y* = 0 everywhere. By the
results of section 9 it then follows that *g*<sub>∞</sub>(t) is stationary and homothetic to the
Eguchi-Hanson metric.

$$
g_{\infty}(t)
$$

$$
y=0
$$

We mention here that the *k* = 2 case of Theorem 10.1 is superseded by Corollary
11.2 of Theorem 11.1. However, since the proof of Theorem 10.1 is simpler we
present it here.

Outline of section 11. The goal of this section is to show that an ancient Ricci flow
(*M<sub>2</sub>,g(t)),t ∈* (−∞,0], which is *κ*-non-collapsed at all scales and satisfies *g(t*) *∈I,*
is stationary and homothetic to the Eguchi-Hanson space. The most important

$$
(M_{2},g(t)),t\in(-\infty,0]
$$

$$
g(t)\in\mathcal{I}
$$ consequence of this is that in Theorem 10.1 in fact *any* blow-up of the singularity
forming at the tip of *M<sub>2</sub>* is homothetic to the Eguchi-Hanson space, whereas we had
previously only proven that there exists *a* blow-up sequence that converges to the
Eguchi-Hanson space.

$$
M_{2}
$$

The proof idea, which we call successive constraining, is to find a continuously
varying family of preserved inequalities Z<sub>θ</sub> ≥ 0, θ ∈ [0,1], for which Z<sub>0</sub> ≥ 0 on
*M<sub>2</sub> ×* (*−∞,0*] implies that *g(t*) is homothetic to the Eguchi-Hanson metric. For our
choice of conserved inequalities Z<sub>θ</sub> ≥ 0, θ ∈ [0,1], it follows from the work of section
9 that *Z<sub>1</sub> ≥* 0 on *M<sub>2</sub> ×* (−∞,0]. Then we deform the inequality *Z<sub>1</sub> ≥* 0 along the
path Z<sub>θ</sub> ≥ 0, θ ∈ [0,1], to the inequality Z<sub>0</sub> ≥ 0 with help of the strong maximum
principle applied to the evolution equation of Z<sub>θ</sub>. This allows us to deduce that g(t)
is stationary and homothetic to the Eguchi-Hanson space. In subsection 11.1 we
give a more detailed outline of the proof of Theorem 11.1.

$$
Z_{\theta}\geq0,\theta\in[0,1]
$$

$$
M_{2}\times(-\infty,0]
$$

$$
Z_{0}\geq0
$$

$$
g(t)
$$

$$
Z_{\theta}\geq0,\theta\in[0,1]
$$

$$
Z_{1}\geq0
$$

$$
M_{2}\times(-\infty,0]
$$

$$
Z_{1}\geq0
$$

$$
Z_{0}\geq0
$$

$$
Z_{\theta}\geq0,\theta\in[0,1]
$$

$$
Z_{\theta}
$$

$$
g(t)
$$

Outline of section 12. The main result of this section is Theorem 12.1, which
characterizes all the possible blow-up limits of a Ricci flow *(M<sub>2</sub>,g(t))* starting from
an initial metric g(0) *∈I* with *supp∈M<sub>2</sub>b(p,0*) < *∞.* We show that the only possible
blow-up limits are (i) the Eguchi-Hanson space, (ii) the flat orbifold R<sup>4</sup>/Z<sub>2</sub>, (iii) the
4d Bryant soliton quotiented by Z<sub>2</sub> and (iv) the shrinking cylinder R × RP <sup>3</sup>.

$$
\left(M_{2},g(t)\right)
$$

$$
g(0)\in\mathcal{I}
$$

$$
\sup_{p\in M_{2}}b(p,0)<\infty
$$

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

$$
\mathbb{Z}_2
$$

$$
\mathbb{R}\times\mathbb{R}P^{3}
$$

Below we give a brief outline of the proof of Theorem 12.1: Assume we are given
a sequence of points (p<sub>i</sub>,t<sub>i</sub>) in spacetime with b(p<sub>i</sub>,t<sub>i</sub>) → 0. Consider the rescaled
metrics
<u>1</u>

$$
(p_{i},t_{i})
$$

$$
b(p_{i},t_{i})\to0
$$

$$
g_{i}(t)=\frac{1}{b(p_{i},t_{i})^{2}}g\big(t_{i}+b(p_{i},t_{i})^{2}t\big),\quad t\in[-b(p_{i},t_{i})^{-2}t_{i},0].
$$

By passing to a subsequence we may assume that either

$$
\begin{aligned}(I)\sup_{i}\frac{b(p_{i},t_{i})}{b(o,t_{i})}<\infty\quad or\quad(II)\lim_{i\to\infty}\frac{b(p_{i},t_{i})}{b(o,t_{i})}=\infty.\end{aligned}
$$

By section 11 we already know that in case (I) we converge to the Eguchi-Hanson
space. Therefore we only need to investigate the behavior in case (II), i.e. at scales
larger than the forming Eguchi-Hanson singularity. For this we need to divide case
(II) into three subcases: By passing to a subsequence we may assume that

$$
\mathrm{\left(I I.a\right)}b_{s}\big(p_{i},t_{i}\big)\to1\mathrm{~o r~}\mathrm{\left(I I.b\right)}b_{s}\big(p_{i},t_{i}\big)\to\eta\in\big(0,1\big)\mathrm{~o r~}\mathrm{\left(I I.c\right)}b_{s}\big(p_{i},t_{i}\big)\to0.
$$

(II.a)

For (II.a) and (II.c) we show in Lemma 12.9 and Lemma 12.6 that (M<sub>2</sub>,g<sub>i</sub>(t),p<sub>i</sub>)
subsequentially converges to the flat orbifold R<sup>4</sup>/Z<sub>2</sub> and the shrinking cylinder *R×*
RP <sup>3</sup>, respectively. The proof of these lemmas is relatively easy. Proving in Lemma
12.8 that the blow-up limit in case (II.b) is homothetic to the 4d Bryant soliton
quotiented by Z<sub>2</sub> is trickier. Here we rely on Lemma 12.3, which characterizes the
geometry of the high curvature regions of *g(t*) at distance scales larger than the
Eguchi-Hanson singularity away from the tip of *M<sub>2</sub>.* In subsection 12.1 we give a
more detailed outline of the proof of Theorem 12.1.

$$
(M_{2},g_{i}(t),p_{i})
$$

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

$$
P^{3}
$$

$$
\mathbb{Z}_2
$$

$$
g(t)
$$

$$
M_{2}
$$

---

1.6. Further questions and conjectures. In this section we collect some conjectures and further questions that arise from our results. The central open question
remaining in this paper is whether or not the Eguchi-Hanson singularity of Theorem
12.1 is isolated. By isolated we mean that the only blow-up limits are the Eguchi-
Hanson space and its asymptotic cone, the flat orbifold R<sup>4</sup>/Z<sub>2</sub>. We conjecture that

$$
\mathbb{R}^4/\mathbb{Z}_2
$$

Conjecture 1. *The Eguchi-Hanson singularity of Theorem 12.1 is not isolated and*
*all four blow-up limits (i)-(iv) occur. In particular, it is accompanied by a Type I*
singularity modeled on the shrinking cylinder R × S<sup>3</sup>/Z<sub>2</sub>.

$$
(i)-(iv)
$$

$$
\mathbb{R}\times S^{3}/\mathbb{Z}_{2}
$$

An affirmative answer to this conjecture would provide evidence for a longstanding
conjecture in Ricci flow stating that a Type II singularity is always accompanied
by a Type I singularity in its vicinity. The author has an argument showing that if
the Eguchi-Hanson singularity were isolated, the curvature would blow up at a rate
faster than (T<sub>sing</sub> − t)<sup>−λ</sup>, where λ is any positive constant.

$$
\lambda
$$

$$
(T_{s i n g}-t)^{-\bar{\lambda}}
$$

Although we have not analyzed the blow-up limits of a U(2)-invariant Ricci flow
(M<sub>k</sub>,g(t)), t ∈ [0,T<sub>sing</sub>), in the k 6= 2 case, we believe that for each k ∈ N there exists
a unique blow-up limit of the singularity arising from the collapse of the two sphere
S<sup>2</sup><sub>o</sub> at the tip of M<sub>k</sub>. In collaboration with Jon Wilkening the author has already
conducted numerical simulations confirming this, and a paper is in preparation
[AW19]. In particular, we conjecture that

$$
U(2)
$$

$$
(M_{k},g(t)),t\in[0,T_{\mathrm{sing}})
$$

$$
k\neq2
$$

$$
k\in\mathbb{N}
$$

$$
S_{o}^{2}
$$

$$
M_{k}
$$

Conjecture 2. Let (M<sub>k</sub>,g(t)) be a U(2)-invariant Ricci flow encountering a singularity at the tip of M<sub>k</sub>, as the area of S<sup>2</sup><sub>o</sub> decreases to zero. Then the following
*picture holds:*

$$
a\ U(2)
$$

$$
\left(M_{k},g(t)\right)
$$

$$
M_{k}
$$

$$
S_{o}^{2}
$$

| k | Blow-up limit at \(o \in S_{o}^{2}\) | Type | Isolated |
| --- | --- | --- | --- |
| 1 | FIK shrinker | Type I | Yes |
| 2 | Eguchi-Hanson space | Type II | No |
| ≥ 3 | Steady Ricci solitons of [A17] | Type II | No |

$$
\overline{o\in S_{o}^{2}}
$$

$$
Type
$$

$$
\overline{Type I}
$$

$$
\geq3
$$

By isolated we mean that the singularity is not accompanied by a Type I singularity in its vicinity. For instance, in the case *k ≥* 2 we expect a singularity caused
by the collapse of the two-sphere S<sup>2</sup><sub>o</sub> at the tip of M<sub>k</sub> to always be accompanied by
a Type I singularity modeled on the shrinking cylinder R× S<sup>3</sup>/Z<sub>k</sub> and therefore not
to be isolated. If for each *k ≥* 3 the corresponding steady Ricci soliton of [A17]
is in fact the unique blow-up limit at the tip of M<sub>k</sub>, then these singularities are
necessarily accompanied by a Type I singularity modeled on S<sup>3</sup>/Z<sub>k</sub>, because these
solitons are asymptotically cylindrical.

$$
k\geq2
$$

$$
S_{o}^{2}
$$

$$
M_{k}
$$

$$
\mathbb{R}\times S^{3}/\mathbb{Z}_{k}
$$

$$
k\geq3
$$

$$
M_{k}
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

Another interesting question is the following:

Question 1. *Can the Eguchi-Hanson singularity occur on a closed four dimensional
manifold?*

The author conjectures that the answer is yes, however only non-generically. The
∼
simplest model on which to investigate this question is M = M<sub>2</sub>#<sub>RP</sub> 3M<sub>2</sub> = S<sup>2</sup> ×

$$
M=M_{2}\#_{\mathbb{R}P^{3}}M_{2}\cong S^{2}\times
$$

---

*S<sup>2</sup>* equipped with an U(2)-invariant metric. One could carry out a construction
as follows: Vary between an initial metric that encounters a R *× RP<sup>3</sup>* neckpinch
singularity and an initial metric that leads to the collapse of one of the *S<sup>2</sup>* factors
of *M.* On the path between these two metrics there should be a metric whose Ricci
flow evolution forms an Eguchi-Hanson singularity in finite time.

$$
S^{2}
$$

$$
U(2)
$$

$$
\mathbb{R}\times\mathbb{R}P^{3}
$$

$$
S^{2}
$$

This paper has not touched upon the behavior of a general non-U(2)-invariant
metric on TS<sup>2</sup>. A first question would be:

$$
TS^{2}
$$

Question 2. *Does the picture of Theorem 12.1 also hold for Ricci flows starting
from non*-U(2)-*invariant perturbations of asymptotically cylindrical* U(2)-*invariant*
metrics on TS<sup>2</sup>?

$$
\dot{T}\dot{S}^{2}?
$$

And a final big question mark is the following:

Question 3. *Are there other four dimensional Ricci flat ALE spaces that can occur
as blow-up limits in Ricci flow?*

So far all known Ricci flat ALE spaces in four dimensions are hyperk¨ahler and
it is not known whether non-hyperk¨ahler examples exist. Kronheimer classified all
hyperk¨ahler ALE spaces [KronI89], [KronII89]. These spaces have one end that is
asymptotic to the cone R<sup>4</sup>/Γ, where Γ *⊂* U(2) is a certain finite group — a binary
dihedral, tetrahedral, octahedral or icosahedral group. In the case that Γ = Z<sub>k</sub> is
cyclic, Gibbons and Hawking [GH78], [GH79] discovered a closed form (3k *−* 6)-
parameter family of such metrics. In the physics literature these metrics are known
as multi-center Eguchi Hanson spaces. It would be interesting to see whether the
results of this paper can be generalized to prove the existence of singularities modeled
on these spaces.

$$
\mathbb{R}^4/\Gamma
$$

$$
\Gamma\subset U(2)
$$

$$
\Gamma=\mathbb{Z}_k
$$

$$
(3k-6)-
$$

1.7. Acknowledgments. The author would like to thank his PhD advisors Richard
Bamler and Jon Wilkening for their constant support and encouragement. This work
was supported by a GSR fellowship, which was funded by NSF grant DMS-1344991.

## 2. Preliminaries

2.1. Notation. Here we collect some of the notation used throughout the paper.

• M<sub>k</sub>, k ∈ N: a manifold diffeomorphic to the blow-up of C<sup>2</sup>/Z<sub>k</sub>, k ≥ 1, at the
origin.

$$
M_{k},k\in\mathbb{N};
$$

$$
\mathbb{C}^2/\mathbb{Z}_k,k\geq1
$$

• S<sub>o</sub><sup>2</sup>: the two-sphere added during the blow-up of C<sup>2</sup>/Z<sub>k</sub>.

$$
S_{o}^{2};
$$

$$
\mathbb{C}^2/\mathbb{Z}_k
$$

• ξ: the radial coordinate on M<sub>k</sub> or the parametrization of the R>0factor in
the product R>0× S<sup>3</sup>/Z<sub>k</sub> ⊂ M<sub>k</sub>.

$$
M_{k}
$$

$$
\xi\mathrm{:}
$$

$$
\mathbb{R}_{>0}
$$

$$
\mathbb{R}_{>0}\times S^{3}/\mathbb{Z}_{k}\subset M_{k}
$$

• o: a fixed point on S<sub>o</sub><sup>2</sup>.

$$
S_{o}^{2}.
$$

$$
O\colon
$$

• Σ<sub>p</sub>: denotes the orbit of p under the U(2)-action. For instance if p ∈ S<sup>2</sup><sub>o</sub> ⊂ M<sub>k</sub>
∼
we have Σ<sub>p</sub> = S<sup>2</sup><sub>o</sub> and when p ∈ M<sub>k</sub> \ S<sup>2</sup><sub>o</sub> we have Σ<sub>p</sub> = S<sup>3</sup>/Z<sub>k</sub>.

$$
\Sigma_{p}:
$$

$$
U(2)
$$

$$
p\in S_{o}^{2}\subset M_{k}
$$

$$
\Sigma_{p}=S_{o}^{2}
$$

$$
p\in M_{k}\setminus S_{o}^{2}
$$

$$
\Sigma_{p}\cong S^{3}/\mathbb{Z}_{k}
$$

• s: the geodesic distance from S<sub>o</sub><sup>2</sup>, and often considered as a function of ξ and
*t.*

$$
S_{o}^{2}
$$

$$
\xi
$$

$$
t.
$$

*•* origin: refers to the point *o.*

*• g:* a metric of the form (2.2) or (2.3) unless otherwise stated

$$
g\dot{}
$$

---

• d<sub>g</sub>: the metric distance induced by g.

$$
d_{g}\text{:}
$$

*•* g(t): a time dependent family of metrics of the form (2.2) or (2.3).

$$
g(t)
$$

*• u, a, b:* the warping functions of the metric (2.2). Depending on context
these will be considered as functions of (*ξ,t), (s,t)* or (*p,t),* where *p* is a
point on M<sub>k</sub>.

$$
u,\;a,\;b;
$$

$$
(p,t)
$$

$$
M_{k}
$$

• Q := <sup>a</sup><sub>b</sub>.

$$
\begin{array}{l}Q:=\frac{a}{b}.\end{array}
$$

• B<sub>g</sub>(p,r): the ball centered at p of radius r with respect to the metric g.

$$
B_{g}(p,r)
$$

$$
g
$$

• C<sub>g</sub>(p,r), r > 0: the subset of a cohomogeneity one U(2)-invariant Riemannian manifold *(M,g)* defined by
{ ∣}
∣

$$
C_{g}(p,r),r>0;
$$

$$
C_{g}(p,r)=\left\{q\in M\Big|\;d_{g}(q,\Sigma_{p})<r\right\}.
$$

The set C<sub>g</sub>(p,r) is diffeomorphic to either M<sub>k</sub> or R × S<sup>3</sup>/Z<sub>k</sub>.

$$
C_{g}(p,r)
$$

$$
M_{k}
$$

$$
\mathbb{R}\times S^{3}/\mathbb{Z}_{k}
$$

$$
\overline{C}_{g}(p,r)
$$

$$
C_{g}(p,r)
$$

• C<sub>g</sub>(p,r): the closure of C<sub>g</sub>(p,r).

• T<sub>sing</sub>: the singular time of a Ricci flow.

$$
T_{sign}:
$$

∞
• CU<sub>(2)</sub>(M<sub>k</sub> × [0,T]): The space of smooth U(2)-invariant functions u : M<sub>k</sub> ×
[0,T] *→* R.

$$
C_{U(2)}^{\infty}(M_k\times[0,T])
$$

$$
u:M_{k}\times
\left[0,\overbrace{T}\right]\rightarrow\mathbb{R}
$$

*• x,y:* K¨ahler quantities introduced in section 4.

$$
x,y:
$$

2.2. The manifold and metric. For k ∈ N let M<sub>k</sub> be diffeomorphic to the blowup of C<sup>2</sup>/Z<sub>k</sub> at the origin. Denote by S<sup>2</sup><sub>o</sub> the embedded two-sphere in M<sub>k</sub> stemming
from the blow-up, and fix some point o for ‘origin’ on S<sub>o</sub><sup>2</sup>.

$$
k\in\mathbb{N}
$$

$$
M_{k}
$$

$$
\mathbb{C}^2/\mathbb{Z}_k
$$

$$
S_{o}^{2}
$$

$$
M_{k}
$$

$$
S_{o}^{2}
$$

We now describe the U(2)-invariant metrics on M<sub>k</sub>, k ≥ 1, studied in this paper.
Let *z<sub>1</sub>,z<sub>2</sub>* be the standard coordinates on C<sup>2</sup> and let U(2) act on C<sup>2</sup> by left multiplication. This action descends to M<sub>k</sub>, k ∈ N. Note that M<sub>k</sub> can be seen as the total
space of the complex line bundle *O(−k*) via

$$
U(2)
$$

$$
M_{k},k\geq1
$$

$$
\mathbb{C}^2
$$

$$
z_{1},z_{2}
$$

$$
U(2)
$$

$$
\mathbb{C}^2
$$

$$
M_{k},k\in\mathbb{N}
$$

$$
M_{k}
$$

$$
O(-k)
$$

$$
\pi:M_{k}\longrightarrow S_{o}^{2}
$$

$$
\left(z_{1},z_{2}\right)\mapsto\left[z_{1},z_{2}\right]
$$

∼
Then U(2) = U(1) × SU(2) acts on M<sub>k</sub> in the following way: The action of U(1)
rotates the fibres of π and SU(2) acts on the base S<sup>2</sup><sub>o</sub> via rotations. Now introduce
the Hopf coordinates

$$
U(2)\cong U(1)\times SU(2)
$$

$$
M_{k}
$$

$$
U(1)
$$

$$
\pi
$$

$$
SU(2)
$$

$$
S_{o}^{2}
$$

$$
z_{1}=\xi\sin\eta e^{i\left(\psi+\phi\right)}=x_{1}+i y_{1}
$$

$$
z_{2}=\xi\cos\eta e^{i\left(\psi-\phi\right)}=x_{2}+i y_{2}
$$

on C<sup>2</sup><sub>∗</sub>, where ξ > 0, η ∈ [0,π/2] and ψ,φ ∈ [0,2π). These coordinates descend to M<sub>k</sub>.
In particular, this allows us to endow M<sub>k</sub> with the radial coordinate ξ : M<sub>k</sub> → R≥<sub>0</sub>,
by continuously extending ξ to S<sup>2</sup><sub>o</sub> by taking ξ = 0 on S<sub>o</sub><sup>2</sup>. Note that the coordinate
ξ is only smooth on M<sub>k</sub> \ S<sub>o</sub><sup>2</sup>.

$$
\mathbb{C}_{*}^{2}
$$

$$
\xi>0,\eta\in[0,\pi/2]
$$

$$
\psi,\phi\in[0,2\pi)
$$

$$
M_{k}
$$

$$
\xi:M_{k}\rightarrow\mathbb{R}_{\geq0}
$$

$$
M_{k}
$$

$$
\xi
$$

$$
S_{o}^{2}
$$

$$
\xi=0
$$

$$
\xi
$$

$$
M_{k}\setminus S_{o}^{2}
$$

$$
S_{o}^{2}
$$

A computation shows that the standard euclidean metric

$$
g_{e u c l}=d x_{1}^{2}+d y_{1}^{2}+d x_{2}^{2}+d y_{2}^{2}
$$

may be written as

$$
g_{e u c l}=d\xi^{2}+\xi^{2}\left(d\eta^{2}+\sin^{2}(2\eta)d\phi^{2}+\left[d\psi-\cos(2\eta)d\phi\right]^{2}\right)
$$ in Hopf coordinates. The 1-form

$$
\omega:=d\psi-\cos(2\eta)d\phi
$$

is dual to the Hopf fibre directions, or equivalently dual to the vector field generated
by the U(1) action. Furthermore

$$
U(1)
$$

$$
d\eta^{2}+\sin^{2}(2\eta)d\phi^{2}
$$

(2.1)

is the pull-back of the Fubini-Study metric g<sub>FS</sub> on CP <sup>1</sup>, normalized to have constant
sectional curvature equal to <sub>4</sub><sup>1</sup>.

$$
g_{FS}
$$

$$
\mathbb{C}P^{1}
$$

$$
\frac{1}{4}
$$

From the above we see that the warped-product metric

(2.2)

$$
g=u(\xi)^{2}d\xi^{2}+a(\xi)^{2}\omega\otimes\omega+b(\xi)^{2}\pi^{*}(g_{F S})
$$

is the most general U(2)-invariant metric on C<sup>2</sup><sub>∗</sub> and descends to a U(2)-invariant
metric on the open dense set C<sup>2</sup><sub>∗</sub>/Z<sub>k</sub> ⊂ M<sub>k</sub>. It will be useful to introduce the change
of coordinates defined by
*ds* = *u(ξ)dξ*

$$
\mathbb{C}_{*}^{2}
$$

$$
U(2)
$$

$$
\mathbb{C}_{*}^{2}/\mathbb{Z}_{k}\subset M_{k}
$$

$$
ds=u(\xi)d\xi
$$

and s = 0 at ξ = 0. Then for p ∈ M<sub>k</sub> the quantity s(p) = d<sub>g</sub>(p,S<sub>o</sub><sup>2</sup>) describes the
radial distance of p from S<sub>o</sub><sup>2</sup>. In these coordinates the metric becomes

$$
s=0
$$

$$
\xi=0
$$

$$
p\in M_{k}
$$

$$
s(p)=d_g(p,S_o^2)
$$

$$
p
$$

$$
S_{o}^{2}
$$

(2.3)

$$
g=d s^{2}+a\big(s\big)^{2}\omega\otimes\omega+b\big(s\big)^{2}\pi^{*}\big(g_{F S}\big),
$$

where in a slight abuse of notation we consider *a* and *b* as functions of *s.* Depending
on the context we will consider *a* and *b* either as functions of *s* or *ξ.*

$$
\xi.
$$

The metric g can be extended to a metric on all of M<sub>k</sub> by taking a(0) = 0 and
b(0) > 0. In other words we shrink the Hopf fibre directions to zero as *s →* 0 or
equivalently as we approach S<sub>o</sub><sup>2</sup>. Note that for every p ∈ S<sub>0</sub><sup>2</sup>

$$
M_{k}
$$

$$
a(0)=0
$$

$$
b(0)>0
$$

$$
s\to0
$$

$$
S_{o}^{2}
$$

$$
p\in S_{0}^{2}
$$

$$
d s^{2}+a(s)^{2}\omega\otimes\omega
$$

is the pull-back of g onto the fibre π<sup>−1</sup>(p).
see that π<sup>−1</sup>(p) is a union of S<sup>1</sup> orbits and
2
π<sup>−1</sup>(p) ⊂ M<sub>k</sub> is parametrized by 0 ≤ ψ <
such an *S<sup>1</sup>* orbit at radial distance *s* from
Because
<u>2π 2π</u>

As U(1) acts on the fibre π<sup>−1</sup>(p), we
*p.* Furthermore, such a *S<sup>1</sup>* orbit in
π
and, by the form of the metric (2.3),
k
S<sup>2</sup><sub>o</sub> has a circumference of length <sup>2π</sup> a(s).
k

$$
\pi^{-1}(p)
$$

$$
U(1)
$$

$$
\pi^{-1}(p)
$$

$$
\pi^{-1}(p)
$$

$$
S^{1}
$$

$$
p.
$$

$$
S^{1}
$$

$$
\pi^{-1}(p)\subset M_{k}
$$

$$
0\leq\psi<\frac{2\pi}{k}
$$

$$
S^{1}
$$

$$
S_{o}^{2}
$$

$$
\frac{2\pi}{k}a(s)
$$

$$
\frac{2\pi}{k}a(s)=\frac{2\pi}{k}a_s(0)s+O(s^2)\ as\ s\to0
$$

we must require that a<sub>s</sub>(0) = k in order to avoid a conical singularity at S<sub>o</sub><sup>2</sup>. This
is how the topology of the manifold enters the analysis of the Ricci flow equation.
Additionally requiring that *a(s*) and *b(s*) can be extended to an odd and even
function, respectively, around *s* = 0 is a sufficient condition for the metric *g* to
be smoothly extendable to all of M<sub>k</sub> [VZ18]. In the rest of the paper all metrics
considered will be of the form (2.2) or equivalently (2.3). In Figure 1 the manifold
M<sub>k</sub> and its metric close to the two sphere S<sup>2</sup><sub>o</sub> is schematically depicted.

$$
a_{s}(0)=k
$$

$$
S_{o}^{2}.
$$

$$
b(s)
$$

$$
s=0
$$

$$
g
$$

$$
M_{k}\ \left[\mathrm{VZ}18\right]
$$

$$
M_{k}
$$

$$
S_{o}^{2}
$$

(M<sub>k</sub>,g), k ∈ N, are cohomogeneity one manifolds, meaning that the generic orbits
of the U(2) action are of codimension 1. The generic orbit is also called the principal
orbit. The non-generic orbits are called non-principal orbits. In the case of M<sub>k</sub> the
principal orbits are diffeomorphic to S<sup>3</sup>/Z<sub>k</sub> and the single non-principal orbit is S<sup>2</sup><sub>o</sub>

$$
\left(M_{k},g\right),k\in\mathbb{N}.
$$

$$
U(2)
$$

$$
M_{k}
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
S_{o}^{2}
$$ s
b(0) a(s)
p π<sup>−1</sup>(p)
S<sup>2</sup><sub>o</sub>

Figure 1. Diagram of the manifold M<sub>k</sub> close to the tip

$$
M_{k}
$$

and of codimension 2. Below we introduce some notation that we frequently employ
throughout the paper:

Definition 2.1. Assume *(M,g)* is a U(2)-invariant cohomogeneity one manifold
with principal orbit S<sup>3</sup>/Z<sub>k</sub> for some fixed k ∈ N and g is a metric of the form (2.3).
Let *p ∈ M* and *r* > 0. Then

$$
(M,g)
$$

$$
U(2)
$$

$$
S^{3}/\mathbb{Z}_{k}
$$

$$
k\in\mathbb{N}
$$

$$
p\in M
$$

$$
r>0
$$

• Let Σ<sub>p</sub> ⊂ M denote the orbit of p under the U(2)-action.
*q ∈ M*

$$
\Sigma_{p}\subset M
$$

$$
U(2)-action
$$

• Let Σ<sup>+</sup><sub>p</sub> be the set of all points
()
∂
with *g τ,˙ ≥* 0.
∂s
{

that can be joined via path *τ* to *p*
}

$$
\Sigma_{p}^{\bar{+}}
$$

$$
q\in M
$$

$$
\begin{array}{l}{\overset{\cdot}{g}\left(\dot{\tau},\frac{\partial}{\partial s}\right)\geq0}\\ \end{array}
$$

*•* Let

$$
C_{g}(p,r):=\left\{q\in M\;\middle|\;d_{g}(q,\Sigma_{p})<r\right\}
$$

*•* Let

$$
C_{g}^{+}(p,r):=\left\{q\in\Sigma_{p}^{+}\mid d_{g}(q,\Sigma_{p})<r\right\}
$$

∼
Note that we have Σ<sub>p</sub> = S<sup>3</sup>/Z<sub>k</sub> if
on a non-principal orbit.

∼
p lies on a principal orbit and Σ<sub>p</sub> = S<sup>2</sup> if p lies

$$
\Sigma_{p}\cong S^{3}/\mathbb{Z}_{k}
$$

$$
\Sigma_{p}\cong S^{2}
$$

2.3. The connection, Laplacian and curvature tensor. We now compute the
connection, Laplacian and curvature tensor for metrics of the form (2.3). To obtain the corresponding expressions for the metric (2.2) use the relation

$$
\frac{\partial}{\partial s}=\frac{1}{u}\frac{\partial}{\partial\xi}.
$$

Take the orthonormal basis

$$
e^{0}=d s\qquad e^{1}=a\left[d\psi-\cos(2\eta)d\phi\right]\qquad e^{2}=b d\eta\qquad e^{3}=b\sin(2\eta)d\phi
$$

of T <sup>∗</sup>M. Let e<sub>i</sub>, i = 1,2,3,4, be the corresponding dual basis of T<sub>∗</sub>M. Define the
connection 1-forms θ<sub>i</sub><sup>j</sup> by ∇e<sub>i</sub> = θ<sub>i</sub><sup>j</sup>e<sub>j</sub> and the curvature 2-forms Ω<sup>j</sup><sub>i</sub> by R(·, ·)e<sub>i</sub> =
Ω<sup>j</sup><sub>i</sub> e<sub>j</sub>. With help of Cartan’s structure equations

$$
T^{*}M
$$

$$
e_{i},i=1,2,3,4
$$

$$
T_{*}M.
$$

$$
\theta_{i}^{j}
$$

$$
\nabla\boldsymbol{e}_{i}=\theta_{i}^{j}\boldsymbol{e}_{j}
$$

$$
\Omega_{i}^{j}
$$

$$
\bar{R}(\cdot,\cdot)e_{i}=
\Omega_{i}^{j}e_{j}
$$

$$
\theta_{i}^{j}=-\theta_{j}^{i}
$$

$$
d e^{i}=-\theta_{j}^{i}\wedge e^{j}
$$

$$
\Omega_{i}^{j}=d\theta_{i}^{j}+\theta_{k}^{j}\wedge\theta_{i}^{k}
$$

one can compute the connection 1-forms and curvature 2-forms. First note that

$$
de^{0}=0
$$

$$
d e^{1}=\frac{a_{s}}{a}e^{0}\wedge e^{1}+\frac{2a}{b^{2}}e^{2}\wedge e^{3}
$$

$$
de^{2}=\frac{b_{s}}{b}e^{0}\wedge e^{2}
$$

$$
d e^{3}=\frac{b_{s}}{b}e^{0}\wedge e^{3}+\frac{2}{b}\cot(2\eta)e^{2}\wedge e^{3}.
$$

Hence we obtain the connection 1-forms θ<sub>ji</sub>:

$$
\theta_{j}^{i}
$$

$$
\theta_{0}^{1}=\frac{a_{s}}{a}e^{1}\quad\theta_{2}^{1}=\frac{a}{b^{2}}e^{3}
$$

$$
\theta_{0}^{2}=\frac{b_{s}}{b}e^{2}\quad\theta_{3}^{2}=-\frac{a}{b^{2}}e^{1}-\frac{2}{b}\cot(2\eta)e^{3}
$$

$$
\theta_{0}^{3}=\frac{b_{s}}{b}e^{3}\quad\theta_{1}^{3}=\frac{a}{b^{2}}e^{2}
$$

Therefore

$$
\nabla_{e_{0}}e_{0}=0\qquad\nabla_{e_{1}}e_{1}=-\frac{a_{s}}{a}e_{0}\qquad\nabla_{e_{2}}e_{2}=-\frac{b_{s}}{b}e_{0}\qquad\nabla_{e_{3}}e_{3}=-\frac{b_{s}}{b}e_{0}
$$

from which we can derive the expression for the Laplacian of a U(2)-symmetric
function f (s) on M<sub>k</sub>.
()

$$
f(s)
$$

$$
M_{k}
$$

$$
\Delta f=\sum_{i=0}^{3}\nabla_{e_{i},e_{i}}^{2}f=f_{ss}+\left(\frac{a_{s}}{a}+2\frac{b_{s}}{b}\right)f_{s}.
$$

(2.4)

Finally, we may compute the components

$$
R_{i j k l}=g\left(R\left(e_{k},e_{l}\right)e_{j},e_{i}\right).
$$ of the curvature tensor. Below we list its non-zero components

$$
R_{0101}=-\frac{a_{ss}}{a}=K_1
$$

$$
R_{0202}=-\frac{b_{ss}}{b}=K_2
$$

$$
R_{0303}=-\frac{b_{ss}}{b}=K_3
$$

$$
R_{0123}=-\frac{2}{b^{2}}\left(a_{s}-Q b_{s}\right)=M_{1}
$$

$$
R_{0231}=\frac{1}{b^{2}}\left(a_{s}-Q b_{s}\right)=M_{2}
$$

$$
R_{0312}=\frac{1}{b^{2}}\left(a_{s}-Q b_{s}\right)=M_{3}
$$

$$
R_{1212}=\frac{a^2}{b^4}-\frac{a_s b_s}{ab}=H_{12}
$$

$$
R_{2323}=\frac{4}{b^2}-3\frac{a^2}{b^4}-\left(\frac{b_s}{b}\right)^2=H_{23}
$$

$$
R_{3131}=\frac{a^{2}}{b^{4}}-\frac{a_{s}b_{s}}{a b}=H_{31}.
$$

All other components are either determined by the standard symmetries of the
curvature tensor or are zero.

2.4. The Ricci flow equation. With help of the above list of curvature components one can check that the Ricci tensor is diagonal and hence the form of the
metric (2.2) is preserved by Ricci flow. Allowing the warping functions *a, b* and *p*
to vary in time, the Ricci flow equation (1.1) in *(ξ,t)* coordinates can be expressed
as a system of coupled parabolic equations in *a, b* and *u.*
()
()

(2.5)

$$
\partial_{t}u=\frac{1}{a}\partial_{\xi}\left(\frac{a_{\xi}}{u}\right)+\frac{2}{b}\partial_{\xi}\left(\frac{b_{\xi}}{u}\right)
$$

(2.6)

$$
\partial_{t}a=\frac{1}{u}\partial_{\xi}\left(\frac{a_{\xi}}{u}\right)-2\frac{a^{3}}{b^{4}}+2\frac{a_{\xi}b_{\xi}}{b u^{2}}
$$

(2.7)

$$
\partial_{t}b=\frac{1}{u}\partial_{\xi}\left(\frac{b_{\xi}}{u}\right)-\frac{4}{b}+2\frac{a^{2}}{b^{3}}+\frac{a_{\xi}b_{\xi}}{a u^{2}}+\frac{b_{\xi}^{2}}{b u^{2}}
$$

Define the time dependent radial distance function *s* = *s(ξ,t*) by

$$
s=s(\xi,t)
$$

$$
d s=u(\xi,t)d\xi
$$

Then

(2.8)

$$
s(\xi,t)=\int_{0}^{\xi}u(\xi,t)\mathrm{d}\xi
$$ and

(2.9)

$$
\frac{\partial}{\partial s}=\frac{1}{u}\frac{\partial}{\partial\xi}.
$$

Furthermore the commutation relation

$$
\left[\partial_{t},\partial_{s}\right]=-\frac{\partial_{t}u}{u}\partial_{s}
$$

holds. In terms of *s* we can use (2.9) to rewrite the Ricci flow equation in a slightly
simpler form

(2.10)

$$
\frac{\partial_{t}u}{u}=\frac{a_{ss}}{a}+2\frac{b_{ss}}{b}
$$

(2.11)

$$
\partial_{t}a=a_{ss}-2\frac{a^{3}}{b^{4}}+2\frac{a_{s}b_{s}}{b}
$$

(2.12)

$$
\partial_{t}b=b_{s s}-\frac{4}{b}+2\frac{a^{2}}{b^{3}}+\frac{a_{s}b_{s}}{a}+\frac{b_{s}^{2}}{b}.
$$

Note that the dependence of the right hand side of this system of equations on *ξ* is
hidden in the variable *s* = *s(ξ,t).* However we can write the equations in terms of
*(s,t)* by introducing the functions

$$
\xi
$$

$$
s=s(\xi,t)
$$

$$
\begin{aligned}\tilde{a}(s,t)&=a(\xi,t),\\\tilde{b}(s,t)&=b(\xi,t).\end{aligned}
$$

and noting that

$$
\partial_{t}a\big|_{\xi}=\partial_{t}\tilde{a}\big|_{s}+\partial_{s}\tilde{a}\big|_{t}\frac{\partial s}{\partial t}\big|_{\xi}
$$

$$
\partial_{t}b\big|_{\xi}=\partial_{t}\tilde{b}\big|_{s}+\partial_{s}\tilde{b}\big|_{t}\frac{\partial s}{\partial t}\big|_{\xi}.
$$

By slight abuse of notation, however, we will drop the tilde and consider the warping
functions a,b and u as functions of either (p,t), p ∈ M<sub>k</sub> or (ξ,t) or (s,t), depending
on context. In *(s,t)* coordinates the Ricci flow equation reads

$$
a,b
$$

$$
(p,t),p\in M_k
$$

$$
\left(\xi,t\right)
$$

$$
(s,t)
$$

(2.13)

$$
\partial_{t}a\big|_{s}=a_{s s}-2\frac{a^{3}}{b^{4}}+2\frac{a_{s}b_{s}}{b}-a_{s}\frac{\partial s}{\partial t}
$$

(2.14)

$$
\partial_{t}b\big|_{s}=b_{s s}-\frac{4}{b}+2\frac{a^{2}}{b^{3}}+\frac{a_{s}b_{s}}{a}+\frac{b_{s}^{2}}{b}-b_{s}\frac{\partial s}{\partial t}
$$

where

(2.15)

$$
\frac{\partial s}{\partial t}\big|_{\xi}=\int_{0}^{s}\frac{a_{ss}}{a}+2\frac{b_{ss}}{b}\mathrm{d}s
$$

Whenever we differentiate a function f : M<sub>k</sub> × [0,T] with respect to time, unless
stated otherwise, assume that the point on the manifold M<sub>k</sub> is held fixed. If we
differentiate with respect to time while holding *s* fixed we will denote the partial
derivative by ∂<sub>t</sub>f |<sub>s</sub> to avoid confusion. Because s is a function of (ξ,t), in general

$$
f:M_{k}\times[0,T]
$$

$$
M_{k}
$$

$$
\partial_{t}f|_{s}
$$ for fixed s<sub>0</sub> > 0 the set {s = s<sub>0</sub>}⊂ M<sub>k</sub> is dependent on time. Therefore holding s
or *ξ* fixed during partial differentiation produces very different results.

$$
s_{0}>0
$$

$$
\{s=s_{0}\}\subset M_{k}
$$

$$
\xi
$$

This following property of the warping functions *a* and *b* will be used throughout
the paper.

Lemma 2.2. Let (M<sub>k</sub>,g(t)), t ∈ [0,T), be a smooth Ricci flow solution. Then for
*all t ∈* [0,T] *the warping functions a(s,t*) *and b(s,t*) *can be extended to an odd and
even function, respectively, on R.*

$$
\left(M_{k},g(t)\right),t\in[0,T)
$$

$$
a(s,t)
$$

$$
t\in[0,T]
$$

$$
b(s,t)
$$

*Proof.* Note that a necessary condition for a metric *g* of the form (2.3) to be smooth
is that its corresponding warping functions *a* and *b* are extendable to odd and even
functions, respectively, on R. Therefore the desired result follows. Alternatively,
notice that if the warping functions of the initial data *a(s,0*) and *b(s,0*) can be
extended to an odd and even function, respectively, on R, we can also extend the
equations (2.13), (2.14) and (2.15) to all of R. An inspection of these equations
shows that the parity of *a* and *b* is preserved under the flow.

$$
a(s,0)
$$

$$
b(s,0)
$$