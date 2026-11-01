---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2112_13466.pdf
converter: mathpix
format: mmd
---

\title{
ON THE DIRICHLET-TO-NEUMANN OPERATOR FOR THE CONNECTION LAPLACIAN
}

\author{
RAVIL GABDURAKHMANOV
}

\begin{abstract}
We study the relationship between the symbol of the Dirichlet-to-Neumann operator associated with a connection Laplacian, and the geometry on and near the boundary. As a consequence, we show that the geometric data on the boundary, and when the dimension of the base is greater than two all corresponding normal derivatives, are determined by the symbol.
\end{abstract}

\section*{1. Introduction}

Let $(N, g)$ be a compact connected Riemannian manifold with non-emtpy boundary $\partial N$, and let $E \rightarrow N$ be a Euclidean vector bundle endowed with a compatible connection $\nabla^{E}$. Consider the connection Laplacian $\Delta^{E}$ associated with the connection $\nabla^{E}$. It is a natural generalization of the Laplace-Beltrami operator. We define the corresponding Dirichlet-to-Neumann (DtN) operator $\Lambda_{g, \nabla^{E}}$ by sending a section $\sigma$ on the boundary $\partial N$ to the outward normal covariant derivative of its harmonic extension.

In this paper we study the DtN operator $\Lambda_{g, \nabla^{E}}$ as a pseudodifferential operator on the boundary. We follow the strategy in the paper [LeU] by Lee and Uhlmann for the Laplace-Beltrami operator. They showed that the Riemannian metric on the boundary can be recovered from a given DtN operator. In addition, if the dimension of the manifold is greater than 2, they showed that all the normal derivatives of the metric can be recovered as well. This result was used in [LeU] to recover a Riemannian manifold from the DtN operator under some assumptions on the geometry and topology of a manifold, and subsequently in [LU, LTU] under assumptions on the geometry only. This method also appears in the work of Cekić [C] on Calderon's problem for Yang-Mills connections.

It is well known that a Riemannian metric on a manifold can be recovered from the Laplacian. This can be done by considering the principal symbol of the Laplacian which is equal to $|\xi|_{g(x)}^{2}$, where $\xi \in T_{x}^{*} N, x \in N$. The Dirichlet-to-Neumann operator is a classical elliptic pseudodifferential operator of order one on the boundary. Therefore, it is natural to use the same idea for the recovery of the geometric data on the boundary from the DtN operator. There is a local factorization of the Laplacian into the composition of two operators near the boundary which establishes the relationship between the symbols of the DtN operator and Laplacian. In particular, it turns out that the principal symbol of the DtN operator is the (minus) square root of the principal symbol of the boundary Laplacian. Therefore, the principal symbol of the DtN operator is equal to $-|\xi|_{\left.g\right|_{\partial N}}$, and it is straightforward to determine the metric from it. The rest part of the symbol is expressed in terms of the local
geometric data in a more sophisticated way. By analyzing these expressions we are able to recover the geometric data on the boundary from the full symbol of the DtN operator. More precisely, we prove the following result.

Theorem 1.1. Suppose $\operatorname{dim} N=n \geq 3$. Let $\left(x^{1}, \ldots, x^{n-1}\right)$ be any local coordinates for an open set $W \subset \partial N$ and $\left(\epsilon_{1}, \ldots, \epsilon_{r}\right)$ any local frame of $E$ over $W$, and let $\left\{\lambda_{j}, j \leq 1\right\}$ be the full symbol of the DtN operator $\Lambda$ in these coordinates and local frame. For any $p \in W$, the full Taylor series of $g$ and $\nabla^{E}$ at $p$ in boundary normal coordinates and boundary normal frame is given by an explicit formula in terms of the matrix functions $\left\{\lambda_{j}\right\}$ and their tangential derivatives at $p$.

On surfaces, the DtN operator naturally scales under the conformal changes of a metric. As a consequence, we cannot recover the normal derivatives of a metric and a connection at the boundary. So the result in this case is a bit weaker.

Theorem 1.2. Let $(N, g)$ be a Riemannian surface. Let $\left(x^{1}\right)$ be any local coordinate for an open set $W \subset \partial N$ and $\left(\epsilon_{1}, \ldots, \epsilon_{r}\right)$ any local frame of $E$ over $W$. Let $\left\{\lambda_{j}, j \leq 1\right\}$ be the full symbol of the DtN operator $\Lambda$ in these coordinate and local frame. Then for any $p \in W$ the metric $g$ and the connection $\nabla^{E}$ at $p$ in these coordinate and frame is given by an explicit formula in terms of the matrix functions $\left\{\lambda_{j}\right\}$ and their tangential derivatives at $p$.

The structure of this paper is as follows. In Section 2 we recall some background material including the definition and properties of the connection Laplacian and associated DtN operator. In Section 3 we obtain some provisional results such as a local representation of the connection Laplacian in boundary normal coordinates and boundary normal frame, the local factorization of the connection Laplacian in these coordinates, and the relation of this factorization to the DtN operator. We then use this results to prove Theorem 1.1. The relationship between the geometry of isomorphic vector bundles, where the isomorphism intertwines the DtN operators, and the discussion of the two-dimensional case conclude the section.

\section*{2. Background material}
2.1. Notation. Let $(N, g)$ be a compact connected Riemannian manifold with boundary $\partial N$ and $\left(E, \nabla^{E}\right)$ be a vector bundle over $N$ of rank $r$ with a connection $\nabla^{E}: \Gamma(E) \rightarrow \Gamma\left(E \otimes T^{*} N\right)$. We assume that $E$ is equipped with a compatible inner product $\langle\cdot, \cdot\rangle_{E}$, the relation
$$d\langle u, v\rangle_{E}=\left\langle\nabla^{E} u, v\right\rangle_{E}+\left\langle u, \nabla^{E} v\right\rangle_{E}$$
holds for any pair of smooth sections $u, v \in \Gamma(E)$. Note that both sides of the above identity are differential forms. We use the standard notation $\Gamma(E)$ for $C^{\infty}$-smooth sections of a vector bundle $E$, and $H^{s}(E)$ for $H^{s}$-smooth sections, where $H^{s}=W^{s, 2}$ and $W^{s, p}$ denotes the $(s, p)$ -Sobolev space. Note that in this notation $H^{0}(E)=L^{2}(E)$. The space of test sections of $E$ is denoted as usually by $\mathcal{D}(E)$. The continuous dual of this space is denoted by $\mathcal{D}^{\prime}(E)$.

We can define the $L^{2}$-inner product of sections by
$$\langle u, v\rangle_{L^{2}}=\int_{N}\langle u, v\rangle_{E} d V_{g},$$
where $d V_{g}$ is the Riemannian volume measure of $(N, g)$. Similarly, we can define the $L^{2}$-inner product in $\Gamma\left(E \otimes T^{*} N\right)$ by
$$\langle\alpha, \beta\rangle_{L^{2}\left(E \otimes T^{*} N\right)}=\int_{N} \operatorname{Tr}_{g}\langle\alpha, \beta\rangle_{E} d V_{g}$$
where the sections $\alpha, \beta \in \Gamma\left(E \otimes T^{*} N\right)$ considered as the $E$-valued 1-forms.
Let us consider the connection Laplacian $\Delta^{E}$ defined by
$$\triangle^{E}=-\operatorname{Tr}_{g} \bar{\nabla}^{E} \nabla^{E},$$
where $\bar{\nabla}^{E}=\nabla^{E} \otimes \nabla^{L C}: \Gamma\left(E \otimes T^{*} N\right) \rightarrow \Gamma\left(E \otimes T^{*} N \otimes T^{*} N\right)$ and $\nabla^{L C}$ is the Levi-Civita connection on $(N, g)$. Note that we have the following equality [EL]
$$\triangle^{E}=\left(\nabla^{E}\right)^{*} \nabla^{E},$$
where $\left(\nabla^{E}\right)^{*}$ is the adjoint of $\nabla^{E}$ with respect to the $L_{2}$-inner products defined above. We will occasionally omit the word "connection" and call this operator the Laplacian for brevity. When it will not make any confusion, we will also sometimes omit the superscript $E$ in the notation of the connection $\nabla^{E}$.

Let us consider the Dirichlet problem for the Laplacian on a Euclidean vector bundle $E$ over a compact connected Riemannian manifold $(N, g)$ with boundary $\partial N$ :
$$\begin{cases}\triangle^{E} u=0 & \text { on } N, \\ \left.u\right|_{\partial N}=\sigma & u \in \Gamma(E), \sigma \in \Gamma\left(\left.E\right|_{\partial N}\right) .\end{cases}$$
It has a unique solution for every $\sigma \in \Gamma\left(\left.E\right|_{\partial N}\right)$. We briefly explain why this is true in the next section. Now this allows us to introduce the Dirichlet-to-Neumann operator $\Lambda_{g, \nabla^{E}}$ : $\Gamma\left(\left.E\right|_{\partial N}\right) \rightarrow \Gamma\left(\left.E\right|_{\partial N}\right)$ associated with the connection Laplacian $\nabla^{E}$ by
$$\Lambda_{g, \nabla^{E}} \sigma=\left.\nabla_{\nu}^{E} u\right|_{\partial N},$$
where $u$ is the solution to 2.1, and $\nu$ is the outward unit normal vector field on $\partial N$.
2.2. Discussion on the Dirichlet problem. We start with well-known Green's identities. Let $w \in \Gamma\left(E \otimes T^{*} N\right)$ and $v \in \Gamma(E)$. Then we have the first Green's identity
$$\left\langle\nabla^{*} w, v\right\rangle_{L^{2}}-\langle w, \nabla v\rangle_{L^{2}\left(E \otimes T^{*} N\right)}=\int_{\partial N}\left\langle\iota_{\nu} w, v\right\rangle d S_{g},$$
where $d S_{g}$ is the associated volume form on the boundary $\partial N$, and $\nu$ is the outward unit normal vector field on $\partial N$. Now let $w=\nabla u$, where $u \in \Gamma(E)$. Then we obtain the following
identity for the Laplacian
$$\left\langle\triangle^{E} u, v\right\rangle_{L^{2}}=\left\langle\nabla^{*} \nabla u, v\right\rangle_{L^{2}}=\langle\nabla u, \nabla v\rangle_{L^{2}\left(E \otimes T^{*} N\right)}+\int_{\partial N}\left\langle\iota_{\nu} \nabla u, v\right\rangle d S_{g},$$
which gives us the second Green's identity
$$\left\langle\Delta^{E} u, v\right\rangle_{L^{2}}-\left\langle u, \Delta^{E} v\right\rangle_{L^{2}}=\int_{\partial N}\left\langle\iota_{\nu} \nabla u, v\right\rangle d S_{g}-\int_{\partial N}\left\langle u, \iota_{\nu} \nabla v\right\rangle d S_{g} .$$

From (2.2) we conclude that the kernel of the Dirichlet Laplacian is zero, since
$$0=\left\langle\triangle^{E} u, u\right\rangle_{L^{2}}=\langle\nabla u, \nabla u\rangle_{L^{2}\left(E \otimes T^{*} N\right)}+\int_{\partial N}\left\langle\iota_{\nu} \nabla u, u\right\rangle d S_{g}=\langle\nabla u, \nabla u\rangle_{L^{2}\left(E \otimes T^{*} N\right)}=\|\nabla u\|_{L^{2}\left(E \otimes T^{*} N\right)},$$
which implies
$$\nabla u=0,$$
and therefore
$$d\langle u, u\rangle_{E}=2\langle\nabla u, u\rangle_{E}=0 .$$
From this we conclude that $\langle u, u\rangle_{E}$ is constant on $N$ and since $u$ vanishes on the boundary it has to be identically zero on the whole manifold $N$. It is clear that this implies the uniqueness of the solution to the boundary value problem (2.1).

The existence of the solution can be shown in two steps. First, we use the Lax-Milgram theorem to prove the existence of a weak solution to the Dirichlet problem
$$\left\{\begin{array}{l}
\Delta^{E} u=-\Delta^{E} \tilde{\sigma}, \quad u \in H^{1}(E), \\
\left.u\right|_{\partial N}=0,
\end{array}\right.$$
where $\tilde{\sigma} \in H^{1}(E)$ in the right hand side is a given function. Then we use the elliptic regularity to show that this solution is smooth if $\tilde{\sigma}$ is. Below we briefly discuss both steps.

Let us recall the Lax-Milgram theorem [E].
Theorem (Lax-Milgram). Let $V$ be a Hilbert space and a $(\cdot, \cdot)$ a bilinear form on $V$, which is
\begin{itemize}
\item[(1)] Bounded: $|a(u, v)| \leq C\|u\|\|v\|$ and
\item[(2)] Coercive: $|a(u, u)| \geq c\|u\|^{2}$.
\end{itemize}

Then for any continuous linear functional $f \in V^{\prime}$ there is a unique solution $u \in V$ to the equation
$$a(u, v)=f(v), \forall v \in V$$
and the following inequality holds
$$\|u\| \leq \frac{1}{c}\|f\|_{V^{\prime}} .$$

Let $\stackrel{\circ}{H}^{1}(E):=\stackrel{\circ}{H}^{1,2}(E)$ denotes the Sobolev space of sections vanishing on the boundary $\partial N$. Consider a bilinear form $a(\cdot, \cdot)$ which acts on $u, v \in \stackrel{\circ}{H}^{1}(E)$ as
$$a(u, v)=\langle\nabla u, \nabla v\rangle_{L^{2}\left(E \otimes T^{*} N\right)} .$$
We see that $a(u, v)$ is a bounded bilinear form on $\stackrel{\circ}{H}^{1}(E)$. For a given $\tilde{\sigma} \in H^{1}(E)$ let us take the functional
$$f_{\tilde{\sigma}}(v)=-\langle\nabla \tilde{\sigma}, \nabla v\rangle_{L^{2}\left(E \otimes T^{*} N\right)} .$$
Clearly, this is a bounded linear functional on $\stackrel{\circ}{H}^{1}(E)$. So it is left to show that $a(u, v)$ is coercive, i.e. there exists $c$ such that
$$\frac{\|\nabla u\|_{L^{2}\left(E \otimes T^{*} N\right)}^{2}}{\|u\|_{L^{2}}^{2}} \geq c>0 .$$
This follows, for instance, from the Sobolev embedding theorem [N]. We showed that all the conditions of the Lax-Milgram theorem are satisfied, therefore, there is a unique weak solution $u \in \stackrel{\circ}{H}^{1}(E)$ to (2.4). Let us now state the elliptic regularity theorem (see, for example, [N]).

Theorem (Elliptic regularity). Suppose $\varphi \in H^{s}(E)$ (smooth), and $u \in \mathscr{D}^{\prime}(E)$ solves the equation
$$\triangle^{E} u=\varphi .$$
Then $u \in H^{s+2}(E)$ (respectively smooth).
Using this theorem we conclude that if $\tilde{\sigma}$ is smooth then the solution $u$ to (2.4) is also smooth.

To obtain the solution to the boundary value problem (2.1) we take a smooth extension $\tilde{\sigma} \in \Gamma(E)$ of $\sigma$, and write $u=w+\tilde{\sigma}$. We see that
$$\left\{\begin{array}{l}
\Delta^{E} u=\Delta^{E} w+\Delta^{E} \tilde{\sigma}, \\
\left.u\right|_{\partial N}=\left.w\right|_{\partial N}+\left.\tilde{\sigma}\right|_{\partial N}=\left.w\right|_{\partial N}+\sigma .
\end{array}\right.$$
Now if $w$ is the solution to (2.4), then $u$ is the solution to (2.1). Note that the restriction to the boundary extends to the trace map
$$\mathcal{T}: H^{s}(E) \rightarrow H^{s-\frac{1}{2}}\left(\left.E\right|_{\partial N}\right),$$
which has the right inverse
$$\mathcal{E}: H^{s-\frac{1}{2}}\left(\left.E\right|_{\partial N}\right) \rightarrow H^{s}(E),$$
i.e. the map such that the equality $\mathcal{T} \circ \mathcal{E}=I d$ holds; both maps are linear bounded operators. Using this we can show the existence and uniqueness of the solution to the boundary value problem
$$\begin{cases}\triangle^{E} u=0, & u \in H^{s+\frac{1}{2}}(E), \\ \mathcal{T}(u)=\sigma, & \sigma \in H^{s}\left(\left.E\right|_{\partial N}\right),\end{cases}$$
for $s \geq \frac{1}{2}$. Note that from the elliptic regularity the solution $u$ is smooth in the interior of $N$.

Let us now consider the complexification $\mathbb{C} \otimes E \simeq E \oplus i E$ of the Euclidean vector bundle $E$. It has a natural structure of Hermitian vector bundle and a compatible connection $\nabla=$ $\nabla^{E} \oplus \nabla^{E}$. The associated Laplacian is
$$\triangle=\triangle^{E} \oplus \triangle^{E},$$
and we see that the complex analogue of problem (2.7) decomposes into two real ones. So all the results on the existence and uniqueness are straightforward from the real case. We will further assume the complexified objects (vector bundle, connection, Laplacian) and use the same notation for them as for their real counterparts.
2.3. Pseudodifferential operators on vector bundles. In this section we will recall the definition of a (standard) pseudodifferential operator (PDO) on vector bundles. In this section we follow the exposition by Treves in [T]. Let $\Omega$ be an open subset of $\mathbb{R}^{n}$. We need first to define the special class of functions called amplitudes. Let $m$ be any real number. We shall denote by $S^{m}(\Omega, \Omega)$ the linear space of $C^{\infty}$ functions in $\Omega \times \Omega \times \mathbb{R}^{n}, a(x, y, \xi)$, which have the following property:

To every compact subset $\mathscr{K}$ of $\Omega \times \Omega$ and to every triplet of $n$-tuples $\alpha, \beta, \gamma$, there is a constant $C_{\alpha, \beta, \gamma}(\mathscr{K})>0$ such that
$$\left|D_{\xi}^{\alpha} D_{x}^{\beta} D_{y}^{\gamma} a(x, y, \xi)\right| \leq C_{\alpha, \beta, \gamma}(\mathscr{K})(1+|\xi|)^{m-|\alpha|}, \forall(x, y) \in \mathscr{K}, \text { and } \forall \xi \in \mathbb{R}^{n},$$
where $D_{z_{i}}:=-i \partial_{z_{i}}$. The elements of $S^{m}(\Omega, \Omega)$ are called amplitudes of degree $\leq m($ in $\Omega \times \Omega)$. The space $S^{m}(\Omega, \Omega)$ is endowed with a natural locally convex topology: denote by $\mathfrak{p} \mathscr{K} ; \alpha, \beta, \gamma(a)$ the infimum of the constants $C_{\alpha, \beta, \gamma}(\mathscr{K})$ such that (2.8) is true. One can see then that the function $\mathfrak{p}_{\mathscr{K} ; \alpha, \beta, \gamma}$ is a seminorm on $S^{m}(\Omega, \Omega)$ and defines the topology of this space when $\mathscr{K}$ ranges over the collection of all compact subsets of $\Omega$ and $\alpha, \beta, \gamma$ over that of all $n$-tuples. Thus topologized, $S^{m}(\Omega, \Omega)$ is a Frï $_{\text {¿ }}$ œchet space. We denote the subspace of amplitudes independent of $y$ by $S^{m}(\Omega)$ and regard its elements as smooth functions in $\Omega \times \mathbb{R}^{n}$ (rather than in $\Omega \times \Omega \times \mathbb{R}^{n}$ ). The topology on $S^{m}(\Omega)$ is the induced subspace topology from $S^{m}(\Omega, \Omega)$. Hence, $S^{m}(\Omega)$ is a $\mathrm{Fr}_{i}$ œchet space, as a closed linear subspace of the $\mathrm{Fr}_{i}$ œchet space. The intersection of all $S^{m}(\Omega)$ is denoted by $S^{-\infty}(\Omega)$. The quotient vector space $S^{m}(\Omega) / S^{-\infty}(\Omega)$ is denoted by $\dot{S}^{m}(\Omega)$ and its elements are called symbols of degree $\leq m$. We use the term symbol for a representative $\left(\in S^{m}(\Omega)\right)$ of an equivalence class in $\dot{S}^{m}(\Omega)$ as well. We will also need the notion of a formal symbol. By a formal symbol we mean a sequence of symbols $a_{m_{j}} \in S^{m_{j}}(\Omega)$ whose orders $m_{j}$ are strictly decreasing and converging to $-\infty$. It is standard to represent it by the formal series
$$\sum_{j=0}^{+\infty} a_{m_{j}}(x, \xi) .$$

From such a formal symbol one can build true symbols, elements of $S^{m_{0}}(\Omega)$ in the present case, which all belong to the same class modulo $S^{-\infty}(\Omega)$. We will denote this class by (2.9). In order to construct a true symbol one may proceed as follows:

First, one may state that a symbol $a(x, \xi)$ belongs to the class (2.9) if, given any large positive number $M$, there is an integer $J \geq 0$ such that
$$a(x, \xi)-\sum_{j=0}^{J} a_{m_{j}}(x, \xi) \in S^{-M}(\Omega) .$$
Second, one can construct such a symbol $a(x, \xi)$ as a sum of a series
$$\sum_{j=0}^{+\infty} \chi_{j}(\xi) a_{m_{j}}(x, \xi),$$
where $\chi_{j}(\xi)$ are suitable cutoff functions. By suitable we mean such that the above series converges in the space $S^{m_{0}}(\Omega)$. Note that since we are using the cutoff functions we are able to deal with terms $a_{m_{j}}(x, \xi)$ that are not "true" elements of $S^{m_{j}}(\Omega)$, e.g. the functions that are non-smooth or even not defined in neighborhoods of the origin $\xi=0$. (If such neighborhoods depend on $x$ we may consider the cutoff functions that also depend on $x$ ). The most important examples of formal symbols (2.9) with terms $a_{m_{j}}(x, \xi)$ that are not $C^{\infty}$ functions of $\xi$ at the origin are the classical symbols. The formal symbol (2.9) is called the classical symbol if each term $a_{m_{j}}(x, \xi)$ is a positive-homogeneous function of degree $m_{j}$ of $\xi$ and if differences $m_{j}-m_{j+1} \in \mathbb{Z}^{+}$, for all $j$. Recall that a function $f(\xi)$ is called positive-homogeneous of degree $d$ with respect to $\xi$ in $\mathbb{R}^{n} \backslash\{0\}$ if $f(\rho \xi)=\rho^{d} f(\xi)$ for every $\rho>0$ (but not necessarily for every real $\rho$ ). For instance, the Heaviside function on $\mathbb{R} \backslash\{0\}$ is positive-homogeneous, but not homogeneous, of degree zero.

Let us continue with the definition of a (standard) PDO. A linear operator $A: \mathscr{E}^{\prime}(\Omega) \rightarrow$ $\mathscr{D}^{\prime}(\Omega)$ is called a (standard) pseudodifferential operator of order $m$ if there is an amplitude $a \in S^{m}(\Omega, \Omega)$ such that $A$ can be represented in the form
$$A u(x)=(2 \pi)^{-n} \iint e^{i(x-y) \cdot \xi} a(x, y, \xi) u(y) d y d \xi .$$

Now we are able to define pseudodifferential operators acting on vector-valued distributions. Let $\mathbb{F}^{n}$ be a $n$-dimensional vector space over field $\mathbb{F}(=\mathbb{R}, \mathbb{C})$. Let $\mathscr{D}^{\prime}\left(\Omega ; \mathbb{F}^{n}\right)\left(\mathscr{E}^{\prime}\left(\Omega ; \mathbb{F}^{n}\right)\right)$ denote the space of (compactly supported) distributions in $\Omega$. Note that if we chose basis in $\mathbb{F}^{n}$ then a $\mathbb{F}^{n}$-valued distribution is a vector with coordinates consisting of $n$ scalar distributions. Using this we can give the following natural definition. A linear operator $A: \mathscr{E}^{\prime}\left(\Omega ; \mathbb{F}^{r}\right) \rightarrow \mathscr{D}^{\prime}\left(\Omega ; \mathbb{F}^{l}\right)$ is called a pseudodifferential operator if in any bases of $\mathbb{F}^{r}$ and $\mathbb{F}^{l}$ it is represented by a matrix of scalar pseudodifferential operators.

Let $F_{1}$ and $F_{2}$ be two vector bundles over a smooth manifold $N$ with fibers $\mathbb{F}^{r}$ and $\mathbb{F}^{l}$, respectively. Note that any $F_{i}$-valued distribution $(i=1,2)$ in any local trivialization is represented by a vector with coordinates being scalar distributions. This allows to represent
any linear operator $\Gamma\left(F_{1}\right) \rightarrow \Gamma\left(F_{2}\right)$ in any local trivializations as an $l \times r$-matrix of linear operators $C^{\infty}(N) \rightarrow C^{\infty}(N)$. Therefore, it is natural to give the following definition.

Definition. A linear operator $A: \mathscr{E}^{\prime}\left(F_{1}\right) \rightarrow \mathscr{D}^{\prime}\left(F_{2}\right)$ is called a pseudodifferential operator (of order $m$ ) if in any pair of local trivializations it is represented by a matrix of scalar pseudodifferential operators (of order $m$ ).

If vector bundles $F_{1}$ and $F_{2}$ are equal to the vector bundle $F$, then we say that $A$ is a PDO (acting) on a vector bundle $F$. Due to this definition most of the theory for scalar PDOs generalizes to this case naturally, e.g. the symbol calculus. In particular, if $A$ and $B$ are two PDOs on vector bundle $F$, then the symbol of the composition $A \circ B$ is defined by the formal symbol
$$\sum_{\alpha} \frac{1}{\alpha!} \partial_{\xi}^{\alpha} a(x, \xi) D_{x}^{\alpha} b(x, \xi),$$
where $a(x, \xi)$ and $b(x, \xi)$ are the symbols of $A$ and $B$, respectively.
We shall say that a PDO $A$ is smoothing if it maps $\mathscr{E}^{\prime}(\Omega)$ to $C^{\infty}(\Omega)$. In order for this to be the case, it is necessary and sufficient for the associated kernel $K_{A}(x, y)$ to be $C^{\infty}$ in $\Omega \times \Omega$.

\subsection*{2.4. Well-posedness of the generalized heat equation and regularity of its solution.}

In this subsection we describe the result by Treves [T, III.1]. In order to be precise we introduce the original setting. Let $X$ be a smooth manifold; $n=\operatorname{dim} X ; t$ be the variable in the closed half-line $\overline{\mathbb{R}}_{+} ; T$ be some positive real number.

We shall deal with functions and distributions valued in a finite-dimensional Hilbert space $H$ over $\mathbb{C}$. The norm in $H$ will be denoted by $|\cdot|_{H}$, whereas the operator norm in $L(H)$, the space of (bounded) linear operators in $H$, will be denoted by $\|\cdot\|$. The inner product in $H$ will be denoted by $(\cdot, \cdot)_{H}$. The space of $H$-valued distributions in $X$ will be denoted by $\mathscr{D}^{\prime}(X ; H)$.

Let $A(t)$ be a pseudodifferential operator of order 1 in $X$, valued in $L(H)$, depending smoothly on $t \in[0, T)$. If we fix basis in $H$, then $A(t)$ is a matrix whose entries are scalar pseudodifferential operators in $X$. This means that in every local chart $\left(\Omega, x_{1}, \ldots, x_{n}\right), A(t)$ is congruent modulo smoothing operators which are $C^{\infty}$-functions of $t$ to an operator
$$A_{\Omega}(t) u(x)=(2 \pi)^{-n} \int e^{i x \cdot \xi} a_{\Omega}(x, t, \xi) \hat{u}(\xi) d \xi, \quad u \in C_{c}^{\infty}(\Omega ; H),$$
where $a_{\Omega}(x, t, \xi)$ is a smooth function of $t \in[0, T)$ valued in $S^{1}(\Omega ; L(H))$, the space of symbols valued in $L(H)$.

According to Treves [T, III.1], the heat equation for $A(t)$ is well-posed and possesses a regularity property described below if the following conditions are satisfied:
\begin{itemize}
\item[(1)] Let $\left(\Omega, x_{1}, \ldots, x_{n}\right)$ be any local chart in $X$. There is a symbol $a_{\Omega}(x, t, \xi)$ satisfying
$$a_{\Omega}(x, t, \xi) \text { is a } C^{\infty} \text { function of } t \in[0, T) \text { valued in } S^{1}(\Omega ; L(H)),$$
\end{itemize}
\begin{itemize}
\item[] and defining the operator $A_{\Omega}(t)$ congruent to $A(t)$ modulo smoothing operators in $\Omega$ depending smoothly on $t \in[0, T)$, such that
\item[(2)] to every compact subset $K$ of $\Omega \times[0, T)$ there is a compact subset $K^{\prime}$ of the open half-plane $\mathbb{C}_{-}=\{z \in \mathbb{C} ; \operatorname{Re} z<0\}$ such that
\item[(3)] the map
$$z \cdot I d-\frac{a_{\Omega}(x, t, \xi)}{\left(1+|\xi|^{2}\right)^{1 / 2}}: H \rightarrow H$$
is a bijection (hence also a homeomorphism), for all $(x, t) \in K, \xi \in \mathbb{R}^{n}, z \in \mathbb{C} \backslash K^{\prime}$.
\end{itemize}

The regularity property that we are interested in is described in the following theorem [T, III, Theorem 1.2].

Theorem 2.1. Let $\mathscr{O}$ be an open subset of $X$, $u$ a $C^{\infty}$ function of $t$ in $[0, T)$ valued in $\mathscr{D}^{\prime}(X ; H)$. Suppose that $u(0) \in C^{\infty}(\mathscr{O} ; H)$ and that
$$\frac{\partial u}{\partial t}-A(t) u \in C^{\infty}(\mathscr{O} \times[0, T) ; H) .$$
Then $u \in C^{\infty}(\mathscr{O} \times[0, T) ; H)$.
This theorem is one of the main ingredients in the proof of Proposition 3.4, which relates the symbol of the DtN operator to the symbol of the connection Laplacian.

\section*{3. Reconstruction of the geometric data on the boundary}

In this section we find the relation between full symbols of the DtN operator and the connection Laplacian, and then use this relation to prove Theorem 1.1. We follow the general strategy used in [LeU] for the DtN operator associated with the Laplace-Beltrami operator.
3.1. Local factorization of the connection Laplacian. Let us recall the construction of geodesic coordinates with respect to the boundary. For each $q \in \partial N$, let $\gamma_{q}:[0, \epsilon) \rightarrow N$ denote the unit-speed geodesic starting at $q$ and normal to $\partial N$. If $\left\{x^{1}, \ldots, x^{n-1}\right\}$ are any local coordinates for $\partial N$ near $p \in \partial N$, we can extend them smoothly to functions on a neighborhood of $p$ in $N$ by letting them be constant along each normal geodesic $\gamma_{q}$. If we then define $x^{n}$ to be the parameter along each $\gamma_{q}$, it follows that $\left\{x^{1}, \ldots, x^{n}\right\}$ form coordinates for $N$ in some neighborhood of $p$, which we call the boundary normal coordinates determined by $\left\{x^{1}, \ldots, x^{n-1}\right\}$. In these coordinates $x^{n}>0$ in the interior of $N$, and $\partial N$ is locally characterized by $x^{n}=0$. The metric in these coordinates has the form
$$g=\sum_{i, j=1}^{n-1} g_{i j}\left(x^{1}, \ldots, x^{n}\right) d x^{i} d x^{j}+\left(d x^{n}\right)^{2} .$$
Let $\left(\epsilon_{1}, \ldots, \epsilon_{r}\right)$ be a smooth local frame of $\left.E\right|_{\partial N}$ near $p \in \partial N$, we can extend it to a smooth local frame $\left(\varepsilon_{1}, \ldots, \varepsilon_{r}\right)$ in a neighborhood of $p$ in $N$ by means of parallel transport along each
$\gamma_{q}$, i.e. for each $q$ we find the unique solution to the parallel transport equation
$$\begin{aligned}
\nabla_{\dot{\gamma}_{q}}^{E} \varepsilon_{\alpha} & =0, \\
\left.\varepsilon_{\alpha}\right|_{\gamma_{q}(0)} & =\epsilon_{\alpha}, \text { for } \alpha=1, \ldots, r .
\end{aligned}$$
We call this frame the boundary normal frame determined by $\left(\epsilon_{1}, \ldots, \epsilon_{r}\right)$. In boundary normal coordinates we have then
$$\nabla_{\partial / \partial x^{n}}^{E} \varepsilon_{\alpha}=0 .$$
In local frame a section $u$ is represented as a vector-valued function on $N$ and the connection $\nabla^{E}$ acts as
$$\nabla^{E} u=d u(\cdot)+\omega(\cdot) u,$$
where $\omega=\omega_{k} d x^{k}$ denotes the matrix of connection forms of $\nabla^{E}$. From (3.1) we have then
$$\omega_{n}=\omega\left(\frac{\partial}{\partial x^{n}}\right)=0 .$$

Remark 3.1. If the connection $\nabla^{E}$ is compatible with an inner product $\langle\cdot, \cdot\rangle_{E}$ on $E$, we have the following relation
$$d\langle u, v\rangle_{E}=\left\langle\nabla^{E} u, v\right\rangle_{E}+\left\langle u, \nabla^{E} v\right\rangle_{E} .$$
Note that if the frame $\left(\epsilon_{1}, \ldots, \epsilon_{r}\right)$ is orthonormal then the associated boundary normal frame is also orthonormal, since we have
$$\begin{gathered}
\frac{\partial}{\partial t}\left\langle\varepsilon_{\alpha}, \varepsilon_{\beta}\right\rangle_{E}=\left\langle\nabla_{\dot{\gamma}}^{E} \varepsilon_{\alpha}, \varepsilon_{\beta}\right\rangle_{E}+\left\langle\varepsilon_{\alpha}, \nabla_{\dot{\gamma}}^{E} \varepsilon_{\beta}\right\rangle_{E}=0 \\
\left.\left\langle\varepsilon_{\alpha}, \varepsilon_{\beta}\right\rangle_{E}\right|_{t=0}=\left\langle\epsilon_{\alpha}, \epsilon_{\beta}\right\rangle_{E}=0, \alpha \neq \beta, \\
\left.\left\langle\varepsilon_{\alpha}, \varepsilon_{\alpha}\right\rangle_{E}\right|_{t=0}=\left\langle\epsilon_{\alpha}, \epsilon_{\alpha}\right\rangle_{E}=1 .
\end{gathered}$$
And applying (3.2) to an orthonormal frame we obtain
$$\begin{aligned}
0=\frac{\partial}{\partial x^{i}}\left\langle\varepsilon_{\alpha}, \varepsilon_{\beta}\right\rangle_{E}=\left\langle\varepsilon_{\tau} \omega_{\alpha}^{\tau}\right. & \left.\left(\frac{\partial}{\partial x^{i}}\right), \varepsilon_{\beta}\right\rangle_{E}+\left\langle\varepsilon_{\alpha}, \varepsilon_{\tau} \omega_{\beta}^{\tau}\left(\frac{\partial}{\partial x^{i}}\right)\right\rangle_{E}= \\
& \left\langle\varepsilon_{\tau}, \varepsilon_{\beta}\right\rangle_{E}\left(\omega_{\alpha}^{\tau}\right)_{i}+\left\langle\varepsilon_{\alpha}, \varepsilon_{\tau}\right\rangle_{E}\left(\omega_{\beta}^{\tau}\right)_{i}=\left(\omega_{\alpha}^{\beta}\right)_{i}+\left(\omega_{\beta}^{\alpha}\right)_{i}, \text { for } i=1, \ldots, n,
\end{aligned}$$
and we see that $\left(\omega_{\beta}^{\alpha}\right)_{i}=-\left(\omega_{\alpha}^{\beta}\right)_{i}$, i.e. the connection form is skew-symmetric.

We will use further the following notation, $x=\left(x^{\prime}, x^{n}\right), x^{\prime}=\left(x^{1}, \ldots, x^{n-1}\right), \partial_{x^{j}}=\partial / \partial x^{j}$, $D_{x^{j}}=-i \partial_{x^{j}}$, and $D_{x}=\left(D_{x^{1}}, \ldots, D_{x^{n}}\right)$, with similar definitions for $D_{x^{\prime}}, \partial_{x}$, and $\partial_{x^{\prime}}$. The Einstein summation convention will be assumed throughout this section.

In boundary normal coordinates and boundary normal frame, the connection Laplacian is
$$\triangle^{E} u=\triangle u+g^{i j}\left[2 \omega_{i} \partial_{x^{j}} u+\left(\left(\nabla_{\partial_{x^{i}}} \omega\right)\left(\partial_{x^{j}}\right)+\omega_{i} \omega_{j}\right) u\right],$$
where $\left(g^{i j}\right)$ is the inverse of the matrix $\left(g_{i j}\right), \triangle$ is the (scalar) Laplace-Beltrami operator on $N$. We can write
$$L u:=\Delta^{E} u=\left[\triangle+i \sum_{j=1}^{n-1} V^{j} D_{x^{j}}+\tilde{Q}\right] u,$$
where
$$\begin{aligned}
V^{j} & =2 g^{j k} \omega_{k}, j=1, \ldots, n-1 \\
\tilde{Q} & =\sum_{i, j=1}^{n-1} g^{i j}\left[\left(\nabla_{\partial_{x^{i}}} \omega\right)\left(\partial_{x^{j}}\right)+\omega_{i} \omega_{j}\right] .
\end{aligned}$$

The Laplace-Beltrami operator in boundary normal coordinates can be written as
$$\begin{aligned}
\Delta u=\sum_{i, j=1}^{n} \varrho^{-1 / 2} \partial_{x^{i}}\left(\varrho^{1 / 2} g^{i j} u\right)=\partial_{x^{n}} \partial_{x^{n}} u & +\frac{1}{2}\left(\partial_{x^{n}} \log \varrho\right) \partial_{x^{n}} u+ \\
& +\sum_{i, j=1}^{n-1}\left(g^{i j} \partial_{x^{i}} \partial_{x^{j}} u+\frac{1}{2} g^{i j}\left(\partial_{x^{i}} \log \varrho\right) \partial_{x^{j}} u+\left(\partial_{x^{i}} g^{i j}\right) \partial_{x^{j}} u\right),
\end{aligned}$$
where $\varrho=\operatorname{det}\left(g_{i j}\right)$. Using this we can write
$$-L=-\triangle-i V^{l} D_{x^{l}}-\tilde{Q}=D_{x^{n}}^{2}+i F(x) D_{x^{n}}+Q\left(x, D_{x^{\prime}}\right),$$
where
$$\begin{aligned}
F(x) & =-\frac{1}{2} \sum_{k, l=1}^{n-1} g^{k l}(x) \partial_{x^{n}} g_{k l}(x), \\
Q\left(x, D_{x^{\prime}}\right) & =\sum_{k, l=1}^{n-1} g^{k l}(x) D_{x^{k}} D_{x^{l}}-i \sum_{k, l=1}^{n-1}\left(\frac{1}{2} g^{k l}(x) \partial_{x^{n}} \log \varrho(x)+\partial_{x^{n}} g^{k l}(x)+V^{l}\right) D_{x^{l}}-\tilde{Q} .
\end{aligned}$$

The Dirichlet-to-Neumann operator in boundary normal coordinates and boundary normal frame is
$$\Lambda_{g, \nabla^{E}} \sigma=\left.\nabla_{\nu}^{E} u\right|_{\partial N}=\left.\left(\frac{\partial}{\partial x^{n}}+\omega_{n}\right) u\right|_{\partial N}=\left.\frac{\partial u}{\partial x^{n}}\right|_{\partial N} .$$
The next Proposition shows that there is a useful local factorization of the Laplacian into a composition of two first-order pseudodifferential operators.

Proposition 3.2. There exists a pseudodifferential operator $A\left(x, D_{x^{\prime}}\right)$ of order one in $x^{\prime}$ depending smoothly on $x^{n} \in[0, T]$, for some $T>0$, such that
$$-L \equiv\left(D_{x^{n}}+i F(x)-i A\left(x, D_{x^{\prime}}\right)\right) \circ\left(D_{x^{n}}+i A\left(x, D_{x^{\prime}}\right)\right)$$
modulo a smoothing operator.

Proof. We use the symbol calculus to construct such an operator $A\left(x, D_{x^{\prime}}\right)$. From (3.3) we get
$$\begin{aligned}
L+\left(D_{x^{n}}+i F-i A\right) \circ\left(D_{x^{n}}\right. & +i A)=-D_{x^{n}}^{2}-i F D_{x^{n}}-Q+D_{x^{n}}^{2}+i F D_{x^{n}}- \\
& -i A D_{x^{n}}+i D_{x^{n}} A-F A+A A=A A-Q+i\left[D_{x^{n}}, A\right]-F A .
\end{aligned}$$
Let $a$ denote the full symbol of $A\left(x, D_{x^{\prime}}\right)$ and $q$ denote the full symbol of $Q\left(x, D_{x^{\prime}}\right)$. Then, by (2.10) the full symbol of (3.6) is
$$\sum_{K} \frac{1}{K!} \partial_{\xi}^{K} a D_{x}^{K} a-q+\partial_{x^{n}} a-F a,$$
and $q$ splits into three terms
$$\begin{aligned}
q\left(x, \xi^{\prime}\right)=\sum_{k, l=1}^{n-1} g^{k l}(x) \xi_{k} \xi_{l}- & \\
-i \sum_{l=1}^{n-1}\left[\sum_{k=1}^{n-1}\left(\frac{1}{2} g^{k l}(x) \partial_{x^{k}} \log \delta(x)+\partial_{x^{k}} g^{k l}(x)\right)\right. & \left.+V^{l}\right] \xi_{l}-\tilde{Q}= \\
& =q_{2}\left(x, \xi^{\prime}\right)+q_{1}\left(x, \xi^{\prime}\right)+q_{0}(x) .
\end{aligned}$$
Let us write
$$a\left(x, \xi^{\prime}\right) \sim \sum_{j \leq 1} a_{j}\left(x, \xi^{\prime}\right),$$
where $a_{j}$ are positive-homogeneous of degree $j$ in $\xi^{\prime}$, that is we will define $A$ by a formal symbol. We shall determine $a_{j}$ recursively so that (3.6) is zero modulo symbols of smoothing operators.

The homogeneous terms of degree two in (3.6) give us
$$a_{1} a_{1}-q_{2}=0,$$
so we can choose
$$a_{1}=-\sqrt{q_{2}} .$$
Note that $q_{2}$ and, therefore, also $a_{1}$ are scalar matrices. The terms of degree one in (3.6) give us
$$a_{0} a_{1}+a_{1} a_{0}+\sum_{l}^{n-1} \partial_{\xi^{l}} a_{1} D_{x^{l}} a_{1}-q_{1}+\partial_{x^{n}} a_{1}-F a_{1}=0,$$
and using relation (3.7), we get
$$-2 \sqrt{q_{2}} a_{0}+\sum_{l}^{n-1} \partial_{\xi^{l}} \sqrt{q_{2}} D_{x^{l}} \sqrt{q_{2}}-q_{1}-\partial_{x^{n}} \sqrt{q_{2}}+F \sqrt{q_{2}}=0$$
thus we have
$$a_{0}=\frac{1}{2 \sqrt{q_{2}}}\left[\sum_{l}^{n-1} \partial_{\xi^{l}} \sqrt{q_{2}} D_{x^{l}} \sqrt{q_{2}}-q_{1}-\partial_{x^{n}} \sqrt{q_{2}}+F \sqrt{q_{2}}\right] .$$
The terms of degree zero in (3.6) give us
$$\begin{aligned}
a_{-1} a_{1}+a_{1} a_{-1}+\sum_{l}^{n-1} \partial_{\xi^{l}} a_{1} D_{x^{l}} a_{0}+\sum_{l}^{n-1} \partial_{\xi^{l}} a_{0} & D_{x^{l}} a_{1}+ \\
& +\frac{1}{2} \sum_{k, l}^{n-1} \partial_{\xi^{k}} \partial_{\xi^{l}} a_{1} D_{x^{k}} D_{x^{l}} a_{1}-q_{0}+\partial_{x^{n}} a_{0}-F a_{0}=0,
\end{aligned}$$
and using relation (3.7) again, we get
$$\begin{aligned}
a_{-1}=\frac{1}{2 \sqrt{q_{2}}}\left[-\sum_{l}^{n-1} \partial_{\xi^{l}} \sqrt{q_{2}} D_{x^{l}} a_{0}-\sum_{l}^{n-1}\right. & \partial_{\xi^{l}} a_{0} D_{x^{l}} \sqrt{q_{2}}+ \\
& \left.+\frac{1}{2} \sum_{k, l}^{n-1} \partial_{\xi^{k}} \partial_{\xi^{l}} \sqrt{q_{2}} D_{x^{k}} D_{x^{l}} \sqrt{q_{2}}-q_{0}+\partial_{x^{n}} a_{0}-F a_{0}\right],
\end{aligned}$$
where $a_{0}$ is given by (3.8). Continuing the recursion for the terms of degree $m \leq-1$ we have
$$-2 \sqrt{q_{2}} a_{m-1}+\sum_{\substack{j, k, K \\ m \leq j, k \leq 1 \\|K|=j+k-m}} \frac{1}{K!} \partial_{\xi}^{K} a_{j} D_{x}^{K} a_{k}+\partial_{x^{n}} a_{m}-F a_{m}=0 .$$
Therefore we get
$$a_{m-1}=\frac{1}{2 \sqrt{q_{2}}}\left[\sum_{\substack{j, k, K \\ m \leq j, k \leq 1 \\|K|=j+k-m}} \frac{1}{K!} \partial_{\xi}^{K} a_{j} D_{x}^{K} a_{k}+\partial_{x^{n}} a_{m}-F a_{m}\right] .$$ \(\square\)

Remark 3.3. Let $p \in \partial N$. Note that we can extend $\left(N, g, E, \nabla^{E}\right)$ along the boundary $\partial N$ near $p$. This means that there is a vector bundle $\left(\tilde{E}, \nabla^{\tilde{E}}\right)$ over a Riemannian manifold $(\tilde{N}, \tilde{g})$ such that $N$ is included in $\tilde{N}$ isometrically, the restriction of $\left(\tilde{E}, \nabla^{\tilde{E}}\right)$ to $N$ coincides with $\left(E, \nabla^{E}\right)$, and the point $p$ lies in the interior of $\tilde{N}$. Clearly, near $p \in \tilde{N}$ there is an extension of boundary normal coordinates (so that $x^{n} \in(-\epsilon, \epsilon)$ ) and boundary normal frame. Due to the construction of $A\left(x, D_{x^{\prime}}\right)$ one sees that the factorization in Proposition 3.2 extends to a neighborhood of $p$ in $\tilde{N}$, i.e. there exists a PDO $\tilde{A}\left(x, D_{x^{\prime}}\right)$ of order one in $x^{\prime}$ depending smoothly on $x^{n} \in[-\tilde{T}, \tilde{T}]$, for some positive $\tilde{T}<T$, such that it coincides with $A\left(x, D_{x^{\prime}}\right)$ for $x^{n} \in[0, \tilde{T}]$.
3.2. The full symbol of the Dirichlet-to-Neumann operator $\Lambda_{g, \nabla^{E}}$. Our next step is to relate the operator $A\left(x, D_{x^{\prime}}\right)$ with the Dirichlet-to-Neumann operator $\Lambda_{g, \nabla^{E}}$. It turns out that this relation is quite simple.

Proposition 3.4. The operator A satisfies the following relation
$$\left.\left.A\left(x, D_{x^{\prime}}\right)\right|_{\partial N} \sigma \equiv \partial_{x^{n}} u\right|_{\partial N}=\Lambda_{g, \nabla^{E} \sigma}$$
modulo a smoothing operator.

Proof. Let $p \in \partial N$. Using Remark 3.3 we consider an extension $\left(\tilde{N}, \tilde{g}, \tilde{E}, \nabla^{\tilde{E}}\right)$ along $\partial N$ near $p$. Choose a coordinate chart $\left(\Omega, x^{\prime}\right)$ in $\partial N$ containing $p$ and denote by $\left(x^{\prime}, x^{n}\right)$ the corresponding boundary normal coordinates in $\tilde{N}$. Let $\Omega^{\prime} \subset \Omega$ be a precompact open subset and $\sigma$ a section in $H^{1 / 2}\left(\left.E\right|_{\partial N}\right)$ compactly supported in $\Omega^{\prime}$. Consider a solution $u \in H^{1}(\tilde{E}) \subset \mathscr{D}^{\prime}(\tilde{N} ; \tilde{E})$ to
$$\left\{\begin{array}{l}
\triangle^{\tilde{E}} u=0, \quad \text { in } \tilde{N} \\
\left.u\right|_{\partial N}=\sigma .
\end{array}\right.$$
By Proposition 3.2 and Remark 3.3, this problem is locally equivalent to the following system of equalities for $u, v$ :
$$\begin{gathered}
\left(I d \cdot D_{x^{n}}+i \tilde{A}\left(x, D_{x^{\prime}}\right)\right) u=v,\left.\quad u\right|_{x^{n}=0}=\sigma, \\
\left(I d \cdot D_{x^{n}}+i F(x)-i \tilde{A}\left(x, D_{x^{\prime}}\right)\right) v=h \in C^{\infty}\left([-\tilde{T}, \tilde{T}] \times \Omega^{\prime} ; \mathbb{C}^{r}\right) .
\end{gathered}$$
The second equation above can be viewed as a backwards generalized heat equation; making the substitution $t=\tilde{T}-x^{n}$, it is equivalent to
$$I d \cdot \partial_{t} v-(\tilde{A}-F) v=-i h, t \in[0,2 \tilde{T}]$$
Since $h$ is smooth and $\tilde{A}-F$ depends smoothly on $t$, by the transposed Leibniz formula we conclude that $v \in C^{\infty}\left([-\tilde{T}, \tilde{T}] ; \mathscr{D}^{\prime}\left(\Omega^{\prime} ; \mathbb{C}^{r}\right)\right)$ (cf. [T, Remark 1.2]). By elliptic regularity for the Laplacian $\triangle^{E}, u$ (and therefore also $v$ ) is smooth in the interior of $N$, and so $\left.v\right|_{x^{n}=T}$ is smooth. Now, if we were to show that the solution to (3.11) is smooth for $t \in[0,2 \tilde{T})$ then we are done. Indeed, we would have
$$I d \cdot D_{x^{n}} u+i \tilde{A}\left(x, D_{x^{\prime}}\right) u=v \in C^{\infty}\left((-\tilde{T}, \tilde{T}], \times \Omega^{\prime} ; \mathbb{C}^{r}\right),$$
and in particular, the restriction to the boundary $\left.v\right|_{x^{n}=0}$ is smooth. Now, if we set $R \sigma=\left.v\right|_{\partial N}$, then
$$\left.I d \cdot D_{x^{n}} u\right|_{\partial N}=-\left.i \tilde{A} u\right|_{\partial N}+R \sigma=-\left.i \tilde{A}\right|_{\partial N} \sigma+R \sigma=-\left.i A\right|_{\partial N} \sigma+R \sigma,$$
and we will get the desired result since $R$ is a smoothing operator. So in order to conclude the proof it is left to prove that $v$ is smooth for $t \in[0,2 \tilde{T})$. We will do this in the subsequent lemma. \(\square\)

Lemma. There is an operator $B$ in the congruence class of $\tilde{A}-F$ which satisfies the conditions for a well-posed heat equation in Section 2.4. As a result, the solution v to the equation (3.11) is smooth for $t \in[0,2 \tilde{T})$.

Proof. We will start by checking the conditions for the operator $\tilde{A}-F$. If some of them will not be satisfied then we will adjust the symbol of $\tilde{A}-F$ to obtain $B$. The first condition is satisfied due to the construction of $\tilde{A}$. Denote by $a_{1}=-I d \cdot \sqrt{q_{2}}$ and $a_{\leq 0}$ the principal part and the reminder part, respectively, of the full symbol of $\tilde{A}-F$ ( $F$ has order zero). Let $\|\|$ be the (operator) norm on complex $r \times r$-matrices induced from the Hermitian norm on $\mathbb{C}^{r}$. Note that for any matrix $M$ we have $\|M\| \geq|\lambda|$, where $\lambda$ is any eigenvalue of $M$, which implies that the matrix
$$I d \cdot z-M$$
is non-degenerate when $|z|>\|M\|$. Indeed, its eigenvalues are equal to $z-\lambda$ and we have
$$|z-\lambda| \geq|z|-|\lambda| \geq|z|-\|M\|>0 .$$
Since $\tilde{A}-F$ is an elliptic PDO of order 1 in $\Omega$ and $\Omega^{\prime}$ is precompact we have the following uniform in $[-\tilde{T}, \tilde{T}] \times \Omega^{\prime}$ bounds
$$c|\xi| \leq\left|a_{1}\right| \leq C_{1}\left(1+|\xi|^{2}\right)^{1 / 2} ;$$
where $c, C_{0}$, and $C_{1}$ are some positive constants. Using this we see that the matrix
$$I d \cdot z-\frac{a_{1}+a_{\leq 0}}{\left(1+|\xi|^{2}\right)^{1 / 2}}$$
is non-degenerate for $|z|>C_{1}+C_{0}$. Indeed, from (3.12),(3.13) the norm of the quotient term is bounded from above by the constant $C_{1}+C_{0}$. It is left to check if (3.14) is non-degenerate when $z=x+i y$ with $-\epsilon<x$, for some sufficiently small $\epsilon>0$. We have
$$I d \cdot\left(x+i y+\frac{\sqrt{q_{2}}}{\left(1+|\xi|^{2}\right)^{1 / 2}}\right)-\frac{a_{\leq 0}}{\left(1+|\xi|^{2}\right)^{1 / 2}}=I d \cdot \rho-A_{\leq 0},$$
where
$$\rho=x+i y+\frac{\sqrt{q_{2}}}{\left(1+|\xi|^{2}\right)^{1 / 2}},$$
and
$$A_{\leq 0}=\frac{a_{\leq 0}}{\left(1+|\xi|^{2}\right)^{1 / 2}} .$$
We know that the matrix (3.15) is non-degenerate when $|\rho|>\left\|A_{\leq 0}\right\|$. Since $q_{2}$ can be arbitrarily small for $\xi$ close to 0 we cannot guarantee that $\rho$ will not vanish for any small $\epsilon>0$.

Therefore, we have to adjust the symbol of $\tilde{A}-F$. From (3.12) we obtain
$$\frac{\sqrt{q_{2}}}{\left(1+|\xi|^{2}\right)^{1 / 2}} \geq \frac{c}{2},$$
when $|\xi| \geq 1$. Hence, when $\epsilon<\frac{c}{2}$ we have
$$|\rho|^{2}=y^{2}+\left(x+\frac{\sqrt{q_{2}}}{\left(1+|\xi|^{2}\right)^{1 / 2}}\right)^{2}>\left(\frac{c}{2}-\epsilon\right)^{2},$$
for $|\xi| \geq 1$. From (3.13) we see that
$$\left\|A_{\leq 0}\right\|^{2} \leq \frac{C_{0}^{2}}{1+|\xi|^{2}},$$
which is less than $\left(\frac{c}{2}-\epsilon\right)^{2}$ when $|\xi| \geq C_{0}\left(\frac{c}{2}-\epsilon\right)^{-1}$. Let $R=\max \left(1, C_{0}\left(\frac{c}{2}-\epsilon\right)^{-1}\right)$, then the matrix (3.15) is non-degenerate for $|\xi| \geq R$. On the other hand, for $|\xi|<R$ we know that $\left\|A_{\leq 0}\right\| \leq C_{0}$. Now let us consider the congruent operator $B\left(t, x^{\prime}, D_{x^{\prime}}\right)$ by adjusting the full symbol as
$$a_{1}+a_{\leq 0}-I d \cdot \psi(\xi),$$
where $\psi(\xi)=C e^{-\frac{|\xi|^{2}}{R^{2}}}$ and the constant $C$ is equal to $e\left(1+R^{2}\right)^{1 / 2}\left(C_{0}+\frac{c}{2}\right)$. One sees that now for $|\xi|<R$ we have
$$|\rho|^{2}=y^{2}+\left(x+\frac{\sqrt{q_{2}}+\psi(\xi)}{\left(1+|\xi|^{2}\right)^{1 / 2}}\right)^{2}>\left(C_{0}+\frac{c}{2}-\epsilon\right)^{2}>C_{0}^{2} \geq\left\|A_{\leq 0}\right\|,$$
so the matrix (3.14) for the adjusted operator is non-degenerate in this case. In the other cases it is clear that it remains non-degenerate, which guarantees that the operator $B\left(t, x^{\prime}, D_{x^{\prime}}\right)$ satisfies the conditions for a well-posed heat equation. The second part of the lemma follows immediately. Indeed, since $B$ is congruent to $\tilde{A}-F$ we have
$$I d \cdot \partial_{t} v-B(t) v \in C^{\infty}\left([-\tilde{T}, \tilde{T}] \times \Omega^{\prime} ; \mathbb{C}^{r}\right)$$
and, therefore, by Theorem (2.1) the solution $v$ is smooth for $t \in[0,2 \tilde{T})$. \(\square\)

Corollary 3.5. The full symbol of the DtN operator $\Lambda_{g, \nabla^{E}}$ is the same as the full symbol of $\left.A\left(x, D_{x^{\prime}}\right)\right|_{\partial N}$. In particular, the DtN operator is a classical elliptic pseudodifferential operator of order 1.

We are now in a position to recover the geometric data (the metric $g$ and the connection $\nabla^{E}$ ) on the boundary $\partial N$ from the given DtN operator $\Lambda$.
3.3. Proof of Theorem 1.1. Let $\left\{x^{1}, \ldots, x^{n}\right\}$ denote boundary normal coordinates associated with $\left\{x^{1}, \ldots, x^{n-1}\right\}$ and $\left(\varepsilon_{1}, \ldots, \varepsilon_{r}\right)$ denote boundary normal frame defined by $\left(\epsilon_{1}, \ldots, \epsilon_{r}\right)$. Note that since
$$\partial_{x^{n}} g_{k l}=-\sum_{\eta, \mu} g_{k \eta}\left(\partial_{x^{n}} g^{\eta \mu}\right) g_{\mu l},$$
it also suffices to determine the inverse matrix $\left(g^{k l}\right)$ and its normal derivatives instead of $\left(g_{k l}\right)$ and its normal derivatives. Using Corollary 3.5 and (3.7) we get
$$\lambda_{1}=-\sqrt{q_{2}},$$
and we have at any $p \in \partial N$,
$$q_{2}\left(p, \xi^{\prime}\right)=\sum_{k, l=1}^{n-1} g^{k l}(p) \xi_{k} \xi_{l}=\left(\frac{\operatorname{Trace} \lambda_{1}}{r}\right)^{2} .$$
Thus, the principal symbol of the DtN operator determines $g^{k l}$ at each boundary point $p$.
Next from Corollary 3.5 and (3.8) we have
$$\begin{aligned}
\lambda_{0}=\frac{1}{2 \sqrt{q_{2}}}\left[\sum_{l}^{n-1} \partial_{\xi^{l}} \sqrt{q_{2}}\right. & \left.D_{x^{l}} \sqrt{q_{2}}-q_{1}-\partial_{x^{n}} \sqrt{q_{2}}+F \sqrt{q_{2}}\right]= \\
& =-\frac{1}{2 \sqrt{q_{2}}} \partial_{x^{n}} \sqrt{q_{2}}+\frac{i}{2 \sqrt{q_{2}}} \sum_{l=1}^{n-1} V^{l} \xi_{l}-\frac{1}{4} \sum_{k, l=1}^{n-1} g^{k l}(x) \partial_{x^{n}} g_{k l}(x)+T_{0},
\end{aligned}$$
where
$$T_{0}=\frac{1}{2 \sqrt{q_{2}}} \sum_{l}^{n-1} \partial_{\xi^{l}} \sqrt{q_{2}} D_{x^{l}} \sqrt{q_{2}}+\frac{i}{2 \sqrt{q_{2}}} \sum_{k, l=1}^{n-1}\left(\frac{1}{2} g^{k l}(x) \partial_{x^{k}} \log \delta(x)+\partial_{x^{k}} g^{k l}(x)\right) \xi_{l}$$
is an expression involving only $g_{k l}, g^{k l}$, and their tangential derivatives along $\partial N$. Note that $\sum g^{k l} g_{k l}=n-1$, and so
$$-\sum_{k, l=1}^{n-1} g^{k l}(x) \partial_{x^{n}} g_{k l}(x)=\sum_{k, l=1}^{n-1} g_{k l}(x) \partial_{x^{n}} g^{k l}(x) .$$
If we set $h^{k l}=\partial_{x^{n}} g^{k l}, h=\sum g_{k l} h^{k l}$, and $\left\|\xi^{\prime}\right\|^{2}=\sum g^{k l} \xi_{k} \xi_{l}=q_{2}$, we can rewrite (3.16) in the form
$$\lambda_{0}(\xi)=-\frac{1}{4\left\|\xi^{\prime}\right\|^{2}} \sum_{k, l=1}^{n-1}\left(h^{k l}-h g^{k l}\right) \xi_{k} \xi_{l}+\frac{i}{2\left\|\xi^{\prime}\right\|} \sum_{l=1}^{n-1} V^{l} \xi_{l}+T_{0} .$$
From antisymmetric part $\lambda_{0}(\xi)-\lambda_{0}(-\xi)$ we obtain
$$\frac{i}{\left\|\xi^{\prime}\right\|} \sum_{l=1}^{n-1} V^{l} \xi_{l},$$
which allows us to determine $V^{l}$ and multiplying by $\frac{1}{2} g_{k l}$ we get
$$\frac{1}{2} g_{k l} V^{l}=g_{k l} g^{l j} \omega_{j}=\delta_{k}^{j} \omega_{j}=\omega_{k},$$
so we determined the connection matrix $\omega_{k}$ for $k=1, \ldots, n-1$ on the boundary $\partial N$. Let us look at the remaining terms. Only the first term in (3.17) is unknown yet. But we can recover it from all the other terms. Thus, we can recover the quadratic form
$$\kappa^{k l}=h^{k l}-h g^{k l} .$$
When $n>2$, this in turn determines $h^{k l}=\partial_{x^{n}} g^{k l}$, since
$$h^{k l}=\kappa^{k l}+\frac{1}{2-n}\left(\sum_{p, q} \kappa^{p q} g_{p q}\right) g^{k l} .$$

Now let us look at (3.9). We have
$$\begin{aligned}
\lambda_{-1}=\frac{1}{2 \sqrt{q_{2}}}[- & \sum_{l}^{n-1} \partial_{\xi^{l}} \sqrt{q_{2}} D_{x^{l}} \lambda_{0}-\sum_{l}^{n-1} \partial_{\xi^{l}} \lambda_{0} D_{x^{l}} \sqrt{q_{2}}+ \\
& \left.+\frac{1}{2} \sum_{k, l}^{n-1} \partial_{\xi^{k}} \partial_{\xi^{l}} \sqrt{q_{2}} D_{x^{k}} D_{x^{l}} \sqrt{q_{2}}-q_{0}+\partial_{x^{n}} \lambda_{0}-F \lambda_{0}\right] \\
& =-\frac{1}{2 \sqrt{q_{2}}} q_{0}+\frac{1}{2 \sqrt{q_{2}}} \partial_{x^{n}} \lambda_{0}+T_{-1}\left(g_{k l}, \omega_{l}\right)= \\
& \quad-\frac{1}{8\left\|\xi^{\prime}\right\|^{3}} \sum_{k, l=1}^{n-1} \partial_{x^{n}} \kappa^{k l} \xi_{k} \xi_{l}+\frac{i}{4\left\|\xi^{\prime}\right\|^{2}} \sum_{l=1}^{n-1} \partial_{x^{n}} V^{l} \xi_{l}+T_{-1}\left(g_{k l}, \omega_{l}\right),
\end{aligned}$$
where $T_{-1}\left(g_{k l}, \omega_{l}\right)$ is an expression involving only $g_{k l}, g^{k l}$, their first normal derivatives and the boundary values of $\omega_{l}$. Here again looking at the antisymmetric part of $\lambda_{-1}$ we determine $\partial_{x^{n}} V^{l}$ and subsequently $\partial_{x^{n}} \omega_{k}$ for $k=1, \ldots, n-1$. The first term of (3.19) is again determined by the other terms, which allows us to recover
$$-\frac{1}{8\left\|\xi^{\prime}\right\|^{3}} \sum_{k, l=1}^{n-1} \partial_{x^{n}} \kappa^{k l} \xi_{k} \xi_{l},$$
and hence also $\partial_{x^{n}} \kappa^{k l}$. Due to (3.18) the latter determines $\partial_{x^{n}} h^{k l}=\partial_{x^{n}}^{2} g^{k l}$.
Proceeding by induction, let $m \leq-1$, and suppose we have shown that, when $-1 \geq j \geq m$,
$$\lambda_{j}=-\frac{1}{\left\|2 \xi^{\prime}\right\|^{2-j}} \sum_{k, l=1}^{n-1}\left(\partial_{x^{n}}^{|j|} k^{k l}\right) \xi_{k} \xi_{l}+\frac{i}{\left\|2 \xi^{\prime}\right\|^{1-j}} \sum_{l=1}^{n-1} \partial_{x^{n}}^{|j|} V^{l} \xi_{l}+T_{j}\left(g_{k l}, \omega_{l}\right),$$
where $T_{j}\left(g_{k l}, \omega_{l}\right)$ involves only the boundary values of $g_{k l}, g^{k l}$, their normal derivatives of order at most $|j|$, and also for $j \leq-1$ involves the boundary values of $\omega_{l}$, and their normal
derivatives of order at most $|j|-1$. From Corollary 3.5 and (3.10) we get
$$\begin{aligned}
\lambda_{m-1}=\frac{1}{2 \sqrt{q_{2}}} & {\left[\partial_{x^{n}} \lambda_{m}+\sum_{\substack{j, k, K \\
m \leq j, k \leq 1 \\
|K|=j+k-m}} \frac{1}{K!} \partial_{\xi}^{K} \lambda_{j} D_{x}^{K} \lambda_{k}-F \lambda_{m}\right]=} \\
& \quad=-\frac{1}{\left\|2 \xi^{\prime}\right\|^{3-m}} \sum_{k, l=1}^{n-1}\left(\partial_{x^{n}}^{|m-1|} \kappa^{k l}\right) \xi_{k} \xi_{l}+\frac{i}{\left\|2 \xi^{\prime}\right\|^{2-m}} \sum_{l=1}^{n-1} \partial_{x^{n}}^{|m-1|} V^{l} \xi_{l}+T_{m-1}\left(g_{k l}, \omega_{l}\right) .
\end{aligned}$$
Taking the antisymmetric part of $\lambda_{m-1}$ we can determine $\partial_{x^{n}}^{|m-1|} V^{l}$ and, therefore, also $\partial_{x^{n}}^{|m-1|} \omega_{k}$. The first term is again determined by the other terms. So we can recover $\partial_{x^{n}}^{|m-1|} \kappa^{k l}$ and thus $\partial_{x^{n}}^{|m-2|} g^{k l}$ also. This completes the induction step.
3.4. Gauge equivalence of the reconstructed connection. Let $\pi_{E}: E \rightarrow X$ and $\pi_{F}$ : $F \rightarrow Y$ be two smooth vector bundles over smooth manifolds. We say that an isomorphism $\phi: E \rightarrow F$ covers a diffeomorphism $\psi: X \rightarrow Y$ if the relation
$$\pi_{F} \circ \phi=\psi \circ \pi_{E}$$
holds. Note that any isomorphism $\phi$ covers the unique underlying diffeomorphism of the bases defined by $\psi=\pi_{F} \circ \phi \circ \pi_{E}^{-1}$. One of the corollaries of the main result is the following Proposition on gauge equivalence.

Proposition 3.6. Let $\left(N_{i}, g_{i}, E_{i}, \nabla^{i}\right)$, where $i=1,2$, be two Euclidean smooth vector bundles defined over connected compact Riemannian manifolds with boundary. Suppose that for some open subsets $\Sigma_{i} \subset \partial N_{i}$ there exists a vector bundle isomorphism $\phi:\left.\left.E_{1}\right|_{\Sigma_{1}} \rightarrow E_{2}\right|_{\Sigma_{2}}$ that intertwines with the corresponding Dirichlet-to-Neumann operators $\Lambda_{\Sigma_{1}}$ and $\Lambda_{\Sigma_{2}}$, i.e. the relation $\phi \circ \Lambda_{\Sigma_{1}}(s) \circ \psi^{-1}=\Lambda_{\Sigma_{2}}\left(\phi \circ s \circ \psi^{-1}\right)$ holds for any smooth section $s$ of $\left.E_{1}\right|_{\Sigma_{1}}$. Then the isomorphism $\phi$ is a gauge equivalence, $\phi^{*} \nabla^{2}=\nabla^{1}$, and covers an isometry $\psi:\left(\Sigma_{1}, g_{1}\right) \rightarrow$ $\left(\Sigma_{2}, g_{2}\right)$.

Proof. Clearly, the isomorphism $\phi$ intertwining the DtN operators $\Lambda_{\Sigma_{1}}$ and $\Lambda_{\Sigma_{2}}$ is equivalent to having the equality of operators
$$\Lambda_{\Sigma_{1}}(s)=\phi^{-1} \circ \Lambda_{\Sigma_{2}}\left(\phi \circ s \circ \psi^{-1}\right) \circ \psi .$$
The operator on the right hand side is a natural pull-back of the operator $\Lambda_{\Sigma_{2}}$ along $\phi$. Therefore, the metric and connection on $\left(E_{1}, \Sigma_{1}\right)$ reconstructed from its full symbol are equal to $\psi^{*} g_{2}$ and $\phi^{*} \nabla^{2}$, respectively. On the other hand the full symbols of the above two operators coincide. Hence, we have $g_{1}=\psi^{*} g_{2}$ and $\nabla^{1}=\phi^{*} \nabla^{2}$, which completes the proof. \(\square\)
3.5. The case of surfaces. In two dimensions, we can only aim to reconstruct a conformal class of metrics from the DtN operator. This is because the connection Laplacian is conformally contravariant in two dimensions. Indeed, from the definition of the connection

Laplacian we have
$$\triangle_{e^{\mu} g}^{E}=e^{-\mu} \triangle_{g}^{E},$$
where the subscript indicates the metric used to define the connection Laplacian. Clearly, $\triangle_{g}^{E} u=0$ if and only if $\triangle_{e^{\mu} g}^{E} u=0$. The unit normal vector at the boundary for the conformal metric is equal to
$$\left.e^{-\mu / 2}\right|_{\partial N} \cdot \frac{\partial}{\partial \nu} .$$
Therefore, we have the following identity for the DtN operators
$$\Lambda_{e^{\mu} g, \nabla^{E}}=\left.e^{-\mu / 2}\right|_{\partial N} \cdot \Lambda_{g, \nabla^{E}} .$$
This identity shows that the DtN operators constructed using conformal metrics coincide if a conformal factor $e^{\mu}$ equals to 1 at the boundary. This fact poses obstacles to the recovery of the normal derivatives of the geometric data at the boundary of surfaces. However, we can still recover the metric and the connection on the boundary from the symbol of the DtN operator. This follows immediately from the proof of the Theorem 1.1.

\section*{References}
\begin{itemize}
\item[] [C] Cekić Mihajlo. Calderi ¿oen problem for Yang-Mills connections. J. Spectr. Theory Electronically published on May 14, 2020. doi: 10.4171/JST/302
\item[] [EL] Eells, J., Lemaire, L. Selected topics in harmonic maps. CBMS Regional Conference Series in Mathematics, 50. American Mathematical Society, Providence, RI, 1983. v+85 pp.
\item[] [E] Evans, L. Partial Differential Equations, volume 19 of Graduate Studies in Mathematics. American Mathematical Society, 1998.
\item[] [KOP] Kurylev, Yaroslav; Oksanen, Lauri; Paternain, Gabriel P. Inverse problems for the connection Laplacian. J. Differential Geom. 110 (2018), no. 3, 457--494. doi:10.4310/jdg/1542423627
\item[] [LTU] Lassas, M.; Taylor, M; Uhlmann, G. The Dirichlet-to-Neumann map for complete Riemannian manifolds with boundary. Comm. Anal. Geom. 11 (2003), no. 2, 207-221.
\item[] [LU] Lassas, M.; Uhlmann, G. On determining a Riemannian manifold from the Dirichlet-to-Neumann map. Ann. Sci. ï¿æcole Norm. Sup. (4) 34 (2001), no. 5, 771-787.
\item[] [LeU] Lee, J. M.; Uhlmann, G. Determining anisotropic real-analytic conductivities by boundary measurements. Comm. Pure Appl. Math., 42 (1989), pp. 1097-1112
\item[] [N] Nicolaescu, Liviu I. Lectures on the geometry of manifolds. Second edition. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ, 2007. xviii+589 pp. ISBN: 978-981-277-862-8; 981-277-862-4
\item[] [T] Trïjæves, Franï¿gois. Introduction to Pseudodifferential and Fourier Integral Operators: Pseudodifferential Operators. Springer Science \& Business Media, 299, (2013), ISBN 1468487809, 9781468487800
\end{itemize}

School of Mathematics, University of Leeds, Leeds LS2 9JT, UK
Email address: mmrg@leeds.ac.uk