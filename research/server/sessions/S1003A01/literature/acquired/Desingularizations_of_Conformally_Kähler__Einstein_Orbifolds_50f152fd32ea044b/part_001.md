---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Desingularizations of Conformally Kähler, Einstein Orbifolds]

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