---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Mass and rigidity in almost Kähler geometry]

---
source_file: 2603_08627v2.pdf
converter: mathpix
format: mmd
---

\title{
Mass and rigidity in almost Kähler geometry
}

\author{
Partha Ghosh
}

\begin{abstract}
We derive an explicit formula for the ADM mass of asymptotically locally Euclidean (ALE) almost Kähler manifolds. The formula expresses the mass in terms of the total Hermitian scalar curvature and topological data associated with the underlying almost complex structure, extending a result of Hein and LeBrun [14] in the Kähler ALE case. Our approach is based on a spin ${ }^{\mathbb{C}}$ adaptation of Witten's proof of the positive mass conjecture in the spin case and is therefore distinct from previous complex-geometric methods. In dimension 4, we prove a positive mass theorem and a Penrose-type inequality for asymptotically Euclidean (AE) almost Kähler manifolds. We also study rigidity phenomena of almost Kähler ALE manifolds. We prove that an almost Kähler-Einstein ALE manifold with nonnegative scalar curvature and certain decay assumptions is necessarily Kähler-Einstein. In particular, any four dimensional Ricci-flat almost Kähler manifold with maximal volume growth and curvature in $L^{2}$ is Kähler, yielding new evidence towards the Bando-Kasue-Nakajima conjecture [5]. We also discuss analogous rigidity results for asymptotically locally flat (ALF) manifolds.
\end{abstract}

\section*{Contents}
1 Introduction ..... 1
1.1 Background ..... 1
1.2 Overview of the main results ..... 2
1.3 Existence of strictly almost Kähler ALE manifolds ..... 8
2 The ADM mass and Witten's trick ..... 10
2.1 Dirac operator in almost Kähler geometry ..... 10
2.2 The mass formula ..... 12
3 Positive mass theorem and Penrose inequality in dimension 4 ..... 17
3.1 Capping off the end with LeBrun's $\Gamma$-capsule ..... 17
3.2 Rescue à la McDuff-Taubes ..... 20
4 Rigidity results ..... 21
Bibliography ..... 25

\section*{1. Introduction}

\subsection*{1.1. Background}

Defining mass in general relativity is a very subtle issue. Roughly speaking, in Minkowski spacetime, we say that the energy content is given by an integral of the energy density of all the fields being considered over a constant time hypersurface. The
problem is that, while this construction can still be carried out for matter fields, it fails for the gravitational field. This is because the gravitational field is now described by the curvature of spacetime and there is no well-defined local concept of energy density in that setting.

This is where the concept of ADM mass enters. Introduced by Arnowitt, Deser, and Misner [4] in the early 1960s through a Hamiltonian formulation of general relativity, the ADM mass encapsulates all the properties of mass one would expect.

A fundamental desired property of mass is its positivity. The Riemannian positive mass theorem states that any complete asymptotically flat (AF) Riemannian manifold with non-negative scalar curvature has non-negative ADM mass, with equality if and only if the manifold is isometric to Euclidean space. The first rigorous proof was established by Schoen and Yau [28, 29] in dimensions up to 7, and independently by Witten [35] in all dimensions for spin manifolds.

While the ADM mass is classically defined for AF manifolds, analogous notion of mass remains well defined under other curvature decay conditions, notably in the asymptotically locally Euclidean (ALE) setting. In the Kähler ALE case, Hein and LeBrun [14] derived a transparent and beautiful mass formula expressing the ADM mass purely in terms of complex-geometric data, relating it to integrals of the scalar curvature and topological quantities. This article is devoted to derive a similar mass formula in the almost Kähler ALE case, which recovers Hein and LeBrun's formula in the Kähler case. The proof adapts Witten's proof of the positive mass conjecture for the spin case in the spin ${ }^{\mathbb{C}}$ case (notice almost Kähler implies spin ${ }^{\mathbb{C}}$ ) and hence different from Hein and LeBrun's approach. We also establish a positive mass theorem and a Penrose-type inequality for four-dimensional almost Kähler asymptotically Euclidean manifolds, following LeBrun's [19] approach, which draws on results from four-dimensional symplectic topology. We also deduce that if the ALE metric is almost Kähler-Einstein with certain decay properties and nonnegative scalar curvature, then it is in fact Kähler-Einstein. Similar rigidity statements are also discussed for asymptotically locally flat (ALF) manifolds.

\subsection*{1.2. Overview of the main results}

Definition 1.1. An almost-Kähler manifold is an almost-Hermitian manifold $(M, g, J)$ whose fundamental two form $\omega(u, v)=g(J u, v)$ is closed.

In the definition $g$ is the Riemannian metric, it preserves the almost complex structure $J$. In other words, an almost-Kähler manifold is a symplectic manifold equipped with a compatible metric.

Definition 1.2. An $n$-dimensional complete Riemannian manifold $(M, g)$ is said to be asymptotically locally Euclidean (ALE) of order $\tau>0$, if there exists a compact subset $K \subset M$ such that $M \backslash K$ has coordinates at infinity; namely there are $R>0$, a finite group $\Gamma \subset O(n)$ acting freely on $\mathbb{R}^{n} \backslash B_{R}(0)$, and a $C^{\infty}$-diffeomorphism $\mathcal{X}$ : $M \backslash K \rightarrow\left(\mathbb{R}^{n} \backslash \overline{B_{R}(0)}\right) / \Gamma$ such that $\phi=\mathcal{X}^{-1} \pi$ satisfies ( $\pi$ is the natural projection $\left.\pi: \mathbb{R}^{n} \rightarrow \mathbb{R}^{n} / \Gamma\right)$
$$\left(\phi^{*} g\right)_{i j}(x)=\delta_{i j}+a_{i j}(x) \text { for } x \in \mathbb{R}^{n} \backslash \overline{B_{R}(0)}$$
where $\left|\partial^{p} a_{i j}(x)\right|=O\left(|x|^{-\tau-p}\right)$ for all $p \geq 0$.

From now on we will write $r$ for $|x|$, where $x$ denote the coordinate at the infinity $M_{\infty}:=M \backslash K$ as described in the definition above. We follow Hein and LeBrun's [14] convention to define the ADM mass.

Definition 1.3. Let $(M, g)$ be an $n$-dimensional ALE manifold of order $\tau>\frac{n-2}{2}$ and integrable scalar curvature. Then the ADM mass of $(M, g)$ is defined as
$$\left.\mathfrak{m}(M, g):=\lim _{r \longrightarrow \infty} \frac{\boldsymbol{\Gamma}\left(\frac{n}{2}\right)}{4(n-1) \pi^{\frac{n}{2}}} \int_{S_{r} / \Gamma}\left(\partial_{i}\left(\phi^{*} g\right)_{i j}(x)-\partial_{j}\left(\phi^{*} g\right)_{i i}(x)\right) \partial_{j}\right\lrcorner d x$$
where $\phi$ is as in definition 1.2, $S_{r}$ is the Euclidean coordinate sphere of radius $r$. Bartnik [6] and Chruściel [9] independently discovered that the ADM mass is well defined, i.e., it is independent of the choice of coordinates at infinity for $\tau>\frac{n-2}{2}$.

For a smooth manifold $M$, one can define the compactly supported de Rham cohomology $H_{c}^{k}(M)$, as well as the usual de Rham cohomology $H^{k}(M)$. If $M$ is oriented, Poincaré duality gives us an isomorphism $H_{c}^{2}(M) \cong\left[H^{2 m-2}(M)\right]^{*}$. On the other hand, there is a natural map $\iota: H_{c}^{2}(M) \rightarrow H^{2}(M)$ induced by the inclusion of compactly supported forms into all differential forms, and in the ALE setting, this map is actually an isomorphism. Using this notation we now state our explicit formula for the mass.

Theorem 1.4. An almost Kähler ALE manifold of $(M, g, J)$ dimension $n=2 m \geq 4$ and of order $\tau>\frac{n-2}{2}$ with $s,\left|\nabla^{\mathrm{LC}} J\right|^{2} \in L^{1}$ has the mass given by
$$\mathfrak{m}(M, g)=\frac{(m-1)!}{4(2 m-1) \pi^{m}} \int_{M} \frac{s+s^{*}}{2} d \mathrm{v}_{g}-\frac{\left\langle\iota^{-1} c_{1}(M, J),[\omega]^{m-1}\right\rangle}{(2 m-1) \pi^{m-1}}$$
where $s$ and $s^{*}$ are respectively the scalar curvature and the star-scalar curvature of $g . c_{1}(M, J)$ is the first Chern class of the complex structure and $\langle$,$\rangle is the duality$ pairing between $H_{c}^{2}(M)$ and $H^{2 m-2}(M)$.
$s^{*}$ the star-scalar curvature is a standard notation in almost Kähler geometry, defined as
$$s^{*}=2 R(\omega, \omega)$$
where $R$ is the Riemann curvature tensor. $s$ and $s^{*}$ are related by the following identity.
$$s^{*}-s=\left|\nabla^{\mathrm{LC}} \omega\right|^{2}=\frac{1}{2}\left|\nabla^{\mathrm{LC}} J\right|^{2}$$
$\nabla^{\mathrm{LC}}$ stands for the Levi-Civita conection. Notice, $s=s^{*}$, if and only if the almost Kähler structure is Kähler. The relation above shows that in the Kähler case, we recover the mass formula for the Kähler case obtained by Hein and LeBrun [14].

Theorem 1.5 (Hein-LeBrun [14], LeBrun [19]). An Kähler ALE manifold $(M, g, J)$ of dimension $n=2 m \geq 4$ and of order $\tau>\frac{n-2}{2}$ with $s \in L^{1}$ has the mass given by
$$\mathfrak{m}(M, g)=\frac{(m-1)!}{4(2 m-1) \pi^{m}} \int_{M} s d \mathrm{v}_{g}-\frac{\left\langle\iota^{-1} c_{1}(M, J),[\omega]^{m-1}\right\rangle}{(2 m-1) \pi^{m-1}}$$

The quantity $s_{H}:=\frac{1}{2}\left(s+s^{*}\right)$ is referred to in the almost Kähler literature as the Hermitian scalar curvature, and we adopt the same terminology here.

The obvious observation is to compare theorem 1.4 with the more familiar compact case. If $(M, g, J)$ is a compact almost Kähler manifold of real dimenson $n=2 m$, then its total Hermitian scalar curvature is a symplectic invariant and known to satisfy the following formula.
$$\int_{M} \frac{s+s^{*}}{2} d \mathrm{v}_{g}=\frac{4 \pi}{(m-1)!}\left\langle c_{1}(M, J),[\omega]^{m-1}\right\rangle$$
This was first discovered by Blair [8]. Theorem 1.4 tells us that the mass measures the extent to which Blair's formula (3) fails in the ALE case:
$$\frac{4 \pi^{m}(2 m-1)}{(m-1)!} \mathfrak{m}(M, g)=\int_{M} \frac{s+s^{*}}{2} d \mathrm{v}_{g}-\frac{4 \pi}{(m-1)!}\left\langle\iota^{-1} c_{1}(M, J),[\omega]^{m-1}\right\rangle$$
An immediate consequence of theorem 1.4 is the following.
Corollary 1.6. Let $(M, g, J)$ be an almost Kähler ALE manifold of dimension $n \geq 4$ and of order $\tau>n-2$. If $(M, g, J)$ scalar-flat with $c_{1}=0$, then $(M, g, J)$ is Kähler.

When $m \geq 3$ and $J$ is integrable, i.e., when $(M, g, J)$ is Kähler, LeBrun and Hein [14] fully exploited the tools from Kähler geometry to show that even if $M$ is a priori assumed to have many "ends", it in fact has only one end (note that in our definition 1.2 we assumed the manifold has a single end). Moreover, when $(M, g, J)$ is Kähler AE, they expressed the topological term
$$\left\langle\iota^{-1} c_{1}(M, J),[\omega]^{m-1}\right\rangle$$
appearing in the mass as a sum of the volumes of complex hypersurfaces in $M$, each with a positive integer multiplicity. This allowed them to establish a positive mass theorem as well as a Penrose-type inequality. The most immediate extension of the positive mass conjecture to ALE manifolds was shown to be false by LeBrun [17]. Under some assumptions on the manifold with the ALE metric, the positive mass conjecture has been investigated in [24], [10].

Unfortunately, the almost Kähler condition does not grant us access to the powerful machinery of complex and Kähler geometry. Instead, one must rely on tools from symplectic geometry, which are substantially more effective only in dimension 4. Le-Brun has already pointed the way in this direction in [19]. While descending from the Kähler to the almost Kähler setting, one must be careful. A major advantage of the Kähler condition is that the almost-complex structure $J$ is parallel, namely $\nabla^{\mathrm{LC}} J=0$. In contrast, in the almost Kähler case we only have
$$\left|\nabla^{\mathrm{LC}} J\right|^{2}=2\left(s^{*}-s\right)=O\left(r^{-(\tau+2)}\right) \quad \text { as } r \longrightarrow \infty$$

In dimension 4, to define the mass we need $\tau>1$ and $\left|\nabla^{\mathrm{LC}} J\right|^{2} \in L^{1}$. However the decay condition $\left|\nabla^{\mathrm{LC}} J\right|^{2}=O\left(r^{-(\tau+2)}\right)$ for $\tau>1$ does not guarantee $\left|\nabla^{\mathrm{LC}} J\right|^{2} \in L^{1}$. Instead we will work with $\left|\nabla^{\mathrm{LC}} J\right|^{2}=O\left(r^{-\eta}\right)$ with $\eta>4$ as $r \longrightarrow \infty$, since this condition implies $\left|\nabla^{\mathrm{LC}} J\right|^{2} \in L^{1}$ and is convenient for using the tools from symplectic geometry we need. One should view this as analogous to the assumption imposed on the scalar
curvature $s$. The ALE condition only gives us $s=O\left(r^{-(2+\tau)}\right)$ which is not enough to ensure $s \in L^{1}$ for $\tau>1$. But $s$ needs to be in $L^{1}$ for the ADM mass to be well defined and hence usually an extra assumption of $s$ being in $L^{1}$ is made. Since we are working with almost Kähler manifolds, similar assumption on the Hermitian scalar curvature $s_{H}$ is quite natural, $s_{H} \in L^{1}$ is also required if we want to make sense of the right hand side of the equation (2). $s, s_{H} \in L^{1}$ implies $\left|\nabla^{\mathrm{LC}} J\right|^{2} \in L^{1}$. Therefore the stronger decay condition of $\left|\nabla^{\text {LC }} J\right|^{2}$ is quite natural and satisfied by the manifolds constructed in theorem 1.12.

In the definition of an ALE manifold 1.2, we assumed that the manifold only has one end. In general, one can talk about ALE manifolds with multiple ends, i.e., the complement of a compact set $M \backslash K$ can have finitely many components, each of which is diffeomorphic to a quotient $\left(\mathbb{R}^{n} \backslash \overline{B_{R}(0)}\right) / \Gamma_{i}$ and at each end the metric $g$ again becomes the Euclidean metric plus error terms that fall off sufficiently rapidly at infinity. It is assumed that the reader is able to comprehend the rigorous definition of ALE with multiple ends from the definition with one end 1.2. For the next theorem, we consider an ALE metric that may have multiple ends.

Theorem 1.7. Let $(M, g, J)$ be an almost Kähler ALE manifold of dimension 4 and of order $\tau>1$ and we allow that $M$ may have multiple "ends". As $r \longrightarrow \infty$, if $\left|\nabla^{\mathrm{LC}} J\right|^{2}=$ $O\left(r^{-\eta}\right)$ with $\eta>4$, then $M$ has exactly one end.

Theorem 1.8. Let $(M, g, J)$ be an almost Kähler ALE manifold of dimension 4 and of order $\tau>1$. If as $r \longrightarrow \infty,\left|\nabla^{\mathrm{LC}} J\right|^{2}=O\left(r^{-\eta}\right)$ with $\eta>4$, then $M$ is diffeomorphic to the complement of a tree of symplectically embedded 2 -spheres in a rational complex surface.

Theorem 1.9. Let $(M, g, J)$ be an almost Kähler ALE manifold of dimension 4 and of order $\tau>1$. If as $r \longrightarrow \infty,\left|\nabla^{\mathrm{LC}} J\right|^{2}=O\left(r^{-\eta}\right)$ with $\eta>4$, then the fundamental group of $M$ is finite.

Theorem 1.10 (Penrose inequality). Let $(M, g, J)$ be an almost Kähler AE manifold of dimension 4 and of order $\tau>1$. If $s \geq 0$ and as $r \longrightarrow \infty,\left|\nabla^{\mathrm{LC}} J\right|^{2}=O\left(r^{-\eta}\right)$ with $\eta>4$, then $(M, J)$ carries a pseudoholomorphic curve $D$ that is expressed as a sum $\sum n_{i} D_{i}$ of compact hypersurfaces of real codimension 2 with positive integer coefficients, with the property that $\bigcup_{i} D_{i} \neq \varnothing$ whenever $(M, J)$ is not diffeomorphic to $\mathbb{R}^{4}$. In terms of the curve, the mass of the manifold then satisfies
$$\mathfrak{m}(M, g) \geq \frac{1}{3 \pi} \sum_{i} n_{i} \operatorname{vol}\left(D_{i}\right)$$
and equality holds if and only if $(M, g, J)$ is scalar-flat Kähler.
This immediately gives us the following.
Theorem 1.11 (positive mass theorem). Let $(M, g, J)$ be an almost Kähler AE manifold of dimension 4 and of order $\tau>1$. If $s \geq 0$ and as $r \longrightarrow \infty,\left|\nabla^{\mathrm{LC}} J\right|^{2}=O\left(r^{-\eta}\right)$ with $\eta>4$, then $\mathfrak{m}(M, g) \geq 0$, with equality iff ( $M, g$ ) is Euclidean space.

Almost Kähler is another way of saying that the Riemannian manifold admits a symplectic form which is compatible with metric. Therefore, there are plenty of examples of almost Kähler ALE manifolds which are not Kähler. One way of constructing
them is to make compactly supported deformations to Kähler ALE manifolds which exist plenty in the literature, e.g., see [16, 17], 22. We give a brief proof of this construction in the next section.

Theorem 1.12. Let $\left(M, g_{0}, J_{0}\right)$ be a Kähler manifold. Let's say $\omega_{0}$ is the Kähler form. Then there exists a smooth compactly supported deformation $J_{t}$ of $J_{0}$ such that for all sufficiently small $t \neq 0$ :
\begin{itemize}
\item[(1)] $J_{t}$ is $\omega_{0}$-compatible,
\item[(2)] $J_{t}$ is not integrable.
\end{itemize}
Consequently $\left(M, g_{t}, J_{t}\right)$ is strictly almost Kähler, where $g_{t}(u, v):=\omega_{0}\left(u, J_{t} v\right)$.
Under the extra assumption of the almost Kähler metric being Einstein, this is in the realm of the so-called Goldberg conjecture [13]: every compact almost-Kähler Einstein manifold is actually Kähler. It should be emphasized that, although Goldberg did not clearly stipulate that the manifolds in question are required to be compact, this is taken to be the case. In fact one can construct counter-examples to the conjecture in the non-compact case in all dimensions $\geq 4$ using Tod's ansatz [3]. In the compact case, Sekigawa [30, 31] has shown that the conjecture is actually true for metrics with $s \geq 0$.

We show that Sekigawa's proof [31] actually goes through in the non-compact case under suitable decay properties of the metric and $\nabla^{\mathrm{LC}} J$ at "infinity" yielding the following.

Theorem 1.13. Let $(M, g, J)$ be an almost-Kähler Einstein ALE manifold of dimension $n \geq 4$ and of order $\tau>\frac{2}{3}(n-4)$ with $s \geq 0$ and as $r \longrightarrow \infty,\left|\left(\nabla^{\mathrm{LC}}\right)^{2} J\right|=O\left(r^{-\eta}\right)$ with $\eta \geq \frac{2}{3}(n-1)$. Then $(M, g, J)$ is Kähler Einstein.

In dimension 4, LeBrun [18] has recently established a stronger statement in the compact case. His result says that any compact almost Kähler 4-manifold $(M, g, J)$ with $s \geq 0$ and $\delta W_{+}=0$ is actually a constant-scalar-curvature Kähler manifold, where $\delta$ denotes the divergence operator and $W_{+}$is the self-dual Weyl curvature. When $g$ is an Einstein metric, this recovers Sekigawa's [30] partial solution to the 4-dimensional Goldberg conjecture. In the noncompact setting, LeBrun's proof carries over under appropriate decay conditions, leading to the following theorem.

Theorem 1.14. Let $(M, g, J)$ be a 4-dimensional almost-Kähler ALE manifold of order $\tau>0$. If $s \geq 0$ and $\delta W_{+}=0$, then $(M, g, J)$ is a constant-scalar-curvature Kähler (cscK) manifold.

Here $W_{+}$denotes the self-dual Weyl curvature of the metric $g$. In particular when $g$ is Einstein we get

Theorem 1.15. Let $(M, g, J)$ be a 4-dimensional almost-Kähler Einstein ALE manifold of order $\tau>0$ with $s \geq 0$. Then $(M, g, J)$ is Kähler Einstein.

This discussion is particularly relevant in the Ricci-flat case, namely for gravitational instantons. A classification of 4-dimensional hyper-Kähler ALE 4-manifolds was given by Kronheimer [16, 15]. A classification of Kähler ALE spaces [32, 36] are also known to be the hyper-Kähler ones and finite free quotients of them. A conjecture by Bando-Kasue-Nakajima [5] says that all 4-dimensional Ricci-flat manifolds with maximal volume growth and curvature in $L^{2}$ are Kähler. In other words, all simply connected

4-dimensional Ricci-flat manifolds with maximal volume growth and curvature in $L^{2}$ are hyper-Kähler. Maximal volume growth and curvature in $L^{2}$ in dimension 4 implies the metric is ALE of order 4 [5].

Nakajima [24] showed that the conjecture is true for the spin case if $\Gamma \subseteq \operatorname{SU}(2)$. Theorem 1.15 provides an improvement on the current state of the conjecture in the following sense.

Theorem 1.16. A 4-dimensional Ricci-flat almost Kähler manifold with maximal volume growth and curvature in $L^{2}$ is Kähler.

Remark 1. The Einstein assumption gives us $\mathrm{Ric}=\frac{s}{n} g$. Hence by Bonnet-Myers an ALE Einstein metric can not have positive scalar curvature. So, only the Ricci-flat case in theorems 1.13 and 1.15 are not vacuous. Moreover with the extra assumption: $s \in L^{1}$, it also cancels out the negative Einstein constant case.

It is worth clarifying the extent to which theorem 1.16 provides new information. For $\Gamma \subset S U(2)$, the symplectic fillings of $S^{3} / \Gamma$ with respect to the standard contact structure are diffeomorphic to the blow-ups of the minimal resolution of $\mathbb{C}^{2} / \Gamma$ ([23, 27, 26]). But the minimal resolution saturates the ALE Hitchin-Thorpe inequality [24] and each blow up violates the inequality. Consequently no non-trivial blow-up can admit a Ricci-flat ALE metric. Hence, within the class relevant to theorem 1.16, the case $\Gamma \subset S U(2)$ appears to be already constrained by the known classification of symplectic fillings together with the ALE Hitchin-Thorpe inequality. In particular, a genuinely new non-vacuous application of theorem 1.16, if one exists, should be sought in the case $\Gamma \subset U(2) \backslash S U(2)$. We do not know at present whether such an example exists.

The analogous rigidity statements also hold for asymptotically locally flat (ALF) manifolds. These are manifolds which are asymptotic to a circle fibration over a Euclidean base, with fibres of asymptotically constant length.

To introduce such class of metrics, we first consider the total space $\mathcal{E}^{n+1}$ of a principal $S^{1}$ bundle $\pi$ over $\mathbb{R}^{n} \backslash \overline{B_{R}(0)}$. Given a positive number $L$, we introduce the vector field $T$ that is equal to $\frac{L}{2 \pi}$ times the infinitesimal generator of the $S^{1}$ action and consider a "model metric" $h$ on $\mathcal{E}$, given by
$$h=\pi^{*} g_{\mathbb{R}^{n}}+\eta^{2}$$
where $\eta$ is a connection 1-form, namely an $S^{1}$ invariant 1-form on $\mathcal{X}$ such that $\eta(T)=1$. Observe that each fiber has length $L$. For such a 1-form $\eta$, one might write $d \eta=\pi^{*} \Omega$ for some $\Omega$ on the base and we will assume this "curvature" 2-form decays at "infinity", i.e., there is a positive number $\tau$ such that
$$D^{i} \Omega=O\left(r^{-\tau-1-i}\right), 0 \leq i \leq 2$$
where $D$ denotes the flat connection on $\mathbb{R}^{n}$.
Definition 1.17. An $n+1$ - dimensional complete Riemannian manifold $(M, g)$ is said to be asymptotically locally flat (ALF) of order $\tau>0$, if there exists a compact subset $K \subset M$ such that $M \backslash K$ has coordinates at infinity: namely there exist $R>0$ and a $C^{\infty}$-diffeomorphism $\mathcal{X}: M \backslash K \rightarrow \mathcal{E}$ such that there exists a model metric $h$ on $\mathcal{E}$
satisfying (5) and
$$\left(\nabla^{h}\right)^{i}\left(\left(\mathcal{X}^{-1}\right)^{*} g-h\right)=O\left(r^{-\tau-i}\right), 0 \leq i \leq 3$$

The proofs used in the ALE case extend directly, mutatis mutandis, to yield the following theorems in the ALF case.

Theorem 1.18. Let $(M, g, J)$ be an almost-Kähler Einstein ALF manifold of dimension $n+1 \geq 4$ and of order $\tau>\frac{2}{3}(n-4)$ with $s \geq 0$ and as $r \longrightarrow \infty,\left|\left(\nabla^{\mathrm{LC}}\right)^{2} J\right|=O\left(r^{-\eta}\right)$ with $\eta \geq \frac{2}{3}(n-1)$. Then $(M, g, J)$ is Kähler Einstein.

Theorem 1.19. Let $(M, g, J)$ be a 4-dimensional almost-Kähler ALF manifold of order $\tau>0$. If $s \geq 0$ and $\delta W_{+}=0$, then $(M, g, J)$ is a constant-scalar-curvature Kähler (cscK) manifold.

Theorem 1.20. Let $(M, g, J)$ be a 4-dimensional almost-Kähler Einstein ALF manifold of order $\tau>0$ with $s \geq 0$. Then $(M, g, J)$ is Kähler Einstein.

This theorem has an immediate corollary.
Corollary 1.21. (1) $S^{2} \times \mathbb{R}^{2}$ does not admit a symplectic form which is compatible with the Riemannian Kerr metrics.
\begin{itemize}
\item[(2)] $\mathbb{C P}^{2} \backslash S^{1}$ does not admit a symplectic form which is compatible with the Chen-Teo metric.
\item[(3)] $\mathbb{C P}^{2} \backslash\{$ point $\}$ does not admit a symplectic form which is compatible with the Taub-bolt metric.
\end{itemize}

The article is organised as follows: §2 discusses Dirac operators in almost Kähler geometry and presents the proof of Theorem 1.4. §3 discusses the positive mass theorem for almost Kähler AE manifolds and related results. §4 establishes the rigidity results for almost Kähler-Einstein ALE manifolds.

Acknowledgments. The author is grateful to Olivier Biquard for helpful discussions and for his feedback on an initial draft of this article. He also thanks David Blair for sharing a copy of his article [8]. Finally, the author would like to thank the anonymous referee for their valuable suggestions, especially for drawing his attention to the issue discussed in remark 1, which significantly helped clarify the scope of this article. This work was supported by European Union's Horizon 2020 Europe research and innovation programme under the Marie Sklodowska-Curie grant agreement no 101034255.

\subsection*{1.3. Existence of strictly almost Kähler ALE manifolds}

Proof of theorem 1.12: We start with a Kähler ALE manifold $\left(M^{2 m}, g_{0}, J_{0}\right)$. Choose a point $p \in M$ and a holomorphic coordinate chart $\left(z_{1}, \ldots, z_{m}\right)$ centered at $p$ for the complex structure $J_{0}$. Let $e_{k}=\frac{\partial}{\partial x_{k}}, J_{0} e_{k}=\frac{\partial}{\partial y_{k}}$, where $z_{k}=x_{k}+i y_{k}$. Choose a non-constant smooth compactly supported function $f \in C_{c}^{\infty}(U)$ supported in the coordinate neighborhood $U$ such that $\partial_{z_{1}} f(0) \neq 0$ and define a smooth endomorphism $A \in \Gamma(\operatorname{End}(T M))$ by
$$A e_{1}=f e_{1}, A\left(J_{0} e_{1}\right)=-f J_{0} e_{1} \text { and } A e_{j}=A\left(J_{0} e_{j}\right)=0 \text { for } j \geq 2$$

Then $A J_{0}+J_{0} A=0$ and $A$ is symmetric with respect to $g_{0}$, i.e., $g_{0}(A u, v)=g_{0}(u, A v)$ because in the orthonormal frame the matrix of $A$ reads $\operatorname{diag}(f,-f, 0, \cdots, 0)$. Now define $J_{t}=e^{t A} J_{0} e^{-t A}$. Clearly $J_{t}^{2}=-1$. Since $A$ anti-commutes with $J_{0}$ (this implies $J_{t}=$ $\left.J_{0} e^{-2 t A}\right)$ and $A$ is $g_{0}$-symmetric we have
$$g_{t}\left(J_{t} u, J_{t} v\right)=\omega_{0}\left(J_{0} e^{-2 t A} u,-v\right)=g_{0}\left(e^{-2 t A} u, v\right)=g_{0}\left(u, e^{-2 t A} v\right)=\omega_{0}\left(u, J_{t} v\right)=g_{t}(u, v)$$
For small enough $t, g_{t}(u, u)>0$ for non-zero $u$. Therefore, $\left(M, g_{t}, J_{t}\right)$ is almost Kähler ALE for small enough $t$. Notice that for small $t, J_{t}$ has an expansion
$$J_{t}=J_{0}+t 2 A J_{0}+O\left(t^{2}\right)$$
We calculate the Nijenhuis tensor of $J_{t}$ :
$$N_{J_{t}}(u, v)=\left[J_{t} u, J_{t} v\right]-J_{t}\left[J_{t} u, v\right]-J_{t}\left[u, J_{t} v\right]-[u, v]$$
Using the fact that $N_{J_{0}} \equiv 0$, we get
$$\begin{aligned}
N_{J_{t}}(u, v)= & 2 t\left(\left[A J_{0} u, J_{0} v\right]+\left[J_{0} u, A J_{0} v\right]-J_{0}\left[A J_{0} u, v\right]-A J_{0}\left[J_{0} u, v\right]-J_{0}\left[u, A J_{0} v\right]\right. \\
& \left.-A J_{0}\left[u, J_{0} v\right]\right)+O\left(t^{2}\right)
\end{aligned}$$
In the holomorphic coordinate neighbourhood $U$, we calculate this for $u=\partial_{z_{1}}, v=\partial_{\bar{z}_{1}}$. We have
$$\begin{aligned}
J_{0}\left(\partial_{z_{1}}\right)=J_{0}\left(e_{1}+J_{0} e_{1}\right) & =-\partial_{\bar{z}_{1}}, J_{0}\left(\partial_{\bar{z}_{1}}\right)=J_{0}\left(e_{1}-J_{0} e_{1}\right)=\partial_{z_{1}} \\
A\left(\partial_{z_{1}}\right)=A\left(e_{1}+J_{0} e_{1}\right) & =f \partial_{\bar{z}_{1}}, A\left(\partial_{\bar{z}_{1}}\right)=A\left(e_{1}-J_{0} e_{1}\right)=f \partial_{z_{1}}
\end{aligned}$$
Therefore,
$$\begin{aligned}
N_{J_{t}}\left(\partial_{z_{1}}, \partial_{\bar{z}_{1}}\right)= & 2 t\left(\left[-f \partial_{\bar{z}_{1}}, \partial_{z_{1}}\right]+\left[-\partial_{\bar{z}_{1}}, f \partial_{z_{1}}\right]-J_{0}\left[-f \partial_{\bar{z}_{1}}, \partial_{\bar{z}_{1}}\right]-A J_{0}\left[-\partial_{\bar{z}_{1}}, \partial_{\bar{z}_{1}}\right]\right. \\
& \left.-J_{0}\left[\partial_{z_{1}}, f \partial_{z_{1}}\right]-A J_{0}\left[\partial_{z_{1}}, \partial_{z_{1}}\right]\right)+O\left(t^{2}\right) \\
= & 2 t\left(\left(\partial_{z_{1}} f\right) \partial_{\bar{z}_{1}}-\left(\partial_{\bar{z}_{1}} f\right) \partial_{z_{1}}-\left(\partial_{\bar{z}_{1}} f\right) \partial_{z_{1}}+\left(\partial_{z_{1}} f\right) \partial_{\bar{z}_{1}}\right)+O\left(t^{2}\right) \\
= & 4 t\left(\left(\partial_{z_{1}} f\right) \partial_{\bar{z}_{1}}-\left(\partial_{\bar{z}_{1}} f\right) \partial_{z_{1}}\right)+O\left(t^{2}\right)
\end{aligned}$$
Extend the vector fields $\partial_{z_{1}}, \partial_{\bar{z}_{1}}$ on whole of $M$ smoothly and call them $\partial_{z_{1}}, \partial_{\bar{z}_{1}}$ again by abuse of notation. Now define a map
$$F: t \mapsto N_{J_{t}}\left(\partial_{z_{1}}, \partial_{\bar{z}_{1}}\right)(p)$$
We have
$$F(0)=0, F^{\prime}(0) \neq 0 \text { since } \partial_{z_{1}} f(0) \neq 0$$
Hence $\exists \epsilon>0$ such that $\forall t \in(0, \epsilon), F(t) \neq 0$. Hence $\forall t \in(0, \epsilon), N_{J_{t}} \not \equiv 0$. \(\square\)

Notice if we implement this construction on a Kähler ALE manifold, the geometry remains same outside a compact set so the metric remains ALE of the same order.

\section*{2. The ADM mass and Witten's trick}

\subsection*{2.1. Dirac operator in almost Kähler geometry}

For any almost Hermitian manifold $(M, g, J)$ of dimension $n=2 m \geq 4$, a connection ∇ on $M$ (acting on sections of the tangent bundle $T M$ ) is Hermitian if it preserves the metric $g$ and the almost complex structure $J$ :
$$\nabla g=0, \nabla J=0$$
Each connection ∇ determines a Cauchy Riemann operator, denoted by $\partial^{\nabla}$, defined as the (0, 1)-part of ∇:
$$\bar{\partial}_{X}^{\nabla} Y=\frac{1}{2}\left(\nabla_{X} Y+J \nabla_{J X} Y\right)$$
There is also an intrinsic Cauchy Riemann operator coming from the almost complex structure $J$ defined by
$$\bar{\partial}_{X} Y=\frac{1}{4}([X, Y]+[J X, J Y]+J[J X, Y]-J[X, J Y])$$
Gauduchon [12] distinguished a real affine line in the set of Hermitian connections. We pick one element from the affine line, the Chern connection: $\nabla^{\mathrm{Ch}}$. The terminology stems from the fact that, in the integrable case, it coincides with the Chern connection of the tangent bundle viewed as a Hermitian, holomorphic bundle of rank $m$. The Chern connection is characterised by the fact that its Cauchy Riemann operator coincides with the intrinsic one:
$$\bar{\partial}^{\nabla^{\mathrm{Ch}}}=\bar{\partial}$$
The metric $g$ defines a Hermitian metric on the anti-cannical bundle $K^{-1}$ and the Chern connection induces a unitary connection on $K^{-1}$, which we call by $A^{\mathrm{Ch}}$.

Now let's talk about spinors. We start with the canonical spinor bundle on $(M, g, J)$ :
$$S_{+}=\bigoplus_{p=0}^{m} \Lambda^{0,2 p} M, \quad S_{-}=\bigoplus_{p=0}^{m-1} \Lambda^{0,2 p+1} M$$
To define a spin connection on $S=S_{+} \oplus S_{-}$, we need a unitary connection $A$ on $K^{-1}$. We call the corresponding Dirac operator $D_{A}$.

There is another intrinsic first order differential operator with the same index of $D_{A}$, which sends $S_{+}$to $S_{-}$and vice versa, namely the normalised Dolbeault operator defined by $\sqrt{2}\left(\bar{\partial}+\bar{\partial}^{\star}\right)$. Here $\bar{\partial}$ on the sections of $\Lambda^{0, p} M$ is defined as
$$\bar{\partial} \psi=(d \psi)^{(0, p+1)}$$
for any $(0, p)$-form $\psi$ and $\bar{\partial}^{*}$ is the Hermitian adjoint of $\bar{\partial}$.
Gauduchon [12] proved that on an almost Kähler manifold $(M, g, J)$, we have
$$D_{A^{\mathrm{Ch}}}=\sqrt{2}\left(\bar{\partial}+\bar{\partial}^{*}\right)$$

In dimension 4, Taubes 34 obtained the same result by indirect arguments and it is a key fact in his magnum opus: "SW=Gr".

For any unitary connection $A$ on $K^{-1}$ and a spinor $\psi \in \Gamma(S)$, the gauge group $\mathcal{G}=$ $\operatorname{Map}\left(M, S^{1}\right)$ acts on the pair $(A, \psi)$ by pull-back. Hence for $g \in \mathcal{G}$,
$$g \cdot(A, \psi)=\left(A-2 g^{-1} d g, g \psi\right)$$
Moreover, $(A, \psi)$ solves the Dirac equation $D_{A} \psi=0$ iff $g \cdot(A, \psi)$ solves it.
The discussion above along with the identity (7) gives us the following lemma.
Lemma 2.1. Up to gauge equivalence there exists a canonical connection $A_{0}$ and a non-trivial spinor $\varphi_{0} \in \Omega^{0} \subset \Gamma\left(S_{+}\right)$, such that $D_{A_{0}} \varphi_{0}=0$. $\varphi_{0}$ can be taken to have point-wise norm one.

Proof. Take $\psi_{0} \in \Omega^{0}$ to be to the constant section of $M \times \mathbb{C}$ which assigns $1 \in \mathbb{C}$ to every point of $M$. Then $A_{0}=A^{\mathrm{Ch}}, \varphi_{0}=\psi_{0}$ solves the Dirac equation $D_{A_{0}} \varphi_{0}=0$ because $d \psi_{0}=0$ and therefore $\bar{\partial} \psi_{0}=0$. \(\square\)

In spinorial terms the Chern connection is characterised as follows (see §1.4.3 in [25] for a detailed exposition). For the constant section $\psi_{0}, A^{\mathrm{Ch}}$ is the unique connection on $K^{-1}$ such that the induced connection on $S, \nabla_{A^{\mathrm{ch}}}$ satisfies
$$\nabla_{A^{\mathrm{Ch}}} \psi_{0} \in \Gamma\left(\Lambda^{1} \otimes \Lambda^{0,2}\right)$$
In fact just using this condition above one can prove that $D_{A^{\text {Ch }}} \psi_{0}=0$. To see this first notice that $\Omega^{0}$ is a $-m i$ eigenspace of the Clifford action of the symplectic form: $\operatorname{cl}(\omega)$ and $\Omega^{0,2}$ is a $c i$ eigenspace of $\operatorname{cl}(\omega)$, where $c \neq-m$. For example, $c=2$ when $m=2$, $c=1$ when $m=3$, and $c=0$ when $m=4$. Now apply $D_{A^{\text {Ch }}}$ on $\operatorname{cl}(\omega) \psi_{0}$ to get
$$D_{A^{\mathrm{Ch}}}\left(\operatorname{cl}(\omega) \psi_{0}\right)=\operatorname{cl}\left(d \omega+d^{*} \omega\right) \psi_{0}+\operatorname{cl}\left((1 \otimes \operatorname{cl}(\omega)) \nabla_{A^{\mathrm{Ch}}} \psi_{0}\right)$$
The rightmost term here means the following: start with $\nabla_{A^{\mathrm{ch}}} \psi_{0} \in \Gamma\left(\Lambda^{1} \otimes \Lambda^{0,2}\right)$, first apply $1 \otimes \operatorname{cl}(\omega)$ to get another element of $\Gamma\left(\Lambda^{1} \otimes \Lambda^{0,2}\right)$ and then apply cl to get an element of $\Gamma\left(S_{-}\right)$. Because $\omega$ is closed and co-closed, equation (8) becomes
$$-m i D_{A^{\mathrm{Ch}}}\left(\psi_{0}\right)=c i D_{A^{\mathrm{Ch}}}\left(\psi_{0}\right)$$
Since $c \neq-m$, this proves $D_{A^{\text {Ch }}} \psi_{0}=0$.
$\nabla_{A^{\mathrm{Ch}}} \psi_{0}=0$ iff $(M, g, J)$ is Kähler, instead if it is almost Kähler, we still have $D_{A^{\text {Ch }}} \psi_{0}=0$. We also have $\nabla^{\text {LC }} \omega \in \Gamma\left(\Lambda^{1} \otimes\left(\Lambda^{2,0} \oplus \Lambda^{0,2}\right)\right)$ and in fact $\nabla_{A^{\text {Ch }}} \psi_{0}$ and $\nabla^{\mathrm{LC}} \omega$ are essentially the same. In concrete terms, we have a pointwise equality of norms:

Lemma 2.2.
$$\left|\nabla_{A^{\mathrm{Ch}}} \psi_{0}\right|^{2}=\frac{1}{8}\left|\nabla^{\mathrm{LC}} \omega\right|^{2}$$

Proof. The Weitzenböck formula gives us
$$0=D_{A^{\mathrm{Ch}}}^{2} \psi_{0}=\nabla_{A^{\mathrm{Ch}}}^{*} \nabla_{A^{\mathrm{Ch}}} \psi_{0}+\frac{s}{4} \psi_{0}+\frac{1}{2} \operatorname{cl}\left(F_{A^{\mathrm{Ch}}}\right) \psi_{0}$$

Now take inner product with $\psi_{0}$ on both sides of the equation. From Blair's calculation [8], it is evident that the only term in $\operatorname{cl}\left(F_{A^{\mathrm{Ch}}}\right)$ which contributes to the inner product is $-\frac{i}{4 m}\left(s+s^{*}\right) \operatorname{cl}(\omega)$. All remaining curvature terms lie in directions orthogonal to $\omega$ and map $\Omega^{0}$ into forms orthogonal to $\Omega^{0}$. Thereafter we have
$$0=\left\langle\nabla_{A^{\mathrm{Ch}}}^{*} \nabla_{A^{\mathrm{Ch}}} \psi_{0}, \psi_{0}\right\rangle+\frac{s}{4}\left|\psi_{0}\right|^{2}-\frac{i}{8 m}\left(s+s^{*}\right)\left\langle\operatorname{cl}(\omega) \psi_{0}, \psi_{0}\right\rangle$$
Since $\psi_{0}$ has pointwise constant norm 1,
$$\left\langle\nabla_{A^{\mathrm{Ch}}}^{*} \nabla_{A^{\mathrm{Ch}}} \psi_{0}, \psi_{0}\right\rangle=\left|\nabla_{A^{\mathrm{Ch}}} \psi_{0}\right|^{2}+\frac{1}{2} \Delta\left|\psi_{0}\right|^{2}=\left|\nabla_{A^{\mathrm{Ch}}} \psi_{0}\right|^{2}$$
$\Omega^{0}$ is a $-m i$ eigenspace of $\operatorname{cl}(\omega)$. Therefore equation (10) reads
$$0=\left|\nabla_{A^{\mathrm{Ch}}} \psi_{0}\right|^{2}+\frac{s}{4}-\frac{2 s+\left|\nabla^{\mathrm{LC}} \omega\right|^{2}}{8}$$
which in turns gives $\left|\nabla_{A^{\mathrm{Ch}}} \psi_{0}\right|^{2}=\frac{1}{8}\left|\nabla^{\mathrm{LC}} \omega\right|^{2}$. \(\square\)

Blair's article [8] is difficult to find, instead one can also look at his book [7] (proof of theorem 10.6) for the calculation used above. In dimension 4, LeBrun gave a different proof of this calculation using Penrose spinor calculus ([20], proposition 2.1).

\subsection*{2.2. The mass formula}

We adapt Witten's spectacular observation on computing the ADM mass $m(M, g)$ of a spin manifold in terms of a harmonic spinor. To set up the proof of the derivation of the mass formula (2), we need a lemma and a proposition.

We take a frame $\left(e_{1}, \ldots, e_{n}\right)$, parallel at an arbitrary point $p \in M$. The dual coframe is given by $\left(e^{1}, \ldots, e^{n}\right)$.

Lemma 2.3. Let $N \subset M$ be any bounded subset of $M$ with $\partial N$ smooth. Then for any $\varphi \in \Gamma(S)$, we have
$$\int_{N}\left(\left|\nabla_{A} \varphi\right|^{2}-\left|D_{A} \varphi\right|^{2}+\frac{s}{4}|\varphi|^{2}+\frac{1}{2}\left\langle\operatorname{cl}\left(F_{A}\right) \varphi, \varphi\right\rangle\right) d \mathrm{v}_{g}=\int_{\partial N} \sum_{i=1}^{n}\left\langle\varphi, L_{i} \varphi\right\rangle * e^{i}$$
where $L_{i}=\sum_{j=1}^{n}\left(\delta_{i j}+\operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right)\right) \nabla_{j}$.
Proof. We make the following calculations.
$$\begin{aligned}
-\left|D_{A} \varphi\right|^{2} & =\sum_{i, j=1}^{n}\left\langle-\operatorname{cl}\left(e_{i}\right) \nabla_{i} \varphi, \operatorname{cl}\left(e_{j}\right) \nabla_{j} \varphi\right\rangle \\
& =\sum_{i, j=1}^{n}\left\langle\nabla_{i} \varphi, \operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right) \nabla_{j} \varphi\right\rangle \\
& =\sum_{i, j=1}^{n} \nabla_{i}\left\langle\varphi, \operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right) \nabla_{j} \varphi\right\rangle-\left\langle\varphi, D_{A}^{2} \varphi\right\rangle
\end{aligned}$$
and
$$\begin{aligned}
\left|\nabla_{A} \varphi\right|^{2} & =\sum_{i=1}^{n}\left\langle\nabla_{i} \varphi, \nabla_{i} \varphi\right\rangle \\
& =\sum_{i=1}^{n} \nabla_{i}\left\langle\varphi, \nabla_{i} \varphi\right\rangle-\sum_{i=1}^{n}\left\langle\varphi, \nabla_{i} \nabla_{i} \varphi\right\rangle \\
& =\sum_{i=1}^{n} \nabla_{i}\left\langle\varphi, \nabla_{i} \varphi\right\rangle+\left\langle\varphi, \nabla_{A}^{*} \nabla_{A} \varphi\right\rangle
\end{aligned}$$
Finally we complement these calculations above with the Weitzenböck formula
$$D_{A}^{2}=\nabla_{A}^{*} \nabla_{A}+\frac{s}{4}+\frac{1}{2} \operatorname{cl}\left(F_{A}\right)$$
and the divergence theorem to finish the proof. \(\square\)

Proposition 2.4. Let ( $M, g, J$ ) be an ALE almost Kähler manifold with $\tau>\frac{n-2}{2}$ and $s,\left|\nabla^{\mathrm{LC}} J\right|^{2} \in L^{1}$. Then in any asymptotic coordinate system, the ADM mass is given by
$$\mathfrak{m}(M, g)=\lim _{r \rightarrow \infty} \frac{1}{2(2 m-1) \pi^{m}} \int_{S_{r} / \Gamma} \theta \wedge \omega^{m-1}$$
for any 1-form $\theta$ with $d \theta=i F_{A^{\mathrm{Ch}}}$ on the end $M_{\infty}$.
Proof. Taking the Bartnik-Chruściel coordinate invariance of the mass [6, 9], we begin by first checking that the assertion is true in a particular asymptotic coordinate system and for a particular choice of $\theta$.

We set up the calculations in local coordinates near "infinity". Let $U \subset M \rightarrow Q$ be a local section of the frame bundle $Q . e$ consists of an orthonormal frame $e=\left(e_{1}, \ldots, e_{n}\right)$ of vector fields defined on the open set $U \subset M$. The local connection form $Z^{e}=e^{*}(Z)$ : $T U \rightarrow \mathfrak{s o}(n)$ is given by the formula:
$$Z^{e}=\sum_{k<l} w_{k l} E_{k l}$$
where the forms $w_{k l}$ denote the forms defining the Levi-Civita connection, $w_{k l}=$ $g\left(\nabla e_{k}, e_{l}\right)$ and $E_{k l}$ are the standard basis matrices of the Lie algebra $\mathfrak{s o}(n)$. Analogously, we fix a section $s: U \rightarrow P_{1}$ of the $U(1)$-principal bundle associated to the canonical spin ${ }^{\mathbb{C}}$-structure and obtain a local connection form
$$A_{s}=s^{*}(A): T U \rightarrow i \mathbb{R}$$
$A_{s}$ is an imaginary valued one form defined on the set $U$. A section $\varphi \in \Gamma(U, S)$ of the spinor bundle $S$ over $U$ can be described by a function $\varphi: U \rightarrow \mathbb{C}^{\left(2^{\frac{n}{2}}\right)}$ using a trivialisation of $S$ over $U$ and using the connection $A$ on the corresponding $U(1)$ -bundle, we lift the Levi-Civita connection on $S$. Finally the covariant derivative of $\varphi$ is computed according to the formula [11]:
$$\nabla_{A} \varphi=d \varphi+\frac{1}{2} \sum_{k<l} w_{k l} \operatorname{cl}\left(e_{k}\right) \operatorname{cl}\left(e_{l}\right) \varphi+\frac{1}{2} A_{s} \varphi$$

Now we take $\varphi=\psi_{0}, A=A^{\mathrm{Ch}}$ and a bounded subset $N \subset M$ with $\partial N=S_{r} / \Gamma$, lemma 2.2 and 2.3 together give us
$$\int_{S_{r} / \Gamma} \sum_{i=1}^{n}\left\langle\psi_{0}, L_{i} \psi_{0}\right\rangle * e^{i}=0$$
Using (11) we compute the integrand. First we take care of the part which involves the connection $A^{\mathrm{Ch}}$.
$$\begin{aligned}
& \sum_{i, j=1}^{n}\left\langle\psi_{0},\left(\delta_{i j}+\operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right)\right) A_{s}^{\mathrm{Ch}}\left(e_{j}\right) \psi_{0}\right\rangle * e^{i} \\
& =\sum_{i, j=1}^{n}\left\langle\psi_{0}, \operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right) A_{s}^{\mathrm{Ch}}\left(e_{j}\right) \psi_{0}\right\rangle * e^{i}+\sum_{i=1}^{m}\left\langle\psi_{0}, A_{s}^{\mathrm{Ch}}\left(e_{i}\right) \psi_{0}\right\rangle * e^{i} \\
& =\sum_{i=1}^{n}\left\langle\psi_{0}, \operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(A_{s}^{\mathrm{Ch}}\right) \psi_{0}\right\rangle * e^{i}+\sum_{i=1}^{m}\left\langle\psi_{0}, A_{s}^{\mathrm{Ch}}\left(e_{i}\right) \psi_{0}\right\rangle * e^{i}
\end{aligned}$$
We use explicit formula for Clifford action of a 1-form to simplify it further. For a complexified 1-form $\alpha \in \Omega^{1} \otimes \mathbb{C}$ and a spinor $\xi \in \Omega^{0, k}$, the Clifford action of $\alpha=$ $\left(\alpha^{0,1}+\alpha^{1,0}\right)$ on $\xi$ is given by the following formula:
$$\left.\operatorname{cl}(\alpha) \xi=\sqrt{2}\left(\alpha^{0,1} \wedge \xi-\overline{\alpha^{1,0}}\right\lrcorner \xi\right)$$
$\left.\overline{\alpha^{1,0}}\right\lrcorner \xi \in \Omega^{0, k-1}$ is the contraction of $\xi$ by $\left(\overline{\alpha^{1,0}}\right)^{\#}$ defined by $\left.\overline{\alpha^{1,0}}\right\lrcorner \xi:=\iota_{\left(\overline{\alpha^{1,0}}\right)^{\#}}(\xi)$, where $\left(\overline{\alpha^{1,0}}\right)^{\#}$ is the vector field metric dual to $\overline{\alpha^{1,0}}$. Using this we notice
$$\begin{aligned}
& \left\langle\psi_{0}, \operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(A_{s}^{\mathrm{Ch}}\right) \psi_{0}\right\rangle+\left\langle\psi_{0}, A_{s}^{\mathrm{Ch}}\left(e_{i}\right) \psi_{0}\right\rangle \\
& =\left\langle\psi_{0}, \operatorname{cl}\left(e_{i}\right)\left(\sqrt{2} \psi_{0}\left(A_{s}^{\mathrm{Ch}}\right)^{0,1}\right)+A_{s}^{\mathrm{Ch}}\left(e_{i}\right) \psi_{0}\right\rangle \\
& \left.=\left\langle\psi_{0},-2 \psi_{0} e_{i}^{0,1}\right\lrcorner\left(A_{s}^{\mathrm{Ch}}\right)^{0,1}+A_{s}^{\mathrm{Ch}}\left(e_{i}\right) \psi_{0}\right\rangle \\
& =-2\left\langle\psi_{0}, \psi_{0}\left(A_{s}^{\mathrm{Ch}}\right)^{0,1}\left(e_{i}^{0,1}\right)\right\rangle+A_{s}^{\mathrm{Ch}}\left(e_{i}\right) \\
& =-2\left\langle\psi_{0},\left(\frac{1}{2}\left(A_{s}^{\mathrm{Ch}}+i A_{s}^{\mathrm{Ch}} \circ J\right)\right)\left(\frac{1}{2}\left(e_{i}+i J e_{i}\right)\right) \psi_{0}+A_{s}^{\mathrm{Ch}}\left(e_{i}\right) \psi_{0}\right\rangle \\
& =\left\langle\psi_{0},\left(-A_{s}^{\mathrm{Ch}}\left(e_{i}\right)-i A_{s}^{\mathrm{Ch}}\left(J e_{i}\right)+A_{s}^{\mathrm{Ch}}\left(e_{i}\right)\right) \psi_{0}\right\rangle \\
& =-i A_{s}^{\mathrm{Ch}}\left(J e_{i}\right)
\end{aligned}$$
One can infact choose an orthonormal basis at $p \in M$ of the form $\left\{e_{i}\right\}=\left\{e_{k}, J e_{k}\right\}$. Then we get $\omega=\sum_{k} e^{k} \wedge J e^{k}$ and
$$\sum_{i=1}^{n} i A_{s}^{\mathrm{Ch}}\left(J e_{i}\right) * e_{i}=i A_{s}^{\mathrm{Ch}} \wedge \frac{\omega^{m-1}}{(m-1)!}$$

Now the total integrand reads
$$\begin{aligned}
& \sum_{i=1}^{n}\left\langle\psi_{0}, L_{i} \psi_{0}\right\rangle * e^{i} \\
& =\sum_{i, j=1}^{n}\left\langle\psi_{0},\left(\delta_{i j}+\operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right)\right) \nabla_{j}^{\mathrm{Ch}} \psi_{0}\right\rangle * e^{i} \\
& =\frac{1}{4} \sum_{k \neq l} \sum_{i, j=1}^{n}\left\langle\psi_{0},\left(\delta_{i j}+\operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right)\right) w_{k l}\left(e_{j}\right) \operatorname{cl}\left(e_{k}\right) \operatorname{cl}\left(e_{l}\right) \psi_{0}\right\rangle * e^{i}-\frac{i}{2} A_{s}^{\mathrm{Ch}} \wedge \frac{\omega^{m-1}}{(m-1)!} \\
& =\frac{1}{4} \sum_{k \neq l} \sum_{i \neq j} w_{k l}\left(e_{j}\right)\left\langle\psi_{0}, \operatorname{cl}\left(e_{i}\right) \operatorname{cl}\left(e_{j}\right) \operatorname{cl}\left(e_{k}\right) \operatorname{cl}\left(e_{l}\right) \psi_{0}\right\rangle * e^{i}-\frac{i}{2} A_{s}^{\mathrm{Ch}} \wedge \frac{\omega^{m-1}}{(m-1)!} \\
& =\frac{1}{4} \sum_{k \neq l} \sum_{i \neq j} w_{k l}\left(e_{j}\right)\left|\psi_{0}\right|^{2}\left(\delta_{i l} \delta_{j k}-\delta_{i k} \delta_{j l}\right) * e^{i}-\frac{i}{2} A_{s}^{\mathrm{Ch}} \wedge \frac{\omega^{m-1}}{(m-1)!} \\
& =\frac{1}{4} \sum_{i \neq j}\left(\omega_{j i}\left(e_{j}\right)-\omega_{i j}\left(e_{j}\right)\right) * e^{i}-\frac{i}{2} A_{s}^{\mathrm{Ch}} \wedge \frac{\omega^{m-1}}{(m-1)!}
\end{aligned}$$
Since the Christoffel symbols $\boldsymbol{\Gamma}_{i j}^{k}=g\left(\nabla_{e_{i}} e_{j}, e_{k}\right)$ are symmetric in $i \leftrightarrow j$, we get $w_{j k}\left(e_{i}\right)=w_{i k}\left(e_{j}\right)$. We notice that
$$\omega_{j i}\left(e_{j}\right)-\omega_{i j}\left(e_{j}\right)=\omega_{j i}\left(e_{j}\right)-\omega_{j j}\left(e_{i}\right)$$
On the other hand the expression ( $\partial_{j} g_{j i}-\partial_{i} g_{j j}$ ) also reads
$$\begin{aligned}
\left(\nabla_{j} g_{j i}-\nabla_{i} g_{j j}\right) & =g\left(\nabla_{e_{j}} e_{j}, e_{i}\right)+g\left(e_{j}, \nabla_{j} e_{i}\right)-g\left(\nabla_{i} e_{j}, e_{j}\right)-g\left(e_{j}, \nabla_{i} e_{j}\right) \\
& =w_{j i}\left(e_{j}\right)+w_{i j}\left(e_{j}\right)-2 w_{j j}\left(e_{i}\right) \\
& =w_{j i}\left(e_{j}\right)+w_{j j}\left(e_{i}\right)-2 w_{j j}\left(e_{i}\right) \\
& =w_{j i}\left(e_{j}\right)-w_{j j}\left(e_{i}\right)
\end{aligned}$$
Therefore we get
$$\sum_{i=1}^{n}\left\langle\psi_{0}, L_{i} \psi_{0}\right\rangle * e^{i}=\frac{1}{4} \sum_{i \neq j}\left(\nabla_{j} g_{j i}-\nabla_{i} g_{j j}\right) * e^{i}-\frac{i}{2} A_{s}^{\mathrm{Ch}} \wedge \omega^{m-1}$$
Bartnik [6] showed us that
$$\left.\lim _{r \rightarrow \infty} \int_{S_{r} / \Gamma} \sum_{i \neq j}\left(\nabla_{j} g_{j i}-\nabla_{i} g_{j j}\right) * e^{i}=\int_{S_{\infty} / \Gamma} \sum\left(\partial_{i}\left(\phi^{*} g\right)_{i j}(x)-\partial_{j}\left(\phi^{*} g\right)_{i i}(x)\right) \partial_{j}\right\lrcorner d x$$
Using (14) we therefore have
$$\mathfrak{m}(M, g)=\lim _{r \rightarrow \infty} \frac{1}{2(2 m-1) \pi^{m}} \int_{S_{r} / \Gamma} \theta \wedge \omega^{m-1}$$
for a particular 1-form $\theta=A_{s}^{\mathrm{Ch}}$ with $d \theta=i F^{\mathrm{Ch}}$ on the end $M_{\infty}$. On the other hand, since $b_{1}\left(M_{\infty}\right)=0$, any other 1-form $\tilde{\theta}$ on $M_{\infty}$ with $d \tilde{\theta}=i F_{A^{\text {Ch }}}$ is given by $\tilde{\theta}=\theta+d f$ for a function $f$. Choosing a different $\theta$ would thus change the integrand by an exact form, leaving the integral on each $S_{r} / \Gamma$ completely unchanged.

Finally, the limit is independent of the asymptotic coordinate system. Notice that
$$d\left(\theta \wedge \omega^{m-1}\right)=i F_{A^{\mathrm{Ch}}} \wedge \omega^{m-1}=\frac{s+s^{*}}{4 m} \omega^{m}=\frac{(m-1)!}{4}\left(s+s^{*}\right) d \mathrm{v}_{g}$$
Thereafter if $N_{1}$ is a real hypersurface in the region $E_{r}$ exterior to $S_{r} / \Gamma$ such that $S_{r} / \Gamma$ and $N_{1}$ are the boundary components of a bounded region $V \subset E_{r}$, then
$$\begin{aligned}
& \frac{4}{(m-1)!}\left|\int_{N_{1}} \theta \wedge \omega^{m-1}-\int_{S_{r} / \Gamma} \theta \wedge \omega^{m-1}\right| \\
& =\left|\int_{V}\left(s+s^{*}\right) d \mathrm{v}_{g}\right| \\
& \leq \int_{V}\left|s+s^{*}\right| d \mathrm{v}_{g} \\
& \leq \int_{E_{r}}\left|s+s^{*}\right| d \mathrm{v}_{g} \longrightarrow 0 \text { as } r \longrightarrow \infty
\end{aligned}$$
since by hypothesis $\left(s+s^{*}\right) \in L^{1}$. \(\square\)

Proof of theorem 1.4. Choose a 1-form $\theta$ defined on $M_{\infty}$ such that
$$d \theta=i F_{A^{\mathrm{Ch}}}$$
Next choose asymptotic coordinates on $M_{\infty}$, and let $r$ be corresponding coordinate radius at infinity. Next, choose a smooth cut-off function $f: M \rightarrow[0,1]$ which vanishes identically on the compact region $M \backslash M_{\infty}$ and satisfies $f \equiv 1$ for $r \geq R_{0}$, where $R_{0}$ is a sufficiently large real number. Define
$$\xi:=i F_{A^{\mathrm{Ch}}}-d(f \theta)$$
Hence $\xi$ is a closed 2-form with compact support. Moreover, $\xi$ is cohomologous to $i F_{A^{\mathrm{ch}}}$ and hence represents the class $2 \pi \iota^{-1}\left(c_{1}\right)=\iota^{-1}\left(i F_{A^{\mathrm{Ch}}}\right)$ in the compactly supported cohomology $H_{c}^{2}(M)$.

For $\tilde{R}>R_{0}$, let $M_{\tilde{R}}$ be the compact manifold with boundary obtained by truncating $M$ at radius $\tilde{R}$, so that $\partial M_{\tilde{R}}=S_{\tilde{R}} / \Gamma$. Using the identity [8]
$$i F_{A^{\mathrm{Ch}}} \wedge \omega^{m-1}=\frac{s+s^{*}}{4 m} \omega^{m}=\frac{(m-1)!}{4}\left(s+s^{*}\right) d \mathrm{v}_{g}$$
we obtain
$$\frac{(m-1)!}{4} \int_{M_{\tilde{R}}}\left(s+s^{\star}\right) d \mathrm{v}_{g}=\int_{M_{\tilde{R}}} i F_{A^{\mathrm{Ch}}} \wedge \omega^{m-1}=\int_{M_{\tilde{R}}}(\xi+d(f \theta)) \wedge \omega^{m-1}$$

It follows that
$$\begin{aligned}
2 \pi\left\langle\iota^{-1}\left(c_{1}\right),[\omega]^{m-1}\right\rangle & =\int_{M} \xi \wedge \omega^{m-1} \\
& =\int_{M_{\tilde{R}}} \xi \wedge \omega^{m-1} \\
& =-\int_{M_{\tilde{R}}} d\left(f \theta \wedge \omega^{m-1}\right)+\frac{(m-1)!}{4} \int_{M_{\tilde{R}}}\left(s+s^{*}\right) d \mathrm{v}_{g} \\
& =-\int_{\partial M_{\tilde{R}}} f \theta \wedge \omega^{m-1}+\frac{(m-1)!}{4} \int_{M_{\tilde{R}}}\left(s+s^{*}\right) d \mathrm{v}_{g} \\
& =-\int_{S_{\tilde{R}} / \Gamma} \theta \wedge \omega^{m-1}+\frac{(m-1)!}{4} \int_{M_{\tilde{R}}}\left(s+s^{*}\right) d \mathrm{v}_{g}
\end{aligned}$$
Rearranging terms yields
$$\frac{1}{2(2 m-1) \pi^{m}} \int_{S_{\tilde{R}} / \Gamma} \theta \wedge \omega^{m-1}=-\frac{\left\langle\iota^{-1}\left(c_{1}\right),[\omega]^{m-1}\right\rangle}{(2 m-1) \pi^{m-1}}+\frac{(m-1)!}{8(2 m-1) \pi^{m}} \int_{M_{\tilde{R}}}\left(s+s^{\star}\right) d \mathrm{v}_{g}$$
Finally, taking the limit as $\tilde{R} \rightarrow \infty$ and invoking the mass formula from proposition 2.4, we obtain
$$\mathfrak{m}(M, g)=-\frac{\left\langle\iota^{-1}\left(c_{1}\right),[\omega]^{m-1}\right\rangle}{(2 m-1) \pi^{m-1}}+\frac{(m-1)!}{8(2 m-1) \pi^{m}} \int_{M}\left(s+s^{\star}\right) d \mathrm{v}_{g}$$
which completes the proof. \(\square\)

\section*{3. Positive mass theorem and Penrose inequality in dimension 4}

\subsection*{3.1. Capping off the end with LeBrun's $\boldsymbol{\Gamma}$-capsule}

The proofs of theorems 1.7-1.11 follow the strategy developed by LeBrun [19], with some modifications to account for the almost Kähler (rather than Kähler) setting. Le-Brun's strategy relies on a natural symplectic compactification of the ALE symplectic 4-manifold $(M, \omega)$, producing a closed symplectic 4-manifold $(\widehat{M}, \widehat{\omega})$ that contains $M$ as the complement of a compact symplectic domain. This construction makes it possible to invoke deep results from 4-dimensional symplectic topology. We start by defining LeBrun's $\Gamma$-capsules, which are needed to cap off the ALE symplectic manifolds $(M, \omega)$.

For any finite subgroup $\Gamma \subset U(2)(\Gamma \neq\{1\})$ that acts freely on the unit sphere $S^{3} \subset$ $\mathbb{C}^{2}$, LeBrun [19] constructed 4-dimensional compact connected symplectic orbifolds $\left(X_{\Gamma}, \omega_{\Gamma}\right)$ such that
\begin{itemize}
\item[(i)] $\left(X_{\Gamma}, \omega_{\Gamma}\right)$ contains exactly one singular point $p$.
\item[(ii)] $p$ has a neighbourhood symplectomorphic to $\left(B, \omega_{0}\right) / \Gamma$ for some standard open ball $B \subset \mathbb{C}^{2}$ centered at the origin, where $\Gamma$ acts on $\left(\mathbb{C}^{2}, \omega_{0}\right)$ in the tautological manner, as a subgroup of $U(2), \omega_{0}=d x^{1} \wedge d x^{2}+d x^{3} \wedge d x^{4}$ is the standard symplectic form $\mathbb{R}^{4}=\mathbb{C}^{2}$.
\end{itemize}
\begin{itemize}
\item[(iii)] There is a symplectic immersion $j: S^{2}$ ↪ $X_{\Gamma} \backslash\{p\}$, with at worst transverse positively oriented double points, such that
$$\int_{S^{2}} j^{*}\left[c_{1}\left(X_{\Gamma} \backslash\{p\}, J\right] \geq 3\right.$$
for some, and hence any $\omega$-compatible almost complex structure $J$.
\end{itemize}

Definition 3.1. Let $\Gamma \subset U(2)$ be any finite subgroup that acts freely on the unit sphere $S^{3} \subset \mathbb{C}^{2}$. Then
\begin{itemize}
\item[-] If $\Gamma \neq\{1\}$, a $\Gamma$-capsule will mean one of the standard symplectic orbifolds $\left(X_{\Gamma}, \omega_{\Gamma}\right)$ satisfying conditions (1)-(3) that LeBrun constructed in §2 of [19]. The unique singular point $p \in X_{\Gamma}$ will then be called the base-point of the $\Gamma$-capsule.
\item[-] When $\Gamma=\{1\}$, we instead define the associated $\Gamma$-capsule $\left(X_{\Gamma}, \omega_{\Gamma}\right)$ to be $\mathbb{C P}^{2}$, equipped with its standard Fubini-Study symplectic structure. In this case the base-point $p$ of $X_{\Gamma}$ will simply mean $[0: 0: 1] \in \mathbb{C P}^{2}$.
\end{itemize}
The next proposition constitutes the first step in the symplectic compactification procedure. Its role is to show that, under suitable decay assumptions, the asymptotic symplectic structure of an ALE almost Kähler manifold can be normalized near infinity and identified with the standard symplectic structure on $\mathbb{R}^{4}$. This normalisation is essential, as it allows one to cap off the noncompact end by a compact symplectic domain in a canonical way. Before going into the proposition, we discuss the asymptotic symplectic structure of an ALE 4-manifold.

Let $\left(M^{4}, g, J\right)$ be an ALE Kähler surface satisfying the hypothesis of theorem 1.10, i.e., it has order $\tau>1$ and as $r \longrightarrow \infty, \nabla^{\mathrm{LC}} J=O\left(r^{-\left(2+\epsilon_{2}\right)}\right)$ with $\epsilon_{2}>0$. We assume that there are $\left(x_{1}, \ldots, x_{4}\right)$ asymptotic coordinates on the universal cover $\widetilde{M}_{\infty}\left(\cong \mathbb{R}^{4} 、 \overline{B_{R}(0)}\right)$ of $M_{\infty}$ in which the components of the metric satisfy
$$g_{j k}=\delta_{j k}+O\left(r^{-\left(1+\epsilon_{1}\right)}\right), \quad\left|\partial_{l} g_{j k}\right|=O\left(r^{-\left(2+\epsilon_{1}\right)}\right)$$
for some $\epsilon_{1}>0$, and such that the fundamental group $\Gamma$ of the end acts by rotations of the coordinates $\left(x_{1}, \ldots, x_{4}\right)$ in a manner that preserves both the background model Euclidean metric $\delta$ and $g$.

Define $\epsilon:=\min \left(\epsilon_{1}, \epsilon_{2}\right)$ and let $\nabla^{\delta}$ be the Levi-Civita connection of the Euclidean metric $\delta$. Our fall-off hypothesis implies that as $r \longrightarrow \infty$,
$$\nabla^{\mathrm{LC}}=\nabla^{\delta}+\boldsymbol{\Gamma}_{i j}^{k}=\nabla^{\delta}+O\left(r^{-(2+\epsilon)}\right)$$
Since $\nabla^{\mathrm{LC}} J=O\left(r^{-\left(2+\epsilon_{2}\right)}\right), \epsilon_{2}>\epsilon>0$, we have $\nabla^{\delta} J=O\left(r^{-(2+\epsilon)}\right)$. Now we identify all the tangent spaces of $\mathbb{R}^{4}$ in the usual way, using the flat Euclidean connection $\nabla^{\delta}$. Since $\nabla^{\delta} J=O\left(r^{-(2+\epsilon)}\right)$, the value of $J$ will approach a well-defined limit $J_{0}$ along some chosen radial ray, and we then extend this limit as a constant-coefficient tensor field on our asymptotic coordinate domain. Along the chosen ray, we then have $J-J_{0}=$ $O\left(r^{-(1+\epsilon)}\right)$ and integrating along great circles in spheres of constant radius then shows that $J-J_{0}$ has $O\left(r^{-(1+\epsilon)}\right)$ fall-off everywhere. The same argument similarly also shows that the fall-off for derivative of $J: \nabla^{\delta} J$ is of the order $O\left(r^{-(2+\epsilon)}\right)$. All together we have the following: there is a $\delta$-compatible constant-coefficient almost-complex structure $J_{0}$
on $\mathbb{R}^{4}$ such that
$$J=J_{0}+O\left(r^{-(1+\epsilon)}\right), \quad \nabla^{\delta} J=O\left(r^{-(2+\epsilon)}\right)$$
Moreover after rotating our coordinates $\left(x_{1}, \cdots, x_{4}\right)$ if necessary, we may arrange $J_{0}$ to become the standard complex structure
$$d x_{1} \otimes \frac{\partial}{\partial x_{2}}-d x_{2} \otimes \frac{\partial}{\partial x_{1}}+d x_{3} \otimes \frac{\partial}{\partial x_{4}}-d x_{4} \otimes \frac{\partial}{\partial x_{3}}$$
on $\mathbb{C}^{2}=\mathbb{R}^{4}$. The argument given above is borrowed from §2 of [14].
Since the action of the fundamental group $\Gamma$ preserves both $J$ and $\delta$, it now follows that $\Gamma \subset U(2)$. More importantly, we therefore automatically obtain fall-off conditions
$$\omega=\omega_{0}+O\left(r^{-(1+\epsilon)}\right), \quad \nabla^{\delta} \omega=O\left(r^{-(2+\epsilon)}\right)$$
where $\omega_{0}=d x_{1} \wedge d x_{2}+d x_{3} \wedge d x_{4}$ is the standard symplectic form on $\mathbb{R}^{4}=\mathbb{C}^{2}$. Now we can state the proposition, which is essentially due to LeBrun [19].

Proposition 3.2. Let $(M, g, J)$ be an $A L E$ almost Kähler surface, let $\widetilde{M_{\infty}}$ be the end of the universal cover of $M_{\infty}$, the end of $M$ and let
$$\left(x_{1}, x_{2}, x_{3}, x_{4}\right): \widetilde{M_{\infty}} \rightarrow \mathbb{R}^{4} \backslash B$$
be a diffeomorphism, where $B \subset \mathbb{R}^{4}$ is a standard closed ball of some large radius centered at the origin. Moreover, suppose that these asymptotics coordinates have been chosen in accordance with the above discussion, so that the Kähler form $\omega$ satisfies the fall-off conditions (15) in this coordinate system, while the action of $\pi_{1}\left(M_{\infty}\right)$ on $\widetilde{M_{\infty}}$ by deck transformations is represented in these coordinates by the action of a finite group $\Gamma \subset U(2)$ of unitary transformations, acting on $\mathbb{R}^{4}=\mathbb{C}^{2}$ in the usual way. Then there is a $\Gamma$ equivariant $C^{2}$-diffeomorphism $\Phi: \mathbb{R}^{4} \backslash C \rightarrow \mathbb{R}^{4} \backslash D$, where $C \subset \mathbb{R}^{4}$ is a standard closed ball centered at the origin, where $D \subset \mathbb{R}^{4}$ is a smooth 4-ball whose boundary $\partial D$ is a $\Gamma$-invariant differentiable $S^{3}$, and where $B \subset C \cap D$, such that
$$\Phi^{*} \omega=\omega_{0}$$
with $|\Phi(x)-x|=O\left(r^{-\epsilon}\right)$ and $\left|\Phi_{*}-I\right|=O\left(r^{-(1+\epsilon)}\right)$.
Proof. This proposition is same as proposition 1.1 (§1) in [19], with the Kähler condition replaced by the almost Kähler assumption. LeBrun's proof of his proposition 1.1 does not rely on the integrability of $J$, but only on the fall-off conditions (15). Consequently, his argument carries over verbatim to the present setting. \(\square\)

Now we are in a position to explain the capping-off procedure to get a closed symplectic manifold $(\widehat{M}, \widehat{\omega})$ from $(M, \omega)$. This is explained in the proof of theorem 3.1 in [19]. We include it here for completeness.

Say $M_{\infty} \cong\left(S^{3} / \Gamma\right) \times \mathbb{R}^{+}$. Choose a $\Gamma$-capsule $\left(X_{\Gamma}, \omega_{\Gamma}\right)$. Proposition 3.2 tells us that the end $M_{\infty}$ contains an asymptotic region symplectomorphic to $\left(\mathbb{C}^{2} \backslash \overline{B_{\Re}}, \omega_{0}\right) / \Gamma$ for some sufficiently large common radius $\Re$. On the other hand, the base point of the $\Gamma$-capsule has a neighbourhood symplectomorphic to $\left(B_{\mathfrak{r}}, \omega_{0}\right) / \Gamma$ for some small
common radius $\mathfrak{r}$, and by shrinking the radius if necessary we can guarantee that this ball-quotient in the $\Gamma$-capsule does not meet some chosen symplectically immersed 2-sphere satisfying (iii). We now inflate the $\Gamma$-capsule by replacing the symplectic form $\omega_{\Gamma}$ by $t^{2} \omega_{\Gamma}$ for some large $t>0$. In the inflated $\Gamma$-capsule, the base point now has a neighbourhood symplectomorphic to $\left(B_{R}(0), \omega_{0}\right) / \Gamma$, where $R=t \mathfrak{r}$. Therefore by taking $t$ to be sufficiently large, we may arrange that $R>\Re$. By now removing $\overline{B_{\Re}(0)} / \Gamma \in p$ from the $\Gamma$-capsule and $\left(\mathbb{C}^{2} 、 \overline{B_{R}(0)}\right) / \Gamma$ from $M_{\infty}$, we are then left with pieces that can be glued together symplectically along copies of $\left(B_{R}(0) \backslash \overline{B_{\Re}(0)}\right) / \Gamma$ to produce a compact symplectic manifold $(\widehat{M}, \widehat{\omega})$.

\subsection*{3.2. Rescue à la McDuff-Taubes}

Now that we have obtained a closed symplectic manifold $(\widehat{M}, \widehat{\omega})$, we may invoke deep results from four-dimensional symplectic geometry due to McDuff [23] and Taubes [33]. The proofs of Theorems 1.7-1.9 are identical to their Kähler counterparts (theorem 3.1, proposition 3.3, proposition 3.4 in [19]), and we therefore refer the reader to [19] for the detailed arguments. The crucial point is that LeBrun's method relies only on the symplectic capping-off construction, rather than on the integrability of the almost-complex structure. Consequently, the argument extends to the almost Kähler setting, provided that $J$ satisfies the decay condition $\left|\nabla^{\mathrm{LC}} J\right|=O\left(r^{-\frac{\eta}{2}}\right)$ as $r \longrightarrow \infty$, for some $\eta>4$, as established above.

The proofs of theorems 1.10 and 1.11 can also be deduced from their Kähler counterparts in [19]. For the convenience of the reader, we briefly outline the main ideas in the proof of theorem 1.10 (Penrose inequality), from which theorem 1.11 (positive mass theorem) immediately follows.

Proof of theorem 1.10. As explained above, starting with an AE almost Kähler manifold ( $M, g, J$ ) with appropriate decay rate of $\nabla^{\mathrm{LC}} J$, the symplectic capping-off procedure produces a compact symplectic manifold $(\widehat{M}, \widehat{\omega})$ by removing a standard symplectic end $\left(\mathbb{R}^{4} \backslash B_{\Re}(0), \omega_{0}\right)$ and replacing it with $\mathbb{C P}^{2}$ minus a ball, equipped with some multiple of the Fubini-Study symplectic form. In this setting, a projective line in $\mathbb{C P}^{2}$ gives us a symplectic 2-sphere of self-intersection +1 in $(\widehat{M}, \widehat{\omega})$.

Invoking corollary 1.5 from 23 , we deduce that $(\widehat{M}, \widehat{\omega})$ is symplectomorphic to a blow up of $\mathbb{C P}^{2}$, equipped with some Kähler form, in a way that sends the given 2-sphere to a projective line $\mathbb{C P}^{1}$ that avoids all the blown up points. Removing this "line at infinity", we this see that $M$ must be diffeomorphic to $\mathbb{R}^{4} \# k \overline{\mathbb{C P}^{2}}$, where $k=b_{2}(M)$, and $H_{2}(M, \mathbb{Z})$ is moreover generated by the homology classes of $k$ disjoint symplectic 2-spheres $E_{1}, \ldots, E_{k} \subset M$ of self-intersection -1.

Therefore, under the natural identification $H_{c}^{2}(M)=H_{2}(M, \mathbb{R})$ arising from the Poincare duality, we have $\iota^{-1}\left(-c_{1}\right)=\sum_{j=1}\left[E_{j}\right]$, as can be checked by integrating both sides against each of the homology generators $\left[E_{j}\right]$. Thus, the mass formula (2) in the AE case gives us
$$\mathfrak{m}(M, g)=\frac{1}{3 \pi} \sum_{j=1}^{k} \int_{E_{j}} \omega+\frac{1}{12 \pi^{2}} \int_{M}\left(s+\frac{1}{4}\left|\nabla^{\mathrm{LC}} J\right|^{2}\right) d \mathrm{v}_{g}$$
The main remaining step in the proof is to show that each of the homology classes $E_{j}$ can in fact be represented by a finite sum of $J$-holomorphic curves with positive integer multiplicities. This is precisely the technical heart of the argument, and at this point
we appeal to the proof of theorem 3.5 (§3) in LeBrun [19]. The crucial observation is again that LeBrun's reasoning does not depend on the integrability of the almost-complex structure, but only on the symplectic nature of the compactification and on Taubes' "SW=Gr" 33 correspondence in the case $b_{2}^{+}=1$ [21]. Since our compactified manifold $(\widehat{M}, \widehat{\omega})$ is symplectic and satisfies $b_{2}^{+}=1$, Taubes' results apply verbatim in the almost Kähler setting.

The classes $E_{j}$ extend naturally to homology classes in $H_{2}(\widehat{M}, \mathbb{Z})$. By construction, these classes satisfy the same intersection-theoretic properties as in LeBrun's setting: they are represented by symplectic exceptional classes with negative self-intersection and positive pairing with the symplectic form.

At this stage one invokes Taubes' theorem identifying Seiberg-Witten basic classes with Gromov invariants on symplectic 4-manifolds with $b_{2}^{+}=1$. The relevant Seiberg-Witten invariants are non-trivial, and therefore each such class $E_{j}$ is represented by a (possibly singular) $J$-holomorphic curve with positive integer multiplicities. One more key point in LeBrun's proof is that one needs to do the symplectic compactification a bit more carefully than we explained above because we would want these $J$-holomorphic curves coming from Taubes' powerful machinery to exist completely inside the image of $M$ inside $\widehat{M}$. The argument uses only symplectic topology and Taubes' correspondence and not the integrability of $J$, hence it carries over unchanged to the present almost Kähler context.

Let $\mathcal{E}_{j}$ be the $J$-holomorphic curve which represents the homology class $\left[E_{j}\right]$. This means that $\int_{E_{j}} \omega$ is in fact exactly the area of $\mathcal{E}_{j}$ and our mass formula therefore can be written as
$$\mathfrak{m}(M, g)=\frac{1}{3 \pi} \sum_{j} \operatorname{vol}\left(\mathcal{E}_{j}\right)+\frac{1}{12 \pi^{2}} \int_{M}\left(s+\frac{1}{4}\left|\nabla^{\mathrm{LC}} J\right|^{2}\right) d \mathrm{v}_{g}$$
If the $D_{i}$ are the various spherical components of the various $E_{j}$, and if $n_{i}$ is the multiplicity with which a given $D_{i}$ occurs in this way, we can then rewrite this as
$$\mathfrak{m}(M, g)=\frac{1}{3 \pi} \sum_{i} n_{i} \operatorname{vol}\left(D_{i}\right)+\frac{1}{12 \pi^{2}} \int_{M}\left(s+\frac{1}{4}\left|\nabla^{\mathrm{LC}} J\right|^{2}\right) d \mathrm{v}_{g}$$
Since, $s \geq 0$, we get the Penrose-type inequality
$$\mathfrak{m}(M, g) \geq \frac{1}{3 \pi} \sum_{i} n_{i} \operatorname{vol}\left(D_{i}\right)$$
The equality case happens when $s \equiv 0, \nabla^{\mathrm{LC}} J \equiv 0$, i.e., $(M, g, J)$ is scalar-flat Kähler. \(\square\)

Proof of theorem 1.11. Theorem 1.10 implies that $\mathfrak{m}(M, g) \geq 0$. If the mass is zero, $\nabla^{\mathrm{LC}} J \equiv 0$ is forced. Hence we descend to the Kähler case and the theorem follows from its Kähler counterpart corollary 3.6 in [19]. \(\square\)

\section*{4. Rigidity results}

In the compact case, theorem 1.13 is established in 31. The order of the ALE metric and the decay property of $\left|\nabla^{\text {LC }} J\right|$ mentioned in the statement of theorem 1.13 is enough
to compensate for the non-compactness of the manifold and the same argument carries over in the ALE case considered here. The main ingredient of the proof in [31] is a remarkable integral formula found by Sekigawa. We use a version of the integral formula written in [2, 1] for our proof.

We begin with some definitions. The almost complex structure $J$ splits the space of real 2-forms into $J$-invariant and $J$-anti-invariant ones. For any real 2-form, we shall use the super-script ' to the sub-bundle of $J$-invariant 2-forms, while the super-script ${ }^{\prime \prime}$ stands for the projection to the sub-bundle of $J$-anti-invariant ones. Thus for any 2 -form $\beta \in \Omega^{2}$,
$$\beta^{\prime}(\cdot, \cdot):=\frac{1}{2}(\beta(\cdot, \cdot)+\beta(J \cdot, J \cdot)) \text { and } \beta^{\prime \prime}(\cdot, \cdot):=\frac{1}{2}(\beta(\cdot, \cdot)-\beta(J \cdot, J \cdot))$$
We denote $W^{\prime \prime}$ the component of the curvature operator defined by
$$\begin{aligned}
W_{X Y Z T}^{\prime \prime}:= & \frac{1}{8}\left(R_{X Y Z T}-R_{J X J Y Z T}-R_{X Y J Z J T}+R_{J X J Y J Z J T}\right. \\
& \left.-R_{X J Y Z J T}-R_{J X Y Z J T}-R_{X J Y J Z T}+R_{J X Y J Z T}\right)
\end{aligned}$$
We also define the twisted Ricci form to be $\rho^{*}:=R(\omega)$. The trace of $\rho^{*}, s^{*}=2 R(\omega, \omega)$ is the $*$-scalar curvature introduced before. Finally we define a 2-form $\phi$ defined by $\phi(X, Y):=\left\langle\nabla_{J X}^{\mathrm{LC}} \omega, \nabla_{Y}^{\mathrm{LC}} \omega\right\rangle$.

Lemma 4.1 (Apostolov-Drăghici-Moroianu [2], Apostolov-Drăghici [1]). Let $(M, g, J)$ be an almost Kähler Einstein manifold. The following relation holds.
$$8 \delta\left\langle\rho^{*}, \nabla^{\mathrm{LC}} \omega\right\rangle-\Delta\left|\nabla^{\mathrm{LC}} \omega\right|^{2}=8\left|W^{\prime \prime}\right|^{2}+4\left|\left(\rho^{*}\right)^{\prime \prime}\right|^{2}+\left|\left(\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}} \omega\right)^{\prime}\right|^{2}+|\phi|^{2}+\frac{s}{n}\left|\nabla^{\mathrm{LC}^{\mathrm{C}}} \omega\right|^{2}$$
$\delta$ denotes the co-differential with respect to $\nabla^{\mathrm{LC}}$.
One can find the formula stated in the lemma in this exact form in proposition 2 in [1] or in proposition 1 in 2.

Proof of theorem 1.13. We have
$$\left|\nabla^{\mathrm{LC}} \omega\right|^{2}=\frac{1}{2}\left|\nabla^{\mathrm{LC}} J\right|^{2}=s^{*}-s=2 R(\omega, \omega)-s$$
Therefore as $r \longrightarrow \infty$, we have
$$\begin{aligned}
\left|W^{\prime \prime}\right| & =O\left(r^{-(\tau+2)}\right) \\
\left|\left(\rho^{*}\right)^{\prime \prime}\right| & =O\left(r^{-(\tau+2)}\right) \\
\left|\left(\left(\nabla^{\mathrm{LC}}\right)^{*} \nabla^{\mathrm{LC}} \omega\right)^{\prime}\right| & =O(|R|)=O\left(r^{-(\tau+2)}\right) \\
\left|\nabla^{\mathrm{LC}} \omega\right|^{2} & =O(|R|)=O\left(r^{-(\tau+2)}\right) \\
|\phi| & =O\left(\left|\nabla^{\mathrm{LC}} \omega\right|^{2}\right)=O\left(r^{-(\tau+2)}\right) \\
s & =O\left(r^{-(\tau+2)}\right)
\end{aligned}$$