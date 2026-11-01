---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: The Yamabe Problem]

# The Yamabe Problem

> Source: https://www.ms.uky.edu/~hislop/papers/lee-thomas.pdf
> Fetched: 2026-10-09 09:02
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
  "source_url": "https://www.ms.uky.edu/~hislop/papers/lee-thomas.pdf",
  "metadata": {
    "provenance_urls": [
      "https://www.ms.uky.edu/~hislop/papers/lee-thomas.pdf"
    ],
    "search_origins": [
      {
        "source": "serper",
        "query": "Yamabe Green"
      },
      {
        "source": "tavily",
        "query": "Yamabe Green"
      }
    ]
  },
  "declared_files": []
}
```

## Source description

by JM LEE · 1987 · Cited by 1592 — Using the Green function for D, we define a " stereographic projection" from. M minus a point to a noncompact manifold M with zero scalar curvature. We then ...

## Retrieved source content

# THE YAMABE PROBLEM

# JOHN M. LEE AND THOMAS H. PARKER

# Contents

1. Introduction
2. Geometric and analytic preliminaries
3. The model case: the sphere
4. The variational approach
5. Conformal normal coordinates
6. Stereographic projections
7. The test function estimate
8. General relativity
9. Analysis on asymptotically flat manifolds
10. The positive mass theorem
11. Solution of the Yamabe problem
Appendix: Witten's proof
Bibliography

1. Introduction. Riemannian differential geometry originated in attempts to generalize the highly successful theory of compact surfaces. From the earliest days, conformal changes of metric (multiplication of the metric by a positive function) have played an important role in surface theory. For example, one consequence of the famous uniformization theorem of complex analysis is the fact that every surface has a conformal metric of constant (Gaussian) curvature. This provides a "standard model" for each homeomorphism class of surfaces, and reduces topological questions to differential geometric ones.

Life would be simple if the naive generalization of this theorem held in higher dimensions: every $n$-manifold would have a conformal metric of constant curvature, and questions in differential topology would be reduced to geometric questions about the constant-curvature models. However, it is easy to see that this cannot be true. In general the problem is highly overdetermined: the curvature tensor has on the order of $n^4$ independent components, while a conformal change of metric allows us to choose only one unknown function. For example, if $n \geqslant 4$, the Weyl tensor, formed from the components of the Riemannian curvature tensor, is conformally invariant and vanishes if and only if the metric is locally conformally equivalent to the Euclidean metric. From this point of view it seems natural instead to seek a

Received by the editors June 24, 1986.
1980 Mathematics Subject Classification. Primary 53A30; Secondary 35J20, 35J60.
Research of the first author supported in part by a research grant from the National Science Foundation.

©1987 American Mathematical Society
0273-0979/87 $1.00 + $.25 per page conformal change of metric that makes only the scalar curvature (the complete contraction of the curvature tensor) constant, for then we are looking for one unknown function to satisfy one condition. Thus we are led to:

The Yamabe Problem. Given a compact Riemannian manifold $(M,g)$ of dimension $n \geqslant 3$, find a metric conformal to $g$ with constant scalar curvature.

In 1960, H. Yamabe [Y] attempted to solve this problem using techniques of calculus of variations and elliptic partial differential equations. He claimed that every compact Riemannian $n$-manifold $M$ has a conformal metric of constant scalar curvature. Unfortunately, his proof contained an error, discovered in 1968 by Neil Trudinger [T]. Trudinger was able to repair the proof, but only with a rather restrictive assumption on the manifold $M$. In order to understand the restriction, let us describe Yamabe's approach.

Suppose $(M,g)$ is a compact Riemannian manifold of dimension $n \geqslant 3$ (which we will always assume is connected). Any metric conformal to $g$ can be written $\tilde{g} = e^{2f}g$, where $f$ is a smooth real-valued function on $M$. If $S$ and $\tilde{S}$ denote the scalar curvatures of $g$ and $\tilde{g}$, respectively, they satisfy the transformation law:

$$\tilde{S} = e^{-2f}\left(S + 2(n - 1)\Delta f - (n - 1)(n - 2)|\nabla f|^2\right),$$

in which $\Delta f$ denotes the Laplacian of $f$ and $\nabla f$ its covariant derivative, defined with respect to the metric $g$. This formula is considerably simplified if we make the substitution $e^{2f} = \varphi^{p-2}$, with $p = 2n/(n - 2)$ and $\tilde{g} = \varphi^{p-2}g$:

(1.1)

$$\tilde{S} = \varphi^{1-p}\left(4\frac{n-1}{n-2}\Delta\varphi + S\varphi\right).$$

NOTATION. Throughout this paper, we will use the following notations:

$$n = \dim M \geqslant 3; \quad p = \frac{2n}{n-2}, \quad a = 4\frac{n-1}{n-2}; \quad \square = a\Delta + S.$$

Thus $\tilde{g} = \varphi^{p-2}g$ has constant scalar curvature $\lambda$ iff $\varphi$ satisfies the Yamabe equation:

(1.2)

$$\square\varphi = \lambda\varphi^{p-1}.$$

This is a sort of "nonlinear eigenvalue problem." The analytic properties of the equation $\square\varphi = \lambda\varphi^q$ depend critically on the value of the exponent $q$: when $q = 1$, the equation is just the linear eigenvalue problem for $\square$. When $q$ is close to 1, as we will see in §4, its analytic behavior is quite similar to that of the linear case, and the problem is easily solved. When $q$ is very large, the methods based on linear theory break down altogether. It happens that the exponent $q = p - 1 = (n + 2)/(n - 2)$ that occurs in the Yamabe equation is precisely the critical value, below which the equation is easy to solve and above which it may be impossible. This accounts for the analytic complexity of the Yamabe problem.

Yamabe observed that equation (1.2) is the Euler-Lagrange equation for the functional

(1.3)

$$Q(\tilde{g}) = \frac{\int_M \tilde{S} dV_{\tilde{g}}}{\left(\int_M dV_{\tilde{g}}\right)^2/p},$$ where $\tilde{g}$ is allowed to vary over metrics conformally equivalent to $g$. To see this, observe that $Q$ can be written $Q(\tilde{g}) = Q(\varphi^{p-2}g) = Q_g(\varphi)$, where

$$Q_g(\varphi) = E(\varphi)/\|\varphi\|_p^2,$$

(1.4)

$$E(\varphi) = \int_M a |\nabla \varphi|^2 + S\varphi^2 dV_g, \quad \|\varphi\|_p = \left( \int_M |\varphi|^p dV_g \right)^{1/p}.$$

Then for any $\psi \in C^\infty(M)$, integration by parts yields

$$\frac{d}{dt} Q_g(\varphi + t\psi) \bigg|_{t=0} = \frac{2}{\|\varphi\|_p^2} \int_M \left(a\Delta\varphi + S\varphi - \|\varphi\|_p^{-p} E(\varphi)\varphi^{p-1}\right)\psi dV_g.$$

Thus $\varphi$ is a critical point of $Q_g$ if and only if it satisfies the Yamabe equation (1.2) with $\lambda = E(\varphi)/\|\varphi\|_p^p$.

Since by Hölder’s inequality $|\int_M S\varphi^2|$ is bounded by a multiple of $\|\varphi\|_p^2$, it follows easily that $Q_g$ (and thus $Q$) is bounded below. We set

(1.5) $$\lambda(M) = \inf \left\{ Q(\tilde{g}) : \tilde{g} \text{ conformal to } g \right\}$$

$$= \inf \left\{ Q_g(\varphi) : \varphi \text{ a smooth, positive function on } M \right\}.$$

This constant $\lambda(M)$ is an invariant of the conformal class of $(M,g)$, called the Yamabe invariant. Its value is central to the analysis of the Yamabe problem.

The solution of the Yamabe problem follows its historical development. It is summarized by three main theorems.

Trudinger’s modification of Yamabe’s proof worked whenever $\lambda(M) \leqslant 0$. In fact, he showed that there is a positive constant $\alpha(M)$ such that the proof works when $\lambda(M) < \alpha(M)$. Now it is easy to show (see §3) that $\lambda(M) \leqslant \lambda(S^n)$, where $S^n$ is the sphere with its standard metric. In 1976, Thierry Aubin [A2] extended Trudinger’s result by showing, in effect, that $\alpha(M) = \lambda(S^n)$ for every $M$. This established:

**THEOREM A** (YAMABE, TRUDINGER, AUBIN). The Yamabe problem can be solved on any compact manifold $M$ with $\lambda(M) < \lambda(S^n)$, where $S^n$ is the sphere with its standard metric.

This result shifts the focus of the proof from analysis to the problem of understanding the essentially geometric invariant $\lambda(M)$. The obvious approach to showing that $\lambda(M) < \lambda(S^n)$ is to find a “test function” $\varphi$ with $Q_g(\varphi) < \lambda(S^n)$. Aubin [A2] sought such a function compactly supported in a small neighborhood of a point $P \in M$. By carefully studying the local geometry of $M$ near $P$ in normal coordinates, he was able to construct such test functions in many cases, proving the following theorem.

**THEOREM B** (AUBIN). If $M$ has dimension $n \geqslant 6$ and is not locally conformally flat then $\lambda(M) < \lambda(S^n)$.

The remaining cases are more difficult because the local conformal geometry does not contain sufficient information to conclude that $\lambda(M) < \lambda(S^n)$. These cases thus require the construction of a global test function. This was done by Richard Schoen [S] in 1984. His theorem completes the solution of the Yamabe problem.

---

THEOREM C (SCHOEN). If M has dimension 3, 4, or 5, or if M is locally conformally flat, then $\lambda(M) < \lambda(S^n)$ unless M is conformal to the standard sphere.

Schoen’s proof introduced two important new ideas. First, he recognized the key role of the Green function for the operator $ \Box $; in fact, his test function was simply the Green function with its singularity smoothed out. Second, he discovered the unexpected relevance of the positive mass theorem of general relativity, which had recently been proved in dimensions 3 and 4 by Schoen and S.-T. Tau [SY1, SY2, SY4]. A curious feature of Schoen’s proof is that it works only in the cases not covered by Aubin’s theorem.

The proof of Theorem C actually requires an $ n$-dimensional version (as yet unpublished) of the positive mass theorem, which was announced by Schoen in [S]. The 5-dimensional case appears to be a straightforward generalization of the 4-dimensional proof in [SY2]. The higher-dimensional case is more difficult. However, for $ n \geqslant 6 $ the result is needed only for locally conformally flat manifolds; Schoen and Yau [SY6] have recently given an alternate proof for this case (see §10).

The solution of the Yamabe problem marks a milestone in the development of the theory of nonlinear partial differential equations. Semilinear equations of the form (1.2) with critical exponent arise in many contexts and have long been studied by analysts. This is the first time that such an equation has been completely solved.

The aim of the present paper is to provide a unified expository account of the proof of the Yamabe theorem, presenting for the first time the complete solution in one place. This account should be accessible to anyone familiar with enough differential geometry to feel comfortable with tensors, covariant derivatives, and normal coordinates; and enough analysis to follow arguments involving Sobolev and Hölder spaces and basic elliptic regularity theory for the Laplace operator.

The proof we present is self-contained (except for a central step in the positive mass theorem), and incorporates several improvements over the proofs currently available in the literature. Most importantly, we show how to recast the local proof of Aubin and the global proof of Schoen in a single framework.

The key simplification is achieved by introducing a special coordinate system, called “conformal normal coordinates”. These are analogous to geodesic normal coordinates on a Riemannian manifold, and greatly simplify local analysis on conformal manifolds. (A related coordinate system was invented by Robin Graham [G] to study conformal invariant theory.)

Using the Green function for $ \Box $, we define a “stereographic projection” from $ M $ minus a point to a noncompact manifold $ \hat{M} $ with zero scalar curvature. We then construct a test function on $ \hat{M} $ whose Yamabe quotient is very close to that of the sphere. Conformal normal coordinates allow us to obtain a precise estimate of this Yamabe quotient. This shows that $\lambda(M) < \lambda(S^n)$ provided a certain quantity called the “distortion coefficient” is positive. This coefficient measures the average behavior of the metric on $ \hat{M} $ near infinity. In the case of Theorem B, it is readily computed from the local conformal geometry of $ M, $ while in the case of Theorem C its positivity follows from the positive mass theorem.

This approach, we feel, sheds considerable light on the relationship between Theorems B and C, and eliminates the need for the "delicate perturbation argument" that Schoen used to handle dimensions 4 and 5. It also shows that the expansion of the Green function contains all the information needed to prove that $\lambda(M) < \lambda(S^n)$.

In §2 of this paper, we recall the notation and background material from differential geometry and analysis that we will be using throughout the paper. §3 is a discussion of the "model case" for the Yamabe problem, the sphere with its standard metric. In §4, we complete the analytic part of the proof by showing that the problem can be solved if $\lambda(M) < \lambda(S^n)$.

Conformal normal coordinates are introduced in §5, and used to give a very simple proof of Aubin's theorem. In §6, we define a stereographic projection for a compact manifold with positive Yamabe invariant, and derive the asymptotic expansion of its metric explicitly to high order. In §7 we construct a test function on $\hat{M}$ and compute its Yamabe quotient.

§§8, 9, and 10 give a brief treatment of the positive mass theorem. In §8, we introduce the physicists' notion of mass of an asymptotically flat manifold, and describe the physical motivation for the positive mass and positive action conjectures. §9 discusses some analytic tools for asymptotically flat manifolds, and §10 sketches a proof of the $n$-dimensional positive mass theorem. Finally, in §11 we complete the proof of the Yamabe theorem.

We are indebted to Karen Uhlenbeck, who first introduced us to the Yamabe problem, and to David Jerison, whose ideas about the expansion of the Green function were very helpful in early conversations. We would also like to thank Jean-Pierre Bourguignon for helpful comments on the manuscript.

2. Geometric and analytic preliminaries. In this section we collect some notations and well-known facts from differential geometry and the theory of linear partial differential equations on manifolds. Most of the results stated here without proof can be found in [KN, A3, or GT].

Geometric notations. We use standard index notation for tensors. If $g_{jk}$ are the components of the metric tensor with respect to a coordinate system $\{x^i\}$, $g_{jk}$ and its inverse $g^{jk}$ are used to raise and lower indices: $T^l_k = g^{jl}T_{jk}$. The metric extends to an inner product on tensors of any type: for example, the norm of the 2-tensor $T$ with components $T_{jk}$ is $|T|^2 = T_{jk}T^{jk} = g^{jl}g^{km}T_{jk}T_{lm}$.

Covariant differentiation is denoted by $\nabla$. If $f$ is a function on $M$, its covariant derivative is the 1-tensor $\nabla f$ whose components we will write $f_j$. The $m$th covariant derivative of $f$ is the $m$-tensor $\nabla^m f$, with components $f_{i_1 i_2 \cdots i_m}$. If $T$ is a tensor, indices of $\nabla^m T$ that result from differentiation will be separated by a comma: for example, if $T_{jk}$ are the components of a 2-tensor $T$ as above, then the components of $\nabla^2 T$ are denoted by $T_{jk,lm}$.

The Euclidean volume form $dx^1 \wedge \cdots \wedge dx^n$ on $\mathbf{R}^n$ will be denoted by $dx$. The standard volume form on the unit $(n-1)$-sphere in $\mathbf{R}^n$ will be denoted by $d\omega$, and we write $d\omega_r = r^{n-1} d\omega$ for the volume form on the sphere $S_r$ of radius $r$. We let $\omega$ denote the volume of the unit sphere, and $\omega_r = r^{n-1}\omega$. If $g$ is a Riemannian metric, $dV_g$ denotes its Riemannian density, which is defined whether or not $M$ is oriented. In local coordinates, $dV_g = (\det g)^{1/2}|dx|$.

The divergence operator is the formal adjoint $\nabla^*\omega = -\omega_i$. On a compact manifold with boundary it satisfies the divergence theorem

$$\int_M \nabla^*\omega dV_g = -\int_{\partial M} \omega(N) dV_{\tilde{g}}$$

where $\tilde{g}$ is the induced metric on $\partial M$ and $N$ is the outward unit normal. (If $M$ is oriented this is just Stokes' theorem. If not, it follows from Stokes' theorem on the oriented double cover of $M$.) The Laplacian is the second-order differential operator $\Delta$ given on functions by

(2.1) $$\Delta u = \nabla^*\nabla u = -(\det g)^{-1/2}\partial_i\left(g^{ij}(\det g)^{1/2}\partial_ju\right).$$

On a compact manifold without boundary the divergence theorem yields the "integration by parts" formula

$$\int_M \langle\nabla v,\nabla u\rangle dV_g = \int_M v\Delta u dV_g.$$

The Riemannian curvature tensor is the tensor with components $R_{ijkl}$, computed in a coordinate system $\{x^i\}$ by:

$$R_{ijkl} = \left(R(\partial_k,\partial_l)\partial_j,\partial_i\right),$$

where $R$ is the curvature operator $R(V,W) = [\nabla_V,\nabla_W] - \nabla_{[V,W]}$. It satisfies the Ricci identity

(2.2) $$\omega_{j,kl} - \omega_{j,lk} = R^i_{jkl}\omega_i$$

for any one-form $\omega_j dx^j$, and the Bianchi identities:

(2.3) $$R_{ijkl} + R_{iklj} + R_{iljk} = 0, \quad R_{ijkl,m} + R_{ijlm,k} + R_{ijmk,l} = 0.$$

The Ricci tensor is the contraction $R_{jl} = R^k_{jkl}$ of the curvature tensor, and the scalar curvature is the trace $S = R_j^j$ of the Ricci tensor. $M$ is said to be Einstein if its Ricci tensor is a scalar multiple of the metric, or equivalently if the traceless Ricci tensor $B_{ij} = R_{ij} - (S/n)g_{ij}$ vanishes. Contracting the second equation in (2.3) on the indices $i$, $k$ and again on $j$, $l$, we obtain:

(2.4) $$S_{,m} - 2R^i_{m,i} = 0.$$

It follows that an Einstein manifold has constant scalar curvature.

The remaining components of the curvature tensor constitute the Weyl tensor $W$, with components:

$$W_{ijkl} = R_{ijkl} - \frac{1}{n-2}\left(R_{ik}g_{jl} - R_{il}g_{jk} + R_{jl}g_{ik} - R_{jk}g_{il}\right)$$

$$+ \frac{S}{(n-1)(n-2)} \left(g_{ik}g_{jl} - g_{il}g_{jk}\right).$$

---

(This formula is chosen so that the trace of $W$ on any pair of indices vanishes. $W$ vanishes identically if $n = 3$.) Using the definitions of $W$ and $B$, we can write the curvature tensor as a sum of three parts:

$$R_{ijkl} = W_{ijkl} + \frac{1}{n-2}\left(B_{ik}g_{jl} - B_{il}g_{jk} + B_{jl}g_{ik} - B_{jk}g_{il}\right)$$

$$+ \frac{S}{n(n-1)}\left(g_{ik}g_{jl} - g_{il}g_{jk}\right).$$

In particular, if $W = 0$ and $B = 0$, the curvature tensor is completely determined by the (constant) scalar curvature $S$, and $M$ is said to have constant curvature. It is well known that a complete, simply connected manifold of constant curvature is isometric to $\mathbf{R}^n$, $S^n$, or $n$-dimensional hyperbolic space.

If $\tilde{g} = e^{2f}g$ is a metric conformal to $g$, one can compute the components of the curvature tensor $\tilde{R}$ of $\tilde{g}$ in terms of those of the curvature of $g$. The results we will need are the transformation laws for the Ricci and scalar curvatures:

(2.5) $$\tilde{R}_{jk} = R_{jk} - (n-2)f_{jk} + (n-2)f_jf_k + (\Delta f - (n-2)f_i f^i)g_{jk};$$

(2.6) $$\tilde{S} = e^{-2f}\left(S + 2(n-1)\Delta f - (n-1)(n-2)f_i f^i\right).$$

As in the introduction, this can be rewritten in the form (1.1). One computes also that the Weyl tensor is conformally invariant: $\tilde{W}_{jkl}^i = W_{jkl}^i$.

A Riemannian manifold $M$ is said to be locally conformally flat if it is locally conformal to Euclidean space. It is a classical result (see for example [E, §28]) that for $n \geqslant 4$ the Weyl tensor vanishes identically if and only if $M$ is locally conformally flat.

The operator $\Box = a\Delta + S$, where $a = 4(n-1)/(n-2)$, is called the conformal Laplacian. It is conformally invariant in the following sense. If $\tilde{g} = \varphi^{p-2}g$ (with $p = 2n/(n-2)$) is a metric conformal to $g$, and $\Box$ is similarly defined with respect to $\tilde{g}$, then computing $\tilde{\Delta}$ in terms of $\Delta$ and using the transformation law (1.1) for scalar curvature, one finds that

(2.7) $$\tilde{\Box}(\varphi^{-1}u) = \varphi^{1-p}\Box u.$$

Analytic preliminaries. Suppose $P$ is a linear partial differential operator on a manifold $M$. If $u$ and $f$ are locally integrable functions on $M$, we say $u$ is a weak (or distribution) solution to the equation $Pu = f$ if, for every smooth compactly supported function $\varphi$,

$$\int_M uP^*\varphi dV_g = \int_M f\varphi dV_g,$$

in which $P^*$ is the formal adjoint of $P$, obtained from $P$ by formally integrating by parts. (In particular, $\Delta^* = \Delta$.) There are many function spaces used in solving differential equations; a nonlinear problem such as the Yamabe problem requires the use of a number of them. Therefore, we begin by defining the spaces we will be using.

---

If $q \geqslant 1$, the Lebesgue space $L^q(M)$ is the set of locally integrable functions $u$ on $M$ for which the norm

$$\|u\|_q = \left( \int_M |u|^q dV_g \right)^{1/q}$$

is finite.

If in addition $k$ is a nonnegative integer, the Sobolev space $L^q_k(M)$ is the set of $u \in L^q(M)$ such that $Pu = f \in L^q(M)$ (in the weak sense) whenever $P$ is a smooth differential operator of order $\leq k$. We define the Sobolev norm $\|\|_{q,k}$ on $L^q_k(M)$ by:

$$\|u\|_{q,k} = \left( \sum_{i=0}^{k} \int_M |\nabla^i u|^q dV_g \right)^{1/q}.$$

The space $C^k(M)$ is the set of $k$ times continuously differentiable functions on $M$, for which the norm

$$\|u\|_{C^k} = \sum_{i=0}^{k} \sup_M |\nabla^i u|$$

is finite. Then the Hölder space $C^{k,\alpha}(M)$ is defined for $0 < \alpha < 1$ as the set of $u \in C^k(M)$ for which the norm

$$\|u\|_{C^{k,\alpha}} = \|u\|_{C^k} + \sup_{x,y} \frac{|\nabla^k u(x) - \nabla^k u(y)|}{|x-y|^\alpha}$$

is finite, where the supremum is over all $x \neq y$ such that $y$ is contained in a normal coordinate neighborhood of $x$, and $\nabla^k u(y)$ is taken to mean the tensor at $x$ obtained by parallel transport along the radial geodesic from $x$ to $y$. As usual, $C^\infty(M)$ and $C_c^\infty(M)$ denote the spaces of smooth functions and smooth compactly supported functions on $M$, respectively. We note that if $M$ is complete, $C_c^\infty(M)$ is dense in $L^q_k(M)$.

The relations among these spaces are expressed in the following theorems.

THEOREM 2.1 (SOBOLEV EMBEDDING THEOREMS FOR $R^n$).

(a) Suppose

$$\frac{1}{r} = \frac{1}{q} - \frac{k}{n}.$$

Then $L^q_k(R^n)$ is continuously embedded in $L^r(R^n)$. In particular, for $q = 2$, $k = 1$, $r = p = 2n/(n-2)$, we have the following Sobolev inequality:

(2.8)

$$\|\varphi\|_p^2 \leqslant \sigma_n \int_{\mathbf{R}^n} |\nabla\varphi|^2 dx, \quad \varphi \in L_1^2(\mathbf{R}^n).$$

We will call the smallest such constant $\sigma_n$ the $n$-dimensional Sobolev constant.

(b) Suppose $0 < \alpha < 1$, and

$$\frac{1}{q} \leqslant \frac{k-\alpha}{n}.$$

Then $L^q_k(R^n)$ is continuously embedded in $C^\alpha(\mathbf{R}^n)$. □

---

We can transfer these results to a compact manifold $M$ by covering $M$ with small coordinate patches, applying the above theorems in normal coordinates, and summing the results with a partition of unity. The general results are expressed in the following theorem.

THEOREM 2.2 (SOBOLEV EMBEDDING THEOREMS FOR COMPACT MANIFOLDS). Suppose $M$ is a compact Riemannian manifold of dimension $n$ (possibly with $C^1$ boundary).

(a) If

$$\frac{1}{r} \geqslant \frac{1}{q} - \frac{k}{n},$$

then $L_k^q(M)$ is continuously embedded in $L'(M)$.

(b) (RELLICH-KONDRAKOV THEOREM) Suppose strict inequality holds in (a). Then the inclusion $L_k^q(M) \subset L'(M)$ is a compact operator.

(c) Suppose $0 < \alpha < 1$, and

$$\frac{1}{q} \leqslant \frac{k - \alpha}{n}.$$

Then $L_k^q(M)$ is continuously embedded in $C^\alpha(M)$. □

It is an important fact, due to Aubin, that in a certain sense the Sobolev inequality holds with the same constant on any compact manifold $M$. We present here a simple proof of this result. The technique is typical of the proofs of Theorem 2.2.

THEOREM 2.3 (AUBIN [A1]). Let $M$ be a compact Riemannian manifold with metric $g$, $p = 2n/(n-2)$, and let $\sigma_n$ be the best Sobolev constant defined in Theorem 2.1(a). Then for every $\varepsilon > 0$ there exists a constant $C_\varepsilon$ such that for all $\varphi \in C^\infty(M)$,

$$\|\varphi\|_p^2 \leqslant (1 + \varepsilon)\sigma_n \int_M |\nabla\varphi|^2 dV_g + C_\varepsilon \int_M \varphi^2 dV_g.$$

PROOF. Fix $\varepsilon > 0$. Around each point $P \in M$ we can choose a neighborhood $U$ such that, in normal coordinates on $U$, the eigenvalues of $g_{jk}$ are between $(1 + \varepsilon)^{-1}$ and $(1 + \varepsilon)$, and furthermore $dV_g = fdx$ where $(1 + \varepsilon)^{-1} < f < (1 + \varepsilon)$. Choose a finite subcover $\{U_i\}$ and a subordinate partition of unity, which we may write as $\{\alpha_i^2\}$, where $\alpha_i \in C^\infty(M)$ and $\sum \alpha_i^2 = 1$. Then we have

$$\|\varphi\|_p^2 = \|\varphi^2\|_{p/2} = \left\| \sum_i \alpha_i^2 \varphi^2 \right\|_{p/2} \leqslant \sum_i \left(\int_M |\alpha_i\varphi|^p dV_g\right)^2/p$$

$$\leqslant (1 + \varepsilon)^{2/p} \sum_i \left(\int_{U_i} |\alpha_i\varphi|^p dx\right)^2/p.$$

---

The Sobolev inequality on $R^n$ (2.8), together with our estimates on the deviation of $g$ and $dV_g$ from the Euclidean metric, imply

$$\left( \int_{U_i} |\alpha_i \varphi|^p dx \right)^2/p \leqslant \sigma_n \int_{U_i} |\nabla(\alpha_i \varphi)|_0^2 dx,$$

$$\leqslant (1 + \varepsilon)^2 \sigma_n \int_{U_i} |\nabla(\alpha_i \varphi)|^2 dV_g,$$

where $|_0$ represents the Euclidean metric in normal coordinates. Furthermore,

$$|\nabla(\alpha_i \varphi)|^2 = \alpha_i^2 |\nabla \varphi|^2 + 2\alpha_i \varphi \langle \nabla \alpha_i, \nabla \varphi \rangle + \varphi^2 |\nabla \alpha_i|^2$$

$$\leqslant (1 + \varepsilon) \alpha_i^2 |\nabla \varphi|^2 + (1 + \varepsilon^{-1}) \varphi^2 |\nabla \alpha_i|^2;$$

the last line follows from the Cauchy-Schwartz inequality and the inequality $2ab < \varepsilon a^2 + \varepsilon^{-1} b^2$. Thus for $\varepsilon$ small,

$$\|\varphi\|_p^2 \leqslant (1 + 4\varepsilon) \sigma_n \sum_i \int_{U_i} \alpha_i^2 |\nabla \varphi|^2 dV_g + C_\varepsilon \sum_i \int_{U_i} \varphi^2 |\nabla \alpha_i|^2 dV_g$$

$$\leqslant (1 + 4\varepsilon) \sigma_n \int_M |\nabla \varphi|^2 dV_g + C'_\varepsilon \int_M \varphi^2 dV_g.$$

Next we turn to the analysis of the Laplace operator $\Delta$.

THEOREM 2.4 (LOCAL ELLIPTIC REGULARITY). Suppose $\Omega$ is an open set in $R^n$, $\Delta$ is the Laplacian with respect to any metric on $\Omega$, and $u \in L^{1}_{\text{loc}}(\Omega)$ is a weak solution to $\Delta u = f$.

(a) If $f \in L^{q}(\Omega)$, then $u \in L^{q+2}(K)$ for any compact set $K \subseteq \Omega$, and if $u \in L^{q}(\Omega)$ then

$$\|u\|_{L^{q+2}(K)} \leqslant C\left(\|\Delta u\|_{L^{q}(\Omega)} + \|u\|_{L^{q}(\Omega)}\right).$$

(b) (Schauder estimates). If $f \in C^{k,\alpha}(\Omega)$, then $u \in C^{k+2,\alpha}(K)$ for any compact subset $K \subseteq \Omega$, and if $u \in C^{\alpha}(\Omega)$ then

$$\|u\|_{C^{k+2,\alpha}(K)} \leqslant C\left(\|\Delta u\|_{C^{k,\alpha}(\Omega)} + \|u\|_{C^{\alpha}(\Omega)}\right).$$

By a procedure similar to that mentioned above, these results can be transferred to a compact manifold.

THEOREM 2.5 (GLOBAL ELLIPTIC REGULARITY). Let $M$ be a compact Riemannian manifold, and suppose $u \in L^{1}_{\text{loc}}(M)$ is a weak solution to $\Delta u = f$.

(a) If $f \in L^{q}(M)$, then $u \in L^{q+2}(M)$, and

$$\|u\|_{q,k+2} \leqslant C\left(\|\Delta u\|_{q,k} + \|u\|_{q}\right).$$

(b) If $f \in C^{k,\alpha}(M)$, then $u \in C^{k+2,\alpha}(M)$, and

$$\|u\|_{C^{k+2,\alpha}} \leqslant C\left(\|\Delta u\|_{C^{k,\alpha}} + \|u\|_{C^{\alpha}}\right).$$

THEOREM 2.6 (STRONG MAXIMUM PRINCIPLE). Suppose $h$ is a nonnegative, smooth function on a connected manifold $M$, and $u \in C^{2}(M)$ satisfies $(\Delta + h)u \geqslant 0$. If $u$ attains its minimum $m \leqslant 0$, then $u$ is constant on $M$.

---

PROPOSITION 2.7 (WEAK REMOVABLE SINGULARITIES THEOREM). Let U be an open set in M and P ∈ U. Suppose u is a weak solution of ($\Delta + h$)u = 0 on U - {P}, with h ∈ L^{n/2}(U) and u ∈ L^q(U) for some q > p/2 = n/(n-2). Then u satisfies ($\Delta + h$)u = 0 weakly on all of U.

PROOF. We need to show that

$$\int_U \left(u\Delta\varphi + hu\varphi\right) dV_g = 0$$

for any $\varphi \in C_c^\infty(U)$. Choose $\alpha \in C_c^\infty(U)$ with support in a ball $B_R(P)$ of small radius R around P, such that $\alpha \equiv 1$ in $B_{R/2}(P)$, and define $\alpha_\epsilon(x) = \alpha(x/\epsilon)$ in normal coordinates around P. Then $\alpha_\epsilon$ is supported in $B_{\epsilon R}(P)$. Since $(1 - \alpha_\epsilon)\varphi$ is compactly supported in U - {P} and ($\Delta + h$)u = 0 there,

$$\int_U \left(u\Delta\varphi + hu\varphi\right) dV_g = \int_U \left(u\Delta\left(\alpha_\epsilon\varphi\right) + hu\alpha_\epsilon\varphi\right) dV_g.$$

We will show that the right-hand side goes to zero as $\varepsilon \to 0$.

Note that hu is integrable by Hölder’s inequality, and so the second term above goes to zero as the support of $\alpha_\epsilon$ shrinks. As for the first term, we have

$$\Delta\left(\alpha_\epsilon\varphi\right) = \varphi\Delta\alpha_\epsilon - 2\left\langle\nabla\alpha_\epsilon,\nabla\varphi\right\rangle + \alpha_\epsilon\Delta\varphi.$$

It is easy to check that $|\nabla\alpha_\epsilon| \leqslant C/\varepsilon$ and $|\Delta\alpha_\epsilon| \leqslant C/\varepsilon^2$. Therefore, if $q^{-1} + r^{-1} = 1,$

$$\left|\int_U u\Delta\left(\alpha_\epsilon\varphi\right) dV_g\right| \leqslant C\varepsilon^{-2}\int_B_{\epsilon R}|u|dV_g$$

$$\leqslant C\varepsilon^{-2}\|u\|_q\left(\int_B_{\epsilon R}dV_g\right)^{1/r}$$

$$\leqslant C'\varepsilon^{-2+n/r}\|u\|_q.$$

Since $q > p/2$ implies $n/r > 2$, this goes to zero as $\varepsilon \to 0$. □

Note that the example $u = r^{2-n}$ on Euclidean space shows that the hypothesis $q > p/2$ cannot be improved.

THEOREM 2.8 (EXISTENCE OF THE GREEN FUNCTION). Suppose M is a compact Riemannian manifold of dimension n ≥ 3, and h is a strictly positive smooth function on M. For each P ∈ M, there exists a unique smooth function $\Gamma_P$ on M - {P}, called the Green function for $\Delta + h$ at P, such that ($\Delta + h$)$\Gamma_P = \delta_P$ in the distribution sense, where $\delta_P$ is the Dirac measure at P. □

3. The model case: the sphere. The analysis of the Yamabe equation (1.2) depends upon a precise understanding of the model case of the sphere $S^n$. In this section we will describe the solution to the Yamabe problem on $S^n$ and prove that the infimum of the Yamabe functional (1.3) is realized by the standard metric on the sphere. We will also show how this leads to the sharp form of the Sobolev inequality on $R^n$. Using the extremals for this inequality we will show that $\lambda(M) \leqslant \lambda(S^n)$ for any compact manifold M.

---

Let $P = (0, \ldots, 0, 1)$ be the north pole on $S^n \subset R^{n+1}$. Stereographic projection $\sigma$: $S^n - \{P\} \rightarrow R^n$ is defined by $\sigma(\zeta^1, \ldots, \zeta^n, \xi) = (x^1, \ldots, x^n)$ for $(\zeta, \xi) \in S^n - \{P\}$, where

$$x^j = \zeta^j / (1 - \xi).$$

It is easy to verify that $\sigma$ is a conformal diffeomorphism. In fact, if $\bar{g}$ is the standard metric on $S^n$, and $ds^2$ the Euclidean metric on $R^n$, then under $\sigma$, $\bar{g}$ corresponds to

$$\rho^*\bar{g} = 4(|x|^2 + 1)^{-2} ds^2,$$

where $\rho$ denotes $\sigma^{-1}$. This can be written as $4u_1^{p-2} ds^2$, where

(3.1) $$u_1(x) = \left(|x|^2 + 1\right)^{(2-n)/2}.$$

By means of stereographic projection, it is simple to write down conformal diffeomorphisms of the sphere. The group of such diffeomorphisms is generated by the rotations, together with maps of the form $\sigma^{-1}\tau_v \sigma$ and $\sigma^{-1}\delta_\alpha \sigma$, where $\tau_v, \delta_\alpha$: $R^n \rightarrow R^n$ are respectively translation by $v \in R^n$:

$$\tau_v(x) = x - v,$$

and dilation by $\alpha > 0$;

$$\delta_\alpha(x) = \alpha^{-1}x.$$

The spherical metric on $R^n$ transforms under dilations to

(3.2) $$\delta_\alpha^*\rho^*\bar{g} = 4u_\alpha^{p-2} ds^2,$$

where $u_\alpha(x) = \left(\frac{|x|^2 + \alpha^2}{\alpha}\right)^{(2-n)/2}.$

There is an obvious metric of constant scalar curvature on the sphere, namely the standard metric. It is an important fact that this metric in fact minimizes the Yamabe functional $Q$ (see Theorem 3.2 below). This result is due originally to Aubin [A1], and independently to G. Talenti [Ta]. We will give a simpler proof, due to Karen Uhlenbeck and Morio Obata.

First we note that the infimum $\lambda(S^n)$ is actually attained by a smooth metric $g$ in the conformal class of the standard metric $\bar{g}$. This will be proved later in §4 (Proposition 4.6). This extremal metric $g$ is thus a metric on $S^n$, conformal to the standard one, which has constant scalar curvature. The following proposition shows that such a metric must be the standard one (up to a conformal diffeomorphism and a constant scale factor). Our proof is a simplification of Obata’s original argument. (The last step was improved following a suggestion of Roger Penrose.)

PROPOSITION 3.1 (OBATA [O]). If $g$ is a metric on $S^n$ that is conformal to the standard metric $\bar{g}$ and has constant scalar curvature, then up to a constant scale factor, $g$ is obtained from $\bar{g}$ by a conformal diffeomorphism of the sphere.

PROOF. We begin by showing that $g$ is Einstein. Considering the given metric $g$ as “background” metric on the sphere, we can write $\bar{g} = \varphi^{-2} g$, where $\varphi \in C^\infty(S^n)$ is strictly positive. Making the substitution $e^{2f} = \varphi^{-2}$ in the transformation law (2.5) for the Ricci tensor, we obtain:

$$\bar{R}_{jk} = R_{jk} + \varphi^{-1}\left((n-2)\varphi_{jk}-(n-1)\frac{\varphi_i\varphi^i}{\varphi}g_{jk}-\Delta\varphi g_{jk}\right),$$

in which the covariant derivatives and Laplacian are to be taken with respect to $g$, not with respect to the standard metric $\bar{g}$. If $B_{jk} = R_{jk}-(S/n)g_{jk}$ represents the traceless Ricci tensor, then since $\bar{g}$ is Einstein,

(3.3) $$0 = \bar{B}_{jk} = B_{jk}+(n-2)\varphi^{-1}\left(\varphi_{jk}+(1/n)\Delta\varphi g_{jk}\right).$$

Since the scalar curvature $S$ is constant, the contracted Bianchi identity (2.4) implies that the divergence $R^{i}_{m,i}$ of the Ricci tensor vanishes identically, and thus so also does $B^{i}_{m,i}$. Because $B_{jk}$ is traceless, integration by parts gives

(3.4) $$\int_{S^n} \varphi\left|B\right|^2 dV_g = \int_{S^n} \varphi B_{jk} B^{jk} dV_g$$

$$= -(n-2)\int_{S^n} B^{jk}\left(\varphi_{jk}+\frac{1}{n}\Delta\varphi g_{jk}\right) dV_g$$

$$= -(n-2)\int_{S^n} B^{jk}\varphi_{jk} dV_g$$

$$= (n-2)\int_{S^n} B^{jk},_k \varphi_j dV_g = 0.$$

Thus $B_{jk}$ must be identically zero, and so $g$ is Einstein.

Since $g$ is conformal to the standard metric $\bar{g}$ on the sphere, which is locally conformally flat, we have $W=0$ as well as $B=0$. As noted in §2, this implies that $g$ has constant curvature, and so $(S^n,g)$ is isometric to a standard sphere. The isometry is the desired conformal diffeomorphism. □

Combining Propositions 3.1 and 4.6, we obtain the complete solution to the Yamabe problem on the sphere:

**Theorem 3.2.** The Yamabe functional (1.3) on $(S^n,\bar{g})$ is minimized by constant multiples of the standard metric and its images under conformal diffeomorphisms. These are the only metrics conformal to the standard one on $S^n$ that have constant scalar curvature. □

**The Sobolev inequality.** The above theorem is closely related to the Sobolev inequality (2.8) on $\mathbf{R}^n$. Since the infimum of the Yamabe functional on the sphere is conformally invariant, stereographic projection converts the Yamabe problem on $S^n$ to an equivalent problem on $\mathbf{R}^n$, as follows.

First it is useful to observe that the restriction to smooth positive test functions in the definition (1.5) of $\lambda(M)$ is unnecessary. Indeed, the functional $Q_g$ is continuous on $L^2_1(M)$ by the Sobolev theorem, and $C^\infty(M)$ is dense in $L^2_1(M)$. But $Q_g(|\varphi|)=Q_g(\varphi)$ for smooth $\varphi$, and a nonnegative function can be approximated arbitrarily closely in $L^2_1$ norm by a positive function. Thus $\lambda(M)$ is the infimum of $Q_g$ over all of $L^2_1(M)$.

For $\varphi\in C^\infty(S^n)$, let $\bar{\varphi}$ denote the weighted push-forward function on $\mathbf{R}^n$ defined by $\bar{\varphi}=u_1\rho^*\varphi$, with $u_1$ the conformal factor given by (3.1). We then have

$$\rho^*\left(\varphi^{p-2}\bar{g}\right)=4\bar{\varphi}^{p-2}ds^2.$$

---

By the conformal invariance of $Q$,

$$\lambda(S^n) = \inf_{\varphi \in C^\infty(S^n)} \frac{\int_{R^n} a |\nabla \bar{\varphi}|^2 dx}{\left(\int_{R^n} |\bar{\varphi}|^p dx\right)^2/p}.$$

But a simple argument using cutoff functions (cf. Lemma 3.4 below) shows that $\bar{\varphi}$ can be approximated by compactly supported functions, and therefore

(3.5) $$\lambda(S^n) = \inf_{\varphi \in C_0^\infty(R^n)} a \| \nabla \varphi \|_2^2 / \|\varphi\|_p^2.$$

The Sobolev inequality says that $\lambda(S^n) > 0$. Thus, identifying $\lambda(S^n)$ and the associated extremal functions is equivalent to identifying the best constant and extremal functions for the Sobolev inequality. Theorem 3.2 then can be rephrased in the following way.

THEOREM 3.3. The $n$-dimensional Sobolev constant $\sigma_n$ is equal to $a/\Lambda$, where

$$\Lambda = \lambda(S^n) = Q(\bar{g}) = n(n-1) \text{vol}(S^n)^{2/n}.$$

Thus the sharp form of the Sobolev inequality on $R^n$ is:

(3.6) $$\|\varphi\|_p^2 \leqslant \frac{a}{\Lambda} \int_{R^n} |\nabla \varphi|^2 dx.$$

Equality is attained only by constant multiples and translates of the functions $u_\alpha$ defined by (3.2). □

An upper bound for the Yamabe invariant. An extremely important feature of the extremal functions $u_\alpha$ is that they become more and more concentrated near the origin as $\alpha \to 0$. In fact, as the following lemma shows, they can be approximated very closely by compactly supported functions, which can in turn be transplanted to a small neighborhood on a manifold $M$ to obtain a test function whose Yamabe quotient is very close to $\lambda(S^n)$.

LEMMA 3.4 (AUBIN [A2]). If $M$ is any compact Riemannian manifold of dimension $n \geqslant 3$, then $\lambda(M) \leqslant \lambda(S^n)$.

PROOF. The functions $u_\alpha$ satisfy $a \| \nabla u_\alpha \|_2^2 = \Lambda \| u_\alpha \|_p^2$ on $R^n$. For any fixed $\varepsilon > 0$, let $B_\varepsilon$ denote the ball of radius $\varepsilon$ in $R^n$, and choose a smooth radial cutoff function $0 \leqslant \eta \leqslant 1$ supported in $B_{2\varepsilon}$, with $\eta \equiv 1$ on $B_\varepsilon$. Consider the smooth, compactly supported function $\varphi = \eta u_\alpha$. Since $\varphi$ is a function of $r = |x|$ alone,

(3.7) $$\int_{R^n} a |\nabla \varphi|^2 dx = \int_{B_{2\varepsilon}} \left(a \eta^2 |\nabla u_\alpha|^2 + 2 a \eta u_\alpha \langle \nabla \eta, \nabla u_\alpha \rangle + au_\alpha^2 |\nabla \eta|^2\right) dx$$

$$\leqslant \int_{R^n} a |\partial_r u_\alpha|^2 dx + C \int_{A_\varepsilon} \left(u_\alpha |\partial_r u_\alpha| + u_\alpha^2\right) dx,$$ where $A_{\varepsilon}$ denotes the annulus $B_{2\varepsilon} - B_{\varepsilon}$. To estimate these terms we observe that

$$\partial_r u_\alpha = (2 - n) r \alpha^{-1} \left( \frac{r^2 + \alpha^2}{\alpha} \right)^{-n/2},$$

and so $u_\alpha \leqslant \alpha^{(n-2)/2} r^{2-n}$ and $\|\partial_r u_\alpha\| \leqslant (n-2) \alpha^{(n-2)/2} r^{1-n}$. Thus, for fixed $\varepsilon$, the second term in (3.7) is $O(\alpha^{n-2})$ as $\alpha \to 0$. For the first term,

$$\int_{\mathbf{R}^n} a |\partial_r u_\alpha|^2 dx = \Lambda \left( \int_{B_{\varepsilon}} u_\alpha^p dx + \int_{\mathbf{R}^n-B_{\varepsilon}} u_\alpha^p dx \right)^2/p$$

$$\leqslant \Lambda \left( \int_{B_{2\varepsilon}} \varphi^p dx + \int_{\mathbf{R}^n-B_{\varepsilon}} \alpha^n r^{-2n} dx \right)^2/p$$

$$= \Lambda \left( \int_{B_{2\varepsilon}} \varphi^p dx \right)^2/p + O(\alpha^n).$$

Therefore the Sobolev quotient of $\varphi$ on $\mathbf{R}^n$ is less than $\Lambda + C\alpha^{n-2}$.

On a compact manifold $M$, let $\varphi = \eta u_\alpha$ in normal coordinates $\{x^i\}$ in a neighborhood of $P \in M$, extended by zero to a smooth function on $M$. Since $\varphi$ is a radial function and $g^{rr} \equiv 1$ in normal coordinates, we have $|\nabla \varphi|^2 = |\partial_r \varphi|^2$ as before. The only corrections to the above estimate are introduced by the scalar curvature term and the difference between $dV_g$ and $dx$. Since $dV_g = (1 + O(r)) dx$ in normal coordinates, the previous calculation gives

$$E(\varphi) = \int_{B_{2\varepsilon}} \left( a |\nabla \varphi|^2 + S \varphi^2 \right) dV_g$$

$$\leqslant (1 + C\varepsilon) \left( \Lambda \| \varphi \|_p^2 + C\alpha^{n-2} + C \int_0^{2\varepsilon} \int_S_r u_\alpha^2 r^{n-1} d\omega dr \right).$$

Lemma 3.5 below shows that the last term is bounded by a constant multiple of $\alpha$. Thus, choosing first $\varepsilon$ and then $\alpha$ small, we can arrange that

$$Q_g(\varphi) \leqslant (1 + C\varepsilon)(\Lambda + C\alpha),$$

which proves that $\lambda(M) \leqslant \Lambda$. □

The following simple calculus lemma will be used again in §5, so we state it in somewhat more generality than needed for the above argument.

Lemma 3.5. Suppose $k > -n$. Then as $\alpha \to 0$,

$$I(\alpha) = \int_0^{\varepsilon} r^k u_\alpha^2 r^{n-1} dr$$

is bounded above and below by positive multiples of $\alpha^{k+2}$ if $n > k + 4$, $\alpha^{k+2} \log(1/\alpha)$ if $n = k + 4$, and $\alpha^{n-2}$ if $n < k + 4$.

Proof. The substitution $\sigma = r/\alpha$ gives

$$I(\alpha) = \alpha^{k+2} \int_0^{\varepsilon/\alpha} \sigma^{k+n-1} (\sigma^2 + 1)^{2-n} d\sigma.$$

---

Observe that $\sigma^2 \leqslant \sigma^2 + 1 \leqslant 2\sigma^2$ for $\sigma \geqslant 1$, so $I(\alpha)$ is bounded above and below by positive multiples of

$$\alpha^{k+2}\left(C + \int_{1}^{\varepsilon/\alpha} \sigma^{k+3-n} d\sigma\right).$$

The expression in parentheses is bounded if $n > k + 4$; it is comparable to $\alpha^{n-k-4}$ if $n < k + 4$, and to $\log(1/\alpha)$ if $n = k + 4$. □

4. The variational approach. In this section we will prove that the Yamabe problem can be solved on a general compact manifold $M$ provided that $\lambda(M) < \lambda(S^n)$. This is the analytic part of the solution.

The most direct approach to minimizing (1.4) would be to construct a sequence of functions for which the functional $Q_g$ approaches its infimum (a "minimizing sequence"), and hope that some subsequence converges to an actual extremal function. However, as we shall see, because the exponent $p$ that occurs in the definition of $Q_g$ is exactly the critical exponent for the Sobolev inequality, this direct approach does not work.

Suppose $\{u_i\}$ is a sequence of smooth functions such that $Q_g(u_i) \rightarrow \lambda(M)$. By homogeneity we can assume that $\|u_i\|_p = 1$ for each $i$. Then

$$\|u_i\|_{2,1}^2 = \int_M \left(|\nabla u_i|\right)^2 + u_i^2 dV_g$$

$$= \frac{1}{a} Q_g(u_i) + \int_M \left(1 - \frac{S}{a}\right)u_i^2 dV_g$$

$$\leqslant \frac{1}{a} Q_g(u_i) + C \|u_i\|_p^2,

by Hölder's inequality. Therefore, $\{u_i\}$ is bounded in $L_1^2(M)$. Since bounded sets in a Hilbert space are weakly precompact, this implies that a subsequence converges weakly to a function $\varphi \in L_1^2(M)$. But since $p$ is precisely the exponent for which the inclusion $L_1^2 \subset L^p$ is not compact, we have no guarantee that the constraint $\|u_i\|_p = 1$ is preserved in the limit. In particular, the limit function $\varphi$ may be identically zero.

The subcritical equation. Yamabe's approach was to consider first the perturbed functional $Q^s(\varphi) = E(\varphi)/\|\varphi\|_s^2$ for $2 \leqslant s \leqslant p$. We set $\lambda_s = \inf\{Q^s(\varphi): \varphi \in C^\infty(M)\}$. Observe that a minimizing function $\varphi$ with $\|\varphi\|_s = 1$ satisfies

(4.1)

$$\Box \varphi = \lambda_s \varphi^{s-1}.$$

We will see that, for $s < p$, this equation always has a smooth, positive, minimizing solution $\varphi_s$. We begin by showing that elliptic regularity for $\Delta$ implies the following basic regularity result for equation (4.1).

THEOREM 4.1 (REGULARITY THEOREM). Suppose $\varphi \in L_1^2(M)$ is a nonnegative weak solution of (4.1) with $2 \leqslant s \leqslant p$, and $|\lambda_s| \leqslant K$ for some constant $K$. If $\varphi \in L^r(M)$ for some $r > (s-2)n/2$ (in particular if $r = s < p$, or if $s = p < r$), then $\varphi$ is either identically zero or strictly positive and $C^\infty$, and $\|\varphi\|_{C^{2,\alpha}} \leqslant C$, where $C$ depends only on $M$, $g$, $K$, and $\|\varphi\|_r$.

---

PROOF. Since $\varphi \in L'(M)$, (4.1) implies that $a\Delta\varphi = \lambda_s\varphi^{s-1} - S\varphi \in L^q(M)$, with $q = r/(s-1)$. By elliptic regularity (Theorem 2.5), this in turn implies $\varphi \in L_2^q(M)$. The Sobolev embedding theorem now gives $\varphi \in L'r'(M)$, with $r' = nr/(ns-n-2r)$. Observe that our hypothesis on $r$ implies $r' > r$. Iterating this argument shows that $\varphi \in L_2^q(M)$ for all $q > 1$. Now the $C^\alpha$ case of the Sobolev embedding theorem (Theorem 2.2(c)) implies that $\varphi \in C^\alpha(M)$ for some $\alpha > 0$. Then $\varphi^{s-1} \in C^\alpha(M)$ as well, so by elliptic regularity again we conclude that $\varphi \in C^{2,\alpha}(M)$. Each of the above applications of the Sobolev and elliptic regularity theorems gives us a bound on the corresponding norm, so we obtain the desired bound on $\|\varphi\|_{C^{2,\alpha}}$.

From (4.1) it follows that $(\Delta + m)\varphi \geqslant 0$, for some constant $m \geqslant 0$ and $m \geqslant \sup\{(S - \lambda_s\varphi^{s-2})/a\}$. If $\varphi = 0$ somewhere, then $\varphi$ is identically zero by the strong maximum principle (Theorem 2.6). Thus $\varphi$ is either strictly positive or zero.

Finally, since $\varphi$ is $C^{2,\alpha}$ and nowhere zero, so is $\varphi^{s-1}$, and so we can apply elliptic regularity iteratively to (4.1) to conclude that $\varphi$ is $C^\infty$. □

We remark that the above result (without the uniform bound on $\|\varphi\|_{C^{2,\alpha}}$) has been proved in the borderline case $r = s = p$ by Trudinger [T]. Since it is not needed for the present argument, we omit it.

PROPOSITION 4.2 (YAMABE [Y]). For $2 \leqslant s < p$, there exists a smooth, positive solution $\varphi_s$ to the subcritical equation (4.1), for which $Q^s(\varphi_s) = \lambda_s$ and $\|\varphi_s\|_s = 1$.

PROOF. Let $\{u_i\} \subset C^\infty(M)$ be a minimizing sequence for $Q^s$, with $\|\mu_i\|_s = 1$. Since $Q^s(|u_i|) = Q^s(u_i)$, after replacing $u_i$ by $|u_i|$ we may assume $\mu_i \geqslant 0$. As we noted at the beginning of this section, $\{u_i\}$ is bounded in $L_1^2(M)$. Since the inclusion map $L_1^2 \subset L^s$ is compact, a subsequence of the $\{\mu_i\}$ converges weakly in $L_1^2$ and strongly in $L^s$ to a function $\varphi_s \in L_1^2(M)$ with $\|\varphi_s\|_s = 1$.

Since by Hölder’s inequality the $L^2$ norm is dominated by the $L^s$ norm, it follows that $\int Su_i^2 \rightarrow \int S\varphi_s^2$. Weak convergence in $L_1^2$ implies that

$$\int_M |\nabla\varphi_s|^2 dV_g = \lim_{i \to \infty} \int_M \left\langle \nabla u_i, \nabla\varphi_s \right\rangle dV_g$$

$$\leqslant \limsup_{i \to \infty} \left(\int_M |\nabla u_i|^2 dV_g\right)^{1/2}\left(\int_M |\nabla\varphi_s|^2 dV_g\right)^{1/2}$$

and therefore $Q^s(\varphi_s) \leqslant \lim_{i \to \infty} Q^s(u_i) = \lambda_s$. But since $\lambda_s$ is by definition the infimum of $Q^s$, we must have $Q^s(\varphi_s) = \lambda_s$, and so $\varphi_s$ is extremal. Thus $\varphi_s$ is a weak solution to the Euler-Lagrange equation (4.1). By the regularity theorem, $\varphi_s$ is positive and $C^\infty$. □

The limit as $s \rightarrow p$. Now our task is to investigate the limit of $\varphi_s$ as $s \rightarrow p$. We will see that, provided $\lambda(M) < \lambda(S^n)$, the functions $\varphi_s$ converge uniformly to a solution of the Yamabe problem.

We begin by describing the behavior of $\lambda_s$. As the following lemma shows, the situation is simplified if the metric $g$ is chosen so that $\int_M dV_g = 1$. From now on, multiplying $g$ by a constant if necessary, we will assume that this holds. We note that Hölder’s inequality then implies that $\|\mu\|_s \leqslant \|\mu\|_{s'}$ if $s \leqslant s'$.

---

LEMMA 4.3 (AUBIN [A2]). If $ \int_M dV_g = 1, $ then $ |\lambda_s| $ is nonincreasing as a function of $ s \in[2,p] $; and if $ \lambda(M) \geqslant0, $ $ \lambda_s $ is continuous from the left.

PROOF. We show first that $ |\lambda_s| $ is nonincreasing. Observe that for any $ s $ and $ s' $ , and any nonzero $ u \in C^\infty(M), $
$$ Q^{s'}(u) = \frac{\|u\|_s^2}{\|u\|_{s'}^2} Q^s(u). $$

If $ s \leqslant s' $ , then $ \|u\|_s \leqslant\|u\|_{s'}, $ and therefore $ |\lambda_{s'}| \leqslant|\lambda_s|.$

We remark that if $ \lambda_s < 0 $ for some $ s, $ we can choose $ u \in C^\infty(M) $ such that $ Q^s(u)<0, $ and (4.2) shows that $ Q^{s'}(u)<0 $ for any $ s' $ ; thus $ \lambda_s < 0 $ for all $ s. $
Now suppose $ \lambda(M) \geqslant0; $ by the above remark $ \lambda_s \geqslant0 $ for $ 2 \leqslant s \leqslant p. $ Choose $ s \in[2,p]. $ Given $ \varepsilon > 0, $ there exists $ u \in C^\infty(M) $ such that $ Q^s(u)<\lambda_s+\varepsilon. $ Since $ \|u\|_s $ is a continuous function of $ s, $ $ \lambda_{s'} \leqslantQ^{s'}(u)<\lambda_s+2\varepsilon $ for $ s' \leqslant s $ sufficiently close to $ s. $ Since $ \lambda_s $ is nonincreasing, this shows that $ \lambda_s $ is continuous from the left. $ \Box $

The error in Yamabe's proof was the claim that the functions $ \{\varphi_s\} $ are uniformly bounded as $ s \rightarrow p. $ This is false in general, as we will see below in the case of the sphere. However, the following uniform $ L^r $ bound does hold provided $ \lambda(M)<\lambda(S^n), $ and this is sufficient to solve the problem.

It has been traditional to consider separately the cases $ \lambda(M) \leqslant0 $ and $ \lambda(M)>0. $ The following proof disposes of both cases together.

PROPOSITION 4.4 (TRUDINGER [T], AUBIN [A2]). Suppose $ \lambda(M)<\lambda(S^n), $ and let $ \{\varphi_s\} $ be the collection of functions given by Proposition 4.2. There are constants $ s_0<p, r>p, $ and $ C>0 $ such that $ \|\varphi_s\|_r \leqslant C $ for all $ s \geqslant s_0. $
PROOF. Let $ \delta>0. $ Multiplying (4.1) by $ \varphi_s^{1+2\delta} $ and integrating, we obtain
$$ \int_M \left(a\left\langle d\varphi_s,(1+2\delta)\varphi_s^{2\delta}d\varphi_s\right\rangle+S\varphi_s^{2+2\delta}\right) dV_g=\lambda_s \int_M \varphi_s^{s+2\delta} dV_g. $
If we set $ w=\varphi_s^{1+\delta}, $ this can be written
$$ \frac{1+2\delta}{(1+\delta)^2} \int_M a\left|dw\right|^2 dV_g=\int_M \left(\lambda_s w^2\varphi_s^{s-2}-Sw^2\right) dV_g. $
Now applying the sharp Sobolev inequality (Theorems 2.3 and 3.3), for any $ \varepsilon>0, $
$$ \|w\|_p^2 \leqslant(1+\varepsilon)\frac{a}{\Lambda} \int_M \left|dw\right|^2 dV_g+C_\varepsilon \int_M w^2 dV_g $
$$ \leqslant(1+\varepsilon)\frac{(1+\delta)^2}{(1+2\delta)} \int_M \frac{\lambda_s}{\Lambda} w^2\varphi_s^{s-2} dV_g+C_\varepsilon'\|w\|_2^2 $
$$ \leqslant(1+\varepsilon)\frac{(1+\delta)^2}{(1+2\delta)} \|w\|_p^2 \| \varphi_s\|_{(s-2)n/2}^{s-2}+C_\varepsilon'\|w\|_2^2, $
by Hölder's inequality.

---

Since $s < p$, $(s - 2)n/2 < s$, and thus by Hölder’s inequality again $\|\varphi_s\|_{(s-2)n/2} \leqslant \|\varphi_s\|_s = 1$. Now if $0 \leqslant \lambda(M) < \Lambda$, then for some $s_0 < p$, $\lambda_s/\Lambda \leqslant \lambda_{s_0}/\Lambda < 1$ for $s \geqslant s_0$. Thus we can choose $\varepsilon$ and $\delta$ small enough so that the coefficient of the first term above is less than 1, and so can be absorbed in the left-hand side. Thus

$$\|w\|_p^2 \leqslant C\|w\|_2^2.$$

The same result obviously holds if $\lambda(M)$ (and hence $\lambda_s$) is less than zero. But applying Hölder’s inequality once more, we see that

$$\|w\|_2 = \|\varphi_s\|_{2(1+\delta)}^{1+\delta} \leqslant \|\varphi_s\|_s^{1+\delta} = 1.$$

Therefore $\|w\|_p = \|\varphi_s\|_{p(1+\delta)}^{1+(\delta)}$ is bounded independently of $s$. □

We can now prove that the Yamabe problem has a solution if $\lambda(M) < \lambda(S^n)$. Theorem A of the Introduction is an immediate consequence of the following result.

THEOREM 4.5. Let $\{\varphi_s\}$ be the functions given by Proposition 4.2, and assume $\lambda(M) < \lambda(S^n)$. As $s \rightarrow p$, a subsequence converges uniformly to a positive function $\varphi \in C^\infty(M)$ which satisfies:

$$Q_g(\varphi) = \lambda(M), \quad \Box \varphi = \lambda(M)\varphi^{p-1}.$$

Thus the metric $\tilde{g} = \varphi^{p-2}g$ has constant scalar curvature $\lambda(M)$.

PROOF. Since the functions $\{\varphi_s\}$ are uniformly bounded in $L^r(M)$, the regularity theorem shows they are uniformly bounded in $C^{2,\alpha}(M)$ as well. The Arzela-Ascoli theorem then implies that a subsequence converges in $C^2$ norm to a function $\varphi \in C^2(M)$. The limit function $\varphi$ therefore satisfies

$$\Box \varphi = \lambda\varphi^{p-1}, \quad Q_g(\varphi) = \lambda,$$

where $\lambda = \lim_{s \rightarrow p}\lambda_s$. If $\lambda(M) \geqslant 0$, Lemma 4.3 shows that $\lambda = \lambda(M)$. On the other hand, if $\lambda(M) < 0$, the fact that $\lambda_s$ is increasing implies that $\lambda \leqslant \lambda(M)$; but since $\lambda(M)$ is the infimum of $Q_g$ we must have $\lambda = \lambda(M)$ in that case as well.

Now a final application of Theorem 4.1 shows that $\varphi$ is $C^\infty$, and it is strictly positive because $\|\varphi\|_p \geqslant \lim_{s \rightarrow p}\|\varphi_s\|_s = 1$. □

There are many other methods of obtaining the solution in the case $\lambda(M) \leqslant 0$. Jerry Kazdan [K] has given an excellent survey.

Existence on the sphere. It is important to note that the hypothesis $\lambda(M) < \lambda(S^n)$ is necessary in the previous theorem. On the sphere itself, the presence of a noncompact group of conformal diffeomorphisms defeats the above approach: the family of metrics $(\sigma^{-1}\delta_\alpha\sigma)^*\bar{g}$ on the sphere, as $\alpha \rightarrow \infty$, are all solutions to the Yamabe equation, but not uniformly bounded.

On the other hand, the very existence of this family of conformal diffeomorphisms enables us, with a little more effort, to prove existence of extremals on the sphere, by means of the following “renormalization” approach, due to Karen Uhlenbeck.

---

PROPOSITION 4.6. There exists a positive, $C^\infty$ function $\psi$ on $S^n$ satisfying $Q_{\bar{g}}(\psi) = \lambda(S^n)$.

Proof. For $2 \leqslant s < p$, let $\varphi_s$ be the solution on $S^n$ to the subcritical problem (4.1), given by Proposition 4.2. Composing with a rotation, we may assume that the supremum of $\varphi_s$ is attained at the south pole for each $s$. If $\{\varphi_s\}$ is uniformly bounded, the method of Theorem 4.5 shows that a subsequence converges to an extremal solution; so assume from now on that $\sup \varphi_s \to \infty$.

Now let $\kappa_\alpha = \sigma^{-1} \delta_\alpha \sigma$: $S^n \rightarrow S^n$ be the conformal diffeomorphism induced by dilation on $\mathbf{R}^n$, as described in the beginning of §3. If we set $g_\alpha = \kappa_\alpha^*\bar{g}$, we can write $g_\alpha = t_\alpha^{p-2}\bar{g}$, where the conformal factor $t_\alpha$ is the function

$$t_\alpha(\zeta, \xi) = \left( \frac{(1 + \xi) + \alpha^2(1 - \xi)}{2\alpha} \right)^{(2-n)/2}$$

Observe that at the south pole $t_\alpha = \alpha^{(2-n)/2}$.

For each $s < p$, let $\psi_s = t_\alpha \kappa_\alpha^*\varphi_s$, with $\alpha = \alpha_s$ chosen so that $\psi_s = 1$ at the south pole. This implies that $\alpha_s = (\sup \varphi_s)^{2/(n-2)} \rightarrow \infty$ as $s \rightarrow p$, and $\psi_s \leqslant \alpha^{(n-2)/2}t_\alpha$ on $M$. Let $\Box_\alpha$ denote the conformally invariant Laplacian with respect to the metric $g_\alpha$; by naturality of $\Box$, $\Box_\alpha(\kappa_\alpha^*\varphi_s) = \kappa_\alpha^*(\Box\varphi_s)$. Then by the transformation law for $\Box$ (2.7) we have

$$\Box\psi_s = \Box\left(t_\alpha \kappa_\alpha^*\varphi_s\right) = t_\alpha^{p-1}\Box_\alpha(\kappa_\alpha^*\varphi_s) = \lambda_s t_\alpha^{p-1}(\kappa_\alpha^*\varphi_s)^{s-1}$$

$$= \lambda_s t_\alpha^{p-s}\psi_s^{s-1}$$

Observe that this transformation law also implies that

$$\|\psi_s\|_{2,1} \leqslant C \int_S^n \psi_s \Box\psi_s dV_{\bar{g}} = C \int_S^n \varphi_s \Box\varphi_s dV_{\bar{g}} \leqslant C' \|\varphi_s\|_{2,1}$$

so $\{\psi_s\}$ is bounded in $L_1^2(S^n)$, and hence also in $L^p(S^n)$ by the Sobolev theorem. Let $\psi \in L_1^2(S^n)$ denote the weak limit.

Now if $P$ is the north pole, on any compact subset of $S^n - \{P\}$ there exists a constant $A$ such that $t_\alpha \leqslant A\alpha^{(2-n)/2}$, and thus the right-hand side of (4.3) is bounded there by $\lambda_2 A^{p-1}$, independently of $s$. This implies that, on any such set, the right-hand side is bounded in $L^r$ for every $r$. Arguing as in the proof of Theorem 4.1, but using local elliptic regularity (Theorem 2.4), $\{\psi_s\}$ is bounded in $C^{2,\alpha}$ on compact sets disjoint from $P$. Let $K_1 \subset K_2 \subset \cdots$ be a sequence of compact sets whose union is $S^n - \{P\}$. By the Arzela-Ascoli theorem, we can choose a subsequence of $\{\psi_s\}$ that converges in $C^2(K_1)$, and then a subsequence that converges in $C^2(K_2)$, etc. Taking a diagonal subsequence, we see that the limit function $\psi$ is $C^2$ on $S^n - \{P\}$.

Since $\lambda_s \rightarrow \Lambda$ and $t_\alpha^{p-s} \leqslant 1$ away from $P$ for $s$ near $p$, we conclude that $\psi$ satisfies $\Box\psi = f\psi^{p-1}$ on $S^n - \{P\}$, for some $C^2$ function $f$ with $0 \leqslant f \leqslant \Lambda$. By the removable singularities result (Proposition 2.7), the same equation must hold weakly on all of $S^n$. For each $s$,

$$\|\psi_s\|_p^p = \int_S^n t_\alpha^p\left(\kappa_\alpha^*\varphi_s\right)^p dV_{\bar{g}}$$

$$= \int_S^n \left(\kappa_\alpha^*\varphi_s\right)^p \kappa_\alpha^*dV_{\bar{g}} = \|\varphi_s\|_p^p \geqslant \text{Vol}(S^n)^{1-p/s}\|\varphi_s\|_s^p.$$

---

This implies that $||\psi||_p \geqslant 1$, and therefore $Q_{\bar{g}}(\psi) \leqslant \Lambda$. But since $\Lambda$ is by definition the infimum of $Q_{\bar{g}}$, we must have $\Box \psi = \Lambda \psi^{p-1}$ and $Q_{\bar{g}}(\psi) = \Lambda$.

It remains to show that $\psi$ is positive and smooth. By the regularity theorem, it suffices to show that $\psi \in L^r$ for some $r > p$. For $q > 1$ the operator $\Box$: $L_2^q \rightarrow L^q$ has a bounded inverse by elliptic regularity. Consider the perturbation

$$\Box_\eta = \Box - \eta \Lambda \psi^{p-2}$$

for $\eta \in C^\infty(S^n)$ supported in a small neighborhood of $P$. $\Box_\eta$ will also have a bounded inverse if the operator norm of the perturbation term $\eta \Lambda \psi^{p-2}$ is small enough. If we choose $q$ such that $2n/(n+2) < q < n/2$ and set $r = nq/(n-2q)$, then for $u \in L_2^q$,

$$\| \eta \Lambda \psi^{p-2} u \|_q \leqslant \Lambda \| \eta^{1/(p-2)} \psi \|_p^{p-2} \| u \|_r \leqslant C \Lambda \| \eta^{1/(p-2)} \psi \|_p^{p-2} \| u \|_{q,2},$$

by the Hölder and Sobolev inequalities. Thus we can make the operator norm as small as we like by choosing $\eta$ with small support and $0 \leqslant \eta \leqslant 1$.

Now $\Box_\eta \psi = (1-\eta) \Lambda \psi^{p-1} \in L^q(S^n)$ since $\psi$ is $C^2$ away from $P$. Therefore, since $\Box_\eta$: $L_2^q \rightarrow L^q$ is invertible, there exists $\xi \in L_2^q(S^n) \subset L_1^2(S^n)$ such that $\Box_\eta(\xi-\psi) = 0$. Using the Sobolev and Hölder inequalities as above, $\| u \|_{2,1}^2 \leqslant \int u \Box u \leqslant \int u \Box_\eta u + \varepsilon \| u \|_{2,1}^2$ when the support of $\eta$ is small. Thus $\Box_\eta$ is injective on $L_1^2$, and so we must have $\psi = \xi \in L_2^q(S^n) \subset L^r(S^n)$. Since $r > p$, Theorem 4.1 implies that $\psi$ is $C^\infty$, and since $\psi = 1$ at the south pole, $\psi$ is strictly positive.

It can be shown, in fact, using methods of H. Brezis, L. Nirenberg, E. Lieb, and P.-L. Lions (see [BL, BN, and L]), that any minimizing sequence on the sphere can be renormalized to converge to a smooth extremal.

Uhlenbeck has adapted the renormalization method described above to give another proof that the Yamabe problem can be solved on any compact manifold $M$ provided that $\lambda(M) < \lambda(S^n)$. Assuming the sequence of solutions to the subcritical equation is not uniformly bounded, she uses Riemannian normal coordinates to transfer the sequence to $R^n$, where a renormalized sequence can be made to converge to a function that contradicts the Sobolev inequality if $\lambda(M) < \lambda(S^n)$. (See also [SU and JL2] for other applications of this technique.)

5. Conformal normal coordinates. In Riemannian geometry, geodesic normal coordinates are invaluable for comparing the local geometry of a manifold with that of $R^n$. In this section we will describe a set of similar coordinate charts on a conformal manifold $M$. These will be normal coordinate charts for some metric $g$ within the conformal class; the freedom in the choice of $g$ will enable us to find coordinate systems that simplify the local geometry more than normal coordinates in a fixed Riemannian structure.

Our first application of conformal normal coordinates will be a very simple proof of Aubin’s Theorem B of the Introduction. In the next section we will apply them to the calculation of asymptotic expansions of the Green function for $\Box$, and in §7 we will use them again to prove Theorem C.

---

Normalized conformal structures were first constructed by Robin Graham [G], who proved, in connection with his work with Charles Fefferman on conformal invariant theory, that for any $P \in M$ it is possible to find a conformal metric for which the symmetrized covariant derivatives of the Ricci tensor of $g$ vanish at $P$. Later in this section we will give a simple proof of Graham's theorem.

Graham's normalization is designed for simplifying the algebra of conformal invariant theory. For our purposes we want a normalization that simplifies the local analysis. Based on formula (2.1) for the Laplacian, we might guess that a good choice for this normalization would be to choose a conformal metric for which $\det g \equiv 1$ in $g$-normal coordinates. (Intrinsically, this means that the Jacobian of the exponential map of $g$ is 1.) This is the normalization we will choose.

THEOREM 5.1 (CONFORMAL NORMAL COORDINATES). Let $M$ be a Riemannian manifold and $P \in M$. For each $N \geqslant 2$ there is a conformal metric $g$ on $M$ such that

$$\det g_{ij} = 1 + O(r^N),$$

where $r = |x|$ in $g$-normal coordinates at $P$. In these coordinates, if $N \geqslant 5$, the scalar curvature of $g$ satisfies $S = O(r^2)$ and $\Delta S = \frac{1}{6}|W|^2$ at $P$.

The proof will be carried out below. First, to illustrate the usefulness of these coordinates, we present an application.

PROOF OF THEOREM B. Let $\{x^i\}$ be conformal normal coordinates in a neighborhood of $P \in M$. Recalling the notation of Lemma 3.4, let $\varphi = \eta u_\alpha$ in $x$-coordinates, where $\eta$ is a cutoff function supported in $B_{2\epsilon}$. Since $dV_g \equiv dx$ in conformal normal coordinates, the estimates of that lemma apply without the factor $(1 + C\epsilon)$ to show that

$$E(\varphi) \leqslant \Lambda \|\varphi\|_p^2 + C\alpha^{n-2} + \int_{B_{2\epsilon}} S\varphi^2 dx.$$

But now in conformal normal coordinates $S = O(r^2)$ and $\Delta S(P) = \frac{1}{6}|W(P)|^2$, so

$$\int_{B_{2\epsilon}} S\varphi^2 dx \leqslant \int_{B_e} Su_\alpha^2 dx + C \int_{A_e} u_\alpha^2 dx$$

$$= \int_0^\epsilon \int_{S_r} \left( \frac{1}{2} S_{,ij} x^i x^j + O(r^3) \right) u_\alpha^2 d\omega_r dr + O(\alpha^{n-2})$$

$$= \int_0^\epsilon \left( -Cr^2 |W(P)|^2 + O(r^3) \right) u_\alpha^2 r^{n-1} dr + O(\alpha^{n-2}).$$

Lemma 3.5 therefore shows that

$$E(\varphi) \leqslant \begin{cases} \Lambda \|\varphi\|_p^2 - C |W(P)|^2 \alpha^4 + o(\alpha^4) & \text{if } n > 6, \\ \Lambda \|\varphi\|_p^2 - C |W(P)|^2 \alpha^4 \log(1/\alpha) + O(\alpha^4) & \text{if } n = 6. \end{cases}$$

---

If $M$ is not locally conformally flat, we can choose $P$ so that $|W(P)|^2 > 0$, and then $Q_g(\varphi) < \Lambda$ for $\alpha$ sufficiently small and $n \geqslant 6$. Thus $\lambda(M) < \Lambda$.

The key ingredient in the proof of Theorem 5.1 is the following inhomogeneous version of Graham's main result.

THEOREM 5.2. Let $P \in M$, $k \geqslant 0$, and let $T$ be a symmetric $(k+2)$-tensor on $T_P M$. There is a unique homogeneous polynomial $f$ of degree $k+2$ in $g$-normal coordinates such that the metric $\tilde{g} = e^{2f}g$ satisfies

$$\text{Sym}\left( \tilde{\nabla}^k \tilde{R}_{ij} \right)(P) = T.$$

PROOF. Let $\{x^i\}$ be $g$-normal coordinates at $P$, $r = |x|$, and let $\mathcal{P}_m$ denote the space of homogeneous polynomials in $x$ of degree $m$. If we set $F_g(x) = R_{ij}(x)x^ix^j$, then by Taylor's theorem

$$F_g = \sum_{m=2}^{k+2} F_g^{(m)} + O(r^{k+3}),$$

where

$$F_g^{(m)} = \frac{1}{(m-2)!} \sum \partial_K R_{ij}(P) x^i x^j x^K \in \mathcal{P}_m.$$

(The sum is over $i, j$ and all multi-indices $K = (k_1, \ldots, k_{m-2})$ of length $|K| = m-2$.) Observe that the covariant derivatives of $R_{ij}$ are related to ordinary partial derivatives by $R_{ij,K}(P) = \partial_K R_{ij}(P) + S_{ijK}$, where the $S_{ijK}$ are constructed as polynomials in the curvature and its derivatives of order $<|K|$ at $P$. If $\tilde{g} = e^{2f}g$ with $f \in \mathcal{P}_{k+2}$, then $\tilde{S}_{ijK} = S_{ijK}$ when $|K| = k$.

Our result is equivalent to finding $f \in \mathcal{P}_{k+2}$ such that

$$0 = \frac{1}{k!} \sum_{|K|=k} \sum_{i,j} \left( \tilde{R}_{ij,K}(P) - T_{ijK} \right) x^i x^j x^K$$

$$= F_{\tilde{g}}^{(k+2)}(x) + \sum \frac{1}{k!} \left( S_{ijK} - T_{ijK} \right) x^i x^j x^K.$$

(We have used the fact that $g$-normal coordinates differ from $\tilde{g}$-normal coordinates by $O(r^{k+2})$.) By Euler's formula, $x^i x^j \partial_i \partial_j f = (x^i \partial_i)^2 f - x^i \partial_i f = (k+2)(k+1)f$; and $\Delta f = \Delta_0 f + O(r^{k+1})$, where $\Delta_0$ is the Euclidean Laplacian in $x$-coordinates. Thus the transformation law (2.5) for $R_{ij}$ gives

$$F_{\tilde{g}}^{(k+2)}(x) = F_g^{(k+2)}(x) + x^i x^j \left( -(n-2) \partial_i \partial_j f + \Delta_0 f \delta_{ij} \right)$$

$$= F_g^{(k+2)}(x) - (n-2)(k+2)(k+1)f + r^2 \Delta_0 f.$$

Thus there is a unique $f$ so that (5.1) is satisfied provided that the operator $r^2 \Delta_0 - (n-2)(k+2)(k+1)$ is invertible on $\mathcal{P}_{k+2}$. This is guaranteed by the following lemma. □

Lemma 5.3. The eigenvalues of $r^2 \Delta_0$ on $\mathcal{P}_m$ are

$$\{\lambda_j = -2j(n-2+2m-2j): j = 0, \ldots, [m/2]\}.$$

---

The eigenfunctions corresponding to $\lambda_j$ are the functions of the form $r^{2j}u$, where $u \in \mathcal{P}_{m-2j}$ is harmonic.

Proof. This holds for $m = 0$ or 1 since $r^2\Delta_0 = 0$ on $\mathcal{P}_m$ in these cases. For $m \geqslant 2$ suppose $f \in \mathcal{P}_m$ satisfies $r^2\Delta_0 f = \lambda f$. By Euler's formula, $\Delta_0 f \in \mathcal{P}_{m-2}$ satisfies

$$\lambda \Delta_0 f = \Delta_0 \left(r^2 \Delta_0 f\right) = \Delta_0 \left(r^2\right) \Delta_0 f - 4x^i \partial_i \Delta_0 f + r^2 \Delta_0^2 f$$

$$= -2n \Delta_0 f - 4(m - 2) \Delta_0 f + r^2 \Delta_0^2 f,$$

so $r^2\Delta_0 (\Delta_0 f) = (\lambda + 2n + 4m - 8)\Delta_0 f$. This means that either $\Delta_0 f = 0$, in which case $\lambda = 0$ and $f$ is harmonic, or $\lambda + 2n + 4m - 8$ is an eigenvalue of $r^2\Delta_0$ on $\mathcal{P}_{m-2}$ with eigenfunction $\Delta_0 f$. In the latter case, $f = \lambda^{-1} r^2\Delta_0 f$. The lemma now follows by induction. □

Corollary 5.4 (Graham [G]). Given $P \in M$, $N \geqslant 0$, there exists a metric conformal to $g$ such that all symmetrized covariant derivatives of the Ricci tensor of order $\leqslant N$ vanish at $P$.

Proof. By induction on $N$: choose $T = 0$ in the above theorem, and note that $f \in \mathcal{P}_{N+2}$ implies that $\tilde{\nabla}^k \tilde{R}_{ij} = \nabla^k R_{ij}$ for $k < N$. □

Lemma 5.5. In $g$-normal coordinates, the function det $g_{ij}$ has the expansion (5.2) det $g_{ij} = 1 - \frac{1}{3} R_{ij} x^i x^j - \frac{1}{6} R_{ij,k} x^i x^j x^k$

$$-\left(\frac{1}{20} R_{ij,kl} + \frac{1}{90} R_{pijm} R_{pklm} - \frac{1}{18} R_{ij} R_{kl}\right) x^i x^j x^k x^l + O\left(r^5\right),$$

where the curvatures are evaluated at $P$.

Proof. Let $\{x^i\}$ denote normal coordinates for $g$ on a neighborhood $U$ of $P$, and use them to identify $U$ with an open set in $\mathbf{R}^n$. To compute the expansion of the metric $g_{ij}(x)$, we first recall the definition of a Jacobi field.

Fix $\tau, \xi \in \mathbf{R}^n$, consider the map $\gamma: \mathbf{R} \times \mathbf{R} \rightarrow \mathbf{R}^n$ by $\gamma_s(t) = t(\tau + s\xi)$ which gives a one-parameter family of radial geodesics, and let $T = \gamma'_s(t)$. The variational vector field

$$X\left(\gamma_s(t)\right) = \frac{\partial}{\partial s} \gamma_s(t) = t\xi$$

is called a Jacobi field. Since for each $s$, $\gamma_s$ satisfies the geodesic equation $\nabla_T T = 0$, and since $0 = \gamma_*[\partial/\partial t, \partial/\partial s] = [T, X] = \nabla_T X - \nabla_X T$, we have

$$0 = \nabla_X \nabla_T T = \nabla_T \nabla_X T - \left([\nabla_T, \nabla_X] - \nabla_{[X,T]}\right) T$$

$$= \nabla_T \nabla_T X - R(T, X) T.$$

Thus $X$ satisfies the Jacobi equation $\nabla_T^2 X = R_T(X)$, where $R_T$ is the curvature endomorphism $R(T, \cdot)T$.

The Taylor series of $f(t) = |X(\gamma_0(t))|^2$ can be computed by repeatedly differentiating with respect to $\nabla_T$, using the Jacobi equation, and evaluating at $t = 0$, noting that $X(0) = 0$ and $\nabla_T X(0) = \xi$. The first few terms are:

$$\nabla_T f(0) = 0,$$

$$\nabla_T^2 f(0) = 2\left\langle \xi, \xi \right\rangle_0,$$

$$\nabla_T^3 f(0) = 0,$$

$$\nabla_T^4 f(0) = 8\left\langle R_\tau \xi, \xi \right\rangle_0,$$

$$\nabla_T^5 f(0) = 20\left\langle (\nabla_\tau R_\tau) \xi, \xi \right\rangle_0,$$

$$\nabla_T^6 f(0) = 36\left\langle (\nabla_\tau^2 R_\tau) \xi, \xi \right\rangle_0 + 32\left\langle R_\tau \xi, R_\tau \xi \right\rangle_0.$$

---

Therefore,

(5.3) $\langle \xi, \xi \rangle_{t\tau} = t^{-2}|X(\gamma_0(t))|^2$
$$= \langle \xi, \xi \rangle_0 + \frac{t^2}{3}\langle R_\tau \xi, \xi \rangle_0 + \frac{t^3}{6}\langle (\nabla_\tau R_\tau)\xi, \xi \rangle_0$
$$+ \frac{t^4}{20}\langle (\nabla_\tau^2 R_\tau)\xi, \xi \rangle_0 + \frac{2t^4}{45}\langle R_\tau \xi, R_\tau \xi \rangle_0 + O(t^5).$$

Polarizing this with respect to $\xi$ and substituting $x = t\tau$ yields the expansion for the metric in normal coordinates:

(5.4) $g_{pq}(x) = \delta_{pq} + \frac{1}{3}R_{pijq}x^i x^j + \frac{1}{6}R_{pijq,k}x^i x^j x^k$
$$+ \left(\frac{1}{20}R_{pijq,kl} + \frac{2}{45}R_{pijm}R_{qklm}\right)x^i x^j x^k x^l + O(r^5),$$

where the curvature terms are to be evaluated at the origin. This can be written $g_{pq} = \exp A_{pq}$, where

$$A_{pq}(x) = \frac{1}{3}R_{pijq}x^i x^j + \frac{1}{6}R_{pijq,k}x^i x^j x^k$
$$+ \left(\frac{1}{20}R_{pijq,kl} - \frac{1}{90}R_{pijm}R_{qklm}\right)x^i x^j x^k x^l + O(r^5).$$

Then det $g_{pq} = \exp(\text{tr } A_{pq})$ has the expansion (5.2).

PROOF OF THEOREM 5.1. Assume by induction that $g$ satisfies det $g_{ij} = 1 + O(r^N)$, $N \geqslant 2$. It can easily be seen that each term in the expansion (5.3) for $\langle \xi, \xi \rangle$ has the form

$$c_k t^k\left(\langle (\nabla_\tau^{k-2}R_\tau)\xi, \xi \rangle + B_k(\xi, \xi)\right),$$

where $c_k$ is a constant and $B_k$ is a bilinear form constructed from $R_\tau$ and its derivatives of order less than $k-2$. Thus the expansion of det $g_{ij}$ is of the form

$$\det g_{ij} = 1 + \sum_{|K|=N-2} c_N(R_{ij,k}-T_{ijK})x^i x^j x^K + O(r^{N+1})$$

where $T_{ijK}$ are the coefficients of a symmetric tensor $T$ on $T_P M$ constructed from the curvature and its derivatives of order less than $N-2$.