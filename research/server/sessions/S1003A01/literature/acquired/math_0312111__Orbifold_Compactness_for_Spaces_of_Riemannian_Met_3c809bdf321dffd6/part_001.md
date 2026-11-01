---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: [math/0312111] Orbifold Compactness for Spaces of Riemannian Metrics and Applications]

---
source_file: math_0312111.pdf
converter: mathpix
format: mmd
---

\title{
ORBIFOLD COMPACTNESS FOR SPACES OF RIEMANNIAN METRICS AND APPLICATIONS
}

\author{
MICHAEL T. ANDERSON
}

\section*{1. Introduction}

The Cheeger-Gromov compactness theorem, cf. [C], [G], [CGv] states that the space of Riemannian $n$-manifolds $\left(M^{n}, g\right)$ satisfying the bounds
$$|R| \leq \Lambda, \text { vol } \geq v_{0}, \operatorname{diam} \leq D,$$
is precompact in the $C^{1, \alpha}$ topology. Here $R$ denotes the Riemann curvature tensor, vol the volume and diam the diameter of $(M, g)$. Thus, for any sequence of metrics $g_{i}$ on $n$-manifolds $M_{i}$ satisfying (1.1), there is a subsequence, also called $g_{i}$, and diffeomorphisms $\phi_{i}: M_{\infty} \rightarrow M_{i}$ such that the metrics $\phi_{i}^{*} g_{i}$ converge in the $C^{1, \alpha}$ topology to a limit metric $g_{\infty}$ on $M_{\infty}$, for any $\alpha<1$. In particular, there are only finitely many diffeomorphism types of $n$-manifolds $M$ which admit Riemannian metrics satisfying (1.1). In addition, the convergence is in the weak $L^{2, p}$ topology, and the limit metric $g_{\infty}$ is $L^{2, p}$, for any $p<\infty$.

While conceptually important, this result is of somewhat limited applicability in itself, since the bound on the full curvature tensor $R$ is very strong and only realizable in special situations. A direct generalization of this result to the more natural situation where one imposes bounds on the Ricci curvature, i.e.
$$|\operatorname{Ric}| \leq \lambda, \text { vol } \geq v_{0}, \operatorname{diam} \leq D,$$
is false. For example, there are sequences of metrics on the double of the tangent bundle of $S^{2}$, i.e. $T S^{2} \cup_{\partial} T S^{2}$, satisfying (1.2), which converge in the Gromov-Hausdorff topology to a metric on the double of the cone on $\mathbb{R P}^{3}, C\left(\mathbb{R P}^{3}\right) \cup_{\partial} C\left(\mathbb{R} \mathbb{P}^{3}\right)$, cf. [An2]. The limit is not a smooth manifold, but is an orbifold, with two orbifold singular points, (the vertices of the cones).

On the other hand, in dimension 4, it was shown in [An3] that such degeneration to orbifolds (with point singularities) is the only possible degeneration under the bounds (1.2); any sequence $g_{i}$ of metrics on a fixed 4-manifold $M^{4}$ satisfying the bounds (1.2) has a subsequence converging in the Gromov-Hausdorff topology to an orbifold, with a bounded number of singular points. The convergence is $C^{1, \alpha}$ away from singular points. In fact, if one enlarges the class of manifolds to include orbifolds, then the space of orbifold metrics is compact in the $C^{1, \alpha}$ and weak $L^{2, p}$ topologies in a natural sense. These orbifold compactness results were first proved for Einstein metrics in [An1] and [BKN], and later generalized to the setting (1.2). Analogous results hold in all dimensions, and with varying manifolds, if one adds a fixed bound on the $L^{n / 2}$ norm of the curvature tensor, cf. [An3].

In this paper, we consider orbifold compactness results which replace the apriori bound on the Ricci curvature in (1.2) with other curvature bounds. These results are then applied to prove orbifold compactness theorems for metrics which are critical points of other natural functionals on the space of metrics besides Einstein metrics.

To describe the results, a precise definition of the orbifolds that arise in this context is needed.

\footnotetext{
Partially supported by NSF Grant DMS 0305865.
}

Definition. An orbifold $V$ is a topological space which is a smooth manifold off a finite set of singular points $\left\{q_{k}\right\}$. A neighborhood of each singular point is a finite union of cones on spherical space-forms $C\left(S^{n-1} / \Gamma\right), \Gamma \subset S O(n)$, where the vertex of each cone is identified with the point $q_{k}$. A metric $g$ on $V$ is $C^{m, \alpha}$ if $g$ is $C^{m, \alpha}$ (locally) on $V \backslash\left\{q_{k}\right\}$, and, in a local uniformization $B^{n} \backslash\{0\}$ of each cone, the metric $g$ extends to a $C^{0}$ metric on the ball $B^{n}$.

On the one hand, this definition is more restrictive than the definition due to Thurston [Th], which allows for codimension 2 cone-like singular sets. On the other hand, the definition allows for several spherical cones to be joined at a single vertex. An orbifold will be called irreducible if there is exactly one cone at each singular point.

We first describe the main result in general, and then discuss applications to critical metrics. Let $B_{x}(r)$ denote the geodesic ball of radius $r$ about $x$ and $S_{x}(r)$ the corresponding geodesic sphere in a complete Riemannian manifold ( $M, g$ ). For simplicity, all manifolds are assumed to be connected and oriented.

Theorem 1.1. Let $\mathcal{M}=\mathcal{M}\left(\Lambda, \nu_{0}, \delta_{0}, C_{0}\right)$ be the space of closed $n$-dimensional Riemannian manifolds $(M, g), n \geq 3$, satisfying the bounds
$$\operatorname{vol}_{g} M=1, \int_{M}|R|^{n / 2} d V_{g} \leq \Lambda$$
together with the following two conditions:
\begin{itemize}
\item[(i)] . (Non-Collapse). There exists $\nu_{0}>0$ such that
$$v o l B_{x}(r) \geq \nu_{0} r^{n},$$
for all $x \in M$ and $r \leq 1$.
\item[(ii)] (Small curvature estimate). There exists $\delta_{0}>0$ and $C_{0}<\infty$ such that if $\left(\int_{B_{x}(r)}|R|^{n / 2}\right)^{2 / n} \leq$ $\delta_{0}$, then
$$\sup _{B_{x}(r / 2)}|R| \leq\left(\frac{C_{0}}{v o l B_{x}(r)} \int_{B_{x}(r)}|R|^{n / 2} d V_{g}\right)^{2 / n}$$
\end{itemize}

Then for any fixed values of $\Lambda, \nu_{0}, \delta_{0}, C_{0}$ and $\alpha<1$, the space $\mathcal{M}$ is $C^{1, \alpha}$ orbifold compact, in that any sequence of metrics $g_{i}$ on $n$-manifolds $M_{i}$ satisying the bounds (1.3)-(1.5) has a subsequence converging, modulo diffeomorphisms, to a limit orbifold ( $V, g$ ), with $C^{1, \alpha}$ metric $g_{\infty}$. The convergence $\left(M_{i}, g_{i}\right) \rightarrow(V, g)$ is in the Gromov-Hausdorff topology, and in the $C^{1, \alpha}$ topology, uniformly on compact subsets of $V_{0}=V \backslash\left\{q_{k}\right\}$, where $\left\{q_{k}\right\}$ is the finite set of singular points. In particular, there are smooth embeddings of $V_{0}$ into $M_{i}$, for $i$ sufficiently large. The limit metric $g_{\infty}$ is locally in $L^{2, p}$ and the sequence converges uniformly on compact sets in the weak $L^{2, p}$ topology on $V_{0}$, for any $p<\infty$.

In addition, there is a bound on the number of orbifold singularities, the number of cones, and the order of local fundamental groups, depending only on $\Lambda, \nu_{0}, \delta_{0}$ and $C_{0}$.

We make some comments on the hypotheses. The volume bound (1.3) is of course just a normalization of $(M, g)$. The bound (1.4) requires that the volume of balls is not too small compared with the volume of Euclidean balls of the same radius. Without such a hypothesis, the structure of the singular set of limits is much more complicated, and has not been analysed in detail. The local curvature estimate (1.5), as well as the global bound (1.3) are analogues of the curvature bound (1.1) in Gromov's compactness theorem. Both hypotheses can be realized for natural classes of metrics, especially on 4-manifolds. On the other hand, in analogy to (1.2), the bound on $\sup _{B(r / 2)}|R|$ in (1.5) can be weakened to a bound on $\sup _{B(r / 2)} \mid$ Ric $\mid$, cf. Remark 2.11.

It is a consequence of the proof of Theorem 1.1 that there are only finitely many diffeomorphism types of $n$-manifolds in $\mathcal{M}\left(\Lambda, \nu_{0}, \delta_{0}, C_{0}\right)$, cf. Remark 2.10. Also, Theorem 1.1 holds if $\mathcal{M}$ is replaced by the corresponding space of orbifolds, cf. Remark 2.12.

There are numerous examples of metrics satisfying the bounds (1.3)-(1.5) which do in fact converge to such orbifold limits; see §2.3 and §3 for further discussion. Although the regular part $V_{0}$ of the limit orbifold $V$ embeds in $M_{i}$, for $i$ sufficiently large, in general the topology of the complement $M \backslash V_{0}$ can be arbitrary, at least if $\Lambda$ in (1.3) is sufficiently large, cf. Remark 2.9. Note that when $n=\operatorname{dim} M$ is odd, there are no orientable $(n-1)$-dimensional spherical space forms except $S^{n-1}$. Hence, all cones at singular points are balls $B^{n}$. Even if the limit $V$ is a smooth manifold $M_{\infty}$, and $M_{i}$ is diffeomorphic to $M_{\infty}$, the convergence of the metrics $g_{i}$ may not be smooth, i.e. $C^{1, \alpha}$, near the points $q_{k}$.

Suppose that one adds the bound
$$\operatorname{volB}_{x}(r) \leq V_{0} r^{n}, \forall x \in M, r \leq 1,$$
for some $V_{0}<\infty$ to the hypotheses of Theorem 1.1. Then the result follows rather easily from the proof of orbifold compactness under the bounds (1.2) in [An3]; the main point is that the bounds (1.2) imply the bound (1.6) via the Bishop-Gromov volume comparison theorem. The proof of Theorem 1.1 when (1.6) holds is given in §2.1.

With this understood, the main issue in the proof of Theorem 1.1 is to prove that (1.6) follows from the bounds (1.3)-(1.5). To do this, we need the following minor variation of standard definitions of asymptotically locally Euclidean spaces.

Definition. A complete Riemannian $n$-manifold $(N, g)$ is ALE (asymptotically locally Euclidean) if there is compact set $K \subset N$ such that each component $E_{j}, j=1, \ldots, \kappa$ of $N \backslash K$ is diffeomorphic to $\left(\mathbb{R}^{n} \backslash B\right) / \Gamma_{j}$, where $B$ is the unit ball about $\{0\} \in \mathbb{R}^{n}$ and $\Gamma_{j}$ is a finite subgroup of $S O(n)$, acting isometrically on $\mathbb{R}^{n}$. Further, there is a chart $\Phi: \widetilde{E}_{j} \rightarrow \mathbb{R}^{n} \backslash B$ in which the metric $\widetilde{g}=\Phi^{*} g$ satisfies
$$\begin{aligned}
\widetilde{g}_{a b} & =\delta_{a b}+o(1) \\
\left|\partial \widetilde{g}_{a b}\right|_{C^{\alpha}} & =O\left(r^{-1-\alpha}\right)
\end{aligned}$$
for all $\alpha<1$.
The following characterization of ALE spaces is then the main tool used to establish (1.6).
Theorem 1.2. Let $(N, g)$ be a complete, non-compact Riemannian $n$-manifold, $n \geq 3$, satisfying
$$v o l B_{x}(r) \geq \nu_{0} r^{n},$$
for some $\nu_{0}>0$ and all $x \in N, r<\infty$. Suppose also that
$$\int_{N}|R|^{n / 2} d V \leq \Lambda<\infty,$$
and that the small curvature estimate (1.5) holds, for some given $\delta_{0}, C_{0}$.
Then $(N, g)$ is ALE, and the number $\kappa$ of ends is bounded by $\nu_{0}, \Lambda, \delta_{0}$ and $C_{0}$. Further, there is a constant $V_{0}$, depending only on $\nu_{0}, \Lambda, \delta_{0}$ and $C_{0}$, such that for all $x$ and $r$,
$$\operatorname{volB}_{x}(r) \leq V_{0} r^{n} .$$
The asymptotic volume ratio is given by
$$\lim _{r \rightarrow \infty} \frac{\operatorname{volB}_{x}(r)}{r^{n}}=\sum_{j=1}^{\kappa} \frac{\omega_{n}}{\left|\Gamma_{j}\right|},$$
where $\omega_{n}$ is the volume of the unit ball in $\mathbb{R}^{n}$.

The proof of Theorem 1.2 is given in §2.2. The fact that Theorem 1.2 implies (1.6) and thus the remainder of the proof of Theorem 1.1 is given in §2.3.

Next we state some applications of Theorem 1.1 to special classes of Riemannian metrics, particularly on 4-manifolds. As perhaps the main example, consider the $L^{2}$ norm of the Weyl curvature as a functional on the space of metrics on a 4-manifold $M=M^{4}$ :
$$\mathcal{W}(g)=\int_{M}\left|W_{g}\right|^{2} d V_{g}$$
Critical points of this functional are Bach-flat metrics, i.e. metrics satisfying the Euler-Lagrange equation
$$\delta \delta W+\frac{1}{2} W(R i c)=0,$$
where $W(\cdot)$ denotes the action of $W$ on symmetric bilinear forms. Via the Bianchi identity, this is equivalent to
$$\delta d\left(\text { Ric }-\frac{s}{6} g\right)-W(\text { Ric })=0$$
The functional $\mathcal{W}$ is conformally invariant, and so one needs to choose a representative of the conformal class. For the purposes here, it is most useful to choose a Yamabe representative, i.e. a metric $\gamma$ of constant scalar curvature minimizing the Yamabe functional in conformal class $[\gamma]$; (the fact that $\gamma$ may not be unique is of no consequence).

Well-known examples of Bach-flat metrics on 4-manifolds are metrics conformal to Einstein metrics, conformally flat metrics, and half-conformally flat metrics, i.e self-dual or anti-selfdual metrics, for which $W^{-}$or $W^{+}=0$, respectively. The analogue of Theorem 1.1 in this context is the following:

Theorem 1.3. Let $M$ be a fixed closed 4-manifold. The space $\mathcal{C}^{+}$of Bach-flat unit volume Yamabe metrics on $M$, for which the scalar curvature $s$ of $g$ satisfies
$$s_{g} \geq s_{0}>0,$$
and the $L^{2}$ norm of the Weyl curvature satisfies
$$\int_{M}|W|^{2} \leq \Lambda,$$
for some $s_{0}>0$ and $\Lambda<\infty$, is orbifold precompact in the $C^{\infty}$ topology.
We note that since Bach-flat metrics are critical for $\mathcal{W}$, the functional $\mathcal{W}$ is constant on connected components of moduli spaces of Bach-flat metrics. This result is the exact analogue of a result proved for Einstein metrics on 4 -manifolds in [An1], [BKN]. Further discussion regarding Theorem 1.3, and related results for critical points of other natural curvature functionals on the space of metrics are proved in §3. For a selection of recent work related to the issues of this paper, see for instance, [Ak], [CH], [CQY], [Lo], [PT], and [TV1,2].

Finally we should include a comment on the history of this work. In analogy to the results established for Einstein metrics, G. Tian suggested to the author in 1993 that Theorem 1.3 might be true, and proposed working jointly on this project. Rather quickly, we realized that the main obstacle to carrying this out was to establish some version of Theorem 1.2. By early 1995, the author had developed the basic ideas leading to a proof of (a version of) Theorem 1.2 and we had agreed that the arguments were in place to begin and complete a manuscript on the work. Unfortunately, both Tian and the author became involved with other, more pressing, projects and the work just lingered without further attention.

With the recent appearance of [TV1], the author decided it was time to complete his ideas and approach to the problem, resulting in this paper. The results of [TV1] and [TV2] are related, but not identical to the results proved here.

While the overall strategy of the proof of Theorem 1.2, (and the other results above), is the same as that developed by the author in 1994-95, more recent results on the structure of the cut locus of Riemannian manifolds have been incorporated, allowing for a simplification of certain technical aspects of the proof.

I would like to thank Gang Tian for suggesting that Theorem 1.3 might be true, and for our early collaboration on the project. My thanks also to John Lott and Marc Herzlich for remarks and correspondence which helped to clarify the exposition of the paper.

\section*{2. General Orbifold Compactness.}

This section is concerned with the proofs of Theorems 1.1 and 1.2. In §2.1, we discuss the proof of Theorem 1.1 in case the bound (1.6) holds, i.e.
$$\operatorname{vol} B_{x}(r) \leq V_{0} r^{n}, r \leq 1,$$
for some (arbitrary) constant $V_{0}<\infty$. The proof in this case is essentially identical to that of [An1], to which we refer for some further details, if needed. Following this, we explain which parts of this proof generalize to the case where (2.1) is not assumed, and indicate why Theorem 1.1 should then follow from Theorem 1.2. Theorem 1.2 is proved in §2.2, while the proof of Theorem 1.1 is then quite easily completed in §2.3.
§2.1. In this subsection, we prove Theorem 1.1 in case (2.1) holds. Thus, let $\left(M_{i}, g_{i}\right)$ be any sequence of closed Riemannian $n$-manifolds satisfying (1.3)-(1.5) and (2.1). The volume bounds (1.4) and (2.1) imply a uniform upper bound $N(r / 2, r)$ on the number of disjoint geodesic balls of radius $r / 2$ in any $r$-ball, depending only on $\nu_{0}, V_{0}$. Any maximal collection of disjoint balls of radius 1/2 in $\left(M_{i}, g_{i}\right)$ gives a covering of $\left(M_{i}, g_{i}\right)$ by balls of radius 1. Hence, the volume bounds imply an upper bound on the cardinality of such a collection of balls, and consequently, one has a uniform upper bound on the diameter:
$$\operatorname{diam}\left(M_{i}, g_{i}\right) \leq D=D\left(\nu_{0}, V_{0}\right) .$$
Since one also has a uniform bound on the number $N(\varepsilon, R)$ of disjoint $\varepsilon$-balls in any $R$-ball of $\left(M_{i}, g_{i}\right)$, Gromov's weak compactness theorem [G] implies that a subsequence of $\left(M_{i}, g_{i}\right)$ converges in the Gromov-Hausdorff topology to a complete length space $\left(X, d_{\infty}\right)$. Thus we need to examine the structure of $\left(X, g_{\infty}\right)$, and improve the convergence to the limit.

For $\delta_{0}$ as in (1.5), and any given $r>0$, let $\left\{x_{k}\right\}$ be a maximal $r / 2$ separated set, (depending on $i)$, in $\left(M_{i}, g_{i}\right)$. Thus, the geodesic balls $B_{x_{k}}\left(\frac{r}{2}\right)$ are disjoint while the balls $B_{x_{k}}(r)$ cover $M_{i}$. (The choice of $\left\{x_{k}\right\}$ is of course not unique, but this is of no concern here). Let
$$G_{i}^{r}=\cup\left\{B_{x_{k}}(r): \int_{B_{x_{k}}(2 r)}|R|^{n / 2} d V<\delta_{0}\right\}$$
where $R=R_{g_{i}}$ is the curvature tensor, and similarly, let
$$B_{i}^{r}=\cup\left\{B_{x_{k}}(r): \int_{B_{x_{k}}(2 r)}|R|^{n / 2} d V \geq \delta_{0}\right\}$$
All quantities here are with respect to $\left(M_{i}, g_{i}\right)$. Hence for each $i, M_{i}=G_{i}^{r} \cup B_{i}^{r}$. Observe that there is uniform bound on the number $Q_{i}^{r}$ of $r$-balls in $B_{i}^{r}$ :
$$Q_{i}^{r} \leq \frac{\Lambda}{\delta_{0}},$$
independent of $i, r$. Further, exactly as in the proof of (2.2), by (1.4) and (2.1) there is a uniform bound on the intrinsic diameter of the geodesic annuli $A_{x}\left(\frac{1}{2} r, 2 r\right)$,
$$\operatorname{diam} A_{x}\left(\frac{1}{2} r, 2 r\right) \leq D r,$$
at arbitrary base points $x \in\left(M_{i}, g_{i}\right)$, with $D=D\left(\nu, V_{0}\right)$. For the same reasons, there is a uniform upper bound on the number of components of $A_{x}\left(\frac{1}{2} r, 2 r\right)$. By (2.1) and (2.5), the total volume of $B_{i}^{r}$ satisfies $\operatorname{vol} B_{i}^{r} \leq V_{0} Q(2 r)^{n}$, and so is small when $r$ is small. Hence, most of the volume of $\left(M_{i}, g_{i}\right)$ is contained in $G_{i}^{r}$.

The small curvature estimate (1.5) implies a uniform curvature bound on $G_{i}^{r}$ :
$$|R| \leq C r^{-2} \text { on } G_{i}^{r} .$$
In fact (2.7) holds on the $r / 2$ thickening of $G_{i}^{r}$. It then follows from a local version of the smooth (i.e. $C^{1, \alpha} \cap L^{2, p}$ ) Gromov compactness theorem, cf. [An1] or [An3] for example, that for any given $r>0$, a subsequence of $G_{i}^{r}$ converges in the $C^{1, \alpha}$ and weak $L^{2, p}$ topologies to a limit manifold $G_{\infty}^{r}$ with limit $C^{1, \alpha} \cap L^{2, p}$ metric $g_{\infty}^{r}$. In particular, $G_{\infty}^{r}$ and $G_{i}^{r}$ are diffeomorphic, for $i$ large, and there exist smooth embeddings $F_{i}^{r}: G_{\infty}^{r} \rightarrow G_{i}^{r} \subset M_{i}$ such that $\left(F_{i}^{r}\right)^{*}\left(g_{i}\right)$ converges in $C^{1, \alpha}$ to $g_{\infty}^{r}$.

Now choose a sequence $r_{j} \rightarrow 0$, with $r_{j+1}=\frac{1}{2} r_{j}$, and perform the above construction for each $j$. Let $G_{i}\left(r_{m}\right)=\left\{x \in\left(M_{i}, g_{i}\right): x \in G_{i}^{j}\right.$, for some $\left.j \leq m\right\}$, so that one has inclusions
$$G_{i}\left(r_{1}\right) \subset G_{i}\left(r_{2}\right) \subset \ldots \subset M_{i}$$
By the argument above, each $G_{i}\left(r_{m}\right) \subset\left(M_{i}, g_{i}\right)$, for $m$ fixed, has a subsequence converging smoothly, i.e. in $C^{1, \alpha}$ and weak $L^{2, p}$, to a limit $G_{\infty}\left(r_{m}\right)$. Clearly $G_{\infty}\left(r_{m}\right) \subset G_{\infty}\left(r_{m+1}\right)$ and we set
$$G=\cup_{1}^{\infty} G\left(r_{m}\right),$$
with the induced metric $g_{\infty}$. Thus, $\left(G_{\infty}, g_{\infty}\right)$ is $C^{1, \alpha}$ and $L^{2, p}$ smooth and for any $m$, there are smooth embeddings $F_{i}^{m}: G\left(r_{m}\right) \rightarrow M_{i}$, for $i$ sufficiently large, such that $\left(F_{i}^{m}\right)^{*}\left(g_{i}\right)$ converges in $C^{1, \alpha}$ to the metric $g_{\infty}$.

Let $\bar{G}$ be the metric completion of $G$ w.r.t. $g_{\infty}$. Then there is a finite set of points $q_{k}, k=1, \ldots, Q$, such that
$$\bar{G}=G \cup\left\{q_{k}\right\} .$$
This follows since there is a uniform upper bound (2.5) on the cardinality of $B_{i}^{r}$, for all $r$ small, and all $i$, independent of $r, i$. It is then easy to see that a subsequence of $\left(M_{i}, g_{i}\right)$ converges to the length space $\left(\bar{G}, g_{\infty}\right)$ in the Gromov-Hausdorff topology, so that $X=\bar{G}$. Moreover, by the construction of $G$, for $i$ sufficiently large, and for any compact domain $K \subset G$, there are embeddings $F_{i}: K \rightarrow M_{i}$ such that $F_{i}^{*} g_{i}$ converges to $g_{\infty}$ in the $C^{1, \alpha}$ and weak $L^{2, p}$ topologies on $K$. Thus, $g_{\infty}$ is locally in $C^{1, \alpha}$ and $L^{2, p}$.

It remains to prove that $\bar{G}$ is an orbifold, with orbifold singular points $\left\{q_{k}\right\}$, i.e. $\bar{G}=V$. This follows by an analysis of the tangent cone of the limit metric $g_{\infty}$ near each $q_{k}$, i.e. by a blow-up analysis. The curvature of $G$ is locally bounded in $L^{p}$, for any $p<\infty$. Further, by lower semicontinuity of the norm under weak convergence, the $L^{n / 2}$ norm of the curvature on $\left(G, g_{\infty}\right)$ is globally bounded:
$$\int_{G}|R|^{n / 2} d V \leq \Lambda .$$
In particular, for any $q=q_{k} \in \bar{G}$,
$$\int_{A_{q}\left(\frac{1}{2} r, 2 r\right)}|R|^{n / 2} d V \rightarrow 0, \quad \text { as } \quad r \rightarrow 0$$

This, together with the estimate (1.5) implies that on the limit $\left(G, g_{\infty}\right)$,
$$\left(\frac{1}{r^{n}} \int_{A_{q}\left(\frac{1}{2} r, 2 r\right)}|R|^{p} d V\right)^{1 / p} \ll r^{-2}$$
Observe that (2.10)-(2.12) are scale-invariant.
Let $s_{j}=2^{-j}$, for $j$ large, and rescale the metric $g_{\infty}$ on $G$ near $q$ by $s_{j}^{-2}$, i.e. consider the metrics $\bar{g}_{j}=s_{j}^{-2} \cdot g_{\infty}$. The volume bounds (1.4) and (2.1), together with the curvature bound (2.12) imply, via the local $C^{1, \alpha} \cap L^{2, p}$ Gromov compactness theorem, that a subsequence of $\left(G \backslash q, \bar{g}_{j}, q\right)$ converges, modulo diffeomorphisms, and in the $C^{1, \alpha}$ and weak $L^{2, p}$ topologies, to a flat limit $\left(T^{\infty}, \bar{g}^{\infty}\right)$. Using the diameter and volume bounds (2.6) and (2.1), it is straightforward to show that $T^{\infty}$ has a bounded number of components and the metric completion $\bar{T}^{\infty}$ of each component of $T^{\infty}$ has a single isolated singularity $\{0\}$. Thus, $\bar{T}^{\infty}$ is a finite collection of complete flat manifolds joined at a single isolated singularity $\{0\}$. From this, it follows also easily that $\bar{T}^{\infty}$ is isometric to a union of flat cones $C\left(S^{n-1} / \Gamma_{j}\right)$. By the smooth convergence, this (unique) structure on the limit is equivalent to the structure of $\left(G, g_{\infty}\right)$ on small scales near the singular point $q$, and shows that $q$ is an orbifold singularity; see [An1] for further details.

The remaining parts of Theorem 1.1 are now also easily established. Thus, the uniform bound on $Q_{i}^{r}$ in (2.5) gives a uniform bound on the number $Q$ of singular points in $\left(V, g_{\infty}\right)$. The lower bound (1.4) on the local volumes implies a lower bound on the local volumes of each spherical cone $C\left(S^{n-1} / \Gamma_{j}\right)$, which gives a uniform upper bound on the order of each local fundamental group $\Gamma_{j}$. The upper volume bound (2.1) then gives a uniform bound on the number of cones joined at any singular point $q \in V$.

As shown above, the limit metric $g_{\infty}$ is locally $C^{1, \alpha}$ and $L^{2, p}$ on $V_{0}=V \backslash\left\{q_{k}\right\}$. A punctured neighborhood of any $q=q_{k}$ has a finite cover diffeomorphic to a finite collection of punctured balls $B^{n} \backslash\{0\}$. The tangent cone analysis above shows that the metric becomes Euclidean to $0^{\text {th }}$ order at $\{0\}$, so that the metric $g_{\infty}$ has a $C^{0}$ extension over $\{0\}$ on each ball. (It is not to be expected in general that $g_{\infty}$ has a smooth extension across \{0\}).

This completes the proof of Theorem 1.1 in case (2.1) holds. \(\square\)

Remark 2.1. If one has a lower bound on the Ricci curvature of $\left(M_{i}, g_{i}\right)$, Ric $_{g_{i}} \geq \lambda g_{i}$, for some $\lambda>-\infty$, then the limit orbifold $\left(V, g_{\infty}\right)$ is irreducible, so that $V \backslash q_{k}$ is locally connected for all $k$. This is proved in [An1] by means of the Cheeger-Gromoll splitting theorem, [CGl]. Without such a lower bound on Ric, the number of cones may be greater than one, although it is necessarily finite.
(ii). If $x_{i} \in\left(M_{i}, g_{i}\right)$ is any (generic) sequence of points such that $x_{i} \rightarrow q$ in the Gromov-Hausdorff topology, then the curvature of $\left(M_{i}, g_{i}\right)$ blows up, i.e. diverges to infinity, as $i \rightarrow \infty$. If one rescales the metrics $g_{i}$ so that the curvature remains bounded near $x_{i}$, then a subsequence converges to a complete ALE space $\left(N, g^{\infty}\right)$, i.e. a complete manifold, or more generally, a complete orbifold, with a finite number of ends, each ALE. Blowing this limit $\left(N, g^{\infty}\right)$ down, i.e. rescaling $g^{\infty}$ by factors converging to 0 , gives a union of spherical cones joined at a single vertex $\{0\}$.

Now the curvature of $\left(M_{i}, g_{i}\right)$ may diverge to infinity at a number of different scales near any singular point $q$, giving rise to a collection of such ALE spaces associated with each scale. This gives rise to a so-called "bubble-tree" of ALE spaces and scales. The structure of the limit orbifold $\left(V, g_{\infty}\right)$ near any singular point $q$ is recaptured by the structure at infinity of the complete ALE orbifold corresponding to the smallest rate at which the curvature of $\left(M_{i}, g_{i}\right)$ diverges to infinity near $q$; this corresponds to the largest distance scale, since the curvature scale corresponds to the inverse square of the distance scale. For full details on the structure of such bubble trees and their relation with the orbifold limit, see [B] and [AC]; see also Remark 2.10 for further analysis.

Consider now the proof of Theorem 1.1 without the assumption (2.1). In this circumstance, there is no uniform bound $N(r / 2, r)$ on the number of $r / 2$ balls in an $r$-ball. However, one can define the sets $G_{i}^{r}$ and $B_{i}^{r}$ in (2.3)-(2.4) in exactly the same way, and again the cardinality of $\left\{B_{i}^{r}\right\}$ is uniformly bounded, i.e. (2.5) holds. Hence, as $r \rightarrow 0,\left\{B_{i}^{r}\right\}$ converges to finite number of points, (in a subsequence). On $G_{i}^{r}$, one has uniform curvature bounds (2.7), depending only on $r$. Standard comparison geometry then gives a uniform upper bound on the local volume ratios of geodesic balls contained in $G_{i}^{r}$. Hence, one can pass to a limit $G$, (in a subsequence), as in (2.8) just as before.

As in (2.9), let $\bar{G}$ be the metric closure of $G$. We note however that without the bound (2.1), it is apriori possible that $\bar{G}=G=\{\mathrm{pt}\}$; it could happen that all of the volume and curvature may concentrate in very small regions about a given point, see for example [Ak].

We will prove that the bound (2.1) does in fact hold on $\left(M_{i}, g_{i}\right)$ by using a blow-up rescaling argument, as discussed in Remark 2.1(ii) with regard to the structure of the singularities of $V$. To do this however requires the characterization of ALE spaces given by Theorem 1.2.
§2.2. This subsection is concerned with the proof of Theorem 1.2. Just as with Theorem 1.1, Theorem 1.2 is comparatively easy to prove if one assumes an upper bound on the volume growth as in (2.1), i.e.
$$\operatorname{vol} B_{x_{0}}(r) \leq \mathcal{V} r^{n},$$
for some fixed base point $x_{0}$ and $\mathcal{V}<\infty$, cf. [An1,Thm.3.5]. On the other hand, the proof to follow is essentially a generalization of the proof in case (2.13) holds.

We first prove the following special case of Theorem 1.2. This serves a basis for the more general result.

Theorem 2.2. Let ( $N, g$ ) be a complete, non-compact smooth Riemannian $n$-manifold, $n \geq 3$, satisfying
$$\operatorname{volB}_{x}(r) \geq \nu_{o} r^{n},$$
for some $\nu_{o}>0$ and all $x \in N$. Suppose in addition that there is a point $x_{0}$ and a non-increasing function $\varepsilon(r):[0, \infty) \rightarrow[0, \infty)$, with $\varepsilon(0)=1$ and $\lim _{r \rightarrow \infty} \varepsilon(r)=0$, such that
$$|R|(r) \leq \frac{\varepsilon(r)}{1+r^{2}},$$
where $|R|(r)=\sup _{x \in S_{x_{0}}(r)}|R|(x)$.
Then $(N, g)$ is ALE. Further, the number $\kappa$ of ends of $N$ and the maximal volume ratio $V_{0}=$ $\sup _{r} \frac{\operatorname{vol} B_{x}(r)}{r^{n}}$ are bounded by the function $\varepsilon(r)$. The asymptotic volume ratio is given by
$$\lim _{r \rightarrow \infty} \frac{\operatorname{volB}_{x}(r)}{r^{n}}=\sum_{k=1}^{\kappa} \frac{\omega_{n}}{\left|\Gamma_{k}\right|},$$
where $\omega_{n}$ is the volume of the unit ball in $\mathbb{R}^{n}$.
Remark 2.3. Theorem 2.2 does not hold in dimension 2. Consider for example the following warped product metric on $\mathbb{R}^{2}$ :
$$g=d r^{2}+f^{2}(r) d \theta^{2},$$
where, for large $r, f(r)=r \ln r$, (for example). A simple calculation shows that the curvature of $g$ satisfies (2.15), while the volume growth satisfies (2.14). However, this metric is not ALE. In terms of the proof to follow below, the tangent cone at infinity is of the form of the universal cover $\left(\widehat{\mathbb{R}^{2} \backslash 0}\right)$ of ( $\mathbb{R}^{2} \backslash 0$ ), which is not a cone on a spherical space-form; (it could be viewed as a cone with infinite cone angle). This situation is possible because $\left(\mathbb{R}^{2} \backslash\{0\}\right)$ is not simply connected. More importantly in the context of the proof below, the circle $S^{1}$ has no intrinsic curvature, whereas
spheres $S^{n-1}$ have non-trivial intrinsic curvature when $n \geq 3$. Note that in higher dimensions, one can form flat manifolds by taking products, $\left(\widetilde{\mathbb{R}^{2} \backslash 0}\right) \times \mathbb{R}^{n-2}$ for example.

Proof of Theorem 2.2: For clarity, we divide the proof into several steps.
Step 1. (Comparison Geometry Estimates).
We begin with some standard estimates from comparison geometry. Fix the base point $x_{0}$, and let $r(x)=\operatorname{dist}\left(x, x_{0}\right)$. Let $S(r)$ denote the geodesic sphere of radius $r$ about $x_{0}$. By using comparison with a rotationally symmetric metric whose curvature satisfies the bound (2.15), one has the following well-known Hessian and Laplacian comparison estimates for $r$ :
$$\begin{gathered}
D^{2} r \leq \frac{1+\mu(r)}{r} \hat{g}, \\
\Delta r \leq \frac{n-1+\mu(r)}{r},
\end{gathered}$$
where $\mu(r)$ depends only on $\varepsilon(r)$ and $\mu(r) \rightarrow 0$ as $r \rightarrow \infty$. Here $D^{2} r$ is the Hessian and $\Delta r=\operatorname{tr} D^{2} r$ is the Laplacian. The distance function $r$ is globally Lipschitz, with Lipschitz constant 1. However, it is not smooth on the cutlocus of $x_{0}$. Off the cutlocus (2.17)-(2.18) hold in the usual sense, since the metric $g$ and function $r$ are smooth there. At such smooth points, $D^{2} r$ is the $2^{\text {nd }}$ fundamental form $A$ of the geodesic sphere $S(r)$, while $\Delta r$ is the mean curvature $H$ of $S(r)$. However, the estimates (2.17)-(2.18) hold globally when $D^{2} r$ and $\Delta r$ are understood in a weak sense, either in the sense of support functions or as distributions; see for instance [Ka] for full details. Here $\hat{g}$ in (2.17) is given by $\hat{g}(X, X)=|X|^{2}-\left\langle X, \sigma^{\prime}\right\rangle^{2}$, where $\sigma$ is any geodesic from $x_{0}$ to $\sigma(r)$; see also [BL] for another definition of $D^{2} r$ on most of the cut locus. (The exact form of (2.17) on the cut locus will not be used however). Well-known analogues of (2.18) appear in the proof of the Cheeger-Gromoll splitting theorem [CGl] and Gromov's extension of the Bishop volume comparsion theorem past the cut locus, [G].

We also point out the obvious but important fact that the products $r D^{2} r$ and $r \Delta r$ are scaleinvariant.

For $r>0$, let $v(r)=\operatorname{vol} S(r)>0$, where vol denotes the $(n-1)$-dimensional Hausdorff measure $\mathcal{H}^{n-1}$ induced by the metric $g$.

Lemma 2.4. The function $v(r)$ is well-defined, for all $r>0$. If $r_{i}$ is an increasing sequence with $r_{i} \rightarrow r<\infty$, then
$$v(r) \leq \liminf _{i \rightarrow \infty} v\left(r_{i}\right) .$$
Moreover, let $\frac{d}{d r}{ }^{+} v(r)=\limsup _{\varepsilon>0, \varepsilon \rightarrow 0} \frac{v(r+\varepsilon)-v(r)}{\varepsilon}$. Then
$$\frac{d^{+}}{d r} v(r) \leq \frac{n-1+\mu(r)}{r} v(r) .$$

Proof: Let $\mathcal{C}$ denote the cutlocus of $x_{0}$ in ( $M, g$ ). By [BL], off a set $X$ with $\mathcal{H}^{n-1}(X)=0$, $\mathcal{C}$ is locally a smooth hypersurface, i.e. every point $x \in \mathcal{C} \backslash X$ has a neighborhood $N_{x}$ such that $N_{x} \cap \mathcal{C}=H_{x}$, where $H_{x}$ is a smooth hypersurface in $M$. Points $y \in H_{x}$ are characterized by the fact that there exist exactly two minimal geodesics from $x_{0}$ to $y$, neither of which has a conjugate point at $y$. Since $\mathcal{H}^{n-1}(X)=0, X$ will be ignored in the following. Let $H$ be the hypersurface given by the union of the local $(n-1)$-manifolds $H_{x}$ and let $S^{\text {reg }}(r)$ denote the regular set of $S(r)$, so that $S(r)=S^{\text {reg }}(r) \cup(H \cap S(r))$ up to a set of $\mathcal{H}^{n-1}$-measure 0. By [IT, Thm. B], $\mathcal{H}^{n-1}(\mathcal{C})$ is finite on compact subsets of $M$, and hence the same holds for the (relatively) open subset $H \subset \mathcal{C}$. Since $H \cap S(r)$ is a closed and bounded subset of $H, \mathcal{H}^{n-1}(H \cap S(r))$ is finite, for all $r$. Hence $v(r)$
is defined for all $r$. Moreover, for all $r$ except a closed set of Hausdorff dimension 0 in $\mathbb{R}, H \cap S(r)$ is of $\mathcal{H}^{n-1}$-measure 0; for such generic $r$,
$$v(r)=\operatorname{volS}^{\text {reg }}(r) .$$
An $r$ satisfying (2.21) will be called regular.
The property (2.19) corresponds to a well-known property of the cutlocus. Since any $x \in S(r)$ is the endpoint of a collection of minimal geodesics $\sigma_{x}$ from $x_{0}$, and since such geodesics are unique up to their endpoints at any distance $r-\varepsilon, \varepsilon>0$, it follows that $S(r)$ is the Hausdorff limit of $S^{\text {reg }}(r-\varepsilon)$ as $\varepsilon \rightarrow 0$. Any domain $U \subset S^{\text {reg }}(r)$ is the smooth limit of (essentially unique) domains $U_{\varepsilon} \subset S^{r e g}(r-\varepsilon)$, while for any given component $C$ of $H \cap S(r)$, there are exactly two disjoint domains $C^{ \pm}(r-\varepsilon) \subset S^{\text {reg }}(r-\varepsilon)$ converging smoothly to $C$ as $\varepsilon \rightarrow 0$. In other words, the limit $C$ is doubly covered. These properties imply (2.19).

To prove (2.20), suppose first that $r$ is non-regular, so that $H \cap S(r) \neq \emptyset$, and hence $v(r)>$ $v o l S^{\text {reg }}(r)$. Then $\mathcal{H}^{n-1}(H)<\infty$ implies that, for $\varepsilon$ sufficiently small, $v(r+\varepsilon)-v(r) \leq 0$. Thus, (2.20) holds in this case.

Assuming then that $r$ is regular, we first observe that
$$\int_{A(r, r+\varepsilon)} \Delta r \geq v(r+\varepsilon)-v(r) .$$
To see this, one applies the divergence theorem to a smooth domain $U_{\delta} \subset A(r, r+\varepsilon)$ approximating $A(r, r+\varepsilon)$ with $U_{\delta} \cap \mathcal{C}=\emptyset$. The boundary terms approximate integrals over the inner and outer boundaries $S(r+\varepsilon)$ and $S(r)$ of $A(r, r+\varepsilon)$ and the cut locus in the interior. The same argument as above establishing (2.19) shows that the outer boundary integral dominates $v(r+\varepsilon)$, (because of the double covering of $H \cap S(r)$ ), and that the boundary term in the interior approximating the cut locus is non-negative. (This argument is the same as that used in the proof of the splitting theorem for Ricci curvature, [CGl]). On the other hand, since $r$ is regular, (2.21) holds and the inner boundary integral converges to $v(r)$.

Using (2.22) together with (2.18) gives
$$\frac{n-1+\mu(r)}{r} \sup _{[r, r+\varepsilon]} v(s) \geq \frac{1}{\varepsilon}(v(r+\varepsilon)-v(r)) .$$
Letting $\varepsilon \rightarrow 0$ and using the fact that $r$ is regular again gives (2.20). \(\square\)

By integrating (2.20) w.r.t. $r$, one obtains
$$\frac{v(r)}{r^{n-1}} \leq C r^{\delta(r)}, \text { and } \frac{v(s)}{s^{n-1}} \leq 2^{\delta(r)} \frac{v(r)}{r^{n-1}}, s \in[r, 2 r],$$
where $\delta(r) \rightarrow 0$ as $r \rightarrow \infty$. In fact, rewriting (2.20) in the form $\frac{d^{+}}{d r}\left(v / r^{n-1}\right) \leq\left(v / r^{n-1}\right)(\varepsilon(r) / r)$, it then follows that
$$\limsup _{r \rightarrow \infty} \frac{d}{d r}^{+} \frac{v(r)}{r^{n-1}} \leq 0 .$$

These global statements on the volume growth are thus simple consequences of the infinitesimal estimate (2.18). We will also need corresponding local estimates on the volume growth. Thus, for any given $r_{0}>1$, let $D\left(r_{0}\right)$ be any domain in $S\left(r_{0}\right)$ and let $D(r) \subset S(r)$ be defined as
$$D(r)=\left\{x \in S(r): \operatorname{dist}(x, D(r)\} \leq r-r_{0}\right\},$$
for $r \geq r_{0}$. If $r \leq r_{0}, D(r)$ is defined in the same way, with $\left|r-r_{0}\right|$ in place of $r-r_{0}$. Then the same argument as above gives
$$\limsup _{r \rightarrow \infty} \frac{d}{d r}^{+} \frac{\operatorname{vol} D(r)}{r^{n-1}} \leq 0 .$$

The estimates (2.17)-(2.18) and hence (2.24)-(2.26) require only a lower bound on the curvature, i.e. follow from the bound
$$\left(K_{\min }\right)(r) \geq-\frac{\mu(r)}{r^{2}},$$
where $\left(K_{\text {min }}\right)(r)$ is the minimal value of the sectional curvatures of $(N, g)$ on $S(r)$. From the upper bound on the curvature, i.e. $\left(K_{\text {max }}\right)(r) \leq \frac{\mu(r)}{r^{2}}$, one obtains the following: suppose $x \in S(r)$ is not in the cutlocus of $x_{0}$, so that there is a unique geodesic $\sigma$ from $x_{0}$ to $x$. The geodesic $\sigma$ has length $r$. Suppose moreover that $\sigma(t) \in S(t)$ is not in the cutlocus of $x_{0}$ for any $t \leq 2 r$, (or $t \leq(1+\delta) r$, for some $\delta>0$ ). Then at such $x$,
$$\begin{gathered}
A=D^{2} r \geq \frac{1-\mu(r)}{r} \hat{g}, \\
H=\Delta r \geq \frac{n-1-\mu(r)}{r},
\end{gathered}$$
(where $\mu(r)$ also depends on $\delta$ ). These estimates will however not hold, in any generalized sense, at the cutlocus.

Remark 2.5. Suppose the manifold $(N, g)$ has a pole, i.e. a point, say $x_{0}$, at which the exponential map is a diffeomorphism. Then the geodesic spheres $S(r)$ are connected, smooth manifolds, for all $r$. Consider the rescaled Riemannian metrics $g_{r}=r^{-2} g_{S(r)}$ on $S(r)$. From (2.17), (2.27) and the Gauss equations for the hypersurface $S(r) \subset N$, one has
$$\left|K_{g_{r}}-1\right|=\mu(r) \rightarrow 0, \quad \text { as } \quad r \rightarrow \infty,$$
where $K_{g_{r}}$ is the intrinsic sectional curvature of $\left(S(r), g_{r}\right)$.
Thus, the geodesic spheres, when rescaled to unit radius, have curvature uniformly converging to 1. Hence, there is a uniform upper bound on their volume and diameter, by Myer's theorem. Translating this statement back to the unscaled metric g, it follows that $\limsup _{r \rightarrow \infty} \operatorname{vol} S(r) / r^{n-1} \leq$ $\sigma_{n-1}$, where $\sigma_{n-1}$ is the volume of the Euclidean ( $n-1$ )-sphere of radius 1. Integrating this inequality, it follows that (2.13) holds. In particular, it follows that $(N, g)$ is ALE, in fact $(N, g)$ is AE, (asymptotically Euclidean). Note that this proof requires $n \geq 3$; for $n=2$ the spheres are circles, and so have no intrinsic curvature, as in Remark 2.3. Note also this argument does not require a lower bound on the volume growth (2.14).

The proof of Theorem 2.2 is a generalization of this kind of argument to the situation where there are no poles.

This simple argument is due to Gromov, (unpublished), and gives rather simple proofs of results of Siu-Yau [SY] and Greene-Wu [GW] for instance.

\section*{Step 2. Tangent cones at infinity.}

Let $r_{k}$ be any sequence diverging to infinity, and consider the geodesic annuli $A_{k}=A_{k}(m)=$ $A_{k}\left(m^{-1} r_{k}, m r_{k}\right)$ about $x_{0}$, for some arbitrary but fixed $1<m<\infty$. We rescale the metric $g$ on $A_{k}$ by setting
$$g_{k}=r_{k}^{-2} \cdot g .$$
All distances of $g$ are contracted by the factor $r_{k}^{-1}$ w.r.t. $g_{k}$, so that $\left(A_{k}, g_{k}\right)$ is a geodesic annulus of width $\left(m^{-1}, m\right)$. The curvature bound (2.15) implies that, w.r.t. $g_{k}$,
$$\left|R_{g_{k}}\right|(x) \leq \varepsilon\left(r_{k}\right),$$
for all $x \in A_{k}$, with $\varepsilon\left(r_{k}\right) \rightarrow 0$ as $k \rightarrow \infty$. Further, the lower volume bound (2.14) implies that
$$\operatorname{vol} B_{x_{k}}(s) \geq \nu_{o} s^{n}$$
for all balls $B_{x_{k}}(s) \subset\left(A_{k}, g_{k}\right)$.

It follows from (the local $C^{1, \alpha} \cap L^{2, p}$ version of) the Gromov compactness theorem, cf. [An1], [An3], that a subsequence of the Riemannian manifolds $\left(A_{k}, g_{k}, x_{k}\right)$, at any base point sequence $x_{k}$ with $r\left(x_{k}\right)=r_{k}$, converges, (modulo diffeomorphisms), in the $C^{1, \alpha}$ and weak $L^{2, p}$ topologies, to a $C^{1, \alpha} \cap L^{2, p}$ limit Riemannian manifold ( $A_{\infty}, g_{\infty}, x_{\infty}$ ). By definition, $A_{\infty}$ is connected, containing the base point $x_{\infty}=\lim x_{k}$ and of course $A_{\infty}=A_{\infty}(m)$. On the limit $\left(A_{\infty}, g_{\infty}\right)$, the curvature is well-defined in $L^{p}$. Since the $L^{p}$ norm of the curvature is lower semi-continuous, (2.29) implies that the limit $\left(A_{\infty}, g_{\infty}\right)$ is flat. In particular, the limit is $C^{\infty}$ smooth.

Next, choose a sequence $m_{j} \rightarrow \infty$, and perform the analysis above for each $m_{j}$. It follows that a diagonal subsequence of the double sequence $\left(A_{k}\left(m_{j}\right), g_{k}, x_{k}\right)$ converges to a maximal connected limit $\left(T_{\infty}, g_{\infty}, x_{\infty}\right)$. Such limits $T_{\infty}$ are called tangent cones at infinity, (from terminology originating in the theory of minimal varieties), although apriori they need not be cones. The arguments above prove that all tangent cones at infinity of $(N, g)$ are flat.

Each tangent cone $T_{\infty}$ has a distinguished distance function $\rho=r_{\infty}$ given as follows. For $r(x)$ as above, let $r_{k}(x)=r_{k}^{-1} \cdot r(x)$. Then $r_{k}\left(x_{k}\right)=1$, and $r_{k}$ is a distance function on $A_{k}$. The functions $r_{k}$ are Lipschitz, with Lipschitz constant 1. In the subsequence above, the sequence $\left\{r_{k}\right\}$ converges, in the Lipschitz topology, to the limit distance function $r_{\infty}=\rho$ on $T_{\infty}$. By construction, $\rho$ takes on all values in $(0, \infty)$ on $T_{\infty}$.

The level sets $S(t)=\left\{x \in T_{\infty}: \rho(x)=t\right\}$ of $\rho$ are called the geodesic spheres of $T_{\infty}$. Thus, $S(t)$ is obtained by taking a limit of the rescaling of $S\left(t r_{k}\right)$ by $r_{k}^{-1}$. Observe that in general only part of $\left(S\left(t r_{k}\right), g_{k}\right)$ will limit on $S(t) \subset T_{\infty}$; other parts may be at infinite distance to $T_{\infty}$. Further, $S(t)$ is not necessarily connected, and the number of components may change with $t$. Observe also that the base point $x_{\infty}$ of $T_{\infty}$ lies in $S(1)$.

\section*{Step 3. Geometry of Tangent Cones.}

All tangent cones $T_{\infty}$ are flat manifolds, possibly with singularities at the metric boundary $\partial T_{\infty}$. Neighborhoods of the boundary $\partial T_{\infty}$ are given by the balls $B(\varepsilon)=\{x: \rho(x)<\varepsilon\}$. From standard scaling properties, the estimates (2.17)-(2.18) translate to
$$\begin{aligned}
D^{2} \rho & \leq \frac{1}{\rho} \hat{g}, \\
\Delta \rho & \leq \frac{n-1}{\rho},
\end{aligned}$$
where again (2.31)-(2.32) are understood to hold in the sense of support functions or distributions at cut points of $\rho$.

In particular, for any bounded domain $D \subset S(1) \subset T_{\infty}$ and associated $D(t) \subset S(t)$ as in (2.25), one has, as in (2.20),
$$\frac{d}{d t}^{+} \frac{\operatorname{vol} D(t)}{t^{n-1}} \leq 0$$
By Lemma 2.4, for a bounded domain $D, \operatorname{vol} D(t) \subset S(1)$ is finite.
Now return for the moment to the original manifold $(N, g)$. For any given $R$ large, decompose $S(R)$ into a collection of connected subdomains as follows. Let $C_{x}(s)=\{y \in S(R)$ : $\left.\operatorname{dist}_{A(R-\varepsilon, R+\varepsilon)}(y, x)<s\right\}$, where the distance is taken in the annulus $A(R-\varepsilon, R+\varepsilon)$ about $x_{0}$; here $\varepsilon=\varepsilon(R)<10^{-3}$ is taken sufficently small so that the number of components of $A(R-\varepsilon, R+\varepsilon)$ equals the number of components of $S(R)$. If $x$ and $x^{\prime}$ are in different components of $S(R)$, (and hence in different components of $A(R-\varepsilon, R+\varepsilon)$ ), define as usual $\operatorname{dist}_{A(R-\varepsilon, R+\varepsilon)}\left(x, x^{\prime}\right)=\infty$.

We may then cover $S(R)$ by a finite collection of connected closed sets $D_{i}$, with disjoint interiors, such that
$$C_{x_{i}}(2 \pi R) \subset D_{i} \subset C_{x_{i}}(4 \pi R) .$$
for some collection of points $x_{i} \in S(R)$. To be precise, choose a maximal collection of disjoint balls $C_{x_{i}}(2 \pi R)$ in $S(R)$ so that the balls $C_{x_{i}}(4 \pi R)$ cover $S(R)$. Then choose the sets $D_{i}$, so that $C_{x_{i}}(2 \pi R) \subset D_{i}$ with $\partial D_{i}$ contained in $C_{x_{i}}(4 \pi R) \backslash C_{x_{i}}(2 \pi R)$ and $\mathcal{H}^{n-1}\left(\partial D_{i}\right)=0$. Let $N(R)$ denote the cardinality of the collection $\left\{D_{i}\right\}$. Of course it is possible apriori that $N(R)$ diverges to infinity as $R \rightarrow \infty$.

By construction, we then have
$$\frac{v(R)}{R^{n-1}}=\sum_{i=1}^{N(R)} \frac{\operatorname{vol}\left(D_{i}\right)}{R^{n-1}} .$$
Again, for any fixed $R$ large and $D_{i}=D_{i}(R)$ as above, define the domains $D_{i}(r) \subset S(r)$, as in (2.25), for $\frac{3}{4} R \leq r \leq \frac{5}{4} R$. Then
$$S(r)=\cup_{i=1}^{N(R)} D_{i}(r),$$
and the structure of $S(r)$ discussed in the proof of Lemma 2.4 and the triangle inequality imply that the domains $D_{i}(r)$ satisfy $\mathcal{H}^{n-1}\left(D_{i}(r) \cap D_{j}(r)\right)=0$, for $i \neq j$. Observe that $D_{i}(r)$ may no longer be necessarily connected, for $r \neq R$, but this is of no importance. By construction, we then have
$$\frac{d}{d r}^{+}\left(\frac{v(r)}{r^{n-1}}\right)_{r=R}=\frac{d}{d r}\left(\sum_{i=1}^{N(R)} \frac{\operatorname{vol}\left(D_{i}(r)\right)}{r^{n-1}}\right)_{r=R}=\sum_{i=1}^{N(R)} \frac{d^{+}}{d r}\left(\frac{v_{i}(r)}{r^{n-1}}\right)_{r=R},$$
where $v_{i}(r)=\operatorname{vol} D_{i}(r)$.
Before proceeding further, we need a slight refinement of the considerations above. Let $S^{-}(R)$ be the union of the components of $S(R)$ which (partially) bound a domain in the annulus $A(R, 2 R)$ about $x_{0}$. Thus, a component $C(R) \subset S^{-}(R)$ if $C(R) \subset \partial K(R)$, where $K(R)$ is a domain in $A(R, 2 R)$ with $\partial K(R) \subset S(R)$. Let $S^{+}(R)=S(R) \backslash S^{-}(R)$, so that $S(R)=S^{+}(R) \cup S^{-}(R)$. Note that $S^{+}(R)$ is always non-empty; it contains components which are the boundaries of ends of $N$ outside $S(R)$, while $S^{-}(R)$ may or may not be empty. Let $v^{+}(R)=v o l S^{+}(R), v^{-}(R)=v o l S^{-}(R)$, so that $v(R)=v^{+}(R)+v^{-}(R)$, for all $R$. Observe that (2.35)-(2.36) hold with $v^{+}(r)$ or $v^{-}(r)$ in place of $v(r)$.

Let $D^{-}(R) \subset A(R, 2 R)$ be the compact domain with $\partial D(R)=S^{-}(R)$. Then (2.23) gives
$$\frac{\operatorname{vol}\left(S(s) \cap D^{-}(R)\right)}{s^{n-1}} \leq(1+\delta) \frac{\operatorname{volS}^{-}(R)}{R^{n-1}},$$
where $\delta \rightarrow 0$ as $R \rightarrow \infty$. Thus, the main issue is to control the volume growth of $S^{+}(R)$ as $R \rightarrow \infty$.
Now suppose
$$\frac{d^{+}}{d r} \frac{v^{+}(r)}{r^{n-1}} \leq 0,$$
for all $r \geq R_{0}$, for some $R_{0}<\infty$. Then (2.37) and (2.38) clearly imply $v(r) \leq K r^{n-1}$, for some $K<\infty$ and so
$$\operatorname{vol} B_{x_{0}}(r) \leq K r^{n} .$$
Hence, as noted prior to its statement, Theorem 2.2 follows in this case from [An1], (see also Step IV below for details on the proof). Thus, we may suppose that there exists some sequence $r_{k} \rightarrow \infty$ such that
$$\left.\frac{d^{+}}{d r} \frac{v^{+}(r)}{r^{n-1}}\right|_{r=r_{k}}>0 .$$

It follows from (2.36) and (2.40) that there exist $i=i\left(r_{k}\right)$ and domains $D_{i} \subset S^{+}\left(r_{k}\right)$, as in (2.34) such that for all $k$,
$$\left.\frac{d}{d r}{\frac{v}{r^{n-1}}}^{v_{i}(r)}\right|_{r=r_{k}}>0 .$$
Let $x_{i} \in S^{+}\left(r_{k}\right), i=i(k)$, be the base points of $D_{i}$. By passing to a subsequence based at $\left\{x_{i}\right\}$ if necessary, one obtains convergence to a tangent cone ( $T_{\infty}, g_{\infty}, x_{\infty}$ ) with associated distance function $\rho$ and level sets $S(t)$, and with $x_{\infty}=\lim x_{i} \in S(1)$. The convergence is in the $C^{1, \alpha}$ topology (on compact subsets), while the convergence of the distance functions is at least Lipschitz. Let $D_{\infty} \subset S(1)$ be the limit of the domains $D_{i}$. Then, by construction, $D_{\infty}$ is not the (partial) boundary of a domain in $A(1,2) \subset T_{\infty}$, so that $\rho$ assumes all values in $\left(\frac{1}{2}, \frac{3}{2}\right)$ near $D_{\infty}$. In particular, $D_{\infty}$ locally disconnects $T_{\infty}$ and hence $\operatorname{vol} D_{\infty}=\mathcal{H}^{n-1}\left(D_{\infty}\right)>0$.

Note that (2.41) implies that the domain $D_{i} \subset S\left(r_{k}\right)$ is regular, cf. (2.21). By taking a small perturbation of $\left\{r_{k}\right\}$ if necessary, (relative to its own size), we may assume that $D_{\infty} \subset S(1) \subset T_{\infty}$ is also regular and (2.41) still holds. For if this were not the case, then the upper bound (2.20), cf. also (2.23), would imply again that (2.39) holds. Let $D_{\infty}(t) \subset S(t)$ be defined as in (2.25), so that $D_{\infty}(t)$ is the limit of the the corresponding domains in $\left(S(t), g_{k}\right)$. Also, let $v_{\infty}(t)=v o l D_{\infty}(t)=$ $\mathcal{H}^{n-1}\left(D_{\infty}(t)\right)$. The regularity of these domains and the $C^{1, \alpha}$ convergence to the tangent cone $T_{\infty}$ implies that, for $t$ close to 1 ,
$$\frac{v o l_{g}\left(D_{i}\left(t r_{k}\right)\right)}{\left(t r_{k}\right)^{n-1}}=\frac{v o l_{g_{k}} D_{i}(t)}{t^{n-1}} \rightarrow \frac{v o l D_{\infty}(t)}{t^{n-1}},$$
and
$$\left.r_{k} \frac{d}{d r}^{+} \frac{\operatorname{vol}_{g}\left(D_{i}(r)\right)}{r^{n-1}}\right|_{r=r_{k}}=\left.\left.\frac{d}{d t}^{+} \frac{\operatorname{vol}_{g_{k}}\left(D_{i}(t)\right)}{t^{n-1}}\right|_{t=1} \rightarrow \frac{d}{d t}^{+} \frac{v_{\infty}(t)}{t^{n-1}}\right|_{t=1} .$$
Hence, from (2.41) one has
$$\left.\frac{d}{d t}{\frac{v}{t^{n-1}}(t)}_{t^{n-1}}\right|_{t=1} \geq 0$$

On the other hand, from (2.33) one has
$$\left.\frac{d}{d t}{\frac{v}{t^{n-1}}(t)}_{t^{n-1}}\right|_{t=1} \leq 0$$
so that
$$\left.\frac{d}{d t}{\frac{v}{t^{n-1}}(t)}_{t^{n-1}}\right|_{t=1}=0$$
The pointwise estimate (2.32), (in the sense of support functions), together with (2.44) implies that $\Delta \rho \equiv(n-1)$ on $D_{\infty}$. Moveover, since $D^{2} \rho \leq \hat{g}$, and $\Delta \rho=\operatorname{tr} D^{2} \rho$, it also follows that $D^{2} \rho=\hat{g}$ on $D_{\infty}$. This implies first that the domain $D_{\infty} \subset S(1)$ is in fact smooth. As in Remark 2.5, the Gauss equations imply that $D_{\infty}$ has constant curvature 1, and hence is a domain in a spherical space form $S^{n-1} / \Gamma$, (since $n \geq 3$ ). Moreover, by the construction in (2.34), $D_{\infty}$ contains an intrinsic geodesic ball of radius at least $2 \pi$, and so it follows that
$$D_{\infty}=S^{n-1} / \Gamma .$$
Since $\rho$ is also a distance function from $D_{\infty}$, it follows that for $t \leq 1, D_{\infty}(t)$ is the spherical spaceform of radius $t$, and curvature $t^{-2}$. Thus, the domain $B_{\infty}=\cup_{t \leq 1} D_{\infty}(t) \subset T_{\infty}$ is a ball of radius 1 in the standard cone $C\left(S^{n-1} / \Gamma\right)$, with vertex $\{0\} \subset\{t=0\}$.

At this stage, it is possible that $S(1) \subset T_{\infty}$ has other components besides $D_{\infty}$; of course each component satisfying (2.43) is the unit ball about the vertex in a standard cone $C\left(S^{n-1} / \Gamma\right)$.

Summarizing, the argument above proves that on any sequence of base points $x_{k}$, with $r_{k}=$ $r\left(x_{k}\right) \rightarrow \infty$, for which
$$\left.\liminf _{r \rightarrow \infty} \frac{d}{d r}^{+} \frac{\operatorname{vol}\left(D_{k}\right)}{r^{n-1}}\right|_{r=r_{k}} \geq 0,$$
any limit $D_{\infty}$ is of the form (2.45). Moreover, the domain $D_{k}$ is a full component of $S\left(r_{k}\right)$ for $k$ sufficiently large.

\section*{Step 4. Completion of Proof.}

The statement (2.46) implies the following: there is an $R<\infty$, sufficiently large, and $\delta>0$ sufficiently small, both depending on $(N, g)$, such that for any $r \geq R$, and any domain $D_{k} \subset S^{+}(r)$ as in (2.34), either
$$\frac{d}{d r} \frac{{ }^{+}}{v o l\left(D_{k}\right)}<-\delta,$$
or,
$$\frac{\operatorname{vol}\left(D_{k}\right)}{r^{n-1}} \leq(1+\delta) \frac{\sigma_{n-1}}{\left|\Gamma_{k}\right|} .$$
Thus, the volume ratio of the domain $D_{k}(r)$ is either strictly decreasing with increasing $r$, or the volume ratio is close to that of the corresponding spherical space-form. In the latter case, the geometry of $\left(D_{k}, g_{k}\right)$ is $\delta$-close to that of a spherical space-form $S^{n-1} / \Gamma_{k}$.

These facts imply that $\operatorname{vol} S(r) / r^{n-1}$ is uniformly bounded. In fact, for all $r \geq R$,
$$\frac{\operatorname{vol}(S(r))}{r^{n-1}} \leq 2 \frac{\operatorname{vol}(S(R))}{R^{n-1}},$$
and hence one has
$$\operatorname{vol} B(r) \leq V_{0} r^{n},$$
for some $V_{0}$ depending on $(N, g)$. This shows that (2.13) holds, and hence from the methods of [An1], it follows that $(N, g)$ has a finite number of ends, each ALE.

For completeness, we give the proof of this. The bounds (2.14) and (2.49) imply that the geodesic sphere $S(1)$ in any tangent cone at infinity $T_{\infty}$ of $(N, g)$ has uniformly bounded volume, diameter and a uniformly bounded number of components. The proof of this is the same as that given in §2.1, since one has a uniform upper bound on the number of disjoint balls of radius $\frac{1}{2}$ in any 1 -ball ( $B(1), g_{r}$ ) about $x_{0}$, for $g_{r}$ as in (2.28). Given a tangent cone ( $T_{\infty}, g_{\infty}$ ) obtained as a limit of rescalings by factors $r_{k}^{-2}$ as in (2.28), observe that the geodesic sphere $S(t) \subset T_{\infty}$ is just the unit geodesic sphere $S(1)$ in the tangent cone $\left(T_{\infty}(t), g_{\infty}(t)\right)$ obtained by rescaling by the factors $\left(t r_{k}\right)^{-2}$.

It follows that in any tangent cone $T_{\infty}$, and for any $t>0$, one has the uniform bound
$$\operatorname{diam} S(t) \leq D \cdot t,$$
for some fixed $D$, compare with (2.6). Here diam is the intrinsic diameter of each component of $S(t)$. For the same reasons, there is a uniform upper bound on the number of components of $S(t)$. As discussed near the end of §2.1, these estimates imply that the metric completion $\bar{T}_{\infty}$ of any $T_{\infty}$ is given by adding a bounded number of points $\left\{z_{j}\right\}$ to $T_{\infty}$, one for each component of $S(t)$, for $t$ small. Hence $\bar{T}_{\infty}$ is a complete flat manifold with a finite collection of isolated singularities.

By an analysis of the developing map for flat structures, one sees that $T_{\infty}$ is a standard flat cone $C\left(S^{n-1} / \Gamma\right)$ with a finite number of points removed, (including the vertex). Thus, only one point, the vertex say $\{0\}=\left\{z_{0}\right\}$, among the collection $\left\{z_{j}\right\}$ may be a singular point; all others have neighborhoods which are balls, and so are locally removable singularities. This result is proved in [An4,Thm.3.2], cf. also [AC], the idea being that isolated singularities of flat manifolds are
necessarily orbifold singularities, and all flat orbifolds are good orbifolds in the sense of Thurston, i.e. are quotients of $\mathbb{R}^{n}$ by a group of isometries.

Thus all tangent cones $T_{\infty}$ of $(N, g)$ are standard cones on spherical space-forms, possibly with a finite number of points removed. Moreover, we now claim that the collection of removable singularities $\left\{z_{j}\right\}, j \geq 1$, is empty, so that all geodesic spheres $S(1)$ are standard spherical spaceforms $S^{n-1} / \Gamma$. Namely, since the convergence of the rescalings $r^{-2} \cdot g$ to $g_{\infty}$ is smooth, (i.e. $C^{1, \alpha}$ ), it follows that for any $r$ sufficiently large, and any base point $x \in S(r)$, the component $\left(A\left(\frac{1}{2}, 1\right), g_{r}, x\right)$ of $\left(A\left(\frac{1}{2}, 1\right), g_{r}\right)$ containing $x$ is close, in $C^{1, \alpha}$, to the standard flat metric on a standard annulus $A\left(\frac{1}{2}, 1\right)$ in $C\left(S^{n-1} / \Gamma\right)$. Npw recall again that if $\left(S(1), g_{r}\right)$, (the rescaling of $(S(r), g)$ by $r^{-2}$ ), is close to $S(1) \subset T_{\infty}$ then for any given $\lambda$ large, $\left(S(\lambda), g_{r}\right)$ is close to $S(\lambda) \subset T_{\infty}$, but is also close to $S(1) \subset T_{\infty}^{\lambda}$, where $T_{\infty}^{\lambda}$ is $T_{\infty}$ scaled down by the factor $\lambda^{-2}$. It follows that for all $r$ sufficiently large, $r \geq R_{0}$, each component of $A\left(\frac{1}{2} r, r\right) \subset(N, g)$ stabilizes, i.e. is independent of $r$; no bifurcations or changes in the topology are possible, since the geometry of each annular region remains very close to that of a standard spherical cone. In particular, for $r$ sufficiently large, the components of $S(r)$ can not bifurcate or merge and hence each geodesic sphere $S(1)$ in any tangent cone at infinity $T_{\infty}$ is connected.

Exactly the same reasoning implies that $(N, g)$ has only a finite number of ends, and each end is asymptotic to a standard cone $C\left(S^{n-1} / \Gamma\right)$. Scaling properties and the $C^{1, \alpha}$ convergence to the tangent cone at infinity imply the decay estimates (1.7). The formula (2.16) follows then immediately.

Finally, we claim that the number $\kappa$ of ends of $(N, g)$, and the volume constant $V_{0}$ depend only on the function $\varepsilon(r)$. Since $\varepsilon(r)$ is fixed, for $r$ sufficiently large, $\varepsilon(r)$ is sufficiently small. Hence, for a given $\mu$ small, the rescaled curvature $r^{2}|R|(r)$ satisfies $r^{2}|R|(r) \leq \mu$, for all $r \geq R_{0}=R_{0}(\mu)$. As above, this implies that the topology of $A\left(R_{0}, \infty\right)$ is that of a finite collection of truncated cones on $S^{n-1} / \Gamma$. On the other hand, for $r \leq R_{0}$, the curvature $R$ of $(N, g)$ is uniformly bounded, by (2.15), and hence $B_{x_{0}}\left(R_{0}\right)$ has bounded volume and bounded topology; in particular, there is a fixed bound on the number of components of $S_{x_{0}}\left(R_{0}\right)$, depending only on $R_{0}$. This proves that the number of ends is bounded by the function $\varepsilon(r)$. The same reasoning gives an estimate on $V_{0}$ in terms of $\varepsilon(r)$.

This completes the proof of Theorem 2.2. \(\square\)

Remark 2.6. As a simple illustration of Theorem 2.2, let $p_{i}, i=1, \ldots \kappa$, be a finite collection of points in a closed Riemannian manifold $(M, g)$. Let $r_{i}(x)=\operatorname{dist}\left(x, p_{i}\right)$ and consider the manifold $N=M \backslash \cup p_{i}$ with the conformally equivalent metric
$$\widetilde{g}=\left(\sum_{i=1}^{\kappa} \frac{1}{\widehat{r}_{i}^{4}}\right) g,$$
where $\widetilde{r}_{i}$ is a smoothing of $r_{i}$ away from $p_{i}$. Then $\widetilde{g}$ is complete and ALE, in fact AE, with $\kappa$ ends. The norm of the curvature depends on $\kappa$. In particular, the $L^{n / 2}$ and $L^{\infty}$ norms of the curvature are unbounded as $\kappa$ increases to infinity. This shows that number of ends, as well as the volume ratio $V_{0}$, in Theorem 2.2 depend on $\varepsilon(r)$.

Similarly, it is easy to construct manifolds satisfying (2.14) and (2.15) with $\varepsilon(r) \equiv 1$ which have infinitely many ends.

Remark 2.7. It is clear that Theorem 2.2 also holds if $(N, g)$ is an orbifold with a bounded number of cones at each singular point, instead of a smooth manifold. By definition, the singular points of orbifolds form a discrete set. Hence the cross sections $S^{n-1} / \Gamma$ of the tangent cones at infinity cannot themselves be orbifolds, for otherwise $N$ would have at least non-trivial curves of
singularities. Hence, the number of orbifold singular points is finite, and again bounded by the function $\varepsilon(r)$.
(ii). In a certain sense, Theorem 2.2 is more general than Theorem 1.2, in that the global bound (1.9) on the $L^{n / 2}$ norm of the curvature is not required in Theorem 2.2. However, for the application to the proof of Theorem 1.1, it is important to know that the number $\kappa$ of ends, and the maximal volume ratio $V_{0}$ depend only on $\Lambda$, and not on the manifold $(N, g)$ or the function $\varepsilon(r)$. Of course a bound on $\Lambda$ does not give apriori control on $\varepsilon(r)$.

Using Theorem 2.2 as a base, we are now in position to prove Theorem 1.2.
Proof of Theorem 1.2.
We recall the hypotheses: ( $N, g$ ) is a complete non-compact Riemannian manifold, satisfying
$$\operatorname{vol} B_{x}(r) \geq \nu_{0} r^{n}, \int_{N}|R|^{n / 2} \leq \Lambda$$
together with the small curvature estimate (1.5), with fixed $\nu_{0}, \Lambda, \delta_{0}$ and $C_{0}$. Let
$$\mathcal{V}_{0}=\sup _{x, r} \frac{\operatorname{vol} B_{x}(r)}{r^{n}} .$$
Then $\mathcal{V}_{0}$ and $\kappa$, the number of ends of $(N, g)$ are finite, and we need to prove there is a bound on $\mathcal{V}_{0}$ and $\kappa$, depending only on $\nu_{0}, \Lambda, \delta_{0}$ and $C_{0}$. Note that all the quantities in (2.51), (2.52) and (1.5) are scale-invariant.

The proof is somewhat simpler if one adds the hypothesis
$$|R|(r) \leq \frac{C}{1+r^{2}},$$
where $r(x)=\operatorname{dist}_{g}\left(x, x_{0}\right)$, for some base point $x_{0} \in N$ and some arbitrary constant $C<\infty$, with $\kappa$ and $\mathcal{V}_{0}$ depending also on $C$. Thus, we first prove the result in this situation, and then show how the proof can be generalized to give the result in full.

Suppose the statement is false; then there exists a sequence of manifolds $\left(N_{i}, g_{i}\right)$ satisfying (2.51)-(2.53), w.r.t base points $x_{i}$, such that either $\kappa_{i} \rightarrow \infty$ or $\mathcal{V}_{i}=\mathcal{V}_{i}\left(g_{i}\right) \rightarrow \infty$, (or both). By the smooth (i.e. $C^{1, \alpha} \cap L^{2, p}$ ) Gromov compactness theorem, there exist radii $R_{i}^{1} \rightarrow \infty$ such that a subsequence of $\left(B\left(R_{i}^{1}\right), g_{i}, x_{i}\right)$ converges uniformly in the $C^{1, \alpha}$ and weak $L^{2, p}$ topologies to a complete limit $\left(N_{0}, g_{0}, x_{0}\right)$. Here $B\left(R_{i}^{1}\right)$ is the ball centered at $x_{i}$; in the following, we assume the subsequence of $\left\{\left(N_{i}, g_{i}\right)\right\}$ has been chosen, so that one has convergence to the limit. The limit metric $g_{0}$ has curvature locally in $L^{p}$, for any $p<\infty$, and has $L^{n / 2}$ norm of curvature satisfying (2.51) on $N_{0}$.

We observe that $R_{i}^{1}$ may be chosen so that
$$\int_{B\left(R_{i}^{1}\right)}|R|^{n / 2} \geq \delta_{0} .$$
For if $\int_{B\left(R_{i}^{1}\right)}|R|^{n / 2}<\delta_{0}$, we may rescale the metrics $g_{i}$ by $\left(R_{i}^{1}\right)^{-2}$ taking $B\left(R_{i}^{1}\right)$ to a ball of radius 1. The small curvature estimate (1.5) implies that the curvature is uniformly bounded in $B(1)$, while (2.53) remains valid outside $B(1)$; (the estimate (2.53) is essentially scale invariant for large $r$ ). Hence, all the arguments above may be applied to this renormalization of the original sequence $\left(N_{i}, g_{i}\right)$.

We may thus apply Theorem 2.2 to conclude that $N_{0}$ has a finite number $\kappa^{0}$ of ends, and a maximal volume ratio $\mathcal{V}^{0}$. Returning to the geometry of the original subsequence ( $N_{i}, g_{i}$ ), it follows that a neighborhood $A\left(\frac{1}{2} R_{i}^{1}, R_{i}^{1}\right)$ of the boundary of $B\left(R_{i}^{1}\right)$ has $\kappa^{0}$ components, and the maximal volume ratio $\mathcal{V}$ in $B\left(R_{i}^{1}\right)$ satisfies $\mathcal{V} \leq 2 \mathcal{V}^{0}$. The curvature of $g_{i}$ on the region $A\left(\frac{1}{2} R_{i}^{1}, R_{i}^{1}\right)$, or the larger region $A\left(m R_{i}^{1}, m^{-1} R_{i}^{1}\right)$, for any fixed $m$, is on the order of $\mu_{i} \cdot\left(R_{i}^{1}\right)^{-2}$, where $\mu_{i} \rightarrow 0$ as
$i \rightarrow \infty$; after rescaling by $\left(R_{i}^{1}\right)^{-2}$, the geometry here is close to that of a collection of truncated spherical cones.

Now rescale the original metrics ( $N_{i}, g_{i}$ ) in the subsequence to make the radius $R_{i}^{1}$ small. Thus, set $g_{i}^{1}=r_{i}^{2}\left(R_{i}^{1}\right)^{-2} g_{i}$, where $r_{i} \rightarrow 0$ slowly, as $i \rightarrow \infty$. The curvature of $g_{i}^{1}$ in the $g_{i}^{1}$-annulus $A\left(m r_{i}, m^{-1} r_{i}\right)$ about $x_{i}$ is on the order of $\mu_{i}^{\prime} \rightarrow 0$ as $i \rightarrow \infty$, since $r_{i}$ is chosen to go to 0 sufficiently slowly. Outside $B\left(r_{i}\right)$, the curvature bound (2.53) still holds w.r.t. $g_{i}^{1}$, and $r_{i}$ may be chosen so that the curvature is uniformly bounded in $\left(A\left(r_{i}, 1\right), g_{i}^{1}\right)$. Thus, via Gromov compactness again, by passing to a further subsequence of the original sequence, we can again pass to a complete rescaled limit $\left(V^{1}, g^{1}, x^{1}\right)$ with a single orbifold singular point $x^{1}=\{0\}$, having a bounded number $\kappa^{0}$ of cones. Now apply Theorem 2.2, (or Remark 2.7), to this configuration; $V^{1}$ has a bounded number $\kappa^{1}$ of ends, and again maximal volume ratio $\mathcal{V}^{1}\left(\geq \mathcal{V}^{0}\right)$. Hence, there is a sequence $R_{i}^{2} \rightarrow \infty$ (slowly) such that the balls $B\left(R_{i}^{2}\right) \subset\left(N_{i}, g_{i}^{1}\right)$ converge uniformly to $\left(V^{1}, g^{1}\right)$; the convergence is $C^{1, \alpha}$ and weak $L^{2, p}$ away from the singular point $\{0\}$. For the same reasons as above justifying (2.54), we may assume that, in the $g_{i}^{1}$ metric,
$$\int_{A\left(1, R_{i}^{2}\right)}|R|^{n / 2} \geq \delta_{0} .$$
Returning then again to the original unscaled subsequence $\left(N_{i}, g_{i}\right)$, it follows that the number of components of $A\left(\frac{1}{2} R_{i}^{1} R_{i}^{2}, R_{i}^{1} R_{i}^{2}\right)$ is $\kappa^{1}$ and the maximal volume ratio $\mathcal{V}$ in the ball $B\left(R_{i}^{1} R_{i}^{2}\right)$ satisfies $\mathcal{V} \leq \mathcal{V}^{1}$.

This process can clearly be repeated any finite number of times, passing to a subsequence of the original sequence ( $N_{i}, g_{i}$ ) if necessary. Each iteration adds $\delta_{0}$ to the total $L^{n / 2}$ norm of curvature. Hence, after $d=d\left(\Lambda, \delta_{0}\right)$ iterations, one has a radius $S_{i}^{d}=\prod_{1}^{d} R_{i}^{k}$ such that
$$\int_{N_{i} \backslash B\left(S_{i}^{d}\right)}|R|^{n / 2} \leq \delta_{0}$$
for which the maximal volume ratio $\mathcal{V}$ in $B\left(S_{i}^{d}\right) \subset\left(N_{i}, g_{i}\right)$ satisfies $\mathcal{V} \leq \mathcal{V}^{d}<\infty$ and the number of components of $A\left(\frac{1}{2} S_{i}^{d}, S_{i}^{d}\right) \subset\left(N_{i}, g_{i}\right)$ is bounded by $\kappa^{d}<\infty$, for $i$ large. The curvature of the annulus $A\left(\frac{1}{2}, 2\right)$ in the rescaling $g_{i}^{d}=\left(S_{i}^{d}\right)^{-2}$ is arbitrarily small when $i$ is large. In the scale $g_{i}^{d}$, the estimate (2.55) is now global, and implies the curvature decays faster than quadratically outside $B(1)$. Theorem 2.2 then gives a uniform bound on the number of ends of $N_{i}$ and a uniform upper bound $\mathcal{V}$ on the maximal volume ratio. This contradicts the assumption that $\mathcal{V}_{i}$ or $\kappa_{i}$ becomes arbitrarily large as $i \rightarrow \infty$, and proves Theorem 1.2 in case (2.53) holds.

Next we turn to the situation where (2.53) is not assumed. The proof in this case has the same overall structure as before; the only difference is that new orbifold singular points, not only \{0\}, may be introduced in the limits. However, these are treated in essentially the same way.