# Desingularizations of Conformally Kaehler, Einstein Orbifolds

- Category: papers
- Identity: arxiv:2601.19215
- Content status: fulltext_ok

---

---
source_file: 2601_19215.pdf
converter: mathpix
format: mmd
---

\title{
Desingularizations of Conformally Kähler, Einstein Orbifolds
}

\author{
Claude LeBrun* and Tristan Ozuch ${ }^{\dagger}$ \\ Stony Brook University \\ MIT
}

\begin{abstract}
Let $\left\{\left(M, g_{i}\right)\right\}_{i=1}^{\infty}$ be a sequence of smooth compact oriented Einstein 4-manifolds of fixed Einstein constant $\lambda>0$ that GromovHausdorff converges to a 4-dimensional Einstein orbifold ( $X, g_{\infty}$ ). Suppose, moreover, that the limit metric $g_{\infty}$ is Hermitian with respect to some complex structure on the limit orbifold $X$, that $X$ has at least one singular point, and that every gravitational instanton that bubbles off from $\left(M, g_{i}\right) \rightarrow\left(X, g_{\infty}\right)$ is anti-self-dual. Then, for all sufficiently large $i$, the given $\left(M, g_{i}\right)$ are all Kähler-Einstein. As a consequence, the limit orbifold $\left(X, g_{\infty}\right)$ is also Kähler-Einstein, and must in fact be one of the orbifold limits classified [38] by Odaka, Spotti, and Sun.
\end{abstract}

\section*{1 Introduction}

Three decades ago, Anderson [1] and Bando-Kasue-Nakajima [5, 6, 7, 36] discovered a generalization of Gromov's compactness theorem [21] that gives 4-dimensional Einstein orbifolds a previously-unsuspected central role in the theory of smooth compact Einstein 4-manifolds. For example, if we are given a sequence ( $M_{i}, g_{i}$ ) of smooth compact connected Einstein 4-manifolds of fixed Einstein constant $\lambda>0$ and fixed Euler characteristic, with volumes

\footnotetext{
*Supported in part by NSF grant DMS-2203572.
${ }^{\dagger}$ Supported in part by NSF grant DMS-2405328.
}
$\operatorname{Vol}\left(M, g_{i}\right)$ uniformly bounded away from zero, then there exists a subsequence $\left(M_{i_{j}}, g_{i_{j}}\right)$ that converges in the Gromov-Hausdorff distance to a compact connected 4-dimensional Einstein orbifold $\left(X, g_{\infty}\right)$ with the same Einstein constant $\lambda$. After further refining our subsequence, we may moreover arrange [2] that the manifolds $M_{i_{j}}$ are all diffeomorphic ${ }^{1}$ to some reference smooth compact 4-manifold $M$. The singularities of the limit orbifold $X$ are moreover isolated, and so constitute a finite subset $\mathfrak{S} \subset X$, while their complement $X-\mathfrak{S}$ is diffeomorphic to a connected open set $U \subset M$. Furthermore, after moving the metrics in the sequence by a suitable sequence of self-diffeomorphisms of $M$, the weak-limit metric $g_{\infty}$ on $X-\mathfrak{S}$ actually becomes the $C^{\infty}$ limit on compact subsets of the given sequence of Einstein metrics restricted to $U \subset M$. Meanwhile, the Riemannian diameter of each connected component of $M-U$ shrinks to zero, but the $L^{2}$ norm of the curvature on each such component remains bounded away from zero. After suitably scaling up these high-curvature regions, their pointed Gromov-Hausdorff limits then yield Ricci-flat ALE spaces that are said to bubble off from $M$. One subtlety is that curvature can accumulate at different length scales, so that some of these ALE limits could themselves be orbifolds. However, any orbifold singularity of such an ALE space in turn arises from a deeper bubble. This hierarchy of scales however terminates in finitely many steps, and the deepest bubbles that thereby arise are therefore smooth. By reversing the process, one can then reconstruct the smooth manifold $M$ from $X$ by [1, 6] cutting out a neighborhood of each orbifold singularity, replacing it with a diffeomorphic copy of the corresponding bubble, and then iterating the process until all the orbifold singularities have been removed.

While the above results indicate that certain Einstein orbifolds can arise as limits of smooth Einstein 4-manifolds, the second author's previous results [42, 43, 41] have definitively shown that not every Einstein orbifold arises in this way. The present article focuses on the problem of determining which compact 4-dimensional Kähler-Einstein orbifolds with $\lambda>0$ can be expressed as limits of sequences of smooth Einstein 4-manifolds. If one specializes the problem by requiring that all the smooth Einstein manifolds in the limiting sequence be Kähler-Einstein manifolds, then a complete answer has already been given by Odaka-Spotti-Sun [38]. But if we now relax our assumptions, and allow the metrics in the given sequence to have arbitrary holonomy,

\footnotetext{
${ }^{1}$ The phenomenon of diffeomorphism-finiteness that is operative here has more recently been shown [15, Theorem 1.12] to hold under dramatically weaker hypotheses.
}
one might still hope that the list of possible Kähler-Einstein orbifold limits might remain unaffected. Unfortunately, however, there is a serious technical obstacle to proving such a statement. The root cause of this difficulty is that we currently lack a complete classification of Ricci-flat ALE manifolds. Indeed, all known examples of such ALE manifolds are half-conformallyflat, so that, when correctly oriented, they satisfy $W^{+} \equiv 0$, where $W^{+} \in$ $\operatorname{End}_{0}\left(\Lambda^{+}\right)$denotes the self-dual piece of the Weyl curvature tensor. While a longstanding conjecture claims that all Ricci-flat ALE 4-manifolds are in fact of this type, the best available result in support of this conjecture [37] assumes the existence of a spin structure on the universal cover of the ALE space for which one of the chiral spin bundles has trivial monodromy at infinity; but, unfortunately, no one has yet discovered a compelling reason why this assumption should a priori always be valid. In this paper, our approach will skirt this issue entirely via recourse to the following definition:

Definition 1. Let $\left(M^{4}, g_{i}\right)$ be a sequence of compact oriented 4-dimensional Einstein manifolds that converges to a positive-scalar-curvature compact Einstein orbifold $\left(X^{4}, g_{\infty}\right)$ in the Gromov-Hausdorff sense. We will then say that $\left(M, g_{i}\right)$ is an admissible sequence, and that $\left(X, g_{\infty}\right)$ is an admissible orbifold limit, if every Ricci-flat ALE space $(Y, \mathrm{~h})$ that bubbles off from the $\left(M, g_{i}\right)$ satisfies $W^{+} \equiv 0$ with respect to the induced orientation.

While restricting our attention to admissible sequences will of course narrow the scope of our investigation, it will nonetheless allow us to prove the following rather satisfying results:

Theorem A. Let $\left(X^{4}, g_{\infty}\right)$ be a compact Kähler-Einstein orbifold of Einstein constant $\lambda>0$, and let $\left(M^{4}, g_{i}\right)$ be an admissible sequence of compact oriented Einstein manifolds with $\left(X, g_{\infty}\right)$ as its orbifold limit. Then, for all $i \gg 0$, the $\left(M, g_{i}\right)$ are actually all Kähler-Einstein. In particular, $\left(X, g_{\infty}\right)$ must be one of the Kähler-Einstein orbifolds classified by Odaka-Spotti-Sun.

Indeed, essentially the same result will also follow even if one merely assumes that $g_{\infty}$ is Hermitian, in the sense that $g_{\infty}(J \cdot, J \cdot)=g_{\infty}$ for some integrable orbifold complex structure $J$ on $X$.

Theorem B. Let $\left(X^{4}, g_{\infty}\right)$ be a compact connected Einstein orbifold of Einstein constant $\lambda>0$, and suppose that $g_{\infty}$ is Hermitian with respect to some integrable orbifold complex structure $J$ on $X$. If $\left(X, g_{\infty}\right)$ has at least one
singular point, and if $\left(M, g_{i}\right) \rightarrow\left(X, g_{\infty}\right)$ is an admissible sequence of Einstein manifolds converging to $X$, then the $\left(M, g_{i}\right)$ are Kähler-Einstein for all $i \gg 0$, and $\left(X, g_{\infty}\right)$ is one of the Kähler-Einstein orbifold limits classified by Odaka-Spotti-Sun.

\section*{2 Singularities of Type T}

When $\left(X, g_{\infty}\right)$ is the orbifold limit of some admissible sequence $\left(M, g_{i}\right)$ of Einstein 4-manifolds, we will show, in Proposition 2.2 below, that its orbifold singularities must all have the following special property:

Definition 2. An isolated orbifold singularity of an oriented orbifold $X^{4}$ will be said to be of type T if it has an open neighborhood modeled on $\mathbb{R}^{4} / \Gamma$ for some finite subgroup $\Gamma<S O(4)$ for which $\mathbb{R}^{4} / \Gamma$ is also the tangent-cone-atinfinity of an oriented anti-self-dual Ricci-flat ALE manifold $\left(Y^{4}, \mathrm{~h}\right)$.

This definition can now be restated in a more concrete and effective form, as an immediate consequence of the results of Şuvaina [44] and Wright [45]:

Proposition 2.1. An oriented singularity $\mathbb{R}^{4} / \Gamma$ is of type T iff $\Gamma<S O(4)$ is conjugate to a subgroup of $U(2)$ of one of the two following types:
\begin{itemize}
\item[-] Finite subgroups $\Gamma \subset S U(2)$. These are classified by the simply-laced Dynkin diagrams, and their images in $S O(3)=S U(2) / \mathbb{Z}_{2}$ are classical symmetry groups of regular polygons or platonic solids.
\end{itemize}

\begin{tabular}[t]{|l|l|l|}
\hline Dynkin Diagram & $\Gamma \subset S U(2)$ & Classical Figure \\
\hline $A_{k} \quad \bullet \cdots \bullet \bullet \bullet$ & Cyclic $\cong \mathbb{Z}_{k+1}$ & ![](https://cdn.mathpix.com/cropped/3fb517a1-0bd7-495f-93f5-958f396c9054-04.jpg?height=60\&width=60\&top_left_y=1763\&top_left_x=1449) \\
\hline $D_{k}$ & Binary Dihedral & ![](https://cdn.mathpix.com/cropped/3fb517a1-0bd7-495f-93f5-958f396c9054-04.jpg?height=68\&width=88\&top_left_y=1848\&top_left_x=1423) \\
\hline $E_{6}$ & Binary Tetrahedral & ![](https://cdn.mathpix.com/cropped/3fb517a1-0bd7-495f-93f5-958f396c9054-04.jpg?height=77\&width=79\&top_left_y=1939\&top_left_x=1432) \\
\hline $E_{7}$ & Binary Octahedral & ![](https://cdn.mathpix.com/cropped/3fb517a1-0bd7-495f-93f5-958f396c9054-04.jpg?height=79\&width=71\&top_left_y=2027\&top_left_x=1440) \\
\hline $E_{8}$ & Binary Icosahedral & ![](https://cdn.mathpix.com/cropped/3fb517a1-0bd7-495f-93f5-958f396c9054-04.jpg?height=79\&width=79\&top_left_y=2117\&top_left_x=1435) \\
\hline
\end{tabular}
For each such $\Gamma$, the corresponding quotient $\mathbb{C}^{2} / \Gamma$ is [28] the tangent cone at infinity of a family of ALE hyper-Kähler 4-manifolds, each of
\begin{itemize}
\item[] which is obtained, up to diffeomorphism, by plumbing together copies of $T^{*} S^{2}$ according to the intersection pattern dual to the Dynkin diagram.
\item[-] Cyclic groups $\Gamma \cong \mathbb{Z}_{\ell m^{2}}<U(2), m \geq 2$, that are generated by
$$\left[\begin{array}{ll}
\zeta & \\
& \zeta^{\ell m n-1}
\end{array}\right]$$
for $\zeta=e^{2 \pi i / \ell m^{2}}$, with $n<m$ and $\operatorname{gcd}(m, n)=1$. Such cyclic subgroups are often indicated [26] by the shorthand $\frac{1}{\ell m^{2}}(1, \ell m n-1)$. For any such subgroup, $\mathbb{C}^{2} / \Gamma$ is the tangent cone at infinity of a free $\mathbb{Z}_{m}$-quotient of a hyper-Kähler manifold of type $A_{\ell m-1}$. Conversely, every non-simplyconnected Ricci-flat ALE Kähler surface is [44] one of these.
\end{itemize}

This of course follows from the classification [44, 45] of oriented Ricci-flat ALE 4-manifolds that are anti-self-dual, in the sense that $W^{+} \equiv 0$. Here, one should especially take note of Wright's striking theorem that any such space is Kähler [45] with respect to some orientation-compatible complex structure. This fact dovetails nicely with our question, because any singularity of type T is therefore modeled on $\mathbb{C}^{2} / \Gamma$ for some finite group $\Gamma \subset U(2)$ that acts freely on the unit sphere $S^{3} \subset \mathbb{C}^{2}$, and any isolated singularity of an orbifold Kähler surface is naturally of this form. However, notice that our requirement that $\mathbb{C}^{2} / \Gamma$ must also be the tangent cone at infinity of an anti-self-dual Ricci-flat ALE manifold imposes further, less obvious constraints. Indeed, in the specific setting where $X$ is an orbifold complex surface, singularities of type T exactly coincide [26, Proposition 3.10] with the ones algebraic geometers have traditionally called singularities of class T. From an algebrogeometric perspective, the key property of these singularities is that they have $\mathbb{Q}$-Gorenstein local smoothings. However, the relevance of this class of singularities to our investigation instead primarily stems from the following differential-geometric observation:

Proposition 2.2. If $\left(X, g_{\infty}\right)$ is an admissible orbifold limit, then $X$ has only singularities of type T.

Proof. The subtlety here is that the ALE spaces that bubble off from a given sequence $\left(M, g_{i}\right) \rightarrow\left(X, g_{\infty}\right)$ might be orbifolds, rather than manifolds. However, when one surgically replaces each orbifold singularity of such an ALE space with the corresponding deeper bubble, and then iterates the process
until it terminates, the resulting ALE manifold is then diffeomorphic to a Ricci-flat ALE Kähler manifold [6, Theorem 3]. Thus, whenever an admissible orbifold limit has a singularity modeled on $\mathbb{C}^{2} / \Gamma$ for some $\Gamma<U(2)$, then $\mathbb{C}^{2} / \Gamma$ is also the tangent cone at infinity of a non-singular Ricci-flat ALE Kähler manifold. \(\square\)

As an immediate consequence, we therefore have:
Proposition 2.3. Among compact Kähler-Einstein orbifolds $\left(X^{4}, g_{\infty}\right)$ that have only isolated singularities, there are infinitely many topological types that can never arise as limits of admissible sequences of Einstein 4-manifolds.

Proof. Let $g_{F S}$ be the Fubini-Study metric on $\mathbb{C P}_{2}$, and, for any prime number $p \geq 5$, consider the finite group of isometries of $\left(\mathbb{C P}_{2}, g_{F S}\right)$ that is generated by
$$\left[\begin{array}{lll}
1 & & \\
& \eta & \\
& & \eta^{-1}
\end{array}\right],$$
where $\eta=e^{2 \pi i / p}$. The orbifold $\mathbb{C P}_{2} / \mathbb{Z}_{p}$ then has exactly three singular points, namely the images of [ $1: 0: 0$ ], [ $0: 1: 0$ ], and $[0: 0: 1]$, and each of these three singular points has a neighborhood modeled on a quotient $\mathbb{C}^{2} / \mathbb{Z}_{p}$, where the generator of the given $\mathbb{Z}_{p}$ action on $\mathbb{C}^{2}$ takes the form
$$\left[\begin{array}{ll}
\eta & \\
& \eta^{-1}
\end{array}\right],\left[\begin{array}{ll}
\eta & \\
& \eta^{2}
\end{array}\right]^{-1}, \text { or }\left[\begin{array}{ll}
\eta & \\
& \eta^{2}
\end{array}\right],$$
respectively. The first of these cyclic groups is a subgroup of $S U(2)$, and so gives rise to a singularity of type T, modeled on the tangent cone at infinity of a gravitational instanton of type $A_{p-1}$. However, the other two singularities are not of type T, because in both cases the relevant cyclic group is not contained in $S U(2)$, and its order is not divisible by a square. These Kähler-Einstein orbifolds $\left(\mathbb{C P}_{2}, g_{F S}\right) / \mathbb{Z}_{p}$ can therefore never be limits of admissible sequences of smooth Einstein manifolds. \(\square\)

Indeed, this set of examples also leads to a stronger conclusion:
Proposition 2.4. Either there are infinitely many topological types of compact Kähler-Einstein orbifolds $\left(X, g_{\infty}\right)$ with isolated singularities that cannot arise as Gromov-Hausdorff limits of smooth Einstein manifolds, or else there are Ricci-flat ALE 4-manifolds that remain to be discovered.

Proof. If we assume that we already know all possible Ricci-flat ALE 4-manifolds, the only additional freedom allowed beyond the type T scenario is that some of the Ricci-flat Kähler gravitational instantons might arise with the non-standard orientation, thus allowing them to have $W^{-}=0$ instead of $W^{+}=0$. However, for any prime $p$, this would still only allow $\mathbb{Z}_{p} \subset \mathbf{U}(2)$ to arise in connection to an orbifold singularity $\mathbb{C}^{2} / \mathbb{Z}_{p}$ if the $\mathbb{Z}_{p}$ action were generated by
$$\left[\begin{array}{ll}
\eta & \\
& \eta^{-1}
\end{array}\right] \text { or }\left[\begin{array}{ll}
\eta & \\
& \eta
\end{array}\right]$$
for some $p^{\text {th }}$ root of unity $\eta$. However, for any prime $p \geq 5$, two of the singularities of the isometric quotients $\mathbb{C P}_{2} / \mathbb{Z}_{p}$ discussed above are certainly not of this form. Thus, these examples cannot be Gromov-Hausdorff limits of sequences of smooth Einstein 4-manifolds unless there are undiscovered ALE gravitational instantons that are not half-conformally-flat. \(\square\)

Of course, the examples displayed in the proof of Proposition 2.3 are just the tip of the iceberg. Even among cyclic quotients of $\mathbb{C P}_{2}$, one could either replace the prime $p$ with an arbitrary product of distinct primes, or change the specific powers of the root of unity $\eta$ in the matrix that generates the action. Another family of examples that would have sufficed to prove Proposition 2.3 can be obtained by instead dividing the product Einstein metric on $\mathbb{C P}_{1} \times \mathbb{C P}_{1}$ by the action of a cyclic group $\mathbb{Z}_{k}, k \neq 2,4$, acting on both $S^{2}$ factors by identical rotations about an axis; these examples have four orbifold singularities, but only two of them are of type T. For an infinite class of non-locally-symmetric Kähler-Einstein examples with singularities that are not of type T, see [13, 17, 25]. For non-Kähler examples of compact 4-dimensional Hermitian Einstein orbifolds which have singularities that are not of type T, see [3, 12, 14, 19].

\section*{3 Hermitian, Einstein Orbifolds}

While Theorem A just concerns the case where ( $X, g_{\infty}$ ) is a Kähler-Einstein orbifold with $\lambda>0$, Theorem B weakens this hypothesis by merely requiring that the $\lambda>0$ Einstein orbifold ( $X, g_{\infty}$ ) be Hermitian. Let us therefore point out that this weaker condition can be restated in various equivalent ways.

Theorem 3.1. A compact oriented simply-connected $\lambda>0$ Einstein orbifold $\left(X^{4}, g\right)$ is Hermitian, in the sense that $g=g(J \cdot, J \cdot)$ for some integrable
orientation-compatible orbifold complex structure $J$ on $X$, if and only if one of the following equivalent conditions holds:
\begin{itemize}
\item[(i)] The Einstein metric $g$ is conformally Kähler, meaning that there is a smooth positive function $u: X \rightarrow \mathbb{R}^{+}$such that $\check{g}=u^{2} g$ is a Kähler metric with respect to some orientation-compatible integrable orbifold complex structure $J$ on $X$.
\item[(ii)] The self-dual Weyl curvature $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$of $g$ has two equal, negative eigenvalues at almost every point of $X$.
\item[(iii)] There is a global self-dual harmonic 2-form $\omega$ on the compact orbifold $(X, g)$ such that $W^{+}(\omega, \omega)>0$ at every point of $X$.
\item[(iv)] The self-dual Weyl curvature $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$satisfies $\operatorname{det}\left(W^{+}\right)>0$ at every point of $X$.
\end{itemize}

Proof. If the Einstein orbifold $(X, g)$ satisfies condition (i), the Riemannian Goldberg-Sachs theorem implies [29] that it either satisfies condition (ii), or else satisfies $W^{+} \equiv 0$. However, the compactness of $X$ and the positivity of the Ricci curvature of $g$ together exclude the latter possibility, because the orbifold generalization of [11, Theorem 1] and the fact that $b_{1}(X)=0$ would then imply that $g$ is globally conformal to a scalar-flat Kähler orbifold metric, contradicting the assumption that $g$ has positive scalar curvature.

The characterization (ii) of conformally Kähler, Einstein metrics is due to Derdziński [18], and is strictly local; the proof moreover shows that if this eigenvalue condition holds on a dense set, it actually holds everywhere. When this happens, the Kähler metric $\check{g}$ is actually extremal in the sense of Calabi; and, after possibly replacing it with a constant multiple, one can arrange for the scalar curvature $s_{\check{g}}$ of this extremal Kähler metric to exactly equal the positive function $u$.

If criterion (iii) is satisfied, then, since the orbifold $X$ is assumed to be compact, the Weitzenböck-formula proof of [32, Theorem 1] works exactly as in the manifold case. This then shows that the conformally related metric for which $|\omega| \equiv \sqrt{2}$ must actually be Kähler.

Criterion (iv) was first proposed by Peng Wu [46]. If $\alpha: X \rightarrow \mathbb{R}$ is the positive eigenvalue of $W^{+}$, the proof in [34] shows that $h=\alpha^{2 / 3} g$ is Kähler, using a Wetizenböck argument that works just as well on a compact orbifold as it does on a compact manifold. \(\square\)

\section*{4 Constraints on Diffeotype}

Next, we completely classify the smooth closed 4-manifolds that carry admissible sequences of Einstein metrics for which the limit is conformally Kähler.

Theorem 4.1. Suppose that $M$ is a smooth compact oriented 4-manifold that admits an admissible sequence $g_{i}$ of Einstein metrics such that $\left\{\left(M, g_{i}\right)\right\}$ Gromov-Hausdorff converges to a Hermitian, Einstein orbifold $\left(X^{4}, g_{\infty}\right)$ with Einstein constant $\lambda>0$. Then $M$ is necessarily diffeomorphic to a Del Pezzo surface. In other words, $M$ is diffeomorphic either to $S^{2} \times S^{2}$ or to a connected sum $\mathbb{C P}_{2} \# \ell \overline{\mathbb{C P}}_{2}$ for some $\ell \in\{0,1, \ldots, 8\}$. In particular, $\pi_{1}(M)=0, b_{+}(M)=1$, and $b_{-}(M) \leq 8$.

Proof. As we previously saw in the proof of Proposition 2.2, $M$ must be diffeomorphic to the manifold obtained by replacing each orbifold singularity of $X$ with a Ricci-flat Kähler ALE manifold. Each such replacement is implemented [1, 6, 36] by cutting out a small distance ball around a singular point $p_{k} \in X$, thereby introducing a boundary modeled on a spherical space-form $S^{3} / \Gamma_{k}$, and then gluing in a truncation of a Ricci-flat anti-selfdual ALE manifold $\left(Y_{k}, \mathrm{~h}^{(k)}\right)$ for which a neighborhood of infinity is modeled on $\left(S^{3} / \Gamma_{k}\right) \times \mathbb{R}^{+}$. If $\Gamma_{k} \subset S U(2)$, so that $\left(Y_{k}, \mathrm{~h}^{(k)}\right)$ is hyper-Kähler, choose a compatible integrable almost-complex structure $J^{(k)}$ which is asymptotic to the obvious one on $\mathbb{C}^{2} / \Gamma_{k}$; otherwise, when $\Gamma_{k} \subset U(2)$ but $Y_{k}$ is not simply connected, there is still an integrable almost-complex structure $J^{(k)}$ that is analogously asymptotic to the obvious choice. Because $\mathrm{h}^{(k)}$ is ALE of order 4, we thus have [7, 33]
$$\mathrm{h}_{a b}^{(k)}=\delta_{a b}+O\left(\varrho^{-4}\right), \quad h_{a b, c}^{(k)}=O\left(\varrho^{-5}\right),$$
and
$$\omega_{a b}^{(k)}=\omega_{a b}^{0}+O\left(\varrho^{-4}\right), \quad \omega_{a b, c}^{(k)}=O\left(\varrho^{-5}\right),$$
where $\varrho$ is the usual Euclidean radius, $\omega^{(k)}$ is the Kähler form of $\left(Y_{k}, \mathrm{~h}^{(k)}, J^{(k)}\right)$ and $\omega^{0}=d x^{1} \wedge d y^{1}+d x^{2} \wedge d y^{2}$ is the standard orbifold symplectic structure on $\mathbb{C}^{2} / \Gamma_{k}$. A quantitative refinement of the standard Moser stability argument then shows [33, Proposition 1.1] that, for each $k$, there is a diffeomorphism $\Psi=\Psi^{(k)}$ defined on some asymptotic region $\varrho>A$ with
$$\Psi^{*} \omega^{(k)}=\omega^{0} \quad \text { and } \quad \Psi=\text { identity }+O\left(\varrho^{-3}\right) .$$

Thus, for a large constant $C \gg 0$ and a suitably small $\varepsilon>0$, the composition of $\Psi$ with multiplication by $C / \varepsilon$ defines a symplectomorphism between the tiny annular region $\varepsilon<\varrho<2 \varepsilon$ in $\left(\mathbb{C}^{2} / \Gamma_{k}, \omega_{0}\right)$ and the annular region in $\left(Y_{k}, \varepsilon^{2} C^{-2} \omega^{(k)}\right)$ that is the image under $\Psi$ of the annulus $C<\varrho<2 C$. Identifying the domain of this map with a tiny annulus about the orbifold singularity $p_{k} \in X$ then shows that the Kähler form on $\left(X, g_{\infty}\right)$ can be extended across $Y_{k}$ as a symplectic form. Since the map used here to attach $Y_{k}$ to the regular part of $X$ is moreover isotopic to the one used to reconstruct $M$ from $X$ and the $Y_{k}$, applying this same procedure to all of the orbifold singularities of $X$ therefore constructs a symplectic form $\omega$ on a manifold diffeomorphic to $M$.

It follows that the smooth compact 4-manifold $M$ admits both a symplectic form $\omega$ and an Einstein metric $g_{i}$ of positive Einstein constant. This implies [16, 30] that $M$ must be diffeomorphic to a Del Pezzo surface. Indeed, since $M$ admits both a symplectic form and a metric of positive scalar curvature, Seiberg-Witten theory implies that it contains a pseudoholomorphic 2-sphere of non-negative self-intersection, and so must be symplectomorphic to a rational or ruled complex surface [35, 39]. The fact that $M$ must also [22] satisfy the strict Hitchin-Thorpe inequality $(2 \chi+3 \tau)(M)=c_{1}^{2}(M)>0$ then narrows the list of possibilities down to the Del Pezzo diffeotypes. \(\square\)

This result is nominally sharp, since every Del Pezzo 4-manifold $M$ actually does admit [16] conformally Kähler, positive- $\lambda$ Einstein metrics $g$, and therefore admits admissible constant sequences $g_{i}=g$ with limit $(M, g)$. However, this tautological construction of course never yields sequences that converge to singular orbifolds. In fact, we will eventually see that demanding that $X$ have at least one singular point actually winnows the list down to the four diffeotypes $\mathbb{C P}_{2} \# \ell \overline{\mathbb{C P}}_{2}, 5 \leq \ell \leq 8$.

We have already seen that most Kähler-Einstein orbifold complex surfaces certainly cannot arise as limits of admissible sequences of Einstein manifolds. This is partly explained by the fact that the first Chern class $c_{1}=c_{1}^{\text {orb }}$ of such an orbifold $X$ is usually only defined as an element of $H^{2}(X, \mathbb{Q})$, and that its self-intersection $c_{1}^{2}(X)$ is therefore in general only a rational number. When the orbifold is the limit of an admissible sequence, however, the situation is drastically simpler.

Proposition 4.2. If a Hermitian, $\lambda>0$ Einstein orbifold $\left(X^{4}, J, g_{\infty}\right)$ is the Gromov-Hausdorff limit of an admissible sequence $\left(M, g_{i}\right)$ of smooth Einstein 4 -manifolds $\left(M, g_{i}\right)$, then $c_{1}^{2}(X, J)=(2 \chi+3 \tau)(M) \in\{1,2,3,4, \ldots, 9\}$.

Proof. We have just seen that $M \approx\left(X-\left\{p_{k}\right\}\right) \cup \coprod_{k} Y_{k}$, where each $p_{k}$ is a singular point of $X$, and where $Y_{k}$ is a corresponding gravitational instanton. Moreover, each overlap $\left(X-\left\{p_{k}\right\}\right) \cap Y_{k}$ is diffeomorphic to $\mathbb{R} \times\left(S^{3} / \Gamma_{k}\right)$ for an appropriate finite group $\Gamma_{k} \subset U(2)$ that acts freely on $S^{3}$. Finally, we have seen that $M$ admits a symplectic structure $\omega$ that is symplectically isotopic to the Kähler form of $\left(J, g_{\infty}\right)$ on $X-\left\{p_{k}\right\}$, and that is symplectically isotopic to the Kähler form of a Ricci-flat Kähler metric on each $Y_{k}$. This in particular implies that there exists a positive integer $m$ such that the $m^{\text {th }}$ tensor power $K^{-m}$ of the anti-canonical line bundle $K^{-1}=\wedge^{2} T^{1,0}$ of $(M, \omega)$ is trivial on each $Y_{k}$, and is bundle-isomorphic to the dual of the pluricanonical line bundle $K^{\otimes m}$ on the regular part $X-\left\{p_{k}\right\}$ of $X$. Let us now choose a generic smooth section of $f$ of $K^{-m}$ which is non-zero on each $Y_{k}$ and meets the zero section of $K^{-m}$ transversely along a compatibly-oriented compact surface $\Sigma^{2} \subset M^{4}$. The homology class of $\Sigma$ in $M$ is then Poincaré dual to $m c_{1}(M, \omega) \in H^{2}(M, \mathbb{Z})$, while its homology class in $X$ is Poincaré dual to $m c_{1}^{\text {orb }}(X, J) \in H^{2}(X, \mathbb{Q})$. The self-intersection $[\Sigma] \cdot[\Sigma]$ therefore computes both $m^{2} c_{1}^{2}(M, \omega)$ and $m^{2} c_{1}^{2}(X, J)$, and we must consequently have $c_{1}^{2}(X, J)=c_{1}^{2}(M, \omega)=\left\langle p_{1}\left(\Lambda^{+}\right), M\right\rangle=(2 \chi+3 \tau)(M) \in\{1, \ldots, 9\}$, where the final list of possible values follows immediately from Theorem 4.1. \(\square\)

As a consequence, we now immediately obtain the following variation on a result of Odaka-Spotti-Sun [38]:
Proposition 4.3. Suppose that the $\lambda>0$ Kähler-Einstein orbifold ( $X^{4}, J, g_{\infty}$ ) is the Gromov-Hausdorff limit of an admissible sequence $\left(M, g_{i}\right)$ of smooth Einstein 4-manifolds $\left(M, g_{i}\right)$. If a singular point of $(X, J)$ has a neighborhood modeled on $\mathbb{C}^{2} / \Gamma_{k}$, where $\Gamma_{k} \subset U(2)$, then
$$\left|\Gamma_{k}\right|<\frac{12}{(2 \chi+3 \tau)(M)} .$$
In particular, every singular point has $\Gamma_{k}=\mathbb{Z}_{2}$ if $(2 \chi+3 \tau)(M) \geq 4$.
Proof. If $g_{0}$ is the metric induced on $S^{4} / \Gamma_{k}$ by the usual round metric on $S^{4}$, then the Bishop-Gromov inequality and Gauss-Bonnet imply that
$$32 \pi^{2} c_{1}^{2}(X)=\int_{X} s_{g_{\infty}}^{2} d \mu_{g_{\infty}}<\int_{S^{4} / \Gamma_{k}} s_{g_{0}}^{2} d \mu_{g_{0}}=\frac{24 \cdot 8 \pi^{2} \chi\left(S^{4}\right)}{\left|\Gamma_{k}\right|}=\frac{32 \pi^{2} \cdot 12}{\left|\Gamma_{k}\right|},$$
where the inequality is necessarily strict because the $\lambda>0$ Kähler-Einstein metric $g_{\infty}$ cannot have constant sectional curvature. The result thus follows, because $c_{1}^{2}(X)=(2 \chi+3 \tau)(M)$ by Proposition 4.2. \(\square\)

Of course, Theorem B makes the stronger claim that this same conclusion actually holds if we merely assume that the limit Einstein orbifold $\left(X, g_{\infty}\right)$ is Hermitian - or equivalently, by Theorem 3.1, that it is conformally Kähler. Moreover, once we have proved Theorem B, it will then follow that a Hermitian, Einstein orbifold limit of an admissible sequence $\left(M, g_{i}\right) \rightarrow\left(X, g_{\infty}\right)$ can only form singularities if $c_{1}^{2}(M)=c_{1}^{2}(X) \leq 4$; and, as we already know by Theorem 4.1, the latter is equivalent to requiring that $M \approx \mathbb{C P}_{2} \# k \overline{\mathbb{C P}}_{2}$, where $5 \leq k \leq 8$. Indeed, the Odaka-Spotti-Sun classification [38] will then go on to predict that the limit of an admissible sequence can only form singularities of the following types:
\begin{itemize}
\item[-] $\mathbb{C P}_{2} \# 5 \overline{\mathbb{C P}}_{2}$ : only $A_{1}$ singularities.
\item[-] $\mathbb{C P}_{2} \# 6 \overline{\mathbb{C P}}_{2}$ : only $A_{1}$ or $A_{2}$ singularities.
\item[-] $\mathbb{C P}_{2} \# 7 \overline{\mathbb{C P}}_{2}$ : only $A_{1}, \ldots, A_{4}$ or $\frac{1}{4}(1,1)$ singularities.
\item[-] $\mathbb{C P}_{2} \# 8 \overline{\mathbb{C P}}_{2}: A_{1}, \ldots, A_{10}, D_{4}, \frac{1}{4}(1,1), \frac{1}{8}(1,3)$, or $\frac{1}{9}(1,2)$ singularities.
\end{itemize}
This striking consequence helps illustrate the interest of Theorems A and B.

\section*{5 Admissible Limits and Desingularizations}

Our key to understanding Gromov-Hausdorff convergence of admissible sequences of Einstein metrics is based on [43, Corollary 4.16], which we next present in a streamlined form that has been adapted to present purposes:

Theorem 5.1 (Ozuch). Given any positive real constant $\nu>0$, there is a constant $\delta=\delta(\nu)>0$ such that, whenever ( $M, g^{\mathcal{E}}$ ) is a smooth compact Einstein 4-manifold with
\begin{itemize}
\item[-] total volume $\geq \nu$, and
\item[-] Ricci curvature $=3$,
\end{itemize}
and for which there is an Einstein 4-orbifold $\left(X, g_{\infty}\right)$ with
$$d_{G H}\left(\left(M, g^{\mathcal{E}}\right),\left(X, g_{\infty}\right)\right)<\delta,$$
then $\left(M, g^{\mathcal{E}}\right)$ is obtained from $\left(X, g_{\infty}\right)$ by the gluing-perturbation procedure detailed in §7 below.

Here we have simplified the discussion by homothetically rescaling our $\lambda>0$ Einstein metrics in order to arrange for them to have $\lambda=3$, which then guarantees, by Myers' theorem, that they all have diameter $\leq \pi$. This simple observation then guarantees that Theorem 5.1 is a straightforward consequence of [43, Corollary 4.16].

The gluing-perturbation procedure cited in Theorem 5.1 consists of first creating a smooth manifold by iteratively replacing each orbifold singularity with the corresponding the gravitational instanton that bubbles off, and then equipping the resulting manifold with a family of so-called Einstein-moduloobstruction metrics that satisfy a weakened form of the Einstein condition. Following [42, 43], the manifolds that arise by this procedure will often be called naïve desingularizations of the original orbifold. For a quantitative discussion of these technical points, see §7 below.

In the absence of further information, however, the construction of naïve desingularizations depends on a detailed inventory of the specific trees of gravitational instantons that are to replace each orbifold singularity, along with scaling data that determines the relevant rates at which the relevant gravitational instantons are to bubble off. However, in the context of admissible sequences, the allowed bubbling modes at each singularity actually form a single continuous family, and any resulting desingularization therefore belongs to a single predetermined diffeotype, which the present paper's second author has elsewhere [42, 43] called the expected topology. Combining the framework of [43, §5] with Theorem 4.1 therefore now provides us with the basic scaffolding needed to support our proofs of Theorems A and B:

Proposition 5.2. Let $\left(X^{4}, g_{\infty}\right)$ be a compact Hermitian, Einstein orbifold with $\lambda>0$ and only isolated singularities of type T . Then there is a single family of naïve desingularizations of $\left(X, g_{\infty}\right)$ by Einstein-modulo-obstruction manifolds diffeomorphic to a Del Pezzo surface such that any admissible sequence $\left(M, g_{i}\right)$ of Einstein 4-manifolds that Gromov-Hausdorff converges to $\left(X, g_{\infty}\right)$ consists, for sufficiently large $i$, of naïve desingularizations that belong to this family.

\section*{6 The Role of Wu's Criterion}

Our proofs of Theorems A and B will also hinge on showing that, for all $i \gg 0$, the Einstein manifolds $\left(M, g_{i}\right)$ must everywhere satisfy Wu's criterion
$$\operatorname{det}\left(W^{+}\right)>0,$$
where the self-dual Weyl curvature $W^{+}$is considered as an endomorphism of the 3-dimensional vector space $\Lambda^{+} \subset \Lambda^{2}$ of self-dual 2-forms at each point of $M$. As was first emphasized by Peng Wu [46], this conformally-invariant condition is satisfied by any conformally Kähler, Einstein metric on a Del Pezzo surface. Conversely, the first author [34] and Wu [46] proved, by two entirely different methods, that any Einstein metric on a compact simply-connected manifold that satisfies (1) everywhere must actually be conformally Kähler. Since (1) is an open condition, this in particular means that smooth Einstein perturbations of Hermitian, Einstein metrics always remain Hermitian. The gist of Theorems A and B is essentially that the same also holds for admissible sequences that merely tend, in the Gromov-Hausdorff sense, to an Einstein orbifold that satisfies any of the equivalent conditions of Theorem 3.1. To achieve this goal, we will use Proposition 5.2 to show that condition (1) continues to hold for such perturbations by carefully controlling the possible degenerations of Einstein 4-manifolds [41, 42, 43] in a manner that provides strong information regarding their curvature [10]. Our proof will thus unfold in accordance with the following rough outline:
\begin{itemize}
\item[(a)] Construct suitable approximations $g_{t_{i}, v_{i}}^{A}$ of the Einstein metrics $g_{i}$.
\item[(b)] Show that these approximations $g_{t_{i}, v_{i}}^{A}$ satisfy condition (1) for $i \gg 0$.
\item[(c)] Show that condition (1) then also holds for the given $g_{i}$ when $i \gg 0$.
\item[(d)] Invoke [34, 46] to conclude that these $g_{i}$ must therefore be Hermitian.
\end{itemize}

The rest of our article is therefore organized as follows. In Section 7, we will review some key technical facts that underpin our construction. In Section 8 we then prove Theorems A and B in the prototypical case where there is only one singularity, and trees of singularities do not arise. In Section 9, we then generalize this to allow for multiple singularities, but still in the absence of bubble-trees. Finally, in Section 10, we prove our results in the most general but technically-challenging setting, where the formation of bubble-trees is allowed.

\section*{7 Desingularizing Einstein Orbifolds}

Recall that the Einstein tensor of a Riemannian $n$-manifold $(M, g)$ is the symmetric tensor field defined by
$$\mathscr{E}=r-\frac{s}{2} g,$$
where $r$ and $s$ are, respectively, the Ricci tensor and scalar curvature of $g$; this definition is chosen so that the differential Bianchi identity implies that $E$ is automatically divergence-free with respect to $g$. In the $n=4$ case that is our sole concern here, the Einstein tensor takes the simple and attractive form
$$\mathscr{E}=\stackrel{\circ}{r}-\frac{s}{4} g$$
when expressed in terms of the trace-free part $\stackrel{\circ}{r}$ of the Ricci tensor $r$, thereby allowing the Einstein equation
$$r=\lambda g$$
for a chosen Einstein constant $\lambda$ to be rewritten as
$$\mathscr{E}+\lambda g=0 .$$
However, because of the diffeomorphism-invariance of the Einstein condition, this last equation fails to be elliptic. To remedy this, we now choose some background metric $g_{0}$, and then define a "gauged and normalized" version
$$\mathscr{F}_{g_{0}}(g)=\mathscr{E}(g)+\lambda g+\delta_{g}^{*} \delta_{g_{0}}(g)$$
of the Einstein tensor. On a compact manifold $M$, the elliptic equation
$$\mathscr{F}_{g_{0}}(g)=0$$
is then equivalent to the pair of conditions
$$\begin{array}{r}
\mathscr{E}(g)+\lambda g=0 \\
\delta_{g}^{*} \delta_{g_{0}} g=0
\end{array}$$

Indeed, since $\delta_{g} \mathscr{E}=0$, applying $\delta_{g}$ to (3) yields $\delta_{g} \delta_{g}^{*} \delta_{g_{0}} g=0$, and this then implies that
$$\int_{M}\left\|\delta_{g}^{*} \delta_{g_{0}} g\right\|^{2} d \mu_{g}=\int_{M}\left\langle\delta_{g_{0}} g, \delta_{g} \delta_{g}^{*} \delta_{g_{0}} g\right\rangle d \mu_{g}=0$$
Since $\operatorname{ker} \delta_{g}^{*}$ exactly consists of the Killing fields on $(M, g)$, equation (5) is equivalent to saying that $\delta_{g_{0}} g$ is a Killing field of $g$. This formalism becomes particularly elegant and natural if $g$ is known, for some a priori reason, to have discrete isometry group, and the reader is therefore invited to provisionally focus on the case in which neither the limit orbifold nor the smooth metrics in the given sequence admit any Killing vector fields. However, the presence of Killing fields merely leads to a mild failure in uniqueness when representing a given Einstein geometry by a solution of (3). While this will have no impact on the regularity-type results that are our goal here, the interested reader may wish to consult [43] for further discussion of this issue.

In dimension four, a straightforward (albeit tedious) calculation shows that the linearization $\bar{P}_{g_{0}}=\left.d \mathscr{F}\right|_{g_{0}}$ of (2) at $g_{0}$ is the elliptic operator
$$\begin{aligned}
\bar{P}_{g_{0}} h= & \frac{1}{2}\left[\nabla^{*} \nabla \mathbf{h}-\operatorname{Hess}(\operatorname{tr} h)-2 \dot{\mathcal{R}}(h)+2 \operatorname{Sym}(r \circ h)\right. \\
& \left.-\left(\Delta \operatorname{tr} h-\nabla^{*} \delta h-\langle r, h\rangle\right) g_{0}+(2 \lambda-s) h\right],
\end{aligned}$$
where the relevant operators, curvatures, traces, and inner products are all defined with respect to $g_{0}$; here Hess and $\Delta=d^{*} d$ respectively denote the Hessian and positive-spectrum Laplacian on scalar-valued functions, while the Riemann curvature tensor acts on symmetric 2-tensors by
$$[\stackrel{\circ}{\mathcal{R}}(h)]_{a b}:=\mathcal{R}^{c}{ }_{a}{ }^{d}{ }_{b} h_{c d} .$$
In particular, when $g_{0}$ is Einstein, with Einstein constant $\lambda$, and when the symmetric 2-tensor is $h$ is traceless and divergence-free, the linearization $\bar{P}_{g_{0}}$ then reduces to
$$P_{g_{0}}:=\frac{1}{2} \nabla^{*} \nabla-\stackrel{\circ}{\mathcal{R}}$$
or, in other words, half the Lichnerowicz Laplacian [8, p. 54] of $g_{0}$.
Remark Of course, these operators can naturally be defined on symmetric 2-tensors belonging to various function spaces. On orbifolds, ALE spaces and
their gluings, the theory developed in [41, 42, 43] actually considers them in the function spaces $C_{\beta}^{k, \alpha}, C_{\beta, *}^{k, \alpha}$ and $C_{\beta, * *}^{k, \alpha}$ described in Appendix A.

In order to begin implementing this last remark, we now focus on the case of an oriented 4-dimensional orbifold ( $X, g_{\infty}$ ) with only finitely many singularities, all of type T. Recall that, according to Definition 2, this means that each singular point $p_{k} \in X$ has a neighborhood modeled on a neighborhood of the origin in a quotient $\mathbb{R}^{4} / \Gamma_{k}, \Gamma_{k}<S O(4)$, that also occurs as the tangent-cone-at-infinity of some Ricci-flat ALE manifold with $W^{+} \equiv 0$. We also remind the reader that a complete list of the $\Gamma_{k}$ allowed by this definition is provided by Proposition 2.1. Now notice that Definition 2 tells us that it makes sense to modify $X$ by cutting out a neighborhood of $p_{k} \in X$ and replacing it with an anti-self-dual Ricci-flat ALE manifold. In order to carry out this procedure in a systematic way, we will next establish some conventions for doing so.

Definition 3 (The function $\varrho_{o}$ on an orbifold). Let $\left(X, g_{\infty}\right)$ be a complete oriented 4-dimensional orbifold with only finitely many isolated singularities. Choose an $\epsilon_{0} \in(0,1)$ such that the Riemannian $\epsilon_{0}$-distance ball $U_{i}=B_{\epsilon_{0}}\left(p_{k}\right)$ around each singular point $p_{k}$ is orientedly diffeomorphic, via the exponential map, to $B^{4} / \Gamma_{k}$ for some finite group $\Gamma_{k}<S O(4)$ that acts freely on $S^{3}$. We then choose a smooth function $\varrho_{o}: X \rightarrow[0,1]$ which, on each $U_{i}$, coincides with the Riemannian distance from the singular point $p_{k}$, and which satisfies $\varrho_{o} \geq \epsilon_{0}$ on the complement of the union of the $U_{i}$. For every $\epsilon \in\left(0, \epsilon_{0}\right)$, we then also set
$$X(\epsilon):=\varrho_{o}^{-1}[\epsilon, 1]=X-\left(\bigcup_{k} B_{\epsilon}\left(p_{k}\right)\right)$$
where $B_{\epsilon}\left(p_{k}\right) \subset U_{i}$ is the radius- $\epsilon$ Riemannian distance ball about $p_{k}$.
Next, we define $\mathfrak{O}\left(g_{\infty}\right)$ to be the space of traceless, divergence-free symmetric 2-tensors on a 4-dimensional manifold or orbifold with metric $g_{\infty}$ that belong to the kernel of $P_{g_{\infty}}$. Then, as explained in [43, Section 5], there is a one-to-one map from a neighborhood of $0 \in \mathfrak{O}\left(g_{\infty}\right)$ to the moduli space of Einstein-modulo-obstructions perturbations of $g_{\infty}$ defined by (3):

Proposition 7.1. For each $v_{o} \in \mathfrak{O}\left(g_{\infty}\right)$, there is a unique metric $\bar{g}_{v_{o}}$ satisfying:
\begin{itemize}
\item[1.] $\mathscr{F}_{g_{\infty}}\left(\bar{g}_{v_{o}}\right) \in \mathfrak{O}\left(g_{\infty}\right)$,
\end{itemize}
\begin{itemize}
\item[2.] $\left\|\bar{g}_{v_{o}}-g_{\infty}\right\|_{C^{2, \alpha}} \leqslant C\left\|v_{o}\right\|_{C^{2, \alpha}}^{2}$, and
\item[3.] $\bar{g}_{v_{o}}-\left(g_{\infty}+v_{o}\right) \perp_{L^{2}\left(g_{\infty}\right)} \mathfrak{O}\left(g_{\infty}\right)$.
\end{itemize}
for some $C>0$. In what follows, this metric $\bar{g}_{v_{o}}$ will be called an Einsteinmodulo-obstructions metric.

We next recall some important key facts regarding ALE Ricci-flat metrics.
Definition 4 (The function $\varrho_{b}$ on an ALE orbifold). We define $\varrho_{b}$ a smooth function on $N$ satisfying $\varrho_{b}:=\left(\Psi_{k}\right)_{*} \rho_{\delta}$ on each $U_{k}$, and $\varrho_{b}:=\left(\Psi_{\infty}\right)_{*} \rho_{\delta}$ on $U_{\infty}=N-K$, and such that $\epsilon_{0} \leqslant \varrho_{b} \leqslant \epsilon_{0}^{-1}$ on the rest of $N$. For $0<\epsilon \leqslant \epsilon_{0}$, we then set
$$N(\epsilon):=\left\{\epsilon<\varrho_{b}<\epsilon^{-1}\right\}=N-\left(\bigcup_{k} \Psi_{k}\left(\overline{B_{\delta}(0, \epsilon)}\right) \cup \Psi_{\infty}\left(\left(\mathbb{R}^{4} / \Gamma_{\infty}\right)-B_{\delta}\left(0, \epsilon^{-1}\right)\right)\right) .$$

Finally, we define $\mathfrak{O}\left(g_{b}\right)$ to be the space of infinitesimal Einstein deformations of $g_{b}$ which are traceless and divergence-free. As is explained in [43, Section 5], there is a one-to-one map from a neighborhood of $0 \in \mathfrak{O}\left(g_{b}\right)$ to the moduli space of K" ahler Ricci-flat ALE metrics perturbations of $g_{b}$.

Definition 5. For each $v_{b} \in \mathfrak{O}\left(g_{b}\right)$, and for a suitable $C>0$, we let $\bar{g}_{v_{b}}$ denote the unique Einstein-modulo-obstructions metric satisfying:
\begin{itemize}
\item[1.] $\mathscr{F}_{g_{b}}\left(\bar{g}_{v_{b}}\right)=0$,
\item[2.] $\left\|\bar{g}_{v_{b}}-g_{b}\right\|_{C_{\beta}^{2, \alpha}} \leqslant C\left\|v_{b}\right\|_{C_{\beta}^{2, \alpha}}^{2}$, and
\item[3.] $\left[\bar{g}_{v_{b}}-\left(g_{b}+v_{b}\right)\right] \perp_{L^{2}\left(g_{b}\right)} \mathfrak{O}\left(g_{b}\right)$.
\end{itemize}

We next review the notion of a naïve desingularization of an orbifold, which played a crucial role in the results of [42, 43].

Gluing of ALE spaces to orbifold singularities. Let $0<2 \epsilon<\epsilon_{0}$ be a fixed constant, $t>0,\left(Y, g_{\infty}\right)$ an orbifold and $\Phi: B_{\delta}\left(0, \epsilon_{0}\right) \subset \mathbb{R}^{4} / \Gamma \rightarrow U$ the inverse of a local chart around a singular point $p \in Y$. Let also ( $N, g_{b}$ ) be an ALE orbifold asymptotic to $\mathbb{R}^{4} / \Gamma$, and $\Psi:\left(\mathbb{R}^{4} / \Gamma\right)-B_{\delta}\left(0, \epsilon_{0}^{-1}\right) \rightarrow N-K$ the inverse of an orbifold chart at infinity.

For $\mathrm{s}>0$, we let $\phi_{\mathrm{s}}: \mathbb{R}^{4} / \Gamma \rightarrow \mathbb{R}^{4} / \Gamma$ denote the rescaling map $x \rightarrow \mathrm{~s} x$. For $t<\epsilon_{0}^{4}$, we then define $Y \nexists N$ as $N$ glued to $Y$ via the diffeomorphism
$$\Phi \circ \phi_{\sqrt{t}} \circ \Psi^{-1}: \Psi\left(A_{\delta}\left(\epsilon_{0}^{-1}, \epsilon_{0} t^{-1 / 2}\right)\right) \rightarrow \phi\left(A_{\delta}\left(\epsilon_{0}^{-1} \sqrt{t}, \epsilon_{0}\right)\right) .$$

We moreover fix some $C^{\infty}$ cut-off function $\Upsilon:[0, \infty) \rightarrow[0,1]$ supported in [0, 2] and equal to 1 on [0, 1].

Definition 6 (Naïve gluing of an ALE space to an orbifold). We define a naïve gluing of $\left(N, g_{b}\right)$ at scale $0<t<\epsilon_{0}^{4}$ to $\left(Y, g_{\infty}\right)$ at the singular point $p$, which we will denote $\left(Y \# N, g_{\infty} \#_{p, t} g_{b}\right)$ by putting $g_{\infty} \#_{p, t} g_{b}=g_{\infty}$ on $Y-U$, $g_{\infty} \#_{p, t} g_{b}=t g_{b}$ on $K$, and
$$g_{\infty} \#_{p, t} g_{b}:=\Upsilon\left(t^{-\frac{1}{4}} \rho_{\delta}\right) \Psi^{*} g_{b}+\left(1-\Upsilon\left(t^{-\frac{1}{4}} \rho_{\delta}\right)\right) \Phi^{*} g_{\infty}$$
on $\mathcal{A}(t, \epsilon):=A_{\delta}\left(\epsilon^{-1} \sqrt{t}, 2 \epsilon\right)$. Given two tensors $h_{o}$ and $h_{b}$ on $Y$ and $N$, we similarly define the naïve gluing of the tensors:
$$h_{o} \#_{p, t} h_{b}:=\Upsilon\left(t^{-\frac{1}{4}} \rho_{\delta}\right) \Psi_{\infty}^{*} h_{b}+\left(1-\Upsilon\left(t^{-\frac{1}{4}} \rho_{\delta}\right)\right) \Phi^{*} h_{o}$$

Let $\left(Y, g_{\infty}\right)$ be an Einstein orbifold, and $\left(M, g^{D}\right)$ a naïve desingularization of $\left(Y, g_{\infty}\right)$ by a tree of ALE Ricci-flat orbifolds $\left(N_{j}, g_{b_{j}}\right)$ glued at scales $T_{j}>0$.

Here, the manifold $M$ is also covered as $M=Y^{t} \cup \bigcup_{j} N_{j}^{t}$, where
$$Y^{t}:=Y-\left(\bigcup_{k} \Phi_{k}\left(B_{\delta}\left(0, t_{k}^{\frac{1}{4}}\right)\right)\right),$$
where $t_{k}>0$ is the relative gluing scale of $N_{k}$ at the singular point $p_{k} \in Y$, and where
$$N_{j}^{t}:=\left(N_{j}-\Psi_{\infty}\left(\left(\mathbb{R}^{4} / \Gamma_{\infty}\right)-B_{\boldsymbol{\delta}}\left(0,2 t_{j}^{-\frac{1}{4}}\right)\right)\right)-\left(\bigcup_{k} \Psi_{k}\left(B_{\boldsymbol{\delta}}\left(0, t_{k}^{\frac{1}{4}}\right)\right) .\right.$$
On $Y^{16 t} \subset Y^{t}$, we have $g^{D}=g_{\infty}$ and on each $N_{j}^{16 t} \subset N_{j}^{t}$, we have $g^{D}=$ $T_{j} g_{b_{j}}$. We also define $t_{\text {max }}:=\max _{j} t_{j}$. By Definition 6, on the intersection $N_{j}^{t} \cap Y^{t}$ we then have $\sqrt{T_{j}} r_{b_{j}}=\varrho_{o}$, and on the intersection $N_{j}^{t} \cap N_{k}^{t}$, we have $\sqrt{T_{j}} r_{b_{j}}=\sqrt{T_{k}} r_{b_{k}}$.

Definition 7 (Function $\varrho_{D}$ on a naïve desingularization). On a naïve desingularization $\left(M, g^{D}\right)$, we define a function $\varrho_{D}$ in the following way:
\begin{itemize}
\item[1.] $\varrho_{D}=\varrho_{o}$ on $Y^{t}$,
\item[2.] $\varrho_{D}=\sqrt{T_{j}} r_{b_{j}}$ on each $N_{j}^{t}$.
\end{itemize}

The function $\varrho_{D}$ is then smooth on $M$.
Definition 8 (Expected topology). A desingularization $\left(M, g_{t, v}^{D}\right)$ of a conformally Kähler, Einstein orbifold $\left(X, g_{\infty}\right)$ is said to have the expected topology if the Ricci-flat ALE spaces used to construct the desingularization are all Kähler, in an orientation-compatible manner.

Notice that the notion of expected topology therefore exactly models the sort of singularity formation that can arise from an admissible sequence in the sense of Definition 1, and so in particular only applies to singularities of type T in the sense of Definition 2.

\section*{8 Simplest Case of the Proof}

We will now illustrate our strategy by proving Theorems A and B in the simple case where $\left(X, g_{\infty}\right)$ only has one singularity, and no bubble-trees arise.

\section*{Approximate Einstein-modulo-obstructions metrics}

As was shown in [40], around a singular point $p$ of $X$, we can find a coordinate system on $\left(X, g_{\infty}\right)$ in which we have an expansion of a solution of $\delta_{\delta}\left(\bar{g}_{v_{\infty}}\right)=0$, for $\boldsymbol{\delta}$ the Euclidean metric, and
$$\bar{g}_{v_{\infty}}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}_{4}+\mathrm{O}\left(\varrho^{5}\right),$$
whose Ricci curvature satisfies
$$r\left(\bar{g}_{v_{\infty}}\right)-3 \bar{g}_{v_{\infty}}=\mathbf{w}_{v_{\infty}}=\mathfrak{w}_{0}+\mathfrak{w}_{2}+\mathrm{O}\left(\varrho^{2}\right) \in \mathfrak{O}\left(g_{\infty}\right),$$
for a constant 2-tensor $\mathfrak{w}_{0}$, and $\mathfrak{w}_{2}$ quadratic on $\mathbb{R}^{4}$
$$\bar{g}_{v_{b}}=\boldsymbol{\delta}+\mathfrak{H}^{4}+\mathrm{O}\left(\varrho_{\boldsymbol{\delta}}^{-8}\right) .$$
Let $\Sigma:=p^{-1}(\{0\})$ for $p: N \mapsto \mathbb{C}^{2} / \Gamma$ the minimal resolution if $\Gamma<S U(2)$, or its image in the appropriate quotient if $\Gamma \nless S U(2)$.

In the rest of the section, we will construct what we call an approximate obstruction space (an approximate co-kernel of the linearization of the Einstein equation) and an approximate Einstein-modulo-obstructions desingularization.

\section*{Extension of obstructions}

Let $\mathbf{w}=\mathfrak{w}_{0}+\mathfrak{w}_{2}+\mathrm{O}\left(\varrho_{o}^{3}\right) \in \mathfrak{O}\left(g_{\infty}\right)$ with $\left|\mathfrak{w}_{i}\right|_{\boldsymbol{\delta}} \leqslant \varrho_{o}^{i}$ and $\mathfrak{o}=O^{4}+\mathrm{O}\left(\varrho_{o}^{-5}\right) \in$ $\mathfrak{O}\left(\bar{g}_{v_{b}}\right)$. As proven in [41, Lemma 2.7], there is a unique tensor $\mathfrak{w}_{0}$ on $N$ satisfying: for $\mathfrak{w}_{0}$ of (13),
$$\begin{aligned}
& P_{\bar{g}_{v_{b}}} w_{0}=0 \\
& w_{0}=\mathfrak{w}_{0}+\mathrm{O}\left(\varrho^{-4}\right) \\
& \int_{\Sigma}\left\langle w_{0}, \mho_{v_{b}}\right\rangle_{\bar{g}_{v_{b}}} d a_{\left(\bar{g}_{v_{b}} \mid \Sigma\right)}=0 \text { for all } \mho_{v_{b}} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)
\end{aligned}$$
From [9, 43], for $\mathfrak{w}_{2}$ of (13), there exists $w_{2}$,
$$\begin{aligned}
P_{\bar{g}_{b}} w_{2} & \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right) \\
w_{2} & =\mathfrak{w}_{2}+\mathrm{O}\left(\varrho^{-2+\epsilon}\right), \quad \forall \epsilon>0 \\
\int_{\Sigma}\left\langle w_{2}\right. & \left., \mho_{v_{b}}\right\rangle_{\bar{g}_{b}} d a_{\left(\bar{g}_{v_{b}} \mid \Sigma\right)}=0 \text { for all } \mho_{v_{b}} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)
\end{aligned}$$
and a unique symmetric 2-tensor $\mathfrak{o}^{4}$ on $X$ such that:
$$\begin{aligned}
P_{\bar{g}_{v_{o}}} \mathfrak{o}^{4} & \in \mathfrak{O}\left(g_{\infty}\right), \\
\mathfrak{o}^{4} & =O^{4}+\mathfrak{O}\left(\varrho_{o}^{-2-\epsilon}\right), \\
\mathfrak{o}^{4} & \perp_{L^{2}\left(\bar{g}_{v_{o}}\right)} \mathfrak{O}\left(g_{\infty}\right) .
\end{aligned}$$

We then define our extensions of the (co)kernels of the building blocks.
Definition 9. Let $\mathbf{w}$ and $\mathfrak{o}$ be as above. We define:
$$\begin{gathered}
\tilde{\mathbf{w}}:=\mathbf{w} \#_{p, t}\left(w_{0}+t w_{2}\right), \text { and } \\
\tilde{\mathfrak{o}}:=\left(t^{2} \mathfrak{o}^{4}\right) \#_{p, t} \mathfrak{o} .
\end{gathered}$$

\section*{Approximate Einstein-modulo-obstructions metrics}

For a metric $g$, let us denote $Q_{g}^{(2)}$ the bilinear terms given by the second derivative of $\mathscr{F}_{g}$ (whose linearization is $P_{g}$ ) at $g$. There exist:
\begin{itemize}
\item[1.] unique symmetric 2-tensors $h_{2}$ on $N$ and $\mho_{2} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)$ satisfying the equations
$$\begin{aligned}
& P_{\bar{g}_{v_{b}}} h_{2}=\lambda \bar{g}_{v_{b}}+w_{0}+\mho_{2} \\
& \quad h_{2}=\mathfrak{H}_{2}+\mathfrak{H}_{2}^{4}+\mathrm{O}\left(\varrho^{-6+\epsilon}\right), \quad \forall \epsilon>0 \\
& \int_{\Sigma}\left\langle h_{2}, \mho_{v_{b}}\right\rangle_{\bar{g}_{v_{b}}} d a_{\left(\bar{g}_{v_{b}} \mid \Sigma\right)}=0 \text { for all } \mho_{v_{b}} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)
\end{aligned}$$
\item[2.] a unique symmetric 2-tensor $h_{3}$ on $N$ satisfying the following equations
$$\begin{aligned}
& P_{\bar{g}_{v_{b}}} h_{3}=0 \\
& \quad h_{3}=\mathfrak{H}_{3}+\mathfrak{H}_{3}^{4}+\mathrm{O}\left(\varrho^{-5+\epsilon}\right), \quad \forall \epsilon>0 \\
& \int_{\Sigma}\left\langle h_{3}, \mho_{v_{b}}\right\rangle_{\bar{g}_{v_{b}}} d a_{\left(\bar{g}_{v_{b}} \mid \Sigma\right)}=0 \text { for all } \mho_{v_{b}} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)
\end{aligned}$$
\item[3.] a unique symmetric 2-tensor $\mathfrak{o}_{(2)}^{4}$ on $X$ such that:
$$\begin{aligned}
P_{\bar{g}_{v_{o}}} \mathfrak{o}_{(2)}^{4} & \in \mathfrak{O}\left(g_{\infty}\right) \\
& \mathfrak{o}_{(2)}^{4}=O_{(2)}^{4}+\mathrm{O}\left(\varrho_{o}^{-2-\epsilon}\right) \\
& \mathfrak{o}_{(2)}^{4} \perp_{L^{2}\left(\bar{g}_{v_{o}}\right)} \mathfrak{O}\left(g_{\infty}\right)
\end{aligned}$$
where $\mho_{2}=O_{(2)}^{4}+\mathrm{O}\left(\varrho_{b}^{-5}\right)$ in (18).
\item[4.] a unique symmetric 2-tensor $h^{4}$ on $X$ and $\mathbf{w}^{4} \in \mathfrak{O}\left(g_{\infty}\right)$ such that:
$$\begin{aligned}
P_{\bar{g}_{v_{o}}} & h^{4}=\mathfrak{o}_{(2)}^{4}+\mathbf{w}^{4} \\
& h^{4}=\mathfrak{H}^{4}+\mathfrak{H}_{2}^{4}+\mathfrak{H}_{3}^{4}+\mathfrak{H}_{4}^{4}+\mathrm{O}\left(\varrho^{1-\epsilon}\right) \\
& h^{4} \\
& \perp_{L^{2}\left(\bar{g}_{v_{o}}\right)} \mathfrak{O}\left(g_{\infty}\right)
\end{aligned}$$
\end{itemize}
\begin{itemize}
\item[5.] and a symmetric 2-tensor $h_{4}$ on $N$ and $\mho_{4} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)$ satisfying the following equations
$$\begin{aligned}
& P_{\bar{g}_{v_{b}}} h_{4}=\lambda h_{2}-Q_{\bar{g}_{v_{b}}}^{(2)}\left(h_{2}, h_{2}\right)+w_{2}+\mho_{4} \\
& \quad h_{4}=\mathfrak{H}_{4}+\mathfrak{H}_{4}^{4}+\mathrm{O}\left(\varrho^{-4+\epsilon}\right) \\
& \int_{\Sigma}\left\langle h_{4}, \mho_{v_{b}}\right\rangle_{\bar{g}_{v_{b}}} d a_{\left(\bar{g}_{v_{b}} \mid \Sigma\right)}=0 \text { for all } \mho_{v_{b}} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)
\end{aligned}$$
for all $\epsilon>0$.
\end{itemize}

Proof of the existence of the above tensors. The proof of the existence and uniqueness of solutions of (18), (21) and (22) are exactly as in [41], which did not depend on any peculiar features of the Eguchi-Hanson metric.

Let us first give a proof for the existence of $h_{3}$ satisfying (19). Here the 2-tensor $\mathfrak{H}_{3}$ satisfies $P_{\boldsymbol{\delta}} \mathfrak{H}_{3}=0$ on $\mathbb{R}^{4}$ so $P_{\bar{g}_{v_{b}}}\left(\Upsilon \mathfrak{H}_{3}\right)=\mathrm{O}\left(\varrho_{b}^{-3}\right)$ on $N$ since $\bar{g}_{v_{b}}-\boldsymbol{\delta}=\mathrm{O}\left(\varrho_{b}^{-4}\right)$. From [43, Lemma 4.3], it is possible to find $h^{\prime}$ such that $P_{\bar{g}_{v_{b}}} h^{\prime}=-P_{\bar{g}_{v_{b}}}\left(\Upsilon \mathfrak{H}_{3}\right)$ if and only if $P_{\bar{g}_{v_{b}}}\left(\Upsilon \mathfrak{H}_{3}\right) \perp_{\bar{g}_{v_{b}}} \mathfrak{O}\left(\bar{g}_{v_{b}}\right)$. Now, by integration by parts: for $\overline{\mathcal{V}}_{v_{b}} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)$,
$$\int_{M}\left\langle P_{\bar{g}_{v_{b}}}\left(\Upsilon \mathfrak{H}_{3}\right), \bar{\mho}_{v_{b}}\right\rangle_{\bar{g}_{v_{b}}} d \mu_{\bar{g}_{v_{b}}}=0 .$$
Indeed, the boundary term is proportional to $\lim _{r \rightarrow \infty} r \int_{\mathbb{S}^{3} / \Gamma}\left\langle\mathfrak{H}_{3}, \mathfrak{H}^{4}\right\rangle_{g_{\mathbb{S}^{3} / \Gamma}} d \mu_{g_{\mathbb{S}^{3} / \Gamma}}$, but the coefficients of $\mathfrak{H}_{3}$ are harmonic in $\varrho^{3}$ while the coefficients of $\mathfrak{H}^{4}$ are harmonic in $\varrho^{-4}$, hence their restrictions on $\mathbb{S}^{3} / \Gamma$ belong to different eigenspaces of the spherical Laplacian and therefore are orthogonal:
$$\int_{\mathbb{S}^{3} / \Gamma}\left\langle\mathfrak{H}_{3}, \mathfrak{H}^{4}\right\rangle_{g_{\mathbb{S}^{3} / \Gamma}} d \mu_{g_{\mathbb{S}^{3} / \Gamma}}=0 .$$
Here, the existence of $\mathfrak{H}_{3}^{4}$ is proved exactly as in the proof of the existence of $\mathfrak{H}_{2}^{4}$ in [41, Lemma 2.3]. \(\square\)

We now define the approximate-solution metrics we will need.
Definition 10. When $v=\left(v_{o}, v_{b}\right) \in \mathfrak{O}\left(g_{\infty}\right) \times \mathfrak{O}\left(g_{b}\right)$ and $t$ are both sufficiently small, we use the conventions of Definition 6 to define the approximate Einstein-modulo-obstructions metric as the naïve desingularization
$$g_{t, v}^{A}:=\left(\bar{g}_{v_{o}}+t^{2} h^{4}\right) \#_{p, t}\left(\bar{g}_{v_{b}}+t h_{2}+t^{3 / 2} h_{3}+t^{2} h_{4}\right) .$$
We define $\tilde{\mathfrak{D}}\left(g_{t, v}^{A}\right)$ as the set of $\tilde{\mathbf{w}}+\tilde{\mathfrak{o}}$ as in Definition 9 for $\mathbf{w} \in \mathfrak{O}\left(g_{\infty}\right)$ and $\mathfrak{o} \in \mathfrak{O}\left(\bar{g}_{v_{b}}\right)$, and single out a specific associated approximate obstruction:
$$\mho_{t, v}^{A}:=\tilde{\mathbf{w}}_{v_{o}}+t^{2} \tilde{\mathbf{w}}^{4}+t \mho_{2}+t^{2} \mho_{4} \in \tilde{\mathfrak{D}}\left(g_{t, v}^{A}\right) .$$

\section*{Control of the approximate solutions}

The metrics $g_{t, v}^{A}$ solve the Einstein-modulo-obstructions equation in a manner that allows us to naturally extend the estimate [41, equation (50)] as follows:

Proposition 8.1. For $0<\beta<\frac{1}{4}$ and $0<\alpha<1$, we have
$$\left\|\mathscr{F}_{g_{t, v}^{D}}\left(g_{t, v}^{A}\right)+\mho_{t, v}^{A}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t}^{D}\right)}=o(t)$$
as $t \rightarrow 0$, while $\left\|g_{t, v}^{A}-g_{t}^{D}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t}^{D}\right)} \rightarrow 0$ as $(t, v) \rightarrow(0,0)$.
Proof. The proof of this estimate is very similar to those in [9, 43, 41]. We will focus here on the most challenging aspect of the proof, which pertains to the region $t^{\frac{1}{4}}<\varrho_{o}<2 t^{\frac{1}{4}}$ or $t^{-\frac{1}{4}}<\varrho_{b}<2 t^{-\frac{1}{4}}$ where the cut-off is used. Here one has
$$\bar{g}_{v_{o}}+t^{2} h^{4}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}_{4}+t^{2} \mathfrak{H}^{4}+t^{2} \mathfrak{H}_{2}^{4}+t^{2} \mathfrak{H}_{3}^{4}+t^{2} \mathfrak{H}_{4}^{4}+\mathrm{O}\left(\varrho^{5}\right)+\mathrm{O}\left(\varrho_{o}^{5-\epsilon} \varrho_{b}^{-4}\right)$$
$$\begin{aligned}
\phi_{\sqrt{t}, *}\left(\bar{g}_{v_{b}}+t h_{2}+t^{3 / 2} h_{3}+t^{2} h_{4}\right)= & \boldsymbol{\delta}+t^{2} \mathfrak{H}^{4}+\mathfrak{H}_{2}+t^{2} \mathfrak{H}_{2}^{4}+\mathfrak{H}_{3}+t^{2} \mathfrak{H}_{3}^{4} \\
& +\mathfrak{H}_{4}+t^{2} \mathfrak{H}_{4}^{4}+\mathrm{O}\left(\varrho_{o}^{2} \varrho_{b}^{-8+\epsilon}\right)+\mathrm{O}\left(\varrho_{b}^{-8}\right)
\end{aligned}$$
for all $\epsilon>0$, where $\phi_{\sqrt{t}, *}$ is defined as in Section 7. Thus, in the gluing annuli $t^{\frac{1}{4}}<\varrho_{o}<2 t^{\frac{1}{4}}$ and $t^{-\frac{1}{4}}<\varrho_{b}<2 t^{-\frac{1}{4}}$, the difference
$$\varrho_{D}^{l}\left|\nabla_{g_{t}^{D}}^{l}\left(\left(\bar{g}_{v_{o}}+t^{2} h^{4}\right)-\phi_{\sqrt{t}, *}\left(\bar{g}_{v_{b}}+t h_{2}+t^{3 / 2} h_{3}+t^{2} h_{4}\right)\right)\right|,$$
is, for $0<\beta<\frac{1}{4}$, of uniform size
$$\mathrm{O}\left(\varrho_{o}^{2} \varrho_{b}^{-8+\epsilon}\right)+\mathrm{O}\left(\varrho_{b}^{-8}\right)+\mathrm{O}\left(\varrho^{5}\right)+\mathrm{O}\left(\varrho_{o}^{5-\epsilon} \varrho_{b}^{-4}\right)=\mathrm{O}\left(t^{\frac{5}{4}}\right)=t^{\frac{\beta}{4}} o(t) .$$
Together with the controls on the cut-off function, this shows that (23) is satisfied in the annulus $t^{\frac{1}{4}}<\varrho_{o}<2 t^{\frac{1}{4}}$ or $t^{-\frac{1}{4}}<\varrho_{b}<2 t^{-\frac{1}{4}}$. The proof for the other regions is easier, and can be found in [9, 41, 43]. \(\square\)

\section*{Curvature of the approximate solutions}

Let $x^{i}$ be canonical coordinate functions on $\mathbb{R}^{4}$ and $\omega_{1}^{0}=d x^{1} \wedge d x^{2}+d x^{3} \wedge d x^{4}$ and $\theta_{1}^{0}=d x^{1} \wedge d x^{2}-d x^{3} \wedge d x^{4}$, and similarly $\omega_{i}^{0}$ and $\theta_{i}^{0}$ for $i \in\{1,2,3\}$. On $g_{b}$, we denote $\omega_{i}$ the hyper-Kähler forms asymptotic to $\omega_{i}^{0}$.

The following proofs rely on the isomorphism between $\Lambda_{g_{b}}^{-} \otimes \Lambda_{g_{b}}^{+}$and traceless 2-tensors obtained as follows: identifying 2-tensors and endomorphisms of $T M$, the composition of endomorphisms $\omega^{-} \circ \omega^{+}$is symmetric traceless.

Lemma 8.2. Let $\mathfrak{w}_{0}$ be a constant 2 -tensor on $\mathbb{R}^{4}$ projected on $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset \operatorname{SU}(2)$. Then, for $i \in\{1,2,3\}$ there exists $\Theta_{i} \in \Lambda_{g_{b}}^{-}$satisfying $d \Theta_{i}=0$ such that $\mathfrak{w}_{0}$ of (15) is equal to $\sum_{i} \Theta_{i} \circ \omega_{i}$.

Proof. Let $\mathfrak{w}_{0}$ be a 2-tensor on $g_{b}$ obtained from [41, Lemma 2.7] asymptotic to a constant traceless 2-tensor $\mathfrak{w}_{0}=\sum_{i, j} \mathfrak{w}_{0, i j} \theta_{j}^{0} \otimes \omega_{i}^{0}$ for $\mathfrak{w}_{0, i j} \in \mathbb{R}$, and the above $\theta_{j}^{0}$ and $\omega_{i}^{0}$ satisfying $d \theta_{i}^{0}=0$ and $d \omega_{i}^{0}=0$. Since $\mathfrak{w}_{0}$ is traceless, there are anti-self-dual 2-forms $\Theta_{i}$ such that $\mathfrak{w}_{0}=\sum_{i} \Theta_{i} \circ \omega_{i}, d d^{*} \Theta_{i}=0$, and $\Theta_{i}=\sum_{j} W_{0, i j} \theta_{j}^{0}+\mathrm{O}\left(\varrho^{-4}\right)$. By integration by parts, this yields:
$$\begin{aligned}
0= & \int_{M}\left\langle d d^{*} \Theta_{i}, \Theta_{i}\right\rangle_{g_{b}} d \mu_{g_{b}} \\
= & -\int_{M} d d^{*} \Theta_{i} \wedge \Theta_{i} \\
= & -\int_{M} d\left(d^{*} \Theta_{i} \wedge \Theta_{i}\right)+d^{*} \Theta_{i} \wedge d \Theta_{i} \\
= & -\lim _{\rho \rightarrow \infty} \int_{\left\{\varrho_{b}=\rho\right\}} d^{*} \Theta_{i} \wedge \Theta_{i} \\
& +\int_{M}\left|d^{*} \Theta_{i}\right|^{2} d \mu_{g_{b}}
\end{aligned}$$
Now, $d^{*} \Theta_{i} \wedge \Theta_{i}=\mathrm{O}\left(\varrho_{b}^{-5}\right)$ so the boundary term vanishes, and $d^{*} \Theta_{i}=0$. Since $\Theta_{i}$ is anti-self-dual , this implies $d \Theta_{i}=0$. \(\square\)

Let us now extend [10, Lemma 8] to the general setting in which the obstructions do not all happen to vanish.

Lemma 8.3. Let $g_{b}$ be an ALE Ricci-flat Kähler metric, and $h_{2}$ as in (18). Then, the first order variation
$$\mathcal{R}_{g_{b}}^{+,(1)}\left(h_{2}\right)$$
in the direction of $h_{2}$ of the self-dual curvature $\mathcal{R}^{+}$of $g_{b}$ has constant eigenvalues equal to those of $\mathcal{R}_{\bar{g}_{o}}^{+}(p)$.

Proof. Since the assertion is essentially local in nature, we may pass, if necessary, to a finite cover of the relevant ALE space, and thereby arrange for it to be hyper-Kähler, as in the proof of [43, Corollary 6.4].

The proof of [10, Lemma 8] using [10, Lemma 3] now immediately extends to show that $\stackrel{\circ}{r}_{g_{b}}^{(1)}\left(h_{2}\right)=\sum_{i} \Omega_{i} \circ \omega_{i}$ for $\Omega_{i}$ anti-self-dual 2-forms satisfying $d \Omega_{i}=0$ and asymptotically constant (or decaying at infinity), and $\omega_{i}$ the three Kähler forms on $g_{b}$. This is exactly our situation by Lemma 8.2. \(\square\)

We can therefore precise our estimate of the curvature of these metrics:
Corollary 8.4. The self-dual Weyl curvature $W^{+}$of $g_{t, v}^{A}$ at any point has eigenvalues arbitrarily close to those of $W^{+}\left(g_{\infty}\right)$ at some corresponding point of $X$, up to an error that tends to zero uniformly as $(t, v) \rightarrow 0$.

Proof. On the region $\varrho_{o}>2 t^{\frac{1}{4}}$ where $g_{t, v}^{A}=\bar{g}_{v_{o}}+t^{2} h^{4}$, we have $\mid \nabla_{g_{\infty}}^{l}\left(\bar{g}_{v_{o}}-\right.$ $\left.g_{\infty}\right) \mid \leqslant C\left\|v_{o}\right\|_{C^{2}}$, and $t^{2}\left|\nabla_{g_{\infty}}^{l} h^{4}\right| \leqslant t^{1-\frac{l}{4}}$. Consequently, when $\left(t, v_{o}\right) \rightarrow 0$, we have $\left|\nabla_{g_{\infty}}^{l}\left(\bar{g}_{v_{o}}+t^{2} h^{4}-g_{\infty}\right)\right| \rightarrow 0$ for $l<4$, and in particular, the self-dual Weyl curvature of $\bar{g}_{v_{o}}+t^{2} h^{4}$ uniformly tends to that of $g_{\infty}$ in this region.

For $\delta>0$ small enough independent of ( $t, v$ ), on the region $\delta^{-1}<\varrho_{b}<$ $t^{-1 / 4}$, where $\frac{1}{t} g_{t, v}^{A}=\bar{g}_{v_{b}}+t h_{2}+t^{\frac{3}{2}} h_{3}+t^{2} h_{4}$, we have
$$g_{t, v}^{A}-\bar{g}_{v_{o}}=t^{2}\left(\mathfrak{H}^{4}+\mathfrak{H}_{2}^{4}+\mathfrak{H}_{3}^{4}+\mathrm{O}\left(\varrho_{b}^{-8}\right)\right),$$
and since $\mathcal{R}_{\delta}^{+,(1)}\left(\mathfrak{H}^{4}\right)=0$, this yields
$$\mathcal{R}^{+}\left(g_{t, v}^{A}\right)=\mathcal{R}^{+}\left(\bar{g}_{v_{o}}\right)+\mathrm{O}\left(t^{2} \varrho_{b}^{-6}\right)=\mathrm{O}\left(t^{\frac{1}{2}}\right)=o(1),$$
and hence
$$W^{+}\left(g_{t, v}^{A}\right)=W^{+}\left(\bar{g}_{v_{o}}\right)+\mathrm{O}\left(t^{2} \varrho_{b}^{-6}\right)=\mathrm{O}\left(t^{\frac{1}{2}}\right)=o(1) .$$

Finally, on the region $\varrho_{b}<\delta^{-1}$, where $\frac{1}{t} g_{t, v}^{A}=\bar{g}_{v_{b}}+t h_{2}+t^{\frac{3}{2}} h_{3}+t^{2} h_{4}$, for $l \leqslant 3$, we have $t^{\frac{i}{2}}\left|\nabla_{\bar{g}_{b}}^{l} h_{i}\right| \leqslant C t^{\frac{i}{2}}$ for $C$ independent of $t$ and $v$ small enough. We therefore have
$$W^{+}\left(g_{t, v}^{A}\right)=W_{\bar{g}_{v_{b}}}^{+,(1)}\left(h_{2}\right)+\mathrm{O}(t) .$$

However, because the Einstein orbifold $\left(X, g_{\infty}\right)$ is assumed to be limit of an admissible sequence of $\lambda>0$ Einstein metrics, $\mathcal{R}^{+}\left(g_{\infty}\right)=\frac{s}{12} g_{\infty}+W^{+}$must
have zero as an eigenvalue at the singular point $p$ by [43], which refined an earlier result of [10]. However, since Theorem 3.1 tells us $g_{\infty}$ is conformal to a Kähler metric of positive scalar curvature, the two smallest eigenvalues of the trace-free tensor $W^{+}$are everywhere equal, it therefore follows that $\mathcal{R}^{+}\left(g_{\infty}\right)$ has eigenvalues $\left(0,0, \frac{s}{4}\right)=(0,0, \lambda)$ at the singular point $p$. By Lemma 8.3, it therefore follows that $\mathcal{R}_{\bar{g}_{v_{b}}}^{+,(1)}\left(h_{2}\right)$ has eigenvalues arbitrarily close to $(0,0, \lambda)$ as $(t, v) \rightarrow 0$. The eigenvalues of $W^{+}$therefore tend to $\left(-\frac{\lambda}{3},-\frac{\lambda}{3}, \frac{2 \lambda}{3}\right)$ in this region, and the claim therefore holds everywhere. \(\square\)

\section*{Proof-of-Concept Versions of Theorems A and B}

Now suppose that $\left(X, g_{\infty}\right)$ is a conformally Kähler, Einstein orbifold with $\lambda=3$, with exactly one singularity, for which there is an admissible sequence $\left(M, g_{i}\right)$ with
$$d_{G H}\left(\left(M, g_{i}\right),\left(X, g_{\infty}\right)\right) \rightarrow 0 .$$
Furthermore, assume that any Ricci-flat ALE rescaled pointed limit that bubbles off from the sequence has no orbifold singularities.

By [43], then, after possibly passing to a subsequence, there then exist scales $t_{i}$, naïve desingularizations $g_{t_{i}}^{D}$, and parameters $v_{i} \in \mathfrak{O}\left(g_{b}\right) \times \mathfrak{O}\left(g_{\infty}\right)$ such that
\begin{itemize}
\item[-] $\left\|g_{i}-g_{t_{i}, v_{i}}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$, and
\item[-] $g_{i}-g_{t_{i}, v_{i}}^{A} \perp_{g_{t j}^{D}} \tilde{\mathfrak{O}}\left(g_{t_{i}, v_{i}}^{A}\right)$.
\end{itemize}
Then [43, Proposition 5.11] tells us that
$$\left\|g_{i}-g_{t_{i}, v_{i}}^{A}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \leqslant C\left\|\mathscr{F}_{g_{t_{i}}^{D}}\left(g_{t_{i}, v_{i}}^{A}\right)+\tilde{\mathfrak{D}}_{t_{i}, v_{i}}^{A}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t_{i}}^{D}\right)}^{A}=o\left(t_{i}\right)$$
as $i \rightarrow \infty$, by virtue of (23). This then allows us to obtain the following curvature-control: for some $C>0$, independent of $i$,
$$\left\|\mathrm{W}^{+}\left(g_{t_{i}, v_{i}}^{A}\right)-\mathrm{W}^{+}\left(g_{i}\right)\right\|_{C^{0}\left(g_{i}\right)} \leqslant C t_{i}^{-1}\left\|\mathrm{~W}^{+}\left(g_{t_{i}, v_{i}}^{A}\right)-\mathrm{W}^{+}\left(g_{i}\right)\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$$
as $i \rightarrow \infty$, since, by definition of the norms: $\|\cdot\|_{C^{0}\left(g_{i}\right)} \leqslant C t_{i}^{-1}\|\cdot\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t_{i}}^{D}\right)}$ because $\varrho_{D}^{2}>t_{i}$. However, because $\operatorname{det}\left(W^{+}\right)\left(g_{\infty}\right)>0$ everywhere,Corollary 8.4 implies that $\operatorname{det} \mathrm{W}^{+}\left(g_{t_{i}, v_{i}}^{A}\right)>0$ for $i \gg 0$. By (24), the open property
$\operatorname{det} \mathrm{W}^{+}>0$ is therefore inherited by the genuine Einstein metrics $g_{i}$ for sufficiently large $i$. We have thus shown that the Einstein metrics $g_{i}$ satisfy Wu's criterion (1), so it follows [34, 46] that the $g_{i}$ must be conformally Kähler when $i \gg 0$. However, such Einstein metrics on smooth 4-manifolds are actually all Kähler-Einstein, aside [31, Theorem A] from two stronglyrigid exceptions for which, up to isometries and rescalings, there is only one conformally-Kähler Einstein manifold on the given 4-manifold; but this rigid scenario is then precluded by our assumption that the limit has an orbifold singularity. We have thus shown that Theorems A and B do in fact hold in the test-case where $X$ has exactly one singularity, and no trees of singularities occur. \(\square\)

\section*{9 Without Trees of Singularities}

We now allow multiple singularities, but exclude the formation of trees of singularities. For example, as explained in Corollary 9.2 below, this applies to desingularizations of a Kähler-Einstein orbifolds with $c_{1}^{2}=4$. In general terms, this case is very similar to the situation discussed in §8, and can best be understood using the framework of [43, Section 5.2] through the use of partial Einstein-modulo-obstructions desingularizations. Roughly speaking, the idea is to desingularize the singularities one-by-one, from the smallest scale to the largest one. A priori, one can only partially desingularize by Einstein-modulo-obstruction metrics. Starting by the smallest scale is crucial as it ensures negligible perturbations of the orbifold at its remaining singular points.

Let us once again take $\left(M, g_{i}\right)$ to be an admissible sequence of Einstein metrics that converges to a conformally Kähler, Einstein orbifold $\left(X, g_{\infty}\right)$ in the Gromov-Hausdorff sense. We now allow $X$ to possibly have multiple singularities, but we still suppose trees of singularities do not occur. As in the previous Section 8, by [42, 43], then, up to taking a subsequence, for $i$ large enough, there exists a naïve desingularization $g_{t_{i}}^{D}$ and parameters $v_{i} \in \tilde{\mathfrak{D}}\left(g_{t_{i}}^{D}\right)$ such that: $\left\|g_{i}-g_{t_{i}}^{D}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$. As in [43, Section 5.2], we will produce a better approximate metrics $g_{t_{i}, v_{i}}^{A}$ by using partial Einstein-moduloobstructions desingularizations as stepping stones.

\section*{Iterative partial naïve desingularizations}

After passing to a subsequence, we may assume that we can order the $n$ singular points of $X$ as $p_{1}, \ldots, p_{n}$ so that
$$0<t_{1, i} \leqslant t_{2, i} \leqslant \ldots \leqslant t_{n, i},$$
where $t_{k, i}$ is the scale of the gluing at $p_{k}$ in the construction of $g_{t_{i}}^{A}$ in Definition 10.

Definition 11 (Partial naïve desingularizations). For $k \in\{1, \ldots, n\}$, the $k^{\text {th }}$ partial desingularization of $\left(X, g_{\infty}\right)$, which we will denote by $\left(Y_{k}, g_{t}^{D_{k}}\right)$, is obtained by the naïve gluing of $g_{b_{1}}, \ldots, g_{b_{k}}$ to $\left(X, g_{\infty}\right)$ at the corresponding points $p_{1}, \ldots, p_{k}$ at the scales $t_{1}, \ldots, t_{k}$.

By iteration on $k$, we can then define approximate-Einstein-modulo-obstructions metrics $g_{t, v}^{A_{k}}$ and actual Einstein-modulo-obstructions metrics $\hat{g}_{t, v}^{k}$ on $Y_{k}$ as follows:

For $k=0, \quad$ we define $g_{t, v}^{D_{0}}=g_{t, v}^{A_{0}}=\hat{g}_{t, v}^{0}=\bar{g}_{v_{o}}$ and $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{0}}\right):=\mathfrak{O}\left(g_{\infty}\right)$.
Now let $0 \leqslant k \leqslant n-1$. The idea is to replace $\bar{g}_{v_{o}}$ by $\hat{g}_{t, v}^{k}$ and $\mathfrak{O}\left(g_{\infty}\right)$ by $\tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k}}\right)$ and to perform the constructions as in Section 8.

We start with some $\hat{g}_{t, v}^{k}$ that in a neighborhood of $p_{k+1}$ satisfies
$$r\left(\hat{g}_{t, v}^{k}\right)-3 \hat{g}_{t, v}^{k}=w_{0}^{k}+w_{2}^{k}+\mathrm{O}\left(\varrho_{o}^{3}\right) \in \mathfrak{O}\left(g_{\infty}\right),$$
and has an expansion
$$\hat{g}_{t, v}^{k}=\boldsymbol{\delta}+\mathfrak{H}_{2}(k)+\mathfrak{H}_{3}(k)+\mathfrak{H}_{4}(k)+\mathrm{O}\left(\varrho^{5}\right),$$
exactly like (12). We can therefore define the approximate Einstein-moduloobstructions $g_{t, v}^{A_{k+1}}$ as in Section 8 as the desingularization of $\hat{g}_{t, v}^{k}$ at $p_{k+1}$ by $\bar{g}_{v_{b}}$ at scale $t_{k+1}$ replacing the $\mathfrak{H}_{i}$ by the present $\mathfrak{H}_{i}(k)$. Indeed, all of the steps of the construction are local and do not see the global properties of $g_{\infty}$, except the construction of $h^{4}$ in (21) with $\mho\left(g_{\infty}\right)$ by $\tilde{\mho}\left(g_{t, v}^{A_{k}}\right)$, which follows from the application of [43, Proposition 4.9] to $P_{g_{t, v}^{D_{k}}}\left(\Upsilon\left(\mathfrak{H}^{4}+\mathfrak{H}_{2}^{4}+\mathfrak{H}_{3}^{4}\right)\right)$, where $\Upsilon$ is a controlled cut-off function supported in a neighborhood of $p_{k+1}$.

We also extend the definition of $\tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k+1}}\right)$ as in Definition 10: as the set of $\tilde{\mathbf{w}}+\tilde{\mathfrak{o}}$ for $(\mathbf{w}, \mathfrak{o}) \in \tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k}}\right) \times \mathfrak{O}\left(\bar{g}_{v_{b}}\right)$, defined exactly as in Section 8 replacing $\bar{g}_{v_{o}}$ by $g_{t, v}^{A_{k}}$ and $\mathfrak{O}\left(g_{\infty}\right)$ by $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k}}\right)$.

Now, by [43, Theorem 4.10], there exists a unique Einstein-modulo-obstructions metric $\hat{g}_{t, v}^{k+1}$ satisfying: for $(t, v)$ small enough,
\begin{itemize}
\item[-] $\left\|\hat{g}_{t, v}^{k+1}-g_{t, v}^{A_{k+1}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t}^{D_{k}}\right)} \rightarrow 0$ as $(t, v) \rightarrow 0$,
\item[-] $\hat{g}_{t, v}^{k+1}-g_{t, v}^{A_{k+1}} \perp_{g_{t, v}^{D_{k}}} \tilde{\mathfrak{D}}\left(g_{t, v}^{A_{k+1}}\right)$, and
\item[-] $\mathscr{F}_{g_{t}{ }^{D_{k+1}}}\left(\hat{g}_{t, v}^{k+1}\right) \in \tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k+1}}\right)$.
\end{itemize}

\section*{Controlling the approximate desingularizations}

As in the proof of [43, (96), Proposition 5.13], the proof of Proposition 8.1, which is local in nature, extends to the case of partial desingularizations.

Proposition 9.1. Let $k \in\{1, \ldots, n\}$. We have the following controls:
\begin{itemize}
\item[(i)] $\left\|\mathscr{F}_{g_{t}{ }^{D_{k}}}\left(g_{t, v}^{A_{k}}\right)-\mho_{t, v}^{A_{k}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t}^{D_{k}}\right)}=o\left(t_{k}\right)$, as $t_{k} \rightarrow 0$,
\item[(ii)] $\left\|\hat{g}_{t, v}^{k}-g_{t, v}^{A_{k}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t}^{D_{k}}\right)}=o\left(t_{k}\right)$, as $t_{k} \rightarrow 0$, and
\item[(iii)] at every point, the eigenvalues of the self-dual Weyl curvature of $\hat{g}_{t, v}^{k}$ are arbitrarily close to those of $g_{\infty}$ at some corresponding point of $X$.
\end{itemize}

Proof. We will prove this by induction on $k$. When $k=0$, one has $g_{t, v}^{D_{0}}=$ $g_{t, v}^{A_{0}}=\hat{g}_{t, v}^{0}=\bar{g}_{v_{o}}$ and the result is clear. Proceeding by induction, let us now assume that the Proposition holds for $0 \leqslant k \leqslant n-1$.

To prove (i), notice that the control of
$$\left\|\mathscr{F}_{g_{t}{ }^{D_{k+1}}}\left(g_{t, v}^{A_{k+1}}\right)-\mho_{t, v}^{A_{k+1}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{2, \alpha}\left(g_{t}^{D_{k+1}}\right)}$$
is exactly as in the proof of (23), as the argument is local, and therefore also applies to partial desingularizations; cf. [43, Proposition 5.13].

To prove (ii), notice that, as in Section 8, we once again have
$$\left\|\hat{g}_{t, v}^{k+1}-g_{t, v}^{A_{k+1}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t, v}^{D_{k+1}}\right)} \leqslant C\left\|\mathscr{F}_{g_{t}^{D_{k+1}}}\left(g_{t, v}^{A_{k+1}}\right)-\mho_{t, v}^{A_{k+1}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t, v}^{D_{k+1}}\right)}$$
for some $C>0$, where the right-hand side is $o\left(t_{k+1}\right)$ as $t_{k+1} \rightarrow 0$. Indeed, this follows from (i) and [43, (88), Proposition 5.11], the proof of which does not require the existence of an Einstein desingularization, but instead holds for any Einstein-modulo-obstructions metric.

Finally, to prove (iii), notice that the proof of Corollary 8.4 also works in our present setting, both at and away from the orbifold singularities. By the property for $k$, the metric $\hat{g}_{t, v}^{k}$, which plays the role of $\bar{g}_{v_{o}}$ in Section 8, has self-dual Weyl curvature with eigenvalues arbitrarily close to those of $\left(X, g_{\infty}\right)$ at some corresponding. An extension of the proof of Corollary 8.4, which is local in nature, then shows that the eigenvalues of $W^{+}\left(g_{t, v}^{A_{k+1}}\right)$ are arbitrarily close to those of $W^{+}\left(g_{\infty}\right)$ at an appropriate point. We then conclude, in exact analogy to (24), that
$$\begin{aligned}
\| \mathrm{W}^{+}\left(g_{t, v}^{A_{k+1}}\right) & -\mathrm{W}^{+}\left(\hat{g}_{t, v}^{k+1}\right) \|_{C^{0}\left(g_{t}^{D k+1}\right)} \\
& \leqslant C t^{-1}\left\|\mathrm{~W}^{+}\left(g_{t, v}^{A_{k+1}}\right)-\mathrm{W}^{+}\left(\hat{g}_{t, v}^{k+1}\right)\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g_{t}^{D k+1}\right)}
\end{aligned}$$
where the right-hand side tends to zero as $(t, v) \rightarrow 0$. \(\square\)

\section*{Conclusion of the proof}

Bringing these ideas together, let us now assume
\begin{itemize}
\item[-] that $X^{4}$ is an orbifold with $n$ isolated singularities $p_{1}, \ldots, p_{n}$;
\item[-] that $\left(X^{4}, g_{\infty}\right)$ is Hermitian and Einstein, with $\lambda>0$;
\item[-] that there is an admissible sequence $\left(M, g_{i}\right)$ with
$$d_{G H}\left(\left(M, g_{i}\right),\left(X, g_{\infty}\right)\right) \rightarrow 0 ; \quad \text { and }$$
\item[-] that no trees of singularities arise in this limiting process.
\end{itemize}

By [43], then, up to taking a subsequence, for $i$ large enough, there exist $t_{i}>0$, along with naïve desingularizations $g_{t_{i}}^{D}$ and parameters
$$v_{i} \in \mathfrak{O}\left(g_{b_{1}}\right) \times \ldots \times \mathfrak{O}\left(g_{b_{n}}\right) \times \mathfrak{O}\left(g_{\infty}\right)$$
for which
\begin{itemize}
\item[-] $\left\|g_{i}-g_{t_{i}, v_{i}}^{A_{n}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g_{t_{i}}^{D}\right)} \rightarrow 0$, and
\item[-] $g_{i}-g_{t_{i}, v_{i}}^{A_{n}} \perp_{g_{t_{i}}^{D}} \tilde{\mathfrak{O}}\left(g_{t_{i}, v_{i}}^{A_{n}}\right)$.
\end{itemize}

Since our assumptions in particular imply that $M$ has the expected topology, and all of the Ricci-flat ALE spaces arising from curvature concentration are Kähler, our assumption that no trees of singularities arise then implies [43, §7.1] that, after passing to a subsequence and up to a diffeomorphism, $g_{i}=\hat{g}_{t_{i}, v_{i}}^{n}$ for one of the above $\hat{g}_{t_{i}, v_{i}}^{n}$. In particular, $g_{i}$ is an Einstein metric satisfying Wu's criterion $\operatorname{det} \mathrm{W}^{+}\left(g_{i}\right)>0$, and it therefore follows [34, 46] that, for $i$ large enough, the $g_{i}$ are necessarily conformally Kähler. However, as previously noted, such metrics on a smooth 4-manifold $M$ are actually Kähler-Einstein unless [31] there is, up to isometries and rescalings, only one conformally-Kähler Einstein manifold on $M$. Theorems A and B thus now follow in the case where no trees of singularities arise. \(\square\)

Combining this with Proposition 4.3 now yields the following application:
Corollary 9.2. Let $\left(X^{4}, g_{\infty}\right)$ be a Kähler-Einstein orbifold with at least one singular point. If $c_{1}^{2}(X) \geq 4$, and if ( $X, g_{\infty}$ ) is the Gromov-Hausdorff limit of an admissible sequence $\left(M, g_{i}\right)$ of smooth $\lambda>0$ Einstein 4-manifolds, then $c_{1}^{2}(X)=4$, and $M \approx \mathbb{C P}_{2} \# 5 \overline{\mathbb{C P}}_{2}$.

Proof. When $c_{1}^{2}(X) \geq 4$ and $\left(X, g_{\infty}\right)$ is Kähler-Einstein, Proposition 4.3 tells us that each singularity of $X$ is modeled on $\mathbb{C}^{2} / \mathbb{Z}_{2}$, and this in particular excludes the formation of bubble-trees. The above argument therefore shows that the Einstein 4-manifolds $\left(M, g_{i}\right)$ must be Hermitian for all sufficiently large $i$. However, classification [31] tells us that, up to isometry and rescalings, there is at most one $\lambda>0$ Hermitian, Einstein metric on the underlying smooth 4-manifold $M$ of a complex surface with $c_{1}^{2} \geq 5$. When $c_{1}^{2}(X) \geq 4$, singularities can therefore only form in the limit when $c_{1}^{2}(M)=c_{1}^{2}(X)=4$ and $M$ is diffeomorphic to $\mathbb{C P}_{2} \# 5 \overline{\mathbb{C P}}_{2}$. \(\square\)

\section*{10 The General Case}

Finally, we deal with trees of singularities by further refining our notion of approximate Einstein-modulo-obstructions metric. In fact, our proof of Proposition 2.2 already depended on the reason why it is possible to handle trees of Ricci-flat Kähler ALE metrics: when glued together in the expected
manner, they can always be approximated by a single Ricci-flat Kähler ALE metric [43]. The essence of what we will now do amounts to a controlled, quantitative implementation of this observation. While there are more elementary ways of carrying this out for the Gibbons-Hawking gravitational instantons, our proof will be geared to handle the general case.

\section*{Asymptotics of the building blocks}

We will now consider:
\begin{itemize}
\item[-] $\left(N_{1}, \bar{g}_{v_{b_{1}}}\right)$ a Ricci-flat ALE orbifold with a singularity at $p_{1}$, and
\item[-] $\left(N_{2}, \bar{g}_{v_{b_{2}}}\right)$ glued at scale $t_{2}$ at a remaining singular point $p_{1}$ of $\left(N_{1}, \bar{g}_{v_{b_{1}}}\right)$.
\end{itemize}

We have the following expansions of the different metrics: for any $l \leqslant 4$,
\begin{itemize}
\item[-] at its singular point $p_{1}: \bar{g}_{v_{b_{1}}}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}_{4}+\ldots+\mathfrak{H}_{l}+\mathrm{O}\left(\rho_{b_{1}}^{l+1}\right)$
\item[-] at its infinity: $\bar{g}_{v_{b_{2}}}=\boldsymbol{\delta}+\mathfrak{H}^{4}+\ldots+\mathfrak{H}^{l}+\mathrm{O}\left(\rho_{b_{2}}^{l+1}\right)$.
\end{itemize}
In particular, developing the equations $\mathscr{F}_{\boldsymbol{\delta}}\left(g_{b_{1}}\right)=0$ and $\mathscr{F}_{\boldsymbol{\delta}}\left(g_{b_{2}}\right)=0$ according to powers of $r_{b_{1}}$ and $r_{b_{2}}$ the above tensors satisfy equalities:
\begin{itemize}
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{H}_{i}+Q_{\boldsymbol{\delta}}^{[i],+}\left(\mathfrak{H}_{2}, \mathfrak{H}_{3}, \ldots, \mathfrak{H}_{i-1}\right)=0$, and
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{H}^{j}+Q_{\boldsymbol{\delta}}^{[j],-}\left(\mathfrak{H}^{4}, \mathfrak{H}^{5}, \ldots, \mathfrak{H}^{j-1}\right)=0$,
\end{itemize}
where $Q_{\delta}^{[j], \pm}$ are specific finite sums of multilinear operations on the tensors and their two first derivatives. The key point is that $Q_{\delta}^{[i],+}\left(\mathfrak{H}_{2}, \mathfrak{H}_{3}, \ldots, \mathfrak{H}_{i-1}\right)=$ $\mathrm{O}\left(\varrho^{i-2}\right)$, and $Q_{\boldsymbol{\delta}}^{[j],-}\left(\mathfrak{H}^{4}, \mathfrak{H}^{5}, \ldots, \mathfrak{H}^{j-1}\right)=\mathrm{O}\left(\varrho^{-j-2}\right)$.

\section*{Approximations of Ricci-flat Kähler metrics}

When $v_{b}=\left(v_{b_{1}}, t_{2}, v_{b_{2}}\right)$ is sufficiently small, we will use $g_{v_{b}}^{B}$ to denote the naïve gluing $\bar{g}_{v_{1}} \#_{p_{1}, t_{2}} \bar{g}_{v_{b_{2}}}$ and let $\varrho_{b}$ be the associated extension of $\varrho_{D}$ of Definition 7. By [43, Section 6.2], there is a unique Ricci-flat Kähler ALE metric $\bar{g}_{v_{b}}$ that, for some $\epsilon>0$, satisfies
\begin{itemize}
\item[1.] $\mathscr{F}_{g_{v_{b}}^{B}}\left(\bar{g}_{v_{b}}\right)=0$,
\item[2.] $\left\|\bar{g}_{v_{b}}-g_{v_{b}}^{B}\right\|_{C_{\beta, * *}^{2, \alpha}} \leqslant \epsilon$, and
\end{itemize}
3. $\bar{g}_{v_{b}}-g_{v_{b}}^{B} \perp_{L^{2}\left(g_{b}\right)} \tilde{\mathfrak{D}}\left(g_{v_{b}}^{B}\right)$,
where $C_{\beta, * *}^{2, \alpha}\left(g_{v_{b}}^{B}\right)$ is defined in Definition 16 below. We emphasize that this construction reaches all nearby Ricci-flat ALE metrics.

The results of [43, Section 6.2] tell us that any Einstein-modulo-obstructions perturbation of a tree of Ricci-flat Kähler ALE metrics is in fact a Ricci-flat Kähler ALE metric. For any $l \in \mathbb{N}$, this metric can then be approximated by a naïve gluing:
$$g_{v_{b}}^{B,[l]}:=\left(\bar{g}_{v_{b_{1}}}+\sum_{j=4}^{l} t_{2}^{\frac{j}{2}} h^{j}\right) \#_{p_{1}, t_{2}}\left(\bar{g}_{v_{b_{2}}}+\sum_{i=2}^{l} t_{2}^{\frac{i}{2}} h_{i}\right),$$
where for $i, j \leqslant 4$, one defines the $h_{i}$ and $h^{j}$ as in (18), (19), (21) where all of the obstructions $\mho_{i}$ and $\mathbf{w}^{4}$ vanish. Following (22), we now solve iteratively for $i, j \geqslant 4$ by applying the following two steps:
1. first, solve the system
$$\begin{aligned}
& P_{\bar{g}_{v_{b_{1}}}} h^{j}=-Q_{\bar{g}_{v_{b_{1}}}}^{[j],-}\left(h^{4}, \ldots, h^{j-1}\right) \\
& \quad h^{j}=\sum_{i \leqslant j-1} \mathfrak{H}_{i}^{j}+\mathfrak{H}_{j}^{j}+\mathrm{O}\left(\varrho^{-1-\epsilon}\right), \quad \forall \epsilon>0 \\
& \int_{\Sigma}\left\langle h^{j}, \mho_{v_{b_{1}}}\right\rangle_{\bar{g}_{v_{b_{1}}}} d a_{\left(\bar{g}_{v_{b_{1}} \mid \Sigma}\right)}=0 \quad \forall \mho_{v_{b_{1}}} \in \mathfrak{O}\left(\bar{g}_{v_{b_{1}}}\right)
\end{aligned}$$
where $Q_{\bar{g}_{v_{1}}}^{[j],-}$ involves the nonlinear terms in $h^{l}$ for $l \leqslant j-1$ appearing when solving $\mathscr{F}_{\bar{g}_{b_{1}}}(g)=0$, and where the $\mathfrak{H}_{i}^{j}$ for $i \leqslant j-1$ are determined by the previously defined $h_{i}$. In order to solve this equation, notice that for $\tilde{\Upsilon}$ a cut-off function supported in a neighborhood of $p_{1}$
$$P_{\bar{g}_{v_{b_{1}}}}\left(\tilde{\Upsilon} \sum_{i \leqslant j-1} \mathfrak{H}_{i}^{j}\right)-Q_{\bar{g}_{v_{b_{1}}}^{[j],-}}\left(h^{4}, \ldots, h^{j-1}\right)=\mathrm{O}\left(r_{b_{1}}^{-2-\epsilon}\right), \quad \forall \epsilon>0,$$
hence, by [40, Lemma 4.42], one can find $h^{\prime}$ such that
$$P_{\bar{g}_{v_{b_{1}}}}\left(h^{\prime}+\tilde{\Upsilon} \sum_{i \leqslant j-1} \mathfrak{H}_{i}^{j}\right)-Q_{\bar{g}_{v_{b_{1}}}^{[j],-}}\left(h^{4}, \ldots, h^{j-1}\right) \in \mathfrak{O}\left(\bar{g}_{v_{b_{1}}}\right) .$$

Since the gluing is unobstructed by [43, Section 6.2], one then shows iteratively that the element of $\mathfrak{O}\left(\bar{g}_{v_{b_{1}}}\right)$ vanishes, and $h^{\prime}=\mathfrak{H}_{j}^{j}+\mathrm{O}\left(\varrho^{-1-\epsilon}\right)$ for $\mathfrak{H}_{j}^{j}=\mathrm{O}\left(\varrho^{-\epsilon}\right)$ for all $\epsilon>0$, and in fact, for any $L \geqslant 2$ and $\epsilon>0$, there is a neighborhood of infinity where
$$h^{\prime}=\mathfrak{H}_{j}^{j}+\sum_{l=j+1}^{L} \mathfrak{H}_{l}^{j}+\mathrm{O}\left(\varrho_{o}^{L-j-\epsilon}\right),$$
2. then, one similarly solves the equation
$$\begin{aligned}
& P_{\bar{g}_{v_{b}}} h_{j}=-Q \bar{g}_{v_{b_{2}}}^{[j],+}\left(h_{2}, \ldots, h_{j-1}\right) \\
& \quad h_{j}=\sum_{i \leqslant j} \mathfrak{H}_{j}^{i}+\mathfrak{H}_{j}^{j+1}+\mathrm{O}\left(\varrho^{-2+\epsilon}\right), \quad \forall \epsilon>0 \\
& \quad \int_{\Sigma}\left\langle h_{j}, \mho_{v_{b_{2}}}\right\rangle_{\bar{g}_{v_{b_{2}}}} d a_{\left(\bar{g}_{v_{b_{2}} \mid \Sigma}\right)}=0 \text { for all } \mho_{v_{b_{2}}} \in \mathfrak{O}\left(\bar{g}_{v_{b_{2}}}\right)
\end{aligned}$$
where $Q_{\bar{g}_{v_{2}}}^{[j],+}$ involves the nonlinear terms in $h^{l}$ for $l \leqslant j$ appearing when solving $\mathscr{F}_{\bar{g}_{v_{2}}}(g)=0$, and where the $\mathfrak{H}_{j}^{i}$ for $i \leqslant j$ are determined by the previous $h^{l}$ defined. One then obtains $\mathfrak{H}_{j}^{j+1}$ determined from the unique solution of (29) such that in a neighborhood of infinity, for all $L \geqslant 4$, and $\epsilon>0 h_{j}=\sum_{l=4}^{L} \mathfrak{H}_{j}^{l}+\mathrm{O}\left(\varrho_{b}^{j-L+\epsilon}\right)$.

The point is that there are no obstructions [43, Section 6.2] which lets us estimate the metrics directly without having to approximate obstructions. Explicit computations generalizing slightly those of Proposition 23 (see also [41, Sections 2 and 3]) lead to the following result.

Proposition 10.1. For any $l \geqslant 4$ and $0<\alpha<1$ and $0<\beta<\frac{1}{4}$, there is $C>0$ independent of $v_{b}$ so that we have the control
$$\left\|\left(1+\varrho_{b}\right)^{4} \mathscr{F}_{g_{v_{b}}^{B}}\left(g_{v_{b}}^{B,[l]}\right)\right\|_{\varrho_{b}^{-2} C_{\beta}^{\alpha}\left(g_{v_{b}}^{B}\right)} \leqslant C t_{2}^{\frac{l+1-\beta}{4}}=o\left(t_{2}^{\frac{l}{4}}\right)$$
and consequently, by [40, (5.15), Lemma 5.19], we therefore have
$$\left\|\bar{g}_{v_{b}}-g_{v_{b}}^{B,[l]}\right\|_{C_{\beta, * *}^{2, \alpha}\left(g_{v_{b}}^{B}\right)} \leqslant C^{\prime} t_{2}^{\frac{l+1-\beta}{4}}=o\left(t_{2}^{\frac{l}{4}}\right)$$
for some $C^{\prime}>0$ independent of $v_{b}$,

In particular, considering $l \geqslant 9$ for $g_{b}$, we have the following controls.
Corollary 10.2. We have the following more concrete controls on $\bar{g}_{v_{b}}$ :
\begin{itemize}
\item[1.] in the region $\sqrt{t_{2}} \ll r_{b_{1}}$, or $1 \ll r_{b_{2}}$, and so in particular at infinity,
$$\bar{g}_{v_{b}}=\bar{g}_{v_{b_{1}}}+t_{2}^{2} h^{4}+o\left(t_{2}^{2} r_{b_{1}}^{-4}\right)$$
\item[2.] in the region $r_{b_{1}} \ll 1$, or $r_{b_{2}} \ll t_{2}^{-\frac{1}{2}}$
$$\bar{g}_{v_{b}}=t_{2}\left(\bar{g}_{v_{b_{1}}}+t_{2} h_{2}+t_{2}^{\frac{3}{2}} h_{3}+t_{2}^{2} h_{4}\right)+o\left(t_{2}^{2} r_{b_{2}}^{4}\right)$$
\item[3.] in the gluing region $\sqrt{t_{2}} \ll r_{b_{1}} \ll 1$ or $1 \ll r_{b_{2}} \ll t_{2}^{-\frac{1}{2}}$, we have
$$\bar{g}_{v_{b}}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}^{4}+\mathfrak{H}_{2}^{4}+\mathfrak{H}_{3}^{4}+\mathfrak{H}_{4}^{4}+\mathfrak{H}_{4}+\mathrm{O}\left(r_{b_{1}}^{5}+r_{b_{2}}^{-5}\right) .$$
\end{itemize}

We finish this section by an estimate of the variations at infinity of a tree of singularities with respect to the size of the bubbles attached to it.
\begin{itemize}
\item[-] for $l \in\{0, \ldots, k+1\}$, Ricci-flat Kähler $g_{b_{l}}$ that can be glued as a tree of singularities according to [43, Section 4.3]
\item[-] $g^{B_{k+1}}$ (resp. $g^{B_{k}}$ ), the naïve gluing of the $g_{b_{l}}$ at scales $T_{l}=t_{0} \ldots t_{l}>0$ for small enough $t_{l}>0$ as a tree for $l \in\{0, \ldots, k+1\}$ (resp. $l \in\{0, \ldots, k\}$ ),
\item[-] $\bar{g}_{B_{k+1}}$ (resp. $\bar{g}_{B_{k}}$ ) the Ricci-flat Kähler ALE perturbation of $g^{B_{k+1}}$ (resp. $\left.g^{B_{k}}\right)$,
\end{itemize}

Proposition 10.3. For any $r_{B_{k}} \gg \sqrt{T_{k+1}}$, we have, for any $l \in \mathbf{N}$, and $C_{l}>0$ depending only on $l$,
$$\varrho_{B_{k}}^{l}\left|\nabla^{l}\left(\bar{g}_{B_{k}}-\bar{g}_{B_{k+1}}\right)\right| \leqslant C_{l} T_{k+1}^{2} r_{B_{k}}^{-4} .$$

More precisely, there is a converging expansion
$$\bar{g}_{B_{k}}-\bar{g}_{B_{k+1}}=\sum_{j \geqslant 4} \mathfrak{K}^{j},$$
with $\left|\mathfrak{K}^{j}\right| \leqslant C_{j}^{\prime} T_{k+1}^{2} \varrho^{-j}$ for $C_{j}^{\prime}>0$ independent of $T_{k+1}$ or $r_{B_{k}}$.
Sketch of proof. The result can be easily obtained for the Ricci-flat Kähler ALE metrics asymptotic to $\mathbb{R}^{4} / \Gamma$ for $\Gamma \subset \operatorname{SU}(2)$ cyclic. Indeed, they are Gibbons-Hawking's gravitational instantons which are explicitly given in coordinates [20].

For the general case, one can combine the resolution of singularities described in [27, Proposition 3.10] together with the description of the asymptotic expansion of the [27, Proposition 3.14] (see also [4, Theorem 2.1]). \(\square\)

\section*{Approximate metrics with trees of singularities}

We now explain how to deal with trees of singularities.

\section*{Setting up the iterative construction}

In this section, we consider $\left(X, g_{\infty}\right)$, a conformally Kähler Einstein orbifold with scalar curvature 12 with multiple singularities of general type. We then consider a naïve desingularization of $\left(X, g_{\infty}\right)$ at all of its singularities by trees of singularities which we will denote $g_{t, v}^{D}$.

We will order our desingularizations according to their depth, that is the size of the bubbles glued.
\begin{itemize}
\item[1.] we start with $g_{t, v}^{D_{0}}:=g_{t, v}^{A_{0}}:=\hat{g}_{t, v}^{0}:=\bar{g}_{v_{o}}$ as before, and
\item[2.] given $g_{t, v}^{D_{k}}$, and the next largest scale $T_{k+1}$ at which to glue a Ricci-flat ALE metric $\bar{g}_{v_{k+1}}$ to a remaining singular point $p_{k+1}$,
$$g_{t, v}^{D_{k+1}}:=g_{t, v}^{D_{k}} \#_{p_{k+1}, T_{k}^{2} t_{k+1}} \bar{g}_{v_{k+1}} .$$
\end{itemize}

The rest of the argument mainly consists in carefully constructing approximations $g_{t, v}^{A_{k}}$ in order to control the Einstein-modulo-obstructions metrics $\hat{g}_{t, v}^{k}$ and their curvature. We will eventually reach the total Einstein-moduloobstructions desingularization and be able to control its curvature.

Proposition 10.4. For each $k \in\{1, \ldots, n\}$, we have:
\begin{itemize}
\item[1.] at every point, the eignenvalues of the self-dual curvature $W^{+}$of $\hat{g}_{t, v}^{k}$ differ form the eigenvalues of $W^{+}\left(g_{\infty}\right)$, at a suitable point of $X$, by only an error that uniformly tends to zero as $(t, v) \rightarrow(0,0)$;
\item[2.] $\left\|\hat{g}_{t, v}^{k}-g^{A_{k}}\right\|_{C_{\beta, *}^{2, \alpha}}=o\left(T_{k}\right)$, and there is $C>0$ such that for any $l \in$ $\{0,1,2,3\}$; and
$$\left|\nabla^{l}\left(\hat{g}_{t, v}^{k}-g^{D_{k}}\right)\right| \leqslant C r_{D_{k}}^{2} .$$
\end{itemize}

\section*{The iterative step}

If we have previously defined $g_{t, v}^{D_{k}}, g_{t, v}^{A_{k}}$ and $\hat{g}_{t, v}^{k}$, and $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k}}\right)$ in a suitable manner, we may then define $g_{t, v}^{A_{k+1}}$ so as to control $\hat{g}_{t, v}^{k+1}$.

If the next considered singular point $p_{k+1}$ is a singular point of $X$, then we define $g_{t, v}^{A_{k+1}}$ and obtain a control of $\hat{g}_{t, v}^{k+1}$ and its curvature exactly as in Section 9. Here, we will therefore consider the remaining case where the singular point $p_{k+1}$ belongs to another Ricci-flat ALE metric of the tree of singularities.

Note. In order to simplify our notation in the remainder of the argument, we will drop (when not necessary) the $(t, v)$-dependence of our tensors and in particular denote $g_{b_{i}}$ for $\bar{g}_{v_{b_{i}}}$. \(\square\)

Assume that:
\begin{itemize}
\item[-] $g^{D_{k}}$ and $\hat{g}^{k}$ defined from the previous steps, satisfy:
$$\mathscr{F}_{g^{D_{k}}}\left(\hat{g}^{k}\right)=\mathfrak{w}_{0}+\mathfrak{w}_{2}+\mathrm{O}\left(T_{k} r_{b_{k}}^{3}\right) \in \tilde{\mathfrak{O}}\left(g^{A_{k}}\right),$$
with $\left|\mathfrak{w}_{l}\right| \leqslant C_{l} T_{k} r_{b_{k}}^{l}$ for $C_{l}>0$,
\item[-] $g^{D_{k+1}}=g^{D_{k}} \#_{p_{k+1}, T_{k}^{2} t_{k+1}} g_{b_{k+1}}$ where $g_{b_{k+1}}$ is a Ricci-flat ALE metric with a remaining singular point $p_{1}$, and
\item[-] $\hat{g}^{k+1}$ the Einstein-modulo-obstructions perturbation of $g^{D_{k+1}}=g_{t, v}^{D_{k+1}}$ transversely to $\tilde{\mathfrak{D}}\left(g^{A_{k}}\right)$.
\end{itemize}
Our goal will now be to obtain curvature estimates for $\hat{g}^{k+1}$ using the construction of an approximate Einstein-modulo-obstructions metric. We will in particular show that the above properties stay true by iteration.

For this we will also use the following metrics.
\begin{itemize}
\item[-] $g^{B_{k+1}}$, the naïve gluing of the tree of singularity at which $g_{b_{k+1}}$ is glued in $g^{D_{k+1}}$,
\item[-] $g^{B_{k}}$, the naïve gluing of the tree of singularity at which $g_{b_{k+1}}$ is glued in $g^{D_{k+1}}$, but without $g_{b_{k+1}}$, and
\item[-] $\bar{g}_{B_{k+1}}$ (resp. $\bar{g}_{B_{k}}$ ) the Ricci-flat Kähler ALE perturbation of $g^{B_{k+1}}$ (resp. $g^{B_{k}}$ ).
\end{itemize}

The rest of the section consists in constructing a suitable approximate Einstein-modulo-obstructions metric $g^{A_{k+1}}$ controlling $\hat{g}^{k+1}$ in $o\left(T_{k+1}\right)$ in order to compensate the $\varrho_{D}^{-2}$ term of our function space. For this, we will
leverage the fact that both $\hat{g}^{k}$ and $\bar{g}_{B_{k}}$ satisfy exact equations in order to rule out errors in powers of $T_{k}$ alone or in powers of $t_{k+1}$ alone. The following key technical lemma follows from the expansion of Ricci curvature at a metric $g$ in the (small) direction $h$ :
$$r(g+h)=r(g)+(g+h)^{-1} * \mathcal{R}(g)+(g+h)^{-2} * \nabla^{2} h+(g+h)^{-3} * \nabla h * \nabla h,$$
where $*$ corresponds to contractions of tensors.
Lemma 10.5. Let $g$ be an Einstein metric on an open set $U \subset \mathbb{R}^{4}$ such that $\left|\nabla_{\boldsymbol{\delta}}^{l}(g-\boldsymbol{\delta})\right|_{\boldsymbol{\delta}}<\frac{1}{100}$ for $l \leqslant L$. Assume that there exist 2-tensors $h_{1}$ and $h_{2}$ small enough in $C^{L}(U, \boldsymbol{\delta})$ such that $\mathscr{F}_{g}\left(g+h_{i}\right)=w_{i}$ for $i \in\{1,2\}$.

Then, we have the following control: there exists a $C_{L}>0$, independent of $g, h_{1}$, and $h_{2}$, such that, for $l \in\{0, \ldots$,$\} ,$
$$\left|\nabla_{g}^{l}\left(\mathscr{F}_{g}\left(g+h_{1}+h_{2}\right)-w_{1}-w_{2}\right)\right|_{g} \leqslant C_{L} \sum_{l_{1}+l_{2}=l o r(l+2)}\left|\nabla_{g}^{l_{1}} h_{1}\right|\left|\nabla_{g}^{l_{2}} h_{2}\right| .$$

Remark. The assumption on $g$ always holds in suitably rescaled harmonic coordinates, whether our space is a manifold or an orbifold; cf. e.g. [24]. ◇

Near the singular point $p_{k+1}$, we have the following expansions of the relevant metrics:
$$\begin{gathered}
\bar{g}_{B_{k}}=\boldsymbol{\delta}+\mathfrak{H}_{2}+\mathfrak{H}_{3}+\mathfrak{H}_{4}+\mathrm{O}\left(r_{b_{1}}^{5}\right) \\
T_{k}^{-1} \hat{g}^{k}=\bar{g}_{B_{k}}+\mathfrak{K}_{0}+\mathfrak{K}_{2}+\mathfrak{K}_{3}+\mathfrak{K}_{4}+\mathrm{O}\left(T_{k} r_{B_{k}}^{5}\right),
\end{gathered}$$
where $\left|\mathfrak{K}_{i}\right| \leqslant T_{k} r_{B_{k}}^{i}$. In particular, by the equation satisfied by $\hat{g}_{t, v}^{k}$ and (32), the above tensors satisfy the following equalities:
\begin{itemize}
\item[-] $P_{\delta} \mathfrak{K}_{0}=0$
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{K}_{2}+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{H}_{2}\right)=\Lambda\left(\boldsymbol{\delta}+\mathfrak{K}_{0}\right)+\mathfrak{w}_{0}$,
\item[-] $P_{\delta} \mathfrak{K}_{3}+Q_{\delta}\left(\mathfrak{K}_{0}, \mathfrak{H}_{3}\right)=0$,
\item[-] $P_{\boldsymbol{\delta}} \mathfrak{K}_{4}+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{H}_{4}\right)+Q_{\boldsymbol{\delta}}\left(\mathfrak{H}_{2}, \mathfrak{K}_{2}\right)+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{H}_{2}, \mathfrak{H}_{2}\right)+Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{K}_{2}, \mathfrak{H}_{2}\right)+$ $Q_{\boldsymbol{\delta}}\left(\mathfrak{K}_{0}, \mathfrak{K}_{2}, \mathfrak{K}_{2}\right)=\Lambda\left(\mathfrak{H}_{2}+\mathfrak{K}_{2}\right)+\mathfrak{w}_{2}$.
\end{itemize}

Extending the results of Section 8, we define the following tensors extending the above ones: given the $h_{i}$ of (29), and $w_{0}$ and $w_{2}$ extensions of $\mathfrak{w}_{0}$ and $\mathfrak{w}_{2}$ of (32) as in Section 8,
\begin{itemize}
\item[-] $P_{\bar{g}_{v_{2}}} k_{0}=0$
\item[-] $P_{\bar{g}_{v_{2}}} k_{2}+Q_{\bar{g}_{v_{2}}}\left(k_{0}, h_{2}\right)-\Lambda\left(\bar{g}_{v_{b_{2}}}+k_{0}\right)-w_{0}=\mho_{2} \in \mathfrak{O}\left(\bar{g}_{v_{b_{2}}}\right)$,
\item[-] $P_{\bar{g}_{v_{2}}} k_{3}+Q_{\bar{g}_{v_{2}}}\left(k_{0}, h_{3}\right)=0$,
\item[-] $P_{\bar{g}_{v_{2}}} k_{4}+Q_{\bar{g}_{v_{2}}}\left(k_{0}, h_{4}\right)+Q_{\bar{g}_{v_{b_{2}}}}\left(h_{2}, h_{2}\right)+Q_{\bar{g}_{v_{b_{2}}}}\left(k_{0}, h_{2}, h_{2}\right)+Q_{\bar{g}_{v_{2}}}\left(k_{0}, k_{2}, h_{2}\right)+$ $Q_{\bar{g}_{v_{b_{2}}}}\left(k_{0}, k_{2}, k_{2}\right)-\Lambda\left(h_{2}+k_{2}\right)-w_{2}=\mho_{4} \in \mathfrak{O}\left(\bar{g}_{v_{b_{2}}}\right)$.
\end{itemize}

Define $\Upsilon_{t}$ to be a cut-off function supported on $r_{D_{k}}<2 t_{k_{0}}^{\frac{1}{4}}$ and equal to 1 on $r_{D_{k}}<t_{k_{0}}^{\frac{1}{4}}$ satisfying for some $C_{l}$ independent of $t$, or $r_{D_{k}}$,
$$\nabla_{g_{k}^{D}}^{l} \Upsilon_{t} \leqslant C_{l} r_{D_{k}}^{l} .$$
Next, define an approximate Einstein-modulo-obstructions metric as:
$g^{A_{k+1}}:=\left(\hat{g}^{k}+\Upsilon_{t}\left(\bar{g}_{B_{k+1}}-\bar{g}_{B_{k}}\right)\right) \widetilde{\#}_{p_{k+1}, T_{k}, t_{k+1}}\left(T_{k+1}^{-1} \bar{g}_{B_{k+1}}+k_{0}+t_{k+1} k_{2}+t_{k+1}^{3 / 2} k_{3}+t_{k+1}^{2} k_{4}\right)$,
where $\widetilde{\#}$ is essentially the same operation introduced in Definition 6, but with the gluing scale $t^{\frac{1}{4}}$ replaced by $T_{k}^{\frac{1}{2}} t_{k+1}^{\frac{2}{9}}$. Finally, define the obstruction space $\tilde{\mathfrak{O}}\left(g^{A_{k+1}}\right)$ as the set of $\tilde{\mathfrak{o}}+\tilde{\mathbf{w}}$ for $\mathfrak{o} \in \mathfrak{O}\left(g_{b_{k+1}}\right)$ and $\mathbf{w} \in \tilde{\mathfrak{D}}\left(g^{A_{k}}\right)$, where $\tilde{\mathfrak{O}}$ and $\tilde{\mathbf{w}}$ are defined as in Definition 9 We also extend the definition of $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k+1}}\right)$ exactly as in Section 8 replacing $\bar{g}_{v_{o}}$ by $g_{t, v}^{A_{k}}$ and $\mathfrak{O}\left(g_{\infty}\right)$ by $\tilde{\mathfrak{O}}\left(g_{t, v}^{A_{k}}\right)$.

\section*{Approximate metrics with trees of singularities}

We now control how close we are to the actual Einstein-modulo-obstructions metric. This proves the last point of Proposition 10.4.

Proposition 10.6. We have the following control:
$$\left\|\mathscr{F}_{g^{D_{k+1}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right\|_{\varrho_{D}^{-2} C_{\beta}^{\alpha}\left(g^{D_{k+1}}\right)} \leqslant o\left(T_{k+1}\right) .$$
Thus, by [43, Proposition 5.11], we have $\left\|\hat{g}_{t, v}^{k+1}-g^{A_{k+1}}\right\|_{C_{\beta, *}^{2, \alpha}\left(g^{D_{k+1}}\right)}=o\left(T_{k+1}\right)$. In particular, since $r_{D_{k+1}} \geqslant T_{k+1}$ there is $C>0$ such that for any $l \in$ \{0, 1, 2, 3\},
$$\left|\nabla^{l}\left(\hat{g}_{t, v}^{k+1}-g^{D_{k+1}}\right)\right|_{g^{D_{k+1}}} \leqslant C r_{D_{k+1}}^{2} .$$

Proof. There are three regions to consider, and we will control our operator on each of them.
\begin{itemize}
\item[1.] In the region where we have $g^{A_{k+1}}=\hat{g}^{k}+\Upsilon_{t}\left(\bar{g}_{B_{k+1}}-\bar{g}_{B_{k}}\right)$, thanks to the local controls of Lemma 10.5 applied to $g$ (30) and (31) we find:
$$r_{D_{k}}^{2+l}\left|\nabla_{g_{k}^{D}}^{l}\left(\mathscr{F}_{g^{D_{k}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right)\right|_{g^{D_{k}}}=\mathrm{O}\left(T_{k+1}^{2} r_{D_{k}}^{-4} r_{D_{k}}^{2}\right) .$$
\item[2.] In the region $t_{k_{0}}^{\frac{1}{4}}<r_{D_{k}}<2 t_{k_{0}}^{\frac{1}{4}}$, thanks to (30) and the controls (33) of the cut-off function, we find:
$$r_{D_{k}}^{2+l}\left|\nabla_{g_{k}^{D}}^{l}\left(\mathscr{F}_{g^{D_{k}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right)\right|_{g^{D_{k}}}=\mathrm{O}\left(T_{k+1}^{2} r_{D_{k}}^{-4}\right)=\mathrm{O}\left(T_{k+1}^{2} t_{k_{0}}\right)=o\left(T_{k+1}\right) .$$
\item[3.] Since $T_{k+1}^{-1} g_{t, v}^{A}=T_{k+1}^{-1} \bar{g}_{B_{k+1}}+k_{0}+t_{k+1} k_{2}+t_{k+1}^{3 / 2} k_{3}+t_{k+1}^{2} k_{4}$, using (31), we find:
$$r_{D_{k+1}}^{2+l}\left|\nabla_{g_{k+1}^{D}}^{l}\left(\mathscr{F}_{g^{D_{k+1}}}\left(g^{A_{k+1}}\right)-\mho^{A_{k+1}}\right)\right|_{g^{D_{k+1}}}=\mathrm{O}\left(T_{k} t_{k+1}^{\frac{5}{2}} r_{b_{k+1}}^{5}\right) .$$
Here, the error comes from multilinear terms involving the following tensors such that for all $l \leqslant 3$, there exists $C_{l}>0$ so that
$$r_{b_{k+1}}^{l}\left|\nabla_{b_{k+1}}^{l}\left(t_{k+1}^{\frac{i}{2}} k_{i}\right)\right|_{g_{b_{k+1}}} \leqslant T_{k} t_{k+1}^{\frac{i}{2}} r_{b_{k+1}}^{i}$$
by (31), and $r_{b_{k+1}}^{l}\left|\nabla_{g_{b_{k+1}}}^{l}\left(t_{k+1}^{-1} \bar{g}_{B_{k+1}}-g_{b_{k+1}}\right)\right|_{g_{b_{k+1}}} \leqslant t_{k+1} r_{b_{k+1}}^{2}$ by Proposition 10.1.
\item[4.] Lastly, in the cut-off region $T_{k}^{\frac{1}{2}} t_{k+1}^{\frac{2}{9}}<r_{D_{k+1}}<2 T_{k}^{\frac{1}{2}} t_{k+1}^{\frac{2}{9}}$, the difference of the metrics is in:
$$T_{k} r_{b_{k}}^{5}+T_{k} r_{b_{k+1}}^{-4} .$$
\end{itemize}

Putting all of this together, we consequently obtain the stated estimate by gluing at scale $t_{k+1}^{\frac{1}{5}} \ll r_{b_{k+1}} \ll t_{k+1}^{\frac{1}{4}}$, which is satisfied by the scale of gluing chosen in the definition of $g^{A_{k+1}}$. \(\square\)

Mimicking the proof of the third point of Proposition 9.1 now yields the following result.

Corollary 10.7. If the eigenvalues of the self-dual Weyl curvature $W^{+}$of $\hat{g}^{k}$ are, are uniformly close to those of $g_{\infty}$ at some corresponding point of $X$, then the eigenvalues of the self-dual Weyl curvature $W^{+}$of $\hat{g}^{k+1}$ also have this property, with an error that uniformly tends to zero as $(t, v) \rightarrow 0$.

\section*{Conclusion of the proof}

Let us now assume that the $\lambda>0$ Einstein orbifold ( $X, g_{\infty}$ ) is conformally Kähler, and that there is an admissible sequence $\left(M, g_{i}\right)$ with
$$d_{G H}\left(\left(M, g_{i}\right),\left(X, g_{\infty}\right)\right) \rightarrow 0 .$$
By [42], after passing to a subsequence indexed by $j$, and for sufficiently large $j$, there thus exist naïve desingularizations $g_{t_{j}}^{D}$ such that $\left\|g_{j}-g_{t_{j}}^{D}\right\|_{C_{\beta_{, *}}^{2, \alpha}\left(g_{t_{j}}^{D}\right)} \rightarrow 0$, possibly with the involvement of trees of singularities. After perhaps refining our subsequence, the associated gluing scales $T_{k, j}>0$ in the tree can then be ordered such that, for all $j$,
$$T_{1, j} \leqslant T_{2, j} \leqslant \ldots \leqslant T_{n, j} .$$
By [42, 43], each $g_{j}$ is then isometric to some such $\hat{g}_{t_{j}, v_{j}}^{n}$ for $j \gg 0$.
However, the two lowest eigenvalues of $W^{+}$are everywhere negative and equal for the conformally Kähler $\lambda>0$ Einstein orbifold metric $g_{\infty}$. By Corollary 10.7, it therefore follows, for $j \gg 0$, that the two lowest eigenvalues of the self-dual Weyl curvatures $W^{+}$of our Einstein metrics $g_{j}$ are therefore everywhere negative. Since $W^{+} \in \operatorname{End}\left(\Lambda^{+}\right)$is trace-free, this means that these $g_{j}$ must have $\operatorname{det}\left(W^{+}\right)>0$ everywhere. Thus, all but a finite number of the Einstein metrics $g_{j}$ must actually satisfy Wu's criterion (1).

It is therefore a formal consequence that all but a finite number of the original $g_{i}$ must also satisfy ( 1 ). Indeed, there would otherwise be a subsequence $\left\{g_{j^{\prime}}\right\} \subset\left\{g_{i}\right\}$ consisting of Einstein metrics that do not satisfy (1). But since the $\left\{g_{j^{\prime}}\right\}$ would still be an admissible sequence converging to $\left(X, g_{\infty}\right)$, the above argument would then demonstrate that (1) must hold for an infinite number of the $\left\{g_{j^{\prime}}\right\}$, and this is of course a contradiction. This shows that, for all $i \gg 0$, the original $\left\{g_{i}\right\}$ must actually satisfy (1), and must therefore [34, 46] be conformally Kähler.

The classification [31, Theorem A] of conformally Kähler, Einstein metrics on smooth, compact 4-manifolds therefore tells us that these $\left(M, g_{i}\right)$ must actually be Kähler-Einstein unless $M$ is either $\mathbb{C P}_{2} \# \overline{\mathbb{C P}}_{2}$ or $\mathbb{C P}_{2} \# 2 \overline{\mathbb{C P}}_{2}$, equipped with a constant multiple of the Page metric or the Chen-LeBrun-Weber metric, respectively. Since these exceptional metrics are also, up to isometry and rescaling, the only conformally Kähler, Einstein metrics on these exceptional manifolds, the ( $M, g_{i}$ ) must in fact be Kähler-Einstein for $i \gg 0$ if we assume that $\left(X, g_{\infty}\right)$ either has an orbifold singularity, or is itself Kähler-Einstein. Theorems A and B thus now follow, as promised. \(\square\)

\section*{A Function Spaces}

For a tensor $s$, a point $x, \alpha>0$ and a Riemannian manifold $(M, g)$. The Hölder seminorm is defined as
$$[f]_{C^{\alpha}(g)}(x):=\sup _{\left\{y \in T_{x} M,|y|<\operatorname{inj}_{g}(x)\right\}}\left|\frac{f(x)-f\left(\exp _{x}^{g}(y)\right)}{|y|^{\alpha}}\right|_{g} .$$

For orbifolds, we consider a norm which is bounded for tensors decaying at the singular points.

Definition 12 (Weighted Hölder norms on an orbifold). Let $\beta \in \mathbb{R}, k \in \mathbb{N}$, $0<\alpha<1$ and $\left(X, g_{\infty}\right)$ an orbifold. Then, for any tensor $s$ on $X$, we define
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g_{\infty}\right)}:=\sup _{X} \varrho_{o}^{-\beta}\left(\sum_{i=0}^{k} \varrho_{o}^{i}\left|\nabla_{g_{\infty}}^{i} s\right|_{g_{\infty}}+\varrho_{o}^{k+\alpha}\left[\nabla_{g_{\infty}}^{k} s\right]_{C^{\alpha}\left(g_{\infty}\right)}\right) .$$

For ALE manifolds, we will consider a norm which is bounded for tensors decaying at infinity.

Definition 13 (Weighted Hölder norms on an ALE orbifold). Let $\beta \in \mathbb{R}$, $k \in \mathbb{N}, 0<\alpha<1$ and $\left(N, g_{b}\right)$ be an ALE manifold. Then, for any tensor $s$ on $N$, we define
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g_{b}\right)}:=\sup _{N} \varrho_{b}^{\beta}\left(\sum_{i=0}^{k} \varrho_{b}^{i}\left|\nabla_{g_{b}}^{i} s\right|_{g_{b}}+\varrho_{b}^{k+\alpha}\left[\nabla_{g_{b}}^{k} s\right]_{C^{\alpha}\left(g_{b}\right)}\right) .$$

Next, using a partition of unity
$$1=\Upsilon_{X^{t}}+\sum_{j} \Upsilon_{N_{j}^{t}}$$
on $M$, where $\Upsilon_{X^{t}}$ equals 1 when $g_{t}^{D}=g_{\infty}$ and $\Upsilon_{N_{j}^{t}}$ equals 1 where $g_{t}^{D}=t_{j} g_{b_{j}}$ (see [42]), we can define a global norm.

Definition 14 (Weighted Hölder norm on a naïve desingularization). Let $\beta \in \mathbb{R}, k \in \mathbb{N}$ and $0<\alpha<1$. We define for $s \in T M^{\otimes l_{+}} \otimes T^{*} M^{\otimes l_{-}}$a tensor $\left(l_{+}, l_{-}\right) \in \mathbb{N}^{2}$, with $l:=l_{+}-l_{-}$the associated conformal weight,
$$\|s\|_{C_{\beta}^{k, \alpha}\left(g^{D}\right)}:=\left\|\Upsilon_{X^{t}} s\right\|_{C_{\beta}^{k, \alpha}\left(g_{\infty}\right)}+\sum_{j} T_{j}^{\frac{l}{2}}\left\|\Upsilon_{N_{j}^{t}} s\right\|_{C_{\beta}^{k, \alpha}\left(g_{b_{j}}\right)} .$$

\section*{Decoupling norms.}

For each singular point $p_{k}$, we consider the annuli $A_{k}\left(t, \epsilon_{0}\right):=\left(\Phi_{k}\right)_{*} A_{\boldsymbol{\delta}}\left(\epsilon_{0}^{-1} \sqrt{t_{k}}, \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0}\right):=\left(\Phi_{k}\right)_{*} B_{\boldsymbol{\delta}}\left(0, \epsilon_{0}\right)$, as well as cut-off functions $\Upsilon_{A_{k}\left(t, \epsilon_{0}\right)}$ and $\Upsilon_{B_{k}\left(\epsilon_{0}\right)}$ respectively supported in $A_{k}\left(t, \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0}\right)$, and equal to 1 on $A_{k}\left(t, 2 \epsilon_{0}\right)$ and $B_{k}\left(\epsilon_{0} / 2\right)$.

Definition 15 ( $C_{\beta, *}^{k, \alpha}$-norm on 2-tensors). Let $h$ be a 2-tensor on $\left(M, g^{D}\right)$, $\left(X, g_{\infty}\right)$ or $\left(N, g_{b}\right)$. We define its $C_{\beta, *}^{k, \alpha}$-norm by
$$\|h\|_{C_{\beta, *}^{k, \alpha}}:=\inf _{h_{*}, \mathfrak{H}_{k}}\left\|h_{*}\right\|_{C_{\beta}^{k, \alpha}}+\sum_{k}\left|\mathfrak{H}_{k}\right|_{\delta},$$
where the infimum is taken on the $\left(h_{*},\left(\mathfrak{H}_{k}\right)_{k}\right)$ satisfying $h=h_{*}+\sum_{k} \Upsilon_{A_{k}\left(t, \epsilon_{0}\right)} \mathfrak{H}_{k}$ for $\left(M, g^{D}\right)$ or $h=h_{*}+\sum_{k} \Upsilon_{B_{k}\left(\epsilon_{0}\right)} \mathfrak{H}_{k}$ for $\left(X, g_{\infty}\right)$ or $\left(N, g_{b}\right)$, where each $\mathfrak{H}_{k}$ is some constant and trace-free symmetric 2 -tensors on $\mathbb{R}^{4} / \Gamma_{k}$.

Finally, we also introduce a function space that is particularly well-suited to Ricci-flat ALE spaces; cf. [40, Definition 5.18].

Definition 16 ( $C_{\beta, * *}^{2, \alpha}$ norm on an ALE orbifold). Let ( $N, g_{b}$ ) be an ALE orbifold, let $h$ be a 2 -tensor on $N$, and assume that $h=\mathfrak{H}^{4}+\mathrm{O}\left(\varrho_{b}^{-4-\beta}\right)$ for $\beta>0$. For $\Upsilon$, a cut-off function supported in $N-K$. We define the $C_{\beta, * *}^{2, \alpha}$-norm of $h$ as:
$$\|h\|_{C_{\beta, * *}^{2, \alpha}}:=\sup \varrho_{b}^{4}\left|\mathfrak{H}^{4}\right|_{g_{\delta}}+\left\|\left(1+\varrho_{b}\right)^{4}\left(h-\Upsilon \mathfrak{H}^{4}\right)\right\|_{C_{\beta, \phi}^{2, \alpha}} .$$

Note that this definition actually corrects a minor error in [43] that is fortunately harmless in most contexts. For a detailed discussion of this point, see [23, Remark A.12] concerning Ricci-flat Kähler ALE metrics.

Acknowledgments. The authors would like to thank the Simons Center for Geometry and Physics for its hospitality during the completion of this article. The first author would also like to express his gratitude to the Simons Foundation and the Fondation Sciences Mathématiques de Paris for their partial financial support of this research.

\section*{References}
[1] M. T. Anderson, Ricci curvature bounds and Einstein metrics on compact manifolds, J. Amer. Math. Soc., 2 (1989), pp. 455-490.
[2] M. T. Anderson and J. Cheeger, Diffeomorphism finiteness for manifolds with Ricci curvature and $L^{n / 2}$-norm of curvature bounded, Geom. Funct. Anal., 1 (1991), pp. 231-252.
[3] V. Apostolov and P. Gauduchon, Selfdual Einstein Hermitian four-manifolds, Ann. Sc. Norm. Super. Pisa Cl. Sci. (5), 1 (2002), pp. 203-243.
[4] H. Auvray, From ALE to ALF gravitational instantons, Compos. Math., 154 (2018), pp. 1159-1221.
[5] S. Bando, Bubbling out of Einstein manifolds, Tohoku Math. J. (2), 42 (1990), pp. 205-216.
[6] -, Correction and addition: "Bubbling out of Einstein manifolds", Tohoku Math. J. (2), 42 (1990), pp. 587-588.
[7] S. Bando, A. Kasue, and H. Nakajima, On a construction of coordinates at infinity on manifolds with fast curvature decay and maximal volume growth, Invent. Math., 97 (1989), pp. 313-349.
[8] A. L. Besse, Einstein Manifolds, vol. 10 of Ergebnisse der Mathematik und ihrer Grenzgebiete (3), Springer-Verlag, Berlin, 1987.
[9] O. Biquard, Désingularisation de métriques d'Einstein. I, Invent. Math., 192 (2013), pp. 197-252.
[10] -, Désingularisation de métriques d'Einstein. II, Invent. Math., 204 (2016), pp. 473-504.
[11] C. P. Boyer, Conformal duality and compact complex surfaces, Math. Ann., 274 (1986), pp. 517-526.
[12] C. P. Boyer and K. Galicki, Sasakian geometry, Oxford Mathematical Monographs, Oxford University Press, Oxford, 2008.
[13] C. P. Boyer, K. Galicki, and J. Kollár, Einstein metrics on spheres, Ann. of Math. (2), 162 (2005), pp. 557-580.
[14] R. L. Bryant, Bochner-Kähler metrics, J. Amer. Math. Soc., 14 (2001), pp. 623-715.
[15] J. Cheeger and A. Naber, Regularity of Einstein manifolds and the codimension 4 conjecture, Ann. of Math. (2), 182 (2015), pp. 1093-1165.
[16] X. X. Chen, C. LeBrun, and B. Weber, On conformally Kähler, Einstein manifolds, J. Amer. Math. Soc., 21 (2008), pp. 1137-1168.
[17] T. C. Collins and G. Székelyhidi, Sasaki-Einstein metrics and K-stability, Geom. Topol., 23 (2019), pp. 1339-1413.
[18] A. Derdziński, Self-dual Kähler manifolds and Einstein manifolds of dimension four, Compositio Math., 49 (1983), pp. 405-433.
[19] K. Galicki and H. B. Lawson, Jr., Quaternionic reduction and quaternionic orbifolds, Math. Ann., 282 (1988), pp. 1-21.
[20] P. Griffiths and J. Harris, Principles of Algebraic Geometry, Wiley-Interscience, New York, 1978.
[21] M. Gromov, Structures métriques pour les variétés riemanniennes, CEDIC, Paris, 1981. Edited by J. Lafontaine and P. Pansu.
[22] N. J. Hitchin, Compact four-dimensional Einstein manifolds, J. Differential Geometry, 9 (1974), pp. 435-441.
[23] Y. Huang and T. Ozuch, Regularity of Einstein 5-manifolds via 4dimensional gap theorems, e-print arXiv:2512.21317 [math.DG], 2025.
[24] J. Jost, Harmonic mappings between Riemannian manifolds, vol. 4 of Proceedings of the Centre for Mathematical Analysis, Australian National University, Australian National University, Centre for Mathematical Analysis, Canberra, 1984.
[25] J. Kollár, Einstein metrics on five-dimensional Seifert bundles, J. Geom. Anal., 15 (2005), pp. 445-476.
[26] J. Kollár and N. I. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math., 91 (1988), pp. 299-338.
[27] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom., 29 (1989), pp. 665-683.
[28] -, A Torelli-type theorem for gravitational instantons, J. Differential Geom., 29 (1989), pp. 685-697.
[29] C. LeBrun, Einstein metrics on complex surfaces, in Geometry and Physics (Aarhus, 1995), vol. 184 of Lecture Notes in Pure and Appl. Math., Dekker, New York, 1997, pp. 167-176.
[30] -, Einstein metrics, complex surfaces, and symplectic 4-manifolds, Math. Proc. Cambridge Philos. Soc., 147 (2009), pp. 1-8.
[31] -, On Einstein, Hermitian 4-manifolds, J. Differential Geom., 90 (2012), pp. 277-302.
[32] -, Einstein metrics, harmonic forms, and symplectic four-manifolds, Ann. Global Anal. Geom., 48 (2015), pp. 75-85.
[33] -, Mass, Kähler manifolds, and symplectic geometry, Ann. Global Anal. Geom., 56 (2019), pp. 97-112.
[34] -, Einstein manifolds, self-dual Weyl curvature, and conformally Kähler geometry, Math. Res. Lett., 28 (2021), pp. 127-144.
[35] A.-K. Liu, Some new applications of general wall crossing formula, Gompf's conjecture and its applications, Math. Res. Lett., 3 (1996), pp. 569-585.
[36] H. Nakajima, Hausdorff convergence of Einstein 4-manifolds, J. Fac. Sci. Univ. Tokyo Sect. IA Math., 35 (1988), pp. 411-424.
[37] -, Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem, in Recent topics in differential and analytic geometry, vol. 18 of Adv. Stud. Pure Math., Academic Press, Boston, MA, 1990, pp. 385-396.
\begin{itemize}
\item[] [38] Y. Odaka, C. Spotti, and S. Sun, Compact moduli spaces of del Pezzo surfaces and Kähler-Einstein metrics, J. Differential Geom., 102 (2016), pp. 127-172.
\item[] [39] H. Ohta and K. Ono, Notes on symplectic 4-manifolds with $b_{2}^{+}=1$. II, Internat. J. Math., 7 (1996), pp. 755-770.
\item[] [40] T. Ozuch, Completion of the Moduli Space of Einstein 4-Manifolds, PhD thesis, École Normale Supérieure (Paris), 2020.
\item[] [41] -, Higher order obstructions to the desingularization of Einstein metrics, Camb. J. Math., 9 (2021), pp. 901-976.
\item[] [42] -, Noncollapsed degeneration of Einstein 4-manifolds, I, Geom. Topol., 26 (2022), pp. 1483-1528.
\item[] [43] -, Noncollapsed degeneration of Einstein 4-manifolds, II, Geom. Topol., 26 (2022), pp. 1529-1634.
\item[] [44] I. Şuvaina, ALE Ricci-flat Kähler metrics and deformations of quotient surface singularities, Ann. Global Anal. Geom., 41 (2012), pp. 109-123.
\item[] [45] E. P. Wright, Quotients of gravitational instantons, Ann. Global Anal. Geom., 41 (2012), pp. 91-108.
\item[] [46] P. Wu, Einstein four-manifolds with self-dual Weyl curvature of nonnegative determinant, Int. Math. Res. Not. IMRN, (2021), pp. 1043-1054.
\end{itemize}
