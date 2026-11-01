# Curvature, Connected Sums, and Seiberg-Witten Theory

- Category: papers
- Identity: doi:10.4310/cag.2003.v11.n5.a1
- Content status: fulltext_ok

---

---
source_file: Curvature__Connected_Sums__and_Seiberg-Witten_Theory_602843790d6f.pdf
converter: mathpix
format: mmd
---

\title{
Curvature, Connected Sums, and Seiberg-Witten Theory
}

\author{
Masashi Ishida and Claude LeBrun ${ }^{1}$
}

\begin{abstract}
We consider several differential-topological invariants of compact 4-manifolds which directly arise from Riemannian variational problems. Using recent results of Bauer and Furuta [5, 4], we compute these invariants in many cases that were previously intractable. In particular, we are now able to calculate the Yamabe invariant for many connected sums of complex surfaces.
\end{abstract}

\section*{1. Introduction.}

Given a smooth compact $n$-dimensional manifold $M$, the canonical metric problem [6] would ask us to geometrize $M$ by somehow endowing it with a preferred Riemannian metric. In practice, this usually amounts to trying to find a critical point for some natural curvature functional on the space of all Riemannian metrics. While few such efforts seem destined to succeed, they often nevertheless lead to interesting diffeomorphism invariants of compact manifolds. A prototypical example of such an invariant, called the Yamabe invariant or sigma constant, historically arose from an attempt to construct Einstein metrics on manifolds of dimension $n>2$.

Einstein metrics (i.e. metrics of constant Ricci curvature) are precisely [7] the critical points of the normalized total scalar curvature
$$\mathfrak{S}(g)=V_{g}^{(2-n) / n} \int_{M} s_{g} d \mu_{g}$$
considered as a functional with domain the space of Riemannian metrics $g$ on a given smooth compact manifold $M$ of dimension $n>2$; here $s=R^{j k}{ }_{j k}$ denotes the scalar curvature, $d \mu$ is the Riemannian volume measure, and $V=\int_{M} d \mu$ is the total volume of $M$ with respect to the relevant metric. Unfortunately, one cannot hope to construct an Einstein metric on $M$ by minimizing or maximizing $\mathfrak{S}$, as the functional is neither bounded above nor

\footnotetext{
${ }^{1}$ Supported in part by NSF grant DMS-0072591.
}
bounded below. However, as was first pointed out by H. Yamabe [37], the restriction of $\mathfrak{S}$ to any conformal class
$$\gamma=[g]=\left\{u g \mid u: M \xrightarrow{C^{\infty}} \mathbb{R}^{+}\right\}$$
of metrics is always bounded below, and Yamabe therefore hoped to construct Einstein metrics by instead first minimizing $\mathfrak{S}$ in each conformal class, and then maximizing over the set of all conformal classes. While this certainly fails in general, it nevertheless yields a real-valued diffeomorphism invariant [18, 32]
$$\mathcal{Y}(M)=\sup _{\gamma} \inf _{g \in \gamma} \mathfrak{S}(g),$$
called the Yamabe invariant of the smooth compact manifold $M$. It is not hard to show that $\mathcal{Y}(M)>0$ if and only if $M$ admits a metric of positive scalar curvature; thus, the problem of computing the Yamabe invariant may be thought of as a quantitative refinement of the question of whether a given manifold admits positive-scalar-curvature metrics.

Until recently, however, the only available non-trivial exact computations of the Yamabe invariant concerned the underlying 4-manifolds of complex algebraic surfaces [25, 26], or their connected sums [29] with copies of $S^{1} \times S^{3}$. Our primary objective in the present article is to remedy this dearth of knowledge, by proving the following result:

Theorem A. Let $X_{j}, j=1, \ldots, 4$, be minimal complex surfaces with
$$\begin{aligned}
b_{1}\left(X_{j}\right) & =0 \\
b_{+}\left(X_{j}\right) & \equiv 3 \bmod 4 \\
\sum_{j=1}^{4} b_{+}\left(X_{j}\right) & \equiv 4 \bmod 8
\end{aligned}$$
Let $N$ be any smooth, compact orientable 4-manifold with $b_{+}(N)=0$ which admits a metric of scalar curvature $\geq 0$. Then, for each $m=1, \ldots, 4$,
$$\mathcal{Y}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right)=-4 \pi \sqrt{2 \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)} .$$

Here \# denotes the connected sum operation, which is carried out by removing standard balls, and gluing along the resulting boundaries. The most important single ingredient in the proof is a recent breakthrough in Seiberg-Witten theory due to Bauer and Furuta [5, 4].

The Yamabe invariant $\mathcal{Y}(M)$ is closely related to the diffeomorphism invariant defined [8, 27] by
$$\mathcal{I}_{s}(M)=\inf _{g} \int_{M}\left|s_{g}\right|^{n / 2} d \mu_{g}$$
where the infimum is taken over all Riemannian metrics on $M$, and where $s$ and $d \mu$ once again respectively denote the scalar curvature and the Riemannian volume measure; cf. Proposition 12 below. By definition, $\mathcal{I}_{s}$ is thus a quantitative obstruction to the existence of scalar-flat metrics. The power of $n / 2$ is dictated by the need for scale invariance: for trivial reasons, any other choice would yield the zero invariant. But, even with this careful choice, it is hardly obvious that the above invariant is non-trivial; and indeed, Petean [30], building upon the earlier work of Gromov-Lawson [14] and Stolz [33], has proved that $\mathcal{I}_{s}$ vanishes for every simply connected $n$-manifold with $n \geq 5$. Dimension four, however, turns out to be quite exceptional for questions concerning the scalar curvature, and Seiberg-Witten theory [36] turns out to predict that $\mathcal{I}_{s}$ is non-zero for many simply connected 4-manifolds. Indeed, in proving Theorem A we will simultaneously prove the following:

Theorem B. Let $X_{j}, j=1, \ldots, 4$ and $N$ be as in Theorem A. Then, for each $m=1, \ldots, 4$,
$$\mathcal{I}_{s}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right)=\mathcal{I}_{s}\left(\#_{j=1}^{m} X_{j}\right)=32 \pi^{2} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$

Example. Let $X$ be the ramified double cover of $\mathbb{C P}_{2}$, with branch locus a smooth complex curve of degree 8. Then the canonical class of $X$ is the pull-back of the hyperplane class from $\mathbb{C P}_{2}$, and it therefore follows that $p_{g}(X)=3$ and $c_{1}^{2}(X)=2$. In particular, $b_{+}(X)=7 \equiv 3 \bmod 4$, so we have
$$\mathcal{Y}(X \# X)=-4 \pi \sqrt{2(2+2)}=-8 \pi \sqrt{2}$$
and
$$\mathcal{I}_{s}(X \# X)=32 \pi^{2}(2+2)=128 \pi^{2} .$$

By contrast, consider the connected sum $X \nexists \bar{X}$, where $\bar{X}$ denotes $X$ with the reverse orientation. Because $X$ was constructed as a branched cover of $\mathbb{C P}_{2}$, it has a handle decomposition without 1- or 3-handles, and the non-spin 4 -manifold $X \nexists \bar{X}$ consequently dissolves [13, Cor. 6.3.19 \& Prop. 9.1.16]:
$$X \# \bar{X} \stackrel{\text { diff }}{\approx} 44 \mathbb{C P}_{2} \# 44 \overline{\mathbb{C P}}_{2} .$$

In particular, $X \nexists \bar{X}$ admits metrics of positive scalar curvature, and so, by Proposition 12 below,
$$\mathcal{I}_{s}(X \# \bar{X})=0 .$$
We can also estimate $\mathcal{Y}(X \# \bar{X})$ on the basis of this picture, although current techniques do not lend themselves to an exact calculation of this number. Indeed, $\mathcal{Y}\left(\mathbb{C P}_{2}\right)=\mathcal{Y}\left(\overline{\mathbb{C P}}_{2}\right)>0$, so that O . Kobayashi's estimate [18] of the Yamabe invariant of a connected sum tells us that
$$\mathcal{Y}\left(S^{4}\right) \geq \mathcal{Y}\left(k \mathbb{C P}_{2} \# \ell \overline{\mathbb{C P}}_{2}\right) \geq \mathcal{Y}\left(\mathbb{C P}_{2}\right),$$
and we therefore see that
$$\mathcal{Y}(X \# \bar{X}) \in[12 \pi \sqrt{2}, 8 \pi \sqrt{6}] .$$
This vividly illustrates the point that $\mathcal{Y}$ and $\mathcal{I}_{s}$ are remarkably sensitive to the relative orientation of the summands in a connected sum! \(\square\)

Of course, curvature comes in many different flavors, and so it is equally natural to consider invariants such as
$$\mathcal{I}_{r}(M)=\inf _{g} \int_{M}|r|_{g}^{n / 2} d \mu_{g}$$
where $r$ denotes the Ricci tensor, and where, once again, $n=\operatorname{dim} M$. It is easy to show that there is a tautological inequality
$$\mathcal{I}_{r}(M) \geq n^{-n / 4} \mathcal{I}_{s}(M),$$
and that equality holds if the Yamabe invariant $\mathcal{Y}(M)$ is both non-positive and realized by an Einstein metric; the failure of equality would thus give a quantitative obstruction to Yamabe's program for finding Einstein metrics. It is therefore interesting to observe that the inequality (6) is often strict in dimension 4. Indeed, we are able to prove:

Theorem C. Let $X_{j}, j=1, \ldots, 4$ be minimal complex surfaces satisfying (1-3). Let $N$ be a smooth compact oriented 4-manifold which admits an anti-self-dual metric of positive scalar curvature. Then, for each choice of $m=1, \ldots, 4$,
$$\mathcal{I}_{r}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right)=8 \pi^{2}\left[4 m-(2 \chi+3 \tau)(N)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)\right]$$

Here, as throughout, $\chi$ and $\tau$ respectively denote the signature and Euler characteristic of an oriented 4-manifold. Note that the above hypotheses regarding $N$ imply that $b_{+}(N)=0$, and hence that $(2 \chi+3 \tau)(N) \leq 4$. In particular, the Yamabe sup-inf on these manifolds is never realized by an Einstein metric if $m>1$.

Example. Let $X$ once again be the ramified double cover of $\mathbb{C P}_{2}$ branched over a smooth octic. Then
$$\begin{aligned}
\mathcal{I}_{r}(X \# X) & =\mathcal{I}_{r}\left(X \# X \# S^{4}\right) \\
& =8 \pi^{2}\left[4 \cdot 2-(2 \chi+3 \tau)\left(S^{4}\right)+c_{1}^{2}(X)+c_{1}^{2}(X)\right] \\
& =8 \pi^{2}[4 \cdot 2-4+2+2] \\
& =64 \pi^{2} .
\end{aligned}$$
On the other hand, we have already seen that
$$\mathcal{I}_{s}(X \# X)=128 \pi^{2},$$
so that
$$\mathcal{I}_{r}(X \# X)-\frac{1}{4} \mathcal{I}_{s}(X \# X)=32 \pi^{2}$$
This gap measures the limiting size of the trace-free part of the Ricci tensor as one approaches the Yamabe sup-inf. Roughly speaking, the gap arises because the geometry is trying to break apart into two copies of the Kähler-Einstein metric on $X$, but, as this happens, a substantial amount of trace-free Ricci curvature accumulates in the neck joining the two copies of $X$. \(\square\)

The same techniques used to prove this result also have a number of other geometrical ramifications. Of these, we will highlight the following:

Theorem D. Let $X_{j}, j=1, \ldots, 4$ be smooth, compact almost-complex 4-manifolds for which the mod-2 Seiberg-Witten invariant is non-zero, and suppose, moreover, that (1-3) hold. Let $N$ be any oriented 4-manifold with $b_{+}=0$. Then, for any $m=2,3$ or 4, the smooth 4-manifold $\left[\#_{j=1}^{m} X_{j}\right] \# N$ does not admit Einstein metrics if
$$12(m-1)+\left(12 b_{1}+3 b_{-}\right)(N) \geq \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$

This generalizes the key technical result of [16].

\section*{2. The Seiberg-Witten Equations.}

If $M$ is a smooth oriented 4-manifold, there always exist Hermitian line bundles $L \rightarrow M$ such that $c_{1}(L) \equiv w_{2}(T M) \bmod 2$. For any such $L$, and any Riemannian metric $g$ on $M$, one can then find rank-2 Hermitian vector bundles $\mathbb{V}_{ \pm}$which formally satisfy
$$\mathbb{V}_{ \pm}=\mathbb{S}_{ \pm} \otimes L^{1 / 2},$$
where $\mathbb{S}_{ \pm}$are the locally defined left- and right-handed spinor bundles of $(M, g)$. Such a choice of $\mathbb{V}_{ \pm}$, up to isomorphism, is called a spin ${ }^{c}$ structure $\mathfrak{c}$ on $M$, and is determined, modulo the 2-torsion subgroup of $H_{1}(M, \mathbb{Z})$, by the first Chern class $c_{1}(L)=c_{1}\left(\mathbb{V}_{ \pm}\right) \in H^{2}(M, \mathbb{Z})$ of the spin ${ }^{c}$ structure. Every unitary connection $A$ on $L$ induces a Dirac operator
$$D_{A}: \Gamma\left(\mathbb{V}_{+}\right) \rightarrow \Gamma\left(\mathbb{V}_{-}\right) .$$
If $A$ is such a connection, and if $\Phi$ is a section of $\mathbb{V}_{+}$, the pair $(\Phi, A)$ is said to satisfy the Seiberg-Witten equations [36] if
$$\begin{aligned}
D_{A} \Phi & =0 \\
F_{A}^{+} & =i \sigma(\Phi),
\end{aligned}$$
were $F_{A}^{+}$is the self-dual part of the curvature of $A$, and where $\sigma: \mathbb{V}_{+} \rightarrow \Lambda^{+}$ is a real-quadratic map arising from the isomorphism $\Lambda^{+} \otimes \mathbb{C}=\odot^{2} \mathbb{S}_{+}$.

For the 4 -manifolds of primary interest here, there turn out to be certain spin ${ }^{c}$ structures for which there exists a solution of the Seiberg-Witten equations for each metric $g$. This situation is neatly codified by the following terminology, first introduced by Kronheimer [21]:

Definition 1. Let $M$ be a smooth compact oriented 4-manifold with $b_{+} \geq$ 2. An element $a \in H^{2}(M, \mathbb{Z})$ /torsion will be called a monopole class of $M$ iff there exists a spin ${ }^{c}$ structure $\mathfrak{c}$ on $M$ with
$$c_{1}^{\mathbb{R}}(L)=a$$
which has the property that the corresponding Seiberg-Witten equations (7-8) have a solution for every Riemannian metric $g$ on $M$. Here $c_{1}^{\mathbb{R}}(L)$ denotes the image of the first Chern class $c_{1}(L)$ of the anti-canonical line bundle of $\mathfrak{c}$ in $H^{2}(M, \mathbb{Z})$ /torsion $\subset H^{2}(M, \mathbb{R})$.

As was first pointed out by Witten [36], the existence of a monopole class implies an a priori lower bound on the $L^{2}$ norm of the scalar curvature of Riemannian metrics. The sharp form of this estimate reads as follows [24]:

Proposition 2. Let $M$ be a smooth compact oriented 4-manifold with monopole class $a \in H^{2}(M, \mathbb{Z}) /$ torsion $\subset H^{2}(M, \mathbb{R})$. If $a \neq 0$, then $M$ does not admit metrics of positive scalar curvature. Moreover, if $g$ is any Riemannian metric on $M$, and if $a^{+} \in H^{2}(M, \mathbb{R})$ denotes the self-dual part of a with respect to the decomposition
$$\mathcal{H}_{g}^{2}=\mathcal{H}_{g}^{+} \oplus \mathcal{H}_{g}^{-}$$
of the space of $g$-harmonic 2-forms into eigenspaces of the ★ operator, then the scalar curvature $s$ of $g$ satisfies
$$\int_{M} s^{2} d \mu \geq 32 \pi^{2}\left(a^{+}\right)^{2}$$
where $d \mu$ denotes the Riemannian volume form of $g$. Finally, the inequality is always strict unless $M$ admits a complex structure of Kähler type, with first Chern class $a$.

One important formal consequence is the following; cf. [16].
Proposition 3. Let $M$ be any smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$. Then $\mathcal{C}=\{$ monopole classes of $M\}$ is a finite set.

Proof. Let $g_{1}=g$ be any Riemannian metric on $M$, and let $\mathbf{e}_{1}=\left[\alpha_{1}\right]$ be the cohomology class of a harmonic self-dual form with respect to $g$, normalized so that $\mathbf{e}_{1}^{2}:=\left[\alpha_{1}\right] \cdot\left[\alpha_{1}\right]=1$. Now the local surjectivity of the period map $\left[11\right.$, Prop. 4.3.14] asserts that $\left[\alpha_{1}\right]$ has a neighbohood in $H^{2}(M, \mathbb{R})$ in which every element can be represented by a self-dual harmonic form for some perturbation of $g$. But any open set in a finite-dimensional vector space spans the space. Thus we can find a basis $\left\{\mathbf{e}_{j}=\left[\alpha_{j}\right] \mid j=1, \ldots, b_{2}(M)\right\}$ for $H^{2}(M, \mathbb{R})$ and a collection of Riemannian metrics $\left\{g_{j} \mid j=1, \ldots, b_{2}(M)\right\}$ such that the harmonic representative $\alpha_{j}$ of $\mathbf{e}_{j}$ with respect to $g_{j}$ is self-dual. For convenience, we normalize these basis elements so that $\mathbf{e}_{j}^{2}=1$ for each $j$. Let $L_{j}: H^{2}(M, \mathbb{R}) \rightarrow \mathbb{R}$ denote the linear functionals $L_{j}(x)=\mathbf{e}_{j} \cdot x$, and now notice that Proposition 2, together with the Cauchy-Schwarz inequality, tells us that any monopole class $a \in H^{2}(M, \mathbb{Z})$ /torsion satisfies
$$\left|L_{j}(a)\right|=\left|\left[\alpha_{j}\right] \cdot a_{g_{j}}^{+}\right| \leq \sqrt{\left(a_{g_{j}}^{+}\right)^{2}} \leq\left(\int_{M} s_{g_{j}}^{2} d \mu_{g_{j}}\right)^{1 / 2}=\varrho_{j},$$
where the constant $\varrho_{j}$ is independent of $a$. This shows that $\mathcal{C} \subset H^{2}(M, \mathbb{R})$ is contained in the $b_{2}(M)$-dimensional parallelepiped
$$\left\{x \in H^{2}(M, \mathbb{R})| | L_{j}(x) \mid \leq \varrho_{j} \forall j=1, \ldots, b_{2}(M)\right\},$$
which, while geometrically wide and flat, is nonetheless a compact set. Since $\mathcal{C} \subset H^{2}(M, \mathbb{Z})$ /torsion is also discrete, it follows that $\mathcal{C}$ is finite. \(\square\)

More recently, the second author discovered that equations (7-8) also imply a family of estimates involving the self-dual Weyl curvature [27]:

Proposition 4 (LeBrun). Let $M$ be a smooth compact oriented 4manifold with monopole class $a$, and let $g$ be any Riemannian metric on $M$. Then the scalar curvature $s$ and self-dual Weyl curvature $W_{+}$of $g$ satisfy
$$\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu \geq 72 \pi^{2}\left(a^{+}\right)^{2}$$
where $d \mu$ denotes the Riemannian volume form of $g$, and where the pointwise norms are calculated with respect to $g$. Moreover, the inequality is always strict unless $M$ admits a symplectic structure with first Chern class $a$.

We remark in passing that one can actually say a great deal more about the borderline cases of the above inequalities. Indeed, the inequality of Proposition 2 is only saturated by constant-scalar-curvature Kähler metrics [24], whereas the inequality of Proposition 4 is only saturated by a class of almost-Kähler metrics with extremely special curvature properties [27]. However, the weaker statements given above will be quite sufficient for the purposes of the present article.

\section*{3. The Bauer-Furuta Invariant.}

Bauer and Furuta [5, 4] recently introduced a remarkable new method for detecting monopole classes. The crux of their theory is the definition of a generalized Seiberg-Witten invariant which takes values in an equivariant stable cohomotopy group. As a courtesy to the reader, we therefore begin with a brief introduction to the relevant homotopy-theoretic machinery.

If $(\mathfrak{X}, x)$ is any finite cell complex with base point, its suspension $\Sigma \mathfrak{X}=\Sigma^{1} \mathfrak{X}$ is just the one-point compactification of $(\mathfrak{X}-\{x\}) \times \mathbb{R}$, equipped with base point $\infty$. Setting $\Sigma^{n} \mathfrak{X}=\Sigma\left(\Sigma^{n-1} \mathfrak{X}\right)$ for $n>1$, one immediately sees that $\Sigma^{n} \mathfrak{X}$ is similarly the one-point compactification of $(\mathfrak{X}-\{x\}) \times \mathbb{R}^{n}$. Now if $(\mathfrak{Y}, y)$ is any other pointed finite cell complex, then the set $\left[\Sigma^{n} \mathfrak{X}, \mathfrak{Y}\right]$ of based homotopy classes of maps $\Sigma^{n} \mathfrak{X} \rightarrow \mathfrak{Y}$ can be identified with $\pi_{n}(\{$ based maps $\mathfrak{X} \rightarrow \mathfrak{Y}\})$, and so is an Abelian group if $n \geq 2$. There is a
natural homomorphism $\left[\Sigma^{n} \mathfrak{X}, \Sigma^{n} \mathfrak{Y}\right] \rightarrow\left[\Sigma^{n+1} \mathfrak{X}, \Sigma^{n+1} \mathfrak{Y}\right]$, induced by Cartesian products with the identity $\mathbb{R} \rightarrow \mathbb{R}$. If $n$ is large with respect to the dimensions of $\mathfrak{X}$ and $\mathfrak{Y}$, then this homomorphism turns out to be an isomorphism. In particular, we may define the $m^{\text {th }}$ stable cohomotopy group of $\mathfrak{X}$ by
$$\pi^{m}(\mathfrak{X})=\lim _{n \rightarrow \infty}\left[\Sigma^{n} \mathfrak{X}, \Sigma^{n} S^{m}\right]=\lim _{n \rightarrow \infty}\left[\Sigma^{n} \mathfrak{X}, S^{m+n}\right] .$$

The Bauer-Furuta construction also involves $S^{1}$-equivariant analogs of these groups. Suppose that $\mathfrak{X}$ is equipped with an $S^{1}$-action leaving the base point $x$ fixed. Then we may equip $\Sigma^{3 n} \mathfrak{X}$ with an $S^{1}$-action by choosing to view it as the one-point compactification of $(\mathfrak{X}-\{x\}) \times \mathbb{C}^{n} \times \mathbb{R}^{n}$, and letting $S^{1} \subset \mathbb{C}^{\times}$act on the $\mathbb{C}^{n}$ factor by scalar multiplication. If $(\mathfrak{Y}, y)$ is another complex with $S^{1}$-action, then the set $\left[\Sigma^{3 n} \mathfrak{X}, \mathfrak{Y}\right]_{S^{1}}$ of based homotopy classes of $S^{1}$-equivariant maps $\Sigma^{3 n} \mathfrak{X} \rightarrow \mathfrak{Y}$ can be identified with $\pi_{n}\left(\left\{\right.\right.$ based $S^{1}$-equivariant maps $\left.\left.\Sigma^{2 n} \mathfrak{X} \rightarrow \mathfrak{Y}\right\}\right)$, and so is an Abelian group whenever $n \geq 2$. We again have natural homomorphisms $\left[\Sigma^{3 n} \mathfrak{X}, \Sigma^{3 n} \mathfrak{Y}\right]_{S^{1}} \rightarrow$ $\left[\Sigma^{3(n+1)} \mathfrak{X}, \Sigma^{3(n+1)} \mathfrak{Y}\right]_{S^{1}}$, and these homomorphisms are again isomorphisms for $n$ sufficiently large. The $S^{1}$-equivariant cohomotopy groups of $\mathfrak{X}$ used in the Bauer-Furuta construction are then given by
$$\pi_{S^{1}}^{m}(\mathfrak{X})=\lim _{n \rightarrow \infty}\left[\Sigma^{3 n} \mathfrak{X}, \Sigma^{3 n} S^{m}\right]_{S^{1}}=\lim _{n \rightarrow \infty}\left[\Sigma^{3 n} \mathfrak{X}, S^{m+3 n}\right]_{S^{1}},$$
where $S^{1}$ acts on $\mathfrak{X}$ in the given manner, and acts trivially on $S^{m}$. In particular, if $\mathbb{E}^{+}=\mathbb{E} \cup\{\infty\}$ is the Thom space of a complex vector bundle $\mathbb{E} \rightarrow B$ over a compact base, $S^{1}$ will be understood to act on $\mathbb{E}$ by fiber-wise complex multiplication, and
$$\begin{aligned}
& \pi_{S^{1}}^{m}\left(\mathbb{E}^{+}\right)=\pi_{0}\left(\left\{S^{1}\right.\right. \text {-equivariant maps } \\
& \left.\left.\qquad\left(\mathbb{E} \oplus \mathbb{C}^{n} \oplus \mathbb{R}^{n}\right)^{+} \rightarrow\left(\mathbb{C}^{n} \times \mathbb{R}^{m+n}\right) \cup\{\infty\}\right\}\right)
\end{aligned}$$
for $n$ sufficiently large. Notice that this only depends on the stable equivalence class of $\mathbb{E}$, rather than $\mathbb{E}$ itself. In particular, if $\mathbb{E}$ is merely specified by an element of $K^{0}(B)$, we can still define the group in question by representing the virtual bundle $\mathbb{E}$ as the formal difference $\mathbb{F} \ominus \mathbb{C}^{\ell}$ of a complex vector bundle and a trivial bundle, and then taking
$$\begin{aligned}
& \pi_{S^{1}}^{m}\left(\mathbb{E}^{+}\right)=\pi_{0}\left(\left\{S^{1}\right.\right. \text {-equivariant maps } \\
& \left.\left.\qquad\left(\mathbb{F} \oplus \mathbb{C}^{n-\ell} \oplus \mathbb{R}^{n}\right)^{+} \rightarrow\left(\mathbb{C}^{n} \times \mathbb{R}^{m+n}\right) \cup\{\infty\}\right\}\right)
\end{aligned}$$
for $n$ sufficiently large.

Bauer and Furuta [5] observe that one can associate stable cohomotopy classes with sufficiently nice maps between Hilbert spaces. Indeed, let
$$\mathcal{L}: \mathcal{H}_{1} \rightarrow \mathcal{H}_{2}$$
be a Fredholm linear map between real Hilbert spaces, and let
$$\mathcal{F}: \mathcal{H}_{1} \rightarrow \mathcal{H}_{2}$$
be a continuous map of the form
$$\mathcal{F}=\mathcal{L}+\mathcal{K},$$
where $\mathcal{K}$ is a compact (non-linear) operator. Assume, in addition, that $\mathcal{F}$ satisfies the following boundedness condition:
the inverse image of any bounded set is bounded.
The boundedness condition allows us to extend $\mathcal{F}$ to a continuous map
$$\mathcal{F}^{+}=\mathcal{H}_{1}^{+} \rightarrow \mathcal{H}_{2}^{+}$$
where $\mathcal{H}_{j}^{+}=\mathcal{H}_{j} \cup\{\infty\}$ is identified with the unit sphere in $S\left(\mathcal{H}_{j} \oplus \mathbb{R}\right) \subset$ $\mathcal{H}_{j} \oplus \mathbb{R}$ via stereographic projection.

Now given any finite-dimensional subspace $\mathbf{W} \subset \mathcal{H}_{2}$ with coker $\mathcal{L} \subset \mathbf{W}$, consider corresponding finite-dimensional subspace $\mathbf{V}:=\mathcal{L}^{-1}(\mathbf{W}) \subset \mathcal{H}_{1}$. We will then say that $\mathbf{W}$ is a good subspace if $\mathcal{F}(\mathbf{V})$ does not intersect the unit sphere $S\left(\mathbf{W}^{\perp}\right) \subset \mathbf{W}^{\perp}$. For any good subspace W we thus have a map $\left.\operatorname{pr}_{\mathbf{W}} \circ \mathcal{F}^{+}\right|_{\mathbf{V}^{+}}: \mathbf{V}^{+} \rightarrow \mathbf{W}^{+}$between finite-dimensional spheres, where the deformation retraction $\mathrm{pr}_{\mathbf{W}}: \mathcal{H}_{2}^{+}-S\left(\mathbf{W}^{\perp}\right) \rightarrow \mathbf{W}^{+}$corresponds, via stereographic projection, to the map $S\left(\mathcal{H}_{2} \oplus \mathbb{R}\right)-S\left(\mathbf{W}^{\perp}\right) \rightarrow S(\mathbf{W} \oplus \mathbb{R})$ given by $v \rightarrow v^{\|} /\left|v^{\|}\right|$, where $v^{\|}$is the orthogonal projection of $v$ into $\mathbf{W} \oplus \mathbb{R}$. It turns out that any finite-dimensional subspace of $\mathcal{H}_{2}$ is a proper subspace of some good subspace, and we can thus define a stable cohomotopy class $[\mathcal{F}] \in \pi^{-\operatorname{ind}(\mathcal{L})}\left(S^{0}\right)$ by taking the limit of this construction over a nested sequence $\mathbf{W}_{1} \subset \mathbf{W}_{2} \subset \mathbf{W}_{3} \subset \cdots$ of good subspaces. In fact, the cohomotopy classes constructed from the individual $\mathbf{W}_{j}$ all agree with one another for sufficiently large $j$. Moreover, $[\mathcal{F}]$ is independent of all the choices made in its construction.

The equivariant version of the construction is similar. Suppose that $\mathcal{L}$ is the direct sum $\mathfrak{L}_{\mathbb{C}} \oplus \mathfrak{L}_{\mathbb{R}}$ of a complex-linear Fredholm map $\mathfrak{L}_{\mathbb{C}}$ between complex Hilbert spaces and a real linear Fredholm map $\mathfrak{L}_{\mathbb{R}}$ between real

Hilbert spaces. Also assume that $\mathcal{F}$ is an $S^{1}$-equivariant map. Then the same procedure gives us an equivariant cohomotopy class $[\mathcal{F}] \in \pi_{S^{1}}^{3}\left(\mathbb{C}^{2} \cup\{\infty\}\right)$, where $\imath=\operatorname{ind}_{\mathbb{C}} \mathfrak{L}_{\mathbb{C}}$ and $\jmath=-\operatorname{ind}_{\mathbb{R}} \mathfrak{L}_{\mathbb{R}}$.

If we replace $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ with real Hilbert-space bundles over a finite cell complex $B$, and allow $\mathcal{L}$ to be a Fredholm morphism of Hilbert bundles, then much the same construction still applies. Indeed, we can always find a trivialization $\mathcal{H}_{2} \cong B \times \mathcal{H}$ so that there is a fixed finite-dimensional subspace $\mathbf{W}_{0} \subset \mathcal{H}$ with coker $\mathcal{L}_{x} \subset \mathbf{W}_{0}$ for every $x \in B$. A finite-dimensional subspace $\mathbf{W} \supset \mathbf{W}_{0}$ is then said to be good if $\mathcal{F}(\mathbf{V})$ avoids the unit sphere in $\mathbf{W}^{\perp}$, where $\mathbf{V}=\mathcal{L}^{-1}(\mathbf{W})$ is now a bundle. For each good subspace $\mathbf{W}$, the map $\left.\operatorname{pr}_{\mathbf{W}} \circ \mathcal{F}^{+}\right|_{\mathbf{V}^{+}}: \mathbf{V}^{+} \rightarrow \mathbf{W}^{+}$determines an element of $\pi^{0}\left(\mathbb{E}^{+}\right)$, where $\mathbb{E}=\mathbf{V} \ominus \mathbf{W}$ is the virtual index of $\mathcal{L}$ in $K O^{0}(B)$, and $\mathbb{E}^{+}$is its Thom space. It once again turns out that any finite-dimensional subspace of $\mathcal{H}$ is a proper subspace of a good subspace, so we may take the limit over a nested sequence $\mathbf{W}_{1} \subset \mathbf{W}_{2} \subset \mathbf{W}_{3} \subset \cdots$ of good subspaces to define the stable cohomotopy class $[\mathcal{F}] \in \pi^{0}\left(\mathbb{E}^{+}\right)$, and one can then show that this class is independent of all choices made along the way.

Similarly, there is an $S^{1}$-equivariant version of this story. The relevant special case goes as follows: suppose that $\mathcal{H}_{1}$ and $\mathcal{H}_{2}$ are each direct sums of complex Hilbert-space bundles over $B$ and real Hilbert-space bundles. Suppose also that $\mathcal{L}$ decomposes as $\mathfrak{L}_{\mathbb{C}} \oplus \mathfrak{L}_{\mathbb{R}}$, where $\mathfrak{L}_{\mathbb{C}}$ is a complex-linear Fredholm morphism, and $\mathfrak{L}_{\mathbb{R}}$ is a Fredholm linear map between real Hilbert spaces. Then if $\mathcal{F}=\mathcal{L}+\mathcal{K}$ is $S^{1}$-equivariant and satisfies the boundedness condition, with $\mathcal{K}$ is compact, then the previous construction, carried out $S^{1}$-equivariantly, gives us a stable cohomotopy class $[\mathcal{F}] \in \pi_{S^{1}}^{\jmath}\left(\mathbb{E}^{+}\right)$, where $\mathbb{E} \in K^{0}(B)$ is the virtual index bundle of $\mathcal{L}, \mathbb{E}^{+}$is its Thom space, and $\jmath=-\operatorname{ind}_{\mathbb{R}} \mathfrak{L}_{\mathbb{R}}$.

We now describe how Bauer and Furuta use this machinery to construct 4 -manifold invariants. Let $(M, g)$ be a smooth compact oriented Riemannian 4 -manifold with a chosen spin ${ }^{c}$ structure $\mathfrak{c}$. Choose some smooth $U(1)$ connection $A_{0}$ on the anti-canonical line bundle $L$ of $\mathfrak{c}$, and, for some $k>2$, consider the monopole map
$$\begin{array}{rllllll}
L_{k+1}^{2}\left(\mathbb{V}_{+}\right) & \oplus L_{k+1}^{2}\left(\Lambda^{1}\right) & \xrightarrow{\psi_{k}} L_{k}^{2}\left(\mathbb{V}_{-}\right) & \oplus & L_{k}^{2}\left(\Lambda^{+}\right) & \oplus & L_{k}^{2} / \mathbb{R} \\
( & \Phi & \alpha) & \mapsto & \left(D_{A} \Phi\right. & , & i F_{A}^{+}+\sigma(\Phi) \\
& , & \left.d^{*} \alpha\right)
\end{array}$$
of real Hilbert spaces. Here $A:=A_{0}+i \alpha$, and $\sigma: \mathbb{V}_{+} \rightarrow \Lambda^{+}$is the quadratic map occurring in equation (8). The monopole map really just represents the Seiberg-Witten equations (7-8) and a gauge-fixing condition, insofar as
$\psi_{k}^{-1}(0)$ by definition consists of the $L_{k+1}^{2}$ solutions of the Seiberg-Witten equations for which $d^{*}\left(A-A_{0}\right)=0$. Now notice that
$$\psi_{k}=\mathcal{L}+\mathcal{K},$$
where $\mathcal{L}$ is the linear Fredholm map given by
$$\mathcal{L}(\Phi, \alpha)=\left(D_{A_{0}} \Phi,-d^{+} \alpha, d^{*} \alpha\right)$$
and where $\mathcal{K}$ is the compact non-linear operator
$$\mathcal{K}(\Phi, \alpha)=\left(\frac{i}{2} \alpha \cdot \Phi, i F_{A_{0}}^{+}+\sigma(\Phi), 0\right) .$$
Also notice that $\psi_{k}$ is equivariant with respect to the $S^{1}$ action associated with the complex-Hilbert-space structures of $L_{k+1}^{2}\left(\mathbb{V}_{+}\right)$and $L_{k}^{2}\left(\mathbb{V}_{-}\right)$. If $b_{1}(M)=0$, and $k>3$, a Weitzenböck-formula argument [5] shows that $\psi_{k}$ satisfies the boundedness condition. By the previous discussion, it therefore determines an equivariant stable cohomotopy class $\left[\psi_{k}\right] \in \pi_{S^{1}}^{b}\left(\mathbb{C}^{2} \cup\{\infty\}\right)$, where $b=b_{+}(M)$ and $\imath=\left[c_{1}^{2}(L)-\tau(M)\right] / 8$. One can show that this class is independent of the metric $g$ used to construct it, and so constitutes a smooth manifold invariant of $M$, depending only on the spin ${ }^{c}$ structure $\mathfrak{c}$. It is also independent of the chosen integer $k>3$, so we will therefore usually denote the invariant by $[\psi]$, rather than by $\left[\psi_{k}\right]$. For much the same reason, we will simply call the monopole map $\psi$, rather than $\psi_{k}$, whenever this is unlikely to lead to confusion.

When $b_{1}(M) \neq 0$, the story is somewhat more involved, but the upshot is similar. Choose a base-point $* \in M$, and identify $H^{1}(M, \mathbb{Z})$ with the group of harmonic maps $u: M \rightarrow S^{1}$ such that $u(*)=1$. Then $\psi_{k}$ is equivariant with respect to the $H^{1}(M, \mathbb{Z})$-action by gauge transformations
$$\begin{aligned}
(\Phi, \alpha) & \mapsto(u \Phi, \alpha-2 i d \log u) \\
(\Psi, \varphi, c, f) & \mapsto(u \Psi, \varphi, c, f)
\end{aligned}$$
and we may use these actions to define
$$\begin{aligned}
\mathcal{A}_{k+1} & =\left[L_{k+1}^{2}\left(\mathbb{V}_{+}\right) \oplus L_{k+1}^{2}\left(\Lambda^{1}\right)\right] / H^{1}(M, \mathbb{Z}) \\
\mathcal{B}_{k} & =\left[\left(L_{k}^{2}\left(\mathbb{V}_{-}\right) \oplus L_{k}^{2}\left(\Lambda^{+}\right) \oplus L_{k}^{2} / \mathbb{R}\right) \times H^{1}(M, \mathbb{R})\right] / H^{1}(M, \mathbb{Z}) .
\end{aligned}$$
Observe that both $\mathcal{A}_{k+1}$ and $\mathcal{B}_{k}$ are Hilbert-space bundles over the Picard torus
$$\operatorname{Pic}^{0}(M)=H^{1}(M, \mathbb{R}) / H^{1}(M, \mathbb{Z}),$$
where the projection $\mathcal{A}_{k+1} \rightarrow \operatorname{Pic}^{0}(M)$ sends $(\Phi, \alpha)$ to the harmonic part of $\alpha$. The monopole map now becomes an $S^{1}$-equivariant compact perturbation of a Fredholm morphism of Hilbert bundles, and we may associated to it a stable cohomotopy class in the manner described above. That is, by choosing a suitable trivialization of $\mathcal{B}_{k}$, we may view our monopole map as an $S^{1}$ -equivariant smooth map
$$\psi_{k}: \mathcal{A}_{k+1} \rightarrow \mathcal{C}_{k},$$
where
$$\mathcal{C}_{k}=L_{k}^{2}\left(\mathbb{V}_{-}\right) \oplus L_{k}^{2}\left(\Lambda^{+}\right) \oplus L_{k}^{2} / \mathbb{R},$$
and extract its stable cohomotopy class by restricting $\psi_{k}$ to $\mathbf{V}=\mathcal{L}^{-1}(\mathbf{W})$ and then projecting into $\mathbf{W}^{+}$for a good subspace $\mathbf{W} \subset \mathcal{C}_{k}$ of sufficiently large dimension. This equivariant stable cohomotopy class is independent of $g$ and $k$, and the resulting picture may be codified as follows:

Theorem 5 (Bauer-Furuta). Let $M$ be a smooth compact oriented 4-manifold with $b_{+}(M)=b$, and let $\mathfrak{c}$ be a spin ${ }^{c}$ structure on $M$. Then the corresponding monopole map $\psi$ determines a stable cohomotopy class
$$[\psi] \in \pi_{S^{1}}^{b}\left(\operatorname{ind}(D)^{+}\right),$$
where $\operatorname{ind}(D) \in K^{0}\left(\operatorname{Pic}^{0}(M)\right)$ is the virtual index bundle of the spin ${ }^{c}$ Dirac operator. Moreover, if $b_{+}(X) \geq b_{1}(X)+2$, an orientation of the vector space $H^{1}(M, \mathbb{R}) \oplus \mathcal{H}_{g}^{+}$determines a group homomorphism $\pi_{S^{1}}^{b}\left(\operatorname{ind}(D)^{+}\right) \rightarrow \mathbb{Z}$ which maps [ $\psi$ ] to the usual Seiberg-Witten invariant.

The class $[\psi]$ will henceforth be called the Bauer-Furuta invariant of $(M, \mathfrak{c})$. Its importance for our purposes stems from the following observation:

Proposition 6. If the Bauer-Furuta invariant $[\psi]$ of ( $M, \mathfrak{c}$ ) is non-zero, then $c_{1}^{\mathbb{R}}(L)$ is a monopole class. (Here, once again, $L$ is the anti-canonical line bundle of $\mathfrak{c}$, and $c_{1}^{\mathbb{R}}(L)$ is the image of $c_{1}(L)$ in $H^{2}(M, \mathbb{Z})$ /torsion.)

Proof. Given a smooth metric $g$ on $M$, we will show that the Seiberg-Witten equations (7-8) admit a solution $(\Phi, A)$ for the spin ${ }^{c}$ structure $\mathfrak{c}$. Our argument will hinge on the fact that, while the monopole map $\psi_{k}$ used in the construction depends on the choice of an integer $k>3$, we always have a commutative diagram
![](https://cdn.mathpix.com/cropped/31297ce1-1cc9-476a-af99-69cbf0ba2ca2-13.jpg?height=188&width=308&top_left_y=2145&top_left_x=819)
where $\psi_{k-1}$ is also continuous. The result will be deduced from this by invoking the Rellich theorem.

Indeed, consider the bounded self-adjoint operator $Q: \mathcal{C}_{k} \rightarrow \mathcal{C}_{k}$ defined by
$$\langle v, Q u\rangle_{L_{k}^{2}}:=\langle v, u\rangle_{L_{k-1}^{2}} .$$
Because the positive self-adjoint operator $Q$ is compact by the Rellich theorem, its eigenspaces $\mathbf{E}_{j}$ are mutually orthogonal, finite-dimensional, span $\mathcal{C}_{k}$, and may be taken to be listed in an order such that the corresponding sequence of eigenvalues $\lambda_{1}>\lambda_{2}>\cdots>\lambda_{j}>\cdots>0$ monotonically decreases to 0. Now choose a sequence of good subspaces $\mathbf{W}_{1} \subset \mathbf{W}_{2} \subset \mathbf{W}_{3} \subset \cdots$ for $\psi_{k}$ so that $\oplus_{i=1}^{j} \mathbf{E}_{i} \subset \mathbf{W}_{j}$. If, for large $j, \psi_{k}\left(\mathbf{V}_{j}\right)$ were to avoid the unit ball in $\mathbf{W}_{j}^{\perp}$, then $\left(\operatorname{pr}_{\mathbf{w}_{j}} \circ \psi_{k}\right)\left(\mathbf{V}_{j}\right)$ would avoid the origin, and $\mathrm{pr}_{\mathbf{W}_{j}} \circ \psi_{k}: \mathbf{V}_{j} \cup\{\infty\} \rightarrow \mathbf{W}_{j} \cup\{\infty\}$ would be $S^{1}$-equivariantly homotopic to the constant map at $\infty$ via dilations; but we would then have $[\psi]=0$, contradicting our hypothesis. Hence the unit ball in $\mathbf{W}_{j}^{\perp}$ must meet the image of $\psi_{k}$ for all j . That is, there must be sequences $p_{j} \in \mathcal{A}_{k+1}, q_{j} \in \mathcal{C}_{k}$, with
$$\psi_{k}\left(p_{j}\right)=q_{j}$$
and
$$\left\|q_{j}\right\|_{L_{k}^{2}}<1, \quad q_{j} \perp \oplus_{i=1}^{j} \mathbf{E}_{i} .$$
However,
$$u \perp \oplus_{i=1}^{j} \mathbf{E}_{i} \Longrightarrow\|u\|_{L_{k-1}^{2}}^{2} \leq \lambda_{j+1}\|u\|_{L_{k}^{2}}^{2}$$
so it follows that that $\left\|q_{j}\right\|_{L_{k-1}^{2}} \leq \sqrt{\lambda_{j+1}} \rightarrow 0$, and hence $q_{j} \rightarrow 0$ in $L_{k-1}^{2}$.
On the other hand, because $\psi_{k}$ satisfies the boundedness condition, and because the $q_{j}$ are all in the unit ball, we have
$$\left\|p_{j}\right\|_{L_{k+1}^{2}}<C$$
for some $C$. The Rellich theorem therefore tells us that there is a subsequence $p_{j_{i}}$ which converges in the $L_{k}^{2}$ norm to some $p_{\infty} \in \mathcal{A}_{k}$. The continuity of $\psi_{k-1}$, together with its compatibility with $\psi_{k}$, now tells us that
$$\psi_{k-1}\left(p_{\infty}\right)=\psi_{k-1}\left(\lim _{i \rightarrow \infty} p_{j_{i}}\right)=\lim _{i \rightarrow \infty} \psi_{k-1}\left(p_{j_{i}}\right)=\lim _{i \rightarrow \infty} q_{j_{i}}=0,$$
which is to say that $p_{\infty}=(\Phi, \alpha)$ gives us a solution $\left(\Phi, A_{0}+i \alpha\right)$ of the gaugefixed Seiberg-Witten equations of class $L_{k}^{2}$. The usual bootstrap regularity argument then shows that this solution is actually $C^{\infty}$. \(\square\)

One of Bauer's key results involves the smash product
$$\wedge: \pi_{S^{1}}^{m}(\mathfrak{X}) \times \pi_{S^{1}}^{m^{\prime}}\left(\mathfrak{X}^{\prime}\right) \rightarrow \pi_{S^{1}}^{m+m^{\prime}}\left(\mathfrak{X} \wedge \mathfrak{X}^{\prime}\right) .$$
Here, if $(\mathfrak{X}, x)$ and $\left(\mathfrak{X}^{\prime}, x^{\prime}\right)$ are pointed finite complexes, their join $\mathfrak{X} \wedge \mathfrak{X}^{\prime}$ is just the one-point compactification of $(\mathfrak{X}-x) \times\left(\mathfrak{X}^{\prime}-x^{\prime}\right)$. The operation in question is then induced by taking Cartesian products. Namely, if
$$f:(\mathfrak{X}-x) \times \mathbb{C}^{n} \times \mathbb{R}^{n} \rightarrow \mathbb{C}^{n} \times \mathbb{R}^{m+n}$$
and
$$f^{\prime}:\left(\mathfrak{X}^{\prime}-x^{\prime}\right) \times \mathbb{C}^{n^{\prime}} \times \mathbb{R}^{n^{\prime}} \rightarrow \mathbb{C}^{n^{\prime}} \times \mathbb{R}^{m^{\prime}+n^{\prime}}$$
are $S^{1}$-equivariant proper maps, so is
$$f \times f^{\prime}:(\mathfrak{X}-x) \times\left(\mathfrak{X}^{\prime}-x^{\prime}\right) \times \mathbb{C}^{n+n^{\prime}} \times \mathbb{R}^{n+n^{\prime}} \rightarrow \mathbb{C}^{n+n^{\prime}} \times \mathbb{R}^{m+m^{\prime}+n+n^{\prime}},$$
and setting $[f] \wedge\left[f^{\prime}\right]=\left[f \times f^{\prime}\right]$ then gives us the desired operation.
Theorem 7 (Bauer). Let $X$ and $Y$ be smooth compact oriented 4manifolds with spin ${ }^{c}$ structures $\mathfrak{c}_{X}$ and $\mathfrak{c}_{Y}$. Then the Bauer-Furuta invariant of the connected sum $X \# Y$, equipped with the spin ${ }^{c}$ structure $\mathfrak{c}_{X} \# \mathfrak{c}_{Y}$, is exactly the the smash product of the invariants of $\left(X, \mathfrak{c}_{X}\right)$ and $\left(Y, \mathfrak{c}_{Y}\right)$ :
$$\left[\psi_{X \# Y}\right]=\left[\psi_{X}\right] \wedge\left[\psi_{Y}\right] .$$
In other words, $\psi_{X \# Y}$ and $\psi_{X} \times \psi_{Y}$ represent the same equivariant stable cohomotopy class.

Corollary 8. Let $M$ be a smooth compact oriented 4-manifold with a spin ${ }^{c}$ structure $\mathfrak{c}_{M}$ for which the Bauer-Furuta invariant is non-trivial. Let $N$ be a smooth compact oriented 4-manifold with negative definite intersection form, and let $\mathfrak{c}_{N}$ be any spin ${ }^{c}$-structure on $N$ with $c_{1}^{2}=-b_{2}(N)$. Then the Bauer-Furuta invariant is also non-trivial for the spin ${ }^{c}$ structure $\mathfrak{c}_{M} \# \mathfrak{c}_{N}$ on the connected sum $M \# N$.

Proof. Since we have chosen a spin ${ }^{c}$ structure on $N$ for which the Dirac operator has index $\left[c_{1}^{2}-\tau(N)\right] / 8=0$, the vector bundle $\operatorname{ind}\left(D_{N}\right) \rightarrow \operatorname{Pic}^{0}(N)$ has rank 0, and the image of the Bauer-Furuta invariant of $N$ under the map
$$\pi_{S^{1}}^{0}\left(\operatorname{ind}\left(D_{N}\right)^{+}\right) \rightarrow \pi_{S^{1}}^{0}\left(\mathrm{pt}^{+}\right),$$
induced by restriction to the fiber over a point in $\operatorname{Pic}^{0}(N)$, is just the class of the identity map. By Theorem 7, the restriction of the invariant $[\psi]=$ $\left[\psi_{M}\right] \wedge\left[\psi_{N}\right]$ of $M \# N$ to $\pi_{S^{1}}^{b}\left(\left[\left.\operatorname{ind}\left(D_{M \# N}\right)\right|_{\text {Pic }^{0}(M) \times \text { pt }}\right]^{+}\right)$therefore equals $\left[\psi_{M}\right] \wedge[\mathrm{id}]=\left[\psi_{M}\right]$. \(\square\)

When $b_{1}(M)=0$ and the spin ${ }^{c}$ structure arises from an almost-complex structure, one has
$$\pi_{S^{1}}^{b}\left(\operatorname{ind}(D)^{+}\right)=\pi_{S^{1}}^{b}\left(S^{b+1}\right),$$
where the sphere $S^{b+1}$ is thought of as $\mathbb{C}^{\imath} \cup\{\infty\}$ for $\imath=\left[c_{1}^{2}(L)-\tau(X)\right] / 8=$ $(b+1) / 2$. If the mod-2 Seiberg-Witten invariant is non-zero and $b=b_{+}(M) \equiv$ $3 \bmod 4$, Bauer [4] then shows that the Bauer-Furuta invariant is represented by the suspension of the Hopf map $S^{3} \rightarrow S^{2}$. In conjunction with Theorem 7, this then implies the following:

Theorem 9 (Bauer). For each $j \in\{1,2,3,4\}$, let $\left(X_{j}, J_{j}\right)$ be a smooth compact almost-complex 4-manifold with $b_{1}=0$ and $b_{+} \equiv 3 \bmod 4$. Suppose, moreover, that $\sum_{j=1}^{4} b_{+}\left(X_{j}\right) \equiv 4 \bmod 8$, and that the canonical spin ${ }^{c}$ structure on each $\left(X_{j} . J_{j}\right)$ has non-zero mod-2 Seiberg-Witten. Then the corresponding spin ${ }^{c}$ structures on the connected sums $\#_{j=1}^{m} X_{j}, m=1, \ldots, 4$, all have non-zero Bauer-Furuta invariant.

Indeed, when $m=2$ or 3, this can be deduced by just looking at the image of the Bauer-Furuta invariant in the non-equivariant stable homotopy group $\pi_{m}^{s t}\left(S^{0}\right)=\pi^{-m}\left(S^{0}\right)$. The $m=4$ case is more subtle, however, and involves the $S^{1}$-equivariant machinery in an essential manner.

With Proposition 6 and Corollary 8, Theorem 9 implies
Proposition 10. Let $X_{j}, j=1, \ldots, 4$, be smooth compact almost-complex 4-manifolds with non-zero mod-2 Seiberg-Witten invariant. Let N be a smooth compact oriented 4-manifold with $b_{+}(N)=0$, and let $E_{1}, \ldots, E_{k}$ be a set of generators for $H^{2}(N, \mathbb{Z})$ /torsion relative to which the intersection form is diagonal. If $b_{1}\left(X_{j}\right)=0, b_{+}\left(X_{j}\right) \equiv 3 \bmod 4$, and $\sum_{j=1}^{4} b_{+}\left(X_{j}\right) \equiv 4 \bmod 8$, then, for any $m=1, \ldots, 4$,
$$\sum_{j=1}^{m} \pm c_{1}\left(X_{j}\right)+\sum_{i=1}^{k} \pm E_{i}$$
is a monopole class of $\left[\#_{j=1}^{m} X_{j}\right] \# N$. Here the ± signs are arbitrary, and are independent of one another.

Corollary 11. Let $X_{j}$ and $N$ be as in Proposition 10, and, for some $m=$ $1, \ldots, 4$, let $g$ be a Riemannian metric on $M=\left[\#_{j=1}^{m} X_{j}\right] \# N$. Then, with respect to the Hodge decomposition
$$H^{2}(M, \mathbb{R})=\mathcal{H}_{g}^{+} \oplus \mathcal{H}_{g}^{-},$$
there is a monopole class $a \in H^{2}(M, \mathbb{R})$ whose self-dual part $a^{+}$satisfies
$$\left(a^{+}\right)^{2} \geq \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$

Proof. Let $E_{1}, \ldots, E_{k}$ be a set of generators for $H^{2}(N, \mathbb{Z}) /$ torsion relative to which the intersection form is diagonal; such a set of generators always exists [10, 5]. Let $\alpha=\sum_{j=1}^{m} c_{1}\left(X_{j}\right)$, and choose new generators $\hat{E}_{i}= \pm E_{i}$ for $H^{2}(N, \mathbb{Z})$ /torsion such that
$$\alpha^{+} \cdot \hat{E}_{i} \geq 0 .$$
Then $a=\alpha+\sum_{i=1}^{k} \hat{E}_{i}$ is a monopole class on $M$, and
$$\begin{aligned}
\left(a^{+}\right)^{2} & =\left[\alpha^{+}+\sum_{i=1}^{k} \hat{E}_{i}^{+}\right]^{2} \\
& =\left(\alpha^{+}\right)^{2}+2 \alpha^{+} \cdot \sum_{i=1}^{k} \hat{E}_{i}^{+}+\left[\left(\sum_{i=1}^{k} \hat{E}_{i}\right)^{+}\right]^{2} \\
& =\left(\alpha^{+}\right)^{2}+2 \sum_{i=1}^{k}\left(\alpha^{+} \cdot \hat{E}_{i}\right)+\left[\left(\sum_{i=1}^{k} \hat{E}_{i}\right)^{+}\right]^{2} \\
& \geq\left(\alpha^{+}\right)^{2} \geq \alpha^{2}=\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right),
\end{aligned}$$
as promised. \(\square\)

\section*{4. Scalar Curvature Problems.}

Recall that a conformal class on a smooth compact manifold $M$ is by definition the set of smooth Riemannian metrics on $M$
$$\gamma=[g]=\left\{u g \mid u: M \rightarrow \mathbb{R}^{+}\right\}$$
which are point-wise proportional to some Riemannian metric $g$. As we saw in §1, each conformal class $\gamma$ has an associated number
$$\mathcal{Y}_{\gamma}=\inf _{g \in \gamma} \frac{\int_{M} s_{g} d \mu_{g}}{\left(\int_{M} d \mu_{g}\right)^{\frac{n-2}{n}}},$$
called the Yamabe constant of $\gamma$. For any metric $g, \mathcal{Y}_{[g]}$ has the same sign as the lowest eigenvalue of the Yamabe Laplacian $\Delta+\frac{(n-2)}{4(n-1)} s_{g}$; if $s_{g}$ does not change sign, moreover, this sign agrees with that of $s_{g}$. A deep theorem [2, 28, 31] of Yamabe, Trudinger, Aubin, and Schoen asserts that any conformal class $\gamma$ contains a metric which actually minimizes the relevant functional. Such a metric is called a Yamabe minimizer. Any Yamabe minimizer has constant scalar curvature. Conversely, any metric $g$ with $s_{g}=$ const $\leq 0$ is a Yamabe minimizer.

Given a smooth compact $n$-manifold $M$, one defines the Yamabe invariant [18, 32, 25, 26] of $M$ by
$$\mathcal{Y}(M)=\sup _{\gamma \in \mathcal{C}(M)} \mathcal{Y}_{\gamma}=\sup _{\gamma} \inf _{g \in \gamma} \frac{\int_{M} s_{g} d \mu_{g}}{\left(\int_{M} d \mu_{g}\right)^{\frac{n-2}{n}}},$$
where $\mathcal{C}(M)$ denotes the space of all conformal classes of metrics on $M$. As already pointed out in §1, this is a real-valued diffeomorphism invariant of $M$. In light of the above comments, it is immediate that $\mathcal{Y}(M)>0$ iff $M$ admits a metric of positive scalar curvature. On the other hand, if $M$ does not admit metrics of positive scalar curvature, the invariant is simply the supremum of the scalar curvatures of unit-volume constant-scalar-curvature metrics on $M$, since any constant-scalar-curvature metric of non-positive scalar curvature is automatically a Yamabe minimizer.

The minimax definition of $\mathcal{Y}(M)$ is technically rather unwieldy. Fortunately, by an observation of Besson-Courtois-Gallot [8], $\mathcal{Y}(M)$ and the conceptually simpler invariant
$$\mathcal{I}_{s}(M)=\inf _{g} \int_{M}\left|s_{g}\right|^{n / 2} d \mu_{g}$$
determine each other whenever $M$ does not admit metrics of positive scalar curvature [1, 26].

Proposition 12. Let $M$ be a smooth compact $n$-manifold, $n \geq 3$. Then
$$\mathcal{I}_{s}(M)= \begin{cases}0 & \text { if } \mathcal{Y}(M) \geq 0 \\ |\mathcal{Y}(M)|^{n / 2} & \text { if } \mathcal{Y}(M) \leq 0 .\end{cases}$$

The proof depends on two main observations. First of all, there are always conformal classes with negative Yamabe constant when $n \geq 3$; because the lowest eigenvalue of the Yamabe Laplacian depends continuously on $g$, $Y(M)>0$ would therefore imply the existence of a scalar-flat metric, and thus force $\mathcal{I}_{s}(M)$ to vanish. Secondly, detailed calculation reveals that the $L^{n / 2}$ norm of $s$ is minimized in each conformal class of negative Yamabe constant by the metrics of constant scalar curvature.

This same argument also shows that $\mathcal{I}_{s}$ can be re-expressed [8, 26] as
$$\mathcal{I}_{s}(M)=\inf _{g} \int_{M}\left|s_{-g}\right|^{n / 2} d \mu_{g},$$
where $s_{-g}(x)=\min \left(s_{g}(x), 0\right)$. Thus, in essence, we are allowed to neglect regions of positive scalar curvature when computing $\mathcal{I}_{s}$. This observation has some important consequences. For example, if $\left(X, g_{X}\right)$ and $\left(Y, g_{Y}\right)$ are any compact Riemannian $n$-manifolds, then, for any $\varepsilon>0$, the Gromov-Lawson method [14] of joining $X$ to $Y$ by a long, thin neck with $s>0$ yields a Riemannian metric $g_{X \# Y}$ on the connected sum $X \# Y$ such that
$$\int_{X \# Y}\left|s_{-g_{X \# Y}}\right|^{n / 2} d \mu_{g_{X \# Y}}<\int_{X}\left|s_{g_{X}}\right|^{n / 2} d \mu_{g_{X}}+\int_{Y}\left|s_{g_{Y}}\right|^{n / 2} d \mu_{g_{Y}}+\varepsilon$$
One therefore has the following general inequality [18]:
Proposition 13. Let $X$ and $Y$ be smooth compact $n$-manifolds, $n \geq 3$. Then
$$\mathcal{I}_{s}(X \# Y) \leq \mathcal{I}_{s}(X)+\mathcal{I}_{s}(Y) .$$

Now the invariant $\mathcal{I}_{s}$ of a smooth compact 4-manifold $M$ is just
$$\mathcal{I}_{s}(M)=\inf _{g} \int_{M} s_{g}^{2} d \mu_{g},$$
so Proposition 2 and Corollary 11 give us the following lower bound:
Proposition 14. Let $X_{j}, j=1, \ldots, 4$, be smooth compact almost-complex 4-manifolds with non-zero mod-2 Seiberg-Witten invariant. Let N be a smooth compact oriented 4-manifold with $b_{+}(N)=0$. If $b_{1}\left(X_{j}\right)=0$, $b_{+}\left(X_{j}\right) \equiv 3 \bmod 4$, and $\sum_{j=1}^{4} b_{+}\left(X_{j}\right) \equiv 4 \bmod 8$, then, for any $m=1, \ldots, 4$,
$$\mathcal{I}_{s}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right) \geq 32 \pi^{2} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$

Combining Propositions 13 and 14, we thus obtain
Theorem B. Let $X_{j}, j=1, \ldots, 4$, be minimal compact complex surfaces with $b_{1}\left(X_{j}\right)=0, b_{+}\left(X_{j}\right) \equiv 3 \bmod 4$, and $\sum_{j=1}^{4} b_{+}\left(X_{j}\right) \equiv 4 \bmod 8$. Let $N$ be a smooth compact oriented 4-manifold with $b_{+}(N)=0$ which admits a metric of non-negative scalar curvature. Then
$$\mathcal{I}_{s}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right)=32 \pi^{2} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)$$
Proof. For any minimal compact complex surface $X$ with $b_{+}>1$, one has [25, 26]
$$\mathcal{I}_{s}(X)=32 \pi^{2} c_{1}^{2}(X) .$$
On the other hand, since $N$ admits a metric of non-negative scalar curvature,
$$\mathcal{I}_{s}(N)=0 .$$
Propositions 13 and 14 thus tells us that
$$\begin{aligned}
\mathcal{I}_{s}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right) & \leq \mathcal{I}_{s}(N)+\sum_{j=1}^{m} \mathcal{I}_{s}\left(X_{j}\right) \\
& =32 \pi^{2} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) \\
& \leq \mathcal{I}_{s}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right),
\end{aligned}$$
and the promised equality follows. \(\square\)

But if $M$ is a 4-manifold with a non-trivial Bauer-Furuta invariant, $M$ does not admit metrics of positive scalar curvature, and hence has $\mathcal{Y}(M) \leq 0$. Theorem A and Proposition 12 therefore together imply

Theorem A. Let $X_{j}, j=1, \ldots, 4$, be minimal compact complex surfaces with $b_{1}\left(X_{j}\right)=0, b_{+}\left(X_{j}\right) \equiv 3 \bmod 4$, and $\sum_{j=1}^{4} b_{+}\left(X_{j}\right) \equiv 4 \bmod 8$. Let $N$ be a smooth compact oriented 4-manifold with $b_{+}(N)=0$ and $\mathcal{Y}(N) \geq 0$. Then
$$\mathcal{Y}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right)=-4 \pi \sqrt{2 \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)} .$$

\section*{5. Ricci Curvature.}

In dimension $n=4$, the Ricci-curvature-based invariant defined by equation (5) becomes
$$\mathcal{I}_{r}(M)=\inf _{g} \int_{M}\left|r_{g}\right|^{2} d \mu_{g}=\inf _{g} \int_{M}\left(\frac{s_{g}^{2}}{4}+\left|\stackrel{\circ}{r}_{g}\right|^{2}\right) d \mu_{g}$$
where $\stackrel{\circ}{r}$ denotes the trace-free piece of the Ricci curvature. Now notice that the Gauss-Bonnet-type formula [7, 15, 35]
$$(2 \chi+3 \tau)(M)=\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s_{g}^{2}}{24}+2\left|W_{+}\right|_{g}^{2}-\frac{\left|\stackrel{\circ}{r}_{g}\right|^{2}}{2}\right) d \mu_{g}$$
therefore tells us that
$$\int_{M}\left|r_{g}\right|^{2} d \mu_{g}=-8 \pi^{2}(2 \chi+3 \tau)(M)+\int_{M}\left(\frac{s_{g}^{2}}{3}+4\left|W_{+}\right|_{g}^{2}\right) d \mu_{g}$$
for any Riemannian metric $g$ on a compact oriented 4-manifold $M$. On the other hand, the Cauchy-Schwarz and triangle inequalities imply [27] that
$$\int_{M}\left(\frac{s_{g}^{2}}{3}+4\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} \geq\left.\frac{2}{9} \int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)\right|_{g} ^{2} d \mu_{g}$$
If $a$ is a monopole class on $M$, Proposition 4 therefore implies [27] that
$$\int_{M}|r|_{g}^{2} d \mu_{g} \geq 8 \pi^{2}\left[2\left(a^{+}\right)^{2}-(2 \chi+3 \tau)(M)\right] .$$
We therefore have
Proposition 15. Let $X_{j}, j=1, \ldots, 4$, be smooth compact almost-complex 4-manifolds with non-zero mod-2 Seiberg-Witten invariant. Suppose, moreover, that $b_{1}\left(X_{j}\right)=0, b_{+}\left(X_{j}\right) \equiv 3 \bmod 4$, and $\sum_{j=1}^{4} b_{+}\left(X_{j}\right) \equiv 4 \bmod 8$. Let $N$ be a smooth compact oriented 4-manifold with $b_{+}(N)=0$. Then, for $m=1, \ldots, 4$,
$$\mathcal{I}_{r}(M) \geq 8 \pi^{2}\left[4 m-(2 \chi+3 \tau)(N)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)\right] .$$

Proof. By Corollary 11, there is a monopole class $a$ on $M=\left[\#_{j=1}^{m} X_{j}\right] \# N$ with $\left(a^{+}\right)^{2} \geq \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)$. On the other hand,
$$(2 \chi+3 \tau)(M)=(2 \chi+3 \tau)(N)-4 m+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right),$$
so that (12) implies that
$$\int_{M}|r|_{g}^{2} d \mu_{g} \geq 8 \pi^{2}\left[4 m-(2 \chi+3 \tau)(N)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)\right]$$
for any metric $g$ on $M$. Taking the infimum over $g$ of the left-hand side now yields the desired inequality. \(\square\)

Amazingly, this estimate is sharp in many cases:
Theorem C. Let $X_{j}, j=1, \ldots, 4$ be minimal complex surfaces satisfying (1-3). Let $N$ be a smooth compact oriented 4-manifold which admits an anti-self-dual metric of positive scalar curvature. Then, for each choice of $m=1, \ldots, 4$,
$$\mathcal{I}_{r}\left(\left[\#_{j=1}^{m} X_{j}\right] \# N\right)=8 \pi^{2}\left[4 m-(2 \chi+3 \tau)(N)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)\right] .$$
Proof. Let us first observe [9, 22] that any anti-self-dual 4-manifold $(N, h)$ of positive scalar curvature satisfies $b_{+}(N)=0$. We thus have
$$\int_{M}|r|_{g}^{2} d \mu_{g} \geq 8 \pi^{2}\left[4 m-(2 \chi+3 \tau)(N)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)\right]$$
by the previous result. Of course, by (11), this equivalent to the statement that
$$\int_{M}\left(\frac{s_{g}^{2}}{3}+4\left|W_{+}\right|_{g}^{2}\right) d \mu_{g} \geq 16 \pi^{2} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right),$$
and what we need to show is that, for any $\varepsilon>0$, there is a metric $g_{\varepsilon}$ on $M$ with
$$\int_{M}\left(\frac{s_{g_{\varepsilon}}^{2}}{3}+4\left|W_{+}\right|_{g_{\varepsilon}}^{2}\right) d \mu_{g_{\varepsilon}}<\varepsilon+16 \pi^{2} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$

Such a metric can be constructed as follows: choose $m$ points $p_{1}, \ldots, p_{m} \in$ $N$, and let $u$ be the conformal Green's function of $\left\{p_{1}, \ldots, p_{m}\right\}$ :
$$\left(\Delta+\frac{s}{6}\right) u=\sum_{j=1}^{m} \delta_{p_{j}} .$$
For any positive constant $c$, the metric $c u^{2} h$ on $N-\left\{p_{1}, \ldots, p_{m}\right\}$ is then scalar-flat, anti-self-dual, and asymptotically flat, with $m$ ends. Equip the pluricanonical model $\check{X}_{j}$ of $X_{j}$ with a Kähler-Einstein orbifold metric [3, 19, 38], choose a point $q_{j}$ of $X_{j}$, remove a small metric ball around $q_{j}$, and glue the boundary of this ball to the $j^{\text {th }}$ boundary component of $N$ minus $m$ balls centered at $p_{1}, \ldots, p_{m}$. As the metrics do not quite match, one must use a partition of unity to smooth things together, but this can be done in a manner such that the $L^{2}$ norms of the curvature tensor on the transition annuli are as small as desired [25, 27]. In the same way, replace a neighborhood of each orbifold point of $\dot{X}_{j}$ by a gravitational instanton [20]. Now the Kähler-Einstein orbifold metric on $\check{X}_{j}$ has
$$\int_{\check{X}_{j}}\left(\frac{s^{2}}{3}+4\left|W_{+}\right|^{2}\right) d \mu=\int_{\check{X}_{j}} \frac{s^{2}}{2} d \mu=16 \pi^{2} c_{1}^{2}\left(X_{j}\right)$$
whereas $N-\left\{p_{1}, \ldots, p_{m}\right\}$ and the gravitational instantons have $s \equiv 0$ and $W_{+} \equiv 0$. The metric $g_{\varepsilon}$ can thus be chosen to satisfy (13), and the result therefore follows. \(\square\)

In particular, since $k \overline{\mathbb{C P}}_{2} \# \ell\left[S^{1} \times S^{3}\right]$ admits anti-self-dual metrics of positive scalar curvature [17, 23], we obtain

Corollary 16. Let $X_{j}, j=1, \ldots, 4$ be minimal complex surfaces satisfying (1-3). Then, for any integers $k, \ell \geq 0$, and any $m=1, \ldots, 4$,
$$\mathcal{I}_{r}\left(\left[\#_{j=1}^{m} X_{j}\right] \# k \overline{\mathbb{C P}}_{2} \# \ell\left[S^{1} \times S^{3}\right]\right)=8 \pi^{2}\left[k+4(\ell+m-1)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)\right] .$$

\section*{6. Obstructions to Einstein Metrics.}

The main point of this article has been that the Bauer-Furuta invariant can be used to deduce certain sharp curvature-integral estimates for many interesting 4-manifolds. However, the same techniques allow one to derive other curvature estimates which, while presumably not sharp, nonetheless
have interesting consequences. In particular, Proposition 4 can also be used to construct many new examples of smooth compact 4-manifolds which do not admit Einstein metrics.

Indeed, the Cauchy-Schwarz and triangle inequalities imply [27] that
$$\int\left(\frac{s^{2}}{24}+2\left|W_{+}\right|^{2}\right) d \mu \geq \frac{1}{27} \int\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu$$
If $a$ is a monopole class on $M$, Proposition 4 therefore tells us [27] that
$$\frac{1}{4 \pi^{2}} \int\left(\frac{s^{2}}{24}+2\left|W_{+}\right|^{2}\right) d \mu \geq \frac{2}{3}\left(a^{+}\right)^{2}$$
By Corollary 11, we therefore have
Theorem D. Let $X_{j}, j=1, \ldots, 4$ be smooth, compact almost-complex 4manifolds for which the mod-2 Seiberg-Witten invariant is non-zero, and suppose, moreover, that (1-3) hold. Let $N$ be any oriented 4-manifold with $b_{+}=0$. Then, for any $m=2,3$ or 4, the smooth 4-manifold $\left[\#_{j=1}^{m} X_{j}\right] \# N$ does not admit Einstein metrics if
$$4 m-(2 \chi+3 \tau)(N) \geq \frac{1}{3} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right) .$$
Proof. By Corollary 11, for any choice of Riemannian metric $g$ on $M=$ $\left[\#_{j=1}^{m} X_{j}\right] \# N$, there is a monopole class $a$ on $M$ with $\left(a^{+}\right)^{2} \geq \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)$. Thus any metric $g$ on $M$ satisfies
$$\frac{1}{4 \pi^{2}} \int\left(\frac{s^{2}}{24}+2\left|W_{+}\right|^{2}\right) d \mu \geq \frac{2}{3} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)$$
by (14), and the inequality is necessarily strict if $m>1$, since $M$ does not then admit a symplectic structure. If $g$ is Einstein, however, the left-hand side equals $(2 \chi+3 \tau)(M)$ by (10). Since
$$(2 \chi+3 \tau)(M)=-4 m+(2 \chi+3 \tau)(N)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)$$
this means that the existence of an Einstein metric $g$ on $M$ implies, for $m=2,3$ or 4, that
$$-4 m+(2 \chi+3 \tau)(N)+\sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)>\frac{2}{3} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right),$$
or in other words that
$$\frac{1}{3} \sum_{j=1}^{m} c_{1}^{2}\left(X_{j}\right)>4 m-(2 \chi+3 \tau)(N)$$
The desired result therefore follows by contraposition. \(\square\)

In particular, using a celebrated result of Taubes [34], this immediately gives us many new spin examples with free fundamental groups:

Corollary 17. Let $X$ be a simply connected symplectic 4-dimensional spin manifold with $b_{+} \equiv 3 \bmod 8$. Then the spin manifold $X \# n K 3 \# \ell\left[S^{1} \times S^{3}\right]$ does not admit Einstein metrics if $n=1,2$ or 3 and $\ell+n \geq c_{1}^{2}(X) / 12$.

We remark that the work of Gompf [12] provides an enormous catalog of choices for $X$. Moreover, by replacing a $K 3$ with one of Kodaira's homotopy $K 3$ 's, one can find infinitely many smooth structures on these manifolds for which the obstruction also applies; cf. [16]. On the other hand, if we take $X$ to have negative signature, the Hitchin-Thorpe inequality [7, 15, 35] would only provide an obstruction to the existence of Einstein metrics on these spaces for $\ell+n \geq c_{1}^{2}(X) / 4$.

Acknowledgment. The authors would like to thank Stefan Bauer and Mikio Furuta for many helpful remarks regarding the Bauer-Furuta invariant.

\section*{References.}
[1] M. Anderson, Extrema of curvature functionals on the space of metrics on 3-manifolds, Calc. Var. Partial Differ. Eq., 5 (1997), pp. 199-269.
[2] T. Aubin, Équations différentielles non linéaires et problème de Yamabe concernant la courbure scalaire, J. Math. Pures Appl. (9), 55 (1976), pp. 269-296.
[3] -, Equations du type Monge-Ampère sur les variétés Kählériennes compactes, C. R. Acad. Sci. Paris, 283A (1976), pp. 119-121.
[4] S. Bauer, A stable cohomotopy refinement of Seiberg-Witten invariants: II. Invent. Math. (2003), DOI: 10.1007/s00222-003-0289-4.
[5] S. Bauer and M. Furuta, A stable cohomotopy refinement of Seiberg-Witten invariants: I. Invent. Math. (2003), DOI:10.1007/s00222-003-0288-5.
[6] M. Berger, Riemannian geometry during the second half of the twentieth century, American Mathematical Society, Providence, RI, 2000. Reprint of the 1998 original.
[7] A. Besse, Einstein Manifolds, Springer-Verlag, 1987.
[8] G. Besson, G. Courtois, and S. Gallot, Volume et entropie minimale des espaces localement symétriques, Inv. Math., 103 (1991), pp. 417-445.
[9] J.-P. Bourguignon, Les variétés de dimension 4 à signature non nulle dont la courbure est harmonique sont d'Einstein, Invent. Math., 63 (1981), pp. 263-286.
[10] S. K. Donaldson, An application of gauge theory to four-dimensional topology, J. Differential Geom., 18 (1983), pp. 279-315.
[11] S. K. Donaldson and P. B. Kronheimer, The Geometry of Four-Manifolds, Oxford University Press, Oxford, 1990.
[12] R. E. Gompf, A new construction of symplectic manifolds, Ann. of Math. (2), 142 (1995), pp. 527-595.
[13] R. E. Gompf and A. I. Stipsicz, 4-manifolds and Kirby calculus, American Mathematical Society, Providence, RI, 1999.
[14] M. Gromov and H. B. Lawson, The classification of simply connected manifolds of positive scalar curvature, Ann. Math., 111 (1980), pp. 423-434.
[15] N. Hitchin, On compact four-dimensional Einstein manifolds, J. Differential Geom., 9 (1974), pp. 435-442.
[16] M. Ishida and C. LeBrun, Spin manifolds, Einstein metrics, and differential topology, Math. Res. Lett., 9 (2002), pp. 229-240.
[17] J. Kim, On the scalar curvature of self-dual manifolds, Math. Ann., 297 (1993), pp. 235-251.
[18] O. Kobayashi, Scalar curvature of a metric of unit volume, Math. Ann., 279 (1987), pp. 253-265.
\begin{itemize}
\item[] [19] R. Kobayashi, Einstein-Kähler V -metrics on open Satake V -surfaces with isolated quotient singularities, Math. Ann., 272 (1985), pp. 385-398.
\item[] [20] P. B. Kronheimer, Instantons gravitationnels et singularités de Klein, C. R. Acad. Sci. Paris Sér. I Math., 303 (1986), pp. 53-55.
\item[] [21] -, Minimal genus in $S^{1} \times M^{3}$, Invent. Math., 135 (1999), pp. 45-61.
[22] C. LeBrun, On the topology of self-dual 4-manifolds, Proc. Amer. Math. Soc., 98 (1986), pp. 637-640.
\item[] [23] -, Explicit self-dual metrics on $\mathbb{C P}_{2} \# \cdots \# \mathbb{C P}_{2}$, J. Differential Geom., 34 (1991), pp. 223-253.
\item[] [24] -, Polarized 4-manifolds, extremal Kähler metrics, and Seiberg-Witten theory, Math. Res. Lett., 2 (1995), pp. 653-662.
\item[] [25] -, Four-manifolds without Einstein metrics, Math. Res. Lett., 3 (1996), pp. 133-147.
\item[] [26] -, Kodaira dimension and the Yamabe problem, Comm. Anal. Geom., 7 (1999), pp. 133-156.
\item[] [27] -, Ricci curvature, minimal volumes, and Seiberg-Witten theory, Inv. Math., 145 (2001), pp. 279-316.
\item[] [28] J. Lee and T. Parker, The Yamabe problem, Bull. Am. Math. Soc., 17 (1987), pp. 37-91.
\item[] [29] J. Petean, Computations of the Yamabe invariant, Math. Res. Lett., 5 (1998), pp. 703-709.
\item[] [30] -, The Yamabe invariant of simply connected manifolds, J. Reine Angew. Math., 523 (2000), pp. 225-231.
\item[] [31] R. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, J. Differential Geom., 20 (1984), pp. 478-495.
\item[] [32] -, Variational theory for the total scalar curvature functional for Riemannian metrics and related topics, Lec. Notes Math., 1365 (1987), pp. 120-154.
\item[] [33] S. Stolz, Simply connected manifolds of positive scalar curvature, Ann. Math., (2) 136 (1992), pp. 511-540.
\end{itemize}
[34] C. H. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett., 1 (1994), pp. 809-822.
[35] J. A. Thorpe, Some remarks on the Gauss-Bonnet formula, J. Math. Mech., 18 (1969), pp. 779-786.
[36] E. Witten, Monopoles and four-manifolds, Math. Res. Lett., 1 (1994), pp. 809-822.
[37] H. Yamabe, On the deformation of Riemannian structures on compact manifolds, Osaka Math. J., 12 (1960), pp. 21-37.
[38] S.-T. Yau, Calabi's conjecture and some new results in algebraic geometry, Proc. Nat. Acad. USA, 74 (1977), pp. 1789-1799.

Masashi Ishida
Department of Mathematics, Sophia University
7-1 Kioi-Cho, Chiyoda-Ku, Tokyo, Japan 102-8554
ishida@mm.sophia.ac.jp
Claude LeBrun
Department of Mathematics, SUNY Stony Brook
Stony Brook, NY 11794-3651, USA
claude@math.sunysb.edu
Received August 1, 2002.
