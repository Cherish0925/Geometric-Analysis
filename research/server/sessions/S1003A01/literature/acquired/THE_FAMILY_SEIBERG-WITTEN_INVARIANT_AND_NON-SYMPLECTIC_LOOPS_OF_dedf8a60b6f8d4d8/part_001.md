---
retention_scope: session
part: 1
total_parts: 5
---

[Part 1/5 of: THE FAMILY SEIBERG-WITTEN INVARIANT AND NON-SYMPLECTIC LOOPS OF DIFFEOMORPHISMS]

---
source_file: 2208_12082.pdf
converter: mathpix
format: mmd
---

\title{
THE FAMILY SEIBERG-WITTEN INVARIANT AND NON-SYMPLECTIC LOOPS OF DIFFEOMORPHISMS
}

\author{
JIANFENG LIN
}

\begin{abstract}
By extending a result of Kronheimer-Mrowka to the family setting, we prove a gluing formula for the family Seiberg-Witten invariant. This formula allows one to compute the invariant for a smooth family of 4-manifolds by cutting it open along a product family of 3-manifolds and studying the induced maps on monopole Floer (co)homology. When the cutting 3-manifold is an L-space, this formula implies a relation between the family Seiberg-Witten invariant, the Seiberg-Witten invariant of the fiber and the index of the family Dirac operator. We use this relation to calculate the Seiberg-Witten invariant of families of 4-manifolds that arise when resolving an ADE singularity using a hyperkähler family of complex structures near the singularity. Several applications are obtained. First, we establish a large family of simply-connected 4-manifolds $M$ (e.g. all elliptic surfaces) such that $\pi_{1}(\operatorname{Diff}(M))$ has a $\mathbb{Z}^{\infty}$-summand . For such $M$, the product $S^{2} \times M$ smoothly fibers over $S^{2}$ with fiber $M$ in infinitely many distinct ways. Second, we show that on any closed symplectic 4-manifold that contains a smoothly embedded sphere of self-intersection -1 or -2, there is a loop of diffeomorphisms that is not homotopic to a loop of symplectormorphisms. This generalizes a previous result by Smirnov and confirms a conjecture by McDuff in dimension 4. It also provides many new examples of 4-manifolds whose space of symplectic forms has a nontrivial fundamental group or first homology group.
\end{abstract}

\section*{1. Introduction}

The Seiberg-Witten invariant is a powerful tool in understanding smooth structures on 4-manifolds. Its family version, as proposed by Donaldson [9] and later pursued by many authors including Ruberman [39, 41], Liu [26], Li-Liu [23], Nakamura [34] and Baraglia-Konno [5], has been used to prove many essential results on smooth families of 4-manifolds [3, 23, 26, 39, 41]). As most gauge theoretic invariants, it is difficult to directly compute this invariant by solving the Seiberg-Witten equations. Hence it is natural to develop a gluing formula that allows one to compute this invariant via a cut-and-paste technique. For classical Seiberg-Witten invariants, such formula has been extensively studied [35, 32, 48, 11]. In particular, using monopole Floer homology, Kronheimer-Mrowka [19] proved a gluing formula for decompositions along a general 3-manifold. For the family Seiberg-Witten invariant, Baraglia-Konno [5] proved a gluing formula for connected sums, generalizing an earlier result by Ruberman [41]. These gluing formulas are powerful in computing the (family) Seiberg-Witten invariants and they have numerous applications.

The purpose of this paper is to extend Kronheimer-Mrowka's gluing formula to the family setting and to obtain new topological applications. This version of gluing formula allows a general cutting 3-manifold and we apply it in the computation of the Seiberg-Witten
invariants of two smooth families that naturally raise from resolution of singularities: the ADE family and the blown-up family. As applications, we obtain new results about the topology of the diffeomorphism groups, the symplectormorphism groups, and the space of symplectic forms.

It takes some works to give statements of the gluing theorems (Theorem L and Theorem M). For readers' convinience, we discuss the topological applications first.
1.1. 4-manifolds with infinite type diffeomorphism groups. The first application concerns the diffeomorphism group of a 4-manifold. There has been active researches on the topology of this topological group in recent years [5, 39, 40, 17, 49, 2, 7]. For example, Ruberman discovered examples of $M$ such that $\operatorname{ker}\left(\pi_{0}(\operatorname{Diff}(M)) \rightarrow \pi_{0}(\operatorname{Homeo}(M))\right)$ is nontrivial [39]. (And he later found a further example for which the kernel contains a $\mathbb{Z}^{\infty}$-summand [40]). Budney-Gabai [7] proved that $\pi_{0}\left(\operatorname{Diff}\left(S^{1} \times D^{3}, \partial\right)\right)$ (i.e., the mapping class group of $S^{1} \times D^{3}$ relative to the boundary) is not finitely generated. Regarding higher homotopy groups, Watanabe proved that $\pi_{i}\left(\operatorname{Diff}\left(D^{4}, \partial\right)\right) \otimes \mathbb{Q} \neq 0$ for $i=1,4,8 \cdots$. For any $i \geqslant 1$, and Auckly-Ruberman [1] found many other examples of closed 4-manifolds so that $\pi_{i}(\operatorname{Diff}(M)) \rightarrow \pi_{i}(\operatorname{Homeo}(M))$ is not injective. Regarding the important example of a $K 3$ surface, Baraglia-Konno [6] proved that $\pi_{1}(\operatorname{Diff}(K 3)) \rightarrow \pi_{1}(\operatorname{Homeo}(K 3))$ is not surjective. And Baraglia [4] proved that $\pi_{1}(\operatorname{Diff}(K 3))$ has a $\mathbb{Z}^{\infty}$ summand. In the current paper, we establish a large family of 4-manifolds whose diffeomorphism group has a $\mathbb{Z}^{\infty}$ summand, showing that this phenomena is very common in dimension 4.

Our construction makes use of the generalized Dehn twist along a smoothly embedded sphere of self-intersection -1 or -2 (i.e. a -1-spheres or a -2-sphere). Let $S$ be such a sphere and let $\nu(S)$ be its closed tubular neighborhood. Then $\nu(S)$ is diffeomorphic to the disk bundle for a complex line bundle over $S$. Let $\gamma: S^{1} \rightarrow \operatorname{Diff}(\nu(S))$ be the circle action given by fiberwise complex multiplication. When $S \cdot S=-1$, the restriction of $\gamma$ on $\partial \nu(S)=S^{3}$ admits a factorization
$$S^{1} \hookrightarrow S U(2) \rightarrow \operatorname{Diff}(\partial \nu(S))$$
Thus we can use a null-homotopy of $S^{1}$ in $S U(2)$ to modify $\gamma$ near $\partial \nu(S)$ and get a loop $\gamma^{\prime}: S^{1} \rightarrow \operatorname{Diff}(\nu(S), \partial)$. Then we extend by the identity map on $M \backslash \nu(S)$ and get a loop $\gamma_{S}: S^{1} \rightarrow \operatorname{Diff}(M)$ supported near $S$. The case $S \cdot S=-2$ is similar. We have $\partial \nu(S)=\mathbb{R P}^{3}$ and the restriction of the circle action $\gamma$ on $\partial \nu(S)$ is contained in a larger group action by $S O(3)$. This allows us to modify $\gamma^{2}$ near $\partial \nu(S)$ and get a loop $\gamma^{\prime}: S^{1} \rightarrow \operatorname{Diff}(\nu(S), \partial)$. Then we extend by the identity map on $M \backslash \nu(S)$ and get the loop $\gamma_{S}: S^{1} \rightarrow \operatorname{Diff}(M)$. Unlike the ordinary Dehn twist, which is a single diffeomorphism, $\gamma_{S}$ is a loop of diffeomorphisms. Let's call $\gamma_{S}$ the generalized Dehn twists along $S$.

Theorem A. Let $M$ be a smooth closed oriented 4-manifold that contains an infinite collection of smoothly embedded -2-spheres $\left\{S_{i}\right\}_{i \in \mathbb{N}}$, all representing different homology classes. Suppose $b_{1}(M)=0$ and assume either one of the following conditions hold:
\begin{itemize}
\item[(1)] $b_{2}^{+}(M)>1$ and $\operatorname{SW}(M, \mathfrak{s}) \neq 0$ for some $\operatorname{spin}^{c}$-structure $\mathfrak{s}$ with $d(\mathfrak{s}, M)=0$. Here
$$d(\mathfrak{s}, M)=\frac{c_{1}^{2}(\mathfrak{s})-3 \sigma(M)-2 \chi(M)}{4}$$
\end{itemize}
\begin{itemize}
\item[] denotes the expected dimension of the Seiberg-Witten moduli space. Or
\item[(2)] $b_{2}^{+}(M)=1$ and there exists a $\operatorname{spin}^{c}$ structure $\mathfrak{s}$ such that $d(\mathfrak{s}, M)=0$ and that $\left\langle c_{1}(\mathfrak{s}),\left[S_{i}\right]\right\rangle=0$ for any $i$. (We don't impose any constraint on the Seiberg-Witten invariant.)
\end{itemize}
Then $\pi_{1}(\operatorname{Diff}(M))$ contains a $\mathbb{Z}^{\infty}$ summand, generated by generalized Dehn twists along a subcollection $\left\{S_{n_{i}}\right\}_{i \in \mathbb{N}}$.

Recall that a space is of finite type if it is weakly homotopy equivalent to a $C W$-complex with finitely many cells in each dimension. Since the fundamental group of a finite type space is always finitely generated, Theorem A implies the following corollary.
Corollary B. Let $M$ be a manifold that satisfies the conditions of Theorem A. Then $\operatorname{Diff}_{0}(X)$ (the unit component of $\operatorname{Diff}(X)$ ) is not of finite type.

Remark 1. It is interesting to compare Baraglia's result and Theorem A with a recent result by Bustmante-Krannich-Kupers [8], which states that the $\pi_{i}(\operatorname{Diff}(M))$ is finitely generated for any $i \geqslant 1$ when $M$ is smooth manifold of dimension $2 n \geqslant 6$ with a finite fundamental group. In an earlier paper [20], Kupers proved the same result for any dimension $\neq 4,5,7$, under the additional assumption that $M$ is 2-connected. As mentioned in [8], it is expected that this 2-connectedness condition can also be removed in odd dimensions $\geqslant 7$. Therefore, Baraglia's result and Theorem Areflect some very special phenomena in dimension 4 which doesn't happen in higher dimensions.

Remark 2. It's natural to ask whether this $\mathbb{Z}^{\infty}$ summand constructed in Theorem A contains some exotic loops of diffeomorphisms (i.e. nonzero elements in $\operatorname{ker}\left(\pi_{1}(\operatorname{Diff}(M)) \rightarrow\right.$ $\left.\left.\pi_{1}(\operatorname{Homeo}(M))\right)\right)$. For those generators (i.e. generalized Dehn twists), one can show that they are nontrivial in $\pi_{1}(\operatorname{Homeo}(M))$ by showing the total space of the corresponding fiber bundle over $S^{2}$ has a different cohomology ring as $S^{2} \times M$. (See Remark 10, This argument was pointed out to the author by Kronheimer). However, the argument breaks down when one tries to show these generators are linearly independent in $\pi_{1}(\operatorname{Homeo}(M))$. Actually we will prove in Corollary D that some linear combinations are indeed contratible in the space of auotomorphisms on $M$. So it's unclear whether this $\mathbb{Z}^{\infty}$ summand contains some exotic elements. We leave this as a curious open question.

There are many ways to construct interesting examples that satisfy the conditions of Theorem A. We give some of them in the following corollary.

Corollary C. Let $M$ be a smooth 4-manifold that belongs to the following list. Then $M$ satisfies the conditions of Theorem $A$ and hence $\pi_{1}(\operatorname{Diff}(M))$ has a $\mathbb{Z}^{\infty}$-summand.
\begin{itemize}
\item[(1)] $M$ is an elliptic surface with $b_{1}(M)=0$.
\item[(2)] $M$ is a hypersurface or a complete intersection in $\mathbb{C P}^{n}$ with $b_{2}^{+}(M)>1$.
\item[(3)] $M$ is a fiber sum $M^{\prime} \#_{T^{2}} E$. Here $E$ is an elliptic surface with $b_{1}(E)=0$ and $M^{\prime}$ is a simply-connected 4-manifold with $b^{+}(M)>1$ and $\mathrm{SW}\left(M^{\prime}, \mathfrak{s}\right) \neq 0$ for some $\mathfrak{s}$ with $d(\mathfrak{s}, M)=0$. The fiber sum is applied along a regular fiber of $E$ and a smoothly embedded torus $F \subset M^{\prime}$ with self-intersection 0 and $[F] \neq 0 \in H_{2}\left(M^{\prime} ; \mathbb{Z}\right)$.
\item[(4)] $M$ is a smooth 4-manifold with $b_{1}(M)=0, b_{2}^{+}(M)>1$ and $\operatorname{SW}(M, \mathfrak{s}) \neq 0$ for some $\mathfrak{s}$ with $d(\mathfrak{s}, M)=0$. And $M$ contains two smoothly embedded spheres $S_{0}, S_{1}$
\end{itemize}
\begin{itemize}
\item[] that satisfy
$$S_{0} \cdot S_{0}=-2, \quad S_{1} \cdot S_{1}=-2, \quad\left|S_{0} \cdot S_{1}\right| \geqslant 3 .$$
\item[(5)] $M$ is a blow up of one of the above manifolds.
\end{itemize}

By the finiteness theorem proved in [20], one can further deduce the following corollary.
Corollary D. Let $M$ be a simply-connected 4-manifold that satisfies the conditions of Theorem A. Then the following conclusions hold.
\begin{itemize}
\item[(1)] Let haut ${ }^{\mathrm{id}}(M)$ be the space of continuous maps $f: M \rightarrow M$ which are homotopic to the identity. Consider the map
$$\pi_{1}(\operatorname{Diff}(M)) \rightarrow \pi_{1}\left(\text { haut }^{\mathrm{id}}(M)\right)$$
induced by the inclusion. Then the kernel of this map contains a $\mathbb{Z}^{\infty}$ subgroup.
\item[(2)] Let $\widetilde{\operatorname{Diff}}(M)$ be the simplicial group of block diffeomorphisms on $M$. Consider the map
$$\pi_{1}(\operatorname{Diff}(M)) \rightarrow \pi_{1}(\widetilde{\operatorname{Diff}}(M))$$
induced by the inclusion. Then the kernel of this map contains a $\mathbb{Z}^{\infty}$ subgroup. Concretely, that means any element in this subgroup can be represented by a loop $\gamma: S^{1} \rightarrow \operatorname{Diff}(M)$ such that the map
$$\widetilde{\gamma}: S^{1} \times M \rightarrow S^{1} \times M \text { defined by }(t, x) \mapsto(t, \gamma(t) \cdot x)$$
can be extended to a diffeomorphism $\hat{\gamma}$ on $D^{2} \times M$.
\item[(3)] $S^{2} \times M$ fibers over $S^{2}$ in infinitely many distinct ways. I.e., there exist infinitely many nonisomorphic smooth fiber bundles whose fibers, bases and total spaces are diffeomorphic to $M, S^{2}$ and $S^{2} \times M$ respectively.
\end{itemize}
1.2. Nonsymplectic loops of diffeomorphisms. The next application concerns the topology of of the symplectormorphism group. This has also been a classical question in symplectic geometry. In a general dimension, the technique of pseudo-holomorphic curves is powerful. In dimension four, because of Taubes's fundamental result " $\mathrm{SW}=\mathrm{Gr}$ " [45, 47], the Seiberg-Witten theory provides extra tools to study this problem. Given a closed symplectic 4-manifold $(M, \omega)$, we let $\operatorname{Symp}(M, \omega)$ be the sympltectormorphism group. We have a natural inclusion map
$$i: \operatorname{Symp}(M, \omega) \rightarrow \operatorname{Diff}(M,[\omega]) .$$
Here $\operatorname{Diff}(M,[\omega])$ denotes the group diffeomorphisms that preserves the symplectic class $[\omega] \in H_{2}(M ; \mathbb{R})$. One may ask the following question:
Question 1.1. Given $(M, \omega)$, is the map (1) a homotopy equivalence?
By Moser's theorem [33], the analogous question in dimension two always has an affirmative answer. But in higher dimensions, it is expected that $\operatorname{Symp}(M, \omega)$ is significantly "smaller" than $\operatorname{Diff}(M,[\omega])$ and the answer to Question 1.1) should usually (if not always) be negative. See [30, Chapter 10] for relevant discussions. In dimension four, for some small rational or ruled surface (e.g., $\mathbb{C P}^{2}, \mathbb{C P}^{2} \# \overline{\mathbb{C P}^{2}}$ and $S^{2} \times S^{2}$ ), the topology of $\operatorname{Symp}(M, \omega)$ is well-understood and a negative answer to Question 1.1 is known. For a
general $M$, finding the homotopy type of $\operatorname{Symp}(M, \omega)$ seems out of reach. But one can still approach Question 1.1 by studying the induced map on homotopy groups. For any $n \geqslant 0$, we pick the identity element as the base point and let
$$i_{n, *}: \pi_{n}(\operatorname{Symp}(M, \omega)) \rightarrow \pi_{n}(\operatorname{Diff}(M,[\omega]))$$
be the map induced by $i$. Note that when $n \geqslant 1$, we have $\pi_{n}(\operatorname{Diff}(M,[\omega]))=\pi_{n}(\operatorname{Diff}(X))$ because $\operatorname{Diff}(M,[\omega])$ contains the unit component of $\operatorname{Diff}(M)$.

Among $\pi_{n}(\operatorname{Symp}(M, \omega))$ for various $n$, the most interesting ones are $\pi_{0}(\operatorname{Symp}(M, \omega))$ and $\pi_{1}(\operatorname{Symp}(M, \omega))$. The former is the so-called symplectic mapping class group, and the later is related to Hofer's geometry [37] and quantum cohomology [42]. So one may start by asking about the surjetivity/injectivity of $i_{n, *}$ when $n=0,1$. It's an open question whether $i_{0, *}$ is always surjective. For the injectivity of $i_{0, *}$, Seidel proved a remarkable result in his thesis [42]. Let $L$ be an embedded Lagrangian sphere in $M$ and let $\lambda_{L}$ be a Dehn-Seidel twist along $L$ (see [43]). Under mild assumptions on the homology of $M$, Seidel proved that $\Lambda_{L}^{2}$, which is smoothly isotopic to the identity, is not symplectically isotopic to the identity. This gives a large family of examples where $i_{0, *}$ is not injective. There has been many subsequent works that prove various generalization and variation of Seidel's result. In particular, Kronheimer [18] established nontrivial higher dimensional families of sympltectic forms, using the family Seiberg-Witten invariants. By a refinement of Kronheimer's argument, Smirnov [44] established a large family of Kähler surfaces for which the map $i_{1, *}$ is not surjective. In other words, on such $M$, there exists a loop of diffeomorphisms that is not smoothly isotopic to any loop of symplectormorphisms. (Previously such phenomena was only known for rational or ruled surfaces.) Both Kronheimer and Smirnov's proofs rely on computations of the family Seiberg-Witten invariants via algebraic geometric methods (counting rational holmorphic curves in a Kähler family). Using the gluing theorem (Theorem L), we can compute this invariant for many smooth families. And we show that any nontrivial linear combinations of generalized Dehn twists along homological distinct spheres are non-symplectic.

To give the precise statement, we let $K$ be the canonical class of a symplectic 4-manifold $(M, \omega)$ and we consider the following sets
$$R_{M}^{1}:=\left\{\alpha \in H_{2}(M ; \mathbb{Z}) \mid \alpha \cdot \alpha=-1,\langle K, \alpha\rangle=-1,\right.$$
$\alpha$ is represented by a smoothly embedded sphere\}
$$R_{M}^{2}:=\left\{\alpha \in H_{2}(M ; \mathbb{Z}) \mid \alpha \cdot \alpha=-2,\langle K, \alpha\rangle=0,\right.$$
$\alpha$ is represented by a smoothly embedded sphere $\} / \pm 1$
$$R_{M}:=R_{M}^{1} \cup R_{M}^{2}$$

Theorem E. Let $(M, \omega)$ be a closed symplectic 4-manifold. We pick an embedded sphere $S_{\alpha}$ for each $\alpha \in R_{M}$. Then the generalized Dehn twists $\left\{\gamma_{S_{\alpha}}\right\}$ generate a free abelian subgroup
$$\mathbb{Z}^{R_{M}} \subset \pi_{1}(\operatorname{Diff}(\mathrm{M})),$$
which intersects trivially with the image of $i_{1, *}$.

Corollary F. Let $(M, \omega)$ be a closed symplectic 4-manifold that contains a smoothly embedded sphere $S$ of self-intersection -1 or -2 . Then the map $i_{1, *}$ is not surjective. Therefore, the map $i$ is not a homotopy equivalence.

Remark 3. McDuff made a conjecture about the symplectomorphism group of a blow up in all even dimensions (see [29], second paragraph before Proposition 1.7). And she made progresses in the 4-dimensional case. Theorem E confirms the 4-dimensional case of this conjecture in full generality. The higher-dimensional case remains open.

We can also reinterpret Theorem F as results on the space of symplectic forms. Let $\mathbb{S}(M)$ be the space of all symplectic forms on $M$ and let $\mathbb{S}_{a}(M)$ be its subspace consisting of sympletctic forms in a fixed cohomology class $a \in H^{2}(M ; \mathbb{R})$. These spaces have also been of interest. For example, it is an open question whether $\mathbb{S}_{a}(M)$ is connected for all symplectic 4-manifold $M$ (i.e., whether cohomologous symplectic forms are always isotopic in dimension 4). One way to study the topology of $\mathbb{S}_{a}(M)$ is via the embedding
$$\mathbb{S}_{a}(M) \hookrightarrow \mathcal{S}(M):=\left\{\alpha \in \Omega^{2}(M) \mid \alpha \wedge \alpha \text { is nowhere vanishing }\right\}$$
into the space of almost symplectic forms, whose homotopy type can be understood by the classical obstruction theory. Note that a theorem by Gromov [14] states that (3) is always a homotopy equivalence when $M$ is an open manifold.

Using a long exact sequence relating the homotopy groups of $\operatorname{Diff}(M), \operatorname{Symp}(M, \omega)$ and $\mathbb{S}_{[\omega]}(M)$, Theorem F implies the following corollary.
Corollary G. The following results hold for any closed symplectic 4-manifold $(M, \omega)$.
\begin{itemize}
\item[(1)] There is a subgroup $\mathbb{Z}^{R_{M}}$ in $H_{1}\left(\mathbb{S}_{[\omega]}(M) ; \mathbb{Z}\right)$.
\item[(2)] There is a subgroup $\mathbb{Z}_{M}^{R_{M}^{2}}$ in $\operatorname{ker}\left(H_{1}\left(\mathbb{S}_{[\omega]}(M) ; \mathbb{Z}\right) \rightarrow H_{1}(\mathcal{S}(M) ; \mathbb{Z})\right)$.
\item[(3)] Suppose $b_{2}^{+}(M) \neq 2,3$. Then there is a subgroup $\mathbb{Z}_{M}^{R_{M}^{1}}$ in $H_{1}(\mathbb{S}(M) ; \mathbb{Z})$.
\item[(4)] Suppose $b_{2}^{+}(M) \neq 3$. Then there is a subgroup $\mathbb{Z}^{R_{M}^{1}}$ in $\pi_{1}(\mathbb{S}(M) ; \mathbb{Z})$.
\end{itemize}
1.3. Fiberwise symplectic structures on the ADE family and the blown-up family. Proof of Theorem F relies on the study of fiberwise symplectic structures on two families of 4-manifolds: the blown-up family and the ADE family. Both appears naturally when one studies surface singularities.

We start by explaining our terminologies. Let
$$M \hookrightarrow \widetilde{M} \xrightarrow{p} \mathcal{Q}$$
be a smooth fiber bundle whose fiber $M$ is a smooth 4-manifold and whose base $\mathcal{Q}$ is another smooth, connected manifold. We fix a base point $b_{0} \in \mathcal{Q}$ and fix a diffeomorphism $M \cong p^{-1}\left(b_{0}\right)$. We denote this bundle by $\widetilde{M} / \mathcal{Q}$ and treat it as a smooth family of 4-manifolds parameterized by $\mathcal{Q}$. For simplicity, we always assume that $\widetilde{M} / \mathcal{Q}$ is a homology product, i.e., $\pi_{1}\left(\mathcal{Q}, b_{0}\right)$ acts trivially on $H^{*}(M ; \mathbb{Z})$.

By a fiberwise symplectic structure on $\widetilde{M} / \mathcal{Q}$, we mean a smooth family $\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$ of symplectic forms on the fibers $\left\{p^{-1}(b)\right\}_{b \in \mathcal{Q}}$. A fiberwise symplectic structure induces a characteristic map
$$\rho: \mathcal{Q} \rightarrow\left\{a \in H^{2}(M ; \underset{6}{\mathbb{R}}) \mid a \cdot a>0\right\} \simeq S^{b_{2}^{+}(M)}$$
defined by $\rho(b)=\left[\omega_{b}\right]$.
Now we introduce the blown-up family. Let $M^{\prime}$ be a smooth 4-manifold. We pick a point $p \in M^{\prime}$ and identify a neighborhood of $U$ of $p$ with the unit disk $D(\mathbb{H})$ in $\mathbb{H}$ (the space of quoternions). Consider the space
$$\mathcal{Q}:=\left\{b \in \mathbb{H} \mid b^{2}=-1\right\}=\left\{x \mathrm{i}+y \mathrm{j}+z \mathrm{k} \mid x^{2}+y^{2}+z^{2}=1\right\} \cong S^{2}$$
Via the right multiplication, each point $b \in \mathcal{Q}$ gives a complex structure $J_{b}$ on $U$. We take the trivial fiber bundle $\mathcal{Q} \times M^{\prime}$ and blow up the fiber $\{b\} \times M^{\prime}$ at $(b, p)$ using $J_{b}$. This gives a smooth family
$$M=M^{\prime} \# \overline{\mathbb{C P}^{2}} \hookrightarrow \widetilde{M} \rightarrow \mathcal{Q},$$
called the blown-up family. We use $S$ to denote the exceptional divisor in $M$ and use PD[S] to denote its Poincaré dual. By computing the family Seiberg-Witten invariant of the blown-up family, we prove the following result.

Theorem H. Let $\widetilde{M} / \mathcal{Q}$ be a blown-up family that admits a fiberwise symplectic structure $\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$ with canonical class $K \in H^{2}(M ; \mathbb{Z})$. Suppose $\langle K,[S]\rangle=-1$. Then both of the following conclusions hold:
\begin{itemize}
\item[(i)] $b_{2}^{+}(M)=3$;
\item[(ii)] The characteristic map (4) has mapping degree ±1.
\end{itemize}

By [22, Theorem 1], the condition $\langle K,[S]\rangle=-1$ is automatically satisfied unless $M$ is rational or ruled. So we get the following corollary.

Corollary $\mathbf{I}$. Let $\widetilde{M} / \mathcal{Q}$ be a blown-up family. Suppose the fiber $M$ satisfies $b_{2}^{+}(M) \neq 1,3$. Then $\widetilde{M} / \mathcal{Q}$ does not admit a fiberwise symplectic structure.

Next, we introduce the ADE family. Recall that an ADE singularity is a discrete surface singularity that locally models on the quotient $\mathbb{H} / \Gamma$, where $\Gamma$ is a finite subgroup of $\operatorname{Sp}(1)$. Up to conjugacy, such groups one-one correspond to Dynkin diagrams of type A, D or E.

Given any complex structure on $\mathbb{H}$ that is compatible with the action of $\Gamma$, the singular variety $\mathbb{H} / \Gamma$ has a minimal resolution. Therefore, we can take the product family $\mathcal{Q} \times$ $D(\mathbb{H}) / \Gamma$ and resolve the fiber $\{b\} \times D(\mathbb{H}) / \Gamma$ using the complex structure $J_{b}$. By doing this, we get a smooth (but not algebraic) family
$$M_{1} \rightarrow \widetilde{M}_{1} \rightarrow \mathcal{Q}$$
whose fiber $M_{1}$ is a complex 4-manifold with boundary $Y=S^{3} / \Gamma$. Let $M$ be any closed 4-manifold such that $M_{1}$ can be embedded smoothly. (e.g., $M$ is the resolution of an algebraic surface with a single ADE singularity.) Then $M$ admits a smooth decomposition $M_{1} \cup_{Y} M_{2}$. By gluing the family (5) with the product family $\mathcal{Q} \times M_{2}$, we obtain a smooth family
$$M \hookrightarrow \widetilde{M}=\widetilde{M}_{1} \cup\left(\mathcal{Q} \times M_{2}\right) \rightarrow \mathcal{Q},$$
called the ADE family. (Note that for an $A_{1}$-singularity, this construction works for any $M$ that contains a smoothly embedded -2-sphere $S$. In this case, $M_{1}$ is just a tubular neighborhood of $S$.)

Theorem J. Let $\widetilde{M} / \mathcal{Q}$ be an ADE family whose fiber is minimal. Suppose there is a fiberwise symplectic structure $\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$ on $\widetilde{M} / \mathcal{Q}$. Then at least one of following two conclusion holds:
\begin{itemize}
\item[(1)] For homology class $a \in H_{2}\left(M_{0} ; \mathbb{Z}\right)$ with $a \cdot a=-2$ (such classes one-one correspond to roots of the corresponding Dynkin diagram), the function $\mathcal{Q} \rightarrow \mathbb{R}$ defined by $b \mapsto\left\langle\left[\omega_{b}\right], a\right\rangle$ takes both positive and negative values, or
\item[(2)] $b_{2}^{+}(M)=3, K$ is torsion, and characteristic map (4) has mapping degree ±1.
\end{itemize}

Corollary K. Any ADE family does not admit a fiberwise minimal symplectic structure in a constant cohomology class.
1.4. Statement of the gluing theorem. Now we state our gluing theorem. We describe our setting as follows: Let
$$M \hookrightarrow \widetilde{M} \xrightarrow{p} \mathcal{Q}$$
be a smooth family of closed 4-manifolds. Again, we assume that $\widetilde{M} / \mathcal{Q}$ is a homology product. We further assume that $\widetilde{M} / \mathcal{Q}$ admits a smooth decomposition
$$\widetilde{M}=\widetilde{M}_{1} \cup_{\mathcal{Q} \times Y}\left(\mathcal{Q} \times M_{2}\right),$$
where $\widetilde{M}_{0} / \mathcal{Q}$ is a (possibly nontrivial) family whose fiber $M_{1}$ is a 4-manifolds with boundary $Y$, and $M_{2}$ is a 4-manifold with boundary $-Y$. By removing a small disk from $M_{2}$ and each fiber of $\widetilde{M}_{1}$, we obtain a single cobordism
$$W_{12}=M_{2} \backslash \AA^{4}: Y \rightarrow S^{3}$$
and a family of cobordisms
$$\widetilde{W}_{01}=\widetilde{M}_{1} \backslash\left(\mathcal{Q} \times \stackrel{\circ}{D}^{4}\right): S^{3} \rightarrow Y .$$
We pick a family spin ${ }^{c}$ structure $\mathfrak{s}_{\widetilde{W}_{01}}$ on $\widetilde{W}_{01} / \mathcal{Q}$ and a spin ${ }^{c}$ structure $\mathfrak{s}_{W_{12}}$ on $W_{12}$ such that $\left.\mathfrak{s}_{\widetilde{W}_{01}}\right|_{\mathcal{Q} \times Y}$ is the pull-back of $\left.\mathfrak{s}_{W_{12}}\right|_{Y}$. We let $\mathbb{S}$ be the set of family spin ${ }^{c}$-structures $\widetilde{\mathfrak{s}}$ on $\widetilde{M} / \mathcal{Q}$ that satisfies
$$\left.\widetilde{\mathfrak{s}}\right|_{\widetilde{W}_{01}}=\mathfrak{s}_{\widetilde{W}_{01}},\left.\quad \widetilde{\mathfrak{s}}\right|_{W_{12}}=\mathfrak{s}_{W_{12}} \quad \text { and } \quad d(\widetilde{\mathfrak{s}}, \widetilde{M})=0 \text {. }$$
Here
$$d(\widetilde{\mathfrak{s}}, \widetilde{M}):=\frac{c_{1}\left(\left.\widetilde{\mathfrak{s}}\right|_{M}\right)^{2}[M]-2 \chi(M)-3 \sigma(M)}{4}+\operatorname{dim}(\mathcal{Q})$$
denotes the expected dimension of the parametrized moduli space. Note that when $Y$ is a rational homology 3-sphere $\left(\mathrm{QHS}^{3}\right), \mathbb{S}$ contains at most one element.

Theorem L. We have the following results regarding the family Seiberg-Witten invariant.
\begin{itemize}
\item[(1)] Suppose $b_{2}^{+}\left(M_{2}\right)>1$. Then we have
$$\sum_{\tilde{\mathfrak{s}} \in \mathbb{S}} \operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1}), \overrightarrow{H M}^{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)(\widetilde{1})\right\rangle$$
\end{itemize}
(2) Suppose $b_{2}^{+}(M)>b_{2}^{+}\left(M_{2}\right)=1$. Then we have
$$\sum_{\widetilde{\mathfrak{s}} \in \mathbb{S}} \operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1}), \overrightarrow{H M}^{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{ \pm}(\check{1})\right\rangle .$$
(3) Suppose $b_{2}^{+}(M)=b_{2}^{+}\left(M_{2}\right)=1$. Then we have
$$\sum_{\tilde{\mathfrak{s}} \in \mathbb{S}} \operatorname{FSW}_{ \pm}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1}), \overrightarrow{H M}^{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)_{ \pm}(\check{1})\right\rangle .$$
Here $\operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})$ and $\operatorname{FSW}_{ \pm}(\widetilde{M}, \widetilde{\mathfrak{s}})$ denote the family Seiberg-Witten invariants for canonical chambers (see Section 2); $\check{1}$ and $\widehat{1}$ denote canonical generators of the monopole Floer (co)homology of $S^{3} ; \overrightarrow{H M}^{*}(-)$ and $\widehat{H M}_{*}(-)$ denote two different versions of cobordism-induced maps; and $\langle-,-\rangle$ denotes the canonical pairing between the monopole Floer homology of $Y$ and the monopole Floer cohomology of $Y$.

Theorem L is a generalization of Kronheimer-Mrowka's result [19] to the family setting and the proof is adapted from their proof. When the cutting 3-manifold $Y$ is an L-space, one can recover $\widehat{H M}_{*}\left(\widetilde{W}_{01}, \mathfrak{s}_{\widetilde{W}_{01}}\right)(\widehat{1})$ by studying the wall-crossing of the family Dirac opeartors and recover $\overrightarrow{H M}^{*}\left(W_{12}, \mathfrak{s}_{W_{12}}\right)(\check{1})$ from the Seiberg-Witten invariant of the fiber $M$. In this case, Theorem L can be used to deduce a relation between the Seiberg-Witten invariants of the family $\widetilde{M} / \mathcal{Q}$ and the fiber $M$.

Theorem M. Let $\widetilde{M} / \mathcal{Q}$ be a family of closed 4-manifolds with a connected, even dimensional base $\mathcal{Q}$. Suppose $\pi_{1}(\mathcal{Q})$ acts trivially on $H_{*}(M ; \mathbb{Z})$ and suppose $\widetilde{M}$ has a decomposition of the form (6) with $b_{1}\left(M_{1}\right)=0$ and $Y$ being an $L$-space. Let $\widetilde{\mathfrak{s}}$ be a family spin ${ }^{c}$ structure on $\widetilde{M}$ and let $\mathfrak{s}$ be a spin ${ }^{c}$ structure on the fiber $M$ which satisfy $\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}=\left.\mathfrak{s}\right|_{M_{2}}$ and $d(\mathfrak{s}) \geqslant d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$. Then we have the following results:
(1) Suppose $b_{2}^{+}\left(M_{1}\right)=0$ and $b_{2}^{+}\left(M_{2}\right)>1$. Then
$$\operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle c_{\frac{\operatorname{dim}(\mathcal{Q})}{2}}\left(-\left(\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right) \otimes L^{-1}\right)\right),[\mathcal{Q}]\right\rangle \cdot \operatorname{SW}(M, \mathfrak{s}) .$$
(2) Suppose $b_{2}^{+}\left(M_{1}\right)=0$ and $b_{2}^{+}\left(M_{2}\right)=1$. Then
$$\operatorname{FSW}_{ \pm}(\widetilde{M}, \widetilde{\mathfrak{s}})=\left\langle c_{\frac{\operatorname{dim}(\mathcal{Q})}{2}}\left(-\left(\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right) \otimes L^{-1}\right)\right),[\mathcal{Q}]\right\rangle \cdot \operatorname{SW}_{ \pm}(M, \mathfrak{s}) .$$
(3) Suppose $b_{2}^{+}\left(M_{1}\right)>0$ and $b_{2}^{+}(M)>1$. Then $\operatorname{FSW}(\widetilde{M}, \widetilde{\mathfrak{s}})=0$.
(4) Suppose $b_{2}^{+}\left(M_{1}\right)>0$ and $b_{2}^{+}(M)=1$. Then $\operatorname{FSW}_{ \pm}(\widetilde{M}, \widetilde{\mathfrak{s}})=0$.
Here $L$ is the unique complex line bundle over $\mathcal{Q}$ such that $\left(\left.\widetilde{\mathfrak{s}}\right|_{\mathcal{Q} \times M_{2}}\right) \otimes p^{*}\left(L^{-1}\right)$ is a pull back of $\left.\widetilde{\mathfrak{s}}\right|_{M_{2}}$. And $\operatorname{Ind}\left(\not D^{+}(\widetilde{M}, \widetilde{\mathfrak{s}})\right)$ denotes the index bundle of the family Dirac operator.

We note that when $M_{1}$ is a tubular neighborhood of an embedded sphere with negative self-intersection number (which is the case in many of our applications), Theorem M can be recovered from Liu's family blow-up formula and family switching formula [26, 27, 28].
1.5. Organization of the paper. In Section 2, we review the definition of the family Seiberg-Witten invariants and recall some of its important properties. In Section 3, we give a very quick review on the monopole Floer homology, following [19]. In Section 4, maps induced by family of cobordisms are defined. The gluing formula (Theorem L) is proved. In Section 6 and 7, we stdudy the ADE family and the blown-up family respectively. The family Seiberg-Witten invariants for these families are computed in Section 8. Theorem H and Theorem J are also proved in Section 8. Finally in Section 9, we prove Theorem A, Theorem E and their corollaries. Readers who are mainly interested in the topological applications could assume Theorem Land skip Section 2 through Section 5.

Acknowledgment We would like to thank Hokuto Konno, Sander Kupers, Tianjun Li, Daniel Ruberman, Weiwei Wu for many enlightening discussions. We are very grateful to Gleb Smirnov for explaining his work in [44] and for many useful comments. And we especially like to thank Peter Kronheimer for suggesting to study the ADE families and for explaining the argument that the $A_{1}$-family is topologically nontrivial.

\section*{2. Recollection of the family Seiberg-Witten theory}
2.1. The family Seiberg-Witten invariants. In this section, we briefly recall the definition and basic properties of the family Seiberg-Witten invariant. For a more detailed exposition, we refer to Li-Liu's paper [23], which carefully sets up the family Seiberg-Witten theory and proves a general wall-crossing formula.

Let $M$ be a connected, closed, smooth oriented 4-manifold. Consider a smooth fiber bundle $p: \widetilde{M} \rightarrow \mathcal{Q}$ whose fibers are diffeomorphic to $M$ and whose base is another connected, closed, oriented smooth manifold $\mathcal{Q}$. We use $M_{b}$ to denote the fiber over $b$. We fix a base point $b_{0} \in Q$ and set $M=M_{b_{0}}$. We treat this fiber bundle as a family of 4-manifolds over $\mathcal{Q}$ and denote it by $\widetilde{M} / \mathcal{Q}$. By taking monodromies, one obtains an action of $\pi_{1}\left(\mathcal{Q}, b_{0}\right)$ on $H_{*}(M ; \mathbb{Z})$

Definition 2.1. We say $\widetilde{M} / \mathcal{Q}$ is a homology product if the monodromy action is trivial.
For a homology product, one has a canonical identification between homology of a general fiber $M_{b}$ with the homology of $M$. From now on, we will assume all families we work with are homology products. (This is automatically satisfied if $\mathcal{Q}$ is simply-connected.) Let
$$T(\widetilde{M} / \mathcal{Q})=\operatorname{ker}\left(p_{*}: T \widetilde{M} \rightarrow T Q\right)$$
be the tangent bundle in the fiber direction. We equip $T(\widetilde{M} / \mathcal{Q})$ with a smooth Riemannian metric $g_{\widetilde{M} / \mathcal{Q}}=\left\{g_{b}\right\}_{b \in \mathcal{Q}}$. A family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}$ is a lift of the corresponding frame bundle to an principal bundle $P$ with fiber
$$\operatorname{Spin}^{c}(4)=\left(\operatorname{SU}(2) \times \operatorname{SU}(2) \times S^{1}\right) / \pm 1 .$$
Associated to $P$, we have a rank-4 Hermitian bundle $S$ over $\widetilde{M}$ (the "spinor bundle"), which is canonically decomposed as the direct sum $S^{+} \oplus S^{-}$. Let $\Lambda^{*} T^{*}(\widetilde{M} / \mathcal{Q})$ be the
bundle (over $\widetilde{M}$ ) of vertical differential forms. The Clifford multiplication gives an action on $S$ by vertical differential forms, which restricts to
$$\rho: \Lambda^{\text {even }}\left(T^{*}(\widetilde{M} / \mathcal{Q})\right) \otimes \mathbb{C} \rightarrow \operatorname{End}\left(S^{+}\right) .$$
We denote the restriction of $P, g_{\widetilde{M} / \mathcal{Q}}, S^{ \pm}$to the fiber $M_{b}$ by $P_{b}, g_{b}$ and $S_{b}^{ \pm}$respectively. We use $\mathfrak{s}$ to denote the restriction of $\widetilde{\mathfrak{s}}$ to $M$.

Now we consider the configuration space
$$\begin{array}{r}
\mathcal{C}:=\left\{\left(b, A_{b}, \phi_{b}\right) \mid b \text { is a point in } \mathcal{Q} . A_{b} \text { is a spin }{ }^{c} \text {-connection on } P_{b},\right. \\
\text { and } \left.\phi_{b} \text { is a smooth section of } S_{b}^{+} .\right\}
\end{array}$$
This is a fiber bundle over $\mathcal{Q}$ whose fiber is a Fréchet space. The (unperturbed) Seiberg-Witten equations for a point $\left(b, A_{b}, \phi_{b}\right) \in \mathcal{C}$ can be written as
$$\begin{aligned}
\rho\left(F_{A_{b}^{t}}^{+}\right)+\left(\phi_{b} \phi_{b}^{*}\right)_{0} & =0 \\
\not D_{A_{b}}^{+} \phi_{b} & =0 .
\end{aligned}$$
Here $A_{b}^{t}$ denotes the induced connection on the determinant bundle $\operatorname{det}\left(S_{b}^{+}\right)$and $F_{A_{b}^{t}}^{+} \in$ $\Omega_{2}^{+}\left(M_{b} ; i \mathbb{R}\right)$ denotes the self-dual part of its curvature. $\not D_{A_{b}}^{+}$denotes the Dirac operator. The endomorphism $\left(\phi_{b} \phi_{b}^{*}\right)_{0} \in \operatorname{End}\left(S_{b}^{+}\right)$is defined by the formula
$$\psi \mapsto\left\langle\psi, \phi_{b}\right\rangle \cdot \phi_{b}-\frac{\left|\phi_{b}\right|^{2}}{2} \psi .$$
A solution of (7) is called reducible if $\phi_{b}=0$. To achieve transversality and to avoid reducible solutions, one needs to introduce a perturbation on the Seiberg-Witten equations as follows: Take a smooth family $\widetilde{\omega}=\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$ of self-dual 2-forms on the fibers $\left\{M_{b}\right\}_{b \in \mathcal{Q}}$. The $\widetilde{\omega}$-perturbed Seiberg-Witten equations are written as
$$\begin{aligned}
\rho\left(F_{A_{b}^{t}}^{+}\right)+\left(\phi_{b} \phi_{b}^{*}\right)_{0} & =\rho\left(\mathrm{i} \omega_{b}\right) \\
\not D_{A_{b}}^{+} \phi_{b} & =0 .
\end{aligned}$$
There is a condition on $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ which can ensure that (8) has no reducible solutions. To state this condition, we use $I\left(M_{b}\right)$ to denote $H^{2}\left(M_{b} ; \mathbb{R}\right)$. Then $I\left(M_{b}\right)$ can be identified with the space of harmonic 2-forms on $M_{b}$ with respect to the metric $g_{b}$. There is a metric-dependent decomposition
$$I\left(M_{b}\right)=I^{+}\left(M_{b}, g_{b}\right) \oplus I^{-}\left(M_{b}, g_{b}\right)$$
where $I^{+}\left(M_{b}, g_{b}\right)$ and $I^{-}\left(M_{b}, g_{b}\right)$ denote the space of self-dual and anti-self-dual harmonic 2-forms respectively. This decomposition induces a projection
$$P_{I^{+}}: I\left(M_{b}\right) \rightarrow I^{+}\left(M_{b}, g_{b}\right) .$$
We have another projection map
$$P_{I}: \Omega^{2}\left(M_{b}\right) \rightarrow I\left(M_{b}\right)$$
defined by the following condition
$$\int_{M_{b}} P_{I}(\omega) \wedge \kappa=\int_{M_{b}} \omega \wedge \kappa \text { for any harmonic 2-form } \kappa \text {. }$$
Note that $P_{I}(\omega) \in I^{+}\left(M_{b}, g_{b}\right)$ if $\omega$ is self-dual.
Definition 2.2. The pair $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ is called admissible if for any $b \in \mathcal{Q}$, we have
$$P_{I}\left(\omega_{b}\right)+2 \pi P_{I}+c_{1}(\mathfrak{s}) \neq 0 .$$

Suppose $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ is admissible. Then the Chern-Weil formula ensures that the curvature equation $F_{A_{b}^{t}}^{+}=i \omega_{b}$ has no solution for any $b$. Hence (8) has no reducible solutions. Consider the Seiberg-Witten moduli space
$$\mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right):=\left\{\left(b, A_{b}, \phi_{b}\right) \in \mathcal{C} \text { that solves (8) }\right\} / \text { gauge transformations. }$$

We say $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ is regular if it is admissible and if the moduli space $\mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ is regular at each point. (That means the linearized Seiberg-Witten equations combined with the gauge fixing equation is form a surjective Fredholm operator. See [23, Page 6] for a precise definition). By the Sard-Smale theorem, this holds for a generic pair $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$. In this case, the moduli space is a compact, smooth manifold of dimension
$$d(\widetilde{M}, \widetilde{\mathfrak{s}}):=\frac{c_{1}^{2}\left(S_{b}^{+}\right)[M]+3 \sigma(M)+2 \chi(M)}{4}+\operatorname{dim} \mathcal{Q} .$$
Since the bundle $\widetilde{M} / Q$ is a homology product, the moduli space $\mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ is orientable and an orientation is specified by an orientation of $\mathcal{Q}$ together with a homological orientation on $M$ (i.e. an orientation of $H^{1}(M ; \mathbb{R}) \oplus H_{+}^{2}(M ; \mathbb{R})$ ).

Although the family Seiberg-Witten invariant can be defined in general. We will focus on the case $d(\widetilde{M}, \widetilde{\mathfrak{s}})=0$ in this paper. Then we use $\# \mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ to denote the number of points in $\mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right)$, counted with sign.

Just like the classical Seiberg-Witten theory, the family Seiberg-Witten theory has a wall-crossing phenomena. Namely, the space of all admissible pairs $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ has a certain chamber structure and the number $\# \mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ will change if the pair goes from one chamber to another. These chambers correspond to elements in the cohomotopy group of $\mathcal{Q}$. To give a precise description, we consider the positive cone
$$V^{+}(M):=\left\{\mathfrak{a} \in H^{2}(M ; \mathbb{R}) \mid(\mathfrak{a} \cup \mathfrak{a})[M]>0\right\} .$$
We use $\left[\mathcal{Q}, V^{+}(M)\right]$ to denote the set of homotopy classes of maps from the base $\mathcal{Q}$ to $V^{+}(M)$. Given any admissible pair $\left(g_{\widetilde{M} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right)$, we have a map from $\mathcal{Q}$ to $V^{+}(M)$ defined by
$$b \mapsto P_{I}\left(\omega_{b}\right)+2 \pi P_{I^{+}} c_{1}(\mathfrak{s}) \in I^{+}\left(M_{b}, g_{b}\right)-\{0\} \subset V^{+}(M) .$$

This map represents an element $\xi\left(g_{\widetilde{M} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right) \in\left[\mathcal{Q}, V^{+}(M)\right]$.
Lemma 2.3. Any element in $\xi \in\left[\mathcal{Q}, V^{+}(M)\right]$ can be realized by some regular pair $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$. Furthermore, the number $\# \mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right)$ only depends on $\xi\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$.

Proof. This is essentially proved in [23]. The authors constructed a bundle $\mathcal{P}$ over $\mathcal{Q}$ whose fiber at $b$ consists of all pairs $(W, l)$, where $W$ is a maximal subspace of $H^{2}\left(M_{b} ; \mathbb{R}\right)$ on which the intersection form is positive definite, and $l$ is a vector in $H^{2}\left(M_{b} ; \mathbb{R}\right)$ that is not perpendicular to $W$. In our situation, since $\widetilde{M}$ is a homology product, the bundle $\mathcal{P}$ is trivial. And there is a bundle map from $\mathcal{P}$ to the trivial bundle $\mathcal{Q} \times V^{+}(M)$ defined by
$$(W, l) \mapsto \text { orthogonal projection of } l \text { to } W \text {. }$$
Since this bundle map induces a homotopy between the fibers, our lemma is essential the same as [23, Proposition 3.6], which states that the chamber structure is classified by homotopy classes of sections of $\mathcal{P}$. \(\square\)

Proof of the following lemma is elementary so we omit.
Lemma 2.4. Let $V$ be a real vector space with a symmetric non-degenerate bilinear form $\langle-,-\rangle$, with $k$ positive eigenvalues and $l$ negative eigenvalues. Assume $k \geqslant 1$. Then we have the the following conclusions:
\begin{itemize}
\item[(i)] The space $V^{+}:=\{\alpha \in V \backslash\{0\} \mid\langle\alpha, \alpha\rangle>0\}$ is homotopy equivalent to $S^{k-1}$.
\item[(ii)] For any $x \in V \backslash\{0\}$ such that $\langle x, x\rangle \geqslant 0$, the space
$$V_{x}^{+}:=\{\alpha \in V \backslash\{0\} \mid\langle\alpha, \alpha\rangle>0,\langle\alpha, x\rangle>0\} .$$
$V_{x}^{+}$is always contractible.
\end{itemize}

By Lemma 2.4, we have $V^{+}(M) \simeq S^{b_{2}^{+}(M)-1}$.
Definition 2.5. For any $\widetilde{\mathfrak{s}}$ with $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$ and any $\xi \in\left[\mathcal{Q}, V^{+}(M)\right]$, we define the family Seiberg-Witten invariant
$$\operatorname{FSW}_{\xi}(\widetilde{M}, \widetilde{\mathfrak{s}}):=\# \mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$$
for any regular pair $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ with $\xi\left(g_{\widetilde{M} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right)=\xi$.
A chamber is called a canonical chamber if it is represented by a constant map. When $b_{2}^{+}(M) \geqslant 2$, the space path $V^{+}(M)$ is connected, so there is only one canonical chamber, denoted by $\xi_{c}$. When $b_{2}^{+}(M)=1$, the space $V^{+}$has two components. By fixing an orientation on $H_{+}^{2}(M ; \mathbb{R})$, we can talk about the positive component and the negative component. The corresponding chambers are called the "positive canonical chamber" and the "negative canonical chamber", denoted by $\xi_{c}^{+}$and $\xi_{c}^{-}$respectively. We will also write the family Seiberg-Witten invariant for $\xi_{c}, \xi_{c}^{+}, \xi_{c}^{-}$as FSW(-), $\mathrm{FSW}_{+}(-)$and $\mathrm{FSW}_{-}(-)$ respectively.

Example 2.6. Let $\mathcal{Q}=S^{2}$. Then $\left[\mathcal{Q}, V^{+}(M)\right]$ contains a single element $\xi_{c}$ when $b_{2}^{+}(M) \neq 1,3$. When $b_{2}^{+}(M)=1$, we have $\left[\mathcal{Q}, V^{+}(M)\right]=\left\{\xi_{c}^{+}, \xi_{c}^{-}\right\}$. When $b_{2}^{+}(M)=3$, there is a bijection $\left[\mathcal{Q}, V^{+}(M)\right] \cong \mathbb{Z}$ provided by the mapping degree. Let $\xi^{j}$ be chamber corresponding to $j \in \mathbb{Z}$. Then the general wall-crossing formula [23, Theorem 4.10] specializes to
$$\operatorname{FSW}_{\xi^{j}}(\widetilde{M}, \widetilde{\mathfrak{s}})=\operatorname{FSW}_{\xi_{c}}(\widetilde{M}, \widetilde{\mathfrak{s}})+j \cdot C(M, \mathfrak{s}) .$$
Here $C(M, \mathfrak{s})$ is the so-called "wall-crossing number" and it only depends on the fiber $M$. (See [23]) for the precise formula.) We call $\xi^{1}$ the winding chamber.

Lemma 2.7. Suppose $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$. Then one has
$$\operatorname{FSW}_{\xi}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})=\operatorname{FSW}_{\xi}\left(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}} \otimes p^{*}(L)\right)$$
for any complex line bundle $L$ over $\mathcal{Q}$ and any chamber $\xi \in\left[\mathcal{Q}, V^{+}(M)\right]$.
Proof. We pick a pair $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ which is regular with respect to both $\widetilde{\mathfrak{s}}$ and $\widetilde{\mathfrak{s}} \otimes p^{*}(L)$. Then the moduli spaces $\mathcal{M}\left(\widetilde{\mathfrak{s}}, g_{\widetilde{M} / \mathcal{Q}^{\prime}} \widetilde{\omega}\right)$ and $\mathcal{M}\left(\widetilde{\mathfrak{s}} \otimes p^{*}(L), g_{\widetilde{M} / \mathcal{Q}^{\prime}} \widetilde{\omega}\right)$ are both finite sets. Therefore, there are only finitely many $b_{1}, \cdots, b_{n} \in \mathcal{Q}$ that appears as the first component of some point in either moduli spaces. For each $b_{i}$, we pick a unit vector $v_{i}$ in the corresponding fiber $L_{b_{i}}$ of $L$. The isomorphism $\phi \mapsto \phi \otimes v_{i}$ between the spinor bundles $S_{b_{i}}^{ \pm} \rightarrow S_{b_{i}}^{ \pm} \otimes L_{b_{i}}$ induces an isomorphism
$$\left.\left.\widetilde{\mathfrak{s}}\right|_{M_{b_{i}}} \cong\left(\widetilde{\mathfrak{s}} \otimes p^{*}(L)\right)\right|_{M_{b_{i}}} \quad \text { for } i=1, \cdots n .$$
These isomorphisms together induce a sign-preserving bijection between $\mathcal{M}\left(\widetilde{\mathfrak{s}}, g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ and $\mathcal{M}\left(\widetilde{\mathfrak{s}} \otimes p^{*}(L), g_{\widetilde{M} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right)$. This finishes the proof. \(\square\)

Remark 4. In [23], the authors studied a more general version of the family Seiberg-Witten invariant when $d\left(\mathfrak{s}_{\widetilde{M}}, \widetilde{M}\right)>0$, by paring the fundamental class $\left[\mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)\right]$ with various cohomology classes of the parametrized configuration space. To adapt (12) to this more general setting, one needs to introduce certain correction terms. We will not pursue this generality in this paper.

The next lemma addresses the behavior of the family Seiberg-Witten invariant under a pull-back of the base.
Lemma 2.8. Let $\widetilde{M} / \mathcal{Q}$ be a homology product with fiber $M$. Consider a smooth map $f: \mathcal{Q}^{\prime} \rightarrow \mathcal{Q}$ from some manifold $\mathcal{Q}^{\prime}$ of the same dimension with $\mathcal{Q}$. Then the pull-back family $\widetilde{M}^{\prime} / \mathcal{Q}^{\prime}$ is also a homology product. Moreover, given any family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}$ and any chamber $\xi \in\left[\mathcal{Q}, V^{+}(M)\right]$, we let $\mathfrak{s}_{\widetilde{M}}$, and $\xi^{\prime} \in\left[\mathcal{Q}^{\prime}, V^{+}(M)\right]$ be their pull-backs via $f$. Assume $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$. Then we have
$$\operatorname{FSW}_{\xi^{\prime}}\left(\widetilde{M}^{\prime} / \mathcal{Q}^{\prime}, \mathfrak{s}_{\widetilde{M}^{\prime}}\right)=\operatorname{deg}(f) \cdot \operatorname{FSW}_{\xi}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}}) .$$
Proof. We pick an generic, admissible pair $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ in the chamber $\xi$. Let $\left(g_{\widetilde{M}^{\prime} / \mathcal{Q}^{\prime}}, \widetilde{\omega}^{\prime}\right)$ be the pull-back of $\left(g_{\widetilde{M} / \mathcal{Q}}, \widetilde{\omega}\right)$ via $f$. We use $\left(g_{\widetilde{M} / \mathcal{Q}^{\prime}}, \widetilde{\omega}\right)$ and $\left(g_{\widetilde{M^{\prime}} / \mathcal{Q}^{\prime}}, \widetilde{\omega}^{\prime}\right)$ to define the family Seiberg-Witten equations on $\widetilde{M} / \mathcal{Q}$ and $\widetilde{M}^{\prime} / \mathcal{Q}^{\prime}$ respectively. By transversality, there are only finitely many points $b_{1}, \cdots, b_{n} \in \mathcal{Q}$ such that the Seiberg-Witten equations have a solution on the fiber $M_{b_{i}}$. By suitably homotope $f$, we may assume that $b_{i}$ is a regular values of $f$. For a point $b^{\prime} \in f^{-1}\left(b_{i}\right)$, we let $\# \mathcal{M}_{b^{\prime}} \in \mathbb{Z}$ be the the contribution of solutions on $M_{b^{\prime}}$ to $\mathrm{FSW}_{\xi^{\prime}}\left(\widetilde{M}^{\prime} / \mathcal{Q}^{\prime}, \mathfrak{s}_{\widetilde{M}^{\prime}}\right)$ and let $\# \mathcal{M}_{b_{i}}$ be the contribution of solutions on $M_{b}$ to $\operatorname{FSW}_{\xi}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})$. By definition, we have
$$\# \mathcal{M}_{b^{\prime}}=\operatorname{deg}\left(f, b^{\prime}\right) \cdot \# \mathcal{M}_{b_{i}}$$
where $\operatorname{deg}\left(f, b^{\prime}\right)$ denotes the local degree of $f$ at $b^{\prime}$. Summing over these equalities over all points in $\bigcup f^{-1}\left(b_{i}\right)$, we finish the proof. \(\square\)

It turns out that one can define group homomorphisms from $\pi_{k}(\operatorname{Diff}(M))$ to $\mathbb{Z}$ using the family Seiberg-Witten invariants (see [39, 3, 5]). We briefly recall this construction here. In Section 9, we will use them to detect the $\mathbb{Z}^{\infty}$ summand in Theorem A.

For simplicity, we focus on the case $b_{1}(M)=0$. Let $\gamma$ be an element in $\pi_{k}(\operatorname{Diff}(M))$ for some $k \geqslant 0$. When $k=0$, we assume that $\gamma$ induces the identity map on $H_{*}(M ; \mathbb{Z})$. Let $\widetilde{\gamma}: S^{k} \times M \rightarrow S^{k} \times M$ be a diffeomorphism that represents $\gamma$. Then we use $\widetilde{\gamma}$ as the clutching function and form the smooth fiber bundle
$$\widetilde{M}:=\left(D^{k+1} \times M\right) \cup_{\widetilde{\gamma}}\left(D^{k+1} \times M\right)$$
over $\mathcal{Q}=S^{k+1}$. The following lemma can be proved by a straightforward application of the Serre spectral sequence.

Lemma 2.9. Any spin ${ }^{c}$ structure $\mathfrak{s}$ on the fiber $M$ can be extended to a family spin ${ }^{c}$ structure $\widetilde{\mathfrak{s}}$ on $\widetilde{M} / \mathcal{Q}$. Such extension is unique when $k \neq 1$. When $k=1$, any two extensions are related by a twisting with a complex line bundle pulled back from $\mathcal{Q}$.

Let $\mathfrak{s}$ be a $\operatorname{spin}^{c}$-structures on $M$ with $d(\mathfrak{s}, M)=-k-1$. We assume $b^{+}(M)>1$ for now. Then the Seiberg-Witten invariant for $\gamma$ is defined as
$$\operatorname{SW}(\gamma, \mathfrak{s}):=\operatorname{FSW}_{\xi_{c}}(\widetilde{M}, \widetilde{\mathfrak{s}}) .$$
Here $\widetilde{\mathfrak{s}}$ is any extension of $\mathfrak{s}$. By Lemma 2.9 and Lemma 2.7, $\operatorname{SW}(\gamma, \mathfrak{s})$ is well-defined.
The following proposition is proved in [4, Theorem 2.6 and Theorem 2.9].
Proposition 2.10. The map $\operatorname{SW}(-, \mathfrak{s}): \pi_{k}(\operatorname{Diff}(M)) \rightarrow \mathbb{Z}$ is a group homomorphism. Furthermore, for any $\gamma$, the number $\operatorname{SW}(\gamma, \mathfrak{s})$ is nonzero for only finitely many $\mathfrak{s}$ with $d(\mathfrak{s}, M)=-k-1$.

Next we turn to the case $b^{+}(M)=1$. We fix a choice of $H \in H^{2}(M ; \mathbb{R})$ with $H \cdot H>0$ and use it to fix an orientation on $H^{+}(M ; \mathbb{R})$. Then we define the "small-perturbation Seiberg-Witten invariant"
$$\operatorname{SW}_{H}(\gamma, \mathfrak{s}):=\left\{\begin{array}{ll}
\operatorname{FSW}_{\xi_{c}^{+}}(\widetilde{M}, \widetilde{\mathfrak{s}}) & \text { if } c_{1}(\mathfrak{s}) \cdot H \geqslant 0 \\
\mathrm{FSW}_{\xi_{c}^{-}}(\widetilde{M}, \widetilde{\mathfrak{s}}) & \text { if } c_{1}(\mathfrak{s}) \cdot H<0
\end{array} .\right.$$

The following lemma helps us to better understand the dependence of $\operatorname{SW}_{H}(\gamma, \mathfrak{s})$ on $H$.
Lemma 2.11. Suppose $H, H^{\prime}$ belongs to the same component of $V^{+}(M)$. Then for any fixed $n$, there exists only finitely many $\operatorname{spin}^{c}$ structures $\mathfrak{s}$ with $d(\mathfrak{s}, M)=n$ such that $c_{1}(\mathfrak{s}) \cdot H \geqslant 0$ whereas $c_{1}(\mathfrak{s}) \cdot H<0$.

Proof. By rescaling $H$ and $H^{\prime}$, we may assume that $H \cdot H=H \cdot H^{\prime}=1$. Let $m=b_{2}^{-}(M)$. Then we can choose a basis $\left\{e_{0}, e_{1}, \cdots, e_{m}\right\}$ for $H^{2}(M ; \mathbb{R})$ such that
$$e_{i} \cdot e_{j}:=\left\{\begin{array}{ll}
1 & \text { if } i=j=0 \\
-1 & \text { if } i=j>0 \\
0 & \text { if } i \neq j
\end{array} .\right.$$
and that $H=e_{0}, H^{\prime}=e_{0}-a e_{1}$ for some $a \in[0,1)$. Assume that
$$c_{1}(\mathfrak{s})=\sum_{i=0}^{m} x_{i} e_{i} \text { for } x_{i} \in \mathbb{R} .$$
Then our assumptions can be written as
$$x_{0}^{2}-x_{1}^{2}-\cdots-x_{m}^{2}=4 n-m+9, \quad x_{0} \geqslant 0, \quad x_{0}-a x_{1}<0 .$$
These (in)equalities together imply a uniform bound on $\left|x_{i}\right|$. So $c_{1}(\mathfrak{s})$ can take only finitely many values. Since there can be only finitely many $\mathfrak{s}$ with identical $c_{1}(\mathfrak{s})$, the proof is finished. \(\square\)

The following proposition is an analogue of Proposition 2.10 in the case $b_{2}^{+}(M)=1$.
Proposition 2.12. The map $\operatorname{SW}_{H}(-, \mathfrak{s}): \pi_{k}(\operatorname{Diff}(M)) \rightarrow \mathbb{Z}$ is a group homomorphism. Furthermore, for any $\gamma$, the number $\operatorname{SW}_{H}(\gamma, \mathfrak{s})$ is nonzero for only finitely many $\mathfrak{s}$ with $d(\mathfrak{s}, M)=-k-1$.

Proof. Proof of the first assertion is exactly the same as Proposition 2.10. So we focus on the second assertion. We fix a family metric $g_{\widetilde{M} / \mathcal{Q}}$. By Lemma 2.11, changing $H$ in the same component of $V^{+}(M)$ does not affect our conclusion. Therefore, we may assume that $H$ can be represented by self-dual harmonic 2-form on $\left(M_{b_{0}}, g_{b_{0}}\right)$. We set the perturbation 2-form $\widetilde{\omega}$ to be identically 0. A compactness argument for Seiberg-Witten moduli space (see 31, Theorem 5.2.4]) implies the following claim: There exist only finitely many $\mathfrak{s}$ with $d(\mathfrak{s}, M)=-k-1$ such that the moduli space $\mathcal{M}\left(g_{\widetilde{M} / \mathcal{Q}}, 0, \widetilde{\mathfrak{s}}\right)$ is nonempty for some extension $\widetilde{\mathfrak{s}}$ of $\mathfrak{s}$. In particular, this implies that for all but finitely many $\mathfrak{s}$ with $d(\mathfrak{s}, M)=-k-1$, the pair $\left(g_{\widetilde{M} / \mathcal{Q}}, 0\right)$ is admissible with respect to some extension $\widetilde{\mathfrak{s}}$ of $\mathfrak{s}$ (in particular, we have $c_{1}(\mathfrak{s}) \cdot H \neq 0$ ) and family Seiberg-Witten invariant $\operatorname{FSW}_{\xi}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})$ equals 0 for the corresponding chamber $\xi$. Since $\xi=\xi_{c}^{+}$when $c_{1}(\mathfrak{s}) \cdot H>0$ and $\xi=\xi_{c}^{-}$when $c_{1}(\mathfrak{s}) \cdot H<0$, we see that
$$\operatorname{SW}_{H}(\gamma, \mathfrak{s})=\operatorname{FSW}_{\xi}(\widetilde{M} / \mathcal{Q}, \widetilde{\mathfrak{s}})=0 .$$
This finishes the proof. \(\square\)
2.2. Seiberg-Witten invariants of symplectic 4-manifolds. In this section, we recall Taubes' remakable theorems about the Seiberg-Witten invariants of symplectic 4-manifolds. We will also state some of its corollaries that we need.

Theorem 2.13 (Taubes [46, 45]). Let $(M, \omega)$ be a symplectic 4-manifold. Suppose $b_{2}^{+}(X)>$ 1. Then the following result holds.
\begin{itemize}
\item[(1)] $\operatorname{SW}\left(M, \mathfrak{s}_{J}\right)= \pm 1$. Here $\mathfrak{s}_{J}$ is the canonical spin ${ }^{c}$ structure.
\item[(2)] Suppose $\operatorname{SW}\left(M, \mathfrak{s}_{J}+e\right) \neq 0$ for some $e \in H^{2}(M ; \mathbb{Z})$. Then $0 \leqslant e \cdot[\omega]$. The equality is achieved only when $e=0$. Furthermore, for any $\omega$-compatible almost complex structure $J$, the Poincaré dual of e can be represented by a $J$-holomorphic curve.
\end{itemize}
When $b_{2}^{+}(M)=1$ and we orient $H^{+}(M ; \mathbb{R})$ using $[\omega]$, the results hold for $\mathrm{SW}_{-}(M)$.

Remark 5. To avoid discussing wall-crossing, the statements of the main theorems in [45, 46] assume $b_{2}^{+}(M)>1$. But the whole proof actually works for $\mathrm{SW}_{-}(M)$ when $b_{2}^{+}(M)=1$ (see [45, Proof of Theorem 0.3]).

Part of Theorem 2.13 can be adapted to the family setting in a straightforward way.
Proposition 2.14. Let $\widetilde{M} / \mathcal{Q}$ be a smooth family that carries a fiberwise symplectic structure $\left\{\omega_{b}\right\}_{b \in \mathcal{Q}}$. (I.e. symplectic structures on the fibers that varies smoothly with b). Let $\xi_{\omega}$ be the "symplectic chamber" defined by the map $\mathcal{Q} \rightarrow V^{+}(M)$ that sends b to $-\left[\omega_{b}\right] \in V^{+}(M)$. Let $\widetilde{\mathfrak{s}}$ be family a spin ${ }^{c}$ structure such that $d(\widetilde{\mathfrak{s}}, \widetilde{M})=0$ and $\left.\widetilde{\mathfrak{s}}\right|_{M}=\mathfrak{s}_{J}+e$ for some nonzero $e \in H^{2}(M ; \mathbb{Z})$. Suppose $\operatorname{FSW}_{\xi_{\omega}}(\widetilde{M} ; \widetilde{\mathfrak{s}}) \neq 0$. Then there exists some $b \in \mathcal{Q}$ such that $e \cdot\left[\omega_{b}\right]>0$.

Proof. We pick a family metric $g_{\mathcal{M} / \mathcal{Q}}$ such that $g_{b}$ is compatible with $\omega_{b}$ for any $b$. Then we consider the the perturbation
$$\omega_{b}^{\prime}=-i \cdot F_{A_{\omega_{b}}}^{+}-r \omega_{b},$$
where $A_{\omega_{b}}$ is a canonical spin ${ }^{c}$ connection determined by $\omega_{b}$, and $r$ is a large positive number. Suppose $e \cdot[\omega] \leqslant 0$ for any $b \in \mathcal{Q}$. By the argument in [46], when $r$ is large enough, the Seiberg-Witten equations on any fiber have no solutions. So the corresponding family Seiberg-Witten invariant is 0 . Note that when $r \gg 0$, the term $-r \omega_{b}$ dominates the other terms in (13). So the chamber corresponding to $\left(g_{\mathcal{M} / \mathcal{Q}},\left\{\omega_{b}^{\prime}\right\}_{b \in \mathcal{Q}}\right)$ is the symplectic chamber $\xi_{\omega}$. \(\square\)

Another important theorem of Taubes is the following result, which states that symplectic 4-manifolds are all of "simple-type".

Theorem 2.15 (Taubes [45]). Let $(M, \omega)$ be a symplectic 4-manifold with $b_{2}^{+}>1$ and let $\mathfrak{s}$ be a $\operatorname{spin}^{c}$-structure such that $d(\mathfrak{s}, M)>0$. Then $\operatorname{SW}(M, \mathfrak{s})=0$.

Next, we state some results deduced from Theorem 2.13.
Theorem 2.16 (Taubes [45]). Let $(M, \omega)$ be a symplectic 4-manifold. Suppose $e \in$ $H_{2}(M ; \mathbb{Z})$ is represented by a smoothly embedded 2-sphere with self-intersection -1. Then for any $\omega$-compatible almost complex structure $J$, there is an embedded $J$-holomorphic curve $S$ in $M$ with self-intersection -1 . Furthermore, if we assume $b_{2}^{+}(M)>1$, then we may pick $S$ such that it represents ±e.

In the case $b_{2}^{+}(M)=1$, Li-Liu proved the following related result.
Theorem 2.17 (Li-Liu [21]). Let $(M, \omega)$ be a symplectic 4-manifold with $b_{2}^{+}(M)=1$. Let $K$ be the canonical class and let $e \in H_{2}(M ; \mathbb{Z})$ be a class with $e \cdot e=K \cdot e=-1$. Suppose $\mathrm{PD}(e)$ can be represented by a smoothly embedded 2-sphere with self-intersection-1. Then for any $\omega$-compatible almost complex structure $J$, there is a $J$-holomorphic curve $C$ that represents $\operatorname{PD}(e)$.

As for smoothly embedded sphere with self-intersection -2, we have the following result:

Lemma 2.18. Let $(M, \omega)$ be a symplectic 4-manifold that contains a smoothly embedded sphere $S$ with self-intersection -2. Assume $M$ is minimal. Then the pairing $\langle K,[S]\rangle$ must be 0.

Proof. The proof is adapted from Theorem 2.16. We use the reflection diffeomorphism $r: M \rightarrow M$ constructed as follows. Let $N$ be a closed tubular neighborhood of $S$. Then we identify $N$ with the unit disk bundle of the sphere $S^{2}$. A reflection on $S^{2}$ induces an orientation preserving diffeomorphism $r^{\prime}: N \rightarrow N$. The restriction $\left.r^{\prime}\right|_{\partial N}$ is an orientation preserving isometry on $\partial N=\mathbb{R P}^{3}$. The group of such isometry is $S O(3) \times S O(3)$. So $\left.r^{\prime}\right|_{\partial N}$ is smoothly isotopic to the identity map. By modifying $r^{\prime}$ near $\partial N$, we get a diffeomorphism $r^{\prime \prime}$ on $N$ that is identity near $\partial N$. By extending $\tau^{\prime \prime}$ with the identity map, we get the diffeomorphism $r: M \rightarrow M$ that is supported near $S$. The action $r^{*}$ on $H^{2}(M ; \mathbb{Z})$ is just the reflection along $\operatorname{PD}[S]$. Therefore, we have
$$r^{*}\left(\mathfrak{s}_{J}\right)=\mathfrak{s}_{J}-\langle K,[S]\rangle \cdot \operatorname{PD}([S])$$
Now we assume $b_{2}^{+}(M)>1$. (The argument when $b_{2}^{+}(M)=1$ is the same if we use SW_ instead of SW.) Suppose $K(S) \neq 0$. Then
$$\operatorname{SW}\left(M, r^{*}\left(\mathfrak{s}_{J}\right)\right)=\operatorname{SW}\left(M, \mathfrak{s}_{J}\right)= \pm 1 .$$
By Theorem 2.13 (2), the class $-\langle K,[S]\rangle \cdot[S]$ is represented by a $J$-holomorphic curve $C$. However, this is impossible: The self-intersection of $C$ equals $-\langle K,[S]\rangle^{2}<0$. But by the regularity theorem of $J$-holomorphic curves ([45, Proposition 7.1]), for a generic $J$, any $J$-holomorphic curve with negative self-intersection must contain a genus-0 component with self-intersection -1. This contradicts with our assumption that $M$ is minimal. \(\square\)

\section*{3. Recollection of the monopole Floer homology}
3.1. Definition of monopole Floer homology. In this section, we briefly recall the construction of the monopole Floer homology of 3-manifolds, following [19]. See also [24] for a self-contained survey.

Let $Y$ be a compact, connected, closed and oriented 3-manifold equipped with a Riemannian metric $g_{Y}$. Given a spin ${ }^{c}$ structure $\mathfrak{s}$ on $Y$, we can associate the spinor bundle $S_{Y}$, which a rank-2 Hermitian bundle over $Y$. We fix an integer $k \geqslant 3$ and let $\mathcal{C}(Y)$ be the $L_{k-1 / 2}^{2}$-completion of the affine space:
$\left\{(B, \phi) \mid B\right.$ is a smooth spin ${ }^{c}$-connection on $S_{Y}$ and $\phi$ is a smooth section of $\left.\left.S_{Y}\right\}\right\}$.
We call $\mathcal{C}(Y)$ the configuration space downstairs. There is a related space $\mathcal{C}^{\sigma}(Y)$ called the configuration space upstairs, which is the $L_{k-1 / 2}^{2}$-completion of the space:
$$\begin{array}{r}
\left\{(B, s, \psi) \mid B \text { is a smooth spinc-connection on } S_{Y}, s \in \mathbb{R}^{\geqslant 0}\right. \\
\text { and } \left.\phi \text { is a smooth section of } S_{Y} \text { with }|\phi|_{L^{2}}=1 .\right\}
\end{array}$$
There is a natural projection map $p: \mathcal{C}^{\sigma}(Y) \rightarrow \mathcal{C}(Y)$ defined by $p(B, s, \phi)=(B, s \phi)$. We call a point $(B, \phi) \in \mathcal{C}(Y)$ (resp. a point $(B, s, \phi) \in \mathcal{C}^{\sigma}(Y)$ ) reducible if $\phi=0$ (resp. $s=0$ ) and call it irreducible otherwise. We use $\mathcal{C}^{*}(Y)$ to denote the subspace of $\mathcal{C}(Y)$ consisting of irreducible points.

The gauge group $\mathcal{G}$ is defined as the $L_{k+1 / 2}^{2}$-completion of the space of smooth maps from $Y$ to $S^{1}$. Then $\mathcal{G}$ acts on $\mathcal{C}(Y)$ as
$$g(B, \psi):=\left(B-g^{-1} d g, g \phi\right)$$
and acts on $\mathcal{C}^{\sigma}(Y)$. as
$$g(B, s, \phi):=\left(B-g^{-1} d g, s, g \phi\right) .$$
We denote the quotient of $\mathcal{C}(Y), \mathcal{C}^{*}(Y)$ and $\mathcal{C}^{\sigma}(Y)$ by $\mathcal{G}$ respectively by $\mathcal{B}(Y), \mathcal{B}^{*}(Y)$ and $\mathcal{B}^{\sigma}(Y)$. Since the action of $\mathcal{G}$ on $\mathcal{C}^{*}(Y)$ and $\mathcal{C}^{\sigma}(Y)$ are free, the space $\mathcal{B}^{*}(Y)$ is a Hilbert manifold and $\mathcal{B}^{\sigma}(Y)$ is a Hilbert manifold with boundary. The map $p$ induces a homeomorphism between $\mathcal{B}^{*}(Y)$ and the interior of $\mathcal{B}^{\sigma}(Y)$.

There is a Chern-Simons-Dirac functional $\mathcal{L}: C(Y) \rightarrow \mathbb{R}$ (see [19, Definition 4.1.1] for the precise formula). Roughly speaking, the monopole Floer homology is modeled on an infinite dimensional Morse homology for $\mathcal{L}$. To achieve transversality, one needs to add a generic, gauge invariant perturbation function $f: \mathcal{C}(Y) \rightarrow \mathbb{R}$. Let $\mathfrak{q}$ be the formal gradient of $f$. Then $\mathfrak{q}$ has two components $\left(\mathfrak{q}^{1}, \mathfrak{q}^{2}\right)$, where $\mathfrak{q}^{1}$ is the connection component and $\mathfrak{q}^{2}$ is the spinor component.

The gradient of the perturbed functional
$$\mathcal{L}_{\mathfrak{q}}:=\mathcal{L}+f: \mathcal{C}(Y) \rightarrow \mathbb{R}$$
is invariant under $\mathcal{G}$ and hence induces a vector field $v_{\mathfrak{q}}^{\sigma}$ on $\mathcal{B}^{\sigma}(Y)$. (More precisely, $v_{\mathfrak{q}}^{\sigma}$ is a section of the $L_{k-3 / 2}^{2}$-completion of the tangent bundle $T \mathcal{B}^{\sigma}(Y)$.)

The vector field $v_{\mathfrak{q}}^{\sigma}$ has finitely many critical points. Furthermore, there are two types of reducible critical points: the boundary stable ones and the boundary unstable ones. To recall their difference, we note that a reducible point $(B, 0) \in C(Y)$ is a critical point of $\mathcal{L}_{\mathfrak{q}}$ if and only if $B$ satisfies the perturbed curvature equation
$$* F_{B^{t}}=\mathfrak{q}^{1}(B, 0),$$
where $B^{t}$ denotes the induced connection on determinant bundle $\bigwedge^{2} S_{Y}$. We consider the perturbed Dirac operator
$$\not D_{B, \mathfrak{q}}: L_{k}^{2}\left(S_{Y}\right) \rightarrow L_{k-1}^{2}\left(S_{Y}\right),$$
defined by
$$\not D_{B, \mathfrak{q}}(\psi)=\not D_{B} \phi+\mathcal{D}_{(B, 0)} \mathfrak{q}^{1}(0, \psi),$$
where the last term denotes the derivative of $\mathfrak{q}^{1}$ at ( $B, 0$ ) in the direction ( $0, \psi$ ). This is a self-adjoint elliptic operator. Part of the transversality assumption requires that the eigenvalues of $\not D_{B, \mathfrak{q}}$ are all simple and nonzero. We arrange these eigenvalues as
$$\cdots \lambda_{-2}<\lambda_{-1}<0<\lambda_{0}<\lambda_{1}<\cdots .$$
Then each $\lambda_{i}$ corresponds to a reducible critical point $\left[\left(B, 0, \psi_{i}\right)\right]$ upstairs, where $\psi_{i}$ is a unit-length eigenvector for $\lambda_{i}$. We call the critical point $\left[\left(B, 0, \psi_{i}\right)\right]$ boundary stable (resp. boundary unstable) if $\lambda_{i}>0$ (resp. $\lambda_{i}<0$ ).

Let $\mathfrak{C}(Y)$ be the set of critical points in $\mathcal{B}^{\sigma}(Y)$. Then we have a decomposition
$$\mathfrak{C}(Y)=\mathfrak{C}^{o}(Y) \cup \mathfrak{C}^{\mathfrak{s}}(Y) \cup \mathfrak{C}^{\mathfrak{s}}(Y)$$
according to the three types: irreducible, boundary stable and boundary unstable. We will suppress $Y$ from our notations when it is clear from the context.