---
retention_scope: session
part: 1
total_parts: 1
---

# An introduction to the Seiberg-Witten equations on symplectic manifolds

> Source: https://math.berkeley.edu/~hutching/pub/tn.pdf
> Fetched: 2026-10-09 12:30
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
  "source": "tavily",
  "source_url": "https://math.berkeley.edu/~hutching/pub/tn.pdf",
  "metadata": {
    "provenance_urls": [
      "https://math.berkeley.edu/~hutching/pub/tn.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Seiberg-Witten exceptional class every tame almost complex structure J-holomorphic subvariety current canonical class minimal symplectic 4-manifold"
      }
    ]
  },
  "declared_files": [
    {
      "url": "https://math.berkeley.edu/~hutching/pub/tn.pdf",
      "name": "tn.pdf",
      "label": "",
      "role": "neighbor_file_reference",
      "parent_url": "https://math.berkeley.edu/~hutching/pub/tn.pdf",
      "identity_bound": false,
      "primary_label": false,
      "download_eligible": false
    }
  ]
}
```

## Source description

Choose an ω-compatible J, and endow X with the Riemannian metric g given by (4.1). The almost complex structure gives a decomposition Λ∗T ∗X ⊗C = M p,q T p,q, where T p,q = ∧pT 1,0 ⊗∧qT 0,1 and T 1,0 (resp. T 0,1) is the holomorphic (resp.
antiholomorphic) part of T ∗X ⊗C.
Suppose a SpinC structure is chosen. Cliﬀord multiplication by ω, cl+(ω) : S+ →S+ splits S+ into ±2i eigenspaces. (In the local model of the second lecture, ω = dx1dx2+dx3dx4, so this claim follows from equation (2.10).) Let E be the −2i eigenspace. This is a line bundle on X. We deﬁne the canonical SpinC structure to be the one for which E is trivial. Thus the identiﬁcation SX →H2(X; Z) sends s to c1(E).
Here are some key facts about the spin bundles and the Cliﬀord action. [...] 33 An element e ∈H2(X; Z) corresponds to a SpinC structure with S+ = E ⊕K−1E where c1(E) = e, and K is the canonical bundle coming from an ω-compatible almost complex structure J. We can regard the Seiberg-Witten invariant as a map SW : H2(X; Z) →Z.
If we write ψ = √r(α, β) with α ∈C∞(E) and β ∈C∞(K−1E), write A = A0 + 2a, and choose µ = rω −iF + A0, then the Seiberg-Witten equations are ∂aα = −∂ ∗ aβ, F + a = −ir 2 (1 −|α|2 + |β|2)ω −r(αβ −αβ).
(5.1) We showed that any solution of these equations must satisfy the estimates Z  1 −2z r  |∇aα|2 + r(1 −|α|2)2  ≤2π[ω] · e, (5.2) Z 1 2|∇∗ aβ|2 + r 2|β|4 + r 4|β|2  ≤z r Z |∇aα|2. [...] (b) SW(c) = ±1.
(c) SW(e) = ± SW(c −e).
(d) If SW(e) ̸= 0, then 0 ≤[ω] · e ≤[ω] · c, and if eith

## Retrieved source content

Title: tn.pdf

URL Source: https://math.berkeley.edu/~hutching/pub/tn.pdf

Published Time: Fri, 08 Jun 2007 16:18:18 GMT

Number of Pages: 40

Markdown Content:
# An introduction to the Seiberg-Witten equations on symplectic manifolds ∗

## Michael Hutchings and Clifford Henry Taubes †

## Summer 1997 

The Seiberg-Witten equations are defined on any smooth 4-manifold. By appropriately counting the solutions to the equations, one obtains smooth 4-manifold invariants. On a symplectic 4-manifold, these invariants have a symplectic interpretation, as a count of pseudoholomorphic curves. This al-lows us to transfer information between the smooth and symplectic categories in four dimensions. In the following lectures, we will try to explain this story. In the first two lectures, we review some background from differential geometry, which will allow us to write down the Seiberg-Witten equations at the end of the second lecture. In the third lecture we define the Seiberg-Witten invariants and discuss their most basic properties. In the fourth lecture we compute the simplest of the Seiberg-Witten invariants on a symplectic 4-manifold. In the fifth lecture we relate the remaining Seiberg-Witten invariants in the symplectic case to pseudoholomorphic curves. 

# Contents 

1 Background from differential geometry 3

1.1 Vector bundles . . . . . . . . . . . . . . . . . . . . . . . . . . 31.2 Connections . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51.3 Metrics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

> ∗Based on the lectures of the second author at the 1997 Park City-IAS Summer Insti-tute.
> †Both authors are supported in part by grants from the National Science Foundation.

11.4 Curvature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81.5 Self-dual two-forms . . . . . . . . . . . . . . . . . . . . . . . . 9

2 Spin and the Seiberg-Witten equations 9

2.1 Principal bundles and associated bundles . . . . . . . . . . . . 92.2 Spin C structures . . . . . . . . . . . . . . . . . . . . . . . . . . 11 2.3 Some group theory . . . . . . . . . . . . . . . . . . . . . . . . 12 2.4 The spinor bundles . . . . . . . . . . . . . . . . . . . . . . . . 14 2.5 Clifford multiplication . . . . . . . . . . . . . . . . . . . . . . 14 2.6 The spin connection . . . . . . . . . . . . . . . . . . . . . . . 15 2.7 The Dirac operator . . . . . . . . . . . . . . . . . . . . . . . . 16 2.8 The Seiberg-Witten equations . . . . . . . . . . . . . . . . . . 17 

3 The Seiberg-Witten invariants 18 

3.1 Gauge transformations . . . . . . . . . . . . . . . . . . . . . . 18 3.2 Basic properties of the moduli space . . . . . . . . . . . . . . 19 3.3 Why the conditions on b2+? . . . . . . . . . . . . . . . . . . . . 21 3.4 Outline of the proof of compactness . . . . . . . . . . . . . . . 21 3.5 The Seiberg-Witten invariant . . . . . . . . . . . . . . . . . . 23 3.6 Examples and applications . . . . . . . . . . . . . . . . . . . . 25 

4 The symplectic case, part I 25 

4.1 Statement of the theorem . . . . . . . . . . . . . . . . . . . . 26 4.2 The canonical Spin C structure . . . . . . . . . . . . . . . . . . 26 4.3 Step 1: Understanding the Dirac equation . . . . . . . . . . . 28 4.4 Step 2: deforming the curvature equation . . . . . . . . . . . . 30 4.5 Step 3: uniqueness of the solution . . . . . . . . . . . . . . . . 30 4.6 Appendix: an estimate on beta . . . . . . . . . . . . . . . . . 33 

5 The symplectic case, part II 33 

5.1 Summary of the last lecture . . . . . . . . . . . . . . . . . . . 33 5.2 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34 5.3 Seiberg-Witten and pseudoholomorphic curves . . . . . . . . . 35 5.4 Definition of the Gromov invariant . . . . . . . . . . . . . . . 36 21 Background from differential geometry 

The data for the Seiberg-Witten equations are a connection A on a certain line bundle, and a section ψ of a certain C2 bundle. In this lecture we will review bundles and connections. We assume familiarity with the tangent bundle and differential forms. (The material in this lecture can be found in almost any modern book on differential geometry; see e.g. [10].) 

## 1.1 Vector bundles 

Let X be a smooth manifold. (In this lecture all spaces will be smooth manifolds.) A vector bundle on X is essentially a family of vector spaces parametrized by X. More precisely: 

Definition 1.1 Let n ∈ { 1, 2, . . . }. A (complex) vector bundle on X of rank n is a space E with an action C × E → E of C and a surjective map 

π : E → X such that: 

• π commutes with the C action, 

• C∗ acts freely, 

• E is locally isomorphic to a product, i.e. for each x ∈ X, there is a neighborhood U ⊂ X of x and a diffeomorphism ξ : E|U = π−1(U ) →

U × Cn, such that the diagram 

E|Uπ   

> !
> !
> BBBBBBBB
> ξ//

U × Cn

> {
> {
> wwwwwwwww

U

commutes, and such that ξ intertwines the C action with the standard 

C action on Cn. ( ξ is called a local trivialization .) If n = 1, we call E a line bundle . One similarly defines a real vector bundle by replacing C above with R. A section of E is a smooth choice of a vector in each fiber, i.e. a smooth map s : X → E such that πs = identity. We denote the space of sections of E by C∞(E). 3It is a consequence of the definition that the fiber Ex of E at any x ∈ X

(that is, π−1(x)) has, in a natural way, a vector space structure of Cn. This is why E is called a vector bundle. In particular, it follows from the definition that the space of sections of E forms a vector space, where ( s1 + s2)( x) = s1(x) + s2(x), and where 

λ · s1(x) = mλ(s1(x)) for λ ∈ C. (We sometimes use mλ to denote the action of λ on E.) In this regard, note that there is a canonical section, the “zero section: 0 : X → E which is a bijection onto the image of multiplication by 0 on E. Note that if s is a section and f : X → C a smooth function, then 

f · s is a section. One can make new vector bundles out of old ones by analogy with the standard operations on vector spaces. For example if E, F are vector bundles over X, then we can define Hom( E, F ) to be the set of ( x, h ) such that x ∈ X

and h : Ex → Fx commutes with the C action. Likewise, the dual bundle E∗

consisting of ( x, h ) such that h : Ex → C and h commutes with the C action. We also have the tensor product E ⊗ F = Hom( E, F ∗). A fundamental example of a (real) vector bundle is the cotangent bundle 

T ∗X → X. We let Ω k(X) = C∞(∧kT ∗X) denote the space of differential forms on X. If E is another vector bundle on X, we can consider “ E-valued differential forms”, namely Ω k(X, E ) = C∞(∧kT ∗X ⊗ E). One more basic construction is the following. 

Definition 1.2 If π : E → X is a vector bundle and f : Y → X is a map, the pullback bundle f ∗E → Y is the fiber product of π and f ,

f ∗E ˜f

−−−→ E

yyπ

Y f

−−−→ X, 

i.e. f ∗E = {(y, e ) | y ∈ Y, e ∈ Ef (y)}, and the projection f ∗E → Y sends (y, e ) 7 → y.There is a natural map ˜f : f ∗E → E defined by ˜f (y, e ) = e. 

For each y ∈ Y , ˜f restricts to an isomorphism ( f ∗E)y → Ef (y).41.2 Connections 

In general, there is no canonical isomorphism of a fiber of a vector bundle with Cn. Let us explore what this means at the infinitesimal level, i.e. at the level of tangent bundles. If π : E → X is a vector bundle, there is an exact sequence of (real) vector bundles on the space E,0 −−−→ π∗E ı

−−−→ T E π∗

−−−→ π∗T X −−−→ 0. (1.1) In this sequence, π∗E is the bundle whose fiber over e ∈ E is the vector space in which e lives, namely Eπ(e). There is a natural map ı from π∗E to the tangent bundle T E , whose image consists of the “vertical” tangent vectors in E. (The map ı sends v ∈ E to the tangent vector ddt 

∣∣t=0 (e + tv ).) And π∗

is the derivative of π.This sequence does not have a canonical splitting. In other words, there is no canonical way to choose a “horizontal” subspace of T E complementary to the vertical subspace π∗E. However we can choose a splitting; and if the splitting satisfies certain compatiblity conditions, we call the splitting a connection. (Such a splitting “connects” the fibers over nearby points of X.) We impose the compatibility condition as follows. 

Definition 1.3 A connection on E is a map A : T E → π∗E, i.e. a 1-form on E with values in π∗E, such that: 

• A is a splitting of the exact sequence (1.1), i.e. A ◦ ı = 1 : π∗E → π∗E.

• A commutes with multiplication by scalars, i.e. if λ ∈ C and mλ : E →

E is multiplication by λ, then m∗

> λ

A = λ · A.It is sometimes useful to write a connection in terms of a local trivializa-tion ξ : E|U → U × Cn. Let ξ1, . . . , ξ n be the n corresponding C-valued func-tions on E|U , i.e. ξ(e) = ( π(e), (ξ1(e), . . . , ξ n(e))). The connection 1-form A

now takes values in Cn; let Aa be the coordinates, i.e. A = ( A1, . . . , An). Then we can write 

Aa = dξ a + Aab ξb. (1.2) Here Aab is a 1-form pulled back from U ; we can think of A as an End( Cn)-valued 1-form on U . (In (1.2) and elsewhere, repeated indices are summed.) 

Exercise 1.4 Show that any connection A over U can be written in the form (1.2), with Aab pulled back from U . Show conversely that for any Aab 

pulled back from U , the 1-form A defined by (1.2) is a connection for E|U .5Exercise 1.5 Show that the space of all connections on E is an affine space over Ω 1(X, End( E)). In other words, if A is a connection, then a 1-form A′ ∈

Ω1(E, π ∗E) is also a connection if and only if there exists α ∈ Ω1(X, End( E)) such that ( A′ − A)e = ( π∗α)( e). A connection gives us a way to differentiate sections of E.

Definition 1.6 Given a connection A, we define the covariant derivative 

∇A : C∞(E) → C∞(T ∗X ⊗ E)as follows. If ψ ∈ C∞(E), then ∇Aψ : TxX → Ex is the composition 

TxX ψ∗

−−−→ Tψ(x)E A

−−−→ (π∗E)ψ(x)˜π

−−−→ Ex.

Here is another way to understand this definition. The “horizontal” sub-space of T E is Ker( A). There is a map H : ( π∗T X )e → TeE which sends a tangent vector v ∈ T X to its horizontal lift at e, namely the unique horizontal vector h ∈ TeE such that π∗h = v. Given a section ψ : X → E

and v ∈ TxX, we can compare the derivative of ψ along v, namely ψ∗v, with the horizontal lift of v, namely Hv . The difference ψ∗v − Hv is a vertical vector in π∗E, and this is the covariant derivative, i.e. 

∇Aψ(v) = ˜ π(ψ∗v − Hv ).

So the covariant derivative measures the deviation of a section from the horizontal subspace. 

Exercise 1.7 1. Check that the map ∇Aψ : T X → E is linear. 2. Show that ∇A(ψ1 + ψ2) = ∇A(ψ1) + ∇A(ψ2). 3. Prove the Leibniz rule ∇A(f ψ ) = df ⊗ ψ + f ∇Aψ.If Aab is the matrix for A in a local trivialization as in (1.2), and if ψ is a section over U , which we think of as a Cn-valued function on U , then (∇Aψ)a = dψ a + Aab ψb.

61.3 Metrics 

We will need to consider vector bundles with a bit more structure on them. 

Definition 1.8 Let E → X be a complex vector bundle. A metric on E is a map g : E ⊗ E → C such that, if 〈v, w 〉 denotes g(v, w ), then: 

• g is antilinear in the first variable and linear in the second variable, i.e. 

〈λv, w 〉 = λ〈v, w 〉 and 〈v, λw 〉 = λ〈v, w 〉.

• 〈 w, v 〉 = 〈v, w 〉.

• g is positive definite , i.e. 〈v, v 〉 > 0 for all v 6 = 0. If E is a real vector bundle, a metric on E is defined the same way, but without the complex conjugation. 

Definition 1.9 If E is a vector bundle with a metric g, a connection A on 

E is compatible with the metric g if for any two sections ψ, η of E, we have an equality of 1-forms 

d〈ψ, η 〉 = 〈∇ Aψ, η 〉 + 〈ψ, ∇Aη〉.

Exercise 1.10 Let E be a complex (resp. real) vector bundle with a metric. Choose a local trivialization sending the metric on E to the standard metric on Cn (resp. Rn). Show that A is compatible with the metric if and only if the matrix-valued 1-form A from equation (1.2) takes values in the Lie algebra Lie(U( n)) (resp. Lie(SO( n))). A Riemannian metric on X is a metric g on the cotangent bundle 

E = T ∗X. Given g, there is a unique connection Γ on T ∗X such that: 

• Γ is compatible with g,

• Γ is torsion-free , i.e. the composition Ω1(X) ∇Γ

−−−→ C∞(X, T ∗X ⊗ T ∗X) anti-sym .

−−−−−→ Ω2(X)is equal to the exterior derivative d. (Note that this condition only make sense for connections on E = T ∗X.) This Γ is called the Levi-Civita connection .We can compute with Γ as follows. At any point p ∈ X, one can choose local coordinates x1, . . . , x n centered at p such that 〈dx j , dx k〉 = δjk +O(|x|2). Then ∇Γ(dx j ) = 0 at p.71.4 Curvature 

The curvature of a connection is a measure of the nonintegrability of the horizontal distribution in E; in other words it is an obstruction to finding nontrivial local sections of E with covariant derivative zero. 

Definition 1.11 If A is a connection on E, the curvature 

FA ∈ Ω2(X, End( E)) is defined as follows. If v, w are two vectors in TxX, extend them to local vector fields. Let Hv, Hw be the horizontal lifts in T E . If e ∈ E, then 

FA(v, w )( e) = ˜ π(−Ae([ Hv, Hw ])) .

In local coordinates, 

F ab  

> A

= dA ab + Aac ∧ Acb . (1.3) 

Exercise 1.12 Check that the definition of curvature makes sense, i.e. FA

is an honest tensor which does not depend on the choice of extension to local vector fields, and prove equation (1.3). We will need the following facts for the computations in the third and fourth lectures. 

Exercise 1.13 Choose local coordinates x1, . . . , x n on X. Let ∇i denote the 

dx i component of ∇A. Show that the dx i ∧ dx j component of FA equals the commutator [ ∇i, ∇j ]. 

Exercise 1.14 1. Show that one can extend the covariant derivative to a map 

∇A : Ω k(X, E ) → Ωk+1 (X, E )by requiring that 

∇A(α ⊗ s) = dα ⊗ s + ( −1) kα ∧ ∇ As. 

for s ∈ C∞(E) and α ∈ Ωk(X). 2. Show that FA = ∇2 

> A

: C∞(E) → Ω2(X, E ). 81.5 Self-dual two-forms 

In the four-dimensional world, there are two special vector bundles which we will need. If X is a smooth 4-manifold with an orientation and a Riemannian metric, the 2-forms have a decomposition into two R3-bundles Λ2T ∗X = Λ 2 

> −

⊕ Λ2+

constructed as follows. There is a map ∗ : Λ 2 → Λ2 defined by 

ω ∧ ∗ η = g(ω, η ) vol ,

where g is the induced metric on Λ 2 and vol ∈ Ω4(X) is the volume form, defined as follows: if e1, . . . , e 4 is an oriented orthonormal basis for T ∗X at a point x ∈ X, then vol( x) = e1 ∧ e2 ∧ e3 ∧ e4.We have ∗2 = 1, and we define Λ 2 

> ±

to be the ±1 eigenspace. Explicitly, if e1, . . . , e 4 is a basis as above, then Λ 2 

> ±

is spanned by e1 ∧ e2 ± e3 ∧ e4,

e1 ∧ e3 ∓ e2 ∧ e4, and e1 ∧ e4 ± e2 ∧ e3. Sections of Λ 2+ (resp. Λ2

> −

) are called self-dual (resp. anti-self-dual ) 2-forms. Note that switching the orientation on X interchanges Λ 2+ and Λ 2

> −

, while deforming the metric moves Λ2 

> ±

continuously inside Λ 2.

# 2 Spin and the Seiberg-Witten equations 

As we said at the beginning of the last lecture, the data for the Seiberg-Witten equations are a connection on a certain line bundle and a section of a certain C2 bundle. Having explained connections in the last lecture, we now need to specify the line bundle and the C2 bundle. At the end of the lecture we will finally be able to write down the Seiberg-Witten equations. 

## 2.1 Principal bundles and associated bundles 

We will use the following general procedure for constructing interesting vector bundles. 

Definition 2.1 Let X be a smooth manifold and G a Lie group. A prin-cipal G bundle on X is a manifold P , a surjective map π : P → X, and a (right) G action on P such that: 9• The G action respects π, i.e. the diagram 

P × G / / 

> #
> #
> GGGGGGGGG

P

> π
> 
> 

X

commutes. 

• The G action is free and transitive on each fiber. 

• Over open balls U ⊂ X there exist G-equivariant, fiber-preserving dif-feomorphisms 

P |U ' U × G. 

The canonical example is the frame bundle Fr of a smooth manifold X.If X is n-dimensional, oriented, and has a Riemannian metric, then Fr is a principal SO( n) bundle on X. The fiber over x ∈ X consists of all linear maps Rn → TxX sending the standard metric and orientation on Rn to the metric and orientation on TxX. The group SO( n) acts by composition on the right. Out of a principal bundle we can construct many vector bundles as follows. Let V be a vector space and ρ : G → Aut( V ) a representation of G. We define the associated vector bundle 

VP =( P × V )/ ∼,

(pg, v ) ∼ (p, ρ (g)v).

Exercise 2.2 1. VP is a vector bundle whose fibers are isomorphic to V .2. If V = Rn is the fundamental representation of SO( n), then VFr = T X .3. A G-invariant metric on V gives rise to a metric on VP .4. The associated bundle construction commutes with linear algebra, i.e. (V ⊗ W )P = VP ⊗ WP , etc. The material in this section can also be found in almost any modern differential geometry book. 10 2.2 Spin C structures 

From the above exercise we see that starting with the frame bundle and taking the vector bundles associated to the exterior powers of the dual fun-damental representation of SO( n), we obtain the bundles of differential forms. Now for n ≥ 3, π1 SO( n) = Z2, and we denote the connected double cover of SO( n) by Spin( n). It turns out that there are representations of Spin( n)which do not descend to SO( n). So, if we could somehow “lift” Fr to a prin-cipal Spin( n) bundle, we would get more associated vector bundles. This motivates the following definition: 

Definition 2.3 A spin structure on an oriented Riemannian manifold X

is a principal Spin( n)-bundle ˆF on X together with a map ˆF → Fr such that the following diagram commutes: ˆF × Spin( n) / / 

> 
> 

ˆF

> 
> 
> 
> 

Fr × SO( n) / / Fr 

> 
> 

X

Not every 4-manifold has a spin structure. For example S4 and S2 × S2

have spin structures, but there does not exist any spin structure on CP 2.However a certain weak version of a spin structure exists more often. Define Spin C(n) = (Spin( n) × U(1)) /Z2.

(Here Z2 acts on the first factor by the covering transformation of π :Spin( n) → SO( n) and on the second factor by multiplication by −1.) There is a well defined map Spin C(n) → SO( n) sending ( x, λ ) 7 → π(x). 

Definition 2.4 A Spin C structure is like a spin structure, but using Spin C(n)instead of Spin( n). That is, a Spin C structure is a principal Spin C bundle, ˆF ,whose projection π to X factors through Fr to give, fiberwise, the standard group homomorphism. Note that although the definition of spin (resp. Spin C) structure uses a Riemannian metric, in fact for any two metrics there is a canonical identifi-cation between the spin (resp. Spin C) structures for one metric and the spin (resp. Spin C) structures for the other metric. 11 Theorem 2.5 On any oriented 4-manifold X, Spin C structures exist, and the set SX of Spin C structures on X is an affine space modelled on H2(X; Z).

This is slightly nontrivial, and we will not prove it here. (Higher dimen-sional manifolds do not always have Spin C structures, although when they do, they always form an affine space over H2.) 

## 2.3 Some group theory 

To see what associated vector bundles we can get from a Spin C structure on a 4-manifold, we now need to discuss the representation theory of Spin C(4). We will give explicit four-dimensional constructions, even though some of these constructions have higher-dimensional generalizations. Some more general theory is discussed in [1, 2, 11, 13, 8]. We want to explain the following fundamental diagram: U(2) s−

←−−− Spin C(4) s+

−−−→ U(2) 

yyy

SO(3) ρ−

←−−− SO(4) ρ+

−−−→ SO(3) .

(2.1) (For us, the most important maps in the diagram are the three maps from Spin C(4).) Recall that SU(2) = 

{( a −bb a

)

: |a|2 + |b|2 = 1 

}

.

We can define an isomorphism SO(4) ' (SU(2) × SU(2)) / ± 1 (2.2) as follows. Identify 

R4 '

{( a −bb a

)

: a, b ∈ C = R2

}

. (2.3) Then ( h−, h +) ∈ SU(2) × SU(2) acts on x ∈ R4 by (h−, h +) · x = h−xh −1+ .

Exercise 2.6 Check that this gives an isomorphism as in (2.2). 12 We then have Spin(4) ' SU (2) × SU (2) and Spin C(4) ' (SU(2) × SU(2) × U(1)) / ± 1.

Observe that U(2) = (SU(2) × U(1)) / ± 1.

We can then define the two maps s+, s − : Spin C(4) → U(2) in the diagram (2.1) by 

s±[h−, h +, λ ] = [ h±, λ ].

To explain the map U(2) → SO(3), note that there is an isomorphism SO(3) ' SU(2) / ± 1 (2.4) defined as follows: identify 

R3 '

{( a −bb a

)

: Re( a) = 0 

}

,

and let h ∈ SU(2) act on x ∈ R3 by 

h · x = hxh −1.

Exercise 2.7 Check that this gives an isomorphism as in (2.4). Now the map U(2) → SO(3) sends [ h, λ ] 7 → ± h.Finally, the fundamental representation of SO(4) on R4 induces an or-thogonal representation of SO(4) on Λ 2R4 which preserves the decomposition Λ2R4 = Λ 2

> −

R4 ⊕ Λ2+R4. The maps ρ−, ρ + are given by the action of SO(4) on Λ2

> −

R4, Λ2+R4 respectively. 

Exercise 2.8 Show that if appropriate identifications of Λ 2

> −

R4 and Λ 2+R4

with R3 are chosen, then the diagram (2.1) commutes. There is one more important map, not on the diagram: Spin C(4) −→ U(1) ,

[h−, h +, λ ] 7 −→ λ2. (2.5) 13 2.4 The spinor bundles 

Let X be an oriented Riemannian 4-manifold with a Spin C structure. As-sociated to the representations s+, s − of Spin C(4) are C2 bundles S+, S −.Sections of these bundles are sometimes called spinors . Since the represen-tations s+, s − are unitary, the spinor bundles S+, S − come with Hermitian metrics. An important related bundle is the (Hermitian) line bundle L associated to the representation (2.5). 

Exercise 2.9 Show that Λ 2S± = L. (This follows from a certain equality of representations of Spin C(4).) 

## 2.5 Clifford multiplication 

The spinor bundles are distinguished from arbitrary vector bundles by their relation with the frame bundle. This relation manifests itself in the existence of Clifford multiplication , a map cl : T ∗X → End( S+ ⊕ S−)with the following properties: 

• For v ∈ T ∗X, cl( v) sends S+ to S− and vice-versa. 

• cl( v)2 = −| v|2.

• If |v| = 1 then cl( v) is unitary. We define cl : T ∗X ⊗ S+ → S− as follows. We begin by defining a map 

R4 × C2 → C2: using matrix multiplication with the identification (2.3), we map ( x, ψ ) 7 → xψ . To show that this induces a map T ∗X ⊗ S+ → S−, by the definition of associated vector bundle, we have to check that it commutes with the representations of Spin C(4), i.e. that for [ h−, h +, λ ] ∈ Spin C(4), (h−xh −1+ )( h+λψ ) = h−λxψ. 

This clearly holds. We define cl : T ∗X ⊗ S− → S+ similarly: this time the map R4 × C2 → C2 sends ( x, ψ ) 7 → − xtψ.If α is a 1-form and ψ is a spinor then the notations cl( α)ψ, cl( α ⊗ ψ), 

α · ψ all indicate Clifford multiplication by α on ψ.14 Remark 2.10 A Spin C structure is actually equivalent to the bundle S =

S− ⊕ S+ together with the Clifford action. From this point of view it easy to describe the H2(X; Z) action on SX : an element α ∈ H2(X; Z) sends S to 

S ⊗ E, where E is the line bundle with c1(E) = α.Digression: Recall that if E is a line bundle on X, the first Chern class 

c1(E) ∈ H2(X; Z) is (at least if X is a closed oriented manifold) the Poincar´ edual of the zero set of a generic section of E. On any X, c1 gives a bijection between the set of isomorphism classes of line bundles on X and H2(X; Z). 

Exercise 2.11 (Chern-Weil theory) Prove: If A is a connection on a line bundle E, then dF A = 0 and the cohomology class [ FA] equals −2πic 1(E). 

## 2.6 The spin connection 

Let A be a connection on L compatible with the metric. This A induces a “Spin C connection” A on S+ (and S− too). To really explain this requires a bit more background than we have given so far. But the idea, abstractly, is that a connection on a principal G bundle 

P is a 1-form with values in Lie( G), the Lie algebra of G, satisfying certain conditions, and this induces a connection on every associated vector bundle. So to define a connection on S+ it is enough to construct a connection on the principal Spin C(4) bundle ˆF . Now the maps Spin C(4) 

> y
> y
> sssssssss
> $
> $
> JJJJJJJJJ

SO(4) U(1) defined previously induce an isomorphism of Lie algebras Lie(Spin C(4)) ' Lie(SO(4)) ⊕ Lie(U(1)) . (2.6) If L is the principal U(1) bundle corresponding to L, then we have maps ˆF

> 
> 
> 
> 
> 
> ????????

Fr L.

15 The Levi-Civita connection gives a Lie(SO(4))-valued 1-form on Fr, and the connection A gives a Lie(U(1))-valued 1-form on L. Now pull these back to ˆF via the above maps, add them, and apply the isomorphism (2.6) to get the required 1-form on ˆF .Explicitly, if X is Euclidean space, with ˆF the trivial Spin C(4) bundle, S+

the trivial C2 bundle, and L the trivial line bundle, then the connection A is an imaginary-valued 1-form Aj dx j (imaginary-valued, not C-valued, because the connection is compatible with the metric), and 

∇A = dx j ⊗ (∂j + 12Aj )acting on C2-valued functions. (The factor of 12 comes from the squaring of λ

in the map (2.5).) Note in particular that the spin connection is compatible with the metric on S+.

Exercise 2.12 Show that ∇A is a module derivation : if α is a 1-form and 

ψ is a section of S+ ⊕ S− then 

∇A(α · ψ) = ( ∇Γα) · ψ + α · ∇ Aψ (2.7) in Ω 1(X, S + ⊕ S−). Here Γ is the Levi-Civita connection. 

## 2.7 The Dirac operator 

Definition 2.13 If A is a compatible connection on L, the Dirac operator 

DA is the composition 

C∞(S+) ∇A

−−−→ C∞(T ∗X ⊗ S+) cl 

−−−→ C∞(S−).

In the local model described above, 

DA =

(∇1 + i∇2 −∇ 3 + i∇4

∇3 + i∇4 ∇1 − i∇2.

)

where ∇j = ∂j + 12 Aj . If we introduce complex coordinates z = x1 + ix 2, w =

x3 + ix 4 and let ∇z = 12 (∇1 − i∇2), etc., then 

DA

(ab

)

= 2 

(∇z a − ∇ wb

∇wa + ∇z b

)

. (2.8) 16 2.8 The Seiberg-Witten equations 

Let X be a smooth oriented Riemannian 4-manifold with a Spin C structure. Fix a self-dual 2-form μ. The Seiberg-Witten equations are 

DAψ = 0 ,F + 

> A

= q(ψ) + iμ 

where A is a compatible connection on L and ψ is a section of S+.Here F + 

> A

is the self-dual component of FA, which is an imaginary-valued 2-form. Also 

q : S+ → iΛ2+T ∗X

is a quadratic form defined as follows. We extend Clifford multiplication to a map Λ 2 → End( S+) by defining cl( v ∧ w) = 12(cl( v) cl( w) − cl( w) cl( v)) . (2.9) We extend complex linearly to Λ 2 ⊗ C and restrict to get a map cl + : Λ 2+ ⊗ C → End( S+).

We then define 

q(ψ) = cl †

> +

(ψ ⊗ ψ†).

Let’s work out the second of the Seiberg-Witten equations in our local model. If {e1, . . . , e 4} is the standard basis for R4 then cl +(e1 ∧ e2 + e3 ∧ e4) = 

(−2i

2i

)

, (2.10) cl +(e1 ∧ e3 − e2 ∧ e4) = 

( 2

−2

)

,

cl +(e1 ∧ e4 + e2 ∧ e3) = 

( −2i

−2i

)

.

If ψ =

(ab

)

then ψ ⊗ ψ† =

(|a|2 ab ab |b|2

)

and thus 

q

(ab

)

=i(|a|2 − | b|2)( e1 ∧ e2 + e3 ∧ e4) + 2 i Im( ab )( e1 ∧ e3 − e2 ∧ e4)+ 2 i Re( ab )( e1 ∧ e4 + e2 ∧ e3).

17 Let F ′ 

> ij

denote the ei ∧ ej component of FA − iμ . Then the second Seiberg-Witten equation becomes 

F ′ 

> 12

+ F ′ 

> 34

= 2 i(|a|2 − | b|2),F ′ 

> 13

− F ′ 

> 24

− i(F ′ 

> 14

+ F ′

> 23

) = 4 ab. (2.11) 

Remark 2.14 Each paper on Seiberg-Witten theory seems to have a slightly different version of these equations. This is due to different conventions for Clifford multiplication and things of this nature. For example, some authors define q using the inverse of cl + instead of the adjoint, which makes their q half as large as ours. The conventions in different papers should be isomorphic under appropriate rescaling. 

Remark 2.15 The Seiberg-Witten equations were first written down by Witten [20]. See [9, 13, 8] for more details. 

# 3 The Seiberg-Witten invariants 

Let X be a closed oriented smooth 4-manifold. Let g be a Riemannian metric on X and let μ be a self-dual 2-form. Let s ∈ S X be a Spin C structure and let S+, S −, L be the corresponding vector bundles. If A is a connection on 

L and ψ is a section of S+, then ( A, ψ ) satisfy the Seiberg-Witten equations when 

F(A, ψ ) = 

( DAψF + 

> A

− q(ψ) − iμ 

)

vanishes. Let us introduce 

ms,g,μ = {(A, ψ ) : F(A, ψ ) = 0 }

to denote the space of solutions of the Seiberg-Witten equations. In this lecture we will discuss how to get information about X by studying topo-logical properties of ms,g,μ that do not depend on g and μ. This information constitutes the Seiberg-Witten invariants of X. For more details on the con-struction of these invariants, see [13, 8]. 

## 3.1 Gauge transformations 

To begin with, the space m (we usually suppress the subscripts s, g, μ ) has an infinite-dimensional group action on it, which we want to mod out by to get 18 a finite dimensional space. The group in question is C∞(X, S 1). A function 

h : X → S1 (a gauge transformation ) acts on m by 

h(A, ψ ) = ( A − 2h−1dh, hψ ).

Exercise 3.1 1. Check that this action sends m to itself. 2. Show that this action is free, except that a point with ψ ≡ 0 has stabilizer S1.Define M = m/C ∞(X, S 1),

M0 = m/{φ ∈ C∞(X, S 1) : φ(∗) = 1 }.

Here ∗ ∈ X is some base point. The group {φ ∈ C∞(X, S 1) : φ(∗) = 1 } of based gauge transformations always acts freely on m, so the space M0 is a bit more likely than M to be nonsingular. We topologize these spaces as follows. We topologize the set of all pairs (A, ψ ) (not necessarily satisfying the Seiberg-Witten equations) with the C∞

Frechet topology. We give m the subspace topology, and we then give M

and M0 the quotient topology. 

## 3.2 Basic properties of the moduli space 

We need the following notation. There is a quadratic form Q on H2(X; R)given by Q(α, β ) = ∫ 

> X

α ∧β ∈ R. Often we write α ·β instead of Q(α, β ). We define b2+ (resp. b2

> −

) to be the dimension of a maximal positive definite (resp. negative definite) subspace of H2(X; R). Also bi denotes dim Hi(X; R). (The numbers bi and b2 

> ±

and the quadratic form Q depend only on the homotopy type of X.) Fix a Spin C structure s. The moduli spaces M, M0 have the following basic properties. 

Proposition 3.2 (a) M is always compact. (b) For generic μ (if g is fixed), M0 is a smooth finite dimensional manifold with a C∞ circle action. If b2+ > 0, then for generic μ, M is smooth and M0 → M is a principal S1 bundle. 

19 (c) For generic μ,

dim( M) = b1 − 1 − b2+ + c21 − τ

4 . (3.1) 

Here τ = b2+ −b2 

> −

is the signature of X, c1 = c1(L), and c21 = Q(c1, c 1).(d) M is orientable (for generic μ). Moreover there is a canonical bijec-tion between orientations of M and orientations of the vector space 

H0(X; R) ⊕ H1(X; R) ⊕ H2+(X; R), where H2+(X; R) is a maximal pos-itive definite subspace for Q.(e) If (g0, μ 0) and (g1, μ 1) are generic, then for a generic path (gt, μ t) con-necting them, W 0 = {t, M0 

> gt,μ t

} is a smooth compact oriented manifold with boundary −M 00 + M01. If b2+ > 1, we can choose the path so that 

W = {t, Mgt,μ t } is also smooth and ∂W = −M 0 + M1.

The compactness property (a) is remarkable for two reasons. First, there is no a priori reason to expect compactness in a situation like this. For exam-ple, if we change q to −q in the second of the Seiberg-Witten equations, then compactness will fail. Second, one might have previously thought that an equation with a compact moduli space would not contain interesting topolog-ical information. For example, the noncompactness of the moduli spaces for the older Yang-Mills equations played a key role in the proof of Donaldson’s first theorem (which says that if Q is positive definite or negative definite then Q : H2(X; Z) → Z can be diagonalized over the integers, which is a very strong restriction on Q). We will outline the proof of compactness later in this lecture. On the other hand, properties (b)–(e) follow from standard machinery. This is because the deformation complex for the Seiberg-Witten equations (i.e. the linearization of the equations, which defines T(A,ψ )M) is elliptic, and there is a standard package for dealing with equations of this type. Another example of an elliptic equation is the equation for pseudoholomorphic curves, for which analogues of properties (b)–(e) are proved using similar techniques. In particular, the dimension formula (c) is proved using the Atiyah-Singer index theorem. Property (d) is proved using the index theorem for families. The rough idea is that the derivative of the Seiberg-Witten equations is a family of operators parametrized by M, and one applies the theorem to this family. Properties (b) and (e) are proved using the Sard-Smale theorem, which is a basic tool for proving infinite-dimensional transversality results. 20 These proofs can be found in, e.g., [13, 8]. Even so, Proposition 3.2 was understood by Witten [20]. In particular, Witten has a proof of compactness. 

## 3.3 Why the conditions on b2+?

If M0 is smooth, then M = M0/S 1 will also be smooth provided that S1

acts freely, i.e. as long as there are no solutions ( A, ψ ) to the Seiberg-Witten equations with ψ ≡ 0. (As a throwback to Yang-Mills theory, one might call such a solution reducible .) If ψ ≡ 0 then the Seiberg-Witten equations read 

F + 

> A

= iμ. (3.2) Let H2 be the space of harmonic 2-forms on X. Recall the Hodge decom-position Ω2 = H2 ⊕ dΩ1 ⊕ ∗ dΩ1.

Let h : Ω 2 → H 2 be the projection. 

Exercise 3.3 1. Equation (3.2) has a solution A if and only if 

h(F + 

> A

) = h(iμ ).

2. h(F + 

> A

) is the self-dual part of the harmonic representative of −2πic 1(L), and hence depends only on L.From this exercise we see that reducibles exist if and only if h(iμ ) equals a certain invariant of L in the space H2+ of harmonic self-dual 2-forms. Since dim( H2+) = b2+ , this is a codimension b2+ condition on μ, at least at the level of heuristic dimension counting. So if b2+ > 0, then for generic μ we expect no reducibles, and if b2+ > 1 then we expect no reducibles for generic 1-parameter families of μ.

## 3.4 Outline of the proof of compactness 

The outline that follows is based on arguments in [9]. The key to compactness is the following a priori estimate: 

Lemma 3.4 [9] If F(A, ψ ) = 0 (and ψ is not identically zero), then 

|ψ|2 ≤ max 

> X

(−s

2 + 2 |μ|

)

(3.3) 

at every point in X.

21 Here s is the scalar curvature of the Riemannian metric on T X . (With respect to a local orthonormal frame, the curvature of the Levi-Civita con-nection is a tensor with components Rij kl , antisymmetric in ( i, j ) and also in (k, l ). Then s = ∑ 

> i,j

Rij ij . For example, the scalar curvature of the round metric on S4 is 12.) To prove this lemma we need the following background: 

Exercise 3.5 1. Prove the Bochner-Weitzenb¨ ock formula :

D†

> A

DA = ∇†

> A

∇A + s

4 + 12 cl( FA)as operators on C∞(S+ ⊕ S−). (The curvature terms arise from com-mutators of covariant derivatives as in Exercise 1.13.) 2. Show that if ψ is a section of S+ then 

D†

> A

DAψ =

(

∇†

> A

∇A + s

4 + 12 cl +(F + 

> A

)

)

ψ. (3.4) 

Remark 3.6 It turns out that D† 

> A

= DA. So the Bochner-Weitzenb¨ ock formula says that D2 

> A

equals the “covariant Laplacian” ∇†

> A

∇A, modulo lower order terms. This is basically the property that Dirac was looking for when he defined the Dirac operator, and this requirement naturally leads to the notion of Clifford multiplication. (See [3].) 

Proof of Lemma 3.4. Choose a point in X at which |ψ|2 is maximized. Then 

4| ψ|2 ≥ 0at this point. (Here 4 = dd ∗.) Compatibility of A with the metric implies 

4| ψ|2 = 2 Re 〈∇ †

> A

∇Aψ, ψ 〉 − 2|∇ Aψ|2

≤ 2 Re 〈∇ †

> A

∇Aψ, ψ 〉.

Plugging both Seiberg-Witten equations into the Bochner-Weitzenb¨ ock for-mula (3.4) gives 0 = ∇†

> A

∇Aψ + s

4ψ + 12 cl +(q(ψ) + iμ )ψ. 

22 Putting this into the inequalities above and using the definition of q we get 0 ≤ 2 Re 

〈( −s

4 − 12 cl +(cl †

> +

(ψ ⊗ ψ†) + iμ )

)

ψ, ψ 

〉

.

Now cl + : Λ 2+ → End( S+) is injective and multiplies lengths by 2, and its image consists of the traceless endomorphisms. It follows that cl +(cl †

> +

(ψ ⊗ ψ†)) = 2 

(

ψ ⊗ ψ† − 12|ψ|2

)

.

Putting this into the inequality above we get 0 ≤

(−s

2 − | ψ|2 + 2 |μ|

)

|ψ|2

at a point where |ψ|2 is maximized. This implies the a priori estimate (3.3). 

2

Starting from this, the idea of the proof of compactness is to use “boot-strapping” to get bounds on all the higher derivatives of A and ψ. Schemat-ically, the Seiberg-Witten equations are of the form 

D

(Aψ

)

=

( ψ2

Aψ 

)

+ smooth (3.5) where D is a certain linear combination of derivatives. By this equation, the bound on ψ2 gives a bound on certain linear combinations of the derivatives of A and ψ. If these bounds imply bounds on all derivatives of A and ψ, then (3.5) can be differentiated to obtain estimates for the second derivatives of 

A and ψ in terms of the estimates for the first derivatives. Repeating this procedure over and over gives bounds on all higher derivatives. Compactness then comes from the Arzela-Ascoli theorem. Thus the key is whether the bounds for the linear combinations of derivatives in (3.5) give bounds on all derivatives. This turns out to be the case, as the Seiberg-Witten equations are elliptic after gauge fixing (which we will not discuss). 

## 3.5 The Seiberg-Witten invariant 

Assume b2+(X) > 1 and μ is generic. Suppose also that we have fixed an orientation of the vector space H0(X; R) ⊕ H1(X; R) ⊕ H2+(X; R). 23 Definition 3.7 Using the basic properties of the moduli space in Proposi-tion 3.2, we define the Seiberg-Witten invariant 

SW X : SX → Z

as follows. If b2+ − b1 is odd, it turns out (using topological facts about the intersection form Q) that the dimension of the moduli space b1 −1−b2+ + c21−τ

> 4

is an even integer 2 d. With this understood, set: 

• SW X = 0 if b2+ − b1 is even. 

• For a Spin C structure s, if d < 0 then SW X (s) = 0. 

• If d = 0, then M is a finite set of points, and the orientation assigns an element of {± 1} to each point. Set SW X (s) = ∑ 

> M

±1. 

• If d > 0 then M is a smooth, oriented 2 d dimensional compact mani-fold. Set SW X (s) = ∫ 

> M

ed, where e ∈ H2(M; Z) is the first Chern class of M0 → M (more precisely the first Chern class of the associated line bundle ( M0 × C)/S 1). The following are some “formal” properties of SW which can be proved more or less directly from the definition, and the basic properties listed in Proposition 3.2. (See e.g. [13, 8].) 

Theorem 3.8 (a) If b2+(X) > 1, then SW X (s) depends only on s and gives a diffeomorphism invariant SW X : SX → Z.(b) SW X (s) = 0 for all but finitely many s.(c) SW X#CP 2 contains the same information as SW X . (There is a blowup formula which we will not give here.) (d) If X = Y #Z and b2+(Y ), b 2+(Z) > 0 then SW X ≡ 0. (This does not contradict (c) because b2+(CP 2) = 0 .) (e) There is a charge conjugation involution s 7 → s on the set of Spin C

structures (which sends c1(L) to −c1(L)), and SW( s) = ± SW( s).

(Note that Y #Z is the connect sum of Y and Z. It is obtained by cutting out small balls in Y and Z and gluing the results together along the boundary spheres. The invariants b2+, b 1 are additive under this operation. Note that 

CP 2 is complex projective space with its non-complex orientation.) 24 3.6 Examples and applications 

For an example where the Seiberg-Witten invariant is nontrivial and has an interesting application, consider the K3 surface 

K3 = ( z41 + z42 + z43 + z44 = 0) ⊂ CP 3.

This 4-manifold has b2+ = 3 , b 2 

> −

= 19. On K3, there is a unique Spin C

structure s with c1(s) = 0. For this s, SW K3(s) = ±1. For all other Spin C

structures, SW = 0. (This will follow from the computation in the next lecture.) Theorem 3.8(c) implies that the blow up K3# CP 2 has nontrivial Seiberg-Witten invariants. (In fact if e is the Poincar´ e dual of the exceptional divisor, and if s is a Spin C structure with c1(L) = ±e, then SW( s) = ±1. This can also be deduced from the computation in the next lecture.) Now Freed-man’s theorem, which classifies topological 4-manifolds, says that K3# CP 2

is homeomorphic to Y = # 3CP 2#20 CP 2 (because the two 4-manifolds have equivalent intersection forms over Z). But SW Y ≡ 0 by Theorem 3.8(d). So we recover the following theorem of Donaldson: 

Theorem 3.9 K3# CP 2 and #3CP 2#20 CP 2 are not diffeomorphic, even though they are homeomorphic. 

(This theorem was first proved by Simon Donaldson using his celebrated 4-manifold invariants [4]. See also [5].) For another application, we will show in the next lecture that if X has a symplectic structure and b2+ > 1 then there exists a Spin C structure s with SW( s) = ±1. This combines with the vanishing theorem 3.8(d) to give an obstruction to the existence of symplectic forms. For example, we get: 

Theorem 3.10 [14] ⊕mCP 2 does not have a symplectic form when m > 1.

(This is true for homotopy theoretic reasons when m is even, so the interesting case is when m is odd.) 

# 4 The symplectic case, part I 

Let X be a closed smooth 4-manifold with b2+ > 1. Suppose that X has a symplectic form ω (i.e. ω is a 2-form, dω = 0, and ω ∧ ω never vanishes). In this lecture we will compute the Seiberg-Witten invariant of X for the simplest Spin C structures. 25 4.1 Statement of the theorem 

We need the following basic facts about our symplectic 4-manifold: 1. X has a canonical orientation, given by ω ∧ ω.2. There is a canonical Spin C structure s0 ∈ S X . Thus we can identify 

SX ' H2(X; Z), by sending s0 to 0 and extending equivariantly. (We will explain this shortly.) 3. The moduli spaces M have canonical orientations. (This is subtle and we will not explain it.) These three facts allow us to regard the Seiberg-Witten invariant as a map SW : H2(X; Z) → Z.

Let K = T 2,0X (defined below) and c = c1(K). Then: 

Theorem 4.1 [14, 15] (a) SW(0) = 1 .(b) SW( c) = ±1.(c) SW( e) = ± SW( c − e).(d) If SW( e) 6 = 0 , then 

0 ≤ [ω] · e ≤ [ω] · c, 

and if either equality holds then e = 0 or e = c.

Part (c) comes from the “charge conjugation invariance” stated in Theo-rem 3.8(e). Parts (a) and (c) clearly imply (b). The rest of this lecture will be devoted to proving (a) and (d). 

## 4.2 The canonical Spin C structure 

An ω-compatible almost complex structure is a map J : T ∗X → T ∗X

such that J2 = −1 and such that 

g(v, w ) = ω(v, Jw ) (4.1) is a Riemannian metric. Gromov [6] observed that as long as ω is nondegen-erate, the space of such J’s is nonempty and contractible. (See also [12].) 26 Exercise 4.2 Given a nondegenerate 2-form ω and a Riemannian metric g,there exists J satisfying (4.1) if and only if ω is self-dual with respect to g

and |ω| = √2. Choose an ω-compatible J, and endow X with the Riemannian metric g

given by (4.1). The almost complex structure gives a decomposition Λ∗T ∗X ⊗ C = ⊕

> p,q

T p,q ,

where T p,q = ∧pT 1,0 ⊗ ∧ qT 0,1 and T 1,0 (resp. T 0,1) is the holomorphic (resp. antiholomorphic) part of T ∗X ⊗ C.Suppose a Spin C structure is chosen. Clifford multiplication by ω, cl +(ω) : 

S+ → S+ splits S+ into ±2i eigenspaces. (In the local model of the second lecture, ω = dx 1dx 2 +dx 3dx 4, so this claim follows from equation (2.10).) Let 

E be the −2i eigenspace. This is a line bundle on X. We define the canonical Spin C structure to be the one for which E is trivial. Thus the identification 

SX → H2(X; Z) sends s to c1(E). Here are some key facts about the spin bundles and the Clifford action. 

Lemma 4.3 There are natural identifications 

S+ = ( T 0,0 ⊕ T 0,2) ⊗ E = E ⊕ (K−1 ⊗ E), (4.2) 

S− = T 0,1 ⊗ E (4.3) 

such that the formula for Clifford multiplication by v ∈ T ∗X ⊗ C acting on 

α ∈ T 0,∗ ⊗ E is 

cl( v) · α = √2( v0,1 ∧ α − ı(v1,0)α). (4.4) 

In particular, cl( ω) equals −2i on E and +2 i on K−1E.

(Here v0,1 is the T 0,1 component of v, and ı denotes interior product.) 

Proof. Starting with a Spin C structure as we defined it in the second lecture, the isomorphisms (4.2), (4.3) are given by rescaled Clifford multiplication. More precisely we extend Clifford multiplication to a complex linear map cl : Λ ∗T ∗X ⊗ C → End( S+ ⊕ S−) as in (2.9). Then there is an isomorphism from K−1 ⊗ E to the +2 i eigenspace of ω on S+ given by 12 cl. (We put in the factor of 12 to make this an isometry.) We can see that this gives the desired isomorphism because in the local model of the second lecture, 12 cl( dzdw ) = 

( 0 0

−2 0

)

.

27 This explains (4.2). The isomorphism T 0,1⊗E → S− in (4.3) is given similarly by 1√2 cl. It is then straightforward to check (4.4). 2

With the preceding understood, we can write ψ =

(αβ

)

with α ∈ C∞(E)and β ∈ Ω0,2(X, E ). The second Seiberg-Witten equation is then 

F + 

> A

= i(|α|2 − | β|2) + 2( αβ − αβ ) + iμ. (4.5) (We obtain this from the local calculation (2.11) by putting α = a and 

β = −12 bdzdw .) We can also state the formula for the dimension 2 d of the moduli space M.If e = c1(E) and c = c1(K), then (3.1) and some fiddling with characteristic classes imply 2d = e · e − c · e. (4.6) In particular, when e = 0 the moduli space is a finite number of points, and to prove Theorem 4.1(a) we must show that the signed number of points is 

±1. 

## 4.3 Step 1: Understanding the Dirac equation 

The first step in the proof of Theorem 4.1 is to write the first of the Seiberg-Witten equations in a nice form, by writing the Dirac operator in terms of the Cauchy-Riemann operator ∂.We begin by observing that there is a canonical connection A0 on K−1.Consider the canonical Spin C structure and identify S+ = ( X × C) ⊕ K−1.Let u0 be the constant section of X × C which assigns 1 ∈ C to each point of X.

Lemma 4.4 There exists a unique compatible connection A0 on K−1 such that 

∇A0 u0 ∈ Ω1(X, K −1),

where A0 is the spin connection associated to A0.Proof. Let A be a compatible connection on K. Any other compatible connection can be written as A + a where a is an imaginary-valued 1-form. We have 

∇A+au0 = ∇Au0 + 12au 0.

28 Since A is compatible with the metric, the X × C component of ∇Au0 is an imaginary-valued 1-form (times u0). So the unique solution is A0 = A + a

where a = −2( ∇Au0)X×C. 2

If X is K¨ ahler, ∇A0 u0 vanishes altogether. If X is not K¨ ahler, we still have 

DA0 u0 = 0 . (4.7) To see this, note the following Leibniz-type formula for the Dirac operator: 

DA0 (ω · u0) = ( dω + d∗ω) · u0 + cl( ω · ∇ A0 u0). (4.8) (This much is true for any connection, differential form, and spinor, and can be derived from (2.7). The rightmost term here means the following: start with ∇A0 u0 ∈ C∞(T ∗X ⊗ S+), first apply 1 ⊗ cl( ω) to get another element of C∞(T ∗X ⊗ S+), and then apply cl to get an element of C∞(S−).)Now u0 is in the −2i eigenspace of cl( ω) and ∇A0 u0 is in ( T ∗X tensor) the +2 i eigenspace. Also ω is closed and self-dual. So (4.8) becomes 

−2iD A0 u0 = 0 + 2 iD A0 u0.

This proves (4.7). Now we come to the point. Consider an arbitrary Spin C structure with 

S+ = E ⊕ K−1E. We can write any connection A on L = K−1E2 as A0 + 2 a

where A0 is the canonical connection on K−1 and a is a connection on E.Then the formula for the Dirac operator is the following. 

Lemma 4.5 If a is a connection on E, α is a section of E, and β is a section of K−1E, then 

DA0+2 a

(αβ

)

= √2( ∂aα + ∂∗

> a

β). (4.9) (Here ∂a : Ω 0,k (X, E ) → Ω0,k +1 (X, E ) denotes the antiholomorphic part of 

∇a.) 

Proof. First consider the canonical Spin C structure. By (4.4), the Leibniz rule as in (4.8), and (4.7), we have 

DA0 (α + β) = DA0

(( 

α + β

2

)

· u0

)

=

(

dα + dβ + d∗β

2

)

· u0

= √2( ∂α + ∂∗β).

29 (Since β is self-dual, cl( dβ ) = cl( d∗β).) The case of a general Spin C structure and connection a follows formally from this. 2

(When X is K¨ ahler, A0 comes from the Levi-Civita connection, and (4.9) follows more straightforwardly from (4.4).) 

Exercise 4.6 Prove Theorem 4.1(c). 

## 4.4 Step 2: deforming the curvature equation 

Since the Seiberg-Witten invariant does not depend on μ, we can choose μ

to suit our convenience. Normally one might think of choosing μ to be small, so as to perturb the equations and get a smooth moduli space. But we will choose μ to be very large. We take 

μ = rω − iF +

> A0

where r is a large positive real number. Let’s also rescale by writing ψ = √r(α, β ). Then the Seiberg-Witten equations become, by (4.5) and (4.9), 

∂aα = −∂∗

> a

β, (4.10) 

F + 

> a

= −ir 

2 (1 − | α|2 + |β|2)ω − r(αβ − αβ ). (4.11) We will later need to decompose the curvature equation (4.11) as follows. We have Λ2+ ⊗ C = Cω ⊕ K ⊕ K−1.

So (4.11) implies 

F 0,2 

> a

= rαβ, (4.12) 

〈ω, F a〉 = −ir (1 − | α|2 + |β|2). (4.13) 

## 4.5 Step 3: uniqueness of the solution 

For the canonical Spin C structure, a is just an imaginary-valued 1-form, and the equations (4.10), (4.11) have an obvious solution, given by a ≡ 0, 

α ≡ 1, β ≡ 0. We will now show that this is the only solution (up to gauge equivalence) if r is sufficiently large. This will prove Theorem 4.1(a) (modulo a transversality issue, see below). In the following calculations we will begin 30 with an arbitrary Spin C structure, which will allow us to simultaneously prove Theorem 4.1(d). We need the following background. First, the Nijenhuis tensor is a map N : Ω 1,0(X) → Ω0,2(X) defined by 

N (α) = ( dα )0,2.

This is a measure of the failure of the almost complex structure to be inte-grable. We claim that N is actually a tensor , i.e. a section of Hom( T 1,0, T 0,2). To show this, we have to check that N (f α ) = f N (α) for every f ∈ C∞(X, C); and this follows readily from the definition. Second, we need another Weitzenb¨ ock formula, which says that 2∂∗

> a

∂a = ∇∗

> a

∇a − i〈ω, F a〉 (4.14) on C∞(E). (See e.g. [5, p. 212]; there X is assumed to be K¨ ahler, but the proof does not use the assumption that J is integrable.) Now here is the proof that the solution is unique. Applying ∂a to the Dirac equation (4.10) and then using Exercise 1.14 and the curvature equation (4.12) gives 

∂a∂∗

> a

β = −∂a∂aα

= −F 0,2 

> a

α + N (∂aα)= −r|α|2β + N (∂aα).

Multiply by β and integrate over X to get 

∫

|∂∗

> a

β|2 =

∫ (〈β, N (∂aα)〉 − r|α|2|β|2) . (4.15) Since N is a tensor bounded independent of r, we can use the triangle in-equality to estimate 

∫

〈β, N (∂aα)〉 ≤ r

2

∫

|β|2 + zr

∫

|∇ aα|2 (4.16) where z is a positive constant independent of r. Putting this inequality into the previous equation gives 

∫ (

|∂∗

> a

β|2 + r|α|2|β|2 − r

2|β|2

)

≤ zr

∫

|∇ aα|2. (4.17) 31 We next want to estimate ∫ |∇ aα|2. Apply the Weitzenb¨ ock formula (4.14) to α, take the inner product with α, integrate over X, and apply the curvature equation (4.13) to get 

∫

|∇ aα|2 =

∫ (2|∂aα|2 + r(1 − | α|2 + |β|2)|α|2) . (4.18) Now comes a key step, where we bring in cohomological information about 

e = c1(E). Chern-Weil theory tells us that 

−2πi [ω] · e =

∫

ω ∧ Fa.

Using the fact that ω is self-dual and putting in the curvature equation (4.13) gives 2π[ω] · e =

∫

r(1 − | α|2 + |β|2).

Putting this into (4.18) gives 

∫

|∇ aα|2 = 2 π[ω] · e +

∫ (2|∂aα|2 + r(1 − | α|2 + |β|2)( |α|2 − 1) ) .

(It is auspicious that the square (1 −| α|2)2 appears.) Now replace |∂aα|2 with 

|∂∗

> a

β|2 (by the Dirac equation (4.10)), put (4.17) (times 2) into the integral on the right, discard the positive term r|α|2|β|2, and rearrange to obtain 

∫ (( 

1 − 2zr

)

|∇ aα|2 + r(1 − | α|2)2

)

≤ 2π[ω] · e. (4.19) If we choose r > 2z, then we can now read off the conclusions of Theo-rem 4.1 from the inequality (4.19). If [ ω] · e < 0 then clearly no solution is possible. If [ ω] · e = 0 then we must have |α| ≡ 1 and β ≡ 0. In particular E has a nonvanishing section, so e = 0. After a gauge transformation, α ≡ 1. From previous equations we have ∇aα ≡ 0, which implies a ≡ 0. So this is the only solution. To complete the proof that SW (e) = ±1, one must check that the moduli space is cut out transversely at this point. The proof is similar to the above calculation and we omit it. If [ ω] · e ≥ [ω] · c, we draw analogous conclusions by using charge conju-gation invariance to reduce to the above cases. 32 4.6 Appendix: an estimate on beta 

We are done with the proof of Theorem 4.1. The key was the estimate (4.19) involving α. Using some of the same techniques, we can also get an estimate on β. We will now do this, as it will help motivate the main theorem in the next lecture. We are going to use equation (4.15) a different way. There is another Weitzenb¨ ock formula which tell us that 

∫

|∂∗

> a

β|2 =

∫ 12

(|∇ ∗

> a

β|2 − i〈ω, F a〉| β|2) .

Putting in the curvature equation (4.13), we get 

∫

|∂∗

> a

β|2 =

∫ (12|∇ ∗

> a

β|2 + r

2(1 − | α|2 + |β|2)|β|2

)

. (4.20) Also, by using the triangle inequality differently, we can replace (4.16) with 

∫

〈β, N (∂aα)〉 ≤ r

4

∫

|β|2 + zr

∫

|∇ aα|2, (4.21) where z is a new constant which is still independent of r. Putting (4.20) and (4.21) into (4.15) and discarding the positive |α|2|β|2 term, we obtain the following estimate: 

∫ (12|∇ ∗

> a

β|2 + r

2|β|4 + r

4|β|2

)

≤ zr

∫

|∇ aα|2. (4.22) 

# 5 The symplectic case, part II 

We will now discuss the Seiberg-Witten invariant on a symplectic manifold 

X (with b2+ > 1) for the remaining Spin C structures, and explain that it is equal to a certain count of pseudoholomorphic curves in X.

## 5.1 Summary of the last lecture 

Since X is symplectic, there is an identification 

SX ' H2(X; Z).

33 An element e ∈ H2(X; Z) corresponds to a Spin C structure with 

S+ = E ⊕ K−1E

where c1(E) = e, and K is the canonical bundle coming from an ω-compatible almost complex structure J. We can regard the Seiberg-Witten invariant as a map SW : H2(X; Z) → Z.

If we write ψ = √r(α, β ) with α ∈ C∞(E) and β ∈ C∞(K−1E), write 

A = A0 + 2 a, and choose μ = rω − iF + 

> A0

, then the Seiberg-Witten equations are 

∂aα = −∂∗

> a

β, F + 

> a

= −ir 

2 (1 − | α|2 + |β|2)ω − r(αβ − αβ ). (5.1) We showed that any solution of these equations must satisfy the estimates 

∫ (( 

1 − 2zr

)

|∇ aα|2 + r(1 − | α|2)2

)

≤ 2π[ω] · e, (5.2) 

∫ (12|∇ ∗

> a

β|2 + r

2|β|4 + r

4|β|2

)

≤ zr

∫

|∇ aα|2. (5.3) Taking r > 2z, we see from (5.2) that if [ ω] · e < 0 then there is no solution, and if [ ω] · e = 0 then e = 0 and there is a unique solution. We conclude that SW( e) = 0 for [ ω] · e < 0, and SW(0) = ±1. (Also SW( e) = SW( c − e)where c = c1(K).) 

## 5.2 Motivation 

Fix e with [ ω] · e > 0. Suppose SW( e) 6 = 0. Then for every r the equations (5.1) must have a solution. Let’s think about what the estimates (5.2), (5.3) say when r is large. 

• By (5.2), |α| wants to equal 1 as much as possible. (But it can’t equal 1 everywhere because E is nontrivial.) 

• (5.2) gives an upper bound on the r.h.s. of (5.3), so |β| and |∇ ∗

> a

β| want to be small. 

• By the Dirac equation, |∂aα| = |∂∗

> a

β| = |∇ ∗

> a

β|, which wants to be considerably smaller than |∇ aα| by (5.3). 34 This last remark suggests that the zero set of α is close to a pseudoholo-morphic curve. The zero set of α is necessarily Poincar´ e dual to e = c1(E), so this suggests that there is some relation between SW( e) and pseudoholo-morphic curves Poincar´ e dual to e. Notice also that the formal dimension of the space of (unparametrized) pseudoholomorphic curves Poincar´ e dual to e

is (by Riemann-Roch) 2d = e · e − c · e, 

which is the same as the dimension of the Seiberg-Witten moduli space. 

## 5.3 Seiberg-Witten and pseudoholomorphic curves 

A nonzero Seiberg-Witten invariant does indeed lead to the existence of a pseudoholomorphic curve, as follows. 

Theorem 5.1 [16, 17] Fix a Spin C structure e. Given a sequence rn → ∞ 

and (an, (αn, β n)) satisfying the equations (5.1) for r = rn, then after taking an appropriate subsequence, there is a compact, complex curve C and a J-holomorphic map f : C → X such that: 

• f∗[C] is the Poincar´ e dual of e in H2(X; Z).

• lim n→∞ 

{

sup x∈C dist( x, α −1 

> n

(0)) + sup x∈α−1  

> n(0)

dist( x, f (C)) 

}

= 0 .

• If G ⊂ X is a closed set and α−1 

> n

(0) ∩G 6 = 0 for all n, then f (C)∩G 6 = 0 .

Note that C is not necessarily connected, and the map f is not necessarily an embedding. But it is worth noting that if C is connected and f is an embedding, then the genus g of C is given by the adjunction formula 

2g − 2 = e · e + c · e. 

Theorem 5.1 has a number of applications to the topology of symplectic 4-manifolds. For example, we showed in the last lecture that SW( c) = ±1, so Theorem 5.1 implies that there exists a pseudoholomorphic map f : C →

X with f∗[C] Poincar´ e dual to c = c1(K). One can use the Sard-Smale theorem together with the adjunction formula to show that if J is generic, then f : C → X is an embedding except that some components might be multiply covered tori with self-intersection number zero. From this one can further deduce that if c · c < 0 then some component of C is an embedded pseudoholomorphic sphere with self-intersection number −1. So we get: 35 Corollary 5.2 Let X be a closed connected symplectic 4-manifold with b2+ >

1 and c1(K)2 < 0. Then there exists an embedded pseudoholomorphic sphere in X with self-intersection number −1, and hence X = Y #CP 2 where Y is symplectic. 

We can go beyond Theorem 5.1 to show that the Seiberg-Witten invariant SW( e) is equal to a suitable count of pseudoholomorphic curves Poincar´ e dual to e. This count is given by a “Gromov invariant” Gr : H2(X; Z) → Z, which we will define in the next section. 

Theorem 5.3 [16, 19] If b2+ > 1, then SW = Gr : H2(X; Z) → Z.

## 5.4 Definition of the Gromov invariant 

We want to count unparametrized, possibly disconnected, pseudoholomor-phic curves Poincar´ e dual to e. We will do this in a fairly standard way, except that we allow tori to be multiply covered and count the multiple cov-ers in a subtle way. The results in this section are discussed in greater detail in [18]. 

Definition 5.4 Given e ∈ H2(X; Z), let He denote the set of finite sets 

h = {(Ci, m i)} such that: 

• Ci is an embedded, connected, pseudoholomorphic submanifold of X,and if ei ∈ H2(X; Z) is the Poincar´ e dual of [ Ci], then the formal dimension 2di = ei · ei − c · ei ≥ 0.

• Ci ∩ Cj = ∅ for i 6 = j.

• mi is a positive integer, which is 1 unless ei · ei = c · ei = 0 (i.e. Ci is a torus with trivial normal bundle). 

• ∑ 

> i

miei = e.

• If d = 12 (e·e−c·e) > 0, fix a set Ω ⊂ X of d points, and require Ω = ∪iΩi

where Ω i contains di points and Ω i ⊂ C. (Notice that d = ∑ di.) The following theorem is the result of arguments due to Ruan, McDuff-Salamon, Ye, Parker-Wolfson and Taubes. 36 Theorem 5.5 If J is generic, then He is a finite set. Furthermore, for each 

i, the pair (Ci, Ωi) is (strongly) nondegenerate (in a technical sense which is specified below). 

Given e ∈ H2(X; Z), we define Gr( e) ∈ Z as follows. If d < 0, we set Gr( e) = 0. We set Gr(0) = 1. If d ≥ 0, we choose a generic J and define Gr( e) = ∑

> h∈H e

∏

> i

r(Ci, m i).

Here r(Ci, m i) is an integer which we will now describe. For this purpose, we must digress momentarily to consider deformations of a pseudoholomorphic curve C. An infinitesimal deformation of C is given by a section of the normal bundle N → C. (We can restrict attention to the normal bundle, instead of considering the pullback of T X , because we are interested only in the image of the curve in X.) The normal bundle is naturally a holomorphic line bundle on C. A deformation s ∈ C∞(N ) is the derivative of a 1-parameter family of pseudoholomorphic curves iff 

Ds = ∂s + νs + μs ∈ C∞(N ⊗ T 0,1C)vanishes. Here ν ∈ C∞(T 0,1C) and μ ∈ C∞(T 0,1C ⊗N ⊗2) are certain sections determined by the 1-jet of the almost complex structure J near C. (If J is integrable, then μ vanishes.) We say that a curve C ⊂ X together with a set Ω C ⊂ C of d points is 

nondegenerate if the operator 

D ⊕ ev : C∞(N ) → C∞(N ⊗ T 0,1C) ⊕ ⊕ p∈ΩC Np

has no cokernel. By the dimension formula, this means that the operator has no kernel either. In this case we want to define r(C, 1) to be ±1, depending on “the sign of the determinant of D ⊕ ev”. What is the sign of the determinant of an infinite dimensional matrix? We are considering operators whose kernel and cokernel are finite dimensional, and have the same dimension. We require this sign to have the following properties: 

• The determinant of an invertible C-linear operator has positive sign. 

• Along a suitably generic path of operators, the determinant switches signs at the points on the path where the kernel (and hence the coker-nel) is not trivial. (A path of operators {O(t)}t∈[0 ,1] is generic if three 37 properties hold: first, Ker( O(t)) = {0} for all but a finite set, Λ, of t.Second, it t ∈ Λ, then dim Ker( O(t)) = 1. Third, if t ∈ Λ, then dO dt 

∣∣t

maps the kernel of O(t) to the cokernel of O(t).) These two criteria turn out to be consistent, and they unambiguously deter-mine a sign for the determinant of D. Thus, to find r(C, 1), we deform D to an invertible C-linear operator (e.g. by deforming the μ term to zero), count the number of points along the deformation where the kernel is not trivial, and take ( −1) to this power. Now suppose C is a torus with trivial normal bundle. We say that C is 

strongly nodegenerate if, for every holomorphic covering f : C′ → C by a torus C′, the operator f ∗D on C∞(f ∗N ) defined by (f ∗D)s = ∂s + ( f ∗ν)s + ( f ∗μ)s

is surjective. In this case r(C, m ) is defined as follows. There are 4 flat real line bundles 

{Lι} on C, classified by ι ∈ H1(C; Z/2). We can twist the operator D by Lι

to get an operator Dι on C∞(N ⊗ Lι). The number r(C, m ) depends on: 

• The sign of the determinant D0, which we signify as + or −.

• The number k ∈ { 0, 1, 2, 3} of nonzero ι such that the sign of the determinant of Dι is −1. Let’s write r±,k (C, m ) for the corresponding value of r(C, m ). To define 

r±,k (C, m ), it is convenient to use the generating function 

f±,k = 1 + 

> ∞

∑

> n=1

r±,k (C, m )tm.

Then we define 

f+,0 = 11 − t,f+,1 = 1 + t, f+,2 = 1 + t

1 + t2 ,f+,3 = (1 + t)(1 − t2)1 + t2 ,f−,k = 1

f+,k 

.

38 Note that r(C, m ) is not always ±1. This completes the definition of Gr. Another derivation of this invariant has been given by Ionel and Parker [7]. 

# References 

[1] M. F. Atiyah, R. Bott, and A. Shapiro, Clifford modules, Topology 3

(1964) suppl. 13–38. [2] N. Berline, E. Getzler, and M. Vergne, Heat kernels and Dirac operators ,Grundlehren der Mathematischen Wissenschaften 298, Springer-Verlag, 192. [3] P. A. M. Dirac, Principles of quantum mechanics , Oxford Univ. Press. [4] S. K. Donaldson, Polynomial invariants for smooth four-manifolds ,Topology 29 (1990), no. 3, 257–315. [5] S. K. Donaldson and P. B. Kronheimer, The geometry of four-manifolds ,Oxford Univ. Press, 1990. [6] M. Gromov, Pseudoholomorphic curves in almost complex manifolds ,Invent. Math. 82 (1985), 307–347. [7] E. Ionel and T. Parker, The Gromov invariants of Ruan-Tian and Taubes, Math. Res. Lett. 4 (1997), no. 4, 521–532. [8] D. Kotschick, P. B. Kronheimer, and T. S. Mrowka, in preparation. [9] P. B. Kronheimer and T. S. Mrowka, The genus of embedded surfaces in the projective plane , Math. Res. Letters 1 (1994), 797–808. [10] S. Kobayashi and K. Nomizu, Foundations of differential geometry , John Wiley and Sons, 1963 (vol. I), 1969 (vol. II). [11] H. B. Lawson Jr. and M–L. Michelson, Spin geometry , Princeton Math-ematical Series 38, Princeton Univ. Press, 1989. [12] D. McDuff and D. Salamon, Introduction to symplectic topology , Oxford Univ. Press, 1995. 39 [13] J. Morgan, The Seiberg-Witten equations and applications to the topol-ogy of smooth four-manifolds , Mathematical Notes 44, Princeton Univ. Press, 1996. [14] C. H. Taubes, The Seiberg-Witten invariants and symplectic forms ,Math. Res. Lett. 1 (1994), 809–822. [15] C. H. Taubes, More constraints on symplectic forms from the Seiberg-Witten invariants , Math. Res. Letters 2 (1995), 9–13. [16] C. H. Taubes, The Seiberg-Witten and the Gromov invariants , Math. Res. Lett. 2 (1995), 221–238. [17] C. H. Taubes, SW = ⇒ Gr : from the Seiberg-Witten equations to pseu-doholomorphic curves , J. Amer. Math. Soc. 9 (1996), 845–918. [18] C. H. Taubes, Counting pseudo-holomorphic submanifolds in dimension 4, J. Differential Geometry 44 (1996) no. 4, 818–893. [19] C. H. Taubes, Counting curves and connections , preprint. [20] E. Witten, Monopoles and 4-manifolds , Math. Res. Lett/ 1 (1994), 769– 796. 40
