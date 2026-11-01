# On the differential form spectrum of hyperbolic manifolds

- Category: papers
- Identity: arxiv:math/0303348
- Content status: fulltext_ok

---

---
source_file: math_0303348.pdf
converter: mathpix
format: mmd
---

\title{
ON THE DIFFERENTIAL FORM SPECTRUM OF HYPERBOLIC MANIFOLDS
}

\author{
GILLES CARRON AND EMMANUEL PEDON
}

\begin{abstract}
We give a lower bound for the bottom of the $L^{2}$ differential form spectrum on hyperbolic manifolds, generalizing thus a well-known result due to Sullivan and Corlette in the function case. Our method is based on the study of the resolvent associated with the Hodge-de Rham Laplacian and leads to applications for the (co)homology and topology of certain classes of hyperbolic manifolds.
\end{abstract}

\section*{1. Introduction}

Let $G / K$ be a Riemannian symmetric space of noncompact type, and let $\Gamma$ be a discrete, torsion-free subgroup of $G$. Thus $\Gamma \backslash G / K$ is a locally Riemannian symmetric space with nonpositive sectional curvature. Most of this article concerns the rank one case, i.e. when $G / K$ is one of the hyperbolic spaces $\mathbb{H}_{\mathbb{R}}^{n}, \mathbb{H}_{\mathbb{C}}^{n}, \mathbb{H}_{\mathbb{H}}^{n}$ or $\mathbb{H}_{\mathbb{C}}^{2}$. In that situation, the quotients $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ are usually called hyperbolic manifolds, and we normalize the Riemannian metric so that the corresponding pinched sectional curvature lies inside the interval [-4, -1].

We denote by $2 \rho$ the exponential rate of the volume growth in $\mathbb{H}_{\mathbb{K}}^{n}$ :
$$2 \rho=\lim _{R \rightarrow+\infty} \frac{\log \operatorname{vol} B(x, R)}{R},$$
and let $\delta(\Gamma)$ be the critical exponent of the Poincaré series associated with $\Gamma$, i.e.
$$\delta(\Gamma)=\inf \left\{s \in \mathbb{R} \text { such that } \sum_{\gamma \in \Gamma} e^{-s d(x, \gamma y)}<+\infty\right\},$$
where $(x, y)$ is any pair of points in $\mathbb{H}_{\mathbb{K}}^{n}$ and $d(x, \gamma y)$ is the geodesic distance from $x$ to $\gamma y$. It is well-known that $0 \leq \delta(\Gamma) \leq 2 \rho$.

For any (locally) symmetric space $X$ considered above, let $\lambda_{0}^{p}(X)$ be the bottom of the $L^{2}$ spectrum of the Hodge-de Rham Laplacian $\Delta_{p}$ acting on compactly supported smooth differential $p$-forms of $X$. In other words,
$$\lambda_{0}^{p}(X)=\inf _{u \in C_{0}^{\infty}\left(\wedge p T^{*} X\right)} \frac{\left(\Delta_{p} u \mid u\right)_{L^{2}}}{\|u\|_{L^{2}}^{2}} .$$

Let us recall the following beautiful result, due to D. Sullivan ([Sul2], Theorem 2.17) in the real case and to K. Corlette ([Cor], Theorem 4.2) in the remaining cases (see also [Els], [Pat] and [Col] in the case of $\mathbb{H}_{\mathbb{R}}^{2}$ ):

\footnotetext{
Date: September 15, 2004.
2000 Mathematics Subject Classification. Primary 53C35, 58J50; Secondary 22E40, 34L15, 57T15.
Key words and phrases. Hyperbolic spaces, hyperbolic manifolds, locally symmetric spaces, cohomology, Hodge-de Rham Laplacian, spectral theory.
}

Theorem A. (1) If $\delta(\Gamma) \leq \rho$, then $\lambda_{0}^{0}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=\rho^{2}$.
(2) If $\delta(\Gamma) \geq \rho$, then $\lambda_{0}^{0}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=\delta(\Gamma)(2 \rho-\delta(\Gamma))$.

The main goal of our paper is to extend this result to the case of differential forms, although we are aware that getting such a simple statement is hopeless. For instance, when $\Gamma$ is cocompact the zero eigenspace of the Hodge-de Rham Laplacian $\Delta_{p}$ acting on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is isomorphic to the $p$-th cohomology group of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$, and contains therefore some information on the topology of this manifold. Thus one does not expect to compute the bottom of the spectrum of $\Delta_{p}$ only in terms of the critical exponent, since we always have $\delta(\Gamma)=2 \rho$ in the cocompact case.

Nevertheless, we are able to give lower bounds for $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)$. In order to state our first result, we set $d=\operatorname{dim}_{\mathbb{R}}(\mathbb{K})$ and denote by $\alpha_{p}$ the bottom of the continuous $L^{2}$ spectrum of $\Delta_{p}$ on the hyperbolic space $\mathbb{H}_{\mathbb{K}}^{n}$.

Theorem B. (1) Assume that $p \neq \frac{d n}{2}$.
\begin{itemize}
\item[(a)] If $\delta(\Gamma) \leq \rho$, then $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq \alpha_{p}$.
\item[(b)] If $\rho \leq \delta(\Gamma) \leq \rho+\sqrt{\alpha_{p}}$, then $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq \alpha_{p}-(\delta(\Gamma)-\rho)^{2}$.
\end{itemize}
(2) Assume that $p=\frac{d n}{2}$.
\begin{itemize}
\item[(a)] If $\delta(\Gamma) \leq \rho$, then either $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=0$ or $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq \alpha_{p}$.
\item[(b)] If $\rho \leq \delta(\Gamma) \leq \rho+\sqrt{\alpha_{p}}$, then either $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=0$ or $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq$ $\alpha_{p}-(\delta(\Gamma)-\rho)^{2}$.
\end{itemize}
Moreover, if $\delta(\Gamma)<\rho+\sqrt{\alpha_{p}}$ the possible eigenvalue 0 is discrete and spectrally isolated.

When $\delta(\Gamma)>\rho+\sqrt{\alpha_{p}}$, assertions (b) are still valid, but yield a triviality since the spectrum must be non negative.
U. Bunke and M. Olbrich pointed out to us that, in the case of convex cocompact subgroups $\Gamma$, Theorem B could be obtained as a consequence of Theorem 4.7 in [BO1] or Theorem 1.8 in [BO2]. However, besides it works in any case, our proof follows a completely different path, relying on an estimate for the resolvent associated with $\Delta_{p}$ on $\mathbb{H}_{\mathbb{K}}^{n}$. In particular, we are also able to discuss the nature of the continuous spectrum of $\Delta_{p}$ on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ when $\delta(\Gamma)<\rho$ (see Proposition 4.2).

Considering the following large class of examples, we see that our estimates in Theorem B are sharp when $\delta(\Gamma) \leq \rho$.

Theorem C. If $\delta(\Gamma) \leq \rho$ and if the injectivity radius of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is not bounded (for instance if the limit set $\Lambda(\Gamma)$ of $\Gamma$ is not the whole sphere at infinity $\mathbb{S}^{d n-1}$ ), then
$$\operatorname{spec}\left(\Delta_{p}, \Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=\operatorname{spec}\left(\Delta_{p}, \mathbb{H}_{\mathbb{K}}^{n}\right)= \begin{cases}{\left[\alpha_{p},+\infty\right)} & \text { if } p \neq \frac{d n}{2} \\ \{0\} \cup\left[\alpha_{p},+\infty\right) & \text { if } p=\frac{d n}{2}\end{cases}$$

Since the exact value of $\alpha_{p}$ is known except in the case of $\mathbb{H}_{\mathbb{O}}^{2}$ (see Theorem 2.4), Theorem B provides an explicit vanishing result for the space of $L^{2}$ harmonic forms, from which we shall obtain several corollaries, most of them having a topological flavour. For instance, we give sufficient conditions for a hyperbolic manifold to have only one end (actually we also deal with general locally symmetric spaces whose isometry group satisfies Kazhdan's property). Denote as usual by $H_{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}, \mathbb{Z}\right)$ the $p$-th homology space of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ with coefficients in $\mathbb{Z}$.

Theorem D. Let $\Gamma$ be a discrete and torsion-free subgroup of the isometry group of a quaternionic hyperbolic space $\mathbb{H}_{\mathbb{H}}^{n}$ or of the octonionic hyperbolic plane $\mathbb{H}_{\mathbb{O}}^{2}$. If
all unbounded connected components of the complement of any compact subset of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ have infinite volume, then $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ has only one end, and
$$H_{d n-1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}, \mathbb{Z}\right)=\{0\} .$$
Theorem E. Let $\Gamma$ be a discrete and torsion-free subgroup of $S U(n, 1)$, with $n \geq$ 2. Assume that the limit set $\Lambda(\Gamma)$ is not the whole sphere at infinity $\mathbb{S}^{2 n-1}$, that $\delta(\Gamma)<2 n$, and that the injectivity radius of $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ has a positive lower bound. Then $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ has only one end, and
$$H_{2 n-1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}, \mathbb{Z}\right)=\{0\} .$$

The first of these two theorems extends a previous result of K. Corlette ([Cor], Theorem 7.1) in the convex cocompact setting. The second enables us to complement a rigidity result due to Y. Shalom ([Sha], Theorem 1.6; see also [BCG2]):

Theorem F. Assume that $\Gamma=A *_{C} B$ is a cocompact subgroup of $S U(n, 1)$ (with $n \geq 2)$ which is a free product of subgroups $A$ and $B$ over an amalgamated subgroup $C$. Then either $2 n-1 \leq \delta(C)<2 n$ and $\Lambda(C)=\mathbb{S}^{2 n-1}$, or $\delta(C)=2 n$.

Our article is organized as follows. Section 2 contains most of the notation and background material that will be used in this article, and especially a fairly detailed introduction to $L^{2}$ harmonic analysis on the differential form bundle over hyperbolic spaces, from the representation theory viewpoint, since this approach is the touchstone of our work. We also briefly comment on the generalization of Theorem A to general nonpositively curved locally symmetric spaces and quotients of Damek-Ricci spaces.

Section 3 is devoted to the analysis of the resolvent
$$R_{p}(s)=\left(\Delta_{p}-\alpha_{p}+s^{2}\right)^{-1}, \quad \text { for } \operatorname{Re} s>0,$$
associated with the Hodge-de Rham Laplacian on hyperbolic spaces. More precisely, we obtain a meromorphic continuation on a suitable ramified cover of $\mathbb{C}$, prove estimates at infinity, and discuss the possible location of the poles on the imaginary axis $\operatorname{Re} s=0$ of $\mathbb{C}$.

In Section 4 we prove the spectral results announced above (Theorems B C), and apply them to derive several vanishing results for the cohomology. We also verify that our results on the bottom of the spectrum are strictly better than the ones given by the Bochner-Weitzenböck formula and the Kato inequality.

Lastly, Section 5 contains the proof of all results dealing with the number of ends and the homology of locally symmetric spaces, in particular of Theorems D, E F

Numerous comments and references will be given throughout the text.
Acknowledgements. We are particularly grateful to M. Olbrich for his careful reading of this article and for the numerous comments he made on it. We would like also to thank G. Besson, G. Courtois and S. Gallot for communicating to us quite soon a result of [BCG2], as well as J.-Ph. Anker, U. Bunke, P.-Y. Gaillard, E. Ghys, L. Guillopé and F. Laudenbach for useful remarks and fruitful discussions.

\section*{2. Notations and background material}

In this section, we shall collect some notations, definitions and preliminary facts which will be used throughout the article. Although some of our results concern general locally symmetric spaces of noncompact type, our paper essentially deals
with (quotients of) hyperbolic spaces, and we prefer therefore to restrict the following comprehensive presentation to that case. Most of unreferred material can be found for instance in the classical books [Hel] and [Kna].
2.1. Hyperbolic spaces. For $n \geq 2$ and $\mathbb{K}=\mathbb{R}, \mathbb{C}, \mathbb{H}$ or for $n=2$ and $\mathbb{K}=\mathbb{O}$, let $\mathbb{H}_{\mathbb{K}}^{n}$ be the Riemannian hyperbolic space of dimension $n$ over $\mathbb{K}$. Recall that $\mathbb{H}_{\mathbb{K}}^{n}$ is realized as the noncompact symmetric space of rank one $G / K$, where $G$ is a connected noncompact semisimple real Lie group with finite centre (namely, the identity component of the group of isometries of $\mathbb{H}_{\mathbb{K}}^{n}$ ) and $K$ is a maximal compact subgroup of $G$ which consists of elements fixed by a Cartan involution $\theta$. More precisely,

\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline if & $\mathbb{K}=\mathbb{R}$ & then & $G=S O_{e}(n, 1)$ & and & $K=S O(n)$; \\
\hline if & $\mathbb{K}=\mathbb{C}$ & then & $G=S U(n, 1)$ & and & $K=S(U(n) \times U(1)) ;$ \\
\hline if & $\mathbb{K}=\mathbb{H}$ & then & $G=S p(n, 1)$ & and & $K=S p(n) \times S p(1) ;$ \\
\hline if & $\mathbb{K}=\mathbb{O}$ & then $n=2$ and & $G=F_{4(-20)}$ & and & $K=\operatorname{Spin}(9)$. \\
\hline
\end{tabular}
(Other pairs $(G, K)$ may be taken to give the same quotient $G / K$.)
Let us begin with some algebraic structure of the Lie groups involved. Let $\mathfrak{g}$ and $\mathfrak{k}$ be the Lie algebras of $G$ and $K$, respectively, and write
$$\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{p}$$
for the Cartan decomposition of $\mathfrak{g}$ (i.e. the decomposition of $\mathfrak{g}$ into eigenspaces for the eigenvalues +1, -1, respectively, of the Cartan involution $\theta$ ). Recall that the subspace $\mathfrak{p}$ is thus identified with the tangent space $T_{e K}(G / K) \simeq \mathbb{R}^{d n}$ of $\mathbb{H}_{\mathbb{K}}^{n}=G / K$ at the origin, where $d=\operatorname{dim}_{\mathbb{R}}(\mathbb{K})$.

Let $\mathfrak{a}$ be a maximal abelian subspace of $\mathfrak{p}(\mathfrak{a} \simeq \mathbb{R}$ since $\operatorname{rank}(G / K)=1)$, with corresponding analytic Lie subgroup $A=\exp (\mathfrak{a})$ of $G$. Let $R(\mathfrak{g}, \mathfrak{a})$ be the restricted root system of the pair $(\mathfrak{g}, \mathfrak{a})$, with positive subsystem $R^{+}(\mathfrak{g}, \mathfrak{a})$ corresponding to the positive Weyl chamber $\mathfrak{a}_{+} \simeq(0,+\infty)$ in $\mathfrak{a}$. It is standard that there exists a linear functional $\alpha \in \mathfrak{a}^{*}$ such that
$$\begin{aligned}
R(\mathfrak{g}, \mathfrak{a}) & = \begin{cases}\{ \pm \alpha\} & \text { if } \mathbb{K}=\mathbb{R}, \\
\{ \pm \alpha, \pm 2 \alpha\} & \text { if } \mathbb{K}=\mathbb{C}, \mathbb{H}, \mathbb{O},\end{cases} \\
\text { and } R^{+}(\mathfrak{g}, \mathfrak{a}) & = \begin{cases}\{\alpha\} & \text { if } \mathbb{K}=\mathbb{R}, \\
\{\alpha, 2 \alpha\} & \text { if } \mathbb{K}=\mathbb{C}, \mathbb{H}, \mathbb{O} .\end{cases}
\end{aligned}$$
As usual, we write $\mathfrak{n}$ for the direct sum of positive root subspaces, i.e.
$$\mathfrak{n}= \begin{cases}\mathfrak{g}_{\alpha} & \text { if } \mathbb{K}=\mathbb{R}, \\ \mathfrak{g}_{\alpha} \oplus \mathfrak{g}_{2 \alpha} & \text { if } \mathbb{K}=\mathbb{C}, \mathbb{H}, \mathbb{O},\end{cases}$$
so that $\mathfrak{g}=\mathfrak{k} \oplus \mathfrak{a} \oplus \mathfrak{n}$ is an Iwasawa decomposition for $\mathfrak{g}$. We let also $N=\exp (\mathfrak{n})$ and $\rho=\frac{1}{2}\left(m_{\alpha} \alpha+m_{2 \alpha} 2 \alpha\right)$, where $m_{\alpha}=\operatorname{dim}_{\mathbb{R}} \mathfrak{g}_{\alpha}=d(n-1)>0$ and $m_{2 \alpha}=\operatorname{dim}_{\mathbb{R}} \mathfrak{g}_{2 \alpha}=$ $d-1 \geq 0$. In the sequel, we shall use systematically the identification
$$\begin{aligned}
\mathfrak{a}_{\mathbb{C}}^{*} & \simeq \mathbb{C}, \\
\lambda \alpha & \mapsto \lambda .
\end{aligned}$$

In particular, we shall view $\rho$ as a real number, namely
$$\rho=\frac{d(n-1)}{2}+d-1= \begin{cases}\frac{n-1}{2} & \text { if } \mathbb{K}=\mathbb{R}, \\ n & \text { if } \mathbb{K}=\mathbb{C}, \\ 2 n+1 & \text { if } \mathbb{K}=\mathbb{H}, \\ 11 & \text { if } \mathbb{K}=\mathbb{O} \text { and } n=2 .\end{cases}$$
This number has also a well-known geometrical interpretation: if $h$ denotes the exponential rate of the volume growth in $\mathbb{H}_{\mathbb{K}}^{n}$, i.e. if
$$h=\lim _{R \rightarrow \infty} \frac{\log \operatorname{vol} B(x, R)}{R},$$
(this quantity does not depend on $x \in \mathbb{H}_{\mathbb{K}}^{n}$ ) then $h=2 \rho$.
Next, let $H_{0} \in \mathfrak{a}_{+}$be such that $\alpha\left(H_{0}\right)=1$. We define a symmetric bilinear form on $\mathfrak{g}$ by
$$\langle X, Y\rangle=\frac{1}{B\left(H_{0}, H_{0}\right)} B(X, Y)=\frac{1}{2\left(m_{\alpha}+4 m_{2 \alpha}\right)} B(X, Y),$$
where $B$ is the Killing form on $\mathfrak{g}$. Then $\langle\cdot, \cdot\rangle$ is positive definite on $\mathfrak{p}$, negative definite on $\mathfrak{k}$ and we have
$$\langle\mathfrak{p}, \mathfrak{k}\rangle=0 .$$
Among others, one reason for this normalization is that the scalar product on $\mathfrak{p} \simeq T_{e K}(G / K)$ defined by the restriction of $\langle\cdot, \cdot\rangle$ induces precisely the $G$-invariant Riemannian metric on $\mathbb{H}_{\mathbb{K}}^{n}=G / K$ which has pinched sectional curvature inside the interval [-4, -1] (and constant, equal to -1, in the real case).

For $t \in \mathbb{R}$, we set $a_{t}=\exp \left(t H_{0}\right)$, so that
$$A=\left\{a_{t}, t \in \mathbb{R}\right\} .$$
We have the classical Cartan decomposition $G=K A K$, which actually can be slightly refined as
$$G=K\left\{a_{t}, t \geq 0\right\} K .$$
When writing $g=k_{1} a_{t} k_{2}$ with $t \geq 0$ according to decomposition (2.9), we then have
$$t=\text { hyperbolic distance } d(g K, e K),$$
where $e K$ is the origin in $\mathbb{H}_{\mathbb{K}}^{n}=G / K$.
2.2. Differential forms. In order to explain the way we shall view a differential form on a hyperbolic space, let us proceed with some tools coming from representation theory of the groups $G$ and $K$. First, denote as usual by $M$ the centralizer of $A$ in $K$, with corresponding Lie algebra $\mathfrak{m}$, and let $P=M A N$ be the standard minimal parabolic subgroup of $G$. For $\sigma \in \widehat{M}$ and $\lambda \in \mathfrak{a}_{\mathbb{C}}^{*} \simeq \mathbb{C}$, the principal series representation $\pi_{\sigma, \lambda}$ of $G$ is the induced representation
$$\pi_{\sigma, \lambda}=\operatorname{Ind}_{P}^{G}\left(\sigma \otimes e^{i \lambda} \otimes \mathbf{1}\right)$$
with corresponding space
$$H_{\sigma, \tau}^{\infty}=\left\{f \in C^{\infty}\left(G, V_{\sigma}\right), f\left(x m a_{t} n\right)=e^{-(i \lambda+\rho) t} \sigma(m)^{-1} f(x), \forall x \in G, \forall m a_{t} n \in P\right\} .$$
This $G$-action is given by left translations: $\pi_{\sigma, \lambda}(g) f(x)=f\left(g^{-1} x\right)$. Moreover, if $H_{\sigma, \lambda}$ denotes the Hilbert completion of $H_{\sigma, \lambda}^{\infty}$ with respect to the norm $\|f\|=$
$\left\|\left.f\right|_{K}\right\|_{L^{2}(K)}$, then $\pi_{\sigma, \lambda}$ extends to a continuous representation of $G$ on $H_{\sigma, \lambda}$. When $\lambda \in \mathbb{R}$, the principal series representation $\pi_{\sigma, \lambda}$ is unitary, in which case it is also irreducible, except maybe for $\lambda=0$.

Next, let $\left(\tau, V_{\tau}\right)$ be a unitary finite dimensional representation of the group $K$ (not necessarily irreducible). It is standard ([Wal], §5.2) that the space of sections of the $G$-homogeneous vector bundle $E_{\tau}=G \times_{K} V_{\tau}$ can be identified with the space
$$\Gamma(G, \tau)=\left\{f: G \rightarrow V_{\tau}, f(x k)=\tau(k)^{-1} f(x), \forall x \in G, \forall k \in K\right\}$$
of functions of (right) type $\tau$ on $G$. We define also the subspaces
$$C^{\infty}(G, \tau)=\Gamma(G, \tau) \cap C^{\infty}\left(G, V_{\tau}\right), \quad \text { and } \quad L^{2}(G, \tau)=\Gamma(G, \tau) \cap L^{2}\left(G, V_{\tau}\right)$$
of $\Gamma(G, \tau)$ which correspond to $C^{\infty}$ and $L^{2}$ sections of $E_{\tau}$, respectively. Note that $L^{2}(G, \tau)$ is the Hilbert space associated with the unitary induced representation $\operatorname{Ind}_{K}^{G}(\tau)$ of $G$, the action being given by left translations.

For $0 \leq p \leq d n$, let $\tau_{p}$ denote the $p$-th exterior product of the complexified coadjoint representation $\mathrm{Ad}_{\mathbb{C}}^{*}$ of $K$ on $\mathfrak{p}_{\mathbb{C}}^{*}$. Then $\tau_{p}$ is a unitary representation of $K$ on $V_{\tau_{p}}=\wedge^{p} \mathfrak{p}_{\mathbb{C}}^{*}$ and the corresponding homogeneous bundle $E_{\tau_{p}}$ is the bundle of differential forms of degree $p$ on $G / K$.

In general, the representation $\tau_{p}$ is not $K$-irreducible and decomposes as a finite direct sum of $K$-types:
$$\tau_{p}=\bigoplus_{\tau \in \widehat{K}} m\left(\tau, \tau_{p}\right) \tau,$$
where $m\left(\tau, \tau_{p}\right) \geq 0$ is the multiplicity of $\tau$ in $\tau_{p}$ (as usual, $\widehat{K}$ stands for the unitary dual of the Lie group $K$ ). Let us set
$$\widehat{K}\left(\tau_{p}\right)=\left\{\tau \in \widehat{K}, m\left(\tau, \tau_{p}\right)>0\right\},$$
so that (2.11) induces the following decomposition:
$$L^{2}\left(G, \tau_{p}\right)=\bigoplus_{\tau \in \widehat{K}\left(\tau_{p}\right)}\left(L^{2}(G, \tau) \otimes \mathbb{C}^{m\left(\tau, \tau_{p}\right)}\right),$$
as well as its analogue when considering $C^{\infty}$ differential $p$-forms.
2.3. The continuous part of the Plancherel formula for $L^{2}\left(G, \tau_{p}\right)$. Let us consider an irreducible unitary representation $\tau \in \widehat{K}$. When restricted to the subgroup $M, \tau$ is generally no more irreducible, and splits into a finite direct sum
$$\left.\tau\right|_{M}=\bigoplus_{\sigma \in \widehat{M}} m(\sigma, \tau) \sigma,$$
where $m(\sigma, \tau) \geq 0$ is the multiplicity of $\sigma$ in $\left.\tau\right|_{M}$ and $\widehat{M}$ stands for the unitary dual of $M$. Let us define then
$$\widehat{M}(\tau)=\{\sigma \in \widehat{M}, m(\sigma, \tau)>0\} .$$

The Plancherel formula for the space $L^{2}(G, \tau)$ of $L^{2}$ sections of the homogeneous bundle $E_{\tau}=G \times_{K} V_{\tau}$ consists in the diagonalization of the corresponding unitary representation $\operatorname{Ind}_{K}^{G}(\tau)$ of $G$. First, we remark that
$$L^{2}(G, \tau) \simeq\left\{L^{2}(G) \otimes V_{\tau}\right\}^{K},$$
where the upper index $K$ means that we take the subspace of $K$-invariant vectors for the right action of $K$ on $L^{2}(G)$. According to Harish-Chandra's famous

Plancherel Theorem for $L^{2}(G)$, the space $L^{2}(G, \tau)$ splits then into the direct sum of a continuous part $L_{c}^{2}(G, \tau)$ and of a discrete part $L_{d}^{2}(G, \tau)$. The latter can be expressed in terms of discrete series representations of $G$, but giving such a precision would be useless for our purpose. The former takes the following form (see e.g. [Ped3], §3, for details):
$$L_{c}^{2}(G, \tau) \simeq \bigoplus_{\sigma \in \widehat{M}(\tau)} \int_{\mathfrak{a}_{+}^{*}}^{\oplus} d \lambda p_{\sigma}(\lambda) H_{\sigma, \lambda} \widehat{\otimes} \operatorname{Hom}_{K}\left(H_{\sigma, \lambda}, V_{\tau}\right)$$
In this formula, $d \lambda$ is the Lebesgue measure on $\mathfrak{a}_{+}^{*} \simeq(0,+\infty), p_{\sigma}(\lambda)$ is the Plancherel density associated with $\sigma$ and $\operatorname{Hom}_{K}\left(H_{\sigma, \lambda}, V_{\tau}\right)$ is the vector space of $K$-intertwining operators from $H_{\sigma, \lambda}$ to $V_{\tau}$, on which $G$ acts trivially. This space is non zero (since $\sigma \in \widehat{M}(\tau))$ but finite dimensional (since every irreducible unitary representation of $G$ is admissible).

By combining formulas (2.12) and (2.13) we get the following result.
Proposition 2.1. The continuous part of the Plancherel formula for $L^{2}\left(G, \tau_{p}\right)$ is given by:
$$L_{c}^{2}\left(G, \tau_{p}\right) \simeq \bigoplus_{\tau \in \widehat{K}\left(\tau_{p}\right)}\left(\bigoplus_{\sigma \in \widehat{M}(\tau)} \int_{\mathfrak{a}_{+}^{*}}^{\oplus} d \lambda p_{\sigma}(\lambda) H_{\sigma, \lambda} \widehat{\otimes} \operatorname{Hom}_{K}\left(H_{\sigma, \lambda}, V_{\tau}\right)\right) \otimes \mathbb{C}^{m\left(\tau, \tau_{p}\right)} .$$
2.4. The spectrum of the Hodge-de Rham Laplacian. The Hodge-de Rham Laplacian $\Delta_{p}=d d^{*}+d^{*} d$ acts on $C^{\infty}$ differential $p$-forms on $\mathbb{H}_{\mathbb{K}}^{n}=G / K$, i.e. on members of the space $C^{\infty}\left(G, \tau_{p}\right)$. Actually, this operator is realized by the action of the Casimir element $\Omega_{\mathfrak{g}}$ of the universal enveloping algebra $U(\mathfrak{g})$ of $\mathfrak{g}$. More precisely, keeping notation (2.7), let $\left\{Z_{i}\right\}$ be any basis for $\mathfrak{g}$ and $\left\{Z^{i}\right\}$ the corresponding basis of $\mathfrak{g}$ such that $\left\langle Z_{i}, Z^{j}\right\rangle=\delta_{i j}$. The Casimir operator can be written as
$$\Omega_{\mathfrak{g}}=\sum_{i} Z_{i} Z^{j} .$$
We can view $\Omega_{\mathfrak{g}}$ as a $G$-invariant differential operator acting on $C^{\infty}\left(G, \tau_{p}\right)$, and have then the well-known identification (Kuga's formula, see [BW], Theorem II.2.5)
$$\Delta_{p}=-\Omega_{\mathfrak{g}} .$$

We shall denote also by $\Delta_{p}$ the unique self-adjoint extension of the Hodgede Rham operator from compactly supported smooth differential forms to $L^{2}$ differential forms on $\mathbb{H}_{\mathbb{K}}^{n}=G / K$. Let us recall that the nature of its spectrum is well known:

Theorem 2.2. (1) If $p \neq \frac{d n}{2}$, the $L^{2}$ spectrum of $\Delta_{p}$ is absolutely continuous, of the form $\left[\alpha_{p},+\infty\right)$ with $\alpha_{p} \geq 0$.
\begin{itemize}
\item[(2)] If $p=\frac{d n}{2}$ (with dn even), one must add the sole discrete eigenvalue 0 , which occurs with infinite multiplicity.
\item[(3)] We have $\alpha_{p}=0$ if and only if $\mathbb{K}=\mathbb{R}$ and $p=\frac{n \pm 1}{2}$. In particular, the discrete eigenvalue 0 occuring in middle dimension $p=\frac{d n}{2}$ is always spectrally isolated.
\end{itemize}

In this result, assertion (1) is essentially Proposition 2.1 assertion (2) is true for any general $G / K$ and can be found e.g. in Bor, [Ped1] or [Olb1], and assertion
(3) follows from results in [BW] and [VZ], as noticed by J. Lott in Lot, § VII.B (see also our Theorem 2.4).

Moreover, the exact value of $\alpha_{p}$ can be calculated with the help of some more representation theory. Let us elaborate. Thanks to (2.15), in order to investigate the continuous $L^{2}$ spectrum of $\Delta_{p}$ and thus to compute $\alpha_{p}$, it is enough to consider the action of the Casimir operator $\Omega_{\mathfrak{g}}$ on the right-hand side of the Plancherel formula given in Proposition 2.1 and, specifically, on each elementary component $H_{\sigma, \lambda} \widehat{\otimes} \operatorname{Hom}_{K}\left(H_{\sigma, \lambda}, V_{\tau}\right)$.

The action of $\Omega_{\mathfrak{g}}$ on $\operatorname{Hom}_{K}\left(H_{\sigma, \lambda}, V_{\tau}\right)$ being trivial, the problem reduces to study its effect on $H_{\sigma, \lambda}$, and even on $H_{\sigma, \lambda}^{\infty}$, by density. But since $\Omega_{\mathfrak{g}}$ is a central element in the enveloping algebra of $\mathfrak{g}$, it acts on the irreducible admissible representation $H_{\sigma, \lambda}^{\infty}$ by a scalar $\omega_{\sigma, \lambda}$. More precisely, let $\mu_{\sigma}$ be the highest weight of $\sigma \in \widehat{M}$ and $\delta_{\mathfrak{m}}$ be the half sum of the positive roots of $\mathfrak{m}_{\mathbb{C}}$ with respect to a given Cartan subalgebra. Then $\sigma\left(\Omega_{\mathfrak{m}}\right)=-c(\sigma) \mathrm{Id}$, where the Casimir value of $\sigma$ is given by
$$c(\sigma)=\left\langle\mu_{\sigma}, \mu_{\sigma}+2 \delta_{\mathfrak{m}}\right\rangle \geq 0 .$$
Using for instance [Kna], Proposition 8.22 and Lemma 12.28, one easily checks that
$$\Omega_{\mathfrak{g}}=\omega_{\sigma, \lambda} \operatorname{Id} \text { on } H_{\sigma, \lambda}^{\infty},$$
where
$$\omega_{\sigma, \lambda}=-\left(\lambda^{2}+\rho^{2}-c(\sigma)\right) .$$
Thus (2.17), (2.15) and Proposition 2.1 show that the action of $\Delta_{p}$ on (smooth vectors of) $L^{2}\left(G, \tau_{p}\right)$ is diagonal, a fact which allows us to calculate the continuous $L^{2}$ spectrum of $\Delta_{p}$.

In order to state this, set
$$\widehat{M}\left(\tau_{p}\right)=\bigcup_{\tau \in \widehat{K}\left(\tau_{p}\right)} \widehat{M}(\tau),$$
and denote by $\sigma_{\text {max }}$ one of the (possibly many) elements of $\widehat{M}\left(\tau_{p}\right)$ such that $c\left(\sigma_{\text {max }}\right) \geq c(\sigma)$ for any $\sigma \in \widehat{M}\left(\tau_{p}\right)$. Our discussion implies immediately the following result.
Proposition 2.3. The continuous $L^{2}$ spectrum of the Hodge-de Rham Laplacian $\Delta_{p}$ is $\left[\alpha_{p},+\infty\right)$, where
$$\alpha_{p}=\rho^{2}-c\left(\sigma_{\max }\right) .$$

With a case-by-case calculation, the previous formula gives the explicit value of $\alpha_{p}$ (at least in theory; in the case $\mathbb{K}=\mathbb{H}$, identifying the representations $\sigma_{\text {max }}$ is quite awkward, see [Ped4]). For instance, $\alpha_{0}$ equals $\rho^{2}$ for any $\mathbb{H}_{\mathbb{K}}^{n}$, since $\sigma_{\text {max }}$ must be the trivial representation (this well-known fact can be proved also by other arguments). For general $p$, we collect the known results in the following theorem. Observe that we can restrict to $p \leq d n / 2$, since $\alpha_{d n-p}=\alpha_{p}$ by Hodge duality.
Theorem 2.4. Let $p \leq \frac{d n}{2}$.
\begin{itemize}
\item[(1)] If $\mathbb{K}=\mathbb{R}$ (see Don, Ped2), then $\alpha_{p}=\left(\frac{n-1}{2}-p\right)^{2}$.
\item[(2)] If $\mathbb{K}=\mathbb{C}$ (see [Ped3]), then
$$\alpha_{p}= \begin{cases}(n-p)^{2} & \text { if } p \neq n, \\ 1 & \text { if } p=n .\end{cases}$$
\end{itemize}
(3) If $\mathbb{K}=\mathbb{H}$ (see Ped4), then
$$\alpha_{p}= \begin{cases}(2 n+1)^{2} & \text { if } p=0, \\ (2 n-p)^{2}+8(n-p) & \text { if } 1 \leq p \leq\left[\frac{4 n-1}{6}\right], \\ (2 n+1-p)^{2} & \text { if }\left[\frac{4 n-1}{6}\right]+1 \leq p \leq n, \\ (2 n-p)^{2} & \text { if } n+1 \leq p \leq 2 n-1, \\ 1 & \text { if } p=2 n .\end{cases}$$

To our knowledge, the value of $\alpha_{p}$ in the exceptional case $\mathbb{H}_{\mathbb{O}}^{2}$ is still unknown.

\subsection*{2.5. The action of the Hodge-de Rham Laplacian on $\tau_{p}$-radial functions.}

For any finite dimension representation $\tau$ of $K$, let us introduce the space of smooth $\tau$-radial functions on $G$ :
$$\begin{aligned}
C^{\infty}(G, \tau, \tau) & =\left\{F \in C^{\infty}\left(G, \text { End } V_{\tau}\right)\right. \\
& \left.F\left(k_{1} g k_{2}\right)=\tau_{p}\left(k_{2}\right)^{-1} F(g) \tau_{p}\left(k_{1}\right)^{-1}, \forall g \in G, \forall k_{1}, k_{2} \in K\right\} .
\end{aligned}$$

Our aim is to calculate the action of the Laplacian $\Delta_{p}$ on $C^{\infty}\left(G, \tau_{p}, \tau_{p}\right)$ (the reason will be given in next subsection). Because of the Cartan decomposition (2.9), it is clear that any $\tau$-radial function on $G$ is entirely determined by its restriction to the semigroup $\left\{a_{t}, t \geq 0\right\}$. Hence it is sufficient to calculate the value of $\Delta_{p} F\left(a_{t}\right)$ for any $F \in C^{\infty}\left(G, \tau_{p}, \tau_{p}\right)$ and any $t \geq 0$.

Because of (2.14) we have
$$\Omega_{\mathfrak{g}}=\Omega_{\mathfrak{p}}-\Omega_{\mathfrak{k}}=\sum_{i} X_{i}^{2}-\sum_{i} Y_{i}^{2}$$
if we choose bases $\left\{X_{i}\right\}$ of $\mathfrak{p}$ and $\left\{Y_{i}\right\}$ of $\mathfrak{k}$ which satisfy respectively $\left\langle X_{i}, X_{j}\right\rangle=\delta_{i j}$ and $\left\langle Y_{i}, Y_{j}\right\rangle=-\delta_{i j}$. On the spaces $C^{\infty}\left(G, \tau_{p}\right)$ and $C^{\infty}\left(G, \tau_{p}, \tau_{p}\right)$, we thus get
$$\Delta_{p}=-\Omega_{\mathfrak{g}}=-\Omega_{\mathfrak{p}}+\tau_{p}\left(\Omega_{\mathfrak{k}}\right),$$
where $\tau_{p}\left(\Omega_{\mathfrak{k}}\right)$ is a zero order differential operator which is diagonal, since $\tau\left(\Omega_{\mathfrak{k}}\right)$ is scalar for each $\tau \in \widehat{K}$, namely
$$\tau\left(\Omega_{\mathfrak{k}}\right)=-c(\tau) \mathrm{Id}=-\left(\mu_{\tau} \mid \mu_{\tau}+2 \delta_{\mathfrak{k}}\right) \mathrm{Id},$$
with notations that are analogous to the ones used in (2.16). Notice that (2.20) is exactly the well-known Bochner-Weitzenböck formula (see (4.3)), since $-\Omega_{\mathfrak{p}}$ coincides with the Bochner Laplacian $\nabla^{*} \nabla$ (see e.g. [BOS], Proposition 3.1).

Now, reminding (2.4) and (2.8), let $\mathfrak{l}_{1}$ and $\mathfrak{l}_{2}$ be the orthogonal projections of the root subspaces $\mathfrak{g}_{\alpha}$ and $\mathfrak{g}_{2 \alpha}$ on $\mathfrak{k}$ with respect to the Cartan decomposition (2.1), so that we have the orthogonal splitting
$$\mathfrak{k}=\mathfrak{m} \oplus \mathfrak{l}_{1} \oplus \mathfrak{l}_{2} .$$
(Remark that $\mathfrak{l}_{2}$ reduces to zero if $\mathbb{K}=\mathbb{R}$.) Let $\left\{Y_{1, r}\right\}_{r=1}^{d(n-1)}$ and $\left\{Y_{2, s}\right\}_{s=1}^{d-1}$ denote the subsystems of the basis $\left\{Y_{i}\right\}$ of $\mathfrak{k}$ which are bases for $\mathfrak{l}_{1}$ and $\mathfrak{l}_{2}$, respectively.

We have then the following result.
Proposition 2.5. If $F \in C^{\infty}\left(G, \tau_{p}, \tau_{p}\right)$, then for any $t \geq 0$ we have
$$\Delta_{p} F\left(a_{t}\right)=-\Omega_{\mathfrak{p}} F\left(a_{t}\right)+\tau_{p}\left(\Omega_{\mathfrak{k}}\right) F\left(a_{t}\right),$$
where
$$\begin{aligned}
& \Omega_{\mathfrak{p}} F\left(a_{t}\right)=\frac{d^{2}}{d t^{2}} F\left(a_{t}\right)+[d(n-1) \operatorname{coth} t+2(d-1) \operatorname{coth} 2 t] \frac{d}{d t} F\left(a_{t}\right) \\
& +(\operatorname{coth} t)^{2} \sum_{r=1}^{d(n-1)} \tau_{p}\left(Y_{1, r}^{2}\right) F\left(a_{t}\right)+(\sinh t)^{-2} F\left(a_{t}\right) \sum_{r=1}^{d(n-1)} \tau_{p}\left(Y_{1, r}^{2}\right) \\
& -2(\sinh t)^{-1}(\operatorname{coth} t) \sum_{r=1}^{d(n-1)} \tau_{p}\left(Y_{1, r}\right) F\left(a_{t}\right) \tau_{p}\left(Y_{1, r}\right) \\
& +(\operatorname{coth} 2 t)^{2} \sum_{s=1}^{d-1} \tau_{p}\left(Y_{2, s}^{2}\right) F\left(a_{t}\right)+(\sinh 2 t)^{-2} F\left(a_{t}\right) \sum_{s=1}^{d-1} \tau_{p}\left(Y_{2, s}^{2}\right) \\
& -2(\sinh 2 t)^{-1}(\operatorname{coth} 2 t) \sum_{s=1}^{d-1} \tau_{p}\left(Y_{2, s}\right) F\left(a_{t}\right) \tau_{p}\left(Y_{2, s}\right)
\end{aligned}$$
Proof. It remains only to show formula (2.22), whose proof is standard and can be found e.g. in Wal, §8.12.6. \(\square\)
2.6. The resolvent of the Hodge-de Rham Laplacian and the associated Green kernel. It is well-known that all kernels $K(x, y)$ of functions of the (positive) Laplace-Beltrami operator $\Delta_{0}$ on a symmetric space $G / K$ only depend on the Riemannian distance: $K(x, y)=k(d(x, y))$. In other words, because of (2.10) and the $G$-invariance of the distance, they can be considered as radial (i.e. bi- $K$ -invariant) functions on $G$. In the case of our bundle of differential forms, kernels of operators related to the Hodge-de Rham Laplacian $\Delta_{p}$ will naturally be $\tau_{p}$-radial functions on $G$ (see e.g. [CM]). In particular, for $s \in \mathbb{C}$ with Re $s>0$, consider the Green kernel $G_{p}(s, \cdot)$ of the resolvent
$$R_{p}(s)=\left(\Delta_{p}-\alpha_{p}+s^{2}\right)^{-1} .$$
By definition, it solves the differential equation
$$\left(\Delta_{p}-\alpha_{p}+s^{2}\right) G_{p}(s, \cdot)=\delta_{e} .$$
Therefore, when $\operatorname{Re} s>0$ the Green kernel $G_{p}(s, \cdot)$ is a Schwartz $\tau_{p}$-radial function on $G^{0}=G \backslash\{e\}$, i.e. a member of the space
$$\begin{aligned}
\mathcal{S}\left(G^{0}, \tau_{p}, \tau_{p}\right)=\{F \in & C^{\infty}\left(G^{0}, \tau_{p}, \tau_{p}\right): \forall D_{1}, D_{2} \in U(\mathfrak{g}), \forall N \in \mathbb{N}, \\
& \left.\sup _{t>0}\left\|F\left(D_{1}: a_{t}: D_{2}\right)\right\|_{\text {End } V_{\tau_{p}}}(1+t)^{N} e^{\rho t}<+\infty\right\},
\end{aligned}$$
where we use the classical Harish-Chandra notation $F\left(D_{1}: a_{t}: D_{2}\right)$ for the two sided derivation of $F$ at $a_{t}$ with respect to the elements $D_{1}$ and $D_{2}$ of the universal enveloping algebra $U(\mathfrak{g})$.

For convenience, we shall often use the alternative notation
$$g_{p}(s, t)=G_{p}\left(s, a_{t}\right),$$
defined for $\operatorname{Re} s>0$ and $t \geq 0$ (with a singularity at $t=0$ ).
2.7. Hyperbolic manifolds. Throughout this paper, $\Gamma$ will denote any torsionfree discrete subgroup of $G$, so that the quotient $\Gamma \backslash G / K$ is a hyperbolic manifold, i.e. a complete Riemannian locally symmetric space with strictly negative curvature. We define $\delta(\Gamma)$ to be the critical exponent of the Poincaré series associated with $\Gamma$, i.e. the nonnegative number
$$\delta(\Gamma)=\inf \left\{s \in \mathbb{R} \text { such that } \sum_{\gamma \in \Gamma} e^{-s d(x, \gamma y)}<+\infty\right\},$$
where $(x, y)$ is any pair of points in $\mathbb{H}_{\mathbb{K}}^{n}$ (for instance, $x=y=e K$ ) and $d$ is the hyperbolic distance. It is easy to check that
$$0 \leq \delta(\Gamma) \leq 2 \rho=h,$$
and it is also known that equality holds if $\Gamma$ has finite covolume (actually the converse is true when $\mathbb{K}=\mathbb{H}$ or $\mathbb{O}$, see [Cor], Theorem 4.4). This critical exponent has been extensively studied. For instance, one of the most striking results says that when $\Gamma$ is geometrically finite, then $\delta(\Gamma)$ is the Hausdorff dimension of the limit set $\Lambda(\Gamma) \subset S^{\infty}$, where the sphere at infinity $S^{\infty}=\partial \mathbb{H}_{\mathbb{K}}^{n} \simeq K / M \simeq \mathbb{S}^{d n-1}$ is endowed with its natural Carnot structure (see the works of S. Patterson, D. Sullivan, C. Yue ([Pat], [Sul1], [Yue]). Regarding the limit set $\Lambda(\Gamma)$, let us recall that it is defined as the set of accumulation points of any $\Gamma$-orbit in the natural compactification $\mathbb{H}_{\mathbb{K}}^{n} \cup S^{\infty}$.

In some cases, we also consider more general locally symmetric spaces $\Gamma \backslash G / K$ of the noncompact type (i.e. with nonpositive sectional curvature, of any rank). All definitions and results described above extend to that situation (except the relationship between $\delta(\Gamma)$ and $\Lambda(\Gamma)$, which is still being investigated, see [Alb], Qui1, Qui2).

Finally, if $X$ stands for any complete Riemannian manifold, we let $\lambda_{0}^{p}(X)$ be the bottom of the $L^{2}$ spectrum of $\Delta_{p}$ on $X$. In other words,
$$\lambda_{0}^{p}(X)=\inf _{u \in C_{0}^{\infty}\left(\wedge^{p} T^{*} X\right)} \frac{\left(\Delta_{p} u \mid u\right)_{L^{2}}}{\|u\|_{L^{2}}^{2}} .$$
With notation of Theorem 2.2 we thus have $\lambda_{0}^{p}\left(\mathbb{H}_{\mathbb{K}}^{n}\right)=\alpha_{p}$ when $p \neq \frac{d n}{2}$. Note also that, when $p=0$, this definition reduces to
$$\lambda_{0}^{0}(X)=\inf _{u \in C_{0}^{\infty}(X)} \frac{\|d u\|_{L^{2}}^{2}}{\|u\|_{L^{2}}^{2}} .$$
2.8. Some remarks about the generalization of Theorem A to other Riemannian manifolds. Hyperbolic spaces admit natural generalizations. Namely, they can be viewed both as a particular class of symmetric spaces of noncompact type and as a particular class of harmonic AN groups (also called Damek-Ricci spaces). The latter are Einstein manifolds which are not symmetric (except for the hyperbolic spaces) but their analysis is quite similar to the one of hyperbolic spaces (see [ADY]).

For these two families of manifolds, the proof of Theorem A can be adapted to get information on the bottom of the spectrum of the Laplacian $\Delta_{0}$ defined on some quotient by a discrete torsion-free subgroup $\Gamma$. Indeed, in both cases one has at his disposal the key ingredient, that is, estimates for the Green kernel (see Theorem 4.2.2 in [AJ] and Theorem 5.9 in [ADY], respectively).

In the case of Damek-Ricci spaces $A N$, the result reads exactly as in Theorem A provided we replace $2 \rho$ by the homogeneous dimension of $N$ (in both cases, these numbers represent the exponential rate $h$ of the volume growth).

As concerns locally symmetric spaces $\Gamma \backslash G / K$, the statement is not as sharp as in Theorem A since it provides in general only bounds for $\lambda_{0}^{0}(\Gamma \backslash G / K)$. Let us elaborate.

Take the Lie groups $G$ and $K$ as in Section 2.1 except that $G / K$ can be now of any rank $\ell \geq 1$, which means that $\mathfrak{a} \simeq \mathbb{R}^{\ell}$. Let us introduce some more notation. First, we have an inner product on all $\mathfrak{g}$ by modifying the symmetric bilinear form (2.7) as follows:
$$\langle X, Y\rangle=-B(X, \theta Y) \quad \forall X, Y \in \mathfrak{g},$$
and we denote by $\|\cdot\|$ the corresponding norm. The restriction of (2.25) to $\mathfrak{p}$ induces a $G$-invariant Riemannian metric on $G / K$ of (non strictly if $\ell>1$ ) negative curvature.

For any element $x \in G$, define $H(x)$ to be the unique element in the closure $\overline{\mathfrak{a}_{+}}$ of the positive Weyl chamber in $\mathfrak{a}$ so that
$$x=k_{1} \exp H(x) k_{2}$$
reflects the Cartan decomposition of $x$ (the analogue of (2.9)). The half-sum $\rho \in \mathfrak{a}^{*}$ of positive roots of the pair $(\mathfrak{g}, \mathfrak{a})$ cannot be considered as a real number anymore. Nevertheless, we can still view it as a member of $\mathfrak{a}$ via (2.25), and it should be noted that
$$\lambda_{0}^{0}(G / K)=\|\rho\|^{2}, \quad h=2\|\rho\|,$$
as well as
$$0 \leq \delta(\Gamma) \leq 2\|\rho\| .$$

Using Theorem 4.2.2 in [AJ], E. Leuzinger has obtained the following result (see [Leu]).

Theorem 2.6. Let $G / K$ be any noncompact Riemannian symmetric space, let $\Gamma$ be a discrete torsion-free subgroup of $G$, and set $\rho_{\text {min }}=\inf _{H \in \overline{\mathfrak{a}_{+}}}\langle\rho, H\rangle /\|H\|$ (so that $\rho_{\min } \leq\|\rho\|$, with equality in the rank one case).
\begin{itemize}
\item[(1)] If $\delta(\Gamma) \leq \rho_{\text {min }}$, then $\lambda_{0}^{0}(\Gamma \backslash G / K)=\|\rho\|^{2}$.
\item[(2)] If $\delta(\Gamma) \in\left[\rho_{\text {min }},\|\rho\|\right]$, then
$$\|\rho\|^{2}-\left(\delta(\Gamma)-\rho_{\min }\right)^{2} \leq \lambda_{0}^{0}(\Gamma \backslash G / K) \leq\|\rho\|^{2} .$$
\item[(3)] If $\delta(\Gamma) \geq\|\rho\|$, then
$$\max \left\{\|\rho\|^{2}-\left(\delta(\Gamma)-\rho_{\min }\right)^{2}, 0\right\} \leq \lambda_{0}^{0}(\Gamma \backslash G / K) \leq \delta(\Gamma)(2\|\rho\|-\delta(\Gamma)) .$$
\end{itemize}

Actually, we have a better expression in terms of a modified critical exponent. The proof is underlying in Leu.

Theorem 2.7. Let $G / K$ be any noncompact Riemannian symmetric space, and let $\Gamma$ be a discrete torsion-free subgroup of $G$. Define $\tilde{\delta}(\Gamma)$ to be the critical exponent of the Poincaré series
$$\sum_{\gamma \in \Gamma} e^{-s d(x, \gamma y)-\rho(H(\gamma))} .$$
(This definition does not depend on the points $x, y \in G / K$.) Then
$$\lambda_{0}^{0}(\Gamma \backslash G / K)=\|\rho\|^{2}-\tilde{\delta}(\Gamma)^{2} .$$

In addition to this statement, one other reason to introduce our modified critical exponent is motivated by the following observation. Suppose that $\Gamma$ is Zariski dense in $G$. In Qui2, J.-F. Quint defines a function $\Phi_{\Gamma}: \overline{\mathfrak{a}_{+}} \rightarrow \mathbb{R} \cup\{-\infty\}$ which measures the growth of $\Gamma$ in the direction of $H \in \overline{\mathfrak{a}_{+}}$, and he shows that this function is concave. According to Corollary 5.5 in Qui2, we have a link between the growth indicator $\Phi_{\Gamma}$ and our modified critical exponent $\tilde{\delta}(\Gamma)$, namely:
$$\tilde{\delta}(\Gamma)=\inf _{\substack{H \in \bar{a}_{+} \\\|H\|=1}}\left(\langle\rho, H\rangle+\Phi_{\Gamma}(H)\right) .$$

\section*{3. The resolvent associated with the Hodge-de Rham Laplacian on hyperbolic spaces}

In our investigation of the bottom of the differential $p$-form spectrum on a hyperbolic manifold $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$, the key step consists in the careful analysis of the resolvent $R_{p}(s)=\left(\Delta_{p}-\alpha_{p}+s^{2}\right)^{-1}$ associated with the covering space $\mathbb{H}_{\mathbb{K}}^{n}$, and this goes through an estimate of the corresponding Green kernel $G_{p}(s, \cdot)$.

As a matter of fact, these estimates will partly be obtained by comparing $G_{p}(s, \cdot)$ to the scalar Green kernel $G_{0}(s, \cdot)$. We thus begin with the following result, whose proof is standard but will be recalled here, since we need to emphasize some of its ingredients. We retain notation from previous sections and particularly from Section 2.6

Proposition 3.1. For any $(\Gamma x, \Gamma y) \in\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \times\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)$ and any $s \in \mathbb{C}$ with Re $s>0$, let
$$g_{0}^{*}(s, \Gamma x, \Gamma y)=\sum_{\gamma \in \Gamma} g_{0}(s, d(x, \gamma y))$$
be the pull-back of the Green kernel from $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ to $\mathbb{H}_{\mathbb{K}}^{n}$. Then, for any $s>0$, $g_{0}^{*}(s, \Gamma x, \Gamma y)$ behaves as the Poincaré series
$$\sum_{\gamma \in \Gamma} e^{-(s+\rho) d(x, \gamma y)} .$$
Proof. We first observe that the Green kernel $g_{0}(s, \cdot)$ defined by (2.24) (and corresponding to the resolvent $R_{0}(s)=\left(\Delta_{0}-\rho^{2}+s^{2}\right)^{-1}$ ) can be explicitly expressed as a hypergeometric function (see for instance [Far], [MW], [ADY]). Indeed, by (2.23) and Proposition 2.5, it must solve the Jacobi type differential equation
$$g_{0}^{\prime \prime}(s, r)+[(d n-1) \operatorname{coth} r+(d-1) \tanh r] g_{0}^{\prime}(s, r)+\left(\rho^{2}-s^{2}\right) g_{0}(s, r)=0,$$
where differentiation is meant with respect to the second variable $r$. Letting
$$u\left(s,-(\sinh r)^{2}\right)=g_{0}(s, r),$$
we see that the function $u$ solves the hypergeometric equation
$$x(1-x) u^{\prime \prime}(s, x)+\left(\frac{d n}{2}-\frac{d(n+1)}{2} x\right) u^{\prime}(s, x)-\frac{\rho^{2}-s^{2}}{4} u(s, x)=0 .$$
Since the resolvent $R_{0}(s)$ acts continuously on $L^{2}\left(\mathbb{H}_{\mathbb{K}}^{n}\right)$ and since we must have the following standard behaviour:
$$g_{0}(s, r) \underset{r \rightarrow 0}{\simeq} \begin{cases}\frac{r^{2-d n}}{\operatorname{vol}\left(\mathbb{S}^{d n-1}\right)} & \text { if } d n>2, \\ -\frac{1}{2 \pi} \log r & \text { if } d n=2,\end{cases}$$
by using theorem 2.3.2 in [AAR] we find that
$$u(s, x)=f_{n, d}(s)(2 x)^{-(s+\rho) / 2}{ }_{2} F_{1}\left(\frac{s+\rho}{2}, \frac{s+1}{2}-\frac{d(n-1)}{4}, s+1, x^{-1}\right),$$
where ${ }_{2} F_{1}$ is the classical Gauss hypergeometric function and
$$f_{n, d}(s)=2^{d-2} \pi^{-(d n-1) / 2} \frac{\Gamma\left(\frac{s+\rho}{2}\right) \Gamma\left(s+\frac{d(n-1)}{2}\right)}{\Gamma(s+1) \Gamma\left(\frac{s}{2}+\frac{d(n-1)}{4}\right)} .$$
¿From these explicit formulas, we deduce important facts. Firstly, the resolvent
$$R_{0}(s): C_{0}^{\infty}\left(\mathbb{H}_{\mathbb{K}}^{n}\right) \longrightarrow C^{\infty}\left(\mathbb{H}_{\mathbb{K}}^{n}\right),$$
which is a priori defined for $\operatorname{Re} s>0$, has a meromorphic extension to the complex plane and has a holomorphic extension to the half-plane $\operatorname{Re} s>-\frac{d(n-1)}{2}$.

Secondly, we can estimate the function $g_{0}(s, r)$ for large values of $r$ (see also [LR]). On the one hand, for every $s \in \mathbb{C}$ such that $\operatorname{Re} s>-\frac{d(n-1)}{2}$, there is a positive constant $c_{1}(s)$ such that
$$\forall r \geq 1, \quad\left|g_{0}(s, r)\right| \leq c_{1}(s) e^{-(\operatorname{Re} s+\rho) r} .$$
On the other hand, when $s$ is a positive real number, $g_{0}$ is a positive real function and it can be bounded from below: there exists a positive constant $c_{2}(s)$ such that
$$\forall r \geq 1, \quad c_{2}(s) e^{-(s+\rho) r} \leq g_{0}(s, r) .$$
The result immediately follows. \(\square\)

Assume that $\delta(\Gamma)<\rho$. As was noticed by Y. Colin de Verdière in [Col], the estimate (3.2) implies also that the resolvent of the Laplacian $\Delta_{0}$ on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ has a holomorphic continuation to the half-plane
$$\left\{s \in \mathbb{C}: \operatorname{Re} s>\min \left(-\frac{d(n-1)}{2}, \delta(\Gamma)-\rho\right)\right\} .$$
According to a well known principle of spectral theory ([RS], Theorem XIII.20), we thus get:

Corollary 3.2. If $\delta(\Gamma)<\rho$, the $L^{2}$ spectrum of the Laplacian $\Delta_{0}$ on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is absolutely continuous.

Now we turn to the general case of differential forms. Reminding notation from Section 2.4 we define $\Sigma$ to be the (minimal) branched cover of $\mathbb{C}$ such that the functions $s \mapsto \sqrt{s^{2}-c(\sigma)+c\left(\sigma_{\text {max }}\right)}$ are holomorphic on $\Sigma$ for all $\sigma \in \widehat{M}\left(\tau_{p}\right)$. This cover is realized as follows: let $\sigma_{1}, \ldots, \sigma_{r}$ denote the distinguished representatives of the $\sigma$ 's in $\widehat{M}\left(\tau_{p}\right)$ such that $c(\sigma) \neq c\left(\sigma_{\text {max }}\right)$. Then
$$\Sigma=\left\{\hat{s}=\left(s, y_{1}, \ldots, y_{r}\right) \in \mathbb{C}^{r+1}: y_{i}^{2}=s^{2}+c\left(\sigma_{\max }\right)-c\left(\sigma_{i}\right), \forall i=1, \ldots r\right\} .$$
$\Sigma$ contains naturally a copy of the half-plane
$$\mathbb{C}_{+}=\{s \in \mathbb{C}, \operatorname{Re} s>0\},$$
namely
$$\mathbb{C}_{+} \equiv\left\{\hat{s}=\left(s, y_{1}, \ldots, y_{r}\right) \in \Sigma: \operatorname{Re} s>0, \operatorname{Re} y_{i}>0, \forall i=1, \ldots r\right\},$$
and we let $\overline{\mathbb{C}_{+}}$stands for its closure in $\Sigma$. Also, we shall still denote by $s$ : $\Sigma \rightarrow \mathbb{C}$ the holomorphic extension of the function $s$ from $\mathbb{C}_{+}$to $\Sigma$. Finally, if $\hat{s}=\left(s, y_{1}, \cdots, y_{r}\right) \in \Sigma$ we set
$$h(\hat{s})=\min \left\{\operatorname{Re} s, \operatorname{Re} y_{1}, \ldots, \operatorname{Re} y_{r}\right\},$$
and we recall that we have put $G^{0}=G \backslash\{e\}$.
Proposition 3.3. There exists a function $F_{p}(\hat{s}, x)$ defined on $\Sigma \times G^{0}$ such that:
\begin{itemize}
\item[(1)] the map $x \mapsto F_{p}(\hat{s}, x)$ belongs to $C^{\infty}\left(G^{0}, \tau_{p}, \tau_{p}\right)$;
\item[(2)] $\hat{s} \mapsto F_{p}(\hat{s}, x)$ is meromorphic on $\Sigma$ and holomorphic on $\Sigma \backslash \mathcal{N}$, where $\mathcal{N}$ is a discrete subset of $\Sigma \backslash \overline{\mathbb{C}_{+}}$;
\item[(3)] $\left(\Delta_{p}-\alpha_{p}+s^{2}\right) F_{p}(\hat{s}, \cdot)=0$;
\item[(4)] for any $\hat{s} \in \Sigma \backslash \mathcal{N}$, there is a constant $A(\hat{s})>0$ such that
$$\forall t>1,\left\|F_{p}\left(\hat{s}, a_{t}\right)\right\|_{\text {End } V_{\tau_{p}}} \leq A(\hat{s}) e^{-(\rho+h(\hat{s})) t} ;$$
\item[(5)] for any $s \in \mathbb{C}_{+}$, there is a constant $A(s)>0$ such that
$$\forall t>1,\left\|F_{p}\left(s, a_{t}\right)\right\|_{\text {End } V_{\tau_{p}}} \leq A(s) e^{-(\rho+\operatorname{Re} s) t} .$$
\end{itemize}
Proof. For $s \in \mathbb{C}_{+}$and $t>0$, define
$$v_{p}(s, t)=(\sinh t)^{d(n-1) / 2}(\sinh 2 t)^{(d-1) / 2} G_{p}\left(s, a_{t}\right) .$$
Using (2.23), Proposition 2.5 and the standard behaviour of hyperbolic functions, we see that $v_{p}$ must solve the differential equation
$$\left(-\frac{d^{2}}{d t^{2}}+\rho^{2}-\alpha_{p}+s^{2}+D+W\left(e^{-t}\right)\right) v_{p}(s, t)=0$$
on $\mathbb{R}_{+}^{*}$, where $W:\{z \in \mathbb{C},|z|<1\} \rightarrow \operatorname{End} V_{\tau_{p}}$ is a holomorphic function vanishing at 0:
$$W(z)=\sum_{l=1}^{\infty} w_{l} z^{l}, \quad \text { with } w_{l} \in \operatorname{End} V_{\tau_{p}},$$
and
$$\begin{aligned}
D & =-\sum_{r=1}^{d(n-1)} \tau_{p}\left(Y_{1, r}^{2}\right)-\sum_{s=1}^{d-1} \tau_{p}\left(Y_{2, s}^{2}\right)+\tau_{p}\left(\Omega_{\mathfrak{k}}\right) \\
& =-\tau_{p}\left(\Omega_{\mathfrak{l}}\right)+\tau_{p}\left(\Omega_{\mathfrak{k}}\right) \\
& =\tau_{p}\left(\Omega_{\mathfrak{m}}\right) \quad(\text { since } \mathfrak{k}=\mathfrak{m} \oplus \mathfrak{l}) \\
& =\bigoplus_{\sigma \in \widehat{M}\left(\tau_{p}\right)} \bigoplus_{l=1}^{m\left(\sigma, \tau_{p}\right)} \sigma\left(\Omega_{\mathfrak{m}}\right) \\
& =\bigoplus_{\sigma \in \widehat{M}\left(\tau_{p}\right)} \bigoplus_{l=1}^{m\left(\sigma, \tau_{p}\right)}\left[-c(\sigma) \operatorname{Id}_{V_{\sigma}}\right] .
\end{aligned}$$
For convenience, let $L_{p}+s^{2}$ be the differential operator defined by the parentheses in the left hand-side of (3.8). Recall from (2.3) that we have $\alpha_{p}=\rho^{2}-c\left(\sigma_{\text {max }}\right)$. Hence, if we put
$$E=\bigoplus_{\sigma \in \widehat{M}\left(\tau_{p}\right)} \bigoplus_{l=1}^{m\left(\sigma, \tau_{p}\right)}\left[c\left(\sigma_{\max }\right)-c(\sigma)\right] \operatorname{Id}_{V_{\sigma}},$$
we can rewrite $L_{p}$ as
$$L_{p}=-\frac{d^{2}}{d t^{2}}+E+W\left(e^{-t}\right) .$$
By definition of $\Sigma$, the function $\hat{s} \mapsto \sqrt{E+s^{2}}$ is holomorphic on $\Sigma$. Thus, the equation $\left(L_{p}+s^{2}\right) v=0$ is of Fuchsian type, and we can look for a solution of the form
$$v_{p}(\hat{s}, t)=e^{-t \sqrt{E+s^{2}}} \sum_{l=0}^{\infty} a_{l}(\hat{s}) e^{-l t},$$
with coefficients $a_{l}(\hat{s})$ recursively defined by the formulas
$$\begin{aligned}
a_{0}(\hat{s}) & =\operatorname{Id}_{V_{\tau_{p}}}, \\
l\left[2 \sqrt{E+s^{2}}+l \operatorname{Id}_{V_{\tau_{p}}}\right] a_{l}(\hat{s}) & =\sum_{k=1}^{l} w_{k} a_{k-l}(\hat{s}) .
\end{aligned}$$
Denote by $\mathcal{N}$ the set consisting of the $\hat{s} \in \Sigma$ such that $2 \sqrt{E+s^{2}}+l \operatorname{Id}_{V_{\tau_{p}}}$ is a non invertible operator for some $l \in \mathbb{N}^{*}$. Then $\mathcal{N}$ is a discrete subset of $\Sigma \backslash \overline{\mathbb{C}_{+}}$and we obtain a meromorphic map
$$\hat{s} \mapsto v_{p}(\hat{s}, \cdot) \in C^{\infty}\left((0,+\infty), \text { End } V_{\tau_{p}}\right)$$
which satisfies the following properties:
\begin{itemize}
\item[-] $\hat{s} \mapsto v_{p}(\hat{s}, \cdot)$ is holomorphic on $\Sigma \backslash \mathcal{N}$;
\item[-] $v_{p}$ solves the differential equation $\left(L_{p}+s^{2}\right) v_{p}(\hat{s}, \cdot)=0$ on $\mathbb{R}_{+}^{*}$;
\item[-] $v_{p}(\hat{s}, t)=e^{-t \sqrt{E+s^{2}}}\left[\operatorname{Id}_{V_{\tau_{p}}}+\mathrm{O}\left(e^{-t}\right)\right]$ as $t \rightarrow+\infty$.
\end{itemize}
Finally, letting $F_{p}$ be defined on $\Sigma \times G^{0}$ by
$$F_{p}\left(\hat{s}, a_{t}\right)=(\sinh t)^{-d(n-1) / 2}(\sinh 2 t)^{-(d-1) / 2} v_{p}\left(\hat{s}, a_{t}\right),$$
and reminding formula (2.6), we get the statements of our proposition. In particular, remark that (3.6) follows from the estimate
$$F_{p}\left(\hat{s}, a_{t}\right) \underset{t \rightarrow+\infty}{=} e^{-t\left(\sqrt{E+s^{2}}+\rho\right)}\left[\operatorname{Id}_{V_{\tau_{p}}}+\mathrm{O}\left(e^{-t}\right)\right],$$
and that we deduce (3.7) by observing that, if $\hat{s}=\left(s, y_{1}, \ldots, y_{r}\right) \in \Sigma$, we have $\operatorname{Re} y_{j}>\operatorname{Re} s$ for all $j$ on $\mathbb{C}_{+}$. In other words,
$$h(\hat{s})=\operatorname{Re} s \quad \text { on } \mathbb{C}_{+} .$$ \(\square\)

Actually, the function $F_{p}$ we introduced in the proposition is in some sense a multiple (in the variable $\hat{s}$ ) of the Green kernel $G_{p}$. Let us be more precise.

Proposition 3.4. There exists a meromorphic function $\phi_{p}: \Sigma \rightarrow \operatorname{End} V_{\tau_{p}}$, holomorphic in the region $\mathbb{C}_{+}$if $p \neq \frac{d n}{2}$ and in the region $\mathbb{C}_{+} \backslash\left\{\sqrt{\alpha_{p}}\right\}$ if $p=\frac{d n}{2}$, such that the resolvent $R_{p}(\hat{s})$ is given by the operator
$$\begin{aligned}
L^{2}\left(\mathbb{H}_{\mathbb{K}}^{n}\right) & \longrightarrow L^{2}\left(\mathbb{H}_{\mathbb{K}}^{n}\right) \\
u & \longmapsto F_{p}(s, \cdot) * \phi_{p}(s) u
\end{aligned}$$
in the indicated regions.

Proof. Since the expression (2.22) is asymptotic to the Euclidean one for small $t$, we know that a radial solution of the equation
$$\left(\Delta_{p}-\alpha_{p}+s^{2}\right) v=0$$
must behave as $\left[\operatorname{vol}\left(\mathbb{S}^{d n-1}\right) t^{d n-2}\right]^{-1}$ as $t \rightarrow 0$ (if $d n>2$; the argument is similar in the other case). Thus there exists a meromorphic function
$$\psi_{p}: \Sigma \rightarrow \operatorname{End} V_{\tau_{p}},$$
holomorphic on $\Sigma \backslash \mathcal{N}$ and such that
$$F_{p}\left(\hat{s}, a_{t}\right) \underset{t \rightarrow 0}{\simeq} \frac{\psi_{p}(\hat{s})}{\operatorname{vol}\left(\mathbb{S}^{d n-1}\right) t^{d n-2}} .$$
Consequently, for any $u \in C_{0}^{\infty}\left(G, \tau_{p}\right)$ we have
$$\left(\Delta_{p}-\alpha_{p}+s^{2}\right)\left(F_{p}(\hat{s}, \cdot) * u\right)=\psi_{p}(\hat{s}) u .$$
Moreover, for $s \in \mathbb{C}_{+}$, our previous estimates (3.7), (3.12) and (3.1), (3.3) imply the following one: there exists a positive constant $C(s)$ such that
$$\forall t>0,\left\|F_{p}\left(s, a_{t}\right)\right\|_{\text {End } V_{\tau_{p}}} \leq C(s) G_{0}\left(\operatorname{Re} s, a_{t}\right) .$$
Hence the operator
$$u \mapsto F_{p}(s, \cdot) * u \quad \text { is bounded from } L^{2} \text { to } L^{2} .$$

Now we study the invertibility of our function $\psi_{p}$.
Lemma 3.5. (1) If $p \neq \frac{d n}{2}$, the function $\psi_{p}$ is invertible (with holomorphic inverse) in the set $\mathbb{C}_{+}$.
(2) If $p=\frac{d n}{2}$, the function $\psi_{p}$ is invertible (with holomorphic inverse) in the set $\mathbb{C}_{+} \backslash\left\{\sqrt{\alpha_{p}}\right\}$.
Moreover, in both cases, $\psi_{p}^{-1}$ extends meromorphically to $\Sigma$.
Proof. Assume first $p \neq n d / 2$. For $s \in \mathbb{C}_{+}$, let $\xi \in \operatorname{ker} \psi_{p}(s)$. Then $v\left(a_{t}\right)=$ $F_{p}\left(s, a_{t}\right) \xi$ provides a solution of the equation
$$\left(\Delta_{p}-\alpha_{p}+s^{2}\right) v=0,$$
and by (3.10) this solution satisfies
$$v\left(a_{t}\right) \underset{t \rightarrow+\infty}{=} e^{-t\left(\sqrt{E+s^{2}}+\rho\right)} \xi+\mathrm{o}\left(e^{-t\left(\sqrt{E+s^{2}}+\rho\right)} \xi\right) .$$
Hence $v$ is $L^{2}$, but we know that (3.16) has no nontrivial $L^{2}$ solutions since $\operatorname{spec}\left(\Delta_{p}\right)=\left[\alpha_{p},+\infty\right)$ is purely continuous by Theorem 2.2 Thus $v=0$, and therefore $\xi=0$ by (3.17). It follows that $\psi_{p}$ is invertible in the half-plane $\mathbb{C}_{+}$, with holomorphic inverse in this region, and that it has a meromorphic extension to $\Sigma$.

Suppose now $p=\frac{d n}{2}$. Then we know that the discrete spectrum of $\Delta_{p}$ reduces to $\{0\}$, with infinite multiplicity. Proceeding as above, we get the second part of our lemma. \(\square\)

According to the lemma and to (3.13), (3.15), for $s \in \mathbb{C}_{+}$(and with the additional condition $s \neq \sqrt{\alpha_{p}}$ if $p=\frac{d n}{2}$ ), the operator
$$u \in L^{2} \mapsto F_{p}(s, \cdot) * \psi_{p}(s)^{-1} u$$
must be the resolvent $R_{p}(s)$ of the operator $\Delta_{p}-\alpha_{p}+s^{2}$, and this proves our proposition. \(\square\)

We can now sum up our discussion by stating:
Theorem 3.6. The Schwartz kernel $G_{p}(s, \cdot)$ of the resolvent
$$R_{p}(s)=\left(\Delta_{p}-\alpha_{p}+s^{2}\right)^{-1}$$
has a meromorphic extension to $\Sigma$ and, outside the discrete subset of poles which lie inside $\Sigma \backslash \mathbb{C}_{+}$(except if $p=\frac{d n}{2}$, in which case $\sqrt{\alpha_{p}} \in \mathbb{C}_{+}$is also a pole), it satisfies the estimate
$$\forall t>1,\left\|G_{p}\left(\hat{s}, a_{t}\right)\right\|_{\text {End } V_{\tau_{p}}} \leq C(\hat{s}) e^{-(\rho+h(\hat{s})) t}$$
for some constant $C(\hat{s})>0$. Moreover, we have $h(\hat{s})=\operatorname{Re} s$ on $\mathbb{C}_{+}$.
Remark 3.7. 1) The meromorphic extension of the resolvent $R_{p}$ to $\Sigma$ was known to several authors. Namely, U. Bunke and M. Olbrich ([BO3], Lemma 6.2) proved the result for all hyperbolic spaces and their convex cocompact quotients (except in the exceptional case $\mathbb{K}=\mathbb{O}$ ), a fact which was already observed by R. Mazzeo and R. Melrose ([MM])in the real case and by C. Epstein, G. Mendoza and R. Melrose (EMM) in the complex case.
2) The estimate in Theorem 3.6 was announced by N. Lohoué in Loh, but only in the region $\mathbb{C}_{+}$.
3) The analysis we have carried out in this section for the resolvent $R_{p}(s)$ is similar to the one presented in [Far] and [MW] for the function case $(p=0)$.

In order to prepare some results of next section, we discuss now the possible location of the poles of the resolvent $R_{p}$ on $\mathbb{C}$. We first look at the imaginary axis.

Proposition 3.8. The resolvent $R_{p}$ has no pole inside the set
$$i \mathbb{R} \backslash\left\{ \pm i \sqrt{c\left(\sigma_{\max }\right)-c(\sigma)}, \sigma \in \widehat{M}\left(\tau_{p}\right)\right\} .$$
Proof. Assume that $s=i \lambda$ is a purely imaginary pole of $R_{p}$. As in the proof of Lemma 3.5 we see that there exists $\xi \in V_{\tau_{p}}$ such that the function defined by $v\left(a_{t}\right)=F_{p}\left(i \lambda, a_{t}\right) \xi$ is a solution of the equation
$$\left(\Delta_{p}-\alpha_{p}-\lambda^{2}\right) v=0$$
on $\mathbb{H}_{\mathbb{K}}^{n}$. Moreover, when $t \rightarrow+\infty$, this solution satisfies the estimate (see (3.10))
$$v\left(a_{t}\right) \underset{t \rightarrow+\infty}{=} e^{-t\left(\sqrt{E-\lambda^{2}}+\rho\right)} \xi+\mathrm{O}\left(e^{-t}\right) \xi .$$

Let $\xi=\sum_{\sigma \in \widehat{M}\left(\tau_{p}\right)} \xi_{\sigma}$ be the decomposition of $\xi$ with respect to the orthogonal splitting
$$V_{\tau_{p}}=\bigoplus_{\sigma \in \widehat{M}\left(\tau_{p}\right)} V_{\sigma}^{\prime}, \quad \text { where } \quad V_{\sigma}^{\prime}=V_{\sigma} \otimes \mathbb{C}^{m\left(\sigma, \tau_{p}\right)} \text {. }$$
Reminding (3.9), we see that there exists a certain $\varepsilon>0$ such that the following asymptotics holds:
$$v\left(a_{t}\right) \underset{t \rightarrow+\infty}{=} \sum_{\substack{\sigma \in \widehat{M}\left(\tau_{p}\right) \\|\lambda| \geq \sqrt{c\left(\sigma_{\max }\right)-c(\sigma)}}} e^{-t\left(i \sqrt{\lambda^{2}-c\left(\sigma_{\max }\right)+c(\sigma)}+\rho\right)} \xi_{\sigma}+\mathrm{O}\left(e^{-(\rho+\varepsilon) t}\right) \xi .$$

Now, let $B_{R}$ be a geodesic ball of radius $R$ in $\mathbb{H}_{\mathbb{K}}^{n}$. With the Green formula and (3.18) we get:
$$\begin{aligned}
0 & =\left\langle\left(\Delta_{p}-\alpha_{p}-\lambda^{2}\right) v, v\right\rangle_{L^{2}\left(B_{R}\right)}-\left\langle v,\left(\Delta_{p}-\alpha_{p}-\lambda^{2}\right) v\right\rangle_{L^{2}\left(B_{R}\right)} \\
& =2 i \operatorname{Im}\left\langle v^{\prime}, v\right\rangle_{L^{2}\left(\partial B_{R}\right)} .
\end{aligned}$$
But
$$\left\langle v^{\prime}, v\right\rangle_{L^{2}\left(\partial B_{R}\right)}=\operatorname{vol}\left(\partial B_{R}\right)\left\langle v^{\prime}\left(a_{R}\right), v\left(a_{R}\right)\right\rangle_{V_{\tau_{p}}}$$
with
$$\operatorname{vol}\left(\partial B_{R}\right) \simeq \operatorname{vol}\left(\mathbb{S}^{d n-1}\right) e^{2 \rho R},$$
so that (3.20) implies:
$$\sum_{\substack{\sigma \in \widehat{M}\left(\tau_{p}\right) \\|\lambda| \geq \sqrt{c\left(\sigma_{\max }\right)-c(\sigma)}}} \sqrt{\lambda^{2}-c\left(\sigma_{\max }\right)+c(\sigma)}\left|\xi_{\sigma}\right|^{2}=0 .$$

Therefore, if $\lambda \notin\left\{ \pm \sqrt{c\left(\sigma_{\text {max }}\right)-c(\sigma)}, \sigma \in \widehat{M}\left(\tau_{p}\right)\right\}$, then $v \in L^{2}$ by (3.20), but we know from Theorem 2.2 that $\Delta_{p}$ has no $L^{2}$ eigenvalue inside $\left[\alpha_{p},+\infty\right)$. Hence $v=0$ and this proves our proposition. \(\square\)

Reminding the definition (3.4) of $\Sigma$, let us observe that the function $\hat{s} \mapsto s$ is a local coordinate in a neighbourhood of
$$\left(0, \sqrt{c\left(\sigma_{\max }\right)-c\left(\sigma_{1}\right)}, \ldots, \sqrt{c\left(\sigma_{\max }\right)-c\left(\sigma_{r}\right)}\right) \in \Sigma .$$
This fact justifies the abuse of notation in the following statement.
Proposition 3.9. If $\alpha_{p}=0$ (i.e. if $\mathbb{K}=\mathbb{R}$ and $p=\frac{n \pm 1}{2}$, see Theorem 2.2), then the map $s \mapsto s R_{p}(s)$ is holomorphic inside an open neighbourhood of $s=0$ in $\Sigma$.

Proof. By the spectral theorem, we know that the strong limit
$$\lim _{s \rightarrow 0^{+}} s^{2}\left(\Delta_{p}+s^{2}\right)^{-1}$$
is the orthogonal projector onto the $L^{2}$ kernel of $\Delta_{p}$. But this kernel is trivial hence the limit above is zero. As we know that $s \mapsto R_{p}(s)$ is meromorphic inside an open neighbourhood of $s=0$ in $\Sigma$, we get the result. \(\square\)

\section*{4. The spectrum of the differential form Laplacian on hyperbolic MANIFOLDS}

We have now all ingredients to prove the key result of our article, namely the Theorem B stated in the introduction, from which we shall derive various corollaries, and especially vanishing results for the cohomology.
4.1. Spectral results. For convenience, let us recall here the statement of our Theorem B. We remind that $\delta(\Gamma) \leq 2 \rho$.

Theorem 4.1. (1) Assume that $p \neq \frac{d n}{2}$.
\begin{itemize}
\item[(a)] If $\delta(\Gamma) \leq \rho$, then $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq \alpha_{p}$.
\item[(b)] If $\rho \leq \delta(\Gamma) \leq \rho+\sqrt{\alpha_{p}}$, then $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq \alpha_{p}-(\delta(\Gamma)-\rho)^{2}$.
\end{itemize}
(2) Assume that $p=\frac{d n}{2}$.
\begin{itemize}
\item[(a)] If $\delta(\Gamma) \leq \rho$, then either $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=0$ or $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq \alpha_{p}$.
\item[(b)] If $\rho \leq \delta(\Gamma) \leq \rho+\sqrt{\alpha_{p}}$, then either $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=0$ or $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq$ $\alpha_{p}-(\delta(\Gamma)-\rho)^{2}$.
\end{itemize}

Moreover, if $\delta(\Gamma)<\rho+\sqrt{\alpha_{p}}$ the possible eigenvalue 0 is discrete and spectrally isolated.

When $\delta(\Gamma)>\rho+\sqrt{\alpha_{p}}$, assertions (b) are still valid, but yield a triviality since we know that the spectrum must be non negative.

Proof. Suppose first that $p \neq \frac{d n}{2}$, and let $s>0$. By our estimate (3.14), we have
$$\left\|g_{p}(s, d(x, y))\right\| \leq C(s) g_{0}(s, d(x, y))$$
for all $x \neq y$ in $\mathbb{H}_{\mathbb{K}}^{n}$. Thus, if $s+\rho>\delta(\Gamma)$, from our Proposition 3.1 we see that, for $x \neq y$, the sum
$$\sum_{\gamma \in \Gamma} \gamma_{y}^{*} g_{p}(s, d(x, y))$$
is finite and defines therefore the Schwartz kernel of an operator
$$T_{p}(s): C_{0}^{\infty}\left(\wedge^{p} T^{*}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)\right) \longrightarrow L_{\mathrm{loc}}^{2}\left(\wedge^{p} T^{*}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)\right) .$$
Moreover, for any $L^{2} p$-form $\alpha$ on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$, we have by (4.1)
$$\left\|T_{p}(s) \alpha\right\|_{L^{2}} \leq C(s)\left\|\left(\Delta_{0}-\rho^{2}+s^{2}\right)^{-1} u\right\|_{L^{2}},$$
where $u=|\alpha|$. Since the operator $\left(\Delta_{0}-\rho^{2}+s^{2}\right)^{-1}$ is bounded on $L^{2}$, our operator $T_{p}(s)$ is also bounded on $L^{2}$. Moreover it is easy to check that $T_{p}(s)$ provides a right inverse (and thus also a left inverse, by self-adjointness) for the operator $\Delta_{p}-\alpha_{p}+s^{2}$ on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$. In other words, $T_{p}(s)$ is the resolvent of $\Delta_{p}-\alpha_{p}+s^{2}$ on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$.
¿From this discussion we see that $\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \geq \alpha_{p}-s^{2}$ for any $s>0$ such that $T_{p}(s)$ exists, i.e. such that $s+\rho>\delta(\Gamma)$. This proves assertion (1).

Suppose now that $p=\frac{d n}{2}$. The proof above still works, except when $s=\sqrt{\alpha_{p}}$, in which case the pole of $R_{p}(s)$ may yield also a pole for the resolvent on the quotient. Reminding Theorem 2.2 we get the last part of assertion (2). \(\square\)

Before proving that a part of our estimates are optimal for a wide class of hyperbolic manifolds, let us give some information about the nature of the spectrum of $\Delta_{p}$. Recall that $\overline{\mathbb{C}_{+}}$denotes the closure of $\mathbb{C}_{+}$in $\Sigma$ (see (3.4) and (3.5)).

Proposition 4.2. Assume that $\delta(\Gamma)<\rho$. The resolvent
$$s \mapsto\left(\Delta_{p}-\alpha_{p}+s^{2}\right)^{-1}$$
on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$, initially defined on $\mathbb{C}_{+}$, has a holomorphic extension to an open neighbourhood of
$$\overline{\mathbb{C}_{+}} \backslash\left\{\hat{s} \in \Sigma: s= \pm i \sqrt{c\left(\sigma_{\max }\right)-c(\sigma)}, \sigma \in \widehat{M}\left(\tau_{p}\right)\right\} .$$
(When $p=\frac{d n}{2}$, the value $s=\sqrt{\alpha_{p}}$ must be excluded also.) In particular, the differential form spectrum of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is absolutely continuous on
$$\left[\alpha_{p},+\infty\right) \backslash\left\{\alpha_{p}+c\left(\sigma_{\max }\right)-c(\sigma), \sigma \in \widehat{M}\left(\tau_{p}\right)\right\} .$$
Proof. When $\delta(\Gamma)<\rho$, the proof of Theorem 4.1 shows that the sum (4.2) converges for $h(\hat{s})>\delta(\Gamma)-\rho$ as soon as the Green kernel $G_{p}(\hat{s}, \cdot)$ of the resolvent on $\mathbb{H}_{\mathbb{K}}^{n}$ is holomorphic in the considered region. Reminding Theorem 3.6 and Proposition 3.8 and observing that the equality (3.11) extends to an open neighbourhood of
$$\overline{\mathbb{C}_{+}} \backslash\left\{\hat{s} \in \Sigma: s= \pm i \sqrt{c\left(\sigma_{\max }\right)-c(\sigma)}, \sigma \in \widehat{M}\left(\tau_{p}\right)\right\},$$
we get the first assertion. The second one is obtained as in Corollary 3.2 \(\square\)

Next, let us observe that if the limit set $\Lambda(\Gamma)$ of $\Gamma$ is not the whole sphere at infinity $S^{\infty}=\partial \mathbb{H}_{\mathbb{K}}^{n}=\mathbb{S}^{d n-1}$, then the injectivity radius of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is not bounded. Indeed, if $x \in \mathbb{S}^{d n-1} \backslash \Lambda(\Gamma)$, then $x$ has a neighbourhood in $\mathbb{H}_{\mathbb{K}}^{n} \cup \mathbb{S}^{d n-1}$ which is isometrically diffeomorphic to an open subset in $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ via the covering map.

Let us remind that the condition $\Lambda(\Gamma) \neq \mathbb{S}^{d n-1}$ is automatically realized in the setting of convex cocompact or geometrically finite with infinite volume quotients of $\mathbb{H}_{\mathbb{K}}^{n}$.

These remarks served us as a motivation for the two following results.
Proposition 4.3. If the injectivity radius of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is not bounded (for instance if $\Lambda(\Gamma) \neq \mathbb{S}^{d n-1}$ ), then
$$\left[\alpha_{p},+\infty\right) \subset \operatorname{spec}\left(\Delta_{p}, \Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \text { when } p \neq \frac{d n}{2},$$
and
$$\{0\} \cup\left[\alpha_{p},+\infty\right) \subset \operatorname{spec}\left(\Delta_{p}, \Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \text { when } p=\frac{d n}{2} .$$
Proof. If the injectivity radius of the Riemannian manifold $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is not bounded, then $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ contains arbitrary large balls isometric to geodesic balls in $\mathbb{H}_{\mathbb{K}}^{n}$. But an argument due to H. Donnelly and Ch. Fefferman (see the proof of Theorem 5.1.(iii) in [DF]) implies then that the essential spectrum of $\Delta_{p}$ on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ contains the essential spectrum of $\Delta_{p}$ on $\mathbb{H}_{\mathbb{K}}^{n}$. \(\square\)

Together with Theorem 4.1 this result yields immediately a generalization of a result of R. Mazzeo and R. Phillips (Theorem 1.11 in [MP]) when $\delta(\Gamma) \leq \rho$.

Corollary 4.4. If $\delta(\Gamma) \leq \rho$ and if the injectivity radius of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is not bounded, then
$$\operatorname{spec}\left(\Delta_{p}, \Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=\operatorname{spec}\left(\Delta_{p}, \mathbb{H}_{\mathbb{K}}^{n}\right)= \begin{cases}{\left[\alpha_{p},+\infty\right)} & \text { if } p \neq \frac{d n}{2} \\ \{0\} \cup\left[\alpha_{p},+\infty\right) & \text { if } p=\frac{d n}{2}\end{cases}$$
Remark 4.5. When $\Gamma$ is convex cocompact, our corollary is a particular case of a result due to U. Bunke and M. Olbrich (see §11 in [BO1], and also Theorem 9.1 in [Olb2]). Actually, these authors give a much more precise information: the full spectral resolution for all vector bundles over convex cocompact quotients of $\mathbb{H}_{\mathbb{K}}^{n}$ (except for $\mathbb{K}=\mathbb{O}$ and $\delta(\Gamma) \geq \rho$ ).
4.2. Comparison with the Bochner-Weitzenböck method. We think it is worthwhile to compare our estimates for the bottom of the spectrum with the ones we can get with a less elaborated method, based on the Bochner-Weitzenböck formula. Hopefully, it will turn out that the estimates in Theorem 4.1 are strictly better than the latter.

Let $X=\left(X^{m}, g\right)$ be a complete Riemannian manifold of dimension $m$. The Bochner-Weitzenböck formula is the identity
$$\Delta_{p} \alpha=\nabla^{*} \nabla \alpha+\mathcal{R}^{p} \alpha, \quad \forall \alpha \in C_{0}^{\infty}\left(\wedge^{p} T^{*} X\right),$$
where ∇ is the connection on $\wedge^{p} T^{*} X$ induced by the Levi-Civita connection and $\mathcal{R}^{p}$ is a field of symmetric endomorphisms of $\wedge^{p} T^{*} X$ built from the curvature tensor (see e.g. [GM]). For instance, when $X$ has constant curvature -1 (typically $X=\Gamma \backslash \mathbb{H}_{\mathbb{R}}^{m}$ ), the curvature term $\mathcal{R}^{p}$ is quite simple:
$$\mathcal{R}^{p}=-p(m-p) \mathrm{Id},$$
but in general it can be hardly calculated. Let us define thus $\mathcal{R}_{\text {min }}^{p}$ to be the infimum over $x \in X$ of the lowest eigenvalues of the symmetric tensors $\mathcal{R}^{p}(x)$ : $\wedge^{p} T_{x}^{*} X \longrightarrow \wedge^{p} T_{x}^{*} X$. With the Kato inequality, we see that
$$\int_{X}\left(\Delta_{p} \alpha, \alpha\right) \geq \int_{X}|\nabla \alpha|^{2}+\mathcal{R}_{\min }^{p} \int_{X}|\alpha|^{2} \geq\left(\lambda_{0}+\mathcal{R}_{\min }^{p}\right) \int_{X}|\alpha|^{2}$$
for any $\alpha \in C_{0}^{\infty}\left(\wedge^{p} T^{*} X\right)$. In other words:
Proposition 4.6. We have $\lambda_{0}^{p}(X) \geq \lambda_{0}^{0}(X)+\mathcal{R}_{\text {min }}^{p}$.
Let us then compare the lower bounds for $\lambda_{0}^{p}(X)$ given by Theorem 4.1 and Proposition 4.6. For simplicity, we shall look only to the real and complex cases.
4.2.1. The real hyperbolic case. We take $X=\Gamma \backslash \mathbb{H}_{\mathbb{R}}^{n}$. Recall that $\mathcal{R}^{p}=-p(n-p)$ Id and let us restrict to the case $p<n / 2$, thanks to Hodge duality. By Theorem 4.1 and Theorem 2.4 we have
$$\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{R}}^{n}\right) \geq \begin{cases}\left(\frac{n-1}{2}-p\right)^{2} & \text { if } \delta(\Gamma) \leq \frac{n-1}{2}, \\ (n-1-p-\delta(\Gamma))(\delta(\Gamma)-p) & \text { if } \frac{n-1}{2} \leq \delta(\Gamma) \leq n-1-p .\end{cases}$$
Using Proposition 4.6 instead, we get that
$$\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{R}}^{n}\right) \geq \begin{cases}\left(\frac{n-1}{2}-p\right)^{2}-p & \text { if } \delta(\Gamma) \leq \frac{n-1}{2}, \\ \delta(\Gamma)(n-1-\delta(\Gamma))-p(n-p) & \text { if } \frac{n-1}{2} \leq \delta(\Gamma) \leq n-1-p .\end{cases}$$
We thus see that, in all cases,
$$\text { (estimate from Theorem } 4.1 \text { ) = (estimate from Proposition 4.6) }+p \text {. }$$
4.2.2. The complex hyperbolic case. We take now $X=\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$. In that situation, our first task is to compute the value of $\mathcal{R}_{\text {min }}^{p}$ :

Proposition 4.7. For the manifold $X=\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$, we have
$$\mathcal{R}_{\min }^{p}= \begin{cases}-2 p(n+1) & \text { if } p \leq n, \\ -2(2 n-p)(n+1) & \text { if } p \geq n\end{cases}$$
Proof. In order to prove this result, we collect first some information from the article [Ped3].

For $0 \leq p \leq 2 n$, the representation $\tau_{p}$ of $K$ splits up into the direct sum
$$\tau_{p}=\bigoplus_{r+s=p} \tau_{r, s}$$
corresponding to the decomposition into differential forms of type $(r, s)$. Besides, each $\tau_{r, s}$ can be decomposed in its turn into irreducible subrepresentations:
$$\tau_{r, s}=\bigoplus_{k=0}^{\min (r, s)} \tau_{r-k, s-k}^{\prime},$$
a fact which actually reflects the Lefschetz decomposition into primitive forms. To sum up, we have
$$\tau_{p}=\bigoplus_{r+s=p} \bigoplus_{k=0}^{\min (r, s)} \tau_{r-k, s-k}^{\prime} .$$

Let us mention three natural equivalences:
$$\begin{aligned}
\tau_{r, s} & \sim \overline{\tau_{s, r}} & & (\text { complex conjugation }), \\
\tau_{r, s} & \sim \tau_{n-s, n-r} & & (\text { Hodge duality }), \\
\tau_{p} & \sim \tau_{2 n-p} & & (\text { idem }),
\end{aligned}$$
whose first two hold also for the $\tau_{r, s}^{\prime}$. Denoting by $\mathcal{B}=\nabla^{*} \nabla$ the Bochner Laplacian, we can write the following Bochner-Weitzenböck formulas:
$$\begin{aligned}
\Delta_{r, s}^{\prime}= & \mathcal{B}_{r, s}^{\prime}+\tau_{r, s}^{\prime}\left(\Omega_{\mathfrak{k}}\right)=\mathcal{B}_{r, s}^{\prime}-c\left(\tau_{r, s}^{\prime}\right) \mathrm{Id}, \\
& \quad \text { where } \quad c\left(\tau_{r, s}^{\prime}\right)=\left\langle\mu_{\tau_{r, s}^{\prime}}, \mu_{\tau_{r, s}^{\prime}}^{\prime}+2 \delta_{\mathfrak{k}}\right\rangle, \\
\Delta_{r, s}= & \mathcal{B}_{r, s}+\tau_{r, s}\left(\Omega_{\mathfrak{k}}\right), \\
\Delta_{p}= & \mathcal{B}_{p}+\tau_{p}\left(\Omega_{\mathfrak{k}}\right) .
\end{aligned}$$
Our aim is thus to calculate
$$\mathcal{R}_{\min }^{p}=\inf \left\{-c\left(\tau_{r-k, s-k}^{\prime}\right), r+s=p, k=0, \ldots, \min (r, s)\right\} .$$
¿From (3.8) in Ped3) we easily see that
$$c\left(\tau_{r, s}^{\prime}\right)=2 r(n-s+1)+2 s(n-r+1)=2(r+s)(n+1)-4 r s$$
when $r+s \leq n$, and that $c\left(\tau_{r, s}^{\prime}\right)$ is given by a combination of this formula with (4.5) when $r+s \geq n$.
¿From (4.9) we deduce that:
\begin{itemize}
\item[-] if $(r, s)$ is fixed with $r+s \leq n$, then $c\left(\tau_{r, s}^{\prime}\right) \geq c\left(\tau_{r-k, s-k}^{\prime}\right)$ for any $k \in \mathbb{N}$;
\item[-] if $r+s=p \leq n$ is fixed, then $c\left(\tau_{r, s}^{\prime}\right)=2(r+s)(n+1)-4 r s$ is maximal for $r=0$ or $s=0$, in which cases it takes the same value $2 p(n+1)$.
\end{itemize}
With (4.4) and (4.6) we finally obtain the aimed result. \(\square\)

Now we go back to our comparisons. Assume $p<n$. By Theorem 4.1 and Theorem 2.4 we have
$$\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right) \geq \begin{cases}(n-p)^{2} & \text { if } \delta(\Gamma) \leq n \\ (2 n-p-\delta(\Gamma))(\delta(\Gamma)-p) & \text { if } n \leq \delta(\Gamma) \leq 2 n-p,\end{cases}$$
whereas Proposition 4.6 yields
$$\lambda_{0}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right) \geq \begin{cases}n^{2}-2 p(n+1) & \text { if } \delta(\Gamma) \leq n, \\ \delta(\Gamma)(2 n-\delta(\Gamma))-2 p(n+1) & \text { if } n \leq \delta(\Gamma) \leq 2 n-p .\end{cases}$$
In both cases, it turns out that
(estimate from Theorem 4.1) = (estimate from Proposition 4.6) $+p(p+2)$.
4.3. Applications to cohomology. We shall use in the sequel the following notation: if $X$ is any complete manifold,
$$\begin{aligned}
& H^{p}(X)=p \text {-th de Rham cohomology space of } X, \\
& \mathcal{H}^{p}(X)=\text { Hilbert space of } L^{2} \text { harmonic } p \text {-forms on } X .
\end{aligned}$$

Let us remark first that our Theorem 4.1 extends to the case of a differential form Laplacian with values in a unitary flat vector bundle or even in a Hilbertian flat vector bundle. Indeed, if $\left(\pi, H_{\pi}\right)$ is a unitary representation of $\Gamma$, the $H_{\pi}$-valued Hodge-de Rham operator $\Delta_{p}^{\pi}$ is simply $\Delta_{p} \otimes \mathrm{Id}_{H_{\pi}}$ when lifted to the universal cover. Thus we can use similar estimates for the corresponding Green kernel.

Keeping this generalization in mind, we state now the following vanishing result.
Theorem 4.8. Assume $p \neq \frac{d n}{2}$. If $\Gamma$ and $p$ are such that $\delta(\Gamma)<\rho+\sqrt{\alpha_{p}}$, then
$$\mathcal{H}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n} ; H_{\pi}\right)=\{0\} .$$
Proof. When $\alpha_{p}>0$, the corollary follows immediately from Theorem 4.1 When $\alpha_{p}=0$, we know from Proposition 3.9 that $s \mapsto s R_{p}(s)=s\left(\Delta_{p}+s^{2}\right)^{-1}$ extends holomorphically to a neighbourhood of $s=0$ in $\Sigma$. Let us denote by $\Delta_{p}^{\Gamma}$ the Laplacian acting on the quotient $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$. Then the proof of Theorem 4.1 shows that the map $s \mapsto s\left(\Delta_{p}^{\Gamma}+s^{2}\right)^{-1}$ also extends holomorphically to a neighbourhood of $s=0$ in $\Sigma$ as soon as the assumption $\delta(\Gamma)<\rho$ is fulfilled. As in the proof of Proposition 3.9 the spectral theorem implies that the $L^{2}$ kernel of $\Delta_{p}^{\Gamma}$ must be trivial. \(\square\)

Remark 4.9. 1) In the convex cocompact case, this vanishing result has been also proved by M. Olbrich (see Corollary 9.9 in [Olb2]).
2) In [CGH], D. Calderbank, P. Gauduchon and M. Herzlich have proved refined Kato inequalities for special classes of sections of vector bundles $E$ over a Riemannian (or spin) manifold $X=\left(X^{m}, g\right)$. Namely, they consider bundles over $X$ attached to an irreducible representation of the holonomy group $S O(m)$ and sections which lie in the kernel of a natural injectively elliptic first-order differential operator. Their approach is based on the representation theory of $S O(m)$. In our situation $X=\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$, an application of their results (Theorem 3.1.ii and Theorem 6.3.ii) gives the following statement: if $\alpha$ is a harmonic $p$-form on $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$, then we have the refined Kato inequality
$$|\nabla \alpha|^{2} \geq \frac{d n-p+1}{d n-p}|d| \alpha| |^{2} .$$
As a consequence, with notation of Section 4.2 if $\frac{d n-p+1}{d n-p} \lambda_{0}^{0}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)+\mathcal{R}_{\text {min }}^{p}>0$, then $\mathcal{H}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)=\{0\}$.

When $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$, an easy calculation shows that this vanishing result is strictly weaker than our Theorem 4.8 When $\mathbb{K} \neq \mathbb{R}$, an obvious explanation is that one expects another refined Kato inequality based on the representation theory of $K$ instead of the one of $S O(d n)$. On the other hand, as shown in [CGH], in order to obtain an optimal result with this technique one has to consider $\Delta|\alpha|^{\theta}$, where $\alpha$ is a $L^{2}$ harmonic $p$-form, and $\theta=(d n-p-1) /(d n-p)$. An easy computation shows that
$$\Delta|\alpha|^{\theta} \leq \theta\left(-\mathcal{R}_{\min }^{p}\right)|\alpha|^{\theta} .$$
Hence, if $|\alpha|^{\theta}$ is non zero and $L^{2}$, we get $\lambda_{0}^{0}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \leq \theta\left(-\mathcal{R}_{\text {min }}^{p}\right)$. In that case, the vanishing result we obtain recovers our Theorem 4.8 in the real case, and is still weaker in the complex case. Moreover it is in general very difficult to check if $|\alpha|^{\theta} \in L^{2}$.

In some cases, the Hilbert spaces $\mathcal{H}^{p}(X)$ have a topological interpretation in terms of cohomology groups, in the spirit of the Hodge Theorem (see for instance, Maz and Yeg for convex cocompact real hyperbolic manifolds, and MP for geometrically finite real hyperbolic manifolds). In this direction, our vanishing result Theorem 4.8 also provides vanishing results for certain cohomology groups, with a dependance on the critical exponent.

In fact, for convex cocompact real hyperbolic manifolds, the vanishing results we can derive from Theorem 4.8 are well known (see Ize, IN, Nay, as well as [Wan2] for another approach based on the Bochner technique).

We therefore prefer to focus on two topological applications of our Theorem 4.8 which seem completely new. The first one enables us to investigate the number of ends of certain classes of hyperbolic manifolds, but we postpone its statement until next section (see Theorem 5.4), which will be particularly devoted to that question in a more general setting. The second one is specific to the complex hyperbolic case:

Proposition 4.10. Suppose that $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ is convex cocompact. If $p$ is such that $p>n$ and $p>\delta(\Gamma)$, then $\mathcal{H}^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right)=\{0\}$ and $H^{p}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right)=\{0\}$.

Proof. According to T. Ohsawa and K. Takegoshi (Corollary 4.2 in [OT]), if $(M, h)$ is a complete Hermitian manifold of complex dimension $n$ which is Kählerian outside some compact subset $A$, and such that the Kähler form can be written as $\omega=i \partial \bar{\partial} s$ with $s \in C^{\infty}(M \backslash A, \mathbb{R}), \lim _{m \rightarrow \infty} s(m)=+\infty$ and $\partial s$ bounded, then there is an isomorphism $\mathcal{H}^{p}(M) \simeq H^{p}(M)$ for any $p>n$. These assumptions may not be satisfied by $M=\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ with $\Gamma$ convex cocompact. However, we claim that the complex hyperbolic metric of such a manifold $M$ is quasi-isometric to a Hermitian metric $h$ which fulfils the above conditions; and this is obviously enough to apply the result of T. Ohsawa and K. Takegoshi.

Let us elaborate. For convenience, we shall view the complex hyperbolic space $\mathbb{H}_{\mathbb{C}}^{n}$ as the open unit ball $\mathbb{B}_{\mathbb{C}}^{n}$ of $\mathbb{C}^{n}$. With our choice of normalization of the Riemannian metric (2.7), this manifold is equipped with a Kähler metric of constant holomorphic sectional curvature equal to -4 , and the corresponding Kähler form is given by the formula
$$\tilde{\omega}=-i \partial \bar{\partial} \log \left(1-|z|^{2}\right)=i \frac{\sum_{i} d z_{i} \wedge d \bar{z}_{i}}{1-|z|^{2}}+i \frac{\left(\sum_{i} \bar{z}_{i} d z_{i}\right) \wedge\left(\sum_{i} z_{i} d \bar{z}_{i}\right)}{\left(1-|z|^{2}\right)^{2}} .$$
Letting $\tilde{s}(z)=-\log \left(1-|z|^{2}\right)$, we thus have $\tilde{\omega}=i \partial \bar{\partial} \tilde{s}$ with $\lim _{m \rightarrow \infty} \tilde{s}(m)=+\infty$ and $\partial \tilde{s}$ bounded. Moreover, on $\mathbb{B}_{\mathbb{C}}^{n}$, the (Riemannian) hyperbolic metric $g_{\text {hyp }}$ and the Euclidean one $g_{\text {eucl }}$ are easily compared:
$$g_{\mathrm{hyp}} \geq e^{\tilde{s}} g_{\mathrm{eucl}} .$$

Next, we observe that our $M=\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ (with $\Gamma$ convex cocompact) is diffeomorphic to the interior of a compact manifold $\bar{M}$ with boundary $\partial \bar{M}$, and each point $p \in \partial \bar{M}$ has a neighbourhood $V_{p}$ in $\bar{M}$ which is isometric to a neighbourhood of $(1,0, \ldots, 0)$ in $\overline{\mathbb{H}_{\mathbb{C}}^{n}}=\overline{\mathbb{B}_{\mathbb{C}}^{n}}$. Thus, by the preceding observation, there exists a function $s_{p}$ on $V_{p}$ such that $s_{p}^{-1}(\infty)=\partial \bar{M} \cap V_{p}, \omega=i \partial \bar{\partial} s_{p}$ and $\partial s_{p}$ is bounded (here, $\omega$ denotes the Kähler metric on $M$ ). By compactness, we can exhibit a finite subset $\left\{p_{1}, \ldots, p_{l}\right\} \subset \partial \bar{M}$ such that $\partial \bar{M} \subset \bigcup_{i} V_{p_{i}}$. Let $\left\{\varphi_{i}\right\}$ be a partition of unity associated with the covering $\bigcup_{i} V_{p_{i}}$ and let $s=\sum_{i} \varphi_{i} s_{p_{i}}$. It is clear that $\lim _{m \rightarrow \partial \bar{M}} s(m)=+\infty$. On the other hand, each function $\varphi_{i}$ is smooth on $\overline{V_{p_{i}}}$ and (4.10) implies the estimates $\left|d \varphi_{i}\right|=\mathrm{O}\left(e^{-s_{p_{i}} / 2}\right)$ and $\left|\partial \bar{\partial} \varphi_{i}\right|=\mathrm{O}\left(e^{-s_{p_{i}}}\right)$ on $\overline{V_{p_{i}}}$. Hence we have
$$|i \partial \bar{\partial} s-\omega| \leq C \sum_{i} e^{-s_{p_{i}} / 2} \chi_{V_{p_{i}}},$$
where $\chi_{V_{p_{i}}}$ denotes the characteristic function of $V_{p_{i}}$. Since
$$\lim _{m \rightarrow \partial \bar{M}} \sum_{i} e^{-s_{p_{i}}(m) / 2} \chi_{V_{p_{i}}}(m)=0$$
we find that the Kähler metric $\omega$ on $M$ is, near the boundary $\partial \bar{M}$, quasi-isometric to the Kähler metric $i \partial \bar{\partial} s$. A similar argument shows also that $\partial s$ is bounded. Thus, if $h$ denotes a Hermitian metric on $M$ which coincides with the Hermitian metric associated with $i \partial \bar{\partial} s$ near the boundary $\partial \bar{M}$, then $h$ is quasi-isometric to the Hermitian metric associated with $\omega$, everywhere on $M$ (since any two Hermitian metrics are quasi-isometric on a compact set). This discussion proves our claim.

Now, recall from Theorem 2.4 that $\alpha_{p}=(n-p)^{2}$. Since $p>n$ we have $\delta(\Gamma)<$ $p=n+\sqrt{\alpha_{p}}$, and we can apply Theorem 4.8 to obtain the vanishing result. \(\square\)

As a consequence, we partially recover a result of G. Besson, G. Courtois and S. Gallot ([BCG1]):

Corollary 4.11. Assume that $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ is a compact complex hyperbolic manifold. Let $\pi: \Gamma \rightarrow S U(m, 1)$ be a convex cocompact representation of $\Gamma$, where $m<2 n$. Then $\delta(\pi(\Gamma)) \geq 2 n=\delta(\Gamma)$.

Proof. From our last proposition, if $\delta(\pi(\Gamma))<2 n$, then
$$H^{2 n}\left(\pi(\Gamma) \backslash \mathbb{H}_{\mathbb{C}}^{m}\right)=\{0\} .$$
But, by definition of $\pi$ we have $H^{2 n}\left(\pi(\Gamma) \backslash \mathbb{H}_{\mathbb{C}}^{m}\right)=H^{2 n}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right)$, and the latter cohomology group is obviously non trivial since $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ is a compact oriented manifold. This discussion forces $\delta(\pi(\Gamma)) \geq 2 n$. (Note that $\delta(\Gamma)=2 \rho=2 n$ because $\Gamma$ is cocompact.) \(\square\)

Remark 4.12. The result of G. Besson, G. Courtois and S. Gallot is in fact much better than ours: it holds without any assumptions on $n$ and $m$ and it says also that there is a constant $C(n, m)$ such that if $\delta(\pi(\Gamma)) \leq 2 n+C(n, m)$ then $\pi(\Gamma)$ is a totally geodesic representation. Note that the analogue of this phenomenon in the real hyperbolic case is also known (see Bow, Ize], IN], Nay, Wan1, Wan2, as well as [BCG1] for a different proof and a more general result).

\section*{5. On the number of ends of certain noncompact locally symmetric spaces}

Let $X$ be an open manifold of dimension $m$. In what follows, we shall use the classical notations:
$$\begin{aligned}
& H_{0}^{p}(X)=p \text {-th compactly supported de Rham cohomology space of } X, \\
& H_{p}(X)=p \text {-th homology space of } X .
\end{aligned}$$
We shall also consider the analogues of theses (co)homology spaces with coefficients in the constant presheaf $\mathbb{Z}$, denoted by $H_{0}^{p}(X, \mathbb{Z})$ and $H_{p}(X, \mathbb{Z})$, respectively. When $X$ is orientable, the Poincaré duality asserts that
$$H_{0}^{p}(X) \simeq\left[H^{m-p}(X)\right]^{*} \simeq H_{m-p}(X), \quad H_{0}^{p}(X, \mathbb{Z}) \simeq\left[H^{m-p}(X, \mathbb{Z})\right]^{*} \simeq H_{m-p}(X, \mathbb{Z}),$$
as soon as these spaces are finite dimensional.
Next, recall that the number of ends of $X$ is the supremum over all compact subsets $A \subset X$ of the number of unbounded connected components of $X \backslash A$.

In this section, we shall give sufficient conditions for a noncompact locally symmetric space $X$ (not necessarily of rank one) to have only one end, by showing in fact a stronger result (as is well-known), namely that $H_{0}^{1}(X)=\{0\}$. Our motivation was at the beginning to look at the complex hyperbolic case, after E. Ghys posed the problem to the first author. It turns out that we were actually able to consider more general situations.

Before describing our results, we need some topological tools.
5.1. Topological preliminaries. Let us begin with the following result (see [Car], Theorem 3.3, for a related observation, and compare with [LiW] as well).

Proposition 5.1. If $X=\left(X^{m}, g\right)$ is a complete Riemannian manifold such that every unbounded connected component of the complement of any compact subset of $X$ has infinite volume (for instance if the injectivity radius is positive) and such that $\lambda_{0}^{0}(X)>0$, then the natural map
$$H_{0}^{1}(X) \longrightarrow \mathcal{H}^{1}(X)$$
is injective. In particular, if furthermore $\lambda_{0}^{1}(X)>0$ then $X$ has only one end (and also $H_{m-1}(X)=\{0\}$ if $X$ is orientable).

Proof. Recall first that the spaces of $L^{2}$ harmonic forms admit a reduced $L^{2}$ cohomology interpretation:
$$\mathcal{H}^{p}(X) \simeq\left\{\alpha \in L^{2}\left(\wedge^{p} T^{*} X\right), d \alpha=0\right\} / \overline{d C_{0}^{\infty}\left(\wedge^{p-1} T^{*} X\right)},$$
where closure is taken with respect to the $L^{2}$ topology. Hence, if $[\alpha] \in H_{0}^{1}(X)$ is mapped to zero in $\mathcal{H}^{1}(X)$, there is a sequence $\left(f_{k}\right)$ of smooth functions with compact support on $X$ such that $\alpha=\lim _{L^{2}} d f_{k}$. Since we have the inequality
$$\left\|d f_{k}-d f_{l}\right\|_{L^{2}}^{2} \geq \lambda_{0}^{0}(X)\left\|f_{k}-f_{l}\right\|_{L^{2}}^{2},$$
and since $\lambda_{0}^{0}(X)>0$, we conclude that this sequence $\left(f_{k}\right)$ converges to some $f \in L^{2}$, so that $\alpha=d f$. But $\alpha$ has compact support, hence $f$ is locally constant outside the compact set $\operatorname{supp}(\alpha)$. Since all unbounded connected components of $X \backslash \operatorname{supp}(\alpha)$ have infinite volume and since $f \in L^{2}$, we see that $f$ has compact support, hence $[\alpha]=[d f]=0$. \(\square\)

In the proof of the last proposition, we have used the fact that $X$ has only one end as soon as $H_{0}^{1}(X)=\{0\}$. Next result gives a sort of converse.

Proposition 5.2. If $X=X^{m}$ is an open manifold having one end, and if every twofold normal covering of $X$ has also one end, then
$$H_{0}^{1}(X, \mathbb{Z})=\{0\} .$$
In particular, $H_{0}^{1}(X)=\{0\}$ and if furthermore $X$ is orientable, then
$$H_{m-1}(X, \mathbb{Z})=\{0\} .$$
Proof. Since $X$ has only one end, we have an exact sequence
$$\{0\} \rightarrow H_{0}^{1}(X, \mathbb{Z}) \rightarrow H^{1}(X, \mathbb{Z}) .$$
Pick an element in $H_{0}^{1}(X, \mathbb{Z})$, and consider its image $\sigma$ in $H^{1}(X, \mathbb{Z})$. With $\sigma$ is associated a continuous map $f: X \rightarrow \mathbb{S}^{1}$, and an induced homomorphism $f_{*}$ : $\pi_{1}(X) \rightarrow \mathbb{Z}$. Because $\sigma$ has a representative with compact support, $f$ is constant outside a compact set $C$; this constant is normalized to be 1.

Assume that $\sigma$ is not zero, then $f_{*}$ is not zero either, and has image $n \mathbb{Z}$, with $n \neq 0$. Then $\Gamma=\operatorname{ker}\left\{f_{*} \bmod 2 n \mathbb{Z}\right\}$ is a normal subgroup of index 2 in $\pi_{1}(X)$. Let $\widehat{X}$ be the corresponding twofold normal covering of $X$, and let $\pi: \widehat{X} \rightarrow X$ be the covering map. Putting $s(z)=z^{2}$, we have a commutative diagram:
![](https://cdn.mathpix.com/cropped/85c82e8a-07a7-4c8e-a90e-74e76023ca8f-28.jpg?height=201&width=231&top_left_y=591&top_left_x=944)
But now $\widehat{X} \backslash \pi^{-1}(C)$ has at least two unbounded connected components. Indeed, on the open set $\widehat{X} \backslash \pi^{-1}(C), \widehat{f}$ is locally constant, taking both values 1 and -1. Hence a contradiction, so $\sigma$ must be trivial in $H^{1}(X, \mathbb{Z})$, and eventually $H_{0}^{1}(X, \mathbb{Z})=\{0\}$. \(\square\)

Although we shall not need it in the sequel, let us mention that we obtain a new proof of a result due to Z. Shen and C. Sormani ([SS]) as a corollary of Proposition 5.2

Proposition 5.3. If $X=\left(X^{m}, g\right)$ is a complete oriented Riemannian manifold with non negative Ricci curvature, then either:
\begin{itemize}
\item[(1)] $H_{m-1}(X, \mathbb{Z})=\{0\}$;
\item[(2)] or $X$ is the determinant line bundle of a non orientable compact manifold with non negative Ricci curvature, and in that case $H_{m-1}(X, \mathbb{Z}) \simeq \mathbb{Z}$;
\item[(3)] or $X$ is isometric to $\Sigma \times \mathbb{R}$ with $\Sigma$ an oriented compact Riemannian manifold with non negative Ricci curvature, and in that case $H_{m-1}(X, \mathbb{Z}) \simeq \mathbb{Z}$.
\end{itemize}

Proof. According to a famous result of J. Cheeger and D. Gromoll ([CG]), either $X$ has one end or $X$ is isometric to $\Sigma \times \mathbb{R}$, with $\Sigma$ as in the statement (3). Assume that the first possibility holds. Then we have the same alternative for any twofold normal covering $\widehat{X}$ of $X$. If $\widehat{X}$ has only one end, we can apply Proposition 5.2 and obtain (1).

Thus, let us assume instead that $\widehat{X}$ is isometric to $\widehat{\Sigma} \times \mathbb{R}$, with $\widehat{\Sigma}$ as before. This means that $X=(\widehat{\Sigma} \times \mathbb{R}) /\{\operatorname{Id}, \gamma\}$ for some isometry $\gamma$ of $\widehat{\Sigma} \times \mathbb{R}$. By the Cheeger-Gromoll result, a line in $\widehat{\Sigma} \times \mathbb{R}$ is of the form $\{\theta\} \times \mathbb{R}$, where $\theta \in \widehat{\Sigma}$. Since $\gamma$ must preserve the set of lines in $\widehat{\Sigma} \times \mathbb{R}$, we see that there exist $a \in \mathbb{R}$ and an isometry $f$ of $\widehat{\Sigma}$ such that $\gamma(\theta, t)=(f(\theta), \pm t+a)$. Since also $\gamma \circ \gamma=\mathrm{Id}$, we must have $\gamma(\theta, t)=(f(\theta),-t+a)$. And as $X$ is oriented, we see that $f$ has to reverse orientation on $\widehat{\Sigma}$. \(\square\)
5.2. The case of general hyperbolic manifolds. We are now able to give the second topological application of Theorem 4.8

Theorem 5.4. Assume that $\mathbb{H}_{\mathbb{K}}^{n} \neq \mathbb{H}_{\mathbb{R}}^{2}$. If $\delta(\Gamma)<\rho+\sqrt{\alpha_{1}}$ and if all unbounded connected components of the complement of any compact subset of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ have infinite volume, then $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ has only one end, and
$$H_{d n-1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}, \mathbb{Z}\right)=\{0\} .$$
Remark 5.5. Except maybe for $\mathbb{K}=\mathbb{O}$, we know from Theorem 2.4 that $\alpha_{1}=$ $(\rho-1)^{2}$, hence the assumption $\delta(\Gamma)<\rho+\sqrt{\alpha_{1}}$ in this statement is equivalent to $\delta(\Gamma)<2 \rho-1$. Since in any case $\delta(\Gamma) \leq 2 \rho$, we see that our assumption is not too restrictive.

Proof. With the hypotheses of the theorem, we know from Theorem 4.8 that $\lambda_{0}^{1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)>0$. By Theorem A we also have $\lambda_{0}^{0}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}\right)>0$, except if $\delta(\Gamma)=2 \rho$. Since we have assumed $\delta(\Gamma)<\rho+\sqrt{\alpha_{1}}$, this cannot occur, as shown by (2.18).

So, the result follows from Proposition 5.1 and Proposition 5.2 \(\square\)

Actually, the assumption on $\delta(\Gamma)$ in the previous result is useless in the quaternionic and octiononic cases:

Corollary 5.6. Let $\mathbb{K}=\mathbb{H}$ or $\mathbb{O}$. If all unbounded connected components of the complement of any compact subset of $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ have infinite volume, then $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ has only one end, and
$$H_{d n-1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}, \mathbb{Z}\right)=\{0\} .$$
Proof. The hypothesis implies that $\Gamma \backslash \mathbb{H}_{\mathbb{K}}^{n}$ itself has infinite volume, so that we can use a rigidity result due to K. Corlette ([Cor], Theorem 4.4; see also [Olb2], Corollary 4.22 for a slight refinement).

Suppose first that $\mathbb{K}=\mathbb{H}$. According to Corlette's result, we have $\delta(\Gamma) \leq 4 n$. In particular we always have $\delta(\Gamma) \leq 4 n<4 n+1=2 \rho-1$, so that Theorem 5.4 applies.

Suppose now that $\mathbb{K}=\mathbb{O}$. In that case Corlette's result says that $\delta(\Gamma) \leq 16$. M. Olbrich kindly communicated to us that he was able to calculate the value of $\alpha_{1}$, namely he found $\alpha_{1}=97$, so that $\rho+\sqrt{\alpha_{1}}>20>\delta(\Gamma)$ and we can use again Theorem 5.4 Another possible argument is the following: Theorem A implies that $\lambda_{0}^{0}\left(\Gamma \backslash \mathbb{H}_{\mathbb{O}}^{2}\right) \geq 96=6 \times 16$, and since $\Gamma \backslash \mathbb{H}_{\mathbb{O}}^{2}$ is an Einstein manifold with Ricci curvature equal to -36, the Bochner formula (4.6) yields $\lambda_{0}^{1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{O}}^{2}\right) \geq 60>0$, so that $\mathcal{H}^{1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{O}}^{2}\right)=\{0\}$. Thus we can use Proposition 5.1 and Proposition 5.2 \(\square\)

Remark 5.7. Our Corollary 5.6 extends a result of K. Corlette about convex cocompact quotients of quaternionic and octonionic hyperbolic spaces (see [Cor], Theorem 7.1).

As another consequence of Theorem 5.4 we give a simple proof of a result due to Y. Shalom ([Sha], Theorem 1.6), which we shall actually improve a bit later on in the $S U(n, 1)$ case (see Corollary 5.14).

Corollary 5.8. Assume that $\Gamma=A *_{C} B$ is a cocompact subgroup of $S O_{e}(n, 1)$ (with $n \geq 3$ ) or $S U(n, 1)$ (with $n \geq 2$ ) which is a free product of subgroups $A$ and $B$ over the amalgamated subgroup $C$. Then $\delta(C) \geq 2 \rho-1$.

Proof. Let $\mathbb{K}$ be either $\mathbb{R}$ or $\mathbb{C}$. By a recent result of G. Besson, G. Courtois and S. Gallot ([BCG2]) we have
$$H_{d n-1}\left(C \backslash \mathbb{H}_{\mathbb{K}}^{n}\right) \neq\{0\} .$$
But $C \backslash \mathbb{H}_{\mathbb{K}}^{n}$ is a Riemannian covering of a compact hyperbolic manifold, so its injectivity radius has a uniform positive lower bound and the unbounded connected components of the complement of any compact subset of $C \backslash \mathbb{H}_{\mathbb{K}}^{n}$ must have infinite volume. To avoid contradiction with Theorem 5.4 (and Remark 5.5), we must have $\delta(C) \geq 2 \rho-1$. \(\square\)

Remark 5.9. In his paper, Y. Shalom proves actually a better result in the complex case, namely, that the inequality is strict. Besides, [BCG2] gives a substantial generalization of Shalom's result: if $A *_{C} B$ is the fundamental group of a compact

Riemannian manifold ( $X^{m}, g$ ) with sectional curvature less than -1, then $\delta(C) \geq$ $m-2$. Also, the equality case is characterized when $X$ is real hyperbolic and $m \geq 4$.

Note that Corollary 5.8 is meaningless in the quaternionic or octonionic case. Indeed, since $S p(n, 1)$ and $F_{4(-20)}$ satisfy the property (T) of Kazhdan, it is well known that none of their cocompact subgroups can be an almagamated product (see §6.a in [HV]).
5.3. The case of locally symmetric spaces which have the Kazhdan property. Let us give now an analogue of Corollary 5.6 in the case of more general noncompact locally symmetric spaces whose isometry group satisfies Kazhdan's property $(T)$.

Theorem 5.10. Let $G / K$ be a symmetric space without any compact factor and without any factor isometric to a real or complex hyperbolic space. Assume that $\Gamma \subset G$ is a torsion-free, discrete subgroup of $G$ such that $\Gamma \backslash G / K$ is non compact and that all unbounded connected components of the complement of any compact subset of $\Gamma \backslash G / K$ have infinite volume. Then $\Gamma \backslash G / K$ has only one end, and
$$H_{m-1}(\Gamma \backslash G / K, \mathbb{Z})=\{0\},$$
where $m=\operatorname{dim}(G / K)$.
Proof. Under our assumptions $G$ satisfies property $(T)$, and the quotients $\Gamma \backslash G / K$ and $\Gamma \backslash G$ have infinite volume. Thus the right regular representation of $G$ on $L^{2}(\Gamma \backslash G)$ has no nontrivial almost invariant vector, and this implies that $\lambda_{0}^{0}(\Gamma \backslash G / K)>$ 0: if instead we had $\lambda_{0}^{0}(\Gamma \backslash G / K)=0$, we could construct a sequence $\left(f_{l}\right)$ of smooth functions with compact support on $\Gamma \backslash G / K$ such that $\left\|d f_{l}\right\|_{L^{2}} \leq\left\|f_{l}\right\|_{L^{2}} / l$. By pulling back this sequence to $\Gamma \backslash G$, we would obtain a sequence of nontrivial almost invariant vectors in $L^{2}(\Gamma \backslash G)$, which is absurd.

Next, the fact that $\mathcal{H}^{1}(\Gamma \backslash G / K)=\{0\}$, and thus that $\Gamma \backslash G / K$ has only one end by Proposition 5.1, is also a heritage of the property $(T)$. Let us elaborate.

According to N. Mok (Mok]) and P. Pansu ([Pan]), the property ( $T$ ) for the group $G$ can be shown with a Bochner type formula which is in fact a special case of a refinement of the Matsushima formula obtained by N. Mok, Y. Siu and S. Yeung ([MSY). In particular there exists on $G / K$ (and on $\Gamma \backslash G / K$ ) a parallel curvature tensor $B$ which is positive definite on symmetric 2-tensors having vanishing trace, and such that for any $L^{2}$ harmonic 1-form $\alpha$ on $\Gamma \backslash G / K$ we have:
$$\int_{\Gamma \backslash G / K} B(\nabla \alpha, \nabla \alpha) d \mathrm{vol}=0 .$$
Since $\alpha$ is closed and coclosed, $\nabla \alpha$ is symmetric and has vanishing trace, thus formula (5.1) implies that $\alpha=0$; hence $\mathcal{H}^{1}(\Gamma \backslash G / K)=\{0\}$. Note that (5.1) is usually stated in the finite volume setting. But the extension to noncompact $\Gamma \backslash G / K$ presents no difficulties: if $\alpha$ is a $L^{2}$ harmonic 1-form on $\Gamma \backslash G / K$, it is easy to check that $\nabla \alpha$ is also $L^{2}$; thus, the integration by part procedure required to derive (5.1) can be justified by standard cut-off arguments.

Since our discussion clearly applies to any finite covering of $\Gamma \backslash G / K$, we finish the proof by employing Proposition 5.2 \(\square\)

Remark 5.11. Assume instead that $\Gamma \backslash G / K$ has finite volume. If we have also $\operatorname{rank}_{\mathbb{Q}} \Gamma \geq 2$, the Borel-Serre compactification of $\Gamma \backslash G / K$ implies that $\Gamma \backslash G / K$ has only one end.
5.4. The specific case of complex hyperbolic manifolds. Besides the result of Theorem 5.6 we have for complex hyperbolic manifolds the following statement.

Theorem 5.12. Let $\Gamma$ be a discrete and torsion-free subgroup of $S U(n, 1)$, with $n \geq 2$. Assume that the limit set $\Lambda(\Gamma)$ is not the whole sphere at infinity $\mathbb{S}^{2 n-1}$, that $\delta(\Gamma)<2 n$, and that the injectivity radius of $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ has a positive lower bound. Then $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ has only one end, and
$$H_{2 n-1}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}, \mathbb{Z}\right)=\{0\} .$$

Note that the hypotheses in this theorem are always satisfied in the convex cocompact setting.

Proof. By Theorem A the hypothesis $\delta(\Gamma)<2 n$ implies that $c=\lambda_{0}^{0}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right)>0$. Thus the following Poincaré inequality holds:
$$\forall f \in C_{0}^{\infty}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right), \quad c\|f\|_{L^{2}}^{2} \leq\|d f\|_{L^{2}}^{2} .$$
On the other hand, our assumption on the injectivity radius implies that the volume of geodesic balls of radius 1 is uniformly bounded from below. Since the Ricci curvature of $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ is constant, a result by N. Varopoulos (see Var, or Theorem 3.14 in [Heb]) asserts that, for some other constant $c^{\prime}>0$, we have the Sobolev inequality:
$$\forall f \in C_{0}^{\infty}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right), \quad c^{\prime}\|f\|_{L^{n /(n-1)}}^{2} \leq\|d f\|_{L^{2}}^{2}+\|f\|_{L^{2}}^{2} .$$
Gathering inequalities (5.2) and (5.3), we obtain the following Euclidian type Sobolev inequality: for some constant $c^{\prime \prime}>0$,
$$\forall f \in C_{0}^{\infty}\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right), \quad c^{\prime \prime}\|f\|_{L^{n /(n-1)}}^{2} \leq\|d f\|_{L^{2}}^{2} .$$

Next, suppose that there exists a compact set $C \subset \Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ such that $\left(\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}\right) \backslash C$ has at least two unbounded connected components, and let $\Omega$ be one of them. According to Theorem 2 in [CSZ], thanks to (5.4) we can find a harmonic function $u$ on $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$, which is valued in [0,1] and satisfies
$$\int_{\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}}|d u|^{2} d \mathrm{vol}<+\infty,$$
as well as
$$\lim _{\substack{m \rightarrow \infty \\ m \in \Omega}} u(m)=0 \text { and } \lim _{\substack{m \rightarrow \infty \\ m \notin \Omega}} u(m)=1 .$$
By Lemma 3.1 in Li , $u$ must be pluriharmonic. In particular, $u$ is harmonic on any complex submanifold of $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$.

Now, let $p \in \mathbb{S}^{2 n-1} \backslash \Lambda(\Gamma)$. Then there exists a neighbourhood $U$ of $p$ in $\mathbb{H}_{\mathbb{C}}^{n} \cup \mathbb{S}^{2 n-1}$, such that $U$ is mapped isometrically in $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ by the covering map $\pi: \mathbb{H}_{\mathbb{C}}^{n} \rightarrow \Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$. But we can find a holomorphic map $F: \mathbb{D} \rightarrow U$ such that $F(\partial \mathbb{D})=F(\mathbb{D}) \cap \mathbb{S}^{2 n-1}$. For instance, if $p=(1,0, \ldots, 0)$ then for some $\varepsilon>0$ small enough,
$$z \mapsto F(z)=\left(\sqrt{1-\varepsilon^{2}}, \varepsilon z, 0, \ldots, 0\right)$$
is such a map. So $u \circ \pi \circ F$ is a bounded harmonic function on $\mathbb{D}$, and takes a constant value on $\partial \mathbb{D}$ (0 or 1). Hence $u$ is constant on $\pi \circ F(\mathbb{D})$ and, by the Maximum Modulus Theorem, $u$ must be constant everywhere. This contradicts (5.5), so that $\Gamma \backslash \mathbb{H}_{\mathbb{C}}^{n}$ must have only one end.

The vanishing result follows again from Proposition 5.2 \(\square\)

Remark 5.13. Actually the proof of Theorem 5.12 extends to the case of any complete Kähler manifold containing a proper holomorphic disc and verifying the Sobolev estimate (5.4). We recover thus a result of J. Kohn and H. Rossi ([KR]) which asserts that a Kähler manifold which is pseudo-convex at infinity has only one end. There is a lot of literature which deals with the number of ends of complete Kähler manifolds, see for instance the references [LiR] and [NR].

As an immediate consequence of our last theorem, we can complement the result of Y. Shalom that we recovered in Corollary 5.8

Corollary 5.14. Assume that $\Gamma=A *_{C} B$ is a cocompact subgroup of $S U(n, 1)$ (with $n \geq 2$ ) which is a free product of subgroups $A$ and $B$ over an amalgamated subgroup $C$. Then either $2 n-1 \leq \delta(C)<2 n$ and $\Lambda(C)=\mathbb{S}^{2 n-1}$, or $\delta(C)=2 n$.

\section*{References}
\begin{itemize}
\item[] [Alb] P. Albuquerque, Patterson-Sullivan theory in higher rank symmetric spaces, Geom. Funct. Anal. 9 (1999), 1-28.
\item[] [AAR] G. E. Andrews, R. Askey and R. Roy, Special functions, Encyclopedia Math. Appl. 71. Cambridge Univ. Press, 1999.
\item[] [ADY] J.-Ph. Anker, E. Damek and C. Yacoub, Spherical analysis on harmonic AN groups, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 23 (1996), no. 4, 643-679.
\item[] [AJ] J.-Ph. Anker and L. Ji, Heat kernel and Green function estimates on noncompact symmetric spaces, Geom. Funct. Anal. 9 (1999), no. 6, 1035-1091.
\item[] [BCG1] G. Besson, G. Courtois and S. Gallot, Lemme de Schwarz réel et applications géométriques, Acta Math. 183 (1999), no. 2, 145-169.
\item[] [BCG2] \_\_\_\_, Hyperbolic manifolds, almagamated products and critical exponents, C. R. Math. Acad. Sci. Paris 336 (2003), no. 3, 257-261.
\item[] [Bor] A. Borel, The $L^{2}$-cohomology of negatively curved Riemannian symmetric spaces, Ann. Acad. Scient. Fenn. Series A.I. Math. 10 (1985), 95-105.
\item[] [BW] A. Borel and N. R. Wallach, Continuous Cohomology, Discrete Subgroups, and Representations of Reductive Groups, second ed., Math. Surveys Monogr. 67, Amer. Math. Soc., 2000.
\item[] [Bow] R. Bowen, Hausdorff dimension of quasicircles, Inst. Hautes Études Sci. Publ. Math. 50 (1979), 11-25.
\item[] [BOS] T. P. Branson, G. Ólafsson and H. Schlichtkrull, A bundle-valued Radon transform, with applications to invariant wave equations, Quart. J. Math. Oxford (2) 45 (1994), 429-461.
\item[] [BO1] U. Bunke and M. Olbrich, The spectrum of Kleinian manifolds, J. Funct. Anal. 172 (2000), 76-164.
\item[] [BO2] \_\_\_\_, Nonexistence of invariant distributions supported on the limit set, The 2000 Twente Conference on Lie groups (Enschede), Acta Appl. Math. 73 (2002), no. 1-2, 3-13.
\item[] [BO3] \_\_\_\_, Towards the trace formula for convex-cocompact groups, Preprint, 2000.
\item[] [CGH] D. M. J. Calderbank, P. Gauduchon and M. Herzlich, Refined Kato inequalities and conformal weights in Riemannian geometry, J. Funct. Anal. 173 (2000), 214-255.
\item[] [CSZ] H. D. Cao, Y. Shen and S. Zhu, The structure of stable minimal hypersurfaces in $\mathbb{R}^{n+1}$, Math. Res. Lett. 4 (1997), no. 5, 637-644.
\item[] [Car] G. Carron, Une suite exacte en $L^{2}$-cohomologie, Duke Math. J. 95 (1998), 343-372.
\item[] [CG] J. Cheeger and D. Gromoll, The splitting theorem for manifolds of nonnegative Ricci curvature, J. Differential Geom. 6 (1971-1972), 119-128.
\item[] [Col] Y. Colin de Verdière, Théorie spectrale des surfaces de Riemann d'aire infinie, In: Colloque en l'honneur de Laurent Schwartz (Palaiseau, 1983), Vol. 2, Astérisque 132, Soc. Math. France, 1985, pp. 259-275.
\item[] [CM] A. Connes and H. Moscovici, The $L^{2}$-index theorem for homogeneous spaces of Lie groups, Ann. of Math. (2) 115 (1982), 292-330.
\item[] [Cor] K. Corlette, Hausdorff dimensions of limit sets, Invent. Math. 102 (1990), no. 3, 521-541.
\item[] [Don] H. Donnelly, The differential form spectrum of hyperbolic space, Manuscripta Math. 33 (1981), 365-385.
\end{itemize}
\begin{itemize}
\item[] [DF] H. Donnelly and Ch. Fefferman, $L^{2}$-cohomology and index theorem for the Bergman metric, Ann. of Math. (2) 118 (1983), 593-618.
\item[] [Els] J. Elstrodt, Die Resolvente zum Eigenwertproblem der automorphen Formen in der hyperbolischen Ebene, Teil I. Math. Ann. 203 (1973), 295-330; Teil II. Math. Z. 132 (1973), 99-134; Teil III. Math. Ann. 208 (1974), 99-132.
\item[] [EMM] Ch. Epstein, R. Melrose and G. Mendoza, Resolvent of the Laplacian on strictly pseudoconvex domains, Acta Math. 167 (1991), no. 1-2, 1-106.
\item[] [Far] J. Faraut, Analyse harmonique sur les paires de Guelfand et les espaces hyperboliques, In: J. L. Clerc \& al. (eds), Analyse harmonique, Les cours du C.I.M.P.A., Nice, 1982, pp. 315-446.
\item[] [Fef] Ch. Fefferman, Monge-Ampère equations, the Bergman kernel, and geometry of pseudoconvex domains, Ann. of Math. (2) 103 (1976), no. 2, 395-416.
\item[] [GM] S. Gallot and D. Meyer, Opérateur de courbure et Laplacien des formes différentielles d'une variété riemannienne, J. Math. Pures Appl. (9) 54 (1975), no. 3, 259-284.
\item[] [HV] P. de la Harpe and A. Valette, La propriété $(T)$ de Kazhdan pour les groupes localement compacts (avec un appendice de Marc Burger), Astérisque 175, Soc. Math. France, 1989.
\item[] [Heb] E. Hebey, Sobolev spaces on Riemannian manifolds, Lecture Notes in Math. 1635, Springer, 1996.
\item[] [Hel] S. Helgason, Differential Geometry, Lie groups, and Symmetric Spaces, Academic Press, 1978.
\item[] [Ize] H. Izeki, Limit sets of Kleinian groups and conformally flat Riemannian manifolds, Invent. Math. 122 (1995), 603-625.
\item[] [IN] H. Izeki and S. Nayatani, Canonical metric on the domain of discontinuity of a Kleinian group, Sémin. Théor. Spectr. Géom. (Univ. Grenoble-I) 16 (1997-1998), 9-32.
\item[] [Kna] A. W. Knapp, Representation Theory of Semisimple Groups. An Overview Based on Examples, Princeton Math. Ser. 36, Princeton Univ. Press, 1986.
\item[] [KR] J. Kohn and H. Rossi, On the extension of holomorphic functions from the boundary of a complex manifold, Ann. of Math. (2) 81 (1965), 451-472.
\item[] [Leu] E. Leuzinger, Critical exponents of discrete groups and $L^{2}$-spectrum, Proc. Amer. Math. Soc. 132 (2004), no. 3, 919-927.
\item[] [Li] P. Li, On the structure of complete Kähler manifolds with nonnegative curvature near infinity, Invent. Math. 99 (1990), no. 3, 579-600.
\item[] [LiR] P. Li and M. Ramachandran, Kähler manifolds with almost nonnegative Ricci curvature, Amer. J. Math. 118 (1996), no. 2, 341-353.
\item[] [LiW] P. Li and J. Wang, Complete manifolds with positive spectrum, J. Differential Geom. 58 (2001), no. 3, 501-534.
\item[] [LM] J. Lee and R. Melrose, Boundary behaviour of the complex Monge-Ampère equation, Acta Math. 148 (1982), 159-192.
\item[] [Loh] N. Lohoué, Estimations asymptotiques des noyaux résolvants du laplacien des formes différentielles sur les espaces symétriques de rang un, de type non compact et applications, C. R. Acad. Sci. Paris Sér. I Math. 307 (1988), no. 11, 551-554.
\item[] [LR] N. Lohoué and Th. Rychener, Die Resolvente von $\Delta$ auf symmetrischen Räumen vom nichtkompakten Typ, Commun. Math. Helv. 57, (1982), 445-468.
\item[] [Lot] J. Lott, Heat kernels on covering spaces and topological invariants, J. Differential Geom. 35 (1992), 471-510.
\item[] [Maz] R. Mazzeo, The Hodge cohomology of a conformally compact metric, J. Differential Geom. 28 (1988), no. 2, 309-339.
\item[] [MM] R. Mazzeo and R. Melrose, Meromorphic extension of the resolvent on complete spaces with asymptotically constant negative curvature, J. Funct. Anal. 75 (1987), no. 2, 260-310.
\item[] [MP] R. Mazzeo and R. S. Phillips, Hodge theory on hyperbolic manifolds, Duke Math. J. 60 (1990), no. 2, 509-559.
\item[] [MW] R. Miatello and N. R. Wallach, The resolvent of the Laplacian on locally symmetric spaces, J. Differential Geom. 36 (1992), no. 3, 663-698.
\item[] [Mok] N. Mok, Harmonic forms with values in locally constant Hilbert bundles, Proceedings of the Conference in Honor of Jean-Piere Kahane (Orsay, 1993), J. Fourier Anal. Appl. special issue (1995), 433-453.
\end{itemize}
\begin{itemize}
\item[] [MSY] N. Mok, Y. T. Siu and S. K. Yeung, Geometric superrigidity, Invent. Math. 113 (1993), 57-83.
\item[] [Nay] S. Nayatani, Patterson-Sullivan measure and conformally flat metrics, Math. Z. 225 (1997), no. 1, 115-131.
\item[] [NR] T. Napier and M. Ramachandran, Structure theorems for complete Kähler manifolds and applications to Lefschetz type theorems, Geom. Funct. Anal. 5 (1995), no. 5, 809-851.
\item[] [Olb1] M. Olbrich, $L^{2}$-invariants of locally symmetric spaces, Doc. Math. 7 (2002), 219-237.
\item[] [Olb2] M. Olbrich, Cohomology of convex cocompact groups and invariant distributions on limit sets, Preprint, Universität Göttingen.
\item[] [OT] T. Ohsawa and K. Takegoshi, Hodge spectral sequence on pseudoconvex domains, Math. $Z .197$ (1988), no. 1, 1-12.
\item[] [Pan] P. Pansu, Formules de Matsushima, de Garmland et propriété (T) pour les groupes agissant sur des espaces symétriques ou des immeubles, Bull. Soc. Math. France 126 (1998), 107-139.
\item[] [Pat] S. J. Patterson, The limit set of a Fuchsian group, Acta Math. 136 (1976), 241-273.
\item[] [Ped1] E. Pedon, Analyse harmonique des formes différentielles sur l'espace hyperbolique réel, Thèse, Université de Nancy-I, 1997.
\item[] [Ped2] \_\_\_\_, Analyse harmonique des formes différentielles sur l'espace hyperbolique réel I. Transformation de Poisson et fonctions sphériques, C. R. Acad. Sci. Paris Sér. I Math., 326 (1998), 671-676.
\item[] [Ped3] \_\_\_\_, Harmonic analysis for differential forms on complex hyperbolic spaces, J. Geom. Phys. 32 (1999), 102-130.
\item[] [Ped4] \_\_\_\_, The differential form spectrum of quaternionic hyperbolic spaces, Preprint, Université de Reims, 2004. To appear in Bull. Sci. Math.
\item[] [Qui1] J.-F. Quint, Mesures de Patterson-Sullivan en rang supérieur, Geom. Funct. Anal. 12 (2002), 776-809.
\item[] [Qui2] \_\_\_\_, Divergence exponentielle des sous-groupes discrets en rang supérieur, Comment. Math. Helv. 77 (2002), 563-608.
\item[] [RS] M. Reed and B. Simon, Methods of Modern Mathematical Physics, Vol. IV, Analysis of Operators, Academic Press, 1979.
\item[] [Sha] Y. Shalom, Rigidity, unitary representations of semisimple groups, and fundamental groups of manifolds with rank one transformation group, Ann. of Math. (2) 152 (2000), no. 1, 113-182.
\item[] [SS] Z. Shen and C. Sormani, The codimension one homology of a complete manifold with nonnegative Ricci curvature, Amer. J. Math. 123 (2001), no. 3, 515-524.
\item[] [Sul1] D. Sullivan, The density at infinity of a discrete group of hyperbolic motions, Inst. Hautes Études Sci. Publ. Math. 50 (1979), 171-202.
\item[] [Sul2] \_\_\_\_, Related aspects of positivity in Riemannian geometry, J. Differential Geom. 25 (1987), 327-351.
\item[] [Var] N. Varopoulos, Small time Gaussian estimates of heat diffusion kernels I. The semi-group technique, Bull. Sci. Math. 113 (1989), 253-277.
\item[] [VZ] D. A. Vogan and G. J. Zuckerman, Unitary representations with non-zero cohomology, Compositio Math. 53 (1984), 51-90.
\item[] [Wal] N. R. Wallach, Harmonic Analysis on Homogeneous Spaces, Dekker, 1973.
\item[] [Wan1] X. Wang, On conformally compact Einstein manifolds, Math. Res. Lett. 8 (2001), no. 5-6, 671-688.
\item[] [Wan2] \_\_\_\_, On the $L^{2}$-cohomology of a convex cocompact hyperbolic manifold, Duke Math. J. 115 (2002), no. 2, 311-327.
\item[] [Yeg] N. Yeganefar, Sur la $L^{2}$-cohomologie des variétés à courbure négative, Duke Math. J. 122 (2004), no. 1, 145-180.
\item[] [Yue] C. Yue, The ergodic theory of discrete isometry groups on manifolds of variable negative curvature, Trans. Amer. Math. Soc. 348 (1996), no. 12, 4965-5005.
\end{itemize}

Laboratoire de Mathématiques Jean Leray (UMR 6629), Université de Nantes, 2, rue de la Houssinière, B.P. 92208, 44322 Nantes Cedex 3, France
E-mail address: Gilles.Carron@math.univ-nantes.fr
Laboratoire de Mathématiques (UMR 6056), Université de Reims, Moulin de la Housse, B.P. 1039, 51687 Reims Cedex 2, France
E-mail address: emmanuel.pedon@univ-reims.fr
