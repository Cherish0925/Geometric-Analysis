---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Seiberg-Witten invariants, orbifolds, and circle actions]

---
source_file: math_0107092.pdf
converter: mathpix
format: mmd
---

\title{
SEIBERG-WITTEN INVARIANTS, ORBIFOLDS, AND CIRCLE ACTIONS
}

\author{
SCOTT JEREMY BALDRIDGE
}

\begin{abstract}
The main result of this paper is a formula for calculating the Seiberg-Witten invariants of 4-manifolds with fixed-point free circle actions. This is done by showing under suitable conditions the existence of a diffeomorphism between the moduli space of the 4-manifold and the moduli space of the quotient 3-orbifold. Two corollaries include $b_{+}>14$-manifolds with fixed-point free circle actions are simple type and a new proof that $\mathcal{S} \mathcal{W}_{Y^{3} \times S^{1}}=\mathcal{S} \mathcal{W}_{Y^{3}}$. An infinite number of $b_{+}=1$ 4-manifolds where the Seiberg-Witten invariants are still diffeomorphism invariants are constructed and studied.
\end{abstract}

\section*{1. Introduction}

The main idea of this work is to systematically study 4-manifolds that admit an $S^{1}$-action and classify them using Seiberg-Witten gauge theory. When the action on $X^{4}$ is free, the quotient by the $S^{1}$-action is a smooth 3-manifold $Y$ and the manifold with given circle action is classified by the Euler class $\chi \in H^{2}(Y ; \mathbb{Z})$. When the circle action is not free there will be non-trivial isotropy groups, which forces the orbit space to be an orbifold rather than a manifold. The main result of this paper is a formula for calculating the Seiberg-Witten invariants of any 4-manifold with a fixed point free circle action. We derive the formula by proving the existence of a diffeomorphism between the moduli space of the 4-manifold with the moduli space of the quotient 3-orbifold.

A given manifold may admit more than one circle action. So while the 3-manifold and Euler class are fully sufficient to classify a free circle action, the Seiberg-Witten invariants are stronger in that they are invariant of the underlying space up to diffeomorphism regardless of the circle action.

The first theorem we prove puts a restriction on the set of Spin ${ }^{c}$ structures with nontrivial Seiberg-Witten invariants for manifolds which admit a fixed point free circle action. (See sections 2 and 3 for descriptions of Spin ${ }^{c}$ structures and Seiberg-Witten invariants.)

Theorem A. Let $\xi$ be a $\operatorname{Spin}^{c}$ structure on $b_{+} \neq 1$ 4-manifold $X$ with a fixed point free circle action such that $S W_{X}(\xi) \neq 0$. Then the $\operatorname{Spin}^{c}$ structure $\xi$ is pulled back from a $\operatorname{Spin}^{c}$ structure on $Y$.

See subsection 4.1 for the statement when $b_{+}(X)=1$. This theorem is already enough to imply that $X$ is SW simple type - that the expected dimension of the moduli space for all Spin ${ }^{c}$ structures with nontrivial invariants is zero.

Let $\pi: X \rightarrow Y$ be the projection map from a smooth 4-manifold with a fixed point free circle action to its quotient orbifold. The manifold $X$ can be thought of as a orbifold circle bundle over $Y$. If $\mathbf{i} \eta$ is the connection 1-form of the circle bundle and $g_{Y}$ is any orbifold metric, we can form the metric $g_{X}=\eta \otimes \eta+\pi^{*}\left(g_{Y}\right)$ on $X$. After perturbing the Seiberg-Witten equations on $Y$ by a closed orbifold 2-form $\delta$ and on $X$ by its self-dual pullback $\pi^{*}(\delta)^{+}=\frac{1}{2}(1+\star) \pi^{*}(\delta)$, there is a moduli space of irreducible solutions to the Seiberg-Witten equations $\mathcal{M}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$ associated with $X$ and $\mathcal{M}^{*}\left(Y, g_{Y}, \delta\right)$ associated with $Y$ (see subsections 2.4 and 3.3 for definitions). Let $\mathcal{N}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$be the subcomponent of $\mathcal{M}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$which are the $\operatorname{Spin}^{c}$ structures

\footnotetext{
Date: 2001.
}
that are pulled back from $Y$. Theorem A tells us that these are the only $\operatorname{Spin}^{c}$ structures that are useful to study. We can now state the main theorem of this paper:

Theorem B. The pullback map $\pi^{*}$ induces a homeomorphism
$$\pi^{*}: \mathcal{M}^{*}\left(Y, g_{Y}, \delta\right) \rightarrow \mathcal{N}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right) .$$
Furthermore, if either of the two moduli spaces is a smooth manifold, then both of them are smooth, and $\pi^{*}$ is a diffeomorphism.

The approach to the proof of Theorem B was inspired by similar work done in [MOY].
As in the free case, a manifold with a fixed point free $S^{1}$-action can still be considered as a unit circle bundle, but now it is a unit circle bundle of an orbifold line bundle over a 3-orbifold. In this setup, $H^{2}(Y ; \mathbb{Z})$ is replaced by a group called $\operatorname{Pic}^{t}(Y)$ which records local data around the singular set (see subsection 2.2). Our main results express the Seiberg-Witten invariants of $X$ in terms of the Seiberg-Witten invariants of the orbifold $Y$ and the orbifold Euler class $\chi$ :

Theorem C. Let $X$ be a closed smooth 4-manifold with $b_{+}>1$ and a fixed point free circle action. Let $Y^{3}$ be the orbifold quotient space and suppose that $\chi \in \operatorname{Pic}^{t}(Y)$ is the orbifold Euler class of the circle action. If $\xi$ is a $\operatorname{Spin}^{c}$ structure over $X$ with $S W_{X}^{4}(\xi) \neq 0$, then $\xi=\pi^{*}\left(\xi_{0}\right)$ for some $\operatorname{Spin}^{c}$ structure on $Y$ and
$$S W_{X}^{4}(\xi)=\sum_{\xi^{\prime} \equiv \xi_{0} \bmod \chi} S W_{Y}^{3}\left(\xi^{\prime}\right),$$
where $\xi^{\prime}-\xi_{0}$ is a well-defined element of $\operatorname{Pic}^{t}(Y)$. When $b_{+}=1$, the formula holds for all $\operatorname{Spin}^{c}$ structures pulled back from $Y$.

This results produces two immediate corollaries. One is a corresponding formula for manifolds with free circle actions. This corollary is useful for calculating examples. The second corollary is a proof of the well known fact that the Seiberg-Witten invariants of $Y^{3} \times S^{1}$ are the same as the Seiberg-Witten invariants of $Y^{3}$.

Theorem C, together with the conjectured formula when $X$ contains fixed points (see section 8), would completely calculate the Seiberg-Witten invariants for all $b_{+}>14$-manifolds with circle actions. These calculations are useful beyond just distinguishing manifolds. When Seiberg-Witten invariants are combined with C. Taubes's results on symplectic manifolds (c.f. [T]), the formulas become an easy and powerful way of calculating an obstruction for an $S^{1}$-manifold to admit a symplectic structure.

We use Theorem B to study the moduli spaces in the case when $b_{+}(X)=1$. Normally when $b_{+}(X)=1$, the Seiberg-Witten invariant depends on the "chamber" of the metric used to calculate it. A theorem of T. J. Li and A. Liu [LL] shows how the numerical invariant changes when the metric moves from one chamber into another. Under certain conditions, their theorem says that the invariant does not change (making it a diffeomorphism invariant again). We show how to construct an infinite number of $b_{+}=1$ manifolds with this property. Theorem B provides a way to see explicitly why the invariants do not change when a chamber wall is crossed.

Acknowledgements: I am deeply grateful to Ronald Fintushel for introducing me to this field and for his constant encouragement. I would also like to thank Thomas H. Parker and Peter Ozsváth for their many helpful discussions.

\section*{2. Seiberg-Witten on 3-orbifolds}

We show that all of the usual notions of gauge theory hold for 3-dimensional real orbifolds. Throughout, we assume that all orbifolds are oriented, connected, and closed unless otherwise specified. We start with the definition of orbifolds (c.f. [S]).
\begin{itemize}
\item[2.1.] Definitions. An $n$-dimensional orbifold $Y$ is a Hausdorff space $|Y|$ together with a system $\Xi=\left(\left\{U_{i}\right\},\left\{\varphi_{i}\right\},\left\{\tilde{U}_{i}\right\},\left\{G_{i}\right\},\left\{\tilde{\varphi}_{i j}\right\}\right)$ which satisfies
\begin{itemize}
\item[1.] $\left\{U_{i}\right\}$ is locally finite.
\item[2.] $\left\{U_{i}\right\}$ is closed under finite intersections.
\item[3.] For each $U_{i}$, there exist a finite group $G_{i}$ acting smoothly and effectively on a connected open subset $\tilde{U}_{i}$ of $\mathbb{R}^{n}$ and a homeomorphism $\varphi_{i}: \tilde{U}_{i} / G_{i} \rightarrow U_{i}$.
\item[4.] If $U_{i} \subset U_{j}$, there exist a monomorphism $f_{i j}: G_{i} \rightarrow G_{j}$ and a smooth embedding $\tilde{\varphi}_{i j}: \tilde{U}_{i} \rightarrow$ $\tilde{U}_{j}$ such that for all $g \in G_{i}, x \in \tilde{U}_{i}, \tilde{\varphi}_{i j}(g \cdot x)=f_{i j}(g) \cdot \tilde{\varphi}_{i j}(x)$ making the following diagram commute:
\end{itemize}
\end{itemize}
![](https://cdn.mathpix.com/cropped/393dcbc9-6054-4dbd-8d6d-fcd127ef622c-03.jpg?height=368&width=318&top_left_y=878&top_left_x=882)
where $\varphi_{i j}$ are induced by the monomorphisms and the $r_{i}$ 's are the natural projections.
The system $\Xi$ is called an atlas and each $\varphi_{i} \circ r_{i}: \tilde{U}_{i} \rightarrow U_{i}$ is called a local chart. An orbifold $Y$ is connected and closed if the underlying space $|Y|$ is. Two atlases give the same orbifold structure if there is a common refinement.

Let $x \in|Y|$ and $\tilde{U}_{x} \rightarrow U$ be a local chart containing $x$. The local group at $x$, denoted $G_{x}$, is the isotropy group of $G$ of any point in $U$ corresponding to $x$ (well-defined up to isomorphism). Set $\Sigma Y=\left\{x \in|Y| \mid G_{x} \neq 1\right\}$. This set is closed and nowhere dense, and in fact it is easily shown that $\operatorname{dim} \Sigma Y \leq n-2$. After removing the singular set, $Y \backslash \Sigma Y$ becomes a manifold.

All theorems henceforth will be stated and proved for 3-dimensional orbifolds $Y$ where $\Sigma Y$ is a finite disjoint set of smooth closed curves $l_{1}, \ldots, l_{n}$ that are assigned integral multiplicities $\alpha_{1}, \ldots, \alpha_{n}$ given by their local isotropy group $\mathbb{Z}_{\alpha_{i}}=\mathbb{Z} / \alpha_{i} \mathbb{Z}$. Let $D$ be the standard complex disk and consider a $\mathbb{Z}_{\alpha_{i}}$ action on it by rotation. We will take a convenient atlas in all of the atlases which give the same orbifold structure. Equip $|Y|$ with an atlas of coordinate charts
$$\begin{array}{rc}
\phi_{i}:\left(S^{1} \times D, S^{1} \times 0\right) \rightarrow\left(U_{i}, l_{i}\right) & i=1, \ldots, n \\
\phi_{x}: D_{x}^{3} \rightarrow U_{x} & x \in Y \backslash\left\{l_{1}, \ldots, l_{n}\right\},
\end{array}$$
where the $\phi_{i}$ induce homeomorphisms from $\left(S^{1} \times D / \mathbb{Z}_{\alpha_{i}}, S^{1} \times 0\right)$ to $\left(U_{i}, l_{i}\right)$, the $\phi_{x}$ are homeomorphisms, the $U_{i}$ are all pairwise disjoint, $U_{x} \cap \Sigma Y=\emptyset$, and the transition functions are all diffeomorphisms.
Example 1. The triple $Y=\left(S^{3}, K, n\right)$ where $K$ is a knot in $S^{3}, K$ is the singular locus $\Sigma Y=K$, and the isotropy group around $K$ is $\mathbb{Z}_{n}$, is an example of a 3-orbifold.

Define an $n$-dimensional orbifold bundle over $Y$ in the following manner. Set $U_{x} \times V^{n}$ over each $U_{x}$ for an $n$-dimensional vector space $V^{n}$. Over $U_{i}$ the vector bundle is given by the quotient
$\left(S^{1} \times D \times V^{n}\right) / \mathbb{Z}_{\alpha_{i}}$ where $\left(S^{1} \times D \times V^{n}\right)$ is a $\mathbb{Z}_{\alpha_{i}}$-equivariant vector bundle specified up to isometry by giving a representation $\sigma_{i}: \mathbb{Z}_{\alpha_{i}} \rightarrow G L_{n}(V)$. The vector bundle over $Y$ is then specified by a 1-cocycle of transition functions over the overlaps.
2.2. Orbifold line bundles. Under tensor product the topological isomorphism classes of orbifold line bundles form a group $\operatorname{Pic}^{t}(Y)$ called the topological Picard group. We describe this group in this subsection.

We can record the information in $\operatorname{Pic}^{t}(Y)$ by using a generalization of equivariant cohomology. Think of $Y$ as the union of $Y \backslash\left\{l_{1}, \ldots, l_{n}\right\}$ and $\amalg\left(l_{i} \times D / \mathbb{Z}_{\alpha_{i}}\right)$. Define $Y_{V}$ to be the union of $Y \backslash\left\{l_{1}, \ldots, l_{n}\right\}$ and $\amalg\left(l_{i} \times\left(D \times_{\mathbb{Z}_{\alpha_{i}}} E \mathbb{Z}_{\alpha_{i}}\right)\right)$ glued using sections of $l_{i} \times\left(D \backslash\{0\} \times_{\mathbb{Z}_{\alpha_{i}}} E \mathbb{Z}_{\alpha_{i}}\right) \rightarrow$ $U_{i} \backslash l_{i}$. These sections are unique up to homotopy because the fibers of the bundle are contractible.

The following theorem is contained in [FuS].
Theorem 2. The following groups are isomorphic:
\begin{itemize}
\item[1.] $H^{1}\left(Y_{V} ; \mathbb{Z}\right) \cong H^{1}(|Y| ; \mathbb{Z})$,
\item[2.] $H^{2}\left(Y_{V} ; \mathbb{Z}\right) \cong \operatorname{Pic}^{t}(Y)$.
\end{itemize}

Remark 3. In the literature, the group $H_{V}^{*}(Y):=H^{*}\left(Y_{V}\right)$ is often called the $V$-cohomology ring of $Y$.

Here is another way to describe $\operatorname{Pic}^{t}(Y)$. For a fixed $i$, define an orbifold line bundle over $Y$ to be a trivial line bundle $A=\left(Y \backslash l_{i}\right) \times \mathbb{C}$ and over $U_{i}$ it is given by $B=\left(S^{1} \times D \times \mathbb{C}_{\xi}\right) / \mathbb{Z}_{\alpha_{i}}$ where $a \in \mathbb{Z}_{\alpha_{i}}$ acts using the standard representation
$$a \cdot(\gamma, w, z) \mapsto\left(\gamma, \mathbf{e}^{\frac{2 \pi \mathrm{i} a}{\alpha_{i}}} w, \mathbf{e}^{\frac{2 \pi \mathrm{i} a}{\alpha_{i}}} z\right) .$$
The bundle is glued together using a transition function $\varphi_{B A}(\gamma, w)=w$ on the overlap $S^{1} \times(D \backslash$ $\{0\}$ ). For each $l_{i}$, create such a line bundle called $E_{i}$.

Let $L$ be an orbifold line bundle over $Y$. There is a collection of integers $\beta_{1}, \ldots \beta_{n}$ satisfying
$$0 \leq \beta_{i}<\alpha_{i}$$
such that the bundle $L \otimes E_{1}^{-\beta_{1}} \otimes \cdots \otimes E_{n}^{-\beta_{n}}$ is a trivial orbifold line bundle over each neighborhood of the $l_{i}$ 's. By forgetting the orbifold structure, it can be naturally identified with a smooth line bundle (denoted by $|L|$ ) over the smooth manifold $|Y|$.

Theorem 4. The isomorphism classes of orbifold line bundles on $Y$ with specified isotropy representations $\xi_{1}^{\beta_{1}}, \ldots, \xi_{n}^{\beta_{n}}$ along $l_{1}, \ldots, l_{n}$ respectively are in bijective correspondence with $\chi \in$ $H^{2}(|Y| ; \mathbb{Z})$.

The proof below generalizes [F2] to the case of an arbitrary orbifold line bundle.
Proof. Given $L \in \operatorname{Pic}^{t}(Y)$, we construct $L \otimes E_{1}^{-\beta_{1}} \otimes \cdots \otimes E_{n}^{-\beta_{n}}$ and its desingularization $|L|$ explicitly. Let $\pi: X \rightarrow Y$ be the unit circle bundle of $L$. Set $Q=\cup U_{i}$ in $Y$ and $P=\pi^{-1}(Q)$ with $P_{i}=\pi^{-1}\left(U_{i}\right)$. Then $X^{\prime}=X \backslash P$ is a principal $S^{1}$-bundle over $Y^{\prime}=Y \backslash Q$.

In general, the unit circle bundle $X$ is an orbifold rather than a manifold. $P_{i}$ is a quotient of $l_{i} \times D^{2} \times S^{1}$ by the action of $\mathbb{Z}_{\alpha}$ defined by $\xi:(\gamma, w, t) \mapsto\left(\gamma, \xi w, \xi^{\beta} t\right)$. It follows that the isotropy group of a point in the quotient of $l_{i} \times\{0\} \times S^{1}$ is $\left\{\xi \in \mathbb{Z}_{\alpha}: \xi^{\beta}=1\right\}$ for all points $p \in l$. When the isotropy group is trivial $(\operatorname{gcd}(\alpha, \beta)=1)$ the quotient is smooth. In the case that $\beta \equiv 0 \bmod _{\alpha}, L$ is a usual line bundle around that loop, but the 4-manifold still has a nontrivial orbifold structure. Set $d=g c d\left(\alpha_{i}, \beta_{i}\right)$.

Let $m_{i}=\partial(\{0\} \times D \times\{1\})$ be the meridian loop of $l_{i}$ before the quotient is taken. Denote the class it represents in the quotient $P_{i}$ by $\tilde{m}_{i}$. The homeomorphism $\varphi_{i}: \partial P_{i} \rightarrow \partial X^{\prime}$ determines a section $s: \partial Y^{\prime} \rightarrow \partial X_{0}$ which is specified up to homology by the relation:
$$\varphi_{*}\left[\tilde{m}_{i}\right]=\left(\frac{\alpha_{i}}{d}\right) s_{*}\left[m_{i}^{\prime}\right]+\left(\frac{\beta_{i}}{d}\right)\left[f^{\prime}\right],$$
where $m_{i}^{\prime}$ is the meridian of $l_{i}$ in $Y^{\prime}, f^{\prime}$ is a fiber of $\partial X^{\prime}$, and $0 \leq \beta_{i} \leq \alpha_{i}$. The local invariants $\left(\alpha_{i}, \beta_{i}\right)$ specify $P_{i}$ up to orientation-preserving equivariant homeomorphism.

The bundle $X^{\prime}$ can be extended to the unit circle bundle of $|L|$ by equivariantly attaching $l_{i} \times D \times S^{1}$ with a bundle isomorphism $\phi_{i}$. Bundle isomorphisms covering the identity are classified up to vertical equivariant isotopy by homotopy classes of maps in $\left[\partial\left(S^{1} \times D\right), S^{1}\right]=\mathbb{Z} \oplus \mathbb{Z}$. However we can change $\phi_{i}$ by a bundle automorphism classified by $\left[S^{1} \times D, S^{1}\right]=H^{1}\left(S^{1} \times D ; \mathbb{Z}\right)=\mathbb{Z}$; these maps change $\left(\phi_{i}\right)_{*}\left(\left[l_{i}\right]\right)$ by a multiple of the fiber. Therefore the resulting bundle $X^{\prime} \cup_{\phi_{i}}\left(l_{i} \times D \times S^{1}\right)$ can be completely specified by the map
$$\left(\phi_{i}\right)_{*}\left[m_{i}\right]=s_{*}\left[m^{\prime}\right]+r\left[f^{\prime}\right]$$
for some $r \in \mathbb{Z}$. Thus we determine the principal $S^{1}$ bundle of $|L|$ by specifying that $r=0$.
In summary:
\begin{itemize}
\item[1.] The unit circle bundle of $L$ is obtained by gluing the quotient $P$ using maps
$$\left(\varphi_{i}\right)_{*}\left[\tilde{m}_{i}\right]=\left(\frac{\alpha_{i}}{d}\right) s_{*}\left[m_{i}^{\prime}\right]+\left(\frac{\beta_{i}}{d}\right)\left[f^{\prime}\right] .$$
Note that this bundle depends only on the section $s_{*}\left[m_{i}^{\prime}\right]$ as well.
\item[2.] The unit circle bundle of $L \otimes E_{1}^{-\beta_{1}} \otimes \cdots \otimes E_{n}^{-\beta_{n}}$ is obtained by gluing in the quotient $\amalg_{i} l_{i} \times\left(D / \mathbb{Z}_{\alpha_{i}}\right) \times S^{1}$ into $X^{\prime}$ using maps $\left(\phi_{i}\right)_{*}\left[\tilde{m}_{i}\right]=s_{*}\left[m_{i}^{\prime}\right]$.
\item[3.] The unit circle bundle of the desingularization $|L|$ is obtained by gluing in $\amalg_{i} l_{i} \times D \times S^{1}$ using maps $\left(\phi_{i}\right)_{*}\left[m_{i}\right]=s_{*}\left[m_{i}^{\prime}\right]$.
\end{itemize}

Next we show that two orbifold line bundles $L_{1}$ and $L_{2}$ with the same isotropy representations and equivalent desingularizations $\left|L_{1}\right|=\left|L_{2}\right|$ are equivalent as orbifold line bundles.

Construct two principal $S^{1}$-bundles $X_{1}$ and $X_{2}$ from $X^{\prime}$ to form unit circle bundles $\left|L_{1}\right|$ and $\left|L_{2}\right|$. The construction depends on choices of the class $\sum_{i=1}^{n}\left(s_{j}\right)_{*}\left[m_{i}^{\prime}\right] \in H_{1}\left(\partial X^{\prime} ; \mathbb{Z}\right)$ coming from sections $s_{j}: \partial Y^{\prime} \rightarrow \partial X_{j}^{\prime}$ for $j=1,2$. Let $\theta_{j} \in H^{2}\left(Y^{\prime}, \partial Y^{\prime}\right)$ be the obstruction to extending these sections over $X_{j}^{\prime}$. Let $\tau \in H^{1}\left(\partial Y^{\prime}\right)$ be the primary difference of $s_{1}$ and $s_{2}$. A diagram chase
![](https://cdn.mathpix.com/cropped/393dcbc9-6054-4dbd-8d6d-fcd127ef622c-05.jpg?height=365&width=982&top_left_y=1822&top_left_x=552)
shows that $j_{1}^{*} \lambda^{-1} \delta_{2}(\tau)=j_{1}^{*} \lambda^{-1}\left(\theta_{1}-\theta_{2}\right)=c_{1}\left(\left|L_{1}\right|\right)-c_{1}\left(\left|L_{2}\right|\right)=0$. Thus there is an element $\tau^{\prime} \in H^{1}\left(\amalg_{i} l_{i} \times D\right)$ such that $\delta_{1} \tau^{\prime}=\lambda^{-1} \delta_{2} \tau$, and $\delta_{3}\left(\tau-i^{*} \tau^{\prime}\right)=0$. Therefore $\tau \in i^{*}\left(H^{1}\left(\amalg_{i} l_{i} \times D ; \mathbb{Z}\right)\right)$ implying that $\left(s_{1}\right)_{*}\left[m_{i}^{\prime}\right]$ is homotopic to $\left(s_{2}\right)_{*}\left[m_{i}^{\prime}\right]$ through a homotopy in $l_{i} \times D$. Since the construction of the unit circle bundle of the orbifold line bundle in (1) depended only on these sections, $L_{1}$ and $L_{2}$ are equivalent. \(\square\)

The above theorem means that a given orbifold line bundle $L$ over $Y$ is specified by the data
$$\left(c_{1}(|L|), \beta_{1}, \ldots, \beta_{n}\right)$$
called the Seifert invariant of $L$ over $Y$. (This data, of course, is not unique).
2.3. Spin ${ }^{c}$ Structures on 3-orbifolds. The Spin ${ }^{c}$ structures on a 3-orbifold $Y$ are defined by a pair $\xi=(W, \rho)$ consisting of a rank 2 complex orbifold bundle $W$ with a hermitian metric (the spinor bundle) and an action $\rho$ of orbifold 1-forms on spinors,
$$\rho: T^{*} Y \rightarrow \operatorname{End}(W),$$
which satisfies the property that, if $e^{1}, e^{2}, e^{3}$ are an orthonormal coframe at a point in $Y$, then the endomorphisms $\rho\left(e^{i}\right)$ are skew-adjoint and satisfy the Clifford relations
$$\rho\left(e^{i}\right) \rho\left(e^{j}\right)+\rho\left(e^{j}\right) \rho\left(e^{i}\right)=-2 \delta_{i j} .$$
We also require that the volume form $e^{1} \wedge e^{2} \wedge e^{3}$ acts by
$$\rho\left(e^{1} \wedge e^{2} \wedge e^{3}\right)=-\mathbf{I} \mathbf{d}_{W} .$$
We will write $c_{1}(\xi)$ for the first Chern class of $\operatorname{det} W$.
Theorem 5. The tangent bundle $T^{*} Y$ of an orbifold always lifts to an orbifold $\operatorname{Spin}^{c}(3)$-bundle.

Proof. If we can split $T Y$ into a 1-dimensional real line bundle and a complex orbifold line bundle $L$, then $w_{2}(T Y)=w_{2}(\mathbb{R} \oplus L)=w_{2}(L)$ is just the mod 2 reduction of $c_{1}(L)$ for some orbifold line bundle $L$. Hence $T Y$ lifts.

We need to find a nowhere zero section of $T Y$. Note that each $l_{i} \times D / \mathbb{Z}_{\alpha_{i}}$ comes with an $\mathbb{Z}_{\alpha_{i}}$-invariant oriented nonzero vector field that is tangent to $l_{i}$ at each point in $D / \mathbb{Z}$. This vector field induces a nonzero section $s:\left.\partial Y^{\prime} \rightarrow T Y\right|_{\partial}$. Remove an extra $S^{1} \times D$ from the interior of $Y^{\prime}$ and put a similar nonzero section on the boundary. The obstruction to extending the section into the interior of
$$Y^{\prime \prime}=Y \backslash\left(\left(S^{1} \times D\right) \cup \amalg_{i} l_{i} \times D / \mathbb{Z}_{\alpha_{i}}\right)$$
is an element of $H^{3}\left(Y^{\prime \prime}, \partial Y^{\prime \prime} ; \pi_{2}\left(S^{2}\right)\right)=\mathbb{Z}$. Using the homology relation
$$\left[\partial\left(S^{1} \times D\right)\right]=-\sum_{i}\left[\partial\left(l_{i} \times D / \mathbb{Z}_{\alpha_{i}}\right)\right],$$
the obstruction can be removed by changing the framing on the boundary of $S^{1} \times D$. Thus $T Y$ admits a nowhere zero vector field. \(\square\)

Remark 6. In [S], I. Satake treated the V-Euler class as the index of a unit vector field on $T Y$ with singularities and showed that $\chi_{V}(Y)=0$ for odd dimensional orbifolds. Thus it is not surprising that nonzero vector fields exists on 3-orbifolds.

Theorem 7. The set of $\operatorname{Spin}^{c}$ structures lifting the frame bundle of a 3-orbifold $Y$ is a principal homogeneous space over $\operatorname{Pic}^{t}(Y)$ : The difference of two $\operatorname{Spin}^{c}$ structures $\xi_{1}, \xi_{2}$ is an orbifold line bundle.

Proof. Let $\xi_{1}$ and $\xi_{2}$ be two Spin ${ }^{c}$ structures which are lifts of the frame bundle. Away from the $l_{i}$ 's, the difference of two Spin ${ }^{c}$ structures is a complex line bundle as in the smooth case. Because
$$\left(c_{1}\left(\xi_{1}\right)-c_{1}\left(\xi_{2}\right)\right)\left[\partial\left(l_{i} \times D / \mathbb{Z}_{\alpha_{i}}\right)\right]=0$$
for all $l_{i}$, we can extend the complex line bundle over the desingularization $|Y|$ using techniques in Theorem 4. Thus we can investigate locally to show that any two lifts of isotropy representations
into $\operatorname{Spin}^{c}(3)$ differ by a representation into $S^{1}$. Note that this is not immediately obvious because there are many different representations of $\mathbb{Z}_{\alpha}$ into $\operatorname{Spin}^{c}(3)=U(2)$.

Let $\Theta_{i}$ be the unit vector field on $l_{i} \times D / \mathbb{Z}_{\alpha}$ which is tangent to the circle $l_{i}$ at each point. We use the fact that $\rho: \mathbb{Z}_{\alpha} \rightarrow S O(3)$ is a rotation which leaves the nonzero vector field $\Theta_{i}$ invariant. Identify $S U(2)$ with the unit quaternions. The map $A d: S U(2) \rightarrow S O(3)$ is given by
$$g \mapsto g h \bar{g}$$
for all $h \in \mathrm{Im} \mathbb{H}$ and is the double cover of $\operatorname{SO}(3)$. Thus $\operatorname{SO}(3)$ can be thought of as the unit quaternions modulo the equivalence $h \sim-h$. Without loss of generality, we may assume that the invariant vector field $\Theta_{i}$ is generated by $\mathbf{i} \in \operatorname{Im} \mathbb{H}$ at each point in $l_{i}$.

It is easy to see that elements of $\operatorname{SO}(3)$ which rotate the second two components while leaving i invariant are of the form $e^{\mathbf{i} \theta} \in \mathbb{H}$. Hence $\rho(1)=\lambda^{\tau}$ where $\lambda$ is a $2 \alpha$-root of unity in $\mathbb{C}$ and $0 \leq \tau<\alpha$.

The Spin ${ }^{c}$ representation $\sigma:$ Spin $^{c} \rightarrow \operatorname{End}(\mathbb{H})$ is given by $\sigma\left(g, e^{i \theta}\right) h=g h e^{i \theta}$ for all $h \in \mathbb{H}$. Here we have used the fact $\operatorname{Spin}^{c}(3)=S U(2) \times S^{1} /(-1,-1)$. Using this identification, Spin ${ }^{c}$ projects to $\operatorname{SO}(3)$ by the adjoint map as well,
$$\left(g, e^{i \theta}\right) \mapsto g h \bar{g}$$
for all $h \in \operatorname{Im} \mathbb{H}$. Thus the representation $\rho$ lifts to $\tilde{\rho}$ :
![](https://cdn.mathpix.com/cropped/393dcbc9-6054-4dbd-8d6d-fcd127ef622c-07.jpg?height=338&width=265&top_left_y=1084&top_left_x=909)
given by $\tilde{\rho}(1)=\left(\lambda^{\tau}, \hat{\rho}(1)\right)$ (or equivalently $\left(-\lambda^{\tau},-\hat{\rho}(1)\right)$ ) for some representation $\hat{\rho}: \mathbb{Z}_{\alpha} \rightarrow S^{1}$. The representation $\hat{\rho}$ is given by $\hat{\rho}(1)=\lambda^{\kappa}$ for some $0 \leq \kappa<\alpha$. Hence the difference of two $\operatorname{Spin}^{c}$ structures $\xi_{1}-\xi_{2}$ locally is a representation $\left(\hat{\rho}_{1}-\hat{\rho}_{2}\right): \mathbb{Z}_{\alpha_{i}} \rightarrow S^{1}$.

Globally, $\xi_{1}-\xi_{2}$ differs by a complex line bundle over $|Y|$ and local isotropy representations into $S^{1}$, i.e., an element in $\operatorname{Pic}^{t}(Y)$ as described in Theorem 4. \(\square\)
2.4. Seiberg-Witten Equations on 3-orbifolds. Fix an orbifold $S O(3)$-connection ∇ on the cotangent bundle $T^{*} Y$ and a $\operatorname{Spin}^{c}$ structure $\xi=(W, \rho)$.

Definition 8. A Hermitian connection ∇ on $W$ is called spinorial with respect to $\nabla$ if it is compatible with Clifford multiplication, i.e.,
$$\boldsymbol{\nabla}(\rho(v) \psi)=\rho(\nabla v) \psi+\rho(v)(\boldsymbol{\nabla} \psi) .$$
The set of all spinorial connections will be denoted by $\mathcal{A}(W)$.
Given a trivialization for $W$, the connection matrix of any $\nabla$-spinorial connection ∇ can be written with respect to this trivialization as
$$\frac{1}{4} \sum \omega_{j}^{i} \otimes \rho\left(e^{i} \wedge e^{j}\right)+b \mathbf{I} \mathbf{d}_{W}$$
where $\omega_{j}^{i}$ are the connection matrices for $\nabla$, and $b \in \Omega^{1}(Y, \mathbf{i} \mathbb{R})$ is an orbifold 1-form. We will often think of spinorial connections on a $\operatorname{Spin}^{c}$ structure as $U(1)$ connections on $\operatorname{det} W$ coupled with the Levi-Civita connection $\nabla_{Y}$ on $T^{*} Y$. A spinorial connection ∇ defines a Dirac operator $D_{A}: \Gamma(Y, W) \rightarrow \Gamma(Y, W)$ on the space of orbifold sections of $W$ which is self-adjoint. The
perturbed Seiberg-Witten equations are the following pair of equations for $(A, \Psi)$ where $A$ is a U(1) orbifold connection on $\operatorname{det} W$ and $\Psi$ is an orbifold section of $W$ :
$$\begin{aligned}
F_{A}+\delta-\star \tau(\Psi) & =0 \\
D_{A}(\Psi) & =0 .
\end{aligned}$$
Here $\tau: \Gamma(Y, W) \rightarrow \Omega^{1}(Y ; \mathbf{i} \mathbb{R})$ is the adjoint to Clifford multiplication, defined by
$$\langle\rho(b) \Psi, \Psi\rangle_{W}=2\langle b, \tau(\Psi)\rangle_{\Lambda^{1}},$$
for all orbifold 1-forms $b \in \Omega^{2}(Y ; \mathbf{i} \mathbb{R})$ and all $\Psi \in \Gamma(Y, W)$. The $\delta \in \Omega^{2}(Y ; \mathbf{i} \mathbb{R})$ is a closed orbifold 2-form used to perturb the equations.

For a fixed metric $g_{Y}$ and perturbation term $\delta$, the moduli space $\mathcal{M}\left(Y, \xi, g_{Y}, \delta\right)$ is the space of solutions to (2) modulo the action of the gauge group $\mathcal{G}=\operatorname{Map}\left(Y, S^{1}\right)$. Let $\mathcal{M}^{*}\left(Y, \xi, g_{Y}, \delta\right)$ denote the set of irreducible solutions (i.e., where $\Psi \not \equiv 0$ ). For a generic perturbation, the moduli space is a compact, smooth manifold containing no reducible solutions. In that case, the fundamental class $\left[\mathcal{M}\left(Y, \xi, g_{Y}, \delta\right)\right]$ is essentially the Seiberg-Witten invariant. Evaluating it against some universal classes defines a map $S W^{3}(\xi) \in \mathbb{Z}$ which is independent of the Riemannian metric and perturbation when $b_{1}(Y)>1$ (c.f., [M]). Denote the union over all distinct Spin ${ }^{c}$ structures by $\mathcal{M}\left(Y, g_{Y}, \delta\right)$.

\section*{3. 4-Manifolds with fixed point free circle actions}

In this section we study manifolds with fixed point free circle actions. We describe the cohomology of these manifolds and show that under some circumstances, line bundles with connections can be pushed forward to orbifold line bundles with connection on the quotient. Finally, we describe how to pullback Spin ${ }^{c}$ structures from Spin ${ }^{c}$ structures on the quotient.
3.1. Homology. A 4-manifold with fixed point free $S^{1}$-action can be viewed as the boundary of a disk bundle or the unit circle bundle of an orbifold line bundle $L$ over a 3-orbifold $Y$. Henceforth, we will assume that $X$ is a unit circle orbifold line bundle $L$ over $Y$ where each local invariant $\beta_{i}$ is relatively prime to $\alpha_{i}$. Denote $\pi: X \rightarrow Y$ for the projection map.

When $X$ is smooth, then $X_{V} \rightarrow Y_{V}$ is an honest $S^{1}$-bundle and we have the Gysin sequence:
![](https://cdn.mathpix.com/cropped/393dcbc9-6054-4dbd-8d6d-fcd127ef622c-08.jpg?height=203&width=956&top_left_y=1726&top_left_x=563)
![](https://cdn.mathpix.com/cropped/393dcbc9-6054-4dbd-8d6d-fcd127ef622c-08.jpg?height=349&width=710&top_left_y=2023&top_left_x=581)

Theorem 9. If $X$ is a 4-manifold with a fixed-point free circle action over $Y$ given by the sphere bundle of a line bundle $L$ over $Y$, then
$$\begin{aligned}
H^{1}(X, \mathbb{Z}) & \cong\left\{\begin{aligned}
H^{1}(|Y| ; \mathbb{Z}), & {[L] \text { is not torsion } } \\
H^{1}(|Y|, \mathbb{Z}) \oplus \mathbb{Z}, & {[L] \text { is torsion } }
\end{aligned}\right. \\
H^{2}(X ; \mathbb{Z}) & \cong\left(\operatorname{Pic}^{t}(Y) /<[L]>\right) \oplus \operatorname{ker}(\cdot \cup[L]): H^{1}(|Y| ; \mathbb{Z}) \rightarrow H_{V}^{3}(Y ; \mathbb{Z}) .
\end{aligned}$$
In particular, since the kernel of $(\cdot \cup[L]): H^{1} \rightarrow H^{3}$ is torsion free, all torsion classes must come from pullbacks in $\pi^{*}\left(\operatorname{Pic}^{t}(Y)\right)$.

When $[L]$ is not torsion, the rank of $\operatorname{Pic}^{t}(Y) /<[L]>$ and $\operatorname{ker}(\cdot \cup[L])$ are both equal to $b_{1}(|Y|)-1$. A basis for the former space can be represented by the Poincaré duals of tori of the form $\pi^{-1}($ loop $)$ for smooth loops in $Y \backslash \Sigma Y$. A basis for the later space can be represented by surfaces in $X$ which, after integrating over the fiber, are the Poincaré duals of surfaces in $|Y|$. The simple intersection relationship between loops and surfaces in $|Y|$ implies that the intersection form $Q_{X}$ should be simple as well.

In fact, since the signature is zero (c.f. [HP]), the classification of intersection forms says that $Q_{X}$ is equivalent to the direct sum of matrices of the form (where $d$ an integer)
$$\left(\begin{array}{ll}
0 & 1 \\
1 & d
\end{array}\right)$$
with respect to a basis $\{A, B\}$ where $A \in \pi^{*}\left(\operatorname{Pic}^{t}(Y)\right)$ is a class pulled back from $Y$. Pulled back classes always have square zero by the naturality of the cup product and the fact that the product of 2-forms on $Y$ is always zero.
3.2. Line bundles over $X$. Orbifold line bundles $E$ over $Y$ pullback to usual line bundles $\pi^{*}(E)$ over $X$. Except for the case $X=|Y| \times S^{1}$, this is a many to one correspondence. Nonetheless, it can be made faithful in the following way. Given a line bundle $E$ with connection $A$ over $X$ with the following two properties:
\begin{itemize}
\item[1.] The curvature two form of $A$ pulls up from $Y$, i.e.,
$$\iota_{\mathrm{T}} F_{A}=0,$$
where T is the everywhere non-zero vector field generated by the circle action on $X$.
\item[2.] There exists a point $x \in Y \backslash \Sigma Y$ such that holonomy of $A$ around $\pi^{-1}(x)$ is trivial.
\end{itemize}
Then $(E, A)$ can be pushed forward to an orbifold line bundle with connection on $Y$ (up to gauge equivalence). If one such point $x \in Y \backslash \Sigma Y$ satisfies the second condition, then all points outside the critical set do. Such connections are said to have trivial fiberwise holonomy.

We state Proposition 5.1.3 from [MOY].
Proposition 10. There is a natural one-to-one correspondence between orbifold line bundles with connection over $Y$ and usual line bundles with connection over $X$, whose curvature forms pull up from $Y$ and whose fiberwise holonomy is trivial. Furthermore, this correspondence induces an identification between orbifold sections of the orbifold bundle over $Y$ with fiberwise constant sections of its pullback over $X$.

Pull back connections $\pi^{*} A$ are characterized by $\nabla_{\mathrm{T}}^{\pi^{*}}{ }_{\Psi}=0$ for all pulled back sections $\Psi$.
3.3. Seiberg-Witten Equations of Smooth 4-manifolds. A Spin ${ }^{c}$ structure $\xi=(W, \sigma)$ on an oriented 4-manifold $X$ is a hermitian vector bundle $W$ of rank 4, together with a Clifford multiplication $\sigma: T^{*} X \rightarrow \operatorname{End}(W)$. The bundle $W$ decomposes into two bundles of rank 2, $W^{+} \oplus W^{-}$, with $\operatorname{det} W^{+}=\operatorname{det} W^{-}$. The bundle $W^{-}$is the subspace annihilated by the action of self-dual 2-forms. We set $c_{1}(\xi)$ to be the first Chern class of $\operatorname{det} W^{+}$.

There is a natural way to pullback a $\operatorname{Spin}^{c}$ structure from $Y$ to $X$. Let $\mathbf{i} \eta$ denote the connection 1-form of the circle bundle $\pi: X \rightarrow Y$, and let $g_{Y}$ be a metric on $Y$, then endow $X$ with the metric $g_{X}=\eta \otimes \eta+\pi^{*}\left(g_{Y}\right)$. Using this metric, there is an orthogonal splitting
$$T^{*} X \cong \mathbb{R} \eta \oplus \pi^{*}\left(T^{*} Y\right) .$$

If $\xi=(W, \rho)$ is a $\operatorname{Spin}^{c}$ structure over $Y$, define the pullback of $\xi$ to be $\pi^{*}(\xi)=\left(\pi^{*}(W) \oplus\right.$ $\left.\pi^{*}(W), \sigma\right)$ where the action
$$\sigma: T^{*} X \rightarrow \operatorname{End}\left(\pi^{*}(W) \oplus \pi^{*}(W)\right)$$
is given by
$$\sigma\left(b \eta+\pi^{*}(a)\right)=\left(\begin{array}{cc}
0 & \pi^{*}(\rho(a))+b \mathbf{I} \mathbf{d}_{\pi^{*}(W)} \\
\pi^{*}(\rho(a))-b \mathbf{I} \mathbf{d}_{\pi^{*}(W)} & 0
\end{array}\right) .$$
This defines a $\operatorname{Spin}^{c}$ structure on $X$.
Choosing a $\operatorname{Spin}^{c}$ structure $\xi_{0}=\left(W_{0}, \rho\right)$ on $Y$ gives rise to a one-to-one correspondence between Hermitian orbifold line bundles and Spin ${ }^{c}$ structures on $Y$ via $E \mapsto W_{0} \otimes E$. Likewise, the pullback Spin ${ }^{c}$ structure $\xi=\pi^{*}\left(\xi_{0}\right)$ induces a one-to-one correspondence between Hermitian line bundles and Spin ${ }^{c}$ structures on $X$.

Remark 11. In this way we can think of a $\operatorname{Spin}^{c}$ structure with respect to $\xi_{0}$ or $\xi$ as a choice of line bundle on $Y$ or $X$ respectively. This allows us to push-forward a $\operatorname{Spin}^{c}$ structure with a trivial fiberwise connection on $\operatorname{det} W^{+}$from $X$ to $Y$ via Proposition 10.

There is a natural connection on $X$ which is compatible with the reduction $T^{*} X=\mathbb{R} \eta \oplus$ $\pi^{*}\left(T^{*} Y\right)$. Let $\nabla^{Y}$ denote the Levi-Civita connection on $Y$ and set $\nabla=d \oplus \pi^{*}\left(\nabla^{Y}\right)$. This is a compatible connection which satisfies
$$\nabla \eta=0, \quad \text { and } \quad \nabla\left(\pi^{*}(\beta)\right)=\pi^{*}\left(\nabla^{Y} \beta\right) .$$

It is more convenient to use this reducible $S O(4)$-connection instead of the Levi-Civita connection. By coupling it with a $U(1)$-connection $A$ on $\operatorname{det} W^{+}$we can define a spinorial connection on $W^{+}$. Define a Dirac operator $\not D_{A}^{+}: \Gamma_{X}\left(W^{+}\right) \rightarrow \Gamma_{X}\left(W^{-}\right)$from the space of smooth sections of $W^{+}$to $W^{-}$. The 4-dimensional perturbed Seiberg-Witten equations for a section $\Psi \in \Gamma_{X}\left(W^{+}\right)$ and a $U(1)$-connection $A$ on $\operatorname{det} W^{+}$are:
$$\begin{aligned}
F_{A}^{+}+\delta-q(\Psi) & =0, \\
\not D_{A}^{+}(\Psi) & =0 .
\end{aligned}$$
Here $F_{A}^{+}$is the projection of the curvature onto the self-dual two forms, $\delta \in \Omega^{+}(X ; \mathbf{i} \mathbb{R})$ is selfdual 2-form used to perturb the equations, and $q: \Gamma_{X}\left(W^{+}\right) \rightarrow \Omega^{+}(X, \mathbf{i} \mathbb{R})$ defined by $q(\Psi)=$ $\Psi \otimes \Psi^{*}-\frac{1}{2}|\Psi|^{2}$ is the adjoint of Clifford multiplication by self-dual 2-forms,i.e,
$$\langle\sigma(\beta) \Psi, \Psi\rangle_{W^{+}}=4\langle\beta, q(\Psi)\rangle_{\mathbf{i}^{+}}$$
for all self-dual 2-forms $\beta \in \Omega^{+}(X ; \mathbf{i} \mathbb{R})$ and all sections $\Psi$.
Similar to the 3-dimensional case, the moduli space $\mathcal{M}\left(X, \xi, g_{X}, \delta\right)$ is the space of solutions $(A, \Psi)$ modulo the action of the gauge group. We are using a reducible connection ∇ instead of the Levi-Civita connection on $T^{*} X$, but this alternative compatible connection is an allowable perturbation of the usual Seiberg-Witten equations and can be used to calculate the Seiberg-Witten invariants (see section 4 of [OS2]). Under suitable generic conditions the moduli space is a compact, oriented, smooth manifold of dimension
$$d(\xi)=\frac{1}{4}\left(c_{1}(\xi)^{2}-2 \chi(X)-3 \sigma(X)\right)$$
which is independent of metric and perturbation when $b_{+}(X)>1$.

The Seiberg-Witten invariant $S W_{X}(\xi)$ is a suitable count of solutions. Fix a base point in $M$ and let $\mathcal{G}^{0} \subset \operatorname{Map}\left(X, S^{1}\right)$ denote the group of maps which map that point to 1. The base moduli space, denoted by $\mathcal{M}^{0}$, is the quotient of the space of solutions by $\mathcal{G}^{0}$. When the moduli space $\mathcal{M}\left(X, \xi, g_{X}, \delta\right)$ is smooth, $\mathcal{M}^{0}$ is a principle $S^{1}$-bundle over $\mathcal{M}\left(X, \xi, g_{X}, \delta\right)$. For a given Spin ${ }^{c}$ structure $\xi$, the 4-dimensional Seiberg-Witten invariant $S W_{X}(\xi)$ is defined to be 0 when $d(\xi)<0$, the sum of signed points when $d(\xi)=0$, or if $d(\xi)>0$, it is the pairing of the fundamental class of $\mathcal{M}\left(X, \xi, g_{X}, \delta\right)$ with the maximal cup product of the Euler class of the $S^{1}$-bundle $\mathcal{M}^{0}$.

The dimension formula (6) simplifies when the manifold has a fixed point free circle action. Because $X$ has a nonzero vector field T, the Euler class is zero. As mentioned previously, the signature of $X$ is also zero.

Proposition 12. Suppose that $X$ is a 4-manifold with a fixed point free circle action. The expected dimension of the moduli space for a $\operatorname{Spin}^{c}$ structure $\xi$ is
$$d(\xi)=\frac{1}{4} c_{1}(\xi)^{2} .$$

\section*{4. Spin ${ }^{c}$ structures and SW solutions}

We continue to work with an orbifold circle bundle $\pi: X \rightarrow Y$ with an $S^{1}$-invariant metric $g_{X}=\eta^{2}+\pi^{*}\left(g_{Y}\right)$. The perturbation $\delta \in \Omega^{2}(Y, \mathbf{i} \mathbb{R})$ is a closed orbifold 2-form used to perturb the 3-dimensional equations which is then pulled back and projected on to the self-dual 2-forms of $X$ to perturb the 4-dimensional equations.
4.1. Restrictions on Spin ${ }^{c}$ structures. First, we make some basic observations. If $S W_{X}(\xi) \neq$ 0 for some Spin ${ }^{c}$ structure $\xi$, then the expected dimension of the moduli space is nonnegative, implying
$$c_{1}(\xi)^{2} \geq 0 .$$
If $b_{+}(X)=1$, then the metric $g_{X}$ induces a splitting $\mathcal{H}^{2}(X ; \mathbb{R})=\mathcal{H}^{+} \oplus \mathcal{H}^{-}$where $\mathcal{H}^{+}$is one dimensional. Let $c_{1}(\xi)^{+}$be the $L^{2}$ projection onto the self-dual subspace $\mathcal{H}^{+}$. When $c_{1}(\xi)^{+}$is nonzero, it provides an orientation for $\mathcal{H}^{+}$. In this situation the Seiberg-Witten invariant depends on the chamber of $2 \pi c_{1}(\xi)+\pi^{*}(\mathbf{i} \delta)$. We will say that $\alpha \in H^{2}(X ; \mathbb{R})$ lies in the positive chamber if $\alpha^{+} \cdot c_{1}(\xi)^{+}>0$. Denote the Seiberg-Witten invariant calculated for $\alpha=\left(2 \pi c_{1}(\xi)+\pi^{*}(\mathbf{i} \delta)\right)$ in this chamber by $S W_{X}^{+}(\xi)$ and denote the invariant of the other chamber by $S W_{X}^{-}(\xi)$.

When $c_{1}(\xi)^{+}=0$ there no distinguished chamber. However, if $S W_{X}(\xi) \neq 0$ in either chamber, the dimension of the moduli is nonzero and
$$0 \leq c_{1}(\xi)^{2}=\left(c_{1}(\xi)^{-}\right)^{2} \leq 0 .$$
Since the intersection form on $\mathcal{H}^{-}$is definite, $c_{1}(\xi)$ is a torsion class and pulled back from $Y$ by Theorem 9.

With this as background, we can state:
Theorem A. Let $\xi$ be a $\operatorname{Spin}^{c}$ structure on 4-manifold $X$ with a fixed point free circle action such that $S W_{X}(\xi) \neq 0$ (in either chamber when $b_{+}=1$ ).
\begin{itemize}
\item[1.] If $b_{+}(X)>1$ or $b_{+}(X)=0$, then $c_{1}(\xi)$ is pulled back from $Y$.
\item[2.] If $b_{+}(X)=1$, then either $c_{1}(\xi)$ is pulled back from $Y$, or $S W_{X}^{+}(\xi)=0$.
\end{itemize}

Remark 13. In case 2b, the Seiberg-Witten invariant of the other chamber can be calculated using the wall crossing formula of [LL].

Corollary 14. If $b_{+}(X)>1$ then $c_{1}(\xi)^{2}=0$ and $X$ is SW simple type.

Recall that a 4-manifold is SW simple type if the dimension of the moduli space is 0 for all Spin ${ }^{c}$ structures with nonzero Seiberg-Witten invariants.

Theorem A follows easily from the following formula about Seiberg-Witten solutions.
Theorem 15. Let $(A, \Psi)$ be any solution in $\mathcal{M}\left(X, \xi, g_{X}, \pi^{*}(\delta)^{+}\right)$. Then
$$0=\int_{X}\left|\nabla_{\mathrm{T}} \Psi\right|^{2}+\left|D^{+} \Psi\right|^{2}+\left|\iota_{\mathrm{T}} F_{A}\right|^{2}+2 \pi^{2} c_{1}(\xi)^{2}+2 \pi c_{1}(\xi) \cdot \pi^{*}(\mathbf{i} \delta) .$$
The vector field T is the unit vector field generated by the circle action.
Remark 16. The equation in Theorem 15 only holds for perturbations which are pulled back from $Y$. It does not hold for a general self-dual 2-form on $X$.

The rest of this subsection contains a proof of Theorem A assuming Theorem 15 above. We will then come back and prove Theorem 15 in the next subsection. We prove each case separately.

Proof of case 1: When $b_{+}(X)>1$, the moduli space is nonempty for all generic metric and perturbation pairs. Since generic pairs are dense in the space of metrics and self-dual 2-forms, we can take a sequence of generic pairs which converge to the pair $\left(g_{X}, 0\right)$. By compactness, solutions of the generic pairs converge to a solution $(A, \Psi) \in \mathcal{M}\left(X, \xi, g_{X}, 0\right)$ and it satisfies
$$0=\int_{X}\left|\nabla_{\mathrm{T}} \Psi\right|^{2}+\left|D^{+} \Psi\right|^{2}+\left|\iota_{\mathrm{T}} F_{A}\right|^{2}+2 \pi^{2} c_{1}(\xi)^{2}$$
by Theorem 15. Using equation (7) we conclude that all terms in equation (8) vanish; in particular, $c_{1}(\xi)^{2}=0$ and
$$\iota_{\mathrm{T}} F_{A}=0 .$$
Since $d F_{A}=0$, this equation implies $\mathcal{L}_{\mathrm{T}} F_{A}=0$ by Cartan's formula. Together the equations $\iota_{\mathrm{T}} F_{A}=\mathcal{L}_{\mathrm{T}} F_{A}=0$ imply that $F_{A}$ is pulled back from $Y$. Since $c_{1}(\xi)=\frac{\mathbf{i}}{2 \pi} F_{A}$, case 1 follows.

When $b_{+}(X)=0$ we have that $b_{2}(X)=0$ is also zero because the signature is zero. Thus $c_{1}(\xi)$ is always a torsion class and this is pulled back by Theorem 9. \(\square\)

Proof of case 2: Assume that $c_{1}(\xi)$ is not pulled back. By the argument proceeding the statement of Theorem A, $c_{1}(\xi)^{+} \neq 0$.

We proceed by contradiction. Suppose that $S W_{X}^{+}(\xi) \neq 0$. In this chamber, the moduli space will be nonempty for all generic pairs of metrics and perturbations. Note that the unperturbed Seiberg-Witten equations $(\delta=0)$ are in this chamber because $\left(2 \pi c_{1}(\xi)-0\right)^{+} \cdot c_{1}(\xi)^{+}>0$. Hence we can use the same argument as in case 1 to show that $c_{1}(\xi)$ is pulled back from $Y$ - contradicting our assumption. Thus $S W_{X}^{+}(\xi)=0$. \(\square\)
4.2. Solutions to the SW equations. In this subsection we prove Theorem 15. The idea is to prove a Weitzenböck-type decomposition for the Dirac operator we constructed in subsection 3.3. Before we prove this decomposition, however, we need to show that the full Dirac operator $\not D_{A}$ : $\Gamma_{X}\left(W^{+} \oplus W^{-}\right) \rightarrow \Gamma_{X}\left(W^{+} \oplus W^{-}\right)$is self-adjoint. The following technical lemma accomplishes this.

Lemma 17. Let $\xi=(W, \sigma)$ be a $\operatorname{Spin}^{c}$ structure over $X$. Let $\boldsymbol{\nabla}$ be a spinorial connection created by coupling a connection $A \in \mathcal{A}\left(\operatorname{det} W^{+}\right)$with the $S O(3)$-connection ∇ defined in subsection 3.3. Similarly, let $\boldsymbol{\nabla}^{\text {L.C. }}$ be the spinorial connection created by coupling the same connection $A$ with the Levi-Civita connection $\nabla^{L . C}$. Then
$$\not D_{A}^{L . C .}=\not D_{A}-\frac{1}{2} \sigma(\eta \wedge d \eta) .$$

Since $\not D^{\text {L.C. }}$ and Clifford multiplication by 3-forms are both self-adjoint operators, $\not D_{A}$ is self-adjoint.

Proof. Extend $\eta$ to an orthonormal coframe $\left\{\eta=e^{0}, e^{1}, e^{2}, e^{3}\right\}$ on a patch of $X$ so that $e^{0}=\eta$, and $\left\{e^{1}, e^{2}, e^{3}\right\}$ are horizontal lifts of an orthonormal coframe $\left\{\bar{e}^{1}, \bar{e}^{2}, \bar{e}^{3}\right\}$ on $Y$. Let $\left\{e_{0}=\mathrm{T}, e_{1}, e_{2}, e_{3}\right\}$ be the dual vector fields with respect to the metric $g_{X}$.

The difference 1-form $\omega=\nabla^{L . C .}-\nabla \in \Omega^{1}\left(\mathfrak{s o}\left(T^{*} X\right)\right)$ can be thought of as an element in $\Omega^{1}\left(\Lambda^{2} T^{*} X\right)$ via the vector space isomorphism
$$i: \mathfrak{s o}\left(T^{*} X\right) \rightarrow \Lambda^{2}\left(T^{*} X\right)$$
defined by
$$i\left(a_{j}^{k}\right)=\frac{1}{2} \sum_{j<k} a_{k}^{j} e^{j} \wedge e^{k}$$
The action of $\mathfrak{s} \mathfrak{o}\left(T^{*} X\right)$ on the bundle $W$ is modeled on $\sigma_{\Lambda^{2}} \circ i$. Thus we can Clifford multiply the $\Lambda^{2}$ component of $\omega \in \Omega^{1}\left(\Lambda^{2} T^{*} X\right)$ to get
$$\not D_{A}^{L . C .}=\not D_{A}+\sigma_{\Lambda^{1} \otimes \Lambda^{2}}(\omega)$$
where $\sigma_{\Lambda^{1} \otimes \Lambda^{2}}: \Lambda^{1} \otimes \Lambda^{2} \rightarrow \operatorname{End}(W)$ is a linear map defined by
$$\sigma_{\Lambda^{1} \otimes \Lambda^{2}}(\alpha \otimes \beta)=\sigma(\alpha) \sigma(\beta)$$
for a basis element $\alpha \otimes \beta \in \Lambda^{1} \otimes \Lambda^{2}$. This map can be conveniently reformulated as
$$\sigma_{\Lambda^{1} \otimes \Lambda^{2}}(\alpha \otimes \beta)=-\sigma\left(\iota_{\alpha^{b}} \beta\right)+\sigma(\alpha \wedge \beta),$$
where $\iota_{\alpha^{b}}$ is contraction with the vector field which is $g_{X}$-dual to $\alpha$.
Let $\left\{\zeta_{12}, \zeta_{13}, \zeta_{23}\right\}$ be the functions defined by
$$d \eta=2 \zeta_{12} e^{1} \wedge e^{2}+2 \zeta_{13} e^{1} \wedge e^{3}+2 \zeta_{23} e^{2} \wedge e^{3} .$$
We can use equation (10) and the first Cartan Structure equation
$$d e^{i}=\sum_{j} e^{j} \wedge w_{j}^{i}$$
to calculate the connection matrix for $\nabla^{L . C .}$. For example, we can write $d \eta$ as
$$d \eta=e^{1} \wedge\left(\zeta_{12} e^{2}+\zeta_{13} e^{3}\right)+e^{2} \wedge\left(-\zeta_{12} e^{1}+\zeta_{13} e^{3}\right)+e^{3} \wedge\left(-\zeta_{13} e^{1}-\zeta_{23} e^{2}\right)$$
to get the top row of the connection matrix
$$\left(\begin{array}{cccc}
0 & \zeta_{12} e^{2}+\zeta_{13} e^{3} & -\zeta_{12} e^{1}+\zeta_{23} e^{3} & -\zeta_{13} e^{1}-\zeta_{23} e^{2} \\
-\zeta_{12} e^{2}-\zeta_{13} e^{3} & 0 & -\zeta_{12} e^{0}+\omega_{2}^{1} & -\zeta_{13} e^{0}+\omega_{3}^{1} \\
\zeta_{12} e^{1}-\zeta_{23} e^{3} & \zeta_{12} e^{0}-\omega_{2}^{1} & 0 & -\zeta_{23} e^{0}+\omega_{3}^{2} \\
\zeta_{13} e^{1}+\zeta_{23} e^{2} & \zeta_{13} e^{0}-\omega_{3}^{1} & \zeta_{23} e^{0}-\omega_{3}^{2} & 0
\end{array}\right)$$
The $\omega_{j}^{i}$ 's in the second, third, and forth row are pulled-back from the connection 1-form for the Levi-Civita connection on $Y$. The connection matrix for $\nabla$ is
$$\left(\begin{array}{cccc}
0 & 0 & 0 & 0 \\
0 & 0 & \omega_{2}^{1} & \omega_{3}^{1} \\
0 & -\omega_{2}^{1} & 0 & \omega_{3}^{2} \\
0 & -\omega_{3}^{1} & -\omega_{3}^{2} & 0
\end{array}\right) .$$

Using the isomorphism $i$, the difference $\nabla^{\text {L.C. }}-\nabla$ can be written as
$$\omega=\frac{1}{2} \sum_{i=1}^{3} e^{i} \otimes \eta \wedge \iota_{e_{i}}(d \eta)+\frac{1}{2} \eta \otimes d \eta$$
A straight forward calculation gives $\sigma_{\Lambda^{1} \otimes \Lambda^{2}}(\omega)=-\frac{1}{2} \sigma(\eta \wedge d \eta)$. \(\square\)

Remark 18. The operators $\not D_{A}^{L . C .}$ and $\not D_{A}$ have the same index.
Lemma 19. The square of the Dirac operator decomposes into
$$\left(\not D_{A}^{+}\right)^{*} \not D_{A}^{+}=-\left(\nabla_{\mathrm{T}}\right)^{2}+\left(D^{+}\right)^{*} D^{+}+\frac{1}{2} \sigma\left(\left(\eta \wedge \iota_{\mathrm{T}} F_{A}\right)^{+}\right) .$$
where ( ) ${ }^{+}$is the projection onto self-dual 2-forms.
Proof. We work with the full Dirac operator first. By using the definition of ∇ from equation (3), we see from
$$\begin{aligned}
\left\langle\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \Psi, \Phi\right\rangle & =\left\langle\Psi, \boldsymbol{\nabla}_{\mathrm{T}}(\sigma(\eta) \Phi)\right\rangle \\
& =\left\langle\Psi, \sigma\left(\nabla_{\mathrm{T}} \eta\right) \Phi\right\rangle+\left\langle\Psi, \sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \Phi\right\rangle \\
& =\left\langle\Psi, \sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \Phi\right\rangle
\end{aligned}$$
that $\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}$ is $L^{2}$ self-adjoint.
The Dirac operator decomposes into a sum of two self-adjoint operators:
$$\not D_{A}=\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}+D,$$
where $D=\sum_{i=1}^{3} \sigma\left(e^{i}\right) \boldsymbol{\nabla}_{e_{i}}$.
Squaring and noting that $\nabla_{T} \eta=0$ and $\sigma(\eta) \sigma(\eta)=-I d$ yields
$$\not D_{A}^{2}=-\left(\boldsymbol{\nabla}_{\mathrm{T}}\right)^{2}+D^{2}+\left\{\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}, D\right\}$$
where $\{\cdot, \cdot\}$ denotes the anticommutator. The last term simplifies using Clifford relations and the equations (1) and (3):
$$\left\{\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}, D\right\}=\sum_{i=1}^{3} \sigma\left(\eta \wedge e^{i}\right)\left[\boldsymbol{\nabla}_{\mathrm{T}}, \boldsymbol{\nabla}_{e_{i}}\right] .$$
One can use the connection matrix (11) to calculate that
$$\left[\mathrm{T}, e_{i}\right]=\nabla_{\mathrm{T}}^{L . C} \cdot e_{i}-\nabla_{e_{i}}^{L . C .} T=0$$
for $i=1,2,3$. Therefore the curvature reduces to
$$F_{\boldsymbol{\nabla}}\left(\mathrm{T}, e_{i}\right)=\left[\boldsymbol{\nabla}_{\mathrm{T}}, \boldsymbol{\nabla}_{e_{i}}\right],$$
and we can see that
$$\left\{\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}, D\right\}=\sum_{i=1}^{3} \sigma\left(\eta \wedge e^{i}\right) F_{\boldsymbol{\nabla}}\left(\mathrm{T}, e_{i}\right)=\sigma(\eta) \sigma\left(\iota_{\mathrm{T}} F_{\boldsymbol{\nabla}}\right) .$$
By the definition of $\nabla$, the action of $\left[\boldsymbol{\nabla}_{\mathrm{T}}, \boldsymbol{\nabla}_{e_{i}}\right]$ for $i=1,2,3$ commutes with Clifford multiplication. Therefore $F_{\boldsymbol{\nabla}}\left(\mathrm{T}, e_{i}\right)$ is a scalar endomorphism, so
$$F_{\boldsymbol{\nabla}}\left(\mathrm{T}, e_{i}\right)=\frac{1}{2} F_{A}\left(\mathrm{~T}, e_{i}\right) .$$
Restricting attention to $W^{+}$gives the formula. \(\square\)

Proof of Theorem 15: Take a solution $(A, \Psi) \in \mathcal{M}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$, apply $\left(\not D_{A}^{+}\right)^{*} \not D_{A}^{+}$, and take the inner product with $\Psi$. After applying Lemma 19 and integrating over $X$ we get
$$\begin{aligned}
0 & =\int_{X}\left\langle\left(\not D_{A}^{+}\right)^{*} \not D_{A}^{+} \Psi, \Psi\right\rangle \\
& =\int_{X}\left\langle\left(\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}\right)^{2} \Psi, \Psi\right\rangle+\left\langle\left(D^{+}\right)^{*} D^{+} \Psi, \Psi\right\rangle+\frac{1}{2}\left\langle\sigma\left(\left(\eta \wedge \iota_{\mathrm{T}} F_{A}\right)^{+}\right) \Psi, \Psi\right\rangle \\
& =\int_{X}\left|\nabla_{\mathrm{T}} \Psi\right|^{2}+\left|D^{+} \Psi\right|^{2}+2\left\langle\left(\eta \wedge \iota_{\mathrm{T}} F_{A}\right), q(\Psi)\right\rangle .
\end{aligned}$$
In the last step we used the adjoint property of $q(\Psi)$ from equation (5) and the fact that $q(\Psi)$ is self-dual.

Substituting the $q(\Psi)=F_{A}^{+}+\pi^{*}(\delta)^{+}$from (4), we get
$$\begin{aligned}
2\left\langle\left(\eta \wedge \iota_{\mathrm{T}} F_{A}\right), q(\Psi)\right\rangle & \left.=2\left\langle\left(\eta \wedge \iota_{\mathrm{T}} F_{A}\right), F_{A}^{+}+\pi^{*}(\delta)^{+}\right)\right\rangle \\
& =\left\langle\iota_{\mathrm{T}} F_{A}, \quad \iota_{\mathrm{T}}\left(F_{A}+\star F_{A}+\pi^{*}(\delta)+\star \pi^{*}(\delta)\right)\right\rangle \\
& =\left|\iota_{\mathrm{T}} F_{A}\right|^{2}+\left\langle\iota_{\mathrm{T}} F_{A}, \iota_{\mathrm{T}} \star\left(F_{A}+\pi^{*}(\delta)\right)\right\rangle \\
& =\left|\iota_{\mathrm{T}} F_{A}\right|^{2}+\frac{1}{2} \mathbf{i} F_{A} \wedge \mathbf{i} F_{A}+\mathbf{i} F_{A} \wedge \pi^{*}(\mathbf{i} \delta)
\end{aligned}$$
The last equality is true by the following calculation. Let $F_{i j}$ be the functions defined by
$$F_{A}=\sum_{0 \leq i<j} \mathbf{i} F_{i j} e^{i} \wedge e^{j} .$$
Then
$$\iota_{\mathrm{T}} F_{A}=\mathbf{i} F_{01} e^{1}+\mathbf{i} F_{02} e^{2}+\mathbf{i} F_{03} e^{3}$$
and
$$\iota_{\mathrm{T}} \star F_{A}=\mathbf{i} F_{12} e^{3}-\mathbf{i} F_{13} e^{2}+\mathbf{i} F_{23} e^{1} .$$
Taking their inner product gives
$$\left\langle\iota_{\mathrm{T}} F_{A}, \iota_{\mathrm{T}} \star F_{A}\right\rangle=F_{01} F_{23}-F_{02} F_{13}+F_{03} F_{12}=\frac{1}{2} \mathbf{i} F_{A} \wedge \mathbf{i} F_{A} .$$
A similar calculation shows that $\left\langle\iota_{\mathrm{T}} F_{A}, \iota_{\mathrm{T}} \star \pi^{*}(\delta)\right\rangle=\mathbf{i} F_{A} \wedge \pi^{*}(\mathbf{i} \delta)$.
Integrating equation (19) over $X$ gives the lemma. \(\square\)

\section*{5. Diffeomorphic moduli spaces}

In this section we prove Theorem B. We continue to work with the circle bundle $\pi: X \rightarrow Y$ with the $S^{1}$-invariant metric $g_{X}=\eta \otimes \eta+\pi^{*}\left(g_{Y}\right)$ as in 3.3. Fix a closed orbifold 2-form $\delta \in \Omega^{2}(Y ; \mathbf{i} \mathbb{R})$ to perturb the 3-dimensional equations and pull it back to get an $S^{1}$-invariant 2-form on $X$. Perturb the 4-dimensional equations by projecting $\pi^{*}(\delta)$ onto the self-dual 2-forms to get $\pi^{*}(\delta)^{+}$.

The total moduli space $\mathcal{M}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$is a disjoint collection of moduli spaces, one component for each Spin ${ }^{c}$ structure $\xi$ on $X$. Define
$$\mathcal{N}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$$
to be the components of the total moduli space whose cohomology class $c_{1}(\xi)$ is pulled back from $Y$.

Theorem A implies that we need only look at these components to calculate the Seiberg-Witten invariants when $b_{+}>1$. This restriction on the total moduli space is done to rule out Spin ${ }^{c}$ structures covered in Theorem A case 2b.

Note that for any Spin ${ }^{c}$ structure $\xi$ whose $c_{1}(\xi)$ class is pulled back and for any 2-form $\delta$,
$$\begin{aligned}
c_{1}(\xi)^{2} & =0 \\
c_{1}(\xi) \cdot \pi^{*}(\mathbf{i} \delta) & =0 .
\end{aligned}$$
In particular, the expected dimension of the moduli space is 0 by Proposition 12.
A pullback of a solution ( $A_{0}, \Psi_{0}$ ) to (2) on $Y$ is the solution ( $A, \Psi$ ) $=\pi^{*}\left(A_{0}, \Psi_{0}\right)$ to (4) on $X$. Pick an orthonormal coframe on a patch of $X$
$$\left\{e^{0}, e^{1}, e^{2}, e^{3}\right\}$$
so that $e^{0}=\eta$, and $\left\{e^{1}, e^{2}, e^{3}\right\}$ are horizontal lifts of an orthonormal coframe $\left\{\bar{e}^{1}, \bar{e}^{2}, \bar{e}^{3}\right\}$ on $Y$. Let $\left\{e_{0}=\mathrm{T}, e_{1}, e_{2}, e_{3}\right\}$ be the dual vector fields with respect to the metric $g_{X}$. In this case the Dirac operator can be written as
$$\not D_{A}^{+}=\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}}+D_{A}$$
where ∇ is a connection on $W^{+}$created by coupling $A$ with the reducible connection ∇ (see subsection 3.3) and $D=\sum \sigma\left(e^{i}\right) \boldsymbol{\nabla}_{e_{i}}$ for $i=1,2,3$. From the construction of the pulled back Spin ${ }^{c}$ structure, it is immediately clear that $\pi^{*}(\Psi)$ is harmonic since it is constant along the fiber and comes from a harmonic spinor on $Y$. The first equation of (4) is satisfied by pulling up the first equation and projecting each term onto the self-dual 2-forms. Since a gauge transformation on $\xi$ pulls back to a gauge transformation of $\pi^{*}(\xi)$, we get a well defined map on the level of moduli spaces.

Theorem B. The pullback map $\pi^{*}$ induces a homeomorphism
$$\pi^{*}: \mathcal{M}^{*}\left(Y, g_{Y}, \delta\right) \rightarrow \mathcal{N}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right) .$$
Furthermore, if either of the two moduli spaces is a smooth manifold, then both of them are smooth, and $\pi^{*}$ is a diffeomorphism.

One remark: There is no restriction on $b_{+}(X)$ in the above theorem.
The next three subsections contains the proof of this theorem. We show that $\pi^{*}$ is a homeomorphism in the first two subsections. In the final subsection we show that $d \pi^{*}$ is an isomorphism on the kernel of the linearizations. This is sufficient to prove that the moduli spaces are diffeomorphic because the expected dimension of each is zero. Bochner vanishing arguments are used to prove that $\pi^{*}$ and $d \pi^{*}$ are surjective.
5.1. $\pi^{*}$ is injective. Suppose we have two irreducible solutions to the 3-dimensional equations whose pullbacks $(A, \Psi)$ and $\left(A^{\prime}, \Psi^{\prime}\right)$ differ by a gauge transformation $g \in \operatorname{Map}\left(X, S^{1}\right)$,
$$g(A, \Psi)=\left(A^{\prime}, \Psi^{\prime}\right) .$$
We wish to show that $g$ is in fact pulled back from $\operatorname{Map}\left(Y, S^{1}\right)$. We think of $g$ as a section of $\operatorname{End}\left(\operatorname{det} W^{+}\right)=\operatorname{End}\left(\pi^{*}(\operatorname{det} W)\right)=\pi^{*}(\operatorname{End}(\operatorname{det} W))$. Use $A$ to create a connection $\nabla^{\operatorname{End}}$ on $\operatorname{End}\left(\pi^{*}\left(W^{+}\right)\right)$which has trivial fiberwise holonomy. Then
$$\begin{aligned}
\left(\nabla_{\mathrm{T}}^{\operatorname{End}} g\right) \Psi & =\nabla_{\mathrm{T}}^{A}(g \Psi)-g \nabla_{\mathrm{T}}^{A} \Psi \\
& =0
\end{aligned}$$
because $\Psi^{\prime}=g \Psi$ are pulled back sections. By the unique continuation theorem for elliptic operators, $\Psi \neq 0$ on a dense open set, hence
$$\nabla_{\mathrm{T}}^{\mathrm{End}^{2}}{ }_{16} \equiv 0$$
on $X$. Thus $g$ is a fiberwise constant section of the line bundle $\pi^{*}(\operatorname{End}(\operatorname{det} W))$ and by Proposition 10, it can be pushed forward to a section of $\operatorname{End}(\operatorname{det} W)$ on $Y$, i.e., a gauge transformation on $Y$.
5.2. $\pi^{*}$ is surjective. Take a solution $(A, \Psi) \in \mathcal{N}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$to the Seiberg-Witten equations (4). We will show that the solution is pulled up from a solution $\left(A_{0}, \Psi_{0}\right)$ on $Y$.

Combining the formula in Theorem 15 with the fact that $\operatorname{Spin}^{c}$ structures from $\mathcal{N}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$ satisfy equations (20), we get
$$0=\int_{X}\left|\nabla_{\mathrm{T}} \Psi\right|^{2}+\left|D^{+} \Psi\right|^{2}+\left|\iota_{\mathrm{T}} F_{A}\right|^{2}+\underbrace{2 \pi^{2} c_{1}(\xi)^{2}}_{0}+\underbrace{2 \pi c_{1}(\xi) \cdot \pi^{*}(\mathbf{i} \delta)}_{0} .$$
and that the following terms must be identically zero:
$$\begin{aligned}
& 0=\nabla_{\mathrm{T}} \Psi, \\
& 0=D^{+} \Psi, \\
& 0=\iota_{\mathrm{T}} F_{A},
\end{aligned}$$

Equation (25) implies $\mathcal{L}_{\mathrm{T}} F_{A}=0$ and together the equations imply that $F_{A}$ is circle invariant and pulled up from $Y$. Equation (23) and the fact that $\Psi \not \equiv 0$ means that $A$ has trivial fiberwise holonomy. Therefore we can apply Proposition 10 and Remark 11 to $\xi$ with connection $A$ to conclude that $\Psi$ corresponds to an orbifold section $\Psi_{0}$ on a $\operatorname{Spin}^{c}$ structure $\xi_{0}$ with connection $A_{0}$ on $Y$.

In this situation, $D^{+}$is the Dirac operator on the orbifold $Y$, so by equations (24) and (23), the second Seiberg-Witten equation of (2) is satisfied for $\left(A_{0}, \Psi_{0}\right)$. It is easy to check that $\left(A_{0}, \Psi_{0}\right)$ also satisfies the first Seiberg-Witten equation.

Therefore the map $\pi^{*}$ is a homeomorphism of moduli spaces. \(\square\)
5.3. The kernels are isomorphic. Consider an irreducible solution $\mathrm{S}=(A, \Psi)$ to the 4-dimensional Seiberg-Witten equations for a fixed metric and perturbation $\left(g_{X}, \pi^{*}(\delta)^{+}\right)$in the Spin ${ }^{c}$ structure $\xi$. In the previous subsection we saw that $(A, \Psi)$ was pulled back from a solution $\mathrm{S}_{0}=\left(A_{0}, \Psi_{0}\right)$ to the 3-dimensional equations on $Y$ in the Spin ${ }^{c}$ structure $\xi_{0}$.

We now describe the tangent space at the solution S. The following sequence of operators (for a fixed $k \geq 5$ )
$$0 \longrightarrow T_{\mathbf{1}} L_{k+2}^{2}\left(Y, S^{1}\right) \xrightarrow{\mathcal{L}_{\mathrm{S}}} T_{\mathrm{S}} L_{k+1}^{2}\left(\mathbf{i} T^{*} Y \oplus W^{+}\right) \xrightarrow{L S W^{4}} L_{k}^{2}\left(\mathbf{i} \Lambda_{+} T^{*} Y \oplus W^{-}\right) \longrightarrow 0$$
is called the deformation complex at S . The map $\mathcal{L}_{\mathrm{S}}$ is the infinitesimal action of the gauge group at S described by its differential at the identity:
$$\mathcal{L}_{\mathrm{S}}: \mathbf{i} f \mapsto(-2 \mathbf{i} d f, \mathbf{i} f \Psi),$$
and $L S W^{4}$ is the linearization of the 4-dimensional Seiberg-Witten equations with fixed perturbation $\pi^{*}(\delta)^{+}$. We can wrap $L S W^{4}$ and $\mathcal{L}_{\mathrm{S}}$ into one operator
$$\mathcal{T}_{\mathrm{S}}: L_{k+1}^{2}\left(\mathbf{i} T^{*} X \oplus W^{+}\right) \rightarrow L_{k}^{2}\left(\mathbf{i} \Lambda_{+} T^{*} X \oplus W^{-} \oplus \mathbf{i} \Lambda^{0} T^{*} Y\right)$$
by setting $\mathcal{T}_{\mathrm{S}}=L S W^{4}+\mathcal{L}_{\mathrm{S}}^{*}$. Then the ker $\mathcal{T}_{\mathrm{S}}$ is the set of $(a, \psi)$ which satisfy
$$\begin{array}{r}
d^{+} a-q(\psi, \Psi)-q(\Psi, \psi)=0, \\
\not D_{A} \psi+\frac{1}{2} \sigma(a) \Psi=0, \\
-2 d^{*} a+\operatorname{iIm}\langle\psi, \Psi\rangle=0 .
\end{array}$$

The last equation is a slice condition for the gauge group action.
Let $\mathcal{H}_{\mathrm{S}}^{*}$ denote the cohomology of the deformation complex at S. We can now state Lemma 2.2.11 from [N, page 129]:

Lemma 20. The deformation complex at S is Fredholm, that is, the coboundary maps have closed ranges and the cohomology spaces are finite dimensional. Moreover,
$$\mathcal{H}_{\mathrm{S}}^{0} \cong \operatorname{ker} \mathcal{L}_{\mathrm{S}}, \quad \mathcal{H}_{\mathrm{S}}^{1} \cong \operatorname{ker} \mathcal{T}_{\mathrm{S}}$$
and
$$\operatorname{coker} \mathcal{T}_{\mathrm{S}} \cong \mathcal{H}_{\mathrm{S}}^{0} \oplus \mathcal{H}_{\mathrm{S}}^{2} .$$
In particular, the expected dimension of the moduli space for the $\operatorname{Spin}^{c}$ structure $\xi$ is
$$d(\xi)=-\chi_{\mathbb{R}}\left(\mathcal{H}_{\mathrm{S}}^{*}\right)=-\operatorname{dim} \mathcal{H}_{\mathrm{S}}^{0}+\operatorname{dim} \mathcal{H}_{\mathrm{S}}^{1}-\operatorname{dim} \mathcal{H}_{\mathrm{S}}^{2} .$$

A metric and perturbation $(g, \delta)$ is called a good pair if $\mathcal{H}_{\mathrm{S}}^{0}=\mathcal{H}_{\mathrm{S}}^{2}=0$ for every solution to the Seiberg-Witten equations in the Spin ${ }^{c}$ structure $\xi$. If $\left(g_{X}, \pi^{*}(\delta)^{+}\right)$is good, then the moduli space $\mathcal{M}\left(X, \xi, g_{X}, \pi^{*}(\delta)^{+}\right)$is a smooth manifold of dimension $d(\xi)$, its formal tangent space can be identified with $\mathcal{H}_{\mathrm{S}}^{1}$ at the point S, and we can use it to calculate the Seiberg-Witten invariants of $\xi$. For a careful treatment of these ideas, see pages 127-135 of [N].

There is a similar complex for the solution $\mathrm{S}_{0}$ on $Y$. It too can be described by an operator
$$\mathcal{T}_{\mathrm{S}_{0}}: L_{k+1}^{2}\left(\mathbf{i} T^{*} Y \oplus W\right) \rightarrow L_{k}^{2}\left(\mathbf{i} \Lambda^{2} T^{*} Y \oplus W \oplus \mathbf{i} \Lambda^{0} T^{*} Y\right)$$
given by the map
$$\left[\begin{array}{c}
a_{0} \\
\psi_{0}
\end{array}\right] \xrightarrow{\mathcal{T}_{\mathrm{S}_{0}}}\left[\begin{array}{c}
d^{+} a_{0}-\tau(\psi, \Psi)-\tau(\Psi, \psi) \\
\not D_{A_{0}} \psi_{0}+\frac{1}{2} \rho\left(a_{0}\right) \Psi_{0} \\
-2 d^{*} a_{0}+\mathrm{i} \operatorname{Im}\left\langle\psi_{0}, \Psi_{0}\right\rangle
\end{array}\right] .$$
It also has a complex at $\mathrm{S}_{0}$, and an associated cohomology denoted by $\mathcal{H}_{\mathrm{S}_{0}}^{*}$ which can be described using $\mathcal{T}_{\mathrm{S}_{0}}$ and a similar statement as Lemma 20 above.

By definition S is irreducible if and only if $\mathcal{H}_{\mathrm{S}}^{0}=0$ (and likewise for $\mathrm{S}_{0}$ ). Hence solutions in $\mathcal{N}^{*}\left(X, \xi, g_{X}, \pi^{*}(\delta)^{+}\right)$satisfy
$$0=d(\xi)=\operatorname{dim} \mathcal{H}_{\mathrm{S}}^{1}-\operatorname{dim} \mathcal{H}_{\mathrm{S}}^{2}$$
by Proposition 12, equation (20), and the previous lemma. Therefore $\mathcal{H}_{\mathrm{S}}^{2}$ vanishes for these solutions precisely when $\operatorname{dim} \mathcal{H}_{\mathrm{S}}^{1}=0$. We will use this fact and the following theorem to show when $\operatorname{dim} \mathcal{H}_{\mathrm{S}}^{2}=0$.

Theorem 21. Let $\mathrm{S}=(A, \Psi) \in \mathcal{N}^{*}\left(X, \xi, g_{X}, \pi^{*}(\delta)^{+}\right)$be a irreducible solution to the Seiberg-Witten equations and let $\mathrm{S}_{0}=\left(A_{0}, \Psi_{0}\right) \in \mathcal{M}^{*}\left(Y, \xi_{0}, g_{Y}, \delta\right)$ be the solution such that $\mathrm{S}=\pi^{*}\left(\mathrm{~S}_{0}\right)$. Then
$$\pi^{*}\left(\mathcal{H}_{\mathrm{S}_{0}}^{1}\right)=\mathcal{H}_{\mathrm{S}}^{1},$$
i.e., the kernels of $\mathcal{T}_{\mathrm{S}_{0}}$ and $\mathcal{T}_{\mathrm{S}}$ are naturally isomorphic via $\pi^{*}$.
Because the expected dimension of the moduli space on the 3-manifold is always zero, when there is a good pair $\left(g_{Y}, \delta\right)$ such that $\operatorname{dim} \mathcal{H}_{\mathrm{S}_{0}}^{0}=\operatorname{dim} \mathcal{H}_{\mathrm{S}_{0}}^{2}=\operatorname{dim} \mathcal{H}_{\mathrm{S}_{0}}^{1}=0$ for all solutions in $\mathcal{M}\left(Y, g_{Y}, \delta\right)$ we get by Theorem 21 that the dimension of $\mathcal{H}_{\mathrm{S}}^{1}$ will be zero for the pulled back solutions as well. Hence $\mathcal{H}_{\mathrm{S}}^{2}=0$ by equation (27) for all irreducible solutions S implying that $\mathcal{N}^{*}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$is a smooth manifold. Thus Theorem 21 finishes the proof of Theorem B. If, in addition, $\mathcal{N}\left(X, g_{X}, \pi^{*}(\delta)^{+}\right)$does not contain any reducible solutions, then $\left(g_{X}, \pi^{*}(\delta)^{+}\right)$will be a good pair for any $\operatorname{Spin}^{c}$ structure pulled back from $Y$.

The rest of this subsection contains the proof of Theorem 21. We use a Bochner vanishing argument similar to equation (22).

Certainly a solution to $\mathcal{T}_{\mathrm{S}_{0}}\left(a_{0}, \psi_{0}\right)=0$ pulls back to a solution of $\mathcal{T}_{\mathrm{S}}\left(\pi^{*}\left(a_{0}\right), \pi^{*}\left(\psi_{0}\right)\right)=0$. We need to show that $\pi^{*}$ is surjective, i.e., for each solution $(a, \psi)$ of the equations (26), we will prove that
$$\boldsymbol{\nabla}_{\mathrm{T}} \psi=0 \quad \text { and } \quad a \in \pi^{*}\left(\Omega^{1}(Y ; \mathbf{i R})\right) .$$

Use $\eta$ to decompose $a$ into $a=f \eta+c$ where $f \in \Omega^{0}(X ; \mathbf{i} \mathbb{R})$ and $c \in \Omega^{1}(X ; \mathbf{i} \mathbb{R})$. Since $(a, \psi)$ satisfies $\not D_{A}^{+} \psi+\frac{1}{2} \sigma(a) \Psi=0$, we have
$$\begin{aligned}
0= & \int_{X}\left|\not D_{A}^{+} \psi+\frac{1}{2} \sigma(a) \Psi\right|^{2} \\
= & \int_{X}\left|\left(\sigma(\eta)\left(\boldsymbol{\nabla}_{\mathrm{T}} \psi+\frac{1}{2} f \Psi\right)\right)+\left(D^{+} \psi+\frac{1}{2} \sigma(c) \Psi\right)\right|^{2} \\
= & \int_{X}\left|\boldsymbol{\nabla}_{\mathrm{T}} \psi+\frac{1}{2} f \Psi\right|^{2}+\left|D^{+} \psi+\frac{1}{2} \sigma(c) \Psi\right|^{2}+ \\
& \quad 2 \operatorname{Re}\left\langle\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \psi, D^{+} \psi\right\rangle+\operatorname{Re}\left\langle\sigma(\eta) \boldsymbol{\nabla}_{\mathrm{T}} \psi, \sigma(c) \Psi\right\rangle+ \\
& \quad \operatorname{Re}\left\langle f \sigma(\eta) \Psi, D^{+} \psi\right\rangle+\operatorname{Re}\left\langle f \sigma(\eta) \Psi, \frac{1}{2} \sigma(c) \Psi\right\rangle .
\end{aligned}$$