# Geography of 4-manifolds with positive scalar curvature

- Category: papers
- Identity: arxiv:2105.12162
- Content status: fulltext_ok

---

---
source_file: 2105_12162.pdf
converter: mathpix
format: mmd
---

\title{
GEOGRAPHY OF 4-MANIFOLDS WITH POSITIVE SCALAR CURVATURE
}

\author{
AGNESE MANTIONE AND RAFAEL TORRES
}

\begin{abstract}
We discuss the geography problem of closed oriented 4-manifolds that admit a Riemannian metric of positive scalar curvature, and use it to survey mathematical work employed to address Gromov's observation that manifolds with positive scalar curvature tend to be inessential by focusing on the four-dimensional case. We also point out an strengthening of a result of Carr and its extension to the non-orientable realm.
\end{abstract}

\section*{1. Introduction}

The geography problem of 4-manifolds with positive scalar curvature for a group $G$ consists of determining the sets
$$\mathcal{G}_{>0}^{\dagger}(G)=\left\{(\chi(M), \sigma(M)): M \in \mathcal{M}_{>0}^{\dagger}(G)\right\},$$
where $\chi(M)$ is the Euler characteristic, $\sigma(M)$ is the signature, and $\mathcal{M}_{>0}^{\dagger}(G)$ is the set of closed smooth oriented 4-manifolds $M$ whose fundamental group is isomorphic to $G$, with † specifying its $w_{2}$-type, and that admit a Riemannian metric ( $M, g$ ) of strictly positive scalar $\operatorname{curvature~}^{\operatorname{scal}_{g}(p)>0}$ for every point $p \in M$. An orientable 4-manifold $M$ has $w_{2}$-type (I) and $\dagger=1$ if $w_{2}(\widetilde{M}) \neq 0, w_{2}$-type (II) and $\dagger=2$ if $w_{2}(M)=0$, and $w_{2}$-type (III) and $\dagger=3$ if $w_{2}(M) \neq 0$ and $w_{2}(\widetilde{M})=0$, where $\widetilde{M}$ is the universal cover of $M$ [14]. There is a division of the set of closed smooth oriented 4-manifolds
$$\mathcal{M}_{>0}(G)=\mathcal{M}_{>0}^{1}(G) \cup \mathcal{M}_{>0}^{2}(G) \cup \mathcal{M}_{>0}^{3}(G),$$
and the aforementioned geography problem becomes the computation of the set
$$\mathcal{G}_{>0}(G)=\mathcal{G}_{>0}^{1}(G) \cup \mathcal{G}_{>0}^{2}(G) \cup \mathcal{G}_{>0}^{3}(G) .$$
Given an element $\alpha \in H_{4}(G)=H_{4}(B G ; \mathbb{Q})$, let $\mathcal{M}_{>0}^{\dagger}(G, \alpha)$ be the set of pairs $(M, f)$ for $M \in \mathcal{M}_{>0}^{\dagger}(G)$ with reference map $f: M \rightarrow B G$ into the corresponding Eilenberg-MacLane space inducing an isomorphism $f_{*}: \pi_{1}(M) \rightarrow G$ and such that $f_{*}([M])=\alpha$ for $\dagger=1,2,3$. Define
$$\mathcal{G}_{>0}^{\dagger}(G, \alpha):=\left\{(\chi(M), \sigma(M)):(M, f) \in \mathcal{M}_{>0}^{\dagger}(G, \alpha)\right\} ;$$
see [23, Section 2]. The set (1.1) consists of the union of the sets (1.4) for $\alpha \in H_{4}(G)$.
We consider some refinements adapted to our purposes of the classic Hausmann-Weinberger invariant [18, §1]
$$q_{>0}^{\dagger}(G):=\min \left\{\chi(M): M \in \mathcal{M}_{>0}^{\dagger}(G)\right\}$$
and
$$q_{>0}(G):=\min \left\{q_{>0}^{\dagger}(G): \dagger=1,2,3\right\}$$

\footnotetext{
2020 Mathematics Subject Classification. 57M50, 53C21, 57R19.
}
as done by Kirk-Livingston [23, Definition 3.3]. We define
$$q_{>0, \alpha}^{\dagger}(G, \sigma):=\min \left\{\chi(M):(M, f) \in \mathcal{M}_{>0}^{\dagger}(G, \alpha) \text { and } \sigma(M)=\sigma\right\}$$
and
$$q_{>0, \alpha}(G, \sigma):=\min \left\{q_{>0, \alpha}^{\dagger}(G, \sigma): \dagger=1,2,3\right\}$$
by taking into account the signature and the reference map as done by Kotschick [24] and Kirk-Livingston [23, Definition 3.3].

In particular,
$$q_{>0}^{\dagger}(G)=\min \left\{q_{>0, \alpha}^{\dagger}(G, \sigma): \sigma \in \mathbb{Z}, \alpha \in H_{4}(G)\right\},$$
and
$$q_{>0}(G)=\min \left\{q_{>0, \alpha}^{\dagger}(G, \sigma): \sigma \in \mathbb{Z}, \alpha \in H_{4}(G), \dagger=1,2,3\right\},$$
and the invariant $q_{>0, \alpha}^{\dagger}(G, \sigma)$ determines $\mathcal{G}_{>0}^{\dagger}(G, \alpha)$ and viceversa for a given $w_{2}$ -type $\dagger=1,2,3$ [23, Theorem 3.4 Item (5)].

A closed orientable $n$-manifold $M$ with fundamental group $G=\pi_{1}(M)$ is said to be an essential manifold if $f_{*}([M]) \neq 0 \in H_{n}(G)$. An observation of Gromov is that manifolds that support a Riemannian metric of positive scalar curvature tend to be inessential. In this note, we address Gromov's observation for 4-manifolds in terms of the geography problem described before. We do so without involving Seiberg-Witten theory [9, §2.4]. The contribution (albeit modest) of this survey is to describe how work of Carr [3], Cecchini-Schick [4], Chodosh-Li [7], Gromov [10], Gromov-Lawson [12, 11, 13], Kirk-Livingston [23], Rosenberg [30, 31], Schick [34] and Schoen-Yau [36] turns the study of the geography problem of closed 4-manifolds with positive scalar curvature into a problem in group (co)homology and geometric group theory. We provide a stronger version to Carr's result in Theorem 6 and its extension to non-orientable manifolds in Theorem [7.

There are two canonical steps to study the geography problem, which are reviewed in Section 2 and Section 3. The first step is the construction of manifolds: a fundamental result of Gromov-Lawson and Schoen-Yau (Theorem 5) is used to construct a myriad of examples of 4-manifolds whose Euler characteristic and signature realize the sets (1.4) for $\alpha=0 \in H_{4}(G)$. In the same vein, we use a result due to Carr that shows that the fundamental group is not an obstruction to the existence of a metric of positive scalar curvature in Theorem 6. We state a stronger result than the one originally considered by Carr and compute some topological invariants of the manifolds. As a warm-up case of the first step, we now describe the geography and computation of the invariants that were introduced for the case of surface groups $G=\pi_{1}\left(\Sigma_{g}\right)$, where $\Sigma_{g}$ is a closed orientable surface of genus $g \in \mathbb{N}$.

Example 1. Geography problem of 4-manifolds with positive scalar curvature and fundamental group isomorphic to a non-trivial surface group. The Eilenberg-MacLane space for these groups is $B \pi_{1}\left(\Sigma_{g}\right)=\Sigma_{g}$ and
$$H_{4}\left(\pi_{1}\left(\Sigma_{g}\right) ; \mathbb{Q}\right)=H_{4}\left(B \pi_{1}\left(\Sigma_{g}\right) ; \mathbb{Q}\right)=H_{4}\left(\Sigma_{g} ; \mathbb{Q}\right)=0 .$$
Hence, $\alpha=0$ is the only case that needs to be considered. The total space $S^{2} \widetilde{\times} \Sigma_{g}$ of the non-trivial 2-sphere bundle over $\Sigma_{g}$ and the product $S^{2} \times \Sigma_{g}$ admit Riemannian
metrics of positive scalar curvature [39, 1.4 Observation]. The values of the modified Hausmann-Weinberger invariants are
$$\chi\left(S^{2} \times \Sigma_{g}\right)=q_{>0}^{2}\left(\pi_{1}\left(\Sigma_{g}\right)\right)=4-4 g=q_{>0}^{3}\left(\pi_{1}\left(\Sigma_{g}\right)\right)=\chi\left(S^{2} \widetilde{\times} \Sigma_{g}\right)$$
and $q_{>0}\left(\pi_{1}\left(\Sigma_{g}\right)\right)=4-4 g$ by a result of Kotschick [24]; see [23, Section 3]. An index theoretical obstruction due to Lichnerowicz and Schrödinger states that the signature of a closed orientable Riemannian 4-manifold $(M, g)$ with scalar curvature $\operatorname{scal}_{g}>0$ and second Stiefel-Whitney class $w_{2}(M)=0$ must satisfy $\sigma(M)=0$; see Theorem 1 and Section 2. Therefore, the identitities
$$q_{>0}^{2}\left(\pi_{1}\left(\Sigma_{g}\right), \sigma\right)=q_{>0}^{2}\left(\pi_{1}\left(\Sigma_{g}\right), 0\right)=q_{>0}^{2}\left(\pi_{1}\left(\Sigma_{g}\right)\right)=q_{>0}\left(\pi_{1}\left(\Sigma_{g}\right)\right)$$
hold. By taking a connected sum $M_{2 k+2}:=S^{2} \times \Sigma_{g} \# k\left(S^{2} \times S^{2}\right)$ with $k \in \mathbb{N}$ copies of the product of two round 2-spheres we obtain a closed simply connected 4-manifold with a Riemannian metric of positive scalar curvature, $w_{2}\left(M_{2 k+2}\right)=0$, Euler characteristic $\chi\left(M_{2 k+2}\right)=4-4 g+2 k$, and signature $\sigma\left(M_{2 k+2}\right)=0$. A fundamental result of Gromov-Lawson and Schoen-Yau states that the existence of a Riemannian metric with positive scalar curvature is a property that is closed under connected sums; see Theorem 5. We conclude that
$$\mathcal{G}_{>0}^{2}\left(\pi_{1}\left(\Sigma_{g}\right)\right)=\left\{(4-4 g+2 k, 0): k \in \mathbb{Z}_{\geq 0}\right\}=\mathcal{G}_{>0}^{2}\left(\pi_{1}\left(\Sigma_{g}\right), 0\right) .$$

The scenario in the case of non-zero second Stiefel-Whitney class is addressed analogously by taking connected sums with the complex projective plane $\mathbb{C P}^{2}$ equipped with the Fubini-Study metric and the underlying 4-manifold taken with the opposite orientation $\overline{\mathbb{C P}^{2}}$. Gromov-Lawson's and Schoen-Yau's result implies that the connected sum $M_{a, b}:=S^{2} \widetilde{\times} \Sigma_{g} \# a\left(\mathbb{C P}^{2}\right) \# b\left(\overline{\mathbb{C P}^{2}}\right)$ admits a Riemannian metric of positive scalar curvature. We have that
$$q_{>0}\left(\pi_{1}\left(\Sigma_{g}\right), \sigma\right)=4-4 g+|\sigma|$$
and
$$\mathcal{G}_{>0}\left(\pi_{1}\left(\Sigma_{g}\right)\right)=\{(4-4 g+|k|, k): k \in \mathbb{Z}\} .$$

The second step in the study of the geography problem is based on three fundamental obstruction techniques, and its goal is to show that the sets (1.4) are empty for $\alpha \neq 0 \in H_{4}(G)$. We now briefly mention these techniques focusing on dimension four, and we recall them in further detail in Section 2. We start with an index theoretical technique that has arguably attracted the most attention of researchers through the years. Rosenberg [30], [31, Section 1.1.1] employed the $C^{*}$-algebraic index of the Dirac operator on a closed orientable manifold with zero Stiefel-Whitney class. For an essential 4-manifold $M$ with second Stiefel-Whitney class $w_{2}(M)=0$, his result imposes restrictions on the sets (1.4) and (1.1); see Theorem 2. These results yield the following theorem.

Theorem A. Let $G$ be a finitely presented group whose first and second Betti numbers satisfy
$$b_{1}(G)-b_{2}(G)=\operatorname{def}(G),$$
where $\operatorname{def}(G)$ is its deficiency. Suppose that $G$ satisfies the strong Novikov conjecture.

The sets $\mathcal{G}_{>0}^{2}(G, \alpha)$ are empty for every $\alpha \neq 0$, we have that
$$\mathcal{G}_{>0}^{2}(G)=\{(2-2 \operatorname{def}(G)+2|k|, 0): k \in \mathbb{Z}\}=\mathcal{G}_{>0}^{2}(G, 0),$$
and the values of the modified Hausmann-Weinberger invariants are
$$q_{>0}^{2}(G)=2-2 \operatorname{def}(G)=q_{>0,0}^{2}(G, 0) .$$

Rosenberg's result and the strong Novikov conjecture are briefly recalled in Section 2. Gromov-Lawson introduced a method to make use of the index of the Dirac operator to obstruct positive scalar curvature through the notion of an enlargeable manifold in [12]. While their techniques where originally deployed for orientable manifolds with $w_{2}=0$, they dropped this hypothesis condition in [13]; cf. Cecchini-Schick [4].

Schoen-Yau's stable minimal surface technique [36] does not make any assumption on the second Stiefel-Whitney class, and it has proven to be a powerful obstruction technique provided that the manifold and its fundamental group satisfy the following property.

Definition 1. A group $G$ satisfies Property NPSC if $H^{1}(G ; \mathbb{Z})=\mathbb{Z}^{s}$ for $s \geq 2$ with generators $\left\{\theta_{1}, \theta_{2}\right\}$ that satisfy
$$\theta_{1} \cap \theta_{2} \cap f_{*}([M]) \neq 0 \in H_{2}(B G ; \mathbb{Z})$$
for $f: M \rightarrow B G$ the reference map of a closed orientable 4-manifold $M$ with $\pi_{1}(M)=G$.

Section 2 contains further details on minimal stable hypersurfaces and the formal obstruction to the existence of a metric of positive scalar curvature that arises from them as observed by Schick [34]; see Theorem 4 . We show in Example 2 that right-angled Artin groups satisfy Property NPSC.

A central conjecture in the study of geometry and topology of Riemannian manifolds of positive scalar curvature states that a closed aspherical $n$-manifold does not admit such a metric. The case $n=2$ corresponds to the Gauss-Bonnet theorem and the case $n=3$ has been proven by Gromov-Lawson [12, 11, 13] and Schoen-Yau [36, 35] along with grounbreaking results of Perelman [27, 29, 28]. Schoen-Yau proposed a strategy for the case $n=4$ in [37, Theorem 6] and Chodosh-Li followed Schoen-Yau's strategy showed that a closed aspherical 4-manifold does not admit a Riemannian metric of positive scalar curvature [7, Theorem 2] using generalized soap bubbles: submanifolds that are stationary for prescribed mean-curvature functionals. We point out in Lemma 2 that recent work of Gromov [10, Main Theorem] and Chodosh-Li [7, Theorem 2] regarding non-existence of Riemannian metrics of positive scalar curvature on closed aspherical 5-manifolds implies the corresponding statement on certain essential 4-manifolds.

An application of the stable minimal hypersurfaces, enlargeability and generalized soap bubbles methods yield the following result.

Theorem B. Let $G$ be a finitely presented group whose first and second Betti numbers satisfy
$$b_{1}(G)-b_{2}(G)=\operatorname{def}(G),$$
where $\operatorname{def}(G)$ is its deficiency. Suppose that either
\begin{itemize}
\item[-] $H_{4}(G)=0$,
\item[-] G satisfies Property NPSC of Definition 1 or
\item[-] $G$ is the fundamental group of a closed orientable aspherical 4-manifold.
\end{itemize}

The sets (1.4) are empty for every $\alpha \neq 0$. We have that
$$\mathcal{G}_{>0}(G)=\{(2-2 \operatorname{def}(G)+|k|, k): k \in \mathbb{Z}\}$$
and
$$\mathcal{G}_{>0}^{2}(G)=\{(2-2 \operatorname{def}(G)+2|k|, 0): k \in \mathbb{Z}\}$$
The values of the modified Hausmann-Weinberger invariants are
$$q_{>0}(G)=2-2 \operatorname{def}(G)=q_{>0,0}(G, 0)$$
and
$$q_{>0,0}(G, \sigma)=|\sigma|+2-2 \operatorname{def}(G)=q_{>0}(G, \sigma) .$$

A list of groups that satisfy the hypothesis of Theorem B includes right-angled Artin groups, Thompson's group, knot and 3-manifold groups, products of surface groups, several 2-knot and super perfect groups, solvable Baumslag-Solitar groups, and fundamental groups of Riemannian 4-manifolds whose sectional curvature is nonpositive. The last result that we mention samples how the geography problem of 4-manifolds with positive scalar curvature can be solved for several groups that do not satisfy Hypothesis (1.21).

Proposition C. Suppose $\operatorname{gcd}(p, q) \neq 1$ and let
$$G_{p, q}=\left\langle x, y: x^{p}=y^{q}=[x, y]=1\right\rangle=\mathbb{Z} / p \oplus \mathbb{Z} / q .$$
The identities
$$q_{>0}\left(G_{p, q}\right)=2=q_{>0}^{2}\left(G_{p, q}\right)$$
and
$$q_{>0,0}\left(G_{p, q}, \sigma\right)=2+|\sigma|$$
hold. Moreover,
$$\mathcal{G}_{>0}\left(G_{p, q}\right)=\left\{(2+|k|, k): k \in \mathbb{Z}_{\geq 0}\right\}$$
and
$$\mathcal{G}_{>0}^{2}\left(G_{p, q}\right)=\left\{(2 k+2,0): k \in \mathbb{Z}_{\geq 0}\right\}=\mathcal{G}_{>0,0}^{2}\left(G_{p, q}, 0\right) .$$

The requirement $\operatorname{gcd}(p, q) \neq 1$ guarantees that the group (1.26) is not cyclic. None of the groups (1.26) satisfy Hypothesis (1.21) since their deficiency is -1.

We finish this introduction by mentioning that the geography problem of closed orientable 4-manifolds for a group $G$ and the Hausmann-Weinberger invariant themselves have not been determined except for a handful of groups; see Hausmann-Weinberger [18], Hildum [19], Kirk-Livingston [22, 23], Kotschick [24].
1.1. Acknowledgements: We thank the referee for her/his detailed referee report, which helped us improve the manuscript. R. T. thanks Thomas Schick for useful e-mail correspondence. We are happy to join the long list of mathematicians that express their gratitude to Misha Gromov for the wonderful mathematics throughout the years.

\section*{2. Obstructions to the existence of a Riemannian metric of positive scalar curvature}

The Dirac operator $D$ on sections of the spinor bundle $S \rightarrow M$ of an orientable Riemannian 4-manifold $(M, g)$ with second Stiefel-Whitney class $w_{2}(M)=0$ yields the Bochner-Lichnerowicz-Weitzenböck formula
$$D^{2}=\nabla^{*} \nabla+\frac{1}{4} \operatorname{scal}_{g}$$
where ∇ is the connection on $S, \nabla^{*}$ its adjoint, and $\nabla^{*} \nabla$ is the connection Laplacian [25, Chapter II]. The formula (2.1), due to work of Lichnerowicz [26] and Schrödinger [38], indicates that the scalar curvature scal ${ }_{g}$ is both an obstruction for $D$ to be the square root operator of the Laplacian, and an error term that arises when the identity $D^{2}=\nabla^{*} \nabla$ is extended from the flat to the curved case.

The formula (2.1) states that a necessary condition for $\operatorname{scal}_{g}>0$ is that the kernel of the Dirac operator must be trivial and its index must vanish. The Atiyah-Singer Index Theorem [25, Theorem 13.10, Chapter III] allows us to phrase this obstruction in terms of a rational Pontrjiagyn number of $M$ known as the $\hat{A}$-genus 25, §8 Chapter II, §11 Chapter III].
Theorem 1. Lichnerowicz [26], Schrödinger [38]. Let $(M, g)$ be a closed orientable Riemannian 4-manifold with second Stiefel-Whitney class $w_{2}(M)=0$. If $\operatorname{scal}_{g}>0$, then $\hat{A}(M)=0$.

Hirzebruch's signature theorem [9, Theorem 1.4.12] relates the $\hat{A}$-genus with the signature of the 4-manifold $M$ by $\hat{A}(M)=-\frac{1}{8} \sigma(M)$. In particular, the signature of a closed orientable Riemannian 4-manifold $(M, g)$ with $\operatorname{scal}_{g}>0$ is zero.

We now briefly discuss a refinement of the $\hat{A}$-genus studied by Hitchin [20] and Rosenberg [30] that take into account the fundamental group of the manifold through the corresponding Eilenberg-MacLane space. Let $[M, f] \in \Omega_{n}^{\text {Spin }}(B G)$ be the Spin-bordism class of the pair $(M, f)$ where $f: M \rightarrow B G$, and and let $C_{r}^{*}(G)$ be the reduced $C^{*}$-algebra of the discrete group $G$. An invariant $\alpha(M) \in K O_{n}\left(C_{r}^{*}(G)\right)$ is defined as the image of the fundamental class $[M, f] \in \Omega^{\operatorname{Spin}}(B G)$ under the map of generalized homology theories
$$\Omega_{*}^{\mathrm{Spin}}(B G) \xrightarrow{D} k o_{*}(B G) \xrightarrow{\text { per }} K O_{*}(B G) \xrightarrow{A} K O_{n}\left(C_{r}^{*}(G)\right),$$
where $k o_{*}(B G)$ and $K O_{*}(B G)$ are the periodic and connective real K-homology of the Eilenberg-MacLane space $B G$, respectively. That is,
$$\alpha(M):=\alpha([M, f])=A \circ \operatorname{per} \circ D([M, f])=0 \in K O_{n}\left(C_{r}^{*}(G)\right) .$$
The invariant (2.3) only depends on the bordism class $[M, f]$. For further details, we direct the reader towards the well-known surveys of Hanke [15], Rosenberg [31], Section 1.1.1], the chapter of Rosenberg-Stolz [32], the lectures of Stolz [39], and the book Lawson-Michelsohn [25, Chapters II, III and IV].

One of the fundamental results in obstructive results to positive scalar curvature is due to Rosenberg. He showed that the vanishing of the invariant (2.3) is a necessary condition for the existence of a Riemannian metric of positive scalar curvature.

Theorem 2. Rosenberg [30]. Let $M$ be a closed orientable $n$-manifold with second Stiefel-Whitney class $w_{2}(M)=0$. If there is a Riemannian metric $(M, g)$ whose scalar curvature satisfies $\operatorname{scal}_{g}>0$, then $A \circ$ per $\circ D([M, f])=0 \in K O_{n}\left(C_{r}^{*}(G)\right)$.

If the group $G$ satisfies the Strong Novikov Conjecture, i.e., if the assembly map
$$A: K O_{*}(B G) \rightarrow K O_{*}\left(C_{r}^{*}(G)\right)$$
in (2.2) is injective, then per $\circ D([M, f])=0 \in K O_{n}(B G)$ in the presence of a Riemannian metric $(M, g)$ with $\operatorname{scal}_{g}>0$.

Theorem 2 and the injectivity of the map (2.4) shift focus onto manifolds whose fundamental classes have nontrivial images in $k o_{n}(B G)$ and $K O_{n}(B G)$. An essential 4-manifold satisfies $\left.f_{*}\left([M]_{K}\right) \neq 0 \in K_{n}(B G)\right) \otimes \mathbb{Q}$, where $[M]_{K} \in K_{n}(M)$ is the $K$-theoretical fundamental class of $M$; see [15, Definition 2.5]. Indeed, every orientable 4-manifold admits a Spin ${ }^{\text {C }}$-structure and the homological Chern character isomorphism $c h: K_{n}(M) \otimes \mathbb{Q} \rightarrow H_{n}(M ; \mathbb{Q})$ in this case yields $c h\left([M]_{K}\right)=[M]+c$ for $c \in H_{i}(M ; \mathbb{Q})$ with $i \leq n$, and $[M]$ is the fundamental class of $M$ in singular homology; see [15, Page 284], [16, Section 4]. If the second Stiefel-Whitney class of an essential n-manifold $M$ with fundamental group $G$ is zero, then the fundamental class of $M$ in connective $K O$-homology $[M]_{k o}:=D([M, \mathrm{id}]) \in k o_{n}(B G)$ is nonzero; cf. [39, Section 2.10], [1, 3.3 Proposition]. Similarly, an essential $n$-manifold $M$ with $w_{2}(M)=0$ yields a nontrivial fundamental class in periodic $K O$-homology per $\left.\circ D([M, f])=f_{*}\left([M]_{K O}\right]\right) \neq 0 \in K O_{n}(B G)$. We conclude that Theorem 2 has the following implication.

Proposition 1. Let $M$ be an essential $n$-manifold and suppose $w_{2}(M)=0$. If the fundamental group $\pi_{1}(M)$ satisfies the Strong Novikov Conjecture, then $M$ does not admit a Riemannian metric of positive scalar curvature.

Gromov-Lawson [12] introduced the concept of enlargeability to employ the role of the fundamental group to obstruct positive scalar curvature. Recall that a closed orientable Riemannian $n$-manifold $(M, g)$ is enlargeable if for every $\epsilon>0$, there is a Riemannian cover $\hat{M} \rightarrow M$ and an $\epsilon$-contracting map $\hat{M} \rightarrow S^{n}(1)$ to the unit $n$-sphere that is constant outside a compact subset and of non-zero degree. The reader is referred to [11, 13] for details.

Theorem 3. Gromov-Lawson [11, Theorem A], [13, Section 12], Cecchini-Schick [4, Theorem A], Schoen-Yau [36]. Suppose $M$ is an enlargeable $n$-manifold with $n \leq 8$. There is no Riemannian metric $(M, g)$ such that $\operatorname{scal}_{g}>0$.

When coupled with other interesting results, Theorem 3 poses constrains on the homotopy types of manifolds of positive scalar curvature in terms of their classifying map. A result of Hanke-Schick implies that $M$ is an essential $n$-manifold whenever $M$ is a closed oriented enlargeable $n$-manifold [17, Theorem 5.1]. The converse of such statement does not hold: Brunnbauer-Hanke have constructed examples of essential $n$-manifolds that are not enlargeable for $n \geq 4$ in [2, Theorem 1.5].

The minimal stable hypersurfaces machinery of Schoen-Yau is a powerful obstruction to the existence of a metric of positive scalar curvature [36, Proof of Theorem 1]. The setting is as follows. Suppose $M$ is a closed oriented $n$-manifold with $H^{1}(M ; \mathbb{Z}) \neq 0$ and $3 \leq n \leq 7$, and suppose $N \subset M$ is a closed stable minimal hypersurface such that its homology class $[N] \neq 0 \in H_{n-1}(M ; \mathbb{Z})$ is dual to a nonzero class in the first cohomology group. If there is a Riemannian metric $(M, g)$ with $\operatorname{scal}_{g}>0$, then there is a Riemannian metric of positive scalar curvature on the hypersurface $N$ within the conformal class of the induced metric.

Schick observed that iterations of Schoen-Yau's results on sequences of stable minimal hypersurfaces provides the following formal obstruction [34, §1]. We denote
by $H_{m}^{+}(X ; \mathbb{Z})$ the subset of the mth-homology group $H_{m}(X ; \mathbb{Z})$ of any space $X$ that consists of classes $f_{*}([M])$ where $f: M \rightarrow X$ for $(M, g)$ that satisfies $\operatorname{scal}_{g}>0$.

Theorem 4. Schick 34, Corollary 1.5]. Let $X$ be any space and $\theta \neq 0 \in H^{1}(X ; \mathbb{Z})$. The cap product with $\theta$ induces a map
$$\theta \cap: H_{m}(X ; \mathbb{Z}) \rightarrow H_{m-1}(X ; \mathbb{Z})$$
that sends
$$H_{m}^{+}(X ; \mathbb{Z}) \rightarrow H_{m-1}^{+}(X ; \mathbb{Z})$$
for $3 \leq m \leq 7$.
The well-known necessary conditions for enlargeability [12, Corollary C], [13, §5], [25, Theorem 5.3, Theorem 5.4] along with Theorem 3 along Theorem 4 yield the following result.

Proposition 2. Let $M$ be an essential $n$-manifold. Suppose that the fundamental group $\pi_{1}(M)=G$ either satisfies Property NPSC of Definition 1 or that it is isomorphic to the fundamental group of a closed orientable Riemannian 4-manifold $(N, g)$ of nonpositive sectional curvature. There is no Riemannian metric on $M$ of positive scalar curvature. In particular, the set
$$\mathcal{G}_{>0}(G, \alpha)=\mathcal{G}_{>0}^{1}(G, \alpha) \sqcup \mathcal{G}_{>0}^{2}(G, \alpha) \sqcup \mathcal{G}_{>0}^{3}(G, \alpha)$$
is empty for every $\alpha \neq 0 \in H_{4}(G)$.
Proof. The proof of Proposition 2 in the case of a group $G$ that satisfies Property NPSC is due to Schick [34, §2]; see Theorem 4. Let $f: M \rightarrow B G$ be the reference map into the classifying space $B G$. The universal coefficient theorem implies that the induced map on cohomology $f^{*}: H^{1}(G) \rightarrow H^{1}(M ; \mathbb{Z})$ is an isomorphism given that the induced map in homology $f_{*}: H_{1}(M ; \mathbb{Z}) \rightarrow H_{1}(G)$ is an isomorphism. Hence, $H^{1}(M ; \mathbb{Z})=\mathbb{Z}^{s}$ for $s \geq 2$ and we have generators $\left\{\theta_{1}, \theta_{2}\right\}$ that satisfy $\left.\theta_{1} \cap \theta_{2} \cap f_{*}(M]\right) \neq 0 \in H_{2}(B G ; \mathbb{Z})$. We employ Schoen-Yau's stable minimal hypersurfaces method [36] and proceed by contradiction. Suppose there is a metric of positive scalar curvature $(M, g)$ and $f_{*}([M])=\alpha \neq 0 \in H_{4}(B G)=H_{4}(G)$. This implies that there is a non-trivial element in $H_{4}^{+}(B G)$. A pair of applications of Theorem 4 implies the existence of an element $a \neq 0 \in H_{2}^{+}(B G)$. However, the only closed oriented 2-manifold that admits a metric of positive scalar curvature is the 2 -sphere, and any map $g: S^{2} \rightarrow B G$ is nullhomotopic since the second homotopy group of the Eilenberg-MacLane space $B G$ is trivial. We then have that $g_{*}\left(\left[S^{2}\right]\right)=0 \in H_{2}(B G)$ and $H_{2}^{+}(B G)=0$. Therefore, we conclude that a closed oriented 4-manifold $M$ whose fundamental group has non-trivial first cohomology group and $f_{*}([M]) \neq 0 \in H_{4}(G)$ does not admit a Riemannian metric of positive scalar curvature.

We now argue the case where $\pi_{1}(M)=\pi_{1}(N)$ for a closed orientable Riemannian 4 -manifold $\left(N, g_{N}\right)$ with $\sec _{g_{N}} \leq 0$. The 4 -manifold $N$ is enlargeable by [12, 13]; cf. [25, Theorem 5.4]. The Hadamard-Cartan theorem implies that the universal cover $\widetilde{N}=\mathbb{R}^{n}$ is contractible and $N$ is an aspherical 4-manifold. Therefore, the Eilenberg-MacLane space is $B \pi_{1}(M)=N$. If $f_{*}([M]) \neq 0 \in H_{4}\left(B \pi_{1}(M)\right)=H_{4}(N)$, there is a non-zero degree map $f: M \rightarrow N$ and $M$ is an enlargeable 4-manifold by [12, 13], [25, Theorem 5.3]. Theorem 3 implies that there is no metric on $M$ with positive scalar curvature and the set (2.7) is empty for every $\alpha \neq 0 \in H_{4}(N)$. \(\square\)

Theorem 4 is particularly efficient on essential manifolds whose fundamental group is a right-angled Artin group (RAAG).

Example 2. RAAG's with non-zero fourth homology group satisfy Property NPSC of Definition 1. A right-angled Artin group is a group with a presentation
$$G=\left\langle g_{1}, \ldots, g_{s}: g_{i} g_{j}=g_{j} g_{i} \forall i \neq j\right\rangle .$$
The presentation (2.8) is specified by a defining graph $\Gamma$, whose vertices are labelled by the generators $\left\{g_{1}, \ldots, g_{s}\right\}$ and an edge of $\Gamma$ that connects two of them $g_{i}$ and $g_{j}$ exists if and only if $g_{i} g_{j}=g_{j} g_{i}$; see the survey article of Charney [5] for further details on these groups. The Eilenberg-MacLane space $B G$ is the Salvetti complex 33 [5, Section 3.6], and Charney-Davis used it to compute its cohomology ring in [6]. The chain complex of $B G$ injects into the chain complex of a $k$-torus and given that all chain and cochain maps in the chain complex of a torus are zero, the only nontrivial cup products in the cohomology ring $H^{*}(G)$ arise from the commuting generators in the presentation (2.8); see [5, 6, 19]. The vertices of $\Gamma$ represent generators $\left\{\gamma_{1}, \ldots, \gamma_{s}\right\}$ of $H^{1}(G)=H^{1}(B G)$ while its edges represent generators of $H^{2}(G)=H^{2}(B G)$ that arise as cup products $\gamma_{i} \cup \gamma_{j}$. Hence, $b_{1}(G)$ is equal to the number of vertices of $\Gamma$ and $b_{2}(G)$ is equal to the number of edges. In more generality, a subgraph of order $k$, known as a $k$-clique, represents the generators of $H^{k}(G)$ and these arise as cup products of $k$ generators of the first cohomology group of $G$. The $k$ th Betti number $b_{k}(G)$ equals the number of $k$-cliques. Regarding the fourth cohomology group, a 4-clique of $\Gamma$ represents the generators of $H^{4}(G)$, which arise as cup products $\gamma_{i_{1} i_{2} i_{3} i_{4}}:=\gamma_{i_{1}} \cup \gamma_{i_{2}} \cup \gamma_{i_{3}} \cup \gamma_{i_{4}}$ and a non-zero element $g_{i_{1} i_{2} i_{3} i_{4}} \neq 0 \in H_{4}(G)$ satisfies $\left\langle g_{i_{1} i_{2} i_{3} i_{4}}, \gamma_{i_{1} i_{2} i_{3} i_{4}}\right\rangle=\delta_{l_{1}, l_{2}}$; interesting examples of graphs can be found in a paper of Hildum [19].

Given an essential 4-manifold whose fundamental group $G$ is a right-angled Artin group, we have that $H_{4}(G) \neq 0$ and there is a 4-clique in the defining graph $\Gamma$. This implies that we can choose elements $\gamma_{1}, \gamma_{2} \in H^{1}(G)$ that correspond to commuting generators of (2.8) such that cap product $\gamma_{1} \cap \gamma_{2} \cap f_{*}([M])$ is equal to a non-zero cup product of elements $\gamma_{i}, \gamma_{j} \in H^{1}(G)$ for $f_{*}([M]) \neq 0 \in H_{4}(G)$; cf. [34, Example 2.2]. We conclude that a right-angled Artin group $G$ with $H_{4}(G) \neq 0$ satisfies the NPSC property of Definition 1.

The summarize this discussion as a lemma.
Lemma 1. An essential 4-manifold whose fundamental group is a right-angled Artin group does not admit a Riemannian metric of positive scalar curvature.

Chodosh-Li have shown that a closed aspherical 4-manifold does not admit a Riemannian metric of positive scalar curvature [7, Theorem 2] following a strategy of Schoen-Yau [37, Theorem 6]. Gromov has recently shown that an essential 5-manifold whose fundamental group is isomorphic to the fundamental group of a closed aspherical 5-manifold does not admit a Riemannian metric of positive scalar curvature. We conclude this section with the observation that Gromov's five-dimensional result has the following implication regarding essential 4-manifolds; cf. Chodosh-Li [7, Theorem 2].

Lemma 2. Let $M$ be an essential 4-manifold whose fundamental group is iso-morphic to the fundamental group of a closed orientable aspherical 4-manifold $M_{0}$. There is no Riemannian metric on $M$ of positive scalar curvature.

Proof. We proceed by contradiction and suppose that there is a Riemannian metric $(M, g)$ with scalar curvature $\operatorname{scal}_{g}>0$. This assumption implies that the product Riemannian 5-manifold $\left(M \times S^{1}, g+d \theta^{2}\right)$ has positive scalar curvature, and there is a non-zero degree map $f: M \times S^{1} \rightarrow M_{0} \times S^{1}$ to the aspherical 5-manifold $M_{0} \times S^{1}$. This is a contradiction by [10, Main Theorem]. We conclude that $M$ does not admit a Riemannian metric of positive scalar curvature. \(\square\)

\section*{3. Cut-and-Paste constructions, positive scalar curvature and PRESCRIBED FUNDAMENTAL GROUP}

The production of 4-manifolds that realize the invariant $q_{>0}(G)$ and that fully determine the set (2.7) is carried out by employing the following fundamental result.

Theorem 5. Gromov-Lawson [12, Theorem A], Schoen-Yau [36, Section 2]. Let $(M, g)$ be a compact Riemannian manifold with $\operatorname{scal}_{g}>0$. Any manifold that is obtained from $M$ by performing surgeries in codimension at least three also admits a Riemannian metric with positive scalar curvature.

Carr has shown that the fundamental group is not an obstruction for the existence of a Riemannian metric of positive scalar curvature for orientable manifolds of dimension four [3, Corollary 2]. His proof consists of constructing a manifold with a Riemannian metric of positive scalar curvature and prescribed finitely presented fundamental group as the boundary of a 2-complex embedded in $\mathbb{R}^{5}$. A different proof of Carr's result follows from the work of Kervaire [21] and Theorem 5. We state a strengthened version of Carr's result which include several topological properties of the manifolds involved that were not considered in [3].

Theorem 6. Let $G$ be a group with finite presentation
$$\left\langle g_{1}, \ldots, g_{s}: r_{1}, \ldots, r_{t}\right\rangle$$
and suppose $n \geq 4$. There exists a closed smooth stably-parallelizable $n$-manifold $M^{n}(G)$ such that
\begin{itemize}
\item[-] the fundamental group of $M^{n}(G)$ is isomorphic to $G$;
\item[-] if $n$ is even, the Euler characteristic is $\chi\left(M^{n}(G)\right)=2-2 \operatorname{def}(G)$ for $\operatorname{def}(G)=s-t$,
\item[-] there exists a Riemannian metric $\left(M^{n}(G), h\right)$ of positive scalar curvature $\mathrm{scal}_{h}>0$, and
\item[-] the classifying map $f: M^{n}(G) \rightarrow B G$ satisfies
\end{itemize}
$$f_{*}\left(\left[M^{n}(G)\right]\right)=0 \in H_{n}(B G) .$$

Both Carr's and Kervaire's constructions produce a closed stably parallelizable n-manifold equipped with a null bordism along with the classifying map (3.4). Such null bordism is the culprit for the existence of a metric of positive scalar curvature in terms of Theorem 3. Moreover, although the Euler class of $M^{n}(G)$ need not be zero, other characteristic numbers are trivial such as the signature of the 4-manifold $M^{4}(G)$. This 4-manifold realizes the modified Hausmann-Weinberger invariant $q_{>0}(G)$ in Theorem A and Theorem B under the assumption that the relation $b_{1}(G)-b_{2}(G)=\operatorname{def}(G)$ holds.

We comment on the proof of Theorem 6 in Remark 1, but we point out first that Theorem 5 makes it possible to extend Carr's result to non-orientable manifolds.

Theorem 7. Let $G$ be a group with finite presentation
$$\left\langle g_{1}, \ldots, g_{s}: r_{1}, \ldots, r_{t}\right\rangle$$
that contains a subgroup of index two, and suppose $n \geq 4$. There exists a closed smooth non-orientable $n$-manifold $N^{n}(G)$ such that
\begin{itemize}
\item[-] the fundamental group of $N^{n}(G)$ is isomorphic to $G$;
\item[-] if $n$ is even, the Euler characteristic is $\chi\left(M^{n}(G)\right)=2-2 \operatorname{def}(G)$ for $\operatorname{def}(G)=s-t$,
\item[-] there exists a Riemannian metric $\left(N^{n}(G), h\right)$ of positive scalar curvature $\mathrm{scal}_{h}>0$, and
\item[-] the classifying map $f: M^{n}(\tilde{G}) \rightarrow B \tilde{G}$ of the the orientation 2-cover $M^{n}(\tilde{G}) \rightarrow N^{n}(G)$ satisfies
\end{itemize}
$$f_{*}\left(\left[M^{n}(\tilde{G})\right]\right)=0 \in H_{n}(B \tilde{G}) .$$

The total space of the non-orientable $S^{n-1}$-bundle over the circle is denoted by $S^{n-1} \widetilde{\times} S^{1}$.

Proof. The first step is to construct a closed non-orientable Riemannian $n$-manifold $\left(X\left(F_{s}\right), g_{0}\right)$ with positive scalar curvature $\operatorname{scal}_{g_{0}}>0$ and a free fundamental group $\pi_{1}\left(X\left(F_{s}\right)\right)$ on $s$ generators, where $s$ is the number of generators in the presentation (3.3) of $G$. The fundamental group of the connected sum
$$X\left(F_{s}\right):=S^{n-1} \widetilde{\times} S^{1} \# S^{1} \times S^{n-1} \# \cdots \# S^{1} \times S^{n-1}$$
of the non-orientable $(n-1)$-sphere bundle with $s-1$ copies of $S^{1} \times S^{n-1}$ is the free group $\pi_{1}\left(X\left(F_{s}\right)\right)=F_{s}=\left\langle g_{1}, \ldots, g_{s}\right\rangle$ on $s$ generators. The claim that the fundamental group of $X_{s}$ is the free group on $s$ generators follows from the Seifert-van Kampen theorem under the assumption that $n \geq 3$. The hypothesis on the existence of a subgroup of index two of $G$ implies that $s \in \mathbb{N}$. The fixedpoint free orientation-reversing involution $S^{1} \times S^{n-1} \rightarrow S^{1} \times S^{n-1}$ that is given by $(\exp 2 \pi i \theta, x) \mapsto(-\exp 2 \pi i \theta,-x)$ is an isometry of the Riemannian product of canonical metrics ( $S^{1} \times S^{n-1}, d \theta^{2}+g_{S^{n-1}}$ ), and the scalar curvature of the latter is positive. We equip $S^{n-1} \widetilde{\times} S^{1}$ with the quotient metric, which has positive scalar curvature. Theorem 5 implies that there is a Riemannian metric of positive scalar curvature on the connected sum (3.5) for every $s$.

For each relation $r_{j}$ in the group presentation (3.3), take an embedded loop $\gamma_{j} \subset X\left(F_{s}\right)$ that represents the homotopy class that corresponds to $r_{j}$. This yields a set of embedded loops
$$\left\{\gamma_{1}, \ldots, \gamma_{r}\right\}$$
along a one-to-one assigment with the set $\left\{r_{1}, \ldots, r_{t}\right\}$ for relations in (3.3). Since an embedded loop has codimension at least two in the $n$-manifold (3.5), transversality guarantees that the set (3.6) consists of pairwise disjoint embedded loops $\gamma_{j} \subset X\left(F_{s}\right)$ for $j=1, \ldots, t$. The possible diffeomorphism type of the tubular neighborhoods of embedded loops in an $n$-manifold $M$ are collected in the following lemma; see [8, Chapter 5] for a definition of the orientation character homomorphism $\rho_{M}: \pi_{1}(M) \rightarrow \mathbb{Z} / 2$.

Lemma 3. Let $M$ be a smooth $n$-manifold and $\gamma \subset M$ be an embedded loop.
If the orientation character of $\gamma$ is zero, the tubular neighborhood $\nu(\gamma) \subset M$ is diffeomorphic to $S^{1} \times D^{n-1}$.

If the orientation character of $\gamma$ is non-zero, the tubular neighborhood $\nu(\gamma) \subset M$ is diffeomorphic to $D^{n-1} \widetilde{\times} S^{1}$.

The second step is as follows. We carve out all disjoint tubular neighborhoods of the loops (3.6) to obtain a codimension zero compact submanifold $X_{s} \subset X\left(F_{s}\right)$ with $t$ boundary components. Since it was assumed that $G$ contains a subgroup of index two, we can choose the loops (3.6) to have trivial orientation character. The boundary of the compact $n$-manifold $X_{s}$ is given by the disjoint union of $t$ copies of
$$\partial\left(\nu\left(\gamma_{i}\right)\right)=\partial\left(S^{1} \times D^{n-1}\right)=S^{1} \times S^{n-2}$$
by Lemma 3. The inclusion
$$X_{s}:=X\left(F_{s}\right) \backslash \bigsqcup_{j=1}^{t} \nu\left(\gamma_{j}\right) \hookrightarrow X\left(F_{s}\right)$$
induces a group homomorphism
$$\pi_{1}\left(X_{s}\right) \rightarrow \pi_{1}\left(X\left(F_{s}\right)\right)$$
that is surjective since the tubular neighborhoods are disjoint. We now argue that the group epimorphism (3.9) is also a monomorphism provided $n \geq 4$. Indeed, suppose a given loop $\gamma_{i_{0}} \subset X_{s}$ bounds a 2-disk that is contained in $X\left(F_{s}\right)$. By a transversality argument, we can push such 2-disk away from all the other loops in (3.6) since $n>2+1$. Thus, the loop $\gamma_{i_{0}}$ bounds a 2-disk in the manifold $X_{s}$ and it is a trivial element in the fundamental group $\pi_{1}\left(X_{s}\right)$. Thus, we conclude that (3.9) is a group isomorphism.

The third step is to cap off each boundary component of $X_{s}$ with a copy of $D^{2} \times S^{n-2}$ in order to construct the closed smooth non-orientable $n$-manifold
$$N^{n}(G):=\left(X\left(F_{s}\right) \backslash \bigsqcup_{j=1}^{t} \nu\left(\gamma_{j}\right)\right) \bigcup\left(\bigsqcup_{j=1}^{t}\left(D_{j}^{2} \times S^{n-2}\right)\right) .$$
The Seifert-van Kampen theorem is used to conclude that the manifold $N^{n}(G)$ has fundamental group isomorphic to (3.3). If $n$ is even, we use a standard homological computation using a Mayer-Vietoris sequence to conclude that the Euler characteristic is $\chi\left(N^{n}(G)\right)=2-2 \operatorname{def}(G)$ for the deficiency $\operatorname{def}(G)=s-t$ of the presentation (3.3) of the group $G$.

The fourth and last step is to appeal to Theorem 5 to conclude that there is a Riemannian metric $\left(N^{n}(G), h\right)$ with scalar curvature $\operatorname{scal}_{h}>0$. The Riemannian product $\left(D^{2} \times S^{n-2}, g_{D^{2}}+g_{S^{n-2}}\right)$ of a round hemisphere with a round $(n-2)$-sphere has positive scalar curvature and the gluing construction (3.10) of $N^{n}(G)$ is along submanifolds of codimension $n-1 \geq 3$. Theorem 5 guarantees the existence of a Riemannian metric $\left(N^{n}(G), h\right)$ of positive scalar curvature scal ${ }_{h}>0$. \(\square\)

Remark 1. A modification to the first step in the proof of Theorem 7 yields a proof of Theorem 6. We substitute the closed 4-manifold (3.5) with the closed orientable 4-manifold
$$X\left(F_{s}\right)=S^{1} \times S^{n-1} \# \cdots \# S^{1} \times S^{n-1}$$
given by the connected sum of $s \in \mathbb{Z}_{\geq 0}$ copies of $S^{1} \times S^{n-1}$. The remaining steps in the proof of Theorem 7 are performed verbatim, and a proof of Theorem 6 is obtained; cf. [21].

\section*{4. Proofs}
4.1. Proof of Theorem A. We show that $\mathcal{G}_{>0}^{2}(G)=\mathcal{G}_{>0}^{2}(G, 0)$, and then proceed to compute the latter set as it was done in Example 1. As it was discussed in Section 2. Proposition 1 states that the sets $\mathcal{G}_{>0}^{2}(G, \alpha)$ are empty for $\alpha \neq 0$ appealing to work of Rosenberg [30, 31]. Let
$$q_{\alpha}(G, \sigma):=\min \{\chi(M):(M, f) \in \mathcal{M}(G, \alpha) \text { and } \sigma(M)=\sigma\}$$
where $\mathcal{M}(G, \alpha)$ is the set of closed smooth oriented 4-manifolds with fundamental group $G$ and $f_{*}([M])=\alpha \in H_{4}(G)$. We now recall a well-known proposition from the literature.

Proposition 3. Kirk-Livingston [23, Proposition 4.1], Kotschick [24].
If $\alpha=0 \in H_{4}(G)$, then the inequalities
$$2-2\left(b_{1}(G)-b_{2}(G)\right)+|\sigma| \leq q_{0}(G, \sigma) \leq 2-2 \operatorname{def}(G)+|\sigma|$$
hold.
Proposition 3 implies that the 4-manifold $M^{4}(G)$ of Theorem 6 realizes the function (1.9) by Hypothesis (1.21). Theorem 1 implies that $\sigma(M)=0$ for every $M \in \mathcal{M}_{>0}^{2}(G)$, and we can conclude that $q_{>0}^{2}(G)=2-2 \operatorname{def}(G)=q_{>0,0}^{2}(G, 0)$. We now need to determine the values of pairs $\{(\chi(M), 0)\}$ to compute the geography and conclude the proof of the theorem. Consider the product of two round 2-spheres $\left(S^{2} \times S^{2}, g_{S^{2}}+g_{S^{2}}\right)$, whose scalar curvature is positive, Theorem 5 implies that the connected sum $M_{k}:=M^{4}(G) \# k\left(S^{2} \times S^{2}\right)$ admits a Riemannian metric of positive scalar curvature for any nonnegative integer number $k$. A Mayer-Vietoris sequence argument shows that Euler characteristic is $\chi\left(M_{k}\right)=2 k-2 \operatorname{def}(G)$ and we conclude that $\mathcal{G}_{>0}^{2}(G)=\left\{(2-2 \operatorname{def}(G)+2 k, 0): k \in \mathbb{Z}_{\geq 0}\right\}$. \(\square\)
4.2. Proof of Theorem B. The proof is similar of Theorem A. Proposition 2 implies that the sets $\mathcal{G}_{>0}(G, \alpha)$ are empty for $\alpha \neq 0$ in the case $H_{4}(G) \neq 0$ and $G$ satisfies Property NPSC or if $G$ is the fundamental group of a closed orientable nonpositively curved Riemannian 4-manifold. If $G$ is the fundamental group of a closed orientable aspherical 4-manifold, the same conclusion holds by Lemma 2. Proposition 3 guarantees that the 4-manifold produced in Theorem 6 realizes the modified Hausmann-Weinberger invariant
$$q_{>0}(G)=2-2 \operatorname{def}(G)=q_{>0,0}(G, 0)=q_{>0,0}^{0}(G, 0) .$$
Using Theorem 5 and taking connected sums with copies of $\mathbb{C P}^{2}$ and/or $\overline{\mathbb{C P}^{2}}$ we conclude that the equality
$$q_{>0}(G, \sigma)=|\sigma|+2-2 \operatorname{def}(G)=q_{>0,0}(G, \sigma)$$
holds and $\mathcal{G}_{>0}(G)=\left\{(2-2 \operatorname{def}(G)+|k|, k): k \in \mathbb{Z}_{\geq 0}\right\}$. Analogously, we conclude that $\mathcal{G}_{>0}^{2}(G)=\left\{(2-2 \operatorname{def}(G)+2 k, 0): k \in \mathbb{Z}_{\geq 0}\right\}$ by invoking Theorem 1 and taking connected sums with copies of $S^{2} \times S^{2}$ equipped with a metric of positive scalar curvature. \(\square\)
4.3. Proof of Proposition C. Notice that the 4-manifold with fundamental group $G_{p, q}$ that is produced by Theorem 6 has Euler characteristic equal to 4. A closed smooth 4-manifold with a Riemannian metric of postive scalar curvature with fundamental group isomorphic to (1.26), Euler characteristic equal to 2, signature equal to zero and trivial second Stiefel-Whitney class is constructed as follows. Consider the loop
$$\gamma_{p}:=S^{1} \times\{z\} \subset S^{1} \times L(q, 1)$$
whose homotopy class corresponds to $p$ times the generator of $\pi_{1}\left(S^{1} \times\{z\}\right)=\mathbb{Z}$; $\{z\}$ is a point in the Lens space $L(q, 1)$ with cyclic fundamental group $\mathbb{Z} / q$. We carve out a tubular neighborhood of (4.5) and cap off the boundary with a copy of $D^{2} \times S^{2}$ to obtain a closed smooth orientable 4-manifold
$$M_{p, q}:=\left(S^{1} \times L(q, 1) \backslash \nu\left(\gamma_{p}\right)\right) \cup\left(D^{2} \times S^{2}\right) .$$
The Seifert-van Kampen theorem implies that the fundamental group of $M_{p, q}$ is isomorphic to $G_{p, q}$ and Theorem 3 implies that the 4-manifold (4.6) admits a metric of positive scalar curvature since the canonical metric $\left(S^{1} \times L(p, 1), d \theta^{2}+g_{L(p, 1)}\right)$ has nonnegative sectional curvature and positive scalar curvature. Proposition 3 implies $q_{>0}\left(G_{p, q}\right)=2$, and $M_{p, q}$ realizes this value; cf. [22, Theorem 2]. Taking connected sums with $\mathbb{C P}^{2}$ and/or $\overline{\mathbb{C P}^{2}}$ we conclude $q_{>0,0}\left(G_{p, q}, \sigma\right)=2+|\sigma|$ and $\mathcal{G}_{>0}\left(G_{p, q}\right)=\{(2+|k|, k): k \in \mathbb{Z}\}$. Analogously, taking connected sums with copies of $S^{2} \times S^{2}$, we conclude that $\mathcal{G}_{>0}^{2}\left(G_{p, q}\right)=\left\{(2 k+2,0): k \in \mathbb{Z}_{\geq 0}\right\}$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] D. Bolotov and A. Dranishnikov. On gromov's scalar curvature conjecture. Proceedings of the American Mathematical Society, 138(4), 2010.
\item[] [2] M. Brunnbauer and B. Hanke. Large and small group homology. Journal of Topology, 3(2):463-486, 2010.
\item[] [3] R. Carr. Construction of manifolds of positive scalar curvature. Transactions of the American Mathematical Society, 307(1):63-74, 1988.
\item[] [4] S. Cecchini and T. Schick. Enlargeable metrics on nonspin manifolds. Proceedings of the American Mathematical Society, 149(5):2199-2211, 2021.
\item[] [5] R. Charney. An introduction to right-angled artin groups. Geometriae Dedicata, 125(1):141-158, 2007.
\item[] [6] R. Charney and M. W. Davis. Finite $\mathrm{k}(\pi, 1) \mathrm{s}$ for artin groups. In Prospects in Topology (AM-138), Volume 138. Princeton University Press, 2016.
\item[] [7] O. Chodosh and C. Li. Generalized soap bubbles and the topology of manifolds with positive scalar curvature. arXiv:2008.11888, 2020.
\item[] [8] J. F. Davis and P. Kirk. Lecture notes in algebraic topology, volume 35. American Mathematical Soc., 2001.
\item[] [9] R. E. Gompf, A. I. Stipsicz, and A. Stipsicz. 4-manifolds and Kirby calculus. Number 20. American Mathematical Soc., 1999.
\item[] [10] M. Gromov. No metrics with positive scalar curvatures on aspherical 5-manifolds. arXiv:2009.05332, 2020.
\item[] [11] M. Gromov and H. B. Lawson Jr. The classification of simply connected manifolds of positive scalar curvature. Annals of Mathematics, pages 423-434, 1980.
\item[] [12] M. Gromov and H. B. Lawson Jr. Spin and scalar curvature in the presence of a fundamental group. i. Annals of Mathematics, pages 209-230, 1980.
\item[] [13] M. Gromov and H. B. Lawson Jr. Positive scalar curvature and the dirac operator on complete riemannian manifolds. Publications Mathématiques de l'IHÉS, 58:83-196, 1983.
\item[] [14] I. Hambleton and M. Kreck. On the classification of topological 4-manifolds with finite fundamental group. Mathematische Annalen, 280(1):85-104, 1988.
\end{itemize}
\begin{itemize}
\item[] [15] B. Hanke. Positive scalar curvature, k-area and essentialness. In Global differential geometry. Springer, 2012.
\item[] [16] B. Hanke, D. Kotschick, J. Roe, and T. Schick. Coarse topology, enlargeability, and essentialness. In Annales scientifiques de l'Ecole normale supérieure, volume 41, pages 473-495, 2008.
\item[] [17] B. Hanke and T. Schick. Enlargeability and index theory. Journal of Differential Geometry, 74(2):293-320, 2006.
\item[] [18] J.-C. Hausmann and S. Weinberger. Caractéristiques d'euler et groupes fondamentaux des variétés de dimension 4. Commentarii Mathematici Helvetici, 60(1):139-144, 1985.
\item[] [19] A. Hildum. The minimum b2 problem for right-angled artin groups. Algebraic \& Geometric Topology, 15(3):1599-1641, 2015.
\item[] [20] N. Hitchin. Harmonic spinors. Advances in Mathematics, 14(1):1-55, 1974.
\item[] [21] M. A. Kervaire. Smooth homology spheres and their fundamental groups. Transactions of the American Mathematical Society, 144:67-72, 1969.
\item[] [22] P. Kirk and C. Livingston. The hausmann-weinberger 4-manifold invariant of abelian groups. Proceedings of the American Mathematical Society, 133(5):1537-1546, 2005.
\item[] [23] P. Kirk and C. Livingston. The geography problem for 4-manifolds with specified fundamental group. Transactions of the American Mathematical Society, 361(8):4091-4124, 2009.
\item[] [24] D. Kotschick. Four-manifold invariants of finitely presented groups. Topology, Geometry and FIeld Theory, pages 89-99, 1994.
\item[] [25] H. B. Lawson and M.-L. Michelsohn. Spin Geometry. Princeton University Press, 2016.
\item[] [26] A. Lichnerowicz. Spineurs harmoniques. C. R. Acad. Sci. Paris, pages 7-9, 1963.
\item[] [27] G. Perelman. The entropy formula for the ricci flow and its geometric applications. arXiv:math/0211159, 2002.
\item[] [28] G. Perelman. Finite extinction time for the solutions to the ricci flow on certain threemanifolds. arXiv:0307245, 2003.
\item[] [29] G. Perelman. Ricci flow with surgery on three-manifolds. arXiv:math/0303109, 2003.
\item[] [30] J. Rosenberg. C*-algebras, positive scalar curvature, and the novikov conjecture. Publications Mathématiques de l'Institut des Hautes Études Scientifiques, 58(1):197-212, 1983.
\item[] [31] J. Rosenberg. Manifolds of positive scalar curvature: a progress report. Surveys in differential geometry, 11(1):259-294, 2006.
\item[] [32] J. Rosenberg and S. Stolz. Metrics of positive scalar curvature and connections with surgery. In Surveys on Surgery Theory (AM-149), Volume 2. Princeton University Press, 2014.
\item[] [33] M. Salvetti. Topology of the complement of real hyperplanes in cn. Invent. Math., 88(3):603-618, 1987.
\item[] [34] T. Schick. A counterexample to the (unstable) gromov-lawson-rosenberg conjecture. Topology, 37(6):1165-1168, 1998.
\item[] [35] R. Schoen and S.-T. Yau. Existence of incompressible minimal surfaces and the topology of three dimensional manifolds with non-negative scalar curvature. Annals of Mathematics, 110(1):127-142, 1979.
\item[] [36] R. Schoen and S.-T. Yau. On the structure of manifolds with positive scalar curvature. Manuscripta Mathematica, 28(1):159-183, 1979.
\item[] [37] R. Schoen and S.-T. Yau. The structure of manifolds with positive scalar curvature. In Directions in partial differential equations, pages 235-242. Elsevier, 1987.
\item[] [38] E. Schrödinger. Diracsches elektron im schwerefeld i. Sitzunsber Preuss. Akad. Wiss., Phys.- Math. Kl., 1932.
\item[] [39] S. Stolz. Manifolds of positive scalar curvature. In Farrell, T. et. al (eds.) Topology of high dimensional manifolds (Trieste 2001), pages 661-709. ICTP Lecture Notes, 2001.
\end{itemize}

Mathematisches Institut der Westfälischen Wilhelms-Universität München, Einsteinstr. 62, DE-48149, Münster, Germany
Email address: amantione@uni-muenster.de
Scuola Internazionale Superiori di Studi Avanzati (SISSA), Via Bonomea 265, 34136, Trieste, Italy
Email address: rtorres@sissa.it
