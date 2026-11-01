---
retention_scope: session
part: 1
total_parts: 1
---

# ON THE GOLDBERG CONJECTURE

> Source: https://libir.josai.ac.jp/il/user_contents/02/G0000284repository/pdf/JOS-KJ00000229294.pdf
> Fetched: 2026-10-08 19:45
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
  "source": "serper",
  "source_url": "https://libir.josai.ac.jp/il/user_contents/02/G0000284repository/pdf/JOS-KJ00000229294.pdf",
  "metadata": {
    "provenance_urls": [
      "https://libir.josai.ac.jp/il/user_contents/02/G0000284repository/pdf/JOS-KJ00000229294.pdf"
    ],
    "search_origins": [
      {
        "source": "serper",
        "query": "LeBrun Goldberg conjecture 1995 full text PDF"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

Conjecture. The almost complex structure of a compact almost Kdhler ,ructure is the critical point condition for a certain class of Riemannian functiona,Is. ...

## Retrieved source content

# ON THE GOLDBERG CONJECTURE

# KOUEI SEKIGAWA

## 1\. INTRODUCTION

An almost Hermitian manifold $(M, J, g)$ is called an almost Kähler manifold if the Kähler form is closed (or equivalently, $\\mathfrak{S} _{X, Y, Z}g((\\nabla\_XJ)Y, Z)=0$, for $X, Y, Z \\in \\mathfrak{X}(M)$. where $\\mathfrak{S}_{X, Y, Z}$ denotes the cyclic sum with respect to $X, Y, Z$). By definition, a Kähler manifold $(\\nabla J=0)$ is an almost Kähler manifold. A non-Kähler, almost Kähler manifold is called a strictly almost Kähler manifold. The first example of compact strictly almost Kähler manifold was found by W.T. Thurston (\[19\]). It is well-known that an almost Kähler manifold with the integrable almost complex structure is a Kähler manifold. Concerning with the integrability, the following conjecture by S.I. Goldberg is known (\[3\]).

Conjecture. The almost complex structure of a compact almost Kähler Einstein manifold is integrable.

Blair and Ianus (\[2\]) studied variations in the set of metrics associated to a given symplectic form on a compact symplectic manifold and showed that the commutativity of the Ricci operator with the almost complex structure is the critical point condition for a certain class of Riemannian functionals. This fact authorizes the Goldberg conjecture. The conjecture is true in the case where the scalar curvature is non-negative (\[18\]). However, the conjecture is still wide open in the case where the scalar curvature is negative. In this talk, we shall introduce some other partial and related results (mainly, in for-dimensional case) to the Goldberg conjecture.

## 2\. PRELIMINARIES

First of all, we prepare some fundamental terminologies and formulas which will be used in our arguments.

Let $M=(M, J, g)$ be a 2n-dimensional almost Hermitian manifold with almost Hermitian structure $(J, g)$. We assume that the Kähler form $\\Omega$ of $M$ is defined by $\\Omega(X, Y) = g(X, JY)$ for $X, Y \\in \\mathfrak{X}(M)$, where $\\mathfrak{X}(M)$ denotes the Lie algebra of all smooth vector fields on $M$. We assume the $M$ is oriented by the volume form $dM = (-1)^n \\frac{\\Omega^n}{n!}$. We denote by $\\nabla$, $R$, $\\rho$ and $\\tau$ the Riemannian connection, the curvature tensor, the Ricci tensor and the scalar curvature of $M$, respectively. The curvature tensor $R$ is defined by $R(X, Y)Z = \[\\nabla\_X, \\nabla\_Y\]Z - \\nabla\_{\[X, Y\]}Z$, for $X, Y, Z \\in \\mathfrak{X}(M)$. We denote by $\\rho^\*$ the Ricci \*-tensor of $M$ defined by

(2.1) $$\\rho^\*(x, y) = \\frac{1}{2} \\text{trace of } (z \\mapsto R(x, Jy)Jz)$$

for $x, y, z \\in T\_p M, p \\in M$. Further, we denote by $\\tau^\*$ the _-scalar curvature of $M$ which is the trace of the linear endomorphism $Q^_ $ defined by $g(Q^ _x, y) = \\rho^_(x, y)$ for $x, y \\in T\_p M, p \\in M$. By the definition, we see immediately

(2.2) $$\\rho^ _(x, y) = \\rho^_(Jy, Jx),$$

and hence $\\rho^ _$ is symmetric if and only if $\\rho^_ $ is $J$-invariant. We may also note that if $M$ is Kähler, then $\\rho^\* = \\rho$ holds on $M$.

**Definition 1.** Almost Hermitian manifold $M = (M, J, g)$ is called a weakly _-Einstein manifold if $\\rho^_ = \\lambda^ _g$ ($\\lambda^_ = \\tau^ _/2n$) holds. Furthermore, if $\\lambda^_ $ is constant, then $M$ is called a \*-Einstein manifold.

The first Chern form $\\gamma$ of $M$ is given by

(2.3) $$8\\pi\\gamma = -\\varphi + 2\\psi,$$

where $\\varphi$ and $\\psi$ are 2-forms on $M$ defined by

$$\\varphi(x, y) = \\text{trace of } (z \\mapsto J(\\nabla\_x J)(\\nabla\_y J)z),$$

$$\\psi(x, y) = \\text{trace of } (z \\mapsto R(x, y)Jz),$$

for $x, y, z \\in T\_p M, p \\in M$. The first Chern class $c\_1(M)$ of $M$ is represented by $\\gamma$ in the de Rham cohomology group.

In the remaining of this section, we assume that the dimension of the considered almost Hermitian manifold is equal to four. It is known that the following identity folds for any four-dimensional almost Hermitian manifold:

(2.4) $$\\frac{1}{2}\\left{\\rho(x, y) + \\rho(Jx, Jy)\\right} - \\frac{1}{2}\\left{\\rho^ _(x, y) + \\rho^_(y, x)\\right} = \\frac{\\tau - \\tau^\*}{4}g(x, y)$$

for $x, y \\in T\_p M, p \\in M$.

The curvature operator $\\mathcal{R}$ is the symmetric endomorphism of the vector bundle $\\wedge^2 M$ of real 2-forms over $M$ defined by

(2.5) $$g(\\mathcal{R}(\\iota(x) \\wedge \\iota(y)), \\iota(z) \\wedge \\iota(w)) = -g(\\mathcal{R}(x, y)z, w)$$ for $x, y, z, w \\in T\_p M, p \\in M$, where $\\iota : TM \\rightarrow T^\*M$ denotes the duality defined by means of the metric $g$. The following decomposition for the vector bundle $\\wedge^2 M$ of real 2-forms on $M$ is useful in our arguments:

(2.6) $$\\wedge^2 M = \\mathbb{R} \\Omega \\oplus \\wedge^1\_0 M \\oplus LM$$

where $\\wedge^1\_0 M$ denotes the vector bundle of real primitive $J$-invariant 2-forms, $LM$ the vector bundle of real primitive $J$-skew-invariant 2-forms over $M$, respectively. The bundle $LM$ is endowed with the natural complex structure (also denote by $J$) which is defined by $(J\\Phi)(X, Y) = -\\Phi(JX, Y)$ ($X, Y \\in \\mathfrak{X}(M)$) for any local section $\\Phi$ of $LM$. The bundle $\\wedge^1\_0 M$ is identified itself with the bundle $\\wedge^2\_- M$ of anti-self-dual 2-forms, while the sum $\\mathbb{R} \\Omega \\oplus LM$ is the bundle $\\wedge^2\_+ M$ of self-dual 2-forms. Further, it is well-known that $M$ is Einstein if and only if both $\\wedge^2\_+ M$ and $\\wedge^2\_- M$ are preserved by the curvature operator $\\mathcal{R}$ (N. Hitchin, \[5\]).

In our talk, for any unitary basis (resp. any local unitary frame field) ${e\_i} = {e\_1, e\_2 = Je\_1, e\_3, e\_4 = Je\_3}$ of any point $p \\in M$ (resp. on a neighborhood of $p$), we shall adapt the following notational convention:

(2.7) $$R\_{ijkl} = g(R(e\_i, e\_j)e\_k, e\_l), \\dots R\_{\\bar{ij}\\bar{kl}} = g(R(Je\_i, Je\_j)Je\_k, Je\_l),$$
$$\\rho\_{ij} = \\rho(e\_i, e\_j), \\dots, \\rho\_{\\bar{ij}} = \\rho(Je\_i, Je\_j),$$
($1 \\leq i, j, k, l \\leq 4$). Then we have the following formulas.

(2.8) $$J\_{ij} = -J\_{ji}, \\quad \\nabla\_i J\_{jk} = -\\nabla\_i J\_{kl},$$
$$\\nabla\_i J\_{\\bar{j}\\bar{k}} = -\\nabla\_i J\_{jk}, \\nabla\_{\\bar{i}} J\_{\\bar{j}\\bar{k}} = -\\nabla\_i J\_{jk},$$
(2.9) $$\|\\nabla J\|^2 = 2(\\tau^\* - \\tau)$$

Taking account of (2.5) and (2.8), we have

(2.10) $$\\nabla \\Omega = \\alpha \\otimes \\Phi - J\\alpha \\otimes J\\Phi,$$

where $\\alpha$ is a local 1-form, $\\Phi$, $J\\Phi \\in LM$ and the local 1-form $J\\alpha$ is defined by $(J\\alpha)(X) = -\\alpha(JX), (X \\in \\mathfrak{X}(M))$. We set $g(\\nabla\_e e\_j, e\_k) = \\Gamma\_{ijk}$. Then, $\\Gamma\_{ijk} = -\\Gamma\_{ikj}$ hold.

Now, we assume that $M = (M, J, g)$ is in addition an Einstein manifold. Then, we have by (2.3)

(2.11) $$\\rho^ _\_{ij} + \\rho^_ _{ji} = \\frac{\\tau^\*}{2}\\delta_{ij}.$$

Since $\\mathcal{R}(\\wedge^2\_+) \\subset \\wedge^2\_+ M$, we may put

(2.12) $$\\mathcal{R}(\\Phi) = u\\Phi + wJ\\Phi + A\\Omega,$$
$$\\mathcal{R}(J\\Phi) = w\\Phi + vJ\\Phi + B\\Omega,$$ where $\\Phi = \\frac{1}{\\sqrt{2}}(e^1 \\wedge e^3 - e^2 \\wedge e^4)$, $J\\Phi = \\frac{1}{\\sqrt{2}}(e^1 \\wedge e^4 + e^2 \\wedge e^3)(e^i = \\iota(e\_i))$, and

$$u = -(R\_{1313} - R\_{1324}),$$
$$v = -(R\_{1414} + R\_{1423}),$$
$$w = -(R\_{1314} + R\_{1323}),$$
$$A = \\frac{1}{\\sqrt{2}}\\rho\_{14}^ _, \\quad B = -\\frac{1}{\\sqrt{2}}\\rho\_{13}^_.$$

Now, we define smooth functions $D$, $G$ and $K$ on $M$ respectively by

$$D = \\sum(R\_{ijkl} - R\_{ijkl})^2,$$
$$G = \\sum(\\rho\_{ij}^\* - \\rho\_{ji}^\*)^2,$$
$$K = (u-v)^2 + 4w^2.$$

Then, we have

$$G = 4\\left\|\\rho^ _\\right\|^2 - (\\tau^_)^2 = 16\\left{(\\rho\_{13}^ _)^2 + (\\rho\_{14}^_)^2\\right},$$
$$K = \\frac{(\\tau^\* - \\tau)^2}{16} - 4\\det \\mathcal{R}' _{LM},$$_
_$$\|\\mathcal{R}_{LM}\|^2 = \\frac{1}{16}D, \\quad \|\\mathcal{R}'\_{LM}\|^2 = \\frac{1}{16}(D-G),$$

where $\\mathcal{R}' _{LM} = P_{LM} \\circ \\mathcal{R} _{LM}$ ($P_{LM}: \\land^2 M \\to LM$ is the projection) and

$$\\Delta\\tau^\* = \\frac{G}{2} + 4K + \\frac{(3\\tau^\* - \\tau)(\\tau^\* - \\tau)}{4} - 4\\mathrm{div}\\bar{\\eta}$$

where $\\bar{\\eta} = (\\bar{\\eta} _a)$ is the vector field on $M$ defined by $\\bar{\\eta}a = \\sum{i,j}(\\nabla\_a J_{ij})\\rho\_{ij}^\*$.

Now, we assume further that the manifold $M$ under consideration is strictly almost Kähler one and $M\_0 = \\left{p \\in M \\mid \\tau^\* - \\tau > 0 \\text{ at } p\\right}$. Then, we may easily observe that $M\_0$ is a non-empty open submanifold of $M$ and there exists two $J$-invariant distributions on $\\mathcal{D}$ and $\\mathcal{D}^{\\perp}$ on $M$ such that $\\mathcal{D} = \\operatorname{span}{\\alpha^ _, J\\alpha^_} (\\iota(\\alpha^\*) = \\alpha)$. Let ${e\_i} = {e\_1, e\_2 = Je\_1, e\_3, e\_4 = Je\_3}$ be a local unitary frame filed on a neighborhood of any points of $M\_0$ such that $\\mathcal{D} = \\operatorname{span}{e\_1, e\_2}$ and $\\mathcal{D}^{\\perp} = \\operatorname{span}{e\_3, e\_4}$. Then, we have

$$\\nabla\\Omega = \\alpha \\otimes \\frac{1}{\\sqrt{2}}(e^1 \\wedge e^3 - e^2 \\wedge e^4) - J\\alpha \\otimes \\frac{1}{\\sqrt{2}}(e^1 \\wedge e^4 + e^2 \\wedge e^3)$$

for some 1-form $\\alpha$ ($\\alpha^\* \\in \\mathcal{D}$). A pair $({e\_i} _{i=1,\\dots,4}, {\\alpha, J\\alpha})$ of local unitary frame filed ${e\_i} = {e\_1, e\_2 = Je\_1, e\_3, e\_4 = Je\_3}$ and 1-forms ${\\alpha, J\\alpha}$ is said to be an adapted one to $\\nabla\\Omega$ if it satisfies (2.16) and $\\mathcal{D} = \\operatorname{span}{e\_1, e\_2}$, $\\mathcal{D}^{\\perp} = \\operatorname{span}{e\_3, e\_4}$. Let $({e\_i}_{i=1,\\dots,4}, {\\alpha, J\\alpha})$ be any adapted pair to $\\nabla\\Omega$. Then, for arbitrary local smooth functions $\\theta$ and $\\varphi$, we may check that $({e\_i(\\theta, \\varphi)} _{i=1,\\dots,4}, {\\alpha(\\theta, \\varphi), J\\alpha(\\theta, \\varphi)})$ (where $\\alpha(\\theta, \\varphi) = (\\cos \\theta)\\alpha - (\\sin \\theta)J\\alpha$, $e\_1(\\theta, \\varphi) = (\\cos \\varphi)e\_1 - (\\sin \\varphi)e\_2$, $e\_2(\\theta, \\varphi) = Je\_1(\\theta, \\varphi)$, $e\_3(\\theta, \\varphi) = (\\cos(\\theta + \\varphi))e\_3 + (\\sin(\\theta + \\varphi))e\_4$, $e\_4(\\theta, \\varphi) = Je\_3(\\theta, \\varphi))$ is also an adapted pair to $\\nabla \\Omega$. With respect to an adapted pair $({e\_i}_{i=1,\\dots,4}, {\\alpha, J\\alpha})$ to $\\nabla \\Omega$, we have the following equalities:

$$w = \\frac{1}{\\sqrt{2}} \\left{- \\Gamma\_{131}\\alpha\_1 - \\Gamma\_{132}\\alpha\_2 - \\nabla\_3\\alpha\_1 + \\alpha\_2\\left(\\Gamma\_{312} + \\Gamma\_{334}\\right)\\right},$$

(2.17)

$$w = \\frac{1}{\\sqrt{2}} \\left{\\Gamma\_{241}\\alpha\_1 + \\Gamma\_{242}\\alpha\_2 + \\nabla\_4\\alpha\_2 + \\alpha\_1\\left(\\Gamma\_{412} + \\Gamma\_{434}\\right)\\right},$$

(2.18)

$$w = \\frac{1}{\\sqrt{2}} \\left{\\Gamma\_{241}\\alpha\_1 + \\Gamma\_{242}\\alpha\_2 - \\nabla\_3\\alpha\_1 + \\alpha\_2\\left(\\Gamma\_{312} + \\Gamma\_{334}\\right)\\right},$$

(2.19)

$$u = \\frac{1}{\\sqrt{2}} \\left{\\Gamma\_{141}\\alpha\_1 + \\Gamma\_{142}\\alpha\_2 + \\nabla\_3\\alpha\_2 - \\frac{\\tau^\* - \\tau}{2\\sqrt{2}} + \\alpha\_1\\left(\\Gamma\_{312} + \\Gamma\_{334}\\right)\\right},$$

(2.20)

$$v = \\frac{1}{\\sqrt{2}} \\left{- \\Gamma\_{141}\\alpha\_1 - \\Gamma\_{142}\\alpha\_2 - \\nabla\_4\\alpha\_1 + \\alpha\_2\\left(\\Gamma\_{412} + \\Gamma\_{434}\\right)\\right},$$

(2.21)

$$v = \\frac{1}{\\sqrt{2}} \\left{- \\Gamma\_{231}\\alpha\_1 - \\Gamma\_{232}\\alpha\_2 - \\nabla\_3\\alpha\_2 - \\alpha\_1\\left(\\Gamma\_{312} + \\Gamma\_{334}\\right)\\right},$$

(2.22)

$$\\rho\_{13}^\* = \\frac{1}{\\sqrt{2}} \\left{\\nabla\_1\\alpha\_2 - \\nabla\_2\\alpha\_1 + \\alpha\_1\\left(\\Gamma\_{112} + \\Gamma\_{134}\\right) + \\alpha\_2\\left(\\Gamma\_{212} + \\Gamma\_{234}\\right)\\right},$$

(2.20)

$$\\rho\_{13}^\* = \\frac{1}{\\sqrt{2}} \\left{\\left(\\Gamma\_{431} - \\Gamma\_{341}\\right)\\alpha\_1 + \\left(\\Gamma\_{432} - \\Gamma\_{342}\\right)\\alpha\_2\\right},$$

(2.20)

$$\\rho\_{14}^\* = -\\frac{1}{\\sqrt{2}} \\left{\\nabla\_1\\alpha\_1 + \\nabla\_2\\alpha\_2 + \\alpha\_1\\left(\\Gamma\_{212} + \\Gamma\_{234}\\right) - \\alpha\_2\\left(\\Gamma\_{112} + \\Gamma\_{134}\\right)\\right},$$

(2.20)

$$\\rho\_{14}^\* = \\frac{1}{\\sqrt{2}} \\left{\\left(\\Gamma\_{342} - \\Gamma\_{432}\\right)\\alpha\_1 - \\left(\\Gamma\_{341} - \\Gamma\_{431}\\right)\\alpha\_2\\right}.$$

(2.21)

$$\\Gamma\_{142} - \\Gamma\_{131} = \\frac{\\alpha\_2}{\\sqrt{2}}, \\quad \\Gamma\_{242} - \\Gamma\_{231} = -\\frac{\\alpha\_1}{\\sqrt{2}}$$

(2.21)

$$\\Gamma\_{132} + \\Gamma\_{141} = \\frac{\\alpha\_1}{\\sqrt{2}}, \\quad \\Gamma\_{232} + \\Gamma\_{241} = \\frac{\\alpha\_2}{\\sqrt{2}}$$

(2.22)

$$\\Gamma\_{131} - \\Gamma\_{232} = -\\frac{\\alpha\_2}{\\sqrt{2}}, \\quad \\Gamma\_{132} + \\Gamma\_{231} = \\frac{\\alpha\_1}{\\sqrt{2}}$$

* * *

(2.23) $(\\Gamma\_{131}\\alpha\_1 + \\Gamma\_{132}\\alpha\_2)\\rho\_{14}^\* - (-\\Gamma\_{132}\\alpha\_1 + \\Gamma\_{131}\\alpha\_2)\\rho\_{13}^\* = 0,$

(2.24) $(\\Gamma\_{131}\\alpha\_1 + \\Gamma\_{132}\\alpha\_2)\\rho\_{13}^\* - \\left(\\Gamma\_{132}\\alpha\_1 - \\Gamma\_{131}\\alpha\_2 - \\frac{\\tau^\* - \\tau}{2\\sqrt{2}}\\right)\\rho\_{14}^\* = 0,$

(2.25) $8\\pi\\gamma = \\tau(e^1 \\wedge e^2 + e^3 \\wedge e^4) + (\\tau^\* - \\tau)e^3 \\wedge e^4$
$$

- 4\\rho\_{14}^ _(e^1 \\wedge e^3 - e^2 \\wedge e^4) + 4\\rho\_{13}^_(e^1 \\wedge e^4 + e^2 \\wedge e^3).
  $$

By (2.20), we see that if $G = 0$ on $M$, namely, $M$ is a weakly \*-Einstein manifold, then the distributions $\\mathcal{D}$ and $\\mathcal{D}^\\perp$ are both integrable. Let $M\_1 = { p \\in M \\mid G > 0 \\text{ at } p }$ and $(M\_0 \\cap (M\_1)^c)^{i}$ be the interior of $M\_0 \\cap (M\_1)^c = M\_0 \\cap (M - M\_1)$. Then, by choosing local functions $\\theta$ and $\\varphi$ suitably, we may obtain an adopted pair $({e\_i}\_{i=1,\\dots,4}, {\\alpha, J\\alpha})$ to $\\nabla\\Omega$ on $M\_0 \\cap M\_1$ or $(M\_0 \\cap (M\_1)^c)^{i}$ satisfying the following conditions:

(2.26) $\\alpha = \|\\alpha\|e^1$, $J\\alpha = \|\\alpha\|e^2,$
$$
\\nabla\\Omega = \|\\alpha\|\\left{e^1 \\otimes \\frac{1}{\\sqrt{2}}(e^1 \\wedge e^3 - e^2 \\wedge e^4) - e^2 \\otimes \\frac{1}{\\sqrt{2}}(e^1 \\wedge e^4 + e^2 \\wedge e^3)\\right},
$$
and
$\\rho\_{13}^\* = \\frac{\\sqrt{G}}{4}$, $\\rho\_{14}^\* = 0.$

We call such an adapted pair a special one to $\\nabla\\Omega$. We may easily observe that the equalities (2.17) ~~(2.25) take more convenient form with respect to special adapted ones. These reduced equalities play an important role in the proofs of Theorems 3.4~~ 3.9 which will be introduced in the next section.

## 3\. PARTIAL AND RELATED RESULTS

In this section, we shall state some partial answers to the Goldberg conjecture. A space of constant negative sectional curvature is an Einstein space of negative scalar curvature.

Theorem 3.1 (Oguro-Sekigawa, \[13\]). A $2n (\\geq 4)$-dimensional real hyperbolic space $\\mathbb{H}^{2n}$ can not admit any compatible almost Kähler structure.

Remark. The local version of the above result was given by Oguro (\[12\]).

An irreducible locally symmetric space is an Einstein space. So, it is a natural question whether a compact locally symmetric space admits compatible almost Kähler structure or not. Concerning this question, we have the following.

* * *

Theorem 3.2 (Murakoshi, Oguro, Sekigawa, \[8\]). Let $M = (M, J, g)$ be a four-dimensional compact almost Kähler locally symmetric space. Then, $M$ is a locally Hermitian symmetric space (and hence, a Kähler manifold).

In the above result, the assumption of compactness cannot be removed. In fact, Oguro-Sekigawa (\[14\]) have showed that the Riemannian product space $\\mathbb{H}^3 \\times \\mathbb{R}^1$ of a 3-dimensional real hyperbolic space $\\mathbb{H}^3$ and a real line $\\mathbb{R}^1$ admits a compatible strictly almost Kähler structure. T. Oguro (\[11\]) obtained a generalization of this example. More precisely, he has constructed uncountably may examples of strictly almost Kähler structures on the product Riemannian manifold $\\mathbb{H}^3 \\times \\mathbb{R}^{2n-3}$. Both real hyperbolic space $\\mathbb{H}^{2n}$ and the Riemannian product space $\\mathbb{H}^3 \\times \\mathbb{R}^1$ can be regarded as solvable Lie group spaces. Recently, W. Obata obtained the following result in her Master's thesis (\[10\]).

Theorem 3.3. Let $G = (G, J, g)$ be a 2n-dimensional negatively curved homogeneous almost Kähler Einstein manifold with Iwasawa type $(\\mathfrak{g}, g)$ ($\\mathfrak{g}$ is the Lie algebra of $G$). Then $(G, J, g)$ is holomorphically isometric to a complex hyperbolic space $\\mathbb{CH}^n$ with the canonical Kähler structure.

We note that W. Jelonek (\[6\]) gave some examples of compact strictly almost Kähler manifolds of negative constant scalar curvature (which are not Einstein).

In the sequel, we shall introduce several recent result for the conjecture in four-dimensional case. Oguro and Sekigawa (\[15\]) proved the following.

Theorem 3.4. Let $M = (M, J, g)$ be a four-dimensional almost Kähler Einstein and \*-Einstein manifold. Then $M$ is Kähler.

Now, we shall introduce the example of four-dimensional strictly almost Kähler Einstein manifold ($\\rho \\equiv 0$) constructed by P. Nurowski and M. Przanowski \[9\] and discuss it. First, we write down their example. Let $M$ be a four-dimensional real half-space given by

$$M = \\left{(x\_1, x\_2, x\_3, x\_4) \\in \\mathbb{R}^4 \\mid x\_1 > 0, (x\_2, x\_3, x\_4) \\in \\mathbb{R}^3\\right}.$$

* * *

We define a Riemannian metric $g$ and almost complex structure $J$ on $M$ respectively by

$$g = \\left( g\_{ij} \\right) = \\begin{pmatrix}
x\_1 & 0 & 0 & 0 \
0 & x\_1 + \\frac{x\_3^2}{4x\_1} & -\\frac{x\_2x\_3}{4x\_1} & \\frac{x\_3}{2x\_1} \
0 & -\\frac{x\_2x\_3}{4x\_1} & x\_1 + \\frac{x\_2^2}{4x\_1} & -\\frac{x\_2}{2x\_1} \
0 & \\frac{x\_3}{2x\_1} & -\\frac{x\_2}{2x\_1} & \\frac{1}{x\_1}
\\end{pmatrix},$$

$$J = \\left( J\_j^i \\right) = \\begin{pmatrix}
0 & 0 & -1 & 0 \
0 & \\frac{x\_3}{2x\_1} & -\\frac{x\_2}{2x\_1} & \\frac{1}{x\_1} \
1 & 0 & 0 & 0 \
\\frac{x\_2}{2} & -x\_1 - \\frac{x\_3^2}{4x\_1} & \\frac{x\_2x\_3}{4x\_1} & -\\frac{x\_3}{2x\_1}
\\end{pmatrix},$$

where $g\_{ij} = g\\left(\\frac{\\partial}{\\partial x\_i}, \\frac{\\partial}{\\partial x\_j}\\right)$ and $J\\left(\\frac{\\partial}{\\partial x\_j}\\right) = \\sum\_i J\_j^i \\frac{\\partial}{\\partial x\_i}$. Then, we see easily that $(J,g)$ is an almost Hermitian structure on $M$ and the Kähler form $\\Omega$ is given by

$$\\Omega = -x\_1dx\_1 \\wedge dx\_3 - \\frac{x\_2}{2}dx\_2 \\wedge dx\_3 + dx\_2 \\wedge dx\_4.$$

Now, we define vector fields $e\_1$, $e\_2$, $e\_3$, $e\_4$ on $M$ respectively by

$$e\_1 = \\frac{1}{\\sqrt{x\_1}} \\frac{\\partial}{\\partial x\_1}, \\quad e\_2 = \\frac{1}{\\sqrt{x\_1}} \\frac{\\partial}{\\partial x\_3} + \\frac{x\_2}{2\\sqrt{x\_1}} \\frac{\\partial}{\\partial x\_4},$$

$$e\_3 = \\sqrt{x\_1} \\frac{\\partial}{\\partial x\_4}, \\quad e\_4 = \\frac{1}{\\sqrt{x\_1}} \\frac{\\partial}{\\partial x\_2} - \\frac{x\_3}{2\\sqrt{x\_1}} \\frac{\\partial}{\\partial x\_4}.$$

Then, we see easily that ${e\_i}\_{i=1,2,3,4}$ is a unitary frame field on $M$ with $e\_2 = Je\_1$, $e\_4 = Je\_3$. By straightforward calculation, we may check that $\\rho = 0$, $\\rho^\* = \\frac{1}{x\_1^3}g$ and hence $(M, J,g)$ is a strictly almost Kähler Ricci-flat weakly _-Einstein manifold with the -scalar curvature $\\tau^ = \\frac{4}{x\_1^3}$. Furthermore, we may observe that $(M, J,g)$ is a space of pointwise constant holomorphic sectional curvature $\\frac{\\tau^_}{8} = \\frac{1}{2x\_1^3}$.

Concerning the above example, we obtain the following result which improves Theorem 3.4.

**Theorem 3.5** (Oguro, Sekigawa, Yamada, \[16\]). Let $M = (M, J,g)$ be a four-dimensional strictly almost Kähler Einstein and weakly _-Einstein manifold. Then, $M$ is a Ricci-flat space of pointwise constant holomorphic sectional curvature $\\frac{\\tau^_}{8}$.

* * *

Remark. J. Armstrong has also obtained the above result by making use of the other technique in his Ph. D. Thesis.

From Theorem 3.5, we have immediately the following.

Corollary 3.6. Let $M = (M, J, g)$ be a four-dimensional compact almost Kähler Einstein and weakly $\\cdot$-Einstein manifold. Then, $M$ is a Kähler manifold.

Concerning the conjecture, we have further the following.

Theorem 3.7 (\[17\]). Let $M = (M, J, g)$ be a four-dimensional almost Kähler Einstein manifold of constant $\\cdot$-scalar curvature. Then, $M$ is a Kähler manifold.

Theorem 3.8 (\[17\]). Let $M = (M, J, g)$ be a four-dimensional compact almost Kähler Einstein manifold. If the norm of skew-symmetric part of the Ricci $\\cdot$-tensor is a constant, then $M$ is a Kähler manifold.

Remark. J. Armstrong (\[1\]) proved that a four-dimensional compact almost Kähler Einstein manifold of constant $\\cdot$-scalar curvature is integrable. So, the above Theorem 3.8 improves Theorem 3.4 and also his result. Further, he proved that if $M$ is a compact four-dimensional almost Kähler Einstein manifold, then equality $\\tau^\* - \\tau = 0$ holds at some point of $M$. We see also that if $M$ is a compact four-dimensional almost Kähler manifold with negative constant scalar curvature then there exists a constant $\\delta(\\leq 1)$ such that the equality $\\tau \\leq \\tau^\* \\leq \\delta\\tau$ holds. We have the following.

Theorem 3.9 (\[17\]). Let $M = (M, J, g)$ be a four-dimensional compact almost Kähler Einstein manifold with negative scalar curvature. Then, the $\\cdot$-scalar curvature $\\tau^ _$ satisfies $\\tau \\leq \\tau^_ \\leq -\\frac{\\tau}{6}$ on $M$.

Remark. Recently, we showed that the assumption of compactness ins the above Theorem 3.8 can be removed.

## References

\[1\] J. Armstrong, On four-dimensional almost Kähler manifolds, Quart. J. Math. Oxford Ser. (2) 48 (1997), no. 192, 405–415.
\[2\] D.E. Blair and S. Ianus, Critical associated metrics on symplectic manifolds, Contemp. Math. 51 (1986), 23–29.
\[3\] S.I. Goldberg, Integrability of almost Kähler manifolds, Proc. Amer. Math. Soc. 21 (1969). 96–100.

* * *

\[4\] E. Heintze, On homogeneous manifolds of negative curvature, Math. Ann. 211 (1974), 23–34.

\[5\] N.J. Hitchin, Compact four-dimensional Einstein manifolds, J. Diff. Geom. 9 (1974), 435–441.

\[6\] W. Jelonek, Some simple examples of almost Kähler non-Kähler structures, Math. Ann. 305 (1996), 639–649.

\[7\] S. Kobayashi, Homogeneous Riemannian manifolds of negative curvature, Tôhoku Math. J. 14 (1962), 413–415.

\[8\] N. Murakoshi, T. Oguro and K. Sekigawa, Four-dimensional almost Kähler locally symmetric spaces, Diff. Geom. Appl. 6 (1996), 237–244.

\[9\] P. Nurowski and M. Przanowski, A four-dimensional example of Ricci flat metric admitting almost Kähler, non-Kähler structure, (preprint, dg-ga 9802057), 1998.

\[10\] W. Obata, Homogeneous Riemannian manifolds of negative curvature and the Goldberg conjecture (Master Thesis, Tôhoku Univ.).

\[11\] T. Oguro, Examples of non-Kähler almost Kähler symmetric spaces, C. R. Math. Rep. Acad. Sci. Canada, XVIII (1996), 243–246.

\[12\] T. Oguro, On almost Kähler manifolds of constant curvature, Tsukuba J. Math. 21 (1997), 199–206.

\[13\] T. Oguro and K. Sekigawa, Non-existence of almost Kähler structure on hyperbolic space of dimension $2n(\\geq 4)$, Math. Ann. 350 (1994), 317–329.

\[14\] T. Oguro and K. Sekigawa, Almost Kähler structures on the Riemannian product of a 3-dimensional hyperbolic space and a real line, Tsukuba J. Math. 20 (1996), 151–161.

\[15\] T. Oguro and K. Sekigawa, Four-dimensional almost Kähler and \*-Einstein manifolds, Geometriae Dedicata 69 (1998), 91–112.

\[16\] T. Oguro,K. Sekigawa and A. Yamada, Four-dimensional almost Kähler Einstein and weakly \*-Einstein manifolds, Yokohama Math. J. 47 (1999), 75–92.

\[17\] T. Oguro,K. Sekigawa, On some four-dimensional almost Kähler Einstein manifolds, preprint.

\[18\] K. Sekigawa, On some compact Einstein almost Kähler Einstein manifolds, J. Math. Soc. Japan 36 (1987), 677–684.

\[19\] W.P. Thurston, Some simple examples of symplectic manifolds, Proc. Amer. Math. Soc. 55 (1976), 467–468.