---
retention_scope: session
part: 1
total_parts: 1
---

# Riccibordversionanglais

> Source: https://univ-avignon.hal.science/hal-05002677/file/RicciBordVersionAnglais.pdf
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
  "source_url": "https://univ-avignon.hal.science/hal-05002677/file/RicciBordVersionAnglais.pdf",
  "metadata": {
    "provenance_urls": [
      "https://univ-avignon.hal.science/hal-05002677/file/RicciBordVersionAnglais.pdf"
    ],
    "search_origins": [
      {
        "source": "exa",
        "query": "Einstein operator Hessian curvature functional fourth order elliptic boundary problem clamped boundary conditions"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

HAL Id: hal-05002677
https://univ-avignon.hal.science/hal-05002677v1
Preprint submitted on 24 Mar 2025
HAL is a multi-disciplinary open access
archive for the deposit and dissemination of scientific research documents, whether they are published or not. The documents may come from
teaching and research institutions in France or
abroad, or from public or private research centers.
L’archive ouverte pluridisciplinaire HAL, est
destinée au dépôt et à la diffusion de documents
scientifiques de niveau recherche, publiés ou non,
émanant des établissements d’enseignement et de
recherche français ou étrangers, des laboratoires
publics ou privés.
HAL Authorization
Prescribed Ricci curvature near an Einstein manifold
with boundary
Erwann Delay
To cite this version:
Erwann Delay. Prescribed Ricci curvature near an Einstein manifold with boundary. 2025. ffhal05002677ff
PRESCRIBED RICCI CURVATURE NEAR AN
EINSTEIN MANIFOLD WITH BOUNDARY
ERWANN DELAY
Abstract. Let (M, g) be a compact Einstein Riemannian manifold with boundary. We show that under certain conditions, the
map that associates to a metric on M its Ricci curvature, its induced conformal class on the boundary, and its mean curvature on
the boundary is locally invertible near g. The contravariant Ricci
operator, as well as other operators such as the Einstein operator,
are also studied.
Keywords: Ricci curvature, Einstein metrics, symmetric 2-tensors,
quasi-linear elliptic PDE.
2010 MSC: 53C21, 53A45, 58J05, 58J37, 35J62.
Conte

## Retrieved source content

# <strong>Prescribed Ricci curvature near an Einstein manifold with boundary</strong> Erwann Delay

To cite this version:

Erwann Delay. Prescribed Ricci curvature near an Einstein manifold with boundary. 2025. ⟨hal-05002677⟩

**HAL Id: hal-05002677**

**https://univ-avignon.hal.science/hal-05002677v1**

Preprint submitted on 24 Mar 2025

**HAL** is a multi-disciplinary open access archive
for the deposit and dissemination of scientific research documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or private research centers.

L’archive ouverte pluridisciplinaire **HAL**, est destinée au dépôt et à la diffusion de documents scientifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.
[Image: Im0]

HAL Authorization

---

# PRESCRIBED RICCI CURVATURE NEAR AN EINSTEIN MANIFOLD WITH BOUNDARY

ERWANN DELAY

Abstract. Let (M, g) be a compact Einstein Riemannian manifold with boundary. We show that under certain conditions, the
map that associates to a metric on M its Ricci curvature, its induced conformal class on the boundary, and its mean curvature on
the boundary is locally invertible near g. The contravariant Ricci
operator, as well as other operators such as the Einstein operator,
are also studied.

$$
(M,g)
$$

Keywords: Ricci curvature, Einstein metrics, symmetric 2-tensors,
quasi-linear elliptic PDE.

2010 MSC: 53C21, 53A45, 58J05, 58J37, 35J62.

## Contents

1. Introduction
2. Definitions, Notations, and Conventions
3. Fredholm Properties and Isomorphisms
4. Case of Ricci Curvature
5. Contravariant Ricci Operator
6. Einstein-type Curvature
7. Riemann-Christoffel Type Curvature
References

1
3
4
5
8
9
13
14

## 1. Introduction

On a Riemannian manifold (M, g), we denote by Ric(g) its Ricci curvature. We first consider the (field of) geometric symmetric 2-tensors
of the form
Ric (g) := Ric(g) + Λg,

$$
\operatorname{Ric}_{\Lambda}(g):=\operatorname{Ric}(g)+\Lambda g,
$$

where Λ is a constant. This tensor is geometrically natural in the sense
that for any sufficiently regular diffeomorphism ϕ,

$$
\varphi
$$

$$
\varphi^{*}\operatorname{Ric}_{\Lambda}(g)=\operatorname{Ric}_{\Lambda}(\varphi^{*}g).
$$

*Date*: March 24, 2025.

---

Here, we address the problem of inverting the operator Ric<sub>Λ</sub>. Given a
symmetric tensor field RΛ on M, we seek a Riemannian metric g such
that

$$
\operatorname{Ric}_{\Lambda}
$$

$$
R_{\Lambda}
$$

$$
M
$$

(1.1)

$$
\mathrm{Ric}_{\Lambda}(g)=R_{\Lambda}.
$$

This requires solving a particularly complex quasi-linear system.

The prescribed Ricci curvature problem dates back to the 1980s. De-
Turck [13], in 1981, first proved a local existence result near a point p in
R<sup>n</sup> under the intrinsic assumption that the matrix of R(p) is invertible
(see also [15]).

$$
p
$$

$$
R(p)
$$

$$
\mathbb{R}^n
$$

Subsequently, global results were obtained: Hamilton [19], in 1984,
treated the case of the unit sphere in R<sup>n+1</sup> (with n > 2), proving a
local inversion result near the standard metric.

$$
\mathbb{R}^{n+1}
$$

$$
n>2)
$$

Such local inversion techniques were later adapted to certain Einstein manifolds [7], [12], [14], [8], [6], [9], and then to parallel Ricci
manifolds [10], [11]. The problem of prescribed Ricci curvature has
also been studied on Lie groups and homogeneous spaces with completely different methods (see [17] and references therein).

Obstruction results to the inversion of Ricci curvature also exist [16],
[3], [19], [5], [7].

So far, the only results concerning manifolds with boundary is local
near a boundary point [23] or for special domains of some cohomogeneity one manifolds [24]. Recent works on Einstein metrics on manifolds
with boundary, such as [1], have inspired us to obtain *global* results on
M near an Einstein metric.

To illustrate our results simply, we state a particular case. The
induced boundary metric is denoted by g<sup>T</sup>, and the mean curvature of
the boundary by H (g).

$$
g^{T}
$$

$$
H(g)
$$

Theorem 1.1. *Let* (M, g) *be a smooth compact Einstein Riemannian*
*manifold with boundary, with* Ric(g) = λg*. Suppose that* λ + Λ 6= 0 *and*
*that* −2Λ *is not in the spectrum of the Hodge Laplacian acting on 1-*
*forms with Dirichlet condition, nor in the spectrum of the Lichnerowicz*
*Laplacian with ADN conditions. Let* k ∈ N\{0} *and* α ∈ (0, 1)*, then*
for every r ∈ C<sup>k+2,α</sup>(M, S₂) close to zero, every conformal class [γ]
close to [g<sup>T</sup>] in [C<sup>k+2,α</sup>(∂M, S<sub>2+</sub>)], and every function H close to H (g)
in C<sup>k+1,α</sup>(∂M), there exists a unique h close to zero in C<sup>k+2,α</sup>(M, S₂)
*such that* 
 Ric (g + h) = Ric (g) + r *in* M,

$$
(M,g)
$$

$$
\mathrm{Ric}(g)=\lambda g
$$

$$
\lambda+\Lambda\neq0
$$

$$
\alpha\in(0,1)
$$

$$
k\in\mathbb{N}\backslash\{0\}
$$

$$
r\in C^{k+2,\alpha}(M,\mathcal{S}_2)
$$

$$
\left[g^{T}\right]
$$

$$
[C^{k+2,\alpha}(\partial M,S_{2}^{+})]
$$

$$
H(g)
$$

$$
C^{k+1,\alpha}(\partial M)
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

$$
\left\{\begin{array}{l l}{\operatorname{Ric}_{\Lambda}(g+h)=\operatorname{Ric}_{\Lambda}(g)+r}&{\text{}\mathit{in}\;M,}\\ {\left[(g+h)^{T}\right]=[\gamma]}&{\text{}\mathit{on}\;\partial M,}\\ {H(g+h)=\mathcal{H}}&{\text{}\mathit{on}\;\partial M.}\\ \end{array}\right.
$$

*Moreover, the map* (r, [γ], H) 7→ h *is smooth from a neighborhood of*
(0, [g<sup>T</sup>], H (g)) to a neighborhood of zero in the corresponding Banach
*spaces.*

$$
(r,[\gamma],\mathcal{H})\mapsto h
$$

$$
(0,[g^{T}],H(g))
$$

The ADN condition, introduced by M. Anderson [2], is a mixed
Dirichlet-Neumann condition specified in Definition 3.4.

---

Our solution’s regularity is optimal, as can be seen by applying a
low-regularity diffeomorphism to the equation (1.1).

We also establish an analogous result for the contravariant Ricci
operator, which is better suited to negative curvature cases.

Furthermore, we extend this approach to other operators, such as
the Einstein tensor.

Finally, we show that the image of certain Riemann-Christoffel-type
operators forms smooth submanifolds in C<sup>∞</sup>.

$$
C^{\infty}
$$

Acknowledgments: I thank Lan-Hsuan Huang for insightful discussions concerning [1] and [2]. This article was partially funded by
the French National Research Agency (ANR) grants ANR-23-CE40-
0010-02 and ANR-24-CE40-0702.

## 2. Definitions, Notations, and Conventions

We denote by ∇ the Levi-Civita connection of g, by Ric(g) its Ricci
curvature, and by Riem(g) its sectional Riemannian curvature.

Let T<sub>pq</sub> be the set of covariant tensors of rank p and contravariant
tensors of rank q. When p = 2 and q = 0, we denote by S₂ the subset
of symmetric tensors, which decomposes as G ⊕ S˚<sub>2</sub>, where G is the set
of g-conformal tensors and S˚<sub>2</sub> is the set of traceless tensors (relative to
g). The set S<sub>2+</sub> denotes the subset of S₂ consisting of positive definite
tensors.

$$
p
$$

$$
\mathcal{T}_{p}^{q}
$$

$$
q.
$$

$$
q=0
$$

$$
p=2
$$

$$
\mathcal{S}_{2}
$$

$$
\mathcal{G}\oplus\mathring{\mathcal{S}}_{2}
$$

$$
\mathring{\mathcal{S}}_{2}
$$

$$
g)
$$

$$
\mathcal{S}_{2}
$$

$$
\mathcal{S}_{2}^{+}
$$

For k ∈ N, α ∈ (0, 1) and a tensor bundle E, C<sup>k,α</sup>(M, E) is the
usual Ḧolder space of tensor fields with C<sup>k,α</sup> regularity. The space of
conformal class of metric of C<sup>k,α</sup> regularity on the boundary is denoted
by
[C<sup>k,α</sup>(∂M, S)] = {[γ], γ ∈ C<sup>k,α</sup>(∂M, S)}

$$
k\in\mathbb{N},\;\alpha\in(0,1)
$$

$$
C^{k,\alpha}(M,E)
$$

$$
C^{k,\alpha}
$$

$$
C^{k,\alpha}
$$

$$
\begin{array}{r l}{[C^{k,\alpha}(\partial M,\mathcal{S}_{2}^{+})]\quad=\quad\{[\gamma],\quad\gamma\in C^{k,\alpha}(\partial M,\mathcal{S}_{2}^{+})\}}\\ {\cong\quad\{\gamma\in C^{k,\alpha}(\partial M,\mathcal{S}_{2}^{+}),|\gamma|=1\},}\end{array}
$$

where |.| is the determinant (with respect to a fixed background metric,
say g<sup>T</sup>), and where for γ ∈ C<sup>k,α</sup>(∂M, S<sub>2+</sub>), we identify its conformal
class [γ] with its unique representative of determinant 1.

$$
\left|.\right|
$$

$$
\left|g^{T}\right)
$$

$$
\gamma\in C^{k,\alpha}(\partial M,\mathcal{S}_2^+)
$$

We use Einstein’s summation convention (indices range from 1 to n),
and we use g<sub>ij</sub> and its inverse g<sup>ij</sup> to raise or lower indices.

$$
g_{ij}
$$

$$
g^{ij}
$$

The Laplacian is defined by

$$
\triangle=-tr\nabla^{2}=\nabla^{*}\nabla,
$$

where ∇<sup>∗</sup> is the formal L² adjoint of ∇. The Lichnerowicz Laplacian
acting on symmetric 2-covariant tensor fields is [20]

$$
\nabla^*
$$

$$
L^{2}
$$

(2.1)

$$
\triangle_{L}=\triangle+2(\mathrm{Ric}-\mathrm{Rim})
$$

where

$$
(\operatorname{Ric}u)_{ij}=\frac{1}{2}[\operatorname{Ric}(g)_{ik}u_j^k+\operatorname{Ric}(g)_{jk}u_i^k],
$$

and

$$
(\mathrm{Riem}\;u)_{i j}=\mathrm{Riem}(g)_{i k j l}u^{k l}.
$$

---

For u a symmetric 2-covariant tensor, its divergence is defined by

$$
\left(\mathrm{div}\boldsymbol{u}\right)_{i}=-\nabla^{j}u_{ji}.
$$

For a 1-form ω on M, its divergence is defined by:

$$
\omega
$$

$$
M,
$$

$$
d^{*}\omega=-\nabla^{i}\omega_{i},
$$

and the symmetric part of its covariant derivatives:

$$
(\mathcal{L}\omega)_{i j}=\frac{1}{2}(\nabla_{i}\omega_{j}+\nabla_{j}\omega_{i}),
$$

(note that L<sup>∗</sup> = div). The Hodge-de Rham Laplacian acting on 1-forms
is denoted by
∗
∆ = dd<sup>∗</sup> + d d = ∆ + Ric.

$$
\mathcal{L}^*=\mathrm{div}\big)
$$

$$
\Delta_{H}=d d^{*}+d^{*}d=\Delta+\mathrm{Ric}.
$$

The Bianchi operator for symmetric 2-tensors into 1-forms is defined
as:
1

$$
B_{g}(h)=\operatorname{div}_{g}h+\frac{1}{2}d(\operatorname{Tr}_{g}h).
$$

## 3. Fredholm Properties and Isomorphisms

We recall here the Fredholm properties of Laplacian-type operators
plus zero-order terms acting on 1-forms or on symmetric two-tensors.
We begin by stating a well-known fact (see eg. [22]).

Proposition 3.1. *Let* k ∈ N*,* α ∈ (0, 1)*, and* c *be a real number. The*
operator from C<sup>k+2,α</sup>(M, T₁) to C<sup>k,α</sup>(M, T₁)×C<sup>k+2,α</sup>(M, T₁)|∂M, given
*by*
{
(∆ + c)ω *in* M

$$
k\in\mathbb{N},\alpha\in(0,1)
$$

$$
C^{k+2,\alpha}(M,\mathcal{T}_{1})
$$

$$
C^{k,\alpha}(M,\mathcal{T}_{1})\times C^{k+2,\alpha}(M,\mathcal{T}_{1})_{|\partial M|}
$$

$$
\left\{\begin{array}{l l}{(\Delta_{H}+c)\omega}&{{~i n~}M}\\ {\omega}&{{~o n~}\partial M.}\\ \end{array}\right.
$$

*is Fredholm of index 0.*

$$
\theta.
$$

Let C₀<sup>k,α</sup>(M, T₁) denote the space of C<sup>k,α</sup>(M, T₁) 1-forms satisfying
the Dirichlet condition (i.e., vanishing on the boundary of M).

$$
C_{0}^{k,\alpha}(M,\mathcal{T}_{1})
$$

$$
C^{k,\alpha}(M,\mathcal{T}_{1})
$$

Corollary 3.2. *Let* k ∈ N*,* α ∈ (0, 1)*, and* c *be a real number. If* −c *is*
not in the spectrum of the Hodge Laplacian ∆<sub>H</sub> with Dirichlet boundary
*condition, then*

$$
k\in\mathbb{N},\alpha\in(0,1)
$$

$$
c
$$

$$
\textit{If}-c
$$

$$
\Delta_{H}
$$

$$
\Delta_{H}+c:C_{0}^{k+2,\alpha}(M,\mathcal{T}_{1})\longrightarrow C^{k,\alpha}(M,\mathcal{T}_{1}),
$$

*is an isomorphism.*

We recall that the kernel of ∆<sub>H</sub> + c with Dirichlet boundary condition is generically trivial for boundary deformations towards the interior (see, for example, [1], Lemma 1.2).

$$
\Delta_{H}+c
$$

The following proposition involves the linearization DH (g) of the
mean curvature operator H at g. Even though we will not need the
explicit formula, we recall one (see [21], for example, with a different sign convention). Let ν be the outward-pointing normal to the boundary and IAB = −〈∇∂<sub>A</sub>ν, ∂<sub>B</sub>〉 be the second fundamental form of the
boundary, so that H = Tr<sub>g</sub>T I. Then we have

$$
\mathbb{I}_{A B}=-\langle\nabla_{\partial_{A}}\nu,\partial_{B}\rangle
$$

$$
H=\operatorname{Tr}_{g^T}\mathbb{I}
$$

$$
DH(g)h=div_{g^T}(h(\nu,.)^T)+\frac{1}{2}\operatorname{Tr}_{g^T}((\nabla_\nu h)^T)-\frac{1}{2}h(\nu,\nu)H.
$$

We can now state the following

Proposition 3.3. *Let* k ∈ N*,* α ∈ (0, 1)*, and* c *be a real number. The*
*operator*

$$
k\in\mathbb{N},\alpha\in(0,1)
$$

$$
L_{c}:C^{k+2,\alpha}(M,\mathcal{S}_{2})\longrightarrow C^{k,\alpha}(M,\mathcal{S}_{2})\times C^{k+1,\alpha}(\partial M,\mathcal{S}_{2})\times C^{k+2,\alpha}(\partial M,\mathring{\mathcal{S}}_{2})\times C^{k+1,\alpha}(\partial M),
$$

*given by*

$$
L_{c}(h)=\left\{\begin{array}{ll}(\Delta_{L}+c)h&in M\\B_{g}(h)&on\partial M\\h^{T}-\frac{1}{n-1}\operatorname{Tr}_{g^{T}}(h^{T})g^{T}&on\partial M\\DH(g)h&on\partial M\end{array}\right.
\theta.
$$

*is Fredholm of index 0.*

Proof. In [2], M. Anderson proves that L<sub>c</sub> is elliptic and Fredholm of
index zero when c = −2λ; the case of arbitrary c follows immediately
by homotopy.

$$
L_{c}
$$

$$
c=-2\lambda
$$

This proposition motivates the definition of a mixed condition between Dirichlet and Neumann, introduced by M. Anderson.

Definition 3.4 (ADN condition). We say that h ∈ C<sup>k+2,α</sup>(M, S₂) satisfies the ADN condition if


$$
h\in C^{k+2,\alpha}(M,\mathcal{S}_2)
$$

$$
\left\{\begin{array}{l l}{B_{g}(h)=0}&{\mathrm{on}\partial M}\\ {h^{T}-\frac{1}{n-1}\operatorname{Tr}_{g^{T}}(h^{T})g^{T}=0}&{\mathrm{on}\partial M}\\ {D H(g)h=0}&{\mathrm{on}\partial M}\end{array}\right.
$$

We thus immediately obtain

Corollary 3.5. *If* −c *is not in the spectrum of the Lichnerowicz Lapla-*
cian with ADN condition, then L<sub>c</sub> is an isomorphism.

$$
\mathit{If}-c
$$

$$
L_{c}
$$

Remark 3.6. The tensor g is in the kernel of L₀ if and only if ∂M is
a minimal hypersurface of M. Indeed, the first three components of
L₀(h) vanish if h = g. For the fourth, note that if g<sub>t</sub> = (1 + t)²g, then
H (g<sub>t</sub>) = (1 + t)<sup>−1</sup>H (g), so by linearizing at t = 0, we obtain

$$
L_{0}
$$

$$
L_{0}(h)
$$

$$
h=g
$$

$$
g_{t}=(1+t)^{2}g
$$

$$
H(g_t)=(1+t)^{-1}H(g)
$$

$$
t=0
$$

$$
2DH(g)g=-H(g).
$$

## 4. Case of Ricci Curvature

In this section, we prove Theorem 1.1. It is now well known that the
Ricci equation is not elliptic due to the invariance of curvature under
diffeomorphism. We will modify this equation by drawing inspiration
from DeTurck’s method. We thus add a gauge term so that this new equation becomes elliptic while ensuring that its solutions remain solutions of the Ricci equation. In order to construct our new equation,
let us recall some differentials of operators.

We already have (see [4], for example)
1

$$
D\operatorname{Ric}(g)h=\frac{1}{2}\Delta_L h-\mathcal{L}_g B_g(h).
$$

The linearization in the first variable of the Bianchi operator is (see,
for example, [8])

$$
[D B_{(.)}(R)](g)h=-R B_{g}(h)+T(g,R)h,
$$

where R is here identified with the corresponding endomorphism of
T <sup>∗</sup>M and
1

$$
T^{*}M
$$

$$
[T(g,R)h]_{j}=T(g,R)_{j}^{k l}h_{k l}=\frac{1}{2}(\nabla^{k}R_{j}^{l}+\nabla^{l}R_{j}^{k}-\nabla_{j}R^{k l})h_{k l}.
$$

We define

$$
\mathrm{Ric}_{\Lambda}(g):=\mathrm{Ric}(g)+\Lambda g
$$

In particular, if g is Einstein with Ric(g) = λg, we have

$$
\mathrm{Ric}(g)=\lambda g
$$

$$
\left[D B_{(.)}\left(\operatorname{Ric}_{\Lambda}(g)\right)\right](g)h=-(\lambda+\Lambda)B_{g}(h).
$$

Finally, recall that for any metric g, B<sub>g</sub>(Ric<sub>Λ</sub>(g)) = 0 by the Bianchi
identity.

$$
g,B_{g}(\operatorname{Ric}_{\Lambda}(g))=0
$$

The equation we choose to solve will be

(4.1)

$$
F(r,h)=(0,0,\gamma,\mathcal{H}),
$$

with

(4.2)

$$
F(h,r):=\left\{\begin{array}{l l}{\operatorname{Ric}_{\Lambda}(g+h)-R_{\Lambda}-\mathcal{L}_{g}((\lambda+\Lambda)^{-1}B_{g+h}(R_{\Lambda}))}&{\mathrm{i n~}M,}\\ {-(\lambda+\Lambda)^{-1}B_{g+h}(R_{\Lambda})}&{\mathrm{o n~}\partial M,}\\ {|(g+h)^{T}|^{\frac{-1}{n-1}}(g+h)^{T}}&{\mathrm{o n~}\partial M,}\\ {H(g+h)}&{\mathrm{o n~}\partial M,}\\ \end{array}\right.
$$

where

$$
R_{\Lambda}=\operatorname{Ric}(g)+\Lambda g+r=(\lambda+\Lambda)g+r,
$$

and |(g + h)<sup>T</sup> | denotes the determinant of (g + h)<sup>T</sup>.

$$
\left|(g+h)^T\right|
$$

$$
(g+h)^T
$$

Let us first verify that the solutions of the new equation are solutions
of the equation we are interested in.

Proposition 4.1. Under the conditions of Theorem 1.1, if h ∈ C<sup>k+2,α</sup>(M, S₂)
*is small enough, and if the metric* g + h *is a solution of* (4.1)*, then it*
*is a solution of*


$$
\mathrm{if}h\in C^{k+2,\alpha}(M,\mathcal{S}_2)
$$

$$
\left\{\begin{array}{l l}{\operatorname{Ric}_{\Lambda}(g+h)=R_{\Lambda}}&{\mathit{in}M,}\\ {|(g+h)^{T}|^{\frac{-1}{n-1}}(g+h)^{T}=\gamma}&{\mathit{on}\partial M,}\\ {H(g+h)=\mathcal{H}}&{\mathit{on}\partial M,}\\ \end{array}\right.
$$

---

$$
B_{g+h}
$$

Proof. Applying B<sub>g+h</sub> to the first component of (4.1), we note that
B<sub>g+h</sub>[Ric<sub>Λ</sub>(g + h)] = 0 by the Bianchi identity. Thus, defining

$$
B_{g+h}[\mathrm{Ric}_{\Lambda}(g+h)]=0
$$

$$
\omega:=(\lambda+\Lambda)^{-1}B_{g+h}(R_{\Lambda}),
$$

we see that ω vanishes at the boundary and

$$
\omega
$$

$$
P_{g+h}\omega:=B_{g+h}[\mathcal{L}_{g}(\omega)]+(\lambda+\Lambda)\omega=0.
$$

The operator P<sub>g</sub> can be expressed in local coordinates as:
[]

$$
P_{g}
$$

$$
(P_{g}\omega)_{j}=-\nabla^{i}\left[\frac{1}{2}(\nabla_{i}\omega_{j}+\nabla_{j}\omega_{i})\right]+\frac{1}{2}\nabla_{j}\nabla^{i}\omega_{i}+\mathrm{Ric}(g)_{j}^{k}\omega_{k}+\Lambda\omega_{j}.
$$

Commuting the derivatives and multiplying by 2, we obtain

$$
2P_{g}=\Delta_{g}\omega+\operatorname{Ric}_{g}\omega+2\Lambda\omega=(\Delta_{H}+2\Lambda)\omega.
$$

Since the operator P<sub>g</sub> with Dirichlet condition has a trivial kernel, by
corollary 3.2, it is an isomorphism from C₀<sup>k+1,α</sup>(M, T₁) to C<sup>k−1,α</sup>(M, T₁),
then for small h in C<sup>k+2,α</sup>(M, S₂), P<sub>g+h</sub> with Dirichlet condition remains injective, we conclude that ω = 0.

$$
P_{g}
$$

$$
C_{0}^{k+1,\alpha}(M,\mathcal{T}_{1})\mathrm{to}C^{k-1,\alpha}(M,\mathcal{T}_{1})
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

$$
P_{g+h}
$$

$$
\omega=0
$$

Remark 4.2. The fact that B<sub>g+h</sub>(RΛ) vanishes proves that the identity
map from (M, g + h) to (M, RΛ) is harmonic (see [18], for example).

$$
B_{g+h}(R_{\Lambda})
$$

$$
\left(M,g+h\right)
$$

$$
\left(M,\widetilde{R}_{\Lambda}\right)
$$

We will now construct the solutions of (4.1) using an implicit function argument in Banach spaces.

Proposition 4.3. *Under the conditions of Theorem 1.1, for any small*
r ∈ C<sup>k+2,α</sup>(M, S₂), for any conformal class [γ] close to [g<sup>T</sup>] in [C<sup>k+2,α</sup>(∂M, S<sub>2+</sub>)],
and for any function H close to H (g) in C<sup>k+1,α</sup>(∂M), there exists a
unique h close to zero in C<sup>k+2,α</sup>(M, S₂) that solves (4.1).

$$
r\in C^{k+2,\alpha}(M,\mathcal{S}_2)
$$

$$
[\gamma]
$$

$$
[g^{\overset{\frown}{T}}]
$$

$$
[C^{\mathring{k}+2,\alpha}(\partial M,\mathcal{S}_{2}^{+})]
$$

$$
H(g)
$$

$$
\widetilde{C}^{k+1,\alpha}(\partial M)
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

*Proof.* We consider F as a mapping defined in a neighborhood of zero in
C<sup>k+2,α</sup>(M, S₂)×C<sup>k+2,α</sup>(M, S₂) with values in C<sup>k,α</sup>(M, S₂)×C<sup>k+1,α</sup>(∂M, S₂)×
[C<sup>k+2,α</sup>(∂M, S<sub>2+</sub>)] × C<sup>k+1,α</sup>(∂M). We already have
<sup>T</sup>

$$
C^{k+2,\alpha}(M,\mathcal{S}_2)\times C^{k+2,\alpha}(M,\mathcal{S}_2)
$$

$$
C^{k,\alpha}(\tilde{M},\mathcal{S}_{2})\times C^{k+1,\alpha}(\partial M,\mathcal{S}_{2})\times
[C^{k+2,\alpha}(\partial M,\mathcal{S}_{2}^{+})]\times C^{k+1,\alpha}(\partial M)
$$

$$
F(0,0)=(0,0,[g^T],H(g)).
$$

Considering the differentials of the operators given at the beginning of
the section, the differential of F with respect to h at 0 is
1

$$
h
$$

$$
D_{h}F(0,0)=\frac{1}{2}L_{2\Lambda},
$$

where L<sub>2Λ</sub> is described in Proposition 3.3. By Corollary 3.5, this operator is an isomorphism from C<sup>k+2,α</sup>(M, S₂) to C<sup>k,α</sup>(M, S₂)×C<sup>k+1,α</sup>(∂M, S₂)×
C<sup>k+2,α</sup>(∂M, S˚<sub>2</sub>)×C<sup>k+1,α</sup>(∂M). The implicit function theorem allows
us to conclude.

$$
L_{2\Lambda}
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

$$
C^{k,\alpha}(M,\mathcal{S}_2)\times C^{k+1,\alpha}(\partial M,\mathcal{S}_2)\times
C^{k+2,\alpha}(\partial M,\mathring{\mathcal{S}}_2)\times C^{k+1,\alpha}(\partial M)
$$

Remark 4.4. If L<sub>2Λ</sub> has a kernel, we can still solve equation (1.1) but
modulo a projection. In this case, we take
1 1

$$
L_{2\Lambda}
$$

$$
R_{\Lambda}=\mathrm{Ric}_{\Lambda}(g)+r-\frac{1}{2}\Pi(h)=(\lambda+\Lambda)g+r-\frac{1}{2}\Pi(h),
$$ where Π is the L²-orthogonal projection onto the kernel; see [10]. According to Remark 3.6, if Λ = 0, the hypotheses of Theorem 1.1 imply
that the boundary of M must not be a minimal hypersurface. For the
case Λ = 0 with minimal boundary, if the kernel is one-dimensional, so
generated by g, we can also solve (1.1) up to a multiplicative constant,
as in [19]. Here, we can take (see [6] and [10], Remark 4.4)

$$
L^{2}
$$

$$
\Lambda=0
$$

$$
\Lambda=0
$$

$$
R_{0}=e^{-\frac{1}{2n\lambda}\langle\mathrm{Tr}_{g}h\rangle}(\mathrm{Ric}(g)+r)=e^{-\frac{1}{2n\lambda}\langle\mathrm{Tr}_{g}h\rangle}(\lambda g+r)
$$

where

$$
\langle\operatorname{Tr}_{g}h\rangle={\frac{1}{\operatorname{Vol}_{g}(M)}}\int_{M}\operatorname{Tr}_{g}h d\mu_{g}.
$$

## 5. Contravariant Ricci Operator

We are interested here in the inversion of the (shifted) contravariant
Ricci operator:
g 7→ Ric (g) := Ric(g) + Λg<sup>−1</sup>

$$
g\mapsto\overline{{\operatorname{Ric}}}_{\Lambda}(g):=\overline{{\operatorname{Ric}}}(g)+\Lambda g^{-1}
$$

whose components in local coordinates are

$$
\overline{{\mathrm{Ric}}}_{\Lambda}(g)^{i j}=g^{i k}g^{j l}\operatorname{Ric}(g)_{k l}+\Lambda g^{i j}=g^{i k}g^{j l}\operatorname{Ric}_{\Lambda}(g)_{k l}.
$$

We will use the obvious notation

$$
\overline{{\operatorname{Ric}}}_{\Lambda}(g)=g^{-1}\operatorname{Ric}_{\Lambda}(g)g^{-1}.
$$

We adapt the steps of Section 4. First, we have
1

$$
D\overline{{\mathrm{Ric}}}_{\Lambda}(g)h=g^{-1}[\frac{1}{2}\Delta_{L}h-\mathcal{L}_{g}B_{g}(h)-2\operatorname{Ric}h-\Lambda h]g^{-1}.
$$

Let us set B<sub>g</sub>(R) = B<sub>g</sub>(gRg), so that if ∇R = 0, we obtain

$$
\overline{{B}}_{g}(\overline{{R}})=B_{g}(g\overline{{R}}g)
$$

$$
\nabla\overline{R}=0
$$

$$
D\overline{{B}}_{(.)}(\overline{{R}})h=-g\overline{{R}}B_{g}(h)+B_{g}(h\overline{{R}}g+g\overline{{R}}h).
$$

If moreover R = (λ + Λ)g<sup>−1</sup>, we find

$$
\overline{R}=(\lambda+\Lambda)g^{-1}
$$

$$
D\overline{B}_{(.)}(\overline{R})h=(\lambda+\Lambda)B_g(h)=g\overline{R}B_g(h).
$$

The gauge equation we choose to solve here will be

$$
F(h,\overline{r})=(0,0,\gamma,\mathcal{H})
$$

with

(5.1)

$$
\overline{{F}}(h,\overline{{r}}):=\left\{\begin{array}{l l}{\overline{{F}}_{1}(h,r)}&{\mathrm{in}M,}\\ {(\lambda+\Lambda)^{-1}\overline{{B}}_{g+h}(\overline{{R}}_{\Lambda})}&{\mathrm{on}\partial M,}\\ {|(g+h)^{T}|^{\frac{-1}{n-1}}(g+h)^{T}}&{\mathrm{on}\partial M,}\\ {H(g+h)}&{\mathrm{on}\partial M,}\\ \end{array}\right.
$$

where

$$
\overline{{F}}_{1}(h,\overline{{r}}):=g[\overline{{\operatorname{Ric}}}_{\Lambda}(g+h)-\overline{{R}}_{\Lambda}]g+\mathcal{L}_{g}\{(\lambda+\Lambda)^{-1}\overline{{B}}_{g+h}[\overline{{R}}_{\Lambda}]\},
$$

and

$$
\overline{{R}}_{\Lambda}=\overline{{\operatorname{Ric}_{\Lambda}}}(g)+\overline{{r}}=(\lambda+\Lambda)g^{-1}+\overline{{r}}.
$$

---

Theorem 5.1. *Let* k ∈ N\{0} *and* α ∈ (0, 1)*. Let* g *be an Einstein*
*metric with* Ric(g) = λg *and let* Λ∈R *such that* λ + Λ 6= 0*. As-*
*sume that* 4λ + 2Λ *is not in the spectrum of the Lichnerowicz Laplacian*
*with ADN condition, nor in the spectrum of the Hodge Laplacian with*
Dirichlet condition. Then for all r ∈ C<sup>k+2,α</sup>(M, S<sup>2</sup>) close to zero, for
every conformal class [γ] close to [g<sup>T</sup>] in [C<sup>k+2,α</sup>(∂M, S<sub>2+</sub>)], and every
function H close to H (g) in C<sup>k+1,α</sup>(∂M, S₂), there exists a unique h
close to zero in C<sup>k+2,α</sup>(M, S₂) such that


$$
k\in\mathbb{N}\backslash\{0\}
$$

$$
\alpha\in(0,1)
$$

$$
\mathrm{Ric}(g)=\lambda g
$$

$$
\lambda+\Lambda\neq0
$$

$$
\Lambda\in\mathbb{R}
$$

$$
4\lambda+2\Lambda
$$

$$
\overline{{r}}\in C^{k+2,\alpha}(M,\mathcal{S}^{2})
$$

$$
\left[g^{T}\right]
$$

$$
[C^{k+2,\alpha}(\partial M,S_{2}^{+})]
$$

$$
H(g)
$$

$$
C^{k+1,\alpha}(\partial M,\mathcal{S}_{2})
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

$$
\left\{\begin{array}{l l}{\overline{{\operatorname{Ric}}}_{\Lambda}(g+h)=\overline{{\operatorname{Ric}}}_{\Lambda}(g)+\overline{{r}}}&{\mathit{on}M}\\ {[(g+h)^{T}]=[\gamma]}&{\mathit{on}\partial M}\\ {H(g+h)=\mathcal{H}}&{\mathit{on}\partial M}\end{array}\right.
$$

*Moreover, the map* (r, [γ], H) 7→ h *is smooth from a neighborhood of*
(0, [g<sup>T</sup>], H (g)) into a neighborhood of zero between the corresponding
*Banach spaces.*

$$
(\overline{{r}},[\gamma],\mathcal{H})\mapsto h
$$

$$
(0,[g^{T}],H(g))
$$

$$
\overline{F}_{1}(0,0)=0
$$

Proof. We still have F <sub>1</sub>(0, 0) = 0 and since g is Einstein,

$$
D_{h}\overline{{F}}_{1}(0,0)=\frac{1}{2}\Delta_{L}-2\lambda-\Lambda.
$$

The corollary (3.5) proves that the operator D<sub>h</sub>F (0, 0) is an isomorphism from C<sup>k+2,α</sup>(M, S₂) to C<sup>k,α</sup>(M, S₂). By the implicit function
theorem, for all (r, [γ], H) close to (0, [g<sup>T</sup>], H (g)) in their respective
spaces, there exists h close to zero in C<sup>k+2,α</sup>(M, S₂) such that

$$
D_{h}\overline{F}(0,0)
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

$$
C^{k,\alpha}(M,\mathcal{S}_{2})
$$

$$
\left(\overline{r},[\gamma],\mathcal{H}\right)
$$

$$
\left(0,[g^{\dot{T}}],H(g)\right)
$$

$$
C^{\dot{k}+2,\alpha}(M,\widehat{\mathcal{S}}_{2})
$$

$$
\overline{{F}}(h,\overline{{r}})=(0,0,\gamma,\mathcal{H}).
$$

We then apply B<sub>g+h</sub> to the equation F <sub>1</sub>(h, r) = 0, obtaining

$$
\overline{B}_{g+h}
$$

$$
\overline{F}_{1}(h,\overline{r})=0
$$

$$
\overline{{P}}_{g+h}\omega:=B_{g+h}\mathcal{L}_{g}\omega-(\lambda+\Lambda)\omega=0
$$

where

$$
\omega=(\lambda+\Lambda)^{-1}\overline{B}_{g+h}(\overline{R}_{\Lambda})
$$

is zero at the boundary. By hypothesis, the operator

$$
\overline{{P}}_{g}=\frac{1}{2}(\Delta-\mathrm{Ric}_{g})-(\lambda+\Lambda)=\frac{1}{2}(\Delta_{H}-4\lambda-2\Lambda),
$$

with Dirichlet boundary condition is injective (and is an isomorphism
from C₀<sup>k+1,α</sup>(M, T₁) to C<sup>k−1,α</sup>(M, T₁) by corollary 3.2), so if h is small
enough, P <sub>g+h</sub> remains so, thus ω = 0.

$$
C_{0}^{k+1,\alpha}(M,\mathcal{T}_{1})
$$

$$
C^{k-1,\alpha}(M,\mathcal{T}_{1})
$$

$$
\overline{P}_{g+h}
$$

$$
\omega=0
$$

## 6. Einstein-type Curvature

We show here that the method of Section 4 can also be adapted to
other operators of Einstein type. For κ and Λ two real constants, we
define the tensor

$$
\mathrm{Ein}(g):=\mathrm{Ric}(g)+\kappa R(g)g+\Lambda g.
$$

---

$$
\kappa=-\frac{1}{2}
$$

Thus, for example, when κ = −<sup>1</sup>/<sub>2</sub>, we recover the Einstein tensor (with
cosmological constant Λ), and if κ = −<sub>2(n1−1)</sub> and Λ = 0, the Schouten
tensor.

$$
\Lambda)
$$

$$
\kappa=-\frac{1}{2(n-1)!}
$$

$$
\Lambda=0
$$

We study the inversion of the operator Ein. Given a symmetric
2-tensor E, we seek g such that

(6.1)

$$
\mathrm{Ein}(g)=E.
$$

Since we have

$$
\mathrm{Tr}_{g}\mathrm{Ein}(g)=(1+n\kappa)R(g)+n\Lambda,
$$

the equation (6.1) is equivalent to

$$
\operatorname{Ric}(g)=E-{\frac{\kappa\operatorname{Tr}_{g}E+\Lambda}{1+n\kappa}}g.
$$

For any E, we define

$$
E.
$$

$$
\mathcal{B}_{g}(E)=\mathrm{div}_{g}E+\frac{2\kappa+1}{2(1+\kappa n)}d\mathrm{Tr}_{g}E=B_{g}(E)-\frac{(n-2)\kappa}{2(1+\kappa n)}d\mathrm{Tr}_{g}E,
$$

such that the Bianchi identity translates here as

$$
\mathcal{B}_{g}(\operatorname{Ein}(g))=0.
$$

Knowing already the differential of B<sub>g</sub>(E) relative to the metric (see [8],
for example), we find that the differential of this operator relative to
the metric is
(n − 2)κ

$$
B_{g}(E)
$$

$$
D[\mathcal{B}_{(.)}(E)](g)h=-E B_{g}(h)+\frac{(n-2)\kappa}{2(1+\kappa n)}d\langle E,h\rangle+T(E,h),
$$

where E is here identified with the endomorphism of T <sup>∗</sup>M corresponding to it, and
1

$$
T^{*}M
$$

$$
\mathrm{it},
$$

$$
T(E,h)_{j}=\frac{1}{2}(\nabla_{k}E_{j l}+\nabla_{l}E_{k j}-\nabla_{j}E_{k l})h^{k l}.
$$

In particular, if g is Einstein, with Ric(g) = λg, then Ein(g) = τ g with
τ = (1 + nκ)λ + Λ, and

$$
\mathrm{Ric}(g)=\lambda g.
$$

$$
\operatorname{Ein}(g)=\tau g
$$

$$
\tau=(1+n\kappa)\lambda+\Lambda
$$

$$
D[\mathcal{B}_{(.)}(E)](g)h=-\tau B_{g}(h)+\frac{(n-2)\kappa}{2(1+\kappa n)}\tau d\operatorname{Tr}_{g}h.
$$

By analogy with Section 4, we define

$$
\mathcal{F}_{1}(h,e):=\operatorname{Ric}(g+h)-E+\frac{\kappa\operatorname{Tr}_{g+h}E+\Lambda}{1+\kappa n}(g+h)-\mathcal{L}_{g}(\tau^{-1}\mathcal{B}_{g+h}(E)),
$$

and

(6.2)

$$
\mathcal{F}(h,r):=\left\{\begin{array}{l l}{\mathcal{F}_{1}(h,e)}&{\mathrm{in}M,}\\ {-\tau^{-1}\mathcal{B}_{g+h}(E)}&{\mathrm{on}\partial M,}\\ {|(g+h)^{T}|^{\frac{-1}{n-1}}(g+h)^{T}}&{\mathrm{on}\partial M,}\\ {H(g+h)}&{\mathrm{on}\partial M,}\\ \end{array}\right.
$$

where

$$
E=\operatorname{Ein}(g)+e=\tau g+e.
$$

---

We already have

$$
\mathcal{F}_{1}(0,0)=0.
$$

Here, we obtain

$$
D_{h}\mathcal{F}_{1}(0,0)h=
\begin{array}{c}{\frac{1}{2}\Delta_{L}h+\frac{1}{1+\kappa n}\left(\kappa\operatorname{Tr}_{g}\operatorname{Ein}(g)\;h+\Lambda h-\kappa\langle\operatorname{Ein}(g),h\rangle g\right)}\\ {-\frac{(n-2)\kappa}{2(1+\kappa n)}\mathcal{L}_{g}\tau^{-1}d\langle\operatorname{Ein}(g),h\rangle,}\\ \end{array}
$$

thus,

$$
D_{h}\mathcal{F}_{1}(0,0)h=
\frac{1}{2}\Delta_{L}h+\frac{1}{1+\kappa n}\left(n\kappa\tau\;h+\Lambda h-\kappa\tau\mathrm{Tr}_{g}h\;g\right)-\frac{(n-2)\kappa}{2(1+\kappa n)}\nabla\nabla\mathrm{Tr}_{g}h.
$$

This differential motivates us to define the operator
(

$$
\begin{array}{r l r}{\mathcal{P}h}&{:=}&{\Delta_{L}h+\frac{2(n\kappa\tau+\Lambda)}{1+k n}h+\frac{\kappa}{n(1+\kappa n)}\Big((n-2)\Delta\operatorname{Tr}_{g}h-2n\tau\operatorname{Tr}_{g}h\Big)\;g}\\ &{=}&{(\Delta_{L}+2\kappa n\lambda+2\Lambda)h+\frac{\kappa}{n(1+\kappa n)}\Big((n-2)\Delta\operatorname{Tr}_{g}h-2n\tau\operatorname{Tr}_{g}h\Big)\;g.}\end{array}
$$

This respects the splitting S₂ = G ⊕ S˚<sub>2</sub>. In particular, if u is a function
on M and ˚h is a symmetric traceless 2-tensor field, we have

$$
\mathcal{S}_{2}=\mathcal{G}\oplus\mathring{\mathcal{S}}_{2}
$$

$$
\mathcal{P}(u g+\mathring{h})=\frac{1}{1+\kappa n}p(u)g+\mathring{P}(\mathring{h}),
$$

where

$$
p(u)=\left(1+2(n-1)\kappa\right)\Delta u+2\Lambda u,
$$

and

$$
\mathring{P}(\mathring{h})=\left[\Delta_{L}+2\kappa n\lambda+2\Lambda\right]\mathring{h}.
$$

If h = ug, we find

$$
h=u g
$$

$$
D_{h}\mathcal{F}_{1}(0,0)(u g)=\frac{1}{2}p(u)g-\frac{(n-2)n\kappa}{2(1+\kappa n)}\mathrm{Hess}u,
$$

˚
where Hess u is the traceless part of the Hessian of u. If h = ˚h is
traceless, we find
1

$$
h=\mathring{h}
$$

$$
D_{h}\mathcal{F}_{1}(0,0)(\mathring{h})=\frac{1}{2}\mathring{P}(\mathring{h}).
$$

Proposition 6.1. We assume κ 6= −<sub>n</sub><sup>1</sup>, −<sub>2(n1−1)</sub>. Let
()

$$
\kappa\ne-\frac{1}{n},-\frac{1}{2(n-1)}
$$

$$
\upsilon=-2\kappa\left(\frac{2(n-1)\Lambda}{1+2(n-1)\kappa}+n\lambda\right).
$$

If −2κnλ − 2Λ is not in the spectrum of ∆<sub>L</sub> + υ Tr(.)g with ADN<sub>κ</sub>
*conditions:*


$$
\mathrm{\it{I f}}-2\kappa n\lambda-2\Lambda
$$

$$
\Delta_{L}+\upsilon\mathrm{Tr}(.)g
$$

$\mathit{ADN}_{\kappa}$

$$
\left\{\begin{array}{l l}{B_{g}(h)-\frac{(n-2)\kappa}{2(1+\kappa n)}d\operatorname{Tr}_{g}h=0}&{\mathit{on}\;\partial M}\\ {h^{T}-\frac{1}{n-1}\operatorname{Tr}_{g^{T}}(h^{T})g^{T}=0}&{\mathit{on}\;\partial M}\\ {D H(g)h=0}&{\mathit{on}\;\partial M}\end{array}\right.,
$$ then D<sub>h</sub>F (0, 0) is an isomorphism from C<sup>k+2,α</sup>(M, S₂) into C<sup>k,α</sup>(M, S₂)×
C<sup>k+1,α</sup>(∂M, S₂)×C<sup>k+2,α</sup>(∂M, S˚<sub>2</sub>)×C<sup>k+1,α</sup>(∂M).

$$
D_{h}\mathcal{F}(0,0)
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

$$
C^{k,\alpha}(M,\mathcal{S}_{2})\times
C^{k+1,\alpha}(\partial M,\mathcal{S}_{2})\times C^{k+2,\alpha}(\partial M,\mathring{\mathcal{S}}_{2})\times C^{k+1,\alpha}(\partial M)
$$

Proof. It suffices to show that the map from C<sup>k+2,α</sup>(M)×C<sup>k+2,α</sup>(M, S˚<sub>2</sub>)
into C<sup>k,α</sup>(M)×C<sup>k,α</sup>(M, S˚<sub>2</sub>)×C<sup>k+1,α</sup>(∂M, S₂)×C<sup>k+2,α</sup>(∂M, S˚<sub>2</sub>)×C<sup>k+1,α</sup>(∂M)
given by


$$
C^{k+2,\alpha}(M)\times C^{k+2,\alpha}(M,\mathring{S}_2)
$$

$$
C^{k,\alpha}(M)\times C^{k,\alpha}(M,\hat{\mathcal{S}}_{2})\times C^{k+1,\alpha}(\partial M,\mathcal{S}_{2})\times C^{k+2,\alpha}(\partial M,\hat{\mathcal{S}}_{2})\times C^{k+1,\alpha}(\partial M)
$$

$$
(u,\mathring{h})\longrightarrow\left\{\begin{array}{ll}(p(u),\mathring{P}(\mathring{h}))&in M\\ B_g(h)-\frac{(n-2)\kappa}{2(1+\kappa n)}d\operatorname{Tr}_g h&on\partial M\\ h^T-\frac{1}{n-1}\operatorname{Tr}_{g^T}(h^T)g^T&on\partial M\\ DH(g)h&on\partial M\end{array}\right.,
$$

where h = ug + ˚h, is an isomorphism.

$$
h=u g+\mathring{h},
$$

In order to do so, we will show that the map
 ()

$$
(u,\mathring{h})\longrightarrow\left\{\begin{array}{l l}{\left(\frac{1}{1+2(n-1)\kappa}p(u),\mathring{P}(\mathring{h})\right)}&{\text{in}M}\\ {B_{g}(h)-\frac{(n-2)\kappa}{2(1+\kappa n)}d\operatorname{Tr}_{g}h}&{\text{on}\partial M}\\ {h^{T}-\frac{1}{n-1}\operatorname{Tr}_{g^{T}}(h^{T})g^{T}}&{\text{on}\partial M}\\ {D H(g)h}&{\text{on}\partial M}\end{array}\right.,
$$

is one. The operator

$$
h\longrightarrow\left\{\begin{array}{l l}{P(h):=\Delta_{L}h+2\kappa n\lambda h+2\Lambda h+\upsilon\operatorname{Tr}(h)g}&{\mathrm{in}M}\\ {B_{g}(h)-\frac{(n-2)\kappa}{2(1+\kappa n)}d\operatorname{Tr}_{g}h}&{\mathrm{on}\partial M}\\ {h^{T}-\frac{1}{n-1}\operatorname{Tr}_{g^{T}}(h^{T})g^{T}}&{\mathrm{on}\partial M}\\ {D H(g)h}&{\mathrm{on}\partial M}\\ \end{array}\right.,
$$

is clearly a Fredholm operator of index zero, like L<sub>c</sub>, by homotopy, it
is therefore an isomorphism since it has a trivial kernel. Moreover, for
any function u and any traceless symmetric two-tensor ˚h,

$$
L_{c},
$$

$$
\mathring{h},
$$

$$
P(u g+\mathring{h})=\frac{1}{1+2(n-1)\kappa}p(u)g+\mathring{P}(\mathring{h}),
$$

which proves the stated result.

Theorem 6.2. Let k ∈ N\{0}, α ∈ (0, 1), κ 6= −<sub>n</sub><sup>1</sup>, −<sub>2(n1−1)</sub> and Λ∈R.
Let g *be an Einstein metric such that* Ein(g) *is non-degenerate. Under*
*the assumptions of Proposition 6.1, we further assume that* −2κnλ−2Λ
is not in the spectrum of ∆<sub>H</sub> with Dirichlet condition. Then, for
every small e ∈ C<sup>k+2,α</sup>(M, S₂), for every conformal class [γ] close
to [g<sup>T</sup>] in [C<sup>k+2,α</sup>(∂M, S₂<sup>+</sup>)], and every function H close to H (g) in
C<sup>k+1,α</sup>(∂M, S₂), there exists a unique h close to zero in C<sup>k+2,α</sup>(M, S₂)
*such that*

 E*in*(g + h) = Ein(g) + e in M,

$k\in\mathbb{N}\backslash\{0\},\thinspace\alpha\in(0,1),\thinspace\kappa\neq-\frac{1}{n},-\frac{1}{2(n-1)}$

$$
\Lambda\in\mathbb{R}
$$

$$
-2\kappa n\lambda-2\Lambda
$$

$$
\Delta_{H}
$$

$$
e\in C^{k+2,\alpha}(M,\mathcal{S}_2)
$$

$$
\left[g^{T}\right]
$$

$$
H(g)
$$

$$
[C^{k+2,\alpha}(\partial M,S_{2}^{+})]
$$

$$
C^{k+2,\alpha}(M,\mathcal{S}_{2})
$$

$$
C^{k+1,\alpha}(\partial M,\mathcal{S}_{2})
$$

$$
\left\{\begin{array}{l l}{\operatorname{Ein}(g+h)=\operatorname{Ein}(g)+e}&{\mathit{in}M,}\\ {|(g+h)^{T}|^{\frac{-1}{n-1}}(g+h)^{T}=\gamma}&{\mathit{on}\partial M,}\\ {H(g+h)=\mathcal{H}}&{\mathit{on}\partial M,}\\ \end{array}\right.
$$

---

*Moreover, the map* (e, [γ], H) 7→ h *is smooth in a neighborhood of*
(0, [g<sup>T</sup>], H (g)) in a neighborhood of zero between the corresponding Ba-
*nach spaces.*

$$
(e,[\gamma],\mathcal{H})\mapsto h
$$

$$
(0,[g^{T}],H(g))
$$

Proof. From the hypotheses, D<sub>h</sub>F (0, 0) is an isomorphism. The preceding calculations and the implicit function theorem then imply that
for (e, γ, H) close to (0, γ, H) in their respective spaces, there exists h
close to zero in C<sup>k+2,α</sup>(M, S₂) such that

$$
D_{h}\mathcal{F}(0,0)
$$

$$
(e,\gamma,\mathcal{H})
$$

$$
(0,\gamma,\mathcal{H})
$$

$$
C^{k+2,\overset{\cdot}{\alpha}}(M,\mathcal{S}_{2})
$$

$$
\mathcal{F}(h,e)=(0,0,\gamma,\mathcal{H}).
$$

We now apply B<sub>g+h</sub> to the equation F₁(h, e) = 0, thus

$$
B_{g+h}
$$

$$
\mathcal{F}_{1}(h,e)=0
$$

$$
B_{g+h}\mathcal{F}_{1}(h,e)=-\mathcal{B}_{g+h}(E)-B_{g+h}\mathcal{L}_{g}\tau^{-1}\mathcal{B}_{g+h}(E)=0.
$$

Setting ω = τ<sup>−1</sup>B<sub>g+h</sub>(E), we then have that ω vanishes at the boundary
and
P ω := B L ω + τ ω = 0.

$$
\omega=\tau^{-1}\mathcal{B}_{g+h}(E)
$$

$$
\omega
$$

$$
P_{g+h}\omega:=B_{g+h}\mathcal{L}_{g}\omega+\tau\omega=0.
$$

But by hypothesis, the operator
1 1

$$
P_{g}=\frac{1}{2}(\Delta-\mathrm{Ric}_{g})+\tau=\frac{1}{2}(\Delta+\mathrm{Ric}_{g}+2\kappa n\lambda+2\Lambda)=\frac{1}{2}(\Delta_{H}+2\kappa n\lambda+2\Lambda)
$$

with Dirichlet boundary condition is injective, so if h is small, P<sub>g+h</sub>
remains injective, hence ω = 0.

$$
h
$$

$$
P_{g+h}
$$

$$
\omega=0
$$

## 7. Riemann-Christoffel Type Curvature

We would like, just as in [7], to show that the image of certain
Riemann-Christoffel type operators are submanifolds in C<sup>∞</sup>, in the
neighborhood of the metric g. We thus define:

$$
C^{\infty}
$$

$$
g
$$

$$
\mathcal{E}_{}{i n}\big(g\big)=\mathrm{Riem}\big(g\big)+g\textcircled{\wedge}\big(a\operatorname{Ric}\big(g\big)+b R\big(g\big)g+c g\big),
$$

where ∧© is the Kulkarni-Nomizu product ( [4] p. 47), and

$$
\textcircled{\bigotimes}
$$

$$
c=\frac{1+(n-2)a}{2(n-1)}\Lambda,\quad b=\frac{\kappa[1+a(n-2)]-a}{2(n-1)},\quad a\neq-\frac{1}{n-2}.
$$

We then obtain:

$$
\mathrm{Tr}_{g}\mathcal{E}\mathrm{in}(g)=[a(n-2)+1]\mathrm{Ein}(g).
$$

We define the Riemann-Christoffel type version of E in(g) by:

$$
\mathcal{E}i n(g)
$$

$$
[g^{-1}\mathcal{E}i n(g)]_{k l m}^{i}:=g^{i j}\mathcal{E}i n(g)_{j k l m}.
$$

Consider R₃<sup>1</sup>, the subspace of T₃₁ consisting of tensors satisfying:

$$
\mathcal{R}_{3}^{1}
$$

$$
\mathcal{T}_{3}^{1}
$$

$$
\tau_{i l m}^{i}=0,\;\tau_{k l m}^{i}=-\tau_{k m l}^{i},\;\tau_{k l m}^{i}+\tau_{m k l}^{i}+\tau_{l m k}^{i}=0.
$$

We define the Fŕechet space:

$$
C^{\infty}=\cap_{k\in\mathbb{N}}C^{k,\alpha},
$$

endowed with the family of seminorms {‖.‖<sub>k,α</sub>}k∈N.

$$
\left\{\left\|\cdot\right\|_{k,\alpha}\right\}_{k\in\mathbb{N}}.
$$

We then proceed similarly to [7] to prove that:

---

Theorem 7.1. *Under the conditions of Theorem 6.2, the image of the*
*map:*

$$
\begin{array}{l}{C^{\infty}(M,\mathcal{S}_{2})\quad\longrightarrow\quad C^{\infty}(M,\mathcal{R}_{3}^{1})\times[C^{\infty}(\partial M,S_{2}^{+})]\times C^{\infty}(\partial M,\mathcal{S}_{2})}\\ {h\quad\mapsto\quad\left\{\begin{array}{l l}{(g+h)^{-1}\mathcal{E}i n(g+h)-(g)^{-1}\mathcal{E}i n(g)}&{\mathit{in}M,}\\ {|(g+h)^{T}|^{-\frac{1}{n-1}}(g+h)^{T}}&{\mathit{on}\partial M,}\\ {H(g+h)}&{\mathit{on}\partial M,}\\ \end{array}\right.}\\ \end{array}
$$

is a smooth submanifold of a neighborhood of (0, [g<sup>T</sup>], H (g)).

[1] Z. An and L. H. Huang, Local structure Theory of Einstein manifolds with
boundary, arXiv: 2405.17577.
[2] M. T. Anderson, On boundary value problems for Einstein metrics, *Geom.*
*Topol.* 12 (2008), no. 4, 2009–2045. MR 2431014.
[3] A. Baldes, *Nonexistence of Riemannian metrics with prescribed Ricci tensor*,
Nonlinear problems in geometry (Mobile, Ala., 1985), Contemp. Math., vol. 51,
Amer. Math. Soc., Providence, RI, 1986, pp. 1–8. MR 848927 (87k:53085)
[4] A.L. Besse, *Einstein manifolds*, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge, vol. 10, Springer Verlag, Berlin, New York, Heidelberg, 1987.
[5] Ph. Delanöe, *Obstruction to prescribed positive Ricci curvature*, Pacific J.
Math. 148 (1991), no. 1, 11–15.
[6], *Local solvability of elliptic, and curvature, equations on compact man-*
*ifolds*, J. Reine Angew. Math. 558 (2003), 23–45. MR 1979181 (2004e:53054)
[7] E. Delay, *Etude locale d’oṕerateurs de courbure sur l’espace hyperbolique*, J.
Math. Pures Appli. 78 (1999), 389–430.
[8], *Study of some curvature operators in the neighbourhood of an asymp-*
*totically hyperbolic Einstein manifold*, Adv. in Math. 168 (2002), 213–224.
[9], *Inversion d’oṕerateurs de courbure au voisinage de la ḿetrique eucli-*
*diennne*, Bull. S.M.F, 145(3) (2017), p. 411-420,
[10], *Inversion d’oṕerateurs de courbures au voisinage d’une ḿetrique Ricci*
*parall`ele*, Annales de l’institut Fourier, Vol. 67 no. 2 (2017), p. 521-538,
[11], L<sup>p</sup> almost conformal isometries of Sub-Semi-Riemannian metrics and
*solvability of a Ricci equation*, Proc. Amer. Math. Soc. 146 (2018), 3499–3507.
[12] E. Delay and M. Herzlich, *Ricci curvature in the neighbourhood of rank-one*
*symmetric spaces*, J. Geom. Anal. 11 (2001), no. 4, 573–588.
[13] D. DeTurck, *Existence of metrics with prescribed ricci curvature : Local theory*,
Invent. Math. 65 (1981), 179–207.
[14], *Prescribing positive Ricci curvature on compact manifolds*, Rend. Sem.
Mat. Univ. Politec. Torino 43 (1985), no. 3, 357–369 (1986).
[15] Dennis DeTurck and Hubert Goldschmidt, *Metrics with prescribed Ricci cur-*
*vature of constant rank. I. The integrable case*, Adv. Math. 145 (1999), no. 1,
1–97.
[16] D.M. DeTurck and N. Koiso, *Uniqueness and nonexistence of metrics with*
*prescribed Ricci curvature*, Ann. Inst. H. Poincaŕe Anal. Non Lińeaire 1 (1984),
no. 5, 351–359.
[17] D.Gaskins,*On the Prescribed Ricci Curvature of Noncompact Homogeneous*
*Spaces with Two Isotropy Summands*, arXiv:2502.19251 [math.DG].
[18] C.R. Graham and J.M. Lee, *Einstein metrics with prescribed conformal infinity*
*on the ball*, Adv. Math. 87 (1991), 186–225.

$$
(0,[g^{T}],H(g))
$$

## References

---

[19] R. Hamilton, *The Ricci curvature equation*, Seminar on nonlinear partial differential equations (Berkeley, Calif., 1983), Math. Sci. Res. Inst. Publ., vol. 2,
Springer, New York, 1984, pp. 47–72. MR 765228 (86b:53040)
[20] A. Lichnerowicz, *Propagateurs et commutateurs en relativit´e ǵeńerale*, Pub.
Math. de l’IHES 10 (1961), 5–56.
[21] J. Lott, *Mean curvature flow in a Ricci flow background.* Comm. Math. Phys.,
313(2), (2012), 517–533.
[22] D. Mitrea, I. Mitrea,M. Mitrea and M. Taylor, *The Hodge–Laplacian: Bound-*
*ary Value Problems on Riemannian Manifolds*, Berlin, Boston: De Gruyter,
vol. 64, 2025. https://doi.org/10.1515/9783111481401
[23] A. Pulemotov, *Metrics with prescribed ricci curvature near the boundary of a*
*manifold*, Mathematische Annalen (2013), no. 357, 969–986.
[24] A. Pulemotov, *The Dirichlet problem for the prescribed Ricci curvature equa-*
*tion on cohomogeneity one manifolds*, Annali di Matematica Pura ed Applicata, 195 (2016), 1269–1286.
Laboratoire de Math´ematiques d’Avignon, Fac. des Sciences, F84916
Avignon, France
F.R.U.M.A.M. – CNRS Aix Marseille Universit´e– F13 331 Marseille,
France
*Email address*: Erwann.Delay@univ-avignon.fr
*URL*: https://erwanndelay.wordpress.com/