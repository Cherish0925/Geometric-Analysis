---
retention_scope: session
part: 1
total_parts: 7
---

[Part 1/7 of: Sobolev-classasymptoticallyhyperbolicmanifolds and]

---
source_file: 2206_12854.pdf
converter: mathpix
format: mmd
---

\title{
SOBOLEV-CLASS ASYMPTOTICALLY HYPERBOLIC MANIFOLDS AND THE YAMABE PROBLEM
}

\author{
PAUL T. ALLEN, JOHN M. LEE, AND DAVID MAXWELL
}

\begin{abstract}
We consider asymptotically hyperbolic manifolds whose metrics have Sobolevclass regularity, and introduce several technical tools for studying PDEs on such manifolds. Our results employ two novel families of function spaces suitable for metrics potentially having a large amount of interior differentiability, but whose Sobolev regularity implies only a Hölder continuous conformal structure at infinity. We establish Fredholm theorems for elliptic operators arising from metrics in these families.

To demonstrate the utility of our methods, we solve the Yamabe problem in this category. As a special case, we show that the asymptotically hyperbolic Yamabe problem is solvable so long as the metric admits a $W^{1, p}$ conformal compactification, with $p$ greater than the dimension of the manifold.
\end{abstract}

\section*{Contents}
1. Introduction ..... 2
Main results ..... 4
Organization ..... 9
Acknowledgements ..... 9
2. Coordinate systems ..... 9
2.1. Hyperbolic space ..... 9
2.2. Neighborhoods near infinity in $M$ ..... 10
2.3. Möbius parametrizations ..... 10
3. Elementary function spaces ..... 11
3.1. Definitions ..... 12
3.2. Embeddings and dense subsets ..... 14
3.3. Covariant derivatives ..... 16
3.4. Tensor operations ..... 18
3.5. Interpolation ..... 19
3.6. Embedding spaces on $\bar{M}$ into weighted spaces on $M$ ..... 20
3.7. Geometric tensor bundles ..... 22
3.8. Duality ..... 23
3.9. Nonlinearities ..... 24
4. Fortified spaces on $\bar{M}$ ..... 25
4.1. Mapping properties of $\hat{\nabla}$ and $\rho$ ..... 27
4.2. Relationships with weighted spaces on $M$ ..... 29

\footnotetext{
Date: June 26, 2022.
2020 Mathematics Subject Classification. 58J05, 53C21, 46E35.
}
4.3. Relationships with spaces on $\bar{M}$ ..... 31
4.4. Boundary asymptotics ..... 32
4.5. Relationships between fortified spaces ..... 33
4.6. Multiplication and nonlinearities ..... 34
5. Asymptotically hyperbolic metrics ..... 37
6. The Yamabe problem ..... 41
6.1. Solution in the $\mathscr{H}^{s, p ; m}$ category ..... 45
6.2. Solution in the $\mathscr{X}^{s, p ; m}$ category ..... 55
7. Boundary asymptotics in fortified spaces ..... 56
7.1. Boundary traces and asymptotic decay ..... 59
7.2. $\mathbb{H}$-mollification ..... 64
7.3. Asymptotic structure ..... 69
8. Elliptic differential operators ..... 71
8.1. Linear differential operators ..... 72
8.2. Geometric operators and Assumption P ..... 74
8.3. Boundary decay estimates ..... 76
8.4. Localized approximate operators at infinity ..... 77
8.5. Interpolations of $\mathcal{P}$ at infinity ..... 81
8.6. A priori estimates ..... 84
9. Fredholm theory ..... 87
9.1. Parametrix construction ..... 87
9.2. Fredholm theorem for weighted Sobolev spaces ..... 89
9.3. Fredholm theorem for Gicquaud-Sakovich spaces ..... 93
9.4. Structure theorems ..... 96
9.5. Regularity bootstrapping and polyhomogeneity ..... 98
Appendix A. Weighted function spaces ..... 99
A.1. Elementary properties ..... 103
A.2. Density of smooth tensors ..... 105
A.3. Interpolation ..... 106
A.4. Duality ..... 109
A.5. Geometric tensor bundles ..... 112
A.6. Equivalent norms ..... 119
Appendix B. Elliptic theory for hyperbolic space ..... 121
Appendix C. Smooth approximation of metrics in fortified spaces ..... 126
Appendix D. Improved regularity for Laplacians ..... 127
References ..... 129

\section*{1. Introduction}

Given a Riemannian manifold ( $M^{n}, g$ ), the Yamabe problem seeks a metric $\widetilde{g}$ that is conformally related to $g$ and that has constant scalar curvature. Writing $\widetilde{g}=\Theta^{q_{n}-2} g$, where $q_{n}=\frac{2 n}{n-2}$, the requirement that the scalar curvature of $\widetilde{g}$ be equal to the constant $\mathrm{R}^{*}$ is
equivalent to requiring that the conformal factor $\Theta$ satisfy the semilinear equation
$$-\left(q_{n}+2\right) \Delta_{g} \Theta+\mathrm{R}[g] \Theta=\mathrm{R}^{*} \Theta^{q_{n}-1},$$
where $\mathrm{R}[g]$ is the scalar curvature of $g$, and where our convention for the Laplacian is $\Delta_{g}=\operatorname{tr}_{g} \nabla^{2}$. Note that $q=\frac{2 n}{n-2}$ is the critical exponent associated to the Sobolev embedding of $W^{1,2}$ into $L^{q}$. In the case where $M$ is compact without boundary, the problem has a long and famous history, with important work by Trudinger and Aubin and Schoen ultimately leading to a satisfactory resolution of the problem; see [LP87], and the references within.

In this paper, we consider the case where $\left(M^{n}, g\right)$ is asymptotically hyperbolic in the sense that $\left(M^{n}, g\right)$ is a complete manifold, and that the sectional curvatures of $g$ approach -1 at infinity. In this setting, we seek to conformally deform $g$ to have scalar curvature $\breve{\mathrm{R}}_{n}:=$ $-n(n-1)$, the curvature of $n$-dimensional hyperbolic space. We further consider the case where the metric $g$ has Sobolev-scale regularity sufficient that $g$ be continuous, but possibly is not continuously differentiable.

We are motivated by regularity results in previous analyses of the Yamabe problem in the asymptotically hyperbolic setting, along with related work in geometric analysis. Most previous studies of the Yamabe problem in the asymptotically hyperboic setting have assumed that the metric $g$ admits a regular conformal structure at infinity [ACF92a, Maz91]. Related studies of elliptic operators arising from asymptotically hyperbolic metrics also require the geometry to have a regular conformal structure (see e.g. [And93, Lee06]).

Yet even if $g$ is assumed to have a smooth conformal compactification, the asymptotic behavior of generic solutions to (1.1) is incompatible with the resulting metric $\widetilde{g}$ also admitting smooth conformal structure [ACF92a]; similar results hold for the more general Einstein constraint equations [AC96, AILSA16]. Geometries that are smooth on the interior, but that do not admit smooth conformal compactifications also appear in the study of boundary regularity for Poincaré-Einstein metrics [CDLS05]. We emphasize that in all these examples, the limited boundary regularity of solutions is due to the algebraic structure of the relevant equations, and is thus an inherent feature of the problem, rather than an artifact of the methods. Thus for geometric analysis problems involving asymptotically hyperbolic geometry, the appropriate regularity setting is one for which metrics are sufficiently regular on $M$ for theory of elliptic PDE to be established, while simultaneously metrics are permitted to be less regular along the conformal boundary.

The work [AILSA18] introduced a category of asymptotically hyperbolic metrics that can have a great deal of Hölder regularity on $M$, but which may only have Lipschitz-continuous conformal compactifications. Fredholm theory for elliptic operators arising from these metrics was established, following the approach of [Lee06], and was subsequently used to show that the Yamabe problem can be solved in this category. In particular, if a metric is initially of this class, then there is a conformally related metric of the same class having constant scalar curvature.

In this work we address the Sobolev setting. In particular, we introduce Banach spaces that allow us to define two different classes of metrics that have $H^{s, p}$ regularity on $M$, but whose
conformal compactification is not better than $H^{m, p}$ on $\bar{M}$. Under conditions on $s, m$, and $p$ that ensure the conformal structure at infinity is continuous, we show that the sectional curvatures approach -1 at infinity in an appropriate sense, and thus that the asymptotically hyperbolic condition is well-defined in these categories. We establish Fredholm theory for elliptic operators arising from such metrics, and subsequently show that the Yamabe problem can be solved in these categories: every asymptotically hyperbolic metric of each regularity class is conformally related to a unique constant-scalar-curvature metric of the same class.

Our motivation for considering Sobolev-class metrics is two-fold. First, there is the intrinsic interest of extending theory that exists for other settings to the asymptotically hyperbolic category. Our work provides a number of technical tools, notably the Fredholm theory for geometric elliptic operators of §9 and the asymptotic decomposition of tensor fields in §7, that are relevant to a wide range of geometric analysis problems. Regularity of the type we consider arises naturally in variational problems and indeed our technique for solving the Yamabe problem highlights this character. We show that the Yamabe problem is solvable so long as the metric admits a $W^{1, p}$ conformal compactification on $\bar{M}$ with $p>n$, the threshold needed to ensure Hölder continuity. Greater regularity (in the interior, or at the boundary) is obtained secondarily after a weak solution has been established.

Second, metrics having Sobolev-class regularity arise routinely in general relativity. As discussed in [ACF92a, AILSA16], the Yamabe problem is a special case of the conformal method used to generate initial data for the gravitational Cauchy problem. It is natural to construct this data in regularity classes compatible with the $L^{2}$-based hyperbolic theory typically used in evolution problems (see [Rin09] and references therein). Moreover, mixed elliptic-hyperbolic schemes for solving the Einstein equations [AM03] involve solving elliptic problems arising from Sobolev-class metrics at each time step during the evolution. An understanding of the asymptotic features of spacetimes generated with these methods has the potential to shed light on open questions regarding conformal structures in general relativity [Fri18].

Main results. In order to give a precise statement of our main results, we introduce a number of key definitions and notations, beginning with a discussion of regularity classes.
Let $\bar{M}$ be a smooth, connected, compact, $n$-dimensional manifold with boundary; let $M$ be the interior of $\bar{M}$ and denote the boundary by $\partial M$. Let $\rho$ be a smooth defining function on $\bar{M}$, meaning $\rho: \bar{M} \rightarrow[0, \infty)$ with $\rho^{-1}(0)=\partial M$ and $d \rho \neq 0$ along $\partial M$. A metric $g$ on $M$ is said to be conformally compact if $\bar{g}=\rho^{2} g$ extends to a non-degenerate, and at least continuous, metric on $\bar{M}$.

Fixing a smoothly conformally compact reference metric, for $k \in \mathbb{N}_{\geq 0}, 1 \leq p<\infty, \delta \in \mathbb{R}$ we define weighted Sobolev spaces $W_{\delta}^{k, p}(M)=\rho^{\delta} W^{k, p}(M)$ to have norm $\|u\|_{W_{\delta}^{k, p}(M)}=$ $\left\|\rho^{-\delta} u\right\|_{W^{k, p}(M)}$. Using an equivalent norm, defined via a collection of local Möbius parametrizations, whose scaling is compatible with hyperbolic geometry (see §2), we generalize
these Sobolev spaces to weighted Bessel potential spaces $H_{\delta}^{s, p}(M)$ having non-integer order of differentiability; see §3.1. The collection of local Möbius parametrizations further allows us to define spaces $X_{\delta}^{s, p}(M)$ of functions having local differentiability measured in $H^{s, p}$, but with global behavior measured in a uniform sense akin to Hölder spaces; again, see §3.1. These spaces, which we refer to as Gicquaud-Sakovich spaces, generalize those introduced in [GS12], and play a key technical role in our analysis.

As discussed above, regularity classes appropriate for geometric analysis problems in the asymptotically hyperbolic setting must have admit functions with (possibly a great deal) more regularity on the interior $M$ than on the compactified manifold $\bar{M}$. However, neither the standard function spaces on $M$, nor those on $\bar{M}$, sufficiently handle these competing demands. For example, functions in $C^{k, \alpha}(\bar{M})$ have at most $C^{k, \alpha}(M)$ interior regularity, while functions in $C^{k, \alpha}(M)$ may not have well-defined boundary values at all.

In the Hölder setting, this situation was addressed in [AILSA18] by introducing spaces $\mathscr{C}^{k, \alpha ; m}(M)$, where we require $k \geq m$, of functions satisfying
$$C_{m}^{k, \alpha}(M) \subset \mathscr{C}^{k, \alpha ; m}(M) \subset C^{m-1,1}(\bar{M}) \cap C_{0}^{k, \alpha}(M) .$$
In §4 we define analogous Sobolev-scale spaces $\mathscr{H}^{s, p ; m}(M)$ and $\mathscr{X}^{s, p ; m}(M)$, which we refer to as fortified spaces, for $1<p<\infty, s \in \mathbb{R}$, and $m \in \mathbb{N}_{\geq 0}$ with $s \geq m$. These are subspaces of weighted $H^{s, p}$ and $X^{s, p}$ spaces respectively but enforce additional regularity at the boundary. For functions, we have
$$\begin{aligned}
H_{m-n / p}^{s, p}(M) & \subset \mathscr{H}^{s, p ; m}(M) \subset H^{m, p}(\bar{M}) \cap H_{-n / p}^{s, p}(M), \\
X_{m}^{s, p}(M) & \subset \mathscr{X}^{s, p ; m}(M) \subset H^{m, p}(\bar{M}) \cap X_{0}^{s, p}(M),
\end{aligned}$$
while similar inclusions exist for tensor fields of various ranks; see Lemma 4.5 and Proposition 4.7. In particular, every fortified space is a subspace of some $H^{m, p}(\bar{M} ; E)$.

As a consequence of this boundary regularity, when $m \geq 1$, elements of fortified spaces possess boundary traces. Importantly, these spaces also admit more detailed boundary structure. The Asymptotic Structure Theorem 7.1 shows that a tensor field $u$ belonging to either $\mathscr{H}^{s, p ; m}$ or $\mathscr{X}^{s, p ; m}$ admits a decomposition $u=\tau+r$, where $\tau$ is smooth on the interior $M$ and describes the leading order asymptotic behavior, and where the remainder $r$ decays as rapidly as the (limited) boundary regularity permits. Theorem 7.1 is a consequence of the fine structure provided by a coordinate-dependent variation of Taylor's Theorem, Theorem 7.11.

We now define the two classes of metrics we consider. To motivate our definition, recall that the curvature operator $\operatorname{Riem}[g]: \Lambda^{2}(T M) \rightarrow \Lambda^{2}(T M)$ relates to that of $\bar{g}=\rho^{2} g$ via the formula
$$\operatorname{Riem}[g]=-|d \rho|_{\bar{g}}^{2} \operatorname{id}+2 \rho \delta * \operatorname{Hess}_{\bar{g}}(\rho)^{\sharp}+\rho^{2} \operatorname{Riem}[\bar{g}] ;$$
here id and $\delta$ are the identity operators on $\Lambda^{2}(T M)$ and $\Lambda^{1}(T M)$, respectively, and * is the Kulkarni-Nomizu product; see [AILSA18]. Thus if $\bar{g}$ is sufficiently regular that the first term on the right side of (1.2) dominates as $\rho \rightarrow 0$, then the curvatures of $g$ are determined by the value of $|d \rho|_{\bar{g}}^{2}$ along $\partial M$. In particular, if $|d \rho|_{\bar{g}}^{2}=1$ along $\partial M$, the curvatures of $g$
approach those of hyperbolic space as $\rho \rightarrow 0$. This motivates the following definition: a continuously conformally compact metric $g$ is said to be asymptotically hyperbolic either of class
$$\begin{aligned}
& \mathscr{H}^{s, p ; m} \text { with } s \geq m>n / p, 1<p<\infty, \text { or } \\
& \mathscr{X}^{s, p ; m} \text { with } s \geq m \geq 1 \text { and } s>n / p, 1<p<\infty,
\end{aligned}$$
if $\bar{g}=\rho^{2} g$ is an element of $\mathscr{H}^{s, p ; m}(M)$ or $\mathscr{X}^{s, p ; m}(M)$, respectively, and if
$$|d \rho|_{\bar{g}}=1 \text { along } \partial M \text {. }$$
The condition (1.5) is well-defined due to Proposition 4.7, which implies that under either (1.3) or (1.4) we have
$$\bar{g}=\rho^{2} g \in C^{0, \alpha}(\bar{M}) \text { for some } \alpha \in(0,1] .$$
The descriptor 'asymptotically hyperbolic' is justified by Proposition 5.1, which shows that the curvature operator of a metric $g$ of class (1.3) or (1.4) for which (1.5) holds indeed satisfies
$$\operatorname{Riem}[g]=-\mathrm{id}+\text { remainder, }$$
where the remainder is the sum of a smooth term that is $O(\rho)$ at $\partial M$ and a less regular term decaying as rapidly as the boundary regularity of $\bar{g}$ permits.
Our main result concerning the Yamabe problem is that it can be solved in both the $\mathscr{H}^{s, p ; m}$ and $\mathscr{X}^{s, p ; m}$ asymptotically hyperbolic categories.

Theorem 1.1 (Yamabe Theorem).
\begin{itemize}
\item[(a)] Suppose $g$ is an asymptotically hyperbolic metric of class (1.3) with $m \leq n$. Then there exists a unique conformal factor $\Theta \in \mathscr{H}^{s, p ; m}(M)$ such that $\left.\Theta\right|_{\partial M}=1$ and such that $\mathrm{R}\left[\Theta^{q_{n}-2} g\right]=-n(n-1)$.
\item[(b)] Suppose $g$ is an asymptotically hyperbolic metric of class (1.4) with $m<n$. Then there exists a unique conformal factor $\Theta \in \mathscr{X}^{s, p ; m}(M)$ such that $\left.\Theta\right|_{\partial M}=1$ and such that $\mathrm{R}\left[\Theta^{q_{n}-2} g\right]=-n(n-1)$.
\end{itemize}

Note the dimensional restrictions on $m$ in Theorem 1.1, which represent a restriction on the regularity of solutions along the conformal boundary. The results of [ACF92a] show that (generically) these restrictions are sharp; see also [AC96], [AILSA18]. Note also that working in the $\mathscr{H}$ category allows for more regularity on $\bar{M}$, albeit in the $L^{p}$, rather than pointwise, sense.

Theorem 1.1 combines the results of Theorems 6.8 and 6.10, which address the Yamabe problem by constructing solutions to (1.1). This, in turn, requires theory for elliptic differential operators arising from metrics of classes (1.3) and (1.4). Our approach follows that of [Lee06] and [AILSA18], with significant technical work required to adapt those methods to the Sobolev regularity setting. We restrict attention to operators satisfying the following assumption.

Assumption $\mathbf{P}$. We assume that $\mathcal{P}[g]$ is a $d^{\text {th }}$-order differential operator, mapping sections of bundle $E$ to that same bundle, arising from a metric $g$ of class (1.3) or (1.4), and satisfying the following.
\begin{itemize}
\item[(a)] $\mathcal{P}[g]$ acts on sections of a geometric tensor bundle $\boldsymbol{E}$, a subbundle of some tensor bundle $T^{k, l} M$ associated to an invariant subspace of the standard representation of $O(n)$ on $T^{k, l} \mathbb{R}^{n}$; see §3.7.
\item[(b)] $\mathcal{P}[g]$ is geometric, meaning that $\mathcal{P}[g] u$ is a linear function of the components of $u$ and their derivatives up to order $d$, with the coefficient of any $k^{\text {th }}$ order derivative of $u$ being a universal polynomial in components of $g$ and $\operatorname{det}\left(g_{i j}\right)^{-1 / 2}$ that involves at most $d-k$ derivatives of $g$.
\item[(c)] $\mathcal{P}[g]$ is scale natural, meaning that in any coordinate expression of $\mathcal{P}[g] u$, the coefficients of the $k^{\text {th }}$ derivative of $u$ involve at most $d-k$ derivatives of components of $g$ distributed over all factors of that coefficient.
\item[(d)] $\mathcal{P}[g]$ is elliptic in the usual sense, a condition that is well-defined due to (1.6).
\item[(e)] $\mathcal{P}[g]$ satisfies the weak $\boldsymbol{L}^{\mathbf{2}}$ conditions
$$s \geq \frac{d}{2} \quad \text { and } \quad \frac{1}{p}-\frac{s}{n} \leq \frac{1}{2}-\frac{d / 2}{n} .$$
\item[(f)] $\mathcal{P}[g]$ is formally self-adjoint in the sense that for all sections $u, v \in H_{0}^{s, p}(M)$ we have
$$\int_{M}\langle u, \mathcal{P}[g] v\rangle_{g} d V_{g}=\int_{M}\langle\mathcal{P}[g] u, v\rangle_{g} d V_{g},$$
which is interpreted in the sense of duality pairings if $s<d$; see §3.8.
\end{itemize}
Two remarks on these assumptions are in order. First, given a metric $g$ of class (1.3) or (1.4), the multiplication properties of Sobolev spaces imply that there exists a set of compatible Sobolev indices $\mathcal{S}_{d}^{s, p}$ such that if $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and if $\delta \in \mathbb{R}$, then a $d^{\text {th }}$-order operator $\mathcal{P}[g]$ satisfying Assumption P gives rise to continuous maps
$$\begin{aligned}
& H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma-d, q}(M ; E), \\
& X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma-d, q}(M ; E) ;
\end{aligned}$$
see Lemma 8.5 and Proposition 8.1. The scale-natural condition is necessary in order to deduce such elementary mapping properties. This condition excludes the operator $\Delta_{g}+$ $\mathrm{R}[g]^{2}$, as some lowest order terms involve a total of four metric derivatives ( $\partial^{2} g \partial^{2} g$, etc.), while the operator $\Delta_{g}+\mathrm{R}[g]$ is permitted under our hypotheses.
Second, the weak $L^{2}$ conditions of Assumption P imply that the $\mathcal{S}_{d}^{s, p}$ is nonempty, a situation that occurs if and only if $(d / 2,2) \in \mathcal{S}_{d}^{s, p}$; see Lemma 8.2. Thus all operators under consideration admit a weak $L^{2}$ theory, a fact that appears in the characterization of the kernel of $\mathcal{P}[g]$ in the Fredholm results of Theorem 1.2 below. Note also that for second-order operators, the weak $L^{2}$ conditions hold as a consequence of the regularity assumed for the metric $g$.

While the maps (1.8) are continuous for any $\delta \in \mathbb{R}$, they may not be Fredholm. In order to determine those values of $\delta$ for which $\mathcal{P}[g]$ is Fredholm, we consider the corresponding operator $\breve{\mathcal{P}}=\mathcal{P}[\breve{g}]$ arising from the metric $\breve{g}$ on the Poincaré ball hyperbolic space $\mathbb{B}$, and acting on sections of corresponding bundle $\breve{E}$. As detailed in [Lee06], for each geometric operator satisfying Assumption P, there exists a set of complex characteristic exponents corresponding to powers of $\rho$ whose coefficients are arbitrary in formal series solutions to $\breve{\mathcal{P}} u=f$. The location of these exponents in the complex plane is symmetric about the line $\operatorname{Re}(z)=n / 2-w$, where $w$ is the weight of the bundle on which $\breve{\mathcal{P}}$ acts, defined as the covariant rank minus the contravariant rank. The indicial radius of $\breve{\mathcal{P}}$ is defined to be the smallest $R \geq 0$ such that $\breve{\mathcal{P}}$ has a characteristic exponent with real part equal to $n / 2-w+R$. The indicial radius of many important operators can be easily calculated; see [Lee06, Chapter 7].
We use the indicial radius of $\breve{\mathcal{P}}$ to determine those weights $\delta$ for which $\mathcal{P}[g]$ is Fredholm as follows. For any $R \geq 0$ and $1<q \leq \infty$, set
$$\mathcal{D}_{q}(R)=\left\{\delta \in \mathbb{R}:\left|\delta+\frac{n-1}{q}-\frac{n-1}{2}\right|<R\right\} .$$
Extending the work of [Lee06, Chapter 5], Theorems B. 3 and B. 6 imply that operator $\breve{\mathcal{P}}$, having indicial radius $R$, provides isomorphisms
$$\begin{gathered}
H_{\delta}^{\sigma, q}(\mathbb{B} ; \breve{E}) \rightarrow H_{\delta}^{\sigma-d, q}(\mathbb{B} ; \breve{E}) \text { and } \\
X_{\delta}^{\sigma, q}(\mathbb{B} ; \breve{E}) \rightarrow X_{\delta}^{\sigma-d, q}(\mathbb{B} ; \breve{E}),
\end{gathered}$$
provided $\delta \in \mathcal{D}_{q}(R)$ and provided the following isomorphism assumption holds.
Assumption I. We assume that
$$\breve{\mathcal{P}}: H_{0}^{d, 2}(\mathbb{B} ; \breve{E}) \rightarrow H_{0}^{0,2}(\mathbb{B} ; \breve{E})$$
is an isomorphism. This assumption is equivalent, see [Lee06], to assuming the existence of compact $K \subset \mathbb{B}$ and constant $C$ such that
$$\|u\|_{L^{2}(\mathbb{B} ; \breve{E})} \leq C\|\breve{\mathcal{P}} u\|_{L^{2}(\mathbb{B} ; \breve{E})} \quad \text { for all } u \in C_{c p c t}^{\infty}(\mathbb{H} \backslash K ; \breve{E}) .$$
Assumption I implies that the indicial radius $R$ of $\breve{\mathcal{P}}$ is positive; see [Lee06].
The hypothesis that $g$ is asymptotically hyperbolic implies that $\mathcal{P}[g]$ can be closely approximated by $\breve{\mathcal{P}}$ in a small neighborhood of each point on $\partial M$. These approximations, together with the isomorphism properties of $\breve{\mathcal{P}}$, allow us to adapt the parametrix construction in [Lee06] to operators arising from metrics of class (1.3) and (1.4). The result is the following Fredholm theorem, which combines the results of Theorems 9.7 and 9.10, and is accompanied by structure theorems for $\mathcal{P}[g]$; see §9.4.

Theorem 1.2 (Fredholm Theorem). Suppose $g$ is an asymptotically hyperbolic of class (1.3) or (1.4), and that $\mathcal{P}=\mathcal{P}[g]$ is a $d^{\text {th }}$ order operator satisfing Assumptions $P$ and I. Let $R$ be the indicial radius of $\mathcal{P}[\breve{g}]$.
\begin{itemize}
\item[(a)] If $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$ then $\mathcal{P}: H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma-d, q}(M ; E)$ is Fredholm of index zero.
\item[(b)] If $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{\infty}(R)$ then $\mathcal{P}: X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma-d, q}(M ; E)$ is Fredholm of index zero.
\end{itemize}
In both cases, the kernel of $\mathcal{P}$ is the kernel of $\mathcal{P}: H_{0}^{d / 2,2}(M ; E) \rightarrow H_{0}^{-d / 2,2}(M ; E)$.
Organization. This paper is organized in order to efficiently escort the reader to our main results concerning the Yamabe problem in the Sobolev category, which are contained in §6. Thus a number of more technical theorems are deferred to subsequent sections and the appendices.

In §2 we introduce a preferred collection of coordinate systems, which are used in §3 to define Hölder and Sobolev spaces on $M$, along with the "local Sobolev spaces" of Gicquaud-Sakovich [GS12] that play a key technical role in our analysis. Section 4 contains the definition of the fortified spaces. These spaces are used in §5 to define, and establish basic properties of, asymptotically hyperbolic metrics in the Sobolev setting.
Section 6 is the heart of the paper, containing our main results concerning the Yamabe problem in the Sobolev category.
The results of §6 require technical results that are deferred to subsequent sections: a detailed theory for the asymptotic structure of tensor fields appears in §7, properties of elliptic operators arising from Sobolev-scale metrics are established in §8, and in §9 we establish Fredholm theory for such operators. Finally, the appendices contain additional technical results.

Acknowledgements. We thank Iva Stavrov for helpful conversations. This work was supported in part by NSF grant DMS-1263544.

\section*{2. Coordinate systems}

In this section we establish notation and define a number of coordinate systems required to define the function spaces that follow. The constructions are, for the most part, a specialization of those of [Lee06, Chapter 2], with certain choices imposed to simplify later arguments.
2.1. Hyperbolic space. Let $\mathbb{H}$ be the $n$-dimensional half-space model of hyperbolic space with coordinates
$$(x, y)=\left(x^{1}, \ldots, x^{n-1}, y=x^{n}\right) \in \mathbb{R}^{n-1} \times(0, \infty)$$
and metric
$$\breve{g}=y^{-2}\left(\left(d x^{1}\right)^{2}+\cdots+\left(d x^{n-1}\right)^{2}+d y^{2}\right) .$$
We use two prototypical classes of open sets in $\mathbb{H}$. The first are the geodesic balls $B_{r}^{\mathbb{H}}$ of radius $r>0$ centered at $(x, y)=(0,1)$; it will be convenient at times to use the containment
estimate
$$B_{r}^{\mathbb{H}} \subset\left\{(x, y):|x|<\sinh (r), e^{-r}<y<e^{r}\right\}$$
where $|\cdot|$ denotes the Euclidean norm.
The second class of open sets consists of neighborhoods near infinity. Given $r>0$ we define
$$Y_{r}=\{(x, y) \in \mathbb{H}:|x|<r, 0<y<r\} .$$
2.2. Neighborhoods near infinity in $M$. For $r>0$ a collar neighborhood is the region
$$A_{r}=\{p \in M: \rho(p)<r\},$$
and we set $\bar{A}_{r}=\{p \in \bar{M}: \rho(p) \leq r\}$. Using compactness of the boundary we can find $r_{0}>0$ and a smooth projection $\Pi_{\partial}: \bar{A}_{r_{0}} \rightarrow \partial M$ such that
$$\Pi_{\partial} \times \rho: \bar{A}_{r_{0}} \rightarrow \partial M \times\left[0, r_{0}\right]$$
is a diffeomorphism. Fixing this choice of $\Pi_{\partial}$, we will sometimes tacitly identify $\bar{A}_{r_{0}}$ with $\partial M \times\left[0, r_{0}\right]$.

Cover the boundary $\partial M$ with finitely many smooth boundary charts ( $\Omega \subset \partial M, \theta$ ) where each map $\theta$ can be extended smoothly to a neighborhood of $\bar{\Omega}$. Using compactness of the boundary, and shrinking $r_{0}$ if needed, we can assume that for each $\hat{p} \in \partial M$ we can find a boundary chart $\left(\Omega_{\hat{p}}, \theta_{\hat{p}}\right)$ and a neighborhood $U(\hat{p}) \subset \Omega_{\hat{p}}$ such that
$$\theta_{\hat{p}}(U(\hat{p}))=\left\{x \in \mathbb{R}^{n-1}:\left|x-\theta_{\hat{p}}(\hat{p})\right|<r_{0}\right\} .$$
$\theta_{\hat{p}}(\hat{p})=0$. Let $Z_{r_{0}}(\hat{p})=\Pi_{\partial}^{-1}(U(\hat{p})) \cap A_{r_{0}}$ which is conveniently identified with $U(\hat{p}) \times$ $\left(0, r_{0}\right)$. We define smooth coordinates near infinity $\Theta_{\hat{p}}=\left(\theta_{\hat{p}} \circ \Pi_{\partial}-\theta_{\hat{p}}(\hat{p}), \rho\right)$, obtaining diffeomorphisms
$$\Theta_{\hat{p}}: Z_{r_{0}}(\hat{p}) \rightarrow Y_{r_{0}} .$$
Extending our earlier notation, for $r \in\left(0, r_{0}\right]$ we have the neighborhood near infinity
$$Z_{r}(\hat{p})=\Theta_{\hat{p}}^{-1}\left(Y_{r}\right) .$$
2.3. Möbius parametrizations. For each $p_{0} \in A_{r_{0} / 8}$, a Möbius parametrization centered at $p_{0}$ is a map $\Phi: B_{2}^{\mathbb{H}} \rightarrow M$ of the following form. First, pick some $\hat{p} \in \partial M$ such that $p_{0}$ lies in $Z_{r_{0} / 8}(\hat{p})$, and let $\Theta=\Theta_{\hat{p}}$ be the associated coordinates near infinity. Writing $\Theta\left(p_{0}\right)=\left(\theta_{0}, \rho_{0}\right)$ we observe
$$\left(\theta_{0}, 0\right)+\rho_{0} B_{2}^{\mathbb{H}} \subset Y_{r_{0}} ;$$
demonstrating this containment is an easy exercise using (2.1) and the identities $e^{2}<8$ and $\sinh (2)<4$. Relying on the containment (2.2) we define the Möbius parametrization $\Phi: B_{2}^{\mathbb{H}} \rightarrow M$ by
$$(\Theta \circ \Phi)(x, y)=\left(\theta_{0}+\rho_{0} x, \rho_{0} y\right) .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/ef5a0d66-5cf7-49a6-8baf-1ceeba55704c-011.jpg?height=491&width=1316&top_left_y=381&top_left_x=393}
\captionsetup{labelformat=empty}
\caption{Figure 1. Neighborhoods at infinity.}
\end{figure}

The restricted images $\Phi\left(B_{1 / 2}^{\mathbb{H}}\right)$ of the Möbius parametrizations cover $A_{r_{0} / 8}$, and we choose finitely many additional maps $\Phi: B_{2}^{\mathbb{H}} \rightarrow M$, which we will also call Möbius parametrizations, such that their restricted images $\Phi\left(B_{1 / 2}^{\mathbb{H}}\right)$ cover $M \backslash A_{r_{0} / 8}$.
For the purposes of defining function spaces it is useful to choose a preferred countable collection of Möbius parametrizations. From the construction of [Lee06] Lemma 2.2 we select a countable collection of points $p_{i}$ in $A_{r_{0} / 8}$ and corresponding Möbius parametrizations $\Phi_{i}$ such that
\begin{itemize}
\item[(a)] the sets $\Phi_{i}\left(B_{1 / 2}^{\mathbb{H}}\right)$ cover $M$,
\item[(b)] the sets $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right)$ are uniformly locally finite: there is an integer $N$ independent of $i$ such that $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right) \cap \Phi_{j}\left(B_{2}^{\mathbb{H}}\right)=\emptyset$ for all but at most $N$ indices $j$,
\item[(c)] more generally, given a metric $\check{g}$ on $M$ with smooth compactification $\rho^{2} \check{g}$ on $\bar{M}$, for every $K>0$ there exists $N_{K}$ such that if $\operatorname{diam}_{\check{g}}(U) \leq K$ then $\Phi_{j}\left(B_{2}^{\mathbb{H}}\right) \cap U=\emptyset$ for all but at most $N_{K}$ indices $j$.
\end{itemize}

\section*{3. Elementary function spaces}

A tensor bundle over $\bar{M}$ is a bundle $T^{k, l} \bar{M}$ of tensors with covariant rank $k$ and contravariant rank $l$. In this section we gather together facts concerning function spaces of sections of a tensor bundle $E$ over $\bar{M}$ and its induced bundle, which we also denote by $E$, over $M$. In addition to tensor bundles, we also work with 'geometric tensor bundles', which are certain subbundles of tensor bundles and potentially depend on a metric, and its regularity, for their definition. So as to avoid undue initial complication from these regularity concerns, unless otherwise noted we let $E$ denote a tensor bundle over $\bar{M}$ throughout this section. Section 3.7 summarizes the alternations needed to adapt the results below to geometric tensor bundles.
3.1. Definitions. Let $\hat{g}$ be a smooth reference metric on $\bar{M}$ and let $\check{g}=\rho^{-2} \hat{g}$, which is a geodesically complete metric on $M$ with sectional curvatures approaching $-|d \rho|_{\hat{g}}^{2}$ as $\rho \rightarrow$ 0; see (5.1) below. The notation $\check{g}$ is meant to invoke our notation $\breve{g}$ for the hyperbolic metric.
For $k \in \mathbb{N}_{\geq 0}$ and $\alpha \in[0,1]$ we have the usual Banach space $C^{k, \alpha}(\bar{M} ; E)$ of $k$-times continuously differentiable sections of $E$ with $k^{\text {th }}$ derivatives $\hat{\nabla}^{k} u$ that are Hölder continuous of order $\alpha$ with respect to the reference metric $\hat{g}$.
Given $\delta \in \mathbb{R}$ the (interior) weighted Hölder space $C_{\delta}^{k, \alpha}(M ; E)$ consists of the continuous sections of $E$ over $M$ satisfying
$$\|u\|_{C_{\delta}^{k, \alpha}(M ; E)}=\sup _{i} \rho_{i}^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{C^{k, \alpha}\left(B_{1}^{\mathbb{H}}\right)}<\infty,$$
where $\rho_{i}=\rho\left(p_{i}\right)$ and where the $C^{k, \alpha}$ norm on $B_{r}^{\mathbb{H}}$ is computed with respect to the Euclidean metric. When $\alpha=0$ we sometimes omit it from the notation.

For simplicity, for product bundles $M \times F$ we replace $E$ in the notation with the common fiber, e.g. $C_{\delta}^{k, \alpha}(M ; \mathbb{R})$. It is often clear from context what bundle $E$ is under consideration, and we drop this part of the notation, especially in the bodies of proofs, whenever it is convenient to do so to minimize notational clutter. Indeed, strictly speaking, equation (3.1) should have involved the quantities $\left\|\Phi_{i}^{*} u\right\|_{C^{k, \alpha}\left(B_{1}^{\left.\mathbb{H} ; \Phi_{i}^{*} E\right)}\right.}$.
We write $C_{\text {loc }}^{\infty}(M ; E)$ for the smooth sections of $E$ over $M$ and $C_{\text {cpct }}^{\infty}(M ; E)$ consists of the compactly supported smooth sections.
For $k \in \mathbb{N}_{\geq 0}$ and $1 \leq p<\infty$ the Sobolev space $W^{k, p}(\bar{M})$ consists of distributional sections $u$ of $E$ satisfying
$$\|u\|_{W^{k, p}(\bar{M} ; E)}:=\left(\sum_{j=0}^{k} \int_{\bar{M}}\left|\hat{\nabla}^{j} u\right|_{\hat{g}}^{p} d V_{\hat{g}}\right)^{1 / p}<\infty .$$
The interior Sobolev spaces $W^{k, p}(M ; E)$ associated with $\check{g}$ are defined in terms of the analogous norm
$$\|u\|_{W^{k, p}(M ; E)}:=\left(\sum_{j=0}^{k} \int_{M}\left|\check{\nabla}^{j} u\right|_{\check{g}}^{p} d V_{\check{g}}\right)^{1 / p} .$$
Given $\delta \in \mathbb{R}$, we define the weighted Sobolev space
$$W_{\delta}^{k, p}(M ; E)=\rho^{\delta} W^{k, p}(M ; E)$$
with norm $\|u\|_{W_{\delta}^{k, p}(M ; E)}=\left\|\rho^{-\delta} u\right\|_{W^{k, p}(M ; E)}$. We write $L_{\delta}^{p}(M ; E)$ instead of $W_{\delta}^{0, p}(M ; E)$. If $U$ is an open subset of $M$, the $W_{\delta}^{k, p}(U)$ norm is defined by replacing $M$ with $U$ in expression (3.2).

The weighted Sobolev spaces can be generalized to non-integer order of differentiability as follows. Recall that for $s \in \mathbb{R}$ and $1<p<\infty$ the Bessel potential space $H^{s, p}\left(\mathbb{R}^{n}\right)$ is
defined by
$$H^{s, p}\left(\mathbb{R}^{n}\right)=\left\{u \in S^{\prime}\left(\mathbb{R}^{n}\right):\left\|\mathcal{F}^{-1} \Lambda^{s} \mathcal{F} u\right\|_{L^{p}\left(\mathbb{R}^{n}\right)}<\infty\right\} ;$$
here $S^{\prime}\left(\mathbb{R}^{n}\right)$ is the dual space of the Schwartz functions, $\Lambda(\xi)=\left(1+|\xi|^{2}\right)^{1 / 2}$, and $\mathcal{F}$ is the Fourier transform. We use the same notation for spaces of tensor-valued distributions over $\mathbb{R}^{n}$ without reference to the specific bundle, in which case the norm is the sum of the norms of the tensor components. If $U \subset \mathbb{R}^{n}$ is an open set, $H^{s, p}(U)$ consists of the restrictions of distributions in $H^{s, p}\left(\mathbb{R}^{n}\right)$ to $U$ and is endowed with the quotient norm.
Let $\chi \geq 0$ be a smooth function on $\mathbb{R}^{n}$ with support contained in $B_{2}^{\mathbb{H}}$ that equals 1 on $B_{1 / 2}^{\mathrm{H}}$. For $s \in \mathbb{R}, 1<p<\infty$, and $\delta \in \mathbb{R}$ we define the weighted Bessel potential space $H_{\delta}^{s, p}(M ; E)$ in terms of the preferred Möbius parametrizations from §2 to be those distributional fields $u$ such that
$$\|u\|_{H_{\delta}^{s, p}(M ; E)}:=\left(\sum_{i} \rho_{i}^{-\delta p}\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}\right)^{1 / p}<\infty ;$$
here $\rho_{i}=\rho\left(\Phi_{i}(0,1)\right)$, the value of $\rho$ at the point determining the parametrization $\Phi_{i}$. As seen below, these are generalizations of the weighted Sobolev spaces $W_{\delta}^{k, p}(M)$; furthermore, they are the asymptotically hyperbolic analogues of the weighted spaces $h_{p, \mu}^{s}\left(\mathbb{R}^{n}\right)$ from [Tri76], which are used in asymptotically Euclidean contexts.

Gicquaud and Sakovich [GS12] introduced a class of novel function spaces with local differentiability measured in Sobolev scales but with global behavior measured in a uniform sense akin to weighted Hölder norms. Generalizing their work to real scales of differentiability, for $s, \delta \in \mathbb{R}$ and $1<p<\infty$ we define the Gicquaud-Sakovich space $X_{\delta}^{s, p}(M ; E)$ to be the set of distributions such that the norm
$$\|u\|_{X_{\delta}^{s, p}(M ; E)}=\sup _{i} \rho_{i}^{-\delta}\left\|\chi \Phi_{i}^{*} u\right\|_{H_{\delta}^{s, p}\left(\mathbb{R}^{n}\right)}$$
is finite.
We obtain spaces of smooth tensor fields by intersecting the corresponding spaces with finite regularity. Thus
$$\begin{aligned}
& H_{\delta}^{\infty, p}(M ; E)=\bigcap_{s \in \mathbb{R}} H_{\delta}^{s, p}(M ; E), \\
& C_{\delta}^{\infty}(M ; E)=\bigcap_{\substack{k \in \mathbb{N} \\
\alpha \in[0,1]}} C_{\delta}^{k, p}(M ; E) .
\end{aligned}$$
Just as the Hölder parameter $\alpha$ plays no role in the latter intersection, the Sobolev embedding of Proposition 3.3 below shows that $p$ is not relevant to the Gicquaud-Sakovich case; thus we define
$$X_{\delta}^{\infty}(M ; E)=\bigcap_{s \in \mathbb{R}} X_{\delta}^{s, p}(M ; E)$$
for any $1<p<\infty$. Note that the Sobolev embedding, together with Lemma 3.2, implies that $X_{\delta}^{\infty}(M ; E)=C_{\delta}^{\infty}(M ; E)$. However, we use the notation $X_{\delta}^{\infty}(M ; E)$ to emphasize the space's origin.

From the form of equations (3.4) and (3.5) it is clear that $H_{\delta}^{s, p}(M ; E)$ and $X_{\delta}^{s, p}(M ; E)$ are each part of a spectrum of spaces with the former involving an $\ell^{p}$ norm and the latter an $\ell^{\infty}$ norm. One could presumably work with the full range of spaces replacing these with general $\ell^{q}$ norms and still obtain good elliptic theory. But special arguments would presumably be needed in $\ell^{\infty}$ case regardless, so for simplicity we work only with these two special cases.

We have the following norm equivalences. The first two allow us to elide cutoff functions in the norm definitions, and the second two show that the new weighted spaces reduce to known spaces when $s=k \in \mathbb{N}_{\geq 0}$.

Lemma 3.1. Let $s, \delta \in \mathbb{R}$ and $1<p<\infty$.
\begin{itemize}
\item[(a)] For all $1 / 2<r<2$,
$$\|u\|_{H_{\delta}^{s, p}(M ; E)} \sim\left[\sum_{i} \rho_{i}^{-\delta p}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{H}\right)}\right]^{\frac{1}{q}} .$$
\item[(b)] For all $1 / 2<r<2$,
$$\|u\|_{X_{\delta}^{s, p}(M ; E)} \sim \sup _{i} \rho_{i}^{-\delta}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)} .$$
\item[(c)] For $k \in \mathbb{N}_{\geq 0}$
$$\|u\|_{H_{\delta}^{k, p}(M ; E)} \sim\|u\|_{W_{\delta}^{k, p}(M ; E)} .$$
\item[(d)] Taking a supremum over all Möbius parametrizations,
$$\|u\|_{X_{\delta}^{s, p}(M ; E)} \sim \sup _{\Phi}\left\|\Phi^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathrm{H}}\right)} .$$
\end{itemize}
These facts are proved in Appendix A except for part (c) which follows from part (a) and [Lee06] Lemma 3.5. When $s=k \in \mathbb{N}_{\geq 0}$ the equivalent norm in part (d) is essentially the norm of the 'local weighted spaces' from [GS12] and techniques from Appendix A can be used to show that the $X_{\delta}^{k, p}(M ; E)$ norm here is indeed equivalent to the norm from that earlier work.
3.2. Embeddings and dense subsets. The following elementary inclusions are essentially immediate consequences of the definitions involved. The only subtle point is the strict inequalities that appear relating weight parameters $\delta, \delta^{\prime}$; the same phenomenon occurs for integer-based Sobolev spaces (cf. [Lee06] Lemma 3.6).

Lemma 3.2 (Basic inclusions on M). Suppose $1<p<\infty, s, \delta \in \mathbb{R}, k \in \mathbb{N}_{\geq 0}$, and $0 \leq \alpha \leq 1$. The following embeddings are continuous under the listed restrictions.
$$\begin{array}{ll}
H_{\delta}^{s, p}(M ; E) \hookrightarrow H_{\delta^{\prime}}^{s, p^{\prime}}(M ; E), & p \geq p^{\prime}, \quad \delta+\frac{n-1}{p}>\delta^{\prime}+\frac{n-1}{p^{\prime}} ; \\
H_{\delta}^{s, p}(M ; E) \hookrightarrow X_{\delta}^{s, p^{\prime}}(M ; E), & p \geq p^{\prime} ; \\
X_{\delta}^{s, p}(M ; E) \hookrightarrow X_{\delta}^{s, p^{\prime}}(M ; E), & p \geq p^{\prime} ; \\
C_{\delta}^{k, \alpha}(M ; E) \hookrightarrow X_{\delta}^{k, p}(M ; E) ; & \\
C_{\delta}^{k, \alpha}(M ; E) \hookrightarrow H_{\delta^{\prime}}^{k, p}(M ; E), & \delta>\delta^{\prime}+\frac{n-1}{p} ; \\
X_{\delta}^{s, p}(M ; E) \hookrightarrow H_{\delta^{\prime}}^{s, p}(M ; E), & \delta>\delta^{\prime}+\frac{n-1}{p} .
\end{array}$$
As discussed in Appendix A, Sobolev embedding for the weighted spaces with general $s \in \mathbb{R}$ follows from Sobolev embedding for $H^{s, p}\left(B_{r}^{\mathbb{H}}\right)$ and techniques identical to those used for spaces with $s \in \mathbb{N}_{\geq 0}$.

Proposition 3.3 (Sobolev embeddings). Suppose $1<p<\infty, r, s, \delta \in \mathbb{R}, k \in \mathbb{N}_{\geq 0}$ and $0<\alpha<1$. The following embeddings are continuous under the listed restrictions.
$$\begin{aligned}
& H_{\delta}^{s, p}(M ; E) \hookrightarrow H_{\delta}^{r, q}(M ; E), \\
& X_{\delta}^{s, p}(M ; E) \hookrightarrow X_{\delta}^{r, q}(M ; E), \\
& H_{\delta}^{s, p}(M ; E) \hookrightarrow C_{\delta}^{k, \alpha}(M ; E), \\
& X_{\delta}^{s, p}(M ; E) \hookrightarrow C_{\delta}^{k, \alpha}(M ; E),
\end{aligned}$$
$$\begin{aligned}
& \frac{1}{p}-\frac{s}{n} \leq \frac{1}{q}-\frac{r}{n}, \quad r \leq s, \quad p \leq q ; \\
& \frac{1}{p}-\frac{s}{n} \leq \frac{1}{q}-\frac{r}{n}, \quad r \leq s ; \\
& \frac{1}{p}-\frac{s}{n} \leq-\frac{k+\alpha}{n} ; \\
& \frac{1}{p}-\frac{s}{n} \leq-\frac{k+\alpha}{n} .
\end{aligned}$$
Appendix A contains proofs of following compactness and density results.
Proposition 3.4 (Rellich Lemma). Suppose $1<p<\infty$ and $s, s^{\prime}, \delta, \delta^{\prime} \in \mathbb{R}$. The following inclusions are compact under the listed restrictions.
$$\begin{array}{ll}
H_{\delta}^{s, p}(M ; E) \rightarrow H_{\delta^{\prime}}^{s^{\prime}, p}(M ; E), & s>s^{\prime}, \quad \delta>\delta^{\prime} ; \\
X_{\delta}^{s, p}(M ; E) \rightarrow X_{\delta^{\prime}}^{s^{\prime}, p}(M ; E), & s>s^{\prime}, \quad \delta>\delta^{\prime} .
\end{array}$$

Proposition 3.5 (Density of Smooth Elements). Suppose $1<p<\infty$ and $s, \delta \in \mathbb{R}$.
\begin{itemize}
\item[(a)] $C_{\text {cpct }}^{\infty}(M ; E)$ is dense in $H_{\delta}^{s, p}(M ; E)$.
\item[(b)] $C_{\text {loc }}^{\infty}(M ; E) \cap X_{\delta}^{s, p}(M ; E)$ is dense in $X_{\delta}^{s, p}(M ; E)$.
\end{itemize}
Note that in general $C_{\delta}^{\infty}(M ; E)$ is not dense in $X_{\delta}^{s, p}(M ; E)$; see Proposition A.6.
3.3. Covariant derivatives. When performing computations in the coordinates of a Möbius parametrization, is useful to be able to transfer between the the pullback connection $\Psi^{*} \hat{\nabla}$ and the connection $\nabla_{\mathbb{E}}$ of the Euclidean connection with respect to local coordinates. One can generally substitute one for the other, and the following lemma is the tool needed to justify this. See also Lemma 3.15 below which concerns transfering tensors such as $\hat{g}$ on $\bar{M}$ to tensors in weighted spaces on $M$.
As an application, Lemma 3.9 below constructs equivalent norms for Sobolev and Gicquaud-Sakovich spaces using $\hat{\nabla}$.

Lemma 3.6. Let $\Phi_{i}$ be a Möbius parametrization and let $D=\Phi_{i}^{*} \hat{\nabla}-\nabla_{\mathbb{E}}$. For each $k \in \mathbb{N}_{\geq 0}$ the coordinate expressions
$$\begin{aligned}
& \left(\rho_{i}^{-1} \nabla_{\mathbb{E}}\right)^{k} \rho_{i}^{-2} \Phi_{i}^{*} \hat{g}, \\
& \left(\rho_{i}^{-1} \nabla_{\mathbb{E}}\right)^{k} \rho_{i}^{2} \Phi_{i}^{*} \hat{g}^{-1}, \\
& \left(\rho_{i}^{-1} \nabla_{\mathbb{E}}\right)^{k} \rho_{i}^{-1} D
\end{aligned}$$
are uniformly bounded (with respect to $i$ ) in any $C^{\ell}\left(B_{2}^{\mathbb{H}}\right)$.
Proof. Writing $\hat{g}=\hat{g}_{a b} d \Theta^{a} d \Theta^{b}$ with respect to the boundary coordinates associated with $\Phi_{i}$,
$$\begin{array}{r}
\left(\Phi_{i}^{*} \hat{g}\right)=\left(\rho_{i}\right)^{2} \hat{g}_{a b}\left(\theta_{0}+\rho_{i} x, \rho_{i} y\right) d x^{a} d x^{b} \\
\left(\Phi_{i}^{*} \hat{g}^{-1}\right)=\left(\rho_{i}\right)^{-2} \hat{g}^{a b} \partial_{x^{a}} \partial_{x^{b}}
\end{array}$$
Since $\hat{g}$ and $\hat{g}^{-1}$ are smooth up to the boundary of $\bar{M}$, bounds for the expressions (3.6) and (3.7) follow from bounds for derivatives in boundary coordinates along with the observation that every derivative of the pullbacks introduces an additional factor of $\rho_{i}$. Bounds for (3.8) follow from writing $D$ as a contraction of
$$\left(\Phi_{i}^{*} \hat{g}\right)^{-1} \nabla_{\mathbb{E}} \Phi_{i}^{*} \hat{g}=\rho_{i}^{2}\left(\Phi_{i}^{*} \hat{g}\right)^{-1} \nabla_{\mathbb{E}} \rho_{i}^{2} \Phi_{i}^{*} \hat{g} .$$
and bounds for (3.6)-(3.7). \(\square\)

Lemma 3.7. Let $1<p<\infty, s \in \mathbb{R}$ and $\delta \in \mathbb{R}$. Then $\hat{\nabla}$ and $\check{\nabla}$ are continuous maps
$$\begin{aligned}
& H_{\delta}^{s, p}(M ; E) \rightarrow H_{\delta}^{s-1, p}\left(M ; T^{0,1} M \otimes E\right), \\
& X_{\delta}^{s, p}(M ; E) \rightarrow X_{\delta}^{s-1, p}\left(M ; T^{0,1} M \otimes E\right) .
\end{aligned}$$
Proof. The continuity of $\hat{\nabla}$ follows from working in the domains of Möbius parametrizations and Lemma 3.6. Since $\Phi_{i}^{*} \check{g}=y^{-2} \rho_{i}^{-2} \check{g}$ a computation shows $\Phi_{i}^{*} \check{\nabla}=\Phi_{i}^{*} \hat{\nabla}+\Gamma$ where $\Gamma$ is a universal tensor with coefficients only involving coordinate derivatives of $y$ and the continuity of $\check{\nabla}$ follows. \(\square\)

The following lemma, a consequence of the Gagliardo-Nirenberg inequality, is used below to establish alternate norms for Sobolev and Gicquaud-Sakovich spaces.

Lemma 3.8. Let $1<p<\infty, m \in \mathbb{N}_{\geq 0}$, and $s \in \mathbb{R}$ with $s \geq m$. Suppose for some $r>0$ that $u$ is a real-valued function with $u \in H^{0, p}\left(B_{r}^{\mathbb{H}}\right)$ and $\nabla_{\mathbb{E}}^{m} u \in H^{s-m, p}\left(B_{r}^{\mathbb{H}}\right)$. Then $u \in H^{s, p}\left(B_{r}^{\mathbb{H}}\right)$ and
$$\|u\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)} \sim\|u\|_{H^{0, p}\left(B_{r}^{\mathbb{H}}\right)}+\left\|\nabla_{\mathbb{E}}^{m} u\right\|_{H^{s-m, p}\left(B_{r}^{\mathbb{H}}\right)}$$
with implicit constants independent of $u$.
Proof. Let $k=\lfloor s\rfloor$ so $s=k+\alpha$ for some $0 \leq \alpha<1$. Observe that since $\left\|\nabla_{\mathbb{E}}^{k} u\right\|_{H^{\alpha, p}\left(B_{r}^{\mathbb{H}}\right)} \lesssim$ $\left\|\nabla_{\mathbb{E}}^{m} u\right\|_{H^{s-m, p}\left(B_{r}^{\mathbb{H}}\right)}$ it suffices to prove the result assuming $m=k$. That is, we wish to show
$$\|u\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)} \lesssim\|u\|_{H^{0, p}\left(B_{r}^{\mathbb{H}}\right)}+\left\|\nabla_{\mathbb{E}}^{k} u\right\|_{H^{\alpha, p}\left(B_{r}^{\mathbb{H}}\right)} ;$$
the reverse inequality is obvious.
If $u \in H^{0, p}\left(B_{r}^{\mathbb{H}}\right)$ and $\nabla_{\mathbb{E}}^{k} u \in H^{\alpha, p}\left(B_{r}^{\mathbb{H}}\right)$ then $\nabla_{\mathbb{E}}^{k} u \in H^{0, p}\left(B_{r}^{\mathbb{H}}\right)$ as well. So the Gagliardo-Nirenberg interpolation inequality implies $u \in H^{k, p}\left(B_{r}^{\mathbb{H}}\right)$ and
$$\|u\|_{H^{k, p}\left(B_{r}^{\mathbb{H}}\right)} \lesssim\|u\|_{H^{0, p}\left(B_{r}^{\mathbb{H}}\right)}+\left\|\nabla_{\mathbb{E}}^{k} u\right\|_{H^{0, p}\left(B_{r}^{\mathbb{H}}\right)} .$$
This completes the proof when $\alpha=0$.
Now suppose $0<\alpha<1$. Then [Tri10, Theorem 3.3.5] implies that an equivalent norm on $H^{s, p}\left(B_{r}^{\mathbb{H}}\right)$ is
$$\|u\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)}=\|u\|_{H^{k+\alpha, p}\left(B_{r}^{\mathbb{H}}\right)} \sim \sum_{0 \leq j \leq k}\left\|\nabla_{\mathbb{E}}^{j} u\right\|_{H^{\alpha, p}\left(B_{r}^{\mathbb{H}}\right)} .$$
Moreover, if $j<k$ then $\left\|\nabla_{\mathbb{E}}^{j} u\right\|_{H^{\alpha, p}\left(B_{r}^{\mathbb{H}}\right)} \lesssim\left\|\nabla_{\mathbb{E}}^{j} u\right\|_{H^{1, p}\left(B_{r}^{\mathbb{H}}\right)} \lesssim\|u\|_{H^{k, p}\left(B_{r}^{\mathbb{H}}\right)}$. Hence
$$\|u\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)} \lesssim\left\|\nabla_{\mathbb{E}}^{k} u\right\|_{H^{\alpha, p}\left(B_{r}^{\mathbb{H}}\right)}+\|u\|_{H^{k, p}\left(B_{r}^{\mathbb{H}}\right)} .$$
The result now follows from equations (3.9) and (3.10). \(\square\)

Lemma 3.9. Let $1<p<\infty, m \in \mathbb{N}$, and $s \in \mathbb{R}$ with $s \geq m$. We have the following norm equivalences for sections of tensor bundle $E$.
\begin{itemize}
\item[(a)] $\|u\|_{H_{\delta}^{s, p}(M ; E)} \sim\|u\|_{H_{\delta}^{0, p}(M ; E)}+\left\|\hat{\nabla}^{m} u\right\|_{H_{\delta}^{s-m, p}\left(M ; T^{0, m} M \otimes E\right)}$.
\item[(b)] $\|u\|_{X_{\delta}^{s, p}(M ; E)} \sim\|u\|_{X_{\delta}^{0, p}(M ; E)}+\left\|\hat{\nabla}^{m} u\right\|_{X_{\delta}^{s-m, p}\left(M ; T^{0, m} M \otimes E\right)}$.
\end{itemize}

Proof. The two results are proved nearly identically; we treat part (a). It suffices to show
$$\|u\|_{H_{\delta}^{s, p}(M)} \lesssim\|u\|_{H_{\delta}^{s, p}(M)}+\left\|\hat{\nabla}^{m} u\right\|_{H_{\delta}^{s-m, p}(M)},$$
as the reverse estimate is obvious.
Let $\Phi_{i}$ be a Möbius parametrization. Applying Lemma 3.6 to the components of $\Phi_{i}^{*} u$ we find
$$\begin{aligned}
\left\|\nabla_{\mathbb{E}}^{m} \Phi_{i}^{*} u\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{H}}\right)} & \lesssim\left\|\Phi_{i}^{*} \hat{\nabla}^{m} u\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{H}}\right)}+\sum_{j=0}^{m-1}\left\|\nabla_{\mathbb{E}}^{j} \Phi_{i}^{*} u\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{H}}\right)} \\
& \lesssim\left\|\Phi_{i}^{*} \hat{\nabla}^{m} u\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{H}}\right)}+\left\|\Phi_{i}^{*} u\right\|_{H^{s-1, p}\left(B_{1}^{\mathbb{H}}\right)} .
\end{aligned}$$

Hence from Lemma 3.8 we conclude
$$\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\Phi_{i}^{*} u\right\|_{H^{0, p}\left(B_{1}^{\mathbb{H}}\right)}+\left\|\Phi_{i}^{*} \hat{\nabla}^{m} u\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{H}}\right)}+\left\|\Phi_{i}^{*} u\right\|_{H^{s-1, p}\left(B_{1}^{\mathbb{H}}\right)} .$$
A standard interpolation argument to control the final term in this expression then leads to
$$\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\Phi_{i}^{*} u\right\|_{H^{0, p}\left(B_{1}^{\mathbb{H}}\right)}+\left\|\Phi_{i}^{*} \hat{\nabla}^{m} u\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{H}}\right)}$$
and the result now follows from multiplying by an appropriate factor of $\rho_{i}$, raising to $p^{\text {th }}$ powers and summing. \(\square\)
3.4. Tensor operations. It is easy to prove the continuity of contraction operations by working in the domains of Möbius parametrizations.

Lemma 3.10 (Contractions). Suppose $E=T^{k_{1}, k_{2}} \bar{M}$ for some $k_{1}, k_{2} \in \mathbb{N}$ and let $\mathrm{c}: E \rightarrow$ $E^{\prime}=T^{k_{1}-1, k_{2}-1} \bar{M}$ be a contraction operation on a pair of indices. Then c extends to the continuous maps
$$\begin{aligned}
H_{\delta}^{s, p}(M ; E) & \rightarrow H_{\delta}^{s, p}\left(M ; E^{\prime}\right), \\
X_{\delta}^{s, p}(M ; E) & \rightarrow X_{\delta}^{s, p}\left(M ; E^{\prime}\right)
\end{aligned}$$
for all $1<p<\infty$ and all $s, \delta \in \mathbb{R}$.

Multiplication in Sobolev spaces involves a number of compatability conditions between the spaces parameters that each encode either a notion of 'multiplication cannot generically improve regularity' or 'multiplication must respect duality of Sobolev spaces'. See, for example, the appendix of [HMT22] for a demonstration of the continuity of multiplication between Bessel potential spaces over bounded open subsets of $\mathbb{R}^{n}$ under the conditions listed below. Continuity of tensor products follows from this scalar result and Lemma 3.1.

Proposition 3.11 (Product estimates). Let $E_{1}$ and $E_{2}$ be tensor bundles over $\bar{M}$. Suppose $s_{1}, s_{2}, \sigma \in \mathbb{R}, 1<p_{1}, p_{2}, q<\infty$ ), and $\delta_{1}, \delta_{2} \in \mathbb{R}$. and define
$$\frac{1}{r_{i}}=\frac{1}{p_{i}}-\frac{s_{i}}{n}, \quad \frac{1}{r}=\frac{1}{q}-\frac{\sigma}{n}, \quad i=1,2 .$$
Tensor product is a continuous map
$$\begin{aligned}
& H_{\delta_{1}}^{s_{1}, p_{1}}\left(M ; E_{1}\right) \times H_{\delta_{2}}^{s_{2}, p_{2}}\left(M ; E_{2}\right) \rightarrow H_{\delta_{1}+\delta_{2}}^{\sigma, q}\left(M ; E_{1} \otimes E_{2}\right), \\
& X_{\delta_{1}}^{s_{1}, p_{1}}\left(M ; E_{1}\right) \times H_{\delta_{2}}^{s_{2}, p_{2}}\left(M ; E_{2}\right) \rightarrow H_{\delta_{1}+\delta_{2}}^{\sigma, q}\left(M ; E_{1} \otimes E_{2}\right), \\
& X_{\delta_{1}}^{s_{1}, p_{1}}\left(M ; E_{1}\right) \times X_{\delta_{2}}^{s_{2}, p_{2}}\left(M ; E_{2}\right) \rightarrow X_{\delta_{1}+\delta_{2}}^{\sigma, q}\left(M ; E_{1} \otimes E_{2}\right)
\end{aligned}$$
provided
$$\begin{gathered}
\frac{1}{q} \leq \frac{1}{p_{1}}+\frac{1}{p_{2}}, \\
0 \leq s_{1}+s_{2}, \\
\sigma \leq \min \left(s_{1}, s_{2}\right), \\
\max \left(\frac{1}{r_{1}}, \frac{1}{r_{2}}\right) \leq \frac{1}{r},
\end{gathered}$$
where the last inequality is strict if
$$\min \left(\frac{1}{r_{1}}, \frac{1}{r_{2}}\right)=0 .$$
We frequently use Proposition 3.11 in a context where we are multiplying
$$\hat{\nabla}^{k_{1}} u_{1} \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u_{\ell}$$
with each $u_{i} \in H_{\text {loc }}^{s, p}\left(M ; E_{i}\right)$ with $s>n / p$. The result lies in $H_{\text {loc }}^{s-k, p}(M ; E)$, where $k=$ $k_{1}+\cdots+k_{\ell}$ and $E$ is the appropriate bundle, under the two restrictions on $k$ in (3.11) below. We have, for example, the following.

Corollary 3.12. Suppose $1<p<\infty, s \in \mathbb{R}$ and $s>n / p$. Given $k_{1}, \cdots, k_{\ell} \in \mathbb{N}_{\geq 0}$ define $k=k_{1}+\cdots+k_{\ell}$ and suppose
$$\begin{aligned}
s & \geq k / 2, \\
\frac{1}{p}-\frac{s}{n} & \leq \frac{1}{2}-\frac{k}{2 n} .
\end{aligned}$$
Given tensor bundles $E_{k}$ over $\bar{M}, 1 \leq k \leq \ell$, tensor product is a continuous map
$$H_{\delta_{1}}^{s-k_{1}, p}\left(M ; E_{1}\right) \times \cdots \times H_{\delta_{\ell}}^{s-k_{\ell}, p}\left(M ; E_{\ell}\right) \rightarrow H_{\delta_{1}+\cdots+\delta_{\ell}}^{s-k}\left(M ; \otimes_{k=1}^{\ell} E_{k}\right)$$
for any weights $\delta_{i}$.
3.5. Interpolation. Suppose $X_{1}$ and $X_{2}$ are two Banach spaces that both embed as subspaces of an ambient Hausdorff topological space; such a pair is called an interpolation couple. For each $0<\theta<1$ there is a complex interpolation space $\left[X_{1}, X_{2}\right]_{\theta}$ satisfying $X_{1} \cap X_{2} \subset\left[X_{1}, X_{2}\right]_{\theta} \subset X_{1}+X_{2}$. See §A. 3 for a quick overview complex interpolation and the proof of the following two interpolation results. Note that Lemma 3.14 concerning interpolation and Gicquaud-Sakovich spaces is far from optimal but suffices for our purposes.

Theorem 3.13 (Complex Interpolation). Let $1<p_{2}<p_{2}<\infty, s_{1}, s_{2} \in \mathbb{R}$ and $\delta_{1}, \delta_{2} \in \mathbb{R}$. Suppose $\theta \in(0,1)$ and let
$$\begin{aligned}
s & =(1-\theta) s_{1}+\theta s_{2}, \\
\frac{1}{p} & =(1-\theta) \frac{1}{p_{1}}+\theta \frac{1}{p_{2}}, \\
\delta & =(1-\theta) \delta_{1}+\theta \delta_{2} .
\end{aligned}$$
Then
$$\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta}=H_{\delta}^{s, p}(M ; E)$$
as sets, and the norms are equivalent.
Lemma 3.14. Let $\left(A_{0}, A_{1}\right)$ be an interpolation pair and suppose $T$ is a linear map
$$T: A_{0}+A_{1} \rightarrow X_{\delta_{0}}^{s_{0}, p_{0}}(M ; E)+X_{\delta_{1}}^{s_{1}, p_{1}}(M ; E)$$
for some $1<p_{0}, p_{1}<\infty, s_{0}, s_{1} \in \mathbb{R}$, and $\delta_{0}, \delta_{1} \in \mathbb{R}$. If $T$ restricts to continuous maps $T_{k}: A_{k} \rightarrow X_{\delta_{k}}^{s_{k}, p_{k}}(M ; E), k=0,1$, then for each $0<\theta<1$ the map $T$ also restricts to a continuous map
$$T_{\theta}:\left[A_{0}, A_{1}\right]_{\theta} \rightarrow X_{\delta}^{s, p}(M ; E),$$
where $s, p$ and $\delta$ are as in equations (3.12). Moreover,
$$\left\|T_{\theta}\right\| \lesssim\left\|T_{0}\right\|^{1-\theta}\left\|T_{1}\right\|^{\theta}$$
with implicit constant independent of $T_{0}, T_{1}$.
3.6. Embedding spaces on $\bar{M}$ into weighted spaces on $M$. The construction of fortified spaces in §4 relies fundamentally on the observation that function spaces on $\bar{M}$ embed continuously into weighted spaces on $M$. Doing so requires the notion of the weight of a tensor bundle, the number of covariant indices minus the number of contravariant indices. Thus, a metric has weight 2 and a tangent vector has weight -1. Lemma 3.7(a) of [Lee06], reproduced below, is the template for analogous embeddings for Sobolev spaces.

Lemma 3.15 (Hölder $\bar{M}$ inclusions). Suppose $k \in \mathbb{N}_{\geq 0}, 0 \leq \alpha \leq 1$, and that $E$ has weight w. Then
$$C^{k, \alpha}(\bar{M} ; E) \hookrightarrow C_{w}^{k, \alpha}(M ; E) .$$
As a first step to generalizing this result we establish the following norm equivalences.
Lemma 3.16. Suppose $k \in \mathbb{N}_{\geq 0}, 1<p<\infty$, and that $E$ has weight $w$. We have the following norm equivalences.
\begin{itemize}
\item[(a)] $\|u\|_{W_{\delta}^{k, p}(M ; E)} \sim \sum_{j=0}^{k}\left\|\hat{\nabla}^{j} u\right\|_{L_{\delta}^{p}\left(M ; T^{0, j} M \otimes E\right)}$.
\item[(b)] $\|u\|_{X_{\delta}^{k, p}(M ; E)} \sim \sum_{j=0}^{k}\left\|\hat{\nabla}^{j} u\right\|_{X_{\delta}^{0, p}\left(M ; T^{0, j} M \otimes E\right)}$.
\end{itemize}
\begin{itemize}
\item[(c)] $\|u\|_{W^{k, p}(\bar{M} ; E)} \sim \sum_{j=0}^{k}\left\|\hat{\nabla}^{j} u\right\|_{L_{w+j-n / p}^{p}\left(M ; T^{0, j} M \otimes E\right)}$.
\end{itemize}

Proof. Part (b) follows from Lemmas 3.7 and 3.9. The remaining equivalences follow from an elementary computation using the following observations:
\begin{itemize}
\item[-] A tensor $u$ of weight $w$ satisfies $|u|_{\check{g}}=\rho^{w}|u|_{\hat{g}}$.
\item[-] The volume elements of $\hat{g}$ and $\check{g}$ are related by $d V_{\check{g}}=\rho^{-n} d V_{\hat{g}}$.
\item[-] Lemma 3.15 implies $\rho^{-1} d \rho \in C_{0}^{\infty}\left(M ; T^{0,1} M\right)$.
\item[-] Lemma 3.15 also implies that the difference tensor between the Levi-Civita connections of $\check{g}$ and $\hat{g}$ lies in $C_{0}^{\infty}\left(M ; T^{0,2} M\right)$ since
$$\check{\nabla}-\hat{\nabla}=\rho^{-1} \bar{D},$$
where $\bar{D} \in C^{\infty}(\bar{M})$ is a tensor of weight 1.
\item[-] The tensor product is continuous
$$C_{0}^{\infty}\left(M ; E_{1}\right) \otimes L_{\delta}^{p}\left(M ; E_{2}\right) \rightarrow L_{\delta}^{p}\left(M ; E_{1} \otimes E_{2}\right) .$$ \(\square\)
\end{itemize}

Note that the first two observations above yield the useful identity
$$\|u\|_{L^{p}(\bar{M} ; E)}=\|u\|_{L_{w-n / p}^{p}}(M ; E) .$$
In the following generalization of Lemma 3.15 the space $H^{s, p}(\bar{M} ; E)$ is the usual Sobolev space when $s \in \mathbb{N}_{\geq 0}$ and is obtained by interpolation for $0<s<\infty$. See, e.g., the construction of [Tay10, Chapter 4] for the case $p=2$, which generalizes to arbitrary 1 < $p<\infty$.

Proposition 3.17 (Sobolev $\bar{M}$ inclusions). Let $w$ be the weight of $E$ and suppose $1<p<$ $\infty$ and $s \in \mathbb{R}$. The following embeddings are continuous under the listed restrictions.
$$\begin{array}{ll}
H^{s, p}(\bar{M} ; E) \hookrightarrow H_{w-n / p}^{s, p}(M ; E), & s \geq 0 ; \\
H^{s, p}(\bar{M} ; E) \hookrightarrow X_{w}^{s, p}(M ; E), & s \geq 1 \text { and } s>n / p .
\end{array}$$
Proof. In the case $s \in \mathbb{N}_{\geq 0}$, inclusion (3.15) follows from parts a and c of Lemma 3.16; the general case follows by interpolation.
For embedding (3.16), first consider the case $s=k \in \mathbb{N}_{\geq 0}$. From Lemma 3.16(b) it suffices to show that $\hat{\nabla}^{i} u \in X_{w}^{0, p}(M)$ for $0 \leq i \leq k$. If $\frac{1}{p}-\frac{k-i}{n}<0$, then Sobolev embedding on $\bar{M}$, Lemma 3.15, and the basic inclusions from Lemma 3.2 imply there exists $\alpha>0$ such that
$$\begin{aligned}
\hat{\nabla}^{i} u \in H^{k-i, p}(\bar{M}) & \hookrightarrow C^{0, \alpha}(\bar{M}) \\
& \hookrightarrow C_{w+i}^{0, \alpha}(M) \\
& \hookrightarrow C_{w}^{0, \alpha}(M) \\
& \hookrightarrow X_{w}^{0, p}(M) .
\end{aligned}$$

On the other hand, if $\frac{1}{p}-\frac{k-i}{n}>0$ then with $\frac{1}{q}=\frac{1}{p}-\frac{k-i}{n}$ we obtain
$$\begin{aligned}
\hat{\nabla}^{i} u \in H^{k-i, p}(\bar{M}) & \hookrightarrow L^{q}(\bar{M}) \\
& =L_{w+i-n / q}^{q}(M) \\
& \hookrightarrow L_{w}^{q}(M) \\
& \hookrightarrow X_{w}^{0, q}(M) \hookrightarrow X_{w}^{0, p}(M)
\end{aligned}$$
since $i-\frac{n}{q}=k-\frac{n}{p}>0$. Finally, the boundary case $\frac{1}{p}-\frac{k-i}{n}=0$ can be treated by first observing that this can only occur for $i>0$ since $k>n / p$. We can therefore proceed as in the case $\frac{1}{p}-\frac{k-i}{n}=0$ above but now choosing any $q>p$ with $i-n / q>0$.
The case where $s>1$ is non-integral follows from interpolation (Lemma 3.14) noting that we can use $H^{k, q_{0}}(\bar{M})$ and $H^{\left.k+1, q_{1}\right)}(\bar{M})$ as endpoints of interpolation where $k \in \mathbb{N}$ satsfies $k<s<k+1$ and where $k q_{0}=(k+1) q_{1}=s p>n$. \(\square\)

The restriction $s \geq 1$ in embedding (3.16) is presumably an artifact of the proof technique and $s>0$ would be more natural. A traveling bump argument shows, however, that the requirement $s>n / p$ is close to optimal: if $p<n$ we can apply a scaling argument to find smooth functions $f_{i}$ each with support on $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right)$ such that $\left\|f_{i}\right\|_{H^{1, p}(\bar{M} ; \mathbb{R})}=1$ for each $i$, and yet $\left\|f_{i}\right\|_{X_{0}^{1, p}(\bar{M} ; \mathbb{R})} \rightarrow \infty$.
3.7. Geometric tensor bundles. Following the terminology of [Lee06], a geometric tensor bundle over $\bar{M}$ is a subbundle $E$ of some tensor bundle $T^{k, l} \bar{M}$ that is associated with an invariant subspace of the standard representation of $O(n)$ (or $S O(n)$ if $\bar{M}$ is orientable) on $T^{k, l} \mathbb{R}^{n}$. These include bundles associated with $G L(n ; \mathbb{R})$ representations such as the symmetric tensors in $T^{0,2} \bar{M}$, but also metric-dependent objects such as the trace-free subbundle.

Section A. 5 contains results specific to function spaces of sections of geometric tensor bundles, and we summarize the salient points here. Let $h \in X_{0}^{S_{0}, p_{0}}\left(M ; T^{0,2} M\right)$ be a metric on $M$, where $1<p_{0}<n$ and $s_{0} \geq 1$ satisfy $s_{0}>n / p_{0}$, such that that $\bar{h}=\rho^{2} h$ extends continuously to a metric on $\bar{M}$. (The condition $s_{0}>n / p_{0}$ ensures $h \in C^{0, \alpha}\left(M ; T^{0,2} M\right)$ for some $\alpha>0$, whereas $s_{0} \geq 1$ is a mild technical condition that is always satisfied in our applications here.) Let $E_{h}$ be a geometric tensor bundle associated with $h$ and let $\hat{E}$ be its ambient tensor bundle. We say that a section $u$ of $\hat{E}$ is an element of $X_{0}^{s_{0}, p_{0}}\left(M ; E_{h}\right)$ if it is a section of $E_{h}$ in the classical $C^{0}$ sense, and if $u \in X_{0}^{s_{0}, p_{0}}(M ; \hat{E})$. Sections with other regularity classes arise as linear combinations of sections in $X_{0}^{s_{0}, p_{0}}\left(M ; E_{h}\right)$ with coefficients in either $H_{\delta}^{s, p}(M ; \mathbb{R})$ or $X_{\delta}^{s, p}(M ; \mathbb{R})$ for some choice of $s$ or $p$. In order to make sense of the multiplication we imposes conditions on these parameters and we define $\mathcal{S}_{0}^{s_{0}, p_{0}}$ to be
the set of pairs $(s, p) \in \mathbb{R} \times(1, \infty)$ such that
$$\begin{gathered}
-s_{0} \leq s \leq s_{0} \\
\frac{1}{p_{0}}-\frac{s_{0}}{n} \leq \frac{1}{p}-\frac{s}{n} \leq \frac{1}{p_{0}^{*}}+\frac{s_{0}}{n} .
\end{gathered}$$
The set $S_{0}^{s_{0}, p_{0}}$ is a special case of related sets $S_{d}^{s_{0}, p_{0}}$ defined in §8 concerning $d^{\text {th }}$ order differential operators. Proposition 3.11 ensures that if $u \in H_{\delta}^{s, p}(M ; \mathbb{R})$ for some $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$ and if $v \in X_{0}^{s_{0}, p_{0}}(M ; \hat{E})$ then $u v \in H_{\delta}^{s, p}(M ; \hat{E})$, and a similar fact is true for coefficients in $X_{\delta}^{s, p}(M ; \mathbb{R})$. We say that $u$ is an element of $H_{\delta}^{s, p}\left(M ; E_{h}\right)$ for some $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$ if $u$ can be written as a finite sum
$$u=\sum_{j=1}^{J} u_{j} v_{j}$$
where each $v_{j} \in X_{0}^{s_{0}, p_{0}}\left(M ; E_{h}\right)$ and each $u_{j} \in H_{\delta}^{\sigma, q}(M ; \mathbb{R})$. In fact, using the condition that $h$ admits a continuous compactification, we show in §(A.5) that one can find a fixed collection $\left\{v_{j}\right\}_{j=1}^{J}$ of elements of $X_{0}^{s, p}\left(M ; E_{h}\right)$ and continuous maps $u \mapsto u_{j}$ such that each $u \in H_{\delta}^{s, p}\left(M ; E_{h}\right)$ has the form (3.17). As a consequence, $H_{\delta}^{\sigma, q}\left(M ; E_{h}\right)$ is a closed subspace of $H_{\delta}^{\sigma, q}(M ; \hat{E})$, and the norm for $H_{\delta}^{\sigma, q}\left(M ; E_{h}\right)$ is simply inherited from its ambient space. A similar analysis holds in the Gicquaud-Sakovich case and $X_{\delta}^{\sigma, q}\left(M ; E_{h}\right)$ is a closed subspace of $X_{\delta}^{\sigma, q}(M ; E)$.
With only a few exceptions all of the results discussed up until this point carry over (either obviously or due to proofs in §A.5) replacing all the tensor bundles with geometric tensor bundles associated with the same metric $h$ satisfying the regularity conditions listed above. There is, of course, the obvious caveat that all of the Sobolev parameters occurring in the statements must additinally lie in the set $\mathcal{S}_{0}^{s_{0}, p_{0}}$ associated with $h$. The following additional adjustments are also required.
\begin{itemize}
\item[(a)] Proposition 3.5 concerning density needs adjusting as there may be no non-zero smooth sections in a general geometric tensor bundle. See Proposition A. 16 instead.
\item[(b)] Lemma 3.7 requires an obvious modification with respect to the target space because $E_{h}$ need not be parallel with respect to the covariant derivatives $\hat{\nabla}$ and $\check{\nabla}$.
\item[(c)] Modest additional formalism is required to generalize Proposition 3.17, especially with respect to interpreting sections of $H^{s, p}\left(\bar{M} ; E_{\bar{h}}\right)$. We do not use this extension, which is left as an exercise for the reader.
\end{itemize}
3.8. Duality. Let $g_{\mathbb{E}}$ be the Euclidean metric on $\mathbb{R}^{n}$. The $L^{2}$ inner product
$$\langle u, v\rangle_{\left(\mathbb{R}^{n}, g_{\mathbb{E}}\right)}=\int_{\mathbb{R}^{n}} u v d V_{g_{\mathbb{B}}}$$
for smooth compactly supported functions extends to a continuous bilinear form on $H^{-s, p^{*}}\left(\mathbb{R}^{n}\right) \times$ $H^{s, p}\left(\mathbb{R}^{n}\right)$ for any $s \in \mathbb{R}$ and $p, p^{*} \in(1, \infty)$ with $\frac{1}{p}+\frac{1}{p^{*}}=1$. Moreover, the map
$$u \mapsto\langle u, \cdot\rangle_{\left(\mathbb{R}^{n}, g_{\mathbb{E}}\right)}$$
yields an isomorphism between $H^{-s, p^{*}}\left(\mathbb{R}^{n}\right)$ and the dual space $\left(H^{s, p}\left(\mathbb{R}^{n}\right)\right)^{*}$. An analogous statement for the weighted Bessel potential spaces involves a choice of metric, and we can formulate duality for metrics with the regularity discussed at the start of §3.7.

Proposition 3.18. (Duality) Suppose metric $h \in X_{0}^{s_{0}, p_{0}}\left(M ; T^{0,2} M\right)$ for some $1<p_{0}<\infty$, with $s_{0} \geq 1$ and $s_{0}>n / p_{0}$, and suppose $\rho^{2} h$ admits a continuous extension to $\bar{M}$.
Let $E_{h}$ be a geometric tensor bundle over $\bar{M}$ associated with $h$ and for compactly supported sections $u, v \in X_{0}^{s_{0}, p_{0}}\left(M ; E_{h}\right)$ define
$$\langle u, v\rangle_{(M, h)}=\int_{M}\langle u, v\rangle_{h} d V_{h},$$
where $\langle\cdot, \cdot\rangle_{h}$ is the inner product induced by $h$ on the fibers of $E_{h}$.
If $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$ then $\left(-s, p^{*}\right) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$ as well and $\langle\cdot, \cdot\rangle_{(M, h)}$ extends to a continuous bilinear map
$$H_{-\delta}^{-s, p^{*}}\left(M ; E_{h}\right) \times H_{\delta}^{s, p}\left(M ; E_{h}\right) \rightarrow \mathbb{R} .$$
for each $\delta \in \mathbb{R}$. Moreover, the map
$$v \mapsto\langle v, \cdot\rangle_{(M, h)}$$
is an isomorphism $H_{-\delta}^{-s, p^{*}}\left(M ; E_{h}\right) \rightarrow\left(H_{\delta}^{s, p}\left(M ; E_{h}\right)\right)^{*}$, and $H_{\delta}^{-s, p}\left(M ; E_{h}\right)$ is precisely the subset of $H_{\text {loc }}^{-s, p}\left(M ; E_{h}\right)$ such that $\langle v, \cdot\rangle_{M ; E_{h}}$ extends to an element of $\left(H_{\delta}^{s, p}\left(M ; E_{h}\right)\right)^{*}$.
3.9. Nonlinearities. Nonlinear functions can be applied to functions in Sobolev spaces once the parameters are sufficiently regular so as to imply Hölder continuity. We first consider the case where the nonlinear function vanishes at zero, in which case decay rates at infinity are preserved.

Proposition 3.19. Suppose $1<p<\infty, s \geq 1, s>n / p$, and $\delta \geq 0$. Let $F \in C^{k, \alpha}(\mathbb{R})$ for some $k \in \mathbb{N}$ and $\alpha \in[0,1)$ with $k+\alpha>s$ and suppose $F(0)=0$.
\begin{itemize}
\item[(a)] If $u \in H_{\delta}^{s, p}(M ; \mathbb{R})$, then $F(u) \in H_{\delta}^{s, p}(M ; \mathbb{R})$ and
$$\|F(u)\|_{H_{\delta}^{s, p}(M ; \mathbb{R})} \lesssim\|u\|_{H_{\delta}^{s, p}(M ; \mathbb{R})}\left(1+\|u\|_{L^{\infty}(M ; \mathbb{R})}^{k+\alpha}\right) .$$
\item[(b)] If $u \in X_{\delta}^{s, p}(M ; \mathbb{R})$, then $F(u) \in X_{\delta}^{s, p}(M ; \mathbb{R})$ and
$$\|F(u)\|_{X_{\delta}^{s, p}(M ; \mathbb{R})} \lesssim\|u\|_{X_{\delta}^{s, p}(M ; \mathbb{R})}\left(1+\|u\|_{L^{\infty}(M ; \mathbb{R})}^{k+\alpha}\right) .$$
\end{itemize}
The implicit constants above depend on $F$ and on a choice of constant $K$ such that $\|u\|_{L^{\infty}(M ; \mathbb{R})} \leq$ $K$ but are otherwise independent of $u$.