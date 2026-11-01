---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Gluing Construction of Einstein Manifolds]

# Gluing Construction of Einstein Manifolds

> Source: https://asset.library.wisc.edu/1711.dl/FBMRGHXECU44I8K/R/file-e4290.pdf
> Fetched: 2026-10-04 22:12
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
  "source_url": "https://asset.library.wisc.edu/1711.dl/FBMRGHXECU44I8K/R/file-e4290.pdf",
  "metadata": {
    "provenance_urls": [
      "https://asset.library.wisc.edu/1711.dl/FBMRGHXECU44I8K/R/file-e4290.pdf"
    ],
    "search_origins": [
      {
        "source": "tavily",
        "query": "\"\"several\" ALE spaces Einstein gluing multiple cores interaction connected sum\" original authoritative source"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

(9.2) Proof. Since h and k1 both have quadratic leading terms, and gcal is ALE, there exist constants c and c1 so that |h|gcal(p) ≤cρ2(p) (9.3) |k1|gcal(p) ≤c1ρ2(p), (9.4) for any p ∈Xt. Similarly, there exists a constant c2 so that |o|gcal(p) ≤c2ρ−2n(p), (9.5) 78 for any p ∈Xt. It follows that |th|gcal(p) ≤cρ2(p) ≤1 2ct 1 2 (9.6) |tuk1|gcal(p) ≤c1uρ2(p) ≤1 2c1ut 1 2 (9.7) |tuo|gcal(p) ≤c2uρ2(p) ≤1 2c2ut 1 2 (9.8) The right hand side is independent of p so ht,u is a Riemannian metric for suﬃciently small t and u. Recall that dgcalRic(h) = Λgcal + λo (9.9) dgcalRic(o) = 0 (9.10) dgcalRic(k1) = o, (9.11) so we have Ric(gcal + th + tuk1) = Ric(gcal) + dgcalRic(th + tuk1) + Q(th + tuk1), (9.12) where, using (4.14), Q is a nonlinear term satisfying |Q(th + tuk1)| ≤b  |Rmgcal||th + tuk1|2 + [...] (3.32) 26 Proof. Recall from (2.41) that o = 1 1 + r2n  −gcal + n(dr ⊗dr) + n(θ ⊗θ)  , (3.33) so in ALE coordinates, we have o = 1 r2n  −geuc + n(dr ⊗dr) + nr2(θ ⊗θ)  + O(r−2n−1) (3.34) as r →∞. Deﬁning oeuc = 1 r2n  −geuc + n(dr ⊗dr) + nr2(θ ⊗θ)  , (3.35) we have lim r→∞ Z Sr/Γn n + 1 r ⟨H, o⟩dSSr/Γn = Z |x|=1 (n + 1)⟨H, oeuc⟩dSSr/Γn.
(3.36) The inner product is ⟨H, oeuc⟩= −⟨H, geuc⟩+ n⟨H, dr ⊗dr⟩+ n⟨H, r2θ ⊗θ⟩.
(3.37) We lift up to R2n, and next we calculate each term in (3.37); the ﬁrst term is ⟨H, geuc⟩= Hijllxixj, (3.38) so by (3.22), Z |x|=1 ⟨H, geuc⟩dS = ω2n−1 2n Hiikk.
(3.39) Also, since r2 = (xi)2, we have rdr = xidxi (3.40) r2dr ⊗dr = xixjdxidxj. [...] J. Han and J. A. Via

## Retrieved source content

### Gluing Construction of Einstein Manifolds

By
Peyman Morteza

###### A dissertation submitted in partial fulfillment of the requirements for the degree of

# Doctor of Philosophy (Mathematics)

at the

UNIVERSITY OF WISCONSIN – MADISON

2018

Date of final oral examination: May 9, 2018

The dissertation is approved by the following members of the Final Oral Committee:

Jeff Viaclovsky (Advisor), Professor, Mathematics

Lu Wang (Co-Advisor), Assistant Professor, Mathematics

Sigurd Angenent, Professor, Mathematics

Andreas Seeger, Professor, Mathematics

* * *

## Abstract

A substantial part of the material presented in this thesis is based on the results in \[26\].
We develop a procedure to construct Einstein metrics by gluing the Calabi metric to an
Einstein orbifold. We show that our gluing problem is obstructed and we calculate the
obstruction explicitly. When our obstruction does not vanish, we obtain a non-existence
result in the case that the base orbifold is compact. When our obstruction vanishes and
the base orbifold is non-degenerate and asymptotically hyperbolic, we prove an existence
result. We also prove a non-existence result in the asymptotically hyperbolic Einstein
case, provided that the obstruction does not vanish.

* * *

## Acknowledgements

This dissertation was written under the supervision of Professor Jeff A. Viaclovsky. I
would like to thank him for guidance. I would also like to thank Professor Lu Wang who
was my Co-Advisor.

Finally, I would like to dedicate this dissertation to my parents Fakhry and Jalal,
my sister Afsaneh, and my brother Arian.

* * *

## List of Figures

1 The desingularization procedure....................... 3
2 Non-Examples . . . .. ............................ 7

* * *

List of Tables

* * *

## Contents

Abstract i
Acknowledgements ii
1 Introduction 1
1.1 Overview . . .. .. .............................. 1
1.1.1 Gluing procedure for solutions of geometric PDEs......... 1
1.1.2 Building blocks and Einstein gluing................. 2
1.2 Background.................... .. .. .. .. .. .. .. 4
1.3 Statement of results ................ .. .. .. .. .. .. .. 6
1.3.1 Outline................................ 10
2 Infinitesimal Einstein deformations of the Calabi metric 12
2.1 The Calabi metric . .............................. 12
2.2 Infinitesimal Einstein deformations. .................... 15
3 Linearized equation on the Calabi metric 21
3.1 Reformulation of the obstruction...................... 24
4 The refined approximate metric 30
5 Solution of the Einstein equation modulo obstructions 35
5.1 Function Spaces . . .............................. 35
5.2 Lyapunov-Schmidt reduction . ........................ 36

* * *

6 Analysis on asymptotically hyperbolic manifolds 43

7 From germs to boundary tensors
8 From boundary tensors to germs
9 Completion of proofs
10 Remarks on the four dimensional case

56
65
77
83

10.1 The tensors _k1, k2_ and _k3._ .. .. ...................... 84

$$
k\_{2}
$$

Bibliography

90

* * *

# Introduction

#### 1.1 Overview

A Riemannian metric _g_ is called Einstein if

$$
Ric(g)=\\Lambda g
$$

(1.1)

where Λ is a constant. Constructing Einstein metrics is an interesting and difficult
problem in differential geometry. Here is one indication for this fact (see \[7, §0.23\]):

” _Despite the simplicity of the condition Ric(g_) = _Λg the reader should not imagine that_
_examples are easy to find. If you are not convinced, try to find yourself which is not_
_in our book. And if you succeed, please write to us immediately. Ricci flat compact_
_manifolds are even harder to come by. The author will be happy to stand you a meal in_
_a starred restaurant in exchange of one of these!_ ”

The goal of this work is to develop a gluing procedure to construct Einstein metrics.
First, we explain the general gluing procedure for the solutions of the geometric PDEs.

##### 1.1.1 Gluing procedure for solutions of geometric PDEs

“Gluing” is a powerful technique to construct solutions of geometric PDEs. This technique has been applied to many areas of differential geometry. For example, there are constructions of minimal surfaces, self-dual metrics, extremal K¨ahler metrics using gluing techniques. Roughly speaking, one starts from solutions defined on two manifolds
_M0_ and _X,_ which have some coincidence along a common region _DZ_ (Damage Zone),
and one tries to construct approximate solutions on a manifold _M_ obtained from _M0_
and _X_ by surgery along _DZ._ The main steps are

$$
M\_{0}
$$

$$
M\_{0}
$$

• construction of a family gt, t > 0 of approximate solutions on M, which converge
when _t →_ 0 to the two given solutions on the disjoint sum _M0 q X,_ up to scaling.

$$
g\_{t},t>0
$$

$$
t\\to0
$$

$$
M\_{0}\\amalg X
$$

• for small enough t, deform the approximate solution gt to a true solution on M.

$$
g\_{t}
$$

The technical step is to prove a uniform estimate for the norm of a inverse of the
linearization of the problem. We apply the above technique in the context of Einstein
metrics. We need to introduce the building blocks for our gluing theorems.

##### 1.1.2 Building blocks and Einstein gluing

2kπi
Let Γn = {en: k = 0,...,n − 1} and consider the action of Γn on Cn by

$$
\\Gamma\_{n}=\\left{e^{\\frac{2k\\pi i}{n}}:k=0,...,n-1\\right}
$$

$$
\\Gamma\_{n}
$$

$$
\\mathbb{C}^n
$$

$$
e^{\\frac{2k\\pi i}{n}}\\cdot\\big(z^{1},...,z^{n}\\big)=\\big(e^{\\frac{2k\\pi i}{n}}z^{1},...,e^{\\frac{2k\\pi i}{n}}z^{n}\\big).
$$

(1.2)

The Calabi metric gcal is a Ricci-flat, K¨ahler, ALE metric on the total space X of the line
bundle O(−n) → Pn−1 which is U(n)-invariant. The group at infinity is Γn ⊂ SU(n).
For the second building block, let _(M0,g0)_ denote an Einstein orbifold of real dimension
_m_ = _2n_ satisfying

$$
g\_{cal}
$$

$$
\\mathcal{O}(-n)\\to\\mathbb{P}^{n-1}
$$

$$
\\mathrm{U}(n)
$$

$$
\\Gamma\_{n}\\subset\\mathrm{SU}(n)
$$

$$
(M\_{0},g\_{0})
$$

$$
m=2n
$$

$$
Ric(g\_0)=\\Lambda g\_0,
$$

(1.3)

and which has a singular point p0 with group Γn. We can desingularize the orbifold

$$
p\_{0}
$$

$$
\\Gamma\_{n}
$$

* * *

(M0,g0) (Xt,t · gcal)
p0
φt
t t
DZM0 DZX

# =⇒

Figure 1: The desingularization procedure.

metric by gluing on a Calabi metric in the following manner. Let _t_ \> 0 be small, and
consider the following regions

$$
X^{t}=\\left{x\\in X:r<2t^{-1/4}\\right}
$$

(1.4)

$$
M\_{0}^{t}=M\\setminus B(p\_{0},(1/2)t^{1/4})
$$

(1.5)

We define the damage zones in _M0_ and _X_

$$
M\_{0}
$$

$$
DZ\_{X}^{t}=\\left{x\\in X\\mid(1/2)t^{-1/4}<r<2t^{-1/4}\\right}
$$

(1.6)

$$
D Z\_{M\_{0}}^{t}={m\\in M\_{0}\\mid(1/2)t^{1/4}<\|z\|<2t^{1/4}}
$$

(1.7)

We identify these zones with a mapping

$$
\\phi\_{t}:DZ\_{X}^{t}\\rightarrow DZ\_{M\_{0}}^{t}
$$

(1.8)

_√_
by φt(x) = tx. Define Mt to be the union of Xt and M0t along the attaching map
t t
φt. The mapping φt identifies DZX with DZM0, so we can construct a new manifold
Mt with a new metric gt = g0#tgcal by gluing at each singular point the region M0t in
t t
M0 with the region tgcal in the Xt, identifying DZX and DZM0 by φt and interpolating
between the metrics g0 and tgcal on DZ. The process is illustrated in the Figure 1.

$$
\\phi\_{t}(x)=\\sqrt{t}x
$$

$$
M^{t}
$$

$$
X^{t}
$$

$$
M\_{0}^{t}
$$

$$
\\phi\_{t}
$$

$$
DZ\_{X}^{t}
$$

$$
\\phi\_{t}
$$

$$
DZ\_{M\_{0}}^{t}
$$

$$
M^{t}
$$

$$
g\_{t}=g\_{0}#t g\_{cal}
$$

$$
M\_{0}^{t}
$$

$$
tg\_{cal}
$$

$$
M\_{0}
$$

$$
X^{t}
$$

$$
DZ\_{X}^{t}
$$

$$
\\tilde{D}Z\_{M\_{0}}^{t}
$$

$$
\\phi\_{t}
$$

$$
g\_{0}
$$

$$
tg\_{cal}
$$

$$
DZ
$$

* * *

#### 1.2 Background

To state our results precisely, we recall some elementary facts and define some notions
precisely. We first state the following lemma,

Lemma 1. If A ∈ SO(2n) satisfies Aγ = γA for γ a generator of Γn, then A ∈ U(n),
_if n ≥ 3._

$$
A\\in SO(2n)
$$

$$
A\\gamma=\\gamma A
$$

$$
\\gamma
$$

$$
\\Gamma\_{n}
$$

$$
A\\in\\mathrm{U}(n)
$$

$$
\\mathit{if};n\\geq3
$$

A consequence of this lemma is that, given an Einstein orbifold _(M0,g0)_ with orbifold
group Γn(n ≥ 3) with one singular point p0, there is a well-defined almost complex
structure J at p0. The corresponding K¨ahler form at p0, will be denoted by ωp0. We can
now define

$$
\\left(M\_{0},g\_{0}\\right)
$$

$$
\\Gamma\_{n}(n\\geq3)
$$

$$
p\_{0}
$$

$$
p\_{0}
$$

$$
\\omega\_{p\_{0}}
$$

$$
p\_{0}
$$

$$
\\langle\\mathcal{R}(\\omega),\\omega\\rangle(p\_{0})=\\sum\_{i,j,k,l}R\_{i j k l}(p\_{0})(\\omega\_{p\_{0}}) _{i j}(\\omega_{p\_{0}})\_{k l},
$$

(1.9)

where _R(p0_) denote the scalar curvature at _p0._ Next, We define the approximate Einstein
metric gt = g0#tgcal in previous subsection precisely. Let χ be a smooth function
satisfying 0 _≤ χ ≤_ 1,
8

$$
R(p\_{0})
$$

$$
p\_{0}
$$

$$
g\_{t};=;g\_{0}#t g\_{cal}
$$

$$
\\chi
$$

$$
0\\leq\\chi\\leq1
$$

$$
\\begin{aligned}&\\chi(s)=\\left{\\begin{aligned}\ &1&&s\\leq1/2\\&&\\&0&&s\\geq2\ &\\end{aligned}\\right.,\ \\end{aligned}
$$

(1.10)

1
and define χt(s) ≡ χ(t4s). Then

$$
\\chi\_{t}(s)\\equiv\\chi(t^{\\frac{1}{4}}s)
$$

$$
\\begin{aligned}&g\_{t}=\\left{\\begin{aligned}\ &g\_{0}&&M\_{0}\\setminus B(p\_{0},2t^{1/4})\\&&\\&(1-\\chi\_{t}(r))\\phi\_{t}^{\*}g\_{0}+\\chi\_{t}(r)t\\cdot g\_{cal}&&(1/2)t^{-1/4}<r<2t^{-1/4}\\&&\\&t\\cdot g\_{cal}&&r<(1/2)t^{-1/4}\ &\\end{aligned}\\right.\ \\end{aligned}
$$

(1.11)

* * *

gives the precise form of the approximate Einstein metric on Mt. Next, we define a
weight function on Mt as follows.
8

$$
M^{t}
$$

$$
M^{t}
$$

$$
\\begin{aligned}&w=\\left{\\begin{aligned}\ &1&&z\\in M\_{0}\\setminus B(p\_{0},i\_{g\_{0}})\\&&\\&\|z\|&&\\frac{1}{2}t^{\\frac{1}{4}}<\|z\|<\\frac{1}{2}i\_{g\_{0}}\\&rt^{\\frac{1}{2}}&&2<r<2t^{-\\frac{1}{4}}\\&&&\\&t^{\\frac{1}{2}}&&r\\leq1\ &\\end{aligned}\\right.,\ \\end{aligned}
$$

(1.12)

where ig0is the injectivity radius of g0, and such that w is increasing in r for 1 < r < 2,
and increasing in \|z\| for 12ig0< \|z\| < ig0. We next consider a class of complete, noncompact Riemannian metrics.

$$
i\_{g\_0}
$$

$$
g\_{0}
$$

$$
1<r<2
$$

$$
\\left\|z\\right\|
$$

$$
\\frac{1}{2}i\_{g\_0}<\|z\|<i\_{g\_0}
$$

Definition 2. Let _M_ = _M ∪ ∂M_ be a smooth, compact manifold with boundary, and
let _g_ be a Riemannian metric on _M._ We say that _g_ is _conformally compact_ if there exists
∞
a function _x ∈ C_ ( _M,_ R) with _x_ \> 0 on _M_ such that

$$
\\overline{M}=M\\cup\\partial M
$$

$$
x\\in C^{\\infty}(\\overline{M},\\mathbb{R})
$$

$$
x>0
$$

$$
\\partial M={p\\in\\overline{M}:x(p)=0},
$$

(1.13)

and _g_ = _x2g_ extends to a Riemannian metric on _M_ of class _C2_ with _dx 6=_ 0 on _∂M._

$$
\\bar{g}=x^{2}g
$$

$$
\\overline{M}
$$

$$
C^{2}
$$

$$
\\neq0
$$

$$
\\partial M
$$

A function _x_ with the above properties is called a boundary defining function. Note
that _g\|_ ∂Mis not well-defined since there might be another candidate for a boundary
defining function _x_ but its conformal class \[ _g\|_ ∂M\] is well-defined and we call it the
conformal infinity of _g._

$$
\\bar{g}\|\_{\\partial M}
$$

$$
\\left\[\\bar{g}\|\_{\\partial M}\\right\]
$$

Definition 3. _Let (M,∂M,g,x) be a smooth, conformally compact manifold. We say_
that (M,∂M,g,x) is asymptotically hyperbolic (AH) if \|dx\|g = 1, where x is a boundary
_defining function as above. If moreover g is Einstein with Ric(g_) = _−(m − 1)g, then g_
_is called asymptotically hyperbolic Einstein (AHE)._

$$
\\left(M,\\partial M,g,x\\right)
$$

$$
(M,\\partial M,g,x)
$$

$$
(AH)if\|dx\|\_{\\bar{g}}=1
$$

$$
Ric(g)=-(m-1)g
$$

* * *

Note that the AH condition is independent of the defining function _x._ Furthermore,
if _m_ = dim(M) is even, the metric _¯g_ extends smoothly to _M_ \[13\]. For more background
on the theory of AHE metrics, we refer the reader to \[8, 14, 20, 23\]. We say that _g_
is non-degenerate if the space of _L2_ infinitesimal Einstein deformations is trivial (see
Definition 9)

$$
m=\\dim(M)
$$

$$
\\bar{g}
$$

$$
\\overline{M}
$$

$$
L^{2}
$$

#### 1.3 Statement of results

Our first result is in the case of a compact Einstein orbifold, which is an extension of
\[10, Theorem 1.2\].

Theorem 1.1. _Let (M0,g0) be a compact Einstein orbifold having a singular point p0_
with orbifold group Γn ⊂ SU(n) with n ≥ 3, and assume that

$$
\\left(M\_{0},g\_{0}\\right)
$$

$$
p\_{0}
$$

$$
\\Gamma\_{n}\\subset\\mathrm{SU}(n)
$$

$$
n\\geq3
$$

$$
n\\langle\\mathcal{R}(\\omega),\\omega\\rangle(p\_{0})+2(n-2)R(p\_{0})\\neq0.
$$

(1.14)

_Then there exist constants_ \> 0 _and δ0_ \> 0 _small, such that there does not exist any_
Einstein metric gE near gt satisfying

$$
\\epsilon>0
$$

$$
\\delta\_{0}>0
$$

$$
g\_{E}
$$

$$
g\_{t}
$$

$$
\|\\nabla^{\\ell}(g\_{t}-g\_{E})\| _{C^{0}(g_{t})}<\\epsilon w^{-\\delta\_{0}-\\ell},
$$

(1.15)

_for_ 0 _≤‘≤ 3, and sufficiently small gluing parameter t._

$$
0\\leq\\ell\\leq3
$$

This theorem does give some new understanding of possible degenerations of Einstein
metrics, but we do not obtain an existence result in the compact case because this gluing
problem is _obstructed._ Theorem 1.1 implies several non-existence results. The first two
“non-examples” are the following.

* * *

p0
(S2n/Γn,g)

p0
(D2n/Γn,gH)

Figure 2: Non-Examples

Non-example 4. Let _(M,g)_ be a compact K¨ahler-Einstein orbifold with Einstein constant Λ 6= 0, and singular point p0 of type Γn and n ≥ 3. In the K¨ahler-Einstein case,
_〈Rω,ω〉_ = _2R_ (see \[7, page 77\]), so the obstruction in (1.14) is equal to 4(n _−_ 1)R(p0).
Consequently, if Λ 6= 0, then there does not exist any Einstein metric near the approximate metric gt, for t sufficiently small. We note that it follows from the adjunction
formula that there is no K¨ahler-Einstein metric near gt for t sufficiently small, so the
main point is that these examples cannot be desingularized by a non-K¨ahler Einstein
metric either.

$$
(M,g)
$$

$$
\\Lambda\\ne0
$$

$$
p\_{0}
$$

$$
\\Gamma\_{n}
$$

$$
n\\geq3
$$

$$
\\langle\\mathcal{R}\\omega,\\omega\\rangle=2R
$$

$$
4(n-1)R(p\_0)
$$

$$
\\Lambda\\ne0
$$

$$
g\_{t},
$$

$$
g\_{t}
$$

Non-example 5. The football metric gS on S2n/Γ is defined as the quotient of the
round metric on S2n by Γ, where Γ acts in the above manner on the first 2n-coordinates
of R2n+1. Since gS has constant curvature equal to 1, the obstruction (1.14) does not
vanish at either of the singular points. Consequently, there does not exist any Einstein
metric near the approximate metric gt, for t sufficiently small.

$$
g\_{S}
$$

$$
S^{2n}/\\Gamma
$$

$$
S^{2n}
$$

$$
\\mathbb{R}^{2n+1}
$$

$$
g\_{S}
$$

$$
g\_{t},
$$

We are able to prove existence theorem when _(M0,g0)_ is asymptotically hyperbolic
Einstein and non-degenerate.

$$
\\left(M\_{0},g\_{0}\\right)
$$

Theorem 1.2. _Let (M0,g0) be an asymptotically hyberbolic Einstein orbifold having a_
singular point p0 with orbifold group Γn ⊂ SU(n), with conformal infinity \[g∞\] and n ≥ 3.

$$
\\left(M\_{0},g\_{0}\\right)
$$

$$
p\_{0}
$$

$$
\\left\[g\_{\\infty}\\right\]
$$

$$
\\Gamma\_{n}\\subset\\mathrm{SU}(n)
$$

$$
n\\geq3
$$

* * *

_If g0 is non-degenerate and_

$$
g\_{0}
$$

$$
n\\langle\\mathcal{R}(\\omega),\\omega\\rangle(p\_{0})+2(n-2)R(p\_{0})=0,
$$

(1.16)

then there exists an AHE metric ĝt on Mt for all t sufficiently small. The conformal
_infinity_ \[ˆg∞,t\] _of the Einstein metric is a small perturbation of_ \[ _g_ ∞ _\], in the sense that_

$$
\\hat{g}\_{t}
$$

$$
M^{t}
$$

$$
\\left\[\\hat{g}\_{\\infty,t}\\right\]
$$

$$
\\left\[g\_{\\infty}\\right\]
$$

$$
\|\\hat{g} _{\\infty,t}-g_{\\infty}\|\_{C^{2}(\\partial M)}<C t.
$$

(1.17)

_for some constant C._

$$
C.
$$

The Einstein metric ˆgt is close, in a weighted norm, to a certain perturbation of gt
which changes the conformal infinity. For the precise statement, see Chapter 9. The
only “explicit” example of this phenomenon that we know of is the following.

$$
\\hat{g}\_{t}
$$

$$
g\_{t}
$$

Example 6. In \[27\], Page and Pope wrote down an explicit 1-parameter family of
U(n)-invariant Einstein metrics O(−n) → Pn−1, see also \[6\]. In \[24\], it was pointed out
by Mazzeo and Singer that at one end of the parameter space, the Page-Pope family
degenerates to an Einstein orbifold, with a Ricci-flat ALE metric bubbling off (which is
in fact the Calabi metric). It can be shown that the limiting orbifold is the quotient of a
Page-Pope metric on D2n, which also comes in a 1-dimensional family, and the parameter
is exactly that for which the obstruction (1.16) is satisfied. Of course, Theorem 1.2 could
be used to produce the Page-Pope metrics on _O(−n),_ but since these metrics are already
known explicitly, it is not necessary to analyze this example in more detail here.

$$
\\mathrm{U}(n)
$$

$$
\\mathcal{O}(-n)\\rightarrow\\mathbb{P}^{n-1}
$$

$$
\\mathbb{D}^{2n}
$$

$$
\\mathcal{O}(-n)
$$

We note that the boundary conformal class in the previous example is that of a
Berger sphere. The boundary Berger sphere conformal classes in the Page-Pope family
on _O(−n_) are those with smaller length of the Hopf fiber than the one for which the

$$
\\mathcal{O}(-n)
$$ obstruction vanishes. The ones with longer fiber length probably do not have any AHE
filling, but the proof of this would require a more detailed analysis than given here (in
particular, it would require a computation of the second obstruction).

There is also a corresponding non-existence result in the AHE case, provided that the
obstruction in (1.16) does not vanish. But to state this properly, we need the following.
Use the boundary defining function _x_ to identify a neighborhood of the boundary, call
it _U2_ with (0,2 ) _× ∂M0,_ and if necessary, we modify the defining function _x_ to a new
defining function _˜x_ satisfying
8

$$
U\_{2\\epsilon}\\mathrm{with}(0,2\\epsilon)\\times\\partial M\_{0}
$$

$$
\\tilde{x}
$$

$$
\\begin{aligned}&\\tilde{x}(z)=\\left{\\begin{aligned}\ &x&&z\\in U\_{2\\epsilon}\\&2\\epsilon\\leq\\tilde{x}\\leq1&&z\\in M\_0\\setminus{U\_{2\\epsilon}}.\ &\\end{aligned}\\right.\ \\end{aligned}
$$

(1.18)

Given a boundary metric _˜g_ ∞close to _g_ ∞, using the identification above we extend _˜g_ ∞
to an asymptotically hyperbolic metric on _M0_ by

$$
\\tilde{g}\_{\\infty}
$$

$$
g\_{\\infty}
$$

$$
\\tilde{g}\_{\\infty}
$$

$$
M\_{0}
$$

$$
\\tilde{g}=g+\\chi\\big(x\\epsilon^{-1}\\big)\\big(\\tilde{g} _{\\infty}-g_{\\infty}\\big).
$$

(1.19)

Our non-existence result in the AHE case is the following.

Theorem 1.3. _Let (M0,g0) be an asymptotically hyberbolic Einstein orbifold having a_
singular point p0 with orbifold group Γn ⊂ SU(n), with conformal infinity \[g∞\] and n ≥ 3.
_Assume that_

$$
\\left(M\_{0},g\_{0}\\right)
$$

$$
p\_{0}
$$

$$
\\Gamma\_{n}\\subset\\mathrm{SU}(n)
$$

$$
\\left\[g\_{\\infty}\\right\]
$$

$$
n\\geq3
$$

$$
n\\langle\\mathcal{R}(\\omega),\\omega\\rangle(p\_{0})+2(n-2)R(p\_{0})\\neq0.
$$

(1.20)

_Fix δ0_ \> 0 _and δ_ ∞\> 0 _small. Then given_ \> _0, there exists a constant δ_ \> 0 _such that_
_if_

$$
\\delta\_{0}>0
$$

$$
\\delta\_{\\infty}>0
$$

$$
\\epsilon>0
$$

$$
\\delta>0
$$

$$
\|\\bar{\\tilde{g}} _{\\infty}-g_{\\infty}\|\_{C^2(\\partial M)}<\\bar{\\delta},
$$

(1.21)

* * *

then there is no AHE metric gE near g˜t satisfying

$$
g\_{E}
$$

$$
\\tilde{g}\_{t}
$$

$$
\|\\nabla^{\\ell}\\big(\\tilde{x}^{-\\delta\_{\\infty}}\\big(\\tilde{g} _{t}-g_{E}\\big)\\big)\| _{C^{0}(g_{t})}<\\epsilon w^{-\\delta\_{0}-\\ell}
$$

(1.22)

_for_ 0 _≤‘≤ 3, and sufficiently small gluing parameter t._

$$
0\\leq\\ell\\leq3
$$

Using this result, we have the following “non-example”.

Non-example 7. Let (D2n,gH) denote the hyperbolic space of real dimension 2n. This
is an AHE metric, with conformal infinity the round sphere S2n−1. The group Γn acts
on D2n, and the hyperbolic metric descends to the quotient. Since gH has constant
curvature equal to −1, the obstruction (1.20) does not vanish at the singular point.
Therefore, there exists no AHE metric near the approximate metric ˜gt, with boundary
conformal class near the round metric.

$$
\\left(\\mathbb{D}^{2n},g\_H\\right)
$$

$$
2n
$$

$$
S^{2n-1}
$$

$$
\\Gamma\_{n}
$$

$$
\\mathbb{D}^{2n}
$$

$$
g\_{H}
$$

$$
-1
$$

$$
\\tilde{g}\_{t}
$$

##### 1.3.1 Outline

We end this chapter with a brief outline of this thesis. In Chapter 2, we will recall
some basic details about the Calabi metric, then we will show that the space of decaying
infinitesimal Einstein deformations is one-dimensional. In Chapter 3, we will identify
the obstruction for finding a solution of the gauged linearized Einstein equation with
prescribed quadratic leading term, and also give a useful reformulation of the obstruction.
In Chapter 4, we will define the “refined” approximate metric which is an improvement
of the “näıve” approximate metric which was defined above. Then in Chapter 5 we will
present the main Lyapunov-Schmidt reduction which yields a solution of the Einstein
equation modulo the space of obstructions, which we will use to prove Theorem 1.1.

The remainder of the thesis will then focus on the asymptotically hyperbolic Einstein
case. In Chapter 6, we will give some background on the theory of AHE Einstein metrics, and in particular compute the indicial roots at infinity for several important operators.
In Chapter 7, we will define a mapping from germs to boundary tensors, which considers
solutions which blow-up at _p0_ at a certain rate with prescribed leading term. This will
be used in Chapter 8, together with a duality argument, to prove that there is a solution
of the linearized equation with a certain prescribed quadratic leading term at _p0,_ and
which is bounded at infinity (in the interior metric). This solution will then be used
in Chapter 9 to prove the main existence theorem, Theorem 1.2. In Chapter 9, the
non-existence result Theorem 1.3 will be proved. Finally, in Chapter 10 we give some
remarks on Biquard’s work in \[10\] for the four dimensional case.

$$
p\_{0}
$$

$$
p\_{0}
$$

* * *

# Infinitesimal Einstein deformations of the Calabi metric

We begin with a brief description of the Calabi metric.

#### 2.1 The Calabi metric

The cone Cn/Γn admits a crepant resolution X which is the total space of the bundle
O(−n) → Pn−1. In \[12\], Calabi proved the following.

$$
\\mathbb{C}^n/\\Gamma\_n
$$

$$
\\mathcal{O}(-n)\\rightarrow\\mathbb{P}^{n-1}
$$

Theorem 8. _The space X admits a_ U(n)- _invariant Ricci-flat K¨ahler ALE metric de-_
noted by gcal.

$$
g\_{cal}
$$

_Proof._ This metric is well-known, so we only present some details in the proof that we
need, following the presentation of \[19\]. Let

$$
u=z^{1}\\bar{z}^{1}+\\ldots+z^{n}\\bar{z}^{n},
$$

and

$$
F:\\mathbb{C}^n\\longrightarrow\\mathbb{R},
$$

be a radial K¨ahler potential to be determined later. The corresponding K¨ahler metric is

$$
g\_{i\\bar{j}}=\\partial\_{i}\\partial\_{\\bar{j}}F=\\partial\_{i}\\big(z^{\\bar{j}}F^{\\prime}(u)\\big)=\\delta\_{i j}F^{\\prime}(u)+z^{\\bar{j}}\\bar{z}^{i}F^{\\prime\\prime}(u).
$$

(2.1)

* * *

For a K¨ahler metric, the components of the Ricci tensor are given by

$$
R\_{i\\bar{j}}=-\\partial\_{i}\\partial\_{\\bar{j}}\\log\\det\\left(g\_{\\alpha\\bar{\\beta}}\\right).
$$

(2.2)

A computation shows that a solution of Rij

= 0 is given by

$$
R\_{i\\bar{j}}=0
$$

$$
\\det\\left(g\_{\\alpha\\overline{{\\beta}}}\\right)=(F^{\\prime})^{n-1}(F^{\\prime}+u F^{\\prime\\prime})=1.
$$

(2.3)

By solving (2.3) we obtain

(2.4)

$$
F(u)=\\int\_{1}^{u}(a^n+x^n)^{\\frac{1}{n}}dx,
$$

$$
F^{\\prime}(u)=\\frac{(a^{n}+u^{n})^{\\frac{1}{n}}}{u},
$$

(2.5)

$$
F^{\\prime\\prime}(u)=\\frac{u^{n-1}(a^{n}+u^{n})^{\\frac{1-n}{n}}}{u}-\\frac{(a^{n}+u^{n})^{\\frac{1}{n}}}{u^{2}}.
$$

(2.6)

We will fix the constant of integration _a_ = 1\. The metric then becomes

$$
g\_{i\\bar{j}}=\\frac{(1+u^{n})^{\\frac{1}{n}}}{u}\\Big{\\delta\_{i j}-\\frac{1}{u(1+u^{n})}z^{j}\\bar{z}^{i}\\Big}.
$$

(2.7)

We next write the metric in radial form. Consider the following 1-forms

$$
dr,J\\big(dr\\big),
$$

(2.8)

where _dr_ is the radial form and _J_ is the standard complex structure. We denote the
dual vectors (with respect to the Euclidean metric) by

$$
d r
$$

$$
\\partial\_{r},J(\\partial\_{r}).
$$

(2.9)

Let θ = −J(dr) and ∂θ denote the dual of θ (with respect to the Euclidean metric). It
r
follows that

$$
\\theta=-J\\left(\\frac{dr}{r}\\right)
$$

$$
\\partial\_{\\theta}
$$

$$
\\theta
$$

$$
J(r\\partial\_r)=\\partial\_\\theta.
$$

(2.10)

* * *

Since the Calabi metric is U(n)-invariant, we only need to compute the metric at the
point ( _r,0,0...,0)._ On this axis, we have

$$
\\mathrm{U}(n)
$$

$$
\\partial\_{r}=\\bar{\\partial} _{1}+\\bar{\\partial}_{1},
$$

(2.11)

$$
g(\\partial\_{r},\\partial\_{r})=g(\\partial\_{1}+\\bar{\\partial} _{1},\\partial_{1}+\\bar{\\partial} _{1})=2g_{1\\bar{1}}=2u^{n-1}(1+u^{n})^{\\frac{1-n}{n}},
$$

and

(2.12)

and also

$$
g\\left(\\partial\_{\\theta},\\partial\_{\\theta}\\right)=g\\left(J\\left(r\\partial\_{r}\\right),J\\left(r\\partial\_{r}\\right)\\right)=g\\left(r\\partial\_{r},r\\partial\_{r}\\right)=2u^{n}\\left(1+u^{n}\\right)^{\\frac{1-n}{n}}.
$$

(2.13)

Also at _(r,0,0...,0)_ and for 2 _≤ i ≤ 2n −_ 2 it follows that

$$
2\\leq i\\leq2n-2
$$

$$
g\\left(\\partial\_{i}+\\bar{\\partial} _{i},\\partial_{i}+\\bar{\\partial}\_{i}\\right)=2\\left(1+u^{n}\\right)^{\\frac{1}{n}}
$$

(2.14)

Finally we obtain the metric in radial coordinates1

$$
2g\_{c a l}\\equiv g=2u^{n-1}(1+u^{n})^{\\frac{1-n}{n}}d r^{2}+2(1+u^{n})^{\\frac{1}{n}}g\_{F S}+2u^{n}(1+u^{n})^{\\frac{1-n}{n}}\\theta^{2},
$$

(2.15)

where u = r2, and gFS denotes the Fubini-Study metric on Pn−1. There is an apparent
singularity at u = 0, which can be resolved by replacing the origin with the Pn−1 as
the zero section of O(−n) −→ Pn−1, and the metric then extends smoothly to the
resolution.

$$
u=r^{2}
$$

$$
g\_{FS}
$$

$$
\\mathbb{P}^{n-1}
$$

$$
u=0
$$

$$
\\mathbb{P}^{n-1}
$$

$$
\\mathcal{O}(-n)\\longrightarrow\\mathbb{P}^{n-1}
$$

We will next set some notation which will be used below. Let _ω_ denote the Fubini-
Study 2-form on Pn−1. Recall that on Pn−1 we have

$$
\\omega
$$

$$
\\mathbb{P}^{n-1}
$$

$$
\\mathbb{P}^{n-1}
$$

$$
d\\theta=2\\omega,;d\\omega=\\bar{0},
$$

(2.16)

1There is a typo in \[19\] for gcal in radial form.

$$
g\_{cal}
$$ where θ is viewed as a connection form for the Hopf fibration S2n−1 → Pn−1. Next, we
define

$$
\\theta
$$

$$
S^{2n-1}\\rightarrow\\mathbb{P}^{n-1}
$$

$$
A(r)=\\frac{r^{n-1}}{(1+r^{2n})^{\\frac{n-1}{2n}}},B(r)=(1+r^{2n})^{\\frac{1}{n}},C(r)=(1+r^{2n})^{\\frac{1-n}{2n}}r^n,
$$

(2.17)

so that

$$
\\left\|A d r\\right\| _{g_{c a l}}=\\left\|C\\theta\\right\| _{g_{c a l}}=1,\\left\|B\\omega\\right\| _{g_{c a l}}^2=n-1.
$$

(2.18)

We also define

$$
d\\bar{r}\\equiv A d r,\\bar{\\theta}\\equiv C\\theta,\\bar{\\omega}\\equiv B\\omega,\\overline{{g\_{F S}}}\\equiv B g\_{F S},
$$

(2.19)

so that the Calabi metric may be written as

$$
g\_{c a l}=d\\bar{r}\\otimes d\\bar{r}+\\overline{{g\_{F S}}}+\\bar{\\theta}\\otimes\\bar{\\theta}.
$$

(2.20)

#### 2.2 Infinitesimal Einstein deformations

In this section we prove that the space of decaying infinitesimal Einstein deformations
of (X,gcal) is one-dimensional and we explicitly identify a generator. We first define the
operators that we need. Let (Mm,g) be a Riemannian manifold of real dimension m.
For a 1-form _ω,_

$$
\\left(X,g\_{\\mathit{cal}}\\right)
$$

$$
\\left(M^{m},g\\right)
$$

$$
\\begin{aligned}&\\delta\_{g}:\\Omega^{1}(M)\\to\\Omega^{0}(M)&\\delta\_{g}(\\omega)=-g^{ij}\\nabla\_{i}\\omega\_{j}\\&\\delta\_{g}^{ _}:\\Omega^{1}(M)\\to S^{2}(T^{_}M)&\\delta\_{g}^{ _}(\\omega){ij}=\\tfrac{1}{2}(\\nabla{i}\\omega\_{j}+\\nabla\_{j}\\omega\_{i})\\&\\mathcal{K}{g}:\\Omega^{1}(M)\\to S{0}^{2}(T^{_}M)&\\mathcal{K} _{g}(\\omega)=\\delta_{g}^{\*}\\omega+\\tfrac{1}{m}\\delta\_{g}(\\omega)g.\ \\end{aligned}
$$

For a symmetric 2-tensor _h,_

* * *

$$
\\begin{aligned}&\\delta\_{g}:S^{2}(T^{ _}M)\\rightarrow\\Omega^{1}(M)&&\\left(\\delta\_{g}(h)\\right){i}=-g^{jk}\\nabla{j}h\_{ki}\\&B\_{g}:S^{2}(T^{_}M)\\rightarrow\\Omega^{1}(M)&&B\_{g}(h)=\\delta\_{g}(h)+\\tfrac{1}{2}d(tr\_{g}h)\\&P\_{g}:S^{2}(T^{ _}M)\\rightarrow S^{2}(T^{_}M)&&P\_{g}(h)=\\tfrac{1}{2}\\nabla^{\*}\\nabla h-\\overset{\\circ}{R}(h),\ \\end{aligned}
$$

◦
where ∇∗ is the formal L2-adjoint of ∇, and R
symmetric two tensors defined by

is the action of curvature tensor on

$$
\\nabla^{\*}
$$

$$
L^{2}-adjoint
$$

$$
\\nabla,
$$

$$
\\overset{\\circ}{R}
$$

$$
\\stackrel{\\circ}{R}(h) _{i j}=g^{k p}g^{l q}R_{i k j l}h\_{p q}.
$$

(2.21)

We note that the operator ∇∗∇ = −∆, is the negative rough Laplacian of h. For
simplicity of notation we will often omit the metric _g_ when it is clear from context. We
also recall the following definition from \[7\].

$$
\\nabla^{\*}\\nabla;=;-\\Delta
$$

Definition 9. An _infinitesimal Einstein deformation_ of an Einstein metric _g_ is a symmetric 2-tensor field _h_ such that

$$
\\delta\_{g}h=0,P\_{g}(h)=0,t r\_{g}(h)=0.
$$

(2.22)

We say that a tensor h is decaying if h = O(r−) as r →∞ for some > 0.

$$
h=O(r^{-\\epsilon})
$$

$$
r\\to\\infty
$$

$$
\\epsilon>0
$$

Theorem 2.1. _The space of decaying infinitesimal Einstein deformations of the Calabi_
_metric is one-dimensional, and is spanned by the element_

$$
o=\\frac{1}{1+r^{2n}}\\Big(-\\overline{{g\_{F S}}}+(n-1)d\\bar{r}\\otimes d\\bar{r}+(n-1)\\bar{\\theta}\\otimes\\bar{\\theta}\\Big).
$$

(2.23)

To prove this, we will first characterize the decaying harmonic (1,1)-forms on the
Calabi metric, which will then be used to characterize the decaying infinitesimal Einstein
deformations. Recall that _n_ denotes the complex dimension, while _m_ = _2n_ denotes the
real dimension.

* * *

Proposition 2.2. On (X,gcal), the space of decaying harmonic (1,1)-forms is one-
_dimensional and is spanned by the element_

$$
(X,g\_{cal})
$$

$$
(1,1)-form s
$$

$$
\\Omega=\\frac{1-n}{1+r^{2n}}d\\bar{r}\\wedge\\bar{\\theta}+\\frac{1}{1+r^{2n}}\\bar{\\omega}.
$$

(2.24)

_Proof._ Define

$$
\\mathcal{H}^{p,q}={\\eta\\in C^{\\infty}(\\Lambda^{p,q}X)\\mid\\eta=O(r^{1-2n}),d\\eta=0,\\delta\\eta=0},
$$

(2.25)

and let Hp,q(X) denote the image of Hp,q(X) in Hp+q(X, C) under the natural mapping
_η 7→_ \[η\]. By \[17, Theorem 8.4.2\], the decomposition

$$
\\mathcal{H}^{p,q}(X)
$$

$$
H^{p,q}(X)
$$

$$
H^{p+q}(X,\\mathbb{C})
$$

$$
\\eta\\mapsto\[\\eta\]
$$

$$
H^{2}(X,\\mathbb{C})=H^{2,0}\\oplus H^{1,1}\\oplus H^{0,2}
$$

holds, which implies that

(2.26)

$$
\\dim(H^{1,1})=1.
$$

(2.27)

∞
By a standard argument (see for example \[16, Section 3\]), if η ∈ C (Λp,qX) satisfies
η = O(r−) for some > 0, then η = O(r−2n+1) as r →∞.

$$
\\eta\\in C^{\\infty}(\\Lambda^{p,q}X)
$$

$$
\\eta=O(r^{-\\epsilon})
$$

$$
\\epsilon>0
$$

$$
\\eta=O\\big(r^{-2n+1}\\big)
$$

$$
r\\to\\infty
$$

The remainder of the proof is therefore to show that the form in (2.24) is both closed
and co-closed, since it is obviously a (1,1)-form. Using (2.16) it is easy to see that Ω is
closed. To prove co-closedness, we recall that for a K¨ahler manifold (Mn,g0,J0,ω0) (n
is complex dimension) we have the following ( see \[25\])

$$
\\big(M^{n},g\_{0},J\_{0},\\omega\_{0}\\big)\\big(i
$$

$$
d V\_{g\_{0}}=\\frac{\\omega\_{0}^{n}}{n!}.
$$

(2.28)

Using (2.28) it follows that

$$
\\begin{aligned}&\*\\omega=\\frac{1}{(n-2)!}B^{n-3}\\omega^{n-2}\\wedge d\\bar{r}\\wedge\\bar{\\theta},\\&dV\_{g}=\\frac{B^{n-1}\\omega^{n-1}}{(n-1)!}\\wedge d\\bar{r}\\wedge\\bar{\\theta}.\ \\end{aligned}
$$

(2.29)

* * *

Now straightforward calculation using (2.16) and (2.29) shows that

$$
\\delta\\Omega=- _d_\\Omega=0.
$$

(2.30)

Finally, it is easy to check that this form extends across the zero section to define a
smooth form on _X._

Next, we complete the proof of Theorem 2.1. If _h_ is an infinitesimal Einstein deformation, then write

$$
h=h\_{+}+h\_{-},
$$

(2.31)

where h+ is the J-invariant part, and h− is the J-anti-invariant part. It is proved in \[7\]
that

$$
h\_{+}
$$

$$
h\_{-}
$$

$$
\\Delta\\Omega=0,
$$

(2.32)

$$
\\Delta I=0,
$$

(2.33)

where Ω is the (1,1)-form associated to h+, and I is the section of Λ0,1 ⊗ T 1,0 associated
to h−. Since the canonical bundle is trivial, the conjugate Hodge star operator applied
to I is a harmonic (1,n − 1)-form. By \[17, Theorem 8.4.2\], this implies that h− ≡ 0.

$$
h\_{+}
$$

$$
\\Lambda^{0,1}\\otimes T^{1,0}
$$

$$
h\_{-}
$$

$$
h\_{-}\\equiv0
$$

By Proposition 2.2, the space of decaying infinitesimal Einstein deformations is
spanned by

$$
o(.,.)=\\Omega(I(.),.).
$$

(2.34)

Observe that _o_ is a symmetric tensor

$$
o(Y\_{1},Y\_{2})=\\Omega(I(Y\_{1}),Y\_{2})=\\Omega(-Y\_{1},I(Y\_{2}))=\\Omega(I(Y\_{2}),Y\_{1})=o(Y\_{2},Y\_{1}).
$$

(2.35)

* * *

Noting that I(∂r) = ∂θ, where ∂θ, ∂r are the duals of θ,dr with respect to the Calabi
metric, we obtain

$$
I(\\overline{\\partial\_{r}})=\\overline{\\partial\_{\\theta}}
$$

$$
\\overline{\\partial\_{\\theta}},\\overline{\\partial\_{r}}
$$

$$
\\bar{\\theta},d\\bar{r}
$$

$$
o(\\overline{\\partial\_{\\theta}},\\overline{\\partial\_{\\theta}})=\\Omega(I(\\overline{\\partial\_{\\theta}}),\\overline{\\partial\_{\\theta}})=\\frac{n-1}{1+r^{2n}}
$$

(2.36)

$$
o(\\overline{{\\partial\_{r}}},\\overline{{\\partial\_{r}}})=\\Omega(I(\\overline{{\\partial\_{r}}}),\\overline{{\\partial\_{r}}})=\\frac{n-1}{1+r^{2n}}.
$$

(2.37)

Also recall that _ω_ is the Fubini-Study form, and that _I_ agrees with standard complex
structure on Pn−1, so

$$
\\omega
$$

$$
\\mathbb{P}^{n-1}
$$

$$
\\omega\\big(.,.\\big)=g\_{F S}\\big(I\\big(.\\big),.\\big)\\implies\\omega\\big(I\\big(.\\big),.\\big)=-g\_{F S}\\big(.,.\\big)\\implies\\bar{\\omega}\\big(I\\big(.\\big),.\\big)=-\\overline{{g\_{F S}}}\\big(.,.\\big)
$$

(2.38)

(for ω we have 〈ω, ω〉cal = n − 1) and o becomes

$$
\\bar{\\omega}
$$

$$
\\langle\\bar{\\omega},\\bar{\\omega}\\rangle\_{\\mathrm{cal}}=n-1)
$$

$$
o=\\frac{1}{1+r^{2n}}\\Big(-\\bar{g}\_{F S}+(n-1)d\\bar{r}\\otimes d\\bar{r}+(n-1)\\bar{\\theta}\\otimes\\bar{\\theta}\\Big),
$$

(2.39)

and clearly

$$
tr(o)=\\frac{1}{1+r^{2n}}(-2(n-1)+2(n-1))=0.
$$

(2.40)

Now observe that we can rewrite _o_ as:

$$
\\begin{aligned}&o=\\frac{1}{1+r^{2n}}\\Big(-\\overline{g\_{FS}}-d\\bar{r}\\otimes d\\bar{r}+n(d\\bar{r}\\otimes d\\bar{r})-\\bar{\\theta}\\otimes\\bar{\\theta}+n(\\bar{\\theta}\\otimes\\bar{\\theta})\\Big)\\&=\\frac{1}{1+r^{2n}}\\Big(-g\_{cal}+n(d\\bar{r}\\otimes d\\bar{r})+n(\\bar{\\theta}\\otimes\\bar{\\theta})\\Big).\ \\end{aligned}
$$

(2.41)

Also since Ω is divergence-free (Ω is co-closed) and _I_ is parallel, it follows that _o_ is
divergence-free, so _o_ is both traceless and divergence-free, as required. This completes
the proof of Theorem 2.1.

We end this section with a slightly modified statement of Theorem 2.1.

* * *

Theorem 2.3. On (X,gcal), the space of decaying solutions of

$$
(X,g\_{cal})
$$

$$
P\_{g}h=0
$$

(2.42)

$$
tr\_{g}h=0,
$$

(2.43)

_is one-dimensional, and is spanned by the element o._

Proof. The only thing we need to prove is that a solution of Pcalh = 0 which is decaying
must also be divergence-free. To see this, since Calabi metric is Ricci-flat we get the
following for linearized operator

$$
P\_{cal}h=0
$$

$$
d\_{\\mathrm{cal}}R i c(h)=\\frac{1}{2}\\nabla\_{\\mathrm{cal}}^{ _}\\nabla\_{\\mathrm{cal}}(h)-\\overset{\\circ}{R}(h)-\\delta\_{\\mathrm{cal}}^{_}B\_{\\mathrm{cal}}(h).
$$

(2.44)

Applying the divergence operator to the equation Pcalh = 0 yields the equation

$$
P\_{1}\\delta\_{g}h=0,
$$

$$
P\_{cal}h=0
$$

(2.45)

where P1 ≡ Bδ∗. Since gcal is Ricci-flat, this implies that

$$
P\_{1}\\equiv B\\delta^{\*}
$$

$$
g\_{cal}
$$

$$
\\Delta\_{H}(\\delta\_{g}h)=0,
$$

(2.46)

where ∆H is the Hodge Laplacian. By \[17, Theorem 8.4.1\], there are no decaying
harmonic 1-forms on X, which implies that δgh = 0.

$$
\\Delta\_{H}
$$

$$
\\delta\_{g}h=0
$$

* * *

# Linearized equation on the Calabi metric

In this chapter we apply a technique in \[10\] to find the obstruction for solving linearized
equation with prescribed leading quadratic term. Let

$$
H=H\_{ijkl}x^{i}x^{j}dx^{k}\\otimes dx^{l}
$$

(3.1)

be a given quadratic tensor defined on R2n which is symmetric in the first two and last
two indices. An easy computation shows that

$$
\\mathbb{R}^{2n}
$$

$$
B\_{e u c}(H)=(-2H\_{k j k l}+H\_{j l k k})x^{j}d x^{l}.
$$

(3.2)

We also need the following basic lemma.

Lemma 10. _Let v be a symmetric_ 2- _tensor with ‖v‖_
Then there exists u with ‖u‖g = O(r2+δ) and Pgcal
cal

g = O(rδ) for some δ ∈ (2−2n,0).
_cal_
(u) = _v if and only if_

$$
\|v\| _{g_{cal}}=O(r^{\\delta})
$$

$$
\\delta\\in(2-2n,0)
$$

$$
\|u\| _{g_{cal}}=O(r^{2+\\delta})
$$

$$
P\_{g\_{cal}}(u)=v
$$

$$
\\langle v,o\\rangle\_{L^{2}(g\_{c a l})}=0.
$$

(3.3)

_Proof._ This follows from standard theory of elliptic operators on weighted spaces (see
\[5\] for example).

Next, we have the following proposition.

* * *

Proposition 3.1. Given (H, Λ) with H a Γn-invariant symmetric 2-tensor on R2n sat-
_isfying_

$$
(H,\\Lambda)
$$

$$
\\Gamma\_{n}
$$

$$
\\mathbb{R}^{2n}
$$

$$
-\\frac{1}{2}\\Delta\_{euc}H=\\Lambda g\_{euc}
$$

(3.4)

$$
B\_{\\underline{{e u c}}}H=0,
$$

(3.5)

_there exists a solution (h,λ) to_

$$
\\left(h,\\lambda\\right)
$$

$$
\\begin{aligned}P\_{g\_{cal}}(h)&=\\Lambda g\_{cal}+\\lambda o\\h&=H+O(r^{-2n+2+\\epsilon})\\B\_{g\_{cal}}(h)&=0,\\end{aligned}
$$

(3.6)

_if and only if_

$$
\\lambda=-\\frac{1}{\|o\| _{L^2}^2}\\lim_{r\\to\\infty}\\int\_{S\_r/\\Gamma\_n}\\frac{n+1}{r}\\langle H,o\\rangle dS\_{S\_r/\\Gamma\_n}.
$$

(3.7)

_Proof._ Let _(h,λ)_ be a solution to (3.6). Let _R_ be a fixed positive real number and
consider the following cut-off function
8

$$
\\left(h,\\lambda\\right)
$$

$$
\\chi(x)=\\begin{cases}\ 1&\\quad\|x\|>2R\ \ 0&\\quad\|x\|<R\\end{cases}\ .
$$

(3.8)

Let h′ = h − χH, then h′ = O(r−2n+2+). We have

$$
h'=h-\\chi H
$$

$$
h^{\\prime}=O\\left(r^{-2n+2+\\epsilon}\\right)
$$

$$
P\_{g\_{c a l}}(h^{\\prime})=-P\_{g\_{c a l}}(\\chi H)+\\Lambda g\_{c a l}+\\lambda o.
$$

(3.9)

Next, we claim that Λgcal − Pgcal(χH) = O(r

−2n). To see this,

$$
\\Lambda g\_{cal}-P\_{g\_{cal}}(\\chi H)=O(r^{-2n})
$$

$$
P\_{g\_{c a l}}(\\chi H)=-\\frac{1}{2}\\Delta(\\chi H)-\\stackrel{\\circ}{R}(H)=\\Lambda g\_{e u c}+O(r^{-2n}),
$$

(3.10)

where we used that Hiikl = Λδkl. Using the fact that

is traceless,

$$
H\_{i i k l}=\\Lambda\\delta\_{k l}
$$

$$
\\langle P\_{g\_{c a l}}(\\chi H)-\\Lambda g\_{c a l},o\\rangle=\\langle P\_{g\_{c a l}}(\\chi H),o\\rangle.
$$

(3.11)

* * *

Integrating by parts yields

$$
\\int\_{r\\leq r\_{0}}\\langle P\_{g\_{c a l}}(\\chi H),o\\rangle d V\_{g\_{c a l}}=\\frac{1}{2}\\int\_{r=r\_{0}}(\\langle\\chi H,\\nabla\_{\\vec{n}}o\\rangle-\\langle\\nabla\_{\\vec{n}}(\\chi H),o\\rangle)d S\_{S\_{r\_{0}/\\Gamma\_{n}}}.
$$

(3.12)

Notice that we have the following asymptotic relations

$$
\\nabla\_{\\vec{n}}o=\\frac{-2n}{r}o+O\\big(r^{-2n-2}\\big)
$$

(3.13)

$$
\\nabla\_{\\vec{n}}(\\chi H)=\\frac{2}{r}H+O(1),
$$

(3.14)

as _r →∞,_ so taking the limit as _r0 →∞_ we obtain

$$
r\\to\\infty
$$

$$
r\_{0}\\rightarrow\\infty
$$

$$
\\int\_{X}\\langle P\_{g\_{c a l}}(\\chi H),o\\rangle d V\_{g\_{c a l}}=-\\lim\_{r\\rightarrow\\infty}\\int\_{S\_{r}/\\Gamma\_{n}}\\frac{n+1}{r}\\langle H,o\\rangle d S\_{S\_{r}/\\Gamma\_{n}}.
$$

(3.15)

Now applying Lemma 10 we should have

$$
\\langle-P\_{g\_{c a l}}(\\chi H)+\\Lambda g\_{c a l}+\\lambda o,o\\rangle=0
$$

(3.16)

which implies

$$
\\lambda=-\\frac{1}{\|o\| _{L^2}^2}\\lim_{r\\to\\infty}\\int\_{S\_r/\\Gamma\_n}\\frac{n+1}{r}\\langle H,o\\rangle dS\_{S\_r/\\Gamma\_n}.
$$

(3.17)

Conversely, assume that (3.7) is satisfied. This implies that (3.16) is satisfied and by
Lemma 10 there exist a solution h′ for the following problem:

$$
-P\_{g\_{c a l}}(\\chi H)+\\Lambda g\_{c a l}+\\lambda o=P(h^{\\prime}).
$$

(3.18)

So h = h′ +χH is the desired solution. Next, we show that h is in Bianchi gauge. Since
the Calabi metric is Ricci-flat, we have

$$
h=h'+\\chi H
$$

$$
0=B\_{g\_{c a l}}P\_{g\_{c a l}}h=\\frac{1}{2}\\nabla^{\*}\\nabla B\_{g\_{c a l}}h.
$$

(3.19)

* * *

Also,

$$
h=H+O\\big(r^{-2n+2+\\epsilon}\\big)\\implies B\_{g\_{c a l}}h=O\\big(r^{-2n+1+\\epsilon}\\big).
$$

(3.20)

Let ω = Bgcalh. Then integrating by parts implies
∫ ∫

$$
\\omega=B\_{g\_{cal}}h
$$

$$
0=\\int\_{B\_{r}/\\Gamma\_{n}}\\langle\\omega,\\Delta\\omega\\rangle d V\_{g\_{c a l}}=\\int\_{B\_{r}/\\Gamma\_{n}}\\lvert\\nabla\\omega\\rvert^{2}d V\_{g\_{c a l}}-\\int\_{S\_{r}/\\Gamma\_{n}}\\langle\\omega,\\nabla\_{\\vec{n}}\\omega\\rangle d S,
$$

(3.21)

and taking the limit as _r →∞_ shows that _∇ω_ = 0 and the later implies that _ω_ = 0.

$$
r\\to\\infty
$$

$$
\\nabla\\omega=0
$$

$$
\\omega=0
$$

#### 3.1 Reformulation of the obstruction

We begin with some integral identities.

Lemma 11. On R2n with coordinates (

x1,...,x2n) we have the following:

$$
\\textit{On}\\mathbb{R}^{2n}
$$

$$
\\left(x^{1},...,x^{2n}\\right)
$$

$$
\\int\_{S^{2n-1}}x^i x^j dS=\\frac{\\omega\_{2n-1}}{2n}\\delta\_{ij}
$$

(3.22)

$$
\\int\_{S^{2n-1}}x^{i}x^{j}x^{k}x^{l}d S=\\frac{\\omega\_{2n-1}}{2n(2n+2)}\\big(\\delta\_{k l}\\delta\_{i j}+\\delta\_{k i}\\delta\_{l j}+\\delta\_{k j}\\delta\_{i l}\\big).
$$

(3.23)

_Proof._ This is proved, for example, in \[11\].

Let g be a Riemannian metric on R2n
coordinates has the form

. The Taylor expansion of the metric in normal

$$
g
$$

$$
\\mathbb{R}^{2n}
$$

$$
g\_{k l}(z)=\\delta\_{k l}-\\frac{1}{3}R\_{i k j l}z^{i}z^{j}+O(\|z\|^{3})
$$

(3.24)

as _\|z\|→_ 0\. The quadratic term is not in Bianchi gauge, so we use the following lemma.

$$
\|z\|\\to0
$$

Lemma 12. _Assume that g0 is Einstein of dimension 2n, with Ric(g0_) = _Λg0. Then_
_there exists a coordinate system near the origin such that_

$$
2n\_{!}
$$

$$
g\_{0}
$$

$$
Ric(g\_0)=\\Lambda g\_0
$$

$$
g\_{k l}(z)=\\delta\_{k l}(0)+H\_{i j k l}z^{i}z^{j}+O(\|z\|^{3}),
$$

(3.25)

* * *

_as \|x\|→ 0, where_

$$
\|x\|\\to0
$$

$$
H\_{i j k l}z^{i}z^{j}=-\\frac{1}{3}R\_{i k j l}z^{i}z^{j}-\\frac{\\Lambda}{3(n+1)}(\\delta\_{k l}\|z\|^{2}+2z^{k}z^{l}).
$$

(3.26)

_Proof._ It is easy to verify that

$$
B\_{e u c}(-\\frac{1}{3}R\_{i k j l}z^{i}z^{j})=-\\frac{2}{3}\\Lambda z^{i},
$$

(3.27)

and that

$$
B\_{e u c}\\left(\\delta\_{i j}\|z\|^{2}+2z^{i}z^{j}\\right)=-(2n+2)z^{i}.
$$

(3.28)

$$
B\_{e u c}(H\_{i j k l}z^{i}z^{j})=0.
$$

Consequently,

(3.29)

Finally, we note that

$$
\\delta\_{e u c}^{\*}(\|z\|^{2}z^{i})=\\delta\_{i j}\|z\|^{2}+2z^{i}z^{j},
$$

(3.30)

so the added term is a Lie derivative of a cubic vector field. A standard argument, see
for example \[1, Section 7\], implies that there is a coordinate system with the stated
property.

Proposition 3.2. Let H = Hijklxixjdxkdxl

_be the symmetric_ 2- _tensor with_

$$
H=H\_{ijkl}x^{i}x^{j}dx^{k}dx^{l}
$$

$$
H\_{i j k l}=-\\frac{1}{3}R\_{i k j l}-\\frac{\\Lambda}{3(n+1)}(\\delta\_{i j}\\delta\_{k l}+2\\delta\_{i k}\\delta\_{j l}).
$$

(3.31)

_Then the constant λ in Proposition 3.1 is given by_

$$
\\lambda
$$

$$
\\lambda=\\frac{1}{\|o\| _{L^{2}}}\\frac{\\omega_{2n-1}}{n}\\Big(\\frac{2-n}{2}\\Lambda-\\frac{1}{8}\\langle\\mathcal{R}(\\omega),\\omega\\rangle\\Big).
$$

(3.32)

* * *

_Proof._ Recall from (2.41) that

$$
o=\\frac{1}{1+r^{2n}}\\Big(-g\_{c a l}+n(d\\bar{r}\\otimes d\\bar{r})+n(\\bar{\\theta}\\otimes\\bar{\\theta})\\Big),
$$

(3.33)

so in ALE coordinates, we have

$$
o=\\frac{1}{r^{2n}}\\Big(-g\_{ec}+n(dr\\otimes dr)+nr^2(\\theta\\otimes\\theta)\\Big)+O(r^{-2n-1})
$$

(3.34)

as _r →∞._ Defining

$$
r\\to\\infty
$$

$$
o\_{e u c}=\\frac{1}{r^{2n}}\\Big(-g\_{e u c}+n(d r\\otimes d r)+n r^{2}(\\theta\\otimes\\theta)\\Big),
$$

(3.35)

$$
\\lim\_{r\\rightarrow\\infty}\\int\_{S\_{r}/\\Gamma\_{n}}\\frac{n+1}{r}\\langle H,o\\rangle d S\_{S\_{r}/\\Gamma\_{n}}=\\int\_{\|x\|=1}(n+1)\\langle H,o\_{e u c}\\rangle d S\_{S\_{r}/\\Gamma\_{n}}.
$$

we have

(3.36)

The inner product is

$$
\\langle H,o\_{e u c}\\rangle=-\\langle H,g\_{e u c}\\rangle+n\\langle H,d r\\otimes d r\\rangle+n\\langle H,r^{2}\\theta\\otimes\\theta\\rangle.
$$

(3.37)

We lift up to R2n, and next we calculate each term in (3.37); the first term is

$$
\\mathbb{R}^{2n}
$$

$$
\\langle H,g\_{e u c}\\rangle=H\_{i j l l}x^{i}x^{j},
$$

(3.38)

so by (3.22),

$$
\\int\_{\|x\|=1}\\langle H,g\_{e u c}\\rangle d S=\\frac{\\omega\_{2n-1}}{2n}H\_{i i k k}.
$$

(3.39)

Also, since r2 = (xi)2, we have

$$
r^{2}=\\left(x^{i}\\right)^{2}
$$

$$
rdr=x^{i}dx^{i}
$$

(3.40)

$$
r^{2}d r\\otimes d r=x^{i}x^{j}d x^{i}d x^{j}.
$$

(3.41)

* * *

Letting J denote the standard complex structure on R2n, then θ = −J(dr), so we have
r

$$
\\mathbb{R}^{2n}
$$

$$
\\theta=-J\\left(\\frac{dr}{r}\\right)
$$

$$
\\left(r\\theta\\right)\\otimes\\left(r\\theta\\right)=x^{p}x^{q}J\_{k}^{p}J\_{l}^{q}d x^{k}d x^{l}.
$$

(3.42)

Clearly,

$$
r^{2}\\langle\\theta\\otimes\\theta,H\\rangle=x^{i}x^{j}x^{p}x^{q}J\_{k}^{p}J\_{l}^{q}H\_{i j k l},
$$

(3.43)

$$
r^{2}\\langle d r\\otimes d r,H\\rangle=x^{i}x^{j}x^{k}x^{l}H\_{i j k l}.
$$

(3.44)

Using (3.23), this implies that
∫

$$
\\begin{align\*}\\int\_{\|x\|=1}\\langle H,dr\\otimes dr\\rangle dS&=\\int\_{\|x\|=1}H\_{ijkl}x^i x^j x^k x^l dS\\&=\\frac{\\omega\_{2n-1}}{2n(2n+2)}(\\delta\_{ij}\\delta\_{kl}+\\delta\_{ik}\\delta\_{jl}+\\delta\_{il}\\delta\_{jk})H\_{ijkl}\\&=\\frac{\\omega\_{2n-1}}{2n(2n+2)}(H\_{iikk}+H\_{ikik}+H\_{ikki}).\\end{align\*}
$$

(3.45)

Also, (3.23) implies
∫

$$
\\begin{align\*}\\int\_{\|x\|=1}\\langle H,\\theta\\otimes\\theta\\rangle dS&=\\int\_{\|x\|=1}H\_{ijkl}x^i x^j x^p x^q J\_k^p J\_l^q dS\\&=\\frac{\\omega\_{2n-1}}{2n(2n+2)}(\\delta\_{ij}\\delta\_{pq}+\\delta\_{ip}\\delta\_{jq}+\\delta\_{iq}\\delta\_{jp})J\_k^p J\_l^q H\_{ijkl}\\&=\\frac{\\omega\_{2n-1}}{2n(2n+2)}(J\_k^p J\_l^p H\_{iikl}+J\_k^p J\_l^q H\_{pqkl}+J\_k^p J\_l^q H\_{qpkl}).\\end{align\*}
$$

(3.46)

Putting together (3.39), (3.45), and (3.46), we obtain
∫

$$
\\begin{aligned}{\\int\_{\|x\|=1}(n+1)\\langle H,o\_{e u c}\\rangle d S=-\\frac{\\omega\_{2n-1}}{2n}(n+1)H\_{k k l l}+\\frac{\\omega\_{2n-1}}{4}(H\_{i i k k}+H\_{i k i k}+H\_{i k k i})}\ {+\\frac{\\omega\_{2n-1}}{4}(J\_{k}^{p}J\_{l}^{p}H\_{i i k l}+J\_{k}^{p}J\_{l}^{q}H\_{p q k l}+J\_{k}^{p}J\_{l}^{q}H\_{q p k l}).}\ \\end{aligned}
$$

(3.47)

Next we compute the terms involving _H_ appearing in (3.47). First,

$$
\\begin{align\*}H\_{kkll}&=-\\frac{1}{3}R\_{klkl}-\\frac{\\Lambda}{3(n+1)}(\\delta\_{kk}\\delta\_{ll}+2\\delta\_{kl}\\delta\_{kl})\\&=-\\frac{1}{3}\\Lambda(2n)-\\frac{\\Lambda}{3(n+1)}((2n)^2+4n)=-2n\\Lambda.\\end{align\*}
$$

(3.48)

* * *

The next two terms are

$$
H\_{i k i k}=-\\frac{1}{3}R\_{i i k k}-\\frac{\\Lambda}{3(n+1)}\\big(\\delta\_{i k}\\delta\_{i k}+2\\delta\_{i i}\\delta\_{k k}\\big)=-\\frac{\\Lambda}{3(n+1)}(2n+8n^{2}),
$$

(3.49)

and

$$
\\begin{aligned}H\_{ikki}&=-\\frac{1}{3}R\_{ikki}-\\frac{\\Lambda}{3(n+1)}(\\delta\_{ik}\\delta\_{ik}+2\\delta\_{ik}\\delta\_{ik})\\&=\\frac{1}{3}2n\\Lambda-\\frac{\\Lambda}{3(n+1)}6n=\\frac{2n\\Lambda}{3}-\\frac{2n\\Lambda}{n+1}.\\end{aligned}
$$

(3.50)

The first term involving _J_ is

$$
\\begin{align\*}J\_{k}^{p}J\_{l}^{p}H\_{iikl}&=J\_{k}^{p}J\_{l}^{p}\\Big(-\\frac{1}{3}R\_{ikil}-\\frac{\\Lambda}{3(n+1)}(\\delta\_{ii}\\delta\_{kl}+2\\delta\_{ik}\\delta\_{il})\\Big)\\&=-\\frac{1}{3}\\Lambda(2n)-\\frac{\\Lambda}{3(n+1)}((2n)^{2}+4n)=-2n\\Lambda.\\end{align\*}
$$

(3.51)

The next term is

$$
\\begin{align\*}J\_{k}^{p}J\_{l}^{q}H\_{pqkl}&=J\_{k}^{p}J\_{l}^{q}\\Big(-\\frac{1}{3}R\_{pkql}-\\frac{\\Lambda}{3(n+1)}(\\delta\_{pq}\\delta\_{kl}+2\\delta\_{pk}\\delta\_{ql})\\Big)\\&=-\\frac{1}{3}\\langle\\mathcal{R}(\\omega),\\omega\\rangle-\\frac{2n\\Lambda}{3(n+1)}.\\end{align\*}
$$

(3.52)

For the last term, we compute

$$
\\begin{align\*}J\_{k}^{p}J\_{l}^{q}H\_{qpkl}&=J\_{k}^{p}J\_{l}^{q}\\Big(-\\frac{1}{3}R\_{qkpl}-\\frac{\\Lambda}{3(n+1)}(\\delta\_{qp}\\delta\_{kl}+2\\delta\_{qk}\\delta\_{pl})\\Big)\\&=-\\frac{1}{3}J\_{k}^{p}J\_{l}^{q}R\_{qkpl}+\\frac{2n\\Lambda}{3(n+1)}.\\end{align\*}
$$

(3.53)

Note that using the Bianchi identity, we have

$$
\\begin{align\*}0&=J\_{k}^{p}J\_{l}^{q}(R\_{qkpl}+R\_{kpql}+R\_{pqkl})\\&=J\_{k}^{p}J\_{l}^{q}R\_{qkpl}-J\_{p}^{k}J\_{l}^{q}R\_{kpql}-J\_{k}^{p}J\_{l}^{q}R\_{pqlk}\\&=J\_{k}^{p}J\_{l}^{q}R\_{qkpl}-J\_{p}^{k}J\_{l}^{q}R\_{kpql}+J\_{k}^{p}J\_{q}^{l}R\_{pqlk}.\\end{align\*}
$$

(3.54)

The first and third terms in the last line of (3.54) are easily seen to be equal, thus we
have

$$
J\_{k}^{p}J\_{l}^{q}R\_{q k p l}=\\frac{1}{2}\\langle\\mathcal{R}(\\omega),\\omega\\rangle.
$$

(3.55)

* * *

Plugging (3.55) into (3.53), we obtain

$$
J\_{k}^{p}J\_{l}^{q}H\_{q p k l}=-\\frac{1}{6}\\langle\\mathcal{R}(\\omega),\\omega\\rangle+\\frac{2n\\Lambda}{3(n+1)}.
$$

(3.56)

We now insert (3.48), (3.49), (3.50), (3.51), (3.52), and (3.56) into (3.47) to obtain

$$
\\begin{aligned}&\\int\_{\|x\|=1}^{\\infty}(n+1)\\langle H,o\_{euc}\\rangle dS=-\\frac{\\omega\_{2n-1}}{2n}(n+1)(-2n\\Lambda)\\&+\\frac{\\omega\_{2n-1}}{4}\\Big(-2n\\Lambda-\\frac{\\Lambda}{3(n+1)}(2n+8n^2)+\\frac{2n\\Lambda}{3}-\\frac{2n\\Lambda}{n+1}\\Big)\\+&\\frac{\\omega\_{2n-1}}{4}\\Big(-2n\\Lambda-\\frac{1}{3}\\langle\\mathcal{R}(\\omega),\\omega\\rangle-\\frac{2n\\Lambda}{3(n+1)}-\\frac{1}{6}\\langle\\mathcal{R}(\\omega),\\omega\\rangle+\\frac{2n\\Lambda}{3(n+1)}\\Big).\\end{aligned}
$$

(3.57)

This simplifies to

$$
\\int\_{\|x\|=1}(n+1)\\langle H,o\\rangle d S=\\omega\_{2n-1}\\Big(\\frac{2-n}{2}\\Lambda-\\frac{1}{8}\\langle\\mathcal{R}(\\omega),\\omega\\rangle\\Big).
$$

(3.58)

Finally, since we are integrating over S2n−1
ω
sphere is 2n−1, which accounts for the extra factor of
_n_

/Γ, where Γ is of order _n,_ the area of the unit
1
appearing in (3.32).
_n_

$$
S^{2n-1}/\\Gamma
$$

$$
n,
$$

$$
\\frac{\\omega\_{2n-1}}{n}
$$

$$
\\frac{1}{n}
$$

* * *

## The refined approximate metric

The approximate metric described in the introduction will be referred to as the “näıve”
approximate metric. In this chapter, we will construct a “refined” approximate metric,
which will be necessary to compute the obstruction. The construction closely follows
that in \[10\] with minor modifications. Recall that the Einstein orbifold is denoted by
(M0,g0) and (X,gcal) denotes the Calabi metric. Also, recall that {xi},i = 1...2n, are
ALE coordinates on _X,_ and that _g0_ satisfies

$$
\\left(M\_{0},g\_{0}\\right)
$$

$$
(X,g\_{cal})
$$

$$
{x^{i}},i=1\\ldots2n
$$

$$
g\_{0}
$$

$$
X
$$

$$
Ric(g\_0)=\\Lambda g\_0.
$$

(4.1)

Near p0, we use the coordinate system {zi},i = 1...2n, from Lemma 12, where g0 takes
the form

$$
p\_{0}
$$

$$
{z^{i}},i=1\\ldots2n
$$

$$
g\_{0}
$$

$$
g\_{0}=g\_{e u c}+H+o(\|z\|^{2}),
$$

(4.2)

with

$$
H=H\_{i j k l}z^{i}z^{j}d z^{k}d z^{l},
$$

(4.3)

given by (3.26).

On the Calabi metric, using Proposition 3.1, there exists a solution _(h,λ)_ for the following problem

$$
\\begin{align\*}P\_{g\_{cal}}Ric(h)&=\\Lambda g\_{cal}+\\lambda o,\\h&=H+O(r^{2-2n+\\epsilon}),\\B\_{g\_{cal}}(h)&=0,\\end{align\*}
$$

(4.4)

for any > 0, where _λ_ is given by (3.32), as _r →∞._ Define

$$
\\epsilon>0
$$

$$
r\\to\\infty
$$

$$
h\_{t}=g\_{cal}+th.
$$

(4.5)

Consider the Calabi metric on Cn −{0}/Γn and define the following two regions

$$
\\mathbb{C}^n-{0}/\\Gamma\_n
$$

$$
DZ^{t}\\equiv{\\frac{1}{2}t^{-\\frac{1}{4}}<r<2t^{-\\frac{1}{4}}}
$$

(4.6)

$$
X^{t}\\equiv{r<2t^{-\\frac{1}{4}}},
$$

(4.7)

(DZ is short for damage zone). Now define the following function on Cn −{0}/Γn
8

$$
\\mathbb{C}^n-{0}/\\Gamma\_n
$$

$$
\\begin{aligned}&\\rho=\\left{\\begin{aligned}\ &r&\\quad when r>2\\&\\&1&\\quad when r\\leq1,\ &\\end{aligned}\\right.\ \\end{aligned}
$$

(4.8)

Lemma 13. For t sufficiently small, ht is a Riemannian metric on Xt and the following
_estimate holds on this region_

$$
h\_{t}
$$

$$
X^{t}
$$

$$
\|\\nabla^{k}(R i c\_{h\_{t}}-t\\Lambda h\_{t}-t\\lambda o)\| _{g_{c a l}}\\leq c\_{k}t^{2}\\rho^{2-k},
$$

(4.9)

for some constants ck and any k ≥ 0.

$$
k\\geq0
$$

$$
c\_{k}
$$

_Proof._ Since _h_ has quadratic leading term and _g_
that \|h\|gcal(p) ≤ cρ2(p) for any p ∈ Xt. It follows that

cal is ALE, there exist a constant c so

$$
g\_{cal}
$$

$$
\|h\| _{g_{cal}}(p)\\leq c\\rho^2(p)
$$

$$
p\\in X^{t}
$$

$$
\|t h\| _{g_{c a l}}(p)\\leq c t\\rho^{2}(p)\\leq2c t^{\\frac{1}{2}}.
$$

(4.10)

* * *

The right hand side is independent of p so ht is a Riemannian metric on Xt for small t.
Recall that

$$
p
$$

$$
h\_{t}
$$

$$
X^{t}
$$

$$
d\_{g\_{cal}}Ric(h)=\\Lambda g\_{cal}+\\lambda o
$$

(4.11)

so we have

$$
Ric(g\_{cal}+th)=Ric(g\_{cal})+td\_{g\_{cal}}Ric(h)+Q(th),
$$

(4.12)

where _Q_ is a nonlinear term. For any Riemannian metric _g,_ and symmetric tensor _h_
small, recall the well-known expansion

$$
Q
$$

$$
g,
$$

$$
h
$$

$$
R m\_{g+h}=R m\_{g}+(g+h)^{-1} _\\nabla^{2}h+(g+h)^{-2}_\\nabla h\*\\nabla h,
$$

(4.13)

where _∗_ denotes various tensor contractions (see, for example \[15, Section 3\]). Contracting again, we obtain

$$
R i c\_{g+h}=(g+h)^{-1} _R m\_{g}+(g+h)^{-2}_\\nabla^{2}h+(g+h)^{-3} _\\nabla h_\\nabla h.
$$

(4.14)

It follows that for _t_ sufficiently small

$$
\|Q(t h)\|\\leq c\_{1}t^{2}(\|R m\_{g\_{c a l}}\|h\|^{2}+\|h\|\\nabla^{2}h\|+\|\\nabla h\|^{2}).
$$

(4.15)

Using (4.4), it follows that

$$
\|R i c(h\_{t})-t\\Lambda h\_{t}-\\lambda o\|=c\_{1}t^{2}(\|R m\_{g\_{c a l}}\|h\|^{2}+\|h\|\\nabla^{2}h\|+\|\\nabla h\|^{2})
$$

(4.16)

Note that

$$
\\left\|\\nabla^{k}h\\right\|\\leq c\_{k}\\rho^{2-k},
$$

(4.17)

so the lemma for _k_ = 0 follows. For _k_ \> 0 the proof is similar, and is omitted.

$$
k=0
$$

* * *

Recalling the attaching map φt defined in (1.8), consider

$$
\\phi\_{t}
$$

$$
M^{t}=M\_{0}^{t}\\cup\_{\\phi\_{t}}X^{t}
$$

(4.18)

where

$$
M\_{0}^{t}=M\\setminus B(p\_{0},(1/2)t^{1/4}).
$$

(4.19)

To define the refined approximate metric on

Mt, let χ be as in (1.10),

$$
M^{t}
$$

$$
\\chi
$$

$$
\\begin{aligned}&g\_{t}=\\left{\\begin{aligned}\ &g\_{0}&&M\\setminus B(p\_{0},2t^{1/4})\\&\\&(1-\\chi\_{t}(r))\\phi\_{t}^{\*}g+\\chi\_{t}(r)th\_{t}&&(1/2)t^{-1/4}<r<2t^{-1/4}\\&\\&th\_{t}&&r<(1/2)t^{-1/4}\ &\\end{aligned}\\right..\ \\end{aligned}
$$

(4.20)

We have the following estimation.

Lemma 14. For each integer k ≥ 0, there exist a constant ck so that gt satisfies the
following estimate on Xt

$$
k\\geq0
$$

$$
c\_{k}
$$

$$
g\_{t}
$$

$$
X^{t}
$$

$$
\|\\nabla^{k}(R i c\_{g\_{t}}-\\Lambda g\_{t}-t\\lambda\\chi\_{t}(\\rho)o)\| _{g_{c a l}}\\leq c\_{k}t^{2}\\rho^{2-k},
$$

(4.21)

where the covariant derivatives and norm are taken with respect to gcal.

$$
g\_{cal}
$$

1
Proof. If r < 12t− 4then gt = tht and by Lemma 13 we are done. If

$$
r<\\frac{1}{2}t^{-\\frac{1}{4}}
$$

$$
g\_{t}=th\_{t}
$$

$$
(1/2)t^{-1/4}<r<2t^{-1/4}
$$

(4.22)

$$
g\_{t}=(1-\\chi\_{t}(r))\\phi\_{t}^{\*}g\_{0}+\\chi\_{t}(r)t h\_{t}
$$

then gt = (1 − χt(r))φ∗t g0 \+ χt(r)

tht. Recall that

$$
\\phi\_{t}^{\*}g\_{0}=tg\_{euc}+t^{2}H+tO\\left(t^{\\frac{3}{2}}r^{3}\\right)
$$

(4.23)

$$
t h\_{t}=t g\_{e u c}+t^{2}H+t O\\left(r^{-2n}\\right)+t O\\left(r^{2-2n+\\epsilon}\\right).
$$

(4.24)

* * *

Since the quadratic terms agree, we have the estimate

$$
g\_{t}=tg\_{euc}+t^{2}H+tO\\left(t^{\\frac{3}{2}}\\rho^{3}\\right).
$$

(4.25)

Writing

$$
\\theta=g\_{t}-t g\_{e u c},
$$

(4.26)

expanding the Ricci tensor near t · geuc we have

$$
t\\cdot g\_{euc}
$$

$$
R i c\_{g\_{t}}=d\_{t\\cdot e u c}R i c(\\theta)+Q\_{e u c}(\\theta),
$$

(4.27)

where Qeuc(θ) satisfies the estimate

$$
Q\_{euc}(\\theta)
$$

$$
t^{2}\|Q\_{e u c}(\\theta)\|\\leq c(\|\\theta\|\\nabla^{2}\\theta\|+\|\\nabla\\theta\|^{2}),
$$

(4.28)

for some constant c, where the norms are with respect to geuc. Note that (4.22) implies
that

$$
g\_{euc}
$$

$$
t\\lambda\\chi\_{t}(\\rho)o=O(t^{2}\\rho^{2}).
$$

(4.29)

From (4.4) it follows that

$$
d\_{t\\cdot e u c}R i c(\\theta)=t\\Lambda g\_{e u c}+O(t^{2}\\rho^{2}),
$$

(4.30)

where _O_ is with respect to the Euclidean metric. Finally we obtain

$$
R i c\_{g\_{t}}-\\Lambda g\_{t}-t\\lambda\\chi\_{t}(\\rho)o=O(t^{2}\\rho^{2}),
$$

(4.31)

so the lemma for _k_ = 0 follows. For general _k_ the proof is similar and is omitted.

$$
k=0
$$

* * *

# Solution of the Einstein equation modulo obstructions

#### 5.1 Function Spaces

In this section we define the function spaces that we will need in order to apply the
implicit function theorem. Let E be a tensor bundle over Xt and δ0 ∈ R be a weight.
We define Cδk,α(Xt,E) to be
0

$$
X^{t}
$$

$$
\\delta\_{0}\\in\\mathbb{R}
$$

$$
C\_{\\delta\_{0}}^{k,\\alpha}(X^{t},E)
$$

$$
\\left\|s\\right\| _{\\alpha}\\equiv\\sup_{d(x,y)<i\_{g\_{cal}}}\\frac{\\left\|s(x)-s(y)\\right\|}{d(x,y)^{\\alpha}}
$$

(5.1)

$$
\|s\| _{C_{\\delta\_{0}}^{k,\\alpha}}\\equiv\\sum\_{i=0}^{k}(\\sup\\rho^{\\delta\_{0}+i}\|\\nabla^{i}s\|)+\|\\rho^{\\delta\_{0}+k+\\alpha}\\nabla^{k}s\|\_{\\alpha}.
$$

(5.2)

Note s(x) and s(y) in (5.1) are compared by means of parallel transport. Let ip0denote
the injectivity radius at the point _p0._ Define the following function
8

$$
s(x)
$$

$$
s(y)
$$

$$
i\_{p\_{0}}
$$

$$
p\_{0}
$$

$$
\\begin{aligned}&\\tilde{z}=\\left{\\begin{aligned}\ &\|z\|&\\quad&for\|z\|<\\tfrac{1}{2}i\_{p\_0}\\&&&\\&1&&on M\_0-B(p\_0,z\_{p\_0})\ &\\end{aligned}\\right..\ \\end{aligned}
$$

(5.3)

We can define a similar norm Cδk,α(M0,E) for tensor bundles over M0
0

$$
C\_{\\delta\_{0}}^{k,\\alpha}(M\_{0},E)
$$

$$
M\_{0}
$$

$$
\|s\| _{C_{\\delta\_{0}}^{k,\\alpha}}\\equiv\\sum\_{i=0}^{k}(\\sup\\tilde{z}^{\\delta\_{0}+i}\|\\nabla^{i}s\|)+\|\\tilde{z}^{\\delta\_{0}+k+\\alpha}\\nabla^{k}s\|\_{\\alpha}.
$$

(5.4)

* * *

When (M0,∂M0,g0,x) is AH, for another weight δ∞∈ R, we define Cδk,α
0,δ
the norm

_(M0,E)_ by
_∞_

$$
\\left(M\_{0},\\partial M\_{0},g\_{0},x\\right)
$$

$$
\\delta\_{\\infty}\\in\\mathbb{R}
$$

$$
AH,
$$

$$
C\_{\\underline{{\\delta\_{0}}},\\underline{{\\delta\_{\\infty}}}}^{k,\\alpha}(M\_{0},E)
$$

$$
\\left\|s\\right\| _{C_{\\delta\_0,\\delta\_\\infty}^{k,\\alpha}}\\equiv\\left\|\\tilde{x}^{-\\delta\_\\infty}s\\right\| _{C_{\\delta\_0}^{k,\\alpha}},
$$

(5.5)

where _x˜_ is defined in (1.18). We also need to define function spaces _C_
topological desingularization Mt. Consider the following norms

δk,α on the
0 _,δ_ ∞ _;t_

$$
\\tilde{x}
$$

$$
C\_{\\delta\_{0},\\delta\_{\\infty};t}^{k,\\alpha}
$$

$$
M^{t}
$$

$$
\\left\|s\\right\| _{C_{\\delta\_0,\\delta\_{\\infty};t}^{k,\\alpha}}\\equiv t^{\\frac{\\delta\_0+l}{2}}\\left\|\\chi\_t s\\right\| _{C_{\\delta\_0}^{k,\\alpha}(X^t)}+\\left\|(1-\\chi\_t)s\\right\| _{C_{\\delta\_0,\\delta\_{\\infty}}^{k,\\alpha}(M\_0^t)},
$$

(5.6)

$$
\|s\| _{C_{\\delta\_{0},\\delta\_{\\infty};t}^{k,\\alpha}}^{\\prime}\\equiv\\sum\_{i=0}^{k}(\\sup w^{\\delta\_{0}+i}\|\\nabla^{i}(\\tilde{x}^{-\\delta\_{\\infty}}s)\|+\|w^{\\delta\_{0}+k+\\alpha}\\nabla^{k}(\\tilde{x}^{-\\delta\_{\\infty}}s)\|\_{\\alpha},
$$

(5.7)

where _l_ = _r − s_ for an _(r,s)_ tensor _E_ and _w_ is the weight function and the covariant
derivatives are with respect to gt in last expression. It is easy to see that these norms are
uniformly equivalent when _t_ is sufficiently small, so we will use them interchangeably,
and omit the prime notation. The exponent of _t_ in (5.6) follows because

$$
l=r-s
$$

$$
(r,s)
$$

$$
g\_{t}
$$

$$
t^{\\frac{l}{2}}\|s\| _{\\frac{g}{t}}=\|s\|_{g},
$$

(5.8)

z˜
and since _ρ_ is comparable to√in the damage zone.
_t_

$$
\\rho
$$

$$
\\frac{\\tilde{z}}{\\sqrt{t}}
$$

In the following, we fix _δ0_ \> 0 and _δ_ ∞\> 0 sufficiently small.

$$
\\delta\_{0}>0
$$

$$
\\delta\_{\\infty}>0
$$

#### 5.2 Lyapunov-Schmidt reduction

Define the space of obstructions

$$
\\mathcal{O} _{t}\\subset C_{\\delta\_{0}+2,\\delta\_{\\infty};t}^{\\alpha}(M^{t})
$$

(5.9)

to be the one-dimensional span of _χ(t)o._ Define the following operator

$$
\\chi(t)o
$$

$$
\\Phi\_{g\_{t}}(g)=R i c(g)-\\Lambda g+\\delta\_{g}^{\*}B\_{g\_{t}}g.
$$

(5.10)

* * *

The essential ingredient to the gluing argument is the following implicit function theorem
\[10\].

Lemma 15. _Let_ Φ : _E→F be a differentiable map between Banach spaces and_

$$
\\Phi:E\\rightarrow F
$$

$$
Q=\\Phi-\\Phi(0)-d\_0\\Phi.
$$

(5.11)

_Assume there exist positive constants q,r0,c such that_

$$
q,r\_{0},c
$$

$$
\\left\|Q(x)-Q(y)\\right\|\\leq q\\left\|x-y\\right\|\\left(\\left\|x\\right\|+\\left\|y\\right\|\\right)x,y\\in B(0,r\_{0})
$$

(5.12)

$$
d\_{0}\\Phi{\\it ~~i s~~ a n ~~i s o m o r p h i s m~~ a n d}\\left\|(d\_{0}\\Phi)^{-1}\\right\|\\leq c.
$$

(5.13)

1 r
If r ≤ min (r0, 2qc) and ‖Φ(0)‖≤ then Φ(x) = 0 has a unique solution in B(0,r).
_2c_

$$
\\begin{array}{l}{\\mathit{If};r\\leq\\operatorname\*{m i n}\\left(r\_{0},\\frac{1}{2q c}\\right)}\ \\end{array}
$$

$$
\|\\Phi(0)\|\\leq\\frac{r}{2c}
$$

$$
\\Phi(x)=0
$$

$$
B(0,r)
$$

Let v ∈ R and consider the following metric on Mt

$$
v\\in\\mathbb{R}
$$

$$
M^{t}
$$

$$
g\_{t,v}=g\_t+t v\\chi\_t o.
$$

(5.14)

Notice that

$$
\|t\\chi\_{t}o\| _{C_{\\delta\_{0},\\delta\_{\\infty};t}^{2,\\alpha}}=O(t^{\\frac{\\delta\_{0}}{2}}).
$$

(5.15)

Proposition 5.1. _Assume (M0,g0) is a non-degenerate Einstein orbifold with one sin-_
gular point p0 with orbifold group Γn (M0 can either be compact or AHE). Then there
_exist η,_ \> 0 _such that for any t < η and v ∈_ R _with \|v\|≤, there exist a unique metric_
ĝt,v solving the following equation

$$
\\left(M\_{0},g\_{0}\\right)
$$

$$
p\_{0}
$$

$$
\\Gamma\_{n}(M\_{0}
$$

$$
\\eta,\\epsilon>0
$$

$$
t<\\eta
$$

$$
v\\in\\mathbb{R}
$$

$$
\|v\|\\leq\\epsilon.
$$

$$
\\hat{g}\_{t,v}
$$

$$
\\Phi(\\hat{g} _{t,v})\\in\\mathcal{O}_{t},
$$

(5.16)

where ĝt,v satisfies the following

$$
\\hat{g}\_{t,v}
$$

$$
\|\\hat{g} _{t,v}-g_{t}\| _{C_{\\delta\_{0},\\delta\_{\\infty}}^{2,\\alpha}}\\leq\\epsilon t^{\\frac{\\delta\_{0}}{2}},
$$

(5.17)

$$
\\int\_{\\mathbb{P}^{n-1}}\\Big\\langle\\frac{1}{t}\\big(\\hat{g} _{t,v}-g_{t,v}\\big),o\\Big\\rangle\_{c a l}d V\_{c a l}=v.
$$

(5.18)

* * *

Also, if we write Φ(ˆgt,v) = λ(t)(χto), then we have the following estimation

$$
\\Phi\\left(\\hat{g} _{t,v}\\right)=\\lambda(t)\\left(\\chi_{t}o\\right)
$$

$$
\|\\hat{g} _{t,v}-g_{t,v}\| _{C_{\\delta\_{0},\\delta\_{\\infty};t}^{2,\\alpha}}\\leq c t^{1+\\frac{\\delta\_{0}}{4}},
$$

(5.19)

$$
\\lambda(t)=t\\lambda+O(t^{2-\\frac{\\delta\_0}{2}})
$$

(5.20)

_as t → 0._

$$
t\\to0.
$$

_Proof._ The following proof is very similar to \[10, Proposition 9.1\]. However, since scalings of various terms are different in higher dimensions, we give a fairly detailed outline
here, omitting some computations. To begin, define the following operator

$$
\\Phi:t^{-\\frac{\\delta\_{0}}{2}}\\tilde{C} _{\\delta_{0},\\delta\_{\\infty};t}^{2,\\alpha}\\oplus\\mathbb{R}\\to t^{-\\frac{\\delta\_{0}}{2}}C\_{\\delta\_{0}+2,\\delta\_{\\infty};t}^{\\alpha}
$$

(5.21)

$$
\\Phi\\big(h,x\\big)=R i c\_{g\_{t,v,h}}-\\Lambda g\_{t,v,h}+\\delta\_{g\_{t,v,h}}^{\*}B\_{g\_{t}}g\_{t,v,h}-x\\chi\_{t}o
$$

(5.22)

˜2,α
where gt,v,h = gt,v \+ h and Cδ is space of all Cδ0,δ _∞;t_
∫

2,α tensors like h which satisfies:
_0,δ∞;t_

$$
g\_{t,v,h}=g\_{t,v}+h
$$

$$
\\tilde{C} _{\\delta_{0},\\delta\_{\\infty};t}^{2,\\alpha}
$$

$$
C\_{\\delta\_{0},\\delta\_{\\infty};t}^{2,\\alpha}
$$

$$
\\int\_{\\mathbb{P}^{n-1}}\\Big\\langle\\frac{1}{t}(h-g\_{t}),o\\Big\\rangle\_{c a l}d V\_{c a l}=v.
$$

(5.23)

For simplicity of notation, in the remainder of the proof we will omit the variable _v._ We
δ δ
2˜2,α 2
want to apply Lemma 15 for E = t−0 Cδ;t ⊕R and F = t−0 Cδα+2,δ;t. From Lemma
0,δ _∞_ 0 ∞
13 it follows that

$$
E=t^{-\\frac{\\delta\_0}{2}}\\tilde{C} _{\\delta\_0,\\delta_\\infty;t}^{2,\\alpha}\\oplus
$$

$$
F=t^{-\\frac{\\delta\_0}{2}}C\_{\\delta\_0+2,\\delta\_\\infty;t}^{\\alpha}
$$

$$
\|\\Phi(0,0)\| _{C_{\\delta\_{0}+2,\\delta\_{\\infty};t}^{0,\\alpha}}=O(t^{1+\\frac{\\delta\_{0}}{4}}).
$$

(5.24)

The linearization of Φ at (0,0) is given by

(5.25)

$$
d\_{(0,0)}\\Phi(h,x)=P\_{t,v}h-x\\chi\_{t}o+\\frac{1}{2}(R i c\_{g\_{t,v}}\\circ h+h\\circ R i c\_{g\_{t,v}}-2\\Lambda h).
$$

Also the quadratic terms are given by

$$
Q\\left(h,x\\right)=\\Phi\\left(h,x\\right)-\\Phi\\left(0,0\\right)-d\_{\\left(0,0\\right)}\\Phi\\left(h,x\\right).
$$

(5.26)

* * *

Using the expansion (4.14), and a similar expansion for the gauge term (see \[15, Section\
3\]), it is not hard to see that there exist constants _r0_ and _q_ so that (5.12) is satisfied.
We need to show that d(0,0)Φ is an isomorphism with bounded inverse. Equivalently, we
need to show that there exists a constant _c_ \> 0 so that

$$
r\_{0}
$$

$$
q
$$

$$
d\_{(0,0)}\\Phi
$$

$$
c>0
$$

$$
t^{-\\frac{\\delta\_{0}}{2}}\\left\|h\\right\| _{C_{\\delta\_{0},\\delta\_{\\infty};t}^{2,\\alpha}}+\|x\|\\leq c t^{-\\frac{\\delta\_{0}}{2}}\\left\|d\_{(0,0)}\\Phi\\right\| _{C_{\\delta\_{0}+2,\\delta\_{\\infty};t}^{2,\\alpha}}.
$$

(5.27)

Assume this is not true, then there exist a sequence ti → 0 and (hi,xi) such that

$$
t\_{i}\\rightarrow0
$$

$$
\\left(h\_{i},x\_{i}\\right)
$$

$$
t\_{i}^{-\\frac{\\delta\_{0}}{2}}\\left\|h\_{i}\\right\| _{C_{\\delta\_{0},\\delta\_{\\infty};t\_{i}}^{2,\\alpha}}+\\left\|x\_{i}\\right\|=1,
$$

(5.28)

but

$$
\\left\|d\_{(0,0)}\\Phi(h\_{i},x\_{i})\\right\| _{C_{\\delta\_{0}+2,\\delta\_{\\infty};t\_{i}}^{2,\\alpha}}\\to0.
$$

(5.29)

Let us first consider that case that xi → 0\. Then without loss of generality we may
assume that

$$
x\_{i}\\rightarrow0
$$

$$
t\_{i}^{-\\frac{\\delta\_{0}}{2}}\\left\|h\_{i}\\right\| _{C_{\\delta\_{0},\\delta\_{\\infty};t\_{i}}^{0}}\\rightarrow1,
$$

(5.30)

and

$$
t\_{i}^{-\\frac{\\delta\_{0}}{2}}\\left\|d\_{(0,0)}\\Phi(h\_{i},x\_{i})\\right\| _{C_{\\delta\_{0}+2,\\delta\_{\\infty};t\_{i}}^{0,\\alpha}}\\to0.
$$

(5.31)

To get a contradiction, we briefly outline the standard blow-up argument. Let pi ∈ Mt
be a sequence of points such that norm is attained. By passing to a subsequence we can
assume that pi → p. There are three cases for p.

$$
p\_{i}\\in M\_{t}
$$

$$
p\_{i}\\rightarrow p
$$

_•_ If _p ∈ M0_ then by standard elliptic theory we can obtain a limit _h_ ∞satisfying
‖h∞‖C0 = 1 and Pg0h∞= 0. But this is impossible because we assumed that
_δ0,δ∞_ _M0_ is non-degenerate.

$$
p\\in M\_{0}
$$

$$
h\_{\\infty}
$$

$$
\\left\|h\_{\\infty}\\right\| _{C_{\\delta\_{0},\\delta\_{\\infty}}^{0}}=1
$$

$$
P\_{g\_0}h\_{\\infty}=0
$$

$$
M\_{0}
$$

* * *

• If p ∈ X then we can obtain a limit h∞with ‖h∞‖C0 = 1 and Pgcalh∞= 0. From
δ0
Theorem 2.3, _h_ ∞= _c · o,_ for some constant _c._ But then (5.18) implies that _c_ = 0,
a contradiction.

$$
p\\in X
$$

$$
h\_{\\infty}
$$

$$
\\left\|h\_{\\infty}\\right\| _{C_{\\delta\_{0}}^{0}}=1
$$

$$
P\_{g\_{cal}}h\_{\\infty}=0
$$

$$
h\_{\\infty}=c\\cdot o,
$$

$$
c=0
$$

• If p ∈ Cn/Γn then we can obtain a limit h∞with ‖h∞‖C0 = 1 and ∇∗∇h∞= 0,
δ0
but this is impossible since the indicial roots are the integers and _δ0_ was chosen
small but non-zero.

$$
p\\in\\mathbb{C}^n/\\Gamma\_n
$$

$$
h\_{\\infty}
$$

$$
\\left\|\\bar{h} _{\\infty}\\right\|_{C\_{\\delta\_0}^0}=\\bar{1}
$$

$$
\\nabla^{\*}\\nabla h\_{\\infty}=0
$$

$$
\\delta\_{0}
$$

Next, we show that xi → 0\. To prove this, we need the following estimates,

$$
x\_{i}\\rightarrow0
$$

$$
\|\\langle u,\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}\|\\leq C t^{n-2-\\frac{\\delta\_{0}}{2}}\\left\\Vert u\\right\\Vert\_{C\_{\\delta\_{0}+2,\\delta\_{\\infty};t}^{0,\\alpha}},
$$

(5.32)

$$
\|\\langle P\_{t}h,\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}\|\\leq C t^{n-\\frac{3}{2}-\\frac{\\delta\_{0}}{4}}\\left\|h\\right\| _{C_{\\delta\_{0},\\delta\_{\\infty};t}^{2,\\alpha}},
$$

(5.33)

$$
\\langle\\chi\_{t}o,\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}=t^{n-2}\\big(\\langle o,o\\rangle\_{L^{2}(g\_{c a l})}+O(t^{\\frac{n}{2}})\\big),
$$

(5.34)

for some constant _C_ \> 0\. The proofs of these estimates are almost exactly the same
as those of \[10, (71)-(73)\] and are omitted. Using (5.28), (5.33), and (5.34), we can
estimate

$$
C>0
$$

$$
\\langle d\_{(0,0)}\\Phi(h\_{i},x\_{i}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}=x\_{i}t\_{i}^{n-2}\\langle o,o\\rangle\_{L^{2}(g\_{c a l})}+o(t\_{i}^{n-2}),
$$

(5.35)

as _i →∞._ However, using (5.29) and (5.32), we also have

$$
i\\to\\infty
$$

$$
\\langle d\_{(0,0)}\\Phi(h\_{i},x\_{i}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}=o(t\_{i}^{n-2}),
$$

(5.36)

as _i →∞._ It follows that

$$
i\\to\\infty
$$

$$
x\_{i}t\_{i}^{n-2}\\langle o,o\\rangle\_{L^{2}(g\_{c a l})}=o(t\_{i}^{n-2}),
$$

(5.37)

as _i →∞._

$$
i\\to\\infty.
$$

* * *

Consequently, we must have xi → 0 as i →∞.

$$
x\_{i}\\rightarrow0
$$

$$
i\\to\\infty
$$

It remains to prove the expansion for λ(t). From Lemma 15, for each _t_ sufficiently
small, we obtain a solution (ht,xt) of Φ(ht,xt) = 0\. Defining ĝt = gt \+ ht, we have
Φgt(ˆgt) = λ(t)(χto). Notice that

$$
\\lambda(t)
$$

$$
\\left(h\_{t},x\_{t}\\right)
$$

$$
\\Phi(h\_{t},x\_{t})=0
$$

$$
\\hat{g} _{t}=g_{t}+h\_{t}
$$

$$
\\Phi\_{g\_{t}}(\\hat{g} _{t})=\\lambda(t)(\\chi_{t}o)
$$

$$
\\langle\\Phi\_{g\_{t}}(g\_{t}+h\_{t}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}=\\lambda(t)\\langle\\chi\_{t}o,\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}.
$$

(5.38)

On the other hand

$$
\\Phi\_{g\_{t}}\\left(\\hat{g} _{t}\\right)=\\Phi_{g\_{t}}\\left(g\_{t}\\right)+d\_{g\_{t}}\\Phi\_{g\_{t}}\\left(h\_{t}\\right)+Q\_{g\_{t}}\\left(h\_{t}\\right),
$$

(5.39)

which implies that

$$
\\langle\\Phi\_{g\_{t}}(\\hat{g} _{t}),\\chi_{t}o\\rangle\_{L^{2}(g\_{t})}=\\langle\\Phi\_{g\_{t}}(g\_{t}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}+\\langle d\_{g\_{t}}\\Phi\_{g\_{t}}(h\_{t}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}+\\langle Q\_{g\_{t}}(h\_{t}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}.
$$

(5.40)

Using (5.32), Lemma 14, and the expansion (4.14), respectively, we can estimate each
of the above terms by

$$
\\langle\\Phi\_{g\_{t}}(g\_{t}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}=\\lambda t^{n-1}\\left\|o\\right\| _{L^{2}(g_{c a l})}^{2}+O(t^{n}),
$$

(5.41)

$$
\\langle d\_{g\_t}\\Phi(h\_t),\\chi\_t o\\rangle\_{L^2(g\_t)}=O(t^{n-\\frac{1}{2}-\\frac{\\delta\_0}{4}})
$$

(5.42)

$$
\\langle Q\_{g\_{t}}(h\_{t}),\\chi\_{t}o\\rangle\_{L^{2}(g\_{t})}=O(t^{n-\\frac{\\delta\_{0}}{2}}),
$$

(5.43)

as _t →_ 0, and we obtain

$$
t\\to0
$$

$$
\\lambda(t)t^{n-2}\\left\|o\\right\| _{L^{2}(g_{c a l})}^{2}=t^{n-2}(\\lambda t\\left\|o\\right\| _{L^{2}(g_{c a l})}^{2}+O(t^{2-\\frac{\\delta\_{0}}{4}})),
$$

(5.44)

which implies

$$
\\lambda(t)=t\\lambda+O(t^{2-\\frac{\\delta\_{0}}{2}}),
$$

(5.45)

as _t →_ 0.

* * *

_Proof of Theorem 1.1._ We first assume that _g0_ is non-degenerate. Observe that the
refined approximate metric is close to the näıve approximate metric in the Cδ2,α weighted
0 _;t_
norm, for _t_ sufficiently small. From identical arguments as in \[10, Section 8\], for any
metric gE satisfying (1.15), then there exists a diffeomorphism ϕ : Mt → Mt so that
Bgt(gt − ϕ∗gE) = 0, and ϕ∗gE remains close to gt in the Cδ2,α weighted norm. The metric
0 _;t_
ϕ∗gE would then give a zero of the mapping Φt, but then (5.20) would then imply that
_λ_ = 0, a contradiction.

$$
g\_{0}
$$

$$
C\_{\\delta\_{0};t}^{2,\\alpha}
$$

$$
g\_{E}
$$

$$
\\varphi:M^{t}\\rightarrow M^{t}
$$

$$
B\_{g\_{t}}(g\_{t}-\\varphi^{\*}g\_{E})=0
$$

$$
\\varphi^{\*}g\_{E}
$$

$$
g\_{t}
$$

$$
C\_{\\delta\_{0};t}^{2,\\alpha}
$$

$$
\\varphi^{\*}g\_{E}
$$

$$
\\Phi\_{t},
$$

$$
\\lambda=0
$$

$$
g\_{0}
$$

If _g0_ is not non-degenerate, then there is a finite dimensional space of infinitesimal
Einstein deformations on ( _M0,g0),_ of dimension _k ≥_ 0\. The proof of Proposition 5.1 can
be modified to yield a mapping

$$
\\left(M\_{0},g\_{0}\\right)
$$

$$
k\\geq0
$$

$$
\\psi\_{t}:B\_{1}\\times(-\\epsilon,\\epsilon)\\rightarrow B\_{1}\\times(-\\epsilon,\\epsilon),
$$

(5.46)

where B1 is a small ball in Rk, whose zero set is in one-to-one correspondence with the
zeroes of Φgt(see also the argument in \[15, Section 11\]). An almost identical argument
as in the proof of Proposition 5.1 shows that the mapping _ψ_ admits an expansion

$$
B\_{1}
$$

$$
\\mathbb{R}^{k}
$$

$$
\\Phi\_{g\_{t}}
$$

$$
\\psi
$$

$$
\\psi\\big(a\_{1},\\ldots,a\_{k},v\\big)=\\big(\\psi\_{1},\\ldots,\\psi\_{k},t\\lambda+O\\big(t^{2-\\frac{\\delta\_{0}}{2}}\\big)\\big),
$$

(5.47)

as _t →_ 0, so the existence of an Einstein metric in the stated neighborhood still implies
that _λ_ = 0.

$$
t\\to0.
$$

$$
\\lambda=0
$$

* * *

# Analysis on asymptotically hyperbolic manifolds

The goal of this chapter is to study the asymptotic behavior of _L2_-solutions of some
elliptic operators on an AHE manifold (Mm,∂M,g,x). We consider the following operators:

$$
L^{2}-solution
$$

$$
\\left(M^{m},\\partial M,g,x\\right)
$$

1. P0 = ∆H − 2Ric, acting on functions,

$$
P\_{0}=\\Delta\_{H}-2Ric
$$

2. P1 = Bδ∗ = 1/2(∇∗∇− Ric) = 1/2(∆H − 2Ric), acting on 1-forms,

$$
P\_{1}=B\\delta^{ _}=\\frac{1}{2}(\\nabla^{_}\\nabla-Ric)=\\frac{1}{2}(\\Delta\_{H}-2Ric)
$$

3. P2 = ∆H − 2Ric, acting on 2-forms,

$$
P\_{2}=\\Delta\_{H}-2Ric
$$

◦
4\. P = 1/2∇∗∇− R, acting on traceless symmetric 2-tensors.

$$
P=\\frac{1}{2}\\nabla^\*\\nabla-\\overset{\\circ}{R},
$$

We also need the following decompositions, noting that we will only consider _C∞_ sections
of bundles, so notations of regularity will be suppressed.

$$
C^{\\infty}
$$

$$
\\Omega^{1}\\overline{{M}}\\big\|\_{\\partial M},
$$

∣
For Ω1M ∣, we have the decomposition
∂M

$$
\\left.\\Omega^{1}\\overline{{M}}\\right\| _{\\partial M}=\\left.\\Omega_{t}^{1}\\overline{{M}}\\right\| _{\\partial M}\\oplus\\left.\\Omega_{n}^{1}\\overline{{M}}\\right\|\_{\\partial M},
$$

(6.1)

* * *

where Ω1t (M) is the space of one-forms on M which vanish on normal vectors (with
respect to g) when restricted to the boundary and Ω1n(M) is the space one-forms on M
which vanish on tangential vectors when restricted to the boundary.

$$
\\Omega\_{t}^{1}(\\overline{M})
$$

$$
\\overline{M}
$$

$$
\\bar{g})
$$