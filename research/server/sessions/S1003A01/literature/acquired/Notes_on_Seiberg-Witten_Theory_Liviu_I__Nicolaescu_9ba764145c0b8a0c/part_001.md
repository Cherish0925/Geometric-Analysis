---
retention_scope: session
part: 1
total_parts: 13
---

[Part 1/13 of: Notes on Seiberg-Witten Theory Liviu I. Nicolaescu]

# Notes on Seiberg-Witten Theory Liviu I. Nicolaescu

> Source: https://academicweb.nd.edu/~lnicolae/swnotes.pdf
> Fetched: 2026-10-09 12:09
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
  "source_url": "https://academicweb.nd.edu/~lnicolae/swnotes.pdf",
  "metadata": {
    "provenance_urls": [
      "https://academicweb.nd.edu/~lnicolae/swnotes.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Taubes Seiberg-Witten canonical class J-holomorphic curves arbitrary compatible almost complex structure closed symplectic 4-manifold"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

3.3. Applications 273 Consider a symplectic 4-manifold (M, ω) equipped with a compatible metric g and associated almost complex structure J so that ω(X, Y ) = g(JX, Y ), ∀X, Y ∈Vect (M).
The almost complex structure canonically deﬁnes a spinc structure σ0 with associated line bundle det(σ0) ∼ = K−1 M .
Any other spinc structure has the form σL = σ0 ⊗L, det(σL) = K−1 M ⊗L2 where L is a Hermitian line bundle. Moreover, Γ(S+ L) = Ω0,0(L) ⊕Ω0,2(L), Γ(S− L) ∼ = Ω0,1(L).
Thus, any spinor ψ ∈Γ(S+ L) naturally decomposes as ψ = α ⊕β ∈Ω0,0(L) ⊕Ω0,2(L). [...] Remark 3.3.31. The above nonvanishing result implies that any symplectic (K¨ ahler) 4-manifold admits almost complex structures which are not homo-topic to an almost complex structure compatible with a symplectic (K¨ ahler) structure; see .
Remark 3.3.32. One can use the information contained in Taubes’ theorem to produce a very ingenious invariant of a symplectic 4-manifold, (M, ω). [...] On the other hand, since f acts as −1 on H2(M, Z) and b+ 2 (X) = 3 we deduce that f changes the orientation of H2 +(X) by −1 and thus changes the Seiberg-Witten invariant by the same factor. ■ 3.3.4. Seiberg-Witten equations on symplectic 4-manifolds. We hope that by now we have convinced the reader of the powerful impact of the K¨ ahler condition on the Seiberg-Witten equations.
This condition can be relaxed in two ways. We can require the manifold to be complex but not K¨ ahler or we can drop the integrability condition on the almost complex s

## Retrieved source content

# Notes on Seiberg-Witten Theory

Liviu I. Nicolaescu

* * *

_To my parents, with love and gratitude_

* * *

* * *

## Contents

Introduction
Chapter 1. Preliminaries

xiii
1

x1.1. Bundles, connections and characteristic classes 1
1.1.1. Vector bundles and connections 1

1.1.2. Chern-Weil theory
x1.2. Basic facts about elliptic equations
x1.3. Clifiord algebras and Dirac operators

11
15
26

1.3.1. Clifiord algebras and their representations 26

1.3.2. The Spin and Spinc groups

33

1.3.3. Spin and spinc structures 39
1.3.4. Dirac operators associated to spin and spinc structures 45

x1.4. Complex difierential geometry
1.4.1. Elementary complex difierential geometry
1.4.2. Cauchy-Riemann operators

52
52
66

1.4.3. Dirac operators on almost K˜ahler manifolds 77
x1.5. Fredholm theory 82

1.5.1. Continuous families of elliptic operators
1.5.2. Genericity results
Chapter 2. The Seiberg-Witten Invariants
x2.1. Seiberg-Witten monopoles
2.1.1. The Seiberg-Witten equations
2.1.2. The functional set-up

82
97
101
101
101
106

x2.2. The structure of the Seiberg-Witten moduli spaces 111
2.2.1. The topology of the moduli spaces 112

* * *

2.2.2. The local structure of the moduli spaces 117
2.2.3. Generic smoothness 128
2.2.4. Orientability 134
x2.3. The structure of the Seiberg-Witten invariants 137
2.3.1. The universal line bundle 137
2.3.2. The case b2+ \> 1 139
2.3.3. The case b2+ = 1 151
2.3.4. Some examples 166
x2.4. Applications 173
2.4.1. The Seiberg-Witten equations on cylinders 173
2.4.2. The Thom conjecture 180
2.4.3. Negative deflnite smooth 4-manifolds 185
Chapter 3. Seiberg-Witten Equations on Complex Surfaces 193
x3.1. A short trip in complex geometry 193
3.1.1. Basic notions 193
3.1.2. Examples of complex surfaces 211
3.1.3. Kodaira classiflcation of complex surfaces 223
x3.2. Seiberg-Witten invariants of K˜ahler surfaces 225
3.2.1. Seiberg-Witten equations on K˜ahler surfaces 225
3.2.2. Monopoles, vortices and divisors 230
3.2.3. Deformation theory 239
x3.3. Applications 243
3.3.1. A nonvanishing result 243
3.3.2. Seiberg-Witten invariants of simply connected elliptic surfaces249
3.3.3. The failure of the _h_-cobordism theorem in four dimensions 271
3.3.4. Seiberg-Witten equations on symplectic 4-manifolds 272
Chapter 4. Gluing Techniques 281
x4.1. Elliptic equations on manifolds with cylindrical ends 281
4.1.1. Manifolds with cylindrical ends 281
4.1.2. The Atiyah-Patodi-Singer index theorem 285
4.1.3. Eta invariants and spectral ows 290
4.1.4. The Lockhart-McOwen theory 296
4.1.5. Abstract linear gluing results 301
4.1.6. Examples 307
x4.2. Finite energy monopoles 325
4.2.1. Regularity 325
4.2.2. Three-dimensional monopoles 327
4.2.3. Asymptotic behavior. Part I 335
4.2.4. Asymptotic behavior. Part II 340
4.2.5. Proofs of some technical results 354

$$
b\_{2}^{+}>1
$$

$$
b\_{2}^{+}=1
$$ x4.3. Moduli spaces of flnite energy monopoles: Local aspects 363

4.3.1. Functional set-up
4.3.2. The Kuranishi picture
4.3.3. Virtual dimensions

363
378
391

4.3.4. Reducible flnite energy monopoles 398
x4.4. Moduli spaces of flnite energy monopoles: Global aspects 403
4.4.1. Genericity results 403

4.4.2. Compactness properties
4.4.3. Orientability issues
x4.5. Cutting and pasting of monopoles
4.5.1. Some basic gluing constructions
4.5.2. Gluing monopoles: Local theory

406
419
422
422
429

4.5.3. The local surjectivity of the gluing construction 440
4.5.4. Gluing monopoles: Global theory 444

x4.6. Applications
4.6.1. Vanishing results
4.6.2. Blow-up formula
Epilogue
Bibliography
Index

454
454
458
465
467
475

* * *

* * *

# Introduction

_My task which I am trying to achieve is by the power of_
_the written word, to make you hear, to make you feel - it_
_is, before all, to make you_ see. _That - and no more, and_
_it is everything._

Joseph Conrad

Almost two decades ago, a young mathematician by the name of Simon Donaldson took the mathematical world by surprise when he discovered some \\pathological" phenomena concerning _smooth_ 4-manifolds. These
pathologies were caused by certain behaviours of instantons, solutions of the
Yang-Mills equations arising in the physical theory of gauge flelds.

Shortly after, he convinced all the skeptics that these phenomena represented only the tip of the iceberg. He showed that the moduli spaces
of instantons often carry nontrivial and surprising information about the
background manifold. Very rapidly, many myths were shattered.

A urry of work soon followed, devoted to extracting more and more
information out of these moduli spaces. This is a highly nontrivial job,
requiring ideas from many branches of mathematics. Gauge theory was
born and it is here to stay.

In the fall of 1994, the physicists N. Seiberg and E. Witten introduced
to the world a new set of equations which according to physical theories had
to contain the same topological information as the Yang-Mills equations.

From an analytical point of view these new equations, now known as
the Seiberg-Witten equations, are easier to deal with than the Yang-Mills
equations. In a matter of months many of the results obtained by studying
instantons were re-proved much faster using the new theory. (To be perfectly honest, the old theory made these new proofs possible since it created the
right mindset to think about the new equations.) The new theory goes
one step further, since it captures in a more visible fashion the interaction
geometry-topology.

The goal of these notes is to help the potential reader share some of
the excitement afiorded by this new world of gauge theory and eventually
become a player him/herself.

There are many di–culties to overcome. To set up the theory one needs
a substantial volume of information. More importantly, all this volume of
information is processed in a nontraditional way which may make the flrst
steps in this new world a bit hesitant. Moreover, the large and fast-growing
literature on gauge theory, relying on a nonnegligible amount of \\folklore"1,
may look discouraging to a beginner.

To address these issues within a reasonable space we chose to present a
few, indispensable, key techniques and as many relevant examples as possible. That is why these notes are far from exhaustive and many notable
contributions were left out. We believe we have provided enough background and intuition for the interested reader to be able to continue the
Seiberg-Witten journey on his/her own.

It is always di–cult to resolve the conict clarity vs. rigor and even
much more so when presenting an eclectic subject such as gauge theory. The
compromises one has to make are always biased and thus may not satisfy
all tastes and backgrounds. We could not escape this bias, but whenever a
proof would have sent us far astray we tried to present all the main concepts
and ideas in as clear a light as possible and make up for the missing details
by providing generous references. Many technical results were left to the
reader as exercises but we made sure that all the main ingredients can be
found in these notes.

Here is a description of the content. The flrst chapter contains preliminary material. It is clearly incomplete and cannot serve as a substitute
for a more thorough background study. We have included it to present in
the nontraditional light of gauge theory many classical objects which may
already be familiar to the reader.

The study of the Seiberg-Witten equations begins in earnest in Chapter
2\. In the flrst section we introduce the main characters: the monopoles,
i.e. the solutions of the Seiberg-Witten equations and the group of gauge
transformations, an inflnite dimensional Abelian group acting on the set of
monopoles. The Seiberg-Witten moduli space and its structure are described
in Section 2.2 while the Seiberg-Witten invariants are presented in Section

1That is, basic facts and examples every expert knows and thus are only briey or not at all
explained in a formal setting. They are usually transmitted through personal interactions.

* * *

2.3. We have painstakingly included all the details concerning orientations
because this is one of the most confusing aspects of the theory. We conclude
this chapter with two topological applications: the proof by P. Kronheimer
and T. Mrowka of the Thom conjecture for CP2 and the new proof based
on monopoles of Donaldson’s flrst theorem, which started this new fleld of
gauge theory.

$$
\\mathbb{C}\\mathbb{P}^2
$$

In Chapter 3 we concentrate on a special, yet very rich, class of smooth
4-manifolds, namely the algebraic surfaces. It was observed from the very beginning by E. Witten that the monopoles on algebraic surfaces can be given
an explicit algebraic-geometric description, thus opening the possibility of
carrying out many concrete computations. The flrst section of this chapter
is a brief and informal survey of the geometry and topology of complex surfaces together with a large list of examples. In Section 3.2 we study in great
detail the Seiberg-Witten equations on K˜ahler surfaces and, in particular,
we prove Witten’s result stating the equivalence between the Seiberg-Witten
moduli spaces and certain moduli spaces of divisors. The third section is
devoted entirely to applications. We flrst prove the nontriviality of the
Seiberg-Witten invariants of a K˜ahler surface and establish the invariance
under difieomorphisms of the canonical class of an algebraic surface of general type. We next concentrate on simply connected elliptic surfaces. We
compute all their Seiberg-Witten invariants following an idea of O. Biquard
based on the factorization method of E. Witten. This computation allows
us to provide the complete _smooth_ classiflcation of simply connected elliptic
surfaces. In x3.3.3, we use the computation of the Seiberg-Witten invariants
of _K3_-surfaces to show that the smooth _h_-cobordism theorem fails in four dimensions. We conclude this section and the chapter with a discussion of the
Seiberg-Witten invariants of symplectic 4-manifolds and we prove Taubes’
theorem on the nontriviality of these invariants in the symplectic world.

The fourth and last chapter is by far the most technically demanding
one. We present in great detail the cut-and-paste technique for computing Seiberg-Witten invariants. This is a very useful yet di–cult technique
but the existing written accounts of this method can be unbalanced as regards their details. In this chapter we propose a new approach to this
technique which in our view has several conceptual advantages and can be
easily adapted to other problems as well. Since the volume of technicalities
can often obscure the main ideas we chose to work in a special yet su–-
ciently general case when the moduli spaces of monopoles on the separating
3-manifold are, roughly speaking, Bott nondegenerate.

Section 4.1 contains preliminary material mostly about elliptic equations on manifolds with cylindrical ends. Most objects on closed manifolds
have cylindrical counterparts which often encode very subtle features. We discovered that a consistent use of cylindrical notions is not only ‰sthetically desirable, but also technically very useful. The cylindrical context
highlights and coherently organizes many important and not so obvious aspects of the whole gluing problem. An important result in this section is
the Cappell-Lee-Miller gluing theorem. We adapt the asymptotic language
of \[ **110\],** which is extremely convenient in gluing problems. This section
ends with the long subsection x4.1.6 containing many useful and revealing
examples. These are frequently used in gauge theory and we could not flnd
any satisfactory reference for them.

In Section 4.2 we study the flnite energy monopoles on cylindrical manifolds. The results are very similar to the ones in Yang-Mills equations and
that is why this section was greatly inspired by \[ **96, 133\].**

Section 4.3 is devoted to the local study of the moduli spaces of flnite
energy monopoles. The local structure is formally very similar to that in
Yang-Mills theory with a notable exception, the computation of the virtual
dimensions, which is part of the folklore. We present in detail this computation since it is often relevant. Moreover, we describe some new exact
sequences relating the various intervening deformation complexes to objects
covered by the Cappell-Lee-Miller gluing theorem. These exact sequences
represent a departure from the mainstream point of view and play a key role
in our local gluing theorem.

Section 4.4 is devoted to the study of global properties of the moduli
spaces of flnite energy monopoles: generic smoothness, compactness (or lack
thereof) and orientability. The orientability is no longer an elementary issue
in the noncompact case and we chose to present a proof of this fact only in
some simpler situations we need for applications.

Section 4.5 contains the main results of this chapter dealing with the process of reconstructing the space of monopoles on a 4-manifold decomposed
into several parts by a hypersurface. This manifold decomposition can be
analytically simulated by a neck stretching process. During this process,
the Seiberg-Witten equations are deformed and their solutions converge to
a singular limit. The key issue to be resolved is whether this process can
be reversed: given a singular limit can we produce monopoles converging to
this singular limit?

In his dissertation \[99\], T. Mrowka proved a very general gluing theorem which provides a satisfactory answer to the above question in the related
context of Yang-Mills equations. In x4.5.2, we prove a local gluing theorem,
very similar in spirit to Mrowka’s theorem but in an entirely new context.
The main advantage of the new approach is that all the spectral estimates
needed in the proof follow immediately from the Cappell-Lee-Miller gluing theorem. Moreover, the Mayer-Vietoris type local model is just a reformulation of the Cappell-Lee-Miller theorem. The asymptotic language of **\[110\]**
has allowed us to provide intuitive, natural and explicit descriptions of the
various morphisms entering into the deflnition of this Mayer-Vietoris model.

The local gluing theorem we prove produces monopoles converging to a
singular limit at a certain rate. If all monopoles degenerated to the singular
limit set at this rate then we could conclude that the entire moduli space on
a manifold with a su–ciently long neck can be reconstructed from the local
gluing constructions. This issue of the surjectivity of the gluing construction
is conspicuously missing in the literature and it is quite nontrivial in nongeneric situations. We deal with it in x4.5.3 by relying on Lojasewicz’s ˆ
inequality in real algebraic geometry.

In x4.5.4 we prove two global gluing theorems, one in a generic situation
and the other one in a special, obstructed setting.

Section 4.6 contains some simple topological applications of the gluing
technique. We prove the connected sum theorem and the blow-up formula.
Moreover, we present a new and very short proof of a vanishing theorem of
Fintushel and Stern.

These notes were written with a graduate student in mind but there are
many new points of view to make it interesting for experts as well (especially
our new approach to the gluing theorem). The minimal background needed
to go through these notes is a knowledge of basic difierential geometry,
algebraic topology and some familiarity with fundamental facts concerning
elliptic partial difierential equations. The list of contents for Chapter 1 can
serve as background studying guide.

**Personal note.** I have spent an exciting time of my life thinking and
writing these notes and I have been supported along the way by many people.

The book grew out of a year long seminar at McMaster University and a
year long graduate course I taught at the University of Notre Dame. I want
to thank the participants at the seminar and the course for their patience,
interest, and most of all, for their many useful questions and comments.

These notes would perhaps not have seen the light of day were it not for
Frank Connolly’s enthusiasm and curiosity about the subject of gauge theory
which have positively afiected me, personally and professionally. I want to
thank him for the countless hours of discussions, questions and comments
which helped me crystallize many of the ideas in the book.

For the past flve years, I have been inspired by Arthur Greenspoon’s
passion for culture in general, and mathematics in particular. His interest in these notes kept my enthusiasm high. I am greatly indebted to him
for reading these notes, suggesting improvements and correcting my often
liberal use of English language and punctuation.

While working on these notes I beneflted from the conversations with
Andrew Sommese, Stephan Stolz and Larry Taylor, who patiently answered
my sometimes clumsily formulated questions and helped clear the fog.

My wife has graciously accepted my long periods of quiet meditation or
constant babbling about gauge theory. She has been a constant source of
support in this endeavor. I want to thank my entire family for being there
for me.

_Notre Dame, Indiana 1999_

* * *

_Chapter 1_

# Preliminaries

_The last thing one knows in constructing a work is what_
_to put flrst._

Blaise Pascal, _Pens¶ees_

The flrst chapter contains a fast and unavoidable biased survey of some
basic facts needed in understanding Seiberg-Witten theory. The choices in
this minimal review reect the author’s background and taste and may not
answer everyone’s needs. We hope the generous list of references will more
than make up for the various omissions.

This introductory chapter has only one goal, namely to familiarize the
reader with the basic terms and points of view in the Seiberg-Witten world
and cannot serve as a substitute for a solid background.

#### 1.1. Bundles, connections and characteristic classes

**1.1.1. Vector bundles and connections.** Smooth vector bundles formalize the notion of \\smooth family of vector spaces". For example, given
a smooth manifold _M_ and a vector space _F_ we can think of the Cartesian
product

$$
\\underline{F}=\\underline{F}\_M:=F\\times M
$$ as a smooth family (Fx)x2M of vector spaces. This trivial example is not
surprisingly called the trivial vector bundle with flber _F_ and base _M._

$$
(F\_{x})\_{x\\in M}
$$

$$
M
$$

We can obtain more interesting examples by gluing these simple ones
using _gluing data._ These consist of

A. an open cover (Ufi) of a smooth manifold M,

$$
\\left(U\_{\\alpha}\\right)
$$

**B.** a _gluing cocycle,_ i.e. a collection of smooth maps

$$
g\_{\\beta\\alpha}:U\_{\\alpha\\beta}\\rightarrow\\operatorname{Aut}(F)
$$

(where Ufifl = U

fi \ Ufl), such that

$$
U\_{\\alpha\\beta}=U\_{\\alpha}\\cap U\_{\\beta}
$$

$$
g\_{\\alpha\\alpha}(x)\\equiv{\\bf1} _{F},\\quad g_{\\gamma\\alpha}\\equiv g\_{\\gamma\\beta}(x)\\cdot g\_{\\beta\\alpha}(x)\\quad\\forall x\\in U\_{\\alpha\\beta\\gamma}:=U\_{\\alpha}\\cap U\_{\\beta}\\cap U\_{\\gamma}\\neq\\emptyset.
$$

is the The open cover _support_

_=;:_ _fiis_ also known as a _trivializing cover._ We will also say it
of the U gflfi.

$$
U\_{\\alpha}
$$

$$
g\_{\\beta\\alpha}
$$

The map gflfi describes the \\transition from F fi:= FUfi to F fl" in the
sense that for every x 2 Ufifl the element (v; x) 2 F fi is identifled with the
element (gflfi(x)v; x) 2 F fl. Pasting together the trivial bundles F fi following
the instructions given by the gluing cocycle we obtain a smooth manifold
_E_ (called the _total space),_ a smooth map _…_ : _E!M_ (called _the canonical_
_projection_) and difieomorphisms
¡
1

$$
g\_{\\beta\\alpha}
$$

$$
\\underline{F} _{\\alpha}:=\\underline{F}_{U\_{\\alpha}}
$$

$$
x\\in U\_{\\alpha\\beta}
$$

$$
\\underline{F}\_{\\beta}
$$

$$
(v,x)\\in\\underline{F}\_{\\alpha}
$$

$$
\\left(g\_{\\beta\\alpha}(x)v,x\\right)\\in\\underline{F}\_{\\beta}
$$

$$
\\underline{F}\_{\\alpha}
$$

$$
\\pi:E\\rightarrow M
$$

$$
\\psi\_{\\alpha}:\\pi^{-1}(U\_{\\alpha})\\to\\underline{F}\_{\\alpha}
$$

(called local _trivializations_) such that for all

x 2 Ufifl, v 2 V

$$
x\\in U\_{\\alpha\\beta},v\\in V
$$

$$
\\psi\_{\\beta}\\circ\\psi\_{\\alpha}^{-1}(v,x)=(g\_{\\beta\\alpha}(x)v,x).
$$

_E!M…_ as above is called a _vector bundle_
deflnition the dimension of the standard flber
Rank-one bundles are also known as _line bundles_

over _M._ The rank of _E_ is by
_F_ (over its fleld of scalars).
.

$$
E\\xrightarrow{\\pi}M
$$

**Example 1.1.1.** Consider the projective space CP
one-dimensional complex subspaces of Cn+1

n deflned as the set of
. There is a natural projection

$$
\\mathbb{C}\\mathbb{P}^n
$$

$$
\\mathbb{C}^{n+1}
$$

$$
\\pi:\\mathbb{C}^{n+1}\\setminus{0}\\rightarrow\\mathbb{C}\\mathbb{P}^n
$$

where _…(x):=the one-dimensional subspace spanned by x._ The flbers

$$
\\pi(x):=
\\pi^{-1}(p),\\quad p\\in\\mathbb{C P}^{n},
$$

¡
are vector subspaces of Cn+1. The family … 1(p) is indeed a smooth family
of vector spaces in the sense described above. It is called the _tautological_
(or universal) line bundle over the projective space and is denoted by Un.

$$
\\pi^{-1}(p)
$$

$$
\\mathbb{C}^{n+1}
$$

$$
\\mathbb{U}\_{n}
$$

$$
\\mathbb{U}\_{n}
$$

Exercise 1.1.1. Describe a gluing cocycle for Un.

Suppose that _X!Yf_ is a smooth map and _E!Y_ is a smooth vector
bundle given by a gluing cocycle gflfi supported by an open cover (Ufi) of
_Y._ Then _f_ induces a vector bundle on _X_ called the _pullback of E by f_ and

$$
X\\xrightarrow{f}Y
$$

$$
E\\rightarrow Y
$$

$$
g\_{\\beta\\alpha}
$$

$$
\\left(U\_{\\alpha}\\right)
$$

* * *

⁄ ¡
denoted by f E. It is given by the open cover (Vfi = f 1(Ufi)) and gluing
cocycle hflfi = gflfi – f.

$$
(V\_{\\alpha}=f^{-1}(U\_{\\alpha}))
$$

$$
f^{\*}E
$$

$$
h\_{\\beta\\alpha}=g\_{\\beta\\alpha}\\circ f
$$

The following exercise describes a very general procedure of constructing
smooth vector bundles.

**Exercise 1.1.2.** Consider a smooth map _P_ from a compact, connected,
smooth manifold _X_ to the space End (V) of endomorphisms of a vector
space V such that P 2(x)=P (x) 8x 2 X, i.e. P (x) is a smooth family of
projectors of _V._

$$
P(x)
$$

$$
P^{2}(x)=P(x)\\forall x\\in X
$$

(a) Show that dim kerP (x) is independent of
common dimension.

_x 2 X._ Denote by _k_ this

$$
x\\in X
$$

$$
P(x)
$$

(b) Show that the assignment _x 7!_ kerP (x) deflnes a rank- _k_ smooth vector
bundle over _X._

$$
P(x)
$$

(c) Provide a projector description of the tautological line bundle over CPn.

$$
\\mathbb{C}\\mathbb{P}^n
$$

(d) Show that any map _X!V⁄ n f0g_ deflnes in a canonical way a vector
bundle over _X_ of rank dim _V ¡_ 1.

$$
X\\to V^{\*}\\setminus{0}
$$

$$
V-1
$$

Remark 1.1.2. Denote by Gk(V) the Grassmannian of k-dimensional subspaces of an _n_-dimensional vector space _V._ Assume _V_ is equipped with an
inner product. For each _k_-dimensional subspace _U‰V_ denote by _PU_ the
?
orthogonal projection onto _U._ The smooth family

$$
G\_{k}(V)
$$

$$
U\\subset V
$$

$$
P\_{U}
$$

$$
U^{\\perp}
$$

$$
G\_{k}(V)\\ni U\\mapsto P\_{U}
$$

deflnes according to the previous exercise a rank-k vector bundle over Gk(V)
called the universal vector bundle and denoted by Uk;n. When k = 1 this is
n¡1 n¡
precisely the tautological line bundle over RP or CP 1.

$$
G\_{k}(V)
$$

$$
\\mathbb{U}\_{k,n}
$$

$$
k=1
$$

$$
\\mathbb{R}\\mathbb{P}^{n-1}
$$

$$
\\dot{\\mathbb{C}}\\mathbb{P}^{n-1}
$$

**Exercise 1.1.3.** Suppose that _x 7! P(X_) is a smooth family of projectors
of a vector space _V_ parameterized by a connected smooth manifold _X._ Set
_k_ = dim kerP (x) and _n_ = dimV and denote by _f_ the map

$$
x\\mapsto P(X)
$$

$$
P(x)
$$

$$
k=\\dim
$$

$$
f:X\\to G\_{k}(V),x\\mapsto\\ker P(x)\\in G\_{k}(V).
$$

Show that f is smooth and that the pullback of Uk;n by f coincides with
the vector bundle deflned by the family of projections _P_ (x).

$$
\\mathbb{U}\_{k,n}
$$

$$
P(x)
$$

A smooth map _s_ from a smooth manifold _X_ to a vector space _F_ is a
smooth selection of an element _s(x_) in each flber _F £ x_ of _F._ In other words,
it is a smooth map s : X ! F X such that … – s = 1X where … : F X! X
is the natural projection. Replacing F X with any smooth vector bundle
…
_E!X_ we get the notion of smooth section of _E._ The space of smooth
sections of E will be denoted by ¡(E) orC1(E). In terms of gluing cocycles
we can describe a section as a collection of smooth maps

$$
s(x)
$$

$$
F\\times x
$$

$$
s:X\\rightarrow\\underline{F}\_{X}
$$

$$
\\pi\\circ s=\\mathbf{1}\_{X}
$$

$$
\\pi:\\underline{F}\_X\\rightarrow X
$$

$$
\\underline{F}\_X
$$

$$
E\\xrightarrow{\\pi}X
$$

$$
\\Gamma(E)
$$

$$
C^{\\infty}(E)
$$

$$
s\_{\\alpha}:U\_{\\alpha}\\rightarrow F
$$ such that

$$
s\_{\\beta}(x)=g\_{\\beta\\alpha}(x)s\_{\\alpha}(x),\\quad\\forall x\\in U\_{\\alpha}\\cap U\_{\\beta}.
$$

The functorial operations in linear algebra have a vector bundle coun-
…i
terpart. Suppose Ei! X (i = 1;2) are two vector bundles over X with
standard flbers Fi, i = 1;2, given by gluing cocycles gflfi;i along the same
support. For example, the direct sum _F1' F2_ corresponds to the _direct_
(Whitney) sum E1' E2 given by the gluing cocycle gflfi;1 ' gflfi;2.

$$
E\_{i}\\stackrel{\\pi\_{i}}{\\rightarrow}X(i=1,2)
$$

$$
F\_{i},;i=1,2,
$$

$$
g\_{\\beta\\alpha;i}
$$

$$
F\_{1}\\oplus F\_{2}
$$

$$
E\_{1}\\oplus E\_{2}
$$

$$
g\_{\\beta\\alpha;1}\\oplus g\_{\\beta\\alpha;2}
$$

⁄ ⁄ ¡1
The dual vector bundle E1 is deflned by the gluing cocycle (gflfi;1)
where \*⁄\*" denotes the conjugate transpose.

$$
E\_{1}^{\*}
$$

$$
(g\_{\\beta\\alpha;1}^{\*})^{-1}
$$

$$
\\text{"}\_{\*}\\text{"}
$$

We can form tensor products, symmetric, exterior products of
vector bundles, etc. In particular, the bundle _E1⁄ › E2_ will be denoted
by Hom ( _E1; E2)._ Its sections are _bundle morphisms,_ i.e. smooth maps
_T_ : _E1! E2_ mapping the flber _E1(x_) _ofE1_ linearly to the flber _E2(x_) of
_E2._ When _E1_ = _E2_ = _E_ we use the notation End (E). If the induced morphisms _T_ (x) are all isomorphisms then _T_ is called a bundle isomorphism. A
bundle automorphism of a vector bundle _E_ is also called a _gauge transformation._ The group of bundle automorphisms of _E_ is denoted by G(E) and
is known as the _gauge group of E._

$$
E\_{1}^{\*}\\otimes E\_{2}
$$

$$
\\left(E\_{1},E\_{2}\\right)
$$

$$
T:E\_{1}\\rightarrow E\_{2}
$$

$$
E\_{1}(x)
$$

$$
E\_{1}
$$

$$
E\_{2}(x)
$$

$$
E\_{1}=E\_{2}=E
$$

$$
E\_{2}
$$

$$
T(x)
$$

**Exercise 1.1.4.** Suppose _L!X_ is a smooth complex line bundle over _X._
Show that
_»⁄_
G(L) = C1(M;C):

$$
L\\rightarrow X
$$

$$
\\mathbb{G}(L)\\cong C^{\\infty}(M,\\mathbb{C}^{\*}).
$$

The line bundle ⁄rank(E1)E1 is called the determinant line bundle of E1
and is denoted by det _E1._

$$
\\Lambda^{\\operatorname{rank}(E\_{1})}E\_{1}
$$

$$
E\_{1}
$$

$$
E\_{1}
$$

If _E!X_ is an R-vector bundle then a _metric_ on _E_ is a section _h_ of
⁄
Symm2(E) such that _h(x_) is positive deflnite for every _x 2 X._ IfE is
complex one deflnes similarly Hermitian metrics on _E.AHermitian bundle_
is a vector bundle equipped with a Hermitian metric.

$$
E\\rightarrow X
$$

$$
\\mathrm{Symm}^2(E^\*)
$$

$$
x\\in X
$$

$$
h(x)
$$

The next exercise will show how to use sections to prove that any complex line bundle over a compact manifold is the pullback of the universal
line bundle over a complex projective space.

**Exercise 1.1.5.** Suppose _M_ is a smooth compact manifold and _E!M_ is
a complex line bundle. A subspace V ‰ C1(E) is said to be ample if for
any _x 2 M_ there exists _u 2 V_ such that _u(x_) 6

$$
E\\rightarrow M
$$

$$
V\\subset C^{\\infty}(E)
$$

$$
u\\in V
$$

$$
u(x)\\neq0
$$

$$
x\\in M
$$

= 0.
1(E).
(a) Show that there exist flnite-dimensional ample subspaces V _‰ C x 2 M_
(b) Let V be a flnite-dimensional ample subspace of C1(E). For each
set
_V_ = fv 2 V; v(x) = 0g:

$$
V\\subset C^{\\infty}(E)
$$

$$
C^{\\infty}(E)
$$

$$
x\\in M
$$

$$
V\_{x}={v\\in V;v(x)=0}.
$$

Equip _V_ with a Hermitian metric and denote by _P_ (x): _V! V_ the orthogonal projection onto Vx. Show that dim kerPx = 1 and the family of

$$
P(x):V\\to V
$$

$$
V\_{x}
$$

$$
P\_{x}=1
$$ projections _fP(x); x 2 M g_ is smooth. As in Exercise 1.1.2(b) we obtain a
complex line bundle _EV ! V._

$$
{P(x);;x\\in M}
$$

$$
E\_{V}\\rightarrow V
$$

(c) Show that the line bundle _E_ is isomorphic to _EV._ In particular, this
shows that _E_ is the pullback of a universal line bundle over a projective
space.

$$
E\_{V}
$$

(d) Suppose that f; g : M! CPn are two (smoothly) homotopic maps.
Denote by Ef (resp. Eg) the pullbacks of the universal line bundle Un via
»
f (resp. g). Show that Ef = Eg.

$$
f,g\ :\ M\ \\to\ \\mathbb{C}\\mathbb{P}^n
$$

$$
E\_{f}\ (resp.\ E\_{g})
$$

$$
\\mathbb{U}\_{n}
$$

$$
E\_{f}\\cong E\_{g}
$$

**Remark 1.1.3.** For every smooth manifold _M_ denote by Pic1(M) the
space of isomorphism classes of smooth complex line bundles over _M_ and by
\[M;CPn\]1 the set of (smooth) homotopy classes of smooth maps M ! Cn.
This is an inductive family

$$
\\mathrm{Pic}^{\\infty}(M)
$$

$$
\[M,\\mathbb{C}\\mathbb{P}^n\]\_{\\infty}
$$

$$
M\\to\\mathbb{C}^n
$$

$$
\[M,\\mathbb{C P}^{1}\] _{\\infty}\\hookrightarrow\[M,\\mathbb{C P}^{2}\]_{\\infty}\\hookrightarrow\\cdots
$$

and we denote by \[M;CP1\]1 its inductive limit. The above exercise shows
that if _M_ is compact we have a bijection

$$
\[M,\\mathbb{C}\\mathbb{P}^{\\infty}\]\_{\\infty}
$$

$$
\\operatorname{Pic}^{\\infty}(M)\\cong\[M,\\mathbb{C}\\mathbb{P}^{\\infty}\]\_{\\infty}.
$$

The tensor product of line bundles induces a structure of Abelian group on
Pic1(M). Since the inductive limit CP1 of the CPn’s is a K(Z;2)-space we
can conclude that we have an isomorphism of groups

$$
\\mathrm{Pic}^{\\infty}(M)
$$

$$
\\mathbb{C}\\mathbb{P}^{\\infty}
$$

$$
\\mathbb{C}\\mathbb{P}^{n}\\text{'s}
$$

$$
K(\\mathbb{Z},2)
$$

$$
c\_{1}^{t o p}:\\operatorname{Pic}^{\\infty}(M)\\to H^{2}(M,\\mathbb{Z}).
$$

For any L 2 Pic1(M) the element c1top(L) is called the topological flrst Chern
_class of L._

$$
L\\in\\mathrm{Pic}^{\\infty}(M)
$$

$$
c\_{1}^{top}(L)
$$

One is often led to study families of vector spaces satisfying additional
properties such as vector spaces in which vectors have lengths and pairs of
vectors have deflnite angles (as in Euclidean geometry). According to Felix
Klein’s philosophy, this is the same as looking at the _symmetry group,_ i.e.
the subgroup of linear maps which preserve these additional features. In
the above case this is precisely the orthogonal group. If we want to deal
with families of such spaces then we must impose restrictions on the gluing
maps: they must be valued in the given symmetry group. Here is one way
to formalize this discussion. Suppose we are given the following data.

_†_ A Lie group _G_ and a representation

$$
\\rho:G\\to\\mathrm{End}\\left(F\\right).
$$

† A smooth manifold X and open cover Ufi.

$$
U\_{\\alpha}
$$

_†_ A _G-valued gluing cocycle,_ i.e. a collection of smooth maps

$$
g\_{\\beta\\alpha}:U\_{\\alpha\\beta}\\rightarrow G
$$ such that gfifi(x)=12 G 8x 2 Ufi and

$$
g\_{\\alpha\\alpha}(x)=1\\in G\\forall x\\in U\_{\\alpha}
$$

$$
g\_{\\gamma\\alpha}(x)=g\_{\\gamma\\beta}(x)\\cdot g\_{\\beta\\alpha}(x)\\quad\\forall x\\in U\_{\\alpha\\beta\\gamma}.
$$

Then the collection

$$
\\rho(g\_{\\beta\\alpha}):U\_{\\alpha\\beta}\\rightarrow\\operatorname{End}(F)
$$

deflnes a gluing cocycle for a vector bundle _E_ with standard flber _F_ and
symmetry group _G._ The vector bundle _E_ is said to have a _G_-structure.

**Remark 1.1.4.** Difierential geometers usually phrase the above construction in terms of _principal G-bundles._ Given a gluing _G_-cocycle as above
we can obtain a smooth manifold P as follows. Glue the product G£Ufi
to G£Ufl along Ufifl using the following prescription: for each x 2 Ufifl
the element (g; x) inG£Ufi is identifled with the element (gflfi(x) ¢ g; x) in
G£Ufl. We obtain a smooth manifold P and a smooth map … : P! X
¡
whose flbers … 1(x) are difieomorphic to the Lie group G. This is called
the principal G-bundle determined by the gluing G-cocycle gflfi. The above
vector bundle _E_ is said to be _induced from P_ via the representation _‰_ and
we write this as _P £_‰ _F._ For more details we refer to vol. 1 of \[64\].

$$
G\\times U\_{\\alpha}
$$

$$
G\\times U\_{\\beta}
$$

$$
U\_{\\alpha\\beta}
$$

$$
x\\in U\_{\\alpha\\beta}
$$

$$
\\left(g,x\\right)
$$

$$
G\\times U\_{\\alpha}
$$

$$
\\left(g\_{\\beta\\alpha}(x)\\cdot g,x\\right)
$$

$$
G\\times U\_{\\beta}
$$

$$
\\pi:P\\to X
$$

$$
\\pi^{-1}(x)
$$

$$
g\_{\\beta\\alpha}
$$

$$
\\rho
$$

$$
P\\times\_{\\rho}F
$$

**Exercise 1.1.6.** Show that the above manifold _P_ comes with a natural free,
right _G_-action and the space of orbits can be naturally identifled with _X._

Exercise 1.1.7. Regard S2n+1 as a real hypersurface in Cn+1 given by the
equation jz0j2 \+ jz1j2 \+ ¢¢¢jznj2 = 1\. The group

$$
S^{2n+1}
$$

$$
\\mathbb{C}^{n+1}
$$

$$
\|z\_{0}\|^{2}+\|z\_{1}\|^{2}+\\cdots\|z\_{n}\|^{2}=1
$$

$$
S^{1}=\\left{e^{\\mathbf{i}t};;;t\\in\\mathbb{R}\\right}\\subset\\mathbb{C}^{\*}
$$

acts on S2n+1 by scalar multiplication. The quotient of this action is obviously CPn.

$$
S^{2n+1}
$$

$$
\\mathbb{C}\\mathbb{P}^n
$$

(a) Show that S2n+1! CPn is a principal S1-bundle. (It is known as the
_Hopf bundle._

$$
S^{2n+1}\\rightarrow\\mathbb{C}\\mathbb{P}^n
$$

$$
S^{1}
$$

(b) Show that the line bundle associated to it via the tautological representation S1! Aut (C1) is precisely the universal line bundle Un over CPn.

$$
S^{1}\\rightarrow\\mathrm{Aut}\\left(\\mathbb{C}^{1}\\right)
$$

$$
\\mathbb{U}\_{n}
$$

$$
\\mathbb{C}\\mathbb{P}^n
$$

**Exercise 1.1.8.** Show that any metric on a rank- _n_ real vector bundle naturally deflnes an _O(n_)-structure.

To exist as a subject, _difierential_ geometry requires a way to _difierentiate_
the objects under investigation. This is where connections come in. A
…
_connection_ (or _covariant derivative_) _r_ on a vector bundle _E!M_ is a map
which associates to every section _s 2_ ¡(E), and any vector fleld _X_ on M,a
new section rXs, such that, for every f 2 C1(M)

$$
E\\xrightarrow{\\pi}M
$$

$$
s\\in\\Gamma(E)
$$

$$
\\nabla\_{X}s
$$

$$
f\\in C^{\\infty}(M)
$$

$$
\\nabla\_{X}(fs)=df(X)s+f\\nabla\_{X}s.
$$ rXs is the derivative of s in the direction X. One usually forgets the vector
fleld _X_ in the above deflnition and thinks of _r_ as a map

$$
\\nabla\_{\\bullet}:\\Gamma(E)\\to\\Gamma(T^{\*}M\\otimes E)
$$

satisfying Leibniz’ rule

$$
\\nabla\_{\\bullet}(f s)=d f(\\bullet)\\otimes s+f\\nabla\_{\\bullet}s.
$$

Note the following fact.

**Proposition 1.1.5.** _There exists at least one connection r0 on E. Moreover, any other connection can be obtained from r0 by the addition of an_
End (E)-valued 1-form A 2 ›1(End (E)) where by deflnition, for any vector
_bundle F ! M we set_

$$
\\nabla^{0}
$$

$$
\\nabla^{0}
$$

$$
A\\in\\Omega^{1}(\\mathrm{End}\\left(E\\right))
$$

$$
F\\rightarrow M
$$

$$
\\Omega^{k}(F):=\\Gamma(\\Lambda^{k}T^{\*}M\\otimes F).
$$

_In particular, the space_ A(E) _of connections on E is an a–ne space modeled_
by ›1(End (E)).

$$
\\mathcal{A}(E)
$$

$$
\\Omega^{1}(End\\left(E\\right))
$$

The trivial bundle _F_ admits a natural connection £ called the _trivial_
_connection._ To describe it recall that sections of _F_ can be regarded as
smooth functions _s_ : _M!F._ Deflne

$$
s:M\\rightarrow F
$$

$$
\\Theta s=ds\\in\\Omega^1(M)\\otimes F.
$$

Any other connection _r_ on _F_ will difier from £ by a 1-form _A_ with coe–-
cients endomorphisms of _F,_ i.e.

$$
\\nabla=\\Theta+A,\\quad A\\in\\Omega^1(M)\\otimes\\mathrm{End}(F).
$$

If _E_ is obtained by gluing the trivial bundles
cocycle gflfi, then any connection on E
rfi on F fi. More precisely, if rfi =£+
1-forms Afi and Afl satisfy the compatibility rules

F fi:= F U using the
fi
is obtained by gluing connections
Afi then on the overlaps Ufifl the

$$
\\underline{F} _{\\alpha};:=;\\underline{F}_{U\_{\\alpha}}
$$

$$
g\_{\\beta\\alpha}
$$

$$
\\nabla^{\\alpha}
$$

$$
\\underline{F}\_{\\alpha}
$$

$$
\\nabla^{\\alpha}=\\Theta+A\_{\\alpha}
$$

$$
U\_{\\alpha\\beta}
$$

$$
A\_{\\alpha}
$$

$$
A\_{\\beta}
$$

$$
A\_{\\beta}=-d g\_{\\beta\\alpha}g\_{\\beta\\alpha}^{-1}+g\_{\\beta\\alpha}A\_{\\alpha}g\_{\\beta\\alpha}^{-1}=g\_{\\alpha\\beta}^{-1}d g\_{\\alpha\\beta}+g\_{\\alpha\\beta}^{-1}A\_{\\alpha}g\_{\\alpha\\beta}.
$$

(1.1.1)

**Exercise 1.1.9.** Prove (1.1.1).

Exercise 1.1.10. Consider a smooth family P : x 7! Px of projectors of the
vector space _F_ parameterized by the connected smooth manifold _X._ Show
that (id ¡ P)£ deflnes a connection on the subbundle ker P ‰ F X.

$$
P:x\\mapsto P\_{x}
$$

$$
(\\mathbf{i}\\mathbf{d}-P)\\Theta
$$

$$
P\\subset\\underline{F}\_X
$$

Imitating the above local description of a connection we can deflne a
notion of connection compatible with a _G_-structure. Thus, let us suppose
the vector bundle _E!M_ has a _G_-structure deflned by the gluing cocycle

$$
E\\rightarrow M
$$

$$
g\_{\\beta\\alpha}:U\_{\\beta\\alpha}\\rightarrow G
$$ and the representation _‰_ : _G !_ Aut (F). Denote by g the Lie algebra of _G._
The gluing cocycle deflnes a principal _G_-bundle _P ! M._ A connection on
_P_ is a collection of 1-forms

$$
\\rho:G\\rightarrow\\mathrm{Aut}\\left(F\\right)
$$

$$
P\\rightarrow M
$$

$$
A\_{\\alpha}\\in\\Omega^{1}(U\_{\\alpha})\\otimes\\mathfrak{g}
$$

¡1
satisfying (1.1.1), where gflfiAfigflfi denotes the adjoint action of gflfi(x) on
¡1 ¡
g while ¡dgflfigflfi = gfifl1dgfifl is the pullback via gfifl of the Maurer-Cartan
form on _G._ (This is the g-valued, left invariant 1-form on _G_ whose value at
**1** is the tautological map _T1G !_ g.)

$$
g\_{\\beta\\alpha}A\_{\\alpha}g\_{\\beta\\alpha}^{-1}
$$

$$
g\_{\\beta\\alpha}(x)
$$

$$
-d g\_{\\beta\\alpha}g\_{\\beta\\alpha}^{-1}=g\_{\\alpha\\beta}^{-1}d g\_{\\alpha\\beta}
$$

$$
g\_{\\alpha\\beta}
$$

$$
T\_{\\mathbf{1}}G\\rightarrow\\mathfrak{g}.)
$$

Given a connection on the principal bundle we can obtain a genuine
connection (i.e. covariant derivative) on _E_ = _P £_‰ _F_ given by the End (F)-
valued 1-forms ‰⁄(Afi), where

$$
E=P\\times\_{\\rho}F
$$

$$
\\rho\_{\*}(A\_{\\alpha})
$$

$$
\\rho\_{\*}:T\_{1}G\\to\\operatorname{End}\\left(F\\right)
$$

denotes the difierential of _‰_ at **12** _G._

$$
\\rho
$$

$$
\\mathbf{1}\\in G
$$

A _gauge transformation_ of a bundle _E_ with a _G_-structure is a collection
of smooth maps Tfi: Ufi! G subject to the gluing conditions

$$
T\_{\\alpha}:U\_{\\alpha}\\rightarrow G
$$

$$
T\_{\\beta}=g\_{\\beta\\alpha}T\_{\\alpha}g\_{\\beta\\alpha}^{-1}.
$$

(From a more invariant point of view, a gauge transformation is a special
section of the bundle of endomorphisms of E.) The set of such gauge transformations forms a group which will be denoted by GG(E).

$$
\\mathcal{G}\_{G}(E)
$$

To a bundle _E_ with a _G_-structure one can naturally associate a vector
bundle Ad (E) deflned by the same gluing _G_-cocycle as _E_ but, instead of _‰,_
one uses the adjoint representation _Ad_ : _G !_ End (g).

$$
\\rho,
$$

$$
Ad:G\\rightarrow End\\left(\\mathfrak{g}\\right)
$$

Proposition 1.1.6. The space AG(E) of G-compatible connections on a
vector bundle E with a G-structure is an a–ne space modeled by ›1(Ad (E)).
Moreover, the group of gauge transformations GG(E) acts on AG(E) by con-
_jugation_
¡1
G (E) £ A (E) 3 (; rA) 7! rA 2 A (E):

$$
\\mathcal{A}\_{G}(E)
$$

$$
\\Omega^{1}(\\mathrm{Ad}\\left(E\\right))
$$

$$
\\mathfrak{G}\_{G}(E)
$$

$$
\\mathcal{A}\_{G}(E)
$$

$$
\\mathfrak{G} _{G}(E)\\times\\mathcal{A}_{G}(E)\\ni(\\gamma,\\nabla^{A})\\mapsto\\gamma\\nabla^{A}\\gamma^{-1}\\in\\mathcal{A}\_{G}(E).
$$

For more details about principal bundles and connections from a gauge
theoretic point of view we refer to the very elegant presentation in \[ **116\].**

If _E_ is a complex vector bundle of complex rank _r_ equipped with a
Hermitian metric _h†; †i_ then it is equipped with a natural _U_ (r)-structure. A
_Hermitian connection r_ on _E_ is by deflnition a connection compatible with
this _U_ (r)-structure or, equivalently,

$$
\\langle\\bullet,\\bullet\\rangle
$$

$$
U(r)
$$

$$
L\_{X}\\langle s\_{1},s\_{2}\\rangle=\\langle\\nabla\_{X}s\_{1},s\_{2}\\rangle+\\langle s\_{1},\\nabla\_{X}s\_{2}\\rangle,\\quad\\forall X\\in\\operatorname{Vect}{(M)},\\quad s\_{1},s\_{2}\\in C^{\\infty}(E).
$$

There is a natural (left) action of G

G(E) onAG(E) given by

$$
\\mathcal{G}\_{G}(E)
$$

$$
\\mathcal{A}\_{G}(E)
$$

$$
T\\cdot\\nabla:=T\\nabla T^{-1}.
$$

* * *

The covariant method of difierentiation has a feature not encountered
in traditional calculus in Rn. More precisely, the classical result \\partial
derivatives commute"
_@2f @2f_

$$
\\mathbb{R}^n
$$

$$
\\frac{\\partial^{2}f}{\\partial x\\partial y}=\\frac{\\partial^{2}f}{\\partial y\\partial x}
$$

no longer holds in this more general context because of deep geometric reasons. One is led to quantify the extent of this noncommutativity and this is
usually encoded by the _curvature_ of a connection.

Suppose _r_ is a connection on a vector bundle _E!M._ For any vector
flelds _X, Y_ on _M_ and any section _u 2_ ¡(E) deflne

$$
\\nabla
$$

$$
E\\rightarrow M
$$

$$
u\\in\\Gamma(E)
$$

$$
\\begin{align\*}F(X,Y)u=F\_{\\nabla}(X,Y)u&:=\[\\nabla\_X,\\nabla\_Y\]u-\\nabla\_{\[X,Y\]}u\\=(\\nabla\_X\\nabla\_Y-\\nabla\_Y\\nabla\_X)u-\\nabla\_{\[X,Y\]}u&\\in\\Gamma(E).\\end{align\*}
$$

Note that for all f 2 C1(M)

$$
f\\in C^{\\infty}(M)
$$

$$
F(fX,Y)u=F(X,fY)u=F(X,Y)(fu)=fF(X,Y)u.
$$

Thus the map

$$
u\\mapsto F(X,Y)u
$$

is an endomorphism of _E_ for all _X; Y._ We denote it by _F_ ( _X;_ Y). Note that
the map

$$
F(X,Y)
$$

$$
TM\\otimes TM\\rightarrow End\\left(E\\right),\\quad X\\otimes Y\\mapsto F(X,Y)
$$

is a skew-symmetric bundle morphism. Thus we can regard the object _F (¢; ¢)_
⁄
as a an element of ›2(End (E)), i.e. a section of ⁄2T M › End (E). F (†; †)
is called the curvature of r. When Fr = 0 we say F is at.

$$
F(\\cdot,\\cdot)
$$

$$
\\Omega^{2}(End\\left(E\\right))
$$

$$
\\Lambda^{2}T^{\*}M\\otimes\\operatorname{End}(E).F(\\bullet,\\bullet)
$$

$$
F\_{\\nabla}=0
$$

**Exercise 1.1.11.** Suppose _E_ is a vector bundle equipped with a _G_-structure
and r is a G-compatible connection. Show that Fr 2 ›2(Ad (E)). In
particular, if _E_ is a Hermitian vector bundle and _r_ is Hermitian then the
curvature of _r_ is a 2-form with coe–cients in the bundle of skew-Hermitian
endomorphisms of _E._

$$
F\_{\\nabla}\\in\\Omega^{2}(\\mathrm{Ad}\\left(E\\right))
$$

Exercise 1.1.12. (a) Consider the trivial bundle F M. Then the trivial
connection £ is at.

$$
\\underline{F}\_{M}
$$

(b) If A 2 ›1(End (F)) then the curvature of £ + A is

$$
A\\in\\Omega^{1}(\\mathrm{End}\\left(\\underline{F}\\right))
$$

$$
\\Theta+A
$$

$$
F\_{A}=dA+A\\wedge A.
$$

Above, A is thought of as a matrix of with entries smooth 1-forms!ij. Then
dA is the matrix with entries the 2-forms d!ij and A^A is a matrix whose
_(i; j)_-entry is the 2-form
X

$$
\\omega\_{ij}
$$

$$
d\\omega\_{ij}
$$

$$
\\sum\_{k}\\omega\_{i k}\\wedge\\omega\_{k j}.
$$

* * *

If E is given by a gluing cocycle gflfi and r is given by the collection of
1-forms Afi 2 ›1(End (F fi)) then the above exercise shows that F is locally
described by the collection of 2-forms dAfi \+ Afi ^ Afi.

$$
g\_{\\beta\\alpha}
$$

$$
A\_{\\alpha}\\in\\Omega^{1}(\\operatorname{End}\\left(\\underline{{F}}\_{\\alpha}\\right))
$$

$$
F
$$

$$
d A\_{\\alpha}+A\_{\\alpha}\\wedge A\_{\\alpha}
$$

**Example 1.1.7.** Suppose _L!M_ is a complex line bundle given by a gluing
⁄
cocycle zflfi: Ufifl! C. Then a connection on L is deflned by a collection
of complex valued 1-forms!fi satisfying
dz

$$
L\\rightarrow M
$$

$$
z\_{\\beta\\alpha}:U\_{\\alpha\\beta}\\rightarrow\\mathbb{C}^{\*}
$$

$$
\\omega\_{\\alpha}
$$

$$
\\omega\_{\\beta}=\\frac{d z\_{\\alpha\\beta}}{z\_{\\alpha\\beta}}+\\omega\_{\\alpha}.
$$

The curvature is given by the collection of 2-forms d!fi.

$$
d\\omega\_{\\alpha}
$$

If _L_ has a U(1)-structure (i.e. is equipped with a Hermitian metric) then
the gluing maps belong to S1:

$$
U(1)
$$

$$
S^{1}
$$

$$
z\_{\\beta\\alpha}:U\_{\\alpha\\beta}\\rightarrow S^{1}.
$$

The connection is Hermitian (i.e. compatible with the metric) if!fi 2
»
›1(Ufi) › u(1) = iR. Thus we can write

$$
\\omega\_{\\alpha}\\in
$$

$$
\\Omega^{1}(U\_{\\alpha})\\otimes\\underline{u}(1)\\cong\\mathbf{i}\\mathbb{R}
$$

$$
\\omega\_{\\alpha}=\\mathbf{i}\\theta\_{\\alpha},\\quad\\theta\_{\\alpha}\\in\\Omega^{1}(U\_{\\alpha}).
$$

They are related by

$$
\\theta\_{\\beta}-\\theta\_{\\alpha}=-\\mathbf{i}\\frac{d z\_{\\alpha\\beta}}{z\_{\\alpha\\beta}}=z\_{\\alpha\\beta}^{\*}(d\\theta)
$$

where _d_ denotes the angular form on _S_

1.

$$
S^{1}
$$

**Exercise 1.1.13.** Consider a Hermitian line bundle _L!M_ and denote by
P ! M the corresponding principal S1-bundle. For each p 2 P denote by
ip the injection
S1 3 eit 7! p ¢ eit 2 P:

$$
L\\rightarrow M
$$

$$
P\\rightarrow M
$$

$$
S^{1}.
$$

$$
p\\in P
$$

$$
i\_{p}
$$

$$
S^{1}\\ni e^{\\mathbf{i}t}\\mapsto p\\cdot e^{\\mathbf{i}t}\\in P.
$$

Suppose _r_ is a Hermitian connection as in the above example. Show that
r naturally deflnes a 1-form! 2 ›1(P) such that

$$
\\omega\\in\\Omega^{1}(P)
$$

$$
i\_{p}^{\*}\\omega=d\\theta,\\quad\\forall p\\in P.
$$

_!_ is called the _global angular form_ determined by _r._ Conversely, show that
any angular form uniquely determines a Hermitian connection on _L._

$$
L.
$$

**Example 1.1.8.** Consider the unit sphere _S2 ‰_ R3 with its canonical orientation as the boundary of the unit ball in R3. Deflne the open cover
fUfi; Uflg by
U = S2 n fsouth poleg

$$
S^{2}\\subset\\mathbb{R}^{3}
$$

$$
\\left{U\_{\\alpha},U\_{\\beta}\\right}
$$

$$
\\mathbb{R}^3
$$

$$
U\_{\\alpha}=S^{2}\\setminus{\\text{soth pole}}
$$

and

$$
U\_{\\beta}=S^{2}\\setminus{\\mathrm{n o r t h;p o l e}}.
$$

We have a natural orientation preserving identiflcation
»

$$
U\_{\\alpha\\beta}\\cong\\mathbb{C}^{\*}.
$$

* * *

Denote by _z_ the complex coordinate on C
the complex line bundle deflned by the gluing cocycle

⁄
. For each n 2 Z denote by Ln

$$
\\mathbb{C}^\*
$$

$$
n\\in\\mathbb{Z}
$$

$$
L\_{n}
$$

$$
z\_{\\beta\\alpha}:\\mathbb{C}^{ _}\\cong U\_{\\alpha\\beta}\\to\\mathbb{C}^{_},\\quad z\\mapsto z^{n}.
$$

Suppose _r_ is a connection on _L_ deflned locally by

!fi,!fl where

$$
\\nabla
$$

$$
\\omega\_{\\alpha},\\omega\_{\\beta}
$$

$$
\\omega\_{\\beta}=-n\\frac{d z}{z}+\\omega\_{\\alpha}.
$$

Denote by _F_ its curvature. It is a complex valued 2-form on _S2_ and thus
it can be integrated over the 2-sphere. Denote by D§ the upper/lower
hemisphere. D+ is identifled in an orientation preserving fashion with the
unit disk _fjzj•1g‰C._ We have
Z Z Z Z

$$
S^{2}
$$

$$
D\_{\\pm}
$$

$$
D\_{+}
$$

$$
{\|z\|\\leq1}\\subset\\mathbb{C}
$$

$$
\\begin{align\*}\\int\_{S^2}F=\\int\_{D\_+}&d\\omega\_\\alpha+\\int\_{D\_-}d\\omega\_\\beta=\\int\_{\\partial D\_+}(\\omega\_\\alpha-\\omega\_\\beta)\\&=n\\int\_{\\partial D\_+}\\frac{dz}{z}=2\\pi\\mathbf{i}n.\\end{align\*}
$$

We arrive at several amazing conclusions.

_†_ The integral of _F_

r is independent of r!!!

$$
\\nabla
$$

$$
F\_{\\nabla}
$$

_†_ The integral of _F_

r is an integer multiple of 2…i !!!

$$
F\_{\\nabla}
$$

† The line bundle Ln with n 6
= 0 cannot admit at connections so that the
noncommutativity of partial derivatives is present for _any_ covariant method

$$
L\_{n}
$$

$$
n\\neq0
$$

of difierentiation !!!
_†_ The line bundle which admits a at connection !!! _L_
C

nwith _n 6_
= 0 is not isomorphic to the trivial line bundle

$$
L\_{n}
$$

$$
n\\neq0
$$

$$
\\mathbb{C}
$$

## C Exercise 1.1.14.

**Exercise 1.1.14.** Prove that the line bundle _L1_ in the above example is
»
isomorphic to the universal line bundle over CP1 = S2.

$$
L\_{1}
$$

$$
\\mathbb{C}\\mathbb{P}^1\\cong S^2
$$

The above conclusions do not represent an isolated occurrence. They
are manifestations of a more general construction called _Chern-Weil theory._
Below we describe a few particular cases of this construction.

**1.1.2. Chern-Weil theory.** Consider a complex vector bundle _E!M_
and _r_ an arbitrary connection on it. Set _n_ = rank (E). The curvature _F_ (r)
can be viewed either as a 2-form on _M_ whose coe–cients are endomorphisms
of _E_ or as a _n £ n_ matrix with entries complex valued 2-forms on _M._ The
multiplication of even-dimensional forms is commutative so we can speak of
determinants of such matrices. Then
¶

$$
n=\\operatorname{rank}\\left(E\\right)
$$

$$
E\\rightarrow M
$$

$$
F(\\nabla)
$$

$$
c(E,\\nabla):=\\operatorname\*{d e t}\\left(\\mathbf{1}\_{E}+\\frac{\\mathbf{i}}{2\\pi}F(\\nabla)\\right)
$$ is a nonhomogeneous element,

$$
c(E,\\nabla)\\in\\Omega^{e v e n}(M)\\otimes\\mathbb{C}:=\\bigoplus\_{k\\geq0}\\Omega^{2k}(M)\\otimes\\mathbb{C}.
$$

The component of degree 2k is denoted by ck(E; r) and is called the k-th
_Chern form_ of _E_ corresponding to the connection _r._ Note that

$$
c\_{k}(E,\\nabla)
$$

$$
c\_{1}(E,\\nabla)=\\frac{\\mathbf{i}}{2\\pi}\\mathrm{tr}\\left(F(\\nabla)\\right)\\in\\Omega^{2}(M)\\otimes\\mathbb{C},
$$

$$
c\_{n}(E,\\nabla)=\\left(\\frac{\\mathbf{i}}{2\\pi}\\right)^{n}\\det(F(\\nabla))\\in\\Omega^{2n}(M)\\otimes\\mathbb{C}.
$$

Example 1.1.9. Consider again the line bundle Ln! S2. The computations in Example 1.1.8 show that
Z

$$
L\_{n}\\rightarrow S^{2}
$$

$$
\\int\_{S^{2}}c\_{1}(L\_{n},\\nabla)=-n
$$

$$
L\_{n}
$$

for any connection on Ln.

The above nice accident is a special case of the following theorem.

**Theorem 1.1.10. (Chern-Weil)** _(a) The Chern forms c_
_for any k and any connection r on E._

k(E; r) are closed

$$
c\_{k}(E,\\nabla)
$$

_(b) For any connections r0, r1 on E and any k 2_ Z
_form T(r1; r0_) _on M such that_

+ there exists a (2k ¡1)-

$$
\\nabla^{0},\\nabla^{1}
$$

$$
k\\in\\mathbb{Z}\_{+}
$$

$$
T(\\nabla^{1},\\nabla^{0})
$$

$$
c\_{k}(E,\\nabla^{1})-c\_{k}(E,\\nabla^{0})=dT(\\nabla^{1},\\nabla^{0}).
$$

For a proof of this theorem we refer to \[ **105\].**
shows that ck(E; r) deflnes a cohomology class in H
(b) is _independent_ of _r._ We denote this class by _c_
_k_-th _Chern characteristic class_ of _E._ The element

Part (a) of this theorem
2k(M;R) which by part
k(E) and we call it the

$$
c\_{k}(E,\\nabla)
$$

$$
H^{2k}(M,\\mathbb{R})
$$

$$
c\_{k}(E)
$$

$$
c(E)=1+c\_1(E)+c\_2(E)+\\cdots
$$

is called the _total Chern class_ of _E._ Note that if _E_ is trivial then all classes
ck(E) vanish. We can turn this statement around and conclude that if one
of the classes ck(E) is not trivial then E is certainly not trivial. Thus these
classes provide a measure of nontriviality of a complex vector bundle.

$$
c\_{k}(E)
$$

$$
c\_{k}(E)
$$

**Remark 1.1.11.** The computations in Example 1.1.8 show that
Z

$$
\\int\_{S^{2}}c\_{1}(L\_{n})=-n
$$

so that in particular Ln is nontrivial and c1(Ln) 2 H2(S2;Z). One can
show that for any smooth manifold _M_ and any complex vector bundle _E !_
M the characteristic class ck(E) belongs to the image of H2k(M;Z) inside

$$
L\_{n}
$$

$$
c\_{1}(L\_{n})\\in H^{2}(S^{2},\\mathbb{Z})
$$

$$
E\\rightarrow
$$

$$
c\_{k}(E)
$$

$$
H^{2k}(M,\\mathbb{Z})
$$

* * *

H2k(M;R). If we denote by { the natural morphism H2(M;Z)! H2(M;R)
then one can show that
top

$$
H^{2k}(M,\\mathbb{R})
$$

$$
H^{2}(M,\\mathbb{Z})\\rightarrow H^{2}(M,\\mathbb{R})
$$

$$
c\_{1}(L)=\\imath(c\_{1}^{top}(L))
$$

where the topological flrst Chern class was deflned in Remark 1.1.3.

Deflne the _Chern polynomial_ of _E_
X

by

$$
c\_{t}(E)=\\sum\_{k\\geq0}c\_{k}(E)t^{k}\\in H^{\*}(M,\\mathbb{R})\[t\].
$$

**Exercise 1.1.15.** Show that

$$
c\_{t}(E\_{1}\\oplus E\_{2})=c\_{t}(E\_{1})\\cdot c\_{t}(E\_{2})
$$

where for simplicity we denoted by

Ln
Show that if E = Li, where Li
i=1

¢" the ^-multiplication in ›even(M).
are complex line bundles then
X

$$
\\text{、}
$$

$$
\\Omega^{\\mathit{even}}(M)
$$

$$
\\hat{E}=\\bigoplus\_{i=1}^{n}\\tilde{L}\_{i}
$$

$$
L\_{i}
$$

$$
c\_{k}(E)=\\sigma\_{k}(y\_{1},\\cdots,y\_{n}):=\\sum\_{1\\leq i\_{1}<\\cdots i\_{k}\\leq n}y\_{i\_{1}}\\cdots y\_{i\_{k}}
$$

where yi:= c1(Li).

$$
y\_{i}:=c\_{1}(L\_{i})
$$

**Exercise 1.1.16.** Consider a complex line bundle
oriented Riemann surface §.

_L_ over a compact, closed,

(a) Show that the quantity

$$
\\deg L:=\\int\_{\\Sigma}c\_{1}(L)
$$

is an integer.

**Hint:** Use the fact that the restriction of _L_ over the complement of a small
disk in § is trivial.

(b) Suppose _u_ is a section of _L_ with only nondegenerate zeros, i.e. for any
¡
x 2 u 1(0) the adjunction map

$$
x\\in u^{-1}(0)
$$

$$
\\mathfrak{a} _{x}:T_{x}\\Sigma\\to L\_{x},\\quad T\_{x}\\Sigma\\ni\\zeta\\mapsto\\left(\\nabla\_{\\zeta}u\\right)\\mid\_{x}\\in L\_{x}
$$

¡
(r some connection on L) is invertible. For each x 2 u 1(0) set

$$
x\\in u^{-1}(0)
$$

$$
\\deg(x):=\\operatorname{sign}\\det\\mathfrak{a}\_{x}.
$$

$$
\\deg L:=\\sum\_{x\\in u^{-1}(0)}\\deg(x).
$$

Show that

S
Hint: Use the fact that L is trivial outside ¡1(0) Dx, where Dx denotes
x2u
a very small disk centered at _x._

$$
\\bigcup\_{x\\in u^{-1}(0)}D\_{x}
$$

$$
D\_{x}
$$

* * *

Deflne the _Chern character_ of a vector bundle to be the cohomology
class
¶k
i X 1 **i**

$$
\\mathbf{ch}\\left(E\\right):=\\mathrm{tr}\\exp(\\frac{\\mathbf{i}}{2\\pi}F(\\nabla))=\\sum\_{k\\geq0}\\frac{1}{k!}\\mathrm{tr}\\left(\\frac{\\mathbf{i}}{2\\pi}F(\\nabla)\\right)^k.
$$

Again this is a closed form whose cohomology class is independent of _r._

**Exercise 1.1.17.** (a) Show that if _L!M_ is a complex line bundle then

$$
\\mathrm{ch}(L)=\\exp(c\_1(L)).
$$

(b) Show that

$$
\\mathbf{c}\\mathbf{h}(E\_{1}\\oplus E\_{2})=\\mathbf{c}\\mathbf{h}\\left(E\_{1}\\right)+\\mathbf{c}\\mathbf{h}\\left(E\_{2}\\right)
$$

and

$$
\\mathbf{ch}\\left(E\_{1}\\otimes E\_{2}\\right)=\\mathbf{ch}\\left(E\_{1}\\right)\\cdot\\mathbf{ch}\\left(E\_{2}\\right).
$$

The construction of the Chern character has a multiplicative counterpart. Suppose that _f_ (T) is a formal power series
X

$$
f(T):=\\sum\_{n\\geq o}a\_n T^n\\in\\mathbb{C}\[\[T\]\]
$$

⁄
such that _a0_ = 1\. _IfE!M_ is a complex vector bundle then _f_ (E) _2 H_ (M)
is the cohomology class represented by
‡X ·
¡ i ¢

$$
a\_{0}=1
$$

$$
E\\rightarrow M
$$

$$
f(E)\\in H^\*(M)
$$

$$
f(E,\\nabla):=\\operatorname\*{d e t}\\Bigl(\\sum\_{n\\geq0}a\_{n}\\bigl(\\frac{\\mathbf{i}}{2\\pi}F(\\nabla)\\bigr)^{n}\\Bigr).
$$

A special case frequently encountered in geometry is that of
1
X

$$
\\mathbf{t}\\mathbf{d}\\left(T\\right):=\\frac{T}{1-\\exp(-T)}=1+\\frac{1}{2}T+\\sum\_{k=1}^{\\infty}(-1)^{k-1}\\frac{B\_{k}}{(2k)!}T^{2k}
$$

where the coe–cients Bk are known as the Bernoulli numbers. Here are a
few values of these numbers
1 1 1

$$
B\_{k}
$$

$$
B\_{1}=\\frac{1}{6},\\quad B\_{2}=\\frac{1}{30},\\quad B\_{3}=\\frac{1}{42},\\quad\\cdots
$$

The cohomology class obtained in this manner is called the _Todd genus_ of
_E_ and is denoted by **td** (E).

Both **ch** and **td** decompose into homogeneous parts
X X

$$
\\mathbf{ch}(E)=\\sum\_{i\\geq0}\\mathbf{ch} _{i}(E),\\mathbf{td}(E)=\\sum_{i\\geq0}\\mathbf{td}\_{i}(E)
$$

expressible in terms of the Chern classes ci. For example

$$
c\_{i}
$$

$$
\\mathbf{ch}\_{0}(E)=\\operatorname{rank}(E),
$$

(1.1.2)

$$
\\mathrm{ch} _{1}(E)=c_{1}(E),\\quad\\mathrm{ch} _{2}(E)=\\frac{1}{2}(c_{1}(E)^{2}-2c\_{2}(E))
$$

* * *

$$
\\mathrm{td} _{0}(E)=1,\ \\mathrm{td}_{1}(E)=\\frac{1}{2}c\_{1}(E),\ \\mathrm{td} _{2}(E)=\\frac{1}{12}\\Big(c_{1}(E)^{2}+2c\_{2}(E)\\Big).
$$

(1.1.3)

So far we have considered only complex vector bundles. There is a real
theory as well. Consider a real vector bundle _E!M_ and _r_ an arbitrary
connection on it. We deflne the _total Pontryagin form_ associated to _E(r_)
by
1

$$
E(\\nabla)
$$

$$
p(E,\\nabla)=\\operatorname\*{d e t}(\\mathbf{1}-\\frac{1}{2\\pi}F(\\nabla)).
$$

2…
Again one can prove that this is a closed form whose cohomology class is
independent of _r._ This time a new phenomenon arises.

**Lemma 1.1.12.** _The components of p(E; r_) _of degree 4k +2are exact._

$$
p(E,\\nabla)
$$

$$
4k+2
$$

**Exercise 1.1.18.** Prove the above lemma.

The cohomology class _p(E_) decomposes as

$$
p(E)
$$

$$
p(E)=1+p\_{1}(E)+p\_{2}(E)+\\cdots+p\_{k}(E)+\\cdots
$$

where

$$
p\_{k}(E)\\in H^{4k}(M,\\mathbb{R}).
$$

The cohomology classes are called the _Pontryagin classes_ of the real vector
bundle _E._ For example, _p1(E_) can be represented by the form
1

$$
p\_{1}(E)
$$

$$
p\_{1}(E,\\nabla)=-\\frac{1}{8\\pi^{2}}\\mathrm{tr}\\left(F(\\nabla)\\wedge F(\\nabla)\\right).
$$

**Exercise 1.1.19.** Suppose _E!M_
Ec its complexiflcation E › C. Show that

is a real vector bundle and denote by

$$
E\\rightarrow M
$$

$$
E^{c}
$$

$$
E\\otimes\\mathbb{C}.
$$

$$
c\_{2k+1}(E^{c})=0\\quad\\mathrm{and}\\quad c\_{2k}(E^{c})=(-1)^{k}p\_{k}(E).
$$

#### 1.2. Basic facts about elliptic equations

Before we begin talking about elliptic equations we must flrst deflne the notion of partial difierential operator (p.d.o. for brevity) on a smooth manifold
and explain the basic operations one can perform on such objects. We refer
again to **\[105\]** for more details.

Consider a smooth, oriented Riemannian manifold _(M; g)_ and _E; F ! M_
complex Hermitian vector bundles over _M._ We will denote the Hermitian
metrics on E (resp. F) byh¢; ¢iE (resp. h¢; ¢iF).

$$
(M,g)
$$

$$
E,F\\rightarrow M
$$

$$
\\langle\\cdot,\\cdot\\rangle\_{E}
$$

$$
\\langle\\cdot,\\cdot\\rangle\_{F})
$$

Denote by **Op** _(E; F)_ the space of C-linear operators

$$
T:C^{\\infty}(E)\\to C^{\\infty}(F).
$$

Denote by C1(M) the space of complex valued smooth functions on M. The
spaces C1(E) and C1(F) have natural structures of C1(M)-modules and

$$
C^{\\infty}(M)
$$

$$
C^{\\infty}(E)
$$

$$
C^{\\infty}(F)
$$

$$
C^{\\infty}(M)
$$ we will be interested in a subspace of **Op** consisting of operators interacting
in a nice way with these module structures.

For each f 2 C1(M) and each T 2 Op (E; F) deflne ad(f)(T) 2
Op(E; _F_) by

$$
f\\in C^{\\infty}(M)
$$

$$
T;\\in;\\mathbf{Op}\\left(E,F\\right)
$$

$$
ad(f)(T)\\in
$$

$$
\\mathbf{O}\\mathbf{p}(E,F)
$$

$$
(a d(f)T)u=\[T,f\]u:=T(f u)-f(T u),\\quad\\forall u\\in C^{\\infty}(E).
$$

Note that the maps _T 7! \[T;f\]_ and _f 7! \[T;f\]_ behave like derivations, i.e.
they satisfy the Leibniz rule

$$
f\\mapsto\[T,f\]
$$

$$
T\\mapsto\[T,f\]
$$

(1.2.1)

$$
\[ST,f\]=\[S,f\]T+S\[T,f\]\\text{and}\[T,fg\]=\[T,f\]g+f\[T,g\]
$$

for all _f; g; T; S_ for which the above operations make sense.

$$
f,g,T,S
$$

Now deflne inductively an increasing sequence of subspaces

$$
\\mathbf{PDO}^{(0)}(E,F)\\subset\\mathbf{PDO}^{(1)}(E,F)\\subset\\cdots\\subset\\mathbf{PDO}^{(k)}(E,F)\\subset\\cdots
$$

following the prescriptions

$$
\\mathrm{PDO}^{(0)}(E,F):=\\mathrm{Hom}(E,F)
$$

and

$$
\\begin{aligned}{}&{{}\\mathbf{PDO}^{(k+1)}(E,F)}\ {:=\\Big{T\\in\\mathbf{Op}\\left(E,F\\right)}&{{};;\[T,f\]\\in\\mathbf{PDO}^{(k)}(E,F),;\\forall f\\in C^{\\infty}(M)\\Big}.}\ \\end{aligned}
$$

The elements of PDO(k)(E; F) will be called partial difierential operators
_of order • k._

$$
\\mathbf{PDO}^{(k)}(E,F)
$$

$$
of order\\leq k
$$

**Example 1.2.1.** (a) Let _E_ = _F_ = C and let _X_ be a smooth vector fleld on
M. Then the Lie derivative LX : C1(M)! C1(M), u 7! LX u, is a p.d.o.
of order at most 1. Indeed, for any u; f 2 C1(M) we have

$$
E=F=\\underline{\\mathbb{C}}
$$

$$
L\_{X}:C^{\\infty}(M)\\to C^{\\infty}(M),:u\\mapsto L\_{X}u
$$

$$
u,f\\in C^{\\infty}(M)
$$

$$
\[L\_{X},f\]u=L\_{X}(f u)-f(L\_{X}u)=(L\_{X}f)u
$$

so that _\[LX;f\]_ is the endomorphism ( _LX f)†._

$$
\\left\[L\_{X},f\\right\]
$$

$$
(L\_{X}f)\\bullet
$$

⁄ ⁄
(b) Let _E_ = _F_ =⁄T _M._ Then the exterior derivative

$$
E=F=\\Lambda^{ _}T^{_}M
$$

$$
d:\\Omega^ _(M)\\to\\Omega^_(M)
$$

is a p.d.o. of order at most 1. Indeed, for any f 2 C1(M) and any
_! 2_ ›⁄ (M) we have

$$
f;\\in;C^{\\infty}(M)
$$

$$
\\omega\\in\\Omega^\*(M)
$$

$$
\[d,f\]\\omega=d(f\\omega)-f(d\\omega)=df\\wedge\\omega.
$$

Thus _\[d; f\]_ is the endomorphism

⁄ ⁄
_df ^†of_ ⁄ _T M._

$$
\\Lambda^{ _}T^{_}M
$$

$$
\\left\[d,f\\right\]
$$

(c) Consider the Laplacian ¢ = _¡@_
at most 2. Indeed, for any _f 2 C_
(1.2.1)
\[@2;f\]† = 2\[@\
\
x2 on C1(R). Then ¢ is a p.d.o. of order\
1(R) we deduce from the Leibniz rule\
_;f\]@ † +(@2f_) _† :_

$$
\\Delta=-\\partial\_{x}^{2};on;C^{\\infty}(\\mathbb{R})
$$

$$
\\Delta
$$

$$
a p.d.o.
$$

$$
f\\in C^{\\infty}(\\mathbb{R})
$$

$$
\[\\partial\_{x}^{2},f\]\\bullet=2\[\\partial\_{x},f\]\\partial\_{x}\\bullet+\\bigr(\\partial\_{x}^{2}f\\bigr)\\bullet.
$$

* * *

(@x2f) is the zeroth order operator deflned as multiplication by @x2f. The
computation in part (a) shows that \[@x;f\] is the operator of multiplication
by @xf. Hence the commutator \[@x2;f\] is the Lie derivative along the vector
df
fleld dx@x which by part (a) is a flrst order p.d.o.

$$
(\\partial\_{x}^{2}f)
$$

$$
\\partial\_{x}^{2}f.
$$

$$
\\left\[\\partial\_{x},f\\right\]
$$

$$
\\partial\_{x}f
$$

$$
\[\\partial\_{x}^{2},f\]
$$

$$
\\frac{df}{dx}\\partial\_{x}
$$

Suppose L 2 PDO(k)(E; F) and choose f1; ¢¢¢; fk 2 C1(M). Then

$$
L\\in\\mathbf{PDO}^{(k)}(E,F)
$$

$$
f\_{1},\\cdots,f\_{k}\\in C^{\\infty}(M)
$$

$$
A\_{L}(f\_{1},\\cdot\\cdot\\cdot f\_{k}):=\[\[L,f\_{1}\],\\cdot\\cdot\\cdot,f\_{k}\]\\in\\operatorname{Hom}{(E,F)}.
$$

One can prove the following.

† AL(f1; ¢¢¢; fk) is symmetric in its arguments.

$$
A\_{L}(f\_{1},\\cdots,f\_{k})
$$

† If df i(x0)=dgi(x0) for all i = 1; ¢¢¢;k then

$$
\\mathrm{If};df\_i(x\_0)=dg\_i(x\_0)
$$

$$
i=1,\\cdots,k
$$

$$
A\_{L}(f\_{1},\\cdots,f\_{k})\\mid\_{x\_{0}}=A\_{L}(g\_{1},\\cdots,g\_{k})\\mid\_{x\_{0}}.
$$

Thus AL(f1; ¢¢¢; fk) jx0depends only on the quantities »i:= df i(x0) and the
symmetry property shows that it is completely determined by
1

$$
A\_{L}(f\_{1},\\cdots,f\_{k})\\left\| _{x_{0}}\\right.
\\xi\_{i}:=d f\_{i}(x\_{0})
$$

$$
\\sigma\_{L}(\\xi):=\\frac{1}{k!}A\_{L}(\\xi,\\cdots,\\xi).
$$

The quantity L(¢) is called the (principal) symbol of L. It is a bundle
morphism
⁄ ⁄
(¢):… _E!… F_

$$
\\sigma\_{L}(\\cdot)
$$

$$
\\sigma\_{L}(\\cdot):\\pi\_{k}^{ _}E\\rightarrow\\pi\_{k}^{_}F
$$

⁄
where …k: SkT M!M denotes the canonical projection of the k-th sym-
⁄
metric power of T M. A p.d.o. L 2 PDO(k) is said to have order k if its
symbol is not trivial. The set of _k_-th order operators will be denoted by
PDOk.

$$
\\pi\_{k}:S^{k}T^{\*}M\\rightarrow M
$$

$$
T^{\*}M
$$

$$
L\\in\\mathbf{PDO}^{(k)}
$$

$$
\\mathbf{PDO}^{k}
$$

1
Proposition 1.2.2. If L1 2 PDO(k) _then_
L2 – L1 2 PDO(k

2
(E1; E2) and L2 2 PDO(k)(E2; E3)
_+k_)(E1; E3)

$$
L\_{1}\\in\\mathbf{PDO}^{(k\_{1})}(E\_{1},E\_{2})
$$

$$
L\_{2}\\in\\mathbf{PDO}^{(k\_{2})}(E\_{2},E\_{3})
$$

$$
L\_{2}\\circ L\_{1}\\in\\mathrm{PDO}^{(k\_{1}+k\_{2})}(E\_{1},E\_{3})
$$

_and_

$$
\\sigma\_{L\_{2}\\circ L\_{1}}(\\xi)=\\sigma\_{L\_{2}}(\\xi)\\circ\\sigma\_{L\_{1}}(\\xi),\\quad\\forall x\\in M,\\quad\\forall\\xi\\in T\_{x}^{\*}M\\setminus{0}.
$$

Example 1.2.3. Suppose r : C1(E)
tion. Then setting _»_ = _df_ we deduce

⁄
! C1(T M › E) is a linear connec-

$$
\\nabla:C^{\\infty}(E)\\to C^{\\infty}(T^{\*}M\\otimes E)
$$

$$
\\xi=d f
$$

$$
A\_{\\nabla}(\\xi)u=\[\\nabla,f\]u=\\xi\\otimes u,\\quad\\forall u\\in C^{\\infty}(E).
$$

$$
\\sigma\_{L}(\\xi)=\\xi\\otimes\\bullet
$$

Thus L(»)=» › †. Similarly, for the exterior derivative

$$
d:\\Omega^ _(M)\\to\\Omega^_(M)
$$

the symbol is given by

$$
\\sigma\_{d}(\\xi)=\\xi\\wedge\\bullet.
$$

PN
2
If ¢ := ¡ @i: C1(RN)! C1(RN) is the (geometers’) Laplacian on
i=1
RN then ‡X ·
2
(»)=¡j»j † = ¡ j» j2 † :

$$
\\Delta:=-\\sum\_{i=1}^{N}\\partial\_{i}^{2}:C^{\\infty}(\\mathbb{R}^{N})\\to C^{\\infty}(\\mathbb{R}^{N})
$$

$$
\\mathbb{R}^{N}
$$

$$
\\sigma\_{\\Delta}(\\xi)=-\|\\xi\|^{2}\\bullet=-\\left(\\sum\_{i}\|\\xi\_{i}\|^{2}\\right)\\bullet.
$$

* * *

**Deflnition 1.2.4.** A _generalized Laplacian_ on a vector bundle _E_ over a Riemannian manifold (M; g) is a second order operator L : C1(E)! C1(E)
such that
( _»)=¡j»j21 :_

$$
(M,g)
$$

$$
L:C^{\\infty}(E)\\rightarrow C^{\\infty}(E)
$$

$$
\\sigma\_{L}(\\xi)=-\|\\xi\| _{g}^{2}\\mathbf{1}_{E}.
$$

**Deflnition 1.2.5.** If _L 2_ **PDO(E;** _F_
mitian vector bundles then a _formal adjoint_
C1(E) such that
Z

) is a p.d.o.
Z

acting between two Her-
⁄
is a p.d.o. L : C1(F)!

$$
L\\in\\mathbf{PDO}(E,F)
$$

$$
C^{\\infty}(E)
$$

$$
L ^ {\*}: C ^ {\\infty} (F) \\rightarrow
$$

$$
\\int\_{M}(L u,v) _{F}d v_{g}=\\int\_{M}(u,L^{\*}v) _{E}d v_{g}
$$

for all compactly supported sections u 2 C1(E) and v 2 C1(F).

$$
u\\in C^{\\infty}(E)
$$

$$
v\\in C^{\\infty}(F)
$$

For a proof of the following result and examples we refer to \[ **105\].**

**Proposition 1.2.6.** _Every k-th order operator L admits a unique formal_ _adjoint L⁄ which is a k-th order operator whose symbol is given by_

$$
L^{\*}
$$

$$
\\sigma\_{L^ _}(\\xi)=(-1)^k\\sigma\_L(\\xi)^_.
$$

A p.d.o. _L_ is called _formally selfadjoint_

⁄
if _L_ = _L._

$$
L=L^{\*}
$$

**Example 1.2.7.** (a) Suppose _E!F_ is a Hermitian vector bundle over a
Riemannian manifold _(M; g)_ and _r_ is a Hermitian connection on _E._ Then
for every vector fleld X on M the covariant derivative rX is a flrst order
p.d.o. C1(E)! C1(E) with formal adjoint
⁄

$$
E\\rightarrow F
$$

$$
(M,g)
$$

$$
\\nabla\_{X}
$$

$$
C^{\\infty}(E)\\rightarrow C^{\\infty}(E)
$$

$$
\\nabla\_{X}^{\*}=-\\nabla\_{X}-\\mathrm{div}\_{g}(X)
$$

where **div**

g(X) is the scalar deflned by

$$
\\mathrm{div}\_{g}(X)
$$

$$
L\_{X}d v\_{g}=\\mathrm{div} _{g}(X)\\cdot d v_{g}.
$$

⁄
(b) If E, r are as above then r r : C1(E)! C1(E) is a generalized
Laplacian called the _covariant Laplacian_ determined by the connection _r._

$$
\\nabla^{\*}\\nabla:C^{\\infty}(E)\\rightarrow C^{\\infty}(E)
$$

(c) The formal adjoint of the exterior derivative

$$
d:\\Omega^{k}(M)\\rightarrow\\Omega^{k+1}(M)
$$

is the operator

$$
d^{\*}=(-1)^{\\nu\_{n,k}} _d_:\\Omega^{k+1}(M)\\rightarrow\\Omega^{k}(M)
$$

where n = dimM, ”n;k = nk + n + 1 and

_⁄_ is the Hodge _⁄_-operator.

$$
\\nu\_{n,k}=nk+n+1
$$

$$
(\\bar{d}+\\bar{d}^{ _})^{2}=d d^{_}+d^{ _}\\bar{d}:\\Omega^{_}(M)\\to\\Omega^{\*}(M)
$$

(d) The operator ( _d_ \+ d⁄)2 = _dd⁄_ \+ _d⁄ d_ :›⁄(M)! ›⁄ (M) is a generalized
Laplacian called the _Hodge Laplacian._

The covariant Laplacian in the above example is in some sense the basic
example of generalized Laplacian. More precisely, we have the following
result. We refer to **\[12\]** for a difierent proof.

* * *

Proposition 1.2.8. Suppose L : C1(E)! C1(E) is a formally selfadjoint
_generalized Laplacian. Then there exists a_ Hermitian _connection on E and_
_a_ symmetric _endomorphism R_ : _E!E such that_

$$
L:C^{\\infty}(E)\\rightarrow C^{\\infty}(E)
$$

$$
\\mathcal{R}:E\\rightarrow E
$$

$$
L=\\nabla^{\*}\\nabla+\\mathcal{R}.
$$

_We will refer to such a presentation of a generalized Laplacian as a_ Weitzenb˜ock presentation. _The endomorphism R is called the_ Weitzenb˜ock remainder _of L._

**Proof** Choose an arbitrary Hermitian connection _r_ on _E._ Then _L0_ =
⁄
_r r_ is a generalized Laplacian so that _L¡L0_ is a formally selfadjoint flrst
order operator which can be represented as

$$
\\nabla^{\*}\\nabla
$$

$$
L\_{0}=
L-L\_{0}
$$

$$
L-L\_{0}=A\\circ\\nabla+B
$$

where

$$
A:C^{\\infty}(T^{\*}M\\otimes E)\\rightarrow C^{\\infty}(E)
$$

is a bundle morphism and _B_ is an endomorphism of _E._ We will regard _A_
as an End (E)-valued 1-form on _M._ Hence

(1.2.2)

$$
L=\\nabla^\*\\nabla+A\\circ\\nabla+B.
$$

The connection _r_ induces a connection on End(E) which we continue
to denote by _r:_
r : C1(End (E))! ›1(End (E)):

$$
\\nabla:C^{\\infty}(\\operatorname{End}\\left(E\\right))\\to\\Omega^{1}(\\operatorname{End}\\left(E\\right)).
$$

We deflne the _divergence_ of _A_ by

$$
\\mathbf{div}\_{g}(A):=-\\nabla^{\*}A.
$$

If (ei) is a localsynchronous frame at
have

P
x0 and if A = i Aiei then, at x0, we
X

$$
\\left(e\_{i}\\right)
$$

$$
x\_{0}
$$

$$
A=\\sum\_{i}A\_{i}e^{i}
$$

$$
x\_{0}.
$$

$$
\\mathrm{div} _{g}(A)=\\sum_{i}\\nabla\_{i}A\_{i}.
$$

Since _L¡L0_ is formally selfadjoint we deduce

$$
L-L\_{0}
$$

$$
A\_{i}^{ _}=-A\_{i},\\quad\\mathrm{div}\_{g}(A)=B^{_}-B.
$$

We seek a Hermitian connection _r_ ~
symmetric endomorphism _R_ of _E_

= r + C, C 2 ›1(End (E)) and a
such that

$$
\\tilde{\\nabla}=\\nabla+C,C\\in\\Omega^{1}(\\operatorname{End}(E))
$$

$$
\\tilde{\\nabla}^{ _}\\tilde{\\nabla}+\\mathcal{R}=\\nabla^{_}\\nabla+A\\circ\\nabla+B.
$$

To determine the terms _C_ and _R_ we work locally, using a _synchronous_ local
frame (ei) atx0. Then
X

$$
\\left(e\_{i}\\right)
$$

$$
x\_{0}
$$

$$
\\tilde{\\nabla}=\\sum\_{i}e^{\\tilde{i}}\\otimes(\\nabla\_{i}+C\_{i}),\\quad C\_{i}^{\*}=-C\_{i},\\quad\\forall i.
$$

* * *

Then, as in \[ **105\],** Example 9.1.26, we deduce that, at _x0,_
X

$$
x\_{0}
$$

$$
\\tilde{\\nabla}^{\*}\\tilde{\\nabla}=-\\sum\_{i}(\\nabla\_{i}+C\_{i})(\\nabla\_{i}+C\_{i})
$$

$$
\\begin{align\*}\\left(\\langle C\_{i}\\rangle^{2}:=C\_{i}C\_{i}^{ _}=-C\_{i}^{2}\\right)\\quad\\=-\\sum\_{i}\\nabla\_{i}^{2}-\\sum\_{i}\\nabla\_{i}C\_{i}-2\\sum\_{i}C\_{i}\\nabla\_{i}+\\sum\_{i}\\langle C\_{i}\\rangle^{2}.\\end{align_}
$$

$$
\\begin{array}{r l}&{(\\langle C\\rangle^{2}=\\sum\_{i}\\langle C\_{i}\\rangle^{2})}\ &{\\quad=\\nabla^{ _}\\nabla-2C\\circ\\nabla-\\mathbf{div}\_{g}(C)+\\langle C\\rangle^{2}=\\nabla^{_}\\nabla+A\\circ\\nabla+B-\\mathcal{R}.}\\end{array}
$$

We deduce immediately that

(1.2.3)

$$
C=-\\frac{1}{2}A,\\quad\\mathcal{R}=B-\\frac{1}{2}\\mathbf{div}\_{g}(A)-\\langle C\\rangle^{2}=\\frac{1}{2}(B+B^{\*})-\\frac{1}{4}\\langle A\\rangle^{2}.
$$

The proposition is proved. ¥

Besides their nice algebraic properties, the generalized Laplacians enjoy
many nice analytic features. They all derive from the _ellipticity_ of these
operators.

**Deflnition 1.2.9.** Let _E; F ! M_ be two smooth vector bundles over the
smooth manifold M. A p.d.o. T 2 PDOk(E; F) is said to be elliptic if for
any x 2 M and any »2Tx⁄M n f0g the linear map T (»): Ex! Fx is an
isomorphism.

$$
T\\in\\mathbf{PDO}^k(E,F)
$$

$$
x\\in M
$$

$$
\\xi\\in T\_{x}^{\*}M\\setminus{0}
$$

$$
\\sigma\_{T}(\\xi):E\_{x}\\to F\_{x}
$$

Clearly, the generalized Laplacians are elliptic second order operators.
The operator _d_ \+ _d⁄_ of Example 1.2.7 (d) is elliptic because ( _d_ \+ d⁄)2 is a
generalized Laplacian. This feature is so frequently encountered in geometry
that it was given a name.

$$
d+d^{\*}
$$

$$
(d+d^{\*})^{2}
$$

**Deflnition 1.2.10.** A _Dirac operator_
C1(F) such that D2 is a generalized Laplacian.

is a flrst order operator D : C1(E)!

$$
D:C^{\\infty}(E)\\rightarrow
$$

$$
C^{\\infty}(F)
$$

$$
D^{2}
$$

Frequently, the Dirac operators are obtained
⁄
**PDO1(E;** _F_) such that both _D D_
Then • ‚
⁄
0 _D_

from an operator _D 2_
and _DD⁄_ are generalized Laplacians.

$$
D\\in
$$

$$
\\mathbf{PDO}^{1}(E,F)
$$

$$
D^{\*}D
$$

$$
DD^{\*}
$$

$$
\\tilde{D}:=\\left\[\\begin{array}{c c}{0}&{D^{\*}}\ {D}&{0}\ \\end{array}\\right\]:C^{\\infty}(E\\oplus F)\\rightarrow C^{\\infty}(E\\oplus F)
$$

is a Dirac operator.

To discuss the basic analytic properties of elliptic operators we need to
introduce a suitable analytical framework. For geometric applications the
Sobolev and H˜older spaces provide such a framework.

To deflne these spaces we need two things: an oriented Riemannian
manifold _(M; g)_ and a K-vector bundle _…_ : _E!M_ endowed with a metric

$$
(M,g)
$$

$$
\\pi:E\\rightarrow M
$$ h = h¢; ¢i and a connection r = rE compatible with h. The metric g = (¢; ¢)
deflnes two important objects:

$$
\\nabla=\\nabla^{E}
$$

$$
h=\\langle\\cdot,\\cdot\\rangle
$$

$$
g=\\left(\\cdot,\\cdot\\right)
$$

(i) the Levi-Civita connection rg and

$$
\\nabla^{g}
$$

(ii) a volume form dvg = ⁄1\. In particular, dvg deflnes a Borel measure on
M. We denote by Lp(M;K) the space of K-valued p-integrable functions on
(M; dvg) (modulo the equivalence relation of equality almost everywhere).

$$
dv\_{g}=\*1
$$

$$
d v\_{g}
$$

$$
L^{p}(M,\\mathbb{K})
$$

$$
\\left(M,d v\_{g}\\right)
$$

Deflnition 1.2.11. Let p 2 \[1; 1\]. An Lp-section of E is a Lebesgue mea-
¡
surable map ˆ : M!E (i.e. ˆ 1(U) is Lebesgue measurable for any open
subset _U‰E_) such that:

$$
p\\in\[1,\\infty\]
$$

$$
\\psi:M\\to E;(\\mathrm{i.e.};\\psi^{-1}(U)
$$

$$
U\\subset E)
$$

$$
x\\in M
$$

$$
(\\mathrm {i}) \\pi \\circ \\psi (x) = x
$$

(i) _… – ˆ(x)=x_ for almost all _x 2 M_ except possibly a negligible set.

(ii) The function x 7! ĵ(x)jh belongs to Lp(M;R).

$$
x\\mapsto\|\\psi(x)\|\_{h}
$$

$$
L^{p}(M,\\mathbb{R})
$$