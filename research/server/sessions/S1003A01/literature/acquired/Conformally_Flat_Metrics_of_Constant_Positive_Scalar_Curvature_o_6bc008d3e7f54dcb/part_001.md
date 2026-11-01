---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Conformally Flat Metrics of Constant Positive Scalar Curvature on Subdomains of the Sphere]

# Conformally Flat Metrics of Constant Positive Scalar Curvature on Subdomains of the Sphere

> Source: https://projecteuclid.org/journals/journal-of-differential-geometry/volume-34/issue-3/Conformally-flat-metrics-of-constant-positive-scalar-curvature-on-subdomains/10.4310/jdg/1214447536.pdf
> Fetched: 2026-10-09 09:05
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
  "source_url": "https://projecteuclid.org/journals/journal-of-differential-geometry/volume-34/issue-3/Conformally-flat-metrics-of-constant-positive-scalar-curvature-on-subdomains/10.4310/jdg/1214447536.pdf",
  "metadata": {
    "provenance_urls": [
      "https://projecteuclid.org/journals/journal-of-differential-geometry/volume-34/issue-3/Conformally-flat-metrics-of-constant-positive-scalar-curvature-on-subdomains/10.4310/jdg/1214447536.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "Schoen Green function conformal blow-up scalar curvature zero asymptotically flat manifold regular point"
      }
    ]
  },
  "declared_files": [
    {
      "url": "https://projecteuclid.org/journals/journal-of-differential-geometry/volume-34/issue-3/Conformally-flat-metrics-of-constant-positive-scalar-curvature-on-subdomains/10.4310/jdg/1214447536.pdf",
      "name": "1214447536.pdf",
      "label": "",
      "role": "primary_object_file",
      "parent_url": "https://projecteuclid.org/journals/journal-of-differential-geometry/volume-34/issue-3/Conformally-flat-metrics-of-constant-positive-scalar-curvature-on-subdomains/10.4310/jdg/1214447536.pdf",
      "identity_bound": true,
      "primary_label": false,
      "download_eligible": true
    }
  ]
}
```

## Source description

1. Introduction Because of the resolution of the Yamabe problem by R. Schoen in 1984  (see also ), it is possible to divide the conformal classes of Rieman-nian metrics on an arbitrary compact manifold M of dimension n > 3 into three disjoint subsets containing respectively those classes which con-tain a metric of constant positive, zero, or negative scalar curvature, ac-cording to the sign of the first eigenvalue of the conformal Laplacian on M. This sign is well-defined within a conformal class. On a given manifold one or more of these subsets may be empty; for example, it is known that the A genus is a topological obstruction governing the existence of metrics of positive scalar curvature when the manifold is spin. When the manifold is not assumed to be compact, these simple statements [...] Just as in the compact setting, though, the hardest analysis is required in questions concerning metrics of constant positive scalar curvature. Very deep results have been obtained by Schoen and Yau  and Schoen  in what is perhaps the most geometrically appealing instance of this prob-lem, namely when the ambient manifold is the ^-sphere S n . One of the basic problems here is to determine which subdomains of the sphere carry complete conformally flat metrics of constant positive scalar curvature. In  this problem was approached through ideas of conformal geometry. [...] These results lead to many more questions. For example, Schoen's con-struction works only when the domain Ω c S n ha

## Retrieved source content

Title: 1214447536.pdf

URL Source: https://projecteuclid.org/journals/journal-of-differential-geometry/volume-34/issue-3/Conformally-flat-metrics-of-constant-positive-scalar-curvature-on-subdomains/10.4310/jdg/1214447536.pdf

Number of Pages: 42

Markdown Content:
> J. DIFFERENTIAL GEOMETRY 34(1991) 581-621

## CONFORMALLY FLAT METRICS OF CONSTANT POSITIVE SCALAR CURVATURE ON SUBDOMAINS OF THE SPHERE 

RAFE MAZZEO & NATHAN SMALE 

> Abstract

A basic problem has been to construct complete conformally flat metrics of constant positive scalar curvature on the complement of arbitrary sets Λ c Sn where Sn is an ^-sphere. A necessary condition for the ex-istence of such a metric is that the Hausdorff dimension of Λ must be less than or equal to (n - 2)/2 . Examples are known when Λ is any finite collection of points, a subsphere, and also when Λ is the limit set of certain Kleinian groups. Up until now no examples have been known where Λ is a smooth (nonspherical) submanifold of positive dimension. We prove here that there are many examples whenever Λ is a small per-turbation of an equatorial subsphere. A local version of this result is also proved. These theorems rely on an analysis of certain degenerate linear elliptic operators, which is complicated by the fact that these operators have infinite dimensional null-spaces. A fairly general construction of pseudodifferential right-inverses for such operators is presented. 

1. Introduction 

Because of the resolution of the Yamabe problem by R. Schoen in 1984 [26] (see also [13]), it is possible to divide the conformal classes of Rieman-nian metrics on an arbitrary compact manifold M of dimension n > 3into three disjoint subsets containing respectively those classes which con-tain a metric of constant positive, zero, or negative scalar curvature, ac-cording to the sign of the first eigenvalue of the conformal Laplacian on 

M. This sign is well-defined within a conformal class. On a given manifold one or more of these subsets may be empty; for example, it is known that the A genus is a topological obstruction governing the existence of metrics of positive scalar curvature when the manifold is spin. When the manifold is not assumed to be compact, these simple statements need modification. In this setting it is geometrically and analytically natural to restrict atten-tion to complete metrics; however, a conformal class always contains both 

Received March 26, 1990. Both authors were partially supported by National Science Foundation Postdoctoral Research Fellowships during the course of this research. 582 RAFE MAZZEO & NATHAN SMALE 

complete and incomplete metrics. Thus, a possible way to generalize this problem is to ask whether on a given noncompact Riemannian manifold there exist complete metrics of constant scalar curvature and, if so, is the sign of this constant well defined within the set of complete metrics within a conformal class. Another possible question is whether starting with a complete metric there exists another complete metric quasi-isometric to the given one with constant scalar curvature. Only partial answers to these questions are known, but even so it is clear that very different phenomena occur than for compact manifolds. In a series of papers [l]-[3], Aviles and McOwen have studied the ques-tion of finding complete metrics which have constant negative scalar cur-vature and which are conformal to a given one. They also consider more general questions concerning prescribing scalar curvature. It is natural to study these problems on noncompact manifolds with 'simple' structure, for example those which arise by deleting a closed subset from a compact Riemannian manifold. An example of this is a result proved by Aviles and McOwen [2] to the effect that if M is an ^-dimensional compact Rieman-nian manifold and if N is a k-dimensional submanifold, then there is a complete metric conformal to the incomplete one on M\N with constant negative scalar curvature if and only if k > (n - 2)/2. This generalizes an older theorem due to Loewner and Nirenberg [ 14] which treats the case when M is a sphere. Just as in the compact setting, though, the hardest analysis is required in questions concerning metrics of constant positive scalar curvature. Very deep results have been obtained by Schoen and Yau [28] and Schoen [27] in what is perhaps the most geometrically appealing instance of this prob-lem, namely when the ambient manifold is the ^-sphere Sn . One of the basic problems here is to determine which subdomains of the sphere carry complete conformally flat metrics of constant positive scalar curvature. In [28] this problem was approached through ideas of conformal geometry. One of the theorems proved there is that if a subdomain Ω = Sn\A car-ries a complete metric with scalar curvature bounded below by a positive constant, then the Hausdorff dimension of Λ is < (n - 2)/2. On the other hand, in [27] Schoen constructs many such domains Ω which carry complete conformally flat metrics of constant positive scalar curvature. In particular, he constructs such metrics on the complement of any finite set of points of cardinality larger than one in the sphere. These results lead to many more questions. For example, Schoen's con-struction works only when the domain Ω c Sn has complement Λ of a very special type. It is natural to conjecture from the results of [28] CONFORMALLY FLAT METRICS 583 

that the complement of any subset Λ of Sn with ^ ( " " 2 ) / 2 ( Λ ) < oo (and of cardinality greater than one) supports a complete conformally flat metric of constant positive scalar curvature on its complement. For ex-ample, consider the simple situation when Λ is an equatorial /c-sphere Λ = Sk . It is easy to find the required metric here. First stereographi-cally project Sn from some point on Sk . Now Ω = R n\R* with its flat metric. Introduce coordinates y e R k, and polar coordinates (r, θ) in the orthogonal complement Rn~ . I n these coordinates the flat metric is 

dχ 2 = dr 2 + r2dθ 2 + dy 2 . This is clearly conformal to 

# (U) i? _ _ y ^

But this is nothing order than the product metric on sn~k~ι x H f c + 1 . As such it is certainly complete and has scalar curvature (1.2) Rnk = (n-k- \){n - k - 2) - (k + l)(fc) = (n - 2k - 2)(n - 1). Thus, Rn k > 0 precisely when n - 2k - 2 > 0, i.e., when k < (n - 2)/2 as expected. A fundamental goal is to characterize those /c-dimensional submani-folds AeS n with k < (n-2)/2 for which Ω = 5 Π\Λ supports a complete conformally flat metric of constant positive scalar curvature. No smooth examples of positive dimension other than round S 's have been known. On the other hand, it is possible to construct complete conformally flat metrics of constant positive scalar curvature on subdomains of the sphere by lifting solutions from compact manifolds which are constructed using the solution of the Yamabe conjecture. In these constructions Λ is the limit set of a Kleinian group, hence is either a round sphere or unrectifi-able with Hausdorff dimension less than (n — 2)/2. We produce the first nonround smooth examples here by analyzing perturbations of the product metric £ 0 of (1.1) on Ω = Sn\S k . We also study questions of uniqueness. It is well known in the noncompact case that the same conformal class may contain different complete metrics with constant scalar curvatures of dif-ferent signs. Perhaps somewhat surprisingly though, we find very many examples of complete, conformally flat constant positive scalar curvature metrics on the complement of any fixed small perturbation of S . In §2 we prove the following theorem: 

Theorem. Let g0 denote the product metric (1.1) on Sn\S k above, where k < (n-2)/2. Then for every C 3a diffeomorphism τ of S n close to the identity, there is an infinite-dimensional family of positive functions 584 RAFE MAZZEO & NATHAN SMALE 

u such that g = u ίn ~2~g is a complete metric on S n\τ{S k) and has scalar curvature equal to R n k where ~g is the usual round metric on S n . These solutions are parametrized by functions in a certain Holder class on the sphere S k with small norm. 

See Theorem (2.21) for the complete statement. This changes the focus of questions from those concerning existence of complete constant posi-tive scalar curvature metrics to those concerning the variety of complete metrics on a given domain with the same constant positive scalar curva-ture. It is important to remark that our methods break down in all other cases, i.e., when k > (n - 2)/2. We also study the analogous question for arbitrary k -dimensional sub-manifolds of Sn, still assuming k < (n - 2)/2. Although we do not produce global examples in this generality, we can construct local ones. 

Theorem. Let % be a tubular neighborhood of the submanifold N c

Sn . Then for every C 2'a function φ on d% close to the identity there is a complete metric g = w4/(/2 ~2) g0 on %f\N with scalar curvature R n k and such that u\ d# = φ. 

Again, see §3 for a more precise statement. These theorems are proved by the implicit function theorem and the technique of contraction mappings applied to the nonlinear PDE which governs the change in scalar curvature under a conformal change of metric. In either case one needs very good control of the linearized operator. This linear operator turns out to be the Laplacian plus spectral parameter Δ + λ

on sn~k~ι x H^ + 1 in the first case and an operator essentially equal to Δ + λ/r 2 on the product of the ball in R" with some compact manifold in the second; here r is the polar distance variable in the ball. Degenerate operators such as these have been studied from several dif-ferent perspectives. The path taken here is based on earlier work of the first author [16]—[18]), which itself is an outgrowth of a general framework for the treatment of a wide variety of degenerate operators due to Melrose ([23], [24]). Detailed analysis of operators with specific types of degen-eracies using these ideas has been carried out in several cases. Beyond the references above the sources [25], [6], [21] should also be mentioned. The fourth section of this paper contains a fairly complete development of the analysis of Δ+Λ(JC) on sn~k~ι x H ^ 1 and other related manifolds acting between natural families of weighted Sobolev and Holder spaces. Here λ(x) is a function converging to a constant along the set of degen-eracies. In particular, we prove that A + λ(x) has closed range on these spaces for all but a discrete set of the weight parameter. We say closed CONFORMALLY FLAT METRICS 585 

range because in general there is an infinite-dimensional kernel or coker-nel. However, for certain values of the weight parameter this operator is actually Fredholm. This is well known in the weight 0 case, since this is just the usual L2 theory of the Laplacian. We are most interested in the spaces for which the operator is actually surjective, since this is necessary in the implicit function theorem and contraction mapping arguments. In any case, we can characterize the spaces for which Δ + λ(x) is injective, surjective, semi-Fredholm, or Fredholm. This should be compared to the analogous case on conic spaces where the Laplacian is Fredholm for all but a discrete set of weights [25], and the identical situation for the Laplacian on R" (which is really a conic operator in disguise) [22]. Operators with this type of degeneracy have been studied by others. The theory developed here was actually undertaken by Melrose and Men-doza after their work in [25], although this work was never completed. Nonetheless, their work would certainly have followed a similar path to that developed here. Rempel-Schulze and Schulze [29] have developed a very complete operator calculus paralleling the one here. We have not used their approach due to the specific requirements of the problems con-sidered. The work of Graham and Lee [7] should also be mentioned. They use the theory of "uniformly degenerate operators" developed in [17] in a nonlinear problem concerning Einstein metrics. These operators corre-spond to the one under consideration if there is no spherical factor. Other approaches to such operators have been taken in [4] and [15]. Concerning this last we shall say more. In that paper it is proved that if h is a smooth metric on the compact ^-dimensional manifold M, and if p is a nonneg-ative function which vanishes only on the fc-dimensional submanifold N

which equals the distance to T V in a tubular neighborhood, then the Lapla-cian for the metric g = p~ 2h is Fredholm on certain weighted Sobolev spaces for a narrow range of weights. These types of metrics generalize those considered in [17], [2]. The connection with the present work is that this Laplacian exhibits exactly the same sorts of degeneracies as Δ + λ on 

ςn-k-ι χ jjfc+i j n fac ^ t j i e r jnethod j s t 0 fi rst a n a i y Z e a model operator on the product manifold R + xsn ~k ~{ x N, just as we do in §4. In fact, our methods work equally well in this more general situation. We develop our theory in §4 in this setting and extend their results to prove the following: 

Theorem. Let P = Δ + λ(x) , where Δ is the Laplacian on M\N with respect to the metric g described above and λ(x) is any smooth function on M\N which tends to a constant value along N. Then P: r H +2 -> 

rδHk is semi-Fredholm for δ £ Λ, where the Sobolev spaces r δHk are 586 RAFE MAZZEO & NATHAN SMALE 

defined precisely in (4.4) and Λ is a discrete set which is described in 

(4.16). Furthermore there is a {possibly empty) interval (-δ 0, δ0) in which P: r δHk+1 -• rδHk is actually Fredholm of index 0. There is an analogous assertion for P acting between weighted Holder spaces. 

Thus, we not only generalize their results to the full range of weights, which is important in certain applications such as the ones in this paper, but we also extend all results to Holder spaces. The first author would like to thank Marc Burger for many helpful dis-cussions and both authors wish to thank Richard Schoen for his interest in this work. 

2. A global result 

In this section we investigate the existence and variety of complete met-rics on Sn\τ(S k) conformal to the standard metric and having constant positive scalar curvature; here τ is an embedding of Sk into Sn close to the identity. As noted above, it follows from [28] that for such a metric to exist, we must have k < (n - 2)/2, and in fact we will assume in the rest of this section that k <{n- 2)/2. Let ~g denote the standard metric on Sn .As shown in the introduction, (S n\S k, ~g) is conformally equivalent to the complete metric (S n\S , g 0), where g0 is the product metric which has scalar curvature R(g 0) = R n k > 0. We will show by a perturbation argument that for every C 3 α embedding τ of Sk in Sn close to the equator map there is an infinite-dimensional family of complete confor-mal metrics on Sn\τ(S k) of scalar curvature equal to Rn k . In fact, we will show that the set of such metrics in a neighborhood of g0 has a nice manifold structure parametrized by its tangent space, which may be iden-tified with the product of an infinite-dimensional space of eigenfunctions for the Laplacian on Hk+ι with the tangent space of the Banach manifold of embeddings τ: Sk —> Sn as above. If u is a positive function on a manifold M with metric # 0 and scalar curvature R(g 0), and g = u4^n~2^g 0 is a conformally related metric with scalar curvature R(g) , then it is standard (see [13]) that u satisfies the differential equation on M, where Δ = Δ is the (negative definite) Laplace operator acting CONFORMALLY FLAT METRICS 587 

on functions on M. The operator   

> TΛn-2

is known as the conformal Laplacian because it satisfies the transformation rule (2.2) L (uφ) = u L (φ). 

We shall set up the problem of finding a complete metric on Sn\τ(S k)

conformal to £ with scalar curvature Rn k by reducing it to solving a PDE on Sn\S k which is a special instance of (2.1). To do this, first assume that τ is extended to be a diffeomorphism close to the identity of all of Sn to itself. We shall be more specific about its regularity and other properties later. We seek a function ϋ on Sn\τ(S k) such that and such that f) 4//(/ί ~2) g is complete. Transfer this equation from Sn\τ(S k)

back to Sn\S k by applying τ* to both sides. We use the fact that by the naturality of the conformal Laplacian, τ*(L gw) = L^ τ*g>) (τ*w) for any metric g and any function w . Setting υ = τ*ϋ we get 

/ v I n " 2 R v{n+2)/{n ~2) - 0 

Next, apply the transformation rule (2.2) with u the function on Sn\S k

such that w 4 / ( n ~2 ) ^ equals the product metric g0 of (1.1) and with v = u(l+w). The result is that Here g(τ) is the metric u4/(n ~2) τ*J on Sn\S k.Clearly the process described above is reversible. Any metric on 

Sn\τ(S k) conformal to the standard one must correspond to a pair (τ,w), 

the uniqueness of which we shall examine later. Let (2.6) H(τ, w) = L, ( t ) (l + «/) for « J 6 C 2 ' a i " ( s V ) a n d T a C 3 ' a diffeomorphism of S" (the Holder spaces ck'a'v will be defined in (2.9)). We shall determine all solutions of H(τ, w) = 0 close to the known solution (/, 0) by using the implicit 588 RAFE MAZZEO & NATHAN SMALE 

function theorem. To do this, we must first calculate the linearization of 

H, then set up appropriate function spaces on which this linearization is surjective. Then an application of the (soft) implicit function theorem will complete the result. Let us first compute the linearization. Although we only need to estab-lish surjectivity at (/, 0) and only in certain directions, it is also necessary to show that this derivative has continuous dependence on (τ, w) in aneighborhood of (/, 0) in the uniform operator topology. This will be established later. At a given τ the derivative of H in w is computed as 

d\ wH(τ, w)φ = ^H(τ 9 w + tφ)\ t=Q 

= L(τ, w)φ. 

Note that (2.7') L(I,0)φ = (A + (n-2k-2))φ. 

For convenience, we will often denote L(1 , 0) by L. On the other hand, to compute the derivative of H in τ at a point (τ,w) let τ(ε) denote a path of diffeomorphisms such that τ(0) is equal to the fixed map τ . Then 

# '"» f. ε=0 ε=0 

The operator on the right in this formula is some second-order operator acting on 1 + w .Finding solutions of (2.1) will involve studying the linearized operators (2.7) and (2.8). In order to do this we must first defined the appropri-ate function spaces in which we will work. In H ^ 1 we will often use coordinates and metrics given by the Poincare model; that is, we iden-tity H/ c + 1 with BM , the unit ball in R* + 1 , endowed with the metric 

> g

.. = 4(1 - s2)~ 2dx idx j, where s = \x\, s e [0, 1), and x e B k+ι . Let 

z = { s 9 θ , y ) 9 5 > 0 , 0 < E S n ~ k ~ ι , y e S k . W e a l s o d e f i n e t h e c o o r d i -n a t e f u n c t i o n r = r(s) = 1 - s 2 . F o r i/ e R , & e N = { 0 , ! , • • • } , a n d CONFORMALLY FLAT METRICS 589 

a e (0, 1) we define the weighted Holder space 

> (9 0)

= {ueC l0C (S x H ) : | M | f c > β > I / < o o } , 

where | \k a v is the norm 

(2.10) 

Here V 7w denotes the yth covariant derivative of u on sn~k~ι x H f c + 1 ,and z = (r, 0, y), z' = {r , #', y) note that we might equally well have used the vector fields rd r, rd y, dθ in place of V near r = 0. Note also that u e C k'a'v iff u = rvv , t; G C * ' " ' 0 . It is trivial that C*' a > 1 / 

is a Banach space and that for k' > k, v > v , and a > a we have £,* ,α ,1/ Qc k>a>" m These spaces have been used in other nonlinear prob-lems involving degenerate or singular PDE (see [30], [7], [12] for example). We will now discuss for which Jacobi fields φ (i.e., for which solutions of Lφ — 0), φ G C2'a'u with \φ\ 2 small, and with appropriate values of v , one expects a corresponding solution of (2.1). We first give a brief discussion of those Jacobi fields for this problem which are in C 2 ' a ' v . We note that there is a Poisson integral formula which represents these Jacobi fields (which are eigenfunctions of the Laplacian on sn~k~ι x Hk+ι ) in terms of their boundary values [8]. However, we shall analyze them briefly using separation of variables so as to see explicitly how they fit into the Holder framework. First let us record the form of the operator L in the polar coordinates (s, θ) , s e [0, 1], y e S k for the ball Bk+ι , and 

θeS n'k'1:As 590 RAFE MAZZEO & NATHAN SMALE 

Now let 0 = μ\ < μ\ < μ\ < be the eigenvalues for -A sk with corre-sponding orthonormal eigenfunctions <p 0, φχ, , A yφt = -μ' iφi, i € N . Similarly, we let 0 = λ\ < λ] < and ψ0, ψx, be the eigenvalues and orthonormal eigenfunctions for -A θ on Sn ι . If u(s, y, θ) =

Σj ιaj ι( s)<Pj(y)Ψι{θ), t h e n f r o m (2.11) L u = 0 i m p l i e s t h a t L ι a i l =

0, where (2-12) 2 2 

The eigenvalues A^ and μj are nonnegative integers: 

μ) q{q + k-\) for some ί € N , A7 = ^(^ + n - k - 2) for some q e N. L^. 7 is an operator on [0,1] for which both endpoints are regular singular points. The indicial roots at s = 0 are (2.14) where we have used (2.13). It follows from this that there is a unique solu-tion a. ι to Lj {a. ι = 0 such that u. ι = a. ι(s)φ j(y)ψ ι(θ) is regular at 

s = 0. To calculate the indicial roots at s — 1 we shall use the expression for Lj ι in terms of the coordinates (r , θ, y) , r = 1 - s2 :L. 7

(2.15) From this it is easily seen that the indicial roots at r = 0 (i.e., 5 = 1 ) are 

## (2.16) yf = τ = 

Let D / = ( | ) 2 + ^ - ( « - 2 f c - 2 ) . By (2.13) Z^ = ( | for some ^ e N . If Dι > 0, then y^ are both real and distinct and the two approximate solutions of L.a = 0 are rΊι . Furthermore, yj < | < γ~}~ 

so near r = 0 only rγ' is in L2{r~ k~x drdy). This implies that the solution of Lj ιa], ι = 0 which is regular at Λ1 = 0 must have leading CONFORMALLY FLAT METRICS 591 

term rΊι in its series expansion near r = 0, for otherwise the function 

Uj(r, y) = cij(r)<Pj(y) would have leading term rΊι in its expansion near 

r = 0, hence would be an L2 eigenfunction for the Laplacian on Hk+ι 

such an eigenfunction is known not to exist. On the other hand, we are interested only in bounded solutions, which necessitates yj > 0. By the expression for Dι recorded after (2.16) this happens only when q = 0, i.e., / = 0, in which case we even have γ^ > 0. The corresponding eigenfunction is rotationally symmetric with respect to the θ variables, hence is an eigenfunction for the Laplacian on hyperbolic space. If Dι = 0, then the two approximate solutions are rk/1 and rkl2 log r. It may be shown that the solution regular at s = 0 behaves like r ' log r, but this is unimportant for us. Finally, if Dι < 0, then yf are both complex with real part | . This happens for at most finitely many values of /. Thus, in all cases the unique function u. ^s, y, θ) = a. ι{s)φ j{y)ψ ι{θ) which solves LUj ι = 0, is bounded as s —• 1, and is regular at s = 0 satisfies: 0 < v < \ , Dχ < 0. Let v0 equal either the minimum of the positive values of yj for those / for which Dι > 0, or | if whenever Dι > 0 the corresponding γj~ < 0. Also set / ( α 5 ί / ) = { M f C 2 ' M : L w = 0} for 0 < v < u Q, 0 < α < 1. We have proved the following: (2.18) Lemma. For 0 < a < 1 and v < v 0, the set <f{a, v) is the closure in c 2 ' " ' " of the set of finite linear combinations of the functions a- 0(s)ψj(y), and hence is infinite dimensional. 

We now must examine the map H of (2.6) and its linearization (2.7) and (2.8) more closely. In particular, we must show that H is bounded between the Holder spaces (2.9) and that its derivative is a continuous map uniformly in (τ, w). This is not true for arbitrary diffeomorphisms τ close to the identity, but requires an extra hypothesis. Let p be the "defining function" for the equator Sk c Sn given by u2/{2 ~n) , where     

> M4/(Λ-2) i s t h e c o n

f o r m a i fa c tor relating the product metric g0 and the round metric ~g on Sn\S .(2.19) Proposition. The metric g{τ) = u 4/{n ~2) τ*~g = p~ 2τ*~g has scalar curvature R(g(τ)) = R n k + O(p) as p -> 0 if the metric τ*~g has unit normal v along S k agreeing with the unit normal V for ~g. 592 RAFE MAZZEO & NATHAN SMALE 

Proof. This is very similar to a computation in [16]. In fact, we prove the following general fact. Let M be a compact manifold and N a com-pact submanifold. Let p be smooth on M away from N and suppose that in Fermi polar coordinates around TV, p is a smooth nonvanishing multiple of the polar distance function r (with respect to h) to TV. Define a new singular metric g = p~ 2h. Choose now a full coordinate system 

(r,y, θ) , where y is a coordinate along TV and θ is the coordinate in the polar sphere sn~k~ι. Then the sectional curvature of g evaluated on any family of two-planes P(t) in Tγ{ί) , where γ(t) is a path converging to TV, has an asymptotic development in nonnegative powers of p, and it converges to the constant term in this expansion. In two-planes in the 

r, y directions it converges to -|V/?| 2 , in two-planes in the θ directions it converges to +|V/?| 2 , and for two-planes in the mixed (r 9y), θ direc-tions it converges to 0. This is proved by a straightforward but lengthy computation. Now sum over all two-planes to obtain the scalar curvature. Clearly, R(g) ^ Rnk \Vp\ 2 as />->0. To apply this to our situation, we need only compute \Vp\ 2 along S

with respect to the metric τ * ^ . But this equals 1 if the unit normal for this metric v equals V. q.e.d. To prove continuity properties of H we first introduce the space in which the diffeomorphisms τ live. Because of the previous proposition we shall require that the unit normal of τ*~g along Sk agrees with the unit normal of "g. This is ensured for example by requiring that the differential of τ is an isometry between the tangent spaces TzSn and 

Tτ^z) Sn for z e S k. This is not a restriction, because all we care about is the image τ(S k). Let % be the set of C 3 ' α embeddings of Sk in 

Sn with its natural structure as a Banach manifold. In a neighborhood of the standard equator map in % choose a fixed extension operator, which extends an embedding τ to a diffeomorphism of the whole sphere 

Sn close to the identity which has the normalization condition specified above. Then we regard this neighborhood of the equator map in I? as a Banach submanifold of the group of all C 3 ' α diffeomorphisms of Sn we shall still call this submanifold ί? . (2.20) Corollary. The map H of (2.6) is a C°° map from a neighbor-hood V of (1 ,0) in gχC 2>a>u(S n-k-ιxH k+ι ) to C0>a>u(S n-k-lxH k+l )for v < v χ = m i n ( ^ 0 , 1). 

Proof We first check that H: <M -> C 0 ' ^ . Because τ e C 3 ' α and 

w e C 2 ' a ' " it is clear that H(τ, w) e. c £ ; α . To show that it has the CONFORMALLY FLAT METRICS 593 

correct decay properties we write H(τ, w) = H(τ, w) - H(1 , 0). In this difference, we collect the terms Δ . Jl+w)-A 1, cR(g(τ))(l+w) 

- cR(g 0), and cR(g(τ))(l + w) ( / 2 + 2 ) / ( / I -2 ) - cR(g 0). The first of these obviously lies in c°' a'u . The second and the third may be estimated using Proposition (2.19). The point here is that R(g(τ)) = Rn k + O(p) .Using this in conjunction with Taylor's formula in the nonlinear expression in w shows that H(τ, w) is in c ° ' α ' ί y . The proof that it is a smooth map is very similar. For example, its first Frechet derivative is computed in (2.7) and (2.8). The differential in w is obviously bounded between these Holder spaces, and that its differential in τ is also bounded requires an argument nearly identical to the one above. Note that the restriction 

vχ < 1 follows from the fact that R(g(τ)) deviates from Rn k by a term which is O(p) . Finally, the estimates for all higher derivatives follow similarly, q.e.d. Finally we come to our main theorem: (2.21) Theorem. Let 0 < v < v χ. There is a splitting of C 2'a>lJ into closed subspaces WθJ'ia, v) and a smooth map Φ from the intersection 

^ n ( ? x /{a, v)) to W such that H(τ 9 wχ, Φ(τ, wχ)) = 0. Here we have written w = (w {, w 2) in terms of its f(a,v) and W components. Furthermore, all solutions of H(τ, w) in %ί are obtained this way. The graph of Φ in & x C 2'a'u x C°' a'u is a smooth Banach submanifold. Proof This is proved using the implicit function theorem in the form presented, for example, in [11]. In fact, we have already shown that H is a smooth mapping from the domain into the range. It remains to identify the splitting C 2 ' α ) 1 / = / ( α , i / ) θ ^ and to show that the differential of 

H in the subspace W is an isomorphism onto c 0 ' " ' ^ . This is proved in §4. In particular, this is the content of Theorem (4.55). 

3. A local result 

In this section we prove the rather general result that, at least locally, there is no obstruction to finding complete, conformally flat metrics of constant positive scalar curvature on Sn\A, where Λ is a /^-dimensional submanifold of Sn with k < (n - 2)/2. For such a Λ and for σ> 0 let 

N(σ , Λ) denote the σ-tubular neighborhood of Λ in Sn and N(σ, Λ) its closure. (3.1) Theorem. Let k < (n - 2)/2, 0 < a < 1, and let A c Sn be a C2'a embedded k-dimension submanifold. Then there exists a σ > 0 such 594 RAFE MAZZEO & NATHAN SMALE 

that ~N(σ , Λ)\Λ admits an infinite-dimensional family of complete metrics conformal to the round metric ~g on S n with scalar curvature identically equal to R n k>0. 

Remarks. The proof of the theorem does not really require Λ to be a submanifold of Sn but merely a submanifold of a Riemannian mani-fold of constant positive scalar curvature. Also, the infinite dimensionality of the space of solutions in the theorem will be made more precise later. The boundary values of the conformal factor on N(σ , Λ)\Λ can be pre-scribed as any sufficiently small C 2 ' α perturbation of a fixed function 

Ψ0eC 2'a(dN(σ,A)). 

We now commence the proof of Theorem (3.1). In order to simplify some of the later calculations we stereographically project Sn\A onto Rn \Γ from some point P φ A and note that it suffices to prove the theorem with R Λ\Γ in place of Sn\A and with the flat metric g0 on Rn

in place of the round metric ~g on Sn since stereographic projection is conformal away from P. N(σ , Γ) now denotes the σ-tubular neighbor-hood of Γ in Rn.Let Ω be an open set in Rn . If u is a positive C 2 function on Ω such that the metric g = u4^n~2^g 0 on Ω has scalar curvature R(g) = n(n-l) ,then it follows from (2.1) that u must satisfy the equation        

> /o ->\An(n~2) (n+2)/(/ι-2) r, r,

(3.2) Δ w - h — κ — — L w )n = 0 , u>0, 

on Ω, where Δ is the Euclidean Laplacian on R" . Thus to prove Theorem (3.1), we must exhibit an infinite-dimensional family of positive solutions of (3.2) with Ω = N(σ , Γ) that blow up fact enough near Γ to guarantee completeness of the metric g.For x e ~N(σ , Γ), σ > 0, let r = r(x) = dist(x, Γ). We will consider 

r as a coordinate function on N(σ , Γ). We will also need to calculate the local form of Δ on N(σ , Γ). First, fix σ small enough so that ~N(σ , Γ) is identified with the disc bundle of radius σ in the normal bundle to Γ in Rn that is, where Ny(σ,Γ) is the ball of radius σ in the fiber of the normal bundle to Γ at y . Let y o e Γ . Then there is a neighborhood ^ of y0 in Γ such that 

Ίf(σ , Γ)|^ = ~N%{σ , Γ) is equivalent to the trivial bundle Bn~k(σ) x ^ , where Bn~k(σ) is the ball of radius σ centered at 0 in Rn~k . Let us CONFORMALLY FLAT METRICS 595 

denote by F this bundle map: 

F is a diffeomorphism and a linear isometry from N {σ , Γ) to Bn (σ) x

{y}, y e % . Thus, F gives us a local coordinate system for ~N{σ , Γ) near y 0 .Using polar coordinates (r, 0) on i?""^ as in §2 so that (r, θ, y) are coordinates on Bn~k x Γ, we may define Holder spaces Ck'a'u(N(σ, Γ)) exactly as in (2.9). However, we shall use a slightly different, although equivalent, formulation of the norms (2.10) for these spaces. Thus, we set where the norm on the right is the C ' α ' norm restricted to the set 

{(r , θ, y: s < r < 2s)} with respect to the underlying metric. (3.3) Proposition. Let (x, y) e Bn~ (σ)x^f be the induced coordinates for JV(σ, Γ) near y 0. Then, for u e C 2'a(N{σ , Γ)), 

Au = A^-kU + A^ + e^ u + e 2Vu on B n~k(σ)x%, where V2 and V denote the Hessian and gradient, respec-tively, on N(σ, Γ) and e { and e 2 are C°' a sections of (Sym 2 N(σ, Γ))* 

and TN{σ , Γ) such that for some constant Co independent of x , y, or σ and for any a, 0 < a < 

1. 

Proof Let y - (y χ, , yk) be coordinates for Γ in %, and let g.j 

and gιj denote the coefficients of the metric on N(σ , Γ) relative to the coordinates (JC , y) induced by F . For convenience, concatenate the in-dices of x and y , so that the coordinates of x are x , 1 < i < n - k ,and those of y are y. , n-k+l<i<n. Then, a straightforward computation shows that 

ϊfj, i,j<n-k, ϊu={ 0{r), i< n-k,j>n-k, if. + O(r) , i, j > n-k, >B + *^( r )' *> J ^n~-k, l[r) , i<n-k,j>n-k, £ + O(r), i,j>n-k, 596 RAFE MAZZEO & NATHAN SMALE 

where # * , gj. and gιj , g^f denote the coefficient of the metric tensor and its inverse for Bn~k and Γ, respectively. Now from the standard formulas for Δ, V 2 , and V in local coordinates, the required estimates follow easily, q.e.d. Since we will be finding exact solutions to (3.2) using a contraction mapping argument, we must first have an approximate solution to this equation on "N(σ , Γ)\Γ with which to start the argument. Let uQ denote the function where cn k = {(n-2k-2)/n) {n ~2)μ . Let H(u) denote the quantity on the left-hand side of (3.2). Then u0 is an approximate solution to H(u) — 0in the following sense. (3.4) Proposition. Let 0 < a < 1 and (2 - n)/2 < v < (4 - n)/2. Then there is a constant C χ independent of a, v, and σ such that         

> i2rτ/λ l .~(4—n)/2—v

# V #K)l < Cσ 

Proof. Let y o e Γ and choose coordinates {x, y) as in Proposition ».3) near y. I computes that (3.3) near y. Using polar coordinates (r, θ) for x e B n k(σ) one easily 

> λ(n+2)/(n-2)

and therefore, by Proposition (3.3), we obtain 

\r 2H(u 0)\r-u < r 2-v\e χ\ \V 2u0\ + r2~v\e 2\ |V« 0 |< C2r{A -n)l2 -y < C2a{"-n)l2 -v

as r < σ . Similarly, one can have which completes the proof. Now, (w o)4/( "~ 2) go is easily seen to be a complete metric (near Γ) and 

u0 is an approximate solution to (3.2) in the sense made precise above, so the strategy is to look for solutions of (3.2) which are obtained by adding to u0 a lower order term. Hence we linearize H about u0, and make a Taylor expansion to get (3.5) H(u + u0) = H(u 0) + Lu + Q{u) , u e C 2'a>u(N(σ , Γ)), CONFORMALLY FLAT METRICS 597 

where v€((2- n)/2 , (4 - n)/2) and _ d

(3.6) 

(n + 2)(n-2k-2) 2, 

> A

r u, 

rι d2

Q(U) = / ^ ^ ( l l o 

^o dt 

Let Lo be the differential operator Lo = r L. We see that H(u 0 + u) = 0for ueC 2'a'v(N{σ,Y)) if and only if 

(3.7) Lou = -r 2H(u 0) - r2Q(u). 

We will look for solutions of (3.7) by inverting. Lo on an appropriate 

C°' a'v and using the contraction mapping method to solve (3.7) as a fixed point problem. Before we study the operator Lo we first estimate 

r2Q{u) in C°' a'v.

(3.8) Proposition. For a e (0,1), v e ((2 - « ) / 2 , (4 - « ) / 2 ) , 

> 2

where C 3 is independent of a, v , σ . Proof From (3.6) it follows that and we easily compute that (3.9) r2^H(u 0 + tu) = 

and so, setting p = p(v) = v — (2 — n)/2 ,Similarly, one can check that      

> j2
> 0,a,u 2n-2-2p .^iι/,2

thus completing the proof Thus, for u e C 2 ' " ' ^ , v e ((2 - Λ)/2, (4 - 2)/2), the right-hand side of (3.7) is in C 0 ' " ' " and we can estimate it from Propositions (3.4) and 598 RAFE MAZZEO & NATHAN SMALE 

(3.8). We must then understand Lo as an operator on C 2 ' α ' " . From (3.6) it is clear that is a bounded operator for any v e R, where C 0 ' β ϊ I / is the set { w e C2>β>I/ (JV(σ, Γ)): M Ξ O on dΉ{σ , Γ)} . To understand asymptotics of solutions to Lou = f we introduce eigenfunction expansions on S

and Γ. Thus, let (φ.(y) , μ2.) and ( ^ ( 0 ) , λj) , 7 , / = 1, 2, , be or-thonormal sequences of unit eigenfunctions   

> n-k-l ψι=

By Proposition (3.3) we can regard Lo near any point y0 e Γ as an operator on Bn~k(σ) x Γ. Let u = Σ~/=i Uji( r)<Pj(y)Ψι(θ) Then by the same procedure as in §2, we see that where          

> /-3 m\ rid aΊda iii

(3.10) Ljja = r ~Tϊ + ^ n~k~ l^~^ + ^λ~λι ~ r ^ ) The indicial roots of L 7 at the regular singular point r = 0 are Let D = D(n , k) denote the value of the discriminant in this radical when 

1 = 0, i.e., when Λ, 2 = 0, and define 

-(n-k-2)/2, D<0,  

> VQ,

D>0. 

We note that when D < 0 and v < vn ,has an infinite-dimensional kernel, for in this case for every j the equation 

LjO a = 0 on the interval 0 < r < σ has a nontrivial solution a(r) such that a(σ) = 0 and which blows up like ru° as r -> 0 furthermore, this function is rotationally invariant on »S n~fc ~1, so it exists globally on iV(σ, Γ). However, as in §2, we can still find a right inverse to LQ on the appropriate Holder spaces. This is the subject of §4, where we prove that there exists a bounded map G: C O α ί / -^ C 0 2 α ι / such that LQG = I on CONFORMALLY FLAT METRICS 599 

C 0 ' α ' I / (see Theorem (4.55)). Furthermore, given this map, it is easy to solve the Dirichlet problem. ( 3 . 1 1 ) Proposition. // 0 < α < 1 , 0 < v < u Q ) φ e C 2 ' α ( < 9 7 V ( σ , Γ ) ) , 

and f e C°' a'u, then there exists a solution u = Gφf e C2'a'u to the problem LQu = f on ~N(σ,Γ)\Γ, u = h on dN(σ , Γ) such that 

, , , , ,

Proof. Choose a fixed bounded extension operator E from C2'a(d~N) 

to compactly supported C 2 ' α functions on ~N(σ, Γ)\Γ and set G (/) = 

Eφ + Gf - G(L 0Eφ) . The boundedness of G implies the necessary esti-mate, q.e.d. The following result implies Theorem (3.1). (3.12) Theorem. Fix ae(0,l) and ue{(2~n)/2, min((4-/i)/2,i/ 0 )). 

Then there exists a number ~o — 7τ(n, a , v, Γ) > 0 such that for all σ < σ, and h e C2'a(d~N(σ, Γ)) with \h\ 2a < σ, there is a solution u e C 2'a^(N{σ,Y)) of equation (3.7) with u = h on dN(σ,Γ) and \u\ 2 a v < C 4σ^~ n)l2 ~v for some constant C 4 independent of σ or v . Proof First we note that this does imply Theorem (3.1). For given the solution u provided by this theorem the function u + u Q satisfies (3.2) on 

N(σ, Γ)\Γ and for σ sufficiently small, u+u 0 > 0. Also, u is dominated by u0 so that (u + w o )4 / ( n ~2 ) go is still complete. Let K > 0 be a number to be chosen later, and let σ be small enough that σ{"-n)l2 -vK < 1. Let Bσ κ = {u e C 2 ' α ^ : |ιι| 2 > α > | / < a^-n)i2 -vK} .For u e B σ κ let T(u) denote the solution of 

L0v = -r 2H(u 0)-r 2Q(u) on]V(σ,Γ)\Γ, 

v = h on dlV(σ , Γ) 

given by Proposition (3.11). Then T(u) e C 2 ' " ' " and by Propositions 3.4 and 3.8 we have 

## \nu)\ 2^ < C5 (σ ( 4 -) / 2 -" + \u\l atV + σ) < C ^

since |M| 0 < 1. Therefore, fixing K = C 6 = Cβ(n, Γ, a), we see that T: B ' -> B v . Of course B v is a closed ball in the Banach space C 2 ' a > 1 / , and hence is a complete metric space. Therefore, if T is a contraction, then it has a unique fixed point u, and this fixed point satisfies (3.7) and the other requirements of the theorem. So it suffices to show that T: B v —• B ^ i s a contraction if σ is sufficiently small. 600 RAFE MAZZEO & NATHAN SMALE 

Let v{,v 2e Bσ κ and let w = T(v {) - T(υ 2). Thus, 

L0w = r 2Q(v x)-r 2Q(v 2) onN(σ,Γ)\Γ, w = 0 on dN(σ , Γ), and w = G{r 2{Q{υ {) - Q(υ 2))) . By the boundedness of G

and so by the mean value theorem (cf. [11]) 

> -1

It therefore suffices to show that the quantity can be made arbitrarily small if σ is small. Let vt = v2 + t(υ ι - v 2). Then from (3.6) and (3.9) 

# Tt Q{v <)= Io ^2 c7 (^, 

where vt - jι^ t- Now, using the fact that \υ t\ < C 9rv and l^'l < C9rv ,we get 

id t

r -τ-( 

r' v < (2n-4)/2+2ί/  

> „(

< C1 0 r (n-2)l2+v 

The last two inequalities use that v > (2 - «)/2 and r < oo. One can also derive the Holder estimate similarly. Thus, 

<C nσ* 

which finishes the proof of Theorem (3.12). 

4. Linear estimates 

Because of the degenerate nature of the linearized operators (2.7), (2.8), and (3.6), the relevant surjectivity properties and estimates that we require CONFORMALLY FLAT METRICS 601 

of them for the arguments of §2,3 are not standard. In this section we derive these properties in as straightforward a manner as possible. As discussed in the introduction, there is a general framework for treat-ing degenerate operators such as the Laplacian on Sp x H^ which devel-oped out of the ideas in Melrose's paper [23] and his later paper with Mendoza [25] concerning elliptic operators on compact spaces with conic singularities. In this latter paper it is shown that such operators, which are called totally characteristic, are Fredholm on certain weighted Sobolev spaces for all but a discrete set of the weight parameter. We prove anal-ogous results for the operators considered here, but as these operators frequently have infinite dimensional kernels or cokernels, the best we may hope to prove in general is that these operators, when acting between the weighted Sobolev or Holder spaces introduced earlier, have closed range for all but a discrete set of the weights. In particular cases, either the kernel or cokernel may degenerate to a finite-dimensional space, in which case the operator is semi-Fredholm or even Fredholm. A bit more generally, our interest in this paper is with operators of the form A + λ(x) on the manifold ^n\N . Here λ(x) is a smooth function on Jt\N which tends to a constant value λ on TV and the metric g

on ΛΓ\N is of the form p~ h , where the metric h is smooth on all of 

Jt and p is a smooth function on Jt\N which vanishes on N and for which Vhp = 1 along N. Significant special cases of this are when 

k = 0 or when k = n - 1. The former case corresponds to manifold with isolated conic points which was studied in [25] and the latter corresponds to a manifold with a "conformally compact metric" [16], of which the hyperbolic space H" is a special case. Of course the prototype of the more general situation is Sn\S with the metric (1.1). It is possible to develop a quite general theory for elliptic operators of arbitrary order with degeneracies of the type exhibited by Δ + λ(x) . This will be taken up in [19]. Here we develop a simple version of this theory which is applicable in the special geometric situation described above. These operators warrant interest because of the many geometric and physical problems in which they arise. Introduce coordinates (r, θ, y) on a neighborhood of T V in Jί , where (r, θ) are Riemannian polar coordinates with respect to h around T V and 

y is a local coordinate chart in TV. Introduce also the manifold M which is obtained by taking the union of Jί\N with the spherical normal bundle of N with the unique minimal C°° structure for which the lifts of smooth functions from Jΐ and the polar coordinates above are smooth. Note that 

M has a single boundary on which r = 0. It is straightforward to calculate 602 RAFE MAZZEO & NATHAN SMALE 

(see [16], [15]) that (4.1) A + λ(x) = L + E, 

where (4.2) L = r 1d1r + (1 - k)rd r + Δfl + r2AN + λ

will serve as a local model near r = 0 and (4.3) E = r £ a . α , / ^ θ> y)(rd r)sd^rd y)β  

> j+\a\ +\β\<2

is an error term that we will eventually show is negligible. In (4.2) Δ^ = Ay

is the Laplacian on N with respect to the metric induced by h and Aθ

is the Laplacian with respect to the standard metric on sn~k~ι. (It is the special dependence of L on y that makes the analysis of this section simpler than in the general case [19].) The ultimate goal in this section is to show that Δ 4- λ(x) is surjective on certain of the weighted Holder spaces (2.10). However, it is much easier to approach this operator through L2 methods. Thus, initially our discussion will concern the behavior of Δ + λ(x) on the weighted Sobolev spaces (4.4) 

rδHk{M) = {u: (rd r)j(rdj) a(d/u e r δL2{r-k~X drdθ dy) , j + |α| + \β\ < k}. 

Only later will we return to the Holder framework. The basic strategy is to first analyze the operator L, which we regard as an operator on the space R+ x Sn~k~ι x i V . W e will prove that (4.5) L:r δHk+2 ->r δHk

has closed range for all but a discrete set of values of the weight δ . This is accomplished by constructing a generalized inverse G for L which is bounded as a map (4.6) and such (4.7) that 

LG G: = 1 rδHk -+r*H GL 

where Pχ, P2 are orthogonal projections onto the cokernel and kernel of 

L in rδHk and rδHk+1 . G depends on δ and k, G = G(δ , k) , and does not exist (or is not bounded) when δ e Λ, Λ a discrete set described CONFORMALLY FLAT METRICS 603 

below. We then show that each G(δ , k) is bounded on the Holder spaces (4.8) G : C * α ' I ' - > C * + 2 β l \where v depends on δ . Finally we show that the error E is negligible on these spaces, and so we may use G as a boundary parametrix for on M. In conjunction with an interior parametrix, this shows that 

A + λ(x):r H ^r H ,

has closed range for all but a discrete set of the values δ, v. Then it may be determined for which of these values this map is surjective, Fredholm, etc. Introduce eigenfunction expansions in (θ, y). If (4.10) Ayφj, = -μ)φ j , Aθψ, = -λ*ψ,, 

then on the (j, I) eigenspace, L is reduced by the Fuchsian operator 

> L

J,l = r2d r + (1 " k>dr ~ rl έj ~ λ) + λ-

As recorded earlier, its indicial roots are arranged in two families: 

k

(4.11) s{(l) = 

The importance of these exponents is that it may be proved that an arbi-trary (locally defined) temperate solution of (A+λ)u = 0 has an asymptotic expansion as r —> 0 with terms / / ( '(logr) p and distributional coefficients in (θ , y) . This is proved in the extreme cases k = 0 in [25] and k = n-1in [18], and the general case appears in [19]. However, it is precisely the difficulty of establishing mapping properties for Lj t which are uniform in both j , / that makes the analysis of L

subtle. This approach is used in [4] and [15], but the central difficulty is that one requires knowledge of the asymptotics of Bessel functions of large argument and order, and this, as Watson puts it, is "a problem of a more recondite nature" [31]. Instead we consider the reduction of L only in the variable y . Thus, let (4.12) Lj = r 2d2 + (1 - k)rd r + A θ - r 2μ) + λ. 

This may be rescaled to a j-independent operator on the cylinder C = R+ x Sn~k~ι by the substitution R = rμj :(4.13) Lo = R 2d2R + (1 - k)Rd R + Aθ-R 2+λ. 604 RAFE MAZZEO & NATHAN SMALE 

We first construct an inverse for LQ, rescale to obtain an inverse for L ,and then sum to obtain an inverse for L.The operator Lo is of totally characteristic type [23], but the presence of -R , as in a Bessel equation of imaginary argument, drastically affects its global behavior on C. We couple its known behavior near 0 from [25] with an obvious extension of an ODE argument which appears in [24] to describe this global behavior. Introduce the space (4.14) &k's'p = {u: φ{R)u e R~ δHkb{C) , (1 - φ(R))u e R' pHk{C)} ,where φ e C0°°(RJ , φ = 1 near R = 0, (4.15) Hk(C) = {u: (Rd R)jd°u e L 2(R~ k~l dRdθ) , j + |α| < k) ,and H (C) is the usual Sobolev space based on differentiations by dR,

dθ and with respect to the measure R~ k~ι dRdθ .

(4.16) Lemma. LQ: j^ k+2 >δ>P _> #Ί<>*>P-* isFredholmprovided δ £

A, where A = {±V\yJk 2/4 + λ] - λ}. 

Remark. If δ e A, then RSi{l) just fails to lie in R~ δL2(R~ k~{ dR dθ) 

near R = 0 for some s^l) in the list (4.10). It is easy to prove that Lo

does not have closed range then. 

Proof. L Q is bounded between these spaces regardless of the value of δ .So it will suffice to construct parametrices Hx, H2 for which Hr. β>f k>δ>p+2 

-> %r k+2>δ>P is bounded and such that both errors Qχ = I - L QHχ and 

Q2 = I - H 2L0 are compact on β^ k>δ>p for every k, p . The H{ are obtained by joining together local parametrices near R = 0 and R — oo . The existence of local parametrices in any bounded neighborhood of 0is the principal result of [25] (cf. also [24]), and this step requires that 

δ £ A . We note however that the construction of such local parametri-ces is fairly easy on a "true" cone such as C, i.e., one which is a warped product. For example, in this situation it is now feasible to introduce a Fourier decomposition in θ and construct a parametrix for the family of ODE's which are induced on the eigenspaces. The reason this works is that the homogeneous solutions to these ordinary differential equations are modified Bessel functions in which the spectral parameter appears only in the order but not in the argument, so that uniform asymptotics are easily obtained. Constructions of this type appear in [5]. More sophisicated ar-guments using the Mellin transform in [25] seem to be required to prove the refined regularity results for totally characteristic operators which we need later. CONFORMALLY FLAT METRICS 605 

For the other case we slightly modify an argument from [24]. Consider the partial principal symbol of Lo in R:(4.17) σ(L 0)=A θ-R 2(\ζ\ 2 + l). 

As an operator on L2(S n~k~ι), σ(L 0) < -R 2 , hence \\σ{L 0)~ ι\\ < l/R 2 .So we define a parametrix for Lo near infinity by 

## (4.18) H^f) = Je iRξ σ(L o)-lf(ξ, θ)dξ. 

Clearly is bounded, and furthermore is compact for any A:, p . This last assertion rests on the fact that K is a finite sum of terms, each of which is both smoothing of order at least one and decaying at least like l/R. Thus, K: J?> k>δ>p _> ^k +ι,s, P+ ι ^^ k i δ ' p 9 and the latter inclusion is compact. The same construction gives a left parametrix. Finally, cut-off functions may be used in the usual way to combine these local parametrices to get a global parametrix on all of 

C. But the existence of bounded left and right parametrices with compact error terms implies that LQ is Fredholm. 

(4.19) Corollary. If u e βf k+2 >δ>p« far some k,p o,δ £ Λ, and 

Lou = f, where f e ^ k ' δ ' p for every p, then u e J^ k+2 >δ>p far ev-ery p. If f e β? k>δ>p» far every k, then u e βr k>δ>p«+ 2 far every k. 

Proof Apply the parametrix H2 to Lou = f to conclude that Since Q2: J^ k'δ'p - ; r * + 1 ' * ' * + 1 and H2: ; r * + 2 * * + 2 , the result fol-lows. Because LQ is Fredholm independently of p, the index of LQ is in-dependent of p. Hence by this corollary, since the kernel of LQ is in-dependent of p, so is the cokernel. (This may also be seen by using the argument of the corollary for the adjoint problem.) However, the index does change as δ crosses over elements of the excluded set Λ. Standard arguments now imply the existence of a generalized inverse 

Go for Lo, i.e., an operator satisfying (4.20) GQL0 = I-P l9 L0G0 = I-P 2606 RAFE MAZZEO & NATHAN SMALE 

between any particular choice of the weighted Sobolev spaces %f ' 'p~2 -> 

^k+2,δ, P ^ g £ A H e r e p^ a n d p^ a r e t he orthogonal projections in                                        

> ^k+2j>p and2,k,δ 9p-2 ontothekemelandcokernelofLQNotethat

although GQ does not depend on k , it does depend on p , if only through the spaces on which the Pt are orthogonal projectors, and of course it also depends on δ. We shall regard Go as an integral kernel: (4.21) Gof(R, θ) = JG O(R, Θ9R9 θ)f(R 9 θ)R-k~l dRdθ ,with similar expressions for Pχ and P2 . Note that the identity / is rep-resented by the Schwartz kernel Rk+ι δ(R - R)δ(θ - θ) , the factor Rk+ι 

being included to compensate for the R in the measure. Because GQ

is an inverse for the totally characteristic operator LQ , it has very regular behavior as either R, R — • 0. This structure is described in great detail in [23], [24], [25] (cf. also [9, §18.3]. Thus, we merely quote results which we shall require later. The most important property of the distribution Go on C = C x C

is that it is the pushforward of a simpler distribution on a slightly more complicated manifold. This manifold is the manifold with corners Cb

obtained by "blowing up" C 2 along its corner {R = R = 0} . Invariantly, this process consists of replacing this corner by its interior normal bundle, which is a quarter circle bundle over dCxdC , and endowing this set with the unique minimal differentiable structure for which polar coordinates in the variables R, R are smooth. c\ is again a manifold with three hypersurface boundary faces: the lifts of the faces defined by R = 0 and 

R = 0 on C 2 and the new front face (the spherical normal bundle). Let the lifts of {R = 0} , {R = 0} be called the left and right faces and have defining functions px, p2, and let the front face have defining function 

Pff . C\ also has two corners (codimension two boundary faces) defined as the intersections of the left and front faces, and of the right and front faces. We shall encounter a similar construction for the full parametrix later when the variable y is reintroduced. It is proved in [25] and [24] that the local parametrices Hχ and H2

for Lo near R = 0 used earlier may be described as the pushforward under the natural "blow-down" map C 2 -• C 2 of distributions, which we also call Hi, which have classical conormal expansions at the lift of the diagonal {R = R , θ = θ} to C% and along the boundary faces {p χ = 0} , 

{p 2 = 0}. They are smooth up to the front face away from the diagonal and are extendible across the front face near the diagonal. For information CONFORMALLY FLAT METRICS 607 

about distributions with classical conormal expansions, see [9, § 18.2]; these are often also called polyhomogeneous distributions, and their expansions are called polyhomogeneous. We shall frequently use these distributions here. Near a boundary with defining function p these expansions have the form P{Sj) &{Sj)^κx> p=0 

where z is a coordinate chart in the boundary, and all coefficient functions are smooth. We shall denote by ^ ^ the subclass where the exponent 

s0 of lowest order equals v . We shall also use the notation s/K = srf" h'° to denote the space of such distibutions with no log factors in the term of lowest order. The most important consequence of the fact that the inverting kernels live in these spaces is that they have definite rates of decay at all boundary faces. We shall deduce this structure for all the operators with which we are concerned here. Before we proceed further, it will be useful to have the explicit for-mulas for the transposes L* o , GQ of the operators Lo, Go . Of course, the transpose is taken in a particular one of the weighted L spaces. Rather than determine the transpose on an arbitrary one of these spaces, we shall restrict attention to only those spaces ^k'δ>p for which p = δ - 2k for k G N . In particular, our fixed L2 space will be JΓ 0'*' 3 =R~ δL2(R~ k~ι dRdθ) . Because L o is symmetric when δ = 0, the adjoint of Lo in R~ δL2 is (4.22) L[ = R-2δ L,R 2δ .

On the other hand, using the expression (4.21), the adjoint of G o on this space is (4.23) G [ { R , Θ , R , Θ ) = R ~ 2 δ G 0 ( R , Θ9R, θ ) R 2 δ .

Of course, Pχ, P2 are orthogonal projections in R~ δL2 , so that (4.24) Pl(R,θ,R 9 θ) = P+R, Θ,R 9Θ), i = 1 , 2. Now we turn to the determination of the exact behavior of Go at infinity and at the boundary faces. (4.25) Lemma. PftR, θ,tR,θ) and G Q{tR, θ,tR,θ) are rapidly decreasing as t —• oo locally uniformly in (R , θ, R, θ) for Go this is only true if (R, θ)φ{R, θ ) . 608 RAFE MAZZEO & NATHAN SMALE 

Proof Since the P. are finite rank projections onto the kernel and cokernel of LQ, their rapid decrease is guaranteed by Corollary (4.19) applied to both Lo and L* o . To deal with GQ, fix R Φ R and con-sider t h e function F(t,θ,θ) = G Q(tR 9 θ,tR,θ). Then, since L[G[ = R~ 2δ L0G0(Rj , θ)R 2δ = I-P 2 so that (4.26) L R Θ ° O ( R , Θ , R , Θ ) = I - R 2 δ P 2 ( R 9 Θ , R , θ ) R ~ 2 δ ,where L ~ 0 9 L — represents L Q acting in either (R,θ) o r (R,θ), it follows that 

(t 2d2 + (1 - k)td t+ AΘ+A~+ 2λ - t 2R2 - t 2R2)F{t, θ, θ) = (L RΘ G0)(tR ,θ,tR,θ) + (L~~G 0){tR ,θ,tR,θ) = -P χ(tR,θ,tR,θ)- R2δ R~ 2δ P2(tR,θ,tR,θ) 9

the delta functions, which represent the identity, are zero because (R, θ) Φ(R,θ). But for fixed R, R this is an equation of the form LfF = G, 

with G e / ' ' for every k, M. The proof of Lemma (4.16), hence also of Corollary (4.19), work perfectly well for the operator L1 and so F

is rapidly decreasing in t.(4.27) Lemma. P.(R 9 Θ,R,Θ) and G0{R, Θ9R9Θ) are rapidly de-creasing as i? —• oo locally uniformly in (θ , R,θ), R>0, and as R-+ oo 

locally uniformly in (R , θ, θ ) , R>0. Furthermore, the coefficient func-tions in the asymptotic expansions for the P ( and G o as R —• 0 are rapidly decreasing as R -> o o , and vice versa. Proof Both assertions are obvious for the P. from Corollary (4.19) and, using this, the proof for Go is very similar to that in the previous lemma. We shall wait to determine the leading exponents in these asymptotic expansions. The next step is to rescale Go back to a generalized inverse for L. , and thus obtain the full inverse for L. Recall that L. is obtained from Lo

by the substitution R = rμ^ . Since from (4.20) and (4.21) 

L 0 G 0 = R M δ ( R - R ) δ ( θ - θ ) - P χ ( R 9 Θ 9 R 9 Θ ) 9

this rescaling transforms this equation into 

L.G^rμ. , θ, fμ. , θ) = μ k/+x δ(r - f)δ(θ -Θ)-P χ(rμ j, θ, fμ j , θ) CONFORMALLY FLAT METRICS 609 

here we have used that δ(R - R) is homogeneous of degree - 1 . This forces the definition (4.28) Gj(r,θ 9ϊ9θ) = μJ kG0(rμj , θ, rμ. , θ) ,so that Gj satisfies (4 29) LjGj = rk+ιδ(r-r)δ(θ-θ)-P lj (r 9θ,r 9θ) 9 

> GJLJ

= rk+l δ(r-r)δ(θ - Θ)-P 2j (r 9 Θ9f9θ) 9

where 

P u { r 9 Θ 9 f 9 θ ) = μ ^ P f r μ . 9 θ 9 f μ j 9 θ ) 9 i = 1 , 2 . Finally, we define the full inverse for L to be (4.30) G{r 9θ9y9r9θ99) 

with similar definitions for the projectors P.(r, θ, y , r, θ, y) in other words G = {-A y)~ x GQ(J-A yr, θ, J-A yr, θ) . It remains to prove that G is actually bounded between the weighted Sobolev spaces (4.4).     

> /? 9A^^ 9

(4.31) Proposition. G: r L —» r H is bounded provided δ fi Λ . Proo/ It suffices to prove that G is bounded between rδL2(r~ k~~ ιdrdθ) 

and {u:urd ru, r2d2u, dθu, d2u, rμ.u, r2μ2u e r~ δL2} = r~ δH2 uni-formly in j . It is easy to check that the rescaling transformation 

f(R, θ) -> f(r, θ) = μ δ-k/2 f(μ jr , θ) 

is an isometry between R L and r~ L . Then, a change of variables in (4.20) shows that G-f — G of, so with all norms in either RΓ δL2 or 

## rδL2:

(4.32) \\Gjf\\ = \\GJ\\ = \\G of\\ < C\\f\\ = C\\f\\ ,with C the norm of Go: R~ δL2 —• R~ δL2 , hence independent of j . The same argument can be applied to rd rGj , r2d2G , djJGj, rμ 2Gj, r2μ2Gjy 

since all of these operators are simply the rescalings of Rd RGQ, , R2G0,

all of which are bounded on R~ δL2 since G o : &°> δ-δ -> ^ 2 5 < M ~ 2 . This sort of argument is taken from [16]. q.e.d. An identical argument shows that Pχ, P2 are also bounded on rδ L2 in fact, using Corollary (4.19), P.: r δL2 -• /^°° . In addition, by a change of variables, Pij oP ij = P tj , i = 1, 2 for all , so that P{, P2 are still pro-jectors. Notice also that unless Pt(R , θ, R, θ) = 0, P.(r, θ, y, r, θ, j>) has infinite rank. 610 RAFE MAZZEO & NATHAN SMALE 

We have now proved that (4.33) LG = I-P {, GL = I-P 2.

By commuting derivatives through the argument of (4.31) we obtain that (4.34) L: rδHk+2 -> rδ Hk, G: rδ Hk -> rδ Hk+2 , P. : rδHk - / ί / * + / 

are all bounded for every k , I. In particular, L has closed range whenever 

δ $ A. 

The distributions G, P( naturally live on a "blown up" version of the product T xT , where T = C x N. This is defined in a manner analogous to that used earlier in defining M and C^ . The product T is a manifold with a corner, and its corner has a natural submanifold which is defined by S = {r = f = 0, y = y} . We define Γπ2 to be the union of T\S 

and the spherical normal bundle of S in T , endowed with the minimal differential structure for which the lifts of smooth functions on T2 and the polar coordinate functions about S are smooth. In fact it is convenient to use these polar coordinates from time to time. Thus, let 

r2 + \y-y\ 2, ω = (r , y - y , f)/p ff = ( ω 0 , ω , ωk+ι ). 

A full set of coordinates near S are {Pff, ω, y , θ, θ) . Γ2 has three bounding hypersurfaces which are defined by {ω 0 = 0}, {ω k+ι = 0}, and {pff = 0} in analogy with c\ we shall let px = ω 0 and p2 =co k+ι . Because of the rapid decrease of Go, Pi proved in Lemma (4.25), the distributions G, P. are smooth in all variables in the interior of T2

(although G still has a singularity along the diagonal) because of the rapid convergence of the sum (4.30). Also, G and the P. still have asymptotic expansions as pχ —> 0 and p2 —• 0 because of Lemma (4.27). There are more general arguments which would guarantee the existence of these asymptotic expansions [24], but the existence of these expansions is not subtle in the present circumstances. Because we know the boundedness properties (4.34) we can determine the exponents in the leading terms of these expansions. (4.35) Proposition. P{, P2, and G are polyhomogeneous on all faces of T2 . These distributions are smooth in the normal variable p ff to the front face and Pχ, P2 are smooth in all variables there. At the side faces these distributions have polyhomogeneous expansions, which may be described as follows: Pχ e $/p hg at both side faces with leading coefficient an eigenfunc-tionfor Δ^, or Δ^, and with s one of the indicial roots in the list (4.10), 

9i(s) > I + δ P2e Λfphg 23 with leading coefficient again an eigenfunction CONFORMALLY FLAT METRICS 611 

in θ , θ and with 9\(s) > \ + 3δ , s α« indicial root; on the left face either G e srf* hg) K(s) >\-δ or Ge ^ , 9t(j) > § + <J, and on the right face either G e sf pshg , 1Λ(s) > \ + δ or G e s/*^, 9ΐ(ί) > \ + 3δ in each of these cases the leading coefficient is an eigenfunction in either θ , θand s is an indicial root. Here we have used the variables r, f instead of pχ, p2 as defining functions for these side faces for simplicity. Proof The existence of these expansions and the smoothness of the co-efficients was commented on earlier. The leading term in any one of these expansions solves the relevant equation to first order, so the coefficient of either r or f is an eigenfunction in either θ or θ with the exponent related to that eigenvalue. It remains only to determine the precise values this leading exponent may take. First of all, since Pχ, P2 are projectors on r L their integral kernels are symmetric; hence for them it suffices to determine their leading terms only on the left face. Since LP χ = 0and LιP2 = 0, the leading exponent in each of these operators must be an indicial root for L or Z/ = r~ Lr , respectively. Hence for P{ the leading exponent is some indicial root in the list (4.10), and for P2 it is 

s - 2δ , s as in (4.10). But now we must use their boundedness on rδL2 :it is proved in [16] (see also [17], [24]), that in the case where there are no 0-variables, an operator of this type which is in fl^/' a t ^and Af pbh'f r at the right face are bounded on rδI? provided 

(4.36) 9t(α) + δ > I , j

The presence of the additional θ variables does not alter this criterion. Applying this to Pχ we see that the indicial root must satisfy fΆ(s) > | +δ , 

and for P2, 9ΐ(ί) = M(s) - 2δ > \ + δ => 9t(j) > \ + 3δ . Then, since by (4.33) Lrθy G = -P χ and L^G = -r~ 2δ r2δ P2 near the two side faces, either the leading terms of G at these faces must be annihilated by L,in which case the leading exponent is an indicial root and there are no logarithms in the terms of lowest order or L applied to the leading term must match the leading term of either -P χ or -r~ 2δ r2δ P2, so that the leading exponent must be the same and the lowest order terms for G

would require a logarithmic factor. Finally, using (4.36) again gives lower bounds on these leading exponents. This proves the proposition in all cases. We come now to the Holder estimates for L. First we prove an a priori estimate for an arbitrary solution of Lu = f. In this the ck+2 'ayl/ 

norm of u is estimated in terms of the ck'a'u norm of Lu and, for 612 RAFE MAZZEO & NATHAN SMALE 

example, the C 0 ' 0 ' " norm of u. This estimate is quite simple and uses only the scale-invariant nature of the Holder spaces (2.5) and the scale-invariance of L. Such estimates appear also in [7]. We should note that it is impossible to prove an a priori estimate which would imply that for a fixed / an arbitrary solution u to Lu = / decays at the same rate as / . In fact, it is possible to find solutions to Lu = 0 for which u has arbitrarily bad growth in some thin set which converges to the boundary. However, from the theory developed earlier in this section, if u G rδ L1

and Lu — 0 then u e rδHk for any k. A scaling argument involving the Sobolev embedding theorem now shows that u e C k'a'δ for any k.The second step in dealing with the properties of L on Holder spaces is to decide for which f e c k'a'u there exists some solution to Lu-f for which u e C + α z / . Of course the natural choice for a solution were it to exist is the solution u = Gf, where G is the generalized inverse of 

L with respect to a particular δ. However, first we prove the a priori estimate. 

(4.37) Proposition. Given any k,a,u if Lu = f, where u e Ck+2 'α'", 

so that feC k'a'v, then 

Proof. Use the usual local coordinates (r, θ, y). Partition T up into boxes B. which have the property that they approximately equal the sets 

{dJ2 < r < 2d i, \y - y o\ < d t} , and choose slightly larger boxes E D B i

which have dimensions in r and y larger than B by a fixed factor 1 + ε .For each / choose an affine map f. (relative to these coordinates) which carries a fixed box E = {^ < r < 3, \y\ < 2} , say, to E . Now it is easy to calculate that f*Lu = Lf*u for any u, and furthermore if u is a function on E, then Now by standard elliptic (4.39) Use the notation ui =theory  

> M / c + 2 a,v
> δ

"\fi U\k,a = \ U\k, 

u\ E , and υt = u\       

> ^=SUP\Ui\k +2, a,u

= supd'f\f*u i\k+2 

(4.40) 'which is the desired inequality. CONFORMALLY FLAT METRICS 613 

To accomplish the second step in the analysis of the behavior of L

on Holder spaces, as discussed earlier, it will suffice to prove that the generalized inverse G and the projectors P. are bounded on these spaces. (4.41) Proposition. For any δ φ Λ, the corresponding operators G, Pi are bounded between C k'a'u - Ck+2 'a'u and C k'a'u -+ C Ua *υ for any k, a, I, and for v - | -δ. Thus, the set Λ' of omitted weights is precisely the set of real parts of the indicial roots (4.10). 

Proof We give a proof only for G, the proof for the Pi being even simpler. First write G = G f + G" , where G' is supported in the set (4.42) {±<r/r<2,\y-y\<p ff }, 

hence contains the singularities of G along the diagonal, and Gn is smooth on the interior of 7^ and carries the conormal singularities of G along the sides given by (4.35). The proof that G' has the correct boundedness properties is very similar to the argument in the previous proposition. To see this we must first represent the action of G'u as an integral. For this it is most convenient to use projective coordinates (r, θ, y, t, θ, w) 

on Tπ , where t = f/r and w = (y — y)/r . It is easy to see that these are smooth in the interior of T% and up to the front face and the side face 

pχ = 0, but are singular at the other side face. The fact that G! is the pushf orward of a distribution on 7^ means that there exists a distribution 

g'(r,θ,y,t,θ,w) such that g is supported in (4.43) {\ <t<2, \w\< 1} 

and (4.44) G'U= ί g'(r, θ 9y,t, θ, w)u(tr, y - wr, θ)Γ k~l dtdw. 

In this formula we have used the fact that r = tr and y = y - rw . Now, use the same partitions of T into boxes Et and Bt and the same affine maps fi as in Proposition (4.37). The same reasoning as in (4.40) may be used. Thus (4.45) < supC,.<|^M| t j , < supC.-lKl* B,  

> ii'

The first inequality holds because each f?Gf is a pseudodifferential op-erator of order - 2 , hence is bounded between C ' α -> C + ' α on the 614 RAFE MAZZEO & NATHAN SMALE 

fixed box E. The desired estimate will hold if we show that the Cλ are independent of /. But this is true because the family of pseudodifferential operators f*G' on E is uniformly bounded in Ψ~ (E) , which in turn is a consequence of the smoothness of G in the parameter p^ .For G" we argue in two steps. First we need to show that G"u is defined for any u e <g ?k >a'1/ . Using the integral representation (4.44) it is clear that we only need check that if u = / then the integration there is well defined. Since the kernel of G ~ f as f -> 0 (i.e., on approach to the face {p 2 = 0}), with s an indicial root, s > § +δ by (4.35), i.e., G" ~ ts

as t -• 0, we need to check that /J j s +I / -f c -1 dt < oo. But j + z / - fc > 0, so this is true. The second step is to prove that if ueC k'a'u , then G"u e ck+2 'a'ι/ .First note that it will suffice to merely prove that G"u € C°'°' v , because in fact any number of the derivatives rd r, rd , dθ , etc. may be applied to Gπ and the resulting operator will always have the same form as G" 

with the same asymptotics at all boundaries. Thus, we will actually have          

> G"ueC l'β'vfor any l,β,v. Now |fG"u\ < J \G"\ \U\ . Since |(?"| is