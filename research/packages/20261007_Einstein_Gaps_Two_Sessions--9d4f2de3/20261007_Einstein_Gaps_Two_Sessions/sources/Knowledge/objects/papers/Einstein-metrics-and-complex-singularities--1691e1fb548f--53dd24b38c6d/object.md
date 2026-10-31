# Einstein metrics and complex singularities

- Category: papers
- Identity: arxiv:math/0206229
- Content status: fulltext_ok

---

---
source_file: math_0206229v1.pdf
converter: mathpix
format: mmd
---

\title{
EINSTEIN METRICS AND COMPLEX SINGULARITIES
}

\author{
DAVID M. J. CALDERBANK AND MICHAEL A. SINGER
}

\begin{abstract}
This paper is concerned with the construction of special metrics on non-compact 4-manifolds which arise as resolutions of complex orbifold singularities. Our study is close in spirit to the construction of the hyperkähler gravitational instantons, but we focus on a different class of singularities. We show that any resolution $X$ of an isolated cyclic quotient singularity admits a complete scalar-flat Kähler metric (which is hyperkähler if and only if $c_{1}(X)=0$ ), and that if $c_{1}(X)<0$ then $X$ also admits a complete (non-Kähler) selfdual Einstein metric of negative scalar curvature. In particular, complete self-dual Einstein metrics are constructed on simply-connected non-compact 4-manifolds with arbitrary second Betti number.

Deformations of these self-dual Einstein metrics are also constructed: they come in families parameterized, roughly speaking, by free functions of one real variable.

All the metrics constructed here are toric (that is, the isometry group contains a 2-torus) and are essentially explicit. The key to the construction is the remarkable fact that toric self-dual Einstein metrics are given quite generally in terms of linear partial differential equations on the hyperbolic plane.
\end{abstract}

\section*{1. Introduction and main theorems}

If $\Gamma$ is a finite subgroup of $S U(2)$, then the complex orbifold $\mathbb{C}^{2} / \Gamma$ has a canonical resolution $X$ with $c_{1}(X)=0$. This non-compact complex surface carries a family of asymptotically locally euclidean (ALE) hyperkähler metrics, the so-called gravitational instantons of Gibbons, Hawking, Hitchin and Kronheimer [9, 11, 17]. In this paper, we extend this picture by looking for 'optimal' metrics on complex resolutions of other surface singularities. Our methods apply to finite cyclic subgroups $\Gamma \subset U(2)$ with the property that $\mathbb{C}^{2} / \Gamma$ has an isolated singular point, the image of the origin in $\mathbb{C}^{2}$. These varieties are toric: there is a $\mathbb{C}^{\times} \times \mathbb{C}^{\times}$subgroup of $\operatorname{GL}_{2}(\mathbb{C})$ commuting with $\Gamma$, which acts on $\mathbb{C}^{2} / \Gamma$ and the resolution $X$. If $\Gamma \not \subset S U(2)$ then $c_{1}(X) \neq 0$ and so $X$ cannot carry a hyperkähler metric. However we shall find ALE Kähler metrics with zero scalar curvature, and if $c_{1}(X)$ is negative definite, complete asymptotically locally hyperbolic (ALH) self-dual Einstein metrics (with respect to the opposite orientation of $X$ ).

The situation is simplest if $\Gamma$ acts by scalar multiples of the identity on $\mathbb{C}^{2}$. Then if $|\Gamma|=p, X$ is the total space of the complex line bundle $\mathcal{O}(-p) \rightarrow \mathbb{C} P^{1}$ and for each $p$ there is a $U(2)$-invariant ALE scalar-flat Kähler (SFK) metric on $X$ : this is due to Burns if $p=1$, to Eguchi-Hanson if $p=2$, and to LeBrun for $p>2$ (see [19]). Note that among these metrics, only Eguchi-Hanson is hyperkähler, corresponding to $\Gamma=\{ \pm 1\} \subset S U(2)$. However, the Burns metric is conformal to the Fubini-Study metric on the punctured projective plane $\mathbb{C} P^{2} \backslash\{\infty\}$, which is a self-dual Einstein (SDE) metric of positive scalar curvature, whereas the LeBrun metrics are (in suitable domains) conformal to Pedersen metrics [24], which are ALH self-dual Einstein metrics of negative scalar curvature (see [12, 6]).

Our main results show that a similar picture continues to hold for more general cyclic subgroups of $U(2)$.

\footnotetext{
Date: May 2019.
}

Theorem A. Let $\Gamma \subset U(2)$ be a finite cyclic subgroup such that $0 \in \mathbb{C}^{2}$ is the only fixed point, and let $X$ be a toric resolution of $\mathbb{C}^{2} / \Gamma$. Then $X$ admits a finite-dimensional family of ALE scalar-flat Kähler metrics.

Several remarks are in order. First, this result extends to the case $\Gamma=\{1\}$, when $X$ is an iterated blow-up of $\mathbb{C}^{2}$ and the metric is asymptotically euclidean-in this form, the result is due to Joyce [15]. The above extension follows easily from Joyce's work and is also implicit in [13, 14].

Second, these metrics are given by explicit formulae and have a 2-torus $T^{2} \cong S^{1} \times S^{1}$ acting by isometries. Note that there is a minimal toric resolution $X_{0}$ of $\mathbb{C}^{2} / \Gamma$ (containing no -1 curves) such that any toric resolution of $\mathbb{C}^{2} / \Gamma$ is an iterated blow-up of $X_{0}$ at fixed points of the torus action. By the gluing theorems of Kovalev and the second author [16], there exist complete scalar-flat Kähler metrics on any iterated blow-up of $X_{0}$, but explicitness is then lost.

In our next result we find closely related non-Kähler SDE metrics, with negative scalar curvature, which may be viewed as hyperbolic analogues of the $A_{n}$ hyperkähler gravitational instantons.

Theorem B. Let $\Gamma$ and $X$ be as in Theorem $A$ and suppose that $c_{1}(X)<0$. Then there is a connected open neighbourhood $X_{+}$of the exceptional fibre $E$ of $X \rightarrow \mathbb{C}^{2} / \Gamma$ given by a smooth positive defining function $F$, with the property that for one of the metrics $g$ in Theorem A,
$$g_{+}:=F^{-2} g$$
is a complete self-dual Einstein metric with negative scalar curvature.
Here the zero-set
$$Y=\{F=0\}$$
is diffeomorphic to the link of the singularity at the origin in $\mathbb{C}^{2} / \Gamma$, which is a lens space, and $X_{+}$is diffeomorphic to $X$. We remark that the constraint $c_{1}(X)<0$ does not give a restriction on the size of $b_{2}(X)$, so this theorem supplies explicit complete Einstein metrics on a family of 4-manifolds with arbitrarily large second Betti number.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-02.jpg?height=776&width=466&top_left_y=1770&top_left_x=799}
\captionsetup{labelformat=empty}
\caption{Figure 1. The one point compactification of $X$.}
\end{figure}

The given formulation of Theorem B is designed to fit naturally with the perspective of asymptotically locally hyperbolic metrics. This is a class of complete, conformally compact metrics generalizing the classical relation
$$h=\frac{4}{\left(1-r^{2}\right)^{2}} g_{e u c}$$
between the hyperbolic metric $h$ on the open ball $\{r<1\}$ and the euclidean metric $g_{\text {euc }}$ on its closure. The key point here is that after multiplication by the square of the defining function $\left(1-r^{2}\right) / 2, h$ extends to a Riemannian metric on the boundary $\{r=1\}$. The relation (1.1) is an example of the same kind, for $g$ extends smoothly (as a Riemannian metric) to $X$.

More generally, if $M$ is a compact manifold with boundary $N$, we say that a Riemannian metric $g$ in the interior $M^{o}$ of $M$ is asymptotically locally hyperbolic (ALH) with conformal infinity $(N, c)$, if for any boundary-defining function $F, F^{2} g$ extends smoothly to $N$ and $F^{2} g$ is in the conformal class $c$. In this situation, we also say that $(M, g)$ is a filling of $(N, c)$ or that $(N, c)$ bounds $(M, g)$. Notice that the freedom to multiply defining functions by any function smooth and positive near $N$ is absorbed precisely by the specification of a conformal class rather than a metric on $N$. These ideas suggest natural boundary-value problems, such as: given $(N, c)$, does there exist a filling $(M, g)$ with $g$ and Einstein metric? If so, is $g$ unique? Following work of Fefferman-Graham, Graham-Lee, Biquard and Anderson [7, 10, 4, 1], one is beginning to have a good understanding of this problem: at least if $c$ has positive Yamabe constant, it seems that 'generically' the Einstein filling exists and is unique up to diffeomorphism, so the problem is well-posed.

If $N$ is of dimension 3, there is another boundary-value problem, namely that of filling $c$ by a self-dual or anti-self-dual Einstein metric. In so far as the Einstein problem is well-posed, this problem must be over-determined. An important step in the study of this problem is Biquard's recent proof [3] of the positive-frequency conjecture of LeBrun [18, 21]. This asserts (roughly speaking) the existence of a decomposition $c=c_{-}+c_{0}+c_{-}$(if $c$ is close to the round conformal structure $c_{0}$ on $S^{3}$ ) with the property that $c_{+}+c_{0}$ bounds a SDE metric on the ball and $c_{-}+c_{0}$ bounds an ASDE metric on the ball-equivalently $c_{+}+c_{0}$ and $c_{-}+c_{0}$ bound SDE metrics on the ball inducing opposite orientations on $S^{3}$. This is a nonlinear version of the decomposition of a function on the circle into positive and negative Fourier modes.

The metric $g_{+}$of Theorem B shows a behaviour similar to that of the standard round metric on $S^{3}$ : if ( $Y, c$ ) is the conformal infinity of $g_{+}$, then $c$ bounds the SDE metric $g_{+}$but also an SDE orbifold metric $g_{-}$(which is a cyclic quotient of a smooth metric on the ball) living on the domain $X_{-}=\{F<0\}$ (the 'other side' of $Y$ ). This picture was well known in the special case of the Pedersen-LeBrun metrics when $X$ is the total space of $\mathcal{O}(-p)$ (see e.g. [12]). It seems that there are many new phenomena worthy of exploration here, and we shall return to them in the near future.

Our next result belongs to the same circle of ideas:
Theorem C. Let $X, X_{+}$and $Y$ be as above, with $c_{1}(X)<0$. Then there exists an infinitedimensional family of conformal structures on $Y$ that bound SDE metrics on $X_{+}$.

These metrics are not as explicit as the one in Theorem B, since the required functions are in general given by integral formulae over the boundary of hyperbolic space. They are parameterized (roughly speaking) by distributions in one variable with compact support in $(-\infty, 0)$. Note also that the generic conformal structure in Theorem C will not bound an SDE orbifold metric on $X_{-}$.

Our results provide an intriguing analogue of the Kähler-Einstein trichotomy: a compact Kähler manifold $M$ can only admit a Kähler-Einstein metric if the first Chern class is positivedefinite, zero, or negative-definite, the sign of the scalar curvature being respectively positive,
zero or negative. (Moreover, thanks to the well-known work of Aubin, Calabi and Yau, the necessary conditions are also sufficient, if $c_{1}(M) \leqslant 0$.)

We have seen here that our non-compact complex surface $X$ admits a toric SDE metric of negative scalar curvature if $c_{1}(X)<0$ and admits a SDE metric of zero scalar curvature if $c_{1}(X)=0$. Of course the only compact SDE metrics of positive scalar curvature are $\mathbb{C} P^{2}$ and $S^{4}$. Since the negative-scalar-curvature SDE metrics are definitely not Kähler, it is natural to ask whether there is an underlying reason for the condition $c_{1}(X)<0$ : for example, is this a special feature of the toric symmetry of our metrics, or is there an analogous statement for general SDE metrics on these surfaces?

Although we cannot answer this question, we can provide a converse to Theorem C, as follows:

Theorem D. Let $g$ be a toric SDE metric of negative scalar curvature, defined in a connected neighbourhood $U$ of an embedded sphere $S$ consisting of special orbits of the torus action. Then $|S \cdot S| \geqslant 3$.

In particular, if $X$ is the complex manifold underlying one of the $A_{n}$ hyperkähler instantons, then $X$ does not admit a toric SDE metric of negative scalar curvature.

The methods of this paper are essentially explicit and depend crucially on the classification of toric SDE metrics of nonzero scalar curvature by Pedersen and the first author [6]. It is indeed remarkable that the torus-symmetry reduces the SDE equations to a standard linear partial differential equation in the hyperbolic plane, which can be studied relatively easily. This may be contrasted with the case of $S U(2)$ or $S O(3)$ symmetry which leads to a nonlinear ordinary differential equation [12, 25]. Solutions of the latter generally have to be written down in terms of $\vartheta$-functions.

In the first two sections we review some essential background: the geometry of resolutions of cyclic singularities from the complex and toric points of view; and the local constructions of $T^{2}$-invariant self-dual and SDE metrics. Then we move on to the proofs of the main theorems giving some examples along the way. An appendix is devoted to a brief exposition of some aspects of the geometry of hyperbolic space that were suppressed in the body of the paper.

A note on orientations. If $X$ is a complex surface, then with the standard complex orientation, a scalar-flat Kähler metric is anti-self-dual. The Fubini-Study metric on $\mathbb{C} P^{2}$, again with the standard complex orientation, is self-dual (and Einstein). In this paper are primary concern is (anti-)self-dual Einstein metrics, which generalize the Fubini-Study metric in a natural sense. We have therefore decided to state our results for self-dual metrics, which implies a reversal of the complex orientation of the complex surface $X$ in the above. We hope the reader will not find this change of orientations too tiresome.

Acknowledgements. Thanks to Henrik Pedersen, Kris Galicki, Michael Anderson and Rafe Mazzeo for helpful discussions. The first author is grateful to the Leverhulme Trust and the William Gordan Seggie Brown Trust for financial support. Both authors are members of EDGE, Research Training Network HPRN-CT-2000-00101, supported by the European Human Potential Programme

The diagrams were produced using Xfig, MAPLE and Paul Taylor's commutative diagrams package.

\section*{2. Toric topology}
2.1. Hirzebruch-Jung strings and cyclic surface singularities. Let $p$ and $q$ be coprime integers with $p>q>0$. Let $\Gamma$ be the cyclic subgroup of $U(2)$ generated by the matrix
$$\left[\begin{array}{cc}
\exp (2 \pi i / p) & 0 \\
0 & \exp (2 \pi i q / p)
\end{array}\right] .$$

The quotient $\mathbb{C}^{2} / \Gamma$ is a complex orbifold, with an isolated singular point corresponding to the origin. The resolution of this singularity by a Hirzebruch-Jung string is well known in algebraic geometry, cf. [2, §III.5], especially [2, Theorem 5.1 and Proposition 5.3]. In outline, the story is as follows. There is a minima ${ }^{1}$ resolution $\pi: X \rightarrow \mathbb{C}^{2} / \Gamma$ with the properties
\begin{itemize}
\item[(i)] $X$ is a smooth complex surface;
\item[(ii)] there is an exceptional divisor $E \subset X$ such that $\pi(E)=\{0\}$, but the restriction of $\pi$ is a biholomorphic map $X \backslash E \rightarrow \mathbb{C}^{2} / \Gamma \backslash\{0\}$;
\item[(iii)] $E=S_{1} \cup S_{2} \cup \cdots \cup S_{k}$ where the $S_{j}$ are holomorphically embedded smooth 2-spheres and the intersection matrix of the $S_{j}$ has the form
\end{itemize}
$$\left(S_{i} \cdot S_{j}\right)=\left[\begin{array}{ccccc}
-e_{1} & 1 & 0 & \cdots & 0 \\
1 & -e_{2} & 1 & \cdots & 0 \\
0 & 1 & -e_{3} & \cdots & 0 \\
\vdots & \vdots & \vdots & & \vdots \\
0 & 0 & 0 & \cdots & -e_{k}
\end{array}\right]$$
where all $e_{j} \geqslant 2$.
The integers $e_{j}$ are determined by $p$ and $q$ through the continued-fraction expansion
$$\frac{q}{p}=\frac{1}{e_{1}-} \frac{1}{e_{2}-} \cdots \frac{1}{e_{k}}$$
or equivalently by the euclidean algorithm in the form:
$$r_{-1}:=p, \quad r_{0}:=q, \quad r_{j-1}=r_{j} e_{j+1}-r_{j+1}, \quad \text { where } 0 \leqslant r_{j+1}<r_{j} .$$
Note that in this version of the division algorithm, the quotients $e_{j}$ are overestimated and since $r_{j+1}<r_{j}$, we have $e_{j} \geqslant 2$ for $j=1, \ldots k$. We remark also that the effect of reversing the order of the $e_{j}$ in this continued fraction is to replace $q / p$ by $\tilde{q} / p$, where $q \tilde{q} \equiv 1 \bmod$ $p$. This replacement in the action (2.1) does not change the orbifold singularity, just as one would expect.

By the adjunction formula, $c_{1}(X) \leqslant 0$; we have $c_{1}(X)<0$ if all $e_{j}>2$ and $c_{1}(X)=0$ if all $e_{j}=2$. In the latter case, $q=p-1, \Gamma \subset S U(2)$ and $X$ is the canonical resolution of the $A_{p-1}$ singularity.
2.2. Toric differential topology. We turn now to a discussion of 'toric' 4 -manifolds and orbifolds. These are a class of smooth 4-manifolds (orbifolds) with a given smooth action of the 2-torus $T^{2}=S^{1} \times S^{1}=\mathbb{R}^{2} / 2 \pi \mathbb{Z}^{2}$ with the property that the generic orbit is a copy of $T^{2}$. The source for this material is the paper of Orlik and Raymond [23]; the summary in [15] is also useful.

We begin with the standard action of $T^{2}$ on $\mathbb{C}^{2}=\mathbb{R}^{4}$
$$\left(t_{1}, t_{2}\right) \cdot\left(z_{1}, z_{2}\right)=\left(e^{i t_{1}} z_{1}, e^{i t_{2}} z_{2}\right)$$
where $\left(t_{1}, t_{2}\right)$ are standard coordinates on $T^{2}$. The quotient space $\mathbb{R}^{4} / T^{2}$ is easily described by introducing polar coordinates $z_{j}=r_{j} e^{i \theta_{j}}$. Then it is clear that $\mathbb{R}^{4} / T^{2}$ is the quarter-space $Q=\left\{\left(r_{1}, r_{2}\right): r_{1} \geqslant 0, r_{2} \geqslant 0\right\}$ and that the orbit corresponding to any interior point of $Q$ is a copy of $T^{2}$, while the orbits corresponding to boundary points have non-trivial stabilizers inside $T^{2}$. Since the origin is the only fixed point of this $T^{2}$-action, the stabilizer of the corner $(0,0) \in Q$ is the whole of $T^{2}$, while the stabilizer of orbits corresponding to the positive $r_{1}$ and $r_{2}$ axes are certain circle subgroups of $T^{2}$. Such circle subgroups are essential in what follows and we adopt the description of them used by Orlik and Raymond.

\footnotetext{
${ }^{1}$ i.e., any other resolution is some blow-up of this one, or equivalently, there are no (-1)-curves
}
2.2.1. Definition. For any pair of coprime integers $(m, n), G(m, n)=\left\{m t_{1}+n t_{2}=0\right\} \subset T^{2}$.

It is clear that $G(m, n)=G(\tilde{m}, \tilde{n})$ if and only if $(\tilde{m}, \tilde{n})= \pm(m, n)$.
With these conventions the stabilizer of the positive $r_{2}$-axis in $\mathbb{R}^{4}$ is $G(1,0)$ and that of the positive $r_{1}$-axis is $G(0,1)$. A complete description of the quotient space consists of the quarter space, with its two edges labelled by their stabilizers:
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-06.jpg?height=88&width=346&top_left_y=621&top_left_x=862)
Here we have opened out the quarter-space in order to simplify the diagram and have relabelled the edges (which correspond to the special orbits with circle-stabilizers) $S$ and $\tilde{S}$. It is to be understood with such diagrams that the generic orbits correspond to the upper half-space.

This $T^{2}$-action on $\mathbb{R}^{4}$ extends smoothly to the one-point compactification $S^{4}$, the point at infinity being another fixed point. The quotient $S^{4} / T^{2}$ is obtained as the one-point compactification of $Q$-it is a di-gon with two vertices and two edges labelled by $(1,0)$ and (0, 1).

Now consider the orbifold $\mathbb{R}^{4} / \Gamma$. Since the action of the finite group $\Gamma$ in (2.1) commutes with the action of $T^{2}$ on $\mathbb{R}^{4}$ it follows that $\mathbb{R}^{4} / \Gamma$ is a toric orbifold (admits an action of $T^{2}$ ). The quotient map $\mathbb{R}^{4} \rightarrow \mathbb{R}^{4} / \Gamma$ induces a map $Q \times T^{2} \rightarrow Q \times T^{2}$, which must be the identity on $Q$. The required map $T^{2} \rightarrow T^{2}$ must be surjective with kernel $\mathbb{Z}(1 / p, q / p)$ so can be taken as
$$\left(t_{1}, t_{2}\right) \mapsto\left(p t_{1}, q t_{1}-t_{2}\right) .$$
The labels $(1,0)$ and $(0,1)$ map to $(p, q)$ and $(0,-1)$ by this map, so the combinatorial picture of $\mathbb{R}^{4} / \Gamma$ is as follows:
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-06.jpg?height=88&width=346&top_left_y=1530&top_left_x=862)
The compactification $S^{4} / \Gamma$ is an orbifold with two isolated singular points and the corresponding quotient is a di-gon with edges labelled by $(p, q)$ and (0, -1).

According to Orlik and Raymond, the general picture of a smooth 4-orbifold $M$ with isolated singular points and smooth $T^{2}$-action will be modelled by the examples we have just described. More precisely, if we assume that $M$ is simply connected, then the quotient $M / T^{2}$ is topologically a closed polygon (simply connected 2-manifold with corners). A typical edge $S_{j}$ is labelled by the coprime pair ( $m_{j}, n_{j}$ ) such that $G\left(m_{j}, n_{j}\right)$ is the corresponding isotropy group. It is convenient also to label the vertex $S_{j} \cap S_{j+1}$ by the number
$$\varepsilon_{j}=m_{j} n_{j+1}-m_{j+1} n_{j}$$
so that the full picture of the boundary of $M / T^{2}$ is as follows:
$$\cdots \frac{\left(m_{j+1}, n_{j+1}\right)}{S_{j+1}} e_{S_{j}}^{\varepsilon_{j}}\left(m_{j}, n_{j}\right) \varepsilon_{j-1}\left(m_{j-1}, n_{j-1}\right) . . .$$
The union of orbits corresponding to the edge $S_{j}$ is an embedded 2-sphere in $M$ and the vertex $S_{j} \cap S_{j+1}$ is a smooth point of $M$ if $\varepsilon_{j}= \pm 1$ and is more generally an orbifold point with isotropy of order $\left|\varepsilon_{j}\right|$. Indeed the precise quotient singularity can be discovered by transforming $\left(m_{j}, n_{j}\right)$ to (0, -1) and $\left(m_{j+1}, n_{j+1}\right)$ to $(p, q), p>q>0$, by an element of $S L(2, \mathbb{Z})$, and comparing with the model described above. One of the crucial points of the work of Orlik-Raymond is the converse to the above description, namely that any diagram of the above type gives rise to a unique 4-orbifold with a given action of $T^{2}$.

The topological properties of $M$ are encoded in diagrams of the above kind. For example, let
$$e_{j}:=\varepsilon_{j-1} \varepsilon_{j}\left(m_{j-1} n_{j+1}-m_{j+1} n_{j-1}\right) .$$
Then if $\left|\varepsilon_{j-1}\right|=\left|\varepsilon_{j}\right|=1$ (and with a suitable orientation convention),
$$S_{j} \cdot S_{j}=e_{j} .$$
Notice that here we have blurred the distinction between the edge $S_{j}$ and the corresponding sphere in $M$ which lies over this edge. We shall continue with this abuse wherever convenient.
2.3. Toric resolutions of singularities. In order to resolve the singularity at the origin of $\mathbb{R}^{4} / \Gamma$
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-07.jpg?height=88&width=346&top_left_y=896&top_left_x=862)
we must replace the vertex by a chain of vertices and edges of the following kind
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-07.jpg?height=92&width=1182&top_left_y=1070&top_left_x=443)
where $\tilde{q} \equiv q(\bmod p)$ and we have used up the freedom to change bases by choosing
$$\left(m_{0}, n_{0}\right)=(0,-1), \quad\left(m_{1}, n_{1}\right)=(1,0) .$$
(This normalization, which will be convenient later, forces us to allow $q$ to be replaced by $\tilde{q}$ as above. We have also chosen all $\varepsilon_{j}=+1$, which can always be done by playing with the sign ambiguity of the $\left(m_{j}, n_{j}\right)$.)

For the rest of this paper we shall assume also that $m_{j}>0$ for $j=1, \ldots k+1$. This has the effect of making the toric resolution have semi-definite intersection-form, as follows from (2.8). Thus we make the following definition.
2.3.1. Definition. A sequence of coprime integers $\left(m_{j}, n_{j}\right)$ is called admissible if
\begin{itemize}
\item[(i)] $\left(m_{0}, n_{0}\right)=(0,-1),\left(m_{1}, n_{1}\right)=(1,0),\left(m_{k+1}, n_{k+1}\right)=(p, \tilde{q}), \tilde{q} \equiv q(\bmod p)$;
\item[(ii)] $m_{j}>0$ for $j=1,2, \ldots k+1$;
\item[(iii)] $m_{j} n_{j+1}-m_{j+1} n_{j}=1$ for $j=0,1, \ldots k$.
\end{itemize}
Then there is a one to one correspondence between admissible sequences and toric resolutions of $\mathbb{R}^{4} / \Gamma$ with semi-definite intersection form.

We note also that the compactified version of this resolution is given by the following diagram:
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-07.jpg?height=95&width=1345&top_left_y=2037&top_left_x=361)
where the point labelled $p$ is the orbifold point at infinity.
It is not difficult to check that for an admissible sequence,
$$\frac{n_{j+1}}{m_{j+1}}=\frac{1}{e_{1}-} \frac{1}{e_{2}-} \cdots \frac{1}{e_{j}} \text { for } j=1,2, \ldots k,$$
where the $e_{j}$ are defined by (2.7). Conversely, the continued-fraction expansion (2.3) defines the minimal admissible sequence and this is the toric description of the Hirzebruch-Jung string. It is not hard to check that any admissible sequence arises from the minimal one by blow-up, (i.e., by connected sum with $\mathbb{C} P^{2}$ ) which corresponds to the replacement
$$\cdots \frac{\left(m_{j+1}, n_{j+1}\right)}{S_{j+1}} \stackrel{ \pm 1}{S_{j+1}} \frac{\left(m_{j}, n_{j}\right)}{S_{j}} \cdots$$
by
$$\cdots \frac{\left(m_{j+1}, n_{j+1}\right)}{S_{j+1}} \stackrel{ \pm 1\left(m_{j+1}+m_{j}, n_{j+1}+n_{j}\right) \pm 1}{E} \stackrel{\left(m_{j}, n_{j}\right)}{E} \cdots$$
where we have labelled the exceptional divisor $E$ and have abused notation by labelling the proper transforms of $S_{j}$ and $S_{j+1}$ by the same symbols. In terms of continued fractions, this process of blowing up corresponds to the identity
$$\cdots \frac{1}{a-} \frac{1}{b-} \cdots=\cdots \frac{1}{a+1-} \frac{1}{1-} \frac{1}{b+1-} \cdots .$$
If a blow-up is performed at either end of the sequence, then $q$ will be changed by a multiple of $p$.

\section*{3. Local constructions of half-flat conformal structures}

In this section we review the local construction of half-flat conformal structures admitting two commuting Killing vectors. For more details, please see [6, 15].

\subsection*{3.1. Joyce's construction.}
3.1.1. Data.
\begin{itemize}
\item[-] $(B, h)$ is an oriented 2-manifold with metric $h$ of constant curvature -1;
\item[-] $\mathcal{W} \rightarrow B$ is the spin-bundle, viewed as a real vector bundle of rank 2 equipped with the induced metric, also denoted $h$;
\item[-] $\mathbb{V}$ is a given 2-dimensional vector space, with symplectic structure $\langle\cdot, \cdot\rangle$ and $M=B \times \mathbb{V}$ is the corresponding product bundle.
\end{itemize}
Note that $\mathbb{V}$ acts in the obvious way by translations on $M$.
Given data as above, we define a $\mathbb{V}$-invariant Riemannian metric on $M$ associated to any bundle isomorphism $\Phi: \mathcal{W} \rightarrow B \times \mathbb{V}$. Indeed, given $\Phi$, we define a family of metrics on $\mathbb{V}$, parameterized by $B$,
$$(v, \tilde{v})_{\Phi}=h\left(\Phi^{-1}(v), \Phi^{-1}(\tilde{v})\right)$$
and then a metric on the total space
$$g_{\Phi}=\Omega^{2}\left(h+(\cdot, \cdot)_{\Phi}\right)$$
where the conformal factor $\Omega>0$ is in $\mathrm{C}^{\infty}(B)$. It is clear that such a metric is invariant under the action of $\mathbb{V}$ on $M$. Any such metric also descends to the quotient $B \times(\mathbb{V} / \Lambda)$ where $\Lambda \subset \mathbb{V}$ is any lattice.

The remarkable observation of Joyce is that $g_{\Phi}$ is conformally half-flat if $\Phi$ satisfies a linear differential equation that we shall call here the Joyce equation. The Joyce equation essentially makes $\Phi$ an eigenfunction of the Dirac operator. Here we shall content ourselves with an explicit form of this equation, suitable for our later purposes. (See the appendix for a sketch of the underlying geometry.)
3.1.2. The Joyce equation. If $B \subset \mathcal{H}^{2}$ we can introduce half-space coordinates $(\rho, \eta)$, where $\rho>0$, so that
$$h=\frac{d \rho^{2}+d \eta^{2}}{\rho^{2}}$$
and an orthonormal frame $\lambda_{1}, \lambda_{2}$ of $\mathcal{W}^{*}$ with the properties
$$\lambda_{1} \otimes \lambda_{1}-\lambda_{2} \otimes \lambda_{2}=d \rho / \rho, \quad \lambda_{1} \otimes \lambda_{2}+\lambda_{2} \otimes \lambda_{1}=d \eta / \rho .$$
(From the complex point of view, $\lambda_{1}+i \lambda_{2}=\sqrt{(d \rho+i d \eta) / \rho}$.)

Since $\Phi \in \mathrm{C}^{\infty}\left(B, \mathcal{W}^{*} \otimes \mathbb{V}\right)$ we can write
$$\Phi=\lambda_{1} \otimes v_{1}+\lambda_{2} \otimes v_{2}$$
where $v_{1}$ and $v_{2}$ are in $\mathrm{C}^{\infty}(B, \mathbb{V})$. Then the Joyce equation is the system
$$\rho \partial_{\rho} v_{1}+\rho \partial_{\eta} v_{2}=v_{1}, \quad \rho \partial_{\eta} v_{1}-\rho \partial_{\rho} v_{2}=0 .$$
Clearly $\Phi$ defines a bundle isomorphism if $\left\langle v_{1}, v_{2}\right\rangle \neq 0$ and then
$$\Phi^{-1}=\frac{\left\langle v_{1}, \cdot\right\rangle \otimes \ell_{1}-\left\langle v_{2}, \cdot\right\rangle \otimes \ell_{2}}{\left\langle v_{1}, v_{2}\right\rangle},$$
where $\ell_{1}, \ell_{2}$ is the dual orthonormal frame of $\mathcal{W}$.
Let us summarize these observations.
3.1.3. Theorem. [15] With the above notation, if
$$\left\langle v_{1}, v_{2}\right\rangle \neq 0 \text { in } B$$
and $v_{1}$ and $v_{2}$ satisfy (3.6), then for any conformal factor $\Omega$, the metric
$$g_{\Phi}=\Omega^{2}\left(\frac{d \rho^{2}+d \eta^{2}}{\rho^{2}}+\frac{\left\langle v_{1}, \cdot\right\rangle^{2}+\left\langle v_{2}, \cdot\right\rangle^{2}}{\left\langle v_{1}, v_{2}\right\rangle^{2}}\right)$$
is a $\mathbb{V}$-invariant conformally half-flat metric on $M$.
3.1.4. Scalar-flat Kähler representatives. For each choice of a point $y$ on the circle at infinity of $\mathcal{H}^{2}$, there is a scalar-flat Kähler metric conformal to $g_{\Phi}$ :
$$g_{S F K}=\frac{\rho\left|\left\langle v_{1}, v_{2}\right\rangle\right|}{\rho^{2}+(\eta-y)^{2}}\left(\frac{d \rho^{2}+d \eta^{2}}{\rho^{2}}+\frac{\left\langle v_{1}, \cdot\right\rangle^{2}+\left\langle v_{2}, \cdot\right\rangle^{2}}{\left\langle v_{1}, v_{2}\right\rangle^{2}}\right) .$$
The fact that $g_{S F K}$ is a scalar-flat Kähler metric follows from [15, Proposition 2.4.4], or alternatively, as explained in [6], from the work of LeBrun [20].
3.1.5. Basic solutions of the Joyce equation. There is a basic solution of the Joyce equation (3.6)-or rather of the corresponding equation where the coefficients $v_{1}$ and $v_{2}$ are ordinary functions rather than $\mathbb{V}$-valued functions-associated to any given point $(0, y)$ of the boundary of $\mathcal{H}^{2}$ :
$$\phi(\rho, \eta ; y)=\frac{\rho \lambda_{1}+(\eta-y) \lambda_{2}}{\sqrt{\rho^{2}+(\eta-y)^{2}}} .$$
In [15] solutions of (3.6) given by finite linear combinations of the form $\phi(\rho, \eta ; y) \otimes(m, n)$ were used to construct conformally half-flat metrics on connected sums of the complex projective plane. This idea will be used in this paper too, though we shall also use suitable infinite linear combinations of these solutions to construct infinite-dimensional families of metrics.
3.1.6. Compactification. We now explain how this construction of conformally half-flat metrics is combined with the previous description of toric 4-manifolds. The main point is to give sufficient conditions for the smooth extension of the metric $g_{\Phi}$ over the special orbits at the boundary. The following sufficient conditions were given by Joyce. Consider a combinatorial diagram with labelled edges and vertices as in §2.2. Consider the boundary of $M / G$ to be identified with the boundary $\rho=0$ of $\mathcal{H}^{2}$. Then if $B$ is a neighbourhood in $\mathcal{H}^{2}$ of a point in the interior of an edge labelled $(m, n)$, the metric (3.9) extends smoothly to the special orbits over $S \cap B$ provided that
$$v_{1}=O(\rho), \quad v_{2}=(m, n)+O\left(\rho^{2}\right) \text { as } \rho \rightarrow 0$$
and
$$\rho^{-2} \Omega^{2} \text { is smooth and positive in } B \text {. }$$

Similarly, if $B$ is now a neighbourhood of a corner at $\eta=\eta_{0}$, say, then (3.9) extends smoothly to the fixed-point if in addition to the boundary conditions (3.12) and (3.13), the conformal factor is chosen so that
$$\frac{\sqrt{\rho^{2}+\left(\eta-\eta_{0}\right)^{2}}}{\rho^{2}} \Omega^{2}$$
is smooth near the corner at $\eta=\eta_{0}$.
3.1.7. Boundary behaviour of the basic solution. The basic solution $\phi(\rho, \eta ; y)$ has very simple boundary behaviour, so that the preceding sufficient conditions are easily checked for linear combinations of them:
$$\text { if } \eta \neq y, \quad \phi(\rho, \eta ; y)=O(\rho) \lambda_{1}+\left(\operatorname{sign}(\eta-y)+O\left(\rho^{2}\right)\right) \lambda_{2} \text { for small } \rho>0 .$$
3.2. Self-dual Einstein metrics. Return now to the local considerations. Suppose that $F \in \mathrm{C}^{\infty}(B)$ is an eigenfunction with eigenvalue 3/4 of the hyperbolic laplacian
$$\Delta F=\frac{3}{4} F .$$
Such a function is a potential for a Joyce matrix in the following sense. Set
$$f(\rho, \eta)=\sqrt{\rho} F(\rho, \eta), \quad v_{1}=\left(f_{\rho}, \eta f_{\rho}-\rho f_{\eta}\right), \quad v_{2}=\left(f_{\eta}, \rho f_{\rho}+\eta f_{\eta}-f\right),$$
regarded as $\mathbb{V}$-valued functions on $B$. Then, as is easily verified,
$$\Phi=\frac{1}{2}\left(\lambda_{1} \otimes v_{1}+\lambda_{2} \otimes v_{2}\right)$$
is a solution of the Joyce equation. The significance of these special solutions of Joyce's equation is as follows.
3.2.1. Theorem. [6] Let $F$ be as in (3.16) and $v_{1}$ and $v_{2}$ as in (3.18). Suppose further that
$$F^{2} \neq 4|d F|^{2}$$
in $B$. Let
$$D_{+}=\{F>0\}, \quad Z=\{F=0\}, \quad D_{-}=\{F<0\} .$$
Then the metric
$$g_{F}=\frac{\left.\left|F^{2}-4\right| d F\right|^{2} \mid}{F^{2}}\left(\frac{d \rho^{2}+d \eta^{2}}{\rho^{2}}+\frac{\left\langle v_{1}, \cdot\right\rangle^{2}+\left\langle v_{2}, \cdot\right\rangle^{2}}{\left\langle v_{1}, v_{2}\right\rangle^{2}}\right)$$
is a $\mathbb{V}$-invariant self-dual Einstein metric in $D_{+} \times \mathbb{V}$ and $D_{-} \times \mathbb{V}$ (if non-empty). The scalar curvature has the same sign as $F^{2}-4|d F|^{2}$, and conversely any $\mathbb{V}$-invariant SDE metric of nonzero scalar curvature arises (locally, and up to homothety) in this way.

Notice that $Z$ is non-empty then the scalar curvature must be negative and that (3.19) ensures that $F$ is a defining function for $Z$. Since $F^{2} g_{F}$ extends to a smooth metric in $B \times \mathbb{V}$, it is clear that $g_{F}$ is 'locally conformally compact' with $Z \times \mathbb{V}$ as its conformal infinity.
3.2.2. Basic solutions. For each $y$, the function
$$F(\rho, \eta ; y)=\frac{\sqrt{\rho^{2}+(\eta-y)^{2}}}{\sqrt{\rho}}$$
is an eigenfunction satisfying (3.16) and it is easy to check that $F(\rho, \eta ; y)$ is a potential for $\phi(\rho, \eta ; y) \otimes(1, y)$.
3.2.3. Remark. The role of $F$ as a potential for $\Phi$ relies on some geometry which we outline in the appendix. The idea is that $\mathcal{W}$ is being identified with $\mathcal{H}^{2} \times \mathbb{V}$; the derivative $d F$ of $F$ is then a section of $\mathcal{W}^{*} \otimes \mathbb{V}^{*}$, which gives a section of $\mathcal{W}^{*} \otimes \mathbb{V}$ using the symplectic form $\langle\cdot, \cdot\rangle$. Explicitly, as a section of $S^{2} \mathcal{W}^{*}, \Phi$ is given by
$$\Phi=\left(\frac{1}{2} F+\rho F_{\rho}\right) \lambda_{1} \otimes \lambda_{1}+\left(\rho F_{\eta}\right)\left(\lambda_{1} \otimes \lambda_{2}+\lambda_{2} \otimes \lambda_{1}\right)+\left(\frac{1}{2} F-\rho F_{\rho}\right) \lambda_{2} \otimes \lambda_{2} .$$
The identification of $\mathcal{W}^{*}$ with $\mathcal{H}^{2} \times \mathbb{V}$ is then obtained by setting
$$\lambda_{1}=(1 / \sqrt{\rho}, \eta / \sqrt{\rho}), \quad \lambda_{2}=(0,-\sqrt{\rho}) .$$
Notice the basic formula
$$\operatorname{det} \Phi=\frac{1}{4} F^{2}-|d F|^{2}$$
which has previously been used.
3.2.4. Example: hyperbolic space. The hyperbolic metric on the unit ball in $\mathbb{R}^{4}$ takes the form
$$g=\left(1-r_{1}^{2}-r_{2}^{2}\right)^{-2}\left(d r_{1}^{2}+d r_{2}^{2}+r_{1}^{2} d \vartheta_{1}^{2}+r_{2}^{2} d \vartheta_{2}^{2}\right)$$
in coordinates $\left(r_{1}, \vartheta_{1}\right),\left(r_{2}, \vartheta_{2}\right)$ adapted to the standard action of $G$. This metric arises in the above construction from the function
$$F=\frac{1}{2}(F(\rho, \eta ;-1)-F(\rho, \eta ; 1)) .$$

To make this explicit is a matter of direct computation, using the formula
$$\left(r_{1}+i r_{2}\right)^{2}=\frac{\eta-1+i \rho}{\eta+1+i \rho}$$
The reader may care to verify that
$$\operatorname{det} \Phi=-\frac{\rho}{\sqrt{\rho^{2}+(\eta-1)^{2}} \sqrt{\rho^{2}+(\eta+1)^{2}}}$$
and that the fibre metric (including the conformal factor) is
$$\frac{\sqrt{\rho^{2}+(\eta-1)^{2}} \sqrt{\rho^{2}+(\eta+1)^{2}}}{\left(\sqrt{\rho^{2}+(\eta-1)^{2}}-\sqrt{\rho^{2}+(\eta+1)^{2}}\right)^{2}}\left[\begin{array}{cc}
(1-u) / 2 & 0 \\
0 & (1+u) / 2
\end{array}\right]$$
where
$$u=\frac{\rho^{2}+\eta^{2}-1}{\sqrt{\rho^{2}+(\eta-1)^{2}} \sqrt{\rho^{2}+(\eta+1)^{2}}}$$
Multiplying out and changing from $(\rho, \eta)$ to $\left(r_{1}, r_{2}\right)$ yields the hyperbolic metric.

\section*{4. The SFK metrics and canonical SDE metrics}

In this section and the next, we shall prove the theorems stated in the introduction. In this section we shall give rather brief indications of the proofs of Theorems A and B (the theorems concerning the scalar-flat Kähler metrics and canonical SDE metrics associated to Hirzebruch-Jung strings). The results described here are given complete proofs, in a more general setting, in the next section. Indeed, this section can be read as a guide to the next section, as an extended set of examples.
4.1. ALE scalar-flat Kähler metrics. In order to prove Theorem A, we take up the toric description of Hirzebruch-Jung strings (and blow-ups of these strings) from §2.2. Thus we suppose given an admissible sequence ( $m_{j}, n_{j}$ ) for $j=0, \ldots k+1$, where
$$\left(m_{k+1}, n_{k+1}\right)=(p, \tilde{q}), \quad \tilde{q} \equiv q \quad(\bmod p) .$$
We supplement this by setting
$$\left(m_{k+2}, n_{k+2}\right)=-\left(m_{0}, n_{0}\right)=(0,1) .$$
Since
$$m_{j} n_{j+1}-m_{j+1} n_{j}=1 \quad(j \neq k+1), \quad m_{k+1} n_{k+2}-m_{k+2} n_{k+1}=p$$
we see that the sequence of rationals $n_{j} / m_{j}$ enjoys a monotonicity property
$$\frac{n_{j+1}}{m_{j+1}}>\frac{n_{j}}{m_{j}} \text { all } j .$$
4.1.1. Notation. Throughout this section we shall denote by $X$ the complex manifold corresponding to the data $(m, n)$-as we have seen, it is a resolution of $\mathbb{C}^{2} / \Gamma$ obtained from the minimal one by blowing up at fixed points of the $G$-action. We denote by $\bar{X}$ the one-point compactification (the added point will be denoted $\infty$ ).

Given an admissible sequence, pick real numbers $y_{0}>y_{1}>\cdots>y_{t+1}$ and define
$$\Phi(\rho, \eta)=\frac{1}{2} \sum_{j=0}^{k+1} \phi\left(\rho, \eta ; y_{j}\right) \otimes\left(m_{j}-m_{j+1}, n_{j}-n_{j+1}\right) .$$
As a finite sum of the basic solutions $\phi(\rho, \eta ; y)$, it is clear that $\Phi$ satisfies the Joyce equation and hence the metric $g_{\Phi}$ of (3.2) is a toric conformally half-flat metric wherever $\operatorname{det} \Phi \neq 0$. By resumming (4.4) in the form
$$\Phi(\rho, \eta)=\frac{1}{2} \sum_{j=0}^{k+1}\left(\phi\left(\rho, \eta ; y_{j}\right)-\phi\left(\rho, \eta ; y_{j-1}\right)\right) \otimes\left(m_{j}, n_{j}\right)$$
where we decree
$$\phi\left(\rho, \eta ; y_{-1}\right)=-\phi\left(\rho, \eta ; y_{k+1}\right),$$
it follows from [15, Lemma 3.3.2] and the monotonicity of the rationals $n_{j} / m_{j}$ that $\operatorname{det} \Phi<0$ in $\mathcal{H}^{2}$. (See also Proposition 5.1.6 below.) So $g_{\Phi}$ defines a $G$-invariant conformally half-flat metric over the whole of $G \times \mathcal{H}^{2}$. Now it follows easily from the definitions and the known boundary behaviour of $\phi(\rho, \eta ; y)$ that if $y_{j}<\eta<y_{j-1}$, then
$$\Phi(\rho, \eta)=\lambda_{1} \otimes O(\rho)+\lambda_{2} \otimes\left(\left(m_{j}, n_{j}\right)+O\left(\rho^{2}\right)\right) .$$
This is indicated by the following diagram
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-12.jpg?height=95&width=1345&top_left_y=2157&top_left_x=361)
where the labelling conventions are as in §2.2. In particular, all points save $y_{k+1}$ are smooth points of the toric manifold, while $y_{k+1}$ is an orbifold point.

It follows from this discussion and the results summarized from Joyce [15] in §3.1.6 that the conformal class defined by $g_{\Phi}$ extends as a smooth orbifold metric to $\bar{X}$. Next one checks that the 'scalar-flat Kähler' conformal factor
$$\Omega^{2}=\frac{\rho|\operatorname{det} \Phi|}{\rho^{2}+\left(\eta-y_{k+1}\right)^{2}}$$
has precisely the correct boundary behaviour so that $g_{S F K}$ of (3.10) extends smoothly to $X$.

Finally we observe (as remarked by Joyce after the proof of [15, Theorem 3.3.1]) that the conformal factor (4.8) ensures that the metric is asymptotic near $y_{k+1}$ to the flat metric on $\mathbb{R}^{4}$ near infinity. Since this is an orbifold singularity of $\bar{X}$ in general, the metric is ALE. (When there is no singularity, we recover Joyce's half conformally flat metrics on $k \mathbb{C} P^{2}$.) This proves Theorem A.

This result effectively gives a $k-1$ dimensional family of ALE scalar-flat Kähler metrics, because an equivalent metric is obtained under a projective transformation of the points $y_{0}, y_{1}, \ldots y_{k+1}$. We could equally well have assumed that the points are increasing (as does Joyce), but to assume them decreasing is more natural in the next section.
4.2. Self-dual Einstein metrics. We shall prove Theorem B using Theorem 3.2.1 [6]. We shall show that if all $e_{j} \geqslant 3$, then the Joyce matrix $\Phi$ admits a potential, for a particular choice of the $y_{j}$. For any set of real numbers $w_{j}$, the eigenfunction
$$F=\sum_{j=0}^{k+1} w_{j} F\left(\cdot ; y_{j}\right)$$
is a potential for the Joyce matrix
$$\Phi=\frac{1}{2} \sum_{j=0}^{k+1} \phi\left(\cdot ; y_{j}\right) \otimes\left(w_{j}, w_{j} y_{j}\right)$$
and this has the form (4.4) if
$$\left(m_{j}-m_{j+1}, n_{j}-n_{j+1}\right)=\left(w_{j}, w_{j} y_{j}\right) .$$
Reading this the other way, we see that the SFK metric on $X$ has (locally) a SDE representative $g_{F}$ in its conformal class, with potential given by (4.9) if and only if
$$w_{j}=\frac{1}{2}\left(m_{j}-m_{j+1}\right),$$
and the sequence $y_{0}, \ldots y_{k+1}$ determined by
$$y_{j}=\frac{n_{j+1}-n_{j}}{m_{j+1}-m_{j}}$$
is monotonic. We claim that if all $e_{j} \geqslant 3$, then the $y_{j}$ are strictly decreasing. This follows because
$$y_{j}-y_{j-1}=\frac{2-e_{j}}{\left(m_{j+1}-m_{j}\right)\left(m_{j}-m_{j-1}\right)}$$
and if all $e_{j} \geqslant 2$ then the sequence $m_{j}$ is strictly increasing.
The SDE representative is defined only where $F \neq 0$, so the next step is to analyze the zero-set of $F$. Since
$$f(\rho, \eta):=\sqrt{\rho} F(\rho, \eta)$$
is continuous up to the boundary we may define
$$Z=\{f=0\}$$
and
$$D_{+}=\{f>0\}, \quad D_{-}=\{f<0\}$$
as subsets of the conformal compactification $\overline{\mathcal{H}}^{2}:=\{\rho \geqslant 0, \eta \in \mathbb{R}\} \cup \infty$ of $\mathcal{H}^{2}$.
Notice that at any interior point of $Z$,
$$|d F|^{2}=-\operatorname{det} \Phi>0$$
so that $F$ is a defining function and $Z \cap \mathcal{H}^{2}$ is a closed submanifold of $\mathcal{H}^{2}$. We claim now that $Z$ is a simple arc joining a certain point $\left(0, \eta_{0}\right)$ to $\infty$ and intersecting no other point on the boundary of $\mathcal{H}^{2}$. First we rule out the possibility that $Z$ contains a closed $C$ curve in the interior of $\mathcal{H}^{2}$. Because $F$ is a defining function, such a curve is a smooth submanifold, and hence is simple. By the Jordan curve theorem, $C$ has an interior $U$, say and because $F$ is continuous on the compact set $U \cup C$, and is zero on the boundary, it is either identically zero or achieves a positive maximum or a negative minimum in $U$. But as a solution of $\Delta F=(3 / 4) F, F$ satisfies a strong maximum principle which rules out the last two possibilities. Hence $F=0$ in $U$, contradicting (for example) (4.18). We conclude that $Z$ consists of one or more disjoint simple arcs joining boundary points of $\mathcal{H}^{2}$.

In order to determine the end-points of $Z$, we must calculate the zeros of $f(0, \eta)$. It can be checked (see also Proposition 5.1.1) that if $y_{j}<\eta<y_{j-1}$, then
$$f_{0}(\eta):=f(0, \eta)=m_{j} \eta-n_{j} .$$
Since $m_{s} \geqslant 0, f_{0}(\eta)$ is non-decreasing in $\left(y_{s+1}, y_{s}\right)$ and since $f_{0}(\eta)$ is continuous, it follows that $f_{0}(\eta)$ is a non-decreasing function of $\eta \in \mathbb{R}$. Since $f_{0}( \pm \infty)= \pm 1$ and $f_{0}$ is strictly increasing in $\left[y_{k+1}, y_{0}\right], f_{0}(\eta)$ has a unique zero at $\eta_{0}$, say (Figure 2).

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-14.jpg?height=960&width=1083&top_left_y=1154&top_left_x=494}
\captionsetup{labelformat=empty}
\caption{Figure 2. The graph of $f_{0}$ when $q / p=3 / 8$. The zero is at 3/8.}
\end{figure}

In fact, since
$$y_{k+1}=\frac{n_{k+2}-n_{k+1}}{m_{k+2}-m_{k+1}}=\frac{q-1}{p}<\frac{q}{p}<\frac{q-n_{k}}{p-m_{k}}=\frac{n_{k+1}-n_{k}}{m_{k+1}-m_{k}}=y_{k}$$
the last inequality following from $n_{k} / m_{k}<q / p$, it follows that $\eta_{0}=q / p$ and this point lies in the interval $\left(y_{k+1}, y_{k}\right)$. Hence the boundary of $D_{+}$is equal to $(q / p, \infty)$.

Since $f$ is smooth up to the boundary near $\left(0, \eta_{0}\right), Z$ must consist of a single, simple arc joining this point to $\infty$. Indeed $\partial_{\rho} f\left(0, \eta_{0}\right)=0$ so $Z$ cuts the $\eta$-axis orthogonally. To complete the proof, we simply define $X_{ \pm}$to be the set of orbits of $X$ lying over $D_{ \pm}$and $Y$ to be the
set of orbits lying over $Z$. Then the pull-back of $f$ to $X$ is a defining function for $Y$ and the restriction $g_{+}$of $g_{F}$ to $X_{+}$is the desired complete SDE metric.

The metric $g_{F}$ extends to the special orbits because $g_{S F K}$ has this property and the ratio of the SDE and SFK conformal factors is
$$\frac{\rho F^{2}}{\rho^{2}+(\eta-(q-1) / p)^{2}}$$
which has a continuous positive limit as $\rho \rightarrow 0$ if $\eta>q / p$. This proves Theorem B.
4.2.1. Remark. As mentioned in the introduction, the restriction $g_{-}$of $g_{F}$ to $X_{-}$is also of interest. It is not difficult to check that $g_{-}$extends to a smooth orbifold metric on $X_{-}$, and passing to the universal cover we obtain a smooth ALH $\Gamma$-invariant SDE metric on the 4-ball.

This picture was well known for the special case when $X$ reduces to $\mathcal{O}(-p)$. Let us now consider these Pedersen-LeBrun metrics in more detail from this point of view.
4.2.2. Example. Here $k=1$ and there is only one parameter $p=e_{1}>0$. We have
$$\left(m_{0}, n_{0}\right)=(0,-1), \quad\left(m_{1}, n_{1}\right)=(1,0), \quad\left(m_{2}, n_{2}\right)=(p, 1), \quad\left(m_{3}, n_{3}\right)=(0,1)$$
and
$$y_{0}=1, \quad y_{1}=1 /(p-1), \quad y_{2}=0 .$$
We see at once that we must take $p \neq 2$ if the $y_{j}$ are to be distinct. This fits with the fact that when $p=2$ the scalar-flat Kähler metric is hyperkähler.

If $p>2$, then we get examples of the type discussed here, with
$$F=-F(\cdot ; 1)-(p-1) F(\cdot ; 1 /(p-1))+p F(\cdot ; 0) .$$

The case $p=1$ is a little tricky from this point of view, but by applying an orientationpreserving projective transformation, we see that we should regard the points $1, \infty, 0$ as increasing: indeed they are increasing after a cyclic permutation. Hence the Einstein metric has positive scalar curvature: it is the Fubini-Study metric on $\mathbb{C} P^{2}$ defined by
$$F=F(\cdot ; 1)+F(\cdot ; \infty)+F(\cdot ; 0)$$
where $F(\rho, \eta ; \infty):=1 / \sqrt{\rho}$.
The results of this section show that exactly the same phenomenon occurs in general, except that there are no further examples with positive scalar curvature, and in the negative scalar curvature case we need $e_{j}>2$ for all $j$.

\section*{5. Infinite-dimensional families of complete SDE metrics}

In this section, we shift viewpoint so that the 'labelling' of the edges of $M / T^{2}$ is regarded as a $\mathbb{V}$-valued step-function
$$(m(y), n(y))=\left(m_{j}, n_{j}\right) \text { for } y_{j}<y<y_{j-1}$$
where we regard $y_{k+2}=-\infty, y_{-1}=+\infty$. Then the derivative $\left(m^{\prime}, n^{\prime}\right)$ of $(m, n)$ with respect to $y$ is defined in the sense of distributions and since
$$\left(m^{\prime}, n^{\prime}\right)=\sum_{j=0}^{k+1} \delta\left(y-y_{j}\right)\left(m_{j}-m_{j+1}, n_{j}-n_{j+1}\right)$$
we see that the matrix $\Phi$ used to construct the metrics in the last section can be written
$$\Phi(\rho, \eta)=\frac{1}{2} \int \phi(\rho, \eta ; y) \otimes\left(m^{\prime}, n^{\prime}\right) d y$$
Note that we shall use 'classical' notation for distributions $\left(i . e ., \int u(y) \phi(y) d y\right.$ in place of $\langle u, \phi\rangle$ for the pairing of a distribution $u$ with a test-function $\phi$ ) throughout this section.

The theme of this section is the replacement of the step-function $(m, n)$ by more general distributions. This point of view gives a rather efficient proofs of the results outlined in the previous section, in a much more general setting.
5.1. Smeared solutions of the Joyce equation and their potentials. Let $\mu$ and $\nu$ be a pair of distributions in $\mathbb{R}$, such that
$$\left(\mu^{\prime}, \nu^{\prime}\right) \text { has compact support. }$$
Since $\phi(\rho, \eta ; y)$ is $\mathrm{C}^{\infty}$ in all variables provided that $\rho>0$,
$$\Phi(\rho, \eta)=\int \phi(\rho, \eta ; y) \otimes\left(\mu^{\prime}(y), \nu^{\prime}(y)\right) d y$$
defines a smooth Joyce matrix in $\mathcal{H}^{2}$. Similarly, if $w$ is any distribution with compact support in $\mathbb{R}$, we may define
$$F(\rho, \eta)=\int F(\rho, \eta ; y) w(y) d y$$
and this will be a smooth eigenfunction of the hyperbolic laplacian. These are the 'smeared' solutions of the title of this section. Moreover, exactly as in §4.2, (5.4) is a potential for (5.3) if
$$\mu^{\prime}(y)=w(y), \quad \nu^{\prime}(y)=y w(y) .$$

Recall that if $u$ is a distribution in one variable then $u^{\prime}=0$ (in the sense of distributions) in an open set if and only if $u$ is locally constant in this open set. Applying this to $\mu$ and $\nu$ we see that (5.2) implies that $\mu$ and $\nu$ are locally constant near infinity: we shall from now on assume that $\mu$ and $\nu$ are odd at infinity that is,
$$\mu(\infty)=-\mu(-\infty), \quad \nu(\infty)=-\nu(-\infty) .$$
We shall use this assumption to transform (5.3) and (5.4) into more convenient Poisson formulae which give $\Phi$ and $F$ in terms of their boundary values. For this we just integrate by parts once in (5.3) and twice in (5.4) to get the formulae
$$\Phi(\rho, \eta)=\frac{\rho}{2} \int \frac{(y-\eta) \lambda_{1}+\rho \lambda_{2}}{\left(\rho^{2}+(\eta-y)^{2}\right)^{3 / 2}} \otimes(\mu(y), \nu(y)) d y$$
and
$$F(\rho, \eta)=\frac{\rho^{3 / 2}}{2} \int \frac{f_{0}(y) d y}{\left(\rho^{2}+(\eta-y)^{2}\right)^{3 / 2}}$$
Here
$$f_{0}(y)=y \mu(y)-\nu(y)$$
if $w$ is related to $\mu$ and $\nu$ as in (5.5). We have already claimed that these are Poisson formulae. More precisely, we have the following result.
5.1.1. Proposition. If $\Phi$ and $F$ are given by (5.8) and (5.9) then we have (in the sense of distributions)
$$\Phi(\rho, \eta) \rightarrow \lambda_{2} \otimes(\mu(\eta), \nu(\eta)) \text { as } \rho \rightarrow 0$$
and
$$\sqrt{\rho} F(\rho, \eta) \rightarrow f_{0}(\eta) \text { as } \rho \rightarrow 0$$
where $f_{0}$ is as in (5.9). Moreover, if $(\mu, \nu)$ is constant in a neighbourhood of $\eta=a$ then
$$\Phi(\rho, \eta)=\lambda_{1} \otimes O(\rho)+\lambda_{2} \otimes\left((\mu(a), \nu(a))+O\left(\rho^{2}\right)\right)$$
and
$$f(\rho, \eta)=f_{0}(\eta)+O\left(\rho^{2}\right), f_{0}(\eta)=\eta \mu(a)-\nu(a) .$$
5.1.2. Remark. From now on, when we say that an eigenfunction $F$ has a boundary value $f_{0}$, we shall always mean (5.11).
5.1.3. Proof. We claim that
$$\lim _{\rho \rightarrow 0} \frac{\rho^{2}}{2\left(\rho^{2}+y^{2}\right)^{3 / 2}}=\delta(y)$$
and that
$$\lim _{\rho \rightarrow 0} \frac{y}{2\left(\rho^{2}+y^{2}\right)^{3 / 2}}=0$$
These two observations yield (5.10) and (5.11) (by translation of $y$ ). To establish the stated limits, test against a function $\phi$ and make the change of variables $y=\rho z$ to get
$$\int \frac{\rho^{2}}{2\left(\rho^{2}+y^{2}\right)^{3 / 2}} \phi(y) d y=\int \frac{\phi(\rho z) d z}{2\left(1+z^{2}\right)^{3 / 2}} \rightarrow \phi(0)$$
as $\rho \rightarrow 0$, since $\int\left(1+z^{2}\right)^{-3 / 2} d z=2$. Similarly
$$\int \frac{\rho y}{2\left(\rho^{2}+y^{2}\right)^{3 / 2}} \phi(y) d y=\int \frac{z \phi(\rho z) d z}{2\left(1+z^{2}\right)^{3 / 2}} \rightarrow 0$$
as $\rho \rightarrow 0$.
If now ( $\mu, \nu$ ) is constant near $\eta=a$ we can expand in powers of $\rho^{2}$ the denominator $\left(\rho^{2}+(a-y)^{2}\right)^{-1 / 2}$ in (5.3). Such an expansion is valid provided $\rho$ is smaller than the distance from $a$ to the support of $\left(\mu^{\prime}, \nu^{\prime}\right)$. This gives (5.12). A similar argument, starting from (5.4), and expanding $F(\rho, \eta ; y)$ in powers or $\rho$, yields (5.13).
5.1.4. Remark. $\Phi$ and $F$ have complete asymptotic expansions for $\rho \rightarrow 0$ whatever the behaviour of $(\mu, \nu)$ or $f$. In general, however, the next term is $\rho^{2} \log \rho$.
5.1.5. Remark. It is natural (and important) to ask what happens at $\infty$. It would be quite straightforward to analyze this separately, but it is more geometric to observe that all quantities are restrictions of globally defined objects on the boundary of $\mathcal{H}^{2}$. For example, if we set
$$\tilde{\rho}=\frac{\rho}{\rho^{2}+\eta^{2}}, \quad \tilde{\eta}=-\frac{\eta}{\rho^{2}+\eta^{2}}, \quad \tilde{y}=-\frac{1}{y}$$
then
$$\frac{\rho^{2}+(\eta-y)^{2}}{\rho}(d y)^{-1}=\frac{\tilde{\rho}^{2}+(\tilde{\eta}-\tilde{y})^{2}}{\tilde{\rho}}(d \tilde{y})^{-1} .$$
These formulae are standard in analysis on hyperbolic space and imply that the analysis near $\rho=\infty$ can be replaced by the analysis near $\tilde{\rho}=0$ which has already been done. Similarly, $\phi(\rho, \eta ; y)$ has an invariant interpretation over $\mathcal{H}^{2} \times \mathbb{R} P^{1}$ as a section (with singularities at a certain subset of the boundary) of $\mathcal{W}^{*} \otimes L$, where $L$ is the Möbius line bundle over $\mathbb{R} P^{1}$. It is the trivialization of this bundle over the complement of $\infty$ that corresponds to the 'odd at infinity' condition that is so prominent in this section. (For more on this, see also the discussion at the end of the appendix.)

We now come to a useful sufficient condition for $\operatorname{det} \Phi \neq 0$.
5.1.6. Proposition. If $\Phi$ is given by (5.7) and
$$\mu(y) \nu(z)-\mu(z) \nu(y) \leqslant 0 \text { for } y \leqslant z$$
with strict inequality for some $y<z$, then $\operatorname{det} \Phi<0$ in $\mathcal{H}^{2}$.

Note that (5.14) make good sense in terms of the tensor product of distributions even when $\mu$ and $\nu$ are not continuous functions.
5.1.7. Proof. Recall that with our orientation conventions, if
$$\Phi=\lambda_{1} \otimes v_{1}+\lambda_{2} \otimes v_{2}$$
then
$$\operatorname{det} \Phi=-\left\langle v_{1}, v_{2}\right\rangle .$$
Hence,
$$\operatorname{det} \Phi(\rho, \eta)=-\frac{\rho^{3}}{8} \iint \frac{(y-z)(\mu(y) \nu(z)-\mu(z) \nu(y))}{\left(\rho^{2}+(\eta-y)^{2}\right)^{3 / 2}\left(\rho^{2}+(\eta-z)^{2}\right)^{3 / 2}} d y d z .$$
The result follows at once.
5.1.8. Remark. If $\mu$ and $\nu$ are piecewise continuous functions with $\mu \geqslant 0$, then (5.14) is equivalent to
$$\frac{\nu(y)}{\mu(y)} \geqslant \frac{\nu(z)}{\mu(z)} \text { for } y \leqslant z$$
so that $\nu(y) / \mu(y)$ is a non-increasing function of $y$. This property is enjoyed by the stepfunction $(m, n)$ and is used in Joyce's proof of the non-vanishing of $\operatorname{det} \Phi$.
5.1.9. Remark. We have now associated to any pair of distributions $(\mu, \nu)$ on $\mathbb{R}$ that satisfy (5.2), (5.6) and (5.14) a $\mathbb{V}$-invariant conformally half-flat metric $g$ on $\mathcal{H}^{2} \times \mathbb{V}$.
5.2. Infinite-dimensional families of SDE metrics. The $\mathbb{V}$-valued step function $(m, n)$ associated to a Hirzebruch-Jung resolution $X$ with $c_{1}(X)<0$ gave rise to an eigenfunction $F$ with boundary data
$$f_{0}^{c a n}(\eta)=m_{j} \eta-n_{j} \text { for } y_{j} \leqslant \eta \leqslant y_{j-1}$$
where $y_{k+2}=-\infty$ and $y_{-1}=+\infty$ as before. In particular $f_{0}(\eta)= \pm 1$ for $\pm \eta$ sufficiently large and positive. The graph of $f_{0}$ is continuous, strictly increasing in $\left[y_{k+1}, y_{0}\right]$ and has the property that it is convex where it is negative and concave where it is positive. The unique zero of $f_{0}$ is at $\eta=q / p$. (Recall the example of Figure 2.)

In order to generate an infinite-dimensional family of complete SDE metrics on $X$, we shall change $f_{0}^{c a n}$ in the interval $(-\infty, q / p)$. (If we change it in $(q / p, \infty)$, we the result will no longer extend smoothly to the special orbits over $\left[y_{j}, y_{j-1}\right]$.) For our first statement, we consider modifications $f_{0}$ that are not too rough.
5.2.1. Theorem. Let $f_{0}(\eta)$ be a continuous function which is equal to $f_{0}^{\text {can }}$ for $\eta \geqslant q / p-\delta$, for some $\delta>0$. Suppose further that $f_{0}(\eta)=-1$ for all $\eta \leqslant a<q / p$ and that $f_{0}$ is piecewise differentiable, strictly increasing and convex on $[a, q / p]$. Then the eigenfunction $F$ with boundary value $f_{0}$ determines an asymptotically hyperbolic SDE metric on the neighbourhood $E \subset X_{+} \subset X$ of the exceptional divisor corresponding to the domain $F>0$ in $\mathcal{H}^{2}$.
5.2.2. Proof. Define
$$\mu=f_{0}^{\prime}(\eta), \quad \nu(\eta)=\eta f_{0}^{\prime}(\eta)-f_{0}(\eta) .$$
Then the distribution $(\mu, \nu)$ determines a Joyce matrix $\Phi$ by (5.7) with the correct boundary values for smooth extension to the special orbits $S_{1}, S_{2}, \ldots S_{k}$. Let us check that $\operatorname{det} \Phi$ is never zero. Since $\mu$ is defined and is positive a.e. in $\left[a, y_{0}\right]$, we can apply Proposition 5.1.6 in the form of (5.16). Indeed,
$$\frac{\nu(y)}{\mu(y)}=y-\frac{f_{0}(y)}{f_{0}^{\prime}(y)}$$
so
$$\left(\frac{\nu}{\mu}\right)^{\prime}=\frac{f_{0} f_{0}^{\prime \prime}}{\left(f_{0}^{\prime}\right)^{2}} \leqslant 0$$
by the assumption that $f_{0}$ is concave where $f_{0}>0$ and $f_{0}$ is convex where $f_{0}<0$. Hence $\nu / \mu$ is a non-increasing function as required. Thus the conformal class of $g_{\Phi}$ is defined over the whole of $T^{2} \times \mathcal{H}^{2}$. We now proceed as in §4.2.

By the maximum principle, $F$ has no interior positive maximum or negative minimum. Hence the zero-set $Z$ is a simple smooth arc joining the boundary at $\eta=q / p$ to $\infty$ and $Z$ decomposes $\overline{\mathcal{H}}^{2}$ into pieces
$$D_{+}=\{F>0\}, \quad D_{-}=\{F<0\} .$$
We define $X_{+}$to be the union of $T^{2}$-orbits over $D_{+}$and $Y$ to be the union of the $T^{2}$-orbits over $Z$. We note that as before, $X_{+}$contains $S_{1} \cup \cdots \cup S_{k}$ (since $f_{0}$ is positive to the right of $\eta=q / p$.) Then the metric $g_{F}$ defines an asymptotically hyperbolic SDE metric on $X_{+}$, with conformal infinity $Y$.
5.2.3. Remark. In the situation of Theorem 5.2.1 we can say more about the zero-set $Z$ of $F$. We claim that it meets each circular arc with end-points $(0, q / p \pm b)$ in precisely one point, for any $b>0$. To see this, note that these arcs are the orbits of the Killing vector field
$$K=\left((\eta-q / p)^{2}-b^{2}\right) \partial_{\eta}+2(\eta-q / p) \rho \partial_{\rho} .$$
Then $K F$ will be an eigenfunction of the laplacian, with eigenvalue 3/4 and so by the maximum principle, $K F<0$ in $\mathcal{H}^{2}$ if this is true near the boundary. Hence if we prove the latter, it will follow that $F$ is strictly decreasing along these circular arcs, and since it starts positive and ends negative, there must be a unique zero. By Proposition 5.1.1,
$$\sqrt{\rho} F(\rho, \eta) \simeq \eta \mu(\eta)-\nu(\eta) \quad \text { if } \rho \text { is small. }$$
Hence
$$\begin{aligned}
\sqrt{\rho} K F & \simeq(\eta-q / p)^{2} \mu(\eta)-(\eta-q / p)(\eta \mu(\eta)-\nu(\eta)) \\
& =\frac{1}{p}\left(-b^{2} \mu(\eta)+(\eta-q / p)(\mu(q / p) \nu(\eta)-\mu(\eta) \nu(q / p)) \leqslant 0\right.
\end{aligned}$$
by considering separately the cases $\eta<q / p$ and $\eta>q / p$ and using $\mu(q / p)=p$ and $\nu(q / p)=q$ as well as the monotonicity property (5.14).

Theorem 5.2.1 produces a family of SDE metrics parameterized by piecewise differentiable functions on $(-\infty, q / p)$ satisfying only monotonicity and convexity assumptions. It is clear that the space of such functions is infinite-dimensional. Hence Theorem 5.2.1 implies Theorem C. Notice that this result is not a perturbation theorem: to the left of $q / p, f_{0}$ can be far from $f_{0}^{\text {can }}$. A particularly interesting example is as follows:
5.2.4. Example. Following an initial suggestion of Atiyah, we note that the odd extension, $f_{0}^{\text {odd }}$, say, of $f_{0}^{\text {can }}$ to the left of $\eta=q / p$ satisfies all the properties of Theorem 5.2.1-see Figure 3. More precisely, for $\eta>0$, we put
$$f_{0}^{\text {odd }}(q / p-\eta)=-f_{0}^{\text {can }}(q / p+\eta)$$
so that that $(\mu, \nu)$ satisfy
$$\mu(q / p-\eta)=\mu(q / p+\eta), \quad \nu(q / p-\eta)=2 q \mu(q / p+\eta) / p-\nu(q / p+\eta) .$$
This extension enjoys the property that $F(\rho, q / p+\eta)=-F(\rho, q / p-\eta)$ so that $Z=\{\eta=q / p\}$ and $D_{+}=\{\eta>q / p\}$. In this case we can compute a representative metric $h$ for the conformal infinity by substituting $\eta=q / p$ into the formula for $F^{2} g_{F}$. Since $F$ vanishes along $\eta=q / p$, so
does its tangential derivative $F_{\rho}$-hence the conformal infinity is determined by the function $F_{\eta}(\rho, q / p)$, which is a sum of the terms
$$F_{\eta}\left(\rho, q / p ; y_{j}\right)-F_{\eta}\left(\rho, q / p ; 2 q / p-y_{j}\right)=\frac{2\left(q / p-y_{j}\right)}{\sqrt{\rho} \sqrt{\rho^{2}+\left(q / p-y_{j}\right)^{2}}}$$
over $j=0, \ldots k$ (where $y_{j}>q / p$ ). We now readily obtain
$$h=\left(\sum_{j=0}^{k} \frac{2\left(q / p-y_{j}\right) \sqrt{\rho}}{\sqrt{\rho^{2}+\left(q / p-y_{j}\right)^{2}}}\right)^{2} \frac{d \rho^{2}}{\rho^{2}}+\rho d \phi^{2}-\frac{1}{\rho}(d \psi-q / p d \phi)^{2} .$$

By definition, the odd extension has an obvious symmetry about $\eta=q / p$ and so $-f_{0}^{\text {odd }}$ should define a toric self-dual Einstein metric on a manifold $X_{-}$diffeomorphic to $X_{+}$. However, to do this, a different integral lattice is needed to define the torus-otherwise $X_{-}$will not be smooth. More precisely, the lift of the symmetry $y \mapsto 2 q / p-y$ to a matrix of determinant -1 in $\operatorname{GL}_{2}(\mathbb{R})$ is
$$\left(\begin{array}{cc}
1 & 0 \\
2 q / p & -1
\end{array}\right)=\left(\begin{array}{cc}
p & 0 \\
q & -1
\end{array}\right)\left(\begin{array}{cc}
p & 0 \\
q & 1
\end{array}\right)^{-1}$$
and the new lattice is the image of $\mathbb{Z}^{2}$ under this transformation. The two lattices have a common sublattice of index $p$, i.e., away from the fixed points there is a common covering space. We deduce that $h$ defines a conformal structure on $S^{3}$ with a $\mathbb{Z}_{p}$-quotient bounding a self-dual Einstein metric for each choice of orientation; however, the two $\mathbb{Z}_{p}$ actions are not the same!

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-20.jpg?height=962&width=1083&top_left_y=1519&top_left_x=494}
\captionsetup{labelformat=empty}
\caption{Figure 3. The graph of $f_{0}^{\text {odd }}$ when $q / p=3 / 8$.}
\end{figure}
5.3. Further results. The metrics constructed by Theorem 5.2.1 all have the property that the underlying conformal structure extends 'a long way' into $X_{-}$. More precisely the conformal structures extend to the complement of the special orbits (a set of codimension 2) in $X_{-}$. The reason for this is that we arranged $\operatorname{det} \Phi \neq 0$ over the whole of $\mathcal{H}^{2}$.

One would expect, however, that there should exist asymptotically hyperbolic SDE metrics on $X_{+}$, with conformal infinity at $Y$, but with the property that the conformal structure does not extend at all into $X_{-}$.
5.3.1. Perturbations I. Let $f_{0}$ be a function satisfying the properties of Theorem 5.2.1 and let $u$ be any distribution with compact support contained in $(-\infty, b)$, say, where $b<q / p$. Consider, for small real $t$,
$$f_{0}^{t}=f_{0}+t u$$
The eigenfunction $F^{t}$ with boundary value $f_{0}^{t}$ will be very close, in the $\mathrm{C}^{\infty}$-topology, to $F$, on any set of the form
$$\overline{\mathcal{H}}^{2} \backslash\left\{(\rho, \eta): 0 \leqslant \rho \leqslant \rho_{0} \text { and } \eta \leqslant b\right\} .$$
In particular, for all sufficiently small $t$, the zero-set of $F^{t}$ will be very close to that of $F$, and $\operatorname{det} \Phi^{t} \neq 0$ where $F^{t} \geqslant 0$. Hence $F^{t}$ yields a deformation of $g_{F}$ as an asymptotically hyperbolic SDE metric.

Note that there is now no reason why $\operatorname{det} \Phi^{t}$ should be nowhere vanishing in $\mathcal{H}^{2}$.
5.3.2. Perturbations II. A more general perturbation can be obtained from the following analytical result [22].
5.3.3. Theorem. Let $Z$ be a simple closed curve dividing $\mathcal{H}^{2}$ into two connected components $D_{ \pm}$. Denote by $\partial \mathcal{H}_{ \pm}^{2}$ the two components of the boundary of $\mathcal{H}^{2}$, so that
$$\partial D_{ \pm}=Z \cup \partial \mathcal{H}_{ \pm}^{2},$$
Then there exists a unique eigenfunction (with eigenvalue 3/4) $F$ on $D_{+}$with the property that $F=0$ on $Z$ and $F$ has prescribed boundary value
$$f_{0}(\eta)=\lim _{\rho \rightarrow 0} \sqrt{\rho} F(\rho, \eta)$$
on $\partial \mathcal{H}_{+}^{2}$.
To use this result, let $Z_{0}$ be the zero-set of an eigenfunction $F_{0}$ with boundary value $f_{0}$ satisfying the conditions of Theorem 5.2.1. Let $Z$ be a small perturbation of $Z_{0}$ (with endpoints fixed) and let $F$ be the eigenfunction, with the same boundary values as $F_{0}$ for $\eta \geqslant q / p$ and vanishing on $Z$. If $Z$ is sufficiently close to $Z_{0}$ then $F$ will be close to $F_{0}$ in $D_{+}$, and so $F^{2}-4|d F|^{2}$ will not vanish on $D_{+}$. Accordingly the metric $g_{F}$ will be an asymptotically hyperbolic SDE metric with conformal infinity on $Z$.

Notice that if $F$ extends beyond its zero-set $Z$, then the latter will be a real-analytic curve, for $F$ is real-analytic in the interior of its domain of definition. Hence if we choose $Z$ to be merely smooth, then $F$ will not extend beyond $Z$ and the conformal structure of $g_{F}$ cannot be extended through $Z$. Note that these examples fill in non-analytic conformal structures, cf. [3].

\section*{6. Proof of Theorem D}

Recall from previous sections that for an eigenfunction $F$ defined in $\mathcal{H}^{2}$, the metric $g_{F}$ extends to the special orbits over the interval $(a, b)$, with isotropy $G(m, n)$ if
$$f(\rho, \eta)=f_{0}(\eta)+\frac{1}{2} \rho^{2} f_{1}(\eta)+\cdots \quad \text { for } a<\eta<b \text { and } \rho \text { small },$$
where
$$f_{0}(\eta)=m \eta-n .$$

Furthermore, $g_{F}$ extends smoothly through the fixed-points corresponding to $a$ and $b$ if $f$ has similar expansions for $\eta$ to the left of $a$ and to the right of $b$, and $f_{0}(\eta)$ is continuous at $a$ and $b$. As a warm-up for the discussion in the rest of this section, let us give a proof of this. If $f$ has an expansion as above, then to leading order
$$v_{1}=\rho\left(f_{1}, \eta f_{1}-m\right), \quad v_{2}=(m, n)$$
and
$$\left\langle v_{1}, v_{2}\right\rangle=\rho\left(n f_{1}-m\left(\eta f_{1}-m\right)\right)=\rho\left(m^{2}-f_{0} f_{1}\right) .$$
To leading order, therefore,
$$g_{F}=\frac{\left|m^{2}-f_{0} f_{1}\right|}{f_{0}^{2}}\left(d \rho^{2}+d \eta^{2}+\frac{\left(n d \theta_{1}-m d \theta_{2}\right)^{2}+\rho^{2}\left(f_{1} d \theta_{2}+\left(m-\eta f_{1}\right) d \theta_{1}\right)^{2}}{\left(m^{2}-f_{0} f_{1}\right)^{2}}\right) .$$
Pick integers $a, b$ with $a n-m b=1$ and make the change of basis
$$d \theta_{1}=a d \phi+m d \psi, d \theta_{2}=b d \phi+n d \psi$$
so that
$$n d \theta_{1}-m d \theta_{2}=d \phi, \quad f_{1} d \theta_{2}+\left(m-\eta f_{1}\right) d \theta_{1}=\left(m^{2}-f_{0} f_{1}\right) d \psi+\left(a m-f_{1}(a \eta-b)\right) d \phi .$$
Then
$$g_{F}=\frac{\left|m^{2}-f_{0} f_{1}\right|}{f_{0}^{2}}\left(d \rho^{2}+\rho^{2} d \psi^{2}+d \eta^{2}+\text { terms in } d \phi^{2} \text { and } d \phi d \psi\right) .$$
In particular the metric in the $(\rho, \psi)$-plane is a smooth rescaling of the flat metric in polar coordinates, and hence extends to $\rho=0$.

The 'corners' are dealt with similarly, using the change of variables $\rho=2 r_{1} r_{2}, \eta=r_{1}^{2}-r_{2}^{2}$.
6.1. Outline of proof. We know that every toric SDE metric arises from a suitable function $F$. We know also that an embedded sphere consisting of special orbits must correspond to a combinatorial diagram of the form
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-22.jpg?height=92&width=511&top_left_y=1601&top_left_x=778)
where $m$ is a positive integer and we have used $S L(2, \mathbb{Z})$ invariance to fix the isotropies of $S_{0}$ an $S_{1}$. The embedded sphere here is $S_{1}$-it has self-intersection $m$, and so we must show that $m \geqslant 3$ to prove Theorem D. The eigenfunction $F$ is defined in a one-sided neighbourhood $U$ of this diagram and $U$ carries a metric $h$ of constant curvature -1. The boundary of $U$ will be divided into two pieces, $\partial U=C_{1} \cup C_{2}$ such that $C_{1}$ contains $S_{1}$ in its interior. Suppose next that we have already proved that if $g_{F}$ extends to the special orbits, then it must do so in the 'standard way'; that is, the boundary of the diagram is part of the conformal infinity of $\overline{\mathcal{H}}^{2}$ and $f$ has the above standard form near the boundary,
$$f_{0}(\eta)= \begin{cases}m \eta-1 & \text { if } \eta<y_{1} ; \\ \eta & \text { if } y_{1}<\eta<y_{0} ; \quad f_{0} \text { continuous at } y_{0} \text { and } y_{1} . \\ 1 & \text { if } y_{0}<\eta .\end{cases}$$
The continuity at $y_{0}$ and $y_{1}$ implies
$$y_{1}=1 /(m-1), \quad y_{0}=1$$
if $m \neq 1$. The result follows now because if $m=2$ then $y_{0}=y_{1}$, which is not allowed, and if $m<1$, then $y_{1}<0$ and $F$ changes sign near $S_{1}$, so the corresponding SDE metric blows up there. The case $m=1$ is a little tricky with this normalization, reflecting a poor choice of basis (or point at infinity) in this case. However if we switch to
![](https://cdn.mathpix.com/cropped/bce67c1c-46f9-41af-b1f3-689607b93c3f-22.jpg?height=90&width=511&top_left_y=2565&top_left_x=778)
then continuity gives $y_{1}=0, y_{0}=1$ and
$$f(0, \eta)= \begin{cases}\eta-1 & \text { if } \eta<0 \\ 2 \eta-1 & \text { if } 0<\eta<1 \\ \eta & \text { if } \eta>1\end{cases}$$
so that $f$ changes sign in the middle of $S_{1}$. Hence this cannot happen for the same reason as before. It is good to note that we do not rule out the existence of the standard metrics on $S^{4}$ and $\mathbb{C} P^{2}$ this way. The reason for this is that those metrics have positive scalar curvature, so $\operatorname{det} \Phi>0$ and the points $y_{0}$ and $y_{1}$ come in the opposite order.

The next several sections are therefore devoted to the proof that if $g_{F}$ has negative scalar curvature, then the only way in which $g_{F}$ can extend smoothly to the special orbits, is the 'standard way' described above.
6.2. Fermi coordinates. Near any point of $S$ we can introduce Fermi coordinates. For $p$ near $S$, we write $r(p)$ for the distance from $p$ to $S$ and use an angular coordinate $\theta$ in the normal bundle of $S$ in $X$. The metric takes the form
$$d r^{2}+r^{2} d \theta^{2}+h_{1}+r h_{2}+r^{2} h_{3}$$
where $h_{1}$ is the 'first fundamental form' (restriction of the metric to $S$ ), $h_{2}$ is the second fundamental form, and $h_{3}$ is a form on $T X$ bilinear in $r d \theta$ and $T S$. By Gauss's lemma, $h_{3}$ does not contain terms in $d r$, though we shall not use this.

Since $S$ is a the fixed-point set of an isometry, the second fundamental form $h_{2}$ is actually zero, but again, we shall not need this precision.

In our case, we can choose another angular variable $\phi \in T^{2}$ as one of the coordinates in $S$; complete the set with $y$. Then to leading order in $r$, we have, near some given point of $S$,
$$g=d r^{2}+d y^{2}+r^{2} d \theta^{2}+a^{2} d \phi^{2}$$
where $a>0$ at $r=0$. We shall now compare this with the metric $g_{F}$.
From §3.2, if $g_{F}$ has negative scalar curvature,
$$g_{F}=\frac{\rho\left(f_{\rho}^{2}+f_{\eta}^{2}\right)-f f_{\rho}}{\rho f^{2}}\left(d \rho^{2}+d \eta^{2}\right)+\frac{\rho}{f^{2}} \frac{1}{\rho\left(f_{\rho}^{2}+f_{\eta}^{2}\right)-f f_{\rho}}\left(d \psi_{1}, d \psi_{2}\right) P^{t} P\binom{d \psi_{1}}{d \psi_{2}}$$
where
$$P=\left(\begin{array}{cc}
\rho f_{\eta}-\eta f_{\rho} & f_{\rho} \\
f-\rho f_{\rho}-\eta f_{\eta} & f_{\eta}
\end{array}\right) .$$
We shall equate the fibre part of this to the 'angular part' of (6.2) and work to leading order in $r$. We shall not divide by any quantity tending to zero with $r$ at this stage, so we can afford to ignore the higher-order corrections to the metric. Since
$$\operatorname{det} P=\rho\left(f_{\rho}^{2}+f_{\eta}^{2}\right)-f f_{\rho}$$
we can write this equation as
$$\frac{\rho}{f^{2}} \frac{1}{\operatorname{det} P} P^{t} P=\left(\begin{array}{cc}
a^{2} & 0 \\
0 & r^{2}
\end{array}\right)+\cdots .$$
It follows that
$$R:=\frac{1}{f} \frac{\sqrt{\rho}}{\sqrt{\operatorname{det} P}} P\left(\begin{array}{cc}
a^{-1} & 0 \\
0 & r^{-1}
\end{array}\right)+\cdots$$
is an orthogonal matrix. In fact $\operatorname{det} R=1$ so we may write
$$R=\left(\begin{array}{cc}
c & s \\
-s & c
\end{array}\right), \quad c^{2}+s^{2}=1 .$$

Hence we find
$$\frac{\sqrt{\rho}}{f \sqrt{\operatorname{det} P}}\left(\begin{array}{cc}
\rho f_{\eta}-\eta f_{\rho} & f_{\rho} \\
f-\rho f_{\rho}-\eta f_{\eta} & f_{\eta}
\end{array}\right)=\left(\begin{array}{cc}
c a & s r \\
-s a & c r
\end{array}\right)+\cdots .$$
This equation contains most of the information needed to prove Theorem D. To get our hands on it we proceed as follows: eliminate $f_{\rho}$ and $f_{\eta}$ between the (1,1), $(1,2)$ and (2,2) components of this equation, to obtain
$$(r \rho-a) c=r \eta s$$
and hence
$$c=\frac{r \eta}{\sqrt{(r \rho-a)^{2}+r^{2} \eta^{2}}}+\cdots, \quad s=\frac{r \rho-a}{\sqrt{(r \rho-a)^{2}+r^{2} \eta^{2}}}+\cdots .$$
Next, eliminate $f_{\rho}$ and $f_{\eta}$ between the ( 1,2 ), ( 2,2 ) and ( 2,1 ) components of this equation, to obtain
$$\frac{\sqrt{\rho}}{\sqrt{\operatorname{det} P}}-r \rho s-r \eta c=-s a$$
so that
$$\frac{\sqrt{\rho}}{\sqrt{\operatorname{det} P}}=\sqrt{(r \rho-a)^{2}+r^{2} \eta^{2}}+\cdots$$
Finally, we note by taking the determinant of (6.6),
$$\frac{\rho}{f^{2}}=a r+\cdots .$$
6.3. Proof that the special orbits are at $\rho=0$. Select a point $p$ on $S$ and suppose that the orbit over $p$ corresponds to the point $\left(\rho_{0}, \eta_{0}\right)$ in the closure of the upper half-plane. Suppose for a contradiction that we have $\rho_{0}>0$.

It follows from (6.8) that $\sqrt{\rho / \operatorname{det} P}$ is bounded away from zero and infinity in the limit. Hence, from the second column of (6.6) it follows that $\partial_{\rho} \log f$ and $\partial_{\eta} \log f$ remain bounded on approach to $\left(\rho_{0}, \eta_{0}\right)$. Hence $\log f$ is bounded there and so $f$ is bounded away from 0 and $\infty$ there. This now contradicts (6.9) which requires $f \rightarrow \infty$ on approach to $\left(\rho_{0}, \eta_{0}\right)$.
6.4. Boundary behaviour of $f$. We now know that $\rho \rightarrow 0$ as $r \rightarrow 0$. Repeating the arguments of the previous subsection (but now with $\rho_{0}=0$ ), we see that $\partial_{\rho} \log f$ and $\partial_{\eta} \log f$ both tend to zero as $\rho \rightarrow 0$. In fact, we obtain
$$f(\rho, \eta)=A+\frac{1}{2} \rho^{2} f_{1}(\eta)+\cdots$$
where $A$ is constant and $f_{1}$ is some function of $\eta$. From (6.8), we see also that, to leading order in $\rho$,
$$\frac{\operatorname{det} P}{\rho}=\frac{1}{a^{2}},$$
and from (6.9)
$$a d r=d \rho / A^{2} .$$
Hence by comparing coefficients of $d r^{2}$ in (6.2) and (6.3),
$$1=\frac{1}{A^{2} a^{2}}\left(A^{2} a\right)^{2}=A^{2} .$$
Hence $A=1$ since we are assuming (as we can) that $f>0$ near $\rho=0$.
6.4.1. Remark. If the isotropy is assumed to be $G(m, n)$ then we would have found $f(\rho, \eta)=$ $m \eta-n+\frac{1}{2} \rho^{2} f_{1}(\eta)$ instead. That is, we have recovered the 'standard situation' described at the beginning of this section.
6.5. Corner behaviour of $f$. We have now established that $f_{0}$ has the 'standard behaviour' (6.1) away from the corners $y_{0}$ and $y_{1}$. It remains to show that $f_{0}$ is continuous at these points. To do this, we repeat the discussion above, but with the metric expanded about the point $S_{0} \cap S_{1}$. It is now natural to introduce parameters $r_{0}$ and $r_{1}$, the distance functions from $S_{0}$ and $S_{1}$ respectively. Since $S_{0}$ and $S_{1}$ are totally geodesic, the restriction of $r_{1}$ to $S_{0}$ is also the distance function from the point $S_{0} \cap S_{1}$ and similarly for $r_{0}$. Therefore the metric takes the form
$$g=d r_{0}^{2}+d r_{1}^{2}+r_{0}^{2} d \vartheta_{0}^{2}+r_{1}^{2} d \vartheta_{1}^{2}+\cdots$$
where ⋯ denotes terms of higher order. If we carry through the calculations of §6.2 with this metric, then we obtain the formulae
$$\begin{aligned}
\frac{\rho}{f^{2}} & =r_{0} r_{1}+\cdots \\
(\log f)_{\rho} & =\frac{r_{1}^{2} \rho-r_{0} r_{1}}{r_{1}^{2} \eta^{2}+\left(r_{0}-r_{1} \rho\right)^{2}}+\cdots \\
(\log f)_{\eta} & =\frac{r_{1}^{2} \eta}{r_{1}^{2} \eta^{2}+\left(r_{0}-r_{1} \rho\right)^{2}}+\cdots
\end{aligned}$$
Let the corner correspond to $\eta=\eta_{0}$. We shall investigate the behaviour of $\log f$ in polar coordinates centred at $\left(0, \eta_{0}\right)$, by introducing
$$\eta-\eta_{0}=R \cos \Theta, \quad \rho=R \sin \Theta .$$
Then
$$\partial_{R} \log f=\cos \Theta \partial_{\eta} \log f+\sin \Theta \partial_{\rho} \log f$$
and this is uniformly bounded for any fixed $\Theta$ by (6.14) and (6.15). Hence $f(R, \Theta)$ has a limit as $R \rightarrow 0$, for each fixed $\Theta$. To see that these limits are independent of $\Theta$, we note that
$$\partial_{\Theta} \log f=R\left(-\sin \Theta \partial_{\eta}+\cos \Theta \partial_{\rho}\right) \log f$$
and the right hand side is $O(R)$, uniformly in $\Theta$. Hence
$$|f(R, 0)-f(R, \pi)|=O(R)$$
and this shows that $f$ is continuous at the corner, by taking $R \rightarrow 0$. In view of the discussion in §6.1, the proof of Theorem D is now complete.

\section*{Appendix}

In this appendix we explain the geometric origin of the basic solutions that we have used in this paper. Much of the discussion goes through for hyperbolic space of arbitrary dimension, but we shall confine ourselves to $\mathcal{H}^{2}$. As in [6], we shall fix a 2-dimensional symplectic vector space $\mathbb{W}$ and consider the symmetric square $S^{2} \mathbb{W}$, equipped with the quadratic form det as a 3-dimensional Minkowksi space. If $g \in S L(\mathbb{W}), x \in S^{2} \mathbb{W}$, then $g \cdot x=g x g^{t}$ is evidently an isometric action, corresponding to the double cover of the identity component of $S O(1,2)$ by $S L_{2}(\mathbb{R})$.

The hyperbolic plane $\mathcal{H}^{2}$ appears as (one sheet of) the hyperboloid $\operatorname{det} x=1$ or essentially equivalently as the projective space $S_{+} / \mathbb{R}^{\times}$where
$$S_{+}=\left\{x \in S^{2} \mathbb{W}: \operatorname{det} x>0\right\}$$
(and $\mathbb{R}^{\times}$stands for the multiplicative group of nonzero real numbers). It is easy to check that there is a natural correspondence
$$\left\{f \in \mathrm{C}^{\infty}\left(S_{+}\right): \square f=0, \quad E \cdot f=\alpha f\right\}=\left\{g \in \mathrm{C}^{\infty}\left(\mathcal{H}^{2}\right): \Delta g=\alpha(\alpha+1) g\right\},$$
where $E$ is the Euler homogeneity operator on $S^{2} \mathbb{W}$ and □ is the wave operator of $S^{2} \mathbb{W}$. If $N$ is any nonzero null vector ( $\operatorname{det} N=0$ ), then $x \mapsto f(N \cdot x)$ is a solution of the wave equation,
for any function $f$. The 'basic solutions' of the equation $\Delta F=(3 / 4) F$ arise in precisely this way, with the simplest possible function homogeneous of degree 1/2, namely $(N \cdot x)^{1 / 2}$.

If we represent $N=n \otimes n$ where $n=(1, y)$ and use the parameterization of the hyperboloid by half-space coordinates
$$x=\frac{1}{\rho}\left[\begin{array}{cc}
1 & \eta \\
\eta & \rho^{2}+\eta^{2}
\end{array}\right]$$
then
$$\sqrt{N \cdot x}=\sqrt{n x^{-1} n^{t}}=\frac{\sqrt{\rho^{2}+(\eta-y)^{2}}}{\sqrt{\rho}}$$
which is the 'basic solution' $F(\rho, \eta ; y)$ of (3.21).
Just as eigenfunctions of the laplacian in $\mathcal{H}^{2}$ correspond to homogeneous solutions of the wave equation in $S_{+}$, so eigenfunctions of the Dirac operator in $\mathcal{H}^{2}$ correspond to homogeneous solutions of the Dirac equation in $S_{+}$. Here we can identify the product bundle $S_{+} \times \mathbb{W}$ as the spin-bundle of $S_{+}$; its restriction to the hyperboloid is naturally isomorphic to the spin-bundle of $\mathcal{H}^{2}$ (though the induced metric at $x$ is given by $x^{-1}$ ). It is easy to check that if $N=n \otimes n$ as before, then the $\mathbb{W}$-valued function $n / \sqrt{N \cdot x}$ is a solution of the minkowskian Dirac equation. This descends to the 'basic solution' of the Joyce equation $\phi(\rho, \eta ; y)$ (3.11) after replacing $n$ by the dual vector $n^{*},\langle n, u\rangle=n^{*}(u)$. (Explicitly, if $n=(1, y)$ then $n^{*}=(-y, 1)$.)

Over the conformal boundary $\mathbb{R} P^{1}$ of $\mathcal{H}^{2}$ there is a family of homogeneous line bundles. In terms of the parameter $n \in \mathbb{W}$, we define the bundle $L$ as corresponding to functions homogeneous of degree 1,
$$f(\lambda n)=\lambda f(n), \lambda \neq 0,$$
and $|L|$ to correspond to functions homogeneous in the sense
$$f(\lambda n)=|\lambda| f(n), \lambda \neq 0 .$$
Notice that $|L|$ can be raised to any real or complex power, while $L$ can be raised only to integral powers, and that $L^{2}=|L|^{2}$. (Topologically, $|L|$ is trivial, but $L$ is the Möbius bundle.) These considerations are important in trying to find the correct interpretation of the formulae for the smeared solutions in §5.1. If $M \rightarrow \mathbb{R} P^{1}$ is a given line bundle, then by a distributional section of $M$ we mean a continuous linear functional on the space $\mathrm{C}^{\infty}\left(\mathbb{R} P^{1}, M^{*} \otimes \Omega\right)$. Here $\Omega$ is the bundle of densities, which can be identified invariantly with $L^{-2}$. In so far as $\sqrt{N \cdot x}$ is a section of $|L|$ for each fixed $x$, it follows that if $u$ is a distributional section of $L^{-2} \otimes|L|^{-1}$ then
$$\int u(n) \sqrt{N \cdot x}$$
is a well-defined function of $x$. This is the $S L_{2}(\mathbb{R})$-invariant interpretation of formula (5.4). The formula (5.3) has a similar interpretation. The ubiquitous 'odd at infinity' condition appears, from this point of view, from a trivialization of the Möbius bundle $L$ over $\mathbb{R} P^{1} \backslash\{\infty\}$.

\section*{References}
\begin{itemize}
\item[] [1] M. T. Anderson, Einstein metrics with prescribed conformal infinity on 4-manifolds, Preprint, SUNY Stonybrook (2001), math.DG/0105243.
\item[] [2] W. Barth, C. Peters and A. V. de Ven, Compact Complex Surfaces, Springer-Verlag, Berlin Heidelberg New York Tokyo (1984).
\item[] [3] O. Biquard, Métriques autoduales sur la boule, Preprint, IRMA Strasbourg (2000), math.DG/0010188.
\item[] [4] O. Biquard, Métriques d'Einstein asymptotiquement symétriques, Astérisque 265 (2000).
\item[] [5] C. P. Boyer, K. Galicki, B. M. Mann and E. G. Rees, Compact 3-Sasakian 7-manifolds with arbitrary second Betti number, Invent. Math. 131 (1998) 321-344.
\end{itemize}
\begin{itemize}
\item[] [6] D. M. J. Calderbank and H. Pedersen, Selfdual Einstein metrics with torus symmetry, Preprint MS-00-22, University of Edinburgh (2001), math.DG/0105263.
\item[] [7] C. Fefferman and C. R. Graham, Conformal invariants, in The Mathematical Heritage of Élie Cartan (Lyon, 1984), Astérisque (1985), pp. 95-116.
\item[] [8] K. Galicki, Multi-centre metrics with negative cosmological constant, Class. Quantum Grav. 8 (1991) 1529-1543.
\item[] [9] G. W. Gibbons and S. W. Hawking, Gravitational multi-instantons, Phys. Lett. B 78 (1978) 430-432.
\item[] [10] C. R. Graham and J. M. Lee, Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991) 186-225.
\item[] [11] N. J. Hitchin, Polygons and gravitons, Math. Proc. Camb. Phil. Soc. 85 (1979) 465-476.
\item[] [12] N. J. Hitchin, Twistor spaces, Einstein metrics and isomonodromic deformations, J. Diff. Geom. 42 (1995) 30-112.
\item[] [13] D. D. Joyce, The hypercomplex quotient and the quaternionic quotient, Math. Ann. 290 (1991) 323-340.
\item[] [14] D. D. Joyce, Quotient constructions for compact self-dual 4-manifolds, Merton College, Oxford (1991).
\item[] [15] D. D. Joyce, Explicit construction of self-dual 4-manifolds, Duke Math. J. 77 (1995) 519-552.
\item[] [16] A. G. Kovalev and M. A. Singer, Gluing theorems for complete anti-self-dual spaces, Geom. Funct. Anal. 11 (2001) 1229-1281.
\item[] [17] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Diff. Geom. 29 (1989) 665-683.
\item[] [18] C. R. LeBrun, $\mathcal{H}$-space with a cosmological constant, Proc. Roy. Soc. London A 380 (1982) 171-185.
\item[] [19] C. R. LeBrun, Counterexamples to the generalized positive action conjecture, Comm. Math. Phys. 118 (1988) 591-596.
\item[] [20] C. R. LeBrun, Explicit self-dual metrics on $\mathrm{CP}^{2} \# \cdots \# \mathbb{C} P^{2}$, J. Diff. Geom. 34 (1991) 223-253.
\item[] [21] C. R. LeBrun, On complete quaternionic-Kähler manifolds, Duke Math. J. 63 (1991) 723-743.
\item[] [22] R. R. Mazzeo, Private communication.
\item[] [23] P. Orlik and F. Raymond, Actions of the torus on 4-manifolds I, Trans. Amer. Math. Soc. 152 (1970) 531-559.
\item[] [24] H. Pedersen, Einstein metrics, spinning top motions and monopoles, Math. Ann. 274 (1986) 35-39.
\item[] [25] K. P. Tod, Self-dual Einstein metrics from the Painlevé VI equation, Phys. Lett. A 190 (1994) 221-224.
\end{itemize}

Department of Mathematics and Statistics, University of Edinburgh, King's Buildings, Mayfield Road, Edinburgh EH9 3JZ, Scotland.
E-mail address: davidmjc@maths.ed.ac.uk
E-mail address: michael@maths.ed.ac.uk
