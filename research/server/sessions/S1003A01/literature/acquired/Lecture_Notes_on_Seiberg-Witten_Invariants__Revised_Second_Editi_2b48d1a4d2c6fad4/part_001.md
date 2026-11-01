---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Lecture Notes on Seiberg-Witten Invariants (Revised Second Edition)]

# Lecture Notes on Seiberg-Witten Invariants (Revised Second Edition)

> Source: https://web.math.ucsb.edu/~moore/seibergwittenrev2edition.pdf
> Fetched: 2026-10-09 12:30
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
  "source_url": "https://web.math.ucsb.edu/~moore/seibergwittenrev2edition.pdf",
  "metadata": {
    "provenance_urls": [
      "https://web.math.ucsb.edu/~moore/seibergwittenrev2edition.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Seiberg-Witten exceptional class every tame almost complex structure J-holomorphic subvariety current canonical class minimal symplectic 4-manifold"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

Thus M has complex coordinate systems (z1, z2) = (x1 + iy1, x2 + iy2) which are related holomorphically on overlaps. We can deﬁne a complex multiplication J : TM →TM by J  ∂ ∂xi  = ∂ ∂yi , J  ∂ ∂yi  = −∂ ∂xi .
This is a vector bundle endomorphism which satisﬁes the identity J2 = −I.
More generally, an almost complex structure on a manifold M is simply a vector bundle endomorphism J : TM →TM such that J2 = −I.
An almost complex structure on a four-manifold enables us to construct trivializations of the tangent bundle TM so that the corresponding transi-tion functions take their values in GL(2, C) ⊂GL(4, R). This enables us to regard TM as a complex vector bundle. [...] Index A, 35, 76 almost complex structure, 55 anticanonical bundle, 56, 108 anti-self-dual, 44 Atiyah-Singer Theorem, 70,72 b0, b1, b2, 43 b+, b−, 44 B, 36, 79 e B, 78 Bianchi identity, 18 c1(E), c2(E), 24 canonical bundle, 107 ˇ Cech cohomology, 51 characteristic class, 22 Chern character, 22 Chern class, 24 χ(Σ), χ(M), 27, 69 Cliﬀord algebra, 57 connected sum, 96 connection orthogonal connection, 12 pullback connection, 14 spin connection, 60 unitary connection, 13 universal connection, 13 Yang-Mills connection, 45 covariant derivative, 9 curvature curvature of a connection, 18 Gaussian curvature, 19 Riemann-Christoﬀel curvature, 63 scalar curvature, 63 dA, 10 DA, 65, 66 D+ A, D− A, 69 δ, 41 ∆, 42, 82 de Rham cohomology, 17 Dirac operator, 65,66 Dolgachev surface, 118 Donaldson’s [...] Remark. The theorem o

## Retrieved source content

# Lecture Notes on Seiberg-Witten Invariants (Revised Second Edition)

## John Douglas Moore

## July, 2010

* * *

Preface

Riemannian, symplectic and complex geometry are often studied by means of solutions to systems of nonlinear differential equations, such as the equations of goodesics, minimal surfaces, pseudoholomorphic curves and Yang-Mills connections. For studying such equations, a new unified technology has been developed, involving analysis on infinite-dimensional manifolds.

A striking applications of the new technology is Donaldson's theory of "anti-self-dual" connections on $SU(2)$-bundles over four-manifolds, which applies the Yang-Mills equations from mathematical physics to shed light on the relationship between the classification of topological and smooth four-manifolds. This reverses the expected direction of application from topology to differential equations to mathematical physics. Even though the Yang-Mills equations are only mildly nonlinear, a prodigious amount of nonlinear analysis is necessary to fully understand the properties of the space of solutions.

At the present state of knowledge, understanding smooth structures on topological four-manifolds seems to require nonlinear as opposed to linear PDE's. It is therefore quite surprising that there is a set of PDE's which are even less nonlinear than the Yang-Mills equation, but can yield many of the most important results from Donaldson's theory. These are the Seiberg-Witten equations.

These lecture notes stem from a graduate course given at the University of California in Santa Barbara during the spring quarter of 1995. The objective was to make the Seiberg-Witten approach to Donaldson theory accessible to second-year graduate students who had already taken basic courses in differential geometry and algebraic topology.

In the meantime, more advanced expositions of Seiberg-Witten theory have appeared (notably \[11\] and \[31\]). It is hoped these notes will prepare the reader to understand the more advanced expositions and the excellent recent research literature.

We wish to thank the participants in the course, as well as Vincent Bor- vi

relli, Xianzhe Dai, Guofang Wei and Rick Ye for many helpful discussions on the material presented here.

J. D. MOORE
Santa Barbara
April, 1996

In the second edition, we have corrected several minor errors, and expanded several of the arguments to make them easier to follow. In particular, we included a new section on the Thom form, and provided a more detailed description of the second Stiefel-Whitney class and its relationship to the intersection form for four-manifolds. The pace increases throughout the text, particularly in the last chapter, and the reader is urged to have pencil and paper handy to verify the calculations.

Our thanks go to David Blecker for pointing out that our earlier proof of the Proposition toward the end of §3.9 was incomplete, and to Lev Vertgeim and an anonymous referee for spotting several misprints and minor errors in the text.

J. D. MOORE
Santa Barbara
January, 2001

In this revision of the second edition, we made several minor corrections.

J. D. MOORE
Santa Barbara
August, 2010

* * *

Contents

1 Preliminaries 1
1.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .

* * *

viii CONTENTS

Bibliography 121

Index 124

* * *

Chapter 1

Preliminaries

1.1 Introduction

During the 1980's, Simon Donaldson used the Yang-Mills equations, which had originated in mathematical physics, to study the differential topology of four-manifolds. Using work of Michael Freedman, he was able to prove theorems of the following type:

Theorem A. There exist many compact topological four-manifolds which have no smooth structure.

Theorem B. There exist many pairs of compact simply connected smooth four-manifolds which are homeomorphic but not diffeomorphic.

The nonlinearity of the Yang-Mills equations presented difficulties, so many new techniques within the theory of nonlinear partial differential equations had to be developed. Donaldson's theory was elegant and beautiful, but the detailed proofs were difficult for beginning students to master.

In the fall of 1994, Edward Witten proposed a set of equations (developed jointly with Nathan Seiberg) which give the main results of Donaldson theory in a far simpler way than had been thought possible. The purpose of these notes is to provide an elementary introduction to the equations which Witten proposed. These equations are now known as the Seiberg-Witten equations.

Our goal is to use the Seiberg-Witten equations to give the differential geometric parts of the proofs of Theorems A and B. The basic idea is simple: one constructs new invariants of smooth four-manifolds, invariants which depend upon the differentiable structure, not just the topology.

The reader is assumed to be familiar with many topological invariants

* * *

## 2 CHAPTER 1. PRELIMINARIES

of four-manifolds: the fundamental group1(M), the cohomology groups H k

(M), the cup product, and so forth. These topological invariants have
been around for a long time and have been intensively studied. The Seiberg- Witten equations give rise to new invariants of four-dimensional smooth manifolds, called the Seiberg-Witten invariants. The key point is that homeomorphic smooth four-manifolds may have quite dierent Seiberg- Witten invariants. Just as homology groups have many applications, one might expect the Seiberg-Witten invariants to have many applications to the geometry and dierential topology of four-dimensional manifolds. Indeed, shortly after the Seiberg-Witten invariants were discovered, sev- eral striking applications were found. One application concerns the geometry of embedded algebraic curves in the complex projective plane CP2. Any such curve has a degree, which is simply the number of times the curve intersects a projective line in general position. Algebraic topologists have another way of calculating the degree. A nonsingular algebraic curve can be regarded as the image of a holomorphic embedding i : ! CP2;

being a compact Riemann surface. The degree of the algebraic curve is the integer d such that

i (fundamental class in H2(; Z)) = d (generator of H2(CP2; Z)): (1.1)

In many algebraic geometry texts (for example, page 220 in \[18\]), one can nd a formula for the genus of an embedded algebraic curve:

(d 1)(d 2) g = : 2

Thom conjectured that if is a compact Riemann surface of genus g and

## i : ! CP2

is any smooth embedding, not necessarily holomorphic, then

(d 1)(d 2) g; 2

the degree being dened by (1.1). (One would not expect equality for general embeddings, since one can always increase the genus in a xed homology class by adding small handles.) The Thom conjecture was proven by Kronheimer and Mrowka, Mor- gan, Szabo and Taubes, and Fintushel and Stern, using the Seiberg-Witten

* * *

1.1. INTRODUCTION 3 equations. These notes should give the reader adequate background to read the proof (versions of which are presented in \[22\] and \[32\]). The proof also gives much new information about embeddings of surfaces in four-manifolds other than CP2. Another application of the Seiberg-Witten invariants comes from dier- ential geometry. One of the most studied problems in Riemannian geometry concerns the relationship between curvature and topology of Riemannian manifolds. Perhaps the simplest type of curvature is the scalar curvature

## s : M ! R

of a Riemannian manifold M. The value of the scalar curvature at p is a constant multiple of the average of all the sectional curvatures at p. It is interesting to ask: which compact simply connected Riemannian manifolds admit metrics with positive scalar curvature? Lichnerowicz found the simplest obstruction to the existence of met- rics of positive scalar curvature on compact simply connected manifolds. We will describe the part of Lichnerowicz’s theorem that applies to four- manifolds later. Building upon the work of Lichnerowicz, Gromov and Lawson were able to obtain a relatively complete description of which com- pact simply connected manifolds of dimension 5 admit metrics of positive scalar curvature in terms of the standard topological invariants. (See \[24\], Corollary 4.5, page 301.) As Witten noticed, a compact four-manifold with positive scalar cur- vature must have vanishing Seiberg-Witten invariants. Thus there is an obstruction to the existence of metrics of positive scalar curvature which depends on the dierentiable structure of the four-manifold, not just its topological type. The Seiberg-Witten invariants show that many compact four-manifolds (including all compact algebraic surfaces of \\general type") do not admit metrics of positive scalar curvature. A third application of the Seiberg-Witten equations is to symplectic geometry. Indeed, Taubes \[37\], \[38\] was able to identify the Seiberg-Witten invariants of a compact symplectic four-manifold with Gromov invariants\| as a consequence he obtained an existence theorem for \\pseudoholomorphic curves" in such manifolds. The rapidity with which these new results were obtained suggested that the Seiberg-Witten equations might have yet further applications to the geometry of four-manifolds. The Seiberg-Witten invariants have become one of the standard tools in studying the dierential topology of four- dimensional manifolds. The dierential geometry needed to study the Seiberg-Witten equations is the geometry of spin and spin c structures. To the novice, these topics may

* * *

4 CHAPTER 1. PRELIMINARIES appear unfamiliar and strange, although spinors have long been regarded as important in physics. The tools needed to study spin and spin c structures are the same standard tools needed by all geometers and topologists: vector bundles, connections, characteristic classes and so forth. We will begin by reviewing some of this necessary background.

# 1.2 What is a vector bundle?

Roughly speaking, a vector bundle is a family of vector spaces, parametrized by a smooth manifold M. How does one construct such a family of vector spaces? Suppose rst that the ground eld is the reals and the vector spaces are to be of dimension m, all isomorphic to R m . In this case, one starts with an open covering fU : 2 Ag of M and for each ; 2 A, smooth transition functions g : U \ U! GL(m; R) = fm m nonsingular real matricesg; which satisfy the \\cocycle condition" g g = g on U \ U \ U : Note that g g = g) g = I on U; and hence the cocycle condition implies that g g = g = I on U \ U : Let Ee denote the set of all triples (;p;v) 2 A M R m such that p 2 U. Dene an equivalence relation on Ee by (;p;v) (;q;w), p = q 2 U \ U; v = g (p)w: Denote the equivalence class of (;p;v) by \[;p;v\] and the set of equivalence classes by E. Dene a projection map : E ! M by (\[;p;v\]) = p: Let Ue = 1

(U) and dene a bijection : Ue! U R
m by (\[;p;v\]) = (p;v):

* * *

1.2. WHAT IS A VECTOR BUNDLE? 5 There is a unique manifold structure on E which makes each into a dieomorphism. With respect to this manifold structure, the projection is a smooth submersion. A real vector bundle of rank m over M is a pair (E;) constructed as above for some choice of open cover fU : 2 Ag of M and some collection g of transition functions which satisfy the cocycle condition. The ber of this vector bundle over p 2 M is Ep=
1

(p), the preimage of p under
the projection. It has the structure of an m-dimensional real vector space. When are two such vector bundles to be regarded as isomorphic? To answer this question, we need the notion of morphism within the category of vector bundles over M. A vector bundle morphism from (E1;1) to (E2;2) over M is a smooth map f : E1! E2 which takes the ber (E1)p of E1 over p to theber (E2)pof E2 over p and restricts to a linear mapon bers, fp: (E1)p! (E2)p. An invertible vector bundle morphism is called a vector bundle isomorphismover M. Let Vect R m(M) denote the space of isomorphism classes of real vector bundles of rank m over M. The reader has no doubt encountered many examples of vector bundles in courses on dierential geometry: the tangent bundle TM, the cotangent bundle T M, the k-th exterior power k T M of the cotangent bundle, and other tensor bundles. Given two vector bundles E1 and E2 over M, one can form their direct sum E1 E2, their tensor product E1 E2, the bundle Hom(E1;E2), and so forth. One can also construct the dual bundle E1 whose bers are the dual spaces to the bers of E1. The construction of such vector bundles is described in detail in x3 of \[29\]. Complex vector bundles are dened in a similar way. The only dierence is that in the complex case the transition functions take their values in the group GL(m; C) of m m complex matrices instead of GL(m; R), and Ee is replaced by the set of triples (;p;v) 2 A M C m such that p 2 U. The construction described above then gives a pair (E;) in which the ber 1

(p) has the structure of a complex vector space of dimension m.
Let Vect C m(M) denote the space of isomorphism classes of complex vector bundles of rank m over M. A complex vector bundle of rank one is also called a complex line bundle. The space of complex line bundles forms an abelian group under the tensor product operation. We will sometimes write

L m = L L L (m times):

Note that if g : U \ U! GL(1; C)

are the transition functions for L, then the transition functions for L m are simply g m .

* * *

## 6 CHAPTER 1. PRELIMINARIES

In addition to real and complex vector bundles, one can dene quater- nionic vector bundles, vector bundles over the quaternions. Quaternions were rst described by William R. Hamilton in 1853. In modern notation, a quaternion is simply a 2 2 matrix of the form

Q = a1 + bi + cj + dk;

where a, b, c and d are real numbers, and

1 0 0 1 0 i i 0 1 =; i =; j =; k = : 0 1 1 0 i 0 0 i

It is readily checked that the sum of two quaternions or the product of two quarternions is again a quaternion. Quaternion multiplication is bilinear over the reals; thus it is determined by the multiplication table for its basis f1; i; j; kg:

## 1 i j k

1 1 i j k i i 1 k j j j k 1 i k k j i 1

Thus of two possible conventions, we choose the one which induces the negative of the cross product on the three-plane of \\imaginary quaternions" spanned by i, j and k. Alternatively, we can think of quaternions as 2 2 complex matrices of the form w z ; z w

where z and w are complex numbers. Note that since

det Q = jzj2 + jwj2;

a nonzero quaternion Q possesses a multiplicative inverse. We let H denote the space of quaternions. It is a skew eld, satisfying all the axioms of a eld except for commutativity of multiplication. Let GL(m; H) denote the group of nonsingular m m matrices with quaternion entries. To dene a quaternionic vector bundle of rank m, one simply requires that the transition functions g take their values in GL(m; H), and we let

* * *

1.2. WHAT IS A VECTOR BUNDLE? 7 Vect H m(M) denote the space of isomorphism classes of quaternionic vector bundles of rank m over M. Note that GL(m; H) is a subgroup of GL(2m; C), which in turn is a sub- group of GL(4m; R). A quaternionic vector bundle of rank m can thought of as a real vector bundle of rank 4m whose transition functions g take their values in GL(m; H) GL(4m; R). More generally, if G is any Lie subgroup of GL(m; R), a G-vector bundle is a rank m vector bundle whose transition functions take their values in G. Let us suppose, for example, that G is the orthogonal group O(m) GL(m; R). In this case the transition functions of a G-vector bundle pre- serve the usual dot product on R
m . Thus the bundle E inherits a ber metric, a smooth function which assigns to each p 2 M an inner product

## h ; ip: EpEp! R:

If G is the special orthogonal group SO(n), a G-vector bundle possesses not only a ber metric, but also an orientation. Similarly, if G is the unitary group U (m) GL(m; C) GL(2m; R), a G-vector bundle is a complex vector bundle of rank m together with a Hermitian metric, a smooth function which assigns to each p 2 M a map

## h ; ip: EpEp! C

## which satises the axioms

1. hv;wipis complex linear in v and conjugate linear in w,
2. hv;wip= hw;vip
3. hv;vip0, with equality holding only if v = 0.
   For example, C n is an inner product space with the inner product given by \*0 1 0 1+ 0 1 z1 w1 z1 @ A; @ A = ( w1 w

n) @ A;
z nwnzn

where we have changed the order in the matrix product so as to agree with the standard conventions of matrix algebra. A section of a vector bundle (E;) is a smooth map

: M ! E such that = identity:

If 2 (E), the restriction of to U can be written in the form (m R

(p) = \[;p; (p)\]; where : U! C
m

H m is a smooth map. The vector-valued functions $\\sigma\_{\\alpha}$ are called the local representatives of $\\sigma$ and they are related to each other by the formula

$$\\sigma\_{\\alpha} = g\_{\\alpha \\beta} \\sigma\_{\\beta} \\quad \\text{on} \\quad U\_{\\alpha} \\cap U\_{\\beta}. \\tag{1.2}$$

In the real or complex case, the set $\\Gamma(E)$ of sections of $E$ is a real or complex vector space respectively, and also a module over the space of smooth functions on $M$. In the quaternionic case, we need to be careful since quaternionic multiplication is not commutative. In this case, (1.2) shows that sections of $E$ can be multiplied on the right by quaternions.

Example. We consider complex line bundles over the Riemann sphere $S^2$, regarded as the one-point compactification of the complex numbers, $S^2 = \\mathbb{C}\\cup{\\infty}$. Give $\\mathbb{C}$ the standard complex coordinate $z$ and let $U\_0 = S^2 - {\\infty}$, $U\_\\infty = S^2 - {0}$. For each integer $n$, define

$$g\_{\\infty 0}: U\_\\infty \\cap U\_0 \\rightarrow GL(1,\\mathbb{C}) \\quad \\text{by} \\quad g\_{\\infty 0}(z) = \\frac{1}{z^n}.$$

This choice of transition function defines a complex line bundle over $S^2$ which we denote by $H^n$. A section of $H^n$ is represented by maps

$$\\sigma\_0: U\_0 \\rightarrow \\mathbb{C}, \\quad \\sigma\_\\infty: U\_\\infty \\rightarrow \\mathbb{C}$$

such that

$$\\sigma\_\\infty = \\frac{1}{z^n} \\sigma\_0, \\quad \\text{on} \\quad U\_\\infty \\cap U\_0.$$

It can be proven that any complex line bundle over $S^2$ is isomorphic to $H^n$ for some $n \\in Z$.

In particular, the cotangent bundle to $S^2$ must be isomorphic to $H^n$ for some choice of $n$. A section $\\sigma$ of the cotangent bundle restricts to $\\sigma\_0 dz$ on $U\_0$ for some choice of complex valued function $\\sigma\_0$. Over $U\_\\infty$, we can use the coordinate $w = 1/z$, and write $\\sigma = -\\sigma\_\\infty dw$. Since $dw = -(1/z)^2dz,$

$$\\sigma\_0 dz = -\\sigma\_\\infty dw \\Rightarrow \\sigma\_\\infty = z^2 \\sigma\_0,$$

and hence $n = -2$. In other words, $T^\*S^2 = H^{-2}$. Similarly, $TS^2 = H^2$.

In a similar way, we can construct all quaternionic line bundles over $S^4$. In this case, we regard $S^4$ as the one-point compactification of the space of quaternions, $S^4 = \\mathbb{H} \\cup{\\infty}$. Let $U\_0 = \\mathbb{H}, U\_\\infty = S^4 - {0}$, and define

$$g\_{\\infty 0}: U\_\\infty \\cap U\_0 \\rightarrow GL(1,\\mathbb{H}) \\quad \\text{by} \\quad g\_{\\infty 0}(Q) = \\frac{1}{Q^n}.$$

As $n$ ranges over the integers, we obtain all quaternionic line bundles over $S^4$.

* * *

1.3. WHAT IS A CONNECTION?

How can we prove the claims made in the preceding paragraphs? Proofs can be based upon theorems from differential topology which classify vector bundles over manifolds. Here are two of the key results:

Classification Theorem for Complex Line Bundles. If M is a smooth manifold, there is a bijection

$$\\text{Vect}\_1^C(M) \\cong H^2(M; \\mathbb{Z}).$$

This theorem will be proven in §1.6. The theorem implies that

$$\\text{Vect}\_1^C(S^2) \\cong H^2(S^2; \\mathbb{Z}) \\cong \\mathbb{Z},$$

and we will see that $H^m$ corresponds to $m \\in \\mathbb{Z}$ under the isomorphism. A argument similar to that for complex line bundles could be used to prove:

Classification Theorem for Quaternionic Line Bundles. If M is a smooth manifold of dimension $\\leq 4$, there is a bijection

$$\\text{Vect}\_1^{M}(M) \\cong H^4(M; \\mathbb{Z}).$$

1.3 What is a connection?

In contrast to differential topology, differential geometry is concerned with "geometric structures" on manifolds and vector bundles. One such structure is a connection. Evidence of the importance of connections is provided by the numerous definitions of connection which have been proposed.

A definition frequently used by differential geometers goes like this. Let

$$\\chi(M) = {\\text{vector fields on } M}, \\quad \\Gamma(E) = {\\text{smooth sections of } E}.$$

Definition 1. A connection on a vector bundle $E$ is a map

$$\\nabla^A : \\chi(M) \\times \\Gamma(E) \\rightarrow \\Gamma(E)$$

which satisfies the following axioms (where $\\nabla\_A^A\\sigma = \\nabla^A(X, \\sigma)$):

$$\\nabla\_A^A(f\\sigma + \\tau) = (Xf)\\sigma + f\\nabla\_A^A\\sigma + \\nabla\_A^A\\tau,$$

(1.3)

$$\\nabla\_{fX+Y}^A\\sigma = f\\nabla\_A^A\\sigma + \\nabla\_A^A\\sigma.$$

(1.4)

Here $f$ is a real-valued function if $E$ is a real vector bundle, a complex-valued function if $E$ is a complex vector bundle.

* * *

10 CHAPTER 1. PRELIMINARIES

It is customary to regard $ \\nabla\_{X}^{A} \\sigma $ as the covariant derivative of $ \\sigma $ in the direction of $ X $.

Given a connection $ \\nabla^{A} $ in the sense of Definition 1, we can define a map

$$d\_{A}: \\Gamma(E) \\rightarrow \\Gamma(T^{\*} M \\otimes E)=\\Gamma(\\mathrm{Hom}(TM,E))$$

by

$$d\_{A}(\\sigma)(X)=\\nabla\_{X}^{A} \\sigma.$$

Then $ d\_{A} $ satisfies a second definition:

**Definition 2. A connection on a vector bundle $ E $ is a map**

$$d\_{A}: \\Gamma(E) \\rightarrow \\Gamma(T^{\*} M \\otimes E)$$

which satisfies the following axiom:

$$d\_{A}(f \\sigma+\\tau)=(df)\\otimes \\sigma+f d\_{A}\\sigma+d\_{A} \\tau.$$ (1.5)

Definition 2 is more frequently used in gauge theory, but in our presentation both definitions will be important. Note that Definition 2 is a little more economical in that one need only remember one axiom instead of two. Moreover, Definition 2 makes clear the analogy between a connection and the exterior derivative.

The simplest example of a connection occurs on the bundle $ E=M\\times \\mathbb{R}^{m} $ , the trivial real vector bundle of rank $ m $ over $ M $ . A section of this bundle can be identified with a vector-valued map

$$\\sigma=\\left( \\begin{array}{c} \\sigma^{1} \ \\sigma^{2} \ \\sigma^{m} \\end{array} \\right): M \\rightarrow \\mathbb{R}^{m}.$$

We can use the exterior derivative to define the "trivial" flat connection $ d\_{A} $ on $ E $ :

$$d\_{A}\\left( \\begin{array}{c} \\sigma^{1} \ \\cdot \ \\sigma^{m} \\end{array} \\right)=\\left( \\begin{array}{c} d \\sigma^{1} \ \\cdot \ d \\sigma^{m} \\end{array} \\right).$$

More generally, given an $ m \\times m $ matrix

$$\\omega=\\left( \\begin{array}{c c c} \\omega\_{1}^{1} & \\cdot & \\omega\_{m}^{1} \ \\cdot & \\ddots & \\cdot \ \\omega\_{1}^{m} & \\cdot & \\omega\_{m}^{m} \\end{array} \\right).$$

* * *

1.3. WHAT IS A CONNECTION?

of real-valued one-forms, we can define a connection $d\_A$ by

$$d\_A \\begin{pmatrix} \\sigma^1 \ . \ \\sigma^m \\end{pmatrix} = \\begin{pmatrix} d\\sigma^1 \ . \ d\\sigma^m \\end{pmatrix} + \\begin{pmatrix} \\omega\_1^1 & . & \\omega\_1^m \ . & \\cdots & . \ \\omega\_m^m & . & \\omega\_m^m \\end{pmatrix} \\begin{pmatrix} \\sigma^1 \ . \ \\sigma^m \\end{pmatrix}. \\tag{1.6}$$

We can write this last equation in a more abbreviated fashion:

$$d\_A \\sigma = d\\sigma + \\omega\\sigma,$$

matrix multiplication being understood in the last term. Indeed, the axiom (1.5) can be verified directly, using the familiar properties of the exterior derivative:

$$d\_A(f\\sigma + \\tau) = d(f\\sigma + \\tau) + \\omega(f\\sigma + \\tau)$$

$$= df \\otimes \\sigma + fd\\tau + f\\omega\\sigma + d\\tau + \\omega\\tau = (df) \\otimes \\sigma + fd\_A\\sigma + d\_A\\tau.$$

We can construct a connection in the trivial complex vector bundle $E = M \\times C^m$ or the trivial quaternionic bundle $M \\times \\mathbb{H}^m$ in exactly the same way, by choosing $\\omega$ to be an $m \\times m$ matrix of complex- or quaternionic-valued one-forms.

Any connection $d\_A$ on a trivial bundle is of the form (1.6). To see this, we apply $d\_A$ to the constant sections

$$e\_1 = \\begin{pmatrix} 1 \ 0 \ 0 \\end{pmatrix}, \\quad e\_2 = \\begin{pmatrix} 0 \ 1 \ 0 \\end{pmatrix}, \\quad \\ldots \\quad e\_m = \\begin{pmatrix} 0 \ 0 \ 1 \\end{pmatrix}.$$

obtaining

$$d\_A e\_j = \\begin{pmatrix} \\omega\_j^1 \ \\omega\_j^2 \ \\omega\_j^m \\end{pmatrix} = \\sum\_{i=1}^{m} e\_i \\omega\_j^i.$$

It then follows directly from the axiom for connections that

$$d\_A \\left( \\sum\_{i=1}^{m} e\_i \\sigma^i \\right) = \\sum\_{i=1}^{m} e\_i d\\sigma^i + \\sum\_{i,j=1}^{m} e\_i \\omega\_j^j \\sigma^j,$$

which is just another way of writing (1.6).

Any vector bundle is "locally trivial." Suppose, for example, that $E$ is a real vector of rank $m$ over $M$ defined by the open covering ${U\_\\alpha : \\alpha \\in A}$ and the transition functions $g\_{\\alpha,b}$. In the notation of the preceding section

$$\\psi\_\\alpha : \\pi^{-1}(U\_\\alpha) \\to U\_\\alpha \\times \\mathbb{R}^m$$

* * *

## 12 CHAPTER 1. PRELIMINARIES

is a vector bundle isomorphism from the restriction of E to U onto the trivial bundle over U. A section 2 (E) possesses a local representative , which is an m-tuple of ordinary functions on U. If dAis a connection on E, then dApossesses a local representative (dA), which is an m-tuple of ordinary one-forms on U. Just as in the preceding paragraph, we can write (dA) = d + !; (1.7)

where ! is an m m matrix of one-forms on U. This matrix ! is called the local representative of the connection dA. To see how the local representatives corresponding to two elements of our distinguished covering are related, we note that since the connection is well-dened on overlaps, we must have

d + ! = g (d + !) on U \ U :

Since = g 1 ,

d + ! = g \[d(g 1 ) + ! g 1 \]

= d + g \[dg 1 + g! g 1 \] :

Thus we conclude that

! = g dg 1 + g! g 1 on U \ U : (1.8)

## This yields

Denition 3. A connection on a real vector bundle E dened by a covering fU : 2 Ag and transition functions fg : ; 2 Ag is a collection of dierential operators fd + ! : 2 Ag;

where d is the exterior derivative on R m -valued functions, and ! is an m m matrix of one-forms on U, which transform according to (1.8).

There is, of course, a similar denition for connections in complex or quater- nionic vector bundles. If E is an O(m)-bundle, an orthogonal connection in E is a connection whose local representatives d+! have the property that ! takes its values in O(m), where O(m) is the space of m m skew-symmetric matrices, the Lie algebra of the orthogonal group O(n). Note that this condition is preserved under the transformation (1.8) because

g 2 O(m);! 2O(m)) g dg 1 ; g! g 1 2O(m):

* * *

1.3. WHAT IS A CONNECTION? 13 Similarly, if E is a U (m)-bundle, a unitary connection in E is a connection such that ! takes its values in U (m), where U (m) is the space of m m skew-Hermitian matrices, the Lie algebra of the unitary group U (m). The general rule is that if E is a G-bundle, a G-connection is a connection whose local representatives ! take values in the Lie algebra of G. Here are some examples of connections: Example 1. Suppose that E = TM, the tangent bundle of a smooth manifold M which is embedded in R
N . The trivial bundle M R N is then a direct sum, M R N = TM NM;

where NM is the normal bundle of M in R N , whose ber at p 2 M is the set of all vectors in R N perpendicular to M. On the trivial bundle M R N , we can take the trivial at connection dened by the vector-valued exterior derivative d. If 2 (E) (M R N ), then d 2 (T M (M R N )). We dene a connection

## dA: (TM) ! (T M TM)

by setting dA() = (d) > ;

where ( ) > denotes projection into the tangent space. It is an enlightening exercise to check that this is just the Levi-Civita connection studied in Riemannian geometry.

## Example 2. Over the Grassmann manifold

Gm(C N ) = f m-dimensional subspaces of C N g

the trivial bundle divides into a direct sum,

Gm(C N ) C N = E E ? ;

where E = f(V;v) 2 Gm(C N ) C N : v 2 V g;

E ? = f(V;v) 2 Gm(C N ) C N : v?V g:

As in the preceding example, we can use the trivial at connection d on the trivial bundle Gm(C N ) C N to dene a connection dAon E by setting

dA() = (d) > ;

where ( ) > denotes the orthogonal projection into E. This connection is called the universal connection in the universal bundle E.

* * *

## 14 CHAPTER 1. PRELIMINARIES

Example 3: the pullback connection. If (E;) is a vector bundle over M dened by the open covering fU : 2 Ag and the transition functions fg : ; 2 Ag, and F : N ! M is a smooth map, the pullback bundle (F E; ) is the vector bundle over N dened by the open covering fF 1

(U) : 2 Ag and the transition functions fg F : ; 2 Ag. An
alternate description is often useful:

F E = f(p;v) 2 N E : F (p) = (v)g; ((p;v)) = p:

If 2 (E) has local representatives, we can dene F 2 (F E) to be the section with local representatives F. Equivalently, in terms of the alternate description,

F : N ! F E by F (p) = (p; F (p)):

More generally, if ! is a dierential form with values in E, we can dene its pullback by F (!) = F! F :

Proposition 1. If dAis a connection on the vector bundle (E;) over M and F : N ! M is a smooth map, there is a unique connection dF Aon the pullback bundle (F E; ) which makes the following diagram commute:

(E)! (T M E) # #

## (F E)! (T N F E)

In this diagram, the horizontal arrows are given by the connections and the vertical arrows are the pullback maps F.

Proof: The commutative diagram implies that if ! is the local represen- tative of dAcorresponding to U, then the local representative of dF A corresponding to F 1

(U) is F!. This establishes uniqueness. For existence, simply dene the local representatives of dF Ato be F! and check that they satisfy the correct transformation formulae.

An important application of the pullback construction is to the existence of parallel transport along curves. If (E;) is a smooth real vector bundle ov rank m over M and : \[a;b\] ! M is a smooth curve, we can form the pullback bundle ( E; ) over the interval \[a;b\]. It is an easy exercise to show that any vector bundle over an interval \[a;b\] is trivial, so we can

* * *

1.3. WHAT IS A CONNECTION? 15 consider E to be the trivial bundle \[a;b\] R
m . The pullback connection can be written as dA= d + !

where ! is a matrix of one-forms on \[a;b\]. If t is the standard coordinate on \[a;b\], 0 1 f11dt fm 1 dt ! = @ A; f 1mdt fm m dt

where fji: \[a;b\] ! R. We now consider the equation

dA= d + ! = 0;

which can be written in terms of components as

i Xm di j + fj= 0; (1.9) dt j=1

a linear system of ordinary dierential equations. It follows from the theory of dierential equations that given an element02 ( E)a, there is a unique solution to (1.9) which satises the initial condition (a) =0. Thus we can dene an isomorphism

## : ( E)a! ( E)b

by setting (0) = (b), where is the unique solution to (1.9) which satises (a) =0. But

( E)a = E(a)and ( E)b = E(b):

## Thus denes an isomorphism

## : E(a)! E(b)

which we call parallel transport along. It is not dicult to show that in the case of an O(m)-bundle with orthogonal connection, or a U (m)-bundle with unitary connection, parallel transport is an isometry. Parallel transport has the following simple application:

Proposition 2. If F0;F1 : N! M are smoothly homotopic maps and E is a vector bundle over M, then F0 E and F1 E are isomorphic vector bundles over N.

* * *

## 16 CHAPTER 1. PRELIMINARIES

Sketch of proof: Let J0;J1 : N ! N \[0; 1\] be the smooth maps dened by

J0(p) = (p; 0); J1(p) = (p; 1):

If F0 is smoothly homotopic to F1, there exists a smooth map H : N \[0; 1\] ! M such that

H J0 = F0; H J1 = F1:

Thus it suces to show that if E is a vector bundle over N \[0; 1\], then J0 E is isomorphic to J1 E. Give E a connection and letp: E(p;0)! E(p;1)denote parallel trans- port along the curve t 7! (p;t). We can then dene a vector bundle isomor- phism : J0 E ! J1 E by

(p;v) = (p;p(v)); for v 2 E(p;0)= J0Ep:

Corollary. Every vector bundle over a contractible manifold is trivial.

Proof: If M is a contractible manifold, the identity map on M is homotopic to the constant map, and hence any vector bundle over M is isomorphic to the pullback of a bundle over a point via the constant map.

# 1.4 The curvature of a connection

Let’s review some familiar facts regarding the exterior derivative. Let

p

(M) = ( p
(T M)) = fdierential p-forms on M g;

so that 0

(M) is just the space of smooth real-valued functions on M. The
exterior derivative d : 0

(M) ! 1
(M) is just the usual dierential of a
function n X @f df = dierential of f = i dx i : i=1 @x

We extend this operator to p

(M) for all p by requiring that d(dx
i

) = 0
and that the Leibniz rule hold:

d(! ^) = d! ^ + ( 1) p ! ^ d; for ! 2 p

(M):
Equality of mixed partial derivatives implies that d d = 0. Thus we obtain a cochain complex

! p 1

(M) ! p
(M) ! p+1
(M) !;

* * *

1.4. THE CURVATURE OF A CONNECTION

and we can define the p-th de Rham cohomology group

$$H^p(M; \\mathbb{R}) = \\frac{\\text{kernel of } d : \\Omega^p(M) \\rightarrow \\Omega^{p+1}(M)}{\\text{image of } d : \\Omega^{p-1}(M) \\rightarrow \\Omega^p(M)}.$$

It is well-known that these groups are isomorphic to the usual singular cohomology groups with real coefficients, and are therefore topological invariants. (Further discussion of de Rham theory can be found in \[7\].)

Now let $E$ be a vector bundle over $M$ and let

$$\\Omega^p(E) = \\Gamma(N^p(T^\* M) \\otimes E) = {p\\text{-forms on } M\\text{ with values in } E}.$$

A connection on $E$ can be regarded as a linear map from zero-forms with values in $E$, to one-forms with values in $E$,

$$d\_A : \\Omega^p(E) \\rightarrow \\Omega^1(E).$$

As in the case of the usual exterior derivative, we can extend $d\_A$ to all of the $\\Omega^p(E)$'s by requiring Leibniz's rule to hold,

$$d\_A(\\omega \\sigma) = d\\omega + (-1)^p\\omega \\wedge d\_A\\sigma, \\quad \\text{for } \\omega \\in \\Omega^p(M), \\quad \\sigma \\in \\Gamma(E).$$

It is not usually true that $d\_A \\circ d\_A = 0$. However,

$$d\_A \\circ d\_A(f\\sigma + \\tau) = d\_A\[df \\otimes \\sigma + fd\_A\\sigma + d\_A\\tau\]$$

$$= d(df)\\sigma - df \\otimes d\_A\\sigma + df \\otimes d\_A\\sigma + f(d\_A \\circ d\_A)\\sigma + d\_A \\circ d\_A\\tau$$

$$= f(d\_A \\circ d\_A)\\sigma + d\_A \\circ d\_A\\tau,$$

so $d\_A \\circ d\_A$ is linear over functions. This implies that $d\_A \\circ d\_A$ is actually a tensor field, called the curvature of the connection.

In the case of the trivial vector bundle $E = M \\times \\mathbb{R}^m$, we can apply $d\_A \\circ d\_A$ to the standard constant sections

$$e\_1 = \\begin{pmatrix} 1 \ 0 \ . \ 0 \\end{pmatrix}, \\quad e\_2 = \\begin{pmatrix} 0 \ 1 \ . \ 0 \\end{pmatrix}, \\quad \\ldots, \\quad e\_m = \\begin{pmatrix} 0 \ 0 \ . \ 1 \\end{pmatrix}.$$

Then

$$d\_A \\circ d\_A(e\_i) = \\begin{pmatrix} \\Omega\_1^i \ \\Omega\_2^i \ . \ \\Omega\_m^i \\end{pmatrix} = \\sum\_{j=1}^{m} e\_j \\Omega\_i^j,$$ where each $\\Omega\_i^j$ is a two-form. Linearity over functions implies that

$$d\_A \\circ d\_A \\left( \\sum\_{i=1}^{m} e\_i \\sigma^i \\right) = \\sum\_{i,j=1}^{m} e\_i \\Omega\_j^j \\sigma^j,$$

or in matrix notation

$$d\_A \\circ d\_A(\\sigma) = \\Omega\\sigma,$$

(1.10)

where $\\Omega$ is a matrix of two-forms.

Suppose now that $E$ is a real vector bundle of rank $m$ over $M$ defined by the open covering ${U\_\\alpha : \\alpha \\in A}$ and the transition functions $g\_{\\alpha\\beta}$. Any element $\\sigma \\in \\Gamma(E)$ possesses local representatives $\\sigma\_\\alpha$, and in accordance with (1.10),

$$d\_A \\circ d\_A(\\sigma\_\\alpha) = \\Omega\_\\alpha \\sigma\_\\alpha,$$

where $\\Omega\_\\alpha$ is a matrix of two-forms. Applying the differential operator $d\_A = d + \\omega\_\\alpha$ to (1.7) yields

$$d\_A \\circ d\_A(\\sigma\_\\alpha) = (d + \\omega\_\\alpha)(d\\sigma\_\\alpha + \\omega\_\\alpha \\sigma\_\\alpha)$$

$$= d(d\\sigma\_\\alpha) + (d\\omega\_\\alpha)\\sigma\_\\alpha - \\omega\_\\alpha \\wedge d\\sigma\_\\alpha + \\omega\_\\alpha \\wedge d\\sigma\_\\alpha + (\\omega\_\\alpha \\wedge \\omega\_\\alpha)\\sigma\_\\alpha$$

$$= (d\\omega\_\\alpha + \\omega\_\\alpha \\wedge \\omega\_\\alpha)\\sigma\_\\alpha,$$

and hence

$$\\Omega\_\\alpha = d\\omega\_\\alpha + \\omega\_\\alpha \\wedge \\omega\_\\alpha.$$

(1.11)

Since $d\_A \\circ d\_A$ is independent of trivialization, the matrices of two-forms must satisfy

$$\\Omega\_\\alpha \\sigma\_\\alpha = g\_{\\alpha\\beta}\\Omega\_\\beta \\sigma\_\\beta = g\_{\\alpha\\beta}\\Omega\_\\beta g\_{\\alpha\\beta}^{-1}\\sigma\_\\alpha \\quad \\text{on } U\_\\alpha \\cap U\_\\beta.$$

Thus the $\\Omega\_\\alpha$'s transform by the rule

$$\\Omega\_\\alpha = g\_{\\alpha\\beta}\\Omega\_\\beta g\_{\\alpha\\beta}^{-1},$$

(1.12)

the way in which local representatives of a two-form with values in the vector bundle End($E$) should transform. In other words, the $\\Omega\_\\alpha$'s determine an End($E$)-valued two-form, called the _curvature_ of the connection $d\_A$, and sometimes denoted simply by $\\Omega$ or $\\Omega\_A$.

Differentiation of equation (1.11) yields the _Bianchi identity_:

$$d\\Omega\_\\alpha = \\Omega\_\\alpha \\wedge \\omega\_\\alpha - \\omega\_\\alpha \\wedge \\Omega\_\\alpha = \[\\Omega\_\\alpha, \\omega\_\\alpha\].$$

(1.13)

Of course, all of the above discussion applies to connections in complex vector bundles or quaternionic vector bundles as well as real vector bundles.

* * *

1.5. CHARACTERISTIC CLASSES 19 In the complex case, for example, the matrices have complex-valued two-forms as entries. In the case of an orthogonal connection in an O(m)-bundle, it follows directly from (1.11) that the matrices are skew-symmetric. In the case of a unitary connection in a U (m)-bundle, these matrices are skew-Hermitian. The case of complex line bundles is particularly important. In this case, the matrices are all 1 1, and the transformation formula (1.12) implies that = on overlaps. Thus the ’s t together to make a globally dened two-formAon M, which is purely imaginary in thecase of a unitary connection. Since the Lie group U (1) is isomorphic to SO(2), a complex line bundle with Hermitian metric can also be regarded as a real vector bundle of rank two together with a ber metric and orientation. Indeed, given an oriented rank two real vector bundle E with ber metric, we can dene multiplication by i to be rotation through 90 degrees in the direction determined by the orientation. If e1 is a locally dened unit-length section of E, we can set e2 = ie1, thereby obtaining a locally dened moving frame (e1;e2). Note that if !12is the corresponding real valued connection form,
de1 = e2!12= ( i!12)e1;

and i!12is the purely imaginary connection form for the unitary bundle. We set FA=12= d!12;

a globally dened curvature two-form on M. ThenA= iFA= i12= id!12is the corresponding purely imaginary two-form when E is regarded as a unitary bundle. The Bianchi identity in this case is simply

## dFA= 0: (1.14)

All of this applies to the case where E = T, the tangent bundle of an oriented two-dimensional Riemannian manifold . In this case, the Levi- Civita connection on T is a unitary connection and its curvature form is FA= KdA;

where K is the Gaussian curvature of and dA is the area two-form of .

# 1.5 Characteristic classes

In general, the curvature matrix is only locally dened. However, it is possible to construct certain polynomials in which are invariant under

* * *

## 20 CHAPTER 1. PRELIMINARIES

the transformation (1.12) and these give rise to geometric and topological invariants. Let us focus rst on the case of a U (m)-vector bundle E, a complex vector bundle of rank m with Hermitian metric. We give E a unitary connection which has local representatives d + ! and curvature matrices . As we saw in the preceding section, is skew-Hermitian, so

k i i ; 2 2

are Hermitian. Hence for each choice of positive integer k, the dierential form " # k i Trace 2

is real-valued. Since trace is invariant under similarity, it follows from (1.12) that " # " # " # k k k i i1i Trace = Trace g g = Trace 2 2 2

on U \ U. Hence these locally dened forms t together into a globally dened real-valued 2k-formk(A). We say thatk(A) is a characteristic form.

Lemma. Each dierential formk(A) is closed, dk(A) = 0.

Proof: It follows from the Bianchi identity that

k k ikik dk(A) = d\[Trace()\] = Trace\[d()\] 2 2

k ik 1 k 1 = Trace\[(d) + + (d)\] 2 k ik 1 k 1 = Tracef\[;!\] + + \[;!\]g = 0; 2

the last equality coming from the fact that Trace(A1 Ak) is invariant under cyclic permutation of A1, . . . , Ak.

This Lemma implies thatk(A) represents a de Rham cohomology class

\[k(A)\] 2 H 2k (M; R):

* * *

1.5. CHARACTERISTIC CLASSES 21 Proposition 1. If E is a U (m)-bundle over M with unitary connection dAand F : N ! M is a smooth map, then the characteristic forms of the pullback connection dF Aon the pullback bundle F E are pullbacks of the characteristic forms of dA:
k (F A) = Fk(A):

Proof: The local representative of dF Aon F 1

(U) is ! = F!, and
the curvature of dF Ais

= d! + ! ^ ! = F d! + F! ^ F! = F :

Thus Trace(() k ) = Trace(F ( k )) = F Trace( k );

or equivalently, k (F A) = Fk(A):

Proposition 2. The de Rham cohomology class \[k(A)\] is independent of the choice of unitary connection dAas well as the choice of Hermitian metric on E.

Proof: We use the cylinder construction from topology. From the bundle (E;) over M we construct the cylinder bundle (E \[0; 1\]; id) over M \[0; 1\]. Note that if E possesses the trivializing covering fU : 2 Ag, then E \[0; 1\] possesses the trivializing covering fU \[0; 1\] : 2 Ag. We can pull two connections dAand dBon E back to M \[0; 1\] via the projection on the rst factor1: M \[0; 1\] ! M. If dAand dBare given over U by d + !; d +;

then the pullback connections are given over U \[0; 1\] by

## d +1!; d +1:

We dene a new connection dCon E \[0; 1\], given over U \[0; 1\] by

d + (1 t)1! + t1 :

If J0;J1 : M ! M \[0; 1\] are the maps dened by J0(p) = (p; 0), J1(p) = (p; 1), then dA= dJ 0 C; dB= dJ1C: Hence by Proposition 1,

\[k(A)\] = J0\[k(C)\] = J1\[k(C)\] = \[k(B)\] 2 H 2k (M; R):

* * *

## 22 CHAPTER 1. PRELIMINARIES

This shows that \[k(A)\] is independent of the choice of unitary connection. The proof that it is independent of the choice of Hermitian metric is similar and is left to the reader. Use the fact that any two Hermitian metrics h; i0 and h; i1 can be connected by aone-parameter family

(1 t)h ; i0 + th ; i1:

According to Proposition 2, to each complex vector bundle E over M we can associate a collection of cohomology classes

k

(E) = \[k(A)\]:
These are called characteristic classes of E. Clearly, if two complex vector bundles are isomorphic over M, they must have the same characteristic classes. Characteristic classes are natural under mappings as the following proposition shows: Proposition 3. If F : N ! M is a smooth map and E is a complex vector bundle over M, then k (F E) = Fk(E):

Proof: This is now an immediate consequence of Proposition 1. We can put the characteristic classes together into a power series called the Chern character:

## ch(E) = \[Trace (exp ((i=2)))\]

1 1 = rank(E) +1(E) +2(E) + +k(E) + : 2! k! This is an element of the cohomology ring

H (M; R) = H0(M; R) H1(M; R) H k (M; R) :

Note that the Chern character collapses to a polynomial since all terms of degree > dim(M) must vanish. Proposition 4. The Chern character satises the identities:

ch(E1 E2) = ch(E1) + ch(E2); ch(E1 E2) = ch(E1)ch(E2):

* * *

1.5. CHARACTERISTIC CLASSES

Proof: Suppose that $E\_1$ and $E\_2$ have Hermitian metrics and unitary connections $d\_{A\_1}$ and $d\_{A\_2}$, respectively. Then $E\_1 \\oplus E\_2$ inherits a Hermitian
metric and a unitary connection $d\_{A\_1 \\oplus A\_2}$, defined by

$$d\_{A\_1 \\oplus A\_2}(\\sigma\_1 \\oplus \\sigma\_2) = (d\_{A\_1} \\sigma\_1) \\oplus (d\_{A\_2} \\sigma\_2).$$

It follows that

$$(d\_{A\_1 \\oplus A\_2})^2(\\sigma\_1 \\otimes \\sigma\_2) = (d\_{A\_1}^2 \\sigma\_1) \\oplus (d\_{A\_2}^2 \\sigma\_2),$$

and hence

$((i/2\\pi)\\Omega^{A\_1 \\oplus A\_2})^k = \\left( \\begin{array}{cc} ((i/2\\pi)\\Omega^{A\_1})^k & 0 \ 0 & ((i/2\\pi)\\Omega^{A\_2})^k \\end{array} \\right).$$

Thus

$$\\tau\_k(E\_1 \\oplus E\_2) = \\tau\_k(E\_1) + \\tau\_k(E\_2),$$

which implies the first of the two identities.

Similarly, $E\_1 \\otimes E\_2$ inherits a Hermitian metric and a unitary connection
$d\_{A\_1 \\oplus A\_2}$, defined by the Leibniz rule

$$d\_{A\_1 \\oplus A\_2}(\\sigma\_1 \\otimes \\sigma\_2) = (d\_{A\_1} \\sigma\_1) \\otimes \\sigma\_2 + \\sigma\_1 \\otimes (d\_{A\_2} \\sigma\_2).$$

Since $d\_{A\_1 \\oplus A\_2}$ is a skew-derivation,

$$(d\_{A\_1 \\oplus A\_2})^2(\\sigma\_1 \\otimes \\sigma\_2) = (d\_{A\_1}^2 \\sigma\_1) \\otimes \\sigma\_2 + \\sigma\_1 \\otimes (d\_{A\_2}^2 \\sigma\_2),$$

from which it follows that

$$(d\_{A\_1 \\oplus A\_2})^{2k}(\\sigma\_1 \\otimes \\sigma\_2) = \\sum\_{j=0}^{k} \\binom{k}{j}(d\_{A\_1}^{2j}\\sigma\_1) \\otimes (d\_{A\_2}^{2k-2j}\\sigma\_2),$$

or

$$\\frac{1}{k!}(d\_{A\_1 \\oplus A\_2})^{2k}(\\sigma\_1 \\otimes \\sigma\_2) = \\sum\_{j=0}^{k} \\frac{1}{j!}(d\_{A\_1}^{2j}\\sigma\_1) \\otimes \\frac{1}{(k-j)!}(d\_{A\_2}^{2k-2j}\\sigma\_2).$$

We conclude that

$$\\exp((d\_{A\_1 \\oplus A\_2})^2) = \\exp((d\_{A\_1})^2)\\exp((d\_{A\_2})^2),$$

which yields the second of the two identities.

* * *

## 24 CHAPTER 1. PRELIMINARIES

In the topology of four-manifolds, certain polynomials in thek(E)’s play a key role. If E is a U (m)-vector bundle over M, the rst and second Chern classes of E are dened by the formulae

12 c1(E) =1(E); c2(E) = \[1(E)2(E)\]: (1.15) 2

To motivate the second of these, we can check that if E has rank two, so that (i=2) is a (2 2)-Hermitian matrix, " # 2 2 1 i i i Trace Trace = Determinant; 2 2 2 2

so the second Chern class is also given by the formula

i c2(E) = the de Rham cohomology class of Determinant : 2

Higher Chern classes could also be dened by similar formulae, but they automatically vanish on manifolds of dimension 4. Note that it follows from (1.15) that

(E) = c (E)
2 2c (E): (1.16) 2 1 2 Use of a Hermitian metric shows that the dual E to a U (m)-vector bundle E over M is obtained from E by conjugating transition functions,

## g 7! g :

Thus we can also think of E as the conjugate of E. A connection on E denes a connection on E by conjugating local representatives,

## ! 7! !; 7! :

Since conjugation changes the sign of the trace of a skew-Hermitian matrix, we see that c1(E) = c1(E); similarly, c2(E) = c2(E). We can also dene characteristic classes of quaternionic and real vec- tor bundles. A quaternionic line bundle E can be regarded as a complex vector bundle of rank two. Right multiplication by j is a conjugate-linear isomorphism from E to itself, so the rst Chern class of E must vanish, but second Chern class is an important invariant of E. On the other hand, a real vector bundle E of rank k can be complex- ied, giving a complex vector bundle E C of rank k. Once again, the complexication is isomorphic to its conjugate so its rst Chern class must vanish, but we can dene the rst Pontrjagin class of E to be

## p1(E) = c2(E C):

* * *

1.6 THE THOM FORM 25

1.6 The Thom form

The first Chern class of a complex line bundle over a compact oriented surface possesses an important geometric interpretation as the algebraic number of zeros of a generic section. We now present that interpretation based upon the construction of a Thom form.

Suppose that $L$ is a complex line bundle over $M$, regarded as an oriented real vector bundle of rank two, as described at the end of §1.4. If $U$ is an open subset of $M$ over which we have constructed a moving frame $(e\_1, e\_2)$ with $e\_2 = ie\_1$, we can define smooth functions

$$t\_{1,2} : \\pi^{-1}(U) \\longrightarrow \\mathbb{R}$$ by $t\_i(a\_1e\_1(p) + a\_2e\_2(p)) = a\_i.$$

Moreover, we can pull the connection and curvature forms $\\omega\_{12}$ and $\\Omega\_{12}$ back to $\\pi^{-1}(U)$.

Definition. The Thom form on $L$ is the smooth two-form defined locally by

$$\\Phi = \\frac{1}{2\\pi} e^{-(t\_1^2+t\_2^2)} \[\\Omega\_{12} + 2(dt\_1 + \\omega\_{12}t\_2) \\wedge (dt\_2 - \\omega\_{12}t\_1)\] .$$

(It is not difficult to verify that this expression is independent of choice of moving frame $(e\_1, e\_2)$, and hence $\\Phi$ is indeed a globally defined differential two-form on $L$).

We can also write

$$\\Phi = \\frac{1}{2\\pi} e^{-(t\_1^2+t\_2^2)} \[\\Omega\_{12} + 2dt\_1 \\wedge dt\_2 + \\omega\_{12} \\wedge d(t\_1^2+t\_2^2)\] ,$$

from which it is easy to check that $\\Phi$ is closed. Moreover, it is clearly rapidly decreasing in the fiber direction, and the familiar integral formula

$$\\int\_R e^{-(t\_1^2+t\_2^2)} dt\_1 dt\_2 = \\int\_0^\\infty \\int\_0^{2\\pi} e^{-r^2} rdrd\\theta = \\pi ,$$

shows that the integral of $\\Phi$ over any fiber is one.

We reiterate the three key properties: (i.) The Thom form is closed. (ii.) It is rapidly decreasing in the fiber direction. (iii.) Its integral over any fiber is one. Any other two-form with the same key properties would be equally effective in establishing a geometric interpretation for the first Chern class. For example, we could replace (1.17) with