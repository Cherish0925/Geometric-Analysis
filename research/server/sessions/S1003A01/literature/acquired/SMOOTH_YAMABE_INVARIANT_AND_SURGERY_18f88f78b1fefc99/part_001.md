---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: SMOOTH YAMABE INVARIANT AND SURGERY]

---
source_file: 0804_1418.pdf
converter: mathpix
format: mmd
---

\title{
SMOOTH YAMABE INVARIANT AND SURGERY
}

\author{
BERND AMMANN, MATTIAS DAHL, AND EMMANUEL HUMBERT
}

\begin{abstract}
We prove a surgery formula for the smooth Yamabe invariant $\sigma(M)$ of a compact manifold $M$. Assume that $N$ is obtained from $M$ by surgery of codimension at least 3. We prove the existence of a positive constant $\Lambda_{n}$, depending only on the dimension $n$ of $M$, such that
$$\sigma(N) \geq \min \left\{\sigma(M), \Lambda_{n}\right\} .$$
\end{abstract}

Contents
\begin{itemize}
\item[1.] Introduction
\end{itemize}

1
\begin{itemize}
\item[2.] The connected sum along a submanifold
\item[3.] The constants $\Lambda_{n, k}$
\item[4.] Limit spaces and limit solutions
\item[5.] $L^{2}$-estimates on $W S$-bundles
\item[6.] Proof of Theorem 1.3
\end{itemize}

Appendix A. Some details

References

\section*{1. Introduction}
1.1. Main result. The smooth Yamabe invariant, also called Schoen's $\sigma$-constant, of a compact manifold $M$ is defined as
$$\sigma(M):=\operatorname{supinf} \int_{M} \operatorname{Scal}^{g} d v^{g},$$
where the supremum runs over all conformal classes $\left[g_{0}\right]$ on $M$ and the infimum runs over all metrics $g$ of volume 1 in $\left[g_{0}\right]$. The integral $\mathcal{E}(g):=$ $\int_{M} \mathrm{Scal}^{g} d v^{g}$ is the integral of the scalar curvature of $g$ integrated with respect to the volume element of $g$ and is known as the Einstein-Hilbert functional.

\footnotetext{
Date: September 2nd, 2012.
2010 Mathematics Subject Classification. 35J60 (Primary), 35P30, 57R65, 58J50, 58C40 (Secondary).
Key words and phrases. Yamabe operator, Yamabe invariant, surgery, positive scalar curvature.
}

Let $n=\operatorname{dim} M$. We assume that $N$ is obtained from $M$ by surgery of codimension $n-k \geq 3$. That is for a given embedding $S^{k} \hookrightarrow$ $M$, with trivial normal bundle, $0 \leq k \leq n-3$, we remove a tubular neighborhood $U_{\epsilon}\left(S^{k}\right)$ of this embedding. The resulting manifold has boundary $S^{k} \times S^{n-k-1}$. This boundary is glued together with the boundary of $B^{k+1} \times S^{n-k-1}$, and we thus obtain the closed smooth manifold
$$N:=\left(M \backslash U_{\epsilon}\left(S^{k}\right)\right) \cup_{S^{k} \times S^{n-k-1}}\left(B^{k+1} \times S^{n-k-1}\right) .$$

Our main result is the existence of a positive constant $\Lambda_{n}$ depending only on $n$ such that
$$\sigma(N) \geq \min \left\{\sigma(M), \Lambda_{n}\right\} .$$
This formula unifies and generalizes previous results obtained by Gromov and Lawson, Schoen and Yau, Kobayashi, Peteana nd Yun. It also allows many conclusions by using bordism theory.

In Section 1.2 we give a detailed description of the background of our result, a stronger version of the main result follows in Section 1.3, followed by a sketch of topological applications, see Section 1.4. The construction of a generalization of surgery is recalled in Section 2. Then, in Section 3 the constant $\Lambda_{n}$ is described and it is proven to be positive. After the proof of some preliminary results on limit spaces in Section 4, we derive a key estimate in Section 5, namely an estimate for the $L^{2}$ -norm of solutions of a perturbed Yamabe equation on a special kind of sphere bundle, called $W S$-bundle. The last section contains the proof of the main theorem, Theorem 1.3.
1.2. Basic notions, the Yamabe problem, and some surgery formulas. We denote by $B^{n}(r)$ the open ball of radius $r$ around 0 in $\mathbb{R}^{n}$ and we set $B^{n}:=B^{n}(1)$. The unit sphere in $\mathbb{R}^{n}$ is denoted by $S^{n-1}$. By $\xi^{n}$ we denote the standard flat metric on $\mathbb{R}^{n}$ and by $\sigma^{n-1}$ the standard metric of constant sectional curvature 1 on $S^{n-1}$. We denote the Riemannian manifold $\left(S^{n-1}, \sigma^{n-1}\right)$ by $\mathbb{S}^{n-1}$. All manifolds in this article are manifolds without boundary unless stated differently.

Let $(M, g)$ be a Riemannian manifold of dimension $n$. The Yamabe operator, or Conformal Laplacian, acting on smooth functions on $M$ is defined by
$$L^{g} u=a \Delta^{g} u+\operatorname{Scal}^{g} u,$$
where $a:=\frac{4(n-1)}{n-2}$ and where $\Delta^{g}=\operatorname{div}^{g} \operatorname{grad}^{g}$ is the non-negative Laplacian associated to the metric $g$. Let $p:=\frac{2 n}{n-2}$. Define the functional $J^{g}$ acting on non-zero compactly supported smooth functions on $M$ by
$$J^{g}(u):=\frac{\int_{M} u L^{g} u d v^{g}}{\left(\int_{M} u^{p} d v^{g}\right)^{\frac{2}{p}}} .$$

If $g$ and $\tilde{g}=f^{\frac{4}{n-2}} g=f^{p-2} g$ are conformal metrics on $M$, then the corresponding Yamabe operators are related by
$$L^{\tilde{g}} u=f^{-\frac{n+2}{n-2}} L^{g}(f u)=f^{1-p} L^{g}(f u) .$$
It follows that
$$J^{\tilde{g}}(u)=J^{g}(f u) .$$
For a compact Riemannian manifold $(M, g)$ the conformal Yamabe constant is defined by
$$\mu(M, g):=\inf J^{g}(u) \in \mathbb{R},$$
where the infimum is taken over all non-zero smooth functions $u$ on $M$. The same value of $\mu(M, g)$ is obtained if one takes the infimum over positive smooth functions. From (3) it follows that the invariant $\mu$ depends only on the conformal class $[g]$ of $g$, and the notation $\mu(M,[g])=\mu(M, g)$ is also used. For the standard sphere we have
$$\mu\left(\mathbb{S}^{n}\right)=n(n-1) \omega_{n}{ }^{2 / n},$$
where $\omega_{n}$ denotes the volume of $\mathbb{S}^{n}$. This value is a universal upper bound for $\mu$.

Theorem 1.1 ([10, Lemma 3]). The inequality
$$\mu(M, g) \leq \mu\left(\mathbb{S}^{n}\right)$$
holds for any compact Riemannian manifold $(M, g)$.
For $u>0$ the $J^{g}$-functional is related to the Einstein-Hilbert-functional via
$$J^{g}(u)=\frac{\mathcal{E}\left(u^{4 /(n-2)} g\right)}{\operatorname{Vol}\left(M, u^{4 /(n-2)} g\right)^{\frac{n-2}{n}}}, \quad \forall u \in C^{\infty}\left(M, \mathbb{R}^{+}\right),$$
and it follows that $\mu(M, g)$ has the alternative characterization
$$\mu(M, g)=\inf _{\tilde{g} \in[g]} \frac{\mathcal{E}(\tilde{g})}{\operatorname{Vol}(M, \tilde{g})^{\frac{n-2}{n}}} .$$
Critical points of the functional $J^{g}$ are given by solutions of the Yamabe equation
$$L^{g} u=\mu|u|^{p-2} u$$
for some $\mu \in \mathbb{R}$. If the inequality in Theorem 1.1 is satisfied strictly, that is if $\mu(M, g)<\mu\left(\mathbb{S}^{n}\right)$, then the infimum in the definition of $\mu(M, g)$ is attained.

Theorem 1.2 ([56, 10]). Let $M$ be connected. If $\mu(M, g)<\mu\left(\mathbb{S}^{n}\right)$ then there exists a smooth positive function $u$ with $J^{g}(u)=\mu$ and $\|u\|_{L^{p}}=1$. This implies that $u$ solves (5) with $\mu=\mu(M, g)$. The minimizer $u$ is unique if $\mu \leq 0$.

The inequality $\mu(M, g)<\mu\left(\mathbb{S}^{n}\right)$ was shown by Aubin [10] for non-conformally flat, compact manifolds of dimension at least 6. Later Schoen [48] could apply the positive mass theorem to obtain this strict inequality for all compact manifolds not conformal to the standard sphere. We thus have a solution of
$$L^{g} u=\mu u^{p-1}, \quad u>0 .$$

To explain the geometric meaning of these results we recall a few facts about the Yamabe problem, see for example [38] and [53, Chapter 5] for more details on this material. The name of Yamabe is associated to the problem, as Yamabe wrote the first article about this subject [57].

For a given compact Riemannian manifold $(M, g)$ the Yamabe problem consists of finding a metric of constant scalar curvature in the conformal class of $g$. The above results yield a minimizer $u$ for $J^{g}$. Equation (5) is equivalent to the fact that the scalar curvature of the metric $u^{4 /(n-2)} g$ is everywhere equal to $\mu$. Thus, the above Theorem, together with $\mu(M, g)<\mu\left(\mathbb{S}^{n}\right)$, resolves the Yamabe problem.

A conformal class $[g]$ on $M$ contains a metric of positive scalar curvature if and only if $\mu(M,[g])>0$. If $M=M_{1} \amalg M_{2}$ is a disjoint union of $M_{1}$ and $M_{2}$ and if $g_{i}$ is the restriction of $g$ to $M_{i}$, then an elementary argument where one rescales the components with different factors yields that
$$\mu(M,[g])=\min \left\{\mu\left(M_{1},\left[g_{1}\right]\right), \mu\left(M_{2},\left[g_{2}\right]\right)\right\}$$
if $\mu\left(M_{1},\left[g_{1}\right]\right) \geq 0$ or $\mu\left(M_{2},\left[g_{2}\right]\right) \geq 0$, and otherwise
$$\mu(M,[g])=-\left(\left|\mu\left(M_{1},\left[g_{1}\right]\right)\right|^{n / 2}+\left|\mu\left(M_{2},\left[g_{2}\right]\right)\right|^{n / 2}\right)^{2 / n} .$$

One now defines the smooth Yamabe invariant of an arbitrary compact manifold $M$ of dimension at least 3 as
$$\sigma(M):=\sup \mu(M,[g]) \leq n(n-1) \omega_{n}^{2 / n},$$
where the supremum is taken over all conformal classes $[g]$ on $M$.
The introduction of this invariant was originally motivated by Yamabe's attempt to find Einstein metrics on a given compact manifold, see [49] and [35]. Yamabe's idea in the early 1960's was to search for a conformal class $\left[g_{\text {sup }}\right]$ that attains the supremum. The minimizer $g_{0}$ of $\mathcal{E}$ among all unit volume metrics in $\left[g_{\text {sup }}\right]$ exists according to Theorem 1.2, and Yamabe hoped that the $g_{0}$ obtained with this minimax procedure would be a stationary point of $\mathcal{E}$ among all unit volume metrics (without fixed conformal class), which is equivalent to $g_{0}$ being an Einstein metric.

Yamabe's approach was very ambitious. If $M$ is a simply connected compact 3-manifold, then an Einstein metric on $M$ is necessarily a round metric on $S^{3}$, hence the 3-dimensional Poincaré conjecture would
follow. It turned out, that his approach actually yields an Einstein metric in some special cases. For example, LeBrun [36] showed that if a compact 4-dimensional manifold $M$ carries a Kähler-Einstein metric with non-positive scalar curvature, then the supremum is attained by the conformal class of this metric. Moreover, in any maximizing conformal class the minimizer is a Kähler-Einstein metric.

Compact quotients $M=\Gamma \backslash \mathbb{H}^{3}$ of 3-dimensional hyperbolic space $\mathbb{H}^{3}$ yield other examples on which Yamabe's approach yields an Einstein metric. On such quotients the supremum is attained by the hyperbolic metric on $M$. The proof of this statement uses Perelman's proof of the Geometrization conjecture, see [9] and [30, Section II.8]. In particular, $\sigma\left(\Gamma \backslash \mathbb{H}^{3}\right)=-6\left(v_{\Gamma}\right)^{2 / 3}$ where $v_{\Gamma}$ is the volume of $\Gamma \backslash \mathbb{H}^{3}$ with respect to the hyperbolic metric.

On a general manifold, Yamabe's approach failed for various reasons. In dimension 3 and 4 obstructions against the existence of Einstein metrics are known today, see for example [34, 37]. In many cases the supremum is not attained.
R. Schoen and O. Kobayashi started to study the smooth Yamabe invariant systematically in the late 1980's, [49, 50, 31, 32]. In particular, they determined $\sigma\left(S^{n-1} \times S^{1}\right)$ to be $\sigma\left(S^{n}\right)=n(n-1) \omega_{n}^{2 / n}$. On $S^{n-1} \times S^{1}$ the supremum in the definition of $\sigma$ is not attained. Because of Schoen's important results in these articles, the smooth Yamabe invariant is also often called Schoen's $\sigma$-constant.

The smooth Yamabe invariant determines the existence of positive scalar curvature metrics. Namely, it follows from above that the smooth Yamabe invariant $\sigma(M)$ is positive if and only if the manifold $M$ admits a metric of positive scalar curvature. Thus the value of $\sigma(M)$ can be interpreted as a quantitative refinement of the property of admitting a positive scalar curvature metric.

In general calculating the $\sigma$-invariant is very difficult. LeBrun 34, Section 5], [36] showed that the $\sigma$-invariant of a complex algebraic surfaces is negative (resp. zero) if and only if it is of general type (resp. of Kodaira dimension 0 or 1), and the value of $\sigma(M)$ can be calculated explicitly in these cases. As already explained above, the $\sigma$-invariant can also be calculated for hyperbolic 3-manifolds, they are realized by the hyperbolic metrics.

There are many manifolds admitting a Ricci-flat metric, but no metric of positive scalar curvature, for example tori, K3-surfaces and compact connected 8-dimensional manifolds admitting metrics with holonomy Spin(7). These conditions imply $\sigma(M)=0$, and the supremum is attained.

Conversely, Bourguignon showed that if $\sigma(M)=0$ and if the supremum is attained by a conformal class $\left[g_{\text {sup }}\right]$, then $\mathcal{E}:\left[g_{\text {sup }}\right] \rightarrow \mathbb{R}$ attains its minimum in a Ricci-flat metric $g_{0} \in\left[g_{\text {sup }}\right]$. Thus Cheeger's splitting
principle implies topological restrictions on $M$ in this case. In particular, a compact quotient $\Gamma \backslash N$ of a non-abelian nilpotent Lie group $N$ does not admit metrics of non-negative scalar curvature, but it admits a sequence of metrics $g_{i}$ with $\mu\left(\Gamma \backslash N, g_{i}\right) \rightarrow 0$. Thus $\Gamma \backslash N$ is an example of a manifold for which $\sigma(\Gamma \backslash N)=0$, for which the supremum is not attained.

All the examples mentioned up to here have $\sigma(M) \leq 0$. Positive smooth Yamabe invariants are even harder to determine. The calculation of non-positive $\sigma(M)$ often relies on the formula
$$|\min \{\sigma(M), 0\}|^{n / 2}=\inf _{g} \int_{M}\left|\operatorname{Sca} \mathrm{I}^{g}\right|^{n / 2} d v^{g}$$
where the infimum runs over all Riemannian metrics $g$ on $M$, see [35, Proof of Proposition 2.1]. This formula does not distinguish between different positive values of $\sigma(M)$, and thus it cannot be used in the positive case.

It has been conjectured by Schoen [50, Page 10, lines 6-11] that all finite quotients of round spheres satisfy $\sigma\left(S^{n} / \Gamma\right)=(\# \Gamma)^{-2 / n} Y\left(\mathbb{S}^{n}\right)$, but this conjecture is only verified for $\mathbb{R} P^{3}$ [13], namely $\sigma\left(\mathbb{R} P^{3}\right)=$ $6\left(\omega_{3} / 2\right)^{2 / 3}$. The smooth Yamabe invariant is also known for connected sums of copies of real projective space $\mathbb{R} P^{3}$ with copies of $S^{2} \times S^{1}$ [3], for $\mathbb{C} P^{2}$ [23] and for connected sums of $\mathbb{C} P^{2}$ with several copies of $S^{3} \times S^{1}$. With similar methods, it can also be determined for some related manifolds, but for example the value of $\sigma\left(S^{2} \times S^{2}\right)$ is not known. To the knowledge of the authors there are no manifolds $M$ of dimension $n \geq 5$ for which it has been shown that $0<\sigma(M)<\sigma\left(S^{n}\right)$, but due to Schoen's conjecture finite quotients of spheres would be examples of such manifolds.

As explicit calculation of the Yamabe invariant is difficult, it is natural to use surgery theory to get estimates for more complicated examples. Several articles study the behavior of the smooth Yamabe invariant under surgery. In [21] and [51] it is proven that the existence of a positive scalar curvature metric is preserved under surgeries of codimension at least 3. In terms of the $\sigma$-invariant this means that if $N$ is obtained from a compact manifold $M$ by surgery of codimension at least 3 and $\sigma(M)>0$, then $\sigma(N)>0$.

Later Kobayashi proved in [32] that if $N$ is obtained from $M$ by 0-dimensional surgery, then $\sigma(N) \geq \sigma(M)$. A first consequence is an alternative deduction of $\sigma\left(S^{n-1} \times S^{1}\right)=\sigma\left(S^{n}\right)$ using the fact that $S^{n-1} \times S^{1}$ is obtained from $S^{n}$ by 0-dimensional surgery. More generally one sees that $\sigma\left(S^{n-1} \times S^{1} \# \cdots \# S^{n-1} \times S^{1}\right)=\sigma\left(S^{n}\right)$ as this connected sum is obtained from $S^{n}$ by 0-dimensional surgeries as well.

Note that it follows from what we said above that the smooth Yamabe invariant of disjoint unions $M=M_{1} \amalg M_{2}$ satisfies
$$\sigma(M)=\min \left\{\sigma\left(M_{1}\right), \sigma\left(M_{2}\right)\right\}$$
if $\sigma\left(M_{1}\right) \geq 0$ or $\sigma\left(M_{2}\right) \geq 0$, and otherwise
$$\sigma(M)=-\left(\left|\sigma\left(M_{1}\right)\right|^{n / 2}+\left|\sigma\left(M_{2}\right)\right|^{n / 2}\right)^{2 / n} .$$
Kobayashi's result then implies $\sigma\left(M_{1} \# M_{2}\right) \geq \sigma\left(M_{1} \amalg M_{2}\right)$, and thus yields a lower bound for $\sigma\left(M_{1} \# M_{2}\right)$ in terms of $\sigma\left(M_{1}\right)$ and $\sigma\left(M_{2}\right)$.

A similar monotonicity formula for the $\sigma$-invariant was proved by Petean and Yun in [45]. They prove that $\sigma(N) \geq \min \{\sigma(M), 0\}$ if $N$ is obtained from $M$ by surgery of codimension at least 3. See also [35, Proposition 4.1] and [1] for other approaches to this result. Clearly, this surgery result is particularly interesting in the case $\sigma(M) \leq 0$, and it has several fruitful applications. In particular, any simply connected compact manifold of dimension at least 5 has $\sigma(M) \geq 0$; see [44]. This result has been generalized to manifolds with certain types of fundamental group in [12]. Further results in the same spirit for $n=4$ can be found in [55].
1.3. Stronger version of the main result. In the present article we derive a surgery formula which is stronger than the Gromov-Lawson resp. Schoen-Yau surgery formula, the Kobayashi surgery formula and the Petean-Yun surgery formula described above. Suppose that $M_{1}$ and $M_{2}$ are compact manifolds of dimension $n$ and that $W$ is a compact manifold of dimension $k$. Let embeddings $W \hookrightarrow M_{1}$ and $W \hookrightarrow M_{2}$ be given. We assume further that the normal bundles of these embeddings are trivial. Removing tubular neighborhoods of the images of $W$ in $M_{1}$ and $M_{2}$, and gluing together these manifolds along their common boundary, we get a new compact manifold $N$, the connected sum of $M_{1}$ and $M_{2}$ along $W$. Strictly speaking $N$ also depends on the choice of trivialization of the normal bundle. See section 2 for more details.

Surgery is a special case of this construction: if $M_{2}=S^{n}, W=S^{k}$ and if $S^{k} \hookrightarrow S^{n}$ is the standard embedding, then $N$ is obtained from $M_{1}$ via $k$-dimensional surgery along $S^{k} \hookrightarrow M_{1}$.

Theorem 1.3. Let $M_{1}$ and $M_{2}$ be compact manifolds of dimension $n$. If $N$ is obtained as a connected sum of $M_{1}$ and $M_{2}$ along a $k$ -dimensional submanifold where $k \leq n-3$, then
$$\sigma(N) \geq \min \left\{\sigma\left(M_{1} \amalg M_{2}\right), \Lambda_{n, k}\right\}$$
where $\Lambda_{n, k}$ is positive, and only depends on $n$ and $k$. Furthermore $\Lambda_{n, 0}=\sigma\left(S^{n}\right)$.

From Theorem 1.1 we know that $\sigma(M) \leq \sigma\left(S^{n}\right)$ and thus we see that $\sigma\left(M \amalg S^{n}\right)=\sigma(M)$ for all compact $M$. Hence, we obtain for the special case of surgery the following corollary.

Corollary 1.4. Let $M$ be a compact manifold of dimension $n$. Assume that $N$ is obtained from $M$ via surgery along a $k$-dimensional sphere
$W, k \leq n-3 . W e$ then have
$$\sigma(N) \geq \min \left\{\sigma(M), \Lambda_{n, k}\right\}$$

The constants $\Lambda_{n, k}$ will be defined in Section 3. In Subsections 3.3 and 3.4 we prove that these constants are positive, and in Subsection 3.5 we prove that $\Lambda_{n, 0}=\mu\left(\mathbb{S}^{n}\right)$. Explicit lower bounds for $\Lambda_{n, k}$ can be found for all $k \notin\{1, n-3\}$, however these are not optimal, see Subsection 3.6. An explicit calculation of $\Lambda_{n, k}$ for $k>0$ seems very difficult. The main problem consists in calculating the conformal Yamabe constant of certain Riemannian products, which in general is a hard problem. See [2, 5] for recent progress on this problem.
1.4. Topological applications. The above surgery result can be combined with standard techniques of bordism theory. As these topological applications are not the main subject of this article, we will only sketch some typical conclusions as examples here.

The first corollary uses the fact that spin bordism groups and oriented bordism groups are finitely generated together with techniques developed for the proof of the $h$-cobordism theorem.
Corollary 1.5. For any $n \geq 5$ there is a constant $C_{n}>0$, depending only on $n$, such that
$$\sigma(M) \in\{0\} \cup\left[C_{n}, \sigma\left(S^{n}\right)\right]$$
for any simply-connected compact manifold $M$ of dimension $n$.
We now sketch how interesting bordism invariants can be constructed using our main result. This construction will be explained here only for spin manifolds, but similar constructions can also be done for oriented, non-spin manifolds or for non-oriented manifolds.

Fix a finitely presented group $\Gamma$, and let $B \Gamma$ be the classifying space of $\Gamma$. We consider pairs $(M, f)$ where $M$ is a compact spin manifold and where $f: M \rightarrow B \Gamma$ is continuous. Two such pairs $\left(M_{1}, f_{1}\right)$ and $\left(M_{2}, f_{2}\right)$ are called spin bordant over $B \Gamma$ if there exists an $(n+1)$-dimensional spin manifold $W$ with boundary $-M_{1} \amalg M_{2}$ with a map $F: W \rightarrow B \Gamma$ such that the restriction of $F$ to the boundary yields $f_{1}$ and $f_{2}$. It is implicitly required that the boundary carries the induced orientation and spin structure and $-M_{1}$ denotes $M_{1}$ with reversed orientation. Being spin bordant over $B \Gamma$ is an equivalence relation. The equivalence class of $(M, f)$ under this equivalence relation is denoted by $[M, f]$ and the set of equivalence classes is called $\Omega_{n}^{\text {Spin }}(B \Gamma)$. Disjoint union of manifolds defines a sum on $\Omega_{n}^{\text {Spin }}(B \Gamma)$ which turns it into an abelian group.

We say that a pair $(M, f)$ with $f: M \rightarrow B \Gamma$ is a $\pi_{1}$-bijective representative of $[M, f]$ if $M$ is connected and if the induced map $f_{*}: \pi_{1}(M) \rightarrow \Gamma$ is a bijection. Any equivalence class in $\Omega_{n}^{\text {Spin }}(B \Gamma)$ has a $\pi_{1}$-bijective representative.

Now we define
$$\begin{aligned}
\Lambda_{n} & :=\min \left\{\Lambda_{n, 1}, \ldots \Lambda_{n, n-3}\right\}>0, \\
& \bar{\sigma}(M):=\min \left\{\sigma(M), \Lambda_{n}\right\} .
\end{aligned}$$

Proposition 1.6. Let $n \geq 5$. Let ( $M_{1}, f_{1}$ ) and ( $M_{2}, f_{2}$ ) be compact spin manifolds with maps $f_{i}: M_{i} \rightarrow B \Gamma$. If $\left(M_{1}, f_{1}\right)$ and $\left(M_{2}, f_{2}\right)$ are spin bordant over $B \Gamma$ and if $\left(M_{2}, f_{2}\right)$ is a $\pi_{1}$-bijective representative of its class, then
$$\bar{\sigma}\left(M_{1}\right) \leq \bar{\sigma}\left(M_{2}\right) .$$

We define $s_{\Gamma}: \Omega_{n}^{\text {Spin }}(B \Gamma) \rightarrow \mathbb{R}$ by
$$s_{\Gamma}([M, f]):=\sup _{\left(M_{1}, f_{1}\right) \in[M, f]} \bar{\sigma}\left(M_{1}\right) .$$
The proposition states $s_{\Gamma}([M, f])=\bar{\sigma}(M)$ if ( $M, f$ ) is a $\pi_{1}$-bijective representative of its class. The surgery formula further implies
$$s_{\Gamma}\left(\left[M_{1}, f_{1}\right]+\left[M_{2}, f_{2}\right]\right) \geq \min \left\{s_{\Gamma}\left(\left[M_{1}, f_{1}\right]\right), s_{\Gamma}\left(\left[M_{2}, f_{2}\right]\right)\right\}$$
if $s_{\Gamma}\left(\left[M_{1}, f_{1}\right]\right) \geq 0$ or $s_{\Gamma}\left(\left[M_{2}, f_{2}\right]\right) \geq 0$, and otherwise
$$s_{\Gamma}\left(\left[M_{1}, f_{1}\right]+\left[M_{2}, f_{2}\right]\right) \geq-\left(\left|s_{\Gamma}\left(\left[M_{1}, f_{1}\right]\right)\right|^{n / 2}+\left|s_{\Gamma}\left(\left[M_{2}, f_{2}\right]\right)\right|^{n / 2}\right)^{2 / n} .$$

We conclude, and obtain the following theorem.
Theorem 1.7. Let $t \in \mathbb{R}, t \geq 0, n \in \mathbb{N}, n \geq 5$. Then the sets
$$\Omega_{n}^{\operatorname{Spin}}(B \Gamma)^{>t}:=\left\{[M, f] \in \Omega_{n}^{\operatorname{Spin}}(B \Gamma) \mid s_{\Gamma}([M, f])>t\right\}$$
and
$$\Omega_{n}^{\operatorname{Spin}}(B \Gamma)^{\geq t}:=\left\{[M, f] \in \Omega_{n}^{\operatorname{Spin}}(B \Gamma) \mid s_{\Gamma}([M, f]) \geq t\right\}$$
are subgroups of $\Omega_{n}^{\text {Spin }}(B \Gamma)$.
The theorem admits - among other interesting conclusions - the following application. For a positive integer $p$ we write $p \# M$ for the connected sum $M \# \cdots \# M$ where $M$ appears $p$ times. We already know that $\sigma(p \# M) \geq \sigma(M)$ if $\sigma(M) \geq 0$.

Corollary 1.8. Suppose that $M$ is a compact spin manifold of dimension at least 5 with $\sigma(M) \in\left(0, \Lambda_{n}\right)$. Let $p$ and $q$ be two relatively prime positive integers. If $\sigma(p \# M)>\sigma(M)$, then $\sigma(q \# M)=\sigma(M)$.

If Schoen's conjecture about the $\sigma$-invariant of quotients of spheres holds true, then quotients of spheres by large fundamental groups yield examples of manifolds $M$ with $\sigma(M) \in\left(0, \Lambda_{n}\right)$.

The determination of manifolds admitting positive scalar curvature metrics, that is manifolds with $\sigma(M)>0$, has led to interesting results and challenging problems in topology, see for example [47]. It would be interesting to develop similar topological tools for manifolds
with $\sigma(M)>\epsilon$ for $\epsilon>0$. As explained above such manifolds form a subgroup on the bordism level.

The subgroups $\Omega_{n}^{\text {Spin }}(B \Gamma)^{>t}$ also provide interesting algebraic structures. Any homomorphism $\Gamma_{1} \rightarrow \Gamma_{2}$ provides a homomorphism
$$\Omega_{n}^{\mathrm{Spin}}\left(B \Gamma_{1}\right)^{>t} \rightarrow \Omega_{n}^{\mathrm{Spin}}\left(B \Gamma_{2}\right)^{>t} .$$
After introducing some factors and powers depending on the dimension, these subgroups carry an ideal-like structure. More precisely, it follows from [5] that for any numbers $t_{5}>0$ there is a sequence $t_{n}>0, n \geq 5$, such that taking products of manifolds defines a $\mathbb{Z}$-bilinear map
$$\Omega_{* \geq 5}^{\mathrm{Spin}}\left(B \Gamma_{1}\right) \times \Omega_{* \geq 5}^{\mathrm{Spin}}\left(B \Gamma_{2}\right)^{>t_{*}} \rightarrow \Omega_{* \geq 5}^{\mathrm{Spin}}\left(B\left(\Gamma_{1} \times \Gamma_{2}\right)\right)^{>t_{*}}$$
where the index $* \geq 5$ indicates that we consider the spin bordism ring of manifolds whose dimension is at least 5. In particular $\Omega_{* \geq 5}^{\text {Spin }}(B \Gamma)^{>t_{*}}$ is a module over the ring $\Omega_{* \geq 5}^{\text {Spin }}:=\Omega_{* \geq 5}^{\text {Spin }}(B\{1\})$ and $\Omega_{* \geq 5}^{\text {Spin }>t_{*}}$ is an ideal in $\Omega_{* \geq 5}^{\text {Spin }}$. Analogous structures exist for $\Omega_{n}^{\text {Spin }}(B \Gamma)^{\geq t}$.
1.5. Comparison to other results. At the end of the section we want to mention some similar constructions in the literature. An analogous surgery formula holds if we replace the Conformal Laplacian by the Dirac operator, see [4] for details and applications. D. Joyce [28], followed by L. Mazzieri [42, 43], considered a problem tightly related to our result: their goal is to construct a metric on a manifold obtained via a connected sum along a $k$-dimensional submanifold. For these metrics they construct a solution of the Yamabe equation on the new manifold that is close to solutions of the Yamabe equations on the original pieces. Such a construction was achieved by D. Joyce for $k=0$ and by L. Mazzieri for $k \in\{1, \ldots, n-3\}$ provided that the embeddings defining the connected sum are isometric. In contrast to our article their solutions on the new manifold are not necessarily minimizers of the volume-normalized Einstein-Hilbert functional. Similar constructions have also been developed by R. Mazzeo, D. Pollack, and K. Uhlenbeck [41] in order to glue together metrics of constant scalar curvature. Recently, J. Corvino, M. Eichmair, and P. Miao showed how to glue together metrics while preserving constant scalar curvature and volume, see [16]. Further, P. T. Chrusciel, J. Isenberg, and D. Pollack [15], found methods to glue together solutions of the vacuum Einstein constraint equations.

Other authors studied the equivariant analogues. In this setting one assumes that a compact Lie group $G$ acts on the manifolds before and after surgery and that the surgery is compatible with this actions. Furthermore all metrics are assumed to be $G$-invariant and the Yamabe constant and Yamabe invariant are replaced by their equivariant analogues. The equivariant Yamabe problem is solved in many cases, in particular on spin manifolds or in the case that all orbits have positive
dimension, see [27], [39, 40]. An equivariant analogue of the Petean-Yun surgery formula was provided in [54]. B. Hanke [24] proved that the existence of $G$-invariant positive scalar curvature metrics is preserved under equivariant surgeries of the appropriate dimensions, which is the equivariant generalization of the result by Gromov and Lawson, respectively Schoen and Yau, cited above.

Acknowledgments. The authors want to thank the Max Planck Institute for Gravitational Physics in Potsdam for its hospitality, its support, and its friendly working conditions which had an important impact on this article. We thank Andreas Hermann for the numerical computation of the equivariant version of $\Lambda_{4,1}$ mentioned in Section 3.7. We also thank Kazuo Akutagawa for interesting discussions and insightful comments. Finally, we want to express our deep thanks to the anonymous referee whose many valuable remarks have helped us greatly to improve the paper.

\section*{2. The connected sum along a submanifold}

In this section we are going to describe how two manifolds are joined along a common submanifold with trivialized normal bundle. Strictly speaking this is a differential topological construction, but since we work with Riemannian manifolds we will make the construction adapted to the Riemannian metrics and use distance neighborhoods defined by the metrics etc.

Let $\left(M_{1}, g_{1}\right)$ and $\left(M_{2}, g_{2}\right)$ be complete Riemannian manifolds of dimension $n$. Let $W$ be a compact manifold of dimension $k$, where $0 \leq k \leq n$. Let $\bar{w}_{i}: W \times \mathbb{R}^{n-k} \rightarrow T M_{i}, i=1,2$, be smooth embeddings. We assume that $\bar{w}_{i}$ restricted to $W \times\{0\}$ maps to the zero section of $T M_{i}$ (which we identify with $M_{i}$ ) and thus gives an embedding $W \rightarrow M_{i}$. The image of this embedding is denoted by $W_{i}^{\prime}$. Further we assume that $\bar{w}_{i}$ restrict to linear isomorphisms $\{p\} \times \mathbb{R}^{n-k} \rightarrow N_{\bar{w}_{i}(p, 0)} W_{i}^{\prime}$ for all $p \in W_{i}$, where $N W_{i}^{\prime}$ denotes the normal bundle of $W_{i}^{\prime}$ defined using $g_{i}$.

By setting $w_{i}:=\exp ^{g_{i}} \circ \bar{w}_{i}$ we obtain the embeddings $w_{i}: W \times$ $B^{n-k}\left(R_{\text {max }}\right) \rightarrow M_{i}$ for some $R_{\text {max }}>0$ and $i=1,2$. We have $W_{i}^{\prime}=$ $w_{i}(W \times\{0\})$ and we define the disjoint union
$$(M, g):=\left(M_{1} \amalg M_{2}, g_{1} \amalg g_{2}\right),$$
and
$$W^{\prime}:=W_{1}^{\prime} \amalg W_{2}^{\prime} .$$
Let $r_{i}$ be the function on $M_{i}$ giving the distance to $W_{i}^{\prime}$. Then $r_{1} \circ$ $w_{1}(p, x)=r_{2} \circ w_{2}(p, x)=|x|$ for $p \in W, x \in B^{n-k}\left(R_{\text {max }}\right)$. Let $r$ be the function on $M$ defined by $r(x):=r_{i}(x)$ for $x \in M_{i}, i=1,2$. For $0<\epsilon$
we set $U_{i}(\epsilon):=\left\{x \in M_{i}: r_{i}(x)<\epsilon\right\}$ and $U(\epsilon):=U_{1}(\epsilon) \cup U_{2}(\epsilon)$. For $0<\epsilon<\theta$ we define
$$N_{\epsilon}:=\left(M_{1} \backslash U_{1}(\epsilon)\right) \cup\left(M_{2} \backslash U_{2}(\epsilon)\right) / \sim,$$
and
$$U_{\epsilon}^{N}(\theta):=(U(\theta) \backslash U(\epsilon)) / \sim$$
where ~ indicates that we identify the point $x \in \partial U_{1}(\epsilon)$ in $M_{1}$ with the corresponding point $w_{2} \circ w_{1}^{-1}(x) \in \partial U_{2}(\epsilon)$ in $M_{2}$. Hence
$$N_{\epsilon}=(M \backslash U(\theta)) \cup U_{\epsilon}^{N}(\theta) .$$

We say that $N_{\epsilon}$ is obtained from $M_{1}, M_{2}$ (and $\bar{w}_{1}, \bar{w}_{2}$ ) by a connected sum along $W$ with parameter $\epsilon$.

The diffeomorphism type of $N_{\epsilon}$ is independent of $\epsilon$, hence we will usually write $N=N_{\epsilon}$. However, in situations when dropping the index causes ambiguities we will keep the notation $N_{\epsilon}$. For example the function $r: M \rightarrow[0, \infty)$ gives a continuous function $r_{\epsilon}: N_{\epsilon} \rightarrow[\epsilon, \infty)$ whose domain depends on $\epsilon$. It is also going to be important to keep track of the subscript $\epsilon$ on $U_{\epsilon}^{N}(\theta)$ since crucial estimates on solutions of the Yamabe equation will be carried out on this set.

The surgery operation on a manifold is a special case of taking connected sum along a submanifold. Indeed, let $M$ be a compact manifold of dimension $n$ and let $M_{1}=M, M_{2}=S^{n}, W=S^{k}$. Let $w_{1}: S^{k} \times B^{n-k} \rightarrow M$ be an embedding defining a surgery and let $w_{2}$ : $S^{k} \times B^{n-k} \rightarrow S^{n}$ be the standard embedding. Since $S^{n} \backslash w_{2}\left(S^{k} \times B^{n-k}\right)$ is diffeomorphic to $B^{k+1} \times S^{n-k-1}$ we have in this situation that $N$ is obtained from $M$ by performing surgery on $w_{1}$, see [33, Section VI, 9].

\section*{3. The constants $\Lambda_{n, k}$}

In Section 1.2 we defined the conformal Yamabe constant only for compact manifolds. There are several ways to generalize the conformal Yamabe constant to non-compact manifolds. In this section we define two such generalizations $\mu^{(0)}$ and $\mu^{(1)}$, and also introduce a related quantity called $\mu^{(2)}$. These invariants will be needed to define the constants $\Lambda_{n, k}$ and to prove their positivity on our model spaces $\mathbb{H}_{c}^{k+1} \times$ $\mathbb{S}^{n-k-1}$.

The definition of $\mu^{(2)}$ comes from a technical difficulty in the proof of Theorem 6.1 and is only relevant in the case $k=n-3 \geq 3$, see Remark 3.4.
3.1. The manifolds $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$. For $0 \leq k<n$ and $c \in \mathbb{R}$ we define the metric $\eta_{c}^{k+1}:=e^{2 c t} \xi^{k}+d t^{2}$ on $\mathbb{R}^{k} \times \mathbb{R}$ and we write
$$\mathbb{H}_{c}^{k+1}:=\left(\mathbb{R}^{k} \times \mathbb{R}, \eta_{c}^{k+1}\right) .$$

This is a model of the simply connected complete manifold of constant curvature $-c^{2}$. We denote by
$$G_{c}:=\eta_{c}^{k+1}+\sigma^{n-k-1}$$
the product metric on $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$. The scalar curvature of $\mathbb{H}_{c}^{k+1} \times$ $\mathbb{S}^{n-k-1}$ is Scal ${ }^{G_{c}}=-k(k+1) c^{2}+(n-k-1)(n-k-2)$.

Proposition 3.1. $\mathbb{H}_{1}^{k+1} \times \mathbb{S}^{n-k-1}$ is conformal to $\mathbb{S}^{n} \backslash \mathbb{S}^{k}$.
Proof. Let $\mathbb{S}^{k}$ be embedded in $\mathbb{S}^{n} \subset \mathbb{R}^{n+1}$ by setting the last $n-k$ coordinates to zero and let $s:=d\left(\cdot, \mathbb{S}^{k}\right)$ be the intrinsic distance to $\mathbb{S}^{k}$ in $\mathbb{S}^{n}$. Then the function $\sin s$ is smooth and positive on $S^{n} \backslash S^{k}$. The points of maximal distance $\pi / 2$ to $\mathbb{S}^{k}$ lie on an $(n-k-1)$-sphere, denoted by $\left(\mathbb{S}^{k}\right)^{\perp}$. On $\mathbb{S}^{n} \backslash\left(\mathbb{S}^{k} \cup\left(\mathbb{S}^{k}\right)^{\perp}\right)$ the round metric is
$$\sigma^{n}=(\cos s)^{2} \sigma^{k}+d s^{2}+(\sin s)^{2} \sigma^{n-k-1} .$$
Substitute $s \in(0, \pi / 2)$ by $t \in(0, \infty)$ such that $\sinh t=\cot s$. Then $\cosh t=(\sin s)^{-1}$ and $\cosh t d t=-(\sin s)^{-2} d s$, so $\sigma^{n}$ is conformal to
$$(\sin s)^{-2} \sigma^{n}=(\sinh t)^{2} \sigma^{k}+d t^{2}+\sigma^{n-k-1} .$$
Here we see that the first two terms give a metric
$$(\sinh t)^{2} \sigma^{k}+d t^{2}$$
on $S^{k} \times(0, \infty)$. This is just the standard metric on $\mathbb{H}_{1}^{k+1} \backslash\left\{p_{0}\right\}$ where $t=d\left(\cdot, p_{0}\right)$, written in polar normal coordinates. In the case $k \geq 1$ it is evident that the conformal diffeomorphism $\mathbb{S}^{n} \backslash\left(\mathbb{S}^{k} \cup\left(\mathbb{S}^{k}\right)^{\perp}\right) \rightarrow$ $\left(\mathbb{H}_{1}^{k+1} \backslash\left\{p_{0}\right\}\right) \times \mathbb{S}^{n-k-1}$ extends to a conformal diffeomorphism $\mathbb{S}^{n} \backslash \mathbb{S}^{k} \rightarrow$ $\mathbb{H}_{1}^{k+1} \times \mathbb{S}^{n-k-1}$.

In the case $k=0$ we equip $s$ and $t$ with a sign, that is we let $s>0$ and $t>0$ on one of the components of $\mathbb{S}^{n} \backslash\left(\mathbb{S}^{0} \cup\left(\mathbb{S}^{0}\right)^{\perp}\right)$, and $s<0$ and $t<0$ on the other component. The functions $s$ and $t$ are then smooth on $\mathbb{S}^{n} \backslash \mathbb{S}^{0}$ and take values $s \in(-\pi / 2, \pi / 2)$ and $t \in \mathbb{R}$. Then the argument is the same as above. \(\square\)
3.2. Definition of $\Lambda_{n, k}$. Let $(N, h)$ be a Riemannian manifold of dimension $n$. For $i=1,2$ we let $\Omega^{(i)}(N, h)$ be the set of non-negative $C^{2}$ functions $u$ that solve the Yamabe equation
$$L^{h} u=\mu u^{p-1}$$
for some $\mu=\mu(u) \in \mathbb{R}$ and satisfy
\begin{itemize}
\item[-] $u \not \equiv 0$,
\item[-] $\|u\|_{L^{p}(N)} \leq 1$,
\item[-] $u \in L^{\infty}(N)$,
\end{itemize}
together with
\begin{itemize}
\item[-] $u \in L^{2}(N)$, for $i=1$,
\end{itemize}
or
\begin{itemize}
\item[-] $\mu(u)\|u\|_{L^{\infty}(N)}^{p-2} \geq \frac{(n-k-2)^{2}(n-1)}{8(n-2)}$, for $i=2$.
\end{itemize}
For $i=1,2$ we set
$$\mu^{(i)}(N, h):=\inf _{u \in \Omega^{(i)}(N, h)} \mu(u) .$$
In particular, if $\Omega^{(i)}(N, h)$ is empty then $\mu^{(i)}(N, h)=\infty$.
Definition 3.2. For integers $n \geq 3$ and $0 \leq k \leq n-2$ let
$$\Lambda_{n, k}^{(i)}:=\inf _{c \in[-1,1]} \mu^{(i)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$$
and
$$\Lambda_{n, k}:=\min \left\{\Lambda_{n, k}^{(1)}, \Lambda_{n, k}^{(2)}\right\} .$$

Note that the infimum could just as well be taken over $c \in[0,1]$ since $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ and $\mathbb{H}_{-c}^{k+1} \times \mathbb{S}^{n-k-1}$ are isometric. We are going to prove that these constants are positive.

Theorem 3.3. For all $n \geq 3$ and $0 \leq k \leq n-3$, we have $\Lambda_{n, k}>0$.
The condition $k \leq n-3$ is important, as this implies that $\mathbb{S}^{n-k-1}$ has positive curvature.

To prove Theorem 3.3 we have to prove that $\Lambda_{n, k}^{(1)}>0$ and that $\Lambda_{n, k}^{(2)}>0$. This is the object of the following two subsections. In the final subsection we prove that $\Lambda_{n, 0}=\mu\left(\mathbb{S}^{n}\right)=n(n-1) \omega_{n}^{2 / n}$.

Remark 3.4. Suppose that either $k \leq n-4$ or $k=n-3 \leq 2$. One can then use methods similar to those used in Section 5 to show that any $L^{p}$-solution of (6) on the model spaces is also an $L^{2}$-solution, see [6]. An analogous argument also works in the case $(n, k)=(6,3)$, for model spaces with $c<1$, and this allows similar conclusions, see [7]. This implies that $\Lambda_{n, k}^{(2)} \geq \Lambda_{n, k}^{(1)}$ if $k \leq n-4$ or $k=n-3 \leq 3$, and hence
$$\Lambda_{n, k}=\Lambda_{n, k}^{(1)} .$$
In the case $k=n-3 \geq 4$ there are $L^{p}$-solutions of (6) on $\mathbb{H}_{1}^{k+1} \times \mathbb{S}^{n-k-1}$ that are not $L^{2}$-solutions.
3.3. Proof of $\Lambda_{n, k}^{(1)}>0$. The proof proceeds in several steps. We first introduce a conformal Yamabe constant for non-compact manifolds and show that it gives a lower bound for $\mu^{(1)}$. We then conclude by studying this conformal invariant.

Let $(N, h)$ be a Riemannian manifold that is not necessarily compact or complete. We define the conformal Yamabe constant $\mu^{(0)}$ of $(N, h)$ following Schoen-Yau [52, Section 2], see also [29], as
$$\mu^{(0)}(N, h):=\inf J^{h}(u)$$
where $J^{h}$ is defined in (1) and the infimum runs over the set of all nonzero compactly supported smooth functions $u$ on $N$. If $h$ and $\tilde{h}$ are conformal metrics on $N$ it follows from (3) that $\mu^{(0)}(N, h)=\mu^{(0)}(N, \tilde{h})$.

Lemma 3.5. Let $0 \leq k \leq n-2$. Then
$$\mu^{(1)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right) \geq \mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$$
for all $c \in \mathbb{R}$.
Proof. Suppose that $u \in \Omega^{(1)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ is a solution of (6) on $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ with $\mu=\mu(u) \in\left[\mu^{(1)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right), \mu^{(1)}\left(\mathbb{H}_{c}^{k+1} \times\right.\right.$ $\left.\mathbb{S}^{n-k-1}\right)+\epsilon$ ]. Let $\chi_{\alpha}$ be a cut-off function on $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ depending only on the distance $r$ to a fixed point, such that $\chi_{\alpha}(r)=1$ for $r \leq \alpha$, $\chi_{\alpha}(r)=0$ for $r \geq \alpha+2$, and $\left|d \chi_{\alpha}\right| \leq 1$. We are going to see that
$$\begin{aligned}
\mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right) & \leq \lim _{\alpha \rightarrow \infty} J^{G_{c}}\left(\chi_{\alpha} u\right) \\
& =\mu\|u\|_{L^{p}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)}^{p-2} \\
& \leq \mu \\
& \leq \mu^{(1)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)+\epsilon .
\end{aligned}$$
Integrating by parts and using Equations (6) and (65) we get
$$\begin{aligned}
\int_{\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}}\left(\chi_{\alpha} u\right) L^{G_{c}}\left(\chi_{\alpha} u\right) d v^{G_{c}}= & \int_{\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}} \chi_{\alpha}^{2} u L^{G_{c}} u d v^{G_{c}} \\
& +a \int_{\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}}\left|d \chi_{\alpha}\right|^{2} u^{2} d v^{G_{c}} \\
= & \mu \int_{\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}} \chi_{\alpha}^{2} u^{p} d v^{G_{c}} \\
& +a \int_{\operatorname{Supp}\left(d \chi_{\alpha}\right)}\left|d \chi_{\alpha}\right|^{2} u^{2} d v^{G_{c}} .
\end{aligned}$$
Since $u \in L^{2}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ and $\left|d \chi_{\alpha}\right| \leq 1$ the last integral goes to zero as $\alpha \rightarrow \infty$ and we conclude that
$$\lim _{\alpha \rightarrow \infty} \int_{\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}}\left(\chi_{\alpha} u\right) L^{G_{c}}\left(\chi_{\alpha} u\right) d v^{G_{c}}=\mu\|u\|_{L^{p}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)}^{p} .$$
Going back to the definition of $J^{G_{c}}$ we easily get (7), and Lemma 3.5 follows. \(\square\)

Remark 3.6. It follows from [22, Theorem 13] and a straight-forward cut-off argument that
$$\mu^{(1)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)=\mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$$
if the space $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ has positive scalar curvature, i.e. if we have $(n-k-1)(n-k-2)>c^{2} k(k+1)$.

We define
$$\Lambda_{n, k}^{(0)}:=\inf _{c \in[-1,1]} \mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right) .$$
Then Lemma 3.5 tells us that $\Lambda_{n, k}^{(1)} \geq \Lambda_{n, k}^{(0)}$, so we are done if we prove that $\Lambda_{n, k}^{(0)}>0$. To do this we need two lemmas.
Lemma 3.7. Let $0 \leq k \leq n-2$. Then
$$\mu^{(0)}\left(\mathbb{H}_{1}^{k+1} \times \mathbb{S}^{n-k-1}\right)=\mu\left(\mathbb{S}^{n}\right) .$$
Proof. The inequality $\mu^{(0)}\left(\mathbb{H}_{1}^{k+1} \times \mathbb{S}^{n-k-1}\right) \leq \mu\left(\mathbb{S}^{n}\right)$ is completely analogous to [10, Lemma 3]. As we do not need this inequality later, we skip the proof. To prove the opposite inequality $\mu^{(0)}\left(\mathbb{H}_{1}^{k+1} \times \mathbb{S}^{n-k-1}\right) \geq$ $\mu\left(\mathbb{S}^{n}\right)$ we use Proposition 3.1 and the conformal invariance of $\mu^{(0)}$, and we obtain
$$\mu^{(0)}\left(\mathbb{H}_{1}^{k+1} \times \mathbb{S}^{n-k-1}\right)=\mu^{(0)}\left(\mathbb{S}^{n} \backslash \mathbb{S}^{k}\right) .$$

Clearly $\mu^{(0)}\left(\mathbb{S}^{n} \backslash \mathbb{S}^{k}\right) \geq \mu\left(\mathbb{S}^{n}\right)$ as the infimum defining the left hand side runs over a smaller set of functions, see [52, Lemma 2.1]. \(\square\)

Lemma 3.8. Let $0 \leq k \leq n-2$ and $0<c_{0} \leq c_{1}$. Then
$$\mu^{(0)}\left(\mathbb{H}_{c_{0}}^{k+1} \times \mathbb{S}^{n-k-1}\right) \geq\left(\frac{c_{0}}{c_{1}}\right)^{\frac{2(n-k-1)}{n}} \mu^{(0)}\left(\mathbb{H}_{c_{1}}^{k+1} \times \mathbb{S}^{n-k-1}\right) .$$
Proof. Let $c>0$. Setting $s=c t+\ln c$ we see that
$$G_{c}=e^{2 c t} \xi^{k}+d t^{2}+\sigma^{n-k-1}=\frac{1}{c^{2}}\left(e^{2 s} \xi^{k}+d s^{2}\right)+\sigma^{n-k-1} .$$
Hence $G_{c}$ is conformal to the metric
$$\tilde{G}_{c}:=e^{2 s} \xi^{k}+d s^{2}+c^{2} \sigma^{n-k-1}$$
and by the conformal invariance of $\mu^{(0)}$ we get that
$$\mu^{(0)}\left(\mathbb{H}_{c_{i}}^{k+1} \times \mathbb{S}^{n-k-1}\right)=\mu^{(0)}\left(\mathbb{R}^{k} \times \mathbb{R} \times S^{n-k-1}, \tilde{G}_{c_{i}}\right)$$
for $i=0,1$. In these coordinates we easily compute that Scal ${ }^{\tilde{G} c_{0}} \geq$ Scal ${ }^{\tilde{G}_{c_{1}}},|d u|_{\tilde{G}_{c_{0}}}^{2} \geq|d u|_{\tilde{G}_{c_{1}}}^{2}$, and $d v^{\tilde{G}_{c_{0}}}=\left(\frac{c_{0}}{c_{1}}\right)^{n-k-1} d v^{\tilde{G}_{c_{1}}}$. We conclude that
$$J^{\tilde{G}_{c_{0}}}(u) \geq\left(\frac{c_{0}}{c_{1}}\right)^{\frac{2(n-k-1)}{n}} J^{\tilde{G}_{c_{1}}}(u)$$
for all functions $u$ on $\mathbb{R}^{k} \times \mathbb{R} \times S^{n-k-1}$ and Lemma 3.8 follows. \(\square\)

If we set $c_{1}=1$ and use Lemma 3.7 together with (4) we get the following result.

Corollary 3.9. For $0 \leq k \leq n-2$ and $c_{0}>0$ we have
$$\inf _{c \in\left[c_{0}, 1\right]} \mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right) \geq n(n-1) \omega_{n}{ }^{2 / n} c_{0}{ }^{4 / n} .$$

Finally, we are ready to prove that $\Lambda_{n, k}^{(0)}$ is positive.
Theorem 3.10. Let $0 \leq k \leq n-3$. Then $\Lambda_{n, k}^{(0)}>0$.
For this theorem the restriction $k \leq n-3$ is necessary. The proof needs the positive scalar curvature of $\mathbb{S}^{n-k-1}$, and it can be shown that the theorem no longer holds for $k=n-2$.
Proof. Choose $c_{0}>0$ small enough so that Scal ${ }^{G_{c_{0}}}>0$. We then have $\mathrm{Scal}^{G_{c}} \geq \mathrm{Scal}^{G_{c_{0}}}$ for all $c \in\left[0, c_{0}\right]$. Hence
$$\mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right) \geq \inf \frac{\int_{\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}}\left(a|d u|_{G_{c}}^{2}+\operatorname{Scal}^{G_{c_{0}}} u^{2}\right) d v^{G_{c}}}{\|u\|_{L^{p}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)}^{2}}$$
where the infimum is taken over all non-zero smooth functions $u$ with compact support. By Hebey [25, Theorem 4.6, page 64], there exists a constant $A>0$ such that for all $c \in\left[0, c_{0}\right]$ and all smooth non-zero functions $u$ compactly supported in $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ we have
$$\|u\|_{L^{p}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)}^{2} \leq A \int_{\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}}\left(|d u|_{G_{c}}^{2}+u^{2}\right) d v^{G_{c}}$$
This implies that
$$\mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right) \geq \frac{1}{A} \min \left\{a, \operatorname{Scal}^{G_{c_{0}}}\right\}>0$$
for all $c \in\left[0, c_{0}\right]$, and together with Lemma 3.8 we obtain that
$$\inf _{c \in[0,1]} \mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)>0 .$$
Since $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ and $\mathbb{H}_{-c}^{k+1} \times \mathbb{S}^{n-k-1}$ are isometric we have
$$\Lambda_{n, k}^{(0)}=\inf _{c \in[-1,1]} \mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)>0 .$$
This ends the proof of Theorem 3.10. \(\square\)

As an immediate consequence we obtain that $\Lambda_{n, k}^{(1)}$ is positive.
Corollary 3.11. Let $0 \leq k \leq n-3$. Then $\Lambda_{n, k}^{(1)}>0$.
3.4. Proof of $\Lambda_{n, k}^{(2)}>0$.

Theorem 3.12. Let $0 \leq k \leq n-3$. Then $\Lambda_{n, k}^{(2)}>0$.
Proof. We prove this by contradiction. Assume that there exists a sequence $\left(c_{i}\right)$ of $c_{i} \in[-1,1]$ for which $\mu_{i}:=\mu^{(2)}\left(\mathbb{H}_{c_{i}}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ tends to a limit $l \leq 0$ as $i \rightarrow \infty$. After removing the indices $i$ for which $\mu_{i}$ is infinite we get for every $i$ a positive solution $u_{i} \in \Omega^{2}\left(\mathbb{H}_{c_{i}}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ of the equation
$$L^{G_{c_{i}}} u_{i}=\mu_{i} u_{i}^{p-1} .$$

By definition of $\Omega^{(2)}\left(\mathbb{H}_{c_{i}}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ we have
$$\frac{(n-k-2)^{2}(n-1)}{8(n-2)} \leq \mu_{i}\left\|u_{i}\right\|_{L^{\infty}}^{p-2},$$
which implies that $\mu_{i}>0$. We conclude that $l:=\lim _{i} \mu_{i}=0$. We cannot assume that $\left\|u_{i}\right\|_{L^{\infty}}$ is attained but we can choose points $x_{i} \in$ $\mathbb{H}_{c_{i}}^{k+1} \times \mathbb{S}^{n-k-1}$ such that $u_{i}\left(x_{i}\right) \geq \frac{1}{2}\left\|u_{i}\right\|_{L^{\infty}}$. Moreover, we can compose the functions $u_{i}$ with isometries so that all the $x_{i}$ are the same point $x$. From (8) we get
$$\frac{1}{2}\left(\frac{(n-k-2)^{2}(n-1)}{8(n-2) \mu_{i}}\right)^{\frac{1}{p-2}} \leq u_{i}(x) .$$
We define $m_{i}:=u_{i}(x)$. Since $\lim _{i \rightarrow \infty} \mu_{i}=0$ we have $\lim _{i \rightarrow \infty} m_{i}=\infty$. Restricting to a subsequence we can assume that $c:=\lim _{i} c_{i} \in[-1,1]$ exists. Define $\tilde{g}_{i}:=m_{i}^{\frac{4}{n-2}} G_{c_{i}}$. We apply Lemma 4.1 with $\alpha=1 / i$, $\left(V, \gamma_{\alpha}\right)=\mathbb{H}_{c_{i}}^{k+1} \times \mathbb{S}^{n-k-1},\left(V, \gamma_{0}\right)=\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}, q_{\alpha}=x_{i}=x$, and $b_{\alpha}=m_{i}^{\frac{2}{n-2}}$. For $r>0$ we obtain diffeomorphisms
$$\Theta_{i}: B^{n}(r) \rightarrow B^{G_{c_{i}}}\left(x, m_{i}^{-\frac{2}{n-2}} r\right)$$
such that the sequence $\Theta_{i}^{*}\left(\tilde{g}_{i}\right)$ tends to the flat metric $\xi^{n}$ on $B^{n}(r)$. We let $\tilde{u}_{i}:=m_{i}^{-1} u_{i}$. By (2) we then have
$$L^{\tilde{g}_{i}} \tilde{u}_{i}=\mu_{i} \tilde{u}_{i}^{p-1}$$
on $B^{G_{c_{i}}}\left(x_{i}, m_{i}^{-\frac{2}{n-2}} r\right)$ and
$$\begin{aligned}
\int_{B^{G_{c_{i}}}\left(x_{i}, m_{i}^{-\frac{2}{n-2}} r\right)} \tilde{u}_{i}^{p} d v^{\tilde{g}_{i}} & =\int_{B^{G_{c_{i}}}\left(x_{i}, m_{i}^{-\frac{2}{n-2}} r\right)} u_{i}^{p} d v^{G_{c_{i}}} \\
& \leq \int_{N} u_{i}^{p} d v^{G_{c_{i}}} \\
& \leq 1 .
\end{aligned}$$
Here we used $d v^{\tilde{g}_{i}}=m_{i}^{p} d v^{G_{c_{i}}}$. The last inequality comes from the fact that any function in $\Omega^{(2)}\left(\mathbb{H}_{c_{i}}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ has $L^{p}$-norm smaller than 1. Since
$$\Theta_{i}:\left(B^{n}(r), \Theta_{i}^{*}\left(\tilde{g}_{i}\right)\right) \rightarrow\left(B^{G_{c_{i}}}\left(x, m_{i}^{-\frac{2}{n-2}} r\right), \tilde{g}_{i}\right)$$
is an isometry we redefine $\tilde{u}_{i}$ as $\tilde{u}_{i} \circ \Theta_{i}$ which gives us solutions of
$$L^{\Theta_{i}^{*}\left(\tilde{g}_{i}\right)} \tilde{u}_{i}=\mu_{i} \tilde{u}_{i}^{p-1}$$
on $B^{n}(r)$ with $\int_{B^{n}(r)} \tilde{u}_{i}^{p} d v^{\Theta_{i}^{*}\left(\tilde{g}_{i}\right)} \leq 1$. Since $\left\|\tilde{u}_{i}\right\|_{L^{\infty}\left(B^{n}(r)\right)}=\tilde{u}_{i}(0)=1$ we can apply Lemma 4.2 with $V=\mathbb{R}^{n}, \alpha=1 / i, g_{\alpha}=\Theta_{i}^{*}\left(\tilde{g}_{i}\right)$, and $u_{\alpha}=\tilde{u}_{i}$ (we can apply this lemma since each compact set of $\mathbb{R}^{n}$ is
contained in some ball $\left.B^{n}(r)\right)$. This shows that there exists a non-negative $C^{2}$ function $u$ on $\mathbb{R}^{n}$ that does not vanish identically (since $u(0)=1$ ) and that satisfies
$$L^{\xi^{n}} u=a \Delta^{\xi^{n}} u=\bar{\mu} u^{p-1}$$
where $\bar{\mu}=0$. By (12) we further have
$$\int_{B^{n}(r)} u^{p} d v^{\xi^{n}}=\lim _{i \rightarrow \infty} \int_{B^{G_{c_{i}}}\left(x, m_{i}^{-\frac{2}{n-2}} r\right)} u_{i}^{p} d v^{G_{c_{i}}} \leq 1$$
for any $r>0$. In particular,
$$\int_{\mathbb{R}^{n}} u^{p} d v^{\xi^{n}} \leq 1 .$$
Lemma 4.3 below then implies the contradiction $0=\bar{\mu} \geq \mu\left(\mathbb{S}^{n}\right)$. This proves that $\Lambda_{n, k}^{(2)}$ is positive. \(\square\)
3.5. The constants $\Lambda_{n, 0}$. Now we show that
$$\Lambda_{n, 0}=\mu\left(\mathbb{S}^{n}\right)=n(n-1) \omega_{n}^{2 / n} .$$
The corresponding model spaces $\mathbb{H}_{c}^{1} \times \mathbb{S}^{n-1}$ carry the standard product metric $d t^{2}+\sigma^{n-1}$ of $\mathbb{R} \times \mathbb{S}^{n-1}$, independently of $c \in[-1,1]$. Thus $\Lambda_{n, 0}^{(i)}=$ $\mu^{(i)}\left(\mathbb{R} \times \mathbb{S}^{n-1}\right)$. Proposition 3.1 yields a conformal diffeomorphism from the cylinder $\mathbb{R} \times \mathbb{S}^{n-1}$ to $\mathbb{S}^{n} \backslash \mathbb{S}^{0}$, the $n$-sphere with north and south poles removed.

Lemma 3.13.
$$\Lambda_{n, 0}^{(i)} \leq \mu\left(\mathbb{S}^{n}\right)=n(n-1) \omega_{n}^{2 / n}$$
for $i=1,2$.
Proof. We use the notation of Proposition 3.1 with $k=0$. Then the standard metric on $S^{n}$ is
$$\sigma^{n}=(\sin s)^{2}\left(d t^{2}+\sigma^{n-1}\right)=(\cosh t)^{-2}\left(d t^{2}+\sigma^{n-1}\right) .$$
It follows that $\left(\omega_{n}\right)^{-2 / n}(\cosh t)^{-2}\left(d t^{2}+\sigma^{n-1}\right)$ is a (non-complete) metric of volume 1 and scalar curvature $n(n-1) \omega^{2 / n}=\mu\left(\mathbb{S}^{n}\right)$ on $\mathbb{H}_{c}^{1} \times$ $\mathbb{S}^{n-1}=\mathbb{R} \times \mathbb{S}^{n-1}$. This is equivalent to saying that
$$u(t):=\omega_{n}^{-\frac{n-2}{2 n}}(\cosh t)^{-\frac{n-2}{2}}$$
is a solution of (6) with $\mu=\mu\left(\mathbb{S}^{n}\right)$ and $\|u\|_{L^{p}}=1$ on $\mathbb{H}_{c}^{1} \times \mathbb{S}^{n-1}$ equipped with the product metric. Clearly we have $u \in L^{2}$, and $\|u\|_{L^{\infty}}=\omega_{n}^{-\frac{n-2}{2 n}}<\infty$. Thus $u \in \Omega^{(1)}\left(\mathbb{H}_{c}^{1} \times \mathbb{S}^{n-1}\right)$. As a consequence, we obtain $\Lambda_{n, 0}^{(1)} \leq n(n-1) \omega_{n}^{2 / n}$.

Further, we have
$$\mu\left(\mathbb{S}^{n}\right)\|u\|_{L^{\infty}}^{p-2}=n(n-1)>\frac{(n-0-2)^{2}(n-1)}{8(n-2)},$$
and thus $u \in \Omega^{(2)}\left(\mathbb{H}_{c}^{1} \times \mathbb{S}^{n-1}\right)$, which implies $\Lambda_{n, 0}^{(2)} \leq n(n-1) \omega_{n}^{2 / n}$. \(\square\)

Lemma 3.14. Let $u \in C^{2}\left(\mathbb{R} \times \mathbb{S}^{n-1}\right)$ be a solution of (6) on $\mathbb{R} \times \mathbb{S}^{n-1}$ with $\|u\|_{L^{p}} \leq 1, u \not \equiv 0$. Then $\mu \geq \mu\left(\mathbb{S}^{n}\right)$.

Proof. As above $\sigma^{n}=(\sin s)^{2}\left(d t^{2}+\sigma^{n-1}\right)$. If $u$ solves (6) with $h=$ $d t^{2}+\sigma^{n-1}$ then $\tilde{u}:=(\sin s)^{-\frac{n-2}{2}} u$ solves
$$L^{\sigma^{n}} \tilde{u}=\mu \tilde{u}^{p-1} .$$
Further $\tilde{u}^{p} d v^{\sigma^{n}}=u^{p} d v^{h}$, hence $\nu:=\|\tilde{u}\|_{L^{p}\left(S^{n} \backslash S^{0}, \sigma^{n}\right)} \leq 1$. For $\alpha>0$ small, we choose a smooth cut-off function $\chi_{\alpha}: S^{n} \rightarrow[0,1]$ which is 1 on $S^{n} \backslash U_{\alpha}\left(S^{0}\right)$, with support disjoint from $S^{0}$, and with $\left|d \chi_{\alpha}\right|_{\sigma^{n}} \leq 2 / \alpha$. Then using (65) in Appendix A. 3 we see that
$$\int_{\mathbb{S}^{n}}\left(\chi_{\alpha} \tilde{u}\right) L^{\sigma^{n}}\left(\chi_{\alpha} \tilde{u}\right) d v^{\sigma^{n}}=\mu \int_{\mathbb{S}^{n}} u^{p} \chi_{\alpha}^{2} d v^{\sigma^{n}}+a \int_{\mathbb{S}^{n}}\left|d \chi_{\alpha}\right|_{\sigma^{n}}^{2} \tilde{u}^{2} d v^{\sigma^{n}}$$
The first summand tends to $\mu \nu^{p}$ as $\alpha \searrow 0$. By Hölder's inequality the second summand is bounded by
$$\frac{4 a}{\alpha^{2}}\|\tilde{u}\|_{L^{p}\left(U_{\alpha}\left(S^{0}\right) \backslash S^{0}, \sigma^{n}\right)}^{2} \operatorname{Vol}\left(U_{\alpha}\left(S^{0}\right) \backslash S^{0}, \sigma^{n}\right)^{2 / n} \leq C\|\tilde{u}\|_{L^{p}\left(U_{\alpha}\left(S^{0}\right) \backslash S^{0}, \sigma^{n}\right)}^{2} \rightarrow 0$$
as $\alpha \searrow 0$. Together with $\lim _{\alpha \searrow 0}\left\|\chi_{\alpha} \tilde{u}\right\|_{L^{p}\left(S^{n} \backslash S^{0}, \sigma^{n}\right)}=\nu$ we obtain
$$\mu\left(\mathbb{S}^{n}\right) \leq J^{\sigma^{n}}\left(\chi_{\alpha} \tilde{u}\right) \rightarrow \mu \nu^{p-2} \leq \mu$$
as $\alpha \searrow 0$. \(\square\)

This lemma obviously implies $\Lambda_{n, 0}^{(i)} \geq \mu\left(\mathbb{S}^{n}\right)$ for $i=1,2$, and thus we have
$$\Lambda_{n, 0}=\Lambda_{n, 0}^{(1)}=\Lambda_{n, 0}^{(2)}=\mu\left(\mathbb{S}^{n}\right) .$$
3.6. The constants $\Lambda_{n, k}$ for $1 \leq k \leq n-3$. For $2 \leq k \leq n-4$ we have found an explicit positive lower bound on $\Lambda_{n, k}^{(0)}$ which will be published in [5]. Together with Remark 3.4 we obtain a lower bound for $\Lambda_{n, k}$, see also [6]. For $m:=k+1 \in\{3, \ldots, n-3\}$ we conclude
$$\Lambda_{n, m-1} \geq n a_{n}\left(\frac{Y_{m}}{m a_{m}}\right)^{\frac{m}{n}}\left(\frac{Y_{n-m}}{(n-m) a_{n-m}}\right)^{\frac{n-m}{n}}$$
A lower bound in the case $k=1$ and in the cases $(n, k)=(5,2)$ was established in [7]. These lower bounds are not optimal, but they are optimal up to a factor of at most 2.

We collected all known and conjectured values for $\Lambda_{n, k}$ for $n \leq 9$ in Figure 1. In the table, > 0 means that no explicit positive lower estimate has been worked out until now.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $n$ & $k$ & known $\Lambda_{n, k}$ & conjectured $\Lambda_{n, k}$ & $\mu\left(\mathbb{S}^{n}\right)$ \\
\hline 3 & 0 & 43.82323 & 43.82323 & 43.82323 \\
\hline 4 & 0 & 61.56239 & 61.56239 & 61.56239 \\
\hline 4 & 1 & 38.9 & 59.40481 & 61.56239 \\
\hline 5 & 0 & 78.99686 & 78.99686 & 78.99686 \\
\hline 5 & 1 & 56.6 & 78.18644 & 78.99686 \\
\hline 5 & 2 & 45.1 & 75.39687 & 78.99686 \\
\hline 6 & 0 & 96.29728 & 96.29728 & 96.29728 \\
\hline 6 & 1 & > 0 & 95.87367 & 96.29728 \\
\hline 6 & 2 & 54.77904 & 94.71444 & 96.29728 \\
\hline 6 & 3 & 49.98764 & 91.68339 & 96.29728 \\
\hline 7 & 0 & 113.5272 & 113.5272 & 113.5272 \\
\hline 7 & 1 & > 0 & 113.2670 & 113.5272 \\
\hline 7 & 2 & 74.50435 & 112.6214 & 113.5272 \\
\hline 7 & 3 & 74.50435 & 111.2934 & 113.5272 \\
\hline 7 & 4 & > 0 & 108.1625 & 113.5272 \\
\hline 8 & 0 & 130.7157 & 130.7157 & 130.7157 \\
\hline 8 & 1 & > 0 & 130.5398 & 130.7157 \\
\hline 8 & 2 & 92.24278 & 130.1272 & 130.7157 \\
\hline 8 & 3 & 95.76372 & 129.3551 & 130.7157 \\
\hline 8 & 4 & 92.24278 & 127.9414 & 130.7157 \\
\hline 8 & 5 & > 0 & 124.7747 & 130.7157 \\
\hline 9 & 0 & 147.8778 & 147.8778 & 147.8778 \\
\hline 9 & 1 & 109.2993 & 147.7507 & 147.8778 \\
\hline 9 & 2 & 109.4260 & 147.4615 & 147.8778 \\
\hline 9 & 3 & 114.3250 & 146.9519 & 147.8778 \\
\hline 9 & 4 & 114.3250 & 146.1089 & 147.8778 \\
\hline 9 & 5 & 109.4260 & 144.6521 & 147.8778 \\
\hline 9 & 6 & > 0 & 141.4740 & 147.8778 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Figure 1. Known and conjectured lower estimates for $\Lambda_{n, k}$.}
\end{table}
3.7. Speculation about $\Lambda_{n, k}$ for $k \geq 1$. We want to speculate about two relations that seem likely to us although we have no proof. Conformally, the model spaces $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$ can be viewed as an interpolation between $\mathbb{R}^{k+1} \times \mathbb{S}^{n-k-1}$ (for $c=0$ ) and the sphere $\mathbb{S}^{n}$ (for $c=1$ ). Since the sphere has the largest possible value of the conformal Yamabe constant we could hope that the function $c \mapsto \mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ is increasing for $c \in[0,1]$, or in particular
$$\mu^{(0)}\left(\mathbb{R}^{k+1} \times \mathbb{S}^{n-k-1}\right) \leq \mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$$
for all $c \in[-1,1]$. This would imply
$$\Lambda_{n, k}=\mu^{(0)}\left(\mathbb{R}^{k+1} \times \mathbb{S}^{n-k-1}\right) .$$

To formulate the second potential relation we define the following variant of $\mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}\right)$ :
$$\mu_{\mathbb{H}_{c}^{k+1}}^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k}\right):=\inf \left\{J^{G_{c}}(u) \mid u \in C_{0}^{\infty}\left(\mathbb{H}_{c}^{k+1}\right)\right\} .$$
Here $J^{G_{c}}$ is the functional of $\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k-1}$, but we only evaluate it for functions that are constant along the sphere $\mathbb{S}^{n-k-1}$. We ask, similarly to the Question formulated in the Introduction in [2], whether
$$\mu_{\mathbb{H}_{c}^{k+1}}^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k}\right)=\mu^{(0)}\left(\mathbb{H}_{c}^{k+1} \times \mathbb{S}^{n-k}\right) .$$
It seems likely to us that the answer is yes, if and only if $|c| \leq 1$.
An affirmative answer for $|c| \leq 1$ would imply, using a reflection argument, that we can restrict not only to functions that are constant along the sphere, but even to radial functions. Here a radial function is defined as a function of the form $u(x, y)=u\left(d^{\mathbb{H}_{c}^{k+1}}(x)\right)$ where $d^{\mathbb{H}_{c}^{k+1}}(x)$ is the distance from $x$ to a fixed point in $\mathbb{H}_{c}^{k+1}$. The constants $\Lambda_{n, k}$ could then be calculated numerically. For example we would obtain
$$\Lambda_{4,1}=\mu^{(0)}\left(\mathbb{R}^{2} \times \mathbb{S}^{2}\right)=59.40481 \ldots$$
and thus $\sigma\left(S^{2} \times S^{2}\right) \geq 59.40481 \ldots$, which should be compared to $\mu\left(\mathbb{S}^{4}\right)=61.56239 \ldots$ and $\mu\left(\mathbb{S}^{2} \times \mathbb{S}^{2}\right)=16 \pi=50.26548 \ldots$

Using the handle reduction techniques of the proof of the $h$-cobordism theorem, together with information about the spin bordism groups in low dimensions, we would be able to conclude the following lower bounds on $\sigma(M)$ for simply connected spin manifolds of dimension $n$ (and with vanishing index in the case $n=8$ ).

\begin{tabular}[t]{|l|l|}
\hline $n$ & $\sigma(M)>$ \\
\hline 5 & 75.3968 \\
\hline 6 & 91.683 \\
\hline 7 & 108.162 \\
\hline 8 & 124.774 \\
\hline
\end{tabular}
If $n=5,6,7$ we use that $M$ is spin bordant to a sphere, for $n=8$ we have that $M$ is spin bordant to a number of copies of $\mathbb{H} P^{2}$. For the standard metric we have $\mu\left(\mathbb{H} P^{2}\right)=144.959 \ldots$. In all four cases we would have $\sigma(M) / \sigma\left(\mathbb{S}^{n}\right)>0.95$. Similar conclusions can be drawn for non-spin manifolds.

These inequalities would imply for example that $\sigma\left(\mathbb{C} P^{3}\right)$ is not attained by the Fubini-Study metric, as $\mu\left(\mathbb{C} P^{3}\right)=82.9864 \ldots$ for this conformal class.

\section*{4. Limit spaces and limit solutions}

In the proofs of the main theorems we will construct limit solutions of the Yamabe equation on certain limit spaces. For this we need the following two lemmas.

Lemma 4.1. Let $V$ be an $n$-dimensional manifold. Let $\left(q_{\alpha}\right)$ be a sequence of points in $V$ that converges to a point $q$ as $\alpha \searrow 0$. Let $\left(\gamma_{\alpha}\right)$ be a sequence of metrics defined on a neighborhood $O$ of $q$ that converges to a metric $\gamma_{0}$ in the $C^{2}(O)$-topology. Finally, let $\left(b_{\alpha}\right)$ be a sequence of positive real numbers such that $\lim _{\alpha \searrow 0} b_{\alpha}=\infty$. Then for $r>0$ there exists for $\alpha$ small enough a diffeomorphism
$$\Theta_{\alpha}: B^{n}(r) \rightarrow B^{\gamma_{\alpha}}\left(q_{\alpha}, b_{\alpha}^{-1} r\right)$$
with $\Theta_{\alpha}(0)=q_{\alpha}$ such that the metric $\Theta_{\alpha}^{*}\left(b_{\alpha}^{2} \gamma_{\alpha}\right)$ tends to the flat metric $\xi^{n}$ in $C^{2}\left(B^{n}(r)\right)$.
Proof. Denote by $\exp _{q_{\alpha}}^{\gamma_{\alpha}}: U_{\alpha} \rightarrow O_{\alpha}$ the exponential map at the point $q_{\alpha}$ defined with respect to the metric $\gamma_{\alpha}$. Here $O_{\alpha}$ is a neighborhood of $q_{\alpha}$ in $V$ and $U_{\alpha}$ is a neighborhood of the origin in $\mathbb{R}^{n}$. We set
$$\Theta_{\alpha}: B^{n}(r) \ni x \mapsto \exp _{q_{\alpha}}^{\gamma_{\alpha}}\left(b_{\alpha}^{-1} x\right) \in B^{\gamma_{\alpha}}\left(q_{\alpha}, b_{\alpha}^{-1} r\right) .$$
It is easily checked that $\Theta_{\alpha}$ is the desired diffeomorphism. \(\square\)

Lemma 4.2. Let $V$ be an $n$-dimensional manifold. Let $\left(g_{\alpha}\right)$ be a sequence of metrics that converges to a metric $g$ in $C^{2}$ on all compact sets $K \subset V$ as $\alpha \searrow 0$. Assume that $\left(U_{\alpha}\right)$ is an increasing sequence of subdomains of $V$ such that $\bigcup_{\alpha} U_{\alpha}=V$. Let $u_{\alpha} \in C^{2}\left(U_{\alpha}\right)$ be a sequence of positive functions such that $\left\|u_{\alpha}\right\|_{L^{\infty}\left(U_{\alpha}\right)}$ is bounded independently of $\alpha$. We assume
$$L^{g_{\alpha}} u_{\alpha}=\mu_{\alpha} u_{\alpha}^{p-1}$$
where the $\mu_{\alpha}$ are numbers tending to $\bar{\mu}$. Then there exists a nonnegative function $u \in C^{2}(V)$, satisfying
$$L^{g} u=\bar{\mu} u^{p-1}$$
on $V$ and a subsequence of $u_{\alpha}$ that tends to $u$ in $C^{1}$ on each open set $\Omega \subset V$ with compact closure. In particular
$$\|u\|_{L^{\infty}(K)}=\lim _{\alpha \searrow 0}\left\|u_{\alpha}\right\|_{L^{\infty}(K)},$$
and
$$\int_{K} u^{r} d v^{g}=\lim _{\alpha \searrow 0} \int_{K} u_{\alpha}^{r} d v^{g_{\alpha}}$$
for any compact set $K$ and any $r \geq 1$.
Proof. Let $K$ be a compact subset of $V$ and let $\Omega$ be an open set with smooth boundary and compact closure in $V$ such that $K \subset \Omega$. From equation (9) and the boundedness of $\left\|u_{\alpha}\right\|_{\infty}$ we see with standard results on elliptic regularity (see for example [18]) that $\left(u_{\alpha}\right)$ is bounded
in the Sobolev space $H^{2,2 n}(\Omega, g)$, that is all derivatives of $\left.u_{\alpha}\right|_{\Omega}$ up to second order are bounded in $L^{2 n}(\Omega)$ ). As this Sobolev space embeds compactly into $C^{1}(\Omega)$, a subsequence of $\left(u_{\alpha}\right)$ converges in $C^{1}(\Omega)$ to a function $u^{\Omega} \in C^{1}(\Omega), u^{\Omega} \geq 0$, depending on $\Omega$. Let $\varphi \in C^{\infty}(\Omega)$ be compactly supported in $\Omega$. Multiplying Equation (9) by $\varphi$ and integrating over $\Omega$, we obtain that $u^{\Omega}$ satisfies Equation (10) weakly on $\Omega$. By standard regularity results $u^{\Omega} \in C^{2}(\Omega)$ and satisfies Equation (10).

As a next step we choose an increasing sequence of compact sets $K_{m}$ satisfying $\bigcup_{m} K_{m}=V$. Using the above arguments and taking successive subsequences it follows that $\left(u_{\alpha}\right)$ converges to functions $u_{m} \in$ $C^{2}\left(K_{m}\right)$ that solve Equation (10) and satisfy $u_{m} \geq 0$ and $\left.u_{m}\right|_{K_{m-1}}=$ $u_{m-1}$. We define $u$ on $V$ by $u=u_{m}$ on $K_{m}$. By taking a diagonal subsequence of $\left(u_{\alpha}\right)$ we get that $\left(u_{\alpha}\right)$ tends to $u$ in $C^{1}$ on any compact set $K \subset V$. This ends the proof of Lemma 4.2. \(\square\)

The next Lemma is useful when the sequence of metrics in Lemma 4.2 converges to the flat metric $\xi^{n}$ on $\mathbb{R}^{n}$.

Lemma 4.3. Let $\xi^{n}$ be the standard flat metric on $\mathbb{R}^{n}$, and assume that $u \in C^{2}\left(\mathbb{R}^{n}\right), u \geq 0, u \not \equiv 0$ satisfies
$$L^{\xi^{n}} u=\mu u^{p-1}$$
for some $\mu \in \mathbb{R}$. Assume in addition that $u \in L^{p}\left(\mathbb{R}^{n}\right)$ and that
$$\|u\|_{L^{p}\left(\mathbb{R}^{n}\right)} \leq 1 .$$
Then $\mu \geq \mu\left(\mathbb{S}^{n}\right)$.
Proof. The map $\varphi: \mathbb{R} \times \mathbb{S}^{n-1} \rightarrow \mathbb{R}^{n} \backslash\{0\}, \varphi(t, x)=e^{t} x$, is a conformal diffeomorphism with
$$d t^{2}+\sigma^{n-1}=e^{-2 t} \varphi^{*} \xi^{n} .$$
Thus if $u$ is a solution of (13), then $\hat{u}:=e^{(n-2) t / 2} u \circ \varphi$ is a solution of $L^{d t^{2}+\sigma^{n-1}} \hat{u}=\mu \hat{u}^{p-1}$ and $\|\hat{u}\|_{L^{p}\left(\mathbb{R} \times \mathbb{S}^{n-1}\right)}=\|u\|_{L^{p}\left(\mathbb{R}^{n}\right)} \leq 1$. The result now follows from Lemma 3.14. \(\square\)

\section*{5. $L^{2}$-estimates on $W S$-bundles}

Manifolds with a certain structure of a double bundle will appear in the proofs of our main results. In this section we derive $L^{2}$-estimates for solutions to a perturbed Yamabe equation on a $W S$-bundle.
5.1. Definition and statement of the result. Let $n \geq 1$ and $0 \leq$ $k \leq n-3$ be integers. Let $W$ be a closed manifold of dimension $k$ and let $I$ be an interval. By a $W S$-bundle we will mean the product $P:=I \times W \times S^{n-k-1}$ equipped with a metric of the form
$$g_{\mathrm{WS}}=d t^{2}+e^{2 \varphi(t)} h_{t}+\sigma^{n-k-1}$$
where $h_{t}$ is a smooth family of metrics on $W$ depending on $t \in I$ and $\varphi$ is a function on $I$. The condition $k \leq n-3$ implies that the sphere $S^{n-k-1}$ carries positive scalar curvature, which is an essential ingredient in the proof of Theorem 5.2. Let $\pi: P \rightarrow I$ be the projection onto the first factor and let $F_{t}:=\pi^{-1}(t)=\{t\} \times W \times S^{n-k-1}$. The metric induced on $F_{t}$ is $g_{t}:=e^{2 \varphi(t)} h_{t}+\sigma^{n-k-1}$. Let $H_{t}$ be the mean curvature of $F_{t}$ in $P$, that is $H_{t} \partial_{t}$ is the mean curvature vector of $F_{t}$. We always use the sign convention for the mean curvature vector for which it points in the direction of decreasing volume of $F_{t}$. The mean curvature is given by the formula
$$H_{t}=-\frac{k}{n-1} \varphi^{\prime}(t)-e\left(h_{t}\right)$$
with $e\left(h_{t}\right):=\frac{1}{2(n-1)} \operatorname{tr}_{h_{t}}\left(\partial_{t} h_{t}\right)$. Clearly, $e\left(h_{t}\right)=0$ if $t \mapsto h_{t}$ is constant. The derivative of the volume element $d v^{g_{t}}$ of $F_{t}$ is
$$\partial_{t} d v^{g_{t}}=-(n-1) H_{t} d v^{g_{t}} .$$
It is straightforward to check that the scalar curvatures of $g_{\mathrm{WS}}$ and $h_{t}$ are related by (see Appendix A. 2 for details)
$$\begin{aligned}
\text { Scal }{ }^{g_{\mathrm{WS}}}= & e^{-2 \varphi(t)} \operatorname{Scal}{ }^{h_{t}}+(n-k-1)(n-k-2) \\
& -k(k+1) \varphi^{\prime}(t)^{2}-2 k \varphi^{\prime \prime}(t)-(k+1) \varphi^{\prime}(t) \operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right) \\
& +\frac{3}{4} \operatorname{tr}\left(\left(h_{t}^{-1} \partial_{t} h_{t}\right)^{2}\right)-\frac{1}{4}\left(\operatorname{tr}\left(h_{t}^{-1} \partial_{t} h_{t}\right)\right)^{2}-\operatorname{tr}\left(h_{t}^{-1} \partial_{t}^{2} h_{t}\right) .
\end{aligned}$$

Definition 5.1. We say that condition $\left(A_{t}\right)$ holds if the following assumptions are true:
\begin{itemize}
\item[1.] ) $t \mapsto h_{t}$ is constant,
\item[2.] ) $e^{-2 \varphi(t)} \inf _{x \in W} \operatorname{Scal}^{h_{t}}(x) \geq-\frac{n-k-2}{32} a$,
\item[3.] ) $\left|\varphi^{\prime}(t)\right| \leq 1$,
\item[4.] ) $0 \leq-2 k \varphi^{\prime \prime}(t) \leq \frac{1}{2}(n-1)(n-k-2)^{2}$.
\end{itemize}

Similarly, we say that condition $\left(B_{t}\right)$ holds if the following assumptions are true:
\begin{itemize}
\item[1.] ) $t \mapsto \varphi(t)$ is constant,
\item[2.] ) $\inf _{x \in F_{t}} \operatorname{Scal}^{g_{\mathrm{WS}}}(x) \geq \frac{1}{2} \mathrm{Scal}^{\sigma^{n-k-1}}=\frac{1}{2}(n-k-1)(n-k-2),\left(B_{t}\right)$
\item[3.] ) $\frac{(n-1)^{2}}{2} e\left(h_{t}\right)^{2}+\frac{n-1}{2} \partial_{t} e\left(h_{t}\right) \geq-\frac{3}{64}(n-k-2)$.
\end{itemize}

Let $P$ be $W S$-bundle equipped with a metric $G$ that is close to $g_{\mathrm{WS}}$ in a sense to be made precise later. Let $\alpha, \beta \in \mathbb{R}$ be such that $[\alpha, \beta] \subset I$. Our goal is to derive an estimate for the distribution of $L^{2}$-norm of a positive solution to the Yamabe equation
$$L^{G} u=\mu u^{p-1} .$$