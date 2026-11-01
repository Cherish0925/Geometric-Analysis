---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Monopole metrics and the orbifold Yamabe problem]

We proceed with the definition of the Sobolev constant.
Definition 7.3. - For $\hat{M}$ compact, we define the Sobolev constant $C_{S}$ as the best constant $C_{S}$ so that for all $f \in C^{0,1}(\hat{M})$ we have
$$\|f\|_{L^{4}} \leqslant C_{S}\left(\|\nabla f\|_{L^{2}}+\|f\|_{L^{2}}\right) .$$
For $M$ non-compact, $C_{S}$ is defined to be the best constant so that
$$\|f\|_{L^{4}} \leqslant C_{S}\|\nabla f\|_{L^{2}},$$
for all $f \in C^{0,1}(M)$ with compact support.
We next prove the lower estimate on the Yamabe invariant in Theorem 1.2.

Theorem 7.4. - Let $(\hat{M}, \hat{g})$ be a LeBrun self-dual conformal class on $n \# \mathbb{C P}^{2}$ with $n$ monopole points $\left\{p_{1}, \ldots, p_{n}\right\}$. Assume that all monopole points are contained in a compact set $\mathcal{K} \subset \mathcal{H}^{3}$. Then there exists a constant $\delta_{n}>0$ depending only upon $n, \mathcal{K}$ such that
$$0<\delta_{n} \leqslant Y(\hat{M},[\hat{g}]) .$$

Proof. - Let $\hat{g}_{\mathrm{LB}, i}$ be a sequence of such LeBrun metrics, with monopole points $p_{i, j}, j=1 \ldots n$, and assume that
$$\left\{p_{i, 1}, \ldots, p_{i, n}\right\} \rightarrow\left\{m_{1} \cdot p_{\infty, 1}, \ldots, m_{k} \cdot p_{\infty, k}\right\},$$
as $i \rightarrow \infty$ with $p_{\infty, j} \in \mathcal{H}^{3}$ for $1 \leqslant j \leqslant k$ allowing for multiplicity (from our assumption, there are no limit points on $\partial \mathcal{H}^{3}$ ). Inspired by [33], let
$$f_{i}=-\left(\rho_{i, 1}+\cdots+\rho_{i, n}\right) / n,$$
where $\rho_{i, j}(\cdot)=d_{\mathcal{H}^{3}}\left(p_{i, j}, \cdot\right)$. Without loss of generality, by conformal invariance, we may assume that $p_{i, 1}=(0,0,1)$. Consider the conformally compactified $\tilde{g}_{i}=e^{2 f_{i}} z^{-2} g_{\mathrm{LB}, i}$, as in (3.11). Note that since all points are contained in a compact set around $p_{i, 1}=(0,0,1), f_{i}$ is bounded from below on any compact set, and $f_{i}(x) \sim-p_{i, 1}(x)$ as $x \rightarrow \partial \mathcal{H}^{3}$. This implies that $\lambda<\operatorname{Vol}\left(\tilde{g}_{i}\right)<\Lambda$, for some positive constants $\lambda$ and $\Lambda$. The same argument in Theorem 7.1, then shows that $\tilde{g}_{i}$ converges to a non-trivial limiting orbifold $\left(\hat{M}_{\infty}, \hat{g}_{\infty}\right)$ with finitely many ALE orbifold bubbles (our conformal factor now varies with $i$, but it remains bounded and strictly positive near the singularities, so the same argument applies). Since $\left|\nabla \rho_{i, j}\right|=1$, this implies the inequality
$$\left|\nabla f_{i}\right|^{2}<1 / n .$$
From (3.12), we estimate the scalar curvature
$$\begin{aligned}
R_{\tilde{g}_{i}} & =6 e^{-2 f_{i}} V_{i}^{-1}\left(-1-\Delta f_{i}-\left|\nabla f_{i}\right|^{2}\right) \\
& >6 e^{-2 f_{i}} V_{i}^{-1}\left(-2-\Delta f_{i}\right)=6 e^{-2 f_{i}} V_{i}^{-1} n^{-1} \sum_{j}\left(-2+\Delta \rho_{i, j}\right),
\end{aligned}$$
where $V_{i}$ is defined in (2.7), corresponding to the $n$ monopole points $p_{i, j}$. Using Lemma 3.1, we obtain the estimate
$$R_{\tilde{g}_{i}}>24 e^{-2 f_{i}} V_{i}^{-1} n^{-1} \sum_{j} e^{-2 \rho_{i, j}} V_{i, j},$$
where $V_{i, j}=1+\Gamma_{p_{i, j}}$. For each $j$, the function $V_{i}^{-1} V_{i, j}$ is smooth and uniformly positive (with a lower bound independent of $i$ ), so we have
$$R_{\tilde{g}_{i}}>C e^{-2 f_{i}} \sum_{j} e^{-2 \rho_{i, j}},$$
for some constant $C>0$. Obviously, for some $j_{0}$ we must have
$$\frac{1}{n} \sum_{j} \rho_{i, j} \geqslant \rho_{i, j_{0}} .$$
Therefore, we have the estimate
$$R_{\tilde{g}_{i}}>\delta>0 .$$

We also claim that there is a uniform bound on the Sobolev constant (7.4). The limit space $\left(\hat{M}_{\infty}, \hat{g}_{\infty}\right)$ has bounded Sobolev constant (7.4) since it is a compact orbifold. Furthermore, all of the bubbles are ALE orbifolds, which have bounded Sobolev constants (7.5) by [11], and each are glued onto the previous orbifold by Euclidean neck regions. Therefore, using a standard partition of unity argument (at possibly several scales) and scale invariance
of the Sobolev constant (7.5), it follows that the Sobolev constant of the sequence is uniformly bounded. This is proved in detail in [27, Proposition 2.2], and the generalization to this case is straightforward, so we omit the details.

To finish the proof, we include the following standard argument. Assume by contradiction that there is a sequence of unit-volume Yamabe minimizers in each conformal class $g_{Y, i}=v_{i}^{2} \tilde{g}_{i}$ with $R_{i} \rightarrow 0$ as $i \rightarrow \infty$, where $R_{i}$ is the (constant) scalar curvature of $g_{Y, i}$. The Yamabe equation is
$$-6 \Delta v_{i}+R\left(\tilde{g}_{i}\right) v_{i}=R_{i} v_{i}^{3} .$$
Multiply by $v_{i}$ and integrate to get
$$\begin{aligned}
6 \int\left|\nabla v_{i}\right|^{2} d V_{\tilde{g}_{i}}+\int R\left(\tilde{g}_{i}\right) v_{i}^{2} d V_{\tilde{g}_{i}} & = \\
& \int R_{i} v_{i}^{4} d V_{\tilde{g}_{i}}=R_{i} \operatorname{Vol}\left(g_{Y, i}\right)=R_{i} .
\end{aligned}$$
The right hand side limits to zero, therefore the left-hand side does also as $i \rightarrow \infty$. From (7.13), $R\left(\tilde{g}_{i}\right)$ is uniformly positive, so the $W^{1,2}$ norm of $v_{i}$ can be made arbitrarily small. Using the uniform Sobolev inequality and lower volume bound for $\tilde{g}_{i}$,
$$\begin{aligned}
& 1=\operatorname{Vol}\left(g_{Y, i}\right)^{1 / 4}= \\
& \quad\left\|v_{i}\right\|_{L^{4}} \leqslant C_{S}\left(\tilde{g}_{i}\right)\left(\left\|\nabla v_{i}\right\|_{L^{2}}+\left\|v_{i}\right\|_{L^{2}}\right) \leqslant C^{\prime}\left\|v_{i}\right\|_{W^{1,2}},
\end{aligned}$$
which is a contradiction for $i$ sufficiently large. \(\square\)

\subsection*{7.3. Convergence of constant scalar curvature metrics}

We are now in a position to describe the possible limits of the Yamabe minimizers. The following Theorem implies the main part of Theorem 1.2.

Theorem 7.5. - Fix $n$, and let $\left(M, g_{i}\right)$ be an arbitrary sequence of $n$-pointed LeBrun metrics, with conformal compactifications $\left(\hat{M},\left[\hat{g}_{i}\right]\right)$. Assume that there exists a constant $\delta_{n}$ such that
$$0<\delta_{n} \leqslant Y\left(\hat{M},\left[\hat{g}_{i}\right]\right) .$$
Let $g_{Y, i} \in\left[\hat{g}_{i}\right]$ be a sequence of unit volume Yamabe minimizers. Then there exists a subsequence $g_{Y, j},\{j\} \subset\{i\}$, which converges to either (1) a constant scalar curvature metric on a $k$-pointed LeBrun orbifold, $1 \leqslant$ $k \leqslant n$, or (2) a single football metric, that is, $S^{4} / \mathbb{Z}_{m}$ with the round metric, for $2 \leqslant m \leqslant n$.

Proof. - As in Theorem 7.1, we choose a compactification with fixed conformal factor $\tilde{g}_{i} \in\left[g_{i}\right]$, so that the sequence $\left(\hat{M}, \tilde{g}_{i}\right)$ will limit to a compactified LeBrun orbifold, with each bubble-tree consisting of a string of multi-Eguchi-Hanson orbifolds, and possibly other AF LeBrun orbifold metrics (in case some monopole points limit to the boundary of $\mathcal{H}^{3}$ ). Call this limit space $\left(\hat{M}_{\infty}, \hat{g}_{\infty}\right)$, and the finite singular set of convergence $S \subset \hat{M}_{\infty}$. We write the sequence of unit volume Yamabe minimizers in each conformal class as $g_{Y, i}=v_{i}^{2} \tilde{g}_{i}$. Let $R_{i}$ denote the scalar curvature of $g_{Y, i}$. By passing to a subsequence, assume that $\lim _{i \rightarrow \infty} R_{i}=R_{\infty}$. From the assumption (7.17), $R_{\infty}>\delta>0$.

The assumption (7.17) implies that the Yamabe minimizers $g_{Y, i}$ satisfy a uniform Sobolev inequality of the following form [46, Proposition 3.1]
$$\|f\|_{L^{4}} \leqslant C_{S}\|\nabla f\|_{L^{2}}+V o l^{-1 / 4}\|f\|_{L^{2}},$$
for any $f \in C^{0,1}(\hat{M})$. The $L^{2}$-norm of the curvature is uniformly bounded, as seen above in Section 6. We may therefore quote the compactness theorem of [46, Theorem 1.1] to obtain a subsequence converging to a multi-fold limit. The Sobolev inequality (7.18) and $b_{1}(\hat{M})=0$ together imply that the limit must be an irreducible orbifold [46, Proposition 7.2].

Let $C_{i}=\max _{\hat{M}} u_{i}$. If $C_{i}$ remains bounded from above, then we argue as follows. On any compact subset $D \subset \hat{M}_{\infty} \backslash S$, we have a Harnack inequality (since the conformal factors are bounded from above, and the sequence is smoothly converging away from the singular set). This implies that the conformal factors $u_{i}$ will either have a strictly positive limit on $\hat{M}_{\infty}$ or will uniformly crash to zero on $\hat{M}_{\infty}$. The latter case cannot happen since $\operatorname{Vol}\left(g_{Y, i}\right)=1$. Consequently, the limit must be a CSC (constant scalar curvature) metric conformal to $\left(\hat{M}_{\infty}, \hat{g}_{\infty}\right)$, and we are in Case (1).

So we next assume that $C_{i} \rightarrow \infty$ as $i \rightarrow \infty$. Let $x_{i}$ be points such that $u_{i}\left(x_{i}\right)=C_{i}$. We first assume that $x_{i} \rightarrow x \in \hat{M}_{\infty} \backslash S$. Then the usual conformal dilation argument says that a bubble is forming on the smooth part [42]. To summarize, this is by looking at the rescaled functions $\tilde{u}_{i}(y)=C_{i}^{-1} u_{i}\left(C_{i}^{-1} y\right)$. By elliptic theory, this sequence has a subseqence converging to a positive solution of $-6 \Delta u=R_{\infty} u^{3}$ on $\mathbb{R}^{4}$, satisfying $u(0)=1$. From our assumption on the Yamabe invariant, $R_{\infty}>\delta>0$. By Caffarelli-Gidas-Spruck [12], the limit must be the spherical metric. This implies that the Yamabe invariant satisfies $Y\left(\hat{M},\left[\tilde{g}_{i}\right]\right) \gtrsim Y\left(S^{4},\left[g_{S}\right]\right)$, for $i$ large, which contradicts Theorem 3.2 above. Therefore, we must have $x_{i} \rightarrow p \in S$ as $i \rightarrow \infty$. Let $\left(X_{1}, g_{1}\right)$ be the first bubble at $p$. Assume that, after the rescaling the sequence to limit to $\left(X_{1}, g_{1}\right)$ (pointed convergence based at $p$ ), $x_{i}$ limits to a finite point of $X_{1}$. The same conformal dilation
argument shows that the rescaled conformal factor (with $g_{1}$ as background metric) must be bounded from above. Away from the singular points of convergence $p_{1, j^{\prime}}, j^{\prime}=1 \ldots k_{1}$, we again have a Harnack inequality. So the rescaled conformal factor either (a) limits identically to zero away from the singlar points, or (b) has a finite positive limit everywhere. In Case (b), the limit of the original sequence must then be a CSC metric on the conformal compactification $\left(\hat{X}_{1}, \hat{g}_{1}\right)$, since this is the only possible irreducible orbifold limit. If $X_{1}$ is an Eguchi-Hanson orbifold, this cannot happen by Proposition 4.2. So the only possibility in Case (b) is that $\left(X_{1}, g_{1}\right)$ is an orbifold LeBrun AF metric, whose compactification is Case (1). Case (a) splits into two possibilities. Case (a1) is that $x_{i}$ will limit to $\infty$ in $\left(X_{1}, g_{1}\right)$. In this case, the only possible irreducible orbifold limit will be a metric on the compactification of the "neck" region. This follows since all ALE spaces in the bubble tree described in Theorem 7.1 have one end, the only possible neck regions are modeled on $\mathbb{R}^{4} / \mathbb{Z}_{m}$. The only CSC metric on the compactification of this is the $S^{4} / \mathbb{Z}_{m}$-football metric, by the Obata-Tashiro Theorem [38, 43]. Therefore, Case (a1) is exactly Case (2). Case (a2) is that $x_{i}$ limits to one of the singular points of convergence of $X_{1}$ in this scaling. We then repeat the above argument around this singular point. In general, we repeat the entire argument at different scalings to see that the limit must be (i) a CSC metric on exactly one of the compactified orbifolds in the bubble-tree, or (ii) limit occurring on a neck region. For Case (i), the Gibbons-Hawing orbifolds do not admit CSC metrics by Proposition 4.2, so Case (i) is exactly Case (1). The argument above shows that Case (ii) is exactly Case (2).

Finally, in Case (1), the limit can never be a compactified 0-pointed LeBrun metric. This is conformal to $S^{4}$ with the round metric, and the only CSC metrics in this conformal class are of constant curvature [38], so have maximal Yamabe invariant. This would contradict (1.4). This also proves $2 \leqslant m$ in Case (2). \(\square\)

\subsection*{7.4. Completion of proofs of Theorems 1.1 and 1.5}

The Yamabe invariant for $n=2,3$ is stricly positive by Proposition 6.1. For Theorem 1.1, as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow \infty$, Theorem 7.5 says the only possible limit is the compactified 1-pointed LeBrun metric, since Case (2) obviously does not happen. This is conformal to the Fubini-Study metric, which is the unique CSC metric in its conformal class by Obata's Theorem [38]. We note that the behavior of the Yamabe-minimizer on a connect sum is
typically non-symmetric [28, 27]. Since the Yamabe minimizers must limit to the Fubini-Study metric, it is then obvious that for $d_{H}\left(p_{1}, p_{2}\right)$ very large, the Yamabe minimizers cannot be invariant under the conformal involution which flips the two monopole points (see Section 5.1). Therefore, there must always be at least two distinct Yamabe minimizers, which are related by this conformal involution.

We next address the $K$-symmetric limit to $S^{4}$. The existence of $K$ -symmetric minimizers follows from [21]. Again, by [46] we can find a subsequence converging to a multi-fold, but which now may have reducible points. But from the estimate on the $K$-Yamabe invariant in Theorem 5.4, as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow \infty$, it is clear that the only possibility for a $K$-Yamabe minimizer is $S^{4}$ with the round metric. This follows because a reflection interchanging the two monopole point is clearly not an isometry of the two Yamabe minimizers, so these are not possible limits. From the arguments in the proof of Theorem 7.5, another possible limit is $\mathbb{C P}^{2} \vee \mathbb{C P}^{2}$, with the Fubini-Study metric scaled to have $V o l=1 / 2$ on each factor. But this cannot occur since the Yamabe invariant of this limit is $24 \pi>8 \pi \sqrt{6}=Y\left(S^{4}, g_{S}\right)$, and this would contradict Theorem 5.4. Similarly, the limit $\mathbb{C P}^{2} \vee S^{4}$ cannot happen either. Therefore, any sequence of Yamabe minimizers must concentrate entirely in the neck region. The only possible limit is then $S^{4}$ with the round metric, with Burns metrics bubbling off at the 2 singular points of convergence. This follows since any reducible limit would be several $S^{4}$-s wedged together, which would have Yamabe invariant strictly larger than $8 \pi \sqrt{6}$.

Remark 7.6. - As shown in [25], $G$ is generated by $K$ and an extra involution $\Lambda$ which is not a lift of a hyperbolic isometry, and is quite difficult to describe explicitly. It is likely that as $d\left(p_{1}, p_{2}\right) \rightarrow \infty$, the $G$-symmetric metric must also limit to $S^{4}$. But since the test metric in (5.12) is not invariant under $\Lambda$, we cannot say this for certain.

The fourth metric in Theorem 1.1 is obtained by adapting the CSC-gluing argument of Joyce to this problem [27], see also [35]. Recall that the Euclidean Schwarzschild metric in dimension $n$ is defined as
$$g=\left(1+\frac{m}{(n-1) r^{n-2}}\right)^{\frac{4}{n-2}} g_{0},$$
on $\mathbb{R}^{n} \backslash\{0\}$, where $g_{0}$ is the Euclidean metric, and $m>0$ is the mass parameter. This metric is scalar-flat, locally conformally flat, and AF with two ends. One chooses a conformal factor which is close to the Fubini-Study
metric on neighborhoods of the monopole points, and is close to a scaleddown Schwarzschild neck region in between; this will be the approximate CSC-metric. One then uses the implicit function theorem, together with the crucial fact that the Fubini-Study metric is CSC-nondegenerate, to perturb to a CSC metric. This adaptation is straightforward, but since the argument is quite lengthy, we omit the details due to space considerations.

As $d_{H}\left(p_{1}, p_{2}\right) \rightarrow 0$, Case (1) in Theorem 7.5 could only be a compactified LeBrun metric with a single point of multiplicity 2 . This is conformal (minus the orbifold point) to the Eguchi-Hanson metric, which does not admit any CSC metric by Theorem 1.3, so this case cannot happen. Consequently, the only possibility for the limit is the $S^{4} / \mathbb{Z}_{2}$-football with the round metric (since the limit of Yamabe minimizers must be irreducible). Similarly, Theorem 1.3 implies that as $d_{H}\left(p_{1}, p_{2}\right) \rightarrow 0$, the only possible $K$-symmetric limit is the $S^{4} / \mathbb{Z}_{2}$-football with the round metric. To see this, again the only concentration can occur in the neck region, which is $\mathbb{R}^{4} / \mathbb{Z}_{2}$. The limit no longer has to be irreducible. But the lowest energy reducible limit would be the wedge of two $S^{4} / \mathbb{Z}_{2}$-footballs, whose Yamabe energy is $8 \pi \sqrt{6}$. However, since in this case the points are not limiting to the boundary of $\mathcal{H}^{3}$, Theorem 5.4 shows that the Yamabe energy must be strictly less than $8 \pi \sqrt{6}$, so this cannot happen, and therefore the limit must be the irreducible $S^{4} / \mathbb{Z}_{2}$-football.

For the first case in Theorem 1.5, as $p_{3} \rightarrow p_{2}$, the only possible limits from Theorem 7.5 are Case (1): a compactified LeBrun metric with a single monopole point, and another multiplicity 2 point, or Case (2): a $S^{4} / \mathbb{Z}_{2}$-football with the round metric. However, under the assumptions of Theorem 1.5, (4.11) says the Yamabe invariant is strictly less than that of the $S^{4} / \mathbb{Z}_{2}$-football, so the limit must be Case (1).

Finally, for the last case in Theorem 1.5, as $p_{3} \rightarrow \partial \mathcal{H}^{3}$, the Yamabe invariant is strictly less than that of $g_{F S}$ by Theorem 3.2. Thus the only possible limit is Case (1), a 2-pointed LeBrun compactified metric.

\section*{8. Questions}

We conclude with a list of questions.
\begin{itemize}
\item[-] What is the optimal lower bound for the Yamabe invariant in (1.5) for $n \geqslant 2$ ? We conjecture that $\delta_{n}=Y_{\text {orb }}\left(S^{4} / \mathbb{Z}_{n},\left[g_{S}\right]\right)$; this is true for $n=2$, as seen above in Theorem 1.1. Furthermore, the assumption that the points are contained in a compact set $\mathcal{K} \subset \mathcal{H}^{3}$ should not be necessary. Removing this assumption would imply that the
\end{itemize}
\begin{itemize}
\begin{itemize}
\item[] moduli space of Yamabe minimizing LeBrun metrics has a nice compactification for any $n$. As seen above, this is true for $n=2,3$.
\item[-] Does the compactified LeBrun metric on $\mathcal{O}(-n)$ admit a CSC metric for $n \geqslant 3$ ? The answer is no for $n=2$ since this is the compactified Eguchi-Hanson metric, which was ruled out by Theorem 1.3. For $n \geqslant 3$, Theorem 1.4 rules out any symmetric solution, but is there a non-symmetric solution? Furthermore, as shown in Theorem 7.1, if all monopole points approach a single point at a uniform rate, the bubble-tree structure is a compactified LeBrun negativemass metric on $\mathcal{O}(-n)$, with a Gibbons-Hawking multi-Eguchi-Hanson bubbling off. From the arguments in Section 7, the limit of the Yamabe minimizers could limit to either a CSC metric on compactified $\mathcal{O}(-n)$, or to the $S^{4} / \mathbb{Z}_{n}$-football (since the compactified GH metric does not admit a CSC metric by Theorem 1.3). Which one actually happens for $n \geqslant 3$ ?
\item[-] Except for the case of a single monopole point with multiplicity $n$, does a $\left[\hat{g}_{L B}\right]$ orbifold conformal class always admit a CSC metric?
\item[-] In Theorem 1.1, for $n=2$ we determined the limiting behavior of the $K$-Yamabe minimizers as $d\left(p_{1}, p_{2}\right) \rightarrow \infty$ (the limit is $S^{4}$ ). Recall that $K$ is an index 2 subgroup of full conformal group $G$. What is the limit of the $G$-Yamabe minimizers?
\item[-] Are CSC metrics on compactified LeBrun metrics CSC nondegenerate? If so, then it would then be possible to apply the Joyce gluing technique to obtain more non-Yamabe-minimizing examples.
\item[-] LeBrun metrics with torus action are a special case of Joyce metrics [26]. These depend on a choice of points on the boundary of hyperbolic 2-space. What happens as these metrics degenerate?
\end{itemize}
\end{itemize}

\section*{BIBLIOGRAPHY}
\begin{itemize}
\item[] [1] K. Akutagawa, "Yamabe metrics of positive scalar curvature and conformally flat manifolds", Differential Geom. Appl. 4 (1994), no. 3, p. 239-258.
\item[] [2] \_\_\_\_, "Convergence for Yamabe metrics of positive scalar curvature with integral bounds on curvature", Pacific J. Math. 175 (1996), no. 2, p. 307-335.
\item[] [3] \_\_\_\_, "Computations of the orbifold Yamabe invariant", arXiv.org:1009.3576, 2010.
\item[] [4] K. Akutagawa \& B. Botvinnik, "Yamabe metrics on cylindrical manifolds", Geom. Funct. Anal. 13 (2003), no. 2, p. 259-333.
\item[] [5] \_\_\_\_, "The Yamabe invariants of orbifolds and cylindrical manifolds, and $L^{2}$ -harmonic spinors", J. Reine Angew. Math. 574 (2004), p. 121-146.
\item[] [6] M. T. Anderson, "Ricci curvature bounds and Einstein metrics on compact manifolds", J. Amer. Math. Soc. 2 (1989), no. 3, p. 455-490.
\end{itemize}
\begin{itemize}
\item[] [7] \_\_\_\_, "Orbifold compactness for spaces of Riemannian metrics and applications", Math. Ann. 331 (2005), no. 4, p. 739-778.
\item[] [8] M. T. Anderson, P. B. Kronheimer \& C. LeBrun, "Complete Ricci-flat Kähler manifolds of infinite topological type", Comm. Math. Phys. 125 (1989), no. 4, p. 637-642.
\item[] [9] T. Aubin, Nonlinear analysis on manifolds. Monge-Ampère equations, Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 252, Springer-Verlag, New York, 1982, xii+204 pages.
\item[] [10] S. Bando, "Bubbling out of Einstein manifolds", Tohoku Math. J. (2) 42 (1990), no. 2, p. 205-216.
\item[] [11] R. Bartnik, "The mass of an asymptotically flat manifold", Comm. Pure Appl. Math. 39 (1986), no. 5, p. 661-693.
\item[] [12] L. A. Caffarelli, B. Gidas \& J. Spruck, "Asymptotic symmetry and local behavior of semilinear elliptic equations with critical Sobolev growth", Comm. Pure Appl. Math. 42 (1989), no. 3, p. 271-297.
\item[] [13] S.-Y. A. Chang, M. J. Gursky \& P. C. Yang, "An equation of Monge-Ampère type in conformal geometry, and four-manifolds of positive Ricci curvature", Ann. of Math. (2) 155 (2002), no. 3, p. 709-787.
\item[] [14] S.-Y. A. Chang, J. Qing \& P. Yang, "On a conformal gap and finiteness theorem for a class of four-manifolds", Geom. Funct. Anal. 17 (2007), no. 2, p. 404-434.
\item[] [15] X. Chen, C. Lebrun \& B. Weber, "On conformally Kähler, Einstein manifolds", J. Amer. Math. Soc. 21 (2008), no. 4, p. 1137-1168.
\item[] [16] X. Chen \& B. Weber, "Moduli spaces of critical riemannian metrics with $L^{n / 2}$ norm curvature bounds", to appear in Advances in Mathematics, 2007.
\item[] [17] S. Donaldson \& R. Friedman, "Connected sums of self-dual manifolds and deformations of singular spaces", Nonlinearity 2 (1989), no. 2, p. 197-239.
\item[] [18] A. Floer, "Self-dual conformal structures on $l \mathbf{C P}^{2}$ ", J. Differential Geom. 33 (1991), no. 2, p. 551-573.
\item[] [19] G. Gibbons \& S. Hawking, "Gravitational multi-instantons", Physics Letters B 78 (1978), no. 4, p. 430-432.
\item[] [20] M. J. Gursky \& J. A. Viaclovsky, "A fully nonlinear equation on four-manifolds with positive scalar curvature", J. Differential Geom. 63 (2003), no. 1, p. 131-154.
\item[] [21] E. Hebey, "From the Yamabe problem to the equivariant Yamabe problem", in Actes de la Table Ronde de Géométrie Différentielle (Luminy, 1992), Sémin. Congr., vol. 1, Soc. Math. France, Paris, 1996, Joint work with M. Vaugon, p. 377-402.
\item[] [22] N. J. Hitchin, "Polygons and gravitons", Math. Proc. Cambridge Philos. Soc. 85 (1979), no. 3, p. 465-476.
\item[] [23] \_\_\_\_, "Einstein metrics and the eta-invariant", Boll. Un. Mat. Ital. B (7) 11 (1997), no. 2, suppl., p. 95-105.
\item[] [24] N. Honda, "Degenerations of LeBrun twistor spaces", to appear in Communications in Mathematical Physics, 2010.
\item[] [25] N. Honda \& J. Viaclovsky, "Conformal symmetries of self-dual hyperbolic monopole metrics", arXiv.org:0902.2019, 2009.
\item[] [26] D. Joyce, "Explicit construction of self-dual 4-manifolds", Duke Math. J. 77 (1995), no. 3, p. 519-552.
\item[] [27] \_\_\_\_, "Constant scalar curvature metrics on connected sums", Int. J. Math. Math. Sci. (2003), no. 7, p. 405-450.
\item[] [28] O. Kobayashi, "Scalar curvature of a metric with unit volume", Math. Ann. 279 (1987), no. 2, p. 253-265.
\item[] [29] P. B. Kronheimer, "The construction of ALE spaces as hyper-Kähler quotients", J. Differential Geom. 29 (1989), no. 3, p. 665-683.
\end{itemize}
\begin{itemize}
\item[] [30] W. Kühnel, "Conformal transformations between Einstein spaces", in Conformal geometry (Bonn, 1985/1986), Aspects Math., E12, Vieweg, Braunschweig, 1988, p. 105-146.
\item[] [31] C. LeBrun, "Counter-examples to the generalized positive action conjecture", Comm. Math. Phys. 118 (1988), no. 4, p. 591-596.
\item[] [32] \_\_\_\_, "Explicit self-dual metrics on $\mathbf{C P}_{2} \# \cdots \mathbf{C P}_{2} "$, J. Differential Geom. 34 (1991), no. 1, p. 223-253.
\item[] [33] C. LeBrun, S. Nayatani \& T. Nitta, "Self-dual manifolds with positive Ricci curvature", Math. Z. 224 (1997), no. 1, p. 49-63.
\item[] [34] J. M. Lee \& T. H. Parker, "The Yamabe problem", Bull. Amer. Math. Soc. (N.S.) 17 (1987), no. 1, p. 37-91.
\item[] [35] R. Mazzeo, D. Pollack \& K. Uhlenbeck, "Connected sum constructions for constant scalar curvature metrics", Topol. Methods Nonlinear Anal. 6 (1995), no. 2, p. 207-233.
\item[] [36] H. Nakajima, "Self-duality of ALE Ricci-flat 4-manifolds and positive mass theorem", in Recent topics in differential and analytic geometry, Adv. Stud. Pure Math., vol. 18, Academic Press, Boston, MA, 1990, p. 385-396.
\item[] [37] \_\_\_\_, "A convergence theorem for Einstein metrics and the ALE spaces [ MR1193019 (93k:53044)]", in Selected papers on number theory, algebraic geometry, and differential geometry, Amer. Math. Soc. Transl. Ser. 2, vol. 160, Amer. Math. Soc., Providence, RI, 1994, p. 79-94.
\item[] [38] M. Obata, "The conjectures on conformal transformations of Riemannian manifolds", J. Differential Geometry 6 (1971/72), p. 247-258.
\item[] [39] Y. S. Poon, "Compact self-dual manifolds with positive scalar curvature", J. Differential Geom. 24 (1986), no. 1, p. 97-132.
\item[] [40] J. G. Ratcliffe, Foundations of hyperbolic manifolds, second ed., Graduate Texts in Mathematics, vol. 149, Springer, New York, 2006, xii+779 pages.
\item[] [41] R. Schoen, "Conformal deformation of a Riemannian metric to constant scalar curvature", J. Differential Geom. 20 (1984), no. 2, p. 479-495.
\item[] [42] \_\_\_\_, "On the number of constant scalar curvature metrics in a conformal class", in Differential geometry, Pitman Monogr. Surveys Pure Appl. Math., vol. 52, Longman Sci. Tech., Harlow, 1991, p. 311-320.
\item[] [43] Y. Tashiro, "Complete Riemannian manifolds and some vector fields", Trans. Amer. Math. Soc. 117 (1965), p. 251-275.
\item[] [44] G. Tian, "On Calabi's conjecture for complex surfaces with positive first Chern class", Invent. Math. 101 (1990), no. 1, p. 101-172.
\item[] [45] G. Tian \& J. Viaclovsky, "Bach-flat asymptotically locally Euclidean metrics", Invent. Math. 160 (2005), no. 2, p. 357-415.
\item[] [46] \_\_\_\_, "Moduli spaces of critical Riemannian metrics in dimension four", Adv. Math. 196 (2005), no. 2, p. 346-372.
\item[] [47] \_\_\_\_, "Volume growth, curvature decay, and critical metrics", Comment. Math. Helv. 83 (2008), no. 4, p. 889-911.
\end{itemize}

> Manuscrit reçu le 15 février 2010,
> révisé le 8 octobre 2010,
> accepté le 15 octobre 2010.

> Jeff A. VIACLOVSKY
> University of Wisconsin
> Department of Mathematics
> 480 Lincoln Drive

Madison, WI 53706 (USA)
jeffv@math.wisc.edu