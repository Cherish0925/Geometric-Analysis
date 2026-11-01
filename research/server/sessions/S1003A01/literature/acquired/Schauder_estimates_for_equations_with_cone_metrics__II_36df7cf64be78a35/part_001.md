---
retention_scope: session
part: 1
total_parts: 5
---

[Part 1/5 of: Schauder estimates for equations with cone metrics, II]

---
source_file: Schauder_estimates_for_equations_with_cone_metrics__II_211630f5f3c5.pdf
converter: mathpix
format: mmd
---

\title{
ANALYSIS \& PDE
}

Volume 17 No. 32024

Bin Guo and Jian Song

SCHAUDER ESTIMATES FOR EQUATIONS WITH CONE METRICS, II
msp

\title{
SCHAUDER ESTIMATES FOR EQUATIONS WITH CONE METRICS, II
}

\author{
Bin Guo and Jian Song
}

\begin{abstract}
We continue our work on the linear theory for equations with conical singularities. We derive interior Schauder estimates for linear elliptic and parabolic equations with a background Kähler metric of conical singularities along a divisor of simple normal crossings. As an application, we prove the short-time existence of the conical Kähler-Ricci flow with conical singularities along a divisor with simple normal crossings.
\end{abstract}
1. Introduction ..... 757
2. Preliminaries ..... 763
3. Elliptic estimates ..... 766
4. Parabolic estimates ..... 807
5. Conical Kähler-Ricci flow ..... 825
References ..... 828

\section*{1. Introduction}

This is a continuation of our paper [20]. Regularity of solutions of complex Monge-Ampère equations is a central problem in complex geometry. Complex Monge-Ampère equations with singular and degenerate data can be applied to study compactness and moduli problems of canonical Kähler metrics in Kähler geometry. In [43], Yau considered special cases of complex singular Monge-Ampère equations as generalizations of his solution to the Calabi conjecture. Conical singularities along complex hypersurfaces of a Kähler manifold are among the mildest singularities in Kähler geometry, and they have been extensively studied, especially in the case of Riemann surfaces [28; 41]. The study of such Kähler metrics with conical singularities has many geometric applications, for example, the Chern number inequality in various settings [38; 39]. Recently, Donaldson [14] initiated the program of studying analytic and geometric properties of Kähler metrics with conical singularities along a smooth complex hypersurface on a Kähler manifold. This is an essential step in the solution of the Yau-Tian-Donaldson conjecture relating existence of Kähler-Einstein metrics and algebraic K-stability on Fano manifolds [7; 8; 9; 40]. In [14], the Schauder estimate for linear Laplace equations with the conical background metric is established using classical potential theory. This is crucial for the openness of the continuity method to find a desirable

\footnotetext{
Research supported in part by the National Science Foundation grants DMS-17-11439 and DMS-17-10500. Both authors thank Duong H. Phong and Ved Datar for many insightful discussions.
MSC2010: 35J15, 35K10, 35K67.
Keywords: conic Kähler metrics, Schauder estimates.
}
(conical) Kähler-Einstein metric. Donaldson's Schauder estimate is generalized to the parabolic case [5] with a similar classical approach. There is also an alternative approach for the conical Schauder estimates using microlocal analysis [23]. Various global and local estimates and regularity are also derived in the conical setting [1; 6; 11; 12; 13; 15; 19; 24; 29; 32; 44; 45].

The Schauder estimates play an important role in linear PDE theory. Apart from the classical potential theory, various proofs have been established by different analytic techniques. In fact, the blow-up or perturbation techniques developed in [36; 42] (also see [2; 3; 33; 34]) are much more flexible and sharper than the classical method. The authors combined the perturbation method in [20] and geometric gradient estimates to establish sharp Schauder estimates for Laplace equations and heat equations on $\mathbb{C}^{n}$ with a background flat Kähler metric of conical singularities along the smooth hyperplane $\left\{z_{1}=0\right\}$ and derived explicit and optimal dependence on conical parameters.

In algebraic geometry, one often has to consider pairs ( $X, D$ ) with $X$ an algebraic variety of complex dimension $n$ and the boundary divisor $D$ a complex hypersurface of $X$. After possible log resolution, one can always assume the divisor $D$ is a union of smooth hypersurfaces with simple normal crossings. The suitable category of Kähler metrics associated to $(X, D)$ is the family of Kähler metrics on $X$ with conical singularities along $D$. In order to study canonical Kähler metrics on pairs and related moduli problems, we are obliged to study regularity and asymptotics for complex Monge-Ampère equation with prescribed conical singularities of normal crossings. However, the linear theory is still missing and has been open for a while. The goal of this paper is to extend our result [20] and establish the sharp Schauder estimates for linear equations with background Kähler metric of conical singularities along divisors of simple normal crossings. We can apply and extend many techniques developed in [20]; however, new estimates and techniques have to be developed because, in the case of conical singularities along a single smooth divisor, the difficult estimate in the conical direction can sometimes be bypassed and reduced to estimates in the regular directions, while such treatment does not work in the case of simple normal crossings. One is forced to treat regions near high codimensional singularities directly with new and more delicate estimates beyond the scope of [20]. More crucially, the estimates in the mixed normal directions (see Section 3D) relies on those in Lemma 3.3, which is new compared to the case of a smooth divisor [20]. This enables us to compare the difference of mixed normal derivatives at two different points. Readers who are interested only in the case of smooth divisors are advised to omit Section 3D.

The standard local models for such conical Kähler metrics are described below.
Let $\boldsymbol{\beta}=\left(\beta_{1}, \ldots, \beta_{p}\right) \in(0,1)^{p}, p \leq n$, and let $\omega_{\boldsymbol{\beta}}$ (or $g_{\boldsymbol{\beta}}$ ) be the standard cone metric on $\mathbb{C}^{p} \times \mathbb{C}^{n-p}$ with cone singularity along $\mathcal{S}=\bigcup_{i=1}^{p} \mathcal{S}_{i}$, where $\mathcal{S}_{i}=\left\{z_{i}=0\right\}$, that is,
$$\omega_{\beta}=\sum_{j=1}^{p} \beta_{j}^{2} \frac{\sqrt{-1} d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2\left(1-\beta_{j}\right)}}+\sum_{j=p+1}^{n} \sqrt{-1} d z_{j} \wedge d \bar{z}_{j} .$$
We shall use $s_{2 p+1}, \ldots, s_{2 n}$ to denote the real coordinates of $\mathbb{C}^{n-p}=\mathbb{R}^{2 n-2 p}$ such that, for $j=p+1, \ldots, n$,
$$z_{j}=s_{2 j-1}+\sqrt{-1} s_{2 j} .$$

In this paper we will study the conical Laplacian equation with the background metric $g_{\beta}$ on $\mathbb{C}^{n}$
$$\Delta_{\beta} u=f \quad \text { in } B_{\beta}(0,1) \backslash \mathcal{S},$$
where $B_{\beta}(0,1)$ is the unit ball with respect to $g_{\beta}$ centered at 0 . The Laplacian $\Delta_{\beta}$ is defined as
$$\Delta_{\beta} u=\sum_{j, k} g_{\beta}^{j \bar{k}} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{k}}=\sum_{j=1}^{p} \beta_{j}^{-1}\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}+\sum_{j=p+1}^{n} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}} .$$
We always assume
$$f \in C^{0}\left(B_{\beta}(0,1)\right) \quad \text { and } \quad u \in C^{0}\left(\overline{B_{\beta}(0,1)}\right) \cap C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) .$$
Throughout this paper, given a continuous function $f$, we write
$$\omega(r):=\omega_{f}(r)=\sup _{\substack{z, w \in B_{\beta}(0,1) \\ d_{\beta}(z, w)<r}}|f(z)-f(w)|$$
for the oscillation of $f$ with respect to $g_{\beta}$ in the ball $B_{\beta}(0,1)$. It is clear that $\omega(2 r) \leq 2 \omega(r)$ for any $r<\frac{1}{2}$. We say a continuous function $f$ is Dini continuous if $\int_{0}^{1} \omega(r) / r d r<\infty$.

Definition 1.1. We will write the (weighted) polar coordinates of $z_{j}$ for $1 \leq j \leq p$ as
$$r_{j}=\left|z_{j}\right|^{\beta_{j}}, \quad \theta_{j}=\arg z_{j} .$$
We define $D^{\prime}$ to be one of the first-order operators $\left\{\partial / \partial s_{2 p+1}, \ldots, \partial / \partial s_{2 n}\right\}$, and $N_{j}$ to be one of the operators $\left\{\partial / \partial r_{j},\left(\beta_{j} r_{j}\right)^{-1}\left(\partial / \partial \theta_{j}\right)\right\}$ which as vector fields are transversal to $\mathcal{S}_{j}$.

Our first main result is the Hölder estimates of the solution $u$ to (1-2).
Theorem 1.2. Suppose $\boldsymbol{\beta} \in\left(\frac{1}{2}, 1\right)^{p}$ and $f \in C^{0}\left(\boldsymbol{B}_{\boldsymbol{\beta}}(0,1)\right)$ is Dini continuous with respect to $g_{\boldsymbol{\beta}}$. Let $u \in C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right) \cap C^{2}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right)$ be the solution to (1-2). Then there exists $C=C(n, \boldsymbol{\beta})>0$ such that, for any two points $p, q \in B_{\beta}\left(0, \frac{1}{2}\right) \backslash \mathcal{S}$,
$$\begin{aligned}
\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right|+\left.\sum_{j=1}^{p}| | z_{j}\right|^{2\left(1-\beta_{j}\right)} & \left.\frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}(p)-\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}(q) \right\rvert\, \\
& \leq C\left(d\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right),
\end{aligned}$$
for any $1 \leq j \leq p$,
$$\left|N_{j} D^{\prime} u(p)-N_{j} D^{\prime} u(q)\right| \leq C\left(d^{1 / \beta_{j}-1}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{1 / \beta_{j}-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{j}}} d r\right),$$
and, for any $1 \leq j, k \leq p$ with $j \neq k$,
$$\left|N_{j} N_{k} u(p)-N_{j} N_{k} u(q)\right| \leq C\left(d^{1 / \beta_{\max }-1}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{1 / \beta_{\max }-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\max }}} d r\right),$$
where $d=d_{\boldsymbol{\beta}}(p, q)>0$ is the $g_{\boldsymbol{\beta}}$-distance of $p$ and $q$ and $\beta_{\max }=\max \left\{\beta_{1}, \ldots, \beta_{p}\right\} \in\left(\frac{1}{2}, 1\right)$.

Remarks 1.3. (1) The number $\beta_{\text {max }}$ on the right-hand side of (1-5) can be replaced by $\max \left\{\beta_{j}, \beta_{k}\right\}$. (2) We assume $\boldsymbol{\beta} \in\left(\frac{1}{2}, 1\right)^{p}$ for the purposes of exposition and simplification of the statements of Theorems 1.2 and 1.7. When some of the angles $\beta_{j}$ lie in $\left(0, \frac{1}{2}\right]$, the pointwise Hölder estimates in Theorem 1.2 are adjusted as follows: in (1-4), if $\beta_{j} \in\left(0, \frac{1}{2}\right]$, we replace the right-hand side by the right-hand side of (1-3); in (1-5), if both $\beta_{j}$ and $\beta_{k} \in\left(0, \frac{1}{2}\right]$, we also replace the right-hand side by that of (1-3); if at least one of the $\beta_{j}, \beta_{k}$ is bigger than $\frac{1}{2}$, (1-5) remains unchanged. The inequalities in Theorem 1.7 can be adjusted similarly. The proofs of these estimates are contained in the proof of the case when $\beta_{j} \in\left(\frac{1}{2}, 1\right)$ by using the corresponding estimates in (2-3).

An immediate corollary of Theorem 1.2 is a precise form of Schauder estimates for (1-2).
Corollary 1.4. Given $\boldsymbol{\beta} \in(0,1)^{p}$ and $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ for some $0<\alpha<\min \left\{1,1 / \beta_{\text {max }}-1\right\}$, if $u \in C^{0}\left(B_{\beta}(0,1)\right) \cap C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right)$ solves ( $1-2$ ), then $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right)$. Moreover, for any compact subset $K \Subset B_{\beta}(0,1)$, there exists a constant $C=C(n, \boldsymbol{\beta}, K)>0$ such that the following estimate holds (see Definition 2.1 for the notations):
$$\|u\|_{C_{\beta}^{2, \alpha}(K)} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}(0,1)\right)}+\frac{\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}}{\alpha\left(\min \left\{\frac{1}{\beta_{\max }}-1,1\right\}-\alpha\right)}\right) .$$

Remark 1.5. A scaling-invariant version of the Schauder estimate (1-6) is that, for any $0<r<1$, there exists a constant $C=C(n, \boldsymbol{\beta}, \alpha)>0$ such that (see Definition 2.4 for the notations)
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}(0, r)\right)}^{*} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}(0, r)\right)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0, r)\right)}^{(2)}\right),$$
which follows from a standard rescaling argument by scaling $r$ to 1 .
Let $g$ be a $C_{\beta}^{0, \alpha}$-conical Kähler metric on $B_{\beta}(0,1)$ (see Definition 3.31). By definition $g$ is equivalent to $g_{\beta}$. We consider the equation
$$\Delta_{g} u=f \quad \text { in } B_{\beta}(0,1) \quad \text { and } \quad u=\varphi \quad \text { on } \partial B_{\beta}(0,1)$$
for some $\varphi \in C^{0}\left(\partial B_{\beta}(0,1)\right)$. The following theorem is the generalization of Corollary 1.4 for nonflat background conical Kähler metrics, which is useful for applications of global geometric complex Monge-Ampère equations.
Theorem 1.6. For any given $\boldsymbol{\beta} \in(0,1)^{p}, f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ and $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$, there is a unique solution $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right) \cap C^{0}\left(\overline{B_{\beta}(0,1)}\right)$ to (1-8). Moreover, for any compact subset $K \Subset B_{\beta}(0,1)$, there exists $C=C(n, \boldsymbol{\beta}, \alpha, g, K)>0$ such that
$$\|u\|_{C_{\beta}^{2, \alpha}(K)} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}(0,1)\right)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}\right) .$$

Theorem 1.6 can immediately be applied to study complex Monge-Ampère equations with prescribed conical singularities along divisors of simple normal crossings, and most of the geometric and analytic results for canonical Kähler metrics with conical singularities along a smooth divisor can be generalized to the case of simple normal crossings.

We now turn to the parabolic Schauder estimates for the solution $u \in \mathscr{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathscr{C}^{2}\left(\mathcal{Q}_{\boldsymbol{\beta}}^{\#}\right)$ to the equation
$$\frac{\partial u}{\partial t}=\Delta_{g_{\beta}} u+f$$
for a Dini continuous function $f$ in $\mathcal{Q}_{\beta}$, where for convenience of notation we write
$$\mathcal{Q}_{\beta}:=B_{\beta}(0,1) \times(0,1] \quad \text { and } \quad \mathcal{Q}_{\beta}^{\#}:=B_{\beta}(0,1) \backslash \mathcal{S} \times(0,1] .$$
Our second main theorem is the following pointwise estimate.
Theorem 1.7. Suppose $\boldsymbol{\beta} \in\left(\frac{1}{2}, 1\right)^{p}$ and $u$ is the solution to (1-9). Then there exists a computable constant $C=C(n, \boldsymbol{\beta})>0$ such that, for any $Q_{p}=\left(p, t_{p}\right), Q_{q}=\left(q, t_{q}\right) \in B_{\boldsymbol{\beta}}\left(0, \frac{1}{2}\right) \backslash \mathcal{S} \times(\hat{t}, 1]($ for some $\hat{t} \in(0,1))$,
$$\begin{aligned}
\left|\left(D^{\prime}\right)^{2} u\left(Q_{p}\right)-\left(D^{\prime}\right)^{2} u\left(Q_{q}\right)\right| & \\
+\left.\sum_{j=1}^{p}| | z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}} & \left(Q_{p}\right)-\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}\left(Q_{q}\right)\left|+\left|\frac{\partial u}{\partial t}\left(Q_{p}\right)-\frac{\partial u}{\partial t}\left(Q_{q}\right)\right|\right. \\
& \leq C\left(\frac{d}{\hat{t}^{3 / 2}}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\hat{t}^{-1} \int_{0}^{d} \frac{\omega(r)}{r} d r+\frac{d}{\hat{t}^{3 / 2}} \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right),
\end{aligned}$$
and, for any $1 \leq j \leq p$,
$$\left|N_{j} D^{\prime} u\left(Q_{p}\right)-N_{j} D^{\prime} u\left(Q_{q}\right)\right| \leq C\left(\frac{d^{1 / \beta_{j}-1}}{\hat{t}^{3 / 2}}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\hat{t}^{-1} \int_{0}^{d} \frac{\omega(r)}{r} d r+\frac{d^{1 / \beta_{j}-1}}{\hat{t}^{3 / 2}} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{j}}} d r\right),$$
and, for any $1 \leq j, k \leq p$ with $j \neq k$,
$$\left|N_{j} N_{k} u\left(Q_{p}\right)-N_{j} N_{k} u\left(Q_{q}\right)\right| \leq C\left(\frac{d^{1 / \beta_{\max }-1}}{\hat{t}^{3 / 2}}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\hat{t}^{-1} \int_{0}^{d} \frac{\omega(r)}{r} d r+\frac{d^{1 / \beta_{\max }-1}}{\hat{t}^{3 / 2}} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\max }}} d r\right),$$
where $d=d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{p}, Q_{q}\right)>0$ is the parabolic $g_{\boldsymbol{\beta}}$-distance of $Q_{p}$ and $Q_{q}, \beta_{\text {max }}=\max \left\{\beta_{1}, \ldots, \beta_{p}\right\}$, and $\omega(r)$ is the oscillation of $f$ in $\mathcal{Q}_{\beta}$ under the parabolic distance $d_{\mathcal{P}, \beta}$ (see Section 2A2).

If $f \in \mathscr{C}_{\boldsymbol{\beta}}^{\boldsymbol{\alpha}, \boldsymbol{\alpha} / 2}\left(\boldsymbol{\mathcal { Q }}_{\boldsymbol{\beta}}\right)$ for some $\alpha \in\left(0, \min \left(1 / \beta_{\text {max }}-1,1\right)\right)$, then we have the following precise estimates as the parabolic analogue of Corollary 1.4.

Corollary 1.8. Suppose $\boldsymbol{\beta} \in(0,1)^{p}$ and $u \in \mathscr{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathscr{C}^{2}\left(\mathcal{Q}_{\boldsymbol{\beta}}^{\#}\right)$ satisfies (1-9). Then there exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that (see Definition 2.6 for the notations)
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}\left(B_{\beta}(0,1 / 2) \times(1 / 2,1]\right)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\frac{\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}}{\alpha\left(\min \left\{\frac{1}{\beta_{\max }}-1,1\right\}-\alpha\right)}\right) .$$

For general nonflat $\mathscr{C}_{\beta}^{\alpha, \alpha / 2}$-conical Kähler metrics $g$, we consider the linear parabolic equation
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f \quad \text { in } \mathcal{Q}_{\beta}, \quad u=\varphi \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta} .$$
We then have the following parabolic Schauder estimates as an analogue of Theorem 1.6.

Theorem 1.9. Given $\boldsymbol{\beta} \in(0,1)^{p}, f \in \mathscr{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ and $\varphi \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right)$, there exists a unique solution $u \in \mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}\left(B_{\beta}(0,1) \times(0,1]\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$ to the Dirichlet boundary value problem (1-10). For any compact subset $K \Subset B_{\boldsymbol{\beta}}(0,1)$ and $\varepsilon_{0}>0$, there exists $C=C\left(n, \boldsymbol{\beta}, \alpha, K, \varepsilon_{0}, g\right)>0$ such that the following interior Schauder estimate holds:
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(K \times\left[\varepsilon_{0}, 1\right]\right)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}\right) .$$
Furthermore, if we assume $\left.u\right|_{t=0}=u_{0} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)$, then $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(\alpha+2) / 2}\left(B_{\boldsymbol{\beta}}(0,1) \times[0,1]\right)$, and there exists a constant $C=C(n, \boldsymbol{\beta}, \alpha, g, K)>0$ such that
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}(K \times[0,1])} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}+\left\|u_{0}\right\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right)}\right) .$$

As an application of Theorem 1.9, we derive the short-time existence of the conical Kähler-Ricci flow with background metric being conical along divisors with simple normal crossings.

Let $(X, D)$ be a compact Kähler manifold, where $D=\sum_{j} D_{j}$ is a finite union of smooth divisors $\left\{D_{j}\right\}$ and $D$ has only simple normal crossings. Let $\omega_{0}$ be a $C_{\boldsymbol{\beta}}^{0, \alpha^{\prime}}(X)$-conical Kähler metric with cone angle $2 \pi \boldsymbol{\beta}$ along $D$ (see Definition 2.8), let $\hat{\omega}_{t}$ be a family of conical metrics with bounded norm $\|\hat{\omega}\|_{\mathscr{C}_{\beta}^{\alpha^{\prime}, \alpha^{\prime} / 2}}$, and let $\hat{\omega}_{0}=\omega_{0}$. We consider the complex Monge-Ampère flow
$$\frac{\partial \varphi}{\partial t}=\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi\right)^{n}}{\omega_{0}^{n}}\right)+f \quad \text { and }\left.\quad \varphi\right|_{t=0}=0$$
for some $f \in \mathscr{C}_{\beta}^{\alpha^{\prime}, \alpha^{\prime} / 2}(X \times[0,1])$.
Theorem 1.10. Given $\alpha \in\left(0, \alpha^{\prime}\right)$, there exists $T=T\left(n, \hat{\omega}, f, \alpha^{\prime}, \alpha\right)>0$ such that (1-11) admits a unique solution $\varphi \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}(X \times[0, T])$.

An immediate corollary of Theorem 1.10 is the short-time existence for the conical Kähler-Ricci flow
$$\frac{\partial \omega}{\partial t}=-\operatorname{Ric}(\omega)+\sum_{j}\left(1-\beta_{j}\right)\left[D_{j}\right],\left.\quad \omega\right|_{t=0}=\omega_{0},$$
where $\operatorname{Ric}(\omega)$ is the unique extension of the Ricci curvature of $\omega$ from $X \backslash D$ to $X$, and $\left[D_{j}\right]$ denotes the current of integration over the component $D_{j}$. In addition we assume $\omega_{0}$ is a $C_{\boldsymbol{\beta}}^{0, \alpha^{\prime}}(X, D)$-conical Kähler metric such that
$$\omega_{0}^{n}=\frac{\Omega}{\prod_{j}\left(\left|s_{j}\right|_{h_{j}}^{2}\right)^{1-\beta_{j}}},$$
where $s_{j}$ and $h_{j}$ are holomorphic sections and hermitian metrics, respectively, of the line bundle associated to $D_{j}$, and $\Omega$ is a smooth volume form.

Corollary 1.11. For any given $\alpha \in\left(0, \alpha^{\prime}\right)$, there exists a constant $T=T\left(n, \omega_{0}, \alpha, \alpha^{\prime}\right)>0$ such that the conical Kähler-Ricci flow (1-12) admits a unique solution $\omega=\omega_{t}$, where $\omega \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}(X \times[0, T])$ and, for each $t \in[0, T], \omega_{t}$ is still a conical metric with cone angle $2 \pi \beta$ along $D$.

Furthermore, $\omega$ is smooth in $X \backslash D \times(0, T]$ and the (normalized) Ricci potentials of $\omega$, by which we mean $\log \left(\omega^{n} / \omega_{0}^{n}\right)$, are still in $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}(X \times[0, T])$.

The short-time existence of the conical Kähler-Ricci flow with singularities along a smooth divisor is derived in [5] by adapting the elliptic potential techniques of Donaldson [14]. Corollary 1.11 treats the general case of conical singularities with simple normal crossings. There have been many results in the analytic aspects of the conical Ricci flow [5; 6; 15; 16; 24; 30; 43]. In [31], the conical Ricci flow on Riemann surfaces is completely classified with jumping conical structure in the limit. Such phenomena is also expected in higher dimension, but it requires much deeper and delicate technical advances both in analysis and geometry.

\section*{2. Preliminaries}

We explain the notations and give some preliminary tools which will be used later in this section.
2A. Notations. To distinguish the elliptic from parabolic norms, we will use $C$ to denote the norms in the elliptic case and $\mathscr{C}$ to denote the norms in the parabolic case.

We always assume the Hölder component $\alpha$ appearing in $C_{\boldsymbol{\beta}}^{0, \alpha}$ or $\mathscr{C}_{\boldsymbol{\beta}}^{\boldsymbol{\alpha}, \alpha / 2}$ (or other Hölder norms) is in $\left(0, \min \left\{\beta_{\max }^{-1}-1,1\right\}\right)$.

2A1. Elliptic case. We will denote $d_{\boldsymbol{\beta}}(x, y)$ to be the distance between two points $x, y \in \mathbb{C}^{n}$ under the metric $g_{\beta}$. $B_{\beta}(x, r)$ will be the metric ball under the metric induced by $g_{\beta}$ with radius $r$ and center $x$. It is well known that $\left(\mathbb{C}^{n} \backslash \mathcal{S}, g_{\boldsymbol{\beta}}\right)$ is geodesically convex, i.e., any two points $x, y \in \mathbb{C}^{n} \backslash \mathcal{S}$ can be joined by a $g_{\beta}$-minimal geodesic $\gamma$ which is disjoint from $\mathcal{S}$.

Definition 2.1. We define the $g_{\beta}$-Hölder norm of functions $u \in C^{0}\left(B_{\beta}(0, r)\right)$ for some $\alpha \in(0,1)$ as
$$\|u\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0, r)\right)}:=\|u\|_{C^{0}\left(B_{\beta}(0, r)\right)}+[u]_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0, r)\right)},$$
where the seminorm is defined as
$$[u]_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0, r)\right)}:=\sup _{x \neq y \in B_{\beta}(0, r)} \frac{|u(x)-u(y)|}{d_{\beta}(x, y)^{\alpha}} .$$
We denote by $C_{\beta}^{0, \alpha}\left(B_{\beta}(0, r)\right)$ the subspace of all continuous functions $u$ such that $\|u\|_{C_{\beta}^{0, \alpha}}<\infty$.
Definition 2.2. The $C_{\boldsymbol{\beta}}^{2, \alpha}$-norm of a function $u$ on $B_{\boldsymbol{\beta}}(0, r)=: B_{\beta}$ is defined as
$$\begin{aligned}
\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}:= & \|u\|_{C^{0}\left(B_{\beta}\right)}+\left\|\nabla_{g_{\beta}} u\right\|_{C^{0}\left(B_{\beta}, g_{\beta}\right)}+\sum_{j=1}^{p}\left\|N_{j} D^{\prime} u\right\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)} \\
& \quad+\left\|\left(D^{\prime}\right)^{2} u\right\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}+\sum_{1 \leq j \neq k \leq p}\left\|N_{j} N_{k} u\right\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}+\sum_{j=1}^{p}\left\|\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}\right\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)} .
\end{aligned}$$
We denote by $C_{\beta}^{2, \alpha}\left(B_{\beta}(0, r)\right)$ the subspace of all continuous functions $u$ such that $\|u\|_{C_{\beta}^{2, \alpha}}<\infty$.
Remark 2.3. These spaces are generalizations of those defined in [20] and are slight variations of those introduced in [14; 23].

Let us compare the Schauder estimates in [14; 23; 20] in the special case when $p=1$, i.e., the conical singularities are supported on $\mathbb{C}^{n-1}$. The Hölder space of [14] is defined using a collection of differential operators as components of $\sqrt{-1} \partial \bar{\partial}$. The collection of differential operators in our definition for $C_{\beta}^{0, \alpha}$ (see [20]) is given by
$$\left\{\frac{\partial}{\partial r}, r^{-1} \frac{\partial}{\partial \theta}, D^{\prime}, \frac{\partial^{2}}{\partial r^{2}}+r^{-1} \frac{\partial}{\partial r}+(\beta r)^{-2} \frac{\partial^{2}}{\partial \theta^{2}}, \frac{\partial}{\partial r} D^{\prime}, r^{-1} \frac{\partial}{\partial \theta} D^{\prime}\right\},$$
while those defined in [23] for the Hölder space $\mathcal{D}_{\omega}^{0, \alpha}$ gives the collection
$$\left\{\frac{\partial}{\partial r}, r^{-1} \frac{\partial}{\partial \theta}, D^{\prime}, \frac{\partial^{2}}{\partial r^{2}}+r^{-1} \frac{\partial}{\partial r}+(\beta r)^{-2} \frac{\partial^{2}}{\partial \theta^{2}}, \frac{\partial}{\partial r} D^{\prime}, r^{-1} \frac{\partial}{\partial \theta} D^{\prime}, \frac{\partial^{2}}{\partial r \partial \theta}\right\} .$$
Here the operators $D^{\prime}$ are given in Definition 1.1. There seems to a typo in the original definition of (2-1) in [23, p. 104, (16)], where the factor $r^{-1}$ is missing in the operator $r^{-1} \partial / \partial \theta D^{\prime}$ (see [32, p. 57]). It was pointed out by the referee that this typo does not affect Proposition 3.3 in [23] since the correct operator was used in the proof. The space $\mathcal{D}_{\omega}^{0, \alpha}$ is introduced in [23] as an alternative definition for the Hölder space of [14] as a consequence of the Schauder estimates in [23, Proposition 3.3]. The Schauder estimates in [23] are stronger than those established in [14] by Donaldson and later in [20] by the authors because of the additional operator $\partial^{2} / \partial r \partial \theta$ in (2-1). This also implies that the two Hölder spaces from [14] and [20] must coincide. For interested readers, we refer to the survey paper [32] for more details on the characterization of the Hölder space of [14] in terms of the operators in (2-1).

For a given set $\Omega \subset B_{\beta}(0,1)$, we define the following weighted (semi)norms.
Definition 2.4. Suppose $\sigma \in \mathbb{R}$ is a given real number and $u$ is a $C_{\beta}^{2, \alpha}$-function in $\Omega$. We will write $d_{x}=d_{\boldsymbol{\beta}}(x, \partial \Omega)$ for any $x \in \Omega$. We define the weighted (semi)norms
$$\begin{gathered}
{[u]_{C_{\beta}^{0, \alpha}(\Omega)}^{(\sigma)}=\sup _{x \neq y \in \Omega} \min \left(d_{x}, d_{y}\right)^{\sigma+\alpha} \frac{|u(x)-u(y)|}{d_{\beta}(x, y)^{\alpha}},} \\
\|u\|_{C^{0}(\Omega)}^{(\sigma)}=\sup _{x \in \Omega} d_{x}^{\sigma}|u(x)|, \quad[u]_{C_{\beta}^{1}(\Omega)}^{(\sigma)}=\sup _{x \in \Omega \backslash \mathcal{S}} d_{x}^{\sigma+1}\left(\sum_{j}\left|N_{j} u\right|(x)+\left|D^{\prime} u\right|(x)\right), \\
{[u]_{C_{\beta}^{2}(\Omega)}^{(\sigma)}=\sup _{x \in \Omega \backslash \mathcal{S}} d_{x}^{\sigma+2}|T u(x)|, \quad[u]_{C_{\beta}^{2, \alpha}(\Omega)}^{(\sigma)}=\sup _{x \neq y \in \Omega \backslash \mathcal{S}} \min \left(d_{x}, d_{y}\right)^{\sigma+2+\alpha} \frac{|T u(x)-T u(y)|}{d_{\beta}(x, y)^{\alpha}},} \\
\|u\|_{C_{\beta}^{2, \alpha}(\Omega)}^{(\sigma)}=\|u\|_{C^{0}(\Omega)}^{(\sigma)}+[u]_{C_{\beta}^{1}(\Omega)}^{(\sigma)}+[u]_{C_{\beta}^{2}(\Omega)}^{(\sigma)}+[u]_{C_{\beta}^{2, \alpha}(\Omega)}^{(\sigma)},
\end{gathered}$$
where $T$ is the collection of operators of second-order
$$\left\{\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2}}{\partial z_{j} \partial \bar{z}_{j}}, N_{j} N_{k}(j \neq k), N_{j} D^{\prime},\left(D^{\prime}\right)^{2}\right\} .$$
When $\sigma=0$, we write the norms above as $[\cdot]^{*}$ or $\|\cdot\|^{*}$ for simplicity of notation.
2A2. Parabolic case. We define $\mathcal{Q}_{\beta}=\mathcal{Q}_{\beta}(0,1)=B_{\beta}(0,1) \times(0,1]$ to be a parabolic cylinder and
$$\partial_{\mathcal{P}} \mathcal{Q}_{\beta}=\left(\overline{B_{\beta}(0,1)} \times\{0\}\right) \cup\left(\partial B_{\beta}(0,1) \times(0,1]\right)$$
to be the parabolic boundary of the cylinder $\mathcal{Q}_{\boldsymbol{\beta}}$. We write $\mathcal{S}_{\mathcal{P}}=\mathcal{S} \times[0,1]$ for the singular set and $\mathcal{Q}_{\boldsymbol{\beta}}^{\#}=\mathcal{Q}_{\boldsymbol{\beta}} \backslash \mathcal{S}_{\mathcal{P}}$ for the complement of $\mathcal{S}_{\mathcal{P}}$. For any two space-time points $Q_{i}=\left(p_{i}, t_{i}\right)$, we define their parabolic distance $d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{1}, Q_{2}\right)$ as
$$d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{1}, Q_{2}\right)=\max \left\{\sqrt{\left|t_{1}-t_{2}\right|}, d_{\boldsymbol{\beta}}\left(p_{1}, p_{2}\right)\right\} .$$

Definition 2.5. We define the $g_{\beta}$-Hölder norm of functions $u \in \mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)$ for some $\alpha \in(0,1)$ as
$$\|u\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}:=\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+[u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)},$$
where the seminorm is
$$[u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}:=\sup _{Q_{1} \neq Q_{2} \in \mathcal{Q}_{\beta}} \frac{\left|u\left(Q_{1}\right)-u\left(Q_{2}\right)\right|}{d_{\mathcal{P}, \beta}\left(Q_{1}, Q_{2}\right)^{\alpha}} .$$
We denote by $\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)$ the subspace of all continuous functions $u$ such that $\|u\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}<\infty$.
Definition 2.6. The $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(\alpha+2) / 2}$-norm of a function $u$ on $\mathscr{Q}_{\boldsymbol{\beta}}$ is defined as
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}\left(\mathcal{Q}_{\beta}\right)}:=\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\left\|\nabla_{g_{\beta}} u\right\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}, g_{\beta}\right)}+\|\mathcal{T} u\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)},$$
where $\mathcal{T}$ is the collection of all the second-order operators in (2-2) with the first-order operator $\partial / \partial t$.
For a given set $\Omega \subset \mathcal{Q}_{\beta}$ we define the following weighted (semi)norms.
Definition 2.7. Suppose $\sigma \in \mathbb{R}$ is a real number and $u$ is a $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(\alpha+2) / 2}$-function in $\Omega$. We will write $d_{\mathcal{P}, Q}=d_{\mathcal{P}, \beta}\left(Q, \partial_{\mathcal{P}} \Omega\right)$ for any $Q \in \Omega$. We define the weighted (semi)norms
$$\begin{gathered}
{[u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\Omega)}^{(\sigma)}=\sup _{Q_{1} \neq Q_{2} \in \Omega} \min \left(d_{\mathcal{P}, Q_{1}}, d_{\mathcal{P}, Q_{2}}\right)^{\sigma+\alpha} \frac{\left|u\left(Q_{1}\right)-u\left(Q_{2}\right)\right|}{d_{\mathcal{P}, \beta}\left(Q_{1}, Q_{2}\right)^{\alpha}}, \quad\|u\|_{\mathscr{C}^{0}(\Omega)}^{(\sigma)}=\sup _{Q \in \Omega} d_{\mathcal{P}, Q}^{\sigma}|u(Q)|,} \\
{[u]_{\mathscr{C}_{\beta}^{1}(\Omega)}^{(\sigma)}=\sup _{Q \in \Omega \backslash \mathcal{S}_{\mathcal{P}}} d_{\mathcal{P}, Q}^{\sigma+1}\left(\sum_{j}\left|N_{j} u\right|(Q)+\left|D^{\prime} u\right|(Q)\right), \quad[u]_{\mathscr{C}_{\beta}^{2,1}(\Omega)}^{(\sigma)}=\sup _{Q \in \Omega \backslash \mathcal{S}_{\mathcal{P}}} d_{\mathcal{P}, Q}^{\sigma+2}|\mathcal{T} u(Q)|,} \\
{[u]_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}(\Omega)}^{(\sigma)}=\sup _{Q_{1} \neq Q_{2} \in \Omega \backslash \mathcal{S}_{\mathcal{P}}} \min \left(d_{\mathcal{P}, Q_{1}}, d_{\mathcal{P}, Q_{2}}\right)^{\sigma+2+\alpha} \frac{\left|\mathcal{T} u\left(Q_{1}\right)-\mathcal{T} u\left(Q_{2}\right)\right|}{d_{\mathcal{P}, \beta}\left(Q_{1}, Q_{2}\right)^{\alpha}},} \\
\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}(\Omega)}^{(\sigma)}=\|u\|_{\mathscr{C}^{0}(\Omega)}^{(\sigma)}+[u]_{\mathscr{C}_{\beta}^{1}(\Omega)}^{(\sigma)}+[u]_{\mathscr{C}_{\beta}^{2,1}(\Omega)}^{(\sigma)}+[u]_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}(\Omega)}^{(\sigma)} .
\end{gathered}$$
When $\sigma=0$, we write the norms above as $[\cdot]^{*}$ or $\|\cdot\|^{*}$ for simplicity of notation.
2A3. Compact Kähler manifolds. Let $(X, D)$ be a compact Kähler manifold with a divisor $D=\sum_{j} D_{j}$ with simple normal crossings, i.e., on an open coordinate chart $\left(U, z_{j}\right)$ of any $x \in D, D \cap U$ is given by $\left\{z_{1} \cdots z_{p}=0\right\}$ and $D_{j} \cap U=\left\{z_{j}=0\right\}$ for any component $D_{j}$ of $D$. We fix a finite cover $\left\{U_{a}, z_{a, j}\right\}$ of $D$.
Definition 2.8. A (singular) Kähler metric $\omega$ is called a conical metric with cone angle $2 \pi \boldsymbol{\beta}$ along $D$ if $\omega$ is equivalent to $\omega_{\beta}$ locally on any coordinate chart $U_{a}$ under the coordinates $\left\{z_{a, j}\right\}$, where $\omega_{\beta}$ is the standard cone metric (1-1) with cone angle $2 \pi \beta_{j}$ along $\left\{z_{a, j}=0\right\}$, and $\omega$ is a smooth Kähler metric in the usual sense on $X \backslash \bigcup_{a} U_{a}$.

A conical metric $\omega$ is in $C_{\boldsymbol{\beta}}^{0, \alpha}(X, D)$ if $\omega$ is in $C_{\boldsymbol{\beta}}^{0, \alpha}\left(U_{a}\right)$ for each $a$ and $\omega$ is smooth in the usual sense on $X \backslash \bigcup_{a} U_{a}$. Similarly we can define the $\mathscr{C}_{\beta}^{\alpha, \alpha / 2}$-conical Kähler metrics on $X \times[0,1]$.

Definition 2.9. A continuous function $u \in C^{0}(X)$ is said to be in $C_{\beta}^{0, \alpha}(X, D)$ if $u$ is in $C_{\beta}^{0, \alpha}\left(U_{a}\right)$ locally on each $U_{a}$ and $u$ is $C^{0, \alpha}$-continuous in the usual sense on $X \backslash \bigcup_{a} U_{a}$. We define the $C_{\beta}^{0, \alpha}(X, D)$-norm of $u$
$$\|u\|_{C_{\beta}^{0, \alpha}(X, D)}:=\|u\|_{C^{0, \alpha}\left(X \backslash \bigcup_{a} U_{a}, \omega\right)}+\sum_{a}\|u\|_{C_{\beta}^{0, \alpha}\left(U_{a}\right)} .$$
The $C_{\beta}^{0, \alpha}(X, D)$-norm depends on the choice of finite covers, and another cover yields a different but equivalent norm. The space $C_{\beta}^{0, \alpha}(X, D)$ is clearly independent of the choice of finite covers.

The other spaces and norms like $C_{\beta}^{2, \alpha}(X, D), \mathscr{C}_{\beta}^{\alpha, \alpha / 2}(X \times[0,1], D)$, etc., can be defined similarly.
2B. A useful lemma. We will frequently use the following elementary estimates from [20]. We write $B_{\mathbb{C}}(0, r)$ for the Euclidean ball in $\mathbb{C}$ with center 0 and radius $r>0$.

Lemma 2.10 (Lemma 2.2 in [20]). Given $r \in(0,1]$, suppose $v \in C^{0}\left(B_{\mathbb{C}}(0, r)\right) \cap C^{2}\left(B_{\mathbb{C}}(0, r) \backslash\{0\}\right)$ satisfies
$$|z|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2} v}{\partial z \partial \bar{z}}=F \quad \text { in } B_{\mathbb{C}}(0, r) \backslash\{0\}$$
for some $F \in L^{\infty}\left(B_{\mathbb{C}}(0, r)\right)$. Then we have the following pointwise estimate for any $z \in B_{\mathbb{C}}\left(0, \frac{9}{10} r\right) \backslash\{0\}$ :
$$\left|\frac{\partial v}{\partial z}(z)\right| \leq C \frac{\|v\|_{L^{\infty}}}{r}+C\|F\|_{L^{\infty}} \cdot \begin{cases}r^{2 \beta_{1}-1} & \text { if } \beta_{1} \in\left(\frac{1}{2}, 1\right), \\ |z|^{2 \beta_{1}-1} & \text { if } \beta_{1} \in\left(0, \frac{1}{2}\right), \\ \left|\log \left(\frac{|z|}{2 r}\right)\right| & \text { if } \beta_{1}=\frac{1}{2},\end{cases}$$
where the $L^{\infty}$-norms are taken in $B_{\mathbb{C}}(0, r)$ and $C>0$ is a uniform constant depending only on the angle $\beta_{1}$.

Finally we remark that the idea of the proof of the estimates in Theorems 1.2 and 1.7 is the same for general $2 \leq p \leq n$. To explain the argument more clearly, we prove the theorems assuming $p=2$, i.e., the cone metric of $\omega_{\beta}$ is singular along the two components $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$.

\section*{3. Elliptic estimates}

In this section, we will prove Theorems 1.2 and 1.6, the Schauder estimates for the Laplace equation (1-2). To begin with, we first observe the simple $C^{0}$-estimate based on the maximum principle.

Suppose $u \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\beta}(0,1)}\right)$ satisfies the equation
$$\begin{cases}\Delta_{\beta} u=0 & \text { in } B_{\beta}(0,1) \backslash \mathcal{S}, \\ u=\varphi & \text { on } \partial B_{\beta}(0,1)\end{cases}$$
for some $\varphi \in C^{0}\left(\partial B_{\beta}(0,1)\right)$, then we have the following lemma.
Lemma 3.1. We have the maximum principle
$$\inf _{\partial B_{\beta}(0,1)} \varphi \leq \inf _{B_{\beta}(0,1)} u \leq \sup _{B_{\beta}(0,1)} u \leq \sup _{\partial B_{\beta}(0,1)} \varphi .$$
Proof. Consider the functions $\tilde{u}_{\epsilon}=u \pm \epsilon\left(\log \left|z_{1}\right|^{2}+\log \left|z_{2}\right|^{2}\right)$ for any $\epsilon>0$. By the proof of Lemma 2.1 in [20], (3-2) is established. \(\square\)

The next step is to show (3-1) is solvable for suitable boundary values.
3A. Conical harmonic functions.
3A1. Smooth approximating metrics. Let $\epsilon \in(0,1)$ be a given small positive number and define a smooth approximating Kähler metric $g_{\epsilon}$ on $B_{\beta}(0,1)$ as
$$g_{\epsilon}=\beta_{1}^{2} \frac{\sqrt{-1} d z_{1} \wedge d \bar{z}_{1}}{\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}}}+\beta_{2}^{2} \frac{\sqrt{-1} d z_{2} \wedge d \bar{z}_{2}}{\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}}}+\sum_{j=3}^{n} \sqrt{-1} d z_{j} \wedge d \bar{z}_{j} .$$
The $g_{\epsilon}$ are product metrics on $\mathbb{C} \times \mathbb{C} \times \mathbb{C}^{n-2}$. It is clear that their Ricci curvatures satisfy
$$\operatorname{Ric}\left(g_{\epsilon}\right)=\sqrt{-1} \partial \bar{\partial} \log \left(\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}}\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}}\right) \geq 0 .$$

Let $u_{\epsilon} \in C^{2}\left(B_{\beta}(0,1)\right)$ be the solution to the equation
$$\Delta_{g_{\epsilon}} u_{\epsilon}=0 \quad \text { in } B_{\beta}(0,1) \quad \text { and } \quad u_{\epsilon}=\varphi \quad \text { on } \partial B_{\beta}(0,1)$$
with a given $\varphi \in C^{0}\left(\partial B_{\beta}(0,1)\right)$. Note that the metric balls $B_{\beta}(0,1)$ and $B_{g_{\epsilon}}(0,1)$ are uniformly close when $\epsilon$ is sufficiently small, so for the following estimates we will work on $B_{\beta}(0,1)$.

Let $u_{\epsilon}$ be the harmonic function for $\Delta_{\epsilon}=\Delta_{g_{\epsilon}}$ as in (3-4), which we may assume without loss of generality is positive by replacing $u_{\epsilon}$ by $u_{\epsilon}-\inf u_{\epsilon}$ if necessary. We will study the Cheng-Yau-type gradient estimate of $u_{\epsilon}$ and the estimate of $\Delta_{1, \epsilon} u_{\epsilon}:=\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}}\left(\partial^{2} u_{\epsilon} / \partial z_{1} \partial \bar{z}_{1}\right)$. Let us recall Cheng-Yau's gradient estimate first.

In Sections 3A2-3A5, for convenience of notation, we will omit the subscript $\epsilon$ in $g_{\epsilon}$ and $u_{\epsilon}$ in the proofs of the lemmas.

3A2. Cheng-Yau gradient estimate revisited. We assume $u_{\epsilon}>0$, as otherwise we could consider the function $u_{\epsilon}+\delta$ for some $\delta>0$ and then let $\delta \rightarrow 0$. We fix a metric ball $B_{g_{\epsilon}}(p, R) \subset B_{\beta}(0,1)$ centered at some point $p \in B_{\beta}(0,1)$. Since $\operatorname{Ric}\left(g_{\epsilon}\right) \geq 0$, the Cheng-Yau gradient estimate holds for $\Delta_{g_{\epsilon}}$-harmonic functions.

Lemma 3.2 [10]. Let $u_{\epsilon} \in C^{2}(B(p, R))$ be a positive $\Delta_{g_{\epsilon}}$-harmonic function. There exists a uniform constant $C=C(n)>0$ such that (the metric balls are taken under the metric $g_{\epsilon}$ )
$$\sup _{x \in B(p, 3 R / 4)}\left|\nabla u_{\epsilon}\right|_{g_{\epsilon}}(x) \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u_{\epsilon}}{R} .$$

As we mentioned above, we will omit the $\epsilon$ in the subscript of $u_{\epsilon}$ and $g_{\epsilon}$. The proof of the lemma is standard [10]. For completeness and to motivate the proofs of Lemmas 3.3 and 3.4, we sketch a proof. Defining $f=\log u$, it can be calculated that
$$\Delta f=\frac{\Delta u}{u}-\frac{|\nabla u|^{2}}{u^{2}}=-|\nabla f|^{2} .$$
Then by Bochner's formula we have
$$\begin{aligned}
\Delta|\nabla f|^{2} & =|\nabla \nabla f|^{2}+|\nabla \bar{\nabla} f|^{2}+2 \operatorname{Re}\langle\nabla f, \bar{\nabla} \Delta f\rangle+\operatorname{Ric}(\nabla f, \bar{\nabla} f) \\
& \left.\geq|\nabla \bar{\nabla} f|^{2}-\left.2 \operatorname{Re}\langle\nabla f, \bar{\nabla}| \nabla f\right|^{2}\right\rangle .
\end{aligned}$$

Let $\phi:[0,1] \rightarrow[0,1]$ be a standard cut-off function such that $\left.\phi\right|_{[0,3 / 4]}=1, \phi_{[5 / 6,1]}=0$ and $0<\phi<1$ otherwise. Let $r(x)=d_{g_{\epsilon}}(p, x)$ be the distance function to $p$ under the metric $g=g_{\epsilon}$. By abusing notation, we also write $\phi(x)=\phi(r(x) / R)$. It can be calculated by Laplacian comparison and the Bochner formula (3-7) that, at the (positive) maximum point $p_{\text {max }}$ of $H:=\phi^{2}|\nabla f|^{2}$,
$$\frac{2}{n} H^{2}-\frac{4\left|\phi^{\prime}\right|}{R} H^{3 / 2}-\frac{8\left(\phi^{\prime}\right)^{2}}{R^{2}} H+\frac{2 H}{R^{2}}\left((2 n-1) \phi \phi^{\prime}+\phi \phi^{\prime \prime}+\left(\phi^{\prime}\right)^{2}\right) \leq 0 .$$
Therefore, for any $x \in B\left(p, \frac{3}{4} R\right)$,
$$\frac{|\nabla u|^{2}}{u^{2}}(x)=|\nabla f(x)|^{2}=H(x) \leq H\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$
3A3. Laplacian estimate in singular directions. We will prove the estimates of
$$\Delta_{j, \epsilon} u_{\epsilon}:=\left(\left|z_{j}\right|^{2}+\epsilon\right)^{1-\beta_{j}} \frac{\partial u_{\epsilon}}{\partial z_{j} \partial \bar{z}_{j}}$$
for a $\Delta_{g_{\epsilon}}$-harmonic function $u_{\epsilon}$.
Lemma 3.3. Under the same assumptions as in Lemma 3.2, along the "bad" directions $z_{1}$ and $z_{2}$, we have that $\Delta_{1, \epsilon} u_{\epsilon}$ and $\Delta_{2, \epsilon} u_{\epsilon}$ satisfy the estimates
$$\sup _{x \in B(p, R / 2)}\left(\left|\Delta_{1, \epsilon} u_{\epsilon}\right|(x)+\left|\Delta_{2, \epsilon} u_{\epsilon}\right|(x)\right) \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u_{\epsilon}}{R^{2}} .$$

As in the proof of Cheng-Yau gradient estimates, we will work on the function $f=f_{\epsilon}=\log u$, and we only need to prove the estimate for $\Delta_{1, \epsilon} u_{\epsilon}$. We write $\Delta_{1, \epsilon} f:=\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}}\left(\partial^{2} f / \partial z_{1} \partial \bar{z}_{1}\right)$.

As above, we will omit the subscript $\epsilon$ in $\Delta_{1, \epsilon} f$. We first observe that
$$\Delta_{1} \Delta_{g_{\epsilon}} f=\Delta_{g_{\epsilon}} \Delta_{1} f .$$
Equation (3-10) can be checked from the definitions using the property that $g_{\epsilon}$ is a product metric. Indeed
$$\begin{aligned}
\Delta_{1} \Delta_{g_{\epsilon}} f & =\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}}\left(\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2} f}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}} \frac{\partial^{2} f}{\partial z_{2} \partial \bar{z}_{2}}+\sum_{j} \frac{\partial^{2} f}{\partial z_{j} \partial \bar{z}_{j}}\right) \\
& =\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}} \Delta_{1} f+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}} \Delta_{1} f+\sum_{j=3}^{n} \frac{\partial^{2}}{\partial z_{j} \partial \bar{z}_{j}} \Delta_{1} f=\Delta_{g_{\epsilon}} \Delta_{1} f .
\end{aligned}$$
On the other hand, note that $\Delta_{g_{\epsilon}} f=\Delta_{g} f=-|\nabla f|^{2}$ by (3-6). Choosing a normal frame $\left\{e_{1}, \ldots, e_{n}\right\}$ at some point $x$ such that $d g(x)=0$ and $\Delta_{1} f=f_{1 \overline{1}}$, we calculate
$$\begin{aligned}
\Delta_{1}|\nabla f|^{2}=\left(f_{j} f_{\bar{j}}\right)_{1 \overline{1}} & =f_{j 1} f_{\bar{j} \overline{1}}+f_{j \overline{1}} f_{\bar{j} 1}+f_{j 1 \overline{1}} f_{\bar{j}}+f_{j} f_{\bar{j} 1 \overline{1}} \\
& =f_{j 1} f_{\bar{j} \overline{1}}+f_{j \overline{1}} f_{\bar{j} 1}+f_{j} f_{\overline{1} 1 \bar{j}}+f_{\bar{j}}\left(f_{1 \overline{1} j}+f_{m} R_{1 \bar{m} j \overline{1}}\right) \\
& =\left|\nabla_{1} \nabla f\right|^{2}+\left|\nabla_{1} \bar{\nabla} f\right|^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle+f_{m} f_{\bar{j}} R_{1 \overline{1} j \bar{m}} \\
& \geq\left(\Delta_{1} f\right)^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle .
\end{aligned}$$

Then
$$\Delta\left(-\Delta_{1} f\right)=-\Delta_{1} \Delta f=\Delta_{1}|\nabla f|^{2} \geq\left(\Delta_{1} f\right)^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle .$$
Let $\varphi:[0,1] \rightarrow[0,1]$ be a standard cut-off function such that $\left.\varphi\right|_{[0,1 / 2]}=1$ and $\left.\varphi\right|_{[2 / 3,1]}=0$. We also define $\varphi(x)=\varphi(r(x) / R)$. Then consider the function $G:=\varphi^{2} \cdot\left(-\Delta_{1} f\right)$. We calculate
$$\begin{aligned}
\Delta G & =\Delta\left(\varphi^{2}\left(-\Delta_{1} f\right)\right) \\
& =\varphi^{2} \Delta\left(-\Delta_{1} f\right)+2 \operatorname{Re}\left\langle\nabla \varphi^{2}, \bar{\nabla}\left(-\Delta_{1} f\right)\right\rangle+\left(-\Delta_{1} f\right) \Delta \varphi^{2} \\
& \geq \varphi^{2}\left(\left(\Delta_{1} f\right)^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle\right)+2 \operatorname{Re}\left\langle\nabla \varphi^{2}, \bar{\nabla}\left(-\Delta_{1} f\right)\right\rangle+\left(-\Delta_{1} f\right) \Delta \varphi^{2} .
\end{aligned}$$
We want to estimate the upper bound of $G$. If the maximum value of $G=\varphi^{2}\left(-\Delta_{1} f\right)$ is negative, we are done. So we assume the maximum of $G$ on $B(p, R)$ is positive, which is achieved at some point $p_{\text {max }} \in B\left(p, \frac{2}{3} R\right)$. Hence, at $p_{\text {max }}$ we have $\left(-\Delta_{1} f\right)>0$. By Laplacian comparison, $\Delta r \leq(2 n-1) / r$, and we get, at $p_{\text {max }}$,
$$\Delta \varphi^{2} \geq \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) .$$
Thus, at $p_{\text {max }}$, the last term on the right-hand side of (3-12) is greater than or equal to
$$\left(-\Delta_{1} f\right) \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) .$$
Substituting this into (3-12), it follows that, at $p_{\text {max }}$, we have $\Delta G \leq 0$ and $\nabla \Delta_{1} f=-2 \varphi^{-1} \Delta_{1} f \nabla \varphi$, and hence
$$\begin{aligned}
0 & \geq \Delta G \\
& \geq \varphi^{2}\left(\Delta_{1} f\right)^{2}+2 \varphi^{2} \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle+4 \varphi \operatorname{Re}\left\langle\nabla \varphi, \bar{\nabla}\left(-\Delta_{1} f\right)\right\rangle+\left(-\Delta_{1} f\right) \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \\
& \geq \varphi^{2}\left(\Delta_{1} f\right)^{2}-4 \varphi\left|\Delta_{1} f\right||\nabla f||\nabla \varphi|+8 \Delta_{1} f|\nabla \varphi|^{2}+\left(-\Delta_{1} f\right) \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \\
& =\frac{G^{2}}{\varphi^{2}}-4 \varphi^{-1} G|\nabla f||\nabla \varphi|-8 G \frac{|\nabla \varphi|^{2}}{\varphi^{2}}+\frac{2 G}{R^{2} \varphi^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \\
& \geq \frac{G^{2}}{\varphi^{2}}-4 \frac{\left|\varphi^{\prime}\right||\nabla f|}{R \varphi} G-8 \frac{\left|\varphi^{\prime}\right|^{2}}{R^{2} \varphi^{2}} G+\frac{2 G}{R^{2} \varphi^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) .
\end{aligned}$$
Therefore, at $p_{\max } \in B\left(p, \frac{2}{3} R\right)$,
$$G^{2}-4 \frac{\varphi\left|\varphi^{\prime} \nabla f\right|}{R} G-8 \frac{\left|\varphi^{\prime}\right|^{2}}{R^{2}} G+\frac{2 G}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \leq 0,$$
and combining (3-8) and the fact that $\varphi, \varphi^{\prime}, \varphi^{\prime \prime}$ are all uniformly bounded, we can get, at $p_{\max }$,
$$G^{2} \leq C(n) R^{-2} G \quad \Longrightarrow \quad G\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$
Then, for any $x \in B\left(p, \frac{1}{2} R\right)$, where $\varphi=1$, we have
$$-\Delta_{1} f(x)=G(x) \leq G\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$

Moreover, recall that $f=\log u$ and $-\Delta_{1} f=-\Delta_{1} u / u+\left|\nabla_{1} f\right|^{2}$, therefore it follows that
$$\sup _{x \in B(p, R / 2)}\left(-\frac{\Delta_{1} u}{u}(x)\right) \leq \frac{C(n)}{R^{2}} .$$
This in particular implies that
$$\sup _{x \in B(p, R / 2)}\left(-\Delta_{1} u(x)\right) \leq C(n) \frac{\operatorname{osc}_{B(p, R / 2)} u}{R^{2}} \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .$$

On the other hand, consider the function $\hat{u}=\max _{B(p, R)} u-u$, which is still a positive $g_{\epsilon}$-harmonic function with $\Delta_{g} \hat{u}=\Delta_{g_{\epsilon}} \hat{u}=0$. Applying (3-15) to the function $\hat{u}$, we get
$$\sup _{x \in B(p, R / 2)}\left(\frac{\Delta_{1} u(x)}{\max _{B(p, R)} u-u(x)}\right)=\sup _{x \in B(p, R / 2)}\left(-\frac{\Delta_{1} \hat{u}}{\hat{u}}(x)\right) \leq \frac{C(n)}{R^{2}},$$
which yields
$$\sup _{x \in B(p, R / 2)} \Delta_{1} u(x) \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .$$
Combining (3-18) and (3-16), we get
$$\sup _{x \in B(p, R / 2)}\left|\Delta_{1} u\right|(x) \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .$$
3A4. Mixed derivatives estimates. In this subsection we will estimate the mixed derivatives
$$\left|\nabla_{1} \nabla_{2} f\right|^{2}=\frac{\partial^{2} f}{\partial z_{1} \partial z_{2}} \overline{\frac{\partial^{2} f}{\partial z_{1} \partial z_{2}}} g^{1 \overline{1}} g^{2 \overline{2}} \quad \text { and } \quad\left|\nabla_{1} \nabla_{\overline{2}} f\right|^{2}=\frac{\partial^{2} f}{\partial z_{1} \partial \bar{z}_{2}} \overline{\frac{\partial^{2} f}{\partial z_{1} \partial \bar{z}_{2}}} g^{1 \overline{1}} g^{2 \overline{2}} \text {, }$$
where as before $f=\log u$ and $u$ is a positive harmonic function of $\Delta_{g_{\epsilon}}$. Here for simplicity, we omit the subscript $\epsilon$ in $u_{\epsilon}, f_{\epsilon}$ and $g_{\epsilon}$. Observing that since $g_{\epsilon}=g$ is a product metric with the nonzero components $g_{k \bar{k}}$ depending only on $z_{k}$, it follows that the curvature tensor
$$R_{i \bar{j} k \bar{l}}=-\frac{\partial^{2} g_{i \bar{j}}}{\partial z_{k} \partial \bar{z}_{l}}+g^{p \bar{q}} \frac{\partial g_{i \bar{q}}}{\partial z_{k}} \frac{\partial g_{p \bar{j}}}{\partial \bar{z}_{l}}$$
vanishes unless $i=j=k=l \in\{1,2\}$ and also $R_{i \bar{i} \bar{i}} \geq 0$ for all $i=1, \ldots, n$.
We fix some notation: we will write $f_{12}=\nabla_{1} \nabla_{2} f$ (in fact this is just the ordinary derivative of $f$ with respect to $g$, since $g$ is a product metric), $\left|f_{12}\right|_{g}^{2}=\left|\nabla_{1} \nabla_{2} f\right|_{g}^{2}$, etc.

Let us first recall that (3-11) implies
$$\begin{aligned}
& \Delta\left(-\Delta_{1} f-\Delta_{2} f\right) \\
& =\sum_{k=1}^{n}\left(g^{1 \overline{1}} g^{k \bar{k}} f_{1 k} f_{\overline{1} \bar{k}}+g^{1 \overline{1}} g^{k \bar{k}} f_{1 \bar{k}} f_{\overline{1} k}+g^{2 \overline{2}} g^{k \bar{k}} f_{2 k} f_{\overline{2} \bar{k}}+g^{2 \overline{2}} g^{k \bar{k}} f_{2 \bar{k}} f_{k \overline{2}}\right) \\
& \quad-2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(-\Delta_{1} f-\Delta_{2} f\right)\right\rangle+f_{1} f_{\overline{1}} g^{1 \overline{1}} g^{1 \overline{1}} R_{1 \overline{1} 1 \overline{1}}+f_{2} f_{\overline{2}} g^{2 \overline{2}} g^{2 \overline{2}} R_{2 \overline{2} 2 \overline{2}} \\
& \geq \sum_{k=1}^{n}\left(\left|\nabla_{1} \nabla_{k} f\right|^{2}+\left|\nabla_{1} \nabla_{\bar{k}} f\right|^{2}+\left|\nabla_{2} \nabla_{k} f\right|^{2}+\left|\nabla_{2} \nabla_{\bar{k}} f\right|^{2}\right)-2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(-\Delta_{1} f-\Delta_{2} f\right)\right\rangle
\end{aligned}$$

Next we calculate $\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2}$. For convenience of notation we will write $f^{12}=f_{\overline{1} \overline{2}} g^{1 \overline{1}} g^{2 \overline{2}}$, and hence $\left|\nabla_{1} \nabla_{2} f\right|^{2}=f_{12} f^{12}$. We calculate
$$\begin{aligned}
\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2} & =g^{k \bar{l}}\left(f_{12} f^{12}\right)_{k \bar{l}}=g^{k \bar{k}}\left(f_{12} f^{12}\right)_{k \bar{k}} \\
& =g^{k \bar{k}}\left(f_{12 k \bar{k}} f^{12}+f_{12 k} f_{, \bar{k}}^{12}+f_{12 \bar{k}} f_{, k}^{12}+f_{12} f_{, k \bar{k}}^{12}\right) .
\end{aligned}$$
The first term on the right-hand side of (3-21) is (by Ricci identities and switching the indices)
$$\begin{aligned}
g^{k \bar{k}} f^{12}\left(f_{k 1 \bar{k} 2}\right. & \left.+g^{m \bar{m}} f_{m 1} R_{k \bar{m} 2 \bar{k}}+g^{m \bar{m}} f_{k m} R_{1 \bar{m} 2 \bar{k}}\right) \\
& =g^{k \bar{k}} f^{12}\left(f_{k \bar{k} 12}+g^{m \bar{m}} f_{m 2} R_{k \bar{m} 1 \bar{k}}+g^{m \bar{m}} f_{m} R_{k \bar{m} 1 \bar{k}}+g^{m \bar{m}} f_{m 1} R_{k \bar{m} 2 \bar{k}}+g^{m \bar{m}} f_{k m} R_{1 \bar{m} 2 \bar{k}}\right) \\
& =g^{k \bar{k}} f^{12}\left(f_{k \bar{k} 12}+g^{m \bar{m}} f_{m 2} R_{k \bar{m} 1 \bar{k}}+g^{m \bar{m}} f_{m 1} R_{k \bar{m} 2 \bar{k}}\right) \\
& =g^{k \bar{k}} f^{12} f_{k \bar{k} 12}+g^{1 \overline{1}} g^{1 \overline{1}} f^{12} f_{21} R_{1 \overline{1} 1 \overline{1}}+g^{2 \overline{2}} g^{2 \overline{2}} f^{12} f_{12} R_{2 \overline{2} 2 \overline{2}},
\end{aligned}$$
and the last term on the right-hand side of (3-21) is the conjugate of the first term; hence we get
$$\begin{aligned}
& \Delta\left|\nabla_{1} \nabla_{2} f\right|^{2}=2 \operatorname{Re}\left(f^{12}(\Delta f)_{12}\right)+2 f^{12} f_{12}\left(g^{1 \overline{1}} g^{1 \overline{1}} R_{1 \overline{1} \overline{1} \overline{1}}+g^{2 \overline{2}} g^{2 \overline{2}} R_{2 \overline{2} 2 \overline{2}}\right) \\
&+g^{k \bar{k}} f_{12 k} f_{, \bar{k}}^{12}+g^{k \bar{k}} f_{12 \bar{k}} f_{, k}^{12} .
\end{aligned}$$
Recall from (3-6) that $\Delta f=-|\nabla f|^{2}$; hence the first term on the right-hand side of (3-23) is
$$\begin{aligned}
2 \operatorname{Re}\left(f^{12}(\Delta f)_{12}\right) & =2 \operatorname{Re}\left(f^{12}\left(-|\nabla f|^{2}\right)_{12}\right) \\
& =-2 \operatorname{Re}\left(f^{12} g^{k \bar{k}}\left(f_{k 12} f_{\bar{k}}+f_{k 1} f_{\bar{k} 2}+f_{k 2} f_{\bar{k} 1}+f_{k} f_{\bar{k} 12}\right)\right) \\
& =-2 \operatorname{Re}\left(f^{12} g^{k \bar{k}}\left(f_{12 k} f_{\bar{k}}+f_{k 1} f_{\bar{k} 2}+f_{k 2} f_{\bar{k} 1}+f_{k} f_{12 \bar{k}}-f_{k} f_{m} R_{1 \bar{m} 2 k} g^{m \bar{m}}\right)\right) \\
& \left.=-\left.4 \operatorname{Re}\langle\nabla f, \bar{\nabla}| \nabla_{1} \nabla_{2} f\right|^{2}\right\rangle-2 \operatorname{Re}\left(f^{12} g^{k \bar{k}} f_{k 1} f_{2 \bar{k}}+f^{12} g^{k \bar{k}} f_{k 2} f_{\bar{k} 1}\right) .
\end{aligned}$$
Combining (3-24) and (3-23), we get
$$\begin{aligned}
\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2} \geq-4 \operatorname{Re}\langle\nabla f, \bar{\nabla}| & \left.\left.\nabla_{1} \nabla_{2} f\right|^{2}\right\rangle+\sum_{k}\left(f_{12 k} f^{12 k}+f_{12 \bar{k}} f^{12 \bar{k}}\right) \\
& -2 \sum_{k}\left(\left|\nabla_{1} \nabla_{2} f\right|\left|\nabla_{1} \nabla_{k} f\right|\left|\nabla_{2} \nabla_{\bar{k}} f\right|+\left|\nabla_{1} \nabla_{2} f\right|\left|\nabla_{2} \nabla_{k} f\right|\left|\nabla_{1} \nabla_{\bar{k}} f\right|\right) .
\end{aligned}$$
On the other hand, by Kato's inequality we have
$$\begin{aligned}
\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2} & =2\left|\nabla_{1} \nabla_{2} f\right| \Delta\left|\nabla_{1} \nabla_{2} f\right|+2|\nabla| \nabla_{1} \nabla_{2} f| |^{2} \\
& \leq 2\left|\nabla_{1} \nabla_{2} f\right| \Delta\left|\nabla_{1} \nabla_{2} f\right|+\sum_{k}\left|\nabla_{k} \nabla_{1} \nabla_{2} f\right|^{2}+\left|\nabla_{\bar{k}} \nabla_{1} \nabla_{2} f\right|^{2} \\
& =2\left|\nabla_{1} \nabla_{2} f\right| \Delta\left|\nabla_{1} \nabla_{2} f\right|+\sum_{k} f_{12 k} f^{12 k}+f_{12 \bar{k}} f^{12 \bar{k}} .
\end{aligned}$$
Combining (3-25) and (3-26), it follows that
$$\Delta\left|\nabla_{1} \nabla_{2} f\right| \geq-2 \operatorname{Re}\langle\nabla f, \bar{\nabla}| \nabla_{1} \nabla_{2} f| \rangle-\sum_{k}\left(\left|\nabla_{1} \nabla_{k} f\right|\left|\nabla_{2} \nabla_{\bar{k}} f\right|+\left|\nabla_{2} \nabla_{k} f\right|\left|\nabla_{1} \nabla_{\bar{k}} f\right|\right) .$$

Combining (3-20) and (3-27) and applying the Cauchy-Schwarz inequality, we have
$$\begin{aligned}
\Delta\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right) \geq- & 2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)\right\rangle \\
& +\sum_{k=1}^{n}\left(\left|\nabla_{1} \nabla_{k} f\right|^{2}+\left|\nabla_{1} \nabla_{\bar{k}} f\right|^{2}+\left|\nabla_{2} \nabla_{k} f\right|^{2}+\left|\nabla_{2} \nabla_{\bar{k}} f\right|^{2}\right) .
\end{aligned}$$
Note that the sum on the right-hand side of (3-27) is (recall under our notation $\left|\nabla_{1} \nabla_{\overline{1}} f\right|^{2}=\left(\Delta_{1} f\right)^{2}$ ) greater than or equal to
$$\left|\nabla_{1} \nabla_{2} f\right|^{2}+\left|-\Delta_{1} f\right|^{2}+\left|-\Delta_{2} f\right|^{2} \geq \frac{1}{12}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)^{2},$$
so we get the equation
$$\begin{aligned}
\Delta\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right) \geq-2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(\left|\nabla_{1} \nabla_{2} f\right|\right.\right. & \left.\left.+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)\right\rangle \\
& +\frac{1}{12}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)^{2} .
\end{aligned}$$
Write
$$Q=\eta^{2}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)=: \eta^{2} Q_{1},$$
where $\eta(x)=\tilde{\eta}(r(x) / R)$ and $\tilde{\eta}$ is a cut-off function such that $\left.\tilde{\eta}\right|_{[0,1 / 3]}=1$ and $\left.\tilde{\eta}\right|_{[1 / 2,1]}=0$. The following arguments are similar to the previous two cases. We calculate
$$\begin{aligned}
\Delta Q & =\eta^{2} \Delta Q_{1}+2 \operatorname{Re}\left\langle\nabla \eta^{2}, \nabla Q_{1}\right\rangle+Q_{1} \Delta \eta^{2} \\
& \geq-2 \eta^{2} \operatorname{Re}\left\langle\nabla f, \bar{\nabla} Q_{1}\right\rangle+2 \operatorname{Re}\left\langle\nabla \eta^{2}, \nabla Q_{1}\right\rangle+\frac{1}{12} \eta^{2} Q_{1}^{2}+Q_{1} \Delta \eta^{2} .
\end{aligned}$$
Apply the maximum principle to $Q$, and if $\max Q \leq 0$, we are done. So we may assume that $\max Q>0$ and that it is attained at $p_{\text {max }}$; thus at $p_{\text {max }}$, we have $Q_{1}>0, \Delta Q \leq 0, \nabla Q_{1}=-2 \eta^{-1} Q_{1} \nabla \eta$ and
$$Q_{1} \Delta \eta^{2} \geq Q_{1} \frac{2}{R^{2}}\left((2 n-1) \eta \eta^{\prime}+\eta \eta^{\prime \prime}+\left(\eta^{\prime}\right)^{2}\right) .$$
So, at $p_{\text {max }}$,
$$\begin{aligned}
0 \geq \Delta Q & \geq 4 \eta Q_{1} \operatorname{Re}\langle\nabla f, \bar{\nabla} \eta\rangle-8 Q_{1}|\nabla \eta|^{2}+\eta^{2} \frac{Q_{1}^{2}}{12}+Q_{1} \frac{2}{R^{2}}\left((2 n-1) \eta \eta^{\prime}+\eta \eta^{\prime \prime}+\left(\eta^{\prime}\right)^{2}\right) \\
& =\frac{Q^{2}}{12 \eta^{2}}+4 Q \eta^{-1} \operatorname{Re}\langle\nabla f, \bar{\nabla} \eta\rangle-\frac{8 Q}{\eta^{2}} \frac{\left(\eta^{\prime}\right)^{2}}{R^{2}}+\frac{2 Q}{R^{2} \eta^{2}}\left((2 n-1) \eta \eta^{\prime}+\eta \eta^{\prime \prime}+\left(\eta^{\prime}\right)^{2}\right) \\
& \geq \frac{1}{\eta^{2}}\left(\frac{Q^{2}}{12}-\frac{40|\nabla f|}{R} Q-\frac{800}{R^{2}} Q-\frac{100 n}{R^{2}} Q\right),
\end{aligned}$$
where we choose $\eta$ such that $\left|\eta^{\prime}\right|,\left|\eta^{\prime \prime}\right| \leq 10$, for example. Therefore, at $p_{\text {max }} \in B\left(p, \frac{1}{2} R\right)$, we have
$$\frac{Q^{2}}{12}-Q\left(\frac{40|\nabla f|}{R}+\frac{800}{R^{2}}+\frac{100 n}{R^{2}}\right) \leq 0 \quad \Longrightarrow \quad Q\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}},$$
since $\sup _{B(p, R / 2)}|\nabla f| \leq C(n) R^{-1}$ from the previous estimates. Then, for any $x \in B\left(p, \frac{1}{3} R\right)$, we have
$$Q_{1}(x)=\eta^{2}(x) Q_{1}(x)=Q(x) \leq Q\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$

Thus it follows that
$$\left|\nabla_{1} \nabla_{2} f\right|(x) \leq Q_{1}(x)+2\left(\Delta_{1} f(x)+\Delta_{2} f(x)\right) \leq \frac{C(n)}{R^{2}}+2\left(\Delta_{1} f(x)+\Delta_{2} f(x)\right) .$$
On the other hand, from $\left|\nabla_{1} \nabla_{2} f\right|=\left|\left(\nabla_{1} \nabla_{2} u / u\right)-\left(\nabla_{1} u / u\right)\left(\nabla_{2} u / u\right)\right|$, we get
$$\begin{aligned}
\left|\nabla_{1} \nabla_{2} u\right|(x) & \leq\left|\nabla_{1} \nabla_{2} f(x)\right| u(x)+u(x) \frac{\left|\nabla_{1} u(x)\right|}{u} \frac{\left|\nabla_{2} u(x)\right|}{u} \\
& \leq C(n) \frac{u(x)}{R^{2}}+2 \Delta_{1} u(x)+2 \Delta_{2} u(x)+u(x) \frac{\left|\nabla_{1} u(x)\right|}{u} \frac{\left|\nabla_{2} u(x)\right|}{u} \\
& \leq C(n) \frac{\text { osc }_{B(p, R)} u}{R^{2}} .
\end{aligned}$$
Therefore we obtain
$$\sup _{B(p, R / 3)}\left|\nabla_{1} \nabla_{2} u\right| \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .$$
By exactly the same argument we get similar estimates for $\left|\nabla_{1} \nabla_{\overline{2}} u\right|$ and $\left|\nabla_{1} \nabla_{k} u\right|+\left|\nabla_{1} \nabla_{\bar{k}} u\right|$ for $k \neq 1$.
Hence we have proved the following lemma.
Lemma 3.4. There exists a constant $C(n)>0$ such that, for the solution $u_{\epsilon}$ to (3-4),
$$\sup _{B_{g \epsilon}(0, R / 2)}\left(\left|\nabla_{i} \nabla_{j} u_{\epsilon}\right|_{g_{\epsilon}}+\left|\nabla_{i} \nabla_{\bar{j}} u_{\epsilon}\right|_{g_{\epsilon}}\right) \leq C(n) \frac{\operatorname{osc}_{B_{g \epsilon}(0, R)} u_{\epsilon}}{R^{2}}$$
for all $i, j=1,2, \ldots, n$.
3A5. Convergence of $u_{\epsilon}$. In this subsection, we will show that the Dirichlet problem (3-1) admits a unique solution for any $\varphi \in C^{0}\left(\partial B_{\beta}(0,1)\right)$. Here we will write $B_{\beta}=B_{\beta}(0,1)$ for simplicity of notation.

Proposition 3.5. For any $\varphi \in C^{0}\left(\partial B_{\beta}\right)$, the Dirichlet boundary value problem (3-1) admits a unique solution $u \in C^{2}\left(B_{\beta} \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\beta}}\right)$. Moreover, $u$ satisfies the estimates in Lemmas 3.2-3.4 with $u_{\epsilon}$ replaced by $u$ and the metric balls replaced by those under the metric $g_{\beta}$, which we will refer to as "derivatives estimates" throughout this section.

Proof. Given the estimates of $u_{\epsilon}$ as in Lemmas 3.2-3.4, we can derive the uniform local $C^{2, \alpha}$ estimates of $u_{\epsilon}$ on any compact subsets of $B_{\beta}(0,1) \backslash \mathcal{S}$.

The $C^{0}$ estimates of $u_{\epsilon}$ follow immediately from the maximum principle (see Lemma 3.1).
Take any compact subsets $K \subseteq K^{\prime} \subset B_{\beta}(0,1)$. By Lemmas 3.2 and 3.3, we have
$$\begin{aligned}
\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial u_{\epsilon}}{\partial z_{1}}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial u_{\epsilon}}{\partial z_{2}}\right|+\left|\frac{\partial u_{\epsilon}}{\partial s_{j}}\right|\right) & \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\beta}\right)}, \\
\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial^{2} u_{\epsilon}}{\partial s_{k} \partial z_{1}}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial^{2} u_{\epsilon}}{\partial s_{k} \partial z_{2}}\right|+\left|\frac{\partial^{2} u_{\epsilon}}{\partial s_{k} \partial s_{j}}\right|\right) & \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\beta}\right)^{2}},
\end{aligned}$$
and the third-order estimates
$$\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial^{3} u_{\epsilon}}{\partial z_{1} \partial s_{k} \partial s_{l}}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial^{3} u_{\epsilon}}{\partial z_{2} \partial s_{k} \partial s_{l}}\right|+\left|\frac{\partial^{3} u_{\epsilon}}{\partial s_{j} \partial s_{k} \partial s_{l}}\right|\right) \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\beta}\right)^{3}} .$$

Moreover, applying the gradient estimate to the $\Delta_{g_{\epsilon}}$-harmonic function $\Delta_{1, \epsilon} u_{\epsilon}$, we get
$$\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial}{\partial z_{1}} \Delta_{1, \epsilon} u_{\epsilon}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial}{\partial z_{2}} \Delta_{1, \epsilon} u_{\epsilon}\right|+\left|\frac{\partial}{\partial s_{j}} \Delta_{1, \epsilon} u_{\epsilon}\right|\right) \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\beta}\right)^{3}} .$$
From (3-34)-(3-36), we see that the functions $u_{\epsilon}$ have uniform $C^{3}$-estimates in the "tangential directions" on any compact subset of $B_{\beta}(0,1)$. Moreover, for any fixed small constant $\delta>0$, let $T_{\delta}(\mathcal{S})$ be the tubular neighborhood of $\mathcal{S}$. We consider the equation
$$\Delta_{\epsilon} u_{\epsilon}=\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2} u_{\epsilon}}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}} \frac{\partial^{2} u_{\epsilon}}{\partial z_{2} \partial \bar{z}_{2}}+\sum_{j=5}^{2 n} \frac{\partial^{2} u_{\epsilon}}{\partial s_{j}^{2}}=0 \quad \text { on } K^{\prime} \backslash T_{\delta / 2}(\mathcal{S}),$$
which is strictly elliptic (with ellipticity depending only on $\delta>0$ ). Hence by standard elliptic Schauder theory, we also have $C^{2, \alpha}$-estimates of $u_{\epsilon}$ in the "transversal directions" (i.e., normal to $\mathcal{S}$ ) and the mixed directions on the compact subset $K \backslash T_{\delta}(\mathcal{S})$. By taking $\delta \rightarrow 0$ and $K \rightarrow B_{\beta}$, and using a diagonal argument, up to a subsequence, the $u_{\epsilon}$ converge in $C_{\text {loc }}^{2, \alpha}\left(B_{\beta} \backslash \mathcal{S}\right)$ to a function $u \in C^{2, \alpha}\left(B_{\beta} \backslash \mathcal{S}\right)$. Clearly, $u$ satisfies the equation $\Delta_{\beta} u=0$ on $B_{\beta} \backslash \mathcal{S}$, and the estimates (3-34)-(3-36) hold for $u$ outside $\mathcal{S}$, which implies that $u$ can be continuously extended through $\mathcal{S}$ and defines a continuous function in $B_{\beta}(0,1)$. It remains to check the boundary value of $u$.

Claim: $u=\varphi$ on $\partial B_{\beta}(0,1)$. It remains to show the limit function $u$ of $u_{\epsilon}$ satisfies the boundary condition $u=\varphi$ on $\partial B_{\beta}(0,1)$, which will be proved by constructing suitable barriers as we did in [20].

The metric ball $B_{\beta}(0,1)$ is given by
$$B_{\beta}(0,1)=\left\{z \in \mathbb{C}^{n}\left|d_{\beta}(0, z)^{2}:=\left|z_{1}\right|^{2 \beta_{1}}+\left|z_{2}\right|^{2 \beta_{2}}+\sum_{j=5}^{2 n} s_{j}^{2}<1\right\} .\right.$$
$B_{\boldsymbol{\beta}}(0,1) \subset B_{\mathbb{C}^{n}}(0,1)$, and their boundaries only intersect at $\mathcal{S}_{1} \cap \mathcal{S}_{2}$, where $z_{1}=z_{2}=0$. Fix any point $q \in \partial B_{\beta}(0,1)$ and consider the cases $q \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ and $q \notin \mathcal{S}_{1} \cap \mathcal{S}_{2}$.