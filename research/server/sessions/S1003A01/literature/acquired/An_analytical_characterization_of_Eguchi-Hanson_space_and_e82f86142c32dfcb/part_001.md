---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: An analytical characterization of Eguchi-Hanson space and ...]

---
source_file: 2604_23410.pdf
converter: mathpix
format: mmd
---

\title{
AN ANALYTICAL CHARACTERIZATION OF EGUCHI-HANSON SPACE AND ITS HIGHER-DIMENSIONAL ANALOGS
}

\author{
MICHAEL B. LAW
}

\begin{abstract}
Let $(M, g)$ be a complete 4-dimensional Ricci-flat ALE orbifold with finitely many orbifold points and group at infinity $\mathbb{Z}_{2}$. We prove that if the $L^{2}$ kernel of its Lichnerowicz Laplacian has dimension at most 3, then $(M, g)$ is either the Eguchi-Hanson space or the flat orbifold $\mathbb{R}^{4} / \mathbb{Z}_{2}$. A similar uniqueness result is proved for Calabi's higher-dimensional analogs of the Eguchi-Hanson space among Ricci-flat Kähler ALE orbifolds with group at infinity $\mathbb{Z}_{m}$.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
1.1. Outline of the paper ..... 4
2. Preliminaries ..... 4
2.1. Notation and conventions ..... 4
2.2. Eguchi-Hanson space ..... 5
2.3. Calabi space ..... 5
3. Global symmetry principles ..... 7
3.1. Geometry of ALE spaces ..... 7
3.2. Finding global Killing fields ..... 9
4. A characterization of Eguchi-Hanson space ..... 12
4.1. Metrics on $\mathbb{S}^{3}$ and $\mathbb{R P}^{3}$ with large isometry groups ..... 12
4.2. Proof of Theorem 1.2: dividing into cases ..... 15
4.3. Case (A) ..... 15
4.4. Case (B) ..... 17
5. A characterization of Calabi space ..... 23
5.1. Homogeneous metrics on $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ and isometry groups ..... 24
5.2. Symmetry reduction and the flat case of Theorem 1.4 ..... 24
5.3. The non-flat case of Theorem 1.4 ..... 26
Acknowledgements ..... 31
References ..... 31

\section*{1. Introduction}

Ricci-flat asymptotically locally Euclidean (ALE) spaces lie at the intersection of differential geometry and mathematical physics. In geometry, they arise in the compactness theory and desingularization of Einstein metrics [3, 6, 9, 19, 38, 42], as well as in the construction of manifolds with special holonomy [27, 28]. In physics, complete 4-dimensional Ricci-flat ALE spaces play a central role in Euclidean quantum gravity [21, 24] and form a class of
gravitational instantons. They also arise in various string theories [8, 20]. Let us first state our definition of an ALE space, which allows for orbifold singularities in a compact set.

Definition 1.1. An asymptotically locally Euclidean (ALE) space is a connected Riemannian orbifold $\left(M^{n}, g\right)$ such that there is a finite subgroup $\Gamma \subset S O(n)$ acting freely on $\mathbb{S}^{n-1}$, a compact set $K \subset M$, a radius $R>0$, a diffeomorphism $\Phi: M \backslash K \rightarrow\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma$, and a decay rate $\tau>0$ such that
$$\left|\nabla^{k}\left(\Phi^{*} \bar{g}-g\right)\right|_{g} \leq \mathcal{O}\left(r^{-\tau-k}\right)$$
as $r \rightarrow \infty$ for each $k \in \mathbb{N}_{0}$. Here, $\bar{g}$ is the Euclidean metric on $\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma, \nabla$ is the Levi-Civita connection with respect to $g$, and $r$ is the Riemannian distance from a point with respect to $g$. We call $\tau$ the order of $(M, g)$, and $\Gamma$ its group at infinity. If $\Gamma=\{1\}$, then $(M, g)$ is called asymptotically Euclidean.

The prototypical example of a nontrivial (i.e. nonflat) 4-dimensional Ricci-flat ALE space is Eguchi-Hanson space [21]. This is a complete Ricci-flat ALE metric on the cotangent bundle of $\mathbb{S}^{2}$ with group at infinity $\mathbb{Z}_{2}$. The metric is hyperkähler and $U(2)$-invariant with cohomogeneity one. See §2.2 for further details. We remark that in addition to its underlying physical motivations, Eguchi-Hanson space appears as a common building block in geometric gluing constructions; see for instance [9, 12, 19, 27].

Soon after Eguchi-Hanson space was discovered, Gibbons and Hawking [22] produced a large class of hyperkähler (thus Ricci-flat) gravitational instantons, including ALE spaces with groups at infinity $\mathbb{Z}_{k}(k \geq 1)$. The latter spaces were also constructed by Hitchin using twistor methods [25]. Kronheimer [33] then unified the known constructions of ALE spaces: he constructed and classified all simply-connected hyperkähler ALE 4-manifolds as hyperkähler quotients, exhibiting an ADE correspondence and identifying each space with the minimal resolution of $\mathbb{C}^{2} / \Gamma$ for $\Gamma \subset \operatorname{SU}(2)$.

Motivated by these developments, Bando, Kasue, and Nakajima [6] conjectured that every complete simply-connected Ricci-flat ALE 4-manifold $(M, g)$ is hyperkähler and hence falls under Kronheimer's classification. While this conjecture remains open in general, it is known to hold under additional assumptions. Nakajima [40] proved it in the affirmative assuming $M$ is spin and $\Gamma \subset S U(2)$. Lock and Viaclovsky [37] proved that if $M$ is diffeomorphic to a minimal resolution of $\mathbb{C}^{2} / \Gamma$ or an iterated blowup thereof, where $\Gamma \subset U(2)$, then $\Gamma \subset S U(2)$ and $g$ is hyperkähler. More recently, there has been progress on uniqueness of Eguchi-Hanson space, which is a special case of the Bando-Kasue-Nakajima conjecture. Li [36] proved that if $(M, g)$ is a 4-dimensional Ricci-flat ALE manifold with $\Gamma \subset S U(2)$ and admits a Hermitian non-Kähler structure, then $(M, g)$ is Eguchi-Hanson space with the opposite orientation. Araneda and Lucietti [4] proved a similar uniqueness result assuming $(M, g)$ is toric, Hermitian and non-Kähler, without any assumptions on $\Gamma \subset S O(4)$.

In this paper, we take a different angle. Rather than imposing global symmetry, we establish uniqueness of certain Ricci-flat ALE spaces under an analytical condition on the Lichnerowicz Laplacian $\Delta_{L}$. On a Ricci-flat space, $\Delta_{L}$ operates on symmetric 2-tensors $h$ by
$$\Delta_{L} h=\Delta h+2 \operatorname{Rm}(h),$$
where $(\Delta h)_{k l}=g^{i j} \nabla_{i j}^{2} h_{k l}$ is the rough Laplacian and $\operatorname{Rm}(h)_{i k}=\operatorname{Rm}_{i j k l} h^{j l}$ is the action of the curvature tensor. The operator $\Delta_{L}$ is (a multiple of) the linearized Ricci curvature in a suitable gauge, and its kernel elements represent metric variations that preserve the Ricci-flat condition to first order.

On ALE spaces, it is natural to focus on the $L^{2}{\operatorname{kernel~} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)}$. In gluing problems for Einstein metrics, such kernel elements account for potential obstructions to resolving
orbifold singularities by gluing in ALE manifolds. In Euclidean quantum gravity, elements of $\operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ are known as normalizable zero modes of the gravitational instanton, and they influence the expansion of the gravitational path integral.

Our first result is a classification of 4-dimensional Ricci-flat ALE spaces with group at infinity $\mathbb{Z}_{2}$ when $\operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ is sufficiently small in dimension.

Theorem 1.2. Let $\left(M^{4}, g\right)$ be a complete 4-dimensional Ricci-flat ALE space with finitely many orbifold points and group at infinity $\mathbb{Z}_{2}$. If $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \leq 3$, then $(M, g)$ is isometric to either the Eguchi-Hanson space or the flat orbifold $\mathbb{R}^{4} / \mathbb{Z}_{2}$.

The flat $\mathbb{R}^{4} / \mathbb{Z}_{2}$ has $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)=0$, while $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)=3$ is achieved on Eguchi-Hanson space (see §2.2). By Theorem 1.2, no intermediate examples exist. Thus, any counterexample to the Bando-Kasue-Nakajima conjecture with group at infinity $\mathbb{Z}_{2}$ must have $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \geq 4$, and therefore carries a correspondingly subtler deformation theory.

The regularity assumption in Theorem 1.2 is natural in applications. For instance, it holds for Ricci-flat ALE spaces arising as bubbles from singularities of noncollapsed Gromov-Hausdorff limits of Einstein 4-manifolds [3, 6].

Our second result is a similar theorem for Ricci-flat Kähler ALE spaces in higher dimensions. These are defined as follows.

Definition 1.3. A Kähler orbifold ( $M^{2 m}, g, J$ ) of complex dimension $m$ is called a Kähler ALE space if its underlying Riemannian orbifold $(M, g)$ is an ALE space with group at infinity $\Gamma \subset U(m) \subset S O(2 m)$.

Note that we do not stipulate convergence of the complex structure $J$ to the standard one on $\mathbb{C}^{m} / \Gamma$.

Among the earliest known Ricci-flat Kähler ALE spaces are what we call the Calabi spaces. The Calabi space of complex dimension $m \geq 2$ lives on the total space of the canonical line bundle $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$ of $\mathbb{C P}^{m-1}$, and the group at infinity is $\mathbb{Z}_{m} \subset S U(m)$ generated by an $m$-th root of unity times the identity. It is equipped with a complete $U(m)$-invariant cohomogeneity one Kähler metric. When $m=2$, the Calabi space coincides with Eguchi-Hanson space and is therefore hyperkähler, but when $m \geq 3$ the Calabi space is not hyperkähler. See §2.3 for further details.

Morteza and Viaclovsky [38] computed that $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)=1$ on all Calabi spaces of complex dimension $m \geq 3$. We will prove an analog of Theorem 1.2 for these spaces.

Theorem 1.4. Let $\left(M^{2 m}, g, J\right)$ be a complete Ricci-flat Kähler ALE space with complex dimension $m \geq 3$ and group at infinity $\mathbb{Z}_{m}$. Assume the orbifold singular set has real codimension at least 4. If
$$\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \leq \begin{cases}2 m-3 & \text { if } m \neq 4, \\ 2 & \text { if } m=4,\end{cases}$$
then $(M, g, J)$ is biholomorphically isometric to either the Calabi space or the flat Kähler orbifold $\mathbb{C}^{m} / \mathbb{Z}_{m}$.

Several remarks are in order. Firstly, Theorem 1.4 can be viewed as a gap theorem: under the stated regularity assumptions, no Ricci-flat Kähler ALE space asymptotic to $\mathbb{C}^{m} / \mathbb{Z}_{m}$ (where $m=3$ or $m \geq 5$ ) can have $2 \leq \operatorname{dim}_{\operatorname{ker}_{L^{2}}}\left(\Delta_{L}\right) \leq 2 m-3$, and no Ricci-flat Kähler ALE space asymptotic to $\mathbb{C}^{4} / \mathbb{Z}_{4}$ can have $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)=2$.

Secondly, the regularity assumption is consistent with the celebrated regularity theory for noncollapsed Gromov-Hausdorff limits of Einstein metrics [14].

Thirdly, the proof of Theorem 1.4 uses the classification of homogeneous metrics on lens spaces $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ with large isometry groups. If the isometry group has dimension above some threshold, only Berger metrics can occur. The threshold is relatively higher when $m=4$, so the tighter bound in (1.3) serves to ensure the threshold is surpassed.
1.1. Outline of the paper. In §2, we lay out notations and conventions, then provide a brief summary of the Eguchi-Hanson and Calabi spaces.

In §3, we work on an arbitrary complete Ricci-flat ALE space with nontrivial group at infinity. We develop a symmetry principle that converts bounds on $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ into the existence of global Killing fields tangential to a constant mean curvature foliation of the end. Moreover, the Killing fields integrate to a global isometric Lie group action. This generalizes a symmetry principle developed by the author for Ricci solitons with certain asymptotics [34], which in turn built on Brendle's seminal work on the Bryant soliton [11]. Some of the ingredients used later in §4-5 are also adapted from [34], but the case analyses and classification arguments are specific to the ALE setting.

In §4, we prove Theorem 1.2. Taking $(M, g)$ as in the theorem, we use the results of §3 to find a 3-dimensional Lie group $G$ acting isometrically on $(M, g)$. If $G$ acts by cohomogeneity one, then well-known facts about homogeneous metrics on $\mathbb{S}^{3}$ and $\mathbb{R P}^{3}$ enable us to determine all possibilities for $G$. The structure theory of cohomogeneity one spaces then leads to a diffeomorphism classification of $M$. Aided by results of Lock-Viaclovsky [37] and Kronheimer [33], this implies $(M, g)$ is either Eguchi-Hanson space or the flat $\mathbb{R}^{4} / \mathbb{Z}_{2}$.

On the other hand, if $G$ does not act by cohomogeneity one, then we show that it acts by cohomogeneity two. Lifting to the universal cover $\left(\tilde{M}_{\infty}, \tilde{g}\right)$ of the end of $(M, g)$, and analyzing the lifted action, we find that $\left(\tilde{M}_{\infty}, \tilde{g}\right)$ is (essentially) isometric to a warped product with 2-dimensional base and round $\mathbb{S}^{2}$ fibers. Using a local variant of Birkhoff's theorem in general relativity, we construct convenient coordinates on an infinite region in the base. From this, we deduce that $\tilde{g}$ is Euclidean Schwarzschild of mass $\mu \in \mathbb{R}$ around an infinite ray. However, the ALE decay rate (Theorem 3.1) forces $\mu=0$, so $\tilde{g}$ (and hence $g$ ) is flat on an open set. By unique continuation, $(M, g)$ must be the flat $\mathbb{R}^{4} / \mathbb{Z}_{2}$.

In §5, we prove Theorem 1.4. Taking $(M, g, J)$ as in the theorem, we use the results of §3 to find a Lie group $G$ of large dimension acting isometrically on $(M, g)$ with cohomogeneity one. Using the classification of homogeneous metrics on certain lens spaces with large isometry groups, we show that the principal orbits of the action are quotient-Berger spheres. The structure theory of cohomogeneity one spaces then leads to a diffeomorphism classification of $M$ and a reduction of $g$ to an ODE system. If $(M, g, J)$ is not the flat $\mathbb{C}^{m} / \mathbb{Z}_{m}$, we further use the Kähler condition and the form of $g$ to determine $J$ explicitly. This reduces everything to the Calabi ansatz, from which it follows that $(M, g, J)$ is a Calabi space.

\section*{2. Preliminaries}
2.1. Notation and conventions. All Riemannian orbifolds are assumed smooth throughout. Given a Riemannian orbifold ( $M, g$ ), we will often abbreviate $g=\langle\cdot, \cdot\rangle$. Denote by ∇ the Levi-Civita connection, and $\Delta=\operatorname{tr}_{g} \circ \nabla^{2}$ the Laplacian on tensor fields. Our convention for the Riemann curvature tensor is
$$\operatorname{Rm}(X, Y) Z=\nabla_{Y} \nabla_{X} Z-\nabla_{X} \nabla_{Y} Z+\nabla_{[X, Y]} Z .$$

By the Myers-Steenrod theorem (see [5] for orbifolds), the isometry group $\mathcal{I}(M, g)$ of $(M, g)$ is a Lie group acting smoothly on $(M, g)$. Its identity component is denoted by
$\mathcal{I}^{0}(M, g)$. The Lie algebra of $\mathcal{I}(M, g)$, denoted by $\mathfrak{I}(M, g)$, is the space of Killing fields on $(M, g)$, i.e. vector fields $X$ on $M$ such that $\mathcal{L}_{X} g=0$ where $\mathcal{L}$ is the Lie derivative.

Given a Lie group $G$ and a closed subgroup $H$ of $G$, the centralizer and normalizer of $H$ in $G$ are denoted $C_{G}(H)$ and $N_{G}(H)$ respectively; both are closed subgroups of $G$. We let $C_{G}^{0}(H)$ and $N_{G}^{0}(H)$ be their identity components. The following facts will be used frequently. Their proofs are rudimentary and are therefore omitted.

Lemma 2.1. If $G$ is a Lie group and $H$ is a discrete subgroup, then $N_{G}^{0}(H)=C_{G}^{0}(H)$.
Lemma 2.2. Let $(\tilde{M}, \tilde{g})$ be a simply-connected Riemannian manifold, and $\Gamma \subset \mathcal{I}(\tilde{M}, \tilde{g})$ a finite subgroup of isometries acting freely. Then the quotient manifold $(M, g)$ has isometry group
$$\mathcal{I}(M, g)=N_{\mathcal{I}(\tilde{M}, \tilde{g})}(\Gamma) / \Gamma .$$

If $\mathcal{I}(M, g)$ acts transitively on $(M, g)$, then we call $g$ a homogeneous metric. Finally, if a compact Lie group $G$ acts smoothly on $M$, then the cohomogeneity of the action is the minimal codimension of an orbit.
2.2. Eguchi-Hanson space. Let $\left\{X_{1}, X_{2}, X_{3}\right\}$ be a left-invariant frame on $\mathbb{S}^{3} \cong S U(2)$, and $\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}\right\}$ its dual coframe. Let $\pi: \mathbb{S}^{3} \rightarrow \mathbb{S}^{2}$ be the Hopf fibration, chosen with fibers tangent to $X_{1}$. For each $\varepsilon>0$, define a metric $\tilde{g}_{\mathrm{EH}, \varepsilon}$ on the manifold $(0, \infty) \times \mathbb{S}^{3}$ by
$$\tilde{g}_{\mathrm{EH}, \varepsilon}=\frac{1}{2}\left(r^{2}+\varepsilon\right)^{-\frac{1}{2}}\left(d r^{2}+r^{2} \sigma_{1} \otimes \sigma_{1}\right)+\left(r^{2}+\varepsilon\right)^{\frac{1}{2}}\left(\sigma_{2} \otimes \sigma_{2}+\sigma_{3} \otimes \sigma_{3}\right) .$$
The metric $\tilde{g}_{\mathrm{EH}, \varepsilon}$ is invariant under left multiplication in $S U(2)$ and a right Hopf circle action; see Lemma 4.1. Moreover, since the metric on each $r$-level set depends on $r$, there are no translational isometries. Thus, we have
$$\mathcal{I}^{0}\left((0, \infty) \times \mathbb{S}^{3}, \tilde{g}_{\mathrm{EH}, \varepsilon}\right)=S U(2) \times_{\mathbb{Z}_{2}} U(1) \cong U(2) .$$
This acts with cohomogeneity one since it acts transitively on each level set of $r$.
In particular, $\tilde{g}_{\mathrm{EH}, \varepsilon}$ is invariant under the antipodal map on $\mathbb{S}^{3}$ (equivalently $q \mapsto-q$ on $\operatorname{SU}(2))$, so it induces a metric $g_{\mathrm{EH}, \varepsilon}$ on $(0, \infty) \times \mathbb{R P}^{3}$. As $r \rightarrow 0$, the Hopf fibers shrink and the $\mathbb{R P}^{3}$-level sets of $r$ collapse to a round $\mathbb{S}^{2}$ of scale $\varepsilon>0$. Thus, attaching an $\mathbb{S}^{2} \cong \mathbb{C P}^{1}$ 'bolt' at $r=0$ results in a complete metric $g_{\mathrm{EH}, \varepsilon}$ on the smooth manifold $\mathcal{O}_{\mathbb{C P}}(-2) \cong T^{*} \mathbb{S}^{2}$. We call $\left(\mathcal{O}_{\mathbb{C P}^{1}}(-2), g_{\mathrm{EH}, \varepsilon}\right)$ the $\varepsilon$-Eguchi-Hanson space. Changing $\varepsilon$ only amounts to scaling the metric and applying a diffeomorphism, so we leave $\varepsilon$ unspecified.

Since the antipodal map is central in the group (2.2), Lemma 2.2 implies that $\mathcal{I}^{0}((0, \infty) \times$ $\left.\mathbb{R P}^{3}, g_{\mathrm{EH}, \varepsilon}\right) \cong U(2) / \mathbb{Z}_{2}$. These isometries extend to the $\mathbb{S}^{2}$ bolt, so $\mathcal{I}^{0}\left(\mathcal{O}_{\mathbb{C} \mathbb{P}^{1}}(-2), g_{\mathrm{EH}, \varepsilon}\right) \cong$ $U(2) / \mathbb{Z}_{2}$ as well. Thus, $U(2)$ acts isometrically and almost effectively on Eguchi-Hanson space with kernel $\mathbb{Z}_{2}$. Moreover, one checks using (2.1) that Eguchi-Hanson space is Ricci-flat and ALE with group at infinity $\mathbb{Z}_{2}$. It is in fact hyperkähler and self-dual.

It is well-known that $\operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ has dimension 3 on Eguchi-Hanson space; see [9, 12] for an explicit basis. One generator arises from scaling, and the other two generators arise from deformations of the complex structure. Thus, modulo diffeomorphisms and scaling, these generators do not produce genuinely new Einstein deformations.
2.3. Calabi space. Let $\pi: \mathbb{S}^{2 m-1} \rightarrow \mathbb{C P}^{m-1}$ be the Hopf fibration, where $m \geq 2$. Let $g_{\mathrm{FS}}$ be the Fubini-Study metric on $\mathbb{C P}^{m-1}$ with holomorphic sectional curvature 4, so that the round metric on $\mathbb{S}^{2 m-1}$ of sectional curvature 1 splits as
$$g_{\mathbb{S}^{2 m-1}}=\sigma \otimes \sigma+\pi^{*} g_{\mathrm{FS}},$$
where $\sigma$ is a 1-form dual to the Hopf vector field $\xi$, satisfying $d \sigma=2 \pi^{*} \omega_{\mathrm{FS}}$. For any $a, b>0$, define the Berger metric on $\mathbb{S}^{2 m-1}$ by
$$\tilde{g}_{a, b}=a^{2} \sigma \otimes \sigma+b^{2} \pi^{*} g_{\mathrm{FS}} .$$
It is standard that $\mathcal{I}^{0}\left(\mathbb{S}^{2 m-1}, \tilde{g}_{a, b}\right) \cong U(m)$ if $a \neq b$, and $\mathcal{I}^{0}\left(\mathbb{S}^{2 m-1}, \tilde{g}_{a, b}\right) \cong S O(2 m)$ if $a=b$.
The cyclic subgroup $\mathbb{Z}_{m} \subset U(1) \subset U(m)$ acts freely on $\mathbb{S}^{2 m-1}$ by rotation of the Hopf fibers. The quotient is the lens space which we denote by
$$\mathbb{S}^{2 m-1} / \mathbb{Z}_{m} .$$
Moreover, the $\mathbb{Z}_{m}$-action is isometric on $\left(\mathbb{S}^{2 m-1}, \tilde{g}_{a, b}\right)$ for any $a, b>0$, and is central in the isometry group, so $\tilde{g}_{a, b}$ descends to a quotient-Berger metric $g_{a, b}$ on $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$. By Lemma 2.2, we have $\mathcal{I}^{0}\left(\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}, g_{a, b}\right) \cong U(m) / \mathbb{Z}_{m}$ whenever $a \neq b$.

Consider the complex line bundle $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$ over $\mathbb{C P}^{m-1}$, which is isomorphic to the canonical line bundle of $\mathbb{C P}^{m-1}$. We now briefly review Calabi's construction [13] of Ricci-flat Kähler ALE metrics on $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$ using what is now called the Calabi ansatz; a detailed account may be found elsewhere (e.g. [44, §8]). We first note that $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$ has sphere bundles diffeomorphic to $\mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$. Thus, choosing a radial coordinate $r$ along the fibers, we obtain a diffeomorphism
$$\mathcal{O}_{\mathbb{C P}^{m-1}}(-m) \backslash \mathbb{C P}^{m-1} \cong(0, \infty) \times \mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$$
where the excluded $\mathbb{C P}^{m-1}$ is the zero section. On $(0, \infty) \times \mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$, one considers metrics of the form
$$g=u(r)\left(d r^{2}+r^{2} \sigma \otimes \sigma\right)+v(r) \pi^{*} g_{\mathrm{FS}}=u(r) d r^{2}+g_{r \sqrt{u(r)}, \sqrt{v(r)}}$$
where $u$ and $v$ are smooth positive functions. Equivalently, with the canonical complex structure under which $J\left(\partial_{r}\right)=\frac{1}{r} \xi$, one considers Kähler forms on $(0, \infty) \times \mathbb{S}^{2 m-1} / \mathbb{Z}_{m}$ of the form
$$\omega=u(r) r d r \wedge \sigma+v(r) \pi^{*} \omega_{\mathrm{FS}},$$
where $\omega_{\mathrm{FS}}$ is the Fubini-Study Kähler form on $\mathbb{C P}^{m-1}$. The Kähler condition $d \omega=0$ and the Ricci-flatness condition yield, respectively,
$$v^{\prime}=2 r u, \quad u v^{m-1}=2 .$$
Solving the system (2.5), we get the general solution
$$u(r)=2\left(2 m\left(r^{2}+\varepsilon\right)\right)^{-\frac{m-1}{m}}, \quad v(r)=\left(2 m\left(r^{2}+\varepsilon\right)\right)^{\frac{1}{m}}$$
where $\varepsilon \in \mathbb{R}$. Let $g_{\text {Cal }, \varepsilon}$ be the metric (2.3) with $u$ and $v$ given by (2.6). If $\varepsilon>0$, then $g_{\text {Cal }, \varepsilon}$ closes up smoothly at $r=0$ to give a complete metric on $\mathcal{O}_{\mathbb{C P}^{m-1}}(-m)$, also denoted by $g_{\text {Cal }, \varepsilon}$. We call $\left(\mathcal{O}_{\mathbb{C P}^{m-1}}(-m), g_{\text {Cal }, \varepsilon}\right)$ the $\varepsilon$-Calabi space. Changing $\varepsilon>0$ only amounts to scaling the metric and applying a diffeomorphism, so we leave $\varepsilon$ unspecified.

It follows from the above discussion about isometry groups of Berger metrics that $\mathcal{I}^{0}\left(\mathcal{O}_{\mathbb{C P}^{m-1}}(-m), g_{\mathrm{Cal}, \varepsilon}\right) \cong U(m) / \mathbb{Z}_{m}$. Thus, $U(m)$ acts isometrically and almost effectively on Calabi space with kernel $\mathbb{Z}_{m}$. The action preserves and is transitive on each level set of $r$, so it has cohomogeneity one. Moreover, as one checks using (2.3) and (2.6), Calabi space is Ricci-flat and Kähler ALE with group at infinity $\mathbb{Z}_{m}$. When $m=2$, Calabi space coincides with Eguchi-Hanson space and is therefore hyperkähler. On the other hand, the Calabi spaces with $m \geq 3$ are not hyperkähler.

Observe that if $h \in \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$, then
$$\Delta \operatorname{tr}_{g} h=\operatorname{tr}_{g} \Delta h=-2 \operatorname{tr}_{g} \operatorname{Rm}(h)=-2 g^{i k} \operatorname{Rm}_{i j k l} h^{j l}=2 \operatorname{Ric}_{j l} h^{j l}=0 .$$
Thus, $\operatorname{tr}_{g} h \in \operatorname{ker}_{L^{2}}(\Delta)=\{0\}$. It then follows by [38, Theorem 2.2] that $\operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ is one-dimensional on each Calabi space with $m \geq 3$. The generator of $\operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ arises from scaling, so it does not produce a genuinely new Einstein deformation.

\section*{3. Global symmetry principles}
3.1. Geometry of ALE spaces. First, we have the following result about decay rates of Ricci-flat ALE spaces, due to Kröncke and Szábo (see also [6, 15]). The original proof is given for Ricci-flat ALE manifolds, but it applies to Ricci-flat ALE spaces after standard orbifold adaptations of the weighted elliptic theory.

Theorem 3.1 ([32]). Let $\left(M^{n}, g\right)$ be an $n$-dimensional Ricci-flat ALE space with group at infinity $\Gamma \neq\{1\}$. Then ( $M, g$ ) is of order $n$.

We will also use that every ALE space with nontrivial group at infinity admits an end foliation by constant mean curvature (CMC) hypersurfaces. This follows from work of Chodosh, Eichmair, and Volkmann.

Theorem 3.2 ([16]). Let $\left(M^{n}, g\right)$ be an $A L E$ space with group at infinity $\Gamma \neq\{1\}$, and let $\mathcal{S}=\mathbb{S}^{n-1} / \Gamma$. Then there exists $R_{0} \gg 1$ and a smooth family of hypersurfaces $\left\{\Sigma_{\rho}\right\}_{\rho \geq R_{0}}$ foliating the end of $M$, such that:
\begin{itemize}
\item[(a)] $\Sigma_{\rho}$ is diffeomorphic to $\mathcal{S}$ and has constant mean curvature $\frac{n-1}{\rho}$.
\item[(b)] In any $A L E$ chart $\Phi: M \backslash K \rightarrow\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma \cong(R, \infty) \times \mathcal{S}$, we have for each $\rho \geq R_{0}$
\end{itemize}
$$\Phi\left(\Sigma_{\rho}\right)=\left\{\left(\rho\left(1+u_{\rho}(\theta)\right), \theta\right) \mid \theta \in \mathcal{S}\right\}$$
where $u_{\rho} \in C^{2, \alpha}(\mathcal{S})$ satisfies $\|u\|_{C^{2, \alpha}(\mathcal{S})} \rightarrow 0$ as $\rho \rightarrow \infty$. In fact, by elliptic bootstrapping, $\left\|u_{\rho}\right\|_{C^{k}(\mathcal{S})} \rightarrow 0$ for every $k \geq 0$.
\begin{itemize}
\item[(c)] Let $H$ be the function defined on the end of $M$ by sending a point $x$ to the mean curvature of the $C M C$ leaf containing $x$. Then $H$ is smooth and $\nabla H$ is nonvanishing.
\end{itemize}

In the rest of this subsection, we establish the following result which exhibits a relation between Killing fields and the CMC leaves.

Corollary 3.3. Let $(M, g)$ be a Ricci-flat $A L E$ space with group at infinity $\Gamma \neq\{1\}$. If $W$ is a Killing field on $(M, g)$, then $W$ is tangential to all sufficiently large leaves of the CMC foliation from Theorem 3.2, i.e. $\langle W, \nabla H\rangle=0$. Moreover, $[W, \nabla H]=0$ on such leaves.

Lemma 3.4. Let $(M, g)$ be an ALE space with group at infinity $\Gamma \neq\{1\}$. Let $g_{\rho}$ be the induced metric on the CMC leaf $\Sigma_{\rho}$ with mean curvature $\frac{n-1}{\rho}$, and $A_{\rho}$ the second fundamental form of $\Sigma_{\rho}$. Using (3.1), we identify $\Sigma_{\rho}$ with $\mathcal{S}$, and consider $g_{\rho}$ and $A_{\rho}$ as symmetric 2-tensors on $\mathcal{S}$. Then as $\rho \rightarrow \infty$, we have
$$\rho^{-2} g_{\rho} \rightarrow \bar{g}_{\infty} \quad \text { and } \quad \rho^{2}\left|A_{\rho}\right|_{g_{\rho}}^{2} \rightarrow n-1 \quad \text { smoothly on } \mathcal{S},$$
where $\bar{g}_{\infty}$ is a metric on $\mathcal{S}$ with constant sectional curvature 1.
Proof. By Theorem 3.2, after identifying $\Sigma_{\rho}$ with $\mathcal{S}$ as described and rescaling the metric on $\Sigma_{\rho}$ by $\rho^{-2}$, the resulting metric converges smoothly to that of the unit slice $\{r=1\}$ in the cone $\left((0, \infty) \times \mathcal{S}, d r^{2}+r^{2} \bar{g}_{\infty}\right)$. Hence $\rho^{-2} g_{\rho} \rightarrow \bar{g}_{\infty}$ smoothly. Likewise, the rescaled second
fundamental form converges smoothly to the second fundamental form of $\{r=1\}$, which has squared norm $n-1$. Therefore $\rho^{2}\left|A_{\rho}\right|_{g_{\rho}}^{2}=\left|\rho^{-1} A_{\rho}\right|_{\rho^{-2} g_{\rho}}^{2} \rightarrow n-1$ smoothly. \(\square\)

Recall that if $\Gamma$ is nontrivial, then the first nonzero eigenvalue of $-\Delta_{\bar{g}_{\infty}}$ on functions $\mathbb{S}^{n-1} / \Gamma \rightarrow \mathbb{R}$ is strictly larger than $n-1$. Using this fact and a standard compactness- contradiction argument, we obtain the next lemma.

Lemma 3.5. Let $\Gamma \neq\{1\}$ and $\mathcal{S}=\mathbb{S}^{n-1} / \Gamma$. There exists $\varepsilon>0$ such that if $g$ is a metric on $\mathcal{S}$ and $\phi$ is a smooth function on $\mathcal{S}$ such that
$$\left\|g-\bar{g}_{\infty}\right\|_{C^{2, \alpha}\left(\bar{g}_{\infty}\right)}<\varepsilon, \quad\|\phi-(n-1)\|_{C^{0, \alpha}\left(\bar{g}_{\infty}\right)}<\varepsilon,$$
then $\operatorname{ker}\left(\Delta_{g}+\phi\right)=0$.
Proof. If the lemma were false, then there exist sequences $g_{k} \rightarrow \bar{g}_{\infty}$ in $C^{2, \alpha}\left(\bar{g}_{\infty}\right)$ and $\phi_{k} \rightarrow n-1$ in $C^{0, \alpha}\left(\bar{g}_{\infty}\right)$, as well as nonzero functions $u_{k}$ such that
$$\left(\Delta_{g_{k}}+\phi_{k}\right) u_{k}=0 .$$
Normalizing, we may assume $\left\|u_{k}\right\|_{L^{2}\left(\bar{g}_{\infty}\right)}=1$. Standard elliptic estimates and the $C^{2, \alpha_{-}}$ convergence $g_{k} \rightarrow \bar{g}_{\infty}$ imply a uniform bound
$$\left\|u_{k}\right\|_{H^{2}\left(\bar{g}_{\infty}\right)} \leq C\left(\left\|\Delta_{g_{k}} u_{k}\right\|_{L^{2}\left(\bar{g}_{\infty}\right)}+\left\|u_{k}\right\|_{L^{2}\left(\bar{g}_{\infty}\right)}\right) \leq C .$$
We can then pass to a subsequence and obtain a limit $u_{k} \rightarrow u$ in $H^{1}\left(\bar{g}_{\infty}\right)$, with $\|u\|_{L^{2}\left(\bar{g}_{\infty}\right)}=1$. Now, (3.2) implies that for any smooth function $\eta$ on $\mathcal{S}$,
$$-\int_{\mathcal{S}}\left\langle\nabla^{g_{k}} \eta, \nabla^{g_{k}} u_{k}\right\rangle \mathrm{dvol}_{g_{k}}+\int_{\mathcal{S}} \phi_{k} u_{k} \eta \mathrm{dvol}_{g_{k}}=0 .$$
Taking $k \rightarrow \infty$, we get
$$-\int_{\mathcal{S}}\left\langle\nabla^{\bar{g}_{\infty}} \eta, \nabla^{\bar{g}_{\infty}} u\right\rangle \mathrm{dvol}_{\bar{g}_{\infty}}+\int_{\mathcal{S}}(n-1) u \eta \mathrm{dvol}_{\bar{g}_{\infty}}=0$$
so $\left(\Delta_{\bar{g}_{\infty}}+(n-1)\right) u=0$ weakly. By elliptic regularity, $u$ is smooth and the PDE holds classically. Since the first nonzero eigenvalue of $-\Delta_{\bar{g}_{\infty}}$ on functions $\mathcal{S} \rightarrow \mathbb{R}$ is strictly larger than $n-1$, we must have $u=0$. But this contradicts the fact that $\|u\|_{L^{2}\left(\bar{g}_{\infty}\right)}=1$. \(\square\)

Proof of Corollary 3.3. Let $\Sigma_{\rho} \subset M$ be a CMC leaf, $g_{\rho}$ and $A_{\rho}$ its induced metric and second fundamental form, and $H$ the mean curvature function as in Theorem 3.2. Let $\Sigma_{\rho, t}$ be the image of $\Sigma_{\rho}$ under the time $t$ flow of $W$, and $H_{\rho, t}$ its mean curvature. By the first variation of mean curvature on a CMC hypersurface in a Ricci-flat manifold (e.g. [35, p. 32]), we have at each point on $\Sigma_{\rho}$
$$\left.\frac{d}{d t}\right|_{t=0} H_{\rho, t}=-\Delta_{g_{\rho}}\langle W, \nu\rangle-\left|A_{\rho}\right|^{2}\langle W, \nu\rangle$$
where $\nu=-\frac{\nabla H}{|\nabla H|}$ is the outward unit normal to $\Sigma_{\rho}$. But $W$ is a Killing field, so $H_{\rho, t}=\frac{n-1}{\rho}$ for all $t$. Combining with (3.3) yields
$$\Delta_{g_{\rho}}\langle W, \nu\rangle+\left|A_{\rho}\right|^{2}\langle W, \nu\rangle=0 .$$
Multiplying both sides of this equation by $\rho^{2}$ gives
$$\Delta_{\rho^{-2} g_{\rho}}\langle W, \nu\rangle+\rho^{2}\left|A_{\rho}\right|_{g}^{2}\langle W, \nu\rangle=0 .$$

By Lemma 3.4, $\rho^{-2} g_{\rho} \rightarrow \bar{g}_{\infty}$ and $\rho^{2}\left|A_{\rho}\right|_{g}^{2} \rightarrow n-1$ smoothly as $\rho \rightarrow \infty$. Then by Lemma $3.5,\langle W, \nu\rangle \equiv 0$ and hence $\langle W, \nabla H\rangle=0$ whenever $\rho$ is sufficiently large. This establishes the first claim in the corollary.

Next, we recall a general identity for vector fields $X$ and $Y$ :
$$\mathcal{L}_{X}\left(Y^{b}\right)=\left(\mathcal{L}_{X} Y\right)^{b}+\left(\mathcal{L}_{X} g\right)(Y, \cdot) .$$
Applying this with $X=W$ and $Y=\nabla H$ gives
$$[W, \nabla H]=\mathcal{L}_{W}(\nabla H)=\left(\mathcal{L}_{W} d H\right)^{\sharp}=\left(d \mathcal{L}_{W} H\right)^{\sharp}=(d\langle W, \nabla H\rangle)^{\sharp}=0,$$
which completes the proof. \(\square\)
3.2. Finding global Killing fields. For the rest of this section, let $\left(M^{n}, g\right)$ be a complete Ricci-flat ALE space of dimension $n \geq 4$ with group at infinity $\Gamma \neq\{1\}$. Write $\mathcal{S}=\mathbb{S}^{n-1} / \Gamma$, and $\bar{g}_{\infty}$ for the round metric on $\mathcal{S}$ with constant sectional curvature 1. Using Theorem 3.1, we fix a diffeomorphism $\Phi: M \backslash K \rightarrow\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma$ such that for each $k \geq 0$,
$$\left|\nabla^{k}\left(\Phi^{*} \bar{g}-g\right)\right|_{g} \leq \mathcal{O}\left(r^{-n-k}\right),$$
where $\bar{g}$ is the Euclidean metric on $\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma$. Given a vector field $\bar{U}$ on $\mathcal{S}$, we can radially extend it to a linearly growing vector field on $\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma$ also denoted by $\bar{U}$. We will say that a vector field $U$ on $M$ extends $\bar{U}$ if $\Phi_{*} U=\bar{U}$ on $\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma$.

Proposition 3.6. Let $\bar{U}$ be a Killing field on $\left(\mathcal{S}, \bar{g}_{\infty}\right)$, and let $U$ be a smooth vector field on $M$ which extends $\bar{U}$. Then there exist a smooth vector field $W$ on $M$ and $\varepsilon \in\left(0, \frac{1}{2}\right)$ such that
$$\begin{aligned}
\Delta W & =0, \\
\left|\nabla^{k}(W-U)\right| & \leq \mathcal{O}\left(r^{-n+2+\varepsilon-k}\right) \text { for each } k \geq 0, \\
\left|\nabla^{k} W\right| & \leq \mathcal{O}\left(r^{1-k}\right) \text { for each } k \geq 0, \\
\left|\mathcal{L}_{W} g\right| & \leq \mathcal{O}\left(r^{-n+1+\varepsilon}\right) .
\end{aligned}$$
Proof. Let $h=\Phi^{*} \bar{g}-g$. The vector field $\bar{U}$ on $\left(\mathbb{R}^{n} \backslash B_{R}(0)\right) / \Gamma$ satisfies $\left|\bar{\nabla}^{k} \bar{U}\right|_{\bar{g}} \leq \mathcal{O}\left(r^{1-k}\right)$ for each $k \geq 0$, where ∇ is the Euclidean derivative. Using (3.4), one can deduce
$$\left|\nabla^{k} U\right| \leq \mathcal{O}\left(r^{1-k}\right) .$$
Using (3.4) and (3.9), we also have on $M \backslash K$ that
$$\left|\nabla^{k} \mathcal{L}_{U} g\right|=\left|\nabla^{k} \mathcal{L}_{U} h\right|=\left|\nabla^{k}(\nabla U * h+U * \nabla h)\right| \leq \mathcal{O}\left(r^{-n-k}\right) \text { for each } k \geq 0 .$$
Next, recall the general relation
$$\operatorname{div}\left(\mathcal{L}_{U} g\right)-\frac{1}{2} \nabla\left(\operatorname{tr} \mathcal{L}_{U} g\right)=\Delta U+\operatorname{Ric}(U) .$$
By (3.10) and Ricci-flatness, this implies
$$\left|\nabla^{k} \Delta U\right| \leq C\left|\nabla^{k+1} \mathcal{L}_{U} g\right| \leq \mathcal{O}\left(r^{-n-1-k}\right) \quad \text { for all } k \geq 0 .$$
For $k \geq 0, \alpha \in(0,1)$, and $\beta \in \mathbb{R}$, let $C_{\beta}^{k, \alpha}$ be the weighted Hölder space of vector fields $X$ on $M$ such that
$$\|X\|_{C_{\beta}^{k, \alpha}}:=\sum_{j=0}^{k}\left(\sup _{x \in M} r(x)^{j-\beta}\left|\nabla^{j} X(x)\right|\right)+\sup _{x \in M} r(x)^{k+\alpha-\beta}\left[\nabla^{k} X\right]_{C^{\alpha}\left(B_{r(x) / 2}(x)\right)}$$
is finite. By standard elliptic theory on ALE spaces (see for instance [32, §4.1]), we have that for all $k \in \mathbb{N}_{0}, \alpha \in(0,1)$, and all $\beta \in \mathbb{R}$ outside some discrete set $\mathcal{D} \subset \mathbb{R}$,
$$\Delta: C_{\beta+2}^{k+2, \alpha} \rightarrow C_{\beta}^{k, \alpha}$$
is Fredholm with image
$$\left\{Y \in C_{\beta}^{k, \alpha}: \int_{M}\langle Y, X\rangle=0 \text { for all } X \in \mathcal{H}_{-\beta-n}\right\},$$
where $\mathcal{H}_{-\beta-n}$ is the space of harmonic vector fields in $C_{-\beta-n}^{\ell, \alpha}$ for arbitrary $\ell$. We let $\beta=-n+\varepsilon$, where $\varepsilon \in\left(0, \frac{1}{2}\right)$ is chosen so that $\beta \notin \mathcal{D}$. Then any $X \in \mathcal{H}_{-\beta-n}$ satisfies $|X| \leq \mathcal{O}\left(r^{-\varepsilon}\right)$ and is therefore in $L^{p}$ for some $p \in(1, \infty)$. By [31, Proposition 4.3], this promotes to $|X| \leq \mathcal{O}\left(r^{-n+1}\right)$. Thus $X$ is an $L^{2}$ harmonic vector field, which must be zero by the Bochner formula and an integration-by-parts argument. Hence, (3.12) is surjective for $\beta=-n+\varepsilon$.

By (3.11), we have $-\Delta U \in C_{-n+\varepsilon}^{k, \alpha}$ for all $k \geq 0$ and $\alpha \in(0,1)$. Hence there is a vector field $\hat{U} \in C_{-n+2+\varepsilon}^{2, \alpha}$ such that
$$\Delta \hat{U}=-\Delta U .$$
Standard weighted elliptic estimates yield $\hat{U} \in C_{-n+2+\varepsilon}^{k+2, \alpha}$ for all $k \geq 0$. So $W:=U+\hat{U}$ satisfies (3.5) and (3.6). Combining with (3.9) and (3.10), we obtain (3.7) and (3.8) respectively. \(\square\)

Recall that the Lichnerowicz Laplacian $\Delta_{L}$ is defined by (1.2) on a Ricci-flat space. The following identity is well-known: see for instance [11, Theorem 4.1] (taking $X=0$ there).

Lemma 3.7. On a Ricci-flat space $(M, g)$, if $W$ is a vector field satisfying $\Delta W=0$, then $\Delta_{L}\left(\mathcal{L}_{W} g\right)=0$.

Next, we show that a dimension bound on $\operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ implies the existence of Killing fields on $(M, g)$. This is a direct analog of [34, Proposition 3.8] for Ricci-flat ALE spaces. Recall that $\mathcal{I}(M, g)$ denotes the isometry group of $(M, g), \mathcal{I}^{0}(M, g)$ is its identity component, and $\mathfrak{I}(M, g)$ is its Lie algebra (i.e. the Lie algebra of Killing fields). Define $\bar{d}=\operatorname{dim} \mathcal{I}\left(\mathcal{S}, \bar{g}_{\infty}\right)$.

Proposition 3.8. Suppose $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \leq d$ for some nonnegative integer $d$. Then there exists a $(\bar{d}-d)$-dimensional vector space $\mathcal{V}$ of Killing fields on $(M, g)$ such that for each $W \in \mathcal{V}$,
\begin{itemize}
\item[(a)] $[W, \nabla H]=0$.
\item[(b)] $\langle W, \nabla H\rangle=0$, i.e. $W$ is tangent to the $C M C$ leaves.
\item[(c)] $W$ is a Killing field for $(M, g)$ and for each sufficiently far CMC leaf.
\item[(d)] $\left|\nabla^{k} W\right| \leq \mathcal{O}\left(r^{1-k}\right)$ for each $k \geq 0$.
\item[(e)] There exists a unique Killing field $\bar{U}$ on $\left(\mathcal{S}, \bar{g}_{\infty}\right)$ such that if $U$ is a smooth vector field on $M$ which extends $\bar{U}$, then $\left|\nabla^{k}(W-U)\right| \leq \mathcal{O}\left(r^{-n+2+\varepsilon-k}\right)$ for each $k \geq 0$. The map $\mathcal{V} \rightarrow \mathfrak{I}\left(\mathcal{S}, \bar{g}_{\infty}\right), W \mapsto \bar{U}$ is linear and injective.
\end{itemize}

Proof. Let $\left\{\bar{U}_{i}\right\}_{i=1}^{\bar{d}}$ be a basis for $\mathfrak{I}\left(\mathcal{S}, \bar{g}_{\infty}\right)$, and let $\left\{U_{i}\right\}_{i=1}^{\bar{d}}$ be smooth vector fields on $M$ which extend $\bar{U}_{i}$. Proposition 3.6 gives vector fields $\left\{W_{i}\right\}_{i=1}^{d}$ and $\varepsilon \in\left(0, \frac{1}{2}\right)$ such that
$$\begin{aligned}
\Delta W_{i} & =0, \\
\left|\nabla^{k}\left(W_{i}-U_{i}\right)\right| & \leq \mathcal{O}\left(r^{-n+2+\varepsilon-k}\right) \text { for each } k \geq 0, \\
\left|\nabla^{k} W_{i}\right| & \leq \mathcal{O}\left(r^{1-k}\right) \text { for each } k \geq 0, \\
\left|\mathcal{L}_{W_{i}} g\right| & \leq \mathcal{O}\left(r^{-n+1+\varepsilon}\right) .
\end{aligned}$$

By (3.13), the decay (3.16), and Lemma 3.7, we have $\mathcal{L}_{W_{i}} g \in \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$. Since the vector fields $U_{i}$ are linearly independent, (3.14) implies that the vector fields $W_{i}$ are linearly independent too.

Let $\mathcal{V}^{\prime}=\operatorname{span}\left\{W_{i}\right\}_{i=1}^{\bar{d}}$, so that $\operatorname{dim} \mathcal{V}^{\prime}=\bar{d}$ by the linear independence. Define a map $\mathcal{R}: \mathcal{V}^{\prime} \rightarrow \mathfrak{I}\left(\mathcal{S}, \bar{g}_{\infty}\right)$ by sending $W_{i}$ to $\bar{U}_{i}$ and extending linearly. This map is clearly injective. Also define a map $\mathcal{T}: \mathcal{V}^{\prime} \rightarrow \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right)$ by $W \mapsto \mathcal{L}_{W} g$.

The assumption $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \leq d$ implies $\operatorname{dim} \operatorname{ker} \mathcal{T} \geq \bar{d}-d$. Let $\mathcal{V}=\operatorname{ker} \mathcal{T}$. Then every $W \in \mathcal{V}$ is a Killing field for $(M, g)$. Combined with Corollary 3.3, this proves (a), (b), and (c). Part (d) follows from (3.15). Part (e) follows from restricting the map $\mathcal{R}: \mathcal{V}^{\prime} \rightarrow \mathfrak{I}\left(\mathcal{S}, \bar{g}_{\infty}\right)$ to $\mathcal{V}$, and applying (3.14). \(\square\)

For all large $\rho>0$, let $\Sigma_{\rho} \subset M$ be the CMC leaf with mean curvature $H=\frac{n-1}{\rho}$. Using Theorem 3.2(b), we identify $\Sigma_{\rho}$ with a Riemannian manifold $\left(\mathcal{S}, g_{\rho}\right)$. We set up the following:
\begin{itemize}
\item[-] Let $\mathcal{V}_{\rho}$ be the restriction of Killing fields in $\mathcal{V}$ to $\Sigma_{\rho}$. By Proposition 3.8, $\mathcal{V}_{\rho} \subset \mathfrak{I}\left(\mathcal{S}, g_{\rho}\right)$.
\item[-] Let $\mathfrak{g}$ be the Lie subalgebra of $\mathfrak{I}(M, g)$ generated by $\mathcal{V}$, and let $G$ be the unique connected Lie subgroup of $\mathcal{I}^{0}(M, g)$ generated by $\mathfrak{g}$.
\item[-] Likewise, let $\mathfrak{g}_{\rho}$ be the Lie subalgebra of $\mathfrak{I}\left(\mathcal{S}, g_{\rho}\right)$ generated by $\mathcal{V}_{\rho}$, and let $G_{\rho}$ be the unique connected Lie subgroup of $\mathcal{I}^{0}\left(\mathcal{S}, g_{\rho}\right)$ generated by $\mathfrak{g}_{\rho}$.
\end{itemize}

The next corollary immediately follows from Corollary 3.3.
Corollary 3.9. For any $X \in \mathfrak{g}$, we have $[X, \nabla H]=0$ and $\langle X, \nabla H\rangle=0$.
With the help of Corollary 3.9, the following assertions are proved in exactly the same manner as [34, Lemma 3.19]. Thus we omit the details.

Lemma 3.10. (a) The restriction map $\mathcal{V} \rightarrow \mathcal{V}_{\rho}$ is a linear isomorphism.
\begin{itemize}
\item[(b)] The restriction map $\mathfrak{g} \rightarrow \mathfrak{g}_{\rho}$ is a Lie algebra isomorphism.
\item[(c)] If $G_{\rho}$ is closed in $\mathcal{I}\left(\mathcal{S}, g_{\rho}\right)$, then $G$ is a compact Lie group acting smoothly and isometrically on $(M, g)$, and the restriction map $G \rightarrow G_{\rho}$ is a Lie group isomorphism.
\end{itemize}

In the case where $\left(\mathcal{S}, \bar{g}_{\infty}\right)$ is homogeneous, i.e. its isometry group acts transitively, the space of Killing fields $\mathfrak{I}\left(\mathcal{S}, \bar{g}_{\infty}\right)$ spans the tangent space to $\mathcal{S}$ at each point. We define the quantity $d_{1}\left(\mathcal{S}, \bar{g}_{\infty}\right) \geq 0$ to be the largest integer $d$ such that
\begin{itemize}
\item[-] Any Lie subalgebra of $\mathfrak{I}\left(\mathcal{S}, \bar{g}_{\infty}\right)$ with dimension $\geq \bar{d}-d$ spans the tangent space to $\mathcal{S}$ at every point.
\end{itemize}

Lemma 3.11. If $\left(\mathcal{S}, \bar{g}_{\infty}\right)$ is homogeneous and $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \leq d_{1}\left(\mathcal{S}, \bar{g}_{\infty}\right)$, then $\mathfrak{g}_{\rho}$ spans the tangent space to $\Sigma_{\rho}$ at every point for all sufficiently large $\rho$.

Proof. Proposition 3.8 gives a $\left(\bar{d}-d_{1}\left(\mathcal{S}, \bar{g}_{\infty}\right)\right)$-dimensional space $\mathcal{V}$ of Killing fields on $(M, g)$. Take a basis $\left\{W_{i}\right\}_{i=1, \ldots, \bar{d}-d_{1}\left(\mathcal{S}, \bar{g}_{\infty}\right)}$ for $\mathcal{V}$, let $\bar{U}_{i}$ be the corresponding vector fields from Proposition 3.8(e), and let $U_{i}$ be arbitrary extensions thereof. Since the map $\mathcal{V} \rightarrow \mathfrak{I}\left(\mathcal{S}, \bar{g}_{\infty}\right)$, $W_{i} \mapsto \bar{U}_{i}$ is linear and injective, it follows that the $U_{i}$ are linearly independent.

Write $X_{i}=W_{i}-U_{i}$. From Propositions 3.6 and 3.8, we have
$$\left|\nabla^{k} W_{i}\right| \leq \mathcal{O}\left(r^{1-k}\right), \quad\left|\nabla^{k} X_{i}\right| \leq \mathcal{O}\left(r^{-n+2+\varepsilon-k}\right), \quad\left|\nabla^{k} U_{i}\right| \leq \mathcal{O}\left(r^{1-k}\right)$$
for each $k \geq 0$. The rest is then identical to [34, Lemma 3.21], so we omit the details. \(\square\)

The next proposition elucidates the global structure of $(M, g)$ if it admits an isometric action of cohomogeneity one. It is an orbifold version of [34, Proposition 3.22], which follows from the work of Mostert [39] in the setting of smooth manifolds and González Álvaro for smooth orbifolds [23].

Proposition 3.12. Suppose there is a compact, connected Lie group $G$ acting smoothly, almost effectively, and isometrically with cohomogeneity one on $(M, g)$. Denote the projection map by $\pi: M \rightarrow M / G$. Then:
\begin{itemize}
\item[(a)] The orbit space $M / G$ is homeomorphic to [0,1).
\item[(b)] There is a closed subgroup $H$ of $G$ such that the principal orbits, i.e. $\pi^{-1}(s)$ for any $s>0$, are diffeomorphic to $\mathcal{S} \cong G / H$. Thus, each point in a principal orbit has isotropy subgroup $H$.
\item[(c)] The singular orbit $X=\pi^{-1}(0)$ is diffeomorphic to $G / K$, where $K$ is a closed subgroup of $G$ such that $H \subsetneq K$ and $K / H \cong \mathcal{S}^{\prime}$ for some spherical space form $\mathcal{S}^{\prime}$ of dimension $\ell \geq 0$.
\item[(d)] $M$ is diffeomorphic to the orbifiber bundle $E=G \times_{K} \operatorname{Cone}\left(\mathcal{S}^{\prime}\right)$ over $G / K \cong X$, where $K$ acts via $k \cdot(g, v)=\left(g k^{-1}, k v\right)$, and $k v$ is the radial extension of the action of $K$ on $K / H \cong \mathcal{S}^{\prime}$.
\item[(e)] Every sphere bundle of $E$ is diffeomorphic to $\mathcal{S}$. Thus $M \backslash X$ is diffeomorphic to $(0, \infty) \times \mathcal{S}$, and under this identification the metric $g$ becomes
$$g=d s^{2}+g(s),$$
where $\{g(s)\}_{s>0}$ is a smooth family of $G$-invariant metrics on $G / H \cong \mathcal{S}$.
\end{itemize}

\section*{4. A characterization of Eguchi-Hanson space}

In this section, we prove Theorem 1.2. Before proceeding, we require some preparations regarding metrics on $\mathbb{S}^{3}$ and $\mathbb{R P}^{3}$ with large isometry groups.
4.1. Metrics on $\mathbb{S}^{3}$ and $\mathbb{R P}^{3}$ with large isometry groups. Below, we will identify $\mathbb{S}^{3}$ as the multiplicative group $S U(2)$ of unit quaternions
$$\mathbb{S}^{3} \cong S U(2)=\left\{a+b \mathbf{i}+c \mathbf{j}+d \mathbf{k} \in \mathbb{H}: a^{2}+b^{2}+c^{2}+d^{2}=1\right\} .$$
Any left-invariant metric $g$ on $S U(2)$ is of the form
$$\tilde{g}=\lambda^{2} \sigma_{1} \otimes \sigma_{1}+\mu^{2} \sigma_{2} \otimes \sigma_{2}+\nu^{2} \sigma_{3} \otimes \sigma_{3},$$
where $\lambda, \mu, \nu>0$ are constants, and $\left\{\sigma_{1}, \sigma_{2}, \sigma_{3}\right\}$ is dual to a left-invariant frame $\left\{X_{1}, X_{2}, X_{3}\right\}$. We may assume $X_{1}=\mathbf{i}, X_{2}=\mathbf{j}, X_{3}=\mathbf{k}$ in $T_{1} S U(2)=\mathfrak{s u}(2)$. If $\lambda=\mu=\nu$, then $\tilde{g}$ is a round metric. If exactly two coefficients are equal, then we call $\tilde{g}$ a Berger metric. If all three coefficients are different, then we call $\tilde{g}$ a generic left-invariant metric. The corresponding isometry groups are well-known and are stated in the next lemma.

Lemma 4.1. Let $\tilde{g}$ be a homogeneous metric on $\mathbb{S}^{3}$. Then $\tilde{g}$ is a left-invariant metric (4.1) on $\operatorname{SU}(2)$ [45, Theorem C]. The isometry group $\mathcal{I}(S U(2), \tilde{g})$ is given as follows:
\begin{itemize}
\item[(a)] If $\tilde{g}$ is a round metric $(\lambda=\mu=\nu)$, then $\mathcal{I}(S U(2), \tilde{g})$ is generated by left multiplications in SU(2), right multiplications in SU(2), and inversion $q \mapsto q^{-1}$ in SU(2). Thus,
$$\mathcal{I}(S U(2), \tilde{g})=\left(S U(2)_{L} \times_{\mathbb{Z}_{2}} S U(2)_{R}\right) \rtimes \mathbb{Z}_{2} \cong S O(4) \rtimes \mathbb{Z}_{2} \cong O(4) .$$
\item[(b)] If $\tilde{g}$ is a Berger metric (without loss of generality we assume $\lambda \neq \mu=\nu$ ), then $\mathcal{I}(S U(2), \tilde{g})$ is generated by left multiplications in $S U(2)$, right multiplications by $e^{\mathbf{i} \theta}$ $(\theta \in[0,2 \pi))$, and the map $q \mapsto \mathbf{j}^{-1} q \mathbf{j}$. Thus,
$$\mathcal{I}(S U(2), \tilde{g})=\left(S U(2)_{L} \times_{\mathbb{Z}_{2}} U(1)_{R}\right) \rtimes \mathbb{Z}_{2} \cong U(2) \rtimes \mathbb{Z}_{2} .$$
\end{itemize}
\begin{itemize}
\item[(c)] If $\tilde{g}$ is a generic left-invariant metric, then $\mathcal{I}(S U(2), \tilde{g})$ is generated by left multiplications in $S U(2)$, the map $q \mapsto \mathbf{i}^{-1} q \mathbf{i}$, and the map $q \mapsto \mathbf{j}^{-1} q \mathbf{j}$. Thus,
$$\mathcal{I}(S U(2), \tilde{g})=S U(2)_{L} \rtimes\left(\mathbb{Z}_{2}\right)^{2} .$$
\end{itemize}

Lemma 4.1 leads to a classification of homogeneous metrics on $\mathbb{R P}^{3}$ :
Corollary 4.2. If $g$ is a homogeneous metric on $\mathbb{R P}^{3}$, then $g$ is isometric to the quotient of a homogeneous metric $\tilde{g}$ on $S U(2)$ by the map $q \mapsto-q$. We have $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)=\mathcal{I}^{0}(S U(2), \tilde{g}) / \mathbb{Z}_{2}$.

Proof. Let $g$ be as in the corollary. Then the universal cover $(S U(2), \tilde{g})$ is homogeneous, and there is an embedding $\iota: \mathbb{Z}_{2} \hookrightarrow \mathcal{I}(S U(2), \tilde{g})$ such that $\iota\left(\mathbb{Z}_{2}\right)$ acts freely and isometrically on $(S U(2), \tilde{g})$ with quotient isometric to $\left(\mathbb{R} \mathbb{P}^{3}, g\right)$. Note that in each case (a)-(c) of Lemma 4.1, the center of $\mathcal{I}^{0}(S U(2), \tilde{g})$ contains a unique copy of $\mathbb{Z}_{2}$ generated by the antipodal map $q \mapsto-q$. To prove the first part of the corollary, we need to show that $\iota\left(\mathbb{Z}_{2}\right)$ is exactly this central copy of $\mathbb{Z}_{2}$. We do this for cases (b) and (c); case (a) is more direct. The second part of the corollary follows from Lemma 2.2.
(a) If $\tilde{g}$ is round, then so is $g$. Since diffeomorphic spherical space forms are isometric [18], and a round $\mathbb{R P}^{3}$ can be obtained by quotienting (SU(2), $\tilde{g}$ ) by the map $q \mapsto-q$, it follows that $\left(\mathbb{R P}^{3}, g\right)$ is isometric to this quotient.
(b) If $\tilde{g}$ is a Berger metric, then $\mathcal{I}(S U(2), \tilde{g}) \cong U(2) \rtimes \mathbb{Z}_{2}$. By Lemma 2.1 and Lemma 2.2, we have
$$\operatorname{dim} C_{\mathcal{I}(S U(2), \tilde{g})}^{0}\left(\iota\left(\mathbb{Z}_{2}\right)\right)=\operatorname{dim} N_{\mathcal{I}(S U(2), \tilde{g})}^{0}\left(\iota\left(\mathbb{Z}_{2}\right)\right)=\operatorname{dim} \mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right) \geq 3,$$
where the last inequality holds because $g$ is homogeneous. We have $C_{\mathcal{I}(S U(2), \tilde{g})}^{0}\left(\iota\left(\mathbb{Z}_{2}\right)\right) \subset$ $\mathcal{I}^{0}(S U(2), \tilde{g}) \cong U(2)$, so (4.2) implies that $C_{\mathcal{I}(S U(2), \tilde{g})}^{0}\left(\iota\left(\mathbb{Z}_{2}\right)\right)$ is either $S U(2)$ or $U(2)$. Either way, it follows that $\iota\left(\mathbb{Z}_{2}\right) \subset C_{\mathcal{I}(S U(2), \tilde{g})}(S U(2))$. This centralizer is computed to consist of right-multiplications by $e^{\mathbf{i} \theta}$ together with right-multiplications by $\mathbf{j} e^{\mathbf{i} \theta}$. Thus, $C_{\mathcal{I}(S U(2), \tilde{g})}(S U(2)) \cong\left\{e^{\mathbf{i} \theta}\right\} \cup \mathbf{j}\left\{e^{\mathbf{i} \theta}\right\} \cong \operatorname{Pin}(2)$. Since the unique order 2 subgroup of $\operatorname{Pin}(2)$ is contained in its identity component, it follows that $\iota\left(\mathbb{Z}_{2}\right) \subset Z\left(\mathcal{I}^{0}(S U(2), \tilde{g})\right)$, as required.
(c) If $\tilde{g}$ is a generic left-invariant metric, then $\mathcal{I}(S U(2), \tilde{g}) \cong S U(2) \rtimes\left(\mathbb{Z}_{2}\right)^{2}$. The inequality (4.2) still holds, but now it implies $C_{\mathcal{I}(S U(2), \tilde{g})}^{0}\left(\iota\left(\mathbb{Z}_{2}\right)\right)=S U(2)$. Thus,
$$\iota\left(\mathbb{Z}_{2}\right) \subset C_{\mathcal{I}(S U(2), \tilde{g})}(S U(2))=Z(S U(2))=Z\left(\mathcal{I}^{0}(S U(2), \tilde{g})\right),$$
where the first equality is easily checked using Case (c) of Lemma 4.1. \(\square\)

The next lemma follows from Lemma 4.1 together with standard facts about subgroups of $S O(4)$ and $U(2)$.

Lemma 4.3. Let $\tilde{g}$ be a homogeneous metric on $\mathbb{S}^{3}$. For each case below, we list all Lie subalgebras $\mathfrak{g}$ of $\mathfrak{I}\left(\mathbb{S}^{3}, \tilde{g}\right)$ with $\operatorname{dim} \mathfrak{g} \geq 3$, up to conjugacy in $\mathcal{I}^{0}\left(\mathbb{S}^{3}, \tilde{g}\right)$. For each $\mathfrak{g}$, we identify the unique connected Lie subgroup $G$ of $\mathcal{I}^{0}\left(\mathbb{S}^{3}, \tilde{g}\right)$ with Lie algebra $\mathfrak{g}$. This gives a complete list of connected Lie subgroups $G \subseteq \mathcal{I}^{0}\left(\mathbb{S}^{3}, \tilde{g}\right)$ with $\operatorname{dim} G \geq 3$, up to conjugacy. Finally, we determine whether $G$ acts transitively on $\mathbb{S}^{3}$; if so, we identify its isotropy subgroup $H \subseteq G$.
\begin{itemize}
\item[(a)] If $\tilde{g}$ is a round metric, i.e. $\mathcal{I}^{0}\left(\mathbb{S}^{3}, \tilde{g}\right)=S O(4) \cong S U(2)_{L} \times_{\mathbb{Z}_{2}} S U(2)_{R}$ and $\mathfrak{I}\left(\mathbb{S}^{3}, \tilde{g}\right)=$ $\mathfrak{s} \mathfrak{o}(4) \cong \mathfrak{s} \mathfrak{u}(2)_{L} \oplus \mathfrak{s} \mathfrak{u}(2)_{R}$, then the possibilities are shown in Table 1.
\item[(b)] If $\tilde{g}$ is a Berger metric, i.e. $\mathcal{I}^{0}\left(\mathbb{S}^{3}, \tilde{g}\right)=U(2)$ and $\mathfrak{I}\left(\mathbb{S}^{3}, \tilde{g}\right)=\mathfrak{u}(2)$, then the possibilities are shown in Table 2.
\item[(c)] If $\tilde{g}$ is a generic left-invariant metric, i.e. $\mathcal{I}^{0}\left(\mathbb{S}^{3}, \tilde{g}\right)=S U(2)$ and $\mathfrak{I}\left(\mathbb{S}^{3}, \tilde{g}\right)=\mathfrak{s} \mathfrak{u}(2)$, then the only possibility is $\mathfrak{g}=\mathfrak{s u}(2)$ and $G=S U(2)$. In this case, $G$ acts transitively on $\mathbb{S}^{3}$ with trivial isotropy subgroup $H$.
\end{itemize}

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline $\mathfrak{g}$ & $G$ & $H$ (if $G$ transitive) \\
\hline $\mathfrak{s} \mathfrak{o}(4)$ & $S O(4)$ & $S O(3)$ \\
\hline $\mathfrak{s} \mathfrak{u}(2)_{L} \oplus \mathfrak{u}(1)_{R}$ & $S U(2)_{L} \times_{\mathbb{Z}_{2}} U(1)_{R} \cong U(2)$ & $\operatorname{diag}(U(1)) / \mathbb{Z}_{2} \cong U(1)$ \\
\hline $\mathfrak{u}(1)_{L} \oplus \mathfrak{s} \mathfrak{u}(2)_{R}$ & $U(1)_{L} \times_{\mathbb{Z}_{2}} S U(2)_{R} \cong U(2)$ & $\operatorname{diag}(U(1)) / \mathbb{Z}_{2} \cong U(1)$ \\
\hline $\mathfrak{s} \mathfrak{u}(2)_{L}$ & $S U(2)_{L}$ & \{1\} \\
\hline $\mathfrak{s} \mathfrak{u}(2)_{R}$ & $S U(2)_{R}$ & \{1\} \\
\hline $\operatorname{diag}(\mathfrak{s u}(2))$ & $\operatorname{diag}(S U(2)) / \mathbb{Z}_{2} \cong S O(3)$ & $G$ not transitive* \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{* In this case, $G$ acts by rotations of $\mathbb{S}^{3} \subset \mathbb{R}^{4}$ that fix an axis.}
\end{table}

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1. Possibilities for $\mathfrak{g}, G$, and $H$ if $\tilde{g}$ is a round metric.}
\begin{tabular}[t]{|l|l|l|}
\hline $\mathfrak{g}$ & $G$ & $H$ (if $G$ transitive) \\
\hline $\mathfrak{u}(2)$ & $U(2)$ & $U(1)$ \\
\hline $\mathfrak{s} \mathfrak{u}(2)$ & $S U(2)$ & \{1\} \\
\hline
\end{tabular}
\end{table}

Table 2. Possibilities for $\mathfrak{g}, G$, and $H$ if $\tilde{g}$ is a Berger metric.

Corollary 4.4. Using Corollary 4.2, we immediately obtain an analog of Lemma 4.3 for homogeneous metrics $g$ on $\mathbb{R P}^{3}$ :
\begin{itemize}
\item[(a)] In each case for $g$ (round, Berger, generic left-invariant), we can classify all Lie subalgebras $\mathfrak{g}$ of $\mathfrak{I}\left(\mathbb{R P}^{3}, g\right)$ with $\operatorname{dim} \mathfrak{g} \geq 3$ up to conjugacy in $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)$. The list is exactly the same as that given in Lemma 4.3.
\item[(b)] For each $\mathfrak{g}$, we can identify the unique connected Lie subgroup $G \subset \mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)$. These are simply the $G$ 's from Lemma 4.3 quotiented by central $\mathbb{Z}_{2}$ 's. This gives a complete list of connected Lie subgroups $G \subseteq \mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)$ with $\operatorname{dim} G \geq 3$, up to conjugacy.
\item[(c)] All $G$ 's act transitively on $\mathbb{R P}^{3}$, except for $G$ coming from the last row of Table 1. For the transitive $G$ 's, the isotropy subgroup $H$ is the image of the corresponding isotropy subgroup from Lemma 4.3 under the quotient map $G \rightarrow G / \mathbb{Z}_{2}$ from the previous point.
\end{itemize}

Corollary 4.5. Let $g$ be a homogeneous metric on $\mathbb{R P}^{3}$ with $\operatorname{dim} \mathcal{I}\left(\mathbb{R P}^{3}, g\right) \geq 4$. Then any Lie subgroup $G \subseteq \mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)$ with $\operatorname{dim} G \geq 4$ must act transitively.

Proof. By Corollary 4.2, $g$ must be the standard $\mathbb{Z}_{2}$-quotient of a homogeneous metric $\tilde{g}$ on $\mathbb{S}^{3}$. Since $\operatorname{dim} \mathcal{I}\left(\mathbb{R P}^{3}, g\right) \geq 4$, we have $\operatorname{dim} \mathcal{I}\left(\mathbb{S}^{3}, \tilde{g}\right) \geq 4$ as well. Thus, by Lemma 4.1, $\tilde{g}$ is either a round metric or a Berger metric.
\begin{itemize}
\item[-] If $\tilde{g}$ is round, then $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)=S O(4) / \mathbb{Z}_{2}$. By Corollary 4.4, any Lie subalgebra of $\mathfrak{I}\left(\mathbb{R P}^{3}, g\right)=\mathfrak{s o}(4)$ with dimension at least 4 must be $\mathfrak{s o}(4), \mathfrak{s u}(2)_{L} \oplus \mathfrak{u}(1)_{R}$, or $\mathfrak{u}(1)_{L} \oplus \mathfrak{s} \mathfrak{u}(2)_{R}$. In the first case, the Killing fields clearly span the tangent space everywhere, so $G$ acts transitively. In the second (resp. third) case, the corresponding subalgebra of Killing fields contains those generating left (resp. right) multiplication in $S U(2)$, so they also span the tangent space at every point.
\item[-] If $\tilde{g}$ is a Berger metric, then $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)=U(2) / \mathbb{Z}_{2}$, which has dimension 4. Thus, $G=\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)$, which acts transitively.
\end{itemize} \(\square\)

Corollary 4.6. If $g$ is a metric on $\mathbb{R P}^{3}$ with $\operatorname{dim} \mathcal{I}\left(\mathbb{R P}^{3}, g\right) \geq 3$, then every connected Lie subgroup $G$ of $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)$ with dimension $\geq 3$ is compact.

Proof. If $\operatorname{dim} \mathcal{I}\left(\mathbb{R P}^{3}, g\right)=3$ this is trivial, so we assume $\operatorname{dim} \mathcal{I}\left(\mathbb{R P}^{3}, g\right) \geq 4$. It is well-known that this implies $g$ is homogeneous [29, p. 48-49]. Corollary 4.4(b) classifies all connected Lie subgroups $G$ of $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g\right)$ with $\operatorname{dim} G \geq 3$. It is clear that each $G$ is compact. \(\square\)
4.2. Proof of Theorem 1.2: dividing into cases. For the rest of §4, $\left(M^{4}, g\right)$ is a complete 4-dimensional Ricci-flat ALE space with finitely many orbifold points and group at infinity $\mathbb{Z}_{2}$. Moreover, we assume that $\operatorname{dim} \operatorname{ker}_{L^{2}}\left(\Delta_{L}\right) \leq 3$. We now proceed to prove Theorem 1.2.

By Proposition 3.8 and the setup before Corollary 3.9, there is a Lie subalgebra $\mathfrak{g}$ of Killing fields on $(M, g)$ with $\operatorname{dim} \mathfrak{g} \geq 6-3=3$, which for large $\rho$ restricts to a Lie algebra $\mathfrak{g}_{\rho}$ of Killing fields on the CMC leaves $\left(\mathbb{R P}^{3}, g_{\rho}\right)$. These Lie algebras integrate to connected Lie groups $G \subseteq \mathcal{I}^{0}(M, g)$ and $G_{\rho} \subseteq \mathcal{I}^{0}\left(\mathbb{R P}^{3}, g_{\rho}\right)$ of dimension $\geq 3$.

By Corollary 4.6, $G_{\rho}$ is compact. By Lemma 3.10, $G$ acts smoothly, isometrically, and effectively on $(M, g)$, and the restriction map $G \rightarrow G_{\rho}$ is an isomorphism. In particular, $G_{\rho}$ for all large $\rho$ (say $\rho \geq R_{0}$ ) are isomorphic. Consider two cases:
\begin{itemize}
\item[(A)] $G$ acts transitively on $\left(\mathbb{R P}^{3}, g_{\rho}\right)$ for some $\rho \geq R_{0}$.
\item[(B)] $G$ does not act transitively on $\left(\mathbb{R P}^{3}, g_{\rho}\right)$ for all $\rho \geq R_{0}$.
\end{itemize}

In §4.3, we will show that Case (A) implies $(M, g)$ is either the Eguchi-Hanson space or the flat orbifold $\mathbb{R}^{4} / \mathbb{Z}_{2}$. In §4.4, we will show that Case (B) necessarily leads to ( $M, g$ ) being the flat $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Altogether, this will prove Theorem 1.2.
4.3. Case (A). In this subsection, we assume $G$ acts transitively on $\left(\mathbb{R P}^{3}, g_{\rho}\right)$, so $g_{\rho}$ is homogeneous. We will show that $(M, g)$ is either Eguchi-Hanson space or the flat $\mathbb{R}^{4} / \mathbb{Z}_{2}$.

Corollary 4.2 determines all possibilities for $g_{\rho}$ and $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g_{\rho}\right)$. Based on this, Corollary 4.4 allows us to classify $G$ (up to isomorphism) and the isotropy subgroup $H$. Table 3 lists all possibilities.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $g_{\rho}$ & $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g_{\rho}\right)$ & $G$ & $H$ \\
\hline \multirow{3}{*}{Round} & \multirow{3}{*}{$S O(4) / \mathbb{Z}_{2}$} & $S O(4) / \mathbb{Z}_{2}$ & $S O(3)$ \\
\hline & & $U(2) / \mathbb{Z}_{2}$ & $U(1)$ \\
\hline & & $S U(2) / \mathbb{Z}_{2}$ & \{1\} \\
\hline \multirow{2}{*}{Berger} & \multirow[t]{2}{*}{$U(2) / \mathbb{Z}_{2}$} & $U(2) / \mathbb{Z}_{2}$ & $U(1)$ \\
\hline & & $S U(2) / \mathbb{Z}_{2}$ & \{1\} \\
\hline Generic left-invariant & $S U(2) / \mathbb{Z}_{2}$ & $S U(2) / \mathbb{Z}_{2}$ & \{1\} \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 3. All possibilities for $g_{\rho}, \mathcal{I}^{0}\left(\mathbb{R P}^{3}, g_{\rho}\right), G, H$ in Case (A).}
\end{table}

By assumption, there exists a pair $(G, H)$ from Table 3 such that $G$ acts smoothly, effectively, and isometrically on $(M, g)$ with cohomogeneity one and principal isotropy $H$. To simplify things, we will modify $G$ and $H$ by using their preimages under the $\mathbb{Z}_{2}$-quotients. Thus, for some pair $(G, H)$ in Table 4, $G$ acts smoothly, almost effectively, and isometrically with cohomogeneity one on $(M, g)$ and principal isotropy $H$.

By Proposition 3.12, it holds that for some $(G, H)$ from Table 4,
\begin{itemize}
\item[(i)] Outside a submanifold $X$, we can identify
$$(M \backslash X, g)=\left((0, \infty) \times G / H, d s^{2}+g(s)\right)$$
where $\{g(s)\}_{s>0}$ are $G$-invariant metrics on a fixed copy of $G / H \cong \mathbb{R P}^{3}$.
\item[(ii)] There is a closed subgroup $K$ of $G$ strictly containing $H$ such that $X$ is diffeomorphic to $G / K$, and $K / H$ is diffeomorphic to a spherical space form of dimension $\ell \geq 0$.
\end{itemize}

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline $G$ & $H$ \\
\hline $S O(4)$ & $O(3)$ \\
\hline $U(2)$ & $U(1) \times \mathbb{Z}_{2}$ \\
\hline $S U(2)$ & $\mathbb{Z}_{2}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 4. In Case (A), some $G$ here acts smoothly, almost effectively, and isometrically with cohomogeneity one on $(M, g)$ and principal isotropy $H$.}
\end{table}
\begin{itemize}
\item[(iii)] From the description of $(M, g)$ as a bundle over $X$, the metric spaces $(G / H, g(s))$ converge in the Hausdorff sense to $X$ as $s \rightarrow 0$.
\end{itemize}

We will use (ii) and (iii) with the following lemma, which follows from standard facts about closed subgroups of $S O(4), U(2)$, and $S U(2)$. Below, $L(4,1)$ is the lens space obtained by quotienting $\mathbb{S}^{3}$ by a Hopf action of $\mathbb{Z}_{4}$.

Lemma 4.7. For each $(G, H)$ in Table 4, we indicate in Table 5 all closed subgroups $K$ of $G$ such that (i) $K$ strictly contains $H$, and (ii) $K / H$ is diffeomorphic to a spherical space form of dimension $\ell \geq 0$. We also indicate the diffeomorphism type of $G / K$.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $G$ & $H$ & $K$ & $G / K$ \\
\hline $S O(4)$ & $O(3)$ & $S O(4)$ & \{point\} \\
\hline \multirow{3}{*}{$U(2)$} & \multirow{3}{*}{$U(1) \times \mathbb{Z}_{2}$} & $U(1) \times \mathbb{Z}_{4}$ & $L(4,1)$ \\
\hline & & $U(1) \times U(1)$ & $\mathbb{S}^{2}$ \\
\hline & & $U(2)$ & \{point\} \\
\hline \multirow{3}{*}{$S U(2)$} & \multirow{3}{*}{$\mathbb{Z}_{2}$} & $\mathbb{Z}_{4}$ & $L(4,1)$ \\
\hline & & $U(1)$ & $\mathbb{S}^{2}$ \\
\hline & & $S U(2)$ & \{point\} \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 5. Results for Lemma 4.7.}
\end{table}

Since the metrics $g(s)$ are homogeneous, Corollary 4.2 implies that $g(s)$ is the $\mathbb{Z}_{2}$-quotient of a metric of the form
$$\tilde{g}(s)=d s^{2}+\lambda(s)^{2} \sigma_{1}(s) \otimes \sigma_{1}(s)+\mu(s)^{2} \sigma_{2}(s) \otimes \sigma_{2}(s)+\nu(s)^{2} \sigma_{3}(s) \otimes \sigma_{3}(s)$$
on $(0, \infty) \times \operatorname{SU}(2)$, where $\lambda, \mu, \nu$ are smooth positive functions, and for each $s>0$, $\left\{\sigma_{1}(s), \sigma_{2}(s), \sigma_{3}(s)\right\}$ is a left-invariant coframe on $S U(2)$. It is well-known that Ricci-flatness leads to diagonalizability of such metrics, i.e. $\sigma_{i}(s)$ can be chosen independently of $s$ (see e.g. [17, §3] for a proof). Thus,
$$g(s)=\lambda(s)^{2} \sigma_{1} \otimes \sigma_{1}+\mu(s)^{2} \sigma_{2} \otimes \sigma_{2}+\nu(s)^{2} \sigma_{3} \otimes \sigma_{3} .$$
From this, we see that any Hausdorff limit of $\left(\mathbb{R P}^{3}, g(s)\right)$ as $s \rightarrow 0$ is homeomorphic to either $\mathbb{R P}^{3}$ or a space of lower dimension. This rules out $G / K \cong L(4,1)$, so Lemma 4.7 leaves us with two possibilities: either $G / K \cong \mathbb{S}^{2}$ or $G / K$ is a point.
\begin{itemize}
\item[-] If $G / K$ is a point, then $M$ is diffeomorphic to the orbifold $\mathbb{R}^{4} / \mathbb{Z}_{2}$. Its universal orbifold cover is $\left(\mathbb{R}^{4}, \tilde{g}\right)$ where $\tilde{g}$ is a Ricci-flat, asymptotically Euclidean metric. By the sharp case of the Bishop-Gromov volume comparison theorem, $\tilde{g}$ is the Euclidean metric. Hence $g$ is flat $\mathbb{R}^{4} / \mathbb{Z}_{2}$.
\end{itemize}
\begin{itemize}
\item[-] If $G / K=\mathbb{S}^{2}$, then $M$ is a smooth manifold. Indeed, either all points in the orbit $G / K$ are orbifold points, or they are all smooth points. Since $M$ is assumed to have finitely many orbifold points, the latter must be true. As the principal part $(0, \infty) \times G / H$ is already smooth, it follows that $M$ is smooth. By construction, $M$ is diffeomorphic to $\mathcal{O}_{\mathbb{C P}^{1}}(-2) \cong T^{*} \mathbb{S}^{2}$. By a theorem of Lock and Viaclovsky [37, Theorem 1.5], $(M, g)$ is hyperkähler. Kronheimer's classification [33] now implies that $(M, g)$ is Eguchi-Hanson space.
\end{itemize}

This concludes Case (A).
4.4. Case (B). In this subsection, we assume $G$ does not act transitively on $\left(\mathbb{R P}^{3}, g_{\rho}\right)$ for all $\rho \geq R_{0}$. We will show that ( $M, g$ ) must be the flat $\mathbb{R}^{4} / \mathbb{Z}_{2}$.

Corollary 4.8. We have $\operatorname{dim} G=3$.
Proof. From §4.2, we already know that $\operatorname{dim} G \geq 3$. If $\operatorname{dim} G \geq 4$, then since $G \cong G_{\rho} \subseteq$ $\mathcal{I}^{0}\left(\mathbb{R P}^{3}, g_{\rho}\right)$ for each $\rho \geq R_{0}$, it follows that $\operatorname{dim} \mathcal{I}\left(\mathbb{R P}^{3}, g_{\rho}\right) \geq 4$. This makes $g_{\rho}$ homogeneous [29, p. 48-49]. By Corollary 4.5, $G$ must act transitively on $\left(\mathbb{R P}^{3}, g_{\rho}\right)$, a contradiction. \(\square\)

Let $\left(\tilde{M}_{\infty}, \tilde{g}\right)$ be the Riemannian universal cover of the end of $(M, g)$. Then $\left(\tilde{M}_{\infty}, \tilde{g}\right)$ is an incomplete asymptotically Euclidean manifold of order 4 diffeomorphic to $\mathbb{R}^{4} \backslash B_{R}(0)$, and it is foliated by CMC 3-spheres. Lifting the action of $G$ on the end of $(M, g)$, we obtain a compact covering group $\tilde{G}$ acting isometrically and effectively on $\left(\tilde{M}_{\infty}, \tilde{g}\right)$. By Corollary 4.8, $\operatorname{dim} \tilde{G}=3$. This restricts to an isometric and effective action on all CMC leaves $\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$, so $\tilde{G}$ can be identified as a subgroup of $\mathcal{I}\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$. Its action on $\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$ is not transitive. Let $\tilde{G}^{0}$ be its identity component. By the classification of compact connected Lie groups of dimension 3, $\tilde{G}^{0}$ is $S U(2), S O(3)$, or $\mathbb{T}^{3}$. However, the next lemma excludes $\tilde{G}^{0}=\mathbb{T}^{3}$. Although this is well-known, we supply a proof for the reader's convenience.

Lemma 4.9. $\mathbb{T}^{3}$ cannot act smoothly and effectively on $\mathbb{S}^{3}$.
Proof. Suppose such an action exists. Since $\mathbb{T}^{3}$ is abelian, the isotropy subgroup $H \subset \mathbb{T}^{3}$ of all points in principal orbits are equal (not just conjugate). Thus, if $H$ is nontrivial, then there exists a nontrivial element $\phi \in H$ which fixes all points in principal orbits. Since principal orbits form a dense open set, it follows that $\phi$ fixes all points on $\mathbb{S}^{3}$. However, this contradicts effectiveness, so $H$ must be trivial. It follows that each principal orbit of the action is 3-dimensional (diffeomorphic to $\mathbb{T}^{3}$ ), hence open in $\mathbb{S}^{3}$. On the other hand, all orbits of the action must be closed. Therefore, a principal orbit must be the whole of $\mathbb{S}^{3}$. But this implies $\mathbb{S}^{3}$ is diffeomorphic to $\mathbb{T}^{3}$, a contradiction. \(\square\)

Next we determine the cohomogeneity of the action of $\tilde{G}^{0}$ on $\left(\tilde{M}_{\infty}, \tilde{g}\right)$, which is one plus the cohomogeneity of the action restricted to $\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$. On $\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$, the principal orbits have positive dimension as the action is effective, but they cannot have dimension 3 as the action is not transitive. Neither can they have dimension 1, because $S O(3)$ and $S U(2)$ do not contain closed subgroups of dimension 2. Therefore, the principal orbits have dimension 2, so the action has cohomogeneity one on $\left(\mathbb{S}^{3}, \tilde{g}_{\rho}\right)$. This also rules out $\tilde{G}^{0}=S U(2)$, as SU (2) cannot act effectively with cohomogeneity one on a 3-sphere (see e.g. [26]). Thus, $\tilde{G}^{0}=S O(3)$. The next proposition summarizes the preceding discussion.