---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: [math/0206047] Seiberg-Witten-Floer Homology and Gluing Formulae]

---
source_file: math_0206047.pdf
converter: mathpix
format: mmd
---

\title{
Seiberg-Witten-Floer Homology and Gluing Formulae
}

\author{
Alan L. Carey, Bai-Ling Wang
}

\begin{abstract}
This paper gives a detailed construction of Seiberg-Witten-Floer homology for a closed oriented 3-manifold with a non-torsion Spin ${ }^{c}$ structure. Gluing formulae for certain 4-dimensional manifolds splitting along an embedded 3-manifold are obtained.
\end{abstract}

\section*{Contents}
1 Introduction and statement of results ..... 2
2 Seiberg-Witten monopoles on 3-manifolds: review ..... 7
3 Seiberg-Witten-Floer homology ..... 12
3.1 The basics of the CSD functional: critical points, relative indices ..... 12
3.2 Estimates on gradient flowlines ..... 17
3.3 Moduli spaces of flowlines: transversality, compactification and orientibility. ..... 22
3.4 Seiberg-Witten-Floer homology: definition and properties ..... 35
3.5 Variants of the Seiberg-Witten-Floer homology ..... 40
4 Gluing formulae for 4-dimensional Seiberg-Witten invariants ..... 43
4.1 Moduli space for 4-manifolds with cylindrical ends ..... 44
4.2 Relative invariants for 4-manifolds with boundary ..... 50
4.3 Gluing formulae for the Seiberg-Witten invariants ..... 53
References ..... 60

\section*{1 Introduction and statement of results}

In this paper we give a detailed account of the construction of Seiberg-Witten-Floer homology for a closed oriented 3-manifold $Y$ with a non-torsion Spin ${ }^{c}$ structure $\mathfrak{s}$ and discuss some applications. The basic idea is to think of the Seiberg-Witten equations as defining critical points for the Chern-Simons-Dirac functional. This functional is on the configuration space (which consists of pairs of $U(1)$ connections and spinors modulo the gauge transformations) but may have degenerate critical points. These can be removed by a suitable perturbation. To construct the Seiberg-Witten-Floer homology one proceeds to study the time independent gradient flow lines from one critical point to another. These flow lines or trajectories may be thought of as solutions to the Seiberg-Witten equations in temporal gauge on the four manifold $Y \times \mathbb{R}$. A suitable choice of perturbation of the Chern-Simons-Dirac functional gives the desired properties (such as smoothness and transversality) for the moduli space of trajectory flowlines.

We now summarise the contents of the paper. In section 2, we review the basic properties of Seiberg-Witten monopoles on a closed, oriented 3-manifold $(Y, g, \mathfrak{s})$ with Spin ${ }^{c}$ structure $\mathfrak{s}$ and metric $g$. Section 3 gives a complete account of the infinite dimensional Morse theory for the Chern-Simons-Dirac functional whose critical points satisfy the Seiberg-Witten equations on $(Y, g, \mathfrak{s})$. The downward gradient flowline of the Chern-Simons-Dirac functional, thought as a solution to the Seiberg-Witten equations on a cylinder $\mathbb{R} \times Y$, is endowed with an energy function (22), such that when the energy is sufficiently small, the flowline stays in a small neighbourhood of some critical point (see Lemma 3.8). This enables us to analyse the local behaviour of any gradient flowline near a critical point in Proposition 3.9, under the small energy condition.

In order to achieve transversality for the moduli space of flowline, we adopt the sort of perturbations suggested by Kronheimer [14] with an additional condition 3.12. We also show that, for generic perturbations, the moduli space of flowlines with finite energy is smooth for each connected component (cf. Theorem 3.16), which can be compactified to a smooth manifold with corners (cf. Proposition 3.18).

The analysis developed in this paper can be applied to more general cases but we only discuss one namely Seiberg-Witten-Floer homology theory for a closed oriented 3-manifold $Y$ with $b_{1}(Y)>0$ and a $\operatorname{Spin}^{c}$ structure $\mathfrak{s}$ such that $c_{1}(\mathfrak{s})$ is non-torsion. For any rational homology 3-sphere, there exists an equivariant Seiberg-Witten Floer homology in [20], which is a topological invariant of the underlying manifold and $\operatorname{Spin}^{c}$ structure. For the case of $(Y, \mathfrak{s})$ with $b_{1}(Y)>0$ and $c_{1}(\mathfrak{s})=0$, Seiberg-Witten-Floer homology theory will be investigated elsewhere [21]. The results on Seiberg-Witten-Floer homology for a closed 3-manifold $Y$ with $b_{1}(Y)>0$ and a non-torsion Spin ${ }^{c}$ structure in this paper are summarized in the following theorem, whose proof will be given in section 3.

Theorem 1.1. For any closed oriented 3-manifold $Y$ with $b_{1}(Y)>0$ and a Spin ${ }^{c}$ structure $\mathfrak{s}$ such that $c_{1}(\mathfrak{s}) \neq 0$ in $H^{2}(Y, \mathbb{Z}) /$ Torsion, let $d(\mathfrak{s})$ be the divisibility of $c_{1}(\mathfrak{s})$ in $H^{2}(Y, \mathbb{Z}) /$ Torsion, that is
$$d(\mathfrak{s})=g . c . d .\left\{<c_{1}(\mathfrak{s}), \sigma>: \text { for } \sigma \in H_{2}(Y, \mathbb{Z})\right\} .$$
Then there exists a finitely generated Seiberg-Witten-Floer complex whose homology $H F_{*}^{S W}(Y, \mathfrak{s})$ satisfies the following properties:
\begin{itemize}
\item[1.] $H F_{*}^{S W}(Y, \mathfrak{s})$ is a topological invariant of $(Y, \mathfrak{s})$ and is a $\mathbb{Z}_{d(\mathfrak{s})}$-graded Abelian group.
\item[2.] There is an action of
$$\mathbb{A}(Y)=\operatorname{Sym}^{*}\left(H_{0}(Y, \mathbb{Z})\right) \otimes \Lambda^{*}\left(H_{1}(Y, \mathbb{Z}) / \text { Torsion }\right)$$
on $H F_{*}^{S W}(Y, \mathfrak{s})$ with elements in $H_{0}(Y, \mathbb{Z})$ and $H_{1}(Y, \mathbb{Z}) /$ Torsion decreasing degree in $H F_{*}^{S W}(Y, \mathfrak{s})$ by 2 and 1 respectively.
\item[3.] For $(-Y,-\mathfrak{s})$, where $-Y$ is $Y$ with the reversed orientation and $-\mathfrak{s}$ is the induced $\operatorname{Spin}^{c}$ structure, the corresponding Seiberg-Witten-Floer complex $C_{*}(-Y,-\mathfrak{s})$ is the dual complex of $C_{*}(Y, \mathfrak{s})$. There is a natural pairing
$$\langle,\rangle: \quad H F_{*}^{S W}(Y, \mathfrak{s}) \times H F_{-*}^{S W}(-Y,-\mathfrak{s}) \longrightarrow \mathbb{Z}$$
such that $<z \cdot \Xi_{1}, \Xi_{2}>=<\Xi_{1}, z \cdot \Xi_{2}>$ for any $z \in \mathbb{A}(Y) \cong \mathbb{A}(-Y)$ and any cycles $\Xi_{1} \in H F_{*}^{S W}(Y, \mathfrak{s})$ and $\Xi_{2} \in H F_{-*}^{S W}(-Y,-\mathfrak{s})$ respectively.
\item[4.] For any subgroup $K \subseteq \operatorname{Ker}\left(c_{1}(\mathfrak{s})\right) \subset H^{1}(Y, \mathbb{Z})$, there is a variant of Seiberg-Witten-Floer homology denoted by $H F_{*,[K]}^{S W}(Y, \mathfrak{s}) . H F_{*,[K]}^{S W}(Y, \mathfrak{s})$ is a topological invariant and a $\mathbb{Z}$-graded $\mathbb{A}(Y)$ module. For any element $[u] \in H^{1}(Y, \mathbb{Z}) / K$, there is an action of $[u]$ on $H F_{*,[K]}^{S W}(Y, \mathfrak{s})$ which decreases degree by $<[u] \wedge c_{1}(\mathfrak{s}),[Y]>$. There exists a $\mathbb{A}(Y)$ -equivariant homomorphism:
$$\pi: \quad H F_{*,[K]}^{S W}(Y, \mathfrak{s}) \longrightarrow H F_{*}^{S W}(Y, \mathfrak{s}) .$$
There is also a natural pairing
$$\langle,\rangle: \quad H F_{*,[K]}^{S W}(Y, \mathfrak{s}) \times H F_{-*,[K]}^{S W}(-Y,-\mathfrak{s}) \longrightarrow \mathbb{Z}$$
satisfying $<z \cdot \Xi_{1}, \Xi_{2}>=<\Xi_{1}, z \cdot \Xi_{2}>$ for any $z \in \mathbb{A}(Y) \cong \mathbb{A}(-Y)$ and any cycles $\Xi_{1} \in H F_{*,[K]}^{S W}(Y, \mathfrak{s})$ and $\Xi_{2} \in H F_{-*,[K]}^{S W}(-Y,-\mathfrak{s})$ respectively. If $K_{1} \subset K_{2}$ are two subgroups in $\operatorname{Ker}\left(c_{1}(\mathfrak{s})\right)$, there is a $\mathbb{A}(Y)$-equivariant homomorphism:
$$H F_{*,\left[K_{1}\right]}^{S W}(Y, \mathfrak{s}) \longrightarrow H F_{*,\left[K_{2}\right]}^{S W}(Y, \mathfrak{s}) .$$
\end{itemize}

Moreover, $H F_{*,\left[K e r\left(c_{1}(\mathfrak{s})\right)\right]}^{S W}(Y, \mathfrak{s})$ satisfies the following periodicity property:
$$H F_{m,\left[K e r\left(c_{1}(\mathfrak{s})\right)\right]}^{S W}(Y, \mathfrak{s}) \cong H F_{m(\bmod d(\mathfrak{s}))}^{S W}(Y, \mathfrak{s}),$$
for any $m \in \mathbb{Z}$.
Section 4 gives an application to the problem of associating invariants to a 4-manifold with boundary and gluing formulae for 4-dimensional monopole invariants. The setup here is to start with a 4-manifold $\left(X_{+}, \mathfrak{s}_{+}\right)$with cylindrical end modelled on $(Y, \mathfrak{t})$ : that is, over the end $[-2, \infty) \times Y$, there is a fixed isomorphism between the restrction of $\mathfrak{s}_{+}$and the pull-back $\operatorname{Spin}^{c}$ structure of $\mathfrak{t}$. In addition, we assume $c_{1}(\operatorname{det}(\mathfrak{t}))$ is non-torsion.

Finite energy solutions to the Seiberg-Witten equations on $X_{+}$define a moduli space with finite variations of the perturbed Chern-Simons-Dirac functional on the end. We associate to this moduli space a boundary asymptotic value map
$$\partial_{\infty}: \quad \mathcal{M}_{X_{+}}\left(\mathfrak{s}_{+}\right) \longrightarrow \mathcal{M}_{Y, X_{+}}(\mathfrak{t}, \eta)$$
where $\mathcal{M}_{Y, X_{+}}(\mathfrak{t}, \eta)$ is the quotient of solutions to the perturbed Seiberg-Witten equations on $(Y, \mathfrak{t}, \eta)$ by the action of those gauge transformations which can be extended to $X_{+}$. In fact,
$$\pi_{+}: \quad \mathcal{M}_{Y, X_{+}}(\mathfrak{t}, \eta) \longrightarrow \mathcal{M}_{Y}(\mathfrak{t}, \eta)$$
is a covering map with fiber an $H^{1}(Y, \mathbb{Z}) / \operatorname{Im}\left(i_{+}^{*}\right)$-homogeneous space. Here $\operatorname{Im}\left(i_{+}^{*}\right)$ is the range of the map $i_{+}^{*}: H^{1}\left(X_{+}, \mathbb{Z}\right) \rightarrow H^{1}(Y, \mathbb{Z})$.

Over the end $[-2, \infty) \times Y$, if $\left(X_{+}, \mathfrak{s}_{+}\right)$is modelled on $(Y, \mathfrak{t})$ up to an isomorphism $u \in C^{\infty}(Y, U(1))$, then the corresponding asymptotic value map is given by $[u] \circ \partial_{\infty}$ with $[u] \in H^{1}(Y, \mathbb{Z}) / \operatorname{Im}\left(i_{+}^{*}\right)$ determined by the connected component of $C^{\infty}(Y, U(1))$ which $u$ belongs to.

Fix an orientations on $\Lambda^{\text {top }} H^{1}\left(X_{+}(0), Y ; \mathbb{R}\right) \otimes \Lambda^{\text {top }} H^{2,+}\left(X_{+}(0), Y ; \mathbb{R}\right)$. The structure of the fiber for $\partial_{\infty}$ and its compactification are discussed in Proposition 4.2 and Proposition 4.4. These propositions tell us that for each $\Gamma_{\alpha} \in \mathcal{M}_{Y, X_{+}}(\mathfrak{t}, \eta)$, there is a Baire set of self-dual 2-forms with compact support such that the fiber of $\partial_{\infty}$ (if non-empty), denoted by $\mathcal{M}_{X_{+}}\left(\mathfrak{s}_{+}, \Gamma_{\alpha}\right)$, is an oriented, smooth manifold of dimension $\mathfrak{i}_{X_{+}}\left(\Gamma_{\alpha}\right)$ given by (54). It can be compactified to a smooth manifold with corners. In particular, for any $d \geq 0$, the components of dimension $d$ in $\mathcal{M}_{X_{+}}\left(\mathfrak{s}_{+}\right)$, denoted by $\mathcal{M}_{X_{+}}^{d}\left(\mathfrak{s}_{+}\right)$, can be described as
$$\mathcal{M}_{X_{+}}^{d}\left(\mathfrak{s}_{+}\right)=\cup_{\alpha \in \mathcal{M}_{Y}(\mathfrak{t}, \eta)}\left(\bigcup_{\Gamma_{\alpha} \in \pi_{+}^{-1}(\alpha), \mathfrak{i}_{X_{+}}\left(\Gamma_{\alpha}\right)=d} \mathcal{M}_{X_{+}}\left(\mathfrak{s}_{+}, \Gamma_{\alpha}\right)\right) .$$
Here $\mathcal{M}_{X_{+}}\left(\mathfrak{s}_{+}, \Gamma_{\alpha}\right)=\partial_{\infty}^{-1}\left(\Gamma_{\alpha}\right)$.

We then define a relative Seiberg-Witten invariant of $X_{+}$. These relative Seiberg-Witten invariants take values in the homology groups $H F_{*,\left[I m\left(i_{+}^{*}\right)\right]}^{S W}(Y, \mathfrak{t})$. We denote this invariant of $X_{+}$by $S W_{X_{+}}\left(\mathfrak{s}_{+}\right)$, which is a linear functional
$$S W_{X_{+}}\left(\mathfrak{s}_{+}, \cdot\right): \quad \mathbb{A}\left(X_{+}\right) \longrightarrow H F_{*,\left[\operatorname{Im}\left(i_{+}^{*}\right)\right]}^{S W}(Y, \mathfrak{t}),$$
where $\mathbb{A}\left(X_{+}\right)=\operatorname{Sym}^{*}\left(H_{0}\left(X_{+}, \mathbb{Z}\right)\right) \otimes \Lambda^{*}\left(H_{1}\left(X_{1}, \mathbb{Z}\right) /\right.$ Torsion $)$ the free graded algebra generated by the class of elements in $H_{0}\left(X_{+}, \mathbb{Z}\right)$ and $H_{1}\left(X_{+}, \mathbb{Z}\right)$ with degree 2 and 1 respectively.
$S W_{X_{+}}\left(\mathfrak{s}_{+}, z\right)$ with $\operatorname{deg}(z)=d$ can be represented in terms of the Seiberg-Witten invariant for the moduli space $\mathcal{M}_{X_{+}}^{d}\left(\mathfrak{s}_{+}\right)$in (4), that is, for each non-empty component $\mathcal{M}_{X_{+}}\left(\mathfrak{s}_{+}, \Gamma_{\alpha}\right)$ with $\mathfrak{i}_{X_{+}}\left(\Gamma_{\alpha}\right)=d$, there is a topological invariant $S W_{X_{+}}\left(\mathfrak{s}_{+}, z, \Gamma_{\alpha}\right)$ defined in subsection 4.2, with
$$S W_{X_{+}}\left(\mathfrak{s}_{+}, z\right)=\sum_{\alpha \in \mathcal{M}_{Y}(\mathfrak{t}, \eta)} \sum_{\Gamma_{\alpha} \in \pi_{+}^{-1}(\alpha)} S W_{X_{+}}\left(\mathfrak{s}_{+}, z, \Gamma_{\alpha}\right)\left\langle\Gamma_{\alpha}\right\rangle .$$

Section 4 also describes results on closed smooth 4-manifolds $(X, \mathfrak{s})$ with Spin ${ }^{c}$ structure $\mathfrak{s}$ and a smooth embedded separating 3-manifold $Y$ such that there is an embedding $[-2,2] \times Y$ in $X$ and $\mathfrak{t}=\left.\mathfrak{s}\right|_{Y}$ is a non-torsion Spin ${ }^{c}$ structure on $Y$. Consider a 1-parameter family of metrics $\left\{g_{R}\right\}_{R>0}$ on $X$ such that for each $X(R)=\left(X, g_{R}\right)$, there are an isometrically embedded submanifold ( $[-R-2, R+2] \times Y, d t^{2}+g_{Y}$ ) and two 4-manifolds $X_{ \pm}(R)$ obtained by setting $X(R)=X_{+}(R) \cup X_{-}(R)$. As $R \rightarrow \infty, X(R)$ has a geometric limit, two 4-manifolds with cylindrical ends, denoted by $X_{ \pm}(\infty)$. Note that there are induced Spin ${ }^{c}$ structures $\mathfrak{s}_{ \pm}$on $X_{ \pm}(\infty)$ from the $\operatorname{Spin}^{c}$ structure $\mathfrak{s}$ on $X$.

Denote by $i_{ \pm}$the boundary embedding maps of $Y$ in $X_{ \pm}(0)$, and by $\operatorname{Im}\left(i_{ \pm}^{*}\right)$ the ranges of the maps $H^{1}\left(X_{ \pm}(0), \mathbb{Z}\right) \rightarrow H^{1}(Y, \mathbb{Z})$. Then we have the following commutative diagram relating various subgroups $\operatorname{Im}\left(i_{+}^{*}\right) \cap \operatorname{Im}\left(i_{-}^{*}\right), \operatorname{Im}\left(i_{ \pm}^{*}\right)$ and $\operatorname{Im}\left(i_{+}^{*}\right)+\operatorname{Im}\left(i_{-}^{*}\right)$ of $\operatorname{Ker}\left(c_{1}(\mathfrak{t})\right)$ in $H^{1}(Y, Z)$ :
![](https://cdn.mathpix.com/cropped/fe62acfa-5786-4f08-ad7d-3eb6081e3ffb-05.jpg?height=307&width=898&top_left_y=1741&top_left_x=675)
which induces a commutative diagram of $\mathbb{A}(Y)$-equivariant homomorphisms between various variants of the Seiberg-Witten-Floer homologies for $(Y, \mathfrak{t})$ :
![](https://cdn.mathpix.com/cropped/fe62acfa-5786-4f08-ad7d-3eb6081e3ffb-05.jpg?height=241&width=1261&top_left_y=2189&top_left_x=494)

With these notations understood, the relative invariants for $\left(X_{ \pm}(\infty), \mathfrak{s}_{ \pm}\right)$are linear functionals
$$S W_{X_{ \pm}}\left(\mathfrak{s}_{ \pm}, \cdot\right): \quad \mathbb{A}\left(X_{ \pm}\right) \longrightarrow H F_{*,\left[\operatorname{Im}\left(i_{ \pm}^{*}\right)\right]}^{S W}( \pm Y, \pm \mathfrak{t}) .$$

Fix an orientation on the line $\Lambda^{\text {top }} H^{1}(X, \mathbb{R}) \otimes \Lambda^{\text {top }} H^{2,+}(X, \mathbb{R})$ which is induced from tensoring the orientations on $\Lambda^{\text {top }} H^{1}\left(X_{+}(0), Y ; \mathbb{R}\right) \otimes \Lambda^{\text {top }} H^{2,+}\left(X_{+}(0), Y ; \mathbb{R}\right)$ and $\Lambda^{\text {top }} H^{1}\left(X_{-}(0), Y ; \mathbb{R}\right) \otimes \Lambda^{\text {top }} H^{2,+}\left(X_{-}(0), Y ; \mathbb{R}\right)$. When $b_{2}^{+}=1$, we also need to fix an orientation on the line $\Lambda^{\text {top }} H^{2,+}(X, \mathbb{R})$.

The Seiberg-Witten invariant for a closed manifold $(X, \mathfrak{s})$ is a linear functional
$$S W_{X}(\mathfrak{s}, \cdot): \mathbb{A}(X) \mapsto \mathbb{Z}$$
as defined in [34] where $\mathbb{A}(X)=\operatorname{Sym}^{*}\left(H_{0}(X)\right) \otimes \Lambda^{*}\left(H_{1}(X) /\right.$ Torsion $)$. Note that there is indeterminacy in the Spin ${ }^{c}$ structures on $X(R)$ obtained by gluing $\mathfrak{s}_{ \pm}$along $(Y, \mathfrak{t})$. The set of these Spin ${ }^{c}$ structures, say $\operatorname{Spin}^{c}\left(X, \mathfrak{s}_{ \pm}\right)$, can be represented by
$$\operatorname{Spin}^{c}\left(X, \mathfrak{s}_{ \pm}\right)=\left\{\mathfrak{s}_{+} \#_{[u]} \mathfrak{s}_{-} \left\lvert\,[u] \in \frac{H^{1}(Y, Z)}{\operatorname{Im}\left(i_{+}^{*}\right)+\operatorname{Im}\left(i_{-}^{*}\right)}\right.\right\} .$$
Here $\mathfrak{s}_{+} \#_{[u]} \mathfrak{s}_{-}$is the resulting $\operatorname{Spin}^{c}$ structure on $X$ obtained by gluing $\mathfrak{s}_{ \pm}$using the gauge transformation $u$ representing $[u]$.

Now our main gluing formulae along $(Y, \mathfrak{t})$ with $b_{1}(Y)>0$ and $c_{1}(\mathfrak{t}) \neq 0$ are contained in the following theorem.

Theorem 1.2. Let $X$ be a closed 4-manifold with $b_{2}^{+} \geq 1$ which can be split as $X=X_{+} \cup_{Y} X_{-}$, where $X_{+}$and $X_{-}$are 4-manifolds with boundary $\partial X_{+}=-\partial X_{-}=Y$. Suppose that we have $\operatorname{Spin}^{c}$ structures $\mathfrak{s}_{+}$and $\mathfrak{s}_{-}$on $X_{+}$and $X_{-}$respectively which restrict to $\mathfrak{t}$ on the boundary. Assume that $b_{1}(Y)>0$ and $c_{1}(\mathfrak{t})$ is non-torsion then the Seiberg-Witten invariants for $\left(X, \mathfrak{s}_{+} \#_{[u]} \mathfrak{s}_{-}\right)$can be expressed as
$$S W_{X}\left(\mathfrak{s}_{+} \#_{[u] \mathfrak{s}-}, z_{+} z_{-}\right)=\left\langle[u]\left(\pi_{+}\left(S W_{X_{+}}\left(\mathfrak{s}_{+}, z_{+}\right)\right)\right), \pi_{-}\left(S W_{X_{-}}\left(\mathfrak{s}_{-}, z_{-}\right)\right)\right\rangle,$$
where $[u]$ acts on $H F_{*,\left[\operatorname{Im}\left(i_{+}^{*}\right)+\operatorname{Im}\left(i_{-}^{*}\right)\right]}^{S W}(Y, \mathfrak{t}), z_{ \pm} \in \mathbb{A}\left(X_{ \pm}\right), \pi_{ \pm}$are the homomorphisms given in (6), and the pairing on the right hand side is the natural pairing on
$$H F_{*,\left[\operatorname{Im}\left(i_{+}^{*}\right)+\operatorname{Im}\left(i_{-}^{*}\right)\right]}^{S W}(Y, \mathfrak{t}) \times H F_{*,\left[\operatorname{Im}\left(i_{+}^{*}\right)+\operatorname{Im}\left(i_{-}^{*}\right)\right]}^{S W}(-Y,-\mathfrak{t}),$$
with the degrees in $H F_{*,\left[\operatorname{Im}\left(i_{+}^{*}\right)+\operatorname{Im}\left(i_{-}^{*}\right)\right]}^{S W}(-Y,-\mathfrak{t})$ shifted by
$$d_{X}(\mathfrak{s})=\frac{1}{4}\left(c_{1}(\mathfrak{s})^{2}-(2 \chi(X)+3 \sigma(X))\right)=\operatorname{deg}\left(z_{1}\right)+\operatorname{deg}\left(z_{2}\right) .$$

When $b_{2}^{+}=1$, the Seiberg-Witten invariants $S W_{X}(\mathfrak{s}, \cdot)$ are defined with a fixed orientation on $H^{2,+}(X, \mathbb{R})$ such that $c_{1}(\mathfrak{s}) \cdot \omega^{+}>0$ for an oriented generator $\omega^{+}$of $H^{2,+}(X, \mathbb{R})$. In particular, there is a set $\mathcal{S}$ of $\operatorname{Spin}^{c}$ structures $\mathfrak{s} \in \operatorname{Spin}^{c}\left(X, \mathfrak{s}_{ \pm}\right)$with $d_{X}(\mathfrak{s})=\operatorname{deg}\left(z_{1}\right)+\operatorname{deg}\left(z_{2}\right)$ such that
$$\sum_{\mathfrak{s} \in \mathcal{S}} S W_{X}\left(\mathfrak{s}, z_{+} z_{-}\right)=\left\langle\pi\left(S W_{X_{+}}\left(\mathfrak{s}_{+}, z_{+}\right)\right), \pi\left(S W_{X_{-}}\left(\mathfrak{s}_{-}, z_{-}\right)\right)\right\rangle .$$
Here $\pi\left(S W_{X_{ \pm}}\left(\mathfrak{s}_{ \pm}, z_{ \pm}\right)\right)$are elements in $H F_{*}^{S W}( \pm Y, \pm \mathfrak{t})$ under the homomorphism (1) and the pairing on the right hand side is the natural pairing on $H F_{*}^{S W}(Y, \mathfrak{t}) \times H F_{*}^{S W}(-Y,-\mathfrak{t}) \rightarrow \mathbb{Z}$.

This gluing theorem generalizes the gluing result of Morgan-Szabo-Taubes (Theorem 9.5 in [25]), has already found applications to the study of Seiberg-Witten-Floer homology as in [26]. We like to thank Vicente Munoz for his help in providing examples to test our gluing formulae.

We would like to acknowledge our gratitude to Matilde Marcolli, Tom Mrowka and Cliff Taubes for many useful correspondences. The authors also thank the Max-Planck-Institut fur Mathematik in Bonn for hospitality and support. This research was supported in part by the Australian Research Council.

\section*{2 Seiberg-Witten monopoles on 3-manifolds: review}

Let $Y$ be a closed, oriented 3-manifold equipped with a Riemannian metric $g$. To introduce the Seiberg-Witten equations on $(Y, g)$, we need to choose a Spin ${ }^{c}$ structure on $Y$. This is a lift of the $\operatorname{SO}(3)$-frame bundle on $Y$ to a $\operatorname{Spin}^{c}(3)$-bundle $P$. Note that $\operatorname{Spin}^{c}(3)=U(2)$, the determinant homomorphism $\operatorname{Spin}^{c}(3) \rightarrow U(1)$ determines a principal $U(1)$-bundle, the corresponding complex line bundle is called the determinant line bundle of the Spin ${ }^{c}$ structure $P$.

The isomorphism classes of Spin ${ }^{c}$ structures are classified by the first Chern class of the determinant line bundle. Given a Spin ${ }^{c}$ structure $P$, there is an associated Spin ${ }^{c}$ bundle
$$W=P \times_{U(2)} \mathbb{C}^{2}$$
which is complex vector bundle whose sections form a module for the Clifford bundle on $(Y, g)$. As a vector space the Clifford bundle can be identified with the exterior bundle on $T^{*} Y$ but with a different algebra structure: the Clifford relation
$$v_{1} v_{2}+v_{2} v_{1}=-2 g\left(v_{1}, v_{2}\right)$$
holds for two sections $v_{1}$ and $v_{2}$ of $T^{*} Y$. To end this discussion, we give a more practical definition of a $\operatorname{Spin}^{c}$ structure on $(Y, g)$.

Definition 2.1. A Spin ${ }^{c}$ structure $\mathfrak{s}$ on an oriented, closed 3-manifold $(Y, g)$ is a pair $(W, \rho)$ consisting of a $U(2)$ bundle $W$ and a Clifford multiplication homomorphism
$\rho: T^{*}(Y) \rightarrow \operatorname{End}(W)$ satisfying the Clifford relation: $\rho\left(v_{1}\right) \rho\left(v_{2}\right)+\rho\left(v_{2}\right) \rho\left(v_{1}\right)=-2 g\left(v_{1}, v_{2}\right)$. and satisfying $\rho\left(e_{1}\right) \rho\left(e_{2}\right) \rho\left(e_{3}\right)=I d_{W}$.

Locally, let $\left\{e^{1}, e^{2}, e^{3}\right\}$ be an oriented orthonormal co-frame for $T^{*} Y$, then the Clifford multiplication can be written as follows
$$\rho\left(\sum_{i=1}^{3} a_{i} e^{i}\right)=\left(\begin{array}{lr}
a_{1} i & -a_{2}+i a_{3} \\
a_{2}+i a_{3} & -a_{1} i
\end{array}\right) .$$

The Clifford multiplication homomorphism $\rho$ can be employed to define an $\mathbb{R}$-bilinear form $\sigma: W \otimes W \rightarrow T^{*} Y \otimes i \mathbb{R}$, given by
$$\begin{aligned}
\sigma(\psi, \psi) & =-\rho^{-1}\left(\psi \otimes \psi^{*}-\frac{|\psi|^{2}}{2} I d\right) \\
& =\frac{i}{2} \operatorname{Im}\left(\left\langle e_{i} . \psi, \psi\right\rangle\right) e^{i} \in \Omega^{1}(Y, i \mathbb{R}) .
\end{aligned}$$
Here $\psi$ is a section of $W$ and $<,>$ is the Hermitian product on $W$. It is easy to check that $\sigma(\cdot, \cdot)$ satisfies the following properties.

Lemma 2.2. Use . to denote Clifford multiplication, <,> is the Hermitian product on $W$ and $g$ is the Riemannian metric on $Y$, extended linearly to $T^{*} Y \otimes_{\mathbb{R}} \mathbb{C}$, Then
\begin{itemize}
\item[1.] $\sigma(\psi, \psi) . \psi=-\frac{1}{2}|\psi|^{2} \psi$, and $|\sigma(\psi, \psi)|^{2}=\frac{1}{4}|\psi|^{4}$.
\item[2.] For any imaginary-valued 1-form $\alpha$ on $Y,\langle\alpha . \psi, \psi\rangle=2 g(\alpha, \sigma(\psi, \psi))$ and $\sigma(\alpha . \psi, \phi)+\sigma(\psi, \alpha . \phi)=-(\operatorname{Re}\langle\psi, \phi\rangle) \alpha$.
\item[3.] $\sigma(\psi, \phi)=0$ if and only if on $Y \backslash \psi^{-1}(0), \phi=$ ir $\psi$ for a real-valued function $r$ on $Y \backslash \psi^{-1}(0)$.
\item[4.] If $\psi$ is a nowhere vanishing section of $W$, then $W \cong \underline{\mathbb{C}} \psi \oplus \psi^{\perp}$, where $\underline{\mathbb{C}} \psi$ is the trivial complex line bundle generated by $\psi$ and $\psi^{\perp}$ is the orthogonal complement of $\psi$ under the Hermitian product. Moreover, $\sigma(\psi, \cdot)$ defines a bundle isomorphism between $\mathbb{R} \psi \oplus \psi^{\perp}$ and $T^{*} Y \otimes i \mathbb{R}$. This last claim implies that a $\operatorname{Spin}^{c}$ structure on $(Y, g)$ can be identified with Turaev's Euler structure [36] on ( $Y, g$ ).
\end{itemize}

Proof. Claims (a) and (b) follow from direct calculations. We only prove claim (d), as from (d), we know that the on $Y \backslash \psi^{-1}(0)$, the kernel of the map $\sigma(\psi, \cdot)$ consists of sections of $\underline{i \mathbb{R}} \psi$, and this implies claim (c).

For a nowhere vanishing section $\psi$ of $W$, we write $\psi=|\psi| \tau_{1}$ where $\tau_{1}$ is a unit-length spinor. Choose a local basis $\left\{\tau_{1}, \tau_{2}\right\}$ for the Spin ${ }^{c}$ bundle, so that Clifford multiplication in the local orthonormal coframe $\left\{e^{1}, e^{2}, e^{3}\right\}$ for $T^{*} Y$ is given by
$$\rho\left(e_{1}\right)=\left(\begin{array}{cc}
i & 0 \\
0 & -i
\end{array}\right), \rho\left(e_{2}\right)=\left(\begin{array}{rr}
0 & -1 \\
1 & 0
\end{array}\right), \rho\left(e_{3}\right)=\left(\begin{array}{cc}
0 & i \\
i & 0
\end{array}\right) .$$
where $\left\{e^{1}, e^{2}, e^{3}\right\}$ can be expressed as
$$e^{1}=-2 i \sigma\left(\tau_{1}, \tau_{1}\right), e^{2}=2 i \sigma\left(\tau_{1}, i \tau_{1}\right), e^{3}=-2 i \sigma\left(\tau_{1}, \tau_{2}\right) .$$
Any section of $\underline{\mathbb{R} \psi} \oplus \psi^{\perp}$ can be written as $u \tau_{1}+v \tau_{2}$ for a real-valued function $u$ and a complexvalued function $v$, then
$$\sigma(\psi, \phi)=\frac{i}{2}|\psi|\left(u e^{1}-\operatorname{Im}(v) e^{2}+\operatorname{Re}(v) e^{3}\right) .$$
Hence, $\sigma(\psi, \cdot)$ defines a bundle isomorphism between $T^{*} Y \otimes i \mathbb{R}$ and $\underline{\mathbb{R}} \psi \oplus \psi^{\perp}$.
In [36], Turaev defined an Euler structure to be a homology class of a nowhere vanishing vector field on $Y$, where two vector fields are called homologous if they are homotopic away from a point. Identifying $T Y$ with $T^{*} Y$ using the Riemannian metric, for any Euler structure on $(Y, g)$, there is a unit-length section $v$ of $T^{*} Y$ representing that Euler structure, which gives rise to the following decomposition $T^{*} Y=\underline{\mathbb{R} . v} \oplus L$. Then the Hodge star operator can endow $L$ with a complex structure given by $J=*(v \wedge \cdot)$. The corresponding Spin ${ }^{c}$ structure is given by $W=\underline{\mathbb{C}} . v \oplus L$ and Clifford multiplication by $v$ is given by $\left(\begin{array}{cc}i & 0 \\ 0 & -i\end{array}\right)$. \(\square\)

With the Levi-Civita connection ∇ on the cotangent bundle $T^{*} Y$, a $U(1)$-connection $A$ on the determinant bundle $\operatorname{det}(W)$ determines a connection $\nabla_{A}$ on $W$ such that $\rho$ is parallel, that is, for $v$ and $\psi$ sections of $T^{*} Y$ and $W$ respectively, $\nabla_{A}$ satisfies
$$\nabla_{A}(v \cdot \psi)=(\nabla v) \cdot \psi+v \cdot \nabla_{A}(\psi) .$$
Then $\nabla_{A}$ is called a Spin ${ }^{c}$ connection on $W$. Applying the Clifford multiplication, we can define a Dirac operator $\not \partial_{A}=\rho \circ \nabla_{A}: \Gamma(W) \rightarrow \Gamma(W)$.

Now we can introduce the Seiberg-Witten equations on $(Y, g, \mathfrak{s})$ for a pair $(A, \psi)$ consisting of a $U(1)$ connection $A$ on the determinant line bundle of $\mathfrak{s}$ and a spinor section $\psi$ of $W$ : [15] [4] [22] [17] [6]:
$$\left\{\begin{array}{l}
\not \diamond_{A} \psi=0, \\
* F_{A}=\sigma(\psi, \psi)+\eta
\end{array}\right.$$
where $\eta$ is a co-closed, imaginary-valued 1-form on $Y$.
Denote by $\mathcal{A}_{Y}(\mathfrak{s})$ the Seiberg-Witten configuration space on $(Y, \mathfrak{s})$ consisting of pairs $(A, \psi)$ as above Then $\mathcal{A}_{Y}(\mathfrak{s})$ is an affine space modelled on $\Omega^{1}(X, i \mathbb{R}) \times \Gamma(W)$. For analytic reasons, we shall use the $L_{1}^{2}$-integrable configuration space, denoted $\mathcal{A}_{L_{1}^{2}}$, and we require $\eta$ to be $L_{2}^{2}$ -integrable, hence $\|\eta\|_{C^{0}}$ is bounded.

The automorphism group of $\operatorname{det}(W)$ is the gauge group $\mathcal{G}_{Y}=\mathcal{G}_{L_{2}^{2}}$ of $L_{2}^{2}$-maps of $Y$ to U(1), locally modelled on the Lie algebra $\Omega_{L_{2}^{2}}^{0}(Y, i \mathbb{R})$. The gauge group $\mathcal{G}_{L_{2}^{2}}$ acts on $\mathcal{A}_{L_{1}^{2}}$ by
gauge transformations: $(A, \psi) \stackrel{u}{\hookrightarrow}\left(A-2 u^{-1} d u, u \psi\right)$, which leave the Seiberg-Witten equations invariant. It acts freely on $\{(A, \psi) \mid \psi \neq 0\}$, those elements are said to be irreducible while $(A, \psi)$ with $\psi=0$ is said to be reducible. Denote by $\mathcal{B}=\mathcal{A}_{L_{1}^{2}} / \mathcal{G}_{L_{2}^{2}}$ the quotient of $\mathcal{A}_{L_{1}^{2}}$ by gauge transformations. We use the notation $\mathcal{A}_{L_{1}^{2}}^{*}$ for the open subset of irreducible configurations, and $\mathcal{B}^{*}=\mathcal{A}_{L_{1}^{2}}^{*} / \mathcal{G}_{L_{2}^{2}}$ for the quotient space of $\mathcal{A}_{L_{1}^{2}}^{*}$ by the gauge group $\mathcal{G}_{L_{2}^{2}}$. Then $\mathcal{B}^{*}$ is a Hausdorff space [10][23], in fact, $\mathcal{B}^{*}$ is a smooth infinite dimensional Hilbert manifold.

At $(A, \psi) \in \mathcal{A}_{L_{1}^{2}}$, the tangent space can be identified with the $L_{1}^{2}$-completion of $\Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(W)$, we denote this completion by $\Omega_{L_{1}^{2}}^{1}(Y, i \mathbb{R}) \oplus \Gamma_{L_{1}^{2}}(W)$. The infinitesimal action of $\mathcal{G}_{L_{2}^{2}}$ at $(A, \psi)$ defines a map
$$\begin{array}{ll}
G_{(A, \psi)}: & \Omega_{L_{2}^{2}}^{0}(Y, i \mathbb{R}) \rightarrow \Omega_{L_{1}^{2}}^{1}(Y, i \mathbb{R}) \oplus \Gamma_{L_{1}^{2}}(W) \\
& G_{(A, \psi)}(f)=(-2 d f, f \psi) .
\end{array}$$
Local slices exist for the action of $\mathcal{G}_{L_{2}^{2}}$ on $\mathcal{A}_{L_{1}^{2}}$. At $[A, \psi] \in \mathcal{B}^{*}$, the tangent space is given by the $L_{1}^{2}$-completion of
$$\left\{(\alpha, \phi) \in \Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(W) \mid d^{*} \alpha+i \operatorname{Im}<\psi, \phi>=0\right\} .$$
The $L_{1}^{2}$ metric on $T_{[A, \psi]} \mathcal{B}^{*}$ is defined by the natural $L_{1}^{2}$-norm on one forms and the $L_{1}^{2}$-norm on sections of $W$ using the connection $\nabla_{A}$. This metric is independent of the choice of representative $(A, \psi)$. At a reducible point $[A, 0] \in \mathcal{B}$, there is a neighbourhood of $[A, 0] \in \mathcal{B}$, which is homeomorphic to the quotient of the $L_{1}^{2}$-completion of
$$\text { Kerd }^{*} \oplus \Gamma(W)$$
by the action of $U(1)$ on the $\Gamma(W)$ factor. Hence, the reducible point $[A, 0]$ is a singular point in $\mathcal{B}$ with the link of singularity homotopy equivalent to $\mathbb{C} P^{\infty}$.

Definition 2.3. The moduli space $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ of the Seiberg-Witten monopoles on $(Y, g, \mathfrak{s})$ is the solution space of the Seiberg-Witten equations (9) modulo the gauge transformation group $\mathcal{G}_{L_{2}^{2}}$. The moduli space $\mathcal{M}_{Y}^{*}(\mathfrak{s}, \eta)$ is the irreducible part of $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$.

There is an a priori pointwise estimate to the spinor part of any solution to the Seiberg-Witten equations (9), which we now state as follows.

Lemma 2.4. Every solution to the Seiberg-Witten equations (9) is gauge equivalent to a $C^{\infty}$ solution. Let $(A, \psi)$ be a smooth solution to the Seiberg-Witten equations (9), then
$$|\psi|^{2} \leq \max _{y \in Y}\left\{0,-s(y)+2\|\eta\|_{C^{0}}\right\}$$
where $s(y)$ is the scalar curvature for $(Y, g)$.

Proof. The first claim follows from standard elliptic regularity theory. The estimate on $|\psi|^{2}$ follows from the Weitzenböck formula (Cf. [15][23])
$$\not \partial_{A}^{2}=\nabla_{A}^{*} \nabla_{A}+\frac{s}{4}-\frac{1}{2} \rho\left(* F_{A}\right) .$$ \(\square\)

Let $(A, \psi) \in \mathcal{A}_{L_{1}^{2}}$ be a solution to the Seiberg-Witten equations (9), then there is a natural associated elliptic complex which incorporates the linearization of the gauge action (10) and the linearization of equations (9) as follows. The linearization of the Seiberg-Witten equations (9) at a solution $(A, \psi)$ defines the following map:
$$\begin{gathered}
L_{(A, \psi)}: \Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(W) \rightarrow \Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(W) \\
L_{(A, \psi)}(\alpha, \phi)=\left(* d \alpha-\sigma(\psi, \phi), \not \partial_{A} \phi+\frac{1}{2} \alpha \cdot \psi\right) .
\end{gathered}$$

The infinitesimal action of $\mathcal{G}_{Y}=\mathcal{G}_{L_{2}^{2}}$ and linearization of the Seiberg-Witten equations at a solution $(A, \psi)$ define the deformation complex
$$\Omega_{L_{2}^{2}}^{0}(Y, i \mathbb{R}) \xrightarrow{G_{(A, \psi)}} \Omega_{L_{1}^{2}}^{1}(Y, i \mathbb{R}) \oplus \Gamma_{L_{1}^{2}}(W) \xrightarrow{L_{(A, \psi)}} \Omega_{L^{2}}^{1}(Y, i \mathbb{R}) \oplus \Gamma_{L^{2}}(W) .$$

It is convenient to put the deformation complex (12) in the following form:
$$\begin{gathered}
\Omega_{L_{1}^{2}}^{1}(Y, i \mathbb{R}) \oplus \Gamma_{L_{1}^{2}}(W) \oplus \Omega_{L_{2}^{2}}^{0}(Y, i \mathbb{R}) \longrightarrow \Omega_{L^{2}}^{1}(Y, i \mathbb{R}) \oplus \Gamma_{L^{2}}(W) \oplus \Omega_{L^{2}}^{0}(Y, i \mathbb{R}) \\
\mathcal{T}_{(A, \psi)}=\left(\begin{array}{cc}
L_{(A, \psi)} & G_{(A, \psi)} \\
G_{(A, \psi)}^{*} & 0
\end{array}\right)
\end{gathered}$$
where $G_{(A, \psi)}^{*}$ is the dual operator of $G_{(A, \psi)}$ under the $L^{2}$-inner product:
$$G_{(A, \psi)}^{*}(a, \phi)=-2\left(d^{*} a+i \operatorname{Im}\langle\psi, \phi\rangle\right) .$$
Note that $\mathcal{T}_{(A, \psi)}$ is a compact perturbation, courtesy of Lemma 2.4, of the sum of the signature operator and the twisted Dirac operator,
$$\left(\begin{array}{cc}
* d & -2 d \\
-2 d^{*} & 0
\end{array}\right) \oplus \partial_{A}$$
which has index 0.
Definition 2.5. We say that $[A, \psi]$ in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ is non-degenerate if the middle cohomology of (12) is zero:
$$\operatorname{Ker} L_{(A, \psi)} / \operatorname{Im} G_{(A, \psi)}=0 .$$

We summarize the main properties of the monopole moduli space $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, their proofs can be found in [11] [17] [16] [37].

Proposition 2.6. Let $(Y, g, \mathfrak{s})$ be a closed, Riemannian 3-manifold with a Spin ${ }^{c}$ structure $\mathfrak{s}$, then the Seiberg-Witten moduli space $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ has the following properties. There exists a Baire set of co-closed 1-forms $\eta \in \Omega_{L_{2}^{2}}^{1}(Y, i \mathbb{R})$ such that all the points in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ are non-degenerate. Moreover, if $b_{1}(Y)>0, \mathcal{M}_{Y}(\mathfrak{s}, \eta)$ consists of only finitely many irreducible points; if $Y$ is a rational homology 3-sphere, assume that a generic $\eta$ satisfies $K e r \not \partial_{\theta}=0$ (where $\theta$ is the unique reducible point in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, that is, $* F_{\theta}=\eta$ ) , then $\mathcal{M}_{Y}^{*}(\mathfrak{s}, \eta)=\mathcal{M}_{Y}(\mathfrak{s}, \eta)-\{\theta\}$ consists of only finitely many irreducible points.

Remark 2.7. Proposition 2.6 still holds for a Baire set of co-closed imaginary-valued 1-forms on a fixed non-empty open set $U \subset Y$ (if $b_{1}(Y)>0$ and $c_{1}(\operatorname{det}(\mathfrak{s}))=0, U$ is chosen such that the map: $H_{\text {cpt }}^{2}(U, \mathbb{R}) \rightarrow H^{2}(Y, \mathbb{Z})$ is non-trivial). This is established in [5].

\section*{3 Seiberg-Witten-Floer homology}

In this Section we will discuss the construction of the Seiberg-Witten-Floer homology groups. The main technical parts have been established in [20]. Here we give another account of analytical parts of the construction of Seiberg-Witten-Floer homology groups and introduce a different perturbation of the Chern-Simons-Dirac functional to achieve transversality for the moduli space of flowlines.

\subsection*{3.1 The basics of the CSD functional: critical points, relative indices}

Let $Y$ be a closed, oriented 3-manifold with a Riemannian metric $g$ and a Spin ${ }^{c}$ structure $\mathfrak{s}=(W, \rho)$ on $Y$. Let $\mathcal{A}$ be the $L_{1}^{2}$-configuration space for the Seiberg-Witten equations, the tangent space at any point is the space of $L_{1}^{2}$-sections: $\Omega_{L_{1}^{2}}^{1}(Y, i \mathbb{R}) \oplus L_{1}^{2}(W)$. Let $\mathcal{G}=\mathcal{G}_{Y}$ be the $L_{2}^{2}$ gauge transformation group on $Y$. Its tangent space at the identity is $\Omega_{L_{2}^{2}}^{0}(Y, i \mathbb{R})$ and $\mathcal{G}$ acts on $\mathcal{A}$ with the quotient space denoted by $\mathcal{B}$. For simplicity, we assume that $c_{1}(\operatorname{det}(\mathfrak{s})) \neq 0$ in $H^{2}(Y, \mathbb{R})$ if $b_{1}(Y)>0$.

Fix a $C^{\infty}$ connection $A_{0}$ on $\operatorname{det}(W)$, then there is a Chern-Simons-Dirac function on $\mathcal{A}$ as in [15]:
$$\mathcal{C}_{\eta}(A, \psi)=-\frac{1}{2} \int_{Y}\left(A-A_{0}\right) \wedge\left(F_{A}+F_{A_{0}}-* 2 \eta\right)+\int_{Y}\left\langle\psi, \not \partial_{A} \psi\right\rangle d v o l_{Y}$$
Here $\eta$ is a co-closed, imaginary-valued 1-form on $Y$ which is $L_{2}^{2}$-integrable and we can assume that $* \eta$ represents a trivial cohomology class in $H^{1}(Y, i \mathbb{R})$. When $\eta=0$, we denote $\mathcal{C}_{\eta}$ by $\mathcal{C}$.

For $g \in \mathcal{G}$, we have
$$\mathcal{C}_{\eta}(g \cdot(A, \psi))-\mathcal{C}_{\eta}(A, \psi)=\left(c_{1}(\operatorname{det}(W)) \wedge[g]\right)([Y]) .$$
Here $[g]$ is the cohomology class $[g]=\left[-2 \pi i g^{-1} d g\right]$ on $Y$ which defines a homomorphism: $\mathcal{G} \rightarrow H^{1}(Y, \mathbb{Z})$, the kernel of this map is the identity component of $\mathcal{G}$. Therefore, $\mathcal{C}_{\eta}$ descends to a map $\mathcal{B} \rightarrow \mathbb{R} / d(\mathfrak{s}) \mathbb{Z}$ where $d(\mathfrak{s})$ is the divisibility of $c_{1}(\mathfrak{s})=c_{1}(\operatorname{det}(W))$ in $H^{2}(Y, \mathbb{Z}) /$ Torsion:
$$d(\mathfrak{s})=g . c . d .\left\{<c_{1}(\mathfrak{s}), \sigma>: \text { for } \sigma \in H_{2}(Y, \mathbb{Z})\right\} .$$
In the case of $c_{1}(\operatorname{det}(W))=0$, we see from (15) that $\mathcal{C}_{\eta}$ descends to a map $\mathcal{B} \rightarrow \mathbb{R}$. If $c_{1}(\operatorname{det}(W))$ is not a torsion element, we know that $\mathcal{C}_{\eta}$ descends to a map $\mathcal{B} \rightarrow S^{1}$.

With the $L^{2}$-metric on sections of the spinor bundle $W$ given by twice the real part of the $L^{2}$-hermitian product, the gradient of $\mathcal{C}_{\eta}$ at $(A, \psi) \in \mathcal{A}$ is given by
$$\nabla \mathcal{C}_{\eta}(A, \psi)=\left(* F_{A}-\sigma(\psi, \psi)-\eta, \not \partial_{A} \psi\right),$$
which is $\mathcal{G}$-equivariant. Hence, $\nabla \mathcal{C}_{\eta}$ defines a section of the $L^{2}$-tangent bundle on $\mathcal{B}^{*}$. Note that the tangent space of $\mathcal{B}^{*}$ at $[A, \psi]$ is the $L_{1}^{2}$-completion of
$$\operatorname{Ker} G_{[A, \psi]}^{*}=\left\{(a, \phi) \in \Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(W) \mid d^{*} a+i \operatorname{Im}\langle\psi, \phi\rangle=0\right\} .$$
The Hessian operator of $\mathcal{C}_{\eta}$ at $[A, \psi] \in \mathcal{B}^{*}$ is given by
$$\begin{gathered}
Q_{[A, \psi]}: \operatorname{KerG}_{[A, \psi]}^{*} \longrightarrow \operatorname{KerG}_{[A, \psi]}^{*} \\
Q_{[A, \psi]}:(a, \phi) \mapsto\left(* d a-2 \sigma(\psi, \phi)-2 d f, \not \partial_{A} \phi+\frac{1}{2} a . \psi+f \psi\right)
\end{gathered}$$
where $f$ is the unique solution in $\Omega_{L_{2}^{2}}^{0}(Y, i \mathbb{R})$ of the equation
$$\left(d^{*} d+\frac{1}{2}|\psi|^{2}\right) f=i \operatorname{Im}\left\langle\not \partial_{A} \psi, \phi\right\rangle .$$
Notice that if $[A, \psi]$ is a critical point of $\mathcal{C}_{\eta}$, then $f=0$ by the maximum principle. The following Lemma describes the properties of the Hessian operator $Q_{[A, \psi]}$ of $\mathcal{C}_{\eta}$ at $[A, \psi] \in \mathcal{B}^{*}$.

Lemma 3.1. $Q_{[A, \psi]}$ defines a closed, unbounded, essentially self-adjoint, Fredholm operator on the $L^{2}$-completion of $\operatorname{Ker} G_{[A, \psi]}^{*}$, and its eigenvectors form an $L^{2}$-complete orthonormal basis for $\operatorname{KerG}_{[A, \psi]}^{*}$. The domain of $Q_{[A, \psi]}$ is the $L_{1}^{2}$-tangent space of $\mathcal{B}^{*}$. The eigenvalues form a discrete subset of the real line which has no accumulation points, and which is unbounded in both directions. Each eigenvalue has finite multiplicity.

Proof. We follow the arguments in [30]. First $Q_{[A, \psi]}$ defines a bounded, essentially self-adjoint, Fredholm operator on the $L_{1}^{2}$-completion of $\operatorname{Ker} G_{[A, \psi]}^{*}$ to the $L^{2}$-completion of $\operatorname{Ker} G_{[A, \psi]}^{*}$. Then
the forgetful map from $L_{1}^{2}$ to $L^{2}$ is compact and the resolvent of $Q_{[A, \psi]}$ is compact so that $Q_{[A, \psi]}$ has no essential spectrum (accumulation points or isolated eigenvalue with infinite multiplicity). Therefore $Q_{[A, \psi]}$ has discrete spectrum without accumulation points and each eigenvalue has finite multiplicity. The remaining statements are standard in the elliptic theory on compact manifolds. \(\square\)

Let $[A, \psi]$ be a critical point of $\mathcal{C}_{\eta}$ on $\mathcal{B}$, then $[A, \psi]$ is a gauge equivalence class of a solution $(A, \psi) \in \mathcal{A}$ to the Seiberg-Witten equations (9). Hence, the set of critical points of $\mathcal{C}_{\eta}$ on $\mathcal{B}$ is $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$. A critical point $[A, \psi] \in \mathcal{M}_{Y}^{*}(\mathfrak{s}, \eta)$ is called non-degenerate if its Hessian operator is non-degenerate. It is easy to see that a non-degenerate critical point is isolated in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$. A reducible critical point is of the form $[A, 0]$ with $* F_{A}=\eta$. For generic $\eta, * F_{A}=\eta$ admits solutions only when $Y$ is a rational homology 3-sphere. We call a reducible critical point non-degenerate if it is isolated in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$. From Proposition 2.6, we obtain the following property of this critical point set.

Lemma 3.2. For generic $\eta$, the critical points of $\mathcal{C}_{\eta}$ on $\mathcal{B}$ are all non-degenerate.

Proof. For an irreducible critical point $c \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)$, choose a $C^{\infty}$ solution $(A, \psi)$ to (9) which represents $c$. The Hessian operator $Q_{c}$ has a $\mathcal{G}$-equivariant extension given by (13), namely
$$\mathcal{T}_{(A, \psi)}=\left(\begin{array}{cc}
L_{(A, \psi)} & G_{(A, \psi)} \\
G_{(A, \psi)}^{*} & 0
\end{array}\right) .$$
By direct calculation, we obtain
$$\operatorname{Ker} Q_{c} \cong \operatorname{Ker} \mathcal{T}_{(A, \psi)} \cong \operatorname{Ker} L_{(A, \psi)} / \operatorname{Im} G_{(A, \psi)} .$$
Then Proposition 2.6 implies that $\operatorname{Ker} Q_{c}=0$ for generic $\eta$.
If $\theta=[A, 0]$ is a critical point of $\mathcal{C}_{\eta}$ on $\mathcal{B}$, which only happens when $Y$ is a rational homology 3-sphere $\left(* F_{A}=\eta\right)$, then one can check that under the condition $\operatorname{Ker} \not \partial_{A}=0, \operatorname{Ker} L_{(A, 0)} / \operatorname{Im} G_{(A, 0)}$ is zero for the deformation complex (13) at $(A, 0)$, hence $\theta$ is also non-degenerate. \(\square\)

Henceforth $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ denotes the set of critical points of $\mathcal{C}_{\eta}$ which are assumed all non-degenerate.

There are two fundamental lemmata concerning the gradient of the Chern-Simons-Dirac functional and the estimate of local distance near a critical point. The first of these shows that $\mathcal{C}_{\eta}$ satisfies the Palais-Smale condition which was proved for the unperturbed case $(\eta=0)$ in [25] [13]. The proof here follows the arguments from [25].

Lemma 3.3. For any $\epsilon>0$, there is $\lambda>0$ such that if $[A, \psi] \in \mathcal{B}$ has $L_{1}^{2}$-distance at least $\epsilon$ from all the critical points in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, then
$$\left\|\nabla \mathcal{C}_{\eta, \nu}([A, \psi])\right\|_{L^{2}}>\lambda .$$

Proof. Suppose that, on the contrary, there is a sequence $c_{i}$ in $\mathcal{B}^{*}$ whose $L_{1}^{2}$-distance from $c_{i}$ to the set of critical points is at least $\epsilon$, for which $\left\|\nabla \mathcal{C}_{\eta}\left(c_{i}\right)\right\|_{L^{2}} \rightarrow 0$ as $i \rightarrow \infty$. Choose a sequence of $\left(A_{i}, \psi_{i}\right)$ representing $c_{i}$, then there is a constant $C$ such that
$$\int_{Y}\left(\left|* F_{A_{i}}-\sigma\left(\psi_{i}, \psi_{i}\right)-\eta\right|^{2}+2\left|\not \partial_{A_{i}} \psi_{A_{i}}\right|^{2}\right) d v o l \leq C .$$
Using the Weitzenböck formula and Lemma 2.2, we have
$$\left\|F_{A_{i}}\right\|_{L^{2}}^{2}+\left\|\sigma\left(\psi_{i}, \psi_{i}\right)+\eta\right\|_{L^{2}}^{2}-2<* F_{A_{i}}, \eta>+2\left\|\nabla_{A_{i}} \psi\right\|_{L^{2}}^{2}+\frac{s}{2}\left\|\psi_{i}\right\|_{L^{2}}^{2} \leq C,$$
where $s$ is the scalar curvature on $(Y, g)$. Applying the inequality $2|a b| \leq \frac{1}{2}|a|^{2}+2|b|^{2}$ and the Cauchy-Schwartz inequality, we can rewrite the above expression as
$$\begin{aligned}
& \frac{1}{2}\left\|F_{A_{i}}\right\|_{L^{2}}^{2}+\frac{1}{8}\left\|\psi_{i}\right\|_{L^{4}}^{4}+2\left\|\nabla_{A_{i}} \psi\right\|_{L^{2}}^{2} \\
\leq & C+3\|\eta\|_{L^{2}}^{2}+\max _{y \in Y}\left\{-\frac{s(y)}{2}\right\} \sqrt{\operatorname{Vol}(Y)}\left\|\psi_{i}\right\|_{L^{4}}^{2} \\
\leq & C+3\|\eta\|_{L^{2}}^{2}+\frac{1}{16}\left\|\psi_{i}\right\|_{L^{4}}^{4}+\max _{y \in Y}\left\{-\frac{|s(y)|^{2}}{2}\right\} \operatorname{Vol}(Y) .
\end{aligned}$$
From this inequality, we see that $\left\|F_{A_{i}}\right\|_{L^{2}},\left\|\psi_{i}\right\|_{L^{4}}$ and $\left\|\nabla_{A_{i}} \psi\right\|_{L^{2}}$ are all bounded independent of $i$. By standard elliptic regularity theory we know that there exists a subsequence of $\left\{A_{i}, \psi_{i}\right\}$, such that $\left(A_{i}, \psi_{i}\right)$ converges in $L_{1}^{2}$-topology to a limit $\left(A_{\infty}, \psi_{\infty}\right)$ which is a solution to the Seiberg-Witten equations (9) and hence represents a critical point in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$. This contradicts the fact that $\left\{\left[A_{i}, \psi_{i}\right]\right\}$ has distance at least $\epsilon$ from the critical points. \(\square\)

Remark 3.4. Note that $\lambda$ is independent of $\eta$ when $\eta$ is sufficiently small, hence from now on, we choose a sufficiently small $\epsilon_{0} \ll 1$ and $\eta$ to have $L^{2}$-norm less than $\epsilon_{0} \lambda$.

The second lemma is the following $L_{1}^{2}$-distance estimate near the non-degenerate critical points of $\mathcal{C}_{\eta}$, which was also established in [25].

Lemma 3.5. Suppose $\alpha$ is a non-degenerate critical point of $\mathcal{C}_{\eta}$. There exists a positive constant $C_{\alpha}$ and an $\epsilon>0$, depending on $\alpha$, such that if the $L_{1}^{2}$-distance from $[A, \psi]$ to $\alpha$ is less than $\epsilon$, then the $L_{1}^{2}$-distance from $[A, \psi]$ to $\alpha$ (denoted by $\operatorname{dist}_{L_{1}^{2}}([A, \psi], \alpha)$ ) is bounded by
$$C_{\alpha}\left\|\nabla \mathcal{C}_{\eta, \nu}(A, \psi)\right\|_{L^{2}} .$$

Proof. When $\operatorname{dist}_{L_{1}^{2}}([A, \psi], \alpha)$ is sufficiently small, there are representatives $(A, \psi)$ and $\left(A_{\alpha}, \psi_{\alpha}\right)$ for $[A, \psi]$ and $\alpha$ respectively such that $(A, \psi)=\left(A_{\alpha}, \psi_{\alpha}\right)+(b, \phi)$ with $(b, \phi) \in T_{\alpha} \mathcal{B}^{*}$ with $L_{1}^{2}$-norm less than some $\epsilon$ (to be determined). Then
$$\nabla \mathcal{C}_{\eta}(A, \psi)=Q_{\alpha}(b, \phi)+N(b, \phi),$$
where $N(b, \phi)$ is a quadratic term in $(b, \phi)$, satisfying $\|N(b, \phi)\|_{L^{2}} \leq C \epsilon\|(b, \phi)\|_{L_{1}^{2}}$ where $C$ is the universal constant for the Sobolev multiplication theorem. As $Q_{\alpha}$ is non-degenerate, let $\lambda_{1}$ be the first absolute eigenvalue of $Q_{\alpha}$ (Cf. Lemma 3.1). We then obtain
$$\begin{aligned}
\lambda_{1}\|(b, \phi)\|_{L_{1}^{2}} & \leq\left\|Q_{\alpha}(b, \phi)\right\|_{L^{2}} \\
& \leq\left\|\nabla \mathcal{C}_{\eta}(A, \psi)\right\|_{L^{2}}+\|N(b, \phi)\|_{L^{2}} \\
& \leq\left\|\nabla \mathcal{C}_{\eta}(A, \psi)\right\|_{L^{2}}+C \epsilon\|(b, \phi)\|_{L_{1}^{2}} .
\end{aligned}$$
Choose $\epsilon<\frac{\lambda_{1}}{2 C}$, then
$$\|(b, \phi)\|_{L_{1}^{2}} \leq \frac{1}{\lambda_{1}-C \epsilon}\left\|\nabla \mathcal{C}_{\eta}(A, \psi)\right\|_{L^{2}} \leq \frac{2}{\lambda_{1}}\left\|\nabla \mathcal{C}_{\eta}(A, \psi)\right\|_{L^{2}} .$$
Set $C_{\alpha}=\frac{2}{\lambda_{1}}$, we get $\operatorname{dist}_{L_{1}^{2}}([A, \psi], \alpha) \leq C_{\alpha}\left\|\nabla \mathcal{C}_{\eta}(A, \psi)\right\|_{L^{2}}$. \(\square\)

For any two irreducible critical points $\left[A_{0}, \psi_{0}\right]$ and $\left[A_{1}, \psi_{1}\right]$, choose a path $\left[A_{t}, \psi_{t}\right]$ on $\mathcal{B}^{*}$ connecting $\left[A_{0}, \psi_{0}\right]$ to $\left[A_{1}, \psi_{1}\right]$. Then by Lemma 3.1, $Q_{\left[A_{t}, \psi_{t}\right]}$ defines a path of self-adjoint Fredholm operators, each of which has eigenvalues forming a discrete subset of the real line with no accumulation points. The spectral flow of $Q_{\left[A_{t}, \psi_{t}\right]}$ along this path is defined to be the intersection number of the spectrum graph
$$\bigcup_{t \in[0,1]} \operatorname{Spec} Q_{\left[A_{t}, \psi_{t}\right]}$$
with the line $\epsilon=0$ (Cf. [1]). The spectral flow of the Hessian operator defines a locally constant function on the space of continuous paths in $\mathcal{B}^{*}$ between $\left[A_{0}, \psi_{0}\right]$ and $\left[A_{1}, \psi_{1}\right]$ depending only on the homotopy class of the path between $\left[A_{0}, \psi_{0}\right]$ and $\left[A_{1}, \psi_{1}\right]$. By the Atiyah-Patodi-Singer index theorem, its $\bmod (d(\mathfrak{s}))$ reduction doesn't depend on the homotopy class of the path, where $d(\mathfrak{s})$ is the divisibility of the first Chern class $c_{1}(\operatorname{det}(W))$ in $H^{2}(Y, \mathbb{Z}) /$ Torsion .

We know that $Q_{[A, \psi]}$ has a $\mathcal{G}$-equivariant extension $\mathcal{T}_{(A, \psi)}$ referred to as the extended Hessian operator at a smooth solution ( $A, \psi$ ) to the Seiberg-Witten equations (9) on $\mathcal{A}$ representing $[A, \psi]$. Let $\left(A_{0}, \psi_{0}\right)$ and $\left(A_{1}, \psi_{1}\right)$ represent two irreducible critical points $\left[A_{0}, \psi_{0}\right]$ and $\left[A_{1}, \psi_{1}\right]$ in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ respectively. By its construction, the kernel of $\mathcal{T}_{\left(A_{i}, \psi_{i}\right)}$ is trivial, and so the spectral flow of $T_{(A, \psi)}$ from $\left(A_{0}, \psi_{0}\right)$ to $\left(A_{1}, \psi_{1}\right)$ is a well defined $\mathbb{Z}$-valued function and
$$S F_{\left[A_{0}, \psi_{0}\right]}^{\left[A_{1}, \psi_{1}\right]} Q=S F_{\left(A_{0}, \psi_{0}\right)}^{\left(A_{1}, \psi_{1}\right)} \mathcal{T}(\bmod d(\mathfrak{s})) .$$

For a homology 3-sphere $Y$, we need to choose the perturbation $\eta$ so that the unique reducible critical point $\theta$ is isolated, that is, $(g, \eta)$ is away from the codimension one set (Cf. [20]) where the corresponding Dirac operator has non-trivial kernel. Then we can replace $\left[A_{0}, \psi_{0}\right]$ by $\theta$ in (16). Now $\mathcal{T}$ has one dimensional kernel at $\theta$, therefore the spectral flow of $\mathcal{T}$ from $\theta$ to an irreducible critical point is defined to be the intersection number of the eigenvalues with the line $\lambda=-\epsilon$ where $\epsilon$ is any sufficiently small positive number (see [1]).

Therefore, using the spectral flow of the Hessian operator, we can define a relative index map on the critical point set $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$.

Definition 3.6. Using the spectral flow of the Hessian operator of the Chern-Simons-Dirac functional, there is a relative index map on the critical point set $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ :
$$\mathfrak{i}: \quad \mathcal{M}_{Y}(\mathfrak{s}, \eta) \times \mathcal{M}_{Y}(\mathfrak{s}, \eta) \longrightarrow \mathbb{Z}_{d(\mathfrak{s})}$$
which is the spectral flow $(\bmod d(\mathfrak{s}))$ of the extended Hessian operator along any path connecting two smooth solutions to (9) representing two critical points in $\mathcal{B}$. When $c_{1}(\mathfrak{s})$ is a torsion class (as occurs for example when $Y$ is a homology 3-sphere) then $\mathfrak{i}$ is an integer-valued function.

\subsection*{3.2 Estimates on gradient flowlines}

The downward gradient flow equation for $\mathcal{C}_{\eta}$ on $\mathcal{A}$ is by definition given by the paths of pairs $(A(t), \psi(t))$ that satisfy the equations
$$\left\{\begin{array}{l}
\frac{d A(t)}{d t}=-* F_{A(t)}+\sigma(\psi, \psi)+\eta, \\
\frac{d \psi(t)}{d t}=-\not \partial_{A(t)} \psi(t) .
\end{array}\right.$$

Using the projection $\pi: Y \times \mathbb{R} \rightarrow Y$, we identify $\Omega^{2,+}(Y \times \mathbb{R}, i \mathbb{R}) \cong \pi^{*}\left(\Omega^{1}(Y, i \mathbb{R})\right)$ by sending $\rho(t)$ to $\frac{1}{2}(* \rho(t)+\rho(t) \wedge d t)$, and identify $\Omega^{1}(Y \times \mathbb{R}, i \mathbb{R}) \cong \pi^{*}\left(\Omega^{0}(Y, i \mathbb{R}) \oplus \Omega^{1}(Y, i \mathbb{R})\right)$ by sending $(f(t), \rho(t))$ to $\rho(t)+f(t) d t$. Using Clifford multiplication by $d t$, we can identify the positive and negative spinor bundles $W^{ \pm}$both as $\pi^{*}(W)$ via $\rho^{ \pm}$, such that for any 1-form $a \in \Omega^{1}(Y, i \mathbb{R})$ and $\psi \in W$, we have $\rho^{+}(a . \psi)=a . d t . \rho^{+}(\psi)=a . \rho^{-}(\psi)$.

Let $\psi(t)$ be a section of $\pi^{*}(W)$ and $A(t)$ be a family of connections on $\operatorname{det}(W)$. Then we can view $A(t)$ as a connection on $\operatorname{det}\left(\pi^{*} W\right)$, and the twisted Dirac operator $\not D_{A}$ for $\left(Y \times \mathbb{R}, \pi^{*}(W)\right)$ can be expressed as $\partial_{t}+\not \partial_{A(t)}$ in the sense of
$$\not D_{A}\left(\rho^{+} \psi\right)=\rho^{-}\left(\left(\partial_{t}+\not \partial_{A(t)}\right) \psi(t)\right) .$$

Then, as discovered by Kronheimer-Mrowka [15], the downward gradient flow equations (18) are the following Seiberg-Witten equations on $\left(Y \times \mathbb{R}, \pi^{*}(W)\right)$ in temporal gauge (the $d t$
component of $U(1)$-connection on the determinant bundle vanishes identically).
$$\left\{\begin{array}{l}
F_{A}^{+}=q(\psi, \psi)+\eta^{+} \\
\not D_{A} \psi=0
\end{array}\right.$$
where $F_{A}^{+}$is the self-dual part of the curvature $F_{A}, \eta^{+}=\frac{1}{2}\left(*_{3} \eta+\eta \wedge d t\right)$, and $q(\psi, \psi)$ is the self-dual 2-form given by
$$q(\psi, \psi)=(d t \wedge \sigma(\psi, \psi))^{+}=\frac{1}{2}\left(d t \wedge \sigma(\psi, \psi)+*_{3} \sigma(\psi, \psi)\right) .$$
Two solutions to the equations (19) are gauge equivalent if the paths in $\mathcal{A}$ they determine in temporal gauge are gauge equivalent under the gauge group $\mathcal{G}_{Y}=\operatorname{Map}(Y, U(1))$.

For any solution $S(t)=(A(t), \psi(t))$ of the downward gradient flow equations (18), we have, for any $t_{1}<t_{2}$,
$$\begin{aligned}
& \mathcal{C}_{\eta}\left(S\left(t_{1}\right)\right)-\mathcal{C}_{\eta}\left(S\left(t_{2}\right)\right) \\
= & -\int_{t_{1}}^{t_{2}}<\nabla \mathcal{C}_{\eta}\left((S(t)), \frac{\partial S(t)}{\partial t}>_{L^{2}} d t\right. \\
= & \int_{t_{1}}^{t_{2}} d t \int_{Y}\left(\left|\frac{\partial A(t)}{\partial t}\right|^{2}+2\left|\frac{\partial \psi(t)}{\partial t}\right|^{2}\right) d v o l_{Y} \\
= & \int_{t_{1}}^{t_{2}} \int_{Y}\left(\left|* F_{A}-\sigma(\psi, \psi)-\eta\right|^{2}+2\left|\not \partial_{A} \psi\right|^{2}\right) d v o l_{Y} \\
= & \int_{t_{1}}^{t_{2}} d t \int_{Y}\left(\left|F_{A}\right|^{2}+|\sigma(\psi, \psi)+\eta|^{2}-2<* F_{A}, \eta>+2\left|\nabla_{A} \psi\right|^{2}+\frac{s}{2}|\psi|^{2}\right) d v o l_{Y} \\
= & \int_{t_{1}}^{t_{2}} d t \int_{Y}\left(\left|F_{A}\right|^{2}+|\sigma(\psi, \psi)+\eta|^{2}+2\left(F_{A} \wedge \eta\right)+2\left|\nabla_{A} \psi\right|^{2}+\frac{s}{2}|\psi|^{2}\right) d v o l_{Y}
\end{aligned}$$
where $F_{A}$ is the curvature of $A(t)$ on a $t$-slice of $\left[t_{1}, t_{2}\right] \times Y, *$ is the Hodge star operator on $(Y, g), \nabla_{A}$ is the covariant derivative on $W$ over the $t$-slice of $\left[t_{1}, t_{2}\right] \times Y$ and all the norms are on the $t$-slice.

Note that $A(t)$ can be viewed as a connection on the determinant line bundle of the pull-back Spin $^{c}$ structure on $\left[t_{1}, t_{2}\right] \times Y$. We will write $\mathbb{A}=A(t)$ for this connection on the determinant line bundle over $\left[t_{1}, t_{2}\right] \times Y$ to distinguish it from $A(t)$ viewed as a connection on the determinant line bundle over the $t$-slice of $\left[t_{1}, t_{2}\right] \times Y$. Similarly, denote the corresponding section of the pull-back Spin ${ }^{c}$ bundle over $\left[t_{1}, t_{2}\right] \times Y$ by $\Psi=\psi(t)$. If $(A(t), \psi(t))$ is a solution to the gradient flow equation (18), then $(\mathbb{A}, \Psi)$ is a solution to the 4-dimensional Seiberg-Witten equations (19) on $\left[t_{1}, t_{2}\right] \times Y$. With this notation understood, the last integration in (20) has a 4-dimensional analogue, called the energy of the 4-dimensional monopole. We denote it by $E_{\left[t_{1}, t_{2}\right] \times Y}(\mathbb{A}, \Psi)$ and define it as follows.
$$\begin{aligned}
& E_{\left[t_{1}, t_{2}\right] \times Y}(\mathbb{A}, \Psi) \\
= & \int_{\left[t_{1}, t_{2}\right] \times Y}\left(\left|F_{\mathbb{A}}\right|^{2}+2\left|q(\Psi, \Psi)+\eta^{+}\right|^{2}+2\left|\nabla_{\mathbb{A}} \Psi\right|^{2}+\frac{s}{2}|\Psi|^{2}\right) d v o l+2\left(F_{\mathbb{A}} \wedge d t \wedge \eta\right)
\end{aligned}$$

Since
$$\left|F_{\mathbb{A}}\right|^{2}=\left|F_{A}\right|^{2}+\left|\frac{\partial A(t)}{\partial t}\right|^{2},\left|\nabla_{\mathbb{A}} \Psi\right|^{2}=\left|\nabla_{A} \psi\right|^{2}+\left|\frac{\partial \psi(t)}{\partial t}\right|^{2}$$
and
$$2\left|q(\Psi, \Psi)+\eta^{+}\right|^{2}=|\sigma(\psi, \psi)+\eta|^{2},$$
we know that
$$E_{\left[t_{1}, t_{2}\right] \times Y}(\mathbb{A}, \Psi)=2\left(\mathcal{C}_{\eta}\left(S\left(t_{1}\right)\right)-\mathcal{C}_{\eta}\left(S\left(t_{2}\right)\right)\right) .$$
Hence we will say that any gradient flow line $S(t)=(A(t), \psi(t))\left(t \in\left[t_{1}, t_{2}\right]\right)$ on $\mathcal{A}$ has a finite variation of $\mathcal{C}_{\eta}$ if $S(t)$ satisfies
$$\mathcal{C}_{\eta}\left(S\left(t_{1}\right)\right)-\mathcal{C}_{\eta}\left(S\left(t_{2}\right)\right)=\int_{t_{1}}^{t_{2}}\left(\left\|\frac{\partial A(t)}{\partial t}\right\|_{L^{2}(Y)}^{2}+2\left\|\frac{\partial \psi(t)}{\partial t}\right\|_{L^{2}(Y)}^{2}\right) d t<\infty .$$
That is, the corresponding 4-dimensional monopole $(\mathbb{A}, \Psi)$ has finite energy over $\left[t_{1}, t_{2}\right] \times Y$, or equivalently
$$\int_{t_{1}}^{t_{2}}\left\|\nabla \mathcal{C}_{\eta}(S(t))\right\|_{L^{2}(Y)}^{2} d t=\int_{t_{1}}^{t_{2}}\left(\left\|\frac{\partial A(t)}{\partial t}\right\|_{L^{2}(Y)}^{2}+\left\|\frac{\partial \psi(t)}{\partial t}\right\|_{L^{2}(Y)}^{2}\right) d t<\infty .$$

Lemma 3.7. Suppose $(\mathbb{A}, \Psi)$ to be a solution to the Seiberg-Witten equations (19) on $[t-2, t+2] \times Y$ with finite energy
$$E_{[t-2, t+2] \times Y}(\mathbb{A}, \Psi)<E_{0} .$$
For any positive integer $k$, there exists a constant $C$ depending on the metric on $Y$ and the perturbation term $\eta$ such that all the $C^{k}$-norms of $F_{\mathbb{A}}$ and $\Psi$ on $\left[t-\frac{3}{2}, t+\frac{3}{2}\right] \times Y$ are bounded by $C\left(\sqrt{E_{0}}+1\right)$.

Proof. Let $N_{s}=[t-s, t+s] \times Y$. From $E_{N_{2}}(\mathbb{A}, \Psi)<E_{0}$, we immediately have
$$\begin{aligned}
& \left\|F_{\mathbb{A}}\right\|_{L^{2}\left(N_{2}\right)}^{2} \leq \frac{E_{0}}{4}+C_{0}, \\
& \|\Psi\|_{L^{4}\left(N_{2}\right)}^{4} \leq 4 E_{0}+C_{0}, \\
& \left\|\nabla_{\mathbb{A}} \Psi\right\|_{L^{2}\left(N_{2}\right)}^{2} \leq \frac{E_{0}}{4}+C_{0},
\end{aligned}$$
for some constant $C_{0}$ depending on the metric on $Y$ and $\eta$. The standard bootstrapping argument in elliptic regularity theory (Cf. [23]) implies that the $C^{k}$-norms of $F_{\mathbb{A}}$ and $\Psi$ on $\left[t-\frac{3}{2}, t+\frac{3}{2}\right] \times Y$ are bounded by $C\left(\sqrt{E_{0}}+1\right)$ for some constant $C_{0}$ depending on the metric on $Y$ and $\eta$. \(\square\)

Lemma 3.8. Given a sufficiently small $\epsilon>0$, there exists a constant $E_{0}>0$ such that, for a solution $(A(t), \psi(t))$ to the Seiberg-Witten equations (19) on $[T-2, T+2] \times Y$ in temporal gauge, with finite energy $E_{[T-2, T+2] \times Y}(A(t), \psi(t))<E_{0}$, there exists a critical point $\alpha$ in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ with $L_{1}^{2}$-distance from $[A(t), \psi(t)] \in \mathcal{B}$ to $\alpha$ less than $\epsilon$ for any $t \in[T-1, T+1]$.

Proof. The critical points of $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ are non-degenerate and hence isolated. Given an $\epsilon$ sufficiently less than $\min \left\{\operatorname{dist}_{L_{1}^{2}}(\alpha, \beta): \alpha, \beta \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)\right\}$, let $\lambda$ be the constant in Lemma 3.3 such that if $[A, \psi]$ has $L_{1}^{2}$-distance at least $\epsilon$ to any critical point in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, then $\left\|\nabla \mathcal{C}_{\eta}([A, \psi])\right\|_{L^{2}(Y)}>\lambda$. Now we only need to show that for any $t \in[T-1, T+1]$, $\left\|\nabla \mathcal{C}_{\eta}([A(t), \psi(t)])\right\|_{L^{2}(Y)}<\lambda$.

Let $N_{s}=[T-s, T+s] \times Y$ and $(\dot{A}, \dot{\psi})=\left(\frac{\partial A(t)}{\partial t}, \frac{\partial \psi(t)}{\partial t}\right)$. Differentiating the Seiberg-Witten equations (19) and noting that $\left(\frac{\partial A(t)}{\partial t}, \frac{\partial \psi(t)}{\partial t}\right)=-\nabla \mathcal{C}_{\eta}(A, \psi)$ is $L^{2}$-orthogonal to the gauge orbit at each point, we obtain the following elliptic system of equations on $[T-2, T+2] \times Y$,
$$\left\{\begin{array}{l}
P_{+}(d \dot{A})-2 q(\dot{\psi}, \psi)=0 \\
d^{*} \dot{A}+i \operatorname{Im}<\dot{\psi}, \psi>=0 \\
\not D_{A} \dot{\psi}+\frac{1}{2} \dot{A} \cdot \psi=0 .
\end{array}\right.$$
We deduce from this system of equations and the estimates on $\psi$ in Lemma 3.7 that
$$\begin{aligned}
\|(\dot{A}, \dot{\psi})\|_{L_{1}^{2}\left(N_{\frac{3}{2}}\right)} & \leq C_{0}\left(\|(\dot{A}, \dot{\psi})\|_{L_{1}^{2}\left(N_{\frac{3}{2}}\right)}+\left\|\left(P_{+}(d \dot{A}), d^{*} \dot{A}, \not D_{A} \dot{\psi}\right)\right\|_{L_{1}^{2}\left(N_{2}\right)}\right) \\
& \leq C_{0}\left(\|(\dot{A}, \dot{\psi})\|_{L_{1}^{2}\left(N_{\frac{3}{2}}\right)}+\left\|\left(q(\dot{\psi}, \psi), i \operatorname{Im}<\dot{\psi}, \psi>, \frac{1}{2} \dot{A} . \psi\right)\right\|_{L_{1}^{2}\left(N_{2}\right)}\right) \\
& \leq C_{1}\left(\sqrt{E_{0}}+\|\psi\|_{C^{0}}\|(\dot{A}, \dot{\psi})\|_{L_{1}^{2}\left(N_{2}\right)}\right) \\
& \leq C_{1}\left(\sqrt{E_{0}}+C_{2}\left(\sqrt{E_{0}}+1\right) \sqrt{E_{0}}\right) \\
& \leq C_{3} \sqrt{E_{0}} .
\end{aligned}$$
Here the $C_{i}$ 's are constants depending on the metric on $Y$ and $\eta$, and $\sqrt{E_{0}}$ bounds the energy of $(A(t), \psi(t))$. Therefore, from the standard elliptic regularity theory of Degiorgi-Nash-Moser ([35] Page 169-179), we get that for any $t \in[T-1, T+1]$,
$$\left\|\nabla \mathcal{C}_{\eta}([A(t), \psi(t)])\right\|_{L^{2}(Y)}=\|(\dot{A}, \dot{\psi})\|_{L^{2}(\{t\} \times Y)} \leq C_{4}\|(\dot{A}, \dot{\psi})\|_{L_{1}^{2}\left(N_{\frac{3}{2}}\right)} \leq C_{5} \sqrt{E_{0}} .$$
Now we can choose our solution $(A(t), \psi(t))$ so that its energy is bounded by $E_{0}$ with $C_{5} \sqrt{E_{0}} \leq \epsilon$, then the claim in the lemma follows. \(\square\)

We remark that standard elliptic regularity theory implies that $[A(t), \psi(t)]$ has, for all $k$, $C^{k}$-distance $\epsilon$ or less to a critical point in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$ for any $t \in[T-1, T+1]$. The claims in

Lemma 3.8 still hold for a solution to the Seiberg-Witten equations on any compact set times $Y$ with sufficiently small energy.

Now we can establish the crucial lemma concerning the exponential decay estimate on a flowline with small energy.

Proposition 3.9. There is a constant $\delta>0$, such that a choice of sufficiently small $\epsilon$ determines $E_{0}>0$ with the following property: suppose that $(A(t), \psi(t))$ is a solution to the Seiberg-Witten equations on $\left[R_{1}-2, R_{2}+2\right] \times Y\left(R_{1}<R_{2}\right)$ in temporal gauge with energy
$$E_{\left[R_{1}-2, R_{2}+2\right] \times Y}(A(t), \psi(t))<E_{0},$$
then there exists a critical point $\alpha \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)$ such that the $L_{1}^{2}$-distance from $[A(t), \psi(t)]$ (for any $t \in\left[R_{1}, R_{2}\right]$ ) to $\alpha$ is at most $4 \epsilon\left(e^{-\delta\left(t-R_{1}\right)}+e^{-\delta\left(R_{2}-t\right)}\right)$. Furthermore, there exists a sequence of constants $\left\{\lambda_{k}\right\}_{k=0,1,2, \ldots}$ such that there is a point $\left(A_{\alpha}, \psi_{\alpha}\right)$ representing $\alpha$ for which
$$\left|\nabla^{k}\left(A(t)-A_{\alpha}\right)\right|+\left|\left(\nabla_{A_{\alpha}}\right)^{k}\left(\psi(t)-\psi_{\alpha}\right)\right| \leq \lambda_{k}\left(e^{-\delta\left(t-R_{1}\right)}+e^{-\delta\left(R_{2}-t\right)}\right),$$
for any point $(t, y) \in\left[R_{1}, R_{2}\right] \times Y$.

Proof. We can choose $\epsilon>0$ and $E_{0}>0$ as in Lemma 3.8, so that $\operatorname{dist}_{L_{1}^{2}}([A(t), \psi(t)], \alpha)<\epsilon$ for some critical point $\alpha \in \mathcal{M}_{Y}(\mathfrak{s}, \eta)$ and any $t \in\left[R_{1}-1, R_{2}+1\right]$. Then, on $\left[R_{1}-1, R_{2}+1\right] \times Y$, we can write
$$(A(t), \psi(t))=\left(A_{\alpha}, \psi_{\alpha}\right)+(b, \phi)$$
for some representative ( $A_{\alpha}, \psi_{\alpha}$ ) of $\alpha$, and ( $b, \phi$ ) has $C^{1}$-norm less than $\epsilon$ and satisfies $d^{*} b+i I m<\psi_{\alpha}, \phi>=0$. As $(A(t), \psi(t))$ is a solution to the Seiberg-Witten equations on $\left[R_{1}-1, R_{2}+1\right] \times Y$, the pair $(b, \phi)$ must satisfy
$$\partial_{t}(b, \phi)+Q_{\alpha}(b, \phi)+N(b, \phi)=0,$$
where $Q_{\alpha}(b, \phi)=\left(* d b-2 \sigma\left(\psi_{\alpha}, \phi\right), \not \partial_{A_{\alpha}} \phi+\frac{1}{2} b . \psi_{\alpha}\right)$ and $N(b, \phi)=\left(-\sigma(\phi, \phi), \frac{1}{2} b . \phi\right)$.
Note that $Q_{\alpha}$ is the Hessian operator of $\mathcal{C}_{\eta}$ at $\alpha$, whose $L^{2}$ spectrum is discrete, real and without accumulation points (Cf. Lemma 3.1). The non-degeneracy of $\alpha$ implies that 0 is not in the spectrum of $Q_{\alpha}$. Let $\mu_{\alpha}$ be the distance between 0 and the spectrum of $Q_{\alpha}$. On the $t$-slice of $\left[R_{1}-1, R_{2}+1\right] \times Y$,
$$\|N(b, \phi)\|_{L_{1}^{2}(\{T\} \times Y)}<\epsilon\|(b, \phi)\|_{L_{1}^{2}(\{T\} \times Y)} .$$

Let $\lambda_{ \pm}$be the components of $(b, \phi)$ in the positive and negative spectral subspaces of $Q_{\alpha}$ respectively. Let $\left\|\lambda_{ \pm}\right\|$be the functions on $\left[R_{1}-1, R_{2}+1\right]$ given by taking the $L^{2}(Y)$-norm on
the $t$-slice of $\left[R_{1}-1, R_{2}+1\right] \times Y$. Then the differential equation (26) gives rise to the following two differential inequalities
$$\begin{aligned}
& \partial_{t}\left\|\lambda_{+}\right\|-\left(\mu_{\alpha}-\epsilon\right)\left\|\lambda_{+}\right\|+\epsilon \lambda_{-} \| \geq 0 ; \\
& \partial_{t}\left\|\lambda_{-}\right\|+\left(\mu_{\alpha}-\epsilon\right)\left\|\lambda_{-}\right\|-\epsilon \lambda_{+} \| \leq 0 .
\end{aligned}$$
When $\epsilon \ll \mu_{\alpha}$, the comparison principle (Cf. Lemma 9.4 in [32]) can be invoked to establish exponential decay with decay rate $\delta \leq \frac{\mu_{\alpha}-\epsilon}{2}$, that is, for any $t \in\left[R_{1}-1, R_{2}+1\right]$, the $L^{2}$-norm of $(b, \phi)$ on the $t$-slice of $\left[R_{1}-1, R_{2}+1\right] \times Y$ is bounded by $4 \epsilon\left(e^{-\delta\left(t-R_{1}\right)}+e^{-\delta\left(R_{2}-t\right)}\right)$. The standard bootstrapping argument of elliptic regularity theory implies that the $L_{1}^{2}$-distance from $[A(t), \psi(t)]$ for any $t \in\left[R_{1}, R_{2}\right]$ to the critical point $\alpha$ is bounded by $\epsilon\left(e^{-\delta\left(t-R_{1}\right)}+e^{-\delta\left(R_{2}-t\right)}\right)$, which is the claim (25). \(\square\)

Corollary 3.10. Let $(A(t), \psi(t))$ be a solution to the Seiberg-Witten equations (19) in temporal gauge with finite energy on $\mathbb{R} \times Y$, then there exist two 3-dimensional monopoles $\left(A_{\alpha}, \psi_{\alpha}\right)$ and $\left(A_{\beta}, \psi_{\beta}\right)$ representing two critical points $\alpha$ and $\beta$ in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$, such that
\begin{itemize}
\item[1.] $A-A_{\alpha}$ and $\psi-\psi_{\alpha}$ decay exponentially along with their first derivatives as $t \rightarrow-\infty$,
\item[2.] $A-A_{\beta}$ and $\psi-\psi_{\beta}$ decay exponentially along with their first derivatives as $t \rightarrow \infty$.
\end{itemize}

Proof. To establish claim (a), we apply Lemma 3.9 to $(A(t), \psi(t))$ as a solution to the Seiberg-Witten equations (19) in temporal gauge on $(-\infty,-R] \times Y$ with energy arbitrarily small for sufficiently large $R$. This gives the estimate (25) for $\left(A_{\alpha}, \psi_{\alpha}\right)$ representing a critical point $\alpha$ at any point $(t, y) \in(-\infty,-R] \times Y$ where, in (25) we take $R_{1}$ to infinity and $R_{2}=-R$. Claim (b) can be proved in the same way. \(\square\)

From this corollary, we know that if $(A(t), \psi(t))$ is a solution to the Seiberg-Witten equations (19) in temporal gauge with finite energy on $\mathbb{R} \times Y$, then there exists a sufficiently large $T$, such that for $t \in(-\infty,-T]$ or $t \in[T, \infty)$, the gauge equivalent class of $[A(t), \psi(t)]$ lies in a small $\epsilon$-neighborhood of some critical point $\alpha$ or $\beta$ respectively, and approaches the critical point exponentially fast.

\subsection*{3.3 Moduli spaces of flowlines: transversality, compactification and orientibility.}

Let $\alpha, \beta$ be two critical points in $\mathcal{M}_{Y}(\mathfrak{s}, \eta)$. Denote by $\mathcal{M}(\alpha, \beta)$ the moduli space of solutions to the gradient flow equations (18) with the asymptotic limits $\alpha, \beta$ as $t \rightarrow-\infty,+\infty$. Note that there is an $\mathbb{R}$-action on $\mathcal{M}(\alpha, \beta)$ given by translation in the $t$ variable, $\mathbb{R}$ acts freely on $\mathcal{M}(\alpha, \beta)$
when $\alpha$ and $\beta$ are two different critical points. Denote by $\hat{\mathcal{M}}(\alpha, \beta)$ the quotient by this $\mathbb{R}$-action on $\mathcal{M}(\alpha, \beta)$.