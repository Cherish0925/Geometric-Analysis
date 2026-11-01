---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Higher order obstructions to the desingularization of Einstein metrics]

# Higher order obstructions to the desingularization of Einstein metrics

> Source: https://projecteuclid.org/journalArticle/Download?urlid=10.4310%2FCJM.2021.v9.n4.a2
> Fetched: 2026-10-10 20:33
> Method: FULLTEXT_HTML_JINA|FETCHERS=JINA,FIRECRAWL,BRIGHTDATA

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
  "source_url": "https://projecteuclid.org/journalArticle/Download?urlid=10.4310%2FCJM.2021.v9.n4.a2",
  "metadata": {
    "provenance_urls": [
      "https://projecteuclid.org/journalArticle/Download?urlid=10.4310%2FCJM.2021.v9.n4.a2"
    ],
    "search_origins": [
      {
        "source": "serper",
        "query": "Ozuch desingularization Einstein metrics obstruction map period parameters"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

Tristan Ozuch We find new obstructions to the desingularization of compact Ein-stein orbifolds by smooth Einstein metrics. These new obstructions, specific to the compact situation, raise the question of whether a compact Einstein 4-orbifold which is limit of Einstein metrics bubbling out Eguchi-Hanson metrics has to be K ̈ahler. We then test these obstructions to discuss if it is possible to ...

## Retrieved source content

Title: Download

URL Source: https://projecteuclid.org/journalArticle/Download?urlid=10.4310/CJM.2021.v9.n4.a2

Number of Pages: 76

Markdown Content:
> Cambridge Journal of Mathematics
> Volume 9, Number 4, 901–976, 2021

# Higher order obstructions to the desingularization of Einstein metrics ∗

Tristan Ozuch 

We find new obstructions to the desingularization of compact Ein-stein orbifolds by smooth Einstein metrics. These new obstructions, specific to the compact situation, raise the question of whether a compact Einstein 4-orbifold which is limit of Einstein metrics bubbling out Eguchi-Hanson metrics has to be K¨ ahler. We then test these obstructions to discuss if it is possible to produce a Ricci-flat but not K¨ ahler metric by the most promising desingu-larization configuration proposed by Page in 1981. We identify 84 obstructions which, once compared to the 57 degrees of freedom, indicate that almost all flat orbifold metrics on T4/Z2 should not be limit of Ricci-flat metrics with generic holonomy while bubbling out Eguchi-Hanson metrics. Perhaps surprisingly, in the most sym-metric situation, we also identify a 14-dimensional family of desin-gularizations satisfying all of our 84 obstructions. 

Keywords and phrases: Einstein 4-manifolds, desingularization, re-duced holonomy. 

Introduction 

An Einstein metric g satisfies, for some real number Λ, the equation Ric( g) = Λ g.

In dimension 4, they are considered optimal due to the homogeneity of their Ricci curvature but also as critical points of the Einstein-Hilbert functional with fixed volume, g  → ∫ 

> M

Rg dvol g, and more importantly as minimizers of the L2-norm of the Riemann curvature tensor, g  → ∫ 

> M

| Rm g |2dvol g.From dimension 4, even under natural assumptions of bounded diame-ter (compactness) and lower bound on the volume (non-collapsing) Einstein 

> ∗

The author would like to thank his PhD advisor, Olivier Biquard for his help and interest in the early stages of this project. 901 902 Tristan Ozuch metrics can develop singularities. One major goal for 4-dimensional geom-etry is therefore to understand the compactification of the moduli space of Einstein metrics on a differentiable manifold M 4 defined as (1) E(M 4) := {(M 4, g) | ∃ Λ ∈ R, Ric( g) = Λ g, Vol( M 4, g) = 1 } /D(M 4)where D(M 4) is the group of diffeomorphisms of M 4 acting on metrics by pull-back and to compactify it with a useful structure. The metric spaces which are limit of Einstein 4-manifolds with uniformly controlled diameter and volume as well as the associated singularity blow-ups have been under-stood for a long time in the Gromov-Hausdorff sense [And89, BKN89]: they are respectively Einstein orbifolds and Ricci-flat ALE orbifolds . The metric completion of ( E(M 4), d GH ) is (2) E(M 4) ∪ ∂oE(M 4),

where ∂oE(M 4) is the set of orbifold dGH -limits with bounded diameter (i.e. at finite dGH -distance) of Einstein metrics on M 4.In the present article, we find new types obstructions to the desingular-ization of Einstein orbifolds which are special to the compact context. They motivate and indicate positive answers the following questions: 

• Assume that ( M 4 

> o

, go) ∈ ∂oE(M 4) where M 4 has the topology of M 4

> o

desingularized by Eguchi-Hanson metrics. Is go K¨ ahler-Einstein? 

• Under the same assumptions, is ∂oE(M 4) of codimension 2 in E(M 4)? 

• Can we desingularize a flat metric on T4/Z2 by smooth Ricci-flat met-rics with generic holonomy thanks to Eguchi-Hanson metrics? 

A new obstruction to the desingularization in the compact case 

Any smooth Einstein 4-manifold close to a compact Einstein orbifold in a mere Gromov-Hausdorff sense has recently been produced by a gluing-perturbation procedure [Ozu19a, Ozu19b]. In the present paper, for simplic-ity, we will focus on an Einstein orbifold ( Mo, go) with integrable Einstein deformations (like all known 4-dimensional examples) and consider only the simplest singularities modeled on R4/Z2 ∼ C2/Z2, whose minimal resolution has the topology T ∗S2 of the Eguchi-Hanson metric [EH78]. 

Remark 0.1. This is conjectured to be the only possible topology for an Einstein desingularization of R4/Z2, see [BKN89]. Higher order obstructions to the desingularization 903 Let us denote M the differentiable manifold obtained by minimal res-olution (in some orientation) of the R4/Z2 ≈ C2/Z2 singularities of Mo.Using [Ozu19a, Ozu19b], we know that if there exists a sequence of Einstein metrics on M converging to ( Mo, go) in the Gromov-Hausdorff sense, then an obstruction already noticed in [Biq13] is satisfied at every singular point of Mo. More precisely, denoting respectively R+

> go

(p) and R−

> go

(p) the selfdual and anti-selfdual parts of the curvature at a singular point p ∈ Mo seen as an endomorphism on the space of 2-forms, we have either det R+

> go

(p) = 0 or det R−

> go

(p) = 0. This means that in some basis, we have either (3) R+

> go

(p) = 

⎡⎣

0 0 00 ∗ ∗

0 ∗ ∗

⎤⎦ or, R−

> go

(p) = 

⎡⎣

0 0 00 ∗ ∗

0 ∗ ∗

⎤⎦ .

We will first show that an additional obstruction holds under weaker assumptions than those of [Biq13]. A physically motivated assumption is that of the stability of the Einstein metric. This condition essentially means that the linearization of the Ricci curvature has nonnegative spectrum, see Definition 1.11. We are now ready to state the first main result of this paper: 

Theorem 0.2. Let (M 4 

> o

, go) be a compact Einstein orbifold with Ric( go) = Λgo for Λ ∈ R, with integrable Einstein deformations and with singularities 

R4/Z2. Assume that we have (M 4 

> o

, go) ∈ E(M 4)GH for M = Mo#T ∗S2# . . . 

#T ∗S2, where # denotes a gluing in the positive or negative orientation and along the cone R4/Z2. Assume additionally one of the following properties: 1. there exists a sequence (gn)n of stable Ricci-flat (Definition 1.11) met-rics in E(M 4) converging to go in the Gromov-Hausdorff sense, or, 2. Mo has only one singularity and is rigid (i.e. does not admit infinites-imal Einstein deformations). Then, for any singular point p of Mo, there exists a basis of the self-dual 2-forms or anti-selfdual 2-forms in which we have (depending on the orientation of the gluing): 

(4) R+

> go

(p) = 

⎡⎣

0 0 00 0 00 0 Λ

⎤⎦ or R−

> go

(p) = 

⎡⎣

0 0 00 0 00 0 Λ

⎤⎦ .

Notice that a curvature of the form (4) is typical of K¨ ahler-Einstein metrics. 904 Tristan Ozuch Theorem 0.2 is specific to the compact case and is in sharp contrast with Biquard’s desingularization [Biq13] in the asymptotically hyperbolic case. Indeed, the degeneration of the asymptotically hyperbolic AdS Taub-Bolt metrics converges to an orbifold which is rigid and has one singularity 

R4/Z2 but does not satisfy (4), see Example 2.1. 

Remark 0.3. Since the convergence is allowed to be only in the Gromov-Hausdorff sense, the assumptions of Theorem 0.2 are weaker than in [Biq13, Corollary 9.3], where the obstruction (3) at the singular point was first ob-served. Moreover, the present proof would also yield an obstruction for other Kleinian singularities by [Biq16, Lemme 9] and [Biq16, Lemme 12]. 

Another goal here is to obtain a new obstruction result under some tech-nical assumption of existence of a sequence of metrics in E(M 4) sufficiently transverse to the boundary ∂oE(M 4) of (2). We will say that a sequence of Einstein metrics is a transverse desingularization of the orbifold ( Mo, go)if the sequence is almost orthogonal to ∂oE(M ), see Definition 1.29 and Figure 2. Almost all Einstein metrics obtained by gluing-perturbation are transverse, see [Top87a, Top87b, LS94, Don12, BK17]. The constructions of [Biq13, Biq16, Biq17] are notable exceptions. A weaker assumption than being transverse for an Einstein desingularization is being nondegenerate .We will say that a sequence of Einstein metrics is a nondegenerate Einstein desingularization of ( Mo, go) ∈ ∂oE(M ) if the sequence approaches ( Mo, go)without being “too tangent” to ∂oE(M ), see Definition 1.29 and Figure 1. This notion is in the spirit of the assumption of genericity of [Spo14] and 

nondegeneracy of [BR15]. 

Proposition 0.4. Let (M 4 

> o

, go) be a compact Einstein orbifold with 

Ric( go) = Λ go for Λ ∈ R, with integrable Einstein deformations and with singularities R4/Z2. Assume that we have (M 4 

> o

, go) ∈ E(M 4)GH for M =

Mo#T ∗S2# . . . #T ∗S2, where # denotes a gluing in the positive or nega-tive orientation and along the cone R4/Z2. Assume additionally one of the following properties: 1. there exists a transverse (Definition 1.29) sequence (gn)n of metrics in E(M 4) converging to go in the Gromov-Hausdorff sense, 2. Λ = 0 and there exists a nondegenerate (Definition 1.29) sequence 

(gn)n of metrics in E(M 4) converging to go in the Gromov-Hausdorff sense, 3. Mo has only one singularity and there exists a nondegenerate sequence 

(gn)n of metrics in E(M 4) converging to go in the Gromov-Hausdorff sense. Higher order obstructions to the desingularization 905 

Then, for any singular point p of Mo, go satisfies the obstruction (4) .

Remark 0.5. The proof of Proposition 0.4 relies on the fact that our com-pact deformations add as many degrees of freedom as new obstructions to satisfy. The obstruction (4) is not satisfied by the orbifolds of the desingular-izations of [Biq13, Biq16, Biq17] or Example 2.1, which rely on nondegen-erate (but not transverse) Einstein deformations coming from the confor-mal infinity. These deformations from the conformal infinity add an infinite number of degrees of freedom without adding any obstruction. 

It is somewhat expected that the completion E(M ) ∪ ∂oE(M ) of the moduli space E(M ) is real-analytic or real-subanalytic, see [And10]. This would imply that the orbifold metrics can be approached by curves of Ein-stein metrics. An initial intuition for Theorem 0.2 is [Biq17] which shows that if Λ = 0 and the obstruction (4) is not satisfied, then the orbifold met-rics cannot be approached by curves of Einstein metrics. Our proofs however do not use this fact and even work in the case when Λ = 0. They rely heav-ily on the computations of the second variations of the Ricci curvature of [Biq16] and the formalism of [Fin11]. 

Is ∂oE( M ) a boundary or a filling? 

An interesting problem on which Theorem 0.2 sheds some light is the size of ∂oE(M 4) the set of singular metrics in the completion (2) of the moduli space of Einstein metrics. Anderson proposes the following “optimistic” (in his own words) conjecture. 

Conjecture 0.6 ([And10]) . The subspace ∂oE(M 4) is of codimension 2 in 

E(M 4)GH .

This conjecture means that we should not think of ∂oE(M 4) as a bound-ary of E(M 4) but rather as a filling of missing pieces as it was pictured in [And92] in the case of M 4 = K3. 

Remark 0.7. This is false in the asymptotically hyperbolic context where the desingularizations of [Biq13] applied to the AdS Taub-Bolt orbifold (Example 2.1) show that ∂oE(M 4) is of codimension 1.

With our present vocabulary, Conjecture 0.6 means that given a compact Einstein orbifold ( Mo, go) ∈ ∂oE(M 4), the space of Einstein desingulariza-tions of Mo which are transverse to ∂oE(M 4) is at least 2-dimensional. Theorem 0.2 can be seen as a step towards this conjecture in the situation where we desingularize by an Eguchi-Hanson metric at a small scale t > 0. Indeed, its proof shows that: 906 Tristan Ozuch 

• if R+

> go

(po) is invertible, then there is no desingularization which is Einstein up to a o(t) error, 

• if the kernel of R+

> go

(po) is of dimension 1, then there is no transverse desingularization which is Einstein up to a o(t2) error and there is exactly a one-dimensional set of desingularizations which are Einstein up to a o(t) error, 

• if the kernel of R+

> go

(po) is of dimension 2 or 3, then the transverse desingularizations which are Einstein up to a o(t2) error are of dimen-sion 2 or 3 and in correspondence with the kernel of R+

> go

(po). Finally, recall that Einstein metrics with a curvature tensor of the form (4) for Λ = 0 at all points are locally hyperk¨ ahler metrics. Since we have only identified the first two obstructions of an infinite list, we might wonder if the remaining obstructions impose this condition at all points. We ask the following question. 

Question 0.8. Let (M 4 

> o

, go) be a Ricci-flat orbifold, and assume that it can be desingularized in the Gromov-Hausdorff sense by Einstein metrics 

(M 4, gn)n∈N∗ forming trees of K¨ ahler Ricci-flat ALE metrics. Are the orb-ifold (M 4 

> o

, go) and the smooth metrics (M 4, gn) necessarily quotients of hy-perk¨ ahler metrics? 

A positive answer to the above question combined with the folklore con-jecture that all Ricci-flat ALE orbifolds are K¨ ahler indicates that it may not be possible to produce Ricci-flat metrics which are not K¨ ahler by gluing constructions on Ricci-flat orbifolds. This pessimistic perspective is related to one of the main issue in Riemannian geometry which is to understand the structure of Ricci-flat metrics on compact manifolds. 

Ricci-flat metrics and reduced holonomy 

For a long time, it was believed that compact Ricci-flat metrics should be flat. The resolution of Calabi’s conjecture by Yau [Yau78] provided many counter-examples. These so-called Calabi-Yau metrics are the only currently known examples and they have reduced holonomy (that is different from the generic holonomy SO (n) in dimension n). A lingering question since then is therefore the following one. 

Question 0.9. Do all compact Ricci-flat manifolds have reduced holonomy? 

A physically relevant additional property that one can ask from a Ricci-flat metric, is that of being stable , see [Ach19]. 

Question 0.10 ([Ach19]) . Do all compact stable Ricci-flat manifolds have reduced holonomy? Higher order obstructions to the desingularization 907 

Construction of hyperk¨ ahler metrics by gluing-perturbation 

Compact non flat Ricci-flat metrics are not explicit at all, but a classical way to approach them and to obtain a more concrete picture is to produce them by gluing various explicit noncompact and singular blocks together into an approximate Ricci-flat metric and perturb it into an actual Ricci-flat metric. Gibbons-Pope [GP79] and Page [Pag78] proposed a conjectural and physically motivated picture for some hyperk¨ ahler, hence Ricci-flat, met-rics on some K3 surfaces. The idea was to desingularize the orbifold T4/Z2

which has 16 singularities of type R4/Z2 by gluing 16 Eguchi-Hanson metrics 

in the same orientation and to perturb the result to a hyperk¨ ahler metric. This was rigorously obtained for Eguchi-Hanson metrics glued at compara-ble scales by Topiwala [Top87a, Top87b] and Lebrun-Singer [LS94], see also [Don12]. The proof heavily relies on K¨ ahler geometry arguments. 

A Ricci-flat but not locally hyperk¨ ahler metric? 

In 1981, Page [Pag81] asks a new question. 

Question 0.11. Is it possible to perturb a gluing of Eguchi-Hanson metrics in different orientations to the orbifold T4/Z2 into a Ricci-flat metric? 

Remark 0.12. It is often conjectured, see for instance [BKN89], that the only Ricci-flat metric asymptotic to R4/Z2 is the Eguchi-Hanson metric. This would therefore describe any possible Einstein desingularization of 

T4/Z2.

Having different orientations for the Eguchi-Hanson metrics prevents the use of K¨ ahler geometry techniques. A positive answer to Question 0.11 would provide a Ricci-flat metric with generic holonomy and a negative answer to Question 0.9. 

Brendle-Kapouleas configuration 

In [BK17], Brendle and Kapouleas studied Question 0.11 in the most sym-metric situation: the orbifold metric comes from the regular lattice Z4, the points where the gluing are done in the positive or negative orientation follow a so-called chessboard pattern , and the Eguchi-Hanson metrics in the same orientation are glued with the same SO (4) or O(4) \SO (4) parameter and the same size. In this 1-dimensional set of configurations, they exhibit one 

interaction between the bubbles glued in different orientation. They remark-ably use this obstruction to construct an intriguing solution to the Ricci flow which exhibits a new behavior: it is an ancient Ricci-flow desingularizing the orbifold T4/Z2.908 Tristan Ozuch 

Partial answer to Page’s question 

In this article, we consider the general situation of the desingularization of a flat metric on T4/Z2 obtained from a lattice L(Z4) for L ∈ GL (4 , R) and desingularized by Eguchi-Hanson metrics glued in various directions, sizes and orientations. For each configuration of positively and negatively oriented Eguchi-Hanson metrics, this yields a 57-dimensional space of candidates to a Ricci-flat gluing-perturbation as in [Ozu19b] and therefore of potential positive answers to Question 0.11. We however identify a great number of interactions between these met-rics which induce obstructions interpreted as curvature conditions similar to those of (3) and (4). 

Theorem 0.13 (Informal, Corollaries 4.3 and 4.10) . We have the follow-ing numbers of constraints in this 57 -dimensional space of desingularization configurations. 1. For general parameters, there are 57 necessary polynomial equations that the gluing parameters of the Eguchi-Hanson metrics should satisfy for an Einstein desingularization to exist. 48 of these equations are analogous to the obstruction (3) .2. For general parameters, there are 84 necessary polynomial equations that the gluing parameters should satisfy for a stable Ricci-flat desin-gularization to exist. 80 of these equations are analogous to the ob-struction (4) .3. For parameters corresponding to a nondegenerate desingularization, there are 84 necessary polynomial equations that the gluing parameters of the Eguchi-Hanson metrics should satisfy for an Einstein desingu-larization to exist. 80 of these equations are analogous to the obstruc-tion (4) .The coefficients of these (quadratic and quartic) polynomial equations depend on the flat metric on T4/Z2 only. 

This indicates that generic flat metrics on T4/Z2, should not be Gromov-Hausdorff limit of Einstein metrics bubbling out Eguchi-Hanson metrics in different orientations. 

Remark 0.14. In the configuration proposed by Brendle and Kapouleas [BK17], the 57 obstructions of the first point are not satisfied. 

A simpler consequence is that a lot of configurations of positively and negatively oriented Eguchi-Hanson metrics are impossible. We in particular obtain the following obstruction under a topological assumption. Higher order obstructions to the desingularization 909 

Theorem 0.15 (Theorem 4.11) . There does not exist a sequence of Einstein metrics dGH -converging to the regular torus (obtained from the lattice Z4)by bubbling out exactly one positively oriented Eguchi-Hanson metric and 15 negatively oriented Eguchi-Hanson metrics. 

Remark 0.16. It is likely that this result holds without assuming that the lattice is the usual Z4, see Conjecture 4.14. 

Remark 0.17. The desingularization by stable Ricci-flat metrics is much more restrictive. A direct extension of the proof of Theorem 0.15 states that the desingularization is impossible with less than 3 positively oriented Eguchi-Hanson metrics and the rest of negatively oriented, see Corollary 4.15. 

A configuration satisfying the first obstructions 

Seeing the above obstruction results, one would be tempted to try and prove that it is impossible to obtain a Ricci-flat but not hyperk¨ ahler metric by gluing-perturbation of Eguchi-Hanson metrics to a flat T4/Z2. One would maybe expect that the above 84 obstructions should be enough to show that every configuration is obstructed. Perhaps surprisingly, we find a set of solutions to our 84 equations. More precisely, there exists an explicit 14-dimensional set of configurations of gluing of Eguchi-Hanson metrics which satisfy the 84 above equations. The orientations of the Eguchi-Hanson metrics follow the chessboard pattern of [BK17], but their directions and sizes are not constrained. 

1. Main definitions 

Note 1.1. All along this article, when the name of a metric is in bold, then it is Einstein. 

1.1. Einstein orbifolds and ALE spaces 

For Γ a finite subgroup of SO (4) acting freely on S3, let us denote ( R4/Γ, e)the flat orbifold obtained by the quotient of the Euclidean metric on R4 by the action of Γ, and re := de(., 0). 

Definition 1.2 (Orbifold (with isolated singularities)) . We will say that a metric space (Mo, g o) is an orbifold of dimension n  2 if there exists 0 > 0

and a finite number of points (pk)k of Mo called singular such that we have the following properties: 910 Tristan Ozuch 

1. the space (Mo\{ pk}k, g o) is a manifold of dimension n,2. for each singular point pk of Mo, there exists a neighborhood of pk,

Uk ⊂ Mo, a finite subgroup acting freely on Sn−1, Γk ⊂ SO (n), and a diffeomorphism Φk : Be(0 ,  0) ⊂ Rn/Γk → Uk ⊂ Mo for which, the pull-back of Φ∗

> k

go on the covering Rn is smooth. Here, diffeomorphism 

is understood in the orbifold sense, i.e. it is a diffeomorphism between the cover R4 and the associated cover of Uk.

Remark 1.3. The analysis on an orbifold is exactly the same as the analysis on a manifold up to using finite local coverings at the singular points. 

Definition 1.4 (The function ro on an orbifold) . We define ro, a smooth function on Mo satisfying ro := (Φ k)∗re on each Uk, and such that on 

Mo\Uk, we have 0  ro < 1 (the different choices will be equivalent for our applications). We will denote, for 0 <   0,

(5) Mo() := {ro >  } = Mo\

( ⋃ 

> k

Φk

(Be(0 ,  )))

.

Let us now turn to ALE metrics. 

Definition 1.5 (ALE orbifold (with isolated singularities)) . An ALE orb-ifold of dimension n  4, (N, g b) is a metric space for which there exists 

0 > 0, singular points (pk)k and a compact K ⊂ N for which we have: 1. (N, g b) is an orbifold of dimension n,2. there exists a diffeomorphism Ψ∞ : ( Rn/Γ∞)\Be(0 ,  −10 ) → N \K such that 

rl

> e

|∇ l(Ψ ∗∞gb − e)|e  Clr−n 

> e

.

Definition 1.6 (The function rb on an ALE orbifold) . We define rb a smooth function on N satisfying rb := (Ψ k)∗re on each Uk, and rb := (Ψ ∞)∗re on 

U∞, and such that 0  rb  −10 on the rest of N (the different choices are equivalent for our applications). For 0 <   0, we will denote 

N () := { < r b <  −1} = N \

( ⋃ 

> k

Ψk

(Be(0 ,  )) ∪ Ψ∞

((R4/Γ∞)\Be(0 ,  −1)))

.

(6) Now, consider a subset So of the singular points of Mo (respectively S

of N ). Higher order obstructions to the desingularization 911 

Definition 1.7 (Functionals ro,S o and rb,S ). We define the functional ro,S o

(respectively rb,S ) exactly like in Definitions 1.4 (respectively 1.6) by only considering the sets Uk containing points of So (respectively S). 

A metric g close to go (with some adapted decay at infinity in the non-compact case) is Einstein and is in Bianchi gauge with respect to go, that is satisfies Bgog := ( δgo + 12 dtr go)g = 0, if and only if it satisfies 

Φgo(g) := Ric( g) − Λg + δ∗ 

> g

Bgog = 0 ,

see for instance [Biq13, Section 6]. The linearization of Φgo at go is 

Pgo := 12 ∇∗

> go

∇go − ˚Rgo,

where ˚R is the action of curvature on symmetric 2-tensors: for an orthonor-mal basis ( ei)i,˚R( h)( X, Y ) = ∑

> i

h( Rm( ei, X )Y, e i

).

Definition 1.8 (Infinitesimal Einstein deformations) . For a compact or ALE Einstein orbifold (M, g) with Ric( g) = Λ g, we define O(g) as the kernel of Pg on L2(g).

Definition 1.9 (Einstein modulo obstructions deformations) . According to [Ozu19b] (see also [Koi83]), there exists  > 0 such that for any v ∈ O(g)

with ‖v‖L2(g) <  , there exists a unique metric ¯gv satisfying 1. Φg(¯ gv) ∈ O(g),2. ¯gv − (g + v) ⊥g O(g),3. ‖¯gv − g‖L2(g)  2.

All along this article, in order to simplify the exposition and for lack of nonintegrable examples, we will only consider Einstein metrics with inte-grable Einstein deformations. 

Definition 1.10 (Einstein metric with integrable deformations) . An Ein-stein metric g only has integrable infinitesimal Einstein deformations if for any v ∈ O(g), the metric ¯gv = gv actually satisfies 1. Φg(gv) = 0 ,2. gv − (g + v) ⊥g O(g),3. ‖gv − g‖L2(g)  2.912 Tristan Ozuch An additional class of metrics we will be interested in is that of stable Ricci-flat metrics. 

Definition 1.11 (Stable Ricci-flat metrics) . We will say that g is a stable Ricci-flat metric if it is Ricci-flat and satisfies: for all smooth compactly supported symmetric 2-tensor h:

〈Pgh, h 〉 

> L2(g)

 0.

All of the known examples of compact Ricci-flat metrics are stable .

1.2. Eguchi-Hanson metrics 

Let us describe the Eguchi-Hanson metric [EH78]. In this article, the Ricci-flat ALE metrics ( N, g b) we will consider will almost always be homothetic transformations of the Eguchi-Hanson metric. The Eguchi-Hanson metric, which we will denote eh , is defined on T ∗S2.It is asymptotic to the flat cone R4/Z2. Denote ( x1, x 2, x 3, x 4) coordinates in an orthonormal basis of R4, and define r := √x21 + x22 + x23 + x24, and a basis of invariant 1-forms on the sphere S3, ( α1, α 2, α 3) by 

α1 := 1

r2 (x1dx 2 − x2dx 1 + x3dx 4 − x4dx 3)and the other by cyclic permutation of the indices {2, 3, 4}.Outside of the zero section of T ∗S2 represented by r = 0, the metric 

eh has the following expression (with the identification T ∗S2\S2 ≈ (R4/

Z2)\{ 0}): (7) eh := 

√ r4

1 + r4 (dr 2 + r2α21) + √1 + r4(α22 + α23).

The metric extends to T ∗S2 by adding the zero section S2 with metric α22+α23

at r = 0. We will always denote S2 that zero-section of T ∗S2.This gives the asymptotic development at infinity 

eh = e − 12r4 (dr 2 + r2α21 − r2α22 − r2α23) + O(r−8),

where H 4 := − 12r4 (dr 2 +r2α21 −r2α22 −r2α23) is divergence-free and trace-free with respect to the Euclidean metric e = dr 2 + r2(α21 + α22 + α23). Higher order obstructions to the desingularization 913 

1.2.1. Curvature of Eguchi-Hanson metrics. On R4, we define the 2-forms 

θ± 

> 1

:= rdr ∧ α1 ± r2α2 ∧ α3,

and similarly θ± 

> 2

and θ± 

> 3

by cyclic permutations, and we define the usual bases 

ω± 

> 1

:= dx 1 ∧ dx 2 ± dx 3 ∧ dx 4

and similarly ω± 

> 2

and ω± 

> 3

by cyclic permutations. The θ+ 

> i

and ω+ 

> i

are selfdual and the θ− 

> i

and ω− 

> i

are anti-selfdual. Direct computations yield the following relation between them: θ+ 

> i

= ω+ 

> i

, and for x ∈ R4,

θ− 

> i

(x) = 

> 3

∑

> j=1

xT (ω+ 

> i

◦ ω− 

> j

)x

|x|2 ω− 

> j

,(8) where ω+1 ◦ ω− 

> i

is the symmetric traceless matrix given by the (commuting) product of the antisymmetric matrices associated to ω+ 

> i

and ω− 

> j

, and where 

xT is the transpose of x.

Remark 1.12. The product ω+ 

> i

◦ ω− 

> j

= ω− 

> i

◦ ω+ 

> j

is a trace-free involution and therefore it is characterized by two planes of eigenvalues 1 and −1.

Remark 1.13. We will often use the identification of the traceless sym-metric 2-tensors Sym 20(T M ) and Ω+ ⊗ Ω− where (ω+, ω −) ∈ Ω+ × Ω− is associated to ω+ ◦ ω− = ω− ◦ ω+.

For any ζ = ( ζ1, ζ 2, ζ 3) ∈ R3, we denote 

ζ ± := ζ1ω± 

> 1

+ ζ2ω± 

> 2

+ ζ3ω± 

> 3

∈ Ω±.

Definition 1.14. We define for any x ∈ R4 the linear transformation ρx

which to ζ = ( ζ1, ζ 2, ζ 3) ∈ R3 associates ρx(ζ) ∈ R3 whose j’s coordinate is 

ρx(ζ)j = xT (ζ+ ◦ ω− 

> j

)x

|x|2 .

Remark 1.15. Identifying R4 with the space of quaternions and R3 with the space of pure quaternions, for any x ∈ R4, the map ρx : R3 → R3 is exactly the rotation produced on the pure quaternionic part by conjugation by x. More precisely, identifying ζ ∈ R3 with the pure quaternion (0 , ζ ) in the usual basis, we have 

(0 , ρ x(ζ)) = x · (0 , ζ ) · x−1.914 Tristan Ozuch The metric eh is Ricci-flat, anti-selfdual and has the following anti-selfdual curvature: (9) R−(eh ) = 1

r6

⎡⎣

8 0 00 −4 00 0 −4

⎤⎦

in a basis asymptotic to the basis ( θ− 

> i

)i, see [EH78]. We also remark that we have H 4 = − ω+1 ◦θ− 

> 1
> 2r4

where H 4 is defined by eh = e + H 4 + O(r−8) at infinity and where ω+1 ◦ θ− 

> 1

is the (commutating) composition of the antisymmetric matrices associated to ω+1 and θ− 

> 1

.More generally, for any ζ = ( ζ1, ζ 2, ζ 3) ∈ R3\{ 0}, consider ( ζ+(k))k∈{ 1,2,3}

an orthogonal basis of Ω + with constant length √2 = |ω+1 | and ζ+(k) =

ζ +/|ζ| = √2ζ+/|ζ+|. We may replace the above 1-forms αk = ω+ 

> k

(dr ) by the 1-forms ζ+(k)(dr ). By a change of variables u = r√|ζ| , one checks that the metric 

eh ζ + := 

√

r4

|ζ|2 + r4

(

dr 2 + r2ζ+(1) (dr )2)

+ √|ζ|2 + r4

(

ζ+(2) (dr )2 + ζ+(3) (dr )2)

(10) is homothetic to eh and more precisely satisfies the following properties. 

Proposition 1.16. Let ζ = ( ζ1, ζ 2, ζ 3) ∈ R3\{ 0} and denote ζ+ := ζ1ω+1 +

ζ2ω+2 + ζ3ω+3 . We have the following properties: 1. at infinity, we have 

(11) eh ζ + = e − ρ(ζ)− ◦ ζ+

2r4 + O(|ζ|4r−8),

2. eh ζ + is isometric to |ζ| · eh ,3. eh (1 ,0,0) + = eh , and 4. on S2, denoting (ζ+(k))k∈{ 1,2,3} an orthonormal basis of the selfdual 2-forms of constant length with ζ+(1) = ζ+/|ζ|, the zero-section of T ∗S2,the metric is |ζ+|(ζ+(2) (dr )2 + ζ+(3) (dr )2).

Remark 1.17. These metrics eh ζ + for ζ ∈ R3\{ 0} reach all of the met-rics obtained by orientation-preserving rotations and rescaling of eh up to isometry .Higher order obstructions to the desingularization 915 We will need to understand their curvature in the last sections of this article. From the computations of [EH78] and Proposition 1.16, we have the following result. For ζ = ( ζ1, ζ 2, ζ 3), denote H 4(ζ+) := − ρ(ζ)−◦ζ +

> 2r4
> e

. Then, the linearization of the curvature at e in the direction H 4(ζ+) is Ricci-flat anti-selfdual and we have (12) deR−(H 4(ζ+)) = |ζ|2

r6

⎡⎣

8 0 00 −4 00 0 −4

⎤⎦

in any orthogonal basis with constant length of the anti-selfdual 2-forms of 

R4 whose first vector is ρ(ζ)− 

> |ζ|

.Identifying the space of endomorphisms of Ω −, End(Ω −) and Ω − ⊗ Ω−,this can be rewritten as (13) deR−(H 4(ζ+)) = 12 πtr (ρ(ζ)− ⊗ ρ(ζ)−)

r6

where πtr h := h − tr h 

> 3

I3 is a projection on trace-free matrices. 

Remark 1.18. In the constant basis (ω− 

> 1

, ω − 

> 2

, ω − 

> 3

), the coefficients of 

deR−(H 4(ζ+)) (seen as a 3 × 3 matrix) are harmonic by (8) as expected from [Biq16, Lemme 3]. 

1.2.2. Infinitesimal variations. The deformations of the Eguchi-Hanson metric are given by the variations of ζ in (10). For ζ = (1 , 0, 0), an orthogonal basis of the L2(eh )-kernel of Peh denoted 

O(eh ) may be computed. Denote ( o1, o2, o3) given by the infinitesimal vari-ations of ζ respectively in the directions (1 , 0, 0), (0 , 1, 0) and (0 , 0, 1). They have the following developments in the coordinates of the above develop-ment (11), (14) ok = O4 

> k

+ O(r−8 

> e

) with O4 

> k

= − θ− 

> 1

◦ θ+

> k

r4 .

Remark 1.19. The symmetric 2-tensor O41 is equal to twice to the asymp-totic term H 4 of eh , see (11) .

The infinitesimal deformations o1, o2 and o3 respectively induce the fol-lowing infinitesimal changes of anti-selfdual curvature in the basis 916 Tristan Ozuch (θ− 

> 1

, θ − 

> 2

, θ − 

> 3

): (15) 1

r6

⎡⎣

8 0 00 −4 00 0 −4

⎤⎦ , 1

r6

⎡⎣

0 4 04 0 00 0 0

⎤⎦ , and 1

r6

⎡⎣

0 0 40 0 04 0 0

⎤⎦ .

For another ζ ∈ R3\{ 0}, let us consider, thanks to the second point of Proposition 1.16, a diffeomorphism φ such that φ∗eh ζ + = |ζ| · eh . Then, (ok(ζ+)) k := (φ∗ok)k forms an orthogonal basis of O(eh ζ +) with 

‖φ∗ok‖L2(eh ζ+ ) = ‖ok‖L2(eh ) since the L2-norm of 2-tensors is invariant by rescaling in dimension 4. Recalling that in the same coordinates at infinity, the first r−4 

> e

-terms of |ζ|φ∗eh and of eh ζ + coincide, we find 

|ζ| · φ∗

( ω+1 ◦ θ−

> 1

2r4

> e

)

= ζ+ ◦ ρ(ζ)−

2r4

> e

and therefore, denoting ( ζ+(k))k∈{ 1,2,3} a basis of the selfdual 2-forms of con-stant length with ζ+(1) = ζ+/|ζ|, the development at infinity of the φ∗ok

is (16) ok(ζ+) = φ∗ok = ζ+(k) ◦ ρ(ζ)−

r4

> e

+ O(|ζ+|3r−8 

> e

).

Remark 1.20. We check that ok(ζ+) = ∂ζ +(k)

eh ζ +, where we denoted 

∂ζ +(k)

eh ζ + the differential of ζ+  → eh ζ + at ζ+ in the direction ζ+(k).

1.2.3. Negative orientation. We will also consider negatively oriented 

Eguchi-Hanson metrics. For ζ = ( ζ1, ζ 2, ζ 3) ∈ R3\{ 0}, we define 

eh ζ − := 

√

r4

|ζ|2 + r4

(

dr 2 +r2ζ−

> (1)

(dr )2)

+ √|ζ|2 + r4

(

ζ−

> (2)

(dr )2 + ζ−

> (3)

(dr )2)

.

(17) It is isometric to |ζ| · eh but has the opposite orientation. At infinity, we have the development 

eh ζ − = e − ζ− ◦ ρ(ζ)+

2r4 + O(|ζ|4r−8).Higher order obstructions to the desingularization 917 

1.3. Na¨ ıve desingularizations 

Let us now recall the definition of a na¨ ıve desingularization of an orbifold from [Ozu19a]. 

Gluing of ALE spaces to orbifold singularities. Let 0 < 2 <  0

be a fixed constant, t > 0, ( Mo, g o) an orbifold and Φ : Be(0 ,  0) ⊂ R4/

Z2 → U a local chart of Definition 1.2 around a singular point p ∈ Mo.Let also ( N, g b) be an ALE metric asymptotic to R4/Z2, and Ψ ∞ : ( R4/

Z2)\Be(0 ,  −10 t 12 ) → N \K a chart at infinity of Definition 1.5. For s > 0, define φs : x ∈ R4/Γ → sx ∈ R4/Γ. For t <  40, we define 

Mo#N as N glued to Mo thanks to the diffeomorphism Φ ◦ φ√t ◦ Ψ−1 : Ψ( Ae(−10 ,  0t−1/2)) → Φ( Ae(−10

√t,  0)) .

Consider χ : R+ → R+, a C∞ cut-off function supported on [0 , 2] and equal to 1 on [0 , 1]. 

Definition 1.21 (Na¨ ıve gluing of an ALE space to an orbifold) . We define a na¨ ıve gluing of (N, g b) at scale 0 < t <  4 to (Mo, g o) at the singular point p, which we will denote (Mo#N, g o#p,t gb) by putting go#p,t gb = go on 

M \U , go#p,t gb = tg b on K, and 

go#p,t gb = χ(t− 14 re)Ψ ∗∞gb + (1 − χ(t− 14 re))Φ∗go

on Ae(−1√t, 2).

Definition 1.22 (Function rD on a na¨ ıve desingularization) . On a na¨ ıve 

(M, g D), we define the function smooth function rD in the following way: 1. rD = ro on Mo(0) defined in (5) ,2. rD = √tjrbj on each Nj(−10 ) defined in (6) and 3. rD = re on Ae(−10

√t,  0).

Let us fix a notation for the desingularization by Eguchi-Hanson metrics. 

Definition 1.23 (Na¨ ıve desingularization by Eguchi-Hanson metrics) . Let 

(Mo, go) be a compact Einstein orbifold with integrable Einstein deforma-tions (Definition 1.10) and R4/Z2 singularities at points j ∈ S, and let 

v ∈ O(go) and ζ = ( ζj 

> j

)j with ζj ∈ R3\{ 0} and j ∈ { +, −} . We define gDζ,v 

the na¨ ıve gluing (as in Definition 1.21) of eh ζ jj /|ζj| to gv at scale |ζj| using the ALE coordinates of (10) and (17) .918 Tristan Ozuch 

Definition 1.24 (Approximate obstructions ˜O(gDζ,v )) . We define ˜O(gDζ,v )

the linear space spanned by the infinitesimal variations of (v, ζ )  → gDζ,v .

Remark 1.25. The space ˜O(gDζ,v ) is very close to the approximate ob-struction space of [Ozu19b] and even yields better estimates. The results of [Ozu19b] therefore hold when using ˜O(gDζ,v ) instead of the similar space 

˜O(gD) of [Ozu19b]. 

We next define the notion of nondegenerate sequence of na¨ ıve desingu-larizations in the spirit of [BR15] (see also the notion of generic smoothings in [Spo14]). It intuitively means that the desingularization sequence reaches an element ∂oE(M ) without being too tangent to ∂oE(M ). 

Definition 1.26 (Nondegenerate na¨ ıve desingularization) . We will say that a sequence of na¨ ıve desingularizations (M, g Dtn,v n) of a compact Einstein orb-ifold (Mo, go) is nondegenerate if, denoting tn, max = max tn,j and tn, min =min tn,j , we have 1. lim n→+∞ tn, min  

> tn, max

> 0 and 2. ‖vn‖2 

> L2 (go)
> tn, min

→ 0.

This technical definition essentially means that the gluing scales are comparable and the Einstein deformations of the orbifold are not too large. A stronger notion is that of transverse desingularization .

Definition 1.27 (Transverse na¨ ıve desingularization) . We will say that a sequence of na¨ ıve desingularizations (M, g Dtn,v n) of a compact Einstein orb-ifold (Mo, go) is transverse if we have 1. lim n→+∞ tn, min  

> tn, max

> 0 and 2. ‖vn‖L2 (go) 

> tn, min

→ 0.

Remark 1.28. Usual desingularizations are transverse and often even or-thogonal , with vn = 0 . The desingularization of [Biq13] is a notable excep-tion. 

Let us finally recall that according to [Ozu19a, Ozu19b], for any Einstein orbifold ( Mo, go), and any δ > 0, there exists  = (( Mo, go), δ ) > 0 such that if an Einstein metric ( M, g) satisfies 

dGH 

((Mo, go), (M, g)) < , Higher order obstructions to the desingularization 919 then, there exists a na¨ ıve desingularization ( M, g D) of ( Mo, go) and a dif-feomorphism φ : M → M with 

‖φ∗g − gD‖C 2,α β, ∗ (gD) < δ, 

where the weighted H¨ older norms C2,α β, ∗ (gD) are defined in Section A in the Appendix. We finally define the notions of nondegenerate and transverse sequence of Einstein metrics desingularizing the orbifold ( Mo, go) ∈ ∂oE(M ). 

Definition 1.29 (Nondegenerate and transverse Einstein desingulariza-tion) . Let (M 4, gn)n∈N be a sequence of Einstein metrics dGH -converging to a compact Einstein orbifold (Mo, go) ∈ ∂oE(M 4). By [Ozu19a, Ozu19b], there exists a sequence of na¨ ıve desingularizations (gDtn,v n)n such that up to acting on gn by a diffeomorphism, we have 1. ‖gn − gDtn,v n‖C 2,α β, ∗ (gDtn,vn )   for some  = (go) > 0 determined in [Ozu19b], 2. gn is in reduced divergence-free gauge (defined in [Ozu19b]) with re-spect to gDtn,v n

3. gn − gDtn,v n is L2(gDtn,ζ n)-orthogonal to ˜O(gDtn,ζ n) of Definition 1.24 We will say that gn is a nondegenerate (respectively transverse ) Einstein desingularization of (Mo, go) if the sequence (gDζn,v n)n is nondegenerate (re-spectively transverse ) in the sense of Definitions 1.26 and 1.27. 

Figure 1: A nondegenerate desingularization (M, gn)n∈N approaches (Mo, go) without being “too tangent” to the boundary ∂oE(M ): it stays in the plain green region. 920 Tristan Ozuch 

Figure 2: A transverse desingularization ( M, gn)n∈N becomes almost or-thogonal to the boundary ∂oE(M ) as it approaches ( Mo, go): it stays in the plain green region. 

2. New obstructions to the desingularization of Einstein orbifolds 

We first deduce a new type of obstruction to the Gromov-Hausdorff desingu-larization of Einstein orbifolds which differs from the ones of [Biq13, Biq16, Ozu19b]. The goal of this section is to prove Theorem 0.2 and Proposi-tion 0.4. This obstruction is special to the compact case, or at least not present in the asymptotically hyperbolic (AH) context if one allows deformations of the conformal infinity (which are infinitely many new degrees of freedom which do not add obstructions). 

Example 2.1. The AdS Taub-Bolt family of metrics constructed by Page-Pope [PP87] are asymptotically hyperbolic (AH) Einstein metrics and con-verge to an AH selfdual Einstein orbifold while bubbling out an Eguchi-Hanson metric (see [Ozu20t, Chapter B] for a precise description of the degeneration). This orbifold has only one singularity R4/Z2 at which we have Ric 0 = 0 because it is Einstein, and in the usual bases of Ω±, we have 

R− =

⎡⎣

−1 0 00 −1 00 0 −1

⎤⎦ ,

because it is selfdual, and finally 

R+ =

⎡⎣

0 0 00 − 32 00 0 − 32

⎤⎦ ,

only has a one-dimensional kernel. Higher order obstructions to the desingularization 921 

The AdS Taub-Bolt orbifold is L2-rigid. If we consider the Einstein de-formations induced by the conformal changes at infinity, then, there exists an infinite dimensional space of nondegenerate Einstein desingularizations, see [Biq13]. This shows that the compactness assumption in Proposition 0.4 is necessary. 

2.1. Degeneration and obstructions 

Let ( Mo, go) be a compact Einstein orbifold with integrable Einstein defor-mations (Definition 1.10) and with a R4/Z2 singularity at p ∈ Mo, and let (N, eh ) be an Eguchi-Hanson metric. At p, we can choose orbifold coordi-nates (Definition 1.2) in which the metric go is in Bianchi gauge with respect to the flat metric e (see [Ozu19b] for a proof in the more difficult case of neck regions), that is satisfies Bego = 0. Since the metric go is smooth in the above orbifold coordinates and because of the Z2-invariance, we have the following development, (18) go = e + H2 + H4 + O(r6

> e

),

where the Hi are homogeneous symmetric 2-tensors with |Hi|e ∼ ri 

> e

with 

BeH2 = 0. At the infinity of N , in the coordinates of (7), we have the following development, (19) eh = e + H 4 + O(r−8 

> e

),

where |H 4|e ∼ r−4 

> e

and with BeH 4 = 0. For a metric g, let us denote Q(2)  

> g

the bilinear terms given by the second derivative of 

h  → Φg(h) := Ric( h) + δ∗

> h

Bgh

at g (whose linearization is Pg). According to [Biq13, Section 3, Section 10 and Lemma 14.1], for any symmetric 2-tensors |H2|e ∼ r2 

> e

with PeH2 = Λ e,and |H4|e ∼ r4 

> e

with PeH4 = Λ H2 − Q(2)  

> e

(H2, H 2), there exist 1. a unique symmetric 2-tensor h2 and reals ( λk)k∈{ 1,2,3} on N satisfying: (20) 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh h2 = Λ eh + ∑

> k

λkok,h2 = H2 + O(r−2),

∫

> S2

〈h2, ok〉eh dv eh |S2 = 0 for all k ∈ { 1, 2, 3}.922 Tristan Ozuch 2. and a symmetric 2-tensor h4 and real numbers ( μk)k∈{ 1,2,3} on N sat-isfying: (21) 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh h4 = Λ h2 − Q(2)  

> eh

(h2, h 2) + ∑

> k

μkok,h4 = H4 + O(r),

∫

> S2

〈h4, ok〉eh dv eh |S2 = 0 for all k ∈ { 1, 2, 3}.

for all  > 0. 

Remark 2.2. The above tensor h4 is not unique since there are 2-tensors which are O(1) at infinity in the kernel of Peh . There will be a best choice of 

h4 in our construction which will ensure that the asymptotics on the orbifold and the ALE match, see Remark 2.11. 

2.1.1. More precision on the first obstruction. Let ζ ∈ R3\{ 0}, and denote ok(ζ±) the basis of O(eh ζ ±) of (16). Since the metric eh ζ ± is homo-thetic to eh , we also find solutions h2 and h4 to 1. a unique symmetric 2-tensor h2(ζ±) on N satisfying the following equa-tions (22) 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ± h2(ζ±) = Λ eh ζ ± + ∑

> k

λk(ζ±)ok(ζ±),h2(ζ±) = H2 + O(r−2),

∫

> S2

〈h2(ζ±), ok(ζ±)〉eh ζ± dv eh ζ± |S2 = 0 for all k ∈ { 1, 2, 3}.

2. and a symmetric 2-tensor h4(ζ±) on N satisfying the following equa-tions 

⎧⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎩

Peh ζ± h4(ζ±) = Λ h2(ζ±)−Q(2)  

> eh ζ±

(h2(ζ±), h 2(ζ±))+ ∑

> k

μk(ζ±)ok(ζ±),h4(ζ±) = H4 + O(r),

∫

> S2

〈h4(ζ±),ok(ζ±)〉eh ζ± dv eh ζ± |S2 = 0 for all k ∈ { 1, 2, 3}.

(23) for all  > 0. Higher order obstructions to the desingularization 923 We moreover have the following values for the λk(ζ±): for some c = 0, (24) λk(ζ±) = c

〈

R±(H2)ζ±, ζ ±

> (k)

〉

,

where ( ζ±

> (k)

)k∈{ 1,2,3} is an orthogonal basis with |ζ±

> (k)

| = √2 and ζ± 

> (1)

= ζ±/|ζ|.We can be more precise about the first obstruction and the symmetric 2-tensor h2.

Lemma 2.3. Let h2 be a solution of (22) (where we omit the dependence in ζ± for simpler equations). Then, we have 

(25) h2 = H2 + H 42 + O(r−4+ ) for any  > 0,

where H 42 is a homogeneous solution to 

(26) PeH 42 = −Q(2)  

> e

(H 4, H 2) + Λ H 4 + ∑

> k

λkO4

> k

, with |H 42 |e ∼ r−2 

> e

.

Moreover, when λk = 0 , then H 42 = 0 .Proof. At infinity, in ALE coordinates we have h2 = H2 + h′ with h′ =

O(r−2+  

> e

) for all  > 0. Since eh = e + H 4 + O(r−8 

> e

), we develop the equation (20) as: 

PeH2 + Pe(h′) + Q(2)  

> e

(H 4, H 2) + O(r−8+  

> e

)= Λ e + Λ H 4 + ∑

> k

λkO4 

> k

+ O(r−8+  

> e

),

and using the assumption that PeH2 = Λ e, we find 

Pe(h′) + Q(2)  

> e

(H 4, H 2) = Λ H 4 + ∑

> k

λkO4 

> k

+ O(r−8+  

> e

),

which is the stated equation. Now let us consider H 2 with |H 2|e ∼ r−2 

> e

such that 

PeH 2 = −Q(2)  

> e

(H 4, H 2) + Λ H 4 + ∑

> k

λkO4

> k

.

It exists by Lemma A.5 in the appendix (one checks that there is no log term). Then, we see that Pe(h′ − H 2) = O(r−8+  

> e

) while h′ = O(r−2+  

> e

). By the theory of elliptic operators between weighted H¨ older spaces (see for 924 Tristan Ozuch instance [PR78] or [LM85]), we therefore find that h′ − H 2 = K0

> r2
> e

+ O(r−6+  

> e

)for a constant symmetric 2-tensor K0, and consequently 

h′ = H 42 + O(r−4+  

> e

) = H 2 + K0

r2

> e

+ O(r−4+  

> e

)which proves the stated result. Let us now prove that if the obstructions λk of (20) vanish, then H 42 = 0. The idea is to use the uniqueness of h2, and show that Lr∂ r h2 satisfies the same equation. Indeed, we have: 0 = Lr∂ r

(Peh h2 − Λeh ) = Q(2)  

> eh

(Lr∂ r eh , h 2) + Peh Lr∂ r h2 − ΛLr∂ r eh ,

= Peh Lr∂ r h2 − 4Λ eh 

+ Q(2)  

> eh

(Lr∂ r eh − 2eh , h 2) − Λ( Lr∂ r eh − 2eh )(27) 

Remark 2.4. In the last line, we used the fact that Q(2)  

> eh

(eh , h 2) + Λ eh =0, which comes from the (Bianchi-free version of ) the identity Ric( sg ) = Ric( g) as 2-tensors for all s > 0. This implies Dg Ric( g) = 0 for all g and differentiating again at g in the direction h gives: 

D2 

> g

Ric( h, g ) + Dg Ric( h) = 0 .

We use this formula with g = eh , h = h2 and use the assumption that 

Deh Ric( h2) = Peh h2 = Λ eh because the λk vanish. 

In (27), we recognize −2o1 = Lr∂ r eh − 2eh . Let us show that the last term vanishes. Using [Biq16, Lemme 3], we find for c = 0, 

Q(2)  

> eh

(o1, h 2) − Λo1 = c ∑

> j

R+1j(H2)oj

and by [Biq13], if λ1 = λ2 = λ3 = 0, then, R+11 (H2) = R+12 (H2) = R+13 (H2) = 0, hence, 

Q(2)  

> eh

(o1, h 2) − Λo1 = 0 .

There remains Peh Lr∂ r h2 = 4Λ eh in (27). Since Lr∂ r h2 ∼ L r∂ r H2 = 4 H2

at infinity, we find the same first two equalities of (20) up to a constant 4. Since 4 h2 is the unique solution up to the addition of an element of O(eh ), we find that Lr∂ r h2 = 4 h2 + O(r−4 

> e

). The point is now that by homogeneity, Lr∂ r H 42 = 0 hence Lr∂ r h2 =4H2 + O(r−4 

> e

), and consequently h2 = H2 + O(r−4 

> e

). Higher order obstructions to the desingularization 925 

Remark 2.5. Let us note that the vanishing of H 42 is dependent on the coordinate system we consider for Eguchi-Hanson metric. It seems that the crucial property if these coordinates we use here is that the vector field r∂ r

is harmonic. Since we will always take eh in the coordinates of (10) , we will always have H 42 = 0 as long as the λk vanish. 

Later on, we will consider deformations of our orbifold as well and we will need to consider metrics which are not quite asymptotic to our target Euclidean metric, but a nearby one, i.e. e+H0 for some constant 2-tensor H0.Similarly, let us consider coordinates in which we have go = e + H0 +

H2 + O(r4

> e

) for H0 a traceless constant 2-tensor and let us denote ψ : R4/

Z2 → R4/Z2 a linear isomorphism for which ψ∗e = e + H0, in order to extend H2 to ψ∗eh ζ ±.

Remark 2.6. Here, by ψ∗eh ζ ±, we really mean the same diffeomorphism applied to eh = e + ∑ 

> k2

˜Hk(θ)r−2k in the polar coordinates θ ∈ RP 3 and 

r ∈ [0 , +∞) as in [Kro89a, Proposition 3.14], where (R4/Z2, e) = ( R+ ×

RP 3, dr 2 + dr 2gRP 3). The metric has to be “closed-up” by a different S2 at 

ψ(0) = 0 .

Then the obstructions are: (28) λk(ζ±) = c

〈

R±(ψ∗H2)ζ±, ζ ±

> (k)

〉

.

We will moreover need to extend constant 2-tensors to our Eguchi-Hanson metrics. 

Lemma 2.7. Let H0 be a constant 2-tensor on R4/Z2, i.e. constant on R4.Then, there exists a unique 2-tensor h0 on T ∗S2 satisfying: 

(29) 

⎧⎪⎨⎪⎩

Peh h0 = 0 ,h0 = H0 + H 40 + O(r−6+ ) for all  > 0

h0 ⊥L2(eh ) O(eh ).

Proof. Let H0 = LX1e be a constant symmetric 2-tensor with X1 a linear vector field. Then, since PeH0 = 0, for χ a cut-off function supported in a neighborhood of infinity of eh , we have Peh (χH 0) = O(r−6 

> e

), and an integration by parts against the ok proves that Peh (χH 0) ⊥ O(eh ) and there is no obstruction to finding h′′ with Peh (χH 0 + h′′ ) = 0 and h′′ = O(r−4+  

> e

)for all  > 0, see [Biq13, Proposition 2.1]. This lets us find a solution h0 to (30) Peh h0 = 0 , with h0 = H0 + O(r−4 

> e

).926 Tristan Ozuch with Beh h0 = 0, tr eh h0 = 0 by the maximum principle since tr eh Peh = 

> 12

∇∗

> eh

∇eh tr eh and Beh Peh = Beh δ∗

> eh

Beh = 12 ∇∗

> eh

∇eh Beh . We can make h0

unique by additionally assuming: h0 ⊥ O(eh ) and we find a development: (31) h0 = H0 + H 40 + O(r−6+  

> e

) with |H 40 |e ∼ r−4 

> e

.

The L2-product between h0 and o ∈ O(eh ) is a priori ill-defined because 

o = O(r−4) and h0 = O(1), but since the coefficients of the leading terms re-stricted to spheres {r = cst } belong to different eigenspaces of the Laplacian on RP 3, this is therefore well-defined. 

Remark 2.8. We can prove that we have h0 = Lx1eh for some vector field 

x1 satisfying 0 = Beh Lx1eh = ∇∗

> eh

∇eh x1 and x1 = X1 + O(r−3+  

> e

). We however do not have any application for this at the moment. 

The link between the next asymptotic term H 42 of the Einstein modulo obstructions deformation h2 = H2 + H 42 + . . . of Lemma 2.3 and the de-velopment of h0 = H0 + H 40 + . . . is given by the following integration by parts: 0 = 

∫

> N

〈Peh h2 − Λeh − ∑

> k

λkok, h 0

〉

> eh

dv eh 

=

∫

> N

〈Peh h2, h 0〉eh dv eh 

=

∫

> N

〈h2, P eh h0〉eh dv eh 

+ 12 lim 

> r→+∞

∫

> {re=r}

〈∇ ∂re (h2), h 0〉eh − 〈 h2, ∇∂re h0〉eh dv {re=r}

0 = − 3

∫

> S3/Z2

〈H2, H 40 〉edv S3/Z2 −

∫

> S3/Z2

〈H 42 , H 0〉edv S3/Z2,(32) where we used that by homogeneity, we have ∇∂re H2 = 2 

> re

H2, ∇∂re H0 = 0, 

∇∂re H 42 = − 2 

> re

H 42 and ∇∂re H 40 = − 4 

> re

H 40 .Finally, if λk = 0, using the fact that H 42 = 0 from Lemma 2.3, we find: (33) 

∫

> S3/Z2

〈H2, H 40 〉edv S3/Z2 = 0 Higher order obstructions to the desingularization 927 

2.1.2. A first obstruction on the orbifold. We have a similar result for the extension of tensors on the orbifold. Consider an infinitesimal Ricci-flat variation of eh ζ ±

> j

in the direction om = om(ζ± 

> j

) ∈ O(eh ζ ±

> j

) where om(ζ± 

> j

)is the 2-tensor defined in (16) and Remark 1.20. In particular, om has a development om = O4 

> m

+ O(|ζ|3r−8 

> e

) with |O4

> m

|e ∼ | ζ|r−4.

Lemma 2.9. We define o4 

> m

for m ∈ { 1, 2, 3} some solutions to the following equation 

(34) 

⎧⎪⎨⎪⎩

Poo4 

> m

∈ O(go),

o4 

> m

= O4 

> m

+ O(r−2−o ) for any  > 0 at the singular point j

o4 

> m

⊥ O(go).

They are determined up to the kernel of Pgo in O(r−2 

> e

) at the singular points and this choice will not alter the result at this level of precision. Proof. Let us consider a cut-off function χ on Mo supported in a small enough neighborhood of a singular point p. We have Pgo(χO 4

> m

) = O(r−4), hence there exists a 2 tensor |O4

> m, 2

| = O(r−2−) so that 

Pgo(χ(O4 

> m

+ O4

> m, 2

)) = O(r−2−).

Finally, using the Fredholm properties of Pgo proven in [Ozu19b], there exists 

|h′| = O(r−) for all  > 0 so that: 

Pgo(χ(O4 

> m

+ O4

> m, 2

) + h′) ∈ O(go).

Now, we can uniquely choose it by imposing ( χ(O4 

> m

+ O4

> m, 2

) + h′) ⊥L2(go)

O(go), where the L2 product is a priori ill-defined as in the proof of Lemma 2.7, but makes sense via the orthogonality of the different eigenspaces of the Laplacian on RP 3.

Proposition 2.10. Let us denote (vl)l an orthonormal basis of O(go). Con-sider the development of the symmetric 2-tensor h2 = H2 + H 42 + O(r−6+  

> e

)

of (22) (again, we will omit the dependence in ζ±). For ζ± ∈ Ω± and the symmetric 2-tensor H 4 = H 4(ζ±) with PeH 4 = 0 

and BeH 4 = 0 , there exists (h4, (νl)l) with a symmetric 2-tensor h4 and real 928 Tristan Ozuch 

numbers (νl)l on Mo satisfying the following equations 

⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩

Poh4 = ∑

> l

νlvl + ∑

> k

λko4

> k

,h4 = H 4 + H 42 + O(|ζ|2r−o ) for any  > 0 at the singular point jh4 ⊥ O(go).

(35) 

We moreover have the following value for the obstruction when λk = 0 

for k ∈ { 1, 2, 3}

(36) νl = 3 

∫

> S3/Z2

〈H 4, V l, 2〉edv S3/Z2.

where we have vl = Vl, 0 + Vl, 2 + O(r4

> e

) with |Vl,m |e ∼ rm 

> e

.

Remark 2.11. The next term in the development of h4 is H 44 with |H 44 |e =

O(r 

> e

+ r− 

> e

) for any  > 0 (it will typically be logarithmic in re) for which we have 

h4 = H 4 + H 42 + H 44 + O(|ζ|2r2−o ).

It satisfies 

(37) PeH 44 + Q(2)  

> e

(H 4, H 4) + Q(2)  

> e

(H 42 , H 2) + Q(3)  

> e

(H 4, H 2, H 2) = 0 .

for Q(m) 

> e

the m-linear terms of the development of h  → (Ric −Λ+ δ∗

> e+h

Be)( e+

h) around h = 0 . The equality (37) is exactly the equation satisfied by the next term in the development of h4 defined in (21) or (23) . That was what made h4 non unique: one could add any element of the kernel of Peh asymp-totic to a constant 2-tensor to it. We can make it unique (and still existing) by imposing that we have for the above H 44 :

h4 = H4 + H 44 + O(r−2+ ).

Proof. Consider χ a cut-off function supported in the neighborhood of the singular point j ∈ Mo. From PeH 4 = 0, rk

> e

|∇ k

> e

(go − e)|e = O(r2

> e

) and using (26), we find 

Po(χ(H 4 + H 42 )) − ∑

> k

λko4 

> k

∈ r−2 

> o

Cαβ (go)Higher order obstructions to the desingularization 929 for 0 < β < 1 where the norms are defined in the Appendix A. Moreover, by integration by parts and using o4 

> k

⊥L2(go) O(go), we find (38) 

∫

> Mo

〈Po(χ(H 4 + H 42 )) , vl

〉

> go

dv go

=

∫

> Mo

〈χ(H 4 + H 42 ), P o(vl)〉

> go

dv go

+ 12 lim 

> r→0

∫

> {ro=r}

〈∇ ∂ro (χH 4), vl〉go − 〈 χH 4, ∇∂ro vl〉godv {ro=r}

+ 12 lim 

> r→0

∫

> {ro=r}

〈∇ ∂ro (χH 42 ), vl〉go − 〈 χH 42 , ∇∂ro vl〉godv {ro=r}

=3 

∫

> S3/Z2

〈H 4, V l, 2〉edv S3/Z2 +

∫

> S3/Z2

〈H 42 , V l, 0〉edv S3/Z2

Indeed, since once restricted to S3/Z2, the coefficients of H 4 and Vl, 0 are eigenfunctions of the Laplace-Beltrami operator and associated to different eigenvalues, the product against the first asymptotic term Vl, 0 vanishes. Note that this also justifies the orthogonality of (35). For the second term Vl, 2,we use the homogeneity of H 4 and Vl, 2 which yield ∇∂re H 4 = − 4 

> re

H 4 and 

∇∂re Vl, 2 = 2 

> re

Vl, 2 and the above value. Thanks to the Fredholm properties of Po proved in [Ozu19b], we have the stated result. When λk = 0 for k ∈ { 1, 2, 3}, then, we can use Lemma 2.3, hence plug 

H 42 = 0 into (38) and find the expected value. Similarly, if ( Mo, go) has several R4/Z2 singularities, denote h4 

> j

the sym-metric 2-tensors of (35) asymptotic to H 4(ζ± 

> j

) + H 42 (ζ± 

> j

) at the singular point j. The symmetric 2-tensor 

h4 := ∑ 

> jsingular

h4

> j

satisfies 

⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩

Poh4 = ∑

> k

νlvl + ∑

> j

∑

> k

λjko4

> j,k

,h4 = H 4(ζ± 

> j

)+ H 42 (ζ± 

> j

)+ O(r−o ) for any  > 0 at each singular point jh4 ⊥ O(go).

(39) 930 Tristan Ozuch 

2.1.3. First variation of the initial obstruction. By [Ozu19b, Propo-sition 5.17], around a singular point j, in coordinates where go = e + Hj, 2 +

O(r4

> e

), for v ∈ O(go) small enough and with v = Vj, 0 + Vj, 2 + O(r4

> e

) in the same coordinates, we have 

gv = ( e + ˜Vj, 0) + ( Hj, 2 + ˜Vj, 2) + O(r4

> e

),

with ˜Vj, 0 = Vj, 0 + O(‖v‖2

> L2(go)

) and ˜Vj, 2 = Vj, 2 + O(‖v‖2

> L2(go)

r2

> e

). We also de-note ψ( ˜Vj, 0) : R4/Z2 → R4/Z2 the linear isomorphism for which ψ( ˜Vj, 0)∗e =

e + ˜Vj, 0.For k ∈ { 1, 2, 3} and a singular point j, and ζ = ( ζj)j with ζj ∈ R3\{ 0},we will denote λjk(ζ, v ) the real numbers of (28) obtained for H0 = ˜Vj, 0 and 

H2 = Hj, 2 + ˜Vj, 2, that is for c > 0, (40) λjk(ζ, v ) = c〈R±(ψ( ˜Vj, 0)∗(Hj, 2 + ˜Vj, 2))ζ± 

> j

, ζ ±

> j, (k)

〉.

We find a link between the variations of the first obstruction λ1 on the Eguchi-Hanson metric and the first obstructions νl on the orbifold. 

Corollary 2.12. Consider (Mo, go) an integrable Einstein orbifold with only 

R4/Z2 singularities. Consider also a small enough v ∈ O(go), the orthonor-mal basis (vl)l of Proposition 2.10 and the Einstein deformation gv of go of Definition 1.10. Assume that we have λjk(ζ, 0) = 0 for all k, j .Then, for some constant C ∈ R∗, we have the following control: 

(41) ∑ 

> jsingular

|ζj|λj

> 1

(ζ, v ) = C ∑

> l

〈v, vl〉νl(ζ, 0) + O(‖v‖2

> L2

|ζ|2),

where the νl are real numbers of (39) , and where |ζ| = max j |ζj|.Proof. Let ( Mo, go) be like in the statement above and consider a small enough v ∈ O(go) and gv the Einstein deformation of go of Definitions 1.9 and 1.10, denote λj

> 1

(ζ, v ) the constant in (40) above. Our goal is to show that the first variation of v  → ∑ 

> j

|ζj|λj

> 1

(ζ, v ) around ( ζ, 0) is proportional to ∑

> k

〈v, vl〉νl(ζ, 0). From the expression (40) and the formula [Biq13, Proposition 3.2], we see that for the singular point j, the first variation of v  → ∑ 

> j

|ζj|λj

> 1

(ζ, v ) is 

∑

> j

|ζj|

∫

> S3/Z2

〈V2, O 4

> j, 1

〉

> e

dv S3/Z2,Higher order obstructions to the desingularization 931 up to a multiplicative constant. Using the equality H 4(ζ± 

> j

) = |ζj| 

> 2

O4

> j, 1

(ζ± 

> j

)together with (39), we see that this equals ∑

> k

〈v, vl〉νl up to a multiplicative constant and the estimate (41) follows. 

2.1.4. Values for the second obstruction. Let H2 be a quadratic sym-metric 2-tensor with PeH2 = Λ e, and H4 with |H4|e ∼ r4 

> e

and PeH4 =ΛH2 −Q(2)  

> e

(H2, H 2), and recall the notation R+(H2) as the common selfdual part of the curvature at re = 0 of Riemannian metrics with a development 

e + H2 + O(r3

> e

). As seen above, we have λk := c〈R+(H2)( ω+1 ), ω +

> k

〉 for the 

λk of (20) and c > 0. In particular, if for all k, λk = 0, then we have 

R+(H2) = 

⎡⎣

0 0 00 R22 R23 

0 R32 R33 

⎤⎦ ,

and in this case, for a positive constant C > 0, by [Biq16, Lemme 9] we have (42) μ1 = C det 

[R22 R23 

R32 R33 

]

Remark 2.13. If Ric( H2) = 0 , then we have tr R+(H2) = 0 and therefore 

det 

[R22 R23 

R32 R33 

]

 0

with equality if and only if R+(H2) = 0 .

In general, we might only know that the λk are small rather than exactly vanishing. We still have the following estimate. 

Lemma 2.14. Let H2 and H4 be homogeneous symmetric 2-tensors as above. We have 

(43) μ1 = C det 

[R22 R23 

R32 R33 

]

+ O( ∑ 

> k

|λk| · | r−2 

> e

H2|ge

).

Proof. According to [Biq16, Lemma 7], we have 

R+(H2) = 

⎡⎣

c−1λ1 c−1λ2 c−1λ3

c−1λ2 R22 R23 

c−1λ3 R32 R33 

⎤⎦ .932 Tristan Ozuch Exactly like in the proof of [Biq16, Lemma 8], we use the expression of 

Q(2)  

> e

given in [Biq16, Lemma 3] in order to express μ1. The value of μ1 is a quadratic form in the coefficients of R+(H2). It is composed of products of a λk and a λj, products of the λk with the remaining Rij , and its last part involving R22 , R23 , R32 and R33 is 

C det 

[R22 R23 

R32 R33 

]

,

as proven in [Biq16, Lemma 8]. Since all of the λk as well as the Rij are linear in H2 and are therefore are controlled by |r−2 

> e

H2|ge. We deduce the stated estimate. For another Eguchi-Hanson metric eh ζ ±, one has similar estimates with the matrix expression of R+(H2) in the basis ( ζ±, |ζ| · ζ±

> (2)

, |ζ| · ζ±

> (3)

) on R · ζ±

and its orthogonal. Note that in that case, we have λk ∼ | ζ| and μ1 ∼ | ζ|2.

2.2. Approximate Einstein metrics and obstructions 

Let ( Mo, go) be a compact Einstein orbifold with integrable Einstein de-formations and only R4/Z2 singularities. For v ∈ O(go) small enough and 

ζ = ( ζ± 

> j

)j with ζj ∈ R3\{ 0}, we recall the notations: 1. gv the Einstein deformation of go of Definition 1.10, 2. for a singular point j, symmetric 2-tensors hj, 2(v, ζ ) and hj, 4(v, ζ ) of (22) and (23) by extending the asymptotic terms of gv on eh ζ ±

> j

and 3. a symmetric 2-tensor h4(v, ζ ) of (39) extending the r−4 term of eh ζ ±

> j

on ( Mo, gv). 4. gD or gD for the na¨ ıve desingularization and rD the associated radial parameter, see Definitions 1.23 and 1.22 

Definition 2.15 (Approximate Einstein modulo obstructions metric gAζ,v ).

We define an approximate Einstein modulo obstructions metric gAζ,v as the na¨ ıve gluing of the metrics eh ζ ±

> j

+ hj, 2(v, ζ ) + hj, 4(v, ζ ) at the singular points 

j of (Mo, gv + h4(v, ζ )) .

There exists C = C(go) > 0 such that we have 

• rkD|∇ k

> eh ζ±
> j

h2|  Cr 2

> D

,

• rkD|∇ k

> eh ζ±
> j

h4|  Cr 4

> D

, and Higher order obstructions to the desingularization 933 

• rkD|∇ k

> eh ζ±
> j

h4|  C|ζ|2r−4 

> D

,we have the following controls: on Mo() (defined in (5)) (44) rkD

∣∣∇k(gAζ,v − gDζ,v )∣∣gDζ,v 

 C|ζ|2,

and on the connected component of M \Mo() containing the singular point 

j ∈ S:

rkD

∣∣∇k(gAζ,v − gDζ,v )∣∣gDζ,v 

 C

(

1{rD>|ζj| 14 }|ζj|2r−4 

> D

+ 1{rD<2|ζj| 14 }r2

> D

)

.(45) where 1A is the indicator function for A.We now approximate the kernel of the linearization of the Einstein op-erator at gAζ,v .

Definition 2.16 (Approximate obstructions ˜O(gAζ,v )) . We define ˜O(gAζ,v )

the linear space spanned by the infinitesimal variations of (v, ζ )  → gAζ,v .More precisely for the element ok ∈ O(eh ζ ±

> j

) with ok = ∂ζj, (k)eh ζ ±

> j

, we define 

˜ok := ∂ζj, (k)gAζ,v 

and, for w ∈ O(gv), we define ˜w the associated infinitesimal deformation of v  → gAζ,v .

Remark 2.17. As in Remark 1.25, the space ˜O(gAζ,v ) is very close to the space ˜O(gDζ,v ) of [Ozu19b] and even yields better estimate. The results of [Ozu19b] therefore hold when replacing ˜O(gDζ,v ) by ˜O(gAζ,v ).

We have the following estimates which show that the space ˜O(gAζ,v ) is an approximate L2-cokernel of the linearization of the Einstein equation. 

Lemma 2.18. For ˜ok ∈ ˜O(gAζ,v ) and ˜w ∈ ˜O(gAζ,v ) as in Definition 2.16 above, we have for any symmetric 2-tensor h on M, 

∣∣〈PgDζ,v h, ˜ok〉L2(gDζ,v )

∣∣  C|ζ| · ‖ h‖C 2,α β, ∗ (gDζ,v )‖ok‖L2(eh ζ± 

> j
> )

and (46) 

∣∣〈PgDζ,v h, ˜w〉L2(gDζ,v )

∣∣  C|ζ| · ‖ h‖C 2,α β, ∗ (gDζ,v )‖w‖L2(go).(47) 934 Tristan Ozuch 

Proof. By integration by parts and symmetry of PgDζv 

on the closed mani-fold M , it is equivalent to control 

∫

M

〈

h, P gDζ,v ˜ok

〉

gDζ,v 

dv gDζ,v and 

∫

M

〈

h, P gDζ,v ˜w

〉

gDζ,v 

dv gDζ,v .

On the region where gDζ,v = eh ζ ±

> j

, we have PgDζ,v ˜ok = 0. There remains the region where gDζ,v = gv on which by differentiating (39) with respect to 

ζ ±

j , we find 

PgDζ,v ˜ok = ∑

l

∂ζj, (k)νlwl + ∑

i,m 

∂ζj, (k)(λmi o4

i,m ),

where ( wl)l denotes an orthonormal basis of O(gv), and where the ∂ζj, (k)νl

are the derivatives of the νl = νl(v, ζ ) of (39) in the direction ζj, (k). Given the expressions (24), (16) and (39), that gives for some C = C(go) > 0, 

∥∥PgDζ,v ˜ok

∥∥L2(eh ζ±

> j

)  C|ζ| · ‖ ok(ζ±

j )‖L2(eh ζ±

> j

).

We find that 

∫

{rD>2|ζ ± 

> j

|1/4}

〈

h, P gDζ,v ˜ok

〉

gDζ,v 

dv gDζ,v  C|ζ| · ‖ h‖C 0(gDζ,v )‖ok(ζ±

j )‖L2(eh ζ±

> j

).

Finally, on the gluing region where |ζ±

j | 14 < r D < 2|ζ±

j | 14 , we have for all 

l ∈ N and Cl > 0

rlD|∇ l(gDζ,v − eh ζ ±

> j

)|gDζ,v  Cl

(|ζ±

j |2r−4

D + r2

D

)

and 

rlD|∇ l(˜ ok − ok)|gDζ,v  C(|ζ±

j |4r−8

D + |ζ±

j |2r−2

D

),

and we find that on the gluing region where |ζ±

j | 14 < r D < 2|ζ±

j | 14 , we have 

∣∣∣PgDζ,v ˜ok

∣∣∣gDζ,v 



∣∣∣PgDζ,v (˜ ok − ok)

∣∣∣gDζ,v 

+ ∣∣(PgDζ,v − Peh ζ±

> j

)(ok)∣∣gDζ,v 

 C|ζ±

j | · ‖ ok‖L2(eh ζ±

> j

).

We therefore globally find the estimate (46). Higher order obstructions to the desingularization 935 For the second estimate, note first that on the region where gDζ,v = gv,we have 

PgDζ,v w = 0 ,

and by a similar argument to the above one, by differentiating (22) and (23), on each region where gDζ,v = eh ζ ±

> j

, we have 

PgDζ,v ˜w = ∑

> k

∂w(λk + μk)ok(ζ± 

> j

),

and we find that there exists C = C(go) > 0 such that |∂w(λk + μk)|  C|ζ|.Together with a control on the gluing region like the above one, one obtains the estimate (47). 

Proposition 2.19. Assume that there exists an Einstein metric gζ,v satis-fying: 1. ΦgDζ,v (gζ,v ) = 0 ,2. gζ,v − gAζ,v ⊥ ˜O(gAζ,v )

3. ‖gζ,v −gAζ,v ‖C 2,α β, ∗ (gDζ,v ) <  for  > 0 small enough determined in [Ozu19b] depending only on go.Then, we actually have for all l for the obstructions of (35) :

(48) νl = O(|ζ| 52 ),

and for each j, and all k ∈ { 1, 2, 3} for the obstructions of (22) and (23) :

(49) λjk + μjk = O(|ζj| 52 ).

Proof. Let us denote π ˜O(gAζ,v )⊥ the L2(gAζ,v )-orthogonal projection on ˜O(gAζ,v )⊥. Thanks to the obstruction result of [Ozu20t, Proposition 5.1], we only have to understand the value of ∥∥π ˜O(gAζ,v )⊥ΦgDζ,v (gAζ,v )∥∥r−2  

> DCα(gDζ,v )

, in order to control both ‖gAζ,v − gζ,v ‖C 2,α β, ∗ (gDζ,v ) and the obstructions, where the norms are defined in Definition A.3 in the Appendix. The estimate on the different Eguchi-Hanson regions has been done in [Biq13, Section 14]. There remains to understand the orbifold region. Using the definition of h4, we control the first variation 

Pgoh4 = ∑

> l

νlvl + ∑

> j
> 3

∑

> k=1

λjko4

> j,k

,936 Tristan Ozuch and on the region where gAζ,v = go + h4 with h4 = O(|ζ|2r−4 

> D

), we have: 

ΦgDζ,v (gAζ,v ) = ∑

> l

νlvl + ∑

> j
> 3

∑

> k=1

λjko4 

> j,k

+ O(|ζ|4r−10  

> D

)which is exactly analogous to the estimate [Biq13, (108)]. The gluing region is treated exactly as in [Biq13, Section 14] for instance, see also the above proof of Lemma 2.18. We conclude like in [Biq13, (109)] that (50) ∥∥π ˜O(gAζ,v )⊥ΦgDζ,v (gAζ,v )∥∥r−2   

> DCα(gDζ,v )

 C|ζ| 32 − β 

> 4

.

We conclude exactly like in order to prove [Biq13, (112)] that we have the stated control (see also [Ozu20t, Proposition 5.1]). 

2.3. A new obstruction to the desingularization of Einstein orbifolds 

By [Ozu19a, Ozu19b], we know that Einstein metrics which are close to an Einstein orbifold ( Mo, go) result from a gluing-perturbation procedure. To prove that it cannot be desingularized, we just need to prove that an obstruction to this procedure does not vanish. 

2.3.1. Approximate obstructions. Let us denote ζ = t · φ with t =(tj)j = ( |ζj|)j and φ = ( φj)j = (ζ± 

> j

/|ζj|)

> j

. By Proposition 2.19, we find the following estimate for any singular point j, any k ∈ { 1, 2, 3}:

tjλjk(φj, v ) + t2 

> j

μjk(φj, v ) = O(t 52

> max

), and (51) 

νl(t · φ, v ) = O(t 52

> max

), for each l,(52) where the λjk(φj, v ) and μjk(φj, v ) and νl(t · φ, v ) are the constants of Lemma (22), (23) and (39) for each eh ζ ±

> j

associated to the development of gv at the singular point j.Our goal is to prove that for all j, both all of the λjk and μj 

> 1

have to vanish when t → 0. The main concern is to rule out the compensation of 

t2 

> j

μj 

> 1

by tjλj 

> 1

just like in the desingularization case of [Biq13, Theorem 14.3]. Higher order obstructions to the desingularization 937 

Proof of Theorem 0.2 and Proposition 0.4. Let us consider (Mo, go) ∈

E(M )GH for M having the topology of Mo desingularized by T ∗S2 in an orientation at each of its singular point and assume that go only has inte-grable Einstein deformations (see Definition 1.10). Let us assume that there exists a sequence of Einstein metrics ( M, gn)n desingularizing ( Mo, go). We will discuss at the end of the proof in which situation we shall assume that this sequence is nondegenerate, transverse or stable. Then, by [Ozu19a, Ozu19b], there exists a sequence of na¨ ıve desingu-larizations gDζn,v n such that the metrics ( M, gn) are Einstein perturbations of gDζn,v n with ζn = ( ζn,j )j. We will use the notations tn = ( tn,j )j, with 

tn,j = |ζn,j | > 0 and φn = ( φn,j )j, φn,j = ζ ± 

> n,j
> |ζn,j |

satisfying ζ± 

> n,j

= tn,j · φn,j ,and we will denote tn · φn = ( tn,j φn,j )j.By compactness, up to taking a subsequence, we can assume that for any 

j, φn,j → φ∞,j on the sphere while tn → 0 and vn → 0 since by assumption the limit is go.Denote λjk(φn,j , v n) and μjk(φn,j , v n) the real numbers of (20) and (21) for these configurations. According to (51), we have the following controls: for all j and k,(53) tn,j λjk(φn,j , v n) + t2

> n,j

μjk(φn,j , v n) = O(t 52

> n, max

).

The first obstruction of [Biq13, Ozu19b] means that at the limit, for any singular point j, we have λjk(φ∞,j , 0) = 0 for k ∈ { 1, 2, 3}, there exists a basis of the selfdual or anti-selfdual (depending on the orientation of the gluing) 2-forms starting with φ∞,j = lim j→+∞ ζ±

> n,j

/|ζn,j | in which we have (54) R±

> go

(j) = 

⎡⎣

0 0 00 aj 

> 2

00 0 aj

> 3

⎤⎦ .

Our goal is to prove that for all j we have, μj

> 1

(φ∞,j , 0) = 0. By Lemma (2.14), this will then imply that either aj 

> 2

= 0 or aj 

> 3

= 0 in (54). Assume towards a contradiction that both aj 

> 2

= 0 and aj 

> 3

= 0. Let us use the variations of the φ  → λjk(φ, 0) computed in [Biq13, Lemma 12.2] at 

φ∞,j , we first have the controls: 

λj

> 1

(φn,j , 0) = O(|φn,j − φ∞,j |2),(55) 938 Tristan Ozuch because the first variation of the smooth map φ  → λj

> 1

(φ, 0) vanishes at φ∞,j .Similarly since we assumed towards a contradiction that aj 

> 2

= 0 and aj 

> 3

= 0, there exists c > 0 depending on ( aj

> 2

, a j

> 3

), so that (56) ∣∣(λj

> 2

(φn,j , 0) , λ j

> 3

(φn,j , 0) )∣ ∣  c|φn,j − φ∞,j |,

since the first order variations of φ  → (λj

> 2

(φ, 0) , λ j

> 3

(φ, 0)) is invertible at 

φ∞,j . For the variations induced by vn ∈ O(go), for any k ∈ { 1, 2, 3}, from the expression (40), we have 

|λjk(φn,j , v n) − λjk(φn,j , 0) | = O(‖vn‖L2(go)).

For the μjk, we have the control μjk(φn,j , v n) = μjk(φ∞,j , 0)+ O(|φn,j −φ∞,j |)+ 

O(‖vn‖L2(go)). Therefore for k = 2 or k = 3, (53) gives 

tn,j λjk(φn,j , v n)(57) = −t2

> n,j

(μjk(φ∞,j , v n) + O(|φn,j − φ∞,j |) + O(‖vn‖L2(go))) + O(t 52

> n, max

).

At any singular point j, we must therefore have ∣∣(λj

> 2

(φn,j , v n), λ j

> 3

(φn,j , v n))∣ ∣ =

O(tn,j + t5/2 

> n, max
> tn,j

), and by (56), this implies that |φn,j − φ∞,j | = O(‖vn‖L2(go) +

tn,j + t5/2

> n, max
> tn,j

).1. In the transverse (Definition 1.27) situation, where we have tn, max =

O(tn,j ) and ‖vn‖L2(go) = o(tn, min ). By rewriting (53) for k = 1, in-cluding the bound (55) with the new information that |φn,j − φ∞,j | =

O(tn,j ) and using |λ1(φ∞,j , v n,j ) − λ1(φ∞,j , 0) | = O(‖vn,j ‖L2(go)) = 

o(tn, min ), we consequently find 

o(t2

> n,j

)+ t2

> n,j

(μj

> 1

(φ∞,j , 0)+ O(|φn,j −φ∞,j |)+ O(‖vn‖L2(go))) = O(t 52

> n, max

),

(58) and therefore μj

> 1

(φ∞,j , 0) = 0. 2. As proven in [Biq17, Proof of Theorem 3], and thanks to the esti-mate (50), we know that the linearization of Ric in Bianchi gauge at 

gn denoted Pgn, satisfies for some on,j,k ∈ L2(gn) (constructed from 

on,j,k ∈ O(eh ζn,j )) for k ∈ { 1, 2, 3}:

〈Pgnon,j, 1, o n,j, 1

〉 

> L2(gn)

= o(1) · ‖ on,j, 1‖L2(gn), and Higher order obstructions to the desingularization 939 

〈Pgnon,j,k , o n,j,k 

〉 

> L2(gn)

= ( ajk + o(1)) · ‖ on,j,k ‖L2(gn),

for k ∈ { 2, 3}. That means that the metric cannot be stable as in Definition 1.11 if aj 

> 2

= −aj 

> 3

= 0. Consequently, we necessarily have 

aj 

> 2

= aj 

> 3

= 0 for stable Ricci-flat desingularizations. 3. If the orbifold satisfies O(go) = {0} and only has one R4/Z2 singular-ity, then the transversality assumption is automatically satisfied and the result follows. 4. In the Ricci-flat situation, then the nondegeneracy assumption is enough because we can use Remark 2.13. Indeed, first, the nonde-generacy assumption gives |φn,j − φ∞,j | = o(t 12

> n,j

), hence |λ1(φn,j , 0) | =

o(tn,j ) by (55); second from (41), we moreover have a better control over the sum of the t2 

> j

λj

> 1

(ζ, v ), namely: 

∑

> j

t2 

> j

λj

> 1

(φn,j , v n) − t2 

> j

λj

> 1

(φn,j , 0) (59) = O(t 52

> max

‖vn‖L2(go)) + O(t2max ‖vn‖2

> L2(go)

).

which together with (55) and (51) and using ‖vn‖2 

> L2(go)

= o(tn,j ) yields the estimate 

∑

> j

o

(

t3 

> n,j

+ t 52

> n, max

t 12 

> n,j

+ t2

> n, max

tn,j 

)

+ ∑

> j

t3

> n,j

(μj

> 1

(φ∞,j , 0) + O(|φn,j − φ∞,j |) + O(‖vn‖L2(go)))

= O(tn,j t 52

> n, max

),

which with tn, max = O(tn,j ) from the nondegeneracy assumption im-plies that ∑

> j

μj

> 1

(φ∞,j , 0) = 0 and since all of the μj

> 1

(φ∞,j , 0) are nonpositive by Remark 2.13, for any j, we have μj

> 1

(φ∞,j , 0) = 0. 5. Similarly for Einstein but non Ricci-flat orbifolds with only one sin-gularity, we use (41) as in the previous point since there is only one term in the sum. 940 Tristan Ozuch 

Remark 2.20. The estimate (52) also implies that: for any l, one has 

lim  

> n→+∞

νl

( tn

tn, max 

· φn , v n

)

= lim 

> n→+∞

νl(tn · φn , v n)

t2

> n, max

= 0 

which has an interpretation in terms of curvature by (39) and (41) .

Remark 2.21. The same obstruction result also holds if we consider desin-gularizations by smooth Ricci-flat ALE of A1, Dk or Ek singularities by [Biq16, Lemme 9]. An obstruction is also satisfied for Ak singularities but it also involves derivatives of the curvature [Biq16, Lemme 12]. It also ex-tends to K¨ ahler Ricci-flat ALE manifolds by taking their hyperk¨ ahler finite cover. 

We also believe that the nondegeneracy assumption is purely technical. Understanding higher order obstructions should yield the following conjec-tural statement which already holds under a stability assumption. 

Conjecture 2.22. Let (Mn, gn)n be a sequence of compact smooth Ricci-flat metrics converging in the Gromov-Hausdorff sense towards a Ricci-flat orbifold (Mo, go) while bubbling Eguchi-Hanson metrics. Then the curvature of go at its singular points is either selfdual or anti-selfdual depending on the orientation of the Eguchi-Hanson metrics. 

3. Ricci-flat modulo obstructions desingularizations of T4/Z2

Let us now work with the flat orbifold T4/Z2. We will study the question of whether or not it is possible to desingularize it by Ricci-flat metrics obtained by gluing Eguchi-Hanson metrics in different orientations at its singular points. 

3.1. The orbifold T4/Z2 and its deformations 