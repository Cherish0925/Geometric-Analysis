---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Positivity of Intersections and Tameness of Almost Complex 4-manifolds]

Proof of Theorem 3. As $C$ is compact, there is a finite set of balls $B_{i} \subset X$ of diameter $\varepsilon$ intersecting $C$ such that $C \subset \bigcup B_{i}$. For each $i$, take a semipositive form $\varphi_{i}$ supported inside $B_{i}$ such that $\int_{C} \varphi_{i}>0$. By Proposition 5.3, for each $i$, there exist a closed 2-form $\omega_{i}$, a positive constant $K_{i}$, and an open set $U_{i} \subset X$ containing $C$ such that $\omega_{i}$ is Poincaré dual to $C$ and $\omega_{i}+K_{i} \varphi_{i}$ is a semipositive form which is strictly positive on $U_{i}$. The intersection $\bigcap U_{i}$ is an open set containing $C$. As $C$ is compact, there exists $\delta>0$ such that every point of $X \delta$-close to $C$ is contained in $\bigcap U_{i}$. Let $S$ be a closed pseudoholomorphic curve such that $\langle[S],[C]\rangle \leq 0$ and some point of $S$ is $\delta$-close to $C$. Since $S$ intersects each $U_{i}$,
$$0<\int_{S}\left(\omega_{i}+K_{i} \varphi_{i}\right)=\langle[S],[C]\rangle+K_{i} \int_{S} \varphi_{i} \leq K_{i} \int_{S} \varphi_{i} .$$
Therefore, $S$ intersects the support of each $\varphi_{i}$ and thus each $B_{i}$. As the $B_{i}$ cover $C$, each point of $C$ is $\varepsilon$-close to $S$. \(\square\)

Proof of Corollary 1.3. Suppose $\langle[S],[C]\rangle>0$ and for every $\delta>0$ there exists a closed pseudo-holomorphic curve $S^{\prime} \subset X$ which is $\delta$-close to $S$ in the Hausdorff metric and satisfies $\langle[S],[C]\rangle \leq 0$. Given $\varepsilon>0$, let $\delta>0$ be as in Theorem 3 and $S^{\prime} \subset X$ be a closed pseudoholomorphic curve which is $\min (\varepsilon, \delta)$-close to $S$ in the Hausdorff metric and satisfies $\left\langle\left[S^{\prime}\right],[C]\right\rangle \leq 0$. Since $S \cap C \neq \emptyset$, as least one point of $S^{\prime}$ is $\delta$-close to $C$ and thus every point of $C$ is $\varepsilon$-close to $S^{\prime}$ and $2 \varepsilon$-close to $S$. As $\varepsilon$ is arbitrary, $C \subset S$. \(\square\)

Proof of Theorem 2. By Proposition 5.3, there exist a closed 2-form $\omega_{C}$ Poincaré dual to $C$ and a positive constant $K$ such that $\omega_{C}+K \varphi$ is a semipositive form which is strictly positive on $C$ and therefore somewhere on $\operatorname{supp}(T)$. By Lemma 3.14,
$$0<T\left(\omega_{C}+K \varphi\right)=T\left(\omega_{C}\right)+K T(\varphi)=T\left(\omega_{C}\right)=\langle[T],[C]\rangle,$$
as claimed. \(\square\)

Proof of Proposition 2.4. Let $T$ be a nonzero complex cycle on $X$. There exists a closed connected pseudoholomorphic curve $C$ such that $C \cap \operatorname{supp}(T) \neq \emptyset$ and $\int_{C} \varphi>0$. As $C$ is closed and connected, there are irreducible components $C_{0}, \ldots, C_{k}$ of $C$ such that
$$C_{0} \cap \operatorname{supp}(T) \neq \emptyset, \quad \int_{C_{k}} \varphi>0, \quad \text { and } \quad C_{i-1} \cap C_{i} \neq \emptyset \quad \forall i=1, \ldots, k .$$
Let $i \in\{0,1, \ldots, k\}$ be the largest integer such that $C_{i} \cap \operatorname{supp}(T) \neq \emptyset$. If $i<k$, then $C_{i} \not \subset \operatorname{supp}(T)$ by the last condition in (6.1) and thus $\left\langle[T],\left[C_{i}\right]\right\rangle \neq 0$ by Corollary 1.2. If $i=k$, then either $T(\varphi) \neq 0$ or $\left\langle[T],\left[C_{k}\right]\right\rangle \neq 0$, by Theorem 2. Therefore, $[T] \neq 0 \in H_{2}(X, \mathbb{R})$ and $(X, J)$ admits a taming symplectic structure by Proposition 1.1. \(\square\)

Proof of Theorem 1. We first show that $(d) \Rightarrow(c) \Rightarrow(b) \Rightarrow(a)$. Suppose $X$ has uncountably many embedded rational curves. As $X$ has only countably many integer homology classes, at least 2 of these curves lie in the same homology class, which thus has nonnegative self-intersection number by the positivity of intersections. Therefore, $(d) \Rightarrow(c)$. Trivially, $(c) \Rightarrow(b)$. It follows from Example 4.4 that $(b) \Rightarrow(a)$. Therefore, it suffices to consider the case when $X$ contains a free curve, $C_{\text {free }}$. Let $\varphi$ be a semipositive Poincaré dual to $C_{\text {free }}$ as in Lemma 5.1. For every $x \in X$, there exists a closed connected pseudoholomorphic curve $C_{x}$ passing through $x$ and intersecting $C_{\text {free }}$ positively. Therefore, $\int_{C_{x}} \varphi>0$ and the result follows from Proposition 2.4. \(\square\)

\section*{A Proof of Proposition 4.1}

With the assumptions as in Proposition 4.1, let
$$q_{u}: u^{*} T X \longrightarrow \mathcal{N} u \quad \text { and } \quad S_{u}:=\left\{z \in \Sigma: \mathrm{d}_{z} u=0\right\} \subset \Sigma-\partial \Sigma$$
be the quotient projection and the subset of the non-immersive points of $u$, respectively. For each $z \in S_{u}$, we define $\operatorname{ord}_{z} u \in \mathbb{Z}^{+}$to be the order of $z$ as a zero of the section $\mathrm{d} u$ of the complex line bundle $T^{*} \Sigma \otimes_{\mathbb{C}} \mathcal{T} u$ over $\Sigma$; this is well-defined by the Carleman Similarity Principle [17, Theorem 2.3.5]. Define
$$\begin{aligned}
\Gamma(T \Sigma) & =\left\{\zeta \in \Gamma(\Sigma ; T \Sigma):\left.\zeta\right|_{\partial \Sigma} \in \Gamma(\partial \Sigma ; T(\partial \Sigma))\right\}, \\
\Gamma(\mathcal{T} u ; \partial \Sigma) & =\left\{\xi \in \Gamma(\Sigma ; \mathcal{T} u):\left.\xi\right|_{\partial \Sigma} \in \Gamma(\partial \Sigma ; \mathrm{d} u(T(\partial \Sigma)))\right\}, \quad \text { and } \\
\Gamma(\mathcal{N} u ; Y) & =\left\{\xi \in \Gamma(\Sigma ; \mathcal{N} u):\left.\xi\right|_{\partial \Sigma} \in \Gamma\left(\partial \Sigma ; \mathcal{N}_{Y}(\partial u)\right)\right\} .
\end{aligned}$$
We denote by
$$\begin{aligned}
D_{Y ; J ; u}: \Gamma(u ; Y):=\left\{\xi \in \Gamma\left(\Sigma ; u^{*} T X\right):\left.\xi\right|_{\partial \Sigma}\right. & \left.\in \Gamma\left(\partial \Sigma ;\{\partial u\}^{*} T Y\right)\right\} \\
& \longrightarrow \Gamma_{J}^{0,1}(u)=\Gamma\left(\Sigma ;\left(T^{*} \Sigma\right)^{0,1} \otimes_{\mathbb{C}} u^{*} T X\right)
\end{aligned}$$
the linearization of the $\bar{\partial}_{J}$-operator on the space of smooth maps from $(\Sigma, \partial \Sigma)$ to $(X, Y)$; see [15, Section 1.2], for example. This is a real Cauchy-Riemann operator such that
$$\begin{aligned}
& D_{Y ; J ; u}(\mathrm{~d} u(\Gamma(T \Sigma))) \subset \mathrm{d} u\left(\Gamma\left(\Sigma ;\left(T^{*} \Sigma\right)^{0,1} \otimes_{\mathbb{C}} T \Sigma\right)\right) \quad \text { and } \\
& D_{Y ; J ; u}(\Gamma(\mathcal{T} u ; \partial \Sigma)) \subset \Gamma\left(\Sigma ;\left(T^{*} \Sigma\right)^{0,1} \otimes_{\mathbb{C}} \mathcal{T} u\right)
\end{aligned}$$
see [15, Section 1.3]. Thus, $D_{Y ; J ; u}$ induces linear operators
$$\begin{aligned}
& \bar{D}_{Y ; J ; u}: \Gamma(u ; Y) / \mathrm{d} u(\Gamma(T \Sigma)) \longrightarrow \Gamma_{J}^{0,1}(u) / \mathrm{d} u\left(\Gamma\left(\Sigma ;\left(T^{*} \Sigma\right)^{0,1} \otimes_{\mathbb{C}} T \Sigma\right)\right) \\
& \text { and } \quad D_{Y ; J ; u}^{\mathcal{N}}: \Gamma(\mathcal{N} u ; Y) \longrightarrow \Gamma\left(\Sigma ;\left(T^{*} \Sigma\right)^{0,1} \otimes_{\mathbb{C}} \mathcal{N} u\right) .
\end{aligned}$$
The projection $q_{u}$ induces homomorphisms
$$\widetilde{q}_{u ; 0}: \operatorname{ker} \bar{D}_{Y ; J ; u} \longrightarrow \operatorname{ker} D_{Y ; J ; u}^{\mathcal{N}} \quad \text { and } \quad \widetilde{q}_{u ; 1}: \operatorname{cok} \bar{D}_{Y ; J ; u} \longrightarrow \operatorname{cok} D_{Y ; J ; u}^{\mathcal{N}} .$$
For $z_{0} \in \Sigma$, let
$$\begin{aligned}
\Gamma_{-z_{0}}(T \Sigma) & \left.=\left\{\zeta \in \Gamma(T \Sigma): \xi\left(z_{0}\right)\right)=0\right\}, \quad \Gamma_{-z_{0}}(\mathcal{N} u ; Y)=\left\{\xi \in \Gamma(\mathcal{N} u ; Y): \xi\left(z_{0}\right)=0\right\}, \\
\Gamma_{-z_{0}}(u ; Y) & =\left\{\xi \in \Gamma(u ; Y): \xi\left(z_{0}\right)=0\right\}, \quad \Gamma_{-2 z_{0}}(\mathcal{N} u ; Y)=\left\{\xi \in \Gamma_{-z_{0}}(\mathcal{N} u ; Y):\left.\nabla \xi\right|_{z_{0}}=0\right\} .
\end{aligned}$$
We denote by
$$\begin{array}{r}
\widetilde{D}_{Y ; J ; u ;-z_{0}}: \Gamma(u ; Y) / \mathrm{d} u\left(\Gamma_{-z_{0}}(T \Sigma)\right) \longrightarrow \Gamma_{J}^{0,1}(u) / \mathrm{d} u\left(\Gamma\left(\Sigma ;\left(T^{*} \Sigma\right)^{0,1} \otimes_{\mathbb{C}} T \Sigma\right)\right) \quad \text { and } \\
\bar{D}_{Y ; J ; u ;-z_{0}}: \Gamma_{-z_{0}}(u ; Y) / \mathrm{d} u\left(\Gamma_{-z_{0}}(T \Sigma)\right) \longrightarrow \Gamma_{J}^{0,1}(u) / \mathrm{d} u\left(\Gamma\left(\Sigma ;\left(T^{*} \Sigma\right)^{0,1} \otimes_{\mathbb{C}} T \Sigma\right)\right)
\end{array}$$
the linear operators induced by $D_{Y ; J ; u}$.
Suppose the operator $\bar{D}_{Y ; J ; u}$ is surjective. By the Implicit Function Theorem for Banach manifolds, as in [17, Section 3.5], a neighborhood $\mathfrak{M}_{0}$ of $[u]$ in $\mathfrak{M}_{(g, b)}(X, Y)$ is then a smooth manifold. Furthermore, the subspace $\mathfrak{M}_{1}:=\mathfrak{f}^{-1}\left(\mathfrak{M}_{0}\right)$ of $\mathfrak{M}_{(g, b), 1}(X, Y)$ is a smooth manifold with boundary so that
$$T_{\left[u^{\prime}, z_{0}\right]} \mathfrak{M}_{1}=\operatorname{ker} \widetilde{D}_{Y ; J ; u^{\prime} ;-z_{0}} \quad \forall\left[u^{\prime}, z_{0}\right] \in \mathfrak{M}_{1}$$
and the first map in (4.1) is a fiber bundle so that the fiber over $\left[u^{\prime}\right] \in \mathfrak{M}_{0}$ is the domain of $u^{\prime}$. The second map in (4.1) is smooth and its differential is given by
$$\mathrm{d}_{\left[u^{\prime}, z_{0}\right]} \operatorname{ev}([\xi])=\xi\left(z_{0}\right) \quad \forall[\xi] \in \operatorname{ker} \widetilde{D}_{Y ; J ; u^{\prime} ;-z_{0}} .$$
If the operator $\bar{D}_{Y ; J ; u}$ is surjective and the second map in (4.1) is a submersion, then the subspace $\mathfrak{M}_{1}^{\circ}\left(x_{0}\right):=\mathrm{ev}^{-1}\left(x_{0}\right) \cap \mathfrak{M}_{1}$ of $\mathfrak{M}_{1}^{\circ}$ is a smooth submanifold satisfying (4.2) and
$$T_{\left[u^{\prime}, z_{0}\right]}\left(\mathfrak{M}_{1}^{\circ}\left(x_{0}\right)\right)=\operatorname{ker} \bar{D}_{Y ; J ; u^{\prime} ;-z_{0}} \quad \forall\left[u^{\prime}, z_{0}\right] \in \mathfrak{M}_{1}^{\circ}\left(x_{0}\right) .$$
The differential $\mathrm{d}_{z_{0}} u^{\prime}$ induces a smooth map $\mathfrak{d}$ from $\mathfrak{M}_{1}^{\circ}\left(x_{0}\right)$ to $T_{z_{0}}^{*} \Sigma \otimes_{\mathbb{R}} T_{x_{0}} X$ such that
$$q_{u} \circ\left\{\mathrm{~d}_{\left[u^{\prime}, z_{0}\right]} \mathfrak{d}([\xi])\right\}=\left.q_{u} \circ \nabla \xi\right|_{z_{0}} \quad \forall[\xi] \in \operatorname{ker} \bar{D}_{Y ; J ; u^{\prime} ;-z_{0}} .$$

By [15, Lemma 1.5.1], the second homomorphism in (A.1) is an isomorphism, the first homomorphism is surjective, and so is the homomorphism
$$\left.\operatorname{ker}\left(\widetilde{q}_{u ; 0}\right) \longrightarrow \bigoplus_{z \in S_{u}} \mathcal{T} u\right|_{z}, \quad \xi \longrightarrow(\xi(z))_{z \in S_{u}} .$$
The statement of [15, Lemma 1.5.1] is made for closed surfaces, but the proof applies to $J$ -holomorphic maps from bordered surfaces as in the statement of Proposition 4.1. Alternatively, the statement of [15, Lemma 1.5.1] can be applied directly after doubling $\Sigma, T \Sigma, u^{*} T X$, and $\mathcal{N} u$ along $\partial \Sigma$ as in the proofs of [13, Theorem 2'] and [10, Section 3]. By [13, Theorem 2'(ii)], the operator $D_{Y ; J ; u}^{\mathcal{N}}$ is onto if $\mu_{Y}^{\mathcal{N}}(u) \geq 4 g+2 b-3$. This establishes Proposition 4.1(1), as well as the parts of (2) concerning the one-marked space $\mathfrak{M}_{1}$ and the forgetful morphism $\mathfrak{f}$.

We can assume $\mu_{Y}^{\mathcal{N}}\left(u^{\prime}\right) \geq \mu_{Y}^{\mathcal{N}}(u) \geq 4 g+2 b-3$ for all $\left[u^{\prime}\right] \in \mathfrak{M}_{0}$ (i.e. the maps $u^{\prime}$ close to $u$ are no more singular than $u$ ). Let $\left[u^{\prime}, z_{0}\right] \in \mathfrak{M}_{1}^{\circ}$ and $\Sigma^{\prime}$ be the domain of $u^{\prime}$. Since
$$\left[\mathrm{d} u^{\prime}(\zeta)\right] \in \operatorname{ker} \widetilde{D}_{Y ; J ; u^{\prime} ;-z_{0}} \quad \text { and } \quad \mathrm{d}_{\left[u^{\prime}, z_{0}\right]} \operatorname{ev}\left(\left[\mathrm{d} u^{\prime}(\zeta)\right]\right)=\mathrm{d}_{z_{0}} u^{\prime}\left(\zeta\left(z_{0}\right)\right) \quad \forall \zeta \in \Gamma\left(\Sigma^{\prime}\right),$$
the image of (A.3) contains $\left.\mathcal{T} u^{\prime}\right|_{z_{0}}$ if $z_{0} \notin S_{u^{\prime}}$. If $z_{0} \in S_{u^{\prime}}$, then this is the case by the surjectivity of (A.6). By the surjectivity of the first homomorphism in (A.1), $\mathrm{d}_{\left[u^{\prime}, z_{0}\right]} \mathrm{ev}$ is thus surjective if the homomorphism
$$\left.\operatorname{ker} D_{Y ; J ; u^{\prime}}^{\mathcal{N}} \longrightarrow \mathcal{N} u^{\prime}\right|_{z_{0}}, \quad \xi \longrightarrow \xi\left(z_{0}\right),$$
is surjective. This is the case if the restriction
$$D_{Y ; J ; u^{\prime} ;-z_{0}}^{\mathcal{N}}: \Gamma_{-z_{0}}\left(\mathcal{N} u^{\prime} ; Y\right) \longrightarrow \Gamma\left(\Sigma ;\left(T^{*} \Sigma^{\prime}\right)^{0,1} \otimes_{\mathbb{C}} \mathcal{N} u^{\prime}\right)$$
of $D_{Y ; J ; u^{\prime}}^{\mathcal{N}}$ is surjective. By the twisting construction of [22, Lemma 2.4.1], the kernel and cokernel of this operator are isomorphic to the kernel and cokernel of a real Cauchy-Riemann operator $D$ as above with $\mathcal{N} u^{\prime}$ replaced by the complex line bundle $\mathcal{N} u^{\prime} \otimes_{\mathbb{C}} \mathcal{O}\left(-z_{0}\right)$, with the same boundary condition on the domain. The Maslov index of the resulting bundle pair is $\mu_{Y}^{\mathcal{N}}\left(u^{\prime}\right)-2$. By [13, Theorem 2'(ii)], such an operator $D$ is thus onto if $\mu_{Y}^{\mathcal{N}}\left(u^{\prime}\right) \geq 4 g+2 b-1$. This establishes the part of Proposition 4.1(2) concerning the evaluation morphism ev, as well as (3).

We now assume that $\mu_{Y}^{\mathcal{N}}\left(u^{\prime}\right) \geq \mu_{Y}^{\mathcal{N}}(u) \geq 4 g+2 b-1$ for all $\left[u^{\prime}\right] \in \mathfrak{M}_{0}$. Let $\left[u^{\prime}, z_{0}\right] \in \mathfrak{M}_{1}^{\circ}\left(v_{0}\right)$ and $\Sigma^{\prime}$ be the domain of $u^{\prime}$. By (A.4), (A.5), and the surjectivity of the first homomorphism in (A.1), the homomorphism
$$q_{u^{\prime}} \circ \mathrm{d}_{\left[u^{\prime}, z_{0}\right]} \mathfrak{d}:\left.T_{\left[u^{\prime}, z_{0}\right]}\left(\mathfrak{M}_{1}^{\circ}\left(x_{0}\right)\right) \longrightarrow T_{z_{0}}^{*} \Sigma^{\prime} \otimes_{\mathbb{C}} \mathcal{N} u^{\prime}\right|_{z_{0}}$$
is surjective if the homomorphism
$$\left.\operatorname{ker} D_{Y ; J ; u^{\prime} ;-z_{0}}^{\mathcal{N}} \longrightarrow T_{z_{0}}^{*} \Sigma^{\prime} \otimes_{\mathbb{C}} \mathcal{N} u^{\prime}\right|_{z_{0}},\left.\quad \xi \longrightarrow \nabla \xi\right|_{z_{0}},$$
is surjective. This is the case if the restriction
$$D_{Y ; J ; u^{\prime} ;-2 z_{0}}^{\mathcal{N}}: \Gamma_{-2 z_{0}}\left(\mathcal{N} u^{\prime} ; Y\right) \longrightarrow \Gamma\left(\Sigma ;\left(T^{*} \Sigma^{\prime}\right)^{0,1} \otimes_{\mathbb{C}} \mathcal{N} u^{\prime}\right)$$
of $D_{Y ; J ; u^{\prime}}^{\mathcal{N}}$ is surjective. By the twisting construction of [22, Lemma 2.4.1], the kernel and cokernel of this operator are isomorphic to the kernel and cokernel of a real Cauchy-Riemann operator $D$ as above with $\mathcal{N} u^{\prime}$ replaced by the complex line bundle $\mathcal{N} u^{\prime} \otimes_{\mathbb{C}} \mathcal{O}\left(-2 z_{0}\right)$, with the same boundary
condition on the domain. The Maslov index of the resulting bundle pair is $\mu_{Y}^{\mathcal{N}}\left(u^{\prime}\right)-4$. By [13, Theorem 2' (ii) ], such an operator $D$ is thus onto if $\mu_{Y}^{\mathcal{N}}\left(u^{\prime}\right) \geq 4 g+2 b+1$. This establishes Proposition 4.1(4).

Department of Mathematics, Stony Brook University, Stony Brook, NY 11794
spencer.cattalani@stonybrook.edu

\section*{References}
\begin{itemize}
\item[] [1] E. Bedford and B.A. Taylor, A new capacity for plurisubharmonic functions Acta Math. 149 (1982), no. 1-2, 1-40
\item[] [2] R. Bott and L. Tu, Differential Forms in Algebraic Topology, Springer-Verlag, 1982
\item[] [3] S. Cattalani, Coarsely holomorphic curves and symplectic topology, Math. Ann. 391 (2025), no. 2, 2925-2941
\item[] [4] J. P. Demailly, Regularization of closed positive currents and intersection theory, J. Algebraic Geom. 1 (1992), no. 3, 361-409
\item[] [5] G. de Rham, Differentiable Manifolds: Forms, Currents, Harmonic Forms, Springer-Verlag, 1984
\item[] [6] S. K. Donaldson, Lefschetz pencils on symplectic manifolds, J. Differential Geom. 53 (1999), no. 2, 205-236
\item[] [7] S. K. Donaldson, Two-forms on four-manifolds and elliptic equations, math/0607083
\item[] [8] S. K. Donaldson and I. Smith, Lefschetz pencils and the canonical class for symplectic fourmanifolds, Topology 42 (2003), no. 4, 743-785
\item[] [9] H. Federer and H. Fleming, Normal and integral currents, Ann. of Math. 72 (1960), no. 3, 458-520
\item[] [10] P. Georgieva and A. Zinger, The moduli space of maps with crosscaps: Fredholm theory and orientability, Comm. Anal. Geom. 23 (2015), no. 3, 81-140
\item[] [11] M. Gromov, Pseudoholomorphic curves in symplectic manifolds, Invent. Math. 82 (1985), no. 2, 307-347
\item[] [12] V. Guedj, Courants extrémaux et dynamique complexe, Ann. Sci. École Norm. Sup. (4) 38 (2005), no. 3, 407-426
\item[] [13] H. Hofer, V. Lizan, and J. Sikorav, On genericity for holomorphic curves in four-dimensional almost-complex manifolds, J. Geom. Anal. 7 (1997), no. 1, 149--159
\item[] [14] S. Ivashkovich and V. Shevchishin, Pseudo-holomorphic curves and envelopes of meromorphy of two-spheres in $\mathbb{C P}^{2}$, math/9804014
\item[] [15] S. Ivashkovich and V. Shevchishin, Structure of the moduli space in a neighborhood of a cuspcurve and meromorphic hulls, Invent. Math. 136 (1999), no. 3, 571--602
\end{itemize}
\begin{itemize}
\item[] [16] D. McDuff, The structure of rational and ruled symplectic 4-manifolds, J. Amer. Math. Soc. 3 (1990), no. 3, 679-712
\item[] [17] D. McDuff and D. Salamon, $J$-holomorphic Curves and Symplectic Topology, Colloquium Publications 52, AMS, 2012
\item[] [18] B. McKay, Smooth projective planes, Geom. Dedicata 116 (2005), 157-202
\item[] [19] J. Milnor, Topology from the Differentiable Viewpoint, University Press of Virginia, 1965
\item[] [20] L. Schwartz, Théorie des Distributions Publications de l'Institut de Mathématique de l'Université de Strasbourg, Herman, 1966
\item[] [21] J. P. Serre, Cohomologie et fonctions de variables complexes, Séminaire Bourbaki, Vol. 2, Exp. No. 71, 213-218, Société Mathématique de France, 1995
\item[] [22] V. Shevchishin, Pseudoholomorphic curves and the symplectic isotopy problem, math/0010262
\item[] [23] D. Sullivan, Cycles for the dynamical study of foliated manifolds and complex manifolds, Invent. Math. 36 (1976), 225-255
\item[] [24] C. Taubes, The Seiberg-Witten and Gromov invariants, Math. Res. Lett. 2 (1995), no. 2, 221-238
\item[] [25] C. Taubes, Tamed to compatible: symplectic forms via moduli space integration, J. Symplectic Geom. 9 (2011), no. 2, 161-250
\item[] [26] D. Varolin, Riemann Surfaces by Way of Complex Analytic Geometry, AMS, 2011
\item[] [27] C. Wendl, Holomorphic Curves in Low Dimensions: From Symplectic Ruled Surfaces to Planar Contact Manifolds, Springer, 2018
\item[] [28] W. Zhang, From Taubes currents to almost Kähler forms, Math. Ann. 356 (2013), no. 3, 969-978
\item[] [29] A. Zinger, Real Ruan-Tian perturbations, math/1701.01420
\end{itemize}