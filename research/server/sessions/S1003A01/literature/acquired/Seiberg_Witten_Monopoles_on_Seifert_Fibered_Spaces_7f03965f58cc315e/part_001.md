---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Seiberg–Witten Monopoles on Seifert Fibered Spaces]

---
source_file: Seiberg_Witten_monopoles_on_Seifert_fibered_spaces_50296bc44118.pdf
converter: mathpix
format: mmd
---

\title{
Seiberg-Witten Monopoles on Seifert Fibered Spaces
}

\author{
Tomasz Mrowka ${ }^{1}$, Peter Ozsváth ${ }^{2}$ and Baozhen Yu
}

\section*{1. Introduction.}

This paper is concerned with Seiberg-Witten gauge theory over Seifert fibered spaces. A Seifert fibered space $\pi: Y \rightarrow \Sigma$ is the unit circle bundle of an orbifold line bundle over $\Sigma$ whose total space is a smooth three-manifold. The case where $Y$ is diffeomorphic to the product of a circle with a Riemann surface has been studied extensively in [29]; in this paper, we will restrict attention to those Seifert fibered spaces which are not diffeomorphic to a product (indeed, those of non-zero degree, in a sense which will be made precise).

Let $i \eta$ denote the connection form of the circle bundle, and $g_{\Sigma}$ be an orbifold metric over $\Sigma$ with constant curvature, then we can endow $Y$ with the metric
$$g_{Y}=\eta^{2}+\pi^{*}\left(g_{\Sigma}\right),$$
for which the tangent bundle $T Y$ has an orthogonal splitting
$$T Y \cong \mathbb{R} \oplus \pi^{*}(T \Sigma) .$$
The Levi-Civita connection on $\Sigma$ then canonically induces a reducible connection ${ }^{\circ} \nabla$ which respects this splitting. We study the solution space to the Seiberg-Witten equations over $Y$, using the above metric and connection on $T Y$ (rather than the Levi-Civita connection, which is usually used in the definition of these equations).

Let $\Sigma$ be a two-dimensional orbifold of genus $g$ with marked points $x_{1}, \ldots, x_{n}$ with associated multiplicities $\alpha_{1}, \ldots, \alpha_{n}$. Viewing the marked points

\footnotetext{
${ }^{1}$ The first author was partially supported by an NSF/NYI fellowship (grant number DMS-9357641) and a Sloan Foundation Fellowship.
${ }^{2}$ The second author was partially supported by an NSF Postdoctoral Fellowship.
}
as "fractional points," one can define a natural Euler characteristic by the formula
$$\chi(\Sigma)=2-2 g+\sum_{i=1}^{n}\left(\frac{1}{\alpha_{i}}-1\right),$$
where $g$ is the genus of the underlying smooth curve $|\Sigma|$.
An orbifold line bundle $E$ over $\Sigma$ (hence, in particular, a Seifert fibered space) is specified up to isomorphism by its Seifert data (see Section 2),
$$\mathbf{b}(E)=\left(b(E), \beta_{1}(E), \ldots, \beta_{n}(E)\right),$$
a vector of integers with
$$0 \leq \beta_{i}(E)<\alpha_{i} .$$
It has an orbifold degree defined by the formula
$$\operatorname{deg}(E)=b(E)+\sum \frac{\beta_{i}(E)}{\alpha_{i}} .$$

The Seiberg-Witten equations on $Y$ are the equations:
$$\begin{aligned}
* \operatorname{Tr}\left(F_{B}\right)-i \tau(\Psi) & =0 \\
\mathbf{D}_{B} \Psi & =0,
\end{aligned}$$
for a spinor $\Psi$ and $B$ a ${ }^{\circ} \nabla$-spinorial connection.
Theorem 1. Let $Y$ be a Seifert fibered space of non-zero degree over the orbifold $\Sigma$. The moduli space of solutions to the Seiberg-Witten Equations on $Y$ with metric $g_{Y}$ and connection ${ }^{\circ} \nabla$ is naturally identified with the union of the moduli space of flat $S^{1}$-connections over $Y$ and two copies of the space of effective orbifold divisors over $\Sigma$ with orbifold degree less than $-\frac{\chi(\Sigma)}{2}$.

Remark 1.1. In the above statement, the solutions have not been partitioned according to the $\operatorname{Spin}_{\mathrm{c}}(3)$ structures in which they live. See Theorem 5.19 for a restatement of Theorem 1 which makes this partitioning explicit.

The map from the solution space to the spaces of divisors is obtained by taking a solution $(B, \Psi)$ to the zero-set of $\Psi$. In the course of the proof of Theorem 1, it is shown that the solution must be circle-invariant and $\Psi$ lies in the ±1 eigenspace of Clifford multiplication by $i * \eta$. Hence $\Psi^{-1}(0)$ consists of a collection of fiber circles and so determines a divisor over $\Sigma$.

In other words, the moduli space of solutions to the Seiberg-Witten Equations consists of a collection of components corresponding to the $S^{1}$ -representation variety of $Y$ (which is a certain number of copies of the Jacobian torus of $|\Sigma|)$ and a collection of components $\mathcal{C}^{+}(\mathbf{e})$ and $\mathcal{C}^{-}(\mathbf{e})$, labeled by all vectors e of non-negative integers $\left(e, \epsilon_{1}, \ldots, \epsilon_{n}\right)$, with
$$0 \leq \epsilon_{i}<\alpha_{i},$$
and
$$e+\sum_{i=1}^{n} \frac{\epsilon_{i}}{\alpha_{i}}<-\frac{\chi(\Sigma)}{2} .$$
The spaces $\mathcal{C}^{+}(\mathbf{e})$ and $\mathcal{C}^{-}(\mathbf{e})$ both correspond to the space of effective orbifold divisors on $\Sigma$ with multiplicities $\epsilon_{i}$ over the singular points $x_{i}$, and a background degree $e$. As such, these spaces are diffeomorphic to the $e^{\text {th }}$ symmetric product of $|\Sigma|, \operatorname{Sym}^{e}(|\Sigma|)$. For $(B, \Psi) \in \mathcal{C}^{ \pm}(\mathbf{e}), \Psi$ lies in the $\pm 1$ eigenspace of Clifford multiplication by $i * \eta$.

So, loosely speaking, the solutions to the Seiberg-Witten equations over Seifert fibered spaces consist of closed orbits of the circle action with bounded weight which, in turn, corrspond to familiar objects from contact geometry. If $\eta$ is a connection form for $Y$ whose curvature form vanishes nowhere (which can always be arranged when the orbifold degree of the bundle defining $Y$ is non-zero), then $\eta$ is a contact form on $Y$. Moreover, the closed orbits for the circle action are precisely the closed orbits for the corresponding Reeb flow.

In a similar vein, flow lines between critical manifolds correspond to holomorphic (or anti-holomorphic) curves in the cylinder $\mathbb{R} \times Y$. Indeed, we obtain a correspondence between the moduli spaces of gradient flow-lines and certain holomorphic curves in the closed orbifold ruled surface $R$, obtained by attaching two copies of the base orbifold to the cylinder. To state the correspondence precisely, we make the following definition.

Definition 1.2. Let $\Sigma_{-}, \Sigma_{+} \subset R$ denote the two "sections at infinity" in the ruled surface. Given a pair of orbifold line bundles $E_{1}$ and $E_{2}$ a divisor on $R$ interpolating between $E_{1}$ and $E_{2}$ is an effective divisor $D \subset R$ which does not contain $\Sigma_{-}$or $\Sigma_{+}$and whose restrictions to these curves are divisors in $E_{1}$ and $E_{2}$ respectively.

Theorem 2. Let $Y$ as in Theorem 1, and fix components $\mathcal{C}^{+}\left(\mathbf{e}_{1}\right), \mathcal{C}^{+}\left(\mathbf{e}_{2}\right)$ in the moduli space $\mathcal{M}_{s w}(Y)$. Let $E_{1}, E_{2}$ be line bundles over $\Sigma$ with Seifert data $\mathbf{e}_{1}$ and $\mathbf{e}_{2}$ respectively. Then, there is a natural identification of the
moduli space of flows between $\mathcal{C}^{+}\left(\mathbf{e}_{1}\right)$ and $\mathcal{C}^{+}\left(\mathbf{e}_{2}\right)$ with the space of divisors in $R$ interpolating between $E_{1}$ and $E_{2}$. Similarly for the space of flows between $\mathcal{C}^{-}\left(\mathbf{e}_{1}\right)$ and $\mathcal{C}^{-}\left(\mathbf{e}_{2}\right)$. Moreover, there are no flows between $\mathcal{C}^{+}\left(\mathbf{e}_{1}\right)$ and $\mathcal{C}^{-}\left(\mathbf{e}_{2}\right)$.

Similar statements hold for flows which involve the reducible locus (see Theorem 10.6).

In addition to providing a conceptual interpretation of the moduli spaces of flow-lines, in terms of holomorphic data, the above theorem furnishes a concrete, computational understanding of these moduli spaces, since the corresponding holomorphic objects can be understood quite explicitly. To clarify this point, we set up an identification between the theory of holomorphic curves in the typically singular ruled surface $R$ (a surface with isolated cyclic quotient singularities in a two-to-one correspondence with the marked points on the base orbifold), with the theory of holomorphic curves in its smooth resolution $\widehat{R}$. We state the correspondence theorem informally as follows, relegating the technically complete statement to Section 11 (see Theorem 7):

Theorem 3. There is a natural identification of the moduli space of divisors on $R$ interpolating between $E_{1}$ and $E_{2}$ with the moduli space of divisors on $\widehat{R}$ in the homology class determined by $E_{1}$ and $E_{2}$, via the procedure described in Section 3.

Note that $\widehat{R}$ is a blow-up of $\mathbb{C P}^{2}$ or a ruled surface (see Section 3) and one can often use this description to understand the moduli space explicitly.

To illustrate the above results, we derive a formula for the climensions of the moduli spaces of flow-lines. But before describing this formula, we must introduce some notation. Suppose that the Seifert fibered space $Y$ has Seifert invariants $\left(b, \beta_{1}, \ldots, \beta_{n}\right)$. Let $d_{k}^{j}$ be the $k^{t h}$ denominator in the Hirzebruch-Jung continued fraction expansion of $\alpha_{j} / \beta_{j}$, i.e. for a fixed $j$, $d_{k}^{j}$ for $k=0, \ldots, m_{j}$ is the sequence of integers which satisfies the initial conditions
$$\begin{aligned}
& d_{0}^{j}=\alpha_{j}, \\
& d_{1}^{j}=\beta_{j},
\end{aligned}$$
the recurrence relation
$$d_{k}^{j}=d_{k-1}^{j}\left\lceil\frac{d_{k-2}^{j}}{d_{k-1}^{j}}\right\rceil-d_{k-2}^{j},$$
and the termination condition that
$$d_{m_{j}}^{j}=1$$
for some integer $m_{j}$. Here, $\lceil x\rceil$ denotes the smallest integer no greater than $x$. Given Seifert data $\mathbf{e}=\left(e, \epsilon_{1}, \ldots, \epsilon_{n}\right)$, let $\xi_{k}^{j}$ be the minimal decomposition of $\epsilon_{j}$ with respect to the $d_{1}^{j}, \ldots, d_{m_{j}}^{j}$, i.e. for a fixed $j$, the $\xi_{k}^{j}$ for $k=1, \ldots, m_{j}$ satisfy the recurrence relation
$$\xi_{k}^{j}=\left\lfloor\frac{\epsilon_{j}-\sum_{i=1}^{k-1} d_{i}^{j} \xi_{i}^{j}}{d_{k}^{j}}\right\rfloor .$$

Definition 1.3. Given the above data, we define a rational quantity, the $Y$-dimension of $\mathbf{e}$, by the formula
$$\begin{aligned}
\operatorname{dim}_{Y}(\mathbf{e})= & \sum_{j=1}^{n}\left\{\left(\sum_{\ell=1}^{m_{j}} \xi_{\ell}^{j}\right)-\left(\sum_{\ell=1}^{m_{j}} d_{\ell}^{j} \xi_{\ell}^{j} \sum_{i=1}^{\ell} \frac{1}{d_{i-1}^{j} d_{i}^{j}}\right)\right. \\
& \left.-\left(\sum_{\ell, k=1}^{m_{j}} d_{k}^{j} \xi_{k}^{j} d_{\ell}^{j} \xi_{\ell}^{j} \sum_{i=1}^{\min (k, \ell)} \frac{1}{d_{i-1}^{j} d_{i}^{j}}\right)\right\} \\
& +e+\frac{\operatorname{deg}(E)}{\operatorname{deg}(Y)}\left(\operatorname{deg}(E)-\operatorname{deg}\left(K_{\Sigma}\right)\right),
\end{aligned}$$
where $K_{\Sigma}$ is the orbifold canonical bundle, and $E$ is the orbifold line bundle over $\Sigma$ with Seifert data e.

Combining Theorems 2 and 3 with the Riemann-Roch formula, we get the following Corollary:

Corollary 1.4. The moduli space of flows from $\mathcal{C}^{ \pm}\left(\mathbf{e}_{1}\right)$ to $\mathcal{C}^{ \pm}\left(\mathbf{e}_{2}\right)$ has dimension given by
$$\operatorname{dim}_{Y}\left(\mathbf{e}_{1}\right)+\operatorname{dim}_{Y^{-1}}\left(\mathbf{e}_{2}\right),$$
where $Y^{-1}$ is the inverse of $Y$, as a circle bundle over $\Sigma$.
We specialize the above results first to the case where $Y$ fibers over a Riemann surface $\Sigma$ with no orbifold points, and then to the case where $Y=\Sigma(p, q, r)$ is a Brieskorn sphere (i.e. the Seifert fibered space which is an integral homology sphere fibering over the genus zero orbifold with three marked points with pairwise relatively prime multiplicities $p, q$, and $r$ ).

Corollary 1.5. Let $Y$ be a non-trivial circle bundle over a Riemann surface $\Sigma$ of genus $g$, with first Chern number $n$. Then, the Seiberg-Witten moduli space is identified with:
$$\left(\mathbb{Z} / n \mathbb{Z} \times(\mathbb{R} / \mathbb{Z})^{2 g}\right) \amalg\left(\coprod_{e=0}^{g-2} \mathcal{C}^{+}(e)\right) \amalg\left(\coprod_{e=0}^{g-2} \mathcal{C}^{-}(e)\right),$$
where now $e$ is simply a non-negative integer, and
$$\mathcal{C}^{+}(e) \cong \mathcal{C}^{-}(e) \cong \operatorname{Sym}^{e}(\Sigma) .$$
The dimension of the space of flows connecting $\mathcal{C}^{+}\left(e_{1}\right)$ with $\mathcal{C}^{+}\left(e_{2}\right)$ is given by
$$\operatorname{dim} \mathcal{M}\left(e_{1}, e_{2}\right)=\frac{\left(e_{1}-e_{2}\right)}{n}\left(e_{1}+e_{2}-(2 g-2)\right)+\left(e_{1}+e_{2}\right) .$$

When $Y=\Sigma(p, q, r)$ is a Brieskorn sphere, the Seiberg-Witten moduli space is a discrete collection of points, since
$$-\frac{\chi(\Sigma(p, q, r))}{2}=\frac{1}{2}\left(1-\frac{1}{p}-\frac{1}{q}-\frac{1}{r}\right)<1 .$$
Following the usual construction of Floer homology, we can form the relatively graded chain complex freely generated by the irreducible critical points, with boundary maps induced by one-dimensional flow lines (see Section 13). In the Brieskorn sphere case, our results then specialize to the following statement about the homology groups of this complex, the irreducible Seiberg-Witten Floer homology groups $\operatorname{HF}_{*}^{i r r}(\Sigma(p, q, r))$ :

Corollary 1.6. For $p, q, r$ pairwise relatively prime, the group
$$\mathrm{HF}_{*}^{i r r}(\Sigma(p, q, r))$$
is a free Abelian group generated by two generators for each triple $\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}\right)$ of non-negative integers satisfying
$$\frac{\epsilon_{1}}{p}+\frac{\epsilon_{2}}{q}+\frac{\epsilon_{3}}{r}<-\frac{\chi(\Sigma(p, q, r))}{2} .$$
The Floer degree of either solution corresponding to $\left(\epsilon_{1}, \epsilon_{2}, \epsilon_{3}\right)$ is calculated by $\operatorname{dim}_{\Sigma(p, q, r)}\left(0, \epsilon_{1}, \epsilon_{2}, \epsilon_{3}\right)$

This paper is organized as follows. Sections 2, 3, and 4 are introductory: Section 2 covers some of the basics of orbifold theory, Section 3 discusses some of the elementary properties of the ruled surfaces associated to an orbifold line bundle and its resolution, and Section 4 covers some of the basics of the Seiberg-Witten monopole equations. Section 5 contains the proof of the circle-invariance of monopoles over a Seifert fibered space $Y$, which gives Theorem 1. Section 6 gives the identification of finite-energy gradient flow-lines with holomorphic data over the cylinder. Section 7 shows how to construct a divisor on the ruled surface, given this data. Section 8 is concerned with the converse problem: it shows how a divisor on $R$ gives rise to a gradient flow-line, by reducing the problem to a Kazdan-Warner equation over the cylinder, which is then solved. Thus, Sections 7 and 8 together construct maps between the moduli spaces, which are shown to give induce identifications on the infinitesimal level in Section 9, proving Theorem 2. Section 10 covers the analogue of Theorem 2 for flows involving the reducibles. Section 11 proves the correspondence between orbifold divisors over the singular ruled surface and divisors over its de-singularization, Theorem 3. Section 12 derives the dimension formula in Corollary 1.4 from the Riemann-Roch theorem, together with the correspondence with the space of divisors in the de-singularized surface from Section 11. Finally, Section 13 is devoted to some examples.

The authors wish to thank P. B. Kronheimer for inspiring conversations and G. Matić for explaining her work with P. Lisca, which provided a fertile testing-ground for our results.

During the preparation of this manuscript, Baozhen Yu passed away. His untimely death has left us with a profound sense of loss.

\section*{2. Orbifolds and Seifert Fibered Spaces.}

A Seifert fibered space is a three-dimensional manifold $Y$ together with an $S^{1}$ action with finite stabilizers (see [31], [30], [9]); these spaces can be profitably viewed in terms of the theory of orbifold bundles. This section outlines some of the elements of this theory. A more extensive discussion can be found in [9].

Let $D$ denote the standard complex disk, on which $\mathbb{Z} / \alpha \mathbb{Z}$ acts by rotation. An orbifold is a Hausdorff space $|\Sigma|$ with a distinguished finite set of "marked points" $x_{1}, \ldots, x_{n}$ given with integral multiplicities $\alpha_{1}, \ldots, \alpha_{n}$ all
greater than 1, equipped with an atlas of coordinate charts
$$\begin{aligned}
\phi_{i}:(D, 0) & \rightarrow\left(U_{i}, x_{i}\right) & i=1, \ldots, n & \\
\phi_{x}: D_{x} & \rightarrow U_{x} & & x \in \Sigma-\left\{x_{1}, \ldots, x_{n}\right\},
\end{aligned}$$
where the $\phi_{i}$ induce homeomorphisms from $(D, 0) /\left(\mathbb{Z} / \alpha_{i} \mathbb{Z}\right)$ to $\left(U_{i}, x_{i}\right)$, the $\phi_{x}$ are homeomorphisms, the neighborhoods $U_{i}$ of the distinguished points are pairwise disjoint, and all transition functions (defined over the overlaps) are holomorphic. Of course, when there are no marked points, $\Sigma$ is simply a smooth holomorphic curve, and the theory which will be outlined below is simply gauge theory over that curve. In the presence of marked points, the underlying topological space $|\Sigma|$ still inherits the structure of a smooth complex curve, with local coordinate on $D /\left(\mathbb{Z} / \alpha_{i} \mathbb{Z}\right)$-neighborhood of the marked point $x_{i}$ given by $w^{\alpha_{i}}$, where $w$ is a local (holomorphic) coordinate on $D$.

An $n$-dimensional orbifold bundle is a collection of $\mathbb{Z} / \alpha_{i} \mathbb{Z}$-equivariant $n$ -dimensional vector bundles $E_{i}$ over $U_{i}$, and vector bundles $E_{x}$ over the $U_{x}$, together with a 1 -cocycle of transition functions over the overlaps. Over each $U_{i}$, a $\mathbb{Z} / \alpha_{i} \mathbb{Z}$-equivariant vector bundle is specified up to isometry by giving a representation
$$\rho_{i}: \mathbb{Z} / \alpha_{i} \mathbb{Z} \rightarrow \mathrm{Gl}_{\mathrm{n}}(\mathbb{C}) .$$
The usual notions from gauge theory generalize in a straightforward way to orbifold bundles. For example, an orbifold connection on an orbifold bundle is a collection $\nabla_{i}$ of $\mathbb{Z} / \alpha_{i} \mathbb{Z}$-equivariant connections over the disks $U_{i}$, and connections $\nabla_{x}$ over the $E_{x}$, which match up; an orbifold section is a collection of $\mathbb{Z} / \alpha_{i} \mathbb{Z}$-equivariant sections $\psi_{i}$ of the $E_{i}$ and sections $\psi_{x}$ of $E_{x}$, all of which match up; and a holomorphic orbifold bundle is a collection of (equivariant) holomorphic bundles over the charts, with a 1-cocycle of holomorphic transition functions.

Example 2.1. Holomorphic sections of the trivial orbifold bundle over $\Sigma$ correspond to holomorphic functions over the smooth curve $|\Sigma|$.

Example 2.2. The rotation action of $\mathbb{Z} / \alpha \mathbb{Z}$ on the disk $D$ naturally lifts to an action on the cotangent bundle of $D$, giving the cotangent bundle the structure of a $\mathbb{Z} / \alpha \mathbb{Z}$-equivariant line bundle, or an orbifold line bundle over $D /(\mathbb{Z} / \alpha \mathbb{Z})$. Moreover, any orbifold $\Sigma$ is naturally endowed with a distinguished holomorphic orbifold line bundle the canonical bundle, denoted $K_{\Sigma}$, defined by gluing the cotangent bundles of the $U_{i}$ and the $U_{x}$ via the complex derivative of the transition functions.

Example 2.3. Given an orbifold $\Sigma$ and a distinguished point $x_{i} \in \Sigma$ whose neighborhood $U_{i}$ is isomorphic to $D /(\mathbb{Z} / \alpha \mathbb{Z})$, we can define a (holomorphic) orbifold line bundle $H_{x_{i}}$ as follows. The bundle is trivial away from $x_{i}$, and, over $U_{x_{i}}$, is given by the $\mathbb{Z} / \alpha_{i} \mathbb{Z}$-equivariant line bundle $D \times \mathbb{C}$, where $a \in \mathbb{Z} / \alpha_{i} \mathbb{Z}$ acts by
$$a \times(w, z) \mapsto\left(e^{\frac{2 \pi \mathrm{i} a}{\alpha_{i}}} w, e^{\frac{2 \pi \mathrm{i} a}{\alpha_{i}}} z\right),$$
with transition function $w$.
Definition 2.4. The topological Picard group, denoted $\operatorname{Pic}^{t}(\Sigma)$, is the group of topological isomorphism classes of orbifold line bundles over $\Sigma$, where the group law is tensor product.

Lemma 2.5. The line bundle $H_{0}$ generates $\operatorname{Pic}^{t}(D /(\mathbb{Z} / \alpha \mathbb{Z}))$, inducing an isomorphism
$$\operatorname{Pic}^{t}(D /(\mathbb{Z} / \alpha \mathbb{Z})) \cong \mathbb{Z} / \alpha \mathbb{Z} .$$
Moreover, multiplying by $w^{-\beta}$, where $w$ is a holomorphic coordinate on $D$, and $0 \leq \beta<\alpha$, gives an identification between holomorphic sections on $H_{0}^{\beta}$ and holomorphic functions on $D /(\mathbb{Z} / \alpha \mathbb{Z})$.

Proof. Holomorphic sections of $H_{0}^{\beta}$ correspond to holomorphic functions
$$f: D \rightarrow \mathbb{C}$$
with
$$f(\zeta w)=\zeta^{\beta} f(w),$$
for each $\zeta$ an $\alpha^{\text {th }}$ root of unity; or equivalently, functions of the form
$$f(w)=w^{\beta} g\left(w^{p}\right),$$
where $g$ is a holomorphic function. \(\square\)

Given an orbifold line bundle $E$ over a closed orbifold $\Sigma$ with exceptional points $x_{1}, \ldots, x_{n}$ and multiplicities $\alpha_{1}, \ldots, \alpha_{n}$, Lemma 2.5 gives a collection of local invariants $\beta_{1}, \ldots, \beta_{n}$ with
$$0 \leq \beta_{i}<\alpha_{i}$$
which describe $E$ near the singular points.

Definition 2.6. The bundle $E \otimes H_{x_{1}}^{-\beta_{1}} \otimes \ldots \otimes H_{x_{n}}^{-\beta_{n}}$ is an orbifold line bundle which is naturally isomorphic to a smooth line bundle over the smooth curve $|\Sigma|$. This bundle is called the de-singularization of $E$ and is denoted $|E|$.

Definition 2.7. Given an orbifold line bundle $E$ over $\Sigma$, the collection of integers
$$\left(b, \beta_{1}, \ldots, \beta_{n}\right),$$
where $b$ is the first Chern number of the de-singularization $|E|$ over $|\Sigma|$, is called the Seifert invariant of $E$ over $\Sigma$.

The integer $b$ will be called the background degree of $E$.
Lemma 2.5 naturally globalizes to give the following:
Proposition 2.8. The holomorphic sections of a holomorphic orbifold line bundle $E$ over $\Sigma$ correspond naturally to the holomorphic sections of its de-singularization $|E|$ over $|\Sigma|$.

Two familiar theorems from complex geometry readily generalize to the orbifold context:

Theorem 2.9 (Riemann-Roch). Let $E$ be a holomorphic line bundle over a complex orbifold $\Sigma$, and $\mathcal{E}$ denote its sheaf of holomorphic sections. Then
$$\chi(\mathcal{E})-\chi\left(\mathcal{O}_{\Sigma}\right)=b,$$
where $\chi(\mathcal{F})$ denotes the (complex) Euler characteristic of the sheaf $\mathcal{F}, \mathcal{O}_{\Sigma}$ denotes the sheaf of regular functions on $\Sigma$, and $b$ is the background degree of $E$. Equivalently,
$$\chi(\mathcal{E})=1-g+b .$$

Theorem 2.10. (Serre duality) Let $E \rightarrow \Sigma$ be an orbifold line bundle over an orbifold equipped with an orbifold metric. Then the Hodge star operator induces an isomorphism
$$H^{0}(\Sigma, E) \cong H^{1}\left(\Sigma, K_{\Sigma} \otimes E^{-1}\right) .$$

An orbifold line bundle $E$ over $\Sigma$ has a naturally associated first Chern number, or degree $\operatorname{deg}(E)$, defined by
$$\operatorname{deg}(E)=b+\sum_{i} \frac{\beta_{i}}{\alpha_{i}} .$$

Example 2.11. Since the pull-back of $d z$ over $D$ by the map which rotates through $\zeta=e^{2 \pi i / \alpha}$ is $\zeta d z$, we see that the local invariants for the canonical bundle are $\alpha-1$. In fact, since we can naturally identify the canonical bundle of a orbifold $\Sigma$ away from the singular points with the canonical bundle of a smooth curve of genus $g$, we have that the Seifert invariant of $K_{\Sigma}$ is
$$\left(2 g-2, \alpha_{1}-1, \ldots, \alpha_{n}-1\right) .$$
Thus, the degree of $K_{\Sigma}$ is minus the Euler characteristic of $\Sigma$ (as defined in Equation 1.1).

We recall the following result (see [9],[30]), which says that the Seifert invariants of an orbifold line bundle classify the bundle.

Proposition 2.12. The map
$$\operatorname{Pic}^{t}(\Sigma) \rightarrow \mathbb{Q} \oplus \bigoplus_{i=1}^{n} Z / \alpha_{i}$$
given by
$$E \mapsto\left(\operatorname{deg}(E), \beta_{1}, \ldots, \beta_{r}\right)$$
is an injection, with image the set of tuples $\left(c, \beta_{i}\right)$ with
$$c \equiv \sum \beta_{i} / \alpha_{i}(\bmod \mathbb{Z}) .$$

In particular, if the $\alpha_{i}$ are mutually coprime, then $\operatorname{Pic}^{t}(\Sigma) \cong \mathbb{Z}$ is generated by a single line bundle $E_{0}$ with
$$\operatorname{deg}\left(E_{0}\right)=\frac{1}{\alpha_{1} \ldots \alpha_{n}} .$$

Suppose $N$ is an orbifold bundle whose local invariants $\beta_{i}$ are all relatively prime to $\alpha_{i}$. Then, the unit circle bundle of $N$, denoted $S(N)$, is naturally a smooth three-manifold. Such a circle bundle is called a Seifert fibered space.

In this case, the orbifold invariants of $N$ are reflected in the topological invariants of its unit sphere bundle, according to the following theorem (see [9]).

Theorem 2.13. If $S(N)$ is a Seifert fibered space, then for $1 \leq i \leq n$, $1 \leq j \leq g$,
$$\begin{aligned}
\pi_{1}(S(N))=\left\langle a_{i}, b_{i}, g_{i}, h\right|\left[a_{j}, h\right] & =\left[b_{j}, h\right]=\left[g_{i}, h\right]=1= \\
& =g^{\alpha_{i}} h^{\beta_{i}}=h^{-b} \prod\left[a_{j}, b_{j}\right] \prod\left[g_{i},\right\rangle
\end{aligned}$$
and
$$\begin{aligned}
& H^{1}(S(N)) \cong \begin{cases}H^{1}(\Sigma) & \operatorname{deg}(N) \neq 0 \\
H^{1}(\Sigma) \oplus \mathbb{Z} & \operatorname{deg}(N)=0\end{cases} \\
& H^{2}(S(N)) \cong\left(\operatorname{Pic}^{t}(\Sigma) / \mathbb{Z}[N]\right) \oplus \mathbb{Z}^{2 g}
\end{aligned}$$

Remark 2.14. The subgroup $\operatorname{Pic}^{t}(\Sigma) / \mathbb{Z}[N] \subset H^{2}(Y ; \mathbb{Z})$ corresponds to the image of the pull-back map
$$\operatorname{Pic}^{t}(\Sigma) \xrightarrow{\pi^{*}}[\text { Line bundles over } Y] \xrightarrow{c_{1}} H^{2}(Y ; \mathbb{Z}) .$$
When $\operatorname{deg}(N) \neq 0$, this is a finite Abelian group, by Proposition 2.12.
Corollary 2.15. If $N$ is as above, with $\operatorname{deg}(N) \neq 0$, then the representation space of flat $S^{1}$ bundles over $S(N), \operatorname{Hom}\left(\pi_{1}(Y), S^{1}\right)$, fits into a split exact sequence
$$0 \longrightarrow \frac{H^{1}(|\Sigma| ; \mathbb{R})}{H^{1}(|\Sigma| ; \mathbb{Z})} \longrightarrow \operatorname{Hom}\left(\pi_{1}(Y), S^{1}\right) \xrightarrow{c_{1}} \operatorname{Pic}^{t}(\Sigma) / \mathbb{Z}[N] \longrightarrow 0 .$$

\section*{3. The Ruled Surface.}

In looking at the flow equations for the Seiberg-Witten equation for a three-manifold $Y$, one is naturally led to consider the cylinder $R^{c}=\mathbb{R} \times Y$. When $Y=S(N)$ has the structure of a Seifert fibered space associated to the orbifold line bundle $N$, the cylinder has a natural compactification, the space obtained by attaching two copies of $\Sigma$ (attached to $Y$ via $\pi$ ), one at each end of the real line, $+\infty$ and $-\infty$. These curves will be denoted $\Sigma_{-}$ and $\Sigma_{+}$respectively, and the compactified space will be denoted $R$.

Equivalently, the space $R$ can be thought of as the orbifold sphere bundle obtained by projectivizing the (orbifold) complex plane bundle $\mathbb{C} \oplus N$ over $\Sigma$, with $\Sigma_{-}, \Sigma_{+}$the projectivizations of $\mathbb{C} \oplus 0$ and $0 \oplus N$ respectively. The projection
$$\pi: R \rightarrow \Sigma$$
naturally extends the projection map of $\mathbb{R} \times Y$ to $\Sigma$, via the obvious identification of $R-\Sigma_{*} \cong \mathbb{R} \times Y$, where $\Sigma_{*}=\Sigma_{+} \amalg \Sigma_{-}$. It is clear from this model that a holomorphic structure on $N$ induces on $R$ the structure of a (possibly singular) complex surface, for which $\pi$ is a holomorphic map.

In fact, the singularities in $R$ are all quotient singularities, which are in a two-to-one correspondence with the marked points of $\Sigma$. More precisely, let $a \in \mathbb{Z} / \alpha \mathbb{Z}$ act on $\mathbb{C}^{2}$ by
$$a \times(w, z)=\left(\zeta^{a} w, \zeta^{\beta a} z\right),$$
where $\zeta$ is a primitive $\alpha^{\text {th }}$ root of unity. Denote the quotient by
$$C_{\alpha, \beta}=\mathbb{C}^{2} /(\mathbb{Z} / \alpha \mathbb{Z}) .$$

Now, if $x \in \Sigma$ is a singular point, then there are two corresponding singular points in the fiber of $\pi$,
$$x_{ \pm}=\Sigma_{ \pm} \cap \pi^{-1}(x),$$
corresponding to the two fixed points of the $S^{1}$ action on $S^{2}$. If the local invariant of $N$ at $x$ is $\beta$, then a neighborhood of $x_{ \pm}$in $R$ is biholomorphic to a neighborhood of the origin in $C_{\alpha, \pm \beta}$.

The minimal resolution, $\widehat{R}$, of $R$ can now be described quite concretely. First recall (see for example [10]; we will revisit this construction in Section 11) that the minimal resolution $\widehat{C}_{\alpha, \beta}$ is constructed by writing $\alpha / \beta$ in its "Hirzebruch-Jung" continued fraction expansion
$$\frac{\alpha}{\beta}=a_{1}-\frac{1}{a_{2}-\frac{1}{\ddots-\frac{1}{a_{m}}}},$$
(with $a_{i} \in \mathbb{Z}, a_{i} \geq 2$ ) which we will abbreviate by writing
$$\frac{\alpha}{\beta}=\left\langle a_{1}, \ldots, a_{m}\right\rangle .$$
Then, $\widehat{C}_{\alpha, \beta}$ is obtained by plumbing together $m$ bundles over $S^{2}$ according to the following diagram:
![](https://cdn.mathpix.com/cropped/42f1b57f-f433-4175-9f9c-9eca23c647ec-013.jpg?height=76&width=781&top_left_y=2030&top_left_x=487)
to obtain a manifold with $m$ two-spheres $\left\{S_{i}\right\}_{i=1}^{m}$, where $S_{i}$ has self-intersection number $-a_{i}$ and intersects only $S_{i-1}$ and $S_{i+1}$ (when $i-1$,
$i+1$ are still in the range from 1 to $m$ ) transversally in a single positive point. The map
$$r: \widehat{C}_{\alpha, \beta} \rightarrow C_{\alpha, \beta}$$
collapses the chain $D=\bigcup_{i=1}^{m} S_{i}$ to $[0,0]$, and is biholomorphic away from the chain. Now, the minimal resolution $\widehat{R}$ is obtained by inserting such a configuration of spheres over each of the $2 n$ singular points in $R$.

Since the restriction of an orbifold line bundle $N$ over $\Sigma,\left.N\right|_{\Sigma-\left\{x_{1}, \ldots, x_{n}\right\}}$, is isomorphic to the restriction of $|N|$ to $|\Sigma|-\left\{x_{1}, \ldots, x_{n}\right\}$, we have that a Zariski open subset of $R$ is isomorphic to a Zariski open subset of the smooth ruled surface obtained by projectivizing $|N| \oplus \mathbb{C}$ over $|\Sigma|$. Thus, we have:

Proposition 3.1. The resolution $\widehat{R}$ is the blowup of a ruled surface fibering over a surface of genus $g$. In particular, if $g=0, \widehat{R}$ is rational.

\section*{4. The Seiberg-Witten Equations.}

We give a brief discussion of the Seiberg-Witten equations, mainly to set up the notation. For a thorough discussion see [28].

Let $Y$ be a Riemannian three-manifold. A $\operatorname{Spin}_{\mathrm{c}}(3)$ structure $(W, \rho)$ is determined by a Hermitian two-plane bundle, the spinor bundle $W$ over $Y$, and a positive Clifford module structure
$$\rho: T^{*} Y \rightarrow \operatorname{su}(W)$$
i.e. a skew-symmetric action of $T^{*} Y$ on $W$ with satisfying the Clifford relation
$$\rho(\theta) \circ \rho(\theta)=-|\theta|^{2} \mathbb{1}_{W},$$
for any $\theta \in \Omega^{1}(Y, \mathbb{R})$, with the property that
$$\rho\left(\mu_{Y}\right)=\mathbb{1}_{W},$$
where $\mu_{Y}$ is the volume form of $Y$, and $\mathbb{1}_{W}$ is the identity endomorphism of the bundle $W$. In this second identity, we have used the action of $\Lambda^{*} Y$ on $W$, also denoted $\rho$, extending the given action of $T^{*} Y$ (this extension exists thanks to the Clifford relation). We will usually abbreviate $\rho(\theta) \Phi$ by $\theta \cdot \Phi$.

Fix an $\operatorname{SO}(3)$-connection ${ }^{\circ} \nabla$ on the cotangent bundle $T^{*} Y$.
Definition 4.1. A Hermitian connection ∇ on $W$ is called spinorial with respect to ° ∇, if ° ∇ is the connection $\nabla$ induces on the cotangent bundle; equivalently, if for all vector fields $X$ and cotangent vector fields $\theta$, we have
$$\left[\nabla_{X}, \rho(\theta)\right]=-\rho\left({ }^{\circ} \nabla_{X} \theta\right)$$

Given an orthonormal coframe $\left\{\theta^{1}, \theta^{2}, \theta^{3}\right\}$ over some patch, and a trivialization for $W$, the connection matrix of any ${ }^{\circ} \nabla$-spinorial connection ∇ can be written with respect to this trivialization as
$$\frac{1}{4} \sum \omega_{j}^{i} \otimes \rho\left(\theta^{i} \wedge \theta^{j}\right)+b \mathbb{1}_{W}$$
where $\omega_{j}^{i}$ are the connection matrices for ${ }^{\circ} \nabla$ with respect to the trivialization $\left\{\theta^{1}, \theta^{2}, \theta^{3}\right\}$ of $T^{*} Y$, and $b \in \Omega^{1}(Y, i \mathbb{R})$ is any purely imaginary 1-form.

The pre-configuration space associated to $W$, written $\mathcal{C}(W)$, is the space
$$\mathcal{C}(W)=\mathcal{A}(W) \times \Gamma(Y, W)$$
formed from the space $\mathcal{A}(W)$ of ${ }^{\circ} \nabla$-spinorial Hermitian connections on $W$, together with the space of spinor fields over $Y$. Since $\mathcal{A}(W)$ has an affine structure for the vector space $\Omega^{1}(Y, i \mathbb{R}), \mathcal{C}(W)$ naturally inherits a manifold structure with
$$T_{(B, \Psi)} \mathcal{C}(W) \cong \Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(Y, W) .$$

The gauge group $\mathcal{G} \cong \operatorname{Map}\left(Y, S^{1}\right)$ acts on $W$ by scalar multiplication, and hence on the space $\mathcal{C}(W)$ by
$$u \times\left(\nabla_{B}, \Psi\right)=\left(u \nabla_{B} u^{-1}, u \Psi\right),$$
an action whose quotient,
$$\mathcal{B}(W)=\mathcal{C}(W) / \mathcal{G},$$
is the configuration space associated to $W$. If $\Phi \not \equiv 0$, one calls the pair $(B, \Psi)$ irreducible, and denotes the space of irreducibles by $\mathcal{C}^{*}(W)$. The gauge group acts freely on the irreducibles. The linearization for the $L^{2}$ slice condition for the group action at $(B, \Psi)$ is the map
$$T_{(B, \Psi)} \mathcal{C}(W) \rightarrow T \mathcal{G}_{e} \cong \Omega^{0}(Y, i \mathbb{R})$$
given by
$$(b, \psi) \mapsto d^{*} b+i \operatorname{Im}(\Psi, \psi),$$
where the second term is the imaginary part of the Hermitian inner product of $\Psi$ with $\psi$. With the help of this slice, one can realize the quotient
$$\mathcal{B}^{*}(W)=\mathcal{C}^{*}(W) / \mathcal{G}$$
as a Hausdorff Hilbert manifold, after giving $\mathcal{C}(W)$ and $\mathcal{G}$ suitable Sobolev topologies.

Following [19], there is a functional whose gradient flow equations are the four-dimensional Seiberg-Witten equations, and whose critical points are the three-dimensional Seiberg-Witten equations. More precisely, if we choose some reference connection $B_{0} \in \mathcal{A}(W)$, there is a functional
$$\operatorname{cs}: \mathcal{C}(W) \rightarrow \mathbb{R}$$
defined by
$$\operatorname{cs}(B, \Psi)=\int_{Y}\left(B-B_{0}\right) \wedge \operatorname{Tr}\left(F_{B}+F_{B_{0}}\right)+\int_{Y}\left\langle\Psi, \mathbf{D}_{B} \Psi\right\rangle,$$
where
$$\mathbf{D}_{B}: \Gamma(Y, W) \rightarrow \Gamma(Y, W)$$
is the Dirac operator of $Y$ induced by the spin connection $B$ on $W$, angle brackets $\langle$,$\rangle here denote the real inner product on W$ (real part of the Hermitian inner product), and Tr denotes the map induced by taking traces of matrices in $\operatorname{ad}(W)$. If $u \in \mathcal{G}$, then
$$\operatorname{cs}(B, \Psi)-\operatorname{cs}(u(B, \Psi))=8 \pi^{2}\left\langle c_{1}(W) \cup[u],[Y]\right\rangle,$$
where $[u]$ denotes the one-dimensional cohomology class obtained by pulling back the fundamental class on $S^{1}$. Thus, in general cs descends as a well-defined circle-valued function on $\mathcal{B}(W)$. When, for example $c_{1}(W)$ is a torsion class, cs is naturally $\mathbb{R}$-valued.

When $\mathbf{D}_{B}$ is self-adjoint, a property which depends only on ° ∇ , a point $(B, \Psi) \in \mathcal{B}(W)$ is a critical point for this functional, i.e. the gradient vector field $\nabla \mathrm{cs}$ vanishes at $(B, \Psi)$, if and only if $(B, \Psi)$ satisfies
$$\begin{array}{r}
* \operatorname{Tr}\left(F_{B}\right)-i \tau(\Psi)=0 \\
\mathbf{D}_{B} \Psi=0,
\end{array}$$
the three-dimensional Seiberg-Witten equations. Here
$$\tau: \Gamma(Y, W) \rightarrow \Omega^{1}(Y, \mathbb{R})$$
is adjoint to Clifford multiplication, in the sense that for all $b \in \Omega^{1}(Y, \mathbb{R})$, $\Psi \in \Gamma(Y, W)$, we have
$$\frac{1}{2}\langle i b \cdot \Psi, \Psi\rangle_{W}=-\langle b, \tau(\Psi)\rangle_{\Lambda^{1}} .$$

The critical points for ∇cs in $\mathcal{B}(W)$, the Seiberg-Witten moduli space in $W$ is denoted $\mathcal{M}_{s w}(W)$, and its irreducible part is denoted $\mathcal{M}_{s w}^{*}(W)$. The Seiberg-Witten moduli space, $\mathcal{M}_{s w}$ is the union over all distinct $\operatorname{Spin}_{\mathrm{c}}(3)$ structures $W$ of the various moduli spaces $\mathcal{M}_{s w}(W)$.

Given a Riemannian four-manifold $X$ carrying a $\operatorname{Spin}_{\mathrm{c}}(4)$-structure $\left(W^{+}, W^{-}, \rho\right)$ we can consider the four-dimensional Seiberg-Witten equations
$$\begin{array}{r}
\operatorname{Tr} F_{A}^{+}-i \sigma(\Phi)=0 \\
\mathbf{D}_{A} \Phi=0
\end{array}$$
where $(A, \Phi) \in \mathcal{A}\left(W^{+}\right) \oplus \Gamma\left(X, W^{+}\right)$. When $X=\mathbb{R} \times Y$ (as Riemannian manifolds) is endowed with the $\operatorname{Spin}_{\mathrm{c}}(4)$-structure induced by $\pi^{*}(W)$, these equations are gauge equivalent to the (upward) gradient flow lines for cs.

\section*{5. Circle invariance of Solutions.}

In this section, we prove Theorem 1. Throughout the section,
$$\pi: Y \rightarrow \Sigma$$
will denote the Seifert fibered space obtained as the unit circle bundle of an orbifold line bundle $N$ over $\Sigma$. Unless explicitly stated otherwise, we assume that $\operatorname{deg}(N) \neq 0$.

\subsection*{5.1. Line Bundles over Seifert Fibered Spaces.}

Orbifold line bundles $E$ over $\Sigma$ induce in a natural way (by "pull-back," $\pi^{*}(E)$ ) line bundles over $Y$. This does not give a faithful correspondence between isomorphism classes, except when $Y \cong|\Sigma| \times S^{1}$ (see Remark 2.14). However, if one equips the line bundle with a connection, one gets a faithful correspondence, as described below (Proposition 5.3).

In order to state properly the image of the correspondence, we must introduce some notions.

Definition 5.1. Let $E$ be a line bundle over $Y$. A connection $A$ in $E$ is said to have trivial fiberwise holonomy if for any $x \in \Sigma-\left\{x_{i}\right\}_{i=1}^{n}$, the holonomy of $A$ around $\pi^{-1}(x), \operatorname{Hol}_{\mathrm{A}} \pi^{-1}(\mathrm{x})$, is trivial.

When the curvature two-form $F(A)$ pulls up from $\Sigma$, i.e. $\iota_{\frac{\partial}{\partial \varphi}} F_{A}=0$, so that $F_{A}=\pi^{*}\left(F_{0}\right)$ (here $\frac{\partial}{\partial \varphi}$ is an infinitesimal generator for the circle action
on $Y$ ), the holonomy around a (generic) fiber is independent of the particular fiber chosen. This is seen by connecting any two points $x, y \in \Sigma-\left\{x_{i}\right\}_{i=1}^{n}$ by a path $\gamma$ missing the $x_{i}$, considering its preimage, a cylinder, and noticing that
$$\operatorname{Hol}_{A} \pi^{-1} x\left(\operatorname{Hol}_{A} \pi^{-1} y\right)^{-1}=e^{\int_{\pi^{-1} \gamma} F(A)}=e^{\int_{\gamma} F_{0}}=1 .$$
Thus, we have the following:
Lemma 5.2. A connection has trivial fiberwise holonomy iff its curvature form pulls up from $\Sigma$, and there is a point $x \in \Sigma-\left\{x_{i}\right\}_{i=1}^{n}$ whose fiber has trivial holonomy.

Now we can state the correspondence:
Proposition 5.3. There is a natural one-to-one correspondence between pairs (orbifold) bundles-with-connection over $\Sigma$ and (usual) bundles-withconnection over $Y$, whose curvature forms pull up from $\Sigma$ and whose fiberwise holonomy is trivial. Furthermore, this correspondence induces an identification between orbifold sections of the orbifold bundle over $\Sigma$ with fiberwise constant sections of its pull-back over $Y$.

Remark 5.4. It is important that the triviality of the fiberwise holonomy be tested over a point not in $\left\{x_{i}\right\}_{i=1}^{n}$. The holonomy over the exceptional circles $\pi^{-1}\left(x_{i}\right)$ is not expected to be trivial; indeed, for an orbifold line bundle $E$ the holonomy around the exceptional circle $\pi^{-1}\left(x_{i}\right)$ is multiplication by $e^{\frac{2 \pi \mathbf{i}}{\alpha_{i}}\left(\beta_{i}(E)-\beta_{i}(Y)\right)}$.

Proof. We first discuss the correspondence between the bundles-with-connection. Given a bundle-with-connection over $\Sigma$, pull-back clearly induces a bundle-with-connection over $Y$ with trivial fiberwise holonomy. To see that the correspondence is one-to-one, we invert this construction.

Suppose we have a line bundle $E$ over $Y$ with connection $A$ with trivial fiberwise holonomy. We must specify, over each $U_{i}$, a $\mathbb{Z} / \alpha_{i} \mathbb{Z}$-equivariant line bundle. Notice that over $U_{i}$, the projection $\pi$ is modeled on
$$\pi_{i}: D \times_{\mathbb{Z} / \alpha_{i} \mathbb{Z}} S^{1} \rightarrow D /\left(\mathbb{Z} / \alpha_{i} \mathbb{Z}\right),$$
so the local charts $\phi_{i}: D \rightarrow D /\left(\mathbb{Z} / \alpha_{i} \mathbb{Z}\right)$ defining the orbifold structure on $\Sigma$ can be factored through $\pi_{i}$, using the local trivializations for the orbifold line bundle defining the Seifert fibered space. Any two such lifts
$$\tau, \tau^{\prime}: D \rightarrow D \times_{\mathbb{Z} / \alpha_{i} \mathbb{Z}} S^{1}$$
differ by the action of the circle; i.e. there is a function
$$f: D \rightarrow S^{1}$$
uniquely specified by the property that
$$\tau(w)=\tau^{\prime}(w) f(w) .$$
This observation allows us to use the connection $A$ to identify canonically the bundles $\tau^{*}(E)$ and $\tau^{\prime *}(E)$ over $D$. The identification is obtained by taking a homotopy from $f$ to the constant map $w \mapsto 1 \in S^{1}$ and then using parallel transport of $A$ along the tracks of the homotopy. This identification is canonical, in the sense that is independent of the particular homotopy connecting $f$ with the constant map. This is true because any two identifications differ by parallel transport around the fiber circles (or, more precisely, curves in the fiber of $\pi$ which are homologous to a generic fiber via a cylinder projecting to a path in $\Sigma$ ) whose holonomy was assumed to be always trivial.

With these observations in place, we can define our orbifold bundle by defining it over $U_{i}$ to be $\tau^{*}(E)$, for some lift $\tau$. The $\mathbb{Z} / \alpha_{i} \mathbb{Z}$ action is induced by the above construction, observing that if $\tau$ is a lift of the projection map $\pi_{i}$, so is
$$w \mapsto \tau\left(e^{\frac{2 \pi \mathbf{i} a}{\alpha_{i}}} w\right),$$
a map we will call $\tau_{a}$. Thus, we have an identification of $\tau_{a}^{*}(E)$ with $\tau^{*}(E)=$ $\tau_{0}^{*}(E)$, giving us the maps covering the $\mathbb{Z} / \alpha_{i} \mathbb{Z}$ action on $D$. The fact that this map actually induces a $\mathbb{Z} / \alpha_{i} \mathbb{Z}$ action on $\tau^{*}(E)$ (i.e. that its $\alpha_{i}^{t h}$ power is trivial) follows from the uniqueness in the above construction, and the observation that $\tau_{0}=\tau_{\alpha_{i}}$.

The statement about the correspondence between sections follows immediately from the definitions. \(\square\)

\subsection*{5.2. The geometry of the Seifert fibered space.}

We give $Y$ the metric
$$g_{Y}=\eta^{2}+\pi^{*}\left(g_{\Sigma}\right),$$
where $i \eta$ is a connection form for a constant curvature connection on $Y$, and $g_{\Sigma}$ is a constant curvature metric on $\Sigma$. The global 1-form $\eta$ induces a reduction in the structure group of $T Y$ to $S O(2)$; the kernel of $\eta$ is naturally
identified with the pull-back of the orbifold tangent bundle of $\Sigma$, so that we have orthogonal splittings
$$T Y \cong \mathbb{R} \frac{\partial}{\partial \varphi} \oplus \pi^{*}(T \Sigma) \quad \text { and } \quad T^{*} Y \cong \mathbb{R} \eta \oplus \pi^{*}\left(T^{*} \Sigma\right)$$
where $\frac{\partial}{\partial \varphi}$ is the vector field dual to $\eta$. Note that for any vector field $X$ dual to the pull-back of a 1-form from $\Sigma$, we have that
$$\left[X, \frac{\partial}{\partial \varphi}\right]=0 .$$
$T^{*} Y$ can be naturally given a connection compatible with this reduction. Letting $\nabla_{\Sigma}$ denote the Levi-Civita connection on $T^{*} \Sigma$, we can give $T^{*} Y$ the connection ${ }^{\circ} \nabla=d \oplus \pi^{*}\left(\nabla_{\Sigma}\right)$; i.e. the $S O(3)$-connection which satisfies
$${ }^{\circ} \nabla \eta=0,$$
and, for any $\theta \in \Omega^{1}(\Sigma, \mathbb{R})$,
$${ }^{\circ} \nabla \pi^{*}(\theta)=\pi^{*}\left(\nabla_{\Sigma} \theta\right) .$$

Let ${ }^{\circ} \widehat{\nabla}$ be the Levi-Civita connection on $Y$. The purpose of the next lemma is to compare ${ }^{\circ} \nabla$-spinorial connections on $W$ with ${ }^{\circ} \widehat{\nabla}$-spinorial connections.

Let $\xi$ denote the constant defined by
$$d \eta=2 \xi \mu_{\Sigma},$$
where $\mu_{\Sigma}$ is the volume form on $\Sigma$. By Chern-Weil theory, we see that
$$\xi=-\frac{\pi \operatorname{deg}(N)}{\operatorname{Vol}(\Sigma)} .$$

Then, we have the following:
Lemma 5.5. Let $(W, \rho)$ be a $\operatorname{Spin}_{\mathrm{c}}(3)$ structure over $Y$, and $\nabla$ and $\widehat{\nabla}$ be a pair of connections in $W$ which are spinorial with respect to °V and ° $\widehat{\nabla}$ respectively, with $\operatorname{Tr}(\nabla)=\operatorname{Tr}(\widehat{\nabla})$. Then, for any $b \in \Omega^{1}(Y, \mathbb{R})$, we have
$$\widehat{\nabla}_{b^{b}}=\nabla_{b^{b}}+\xi\left(\frac{1}{2} \rho(b)-\langle b, \eta\rangle \rho(\eta)\right),$$
where $b^{\mathrm{b}}$ denotes the vector field which is $g_{Y}$-dual to $b$. If $\mathbf{D}$ and $\widehat{\mathbf{D}}$ are the Dirac operators ∇ and $\widehat{\nabla}$ induce on $W$, then
$$\widehat{\mathbf{D}}=\mathbf{D}-\frac{1}{2} \xi .$$

Proof. Pick an orthonormal coframe on a patch of $Y$
$$\left\{\theta^{0}, \theta^{1}, \theta^{2}\right\}$$
so that $\theta^{0}=\eta$, and $\left\{\theta^{1}, \theta^{2}\right\}$ is pulled back from an orthonormal coframe on $\Sigma$. The connection matrix $\left(\omega_{j}^{i}\right)$ for the covariant derivative $\hat{\nabla}$ with respect to this coframe is given by
$$\left(\begin{array}{ccc}
0 & -\xi \theta^{2} & \xi \theta^{1} \\
\xi \theta^{2} & 0 & \xi \theta^{0}+\omega_{2}^{1} \\
-\xi \theta^{1} & -\xi \theta^{0}-\omega_{2}^{1} & 0
\end{array}\right),$$
which is an easy consequence of Cartan's structural equations,
$$d \theta^{i}=\sum_{j} \omega_{j}^{i} \wedge \theta^{j}$$
and where $\omega_{2}^{1}$ is the (pull-back of the) connection 1-form for the Levi-Civita connection on $\Sigma$. (Notice that the connection matrices here are for $T^{*} Y$, which are off by a sign from the connection matrices for $T Y$.) Thus,
$${ }^{\circ} \widehat{\nabla}-{ }^{\circ} \nabla=\left(\begin{array}{ccc}
0 & -\xi \theta^{2} & \xi \theta^{1} \\
\xi \theta^{2} & 0 & \xi \theta^{0} \\
-\xi \theta^{1} & -\xi \theta^{0} & 0
\end{array}\right) .$$
In local coordinates, Formula 4.2 says that
$$\begin{aligned}
\widehat{\nabla}-\nabla & =\frac{1}{4} \sum \omega_{j}^{i} \otimes \rho\left(\theta^{i} \wedge \theta^{j}\right) \\
& =\frac{1}{2} \xi\left(-\theta^{0} \otimes \rho\left(\theta^{0}\right)+\theta^{1} \otimes \rho\left(\theta^{1}\right)+\theta^{2} \otimes \rho\left(\theta^{2}\right)\right) \rho\left(\mu_{Y}\right),
\end{aligned}$$
from which both formulas follow easily. \(\square\)

Remark 5.6. As a consequence of the above result, we have that the Dirac operator $\mathbf{D}$ is self-adjoint, since both $\widehat{\mathbf{D}}$ and multiplication by a real scalarvalued function are self-adjoint.

Corollary 5.7. The anticommutator of the Dirac operator with Clifford multiplication by a 1-form is given by the formula
$$\{\mathbf{D}, \rho(b)\}=-\rho((* d+d *) b)-2 \nabla_{b^{b}}+2 \xi\langle b, \eta\rangle .$$

Proof. This follows immediately from the analogous formula for the Levi-Civita Dirac operator (see for example [4]):
$$\{\widehat{\mathbf{D}}, \rho(b)\}=\rho((* d+d *) b)-2 \widehat{\nabla}_{b^{b}}$$
together with the Lemma. \(\square\)

\subsection*{5.3. Weitzenböck Decomposition of the Dirac Operator.}

Given a $\operatorname{Spin}_{\mathrm{c}}(3)$-structure $(W, \rho)$ on $Y$, let ∇ be a ° $\nabla$-spinorial connection on $W$, where ${ }^{\circ} \nabla$ is the reducible connection considered above. Corresponding to the splitting of $T^{*} Y$, there is a canonical decomposition of the Dirac operator into two terms
$$\mathbf{D}=\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}+\mathrm{D}_{2},$$
which can be taken as the defining equation for $\mathrm{D}_{2}$. Since (taking $L^{2}$-adjoint)
$$\left(\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}\right)^{*} \psi=\nabla_{\frac{\partial}{\partial \varphi}} \eta \cdot \psi=\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}} \psi+\left(\nabla_{\frac{\partial}{\partial \varphi}} \eta\right) \cdot \psi=\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}} \psi$$
(here we have used Equation 5.2, together with spinoriality, Equation 4.1), we have decomposed the Dirac operator as a sum of self-adjoint operators. Correspondingly, we can give a Weitzenböck-type decomposition of the square of the Dirac operator:
$$\mathbf{D}^{2}=\left(\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}\right)^{2}+\left(\mathrm{D}_{2}\right)^{2}+\left\{\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}, \mathrm{D}_{2}\right\},$$
as a sum of three operators, the first two of which are manifestly non-negative. Since the sum of the first two terms on the right has the same symbol as $\mathbf{D}^{2}$, the third term on the right is a priori a first-order operator. In fact, it turns out that this third term is a zeroth order operator, which can be written in terms of Clifford multiplication, as follows.

Let
$$\Pi_{\eta^{\perp}}: T^{*} Y \rightarrow \eta^{\perp} \subset T^{*} Y$$
denote orthogonal projection of $T^{*} Y$ to the space perpendicular to $\eta$, a subbundle which is naturally isomorphic to $\pi^{*}\left(T^{*} \Sigma\right)$. Then we have the following:

Lemma 5.8. The cross-term appearing Formula 5.8 is a zeroth-order operator. More precisely,
$$\left\{\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}, \mathrm{D}_{2}\right\}=-\frac{1}{2} \rho\left(\Pi_{\eta^{\perp}} * \operatorname{Tr} F_{B}\right) .$$
Proof. Let $\theta^{1}, \theta^{2}$ be a pair of orthonormal covectors over a neighborhood of $Y$ pulled back from (a neighborhood in) $\Sigma$, and $e_{1}, e_{2}$ their duals. Then we can write $\mathrm{D}_{2}=\theta^{1} \cdot \nabla_{e_{1}}+\theta^{2} \cdot \nabla_{e_{2}}$, so
$$\left\{\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}, \mathrm{D}_{2}\right\}=\eta \cdot \theta^{1} \cdot\left[\nabla_{\frac{\partial}{\partial \varphi}}, \nabla_{e_{1}}\right]+\eta \cdot \theta^{2} \cdot\left[\nabla_{\frac{\partial}{\partial \varphi}}, \nabla_{e_{2}}\right] .$$
Here we have used the properties of ∇ from Equations 5.2, 5.3, and 4.1, together with the Clifford relations $\eta \cdot \theta^{i} \cdot=-\theta^{i} \cdot \eta \cdot$. Now, for general vector fields $u$ and $v$,
$$\left[\nabla_{u}, \nabla_{v}\right]-\nabla_{[u, v]}=F(u, v) ;$$
so using Equation 5.1, we see that
$$\left\{\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}, \mathrm{D}_{2}\right\}=\eta \cdot \theta^{1} \cdot \widehat{F}_{B}\left(\frac{\partial}{\partial \varphi}, e_{1}\right)+\eta \cdot \theta^{2} \cdot \widehat{F}_{B}\left(\frac{\partial}{\partial \varphi}, e_{2}\right) .$$
Since ${ }^{\circ} \nabla$ pulls up from $\Sigma$, we have that the action of $\widehat{F}_{B}\left(\frac{\partial}{\partial \varphi}, e_{i}\right)$ for $i=$ 1,2 must commute with Clifford multiplication, hence it must be a scalar endomorphism, so
$$\widehat{F}_{B}\left(\frac{\partial}{\partial \varphi}, e_{i}\right)=\frac{1}{2} \operatorname{Tr} F_{B}\left(\frac{\partial}{\partial \varphi}, e_{i}\right) .$$
So, by definition, we see that
$$\left\{\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}, \mathrm{D}_{2}\right\}=\frac{1}{2} \rho\left(\eta \wedge\left(\iota_{\frac{\partial}{\partial \varphi}} \operatorname{Tr}\left(F_{B}\right)\right)\right) .$$
The lemma now follows, since for any two-from $\omega$, we have
$$\Pi_{\eta^{\perp}} * \omega=* \eta \wedge\left(\iota_{\frac{\partial}{\partial \varphi}} \omega\right),$$
and
$$\rho(\omega)=-\rho(* \omega),$$
by the assumption that $\rho\left(\mu_{Y}\right)$ is the identity map on $W$. \(\square\)

\subsection*{5.4. The Squaring Map.}

Since the square of Clifford multiplication by $\pi^{*}\left(\mu_{\Sigma}\right)$ is the identity map, this operator breaks $W$ into its (orthogonal) +1 and -1 eigenbundles.

Definition 5.9. $S^{+}$(resp. $S^{-}$) is the bundle of spinors $\Psi$ satisfying
$$i \pi^{*}\left(\mu_{\Sigma}\right) \cdot \Psi=\Psi \quad\left(\text { resp. } \quad i \pi^{*}\left(\mu_{\Sigma}\right) \cdot \Psi=-\Psi\right) .$$

Clifford multiplication by $\eta$ preserves the splitting $W \cong S^{+} \oplus S^{-}$, so Clifford multiplication by anything in $\eta^{\perp} \cong \pi^{*}\left(T^{*} \Sigma\right)$ must reverse it. Indeed, it is straightforward to verify that Clifford multiplication induces an isometry between $\pi^{*}\left(T^{*} \Sigma\right)$ and the skew-symmetric endomorphisms of $S^{ \pm}$ which reverse chirality or, equivalently, it induces an isometry
$$\pi^{*}\left(T^{*} \Sigma\right) \cong \operatorname{Hom}_{\mathbb{C}}\left(S^{+}, S^{-}\right) .$$

We will now investigate the manner in which the bilinear map $\tau$ of Equation 4.6 behaves under this splitting.

Lemma 5.10. Let $\alpha \in S^{+}, \beta \in S^{-}$be spinors. Then,
$$\begin{aligned}
\langle i \tau(\alpha+\beta), \eta\rangle & =i \frac{1}{2}\left(|\alpha|^{2}-|\beta|^{2}\right) \\
\Pi_{\eta^{\perp}} i \tau(\alpha+\beta) & =-\left(\alpha \otimes \beta^{*}+\beta \otimes \alpha^{*}\right) .
\end{aligned}$$
Proof. To see the first equation,
$$\begin{aligned}
\langle\eta, \tau(\alpha+\beta)\rangle & =-\langle i \rho(\eta)(\alpha+\beta), \alpha+\beta\rangle \\
& =\langle i \rho(* \eta)(\alpha+\beta), \alpha+\beta\rangle \\
& =|\alpha|^{2}-|\beta|^{2} .
\end{aligned}$$

For the second, we have
$$\begin{aligned}
\left\langle\tau(\alpha+\beta), i\left(\alpha^{*} \otimes \beta+\beta^{*} \otimes \alpha\right)\right\rangle & =\frac{1}{2}\left\langle\left(\alpha^{*} \otimes \beta+\beta^{*} \otimes \alpha\right)(\alpha+\beta), \alpha+\beta\right\rangle \\
& =|\alpha|^{2}|\beta|^{2} .
\end{aligned}$$
The result follows from this, together with the fact that the transformation $i\left(\alpha^{*} \otimes \beta+\beta^{*} \otimes \alpha\right) \in \operatorname{Hom}_{\mathbb{C}}\left(S^{+}, S^{-}\right)$has norm $|\alpha||\beta|$. \(\square\)

The Kähler structure on $\Sigma$ induces a canonical (orbifold) $\operatorname{Spin}_{\mathrm{c}}(2)$ structure (see [33],[25]), $\mathbb{C} \oplus K_{\Sigma}^{-1}$, with Clifford module structure given by the symbol of $\sqrt{2}\left(\bar{\partial}+\bar{\partial}^{*}\right)$. This in turn endows $Y$ with a canonical $\operatorname{Spin}_{c}(3)$ structure with $W_{c}=\mathbb{C} \oplus K_{\Sigma}^{-1}$, given by defining $\left.\rho(\eta)\right|_{S^{ \pm}}= \pm i$. Moreover, $W_{c}$ has a canonical ${ }^{\circ} \nabla$-spinorial connection $\nabla_{c}$, whose associated Dirac operator is given by
$$(\alpha, \beta) \mapsto\left(i \frac{\partial}{\partial \varphi} \alpha+\sqrt{2} \bar{\partial}^{*} \beta, \sqrt{2} \bar{\partial} \alpha-i \frac{\partial}{\partial \varphi} \beta\right) .$$
This $\operatorname{Spin}_{\mathrm{c}}(3)$-structure gives rise to a one-to-one correspondence between the Hermitian line bundles $E$ over $Y$ and the $\operatorname{Spin}_{\mathrm{c}}(3)$ structures over $Y$ under $E \mapsto E \otimes W_{c}$, a $\operatorname{Spin}_{\mathrm{c}}(3)$ structure whose $S^{+}$-bundle (in the sense of Definition 5.9) is $E$. Indeed, tensor product with ( $W_{c}, \nabla_{c}$ ) induces an identification between $\mathcal{A}(E)$, the space of Hermitian connections in a line bundle $E$, and $\mathcal{A}\left(W_{c} \otimes E\right)$, the space of ${ }^{\circ} \nabla$-spinorial connections in the $\operatorname{Spin}_{\mathrm{c}}(3)$ structure $W_{c} \otimes E$.

\subsection*{5.5. The Vanishing Spinor Argument.}

We recall the Kähler vortex equations over $\Sigma$. Given a Hermitian orbifold line bundle $E_{0}$ over $\Sigma$, let $\alpha_{0}, \beta_{0}$, be orbifold sections in $\Gamma\left(\Sigma, E_{0}\right)$ and $\Gamma\left(\Sigma, K_{\Sigma}^{-1} \otimes E_{0}\right)$ respectively, and $B_{0}$ be a compatible orbifold connection in $E_{0}$. The triple $\left(B_{0}, \alpha_{0}, \beta_{0}\right)$ is called a Kähler vortex in $E_{0}$ if it satisfies the equations
$$\begin{aligned}
& 2 F_{B_{0}}-F_{K_{\Sigma}}=i\left(\left|\alpha_{0}\right|^{2}-\left|\beta_{0}\right|^{2}\right) \mu_{\Sigma} \\
& \bar{\partial}_{B_{0}} \alpha_{0}=0 \text { and } \bar{\partial}_{B_{0}}^{*} \beta_{0}=0 \\
& \alpha_{0}=0 \text { or } \\
& \beta_{0}=0 .
\end{aligned}$$
Once again, these equations are preserved by the gauge group of unitary transformations of $E_{0}$, so we can form a moduli space of vortices, written $\mathcal{M}_{v}(\Sigma)$.

The pull-back of a Kähler vortex over $\Sigma$ is naturally the solution of the Seiberg-Witten Equations 4.4 and 4.5 over $Y$. The holomorphicity conditions on $\alpha_{0}$ and $\beta_{0}$, along with the their circle invariance, ensure that the pull-back spinor is harmonic, according to Equation 5.12. As explained in Lemma 5.10, the squaring map is equivalent to the pair of Equations 5.10 and 5.11, the first of which is Equation 5.13, the second is automatically satisfied because both sides vanish: the left hand side because $F_{B}$ pulls up from $\Sigma$, the right because of Equation 5.15.

Since a gauge transformation on $E_{0}$ pulls back to a gauge transformation of $W$, we get a well-defined map on the level of moduli spaces
$$\pi^{*}: \mathcal{M}_{v}(\Sigma) \rightarrow \mathcal{M}_{s w}(Y) .$$

Letting $\mathcal{M}_{v}^{*}(\Sigma) \subset \mathcal{M}_{v}(\Sigma)$ be the subspace represented by vortices for which $\alpha_{0}$ and $\beta_{0}$ do not simultaneously vanish, and $\mathcal{M}_{s w}^{*}(Y) \Subset \mathcal{M}_{s w}(Y)$ denote the moduli space of irreducible critical points, we will prove the following:

Theorem 4. The pull-back map $\pi^{*}$ induces a diffeomorphism between $\mathcal{M}_{v}^{*}(\Sigma)$ and $\mathcal{M}_{s w}^{*}(Y)$.

Remark 5.11. Note that the spaces are identified as differentiable manifolds, not as "moduli spaces"; i.e. whereas $\mathcal{M}_{v}^{*}(\Sigma)$ is always cut out by a map whose differential is surjective (according to Theorem 5), $\mathcal{M}_{s w}^{*}(Y)$ is cut out by a map which always has index zero, as it is cut out by the gradient of a function (which always has a self-adjoint linearization on its critical set).

The proof occupies the rest of this subsection, and Subsection 5.6. As a first step, we show that $\pi^{*}$ induces a homeomorphism. First, we see that $\pi^{*}$ is injective. That is, if a gauge transformation $u$ preserves an irreducible solution which pulls back from $\Sigma$, then it must actually be the pull-back of a gauge transformation over $E_{0}$. Viewing $u$ as a section of $\operatorname{End}\left(\pi^{*}\left(E_{0}\right)\right)=$ $\pi^{*}\left(\operatorname{End}\left(E_{0}\right)\right)$, we have, by the definition of the covariant derivative on the endomorphism bundle, that
$$\left(\nabla_{\frac{\partial}{\partial \varphi}} u\right) \Psi=\left[\nabla_{\frac{\partial}{\partial \varphi}}, u\right] \Psi=0 .$$
But $\Psi \neq 0$ over a dense open subset of $\Sigma$, so $\nabla_{\frac{\partial}{\partial \varphi}} u=0$ over all of $Y$. Thus $u$ is the pull-back of a section in $\Gamma\left(\Sigma, \operatorname{End}\left(E_{0}\right)\right)$, by the correspondence in Proposition 5.3.

We will now show that $\left.\pi^{*}\right|_{\mathcal{M}_{v}^{*}} ^{*}$ surjects onto $\mathcal{M}_{s w}^{*}$. Consider any solution $(B, \Psi)$. As above we can decompose $\Psi=\alpha+\beta$ into its components in $S^{ \pm}$.

Combining Equation 5.8, Equation 4.5, and Equation 5.8, we get that
$$0=\left(\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}\right)^{2} \Psi+\left(\mathrm{D}_{2}\right)^{2} \Psi-\frac{1}{2} \rho\left(\Pi_{\eta^{\perp}} * \operatorname{Tr} F_{B}\right) \Psi$$
Taking the inner product of the above with $\Psi$, and integrating over $Y$, we get
$$0=\left|\nabla_{\frac{\partial}{\partial \varphi}} \Psi\right|^{2}+\left|\mathrm{D}_{2}^{2} \Psi\right|^{2}-\frac{1}{2}\left\langle\rho\left(\Pi_{\eta^{\perp}} * \operatorname{Tr} F_{B}\right) \Psi, \Psi\right\rangle .$$

Clearly the first two terms are individually non-negative. To analyze the third term, combine

Equation 4.4, with its interpretation from Lemma 5.10, to get that
$$\begin{aligned}
-\frac{1}{2}\left\langle\rho\left(\Pi_{\eta^{\perp}} F_{B}\right) \Psi, \Psi\right\rangle & =-\frac{1}{2}\langle i \tau(\alpha+\beta) \alpha, \beta\rangle \\
& =\frac{1}{2}\left\langle\left(\alpha \otimes \beta^{*}+\beta \otimes \alpha^{*}\right)(\alpha+\beta), \alpha+\beta\right\rangle \\
& =|\alpha|^{2}|\beta|^{2},
\end{aligned}$$
another manifestly non-negative quantity, which, by Equation 5.16 must vanish identically.

Thus, we can draw the following conclusions
$$\begin{aligned}
\Pi_{\eta^{\perp}}\left(* \operatorname{Tr} F_{B}\right) & =0, \\
\nabla_{\frac{\partial}{\partial \varphi}} \alpha=\nabla_{\frac{\partial}{\partial \varphi}} \beta & =0 \\
|\alpha||\beta| & =0 .
\end{aligned}$$
Since $\Psi \not \equiv 0$, one of $\alpha, \beta \not \equiv 0$, so Equation 5.18 shows that the fiberwise holonomy in $E_{0}$ must be trivial. By the correspondence in Proposition 5.3, which we can apply thanks to Equations 5.17 and 5.18, we see that the sections $\alpha$ and $\beta$ of $S^{ \pm}$, together with the connection $B$, correspond to orbifold sections $\alpha_{0}, \beta_{0}$ of the orbifold bundles $E_{0}$ and $K_{\Sigma}^{-1} \otimes E_{0}$, together with the connection $B_{0}$.

Now, the Equation 4.5 together with Equation 5.18 gives us Equation 5.14. The unique continuation theorem for the $\bar{\partial}$ operator, together with Equation 5.19 gives us Equation 5.15.

To get an identification between actual moduli spaces, we need to show that $\pi^{*}$ identifies the kernels, at each point in the respective moduli spaces, of the linearizations of the maps which cut out those moduli spaces.

\subsection*{5.6. The Linearizations.}

We wish to describe the linearization of the map $\nabla \mathrm{cs}$, which cuts out the moduli space $\mathcal{M}_{s w} \subset \mathcal{B}$. First, consider the bilinear map
$$\widehat{\tau}: W \otimes W \rightarrow\left(\Omega^{1} \oplus \Omega^{3}\right)(Y, \mathbb{R})$$
characterized by the property that for any $b \in\left(\Omega^{1} \oplus \Omega^{3}\right)(Y, \mathbb{R})$ and $\psi_{1}, \psi_{2} \in$ $\Gamma(Y, W)$,
$$\left\langle i \rho(b) \psi_{1}, \psi_{2}\right\rangle_{W}=-\left\langle b, \widehat{\tau}\left(\psi_{1}, \psi_{2}\right)\right\rangle_{\Lambda^{1} \oplus \Lambda^{3}} .$$

The $\Omega^{1}$ component of $\widehat{\tau}$ is the bilinear form associated to the quadratic map $\tau$, and the $\Omega^{3}$ component of is the imaginary part of the Hermitian inner product on $W$. Thus, the linearization of $\nabla \mathrm{cs}$ at a solution $(B, \Psi)$ can be described as a map
$$D_{[B, \Psi]} \nabla \operatorname{cs}: \Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(Y, W) \rightarrow \Omega^{3}(Y, i \mathbb{R}) \oplus \Omega^{1}(Y, i \mathbb{R}) \oplus \Gamma(Y, W),$$
given by the formula:
$$(b, \psi) \mapsto\left((* d+d *) b-i \widehat{\tau}(\Psi, \psi),\left(\mathbf{D}_{B} \psi\right)+b \cdot \Psi\right) .$$

The vortex moduli space, on the other hand, can be thought of as the zero set of a map defined on
$$\begin{gathered}
\mathcal{B}_{0}^{ \pm}=\mathcal{A}_{0} \times \Gamma\left(\Sigma, S^{ \pm}\right) / \mathcal{G}, \\
\mathcal{V}^{ \pm}: \mathcal{B}_{0}^{ \pm} \rightarrow i \Lambda^{2}(\Sigma) \times_{\mathcal{G}} \Gamma\left(\Sigma, S^{\mp}\right), \\
\mathcal{V}^{ \pm}\left(B_{0}, \Psi\right)=\left(F_{B_{0}} \pm i|\Psi|^{2},\left(\mathrm{D}_{2 B_{0}}\right) \Psi\right) .
\end{gathered}$$

Pulling back gives a map from the vortex configuration space to the Seiberg-Witten configuration space:
$$\pi^{*}: \mathcal{B}_{0}^{ \pm} \rightarrow \mathcal{B} .$$
We have shown that $\mathcal{M}_{s w}^{*}$ is contained in the image of this map; indeed, that $\mathcal{M}_{s w}^{*}=\pi^{*} \mathcal{M}_{v}^{*}$. We will now show that $\pi^{*}$ naturally induces identifications
$$\operatorname{Ker} D_{(B, \Psi)} \nabla \operatorname{cs}=\operatorname{Ker} D_{\left(\pi^{*}\right)^{-1}(B, \Psi)} \mathcal{V}^{ \pm},$$
when $(B, \Psi) \in \mathcal{M}_{s w}^{*}$. More explicitly, this is saying that for any $(B, \Psi) \in$ $\mathcal{M}_{s w}^{*}$, if $(b, \psi)$ satisfies
$$\mathbf{D}_{B} \psi+b \cdot \Psi=0$$
$$(* d+d *) b-i \widehat{\tau}(\Psi, \psi)=0,$$
then
$$\begin{aligned}
\Psi \in \Gamma\left(Y, S^{ \pm}\right) & \Longrightarrow \psi \in \Gamma\left(Y, S^{ \pm}\right) . \\
\nabla_{\frac{\partial}{\partial \varphi}} \psi & =0 \\
b & \in \pi^{*}\left(\Omega^{1}(\Sigma, i \mathbb{R})\right)
\end{aligned}$$

We will assume that $\Psi \in \Gamma\left(Y, S^{+}\right)$; the case where $\Psi \in \Gamma\left(Y, S^{-}\right)$is analogous. Applying $\mathbf{D}_{B}$ to Equation 5.22, and applying Equation 5.7, together with the fact that $\mathbf{D}_{B} \Psi=0$, we see that
$$\begin{aligned}
\mathbf{D}_{B} \mathbf{D}_{B} \psi+\mathbf{D}_{B}(b \cdot \Psi) & =\mathbf{D}_{B} \mathbf{D}_{B} \psi+\mathbf{D}_{B}(b \cdot \Psi) \\
& =\mathbf{D}_{B}^{2} \psi-(* d+d *) b \cdot \Psi-2 \nabla_{b^{b}} \Psi+2 \xi\langle b, \eta\rangle \eta \cdot \Psi .
\end{aligned}$$
Let $\psi=\alpha+\beta$ be the decomposition of $\psi$ in $\Gamma\left(Y, S^{ \pm}\right)$. We will show that $\beta=0$, by taking the inner product of the above equation with $\beta$ and making four observations.
\begin{itemize}
\item[1.] By Equation 5.17 combined with Equation 5.8, we see that $\mathbf{D}_{B}^{2}$ preserves the grading on $S^{ \pm}$, so
$$\left\langle\mathbf{D}_{B}^{2} \psi, \beta\right\rangle=\left\langle\mathbf{D}_{B}^{2} \beta, \beta\right\rangle=\left\langle\left(\eta \cdot \nabla_{\frac{\partial}{\partial \varphi}}\right)^{2} \beta, \beta\right\rangle+\left\langle\left(\mathrm{D}_{2}\right)^{2} \beta, \beta\right\rangle .$$
\item[2.] Combining Equation 5.23 with the definition of $\widehat{\tau}$, we see that
$$\begin{aligned}
\langle-(* d+d *) b \cdot \Psi, \beta\rangle & =-\langle i \widehat{\tau}(\Psi, \psi) \cdot \Psi, \beta\rangle \\
& =\langle\widehat{\tau}(\Psi, \psi), \widehat{\tau}(\Psi, \beta)\rangle \\
& =\langle\widehat{\tau}(\Psi, \beta), \widehat{\tau}(\Psi, \beta)\rangle .
\end{aligned}$$
The last equality follows from the fact that $\widehat{\tau}(\Psi, \alpha)$ preserves the splitting of $W$ into $S^{ \pm}$, whereas $\widehat{\tau}(\Psi, \beta)$ reverses it, so they must be orthogonal.
\item[3.] Since the splitting of $W$ into $S^{ \pm}$is induced by the eigenspaces of Clifford multiplication by a covariantly constant 2-form, $i \mu_{\Sigma}$, spinoriality of ∇ ensures that covariant differentiation respects the splitting. Also, Clifford multiplication by $\eta$ preserves the spitting, so
$$\left\langle-2 \nabla_{a^{*}} \Psi+2 \xi\langle a, \eta\rangle \eta \cdot \Psi, \beta\right\rangle=0 .$$
\end{itemize}
Taking the inner product of Equation 5.27 with $\beta$ and applying these observations (the vanishing of four a priori non-negative terms), we can conclude that
$$\langle\widehat{\tau}(\Psi, \beta), \widehat{\tau}(\Psi, \beta)\rangle=0 ;$$
but this implies that $\beta=0$, and we have $\psi \in \Gamma\left(Y, S^{+}\right)$as in Equation 5.24.

Next, we turn our attention to deriving Equation 5.25. Since, as we have just established, both $\Psi, \psi \in \Gamma\left(Y, S^{+}\right)$, it follows that $\widehat{\tau}(\Psi, \psi)$ must preserve the splitting of $S^{ \pm}$, so that $\Pi_{\eta^{\perp}} \widehat{\tau}(\Psi, \psi)=0$; i.e. by Equation 5.23,
$$\iota_{\frac{\partial}{\partial \varphi}} d b=0 .$$
Hence, $d b$ pulls up from $\Sigma$, and, once again by Equation 5.23, together with Equation 5.3, we get that
$$0={ }^{\circ} \nabla_{\frac{\partial}{\partial \varphi}} \widehat{\tau}(\Psi, \psi) ;$$
which implies, after taking the $\eta$-component, that
$$0=\frac{\partial}{\partial \varphi}\langle\Psi, \psi\rangle .$$
Decompose $b$ according to the splitting of the cotangent bundle,
$$b=f \eta+c,$$
i.e. $f \in \Omega^{0}(Y, i \mathbb{R})$ and $c \in \Omega^{1}(Y, i \mathbb{R})$. Then, the $S^{+}$-component of Equation 5.22 gives us that
$$i \nabla_{\frac{\partial}{\partial \varphi}} \psi+i f \Psi=0$$
Hitting this equation with $i \nabla_{\frac{\partial}{\partial \varphi}}$ and integrating against $\psi$, we get
$$\begin{aligned}
0 & =\left\langle i \nabla_{\frac{\partial}{\partial \varphi}} \psi, i \nabla_{\frac{\partial}{\partial \varphi}} \psi\right\rangle-\int\left(\frac{\partial}{\partial \varphi} f\right)\langle\Psi, \psi\rangle \\
& =\left\langle i \nabla_{\frac{\partial}{\partial \varphi}} \psi, i \nabla_{\frac{\partial}{\partial \varphi}} \psi\right\rangle+\int f \frac{\partial}{\partial \varphi}\langle\Psi, \psi\rangle \\
& =\left\langle i \nabla_{\frac{\partial}{\partial \varphi}} \psi, i \nabla_{\frac{\partial}{\partial \varphi}} \psi\right\rangle,
\end{aligned}$$
by Equation 5.28, together with the fact that $\nabla_{\frac{\partial}{\partial \varphi}} \Psi=0$. Hence, we have obtained Equation 5.25.

To show that the form $b$ pulls up from $\Sigma$, notice that Equation 5.29 combined with Equation 5.25 shows that $f=0$ on the (dense, open) set where $\Psi \neq 0$, so it must vanish identically. Thus,
$$\iota_{\frac{\partial}{\partial \varphi}} b=0 .$$

Combined with the fact that $d b$ pulls up from $\Sigma$, we get that $b$ itself must pull up, giving Equation 5.26.

This completes the proof of Equation 5.21.

\subsection*{5.7. Vortices over Orbifolds.}

The complex interpretation of irreducible solutions in $\mathcal{M}_{s w}^{*}(Y)$ appearing in Theorem 1 follows from Theorem 4, together with the following theorem, which is essentially contained in [17],[5], about vortices over orbifolds.

Definition 5.12. A vortex with $\beta_{0}=0$ (resp. $\alpha_{0}=0$ ) is called a positive vortex (resp. negative vortex). The moduli space of positive vortices (resp. negative vortices) in a line bundle $E$ over $\Sigma$ will be denoted $\mathcal{M}_{v}^{+}(E)$ (resp $\left.\mathcal{M}_{v}^{-}(E)\right)$.

Theorem 5. Let $E \rightarrow \Sigma$ be an orbifold line bundle with background Chern number $e$. The moduli space of vortices $\mathcal{M}_{v}^{+}(E) \cong \mathcal{M}_{v}^{-}\left(K_{\Sigma} \otimes E^{-1}\right)$ is empty if
$$\operatorname{deg}(E)>\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2},$$
and it is naturally diffeomorphic to the e-fold symmetric product of $|\Sigma|$, $\operatorname{Sym}^{e}(|\Sigma|)$, if
$$\operatorname{deg}(E)<\frac{\operatorname{deg}\left(K_{\Sigma}\right)}{2} .$$

Proof. For the proof, we refer to [5],[17]. We give the outline of the argument.
The identification of $\mathcal{M}_{v}^{+}(\Sigma, E)$ with $\mathcal{M}_{v}^{-}(\Sigma, E)$ arises from Serre duality, which gives a map
$$*: \Gamma(\Sigma, E) \rightarrow \Gamma\left(\Sigma, K_{\Sigma}^{-1} \otimes\left(K_{\Sigma} \otimes E^{-1}\right)\right),$$
with
$$\bar{\partial}^{*} *=-* \bar{\partial} .$$

Since a line bundle with negative degree supports no holomorphic sections, the vortex equations force any bundle $E$ with a non-zero vortex to satisfy Inequality 5.30.