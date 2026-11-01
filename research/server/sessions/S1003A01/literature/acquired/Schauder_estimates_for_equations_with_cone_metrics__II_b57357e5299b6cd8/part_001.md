---
retention_scope: session
part: 1
total_parts: 5
---

[Part 1/5 of: Schauder estimates for equations with cone metrics, II]

---
source_file: 1809_03116.pdf
converter: mathpix
format: mmd
---

\title{
SCHAUDER ESTIMATES FOR EQUATIONS WITH CONE METRICS, II
}

\author{
BIN GUO AND JIAN SONG
}

\begin{abstract}
This is the continuation of our paper [20], to study the linear theory for equations with conical singularities. We derive interior Schauder estimates for linear elliptic and parabolic equations with a background Kähler metric of conical singularities along a divisor of simple normal crossings. As an application, we prove the short-time existence of the conical Kähler-Ricci flow with conical singularities along a divisor with simple normal crossings.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. Preliminaries ..... 6
2.1. Notations ..... 6
2.2. A useful lemma ..... 9
3. Elliptic estimates ..... 9
3.1. Conical harmonic functions ..... 10
3.2. Tangential and Laplacian estimates ..... 19
3.3. Mixed normal-tangential estimates along the directions $\mathcal{S}$ ..... 23
3.4. Mixed normal directions ..... 31
3.5. Non-flat conical Kähler metrics ..... 42
4. Parabolic estimates ..... 48
4.1. Conical heat equations ..... 48
4.2. Sketched proof of Theorem 1.3 ..... 53
4.3. Interior Schauder estimate for non-flat conical Kähler metrics ..... 53
4.4. Schauder estimate near $t=0$ ..... 58
5. Conical Kähler-Ricci flow ..... 65
References ..... 68

\section*{1. Introduction}

Regularity of solutions of Complex Monge-Ampère equations is a central problem in complex geometry. Complex Monge-Ampère equations with singular and degenerate data can be applied to study compactness and moduli problems of canonical Kähler metrics in Kähler geometry. In [43], Yau has already considered special cases of complex singular Monge-Ampère equations as generalization of his solution to the Calabi conjecture. Conical singularities along complex hypersurfaces of a Kähler manifold are among the mildest singularities in Kähler geometry and it has been extensively studied, especially in the case of Riemann surfaces [41, 28]. The study of such Kähler metrics with conical singularities has many geometric applications, for example, the

\footnotetext{
Research supported in part by National Science Foundation grants DMS-17-11439 and DMS-17-10500.
}

Chern number inequality in various settings [39, 38]. Recently, Donaldson [14] initiated the program of studying analytic and geometric properties of Kähler metrics with conical singularities along a smooth complex hypersurface on a Kähler manifold. This is an essential step to the solution of the Yau-Tian-Donaldson conjecture relating existence of Kähler-Einstein metrics and algebraic K-stability on Fano manifolds [5, 6, 7, 40]. In [14], the Schauder estimate for linear Laplace equations with conical background metric is established using classical potential theory. This is crucial for the openness of the continuity method to find desirable (conical) Kähler-Einstein metric. Donaldson's Schauder estimate is generalized to the parabolic case [8] with similar classical approach. There is also an alternative approach for the conical Schauder estimates using microlocal analysis [23]. There are also various global and local estimates and regularity derived in the conical setting [1, 15, 9, 11, 13, 12, 18, 15, 24, 29, 31, 44, 45].

The Schauder estimates play an important role in the linear PDE theory. Apart from the classical potential theory, various proofs have been established by different analytic techniques. In fact, the blow-up or perturbation techniques developed in [36, 42] (also see [33, 34, 2, 3]) are much more flexible and sharper than the classical method. The authors combined the perturbation method in [20] and geometric gradient estimates to establish sharp Schauder estimates for Laplace equations and heat equations on $\mathbb{C}^{n}$ with a background flat Kähler metric of conical singularities along the smooth hyperplane $\left\{z_{1}=0\right\}$ and derived explicit and optimal dependence on conical parameters.

In algebraic geometry, one often has to consider pairs $(X, D)$ with $X$ being an algebraic variety of complex dimension $n$ and the boundary divisor $D$ as a complex hypersurface of $X$. After possible log resolution, one can always assume the divisor $D$ is a union of smooth hypersurfaces with simple normal crossings. The suitable category of Kähler metrics associated to $(X, D)$ is the family of Kähler metrics on $X$ with conical singularities along $D$. In order to study canonical Kähler metrics on pairs and related moduli problems, we are obliged to study regularity and asymptotics for complex Monge-Ampère equation with prescribed conical singularities of normal crossings. However, the linear theory is still missing and has been open for a while. The goal of this paper is to extend our result [20] and establish the sharp Schauder estimates for linear equations with background Kähler metric of conical singularities along divisors of simple normal crossings. We can apply and extend many techniques developed in [20], however, new estimates and techniques have to be developed because in case of conical singularities along a single smooth divisor, the difficult estimate in the conical direction can sometimes be bypassed and reduced to estimates in the regular directions, while such treatment does not work in the case of simple normal crossings. One is forced to treat regions near high codimensional singularities directly with new and more delicate estimate beyond the scope of [20].

The standard local models for such conical Kähler metrics can be described as below.
Let $\boldsymbol{\beta}=\left(\beta_{1}, \ldots, \beta_{p}\right) \in(0,1)^{p}$ and $p \leq n$ and $\omega_{\boldsymbol{\beta}}$ (or $g_{\boldsymbol{\beta}}$ ) be the standard cone metric on $\mathbb{C}^{p} \times \mathbb{C}^{n-p}$ with cone singularity along $\mathcal{S}=\cup_{i=1}^{p} \mathcal{S}_{i}$, where $\mathcal{S}_{i}=\left\{z_{i}=0\right\}$, that is,
$$\omega_{\boldsymbol{\beta}}=\sum_{j=1}^{p} \beta_{j}^{2} \frac{\sqrt{-1} d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2\left(1-\beta_{j}\right)}}+\sum_{j=p+1}^{n} \sqrt{-1} d z_{j} \wedge d \bar{z}_{j} .$$
We shall use $s_{2 p+1}, \ldots s_{2 n}$ to denote the real coordinates of $\mathbb{C}^{n-p}=\mathbb{R}^{2 n-2 p}$, such that for $j=$ $p+1, \ldots, n$
$$z_{j}=s_{2 j-1}+\sqrt{-1} s_{2 j} .$$

In this paper we wills study the following conical Laplacian equation with the background metric $g_{\boldsymbol{\beta}}$ on $\mathbb{C}^{n}$
$$\Delta_{\boldsymbol{\beta}} u=f, \quad \text { in } B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S},$$
where $B_{\boldsymbol{\beta}}(0,1)$ is the unit ball with respect to $g_{\boldsymbol{\beta}}$ centered at 0 . The Laplacian $\Delta_{\boldsymbol{\beta}}$ is defined as
$$\Delta_{\boldsymbol{\beta}} u=\sum_{j, k} g_{\boldsymbol{\beta}}^{j \bar{k}} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{k}}=\sum_{j=1}^{p}\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}+\sum_{j=p+1}^{n} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}} .$$
We always assume $f \in C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right)$ and $u \in C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right) \cap C^{2}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right)$. Throughout this paper, given a continuous function $f$ we denote
$$\omega(r):=\omega_{f}(r)=\sup _{z, w \in B_{\boldsymbol{\beta}}(0,1), d_{\boldsymbol{\beta}}(z, w)<r}|f(z)-f(w)|$$
the oscillation of $f$ with respect to $g_{\boldsymbol{\beta}}$ in the ball $B_{\boldsymbol{\beta}}(0,1)$. It is clear that $\omega(2 r) \leq 2 \omega(r)$ for any $r<1 / 2$. We say a continuous function $f$ is Dini continuous if $\int_{0}^{1} \frac{\omega(r)}{r} d r<\infty$.
Definition 1.1. We will write the (weighted) polar coordinates of $z_{j}$ for $1 \leq j \leq p$ as
$$r_{j}=\left|z_{j}\right|^{\beta_{j}}, \quad \theta_{j}=\arg z_{j} .$$
We denote $D^{\prime}$ to be one of the first order operators $\left\{\frac{\partial}{\partial s_{2 p+1}}, \ldots, \frac{\partial}{\partial s_{2 n}}\right\}$, and $N_{j}$ to be one of the operators $\left\{\frac{\partial}{\partial r_{j}}, \frac{\partial}{\beta_{j} r_{j} \partial \theta_{j}}\right\}$ which as vector fields are transversal to $\mathcal{S}_{j}$.

Our first main result is the Hölder estimates of the solution $u$ to the equation (1.2).
Theorem 1.1. Suppose $\boldsymbol{\beta} \in(1 / 2,1)^{p}$ and $f \in C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right)$ is Dini continuous with respect to $g_{\boldsymbol{\beta}}$. Let $u \in C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right) \cap C^{2}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right)$ be the solution to the equation (1.2), then there exists $C=C(n, \boldsymbol{\beta})>0$ such that for any two points $p, q \in B_{\boldsymbol{\beta}}(0,1 / 2) \backslash \mathcal{S}$,
$$\begin{aligned}
& \left.\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right|+\left.\sum_{j=1}^{p}| | z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}(p)-\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}(q) \right\rvert\, \\
\leq & C\left(d\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right),
\end{aligned}$$
for any $1 \leq j \leq p$,
$$\left|N_{j} D^{\prime} u(p)-N_{j} D^{\prime} u(q)\right| \leq C\left(d^{\frac{1}{\beta_{j}}-1}\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{\frac{1}{\beta_{j}}-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{j}}} d r\right),$$
and for any $1 \leq j, k \leq p$ with $j \neq k$,
$$\left|N_{j} N_{k} u(p)-N_{j} N_{k} u(q)\right| \leq C\left(d^{\frac{1}{\beta_{\max }}-1}\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{\frac{1}{\beta_{\max }}-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\max }}} d r\right),$$
where $d=d_{\boldsymbol{\beta}}(p, q)>0$ is the $g_{\boldsymbol{\beta}}$-distance of $p$ and $q$ and $\beta_{\text {max }}=\max \left\{\beta_{1}, \ldots, \beta_{p}\right\} \in(1 / 2,1)$.
Remark 1.1. (1) We remark that the number $\beta_{\text {max }}$ on the RHS of (1.5) can be replaced by $\max \left\{\beta_{j}, \beta_{k}\right\}$. (2) In Theorem 1.1 and Theorem 1.3 below, we assume $\boldsymbol{\beta} \in(1 / 2,1)^{p}$ just for exposition purposes and cleanness of the statement. When some of angles $\beta_{j}$ lie in (0, 1/2], the pointwise Hölder estimates in Theorem 1.1 are adjusted as follows: if $\beta_{j} \in(0,1 / 2]$ in (1.4), we replace the RHS by the RHS of (1.3). In (1.5), if both $\beta_{j}$ and $\beta_{k} \in(0,1 / 2]$, we also replace the RHS by that of (1.3); if at least one of the $\beta_{j}, \beta_{k}$ is bigger than 1/2, (1.5) remains unchanged. The inequalities in Theorem 1.3 can be adjusted similarly. The proofs of these estimates are contained in the proof of the case when $\beta_{j} \in(1 / 2,1)$ by using the corresponding estimates in (2.2).

An immediate corollary of Theorem 1.1 is a precise form of Schauder estimates for equation (1.2).
Corollary 1.1. Given $\boldsymbol{\beta} \in(0,1)^{p}$ and $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ for some $0<\alpha<\min \left\{1, \frac{1}{\beta_{\text {max }}}-1\right\}$, if $u \in C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right) \cap C^{2}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right)$ solves equation (1.2), then $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)$. Moreover, for any compact subset $K \Subset B_{\boldsymbol{\beta}}(0,1)$, there exists a constant $C=C(n, \boldsymbol{\beta}, K)>0$ such that the following estimate holds (see Definition 2.1 for the notations)
$$\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}(K)} \leq C\left(\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\frac{\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}}{\alpha\left(\min \left\{\frac{1}{\beta_{\max }}-1,1\right\}-\alpha\right)}\right) .$$

Remark 1.2. A scaling-invariant version of the Schauder estimate (1.6) is that for any $0<r<1$, there exists a constant $C=C(n, \boldsymbol{\beta}, \alpha)>0$ such that (see Definition 2.3 for the notations)
$$\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right)}^{*} \leq C\left(\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}(0, r)\right)}+\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right)}^{(2)}\right),$$
which follows from a standard rescaling argument by scaling $r$ to 1 .
Let $g$ be a $C_{\boldsymbol{\beta}}^{0, \alpha}$-conical Kähler metric on $B_{\boldsymbol{\beta}}(0,1)$ (see Definition 3.1 below). By definition $g$ is equivalent to $g_{\beta}$. We consider the equation
$$\Delta_{g} u=f \text { in } B_{\boldsymbol{\beta}}(0,1), \text { and } u=\varphi \text { on } \partial B_{\boldsymbol{\beta}}(0,1),$$
for some $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$. The following theorem is the generalization of Corollary 1.1 for nonflat background conical Kähler metrics, which is useful for applications of global geometric complex Monge-Ampère equations.
Theorem 1.2. For any given $\boldsymbol{\beta} \in(0,1)^{p}, f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ and $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$, there is a unique solution $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ to the equation (1.8). Moreover, for any compact subset $K \Subset B_{\boldsymbol{\beta}}(0,1)$, there exits $C=C(n, \boldsymbol{\beta}, \alpha, g, K)>0$ such that
$$\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}(K)}^{2, \alpha} \leq C\left(\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}\right) .$$

Theorem 1.2 can immediately be applied to study complex Monge-Ampère equations with prescribed conical singularities along divisors of simple normal crossings and most of the geometric and analytic results for canonical Kähler metrics with conical singularities along a smooth divisor can be generalized to the case of simple normal crossings.

We now turn to the parabolic Schauder estimates for the solution $u \in \mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathcal{C}^{2}\left(\mathcal{Q}_{\boldsymbol{\beta}}^{\#}\right)$ to the equation
$$\frac{\partial u}{\partial t}=\Delta_{g_{\beta}} u+f,$$
for a Dini continuous function $f$ in $\mathcal{Q}_{\boldsymbol{\beta}}$, where for notation convenience we write $\mathcal{Q}_{\boldsymbol{\beta}}:=B_{\boldsymbol{\beta}}(0,1) \times$ $(0,1]$ and $\mathcal{Q}_{\boldsymbol{\beta}}^{\#}:=B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S} \times(0,1]$. Our second main theorem is the following pointwise estimate.

Theorem 1.3. Suppose $\boldsymbol{\beta} \in(1 / 2,1)^{p}$ and $u$ is the solution to (1.9). Then there exists a computable constant $C=C(n, \boldsymbol{\beta})>0$ such that for any $Q_{p}=\left(p, t_{p}\right), Q_{q}=\left(q, t_{q}\right) \in B_{\boldsymbol{\beta}}(0,1 / 2) \backslash \mathcal{S} \times(\hat{t}, 1]$ (for some $\hat{t} \in(0,1)$ ) such that
$$\begin{aligned}
& \left.\left|\left(D^{\prime}\right)^{2} u\left(Q_{p}\right)-\left(D^{\prime}\right)^{2} u\left(Q_{q}\right)\right|+\left.\sum_{j=1}^{p}| | z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}\left(Q_{p}\right)-\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}\left(Q_{q}\right) \right\rvert\, \\
+ & \left|\frac{\partial u}{\partial t}\left(Q_{p}\right)-\frac{\partial u}{\partial t}\left(Q_{q}\right)\right| \leq C\left(\frac{d}{\hat{t}^{3 / 2}}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\hat{t}^{-1} \int_{0}^{d} \frac{\omega(r)}{r} d r+\frac{d}{\hat{t}^{3 / 2}} \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right)
\end{aligned}$$
and for any $1 \leq j \leq p$
$$\left|N_{j} D^{\prime} u\left(Q_{p}\right)-N_{j} D^{\prime} u\left(Q_{q}\right)\right| \leq C\left(\frac{d^{\frac{1}{\beta_{j}}-1}}{\hat{t}^{3 / 2}}\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\hat{t}^{-1} \int_{0}^{d} \frac{\omega(r)}{r} d r+\frac{d^{\frac{1}{\beta_{j}}-1}}{\hat{t}^{3 / 2}} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{j}}} d r\right),$$
and for any $1 \leq j, k \leq p$ with $j \neq k$
$$\left|N_{j} N_{k} u\left(Q_{p}\right)-N_{j} N_{k} u\left(Q_{q}\right)\right| \leq C\left(\frac{d^{\frac{1}{\beta_{\max }}}-1}{\hat{t}^{3 / 2}}\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\hat{t}^{-1} \int_{0}^{d} \frac{\omega(r)}{r} d r+\frac{d^{\frac{1}{\beta_{\max }}}-1}{\hat{t}^{3 / 2}} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\max }}} d r\right),$$
where $d=d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{p}, Q_{q}\right)>0$ is the parabolic $g_{\beta}$-distance of $Q_{p}$ and $Q_{q}$, and $\beta_{\text {max }}=\max \left\{\beta_{1}, \ldots, \beta_{p}\right\}$, and $\omega(r)$ is the oscillation of $f$ in $\mathcal{Q}_{\boldsymbol{\beta}}$ under the parabolic distance $d_{\mathcal{P}, \boldsymbol{\beta}}$ (c.f. Section 2.1.2).

If $f \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \frac{\alpha}{2}}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$ for some $\alpha \in\left(0, \min \left(\frac{1}{\beta_{\text {max }}}-1,1\right)\right)$, then we have the following precise estimates as the parabolic analogue of Corollary 1.1.
Corollary 1.2. Suppose $\boldsymbol{\beta} \in(0,1)^{p}$ and $u \in \mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathcal{C}^{2}\left(\mathcal{Q}_{\boldsymbol{\beta}}^{\#}\right)$ satisfies the equation (1.9), then there exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that (see Definition 2.5 for the notations)
$$\|u\|_{\mathcal{C}_{\beta}^{2+\alpha, \frac{\alpha+2}{2}}\left(B_{\boldsymbol{\beta}}(0,1 / 2) \times(1 / 2,1]\right)} \leq C\left(\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\frac{\|f\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \frac{\alpha}{2}}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}}{\alpha\left(\min \left\{\frac{1}{\beta_{\max }}-1,1\right\}-\alpha\right)}\right) .$$

For general non-flat $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}$-conical Kähler metrics $g$, we consider the linear parabolic equation
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f, \text { in } \mathcal{Q}_{\boldsymbol{\beta}}, u=\varphi \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}} .$$
We then have the following parabolic Schauder estimates as an analogue of Theorem 1.2.
Theorem 1.4. Given $\boldsymbol{\beta} \in(0,1)^{p}, f \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ and $\varphi \in \mathcal{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right)$, there exists a unique solution $u \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}}\left(B_{\boldsymbol{\beta}}(0,1) \times(0,1]\right) \cap \mathcal{C}^{0}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ to the Dirichlet boundary value problem (1.10). For any compact subset $K \Subset B_{\boldsymbol{\beta}}(0,1)$ and $\varepsilon_{0}>0$ there exists $C=C\left(n, \boldsymbol{\beta}, \alpha, K, \varepsilon_{0}, g\right)>0$ such that the following interior Schauder estimate holds
$$\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}\left(K \times\left[\varepsilon_{0}, 1\right]\right)} \leq C\left(\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\|f\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}\right) .$$
Furthermore, if we assume $\left.u\right|_{t=0}=u_{0} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)$, then $u \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}}\left(B_{\boldsymbol{\beta}}(0,1) \times[0,1]\right)$ and there exists a constant $C=C(n, \boldsymbol{\beta}, \alpha, g, K)>0$ such that
$$\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}}(K \times[0,1])} \leq C\left(\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\|f\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\left\|u_{0}\right\|_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}\right) .$$

As an application of Theorem 1.4, we derive the short-time existence of the conical Kähler-Ricci flow with background metric being conical along divisors with simple normal crossings.

Let $(X, D)$ be a compact Kähler manifold, where $D=\sum_{j} D_{j}$ is a finite union of smooth divisors $\left\{D_{j}\right\}$ and $D$ has only simple normal crossings. Let $\omega_{0}$ be a $C_{\boldsymbol{\beta}}^{0, \alpha^{\prime}}(X)$-conical Kähler metric with cone angle $2 \pi \boldsymbol{\beta}$ along $D$ (see Definition 2.7) and $\hat{\omega}_{t}$ be a family of conical metrics with bounded norm $\|\hat{\omega}\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}}$ and $\hat{\omega}_{0}=\omega_{0}$. We consider the complex Monge-Ampère flow
$$\frac{\partial \varphi}{\partial t}=\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi\right)^{n}}{\omega_{0}^{n}}\right)+f, \text { and }\left.\varphi\right|_{t=0}=0,$$
for some $f \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}(X \times[0,1])$.

Theorem 1.5. Given $\alpha \in\left(0, \alpha^{\prime}\right)$, there exists $T=T\left(n, \hat{\omega}, f, \alpha^{\prime}, \alpha\right)>0$ such that (1.11) admits a unique solution $\varphi \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}(X \times[0, T])$.

An immediate corollary of Theorem 1.5 is the short time existence for the conical Kähler-Ricci flow defined as below
$$\frac{\partial \omega}{\partial t}=-\operatorname{Ric}(\omega)+\sum_{j}\left(1-\beta_{j}\right)\left[D_{j}\right],\left.\quad \omega\right|_{t=0}=\omega_{0},$$
where $\operatorname{Ric}(\omega)$ is the unique extension of the Ricci curvature of $\omega$ from $X \backslash D$ to $X$ and $\left[D_{j}\right]$ denotes the current of integration over the component $D_{j}$. In addition we assume $\omega_{0}$ is a $C_{\boldsymbol{\beta}}^{0, \alpha^{\prime}}(X, D)$-conical Kähler metric such that
$$\omega_{0}^{n}=\frac{\Omega}{\prod_{j}\left(\left|s_{j}\right|_{h_{j}}^{2}\right)^{1-\beta_{j}}},$$
where $s_{j}, h_{j}$ are holomorphic sections and hermitian metrics of the line bundle associated to $D_{j}$, respectively, and $\Omega$ is a smooth volume form.

Corollary 1.3. For any given $\alpha \in\left(0, \alpha^{\prime}\right)$, there exists a constant $T=T\left(n, \omega_{0}, \alpha, \alpha^{\prime}\right)>0$ such that the conical Kähler-Ricci flow (1.12) admits a unique solution $\omega=\omega_{t}$, such that $\omega \in \mathcal{C}_{\boldsymbol{\beta}}^{\boldsymbol{\alpha}, \boldsymbol{\alpha} / 2}(X \times[0, T])$ and for each $t \in[0, T], \omega_{t}$ is still a conical metric with cone angle $2 \pi \boldsymbol{\beta}$ along $D$.

Furthermore, $\omega$ is smooth in $X \backslash D \times(0, T]$ and the (normalized) Ricci potentials of $\omega, \log \left(\frac{\omega^{n}}{\omega_{0}^{n}}\right)$ is still in $\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}(X \times[0, T])$.

The short time existence of the conical Kähler-Ricci flow with singularities along a smooth divisor is derived in [8] by adapting the elliptic potential techniques of Donaldson [14]. Corollary 1.3 treats the general case of conical singularities with simple normal crossings. There have been many results in the analytic aspects of the conical Ricci flow [8, 9, 15, 16, 24, 32, 43]. In [30], the conical Ricci flow on Riemann surfaces is completely classified with jumping conical structure in the limit. Such phenomena is also expected in higher dimension, but it requires much deeper and delicate technical advances both in analysis and geometry.

\section*{2. Preliminaries}

We explain the notations and give some preliminary tools which will be used later in this section.

\subsection*{2.1. Notations}

To distinguish the elliptic from parabolic norms, we will use the ordinary $C$ to denote the norms in the elliptic case and the script $\mathcal{C}$ to denote the norms in the parabolic case.

We always assume the Hölder component $\alpha$ appearing in $C_{\boldsymbol{\beta}}^{0, \alpha}$ or $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}$ (or other Hölder norms) to be in $\left(0, \min \left\{\beta_{\text {max }}^{-1}-1,1\right\}\right)$.
2.1.1. Elliptic case. We will denote $d_{\boldsymbol{\beta}}(x, y)$ to be the distance of two points $x, y \in \mathbb{C}^{n}$ under the metric $g_{\boldsymbol{\beta}} . B_{\boldsymbol{\beta}}(x, r)$ will be the metric ball under the metric induced by $g_{\boldsymbol{\beta}}$ with radius $r$ and center $x$. It is well-known that $\left(\mathbb{C}^{n} \backslash \mathcal{S}, g_{\boldsymbol{\beta}}\right)$ is geodesically convex, i.e. any two points $x, y \in \mathbb{C}^{n} \backslash \mathcal{S}$ can be joined by a $g_{\boldsymbol{\beta}}$-minimal geodesic $\gamma$ which is disjoint with $\mathcal{S}$.

Definition 2.1. We define the $g_{\boldsymbol{\beta}}$-Hölder norm of functions $u \in C^{0}\left(B_{\boldsymbol{\beta}}(0, r)\right)$ for some $\alpha \in(0,1)$ as
$$\|u\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right)}:=\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}(0, r)\right)}+[u]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right)},$$
where the semi-norm is defined as $[u]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right)}:=\sup _{x \neq y \in B_{\boldsymbol{\beta}}(0, r)} \frac{|u(x)-u(y)|}{d_{\boldsymbol{\beta}}(x, y)^{\alpha}}$. We denote the subspace of all continuous functions $u$ such that $\|u\|_{C_{\boldsymbol{\beta}}^{0, \alpha}}<\infty$ as $C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right)$.

Definition 2.2. The $C_{\boldsymbol{\beta}}^{2, \boldsymbol{\alpha}}$ norm of a function $u$ on $B_{\boldsymbol{\beta}}(0, r)=: B_{\boldsymbol{\beta}}$ is defined as:
$$\begin{aligned}
\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}:= & \|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}\right)}+\left\|\nabla_{g_{\boldsymbol{\beta}}} u\right\|_{C^{0}\left(B_{\boldsymbol{\beta}}, g_{\boldsymbol{\beta}}\right)}+\sum_{j=1}^{p}\left\|N_{j} D^{\prime} u\right\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)} \\
& +\sum_{1 \leq j \neq k \leq p}\left\|N_{j} N_{k} u\right\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}+\sum_{j=1}^{p}\left\|\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}\right\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)} .
\end{aligned}$$

For a given set $\Omega \subset B_{\boldsymbol{\beta}}(0,1)$ we define the following weighted (semi)norms.
Definition 2.3. Suppose $\sigma \in \mathbb{R}$ is a given real number and $u$ is a $C_{\boldsymbol{\beta}}^{2, \alpha}$-function in $\Omega$. We denote $d_{x}=d_{\boldsymbol{\beta}}(x, \partial \Omega)$ for any $x \in \Omega$. We define the weighted (semi)norms
$$\begin{gathered}
{[u]_{C_{\beta}^{0, \alpha}(\Omega)}^{(\sigma)}=\sup _{x \neq y \in \Omega} \min \left(d_{x}, d_{y}\right)^{\sigma+\alpha} \frac{|u(x)-u(y)|}{d_{\boldsymbol{\beta}}(x, y)^{\alpha}},} \\
\|u\|_{C^{0}(\Omega)}^{(\sigma)}=\sup _{x \in \Omega} d_{x}^{\sigma}|u(x)|, \quad[u]_{C_{\boldsymbol{\beta}}^{1}(\Omega)}^{(\sigma)}=\sup _{x \in \Omega \backslash \mathcal{S}} d_{x}^{\sigma+1}\left(\sum_{j}\left|N_{j} u\right|(x)+\left|D^{\prime} u\right|(x)\right) \\
{[u]_{C_{\boldsymbol{\beta}}^{2}(\Omega)}^{(\sigma)}=\sup _{x \in \Omega \backslash \mathcal{S}} d_{x}^{\sigma+2}|T u(x)|,} \\
{[u]_{C_{\boldsymbol{\beta}}^{2, \alpha}(\Omega)}^{(\sigma)}=\sup _{x \neq y \in \Omega \backslash \mathcal{S}} \min \left(d_{x}, d_{y}\right)^{\sigma+2+\alpha} \frac{|T u(x)-T u(y)|}{d_{\boldsymbol{\beta}}(x, y)^{\alpha}},}
\end{gathered}$$
and
$$\|u\|_{C_{\beta}^{2, \alpha}(\Omega)}^{(\sigma)}=\|u\|_{C^{0}(\Omega)}^{(\sigma)}+[u]_{C_{\beta}^{1}(\Omega)}^{(\sigma)}+[u]_{C_{\beta}^{2}(\Omega)}^{(\sigma)}+[u]_{C_{\beta}^{2, \alpha}(\Omega)}^{(\sigma)},$$
where $T$ denotes the following operators of second order:
$$\left\{\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2}}{\partial z_{j} \partial \bar{z}_{j}}, N_{j} N_{k}(j \neq k), N_{j} D^{\prime},\left(D^{\prime}\right)^{2}\right\} .$$
When $\sigma=0$, we denote the norms above as $[\cdot]^{*},\|\cdot\|^{*}$ for notation simplicity.
2.1.2. Parabolic case. We denote $\mathcal{Q}_{\boldsymbol{\beta}}=\mathcal{Q}_{\boldsymbol{\beta}}(0,1)=B_{\boldsymbol{\beta}}(0,1) \times(0,1]$ to be parabolic cylinder and
$$\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}=\left(\overline{B_{\boldsymbol{\beta}}(0,1)} \times\{0\}\right) \cup\left(\partial B_{\boldsymbol{\beta}}(0,1) \times(0,1]\right)$$
to be the parabolic boundary of the cylinder $\mathcal{Q}_{\boldsymbol{\beta}}$. We write $\mathcal{S}_{\mathcal{P}}=\mathcal{S} \times[0,1]$ as the singular set and $\mathcal{Q}_{\boldsymbol{\beta}}^{\#}=\mathcal{Q}_{\boldsymbol{\beta}} \backslash \mathcal{S}_{\mathcal{P}}$ the complement of $\mathcal{S}_{\mathcal{P}}$. For any two space-time points $Q_{i}=\left(p_{i}, t_{i}\right)$, we define their parabolic distance $d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{1}, Q_{2}\right)$ as
$$d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{1}, Q_{2}\right)=\max \left\{\sqrt{\left|t_{1}-t_{2}\right|}, d_{\boldsymbol{\beta}}\left(p_{1}, p_{2}\right)\right\} .$$

Definition 2.4. We define the $g_{\boldsymbol{\beta}}$-Hölder norm of functions $u \in \mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$ for some $\alpha \in(0,1)$ as
$$\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}:=\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+[u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)},$$
where the semi-norm is defined to be $[u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}:=\sup _{Q_{1} \neq Q_{2} \in \mathcal{Q}_{\beta}} \frac{\left|u\left(Q_{1}\right)-u\left(Q_{2}\right)\right|}{d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{1}, Q_{2}\right)^{\alpha}}$. We denote the subspace of all continuous functions $u$ such that $\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}<\infty$ as $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$.

Definition 2.5. The $\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}}$ norm of a function $u$ on $\mathcal{Q}_{\boldsymbol{\beta}}$ is defined as:
$$\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}}{ }_{\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}}:=\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\left\|\nabla_{g_{\beta}} u\right\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}, g_{\beta}\right)}+\|\mathcal{T} u\|_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)},$$
where $\mathcal{T}$ denotes all the second order operators in (2.1) and the first order operator $\frac{\partial}{\partial t}$.
For a given set $\Omega \subset \mathcal{Q}_{\boldsymbol{\beta}}$ we define the following weighted (semi)norms.
Definition 2.6. Suppose $\sigma \in \mathbb{R}$ is a real number and $u$ is a $\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}}$-function in $\Omega$. We denote $d_{\mathcal{P}, Q}=d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q, \partial_{\mathcal{P}} \Omega\right)$ for any $Q \in \Omega$. We define the weighted (semi)norms
$$\begin{gathered}
{[u]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}(\Omega)}^{(\sigma)}=\sup _{Q_{1} \neq Q_{2} \in \Omega} \min \left(d_{\mathcal{P}, Q_{1}}, d_{\mathcal{P}, Q_{2}}\right)^{\sigma+\alpha} \frac{\left|u\left(Q_{1}\right)-u\left(Q_{2}\right)\right|}{d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{1}, Q_{2}\right)^{\alpha}},} \\
\|u\|_{\mathcal{C}^{0}(\Omega)}^{(\sigma)}=\sup _{Q \in \Omega} d_{\mathcal{P}, Q}^{\sigma}|u(Q)|, \quad[u]_{\mathcal{C}_{\beta}^{1}(\Omega)}^{(\sigma)}=\sup _{Q \in \Omega \backslash \mathcal{S}_{\mathcal{P}}} d_{\mathcal{P}, Q}^{\sigma+1}\left(\sum_{j}\left|N_{j} u\right|(Q)+\left|D^{\prime} u\right|(Q)\right) \\
{[u]_{\mathcal{C}_{\beta}^{2,1}(\Omega)}^{(\sigma)}=\sup _{Q \in \Omega \backslash \mathcal{S}_{\mathcal{P}}} d_{\mathcal{P}, Q}^{\sigma+2}|\mathcal{T} u(Q)|,} \\
{[u]_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha}, \frac{\alpha+2}{2}(\Omega)}^{(\sigma)}=\sup _{Q_{1} \neq Q_{2} \in \Omega \backslash \mathcal{S}_{\mathcal{P}}} \min \left(d_{\mathcal{P}, Q_{1}}, d_{\mathcal{P}, Q_{2}}\right)^{\sigma+2+\alpha} \frac{\left|\mathcal{T} u\left(Q_{1}\right)-\mathcal{T} u\left(Q_{2}\right)\right|}{d_{\mathcal{P}, \boldsymbol{\beta}}\left(Q_{1}, Q_{2}\right)^{\alpha}},}
\end{gathered}$$
and
$$\|u\|_{\mathcal{C}_{\beta}^{2+\alpha, \frac{\alpha+2}{2}(\Omega)}}^{(\sigma)}=\|u\|_{\mathcal{C}^{0}(\Omega)}^{(\sigma)}+[u]_{\mathcal{C}_{\beta}^{1}(\Omega)}^{(\sigma)}+[u]_{\mathcal{C}_{\beta}^{2,1}(\Omega)}^{(\sigma)}+[u]_{\mathcal{C}_{\beta}^{2+\alpha, \frac{\alpha+2}{2}}(\Omega)}^{(\sigma)} .$$
When $\sigma=0$, we denote the norms above as $[\cdot]^{*}$ or $\|\cdot\|^{*}$ for simplicity.
2.1.3. Compact Kähler manifolds. Let $(X, D)$ be a compact Kähler manifold with a divisor $D=$ $\sum_{j} D_{j}$ with simple normal crossings, i.e. on an open coordinates chart $\left(U, z_{j}\right)$ of any $x \in D, D \cap U$ is given by $\left\{z_{1} \cdots z_{p}=0\right\}$, and $D_{j} \cap U=\left\{z_{j}=0\right\}$ for any component $D_{j}$ of $D$. We fix a finite cover $\left\{U_{a}, z_{a, j}\right\}$ of $D$.

Definition 2.7. A (singular) Kähler metric $\omega$ is called a conical metric with cone angle $2 \pi \beta$ along $D$, if locally on any coordinates chart $U_{a}, \omega$ is equivalent to $\omega_{\boldsymbol{\beta}}$ under the the coordinates $\left\{z_{a, j}\right\}$, where $\omega_{\boldsymbol{\beta}}$ is the standard cone metric (1.1) with cone angle $2 \pi \beta_{j}$ along $\left\{z_{a, j}=0\right\}$, and on $X \backslash \cup_{a} U_{a}$ $\omega$ is a smooth Kähler metric in the usual sense.

A conical metric $\omega$ is in $C_{\boldsymbol{\beta}}^{0, \alpha}(X, D)$ if for each $a, \omega$ is $C_{\boldsymbol{\beta}}^{0, \alpha}\left(U_{a}\right)$ and on $X \backslash \cup_{a} U_{a} \omega$ is smooth in the usual sense. Similarly we can define the $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}$-conical Kähler metrics on $X \times[0,1]$.

Definition 2.8. A continuous function $u \in C^{0}(X)$ is said to be in $C_{\boldsymbol{\beta}}^{0, \alpha}(X, D)$ if locally on each $U_{a}, u$ is in $C_{\boldsymbol{\beta}}^{0, \alpha}\left(U_{a}\right)$ and on $X \backslash \cup_{a} U_{a}$ it is $C^{0, \alpha}$-continuous in the usual sense. We define the $C_{\boldsymbol{\beta}}^{0, \alpha}(X, D)$-norm of $u$ as
$$\|u\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(X, D)}:=\|u\|_{C^{0, \alpha}\left(X \backslash \cup_{a} U_{a}, \omega\right)}+\sum_{a}\|u\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(U_{a}\right)} .$$
The $C_{\boldsymbol{\beta}}^{0, \alpha}(X, D)$-norm depends on the choice of finite covers, and another cover yields a different but equivalent norm. The space $C_{\boldsymbol{\beta}}^{0, \alpha}(X, D)$ is clearly independent of the choice of finite covers.

The other spaces and norms like $C_{\boldsymbol{\beta}}^{2, \alpha}(X, D), \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}(X \times[0,1], D)$, etc, can be defined similarly.

\subsection*{2.2. A useful lemma}

We will frequently use the following elementary estimates from [20].
Lemma 2.1 (Lemma 2.2 in [20]). Given $r \in(0,1]$, suppose $v \in C^{0}\left(B_{\mathbb{C}}(0, r)\right) \cap C^{2}\left(B_{\mathbb{C}}(0, r) \backslash\{0\}\right)$ satisfies the equation
$$|z|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2} v}{\partial z \partial \bar{z}}=F, \quad \text { in } B_{\mathbb{C}}(0, r) \backslash\{0\},$$
for some $F \in L^{\infty}\left(B_{\mathbb{C}}(0, r)\right)$, then we have the pointwise estimate that for any $z \in B_{\mathbb{C}}(0,9 r / 10) \backslash\{0\}$
$$\left|\frac{\partial v}{\partial z}(z)\right| \leq C \frac{\|v\|_{L^{\infty}}}{r}+C\|F\|_{L^{\infty}} \cdot\left\{\begin{array}{l}
r^{2 \beta_{1}-1}, \text { if } \beta_{1} \in(1 / 2,1) \\
|z|^{2 \beta_{1}-1}, \text { if } \beta_{1} \in(0,1 / 2) \\
|\log (|z| / 2 r)|, \text { if } \beta_{1}=1 / 2,
\end{array}\right.$$
where the $L^{\infty}$-norms are taken in $B_{\mathbb{C}}(0, r)$ and $C>0$ is a uniform constant.
Finally we remark that the idea of the proof of the estimates in Theorems 1.1 and 1.3 is the same for general $2 \leq p \leq n$. To explain the argument clearer we prove the theorems assuming $p=2$, i.e. the cone metric of $\omega_{\boldsymbol{\beta}}$ is singular along the two components $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$.

\section*{3. Elliptic estimates}

In this section, we will prove Theorems 1.1 and 1.2, the Schauder estimates for the Laplace equation (1.2). To begin with, we first observe the simple $C^{0}$-estimate based on maximum principle.

Suppose $u \in C^{2}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ satisfies the equation
$$\left\{\begin{array}{l}
\Delta_{\beta} u=0, \text { in } B_{\beta}(0,1) \backslash \mathcal{S}, \\
u=\varphi, \text { on } \partial B_{\beta}(0,1)
\end{array}\right.$$
for some $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$, then
Lemma 3.1. We have the following maximum principle,
$$\inf _{\partial B_{\boldsymbol{\beta}}(0,1)} \varphi \leq \inf _{B_{\boldsymbol{\beta}}(0,1)} u \leq \sup _{B_{\boldsymbol{\beta}}(0,1)} u \leq \sup _{\partial B_{\boldsymbol{\beta}}(0,1)} \varphi .$$

Proof. Consider the functions $\tilde{u}_{\epsilon}=u \pm \epsilon\left(\log \left|z_{1}\right|^{2}+\log \left|z_{2}\right|^{2}\right)$ for any $\epsilon>0$. By the same proof of Lemma 2.1 in [20], (3.2) is established. \(\square\)

Next step is to show the equation (3.1) is solvable for suitable boundary values.

\subsection*{3.1. Conical harmonic functions}
3.1.1. Smooth approximating metrics. Let $\epsilon \in(0,1)$ be a given small positive number and we define a smooth approximating Kähler metric on $B_{\boldsymbol{\beta}}(0,1)$
$$g_{\epsilon}=\beta_{1}^{2} \frac{\sqrt{-1} d z_{1} \wedge d \bar{z}_{1}}{\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}}}+\beta_{2}^{2} \frac{\sqrt{-1} d z_{2} \wedge d \bar{z}_{2}}{\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}}}+\sum_{j=3}^{n} \sqrt{-1} d z_{j} \wedge d \bar{z}_{j} .$$
$g_{\epsilon}$ are product metrics on $\mathbb{C} \times \mathbb{C} \times \mathbb{C}^{n-2}$. It is clear that its Ricci curvature satisfies
$$\operatorname{Ric}\left(g_{\epsilon}\right)=\sqrt{-1} \partial \bar{\partial} \log \left(\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}}\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}}\right) \geq 0 .$$

Let $u_{\epsilon} \in C^{2}\left(B_{\boldsymbol{\beta}}(0,1)\right)$ be the solution to the equation with a given $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$
$$\Delta_{g_{\epsilon}} u_{\epsilon}=0, \text { in } B_{\boldsymbol{\beta}}(0,1), \text { and } u_{\epsilon}=\varphi, \text { on } \partial B_{\boldsymbol{\beta}}(0,1) .$$
Note that the metric balls $B_{\boldsymbol{\beta}}(0,1)$ and $B_{g_{\epsilon}}(0,1)$ are uniformly close when $\epsilon$ is sufficiently small, so for the following estimates we will work on $B_{\boldsymbol{\beta}}(0,1)$.

Let $u_{\epsilon}$ be the harmonic function for $\Delta_{\epsilon}=\Delta_{g_{\epsilon}}$ as in (3.4), which we may assume without of loss of generality is positive by replacing $u_{\epsilon}$ by $u_{\epsilon}-\inf u_{\epsilon}$ if necessary. We will study the Cheng-Yau-type gradient estimate of $u_{\epsilon}$ and the estimate of $\Delta_{\epsilon, 1} u_{\epsilon}:=\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2} u_{\epsilon}}{\partial z_{1} \partial \bar{z}_{1}}$. Let us recall Cheng-Yau's gradient estimate first.

In Subsections 3.1.2-3.1.5, for notation convenience, we will omit the subscript $\epsilon$ in $g_{\epsilon}, u_{\epsilon}$, in the proofs of lemmas.
3.1.2. Cheng-Yau gradient estimate revisit. We will also assume $u_{\epsilon}>0$, otherwise consider the function $u_{\epsilon}+\delta$, for some $\delta>0$ then letting $\delta \rightarrow 0$. We fix a ball metric $B_{g_{\epsilon}}(p, R) \subset B_{\boldsymbol{\beta}}(0,1)$ centered at some point $p \in B_{\boldsymbol{\beta}}(0,1)$. Since $\operatorname{Ric}\left(g_{\epsilon}\right) \geq 0$, the Cheng-Yau gradient estimate holds for $\Delta_{g_{\epsilon}}$-harmonic functions.
Lemma 3.2 ([10]). Let $u_{\epsilon} \in C^{2}(B(p, R))$ be a positive $\Delta_{g_{\epsilon}}$-harmonic function. There exists a uniform constant $C=C(n)>0$ such that (the metric balls are taken under the metric $g_{\epsilon}$ )
$$\sup _{x \in B(p, 3 R / 4)}\left|\nabla u_{\epsilon}\right|_{g_{\epsilon}}(x) \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u_{\epsilon}}{R} .$$

As we mentioned above, we will omit the $\epsilon$ in the subscript of $u_{\epsilon}$ and $g_{\epsilon}$. The proof of the lemma is standard ([10]). For completeness and to motivate the proof of Lemmas 3.3 and 3.4 below, we provide a sketched proof. Define $f=\log u$, and it can be calculated that
$$\Delta f=\frac{\Delta u}{u}-\frac{|\nabla u|^{2}}{u^{2}}=-|\nabla f|^{2} .$$
Then by Bochner formula, we have
$$\begin{aligned}
\Delta|\nabla f|^{2} & =|\nabla \nabla f|^{2}+|\nabla \bar{\nabla} f|^{2}+2 \operatorname{Re}\langle\nabla f, \bar{\nabla} \Delta f\rangle+\operatorname{Ric}(\nabla f, \bar{\nabla} f) \\
& \left.\geq|\nabla \bar{\nabla} f|^{2}-\left.2 \operatorname{Re}\langle\nabla f, \bar{\nabla}| \nabla f\right|^{2}\right\rangle .
\end{aligned}$$
Let $\phi:[0,1] \rightarrow[0,1]$ be a standard cut-off function such that $\left.\phi\right|_{[0,3 / 4]}=1$ and $\phi_{[5 / 6,1]}=0$ and between 0,1 otherwise. let $r(x)=d_{g_{\epsilon}}(p, x)$ be the distance function to $p$ under the metric $g=g_{\epsilon}$. By abusing notation we also write $\phi(x)=\phi\left(\frac{r(x)}{R}\right)$. It can be calculated by Laplacian comparison and the Bochner formula (3.7) that at the (positive) maximum point $p_{\text {max }}$ of $H:=\phi^{2}|\nabla f|^{2}$ that
$$\frac{2}{n} H^{2}-\frac{4\left|\phi^{\prime}\right|}{R} H^{3 / 2}-\frac{8\left(\phi^{\prime}\right)^{2}}{R^{2}} H+\frac{2 H}{R^{2}}\left((2 n-1) \phi \phi^{\prime}+\phi \phi^{\prime \prime}+\left(\phi^{\prime}\right)^{2}\right) \leq 0,$$
therefore for any $x \in B(p, 3 R / 4)$
$$\frac{|\nabla u|^{2}}{u^{2}}(x)=|\nabla f(x)|^{2}=H(x) \leq H\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$
3.1.3. Laplacian estimate in singular directions. We will prove the estimates of $\Delta_{j, \epsilon} u_{\epsilon}:=\left(\left|z_{j}\right|^{2}+\right.$ $\epsilon)^{1-\beta_{j}} \frac{\partial u_{\epsilon}}{\partial z_{j} \partial \bar{z}_{j}}$ for a $\Delta_{g_{\epsilon}}$-harmonic function $u_{\epsilon}$.

Lemma 3.3. Under the same assumptions as in Lemma 3.2, along the "bad" directions $z_{1}, z_{2}$, $\Delta_{\epsilon, 1} u_{\epsilon}$ and $\Delta_{\epsilon, 2} u_{\epsilon}$ satisfy the estimates
$$\sup _{x \in B(p, R / 2)}\left(\left|\Delta_{\epsilon, 1} u_{\epsilon}\right|(x)+\left|\Delta_{\epsilon, 2} u_{\epsilon}\right|(x)\right) \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u_{\epsilon}}{R^{2}} .$$

As in the proof of Cheng-Yau gradient estimates, we will work on the function $f=f_{\epsilon}=\log u$ and we only need to prove the estimate for $\Delta_{1, \epsilon} u_{\epsilon}$. We write $\Delta_{1, \epsilon} f:=\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2} f}{\partial z_{1} \partial \bar{z}_{1}}$.

As above, we will omit the subscript $\epsilon$ in $\Delta_{1, \epsilon} f$. We first observe that
$$\Delta_{1} \Delta_{g_{\epsilon}} f=\Delta_{g_{\epsilon}} \Delta_{1} f .$$
(3.10) can be checked from the definitions by the property that $g_{\epsilon}$ is a product-metric. Indeed
$$\begin{aligned}
\Delta_{1} \Delta_{g_{\epsilon}} f & =\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}}\left(\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2} f}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}} \frac{\partial^{2} f}{\partial z_{2} \partial \bar{z}_{2}}+\sum_{j} \frac{\partial^{2} f}{\partial z_{j} \partial \bar{z}_{j}}\right) \\
& =\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}} \Delta_{1} f+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}} \Delta_{1} f+\sum_{j=3}^{n} \frac{\partial^{2}}{\partial z_{j} \partial \bar{z}_{j}} \Delta_{1} f \\
& =\Delta_{g_{e}} \Delta_{1} f .
\end{aligned}$$

On the other hand, note that by (3.6) $\Delta_{g_{\epsilon}} f=\Delta_{g} f=-|\nabla f|^{2}$. By choosing a normal frame $\left\{e_{1}, \ldots, e_{n}\right\}$ at some point $x$ such that $d g(x)=0$ and $\Delta_{1} f=f_{1 \overline{1}}$, we calculate
$$\begin{aligned}
\Delta_{1}|\nabla f|^{2} & =\left(f_{j} f_{\bar{j}}\right)_{1 \overline{1}} \\
& =f_{j 1} f_{\bar{j} \overline{1}}+f_{j \overline{1}} f_{\bar{j} 1}+f_{j 1 \overline{1}} f_{\bar{j}}+f_{j} f_{\bar{j} 1 \overline{1}} \\
& =f_{j 1} f_{\bar{j} \overline{1}}+f_{j \overline{1}} f_{\bar{j} 1}+f_{j} f_{\overline{1} \bar{j} \bar{j}}+f_{\bar{j}}\left(f_{1 \overline{1} j}+f_{m} R_{1 \bar{m} j \overline{1}}\right) \\
& =\left|\nabla_{1} \nabla f\right|^{2}+\left|\nabla_{1} \bar{\nabla} f\right|^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle+f_{m} f_{\bar{j}} R_{1 \overline{1} j \bar{m}} \\
& \geq\left(\Delta_{1} f\right)^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle .
\end{aligned}$$
Then it follows that
$$\Delta\left(-\Delta_{1} f\right)=-\Delta_{1} \Delta f=\Delta_{1}|\nabla f|^{2} \geq\left(\Delta_{1} f\right)^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle .$$
Let $\varphi:[0,1] \rightarrow[0,1]$ be a standard cut-off function such that $\left.\varphi\right|_{[0,1 / 2]}=1$ and $\left.\varphi\right|_{[2 / 3,1]}=0$. We also define $\varphi(x)=\varphi\left(\frac{r(x)}{R}\right)$. Then consider the function $G:=\varphi^{2} \cdot\left(-\Delta_{1} f\right)$. We calculate
$$\begin{aligned}
\Delta G & =\Delta\left(\varphi^{2}\left(-\Delta_{1} f\right)\right) \\
& =\varphi^{2} \Delta\left(-\Delta_{1} f\right)+2 \operatorname{Re}\left\langle\nabla \varphi^{2}, \bar{\nabla}\left(-\Delta_{1} f\right)\right\rangle+\left(-\Delta_{1} f\right) \Delta \varphi^{2} \\
& \geq \varphi^{2}\left(\left(\Delta_{1} f\right)^{2}+2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle\right)+2 \operatorname{Re}\left\langle\nabla \varphi^{2}, \bar{\nabla}\left(-\Delta_{1} f\right)\right\rangle+\left(-\Delta_{1} f\right) \Delta \varphi^{2} .
\end{aligned}$$
We want to estimate the upper bound of $G$. If the maximum value of $G=\varphi^{2}\left(-\Delta_{1} f\right)$ is negative, we are done. So we assume the maximum of $G$ on $B(p, R)$ is positive, which is achieved at some
point $p_{\text {max }} \in B(p, 2 R / 3)$. Hence at $p_{\text {max }}$, we have $\left(-\Delta_{1} f\right)>0$. By Laplacian comparison that $\Delta r \leq \frac{2 n-1}{r}$, we get at $p_{\text {max }}$,
$$\Delta \varphi^{2} \geq \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) .$$
Thus at $p_{\text {max }}$, the last term on RHS of (3.12) is
$$\geq\left(-\Delta_{1} f\right) \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) .$$
Substituting this into (3.12), it follows that at $p_{\text {max }}, \Delta G \leq 0$ and $\nabla \Delta_{1} f=-\frac{2}{\varphi} \Delta_{1} f \nabla \varphi$ and
$$\begin{aligned}
0 \geq & \Delta G \\
\geq & \varphi^{2}\left(\Delta_{1} f\right)^{2}+2 \varphi^{2} \operatorname{Re}\left\langle\nabla f, \bar{\nabla} \Delta_{1} f\right\rangle+4 \varphi \operatorname{Re}\left\langle\nabla \varphi, \bar{\nabla}\left(-\Delta_{1} f\right)\right\rangle \\
& \quad+\left(-\Delta_{1} f\right) \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \\
\geq & \varphi^{2}\left(\Delta_{1} f\right)^{2}-4 \varphi\left|\Delta_{1} f\right||\nabla f||\nabla \varphi|+8 \Delta_{1} f|\nabla \varphi|^{2}+\left(-\Delta_{1} f\right) \frac{2}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \\
= & \frac{G^{2}}{\varphi^{2}}-4 \varphi^{-1} G|\nabla f||\nabla \varphi|-8 G \frac{|\nabla \varphi|^{2}}{\varphi^{2}}+\frac{2 G}{R^{2} \varphi^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \\
\geq & \frac{G^{2}}{\varphi^{2}}-4 \frac{\left|\varphi^{\prime}\right||\nabla f|}{R \varphi} G-8 \frac{\left|\varphi^{\prime}\right|^{2}}{R^{2} \varphi^{2}} G+\frac{2 G}{R^{2} \varphi^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) .
\end{aligned}$$
Therefore at $p_{\text {max }} \in B(p, 2 R / 3)$, it holds that
$$G^{2}-4 \frac{\varphi\left|\varphi^{\prime} \nabla f\right|}{R} G-8 \frac{\left|\varphi^{\prime}\right|^{2}}{R^{2}} G+\frac{2 G}{R^{2}}\left((2 n-1) \varphi \varphi^{\prime}+\varphi \varphi^{\prime \prime}+\left(\varphi^{\prime}\right)^{2}\right) \leq 0,$$
combining (3.8) and the fact that $\varphi, \varphi^{\prime}, \varphi^{\prime \prime}$ are all uniformly bounded, we can get at $p_{\text {max }}$
$$G^{2} \leq C(n) R^{-2} G \quad \Rightarrow \quad G\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$
Then for any $x \in B(p, R / 2)$, where $\varphi=1$, we have
$$-\Delta_{1} f(x)=G(x) \leq G\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$
Moreover, recall that $f=\log u$ and $-\Delta_{1} f=-\frac{\Delta_{1} u}{u}+\left|\nabla_{1} f\right|^{2}$, therefore it follows that
$$\sup _{x \in B(p, R / 2)}\left(-\frac{\Delta_{1} u}{u}(x)\right) \leq \frac{C(n)}{R^{2}} .$$
This in particular implies that
$$\sup _{x \in B(p, R / 2)}\left(-\Delta_{1} u(x)\right) \leq C(n) \frac{\operatorname{osc}_{B(p, R / 2)} u}{R^{2}} \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .$$

On the other hand, by considering the function $\hat{u}=\max _{B(p, R)} u-u$, which is still a positive $g_{\epsilon}$-harmonic function $\Delta_{g} \hat{u}=\Delta_{g_{\epsilon}} \hat{u}=0$. Applying (3.15) to the function $\hat{u}$, we get
$$\sup _{x \in B(p, R / 2)}\left(\frac{\Delta_{1} u(x)}{\max _{B(p, R)} u-u(x)}\right)=\sup _{x \in B(p, R / 2)}\left(-\frac{\Delta_{1} \hat{u}}{\hat{u}}(x)\right) \leq \frac{C(n)}{R^{2}}$$
which yields that
$$\sup _{x \in B(p, R / 2)} \Delta_{1} u(x) \leq C(n) \frac{\operatorname{osc}_{B(p, R / 2)} u}{R^{2}} .$$

Combining (3.18) and (3.16), we get
$$\sup _{x \in B(p, R / 2)}\left|\Delta_{1} u\right|(x) \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .$$
3.1.4. Mixed derivatives estimates. In this subsection, we will estimate the following mixed derivatives
$$\left|\nabla_{1} \nabla_{2} f\right|^{2}=\frac{\partial^{2} f}{\partial z_{1} \partial z_{2}} \overline{\frac{\partial^{2} f}{\partial z_{1} \partial z_{2}}} g^{1 \overline{1}} g^{2 \overline{2}}, \quad\left|\nabla_{1} \nabla_{\overline{2}} f\right|^{2}=\frac{\partial^{2} f}{\partial z_{1} \partial \bar{z}_{2}} \overline{\frac{\partial^{2} f}{\partial z_{1} \partial \bar{z}_{2}}} g^{1 \overline{1}} g^{2 \overline{2}},$$
where as before $f=\log u$ and $u$ is a positive harmonic function of $\Delta_{g_{\epsilon}}$. Here for simplicity, we omit the subscript $\epsilon$ in $u_{\epsilon}, f_{\epsilon}$ and $g_{\epsilon}$. Observing that since $g_{\epsilon}=g$ is a product metric with the non-zero components $g_{k \bar{k}}$ depending only on $z_{k}$, it follows that the curvature tensor
$$R_{i \bar{j} k \bar{l}}=-\frac{\partial^{2} g_{i \bar{j}}}{\partial z_{k} \partial \bar{z}_{l}}+g^{p \bar{q}} \frac{\partial g_{i \bar{q}}}{\partial z_{k}} \frac{\partial g_{p \bar{j}}}{\partial \bar{z}_{l}}$$
vanishes unless $i=j=k=l=1$ or 2, and also $R_{\bar{i} \bar{i} \bar{i}} \geq 0$ for all $i=1, \ldots, n$.
We fix some notations: we will write $f_{12}=\nabla_{1} \nabla_{2} f$ (in fact this is just the ordinary derivative of $f$ w.r.t. $g$, since $g$ is a product metric), $\left|f_{12}\right|_{g}^{2}=\left|\nabla_{1} \nabla_{2} f\right|_{g}^{2}$, etc.

Let us first recall that the equation (3.11) implies
$$\begin{aligned}
\Delta\left(-\Delta_{1} f-\Delta_{2} f\right)= & \sum_{k=1}^{n}\left(g^{1 \overline{1}} g^{k \bar{k}} f_{1 k} f_{\overline{1} \bar{k}}+g^{1 \overline{1}} g^{k \bar{k}} f_{1 \bar{k}} f_{\overline{1} k}+g^{2 \overline{2}} g^{k \bar{k}} f_{2 k} f_{\overline{2} \bar{k}}+g^{2 \overline{2}} g^{k \bar{k}} f_{2 \bar{k}} f_{k \overline{2}}\right) \\
& -2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(-\Delta_{1} f-\Delta_{2} f\right)\right\rangle+f_{1} f_{\overline{1}} g^{1 \overline{1}} g^{1 \overline{1}} R_{1 \overline{1} 1 \overline{1}}+f_{2} f_{\overline{2}} g^{2 \overline{2}} g^{2 \overline{2}} R_{2 \overline{2} 2 \overline{2}} \\
\geq & \sum_{k=1}^{n}\left(\left|\nabla_{1} \nabla_{k} f\right|^{2}+\left|\nabla_{1} \nabla_{\bar{k}} f\right|^{2}+\left|\nabla_{2} \nabla_{k} f\right|^{2}+\left|\nabla_{2} \nabla_{\bar{k}} f\right|^{2}\right) \\
& -2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(-\Delta_{1} f-\Delta_{2} f\right)\right\rangle
\end{aligned}$$

Next we calculate $\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2}$. For notation convenience we will write $f^{12}=f_{\overline{1} \overline{2}} g^{1 \overline{1}} g^{2 \overline{2}}$, and hence $\left|\nabla_{1} \nabla_{2} f\right|^{2}=f_{12} f^{12}$. We calculate
$$\begin{aligned}
\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2} & =g^{k \bar{l}}\left(f_{12} f^{12}\right)_{k \bar{l}}=g^{k \bar{k}}\left(f_{12} f^{12}\right)_{k \bar{k}} \quad \text { (since } g \text { is a product metric) } \\
& =g^{k \bar{k}}\left(f_{12 k \bar{k}} f^{12}+f_{12 k} f_{, \overline{,}}^{12}+f_{12 \bar{k}} f_{, k}^{12}+f_{12} f_{, k \bar{k}}^{12}\right) .
\end{aligned}$$
The first term on the RHS of (3.21) is (by Ricci identities and switching the indices)
$$\begin{aligned}
& g^{k \bar{k}} f^{12}\left(f_{k 1 \bar{k} 2}+g^{m \bar{m}} f_{m 1} R_{k \bar{m} 2 \bar{k}}+g^{m \bar{m}} f_{k m} R_{1 \bar{m} 2 \bar{k}}\right) \\
= & g^{k \bar{k}} f^{12}\left(f_{k \bar{k} 12}+g^{m \bar{m}} f_{m 2} R_{k \bar{m} 1 \bar{k}}+g^{m \bar{m}} f_{m} R_{k \bar{m} 1 \bar{k}, 2}+g^{m \bar{m}} f_{m 1} R_{k \bar{m} 2 \bar{k}}+g^{m \bar{m}} f_{k m} R_{1 \bar{m} 2 \bar{k}}\right) \\
= & g^{k \bar{k}} f^{12}\left(f_{k \bar{k} 12}+g^{m \bar{m}} f_{m 2} R_{k \bar{m} 1 \bar{k}}+g^{m \bar{m}} f_{m 1} R_{k \bar{m} 2 \bar{k}}\right) \\
= & g^{k \bar{k}} f^{12} f_{k \bar{k} 12}+g^{1 \overline{1}} g^{1 \overline{1}} f^{12} f_{21} R_{1 \overline{1} 1 \overline{1}}+g^{2 \overline{2}} g^{2 \overline{2}} f^{12} f_{12} R_{2 \overline{2} 2 \overline{2}},
\end{aligned}$$
and the last term on the RHS of (3.21) is the conjugate of the first term, hence we get
$$\begin{aligned}
\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2}= & 2 \operatorname{Re}\left(f^{12}(\Delta f)_{12}\right)+2 f^{12} f_{12}\left(g^{1 \overline{1}} g^{1 \overline{1}} R_{1 \overline{1} 1 \overline{1}}+g^{2 \overline{2}} g^{2 \overline{2}} R_{2 \overline{2} 2 \overline{2}}\right) \\
& +g^{k \bar{k}} f_{12 k} f^{12}{ }_{, \bar{k}}+g^{k \bar{k}} f_{12 \bar{k}} f^{12}{ }_{, k} .
\end{aligned}$$

Recall from (3.6) we have $\Delta f=-|\nabla f|^{2}$, hence the first term on RHS of (3.23) is
$$\begin{aligned}
2 \operatorname{Re}\left(f^{12}(\Delta f)_{12}\right) & =2 \operatorname{Re}\left(f^{12}\left(-|\nabla f|^{2}\right)_{12}\right) \\
& =-2 \operatorname{Re}\left(f^{12} g^{k \bar{k}}\left(f_{k 12} f_{\bar{k}}+f_{k 1} f_{\bar{k} 2}+f_{k 2} f_{\bar{k} 1}+f_{k} f_{\bar{k} 12}\right)\right) \\
& =-2 \operatorname{Re}\left(f^{12} g^{k \bar{k}}\left(f_{12 k} f_{\bar{k}}+f_{k 1} f_{\bar{k} 2}+f_{k 2} f_{\bar{k} 1}+f_{k} f_{12 \bar{k}}-f_{k} f_{m} R_{1 \bar{m} 2 k} g^{m \bar{m}}\right)\right) \\
& \left.=-\left.4 \operatorname{Re}\langle\nabla f, \bar{\nabla}| \nabla_{1} \nabla_{2} f\right|^{2}\right\rangle-2 \operatorname{Re}\left(f^{12} g^{k \bar{k}} f_{k 1} f_{2 \bar{k}}+f^{12} g^{k \bar{k}} f_{k 2} f_{\bar{k} 1}\right)
\end{aligned}$$
Combining (3.24) and (3.23), we get
$$\begin{aligned}
\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2} \geq & \left.-\left.4 \operatorname{Re}\langle\nabla f, \bar{\nabla}| \nabla_{1} \nabla_{2} f\right|^{2}\right\rangle+\sum_{k}\left(f_{12 k} f^{12 k}+f_{12 \bar{k}} f^{12 \bar{k}}\right) \\
& -2 \sum_{k}\left(\left|\nabla_{1} \nabla_{2} f\right|\left|\nabla_{1} \nabla_{k} f\right|\left|\nabla_{2} \nabla_{\bar{k}} f\right|+\left|\nabla_{1} \nabla_{2} f\right|\left|\nabla_{2} \nabla_{k} f\right|\left|\nabla_{1} \nabla_{\bar{k}} f\right|\right) .
\end{aligned}$$
On the other hand we have by Kato's inequality
$$\begin{aligned}
\Delta\left|\nabla_{1} \nabla_{2} f\right|^{2} & =2\left|\nabla_{1} \nabla_{2} f\right| \Delta\left|\nabla_{1} \nabla_{2} f\right|+2|\nabla| \nabla_{1} \nabla_{2} f| |^{2} \\
& \leq 2\left|\nabla_{1} \nabla_{2} f\right| \Delta\left|\nabla_{1} \nabla_{2} f\right|+\sum_{k}\left|\nabla_{k} \nabla_{1} \nabla_{2} f\right|^{2}+\left|\nabla_{\bar{k}} \nabla_{1} \nabla_{2} f\right|^{2} \\
& =2\left|\nabla_{1} \nabla_{2} f\right| \Delta\left|\nabla_{1} \nabla_{2} f\right|+\sum_{k} f_{12 k} f^{12 k}+f_{12 \bar{k}} f^{12 \bar{k}} .
\end{aligned}$$
Combining (3.25) and (3.26) it follows that
$$\Delta\left|\nabla_{1} \nabla_{2} f\right| \geq-2 \operatorname{Re}\langle\nabla f, \bar{\nabla}| \nabla_{1} \nabla_{2} f| \rangle-\sum_{k}\left(\left|\nabla_{1} \nabla_{k} f\right|\left|\nabla_{2} \nabla_{\bar{k}} f\right|+\left|\nabla_{2} \nabla_{k} f\right|\left|\nabla_{1} \nabla_{\bar{k}} f\right|\right) .$$
Combining (3.20), (3.27) and applying Cauchy-Schwarz inequality, we have
$$\begin{aligned}
& \Delta\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right) \\
\geq- & -2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)\right\rangle \\
& \quad+\sum_{k=1}^{n}\left(\left|\nabla_{1} \nabla_{k} f\right|^{2}+\left|\nabla_{1} \nabla_{\bar{k}} f\right|^{2}+\left|\nabla_{2} \nabla_{k} f\right|^{2}+\left|\nabla_{2} \nabla_{\bar{k}} f\right|^{2}\right) .
\end{aligned}$$
Note that the sum on the RHS of (3.27) is (recall under our notation $\left|\nabla_{1} \nabla_{\overline{1}} f\right|^{2}=\left(\Delta_{1} f\right)^{2}$ )
$$\geq\left|\nabla_{1} \nabla_{2} f\right|^{2}+\left|-\Delta_{1} f\right|^{2}+\left|-\Delta_{2} f\right|^{2} \geq \frac{1}{12}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)^{2},$$
so we get the following equation
$$\begin{aligned}
& \Delta\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right) \\
\geq & -2 \operatorname{Re}\left\langle\nabla f, \bar{\nabla}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)\right\rangle \\
& +\frac{1}{12}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)^{2} .
\end{aligned}$$
Denote $Q=\eta^{2}\left(\left|\nabla_{1} \nabla_{2} f\right|+2\left(-\Delta_{1} f-\Delta_{2} f\right)\right)=: \eta^{2} Q_{1}$, where $\eta(x)=\tilde{\eta}(r(x) / R)$ and $\tilde{\eta}$ is a cut-off function such that $\left.\tilde{\eta}\right|_{[0,1 / 3]}=1$ and $\left.\tilde{\eta}\right|_{[1 / 2,1]}=0$. The following arguments are similar to the previous
two cases. We calculate
$$\begin{aligned}
\Delta Q & =\eta^{2} \Delta Q_{1}+2 \operatorname{Re}\left\langle\nabla \eta^{2}, \nabla Q_{1}\right\rangle+Q_{1} \Delta \eta^{2} \\
& \geq-2 \eta^{2} \operatorname{Re}\left\langle\nabla f, \bar{\nabla} Q_{1}\right\rangle+2 \operatorname{Re}\left\langle\nabla \eta^{2}, \nabla Q_{1}\right\rangle+\eta^{2} \frac{Q_{1}^{2}}{12}+Q_{1} \Delta \eta^{2} .
\end{aligned}$$
Apply maximum principle to $Q$ and if the $\max Q \leq 0$, we are done. So we may assume that $\max Q>0$ and is attained at $p_{\text {max }}$, thus at $p_{\text {max }}, Q_{1}>0, \Delta Q \leq 0, \nabla Q_{1}=-2 \eta^{-1} Q_{1} \nabla \eta$ and
$$Q_{1} \Delta \eta^{2} \geq Q_{1} \frac{2}{R^{2}}\left((2 n-1) \eta \eta^{\prime}+\eta \eta^{\prime \prime}+\left(\eta^{\prime}\right)^{2}\right) .$$
So at $p_{\text {max }}$ it holds that
$$\begin{aligned}
0 & \geq \Delta Q \\
& \geq 4 \eta Q_{1} \operatorname{Re}\langle\nabla f, \bar{\nabla} \eta\rangle-8 Q_{1}|\nabla \eta|^{2}+\eta^{2} \frac{Q_{1}^{2}}{12}+Q_{1} \frac{2}{R^{2}}\left((2 n-1) \eta \eta^{\prime}+\eta \eta^{\prime \prime}+\left(\eta^{\prime}\right)^{2}\right) \\
& =\frac{Q^{2}}{12 \eta^{2}}+4 Q \eta^{-1} \operatorname{Re}\langle\nabla f, \bar{\nabla} \eta\rangle-\frac{8 Q}{\eta^{2}} \frac{\left(\eta^{\prime}\right)^{2}}{R^{2}}+\frac{2 Q}{R^{2} \eta^{2}}\left((2 n-1) \eta \eta^{\prime}+\eta \eta^{\prime \prime}+\left(\eta^{\prime}\right)^{2}\right) \\
& \geq \frac{1}{\eta^{2}}\left(\frac{Q^{2}}{12}-\frac{40|\nabla f|}{R} Q-\frac{800}{R^{2}} Q-\frac{100 n}{R^{2}} Q\right)
\end{aligned}$$
where we choose $\eta$ such that $\left|\eta^{\prime}\right|,\left|\eta^{\prime \prime}\right| \leq 10$, for example. Therefore at $p_{\text {max }} \in B(p, R / 2)$ we have
$$\frac{Q^{2}}{12}-Q\left(\frac{40|\nabla f|}{R}+\frac{800}{R^{2}}+\frac{100 n}{R^{2}}\right) \leq 0 \quad \Rightarrow \quad Q\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}},$$
since $\sup _{B(p, R / 2)}|\nabla f| \leq C(n) R^{-1}$ from the previous estimates. Then for any $x \in B(p, R / 3)$ we have
$$Q_{1}(x)=\eta^{2}(x) Q_{1}(x)=Q(x) \leq Q\left(p_{\max }\right) \leq \frac{C(n)}{R^{2}} .$$
Thus it follows that
$$\left|\nabla_{1} \nabla_{2} f\right|(x) \leq Q_{1}(x)+2\left(\Delta_{1} f(x)+\Delta_{2} f(x)\right) \leq \frac{C(n)}{R^{2}}+2\left(\Delta_{1} f(x)+\Delta_{2} f(x)\right) .$$
On the other hand from $\left|\nabla_{1} \nabla_{2} f\right|=\left|\frac{\nabla_{1} \nabla_{2} u}{u}-\frac{\nabla_{1} u}{u} \frac{\nabla_{2} u}{u}\right|$
$$\begin{aligned}
\left|\nabla_{1} \nabla_{2} u\right|(x) & \leq\left|\nabla_{1} \nabla_{2} f(x)\right| u(x)+u(x) \frac{\left|\nabla_{1} u(x)\right|}{u} \frac{\left|\nabla_{2} u(x)\right|}{u} \\
& \leq C(n) \frac{u(x)}{R^{2}}+2 \Delta_{1} u(x)+2 \Delta_{2} u(x)+u(x) \frac{\left|\nabla_{1} u(x)\right|}{u} \frac{\left|\nabla_{2} u(x)\right|}{u} \\
& \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .
\end{aligned}$$
Therefore we obtain that
$$\sup _{B(p, R / 3)}\left|\nabla_{1} \nabla_{2} u\right| \leq C(n) \frac{\operatorname{osc}_{B(p, R)} u}{R^{2}} .$$
By exactly the same argument we can also get similar estimates for $\left|\nabla_{1} \nabla_{\overline{2}} u\right|$ and $\left|\nabla_{1} \nabla_{k} u\right|+\left|\nabla_{1} \nabla_{\bar{k}} u\right|$ for $k \neq 1$.

Hence we have proved the following lemma:
Lemma 3.4. There exists a constant $C(n)>0$ such that for the solution $u_{\epsilon}$ to the equation (3.4)
$$\sup _{B_{g_{\epsilon}}(0, R / 2)}\left(\left|\nabla_{i} \nabla_{j} u_{\epsilon}\right|_{g_{\epsilon}}+\left|\nabla_{i} \nabla_{\bar{j}} u_{\epsilon}\right|_{g_{\epsilon}}\right) \leq C(n) \frac{\operatorname{osc}_{B_{g_{\epsilon}}(0, R)} u_{\epsilon}}{R^{2}},$$
for all $i, j=1,2, \cdots, n$.
3.1.5. Convergence of $u_{\epsilon}$. In this section, we will show the Dirichlet problem (3.1) admits a unique solution for any $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$. We will write $B_{\boldsymbol{\beta}}=B_{\boldsymbol{\beta}}(0,1)$ for notation simplicity in this subsection.

Proposition 3.1. The Dirichlet boundary value problem (3.1) admits a unique solution $u \in C^{2}\left(B_{\boldsymbol{\beta}} \backslash \mathcal{S}\right) \cap$ $C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ for any $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}\right)$. Moreover, $u$ satisfies the estimates in Lemmas 3.2, 3.3 and 3.4 with $u_{\epsilon}$ replaced by $u$ and the metric balls replaced by those under the metric $g_{\boldsymbol{\beta}}$, which we will refer as "derivatives estimates" throughout this section.

Proof. Given the estimates of $u_{\epsilon}$ as in lemmas 3.2, 3.3 and 3.4, we can derive the uniform local $C^{2, \alpha}$ estimates of $u_{\epsilon}$ on any compact subsets of $B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}$.

The $C^{0}$ estimates of $u_{\epsilon}$ follow immediately from the maximum principle (see Lemma 3.1).
Take any compact subsets $K \Subset K^{\prime} \Subset B_{\boldsymbol{\beta}}(0,1)$. By Lemma 3.3, we have
$$\begin{array}{r}
\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial u_{\epsilon}}{\partial z_{1}}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial u_{\epsilon}}{\partial z_{2}}\right|+\left|\frac{\partial u_{\epsilon}}{\partial s_{j}}\right|\right) \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\beta}\right)}, \\
\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial^{2} u_{\epsilon}}{\partial s_{k} \partial z_{1}}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial^{2} u_{\epsilon}}{\partial s_{k} \partial z_{2}}\right|+\left|\frac{\partial^{2} u_{\epsilon}}{\partial s_{k} \partial s_{j}}\right|\right) \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\boldsymbol{\beta}}\right)^{2}},
\end{array}$$
and the third-order estimates
$$\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial^{3} u_{\epsilon}}{\partial z_{1} \partial s_{k} \partial s_{l}}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial^{3} u_{\epsilon}}{\partial z_{2} \partial s_{k} \partial s_{l}}\right|+\left|\frac{\partial^{3} u_{\epsilon}}{\partial s_{j} \partial s_{k} \partial s_{l}}\right|\right) \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\boldsymbol{\beta}}\right)^{3}} .$$
Moreover, applying the gradient estimate to the $\Delta_{g_{\epsilon}}$-harmonic function $\Delta_{\epsilon, 1} u_{\epsilon}$, we get
$$\sup _{K^{\prime}}\left(\left|z_{1}\right|^{1-\beta_{1}}\left|\frac{\partial}{\partial z_{1}} \Delta_{\epsilon, 1} u_{\epsilon}\right|+\left|z_{2}\right|^{1-\beta_{2}}\left|\frac{\partial}{\partial z_{2}} \Delta_{\epsilon, 1} u_{\epsilon}\right|+\left|\frac{\partial}{\partial s_{j}} \Delta_{\epsilon, 1} u_{\epsilon}\right|\right) \leq C(n) \frac{\left\|u_{\epsilon}\right\|_{\infty}}{d\left(K^{\prime}, \partial B_{\beta}\right)^{3}} .$$
From (3.34), (3.35) and (3.36), we see that the functions $u_{\epsilon}$ have uniform $C^{3}$ estimates in the "tangential directions" on any compact subset of $B_{\boldsymbol{\beta}}(0,1)$. Moreover, for any fixed small constant $\delta>0$, let $T_{\delta}(\mathcal{S})$ be the tubular neighborhood of $\mathcal{S}$. We consider the equation
$$\Delta_{\epsilon} u_{\epsilon}=\left(\left|z_{1}\right|^{2}+\epsilon\right)^{1-\beta_{1}} \frac{\partial^{2} u_{\epsilon}}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{1-\beta_{2}} \frac{\partial^{2} u_{\epsilon}}{\partial z_{2} \partial \bar{z}_{2}}+\sum_{j=5}^{2 n} \frac{\partial^{2} u_{\epsilon}}{\partial s_{j}^{2}}=0, \text { on } K^{\prime} \backslash T_{\delta / 2}(\mathcal{S}),$$
which is strictly elliptic (with ellipticity depending only on $\delta>0$ ). Hence by standard elliptic Schauder theory, we also have $C^{2, \alpha}$-estimates of $u_{\epsilon}$ in the "transversal directions" (i.e. normal to $\mathcal{S}$ ) and the mixed directions, on the compact subset $K \backslash T_{\delta}(\mathcal{S})$. By taking $\delta \rightarrow 0, K \rightarrow B_{\boldsymbol{\beta}}$, and a diagonal argument, up to a subsequence $u_{\epsilon}$ converge in $C_{\text {loc }}^{2, \alpha}\left(B_{\boldsymbol{\beta}} \backslash \mathcal{S}\right)$ to a function $u \in C^{2, \alpha}\left(B_{\boldsymbol{\beta}} \backslash \mathcal{S}\right)$. Clearly, $u$ satisfies the equation $\Delta_{\boldsymbol{\beta}} u=0$ on $B_{\boldsymbol{\beta}} \backslash \mathcal{S}$, and the estimates (3.34), (3.35) and (3.36) hold for $u$ outside $\mathcal{S}$, which implies that $u$ can be continuously extended through $\mathcal{S}$ and defines a continuous function in $B_{\boldsymbol{\beta}}(0,1)$. It remains to check the boundary value of $u$.
Claim: $u=\varphi$ on $\partial B_{\boldsymbol{\beta}}(0,1)$
It remains to show the limit function $u$ of $u_{\epsilon}$ satisfies the boundary condition $u=\varphi$ on $\partial B_{\boldsymbol{\beta}}(0,1)$, which will be proved by constructing suitable barriers as we did in [20].

The metric ball $B_{\boldsymbol{\beta}}(0,1)$ is given by
$$B_{\boldsymbol{\beta}}(0,1)=\left\{z \in \mathbb{C}^{n}\left|d_{\boldsymbol{\beta}}(0, z)^{2}:=\left|z_{1}\right|^{2 \beta_{1}}+\left|z_{2}\right|^{2 \beta_{2}}+\sum_{j=5}^{2 n} s_{j}^{2}<1\right\} .\right.$$
$B_{\boldsymbol{\beta}}(0,1) \subset B_{\mathbb{C}^{n}}(0,1)$ and their boundaries only intersect at $\mathcal{S}_{1} \cap \mathcal{S}_{2}$, where $z_{1}=z_{2}=0$. Fix any point $q \in \partial B_{\boldsymbol{\beta}}(0,1)$ and we consider the cases when $q \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ or $q \notin \mathcal{S}_{1} \cap \mathcal{S}_{2}$.

Case 1: $q \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$, i.e. $z_{1}(q)=z_{2}(q)=0$. Consider the point $q^{\prime}=-q \in \partial B_{\boldsymbol{\beta}}(0,1) \cap \partial B_{\mathbb{C}^{n}}(0,1)$, and $q$ is the unique farthest point to $q^{\prime}$ on $\partial B_{\boldsymbol{\beta}}(0,1)$ under the Euclidean distance, hence the function $\Psi_{q}(z):=d_{\mathbb{C}^{n}}\left(z, q^{\prime}\right)^{2}-4$ satisfies $\Psi_{q}(q)=0$ and $\Psi_{q}(z)<0$ for all $z \in \partial B_{\boldsymbol{\beta}}(0,1) \backslash\{q\}$. By the continuity of $\varphi$ for any $\delta>0$, there is a small neighborhood $V$ of $q$ such that $\varphi(q)-\delta<$ $\varphi(z)<\varphi(q)+\delta$ for all $z \in \partial B_{\boldsymbol{\beta}}(0,1) \cap V$ and on $\partial B_{\boldsymbol{\beta}}(0,1) \backslash V, \Psi_{q}$ is bounded above by a negative constant. Hence we can make $\varphi_{q}(z):=\varphi(q)-\delta+A \Psi_{q}(z)<\varphi(z)$ for all $z \in \partial B_{\boldsymbol{\beta}}(0,1)$ if $A$ is chosen large enough. The function $\varphi_{q}$ is $\Delta_{g_{\epsilon}}$-subharmonic hence by maximum principle we have $u_{\epsilon}(z) \geq \varphi_{q}(z)$ for all $z \in B_{\boldsymbol{\beta}}(0,1)$. Letting $\epsilon \rightarrow 0$ we get $u(z) \geq \varphi_{q}(z)$. Then taking $z \rightarrow q$ it follows that $\liminf _{z \rightarrow q} u(z) \geq \varphi(q)-\delta$, but $\delta>0$ is arbitrary so we have $\liminf _{z \rightarrow q} u(z) \geq \varphi(q)$.