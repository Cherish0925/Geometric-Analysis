---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Seiberg–Witten Invariants and Pseudo-Holomorphic Subvarieties for Self-Dual, Harmonic 2–Forms]

precludes only the use of the proofs in [15] of statements which actually refer to this integral.) 

# 6 Large r behavior away from α−1(0) 

Fix a Spin C structure for X and then consider a solution ( A, ψ ) to (2.9) for the given Spin C structure and for some large value of r. The purpose of this section is to investigate the behavior of ( A, ψ ) to (2.9) at points which lie neither on 

Z nor on α−1(0). Here are the basic observations: First, 2 −1/2|ω| − | α|2 and 

|β| are both O(r−1). In particular, this means that FA is bounded. More to 

> Clifford Henry Taubes Geometry and Topology, Volume 3 (1999)
> 198

the point, the connection A is close to a canonical connection A0 whose gauge orbit depends only on the metric and the choice of ω . (Note that this orbit is independent of the chosen Spin C structure.) Proposition 6.1, below, gives the precise measure of closeness that is used here. The statement of Proposition 6.1 requires a preliminary, three part digression whose purpose is to define the connection A0 . The first part of the digression remarks that the −√2i|ω| eigenspace of the Clifford multiplication endomor-phism by c+(ω) on S+ defines a complex line bundle E → X − Z . The com-ponent α of ψ is a section of E , and then the component β is one of K −1E .Here, K −1 is the inverse of the canonical bundle, K , for the almost complex structure J ≡ √2g−1ω/ |ω| on X − Z .Note that the line bundle L = det( S+) restricts to X − Z as 

L|X−Z ≈ K −1E2. (6.1) Meanwhile, α trivializes E where α 6 = 0 and so the unit length section α2/|α|2

of E2 provides an isometric identification of L with K −1 on the complement of Z and α−1(0). The second part of the digression reviews the definition from [18] or Section 1c of [15] of a canonical connection on the line bundle K−1 → X − Z . (Note that this connection is unique up to gauge equivalence.) To define a canonical connection, first remark that there is a canonical Spin C structure for X − Z so that the −√2i|ω| eigenbundle for the c+(ω) action on the corresponding S+

is the trivial bundle over X − Z . For this Spin C structure, the corresponding line bundle L is isomorphic to K −1 . With this understood, there is a unique connection (up to isomorphism) on K −1 for which the induced connection on the aforementioned −√2i|ω| eigenbundle is trivial. Such a connection is a canonical one. Part 3 of the digression defines a canonical connection on L|X−Z by using the identification α2/|α|2 between L and K −1 (where α 6 = 0 on X − Z ) to pull a canonical connection on K −1 back to L.End the digression. 

Proposition 6.1 Fix a Spin C structure for X and δ > 0. There is a constant 

ζδ ≥ 1 with the following significance: Suppose that r ≥ ζδ and that (A, ψ )

are a solution to (2.9) as defined by r and the given Spin C structure. There is a canonical connection A0 on L|X−Z for which |A − A0| + |FA − FA0| ≤ 

ζδr−1 + ζδr exp[ −√r dist( x, α −1(0)) /ζ δ] at all points x ∈ X with distance δ or more from Z and distance r−1/2 or more from α−1(0) .

> Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties Geometry and Topology, Volume 3 (1999)
> 199

(This proposition should be compared with Proposition 4 .4 in [15].) 

Proof of Proposition 6.1 Away from Z and where α 6 = 0, the section 

α/ |α| defines a trivialization of the line bundle E , and with this understood, the difference between A and a particular canonical connection A0 is given by 2(¯ α/ |α|)∇A(α/ |α|). Thus, the absolute value of ∇A(α/ |α|) measures the size of A − A0 . Likewise, the norm of dA∇A(α/ |α|) measures the size of FA − FA0 .With the task ahead now clear, note that the arguments which establish the required bounds on the derivatives of α are, for the most part, straightforward modifications of the arguments which prove Proposition 4 .4 in [15]. In partic-ular, the reader will be referred to the latter reference at numerous points. In any event, the details are given in the subsequent four steps. 

Step 1 A straightfoward modification of the proof of Proposition 4 .4 in [15] (which is left to the reader) proves the following preliminary estimate: 

Lemma 6.1 Fix a Spin C structure for X and fix δ > 0. There is a constant 

ζδ with the following significance: Let (A, ψ ) solve the version of (2.9) which is defined by the given Spin C structure and by r ≥ ζδ . If x ∈ X has distance δ

or more from Z , then 

r|(2 −1/2|ω| − | α|2)|7 + r2|β|2 + |∇ Aα|2 + r|∇ Aβ|2

≤ ζδ(1 + r exp[ −√r dist (x, α −1(0)) /ζ δ]) . (6.2) 

Step 2 Now, introduce α ≡ 21/4|ω|−1/2α. Add the two lines of (3.53) to obtain a differential inequality for the function y ≡ |∇ Aα|2 + |∇ Aβ|2 . Use Lemma 6.1 to bound |w| to find that the aforementioned inequality implies that 2 −1d∗dy + 4 −1rζ −1 

> δ

y ≤ ζδr−1 at points with distance δ or more to Z and distance ζδr−1/2 or more to α−1(0). Note that (6.3) implies that y′ ≡ y−4ζ 2 

> δ

r−2

obeys the inequality 2−1d∗dy ′ + 4 −1rζ −1 

> δ

y′ ≤ 0. (6.3) at points with distance δ or more to Z and ζδr−1/2 or more to α−1(0). Given (6.3), a straightforward modification of the proof of Proposition 4 .4 in [15] yields the bound 

|∇ Aα|2 + |∇ Aβ|2 ≤ ζδr−2 + ζδr exp( −√r dist( ·, α −1(0)) /ζ δ) (6.4) at points with distance 2 δ or more from Z . (Bounds on the size of both |∇ Aα|2

and |∇ Aβ|2 near α−1(0) come via Proposition 3.3.) 

> Clifford Henry Taubes Geometry and Topology, Volume 3 (1999)
> 200

Take the δ/ 2 version of (6.4) with the fact that α/ |α| = α/ |α| to bound the difference between A and a canonical connection on L by 

ζδ(r−1 + r1/2 exp( −√r dist( ·, α −1(0)) /ζ δ)) at points with distance δ or more from Z and r−1/2 or more from α−1(0). 

Step 3 As remarked above, a bound on |∇ 2

> A

α| provides a bound on |FA−FA0|.To obtain the latter, first differentiate (3.55) and commute covariant derivatives to obtain an equation for ∇2

> A

α of the form ∇∗

> A

∇A(∇2

> A

α)+(4 √2) −1r|ω|(∇2

> A

α)+ Remainder = 0. Take the inner product of this last equation with ∇2

> A

α to obtain an equation for |∇ 2

> A

α|2 having the form 2 −1d∗d|∇ 2

> A

α|2+4 −1r|ω||∇ 2

> A

α|2+

|∇ A(∇2

> A

α)|2 + 〈∇ 2

> A

α, Remainder 〉 = 0. Here, 〈 , 〉 denotes the Hermitian inner product on E ⊗ (⊗2T ∗X). A similar equation for |∇ 2

> A

β| is obtained by differentiating (3.56). Add the resulting two equations. Then, judicious use Lemma 6.1, (6.5) and the triangle inequality produces a differential inequality for y′ ≡ |∇ 2

> A

α|2 + |∇ 2

> A

β|2 − ζδr−2 which has the same form as (6.3). And, with this understood, the arguments which yield (6.4) yield the bound 

y′ ≤ ζδr−2 + ζδ(sup 

> σ≥δ

|y′|) exp( −√r dist( ·, α −1(0)) /ζ δ) (6.5) at points where σ ≥ 2δ .

Step 4 The δ/ 2 version of (6.5) with a bound on |∇ 2

> A

α|2 + |∇ 2

> A

β|2 where 

σ ≥ δ/ 2 by ζδr2 gives Proposition 6.1’s bound on |FA − FA0|. Thus, the last task is to obtain a supremum bound on |∇ 2

> A

α|2 + |∇ 2

> A

β|2 .For this purpose, fix a ball of radius 2 r−1/2 whose points all have distance δ/ 4or more from Z . Take Gaussian coordinates based at the center of this ball and rescale so that the radius r−1/2 concentric ball becomes the radius 1 ball in R4

with center at the origin. Equation (2.9) rescales to give an r = 1 version of the same equation on the radius 2 ball in R4 with a metric g′ which is close to the Euclidean metric gE and form ω′ which is close a constant self dual form of size |ω(x)|. Here, x is the center of the chosen ball in X . To be precise, 

|g′ − gE| ≤ ζr −1 and the derivatives of g′ of order k ≥ 2 are O(r−k/ 2) in size. Meanwhile the form ω′ differs by O(r−1/2) from a constant form, and its k -th derivatives are O(r−k/ 2) in size. With the preceding understood, standard elliptic regularity results (as in Chap-ter 6 of [12]) bound the second derivatives of the rescaled versions of α and β by 

ζδ . Rescaling the latter bounds back to the original size gives |∇ 2

> A

α|2+|∇ 2

> A

β|2 ≤

ζδr2 as required. 

> Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties Geometry and Topology, Volume 3 (1999)

201 7 Proof of Theorem 2.2 

Fix a Spin C structure for X and suppose that there exists an unbounded, increasing sequence {rn} of positive numbers with the property that each r = rn

version of (2.9) with the given Spin C structure has a solution ( An, ψ n). The purpose of this section is to investigate the n → ∞ limits of α−1 

> n

(0) and in doing so, prove the claims of Theorem 2.2. This investigation is broken into six parts. 

a) The curvature as a current 

Each connection An has its associated curvature 2–form, and the difference between An ’s curvature 2–form and the curvature 2–form of the canonical con-nection on K −1 will be viewed as a current on X . This current, Fn , associates to a smooth 2–form μ the number 

Fn(μ) ≡ 2−1

∫

> X

i

2π (FAn − FA0) ∧ μ. (7.1) Here, FA0 is the curvature 2–form of the canonical connection on K−1 . (Even though the canonical connection on K −1 is defined only over X − Z (see the beginning of the previous section), the norm of its curvature is none-the-less integrable over X . Thus, (7.1) makes sense even for μ whose support intersects 

Z . The integrability of |FA0| follows from the bound |FA0| ≤ ζ dist( ·, Z )−2 .) With the sequence {F n} understood, fix δ > 0 and suppose that each point in the support of μ has distance δ or more from Z . It then follows from Lemma 3.1 and Proposition 4.2 that 

|F n(μ)| ≤ ζδ sup 

> X

|μ|. (7.2) This uniform bound implies that the sequence {F n} defines a bounded sequence of linear functional on the space of smooth 2–forms on X with support where the distance to Z is at least δ .With the preceding understood, a standard weak convergence argument finds a subsequence of {F n} (hence renumbered consecutively) which converges in the following sense: Let μ be a smooth 2–form with compact support on X − Z

and then lim n→∞ Fn(μ) exists. Moreover, this limit, 

F(·) ≡ lim  

> n→∞

Fn(·), (7.3) defines a bounded linear functional when restricted to forms whose support has distance from Z which is bounded from below by any fixed positive number. 

> Clifford Henry Taubes Geometry and Topology, Volume 3 (1999)
> 202

Note that the current F is integral in the following sense: Let μ be a closed 2– form with compact support on X−Z and with integral periods on H2(X−Z; Z). Then 

F(μ) ∈ Z. (7.4) 

b) The support of F

This part of the discussion considers the support of the current F . Here is the crucial lemma: 

Lemma 7.1 There is a closed subspace C ⊂ X − Z with the following prop-erties: 

• F(μ) = 0 when μ is a 2–form on X with compact support in (X −Z)−C .

• Conversely, let B ⊂ X − Z be an open set which intersects C . Then there is a 2–form μ with compact support in B and with F(μ) 6 = 0 .

• Fix δ > 0. Then the set of points in C with distance at least δ from Z

has finite 2–dimensional Hausdorff measure. 

• Conversely, let δ > 0 and there is a constant ζδ ≥ 1 with the following significance: Let ρ ∈ (0 , ζ −1 

> δ

) and let B ⊂ X be a ball of radius ρ and center on Z whose points have distance δ or more from Z . Then the 

2–dimensional Hausdorff measure of B ∩ C is greater than ζ −1 

> δ

ρ2 .

• There is a subsequence of (An, ψ n) such that the corresponding sequence 

{α−1 

> n

(0) } converges to C in the following sense: For any δ > 0, the following limit exists and is zero: 

lim 

> n→∞

[ sup  

> {x∈C:dist (x,Z )≥δ}

dist( x, α −1 

> n

(0)) + sup   

> {x∈α−1
> n(0): dist (x,Z )≥δ}

dist( x, C ))] .

(7.5) 

Proof of Lemma 7.1 To construct C , consider first a large positive integer 

N and a very large positive integer n. (Here, a lower bound on n comes from the choice of N .) Use Lemma 4.1 to find a set Λ ′

> n

(N ) of balls of radius 16 −N

with the following properties: The balls are disjoint, their centers lie on α−1 

> n

(0) and have distance at least 4 · 16 −N from Z , and the set Λ n(N ) of concentric balls of radius 2 · 16 −N covers the set of point in α−1 

> n

(0) with distance 8 · 16 −N

from Z . According to Lemma 4.1, when n is sufficiently large, this set Λ n(N )has a bound on the number of its elements which is independent of n. Let ν(N )be an integer which is greater than the number of elements in each Λ n(N ). 

> Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties Geometry and Topology, Volume 3 (1999)
> 203

Label the centers of the balls in Λ n(N ) and then add the final point some num-ber of times (if necessary) to make a point xn(N ) ≡ (xn(1; N ), . . . , x n(ν(N ); N )) 

∈ × ν(N )X . By a diagonalization process, one can find an infinite sequence of in-dices n (hence relabeled consecutively from 1) so that for each N , the sequence 

{xn(N )}n≥1 converges in ×ν(N )X .For each N , let x(N ) ≡ {x(1 , N ), . . . , x (ν(N ), N )} denote the limit of 

{xn(N )}n≥1 . One can think of x(N ) as either a point in ×ν(N )X , or else an ordered set of ν(N ) points in X . Think of x(N ) in the latter sense, and let 

U (N ) denote the union of the balls of radius 4 · 16 −N with centers at the points 

x(N ) (that is, at {x(i, N )}1≤i≤ν(N ) ). Lemma 5 .1 of [15] argues that these sets are nested in that U (N + 1) ⊂ U (N ). With this understood, set 

C ≡ ⋂ 

> N≥1

U (N ). (7.6) The argument for the asserted properties of C is essentially the same as that for Lemma 5 .2 in Section 5c of [15]. In this regard, Lemma 4.1 here replaces Lemma 3 .6 in [15], and Proposition 4.2 here replaces Proposition 4 .4 in [15]. The details are straightforward and left to the reader. 

c) A positive cohomology assignment 

The purpose of this subsection is to give a more precise characterization of the distribution F .To begin, note that the construction of C indicated above can be used (as in the proof of Lemma 5 .3 in [15]) to prove that the current F is type 1−1 in the sense that F(μ) = 0 when μ is a section of the subbundle K −1 ⊂ Λ+ . The fact that F is type 1 −1 is implied by Lemma 7.2 below which is a significantly stronger assertion: 

Lemma 7.2 Let D ⊂ C denote the standard, unit disc, and let σ : D → X −Z

be a smooth map which extends to the closure, D, of D as a continuous map that sends ∂D into X − C . Then, {2−1 ∫ 

> D

σ∗ ( i 

> 2π

(FAn − FA0))}  

> n≥1

converges, and the limit, I(σ) ∈ Z. Moreover, 

• I(σ) = 0 if σ(D) ∩ C = ∅.

• I(σ) > 0 if σ is a pseudo-holomorphic map and σ−1(C) 6 = ∅. (7.7) 

Proof of Lemma 7.2 The arguments which prove Lemma 6 .2 in [15] are of a local character and so can be brought to bear directly to give Lemma 7.2. 

> Clifford Henry Taubes Geometry and Topology, Volume 3 (1999)
> 204

The discussion surrounding Lemma 6 .2 in [15] concerns the notion of a positive cohomology assignment for C . The latter is defined as follows: First, let D ⊂ C

be the standard unit disk again. A map σ : D → X − Z is called admissible 

when σ extends as a continuous map to the closure, D , of D which maps ∂D 

into X − C . A positive cohomology assignment specifies an integer, I(σ), for each admissible map σ from D to X − Z subject to the following constraints: 

• If σ(D) ⊂ X − C , then I(σ) = 0. 

• A homotopy h : [0 , 1] × D → X is called admissible when it extends as a continuous map from [0 , 1] × D into X that sends [0 , 1] × ∂D to X − C .If h is an admissible homotopy, then I(h(1 , ·)) = I(h(0 , ·)). 

• Let σ : D → X be admissible and suppose that θ : D → D is a proper, degree k map. Then I(σ · θ) = kI (σ). 

• Suppose that σ : D → X is admissible and that σ−1(C) is contained in a disjoint union ∪νDν ⊂ D, where each Dν = θν(D) with θν : D → D

being an orientation preserving embedding. Then I(σ) = ∑ 

> ν

I(σ · θν). 

• If σ is admissible and pseudo-holomorphic with σ−1(C) 6 = ∅, then I(σ) >

0. (7.8) The next result follows from Lemma 7.2 and the particulars of the definition of 

F in (7.3) as a limit. 

Lemma 7.3 Let C be as in Lemma 7.1 and let I(·) be as described in Lemma 7.2. Then I(·) defines a positive cohomology assignment for C .

Proof of Lemma 7.3 Use the proof of Lemma 6 .2 in [15]. 

d) C as a pseudo-holomorphic submanifold 

Proposition 6 .1 in [15] asserts that a closed set in a compact, symplectic 4– manifold with finite 2–dimensional Hausdorff measure and a positive coho-mology assignment is the image of a compact, complex curve by a pseudo-holomorphic map. (Note, however that the proof of Proposition 6 .1 in [15] has errors which occur in Section 6e of [15], and so the reader is referred to the revised proof in the version which is reprinted in [20].) It is important to realize that the assumed compactness of X in the statement of Proposition 6 .1of [15] is present only to insure that the complex curve in question is compact. In particular, the proof of Proposition 6 .1 in [15] from the reprinted version in [20] yields: 

> Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties Geometry and Topology, Volume 3 (1999)
> 205

Proposition 7.1 Let Y be a 4–dimensional symplectic manifold with com-patible almost complex structure. Suppose that C ⊂ Y is a closed subset with the following properties: 

• The restriction of C to any open Y ′ ⊂ Y with compact closure has finite 

2–dimensional Hausdorff measure. 

• C has a positive cohomology assignment. Then the following are true: 

• There is a smooth, complex curve C 0 (not necessarily compact) with a proper, pseudo-holomorphic map f : C 0 → Y with C = f (C 0).

• There is a countable set Λ0 ⊂ C 0 with no accumulation points such that 

f embeds each component C 0 − Λ0 .

• Here is an alternate description of the cohomology assignment for C :Let σ : D → Y be an admissible map, and let σ′ be any admissible perturbation of σ which is transverse to f and which is homotopic to σ

via an admissible homotopy. Construct the fibered product T ≡ { (x, y ) ∈

D × C1 : σ′(x) = ϕ(y)}. This T is a compact, oriented 0–manifold, so a finite set of signed points; and the cohomology assignment gives σ the sum of the signs of the points of T .

Proof of Proposition 7.1 As remarked at the outset, the proof of Proposition 6.1 in [15] from the revised version in [20] can be brought to bear here with negligible modifications. Lemma 7.3 enables Proposition 7.1 to be applied to the set C from Lemma 7.1. In particular, one can conclude that C is the image of a smooth, complex curve 

C 0 via a proper, pseudo-holomorphic 

f : C 0 → X − Z. (7.9) Moreover, f can be taken to be an embedding upon restriction to each compo-nent of the complement in C 0 of a countable set with no accumulation points. In particular, it follows that C restricts to any open subset with compact closure in X − Z as a pseudo-holomorphic subvariety. 

e) The energy of C

The purpose of this subsection is to state and prove 

> Clifford Henry Taubes Geometry and Topology, Volume 3 (1999)
> 206

Lemma 7.4 The set C from Lemma 7.1 is a finite energy, pseudo-holomorphic subvariety in the sense of Definition 1.1. Furthermore, there are universal constants ζ1, ζ 2 (independent of the metric) such that 

∫

> C

ω ≤ ζ1eω(s) + ζ2

∫

> X

(|Rg| + |W + 

> g

|)|ω|dvol g. (7.10) 

In this equation, eω(s) equals the evaluation on the fundamental class of X of the cup product of c1(L) with [ω]. Meanwhile, Rg is the scalar curvature for the metric g , and W + 

> g

is the metric’s self-dual, Weyl curvature. Also, dvol g is the metric’s volume form. 

Proof of Lemma 7.4 First of all, define an equivalence relation on the com-ponents of C 0 (from (7.9)) by declaring two components to be equivalent if their images via f coincide. The quotient by this equivalence relation defines another smooth, complex curve, C0 , together with a proper, pseudo-holomorphic map 

ϕ : C0 → X − Z whose image is C . Moreover, there is a countable set Λ 0 ⊂ C0

which has no accumulation points and whose complement is embedded by ϕ.With the preceding understood, it remains only to establish that C has finite energy. For this purpose, fix δ > 0 and re-introduce the bump function χδ .(Remember that χδ vanishes where the distance to Z is greater than 2 δ , and it equals 1 where the distance to Z is less than δ .) Since ω restricts to C as a positive form, it follows that C has finite energy if and only if lim 

> δ→0

∫

> C

(1 − χδ)ω (7.11) exists, and this limit exists if and only if the set {∫ 

> C

(1 − χδ)ω} 

> δ> 0

is bounded in [0 , ∞). Thus, the task is to find a δ –independent upper bound for this set. With the preceding understood, remark first that Proposition 7.1 as applied to 

C yields ∫

> C

(1 − χδ)ω ≤

∫

> C0

f ∗((1 − χδ)ω) = F((1 − χδ)ω). (7.12) Now, given ε > 0, the right-hand expression in (7.12) is no greater than 

Fn((1 − χδ)ω) + ε (7.13) when n is sufficiently large. Moreover, as Fn is defined on all smooth forms, the first term in (7.13) is equal to (4 π)−1

∫

> X

(1 − χδ)iF A ∧ ω − (4 π)−1

∫

> X

(1 − χδ)iF A0 ∧ ω. (7.14) 

> Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties Geometry and Topology, Volume 3 (1999)
> 207

with A = An .Both terms in (7.14) are δ dependent and so must be analyzed further. In particular, Lemma 7.4 follows with the exhibition of a bound on these terms by ζ(eω(s) + ∫ 

> X

(|Rg| + |W + 

> g

|)|ω|dvol g .For the right most term, remark that only F + 

> A0

appears in (7.14) (since ω is self dual), and a calculation (which is left to the reader) finds a universal constant 

ζ with the property that 

|F + 

> A0

| ≤ ζ(|∇ ω|2 + |Rg| + |W + 

> g

|). (7.15) Here, ω ≡ ω/ |ω|. Equation (7.15) implies that the right most term in (7.14) is not greater than 

ζ

(∫ 

> X

|ω||∇ ω|2 +

∫

> X

(|Rg| + |W + 

> g

|)|ω|dvol g

)

. (7.16) Here the constant ζ is also metric independent. Meanwhile, the first integral in (7.16) is bounded by ζ ∫

> X

(|Rg|+|W + 

> g

|)|ω|dvol g which can be seen by integrating both sides of (3.7) and then integrating by parts to eliminate the d∗d|ω| term. This means in particular that the right most term in (7.16) is bounded by a universal multiple of ∫

> X

(|Rg| + |W + 

> g

|)|ω|dvol g .Now consider the left most term in (7.14). For this purpose, use (2.9) to identify the latter with (8 √2π)−1r

∫

> X

(1 − χδ)|ω|(2 −1/2|ω| − | α|2 + |β|2). (7.17) One should compare this expression for that implied by (2.9) for eω(s), namely 2−1eω(s) = (8 √2π)−1r

∫

> X

|ω|(2 −1/2|ω| − | α|2 + |β|2). (7.18) In particular, note that (7.18) implies the identity (8 √2π)−1r

∫

> X

|ω|| β|2 = 4 −1eω(s) − (16 √2π)−1r

∫

> X

|ω|(2 −1/2|ω| − | ψ|2).

(7.19) It then follows from the second line of (3.2) (and the integration of (3.7)) that (8 √2π)−1r

∫

> X

|ω|| β|2 = ζ

(

eω(s) + 

∫

> X

(|Rg| + |W + 

> g

|)|ω|dvol g

)

. (7.20) This last bound can now be plugged back into bounding (7.17) since the ex-pression in (7.17) is no greater than (8 √2π)−1

(

r

∫

> X

χδ|ω|| (2 −1/2|ω| − | ψ|2)| + 2 r

∫

> X

|ω|| β|2

)

. (7.21) 

> Clifford Henry Taubes Geometry and Topology, Volume 3 (1999)

208 Thus, (7.20) and the second line of (3.2) bound the left most term in (7.14) by the required ζ (eω(s) + ∫ 

> X

(|Rg| + |W + 

> g

|)|ω|dvol g

).

f ) Intersections with the linking 2–spheres 

After Lemma 7.4, all that remains to prove Theorem 2.2 is to establish that Lemma 7.4’s pseudo-holomorphic subvariety C has intersection number equal to 1 with any 2–sphere in X − Z which has linking number 1 with Z .To prove this last assertion, consider that each αn defines a section of the bundle E whose square is given in (6.1) as L|X−ZK . Now, L is trivial over a linking 2–sphere for Z as L is a bundle over the whole of X . This means that 

E restricts to a linking 2–sphere of Z as the square root of the restriction of K .Moreover, according to Lemma 2.1, the restriction of K to a linking 2–sphere has degree 2, so E restricts to such a 2–sphere with degree 1. This means that the current Fn in (7.1) evaluates as 1 on any closed form which represents the Thom class of a fixed, linking 2–sphere. In particular, the same must be true for a limit current F , and the nature of the convergence in Proposition 7.1 implies that C has intersection number 1 with such a 2–sphere. 

Achnowledgement This research was supported in part by the National Science Foundation. 

# References 

[1] M F Atiyah , I Singer , N J Hitchin , Self-duality in 4–dimensional Rieman-nian geometry , Proc. Roy. Soc. London Ser. A, 362 (1978) 425–461 [2] S K Donaldson , Symplectic submanifolds and almost complex geometry , Jour. Diff. Geom. 44 (1996) 666–705 [3] D S Freed , K K Uhlenbeck , Instantons and Four–Manifolds , Springer–Verlag (1984) [4] M Gromov , Pseudo-holomorphic curves in symplectic manifolds , Invent. Math. 82 (1985) 307–347 [5] K Honda , Harmonic forms for generic metrics , preprint (1997) [6] M Hutchings , Y-J Lee , Circle-valued Morse theory, R–torsion and Seiberg– Witten invariants of 3–manifolds , Topology, to appear [7] M Hutchings , Y-J Lee , Circle-valued Morse theory and Reidemeister torsion ,preprint (1997) [8] D Kotschick , P B Kronheimer , T S Mrowka , in preparation 

> Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties Geometry and Topology, Volume 3 (1999)

209 [9] C LeBrun , Yamabe constants and the perturbed Seiberg–Witten equations ,Commun. Anal. Geom. 5 (1997) 535-553 [10] D McDuff , D Salamon , J –Holomorphic Curves and Quantum Cohomology ,American Mathematical Society, Providence (1996) [11] J M Morgan , The Seiberg–Witten Equations and Applications to the Topology of Smooth 4–Manifolds , Mathematical Notes, 44, Princeton University Press (1996) [12] C B Morrey , Multiple Integrals in the Calculus of Variations , Springer–Verlag (1966) [13] P Pansu , Pseudo-holomorphic curves in symplectic manifolds , from: “Holo-morphic Curves in Symplectic Geometry”, (M Audin and F Lafontaine, editors) Progress in Math. 117, Birkh¨ auser (1994) 233–250 [14] T Parker , J Wolfson , Pseudo-holomorphic maps and bubble trees , J. Geom. Anal. 3 (1993) 63–98 [15] C H Taubes , SW ⇒ Gr : From the Seiberg–Witten equations to pseudo-holomorphic curves , J. Amer. Math. Soc. 9 (1996) 845–918 [16] C H Taubes , The structure of pseudo-holomorphic subvarieties for a degener-ate almost complex structure and symplectic form on S1 × B3 , Geometry and Topology, 2 (1998) 221–332 [17] C H Taubes , The geometry of the Seiberg–Witten invariants , from: “Surveys in Differential Geometry, 1996”, (S T Yau, editor) International Press, to appear [18] C H Taubes , The Seiberg–Witten and the Gromov invariants , Math. Res. Let-ters 2 (1995) 221–238. [19] C H Taubes , SW = Gr : Counting curves and connections , preprint (1997) [20] C H Taubes , SW ⇒ Gr : From the Seiberg–Witten equations to pseudo-holomorphic curves , from: “Proceedings of the First IP Lecture Series, Vol. II”, (R Wentworth, editor), International Press, to appear [21] V Turaev , A combinatorial formula for the Seiberg–Witten invariants of 3-manifolds , preprint (1998) [22] R Ye , Gromov’s compactness theorem for pseudo-holomorphic curves , Trans. Amer. Math. Soc. 342 (1994) 671–694 [23] E Witten , Monopoles and 4–manifolds , Math. Res. Letters, 1 (1994) 769–796 

> Clifford Henry Taubes Geometry and Topology, Volume 3 (1999)

210


## Native file acquisition

```json
[
  {
    "url": "https://msp.org/gt/1999/3-1/gt-v3-n1-p08-p.pdf",
    "final_url": "https://msp.org/gt/1999/3-1/gt-v3-n1-p08-p.pdf",
    "name": "gt-v3-n1-p08-p.pdf",
    "size": 334045,
    "role": "primary_object_file",
    "status": "downloaded",
    "checksum": "sha256:2e2e4cf87a44b3da85ffbfc6c49d85f52252a0cc12b4a5a46bd2f5df6caa369d",
    "identity_bound": true,
    "parent_url": "https://msp.org/gt/1999/3-1/gt-v3-n1-p08-p.pdf",
    "primary_label": false,
    "download_eligible": true,
    "label": ""
  }
]
```
