---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1110_0414.pdf
converter: mathpix
format: mmd
---

\title{
VOLUME ENTROPY RIGIDITY OF NON-POSITIVELY CURVED SYMMETRIC SPACES
}

\author{
FRANÇOIS LEDRAPPIER
}

To Werner Ballmann for his 60th birthday

\begin{abstract}
We characterize symmetric spaces of non-positive curvature by the equality case of general inequalities between geometric quantities.
\end{abstract}

\section*{1. Introduction}

Let $(M, g)$ be a closed connected Riemannian manifold, and $\pi:(\widetilde{M}, \widetilde{g}) \rightarrow(M, g)$ its universal cover endowed with the lifted Riemannian metric. We denote $p(t, x, y), t \in \mathbb{R}_{+}, x, y \in$ $\widetilde{M}$ the heat kernel on $\widetilde{M}$, the fundamental solution of the heat equation $\frac{\partial u}{\partial t}=\operatorname{Div} \nabla u$ on $\widetilde{M}$. Since we have a compact quotient, all the following limits exist as $t \rightarrow \infty$ and are independent of $x \in \widetilde{M}$ :
$$\begin{aligned}
\lambda_{0} & =\inf _{f \in C_{c}^{2}(\widetilde{M})} \frac{\int|\nabla f|^{2}}{\int|f|^{2}}=\lim _{t}-\frac{1}{t} \ln p(t, x, x) \\
\ell & =\lim _{t} \frac{1}{t} \int d(x, y) p(t, x, y) d \operatorname{Vol}(y) \\
h & =\lim _{t}-\frac{1}{t} \int p(t, x, y) \ln p(t, x, y) d \operatorname{Vol}(y) \\
v & =\lim _{t} \frac{1}{t} \ln \operatorname{Vol} B_{\widetilde{M}}(x, t),
\end{aligned}$$
where $B_{\widetilde{M}}(x, t)$ is the ball of radius $t$ centered at $x$ in $\widetilde{M}$ and Vol is the Riemannian volume on $\widetilde{M}$.

All these numbers are nonnegative. Recall $\lambda_{0}$ is the Rayleigh quotient of $\widetilde{M}, \ell$ the linear drift, $h$ the stochastic entropy and $v$ the volume entropy. There is the following relation:
$$4 \lambda_{0} \stackrel{(a)}{\leq} h \stackrel{(b)}{\leq} \ell v \stackrel{(c)}{\leq} v^{2} .$$
See [L1] for (a), [Gu] for (b). Inequality (c) is shown in [L3] as a corollary of (b) and (2):
$$\ell^{2} \leq h$$

\footnotetext{
2000 Mathematics Subject Classification. 53C24, 53C20, 58J65.
Key words and phrases. volume entropy, rank one manifolds.
}

If $(\widetilde{M}, g)$ is a locally symmetric space of nonpositive curvature, all five numbers $4 \lambda_{0}, \ell^{2}, h, \ell v$ and $v^{2}$ coincide and are positive unless $(\widetilde{M}, g)$ is $\left(\mathbb{R}^{n}\right.$, Eucl.). Our result is a partial converse:

Theorem 1.1. Assume $(M, g)$ has nonpositive curvature. With the above notation, any of the equalities
$$\ell=v, \quad h=v^{2} \quad \text { and } \quad 4 \lambda_{0}=v^{2}$$
hold if, and only if, $(\widetilde{M}, \widetilde{g})$ is a symmetric space.
As recalled in [L3], Theorem 1.1 is known in negative curvature and follows from [K], [BFL, [FL], [BCG] and [L1]. The other possible converses are delicate: even for negatively curved manifolds, in dimension greater than two, it is not known that $h=\ell v$ holds only for locally symmetric spaces. This is equivalent to a conjecture of Sullivan (see [L2] for a discussion). Sullivan conjecture holds for surfaces of negative curvature ([L1], [Ka]). It is not known either whether $4 \lambda_{0}=h$ holds only for locally symmetric spaces. This would follow from the hypothetical $4 \lambda_{0} \stackrel{(d)}{\leq} \ell^{2}$ by the arguments of this note.

We assume henceforth that $(M, g)$ has nonpositive sectional curvature. Given a geodesic $\gamma$ in $M$, Jacobi fields along $\gamma$ are vector fields $t \mapsto J(t) \in T_{\gamma(t)} M$ which describe infinitesimal variation of geodesics around $\gamma$. By nonpositive curvature, the function $t \mapsto\|J(t)\|$ is convex. Jacobi fields along $\gamma$ form a vector space of dimension 2 Dim $M$. The rank of the geodesic $\gamma$ is the dimension of the space of Jacobi fields such that $t \mapsto\|J(t)\|$ is a constant function on $\mathbb{R}$. The rank of a geodesic $\gamma$ is at least one because of the trivial $t \mapsto \dot{\gamma}(t)$ which describes the variation by sliding the geodesic along itself. The rank of the manifold $M$ is the smallest rank of geodesics in $M$. Using rank rigidity theorem ([B1], [BS]), we reduce in section 2 the proof of Theorem 1.1 to proving that if $(M, g)$ is rank one, equality in (2) implies that $(\widetilde{M}, \widetilde{g})$ is a symmetric space. For this, we show in section 3 that equality in (2) implies that $(\widetilde{M}, \widetilde{g})$ is asymptotically harmonic (see the definition below). This uses the Dirichlet property at infinity (Ballmann [B2]). Finally, it was recently observed by A. Zimmer ([Z]) that asymptotically harmonic universal covers of rank one manifolds are indeed symmetric spaces.

\section*{2. Generalities and reduction of Theorem 1.1}

We recall the notations and results from Ballmann's monograph [B3] about the Hadamard manifold $(\widetilde{M}, \widetilde{g})$ that we use. The space $\widetilde{M}$ is homeomorphic to a ball. The covering group $G:=\pi_{1}(M)$ satisfies the duality condition ([B3] page 45).
2.1. Boundary at infinity. Two geodesic rays $\gamma, \gamma^{\prime}$ in $\widetilde{M}$ are said to be asymptotic if $\sup _{t \geq 0} d\left(\gamma(t), \gamma^{\prime}(t)\right)<\infty$. The set of classes of asymptotic unit speed geodesic rays is called the boundary at infinity $\widetilde{M}(\infty) . \widetilde{M} \cup \widetilde{M}(\infty)$ is endowed with the topology of a compact space where $\widetilde{M}(\infty)$ is a sphere and where, for each unit speed geodesic ray $\gamma, \gamma(t) \rightarrow[\gamma]$
as $t \rightarrow \infty$. The action of the group $G$ on $\widetilde{M}(\infty)$ is the continuous extension of its action on $\widetilde{M}$. For any $x, \xi \in \widetilde{M} \times \widetilde{M}(\infty)$, there is a unique unit speed geodesic $\gamma_{x, \xi}$ such that $\gamma_{x, \xi}(0)=x$ and $\left[\gamma_{x, \xi}\right]=\xi$. The mapping $\xi \mapsto \dot{\gamma}_{x, \xi}(0)$ is a homeomorphism $\pi_{x}^{-1}$ between $\widetilde{M}(\infty)$ and the unit sphere $S_{x} \widetilde{M}$ in the tangent space at $x$ to $\widetilde{M}$. We will identify $S \widetilde{M}$ with $\widetilde{M} \times \widetilde{M}(\infty)$ by $(x, v) \mapsto\left(x, \pi_{x} v\right)$. Then the quotient $S M$ is identified with the quotient of $\widetilde{M} \times \widetilde{M}(\infty)$ under the diagonal action of $G$.

Fix $x_{0} \in \widetilde{M}$ and $\xi \in \widetilde{M}(\infty)$. The Busemann function $b_{\xi}$ is the function on $\widetilde{M}$ given by:
$$b_{\xi}(x)=\lim _{y \rightarrow \xi} d(y, x)-d\left(y, x_{0}\right) .$$
Clearly, $b_{g \xi}(g x)=b_{\xi}(x)+b_{g \xi}\left(g x_{0}\right)$. Moreover, the function $x \mapsto b_{\xi}(x)$ is of class $C^{2}$ ( HI ). It follows that the fonction $\Delta_{x} b_{\xi}$ satisfies $\Delta_{g x} b_{g \xi}=\Delta_{x} b_{\xi}$ and therefore defines a function $B$ on $G \backslash(\widetilde{M} \times \widetilde{M}(\infty))=S M$. It follows from the argument of [HI] that the function $B$ is continuous on $S M$ (see [B3], Proposition 2.8, page 69).
2.2. Jacobi fields. Let $(x, v)$ be a point in $T \widetilde{M}$. Tangent vectors in $T_{x, v} T \widetilde{M}$ correspond to variations of geodesics and can be represented by Jacobi fields along the unique geodesic $\gamma_{x, v}$ with initial value $\gamma(0)=x, \dot{\gamma}(0)=v$. A Jacobi field $J(t), t \in \mathbb{R}$ along $\gamma_{x, v}$ is uniquely determined by the values of $J(0)$ and $J^{\prime}(0)$. We describe tangent vectors in $T_{x, v} T \widetilde{M}$ by the associated pair $\left(J(0), J^{\prime}(0)\right)$ of vectors in $T_{x} \widetilde{M}$. The metric on $T_{x, v} T \widetilde{M}$ is given by $\left\|\left(J_{0}, J_{0}^{\prime}\right)\right\|^{2}=\left\|J_{0}\right\|^{2}+\left\|J_{0}^{\prime}\right\|^{2}$. Assume $(x, v) \in S M$. A vertical vector in $T_{x, v} S \widetilde{M}$ is a vector tangent to $S_{x} \widetilde{M}$. It corresponds to a pair $\left(0, J^{\prime}(0)\right)$, with $J^{\prime}(0)$ orthogonal to $v$. Horizontal vectors correspond to pairs $(J(0), 0)$. In particular, let $X$ be the vector field on $S \widetilde{M}$ such that the integral flow of $X$ is the geodesic flow. The geodesic spray $X_{x, v}$ is the horizontal vector associated to $(v, 0)$. The orthogonal space to $X$ is preserved by the differential $D g_{t}$ of the geodesic flow. More generally, the Jacobi fields representation of $T T \widetilde{M}$ satisfies $D_{x, v} g_{t}\left(J(0), J^{\prime}(0)\right)=\left(J(t), J^{\prime}(t)\right)$.

For any vector $Y \in T_{x} \widetilde{M}$, there is a unique vector $Z=S_{x, v} Y$ such that the Jacobi field $J$ with $J(0)=Y, J^{\prime}(0)=Z$ satisfies $\|J(t)\| \leq C$ for $t \geq 0$ ([B3] Proposition 2.8 (i)). The mapping $S_{x, v}: T_{x} \widetilde{M} \rightarrow T_{x} \widetilde{M}$ is linear and selfadjoint. The vectors $(Y, S Y)$ describe variations of asymptotic geodesics and the subspace $E_{x, v}^{s} \subset T_{x, v} T \widetilde{M}$ they generate corresponds to $T W_{x, v}^{s}$, where $W_{x, v}^{s}$, the set of initial vectors of geodesics asymptotic to $\gamma_{x, v}$, is identified with $\widetilde{M} \times \pi_{x}(v)$ in $\widetilde{M} \times \widetilde{M}(\infty)$. Observe that $S_{x, v} \dot{\gamma}_{x, v}(0)=0$ and that the operator $S_{x, v}$ preserves $\left(\dot{\gamma}_{x, v}(0)\right)^{\perp}$. Recall from [B3], Proposition 3.2 page 71, that, for $Y \in\left(\dot{\gamma}_{x, v}(0)\right)^{\perp}$, with $\pi_{x} v=\xi$,
$$D_{Y}\left(\nabla b_{\xi}\right)=-S_{x, v} Y,$$
and therefore $\Delta_{x} b_{\xi}=-\operatorname{Tr} S_{x, v}$ with $\pi_{x}(v)=\xi$.
Similarly, there is a selfadjoint linear operator $U_{x, v}: T_{x} \widetilde{M} \rightarrow T_{x} \widetilde{M}$ such that the Jacobi field $J$ with $J(0)=Y, J^{\prime}(0)=U Y$ satisfies $\|J(t)\| \leq C$ for $t \leq 0$. The subspace $E_{x, v}^{u} \subset$
$T_{x, v} T \widetilde{M}$ they generate corresponds to $T W_{x, v}^{u}$, where $W_{x, v}^{u}$ is the set of opposite vectors to vectors in $W_{x,-v}^{s}$. By definition, $S_{\dot{\gamma}_{x,(0)}}=-U_{\dot{\gamma}_{x,-v}(0)}$, so that we also have:
$$B(x, v):=-\operatorname{Tr} S_{x, v}=\operatorname{Tr} U_{x,-v} .$$
We have $\operatorname{Ker} S=\operatorname{Ker} U$ and $Y \in \operatorname{Ker} S$ if, and only if, the Jacobi field $J(t)$ with $J(0)=$ $Y, J^{\prime}(0)=0$ is bounded for all $t \in \mathbb{R}$. The rank of the geodesic $\gamma_{x, v}$ therefore is $\kappa=$ Dim Ker $S$ and the geodesic $\gamma_{x, v}$ is of rank one only if $\operatorname{Det}\left(\left.(U-S)\right|_{\left.(\dot{\gamma} x, v(0))^{\perp}\right)}=0\right.$.
Recall that $S M$ is identified with the quotient of $\widetilde{M} \times \widetilde{M}(\infty)$ under the diagonal action of $G$. Clearly, for $g \in G, g\left(W_{x, v}^{s}\right)=W_{D g(x, v)}^{s}$ so that the $W^{s}$ define a foliation $\mathcal{W}^{s}$ on $S M$. The leaves of the foliation $\mathcal{W}^{s}$ are quotient of $\widetilde{M}$, they are naturally endowed with the Riemannian metric induced from $\widetilde{g}$.
2.3. Proof of Theorem 1.1. We continue assuming that $(\widetilde{M}, \widetilde{g})$ has nonpositive curvature. By the Rank Rigidity Theorem (see [B3]), $(\widetilde{M}, \widetilde{g})$ is of the form
$$\left(\widetilde{M}_{0} \times \widetilde{M}_{1} \times \cdots \times \widetilde{M}_{j} \times \widetilde{M}_{j+1} \times \cdots \times \widetilde{M}_{k}, \widetilde{g}\right)^{1},$$
where $\widetilde{g}$ is the product metric $\widetilde{g}^{2}=\left(\widetilde{g}_{0}\right)^{2}+\left(\widetilde{g}_{1}\right)^{2}+\cdots+\left(\widetilde{g}_{j}\right)^{2}+\left(\widetilde{g}_{j+1}\right)^{2}+\cdots+\left(\widetilde{g}_{k}\right)^{2}$, $\left(\widetilde{M}_{0}, \widetilde{g}_{0}\right)$ is Euclidean, $\left(\widetilde{M}_{i}, \widetilde{g}_{i}\right)$ is an irreducible symmetric space of rank at least two for $i=1, \cdots, j$ and a rank-one manifold for $i=j+1, \cdots, k$. If the $\left(\widetilde{M}_{i}, \widetilde{g}_{i}\right), i=j+1, \cdots k$, are all symmetric spaces of rank one, then $(\widetilde{M}, \widetilde{g})$ is a symmetric space. Moreover in that case, all inequalities in (1) are equalities: this is the case for irreducible symmetric spaces (all numbers are 0 for Euclidean space; for the other spaces, $4 \lambda_{0}$ and $v^{2}$ are classically known to coincide ([O]) and we have:
$$4 \lambda_{0}(\widetilde{M})=\sum_{i} 4 \lambda_{0}\left(\widetilde{M}_{i}\right), \quad v^{2}(\widetilde{M})=\sum_{i} v^{2}\left(\widetilde{M}_{i}\right) .$$
To prove Theorem 1.1, it suffices to prove that if $\ell^{2}=h$, all $\widetilde{M}_{i}$ in the decomposition are symmetric spaces. This is already true for $i=0,1, \cdots j$. It remains to show that $\left(\widetilde{M}_{i}, \widetilde{g}_{i}\right)$ are symmetric spaces for $i=j+1, \cdots k$. Eberlein showed that each one of the spaces $\left(M_{i}, \widetilde{g}_{i}\right)$ admits a cocompact discrete group of isometries (see Kn , Theorem 3.3). This shows that the linear drifts $\ell_{i}$ and the stochastic entropies $h_{i}$ exist for each one of the spaces $\left(\widetilde{M}_{i}, \widetilde{g}_{i}\right)$. Moreover, we clearly have
$$\ell^{2}=\sum_{i} \ell_{i}^{2}, \quad h=\sum h_{i} .$$
Therefore Theorem 1.1 follows from
Theorem 2.1. Assume $(M, g)$ is a closed connected rank one manifold of nonpositive curvature and that $\ell^{2}=h$. Then $(\widetilde{M}, \widetilde{g})$ is a symmetric space.

\footnotetext{
${ }^{1}$ With a clear convention for the cases when $\operatorname{Dim} \widetilde{M}_{0}=0, j=0$ or $k=j$.
}

A Hadamard manifold $\widetilde{M}$ is called asymptotically harmonic if the function $B\left(=\Delta_{x} b\right)$ is constant on $S \widetilde{M}$. Theorem 2.1 directly follows from two propositions:
Proposition 2.2. Assume $(M, g)$ is a closed connected rank one manifold of nonpositive curvature and that $\ell^{2}=h$. Then $(\widetilde{M}, \widetilde{g})$ is asymptotically harmonic.
Proposition 2.3. [[Z], Theorem 1.1] Assume ( $M, g$ ) is a closed connected rank one manifold of nonpositive curvature such that $(\widetilde{M}, \widetilde{g})$ is asymptotically harmonic. Then, $(\widetilde{M}, \widetilde{g})$ is a symmetric space.

\section*{3. Proof of Proposition 2.2}

We consider the foliation $\mathcal{W}$ of subsection 2.2. Recall that the leaves are endowed with a natural Riemannian metric. We write $\Delta^{\mathcal{W}}$ for the associated Laplace operator on functions which are of class $C^{2}$ along the leaves of $\mathcal{W}$. A probability measure $m$ on $S M$ is called harmonic if it satisfies, for any $C^{2}$ function $f$, we have:
$$\int_{S M} \Delta^{\mathcal{W}} f d m=0 .$$
Let $M$ be a closed connected manifold such that $\ell^{2}=h$. In [L3] it is shown that then, there exists a harmonic probability measure $m$ on $S M$ such that, at $m$-a.e. $(x, v), B(x, v)=\ell$. Since $B$ is a continuous function, Proposition 2.2 follows from
Theorem 3.1. Let $(M, g)$ be a closed connected rank one manifold of nonpositive curvature, $\mathcal{W}$ the stable foliation on $S M$ endowed with the natural metric as above. Then, there is only one harmonic probability measure $m$ and the support of $m$ is the whole space $S M$.
Proof. Let $m$ be a $\mathcal{W}$ harmonic probability measure on $S M$. Then, there is a unique $G$-invariant measure $\widetilde{m}$ on $S \widetilde{M}$ which coincide with $m$ locally. Seen as a measure on $\widetilde{M} \times \widetilde{M}(\infty)$, we claim that $\widetilde{m}$ is given, for any $f$ continuous with compact support, by:
$$\int f(x, \xi) d \widetilde{m}(x, \xi)=\frac{1}{\operatorname{Vol} M} \int_{\widetilde{M}}\left(\int_{\widetilde{M}(\infty)} f(x, \xi) d \nu_{x}(\xi)\right) d x$$
where the family $x \mapsto \nu_{x}$ is a family of probability measures on $\widetilde{M}(\infty)$ such that, for all $\varphi$ continuous on $\widetilde{M}(\infty), x \mapsto \int \varphi(\xi) d \nu_{x}(\xi)$ is a harmonic function on $\widetilde{M}$ and the measure $d x$ is the Riemannian volume on $\widetilde{M}$. The claim follows from [Ga]. For convenience, let us reprove it: on the one hand, the measure $\widetilde{m}$ projects on $\widetilde{M}$ as a $G$-invariant measure satisfying $\int \Delta f d m=0$. The projection of $\widetilde{m}$ on $\widetilde{M}$ is proportional to Volume, gives measure 1 to fundamental domains and formula (3) is the desintegration formula. On the other hand, if one projects $\widetilde{m}$ first on $\widetilde{M}(\infty)$, there is a probability measure $\nu$ on $\widetilde{M}(\infty)$ such that
$$\int f(x, \xi) d \widetilde{m}(x, \xi)=\int_{\widetilde{M}(\infty)}\left(\int_{\widetilde{M}} f(x, \xi) d m_{\xi}(d x)\right) d \nu(\xi)$$

For $\nu$-a.e. $\xi$, the measure $m_{\xi}$ is a harmonic measure on $\widetilde{M}$; therefore, for $\nu$-a.e. $\xi$, there is a positive harmonic function $k_{\xi}(x)$ such that $m_{\xi}=k_{\xi}(x)$ Vol. Comparing the two expressions for $\int f d \widetilde{m}$, we see that the measure $\nu_{x}$ is given by
$$\nu_{x}=k_{\xi}(x) \nu$$
and $x \mapsto \int_{\widetilde{M}(\infty)} \varphi(\xi) d \nu_{x}(\xi)$ is indeed a harmonic function.
The $G$-invariance of $\widetilde{m}$ implies that, for all $g \in G, g_{*} \nu_{x}=\nu_{g x}$. In particular, the support of $\nu$ is $G$-invariant. By [E] (see [B3], page 48), the support of $\nu$ is the whole $\widetilde{M}(\infty)$ and therefore the support of $m$ is the whole $S M$. This result would be sufficient for proving Proposition 2.2, but using discretization, we are going to identify the measure $\nu_{x}$ on $\widetilde{M}(\infty)$ as the hitting measure of the Brownian motion on $\widetilde{M}$ starting from $x$. This shows Theorem 3.1

Fix $x_{0} \in \widetilde{M}$. The discretization procedure of Lyons and Sullivan ([LS]) associates to the Brownian motion on $\widetilde{M}$ a probability measure $\mu$ on $G$ such that $\mu(g)>0$ for all $g$ and that any bounded harmonic function $F$ on $\widetilde{M}$ satisfies
$$F\left(x_{0}\right)=\sum_{g \in G} F\left(g x_{0}\right) \mu(g) .$$
Recall that for all $\varphi$ continuous on $\widetilde{M}(\infty), x \mapsto \nu_{x}(\varphi)$ is a harmonic function and that $\nu_{g x}=g_{*} \nu_{x}$. It follows that the measure $\nu_{x_{0}}$ is stationary for $\mu$, i.e. it satisfies:
$$\nu_{x_{0}}=\sum_{g \in G} g_{*} \nu_{x_{0}} \mu(g) .$$
Since the support of $\mu$ generates $G$ as a semigroup (actually, it is already the whole $G$ ), there is only one stationary probability measure on $\widetilde{M}(\infty)$ (see [B3], Theorem 4.11 page 58). We know one already: the hitting measure $m_{x_{0}}$ of the Brownian motion on $\widetilde{M}$ starting from $x_{0}$. This shows that $\nu_{x_{0}}=m_{x_{0}}$. Since $x_{0}$ was arbitrary in the above reasoning, we have $\nu_{x}=m_{x}$ for all $x \in \widetilde{M}$ and the measure $\widetilde{m}$ is given by:
$$\int f(x, \xi) d \widetilde{m}(x, \xi)=\frac{1}{\operatorname{Vol} M} \int_{\widetilde{M}}\left(\int_{\widetilde{M}(\infty)} f(x, \xi) d m_{x}(\xi)\right) d x .$$ \(\square\)

Acknowledgements I am very grateful to Gerhard Knieper for his interest and his comments, in particular for having attracted my attention to [Z]. I also acknowledge partial support of NSF grant DMS-0811127.

\section*{References}
[B1] W. Ballmann, Nonpositively curved manifolds of higher rank, Ann. Math, 122 (1985), 597-609.
[B2] W. Ballmann, On the Dirichlet problem at infinity for manifolds of nonpositive curvature, Forum Mathematicum, 1 (1989), 201-213.
[B3] W. Ballmann, Lectures on spaces of nonpositive curvature, DMV Seminar, 25 (1995).
[BCG] G. Besson, G. Courtois and S. Gallot, Entropies et rigidités des espaces localement symétriques de courbure strictement négative, Geom. Func. Anal. 5 (1995), 731-799.
[BFL] Y. Benoist, P. Foulon and F. Labourie, Flots d'Anosov à distributions stables et instables différentiables, J. Amer. Math. Soc. 5 (1992), 33-74.
[BS] K. Burns and R. Spatzier, Manifolds of nonpositive curvature and their buildings, Publications math. IHES, 65 (1987), 35-59.
[E] P. Eberlein, Geodesic flows on negatively curved manifolds, II, Transactions Amer. math. Soc., 178 (1973), 57-82.
[FL] P. Foulon and F. Labourie, Sur les variétés compactes asymptotiquement harmoniques, Invent. Math. 109 (1992), 97-111.
[Ga] L. Garnett, Foliations, the ergodic theorem and Brownian motion, J. Funct. Anal. 51 (1983), 285-311.
[Gu] Y. Guivarc'h, Sur la loi des grands nombres et le rayon spectral d'une marche aléatoire, Astérisque, 74 (1980) 47-98.
[HI] E. Heintze and H.-C. Im Hof, Geometry of horospheres, J. Diff. Geom. 12 (1977), 481-491.
[K] V. A. Kaimanovich, Brownian motion and harmonic functions on covering manifolds. An entropic approach, Soviet Math. Dokl. 33 (1986) 812-816.
[Ka] A. Katok, Four applications of conformal equivalence to geometry and dynamics, Ergod. Th. \& Dynam. Sys., $8^{*}$ (1988), 139-152.
[Kn] G. Knieper, On the asymptotic geometry of non-positively curved manifolds, GAFA, 7 (1997), 755-782.
[L1] F. Ledrappier, Harmonic measures and Bowen-Margulis measures, Israel J. Math. 71 (1990), 275-287.
[L2] F. Ledrappier, Applications of dynamics to compact manifolds of negative curvature, in Proceedings of the ICM Zürich 1994, Birkhäuser (1995), 1195-1202.
[L3] F. Ledrappier, Linear drift and entropy for regular covers, GAFA, 20 (2010), 710-725.
[LS] T. Lyons and D. Sullivan, Function theory, random paths and covering spaces, J. Differential Geometry, 19 (1984), 299-323.
[O] M.A. Olshanetsky, Martin boundary for the Laplace-Beltrami operator on a Riemannian symmetric space of non-positive curvature, Uspehi Mat. Nauk., 24:6 (1969), 189-190.
[Z] A. M. Zimmer, Asymptotically harmonic manifolds without focal points, preprint, (http://arxiv.org/abs/1109.2481),

LPMA, UMR CNRS 7599, Université Paris 6, Boîte Courrier 188, 4, Place Jussieu, 75252 PARIS cedex 05, France

Department of Mathematics, University of Notre Dame, Notre Dame, IN 46556, USA
E-mail address: fledrapp@nd.edu