---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Convergence for Yamabe metrics of positive scalar curvature with integral bounds on curvature]

---
source_file: Convergence_for_Yamabe_metrics_of_positive_scalar_curvature_with_integral_bounds_7637361d60e6.pdf
converter: mathpix
format: mmd
---

\title{
CONVERGENCE FOR YAMABE METRICS OF POSITIVE SCALAR CURVATURE WITH INTEGRAL BOUNDS ON CURVATURE
}

\author{
Kazuo Akutagawa
}

\title{
CONVERGENCE FOR YAMABE METRICS OF POSITIVE SCALAR CURVATURE WITH INTEGRAL BOUNDS ON CURVATURE
}

\author{
Kazuo Akutagawa
}

\begin{abstract}
Let $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ be the class of compact connected smooth $n$ manifolds $M(n \geq 3)$ with Yamabe metrics $g$ of unit volume which satisfy
$$\mu(M,[g]) \geq \mu_{0}>0,$$
where $[g]$ and $\mu(M,[g])$ denote the conformal class of $g$ and the Yamabe invariant of $(M,[g])$, respectively. The purpose of this paper is to prove several convergence theorems for compact Riemannian manifolds in $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ with integral bounds on curvature. In particular, we present a pinching theorem for flat conformal structures of positive Yamabe invariant on compact 3-manifolds.
\end{abstract}

\section*{1. Introduction.}

Let $M$ be a compact connected smooth manifold of dimension $n \geq 3$. The Yamabe functional $I$ on a conformal class $C$ of $M$ is defined by
$$I(g)=\frac{\int_{M} S_{g} d v_{g}}{V_{g}^{(n-2) / n}} \quad \text { for } \quad g \in C$$
where $S_{g}, d v_{g}$ and $V_{g}$ denote the scalar curvature, the volume element and the volume $\operatorname{vol}(M, g)$ of $(M, g)$, respectively. The infimum of this functional is denoted by $\mu(M, C)$, i.e.,
$$\mu(M, C)=\inf _{g \in C} I(g)$$
and called the Yamabe invariant of ( $M, C$ ). The following so-called Yamabe problem was solved affirmatively by the work of Yamabe [Ym], Trudinger [T], Aubin [Au1] and Schoen [S1, SY2]:

Given a conformal class $C$ on a compact manifold $M$ of dimension $n \geq 3$, find a metric $g$ which minimizes the Yamabe functional $I$ on the conformal class $C$.

We call a metric, which is a solution of the Yamabe problem, simply a Yamabe metric. It is well-known that the scalar curvature of every Yamabe metric is constant. Moreover, a Yamabe metric of positive scalar curvature stisfies a volume estimate of geogesic balls from below (see §2). In [K1, K2] and [S3], a differential-topological invariant $\mu(M)$ of $M$ was independently introduced by Kobayashi and Schoen , which is defined as the supremum of $\mu(M, C)$ of all conformal structures $C$ on $M$, i.e.,
$$\mu(M)=\sup \{\mu(M, C) ; C \text { is a conformal structure on } M\} .$$

They also studied properties of $\mu(M)$ and proposed some problems (for recent remarkable developments see [L1, L2]). In particular, Schoen conjectured affirmatively the following problem. That is whether the positive constant curvature metrics $h$ on non-simply connected quotient spaces $S^{n} / \Gamma$ of the standard $n$-sphere $S^{n}$ acheive the supremum of $\mu\left(S^{n} / \Gamma, C\right)$, i.e., $\mu\left(S^{n} / \Gamma,[h]\right)=\mu\left(S^{n} / \Gamma\right)$, where $[h]$ denotes the conformal class of $h$.

On the other hand, Gromov and Lawson [GL] (cf. [SY1]) proved that a irreducible oriented compact 3-manifold $M^{3}$ admitting a metric of positive scalar curvature is diffeomorphic to a quotient space of a homotopy 3 -sphere. Moreover, if $M^{3}$ admits a conformally flat metric, then $M^{3}$ is diffeomorphic to a quoitent space of $S^{3}$ (cf. [Ku]). Under these situation, the following naive problem arises naturally; for a quotient manifold $X^{3}$ of a homotopy 3-sphere which admits a metric of positive scalar curvature, is there a positive constant curvature metric $h$ such that $\mu\left(X^{3},[h]\right)=\mu\left(X^{3}\right)$ ? It also should be pointed out that, which was proved by Izeki [I], if a compact 3-manifold $N^{3}$ admits a conformally flat metric of positive scalar curvature, then a finite cover of $N^{3}$ is diffeomorphic to $S^{3}$ or a connected sum $k\left(S^{1} \times S^{2}\right)$ of $k$-copies of $S^{1} \times S^{2}$.

Let $A_{g}$ denote the tensor field $\left(A_{i j k}\right)=\left(\nabla_{k} R_{i j}-\nabla_{j} R_{i k}\right)$ of type ( 0,3 ), where $\left(R_{i j}\right)$ stands for the Ricci curvature $\operatorname{Ric}_{g}$ of a metric $g$ and ∇ the Levi-Civita connection of $g$. We note that if $(M, g)$ is a conformally flat manifold of constant scalar curvature, then $A_{g}$ vanishes identically (i.e., $h$ is of harmonic curvature). Conversely, under the condition $\operatorname{dim} M=3$, $A_{g} \equiv 0$ implies that $(M, g)$ is a conformally flat manifold of constant scalar curvature. Throughout this paper, we always assume that $p, q$ and $\mu_{0}$ are positive constants satisfying $p>\frac{n}{2}, \max \left\{1, \frac{n}{4}\right\}<q<\frac{n}{2}$ and $\mu_{0}<n(n-$ 1) $\operatorname{vol}\left(S^{n}(1)\right)^{2 / n}$, where $S^{n}(1)$ denotes the Euclidean $n$-sphere of radius 1. We also always denote by $\alpha=2-\frac{n}{p}(>0)$ and $\beta=4-\frac{n}{q}(>0)$.

Let $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ be the class of compact connected smooth $n$-manifolds $M$ $(n \geq 3)$ with Yamabe metrics $g$ of unit volume which satisfy
$$\mu(M,[g]) \geq \mu_{0}>0 .$$

Inspired by the above problems, we obtain the following convergence theorem.

Theorem 1.1. Let $\left\{\left(M_{i}, g_{i}\right)\right\}_{i \in \mathbf{N}}$ be a sequence in $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ which satisfy
$$\int_{M_{i}}\left|R_{g_{i}}\right|^{n / 2} d v_{g_{i}} \leq \Lambda_{1}, \quad \int_{M_{i}}\left|\nabla A_{g_{i}}\right|^{q} d v_{g_{i}} \leq \Lambda_{2}$$
with some positive constants $\Lambda_{1}, \Lambda_{2}$, where $\left|R_{g_{1}}\right|$ denotes the norm of Riemann curvature tensor $R_{g_{i}}$ of $g_{i}$. Then either of the following two cases must be hold.
(1°) $\left(M_{i}, g_{i}\right)$ converges to a point in the Hausdorff distance.
(2°) There exist a subsequence $\{j\} \subset\{i\}$, a compact connected metric space $\left(M_{\infty}, d_{\infty}\right)$ with positive diameter and a finite subset $\mathcal{S}=\left\{x_{1}, \ldots, x_{k}\right\} \subset$ $M_{\infty}$ (possibly empty) such that:
(2°.1) $\left(M_{j}, g_{j}\right)$ converges to $\left(M_{\infty}, d_{\infty}\right)$ in the Hausdorff distance.
$\left(2^{\circ} .2\right) \quad M_{\infty} \backslash \mathcal{S}$ has a structure of smooth $n$-manifold and a $C^{\beta} \cap$ $L_{\mathrm{loc}}^{2, n q /(n-2 q)}$ metric $g_{\infty}$ of positive constant scalar curvature $S_{g_{\infty}}$ such that $g_{\infty}$ is compatible with the distance $d_{\infty}$ on $M_{\infty} \backslash \mathcal{S}$ and that
$$0<\mu_{0} \leq S_{g_{\infty}} \leq n(n-1) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n} .$$
(2°.3) For each compact subset $K \subset M_{\infty} \backslash \mathcal{S}$, there exists an into diffeomorphism $\Phi_{j}: K \longrightarrow M_{j}$ for $j$ sufficiently large such that the pull-back metrics $\left(\Phi_{j}\right)^{*} g_{j}$ converges to $g_{\infty}$ in the $C^{\beta^{\prime}}$ topology for $\beta^{\prime}<\beta$ and weakly in the $L^{2, n q /(n-2 q)}$ topology on $K$.
$$\lim _{j \rightarrow \infty} S_{g_{j}}=S_{g_{\infty}} .$$
(2°.5) For every $x_{a} \in \mathcal{S}(a=1, \ldots, k)$ and $j$, there exist $x_{a, j} \in M_{j}$ and positive number $r_{j}$ such that:
(2°.5 a) $B_{\varepsilon}\left(x_{a, j}\right)$ converges to $B_{\varepsilon}\left(x_{a}\right)$ in the Hausdorff distance for all $\varepsilon>0$.
$$\lim _{j \rightarrow \infty} r_{j}=\infty .$$
(2°.5 c) $\left(\left(M_{j}, r_{j} g_{j}\right), x_{a, j}\right)$ converges to $\left(\left(N_{a}, h_{a}\right), x_{a, \infty}\right)$ in the pointed Hausdorff distance, where $\left(N_{a}, h_{a}\right)$ is a complete noncompact, scalar-flat, non-flat $C^{\infty}$ Riemannian $n$-manifold which satisfies
$$\sup _{N_{a}}\left|R_{h_{a}}\right|<\infty, \quad 0<\int_{N_{a}}\left|R_{h_{a}}\right|^{n / 2} d v_{h_{a}}<\infty,$$
and
$$\operatorname{vol}\left(B_{r}(x) ; h_{a}\right) \geq\left(5 \cdot 2^{n}(n-1)\right)^{-n / 2}(n-2)^{n / 2} \mu_{0}^{n / 2} r^{n}$$
for $x \in N_{a}$ and $r>0$. In particular, when $n=3$ (resp. $n=4,5$ ) each ( $N_{a}, h_{a}$ ) is conformally flat (resp. of harmonic curvature).
(2°.5 d) For every $r>0$, there exists an into diffeomorphism $\Psi_{j}$ : $B_{r}\left(x_{a, \infty}\right) \longrightarrow M_{j}$ for $j$ sufficiently large such that $\left(\Psi_{j}\right)^{*}\left(r_{j} g_{j}\right)$ converges to $h_{a}$ in the $C^{1, \sigma}$ topology for $\sigma<1$ and weakly in the $L^{2, s}$ topology for $s>n$ on $B_{r}\left(x_{a, \infty}\right)$.
(2°.6) It holds
$$\lim _{j \rightarrow \infty} \int_{M_{j}}\left|R_{g_{j}}\right|^{n / 2} d v_{g_{j}} \geq \int_{M_{\infty}}\left|R_{g_{\infty}}\right|^{n / 2} d v_{g_{\infty}}+\sum_{a=1}^{k} \int_{N_{a}}\left|R_{h_{a}}\right|^{n / 2} d v_{h_{a}}$$

Remark 1.2.
\begin{itemize}
\item[(1)] Theorem 1.1 is a generalization of Theorem 1.2 in [Ak].
\item[(2)] Since the metric $g_{\infty}$ is of class $C^{\beta} \cap L_{\text {loc }}^{2, n q /(n-2 q)}$, then its curvature tensors $R_{g_{\infty}}, \operatorname{Ric}_{g_{\infty}}$ and $S_{g_{\infty}}$ make sense in $L_{\text {loc }}^{n q /(n-2 q)}$.
\item[(3)] It would be conjectured that only the second case (2°) holds, and when $n=3$ each conformally flat, scalar-flat 3-manifold $\left(N_{a}, h_{a}\right)$ in (2°. 5 c) is asymptotically locally Euclidean (cf. [BKN]). However, when solving them, a technical difficulty arises in obtaining volume estimates of geodesic balls from above. Moreover, when $n=3$ and $M_{i}$ is a quotient 3 -manifold $M^{3}$ of a homotopy 3 -sphere for all $i$, then it would be also conjectured that $\mathcal{S}=\phi$ (see [B, AC1] for reconstruction of manifolds).
\end{itemize}

The following result includes a pinching theorem for flat conformal structures of positive Yamabe invariant on compact 3 -manifolds (see Remark 2.2).

Theorem 1.3. For given positive constants $s\left(>\frac{n}{3}\right)$ and $\Lambda$, there exists a positive constant $\varepsilon_{0}=\varepsilon_{0}\left(\mu_{0}, n, p, s, \Lambda\right)$ such that if a compact Riemannian $n$-manifold $(M, g) \in \mathcal{Y}_{1}\left(n, \mu_{0}\right)$ satisfies
$$\int_{M}\left|R_{g}\right|^{p} d v_{g} \leq \Lambda, \quad \int_{M}\left|\nabla A_{g}\right|^{s} d v_{g} \leq \varepsilon_{0}$$
then $M$ admits a Yamabe metric $h$ of harmonic curvature with
$$V_{h}=1, \quad \mu(M,[h]) \geq \mu_{0}>0 .$$
In particular, when $n=3\left(M^{3}, h\right)$ is conformally flat, and a finite cover of $M^{3}$ is diffeomorphic to $S^{3}$ or a connected sum $k\left(S^{1} \times S^{2}\right)$ for some $k \in \mathrm{~N}$.

In §2 we give basic known facts on Yamabe metrics and the Hausdorff distance. These contain a geometric inequality for Yamabe metrics of positive scalar curvature, which plays a key role in our proofs. In §3 we give the notion of $L^{2, p}$ harmonic radius. We then summarize convergence results
for manifolds and a priori estimates for $L^{2, p}$ harmonic radius, which were developed mainly by Anderson [An2, 3, AC2]. The proofs of our theorems are essentially based on these results. For the proofs of Theorem 1.1 and Theorem 1.3, we also give another a priori estimate for $L^{2, p}$ harmonic radius. In §4, using these results, we prove compactness and pinching theorems for Yamabe metrics of positive scalar curvature, and we also prove Theorem 1.3. Finally, in §5 we give the proof of Theorem 1.1.

Acknowledgment. I would like to thank Professors A. Kasue and S. Nayatani for useful discussions. I would also like to thank Professor A. Treibergs for his kind hospitality while I visited to the University of Utah in summer 1993, when part of this work was carried out.

\section*{2. Preliminaries.}

In this section, first we shall give several known properties for Yamabe metrics. Let $M$ be a compact $n$-manifold. Since a Yamabe metric $g$ on $M$ is a minimizer of the Yamabe functional $I:[g] \longrightarrow \mathbf{R}$, then the first variational formula shows the following equation (cf. [Au2], [LP]):
$$S_{g}=\mu(M,[g]) V_{g}^{-2 / n} \equiv \mathrm{const} . .$$
Moreover, the following inequality is due to Aubin [Au1].
$$\mu(M,[g]) \leq n(n-1) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n} .$$
Now let $g$ be a Yamabe metric of positive scalar curvature on $M$. The Yamabe invariant $\mu(M,[g])$ is rewritten as
$$\mu(M,[g])=\inf _{\substack{u \in L^{1,2}(M) \\ u \neq 0}} \frac{\frac{4 \frac{n-1}{n-2} \int_{M}|\nabla u|^{2} d v_{g}+\int_{M} S_{g} u^{2} d v_{g}}{\left(\int_{M}|u|^{2 n /(n-2)} d v_{g}\right)^{(n-2) / n}}}{\left(\int_{M}\right.},$$
where $L^{1,2}(M)$ denotes the Sobolev space of functions on $M$ with $L^{2}$ first derivatives (cf. [Au2, GT]). It then follows from (2.1), (2.3) and the positivity of $\mu(M,[g])$ that
$$\left(\int_{M}|u|^{2 n /(n-2)} d v_{g}\right)^{(n-2) / n} \leq \frac{1}{c_{g}} \int_{M}|\nabla u|^{2} d v_{g}+\frac{1}{V_{g}^{2 / n}} \int_{M} u^{2} d v_{g}$$
for $u \in L^{1,2}(M)$, where $c_{g}=\frac{n-2}{4(n-1)} \mu(M,[g])>0$. By the Sobolev inequality (2.4), we can prove the following geometric inequalities for Yamabe metrics of positive scalar curvature (cf. [Ak]). In particular, the first inequality (2.5) is of essential use in the proofs of our theorems.

Proposition 2.1. Let $g$ be a Yamabe metric of positive scalar curvature on $M$. Then
$$\begin{gathered}
\operatorname{vol}\left(B_{r}(x)\right) \geq\left(5 \cdot 2^{n-2}\right)^{-n / 2} c_{g}^{n / 2} r^{n} \quad \text { for } x \in M \text { and } r \leq \sqrt{\frac{V_{g}^{2 / n}}{c_{g}}}, \\
\operatorname{diam}(M, g) \leq 2\left(5 \cdot 2^{n-2}\right)^{n / 2} \sqrt{\frac{V_{g}^{2 / n}}{c_{g}}},
\end{gathered}$$
where $B_{r}(x)=B_{r}(x ; g)$ denotes the geodesic ball of radius $r$ centered at $x$ and $\operatorname{vol}\left(B_{r}(x)\right)=\operatorname{vol}\left(B_{r}(x) ; g\right)$ the volume of $B_{r}(x)$ with respect to $g$.

Remark 2.2. Let $\mathcal{M}_{1}\left(n, \mu_{0}, p, S_{0}\right)$ (resp. $\mathcal{M}_{1}\left(n, \mu_{0}\right)$ ) denote the class of compact Riemannian $n$-manifolds $(M, g)$ of unit volume which satisfy
$$\begin{aligned}
& \mu(M,[g]) \geq \mu_{0}>0, \quad \int_{M}\left(S_{g}^{+}\right)^{p} d v_{g} \leq S_{0}, \\
(\text { resp. } \quad & \left.\mu(M,[g]) \geq \mu_{0}>0\right),
\end{aligned}$$
where $S_{g}^{+}=\max \left\{S_{g}, 0\right\}$ and $p>\frac{n}{2}$. For an element $(M, g) \in \mathcal{M}_{1}\left(n, \mu_{0}, p, S_{0}\right)$, Kasue and Kumura [KK] proved geometric inequalities similar to (2.5) and (2.6). In Theorem 2.3 below, if we replace $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ by $\mathcal{M}_{1}\left(n, \mu_{0}, p, S_{0}\right)$, then the same conclusion holds. We can also prove convergence theorems for Riemannian manifolds in $\mathcal{M}_{1}\left(n, \mu_{0}, p, S_{0}\right)$ with integral bounds on curvature, similar to those in this paper. In particular, if we only replace $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ by $\mathcal{M}_{1}\left(n, \mu_{0}\right)$ in Theorems 1.3 and 4.1, then similar conclusions hold.

Next, we recall the definition of the Hausdorff distance on the set $\mathcal{M E T}$ of all isometry classes of compact metric spaces introduced by Gromov [Gr] (cf. [F]). Let $X$ and $Y$ be compact metric spaces. A map $f: X \longrightarrow Y$ (not necessarily continuous) is said to be an $\varepsilon$-Hausdorff approximation if the following two conditions are satisfied.
$$\begin{aligned}
& \text { The } \varepsilon \text {-neighborhood of } f(X) \text { in } Y \text { is equal to } Y \text {. } \\
& \left|d_{X}(x, y)-d_{Y}(f(x), f(y))\right|<\varepsilon \quad \text { for } x, y \in X \text {. }
\end{aligned}$$
The Hausdorff distance $d_{H}(X, Y)$ between $X$ and $Y$ is defined to be the infimum of all positive numbers $\varepsilon$ such that there exist $\varepsilon$-Hausdorff approximations from $X$ to $Y$ and from $Y$ to $X$. Unfortunately $d_{H}(\cdot, \cdot)$ does not satisfy the triangle inequality. However the inequality (2.7) below holds and then shows that it gives a metrizable complete uniform structure on the set $\mathcal{M} \mathcal{E} \mathcal{T}$. Thus we treat $d_{H}(\cdot, \cdot)$ as if it is a distance function.
$$d_{H}(X, Z) \leq 2\left\{d_{H}(X, Y)+d_{H}(Y, Z)\right\},$$
for $X, Y, Z \in \mathcal{M} \mathcal{E} \mathcal{T}$.
For noncompact metric spaces, we also recall the definition of the pointed Hausdorff distance. Let $(X, x)$ and $(Y, y)$ be pointed metric spaces (possibly compact). A map $f:(X, x) \longrightarrow(Y, y)$ is said to be an $\varepsilon$-pointed Hausdorff approximation if
$$\begin{aligned}
& f(x)=y \\
& f\left(B_{1 / \varepsilon}(x)\right) \subset B_{1 / \varepsilon}(y) \\
& \left.f\right|_{B_{1 / \varepsilon}(x)}: B_{1 / \varepsilon}(x) \longrightarrow B_{1 / \varepsilon}(y) \text { is an } \varepsilon \text {-Hausdorff approximation. }
\end{aligned}$$
The pointed Hausdorff distance $d_{p, H}((X, x),(Y, y))$ between pointed metric spaces $(X, x)$ and $(Y, y)$ is the infimum of all positive numbers $\varepsilon$ such that there exist $\varepsilon$-pointed Hausdorff approximations from $(X, x)$ to $(Y, y)$ and from ( $Y, y$ ) to ( $X, x$ ). $d_{p, H}(\cdot, \cdot)$ also defines a distance on the set $\mathcal{M} \mathcal{E} \mathcal{T}_{0}$ of all isometry classes of pointed metric spaces whose metric balls are all precompact.

By (2.2), (2.5) and (2.6), we can prove the following precompactness theorem for Yamabe metric of positive scalar curvature (cf. [Ak]), which is also of use in the proof of Theorem 1.1.

Theorem 2.3. The set $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ is precompact in $\mathcal{M E T}$ with respect to the Hausdorff distance.

\section*{3. $L^{2, p}$ harmonic radius.}

In this section, we first give the notion of $L^{2, p}$ harmonic radius (cf. [An2, 3], [AC2]). Let $(M, g)$ be a complete Riemannian $n$-manifold (without boundary). For given $p\left(>\frac{n}{2}\right)$ and $L(>0)$, the $L^{2, p}$ harmonic radius at $x \in M$ is the radius $r_{H}(x)=r_{H}(x ; g, p, L)$ of the largest geodesic ball $B_{r_{H}(x)}(x)(\subset M)$ centered at $x$, on which there exist harmonic coordinates $U=\left\{u^{i}\right\}_{i=1}^{n}$ : $B_{r_{H}(x)}(x) \longrightarrow \mathbf{R}^{n}$ (cf. [J, DK]) such that the metric components $g_{i j}=$ $g\left(\partial / \partial u^{i}, \partial / \partial u^{j}\right)$ are bounded in the $L^{2, p}$ norm on $\tilde{B}=U\left(B_{r_{H}(x)}(x)\right)$, i.e.,
$$\begin{aligned}
& e^{-L} \cdot \delta_{i j} \leq g_{i j} \leq e^{L} \cdot \delta_{i j} \quad \text { (as bilinear forms) }, \\
& r_{H}(x)^{\alpha-1}\left\|\partial g_{i j}\right\|_{L^{p}(\tilde{B})}+r_{H}(x)^{\alpha}\left\|\partial \partial g_{i j}\right\|_{L^{p}(\tilde{B})} \leq L
\end{aligned}$$
for $i, j=1, \cdots, n$, where $\alpha=2-\frac{n}{p}(>0)$.
Remark 3.1.
\begin{itemize}
\item[(1)] By the Sobolev embedding theorem $L^{2, p}(\tilde{B}) \subset C^{\alpha}(\tilde{B})$, the $L^{2, p}$ harmonic radius controls the $C^{\alpha}$ norm of $g_{i j}$ on $\tilde{B}$.
\end{itemize}
\begin{itemize}
\item[(2)] For the rescaled metric $h=\lambda^{2} \cdot g(\lambda \equiv$ const. $>0)$, the $L^{2, p}$ harmonic radius at $x$ changes as follows;
$$r_{H}(x ; h)=\lambda \cdot r_{H}(x ; g) .$$
\end{itemize}

Next we shall summarize part of convergence results for manifolds and a priori estimates for $L^{2, p}$ harmonic radius, which were developed by Anderson [An1-3, AC2] and also many mathematicians (cf. [BKN, Ga1-2, GW, Gr, Ka, N, P, Yn1, 3]). These are also of essential use in our proofs of §4 and §5.

Theorem 3.2. Let $\left\{\left(M_{i}, g_{i}\right)\right\}_{i \in \mathrm{~N}}$ be a sequence of compact $C^{\infty}$ Riemannian $n$-manifolds which satisfy, for each $i \in \mathbf{N}$
$$r_{H}(x) \geq r_{0} \quad \text { for } \quad x \in M_{i}, \quad V_{g_{i}} \leq V_{0}$$
with some positive constants $r_{0}, V_{0}$. Then there exist a subsequence $\{j\} \subset$ $\{i\}$, a compact $C^{\infty} n$-manifold $M_{\infty}$ with $C^{\alpha} \cap L^{2, p}$ metric $g_{\infty}$ and a diffeomorphism $\Phi_{j}: M_{\infty} \longrightarrow M_{j}$ for each $j$ such that $\left(\Phi_{j}\right)^{*} g_{j}$ converges to $g_{\infty}$ in the $C^{\alpha^{\prime}}$ topology for $\alpha^{\prime}<\alpha$ and weakly in the $L^{2, p}$ topology on $M_{\infty}$.

Remark 3.3. In Theorem 3.2, we should remark the following fact. For a point $x \in M_{\infty}$ and fix it. From (3.3), for each $h(j)=\left(\Phi_{j}\right)^{*} g_{j}$, there exist harmonic coordinates
$$U_{j}=\left\{u^{a}\right\}_{a=1}^{n}\left(=\left\{u(j)^{a}\right\}_{a=1}^{n}\right): B_{r_{0}}\left(\subset M_{\infty}\right) \longrightarrow \mathbf{R}^{n} \quad \text { with } \quad U_{j}(x)=\mathbf{0} \in \mathbf{R}^{n}$$
such that the metric components $h(j)_{a b}=h(j)\left(\partial / \partial u^{a}, \partial / \partial u^{b}\right)$ satisfy (3.1) and (3.2). Then, by (3.1), (3.2), the $L^{p}$ estimates for elliptic differential equations (cf. [GT]) and the construction of $\Phi_{j}$ and $M_{\infty}$, there exists a coordinate system $\left\{V_{\lambda}\right\}_{\lambda=1}^{m}$ of class $C^{\infty}$ on $M_{\infty}$ such that
$$\left\|U_{j} \circ V_{\lambda}^{-1}\right\|_{L^{4, p}} \leq C, \quad\left\|U_{j} \circ V_{\lambda}^{-1}\right\|_{C^{2, \alpha}} \leq C$$
where $C$ is independent of $j$ and $x \in M_{\infty}$ (cf. [AC2, Ka]). Similar results hold in the following Theorems 3.4 and 3.5.

Theorem 3.4. Let $\left\{\left(M_{i}, g_{i}\right)\right\}_{i \in \mathrm{~N}}$ be a sequence of compact $C^{\infty}$ Riemannian $n$-manifolds and $\Omega_{i} \subset M_{i}$ open subsets (possibly disconnected) which satisfy, for each $i \in \mathbf{N}$
$$r_{H}(x) \geq r_{0} \quad \text { for } \quad x \in \Omega_{i} \subset M_{i}, \quad 0<c_{1} \leq \operatorname{vol}\left(\Omega_{i}\right) \leq c_{2}$$
and that each $\Omega_{i}(2 \varepsilon)=\left\{x \in \Omega_{i} ;\right.$ dist $\left._{g_{i}}\left(x, \partial \Omega_{i}\right)>2 \varepsilon\right\}$ is nonempty, where $r_{0}, c_{1}, c_{2}$ and $\varepsilon$ denote positive constants. Then there exist a subsequence
$\{j\} \subset\{i\}$, a compact $C^{\infty} n$-manifold $\Omega_{\infty}(\varepsilon)$ (possibly disconnected but only finitely many components) with $C^{\alpha} \cap L^{2, p}$ metric $g_{\infty}$ and an into diffeomorphism $\Phi_{j}: \Omega_{\infty}(\varepsilon) \longrightarrow \Omega_{j}\left(\frac{\varepsilon}{2}\right)$ with $\Phi_{j}\left(\Omega_{\infty}(\varepsilon)\right) \supset \Omega_{j}\left(\frac{3}{2} \varepsilon\right)$ for each $j$ such that $\left(\Phi_{j}\right)^{*} g_{j}$ converges to $g_{\infty}$ in the $C^{\alpha^{\prime}}$ topology for $\alpha^{\prime}<\alpha$ and weakly in the $L^{2, p}$ topology on $\Omega_{\infty}(\varepsilon)$.

Theorem 3.5. Let $\left\{\left(M_{i}, g_{i}, b_{i}\right)\right\}_{i \in \mathrm{~N}}$ be a sequence of pointed compact $C^{\infty}$ Riemannian $n$-manifolds which satisfy:
$$\sup _{M_{3}}\left|R_{g_{i}}\right| \leq \Lambda \quad \text { for } \quad i \in \mathbf{N}$$
with some constant $\Lambda$,
$$\operatorname{diam}\left(M_{i}, g_{i}\right) \longrightarrow \infty \quad(i \longrightarrow \infty),$$
and for any $R>0$ there exist $i_{R} \in \mathbf{N}$ and $r_{0}(>0)$ such that
$$\operatorname{inj}_{\left(M_{i}, g_{i}\right)}(x) \geq r_{0}>0 \quad \text { for } \quad x \in B_{R}\left(b_{i} ; g_{i}\right), \quad i \geq i_{R},$$
where $\operatorname{inj}_{\left(M_{i}, g_{i}\right)}(x)$ denotes the injectivity radius of $\left(M_{i}, g_{i}\right)$ at $x$. Then there exist a subsequence $\{j\} \subset\{i\}$ and a noncompact complete $C^{\infty}$ pointed $n$ manifold $\left(N, b_{\infty}\right)$ with $C^{1, \sigma}(0<\sigma<1)$ metric $h$ such that $\left(M_{j}, g_{j}, b_{j}\right)$ converges to $\left(N, h, b_{\infty}\right)$ in the pointed Hausdroff distance. Moreover, for each $r>0$ there exists an into diffeomorphism $\Phi_{j}: B_{r}\left(b_{\infty} ; h\right)(\subset N) \longrightarrow M_{j}$ with $b_{j} \in \Phi_{j}\left(B_{r}\left(b_{\infty} ; h\right)\right)$ for $j$ sufficiently large such that $\left(\Phi_{j}\right)^{*} g_{j}$ converges to $h$ in the $C^{1, \sigma}$ topology on $B_{r}\left(b_{\infty} ; h\right)$ and that $\lim _{j \rightarrow \infty} \Phi_{j}^{-1}\left(b_{j}\right)=b_{\infty}$.

In order to state a priori estimates for $L^{2, p}$ harmonic radius, we set, for a given $\delta>0$
$$v^{\delta}(x)=\sup \left\{r>0 ; \operatorname{vol}\left(B_{s}(y)\right) \geq \delta \cdot s^{n} \quad \text { for all } \quad B_{s}(y) \subset B_{r}(x)\right\},$$
which was introduced by Anderson [An3]. We note that, for each $\delta<\omega_{n}$, $v^{\delta}(x)$ is positive for any $x \in M$, where $\omega_{n}$ denotes the volume of the unit ball in $\mathbf{R}^{n}$. Let $\mathcal{M}_{1}(n)$ denote the space of all compact $C^{\infty}$ Riemannian $n$-manifolds $(M, g)$ with unit volume $V_{g}=1$.

Theorem 3.6. For $(M, g) \in \mathcal{M}_{1}(n)$ which satisfies
$$\int_{M}\left|R_{g}\right|^{p} d v_{g} \leq \Lambda$$
with some positive constant $\Lambda$. Then there exists a positive constant $c_{0}=$ $c_{0}(\Lambda, n, p, \delta, L)$ such that
$$r_{H}(x) \geq c_{0} \cdot v^{\delta}(x) \quad \text { for } \quad x \in M \text {. }$$

Theorem 3.7. Let $(M, g)$ be an element in $\mathcal{M}_{1}(n)$ which satisfies
$$\int_{B_{r}}\left|R_{g}\right|^{p} d v_{g} \leq \Lambda$$
with some positive constant $\Lambda$, where $B_{r}$ denotes a geodesic ball of radius $r>0$ in $M$. Then there exists a positive constant $c_{0}=c_{0}(\Lambda, n, p, \delta, L)$ such that
$$\gamma_{H}(x) \geq c_{0} \cdot \nu^{\delta}(x) \quad \text { for } \quad x \in B_{r},$$
where $\gamma_{H}(x)=\min \left\{r_{H}(x), \operatorname{dist}_{g}\left(x, \partial B_{r}\right)\right\}$ and $\nu^{\delta}(x)=\min \left\{v^{\delta}(x)\right.$, $\left.\operatorname{dist}_{g}\left(x, \partial B_{r}\right)\right\}$.

Finally, for the proofs of Theorem 1.1 and Theorem 1.3, we shall prove another a priori estimate for $L^{2, p}$ harmonic radius. To start with, we prove the following lemma (cf. [An1, SU, S2]).

Lemma 3.8. Let $(M, g)$ be a compact $C^{\infty}$ Riemannian $n$-manifold which satisfies the following Sobolev inequality
$$\left(\int_{M}|u|^{2 n /(n-2)} d v_{g}\right)^{(n-2) / n} \leq \frac{1}{c_{s}} \int_{M}|\nabla u|^{2} d v_{g}+\frac{1}{V_{g}^{2 / n}} \int_{M} u^{2} d v_{g}$$
for $u \in L^{1,2}(M)$ with some positive constant $c_{s}$ and
$$\int_{M}\left|\nabla A_{g}\right|^{q} \leq \Lambda$$
with some constant $\Lambda$. Then there exist positive constants $\varepsilon_{0}=\varepsilon_{0}\left(n, q, c_{s}\right)$ and $c_{1}=c_{1}\left(n, q, c_{s}, V_{g}, \Lambda, r\right)$ such that, if
$$\int_{B_{r}}\left|R_{g}\right|^{n / 2} d v_{g} \leq \varepsilon_{0},$$
then
$$\int_{B_{\frac{r}{2}}}\left|R_{g}\right|^{n q /(n-2 q)} d v_{g} \leq c_{1}$$
where $B_{r}=B_{r}(x)$ is a geodesic ball of radius $r>0$ in $M$.
Proof. We first note that the Riemann curvature tensor $R_{g}=\left(R_{i j k l}\right)$ satisfies the following equation
$$\Delta_{g} R_{i j k l}=-\nabla_{i} A_{j k l}+\nabla_{j} A_{i k l}+\left(R_{g} * R_{g}\right)_{i j k l},$$
where $R_{g} * R_{g}$ denotes a linear combination of contractions of the tensor $R_{g} \otimes R_{g}$ by the metric $g$ and $\Delta_{g}=g^{i j} \nabla_{i} \nabla_{j}$ the (nonpositive) Laplacian of $g$, respectively. From (3.8), we then obtain the following differential inequality
$$\Delta_{g}\left|R_{g}\right| \geq-c_{2}\left|\nabla A_{g}\right|-c_{3}\left|R_{g}\right|^{2},$$
where $c_{2}$ and $c_{3}$ are positive constants depending only on $n$.
Let $u=\left|R_{g}\right|$ and $\xi$ a cut-off function satisfying $\xi=1$ on $B_{\frac{r}{2}}$ and $\xi=$ 0 on $M \backslash B_{r}$ with $|\nabla \xi| \leq \frac{4}{r}$. Using Hölder's inequality in (3.5), we may particularly assume $q \leq \frac{n^{2}}{4(n-1)}$. Multiply both sides of (3.9) by $\xi^{2} u^{\tau}$, where $\tau=\frac{n(q-1)}{n-2 q}\left(\max \left\{1, \frac{2 n-4}{n}\right\}<\tau+1 \leq \frac{n}{2}\right)$. Integrating by part, we obtain
$$\begin{aligned}
& \frac{4 \tau}{(\tau+1)^{2}} \int \xi^{2}\left|\nabla\left(u^{(\tau+1) / 2}\right)\right|^{2} d v_{g}-2 \int \xi u^{\tau}|\nabla \xi||\nabla u| d v_{g} \\
& \leq c_{4} \int \xi^{2} u^{\tau}\left(\left|\nabla A_{g}\right|+u^{2}\right) d v_{g},
\end{aligned}$$
where $c_{4}=\max \left\{c_{2}, c_{3}\right\}$. The Young inequality implies
$$\xi u^{\tau}|\nabla \xi||\nabla u| \leq u^{\tau+1}|\nabla \xi|^{2}+\frac{\xi^{2}}{(\tau+1)^{2}}\left|\nabla\left(u^{(\tau+1) / 2}\right)\right|^{2} .$$
Using (3.10) in (3.11) then gives
$$\begin{aligned}
& \int \xi^{2}\left|\nabla\left(u^{(\tau+1) / 2}\right)\right|^{2} d v_{g} \\
& \leq \frac{(\tau+1)^{2}}{(4 \tau-2)}\left[c_{4} \int \xi^{2} u^{\tau}\left(\left|\nabla A_{g}\right|+u^{2}\right) d v_{g}+2 \int u^{\tau+1}|\nabla \xi|^{2} d v_{g}\right] .
\end{aligned}$$
From (3.4) and (3.12), we obtain
$$\begin{aligned}
& \left(\int\left(\xi u^{(\tau+1) / 2}\right)^{2 n /(n-2)} d v_{g}\right)^{(n-2) / n} \\
& \leq \frac{c_{5} \tau}{c_{s}} \int\left(\xi^{2} u^{\tau+2}+\xi^{2} u^{\tau}\left|\nabla A_{g}\right|+|\nabla \xi|^{2} u^{\tau+1}\right) d v_{g}+\frac{1}{V_{g}^{2 / n}} \int \xi^{2} u^{\tau+1} d v_{g}
\end{aligned}$$
where $c_{5}$ is a positive constant depending only on $n$.
By Hölder's inequality, we note
$$\int \xi^{2} u^{\tau+2} d v_{g} \leq\left(\int_{B_{r}} u^{n / 2} d v_{g}\right)^{2 / n}\left(\int\left(\xi u^{(\tau+1) / 2}\right)^{2 n /(n-2)} d v_{g}\right)^{(n-2) / n}$$

Taking $\varepsilon_{0}$ in (3.6) satisfying $\varepsilon_{0}^{2 / n} \leq \frac{c_{s}}{2 c_{5} \tau}$, it then follows from (3.5), (3.13), (3.14) and Hölder's inequality again that
$$\begin{aligned}
& \left(\int \xi^{2 n /(n-2)}\left|R_{g}\right|^{n q /(n-2 q)} d v_{g}\right)^{(n-2) / n} \\
& \leq\left(\int\left(\xi u^{(\tau+1) / 2}\right)^{2 n /(n-2)} d v_{g}\right)^{(n-2) / n} \\
& \leq \frac{2 c_{5} \tau}{c_{s}} \int\left(|\nabla \xi|^{2} u^{\tau+1}+\xi^{2} u^{\tau}\left|\nabla A_{g}\right|\right) d v_{g}+\frac{2}{V_{g}^{2 / n}} \int \xi^{2} u^{\tau+1} d v_{g} \\
& \leq c_{6}\left[\int\left(|\xi|^{2}+|\nabla \xi|^{2}\right) u^{\tau+1} d v_{g}\right. \\
& \left.\quad+\left(\int_{B_{r}}\left|\nabla A_{g}\right|^{q} d v_{g}\right)^{1 / q} \cdot\left(\int\left(\xi^{2} u^{\tau}\right)^{q /(q-1)} d v_{g}\right)^{(q-1) / q}\right] \\
& \leq c_{7}\left(1+\frac{1}{r^{2}}\right)\left(\int_{B_{r}}\left|R_{g}\right|^{n / 2} d v_{g}\right)^{2(\tau+1) / n} \\
& +c_{6}\left(\int_{M}\left|\nabla A_{g}\right|^{q} d v_{g}\right)^{1 / q} \cdot\left(\int \xi^{2 n /(n-2)} u^{n q /(n-2 q)} d v_{g}\right)^{(q-1) / q} \\
& \leq c_{7}\left(1+\frac{1}{r^{2}}\right) \varepsilon_{0}^{2(\tau+1) / n}+c_{6} \Lambda^{1 / q} \cdot\left(\int \xi^{2 n /(n-2)}\left|R_{g}\right|^{n q /(n-2 q)} d v_{g}\right)^{(q-1) / q},
\end{aligned}$$
where $c_{6}=c_{6}\left(n, c_{s}, V_{g}\right)$ and $c_{7}=c_{7}\left(n, q, c_{s}, V_{g}\right)$.
Set $X=\int \xi^{2 n /(n-2)}\left|R_{g}\right|^{n q /(n-2 q)} d v_{g}$. The inequality (3.15) implies
$$X^{(n-2) / n}-c_{6} \Lambda^{1 / q} \cdot X^{(q-1) / q}-c_{7}\left(1+\frac{1}{r^{2}}\right) \varepsilon_{0}^{2 q(n-2) / n(n-2 q)} \leq 0 .$$
From $q<\frac{n}{2}$ we note
$$0<\frac{q-1}{q}<\frac{n-2}{n} .$$
It then follows from (3.16) and (3.17) that there exists a positive constant $c_{1}=c_{1}\left(n, q, c_{s}, V_{g}, \Lambda, r\right)$ such that
$$\int_{B_{\frac{r}{2}}}\left|R_{g}\right|^{n q /(n-2 q)} d v_{g} \leq X \leq c_{1} .$$
This completes the proof of Lemma 3.8. \(\square\)

Proposition 3.9. Let $(M, g)$ be an element in $\mathcal{M}_{1}(n)$ which satisfies the Sobolev inequality (3.4) and (3.5) in Lemma 3.8. Let $B_{r}$ denote a geodesic
ball of radius $r>0$ in $M$. Then there exist positive constants $\varepsilon_{0}=\varepsilon_{0}\left(n, q, c_{s}\right)$ and $c_{0}=c_{0}\left(n, q, c_{s}, \Lambda, r, \delta, L\right)$ such that if
$$\int_{B_{2 r}}\left|R_{g}\right|^{n / 2} d v_{g} \leq \varepsilon_{0}$$
then
$$\gamma_{H}(x) \geq c_{0} \cdot \nu^{\delta}(x) \quad \text { for } \quad x \in B_{r},$$
where $\gamma_{H}(x)=\min \left\{r_{H}(x), \operatorname{dist}_{g}\left(x, \partial B_{r}\right)\right\}, \nu^{\delta}(x)=\min \left\{v^{\delta}(x), \operatorname{dist}_{g}\left(x, \partial B_{r}\right)\right\}$ and $r_{H}(x)$ denotes the $L^{2, n q /(n-2 q)}$ harmonic radius at $x$.

Proof. We take the same $\varepsilon_{0}$ in (3.18) as in (3.6). By Lemma 3.8 we obtain the following estimate
$$\int_{B_{r}}\left|R_{g}\right|^{n q /(n-2 q)} d v_{g} \leq \tilde{c}_{1}$$
where $\tilde{c}_{1}=\tilde{c}_{1}\left(n, q, c_{s}, \Lambda, r\right)$. It then follows from (3.19) and Theorem 3.7 that there exists a positive constant $c_{0}=c_{0}\left(n, q, c_{s}, \Lambda, r, \delta, L\right)$ such that
$$\gamma_{H}(x) \geq c_{0} \cdot \nu^{\delta}(x) \quad \text { for } \quad x \in B_{r} .$$
This completes the proof of Proposition 3.9. \(\square\)

\section*{4. Compactness and pinching theorems for Yamabe metrics.}

In this section, we shall prove compactness and pinching theorems for Yamabe metrics of positive scalar curvature with integral bounds on curvature, and we also prove Theorem 1.3.

Theorem 4.1. Let $\left\{\left(M_{i}, g_{i}\right)\right\}_{i \in \mathbb{N}}$ be a sequence in $\mathcal{Y}_{1}\left(n, \mu_{0}\right)$ such that each $\left(M_{i}, g_{i}\right)$ satisfies
$$\int_{M_{\imath}}\left|R_{g_{\imath}}\right|^{p} d v_{g_{\imath}} \leq \Lambda$$
with some positive constant $\Lambda$. Then there exist a subsequence $\{j\} \subset\{i\}$, a compact $C^{\infty} n$-manifold $M_{\infty}$ with $C^{\alpha} \cap L^{2, p}$ metric $g_{\infty}$ of positive constant scalar curvature $S_{g_{\infty}}$ and a diffeomorphism $\Phi_{j}: M_{\infty} \longrightarrow M_{j}$ for each $j$ such that the following hold.
$$V_{g_{\infty}}=1, \quad 0<\mu_{0} \leq S_{g_{\infty}} \leq n(n-1) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n} .$$
$\left(\Phi_{j}\right)^{*} g_{j}$ converges to $g_{\infty}$ in the $C^{\alpha^{\prime}}$ topology for $\alpha^{\prime}<\alpha$ and weakly in the $L^{2, p}$ topology on $M_{\infty}$.

Moreover, there are only finitely many diffeomorphism types of compact $n$ manifolds $M$, which satisfy that there exists a Yamabe metric $g$ on each $M$ such that $(M, g) \in \mathcal{Y}_{1}\left(n, \mu_{0}\right)$ with (4.1).

Corollary 4.2. There exists a positive constant $\varepsilon_{0}=\varepsilon_{0}\left(n, p, \mu_{0}\right)$ such that if a compact Riemannian manifold $(M, g) \in \mathcal{Y}_{1}\left(n, \mu_{0}\right)$ satisfies
$$\int_{M}\left|Z_{g}\right|^{p} d v_{g} \leq \varepsilon_{0},$$
then $M$ admits a $C^{\infty}$ metric $h$ of positive constant curvature with
$$V_{h}=1, \quad \mu(M,[h]) \geq \mu_{0}>0,$$
where $Z_{g}=\left(Z_{i j k l}\right)$ denotes the concircular curvature tensor of $g$, i.e.,
$$Z_{i j k l}=R_{i j k l}-\frac{S_{g}}{n(n-1)}\left(g_{i k} g_{j l}-g_{i l} g_{j k}\right) .$$
Moreover,
$$\#\left(\pi_{1}(M)\right) \leq\left(\frac{n(n-1) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n}}{\mu_{0}}\right)^{n / 2} .$$

Remark 4.3. Under more general setting, compactness and pinching results similar to Theorem 4.1 and Corollary 4.2 have been already proved in [An3] and [Yn2]. However, we make only minimal assumptions for Yamabe metrics of positive scalar curvature and conclude some additional results.
Proof of Theorem 4.1. Set $\delta=\left(5 \cdot 2^{n-2}\right)^{-n / 2}\left(\frac{n-2}{4(n-1)}\right)^{n / 2} \mu_{0}^{n / 2}>0$. From (2.2), (2.5) and $V_{g_{1}}=1$, we obtain
$$v^{\delta}(x) \geq \sqrt{\frac{4}{n(n-2) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n}}}>0 \quad \text { for } \quad x \in M .$$
Using (4.1) and (4.3) in Theorem 3.6, then there exists a positive constant $c_{0}=c_{0}(\Lambda, n, p)$ such that the following estimate for $L^{2, p}$ harmonic radius holds
$$r_{H}(x) \geq c_{0} \sqrt{\frac{4}{n(n-2) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n}}}>0 \quad \text { for } \quad x \in M .$$
It then follows from (4.4) and Theorem 3.2 that there exist a subsequence $\{j\} \subset\{i\}$, a compact $C^{\infty} n$-manifold $M_{\infty}$ with $C^{\alpha} \cap L^{2, p}$ metric $g_{\infty}$ and a
diffeomorphism $\Phi_{j}: M_{\infty} \longrightarrow M_{j}$ for each $j$ such that $\left(\Phi_{j}\right)^{*} g_{j}$ converges to $g_{\infty}$ in the $C^{\alpha^{\prime}}$ topology for $\alpha^{\prime}<\alpha$ and weakly in the $L^{2, p}$ topology on $M_{\infty}$, and then $V_{g_{\infty}}=1$.

Moreover, taking a subsequence if necessary, we may assume that
$$\lim _{j \rightarrow \infty} S_{g_{j}}=S_{g_{\infty}} \equiv \text { const., }$$
then we also obtain
$$0<\mu_{0} \leq S_{g_{\infty}} \leq n(n-1) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n} .$$
This completes the proof of Theorem 4.1. \(\square\)

Proof of Corollary 4.2. Our assertion will be done by contradiction. If the assertion does not hold, then there exist sequences $\left\{\varepsilon_{i}\right\}_{i \in \mathrm{~N}}$ of positive constants and $\left\{\left(M_{i}, g_{i}\right)\right\}_{i \in \mathbf{N}} \subset \mathcal{Y}_{1}\left(n, \mu_{0}\right)$ satisfying $\varepsilon_{1}>\varepsilon_{2}>\cdots \longrightarrow 0$ and
$$\int_{M_{i}}\left|Z_{g_{i}}\right|^{p} d v_{g_{i}} \leq \varepsilon_{i}$$
for all $i \in \mathbf{N}$ such that each $M_{i}$ never admits a metric of positive constant curvature.

From (2.2) and $\left|R_{g_{2}}\right|^{2}=\left|Z_{g_{2}}\right|^{2}+\frac{2}{n(n-1)} S_{g_{2}}^{2}$, we first note that
$$\left|R_{g_{i}}\right| \leq\left|Z_{g_{i}}\right|+\sqrt{2 n(n-1)} \operatorname{vol}\left(S^{n}(1)\right)^{2 / n}$$
for $i \in \mathbf{N}$. Combinig (4.5) and (4.6) with Minkowski's inequality, we have
$$\begin{aligned}
\int_{M_{\mathrm{i}}}\left|R_{g_{\mathrm{i}}}\right|^{p} d v_{g_{\mathrm{i}}} & \leq\left[\left(\int_{M_{\mathrm{i}}}\left|Z_{g_{i}}\right|^{p} d v_{g_{\mathrm{i}}}\right)^{1 / p}+\sqrt{2 n(n-1)} \operatorname{vol}\left(S^{n}(1)\right)^{2 / n}\right]^{p} \\
& \leq\left[\varepsilon_{i}^{1 / p}+\sqrt{2 n(n-1)} \operatorname{vol}\left(S^{n}(1)\right)^{2 / n}\right]^{p}
\end{aligned}$$
for $i \in \mathbf{N}$. It then follows from (4.7) and Theorem 4.1 that there exist a subsequence $\{j\} \subset\{i\}$, a compact $C^{\infty} n$-manifold $M_{\infty}$ with $C^{\alpha} \cap L^{2, p}$ metric $h$ of positive constant scalar curvature $S_{h}$ and a diffeomorphism $\Phi_{j}: M_{\infty} \longrightarrow$ $M_{j}$ for each $j$ such that the following hold.
$$\begin{aligned}
& V_{h}=1, \quad 0<\mu_{0} \leq S_{h} \leq n(n-1) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n} . \\
& h(j)=\left(\Phi_{j}\right)^{*} g_{j} \longrightarrow h \quad(j \longrightarrow \infty)
\end{aligned}$$
in the $C^{\alpha^{\prime}}$ topology for $\alpha^{\prime}<\alpha$ and weakly in the $L^{2, p}$ topology on $M_{\infty}$.
$$\lim _{j \rightarrow \infty} S_{g_{j}}=S_{h} \equiv \text { const.. }$$
Using (4.7) in (4.1) of Theorem 4.1 then gives the following estimate for $L^{2, p}$ harmonic radius of each $h(j)$
$$r_{H}(x ; h(j)) \geq r_{0}>0 \quad \text { for } \quad x \in M_{\infty},$$
where $r_{0}=r_{0}\left(n, p, \mu_{0}\right)$. From (4.9) and (4.11), we can cover $M_{\infty}$ by a finite collection of geodesic balls $\left\{B_{\frac{r_{0}}{2}}\left(y_{k} ; h\right) ; y_{k} \in M_{\infty}\right\}_{k=1}^{l}$ with respect to $h$. It then follows from (4.11) and Remark 3.3 that there exist harmonic coordinates
$$\begin{aligned}
U_{j, k}=\left\{u^{a}\right\}_{a=1}^{n}\left(=\left\{u(j)^{a}\right\}_{a=1}^{n}\right): B_{r_{0}}\left(y_{k} ; h(j)\right)\left(\subset M_{\infty}\right) & \longrightarrow \mathbf{R}^{n} \\
& \text { with } U_{j, k}\left(y_{k}\right)=\mathbf{0} \in \mathbf{R}^{n}
\end{aligned}$$
and a coordinate system $\left\{V_{\lambda}\right\}_{\lambda=1}^{m}$ of class $C^{\infty}$ on $M_{\infty}$ such that the metric components $h(j)_{a b}=h(j)\left(\partial / \partial u^{a}, \partial / \partial u^{b}\right)$ satisfy (3.1) and (3.2) on $\tilde{B}_{j, k}=$ $U_{j, k}\left(B_{r_{0}}\left(y_{k} ; h(j)\right)\right)$, and that
$$\left\|U_{j, k} \circ V_{\lambda}^{-1}\right\|_{L^{4, p}} \leq C, \quad\left\|U_{j, k} \circ V_{\lambda}^{-1}\right\|_{C^{2, \alpha}} \leq C$$
where $C$ is independent of $j$ and $k$. From (4.12), taking a subsequence if necessary, we may assume that there exists a coordinate system $\left\{U_{\infty, k}\right\}_{k=1}^{l}$ of class $C^{2, \alpha} \cap L^{4, p}$ such that, for each $k, U_{j, k}$ converges to $U_{\infty, k}$ in the $C^{2, \alpha^{\prime}}$ topology for $\alpha^{\prime}<\alpha$ and weakly in the $L^{4, p}$ topology. We also assume that a collection of geodesic balls $\left\{B_{r_{0}}\left(y_{k} ; h(j)\right)\right\}_{k=1}^{l}$ covers $M_{\infty}$ and that $U_{j, k}\left(B_{r_{0}}\left(y_{k} ; h(j)\right)\right) \supset \tilde{B}_{\infty, k}(1 / 2)$ for all $j$ and $k$, where $\tilde{B}_{\infty, k}(1 / 2)=$ $U_{\infty, k}\left(B_{\frac{r_{0}}{2}}\left(y_{k} ; h\right)\right)$.

On the other hand, from (4.5) we obtain
$$\begin{aligned}
& \int_{M_{\infty}}\left|\widehat{\operatorname{Ric}}_{h(j)}\right|^{p} d v_{h(j)}=\int_{M}\left|\widehat{\operatorname{Ric}}_{g_{j}}\right|^{p} d v_{g_{j}} \\
& \leq\left(\frac{n-2}{4}\right)^{p / 2} \int_{M_{j}}\left|Z_{g_{j}}\right|^{p} d v_{g_{j}} \longrightarrow 0 \quad(j \longrightarrow 0),
\end{aligned}$$
where $\widehat{\operatorname{Ric}}_{g}$ denotes the traceless part of $\operatorname{Ric}_{g}$, i.e., $\widehat{\operatorname{Ric}}_{g}=\operatorname{Ric}_{g}-\frac{S_{g}}{n} \cdot g$. In each harmonic coordinates $U_{j, k}$, by using (3.1) in (4.13), then the components $\widehat{R(j)}_{a b}$ of $\widehat{\operatorname{Ric}}_{h(j)}$ converge to 0 strongly in the $L^{p}$ topology on $\tilde{B}_{\infty, k}(1 / 2)$. Combining (4.9) with this fact, we obtain
$$R(j)_{a b} \longrightarrow \frac{S_{h}}{n} \cdot h_{a b} \quad \text { strongly in } \quad L^{p}\left(\tilde{B}_{\infty, k}(1 / 2)\right),$$
where $R(j)_{a b}$ denote the components of $\operatorname{Ric}_{h(j)}$. In terms of this harmonic coordinates, $R(j)_{a b}$ are expressed as follows (cf. [J, DK]).
$$h(j)^{c d} \frac{\partial^{2} h(j)_{a b}}{\partial u^{c} \partial u^{d}}+Q_{a b}(\partial h(j))=-2 R(j)_{a b} \quad \text { on } \quad \tilde{B}_{j, k},$$
where $Q$ is a quadratic term in the first derivatives $\partial h(j)$ of $h(j)$. It then follows from (4.9), (4.14) and (4.15) that the metric $h$ in terms of the coordinates $\left\{U_{\infty, k}\right\}_{k=1}^{l}$ is a weak $C^{\alpha} \cap L^{2, p}$ solution to the following equation
$$h^{c d} \frac{\partial^{2} h_{a b}}{\partial u^{c} \partial u^{d}}+Q_{a b}(\partial h)=-\frac{2}{n} S_{h} \cdot h_{a b} \quad \text { on } \quad \tilde{B}_{\infty, k}(1 / 2) .$$
Applying the elliptic regularity theory (cf. [Gi, GT]) to the equation (4.16), we obtain that $h$ is an Einstein metric of class $C^{\infty}$ on $M_{\infty}$, and then $\left\{U_{\infty, k}\right\}_{k=1}^{l}$ is a harmonic coordinate system of class $C^{\infty}$ compatible with $\left\{V_{\lambda}\right\}_{\lambda=1}^{m}$. From (4.5), we also obtain that $h$ is a positive constant curvature metric on $M_{\infty}$. Here we remark that an Einstein metric is a Yamabe metric (cf. [O, S3]). Combining (4.8) and (4.10) with these facts then contradict our assumption.

Since there exists a $C^{\infty}$ metric $h$ of positive constant curvature on $M$ satisfying (4.2), then from (2.1) we have
$$\mu_{0} \leq \mu(M,[h])=n(n-1)\left(\frac{\operatorname{vol}\left(S^{n}(1)\right)}{\#\left(\pi_{1}(M)\right)}\right)^{2 / n} .$$
This completes the proof of Corollary 4.2. \(\square\)

Proof of Theorem 1.3. Our assertion will be also done by contradiction. If the assertion does not hold, then there exist sequences $\left\{\varepsilon_{i}\right\}_{i \in \mathrm{~N}}$ of positive constants and $\left\{\left(M_{i}, g_{i}\right)\right\}_{i \in \mathbf{N}} \subset \mathcal{Y}_{1}\left(n, \mu_{0}\right)$ of compact Riemannian $n$-manifolds satisfying $\varepsilon_{1}>\varepsilon_{2}>\cdots \longrightarrow 0$ and
$$\int_{M_{i}}\left|R_{g_{i}}\right|^{p} d v_{g_{i}} \leq \Lambda, \quad \int_{M_{i}}\left|\nabla A_{g_{i}}\right|^{s} d v_{g_{i}} \leq \varepsilon_{i}$$
for all $i \in \mathbf{N}$ such that each $M_{i}$ never admits a $C^{\infty}$ metric of harmonic curvature.

Since each $M_{i}$ satisfies the estimate (4.17), we can apply volume estimates of geodesic balls from above due to Yang [Yn3]. Then, there exist positive constants $c_{0}=c_{0}(n)$ and $\rho_{0}=\rho_{0}(n, p, \Lambda)$ such that
$$\operatorname{vol}\left(B_{r}\left(x ; g_{i}\right)\right) \leq c_{0} r^{n} \quad \text { for } \quad r \leq \rho_{0} \quad \text { and } \quad x \in M_{i} .$$

From (4.17), (4.18) and Hölder's inequality, we have
$$\begin{aligned}
& \int_{B_{r}(x)}\left|R_{g_{\imath}}\right|^{n / 2} d v_{g_{\imath}} \\
& \leq\left(\int_{B_{r}(x)}\left|R_{g_{\imath}}\right|^{p} d v_{g_{\imath}}\right)^{n / 2 p} \cdot \operatorname{vol}\left(B_{r}\left(x ; g_{i}\right)\right)^{(2 p-n) / 2 p} \\
& \leq \Lambda^{n / 2 p}\left(c_{0} r^{n}\right)^{(2 p-n) / 2 p} \text { for } r \leq \rho_{0} \text { and } x \in M_{i} .
\end{aligned}$$
Taking $\rho_{1}=\rho_{1}(n, p, \Lambda)$ satisfying $\Lambda^{n / 2 p}\left(c_{0} \rho_{1}^{n}\right)^{(2 p-n) / 2 p} \leq \varepsilon_{0}$ and $\rho_{1} \leq \rho_{0}$, where $\varepsilon_{0}$ is the same constant as in (3.6) with $c_{s}=\frac{n-2}{4(n-1)} \mu_{0}>0$. By Hölder's inequality and $V_{g_{i}}=1$, we may particularly assume that $s<\frac{n}{2}$. It then follows from (2.4), (4.17), (4.19) and Lemma 3.8 that
$$\int_{B_{\frac{\rho_{1}}{2}}(x)}\left|R_{g_{\imath}}\right|^{n s /(n-2 s)} d v_{g_{\imath}} \leq c_{1} \quad \text { for } x \in M_{i}$$
where $c_{1}=c_{1}\left(n, p, s, \mu_{0}, \Lambda\right)$. Here, by (2.5) and $V_{g_{i}}=1$, there exists a finite subset $\left\{x_{a}(i)\right\}_{a=1}^{m_{0}} \subset M_{i}$ for each $i \in \mathbf{N}$ such that $\left\{B_{\frac{\rho_{1}}{2}}\left(x_{a}(i)\right)\right\}_{i=1}^{m_{0}}$ is a covering of $M_{i}$, where $m_{0}=m_{0}\left(n, p, \mu_{0}, \Lambda\right)$. Combining (4.20) with this fact then gives
$$\int_{M_{\imath}}\left|R_{g_{\imath}}\right|^{n s /(n-2 s)} d v_{g_{\imath}} \leq \sum_{a=1}^{m_{0}} \int_{B_{\frac{\rho_{1}}{2}}\left(x_{a}(i)\right)}\left|R_{g_{\imath}}\right|^{n s /(n-2 s)} d v_{g_{\imath}} \leq m_{0} c_{1} \quad \text { for } i \in \mathrm{~N} .$$

Set $p=\frac{n s}{n-2 s}(>2 s)$ and $\alpha=4-\frac{n}{s}(>1)$ in the proof of Corollary 4.2, respectively. From (4.21), Theorem 4.1 and Remark 3.3, the same results as (4.8)-(4.12) and (4.15) hold, and then we will use the same notation as in the proof of Corollary 4.2 except for $p$ and $\alpha$. In terms of each harmonic coordinates $U_{j, k}$, the Ricci curvature $\operatorname{Ric}_{h(j)}$ satisfies the following equation beside (4.15)
$$\begin{aligned}
& h(j)^{c d} \frac{\partial^{2} R(j)_{a b}}{\partial u^{c} \partial u^{d}}+\left(\partial h(j) * \partial \operatorname{Ric}_{h(j)}\right)_{a b} \\
& =\left[\left(\partial \partial h(j)+\partial h(j) * \partial h(j)+\operatorname{Ric}_{h(j)}\right) * \operatorname{Ric}_{h(j)}\right]_{a b} \\
& \quad+h(j)^{c d}\left[\nabla_{c} A(j)_{a d b}-\nabla_{a} A(j)_{c b d}\right] \\
& \left(\equiv T(j)_{a b}\right) \quad \text { on } \tilde{B}_{j, k},
\end{aligned}$$
where $A(j)=A_{h(j)}$. Here we note
$$\left\|h(j)_{a b}\right\|_{L^{2, \frac{n s}{n-2 s}}}\left(\tilde{B}_{j, k}\right) \leq C_{1}, \quad\left\|h(j)_{a b}\right\|_{C^{1,3-\frac{n}{s}}\left(\tilde{B}_{j, k}\right)} \leq C_{1}$$
for all $j, k$ and $a, b=1, \cdots, n$, where $C_{1}$ and $C_{2}, C_{3}$ below are independent of $j$. Combining (4.17), (4.21) and (4.23) with (4.22) then gives
$$\left\|T(j)_{a b}\right\|_{L^{*}\left(\tilde{B}_{j, k}\right)} \leq C_{2}$$
for all $j, k$ and $a, b=1, \cdots, n$. From (4.23), (4.24) and the $L^{p}$ estimate (cf. [GT]) for (4.22), we have for $B \Subset \tilde{B}_{j, k}$
$$\left\|R(j)_{a b}\right\|_{L^{2, g}(B)} \leq C_{3}$$
for all $j, k$ and $a, b=1, \cdots, n$.
From (4.17), (4.23) and (4.25), there exist a $C^{1,3-n / s} \cap L^{2, n s /(n-2 s)}$ metric $h$ and a $L^{2, s}$ symmetric tensor $P$ of type $(0,2)$ on $M_{\infty}$ such that we obtain the following.
$$h(j)_{a b} \longrightarrow h_{a b} \quad(j \longrightarrow \infty)$$
in the $C^{1, \alpha^{\prime}}$ topology for $\alpha^{\prime}<3-\frac{n}{s}$ and weakly in the $L^{2, n s /(n-2 s)}$ topology on $\tilde{B}_{\infty, k}(1 / 2)$.
$$R(j)_{a b} \longrightarrow P_{a b} \quad(j \longrightarrow \infty)$$
weakly in the $L^{2, s}$ topology on $\tilde{B}_{\infty, k}(1 / 2)$, where $P_{a b}$ denote the components of $P$.
$$\nabla_{a} A(j)_{b c d} \longrightarrow 0 \quad \text { strongly in } \quad L^{s}\left(\tilde{B}_{\infty, k}(1 / 2)\right) .$$

It then follows from (4.12), (4.15), (4.22) and (4.26)-(4.28) that, in terms of the $C^{3,3-n / s} \cap L^{4, n s /(n-2 s)}$ coordinates $\left\{U_{\infty, k}\right\}_{k=1}^{l}, h$ is a weak $C^{1,3-n / s} \cap$ $L^{2, n s /(n-2 s)}$ solution and $P$ a weak $L^{2, s}$ solution to the following equations, on each $\tilde{B}_{\infty, k}(1 / 2)$
$$\begin{aligned}
h^{c d} \frac{\partial^{2} h_{a b}}{\partial u^{c} \partial u^{d}}+Q_{a b}(\partial h) & =-2 P_{a b}, \\
h^{c d} \frac{\partial^{2} P_{a b}}{\partial u^{c} \partial u^{d}}+(\partial h * \partial P)_{a b} & =[(\partial \partial h+\partial h * \partial h+P) * P]_{a b} .
\end{aligned}$$
Applying the elliptic regularity theory (cf. [Gi, GT]) to the equations (4.29) and (4.30), we obtain that $h$ is a $C^{\infty}$ metric of $S_{h} \equiv$ const. on $M_{\infty}$, and then $P=\operatorname{Ric}_{h},\left\{U_{\infty, k}\right\}_{k=1}^{l}$ is a harmonic coordinate system of class $C^{\infty}$ compatible with $\left\{V_{\lambda}\right\}_{\lambda=1}^{m}$. From (4.28) we also note that $\nabla A_{h} \equiv 0$. By the definition of $A_{h}$, we then obtain
$$\int_{M_{\infty}}\left|A_{h}\right|^{2} d v_{h} \leq 2 \int_{M_{\infty}}\left|\operatorname{Ric}_{h}\right| \cdot\left|\nabla A_{h}\right| d v_{h}=0 .$$

From (4.31) we have $A_{h} \equiv 0$, i.e., $h$ is of harmonic curvature. Since a sequence of Yamabe metrics $h(j)=\left(\Phi_{j}\right)^{*} g_{j}$ converges to the $C^{\infty}$ metric $h$ in the $C^{1, \alpha^{\prime}}$ topology for $\alpha^{\prime}<3-\frac{s}{n}$ and weakly in the $L^{2, n s /(n-2 s)}$ topology on $M_{\infty}$, then $h$ is also a Yamabe metric on $M_{\infty}$. In fact, unless $h$ is a Yamabe metric, one can show that $h(j)$ is not a Yamabe metric for $j$ sufficiently large. Combining this fact with the following
$$V_{h}=1, \quad \mu\left(M_{\infty},[h]\right) \geq \mu_{0}>0,$$
it then contradicts our assumption.
When $n=3, A_{h} \equiv 0$ implies that ( $M^{3}, h$ ) is conformally flat. Now the compact 3-manifold $M^{3}$ admits a conformally flat metric $h$ of positive scalar curvature. Then, by Izeki's theorem [I], the rest assertion is immediate. This completes the proof of Theorem 1.3. \(\square\)

\section*{5. Proof of Theorem 1.1.}

In this section we shall prove Theorem 1.1.
By Theorem 2.3, if the first case (1°) in Theorem 1.1 does not hold, then there exist subsequence $\{j\} \subset\{i\}$ and a connected compact metric space $\left(M_{\infty}, d_{\infty}\right)$ with $\operatorname{diam}\left(M_{\infty}, d_{\infty}\right)=D_{0}>0$ such that
$$\lim _{j \rightarrow \infty} d_{H}\left(\left(M_{j}, g_{j}\right),\left(M_{\infty}, d_{\infty}\right)\right)=0$$
Taking a subsequence if necessary, we may assume that
$$\operatorname{diam}\left(M_{j}, g_{j}\right) \geq \frac{1}{2} D_{0}>0$$
for all $j$ and that there exists a $(1 / j)$-Hausdorff approximation
$$\varphi_{j}:\left(M_{j}, g_{j}\right) \longrightarrow\left(M_{\infty}, d_{\infty}\right)$$
for each $j$. For each $y \in M_{\infty}$, we can find $y_{j} \in M_{j}$ such that
$$d_{\infty}\left(y, \varphi_{j}\left(y_{j}\right)\right)<\frac{1}{j} .$$
We define the singular set $\mathcal{S}$ by
$$\begin{aligned}
\mathcal{S}=\bigcap_{0<r<D_{0}}\left\{y \in M_{\infty} ; \liminf _{j \rightarrow \infty} \int_{B_{2 r}\left(y_{j}\right)}\left|R_{g_{j}}\right|^{n / 2} d v_{g_{j}} \geq \varepsilon_{0}\right. & \\
& \text { for arbitrary } \left.\left\{y_{j}\right\}_{j \in \mathbb{N}} \text { as above }\right\},
\end{aligned}$$
where $\varepsilon_{0}=\varepsilon_{0}\left(n, q, \mu_{0}\right)$ denotes a constant similar to $\varepsilon_{0}$ in Proposition 3.9.
To prove Theorem 1.1, we first note the following.
Lemma 5.1. $\mathcal{S}$ is a finite set.
Proof. Take a small constant $r>0$ and fix it. Then we can cover $\mathcal{S}$ by a finite collection of metric balls $\left\{B_{2 r}\left(x_{a}\right) ; x_{a} \in \mathcal{S}\right\}_{a \in \Gamma}$ with respect to $d_{\infty}$ such that the collection $\left\{B_{r}\left(x_{a}\right)\right\}_{a \in \Gamma}$ is disjoint. Since $x_{a} \in \mathcal{S}$, for $j$ sufficiently large there exists a point $x_{a, j} \in M_{j}$ such that
$$\begin{aligned}
\int_{B_{\frac{r}{2}}\left(x_{a, j}\right)}\left|R_{g_{j}}\right|^{n / 2} d v_{g_{j}} \geq \frac{\varepsilon_{0}}{2}, & \\
d_{\infty}\left(x_{a}, \varphi_{j}\left(x_{a, j}\right)\right)<\frac{1}{j} & \text { for } a \in \Gamma, \\
B_{\frac{r}{2}}\left(x_{a, j}\right) \cap B_{\frac{r}{2}}\left(x_{b, j}\right)=\phi & \text { for } a \neq b .
\end{aligned}$$
It follows from (5.2)-(5.4) that
$$\begin{aligned}
\#(\Gamma) & \leq 2 \varepsilon_{0}^{-1} \sum_{a \in \Gamma} \int_{B_{\frac{\Gamma}{2}}\left(x_{a, j}\right)}\left|R_{g_{j}}\right|^{n / 2} d v_{g_{j}} \\
& \leq 2 \varepsilon_{0}^{-1} \int_{M_{j}}\left|R_{g_{j}}\right|^{n / 2} d v_{g_{j}} \leq 2 \Lambda_{1} \varepsilon_{0}^{-1} .
\end{aligned}$$
Since $2 \Lambda_{1} \varepsilon_{0}^{-1}$ is independent of $r$, letting $r \rightarrow 0$ in (5.5), we then obtain
$$\#(\mathcal{S}) \leq 2 \Lambda_{1} \varepsilon_{0}^{-1} .$$
This completes the proof of Lemma 5.1. \(\square\)

Next we give a proof of (2°.2) - (2°.4). Fix a point $y \in M_{\infty} \backslash \mathcal{S}$.
Lemma 5.2. There exist $r$ satisfying $0<r \leq \frac{1}{4} d_{\infty}(y, \mathcal{S})$, a point $y_{j} \in M_{j}$ for each $j$ and a positive constant $r_{0}=r_{0}\left(n, q, \mu_{0}, \Lambda_{2}, r\right)$ such that
$$\gamma_{H}(x) \geq r_{0}>0 \quad \text { for } \quad x \in B_{r}\left(y_{j}\right) \subset M_{j},$$
where $\gamma_{H}(x)=\min \left\{r_{H}(x), \operatorname{dist}_{g_{j}}\left(x, \partial B_{r}\left(y_{j}\right)\right)\right\}$ and $r_{H}(x)$ denotes the $L^{2, n q /(n-2 q)}$ harmonic radius at $x$.

Proof. Taking a subsequence if necessary, we can find $r$ satisfying $0<r \leq$ $\frac{1}{4} d_{\infty}(y, \mathcal{S})$ and $y_{j} \in M_{j}$ for each $j$ such that $d_{\infty}\left(y, \varphi_{j}\left(y_{j}\right)\right)<\frac{1}{j}$ and
$$\int_{B_{2 r}\left(y_{j}\right)}\left|R_{g_{j}}\right|^{n / 2} d v_{g_{j}} \leq \varepsilon_{0} \quad \text { for all } j .$$

Using (2.4), (5.7) and $\int_{M_{3}}\left|\nabla A_{g_{3}}\right|^{q} d v_{g_{3}} \leq \Lambda_{2}$ in Proposition 3.9, then gives
$$\gamma_{H}(x) \geq c_{0} \cdot \nu^{\delta}(x) \quad \text { for } \quad x \in B_{r}\left(y_{j}\right) \quad \text { and all } j,$$
where $c_{0}=c_{0}\left(n, q, \mu_{0}, \delta, \Lambda_{2}, C\right)$ and $\nu^{\delta}(x)=\min \left\{v^{\delta}(x), \operatorname{dist}_{g_{j}}\left(x, \partial B_{r}\left(y_{j}\right)\right)\right\}$. Now set $\delta=\left(5 \cdot 2^{n-2}\right)^{-n / 2}\left(\frac{n-2}{4(n-1)}\right)^{n / 2} \mu_{0}^{n / 2}>0$. It then follows from (2.5) and (5.8) that
$$\gamma_{H}(x) \geq r_{0}>0 \quad \text { for } \quad x \in B_{r}\left(y_{j}\right) \quad \text { and all } j .$$
This completes the proof of Lemma 5.2. \(\square\)

By (5.6), for each $j$ there exist harmonic coordinates $U_{j}: B_{r_{0}}\left(y_{j}\right) \longrightarrow \mathbf{R}^{n}$ with $U_{j}\left(B_{r_{0}}\left(y_{j}\right)\right) \supset B_{2 \rho}=\left\{x \in \mathbf{R}^{n} ;|x|<2 \rho\right\}$ for some $\rho>0$ independent of $j$, such that the metric components of $g_{j}$ satisfy (3.1) and (3.2) for $p=\frac{n q}{n-2 q}$ and $\alpha=4-\frac{n}{q}(=\beta>0)$. Now $\left.\varphi_{j} \circ U_{j}^{-1}\right|_{B_{\rho}}$ is a $\left(\frac{1}{j}\right)$-Hausdorff approximation from $\left(B_{p}, \gamma_{j}\right)$ to a neighborhood of $y$ in $M_{\infty}$ equipped with $d_{\infty}$, where $\gamma_{j}=$ $\left(U_{j}^{-1}\right)^{*} g_{j}$. From (3.1) and (3.2), taking a subsequence if necessary, there exists a $C^{\beta} \cap L^{2, n q /(n-2 q)}$ metric $\gamma_{y, \infty}$ on $B_{\rho}$ such that $\left.\varphi_{j} \circ U_{j}^{-1}\right|_{B_{\rho}}$ converges to an isometry $H_{y}:\left(B_{\rho}, \gamma_{y, \infty}\right) \longrightarrow\left(O_{y}, d_{\infty}\right)$, where $O_{y}$ is also a neighborhood of $y$. Moreover, for any $y, z \in M_{\infty} \backslash \mathcal{S}, H_{z}^{-1} \circ H_{y}:\left(H_{y}^{-1}\left(O_{y} \cap O_{z}\right), \gamma_{y, \infty}\right) \longrightarrow$ $\left(H_{z}^{-1}\left(O_{y} \cap O_{z}\right), \gamma_{z, \infty}\right)$ is also an isometry unless $O_{y} \cap O_{z}=\phi$. Since each metric $\gamma_{y, \infty}$ is of class $C^{\beta}$, then $H_{z}^{-1} \circ H_{y}$ is of class $C^{1, \beta}$ unless $O_{y} \cap O_{z}=\phi$ (cf. [CH]). By Whitney's theorem, there exists a unique $C^{\infty}$ structure on $M_{\infty} \backslash \mathcal{S}$ compatible with the $C^{1, \beta}$ structure $\left\{\left(H_{y}^{-1}, O_{y}\right)\right\}_{y \in M_{\infty} \backslash \mathcal{S}}$. Thus $\left\{\gamma_{y, \infty}\right\}_{y \in M_{\infty} \backslash \mathcal{S}}$ also gives a $C^{\beta}$ metric $g_{\infty}$ on $M_{\infty} \backslash \mathcal{S}$ compatible with $d_{\infty}$.

For each $x_{a} \in \mathcal{S}=\left\{x_{1}, \cdots, x_{k}\right\}$, let $\left\{x_{a, j}\right\}_{j \in \mathrm{~N}}$ be points same as in the proof of Lemma 5.1. For each $m \in \mathbf{N}$, define the open subsets $D_{j}\left(2^{-m}\right)$ in $M_{y}$ and $D_{\infty}\left(2^{-m}\right)$ in $M_{\infty}$ by
$$D_{j}\left(2^{-m}\right)=\left\{x \in M_{j} ; \operatorname{dist}_{g_{j}}\left(x, x_{a, j}\right)>2^{-m} \quad \text { for } \quad a=1, \cdots, k\right\}$$
and
$$D_{\infty}\left(2^{-m}\right)=\left\{x \in M_{\infty} ; d_{\infty}(x, \mathcal{S})>2^{-m}\right\},$$
respectively. From (5.1) and (5.6), each $D_{j}\left(2^{-m}\right)$ is nonempty for $m$ sufficiently large. Also from (3.1), (5.6) and $V_{g_{j}}=1$, we have for all $j$
$$0<c_{1} \leq \operatorname{vol}\left(D_{j}\left(2^{-m}\right), g_{j}\right) \leq 1$$
for some constant $c_{1}=c_{1}(m)$ independent of $j$. Replace $\Omega_{i}$ and $\varepsilon$ in Theorem 3.4 by $D_{j}\left(2^{-m-1}\right)$ and $2^{-m-1}$ respectively. It then follows from (5.6), (5.9) and Theorem 3.4 that, for each $m$, there exist a subsequence $\left\{j_{m}\right\} \subset\{j\}$, a
$C^{\infty} n$-manifold $\mathcal{D}_{\infty}^{m}$ with $C^{\beta} \cap L^{n q /(n-2 q)}$ metric $g_{\infty}^{m}$ and an into diffeomorphism $F_{j_{m}}: \mathcal{D}_{\infty}^{m} \longrightarrow D_{j_{m}}\left(3 \cdot 2^{-m-2}\right)$ with $F_{j_{m}}\left(\mathcal{D}_{\infty}^{m}\right) \supset D_{j_{m}}\left(5 \cdot 2^{-m-2}\right)$ for each $j_{m}$ such that $\left(F_{j_{m}}\right)^{*} g_{j_{m}}$ converges to $g_{\infty}^{m}$ in the $C^{\beta^{\prime}}$ topology for $\beta^{\prime}<\beta$ and weakly in the $L^{2, n q /(n-2 q)}$ topology on $\mathcal{D}_{\infty}^{m}$. Moreover we assume that $\left\{j_{m+1}\right\} \subset\left\{j_{m}\right\}$ for all $m$.

Now we remark that $\varphi_{j_{m}} \circ F_{j_{m}}: \mathcal{D}_{\infty}^{m} \longrightarrow M_{\infty}$ converges to an into isometry $G^{m}:\left(\mathcal{D}_{\infty}^{m}, g_{\infty}^{m}\right) \longrightarrow\left(D_{\infty}\left(3 \cdot 2^{-m-2}\right), g_{\infty}\right)$ with $G^{m}\left(\mathcal{D}_{\infty}^{m}\right) \supset D_{\infty}\left(5 \cdot 2^{-m-2}\right)$ for each $m$. Take the diagonal sequence $\left\{j_{j}\right\}$ of $\left\{j_{m}\right\}_{j, m \in \mathbf{N}}$. We shall rewrite the index " $j_{j}$ " by " $j$ " again. Then we obtain that, for each $m$, there exists an into diffeomorphism $\Phi_{j}^{m}=\left.F_{j} \circ\left(G^{m}\right)^{-1}\right|_{D_{\infty}\left(5 \cdot 2^{-m-2}\right)}: D_{\infty}\left(5 \cdot 2^{-m-2}\right) \longrightarrow M_{j}$ for $j$ sufficiently large such that $\left(\Phi_{j}^{m}\right)^{*} g_{j}$ converges to $g_{\infty}$ in the $C^{\beta^{\prime}}$ topology for $\beta^{\prime}<\beta$ and weakly in the $L^{2, n q /(n-2 q)}$ topology on $D_{\infty}\left(5 \cdot 2^{-m-2}\right)$. We also note that $g_{\infty}$ is a $L_{\text {loc }}^{2, n q /(n-2 q)}$ metric on $M_{\infty} \backslash \mathcal{S}$. Moreover, taking a subsequence if necessary, we may assume that
$$\lim _{j \rightarrow \infty} S_{g_{j}}=S_{g_{\infty}} \equiv \text { const., }$$
then we obtain
$$0<\mu_{0} \leq S_{g_{\infty}} \leq n(n-1) \operatorname{vol}\left(S^{n}(1)\right)^{2 / n} .$$
For a compact subset $K \subset M_{\infty} \backslash \mathcal{S}$, there exists $m \in \mathbf{N}$ such that $K \subset$ $D_{\infty}\left(5 \cdot 2^{-m-2}\right)$. Thus we can take $\Phi_{j}=\left.\Phi_{j}^{m}\right|_{K}$ as in (2°.3).

Finally we give a proof of (2°.5) and (2°.6). Fix a point $x_{a} \in \mathcal{S}$. There exists $x_{a, j} \in M_{j}$ such that $d_{\infty}\left(\varphi_{j}\left(x_{a, j}\right), x_{a}\right)<\frac{1}{j}$. Since $\mathcal{S}$ is a finite set, we can take $\rho>0$ so that $\left(B_{2 \rho}\left(x_{a}\right) \backslash\left\{x_{a}\right\}\right) \cap \mathcal{S}=\phi$. For each $j$, we define the positive number $r_{j}$ in (2°.5) by
$$r_{j}=\sup _{B_{\rho}\left(x_{a, j}\right)}\left|R_{g_{j}}\right| .$$
By the definition of $\mathcal{S}$,
$$r_{j} \longrightarrow \infty \quad(j \longrightarrow \infty) .$$
Moreover we may assume that $\left|R_{g_{j}}\right|$ takes a local maximum value $r_{j}$ at $x_{a, j}$. We consider the new sequence of pointed Riemannian manifolds ( $\left(M_{j}, \tilde{g}_{j}\right)$, $x_{a, j}$ ), where $\tilde{g}_{j}=r_{j} g_{j}$. From (2.1), (2.2), (2.5), (5.1), (5.10) and the condi-
tions in Theorem 1.1, this sequence satisfies:
$$\sup _{\sqrt{r_{j} \cdot p}\left(x_{a, j} ; \tilde{g}_{j}\right)}\left|R_{\tilde{g}_{j}}\right|=1, \quad\left|R_{\tilde{g}_{j}}\right|\left(x_{a, j}\right)=1,$$
$$\operatorname{diam}\left(M_{j}, \tilde{g}_{j}\right)=\sqrt{r_{j}} \operatorname{diam}\left(M_{j}, g_{j}\right) \longrightarrow \infty \quad(j \longrightarrow \infty),$$
$$V_{\tilde{g}_{j}}=r_{j}^{n / 2} V_{g_{j}}=r_{j}^{n / 2} \longrightarrow \infty \quad(j \longrightarrow \infty),$$
$$S_{\tilde{g}_{j}}=r_{j}^{-1} S_{g_{j}}=r_{j}^{-1} \mu\left(M_{j},\left[g_{j}\right]\right) \longrightarrow 0 \quad(j \longrightarrow \infty),$$
$$\begin{aligned}
& \int_{B_{\sqrt{r_{j} \cdot \rho}}\left(x_{a, j} ; \tilde{g}_{\jmath}\right)}\left|R_{\tilde{g}_{j}}\right|^{n / 2} d v_{\tilde{g}_{j}}=\int_{B_{\rho}\left(x_{a, j} ; g_{\jmath}\right)}\left|R_{g_{j}}\right|^{n / 2} d v_{g_{j}} \leq \Lambda_{1}, \\
& \int_{B_{\sqrt{r_{j}} \cdot \rho}\left(x_{a, j} ; \tilde{g}_{\jmath}\right)}\left|\nabla A_{\tilde{g}_{j}}\right|^{q} d v_{\tilde{g}_{j}}
\end{aligned}$$
$$=r_{j}^{-2 q+n / 2} \int_{B_{\rho}\left(x_{a, j} ; g_{j}\right)}\left|\nabla A_{g_{j}}\right|^{q} d v_{g_{j}} \longrightarrow 0 \quad(j \longrightarrow \infty),$$
$$\operatorname{vol}\left(B_{r}(x) ; \tilde{g}_{j}\right) \geq\left(5 \cdot 2^{n}(n-1)\right)^{-n / 2}(n-2)^{n / 2} \mu_{0}^{n / 2} r^{n}$$
for $x \in B_{c_{2} \sqrt{r_{j}}}\left(x_{a, j} ; \tilde{g}_{j}\right)$, where $c_{2}=c_{2}(n)>0$. By using (5.11) and (5.17) in Theorem 5.3 below due to Cheeger-Gromov-Taylor [CGT], then for any $R>0$, there exists $j_{R} \in \mathrm{~N}$ and $r_{0}(>0)$ such that
$$\operatorname{inj}_{\left(M_{,}, \tilde{g}_{j}\right)}(x) \geq r_{0}>0 \quad \text { for } \quad x \in B_{R}\left(x_{a, j} ; \tilde{g}_{j}\right), \quad j \geq j_{R} .$$

Theorem 5.3. Let $B_{r}(x)$ be a metric ball of radius $r$ in a Riemannian manifold $(M, g)$ such that for $r^{\prime}<r, \overline{B_{r^{\prime}}(x)}$ is compact. Assume that on $B_{r}(x), \omega \leq K_{g} \leq \kappa$ and $r \leq \frac{\pi}{\sqrt{\kappa}}$ ( $r$ arbitrary if $\kappa \leq 0$ ) for some constants $\omega, \kappa$. Let $B_{r}^{\omega}$ be a geodesic ball of radius $r$ in the simply-connected space form of constant curvature $\omega$. Then, for positive constants $r_{0}$ and $s$ with $r_{0}+2 s \leq r$ and $r_{0} \leq \frac{r}{4}$, the following inequality holds
$$\operatorname{inj}_{(M, g)}(x) \geq \frac{r_{0}}{2} \cdot \frac{1}{1+\operatorname{vol}\left(B_{r_{0}+s}^{\omega}\right) / \operatorname{vol}\left(B_{s}(x)\right)} .$$

It then follows from (5.11), (5.12), (5.18) and Theorem 3.5 that there exists a noncompact complete $C^{\infty}$ pointed $n$-manifold $\left(N_{a}, x_{a, \infty}\right)$ with $C^{1, \sigma}(0<$
$\sigma<1)$ metric $h_{a}$ such that, taking a subsequence if necessary, $\left(\left(M_{j}, \tilde{g}_{j}\right), x_{a, j}\right)$ converges to $\left(\left(N_{a}, h_{a}\right), x_{a, \infty}\right)$ in the pointed Hausdorff distance. Moreover, for each $r>0$ there exists an into diffeomorphism $\Psi_{j}: B_{r}\left(x_{a, \infty}\right)\left(\subset N_{a}\right) \longrightarrow$ $M_{j}$ with $x_{a, j} \in \Psi_{j}\left(B_{r}\left(x_{a, \infty}\right)\right)$ for $j$ sufficiently large such that $\left(\Psi_{j}\right)^{*} \tilde{g}_{j}$ converges to $h_{a}$ in the $C^{1, \sigma}$ topology on $B_{r}\left(x_{a, \infty}\right)$ and that $\lim _{j \rightarrow \infty} \Psi_{j}^{-1}\left(x_{a, j}\right)=x_{a, \infty}$.

On the other hand, by using (5.10), (5.11), (5.17) and the Bishop comparison theorem [BC, Corollary 4, p. 245] in Theorem 3.7, then for any $s(>n)$ satisfying $1-\frac{n}{s}>\sigma$ there exists $r_{1}(>0)$ such that
$$r_{H}(x) \geq r_{1}>0 \quad \text { for } \quad x \in B_{\frac{1}{2} \sqrt{r_{j} \cdot \rho}}\left(x_{a, j} ; \tilde{g}_{j}\right),$$
where $r_{H}(x)$ denotes the $L^{2, s}$ harmonic radius at $x \in M_{j}$. In terms of each harmonic coordinates in $\Psi_{j}^{-1}\left(B_{\frac{1}{2} \sqrt{r_{j}} \cdot \rho}\left(x_{a, j} ; \tilde{g}_{j}\right)\right)$, by (5.11), (5.16), the $L^{p}$ estimates and the Sobolev inequality (cf. [GT]), then the components $\tilde{h}(j)_{k l}$ of $\tilde{h}_{j}=\left(\Psi_{j}\right)^{*} \tilde{g}_{j}, \tilde{R}(j)_{k l}$ of $\operatorname{Ric}_{\tilde{h}_{j}}$ and $\nabla_{b} \tilde{A}(j)_{c k l}$ of $\nabla A_{\tilde{h}_{j}}$ satisfy
$$\begin{aligned}
\left\|\tilde{h}(j)_{k l}\right\|_{L^{2, s}} & \leq C, \quad\left\|\tilde{h}(j)_{k l}\right\|_{C^{1,1-n / s}} \leq C, \\
\left\|\tilde{R}(j)_{k l}\right\|_{L^{2, q}} & \leq C, \\
\left\|\nabla_{b} \tilde{A}(j)_{c k l}\right\|_{L^{q}} & \leq C,
\end{aligned}$$
where $C$ is independent of $j$. From (5.16) and (5.19)-(5.21), there exists a $L^{2, q}$ symmetric tensor $P$ of type $(0,2)$ on $N_{a}$ such that we obtain the following.
$$\tilde{h}(j)_{k l} \longrightarrow\left(h_{a}\right)_{k l} \quad(j \longrightarrow \infty)$$
in the $C^{1, \sigma}$ topology for $\sigma<1-\frac{n}{s}$ and weakly in the $L^{2, s}$ topology, where $\left(h_{a}\right)_{k l}$ denote the components of $h_{a}$.
$$\tilde{R}(j)_{k l} \longrightarrow P_{k l} \quad(j \longrightarrow \infty)$$
weakly in the $L^{2, q}$ topology.
$$\nabla_{b} \tilde{A}(j)_{c k l} \longrightarrow 0 \quad(j \longrightarrow \infty)$$
strongly in the $L^{q}$ topology. It then follows from (5.22)-(5.24) that $h_{a}$ is a weak $C^{1,1-n / s} \cap L^{2, s}$ solution and $P$ a weak $L^{2, q}$ solution to the following
equations
$$\left(h_{a}\right)^{b c} \frac{\partial^{2}\left(h_{a}\right)_{k l}}{\partial u^{b} \partial u^{c}}+Q_{k l}\left(\partial\left(h_{a}\right)\right)=-2 P_{k l},$$
$$\left(h_{a}\right)^{b c} \frac{\partial^{2} P_{k l}}{\partial u^{b} \partial u^{c}}+\left(\partial\left(h_{a}\right) * \partial P\right)_{k l}=\left[\left(\partial \partial\left(h_{a}\right)+\partial\left(h_{a}\right) * \partial\left(h_{a}\right)+P\right) * P\right]_{k l} .$$
Applying the elliptic regularity theory (cf. [Gi, GT]) to the equations (5.25) and (5.26), we obtain $h_{a}$ is a $C^{\infty}$ metric on $N_{a}$, and then $P=\operatorname{Ric}_{h_{a}}$. From (5.10), (5.11), (5.14), (5.15) and (5.17), we also note that $S_{h_{\mathrm{a}}} \equiv 0$ and
$$\begin{aligned}
& \sup _{N_{a}}\left|R_{h_{a}}\right|=1, \quad 0<\int_{N_{a}}\left|R_{h_{a}}\right|^{n / 2} d v_{h_{a}} \leq \Lambda_{1}, \\
& \operatorname{vol}\left(B_{r}(x) ; h_{a}\right) \geq\left(5 \cdot 2^{n}(n-1)\right)^{-n / 2}(n-2)^{n / 2} \mu_{0}^{n / 2} r^{n}
\end{aligned}$$
for $x \in N_{a}$ and $r>0$.
From the definition of $A_{\tilde{g}_{j}}$ and Hölder's inequality, we note
$$\begin{aligned}
\int_{M_{j}}\left|A_{\tilde{g}_{j}}\right|^{2} d v_{\tilde{g}_{j}} & \leq 2 \int_{M_{j}}\left|\operatorname{Ric}_{\tilde{g}_{j}}\right| \cdot\left|\nabla A_{\tilde{g}_{j}}\right| d v_{\tilde{g}_{j}} \\
& \leq 2\left(\int_{M_{j}}\left|\operatorname{Ric}_{\tilde{g}_{j}}\right|^{q /(q-1)} d v_{\tilde{g}_{j}}\right)^{(q-1) / q}\left(\int_{M_{j}}\left|\nabla A_{\tilde{g}_{j}}\right|^{q} d v_{\tilde{g}_{j}}\right)^{1 / q} .
\end{aligned}$$
By using Hölder's inequality and $V_{g_{j}}=1$ in $\int_{M_{j}}\left|A_{g_{j}}\right|^{q} d v_{g_{j}} \leq \Lambda_{2}$ and $q>$ $\max \left\{1, \frac{n}{4}\right\}$, we may assume that
$$\frac{q}{q-1} \geq \frac{n}{2} \quad \text { when } \quad n \leq 5 .$$
From (5.11), (5.15), (5.16), (5.27) and (5.28), we then obtain for $n \leq 5$
$$\begin{aligned}
\int_{M_{j}}\left|A_{\tilde{g}_{j}}\right|^{2} d v_{\tilde{g}_{j}} \leq 2 & \left(\int_{M_{j}}\left|\operatorname{Ric}_{\tilde{g}_{j}}\right|^{n / 2} d v_{\tilde{g}_{j}}\right)^{(q-1) / q} \\
& \cdot r_{j}^{-2+n / 2 q}\left(\int_{M_{j}}\left|\nabla A_{g_{j}}\right|^{q} d v_{g_{j}}\right)^{1 / q} \\
\leq & 2 r_{j}^{-2+n / 2 q} \Lambda_{1}^{(q-1) / q} \Lambda_{2}^{1 / q} \longrightarrow 0 \quad(j \longrightarrow \infty) .
\end{aligned}$$
By (5.29), when $n \leq 5$ we have that $A_{h_{a}} \equiv 0$, i.e., $h_{a}$ is of harmonic curvature. In particular, when $n=3\left(N_{a}, h_{a}\right)$ is conformally flat.

The proof of (2°.6) follows from the lower semicontinuity of the curvature integral. This completes the proof of Theorem 1.1. \(\square\)