---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Contents]

# Contents

> Source: https://www.math.uci.edu/~jviaclov/lecturenotes/PCMI_Lectures_Final.pdf
> Fetched: 2026-10-04 22:08
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
  "source": "exa",
  "source_url": "https://www.math.uci.edu/~jviaclov/lecturenotes/PCMI_Lectures_Final.pdf",
  "metadata": {
    "provenance_urls": [
      "https://www.math.uci.edu/~jviaclov/lecturenotes/PCMI_Lectures_Final.pdf"
    ],
    "search_origins": [
      {
        "source": "exa",
        "query": "second variation integral |Ric - lambda g|^2 at Einstein metric Lichnerowicz operator gauge fixing"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

##### Contents

Critical Metrics for Riemannian Curvature Functionals Jeff A. Viaclovsky 1

Critical Metrics for Riemannian Curvature Functionals 3 
Introduction 3 
Lecture 1. The Einstein-Hilbert functional 5 
1. Notation and conventions 5 
2. First variation 6 
3. Normalized functional 7 
4. Second variation 8 
5. Transverse-traceless variations 9 
Lecture 2. Conformal geometry 11 
1. Conformal variations 11 
2. Global conformal minimization 12 
3. Green’s function metric and mass 13 
4. The Yamabe Problem 14 
5. Generalizations of the Yamabe Problem 15 
Lecture 3. Diffeomorphisms and gauging 17 
1. Splitting 17 
2. Second variation as a bilinear form 18 
3. Ebin-Palais slice theorem (infinitesimal version) 19 
4. Saddle point structure and the smooth Yamabe invariant. 21 
Lecture 4. The moduli space of Einstein metrics 23 
1. Moduli space of Einstein metrics 23 
2. The nonlinear map 24 
3. Structure of nonlinear terms 25 
4. Existence of the Kuranishi map 26 
5. Rigidity of Einstein metrics 27 
Lecture 5. Quadratic curvature functionals 31 
1. Quadratic curvature functionals 31 
2. Curvature in dimension four 33 
3. Einstein metrics in dimension four 34 
4. Optimal metrics 35 
5. Anti-self-dual or self-dual metrics 36 
Lecture 6. Anti-self-dual metrics 39 

i

ii

1. Deformation theory of anti-self-dual metrics 39 
2. Weitzenb¨ock formulas 40 
3. Calabi-Yau metric on K3 surface 41 
4. Twistor methods 43 
5. Gluing theorems for anti-self-dual metrics 43 
Lecture 7. Rigidity

## Retrieved source content

## Contents

Critical Metrics for Riemannian Curvature Functionals

Jeff A. Viaclovsky

1

Critical Metrics for Riemannian Curvature Functionals 3

Introduction
Lecture 1. The Einstein-Hilbert functional

01. Notation and conventions
02. First variation
03. Normalized functional
04. Second variation
05. Transverse-traceless variations
    Lecture 2. Conformal geometry
06. Conformal variations
07. Global conformal minimization
08. Green’s function metric and mass
09. The Yamabe Problem
10. Generalizations of the Yamabe Problem
    Lecture 3. Diffeomorphisms and gauging
11. Splitting

3
5
5
6
7
8
9
11
11
12
13
14
15
17
17

2. Second variation as a bilinear form 18
3. Ebin-Palais slice theorem (infinitesimal version) 19
4. Saddle point structure and the smooth Yamabe invariant. 21

Lecture 4. The moduli space of Einstein metrics

01. Moduli space of Einstein metrics
02. The nonlinear map
03. Structure of nonlinear terms
04. Existence of the Kuranishi map
05. Rigidity of Einstein metrics
    Lecture 5. Quadratic curvature functionals
06. Quadratic curvature functionals
07. Curvature in dimension four
08. Einstein metrics in dimension four
09. Optimal metrics
10. Anti-self-dual or self-dual metrics
    Lecture 6. Anti-self-dual metrics

23
23
24
25
26
27
31
31
33
34
35
36
39

* * *

1. Deformation theory of anti-self-dual metrics
2. Weitzenb¨ock formulas
3. Calabi-Yau metric on K3 surface
4. Twistor methods
5. Gluing theorems for anti-self-dual metrics

39
40
41
43
43

Lecture 7. Rigidity and stability for quadratic functionals 45

01. Strict local minimization 45

02. Local description of the moduli space

03. Some rigidity results

04. Other dimensions
    Lecture 8. ALE metrics and orbifold limits

05. Ricci-flat ALE metrics

06. Non-collapsed limits of Einstein metrics

07. Bt-flat metrics

08. Non-collapsed limits of Bt-flat metrics
    Lecture 9. Regularity and volume growth

09. Local regularity

10. Volume growth estimate

11. ALE order and removable singularity theorems

12. Chen-LeBrun-Weber metric
    Lecture 10. A gluing theorem for Bt-flat metrics

13. Existence of critical metrics

14. Lyapunov-Schmidt reduction

15. The building blocks

16. Remarks on the proof
    Bibliography


47
49
50
51
51
53
55
57
59
59
60
61
63
65
65
66
67
68
71

* * *

# Critical Metrics for Riemannian Curvature Functionals

Jeff A. Viaclovsky

* * *

* * *

# Critical Metrics for Riemannian Curvature Functionals

Jeff A. Viaclovsky

### Introduction

The goal of these lectures is to gain an understanding of critical points of certain
Riemmannian functionals. The starting point will be the (normalized) Einstein-
Hilbert functional:
∫

$$
\\tilde{\\mathcal{E}}(g)=V o l(g)^{\\frac{2-n}{n}}\\int\_{M}R\_{g}d V\_{g},
$$

where Rg is the scalar curvature. The Euler-Lagrange equations of Ẽ(g) are

$$
R\_{g}
$$

$$
\\tilde{\\mathcal{E}}(g)
$$

(0.1)

$$
Ric(g)=\\lambda\\cdot g,
$$

where _Ric_ denotes the Ricci tensor, and _λ_ is a constant. A Riemannian manifold
_(M,g)_ satisfying (0.1) is called an _Einstein manifold._

$$
(M,g)
$$

In Lecture 1, we will study the first and second variation of the functional
Ẽ(g), and give an analysis of the Jacobi operator on transverse-traceless tensors.
In Lecture 2, we will study conformal variations, discuss the Lichnerowicz eigenvalue estimate and Obata’s Theorem, and give a survey of the Yamabe Problem.
In Lecture 3, we will introduce an important splitting of the space of symmetric
2-tensors into pure-trace directions, transverse-traceless directions, and “diffeomorphism” directions. An infinitesimal version of the Ebin-Palais slice theorem will
show that the diffeomorphism directions can be ignored. It will follow that critical
points of the Einstein-Hilbert functional are in general saddle points. This leads
one naturally to define the smooth Yamabe invariant of a manifold, or _σ_-constant.

$$
\\tilde{\\mathcal{E}}(g)
$$

Next, in Lecture 4, we will study the space of Einstein metrics modulo diffeomorphism, and use Fredholm theory to construct a map between finite-dimensional
spaces called the _Kuranishi map_ whose zero set is locally in one-to-one correspondence with the moduli space of Einstein metrics (locally). We will also discuss some
basic rigidity results for Einstein metrics.

The topic in Lecture 5 will be quadratic curvature functionals in dimension
four, that is linear combinations of the following quadratic curvature functionals:
∫ ∫ ∫

$$
\\mathcal{W}(g)=\\int\_{M}\|W\_{g}\|^{2}d V\_{g},\ \\rho(g)=\\int\_{M}\|R i c\_{g}\|^{2}d V\_{g},\ \\mathcal{S}(g)=\\int\_{M}R\_{g}^{2}d V\_{g}.
$$

Department of Mathematics, University of Wisconsin, Madison, WI 53706

E-mail address: [jeffv@math.wisc.edu](mailto:jeffv@math.wisc.edu)

The author would like to thank the organizers of this PCMI Program for the invitation to give
these lectures. Also, thanks are due to Michael T. Lock, who served as teaching assistant, and
who helped make many significant improvements to these lectures.

* * *

Einstein metrics are critical for these functionals, and we will give a discussion
of some known results about Einstein metrics. There are also many non-Einstein
critical metrics for various linear combinations of these functionals. There is a
special family of critical metrics for _W_ known as anti-self-dual metrics. In Lecture 6,
we will study the deformation theory of such metrics, and discuss local properties of
the moduli space and existence of the Kuranishi map. We will also discuss several
other interesting properties of anti-self-dual metrics.

In Lecture 7, we will discuss some rigidity and stability results regarding critical metrics for quadratic curvature functionals, which are joint work with Matt
Gursky. As mentioned above, critical points of the Einstein-Hilbert functional in
general have a saddle-point structure. However, critical points for certain quadratic functionals have a nicer local variational structure, see Theorem 7.1. Several
rigidity results will also be discussed (which will be crucial in the final lecture).

In Lecture 8, we will study a special class of metrics called asymptotically
locally Euclidean metrics (ALE), and present several hyperk¨ahler examples. We
will also discuss a result about non-collapsed limits of Einstein metrics: with certain
geometric assumptions, a subsequence will converge to an orbifold Einstein metric.
A natural question is whether one can reverse this process; that is, can one start with
an orbifold Einstein metric, use Ricci-flat ALE metrics to resolve the singularities,
and find an Einstein metric on the resolution? We will discuss a recent result of
Biquard in the asymptotically hyperbolic Einstein setting which says that this is
possible, provided that a certain obstruction vanishes.

We will next discuss a generalization of the Einstein condition, called Bt-flat
metrics, give several examples, and discuss an analogous orbifold convergence result
which is joint work with Gang Tian. In Lecture 9, we will present some of the key
points of the proof of this result, and also give a discussion an Einstein metric on
CP2#2CP2 found by Chen-LeBrun-Weber.

$$
B^{t}
$$

$$
\\mathbb{C}\\mathbb{P}^2#2\\overline{\\mathbb{C}\\mathbb{P}}^2
$$

Finally, in Lecture 10 we will discuss an existence theorem for critical metrics
on certain 4-manifolds which is joint work with Matt Gursky. The general idea is
to “glue” together two metrics which are critical for a functional to get an “approximate” critical metric, and then find conditions so that one can perturb to an
actual solution. Theorem 10.1 produces critical metrics for specific functionals on
2 2
the manifolds CP2#CP,CP2#2CP , and S2 × S2#S2 × S2.

$$
\\mathbb{C}\\mathbb{P}^{2}#\\overline{\\mathbb{C}\\mathbb{P}}^{2},\\mathbb{C}\\mathbb{P}^{2}#2\\overline{\\mathbb{C}\\mathbb{P}}^{2}
$$

$$
S^{2}\\times S^{2}#S^{2}\\times S^{2}
$$

This is an expanded version of lectures the author gave at the PCMI Program
in Geometric Analysis in Park City from July 16-19, 2013.

* * *

# The Einstein-Hilbert functional

### 1\. Notation and conventions

The notation ∇XY will denote the covariant derivative on a Riemannian manifold
(M,g). In a coordinate system {xi}, i = 1...n, the Christoffel symbols are defined
by

$$
\\nabla\_{X}Y
$$

$$
(M,g)
$$

$$
{x^{i}},i=1\\ldots n,
$$

(1.1)

$$
\\nabla\_{\\partial\_{i}}\\partial\_{j}=\\Gamma\_{i j}^{k}\\partial\_{k},
$$

where ∂i denotes the ith coordinate tangent vector field.
can be expressed in terms of the metric as

The Christoffel symbols

$$
\\partial\_{i}
$$

(1.2)

$$
\\Gamma\_{i j}^{k}=\\frac{1}{2}g^{k l}\\Big(\\partial\_{i}g\_{j l}+\\partial\_{j}g\_{i l}-\\partial\_{l}g\_{i j}\\Big).
$$

The curvature tensor as a (1,3)-tensor is given by

(1.3)

$$
R(X,Y)Z=\\overline{{\\nabla\_{X}\\nabla\_{Y}Z}}-\\overline{{\\nabla\_{Y}\\nabla\_{X}Z}}-\\overline{{\\nabla\_{\[X,Y\]}Z}},
$$

and in coordinates our convention is

(1.4)

$$
R(\\partial\_{i},\\partial\_{j})\\partial\_{k}=R\_{i j k}^{l}\\partial\_{l}.
$$

The curvature tensor as a (0,4)-tensor is given by
(

(1.5)

$$
\\overline{{R m}}(X,Y,Z,W)\\equiv-g\\big(R(X,Y)Z,W\\big),
$$

and in coordinates

(1.6)

$$
R\_{i j k l}=R m(\\partial\_{i},\\partial\_{j},\\partial\_{k},\\partial\_{l}).
$$

Note that our convention is

(1.7)

$$
R\_{i j l k}=R\_{i j k}^{\\quad m}g\_{m l}.
$$

That is, we lower the upper index to the _third_ position (warning: some authors to
lower this index to a different position). The components of the Ricci tensor are
given by

(1.8)

$$
R\_{i j}=R\_{l i j}^{l}=g^{l m}R\_{l i m j}=R\_{j i},
$$

and the scalar curvature is

(1.9)

$$
R=g^{pq}R\_{pq}=g^{pq}g^{lm}R\_{lpmq}.
$$

* * *

### 2\. First variation

We let _M_ denote the space of Riemannian metrics on a manifold _M_ :

(1.10)

$$
\\mathcal{M}={g\\in\\Gamma(S^{2}(T^{\*}M)),g\\mathrm{ispositivedefinite}},
$$

where Γ(S2(T ∗M)) denotes the space of smooth symmetric covariant 2-tensors on
_M._ The (unnormalized) Einstein-Hilbert functional _E_ : _M→_ R is defined by
∫

$$
\\Gamma(S^{2}(T^{\*}M))
$$

$$
\\mathcal{E}:\\mathcal{M}\\to
$$

(1.11)

$$
\\mathcal{E}(g)=\\int\_{M}R\_{g}d V\_{g}.
$$

This is a _Riemannian functional_ in the sense that it is invariant under diffeomorphisms:

(1.12)

$$
\\mathcal{E}(\\varphi^{\*}g)=\\mathcal{E}(g).
$$

Next, we compute the Euler-Lagrange equations of the unnormalized functional:

Proposition 1.1. _If M is closed and n ≥ 3, then a metric g ∈M is critical for E_
_if and only if g is Ricci-flat._

$$
n\\geq3
$$

$$
g\\in\\mathcal{M}
$$

$$
\\mathcal{E}
$$

Proof. Let g(t) be a variation, with h = g′(0). Then
∫

$$
h=g^{\\prime}(0)
$$

(1.13)

$$
\\begin{align\*}(\\mathcal{E}(g(t))'&=\\int\_{M}(R\_{g(t)}dV\_{g(t)})'\\&=\\int\_{M}R' _{g(t)}dV_{g(t)}+R\_{g(t)}(dV\_{g(t)})'.\\end{align\*}
$$

Recall the formula for the linearization of the scalar curvature
∣

(1.14)

$$
\\left.(R\_{g(t)})^{\\prime}\\right\| _{t=0}=-\\Delta(t r h)+\\delta^{2}h-R_{l p}h^{l p},
$$

where _δ2_ is the double-divergence operator defined in coordinates by

$$
\\delta^{2}
$$

$$
\\delta^{2}h=\\nabla^{i}\\nabla^{j}h\_{i j},
$$

(1.15)

and ∆ is the Laplacian on functions (note that we use the analysts’ Laplacian,
which has negative eigenvalues). We also recall the formula for the linearization of
the volume element
∣ 1

$$
\\Delta
$$

$$
(d V\_{g(t)})^{\\prime}\\big\| _{t=0}=\\frac{1}{2}t r_{g}(h)d V\_{g}.
$$

(1.16)

Next, we evaluate (1.13) at t = 0, and consider Eg′ as a mapping on symmetric
tensors. Substituting the formulas (1.14) and (1.16) into (1.13), and integrating by
parts, we obtain
∫ ()

$$
t=0,
$$

$$
\\mathcal{E}\_{g}^{\\prime}
$$

$$
\\begin{aligned}{\\mathcal{E} _{g}^{\\prime}(h)}&{{}=\\int_{M}\\Big(R^{\\prime}+\\frac{R}{2}t r\_{g}(h)\\Big)d V\_{g}}\ {}&{{}=\\int\_{M}\\Big(-\\Delta(t r h)+\\delta^{2}h-R^{l p}h\_{l p}+\\frac{R}{2}t r\_{g}(h)\\Big)d V\_{g}}\ {}&{{}=\\int\_{M}\\Big((-R^{l p}+\\frac{R}{2}g^{l p})h\_{l p}\\Big)d V\_{g}.}\ \\end{aligned}
$$

If this vanishes for all variations _h,_ then

$$
Ric=\\frac{R}{2}g.
$$

If _n_ \> 2, taking a trace, we find that _R_ = 0, so _(M,g)_ is Ricci-flat.

$$
n>2
$$

$$
R=0.
$$

* * *

Remark 1.2. If _n_ = 2 then _E_
surprising in view of the Gauss-Bonnet Theorem:
∫

has zero variation, thus is constant. This is not

$$
n=2
$$

(1.17)

$$
\\int\_{M^{2}}K\_{g}d V\_{g}=2\\pi\\chi(M^{2}),
$$

where Kg = Rg

_/2_ is the Gaussian curvature, and _χ_ denotes the Euler characteristic.

$$
K\_{g}=R\_{g}/2
$$

$$
\\chi
$$

Exercise 1.3.

(i) Prove (1.14). (Hint: first prove that (1.2) linearizes to
()

(1.18)

$$
(\\Gamma\_{i j}^{k})^{\\prime}=\\frac{1}{2}g^{k l}\\Big(\\nabla\_{i}h\_{j l}+\\nabla\_{j}h\_{i l}-\\nabla\_{l}h\_{i j}\\Big).
$$

Next, write out a formula for the scalar curvature in terms of Christoffel symbols,
and use (1.18). Note: these computations are much simpler if one works in a normal
coordinate system, since the Christoffel symbols vanish at the base point in normal
coordinates.)
√

(ii) Prove (1.16) using that the volume element is locally

dVg = det(gij) · dx.

$$
d V\_{g}=\\sqrt{\\det(g\_{i j})}\\cdot d x
$$

#### 2.1. Diffeomorphism invariance _⇒_ Bianchi identity

Define the divergence operator δ : Γ(S2(T ∗M))

→ Γ(T ∗M) by

$$
\\delta:\\Gamma(S^{2}(T^{ _}M))\\rightarrow\\Gamma(T^{_}M)
$$

(1.19)

$$
(\\delta h) _{j}=g^{p q}\\nabla_{p}h\_{q j}.
$$

The tensor that arises in the above calculation

(1.20)

$$
G=-R i c+\\frac{R}{2}g,
$$

is known as the Einstein tensor. By the contracted second Bianchi identity, it is
divergence-free. This is actually a consequence of diffeomorphism invariance of the
functional. To see this, let φt be a path of diffeomorphisms, and let gt = φ∗t g.
Then g′ = LX g, where X is the tangent vector field of this 1-parameter group of
diffeomorphisms at _t_ = 0, and _L_ is the Lie derivative operator. Integrating by
parts:
∫ ∫

$$
\\phi\_{t}
$$

$$
g\_{t}=\\phi\_{t}^{\*}g.
$$

$$
g^{\\prime}=\\mathcal{L}\_{X}g,
$$

$$
t=0
$$

$$
\\mathcal{L}
$$

$$
\\int\_{M}\\langle G,\\mathcal{L} _{X}g\\rangle d V_{g}=-\\int\_{M}\\langle2\\delta G,X\\rangle d V\_{g},
$$

for any vector field _X,_ which implies that _δG_ = 0\. Moreover, this argument shows
that if _F_ is _any_ Riemannian functional, then _δ∇F_ = 0.

$$
\\delta G=0
$$

$$
\\delta\\nabla\\mathcal{F}=0
$$

### 3\. Normalized functional

The functional _E_ is not scale-invariant for _n ≥_ 3\. To account for this, we define the
normalized Einstein-Hilbert functional by
∫

$$
n\\geq3
$$

$$
\\mathcal{E}
$$

(1.21)

$$
\\tilde{\\mathcal{E}}(g)=V o l(g)^{\\frac{2-n}{n}}\\int\_{M}R\_{g}d V\_{g}.
$$

Proposition 1.4. _A metric g is critical for Ẽ under all conformal variations (those_
_of the form h_ = _f · g for f_ : _M → R) if and only if g has constant scalar curvature._ _Furthermore, a metric g ∈M is critical for Ẽ if and only if g is Einstein, that is,_ _Ric(g_) = _λ · g for some constant λ ∈ R._

$$
\\tilde{\\mathcal{E}}
$$

$$
h=f\\cdot g
$$

$$
f:M\\to\\mathbb{R}\\big)i\_j
$$

$$
g\\in\\mathcal{M}
$$

$$
\\tilde{\\mathcal{E}}\ \\textit{if}
$$

$$
Ric(g)=\\lambda\\cdot g
$$

$$
\\lambda\\in\\mathbb{R}
$$

* * *

Proof. We compute

$$
\\begin{aligned}{\\tilde{\\mathcal{E}}^{\\prime}(h)}&{{}={V o l}(g)^{\\frac{2-n}{n}}\\Big(\\frac{2-n}{n}{V o l}(g)^{-1}\\int\_{M}\\frac{1}{2}(t r\_{g}h)d V\_{g}\\cdot\\int\_{M}R\_{g}d V\_{g}\\Big)}\ {}&{{}\\qquad+{V o l}(g)^{\\frac{2-n}{n}}\\int\_{M}\\Big(-R^{l p}+\\frac{R}{2}g^{l p}\\Big)h\_{l p}d V\_{g}.}\ \\end{aligned}
$$

If _g(t_) = _f_ (t)g, then

$$
g(t)=f(t)g
$$

$$
\\tilde{\\mathcal{E}}^{\\prime}(h)=\\frac{n-2}{2n}V o l(g)^{\\frac{2-n}{n}}\\Big(\\int\_{M}(t r\_{g}h)(R\_{g}-\\overline{{R}})d V\_{g}\\Big),
$$

where _R_ denotes the average scalar curvature. If this is zero for an arbitrary function
trgh, then Rg must be constant. The full variation then simplifies to
∫ ()

$$
\\overline{R}
$$

$$
tr\_{g}h
$$

$$
R\_{g}
$$

(1.22)

$$
\\tilde{\\mathcal{E}}^{\\prime}(h)=V o l(g)^{\\frac{2-n}{n}}\\int\_{M}\\Big(-R^{l p}+\\frac{R}{n}g^{l p}\\Big)h\_{l p}d V\_{g}.
$$

If this vanishes for all variations, then the traceless Ricci tensor must vanish, so
_(M,g)_ is Einstein.

$$
(M,g)
$$

### 4\. Second variation

Since the functional is scale invariant, from now on we will always restrict to variations satisfying
∫

(1.23)

$$
\\int\_{M}t r\_{g}(h)d V\_{g}=0.
$$

Proposition 1.5. _Let g be Einstein with Ric(g_) = _λ · g. Then the second derivative_
_of Ẽ at t_ = 0 _is given by_
{ ∫ ∫}

$$
Ric(g)=\\lambda\\cdot g
$$

$$
\\tilde{\\mathcal{E}}
$$

$$
t=0
$$

(1.24)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}=V o l(g)^{\\frac{2-n}{n}}\\Big{\\frac{2-n}{2}\\lambda\\int\_{M}\|h\|^{2}d V\_{g}+\\int\_{M}\\langle G^{\\prime}(h),h\\rangle d V\_{g}\\Big}.
$$

Proof. The proof is left as an exercise. An important point is that the second
derivative of a functional is well-defined at a critical point (it only depends on the
tangent to the variation).

Exercise 1.6.

Prove the formula for the linearization of the Ricci tensor,
(

(1.25)

$$
\\begin{aligned}{({R i c}^{\\prime}) _{i j}=\\frac{1}{2}\\Big(}&{{}-\\Delta h_{i j}+\\nabla\_{i}(\\delta h) _{j}+\\nabla_{j}(\\delta h) _{i}-\\nabla_{i}\\nabla\_{j}(t r\_{g}h)}\ {}&{{}-2R\_{i l j p}h^{l p}+R\_{i}^{p}h\_{j p}+R\_{j}^{p}h\_{i p}\\Big),}\ \\end{aligned}
$$

where ∆ : Γ(S2

(T ∗M)) → Γ(S2(T ∗M)) is the rough Laplacian defined by

$$
\\Delta:\\Gamma(S^{2}(T^{ _}M))\\rightarrow\\Gamma(S^{2}(T^{_}M))
$$

(1.26)

$$
(\\Delta h) _{i j}=g^{p q}\\nabla_{p}\\nabla\_{q}h\_{i j}.
$$

(Hint: write out a formula for the Ricci tensor in terms of Christoffel symbols, and
use (1.18). Use normal coordinates to simplify the computation.)

Next, letting

(1.27)

$$
(Rm\*h) _{ij}=R_{iljp}h^{lp}
$$

equation (1.24) can be rewritten as follows.

* * *

Proposition 1.7. _Let g be Einstein with Ric(g_) = _λ · g. Then the second derivative_
_of Ẽ at t_ = 0 _is given by_
∫

$$
Ric(g)=\\lambda\\cdot g
$$

$$
\\tilde{\\mathcal{E}}
$$

$$
t=0
$$

(1.28)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}=V o l(g)^{\\frac{2-n}{n}}\\int\_{M}\\langle h,J h\\rangle d V\_{g},
$$

where J : Γ(S2(T ∗M)) → Γ(S

2(T ∗M)) is the operator

$$
J:\\Gamma(S^{2}(T^{ _}M))\\rightarrow\\Gamma(S^{2}(T^{_}M))
$$

(1.29)

$$
J h=\\frac{1}{2}\\Delta h-\\frac{1}{2}\\mathcal{L}(\\delta h)+(\\delta^{2}h)g-\\frac{1}{2}(\\Delta t r\_{g}h)g-\\frac{\\lambda}{2}(t r\_{g}h)g+R m\*h.
$$

### 5\. Transverse-traceless variations

We next have the following definition.

Definition 1.8. _A symmetric_ 2- _tensor h is called transverse-traceless (TT for_
short) if δgh = 0 and trg(h) = 0.

$$
\\delta\_{g}h=0
$$

$$
tr\_{g}(h)=0
$$

The second variation formula simplifies considerably for TT variations:

Proposition 1.9. _If h is transverse-traceless, then_
∫

(1.30)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}=V o l(g)^{\\frac{2-n}{n}}\\Big{\\int\_{M}\\Big\\langle h,\\frac{1}{2}\\Delta h+R m\*h\\Big\\rangle d V\_{g}\\Big}.
$$

The first term is manifestly negative, which shows that critical metrics for _Ẽ_
always have a saddle point structure. In other words, modulo a finite dimensional
space, _Ẽ_ is locally strictly _maximizing_ in TT directions.

$$
\\tilde{\\mathcal{E}}
$$

$$
\\tilde{\\mathcal{E}}
$$

#### 5.1. The case of constant curvature

If _(M,g)_ has constant sectional curvature, then

(1.31)

$$
R\_{i j k l}=k\_{0}\\left(g\_{i k}g\_{j l}-g\_{j k}g\_{i l}\\right).
$$

The above second variation formula for TT tensors simplifies to
∫

(1.32)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}=V o l(g)^{\\frac{2-n}{n}}\\Big{\\int\_{M}\\Big\\langle h,\\frac{1}{2}\\Delta h-k\_{o}h\\Big\\rangle d V\_{g}\\Big}.
$$

This immediately yields:

Corollary 1.10. Let (Mn,g) have constant sectional curvature k0. If k0 \> 0 and
_n_ \> _2, then the second variation is strictly negative when restricted to transversetraceless variations. If k0_ = _0, then the second variation is strictly negative except_
_for parallel h._

$$
\\left(M^{n},g\\right)
$$

$$
n>2
$$

$$
\\text{"}k\_{0}>0\\text{"}
$$

$$
k\_{0}=0
$$

For _n_ = 2, as pointed out above, we know that _Ẽ_ is constant; thus our computation shows that if h is TT then h is identically zero on S2, and h must be
parallel on T 2. The parallel sections in the case k0 = 0 correspond to deformations
of the flat structure, this will be discussed in more detail in Lecture 4 (also see
Exercise 4.16 below).

$$
\\tilde{\\mathcal{E}}
$$

$$
n=2
$$

$$
S^{2}
$$

$$
T^{2}
$$

$$
k\_{0}=0
$$

* * *

#### 5.2. Hyperbolic manifolds

In the hyperbolic case, we have

Lemma 1.11. If (Mn,g) is compact and hyperbolic, then the smallest eigenvalue
_of the rough Laplacian on TT tensors is at least n._

$$
\\textit{If}\\left(M^{n},g\\right)
$$

Proof. Exercise. Hint: start with the inequality
∫

(1.33)

$$
\\int\_{M}\|\\nabla\_{i}h\_{j k}-\\nabla\_{j}h\_{i k}\|^{2}d V\_{g}\\geq0,
$$

integrate by parts, commute covariant derivatives, etc.

This immediately yields

Corollary 1.12. If (Mn _maximizing in TT directions._

_,g_)

_is hyperbolic and n_ \> _2, then Ẽ is locally strictly_

$$
\\left(M^{n},g\\right)
$$

$$
n;>;2,
$$

$$
\\tilde{\\mathcal{E}}
$$

(1.34)

Define the operator _d_

∇
: Γ(S02(T ∗

M)) → Γ(Λ2 ⊗ T ∗M) by

$$
d^{\\nabla}:\\Gamma(S\_{0}^{2}(T^{ _}M))\\to\\Gamma(\\Lambda^{2}\\otimes T^{_}M){~}{\\operatorname{by}}
$$

$$
(\\boldsymbol{d}^{\\nabla}\\boldsymbol{h}) _{i j k}=\\nabla_{i}h\_{j k}-\\nabla\_{j}h\_{i k},
$$

which is called the _Codazzi_ operator. From the proof of Lemma 1.11, the eigentensors corresponding to the least eigenvalue of the rough Laplacian are exactly
the Codazzi tensor, that is, _d∇ h_ = 0\. These yield kernel elements of the second
variation when _n_ = 2, this will be examined in more detail below in Lecture 4.

$$
d^{\\nabla}h=0
$$

$$
n=2
$$

#### 5.3. The case of _S2 × S2_

$$
S^{2}\\times S^{2}
$$

A nice example with saddle-point structure in the TT-directions is given by the
product metric on S2 × S2. Let πi: S2 × S2 → S2 denote the projection onto the
ith factor for i = 1,2. The product metric is g = g1 \+ g2 where gi = πi∗gS2, and
gS2 is the round metric on S2 of constant Gaussian curvature equal to 1.

$$
S^{2}\\times S^{2}
$$

$$
\\pi\_{i}:S^{2}\\times S^{2}\\rightarrow S^{2}
$$

$$
i=1,2
$$

$$
g=g\_{1}+g\_{2}
$$

$$
g\_{i}=\\pi\_{i}^{\*}g\_{S^{2}}
$$

$$
S^{2}
$$

Proposition 1.13. On S2×S2 with the product metric g1+g2, the lowest eigenvalue
of the operator 1/2 ∆h +Rm ∗ h on TT tensors is −1. The corresponding eigenspace
_is_ 1- _dimensional, and is spanned by h_ = _g1 − g2. The next largest eigenvalue is 1._

$$
S^{2}{\\times}S^{2}
$$

$$
g\_{1}+g\_{2}
$$

$$
\\frac{1}{2}\\Delta h+R m\*h
$$

$$
h=g\_{1}-g\_{2}
$$

Proof. This is left as an exercise, with the following hint: decompose a traceless symmetric 2-tensor as
◦f◦f

(1.35)

$$
h=\\overset{\\circ}{h\_{1}}+\\frac{f}{m}g\_{1}+\\hat{h}+\\overset{\\circ}{h\_{2}}-\\frac{f}{m}g\_{2},
$$

◦
where hi is the pull-back of a tensor from the ith factor, hi is its trace-free part,
for _i_ = 1,2, and _ĥ_ are the mixed directions. Since the curvature tensor is given by

$$
h\_{i}
$$

$$
\\overset{\\circ}{h\_{i}}
$$

(1.36)

$$
R\_{i j k l}=(g\_{1}) _{i k}(g_{1}) _{j l}-(g_{1}) _{j k}(g_{1}) _{i l}+(g_{2}) _{i k}(g_{2}) _{j l}-(g_{2}) _{j k}(g_{2})\_{i l},
$$

the eigenvalue equation reduces to three separate equations on the pieces in the
decomposition (1.35), which can be analyzed separately. For more details, see for
example \[GV15, Proposition 7.9\].

Exercise 1.14. (i) Find a constant scalar curvature deformation of the product
metric corresponding to _h_ = _g1 − g2,_ and which increases the functional _Ẽ._

$$
h=g\_{1}-g\_{2}
$$

$$
\\tilde{\\mathcal{E}}
$$

(ii) Show that α1 α2 ( = symmetric product), where αi are 1-forms dual to
Killing fields are eigentensors with eigenvalue 1.

$$
\\alpha\_{1}\\odot\\alpha\_{2}(\\odot=
\\alpha\_{i}
$$

* * *

# Conformal geometry

### 1\. Conformal variations

We will next look at _conformal variations,_ that is, those variations of the form
_h_ = _f · g,_ for a function _f_ : _M →_ R.

$$
\\mathit{h}=f\\cdot g,
$$

$$
f:M\\to\\mathbb{R}
$$

Proposition 2.1. _Assume that g has constant scalar curvature, and let h_ = _fg_
∫
with fdVg = 0\. Then
M
{ ∫ ()}

$$
h=f g
$$

$$
\\begin{array}{l}\\int\_{M}f d V\_{g}=0\\end{array}
$$

(2.1)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}=V o l(g)^{\\frac{2-n}{n}}\\frac{2-n}{2}\\Big{\\int\_{M}\\Big((n-1)\\Delta f+R\_{g}f\\Big)f d V\_{g}\\Big}.
$$

Proof. Assuming _g_ is Einstein, this follows from the above formulas, but it is
easy to verify that this holds more generally for constant scalar curvature metrics,
the calculation is left as an exercise.

Let (Sn,gS) denote the unit n-sphere with round metric gS. Note that the
Ricci tensor satisfies Ric(gS) = (n − 1)gS. An immediate corollary is the following

$$
\\left(S^{n},g\_{S}\\right)
$$

$$
g\_{S}
$$

$$
Ric(g\_S)=(n-1)g\_S
$$

Corollary 2.2. Let g have constant scalar curvature. If Rg ≤ 0, then Ẽ is locally
strictly minimizing in the conformal direction. If Rg \> 0 and Ric ≥ (n − 1)g, then
the same is true, unless g is isometric to (Sn,gS).

$$
R\_{g}\\leq0
$$

$$
\\tilde{\\mathcal{E}}
$$

$$
R\_{g}>0
$$

$$
Ric\\geq(n-1)g
$$

$$
\\left(S^{n},g\_{S}\\right)
$$

The case Rg ≤ 0 is obvious and the case Rg \> 0 will follow from a result due
to Lichnerowicz which we will discuss next. Let _λ1_ denote the lowest non-trivial
eigenvalue of the Laplacian on functions, that is _∆u_ = _−λ1u._ We have the following
eigenvalue estimate which was proved by Lichnerowicz in 1958 in \[Lic58\], and for
which the equality case was characterized by Obata in 1962 \[Oba62\]:

$$
R\_{g}>0
$$

$$
R\_{g}\\leq0
$$

$$
\\lambda\_{1}
$$

$$
\\Delta u=-\\lambda\_{1}u
$$

Theorem 2.3 (Lichnerowicz-Obata). If a compact manifold (Mn

_,g_) _satisfies_

(2.2)

$$
\\left(M^{n},g\\right)
$$

$$
Ric\\geq(n-1)\\cdot g,
$$

then λ1 ≥ n, with equality if and only if (Mn,g) is isometric to (Sn,gS).

$$
\\lambda\_{1}\\geq n
$$

$$
\\textit{if}\\left(M^{n},g\\right)
$$

$$
\\left(S^{n},g\_{S}\\right)
$$

Proof. We only give an outline of the proof.
derivatives, write
∫ ∫

First, commuting covariant
∫

$$
\\int\_{M}(\\Delta f)^{2}d V\_{g}=\\int\_{M}\|\\nabla^{2}f\|^{2}d V\_{g}+\\int\_{M}R i c(\\nabla f,\\nabla f)d V\_{g},
$$

(2.3)

and then use the matrix inequality \|A\|2 ≥ (1/n)(tr(A))2. If λ1 = n, then equality
in this inequality implies that there is a non-trivial solution of the equation
∆f

$$
\|A\|^{2}\\geq(1/n)(tr(A))^{2}
$$

$$
\\lambda\_{1}=n
$$

(2.4)

$$
\\nabla^{2}f=\\frac{\\Delta f}{n}g=-f\\cdot g.
$$

This implies that along any unit-speed geodesic,

(2.5)

$$
f(s)=A\\cos(s)+B\\sin(s),
$$ where s is the arc-length from a fixed point P+. If we choose the point P+ to be
a maximum of f, then f (s) = Acos(s) along any geodesic through P+. One then
uses this information to construct an isometry with (Sn,gS). For more details, see
\[Oba62\] and also \[K¨uh88\] for an excellent exposition.

$$
P\_{+}
$$

$$
P\_{+}
$$

$$
f,
$$

$$
f(s)=A\\cos(s)
$$

$$
P\_{+}
$$

$$
\\left(S^{n},g\_{S}\\right)
$$

#### 1.1. Conformal variations on Sn

$$
S^{n}
$$

On (Sn,gS), eigenfunctions corresponding to the eigenvalue n yield directions with
Ẽ′′ = 0\. There is a nice geometric explanation for this fact:

$$
\\left(S^{n},g\_{S}\\right)
$$

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}=0
$$

Proposition 2.4. Let φt be a
of gS. Then

1- _parameter group of conformal automorphisms_

$$
\\phi\_{t}
$$

$$
\\frac{d}{d t}(\\phi\_{t}^{\*}g\_{S})\|\_{t=0}=f g,
$$

(2.6)

_where f is an eigenfunction satisfying ∆f_ = _−nf._

$$
\\Delta f=-nf.
$$

Proof. We leave this as an exercise, with the following hint: use the Hodge
decomposition to write any 1-form _α_ dual to a conformal vector field as _α_ = _df_ \+ _ω,_
with _ω_ divergence free. Apply the conformal Killing operator to _α_ and use the
resulting equation to show that the trace-free Hessian of _f_ vanishes, and that _ω_ is
Killing.

$$
\\alpha=d f+\\omega,
$$

$$
\\omega
$$

### 2\. Global conformal minimization

Actually, it turns out that something much stronger is true for Einstein metrics:

Theorem 2.5. An Einstein metric (Mn,g) is the unique global minimizer of Ẽ in
its conformal class (up to scaling), unless (M,g) is isometric to (Sn,gS). In this
case, any critical point is the pull-back of gS under a conformal diffeomorphism.

$$
\\left(M^{n},g\\right)
$$

$$
\\tilde{\\mathcal{E}}
$$

$$
(M,g)
$$

$$
\\left(S^{n},g\_{S}\\right)
$$

This will be proved below. The first key point in the proof is the following
theorem of Obata:

Theorem 2.6 (\[Oba72\]). If (Mn,g) is Einstein, then g is the unique constant
_scalar curvature metric in its conformal class (up to scaling), unless (M,g) is iso-_
metric to (Sn,gS), in which case all critical points are the pull-back of gS under a
_conformal diffeomorphism._

$$
\\textit{If}\\left(M^{n},g\\right)
$$

$$
(M,g)
$$

$$
\\left(S^{n},g\_{S}\\right)
$$

Proof. To prove this, assume that _ĝ_ is a constant scalar curvature metric
which is conformal to _g._ Letting _E_ denote the traceless Ricci tensor, we recall the
transformation formula: if g = φ−2ĝ, then
()

$$
\\hat{g}
$$

$$
g.
$$

(2.7)

$$
g=\\phi^{-2}\\hat{g}
$$

$$
E\_{g}=E\_{\\hat{g}}+(n-2)\\phi^{-1}\\left(\\nabla^{2}\\phi-(\\Delta\\phi/n)\\hat{g}\\right),
$$

where _n_ is the dimension, and the covariant derivatives are taken with respect to
_ĝ._ Since _g_ is Einstein, we have

$$
\\hat{g}.
$$

$$
g
$$

(2.8)

$$
E\_{\\hat{g}}=(2-n)\\phi^{-1}\\big(\\nabla^{2}\\phi-\\frac{1}{n}(\\Delta\\phi)\\hat{g}\\big).
$$

* * *

Integrating,
∫

$$
\\begin{aligned}{\\int\_{M}\\phi\|E\_{\\hat{g}}\|^{2}d V\_{\\hat{g}}}&{{}=(2-n)\\int\_{M}\\phi E\_{\\hat{g}}^{i j}\\left{\\phi^{-1}\\big(\\nabla^{2}\\phi-\\frac{1}{n}(\\Delta\\phi)\\hat{g}\\big) _{i j}\\right}d V_{\\hat{g}}}\ {}&{{}=(2-n)\\int\_{M}E\_{\\hat{g}}^{i j}\\nabla^{2}\\phi\_{i j}d V\_{\\hat{g}}}\ {}&{{}=(n-2)\\int\_{M}(\\nabla\_{j}E\_{\\hat{g}}^{i j}\\cdot\\nabla\_{i}\\phi)d V\_{\\hat{g}}=0,}\ \\end{aligned}
$$

by the Bianchi identity. Consequently, _ĝ_ is also Einstein. If _ĝ_ is not a constant
multiple of _g,_ then _(M,g)_ admits a nonconstant solution of the equation

$$
\\hat{g}
$$

$$
\\hat{g}
$$

$$
g,
$$

$$
(M,g)
$$

$$
\\nabla^{2}\\phi=\\frac{\\Delta\\phi}{n}g.
$$

(2.9)

Taking a divergence of this equation, it follows that _φ_ \+ _c,_ where _c_ is a constant,
is an eigenfunction of the Laplacian with eigenvalue _n,_ so _(M,g)_ is isometric to
(Sn,gS) by the same argument in Theorem 2.3 given above.

$$
\\phi+c,
$$

$$
c
$$

$$
n,
$$

$$
\\left(S^{n},g\_{S}\\right)
$$

$$
(M,g)
$$

We will next take a slight detour and discuss the Yamabe Problem, before
returning to the proof of Theorem 2.5.

### 3\. Green’s function metric and mass

A key idea in the final resolution of the Yamabe Problem is the following construction of an asymptotically flat metric, called the Green’s function metric. First, we
define an asymptotically flat metric:

Definition 2.7. A complete Riemannian manifold (Xn,g) is called asymptotically
flat or AF of order τ if there exists a diffeomorphism ψ : X \ K → (Rn \ B(0,R))
where _K_ is a compact subset of _X,_ and such that under this identification,

$$
\\left(X^{n},g\\right)
$$

$$
\\tau
$$

$$
\\psi:X\\setminus K\\to(\\mathbb{R}^n\\setminus B(0,R))
$$

$$
X
$$

(2.10)

$$
\\begin{aligned}{(\\psi\_{ _}g){i j}}&{{}=\\delta{i j}+O(\\rho^{-\\tau}),}\ {\\partial^{\|k\|}(\\psi\_{_}g)\_{i j}}&{{}=O(\\rho^{-\\tau-k}),}\ \\end{aligned}
$$

(2.11)

for any partial derivative of order _k,_ as _r →∞,_ where _ρ_ is the distance to some
fixed basepoint.

$$
k,
$$

$$
r\\to\\infty
$$

$$
\\rho
$$

The conformal Laplacian is the operator:

(2.12)

$$
\\Box u=-4\\frac{n-1}{n-2}\\Delta u+R u.
$$

If _(M,g)_ is compact and _R_ \> 0, then for any _p ∈ M,_ there is a unique positive
solution to the equation

$$
(M,g)
$$

$$
R>0,
$$

$$
p\\in M
$$

(2.13)

$$
\\square G=0on M\\setminus{p}
$$

$$
G=\\rho^{2-n}(1+o(1))
$$

as _ρ →_ 0, where _ρ_ is geodesic distance to the basepoint _p._ This function _G_ is called
the _Green’s function for the conformal Laplacian._

$$
\\rho\\to0,
$$

$$
\\rho
$$

$$
p.
$$

4
Exercise 2.8. Show that if ˜g = u n−2

_g,_ then

$$
\\tilde{g}=u^{\\frac{4}{n-2}}g,
$$

(2.14)

$$
\\Box\_{g}u=R\_{\\tilde{g}}u^{\\frac{n+2}{n-2}}.
$$

* * *

4
Denote N = M {p} with metric gN = G n−2 gM. From Exercise 2.8, gN is
scalar-flat. From a more careful expansion of the Green’s function, it is possible to
show that gN is also asymptotically flat, but we omit the proof.

$$
N=M\\setminus{p}
$$

$$
g\_{N}=G^{\\frac{4}{n-2}}g\_{M}
$$

$$
g\_{N}
$$

The mass of an AF space is defined by
∫
∑

(2.15)

$$
\\mathrm{mass}(g\_{N})=\\lim\_{R\\rightarrow\\infty}\\frac{1}{\\omega\_{n-1}}\\int\_{S(R)}\\sum\_{i,j}(\\partial\_{i}g\_{i j}-\\partial\_{j}g\_{i i})(\\partial\_{i}\\lrcorner d V\_{g}),
$$

where ωn−1 = Vol(Sn−1), and S(R) denotes the sphere of radius R. It was shown
in \[Bar86\] that if _τ_ \> ( _n −_ 2)/2, then this mass is well-defined, that is, it is independent of the coordinate system chosen around infinity. The mass is consequently
a geometric invariant of an AF metric, and plays an important rˆole in the final
resolution of the Yamabe Problem, which we discuss next.

$$
\\omega\_{n-1}=Vol(S^{n-1})
$$

$$
S(R)
$$

$$
\\tau>(n-2)/2
$$

### 4\. The Yamabe Problem

By Ḧolder’s inequality, the functional _Ẽ_ is bounded from below when restricted to
any fixed conformal class. It is then natural to minimize in the conformal direction:

$$
\\tilde{\\mathcal{E}}
$$

$$
Y(M,\[g\])=\\inf\_{\\tilde{g}\\in\[g\]}\\tilde{\\mathcal{E}}(\\tilde{g}).
$$

(2.16)

This is called the _conformal Yamabe invariant._

Theorem 2.9. If (Mn,g) is compact, then there exists a conformal metric g˜ ∈ \[g\]
_which has constant scalar curvature, and which minimizes Ẽ in its conformal class._

$$
\\textit{If}\\left(M^{n},g\\right)
$$

$$
\\tilde{g}\\in\[g\]
$$

$$
\\tilde{\\mathcal{E}}
$$

Outline of Proof. For any conformal class, Aubin showed that

(2.17)

$$
Y(M,\[g\])\\leq\\tilde{\\mathcal{E}}(g\_{S}).
$$

The idea of the proof of this estimate is to choose a conformal factor which is
spherical in an-neighborhood of a point, and zero everywhere else (this is called
a “bubble”). Expanding the Yamabe energy of this test function in the parameter
then yields a leading term which is exactly the Yamabe energy of the spherical
metric.

Next, one shows that if this inequality is strict, then a solution exists. This step
is now considered “trivial” by experts, but in fact this took a long time to figure
out. Yamabe’s original paper \[Yam60\] contains a serious mistake on this point,
this was fixed by Trudinger \[Tru68\], and then optimized by Aubin \[Aub76\].

The more difficult step is to show that if (M,\[g\]) is not conformally diffeomorphic to (Sn, \[gS\]) then the inequality (2.17) is strict. In case n ≥ 6 and g is not
locally conformally flat, this was proved by Aubin \[Aub76, Aub98\] by basing the
above test function at a point where the Weyl tensor does not vanish. The locally
conformally flat case was proved by Schoen-Yau \[SY88\] using ideas involving the
developing map. The case _n ≤_ 6 was proved by Schoen \[Sch84\]. The main idea
is the following. Instead of making the above test function be zero away from the
bubble, Schoen’s idea was to instead choose the conformal factor to be the Green’s
function for the conformal Laplacian away from the bubble. The mass of the associated asympotically flat metric arises as the next term in the expansion of the
Yamabe energy of this test function, so the result follows from the positive mass
theorem of Schoen-Yau \[SY79, SY81, Sch89\].

$$
\\left(M,\\left\[g\\right\]\\right)
$$

$$
\\left(S^{n},\\left\[g\_{S}\\right\]\\right)
$$

$$
n\\geq6
$$

$$
n\\leq6
$$

We next return to the global minimization statement in Theorem 2.5:

* * *

Proof of Theorem 2.5. The uniqueness follows from Theorem 2.6. For the
minimization statement, of course, we know a minimizer exists from the resolution
of the Yamabe problem, but there is an “easy” proof in the Einstein case. In the
negative or zero scalar curvature case, one can apply a standard argument from
the calculus of variations to show that a minimizing sequence converges. In the
positive case, scale so that _Ric_ = ( _n −_ 1)g. Then

$$
Ric=(n-1)g
$$

(2.18)

$$
\\tilde{\\mathcal{E}}(g)=n(n-1)V o l(g)^{2/n}.
$$

By Bishops’ volume comparison theorem, Vol(M,g) ≤ Vol(Sn,gS) with equality if
and only if g is isometric to gS. So if g is not isometric to gS, we have

$$
Vol(M,g)\\leq Vol(S^n,g\_S)
$$

$$
g
$$

$$
g\_{S}
$$

(2.19)

$$
g\_{S}
$$

$$
Y(M,\[g\])=\\inf\_{\\tilde{g}\\in\[g\]}\\tilde{\\mathcal{E}}(g)<\\tilde{\\mathcal{E}}(g\_{S}).
$$

As discussed above, this estimate implies that a minimizing sequence converges (no
bubbles are possible).

Finally, the case of (Sn,gS) takes some extra work. One needs to suitably renormalize a minimizing sequence using the conformal group to obtain a minimizing
sequence which converges, see \[LP87, Proposition 4.6\] for an argument due to
Karen Uhlenbeck.

$$
\\left(S^{n},g\_{S}\\right)
$$

Remark 2.10. An important question is if the set of unit volume constant scalar
curvature metrics in a conformal class is compact if the manifold is not conformally diffeomorphic to the sphere. This is true in dimensions _n ≤_ 24 \[KMS09\].
Surprisingly, it is false in higher dimensions \[Bre08, BM09\].

$$
n\\leq24
$$

### 5\. Generalizations of the Yamabe Problem

We mention that there are many other Yamabe-type conformal deformation problems which also have variational characterizations. We describe one such example
next. Define the _Schouten tensor_ by
()

(2.20)

$$
A\_{g}=\\frac{1}{n-2}\\left(Ric\_{g}-\\frac{R\_{g}}{2(n-1)}g\\right).
$$

Consider the functional

(2.21)

$$
\\tilde{\\mathcal{F}} _{\\sigma_{2}}(g)=V o l(g)^{\\frac{4}{n}-1}\\int\_{M}\\sigma\_{2}(g^{-1}A\_{g})d V\_{g},
$$

where _σ2_ denotes the second elementary symmetric function of the eigenvalues.
This functional has a nice conformal variational property, analogous to that for the
Einstein-Hilbert functional.

$$
\\sigma\_{2}
$$

Theorem 2.11 (\[Via00\]). If n 6= 4, a metric g is a critical for F˜σ2 under all
_conformal variations if and only if_

$$
If n\\neq4
$$

(2.22)

$$
\\textit{if}
$$

$$
\\tilde{\\mathcal{F}} _{\\sigma_{2}}
$$

$$
\\sigma\_{2}(g^{-1}A\_{g})=C,
$$

_for some constant C._

$$
C
$$

One may also generalize the Yamabe problem by asking if it is possible to conformally deform a metric so that (2.22) is satisfied. Note that, in contrast to the
Yamabe equation which is semi-linear, equation (2.22) is a fully nonlinear equation,
and some assumption must be made on the conformal structure to ensure that the equation is elliptic. There has been much progress on this _σ2_ problem, see for example \[CGY02a, CGY02b, GW06, GV03, STW07\]. More generally, one can
consider other symmetric functions of the eigenvalues, and for the kth elementary
function, this is known as the σk-Yamabe Problem. The locally conformally flat
case has been solved for all _k,_ see \[GW03, LL03\]. This has also been solved for
the case _k > n/2,_ see \[GV07\]. There have been many other related works involving
various symmetric functions of the eigenvalues, we refer the reader to \[Via06\] for
a more detailed description and other references.

$$
\\sigma\_{2}
$$

$$
\\sigma\_{k}-
$$

$$
k,
$$

$$
k>n/2
$$

For solving conformal deformation problems, we note that parabolic methods
also play an important rˆole, see for example \[Bre05, Bre07, GW03, STW07\].
Another generalization of the Yamabe Problem is to the class of higher order equations, and deals with prescribing _Q_-curvature, which is a higher order generalization of the scalar curvature. We will not discuss this further, and refer the reader
to \[BG08, DM08\] for details about the notion of _Q_-curvature.

The Yamabe Problem can also be generalized to the setting of orbifolds \[AB03,\
AB04, Aku12\]. This turns out to be more subtle than the Yamabe Problem on
manifolds – there in fact exist conformal classes on compact orbifolds which do
not contain any constant scalar curvature metrics. For example, the conformal
compactifications of hyperk¨ahler ALE metrics and also the conformal classes of
certain Bochner-K¨ahler metrics on weighted projective spaces do not admit any
solution of the orbifold Yamabe Problem \[Via10, Via13a\].

* * *

# Diffeomorphisms and gauging

### 1\. Splitting

We begin by discussing a decomposition of the space of symmetric 2-tensors; some
references for this material are \[BE69, Bes08\]. We let K : T ∗M→S02(T ∗M) be
the conformal Killing operator

$$
\\mathcal{K}:T^{ _}M\\rightarrow S\_{0}^{2}(T^{_}M)
$$

(3.1)

$$
(\\mathcal{K}\\alpha) _{i j}=\\nabla_{i}\\alpha\_{j}+\\nabla\_{j}\\alpha\_{i}-\\frac{2}{n}(\\delta\\alpha)g\_{i j}.
$$

Also, consider the operator : Γ(T ∗M) → Γ(T ∗M), defined by = δK where
δ : Γ(S2(T ∗M)) → Γ(T ∗M) is the divergence defined by

$$
\\square:\\Gamma(T^{ _}M)\\to\\Gamma(T^{_}M)
$$

$$
\\square=\\delta\\mathcal{K}
$$

$$
\\delta:\\Gamma(S^{2}(T^{ _}M))\\rightarrow\\Gamma(T^{_}M)
$$

(3.2)

$$
(\\delta h) _{j}=g^{p q}\\nabla_{p}h\_{i q}.
$$

Exercise 3.1.

(i) Show that the operator is elliptic and self-adjoint.

$$
\\square
$$

(ii) Prove that the kernel of
they satisfy _Kα_

is exactly the space of conformal Killing forms, i.e.,
= 0.

$$
\\mathcal{K}\\alpha=0
$$

Lemma 3.2.
_decomposition:_

_The space of symmetric_ 2- _tensors admits the following orthogonal_

(3.3)

$$
S^{2}(T^{\*}M)={f\\cdot g}\\oplus{\\mathcal{K}(\\alpha)}\\oplus{\\delta h=0,t r\_{g}(h)=0}.
$$

Proof. Given h ∈ S02(T ∗M), consider the 1-form δh. By Fredholm theory,
the equation _α_ = _δh_ has a solution if and only if _δh_ is orthogonal to the kernel
of the adjoint operator, which is exactly the space of conformal Killing 1-forms (by
the exercise). If _κ_ is any conformal Killing 1-form, then
∫ ∫

$$
h\\in S\_{0}^{2}(T^{\*}M)
$$

$$
\\delta h
$$

$$
\\Box\\alpha=\\delta h
$$

$$
\\int\_{M}\\langle\\delta h,\\kappa\\rangle=\\frac{1}{2}\\int\_{M}\\langle h,\\mathcal{K}\\kappa\\rangle=0.
$$

So the equation _α_ = _δh_ has a solution, which proves that _h −Kα_ is divergencefree.

$$
\\Box\\alpha=\\delta h
$$

$$
h-\\mathcal{K}\\alpha
$$

#### 1.1. Another decomposition

The orthogonal decomposition given in (3.3) implies the decomposition

(3.4)

$$
S^{2}(T^{\*}M)={f\\cdot g}+{\\mathcal{L}(\\alpha)}\\oplus{\\delta h=0,t r\_{g}(h)=0}.
$$

Proposition 3.3. _If (M,g) is Einstein, with Ric_ = _λ · g, then this latter decompo-_
sition is a direct sum, unless (M,g) is isometric to (Sn,gS).

$$
R i c=\\lambda\\cdot g
$$

$$
\\textit{If}\\left(M,g\\right)
$$

$$
(M,g)
$$

$$
\\left(S^{n},g\_{S}\\right)
$$

Proof. We need to show that the spaces _{f · g}_ and _{L(α)}_ have intersection
_{0}._ So if _L(α_) = _f · g,_ then taking a trace, we have

$$
{f\\cdot g}
$$

$$
{\\mathcal{L}(\\alpha)}
$$

$$
\\mathcal{L}(\\alpha)=f\\cdot g.
$$

$$
2\\delta\\alpha=nf,
$$

* * *

$$
\\mathcal{K}(\\alpha)=0
$$

which implies that _K(α_) = 0\. Taking a divergence of this equation, we have

$$
\\begin{aligned}{\\nabla\_{i}(\\nabla\_{i}\\alpha\_{j}+\\nabla\_{j}\\alpha\_{i}-(2/n)(\\delta\\alpha)g\_{i j})}&{{}=\\Delta\\alpha\_{j}+\\nabla\_{i}\\nabla\_{j}\\alpha\_{i}-(2/n)\\nabla\_{j}(\\delta\\alpha)}\ {}&{{}=\\Delta\\alpha\_{j}+\\left(1-\\frac{2}{n}\\right)\\nabla\_{j}(\\delta\\alpha)+\\lambda\\alpha\_{j}.}\ \\end{aligned}
$$

Next, recall the Bochner formula for 1-forms

(3.5)

$$
(\\Delta\\alpha) _{i}=-(\\Delta_{H}\\alpha) _{i}+R_{i p}g^{p j}\\alpha\_{j},
$$

where ∆H is the Hodge Laplacian. This yields that

$$
\\Delta\_{H}
$$

$$
\\Delta\\alpha=-\\left(d\\delta\_{H}+\\delta\_{H}d\\right)\\alpha+\\lambda\\alpha,
$$

where δH is the Hodge divergence (which is the negative of our divergence). Putting
these together, we obtain
()

$$
\\delta\_{H}
$$

(3.6)

$$
\\Box\\alpha=-2\\left(\\frac{n-1}{n}\\right)d\\delta\_{H}\\alpha-\\delta\_{H}d\\alpha+2\\lambda\\alpha=0.
$$

Next, pairing (3.6) with _α_ and integrating,
() ∫ ∫

$$
-2\\left(\\frac{n-1}{n}\\right)\\int\_{M}\|\\delta\\alpha\|^{2}d V\_{g}-\\int\_{M}\|d\\alpha\|^{2}d V\_{g}+2\\lambda\\int\_{M}\|\\alpha\|^{2}d V\_{g}=0.
$$

This implies that _α_ = 0 if _λ_ < 0 (so any conformal Killing field vanishes for a
negative Einstein metric). If _λ_ = 0, we see that _δα_ = 0 and _dα_ = 0\. In particular,
_α_ is a Killing 1-form, and we are done.

$$
\\alpha=0if\\lambda<0
$$

$$
\\lambda=0
$$

$$
\\delta\\alpha=0
$$

In the case _λ_ \> 0, applying a divergence to (3.6) yields
()

$$
\\lambda>0
$$

(3.7)

$$
2\\left(\\frac{n-1}{n}\\right)\\Delta(\\delta\\alpha)+2\\lambda(\\delta\\alpha)=0.
$$

By Lichnerowicz’ Theorem, this implies that _δα_ = 0 unless _(M,g)_ is isometric to
(Sn,gS), so α is Killing.

$$
\\left(S^{n},g\_{S}\\right)
$$

### 2\. Second variation as a bilinear form

From Proposition 1.5, let us recall the second variation is
∫

(3.8)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}(h,h)=V o l(g)^{\\frac{2-n}{n}}\\int\_{M}\\langle h,J h\\rangle d V\_{g},
$$

where _J_ is the operator

$$
Jh=\\frac{2-n}{2}\\lambda h+G'h.
$$

(3.9)

Using polarization, the Hessian of _Ẽ_ is the bilinear form given by
∫

(3.10)

$$
\\tilde{\\mathcal{E}}
$$

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}(h\_{1},h\_{2})=V o l(g)^{\\frac{2-n}{n}}\\int\_{M}\\langle h\_{1},J h\_{2}\\rangle d V\_{g}.
$$

Proposition 3.4. _The decomposition_

(3.11)

$$
S^{2}(T^{\*}M)={f\\cdot g}\\oplus{\\mathcal{L}(\\alpha)}\\oplus{\\delta h=0,t r\_{g}(h)=0}
$$

is orthogonal with respect to Ẽ′′(·, ·).

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}(\\cdot,\\cdot)
$$

* * *

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}(\\mathcal{L}(\\alpha),\\cdot)=0
$$

Proof. First, Ẽ′′(L(α), ·)=0 from diffeomorphism invariance. So we just
need to check that

) = 0(3.12)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}(f\\cdot g,z)=0
$$

if _z_ is TT. To see this,

$$
\\begin{align\*}\\tilde{\\mathcal{E}}^{\\prime\\prime}(f\\cdot g,z)&=Vol(g)^{\\frac{2-n}{n}}\\int\_{M}\\langle f\\cdot g,Jz\\rangle dV\_g\\&=Vol(g)^{\\frac{2-n}{n}}\\int\_{M}\\langle f\\cdot g,\\frac{1}{2}\\Delta z+Rm _z\\rangle dV\_g\\&=Vol(g)^{\\frac{2-n}{n}}\\int\_{M}f(R\_{ijip}z\_{jp})dV\_g=0.\\end{align_}
$$

To summarize: if _h_ is any symmetric 2-tensor, then decompose _h_ as

$$
h
$$

$$
h
$$

(3.13)

$$
h=f\\cdot g+\\mathcal{L}\\alpha+z,
$$

where _z_ is TT. Then

$$
z
$$

(3.14)

$$
\\tilde{\\mathcal{E}}^{\\prime\\prime}(h,h)=\\tilde{\\mathcal{E}}^{\\prime\\prime}(f\\cdot g,f\\cdot g)+\\tilde{\\mathcal{E}}^{\\prime\\prime}(z,z).
$$

So we have shown that to check the second variation, we really only need to consider
conformal variations and TT variations separately.

### 3\. Ebin-Palais slice theorem (infinitesimal version)

The above discussion was at the level of the “tangent space to the space of Riemannian metrics at g”. We will next transfer this statement directly to the space
of Riemannian metrics near _g_ modulo diffeomorphism.

$$
g
$$

Theorem 3.5. _The local behavior of Ẽ, when considered as a map on M/D (the_
_space of Riemannian metrics modulo diffeomorphism), is determined by the conformal and TT directions (to second order)._

$$
\\mathcal{M}/\\mathcal{D}
$$

$$
\\tilde{\\mathcal{E}}
$$

The main tool for this is the following infinitesimal version of a “slice” theorem
due to Ebin-Palais. The notation Ck,α will denote the space of Ḧolder continuous
mappings (or tensors) with 0 < _α_ < 1.

$$
C^{k,\\alpha}
$$

$$
0<\\alpha<1
$$

‘
Theorem 3.6. For each metric g1 in a sufficiently small C +1,α-neighborhood of g
‘
(‘ ≥ 1), there is a C +2,α-diffeomorphism ϕ : M→M such that
˜

$$
g\_{1}
$$

$$
C^{\\ell+1,\\alpha}\\operatorname{-}\\mathit{neighborho}
$$

$$
(\\ell\\geq1)
$$

$$
C^{\\ell+2,\\alpha}
$$

(3.15)

$$
\\varphi:M\\rightarrow M
$$

$$
\\tilde{\\theta}\\equiv\\varphi^{\*}g\_{1}-g
$$

_satisfies_

(3.16)

$$
\\delta\_{g}\\Big(\\tilde{\\theta}-\\frac{1}{n}t r\_{g}(\\tilde{\\theta})g\\Big)=0.
$$

Proof. Let {ω1,...,ωκ} denote a basis of the space of conformal Killing forms
with respect to _g._ Consider the map

$$
{\\omega\_{1},\\ldots,\\omega\_{\\kappa}}
$$

)(3.17)

$$
\\mathcal{N}:C^{\\ell+2,\\alpha}(T M)\\asymp\\mathbb{R}^{\\kappa}\\asymp C^{\\ell+1,\\alpha}(S^{2}(T^{ _}M))\\to C^{\\ell,\\alpha}(T^{_}M)
$$

given by

(3.18)

$$
\\mathcal{N}(X,v,\\theta)=\\mathcal{N} _{\\theta}(X,v)=\\big(\\delta_{g}\\big\[\\overbrace{\\varphi\_{X,1}^{\*}(g+\\theta)}^{\\circ}\\big\]+\\sum\_{i}v\_{i}\\omega\_{i}\\big),
$$ where ϕX,1 denotes the diffeomorphism obtained by following the flow generated
by the vector field _X_ for unit time, and _◦_ denotes the traceless part with respect
to _g._ Linearizing in _(X,v)_ at _(X,v,θ)_ = (0,0,0), we find

$$
\\varphi\_{X,1}
$$

$$
(X,v,\\theta)=(\\bar{0},0,0)
$$

$$
\\begin{aligned}{\\mathcal{N} _{0}^{\\prime}(Y,a)}&{{}=\\frac{d}{d\\epsilon}\\big(\\delta_{g}\\big\[\\overbrace{\\varphi\_{\\epsilon Y,1}^{\*}(g)}^{\\circ}\\big\]+\\sum\_{i}(\\epsilon a\_{i})\\omega\_{i}\\big)\\Big\| _{\\epsilon=0}}\ {}&{{}=\\big(\\delta_{g}\[\\overbrace{\\mathcal{L} _{g}Y^{\\flat}}^{\\circ}\]+\\sum_{i}a\_{i}\\omega\_{i}\\big)}\ {}&{{}=\\big(\\square Y^{\\flat}+\\sum\_{i}a\_{i}\\omega\_{i}\\big),}\ \\end{aligned}
$$

where Y \[is the dual one-form to Y. The adjoint map (N0′)∗: Cm+2,α(T ∗M) →\
Cm,α(TM) × Rκ is given by\
( ∫)\
\
$$\
Y^{\\flat}\
$$\
\
$$\
(\\mathcal{N}\_{0}^{\\prime})^{ _}:C^{m+2,\\alpha}(T^{_}M)\\rightarrow\
$$\
\
$$\
C^{m,\\alpha}(T M)\\times\\mathbb{R}^{\\kappa}\
$$\
\
(3.19)\
\
$$\
(\\mathcal{N} _{0}^{\\prime})^{\*}(\\eta)=\\Big((\\square\\eta)^{\\sharp},\\int_{M}\\langle\\eta,\\omega\_{i}\\rangle d V\_{g}\\Big),\
$$\
\
where ( η)\] is the vector field dual to η.

$$
(\\square\\eta)^{\\sharp}
$$

If _η_ is in the kernel of the adjoint, the first equation implies that _η_ is a conformal
Killing form, while the second implies that _η_ is orthogonal (in _L2_) to the space of
conformal Killing forms. It follows that η = 0, so the map N0′ is surjective.

$$
\\eta
$$

$$
L^{2})
$$

$$
\\eta=0
$$

$$
\\mathcal{N}\_{0}^{\\prime}
$$

Omitting a few technical details for simplicity, applying an infinite-dimensional
version of the implicit function theorem (which will be discussed in detail below in
‘
Lecture 4), given θ1 ∈ C +1,α(S2(T ∗M)) small enough we can solve the equation
‘
Nθ1 = 0; i.e., there is a vector field X∈C +2,α(TM), and a v ∈ Rκ, such that

$$
\\theta\_{1}\\in C^{\\ell+1,\\alpha}(S^{2}(T^{\*}M))
$$

$$
\\mathcal{N} _{\\theta_{1}}=0;i.e
$$

$$
X\\in C^{\\ell+2,\\alpha}(T M)
$$

$$
\\mathrm {a} v \\in \\mathbb {R} ^ {\\kappa}
$$

(3.20)

$$
\\delta\_{g}\[\\overbrace{\\varphi^{\*}g\_{1}}^{\\circ}\]+\\sum\_{i}v\_{i}\\omega\_{i}=0,
$$

where ϕ = ϕX,1. Letting θ˜ = ϕ∗g1 − g, then

_θ˜_ satisfies

$$
\\varphi=\\varphi\_{X,1}
$$

$$
\\tilde{\\theta}=\\varphi^{\*}g\_{1}-g
$$

$$
\\tilde{\\theta}
$$

(3.21)

$$
\\delta\_{g}\[\\stackrel{\\circ}{\\tilde{\\theta}}\]+\\sum\_{i}v\_{i}\\omega\_{i}=0,
$$

Pairing with ωj, for j = 1...κ, and integrating by parts, we see that vj = 0, and
we are done.

$$
\\omega\_{j}
$$

$$
j=1\\ldots\\kappa,
$$

$$
v\_{j}=0,
$$

Exercise 3.7. Verify the above formula (3.19) for (

N0′)∗.

$$
(\\mathcal{N}\_{0}^{\\prime})^{\*}
$$

Exercise 3.8. By adding a scaling factor to the map
to show that we can find a constant _c_ (depending upon

_N,_ modify the above argument
_g1),_ and find

$$
\\mathcal{N}
$$

(3.22)

$$
g\_{1})
$$

$$
\\tilde{\\theta}\\equiv e^{c}\\varphi^{\*}g\_{1}-g,
$$

so that in addition to the traceless part of _θ˜_ being TT, _θ˜_ also satisfies
∫

$$
\\tilde{\\theta}
$$

$$
\\mathrm {T T}, \\tilde {\\theta}
$$

$$
\\int\_{M}t r\_{g}\\tilde{\\theta}d V\_{g}=0.
$$

That is, we can also “gauge away” the scale-invariance of the functional. Equivalently, we can look at a slice of unit-volume metrics modulo diffeomorphism.

* * *

Remark 3.9. The reason this is called an “infinitesimal” version of the Slice Theorem is because the full Ebin-Palais Slice Theorem constructs a local slice for the
action of the diffeomorphism group, see \[Ebi68\]. The main difficulty is that the natural action of the diffeomorphism group on the space of Riemannian metrics is not
differentiable as a mapping of Banach spaces (with say Sobolev or Ḧolder norms).
It is however differentiable as a mapping of ILH spaces, see \[Omo70, Koi78\].
For the purposes of these lectures, we will content ourselves with the infinitesimal
version, and will not go into details about the full slice theorem

Proof of Theorem 3.5. Combining the above discussions, given any _g1_ sufficiently near _g,_ we can write
˜

$$
g\_{1}
$$

$$
g,
$$

(3.23)

$$
\\varphi^{\*}g\_{1}=g+\\tilde{\\theta},
$$

∫
with θ˜ = f · g + z with fdVg
M

= 0, and _z_ is TT. Then

$$
\\tilde{\\theta}=f\\cdot g+z\\mathrm{with}\\int\_{M}f dV\_{g}=0
$$

$$
\\begin{aligned}{\\tilde{\\mathcal{E}}(g\_{1})}&{{}=\\tilde{\\mathcal{E}}(\\varphi^{\*}g\_{1}){ ~~(f r o m~~ d i f f e o m o r p h i s m~i n v a r i a n c e)}}\ {}&{{}=\\tilde{\\mathcal{E}}(g+\\tilde{\\theta})}\ {}&{{}=\\tilde{\\mathcal{E}}(g)+\\tilde{\\mathcal{E}} _{g}^{\\prime}(\\tilde{\\theta})+\\tilde{\\mathcal{E}}_{g}^{\\prime\\prime}(f\\cdot g+z,f\\cdot g+z)+\\operatorname{remainder}}\ {}&{{}=\\tilde{\\mathcal{E}}(g)+\\tilde{\\mathcal{E}} _{g}^{\\prime\\prime}(f\\cdot g,f\\cdot g)+\\tilde{\\mathcal{E}}_{g}^{\\prime\\prime}(z,z)+\\operatorname{remainder}.}\ \\end{aligned}
$$

### 4\. Saddle point structure and the smooth Yamabe invariant.

We have seen that the functional _Ẽ_ is minimizing in the conformal directions, but
maximizing (modulo a finite-dimensional subspace) in the TT directions. So an
Einstein metric is always a saddle point for _E._ This suggests defining the following
min-max type invariant.

$$
\\tilde{\\mathcal{E}}
$$

First, we minimize in the conformal direction:

$$
Y(M,\[g\])=\\inf\_{\\tilde{g}\\in\[g\]}\\tilde{\\mathcal{E}}(g).
$$

This is called the _conformal Yamabe invariant._

The min-max invariant is then defined by

$$
Y(M)=\\sup\_{g\\in\\mathcal{M}}Y(M,\[g\]),
$$

which we will call the _smooth Yamabe invariant_ of _M,_ also known as the _σ-invariant_
of _M._ This was defined independently by Osamu Kobayashi \[Kob87\] and Richard
Schoen \[Sch89\].

#### 4.1. Some known cases

We will not focus on smooth Yamabe invariants in this lecture, but only list a few
known cases:

$$
\\bullet Y(S^{n})=Y(S^{n},\[g\_{S}\])=n(n-1){V o l}(S^{n})^{\\frac{2}{n}}.
$$

• Y (S1 × Sn−1) = Y (Sn, \[gS\]), proved by Schoen \[Sch89\].

$$
Y(S^{1}\\times S^{n-1})=Y(S^{n},\[g\_S\])
$$

• Y (RP3) = Y (RP3, \[gS\]), proved by Bray-Neves \[BN04\].

$$
Y(\\mathbb{R}\\mathbb{P}^3)=Y(\\mathbb{R}\\mathbb{P}^3,\[g\_S\])
$$

• If (M3,gH) is compact hyperbolic, then Y (M3) = Y (M3, \[gH\]). This
follows from Perelman’s work, see \[AIL07\].

$$
\\left(M^{3},g\_{H}\\right)
$$

$$
Y(M^{3})=Y(M^{3},\[g\_{H}\])
$$

* * *

_√_
• Y (CP2) = Y (CP2, \[gFS\]) = 12π 2, where gFS is the Fubini-Study metric,
proved by LeBrun \[LeB97\], see also \[GL98\].

$$
\\bullet Y(\\mathbb{C}\\mathbb{P}^2)=Y(\\mathbb{C}\\mathbb{P}^2,\[g\_{FS}\])=12\\pi\\sqrt{2},
$$

$$
g\_{FS}
$$

$$
\\mathrm{\[LeB97\]}
$$

There are many other cases for which the Yamabe invariant is known, but we do
not list them here. We note that an effective tool in dimension four is Seiberg-
Witten Theory, see \[LeB99, Sun09\]. Also, there are also many known estimates
on Yamabe invariants (see for example \[ADH13, Pet00\]), but there is not a single
known example of a compact manifold _M_ with positive Yamabe invariant which
has been shown to satisfy 0 < Y (M) < Y (Sn) in dimensions n ≥ 5.

$$
0<Y(M)<Y(S^n)
$$

$$
n\\geq5
$$

#### 4.2. Some unknown cases

It is a very difficult problem to determine Yamabe invariants in general. Here are
a few prominent unknown cases:

• What is Y (Sn/Γ), where Sn/Γ is a spherical space form with \|Γ\| > 1? Is
it achieved by the round metric? The only known case is the Bray-Neves
result listed above.

$$
Y(S^n/\\Gamma)
$$

$$
\\bar{S}^{n}/\\Gamma
$$

$$
\|\\Gamma\|>1?
$$

_•_ What is _Y_ (CP2#CP2)? The only result known is due to O. Kobayashi
\[Kob87\]:

$$
Y(\\mathbb{C P}^{2}#\\mathbb{C P}^{2})?
$$

$$
Y(\\mathbb{C}\\mathbb{P}^2#\\mathbb{C}\\mathbb{P}^2)\\geq Y(\\mathbb{C}\\mathbb{P}^2).
$$

_•_ What is _Y_ (CP2#CP )? Again, the only result known is2
2

$$
Y(\\mathbb{C P}^{2}#\\overline{{\\mathbb{C P}}}^{2})?
$$

$$
Y(\\mathbb{C}\\mathbb{P}^2#\\overline{\\mathbb{C}\\mathbb{P}}^2)\\geq Y(\\mathbb{C}\\mathbb{P}^2).
$$

• What is Y (S2 × S2)? The only known result is that
22

$$
Y(S^{2}\\times S^{2})?
$$

$$
Y(S^{2}\\times S^{2})>Y(S^{2}\\times S^{2},g\_{S^{2}}+g\_{S^{2}})
$$

(strict inequality). This follows from Exercise 1.14 and a result of B¨ohm-
Wang-Ziller that CSC metrics sufficiently near an Einstein metric are also
Yamabe minimizers in their conformal class \[BWZ04, Theorem C\].

We end by noting there are relatively few theorems giving conditions for the uniqueness of a Yamabe metric. There is Obata’s Theorem 2.6, and the result of \[BWZ04\]
mentioned above; also see \[dLPZ12\] and \[Kat94\].

* * *

# The moduli space of Einstein metrics

### 1\. Moduli space of Einstein metrics

Next, given an Einstein metric _g_ with _Ric(g_) = _λ · g,_ we would like understand the
space of solutions of the equation

$$
Ric(g)=\\lambda\\cdot g,
$$

(4.1)

$$
Ric(\\tilde{g})=\\lambda\\cdot\\tilde{g}
$$

$$
\\tilde{g}
$$

with ˜g near g. This will be infinite-dimensional since ϕ∗g will also be a solution
for any diffeomorphism _ϕ_ : _M→M._ Therefore, we need to look at the space of
Einstein metrics modulo diffeomorphism. Our goal is to prove:

$$
g.
$$

$$
\\varphi^{\*}g
$$

$$
\\varphi:M\\rightarrow M
$$

Theorem 4.1. _Assume g is Einstein with Ric(g_) = _λ · g and λ_ < _0\. Then the space_
_of Einstein metrics near g modulo diffeomorphism is locally isomorphic to the zero_
_set of a map_

$$
Ric(g)=\\lambda\\cdot g
$$

$$
\\lambda<0
$$

(4.2)

$$
\\Psi:H\_{E}^{1}\\to H\_{E}^{1},
$$

_where_

(4.3)

$$
H\_{E}^{1}={h\\in S^{2}(T^{ _}M):\\delta\_{g}h=0,t r\_{g}h=0,\\Delta h+2R m_ h=0},
$$

_where Rm ∗ h is the operator defined above in_ (1.27).

$$
Rm\*h
$$

Elements in the space _HE1_ are called _infinitesimal Einstein deformations._

$$
H\_{E}^{1}
$$

#### 1.1. Ellipticity

The diffeomorphism invariance also means that the above equation cannot be elliptic. Indeed, differentiating

))(4.4)

$$
Ric(\\varphi\_{t}^{ _}g)=\\varphi\_{t}^{_}(Ric(g))
$$

yields

(4.5)

$$
R i c^{\\prime}(\\mathcal{L} _{X}g)=\\mathcal{L}_{X}(R i c(g))=\\lambda\\cdot\\mathcal{L}\_{X}g.
$$

Exercise 4.2. Show that this implies that the symbol of Ric′ is not elliptic.

$$
Ric'
$$

We will next describe a procedure called “gauging” which shows in effect, that
the diffeomorphism directions are the only obstruction to ellipticity. This is somewhat analogous to the “Coulomb gauge” in electrodynamics.

#### 1.2. A gauge choice

Recall from above, that at an Einstein metric satisfying _Ric(g_) = _λ·g,_ the linearized
Ricci tensor is given by

$$
Ric(g)=\\lambda\\cdot g
$$

(4.6)

$$
(R i c^{\\prime}) _{i j}=\\frac{1}{2}\\Big(-\\Delta h_{i j}+\\nabla\_{i}(\\delta h) _{j}+\\nabla_{j}(\\delta h) _{i}-\\nabla_{i}\\nabla\_{j}(t r h)-2R\_{i l j p}h^{l p}+2\\lambda h\_{i j}\\Big).
$$

* * *

Define the operator

$$
\\beta\_{g}h=\\delta\_{g}h-\\frac{1}{2}d(t r\_{g}h).
$$

(4.7)

Exercise 4.3. _Show that_ 1

(4.8)

$$
\\frac{1}{2}\\mathcal{L}\\beta\_{g}h=\\frac{1}{2}\\Big(\\nabla\_{i}(\\delta h) _{j}+\\nabla_{j}(\\delta h) _{i}-\\nabla_{i}\\nabla\_{j}({t r}h)\\Big).
$$

Combining the above expressions,
(
1 1

(4.9)

$$
(R i c^{\\prime}-\\frac{1}{2}\\mathcal{L}\\beta\_{g})h=\\frac{1}{2}\\Big(-\\Delta h-2R m\*h+2\\lambda h\\Big).
$$

### 2\. The nonlinear map

Given θ ∈ C2,α(S2T ∗M), consider the map

$$
\\theta\\in C^{2,\\alpha}(S^{2}T^{\*}M)
$$

))(4.10)

$$
P\_{g}:C^{2,\\alpha}(S^{2}(T^{ _}M))\\rightarrow C^{0,\\alpha}(S^{2}(T^{_}M))
$$

defined by

(4.11)

$$
P\_{g}(\\theta)={R i c}(g+\\theta)-\\lambda\\cdot(g+\\theta)-\\frac{1}{2}\\mathcal{L} _{g+\\theta}\\beta_{g}\\theta.
$$

Proposition 4.4.

The operator Pg

_is elliptic._

$$
P\_{g}
$$

Proof. This is immediate: from the above, the linearized operator at _θ_ = 0 is
()
1

$$
\\theta=0
$$

(4.12)

$$
P\_{g}^{\\prime}h=\\frac{1}{2}\\Big(-\\Delta h-2R m\*h\\Big),
$$

which is clearly elliptic.

We next see that zeroes of Pg are in fact Einstein metrics.

$$
P\_{g}
$$

Proposition 4.5. Assume that λ < 0. If θ ∈ C3,α is sufficiently near g and
∞
satisfies Pg(θ) = 0, then Ric(g + θ) = λ(g + θ), and θ ∈ C.

$$
\\lambda<0
$$

$$
\\theta;\\in;C^{3,\\alpha}
$$

$$
P\_{g}(\\theta)=0
$$

$$
Ric(g+\\theta)=\\lambda(g+\\theta)
$$

$$
\\theta\\in C^{\\infty}
$$

Proof. Apply the operator βg+θ to the equation Pg(θ) = 0 to obtain

$$
\\beta\_{g+\\theta}
$$

$$
P\_{g}(\\theta)=0
$$

= 0(4.13)

$$
\\beta\_{g+\\theta}\\mathcal{L} _{g+\\theta}\\beta_{g}\\theta=0
$$

A computation shows that this is equivalently (exercise):

(4.14)

$$
\\left(\\Delta\_{g+\\theta}+R i c(g+\\theta)\\right)\\left(\\beta\_{g}\\theta\\right)=0.
$$

Since θ is sufficiently small in C2,α norm, and Ric(g) is strictly negative definite,
then Ricg+θ is also strictly negative definite. Pairing with βgθ and integrating by
parts then shows that βgθ = 0.

$$
\\theta
$$

$$
C^{2,\\alpha}
$$

$$
Ric(g)
$$

$$
Ric\_{g+\\theta}
$$

$$
\\beta\_{g}\\theta
$$

$$
\\beta\_{g}\\theta=0
$$

Exercise 4.6. Prove the regularity statement in Proposition 4.5. (Hint: Letting
_g˜_ = _g_ \+ _θ,_ in harmonic coordinates, the Ricci tensor can be written in the form
1

$$
\\tilde{g}=g+\\theta
$$

)(4.15)

$$
{R i c} _{k l}(\\tilde{g})=-\\frac{1}{2}\\tilde{g}^{i j}\\partial_{i j}^{2}\\tilde{g} _{k l}+Q_{k l}(\\partial\\tilde{g},\\tilde{g})
$$

where Q(∂g,˜ g˜) is an expression that is quadratic in _∂g˜,_ polynomial in _˜g_ and has
√
_\|g˜\|_ in its denominator. Use a bootstrap argument in these coordinates. )

$$
Q\\big(\\partial\\tilde{g},\\tilde{g}\\big)
$$

$$
\\partial\\tilde{g},
$$

$$
\\tilde{g}
$$

$$
\\sqrt{\\left\|\\tilde{g}\\right\|}
$$

Exercise 4.7. Show that we only need to assume that θ ∈ C2,α. (Hint: instead of
differentiating in the first step, integrate by parts.)

$$
\\theta\\in C^{2,\\alpha}
$$

Next, we have a converse up to diffeomorphism: Einstein metrics near to _g_ can
be gauged to yield zeroes of Pg.

$$
P\_{g}
$$

* * *

Proposition 4.8. _If g˜ is an Einstein metric near g with Einstein constant λ, then_
there exists a diffeomorphism ϕ : M→M such that θ˜ = ϕ∗g˜− g satisfies Pg(θ˜) = 0.

$$
\\lambda,
$$

$$
\\varphi:M\\rightarrow M
$$

$$
\\tilde{\\theta}=\\varphi^{\*}\\tilde{g}-g
$$

$$
P\_{g}(\\tilde{\\theta})=0
$$

The proof uses a modified (infinitesimal) Ebin-Palais slice theorem using the
Bianchi gauge:

‘
Lemma 4.9. For each metric g1 in a sufficiently small C +1,α-neighborhood of g
‘
(‘ ≥ 1), there is a C +2,α-diffeomorphism ϕ : M→M such that
˜

$$
g\_{1}
$$

$$
C^{\\ell+1,\\alpha}\\operatorname{-\\mathit{neighborhol}}
$$

$$
C^{\\ell+2,\\alpha}
$$

$$
(\\ell\\geq1)
$$

$$
\\varphi:M\\rightarrow M
$$

(4.16)

$$
\\tilde{\\theta}\\equiv\\varphi^{\*}g\_{1}-g
$$

_satisfies_

) = 0(4.17)

$$
\\beta\_{g}(\\tilde{\\theta})=0
$$

Proof. The proof is almost identical to that of Theorem 3.6, and is omitted.

Proof of Proposition 4.8.

If ˜g is Einstein then ϕ∗g˜ is also Einstein. Since

$$
\\tilde{g}
$$

$$
\\varphi^{\*}\\tilde{g}
$$

(4.18)

$$
\\beta\_{g}\\left(\\tilde{\\theta}\\right)=\\beta\_{g}\\left(\\varphi^{\*}\\tilde{g}-g\\right)=0,
$$

we obviously obtain a zero of _P_

g.

$$
P\_{g}
$$

### 3\. Structure of nonlinear terms

Let us write

(4.19)

$$
P\_{g}(\\theta)=P\_{g}(0)+P\_{g}^{\\prime}(\\theta)+Q\_{g}(\\theta).
$$

The following proposition is crucial, and shows that the nonlinear term is manageable.

Proposition 4.10.

_For θ1,θ2 sufficiently small, there exists a constant C so that_

$$
\\theta\_{1},\\theta\_{2}
$$

(4.20)

$$
\|Q\_{g}(\\theta\_{1})-Q\_{g}(\\theta\_{2})\| _{C^{0,\\alpha}}\\leq C(\|\\theta_{1}\| _{C^{2,\\alpha}}+\|\\theta_{2}\| _{C^{2,\\alpha}})\|\\theta_{1}-\\theta\_{2}\|\_{C^{2,\\alpha}}.
$$

Proof.

The proof is left as an exercise, with a few hints. First, show that
1

(4.21)

$$
\\Gamma(g+h) _{i j}^{k}=\\Gamma(g)_{i j}^{k}+\\frac{1}{2}(g+h)^{k m}\\left{\\nabla\_{j}h\_{i m}+\\nabla\_{i}h\_{j m}-\\nabla\_{m}h\_{i j}\\right}.
$$

In shorthand, we can therefore write the covariant derivative of any tensor _T_ as

$$
T
$$

(4.22)

$$
\\nabla\_{g+h}T=\\nabla\_{g}T+(g+h)^{-1} _\\nabla\_{g}h_ T,
$$

where the notation _∗_ denotes taking various contractions of the tensors involved
(the exact indices contracted do not matter for the conclusion).

(4.23)

Next, for any metric ˜g, the curvature tensor can be written in shorthand as

$$
\\tilde{g},
$$

$$
R m\_{\\tilde{g}}=\\nabla\_{\\tilde{g}}\\Gamma\_{\\tilde{g}}.
$$

Using (4.22), show that this implies an expansion of the form

(4.24)

$$
R m(g+h)=R m(g)+(g+h)^{-1} _\\nabla^{2}h+(g+h)^{-2}_\\nabla h\*\\nabla h.
$$

Contract with (g + h)−1 to get

_Ric(g_ \+ _h_) and then use the formula

$$
(g+h)^{-1}
$$

$$
Ric(g+h)
$$

(4.25)

$$
(g+h)^{-1}=g^{-1}-g^{-1}(g+h)^{-1}h.
$$

to pull out the terms in the linearization,
resulting expression for Qg.

and (4.20) will then follow from the

$$
Q\_{g}
$$

* * *

### 4\. Existence of the Kuranishi map

The following is the main tool
\[Biq13a, Lemma 8.3\].

used to construct the map Ψ, see for example

Lemma 4.11. _Let H_ : _E→F be a smooth map between Banach spaces. Define_
Q = H − H(0) − H′(0). Assume that there are positive constants C1,s0,C2 so that
_the following are satisfied:_

$$
H:E\\to F
$$

$$
Q=H-H(0)-H^{\\prime}(0)
$$

$$
C\_{1},s\_{0},C\_{2}
$$

_•_ (1) _The nonlinear term Q satisfies_

$$
Q
$$

$$
\|Q(x)-Q(y)\| _{F}\\leq C_{1}(\|x\| _{E}+\|y\|_{E})\|x-y\|\_{E}
$$

_for every x,y ∈ BE(0,s0)._

$$
x,y\\in B\_{E}(0,s\_{0})
$$

• (2) The linearized operator at 0, H′(0) : E→F is an isomorphism with
_inverse bounded by C2._

$$
0,H'(0):E\\to F
$$

$$
C\_{2}
$$

If s and ‖H(0)‖F are sufficiently small (depending upon C1,s0,C2), then there is
_a unique solution x ∈ BE(0,s_) _of the equation H(x_) = _0._

$$
\|H(0)\|\_{F}
$$

$$
\\left(C\_{1},s\_{0},C\_{2}\\right)
$$

$$
x\\in B\_{E}(0,s)
$$

$$
H(x)=0
$$

Outline of Proof. The equation _H(x_) = 0 expands to

(4.26)

$$
H(x)=0
$$

$$
H(0)+H^{\\prime}(0)(x)+Q(x)=0.
$$

If we let x = Gy, where G is the inverse of H′(0), then we have

$$
x=G y
$$

$$
H^{\\prime}(0)
$$

(4.27)

$$
H(0)+y+Q(Gy)=0,
$$

or

(4.28)

$$
y=-H(0)-Q(Gy).
$$

In other words, _y_ is a fixed point of the mapping

$$
y
$$

(4.29)

$$
T:y\\mapsto-H(0)-Q(Gy).
$$

With the assumptions in the lemma, it follows that _T_ is a contraction mapping,
so a fixed point exists by the standard fixed point theorem (T ny0 converges to a
unique fixed point for any _y0_ sufficiently small).

$$
T
$$

$$
(T^{n}y\_{0}
$$

To prove Theorem 4.1, we next construct the map

$$
\\Psi:H\_{E}^{1}\\to H\_{E}^{1},
$$

(4.30)

whose zero set is locally isomorphic to the zero set of _P._ Consider _H_ = Π _◦ P,_
where Π is projection to the orthogonal complement of HE1. The differential of this
map is now surjective. Choose any complement K to the space HE1, and restrict
the mapping to this complement. Equivalently, let _G_ be any right inverse, i.e.,
H′(0)G = Id, and let K be the image of G. Given a kernel element x0 ∈ HE1, the
equation _H(x0_ \+ _Gy_) = 0 expands to

$$
H=\\Pi\\circ P,
$$

$$
H\_{E}^{1}
$$

$$
H\_{E}^{1},
$$

$$
H^{\\prime}(0)G=Id
$$

$$
x\_{0}\\in H\_{E}^{1}
$$

$$
H(x\_{0}+G y)=0
$$

(4.31)

$$
H(0)+H^{\\prime}(0)(x\_{0}+G y)+Q(x\_{0}+G y)=0.
$$

We therefore need to find a fixed point of the map

(4.32)

$$
T\_{x\_{0}}:y\\mapsto-H(0)-Q(x\_{0}+G y),
$$

and the proof is the same as before.

To finish the proof of Theorem 4.1, we need to identify the kernel of the linearized operator.

* * *

$$
Ker(P'\_g)
$$

$$
\\textit{If}\\lambda<0
$$

Proposition 4.12. If λ < 0, then Ker(Pg′) consists exactly of transverse-traceless
_tensors satisfying_

(4.33)

$$
\\Delta h+2Rm\*h=0.
$$

Proof. If P ′(h) = 0, then h is smooth by elliptic regularity, Also,
1

$$
P^{\\prime}(h)=0
$$

(4.34)

$$
P^{\\prime}h=R i c^{\\prime}(h)-\\lambda h-\\frac{1}{2}\\mathcal{L} _{g}\\beta_{g}h.
$$

Applying βg to this equation, yields βgLgβgh = 0, so βgh = 0 by the above argument. Taking a trace, we find that

$$
\\beta\_{g}
$$

$$
\\beta\_{g}\\mathcal{L} _{g}\\beta_{g}h=0
$$

$$
\\beta\_{g}h=0
$$

(4.35)

$$
\\Delta(t r\_{g}(h))+2\\lambda\\cdot t r\_{g}(h)=0,
$$

$$
tr\_{g}(h)=0
$$

so trg(h) = 0 since λ < 0.

$$
\\lambda<0
$$

### 5\. Rigidity of Einstein metrics

In general it is quite difficult to construct the map Ψ explicitly, but one of the
easiest consequences of the above discussion is the following (see \[Koi78\]):

$$
\\Psi
$$

1
Corollary 4.13. _If Ric(g_) = _λ·g with λ_ < _0, and HE_ = _{0} then g is rigid (isolated_
as an Einstein metric). That is, if gt is a path of Einstein metrics passing through
_g, all with Einstein constant λ_ < _0, then there exist a path of diffeomorphisms_
ϕt: M→M such that gt = ϕ∗t g.

$$
\\lambda<0,
$$

$$
Ric(g)=\\lambda\\cdot g
$$

$$
H\_{E}^{1}=\\left{0\\right}
$$

$$
\\textit{if}g\_t
$$

$$
g,
$$

$$
\\lambda<0
$$

$$
g\_{t}=\\varphi\_{t}^{\*}g
$$

$$
\\varphi\_{t}:M\\rightarrow M
$$

We next discuss a few cases where it is known that _HE1_ = 0\. For a longer list,
see \[Koi78, Koi80, Koi82\].

$$
H\_{E}^{1}=0
$$

#### 5.1. The negative case

In the hyperbolic case, in Lecture 1 we proved that for _n ≥_ 3, _HE1_ = _{0},_ so
hyperbolic manifolds are locally rigid as Einstein metrics. In fact, something much
stronger is true in dimension four:

$$
n\\geq3,H\_{E}^{1}={0}
$$

Theorem 4.14 (Besson-Courtois-Gallot \[BCG95\]). If (M4,g) is compact and
_hyperbolic, then g is the unique Einstein metric on M, up to scaling._

$$
\\textit{If}\\left(M^{4},g\\right)
$$

This is proved using completely different methods than we have discussed here
(using the notion of volume entropy), which we will not have time to go into.
This is a generalization of Mostow rigidity, which says that hyperbolic metrics
are determined up to scaling by homotopy type in dimensions _n ≥_ 3 \[Mos68\].
An analogous rigidity result was proved for complex hyperbolic 4-manifolds using
Seiberg-Witten Theory in \[LeB95\].

$$
n\\geq3\\left\[\\mathbf{M o s68}\\right\]
$$

Einstein metrics with negative sectional curvature are also locally rigid:

Exercise 4.15. Show that any Einstein metric with negative sectional curvature
is rigid, that is, _HE1_ = _{0}._

$$
H\_{E}^{1}=\\left{0\\right}
$$

In the case of _n_ = 2, we saw in Lecture 1 that elements of _HE1_ are Codazzi
tensors. Using some elementary Riemann surface theory, it is possible to identify
these with the space of real parts of holomorphic quadratic differentials, see for
example \[EE69\]. By the Riemann-Roch Theorem, this space is of real dimension
_6‘ −_ 6, where _‘_ is the genus for genus _‘ ≥_ 2 \[Don11\].

$$
H\_{E}^{1}
$$

$$
n=2
$$

$$
\\ell\\geq2\[\\mathbf{D o n11}\]
$$

$$
6\\ell-6
$$

In the case of _n ≥_ 3, Codazzi tensors do not give infinitesimal Einstein deformations of a hyperbolic metric. However, they do yield infinitesimal deformations
of the locally conformally flat structure \[Laf83\]. Hyperbolic metrics admitting such
deformations are called _bendable._ For examples, see \[JM87\].

$$
n\\geq3
$$

* * *

#### 5.2. The positive case

It is possible to modify the above construction so that it works also in the positive
Einstein case, but we leave this as an exercise. The main difference is that the
gauge term should be chosen differently. We will just mention two issues that arise.

_•_ A positive Einstein metric can admit a nontrivial group of isometries (identity component). Letting Isom(M,g) denote the isometry group, we note
that Isom(M,g) acts on the space of symmetric tensors, and therefore,
by linearizing at the identity transformation, so does the space of Killing
fields K, which is the Lie algebra of Isom(M,g). Taking this action into
account, the end result is that the map Ψ is equivariant with respect to
the isometry group, and the actual moduli space is locally described by
Ψ−1(0)/K, rather than just Ψ−1(0).

$$
\\Psi^{-1}(0)/\\mathfrak{K},
$$

$$
\\Psi^{-1}(0)
$$

_•_ In the case of the sphere, we run into the problem of first nontrivial
eigenfunctions yielding pure trace kernel. However, these can also be
“gauged away” since they arise as tangents to conformal diffeomorphisms.
See for example \[GV15, Section 6\] for details.

Next, we discuss a few known rigid examples in the positive case:

• Any spherical space form Sn/Γ with the round metric gS. In this case, we
saw in Lecture 1 that the linearized operator obviously has trivial kernel,
see Corollary 1.10.

$$
g\_{S}
$$

_• S2 × S2_ with the product metric _g1_ \+ _g2._ In this case, we saw in Exercise 1.14 that the first two eigenvalues of of the linearized operator are _−1_
and 1, thus 0 does not occur as an eigenvalue.

$$
g\_{1}+g\_{2}
$$

$$
S^{2}\\times S^{2}
$$