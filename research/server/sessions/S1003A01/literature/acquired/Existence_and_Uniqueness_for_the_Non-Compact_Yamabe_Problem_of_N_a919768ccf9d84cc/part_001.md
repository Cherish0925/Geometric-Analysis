---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Existence and Uniqueness for the Non-Compact Yamabe Problem of Negative Curvature Type]

# Existence and Uniqueness for the Non-Compact Yamabe Problem of Negative Curvature Type

> Source: https://ora.ox.ac.uk/objects/uuid:6c6923a6-7b99-4581-bdee-97e45e3d8024/files/s9z9031499
> Fetched: 2026-10-05 05:57
> Method: FULLTEXT_HTML_JINA|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA|ORIGINAL_FILES=1

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
  "source": "serper",
  "source_url": "https://ora.ox.ac.uk/objects/uuid:6c6923a6-7b99-4581-bdee-97e45e3d8024/files/s9z9031499",
  "metadata": {
    "provenance_urls": [
      "https://ora.ox.ac.uk/objects/uuid:6c6923a6-7b99-4581-bdee-97e45e3d8024/files/s9z9031499"
    ],
    "search_origins": [
      {
        "source": "serper",
        "query": "asymptotically locally complex hyperbolic Yamabe equation maximum principle uniqueness decay"
      },
      {
        "source": "exa",
        "query": "asymptotically locally complex hyperbolic Yamabe equation maximum principle uniqueness decay"
      },
      {
        "source": "tavily",
        "query": "asymptotically locally complex hyperbolic Yamabe equation maximum principle uniqueness decay"
      },
      {
        "source": "tavily",
        "query": "\"asymptotically complex hyperbolic\" Yamabe equation conformal factor tends to 1 scalar curvature prescribed"
      }
    ]
  },
  "declared_files": [
    {
      "url": "https://ora.ox.ac.uk/objects/uuid:6c6923a6-7b99-4581-bdee-97e45e3d8024/files/s9z9031499",
      "name": "s9z9031499",
      "label": "",
      "role": "primary_object_file",
      "parent_url": "https://ora.ox.ac.uk/objects/uuid:6c6923a6-7b99-4581-bdee-97e45e3d8024/files/s9z9031499",
      "identity_bound": true,
      "primary_label": false,
      "download_eligible": true
    }
  ]
}
```

## Source description

by J Hogg · 2024 · Cited by 4 — We study existence and uniqueness results for the Yamabe problem on non-compact manifolds of negative curvature type. asymptotically locally hyperbolic. decay ...

## Retrieved source content

Title: Hogg_and_Nguyen_2023_Existence_and_uniqueness.pdf

URL Source: https://ora.ox.ac.uk/objects/uuid:6c6923a6-7b99-4581-bdee-97e45e3d8024/files/s9z9031499

Number of Pages: 36

Markdown Content:
# Existence and Uniqueness for the Non-Compact Yamabe Problem of Negative Curvature Type 

## Joseph Hogg and Luc Nguyen ∗

Abstract 

We study existence and uniqueness results for the Yamabe problem on non-compact manifolds of negative curvature type. Our first existence and uniqueness result concerns those such manifolds which are asymptotically locally hyperbolic. In this context, our result requires only a partial C2 decay of the metric, namely the full decay of the metric in C1 and the decay of the scalar curvature. In particular, no decay of the Ricci curvature is assumed. In our second result we establish that a local volume ratio condition, when combined with negativity of the scalar curvature at infinity, is sufficient for existence of a solution. Our volume ratio condition appears tight. This paper is based on the DPhil thesis of the first author. 

# Contents 

1 Introduction 22 The Yamabe problem for ALH manifolds 6

2.1 Definitions and notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 72.2 Existence of a solution for the Yamabe problem . . . . . . . . . . . . . . . . 92.3 Asymptotic properties of the conformal factor . . . . . . . . . . . . . . . . . 12 2.3.1 An upper bound at infinity . . . . . . . . . . . . . . . . . . . . . . . . 12 2.3.2 A lower bound at infinity . . . . . . . . . . . . . . . . . . . . . . . . . 16 2.3.3 First derivative estimates at infinity . . . . . . . . . . . . . . . . . . . 20 2.4 Uniqueness and completion of the proof of Theorem 1.1 . . . . . . . . . . . . 21 2.5 Asymptotically warped product manifolds . . . . . . . . . . . . . . . . . . . 23 

3 Volume ratio conditions for solvability of the Yamabe problem 25 

3.1 An upper bound on the eigenvalue for the conformal Laplacian . . . . . . . . 25 3.2 Sharpness of the eigenvalue estimate . . . . . . . . . . . . . . . . . . . . . . 29 

> ∗

Mathematical Institute and St Edmund Hall, University of Oxford, Andrew Wiles Building, Radcliffe Observatory Quarter, Woodstock Road, Oxford OX2 6GG, UK. Email: luc.nguyen@maths.ox.ac.uk 

11 Introduction 

We are interested in the Yamabe problem on non-compact manifolds: given some complete non-compact Riemannian manifold ( M, g ) of dimension n ≥ 3, does there exist a correspond-ing complete conformal metric whose scalar curvature is constant? Equivalently, we would like to find a complete metric ˜ g = u 4 

> n−2

g where u is some strictly positive smooth function on M solving the Yamabe equation 

S˜g = u− n+2  

> n−2

(−cn∆gu + Sgu) ≡ constant, cn := 4( n − 1) 

n − 2 .

Here, Sg and S˜g refer to the scalar curvatures of the corresponding metrics. The operator 

−cn∆g + Sg is known as the conformal Laplacian. In the case that M is compact, the Yamabe problem has been extensively studied. The existence of a solution was established through the combined works of Yamabe [Yam60], Trudinger [Tru68], Aubin [Aub76] and Schoen [Sch84]. For other aspects of the Yamabe problem, see e.g. [Bre08, BM09, CGS89, CL99, GNN79, GNN81, KMS09, KMPS99, LZ04, LZ05, LZ07, Mar08, XZ22] and references therein. Our work is focused on the Yamabe problem of “negative curvature type” on non-compact manifolds, namely we are interested in obtaining conformal changes to constant negative scalar curvature. Consequently, asserting that S˜g ≡ − n(n−1), the equation for the conformal change in scalar curvature yields the Yamabe equation 

−cn∆gu + Sgu = −n(n − 1) u n+2  

> n−2

. (Ya) Finding a solution to the Yamabe problem thus amounts to finding a positive solution of the equation (Ya) above for which the corresponding conformal metric is complete. The Yamabe problem of negative curvature type on non-compact manifolds has been studied extensively in the literature. Important progress has been made by Andersson, Chru´ sciel and Friedrich [ACF92], Gover and Waldron [GW17], Graham [Gra17] and Loewner and Nirenberg [LN74]. For further literature see e.g. [Avi82, AM85, AM88a, AM88b, CP08, Fin98, Fin99, HS20, HL21, Jia21, Jin88, Lab05, LN74, Maz91, MP96, RRV97, SY88, V´ er81] and references therein. In the present work we consider conditions for existence of a solution to the Yamabe problem on a given non-compact Riemannian manifold ( M, g ) where g has asymptotically negative scalar curvature. We assume throughout the paper that g is complete and satisfies a condition of the type lim sup Sg ≤ − ε < 0 (1.1) for some ε > 0 and where the limit is taken along any divergent sequence in the manifold. It is known that (1.1) is insufficient to conclude that the Yamabe problem can be solved. For example, in [AM88b], alongside a number of existence results, Aviles and McOwen give 2an example of a complete metric g on R×Tn−1 satisfying (1.1) for which the Yamabe problem has no solution. It is therefore of interest to understand what conditions, in addition to (1.1), are necessary and/or sufficient for the Yamabe problem to have a solution. Our first result concerns asymptotically locally hyperbolic (ALH) manifolds, a well-studied class of manifolds satisfying (1.1), in a weaker sense than considered in the existing literature (e.g. [ACF92] and [AILA18]). In particular, our notion of ALH requires only C1

decay in the metric components to those of the model space and a bound on the scalar curvature of the form 

Sg ≤ − n(n − 1) + Ce −αr or (1.2) 

|Sg + n(n − 1) | ≤ Ce −αr (1.3) for α ∈ (0 , n ) and some constant C > 0, without requiring decay of the full curvature tensor. For the precise definition, see Section 2.1. We establish: 

Theorem 1.1. Suppose (M, g ) is an ALH manifold of regularity order 1 and with decay exponent α ∈ (0 , n ). If the scalar curvature satisfies (1.2) on M , then there exists a positive smooth solution u to (Ya) on M satisfying lim inf r→∞ u ≥ 1 corresponding to a complete conformal metric ˜g with S˜g ≡ − n(n − 1) .If the scalar curvature satisfies the stronger condition (1.3) on M , then the solution u

above is the unique solution satisfying lim r→∞ u = 1 , the corresponding conformal manifold 

(M, ˜g) is ALH of regularity order 0 and with decay exponent α, and u is maximal among all solutions to (Ya) , that is any other solution ˜u satisfies ˜u ≤ u.

Some comments on the conclusions of the theorem are in order. Concerning the unique-ness, we are able to slightly relax the condition lim r→∞ u = 1; see Proposition 2.15. However, this necessary condition for uniqueness cannot be dropped in its entirety: 

Example 1.2. Take M = B1 to be the unit ball in Rn, δ to be the Euclidean metric and 

g = 4(1 − | x|2)2 δ and g′ = 4R2

(R2 − | x|2)2 δ

to be the Poincar´ e metrics on B1 and BR for some R > 1. Clearly, on B1, if we write 

g′ = u 4 

> n−2

g then u must solve the Yamabe equation for (M = B1, g ) and lim r(x)→∞ u(x) = 0 .In fact, u(x)en−22 r(x) tends to   4RR2−1

n−22 as r(x) → ∞ .

Regarding the loss in regularity order of the resulting conformal ALH metric, this is ex-pected due to the assumption that the scalar curvature decays only in L∞ in (1.3). Under stronger decay assumptions, one may appeal to elliptic regularity theory to obtain corre-spondingly stronger regularity of the resulting conformal metric at infinity. 3We place our result in the context of the existing literature on the Yamabe problem for asymptotically hyperbolic manifolds. A fundamental and pioneering work of Loewner and Nirenberg [LN74] showed that, on every open subset M of Rn with regular boundary, there exists a complete and conformally flat metric g which is ALH and has constant negative scalar curvature. Of special relevance to Theorem 1.1 is the work of Andersson, Chru´ sciel and Friedrich [ACF92] which proved, roughly speaking and among other things, the existence and uniqueness of a solution to the Yamabe problem when ( M, g ) is ALH and admits a C2

conformal compactification 1. We note that the existence of such a conformal compactification mandates the full decay of all sectional curvatures to a negative constant near infinity. Under weaker regularity assumptions on the conformal compactification, while still maintaining the full curvature decay, a similar result has been obtained in [AILA18]. We remark that in Theorem 1.1, we require instead an assumption on the scalar curvature alone. It is not hard to give examples of metrics which satisfy the conditions of Theorem 1.1 but whose Ricci curvature is not asymptotic to a constant multiple of the metric; see Example 2.3. In our second main result, we give a local condition which, together with (1.1), ensures the existence of a solution to the Yamabe problem. Our result is motivated by a result of Aviles and McOwen in [AM88b] which asserts that the negativity of the first eigenvalue of the conformal Laplacian on some compact domain, in combination with (1.1), implies the existence of a solution to the Yamabe problem. We prove: 

Theorem 1.3. Let (M, g ) be a Riemannian manifold and suppose that there exist two open sets Ω1 ⊂ Ω2 with C1 boundary which satisfy (taking dg to be the geodesic distance with respect to g) that 

dg(x, ∂ Ω2) = R for each x ∈ ∂Ω1 for some R > 0, (1.4) 

V ol g(Ω 2 \ Ω1)

V ol g(Ω 1) ≤ sinh 2

pn(n − 2) 2 R

!

, (1.5) 

and the scalar curvature satisfies Sg ≤ − n(n − 1) on Ω2. Then, the conformal Laplacian 

−cn∆g + Sg for (M, g ) has a negative first eigenvalue on Ω2. Consequently, if g satisfies 

(1.1) , there exists a complete metric ˜g conformal to g on M of constant scalar curvature 

−n(n − 1) .

Our Theorem 1.3 gives a new sufficient condition for existence, relating a local volume growth to the solvability of the Yamabe problem on the whole manifold. The local condition (1.5) is tight in the following sense: 

> 1The related question of when intrinsic definitions of non-compact ALH manifolds imply the existence of a corresponding conformal compactification of a certain regularity is addressed, for example, in [BG11] and [Gic13].

4Remark 1.4. The constant 

√n(n−2) 2 in (1.5) is sharp with respect to the existence of a negative first eigenvalue for the conformal Laplacian. Namely, for any β > pn(n − 2) there exists a manifold (M, g ) and concentric annuli Ω1 ⊂ Ω2 satisfying (1.4) with volume ratio 

V ol g(Ω 2 \ Ω1)

V ol g(Ω 1) ≤ sinh 2

β

2 R



(1.6) 

and with scalar curvature satisfying Sg ≤ − n(n − 1) on Ω2 but for which the first eigenvalue for the conformal Laplacian on Ω2 is positive. See Proposition 3.6 and the comment following it. 

While the relationship between volume comparison and the first eigenvalue for the Lapla-cian −∆g has been well observed in the literature, the relation between volume comparison and the solvability of the Yamabe problem is less understood. Although it is sharp for the existence of a negative first eigenvalue for the conformal Laplacian, we do not know whether our bound in (1.5) is optimal for the solvability of the Yamabe problem. It would be in-teresting to understand what the sharp volume ratio bound of the form (1.5) would be for existence of solutions to the Yamabe problem. Theorem 1.3 is of a different flavour to Theorem 1.1. We first note that, for the ALH manifolds treated in Theorem 1.1, the volume ratio in the asymptotic region behaves differ-ently than (1.5); in particular if we fix Ω 1 in the asymptotic region and consider large R, the volume ratio satisfies 

V ol g(Ω 2 \ Ω1)

V ol g(Ω 1) ≈ e(n−1) R ≫ sinh 2

pn(n − 2) 2 R

!

. (1.7) Furthermore, we have the following remark: 

Remark 1.5. Consider a manifold (M, g ) of the form M = R×N where (N, h ) is a manifold of constant negative scalar curvature and g = dr 2 + e−βr h for some 0 ≤ β < 

√n(n−2)  

> n−1

. By 

(3.15) , a computation gives Sg = −(n−1)( n−2) e2βr +O(1) → −∞ as r → ∞ . Additionally, taking Ω1 = ( r0, r 0 +1) ×N , Ω2 = ( r0 −R, r 0 + 1+ R)×N for some r0 ≫ R ≫ 1 we have that 

(1.5) is satisfied. And lastly, by Proposition 2.17, g is not conformal to a locally hyperbolic metric. Consequently, (M, g ) provides an example which is not covered by Theorem 1.1 and for which we may solve the Yamabe problem on (M, g ).

We briefly discuss the proofs of our results. The proof of the existence part of Theorem 1.1 makes use of the procedures in [ACF92] and [AM88b] where barrier functions play an important role. Due to the weaker asymptotic conditions on the scalar curvature in (1.2), or (1.3), additional work is required to construct such barrier functions. For the unique-ness part, we treat separately the lower and upper bounds at infinity for solutions of (Ya). 5For the upper bound, we adapt certain ideas from [LN74] using certain reference solutions. The main difference is that we lack an explicit closed form of the reference solutions and so the final conclusion is drawn from an asymptotic analysis of these solutions, exploiting the conformal invariance of the equation. For the lower bound, we highlight that our treatment is very different from approaches seen in the literature, where one typically uses the exis-tence of a sufficiently regular conformal compactification in order to compare the solution to some reference solution exterior to the compactified manifold. Owing to our lack of such a compactification, we instead perform a blow-up analysis intrinsically to the given manifold, identifying a limiting equation from which we deduce the desired lower bound at infinity. To prove Theorem 1.3, we make use of a particular test function for the variational func-tional corresponding to the first eigenvalue of the conformal Laplacian. This test function is constructed by minimising the sup-norm of the integrand in the variational functional, following the procedure in [Aro65] and using the volume ratio condition (1.5). It was sur-prising to the authors that condition (1.5) for the volume ratio turned out to be sharp in the sense of Remark 1.4 above. While falling outside the scope of the present paper, it would be interesting to understand what other geometric quantities similar in nature to the volume ratio used here could have relevance to the behaviour of the first eigenvalue of the conformal Laplacian and the solvability of the Yamabe problem. The paper is structured as follows. In Section 2, we address Theorem 1.1 and our work in the context of ALH manifolds. In Section 3, we address Theorem 1.3 and our related study of the volume ratios of multiply warped product manifolds. 

Acknowledgments. 

J.H. was partially supported by the EPSRC Centre for Doctoral Training in Partial Dif-ferential Equations [grant number EP/L015811/1]. The authors would like to thank the anonymous referee for their constructive comments. 

# 2 The Yamabe problem for asymptotically locally hy-perbolic manifolds 

In this section, we prove Theorem 1.1. We first make precise our setting in Section 2.1. Our results are then split into two main sections; Section 2.2 addresses the existence of a solution to the Yamabe problem and Section 2.3 focuses on an understanding of the asymptotic behaviour of the obtained conformal factor. We then summarise how the results of the previous two sections combine to prove Theorem 1.1 in Section 2.4. Finally, in Section 2.5, we provide a discussion of how Theorem 1.1 can be applied to the broader class of asymptotically warped product manifolds, in particular via a result regarding the conformal classes of reference warped product metrics. 62.1 Definitions and notation 

We will consider manifolds which may be decomposed as a union M = M0 ∪ M +, where 

M0 is some compact interior region, M + is a non-compact exterior region and both parts are disjoint apart form their common boundary. We assume further that we may express 

M + = R≥0×N where N is some ( n−1) - dimensional compact manifold. On the end R≥0×N ,we denote by r a coordinate on the R≥0 fibre. Additionally, we denote the coordinates on any local (angular) chart on N with a θa, where a = 1 , . . . , n − 1, and we use a, b, c, . . . to index angular coordinates. When referring to the full set of coordinates on M + we use the notation x1 = θ1, . . . , x n−1 = θn−1, xn = r and we use i, j, k, . . . to index over all coordinates. We define a reference locally hyperbolic metric ˚ g on the exterior region M + to be ˚g = dr 2 + f 2 

> k

(r + r0)˚h (2.1) for some r0 > 0 where ˚h is a metric on N of constant scalar curvature ( n − 1)( n − 2) k for 

k ∈ {− 1, 0, 1} and 

fk(r) = 



sinh( r) k = 1 ,er k = 0 ,

cosh( r) k = −1.

In particular, when k = 1 and N = Sn−1, ˚ g is the standard hyperbolic metric. We additionally note that the scalar curvature of a warped product metric like ˚ g may be computed via the formula 

S˚g = −2( n − 1) f ′′ 

> k

fk

− (n − 1)( n − 2) 

f ′

> k

fk

2

+ S˚h

f 2

> k

.

From this, one may compute that S˚g ≡ − n(n − 1) for each k in the above definition. For the next definition below, we choose a finite set of preferred charts Ui covering N ,each with a preferred choice of local coordinates {θ1, . . . , θ n−1}. We extend these charts to 

M + by defining Vi = R≥0 × Ui with coordinates {r, θ 1, . . . , θ n−1} and fix them from hereon. For a function φ on the end R≥0 × N we use the notation φ = Om(e−αr ) to indicate that 

φ and all of its first m derivatives in the coordinates defined above decay as e−αr , that is there exists a constant C > 0 such that φ satisfies |∂β φ| ≤ Ce −αr where β indicates any multi-index with 0 ≤ | β| ≤ m.We adopt the following definition of ALH manifolds which, while differing slightly, is consistent with those found in the literature (e.g. in [AILA18, CH03, CGNP18, Wan01]). 

Definition 2.1 (Asymptotically Locally Hyperbolic) . We say a Riemannian manifold (M, g )

is asymptotically locally hyperbolic of regularity order m ∈ N and with decay exponent α > 07if we can write M = M0 ∪ (R≥0 × N ) and we can write the metric components of g on any preferred coordinate chart as 

grr = ˚ grr = 1 , gab = ˚ gab + Om

 e−(α−2) r , gra = Om

 e−(α−1) r

where ˚g is a reference locally hyperbolic metric of the form (2.1) for some k ∈ {− 1, 0, 1}. If 

(N, ˚h) is the round sphere then we simply say that g is asymptotically hyperbolic. 

It is clear that if ( M, g ) is ALH with decay exponent α then it is also ALH with decay exponent α′ for any 0 < α ′ < α . We note that if α < 1, then ( M, g ) is C0,α conformally compactifiable and if α ≥ 1 then ( M, g ) is C1 conformally compactifiable. For terminology, see for example [CGNP18]. In the remainder of this paper, we will make regular use of the coordinate function r

corresponding to the R≥0 fibre of the exterior region M +. We note that the particular choice of r is not unique, in that the reference metric ˚ g defined above may be expressed in the form (2.1) for arbitrarily many choices of coordinate function r via diffeomorphism of M + or by an altogether different choice of splitting of M into the interior and exterior regions M0 and 

M +. To avoid this complication, whenever we speak of an ALH manifold as defined above, we implicitly assume that there is a pre-chosen r.We provide the following computational lemma establishing the corresponding decay of the metric inverse and Christoffel symbols which will be useful to us later. 

Lemma 2.2. Suppose (M, g ) is an ALH manifold of regularity order 1 and decay exponent 

α. Then, in any of the preferred charts 

grr = 1 + O1(e−2αr ),

Γrrr = O  e−αr  ,

Γabr = ˚Γabr + O  e−αr  ,gra = O1(e−(α+1) r),

Γarr = O  e−(α+1) r ,

Γrab = ˚Γrab + O  e−(α−2) r ,gab = ˚ gab + O1(e−(α+2) r),

Γrar = O  e−(α−1) r ,

Γabc = ˚Γabc + O  e−αr  ,

where we use the notation ˚Γ to denote the Christoffel symbols of the reference locally hyper-bolic metric ˚g which satisfy 

˚Γrab = O2

 e2r , ˚Γabr = O2 (1) , ˚Γabc = O2 (1) .

We provide an example of an ALH manifold in the sense of Definition 2.1 which is not covered by the existing literature for the Yamabe problem on asymptotically hyperbolic manifolds. In particular, the class described below includes metrics where not all of the sectional curvatures are decaying to a negative constant at infinity. 

Example 2.3. Consider the warped product manifold M 3 = R≥0 × T2 where T2 is the 2-dimensional flat torus with metric (dx 1)2 + ( dx 2)2 and standard coordinates {xa}. We endow 

M 3 with the diagonal metric 

g = dr 2 + e2r  p(r)( dx 1)2 + p−1(r)( dx 2)2 .

8This metric is ALH in the sense of Definition 2.1 provided, for example, p(r) = 1 + O(e−αr )

and p′(r) = O(e−αr ), which we assume in this example. The metric g has Ricci curvature 

Rrr = −2 − 12

p′

p

2

, R11 = e2rp −2 + 12

p′

p

2

− p′

p − 12

p′′ 

p

!

,R22 = e2rp−1 −2 − 12

p′

p

2

+ p′

p + 12

p′′ 

p

!

.

We see that the Ricci curvature does not necessarily decay to a constant multiple of the metric (note the presence of the p′′ term in R11 and R22 ). In contrast, the metric g has scalar curvature 

Sg = −6 − 12

p′

p

2

= −6 − O (e−αr ). (2.2) The example above demonstrates a class which does not satisfy the requirements (dis-cussed in more detail in the following section) in [ACF92] or [AILA18] but which falls under Definition 2.1. There are certainly many such p which behave wildly in C2 and so have poor behaviour of the Ricci curvature, for example take p(r) = 1 + e−2αr sin( eαr ). 

## 2.2 Existence of a solution for the Yamabe problem 

In this section we will exhibit a sub-solution to (Ya), from which existence of a solution follows via the arguments of Aviles and McOwen in [AM88b]. 

Lemma 2.4. Let (M, g ) be ALH of regularity order 1 and with decay exponent α < n and satisfy (1.2) . For any 0 < β < min( n − 1, α ), there exist constants 0 < δ < 1, close to 1,and θ > 0, large, such that the function u− ∈ H1loc (M ) defined by 

u− := 



1 − C(θ, δ )e−αr on {rδ ≤ r} × N

1 − θe −βr on {rθ ≤ r ≤ rδ} × N

0 on M0 ∪ ({r ≤ rθ} × N ) ,

where rδ := 1 

> β

log   θ

> 1−δ

, rθ := 1 

> β

log ( θ) and C(θ, δ ) =   θ

> 1−δ

αβ , is a sub-solution of (Ya) on 

M which is positive outside of some compact set. 

We note here that the choice of C(θ, δ ) ensures that u− is continuous and therefore belongs to H1loc (M ). The change at rδ is used only in the case that n − 1 ≤ α < n .9We have a sub-solution of the form u− = u−(r) so we are led to consider the ordinary differential inequality arising immediately from (Ya) 

−cn

 1 + O(e−2αr ) u′′ − + cn



(n − 1) f ′

> k

fk

+ O(e−αr )



u′−

−  n(n − 1) + O(e−αr ) u− ≤ − n(n − 1) u n+2  

> n−2
> −

. (2.3) 

Proof. Fix some 0 < β < min( n − 1, α ). To establish that u− is a sub-solution, we must show that (2.3) holds on {rθ ≤ r ≤ rδ} and {rδ ≤ r} and check the following transmission conditions at rθ and at rδ,lim 

> r↗rθ

u′−(r) ≤ lim 

> r↘rθ

u′−(r) and lim 

> r↗rδ

u′−(r) ≤ lim 

> r↘rδ

u′−(r).

The first condition is immediate as β > 0 and the second condition holds true as β < α .To establish (2.3) it suffices to show, for some constant C1 > 0 depending only on g, that there exist θ and δ (possibly depending on β) such that 

L−u− := − cnu′′ − − cn



(n − 1) f ′

> k

fk

− C1e−αr 



u′−

−  n(n − 1) − C1e−αr  u− + C1e−2αr |u′′ −| ≤ − n(n − 1) u n+2 

> n−2
> −

(2.4) holds on {rθ < r < r δ} and {rδ < r }. We note here that u′− ≥ 0 for all r.In the following, we write C to indicate a constant changing from line to line but de-pending only on g. For {rθ < r < r δ}, we have that n(n − 1) u n+2  

> n−2
> −

≤ n(n − 1) δ 4 

> n−2

u− as 0 ≤ u− ≤ δ. We compute 

L−u− + n(n − 1) u n+2  

> n−2
> −

< c nθ



β2 − (n − 1) β + 14n(n − 2)(1 − δ 4 

> n−2

)



e−βr 

+ C(e(β−α)r + θe −αr + θe −2r

| {z }

> A

)e−βr 

where we used that f ′   

> k(r+r0)
> fk(r+r0)

> 1 − Ce −2r and u′− ≥ 0. Note first that, for δ close to 1, the first term of the RHS of the above is a negative multiple of e−βr . In addition, as β < α 

we have, for r ≥ rθ, that |A(r)| ≤ A(rθ) ≤ C(θ1− αβ + θ1− 2 

> β

). Consequently, for θ sufficiently large, the first term on the RHS dominates and, for all δ sufficiently close to 1, we have 

L−u− + n(n − 1) u n+2  

> n−2
> −

< 0 in {rθ < r < r δ}. We choose such a θ and fix it from here on. On {r > r δ}, note that we have δ ≤ u− ≤ 1. As 

x n+2  

> n−2

− 1 − n + 2 

n − 2(x − 1) =

Z 1

> x

4 n + 2 (n − 2) 2 t− n−6 

> n−2

(x − t) dt < 4 n + 2 (n − 2) 2 δ− n−6 

> n−2

(x − 1) 2

10 for δ < x ≤ 1. We have, 

n(n − 1) u n+2  

> n−2
> −

< n (n − 1) − cn

n

4 (n + 2) C(θ, δ )e−αr + cn

n(n + 2) (n − 2) δ− n−6 

> n−2

C(θ, δ )2e−2αr .

Using again that f ′   

> k(r+r0)
> fk(r+r0)

> 1 − Ce −2r and u′− ≥ 0, we obtain 

L−u− + n(n − 1) u n+2  

> n−2
> −

≤ cne−αr C(θ, δ )

h

α2 − (n − 1) α − n

+ C



δ− n−6 

> n−2

C(θ, δ )e−αr + e−αr + e−2r + 1

C(θ, δ )

| {z }

> B

i 

. (2.5) As α < n , α2 − (n − 1) α − n < 0. We note that B(r) is non-increasing. We have for r > r δ.0 < B (r) < B (rδ) = 

"

δ− n−6 

> n−2

(1 − δ) + 

 θ

1 − δ

− αβ

+

 θ

1 − δ

− 2

> β

+ 1

C(θ, δ )

#

→ 0 as δ ↗ 1.

It follows that for δ close to 1, L−u− + n(n − 1) u n+2  

> n−2
> −

< 0 as required. We note that if α = n, the leading term in (2.5) vanishes and so the above computation does not work . However, it is possible to adapt the proof to include the case that α = n

by using a decay rate of re −nr for r > r δ and making the corresponding adjustments. Asimilar obstacle occurs in the later construction of a corresponding super-solution and can be treated with the same adjustment. We now use the above sub-solution to prove the existence part of Theorem 1.1. 

Proposition 2.5. Let (M, g ) be ALH of regularity order 1 and with decay exponent α ∈

(0 , n ) satisfying (1.2) . There exists a positive smooth solution u of (Ya) on M satisfying 

u ≥ 1 − Ce −αr for some C > 0. Consequently, there exists a complete conformal metric ˜g

such that S˜g ≡ − n(n − 1) on M .Proof. By Lemma 2.4 there exists a sub-solution u− of (Ya) which satisfies u− ≥ 1 − Ce −αr .The sub- and super-solution argument of Aviles and McOwen in [AM88b, Proposition 2.1] yields a smooth solution u of (Ya) satisfying u ≥ u− on M . It remains to show that u

is positive on all of M ; once this is established, we will have obtained a conformal metric ˜g = u 4 

> n−2

g which is complete, from the sub-solution lower bound, and has constant scalar curvature. As u ≥ u−, u is non-negative and positive outside of some compact set. Let B be a large ball on which u̸ ≡ 0 and outside of which u > 0. On B, the scalar curvature Sg ≤ A for 11 some constant A > 0. Consequently, taking a sufficiently large constant C > 0 such that u

satisfies 

cn∆gu − Cu ≤ [n(n − 1) u n+2  

> n−2

+ Au ] − Cu ≤ 0,

we can apply the strong maximum principle ([GT01, Theorem 3.5]) to deduce that, as u̸ ≡ 0on B, u is strictly positive in B and so on all of M .

## 2.3 Asymptotic properties of the conformal factor 

In order to complete the proof of the remaining parts of Theorem 1.1, we study the asymp-totic properties of solutions of the Yamabe equation as well as the asymptotic properties of the particular conformal factor obtained as the solution to (Ya) in the previous sub-section. 

2.3.1 An upper bound at infinity 

We will first establish an a priori upper bound on solutions to the Yamabe equation for ALH manifolds in the sense of Definition 2.1. 

Proposition 2.6. Let (M, g ) be ALH in the sense of Definition 2.1 and suppose that 

lim inf  

> r(x)→∞

Sg(x) ≥ − n(n − 1) . (2.6) 

Then all solutions of the (Ya) on (M, g ) satisfy lim sup r(x)→∞ u(x) ≤ 1.

A key point for our discussion will be to compare the Laplacian of the perturbed metric 

g to that of the reference metric ˚ g. In particular, where we use ∇ and ˚∇ to denote the covariant derivative with respect to g and ˚ g respectively, we compute directly that ∆gφ = ˚ gij ˚∇i ˚∇j + ( gij − ˚gij )˚∇i ˚∇j φ + gij (Γ kij − ˚Γkij )∂kφ

= ∆ ˚gφ + aij ˚∇ij φ + bi ˚∇iφ (2.7) where aij := gij − ˚gij and bi := gjk (Γ ijk − ˚Γijk ) satisfy aij = O1(e−(α+2) r) and bi = O(e−αr )using the estimates for the Christoffel symbols found in the proof of Lemma 2.2. We will make use of the following consequence of the maximum principle: 

Lemma 2.7. Let u > 0 be a bounded smooth solution to (Ya) on a bounded open set Ω ⊂ M

and ¯u > 0 be a smooth super–solution to (Ya) on Ω satisfying ¯u(x) → ∞ as x → ∂Ω. Then necessarily u < ¯u on Ω.Proof. Due to the facts that ¯ u → ∞ as x → ∂Ω, u is bounded and both u > 0 and ¯ u > 0, there must exist some C > 0 such that the difference wC := C ¯u − u satisfies that wC ≥ 012 and achieves 0 at some point in Ω. We claim that C < 1. If C ≥ 1, then wC would satisfy, 

−cn∆gwC − n(n − 1) wC ≥ − n(n − 1) 



C ¯u n+2  

> n−2

− u n+2 

> n−2



≥ − n(n − 1) 



(C ¯u) n+2  

> n−2

− u n+2 

> n−2



= c(x)wC

where 

c(x) := 

((C ¯u) n+2     

> n−2−un+2
> n−2
> C¯u−u

for wC̸ = 0 , 

> n+2
> n−2

(C ¯u(x)) 4 

> n−2

if wC = 0 .

We could then apply the strong maximum principle to the linear differential inequality 

−cn∆gwC − (n(n − 1) + c(x)) wC ≥ 0, noting that the sign of ( n(n − 1) + c(x)) does not matter as the value of the minimum in question is 0, see [GT01, Section 3.2]. We would then have that wC ≡ 0, a contradiction as wC → ∞ at the boundary. We conclude that C < 1 as claimed and so u < ¯u in Ω. In order to prove the upper bound in Proposition 2.6, we will study a family of ODE solutions on annuli in the following series of lemmas. 

Lemma 2.8. There exists a positive solution u1 of the equation 

−cn (u′′  

> 1

+ ( n − 1) u′

> 1

) − n(n − 1) u1 + n(n − 1) u n+2  

> n−2
> 1

= 0 on (−1, 1) (2.8) 

satisfying u1(r) → ∞ as r → ± 1 and there exists a constant C > 0 depending on n such that u1 satisfies 

1

C (1 − | r|)− n−22 ≤ u1(r) ≤ C(1 − | r|)− n−22 ,u′

> 1

(r) ≤ C(1 − | r|)− n 

> 2

,u′′  

> 1

(r) ≤ C(1 − | r|)− n+2 2 .

(2.9) 

Proof. This result is essentially due to [ACF92]. Consider the model locally hyperbolic manifold ( R × Tn−1, g δ) where ( Tn−1,˚h) is the flat Torus. Define the annulus A1 := {| r| ≤ 

1} ⊂ M . We note here that any solution of (2.8) would automatically be a solution of the Yamabe equation 

−cn∆gδ u1 − n(n − 1) u1 + n(n − 1) u n+2  

> n−2
> 1

= 0 on the annulus in this particular model space. From [ACF92, Theorem 1.2], we know that, on the annulus A1, there exists a unique solution u1 of the Yamabe equation satisfying u1 → ∞ 

at the boundary ∂A 1. Additionally, from Theorem 1.3 of [ACF92], we know the behaviour of u1 at the boundary satisfies (2.9). We note that the Yamabe equation is invariant under symmetries of the Torus and so, by uniqueness, u1 must be radial and so the Yamabe equation reduces to the ODE (2.8) as desired. 13 Equation (2.8) has the following important scaling property that we will make use of: if we define the family {uR} by 

uR(r) = 

 (e2 − 1) eR

e2+ R + e2R+r − e2+ r − eR

n−22

u1



log 

 (e2R − 1) er+1 

e2+ R + e2R+r − e2+ r − eR

 

, (2.10) then each uR provides a solution of the ODE 

−cn (u′′  

> R

+ ( n − 1) u′

> R

) − n(n − 1) uR + n(n − 1) u n+2  

> n−2
> R

= 0 on ( −R, R ). (2.11) Furthermore, from the growth rate of u1 in (2.9) we have that each uR satisfies that uR(r) →∞ as r → ± R and, for some constant CR > 0 depending on R and n, that 1

CR

(R − | r|)− n−22 ≤ uR(r) ≤ CR(R − | r|)− n−22 ,u′

> R

(r) ≤ CR(R − | r|)− n 

> 2

,u′′ 

> R

(r) ≤ CR(R − | r|)− n+2 2 .

(2.12) We now establish locally uniform convergence of this family to 1 as R → ∞ .

Lemma 2.9. The family {uR}R> 0 of positive solutions of the equation (2.11) defined above is decreasing with respect to R and satisfies uR ↘ 1 uniformly on compact sets as R → ∞ .Proof. If R1 < R 2, we may apply Lemma 2.7 on the annulus AR1 (0) to see that uR2 < u R1 .Consequently, {uR} is monotone decreasing. Define the pointwise limit u∞(r) := lim R→∞ uR(r). We now show that {uR} converges locally in C2 to u∞. To this end, a locally uniform bound on the first derivative will suffice, as from this we immediately obtain local boundedness of u′′  

> R

and u′′′  

> R

(the latter after differ-entiating the ODE once). The Arzela-Ascoli theorem then provides the desired convergence. To obtain such a bound on the first derivative, note that on any compact domain [ −R0, R 0]and for R > R 0 + ε, the fact that {uR} is monotone decreasing implies 

u′′  

> R

+ ( n − 1) u′ 

> R

= n(n − 2) 4



u n+2  

> n−2
> R

− uR



is bounded in [ −R0, R 0] uniformly as R → ∞ . Integrating the above from some point 

s ∈ [−R0, R 0] to r ∈ [−R0, R 0] we obtain that u′

> R

(r) − u′

> R

(s) is bounded in [ −R0, R 0]uniformly as R → ∞ . Integrating the above, now in s, from −R0 to R0 we see that u′ 

> R

is bounded in [ −R0, R 0] uniformly as R → ∞ .We proceed to show that u∞ is constant by using the scaling property (2.10) of the family 

uR. In particular, for any R, S > 0 we can verify that 

uR(r) = 

 (e2S − 1) eR

e2S+R + e2R+r − e2S+r − eR

n−22

uS



log 

 (e2R − 1) er+S

e2S+R + e2R+r − e2S+r − eR

 

.

(2.13) 14 Consider the value of uR at r = 0 and write R = S + Λ. We then have 

uS+Λ (0) = 

 e3S+Λ − eS+Λ 

e3S+Λ + e2( S+Λ) − e2S − eS+Λ 

n−22

uS



log 

 e3S+2Λ − eS

e3S+Λ + e2( S+Λ) − e2S − eS+Λ 

 

.

Taking the limit as S → ∞ while keeping Λ fixed we then obtain that for all Λ, u∞(0) = 

u∞(log  eΛ) = u∞(Λ). Consequently, u∞ ≡ C∞ for some constant C∞ ≥ 0. Recall that uR converges locally in C2 to u∞ and so u∞ solves the Yamabe equation. Consequently, as u∞ is constant, either u∞ ≡ 0 or u∞ ≡ 1. It then suffices to show that u∞(0) > 0 to conclude the proof. We take the limit in (2.10) as R → ∞ at r = 0 to obtain lim  

> R→∞

uR(0) = lim  

> R→∞

e− n−22 Ru1

 1 − (e2 − 1) e−R + O(e−2R)

and we note also that 1 − (e2 − 1) e−R + O(e−2R) → 1. Then, from the asymptotic rates (2.9) for u1, we conclude that 

u∞(0) = lim  

> R→∞

uR(0) ≥ lim  

> R→∞

Ce − n−22 R  (e2 − 1) e−R + O(e−2R)− n−22 = C(e2 − 1) − n−22 > 0.

Consequently, we conclude that u∞ ≡ 1. Having established the properties of the family uR above, we now prove Proposition 2.6 by showing that these functions can be used to generate super-solutions with the desired properties on annuli in the asymptotic region. 

Proof of Proposition 2.6. First, we consider the Yamabe equation for g as a perturbation of an elliptic equation with respect to the reference metric ˚ g as in (2.7). Fix R > 0 and consider some point x∗ ∈ M + such that r∗ := r(x∗) > R . To bound the value of u at x∗, we define the annulus Ω R := Ω( R, r ∗) = {x ∈ M + : |r(x) − r∗| < R } and define a candidate super-solution to (Ya) on Ω R,¯u(x) := Au R(r(x) − r∗)where uR is defined in (2.10) and A > 0 is some constant to be determined. In the argument below, all implicit constants in various O terms are independent of both A and R.We first note that 

−cn∆˚g ¯u = −cn (∂rr ¯u + ( n − 1) qk(r)∂r ¯u) = A  −cn (u′′  

> R

+ ( n − 1) u′

> R

) + O(e−2r|u′

> R

|)

where 

qk(r) = 



coth( r) k = 1 ,

1 k = 0 ,

tanh( r) k = −1,

15 and k is as in the definition of reference metrics in (2.1) and we use only that qk = 1+ O(e−2r). Consequently, from (2.11), we have that ¯ u satisfies 

−cn∆˚g ¯u − n(n − 1)¯ u + n(n − 1)¯ u n+2  

> n−2

= ( A n+2  

> n−2

− A)u n+2  

> n−2
> R

+ AO(e−2r|u′

> R

|)for the reference metric ˚ g on Ω R ⊂ M + and ¯ u blows up as x → ∂ΩR. If follows that 

−cn∆˚g ¯u + Sg ¯u + n(n − 1)¯ u n+2  

> n−2

+ aij ˚∇ij ¯u + bi ˚∇i ¯u

= n(n − 1)( A n+2  

> n−2

− A)u n+2  

> n−2
> R

+ A



aij ˚∇ij uR + bi ˚∇iuR + ( Sg + n(n − 1)) uR



≥ n(n − 1)( A n+2  

> n−2

− A)u n+2  

> n−2
> R

− Aε (r∗) ( |u′′ 

> R

| + |u′

> R

| + |uR|)where ε(r) ≥ 0 and lim r→∞ ε(r) = 0; here we have used (2.6) as well as the asymptotic local hyperbolicity. From the asymptotic rates in (2.12), we see that there exists a constant CR > 0 depending on R such that |u′′ 

> R

| + |u′

> R

| + |uR| ≤ CRu n+2  

> n−2
> R

near the boundary. Therefore, 

−cn∆˚g ¯u + Sg ¯u + n(n − 1)¯ u n+2  

> n−2

+ aij ˚∇ij ¯u + bi ˚∇i ¯u

≥ n(n − 1) 



A n+2  

> n−2

− A (1 + CRε(r∗)) 



u n+2  

> n−2
> R

.

We can now choose A = 1 + ˜Cε (r∗) with a sufficiently large constant ˜C independent of x∗

so that the RHS above is positive and so ¯ u is a strict super-solution to (Ya). We may now apply Lemma 2.7 to conclude that u < ¯u on Ω R and so we have shown that any solution to the Yamabe equation u satisfies u(x∗) < (1 + ˜Cε (r∗)) uR(0) . Conse-quently, as x∗ was arbitrary and ε(r∗) → 0, we have lim sup r(x)→∞ u(x) ≤ uR(0) . As R > 0was arbitrary, we may now take the limit as R → ∞ to conclude, from Lemma 2.9, that lim sup r(x)→∞ u(x) ≤ 1 as desired. 

2.3.2 A lower bound at infinity 

In this sub-section, we provide an a priori lower bound for solutions u of the Yamabe equation for ALH manifolds in the sense of Definition 2.1. We highlight that Example 1.2 demonstrates, in a similar way as for uniqueness of the conformal factor, that we must impose some additional condition before attempting to bound the conformal factor u from below. We first provide a lower bound under the assumption that the solution is bounded away from zero at infinity in the sense of (2.15) below. We then refine this first result by weakening the strictly positive requirement of (2.15) to allow some degree of decay of u to zero. 16 Lemma 2.10. Let (M, g ) be ALH in the sense of Definition 2.1 and suppose that 

lim  

> r(x)→∞

|Sg(x) − n(n − 1) | = 0 . (2.14) 

Then any solution u of (Ya) on (M, g ) satisfying 

lim inf  

> r(x)→∞

u(x) > 0 (2.15) 

must satisfy lim r(x)→∞ u(x) = 1 .

Proof. Suppose, for the sake of contradiction that the conclusion fails. Since, by Proposition 2.6, we have that lim sup r(x)→∞ u(x) ≤ 1, we must have that δ = lim inf r(x)→∞ u(x) ∈ (0 , 1). Let {(ri, θ i)} ⊂ M + be a sequence such that ri → ∞ and u(ri, θ i) → δ. Passing to a subsequence, we may assume that θi → θ∞ for some θ∞ ∈ N . Take a normal coordinate chart U on N around θ∞ with coordinate functions θa : U → Rn so that ˚hab (θ∞) = δab .Consider the region Ω := R≥0 × U ⊂ M +. For each i, define a map Ψ i : Ω → R × Rn−1 =

{(˜ r, ˜θ) : ˜ r ∈ R, ˜θ ∈ Rn−1} by Ψi(r, θ ) = ( r − ri, e ri (θ − θi)) and define ˜Vi := Ψ i(Ω) . We also write ψi(θ) := eri (θ − θi). Define vi := u ◦ Ψ−1 

> i

: ˜Vi → R.

We note here that ˜V1 ⊂ ˜V2 ⊂ . . . and ∪i ˜Vi = R × Rn−1.We next compute the equation corresponding to (Ya) that vi satisfies. We denote partial derivatives in the coordinates (˜ r, ˜θ) by ˜∂, that is we write ∂∂ ˜r = ˜∂r and ∂∂ ˜θa = ˜∂a. On R×Rn−1

let gi =  Ψ−1

> i

∗ g. Noting that, by asymptotic local hyperbolicity, we may express g in the form 

g = dr 2 + εra drdθ a +



fk(r + r0)˚hab + εab 



dθ adθ b,

where εra (r, θ ) = Om(e−(α−1) r) and εab (r, θ ) = Om(e−(α−2) r). We thus have 

gi = d˜r2 + e−ri εra ◦ Ψ−1 

> i

d˜rd ˜θa + e−2ri



f 2 

> k

(˜ r + ri + r0)˚hab ◦ ψ−1 

> i

+ εab ◦ Ψ−1

> i



d˜θad˜θb

= d˜r2 + e2(˜ r+r0)˚hab ◦ ψ−1 

> i

d˜θad˜θb + e−2ri ˆεab d˜θad˜θb + e−αr i



˜εra d˜rd ˜θa + ˜ εab d˜θad˜θb



where ˆ εab = ˆ εiab =  f 2 

> k

(˜ r + ri + r0) − e2( ri+˜ r+r0)˚hab ◦ ψ−1 

> i

, ˜ εra = ˜ εira = e(α−1) ri εra ◦ Ψ−1

> i

and ˜ εab = ˜ εiab = e(α−2) ri εab ◦ Ψ−1 

> i

. In particular, as i → ∞ , the sequence of matrices of metric components of gi in (˜ r, ˜θ) is uniformly bounded in C1 and uniformly positive definite on any compact subset of R × Rn−1. In addition, {gi} converges in C1loc (R × Rn−1) to 

g∞ = d˜r2 + e2(˜ r+r0)δab d˜θad˜θb.17 Each vi solves the equation 

−cn∆gi vi = sivi − n(n − 1) 



v n+2  

> n−2
> i

− vi



= civi (2.16) where si = Sgi ◦ Ψ−1 

> i

+ n(n − 1) which, by (2.14), satisfies si → 0 in C0loc as i → ∞ and 

ci = si − n(n − 1) 

 u ◦ Ψ−1

> i

 4 

> n−2

− 1



. By Proposition 2.6, u is bounded and so {ci} is uniformly bounded on any compact subset of R × Rn−1. Consequently, fixing some R > 0, we may apply the Harnack inequality of [GT01, Theorem 8.20] to the equation Livi = 0 where Li := cn∆gi + ci to conclude that, on the ball BR(0 , 0) ⊂ R × Rn−1,sup 

> BR(0 ,0)

vi ≤ CR inf  

> BR(0 ,0)

vi ≤ CRδ (2.17) where the final inequality follows from the fact that vi(0 , 0) → δ by construction and C is some constant independent of i (depending only on n, R and bounds on the ellipticity of Li

and sup-norm of the coefficients of Li which we have shown may be chosen independently of 

i). We conclude that {vi} is uniformly bounded on BR(0 , 0). After recasting (2.16) to non-divergence form and noting that g is ALH of regularity order 1, we may now apply standard W 2,p estimates ([GT01, Theorem 9.11]) to conclude that vi are locally uniformly bounded in W 2,p for all p ∈ (1 , ∞) and hence in C1,β for all 

β ∈ (0 , 1). Therefore, passing to a subsequence if necessary, we may assume that vi →

v∞ in C1loc (R × Rn−1). Furthermore, for any point (˜ r0, ˜θ0) ∈ R × Rn−1 and corresponding sequence (¯ ri, ¯θi) := Ψ −1 

> i

(˜ r0, ˜θ0) ∈ M +, we have that 

v∞(˜ r0, ˜θ0) = lim 

> i→∞

(vi ◦ Ψi)(¯ ri, ¯θi) = lim  

> i→∞

u(¯ ri, ¯θi) ≥ δ. 

We now pass to the limit as i → ∞ in (2.16) to obtain 

−cn∆g∞ v∞ = −n(n − 1) 



v n+2  

> n−2
> ∞

− v∞



on R × Rn−1, (2.18) and so v∞ is in fact in C∞(R × Rn−1) (as v∞ > 0). By construction, we have that v∞(0 , 0) = lim i→∞ vi(Ψ( ri, θ i)) = lim i→∞ u(ri, θ i) = δ. Since δ is a strict sub-solution of (2.18) and 

v∞ ≥ δ on R × Rn−1, we obtain a contradiction to the strong comparison principle. We are now able to prove our main result of the section, expanding the extent of the lower bound result by allowing for the conformal factor to exhibit decay to zero at infinity. 

Proposition 2.11. Let (M, g ) be an ALH manifold in the sense of Definition 2.1 which satisfies (2.14) . Suppose that u is a solution of the Yamabe problem on (M, g ) and that there exist an S > 0 and r1 > r 0 such that u(r + S)

u(r) > n

2 e− n−22 S − n − 22 e− n  

> 2S

for all r > r 1, (2.19) 

where u(r) := min N u(r, ·). Then lim r(x)→∞ u(x) = 1 .

18 We note that the asymptotic exponential rate of −n−22 is also seen in Example 1.2 and represents a borderline rate where a solution to (Ya) exists with such a rate of decay but notably the corresponding conformal metric fails to be complete. Indeed, for any slower decay, we obtain the following immediate corollary of Proposition 2.11: 

Corollary 2.12. Let (M, g ) be an ALH manifold in the sense of Definition 2.1 which satisfies 

(2.14) . There does not exist a solution u of (Ya) on M satisfying eβr (x)u(x) → 0 as r(x) → ∞ 

for any 0 < β < n−22 .Proof of Proposition 2.11. By Lemma 2.10, it suffices to show that lim inf r(x)→∞ u(x) > 0. Suppose not, then there exists a sequence ri → ∞ such that u(ri) → 0. It follows that min  

> r(x)∈[r1,R ]

u(x) → 0 as R → ∞ .

Consequently, for R sufficiently large the minimum cannot be attained at r1. Furthermore, the fact that u ≤ 1 (by Proposition 2.6) and lim inf u = 0 together imply, via the strong maximum principle, that u < 1 and satisfies 

−cn∆gu = −n(n − 1) 



u n+2  

> n−2

− u



> 0.

The strong maximum principle again implies that the minimum of u on {r(x) ∈ [r1, R ]} is achieved only on {r(x) = R} and so u is strictly decreasing for large r.Define αi := u(ri)−1 → ∞ and consider wi := αivi where vi is as in the proof of Lemma 2.10. Note that, by (2.16), wi satisfies −cn∆gi wi = ciwi. As in the proof of Lemma 2.10, we have that wi → w∞ in C1loc (R × Rn−1). Since αi → ∞ , the limit w∞ now solves 

−cn

 ˜∂rr w∞ + ( n − 1) ˜∂rw∞ + e−2(˜ r+r0)∆n−1w∞



= n(n − 1) w∞ on R × Rn−1. (2.20) Moreover, by construction, w∞(r, θ ) ≥ 1 for r ≤ 0 and there exists a θ0 such that w∞(0 , θ 0) = 1. We will now see that the above provides a contradiction to (2.19). Indeed, consider the radial function 

w(r) = n

2 e− n−22 r − n − 22 e− n 

> 2r

which solves (2.20) and satisfies w(0) = 1 and w′(0) = 0. By assumption (2.19), there exists an S > 0 such that w∞(S, θ ) > w (S) for all θ ∈ N . Consequently, as w∞(0 , θ ) ≥ 1 = w(0), the strong maximum principle and the Hopf Lemma imply that we must have w∞ > w in the region {r(x) ∈ (0 , S )} and ∂rw∞(0 , θ 0) > 0. The latter contradicts the fact that w∞(r, θ ) ≥ 1for r ≤ 0 and w∞(0 , θ 0) = 1. 19 2.3.3 First derivative estimates at infinity 

In this sub-section, we prove results for the first derivative decay of the conformal factor. We begin by defining a particular super-solution on M . The following super-solution will provide an asymptotic upper bound on our solution obtained in Proposition 2.5 and will allow us to conclude that the conformal metric remains locally asymptotically hyperbolic to the same order. 

Lemma 2.13. Let (M, g ) be ALH of regularity order 1 and with decay exponent α ∈ (0 , n )

and Sg ≥ − n(n − 1) − Ce −αr for some constant C > 0. There exist constants A > 0 and 

R > 0 such that the function u+ ∈ H1loc (M ) defined by 

u+(r) := 

(

1 + Ae −αr on {r ≥ R} × N

1 + Ae −αR on M0 ∪ ({r < R } × N ) ,

is a super-solution to (Ya) on M .Proof. We first note that the transmission condition 0 = lim r↗R u′

> +

(r) ≥ lim r↘R u′

> +

(r) = 

−αAe −αR certainly holds. Thus, we only need to find large A and R such that 

−cn∆gu+ + Sgu+ ≥ − n(n − 1) u n+2 

> n−2
> +

holds in the two regions r ≤ R and r > R .We proceed similarly as in the proof of Lemma 2.4 with the difference that, as u+ > 1, we can estimate directly on the RHS that 

−n(n − 1) u n+2  

> n−2
> +

≤ − n(n − 1) 



1 + n + 2 

n − 2(u+ − 1) 



.

In the following the value of C may change from line to line but always depends only on 

g and we choose R larger if necessary so that R > 1. We compute for r > R , using that   

> f′
> k
> fk

(r + r0) > 1 − Ce −2r and u′ 

> +

< 0, 

−cn∆gu+ + Sgu++n(n − 1) u n+2  

> n−2
> +

≥− cnAe −αr 

"

α2 − (n − 1) α − n + Ce −αr + Ce −2r + CA| {z }

> B

#

.

Thus, we must choose A and R such that B ≤ 0. As α2 − (n − 1) α − n < 0, we can select an A0 and R such that the RHS of the above is positive for all A > A 0. Fix R from hereon. It remains to find an A > A 0 such that (2.3) holds on r ≤ R which can be verified by direct computation and noting that the scalar curvature must be bounded on this compact interior region. 20 Having established the super- solution above, we use it to gain control on the solution u

obtained in the Section 2.2. 

Lemma 2.14. Let (M, g ) be an ALH manifold of regularity order 1 and with decay exponent 

α ∈ (0 , n ) satisfying (1.3) . Then the smooth solution u of (Ya) on M obtained in Proposition 2.5 satisfies |u − 1| + |˚∇u|˚g = O(e−αr ). Furthermore, u is maximal in the sense that any solution ˜u of (Ya) satisfies ˜u ≤ u.Proof. We first prove the sup-norm decay. From Proposition 2.5, we have that u ≥ u− ≥

1 − Ce −αr where u− is the sub-solution constructed in Lemma 2.4. Additionally, Proposition 2.6 gives that lim sup r(x)→∞ u ≤ 1. Consequently, we have that lim r(x)→∞ u(x) = 1 To obtain the rate of decay from above, we show that u ≤ u+ where u+ is the super-solution u+ ≤ 1 + Ce −αr constructed in Lemma 2.13. For the sake of contradiction, we suppose that inf u+ 

> u

= 1 

> C

< 1 for some constant C > 1. As lim r(x)→∞ u+(x) 

> u(x)

= 1, the infimum would be achieved and so we could define v := Cu + − u which would satisfy v ≥ 0 and would achieve 0 at some minimum. We could then apply the same maximum principle argument as in Lemma 2.7 to conclude that inf u+ 

> u

≥ 1 and so u ≤ u+ as desired. We next prove the derivative estimates. Let ( r∗, θ ∗) ∈ M + be some arbitrary point with 

r∗ sufficiently large. Take a normal coordinate chart U on N around θ∗ with coordinate functions θa : U → Rn so that ˚hab (θ∞) = δab . Consider the region Ω := ( r∗ − 1, r ∗ + 1) × U ⊂ M +.

Define a map Ψ : Ω → R × Rn−1 = {(˜ r, ˜θ) : ˜ r ∈ R, ˜θ ∈ Rn−1} by Ψ( r, θ ) = ( r − r∗, e r∗ (θ − θ∗)) and define ˜V := Ψ(Ω) . We also write ψ(θ) := er∗ (θ − θ∗). Define v := u ◦ Ψ−1 : ˜V → R.

Let g∗ = (Ψ −1)∗g. As in the proof of Lemma 2.10, as r∗ → ∞ , g∗ converges in C1 to g∞ =

d˜r2 + e2(˜ r+r0)δab d˜θad˜θb. Moreover (see equation (2.16)), v satisfies ∆ g∗ v = O (e−αr ∗ ) where the implicit constant in the O term is independent of r∗. Applying W 2,p estimates to the above equation, after recasting to non-divergence form, and using Sobolev embeddings, we obtain |∇ v(0 , 0) |g∞ = O(e−αr ∗ ) and so obtain decay in the first derivative |∇ u|˚g = O(e−αr ). We finally address the maximality of u. Given another solution ˜ u > 0 of (Ya), we know that lim sup r(x)→∞ ˜u(x) ≤ 1, again from Proposition 2.6, and so we have that lim inf r(x)→∞ u 

> ˜u

≥

1 as lim r(x)→∞ u(x) = 1. Consequently, if inf u 

> ˜u

< 1 then the infimum must be attained and so we may apply the maximum principle (as in the proof of u ≤ u+) to conclude that ˜ u ≤ u.

## 2.4 Uniqueness and completion of the proof of Theorem 1.1 

Under assumption (1.2), the first part of Theorem 1.1 is proved in Proposition 2.5. For the remainder of the proof, we will assume that (1.3) holds. By Lemma 2.14, we know that 21 lim r→∞ u = 1, |u − 1| + |˚∇u|˚g = O(e−αr ) and u is the maximal solution of (Ya). It remains to prove the uniqueness of u and that the conformal metric ˜ g = u 4 

> n−2

g is ALH of regularity order 0 and with decay exponent α, which we now treat in turn. The uniqueness of u is a direct corollary of the stronger result below: 

Proposition 2.15. Let (M, g ) be ALH of regularity order 1 and decay exponent α ∈ (0 , n )

satisfying (1.3) . Then the solution u of the Yamabe problem on (M, g ) obtained in Proposition 2.5 is the unique solution such that there exist an S > 0 and r1 > r 0 such that u(r + S)

u(r) > n

2 e− n−22 S − n − 22 e− n  

> 2S

for all r > r 1, (2.21) 

where u(r) := min N ˜u(r, ·).Proof. Let ˜ u be any solution of (Ya) on ( M, g ) satisfying (2.21). By Proposition 2.11, we know that lim r→∞ ˜u = 1. Observe that in the proof of the maximality of u in Lemma 2.14 we actually proved that any solution of (Ya) which tends to 1 at infinity is maximal. Consequently, both u and ˜ u are maximal and hence equal. Lastly, we prove that the asymptotic local hyperbolicity of the obtained complete con-formal metric of constant scalar curvature, thus completing the proof of Theorem 1.1. 

Lemma 2.16. Let (M, g ) be an ALH manifold of regularity order 1 and with decay exponent 

α ∈ (0 , n ) satisfying (1.3) . Let u be the solution of (Ya) obtained in Proposition 2.5, then 

u = 1 + O(e−αr ) and the corresponding conformal metric is ALH of regularity order 0 and with decay exponent α.Proof. By Lemma 2.14 we have |u − 1| + |˚∇u|˚g = O(e−αr ). Consider the new coordinate function 

z := r +

Z ∞

> r



1 − u 2

> n−2



ds . 

First note that 

z − r =

Z ∞

> r



1 − u 2

> n−2



ds = O1(e−αr )and the map ( r, θ ) 7 → (z, θ ) is a diffeomorphism for large r. We will show that this implies ˜g = u 4 

> n−2

g is ALH of regularity order 0 and decay exponent α with respect to the coordinate system ( z, θ ). We compute that 

dz = u 2 

> n−2

dr −

Z ∞

> r

4 − nn − 2u4−nn−2 ∂au ds 



dθ a = u 2 

> n−2

dr + O(e−(α−1) r)dθ a.

22 Recalling that g is ALH and so may be written g = dr 2 + fk(r + r0)2˚h + εra dθ adr + εab dθ adθ b

where εab = O(e−(α−2) r) and εra = O(e−(α−1) r), we deduce that ˜g = dz 2 + fk(z + r0)2˚h + ˜ εza dθ adz + ˜ εab dθ adθ b

where ˜ εza = O(e−(α−1) z ) and ˜εab = u 4 

> n−2

εab +



u 4 

> n−2

fk(r + r0)2 − fk(z + r0)2

˚hab + O(e−2( α−1) z ).

Since fk(r + r0)2 = fk(z + r0)2 + O1(e−(α−2) z ), the conclusion follows. 

## 2.5 Asymptotically warped product manifolds 

To conclude this section, we briefly outline some remarks on the Yamabe Problem for asymp-totically warped product manifolds. Recall that, in the definition of ALH manifolds, we supposed that we could decompose (M, g ) in two parts, M = M0 ∪ M +, where M0 is some compact manifold with boundary, 

M + = R+ × N with ( N, ˚h) some compact manifold of constant scalar curvature S˚h =(n − 1)( n − 2) k for some k ∈ {− 1, 0, 1} and M0 and M + coincide on their common boundary. We then considered those metrics g which asymptote to the locally hyperbolic reference metrics in (2.1). One may, instead, consider a different choice of reference metric to which g is asymptotic. An immediate generalisation of interest would be the following warped product metrics ˚gf = dz 2 + f 2(z)˚h (2.22) where f is some positive function, usually referred to as the warping function. Metrics g

which are asymptotic to ˚ gf will be informally referred to as asymptotically warped product (AWP) metrics. In this section, we discuss the applications of Proposition 1.1 in this broader category of AWP metrics. This amounts to understanding whether the warped product metrics of (2.22) are conformal to the reference locally hyperbolic metrics of (2.1). We establish a necessary and sufficient condition on the warping function for such conformality in Proposition 2.17. The condition we identify is an integral condition of Keller-Osserman type (see [Kel57, Oss57]). Furthermore, we also show that, if the warped product metric is not conformally locally hyperbolic, then it is conformal to a complete metric of finite volume. 

Proposition 2.17. Let f : [0 , ∞) → R be a smooth, positive function. The metric ˚gf in 

(2.22) is conformal to a locally hyperbolic metric (2.1) if and only if 

I(f ) := 

Z ∞

> 0

1

f (s) ds < ∞. (2.23) 23 Moreover, if (2.23) does not hold, then ˚gf is conformal to dˇz2 + e−2ˇ z˚h which is a complete metric of finite volume on M +.Proof. Step 1: We first suppose that I(f ) < ∞ and show that ˚ gf is conformal to a locally hyperbolic metric. Recall the function fk in the definition of the locally hyperbolic reference metrics ˚ g in (2.1) and consider the following separable ODE for an unknown function K:

f (z)K′(z) = fk(K(z)) = 



sinh( K(z) + r0) k = 1 ,eK(z)+ r0 k = 0 ,

cosh( K(z) + r0) k = −1,

(2.24) with the initial condition K(z0) = 0 where z0 = 0 and r0 = 2 arctanh (exp( −I(f ))) if 

k = 1, z0 = 0 and r0 = log ( I(f )) if k = 0, and z0 satisfies R ∞ 

> z0

f (s) ds < π 

> 2

and r0 =2 arctanh 



tan 

π 

> 4

− 12

R ∞ 

> z0

f (s) ds 

 

if k = −1. It is straightforward to check that the explicit solution is defined for all z ≥ z0 and, furthermore, that K(z) is strictly increasing and 

K(∞) = ∞. Consequently, K : [ z0, ∞) → [0 , ∞) is a diffeomorphism. Consider a coordinate system ( r, θ ) on M + where θ is some coordinate system on N and 

r = K(z) for z > z 0. For z > z 0, in view of (2.1) and (2.24), we have ˚gf = ( K′(z)) −2  dr 2 + ( K′(z)f (z)) 2h = ( K′(z)) −2˚g

as desired. Step 2: In order to show the sufficiency in the proposition, we first prove that I(f ) = ∞ if and only if ˚ gf is conformal to a complete, finite volume metric on M +.To see this, first suppose I(f ) = ∞ and define ˇK(z) = log  1 + R z 

> 0

(f (s)) −1ds  so that ˇK′(z) = ( f (z)) −1 e− ˇK(z). As I(f ) = ∞, we may define a new coordinate ˇ z = ˇK(z) so that ˚gf = dz 2 + f 2(z)˚h =   ˇK′(z)−2 

dˇz2 + ( ˇK′(z)f (z)) 2˚h



=   ˇK′(z)−2 

dˇz2 + e−2ˇ z˚h



and so ˚ gf is conformal to dˇz2 + e−2ˇ z˚h which can readily be seen to be both complete and of finite volume on M +.Conversely, suppose that there exists some conformal factor u(z, θ ) such that ˇ g = u 4 

> n−2

(z, θ )˚ gf

for some complete, finite volume metric ˇ g. Consider the divergent curves γθ : [0 , ∞) → M +

defined by γθ(t) = ( z(t), θ ) for θ ∈ N . By completeness, we have that the length Lˇg(γθ) = ∞

for all θ ∈ N . We compute directly the length 

∞ = Lˇg(γθ) = 

Z ∞

> 0

pˇg ( ˙ γθ(t), ˙γθ(t)) dt =

Z ∞

> 0

u 2 

> n−2

(z, θ ) dz. 

24 Consequently, we may write 

∞ =

Z

> N

Lˇg(γθ) dθ =

Z

> N

Z ∞

> 0

u 2 

> n−2

(z, θ ) dz dθ 

≤

Z 

> N

Z ∞

> 0

u 2nn−2 (z, θ )f n−1(z) dz dθ 

 1 

> n

Z 

> N

Z ∞

> 0

1

f (z) dz dθ 

n−1

> n

= V ol ˇg(M +) 1 

> n

V ol h(N )n−1 

> n

I(f )n−1 

> n

.

Since V ol ˇg(M +) < ∞ we deduce that I(f ) = ∞.Step 3: We now suppose that I(f ) = ∞ and prove that then ˚ gf cannot be conformal to a locally hyperbolic metric. By Step 2, ˚ gf (which has I(f ) = ∞) cannot be conformal to another warped product metric ˚ g ˜f with I( ˜f ) < ∞, as the former is conformal to a complete metric of finite volume, and the latter cannot be. On the other hand, we can compute that I(fk) < ∞ for the reference locally hyperbolic metrics in (2.1) for each k = −1, 0, 1. The conclusion follows. It should be clear that, via Proposition 2.17, one can apply Theorem 1.1 to solve the Yamabe problem for AWP metrics with a wide range of warping functions. For further detail, the reader is referred to [Hog20]. The only reference warped product metrics for which this line of argument does not apply are those which are conformal to ˇ g = dˇz2 + e−2ˇ z˚h.It can be shown that ˇ g admits a conformal compactification where infinity corresponds to a single point, which is very different to the situation for ALH metrics. 

# 3 Volume ratio conditions for solvability of the Yam-abe problem 

In this section of this paper, we prove Theorem 1.3 concerning the negativity of the first eigenvalue of the conformal Laplacian on sub-domains of non-compact manifolds of negative curvature type satisfying the volume ratio condition (1.5). In view of the work of [AM88b], this leads us to an existence result for the Yamabe problem. We furthermore show that condition (1.5) is sharp for the negativity of the first eigenvalue (see Proposition 3.6). 

## 3.1 An upper bound on the eigenvalue for the conformal Laplacian 

As in the setting of Theorem 1.3, let ( M, g ) be a Riemannian manifold and suppose that there exist two open sets Ω 1 ⊂ Ω2 with C1 boundary which satisfy (1.4) and that the scalar curvature satisfies Sg ≤ − n(n − 1) on Ω 2.25 In proving Theorem 1.3, we relate the first eigenvalue of the conformal Laplacian on Ω 2

to the following sup-norm minimisation problem: 

H0 = inf 



H( ˜ φ) := sup 

> 0≤r≤R

F ( ˜ φ(r), ˜φ′(r)) : ˜ φ ∈ C1([0 , R ]) , ˜φ(0) = 0 , ˜φ(R) = 1 



(3.1) where F (y, z ) := cnz2−n(n−1) y2 and R is given in (1.4). Note that H( ˜ φ) ≥ F ( ˜ φ(0) , ˜φ′(0)) ≥

0 and so H0 ≥ 0. We recall the variational formulation of the first eigenvalue λ of the conformal Laplacian with Dirichlet boundary data on the bounded domain Ω 2:

λ = inf   

> φ∈H10(Ω 2),
> ∥φ∥L2=1

Z

> Ω2

 cn|∇ gφ|2 + Sgφ2 dV g. (3.2) Define the distance function r : Ω 2 \ Ω1 → [0 , R ] by r(x) = dg(x, ∂ Ω2). Central in our discussion will be test functions φ = φ(r) of the form 

φ(x) = 

( 1 x ∈ Ω1

˜φ(r(x)) x ∈ Ω2 \ Ω1

(3.3) where ˜ φ : [0 , R ] → R is a C1 function satisfying ˜ φ(0) = 0 and ˜ φ(R) = 1. We note that, as r

is Lipschitz, these conditions on ˜ φ ensure that φ ∈ H10 (Ω 2) and so is a valid test function. Assuming this form for φ, we bound the integral in (3.2) by 

Z

> Ω2

 cn|∇ gφ|2 + Sgφ2 dV g ≤

Z

> Ω2

 cn(φ′)2 − n(n − 1) φ2 dV g

≤ − n(n − 1) V ol g(Ω 1) + 

Z

> Ω2\Ω1

 cn( ˜ φ′)2 − n(n − 1) ˜ φ2 dV g

≤ − n(n − 1) V ol g(Ω 1) + V ol g(Ω 2 \ Ω1) sup 

> 0≤r≤R

 cn( ˜ φ′(r)) 2 − n(n − 1) ˜ φ2(r)

= −n(n − 1) V ol g(Ω 1) + V ol g(Ω 2 \ Ω1)H( ˜ φ) (3.4) where we used additionally that Sg ≤ − n(n − 1) on Ω 2. In particular, we have: 

Lemma 3.1. Let (M, g ) be a Riemannian manifold and suppose that there exist two open sets Ω1 ⊂ Ω2 with C1 boundary which satisfy (1.4) , that the scalar curvature satisfies Sg ≤−n(n − 1) on Ω2, and that 

H0

V ol g(Ω 2 \ Ω1)

V ol g(Ω 1) < n (n − 1) , (3.5) 

where H0 is the infimum defined in (3.1) . Then, the conformal Laplacian −cn∆g + Sg for 

(M, g ) has a negative first eigenvalue on Ω2.

26 Proof. The lemma follows from (3.1) and (3.4). The proof of Theorem 1.3 will use the explicit form of the solution of the minimisation problem (3.1) which we will obtain using [Aro65]. 2

Lemma 3.2. The minimisation problem (3.1) is uniquely solved by 

H0 = n(n − 1) csch 2

pn(n − 2) 2 R

!

and 

˜φ(r) = sinh 

pn(n − 2) 2 r

!

csch 

pn(n − 2) 2 R

!

. (3.6) 

Proof. Let A denote the set of admissible functions for (3.1), i.e. ψ ∈ A if ψ ∈ C1([0 , R ]), 

ψ(0) = 0 and ψ(R) = 1. Following [Aro65], we show that if ψ ∈ A , ψ′ > 0 in (0 , R ) and 

ψ solves the ODE F (ψ, ψ ′) ≡ constant in (0 , R ), then ψ is the unique minimiser of (3.1). To this end, we show that, for any function ψ2 ∈ A different from ψ, there exist points 

ξ, ξ 2 ∈ (0 , R ) such that ψ2(ξ) = ψ(ξ2) and ψ′

> 2

(ξ) > ψ ′(ξ2) > 0. This will suffice to show that 

ψ is the unique minimiser as 

H(ψ2) ≥ F (ψ2(ξ), ψ ′

> 2

(ξ)) > F (ψ(ξ2), ψ ′(ξ2)) = constant = H(ψ),

where the second inequality uses the fact that ∂z F > 0 for z > 0. As ψ′ > 0 in (0 , R ), we may define the inverse α(y) = ψ−1(y). Clearly α([0 , 1]) = [0 , R ]and α ∈ C([0 , 1]) ∩ C1((0 , 1)). Define r1 = sup {r : r ∈ [0 , R ], ψ 2(r) ≤ 0} and r2 = inf {r : r ∈

(r1, R ], ψ 2(r) ≥ 1}. Then 0 ≤ ψ2 ≤ 1 in [ r1, r 2], 0 < ψ 2 < 1 in ( r1, r 2) and we may define the function g := α(ψ2) on [ r1, r 2] where g ∈ C([ r1, r 2]) ∩ C1(( r1, r 2)). We claim that there exists r0 ∈ (r1, r 2) such that ψ(r0)̸ = ψ2(r0). Suppose not, then 

ψ(r) = ψ2(r) for r ∈ [r1, r 2] and so ψ(r1) = 0 and ψ(r2) = 1. By the strict monotonicity of 

ψ, we then have r1 = 0 and r2 = R, which implies ψ ≡ ψ2, a contradiction. Note that g(r1) = 0 ≤ r1, g(r0)̸ = r0 and g(r2) = R ≥ r2. As g ∈ C([ r1, r 2]) ∩ C1(( r1, r 2)), we may apply the mean value theorem to either interval ( r1, r 0) or ( r0, r 2) to deduce the existence of ξ ∈ (r1, r 2) such that g′(ξ) > 1. Set ξ2 = α(ψ2(ξ)) ∈ (0 , R ) and observe that 

g′(ξ) = ψ′ 

> 2(ξ)
> ψ′(ξ2)

> 1. Consequently, ψ2(ξ) = ψ(ξ2) and ψ′

> 2

(ξ) > ψ ′(ξ2) > 0, as desired. Direct computation verifies that the function ˜ φ from the statement of the lemma solves 

F ( ˜ φ, ˜φ′) = n(n − 1) csch 2

pn(n − 2) 2 R

!

and satisfies ˜ φ(0) = 0, ˜ φ(R) = 1 and ˜ φ′ > 0 in (0 , R ). The conclusion follows. 

> 2In fact, the work of Aronsson addressed a broader class of sup-norm minimisation problems and for rougher admissible functions.

27 We may now use the explicit minimiser above with the ideas from Lemma 3.1 to prove the following bounds on the first eigenvalue: 

Lemma 3.3. Let (M, g ) be a Riemannian manifold and suppose that there exist two open sets Ω1 ⊂ Ω2 with C1 boundary which satisfy (1.4) and that the scalar curvature satisfies 

Sg ≤ − n(n − 1) on Ω2. If (1.5) holds, then 

λ < n (n − 1) 

V ol g(Ω 2 \ Ω1) csch 2

√n(n−2) 2 R



− V ol g(Ω 1)

V ol g(Ω 2) ≤ 0. (3.7) 

On the other hand, if (1.5) does not hold, we have 

λ < n (n − 1) 

V ol g(Ω 2 \ Ω1) csch 2

√n(n−2) 2 R



− V ol g(Ω 1)

V ol g(Ω 1) . (3.8) 

Proof. Define φ to be the function of the form (3.3) where ˜ φ is taken to be the minimiser obtained in Lemma 3.2. Substituting φ in the integral in (3.2) and using (3.4) we obtain 

λ ≤ n(n − 1) 

V ol g(Ω 2 \ Ω1) csch 2

√n(n−2) 2 R



− V ol g(Ω 1)

∥φ∥L2(Ω 2)

. (3.9) If the inequality above were saturated, then φ (up to a harmless normalisation) would be a minimiser of (3.2) and hence would be smooth in Ω 2, contradicting the gradient discontinuity at the boundary ∂Ω1 observed using the explicit form for ˜ φ obtained in Lemma 3.2 and recalling (3.3). Consequently, inequality (3.9) above is, in fact, strict. In the case that (1.5) holds, the numerator in (3.9) is non-positive and so, using that 

∥φ∥L2(Ω 2) < V ol g(Ω 2), we obtain (3.7). Likewise, if (1.5) does not hold, the numerator is positive and we use that ∥φ∥L2(Ω 2) > V ol g(Ω 1) to obtain (3.8). We may now prove Theorem 1.3 as an immediate consequence of the lemma above: 

Proof of Theorem 1.3. Combined with assumption (1.1), the existence of a solution to the Yamabe problem now follows from [AM88b, Theorem C] provided that we can show that the first eigenvalue λ of the conformal Laplacian on Ω 2 is negative. This negativity is an immediate consequence of assumption (1.5) and estimate (3.7) from Lemma 3.3. We conclude the section with the following corollaries of Theorem 1.3 for geodesic balls and for annuli which will aid in our discussion regarding warped product and multiply warped product type manifolds in the next subsection. In particular, for geodesic balls we have: 28 Corollary 3.4. Let (M, g ) be a Riemannian manifold and suppose there exist constants 

α, R > 0 and some geodesic ball B(1+ α)R which satisfies 

V ol g(B(1+ α−1)R \ Bα−1R)

V ol g(Bα−1R) ≤ sinh 2 Rpn(n − 2) 2

!

(3.10) 

and on which the scalar curvature satisfies Sg ≤ − n(n − 1) . Then, the conformal Laplacian 

−cn∆g + Sg for (M, g ) has a negative first eigenvalue on B(1+ α−1)R.

In the case of multiply warped product metrics (see (3.14)), which have a radial fibre whose coordinate we denote by r, we fix some value r0 ∈ R and define the annular region 

AR(r0) = {x ∈ M : |r(x) − r0| ≤ R}. We may then obtain as a corollary of Theorem 1.3, 

Corollary 3.5. Let (M, g ) be a Riemannian manifold and suppose there exist constants 

α, R > 0 and some annulus A(1+ α)R(r0) which satisfies 

V ol g(A(1+ α−1)R(r0) \ Aα−1R(r0)) 

V ol g(Aα−1R(r0)) ≤ sinh 2 Rpn(n − 2) 2

!

(3.11) 

and on which the scalar curvature satisfies Sg ≤ − n(n − 1) . Then, the conformal Laplacian 

−cn∆g + Sg for (M, g ) has a negative first eigenvalue on A(1+ α−1)R(r0).

The proofs of the two corollaries follow directly from Theorem 1.3 with the appropriate choices made for Ω 1, Ω 2 and R.

## 3.2 Sharpness of the eigenvalue estimate 

In this section we demonstrate that the volume ratio condition (1.5) in Theorem 1.3 is sharp for the negativity of the first eigenvalue. In particular, we will show: 

Proposition 3.6. Let β > 0. There exists a constant C > 0, such that for any large R there is a complete, non-compact manifold (M, g ) and bounded domains Ω1 ⊂ Ω2 satisfying (1.4) 

with volume ratio V ol g(Ω 2 \ Ω1)

V ol g(Ω 1) < Ce βR (3.12) 

and with scalar curvature satisfying Sg ≤ − n(n − 1) on M for which the first eigenvalue for the conformal Laplacian on Ω2 satisfies 

λ > 

( 1(n−1)( n−2) β2 if β > n − 1, 

> n−1
> n−2

β2 − n(n − 1) if β ≤ n − 1. (3.13) 

In particular, if β > pn(n − 2) , then λ is positive. 

29 Note that, for large R, (3.12) implies (1.6) with a slightly larger β. Remark 1.4 follows. We consider the product manifolds M = R × N1 × . . . × Nm where m ≥ 1 and each Ni is a compact manifold of dimension ni ≥ 1 with P 

> i

ni = n − 1. We endow M with a (multiply) warped metric g of the form 

g = dr 2 + X

> i

p2 

> i

(r)hi (3.14) where pi : R → (0 , ∞) are warping functions and hi are metrics on each of the Ni. Acomputation shows that ( M, g ) has Laplacian ∆ g = ∂rr + P 

> i

nip′ 

> i
> pi

∂r + P

> i
> 1
> p2
> i

∆hi and 

Sg = −2 X

> i

ni

p′′ 

> i

pi

− X

> i

ni(ni − 1) 

p′

> i

pi

2

− 2 X

> i<j

ninj

p′

> i

p′

> j

pipj

+ X

> i

Shi

p2

> i

. (3.15) A particularly convenient family of warped product metrics for our purposes will be: 

Example 3.7. Let (M, g ) be a multiply warped product as in (3.14) with each Ni = S1 (so that m = n − 1) and pi = eαir for some αi ∈ R. We note that 

Sg = −2 X

> i

αi

!2

+ 2 X

> i<j

αiαj .

As a consequence, for any given β and constant C ≥ − nn−1 β2, there exists a choice of αi

such that β = P 

> i

αi and Sg ≡ − C. In particular, if |β| ≤ n − 1, then there exists a choice of αi with P 

> i

αi = β so that Sg ≡ − n(n − 1) .

We now turn to a study of the volume ratios of concentric balls in the example above. 

Lemma 3.8. Let (M, g ) be as in Example 3.7. Then there exists a constant C depending only on αi such that, for any R sufficiently large, one can find concentric balls B2R and BR

such that V ol g(B2R \ BR)

V ol g(BR) ≤ Ce βR .

Proof. Fixing some large R and taking some ball BR(p0), writing p0 = ( r0, x 0), we have immediately that 

BR(p0) ⊂ { p : |r(p) − r0| ≤ R}.

On the other hand, defining S0 := {r0} × Tn−1 we have that 

dg(p, p 0) ≤ dg(p, S 0) + diam( S0) = r(p) − r0 + er0 diam( Tn−1).

Consequently, writing A0 = er0 diam( Tn−1), we have that 

{| r − r0| ≤ R − A0} ⊂ BR(p0) ⊂ {| r − r0| ≤ R}

30 from which we obtain 

V ol g(B2R(p0)) ≤

Z

> Tn−1

Z r0+2 Rr0−2R

eβr dr dx = βV ol (Tn−1)  eβ(r0+2 R) − eβ(r0−2R)

and 

V ol g(BR(p0)) ≥

Z

> Tn−1

Z r0+( R−A0)

> r0−(R−A0)

eβr dr dx = βV ol (Tn−1)e−A0  eβ(r0+R) − eβ(r0−R+2 A0)

from which we may estimate 

V ol g(B2R \ BR)

V ol g(BR) ≤ eA0 eβ(r0+2 R) − eβ(r0−2R)

eβ(r0+R) − eβ(r0−R+2 A0) − 1.

Consequently, ( M, g ) satisfies the following bound on the volume ratio for large balls 

V ol g(B2R \ BR)

V ol g(BR) ≤ Ce βR  1 + O(e−2( n−1) R) − 1 (3.16) and so, taking R large, we obtain 

V ol g(B2R \ BR)

V ol g(BR) ≤ Ce βR .

for some large constant C > 0 depending only on αi.We are now ready to prove Proposition 3.6. However, before this, we make the following remark: 

Remark 3.9. As a consequence of Lemma 3.8, we may use Corollary 3.5 of Theorem 1.3 to prove that any manifold of the form of Example 3.7 admits a solution to the Yamabe problem, provided that β < pn(n − 2) .Proof of Proposition 3.6. Let ( M, g ) be of the form of Example 3.7 where αi are chosen such that P 

> i

αi = β and 

Sg ≡

(

− nn−1 β2 if β > n − 1,

−n(n − 1) if β ≤ n − 1.

In particular, Sg ≤ − n(n − 1). We note that, by the same argument as in the proof of Lemma 3.8, there exists a C(α1, . . . , α n−1) > 0 such that we may choose concentric annuli Ω2 = A2R and Ω 1 = AR satisfying 

V ol g(A2R \ AR)

V ol g(AR) ≤ C(α1, . . . , α n−1)eβR .

31 As the eigenspace corresponding to the first eigenvalue λ is necessarily one dimensional, we must have that the first eigenfunctions φ of the conformal Laplacian on A2R are radially symmetric (i.e. φ = φ(r)) by virtue of the symmetry of the torus. Consequently, φ satisfies the constant coefficient ODE 

φ′′ + βφ ′ + λ − Sg

cn

φ = 0 on Ω 2 subjected to the zero Dirichlet boundary condition. It follows that the corresponding characteristic equation must have complex, non-real roots, which implies that 

β2 − (n − 2)( λ − Sg)(n − 1) < 0.

Consequently, λ > n−1 

> n−2

β2 − Sg and so, recalling our choice of Sg, the proposition follows. To conclude, we remark that one may use Theorem 1.3 to show existence of solutions to the Yamabe problem for manifolds obtained from the warped product type metrics discussed above via perturbations which preserve the volume ratio and scalar curvature conditions. In a future work, it would be interesting to explore which results similar to those achieved for ALH manifolds could be obtained in the setting of Theorem 1.3 and to understand to what extent the upper bound on the scalar curvature could be loosened. 

# References 

[ACF92] L. Andersson, P. T. Chru´ sciel, and H. Friedrich. On the regularity of solutions to the Yamabe equation and the existence of smooth hyperboloidal initial data for Einstein’s field equations. Comm. Math. Phys. , 149(3):587–612, 1992. [AILA18] P. T. Allen, J. Isenberg, J. M. Lee, and I. Stavrov Allen. Weakly asymptotically hyperbolic manifolds. Comm. Anal. Geom. , 26(1):1–61, 2018. [AM85] P. Aviles and R. C. McOwen. Conformal deformations of complete manifolds with negative curvature. J. Differential Geom. , 21(2):269–281, 1985. [AM88a] P. Aviles and R. C. McOwen. Complete conformal metrics with negative scalar curvature in compact Riemannian manifolds. Duke Math. J. , 56(2):395–398, 1988. [AM88b] P. Aviles and R. C. McOwen. Conformal deformation to constant negative scalar curvature on noncompact Riemannian manifolds. J. Differential Geom. ,27(2):225–239, 1988. 32 [Aro65] G. Aronsson. Minimization problems for the functional sup x F (x, f (x), f ′(x)). 