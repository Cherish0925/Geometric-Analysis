# Hyperbolic four-manifolds with vanishing Seiberg-Witten invariants

- Category: papers
- Identity: arxiv:1812.06536
- Content status: fulltext_ok

---

---
source_file: 1812_06536v1.pdf
converter: mathpix
format: mmd
---

\title{
HYPERBOLIC FOUR-MANIFOLDS WITH VANISHING SEIBERG-WITTEN INVARIANTS
}

\author{
IAN AGOL AND FRANCESCO LIN
}

\begin{abstract}
We show the existence of hyperbolic 4-manifolds with vanishing Seiberg-Witten invariants, addressing a conjecture of Claude LeBrun. This is achieved by showing, using results in geometric and arithmetic group theory, that certain hyperbolic 4-manifolds contain $L$-spaces as hypersurfaces.
\end{abstract}

\section*{1. Introduction}

In [9, Conjecture 1.1], Claude LeBrun asked whether the Seiberg-Witten invariants of hyperbolic 4-manifolds vanish. This question stems from his result that for a hyperbolic 4-manifold, Seiberg-Witten basic classes satisfy much stronger constraints than one would expect; furthermore, it turns out to be related to several problems in low-dimensional topology [18, §4]. Here, we show that there exist certain hyperbolic 4-manifolds with vanishing Seiberg-Witten invariants.

Theorem 1.1. There exist closed arithmetic hyperbolic 4-manifolds with vanishing Seiberg-Witten invariants.

In the statement, we consider all possible Seiberg-Witten invariants coming from evaluating elements of the cohomology ring $\Lambda^{*} H^{1}(X ; \mathbb{Z}) \otimes \mathbb{Z}[U]$ of the space of configurations. Theorem 1.1 is proved by exhibiting hyperbolic 4-manifolds admitting separating $L$-spaces, using the main result of [6]; under mild additional conditions, this implies that such manifolds admit finite covers with vanishing Seiberg-Witten invariants. Our construction will show in fact that there are infinitely many commensurability classes of arithmetic hyperbolic 4-manifolds containing representatives with vanishing Seiberg-Witten invariants. Furthermore, by interbreeding as in [4], one can also obtain non-arithmetic examples.

Acknowledgements. The first author was funded by a Simons Investigator award. The second author was partially funded by NSF grant DMS-1807242. We thank Alan Reid for comments on an earlier draft.

\section*{2. A vanishing criterion for the Seiberg-Witten invariants}

We discuss a vanishing result for the Seiberg-Witten invariants of fourmanifolds containing a separating hypersurface. This is well-known to experts, but the exact form we will need is only implicitly stated in [7], so we will point it out for the reader's convenience. Most of our discussion is based on formal properties of the invariants, and we will follow closely follow the exposition of [7, Chapter 3].

Consider a spin ${ }^{c}$ structure $\mathfrak{s}_{X}$ on a closed oriented 4-manifold $X$. For a cohomology class $u \in \Lambda^{*} H^{1}(Y ; \mathbb{Z}) \otimes \mathbb{Z}[U]$, we define the Seiberg-Witten invariant $\mathfrak{m}\left(u \mid X, \mathfrak{s}_{X}\right)$ to be the evaluation of $u$ on the moduli space of solutions to the Seiberg-Witten equations. This is a topological invariant provided that $b_{2}^{+} \geq 2$. The latter is not a restrictive assumption in our case; hyperbolic 4 -manifolds have signature zero by [2, Theorem 3] and the Hirzebruch signature formula. Hence
$$\chi(X)=2\left(1-b_{1}(X)+b_{2}^{+}(X)\right) .$$
If $b_{2}^{+}(X) \leq 1$, we would have $\chi(X) \leq 4$; on the other hand, in all known examples of closed orientable hyperbolic 4-manifolds $\chi \geq 16$ [14, 11] (recall that by Gauss-Bonnet, volume and Euler characteristic are proportional).

We discuss a vanishing criterion for $\mathfrak{m}\left(u \mid X, \mathfrak{s}_{X}\right)$. Let $Y$ be a closed, oriented three-manifold. To this, in [7, Section 3.1] it is defined for each spin ${ }^{c}$ structure $\mathfrak{s}$ on $Y$ the monopole Floer homology groups fitting in the exact triangle of graded $\mathbb{Z}[U]$-modules
$$\cdots \longrightarrow \overline{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{i_{*}} \widetilde{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{j_{*}} \widehat{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{p_{*}} \overline{H M}_{*}(Y, \mathfrak{s}) \longrightarrow \cdots$$
where $U$ has degree -2 (notice that this convention differs from the one in the four-dimensional literature; this is because we identify $U$ with the corresponding capping operation in homology). The reduced Floer group $H M_{*}(Y, \mathfrak{s})$ is defined to be the image of $j_{*}$ in $\widehat{H M}_{*}(Y, \mathfrak{s})$ [7, Definition 3.6.3]. We will be particularly interested in the case in which $Y$ is a rational homology sphere. In this case we have an identification of $\mathbb{Z}[U]$-modules (up to grading shift) with Laurent series [7, Proposition 35.3.1]
$$\overline{H M}_{*}(Y, \mathfrak{s}) \cong \mathbb{Z}\left[U^{-1}, U\right] .$$

Definition 2.1 ([8]). We say that a rational homology sphere $Y$ is an $L$ space if, up to grading shift, $\widehat{H M}_{*}(Y, \mathfrak{s})=\mathbb{Z}[U]$ as $\mathbb{Z}[U]$-modules for all spin ${ }^{c}$ structures $\mathfrak{s}$.

As the map $p_{*}$ in equation (1) is an isomorphism in degrees low enough [7, Section 22.2], for an $L$-space $H M_{*}(Y, \mathfrak{s})=0$ for all $\operatorname{spin}^{c}$ structures $\mathfrak{s}$

Proposition 2.2. Let $X$ be a four-manifold given as $X=X_{1} \cup_{Y} X_{2}$. Suppose that the separating hypersurface $Y$ is an $L$-space (so that in particular $b_{1}(Y)=0$ ), and that $b_{2}^{+}\left(X_{i}\right) \geq 1$. Then all the Seiberg-Witten invariants of $X$ vanish.

Remark 2.3. A simpler to state vanishing criterion is the following: if $b_{1}(X)=0$ and $b_{2}^{+}(X)$ is even, then all Seiberg-Witten invariants are zero. In fact, under this assumption all Seiberg-Witten moduli spaces are odd dimensional [7, Theorem 1.4.4], while all classes in our cohomology ring are even dimensional. On the other hand, we are not aware of examples of hyperbolic 4-manifolds satisfying these conditions.

Proof of Proposition 2.2. All we need to do is to discuss the results of [7, Chapter 3] while keeping track of the specific spin ${ }^{c}$ structures. First of all, notice that as $b_{1}(Y)=0$, a spin ${ }^{c}$ structure $\mathfrak{s}_{X}$ on $X$ is determined by the restrictions $\mathfrak{s}_{i}=\left.\mathfrak{s}_{X}\right|_{X_{i}}$. This follows from the injectivity of the map $H^{2}(X ; \mathbb{Z}) \rightarrow H^{2}\left(X_{1} ; \mathbb{Z}\right) \oplus H^{2}\left(X_{2} ; \mathbb{Z}\right)$ in the Mayer-Vietoris sequence, and the fact the these groups classify spin ${ }^{c}$ structures. Let $\mathfrak{s}=\left.\mathfrak{s}_{X}\right|_{Y}$. It is sufficient to show that $\mathfrak{m}\left(u \mid X, \mathfrak{s}_{X}\right)=0$ for classes $u=u_{1} u_{2}$ where $u_{i}$ is a cohomology class in the configuration space of $X_{i}$. Recall from [7, Section 3.4] that a cobordism $W$ from $Y_{0}$ to $Y_{1}$ induces a map in homology fitting with the exact triangle; furthermore, if $b_{2}^{+}(W) \geq 1$, we have that $\overline{H M}_{*}(u \mid W, \mathfrak{s})=0$ [7, Proposition 3.5.2]. Given data as above, we can define the relative invariant $\psi_{\left(u_{1} \mid X_{1}, \mathfrak{s}_{1}\right)} \in \widehat{H M}_{*}(Y, \mathfrak{s})$ obtained as follows: let $W_{1}$ be the cobordism obtained from $X_{1}$ by removing a ball, and consider the induced map
$$\widehat{H M}_{*}\left(u_{1} \mid W_{1}, \mathfrak{s}_{1}\right): \widehat{H M}_{*}\left(S^{3}\right)=\mathbb{Z}[U] \rightarrow \widehat{H M}_{*}(Y, \mathfrak{s}) .$$
Then $\psi_{\left(u_{1} \mid X_{1}, \mathfrak{s}_{1}\right)}=\widehat{H M}_{*}\left(u_{1} \mid W_{1}, \mathfrak{s}_{1}\right)(1)$. On the other hand, we have the commutative diagram
$$\begin{aligned}
& \widehat{H M}_{*}\left(S^{3}\right) \xrightarrow{p_{*}} \overline{H M}_{*}\left(S^{3}\right) \\
& \widehat{H M}_{*}\left(u_{1} \mid W_{1}, \mathfrak{s}_{1}\right) \mid\left\lfloor\overline{H M}_{*}\left(u_{1} \mid W_{1}, \mathfrak{s}_{1}\right)\right. \\
& \widehat{H M}_{*}(Y, \mathfrak{s}) \xrightarrow{p_{*}} \overline{H M}_{*}(Y, \mathfrak{s})
\end{aligned}$$
and as $b_{2}^{+}\left(W_{1}\right) \geq 1$, the vertical map on the right vanishes; in turn, this implies that $\psi_{\left(u_{1} \mid X_{1}, \mathfrak{s}_{1}\right)} \in \operatorname{ker}\left(p_{*}\right)=H M_{*}(Y, \mathfrak{s})$. Similarly, using the map induced in cohomology by $W_{2}$, we obtain an element $\psi_{\left(u_{2} \mid X_{2}, \mathfrak{s}_{2}\right)} \in H M_{*}(-Y, \mathfrak{s})$; this last group is by Poincaré duality identified with $H M^{*}(Y, \mathfrak{s})$. The general gluing theorem in [7, Equation 3.22], when keeping track of the spin ${ }^{c}$ structures, is then
$$\mathfrak{m}\left(u \mid X, \mathfrak{s}_{X}\right)=\left\langle\psi_{\left(u_{1} \mid X_{1}, \mathfrak{s}_{1}\right)}, \psi_{\left(u_{2} \mid X_{2}, \mathfrak{s}_{2}\right)}\right\rangle,$$
where the angular brackets denote the natural pairing
$$H M_{*}(Y, \mathfrak{s}) \times H M^{*}(Y, \mathfrak{s}) \rightarrow \mathbb{Z} .$$
In our assumptions, the group $H M_{*}(Y, \mathfrak{s})$ vanishes, so this pairing is zero, and the result follows. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/472d0c62-9ff4-4925-8514-89f291379705-4.jpg?height=443&width=786&top_left_y=434&top_left_x=660}
\captionsetup{labelformat=empty}
\caption{Figure 1. A double cover of $X$ contains a separating $L$-space.}
\end{figure}

Remark 2.4. In fact, for our purposes of understanding gluing formula for Seiberg-Witten invariants, it suffices to consider the reduced invariants with rational coefficients $H M_{*}(Y, \mathfrak{s} ; \mathbb{Q})$. In particular, the previous discussion only relies on the vanishing of this group. Furthermore, via the universal coefficients theorem, this is implied by the vanishing of $H M_{*}(Y, \mathfrak{s} ; \mathbb{Z} / 2 \mathbb{Z})$, so that our main result actually applies for the reduced Floer homology group with $\mathbb{Z} / 2 \mathbb{Z}$-coefficients.

Our examples will be based on the following.
Corollary 2.5. Suppose $X$ is a 4 -manifold with $b_{2}^{+} \geq 1$ which admits an embedded non-separating $L$-space $Y$. Then $X$ admits infinitely many covers which have all vanishing Seiberg-Witten invariants.

Proof. Consider the double cover $\tilde{X}$ of $X$ formed by gluing together two copies $W_{1}$ and $W_{2}$ of the cobordism from $Y$ to $Y$ obtained by cutting $X$ along $Y$, see Figure 1. Consider a properly embedded path $\gamma \subset W_{1}$ between the two copies of $Y$, and denote by $T$ its tubular neighborhood. We then have the decomposition $X=\left(W_{1} \backslash T\right) \cup\left(W_{2} \backslash T\right)$, where the two manifolds are glued along a copy of $Y \# \bar{Y}$; here $\bar{Y}$ denotes $Y$ with the opposite orientation. The latter is an $L$-space [10, Section 4], and both $W_{1} \backslash T$ and $W_{2} \backslash T$ have $b_{2}^{+} \geq 1$, so we conclude. Of course, we can modify this construction to provide infinitely many examples. \(\square\)

\section*{3. Geodesic hypersurfaces in arithmetic hyperbolic 4-manifolds}

In this section, we will discuss various properties of arithmetic hyperbolic lattices. For the general case of arithmetic lattices, see [20], and for the 3-dimensional case, consult [13]. We first review the definitions and construction of arithmetic manifolds of simplest type.

Definition 3.1. Let $G$ be a group, $H_{1}, H_{2} \leq G$ be subgroups. We say that $H_{1}$ is commensurable in $G$ with $H_{2}$ if $\left[H_{1}: H_{1} \cap H_{2}\right]<\infty,\left[H_{2}: H_{1} \cap H_{2}\right]<$ $\infty$.

Definition 3.2. Consider a non-degenerate quadratic form $q: k^{n+1} \rightarrow k$ for a totally real number field $k \subset \mathbb{R}$ with ring of integers $\mathcal{O}_{k}$. Assume that $q$ is Lorentzian, i.e. has signature $(n, 1)$ over $\mathbb{R}$. Moreover, for each non-trivial embedding $\sigma: k \rightarrow \mathbb{R}$, assume that $\sigma \circ q$ is positive definite. Let $O(q ; k)$ denote the group of matrices preserving $k$, i.e. linear transforms $A: k^{n+1} \rightarrow$ $k^{n+1}$ such that $q \circ A=q$. Then the subgroup $O\left(q ; \mathcal{O}_{k}\right) \subset O(q ; k) \subset O(q ; \mathbb{R})$ is a lattice, and acts discretely on the hyperboloid of two sheets $\mathcal{H}=\{x \in$ $\left.\mathbb{R}^{n+1} \mid q(x)=-1\right\}$. Up to isometry, the group $O(q ; \mathbb{R}) \cong O(n, 1 ; \mathbb{R})$, the orthogonal group associated to the quadratic form $-x_{0}^{2}+x_{1}^{2}+\cdots+x_{n}^{2}$. Projectivizing, $P O\left(q ; \mathcal{O}_{k}\right)$ acts discretely on hyperbolic space $\mathbb{H}^{n}$, which is the quotient of the hyperboloid $\mathcal{H}$ by the antipodal map. A hyperbolic orbifold $\mathbb{H}^{n} / \Gamma$ is said to be of simplest type if $\Gamma$ is commensurable (up to conjugacy) with $P O\left(q ; \mathcal{O}_{k}\right)$ for some such $q$.

Example: Let $q_{n}: k^{n+1} \rightarrow k$ be defined by $q_{n}\left(x_{0}, x_{1}, \ldots, x_{n}\right)=-\sqrt{2} x_{0}^{2}+$ $x_{1}^{2}+\cdots+x_{n}^{2}$ over the field $k=\mathbb{Q}(\sqrt{2})$. Let $\sigma: k \rightarrow k$ be the Galois automorphism induced by $\sigma(\sqrt{2})=-\sqrt{2}$. Then $\sigma \circ q_{n}\left(x_{0}, \ldots, x_{n}\right)=\sqrt{2} x_{0}^{2}+$ $x_{1}^{2}+\cdots+x_{n}^{2}$ is positive definite. Hence $P O\left(q_{n} ; \mathbb{Z}[\sqrt{2}]\right)$ is a discrete arithmetic lattice acting on $\mathbb{H}^{n}$. See [20, §6.4].

Definition 3.3. Let $G$ be a group. Then $G^{(2)}=\left\langle g^{2} \mid g \in G\right\rangle$.
If $G$ is finitely generated, then $G^{(2)}$ is finite-index in $G$, and $G / G^{(2)}$ is an elementary abelian 2-group.

Theorem 3.4. Let $M^{3}$ be an orientable hyperbolic arithmetic 3-manifold of simplest type with $H_{1}(M ; \mathbb{Z} / 2)=0$ and not defined over $\mathbb{Q}$. Then $M$ embeds as a totally geodesic non-separating submanifold in a compact arithmetic hyperbolic 4-manifold.

Proof. Let $\Gamma=\pi_{1}(M) \leq \operatorname{Isom}^{+}\left(\mathbb{H}^{3}\right)$. Since $M$ is a $\mathbb{Z} / 2 \mathbb{Z}$-homology sphere, $\Gamma^{(2)}=\Gamma$. By [6, Theorem 1.1 (2)], $\mathbb{H}^{n} / \Gamma^{(2)} \cong M$ embeds as a totally geodesic submanifold of a closed orientable hyperbolic 4-manifold $W$ (the fact that $M$ is not defined over $\mathbb{Q}$ implies that $W$ is compact). Briefly, this is proved by showing that $\Gamma^{(2)} \leq P O(q ; k)$ so that it is commensurable with $P O\left(q ; \mathcal{O}_{k}\right)$ for some Lorentzian quadratic form $q: k^{4} \rightarrow k$. Taking the quadratic form $Q_{d}=d y^{2}+q, d \in \mathbb{N}$, we get an embedding of $P O\left(q ; \mathcal{O}_{k}\right)<P O\left(Q_{d} ; \mathcal{O}_{k}\right)<$ $P O\left(Q_{d} ; \mathbb{R}\right) \cong P O(4,1 ; \mathbb{R})$. Then a subgroup separability result allows one to embed $\Gamma$ in a torsion-free lattice $\Lambda<P O\left(Q_{d} ; k\right)$ so that $W=\mathbb{H}^{4} / \Lambda$. By [1, Theorem 2], there exists a further finite-sheeted cover $\tilde{W} \rightarrow W$, and a lift $M \rightarrow \tilde{W}$ such that the lift of $M$ is non-separating in $\tilde{W}$. This is achieved again by a subgroup separability result. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/472d0c62-9ff4-4925-8514-89f291379705-6.jpg?height=634&width=778&top_left_y=445&top_left_x=640}
\captionsetup{labelformat=empty}
\caption{Figure 2. In this picture, the numbers indicate the branching. The top picture has an obvious order 2 rotational symmetry along the axis depicted by the big dot. The quotient is the link in $S^{3}$ depicted on the bottom left. This is isotopic to the link on the right (which is topologically the same, but with different branchings). Now, the curve with branching 2 is the 3-braid $\sigma_{1} \sigma_{2}^{-1}$, so that taking the $n$-fold branched cover along the other component we see that $M_{n}$ is the branched double cover over $\left(\sigma_{1} \sigma_{2}^{-1}\right)^{n}$.}
\end{figure}

\section*{4. Examples}

The Fibonacci manifold $M_{n}$ is the cyclic branched $n$-fold cover over the figure-eight knot. For $n=2$ we obtain a lens space, for $n=3$ the Hantzche-Wendt manifold, while for $n \geq 4$ it is hyperbolic.

For every $n$ the Fibonacci manifold $M_{n}$ is an $L$-space. To see this, recall from [19] that $M_{n}$ is the branched double cover over the closure of the 3braid $\left(\sigma_{1} \sigma_{2}^{-1}\right)^{n}$ (see Figure 2), which is alternating. Using the surgery exact triangle [8], these can be shown to be $L$-spaces as in the context of Heegaard Floer homology [15], with the caveat that in our setting the computation only holds with coefficients in $\mathbb{Z} / 2 \mathbb{Z}$; on the other hand this is enough for our purposes, see Remark 2.4. Notice also that for $n \neq 0$ modulo 3, the closure is a knot, so that $M_{n}$ is a $\mathbb{Z} / 2 \mathbb{Z}$-homology sphere.

By [5], $M_{n}$ is arithmetic when $n=4,5,6,8,12$. Of these examples, $n=$ 4, 5, 8 are $\mathbb{Z} / 2 \mathbb{Z}$ homology spheres. The only one of these three which is simplest type and not defined over $\mathbb{Q}$ is $M_{5}$. This is example [13, 13.7.4(a)(iii)], which has invariant trace field a quartic field. As they point out, this is commensurable with a tetrahedral group [13, 13.7.4(a)(i)] which is simplest type
and not defined over $\mathbb{Q}$ by [12, Theorem 1]. It is defined over a quadratic form over the field $\mathbb{Q}(\sqrt{5})$.

Thus, by Theorem 3.4, $M_{5}$ has a non-separating embedding into a closed orientable hyperbolic 4-manifold $W$. We may assume that $\chi(W)>2$ (by passing to a 2-fold cover if needed), and hence $b_{2}^{+}(W)>1$. Thus by Corollary 2.5, these embed into a hyperbolic 4-manifold with vanishing Seiberg-Witten invariants. This completes the proof of Theorem 1.1.

Remark 4.1. One may also get other examples by cutting and doubling or using the interbreeding technique of Gromov-Piatetskii-Shapiro to get non-arithmetic examples. One can isometrically embed this $L$-space $M_{5}$ in infinitely many incommensurable hyperbolic 4-manifolds via the method of [6] by taking the forms $Q_{1}$ and $Q_{d}$ in the proof of Theorem 3.4 so that $d$ is square-free in $k=\mathbb{Q}(\sqrt{5})$, and then cut and cross-glue to give a closed non-arithmetic manifold containing $M_{n}$ as a non-separating hypersurface [4, §2.9].

\section*{5. Conclusion}

We conclude by pointing out some natural questions related to our method.
\begin{itemize}
\item[(1)] Can one find an explicit hyperbolic example (such as the Davis manifold or the manifolds described in [11]) that satisfies the properties of Proposition 2.2? Recall that the Davis manifold has $b_{1}=24$ and $b_{2}^{+}=36$ [16], so that all moduli spaces have odd dimension.
\item[(2)] Can one embed any orientable hyperbolic 3-manifold of simple type as a geodesic hypersurface in an orientable hyperbolic 4-manifold? More generally, can one show that orientable hyperbolic 3-manifolds have quasiconvex embeddings into orientable hyperbolic 4-manifolds?
\item[(3)] Can one use bordered Floer theory to compute the Seiberg-Witten invariants of Haken hyperbolic 4-manifolds (in the sense of [3])?
\item[(4)] Which commensurability classes of compact hyperbolic 3-manifold of the simplest type contain $L$-spaces? Note that it is not even known if there are infinitely many commensurability classes of arithmetic rational homology 3-spheres.
\end{itemize}

\section*{References}
\begin{itemize}
\item[] [1] Nicolas Bergeron, Premier nombre de Betti et spectre du laplacien de certaines variétés hyperboliques, Enseign. Math. (2) 46 (2000), no. 1-2, 109-137.
\item[] [2] Chern, Shiing-Shen, On curvature and characteristic classes of a Riemann manifold, Abh. Math. Sem. Univ. Hamburg 20 (1955), 117-126.
\item[] [3] Bell Foozwell and Hyam Rubinstein, Introduction to the theory of Haken $n$-manifolds, Topology and geometry in dimension three, Contemp. Math., vol. 560, Amer. Math. Soc., Providence, RI, 2011, pp. 71-84.
\item[] [4] Gromov, M. and Piatetski-Shapiro, I. Nonarithmetic groups in Lobachevsky spaces. Inst. des Hautes Études Sci. Publ. Math. No. 66 (1988), 93-103.
\end{itemize}
\begin{itemize}
\item[] [5] Hugh M. Hilden, María Teresa Lozano, and José María Montesinos-Amilibia, The arithmeticity of the figure eight knot orbifolds, Topology '90 (Columbus, OH, 1990) 169-183.
\item[] [6] Alexander Kolpakov, Alan W. Reid, and Leone Slavich, Embedding arithmetic hyperbolic manifolds, Mathematical Research Letters 25 (2018), no. 4, 1305-1328, arXiv:1703.10561.
\item[] [7] Kronheimer, Peter and Mrowka, Tomasz, Monopoles and three-manifolds, New Mathematical Monographs, 10. Cambridge University Press, Cambridge, 2007. xii+796 pp
\item[] [8] Kronheimer, P. and Mrowka, T. and Ozsváth, P. and Szabó, Z., Monopoles and lens space surgeries, Ann. of Math. (2) 165 (2007), no. 2, 457-546.
\item[] [9] Claude LeBrun, Hyperbolic manifolds, harmonic forms, and Seiberg-Witten invariants, Proceedings of the Euroconference on Partial Differential Equations and their Applications to Geometry and Physics (Castelvecchio Pascoli, 2000), vol. 91, 2002, pp. 137-154.
\item[] [10] Lin, Francesco, Pin(2)-monopole Floer homology, higher compositions and connected sums, J. Topol. 10 (2017), no. 4, 921-969.
\item[] [11] C. Long, Small volume closed hyperbolic 4-manifolds, Bull. Lond. Math. Soc. 40 (2008), no. 5, 913-916.
\item[] [12] C. Maclachlan and A. W. Reid, The arithmetic structure of tetrahedral groups of hyperbolic isometries, Mathematika 36 (1989), no. 2, 221-240 (1990).
\item[] [13] Colin Maclachlan and Alan W. Reid, The arithmetic of hyperbolic 3-manifolds, Graduate Texts in Mathematics, vol. 219, Springer-Verlag, New York, 2003.
\item[] [14] Marston Conder and Colin Maclachlan, Compact hyperbolic 4-manifolds of small volume, Proc. Amer. Math. Soc. 133 (2005), no. 8, 2469-2476.
\item[] [15] Ozsváth, Peter and Szabó, Zoltán, On the Heegaard Floer homology of branched double-covers, Adv. Math. 194 (2005), no. 1, 1-33.
\item[] [16] Ratcliffe, John G. and Tschantz, Steven T., On the Davis hyperbolic 4-manifold, Topology Appl. 111 (2001), no. 3, 327-342.
\item[] [17] Alan W. Reid, Arithmetic kleinian graups and their fuchsian subgroups, Ph.D. thesis, Aberdeen, 1987.
\item[] [18] Alan W. Reid, Surface subgroups of mapping class groups, Problems on mapping class groups and related topics, 257-268, Proc. Sympos. Pure Math., 74, Amer. Math. Soc., Providence, RI, 2006.
\item[] [19] Vesnin, A. Yu. and Mednykh, A. D.,Fibonacci manifolds as two-sheeted coverings over a three-dimensional sphere, and the Meyerhoff-Neumann conjecture, Siberian Math. J. 37 (1996), no. 3, 461-467
\item[] [20] Dave Witte Morris, Introduction to arithmetic groups, Deductive Press, http://deductivepress.ca/, 2015.
\end{itemize}

University of California, Berkeley, 970 Evans Hall \#3840, Berkeley, CA 94720-3840
E-mail address: ianagol@math.berkeley.edu
Princeton University, Department of Mathematics, Fine Hall, Washington Road, Princeton NJ 08544-1000
E-mail address: f14@math.princeton.edu
