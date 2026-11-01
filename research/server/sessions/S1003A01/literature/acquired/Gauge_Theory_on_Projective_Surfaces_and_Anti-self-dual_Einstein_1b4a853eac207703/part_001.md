---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Gauge Theory on Projective Surfaces and Anti-self-dual Einstein Metrics in Dimension Four]

---
source_file: 1509_04276.pdf
converter: mathpix
format: mmd
---

\title{
GAUGE THEORY ON PROJECTIVE SURFACES AND ANTI-SELF-DUAL EINSTEIN METRICS IN DIMENSION FOUR
}

\author{
MACIEJ DUNAJSKI AND THOMAS METTLER
}

\begin{abstract}
Given a projective structure on a surface $N$, we show how to canonically construct a neutral signature Einstein metric with non-zero scalar curvature as well as a symplectic form on the total space $M$ of a certain rank 2 affine bundle $M \rightarrow N$. The Einstein metric has anti-self-dual conformal curvature and admits a parallel field of anti-self-dual planes. We show that locally every such metric arises from our construction unless it is conformally flat. The homogeneous Einstein metric corresponding to the flat projective structure on $\mathbb{R} \mathbb{P}^{2}$ is the non-compact real form of the Fubini-Study metric on $M=\operatorname{SL}(3, \mathbb{R}) / \operatorname{GL}(2, \mathbb{R})$. We also show how our construction relates to a certain gauge-theoretic equation introduced by Calderbank.
\end{abstract}

\section*{1. Introduction}

A projective structure on a smooth surface $N$ is an equivalence class [D] of torsion-free connections on $T N$ having the same unparametrised geodesics. Canonically associated to a projective surface $(N,[\nabla])$ is a rank 2 affine bundle $M \rightarrow N$ which is modelled on $T^{*} N$ and which arises as the complement of a certain $\mathbb{R P}^{1}$-subbundle of the projectivised cotractor bundle $\mathbb{P}(E) \rightarrow N$ of $(N,[\nabla])$. The aim of this paper is to canonically construct a pair $(g, \Omega)$ on $M$, consisting of a neutral signature anti-self-dual (ASD) Einstein metric $g$, as well as a symplectic form $\Omega$. The pair $(g, \Omega)$ is related by an endomorphism $I:$ $T M \rightarrow T M$ whose square is the identity and hence it defines what is known as a bi-Lagrangian structure or almost para-Kähler structure on $M$. We construct the pair $(g, \Omega)$ by taking a $\operatorname{GL}(2, \mathbb{R})$-quotient of the Cartan geometry associated to $(N,[\nabla])$ and in doing so, establish a one-to-one correspondence between projective vector fields on $(N,[\nabla])$ and sympletic Killing vector fields on $(M, g, \Omega)$. In addition, we observe that every Killing vector field of $(M, g)$ is symplectic with respect to $\Omega$ and hence the lift of a projective vector field on ( $N,[\nabla]$ ).

The sections of the affine bundle $M \rightarrow N$ are in one-to-one correspondence with the [D] representative connections and hence the choice of a representative connection $\nabla \in[\nabla]$ provides a diffeomorphism $T^{*} N \rightarrow M$. Pulling back the pair ( $g, \Omega$ ) with this diffeomorphism gives a pair ( $g_{\nabla}, \Omega_{\nabla}$ ) on $T^{*} N$ which - in canonical local coordinates $\left(x^{i}, \xi_{i}\right)$ on the contangent bundle $\nu: T^{*} N \rightarrow N$ - takes the form
$$\begin{aligned}
g_{\nabla} & =\left(d \xi_{i}-\left(\Gamma_{i j}^{k} \xi_{k}-\xi_{i} \xi_{j}-R_{(i j)}\right) d x^{j}\right) \odot d x^{i} \\
\Omega_{\nabla} & =d \xi_{i} \wedge d x^{i}+\frac{1}{3} R_{[i j]} d x^{i} \wedge d x^{j}
\end{aligned}$$
Here $\Gamma_{j k}^{i}$ denote the Christoffel symbols and $R_{(i j)}, R_{[i j]}$ the components of the symmetric - and antisymmetric part of the Ricci curvature of ∇ with respect to the coordinates $\left(x^{i}\right)$. The first two summands in the coordinate expression for the metric $g_{\nabla}$ give the classical Patterson-Walker metric $h_{\nabla}$ which is

\footnotetext{
Date: June 6, 2017.
}
canonically defined on $T^{*} N$ from a torsion-free connection ∇ on $N$. The metric $g_{\nabla}$ is thus part of a one-parameter family $g_{\nabla, \Lambda}$ of metrics on $T^{*} N$ defined by
$$g_{\nabla, \Lambda}=h_{\nabla}+\Lambda \lambda^{2}+\left(\frac{1}{\Lambda}\right) v^{*} \operatorname{Ric}^{+}(\nabla),$$
where $\lambda$ denotes the tautological 1-form of $T^{*} N$ and $\Lambda$ is any non-zero real number. The family of metrics $g_{\nabla, \Lambda}$ already appeared in [11] where they are locally characterized as the neutral signature type II Osserman metrics whose Jacobi operator have non-zero eigenvalues. However, the relation of the metric $g_{\nabla}=g_{\nabla, 1}$ to projective differential geometry is not noted there. The reader may also consult [15, 16] and references cited therein for results about the classification of neutral signature four-dimensional Osserman metrics. All the metrics in the family $g_{\nabla, \Lambda}$ are anti-self-dual and Einstein with scalar curvature $24 \Lambda \neq 0$. Moreover, in Theorem 4.1 we show that all ASD Einstein metrics which admit a parallel ASD totally null distributions are locally of the form (1.1). We also observe that if a connection ∇ has skew-symmetric Ricci tensor, then the limit $\Lambda \rightarrow 0$ of the above family $g_{\nabla, \Lambda}$ yields an anti-self-dual Ricci flat metric which previously appeared in the work of Derdziński [14].

In the final part of the article we relate the metric $g$ to a certain gauge-theoretic equation introduced by Calderbank in [7]. We also discuss some examples.

This paper mainly concerns itself with the two-dimensional case, but there are obvious higher dimensional generalisations which we briefly discuss in an Appendix.

Acknowledgments. The authors wish to thank Andreas Čap, Andrzej Derdziński, Nigel Hitchin, and Claude LeBrun for helpful discussions regarding the contents of this paper. TM is grateful for travel support via the grant SNF 200020_144438 of the Swiss National Science Foundation.

\section*{2. Preliminaries}
2.1. Algebraic preliminaries. As usual, we let $\mathbb{R}^{n}$ the denote the space of column vectors of height $n$ with real entries and $\mathbb{R}_{n}$ the space of row vectors of length $n$ with real entries. Matrix multiplication $\mathbb{R}_{n} \times \mathbb{R}^{n} \rightarrow \mathbb{R}$ is a non-degenerate pairing identifying $\mathbb{R}_{n}$ with the dual vector space of $\mathbb{R}^{n}$.

Let $\mathbb{R} \mathbb{P}^{2}=\left(\mathbb{R}^{3} \backslash\{0\}\right) / \mathbb{R}^{*}$ denote space of lines in $\mathbb{R}^{3}$ through the origin, i.e., two-dimensional real projective space. For any nonzero $x \in \mathbb{R}^{3}$ let $[x]$ denote its corresponding point in $\mathbb{R P}^{2}$. Let $\mathbb{R P}_{2}=\left(\mathbb{R}_{3} \backslash\{0\}\right) / \mathbb{R}^{*}$ denote the dual projective space and likewise for any nonzero $\xi \in \mathbb{R}_{3}$ we denote by $[\xi]$ its corresponding point in $\mathbb{R P}_{2}$.

The group $\operatorname{SL}(3, \mathbb{R})$ acts from the left on $\mathbb{R}^{3}$ by matrix multiplication and this action descends to define a transitive left action on $\mathbb{R P}^{2}$. Likewise, $\operatorname{SL}(3, \mathbb{R})$ acts on $\mathbb{R}_{3}$ from the left by the rule
$$h \cdot \xi=\xi h^{-1}$$
for $h \in \operatorname{SL}(3, \mathbb{R})$ and this actions descends to define a transitive left action on $\mathbb{R} \mathbb{P}_{2}$. The stabiliser subgroup of $\left[x_{0}\right] \in \mathbb{R P}^{2}$ where $x_{0}={ }^{t}(100)$ will be denoted by $H$, so that $\mathbb{R P}^{2} \simeq \operatorname{SL}(3, \mathbb{R}) / H$. The elements of $H \subset \operatorname{SL}(3, \mathbb{R})$ are matrices of the form
$$b \rtimes a=\left(\begin{array}{cc}
\operatorname{det} a^{-1} & b \\
0 & a
\end{array}\right),$$
with $a \in \mathrm{GL}(2, \mathbb{R})$ and $b \in \mathbb{R}_{2}$. Denoting by $\mathbb{R P}_{1} \subset \mathbb{R} \mathbb{P}_{2}$ the projective line consisting of those elements $[\xi] \in \mathbb{R P}_{2}$ which satisfy $[\xi] \cdot\left[x_{0}\right]=0$, the group $H$ acts faithfully from the left by affine transformations
on the affine 2 -space $\mathbb{A}_{2}=\mathbb{R} \mathbb{P}_{2} \backslash \mathbb{R} \mathbb{P}_{1}$. Indeed, if we represent an element in $\mathbb{A}_{2}$ by a vector $(1, \xi) \in \mathbb{R}_{3}$ with $\xi \in \mathbb{R}_{2}$, we obtain
$$(1, \xi)\left(\begin{array}{cc}
\operatorname{det} a^{-1} & b \\
0 & a
\end{array}\right)^{-1}=\left(\operatorname{det} a,-b a^{-1} \operatorname{det} a+\xi a^{-1}\right)$$
so that the induced affine transformation is
$$(b \rtimes a) \cdot \xi=\xi a^{-1} \operatorname{det} a^{-1}-b a^{-1} .$$
Consequently, we may naturally think of $H$ as the 2-dimensional real affine group.
2.2. Projective structures. In this preliminary subsection we shall summarise basic facts about projective structures on a surface which underlie the results of the paper; the reader may consult [2] for additional details. Let $N$ be a connected smooth surface. By an affine torsion-free connection on $N$ we mean a torsion-free connection on its tangent bundle $T N$. The set of torsion-free connections on $T N$ is an affine space modelled on the smooth sections of the vector bundle $V=T N \otimes S^{2}\left(T^{*} N\right)$. We have a canonical trace mapping $V \rightarrow T^{*} N$ and an inclusion
$$\imath: T^{*} N \rightarrow V, \quad v \mapsto v \otimes \mathrm{Id}+\mathrm{Id} \otimes v .$$
Consequently, $V$ decomposes into a direct sum $V \simeq V_{0} \oplus T^{*} N$, where $V_{0}$ denotes the trace-free part of $V$.

The curvature $R^{\nabla}$ of the connection ∇ is defined by
$$R^{\nabla}(X, Y) Z=\nabla_{X} \nabla_{Y} Z-\nabla_{Y} \nabla_{X} Z-\nabla_{[X, Y]} Z$$
for all vector fields $X, Y, Z$ on $N$. We define the Ricci curvature of ∇ to be
$$\operatorname{Ric}(\nabla)(X, Y)=\operatorname{tr}\left(Z \rightarrow R^{\nabla}(Z, X) Y\right)$$
for all vector fields $X, Y$ on $N .{ }^{1}$ The Ricci curvature need not be symmetric and we denote by $\operatorname{Ric}^{ \pm}(\nabla)$ its symmetric and anti-symmetric part.

A vector field $K$ defined on some open set $U \subset N$ is called affine for the torsion-free connection ∇ on $T N$ if its local flow $\phi_{t}$ preserves the geodesics of ∇ . The set of such vector fields on $U$ is a Lie subalgebra of the Lie algebra of vector fields on $U$ which we will denote by $\mathcal{A}_{\nabla}(U)$. Clearly, $K \in \mathcal{A}_{\nabla}(U)$ if and only if
$$0=\mathcal{L}_{K} \nabla:=\lim _{t \rightarrow 0} \frac{1}{t}\left(\phi_{t}^{*} \nabla-\nabla\right)$$
on $U$. A straightforward computation yields that (2.1) is equivalent to the vanishing of the symmetric part of $\nabla^{2} K$. By definition, the map $K \mapsto \mathcal{L}_{K} \nabla$ takes values in $\Gamma(V)$ and hence defines a second order linear differential operator $\mathcal{L}^{\nabla}: \Gamma(T N) \rightarrow \Gamma(V)$.

A projective structure $[\nabla]$ on $N$ is an equivalence class of torsion-free connections on $T N$, where two such connections $\hat{\nabla}$ and ∇ are called projectively equivalent if they share the same unparametrised geodesics. By a classical result of Weyl [46] this is equivalent to $\hat{\nabla}-\nabla$ being pure trace, that is, the existence of a 1-form $\Upsilon$ on $N$ such that
$$\hat{\nabla}_{X} Y=\nabla_{X} Y+\Upsilon(X) Y+\Upsilon(Y) X,$$

\footnotetext{
${ }^{1}$ This definition is common in projective differential geometry, but differs from the more standard definition, where the Ricci curvature is defined as $\operatorname{Ric}(\nabla)(X, Y)=\operatorname{tr}\left(Z \rightarrow R^{\nabla}(Z, Y) X\right)$.
}
for all vector fields $X, Y$ on $N$. Consequently, the set of projective structures on $N$ is an affine space modelled on the smooth sections of $V_{0}$.

Using index notation, the projective Schouten tensor P of ∇ is defined by
$$\mathrm{P}_{i j}=R_{(i j)}+\frac{1}{3} R_{[i j]},$$
where $R_{(i j)}$ denotes the symmetric part - and $\mathrm{R}_{[i j]}$ the anti-symmetric part of the Ricci curvature of ∇ . If we change the connection in the projective class using (2.2) then
$$\hat{\mathrm{P}}_{i j}=\mathrm{P}_{i j}-\nabla_{i} \Upsilon_{j}+\Upsilon_{i} \Upsilon_{j}, \quad \hat{\mathrm{P}}_{[i j]}=\mathrm{P}_{[i j]}-\nabla_{[i} \Upsilon_{j]} .$$

A vector field $K$ defined on some open set $U \subset N$ is said to be projective for [∇] if its local flow $\phi_{t}$ preserves the unparametrised geodesics of [V]. The set of such vector fields on $U$ is a Lie subalgebra of the Lie algebra of vector fields on $U$ which we will denote by $\mathcal{P}_{[\text {V] }}(U)$. A vector field $K$ belongs to $\mathcal{P}_{[\nabla]}(U)$ if and only if
$$0=\mathcal{L}_{K}[\nabla]:=\left(\mathcal{L}_{K} \nabla\right)_{0}$$
on $U$, where $\nabla \in[\nabla]$, and the explicit expression for $\mathcal{L}_{K} \nabla$ is given by (3.11). By definition, the right hand side of (2.4) is a smooth section of $V_{0}$ so that the map $K \mapsto \mathcal{L}_{K}[\nabla]$ defines a second order linear differential operator $\mathcal{L}^{[\nabla]}: \Gamma(T N) \rightarrow \Gamma\left(V_{0}\right)$.

If $N$ is orientable, we may restrict attention to connections in [D] which preserve an area form $\epsilon$ on $N$, so that $\nabla \epsilon=0$. We shall refer to such connections as special [21]. Note that special connections always exist globally. For special connections the Schouten tensor is symmetric, that is $\mathrm{P}_{[i j]}=0$. The residual freedom in special connections within a given projective class is given by (2.2) where $\Upsilon=d f$ for some smooth real-valued function $f$ on $N$. The special condition is preserved if $\hat{\epsilon}=e^{3 f} \epsilon$.
2.3. The Cartan geometry of a projective surface. In [10] (see also [26] for a modern reference), Cartan associates to a projective structure [ $\nabla$ ] on a smooth surface $N$ a Cartan geometry ( $\pi: P_{[\nabla]} \rightarrow$ $N, \theta)$ of type ( $\operatorname{SL}(3, \mathbb{R}), H$ ) which consists of a principal right $H$-bundle $\pi: P_{[\nabla]} \rightarrow N$ together with a Cartan connection $\theta \in \Omega^{1}\left(P_{[V]}, \mathfrak{S l}(3, \mathbb{R})\right)$ having the following properties:
\begin{itemize}
\item[(i)] $\theta\left(X_{v}\right)=v$ for fundamental vector field $X_{v}$ on $P_{[\mathrm{V}]}$;
\item[(ii)] $\theta_{u}: T_{u} P_{[\nabla]} \rightarrow \mathfrak{s l}(3, \mathbb{R})$ is an isomorphism for all $u \in P_{[\nabla]}$;
\item[(iii)] $R_{h}^{*} \theta=\operatorname{Ad}\left(h^{-1}\right) \theta=h^{-1} \theta h$ for all $h \in H$;
\item[(iv)] write
$$\theta=\left(\begin{array}{cc}
-\operatorname{tr} \phi & \eta \\
\omega & \phi
\end{array}\right)$$
for an $\mathbb{R}^{2}$-valued 1-form $\omega=\left(\omega^{i}\right)$, an $\mathbb{R}_{2}$-valued 1-form $\eta=\left(\eta_{i}\right)$ and a $\mathfrak{g} \mathfrak{l}(2, \mathbb{R})$-valued 1-form $\phi=\left(\phi_{j}^{i}\right)$. If $X_{x}$ is a vector field on $P_{[\nabla]}$ having the property that
$$\omega\left(X_{x}\right)=x, \quad \eta\left(X_{x}\right)=0, \quad \phi\left(X_{x}\right)=0,$$
for some non-zero $x \in \mathbb{R}^{2}$, then the the integral curve of $X_{x}$, when projected to $N$, becomes a geodesic of [V] and conversely every geodesic of [V] arises in this way;
\item[(v)] The curvature 2-form $\Theta$ satisfies
$$\Theta=d \theta+\theta \wedge \theta=\left(\begin{array}{cc}
0 & L(\omega \wedge \omega) \\
0 & 0
\end{array}\right),$$
for a smooth curvature function $L: P_{[\nabla]} \rightarrow \operatorname{Hom}\left(\mathbb{R}^{2} \wedge \mathbb{R}^{2}, \mathbb{R}_{2}\right)$.
\end{itemize}

Note the Bianchi-identity
$$d \Theta=\Theta \wedge \theta-\theta \wedge \Theta,$$
the algebraic part of which reads
$$0=L(\omega \wedge \omega) \wedge \omega .$$
A projective structure [D] is called flat if locally [∇] is defined by a flat connection. A consequence of Cartan's construction is that a projective structure is flat if and only if $L$ vanishes identically.

Remark 2.1. Cartan's bundle is unique in the following sense: If $\left(\hat{\pi}: \hat{P}_{[\nabla]} \rightarrow N, \hat{\theta}\right)$ is another Cartan geometry of type ( $\mathrm{SL}(3, \mathbb{R}), H$ ) satisfying the properties (iii),(iv),(v), then there exists a $H$-bundle isomorphism $\psi: P_{[\nabla]} \rightarrow \hat{P}_{[\nabla]}$ so that $\psi^{*} \hat{\theta}=\theta$.

Remark 2.2. Let $w$ be any real number. The line bundle associated to $P_{[\nabla]}$ via the $H$-representation $\chi_{w}$ : $H \rightarrow \operatorname{GL}^{+}(1, \mathbb{R}), b \rtimes a \mapsto|\operatorname{det} a|^{w}$ will be denoted by $\mathcal{E}(w)$. Following [2], we call its sections densities of projective weight $w$. In particular, nowhere vanishing sections of $\mathcal{E}(1)$ are known as projective scales.
2.4. The choice of a representative connection. For what follows it is necessary to have an explicit construction of the Cartan geometry $\left(\pi: P_{[\nabla]} \rightarrow N, \theta\right)$ of a projective surface $(N,[\nabla])$. This can be achieved conveniently by fixing a representative connection $\nabla \in[\nabla]$. To this end let $v: F \rightarrow N$ denote the coframe bundle of $N$ whose fibre at at point $p \in N$ consists of the linear isomorphisms $u: T_{p} N \rightarrow$ $\mathbb{R}^{2}$. The group GL(2, $\mathbb{R}$ ) acts transitively from the right on each $v$-fibre by the rule $R_{a}(u)=u \cdot a=a^{-1} \circ u$ for all $a \in \mathrm{GL}(2, \mathbb{R})$. This action turns $v: F \rightarrow N$ into a principal right $\operatorname{GL}(2, \mathbb{R})$-bundle. The bundle $F \rightarrow N$ is equipped with a tautological $\mathbb{R}^{2}$-valued 1-form $\omega=\left(\omega^{i}\right)$ satisfying the equivariance property $\left(R_{a}\right)^{*} \omega=a^{-1} \omega$, where the 1-form $\omega$ is defined by $\omega_{u}=u \circ v_{u}^{\prime}$.

Suppose $\varphi=\left(\varphi_{j}^{i}\right) \in \Omega^{1}(F, \mathfrak{g l}(2, \mathbb{R}))$ is the connection 1-form of $\nabla \in[\nabla]$, then we have the structure equations
$$\begin{aligned}
d \omega^{i} & =-\varphi_{j}^{i} \wedge \omega^{j}, \\
d \varphi_{l}^{k}+\varphi_{j}^{k} \wedge \varphi_{l}^{j} & =\frac{1}{2}\left(\delta_{i}^{k} \mathrm{P}_{j l}-\delta_{j}^{k} \mathrm{P}_{i l}-2 \mathrm{P}_{[i j]} \delta_{l}^{k}\right) \omega^{i} \wedge \omega^{j},
\end{aligned}$$
where - by slight abuse of notation - the $\mathbb{R}_{2} \otimes \mathbb{R}_{2}$-valued map $\mathrm{P}=\left(\mathrm{P}_{i j}\right)$ represents the Schouten tensor of ∇ . We define a right $H$-action on $F \times \mathbb{R}_{2}$ by the rule
$$(u, \xi) \cdot(b \rtimes a)=\left(\operatorname{det} a^{-1} a^{-1} \circ u, \xi a \operatorname{det} a-b \operatorname{det} a\right),$$
for all $b \rtimes a \in H$ and $(u, \xi) \in F \times \mathbb{R}_{2}$. Denoting by $\pi: F \times \mathbb{R}_{2} \rightarrow N$ the basepoint projection of the first factor, this action turns $\pi: F \times \mathbb{R}_{2} \rightarrow N$ into a principal right $H$-bundle over $N$. On $F \times \mathbb{R}_{2}$ we define the $\mathfrak{s l}(3, \mathbb{R})$-valued 1-form
$$\theta=\left(\begin{array}{cc}
-\frac{1}{3} \operatorname{tr} \varphi+\xi \omega & -d \xi+\xi \varphi-\omega^{t} \mathrm{P}^{t}-\xi \omega \xi \\
\omega & \varphi-\frac{1}{3} \operatorname{Itr} \varphi-\omega \xi
\end{array}\right) .$$
Then $\left(\pi: F \times \mathbb{R}_{2} \rightarrow N, \theta\right)$ is a Cartan geometry of type $(\operatorname{SL}(3, \mathbb{R}), H)$ satisfying the properties (iii) to (v) for the projective structure defined by ∇ . It follows from the uniqueness part of Cartan's construction that $\left(\pi: F \times \mathbb{R}_{2} \rightarrow N, \theta\right)$ is isomorphic to the Cartan geometry of ( $N,[\nabla]$ ).
2.5. The Patterson-Walker metric. In [36], Patterson and Walker use an affine torison-free connection ∇ on a smooth manifold to construct a split-signature metric on its cotangent bundle. Here we briefly review their construction for the case of a surface $N$. As before, let $v: F \rightarrow N$ denote the coframe bundle of $N$ with tautological 1-form $\omega$ and let $\varphi$ denote the connection form of $\nabla$. The cotangent bundle $v: T^{*} N \rightarrow N$ is the bundle associated to the $\operatorname{GL}(2, \mathbb{R})$-representation $\chi$ on $\mathbb{R}_{2}$ defined by the rule $\chi(a) \xi=\xi a^{-1}$ for all $a \in \mathrm{GL}(2, \mathbb{R})$ and $\xi \in \mathbb{R}_{2}$. The 1-forms on $F \times \mathbb{R}_{2}$ that are semibasic for the projection $\zeta: F \times \mathbb{R}_{2} \rightarrow T^{*} N \simeq\left(F \times \mathbb{R}_{2}\right) / \sim_{\chi}$ are spanned by the components of $\omega$ and $d \xi-\xi \varphi$. In particular, the equivariance properties of $\omega, \theta$ and $\xi$ imply that the tensor field $(d \xi-\xi \varphi) \omega=$ $\left(d \xi_{i}-\xi_{k} \varphi_{i}^{k}\right) \otimes \omega^{i}$ is invariant under the GL( $2, \mathbb{R}$ )-right action,
$$\left(R_{a}\right)^{*}(d \xi-\xi \varphi) \omega=\left(d \xi a-\xi a a^{-1} \varphi a\right) a^{-1} \omega=(d \xi-\xi \varphi) \omega .$$
It follows that there exists a unique split-signature metric $h_{\nabla}$ and a unique 2-form $-\Omega_{0}$ on $T^{*} N$ such that
$$\zeta^{*} h_{\nabla}=\left(d \xi_{i}-\xi_{k} \varphi_{i}^{k}\right) \circ \omega^{i} \quad \text { and } \quad \zeta^{*} \Omega_{0}=-\left(d \xi_{i}-\xi_{k} \varphi_{i}^{k}\right) \wedge \omega^{i} .$$
Note that the 1 -form $\xi \omega$ is semi-basic for the projection $\zeta$ and invariant under the $\operatorname{GL}(2, \mathbb{R})$-right action, hence the pullback of a unique 1-form $\lambda$ on $T^{*} N$ which is of course the tautological 1-form (or Liouville 1-form) of $T^{*} N$. The structure equation (2.7) gives
$$-d\left(\xi_{i} \omega^{i}\right)=-d \xi_{i} \wedge \omega^{i}+\xi_{k} \varphi_{i}^{k} \wedge \omega^{i},$$
hence $\Omega_{0}=-d \lambda$ is just the canonical symplectic form of $T^{*} N$ and independent of ∇ . The metric $h_{\nabla}$ does however depend on ∇ and is called the Patterson-Walker metric or the Riemannian extension of $\nabla$. In canonical local coordinates $\left(x^{i}, \boldsymbol{\xi}_{i}\right)$ on an open subset of the cotangent bundle it takes the form
$$h_{\nabla}=d \xi_{i} \odot d x^{i}-\Gamma_{i j}^{k} \xi_{k} d x^{i} \odot d x^{j},$$
where $\Gamma_{j k}^{i}$ denote the Christoffel symbols of ∇ with respect to the coordinates $\left(x^{i}\right)$.
2.6. Anti-self-duality. Let $M$ be an oriented four-dimensional manifold with a metric $g$ of signature $(2,2)$. The Hodge * operator is an involution on two-forms, and induces a decomposition
$$\Lambda^{2}\left(T^{*} M\right)=\Lambda_{+}^{2}\left(T^{*} M\right) \oplus \Lambda_{-}^{2}\left(T^{*} M\right)$$
of two-forms into self-dual (SD) and anti-self-dual (ASD) components, which only depends on the conformal class of $g$. The Riemann tensor of $g$ has the symmetry $R_{a b c d}=R_{[a b][c d]}$ so can be thought of as a map $\mathcal{R}: \Lambda^{2}\left(T^{*} M\right) \rightarrow \Lambda^{2}\left(T^{*} M\right)$ which admits a decomposition under (2.11):
$$\mathcal{R}=\left(\begin{array}{c|c}
C_{+}-2 \Lambda & \phi \\
\hline \phi & C_{-}-2 \Lambda
\end{array}\right) .$$
Here $C_{ \pm}$are the SD and ASD parts of the (conformal) Weyl tensor, $\phi$ is the trace-free Ricci curvature, and $-24 \Lambda$ is the scalar curvature which acts by scalar multiplication. The metric $g$ is ASD if $C_{+}=0$. It is ASD and Einstein if $C_{+}=0$ and $\phi=0$. Finally it is ASD Ricci-flat (or equivalently hyper-symplectic) if $C_{+}=\phi=\Lambda=0$. In this case the Riemann tensor is also anti-self-dual.

Locally there exist real rank-two vector bundles $\mathbb{S}, \mathbb{S}^{\prime}$ (spin-bundles) over $M$ equipped with parallel symplectic structures $\varepsilon, \varepsilon^{\prime}$ such that
$$T M \cong \mathbb{S} \otimes \mathbb{S}^{\prime}$$
is a canonical bundle isomorphism, and
$$g\left(v_{1} \otimes w_{1}, v_{2} \otimes w_{2}\right)=\varepsilon\left(v_{1}, v_{2}\right) \varepsilon^{\prime}\left(w_{1}, w_{2}\right)$$
for $v_{1}, v_{2} \in \Gamma(\mathbb{S})$ and $w_{1}, w_{2} \in \Gamma\left(\mathbb{S}^{\prime}\right)$. A vector $V \in \Gamma(T M)$ is called null if $g(V, V)=0$. Any null vector is of the form $V=\lambda \otimes \pi$ where $\lambda$, and $\pi$ are sections of $\mathbb{S}$ and $\mathbb{S}^{\prime}$ respectively. An $\alpha$-plane (respectively a $\beta$-plane) is a two-dimensional plane in $T_{p} M$ spanned by null vectors of the above form with $\pi$ (respectively $\lambda$ ) fixed, and an $\alpha$-surface ( $\beta$-surface) is a two-dimensional surface in $\zeta \subset M$ such that its tangent plane at every point is an $\alpha$-plane ( $\beta$-plane). The seminal theorem of Penrose [37] states that a maximal, three dimensional, family of $\alpha$-surfaces exists in $M$ iff $C_{+}=0$.

\section*{3. From projective to bi-Lagrangian structures}

In this section we show how to canonically construct a bi-Lagrangian structure on the total space of a certain rank 2 affine bundle over a projective surface $(N,[\nabla])$. Recall that the group $H$ also acts faithfully on $\mathbb{R}_{2}$ by affine transformations defined by the rule
$$(b \rtimes a) \cdot \xi=\xi a^{-1} \operatorname{det} a^{-1}-b a^{-1}$$
for all $\xi \in \mathbb{R}_{2}$ and $b \rtimes a \in H$. Therefore, the bundle associated to $P_{[\nabla]}$ via this affine $H$-action is a rank-2 affine bundle $M \rightarrow N$. We will refer to $M$ as the canonical affine bundle of ( $N,[\nabla]$ ).

By definition, an element of $M$ is an equivalence class $[u, \xi]$ with $u \in P_{[\nabla]}$ and $\xi \in \mathbb{R}_{2}$ subject to the equivalence relation
$$\left(u_{1}, \xi_{1}\right) \sim\left(u_{2}, \xi_{2}\right) \quad \Longleftrightarrow \quad u_{2}=u_{1} \cdot b \rtimes a \wedge \xi_{2}=(b \rtimes a)^{-1} \cdot \xi_{1}, \quad b \rtimes a \in H .$$
Clearly, every element of $M$ has a representative $(u, 0)$, unique up to a $\operatorname{GL}(2, \mathbb{R})$ transformation, where here $\mathrm{GL}(2, \mathbb{R}) \subset H$ consists of those elements $b \rtimes a \in H$ satisfying $b=0$. For simplicity of notation, we will henceforth write $a$ instead of $0 \rtimes a$ for the elements of $\operatorname{GL}(2, \mathbb{R}) \subset H$. It follows that as a smooth manifold, $M$ is canonically diffeomorphic to the quotient $P_{[\text {∇] }} / \mathrm{GL}(2, \mathbb{R})$ and we let $\mu: P_{[\text {V] }} \rightarrow M$ denote the quotient projection.

Remark 3.1. It can be shown that the sections of $M \rightarrow N$ are in one-to-one correspondence with the [∇]-representative connections. The submanifold geometry in $M$ of representative connections is studied in depth in two articles by the second author [33, 34].

We use the standard fact that the tangent bundle of $N$ is the bundle associated to $P_{[\nabla]}$ via the natural $H$-action on $\mathfrak{s l}(3, \mathbb{R}) / \mathfrak{h}$ induced by the adjoint representation of $H$ on its Lie algebra $\mathfrak{h}$. An element in the Lie algebra $\mathfrak{s l}(3, \mathbb{R})$ of $\operatorname{SL}(3, \mathbb{R})$ can be written as
$$m_{x, \xi, \alpha}=\left(\begin{array}{cc}
-\operatorname{tr} \alpha & \xi \\
x & \alpha
\end{array}\right) \text {, }$$
where $x \in \mathbb{R}^{2}, \xi \in \mathbb{R}_{2}, \alpha \in \mathfrak{g} \mathfrak{l}(2, \mathbb{R})$ and $\mathfrak{h}$ consists of those elements for which $x=0$. Therefore, the elements in the quotient $\mathfrak{s l}(3, \mathbb{R}) / \mathfrak{h} \simeq \mathbb{R}^{2}$ are uniquely represented by matrices of the form $m_{x, 0,0}$. Hence the induced action of $H$ is
$$(b \rtimes a)\left(\begin{array}{ll}
0 & 0 \\
x & 0
\end{array}\right)(b \rtimes a)^{-1}=\left(\begin{array}{cc}
0 & 0 \\
(\operatorname{det} a) a x & 0
\end{array}\right) \quad \bmod \mathfrak{h} .$$

In particular, since the cotangent bundle of $N$ is the bundle associated to the representation $\chi: H \rightarrow$ $\mathrm{GL}\left(\mathbb{R}_{2}\right)$ which is dual to the representation defined by (3.2), it follows that $\chi$ is defined by the rule
$$\chi(b \rtimes a) \xi=\xi a^{-1} \operatorname{det} a^{-1},$$
for all $\xi \in \mathbb{R}_{2}$ and $b \rtimes a \in H$.
Since $\chi$ is precisely the linear part of the affine $H$-action (3.1), we see that the affine bundle $M \rightarrow N$ is modelled on the cotangent bundle of $N$.
3.1. A bundle embedding. It turns out that we can embed $P_{[\nabla]} \rightarrow M$ as subbundle of the coframe bundle $F \rightarrow M$ of $M$. Here, we define a coframe at $p \in M$ to be a linear isomorphism $T_{p} M \rightarrow \mathbb{R}_{2} \oplus \mathbb{R}^{2}$ and we denote the tautological $\mathbb{R}_{2} \oplus \mathbb{R}^{2}$-valued 1-form on $F$ by $\zeta$.

By definition of $M$, a vector field $X$ on $M$ is represented by a unique $\left(\mathbb{R}_{2} \oplus \mathbb{R}^{2}\right)$-valued function $\left(X_{+}, X_{-}\right)$on $P_{[\nabla]}$ satisfying the equivariance condition
$$R_{a}^{*} X_{+}=X_{+} a \operatorname{det} a, \quad R_{a}^{*} X_{-}=\left(\operatorname{det} a^{-1}\right) a^{-1} X_{-} .$$
Therefore, we obtain a unique map $\psi: P_{[\nabla]} \rightarrow F$ having the property that for every vector field $X$ on $M$ and for all $u \in P_{[\nabla]}$
$$\psi(u)(X(\mu(u)))=\left(X_{+}(u), X_{-}(u)\right),$$
where ( $X_{+}, X_{-}$) is the function on $P_{[\nabla]}$ representing $X$. Clearly, $\psi$ is a smooth embedding. Furthermore, from (3.3) we obtain
$$\psi(u \cdot a)=\psi(u) \cdot \chi(a)$$
where $\chi: H \ni \operatorname{GL}(2, \mathbb{R}) \rightarrow \operatorname{Aut}\left(\mathbb{R}_{2} \oplus \mathbb{R}^{2}\right)$ is the Lie group embedding defined by the rule
$$\chi(a)(\xi, x)=\left(\xi a \operatorname{det} a,\left(\operatorname{det} a^{-1}\right) a^{-1} x\right) .$$
Consequently, the pair $(\psi, \chi)$ embeds $P_{[\nabla]} \rightarrow M$ as a subbundle of the coframe bundle of $M$ whose structure group is isomorphic to $\operatorname{GL}(2, \mathbb{R})$. Furthermore, unraveling the definition of $\zeta$, it follows that we have
$$\psi^{*} \zeta=(\eta, \omega) .$$
The induced geometric structure on $M$ defined by the reduction of the coframe bundle of $M$ is a bi-Lagrangian structure, so we will study these structures next.
3.2. Bi-Lagrangian structures. A bi-Lagrangian structure on smooth 4-manifold $M$ (or more generally an even dimensional manifold) consists of a symplectic structure $\Omega$ together with a splitting of the tangent bundle of $M$ into a direct sum of $\Omega$-Lagrangian subbundles $E_{ \pm}$
$$T M=E_{+} \oplus E_{-} .$$
A manifold equipped with a bi-Lagrangian structure will be called a bi-Lagrangian manifold. The endomorphism $I: T M \rightarrow T M$ defined by
$$v=v_{+}+v_{-} \mapsto v_{+}-v_{-}, \quad v \in T M, v_{ \pm} \in E_{ \pm}$$
is $\Omega$-skew-symmetric, satisfies $I^{2}=\mathrm{Id}$ and its ±1-eigenbundle is $E_{ \pm}$. Clearly, $I$ is the unique endomorphism of the tangent bundle having these properties and therefore, we may equivalently think of a bi-Lagrangian structure as a pair $(\Omega, I)$ consisting of a symplectic structure $\Omega$ and a $\Omega$-skew-symmetric endomorphism $I: T M \rightarrow T M$ whose square is the identity.

Note also, that we may use the pair $(\Omega, I)$ to define a pseudo-Riemannian metric
$$g(v, w)=\Omega(v, I(w)), \quad v, w \in T M,$$
whose signature is $(2,2)$ and for which $I$ is skew-symmetric. Of course, a bi-Lagrangian structure is also equivalently described in terms of the pair $(g, I)$ or the pair $(g, \Omega)$.

Remark 3.2. What we call a bi-Lagrangian structure is also referred to as an almost para-Kähler structure and a para-Kähler structure provided $E_{ \pm}$are both Frobenius integrable. Note that in [4] the term bi-La-grangian structure is reserved for the case where both $E_{ \pm}$are Frobenius integrable.

Remark 3.3. We call a vector field defined on some open subset $U \subset(M, \Omega, I)$ bi-Lagrangian if its (local) flow preserves both $\Omega$ and $I$. The set of such vector fields on $V$ is a Lie subalgebra of the Lie algebra of vector fields on $V$ which we will denote by $\mathcal{B}_{(\Omega, I)}(U)$.

A bi-Lagrangian structure admits an interpretation as a reduction of the structure group of the coframe bundle of $M$. To this end consider the symmetric bilinear form of signature $(2,2)$ on $\mathbb{R}_{2} \oplus \mathbb{R}^{2}$
$$\left\langle\left(\xi_{1}, x^{1}\right),\left(\xi_{2}, x^{2}\right)\right\rangle=-\frac{1}{2}\left(\xi_{1} x^{2}+\xi_{2} x^{1}\right)$$
and the skew-symmetric non-degenerate bilinear form
$$>\left(\xi_{1}, x^{1}\right),\left(\xi_{2}, x^{2}\right)<=\frac{1}{2}\left(\xi_{1} x^{2}-\xi_{2} x^{1}\right) .$$
The two bilinear forms are related by the endomorphism $\iota$ sending $(\xi, x) \mapsto(\xi,-x)$. The endomorphism $\iota$ satisfies $l^{2}=\mathrm{Id}$ and its 1 -eigenspace is $\mathbb{R}_{2} \oplus\{0\}$ and its -1 -eigenspace is $\{0\} \oplus \mathbb{R}^{2}$. By construction, both eigenspaces are null and Lagrangian, that is, both bilinear forms vanish identically when restricted to the $t$-eigenspaces. The group $\operatorname{GL}(2, \mathbb{R})$ acts from the left on $\mathbb{R}_{2} \oplus \mathbb{R}^{2}$ by
$$a \cdot(\xi, x)=\left(\xi a^{-1}, a x\right)$$
and this action preserves both bilinear forms. We henceforth identify $\operatorname{GL}(2, \mathbb{R})$ with its image subgroup in $\operatorname{Aut}\left(\mathbb{R}_{2} \oplus \mathbb{R}^{2}\right)$. In fact, $\operatorname{GL}(2, \mathbb{R})$ is the largest subgroup of $\operatorname{Aut}\left(\mathbb{R}_{2} \oplus \mathbb{R}^{2}\right)$ preserving both bilinear forms.

Given a bi-Lagrangian structure $(\Omega, I)$ on $M$ we say that a coframe $u$ at $p \in M$ is adapted to $(\Omega, I)$ if for all $v, w \in T_{p} M$
$$\left.\Omega_{p}(v, w)=\right\rangle u(v), u(w)\langle\quad \text { and } \quad(u \circ I)(v)=(\iota \circ u)(v) .$$
The set of all coframes of $M$ adapted to $(\Omega, I)$ defines a reduction $\lambda: B_{(\Omega, I)} \rightarrow M$ of the coframe bundle $F \rightarrow M$ of $M$ with structure group $\operatorname{GL}(2, \mathbb{R})$. Conversely, every reduction of the coframe bundle of $M$ with structure group $\operatorname{GL}(2, \mathbb{R})$ defines a unique pair $(\Omega, I)$, consisting of a non-degenerate 2-form on $M$ and a $\Omega$-skew symmetric endomorphism $I: T M \rightarrow T M$ whose square is the identity. Note however that $\Omega$ need not be closed.

The tautological $\mathbb{R}_{2} \oplus \mathbb{R}^{2}$-valued 1-form $\zeta$ on $B_{(\Omega, I)}$ will be written as $\zeta=(\eta, \omega)$, so that $\eta=\left(\eta_{i}\right)$ is an $\mathbb{R}_{2}$-valued 1-form on $B_{(\Omega, I)}$ and $\omega=\left(\omega^{i}\right)$ is an $\mathbb{R}^{2}$-valued 1-form on $B_{(\Omega, I)}$. By construction, we have
$$\lambda^{*} \Omega=-\eta \wedge \omega:=-\eta_{i} \wedge \omega^{i} .$$
Furthermore, let $\hat{L}_{ \pm}=\left(\lambda^{\prime}\right)^{-1}\left(E_{ \pm}\right) \subset T B_{(\Omega, I)}$, then the subbundle $\hat{L}_{+}$is defined by the equations $\eta=0$ and the subbundle $\hat{L}_{-}$is defined by the equations $\omega=0$.

A linear connection on $F$ is said to be adapted to $(\Omega, I)$ if it pulls back to $B_{(\Omega, I)}$ to become a principal $\mathrm{GL}(2, \mathbb{R})$-connection on $B_{(\Omega, I)}$. An adapted connection is given by a $\mathfrak{g l}(2, \mathbb{R})$-valued equivariant 1-form $\nu$ on $B_{(\Omega, I)}$ such that
$$\begin{aligned}
d \eta & =-\eta \wedge \nu+\frac{1}{2} T_{+}((\eta, \omega) \wedge(\eta, \omega)), \\
d \omega & =-\nu \wedge \omega+\frac{1}{2} T_{-}((\eta, \omega) \wedge(\eta, \omega)),
\end{aligned}$$
for some torsion map $T_{+}$on $B_{(\Omega, I)}$ with values in $\operatorname{Hom}\left(\Lambda^{2}\left(\mathbb{R}_{2} \oplus \mathbb{R}^{2}\right), \mathbb{R}_{2}\right)$ and some torsion map $T_{-}$on $B_{(\Omega, I)}$ with values in $\operatorname{Hom}\left(\Lambda^{2}\left(\mathbb{R}_{2} \oplus \mathbb{R}^{2}\right), \mathbb{R}^{2}\right)$, both of which are equivariant with respect to the $\operatorname{GL}(2, \mathbb{R})$ right action. It is an easy exercise in linear algebra to check that for every bi-Lagrangian structure there exists a unique adapted connection $\nu$ so that
$$\begin{aligned}
& d \eta=-\eta \wedge \nu+\frac{1}{2} T_{+}(\omega \wedge \omega), \\
& d \omega=-\nu \wedge \omega+\frac{1}{2} T_{-}(\eta \wedge \eta),
\end{aligned}$$
with $T_{+}$taking values in $\operatorname{Hom}\left(\Lambda^{2} \mathbb{R}^{2}, \mathbb{R}_{2}\right)$ and $T_{-}$taking values in $\operatorname{Hom}\left(\Lambda^{2} \mathbb{R}_{2}, \mathbb{R}^{2}\right)$. It follows that $E_{ \pm}$is integrable if and only if $T_{ \pm}$vanishes identically. Furthermore, the identity $d(\eta \wedge \omega)=0$ implies
$$T_{+}(\omega \wedge \omega) \wedge \omega=0 \quad \text { and } \quad T_{-}(\eta \wedge \eta) \wedge \eta=0 .$$
The linear connection $\nu$ on the bundle of adapted frames induces connections on the tensor bundles of $M$ in the usual way. By construction, the induced connection ${ }^{v} \nabla$ on $T M$ is the unique (affine) connection with torsion $\tau$ satisfying
$${ }^{v} \nabla \Omega=0 \quad \text { and } \quad{ }^{v} \nabla I=0 \quad \text { and } \quad \tau\left(X_{+}, X_{-}\right)=0,$$
for all $X_{ \pm} \in \Gamma\left(E_{ \pm}\right)$. To the to best of our knowledge, the connection ${ }^{v} \nabla$ was first studied by Libermann [29], so we call $\nu$ the Libermann connection. Of course, if $\tau$ vanishes identically, then ${ }^{v} \nabla$ is just the Levi-Civita connection of $g$.
3.3. From projective to bi-Lagrangian structures. Denoting by $B_{(\Omega, I)}$ the bundle of adapted coframes of a bi-Lagrangian structure $(\Omega, I)$ and by $P_{[\nabla]}$ the Cartan bundle of a projective structure [∇], we obtain:

Theorem 3.4. Let $(N,[\nabla])$ be a projective surface with Cartan bundle $\left(\pi: P_{[\nabla]} \rightarrow N, \theta\right)$. Then there exists a bi-Lagrangian structure $(\Omega, I)$ on the quotient $M=P_{[\mathrm{V}]} / \operatorname{GL}(2, \mathbb{R})$ having the following property: There exists a $\operatorname{GL}(2, \mathbb{R})$-bundle isomorphism $\psi: P_{[\nabla]} \rightarrow B_{(\Omega, I)}$ so that
$$\psi^{*}\left(\begin{array}{cc}
-\frac{1}{3} \operatorname{tr} v & \eta \\
\omega & v-\frac{1}{3} \operatorname{Id} \operatorname{tr} v
\end{array}\right)=\theta,$$
where $(\eta, \omega)$ denotes the tautological 1-form on $B_{(\Omega, I)}$ and $\nu$ the Libermann connection. Moreover, the $E_{-}$-bundle of the bi-Lagrangian structure $(\Omega, I)$ is always Frobenius integrable and the $E_{+}$-bundle is Frobenius integrable if and only if [V] is flat.

Proof. We write
$$\theta=\left(\begin{array}{cc}
-\operatorname{tr} \phi & \hat{\eta} \\
\hat{\omega} & \phi
\end{array}\right)$$
for the Cartan connection on $P_{[\nabla]}$. From §3.1 we know that we have an embedding $(\psi, \chi)$ of $P_{[\nabla]} \rightarrow M$ as a GL(2, $\mathbb{R}$ )-subbundle $\lambda: B_{(\Omega, I)} \rightarrow M$ of the coframe bundle of $M$. Furthermore, $\psi$ satisfies
$$\psi^{*}(\eta, \omega)=(\hat{\eta}, \hat{\omega}),$$
where $(\eta, \omega)$ denotes the tautological $\left(\mathbb{R}_{2} \oplus \mathbb{R}^{2}\right)$-valued 1-form on $B_{(\Omega, I)}$. Therefore, we obtain a unique non-degenerate 2-form $\Omega$ on $M$ and a unique $\Omega$-skew-symmetric endomorphism $I: T M \rightarrow T M$ whose square is the identity. The 2-form $\Omega$ pulled back to $B_{(\Omega, I)}$ becomes $-\eta \wedge \omega$. The structure equations (2.5) imply that we have
$$\begin{aligned}
d \hat{\omega} & =-(\phi+\operatorname{Itr} \phi) \wedge \hat{\omega}, \\
d \hat{\eta} & =-\hat{\eta} \wedge(\phi+\operatorname{Itr} \phi)+L(\hat{\omega} \wedge \hat{\omega}) .
\end{aligned}$$
In particular, we obtain
$$\begin{aligned}
d(\hat{\eta} \wedge \hat{\omega}) & =[-\hat{\eta} \wedge(\phi+\operatorname{Itr} \phi)+L(\hat{\omega} \wedge \hat{\omega})] \wedge \hat{\omega}-\hat{\eta} \wedge[-(\phi+\operatorname{Itr} \phi) \wedge \hat{\omega}] \\
& =L(\hat{\omega} \wedge \hat{\omega}) \wedge \hat{\omega}=0,
\end{aligned}$$
where the last equality follows since $N$ is two-dimensional. This shows that $\Omega$ is symplectic, so that the pair $(\Omega, I)$ defines a bi-Lagrangian structure on $M$. The equivariance properties of $\theta$ and (3.6) imply that the $\psi$-pushforward of $\phi+\operatorname{Itr} \phi$ is a principal right $\operatorname{GL}(2, \mathbb{R})$-connection on $B_{(\Omega, I)}$ which satisfies (3.5) with $T_{-} \equiv 0$ and $T_{+}=L \circ \psi^{-1}$. In particular, $E_{-}$is always integrable and $E_{+}$is integrable if and only if $L$ vanishes identically, that is, [V] is flat. Denoting by $\nu$ the Libermann connection of $(\Omega, I)$, we obtain from its uniqueness that
$$\psi^{*} v=\phi+\operatorname{Itr} \phi,$$
which completes the proof. \(\square\)

Remark 3.5. Recall that if $X_{x}$ is a vector field on $P_{[\text {∇] }}$ having the property that
$$\omega\left(X_{x}\right)=x, \quad \eta\left(X_{x}\right)=0, \quad \phi\left(X_{x}\right)=0,$$
for some non-zero $x \in \mathbb{R}^{2}$, then the the integral curve of $X_{x}$, when projected to $N$, becomes a geodesic of [D]. Conversely every geodesic of [∇] arises in this way. Likewise, a geodesic of the Libermann connection arises as the projection of an integral curve of a horizontal vector field on $B_{(\Omega, I)}$ which is constant on the canonical 1-form. It follows that the geodesics on $(N,[\nabla])$ correspond to the geodesics of the Libermann connection on $(M, \Omega, I)$ that are everywhere tangent to $E_{-}$.
3.4. A local coordinate descripition. Recall from §2.3 that the choice of a representative connection $\nabla \in[\nabla]$ gives a $H$-bundle isomorphism $P_{[\nabla]} \simeq F \times \mathbb{R}_{2}$. In particular, we obtain a diffeomorphism $\psi_{\nabla}:\left(F \times \mathbb{R}_{2}\right) / \operatorname{GL}(2, \mathbb{R}) \rightarrow M$. By construction, the quotient $\left(F \times \mathbb{R}_{2}\right) / \operatorname{GL}(2, \mathbb{R})$ is the cotangent bundle of $N$. Denoting the projection $F \times \mathbb{R}_{2} \rightarrow T^{*} N$ by $\mu$ as well, we obtain
$$\begin{aligned}
& (\psi \circ \mu)^{*} g=-\left(-d \xi+\xi \varphi-\mathrm{P}^{t} \omega-\xi \omega \xi\right) \odot \omega, \\
& (\psi \circ \mu)^{*} \Omega=\omega \wedge\left(-d \xi+\xi \varphi-\mathrm{P}^{t} \omega-\xi \omega \xi\right),
\end{aligned}$$
where the $\mathbb{R}_{2} \otimes \mathbb{R}_{2}$-valued map $\mathrm{P}=\left(\mathrm{P}_{i j}\right)$ on $F$ represents the Schouten tensor of ∇ and $\varphi$ the connection form of $\nabla$. Using (3.8), we see that in terms of the Patterson-Walker metric $h_{\nabla}$ of ∇ and the Liouville 1 -form $\lambda$ of $T^{*} N$, the metric can be expressed as
$$g_{\nabla}:=\left(\psi_{\nabla}\right)^{*} g=h_{\nabla}+\lambda^{2}+v^{*} \operatorname{Ric}^{+}(\nabla)$$
and for the symplectic form we obtain
$$\Omega_{\nabla}:=\left(\psi_{\nabla}\right)^{*} \Omega=-\Omega_{0}+\frac{1}{3} v^{*} \operatorname{Ric}^{-}(\nabla) .$$
In canonical local coordinates ( $x^{i}, \xi_{i}$ ) on $T^{*} N$, we thus have the expressions
$$\begin{aligned}
g_{\nabla} & =\left(d \xi_{i} \odot d x^{i}-\left(\xi_{l} \Gamma_{i j}^{l}-\mathrm{P}_{(i j)}-\xi_{i} \xi_{j}\right) d x^{i} \odot d x^{j}\right) \\
\Omega_{\nabla} & =d \xi_{i} \wedge d x^{i}+\mathrm{P}_{[i j]} d x^{i} \wedge d x^{j}
\end{aligned}$$
where $\Gamma_{j k}^{i}$ denote the Christoffel symbols and $\mathrm{P}_{i j}$ the components of the Schouten tensor of ∇ with respect to the coordinates $x^{i}$.

Remark 3.6. Besides taking the quotient of the Cartan bundle by GL(2, $\mathbb{R}$ ), one might also consider the quotient by $\mathbb{R}^{2} \rtimes H$, where $H$ is the connected nonabelian real Lie group of dimension two. This quotient - which is a formal analogue to the construction of the conformal Fefferman metrics [22] - was studied in [31]. We also refer the reader to [24] for a generalisation of this construction to higher dimensions and its relation to the classical Patterson-Walker metrics [36].
3.5. Lift of projective vector fields. Denoting by $\rho: M \rightarrow N$ the basepoint projection, an immediate consequence of Theorem 3.4 is:

Corollary 3.7. For every open set $U \subset N$ the Lie algebra of projective vector fields $\mathcal{P}_{[\nabla]}(U)$ is isomorphic to the Lie algebra of bi-Lagrangian vector fields $\mathcal{B}_{(\Omega, I)}\left(\rho^{-1}(U)\right)$.

Proof. By standard results about Cartan geometries (c.f. [9]), the projective vector fields on $U \subset(N,[\nabla])$ are in one-to-one correspondence with the vector fields on $\pi^{-1}(U) \subset P_{[\nabla]}$ whose flow preserves the Car$\tan$ connection $\theta$ and which are equivariant for the principal right action. Theorem 3.4 implies that such a vector field corresponds to a vector field on $\psi\left(\pi^{-1}(U)\right) \subset B_{(\Omega, I)}$ preserving both the tautological form $(\eta, \omega)$ and the Libermann connection. Again, by standard results about $G$-structures [9], such vector fields are in one-to-one correspondence with vector fields on $\rho^{-1}(U)$ preserving both $\Omega$ and $I$. \(\square\)

Corollary 3.7 can be strengthened in the sense that we show that every Killing vector field for $(M, g)$ is also symplectic with respect to $\Omega$ and hence the lift of a projective vector field on $(N,[\nabla])$. As a warm up, we first consider a correspondence between affine vector fields and Killing vector fields for the asscoiated Patterson-Walker metric (2.10). Let ∇ be an affine connection on $N$. Recall that a vector field $K$ on $N$ is affine with respect to ∇ if and only if
$$0=\left(\mathcal{L}_{K} \nabla\right)_{i j}^{k} \equiv \frac{\partial^{2} K^{k}}{\partial x^{i} \partial x^{j}}+K^{m} \frac{\partial}{\partial x^{m}} \Gamma_{i j}^{k}-\Gamma_{i j}^{m} \frac{\partial K^{k}}{\partial x^{m}}+\Gamma_{i m}^{k} \frac{\partial K^{m}}{\partial x^{j}}+\Gamma_{j m}^{k} \frac{\partial K^{m}}{\partial x^{i}},$$
where we write $K=K^{i} \frac{\partial}{\partial x^{i}}$ in local coordinates $\left(x^{i}\right)$ on $U \subset N$ and where $\Gamma_{j k}^{i}$ denote the Christoffel symbols of ∇ with respect to $\left(x^{i}\right)$. Any vector field on $N$ corresponds to a linear function on $T^{*} N$, which in canonical local coordinates ( $x^{i}, \xi_{i}$ ) is given by $K^{i} \xi_{i}$. This function, together with the canonical symplectic structure on $T^{*} N$ gives rise to the Hamiltonian vector field
$$\widetilde{K}=K^{i} \frac{\partial}{\partial x^{i}}-\xi_{j} \frac{\partial K^{j}}{\partial x^{i}} \frac{\partial}{\partial \xi_{i}} .$$
This vector field is sometimes referred to as the complete lift [41].

Proposition 3.8. Let $K$ be an affine vector field for a connection ∇ on $U \subset N$. Then its complete lift (3.12) is a Killing vector field for the Patterson-Walker metric (2.10).

Proof. Consider the one-parameter group of transformations generated by the vector field (3.12)
$$x^{i} \longrightarrow x^{i}+\epsilon K^{i}+O\left(\epsilon^{2}\right), \quad \xi_{i} \longrightarrow \xi_{i}-\epsilon \xi_{j} \frac{\partial K^{j}}{\partial x^{i}}+O\left(\epsilon^{2}\right) .$$
This yields
$$\begin{aligned}
g \quad & \longrightarrow g+\epsilon\left\{\xi_{j} K^{i} d x^{j} d \xi_{i}-\xi_{i} K^{j} d x^{i} d \xi_{j}-\left(\xi_{j} \xi_{i} \xi_{k} K^{j}\right) d x^{i} d x^{k}\right. \\
& \left.-2 \Gamma_{i k}^{j} \xi_{j}\left(\xi_{m} K^{i}\right) d x^{k} d x^{m}+\Gamma_{i k}^{j} \xi_{m} \xi_{j} K^{m} d x^{i} d x^{k}-K^{m}\left(\xi_{m} \Gamma_{i k}^{j}\right) \xi_{j} d x^{i} d x^{k}\right\}+O\left(\epsilon^{2}\right) \\
& =g-\epsilon \xi_{k} \mathcal{L}_{K}\left(\Gamma_{i j}^{k}\right) d x^{i} \odot d x^{j}+O\left(\epsilon^{2}\right)
\end{aligned}$$
Therefore
$$\mathcal{L}_{\widetilde{K}} g=-\xi_{k} \mathcal{L}_{K}\left(\Gamma_{i j}^{k}\right) d x^{i} \odot d x^{j},$$
and the result follows. \(\square\)

Recall that a vector field $K$ is projective for ∇ if and only if $\left(\mathcal{L}_{K} \nabla\right)_{0}=0$, that is, there exists a 1-form $\rho$ on $N$ such that
$$\left(\mathcal{L}_{K} \nabla\right)_{i j}^{k}=\delta_{i}{ }^{k} \rho_{j}+\delta_{j}{ }^{k} \rho_{i} .$$

Proposition 3.9. Let $K$ be a projective vector field with $\rho_{i}=\nabla_{i} f$. Then
$$K-\xi_{j} \frac{\partial K^{j}}{\partial x^{i}} \frac{\partial}{\partial \xi_{i}}+f \xi_{i} \frac{\partial}{\partial \xi_{i}}$$
is a conformal Killing vector field for the Patterson-Walker metric (2.10).
Proof. The proof is similar to that of Proposition (3.8). The one-parameter group of transformation generated by (3.15) is
$$x^{i} \longrightarrow x^{i}+\epsilon K^{i}+O\left(\epsilon^{2}\right), \quad \xi_{i} \longrightarrow \xi_{i}-\epsilon \xi_{j} \frac{\partial K^{j}}{\partial x^{i}}-\epsilon f \xi_{i}+O\left(\epsilon^{2}\right),$$
which gives
$$g \longrightarrow g-\epsilon \xi_{k}\left(\mathcal{L}_{K} \nabla\right)_{i j}^{k} d x^{i} \odot d x^{j}-\xi_{k} d x^{k} \odot d f+\epsilon f g+O\left(\epsilon^{2}\right)$$
This does not change the conformal class iff $K$ satisfies (3.14) with $\rho=d f$. \(\square\)

Finally we give the main result of this Section, and establish a one-to-one correspondence between projective vector fields on $(N,[\nabla])$, and Killing vector fields on the Einstein lift on $M$.

Theorem 3.10. Let $K$ be a projective vector field on $(U,[\nabla])$, where $U \subset N$. Then
$$\mathcal{K}:=K-\xi_{j} \frac{\partial K^{j}}{\partial x^{i}} \frac{\partial}{\partial \xi_{i}}+\rho_{i} \frac{\partial}{\partial \xi_{i}}$$
is a Killing vector field for $g_{\nabla}$ which is symplectic with respect to the symplectic form $\Omega_{\nabla}$. Conversely, any Killing vector field for $g_{\nabla}$ is a lift (3.16) from $N$ of some projective vector field.

Proof. The integrability conditions for (3.14) are [42] (note however that that our sign conventions for the Schouten tensor differ from that in [42], so the sign of the RHS of (3.17) is opposite to what is given in [42])
$$\mathcal{L}_{K} \mathrm{P}_{i j}=-\nabla_{i} \rho_{j} .$$
We shall also write $\mathcal{K}=\tilde{K}+K_{\rho}$, where $\tilde{K}$ is the complete lift (3.12) and $K_{\rho}:=\rho_{i} \partial / \partial \xi_{i}$. Using (3.9) we compute
$$\begin{aligned}
\mathcal{L}_{\mathcal{K}} g_{\nabla}= & \mathcal{L}_{\widetilde{K}} h_{\nabla}+\mathcal{L}_{\widetilde{K}} \lambda \odot \lambda+\mathcal{L}_{K} \operatorname{Ric}^{+}(\nabla)+\mathcal{L}_{K_{\rho}} h_{\nabla}+\mathcal{L}_{K_{\rho}}(\lambda \odot \lambda) \\
= & -\xi_{k}\left(\mathcal{L}_{K} \nabla\right)_{i j}^{k} d x^{i} \odot d x^{j}+0-\left(\nabla_{i} \rho_{j}\right) d x^{i} \odot d x^{j}+d x^{i} \odot d \rho_{i} \\
& -\Gamma_{i j}^{k} \rho_{k} d x^{i} \odot d x^{j}+\left(\rho_{i} d x^{i}\right) \odot\left(\xi_{j} d x^{j}\right)=0,
\end{aligned}$$
where we have used (3.13), (3.14) and (3.17).
Now verify the symplectic condition
$$\begin{aligned}
\mathcal{L}_{\mathcal{K}} \Omega_{\nabla} & =\mathcal{L}_{\widetilde{K}}\left(d \xi_{i} \wedge d x^{i}\right)+\mathcal{L}_{K_{\rho}}\left(d \xi_{i} \wedge d x^{i}\right)+\mathcal{L}_{K}\left(\mathrm{P}_{i j} d x^{i} \wedge d x^{j}\right) \\
& =\left(d \rho_{i} \wedge d x^{i}-d \rho_{i} \wedge d x^{i}\right)=0
\end{aligned}$$
as the complete lift $\widetilde{K}$ is Hamiltonian with respect to $d \xi_{i} \wedge d x^{i}$, and we have used the skew part of the integrability conditions (3.17).

To prove the converse, consider a general vector field $\mathcal{K}=K^{i} \partial / \partial x^{i}+Q_{i} \partial / \partial \xi_{i}$ on $M$, and impose the Killing equations. The $d \xi_{i} \odot d \xi_{j}$ components of these equations imply that $K^{j}=K^{j}\left(x^{1}, x^{2}\right)$. The $d \xi_{i} \odot d x^{j}$ components yield the general form (3.16), where $\rho_{i}$ are some unspecified functions on $N$. Finally the $d x^{i} \odot d x^{j}$ components imply that the vector field $K^{i} \partial / \partial x^{i}$ on $N$ is projective. \(\square\)

\section*{4. Local characterization of the metric}

In the previous section we have shown that the metric $g$ constructed on the canonical affine bundle of a projective surface ( $N,[\nabla]$ ) is isometric to the metric
$$g_{\nabla}=h_{\nabla}+\lambda^{2}+v^{*} \operatorname{Ric}^{+}(\nabla)$$
on the cotangent bundle $v: T^{*} N \rightarrow N$ of $N$, where $\nabla \in[\nabla]$ is any representative connection. The metric (4.1) has previously appeard in [11] as a member of a one-parameter family $g_{\nabla, \Lambda}$ of split-signature metrics on $T^{*} N$ that one can associate to a torsion-free connection on $N$. The metrics take the form
$$g_{\nabla, \Lambda}=h_{\nabla}+\Lambda \lambda^{2}+\left(\frac{1}{\Lambda}\right) v^{*} \operatorname{Ric}^{+}(\nabla),$$
where $\Lambda$ is any non-zero real number. In particular, in [11] it is noted that the metrics $g_{\nabla, \Lambda}$ are anti-self-dual ${ }^{2}$ and Einstein with scalar curvature $24 \Lambda$, as can easily be verified by direct computation. Moreover, under the assumption that ∇ is non-flat, the metrics $g_{\nabla, \Lambda}$ are locally characterized as the neutral signature four-dimensional type II Osserman metrics whose Jacobi operator have non-zero eigenvalues. We refer the reader to [11, Thm. 7.3] for details. Here we provide another characterisation. Recall [3, 13, 43] that a distribution $\mathcal{D} \subset T M$ on a Riemannian manifold $(M, g)$ is called parallel if ${ }^{g} \nabla_{X} Y \in \Gamma(D)$ if $Y \in \Gamma(D)$, where ${ }^{g} \nabla$ is the Levi-Civita connection of $g$. Thus, if $\mathcal{D}$ is parallel, then it is necessarily Frobenius integrable as $[X, Y]={ }^{g} \nabla_{X} Y-{ }^{g} \nabla_{Y} X \in \Gamma(D)$ if $X, Y \in \Gamma(D)$.

\footnotetext{
${ }^{2}$ self-dual with respect to the orientation convention of [11].
}

Theorem 4.1. Let $(M, g)$ be an ASD Einstein manifold with scalar curvature 24 admitting a parallel ASD totally null distribution. Then $(M, g)$ is conformally flat, or it is locally isometric to $\left(T^{*} N, g_{\nabla}\right)$ for some torsion-free connection ∇ on $N$.

Proof. We shall rely on two isomorphisms: $T M=\mathbb{S} \otimes \mathbb{S}^{\prime}$, and $\Lambda^{2}{ }_{-}=\mathbb{S} \odot \mathbb{S}$. Let the ASD totally null distribution correspond to an ASD two-form $\Theta \in \Gamma\left(\Lambda_{-}^{2}\right)$, or equivalently to a section $\imath \in \Gamma(\mathbb{S})$. The Frobenius integrability conditions imply the local existence of two functions $\xi_{1}$ and $\xi_{2}$ on $M$ such that $\operatorname{Ker}(\Theta)=\operatorname{span}\left\{\partial / \partial \xi_{1}, \partial / \partial \xi_{2}\right\}$. We can rescale $\iota$ so that the corresponding two-form is closed, and proportional to $d x^{1} \wedge d x^{2}$ for some functions ( $x^{1}, x^{2}$ ) which are constant on each $\beta$-surface in the two parameter family. The functions $\left(\xi_{1}, \xi_{2}\right)$ are then the coordinates on the $\beta$-surface. The corresponding metric takes the form
$$g=d \xi_{i} \odot d x^{i}+\Theta_{i j}(x, \xi) d x^{i} \odot d x^{j}$$
for some symmetric two-by-two matrix $\Theta$. The anti-self-duality condition on the Weyl tensor forces the components of $\Theta$ to be at most cubic in $\left(\xi_{1}, \xi_{2}\right)$, with some additional algebraic relations between the components. Imposing the Einstein condition gives
$$\Theta_{i j}=\xi_{i} \xi_{j}+\mathrm{P}_{j i}-\Gamma_{i j}^{k} \xi_{k},$$
where the functions $\Gamma_{i j}^{k}$ do not depend on the coordinates $\xi_{1}, \xi_{2}$ and are otherwise arbitrary. Finally, the functions $\mathrm{P}_{i j}$ are determined by (2.8). Comparing with the coordinate expression (3.10) proves the claim. \(\square\)

Remark 4.2. If ∇ is a torsion-free connection on $N$ with skew-symmetric Ricci tensor, then (4.2) simplifies to become
$$g_{\nabla, \Lambda}=h_{\nabla}+\Lambda \lambda^{2} .$$
In particular, the limit $\Lambda \rightarrow 0$ is well-defined and hence the metric $g_{\nabla}$ can be deformed to a Ricci-flat anti-self-dual metric $g_{\nabla, 0}=h_{\nabla}$ which appeared in [14].

Remark 4.3. Note that if we correspondingly define a charged symplectic form ${ }^{3}$
$$\Omega_{\nabla, \Lambda}=d \lambda+\left(\frac{1}{3 \Lambda}\right) v^{*} \operatorname{Ric}^{-}(\nabla),$$
then the pair $\left(g_{\nabla, \Lambda}, \Omega_{\nabla, \Lambda}\right)$ defines a bi-Lagrangian structure on $T^{*} N$ for every $\Lambda \neq 0$. The symplectic form $\Omega_{\nabla, \Lambda}$ is ASD with respect to our choice of orientation and the metric (4.2). Moreover, denoting by ${ }^{g} \nabla$ the Levi-Civita connection of the metric $g_{\nabla, \Lambda}$, we obtain
$${ }^{g} \nabla \Omega_{\nabla, \Lambda}=4 L$$
where $L$ is the pull-back to $M$ of the Liouville curvature $\epsilon^{i j} \nabla_{i} \mathrm{P}_{j k} d x^{k} \otimes\left(d x^{1} \wedge d x^{2}\right)$ of [D], which vanishes if and only if ∇ is projectively flat.

\footnotetext{
${ }^{3}$ This terminology is motivated by the Hamiltonian description of a charged particle moving on a manifold, where the canonical symplectic structure on the cotangent bundle needs to be modified by a pull-back of a closed two-form (magnetic field) from the base manifold. In our case the two-form is the skew-symmetric part of the Schouten tensor, and the inverse of the Ricci scalar plays a role of electric charge. This magnetic term can always be set to zero by an appropriate choice of a connection in a projective class - here we find it convenient not to make any choices at this stage.
}

Remark 4.4. Straightforward calculations show that Theorem 3.10 carries over to the case ( $g_{\nabla, \Lambda}, \Omega_{\nabla, \Lambda}$ ) with respect to the lift
$$\mathcal{K}:=K-\xi_{j} \frac{\partial K^{j}}{\partial x^{i}} \frac{\partial}{\partial \xi_{i}}+\frac{1}{\Lambda} \rho_{i} \frac{\partial}{\partial \xi_{i}} .$$
Remark 4.5. The existence of a neutral metric $g$ with a two-plane distribution imposes topological restrictions on $M$. If $M$ is compact then [1, 25]
$$\chi[M] \equiv 0 \bmod 2, \quad \chi[M] \equiv \tau[M] \bmod 4,$$
where $\tau[M]$ and $\chi[M]$ are the signature and Euler characteristic respectively. C. LeBrun pointed out to the authors the following argument which shows that a stronger statement is true in the case where the two-plane distribution $\mathcal{D}$ is totally null with respect to $g .{ }^{4}$ We may assume that $D$ is the graph of an isomorphism $\mathcal{V} \rightarrow \mathcal{V}^{\prime}$, where $T M=\mathcal{V} \oplus \mathcal{V}^{\prime}$ is an orthogonal decomposition into time-like and spacelike sub-bundles with respect to some chosen background metric $h$ on $M$. After possibly passing to a double cover we can assume $\mathcal{V}$ and $\mathcal{V}^{\prime}$ to be orientable. Moreover, we may fix orientations so that the isomorphism $\mathcal{V} \rightarrow \mathcal{V}^{\prime}$ is orientation reversing, thus equipping $M$ with an orientation so that $D$ is antiself-dual. By rotating clockwise in $\mathcal{V}$ and $\mathcal{V}^{\prime}$ with respect to $h$, we obtain an almost complex structure on $M$ such that $\mathcal{V}$ becomes a complex line sub-bundle $L$, and so that $\mathcal{V}^{\prime}$ becomes its dual bundle $L^{*}$. Consequently, $M$ admits an almost complex structure $J$ such that the canonical bundle of $(M, J)$ is trivial. After possibly passing to a double cover it therefore follows that $M$ is oriented and spin and - assuming $M$ is compact - that
$$2 \chi[M]+3 \tau[M]=0 .$$
Note that fixing the orientation so that $\mathcal{D}$ is self-dual leads to a sign change in (4.3) as $\tau$ changes sign when reversing the orientation whereas $\chi$ does not. Also, note that the existence of $\mathcal{D}$ forces $M$ to be orientable hence (4.3) still holds true (assuming our choice of orientation) without passing to the cover as $\chi$ and $\tau$ are both doubled when passing to a double cover.

\section*{5. Gauge theory of Tractor Connection}

In this Section we shall present a gauge-theoretic construction of the metric (1.1). We shall introduce a projectively invariant equation on a connection, and a pair of Higgs fields on an auxilary vector bundle $E \rightarrow N$. In the special case when $E$ is a rank-3 cotractor bundle (see §5.2) and the gauge group is $S L(3, \mathbb{R})$, the horizontal lifts of the geodesic spray of ∇ and the Higgs field will give rise to an integrable $\alpha$-plane (twistor) distribution on $T M$, where $M=\mathbb{P}(E)$ with a projective line removed from each fiber.

Let $(N,[\nabla])$ be a projective structure on a surface, and let $E \rightarrow N$ be a vector bundle with $\mathfrak{g}$ -connection $A$, where $\mathfrak{g}$ is some Lie algebra. Let $\phi$ be a one-form on $N$, called the Higgs pair, with values in the Lie algebra $\mathfrak{g}$. In an open set $U \subset N$ we shall write $\phi=\phi_{i} d x^{i}$ and regard $\phi$ and $A$ as $\mathfrak{g}$ valued one-forms on $N$ transforming as
$$\begin{aligned}
A & \longrightarrow \gamma A \gamma^{-1}-d \gamma \gamma^{-1} \\
\phi & \longrightarrow \gamma \phi \gamma^{-1}
\end{aligned}$$
under the gauge transformations. Here $\gamma: N \rightarrow G$, and $G$ is the gauge group with the Lie algebra $\mathfrak{g}$.
For any chosen connection $\nabla \in[\nabla]$ in the projective class consider the system of equations
$$D_{(i} \phi_{j)}=0,$$

\footnotetext{
${ }^{4}$ Private communication, March 2016.
}
where
$$D_{i} \phi_{j}:=\partial_{i} \phi_{j}-\Gamma_{i j}^{k} \phi_{k}-\left[A_{i}, \phi_{j}\right] .$$
In [7, 8] these equations appear in a slightly different setup, when $A$ is a connection on a principal (rather than a vector) bundle. While our construction below is self-contained, and does not rely on the results of [7, 8], we shall nevertheless refer to (5.1) as the Calderbank equations.
5.1. The Calderbank equations. An equivalent way to formulate (5.1) is to say that the Higgs pair is constant along the charged geodesic spray on $T N$, i.e.
$$\Theta^{A}(\phi):=\left(\pi^{i} \frac{\partial}{\partial x^{i}}-\Gamma_{i j}^{k} \pi^{i} \pi^{j} \frac{\partial}{\partial \pi^{k}}\right)(\phi)-[A, \phi]=0,$$
where $\pi^{i}$ are coordinates on the fibres of $T N$, and $\phi=\phi_{i} \pi^{i}$ and $A=A_{i} \pi^{i}$ are $\mathfrak{g}$-valued linear functions on $T N$. The equations (5.1) do not depend on the choice of the connection ∇ in the projective class if the Higgs field $\phi$ has projective weight 2.

In §5.2 we shall show how the Calderbank equations with the gauge group $\operatorname{SL}(3, \mathbb{R})$ - regarded as a subgroup of the group of diffeomorphisms of $\mathbb{R P}^{2}$ - leads to the neutral signature anti-self-dual Einstein metric (3.10). We shall first list some other (implicit) occurrences of these equations for other gauge groups.
5.1.1. Null reductions of anti-self-dual Yang-Mills equations. If the projective structure is flat, then (5.1) is the symmetry reduction of the anti-self-dual Yang-Mills (ASDYM) equation on $\mathbb{R}^{2,2}$ by two null translations and such that the $(2,2)$ metric $g$ restricted to the two-dimensional space of orbits $N=\mathbb{R}^{2}$ is totally isotropic, and the bi-vector generated by the null translations is anti-self-dual.

To see it, consider a $\mathfrak{g}$-valued connection one-form $A$ on $\mathbb{R}^{2,2}$, and set $F=d A+A \wedge A$. In local coordinates adapted to $\mathbb{R}^{2,2}=T N$ with $x^{i}$ the coordinates on $N$, the null isometries are $\partial / \partial \xi_{i}$, and the metric is
$$g=d x^{1} d \xi_{1}+d x^{2} d \xi_{2} .$$
Choose an orientation on $\mathbb{R}^{2,2}$ such that the two-form $d x^{1} \wedge d x^{2}$ is ASD. Defining two Higgs fields $\left.\left.\phi_{1}=\partial / \partial \xi_{2}\right\lrcorner A, \phi_{2}=\partial / \partial \xi_{1}\right\lrcorner A$, the ASDYM equations $F=-* F$ yield [32]
$$D_{1} \phi_{1}=0, \quad D_{2} \phi_{2}=0, \quad D_{1} \phi_{2}+D_{2} \phi_{1}=0,$$
where $D=d+A_{1} d x^{1}+A_{2} d x^{2}$ is a covariant derivative on $N$ induced by $A$. In [40] these equations have been solved completely for the gauge group $\operatorname{SL}(2)$.
5.1.2. Prolongation of the Calderbank equations. Instead of regarding both the connection and the Higgs pair as unknowns, we shall assume that the connection is given and consider (5.3) as a system of PDEs for the Higgs pair. To determine all derivatives of the Higgs pair in (5.3) we prolong the system once, and define $\mu$ by the equation
$$D_{i} \phi_{j}=\frac{1}{2} \mu \epsilon_{i j},$$
where $\epsilon=d x^{1} \wedge d x^{2}$ is the parallel volume form of $\nabla \in[\nabla]$. Commuting the covariant derivatives now leads to a closed system and therefore a connection
$$D_{i}\binom{\phi_{j}}{\mu}=\binom{\frac{1}{2} \mu \epsilon_{i j}}{2\left[\phi_{i}, \mathcal{F}\right]},$$
where $\mathcal{F}=\left[D_{1}, D_{2}\right]$ is the $\mathfrak{g}$-valued curvature of the connection $A$. The system is now closed. Commuting the covariant derivatives on $\mu$ leads to an integrability condition
$$[\mathcal{F}, \mu]-2 D_{1}\left[\phi_{2}, \mathcal{F}\right]+2 D_{2}\left[\phi_{1}, \mathcal{F}\right]=0 .$$
5.1.3. Killing equations. If the connection $A$ is flat, and $\mathfrak{g}=\mathbb{R}$ then the Calderbank equations become the projectively invariant Killing equations.
5.1.4. Anti-self-dual conformal structures with null conformal Killing vectors. Let $\mathfrak{g}$ be a subalgebra of the infinite dimensional Lie algebra of vector fields $\mathfrak{d i f f}(\Sigma)$ on a surface $\Sigma$ consisting of those elements of $\mathfrak{d i f f}(\Sigma)$ which commute with a fixed vector field $K$ on $\Sigma$. Let $M \rightarrow N$ be a surface bundle over $N$, with two dimensional fibres $\Sigma$. In this case the Calderbank equations are solvable by quadrature and the two-dimensional distribution
$$\mathcal{D}=\left\{\Theta^{A}:=\pi^{i} \frac{\partial}{\partial x^{i}}-\Gamma_{i j}^{k} \pi^{i} \pi^{j} \frac{\partial}{\partial \pi^{k}}-A_{i}(x) \pi^{i}, \phi=\pi^{i} \phi_{i}\right\}$$
spanning an $\mathbb{R} \mathbb{P}^{1}$ worth of null self-dual surfaces ( $\alpha$-surfaces) through each point of $M$ is the twistor distribution for the most general ASD $(2,2)$ conformal structure which admits a null conformal Killing vector $K$ [18, 7, 35].
5.1.5. The Patterson-Walker Riemannian extension. The conformal structure resulting from the distribution (5.4) is a generalisation of the Patterson-Walker lift [44, 3]. To recover the Patterson-Walker metric
$$g=d \xi_{i} \odot d x^{i}-\Gamma_{i j}^{k} \xi_{k} d x^{i} \odot d x^{j}$$
take the gauge algebra $\mathfrak{g}=\mathfrak{g} \mathfrak{l}(2, \mathbb{R})$ which generates linear transformations of $\Sigma=\mathbb{R}^{2}$. If the coordinates on $\Sigma$ are $\left(\xi_{1}, \xi_{2}\right)$, the elements of $\mathfrak{g} \mathfrak{l}(2, \mathbb{R})$ are vector fields of the form $\mathbf{t}_{i}{ }^{j}=\xi_{i} \frac{\partial}{\partial \xi_{j}}$. Taking the connection $A$ and the Higgs field given by
$$A_{i}=-\Gamma_{i j}^{k} \xi_{k} \frac{\partial}{\partial \xi_{j}}, \quad \phi_{i}=\left(b^{k} \xi_{k}\right) \epsilon_{i j} \frac{\partial}{\partial \xi_{j}}$$
where $b^{k}$ is a non-zero constant leads to an integrable distribution (5.4), as then
$$\begin{aligned}
{\left[\boldsymbol{\Theta}^{A}, \phi\right] } & =\pi^{i} b^{j}\left(\Gamma_{j k}{ }^{k} \xi_{i}+\Gamma_{i j}{ }^{k} \xi_{k}\right) \epsilon_{l m} \pi^{l} \frac{\partial}{\partial \xi_{m}} \\
& =0(\bmod \phi) .
\end{aligned}$$
The resulting metric (2.10) on $M=T N$ is then uniquely determined by the condition that the integral two-surfaces of $\mathcal{D}$ in $T N \times \mathbb{R P}^{1}$ project down to self-dual totally null surfaces on $T N$. The generators of the gauge group satisfy $[\mathbf{v}, K]=\mathbf{v}$, where $K=\xi_{1} \partial / \partial \xi_{1}+\xi_{2} \partial / \partial \xi_{2}$ is a conformal null Killing vector of (2.10).

We shall end this subsection by clarifying the connection between projective changes of $\nabla \subset[\nabla]$, and conformal rescalings of the metric $g$ on $T^{*} N$. We shall restrict our discussion to special connections in [D] which preserve some volume. Consider the effect of transformation (2.2) with $\Upsilon_{i}=\nabla_{i} f$, together with rescaling the fibers of $T N \rightarrow N$
$$\xi_{i} \rightarrow \hat{\xi}_{i}=e^{2 f} \xi_{i}$$
on the Patterson-Walker lift ${ }^{5}$ (2.10). A straightforward calculation yields
$$\hat{g}=e^{2 f} g .$$
Thus conformal scales on $T N$ correspond to projective scales on $N$.
5.2. Tractor connection and ASD Einstein metrics. In this Section we shall consider the Calderbank equations, where the gauge group is $\operatorname{SL}(3, \mathbb{R})$, and $E$ is the standard cotractor bundle for the projective structure $[\nabla]$. Recall the Cartan bundle $P_{[\nabla]}$ from section (2.3). We may think of the left action of $H \subset \operatorname{SL}(3, \mathbb{R})$ on $\mathbb{R}_{3}$ by matrix multiplication as a (linear) $H$-representation and consequently, we obtain an associated rank-3 vector bundle $E$ for every projective surface $(N,[\nabla])$. The vector bundle $E$ is commonly referred to as the cotractor bundle of $(N,[\nabla])$. Interest in $E$ stems from the fact that it comes canonically equipped with an $\operatorname{SL}(3, \mathbb{R})$ connection which is flat if and only if $(N,[\nabla])$ is, see [2].

Let $\mathcal{E}(1)$ be the line bundle of projective densities of weight 1 . Consider a rank-three vector bundle $E=\mathcal{E}(1) \oplus\left(T^{*} N \otimes \mathcal{E}(1)\right)$ over $N$ with connection [2]
$$\mathcal{D}_{i}\binom{\sigma}{\mu_{j}}=\binom{\nabla_{i} \sigma-\mu_{i}}{\nabla_{i} \mu_{j}+\mathrm{P}_{i j} \sigma},$$
where $\mathrm{P}_{i j}$ is the (not necessarily symmetric) Schouten tensor of projective geometry. The splitting of the cotractor bundle depends on a choice of a connection ∇ in the projective class [V], and under (2.2) changes according to
$$\binom{\hat{\sigma}}{\hat{\mu}_{j}}=\binom{\sigma}{\mu_{j}+\Upsilon_{j} \sigma} .$$
Using the tractor indices $\alpha, \beta, \cdots=0,1,2$ we can rewrite the connection (5.7) in terms of its Christoffel symbols $\gamma_{i \alpha}^{\beta}$ as
$$\gamma_{i 0}^{0}=0, \quad \gamma_{i 0}^{j}=\delta_{i}^{j}, \quad \gamma_{i j}^{k}=\Gamma_{i j}^{k}, \quad \gamma_{i j}^{0}=-\mathrm{P}_{i j} .$$
The vector fields
$$\mathbf{t}_{\alpha}{ }^{\beta}=\psi_{\alpha} \frac{\partial}{\partial \psi_{\beta}}$$
generate the linear action of $\operatorname{GL}(3, \mathbb{R})$ on the fibres of $E$. These generators descend to eight vector fields (which we shall also denote $\mathbf{t}_{\alpha}{ }^{\beta}$ ) which generate the action of $\operatorname{SL}(3, \mathbb{R})$ on the fibres of the projective cotractor bundle $\mathbb{P}(E)$ which is a quotient of $E$ by the Euler vector field $\sum_{\alpha=0}^{2} \mathbf{t}_{\alpha}{ }^{\alpha}$. Setting $\xi_{i}=\psi_{i} / \psi_{0}$ yields
$$\mathbf{t}_{i}{ }^{j}=\xi_{i} \frac{\partial}{\partial \xi_{j}}, \quad \mathbf{t}_{i}{ }^{0}=-\xi_{i} \xi_{j} \frac{\partial}{\partial \xi_{j}}, \quad \mathbf{t}_{0}{ }^{i}=\frac{\partial}{\partial \xi_{i}}, \quad \mathbf{t}_{0}{ }^{0}=-\xi_{j} \frac{\partial}{\partial \xi_{j}} .$$
Consider the Calderbank equations with the gauge group $\operatorname{SL}(3, \mathbb{R}) \subset \operatorname{Diff}\left(\mathbb{R P}^{2}\right)$, where the connection is given by a vector-valued one-form
$$A=A_{i} d x^{i}=-\gamma_{i \beta}^{\alpha} d x^{i} \otimes \mathbf{t}_{\alpha}^{\beta}$$