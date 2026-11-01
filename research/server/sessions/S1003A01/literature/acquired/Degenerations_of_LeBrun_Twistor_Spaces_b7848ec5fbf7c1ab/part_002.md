---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Degenerations of LeBrun Twistor Spaces]

Next we show that if we pull-back the family $q: \mathscr{Z} \rightarrow \mathscr{Q}$ to $Q \times \mathbb{C}^{*}$ by the trivializing map $\phi$ (see (4.4)), then on the central fiber there appears the twistor space of the LeBrun metric on $\mathscr{O}(-n)$. For this, if we put $u=x_{2} /\left(s x_{0}-x_{1}\right)$ and $v=x_{3} /\left(s x_{0}-x_{1}\right)$, then by a simple computation, on the quadric $Q_{s}(s \neq 0)$, we have
$$\left(x_{0}, x_{1}, x_{2}, x_{3}\right)=(u v+1, s(u v-1), 2 s u, 2 s v) .$$
On the other hand, by Lemma 4.2, the plane $H_{i}$ is defined by the equation (4.8) with the coefficients $b, c$ replaced by $b_{i}, c_{i}$, where $\left(b_{i}, c_{i}\right) \in \mathbb{R} \times \mathbb{C}$ satisfies the inequality (4.9). Substituting (4.15) to the equation of $H_{i}$, we get
$$\left(1-b_{i} s\right) u v-2 s c_{i} u-2 s \bar{c}_{i} v+\left(1+b_{i} s\right)=0 .$$
Let $\tilde{h}_{i}=\tilde{h}_{i}(u, v, s)$ be the left-hand side of (4.16). Then $\tilde{h}_{i}$ is a defining equation of the divisor $\phi^{-1}\left(H_{i}\right)$ in $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C} \mathbb{P}^{1} \times \mathbb{C}$. Therefore, the pull-back family $\phi^{*} \mathscr{Z} \rightarrow \mathbb{C} \mathbb{P}^{1} \times \mathbb{C} \mathbb{P}^{1} \times \mathbb{C}$ is given by the equation
$$x y=\tilde{h}_{1} \tilde{h}_{2} \cdots \tilde{h}_{n},$$
where $(x, y) \in \mathscr{O}(n-1,1) \oplus \mathscr{O}(1, n-1)$ by Lemma 4.1 as before. Then by (4.16), the defining equation of the inverse image of $\mathbb{C P}^{1} \times \mathbb{C P}^{1} \times\{0\}$ (under the projection $\phi^{*} \mathscr{Z} \rightarrow$ $\mathbb{C} \mathbb{P}^{1} \times \mathbb{C P}^{1} \times \mathbb{C}$ ) is given by
$$x y=(u v+1)^{n} .$$
By Theorem 3.3, this is exactly the defining equation of (a Zariski open subset of) the twistor space of the LeBrun metric on $\mathscr{O}(-n)$, as required.

If one wants not a subset but the entire twistor space, it is enough to compactify the fibers of the family $\mathscr{Z}(\rightarrow \mathscr{Q}) \rightarrow \mathbb{C}$ by considering the projective bundle $\mathbb{P}\left(\mathscr{L}_{1} \oplus \mathscr{L}_{2} \oplus \mathscr{O}\right)$ instead of $\mathscr{L}_{1} \oplus \mathscr{L}_{2}$, and pull it back by $\phi$.

\section*{5. Discussions about degenerations of the metrics}

So far we have studied degenerations of twistor spaces. But originally these are of course motivated by understanding degenerations of (anti)-self-dual metrics or conformal classes on the 4 -manifolds. In this final section we briefly discuss what happens for base 4 -manifolds, by picking up Kähler representatives of the conformal classes on (dense) open subsets of the 4-manifolds. For a thorough investigation in this direction, we refer a paper by Viaclovsky [12].

We recall that LeBrun [7] first constructs a scalar-flat Kähler metric on a collinear blow-up of $\mathbb{C}^{2}$ explicitly, and then verifies that the metric can be extended to a one point compactification after adjusting a conformal gauge. Here for avoiding confusion we call these scalar flat Kähler metrics as LeBrun metrics.

As showed by Tian-Viaclovsky [11, Theorem 1.1], any sequence of complete Kähler metrics with constant scalar curvature on a 4-manifold satisfying some boundedness condition on the curvature tensor and Sobolev constants has a converging subsequence with the limit being a Kähler orbifold, where the convergence is in the Gromov-Hausdorff sense as pointed spaces. For avoiding confusion with monopole centers, we refer the point of pointed spaces as a base point.

Let $\left\{\left\{p_{i 1}, p_{i 2}, \cdots, p_{i n}\right\} \subset \mathscr{H}^{3} \mid i=1,2, \cdots\right\}$ be a sequence of $n$ points on the hyperbolic space, and $\left\{g_{i}\right\}$ the sequence of the LeBrun metrics which have these $n$ points as the set of monopole points. First as in Section 2 we consider the situation that the first point $p_{i 1}$ goes to infinity as $i \rightarrow \infty$ while the remaining $(n-1)$ points stay fixed. Then if we take a compact domain $K \subset \mathscr{H}^{3}$ and if we choose as a base point a point $q_{i}$ which belongs to the subset over $K$, then since the Green function centered at $p_{i 1}$ tends to zero as $i \rightarrow \infty$ on the $R$-ball centered at $q_{i}$ for any $R>0$, the space with LeBrun metric $g_{i}$ converges to the space equipped with the LeBrun metric having the fixed $(n-1)$ points as the set of monopole points. The degeneration from $n \mathbb{C P}^{2}$ to $(n-1) \mathbb{C P}^{2}$ constructed in Section 2 is the twistor translation of this degeneration.

Next consider the same sequence of $n$ points as in the previous paragraph but this time as base points we choose the moving point $p_{i 1}$, viewed as a point on $n \mathbb{C P}^{2}$. Then since the distance between the fixed $(n-1)$ points and the base point goes to infinity as $i \rightarrow \infty$, the limit as pointed space should be the space equipped with the LeBrun metric with one monopole point; namely the Burns metric. This is rather the space which disappeared in the last degeneration, and thus changing a base point can give a different limit.

Also it is natural to expect that in the degeneration of the twistor spaces constructed in Section 2, at the limit (central fiber), we find not only a twistor space of $(n-1) \mathbb{C P}^{2}$ but also the twistor space of Fubini-Study metric (which is a conformal compactification of the Burns metric). However, even if we regard our degeneration as a family $\mathscr{Z} \rightarrow \mathbb{C}(\lambda)$ and try to perform the birational transformations within the 4-fold $\mathscr{L}$, I could not find the flag twistor space at the central fiber. We note that the existence of such a model is guaranteed by the framework of Donaldson-Friedman [2]. If one can find the flag twistor space at the central fiber of the family, it provides an explicit realization of the Donaldson-Friedman model for the case of the present degeneration, not relying on deformation theory of complex spaces.

Next in accordance with the degeneration taken up in Section 3 we consider the sequence $\left\{\left\{p_{i 1}, p_{i 2}, \cdots, p_{i n}\right\} \subset \mathscr{H}^{3} \mid i=1,2, \cdots\right\}$ of $n$ points for which all $p_{i j}$-s approach to a point $p \in \mathscr{H}^{3}$ as $i \rightarrow \infty$. In this case, as was explicitly shown in coordinates by LeBrun [7, page 235-236], the limit is a space equipped with the LeBrun's scalar flat Kähler metric on $\mathscr{O}(-n)$. However we note that we have to choose a conformal gauge which is different from the above LeBrun metrics on the collinear blowup of $\mathbb{C}^{2}$; instead another Kähler representative found in [7, page 243-244] has to be chosen to get the above limit.

As was discovered in [7, page 236-237], if we look at this degeneration more carefully, it provides a typical example of bubbling off phenomena of ALE spaces. Namely, when all the monopole points $p_{i 1}, \cdots, p_{i n}$ of LeBrun metrics become closer to a point $p \in \mathscr{H}^{3}$ in such a way that their angular positions relative to $p$ as well as the ratio of the distances from $p$ are preserved, around the point $p$ we make a sequence of rescalings in a way that the distances from $p$ become constant. Then at the limit the curvature of the hyperbolic space becomes zero and as a result a Gibbons-Hawking space with $n$ monopole points on $\mathbb{R}^{3}$ bubble off from the point $p$.

To understand this bubble off through our degeneration of the twistor spaces constructed in Section 4, for each $s \in \mathbb{R}$ with $0<s<1$, we define a dilation $\psi_{s}: \mathbb{R}^{3} \rightarrow \mathbb{R}^{3}$ by $\psi_{s}(b, c)=$ $(b / s, c / s)$ for $(b, c) \in \mathbb{R} \times \mathbb{C}=\mathbb{R}^{3}$. Then for the ellipsoids we have $\psi_{s}(\mathscr{B}(1))=\mathscr{B}(s)$. Hence pulling back by $\psi_{s}, \mathscr{B}(s)$ becomes $\mathscr{B}(1)$ and the point $p_{j}=\left(b_{j}, c_{j}\right) \in \mathscr{B}(s)$ is pulled back to $s \cdot p_{j}=\left(s b_{j}, s c_{j}\right)$. Thus by letting $s \rightarrow 0$, all the monopole points become closer to the origin, while their relative position is exactly as explained in the last paragraph.

Finally it seems natural to expect that, when any sequence $\left\{\left\{p_{i 1}, p_{i 2}, \cdots, p_{i n}\right\} \subset \mathscr{H}^{3} \mid i=\right.$ $1,2, \cdots\}$ of $n$ points is given, possible limits (as pointed spaces) of the associated LeBrun metrics, implied by the above Tian-Viaclovsky's convergence theorem, are LeBrun orbifolds with $k(0 \leq k \leq n)$ monopole points, where the LeBrun orbifold metric means a natural generalization of the LeBrun metrics, allowing some of the monopole points to coincide (see [12, Section 2.2] for the precise definition). Then it would be possible to say that the degenerations considered in Sections 2 and 3 are two extremal cases among these degenerations.

\section*{References}
\begin{itemize}
\item[] [1] M. Atiyah, N. Hitchin, I. Singer, Self-duality in four-dimensional Riemannian geometry, Proc. Roy. Soc. London, Ser. A 362 (1978), 425-461.
\item[] [2] S.K. Donaldson, R. Friedman, Connected sums of self-dual manifolds and deformations of singular spaces, Nonlinearity 2 (1989) 197-239.
\item[] [3] G.W. Gibbons, S.W. Hawking, Gravitational multi-instantons, Phys. Lett. 78B (1978) 430-432.
\item[] [4] N. Hitchin, Polygons and Gravitons, Math. Proc. Cambridge Philos. Soc. 85 (1979), 465-476.
\item[] [5] N. Honda and J. Viaclovsky, Conformal symmetries of self-dual hyperbolic monopole metrics. preprint. arXiv:0902.2019
\item[] [6] C. LeBrun, Counter-examples to the generalized positive action conjecture, Comm. Math. Phys. 118 (1988), 591-596.
\item[] [7] C. LeBrun, Explicit self-dual metrics on $\mathbb{C P}^{2} \cdots \mathbb{C P}^{2}$, J. Diff. Geom. 34 (1991), 223-253.
\item[] [8] C. LeBrun, Twistors, Kähler manifolds, and bimeromorphic geometry I, J. Amer. Math. Soc. 5 (1992), 289-316.
\item[] [9] M. Pontecorvo, On twistor spaces of anti-self-dual Hermitian surfaces, Tran. Amer. Math. Soc. 331 (1992), 653-661.
\item[] [10] Y. S. Poon, Compact self-dual manifolds of positive scalar curvature, J. Diff. Geom. 24 (1986), 97-132.
\item[] [11] G. Tian, J. Viaclovsky, Moduli spaces of critical Riemannian metrics in dimension four, Adv. Math. 196 (2005), 346-372.
\item[] [12] J. Viaclovsky, Yamabe invariants and limits of self-dual hyperbolic monopole metrics, arXiv.org.1002.2119, 2010.
\end{itemize}

Department of Mathematics, Tokyo Institute of Technology, O-okayama, Tokyo, Japan
Current Address: Mathematical Institute, Tohoku University, Sendai, Miyagi, Japan
E-mail address: honda@math.tohoku.ac.jp