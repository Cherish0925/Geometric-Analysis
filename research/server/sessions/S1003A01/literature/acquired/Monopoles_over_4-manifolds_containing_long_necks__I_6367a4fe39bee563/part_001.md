---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Monopoles over 4-manifolds containing long necks, I]

---
source_file: f29f44d34606_gt-v9-n1-p01-s.pdf
converter: mathpix
format: mmd
---

Geometry \& Topology
Volume 9 (2005) 1-93
Published: 17 December 2004

\title{
Monopoles over 4-manifolds containing long necks, I
}

\author{
Kim A Frøyshov \\ Fakultät für Mathematik, Universität Bielefeld \\ Postfach 100131, D-33501 Bielefeld, Germany \\ Email: froyshov@mathematik.uni-bielefeld.de
}

\begin{abstract}
We study moduli spaces of Seiberg-Witten monopoles over spin ${ }^{c}$ Riemannian 4-manifolds with long necks and/or tubular ends. This first part discusses compactness, exponential decay, and transversality. As applications we prove two vanishing theorems for Seiberg-Witten invariants.
\end{abstract}

AMS Classification numbers Primary: 57R58
Secondary: 57R57

Keywords: Floer homology, Seiberg-Witten, Bauer-Furuta, compactness, monopoles

Proposed: Dieter Kotschick
Seconded: Simon Donaldson, Tomasz Mrowka

Received: 9 October 2003
Revised: 1 December 2004

\section*{1 Introduction}

This is the first of two papers devoted to the study of moduli spaces of Seiberg-Witten monopoles over spin ${ }^{c}$ Riemannian 4-manifolds with long necks and/or tubular ends. Our principal motivation is to provide the analytical foundations for subsequent work on Floer homology. Such homology groups should appear naturally when one attempts to express the Seiberg-Witten invariants of a closed spin ${ }^{c} 4$-manifold $Z$ cut along a hypersurface $Y$, say
$$Z=Z_{1} \cup_{Y} Z_{2},$$
in terms of relative invariants of the two pieces $Z_{1}, Z_{2}$. The standard approach, familiar from instanton Floer theory (see [13, 10]), is to construct a 1-parameter family $\left\{g_{T}\right\}$ of Riemannian metrics on $Z$ by stretching along $Y$ so as to obtain a neck $[-T, T] \times Y$, and study the monopole moduli space $M^{(T)}$ over $\left(Z, g_{T}\right)$ for large $T$. There are different aspects of this problem: compactness, transversality, and gluing. The present paper will focus particularly on compactness, and also establish transversality results sufficient for the construction of Floer homology groups of rational homology 3 -spheres. The second paper in this series will be devoted to gluing theory.
Let the monopole equations over the neck $[-T, T] \times Y$ be perturbed by a closed 2-form $\eta$ on $Y$, so that temporal gauge solutions to these equations correspond to downward gradient flow lines of the correspondingly perturbed Chern-Simons-Dirac functional $\vartheta_{\eta}$ over $Y$. Suppose all critical points of $\vartheta_{\eta}$ are non-degenerate. Because each moduli space $M^{(T)}$ is compact, one might expect, by analogy with Morse theory, that a sequence $\omega_{n} \in M^{\left(T_{n}\right)}$ where $T_{n} \rightarrow \infty$ has a subsequence which converges in a suitable sense to a pair of monopoles over the cylindrical-end manifolds associated to $Z_{1}, Z_{2}$ together with a broken gradient line of $\vartheta_{\eta}$ over $\mathbb{R} \times Y$. The first results in this direction were obtained by Kronheimer-Mrowka [21] (with $\eta=0$ ) and Morgan-Szabó-Taubes [28] (in a particular case, with $\eta$ non-exact). Nicolaescu's book [29] contains some foundational results in the case $\eta=0$. Marcolli-Wang [26] proved a general compactness theorem for $\eta$ exact. In this paper we will consider the general case when $\eta$ may be non-exact. Unfortunately, compactness as stated above may then fail. (A simple class of counter-examples is described after Theorem 1.4 below.) It is then natural to seek topological conditions which ensure that compactness does hold. We will consider two approaches which provide different sufficient conditions. In the first approach, which is a refinement of well-known techniques (see [9, 29]), one first establishes global bounds on what is morally a version of the energy functional (although the energy concept is ambiguous in the presence of perturbations) and then derives local $L^{2}$
bounds on the curvature forms. In the second approach, which appears to be new, one begins by placing the connections in Coulomb gauge with respect to a given reference connection and then obtains global bounds on the corresponding connection forms in suitably weighted Sobolev norms, utilizing the a priori pointwise bounds on the spinors.

The paper also contains expository sections on configuration spaces and exponential decay, borrowing some ideas from Donaldson [10], to which we also refer for the Fredholm theory. In the transversality theory of moduli spaces we mostly restrict ourselves, for the time being, to the case when all ends of the 4-manifold in question are modelled on rational homology spheres. The perturbations used here are minor modifications of the ones introduced in [15]. It is not clear to us that these perturbations immediately carry over to the case of more general ends, as has apparently been assumed by some authors, although we expect that a modified version may be shown to work with the aid of gluing theory.

In most of this paper we make an assumption on the cohomology class of $\eta$ which rules out the hardest case in the construction of Floer homology (see Subsection 1.2). This has the advantage that we can use relatively simple perturbations. A comprehensive monopole Floer theory including the hardest case is expected to appear in a forthcoming book by Kronheimer-Mrowka [20]. An outline of their construction (and much more) can be found in [22].

A large part of this work was carried out during a one-year stay at the Institut des Hautes Études Scientifiques, and the author is grateful for the hospitality and excellent research environment which he enjoyed there. This work was also supported by a grant from the National Science Foundation.

\subsection*{1.1 Vanishing results for Seiberg-Witten invariants}

Before describing our compactness results in more detail we will mention two applications to Seiberg-Witten invariants of closed 4-manifolds.

By a spin ${ }^{c}$ manifold we shall mean an oriented smooth manifold with a spin ${ }^{c}$ structure. If $Z$ is a spin ${ }^{c}$ manifold then $-Z$ will refer to the same smooth manifold equipped with the opposite orientation and the corresponding spin ${ }^{c}$ structure.

If $Z$ is a closed, oriented 4 -manifold then by an homology orientation of $Z$ we mean an orientation of the real vector space $H^{0}(Z)^{*} \oplus H^{1}(Z) \oplus H^{+}(Z)^{*}$, where
$H^{+}(Z)$ is any maximal positive subspace for the intersection form on $H^{2}(Z)$. The dimension of $H^{+}$is denoted $b_{2}^{+}$.
In [7] Bauer and Furuta introduced a refined Seiberg-Witten invariant for closed spin ${ }^{c} 4$-manifolds $Z$. This invariant $\widetilde{\mathrm{SW}}(Z)$ lives in a certain equivariant stable cohomotopy group. If $Z$ is connected and $b_{2}^{+}(Z)>1$, and given an homology orientation of $Z$, then according to [6] there is a natural homomorphism from this stable cohomotopy group to $\mathbb{Z}$ which maps $\widetilde{\mathrm{SW}}(Z)$ to the ordinary Seiberg-Witten invariant $\operatorname{SW}(Z)$ defined by the homology orientation. In [5] Bauer showed that, unlike the ordinary Seiberg-Witten invariant, the refined invariant does not in general vanish for connected sums where both summands have $b_{2}^{+}>0$. However, $\widetilde{\mathrm{SW}}(Z)=0$ provided there exists a metric and perturbation 2-form on $Z$ for which the Seiberg-Witten moduli space $M_{Z}$ is empty (see 6, Remark 2.2] and [18, Proposition 6]).

Theorem 1.1 Let $Z$ be a closed spin ${ }^{c}$ 4-manifold and $Y \subset Z$ a closed, orientable 3-dimensional submanifold. Suppose
\begin{itemize}
\item[(i)] $Y$ admits a Riemannian metric with positive scalar curvature, and
\item[(ii)] $H^{2}(Z ; \mathbb{Q}) \rightarrow H^{2}(Y ; \mathbb{Q})$ is non-zero.
\end{itemize}

Then there exists a metric and perturbation 2-form on $Z$ for which $M_{Z}$ is empty, hence $\widetilde{S W}(Z)=0$.

This generalizes a result of Fintushel-Stern [12] and Morgan-Szabó-Taubes [28] which concerns the special case when $Y \approx S^{1} \times S^{2}$ is the link of an embedded 2-sphere of self-intersection 0. One can derive Theorem 1.1 from Nicolaescu's proof [29] of their result and the classification of closed orientable 3-manifolds admitting positive scalar curvature metrics (see [23, p 325]). However, we shall give a direct (and much simpler) proof where the main idea is to perturb the monopole equations on $Z$ by a suitable 2-form such that the corresponding perturbed Chern-Simons-Dirac functional on $Y$ has no critical points. One then introduces a long neck $[-T, T] \times Y$. See Section 9 for details.
We now turn to another application, for which we need a little preparation. For any compact spin ${ }^{c}$ 4-manifold $Z$ whose boundary is a disjoint union of rational homology spheres set
$$d(Z)=\frac{1}{4}\left(c_{1}\left(\mathcal{L}_{Z}\right)^{2}-\sigma(Z)\right)+b_{1}(Z)-b_{2}^{+}(Z) .$$
Here $\mathcal{L}_{Z}$ is the determinant line bundle of the spin ${ }^{c}$ structure, and $\sigma(Z)$ the signature of $Z$. If $Z$ is closed then the moduli space $M_{Z}$ has expected dimension $d(Z)-b_{0}(Z)$.

In [14] we will assign to every spin ${ }^{c}$ rational homology 3-sphere $Y$ a rational number $h(Y)$. (A preliminary version of this invariant was introduced in [15].) In Section 9 of the present paper this invariant will be defined in the case when $Y$ admits a metric with positive scalar curvature. It satisfies $h(-Y)=-h(Y)$. In particular, $h\left(S^{3}\right)=0$.

Theorem 1.2 Let $Z$ be a closed, connected spin ${ }^{c}$ 4-manifold, and let $W \subset Z$ be a compact, connected, codimension 0 submanifold whose boundary is a disjoint union of rational homology spheres $Y_{1}, \ldots, Y_{r}, r \geq 1$, each of which admits a metric of positive scalar curvature. Suppose $b_{2}^{+}(W)>0$ and set $W^{c}=Z \backslash \operatorname{int} W$. Let each $Y_{j}$ have the orientation and spin ${ }^{c}$ structure inherited from $W$. Then the following hold:
\begin{itemize}
\item[(i)] If $2 \sum_{j} h\left(Y_{j}\right) \leq-d(W)$ then there exists a metric and perturbation 2- form on $Z$ for which $M_{Z}$ is empty, hence $\widetilde{S W}(Z)=0$.
\item[(ii)] If $b_{2}^{+}(Z)>1$ and $2 \sum_{j} h\left(Y_{j}\right)<d\left(W^{c}\right)$ then $S W(Z)=0$.
\end{itemize}

Note that (ii) generalizes the classical theorem (see [30, 29]) which says that $\operatorname{SW}(Z)=0$ if $Z$ is a connected sum where both sides have $b_{2}^{+}>0$.

\subsection*{1.2 The Chern-Simons-Dirac functional}

Let $Y$ be a closed, connected Riemannian spin ${ }^{c} 3$-manifold. We consider the Seiberg-Witten monopole equations over $\mathbb{R} \times Y$, perturbed by adding a 2 -form to the curvature part of these equations. This 2-form should be the pull-back of a closed form $\eta$ on $Y$. Recall from [21, 28] that in temporal gauge these perturbed monopole equations can be described as the downward gradient flow equation for a perturbed Chern-Simons-Dirac functional, which we will denote by $\vartheta_{\eta}$, or just $\vartheta$ when no confusion can arise.

For transversality reasons we will add a further small perturbation to the monopole equations over $\mathbb{R} \times Y$, similar to those introduced in [15, Section 2]. This perturbation depends on a parameter $\mathfrak{p}$ (see Subsection 3.3). When $\mathfrak{p} \neq 0$ then the perturbed monopole equations are no longer of gradient flow type. Therefore, $\mathfrak{p}$ has to be kept small in order for the perturbed equations to retain certain properties (see Subsection 4.2).

If $S$ is a configuration over $Y$ (ie a spin connection together with a section of the spin bundle) and $u: Y \rightarrow \mathrm{U}(1)$ then
$$\vartheta(u(S))-\vartheta(S)=2 \pi \int_{Y} \widetilde{\eta} \wedge[u],$$
where $[u] \in H^{1}(Y)$ is the pull-back by $u$ of the fundamental class of U(1), and
$$\widetilde{\eta}=\pi c_{1}\left(\mathcal{L}_{Y}\right)-[\eta] \in H^{2}(Y) .$$
Here $\mathcal{L}_{Y}$ is the determinant line bundle of the spin ${ }^{c}$ structure of $Y$.
Let $\mathcal{R}_{Y}$ be the space of (smooth) monopoles over $Y$ (ie critical points of $\vartheta$ ) modulo all gauge transformations $Y \rightarrow \mathrm{U}(1)$, and $\widetilde{\mathcal{R}}_{Y}$ the space of monopoles over $Y$ modulo null-homotopic gauge transformations.

When no statement is made to the contrary, we will always make the following two assumptions:
\begin{itemize}
\item[(O1)] $\tilde{\eta}$ is a real multiple of some rational cohomology class.
\item[(O2)] All critical points of $\vartheta$ are non-degenerate.
\end{itemize}

The second assumption implies that $\mathcal{R}_{Y}$ is a finite set. This rules out the case when $\widetilde{\eta}=0$ and $b_{1}(Y)>0$, because if $\widetilde{\eta}=0$ then the subspace of reducible points in $\mathcal{R}_{Y}$ is homeomorphic to a $b_{1}(Y)$-dimensional torus. If $\widetilde{\eta} \neq 0$ or $b_{1}(Y)=0$ then the non-degeneracy condition can be achieved by perturbing $\eta$ by an exact form (see Proposition 8.1).

For any $\alpha, \beta \in \widetilde{\mathcal{R}}_{Y}$ let $M(\alpha, \beta)$ denote the moduli space of monopoles over $\mathbb{R} \times Y$ that are asymptotic to $\alpha$ and $\beta$ at $-\infty$ and $\infty$, respectively. Set $\check{M}=M / \mathbb{R}$. By a broken gradient line from $\alpha$ to $\beta$ we mean a sequence $\left(\omega_{1}, \ldots, \omega_{k}\right)$ where $k \geq 0$ and $\omega_{j} \in \check{M}\left(\alpha_{j-1}, \alpha_{j}\right)$ for some $\alpha_{0}, \ldots, \alpha_{k} \in \widetilde{\mathcal{R}}_{Y}$ with $\alpha_{0}=\alpha, \alpha_{k}=\beta$, and $\alpha_{j-1} \neq \alpha_{j}$ for each $j$. If $\alpha=\beta$ then we allow the empty broken gradient line (with $k=0$ ).

\subsection*{1.3 Compactness}

Let $X$ be a spin ${ }^{c}$ Riemannian 4-manifold with tubular ends $\overline{\mathbb{R}}_{+} \times Y_{j}, j=$ $1, \ldots, r$, where $r \geq 0$ and each $Y_{j}$ is a closed, connected Riemannian spin ${ }^{c}$ 3-manifold. Setting $Y=\cup_{j} Y_{j}$ this means that we are given
\begin{itemize}
\item[-] an orientation preserving isometric embedding $\iota: \overline{\mathbb{R}}_{+} \times Y \rightarrow X$ such that
$$X_{: t}=X \backslash \iota((t, \infty) \times Y)$$
is compact for any $t \geq 0$,
\item[-] an isomorphism between the spin ${ }^{c}$ structure on $\overline{\mathbb{R}}_{+} \times Y$ induced from $Y$ and the one inherited from $X$ via the embedding $\iota$.
\end{itemize}

Here $\mathbb{R}_{+}$is the set of positive real numbers and $\overline{\mathbb{R}}_{+}=\mathbb{R}_{+} \cup\{0\}$. Usually we will just regard $\overline{\mathbb{R}}_{+} \times Y$ as a (closed) submanifold of $X$.

Let $\eta_{j}$ be a closed 2-form on $Y_{j}$ and define $\widetilde{\eta}_{j} \in H^{2}\left(Y_{j}\right)$ in terms of $\eta_{j}$ as in (2). We write $\vartheta$ instead of $\vartheta_{\eta_{j}}$ when no confusion is likely to arise. We perturb the curvature part of the monopole equations over $X$ by adding a 2 -form $\mu$ whose restriction to $\mathbb{R}_{+} \times Y_{j}$ agrees with the pull-back of $\eta_{j}$. In addition we perturb the equations over $\mathbb{R} \times Y_{j}$ and the corresponding end of $X$ using a perturbation parameter $\mathfrak{p}_{j}$. If $\vec{\alpha}=\left(\alpha_{1}, \ldots, \alpha_{r}\right)$ with $\alpha_{j} \in \widetilde{\mathcal{R}}_{Y_{j}}$ let $M(X ; \vec{\alpha})$ denote the moduli space of monopoles over $X$ that are asymptotic to $\alpha_{j}$ over $\mathbb{R}_{+} \times Y_{j}$.

Let $\lambda_{1}, \ldots, \lambda_{r}$ be positive constants. We consider the following two equivalent conditions on the spin ${ }^{c}$ manifold $X$ and $\widetilde{\eta}_{j}, \lambda_{j}$ :
\begin{itemize}
\item[(A)] There exists a class $\widetilde{z} \in H^{2}(X ; \mathbb{R})$ such that $\left.\widetilde{z}\right|_{Y_{j}}=\lambda_{j} \widetilde{\eta}_{j}$ for $j=1, \ldots, r$.
\item[] (A') For configurations $S$ over $X_{: 0}$ the sum $\sum_{j} \lambda_{j} \vartheta\left(\left.S\right|_{\{0\} \times Y_{j}}\right)$ depends only on the gauge equivalence class of $S$.
\end{itemize}

Note that if $\lambda_{j}=1$ for all $j$ then (A) holds precisely when there exists a class $z \in H^{2}(X ; \mathbb{R})$ such that $\left.z\right|_{Y_{j}}=\left[\eta_{j}\right]$ for $j=1, \ldots, r$.

Theorem 1.3 If Condition (A) is satisfied and each $\mathfrak{p}_{j}$ has sufficiently small $C^{1}$ norm then the following holds. For $n=1,2, \ldots$ let $\omega_{n} \in M\left(X ; \vec{\alpha}_{n}\right)$, where $\vec{\alpha}_{n}=\left(\alpha_{n, 1}, \ldots, \alpha_{n, r}\right)$. If
$$\inf _{n} \sum_{j=1}^{r} \lambda_{j} \vartheta\left(\alpha_{n, j}\right)>-\infty$$
then there exists a subsequence of $\omega_{n}$ which chain-converges to an ( $r+1$ )-tuple $\left(\omega, \vec{v}_{1}, \ldots, \vec{v}_{r}\right)$ where $\omega$ is an element of some moduli space $M(X ; \vec{\beta})$ and $\vec{v}_{j}$ is a broken gradient line over $\mathbb{R} \times Y_{j}$ from $\beta_{j}$ to some $\gamma_{j} \in \widetilde{\mathcal{R}}_{Y_{j}}$. Moreover, if $\omega_{n}$ chain-converges to $\left(\omega, \vec{v}_{1}, \ldots, \vec{v}_{r}\right)$ then for sufficiently large $n$ there is a gauge transformation $u_{n}: X \rightarrow U(1)$ which is translationary invariant over the ends and maps $M\left(X ; \vec{\alpha}_{n}\right)$ to $M(X ; \vec{\gamma})$

The assumption (4) imposes an "energy bound" over the ends of $X$, as we will show in Subsection 7.2 The notion of chain-convergence is defined in Subsection 7.1 The limit, if it exists, is unique up to gauge equivalence (see Proposition 7.2 below).

\subsection*{1.4 Compactness and neck-stretching}

In this subsection cohomology groups will have real coefficients.
We consider again a spin ${ }^{c}$ Riemannian 4-manifold $X$ as in the previous subsection, but we now assume that the ends of $X$ are given by orientation preserving isometric embeddings
$$\begin{aligned}
\iota_{j}^{\prime}: \overline{\mathbb{R}}_{+} \times Y_{j}^{\prime} \rightarrow X, & j=1, \ldots, r^{\prime}, \\
\iota_{j}^{ \pm}: \overline{\mathbb{R}}_{+} \times\left( \pm Y_{j}\right) \rightarrow X, & j=1, \ldots, r,
\end{aligned}$$
where $r, r^{\prime} \geq 0$. Here each $Y_{j}^{\prime}, Y_{j}$ should be a closed, connected spin ${ }^{c}$ Riemannian 3-manifold, and as before there should be the appropriate identifications of spin ${ }^{c}$ structures. For every $T=\left(T_{1}, \ldots, T_{r}\right)$ with $T_{j}>0$ for each $j$, let $X^{(T)}$ denote the manifold obtained from $X$ by gluing, for $j=1, \ldots, r$, the two ends $\iota_{j}^{ \pm}\left(\overline{\mathbb{R}}_{+} \times Y_{j}\right)$ to form a neck $\left[-T_{j}, T_{j}\right] \times Y_{j}$. To be precise, let $X^{\{T\}} \subset X$ be the result of deleting from $X$ the sets $\iota_{j}^{ \pm}\left(\left[2 T_{j}, \infty\right) \times Y_{j}\right), j=1, \ldots, r$. Set
$$X^{(T)}=X^{\{T\}} / \sim,$$
where we identify
$$\iota_{j}^{+}(t, y) \sim \iota_{j}^{-}\left(2 T_{j}-t, y\right)$$
for all $(t, y) \in\left(0,2 T_{j}\right) \times Y_{j}$ and $j=1, \ldots, r$. We regard $\left[-T_{j}, T_{j}\right] \times Y_{j}$ as a submanifold of $X^{(T)}$ by means of the isometric embedding $(t, y) \mapsto \pi_{T} \iota_{j}^{+}(t+$ $T_{j}, y$ ), where $\pi_{T}: X^{\{T\}} \rightarrow X^{(T)}$. Also, we write $\mathbb{R}_{+} \times\left( \pm Y_{j}\right)$ instead of $\iota_{j}^{ \pm}\left(\mathbb{R}_{+} \times\right.$ $Y_{j}$ ), and similarly for $\mathbb{R}_{+} \times Y_{j}^{\prime}$, if this is not likely to cause any confusion.

Set $X^{\#}=X^{(T)}$ with $T_{j}=1$ for all $j$. The process of constructing $X^{\#}$ from $X$ (as smooth manifolds) can be described by the unoriented graph $\gamma$ which has one node for every connected component of $X$ and, for each $j=1, \ldots, r$, one edge representing the pair of embeddings $\iota_{j}^{ \pm}$.

A node in an oriented graph is called a source if it has no incoming edges. If $e$ is any node in $\gamma$ let $X_{e}$ denote the corresponding component of $X$. Let $Z_{e}=\left(X_{e}\right)_{: 1}$ be the corresponding truncated manifold as in (3). Let $\gamma \backslash e$ be the graph obtained from $\gamma$ by deleting the node $e$ and all edges of which $e$ is a boundary point. Given an orientation $o$ of $\gamma$ let $\partial^{-} Z_{e}$ denote the union of all boundary components of $Z_{e}$ corresponding to incoming edges of $(\gamma, o)$. Let $F_{e}$ be the kernel of $H^{1}\left(Z_{e}\right) \rightarrow H^{1}\left(\partial^{-} Z_{e}\right)$, and set
$$\Sigma(X, \gamma, o)=\operatorname{dim} H^{1}\left(X^{\#}\right)-\sum_{e} \operatorname{dim} F_{e} .$$

It will follow from Lemma 5.3 below that $\Sigma(X, \gamma, o) \leq 0$ if each connected component of $\gamma$ is simply-connected.

We will now state a condition on $(X, \gamma)$ which is recursive with respect to the number of nodes of $\gamma$.
\begin{itemize}
\item[(C)] If $\gamma$ has more than one node then it should admit an orientation $o$ such that the following two conditions hold:
\begin{itemize}
\item[-] $\Sigma(X, \gamma, o)=0$,
\item[-] Condition (C) holds for $\left(X \backslash X_{e}, \gamma \backslash e\right)$ for all sources $e$ of $(\gamma, o)$.
\end{itemize}
\end{itemize}
We are only interested in this condition when each component of $\gamma$ is simplyconnected. If $\gamma$ is connected and has exactly two nodes $e_{1}, e_{2}$ then (C) holds if and only if $H^{1}\left(X^{\#}\right) \rightarrow H^{1}\left(Z_{e_{j}}\right)$ is surjective for at least one value of $j$, as is easily seen from the Mayer-Vietoris sequence. See Subsection 5.3 and the proof of Proposition 5.6 for more information about Condition (C).

Let the Chern-Simons-Dirac functionals on $Y_{j}, Y_{j}^{\prime}$ be defined in terms of closed 2-forms $\eta_{j}, \eta_{j}^{\prime}$ respectively. Let $\widetilde{\eta}_{j}$ and $\widetilde{\eta}_{j}^{\prime}$ be the corresponding classes as in (2). Let $\lambda_{1}, \ldots, \lambda_{r}$ and $\lambda_{1}^{\prime}, \ldots, \lambda_{r^{\prime}}^{\prime}$ be positive constants. The following conditions on $X, \widetilde{\eta}_{j}, \widetilde{\eta}_{j}^{\prime}, \lambda_{j}, \lambda_{j}^{\prime}$ will appear in Theorem 1.4 below.
\begin{itemize}
\item[(B1)] There exists a class in $H^{2}\left(X^{\#}\right)$ whose restrictions to $Y_{j}$ and $Y_{j}^{\prime}$ are $\left[\eta_{j}\right]$ and $\left[\eta_{j}^{\prime}\right]$, respectively, and all the constants $\lambda_{j}, \lambda_{j}^{\prime}$ are equal to 1 .
\item[(B2)] There exists a class in $H^{2}\left(X^{\#}\right)$ whose restrictions to $Y_{j}$ and $Y_{j}^{\prime}$ are $\lambda_{j} \widetilde{\eta}_{j}$ and $\lambda_{j}^{\prime} \widetilde{\eta}_{j}^{\prime}$, respectively. Moreover, the graph $\gamma$ is simply-connected, and Condition (C) holds for $(X, \gamma)$.
\end{itemize}

Choose a 2-form $\mu$ on $X$ whose restriction to each end $\mathbb{R}_{+} \times\left( \pm Y_{j}\right)$ is the pull-back of $\eta_{j}$, and whose restriction to $\mathbb{R}_{+} \times Y_{j}^{\prime}$ is the pull-back of $\eta_{j}^{\prime}$. Such a form $\mu$ gives rise, in a canonical way, to a form $\mu^{(T)}$ on $X^{(T)}$. We use the forms $\mu, \mu^{(T)}$ to perturb the curvature part of the monopole equations over $X$, $X^{(T)}$, respectively. We use the perturbation parameter $\mathfrak{p}_{j}^{\prime}$ over $\mathbb{R} \times Y_{j}^{\prime}$ and the corresponding ends, and $\mathfrak{p}_{j}$ over $\mathbb{R} \times Y_{j}$ and the corresponding ends and necks.

Moduli spaces over $X$ will be denoted $M\left(X ; \vec{\alpha}_{+}, \vec{\alpha}_{-}, \vec{\alpha}^{\prime}\right)$, where the $j$ 'th component of $\vec{\alpha}_{ \pm}$specifies the limit over the end $\mathbb{R}_{+} \times\left( \pm Y_{j}\right)$ and the $j$ 'th component of $\vec{\alpha}^{\prime}$ specifies the limit over $\mathbb{R}_{+} \times Y_{j}^{\prime}$.

Theorem 1.4 Suppose at least one of the conditions (B1), (B2) holds, and for $n=1,2, \ldots$ let $\omega_{n} \in M\left(X^{(T(n))} ; \vec{\alpha}_{n}^{\prime}\right)$, where $\vec{\alpha}_{n}^{\prime}=\left(\alpha_{n, 1}^{\prime}, \ldots, \alpha_{n, r^{\prime}}^{\prime}\right)$ and
$T_{j}(n) \rightarrow \infty$ for $j=1, \ldots, r$. Suppose also that the perturbation parameters $\mathfrak{p}_{j}, \mathfrak{p}_{j}^{\prime}$ are admissible for each $\vec{\alpha}_{n}^{\prime}$, and that
$$\inf _{n} \sum_{j=1}^{r^{\prime}} \lambda_{j}^{\prime} \vartheta\left(\alpha_{n, j}^{\prime}\right)>-\infty .$$
Then there exists a subsequence of $\omega_{n}$ which chain-converges to an ( $r+r^{\prime}+1$ )- tuple $\mathbb{V}=\left(\omega, \vec{v}_{1}, \ldots, \vec{v}_{r}, \vec{v}_{1}^{\prime}, \ldots, \vec{v}_{r^{\prime}}^{\prime}\right)$, where
\begin{itemize}
\item[-] $\omega$ is an element of some moduli space $M\left(X ; \vec{\alpha}_{1}, \vec{\alpha}_{2}, \vec{\beta}^{\prime}\right)$,
\item[-] $\vec{v}_{j}$ is a broken gradient line over $\mathbb{R} \times Y_{j}$ from $\alpha_{1 j}$ to $\alpha_{2 j}$,
\item[-] $\vec{v}_{j}^{\prime}$ is a broken gradient line over $\mathbb{R} \times Y_{j}^{\prime}$ from $\beta_{j}^{\prime}$ to some $\gamma_{j}^{\prime} \in \widetilde{\mathcal{R}}_{Y_{j}^{\prime}}$.
\end{itemize}
Moreover, if $\omega_{n}$ chain-converges to $\mathbb{V}$ then for sufficiently large $n$ there is a gauge transformation $u_{n}: X^{(T(n))} \rightarrow U(1)$ which is translationary invariant over the ends and maps $M\left(X^{(T(n))} ; \vec{\alpha}_{n}^{\prime}\right)$ to $M\left(X^{(T(n))} ; \vec{\gamma}^{\prime}\right)$.

The notion of chain-convergence is defined in Subsection 7.1 Note that the chain-limit is unique only up to gauge equivalence, see Proposition 7.2

What it means for the perturbation parameters $\mathfrak{p}_{j}, \mathfrak{p}_{j}^{\prime}$ to be "admissible" is defined in Definition 7.3 As in Theorem 1.3, if (B2) holds and the perturbation parameters have sufficiently small $C^{1}$ norm then they are admissible for any $\vec{a}^{\prime}$, see Proposition 5.6. If (B1) is satisfied but perhaps not (B2) then for any $C_{1}<\infty$ there is a $C_{2}>0$ such that if the perturbation parameters have $C^{1}$ norm $<C_{2}$ then they are admissible for all $\vec{\alpha}^{\prime}$ satisfying $\sum_{j=1}^{r^{\prime}} \lambda_{j}^{\prime} \vartheta\left(\alpha_{j}^{\prime}\right)>-C_{1}$, see the remarks after Proposition 4.5.

The conditions (B1), (B2) in the theorem correspond to the two approaches to compactness referred to at the beginning of this introduction: If (B1) is satisfied then one can take the "energy approach", whereas if (B2) holds one can use the "Hodge theory approach"

The conclusion of the theorem does not hold in general when neither (B1) nor (B2) are satisfied. For in that case Theorem 1.1 would hold if instead of (ii) one merely assumed that $b_{1}(Y)>0$. Since $\mathbb{R}^{4}$ contains an embedded $S^{1} \times S^{2}$ this would contradict the fact that there are many spin ${ }^{c}$ 4-manifolds with $b_{2}^{+}>1$ and non-zero Seiberg-Witten invariant.

For the moment we will abuse language and say that (B2) holds if it holds for some choice of constants $\lambda_{j}, \lambda_{j}^{\prime}$, and similarly for (B1). Then a simple example where (B1) is satisfied but not (B2) is $X=\mathbb{R} \times Y$, where one glues the two
ends to obtain $X^{(T)}=(\mathbb{R} / 2 T \mathbb{Z}) \times Y$. There are also many examples where (B2) is satisfied but not (B1). For instance, consider the case when $X$ consists of two copies of $\mathbb{R} \times Y$, say $X=\mathbb{R} \times Y \times\{1,2\}$ with $Y$ connected, and one glues $\mathbb{R}_{+} \times Y \times\{1\}$ with $\mathbb{R}_{-} \times Y \times\{2\}$. In this case $r=1$ and $r^{\prime}=2$, so we are given closed 2-forms $\eta_{1}, \eta_{1}^{\prime}, \eta_{2}^{\prime}$ on $Y$. Condition (B1) now requires that these three 2 -forms represent the same cohomology class, while (B2) holds as long as there are $a_{1}, a_{2}>0$ such that $\left[\eta_{1}\right]=a_{1}\left[\eta_{1}^{\prime}\right]=a_{2}\left[\eta_{2}^{\prime}\right]$.

\subsection*{1.5 Outline}

Here is an outline of the content of the remainder of this paper. In Section 2 we study orbit spaces of configurations over Riemannian $n$-manifolds with tubular ends. This includes results on the Laplacians on such manifolds, which are also applied later in Subsection 5.1 to the study of the $d^{*}+d^{+}$operator in the case $n=4$. Section 3 introduces monopoles, perturbations, and moduli spaces. Section 4 establishes local compactness results for monopoles, and technical results on perturbations. In Section 5 the Hodge theory approach to local compactness is presented, which is an alternative to the energy approach of Subsection 4.3. Section 6 is devoted to exponential decay, which is needed for the global compactness results in Section 7, where Theorems 1.3 and 1.4 are proved. Section 8 discusses non-degeneracy of critical points and regularity of moduli spaces. Finally, in Section 9 we prove Theorems 1.1 and 1.2. There are also two appendices. The first of these explains how to patch together sequences of local gauge transformations (an improvement of Uhlenbeck's technique). The second appendix contains a quantitative inverse function theorem which is used in the proof of exponential decay.

\section*{2 Configuration spaces}

\subsection*{2.1 Configurations and gauge transformations}

Let $X$ be a Riemannian $n$-manifold with tubular ends $\overline{\mathbb{R}}_{+} \times Y_{j}, j=1, \ldots, r$, where $n \geq 1, r \geq 0$, and each $Y_{j}$ is a closed, connected Riemannian $(n-1)-$ manifold. This means that we are given for each $j$ an isometric embedding
$$\iota_{j}: \overline{\mathbb{R}}_{+} \times Y_{j} \rightarrow X ;$$
moreover, the images of these embeddings are disjoint and their union have precompact complement. Usually we will just regard $\overline{\mathbb{R}}_{+} \times Y_{j}$ as a submanifold
of $X$. Set $Y=\cup_{j} Y_{j}$ and, for $t \geq 0$,
$$X_{: t}=X \backslash(t, \infty) \times Y .$$
Let $\mathbb{S} \rightarrow X$ and $\mathbb{S}_{j} \rightarrow Y_{j}$ be Hermitian complex vector bundles, and $L \rightarrow$ $X$ and $L_{j} \rightarrow Y_{j}$ principal U(1)-bundles. Suppose we are given, for each $j$, isomorphisms
$$\iota_{j}^{*} \mathbb{S} \stackrel{\approx}{\rightarrow} \overline{\mathbb{R}}_{+} \times \mathbb{S}_{j}, \quad \iota_{j}^{*} L \xrightarrow{\approx} \overline{\mathbb{R}}_{+} \times L_{j} .$$
By a configuration in $(L, \mathbb{S})$ we shall mean a pair $(A, \Phi)$ where $A$ is a connection in $L$ and $\Phi$ a section of $\mathbb{S}$. Maps $u: X \rightarrow \mathrm{U}(1)$ are referred to as gauge transformations and these act on configurations in the natural way:
$$u(A, \Phi)=(u(A), u \Phi) .$$
The main goal of this section is to prove a "local slice" theorem for certain orbit spaces of configurations modulo gauge transformations.

We begin by setting up suitable function spaces. For $p \geq 1$ and any non-negative integer $m$ let $L_{m}^{p}(X)$ be the completion of the space of compactly supported smooth functions on $X$ with respect to the norm
$$\|f\|_{m, p}=\|f\|_{L_{m}^{p}}=\left(\sum_{k=0}^{m} \int_{X}\left|\nabla^{k} f\right|^{p}\right)^{1 / p} .$$
Here the covariant derivative is computed using some fixed connection in the tangent bundle $T X$ which is translationary invariant over each end. Define the Sobolev space $L_{k}^{p}(X ; \mathbb{S})$ of sections of $\mathbb{S}$ similarly.
We also need weighted Sobolev spaces. For any smooth function $w: X \rightarrow \mathbb{R}$ set $L_{m}^{p, w}(X)=e^{-w} L_{m}^{p}(X)$ and
$$\|f\|_{L_{k}^{p, w}}=\left\|e^{w} f\right\|_{L_{k}^{p}} .$$
In practice we require that $w$ have a specific form over the ends, namely
$$w \circ \iota_{j}(t, y)=\sigma_{j} t,$$
where the $\sigma_{j}$ 's are real numbers.
The following Sobolev embeddings (which hold in $\mathbb{R}^{n}$, hence over $X$ ) will be used repeatedly:
$$\begin{gathered}
L_{m+1}^{p} \subset L_{m}^{2 p} \quad \text { if } p \geq n / 2, m \geq 0, \\
L_{2}^{p} \subset C_{B}^{0} \quad \text { if } p>n / 2 .
\end{gathered}$$
Here $C_{B}^{0}$ denotes the Banach space of bounded continuous functions, with the supremum norm. Moreover, if $p m>n$ then multiplication defines a continuous map $L_{m}^{p} \times L_{k}^{p} \rightarrow L_{k}^{p}$ for $0 \leq k \leq m$.

For the remainder of this section fix $p>n / 2$. Note that this implies $L_{1}^{p} \subset L^{2}$ over compact $n$-manifolds.

We will now define an affine space $\mathcal{C}$ of $L_{1, \text { loc }}^{p}$ configurations in $(L, \mathbb{S})$. Let $A_{o}$ be a smooth connection in $L$. Choose a smooth section $\Phi_{o}$ of $\mathbb{S}$ whose restriction to $\mathbb{R}_{+} \times Y_{j}$ is the pull-back of a section $\psi_{j}$ of $\mathbb{S}_{j}$. Suppose $\psi_{j}=0$ for $j \leq r_{0}$, and $\psi_{j} \not \equiv 0$ for $j>r_{0}$, where $r_{0}$ is a non-negative integer. Fix a weight function $w$ as above with $\sigma_{j} \geq 0$ small for all $j$, and $\sigma_{j}>0$ for $j \leq r_{0}$. Set
$$\mathcal{C}=\left\{\left(A_{o}+a, \Phi_{o}+\phi\right): a, \phi \in L_{1}^{p, w}\right\} .$$
We topologize $\mathcal{C}$ using the $L_{1}^{p, w}$ metric.
We wish to define a Banach Lie group $\mathcal{G}$ of $L_{2, \text { loc }}^{p}$ gauge transformations over $X$ such that $\mathcal{G}$ acts smoothly on $\mathcal{C}$ and such that if $S, S^{\prime} \in \mathcal{C}$ and $u(S)=S^{\prime}$ for some $L_{2, \text { loc }}^{p}$ gauge transformations $u$ then $u \in \mathcal{G}$. If $u \in \mathcal{G}$ then we must certainly have
$$\left(-u^{-1} d u,(u-1) \Phi_{o}\right)=u\left(A_{o}, \Phi_{o}\right)-\left(A_{o}, \Phi_{o}\right) \in L_{1}^{p, w} .$$
Now
$$\|d u\|_{L_{1}^{p, w}} \leq \mathrm{const} \cdot\left(\left\|u^{-1} d u\right\|_{L_{1}^{p, w}}+\left\|u^{-1} d u\right\|_{L_{1}^{p, w}}^{2}\right),$$
and vice versa, $\|d u\|_{L_{1}^{p, w}}$ controls $\left\|u^{-1} d u\right\|_{L_{1}^{p, w}}$, so we try
$$\mathcal{G}=\left\{u \in L_{2, \mathrm{loc}}^{p}(X ; \mathrm{U}(1)): d u,(u-1) \Phi_{o} \in L_{1}^{p, w}\right\} .$$
By $L_{2, \text { loc }}^{p}(X ; \mathrm{U}(1))$ we mean the set of elements of $L_{2, \text { loc }}^{p}(X ; \mathbb{C})$ that map into U(1). We will see that $\mathcal{G}$ has a natural smooth structure such that the above criteria are satisfied.
(This approach to the definition of $\mathcal{G}$ was inspired by [10].)

\subsection*{2.2 The Banach algebra}

Let $\widetilde{x}$ be a finite subset of $X$ which contains at least one point from every connected component of $X$ where $\Phi_{o}$ vanishes identically.

Definition 2.1 Set
$$\mathcal{E}=\left\{f \in L_{2, \mathrm{loc}}^{p}(X ; \mathbb{C}): d f, f \Phi_{o} \in L_{1}^{p, w}\right\},$$
and let $\mathcal{E}$ have the norm
$$\|f\|_{\mathcal{E}}=\|d f\|_{L_{1}^{p, w}}+\left\|f \Phi_{o}\right\|_{L_{1}^{p, w}}+\sum_{x \in \widetilde{x}}|f(x)| .$$

We will see in a moment that $\mathcal{E}$ is a Banach algebra (without unit if $r_{0}<r$ ). The next lemma shows that the topology on $\mathcal{E}$ is independent of the choice of $\Phi_{o}$ and $\widetilde{x}$.

Lemma 2.1 Let $Z \subset X$ be a compact, connected codimension 0 submanifold.
\begin{itemize}
\item[(i)] If $\left.\Phi_{o}\right|_{Z} \not \equiv 0$ then there is a constant $C$ such that
$$\int_{Z}|f|^{p} \leq C \int_{Z}|d f|^{p}+\left|f \Phi_{o}\right|^{p}$$
for all $f \in L_{1}^{p}(Z)$.
\item[(ii)] There are constants $C_{1}, C_{2}$ such that
$$\left|f\left(z_{2}\right)-f\left(z_{1}\right)\right| \leq C_{1}\|d f\|_{L^{2 p}(Z)} \leq C_{2}\|d f\|_{L_{1}^{p}(Z)}$$
for all $f \in L_{2}^{p}(Z)$ and $z_{1}, z_{2} \in Z$.
\end{itemize}

Proof Part (i) follows from the compactness of the embedding $L_{1}^{p}(Z) \rightarrow$ $L^{p}(Z)$. The first inequality in (ii) can either be deduced from the compactness of $L_{1}^{2 p}(Z) \rightarrow C^{0}(Z)$, or one can prove it directly, as a step towards proving the Rellich lemma, by considering the integrals of $d f$ along a suitable family of paths from $z_{1}$ to $z_{2}$. \(\square\)

Lemma 2.2 Let $Y$ be a closed Riemannian manifold, and $\sigma>0$.
\begin{itemize}
\item[(i)] If $q \geq 1$ and $f: \mathbb{R}_{+} \times Y \rightarrow \mathbb{R}$ is a $C^{1}$ function such that $\lim _{t \rightarrow \infty} f(t, y)=$ 0 for all $y \in Y$ then
$$\|f\|_{L^{q, \sigma}\left(\mathbb{R}_{+} \times Y\right)} \leq \sigma^{-1}\left\|\partial_{1} f\right\|_{L^{q, \sigma}\left(\mathbb{R}_{+} \times Y\right)} .$$
\item[(ii)] If $q>1, T \geq 1$, and $f:[0, T] \times Y \rightarrow \mathbb{R}$ is a $C^{1}$ function then
$$\|f\|_{L^{q}([T-1, T] \times Y)} \leq\left\|f_{0}\right\|_{L^{q}(Y)}+(\sigma r)^{-1 / r}\left\|\partial_{1} f\right\|_{L^{q, \sigma}([0, T] \times Y)},$$
where $f_{0}(y)=f(0, y)$ and $\frac{1}{q}+\frac{1}{r}=1$.
\end{itemize}
Here $\partial_{1}$ is the partial derivative in the first variable, ie in the $\mathbb{R}_{+}$coordinate.
Proof Part (i):
$$\begin{aligned}
\|f\|_{L^{q, \sigma}\left(\mathbb{R}_{+} \times Y\right)} & =\left(\int_{\mathbb{R}_{+} \times Y}\left|\int_{0}^{\infty} e^{\sigma t} \partial_{1} f(s+t, y) d s\right|^{q} d t d y\right)^{1 / q} \\
& \leq \int_{0}^{\infty}\left(\int_{\mathbb{R}_{+} \times Y}\left|e^{\sigma t} \partial_{1} f(s+t, y)\right|^{q} d t d y\right)^{1 / q} d s \\
& \leq\left(\int_{0}^{\infty} e^{-\sigma s} d s\right)\left(\int_{\mathbb{R}_{+} \times Y}\left|e^{\sigma(s+t)} \partial_{1} f(s+t, y)\right|^{q} d t d y\right)^{1 / q} \\
& \leq \sigma^{-1}\left\|\partial_{1} f\right\|_{L^{q, \sigma}\left(\mathbb{R}_{+} \times Y\right)}
\end{aligned}$$

Part (ii) follows by a similar computation. \(\square\)

Parts (i)-(iv) of the following proposition are essentially due to Donaldson [10].
Proposition 2.1
\begin{itemize}
\item[(i)] There is a constant $C_{1}$ such that
$$\|f\|_{\infty} \leq C_{1}\|f\|_{\mathcal{E}}$$
for all $f \in \mathcal{E}$.
\item[(ii)] For every $f \in \mathcal{E}$ and $j=1, \ldots, r$ the restriction $\left.f\right|_{\{t\} \times Y_{j}}$ converges uniformly to a constant function $f^{(j)}$ as $t \rightarrow \infty$, and $f^{(j)}=0$ for $j>r_{0}$.
\item[(iii)] There is a constant $C_{2}$ such that if $f \in \mathcal{E}$ and $f^{(j)}=0$ for all $j$ then
$$\|f\|_{L_{2}^{p, w}} \leq C_{2}\|f\|_{\mathcal{E}} .$$
\item[(iv)] There is an exact sequence
$$0 \rightarrow L_{2}^{p, w} \xrightarrow{\iota} \mathcal{E} \xrightarrow{e} \mathbb{C}^{r_{0}} \rightarrow 0,$$
where $\iota$ is the inclusion and $e(f)=\left(f^{(1)}, \ldots, f^{\left(r_{0}\right)}\right)$.
\item[(v)] $\mathcal{E}$ is complete, and multiplication defines a continuous map $\mathcal{E} \times \mathcal{E} \rightarrow \mathcal{E}$.
\end{itemize}

Proof First observe that for any $f \in L_{2 \text {,loc }}^{p}(X)$ and $\epsilon>0$ there exists a $g \in C^{\infty}(X)$ such that $\|g-f\|_{L_{2}^{p, w}}<\epsilon$. Therefore it suffices to prove (i)-(iii) when $f \in \mathcal{E}$ is smooth. Part (i) is then a consequence of Lemma 2.1 and Lemma 2.2 (ii), while Part (ii) for $r_{0}<j \leq r$ follows from Lemma 2.1
We will now prove (ii) when $1 \leq j \leq r_{0}$. Let $f \in \mathcal{E}$ be smooth. Since $\int_{\mathbb{R}_{+} \times Y_{j}}|d f|<\infty$ by the Hölder inequality, we have
$$\int_{0}^{\infty}\left|\partial_{1} f(t, y)\right| d t<\infty \quad \text { for almost all } y \in Y_{j}$$
For $n \in \mathbb{N}$ set $f_{n}=\left.f\right|_{[n-1, n+1] \times Y_{j}}$, regarded as a function on $B=[n-1, n+1] \times$ $Y_{j}$. Then $\left\{f_{n}\right\}$ converges a.e., so by Egoroff's theorem $\left\{f_{n}\right\}$ converges uniformly over some subset $T \subset B$ of positive measure. There is then a constant $C>0$, depending on $T$, such that for every $g \in L_{1}^{p}(B)$ one has
$$\int_{B}|g|^{p} \leq C\left(\int_{B}|d g|^{p}+\int_{T}|g|^{p}\right) .$$
It follows that $\left\{f_{n}\right\}$ converges in $L_{2}^{p}$ over $B$, hence uniformly over $B$, to some constant function.

Part (iii) follows from Lemma 2.1 and Lemma 2.2 (i). Part (iv) is an immediate consequence of (ii) and (iii). It is clear from (i) that $\mathcal{E}$ is complete. The multiplication property follows easily from (i) and the fact that smooth functions are dense in $\mathcal{E}$. \(\square\)

\subsection*{2.3 The infinitesimal action}

If $f: X \rightarrow i \mathbb{R}$ and $\Phi$ is a section of $\mathbb{S}$ we define a section of $i \Lambda^{1} \oplus \mathbb{S}$ by
$$\mathcal{I}_{\Phi} f=(-d f, f \Phi)$$
whenever the expression on the right makes sense. Here $\Lambda^{k}$ denotes the bundle of $k$-forms (on $X$, in this case). If $S=(A, \Phi)$ is a configuration then we will sometimes write $\mathcal{I}_{S}$ instead of $\mathcal{I}_{\Phi}$. Set
$$\mathcal{I}=\mathcal{I}_{\Phi_{o}} .$$
If $\Phi$ is smooth then the formal adjoint of the operator $\mathcal{I}_{\Phi}$ is
$$\mathcal{I}_{\Phi}^{*}(a, \phi)=-d^{*} a+i\langle i \Phi, \phi\rangle_{\mathbb{R}},$$
where $\langle\cdot, \cdot\rangle_{\mathbb{R}}$ is the real inner product on $\mathbb{S}$. Note that
$$\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}=\Delta+|\Phi|^{2}$$
where $\Delta$ is the positive Laplacian on $X$.
Set
$$L \mathcal{G}=\{f \in \mathcal{E}: f \text { maps into } i \mathbb{R}\} .$$
From Proposition 2.1 (i) we see that the operators
$$\mathcal{I}_{\Phi}: L \mathcal{G} \rightarrow L_{1}^{p, w}, \quad \mathcal{I}_{\Phi}^{*}: L_{1}^{p, w} \rightarrow L^{p, w}$$
are well-defined and bounded for every $\Phi \in \Phi_{o}+L_{1}^{p, w}(X ; \mathbb{S})$.
Lemma 2.3 For every $\Phi \in \Phi_{o}+L_{1}^{p, w}(X ; \mathbb{S})$, the operators $\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}$ and $\mathcal{I}_{\Phi}$ have the same kernel in $L \mathcal{G}$.

Proof Choose a smooth function $\beta: \mathbb{R} \rightarrow \mathbb{R}$ such that $\beta(t)=1$ for $t \leq 1$, $\beta(t)=0$ for $t \geq 2$. For $r>0$ define a compactly supported function
$$\beta_{r}: X \rightarrow \mathbb{R}$$
by $\left.\beta_{r}\right|_{X_{: 0}}=1$, and $\beta_{r}(t, y)=\beta(t / r)$ for $(t, y) \in \mathbb{R}_{+} \times Y_{j}$.
Now suppose $f \in L \mathcal{G}$ and $\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi} f=0$. Lemma 2.1 (i) and elliptic regularity gives $f \in L_{2, \text { loc }}^{p}$, so we certainly have
$$\mathcal{I}_{\Phi} f \in L_{1, \mathrm{loc}}^{p} \subset L_{\mathrm{loc}}^{2} .$$
Clearly,
$$\left\|\mathcal{I}_{\Phi} f\right\|_{2} \leq \liminf _{r \rightarrow \infty}\left\|\mathcal{I}_{\Phi}\left(\beta_{r} f\right)\right\|_{2} .$$

Over $\mathbb{R}_{+} \times Y_{j}$ we have
$$\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}=-\partial_{1}^{2}+\Delta_{Y_{j}}+|\Phi|^{2},$$
where $\partial_{1}=\frac{\partial}{\partial t}$ and $\Delta_{Y_{j}}$ is the positive Laplacian on $Y_{j}$, so
$$\begin{aligned}
\left\|\mathcal{I}_{\Phi}\left(\beta_{r} f\right)\right\|_{2}^{2}= & \int_{X} \mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}\left(\beta_{r} f\right) \cdot \beta_{r} \bar{f} \\
= & -\sum_{j} \int_{\mathbb{R}_{+\times Y_{j}}}\left(\left(\partial_{1}^{2} \beta_{r}\right) f+2\left(\partial_{1} \beta_{r}\right)\left(\partial_{1} f\right)\right) \cdot \beta_{r} \bar{f} \\
\leq & C_{1}\|f\|_{\infty}^{2} \int_{0}^{\infty}\left|r^{-2} \beta^{\prime \prime}(t / r)\right| d t \\
& \quad+C_{1}\|f\|_{\infty}\|d f\|_{p}\left(\int_{0}^{\infty}\left|r^{-1} \beta^{\prime}(t / r)\right|^{q} d t\right)^{1 / q} \\
\leq & C_{2}\|f\|_{\mathcal{E}}^{2}\left(r^{-1} \int_{1}^{2}\left|\beta^{\prime \prime}(u)\right| d u+r^{1-q} \int_{1}^{2}\left|\beta^{\prime}(u)\right|^{q} d u\right) \\
& \rightarrow 0 \text { as } r \rightarrow \infty,
\end{aligned}$$
where $C_{1}, C_{2}>0$ are constants and $\frac{1}{p}+\frac{1}{q}=1$. Hence $\mathcal{I}_{\Phi} f=0$. \(\square\)

Lemma $2.4 \mathcal{I}^{*} \mathcal{I}: L_{2}^{q, w}(X) \rightarrow L^{q, w}(X)$ is Fredholm of index $-r_{0}$, for $1<q<$ $\infty$.

Proof Because $\mathcal{I}^{*} \mathcal{I}$ is elliptic the operator in the Lemma is Fredholm if the operator
$$-\partial_{1}^{2}+\Delta_{Y_{j}}+\left|\psi_{j}\right|^{2}: L_{2}^{q, \sigma_{j}} \rightarrow L^{q, \sigma_{j}},$$
acting on functions on $\mathbb{R} \times Y_{j}$, is Fredholm for each $j$. The proof of [10, Proposition 3.21] (see also [24]) can be generalized to show that (7) is Fredholm if $\sigma_{j}^{2}$ is not an eigenvalue of $\Delta_{Y_{j}}+\left|\psi_{j}\right|^{2}$. Since we are taking $\sigma_{j} \geq 0$ small, and $\sigma_{j}>0$ if $\psi_{j}=0$, this establishes the Fredholm property in the Lemma.

We will now compute the index. Set
$$\operatorname{ind}^{ \pm}=\operatorname{index}\left\{\mathcal{I}^{*} \mathcal{I}: L_{2}^{q, \pm w}(X) \rightarrow L^{q, \pm w}(X)\right\} .$$
Expressing functions on $Y_{j}$ in terms of eigenvectors of $\Delta_{Y_{j}}+\left|\psi_{j}\right|^{2}$ as in [3, 10] one finds that the kernel of $\mathcal{I}^{*} \mathcal{I}$ in $L_{k^{\prime}}^{q^{\prime}, \pm w}$ is the same for all $q^{\prime}>1$ and integers $k^{\prime} \geq 0$. Combining this with the fact that $\mathcal{I}^{*} \mathcal{I}$ is formally self-adjoint we see that
$$\mathrm{ind}^{+}=-\mathrm{ind}^{-} .$$

Now choose smooth functions $w_{j}: \mathbb{R} \rightarrow \mathbb{R}$ such that $w_{j}(t)=\sigma_{j}|t|$ for $|t| \geq 1$. We will apply the addition formula for the index, see [10, Proposition 3.9]. This is proved only for first order operators in [10] but holds for higher order operators as well, with essentially the same proof. The addition formula gives
$$\begin{aligned}
\operatorname{ind}^{-} & =\operatorname{ind}^{+}+\sum_{j} \operatorname{index}\left\{\mathcal{I}_{\psi_{j}}^{*} \mathcal{I}_{\psi_{j}}: L_{2}^{q,-w_{j}}\left(\mathbb{R} \times Y_{j}\right) \rightarrow L^{q,-w_{j}}\left(\mathbb{R} \times Y_{j}\right)\right\} \\
& =\operatorname{ind}^{+}+2 \sum_{j} \operatorname{dim} \operatorname{ker}\left(\Delta_{Y_{j}}+\left|\psi_{j}\right|^{2}\right) \\
& =\mathrm{ind}^{+}+2 r_{0} .
\end{aligned}$$
Therefore, ind $^{+}=-r_{0}$ as claimed. \(\square\)

Proposition 2.2 For any $\Phi \in \Phi_{o}+L_{1}^{p, w}(X ; \mathbb{S})$ the following hold:
\begin{itemize}
\item[(i)] The operator
$$\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}: L \mathcal{G} \rightarrow L^{p, w}$$
is Fredholm of index 0, and it has the same kernel as $\mathcal{I}_{\Phi}: L \mathcal{G} \rightarrow L_{1}^{p, w}$ and the same image as $\mathcal{I}_{\Phi}^{*}: L_{1}^{p, w} \rightarrow L^{p, w}$.
\item[(ii)] $\mathcal{I}_{\Phi}(L \mathcal{G})$ is closed in $L_{1}^{p, w}$ and
$$L_{1}^{p, w}\left(i \Lambda^{1} \oplus \mathbb{S}\right)=\mathcal{I}_{\Phi}(L \mathcal{G}) \oplus \operatorname{ker}\left(\mathcal{I}_{\Phi}^{*}\right) .$$
\end{itemize}

Proof It is easy to deduce Part (ii) from Part (i). We will now prove Part (i). Since
$$\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}-\mathcal{I}^{*} \mathcal{I}=|\Phi|^{2}-\left|\Phi_{o}\right|^{2}: L_{2}^{p, w} \rightarrow L^{p, w}$$
is a compact operator, $\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}$ and $\mathcal{I}^{*} \mathcal{I}$ have the same index as operators between these Banach spaces. It then follows from Lemma 2.4 and Proposition 2.1 (iv) that the operator (8) is Fredholm of index 0. The statement about the kernels is the same as Lemma 2.3. To prove the statement about the images, we may as well assume $X$ is connected. If $\Phi \neq 0$ then the operator (8) is surjective and there is nothing left to prove. Now suppose $\Phi=0$. Then all the weights $\sigma_{j}$ are positive, and the kernel of $\mathcal{I}_{\Phi}$ in $\mathcal{E}$ consists of the constant functions. Hence the image of (8) has codimension 1. But $\int_{X} d^{*} a=0$ for every 1-form $a \in L_{1}^{p, w}$, so $d^{*}: L_{1}^{p, w} \rightarrow L^{p, w}$ is not surjective. \(\square\)

In the course of the proof of (i) we obtained:
Proposition 2.3 If $X$ is connected and $r_{0}=r$ then
$$d^{*} d(\mathcal{E})=\left\{g \in L^{p, w}(X ; \mathbb{C}): \int_{X} g=0\right\} .$$

We conclude this subsection with a result that will be needed in the proofs of Proposition 5.3 and Lemma 5.5 below. Let $1<q<\infty$ and for any $L_{1, \text { loc }}^{q}$ function $f: X \rightarrow \mathbb{R}$ set
$$\delta_{j} f=\int_{\{0\} \times Y_{j}} \partial_{1} f, \quad j=1, \ldots, r$$
The integral is well-defined because if $n$ is any positive integer then there is a bounded restriction map $L_{1}^{q}\left(\mathbb{R}^{n}\right) \rightarrow L^{q}\left(\{0\} \times \mathbb{R}^{n-1}\right)$.

Choose a point $x_{0} \in X$.
Proposition 2.4 If $X$ is connected, $1<q<\infty, r \geq 1$, and if $\sigma_{j}>0$ is sufficiently small for each $j$ then the operator
$$\begin{aligned}
\beta: L_{2}^{q,-w}(X ; \mathbb{R}) & \rightarrow L^{q,-w}(X ; \mathbb{R}) \oplus \mathbb{R}^{r} \\
f & \mapsto\left(\Delta f,\left(\delta_{1} f, \ldots, \delta_{r-1} f, f\left(x_{0}\right)\right)\right)
\end{aligned}$$
is an isomorphism.
Proof By the proof of Lemma 2.4. $\Delta: L_{2}^{q,-w} \rightarrow L^{q,-w}$ has index $r$, hence $\operatorname{ind}(\beta)=0$. We will show $\beta$ is injective. First observe that $\sum_{j=1}^{r} \delta_{j} f=0$ whenever $\Delta f=0$, so if $\beta f=0$ then $\delta_{j} f=0$ for all $j$.

Suppose $\beta f=0$. To simplify notation we will now assume $Y$ is connected. Over $\mathbb{R}_{+} \times Y$ we have $\Delta=-\partial_{1}^{2}+\Delta_{Y}$. Let $\left\{h_{\nu}\right\}_{\nu=0,1, \ldots}$ be a maximal orthonormal set of eigenvectors of $\Delta_{Y}$, with corresponding eigenvalues $\lambda_{\nu}^{2}$, where $0=\lambda_{0}<$ $\lambda_{1} \leq \lambda_{2} \leq \cdots$. Then
$$f(t, y)=a+b t+g(t, y),$$
where $a, b \in \mathbb{R}$, and $g$ has the form
$$g(t, y)=\sum_{\nu \geq 1} c_{\nu} e^{-\lambda_{\nu} t} h_{\nu}(y)$$
for some real constants $c_{\nu}$. Elliptic estimates show that $g$ decays exponentially, or more precisely,
$$\left|\left(\nabla^{j} f\right)_{(t, y)}\right| \leq d_{j} e^{-\lambda_{1} t}$$
for $(t, y) \in \mathbb{R}_{+} \times Y$ and $j \geq 0$, where $d_{j}>0$ is a constant. Now
$$\partial_{1} f(t, y)=b-\sum_{\nu \geq 1} c_{\nu} \lambda_{\nu} e^{-\lambda_{\nu} t} h_{\nu}(y) .$$
Since $\Delta_{Y}$ is formally self-adjoint we have $\int_{Y} h_{\nu}=0$ if $\lambda_{\nu} \neq 0$, hence
$$b \operatorname{Vol}(Y)=\int_{\{\tau\} \times Y} \partial_{1} f=0 .$$

It follows that $f$ is bounded and $d f$ decays exponentially over $\mathbb{R}_{+} \times Y$, so
$$0=\int_{X} f \Delta f=\int_{X}|d f|^{2}$$
hence $f$ is constant. Since $f\left(x_{0}\right)=0$ we have $f=0$. \(\square\)

\subsection*{2.4 Local slices}

Fix a finite subset $\mathfrak{b} \subset X$.
Definition 2.2 Set
$$\begin{aligned}
& \mathcal{G}_{\mathfrak{b}}=\left\{u \in 1+\mathcal{E}: u \text { maps into } \mathrm{U}(1) \text { and }\left.u\right|_{\mathfrak{b}} \equiv 1\right\} \\
& L \mathcal{G}_{\mathfrak{b}}=\left\{f \in \mathcal{E}: f \text { maps into } i \mathbb{R} \text { and }\left.f\right|_{\mathfrak{b}} \equiv 0\right\}
\end{aligned}$$
and let $\mathcal{G}_{\mathfrak{b}}$ and $L \mathcal{G}_{\mathfrak{b}}$ have the subspace topologies inherited from $1+\mathcal{E} \approx \mathcal{E}$ and $\mathcal{E}$, respectively.

By $1+\mathcal{E}$ we mean the set of functions on $X$ of the form $1+f$ where $f \in \mathcal{E}$. If $\mathfrak{b}$ is empty then we write $\mathcal{G}$ instead of $\mathcal{G}_{\mathfrak{b}}$, and similarly for $L \mathcal{G}$.

Proposition 2.5
\begin{itemize}
\item[(i)] $\mathcal{G}_{\mathfrak{b}}$ is a smooth submanifold of $1+\mathcal{E}$ and a Banach Lie group with Lie algebra $L \mathcal{G}_{\mathfrak{b}}$.
\item[(ii)] The natural action $\mathcal{G}_{\mathfrak{b}} \times \mathcal{C} \rightarrow \mathcal{C}$ is smooth.
\item[(iii)] If $S \in \mathcal{C}, u \in L_{2, \text { loc }}^{p}(X ; U(1))$ and $u(S) \in \mathcal{C}$ then $u \in \mathcal{G}$.
\end{itemize}

Proof (i) If $r_{0}<r$ then $1 \notin \mathcal{E}$, but in any case,
$$f \mapsto \sum_{k=1}^{\infty} \frac{1}{k!} f^{k}=\exp (f)-1$$
defines a smooth map $\mathcal{E} \rightarrow \mathcal{E}$, by Proposition 2.1 (v). Therefore, the exponential map provides the local parametrization around 1 required for $\mathcal{G}_{\mathfrak{b}}$ to be a submanifold of $1+\mathcal{E}$. The verification of (ii) and (iii) is left to the reader. \(\square\)

Let $\mathcal{B}_{\mathfrak{b}}=\mathcal{C} / \mathcal{G}_{\mathfrak{b}}$ have the quotient topology. This topology is Hausdorff because it is stronger than the topology defined by the $L^{2 p}$ metric on $\mathcal{B}_{\mathfrak{b}}$ (see [11]). The image in $\mathcal{B}_{\mathfrak{b}}$ of a configuration $S \in \mathcal{C}$ will be denoted $[S]$, and we say $S$ is a representative of $[S]$.

Let $\mathcal{C}_{\mathfrak{b}}^{*}$ be the set of all elements of $\mathcal{C}$ which have trivial stabilizer in $\mathcal{G}_{\mathfrak{b}}$. In other words, $\mathcal{C}_{\mathfrak{b}}^{*}$ consists of those $(A, \Phi) \in \mathcal{C}$ such that $\mathfrak{b}$ contains at least one point from every component of $X$ where $\Phi$ vanishes almost everywhere. Let $\mathcal{B}_{\mathfrak{b}}^{*}$ be the image of $\mathcal{C}_{\mathfrak{b}}^{*} \rightarrow \mathcal{B}_{\mathfrak{b}}$. It is clear that $\mathcal{B}_{\mathfrak{b}}^{*}$ is an open subset of $\mathcal{B}_{\mathfrak{b}}$.
If $\mathfrak{b}$ is empty then $\mathcal{C}^{*} \subset \mathcal{C}$ and $\mathcal{B}^{*} \subset \mathcal{B}$ are the subspaces of irreducible configurations. As usual, a configuration that is not irreducible is called reducible.

We will now give $\mathcal{B}_{\mathfrak{b}}^{*}$ the structure of a smooth Banach manifold by specifying an atlas of local parametrizations. Let $S=(A, \Phi) \in \mathcal{C}_{\mathfrak{b}}^{*}$ and set
$$V=\mathcal{I}_{\Phi}^{*}\left(L_{1}^{p, w}\right), \quad W=\mathcal{I}_{\Phi}^{*} \mathcal{I}_{\Phi}\left(L \mathcal{G}_{\mathfrak{b}}\right) .$$
By Proposition 2.2 we have
$$\operatorname{dim}(V / W)=|\mathfrak{b}|-\ell$$
where $\ell$ is the number of components of $X$ where $\Phi$ vanishes almost everywhere Choose a bounded linear map $\rho: V \rightarrow W$ such that $\left.\rho\right|_{W}=I$, and set
$$\mathcal{I}_{\Phi}^{\#}=\rho \mathcal{I}_{\Phi}^{*} .$$
Then
$$L_{1}^{p, w}\left(i \Lambda^{1} \oplus \mathbb{S}\right)=\mathcal{I}_{\Phi}\left(L \mathcal{G}_{\mathfrak{b}}\right) \oplus \operatorname{ker}\left(\mathcal{I}_{\Phi}^{\#}\right)$$
by Proposition 2.2. Consider the smooth map
$$\Pi: L \mathcal{G}_{\mathfrak{b}} \times \operatorname{ker}\left(\mathcal{I}_{\Phi}^{\#}\right) \rightarrow \mathcal{C}, \quad(f, s) \mapsto \exp (f)(S+s) .$$
The derivative of this map at $(0,0)$ is
$$D \Pi(0,0)(f, s)=\mathcal{I}_{\Phi} f+s,$$
which is an isomorphism by the above remarks. The inverse function theorem then says that $\Pi$ is a local diffeomorphism at (0, 0).

Proposition 2.6 In the situation above there is an open neighbourhood $U$ of $0 \in \operatorname{ker}\left(\mathcal{I}_{\Phi}^{\#}\right)$ such that the projection $\mathcal{C} \rightarrow \mathcal{B}_{\mathfrak{b}}$ restricts to a topological embedding of $S+U$ onto an open subset of $\mathcal{B}_{\mathfrak{b}}^{*}$.

It is clear that the collection of such local parametrizations $U \rightarrow \mathcal{B}_{\mathfrak{b}}^{*}$ is a smooth atlas for $\mathcal{B}_{\mathfrak{b}}^{*}$.

Proof It only remains to prove that $S+U \rightarrow \mathcal{B}_{\mathfrak{b}}$ is injective when $U$ is sufficiently small. So suppose $\left(a_{k}, \phi_{k}\right),\left(b_{k}, \psi_{k}\right)$ are two sequences in $\operatorname{ker}\left(\mathcal{I}_{\Phi}^{\#}\right)$ which both converge to 0 as $k \rightarrow \infty$, and such that
$$u_{k}\left(A+a_{k}, \Phi+\phi_{k}\right)=\left(A+b_{k}, \Phi+\psi_{k}\right)$$
for some $u_{k} \in \mathcal{G}_{\mathfrak{b}}$. We will show that $\left\|u_{k}-1\right\|_{\mathcal{E}} \rightarrow 0$. Since $\Pi$ is a local diffeomorphism at $(0,0)$, this will imply that $u_{k}=1$ for $k \gg 0$.

Written out, the assumption on $u_{k}$ is that
$$\begin{aligned}
u_{k}^{-1} d u_{k} & =a_{k}-b_{k}, \\
\left(u_{k}-1\right) \Phi & =\psi_{k}-u_{k} \phi_{k} .
\end{aligned}$$
By (5) we have $\left\|d u_{k}\right\|_{L_{1}^{p, w}} \rightarrow 0$, which in turn gives $\left\|u_{k} \phi_{k}\right\|_{L_{1}^{p, w}} \rightarrow 0$, hence
$$\left\|\left(u_{k}-1\right) \Phi\right\|_{L_{1}^{p, w}} \rightarrow 0 .$$
Because $u_{k}$ is bounded and $d u_{k}$ converges to 0 in $L_{1}^{p}$ over compact subsets, we can find a subsequence $\left\{k_{j}\right\}$ such that $u_{k_{j}}$ converges in $L_{2}^{p}$ over compact subsets to a locally constant function $u$. Then $\left.u\right|_{\mathfrak{b}}=1$ and $u \Phi=\Phi$, hence $u=1$. Set $f_{j}=u_{k_{j}}-1$ and $\phi=\Phi-\Phi_{o} \in L_{1}^{p, w}$. Then $\left\|d f_{j} \otimes \phi\right\|_{L^{p, w}} \rightarrow 0$. Furthermore, given $\epsilon>0$ we can find $t>0$ such that
$$\int_{[t, \infty) \times Y}\left|e^{w} \phi\right|^{p}<\frac{\epsilon}{4}$$
and $N$ such that
$$\int_{X_{: t}}\left|e^{w} f_{j} \phi\right|^{p}<\frac{\epsilon}{2}$$
for $j>N$. Then $\int_{X}\left|e^{w} f_{j} \phi\right|^{p}<\epsilon$ for $j>N$. Thus $\left\|f_{j} \phi\right\|_{L^{p, w}} \rightarrow 0$, and similarly $\left\|f_{j} \nabla \phi\right\|_{L^{p, w}} \rightarrow 0$. Altogether this shows that $\left\|f_{j} \phi\right\|_{L_{1}^{p, w}} \rightarrow 0$. Combined with (10) this yields
$$\left\|\left(u_{k_{j}}-1\right) \Phi_{0}\right\|_{L_{1}^{p, w}} \rightarrow 0,$$
hence $\left\|u_{k_{j}}-1\right\|_{\mathcal{E}} \rightarrow 0$. But we can run the above argument starting with any subsequence of $\left\{u_{k}\right\}$, so $\left\|u_{k}-1\right\|_{\mathcal{E}} \rightarrow 0$. \(\square\)

\subsection*{2.5 Manifolds with boundary}

Let $Z$ be a compact, connected, oriented Riemannian $n$-manifold, perhaps with boundary, and $\mathfrak{b} \subset Z$ a finite subset. Let $\mathbb{S} \rightarrow Z$ be a Hermitian vector bundle and $L \rightarrow Z$ a principal U(1)-bundle. Fix $p>n / 2$ and let $\mathcal{C}$ denote the space of $L_{1}^{p}$ configurations $(A, \Phi)$ in $(L, \mathbb{S})$. Let $\mathcal{G}_{\mathfrak{b}}$ be the group of those $L_{2}^{p}$ gauge transformations $Z \rightarrow \mathrm{U}(1)$ that restrict to 1 on $\mathfrak{b}$, and $\mathcal{C}_{\mathfrak{b}}^{*}$ the set of all elements of $\mathcal{C}$ that have trivial stabilizer in $\mathcal{G}_{\mathfrak{b}}$. Then
$$\mathcal{B}_{\mathfrak{b}}^{*}=\mathcal{C}_{\mathfrak{b}}^{*} / \mathcal{G}_{\mathfrak{b}}$$
is again a (Hausdorff) smooth Banach manifold. As for orbit spaces of connections (see [11, p 192]) the main ingredient here is the solution to the Neumann problem over $Z$, according to which the operator
$$\begin{aligned}
T_{\Phi}: L_{2}^{p}(Z) & \rightarrow L^{p}(Z) \oplus \partial L_{1}^{p}(\partial Z), \\
f & \mapsto\left(\Delta f+|\Phi|^{2} f, \partial_{\nu} f\right)
\end{aligned}$$
is a Fredholm operator of index 0 (see [31, Section 5.7] and [16, pages 85-86]). Here $\nu$ is the inward-pointing unit normal along $\partial Z$, and $\partial L_{1}^{p}(\partial Z)$ is the space of boundary values of $L_{1}^{p}$ functions on $Z$. Henceforth we work with imaginary-valued functions, and on $\partial Z$ we identify 3-forms with functions by means of the Hodge *-operator. Then $T_{\Phi}=J_{\Phi} \mathcal{I}_{\Phi}$, where
$$J_{\Phi}(a, \phi)=\left(\mathcal{I}_{\Phi}^{*}(a, \phi),\left.(* a)\right|_{\partial Z}\right) .$$
Choose a bounded linear map
$$\rho: L^{p}(Z) \oplus \partial L_{1}^{p}(\partial Z) \rightarrow W:=T_{\Phi}\left(L \mathcal{G}_{\mathfrak{b}}\right)$$
which restricts to the identity on $W$, and set $J_{\Phi}^{\#}=\rho J_{\Phi}$. An application of Stokes' theorem shows that
$$\operatorname{ker}\left(T_{\Phi}\right) \subset \operatorname{ker}\left(\mathcal{I}_{\Phi}\right) \quad \text { in } L_{2}^{p}(Z),$$
hence
$$T_{\Phi}=J_{\Phi}^{\#} \mathcal{I}_{\Phi}: L \mathcal{G}_{\mathfrak{b}} \rightarrow W$$
is an isomorphism. In general, if $V_{1} \xrightarrow{T_{1}} V_{2} \xrightarrow{T_{2}} V_{3}$ are linear maps between vector spaces such that $T_{2} T_{1}$ is an isomorphism, then $V_{2}=\operatorname{im}\left(T_{1}\right) \oplus \operatorname{ker}\left(T_{2}\right)$. Therefore, for any $(A, \Phi) \in \mathcal{C}_{\mathfrak{b}}^{*}$ we have
$$L_{1}^{p}\left(Z ; i \Lambda^{1} \oplus \mathbb{S}\right)=\mathcal{I}_{\Phi}\left(L \mathcal{G}_{\mathfrak{b}}\right) \oplus \operatorname{ker}\left(J_{\Phi}^{\#}\right),$$
where both summands are closed subspaces. Thus we obtain the analogue of Proposition 2.6 with local slices of the form $(A, \Phi)+U$, where $U$ is a small neighbourhood of $0 \in \operatorname{ker}\left(J_{\Phi}^{\#}\right)$.

\section*{3 Moduli spaces}

\subsection*{3.1 Spin ${ }^{c}$ structures}

It will be convenient to have a definition of spin ${ }^{c}$ structure that does not refer to Riemannian metrics. So let $X$ be an oriented $n$-dimensional manifold and $P_{\mathrm{GL}}$ its bundle of positive linear frames. Let $\widetilde{\mathrm{GL}}^{+}(n)$ denote the 2-fold
universal covering group of the identity component $\operatorname{GL}^{+}(n)$ of $\operatorname{GL}(n, \mathbb{R})$, and denote by -1 the non-trivial element of the kernel of $\widetilde{\mathrm{GL}}^{+}(n) \rightarrow \mathrm{GL}^{+}(n)$. Set
$$\mathrm{GL}^{c}(n)=\widetilde{\mathrm{GL}}^{+}(n) \underset{ \pm(1,1)}{\times} \mathrm{U}(1) .$$
Then there is a short exact sequence
$$0 \rightarrow \mathbb{Z} / 2 \rightarrow \operatorname{GL}^{c}(n) \rightarrow \operatorname{GL}^{+}(n) \times \mathrm{U}(1) \rightarrow 1,$$
and $\operatorname{Spin}^{c}(n)$ is canonically isomorphic to the preimage of $\operatorname{SO}(n)$ by the projection $\mathrm{GL}^{c}(n) \rightarrow \mathrm{GL}^{+}(n)$.

Definition 3.1 By a spin ${ }^{c}$ structure $\mathfrak{s}$ on $X$ we mean a principal $\operatorname{GL}^{c}(n)-$ bundle $P_{\mathrm{GL}^{c}} \rightarrow X$ together with a $\operatorname{GL}^{c}(n)$ equivariant map $P_{\mathrm{GL}^{c}} \rightarrow P_{\mathrm{GL}^{+}}$ which covers the identity on $X$. If $\mathfrak{s}^{\prime}$ is another spin ${ }^{c}$ structure on $X$ given by $P_{\mathrm{GL}^{c}}^{\prime} \rightarrow P_{\mathrm{GL}^{+}}$then $\mathfrak{s}$ and $\mathfrak{s}^{\prime}$ are called isomorphic if there is a U(1) equivariant map $P_{\mathrm{GL}^{c}}^{\prime} \rightarrow P_{\mathrm{GL}^{c}}$ which covers the identity on $P_{\mathrm{GL}^{+}}$.

The natural U(1)-bundle associated to $P_{\mathrm{GL}^{c}}$ is denoted $\mathcal{L}$, and the Chern class $c_{1}(\mathcal{L})$ is called the canonical class of the spin ${ }^{c}$ structure.

Now suppose $X$ is equipped with a Riemannian metric, and let $P_{\mathrm{SO}}$ be its bundle of positive orthonormal frames, which is a principal $\operatorname{SO}(n)$-bundle. Then the preimage $P_{\text {Spin }}{ }^{c}$ of $P_{\text {SO }}$ by the projection $P_{\mathrm{GL}^{c}} \rightarrow P_{\mathrm{GL}^{+}}$is a principal $\operatorname{Spin}^{c}(n)$-bundle over $X$, ie a spin ${ }^{c}$ structure of $X$ in the sense of [23]. Conversely, $P_{\mathrm{GL}^{c}}$ is isomorphic to $P_{\operatorname{Spin}^{c}} \underset{\operatorname{Spin}^{c} n}{\times} \operatorname{GL}^{c}(n)$. Thus there is a natural 1-1 correspondence between (isomorphism classes of) spin ${ }^{c}$ structures of the smooth oriented manifold $X$ as defined above, and spin ${ }^{c}$ structures of the oriented Riemannian manifold $X$ in the sense of [23].

By a spin connection in $P_{\text {Spin }}{ }^{c}$ we shall mean a connection in $P_{\text {Spin }}{ }^{c}$ that maps to the Levi-Civita connection in $P_{\text {SO }}$. If $A$ is a spin connection in $P_{\text {Spin }}{ }^{c}$ then $\hat{F}_{A}$ will denote the $i \mathbb{R}$ component of the curvature of $A$ with respect to the isomorphism of Lie algebras
$$\operatorname{spin}(n) \oplus i \mathbb{R} \stackrel{\approx}{\rightarrow} \operatorname{spin}^{c}(n)$$
defined by the double cover $\operatorname{Spin}(n) \times \mathrm{U}(1) \rightarrow \operatorname{Spin}^{c}(n)$. In terms of the induced connection $\check{A}$ in $\mathcal{L}$ one has
$$\hat{F}_{A}=\frac{1}{2} F_{\check{A}} .$$
If $A, A^{\prime}$ are spin connections in $P_{\text {Spin }}{ }^{\text {c }}$ then we regard $A-A^{\prime}$ as an element of $i \Omega_{X}^{1}$.

The results of Section 2 carry over to spaces of configurations $(A, \Phi)$ where $A$ is a spin connection in $P_{\text {Spin }}{ }^{c}$ and $\Phi$ a section of some complex vector bundle $\mathbb{S} \rightarrow X$.

When the spin ${ }^{c}$ structure on $X$ is understood then we will say "spin connection over $X$ " instead of "spin connection in $P_{\text {Spin }}$ ".

If $n$ is even then the complex Clifford algebra $\mathbb{C} \ell(n)$ has up to equivalence exactly one irreducible complex representation. Let $\mathbb{S}$ denote the associated spin bundle over $X$. Then the eigenspaces of the complex volume element $\omega_{\mathbb{C}}$ in $\mathbb{C} \ell(n)$ defines a splitting $\mathbb{S}=\mathbb{S}^{+} \oplus \mathbb{S}^{-}$(see [23]).

If $n$ is odd then $\mathbb{C} \ell(n)$ has up to equivalence two irreducible complex representations $\rho_{1}, \rho_{2}$. These restrict to equivalent representations of $\operatorname{Spin}^{c}(n)$, so one gets a well-defined spin bundle $\mathbb{S}$ for any spin ${ }^{c}$ structure on $X$ [23]. If $\alpha$ is the unique automorphism of $\mathbb{C} \ell(n)$ whose restriction to $\mathbb{R}^{n}$ is multiplication by -1 then $\rho_{1} \approx \rho_{2} \circ \alpha$. Hence if $A$ is any spin connection over $X$ then the sign of the Dirac operator $D_{A}$ depends on the choice of $\rho_{j}$. To remove this ambiguity we decree that Clifford multiplication of $T X$ on $\mathbb{S}$ is to be defined using the representation $\rho_{j}$ satisfying $\rho_{j}\left(\omega_{\mathbb{C}}\right)=1$.

In the case of a Riemannian product $\mathbb{R} \times X$ there is a natural 1-1 correspondence $\operatorname{Spin}^{c}(\mathbb{R} \times X)=\operatorname{Spin}^{c}(X)$, and we can identify
$$\mathcal{L}_{\mathbb{R} \times X}=\mathbb{R} \times \mathcal{L}_{X} .$$
If $A$ is a spin connection over $\mathbb{R} \times X$ then $\left.A\right|_{\{t\} \times X}$ will denote the spin connection $B$ over $X$ satisfying $\left.\check{A}\right|_{\{t\} \times X}=\check{B}$.
When $n$ is odd then we can also identify
$$\mathbb{S}_{\mathbb{R} \times X}^{+}=\mathbb{R} \times \mathbb{S}_{X} .$$
If $e$ is a tangent vector on $X$ then Clifford multiplication with $e$ on $\mathbb{S}_{X}$ corresponds to multiplication with $e_{0} e$ on $\mathbb{S}_{\mathbb{R} \times X}^{+}$, where $e_{0}$ is the positively oriented unit tangent vector on $\mathbb{R}$. Therefore, reversing the orientation of $X$ changes the sign of the Dirac operator on $X$.

From now on, to avoid confusion we will use $\partial_{B}$ to denote the Dirac operator over a 3-manifold with spin connection $B$, while the notation $D_{A}$ will be reserved for Dirac operators over 4-manifolds.

By a configuration over a spin ${ }^{c}$ 3-manifold $Y$ we shall mean a pair $(B, \Psi)$ where $B$ is a spin connection over $Y$ and $\Psi$ a section of the spin bundle $\mathbb{S}_{Y}$. By a configuration over a spin ${ }^{c} 4$-manifold $X$ we mean a pair $(A, \Phi)$ where $A$ is a spin connection over $X$ and $\Phi$ a section of the positive spin bundle $\mathbb{S}_{X}^{+}$.

\subsection*{3.2 The Chern-Simons-Dirac functional}

Let $Y$ be a closed Riemannian spin ${ }^{c}$ 3-manifold and $\eta$ a closed 2-form on $Y$ of class $C^{1}$. Fix a smooth reference spin connection $B_{o}$ over $Y$ and for any configuration $(B, \Psi)$ over $Y$ define the Chern-Simons-Dirac functional $\vartheta=\vartheta_{\eta}$ by
$$\vartheta(B, \Psi)=-\frac{1}{2} \int_{Y}\left(\hat{F}_{B}+\hat{F}_{B_{o}}+2 i \eta\right) \wedge\left(B-B_{o}\right)-\frac{1}{2} \int_{Y}\left\langle\partial_{B} \Psi, \Psi\right\rangle .$$
Here and elsewhere $\langle\cdot, \cdot\rangle$ denotes Euclidean inner products, while $\langle\cdot, \cdot\rangle_{\mathbb{C}}$ denotes Hermitian inner products. Note that reversing the orientation of $Y$ changes the sign of $\vartheta$. Let $\mathcal{C}=\mathcal{C}_{Y}$ denote the space of $L_{1}^{2}$ configurations $(B, \Psi)$. Then $\vartheta$ defines a smooth map $\mathcal{C}_{Y} \rightarrow \mathbb{R}$ which has an $L^{2}$ gradient
$$\nabla \vartheta_{(B, \Psi)}=\left(*\left(\hat{F}_{B}+i \eta\right)-\frac{1}{2} \sigma(\Psi, \Psi),-\partial_{B} \Psi\right) .$$
If $\left\{a_{j}\right\}$ is a local orthonormal basis of imaginary-valued 1-forms on $Y$ then
$$\sigma(\phi, \psi)=\sum_{j=1}^{3}\left\langle a_{j} \phi, \psi\right\rangle a_{j} .$$
Here and elsewhere the inner products are Euclidean unless otherwise specified. Since $\nabla \vartheta$ is independent of $B_{o}, \vartheta$ is independent of $B_{o}$ up to additive constants. If $u: Y \rightarrow \mathrm{U}(1)$ then
$$\vartheta(u(S))-\vartheta(S)=\int_{Y}\left(\hat{F}_{B}+i \eta\right) \wedge u^{-1} d u=2 \pi \int_{Y} \widetilde{\eta} \wedge[u]$$
where $[u] \in H^{1}(Y)$ is the pull-back by $u$ of the fundamental class of U(1), and $\widetilde{\eta}$ is as in (2).

The invariance of $\vartheta$ under null-homotopic gauge transformations imply
$$\mathcal{I}_{\Psi}^{*} \nabla \vartheta_{(B, \Psi)}=0 .$$
Let $H_{(B, \Psi)}: L_{1}^{2} \rightarrow L^{2}$ be the derivative of $\nabla \vartheta: \mathcal{C} \rightarrow L^{2}$ at $(B, \Psi)$, ie
$$H_{(B, \Psi)}(b, \psi)=\left(* d b-\sigma(\Psi, \psi),-b \Psi-\partial_{B} \psi\right) .$$
Note that $H_{(B, \Psi)}$ is formally self-adjoint, and $H_{(B, \Psi)} \mathcal{I}_{\Psi}=0$ if $\partial_{B} \Psi=0$. As in [15], a critical point $(B, \Psi)$ of $\vartheta$ is called non-degenerate if the kernel of $\mathcal{I}_{\Psi}^{*}+H_{(B, \Psi)}$ in $L_{1}^{2}$ is zero, or equivalently, if $\mathcal{I}_{\Psi}+H_{(B, \Psi)}: L_{1}^{2} \rightarrow L^{2}$ is surjective. Note that if $\eta$ is smooth then any critical point of $\vartheta_{\eta}$ has a smooth representative.

Let $\mathcal{G}$ be the Hilbert Lie group of $L_{2}^{2}$ maps $Y \rightarrow \mathrm{U}(1)$, and $\mathcal{G}_{0} \subset \mathcal{G}$ the subgroup of null-homotopic maps. Set
$$\mathcal{B}=\mathcal{C} / \mathcal{G}, \quad \widetilde{\mathcal{B}}=\mathcal{C} / \mathcal{G}_{0} .$$
Then $\vartheta$ descends to a continuous map $\widetilde{\mathcal{B}} \rightarrow \mathbb{R}$ which we also denote by $\vartheta$. If Condition (O1) holds (which we always assume when no statement to the contrary is made) then there is a real number $q$ such that
$$\vartheta(\mathcal{G} S)=\vartheta(S)+q \mathbb{Z}$$
for all configurations $S$. If (O1) does not hold then $\vartheta(\mathcal{G} S)$ is a dense subset of $\mathbb{R}$.

If $S$ is any smooth configuration over a band $(a, b) \times Y$, with $a<b$, let $\nabla \vartheta_{S}$ be the section of the bundle $\pi_{2}^{*}\left(\mathbb{S}_{Y} \oplus i \Lambda_{Y}^{1}\right)$ over $(a, b) \times Y$ such that $\left.\nabla \vartheta_{S}\right|_{\{t\} \times Y}=$ $\nabla \vartheta_{S_{t}}$. Here $\pi_{2}: \mathbb{R} \times Y \rightarrow Y$ is the projection. Note that $S \mapsto \nabla \vartheta_{S}$ extends to a smooth map $L_{1}^{2} \rightarrow L^{2}$.

Although we will normally work with $L_{1}^{2}$ configurations over $Y$, the following lemma is sometimes useful.

Lemma $3.1 \vartheta$ extends to a smooth function on the space of $L_{1 / 2}^{2}$ configurations over $Y$.

Proof The solution to the Dirichlet problem provides bounded operators
$$E: L_{1 / 2}^{2}(Y) \rightarrow L_{1}^{2}\left(\mathbb{R}_{+} \times Y\right)$$
such that, for any $f \in L_{1 / 2}^{2}(Y)$, the function $E f$ restricts to $f$ on $\{0\} \times Y$ and vanishes on $(1, \infty) \times Y$, and $E f$ is smooth whenever $f$ is smooth. (see [31, p 307]). Similar extension maps can clearly be defined for configurations over $Y$. The lemma now follows from the observation that if $S$ is any smooth configuration over $[0,1] \times Y$ then
$$\vartheta\left(S_{1}\right)-\vartheta\left(S_{0}\right)=\int_{[0,1] \times Y}\left\langle\nabla \vartheta_{S}, \frac{\partial S}{\partial t}\right\rangle,$$
and the right hand side extends to a smooth function on the space of $L_{1}^{2}$ configurations $S$ over $[0,1] \times Y$. \(\square\)

We will now relate the Chern-Simons-Dirac functional to the 4-dimensional monopole equations, cf [21, 28]. Let $X$ be a spin ${ }^{c}$ Riemannian 4-manifold.