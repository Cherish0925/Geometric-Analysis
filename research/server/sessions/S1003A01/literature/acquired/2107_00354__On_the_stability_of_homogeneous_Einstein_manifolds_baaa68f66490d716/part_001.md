---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: [2107.00354] On the stability of homogeneous Einstein manifolds II]

---
source_file: 2107_00354.pdf
converter: mathpix
format: mmd
---

\title{
ON THE STABILITY OF HOMOGENEOUS EINSTEIN MANIFOLDS II
}

\author{
JORGE LAURET AND CYNTHIA WILL
}

\begin{abstract}
For any $G$-invariant metric on a compact homogeneous space $M=G / K$, we give a formula for the Lichnerowicz Laplacian restricted to the space of all $G$-invariant symmetric 2-tensors in terms of the structural constants of $G / K$. As an application, we compute the $G$-invariant spectrum of the Lichnerowicz Laplacian for all the Einstein metrics on most generalized Wallach spaces and any flag manifold with $b_{2}(M)=1$. This allows to deduce the $G$-stability and critical point types of each of such Einstein metrics as a critical point of the scalar curvature functional.
\end{abstract}

\section*{Contents}
1. Introduction ..... [1]
2. Preliminaries ..... 5
2.1. $G$-stability ..... 5
2.2. Ricci curvature ..... 6
2.3. Lichnerowicz Laplacian ..... 6
2.4. Structural constants ..... 7
2.5. Einstein equations ..... 8
2.6. Scalar curvature ..... 9
3. A formula for $\mathrm{L}_{\mathfrak{p}}$ in terms of structural constants ..... 9
3.1. Case $r=2$ ..... 13
4. Generalized Wallach spaces ..... 13
4.1. Case $d_{1}=d_{2}=d_{3}$ ..... 15
4.2. Case $d_{1}=d_{2} \neq d_{3}$ ..... 16
4.3. Case $d_{1}, d_{2}, d_{3}$ pairwise different ..... 19
4.4. Application to the prescribed Ricci curvature problem ..... 24
5. Flag manifolds ..... 27
References ..... 28
6. Appendix: Maple codes ..... 29

\section*{1. Introduction}

Back in 1915, Hilbert considered in [H] the simplest curvature functional on the space $\mathcal{M}_{1}$ of all unit volume Riemannian metrics on a given compact manifold $M$, i.e., the total scalar curvature
$$\widetilde{\mathrm{Sc}}(g):=\int_{M} \mathrm{Sc}(g) d \operatorname{vol}_{g},$$
and proved that their critical points are precisely the metrics of constant Ricci curvature, i.e., $\operatorname{Rc}(g)=\rho g$ for some $\rho \in \mathbb{R}$, so-called Einstein metrics (see [B, 4.21]). A long time later, in the seventies, Berger [Be] and Koiso [Ko1] independently discovered that if one

\footnotetext{
Date: July 1, 2022.
This research was partially supported by a grant from Univ. Nac. de Córdoba, Argentina.
}
considers the restriction of $\widetilde{\mathrm{Sc}}$ to the space $\mathcal{C}_{1}$ of all unit volume constant scalar curvature metrics, then the coindex and nullity of any Einstein metric are both finite (modulo trivial variations). A fundamental problem is therefore to determine whether a given Einstein metric $g$ is stable (or linearly stable), i.e., coindex and nullity indeed vanish, or equivalently, the Hessian of $\widetilde{\mathrm{Sc}}$ is negative definite on the tangent space $T_{g} \mathcal{C}_{1}$ (modulo trivial variations). Any stable Einstein metric is in particular a local maximum of $\left.\widetilde{\mathrm{S}}\right|_{\mathcal{C}_{1}}$ and it is rigid, in the sense that every Einstein metric sufficiently close to $g$ is isometric to $g$ up to scaling. It was proved by Koiso that the non-degeneracy of the Hessian is actually enough to get rigidity (see [Ko2, Proposition 3.3] and [B, 12.66]).

Stability seems to be a very strong property, which is in addition hard to be established. Indeed, the only known examples so far of stable Einstein metrics (or local maxima of $\left.\widetilde{\mathrm{Sc}}\right|_{\mathcal{C}_{1}}$ ) with positive scalar curvature are given by some irreducible symmetric spaces. The space $T_{g} \mathcal{C}_{1}$ coincides, modulo trivial variations, with $\mathcal{T} \mathcal{T}_{g}=\operatorname{Ker} \delta_{g} \cap \operatorname{Ker}_{\boldsymbol{\operatorname { t r }}}$, the space of divergence-free (or transversal) and traceless symmetric 2-tensors, so-called TT-tensors, and if $\operatorname{Rc}(g)=\rho g$, then for any $T \in \mathcal{T} \mathcal{T}_{g}$ the Hessian is given by
$$\widetilde{\mathrm{Sc}}_{g}^{\prime \prime}(T, T)=\frac{1}{2}\left\langle\left(2 \rho \mathrm{id}-\Delta_{L}\right) T, T\right\rangle_{g},$$
where $\Delta_{L}$ is the Lichnerowicz Laplacian of $g$ (see [B, 4.64]). Thus $g$ is stable if and only if $2 \rho<\lambda_{L}$, where $\lambda_{L}$ denotes the smallest eigenvalue of $\left.\Delta_{L}\right|_{\mathcal{T} \mathcal{T}_{g}}$ (cf. [CH, §4] and [WW, §1]). The number $\lambda_{L}$ is usually hard to compute or even estimate, it is known for only few metrics. Note that $\left.\widetilde{\mathrm{Sc}}^{\prime \prime}\right|_{\mathcal{T} \mathcal{T}_{g}}$ is non-degenerate if and only if $2 \rho \notin \operatorname{Spec}\left(\left.\Delta_{L}\right|_{\mathcal{T} \mathcal{T}_{g}}\right)$.

We assume that $M$ is homogeneous in this paper. After fixing a transitive action of a compact Lie group $G$ on $M$, we study the stability of $G$-invariant Einstein metrics, which are precisely the critical points of Sc : $\mathcal{M}_{1}^{G} \longrightarrow \mathbb{R}$, where $\mathcal{M}_{1}^{G}$ is the finite-dimensional manifold of all unit volume $G$-invariant metrics on $M$. The $G$-action provides a presentation $M=G / K$ of $M$ as a homogeneous space, where $K \subset G$ is the isotropy subgroup at some origin point $o \in M$. It is proved in [L, §3.4] that
$$T_{g} \mathcal{M}_{1}^{G}=T_{g} N_{G}(K)^{*} g \oplus \mathcal{T} \mathcal{T}_{g}^{G},$$
where $N_{G}(K) \subset \operatorname{Diff}(M)$ is the normalizer of $K$ and $\mathcal{T} \mathcal{T}_{g}^{G}$ is the space of $G$-invariant TT-tensors. An Einstein metric $g \in \mathcal{M}_{1}^{G}$ is therefore called G-stable when $\left.\mathrm{Sc}_{g}^{\prime \prime}\right|_{\mathcal{T} \mathcal{T}_{g}^{G}}<0$, or equivalently, $2 \rho<\lambda_{L}^{G}$, where $\lambda_{L}^{G}$ is the smallest eigenvalue of $\left.\Delta_{L}\right|_{\mathcal{T} \mathcal{T}_{g}^{G}}$. Note that
$$\lambda_{L} \leq \lambda_{L}^{G} .$$
One of the aims of [L] and this paper is to show that this 'algebraic' upper bound for $\lambda_{L}$ is in most cases enough to establish the instability of a homogeneous Einstein metric.

Any $G$-stable Einstein metric is in particular a local maximum of $\mathrm{Sc}: \mathcal{M}_{1}^{G} \longrightarrow \mathbb{R}$, and if $\left.\mathrm{Sc}_{g}^{\prime \prime}\right|_{\mathcal{T}_{g}^{G}}$ is non-degenerate, then $g$ is $G$-rigid, in the sense that $g$ is isolated in the moduli space of $G$-invariant Einstein metrics on $M$ up to pull-back by $N_{G}(K)$ and scaling. $G$ -stability is of course a necessary condition for the classical stability described above, and it is also extremely rare. As far as we know, besides irreducible symmetric metrics and the special case when any subalgebra of $\mathfrak{g}$ containing $\mathfrak{k}$ is of the form $\mathfrak{k} \oplus \mathfrak{a}$ with $[\mathfrak{a}, \mathfrak{a}]=0$ (e.g., if $K$ is a maximal subgroup of $G$, see [WZ, Bo]), the only known $G$-stable Einstein metrics with $\operatorname{dim} \mathcal{M}_{1}^{G}>1$ are:
\begin{itemize}
\item[-] the standard metric on SU(2), $E_{7} / \operatorname{SO}(8)$ and $E_{8} / \operatorname{Spin}(8) \times \operatorname{Spin}(8)$, discovered in AANS (see also [CN, Remark 2.3]),
\item[-] and the unique Kähler-Einstein metric on each of the 13 flag manifolds with second Betti number $b_{2}(M)$ equal to 1, which can be deduced from [AC2, Theorem 3.1] (here $G$ is always an exceptional simple Lie group).
\end{itemize}

It is unknown whether these $G$-stable Einstein metrics are stable, as well as whether they realize the Yamabe invariant of $M$ (i.e., whether $\operatorname{Sc}(g)$ is the supreme among all Yamabe metrics of $M$, which are those with the smallest scalar curvature in its unit volume conformal class).

Remark 1.1. After the first version of the present paper was uploaded to arXiv, many new examples of $G$-stable standard metrics have been found in LaL and the $G$-stable Einstein metric on $E_{7} / \operatorname{SO}(8)$ has been proved to be stable in [SSW].

On the other hand, if $g$ is $G$-unstable, i.e., $\lambda_{L}^{G}<2 \rho$ (or $\operatorname{Sc}_{g}^{\prime \prime}(T, T)>0$ for some $T \in$ $\mathcal{T} \mathcal{T}_{g}^{G}$ ), then $g$ is also dynamically unstable for the normalized Ricci flow, in the sense that there is an ancient solution emerging from $g$ (see [CH, Kr]), and $g$ does not realize the Yamabe invariant of $M$ (see [BWZ, Theorem 5.1]). Excepting the ones described in the two items above, all the homogeneous Einstein metrics studied in this paper were found to be $G$-unstable. Indeed, $G$-instability is considered a generic property of a compact homogeneous Einstein manifold by the experts.

It follows from (2) that the spectrum of the Lichnerowicz Laplacian $\Delta_{L}$ restricted to $\mathcal{T} \mathcal{T}_{g}^{G}$ plays a crucial role in the study of $G$-stability and $G$-non-degeneracy. Consider any reductive decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$ of $M=G / K$ and all the corresponding usual identifications $T_{o} M \equiv \mathfrak{p}, \mathcal{S}^{2}(M)^{G} \equiv \operatorname{sym}(\mathfrak{p})^{K}$, etc. According to [L, Lemma 4.7], for any $g \in \mathcal{M}^{G}$,
$$\Delta_{L} T=\left\langle\mathrm{L}_{\mathfrak{p}} A \cdot, \cdot\right\rangle, \quad \forall T \in \mathcal{T} \mathcal{T}_{g}^{G}, \quad T=\langle A \cdot, \cdot\rangle \in \mathcal{S}^{2}(M)^{G}, \quad A \in \operatorname{sym}(\mathfrak{p})^{K},$$
where $\mathrm{L}_{\mathfrak{p}}=\mathrm{L}_{\mathfrak{p}}(g): \operatorname{sym}(\mathfrak{p}) \longrightarrow \operatorname{sym}(\mathfrak{p})$ is the self-adjoint operator defined by
$$\left\langle\mathrm{L}_{\mathfrak{p}} A, B\right\rangle=\frac{1}{2}\left\langle\theta(A) \mu_{\mathfrak{p}}, \theta(B) \mu_{\mathfrak{p}}\right\rangle+2 \operatorname{tr} \mathrm{M}_{\mu_{\mathfrak{p}}} A B, \quad \forall A, B \in \operatorname{sym}(\mathfrak{p}),$$
and $\langle\cdot, \cdot\rangle$ is determined by $g$. Here $\mu_{\mathfrak{p}}:=\left.\operatorname{pr}_{\mathfrak{p}} \circ \mu\right|_{\mathfrak{p} \times \mathfrak{p}}: \mathfrak{p} \times \mathfrak{p} \longrightarrow \mathfrak{p}$ and $\mathrm{M}: \Lambda^{2} \mathfrak{p}^{*} \otimes \mathfrak{p} \rightarrow$ $\operatorname{sym}(\mathfrak{p})$ is the moment map for the usual representation $\theta$ of $\mathfrak{g} \mathfrak{l}(\mathfrak{p})$ on $\Lambda^{2} \mathfrak{p}^{*} \otimes \mathfrak{p}$ (see \$2.2). Thus $\lambda_{L}^{G}$ (denoted by $\lambda_{\mathfrak{p}}$ in subsequent sections) is the smallest eigenvalue of the operator $\mathrm{L}_{\mathfrak{p}}$ restricted to $\operatorname{sym}(\mathfrak{p})^{K}$ (modulo trivial variations). This was applied to the naturally reductive case in [L], where formula (3) considerably simplifies.

In this paper, we give a formula for the Lichnerowicz Laplacian $\mathrm{L}_{\mathfrak{p}}$ in the general case, in terms of the well-known structural constants $[i j k]$ 's of $G / K$ relative to a $Q$-orthogonal decomposition $\mathfrak{p}=\mathfrak{p}_{1} \oplus \cdots \oplus \mathfrak{p}_{r}$ in $\operatorname{Ad}(K)$-invariant subspaces, where $Q$ is any bi-invariant inner product on $\mathfrak{g}$ (see (14)). Assume that the subspaces $\mathfrak{p}_{k}$ 's are all $\operatorname{Ad}(K)$-irreducible and pairwise inequivalent, which implies that $\left\{\frac{1}{\sqrt{d_{1}}} I_{1}, \ldots, \frac{1}{\sqrt{d_{r}}} I_{r}\right\}$ is an orthonormal basis of $\operatorname{sym}(\mathfrak{p})^{K}$, where $d_{k}:=\operatorname{dim} \mathfrak{p}_{k}$ and $\left.I_{k}\right|_{\mathfrak{p}_{i}}:=\delta_{k i} I$.
Theorem 1.2. (See Theorem 3.1). For any metric $g=\left.x_{1} Q\right|_{\mathfrak{p}_{1}}+\cdots+\left.x_{r} Q\right|_{\mathfrak{p}_{r}} \in \mathcal{M}^{G}$, the entries of the matrix of $\mathrm{L}_{\mathfrak{p}}$ with respect to the above basis are given by
$$\left[\mathrm{L}_{\mathfrak{p}}\right]_{k k}=\frac{1}{d_{k}} \sum_{i, j \neq k} \frac{x_{k}}{x_{i} x_{j}}[i j k]+\frac{1}{d_{k}} \sum_{i \neq k} \frac{x_{i}}{x_{k}^{2}}[i k k], \quad\left[\mathrm{L}_{\mathfrak{p}}\right]_{k m}=\frac{1}{\sqrt{d_{k}} \sqrt{d_{m}}} \sum_{i} \frac{x_{i}^{2}-x_{k}^{2}-x_{m}^{2}}{x_{i} x_{k} x_{m}}[i k m] .$$

The formula is also useful beyond the multiplicity-free case, see Remarks 3.3 and 3.4. Theorem 1.2 allows the systematic computation of the spectrum of $\mathrm{L}_{\mathfrak{p}}$ for any homogeneous Einstein metric available in the literature, provided that the numbers $d_{k}$ 's and $[i j k]$ 's are known for the homogeneous space. This is usually the case since Einstein equations are often written in terms of these numbers (see §2.5).

The rest of the paper is explorative in nature. In §4, we use the formula in Theorem 1.2 to compute the spectrum of the Lichnerowicz Laplacian $\mathrm{L}_{\mathfrak{p}}$ for all Einstein metrics on any generalized Wallach space $G / K$ with $G$ simple (5 infinite families and

10 exceptional examples; each space admits between 2 and 4 Einstein metrics), except $\operatorname{SO}(k+l+m) / \operatorname{SO}(k) \times \operatorname{SO}(l) \times \operatorname{SO}(m)$ and $\operatorname{Sp}(k+l+m) / \operatorname{Sp}(k) \times \operatorname{Sp}(l) \times \operatorname{Sp}(m)$, where $k, l, m$ are pairwise different. We also apply Theorem 1.2 in §5 to do the same for all Einstein metrics on flag manifolds with $b_{2}(M)=1$ (13 exceptional examples, each one admitting between 3 and 6 Einstein metrics). The $G$-stability and critical point types of each of these metrics so obtained are collected in Tables 2, 6, 8 and Tables 12, 15, respectively. The most noteworthy finds of our exploration are:
\begin{itemize}
\item[-] The only local maxima of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ are the standard metrics on SU(2), $E_{7} / \mathrm{SO}(8)$ and $E_{8} / \operatorname{Spin}(8) \times \operatorname{Spin}(8)$, and the Kähler metrics on the flag manifolds with $b_{2}(M)=1$. However, the Kähler-Einstein metrics on flag manifolds with $b_{2}(M)=2$ and three isotropy summands are never local maxima (cf. [CHI]).
\item[-] Any standard Einstein metric on a generalized Wallach space (3 infinite families and 7 isolated examples) is either a local maximum or a local minimum of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$. The value of the volume normalized scalar curvature $\mathrm{Sc}_{N}$ at the standard metric is always strictly less than for all the other Einstein metrics, except precisely in the cases when it is a local maximum.
\item[-] A generalized Wallach space admits a local minimum if and only if it admits four Einstein metrics.
\item[-] For any of the three Kähler-Einstein metrics on any of the generalized Wallach spaces which are also flag manifolds (necessarily with $b_{2}(M)=2$ ), the kernel of the Lichnerowicz Laplacian $\left.\Delta_{L}\right|_{\mathcal{T} \mathcal{T}_{g}^{G}}$ is non-trivial. By [LW], this implies that there exists a symmetric 2-tensor $T$ as close to $\operatorname{Rc}(g)$ as you like such that either the existence or the (local) uniqueness of a solution to the prescribed Ricci curvature problem $\operatorname{Rc}\left(g^{\prime}\right)=c T$ fail (see §4.4). Indeed, for each of these Kähler-Einstein metrics $g_{K E}$, we provide a pairwise non-homothetic curve $g_{t}, t \in[1, \infty)$ of $G$-invariant metrics $\left(\operatorname{Sc}\left(g_{t}\right)\right.$ is strictly increasing) having the same volume as $g_{1}=g_{K E}$ and such that $\operatorname{Rc}\left(g_{t}\right)=\operatorname{Rc}\left(g_{K E}\right)$ for all $t \geq 1$. This only happens for these metrics, all the other ones are Ricci locally invertible.
\item[-] All the Einstein metrics studied are non-degenerate critical points of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ and in particular $G$-rigid. The $G$-rigidity was previously known, it follows from the finiteness (up to scaling) of the set of Einstein metrics on each of these homogeneous spaces (see [LNF, Ar]).
\item[-] Any non-Kähler Einstein metric on a flag manifold with $b_{2}(M)=1$ is a saddle point of coindex 1, except for one of the metrics on each of the three spaces $E_{8} / \operatorname{SU}(10) \times$ $\operatorname{SU}(3) \times \operatorname{SU}(1), E_{8} / \operatorname{SU}(5) \times \operatorname{SU}(4) \times \mathrm{U}(1)$ and $E_{8} / \mathrm{SU}(5) \times \operatorname{SU}(3) \times \operatorname{SU}(2) \times \mathrm{U}(1)$, which has coindex 2.
\end{itemize}

The normalized Ricci flow on $\mathcal{M}_{1}^{G}$ is precisely the gradient flow of Sc, whose dynamical behavior is mostly governed by the $G$-stability types of their fixed points, the $G$-invariant Einstein metrics. The Ricci flow on generalized Wallach spaces was studied in [AANS], where the authors prove that, generically, there are only three possible dynamical behaviors. Our approach provides an alternative proof for that. On flag manifolds with $b_{2}(M)=1$, the dimension of the unstable manifold for each fixed point at the infinity is given in [AC2, Theorem 3.1]. It can be shown that such dimension is precisely one more than the coindex of the corresponding critical point. Our computations of the coindex agree with these results.

Remark 1.3. (cf. [CH, Remark 1.6]). As proposed in [GHP], higher-dimensional versions of the spherically symmetric Schwarzschild black hole can be constructed by replacing the 2-sphere with other compact Einstein manifolds. The instability condition for the
$(n+2)$-dimensional black hole obtained is given by
$$\lambda_{L}<\frac{\rho}{n-1}\left(4-\frac{(n-5)^{2}}{4}\right)=\rho\left(\frac{9-n}{4}\right),$$
where $\lambda_{L}$ and $\rho$ correspond to the Einstein manifold $M^{n}$. It is also proved in [GHP] that this instability criterion is identical to that for the instability of the Freund-Rubin compactification $A d S_{m} \times M^{n}$ in the context of the AdS/CFT correspondence. Remarkably, among all the homogeneous Einstein manifolds studied in this paper, in spite of $\lambda_{L}^{G}$ is in many cases negative (recall that $\lambda_{L} \leq \lambda_{L}^{G}$ ), the Einstein-Kähler metric on the full flag manifold $M^{6}=\operatorname{SU}(3) / \mathrm{S}\left(\mathrm{U}(1)^{3}\right)$ (which is not the standard metric) is the only one satisfying the instability condition above with $\lambda_{L}$ replaced by $\lambda_{L}^{G}$. Since $\lambda_{L}^{G}=0$ for this particular metric (see Table 2, line $W_{2}, k=1$ ), it follows that $\lambda_{L} \leq 0$, providing an 8-dimensional generalized black hole which is unstable. Topologically, $M^{6}$ is the projective holomorphic tangent bundle of $\mathbb{C} P^{2}$ (see [B, Example 13.80 and Chapter 8]).

Acknowledgements. We are very grateful with Ioannis Chrysikos, Lino Grama, Yurii Nikonorov and Wolfgang Ziller for many helpful conversations.

\section*{2. Preliminaries}

Let $M$ be a compact connected differentiable manifold. We assume that $M$ is homogeneous and fix an almost-effective transitive action of a compact Lie group $G$ on $M$. The $G$ -action determines a presentation $M=G / K$ of $M$ as a homogeneous space, where $K \subset G$ is the isotropy subgroup at some point $o \in M$. Let $\mathcal{M}^{G}$ denote the finite-dimensional manifold of all $G$-invariant Riemannian metrics on $M$.

It is well known that $g \in \mathcal{M}_{1}^{G}$ is Einstein, i.e., $\operatorname{Rc}(g)=\rho g$ for some $\rho \in \mathbb{R}$ (which is necessarily positive if $G$ is non-abelian), if and only if $g$ is a critical point of the scalar curvature functional Sc : $\mathcal{M}_{1}^{G} \longrightarrow \mathbb{R}$, where $\mathcal{M}_{1}^{G} \subset \mathcal{M}^{G}$ is the codimension one submanifold of all unit volume metrics. We study in this paper the stability of $G$-invariant Einstein metrics on $M$ as critical points of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$, which is encoded in the signature of the second derivative or Hessian Sc''. We refer to [L] for a more detailed treatment.
2.1. $G$-stability. The tangent space of $\mathcal{M}_{1}^{G}$ at $g$ is given by the subspace of $\mathcal{S}^{2}(M)^{G}$ of $g$-traceless elements, where $\mathcal{S}^{2}(M)^{G}$ is the space of all $G$-invariant symmetric 2-tensors. It follows from [L, Corollary 3.12] that
$$T_{g} \mathcal{M}_{1}^{G}=T_{g} \operatorname{Aut}(G / K) \cdot g \oplus \mathcal{T} \mathcal{T}_{g}^{G},$$
where $\operatorname{Aut}(G / K) \subset \operatorname{Diff}(M)$ is the Lie group of automorphisms of $G$ taking $K$ onto $K$, acting by pullback on $\mathcal{M}^{G}$ (i.e., $T_{g} \operatorname{Aut}(G / K) \cdot g$ is the space of trivial variations of $g$ ), and $\mathcal{T} \mathcal{T}_{g}^{G}:=\left(\operatorname{Ker} \delta_{g} \cap \operatorname{Ker}_{\operatorname{tr}}\right)^{G}$ is the space of $G$-invariant TT-tensors. Note that since $G$ is compact, $T_{g} \operatorname{Aut}(G / K) \cdot g=T_{g} N_{G}(K) \cdot g$, where $N_{G}(K)$ is the normalizer of $K$ in $G$ and so $T_{g} N_{G}(K) \cdot g$ is the tangent space of the $G$-equivariant isometry class of $g$ (see L, §3.3]).
Definition 2.1. An Einstein metric $g \in \mathcal{M}_{1}^{G}$ is said to be,
\begin{itemize}
\item[-] $G$-stable: $\left.\mathrm{Sc}_{g}^{\prime \prime}\right|_{\mathcal{T}_{g}^{G}}<0$ (in particular, $g$ is a local maximum of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ ).
\item[-] $G$-unstable: $\operatorname{Sc}_{g}^{\prime \prime}(T, T)>0$ for some $T \in \mathcal{T} \mathcal{T}_{g}^{G}$ ( $g$ is a saddle point, unless $\left.\operatorname{Sc}_{g}^{\prime \prime}\right|_{\mathcal{T} \mathcal{T}_{g}^{G}}>0$, in which case $g$ is a local minimum of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ ). The coindex is the dimension of the maximal subspace of $\mathcal{T} \mathcal{T}_{g}^{G}$ on which $\mathrm{Sc}_{g}^{\prime \prime}$ is positive definite.
\item[-] $G$-non-degenerate: $\left.\mathrm{Sc}_{g}^{\prime \prime}\right|_{\mathcal{T} \mathcal{T}_{g}^{G}}$ is non-degenerate (thus $g$ is $G$-rigid, in the sense that it is an isolated critical point up to the $\operatorname{Aut}(G / K)$-action), and otherwise, $G$-degenerate.
\end{itemize}

Recall that without assuming $G$-invariance, the classical stability of $g$ means that $\mathrm{Sc}_{g}^{\prime \prime}$ is negative definite on $\mathcal{T} \mathcal{T}_{g}$, the infinite dimensional vector space of all unit volume constant scalar curvature (non-trivial) variations of $g$.

It is worth noticing that the space of trivial variations vanishes, i.e., $T_{g} \mathcal{M}_{1}^{G}=\mathcal{T} \mathcal{T}_{g}^{G}$, under any of the following conditions: $g$ is naturally reductive with respect to $G$; the isotropy representation does not contain the trivial representation; $G$ is semisimple and the isotropy representation is mutiplicity-free (i.e., any two different $\operatorname{Ad}(K)$-invariant irreducible subspaces are inequivalent as $\operatorname{Ad}(K)$-representations), e.g., when $\operatorname{rk}(G)=\operatorname{rk}(K)$ (see [L, §3.3]).
2.2. Ricci curvature. Given a compact homogeneous space $M=G / K$ as above, we consider any reductive decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$, giving rise to the usual identification $T_{o} M \equiv \mathfrak{p}$, where $\mathfrak{g}$ and $\mathfrak{k}$ are the Lie algebras of $G$ and $K$, respectively. Let $\mu$ denote the Lie bracket of $\mathfrak{g}$. We extend $\langle\cdot, \cdot\rangle:=g_{o}$ in the usual way to inner products on $\mathfrak{g l}(\mathfrak{p})$ and $\Lambda^{2} \mathfrak{p}^{*} \otimes \mathfrak{p}$, respectively:
$$\langle A, B\rangle:=\operatorname{tr} A B^{t}, \quad\langle\lambda, \lambda\rangle:=\sum\left|\operatorname{ad}_{\lambda} X_{i}\right|^{2}=\sum\left|\lambda\left(X_{i}, X_{j}\right)\right|^{2},$$
where $\left\{X_{i}\right\}$ is any orthonormal basis of $\mathfrak{p}$ relative to $\langle\cdot, \cdot\rangle$. If
$$\mu_{\mathfrak{p}}:=\left.\operatorname{pr}_{\mathfrak{p}} \circ \mu\right|_{\mathfrak{p} \times \mathfrak{p}}: \mathfrak{p} \times \mathfrak{p} \longrightarrow \mathfrak{p},$$
where $\mathrm{pr}_{\mathfrak{p}}: \mathfrak{g} \rightarrow \mathfrak{p}$ is the projection on $\mathfrak{p}$ relative to $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$, then the Ricci operator $\operatorname{Ric}(g)$ of the metric $g$ is given by
$$\operatorname{Ric}(g)=\mathrm{M}_{\mu_{\mathfrak{p}}}-\frac{1}{2} \mathrm{~B}_{\mu},$$
where $\left\langle\mathrm{B}_{\mu} \cdot, \cdot\right\rangle:=\left.\mathrm{B}_{\mathfrak{g}}\right|_{\mathfrak{p} \times \mathfrak{p}}, \mathrm{B}_{\mathfrak{g}}$ denotes the Killing form of the Lie algebra $\mathfrak{g}$ and
$$\left\langle\mathrm{M}_{\mu_{\mathfrak{p}}}, A\right\rangle:=\frac{1}{4}\left\langle\theta(A) \mu_{\mathfrak{p}}, \mu_{\mathfrak{p}}\right\rangle, \quad \forall A \in \mathfrak{g} \mathfrak{l}(\mathfrak{p}) .$$
Here $\theta$ is the representation of $\mathfrak{g l}(\mathfrak{p})$ given by,
$$\theta(A) \lambda:=A \lambda(\cdot, \cdot)-\lambda(A \cdot, \cdot)-\lambda(\cdot, A \cdot), \quad \forall A \in \mathfrak{g} \mathfrak{l}(\mathfrak{p}), \quad \lambda \in \Lambda^{2} \mathfrak{p}^{*} \otimes \mathfrak{p} .$$
The function $\mathrm{M}: \Lambda^{2} \mathfrak{p}^{*} \otimes \mathfrak{p} \rightarrow \operatorname{sym}(\mathfrak{p})$ is therefore the moment map from geometric invariant theory (see e.g. [BL] and the references therein) for the representation $\theta$ of $\mathfrak{g l}(\mathfrak{p})$. Alternatively, the moment map can be defined by,
$$\left\langle\mathrm{M}_{\mu_{\mathfrak{p}}} X, X\right\rangle=-\frac{1}{2} \sum\left\langle\mu_{\mathfrak{p}}\left(X, X_{i}\right), X_{j}\right\rangle^{2}+\frac{1}{4} \sum\left\langle\mu_{\mathfrak{p}}\left(X_{i}, X_{j}\right), X\right\rangle^{2}, \quad \forall X \in \mathfrak{p} .$$
It follows from (7) and (8) that
$$\operatorname{Sc}(g)=-\frac{1}{4}\left|\mu_{\mathfrak{p}}\right|^{2}-\frac{1}{2} \operatorname{tr} \mathrm{~B}_{\mu} .$$
We refer to [LfL] for more details on this formula for the Ricci curvature from the moving bracket approach point of view.
2.3. Lichnerowicz Laplacian. It is well known that the second variation of the total scalar curvature at any Einstein metric $g$ on $M$, say with $\operatorname{Rc}(g)=\rho g$, is given on $\mathcal{T} \mathcal{T}_{g}$ by
$$\mathrm{Sc}_{g}^{\prime \prime}=\frac{1}{2}\left\langle\left(2 \rho \mathrm{id}-\Delta_{L}\right) \cdot, \cdot\right\rangle_{g},$$
where $\Delta_{L}$ is the Lichnerowicz Laplacian of $g$ (see [B, 4.64]). Consider the self-adjoint operator
$$\mathrm{L}_{\mathfrak{p}}=\mathrm{L}_{\mathfrak{p}}(g): \operatorname{sym}(\mathfrak{p}) \longrightarrow \operatorname{sym}(\mathfrak{p}), \quad \operatorname{sym}(\mathfrak{p}):=\left\{A: \mathfrak{p} \rightarrow \mathfrak{p}: A^{t}=A\right\},$$
defined by
$$\left\langle\mathrm{L}_{\mathfrak{p}} A, B\right\rangle=\frac{1}{2}\left\langle\theta(A) \mu_{\mathfrak{p}}, \theta(B) \mu_{\mathfrak{p}}\right\rangle+2 \operatorname{tr} \mathrm{M}_{\mu_{\mathfrak{p}}} A B . \quad \forall A, B \in \operatorname{sym}(\mathfrak{p}) .$$

It is proved in [L, Lemma 4.7] that this is precisely the operator defined by $\Delta_{L}$ under the usual identifications, that is,
$$\Delta_{L} T=\left\langle\mathrm{L}_{\mathfrak{p}} A \cdot, \cdot\right\rangle, \quad \forall T \in \mathcal{T} \mathcal{T}_{g}^{G}, \quad T=\langle A \cdot, \cdot\rangle \in \mathcal{S}^{2}(M)^{G}, \quad A \in \operatorname{sym}(\mathfrak{p})^{K},$$
where
$$\operatorname{sym}(\mathfrak{p})^{K}:=\{A \in \operatorname{sym}(\mathfrak{p}):[\operatorname{Ad}(K), A]=0\} \equiv \mathcal{S}^{2}(M)^{G} .$$
According to (11), the $G$-stability type of $g$ is therefore determined by how is the constant $2 \rho$ suited relative to the spectrum of the Lichnerowicz Laplacian $\mathrm{L}_{\mathfrak{p}}$. If $\lambda_{\mathfrak{p}}=\lambda_{\mathfrak{p}}(g)$ and $\lambda_{\mathfrak{p}}^{\text {max }}=\lambda_{\mathfrak{p}}^{\text {max }}(g)$ denote, respectively, the minimum and maximum eigenvalue of $\mathrm{L}_{\mathfrak{p}}=\mathrm{L}_{\mathfrak{p}}(g)$ restricted to the subspace $\mathcal{T} \mathcal{T}_{g}^{G}$, then an Einstein metric $g \in \mathcal{M}_{1}^{G}$, say $\operatorname{Rc}(g)=\rho g$, is
\begin{itemize}
\item[-] $G$-stable if and only if $2 \rho<\lambda_{\mathfrak{p}}$,
\item[-] $G$-unstable if and only if $\lambda_{\mathfrak{p}}<2 \rho$,
\item[-] $G$-non-degenerate if and only if $2 \rho \notin \operatorname{Spec}\left(\left.\mathrm{~L}_{\mathfrak{p}}\right|_{\mathcal{T} \mathcal{T}_{g}^{G}}\right)$,
\item[-] a local minimum of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ if $\lambda_{\mathfrak{p}}^{\text {max }}<2 \rho$.
\end{itemize}
We note that on trivial variations (see(4)), $\left.\mathrm{L}_{\mathfrak{p}}\right|_{T_{g} \operatorname{Aut}(G / K) \cdot g}=2 \rho$ id (see [L, (30)]). Recall that $\lambda_{\mathfrak{p}}$ was denoted by $\lambda_{L}^{G}$ in §1.

Given an intermediate subgroup $K \subset H \subset N_{G}(K)$, if $\operatorname{sym}(\mathfrak{p})^{H}$ is the subspace of sym $(\mathfrak{p})^{K}$ of those maps which are $\operatorname{Ad}(H)$-invariant, then
$$\mathrm{L}_{\mathfrak{p}} \operatorname{sym}(\mathfrak{p})^{H} \subset \operatorname{sym}(\mathfrak{p})^{H},$$
for any $g \in \mathcal{M}^{G, H}:=\mathcal{M}^{G} \cap \operatorname{sym}(\mathfrak{p})^{H}$, the submanifold of $G$-invariant metrics which are in addition $\operatorname{Ad}(H)$-invariant (see [L, §4.4]). Note that since $\lambda_{\mathfrak{p}} \leq \operatorname{Spec}\left(\left.\mathrm{L}_{\mathfrak{p}}\right|_{\mathcal{T} \mathcal{T}_{g}^{G} \cap \operatorname{sym}(\mathfrak{p})^{H}}\right)$, if the minimum eigenvalue of $\left.\mathrm{L}_{\mathfrak{p}}\right|_{\mathcal{T} \mathcal{T}_{g}^{G} \cap \mathrm{sym}(\mathfrak{p})^{H}}$ is $\leq 2 \rho$, then $g$ is $G$-unstable, and that $g$ is $G$-degenerate if $2 \rho \in \operatorname{Spec}\left(\left.\mathrm{~L}_{\mathfrak{p}}\right|_{\mathcal{T} \mathcal{T}_{g}^{G} \cap \operatorname{sym}(\mathfrak{p})^{H}}\right)$.

Remark 2.2. It may be the case that $\mathcal{M}^{G}=\operatorname{Aut}(G / K) \cdot \mathcal{M}^{G, H}$, that is, any $G$-invariant metric is isometric to an $\operatorname{Ad}(H)$-invariant one. A typical example of this behavior is the Stiefel manifold $\mathrm{SO}(k+2) / \mathrm{SO}(k), k \geq 3$ (see [K, §4] and Examples 3.7 and 3.8 below). Since the function Sc therefore takes the same values on $\mathcal{M}_{1}^{G, H}$ than on $\mathcal{M}_{1}^{G}$, the $G$ -stability and critical point types of an Einstein metric $g \in \mathcal{M}_{1}^{G, H}$ as a critical point of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G, H}}$ and $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ coincide, and so such types can be obtained from the spectrum of $\left.\mathrm{L}_{\mathfrak{p}}\right|_{\mathcal{T} \mathcal{T}_{g}{ }^{G} \cap \operatorname{sym}(\mathfrak{p})^{H}}$.
2.4. Structural constants. We fix a bi-invariant inner product $Q$ on $\mathfrak{g}$ and consider the $Q$-orthogonal reductive decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$, and as a background metric, $\left.Q\right|_{\mathfrak{p}} \in \mathcal{M}^{G}$. For each $Q$-orthogonal decomposition,
$$\mathfrak{p}=\mathfrak{p}_{1} \oplus \cdots \oplus \mathfrak{p}_{r},$$
in $\operatorname{Ad}(K)$-invariant subspaces (not necessarily $\operatorname{Ad}(K)$-irreducible), we denote the corresponding structural constants by
$$[i j k]:=\sum_{\alpha, \beta, \gamma} Q\left(\left[e_{\alpha}^{i}, e_{\beta}^{j}\right], e_{\gamma}^{k}\right)^{2},$$
where $\left\{e_{\alpha}^{i}\right\},\left\{e_{\beta}^{j}\right\}$ and $\left\{e_{\gamma}^{k}\right\}$ are $Q$-orthonormal basis of $\mathfrak{p}_{i}, \mathfrak{p}_{j}$ and $\mathfrak{p}_{k}$, respectively. Note that $[i j k]$ is invariant under any permutation of $i j k$ and it vanishes if and only if $\left[\mathfrak{p}_{i}, \mathfrak{p}_{j}\right] \perp$ $\mathfrak{p}_{k}$. These numbers have been strongly used in the literature since McKenzie Wang and Wolfgang Ziller introduced them in their pioneering article [WZ].

For each $g \in \mathcal{M}^{G}$, there exists at least one decomposition as in (13) which is also $g$-orthogonal and
$$g=\left.x_{1} Q\right|_{\mathfrak{p}_{1}}+\cdots+\left.x_{r} Q\right|_{\mathfrak{p}_{r}}, \quad x_{i}>0 .$$
The metric $g$ will often be denoted by $\left(x_{1}, \ldots, x_{r}\right)$. We note that
$$\left|\mu_{\mathfrak{p}}\right|^{2}=\sum_{i, j, k} \frac{x_{k}}{x_{i} x_{j}}[i j k],$$
as $\left\{\frac{1}{\sqrt{x_{i}}} e_{\alpha}^{i}\right\}$ is a $g$-orthonormal basis of $\mathfrak{p}_{i}$ for all $i$.
2.5. Einstein equations. Recall from (6) that the Ricci operator of $g$ is given by $\operatorname{Ric}(g)=$ $\mathrm{M}_{\mu_{\mathfrak{p}}}-\frac{1}{2} \mathrm{~B}_{\mu}$. If we assume that, for each $k,\left.\mathrm{M}_{\mu_{\mathfrak{p}}}\right|_{\mathfrak{p}_{k}}=m_{k} I_{\mathfrak{p}_{k}}$ for some $m_{k} \in \mathbb{R}$ ( $I_{\mathfrak{s}}$ denotes the identity map on $\mathfrak{s}$ for any vector space $\mathfrak{s}$ ), then it follows from (9) that
$$m_{k}=-\frac{1}{2 d_{k}} \sum_{i, j} \frac{x_{j}}{x_{i} x_{k}}[i j k]+\frac{1}{4 d_{k}} \sum_{i, j} \frac{x_{k}}{x_{i} x_{j}}[i j k], \quad \forall k=1, \ldots, r,$$
where $d_{k}:=\operatorname{dim} \mathfrak{p}_{k}$ and $g=\left(x_{1}, \ldots, x_{r}\right)$. Let us also assume that $-\left.\mathrm{B}_{\mathfrak{g}}\right|_{\mathfrak{p}_{k} \times \mathfrak{p}_{k}}=b_{k} Q$, $b_{k} \in \mathbb{R}$, which implies that $\left.\mathrm{B}_{\mu}\right|_{\mathfrak{p}_{k}}=-\frac{b_{k}}{x_{k}} I_{\mathfrak{p}_{k}}$. Note that $b_{k} \geq 0$, where equality holds if and only if $\mathfrak{p}_{k} \subset \mathfrak{z}(\mathfrak{g})$, and that if $G$ is semisimple and $Q=-\mathrm{B}_{\mathfrak{g}}$, then $b_{k}=1$ for all $k$.

We therefore obtain that
$$\left.\operatorname{Ric}(g)\right|_{\mathfrak{p}_{k}}=\rho_{k} I_{\mathfrak{p}_{k}}, \quad \rho_{k}=\frac{b_{k}}{2 x_{k}}+m_{k},$$
where each number $\rho_{k}$ can be written in the following ways:
$$\begin{aligned}
\rho_{k} & =\frac{b_{k}}{2 x_{k}}-\frac{1}{2 d_{k}} \sum_{i, j} \frac{x_{j}}{x_{i} x_{k}}[i j k]+\frac{1}{4 d_{k}} \sum_{i, j} \frac{x_{k}}{x_{i} x_{j}}[i j k], \\
& =\frac{b_{k}}{2 x_{k}}-\frac{1}{4 d_{k}} \sum_{i, j}\left(\frac{x_{i}}{x_{j} x_{k}}+\frac{x_{j}}{x_{i} x_{k}}-\frac{x_{k}}{x_{i} x_{j}}\right)[i j k], \\
& =\frac{b_{k}}{2 x_{k}}-\frac{1}{4 d_{k}} \sum_{i, j} \frac{x_{i}^{2}+x_{j}^{2}-x_{k}^{2}}{x_{i} x_{j} x_{k}}[i j k] .
\end{aligned}$$
The Einstein equations therefore become: $\operatorname{Ric}(g)=\rho I$ if and only if
$$\rho_{k}=\rho, \quad \forall k=1, \ldots, r \quad \text { and } \quad\left\langle\operatorname{Ric}(g) \mathfrak{p}_{i}, \mathfrak{p}_{j}\right\rangle=0, \quad \forall i \neq j .$$
The two assumptions we have made above (namely, $\left.\mathrm{M}_{\mu_{\mathfrak{p}}}\right|_{\mathfrak{p}_{k}}=m_{k} I_{\mathfrak{p}_{k}}$ and $-\left.\mathrm{B}_{\mathfrak{g}}\right|_{\mathfrak{p}_{k}}=$ $\left.b_{k} Q\right|_{\mathfrak{p}_{k}}$ ) hold, for instance, in the case when the $\mathfrak{p}_{k}$ 's are all $\operatorname{Ad}(K)$-irreducible, or more in general, if they are all $\operatorname{Ad}(H)$-invariant and irreducible for some intermediate subgroup $K \subset H \subset N_{G}(K)$. If in addition the $\mathfrak{p}_{k}$ 's are pairwise inequivalent as $K$-representations (resp. $H$-representations), then any $G$-invariant (resp. $(G \times H)$-invariant) metric is of the form (15) and the right-hand side Einstein equations are automatically fulfilled.

These intermediate subgroups $K \subset H \subset N_{G}(K)$ can be used to search for Einstein metrics in the difficult case when $G / K$ is not multiplicity-free (see [S] and references therein).

Example 2.3. The isotropy representation $\mathfrak{p}$ of $\operatorname{SO}(7) / \operatorname{SO}(2)$ is highly non-multiplicity free, it decomposes in 10 one-dimensional and 5 two-dimensional irreducible SO(2)-subrepresentations. However, for the subgroup $H=\mathrm{SO}(4) \times \mathrm{SO}(2)$ of the normalizer of $\mathrm{SO}(2)$, $\mathfrak{p}$ only admits 4 inequivalent $\operatorname{Ad}(H)$-irreducible subspaces of dimensions 2, 4, 6 and 8, respectively.
2.6. Scalar curvature. It follows from (10) and (16) (or alternatively, from (18)) that the scalar curvature of a metric $g=\left(x_{1}, \ldots, x_{r}\right)$ is given by
$$\operatorname{Sc}(g)=\frac{1}{2} \sum_{k} \frac{b_{k} d_{k}}{x_{k}}-\frac{1}{4} \sum_{i, j, k} \frac{x_{k}}{x_{i} x_{j}}[i j k] .$$
We note that this formula is assuming nothing about $\mathrm{M}_{\mu_{\mathfrak{p}}}$, and if we set $Q:=-\mathrm{B}_{\mathfrak{g}}$ in the case when $G$ is semisimple, then $b_{k}=1$ for all $k$ and the formula is valid for any $\operatorname{Ad}(K)$-invariant decomposition as in (13).

A useful homothety invariant of $g$ is the volume normalized scalar curvature defined by
$$\operatorname{Sc}_{N}(g):=\left(\operatorname{det}_{Q} g\right)^{\frac{1}{n}} \operatorname{Sc}(g)=\left(x_{1}^{d_{1}} \ldots x_{r}^{d_{r}}\right)^{\frac{1}{n}} \operatorname{Sc}(g) .$$
Note that $g \in \mathcal{M}^{G}$ is Einstein if and only if $g$ is a critical point of $\operatorname{Sc}_{N}: \mathcal{M}^{G} \rightarrow \mathbb{R}$.
If $G / K$ is not multiplicity-free, then it is sometimes useful to use instead formula (10) for the scalar curvature to find Einstein metrics (see [K]).

\section*{3. A formula for $\mathrm{L}_{\mathfrak{p}}$ in terms of structural constants}

Let $g$ be a $G$-invariant metric on a connected homogeneous space $M=G / K$ with $G$ compact and $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$ a reductive decomposition as in §2.4. Recall that $\mathrm{L}_{\mathfrak{p}} \operatorname{sym}(\mathfrak{p})^{H} \subset$ $\operatorname{sym}(\mathfrak{p})^{H}$ for any intermediate subgroup $K \subset H \subset N_{G}(K)$, so
$$\operatorname{Spec}\left(\left.L_{\mathfrak{p}}\right|_{\operatorname{sym}(\mathfrak{p})^{H}}\right) \subset \operatorname{Spec}\left(\left.L_{\mathfrak{p}}\right|_{\operatorname{sym}(\mathfrak{p})^{K}}\right) .$$
In the case when $\mathfrak{p}$ is $\operatorname{Ad}(H)$-multiplicity-free, we consider the orthonormal basis of $\operatorname{sym}(\mathfrak{p})^{H}$ given by,
$$\left\{\frac{1}{\sqrt{d_{1}}} I_{1}, \ldots, \frac{1}{\sqrt{d_{r}}} I_{r}\right\},$$
where $I_{k}$ is the block map $\left[0, \ldots, 0, I_{\mathfrak{p}_{k}}, 0, \ldots, 0\right]$ of $\mathfrak{p}$.
Theorem 3.1. Assume that the subspaces $\mathfrak{p}_{k}$ 's are all $\operatorname{Ad}(H)$-invariant, $\operatorname{Ad}(H)$-irreducible and pairwise inequivalent for some intermediate subgroup $K \subset H \subset N_{G}(K)$. Then, for any metric $g=\left(x_{1}, \ldots, x_{r}\right)$, the entries of the matrix of the Lichnerowicz Laplacian $\mathrm{L}_{\mathfrak{p}}$ with respect to the orthonormal basis (21) of $\operatorname{sym}(\mathfrak{p})^{H}$ are given by
$$\left[\mathrm{L}_{\mathfrak{p}}\right]_{k k}=\frac{1}{d_{k}} \sum_{i, j \neq k} \frac{x_{k}}{x_{i} x_{j}}[i j k]+\frac{1}{d_{k}} \sum_{i \neq k} \frac{x_{i}}{x_{k}^{2}}[i k k], \quad \forall k=1, \ldots, r,$$
and
$$\left[\mathrm{L}_{\mathfrak{p}}\right]_{k m}=\frac{1}{\sqrt{d_{k}} \sqrt{d_{m}}} \sum_{i} \frac{x_{i}^{2}-x_{k}^{2}-x_{m}^{2}}{x_{i} x_{k} x_{m}}[i k m], \quad \forall k \neq m .$$

Remark 3.2. In the case when $H=K$, i.e., $G / K$ is multiplicity-free, this is indeed the matrix of $\mathrm{L}_{\mathfrak{p}}: \operatorname{sym}(\mathfrak{p})^{K} \rightarrow \operatorname{sym}(\mathfrak{p})^{K}$.

Remark 3.3. The spectrum of the symmetric $r \times r$ matrix given in the theorem, restricted to the hyperplane $\left\{\left(a_{1}, \ldots, a_{r}\right): \sum \sqrt{d_{i}} a_{i}=0\right\}$ (which corresponds to $\operatorname{sym}_{0}(\mathfrak{p})^{H}$ ), is therefore contained in $\left[\lambda_{\mathfrak{p}}, \lambda_{\mathfrak{p}}^{\text {max }}\right]$ (see §2.3), providing estimates which are very useful in the study of the $G$-stability of an Einstein metric $g$.

Remark 3.4. If the decomposition $\mathfrak{p}=\mathfrak{p}_{1} \oplus \cdots \oplus \mathfrak{p}_{r}$ is only assumed to be $\operatorname{Ad}(K)$-invariant and we call $L$ the symmetric $r \times r$ matrix defined as in the above theorem using the corresponding structural constants, then $L$ is a principal submatrix of the matrix of $\left.\mathrm{L}_{\mathfrak{p}}\right|_{\operatorname{sym}(\mathfrak{p})^{K}}$ and so the spectrum of $L$ restricted to the hyperplane $\sum \sqrt{d_{i}} a_{i}=0$ (intersected with $\mathcal{T} \mathcal{T}_{g}^{G}$ if necessary) lies in $\left[\lambda_{\mathfrak{p}}, \lambda_{\mathfrak{p}}^{\text {max }}\right]$. In particular, the $G$-instability of an Einstein metric $g$ (say $\operatorname{Rc}(g)=\rho g)$ follows as soon as some eigenvalue of $L$ is less than $2 \rho$.

Proof. Recall from 42.2 that $g$ defines inner products on $\operatorname{sym}(\mathfrak{p})$ and $\Lambda^{2} \mathfrak{p}^{*} \otimes \mathfrak{p}$ both denoted by $\langle\cdot, \cdot\rangle$. According to the definition of the operator $\mathrm{L}_{\mathfrak{p}}$ given in (12),
$$\left\langle\mathrm{L}_{\mathfrak{p}} I_{k}, I_{m}\right\rangle=\frac{1}{2}\left\langle\theta\left(I_{m}\right) \theta\left(I_{k}\right) \mu_{\mathfrak{p}}, \mu_{\mathfrak{p}}\right\rangle+2 m_{k}\left\langle I_{k}, I_{m}\right\rangle, \quad \forall k, m .$$
If we write $\mu_{\mathfrak{p}}: \mathfrak{p} \times \mathfrak{p} \rightarrow \mathfrak{p}$ (see (5)) as
$$\mu_{\mathfrak{p}}=\sum_{i, j, l} \mu_{i j}^{l}, \quad \mu_{i j}^{l}: \mathfrak{p}_{i} \times \mathfrak{p}_{j} \longrightarrow \mathfrak{p}_{l},$$
then following properties can be easily checked:
\begin{itemize}
\item[-] $\mu_{i j}^{l}(X, Y)=-\mu_{j i}^{l}(Y, X)$ for all $X \in \mathfrak{p}_{i}, Y \in \mathfrak{p}_{j}$,
\item[-] $\mu_{i j}^{l} \perp \mu_{i^{\prime} j^{\prime}}^{l^{\prime}}$ for any $(i, j, l) \neq\left(i^{\prime}, j^{\prime}, l^{\prime}\right)$,
\item[-] $\left|\mu_{i j}^{l}\right|^{2}=\frac{x_{l}}{x_{i} x_{j}}[i j l]$; in particular, $\sum_{i, j, k} \frac{x_{k}}{x_{i} x_{j}}[i j k]=\left|\mu_{\mathfrak{p}}\right|^{2}$.
\end{itemize}

Using (8) we obtain that
$$\theta\left(I_{k}\right) \mu_{i j}^{l}=\left\{\begin{array}{cl}
0, & k \neq i, j, l, \\
-\mu_{k j}^{l}, & k=i \neq j, l, \\
-\mu_{i k}^{l}, & k=j \neq i, l, \\
-2 \mu_{k k}^{l}, & k=i=j \neq l, \\
\mu_{i j}^{k}, & k=l \neq i, j, \\
0, & k=l=i \neq j, \\
0, & k=l=j \neq i, \\
-\mu_{k k}^{k}, & k=l=i=j,
\end{array}\right.$$
and
$$\theta\left(I_{m}\right) \theta\left(I_{k}\right) \mu_{i j}^{l}=\left\{\begin{array}{cl}
\mu_{k j}^{l}, & m=k=i \neq j, l, \\
\mu_{i k}^{l}, & m=k=j \neq i, l, \\
4 \mu_{k k}^{l}, & m=k=i=j \neq l, \\
\mu_{i j}^{k}, & m=k=l \neq i, j, \\
\mu_{k k}^{k}, & m=k=l=i=j, \\
\hline \mu_{k m}^{l}, & k=i \neq m=j \neq l \neq k, \\
-\mu_{k j}^{m}, & k=i \neq m=l \neq j \neq k, \\
0, & k=i \neq m=j=l, \\
\hline \mu_{m k}^{l}, & k=j \neq m=i \neq l \neq k, \\
-\mu_{i k}^{m}, & k=j \neq m=l \neq i \neq k, \\
0, & k=j \neq m=i=l, \\
-2 \mu_{k k}^{m}, & k=i=j \neq m=l, \\
\hline-\mu_{m j}^{k}, & k=l \neq m=i \neq j \neq k, \\
-\mu_{i m}^{k}, & k=l \neq m=j \neq i \neq k, \\
-2 \mu_{m m}^{k}, & k=l \neq m=i=j,
\end{array} .\right.$$
This implies that if we set $[i j k]_{g}:=\left|\mu_{i j}^{k}\right|^{2}$, then
$$\begin{aligned}
\left\langle\theta\left(I_{k}\right) \theta\left(I_{k}\right) \mu_{\mathfrak{p}}, \mu_{\mathfrak{p}}\right\rangle & =\sum_{j, l \neq k}[k j l]_{g}+\sum_{i, l \neq k}[k i l]_{g}+4 \sum_{l \neq k}[k k l]_{g}+\sum_{i, j \neq k}[i j k]_{g}+[k k k]_{g}, \\
& =2 \sum_{i, j \neq k}[k i j]_{g}+4 \sum_{i \neq k}[k k i]_{g}+\sum_{i, j \neq k}[i j k]_{g}+[k k k]_{g},
\end{aligned}$$
and for $k \neq m$,
$$\begin{aligned}
\left\langle\theta\left(I_{m}\right) \theta\left(I_{k}\right) \mu_{\mathfrak{p}}, \mu_{\mathfrak{p}}\right\rangle= & \sum_{l \neq k, m}[k m l]_{g}-\sum_{j \neq k, m}[k j m]_{g}+\sum_{l \neq k, m}[k m l]_{g}-\sum_{i \neq k, m}[k i m]_{g} \\
& -2[k k m]_{g}-\sum_{j \neq k, m}[m j k]_{g}-\sum_{i \neq k, m}[m i k]_{g}-2[m m k]_{g} \\
= & 2 \sum_{i \neq k, m}[k m i]_{g}-2 \sum_{i \neq k, m}[k i m]_{g} \\
& -2[k k m]_{g}-2 \sum_{i \neq k, m}[m i k]_{g}-2[m m k]_{g} .
\end{aligned}$$
It now follows from (22) and (17) that in terms of $\left\{\frac{1}{\sqrt{d_{1}}} I_{1}, \ldots, \frac{1}{\sqrt{d_{r}}} I_{r}\right\}$,
$$\begin{aligned}
\left.\mathrm{L}_{\mathfrak{p}}\right]_{k k} & =\frac{1}{d_{k}}\left\langle\mathrm{~L}_{\mathfrak{p}} I_{k}, I_{k}\right\rangle=\frac{1}{2 d_{k}}\left\langle\theta\left(I_{k}\right) \theta\left(I_{k}\right) \mu_{\mathfrak{p}}, \mu_{\mathfrak{p}}\right\rangle+2 m_{k} \\
& =\frac{1}{2 d_{k}}\left(2 \sum_{i, j \neq k}[k i j]_{g}+4 \sum_{i \neq k}[k k i]_{g}+\sum_{i, j \neq k}[i j k]_{g}+[k k k]_{g}-2 \sum_{i, j}[k i j]_{g}+\sum_{i, j}[i j k]_{g}\right), \\
& =\frac{1}{2 d_{k}}\left(2 \sum_{i, j \neq k}[k i j]_{g}+4 \sum_{i \neq k}[k k i]_{g}+2 \sum_{i, j \neq k}[i j k]_{g}+2[k k k]_{g}-2 \sum_{i, j}[k i j]_{g}+2 \sum_{i \neq k}[i k k]_{g}\right), \\
& =\frac{1}{2 d_{k}}\left(-2 \sum_{i \neq k}[k k i]_{g}-2 \sum_{i \neq k}[k i k]_{g}+4 \sum_{i \neq k}[k k i]_{g}+2 \sum_{i, j \neq k}[i j k]_{g}+2 \sum_{i \neq k}[i k k]_{g}\right), \\
& =\frac{1}{d_{k}}\left(\sum_{i \neq k}[k k i]_{g}+\sum_{i, j \neq k}[i j k]_{g}\right),
\end{aligned}$$
and for $k \neq m$,
$$\begin{aligned}
{\left[\mathrm{L}_{\mathfrak{p}}\right]_{k m} } & =\frac{1}{\sqrt{d_{k}} \sqrt{d_{m}}}\left\langle\mathrm{~L}_{\mathfrak{p}} I_{m}, I_{k}\right\rangle=\frac{1}{2 \sqrt{d_{k}} \sqrt{d_{m}}}\left\langle\theta\left(I_{m}\right) \theta\left(I_{k}\right) \mu_{\mathfrak{p}}, \mu_{\mathfrak{p}}\right\rangle \\
& =\frac{1}{\sqrt{d_{k}} \sqrt{d_{m}}}\left(\sum_{i \neq k, m}[k m i]_{g}-\sum_{i \neq k, m}[k i m]_{g}-[k k m]_{g}-\sum_{i \neq k, m}[m i k]_{g}-[m m k]_{g}\right) .
\end{aligned}$$
Finally, we use that $[i j k]_{g}=\frac{x_{k}}{x_{i} x_{j}}[i j k]$ to derive the formulas as stated in the theorem, concluding the proof. \(\square\)

Remark 3.5. If $g$ is naturally reductive with respect to $G$ and $\mathfrak{p}$, then the numbers $[i j k]_{g}$ are invariant under any permutation of $i j k$ and so one obtains from the above proof that
$$\left[\mathrm{L}_{\mathfrak{p}}\right]_{k k}=\frac{1}{d_{k}} \sum_{j \neq k ; i}[i j k]_{g}, \quad \forall k, \quad\left[\mathrm{~L}_{\mathfrak{p}}\right]_{k m}=-\frac{1}{\sqrt{d_{k}} \sqrt{d_{m}}} \sum_{i}[i k m]_{g}, \quad \forall k \neq m .$$
This provides an alternative proof of [L, Theorem 5.3].
Example 3.6. Consider the full flag manifold $\operatorname{SU}(n) / T$, where $T$ is the diagonal maximal torus. The standard reductive decomposition is given by
$$\mathfrak{s} \mathfrak{u}(n)=\mathfrak{t} \oplus \mathfrak{p}_{12} \oplus \mathfrak{p}_{13} \oplus \cdots \oplus \mathfrak{p}_{(n-1) n},$$
where each $\mathfrak{p}_{i j}:=\left\{z E_{i j}-\bar{z} E_{j i}: z \in \mathbb{C}\right\}$ is 2-dimensional and they are all $\operatorname{Ad}(T)$-irreducible and pairwise inequivalent. Note that $\operatorname{dim} \mathcal{M}^{G}=\frac{n(n-1)}{2}$. Thus $\left[\mathfrak{p}_{i j}, \mathfrak{p}_{k l}\right]_{\mathfrak{p}}=0$ if $\{i, j\}$ and $\{k, l\}$ are either equal or disjoint, and $\left[\mathfrak{p}_{i j}, \mathfrak{p}_{i k}\right]_{\mathfrak{p}}$ is nonzero and it is contained in $\mathfrak{p}_{j k}$
for all $j \neq k$. Moreover, since all the nonzero structural constants are equal to $\frac{1}{n}$, it follows from (18) that the standard or Killing metric $g_{\mathrm{B}}=(1, \ldots, 1)$ (set $Q=-\mathrm{B}_{\mathfrak{s u}(n)}$ ) is Einstein with $2 \rho=1-\frac{1}{2 n(n-2)}$. According to Theorem 3.1, for $H=T$, one obtains that $\left[\mathrm{L}_{\mathfrak{p}}\right]=\frac{1}{2 n}(2(n-2) I-\operatorname{Adj}(X))$, where $X=J(n, 2,1)$ is the Johnson graph with parameters $(n, 2,1)$ (see [GR, §1.6]) and $\operatorname{Adj}(X)$ denotes its adjacency matrix. The spectrum of $\operatorname{Adj}(X)$ is therefore given by $\{2(n-2), n-4,-2\}$ with multiplicities $1, n-1, \frac{n(n-3)}{2}$, respectively (see [GR, §10.1, §10.2]). This implies that
$$\operatorname{Spec}\left(\mathrm{L}_{\mathfrak{p}}\right)=\left\{0, \lambda_{\mathfrak{p}}, \lambda_{\mathfrak{p}}^{\max }\right\}, \quad \lambda_{\mathfrak{p}}=\frac{1}{2}, \quad \lambda_{\mathfrak{p}}^{\max }=\frac{n-1}{n}, \quad \forall n \geq 4,$$
with multiplicities $1, n-1$ and $\frac{n(n-3)}{2}$, respectively. For $n=3, X$ is the complete graph on 3 vertices and so the spectrum of $\operatorname{Adj}(X)$ equals $\{2,-1\}$, with respective multiplicities 1 and 2. Thus $\lambda_{\mathfrak{p}}=\lambda_{\mathfrak{p}}^{\text {max }}=\frac{1}{2}$ and has multiplicity 2. A straightforward comparison between the values of $2 \rho, \lambda_{\mathfrak{p}}$ and $\lambda_{\mathfrak{p}}^{\text {max }}$ gives the following picture:
\begin{itemize}
\item[-] The standard metric $g_{\mathrm{B}}$ on each $\operatorname{SU}(n) / T$ is always $G$-unstable with coindex $n-1$.
\item[-] $g_{\mathrm{B}}$ is a local minimum for $n=3$, it is $G$-degenerate for $n=4$ and it is a saddle point for any $n \geq 5$.
\item[-] $g_{\mathrm{B}}$ is always $G$-non-degenerate, and in particular $G$-rigid, except on $\operatorname{SU}(4) / T$. We do not know whether $g_{\mathrm{B}}$ is a local minimum for $\operatorname{SU}(4) / T$ or not.
\end{itemize}
This example is a particular case of [L, §6], where the $G$-stability of the standard metric is studied using the spectrum of $\operatorname{Adj}(X)$ on $\operatorname{SU}(n k) / \operatorname{S}\left(U(k)^{n}\right), \operatorname{Sp}(n k) / \operatorname{Sp}(k)^{n}$ and $\operatorname{SO}(n k) / \operatorname{S}\left(\mathrm{O}(k)^{n}\right)$.
Example 3.7. The isotropy representation of the Stiefel manifold $\operatorname{SO}(k+2) / \operatorname{SO}(k), k \geq 3$, decomposes as $\mathfrak{p}=\mathfrak{p}_{1} \oplus \mathfrak{p}_{2} \oplus \mathfrak{p}_{3}$, where $d_{1}=d_{2}=k, d_{3}=1$ and $\mathfrak{p}_{1}, \mathfrak{p}_{2}$ are equivalent $\operatorname{Ad}(K)$ -representations of real type. This implies that $\operatorname{dim} \mathcal{M}^{G}=4$. It is proved in [K, §4] that this space admits a unique Einstein metric given by $g=\left(1,1, \frac{2 k}{k+1}\right)$, with $2 \rho=\frac{k}{k+1}$, and that for the intermediate subgroup $H:=\mathrm{SO}(k) \times \mathrm{SO}(2)$ of the normalizer of $\mathrm{SO}(k)$ one has that $\mathcal{M}^{G}=\operatorname{Ad}(H) \cdot \mathcal{M}^{G, H}$. Thus we only need to compute the spectrum of $\mathrm{L}_{\mathfrak{p}}(g)$ restricted to $\operatorname{sym}(\mathfrak{p})^{H}$ (see Remark 2.2), which is precisely the 3-dimensional space of diagonal $\operatorname{Ad}(H)$ -invariant tensors since $\mathfrak{p}_{1}, \mathfrak{p}_{2}$ are now inequivalent $\operatorname{Ad}(H)$-representations. It follows from Theorem 3.1 that
$$\left.L_{\mathfrak{p}}\right|_{\operatorname{sym}(\mathfrak{p})^{H}}=\left[\begin{array}{ccc}
\frac{k+1}{2 k^{2}} & \frac{k^{2}-2 k-1}{2 k^{2}(k+1)} & -\frac{\sqrt{k}}{k+1} \\
\frac{k^{2}-2 k-1}{2 k^{2}(k+1)} & \frac{k+1}{2 k^{2}} & -\frac{\sqrt{k}}{k+1} \\
-\frac{\sqrt{k}}{k+1} & -\frac{\sqrt{k}}{k+1} & \frac{2 k}{k+1}
\end{array}\right],$$
and it is therefore straightforward to check that $\lambda_{\mathfrak{p}}=\frac{2 k+1}{k^{2}(k+1)}$ and $\lambda_{\mathfrak{p}}^{\text {max }}=\frac{2 k+1}{k+1}$. Since $\lambda_{\mathfrak{p}}<2 \rho<\lambda_{\mathfrak{p}}^{\text {max }}$, we obtain that $g$ is always a $G$-non-degenerate and $G$-unstable saddle point.
Example 3.8. In the case $S^{2} \times S^{3}=\operatorname{SO}(4) / \operatorname{SO}(2)$, one also has as above that $\mathfrak{p}=\mathfrak{p}_{1} \oplus \mathfrak{p}_{2} \oplus \mathfrak{p}_{3}$, $d_{1}=d_{2}=2, d_{3}=1$ and $\mathfrak{p}_{1}, \mathfrak{p}_{2}$ equivalent, but here $\operatorname{dim} \mathcal{M}^{G}=5$ since $\mathfrak{p}_{1}$ and $\mathfrak{p}_{2}$ are of complex type. Besides the Einstein metric $g=\left(1,1, \frac{4}{3}\right)$, there is another Einstein metric $g_{\times} \in \mathcal{M}^{G}$, which was discovered in [AFD] and is isometric to the product metric. The metric $g_{\times}$actually belongs to a one-parameter family of Einstein metrics in $\mathcal{M}^{G}$ given by the orbit $\operatorname{Aut}(G / K) \cdot g_{\times}$(note that $\operatorname{Aut}(G / K)=\mathrm{O}(2)$ ). The argument used in Example 3.7 to compute the spectrum of $\mathrm{L}_{\mathfrak{p}}(g)$ is still valid, giving that $\lambda_{\mathfrak{p}}(g)=\frac{5}{12}$ and $\lambda_{\mathfrak{p}}^{\text {max }}(g)=\frac{5}{3}$. On the other hand, we have that $\operatorname{dim} T_{g_{\times}} \operatorname{Aut}(G / K) \cdot g_{\times}=1$ (see (4)) and it is easy to see by using that $g_{\times}$is the product metric that $g_{\times}$is a $G$-non-degenerate and $G$-unstable saddle point of coindex 1.

Beyond left-invariant metrics on Lie groups, the above is the only example we know of a continuous family of Einstein metrics in $\mathcal{M}_{1}^{G}$, i.e., with $\operatorname{dim} T_{g} \operatorname{Aut}(G / K) \cdot g>0$.
3.1. Case $r=2$. For homogeneous spaces with only two isotropy summands the above formulas considerably simplify. We refer to [DK, He] for a complete classification of these spaces (43 infinite families and 78 isolated examples) together with their Einstein metrics (only 19 isolated examples do not admit any). Note that $\operatorname{dim} \mathcal{M}_{1}^{G}=1$ in this case (with the only exception of $\mathrm{SO}(8) / G_{2}$ ), so $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ is a one-variable function.

It follows from (18) that the Ricci eigenvalues are
$$\begin{aligned}
& \rho_{1}=\left(\frac{b_{1}}{2}-\frac{[111]}{4 d_{1}}-\frac{[122]}{2 d_{1}}\right) \frac{1}{x_{1}}-\frac{[112]}{2 d_{1}} \frac{x_{2}}{x_{1}^{2}}+\frac{[122]}{4 d_{1}} \frac{x_{1}}{x_{2}^{2}}, \\
& \rho_{2}=\left(\frac{b_{2}}{2}-\frac{[222]}{4 d_{2}}-\frac{[112]}{2 d_{2}}\right) \frac{1}{x_{2}}-\frac{[122]}{2 d_{2}} \frac{x_{1}}{x_{2}^{2}}+\frac{[112]}{4 d_{2}} \frac{x_{2}}{x_{1}^{2}},
\end{aligned}$$
and from Theorem 3.1 that
$$\left[\mathrm{L}_{\mathfrak{p}}\right]_{11}=\frac{[122] x_{1}}{d_{1} x_{2}^{2}}+\frac{[112] x_{2}}{d_{1} x_{1}^{2}}, \quad\left[\mathrm{~L}_{\mathfrak{p}}\right]_{22}=\frac{[112] x_{2}}{d_{2} x_{1}^{2}}+\frac{[122] x_{1}}{d_{2} x_{2}^{2}} .$$
Since $\operatorname{Spec}\left(\mathrm{L}_{\mathfrak{p}}\right)=\left\{0, \lambda_{\mathfrak{p}}\right\}$, we obtain that
$$\lambda_{\mathfrak{p}}=\left[\mathrm{L}_{\mathfrak{p}}\right]_{11}+\left[\mathrm{L}_{\mathfrak{p}}\right]_{22}=\frac{d_{1}+d_{2}}{d_{1} d_{2}}\left(\frac{[112] x_{2}}{x_{1}^{2}}+\frac{[122] x_{1}}{x_{2}^{2}}\right) .$$
This can be used to find the $G$-stability and critical point types of any Einstein metric $\left(x_{1}, x_{2}\right)$ on a homogeneous space $M=G / K$ of this kind, after computing or finding in the literature the structural constants of $G / K$ (see LaL] for the case of standard Einstein metrics).

Example 3.9. If $M=G / K$ is a flag manifold (i.e., $G$ simple and $K$ the centralizer of a torus in $G$, see §5) with two isotropy summands (see e.g. [AC2, Table 1] for a complete list, consisting of 3 classical families and 10 exceptional examples), then it can be assumed that the only non-zero structural constant is $[112]=\frac{d_{1} d_{2}}{d_{1}+4 d_{2}}$ (set $Q:=-\mathrm{B}_{\mathfrak{g}}$ ) and so,
$$\rho_{1}=\frac{1}{2 x_{1}}-\frac{[112] x_{2}}{2 d_{1} x_{1}^{2}}, \quad \rho_{2}=\frac{1}{2 x_{2}}-\frac{[112]\left(2 x_{1}^{2}-x_{2}^{2}\right)}{4 d_{2} x_{1}^{2} x_{2}}, \quad \lambda_{\mathfrak{p}}=\frac{\left(d_{1}+d_{2}\right) x_{2}}{\left(d_{1}+4 d_{2}\right) x_{1}^{2}} .$$
It is easy to see that there are exactly two solutions to $\rho_{1}=\rho_{2}$ up to scaling, the Kähler-Einstein metric $g_{0}=(1,2)$ and a non-Kähler Einstein metric given by $g_{1}=\left(1, \frac{4 d_{2}}{d_{1}+2 d_{2}}\right)$. On the other hand, a straightforward inspection gives that $g_{0}$ is always $G$-stable (i.e., $2 \rho<\lambda_{\mathfrak{p}}$ ) and $g_{1}$ is always $G$-unstable (i.e., $\lambda_{\mathfrak{p}}<2 \rho$ ). In particular, $g_{0}$ is a local maximum of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ and $g_{1}$ a local minimum for any of these spaces (cf. [AC1, Theorem 1]).

\section*{4. Generalized Wallach spaces}

A connected homogeneous space $M=G / K$ with $G$ compact semisimple is called a generalized Wallach space if the $\mathrm{B}_{\mathfrak{g}}$-orthogonal reductive decomposition $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$ satisfies that $\mathfrak{p}=\mathfrak{p}_{1} \oplus \mathfrak{p}_{2} \oplus \mathfrak{p}_{3}$ for some $\operatorname{Ad}(K)$-irreducible subspaces $\mathfrak{p}_{i}$ 's such that $\left[\mathfrak{p}_{i}, \mathfrak{p}_{i}\right] \subset \mathfrak{k}$ for all $i=1,2,3$. Equivalently, the only nonzero structural constant is [123]. The generalized Wallach spaces with $G$ simple are listed in Table 1, together with the numbers [123] and $a_{i}:=[123] / d_{i}$, where $d_{i}:=\operatorname{dim} \mathfrak{p}_{i}$ (see [N, CKL]). For a table with the dimensions $d_{i}$ 's see [CN, Table 1].

In what follows, as an application of the formula given in Theorem 3.1, we compute the spectrum of the Lichnerowicz Laplacian $\mathrm{L}_{\mathfrak{p}}$ for each $G$-invariant Einstein metric on most of these spaces (see Tables 2, 6 and 8). In this way, we obtain the $G$-stability type of all these Einstein metrics, as well as what type of critical points of $\left.\mathrm{Sc}\right|_{\mathcal{M}_{1}^{G}}$ are. It was proved in [AANS, Theorem 7] that, generically, there are three possible behaviors depending on the region the triple $\left(a_{1}, a_{2}, a_{3}\right)$ attached to $G / K$ belongs. The regions are described in

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $W_{i}$ & $\mathfrak{g} / \mathfrak{k}$ & $a_{1}=\frac{[123]}{d_{1}}$ & $a_{2}=\frac{[123]}{d_{2}}$ & $a_{3}=\frac{[123]}{d_{3}}$ & [123] \\
\hline $W_{1}$ & $\frac{\mathfrak{s} \mathfrak{o}(k+l+m)}{\mathfrak{s} \mathfrak{o}(k) \oplus \mathfrak{s} \mathfrak{o}(l) \oplus \mathfrak{s} \mathfrak{o}(m)}$ & $\frac{k}{2(k+l+m-2)}$ & $\frac{l}{2(k+l+m-2)}$ & $\frac{m}{2(k+l+m-2)}$ & $\frac{k l m}{2(k+l+m-2)}$ \\
\hline $W_{2}$ & $\frac{\mathfrak{s} \mathfrak{u}(k+l+m)}{\mathfrak{s}(\mathfrak{u}(k) \oplus \mathfrak{u}(l) \oplus \mathfrak{u}(m))}$ & $\frac{k}{2(k+l+m)}$ & $\frac{l}{2(k+l+m)}$ & $\frac{m}{2(k+l+m)}$ & $\frac{k l m}{k+l+m}$ \\
\hline $W_{3}$ & $\frac{\mathfrak{s p}(k+l+m)}{\boldsymbol{\mathfrak { s p }}(k) \oplus \mathfrak{s p}(l) \oplus \mathfrak{s p}(m)}$ & $\frac{k}{2(k+l+m+1)}$ & $\frac{l}{2(k+l+m+1)}$ & $\frac{m}{2(k+l+m+1)}$ & $\frac{2 k l m}{k+l+m+1}$ \\
\hline $W_{4}$ & $\frac{\mathfrak{s u}(2 l)}{\mathfrak{u}(l)}, l \geq 2$ & $\frac{l^{2}-1}{4}$ & $\frac{l-1}{4 l}$ & $\frac{1}{4}$ & $\frac{l+1}{4 l}$ \\
\hline $W_{5}$ & $\frac{\mathfrak{s} \mathfrak{o}(2 l)}{\mathfrak{u}(1) \oplus \mathfrak{u}(l-1)}, l \geq 4$ & $\frac{l-2}{4(l-1)}$ & $\frac{l-2}{4(l-1)}$ & $\frac{1}{2(l-1)}$ & $\frac{l-2}{2}$ \\
\hline $W_{6}$ & $\frac{\mathfrak{e}_{6}}{\mathfrak{s} \mathfrak{u}(4) \oplus 2 \mathfrak{s} \mathfrak{p}(1) \oplus \mathbb{R}}$ & $\frac{1}{4}$ & $\frac{1}{4}$ & $\frac{1}{6}$ & 4 \\
\hline $W_{7}$ & $\frac{\mathfrak{e}_{6}}{\mathfrak{s} \mathfrak{o}(8) \oplus \mathbb{R}^{2}}$ & $\frac{1}{6}$ & $\frac{1}{6}$ & $\frac{1}{6}$ & $\frac{8}{3}$ \\
\hline $W_{8}$ & $\frac{\mathfrak{e}_{6}}{\mathfrak{s p}(3) \oplus \mathfrak{s p}(1)}$ & $\frac{1}{4}$ & $\frac{1}{8}$ & $\frac{7}{24}$ & $\frac{7}{2}$ \\
\hline $W_{9}$ & $\frac{\mathfrak{e}_{7}}{\mathfrak{s} \mathfrak{o}(8) \oplus 3 \mathfrak{s} \mathfrak{p}(1)}$ & $\frac{2}{9}$ & $\frac{2}{9}$ & $\frac{2}{9}$ & $\frac{64}{9}$ \\
\hline $W_{10}$ & $\frac{\mathfrak{e}_{7}}{\mathfrak{s} \mathfrak{u}(6) \oplus \mathfrak{s p}(1) \oplus \mathbb{R}}$ & $\frac{2}{9}$ & $\frac{1}{6}$ & $\frac{5}{18}$ & $\frac{20}{3}$ \\
\hline $W_{11}$ & $\frac{\mathfrak{e}_{7}}{\mathfrak{s} \mathfrak{o}(8)}$ & $\frac{5}{18}$ & $\frac{5}{18}$ & $\frac{5}{18}$ & $\frac{175}{18}$ \\
\hline $W_{12}$ & $\frac{\mathfrak{e}_{8}}{\mathfrak{s} \mathfrak{o}(12) \oplus 2 \mathfrak{s} \mathfrak{p}(1)}$ & $\frac{1}{5}$ & $\frac{1}{5}$ & $\frac{4}{15}$ & $\frac{64}{5}$ \\
\hline $W_{13}$ & $\frac{\mathfrak{e}_{8}}{\mathfrak{s} \mathfrak{o}(8) \oplus \mathfrak{s} \mathfrak{o}(8)}$ & $\frac{4}{15}$ & $\frac{4}{15}$ & $\frac{4}{15}$ & $\frac{256}{15}$ \\
\hline $W_{14}$ & $\frac{\mathfrak{f}_{4}}{\mathfrak{s} \mathfrak{o}(5) \oplus 2 \mathfrak{s} \mathfrak{p}(1)}$ & $\frac{5}{18}$ & $\frac{5}{18}$ & $\frac{1}{9}$ & $\frac{20}{9}$ \\
\hline $W_{15}$ & $\frac{\mathfrak{f}_{4}}{\boldsymbol{\mathfrak { s }} \boldsymbol{\mathfrak { o }}(8)}$ & $\frac{1}{9}$ & $\frac{1}{9}$ & $\frac{1}{9}$ & $\frac{8}{9}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1. Generalized Wallach spaces with $G$ simple (see [N, CKL]). In case $W_{1}$, the triple $(k, 2,2)$ (and its permutations) must be avoided, and $(k, 1,1)$ (i.e., the Stiefel manifold $\operatorname{SO}(k+2) / \operatorname{SO}(k)$ ) are the only instances in which $G / K$ is not multiplicity-free. The spaces $W_{2}, W_{5}$ and $W_{7}$ are also flag manifolds (see §5).}
\end{table}
[CN, Table 2] (the case 5 is incorrectly assigned to region $O_{3}$, it is actually in $O_{1}$ ). It is easy to check that the spaces $W_{1}$ with $l=m$ are in $O_{1}$. There is no contradiction between our results and the behaviors described in these papers.

Note that $\operatorname{dim} \mathcal{M}_{1}^{G}=2$ for any generalized Wallach space (except $\operatorname{SO}(k+2) / \operatorname{SO}(k)$, see Example 3.7) and so
$$\operatorname{Spec}\left(L_{\mathfrak{p}}(g)\right)=\left\{0, \lambda_{\mathfrak{p}}, \lambda_{\mathfrak{p}}^{\max }\right\}$$
for any Einstein metric $g=\left(x_{1}, x_{2}, x_{3}\right) \in \mathcal{M}^{G}$. We will always set $Q=-\mathrm{B}_{\mathfrak{g}}$ as a background metric. Using that [123] is the only nonzero structural constant, it easily follows from Theorem 3.1 that
$$\mathrm{L}_{\mathfrak{p}}(g)=\left[\begin{array}{ccc}
a_{1} \frac{2 x_{1}}{x_{2} x_{3}} & \sqrt{a_{1} a_{2}} \frac{x_{3}^{2}-x_{1}^{2}-x_{2}^{2}}{x_{1} x_{2} x_{3}} & \sqrt{a_{1} a_{3}} \frac{x_{2}^{2}-x_{1}^{2}-x_{3}^{2}}{x_{1} x_{2} x_{3}} \\
\sqrt{a_{1} a_{2}} \frac{x_{3}^{2}-x_{1}^{2}-x_{2}^{2}}{x_{1} x_{2} x_{3}} & a_{2} \frac{2 x_{2}}{x_{1} x_{3}} & \sqrt{a_{2} a_{3}} \frac{x_{1}^{2}-x_{2}^{2}-x_{3}^{2}}{x_{1} x_{2} x_{3}} \\
\sqrt{a_{1} a_{3}} \frac{x_{2}^{2}-x_{1}^{2}-x_{3}^{2}}{x_{1} x_{2} x_{3}} & \sqrt{a_{2} a_{3}} \frac{x_{1}^{2}-x_{2}^{2}-x_{3}^{2}}{x_{1} x_{2} x_{3}} & a_{3} \frac{2 x_{3}}{x_{1} x_{2}}
\end{array}\right] .$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|l|}
\hline $W_{i}$ & $\mathfrak{g} / \mathfrak{k}$ & $b$ & $\frac{1-2 b}{2 b}$ & $g$ & $\lambda_{\mathfrak{p}}$ & $\lambda_{\mathfrak{p}}^{\text {max }}$ & $2 \rho$ & Type \\
\hline $W_{1}$ & $\mathfrak{s} \mathfrak{o}(3)$ & $\frac{1}{2}$ & & $g_{\mathrm{B}}$ & $\frac{3}{2}$ & $\frac{3}{2}$ & $\frac{1}{2}$ & G-stab. \\
\hline $W_{1}$ & $$\begin{gathered}
\frac{\mathfrak{s} \mathfrak{o}(3 k)}{\mathfrak{s} \mathfrak{o}(k) \oplus \mathfrak{s} \mathfrak{o}(k) \oplus \mathfrak{s} \mathfrak{o}(k)} \\
k \geq 3
\end{gathered}$$ & $\frac{k}{2(3 k-2)}$ & $\frac{2(k-1)}{k}$ &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} & $$\begin{gathered}
\frac{3 k}{2(3 k-2)} \\
\frac{2 k-1}{(k-1)(3 k-2)}
\end{gathered}$$ & $$\begin{gathered}
\frac{3 k}{2(3 k-2)} \\
\frac{3(k-1)}{3 k-2}
\end{gathered}$$ & $$\begin{gathered}
\frac{5 k-4}{2(3 k-2)} \\
\frac{2 k-1}{3 k-2}
\end{gathered}$$ &
\begin{tabular}[t]{l}
$G$-unst. \\
$G$-unst.
\end{tabular} \\
\hline $W_{2}$ & $\frac{\mathfrak{s} \mathfrak{u}(3 k)}{\mathfrak{s}(\mathfrak{u}(k) \oplus \mathfrak{u}(k) \oplus \mathfrak{u}(k))}$ & $\frac{1}{6}$ & 2 &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{1}{2}$ \\
0
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{1}{2}$ \\
1
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{5}{6}$ \\
$\frac{2}{3}$
\end{tabular} &
\begin{tabular}[t]{l}
$G$-unst. \\
$G$-unst.
\end{tabular} \\
\hline $W_{3}$ & $\frac{\mathfrak{s} \mathfrak{p}(3 k)}{\mathfrak{s} \mathfrak{p}(k) \oplus \mathfrak{s} \mathfrak{p}(k) \oplus \mathfrak{s} \mathfrak{p}(k)}$ & $\frac{k}{2(3 k+1)}$ & $\frac{2 k+1}{k}$ &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$, \\
$g_{i}$
\end{tabular} & $$\begin{gathered}
\frac{3 k}{2(3 k+1)} \\
\frac{-(4 k+1)}{2(2 k+1)(3 k+1)}
\end{gathered}$$ & $$\begin{aligned}
& \frac{3 k}{2(3 k+1)} \\
& \frac{3(2 k+1)}{2(3 k+1)}
\end{aligned}$$ & $$\begin{aligned}
& \frac{5 k+2}{2(3 k+1)} \\
& \frac{4 k+1}{2(3 k+1)}
\end{aligned}$$ &
\begin{tabular}[t]{l}
$G$-unst. \\
$G$-unst.
\end{tabular} \\
\hline $W_{5}$ & $\frac{\mathfrak{s} \mathfrak{o}(8)}{\mathfrak{u}(1) \oplus \mathfrak{u}(3)}$ & $\frac{1}{6}$ & 2 &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{1}{2}$ \\
0
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{1}{2}$ \\
1
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{5}{6}$ \\
$\frac{2}{3}$
\end{tabular} &
\begin{tabular}[t]{l}
$G$-unst. \\
$G$-unst.
\end{tabular} \\
\hline $W_{7}$ & $\frac{\mathfrak{e}_{6}}{\mathfrak{s} \mathfrak{o}(8) \oplus \mathbb{R}^{2}}$ & $\frac{1}{6}$ & 2 &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{1}{2}$ \\
0
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{1}{2}$ \\
1
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{5}{6}$ \\
$\frac{2}{3}$
\end{tabular} &
\begin{tabular}[t]{l}
$G$-unst. \\
$G$-unst.
\end{tabular} \\
\hline $W_{9}$ & $\frac{\mathfrak{e}_{7}}{\mathfrak{s} \mathfrak{o}(8) \oplus 3 \mathfrak{s} \mathfrak{p}(1)}$ & $\frac{2}{9}$ & $\frac{5}{4}$ &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{2}{3}$ \\
$\frac{13}{30}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{2}{3}$ \\
$\frac{5}{6}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{7}{9}$ \\
$\frac{13}{18}$
\end{tabular} &
\begin{tabular}[t]{l}
$G$-unst. \\
$G$-unst.
\end{tabular} \\
\hline $W_{11}$ & $\frac{\mathfrak{e}_{7}}{\mathfrak{s} \mathfrak{o}(8)}$ & $\frac{5}{18}$ & $\frac{4}{5}$ &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{15}{18}$ \\
$\frac{2}{3}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{15}{18}$ \\
$\frac{7}{6}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{13}{18}$ \\
$\frac{7}{9}$
\end{tabular} &
\begin{tabular}[t]{l}
G-stab. \\
$G$-unst.
\end{tabular} \\
\hline $W_{13}$ & $\frac{\mathfrak{e}_{8}}{\mathfrak{s} \mathfrak{o}(8) \oplus \mathfrak{s} \mathfrak{o}(8)}$ & $\frac{4}{15}$ & $\frac{7}{8}$ &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{12}{15}$ \\
$\frac{7}{10}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{12}{15}$ \\
$\frac{69}{70}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{11}{15}$ \\
$\frac{23}{30}$
\end{tabular} &
\begin{tabular}[t]{l}
G-stab. \\
$G$-unst.
\end{tabular} \\
\hline $W_{15}$ & $\frac{\mathfrak{f}_{4}}{\mathfrak{s} \mathfrak{o}(8)}$ & $\frac{1}{9}$ & $\frac{7}{2}$ &
\begin{tabular}[t]{l}
$g_{\mathrm{B}}$ \\
$g_{i}$
\end{tabular} & $$\begin{gathered}
\frac{1}{3} \\
-\frac{11}{42}
\end{gathered}$$ &
\begin{tabular}[t]{l}
$\frac{1}{3}$ \\
$\frac{7}{6}$
\end{tabular} &
\begin{tabular}[t]{l}
$\frac{8}{9}$ \\
$\frac{11}{18}$
\end{tabular} &
\begin{tabular}[t]{l}
$G$-unst. \\
$G$-unst.
\end{tabular} \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 2. Einstein metrics $g_{\mathrm{B}}, g_{1}, g_{2}, g_{3}$ on generalized Wallach spaces with $a_{1}=a_{2}=a_{3}=b$ (see [LNF]). The metrics $g_{i}$ 's all satisfy that $\lambda_{\mathfrak{p}}<2 \rho<$ $\lambda_{\mathfrak{p}}^{\text {max }}$ and so they are $G$-unstable and $G$-non-degenerate saddle points with coindex 1. All the standard metrics $g_{\mathrm{B}}$ 's which are $G$-unstable are local minima of coindex 2 since $\lambda_{\mathfrak{p}}=\lambda_{\mathfrak{p}}^{\text {max }}<2 \rho$. Note that $g_{1}, g_{2}, g_{3}$ are all Kähler metrics in the flag cases $W_{2}, W_{5}$ and $W_{7}$, which are precisely the cases when $\lambda_{\mathfrak{p}}=0$.}
\end{table}
4.1. Case $d_{1}=d_{2}=d_{3}$. It is proved in [LNF, Theorem 3] that $G / K(\neq \operatorname{SO}(3))$ admits in this case four $G$-invariant Einstein metrics up to scaling, the standard metric $g_{\mathrm{B}}=(1,1,1)$ and
$$g_{1}=\left(\frac{1-2 b}{2 b}, 1,1\right), \quad g_{2}=\left(1, \frac{1-2 b}{2 b}, 1\right), \quad g_{3}=\left(1,1, \frac{1-2 b}{2 b}\right),$$

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $W_{i}$ & $g$ & $\left(\operatorname{det}_{g_{\mathrm{B}}} g\right)^{\frac{1}{n}} \operatorname{Sc}(g)$ & $W_{i}$ & $g$ & $\left(\operatorname{det}_{g_{\mathrm{B}}} g\right)^{\frac{1}{n}} \operatorname{Sc}(g)$ \\
\hline $W_{1}$ & $g_{\mathrm{B}}$ & $\frac{3}{4}(k=3)$ & $W_{7}$ & $g_{\mathrm{B}}$ $g_{i}$ & 20
$$16 \cdot 2^{\frac{1}{3}} \approx 20.1587$$ \\
\hline \multirow{2}{*}{$W_{1}$} & $g_{\mathrm{B}}$ & $\frac{3 k^{2}(5 k-4)}{4(3 k-2)}$ & \multirow{2}{*}{$W_{9}$} & $g_{\mathrm{B}}$ & $\frac{112}{3} \approx 37.3333$ \\
\hline & $g_{i}$ & $\frac{3 k^{2}(2 k-1)}{3 k-2}\left(\frac{2 k-2}{k}\right)^{\frac{1}{3}}$ & & $g_{i}$ & $\frac{52}{3} 10^{\frac{1}{3}} \approx 37.3435$ \\
\hline \multirow{2}{*}{$W_{2}$} & $g_{\mathrm{B}}$ & $\frac{5 k^{2}}{2}$ & \multirow{2}{*}{$W_{11}$} & $g_{\mathrm{B}}$ & $\frac{455}{12} \approx 37.9166$ \\
\hline & $g_{i}$ & $2^{\frac{4}{3}} k^{2} \approx 2.52 k^{2}$ & & $g_{i}$ & $\frac{49}{6} 10^{\frac{2}{3}} \approx 37.9063$ \\
\hline \multirow{2}{*}{$W_{3}$} & $g_{\mathrm{B}}$ & $\frac{n(5 k+2)}{4(3 k+1)}$ & \multirow{2}{*}{$W_{13}$} & $g_{\mathrm{B}}$ & $\frac{352}{5}=70.4$ \\
\hline & $g_{i}$ & $\frac{3 k^{2}(4 k+1)}{3 k+1}\left(\frac{2 * k+1}{k}\right)^{\frac{1}{3}}$ & & $g_{i}$ & $\frac{184}{5} 7^{\frac{2}{3}} \approx 70.3958$ \\
\hline \multirow{2}{*}{$W_{5}$} & $g_{\mathrm{B}}$ & $\frac{15}{2}=7.5$ & \multirow{2}{*}{$W_{15}$} & $g_{\mathrm{B}}$ & $\frac{32}{3} \approx 10.6666$ \\
\hline & $g_{i}$ & $6 \cdot 2^{\frac{1}{3}} \approx 7.5595$ & & $g_{i}$ & $\frac{11}{3} 28^{\frac{1}{3}} \approx 11.1341$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 3. Volume normalized scalar curvature of Einstein metrics in Table 2. Note that $\mathrm{Sc}_{N}\left(g_{\mathrm{B}}\right)<\mathrm{Sc}_{N}\left(g_{i}\right)$ always holds, except for $W_{11}$ and $W_{13}$, that is, precisely when the standard metric $g_{\mathrm{B}}$ is a local maximum.}
\end{table}
where $b:=a_{1}=a_{2}=a_{3}=[123] / d_{i}$. Note that $b \leq \frac{1}{2}$ and equality holds if and only if $\mathfrak{g} / \mathfrak{k}=\mathfrak{s o}(3)$. It follows from (18) that for $g_{\mathrm{B}}, 2 \rho=1-b$ and by (23),
$$\mathrm{L}_{\mathfrak{p}}\left(g_{\mathrm{B}}\right)=\left[\begin{array}{ccc}
2 b & -b & -b \\
-b & 2 b & -b \\
-b & -b & 2 b
\end{array}\right], \quad \text { so } \quad \lambda_{\mathfrak{p}}=\lambda_{\mathfrak{p}}^{\max }=3 b .$$
On the other hand, for each $g_{i}$ we have that $2 \rho=\frac{1+2 b}{2}$,
$$L_{\mathfrak{p}}\left(g_{1}\right)=\left[\begin{array}{ccc}
(1-2 b) & -\frac{1}{2}(1-2 b) & -\frac{1}{2}(1-2 b) \\
-\frac{1}{2}(1-2 b) & \frac{4 b^{2}}{1-2 b} & -\frac{4 b^{2}+4 b-1}{2(1-2 b)} \\
-\frac{1}{2}(1-2 b) & -\frac{4 b^{2}+4 b-1}{2(1-2 b)} & \frac{4 b^{2}}{1-2 b}
\end{array}\right],$$
and thus it is straightforward to check that
$$\operatorname{Spec}\left(\mathrm{L}_{\mathfrak{p}}\left(g_{i}\right)\right)=\left\{0, \frac{12 b^{2}+4 b-1}{2(1-2 b)}, \frac{3(1-2 b)}{2}\right\}, \quad \forall i=1,2,3 .$$
All this data together with the resulting types have been collected in Table 2. We furthermore give in Table 3 the value of the volume normalized scalar curvature $\mathrm{Sc}_{N}$ (see (20)) for these metrics.