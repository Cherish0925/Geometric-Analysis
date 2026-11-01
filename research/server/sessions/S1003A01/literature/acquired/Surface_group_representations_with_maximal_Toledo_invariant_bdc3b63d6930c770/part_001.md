---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Surface group representations with maximal Toledo invariant]

---
source_file: math_0605656.pdf
converter: mathpix
format: mmd
---

\title{
SURFACE GROUP REPRESENTATIONS WITH MAXIMAL TOLEDO INVARIANT
}

\author{
MARC BURGER, ALESSANDRA IOZZI, AND ANNA WIENHARD
}

\section*{Dedicated to Domingo Toledo on his 60th birthday}

\begin{abstract}
We develop the theory of maximal representations of the fundamental group $\pi_{1}(\Sigma)$ of a compact connected oriented surface $\Sigma$ (possibly with boundary) into Lie groups $G$ of Hermitian type. For any homomorphism $\rho: \pi_{1}(\Sigma) \rightarrow G$, we define the Toledo invariant $\mathrm{T}(\Sigma, \rho)$, a numerical invariant which has both topological and analytical interpretations. We establish important properties of $\mathrm{T}(\Sigma, \rho)$, among which continuity, uniform boundedness on the representation variety, additivity under connected sum of surfaces and congruence relations $\bmod \mathbb{Z}$. We thus obtain information about the representation variety as well as striking geometric properties of maximal representations, that is representations whose Toledo invariant achieves the maximum value.

Moreover we establish properties of boundary maps associated to maximal representations which generalize naturally monotonicity properties of semiconjugations of the circle.

We define a rotation number function for general locally compact groups and study it in detail for groups of Hermitian type. Properties of the rotation number together with the existence of boundary maps lead to additional invariants for maximal representations and show that the subset of maximal representations is always real semialgebraic.

In the case of surfaces without boundary some of the results were announced in [13].
\end{abstract}

\section*{Contents}
\begin{itemize}
\item[1.] Introduction
\item[1.1.] The Toledo invariant
\item[1.2.] Geometric properties of maximal representations
\item[1.3.] Boundary maps
\item[1.4.] Toledo invariant and rotation numbers
\end{itemize}

\footnotetext{
Date: November 26, 2024.
A.I. and A.W. were partially supported by FNS grant PP002-102765. A.W. was partially supported by the National Science Foundation under agreement No. DMS-0111298 and No. DMS-0604665.
}
2. Preliminaries ..... 12
2.1. Hermitian symmetric spaces, bounded continuous cohomology ..... 12
2.2. Bounded singular and bounded group cohomology ..... 14
2.3. (Bounded) Borel cohomology versus (bounded) continuous cohomology ..... 15
3. Toledo numbers, basic properties and first consequences ..... 15
3.1. Definitions and basic properties ..... 16
3.2. The analytic formula ..... 17
3.3. Proof of Theorem 3.3 ..... 19
3.4. Continuity ..... 21
4. Structure of maximal representations: the Zariski dense case ..... 23
4.1. The formula ..... 23
4.2. $\mathcal{X}$ is of tube type ..... 25
4.3. The image of $\rho$ is discrete ..... 26
4.4. The representation $\rho$ is injective ..... 27
5. Regularity properties of the boundary map: the Zariski dense case ..... 28
5.1. General properties of boundary maps ..... 28
5.2. Exploiting maximality ..... 30
6. Structure of maximal representations and boundary maps: the general case ..... 33
7. Rotation numbers and applications to groups of Hermitian type ..... 37
7.1. Basic definitions and properties ..... 37
7.2. Rotation numbers on groups of Hermitian type ..... 40
8. Toledo numbers: formula and applications to representation varieties ..... 43
8.1. The formula ..... 43
8.2. The bounded fundamental class and generalized $w_{1}$-classes ..... 46
8.3. Applications to representation varieties ..... 50
9. Examples ..... 51
Appendix A. Index of Notation ..... 53
References ..... 53

\section*{1. Introduction}

Let $\Sigma$ be an oriented compact surface with boundary $\partial \Sigma$ and let $G$ be a connected semisimple Lie group with finite center. The problem of understanding the representation variety Hom $\left(\pi_{1}(\Sigma), G\right)$ has received considerable interest. A major theme is the problem of singling out
special components of this representation variety which should generalize Teichmüller space and then studying the geometric significance of the representations belonging to such components.

If $G$ is a split real group and $\partial \Sigma=\emptyset$, there is a component whose global properties were studied by Hitchin [33]; the geometric significance of these representations was recently brought into the open on the one hand by the work of Labourie [40] relating them to Anosov structures, and on the other hand by Fock and Goncharov [22, 23] studying them via the notion of positivity introduced by Lusztig [42].

When $G$ is of Hermitian type and $\partial \Sigma=\emptyset$, one can define the Toledo invariant of a representation and hence the notion of maximal representation: these form a union of connected components of the representation variety. The global properties of these components were investigated by García-Prada, Bradlow and Gothen using Higgs bundles [29, 4, 5] and the geometric properties of maximal representations were investigated by the authors in [13, 7].

The purpose of this paper is to introduce and study the notion of Toledo invariant when $\partial \Sigma \neq \emptyset$ and investigate the structure of the corresponding maximal representations. The treatment includes the case in which $\partial \Sigma=\emptyset$ on which it sheds new light.

The main results are the structure theorem (Theorem 5), the regularity properties of boundary maps (Theorem 8) and the formula for the Toledo invariant in terms of rotations numbers (Theorem 12). For more background on the study of maximal representations we refer to [4, 5, 11, 7, 13, 26, 27, 28, 32, 49, 39, 51].
1.1. The Toledo invariant. Let $G$ be a group of Hermitian type (see § 2.1.1), so that in particular the associated symmetric space $\mathcal{X}$ is Hermitian of noncompact type; then $\mathcal{X}$ carries a unique Hermitian (normalized) metric of minimal holomorphic sectional curvature -1. The Kähler form $\omega_{\mathcal{X}}$ of this metric gives rise in the familiar way to a continuous class $\kappa_{G} \in \mathrm{H}_{\mathrm{c}}^{2}(G, \mathbb{R})$ and, owing to the isomorphism between bounded continuous and continuous cohomology in degree two, to the bounded Kähler class $\kappa_{G}^{\mathrm{b}} \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ (see § 2.1). The bounded Kähler class is the source of new invariants for representations and has been considered in [10, 13, 7, 14, 12].

Let $\Sigma$ be a connected oriented compact surface with boundary $\partial \Sigma$, and $\rho: \pi_{1}(\Sigma) \rightarrow G$ a representation. When $\partial \Sigma=\emptyset$, the Toledo invariant is given by the evaluation of $\rho^{*}\left(\kappa_{G}\right)$ on the fundamental class $[\Sigma]$,
$$\mathrm{T}(\Sigma, \rho)=\left\langle\rho^{*}\left(\kappa_{G}\right),[\Sigma]\right\rangle .$$

In the general case we obtain by pullback in bounded cohomology a bounded class
$$\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right) \in \mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{R}\right) \cong \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \mathbb{R}) .$$
The canonical map $j_{\partial \Sigma}: \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \partial \Sigma, \mathbb{R}) \rightarrow \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \mathbb{R})$ from singular bounded cohomology relative to $\partial \Sigma$ to singular bounded cohomology is an isomorphism (see (2.d) in § 2.2), and we define
$$\mathrm{T}(\Sigma, \rho)=\left\langle j_{\partial \Sigma}^{-1} \rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right),[\Sigma, \partial \Sigma]\right\rangle,$$
where now $j_{\partial \Sigma}^{-1} \rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)$ is considered as an ordinary relative class and $[\Sigma, \partial \Sigma]$ is the relative fundamental class. The above construction applies to any class $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ and we denote by $\mathrm{T}_{\kappa}(\Sigma, \rho)$ the resulting invariant. This generalization will be useful when we consider integral classes. This construction circumvents the fact that $\mathrm{H}^{2}(\Sigma, \mathbb{R})=0$ when $\partial \Sigma \neq \emptyset$; indeed in all cases $\mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \mathbb{R})$ is infinite dimensional, provided $\chi(\Sigma) \leq-1$.

The basic properties of the Toledo invariant are summarized in the following

Theorem 1. Let $G$ be a group of Hermitian type and $\rho: \pi_{1}(\Sigma) \rightarrow G$ a representation. Then
\begin{itemize}
\item[(1)] $|\mathrm{T}(\Sigma, \rho)| \leq|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}}$, where $\mathrm{r}_{\mathcal{X}}$ is the rank of $\mathcal{X}$.
\item[(2)] The map $\mathrm{T}(\Sigma, \cdot)$ is continuous on Hom $\left(\pi_{1}(\Sigma), G\right)$; if $\partial \Sigma=\emptyset$, its range is finite, while if $\partial \Sigma \neq \emptyset$ its range is the interval
$$\left[-|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}},|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}}\right] .$$
\item[(3)] If $\Sigma$ is the connected sum of two (connected) surfaces $\Sigma_{i}$ along a separating loop, then
$$\mathrm{T}(\Sigma, \rho)=\mathrm{T}\left(\Sigma_{1}, \rho_{1}\right)+\mathrm{T}\left(\Sigma_{2}, \rho_{2}\right),$$
\end{itemize}
where $\rho_{i}$ is the restriction of $\rho$ to $\pi_{1}\left(\Sigma_{i}\right)$.
[Theorem 1 follows from Corollary 3.4, Proposition 3.10, Corollary 3.12 and Proposition 3.2.]

Here and in the sequel, an essential role is played by Theorem 3.3, where we identify the Toledo invariant with an invariant defined in analytic terms, introduced and studied in [11]. In view of Theorem [1, we set the following

Definition 2. A representation $\rho: \pi_{1}(\Sigma) \rightarrow G$ is maximal if
$$\mathrm{T}(\Sigma, \rho)=|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}} .$$

We denote by $\operatorname{Hom}_{\text {max }}\left(\pi_{1}(\Sigma), G\right)$ the subspace of the representation variety consisting of maximal representations. Notice that when $\partial \Sigma=$ $\emptyset$ this subspace is a union of components of the representation variety, while when $\partial \Sigma \neq \emptyset$ the whole representation variety is connected (see however Corollary 14).
1.2. Geometric properties of maximal representations. Before treating the case of a general group of Hermitian type, we state the structure theorem for maximal representation into $\operatorname{PU}(1,1)$ which generalizes to the case of surfaces with boundary Goldman's characterization of maximal representations when $\partial \Sigma=\emptyset$ [26, 27].

Theorem 3. Let $\Sigma$ be a connected oriented surface such that $\chi(\Sigma) \leq$ -1. A representation $\rho: \pi_{1}(\Sigma) \rightarrow \mathrm{PU}(1,1)$ is maximal if and only if it is the holonomy representation of a complete hyperbolic metric on the interior $\Sigma^{\circ}$ of $\Sigma$.

Remark 4. Theorem 3 is proved in § 3.2; the "only if" part is a consequence of [11] together with the formula in Theorem 3.3; the "if" part, while being Gauss-Bonnet's theorem in the boundaryless case, requires a quite different argument when $\partial \Sigma \neq \emptyset$.

We observe that when $\partial \Sigma \neq \emptyset$, the invariant $\mathrm{T}(\Sigma, \rho)$ depends not only on $\pi_{1}(\Sigma)$ but also on $\Sigma$ : in fact, if $\Sigma_{1}, \Sigma_{2}$ are nondiffeomorphic surfaces with isomorphic fundamental groups, $i: \pi_{1}\left(\Sigma_{1}\right) \rightarrow \pi_{1}\left(\Sigma_{2}\right)$ is an isomorphism and $\rho: \pi_{1}\left(\Sigma_{2}\right) \rightarrow \mathrm{PU}(1,1)$ is a maximal representation, then it follows from Theorem 3 that $\rho \circ i$ is not maximal.

The first result beyond the case PU(1, 1) was obtained by Toledo [49] who, in the boundaryless case, showed that a maximal representation into $\operatorname{PU}(1, m)$ stabilizes a complex geodesic. It turns out that the appropriate generalization of complex geodesic is, in this context, the notion of maximal tube type subdomain. Roughly speaking, tube type domains are bounded symmetric domains which admit a model which corresponds to the upper half space model in the case of the Poincaré disk, and their significance for rigidity questions of isometric group actions already appeared in [10, 14]. For a general Hermitian symmetric space $\mathcal{X}$, maximal tube type subdomains exist, are of rank equal to the rank of $\mathcal{X}$ and are $G$-conjugate. As alluded to above, the maximal tube type subdomains in complex hyperbolic $n$-space are the complex geodesics.

The main structure theorem for maximal representations is:
Theorem 5. Let $\mathbf{G}$ be a connected semisimple algebraic group defined over $\mathbb{R}$ such that $G=\mathbf{G}(\mathbb{R})^{\circ}$ is of Hermitian type. Let $\Sigma$ be a compact
connected oriented surface with (possibly empty) boundary and $\chi(\Sigma) \leq$ -1. If $\rho: \pi_{1}(\Sigma) \rightarrow G$ is a maximal representation, then
\begin{itemize}
\item[(1)] $\rho$ is injective with discrete image;
\item[(2)] the Zariski closure $\mathbf{H}<\mathbf{G}$ of the image of $\rho$ is reductive;
\item[(3)] the reductive Lie group $H:=\mathbf{H}(\mathbb{R})^{\circ}$ has compact centralizer in $G$ and the symmetric space $\mathcal{Y}$ associated to $H$ is Hermitian of tube type;
\item[(4)] $\rho\left(\pi_{1}(\Sigma)\right)$ stabilizes a maximal tube type subdomain $\mathcal{T} \subset \mathcal{X}$.
\end{itemize}
[Theorem 5 is proved in §4 when $\rho$ has Zariski dense image, while the general case is treated in § [6.]

Remark 6. (1) In the case in which $\partial \Sigma=\emptyset$, Theorem 5 was announced in [13].
\begin{itemize}
\item[(2)] When $\partial \Sigma=\emptyset$, Theorem 5(4) was obtained by Hernández for $G=\mathrm{PU}(2, m)$ [32]. Assuming that the representation is reductive, Bradlow, García-Prada and Gothen also obtained Theorem 5(4) for $G=\operatorname{SU}(n, m)$ [4] and for $\operatorname{SO}^{*}(2 n)$ [5]. In each of these works the Toledo invariant appears as the first Chern class of an appropriate complex line bundle over $\Sigma$.
\item[(3)] When $\partial \Sigma \neq \emptyset$ and $G=\operatorname{PU}(1, m)$, Koziarz and Maubon introduced [38] an invariant lying in the de Rham cohomology of $\Sigma$ with compact support, whose evaluation on $[\Sigma, \partial \Sigma]$ can be shown to be equal to our notion of Toledo invariant; in this context, they obtained in [38] Theorem 5(4) as well as Theorem 3.
\end{itemize}

The symmetric space $\mathcal{Y}$ in Theorem 5 is the variety of maximal compact subgroups of $H$; since $H$ has compact centralizer in $G$, there is a unique totally geodesic embedding $i: \mathcal{Y} \rightarrow \mathcal{X}$ which is not necessarily holomorphic but is tight. This latter notion, which is analytic in nature, stems from our approach via bounded cohomology, see [12].

A special case of Theorem 5 is when the homomorphism $\rho$ has Zariski dense image. Then $\mathcal{Y}=\mathcal{X}$ and hence $\mathcal{X}$ is of tube type. This result is optimal in the sense that every tube type domain admits a maximal representation with Zariski dense image. More precisely, let $d: \mathbb{D} \rightarrow \mathcal{X}$ be a diagonal disk, also called tight holomorphic disk in [21, 12] (see (2.b)§ 2.1.2 for the definition), and $\Delta: \operatorname{SU}(1,1) \rightarrow \mathbf{G}(\mathbb{R})^{\circ}$ a homomorphism associated to $d$.

Theorem 7. Assume that $\mathcal{X}$ is of tube type, that $\chi(\Sigma) \leq-2$, and let
$$h: \pi_{1}(\Sigma) \rightarrow \operatorname{SU}(1,1)$$
be a complete hyperbolization of $\Sigma^{\circ}$. If the surface is of type $(g, n)=$ $(1,2)$ or $(0,4)$, we assume that $h$ sends one, respectively two, boundary
components of $\partial \Sigma$ to hyperbolic elements. Then $\rho_{0}:=\Delta \circ h: \pi_{1}(\Sigma) \rightarrow$ $G$ admits a deformation $\left(\rho_{t}\right)_{t \geq 0}$ such that:
\begin{itemize}
\item[(1)] $\rho_{t}$ is maximal for all $t \geq 0$, and
\item[(2)] $\rho_{t}$ has Zariski dense image for all $t>0$.
\end{itemize}
[This theorem is proved in § 9]
1.3. Boundary maps. Maximal representations give rise to boundary maps with special regularity properties which in turn play an important role in the study of the set of maximal representations and in the construction of new invariants thereof. Monotonicity (or positivity) is one of these properties and in order to express it we need the notion of maximal triples of points in the Shilov boundary of a symmetric domain: those are the vertices of ideal geodesic triangles of maximal Kähler area in a sense made precise in [21] (see § frm-e.1.3 for the definition).

Theorem 8. Let $h: \pi_{1}(\Sigma) \rightarrow \mathrm{PU}(1,1)$ be a complete hyperbolization of $\Sigma^{\circ}$ of finite area and $\rho: \pi_{1}(\Sigma) \rightarrow G$ a representation into a group of Hermitian type. Then $\rho$ is maximal if and only if there exists a left continuous map
$$\varphi: \partial \mathbb{D} \rightarrow \check{S}$$
with values in the Shilov boundary $\check{S}$ of the bounded symmetric domain associated to $G$ such that
\begin{itemize}
\item[(1)] $\varphi$ is strictly $\rho \circ h^{-1}$-equivariant, and
\item[(2)] $\varphi$ is monotone, that is it maps positively oriented triples on $\partial \mathbb{D}$ to maximal triples on $\check{S}$.
\end{itemize}
[Theorem 8 is proved in § 5 in the case in which $\rho$ has Zariski dense image and in § 6 in the general case.]

Remark 9. The theorem holds true also if "left continuous" is replaced by "right continuous".

The characterization in Theorem 8 clarifies the relation between maximal representations and the Hitchin or positive representations into split real Lie groups which were recently studied by Labourie [40], Guichard [31], and Fock and Goncharov [22]. Indeed in the latter the authors established a similar characterization in terms of equivariant maps from $\partial \mathbb{D}$ into (full) flag varieties which send positively oriented triple in $\partial \mathbb{D}$ to positive triples of flags in the sense of Lusztig.

In the only case when $G$ is of Hermitian type as well as real split, namely when $G$ is locally isomorphic to a symplectic group $\operatorname{Sp}(V)$, the Shilov boundary can be identified with the space of Lagrangian
subspaces in $V$ and in this case the notion of maximality of triples in $\check{S}$ coincides with the notion of positivity of triples in partial flag varieties - such as the space of Lagrangians - defined by Lusztig in [43]. Thus Theorem 8 implies that the space of positive representations into $\operatorname{PSp}(V)$ defined by Fock and Goncharov [22, Definition 1.10], is a proper subset of the space of maximal representations. For the Hitchin component (when $\partial \Sigma=\emptyset$ ) this was observed in [7].

The issue of continuity of the boundary map $\varphi$ presents itself naturally. When $\partial \Sigma=\emptyset$, the continuity of $\varphi$ was established in [7] in the case in which $G=\operatorname{Sp}(V)$ is a symplectic group, as a byproduct of the construction of an Anosov system; the case of a general group of Hermitian type will be treated in a forthcoming paper. When $\partial \Sigma \neq \emptyset$, then already in the case $G=\operatorname{PU}(1,1)$ the map $\varphi$ will not be in general continuous as the case in which $\rho$ is an infinite area hyperbolization indicates. In fact, if $G=\mathrm{PU}(1,1)$, the map $\varphi$ is a semiconjugacy in the sense of Ghys [25] and this will be used in § 8.2 to define a canonical integral bounded class
$$\kappa_{\Sigma, \mathbb{Z}}^{\mathrm{b}} \in \mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{Z}\right)$$
which, when $\partial \Sigma=\emptyset$, corresponds to the fundamental class under the comparison map. Letting $\kappa_{\Sigma}^{\mathrm{b}} \in \mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{R}\right)$ denote the corresponding real class, we will establish in § 8.2 (see Corollary 8.6) the following

Corollary 10. For any homomorphism $\rho: \pi_{1}(\Sigma) \rightarrow G$, the following are equivalent:
\begin{itemize}
\item[(1)] $\rho$ is maximal, and
\item[(2)] $\rho^{*}(\kappa)=\lambda_{G}(\kappa) \kappa_{\Sigma}^{\mathrm{b}}$, for all $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$, where $\lambda_{G}$ is a certain explicit linear form on $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$.
\end{itemize}

The extent to which Corollary 10 does not hold for integral classes will be the source of new invariants of maximal representations which will be given an explicit form once rotation numbers are introduced in the next section.
1.4. Toledo invariant and rotation numbers. In order to define a notion of integral class in continuous bounded cohomology we consider, for $G$ a locally compact second countable group and $A=\mathbb{Z}$ or $\mathbb{R}$, the cohomology $\widehat{\mathrm{H}}_{\mathrm{cb}}^{\bullet}(G, A)$ of the complex of bounded Borel cochains on $G$ which turns out to coincide with bounded continuous cohomology if $A=\mathbb{R}$ (see § 2.3). Given $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$, we introduce in § 7 the rotation number
$$\operatorname{Rot}_{\kappa}: G \rightarrow \mathbb{R} / \mathbb{Z},$$
which is a class function whose restriction to any amenable closed subgroup is a homomorphism and we show its continuity (Corollary 7.6).

The rotation number $\operatorname{Rot}_{\kappa}$ generalizes the classical rotation number of an orientation preserving homeomorphism of the circle as well as the symplectic rotation number introduced by Barge and Ghys in [1] and the construction of Clerc and Koufany in [18]. The exact relations are discussed in § 7.

When $G$ if of Hermitian type and $K<G$ is a maximal compact subgroup, the basic properties of the rotation number $\operatorname{Rot}_{\kappa}$ are summarized in the following

Theorem 11. (1) The map
$$\begin{aligned}
\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z}) & \rightarrow \operatorname{Hom}_{\mathrm{c}}(K, \mathbb{R} / \mathbb{Z}) \\
\kappa & \left.\mapsto \operatorname{Rot}_{\kappa}\right|_{K}
\end{aligned}$$
is an isomorphism.
\begin{itemize}
\item[(2)] The change of coefficients $\widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z}) \rightarrow \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ is injective with image a lattice.
\item[(3)] For every $g \in G$,
$$\operatorname{Rot}_{\kappa}(g)=\operatorname{Rot}_{\kappa}(k),$$
where $k \in K$ is conjugate to the elliptic component $g_{e}$ in the refined Jordan decomposition $g=g_{e} g_{h} g_{u}$ of $g$.
\item[(4)] The unique continuous lift
$$\widetilde{\operatorname{Rot}_{\kappa}}: \widetilde{G} \rightarrow \mathbb{R}$$
vanishing at $e$ is a homogeneous quasimorphism.
\end{itemize}
[Theorem 11 is proved in Propositions 7.7, 7.8] and Theorem 7.9; for the refined Jordan decomposition see [3, § 2].]

We turn now to the formula of the Toledo invariant $\mathrm{T}_{\kappa}(\Sigma, \rho)$ when $\kappa$ is an integral bounded class. For this we assume that $\partial \Sigma \neq \emptyset$ and let
$$\pi_{1}(\Sigma)=\left\langle a_{1}, b_{1}, \ldots, a_{g}, b_{g}, c_{1}, \ldots, c_{n}: \prod_{i=1}^{g}\left[a_{i}, b_{i}\right] \prod_{j=1}^{n} c_{j}=e\right\rangle$$
be a presentation where the elements $c_{i}$ represent loops which are freely homotopic to the corresponding boundary components of $\partial \Sigma$ with positive orientation. Given a homomorphism $\rho: \pi_{1}(\Sigma) \rightarrow G$, let $\widetilde{\rho}: \pi_{1}(\Sigma) \rightarrow \widetilde{G}$ be a lift of $\rho$ to the universal covering $\widetilde{G}$, taking into account that $\pi_{1}(\Sigma)$ is free.

Theorem 12. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$. Then
$$\mathrm{T}_{\kappa}(\Sigma, \rho)=-\sum_{j=1}^{n} \widetilde{\operatorname{Rot}_{\kappa}}\left(\widetilde{\rho}\left(c_{j}\right)\right) .$$
[Theorem 12 is proved in § 8.1.]
When the boundary of $\Sigma$ is empty, a formula for $\mathrm{T}_{\kappa}$ (see Theorem 8.3) can be obtained by cutting $\Sigma$ along a separating loop and using Theorem 12 together with the additivity property of the Toledo invariant in Theorem 1(3).

In conjunction with Corollary 10, rotation numbers give rise to nontrivial invariants of maximal representations; recalling that the Shilov boundary $\check{S}$ of the bounded symmetric domain $\mathcal{D}$ associated to $G$ is a homogeneous space with typical stabilizer $Q$ and letting $e_{G}$ denote the exponent of the finite group $Q / Q^{\circ}$, we have:

Theorem 13. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ and $\rho_{0}: \pi_{1}(\Sigma) \rightarrow G$ a maximal representation.
\begin{itemize}
\item[(1)] For every maximal representation $\rho: \pi_{1}(\Sigma) \rightarrow G$ the map
$$\begin{aligned}
\mathrm{R}_{\kappa}^{\rho_{0}}(\rho): \pi_{1}(\Sigma) & \longrightarrow \mathbb{R} / \mathbb{Z} \\
\gamma & \mapsto \operatorname{Rot}_{\kappa}(\rho(\gamma))-\operatorname{Rot}_{\kappa}\left(\rho_{0}(\gamma)\right)
\end{aligned}$$
is a homomorphism.
\item[(2)] If $\mathcal{D}$ is of tube type, then $\mathrm{R}_{\kappa}^{\rho_{0}}(\rho)$ takes values in $e_{G}^{-1} \mathbb{Z} / \mathbb{Z}$ and
$$\operatorname{Hom}_{\max }\left(\pi_{1}(\Sigma), G\right) \rightarrow \operatorname{Hom}\left(\pi_{1}(\Sigma), \mathbb{R} / \mathbb{Z}\right)$$
is constant on connected components.
\end{itemize}
[Theorem 13 is proved in § 8.2.]
In Example 8.7 we describe for $G=\operatorname{Sp}(V), \operatorname{dim}(V)=4 m$ and $\partial \Sigma=\emptyset$ that already $\operatorname{Rot}_{\kappa}(\rho): \pi_{1}(\Sigma) \rightarrow \mathbb{Z} / 2 \mathbb{Z}$ is a homomorphism and discuss its relationship with the first Stiefel-Withney class of a certain real vector bundle constructed using the boundary map from Theorem 8.

We turn now to our final application to representation varieties. For this we assume again that $\partial \Sigma \neq \emptyset$ and use the familiar presentation of $\pi_{1}(\Sigma)$ given in (1.1). Then
$$\begin{array}{r}
\operatorname{Hom}^{\check{S}}\left(\pi_{1}(\Sigma), G\right):=\left\{\rho \in \operatorname{Hom}\left(\pi_{1}(\Sigma), G\right): \rho\left(c_{i}\right)\right. \text { has at least } \\
\text { one fixed point in } \check{S}, 1 \leq i \leq n\},
\end{array}$$
is a semialgebraic set if $G$ is real algebraic and we have as a consequence of Theorem 8, that
$$\operatorname{Hom}_{\max }\left(\pi_{1}(\Sigma), G\right) \subset \operatorname{Hom}^{\check{S}}\left(\pi_{1}(\Sigma), G\right) .$$

Corollary 14. Let $\kappa \in \widehat{\mathrm{H}}_{\mathrm{cb}}^{2}(G, \mathbb{Z})$ and assume that $\mathcal{D}$ is of tube type. Then:
\begin{itemize}
\item[(1)] $\mathrm{T}_{\kappa}(\Sigma, \rho) \in e_{G}^{-1} \mathbb{Z}$ for every $\rho \in \operatorname{Hom}^{\check{S}}\left(\pi_{1}(\Sigma), G\right)$, and
\item[(2)] $\operatorname{Hom}_{\text {max }}\left(\pi_{1}(\Sigma), G\right)$ is a union of connected components of the set $\operatorname{Hom}^{\check{S}}\left(\pi_{1}(\Sigma), G\right)$.
\end{itemize}
[Corollary 14 is proved in § 8.3.]
An alternative boundary condition might be imposed by fixing instead a set $\mathcal{C}=\left\{\mathcal{C}_{1}, \ldots, \mathcal{C}_{n}\right\}$ of conjugacy classes in $G$ and defining
$$\operatorname{Hom}^{\mathcal{C}}\left(\pi_{1}(\Sigma), G\right):=\left\{\rho \in \operatorname{Hom}\left(\pi_{1}(\Sigma), G\right): \rho\left(c_{i}\right) \in \mathcal{C}_{i}, 1 \leq i \leq n\right\} .$$
Then $\operatorname{Hom}^{\mathcal{C}}\left(\pi_{1}(\Sigma), G\right)$ is also a semialgebraic set and it follows immediately from Theorem 12 that $T_{\kappa}$ is constant on its connected components.

Notice however that Corollary 14 implies that for many choices of conjugacy classes the intersection $\operatorname{Hom}_{\text {max }}\left(\pi_{1}(\Sigma), G\right) \cap \operatorname{Hom}^{\mathcal{C}}\left(\pi_{1}(\Sigma), G\right)$ considered above is actually empty. For example in the case when $\Sigma$ has precisely one boundary component Theorem 12 readily implies that for any maximal representation the rotation number of the conjugacy class $\mathcal{C}=\left\{\mathcal{C}_{1}\right\}$ has to be zero. From a different point of view, fixing a conjugacy class $\mathcal{C}$ with nonzero rotation number, gives a modified Milnor-Wood type inequality as in Theorem 1(1) for the Toledo invariant restricted to $\operatorname{Hom}^{\mathcal{C}}\left(\pi_{1}(\Sigma), G\right)$. Goldman showed in [28] that for the one-punctured torus, representations into $\operatorname{PSL}(2, \mathbb{R})$ maximizing the Toledo invariant with respect to this modified Milnor-Wood type inequality correspond to singular hyperbolic structures on the torus with cone type singularities in the puncture.

Acknowledgments: The authors are grateful to D. Toledo for his crucial comments in the beginning of our study of maximal representations and for his continuing interest and support. The authors thank N. A'Campo for asking the question which triggered the study of maximal representations of surface groups with boundary, Y. Benoist for suggesting which formula computes the Toledo invariant (see Theorem 12) and F. Labourie for various enjoyable and useful conversations. Our thanks go also to S. Bradlow, O. García-Prada, P. Gothen
and I. Mundet i Riera for interesting discussions concerning the relation between our work and their approach through Higgs bundles. The third author wants to thank O. Guichard for his questions and remarks, which lead to a correction in Theorem 13.

\section*{2. Preliminaries}

\subsection*{2.1. Hermitian symmetric spaces, bounded continuous cohomology.}
2.1.1. A Lie group $G$ is of Hermitian type if it is connected, semisimple with finite center and no compact factors, and if the associated symmetric space is Hermitian. A Lie group $G$ is of type (RH) if it is connected reductive with compact center and the quotient $G / G_{c}$ by the largest connected compact normal subgroup $G_{c}$ is of Hermitian type.

If $G$ is a locally compact group, $\mathrm{H}_{\mathrm{c}}^{\bullet}(G, \mathbb{R})$ denotes the continuous cohomology with $\mathbb{R}$-trivial coefficients, while $\mathrm{H}_{\mathrm{cb}}^{\bullet}(G, \mathbb{R})$ is the bounded continuous cohomology; for the general theory concerning the latter and its relation to the former, we refer to [46, 15, 9, 8].

When $G$ is of type (RH) and $\mathcal{X}$ is its associated symmetric space, we have isomorphisms
$$\Omega^{2}(\mathcal{X})^{G} \longrightarrow \mathrm{H}_{\mathrm{c}}^{2}(G, \mathbb{R}) \longleftarrow \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R}),$$
where the first is the Van Est isomorphism between the complex $\Omega^{\bullet}(\mathcal{X})^{G}$ of $G$-invariant differential forms on $\mathcal{X}$ and $\mathrm{H}_{\mathrm{c}}^{\bullet}(G, \mathbb{R})$ [50], while the second is the comparison map which in degree two is an isomorphism [15]. Given $\omega \in \Omega^{2}(\mathcal{X})^{G}$ and $x \in \mathcal{X}$ a basepoint, the function
$$c_{\omega}\left(g_{0}, g_{1}, g_{2}\right):=\frac{1}{2 \pi} \int_{\Delta\left(g_{0} x, g_{1} x, g_{2} x\right)} \omega,$$
where $\Delta\left(g_{0} x, g_{1} x, g_{2} x\right)$ denotes a smooth triangle with geodesic sides, defines a homogeneous $G$-invariant cocycle which is moreover bounded; when $\omega=\omega_{\mathcal{X}}$ is the Kähler form for the unique $G$-invariant Hermitian metric of minimal holomorphic sectional curvature -1 (normalized metric), we let $\kappa_{G} \in \mathrm{H}_{\mathrm{c}}^{2}(G, \mathbb{R})$ and $\kappa_{G}^{\mathrm{b}} \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ denote the corresponding classes and refer to $\kappa_{G}$ (respectively $\kappa_{G}^{\mathrm{b}}$ ) as the Kähler class (respectively bounded Kähler class). For the Gromov norm of $\kappa_{G}^{\mathrm{b}}$, we have that
$$\left\|\kappa_{G}^{\mathrm{b}}\right\|=\frac{\mathrm{r}_{\mathcal{X}}}{2},$$
where $\mathrm{r}_{\mathcal{X}}$ is the rank of $\mathcal{X}$.
2.1.2. Let $G$ be of Hermitian type and $\mathcal{X}$ be the associated symmetric space. Then:
\begin{itemize}
\item[(2.] a) A maximal polydisk in $\mathcal{X}$ is the image of a totally geodesic and holomorphic embedding $t: \mathbb{D}^{\mathbf{r}_{\mathcal{X}}} \rightarrow \mathcal{X}$ of a product of $\mathrm{r}_{\mathcal{X}}$ Poincaré disks.
\item[(2.] b) A diagonal disk (or tight holomorphic disk in $\mathcal{X}$ is the image of the diagonal $\mathbb{D} \subset \mathbb{D}^{\mathfrak{r}_{\mathcal{X}}}$ under $t$; we will denote by $d: \mathbb{D} \rightarrow \mathcal{X}$ the resulting totally geodesic and holomorphic embedding.
\end{itemize}

To the above objects are associated a connected finite covering $L$ of PU(1,1) and homomorphisms $\tau: L^{\mathrm{r} \mathcal{X}} \rightarrow G$ and $\Delta: L \rightarrow G$ with respect to which $t$ and $d$ are equivariant. We have moreover that
$$\tau^{*}\left(\kappa_{G}^{\mathrm{b}}\right)=\kappa_{L^{\mathrm{r} \mathcal{X}}}^{\mathrm{b}} \quad \text { and } \Delta^{*}\left(\kappa_{G}^{\mathrm{b}}\right)=\mathrm{r}_{\mathcal{X}} \kappa_{L}^{\mathrm{b}} .$$
2.1.3. Let $G$ be of type (RH), $\mathcal{X}$ the associated symmetric space, $\mathcal{D}$ the bounded domain realization and $\check{S}$ its Shilov boundary. Then $\check{S}$ is a homogeneous $G$-space of the form $G / Q$, where $Q$ is a specific parabolic subgroup (which is maximal if $\mathcal{X}$ is irreducible). Two points $x, y \in \check{S}$ are transversal if $(x, y)$ lies in the open $G$-orbit in $\check{S}^{2}$. Let $\check{S}^{(3)}$ denote the set of triples of pairwise transversal points. It was shown by Clerc and Ørsted [20, 21] that the map
$$\begin{aligned}
\mathcal{D}^{3} & \longrightarrow \mathbb{R} \\
(x, y, z) & \mapsto \frac{1}{2 \pi} \int_{\Delta(x, y, z)} \omega_{\mathcal{D}},
\end{aligned}$$
where $\omega_{\mathcal{D}}$ is the Kähler form for the normalized metric on $\mathcal{D}$, extends continuously to $\check{S}^{(3)}$; Clerc showed then that by taking appropriate tangential limits one obtains a well defined $G$-invariant Borel cocycle
$$\beta_{\check{S}}: \check{S}^{3} \rightarrow \mathbb{R}$$
extending the previous one, which satisfies
$$\left|\beta_{\check{S}}(x, y, z)\right| \leq \frac{r_{\mathcal{D}}}{2},$$
where $\mathrm{r}_{\mathcal{D}}=\mathrm{r}_{\mathcal{X}}$ (see [17, Theorem 5.3]). In the following $\beta_{\check{S}}$ will be referred to as the generalized Maslov cocycle and a triple $x, y, z \in \check{S}$ for which $\beta_{\check{S}}(x, y, z)=\frac{\mathrm{r}_{\mathcal{D}}}{2}$ will be called maximal.

Let now $\left(\mathcal{B}_{\text {alt }}^{\infty}\left(\check{S}^{\bullet}\right)\right)$ denote the complex of bounded alternating Borel cocycles on $\check{S}$. Then, under the canonical map
$$\mathrm{H}^{\bullet}\left(\mathcal{B}_{\mathrm{alt}}^{\infty}\left(\check{S}^{\bullet}\right)^{G}\right) \rightarrow \mathrm{H}_{\mathrm{cb}}^{\bullet}(G, \mathbb{R})$$
(see [14, § 4.2.], [9, Corollary 2.2.]) the class defined by $\beta_{\check{S}}$ corresponds to $\kappa_{G}^{\mathrm{b}}$.
2.2. Bounded singular and bounded group cohomology. A "space" will always refer to a countable CW-complex and $A$ will be one of the coefficients $\mathbb{Z}, \mathbb{R}, \mathbb{R} / \mathbb{Z}$. For a pair of spaces $Y \subset X, \mathrm{H}^{\bullet}(X, Y, A)$ and $\mathrm{H}_{\mathrm{b}}^{\bullet}(X, Y, A)$ denote respectively the singular relative cohomology with coefficients in $A$ and its bounded counterpart; observe that $\mathrm{H}^{\bullet}(X, Y, \mathbb{R} / \mathbb{Z})=$ $\mathrm{H}_{\mathrm{b}}^{\bullet}(X, Y, \mathbb{R} / \mathbb{Z})$. Also, $\mathrm{H}^{\bullet}\left(\pi_{1}(X), A\right)$ and $\mathrm{H}_{\mathrm{b}}^{\bullet}\left(\pi_{1}(X), A\right)$ denote respectively the group cohomology and the bounded group cohomology of $\pi_{1}(X)$ with $A$-coefficients and $\mathrm{H}^{\bullet}\left(\pi_{1}(X), \mathbb{R} / \mathbb{Z}\right)=\mathrm{H}_{\mathrm{b}}^{\bullet}\left(\pi_{1}(X), \mathbb{R} / \mathbb{Z}\right)$. These cohomology theories come with the following natural comparison maps
$$\begin{aligned}
& \mathrm{H}_{\mathrm{b}}^{\bullet}(X, Y, A) \rightarrow \mathrm{H}^{\bullet}(X, Y, A) \\
& \mathrm{H}_{\mathrm{b}}^{\bullet}\left(\pi_{1}(X), A\right) \rightarrow \mathrm{H}^{\bullet}\left(\pi_{1}(X), A\right) \\
& \mathrm{H}^{\bullet}\left(\pi_{1}(X), A\right) \rightarrow \mathrm{H}^{\bullet}(X, A) \\
& \mathrm{H}_{\mathrm{b}}^{\bullet}\left(\pi_{1}(X), A\right) \rightarrow \mathrm{H}_{\mathrm{b}}^{\bullet}(X, A),
\end{aligned}$$
where the last two are induced by the classifying map $X \rightarrow B \pi_{1}(X)$.
We recall the following facts:
\begin{itemize}
\item[(2.] c) the short exact sequence
$$0 \longrightarrow \mathbb{Z} \longrightarrow \mathbb{R} \longrightarrow \mathbb{R} / \mathbb{Z} \longrightarrow 0$$
gives rise to long exact sequences in each of the four cohomology theories; these sequences are natural with respect to the four comparison maps;
\item[(2.] d) the inclusion of spaces $Z_{1} \subset Z_{2} \subset X$ induces a long exact sequence in singular relative and bounded singular relative cohomology which fit into the long exact sequences coming from the coefficient sequence in (2.c);
\item[(2.] e) in general the comparison map
$$g_{X}: \mathrm{H}_{\mathrm{b}}^{\bullet}\left(\pi_{1}(X), \mathbb{R}\right) \rightarrow \mathrm{H}_{\mathrm{b}}^{\bullet}(X, \mathbb{R})$$
is an isomorphism [30, 6, 35], referred to as Gromov isomorphism; as a consequence, if each connected component of $Z_{1}$ and $Z_{2}$ has amenable fundamental group the map
$$j_{Z_{1}, Z_{2}}: \mathrm{H}_{\mathrm{b}}^{\bullet}\left(X, Z_{2}, \mathbb{R}\right) \rightarrow \mathrm{H}_{\mathrm{b}}^{\bullet}\left(X, Z_{1}, \mathbb{R}\right)$$
is an isomorphism; when $Z_{1}=\emptyset$ we set $j_{\emptyset, Z_{2}}=: j_{Z_{2}}$ for ease of notation. We will only need the above isomorphism when all spaces involved are $K(\pi, 1)$ 's, in which case we have for all
\end{itemize}
coefficients $A$ a commutative diagram
![](https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-15.jpg?height=223&width=539&top_left_y=474&top_left_x=757)
where the horizontal maps are isomorphisms.
2.3. (Bounded) Borel cohomology versus (bounded) continuous cohomology. Given a locally compact group $G$ and $A=\mathbb{Z}, \mathbb{R}, \mathbb{R} / \mathbb{Z}$, we have the complexes $\left(\mathrm{C}\left(G^{\bullet}, A\right)\right),\left(\mathrm{C}_{\mathrm{b}}\left(G^{\bullet}, A\right)\right),\left(\mathcal{B}\left(G^{\bullet}, A\right)\right)$ and $\left(\mathcal{B}_{\mathrm{b}}\left(G^{\bullet}, A\right)\right)$, of $A$-valued continuous, bounded continuous, Borel and bounded Borel cochains on $G$ which lead, by taking the cohomology of the $G$-invariants, to the $A$-valued continuous $\mathrm{H}_{\mathrm{c}}^{\bullet}(G, A)$, bounded continuous $\mathrm{H}_{\mathrm{cb}}^{\bullet}(G, A)$, Borel $\widehat{\mathrm{H}}_{\mathrm{c}}^{\bullet}(G, A)$ and bounded Borel $\widehat{\mathrm{H}}_{\mathrm{cb}}^{\bullet}(G, A)$ cohomology. Of course when $A=\mathbb{Z}$ the first two cohomology theories are not of much use and their Borel version is a natural substitute. We have at any rate comparison maps coming from the obvious inclusions of complexes
![](https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-15.jpg?height=214&width=467&top_left_y=1313&top_left_x=793)
For us the following facts will be of importance:
\begin{itemize}
\item[(2.] f) the short exact sequence
![](https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-15.jpg?height=50&width=543&top_left_y=1675&top_left_x=755)
gives rise to long exact sequences in Borel and bounded Borel cohomology which are compatible with respect to the comparison map;
\item[(2.] g) $\mathrm{H}_{\mathrm{cb}}^{\bullet}(G, \mathbb{R} / \mathbb{Z})=\mathrm{H}_{\mathrm{c}}^{\bullet}(G, \mathbb{R} / \mathbb{Z})$ and $\widehat{\mathrm{H}}_{\mathrm{cb}}^{\bullet}(G, \mathbb{R} / \mathbb{Z})=\widehat{\mathrm{H}}_{\mathrm{c}}^{\bullet}(G, \mathbb{R} / \mathbb{Z})$;
\item[(2.] h) if $A=\mathbb{R}, \mathbb{Z}$, then $\widehat{\mathrm{H}}_{\mathrm{c}}^{1}(G, A)=\operatorname{Hom}_{\mathrm{c}}(G, A)$ and $\mathrm{H}_{\mathrm{cb}}^{1}(G, A)=0$;
\item[(2.] i) $\mathrm{H}_{\mathrm{cb}}^{\bullet}(G, \mathbb{R})=\widehat{\mathrm{H}}_{\mathrm{cb}}^{\bullet}(G, \mathbb{R})$, which can be checked by using the regularization operators defined in [2, § 4];
\item[(2.1)] if $G$ is a Lie group, the comparison map $\mathrm{H}_{\mathrm{c}}^{\bullet}(G, \mathbb{R}) \rightarrow \widehat{\mathrm{H}}_{\mathrm{c}}^{\bullet}(G, \mathbb{R})$ is an isomorphism [52, Theorem 3].
\end{itemize}

\section*{3. Toledo numbers, basic properties and first CONSEQUENCES}
3.1. Definitions and basic properties. Let $\Sigma$ be a compact oriented surface with (possibly empty) boundary $\partial \Sigma, G$ a locally compact group and $\rho: \pi_{1}(\Sigma) \rightarrow G$ a homomorphism. Using the diagram
$$\begin{aligned}
\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R}) \xrightarrow{\rho^{*}} \mathrm{H}_{\mathrm{b}}^{2}\left(\pi_{1}(\Sigma), \mathbb{R}\right) \xrightarrow{g_{\Sigma}} & \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \mathbb{R}) \\
& \int_{j_{\partial \Sigma}} \\
& \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \partial \Sigma, \mathbb{R})
\end{aligned}$$
where $\rho^{*}$ is the pullback in bounded cohomology, $g_{\Sigma}$ the Gromov isomorphism in (2.e) and $j_{\partial \Sigma}$ is the isomorphism in (2.e) in bounded singular cohomology induced by the inclusion $(\Sigma, \emptyset) \rightarrow(\Sigma, \partial \Sigma)$, we make the following

Definition 3.1. The Toledo number of $\rho$ relative to a class $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$ is
$$\mathrm{T}_{\kappa}(\Sigma, \rho):=\left\langle\left(j_{\partial \Sigma}\right)^{-1} g_{\Sigma} \rho^{*}(\kappa),[\Sigma, \partial \Sigma]\right\rangle .$$
Here $[\Sigma, \partial \Sigma] \in \mathrm{H}^{2}(\Sigma, \partial \Sigma, \mathbb{R})$ denotes the relative fundamental class and $\left(j_{\partial \Sigma}\right)^{-1} g_{\Sigma} \rho^{*}(\kappa)$ is considered as an ordinary relative cohomology class.

When $G$ is of type (RH) the Toledo number $\mathrm{T}(\Sigma, \rho)$ of $\rho$ is defined as $\mathrm{T}_{\kappa}(\Sigma, \rho)$ where $\kappa=\kappa_{G}^{\mathrm{b}}$ is the bounded Kähler class (see § 2.1.1). The following two properties are immediate:
\begin{itemize}
\item[-] if $\rho_{1}$ and $\rho_{2}$ are $G$-conjugate, then $\mathrm{T}_{\kappa}\left(\Sigma, \rho_{1}\right)=\mathrm{T}_{\kappa}\left(\Sigma, \rho_{2}\right)$;
\item[-] if $f: \Sigma_{1} \rightarrow \Sigma_{2}$ is a continuous map of degree $d \geq 1, \rho_{i}$ : $\pi_{1}\left(\Sigma_{i}\right) \rightarrow G$ are homomorphisms related by $\rho_{1}=\rho_{2} f_{*}$, where $f_{*}$ is the morphism induced on the fundamental groups, then $\mathrm{T}_{\kappa}\left(\Sigma_{1}, \rho_{1}\right)=d \cdot \mathrm{~T}_{\kappa}\left(\Sigma_{2}, \rho_{2}\right)$.
\end{itemize}
The next results describe the behavior of the Toledo numbers under natural topological operations on surfaces.

Proposition 3.2. Let $\Sigma$ be a surface and $\rho: \pi_{1}(\Sigma) \rightarrow G$ a homomorphism.
\begin{itemize}
\item[(1)] (Additivity) If $\Sigma=\Sigma_{1} \cup_{C} \Sigma_{2}$ is the connected sum of two sub surfaces $\Sigma_{i}$ along a separating loop $C$, then
$$\mathrm{T}_{\kappa}(\Sigma, \rho)=\mathrm{T}_{\kappa}\left(\Sigma_{1}, \rho_{1}\right)+\mathrm{T}_{\kappa}\left(\Sigma_{2}, \rho_{2}\right),$$
where $\rho_{i}$ is the restriction of $\rho$ to $\pi_{1}\left(\Sigma_{i}\right)$.
\item[(2)] (Invariance under gluing) If $\Sigma^{\prime}$ is the surface obtained by cutting $\Sigma$ along a nonseparating loop $C$ and $i: \Sigma^{\prime} \rightarrow \Sigma$ is the canonical map, then
$$\mathrm{T}_{\kappa}\left(\Sigma^{\prime}, \rho i_{*}\right)=\mathrm{T}_{\kappa}(\Sigma, \rho) .$$
\end{itemize}

Proof. Here we prove the additivity property, the proof of the invariance under gluing proceeds along similar lines. Let $\alpha \in \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \partial \Sigma)$ and let
$$j:=j_{\partial \Sigma \cup C, \partial \Sigma}: \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \partial \Sigma \cup C) \rightarrow \mathrm{H}_{\mathrm{b}}^{2}(\Sigma, \partial \Sigma)$$
be the morphism given by the inclusion $(\Sigma, \partial \Sigma) \rightarrow(\Sigma, \partial \Sigma \cup C)$; notice that $j$ is an isomorphism since every connected component of $\partial \Sigma \cup C$ has amenable fundamental group. Then:
$$\begin{aligned}
\langle\alpha,[\Sigma, \partial \Sigma]\rangle & =\left\langle j^{-1}(\alpha),\left[\Sigma_{1}, \partial \Sigma_{1}\right]+\left[\Sigma_{2}, \partial \Sigma_{2}\right]\right\rangle \\
& =\left\langle\left. j^{-1}(\alpha)\right|_{\Sigma_{1}},\left[\Sigma_{1}, \partial \Sigma_{1}\right]\right\rangle+\left\langle\left. j^{-1}(\alpha)\right|_{\Sigma_{2}},\left[\Sigma_{2}, \partial \Sigma_{2}\right]\right\rangle .
\end{aligned}$$
Using that $\left.j^{-1}(\alpha)\right|_{\Sigma_{i}}=\left(j_{i}\right)^{-1}\left(\left.\alpha\right|_{\Sigma_{i}}\right)$, where $j_{i}:=j_{\partial \Sigma_{i}-C, \partial \Sigma_{i}}$ we get $\langle\alpha,[\Sigma, \partial \Sigma]\rangle=\left\langle\left(j_{1}\right)^{-1}\left(\left.\alpha\right|_{\Sigma_{1}}\right),\left[\Sigma_{1}, \partial \Sigma_{1}\right]\right\rangle+\left\langle\left(j_{2}\right)^{-1}\left(\left.\alpha\right|_{\Sigma_{2}}\right),\left[\Sigma_{2}, \partial \Sigma_{2}\right]\right\rangle$. Specializing to $j_{\partial \Sigma}(\alpha)=g_{\Sigma} \rho^{*}(\kappa)$ and observing that
$$\left(j_{i}\right)^{-1}\left(\left.\alpha\right|_{\Sigma_{i}}\right)=\left.\left(j_{i}\right)^{-1}(\alpha)\right|_{\Sigma_{i}}=\left(j_{\partial \Sigma_{i}}\right)^{-1} g_{\Sigma_{i}} \rho_{i}^{*}(\kappa)$$
concludes the proof. \(\square\)
3.2. The analytic formula. In this section we relate the Toledo numbers introduced in § 3.1 to invariants introduced and studied in [11]. Let $G$ be a locally compact group. Let $L$ be a finite connected covering of $\mathrm{PU}(1,1), \Gamma<L$ a lattice and $\rho: \Gamma \rightarrow G$ a homomorphism. Composing the transfer map
$$\mathrm{T}_{\mathrm{b}}: \mathrm{H}_{\mathrm{b}}^{2}(\Gamma, \mathbb{R}) \rightarrow \mathrm{H}_{\mathrm{cb}}^{2}(L, \mathbb{R})$$
with the pullback $\rho^{*}$, we obtain the bounded Toledo map
$$\mathrm{T}_{\mathrm{b}}(\rho): \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R}) \rightarrow \mathrm{H}_{\mathrm{cb}}^{2}(L, \mathbb{R})=\mathbb{R} \kappa_{L}^{\mathrm{b}}$$
(see [11]) which leads to an invariant $\mathrm{t}_{\mathrm{b}}(\rho, \kappa) \in \mathbb{R}$ given by
$$\mathrm{T}_{\mathrm{b}}(\rho)(\kappa)=\mathrm{t}_{\mathrm{b}}(\rho, \kappa) \kappa_{L}^{\mathrm{b}}$$
for $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$. When $G$ is of type (RH) we set, in analogy with § 3.1,
$$\mathrm{t}_{\mathrm{b}}(\rho)=\mathrm{t}_{\mathrm{b}}\left(\rho, \kappa_{G}^{\mathrm{b}}\right) .$$
Theorem 3.3. Let $h: \pi_{1}(\Sigma) \rightarrow \Gamma$ be an isomorphism whose composition with the projection to $\operatorname{PU}(1,1)$ is the developing homomorphism of a complete hyperbolic structure on $\Sigma^{\circ}$ with finite area. Then
$$\mathrm{T}_{\kappa}(\Sigma, \rho)=|\chi(\Sigma)| \mathrm{t}_{\mathrm{b}}\left(\rho \circ h^{-1}, \kappa\right)$$
for any homomorphism $\rho: \pi_{1}(\Sigma) \rightarrow G$ and $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$.
We defer the proof of this theorem until § 3.3 and collect here a few important consequences.

Corollary 3.4. We have the following Milnor-Wood type bounds:
\begin{itemize}
\item[(1)] $\left|\mathrm{T}_{\kappa}(\Sigma, \rho)\right| \leq 2|\chi(\Sigma)|\|\kappa\|$;
\item[(2)] if $G$ is of type ( $R H$ ), then $|\mathrm{T}(\Sigma, \rho)| \leq|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}}$.
\end{itemize}

Proof. The first assertion follows from Theorem 3.3 and the fact that the transfer $\mathrm{T}_{\mathrm{b}}$ and the pullback are both norm decreasing. The second assertion follows from the first one and the equality $\left\|\kappa_{G}^{\mathrm{b}}\right\|=\frac{\mathrm{r}_{\mathcal{X}}}{2}$ (see § 2.1). \(\square\)

The following are then the two main concepts of this paper:
Definition 3.5. Let $G$ be a group of type (RH).
\begin{itemize}
\item[(1)] A homomorphism $\rho: \pi_{1}(\Sigma) \rightarrow G$ of a surface group $\pi_{1}(\Sigma)$ is maximal if $\mathrm{T}(\Sigma, \rho)=|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}}$.
\item[(2)] A homomorphism $\rho: \Gamma \rightarrow G$ of a lattice $\Gamma<L$ is maximal if $\mathrm{t}_{\mathrm{b}}(\rho)=\mathrm{r}_{\mathcal{X}}$.
\end{itemize}

Observe that the first definition generalizes the concept of maximal representation given in the introduction and puts it in the context of groups of type (RH) which will turn out to be the right one for the proofs. The second concept of maximality is equivalent to the one introduced in [11], the equivalence being given by [11, Lemma 5.3]. The relationship between the above definitions is given by Theorem 3.3.

Proof of Theorem 3. Let $h: \pi_{1}(\Sigma) \rightarrow \mathrm{PU}(1,1)$ be a hyperbolization of $\Sigma^{\circ}$ with finite area and image $\Gamma$; in particular $h$ is induced by a diffeomorphism $f: \Sigma^{\circ} \rightarrow \Gamma \backslash \mathbb{D}$. Let $\rho: \pi_{1}(\Sigma) \rightarrow \mathrm{PU}(1,1)$ be a homomorphism. If $\rho$ is maximal, then, by Theorem 3.3, $\rho \circ h^{-1}: \Gamma \rightarrow G$ is maximal as a representation of the lattice $\Gamma$ and it follows then from [11, Lemma 5.2 and Corollary 11] that $\rho \circ h^{-1}$ is induced by a diffeomorphism
$$f_{\rho}: \Gamma \backslash \mathbb{D} \rightarrow \rho\left(\pi_{1}(\Sigma)\right) \backslash \mathbb{D}$$
which implies that $\rho$ itself is induced by the diffeomorphism
$$f_{\rho} \circ f: \Sigma^{\circ} \rightarrow \rho\left(\pi_{1}(\Sigma)\right) \backslash \mathbb{D} .$$

Conversely, if $\rho$ is induced by a complete hyperbolic metric on $\Sigma^{\circ}$, there exists a semiconjugation $F: \partial \mathbb{D} \rightarrow \partial \mathbb{D}$ in the sense of Ghys [25] with $\rho(\gamma) F=F h(\gamma)$. Since $\kappa_{\mathrm{PU}(1,1)}^{\mathrm{b}}$ is the bounded real Euler class [25], we have that
$$\rho^{*}\left(\kappa_{\mathrm{PU}(1,1)}^{\mathrm{b}}\right)=h^{*}\left(\kappa_{\mathrm{PU}(1,1)}^{\mathrm{b}}\right)$$
and hence
$$\left(\rho \circ h^{-1}\right)^{*}\left(\kappa_{\mathrm{PU}(1,1)}^{\mathrm{b}}\right)=\left.\kappa_{\mathrm{PU}(1,1)}^{\mathrm{b}}\right|_{\Gamma}$$
which, applying the transfer map, implies that $\mathrm{t}_{\mathrm{b}}\left(\rho \circ h^{-1}\right)=1$ and thus $\rho$ is maximal by Theorem 3.3. \(\square\)
3.3. Proof of Theorem 3.3. The statement of Theorem 3.3 can be reformulated as follows. Let $\Gamma<L$ be a torsionfree lattice; we consider the finite area surface $S=\Gamma \backslash \mathbb{D}$ as interior of a compact surface $\bar{S}$ with boundary $\partial \bar{S}$, which is a union of circles. Given a homomorphism $\rho: \Gamma \rightarrow G$ and identifying $\Gamma$ with $\pi_{1}(S)=\pi_{1}(\bar{S})$, the assertion is that
$$\mathrm{T}_{\kappa}(\bar{S}, \rho)=|\chi(S)| \mathrm{t}_{\mathrm{b}}(\kappa, \rho) .$$
For $T \geq 0$ large enough, let $S_{\geq T}$ denote the union of the convex cusp neighborhoods bounded by horocycles of length $1 / T$. It is easy to verify that if $\beta \in \mathrm{H}_{\mathrm{b}}^{2}(\Gamma, \mathbb{R})$ we have
$$\left\langle\left(j_{\partial \bar{S}}\right)^{-1} g_{\bar{S}}(\beta),[\bar{S}, \partial \bar{S}]\right\rangle=\left\langle\left(j_{T}\right)^{-1} g_{S}(\beta),\left[S, S_{\geq T}\right]\right\rangle$$
where, for ease of notation, $j_{T}$ refers to the canonical isomorphism
$$\mathrm{H}_{\mathrm{b}}^{2}\left(S, S_{\geq T}, \mathbb{R}\right) \rightarrow \mathrm{H}_{\mathrm{b}}^{2}(S, \mathbb{R}) .$$
Introducing the notation
$$\mathrm{T}_{\mathrm{b}}(\beta)=\tau(\beta) \kappa_{L}^{\mathrm{b}},$$
where $\mathrm{T}_{\mathrm{b}}$ is the transfer operator, the theorem will then follow from (3.1) and the proposition below applied to $\beta=\rho^{*}(\kappa)$.

Proposition 3.6. With the above notation
$$\left\langle\left(j_{T}\right)^{-1} g_{S}(\beta),\left[S, S_{\geq T}\right]\right\rangle=\tau(\beta)|\chi(S)| .$$

The rest of this subsection is devoted to the proof of Proposition 3.6 for which we will need the three lemmas below. We fix the following notation, if $Y$ is any topological space, let $S_{m}(Y)$ denote the set of singular $m$-simplices and $F_{\mathrm{b}}(Y, \mathbb{R})$ the space of bounded $m$-cochains.

Lemma 3.7 (Loeh-Strohm, [41, Theorem 2.37]). Let $U \subset \mathbb{D}$ be a convex subset and $\Lambda<L$ be a discrete torsionfree subgroup preserving $U$. The canonical isomorphism
$$\mathrm{H}_{\mathrm{b}}^{m}(\Lambda, \mathbb{R}) \xrightarrow{\cong} \mathrm{H}_{\mathrm{b}}^{m}(\Lambda \backslash U, \mathbb{R})$$
can be implemented by the map
$$\begin{aligned}
\mathrm{C}_{\mathrm{b}, \text { alt }}\left(U^{m+1}, \mathbb{R}\right)^{\Lambda} & \rightarrow F_{\mathrm{b}}^{m}(\Lambda \backslash U, \mathbb{R}) \\
f & \longmapsto \bar{f},
\end{aligned}$$
defined by $\bar{f}(\sigma):=f\left(\tilde{\sigma}_{0}, \ldots, \tilde{\sigma}_{m}\right)$, where $\sigma: \Delta^{m} \rightarrow \Lambda \backslash U$ is an $m$ simplex and $\tilde{\sigma}: \Delta^{m} \rightarrow U$ is a lift with vertices $\tilde{\sigma}_{0}, \ldots, \tilde{\sigma}_{m}$.

The next lemma follows from standard properties of the transfer map and will also be useful later on. Let $A(x, y, z)$ denote the area of a geodesic triangle in $\mathbb{D}$ with vertices $x, y, z$, and let $\mu$ be the $L$-invariant probability measure on $\Gamma \backslash L$.

Lemma 3.8. Let $a \in \mathrm{C}_{\mathrm{b}, \text { alt }}\left(\mathbb{D}^{3}, \mathbb{R}\right)^{\Gamma}$ be a representative of the class $\beta \in \mathrm{H}_{\mathrm{b}}^{2}(\Gamma, \mathbb{R})$. Then
$$\int_{\Gamma \backslash L} a(g x, g y, g z) d \mu(g)=\frac{\tau(\beta)}{2 \pi} A(x, y, z) .$$

We will also need to represent the relative cycle $\left[S, S_{\geq T}\right]$ using smearing in the context of relative measure homology. For $\epsilon \in S_{2}(\mathbb{D})$ we consider as usual the continuous map
$$\begin{aligned}
m_{\epsilon}: \Gamma \backslash L & \rightarrow S_{2}(S) \\
\Gamma g & \mapsto p(g \epsilon)
\end{aligned}$$
where $p: \mathbb{D} \rightarrow S$ is the canonical projection and define
$$S m_{T}(\epsilon)=\left(m_{\epsilon}\right)_{*}\left(\left.\mu\right|_{(\Gamma \backslash L)_{T}}\right),$$
where $(\Gamma \backslash L)_{T}=\left\{\Gamma g \in \Gamma \backslash L: p(g 0) \in S_{\leq T}\right\}$ and $S_{\leq T}$ is the complement of $S_{\geq T}$. The following is then a verification proceeding along standard arguments.

Lemma 3.9. Let $\sigma: \Delta^{2} \rightarrow \mathbb{D}$ be a geodesic simplex and $\sigma^{\prime}$ its reflection alone one side. Then there is $C>1$ such that the boundary of the measured chain
$$\mu_{C T}:=S m_{C T}(\sigma)-S m_{C T}\left(\sigma^{\prime}\right)$$
has it support in $S_{1}\left(S_{\geq T}\right)$ and $\mu_{C T}$ represents the relative cycle
$$\frac{2 A(\sigma)}{A(S)}\left[S, S_{\geq T}\right]$$
where $A$ refers to the hyperbolic area.
Proof of Proposition 3.6. In the notation of Lemma 3.7, let $a \in \mathrm{C}_{\mathrm{b}, \text { alt }}\left(D^{3}, \mathbb{R}\right)^{\Gamma}$ be such that $\bar{a}$ is a representative of $g_{S}(\beta)$. Then for $T_{0}$ large enough $\bar{a}$ restricted to $S_{\geq T_{0}}$ is trivial in bounded cohomology and using Lemma 3.7 applied to appropriate cusp neighborhoods we get a continuous bounded function
$$\bar{f}: S_{1}\left(S_{\geq T_{0}}\right) \rightarrow \mathbb{R}$$
with $\left.\bar{a}\right|_{S_{2}\left(S_{\geq T_{0}}\right)}=d \bar{f}$.
For $T \geq T_{0}$ define $f_{T}: S_{1}(S) \rightarrow \mathbb{R}$ as being equal to $\bar{f}$ on simplices in $S_{\geq T}$ and zero otherwise, and let $a_{T}:=\bar{a}-d f_{T}$. Then $a_{T}$ is a bounded

Borel function on $S_{2}(S)$ and $\left\|a_{T}\right\|_{\infty} \leq C$ for some constant $C>0$. Moreover $a_{T}$ is a representative of $\left(j_{T}\right)^{-1} g_{S}(\beta)$. For $T_{2} \geq T_{1} \geq T_{0}$ we clearly have
$$\left\langle\left(j_{T_{1}}\right)^{-1} g_{S}(\beta),\left[S, S_{\geq T_{1}}\right]\right\rangle=\left\langle\left(j_{T_{1}}\right)^{-1} g_{S}(\beta),\left[S, S_{\geq T_{2}}\right]\right\rangle .$$
According to Lemma 3.9 the right hand side equals
$$\left\langle a_{T_{1}}, \frac{A(S)}{2 A(\sigma)} \mu_{C T_{2}}\right\rangle$$
which, letting $T_{2} \rightarrow \infty$, gives
$$\frac{A(S)}{2 A(\sigma)} \int_{\Gamma \backslash L}\left(a_{T_{1}}(p g(\sigma))-a_{T_{1}}\left(p g\left(\sigma^{\prime}\right)\right)\right) d \mu(g) .$$
Since however the left hand side of (3.2) is independent of $T_{1}$, we let $T_{1} \rightarrow \infty$ and, using the dominated convergence theorem, obtain
$$\begin{aligned}
& \left\langle\left(j_{T}\right)^{-1} g_{S}(\beta),\left[S, S_{\geq T}\right]\right\rangle \\
= & \frac{A(S)}{2 A(\sigma)} \int_{\Gamma \backslash L}\left(a\left(g \sigma_{0}, g \sigma_{1}, g \sigma_{2}\right)-a\left(g \sigma_{0}^{\prime}, g \sigma_{1}^{\prime}, g \sigma_{2}^{\prime}\right)\right) d \mu(g)
\end{aligned}$$
which, together with Lemma 3.8 proves the proposition. \(\square\)
3.4. Continuity. We will now use Theorem 3.3 to show the following

Proposition 3.10. Let $G$ be a group of Hermitian type and let $\kappa \in$ $\mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$. Then the map
$$\begin{aligned}
\mathrm{T}_{\kappa}(\Sigma, \cdot): \operatorname{Hom}\left(\pi_{1}(\Sigma), G\right) & \longrightarrow \mathbb{R} \\
\rho & \mapsto \mathrm{T}_{\kappa}(\Sigma, \rho)
\end{aligned}$$
is continuous.
Together with the following basic example of maximal representation, the continuity of $\rho \mapsto \mathrm{T}_{\kappa}(\Sigma, \rho)$ allows us to determine the range of the map in (3.3) when $\kappa=\kappa_{G}^{\mathrm{b}}$ and $\partial \Sigma \neq \emptyset$.

Example 3.11. Let $G$ be of Hermitian type with associated symmetric space $\mathcal{X}, d: \mathbb{D} \rightarrow \mathcal{X}$ a diagonal disk (see (2,b)) and $\Delta: L \rightarrow G$ the corresponding homomorphism, where $L$ is an appropriate finite covering of $\mathrm{PU}(1,1)$. Then if $h: \pi_{1}(\Sigma) \rightarrow \Gamma<L$ is a finite area hyperbolization of $\Sigma^{\circ}$, the homomorphism $\rho:=\Delta \circ h$ is maximal. Indeed, we have that
$$\Delta^{*}\left(\kappa_{G}^{\mathrm{b}}\right)=\mathrm{r}_{\mathcal{X}} \kappa_{L}^{\mathrm{b}}$$
and hence (Theorem 3.3)
$$\mathrm{T}(\Sigma, \Delta \circ h)=|\chi(\Sigma)| \mathrm{t}_{\mathrm{b}}\left(\left.\Delta\right|_{\Gamma}\right)=|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}} .$$

Observe that if $d^{\prime}$ is the composition of $d$ with an antiholomorphic isometry of $\mathbb{D}$ and $\Delta^{\prime}: L \rightarrow G$ is the corresponding homomorphism, then $\mathrm{T}\left(\Sigma, \Delta^{\prime} \circ h\right)=-|\chi(\Sigma)| \mathrm{r}_{\mathcal{X}}$.

Corollary 3.12. Assume that $\partial \Sigma \neq \emptyset$. Then the range of the map $T(\Sigma, \cdot)$ is the interval $\left[-\mathrm{r}_{\mathcal{X}}|\chi(\Sigma)|, \mathrm{r}_{\mathcal{X}}|\chi(\Sigma)|\right]$.

Proof. By Corollary 3.4 the range is contained in the above interval and, by Example 3.11 it contains the endpoints. Since $\partial \Sigma \neq \emptyset, \pi_{1}(\Sigma)$ is a free group and hence $\operatorname{Hom}\left(\pi_{1}(\Sigma), G\right)$ is connected. The corollary then follows from Proposition 3.10. \(\square\)

Turning now to the proof of Proposition 3.10 we will need the following:

Lemma 3.13. Let $G$ be a connected semisimple Lie group with associated symmetric space $\mathcal{X}$, let $\mathrm{C}(\mathbb{D}, \mathcal{X})$ be the space of continuous maps from the Poincaré disk $\mathbb{D}$ into $\mathcal{X}$, with the topology of uniform convergence on compact sets, and let $\Gamma$ be a torsionfree lattice in PU(1,1). Then there is a continuous map
$$\begin{aligned}
\operatorname{Hom}(\Gamma, G) & \rightarrow \mathrm{C}(\mathbb{D}, \mathcal{X}) \\
\rho & \mapsto F_{\rho}
\end{aligned}$$
such that $F_{\rho}$ is equivariant with respect to $\rho: \Gamma \rightarrow G$.
Proof. Let $\mathcal{K}$ be a simplicial complex such that $|\mathcal{K}|$ is homeomorphic to $\Gamma \backslash \mathbb{D}$. Let $\rho: \Gamma \rightarrow G$ be a homomorphism and $F: \widetilde{\mathcal{K}}^{(0)} \rightarrow \mathcal{X}$ a $\rho$ -equivariant map defined on the 0-skeleton of the universal covering of $\mathcal{K}$. Using barycentric coordinates on the simplices of $\widetilde{\mathcal{K}}$ and the center of mass in $\mathcal{X}$, one obtains a canonical continuous extension $F^{\text {ext }}: \widetilde{\mathcal{K}} \rightarrow$ $\mathcal{X}$ which is thus $\rho$-equivariant and depends continuously on $F$. Fix $Y \subset \widetilde{\mathcal{K}}^{(0)}$ a complete set of representatives of $\Gamma$-orbits in $\widetilde{\mathcal{K}}^{(0)}$ and fix any map $f: Y \rightarrow \mathcal{X}$. Then given $\rho: \Gamma \rightarrow G$, we define $f_{\rho}: \widetilde{\mathcal{K}}^{(0)} \rightarrow \mathcal{X}$ as the unique $\rho$-equivariant extension of $f$ and $F_{\rho}:=\left(f_{\rho}\right)^{\text {ext }}$. The assertion that $\rho \mapsto F_{\rho}$ is continuous follows from the continuity of the center of mass construction in $\mathcal{X}$. \(\square\)

Proof of Proposition 3.10. We realize, as we may, the bounded continuous cohomology of $G$ on the complex $\left(\mathrm{C}_{\mathrm{b}, \text { alt }}\left(\mathcal{X}^{\bullet}, \mathbb{R}\right)\right)$ of bounded continuous alternating cochains on $\mathcal{X}$ and similarly for $L$ and $\Gamma$ on $\left(\mathrm{C}_{\mathrm{b}, \text { alt }}\left(\mathbb{D}^{\bullet}, \mathbb{R}\right)\right)$. Given a homomorphism $\rho: \Gamma \rightarrow G$, the continuous $\rho$-equivariant map $F_{\rho} \in \mathrm{C}(\mathbb{D}, \mathcal{X})$ in the previous lemma induces by precomposition a map of complexes
$$\left(\mathrm{C}_{\mathrm{b}, \text { alt }}\left(\mathcal{X}^{\bullet}, \mathbb{R}\right)\right)^{G} \rightarrow\left(\mathrm{C}_{\mathrm{b}, \text { alt }}\left(\mathbb{D}^{\bullet}, \mathbb{R}\right)\right)^{\Gamma}$$
which, according to [9], represents the pullback $\rho^{*}: \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R}) \rightarrow$ $\mathrm{H}_{\mathrm{b}}^{2}(\Gamma, \mathbb{R})$. In particular, if $c: \mathcal{X}^{3} \rightarrow \mathbb{R}$ is a bounded continuous $G$ invariant alternating cocycle representing $\kappa \in \mathrm{H}_{\mathrm{cb}}^{2}(G, \mathbb{R})$, then the cocycle
$$\left(z_{1}, z_{2}, z_{3}\right) \mapsto c\left(F_{\rho}\left(z_{1}\right), F_{\rho}\left(z_{2}\right), F_{\rho}\left(z_{3}\right)\right)$$
represents $\rho^{*}(\kappa) \in \mathrm{H}_{\mathrm{b}}^{2}(\Gamma, \mathbb{R})$ [9]. We deduce then from Lemma 3.8 that
$$\int_{\Gamma \backslash L} c\left(F_{\rho}\left(g z_{1}\right), F_{\rho}\left(g z_{2}\right), F_{\rho}\left(g z_{3}\right)\right) d \mu(g)=\frac{1}{2 \pi} \mathrm{t}_{\mathrm{b}}(\rho, \kappa) A\left(z_{1}, z_{2}, z_{3}\right) .$$

If now $\rho_{n} \rightarrow \rho$, then according to Lemma $3.13 F_{\rho_{n}} \rightarrow F_{\rho}$ uniformly on compact sets and hence
$$c\left(F_{\rho_{n}}\left(g z_{1}\right), F_{\rho_{n}}\left(g z_{2}\right), F_{\rho_{n}}\left(g z_{3}\right)\right) \rightarrow c\left(F_{\rho}\left(g z_{1}\right), F_{\rho}\left(g z_{2}\right), F_{\rho}\left(g z_{3}\right)\right)$$
pointwise. Since
$$\left|c\left(F_{\rho_{n}}\left(g z_{1}\right), F_{\rho_{n}}\left(g z_{2}\right), F_{\rho_{n}}\left(g z_{3}\right)\right)\right| \leq\|c\|_{\infty},$$
the dominated convergence theorem implies that $\mathrm{t}_{\mathrm{b}}\left(\rho_{n}, \kappa\right) \rightarrow \mathrm{t}_{\mathrm{b}}(\rho, \kappa)$. \(\square\)

\section*{4. Structure of maximal representations: the Zariski DENSE CASE}

In this section we will investigate the structure of maximal homomorphisms $\rho: \Gamma \rightarrow G$, where, as before, $\Gamma<L$ is a lattice in a finite connected covering $L$ of $\mathrm{PU}(1,1), G=\operatorname{Iso}(\mathcal{X})^{\circ}$ is the connected component of the group of isometries of an irreducible Hermitian symmetric space $\mathcal{X}$, and we assume now that the image of $\rho$ is Zariski dense. More precisely, if G is the connected adjoint $\mathbb{R}$-group associated to the complexification of the Lie algebra of $G$, we will prove the following:

Theorem 4.1. If $\rho: \Gamma \rightarrow \mathbf{G}(\mathbb{R})^{\circ}$ is a maximal representation with Zariski dense image, then:
\begin{itemize}
\item[(1)] the Hermitian symmetric space $\mathcal{X}$ is of tube type;
\item[(2)] the image of $\rho$ is discrete;
\item[(3)] the representation $\rho$ is injective, modulo possibly the center $\mathcal{Z}(\Gamma)$ of $\Gamma$.
\end{itemize}
4.1. The formula. Here we will use heavily the results of [14]. In particular, let $\mathcal{D}$ be the bounded domain realization of $\mathcal{X}$ and $\check{S}$ its Shilov boundary. Recall that $\check{S}=G / Q$ where $Q$ is a specific maximal parabolic subgroup of $G$; and denote by $\check{S}^{(2)}$ the set of pairs of transverse points in $\check{S}$.

The lattice $\Gamma$ acts on the boundary of the Poincaré disk $\partial \mathbb{D}$ and, as is well known, the space $(\partial \mathbb{D}, \lambda)$ where $\lambda$ is the round measure on $\partial \mathbb{D}$ is a Poisson boundary for $\Gamma$; moreover, the $\Gamma$-action on $\partial \mathbb{D} \times \partial \mathbb{D}$ is ergodic. With this we can apply [10, Proposition 7.2] and [14, Theorem 4.7] to conclude:

Theorem 4.2. Assume that $\rho: \Gamma \rightarrow \mathbf{G}(\mathbb{R})^{\circ}=G$ is a homomorphism with Zariski dense image. Then there exists a $\rho$-equivariant measurable map $\varphi: \partial \mathbb{D} \rightarrow \check{S}$ such that $\left(\varphi\left(x_{1}\right), \varphi\left(x_{2}\right)\right) \in \check{S}^{(2)}$ for almost all $\left(x_{1}, x_{2}\right) \in(\partial \mathbb{D})^{2}$.

Using the boundary map $\varphi$, we now give an explicit cocycle on $(\partial \mathbb{D})^{3}$ representing the pullback $\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right) \in \mathrm{H}_{\mathrm{b}}^{2}(\Gamma, \mathbb{R})$. To this purpose, if $\beta_{\check{S}}$ : $\check{S}^{3} \rightarrow \mathbb{R}$ is the generalized Maslov cocycle (see § 2.1.3), we have:

Corollary 4.3 ([14, Proposition 4.6]). Under the canonical isomorphism
$$\mathrm{H}_{\mathrm{b}}^{2}(\Gamma, \mathbb{R}) \cong \mathcal{Z} L_{\mathrm{w} *, \text { alt }}^{\infty}\left((\partial \mathbb{D})^{3}, \mathbb{R}\right)^{\Gamma}$$
the class $\rho_{\mathrm{b}}^{*}\left(\kappa_{G}^{\mathrm{b}}\right)$ corresponds to the cocycle
$$\begin{aligned}
(\partial \mathbb{D})^{3} & \longrightarrow \\
(x, y, z) & \longmapsto \beta_{\breve{S}}(\varphi(x), \varphi(y), \varphi(z)) .
\end{aligned}$$

We then conclude:
Corollary 4.4. Let $\rho: \Gamma \rightarrow G=\mathbf{G}(\mathbb{R})^{\circ}$ be a homomorphism with Zariski dense image and $\varphi: \partial \mathbb{D} \rightarrow \check{S}$ a measurable $\rho$-equivariant boundary map. Then if $\mu$ is the L-invariant probability measure on $\Gamma \backslash L$, we have that
$$\int_{\Gamma \backslash L} \beta_{\check{S}}(\varphi(g x), \varphi(g y), \varphi(g z)) d \mu(g)=\mathrm{t}_{\mathrm{b}}(\rho) \beta_{\partial \mathbb{D}}(x, y, z)$$
for almost every $(x, y, z) \in(\partial \mathbb{D})^{3}$. In particular, if $\rho$ is maximal,
$$\beta_{\check{S}}(\varphi(x), \varphi(y), \varphi(z))=\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}(x, y, z)$$
for almost every $(x, y, z) \in \partial \mathbb{D}$ and thus
$$\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)=\mathrm{r}_{\mathcal{X}} \kappa_{L}^{\mathrm{b}} .$$
Proof. We have that
$$\mathrm{T}_{\mathrm{b}}\left(\rho^{*}\left(\kappa_{G}^{\mathrm{b}}\right)\right)=\mathrm{t}_{\mathrm{b}}(\rho) \kappa_{L}^{\mathrm{b}},$$
so that the formula follows from Corollary 4.3 and the functoriality of the transfer operator in [46, III.8].

Assume now that $\rho$ is maximal, that is $\mathrm{t}_{\mathrm{b}}(\rho)=\mathrm{r}_{\mathcal{X}}$. Fix $\left(x_{0}, y_{0}, z_{0}\right) \in$ $(\partial \mathbb{D})^{3}$ such that $\beta_{\partial \mathbb{D}}\left(x_{0}, y_{0}, z_{0}\right)=\frac{1}{2}$ and (4.1) holds. Since for every $a, b, c \in \check{S}$
$$\left|\beta_{\check{S}}(a, b, c)\right| \leq \frac{\mathrm{r}_{\mathcal{X}}}{2},$$
([21] - see also [14, Theorem 4.2]) and since $\mu$ is a probability measure, we deduce from (4.1) that for almost every $g \in L$
$$\beta_{\check{S}}\left(\varphi\left(g x_{0}\right), \varphi\left(g y_{0}\right), \varphi\left(g z_{0}\right)\right)=\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}\left(x_{0}, y_{0}, z_{0}\right) .$$
Similarly, if $\beta_{\partial \mathbb{D}}\left(x_{0}, y_{0}, z_{0}\right)=-\frac{1}{2}$, by the same argument we deduce that (4.4) holds for almost every $g \in L$. Thus the function on $(\partial \mathbb{D})^{3}$
$$(x, y, z) \mapsto \beta_{\breve{S}}(\varphi(x), \varphi(y), \varphi(z))$$
is essentially $L$-invariant and (4.4) implies then that this function coincides almost everywhere with $\mathrm{r}_{\mathcal{X}} \beta_{\partial \mathbb{D}}$. \(\square\)
4.2. $\mathcal{X}$ is of tube type. In this section we prove the first assertion of Theorem 4.1. For this we will use our characterization of tube type domains obtained in [14]. In particular we defined in [14, § 2.4] the Hermitian triple product, a $G$-invariant map
$$\langle\langle\cdot, \cdot, \cdot\rangle\rangle: \check{S}^{(3)} \rightarrow \mathbb{R}^{\times} \backslash \mathbb{C}^{\times}$$
on the set $\check{S}^{(3)}$ of triples of points in $\check{S}$ which are pairwise transverse, and which is related to the generalized Maslov cocycle by
$$\langle\langle x, y, z\rangle\rangle \equiv e^{i \pi p_{\mathcal{X}} \beta_{\tilde{S}}(x, y, z)} \quad \bmod \mathbb{R}^{\times}$$
for all $(x, y, z) \in \check{S}^{(3)}$, where $p_{\mathcal{X}}$ is an integer defined in terms of the root system associated to $G$. Let $\check{S}=G / Q$ and $\mathbf{Q}$ be the $\mathbb{R}$-parabolic subgroup of G with $\mathbf{Q}(\mathbb{R})=Q$.

Then if $A^{\times}$is the $\mathbb{R}$-algebraic group $\mathbb{C}^{\times} \times \mathbb{C}^{\times}$(with real structure $(\lambda, \mu) \mapsto(\bar{\mu}, \bar{\lambda}))$ and $\mathbb{C}^{\times} \mathbb{1}=\left\{(\lambda, \lambda) \in A: \lambda \in \mathbb{C}^{\times}\right\}$, we constructed a rational G-invariant map defined over $\mathbb{R}$
$$\langle\langle\cdot, \cdot, \cdot\rangle\rangle_{\mathbb{C}}:(\mathbf{G} / \mathbf{Q})^{3} \rightarrow \mathbb{C}^{\times} \mathbb{1} \backslash A^{\times},$$
which we called the complex Hermitian triple product, and which is related to the Hermitian triple product by the commutative diagram
![](https://cdn.mathpix.com/cropped/4c2b5273-bae1-4a9e-bc17-559dcbfd0d15-25.jpg?height=223&width=518&top_left_y=2207&top_left_x=767)
where $\imath$ is given by the $G$-map $\imath: \breve{S} \rightarrow \mathbf{G} / \mathbf{Q}$ sending $\check{S}$ to $(\mathbf{G} / \mathbf{Q})(\mathbb{R})$, and $\Delta([\lambda])=[(\lambda, \bar{\lambda})]$, (see [14, Corollary 2.11]); the statement includes the fact that the domain of definition of $\langle\langle\cdot, \cdot, \cdot\rangle\rangle_{\mathbb{C}}$ contains $\check{S}^{(3)}$.