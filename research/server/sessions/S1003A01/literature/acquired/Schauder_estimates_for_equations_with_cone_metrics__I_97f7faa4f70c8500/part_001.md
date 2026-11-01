---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Schauder estimates for equations with cone metrics, I]

---
source_file: 1612_00075.pdf
converter: mathpix
format: mmd
---

\title{
SCHAUDER ESTIMATES FOR EQUATIONS WITH CONE METRICS, I ${ }^{1}$
}

\author{
Bin Guo and Jian Song
}

\begin{abstract}
This is the first paper in a series to develop a linear and nonlinear theory for elliptic and parabolic equations on Kähler varieties with mild singularities. Donaldson has established a Schauder estimate for linear and complex Monge-Ampère equations when the background Kähler metrics on $\mathbb{C}^{n}$ have cone singularities along a smooth complex hypersurface. We prove a sharp pointwise Schauder estimate for linear elliptic and parabolic equations on $\mathbb{C}^{n}$ with background metric $g_{\beta}=\sqrt{-1}\left(d z_{1} \wedge d \overline{z_{1}}+\right.$ $\left.\ldots+\beta^{2}\left|z_{n}\right|^{-2(1-\beta)} d z_{n} \wedge d \overline{z_{n}}\right)$ for $\beta \in(0,1)$. Our results give an effective elliptic Schauder estimate of Donaldson and a direct proof for the short time existence of the conical Kähler-Ricci flow.
\end{abstract}

\section*{1. Introduction}

In [32], Yau considers complex Monge-Ampère equations with a singular right hand side as a generalization of his solution to the Calabi conjecture. More precisely, let $(X, \omega)$ be an $n$ -dimensional Kähler manifold with a Kähler form $\omega=\sqrt{-1} \sum g_{i j} d z_{i} \wedge d \overline{z_{j}}$ associated to a Kähler metric $g$. Let $L$ and $L^{\prime}$ be two holomorphic line bundles over $X$ equipped with two smooth hermitian metrics $h$ and $h^{\prime}$. Let $\sigma$ and $\sigma^{\prime}$ be two holomorphic sections of $L$ and $L^{\prime}$ respectively. Then various global and local regularity results are established in [32] for solutions of the following complex Monge-Ampère equation with suitable assumptions on $\beta, \beta^{\prime}>0$,
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=|\sigma|_{h}^{-2 \beta}\left|\sigma^{\prime}\right|_{h^{\prime}}^{2 \beta^{\prime}} e^{F} \omega^{n},$$
where $F \in C^{\infty}(X)$. A fundamental result of Kolodziej [15] shows that as long as $|\sigma|^{-2 \beta}\left|\sigma^{\prime}\right|^{2 \beta^{\prime}} e^{F} \in$ $L^{p}(X)$ for some $p>1$, there exists a unique solution $\varphi \in L^{\infty}(X) \cap P S H(X, \omega)$, where $P S H(X, \omega)$ is the set of all quasi-plurisubharmonic functions on $X$ associated to $\omega$. When $\beta^{\prime}=0$ and $D=\{\sigma=0\}$ is a smooth complex hypersurface of $X$, equation (1.1) becomes
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=|\sigma|_{h}^{-2 \beta} e^{F} \omega^{n} .$$
Equation (1.2) is considered by Donaldson [9] to obtain Kähler-Einstein metrics with cone singularities along the smooth divisor $D$. The curvature equation for $\omega_{\varphi}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi$ from equation (1.2) is given by
$$\operatorname{Ric}\left(\omega_{\varphi}\right)=(\operatorname{Ric}(\omega)-\sqrt{-1} \partial \bar{\partial} F-\beta \operatorname{Ric}(h))+\beta[D],$$
where $[D]$ is the nonnegative current defined by $[D]=\sqrt{-1} \partial \bar{\partial} \log |\sigma|^{2}$. By combining results from [9, 5], $\omega_{\varphi}$ is smooth on $X \backslash D$ and it is equivalent to the standard cone singularities in the conical Hölder sense. In fact, conical Einstein metrics were already studied with potential geometric applications in many literatures (cf. [28, 30, 17, 18]). The recent success in solving the Yau-Tian-Donaldson conjecture (cf. [27, 4, 5, 6, 29]) has also inspired many works on the study of canonical Kähler metrics with cone singularities and their relation to algebraic geometry (cf. [1, 13, 25, 7, 14, 19, 21, 33, 34, 10]). One of the main difficulties in solving (1.2) is how to derive a suitable Schauder estimate for the linearized equation of (1.2). Such an important estimate is first established by Donaldson in [9] with the classical approach of potential theory. Symmetry plays an essential role in the proof and it seems difficult to adapt this approach to more general settings of singular background metrics, in particular, Kähler metrics with cone singularities along divisors of simple normal crossings.

\footnotetext{
${ }^{1}$ Research supported in part by National Science Foundation grant DMS-1406124
}

The Schauder estimates for Laplace equations and heat equations are fundamental tools in both PDEs theories and geometric analysis. Apart from the classical potential theory, various proofs have been established by different important analytic techniques (cf. [2, 3, 24, 22, 23, 31]). Recently, an elementary and elegant pointwise Schauder estimate for the standard Laplace equation on $\mathbb{R}^{n}$ is obtained by Wang [31]. Wang's techniques are quite flexible and we are able to combine such perturbation techniques with geometric gradient estimates to prove sharp Schauder estimates for Laplace equations on $\mathbb{C}^{n}$ with a conical background Kähler metric.

Let $g_{\beta}$ be the standard conical Kähler metric on $\mathbb{C}^{n}$ defined by
$$g_{\beta}=\sqrt{-1}\left(d z_{1} \wedge d \overline{z_{1}}+\ldots+d z_{n-1} \wedge d \overline{z_{n-1}}+\beta^{2}\left|z_{n}\right|^{-2(1-\beta)} d z_{n} \wedge d \overline{z_{n}}\right),$$
for some $\beta \in(0,1)$, where $z=\left(z_{1}, \ldots, z_{n}\right)$ are the standard complex coordinates on $\mathbb{C}^{n}$. Let
$$\mathcal{S}=\left\{z_{n}=0\right\}$$
be the singular set of $g_{\beta}$. Obviously $g_{\beta}$ is a smooth flat Kähler metric on $\mathbb{C}^{n} \backslash \mathcal{S}$ and it extends to a conical Kähler metric on $\mathbb{C}^{n}$ with cone angle $2 \pi \beta$ along the hyperplane $\mathcal{S}$.

In this paper, we will consider the following conical Laplace equation with the background conical Kähler metric $g_{\beta}$ on $\mathbb{C}^{n}$
$$\Delta_{\beta} u=f, \quad \text { in } \quad B_{\beta}(0,1),$$
where $B_{\beta}(p, r)$ is the geodesic ball in $\left(\mathbb{C}^{n}, g_{\beta}\right)$ centered at $p$ of radius $r$, and
$$\Delta_{\beta}=\sum_{i, j=1}^{n}\left(g_{\beta}\right)^{i \bar{j}} \frac{\partial^{2}}{\partial z_{i} \partial \overline{z_{j}}}$$
is the Laplace operator associated to $g_{\beta}$. We introduce a family of first order differential operators which are already considered in [9].

Definition 1.1. We write
$$z_{i}=s_{2 i-1}+\sqrt{-1} s_{2 i}$$
in real coordinates for $i=1, \ldots, n-1$ and
$$r_{n}=\left|z_{n}\right|^{\beta}, \theta_{n}=\arg z_{n} .$$
in weighted polar coordinates. The differential operators $D_{j}$ for $j=1, \ldots, 2 n$ are defined by
$$D_{i}=\frac{\partial}{\partial s_{i}}, i=1,2, \ldots, 2 n-2 .$$
and
$$D_{2 n-1}=\frac{\partial}{\partial r_{n}}, D_{2 n}=\frac{\partial}{r_{n} \partial \theta_{n}} .$$

We now state the main result of the paper.
Theorem 1.1. Suppose $\beta \in(1 / 2,1)$ and $f(x)$ is Dini continuous on $B_{\beta}(0,1)$ with respect to $g_{\beta}$ for some $\beta \in(0,1)$. Let
$$\omega(r)=\sup _{d_{\beta}(z, w)<r, z, w \in B_{\beta}(0,1)}|f(z)-f(w)| .$$
If $u \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \cap L^{\infty}\left(B_{\beta}(0,1)\right)$ is a solution of the conical Laplace equation (1.3)
$$\Delta_{\beta} u=f,$$
then there exists $C=C(n, \beta)>0$ such that for any $p, q \in B_{\beta}\left(0, \frac{1}{2}\right) \backslash \mathcal{S}$,
$$\begin{aligned}
& \sum_{i, j=1}^{2 n-2}\left|D_{i} D_{j} u(p)-D_{i} D_{j} u(q)\right|+\left|\left(\left|z_{n}\right|^{2-2 \beta} \frac{\partial^{2} u}{\partial z_{n} \partial \overline{z_{n}}}\right)(p)-\left(\left|z_{n}\right|^{2-2 \beta} \frac{\partial^{2} u}{\partial z_{n} \partial \overline{z_{n}}}\right)(q)\right| \\
\leq & C\left(d \sup _{B_{\beta}(0,1)}|u|+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right)
\end{aligned}$$
and
$$\begin{aligned}
& \sum_{i=2 n-1}^{2 n} \sum_{j=1}^{2 n-2}\left|D_{i} D_{j} u(p)-D_{i} D_{j} u(q)\right| \\
\leq & C\left(d^{\frac{1}{\beta}-1} \sup _{B_{\beta}(0,1)}|u|+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{\frac{1}{\beta}-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta}} d r\right),
\end{aligned}$$
where $d=d_{\beta}(p, q)$ is the distance between $p$ and $q$ with respect to $g_{\beta}$.
The estimate (1.4) measures the Hölder continuity of second derivatives of the solution $u$ in the tangential directions of $\mathcal{S}$, while the estimate (1.5) measures Hölder continuity of mixed second derivatives in the tangential and transversal directions. The mixed derivative estimates are more difficult to handle. The case of $\beta \in(0,1 / 2]$ can be treated in the same fashion and is relatively easy with stronger estimates (c.f. Proposition 2.5).

The conical Hölder function spaces $C_{\beta}^{2, \alpha}$ (cf. Defintion 2.1) for the background Kähler metric $g_{\beta}$ is first introduced in [9]. It is also shown in [9] that if $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right)$ for some $\alpha \in$ $\left(0, \min \left\{\frac{1}{\beta}-1,1\right\}\right)$ and $\Delta_{\beta} u=f$, then
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1 / 2)\right)} \leq C(n, \beta, \alpha)\left(\|u\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}\right) .$$
As a direct consequence of Theorem 1.1, we derive the following sharp Schauder estimate, generalizing the Schauder estimate for the Laplace equation on Euclidean $\mathbb{R}^{n}$ and improving Donaldson's Schauder estimate (1.6).

Corollary 1.1. Suppose $\beta \in(1 / 2,1)$ and $f(x) \in C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)$ for some $\alpha \in\left(0, \min \left\{\frac{1}{\beta}-1,1\right\}\right)$. If $u \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \cap L^{\infty}\left(B_{\beta}(0,1)\right)$ is a solution of the conical Laplace equation (1.3), then $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\left(0, \frac{1}{2}\right)\right)$ and
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}\left(0, \frac{1}{2}\right)\right)} \leq C(n, \beta)\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\frac{\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}}{\alpha\left(\min \left\{\frac{1}{\beta}-1,1\right\}-\alpha\right)}\right) .$$

The Schauder estimate (1.7) improves Donaldson's original Schauder estimate in the way that it gives the sharp dependence on $\alpha$ for fixed $\beta$ and $u$ is only required to be bounded and locally $C^{2}$. Such dependence on $\alpha$ is a slight modification of the classical Schauder estimates for the standard Laplace equation on $\mathbb{R}^{n}$. In section 2, we will present formulae generalizing estimates (1.4) and (1.5). In particular, the dependance of the constant $C(n, \beta)$ in estimate (1.5) on $\beta$ can be explicitly formulated from the proof of Theorem 1.1.

Our method can be easily modified to derive a Schauder estimate for linear parabolic equations on $\mathbb{C}^{n}$ with the conical background Kähler metric $g_{\beta}$. In section 3, we apply similar techniques
to derive sharp Schauder estimates for linear parabolic equations with conical singularities. We first define the parabolic metric ball $\mathcal{Q}_{\beta}\left(P_{0}, r\right)$ centered at $P_{0}=\left(p_{0}, t_{0}\right)$ of radius $r$ by
$$\mathcal{Q}_{\beta}\left(P_{0}, r\right)=\left\{(p, t) \in \mathbb{C}^{n} \times[0, \infty) \mid d_{\mathcal{P}, \beta}\left((p, t),\left(p_{0}, t_{0}\right)\right)<r, t<t_{0}\right\},$$
where
$$d_{\mathcal{P}, \beta}\left((p, t),\left(p_{0}, t_{0}\right)\right)=\max \left\{d_{\beta}\left(p, p_{0}\right), \sqrt{\left|t-t_{0}\right|}\right\}$$
is the conical parabolic distance on $\mathbb{C}^{n} \times \mathbb{R}$. Denote
$$\mathcal{S}_{\mathcal{P}}=\{(p, t) \mid p \in \mathcal{S}, t \in[0, \infty)\} .$$
We now consider the following conical heat equation with respect to the background conical metric $g_{\beta}$,
$$\square_{\beta} u=f, \quad \mathcal{Q}_{\beta}((0,1), 1),$$
where $\square_{\beta}=\left(\frac{\partial}{\partial t}-\Delta_{\beta}\right) u$. The following theorem is the parabolic analogue of Theorem 1.1 for the pointwise Schauder estimate for solutions of the conical heat equation (1.8).

Theorem 1.2. Suppose $f(x, t)$ is Dini continuous on $\mathcal{Q}_{\beta}((0,1), 1)$ with respect to $d_{\mathcal{P}, \beta}$ for some $\beta \in(1 / 2,1)$ and let
$$\omega(r)=\sup _{d_{\mathcal{P}, \beta}\left(\left(p_{1}, t_{1}\right),\left(p_{2}, t_{2}\right)\right)<r,\left(p_{1}, t_{1}\right),\left(p_{2}, t_{2}\right) \in \mathcal{Q}_{\beta}((0,1), 1)}\left|f\left(p_{1}, t_{1}\right)-f\left(p_{2}, t_{2}\right)\right| .$$
If $u \in \mathcal{P}^{2}\left(\mathcal{Q}_{\beta}((0,1), 1) \backslash \mathcal{S}_{\mathcal{P}}\right) \cap L^{\infty}\left(\mathcal{Q}_{\beta}((0,1), 1)\right)$ is a solution of the conical heat equation (1.8), then there exists $C(n, \beta)>0$ such that for any $P, Q \in \mathcal{Q}_{\beta}\left((0,1), \frac{1}{2}\right) \backslash \mathcal{S}_{\mathcal{P}}$,
$$\begin{aligned}
& \sum_{i, j=1}^{2 n-2}\left|D_{i} D_{j} u(P)-D_{i} D_{j} u(Q)\right|+\left|\left(\left|z_{n}\right|^{2-2 \beta} \frac{\partial^{2} u}{\partial z_{n} \partial \overline{z_{n}}}\right)(P)-\left(\left|z_{n}\right|^{2-2 \beta} \frac{\partial^{2} u}{\partial z_{n} \partial \overline{z_{n}}}\right)(Q)\right| \\
\leq & C\left(d \sup _{B_{\beta}(0,1)}|u|+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right)
\end{aligned}$$
and
$$\begin{aligned}
& \sum_{i=2 n-1}^{2 n} \sum_{j=1}^{2 n-2}\left|D_{i} D_{j} u(P)-D_{i} D_{j} u(Q)\right| \\
\leq & C\left(d^{\frac{1}{\beta}-1} \sup _{B_{\beta}(0,1)}|u|+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{\frac{1}{\beta}-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta}} d r\right),
\end{aligned}$$
where $d=d_{\mathcal{P}, \beta}(P, Q)$.
Similarly like Corollary 1.1, we have the following parabolic Schauder estimates.
Corollary 1.2. Suppose $\beta \in(1 / 2,1)$ and $f \in \mathcal{P}_{\beta}^{0, \alpha}\left(\mathcal{Q}_{\beta}(0,1)\right)$ for some $\alpha \in\left(0, \min \left\{\frac{1}{\beta}-1,1\right\}\right)$. If $u \in \mathcal{P}^{2}\left(\mathcal{Q}_{\beta}((0,1), 1) \backslash \mathcal{S}\right) \cap L^{\infty}\left(\mathcal{Q}_{\beta}((0,1), 1)\right)$ is a solution of the conical heat equation (1.8), then $u \in \mathcal{P}_{\beta}^{2, \alpha}\left(\mathcal{Q}_{\beta}\left((0,1), \frac{1}{2}\right)\right)$ and
$$\|u\|_{\mathcal{P}_{\beta}^{2, \alpha}\left(\mathcal{Q}_{\beta}\left((0,1), \frac{1}{2}\right)\right)} \leq C(n, \beta)\left(\sup _{\mathcal{Q}_{\beta}((0,1), 1)}|u|+\frac{\|f\|_{\mathcal{P}_{\beta}^{0, \alpha}\left(\mathcal{Q}_{\beta}((0,1), 1)\right)}}{\alpha\left(\min \left\{\frac{1}{\beta}-1,1\right\}-\alpha\right)}\right),$$
where the $\mathcal{P}_{\beta}^{2, \alpha}$-norm and $\mathcal{P}_{\beta}^{0, \alpha}$-norm of functions are defined in Definition 3.1.

In [7], a parabolic Schauder estimate is derived by adapting the elliptic Schauder estimates in [9] and such an estimate leads to the short time existence of the Kähler-Ricci flow on a Kähler manifold with conical singularities along a smooth divisor. The argument in [7] is very long and based on asymptotic analysis for the heat kernel. Our approach is more direct and can be used for more general settings. In the sequel, we will prove the maximal time existence for the conical Kähler-Ricci flow on a Kähler manifold with cone singularities along divisors of simple normal crossings.

In the sequels, we will build the Schauder theory for Laplace and complex Monge-Ampère equations with a background Kähler metric with asymptotically cone singularities based on the techniques developed in this paper. A special case will be the Laplace equation of a background Kähler metric with conical singularities along divisors of simple normal crossings. Furthermore, we are interested in the more degenerate case when the cone angles are allowed to be greater than $2 \pi$ or equivalently $\beta>1$. Ultimately, we aim to develop a foundational theory to study analytic and geometric regularity for canonical Kähler metrics on Kähler varieties with mild singularities, in particular, Kähler-Einstein metrics on projective varieties with log terminal singularities. This might lead to deep understanding for the classification of Kähler varieties and algebraic singularities through singular canonical Kähler metrics.

\section*{2. Elliptic Schauder estimates}

We will prove Theorem 1.1 and Corollary 1.1 in this section.
2.1. Notations. Let $g_{\beta}$ be the standard cone metric on $\mathbb{C}^{n}=\mathbb{C}^{n-1} \times \mathbb{C}$ for some $\beta \in(0,1)$, given by
$$g_{\beta}=\sum_{j=1}^{n-1} \sqrt{-1} d z_{j} \wedge d \overline{z_{j}}+\beta^{2}\left|z_{n}\right|^{-2(1-\beta)} \sqrt{-1} d z_{n} \wedge d \overline{z_{n}}$$
It has conical singularities along the hyperplane
$$\mathcal{S}=\mathbb{C}^{n-1} \times\{0\}$$
with cone angle $2 \pi \beta \in(0,2 \pi)$. In the following we will also use $\left\{s_{1}, \ldots, s_{2 n-2}\right\}$ to be the real coordinates functions of $\mathbb{C}^{n-1}=\mathbb{R}^{2 n-2}$, where $z_{i}=s_{2 i-1}+\sqrt{-1} s_{2 i}$, for $i=1, \ldots, 2 n-2$.

We will denote $B_{\beta}(p, r)$ by the open metric ball with respect to $g_{\beta}$ centered at $p \in \mathbb{C}^{n}$ and of radius $r>0$. Let $d_{\beta}(x, y)$ be the distance of $x, y$ with respect to the metric $g_{\beta}$. Since $\beta \in(0,1)$, the smooth part of $\left(\mathbb{C}^{n}, g_{\beta}\right)$ is geodesic convex. More precisely, if $x, y \notin \mathcal{S}$, the minimal geodesic joining $x$ and $y$ does not intersect $\mathcal{S}$.
Definition 2.1. We define the $C_{\beta}^{0, \alpha}$-norm of a function $u$ on the ball $B_{\beta}(0,1)$ as
$$\|u\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}=\|u\|_{C^{0}\left(B_{\beta}(0,1)\right)}+\sup _{x \neq y \in B_{\beta}(0,1)} \frac{|u(x)-u(y)|}{d_{\beta}(x, y)^{\alpha}},$$
for $\alpha \in(0,1]$.
The following definition coincides with the Schauder norm introduced by Donaldson [9].
Definition 2.2. We define the $C_{\beta}^{2, \alpha}$-norm of a function $u$ on the ball $B_{\beta}(0,1)$ as
$$\begin{aligned}
\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right)}= & \|u\|_{C^{0}\left(B_{\beta}(0,1)\right)}+\sum_{i=1}^{2 n}\left\|D_{i} u\right\|_{C^{0}\left(B_{\beta}(0,1)\right)} \\
& +\sum_{i=1}^{2 n} \sum_{j=1}^{2 n-2}\left\|D_{i} D_{j} u\right\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}+\left\|\left|z_{n}\right|^{2-2 \beta} \frac{\partial^{2} u}{\partial z_{n} \partial \bar{z}_{n}}\right\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}
\end{aligned}$$
for $\alpha \in(0,1]$, where $D_{i}$ is defined in Definition 1.1 for $i=1,2, \ldots, 2 n$.
Definition 2.3. We decompose the gradient operator $\nabla_{g_{\beta}}$ by $\nabla_{g_{\beta}}=\left(D^{\prime}, D^{\prime \prime}\right)$, where $D^{\prime}$ and $D^{\prime \prime}$ are given by
$$D^{\prime}=\left(D_{1}, D_{2}, \ldots, D_{2 n-2}\right), \quad D^{\prime \prime}=\left(D_{2 n-1}, D_{2 n}\right) .$$

Obviously, $D^{\prime}$ commute with $D^{\prime \prime}$ and $\Delta_{\beta}$.
2.2. The maximum priniciple. Let $u \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\beta}(0,1)}\right)$ be a solution to the conical Laplace equation
$$\Delta_{\beta} u=\sum_{j=1}^{n-1} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}+\beta^{-2}\left|z_{n}\right|^{2(1-\beta)} \frac{\partial^{2} u}{\partial z_{n} \partial \bar{z}_{n}}=0, \quad \text { in } B_{\beta}(0,1) \backslash \mathcal{S} .$$
Then we have the following maximum principle.
Lemma 2.1. Suppose $u \in C^{0}\left(\overline{B_{\beta}(0,1)}\right) \cap C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right)$ solves the equation (2.1), then
$$\inf _{\partial B_{\beta}(0,1)} u \leq \inf _{B_{\beta}(0,1)} u \leq \sup _{B_{\beta}(0,1)} u \leq \sup _{\partial B_{\beta}(0,1)} u .$$
Proof. We first define $u_{\epsilon}(z)=u(z)+\epsilon \log \left|z_{n}\right|^{2}$ for any $\epsilon>0$. Since $u$ is continuous on $\overline{B_{\beta}(0,1)}$ and $u_{\epsilon}(z) \rightarrow-\infty$ as $z \rightarrow \mathcal{S}$, the maximum of $u_{\epsilon}$ in $\overline{B_{\beta}(0,1)}$ cannot be achieved at $\mathcal{S} \cap \overline{B_{\beta}(0,1)}$. Hence the standard maximum principle implies that the supremum of $u_{\epsilon}$ has to be obtained at $\partial B_{\beta}(0,1) \backslash \mathcal{S}$, that is, for any fixed $z \in B_{\beta}(0,1) \backslash \mathcal{S}$,
$$u_{\epsilon}(z) \leq \sup _{\partial B_{\beta}(0,1)} u_{\epsilon} \leq \sup _{\partial B_{\beta}(0,1)} u .$$
Letting $\epsilon \rightarrow 0$, we have $u(z) \leq \sup _{\partial B_{\beta}(0,1)} u$ and so $\sup _{B_{\beta}(0,1)} u \leq \sup _{\partial B_{\beta}(0,1)} u$. Similarly we can prove $\inf _{B_{\beta}(0,1)} u \geq \inf _{\partial B_{\beta}(0,1)} u$. \(\square\)

Lemma 2.1 immediately implies uniqueness of the solution in $C^{0}\left(\overline{B_{\beta}(0,1)}\right) \cap C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right)$ to the conical Dirichilet problem
$$\begin{cases}\Delta_{\beta} u=0, & \text { in } B_{\beta}(0,1) \backslash \mathcal{S} \\ u=\varphi \in C^{0}\left(\partial B_{\beta}(0,1)\right), & \text { on } \partial B_{\beta}(0,1)\end{cases}$$
We will establish the existence of the solution to (2.2) in section 2.4.
2.3. One dimensional case. In this section, we establish some basic estimates for the conical Poisson equation on $\mathbb{C}$. Let
$$\hat{g}_{\beta}=\sqrt{-1}|z|^{-2(1-\beta)} d z \wedge d \bar{z}$$
be a conical metric on $\mathbb{C}$ for some $\beta \in(1 / 2,1)$. We will consider the case when $\beta \in(1 / 2,1)$ because the case of $\beta \in(0,1 / 2]$ is relatively easy and can be treated with little modification.

Let $B=B(0,1) \subset \mathbb{C}$ be the Euclidean unit ball. We consider the following conical Poisson equation
$$\Delta_{\hat{g}_{\beta}} u=|z|^{2(1-\beta)} \frac{\partial^{2} u}{\partial z \partial \bar{z}}=F,$$
for some continuous function $F \in C^{0}(\bar{B})$.
Suppose $u \in C^{0}(\bar{B}) \cap C^{2}(B \backslash\{0\})$ solves equation (2.3). We will apply the Riez representation formula. Let $h$ be the harmonic function satisfying
$$\frac{\partial^{2}}{\partial z \partial \bar{z}} h=0 \quad \text { in } B,\left.\quad h\right|_{\partial B}=\left.u\right|_{\partial B} .$$

The standard gradient estimate for harmonic functions gives
$$\sup _{\frac{1}{2} B}\left|\frac{\partial h}{\partial z}\right| \leq C\|u\|_{L^{\infty}} .$$
The Riesz representation formula ([12]) implies that
$$u(z)=h(z)+\frac{1}{2 \pi} \int_{|w|<1}\left(\log \frac{|w-z|}{|1-\bar{w} z|}\right) \frac{F(w)}{|w|^{2(1-\beta)}} \sqrt{-1} d w \wedge d \bar{w} .$$

Lemma 2.2. There exist constants $C_{1}$ and $C_{2}=C_{2}(\beta)>0$ such that
$$\sup _{\frac{1}{2} B^{*}}\left|\frac{\partial u}{\partial z}(z)\right| \leq C_{1}\|u\|_{L^{\infty}(B)}+C_{2}(\beta)\|F\|_{L^{\infty}(B)} .$$

Proof. We fix $z \in \frac{1}{2} B^{*}$. It follows from (2.5) by direct calculations that
$$\left|\frac{\partial u}{\partial z}\right| \leq\left|\frac{\partial h}{\partial z}\right|+\frac{\sqrt{-1}}{4 \pi} \int_{B} \frac{|F(w)| d w \wedge d \bar{w}}{|w-z||w|^{2(1-\beta)}}+\frac{\sqrt{-1}}{4 \pi} \int_{B} \frac{|w||F(w)| d w \wedge d \bar{w}}{|1-\bar{w} z||w|^{2(1-\beta)}} .$$
The last term on RHS is bounded by
$$\frac{\sqrt{-1}}{2} \int_{B} \frac{|w||F(w)| d w \wedge d \bar{w}}{|1-\bar{w} z||w|^{2(1-\beta)}} \leq C\|F\|_{\infty} \int_{0}^{1} \frac{t^{2}}{t^{2(1-\beta)}} d t=\frac{C\|F\|_{L^{\infty}(B)}}{2 \beta+1} .$$
To estimate the second term on RHS, we divide $B$ into four regions,
$$\begin{gathered}
\Omega_{1}=\left\{w \in B| | w \left\lvert\, \leq \frac{|z|}{2}\right.\right\}, \quad \Omega_{2}=\left\{w \in B| | w\left|\leq|w-z|,|w| \geq \frac{|z|}{2}\right\}\right. \\
\Omega_{3}=\left\{w \in B| | w-z\left|\leq \frac{|z|}{2} \leq|w|\right\}, \quad \Omega_{4}=\left\{w \in B| | w-z\left|\leq|w|,|w-z| \geq \frac{|z|}{2}\right\} .\right.\right.
\end{gathered}$$
We have the following estimates
$$\begin{gathered}
\int_{\Omega_{1}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w-z||w|^{2(1-\beta)}} \leq \frac{2}{|z|} \int_{|w| \leq \frac{|z|}{2}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w|^{2(1-\beta)}} \leq C(\beta)|z|^{2 \beta-1} \\
\int_{\Omega_{2}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w-z||w|^{2(1-\beta)}} \leq \int_{\Omega_{2}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w|^{2(1-\beta)+1}} \leq C \int_{|z| / 2}^{1} t^{-2(1-\beta)} d t \leq C(\beta), \\
\int_{\Omega_{3}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w-z||w|^{2(1-\beta)}} \leq \frac{C}{|z|^{2(1-\beta)}} \int_{|w-z| \leq \frac{|z|}{2}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w-z|} \leq C|z|^{2 \beta-1}, \\
\int_{\Omega_{4}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w-z||w|^{2(1-\beta)}} \leq \int_{\Omega_{4}} \frac{\sqrt{-1} d w \wedge d \bar{w}}{|w-z|^{2(1-\beta)+1}} \leq C \int_{|z| / 2}^{1} t^{-2(1-\beta)} d t \leq C(\beta) .
\end{gathered}$$
Combining the above estimates with the gradient estimate (2.4) of $h$, we obtain the desired estimate. We further remark that the constant $C(\beta)$ is comparable to $1 /(2 \beta-1)$. \(\square\)

We now state the main result in this subsection, which is a scaling version of Lemma 2.2.
Proposition 2.1. Let $u \in C^{0}(\overline{B(0,1)}) \cap C^{2}(B(0,1) \backslash\{0\})$ be a solution of equation (2.3) on $B(0,1)$ for some $\beta \in(1 / 2,1)$. There exists $C=C(n, \beta)>0$ such that for all $\rho \in(0,1)$,
$$\sup _{B(0, \rho / 2) \backslash\{0\}}\left|\frac{\partial u}{\partial z}\right| \leq C\left(\frac{\|u\|_{L^{\infty}(B(0, \rho))}}{\rho}+\rho^{2 \beta-1}\|F\|_{L^{\infty}(B(0, \rho))}\right),$$
where $B(0, \rho)$ is the Euclidean ball in $\mathbb{C}$ centered at 0 of radius $\rho$.

Proof. The proposition follows from Lemma 2.2 by scaling the equation and $B(0, \rho)$. \(\square\)
2.4. Conical harmonic functions. In this subsection we will prove that the equation (2.2) admits a unique solution and we will also derive a gradient estimate.

We will construct a solution to the equation (2.2) by smooth approximation. Let $g_{\epsilon}$ be a sequence of smooth Kähler metrics defined by
$$g_{\epsilon}=\sqrt{-1}\left(\sum_{j=1}^{n-1} d z_{j} \wedge d \bar{z}_{j}+\beta^{2}\left(\left|z_{n}\right|^{2}+\epsilon\right)^{-(1-\beta)} d z_{n} \wedge d \bar{z}_{n}\right)$$
For fixed $r>0$,
$$B_{g_{\epsilon}}(0,0.9 r) \subset B_{\beta}(0, r) \subset B_{g_{\epsilon}}(0, r)$$
for sufficiently small $\epsilon>0$.
We consider the following approximating Dirichlet problem
$$\left\{\begin{aligned}
\Delta_{g_{\epsilon}} u_{\epsilon}=0, & \text { in } B_{\beta}(0, r) \backslash \mathcal{S}, \\
u_{\epsilon}=\varphi, & \text { on } \partial B_{\beta}(0, r)
\end{aligned}\right.$$
for some $\varphi \in C^{0}\left(\partial B_{\beta}(0, r)\right)$.
Lemma 2.3. For any $\epsilon>0$, there exists a unique solution $u_{\epsilon} \in C^{0}\left(\overline{B_{\beta}(0, r)}\right) \cap C^{\infty}\left(B_{\beta}(0, r)\right)$ to the conical Dirichlet problem (2.7). Furthermore,
$$\left\|u_{\epsilon}\right\|_{L^{\infty}\left(B_{\beta}(0, r)\right.} \leq \sup _{\partial B_{\beta}(0, r)}|\varphi| .$$
Proof. Equation (2.7) can be solved by Peron's method since $g_{\epsilon}$ is a smooth Riemannian metric and the boundary $B_{\beta}(0, r)$ admits admissible barrier functions. Such barrier functions are also constructed in the proof of Lemma 2.5. The estimate (2.8) follows immediately from the maximum principle. \(\square\)

Lemma 2.4. There exist $C=C(n)$ and $\epsilon_{0}=\epsilon(n, r)>0$ such that for all $0<\epsilon<\epsilon_{0}$,
$$\sup _{B_{\beta}(0, r / 2)}\left|\nabla_{g_{\epsilon}} u_{\epsilon}\right|_{g_{\epsilon}} \leq \frac{C}{r} \operatorname{osc}_{B_{\beta}(0, r)} u_{\epsilon} .$$
Proof. We will apply Cheng-Yau's gradient estimates to prove the lemma. We first observe that
$$\operatorname{Ric}\left(g_{\epsilon}\right)=-\sqrt{-1} \partial \bar{\partial} \log \operatorname{det} g_{\epsilon}=\sqrt{-1} \partial \bar{\partial} \log \left(\left|z_{n}\right|^{2}+\epsilon\right)^{1-\beta} \geq 0 .$$
By Cheng-Yau's gradient estimate [8], we immediately have
$$\sup _{B_{\beta}(0, r / 2)}\left(\sum_{i=1}^{2 n-2}\left(\frac{\partial u_{\epsilon}}{\partial s_{i}}\right)^{2}+\left(\left|z_{n}\right|^{2}+\epsilon\right)^{1-\beta}\left|\frac{\partial u_{\epsilon}}{\partial z_{n}}\right|^{2}\right)=\sup _{B_{\beta}(0, r / 2)}\left|\nabla u_{\epsilon}\right|_{g_{\epsilon}}^{2} \leq C(n) \frac{\left(\operatorname{osc}_{B_{\beta}(0, r)} u\right)^{2}}{r^{2}}$$
for sufficiently small $\epsilon>0$ because $B_{g_{\epsilon}}(0, r)$ is sufficiently close to $B_{\beta}(0, r)$. \(\square\)

Since the $g_{\epsilon}$-harmonic function $u_{\epsilon}$ is uniformly bounded in $C^{0}\left(\overline{B_{\beta}(0, r)}\right)$ for $\epsilon \in(0,1), u_{\epsilon}$ is uniformly bounded on $C^{k}(K)$ with respect $g_{\beta}$ for any $k \in \mathbb{Z}^{+}$and compact subset $K \subset \subset$ $B_{\beta}(0, r) \backslash \mathcal{S}$. Therefore $u_{\epsilon}$ converges after passing to a subsequence to some function
$$u \in L^{\infty}\left(\overline{B_{\beta}(0, r)}\right) \cap C^{\infty}\left(B_{\beta}(0, r) \backslash \mathcal{S}\right) .$$
In fact, $u$ is Lipschitz on $\overline{B_{\beta}(0, r)}$ with respect to $g_{\beta}$ from the gradient estimate (2.9).

Lemma 2.5. The limit function $u$ is the unique solution of
$$\left\{\begin{aligned}
\Delta_{\beta} u=0, & \text { in } B_{\beta}(0, r) \backslash\{0\}, \\
u=\varphi, & \text { on } \partial B_{\beta}(0, r)
\end{aligned}\right.$$
Proof. By definition, $\Delta_{\beta} u=0$ on $B_{\beta}(0, r) \backslash\{0\}$ by local $C^{\infty}$ convergence of $u_{\epsilon}$ to $u$ away from $\mathcal{S}$. It remains to verify that $u=\varphi$ on $\partial B_{\beta}(0, r)$.

The metric ball $B_{\beta}(0, r) \subset \mathbb{C}^{n}$ is given by
$$B_{\beta}(0, r)=\left\{\left(s, z_{n}\right) \in \mathbb{R}^{2 n-2} \times \mathbb{C}\left|\sum_{j=1}^{2 n-2} s_{j}^{2}+\left|z_{n}\right|^{2 \beta}<r^{2}\right\} .\right.$$
It is straightforward to verify that $\partial B_{\beta}(0, r)$ is smooth except on $\mathcal{S}=\left\{z_{n}=0\right\}$. Since $g_{\beta}$ is greater than the standard Euclidean metric on $\mathbb{C}^{n}$,
$$B_{\beta}(0, r) \subset B_{\mathbb{C}^{n}}(0, r), \quad \partial B_{\beta}(0, r) \cap \partial B_{\mathbb{C}^{n}}(0, r) \subset \mathcal{S}$$
when $r \leq 1$, where $B_{\mathbb{C}^{n}}(0, r)$ is the Euclidean metric ball centered at 0 of radius $r$.
We define $d_{\beta}(z)$ to be the distance function from $z$ to 0 with respect to $g_{\beta}$. It is given by
$$d_{\beta}^{2}(z)=d_{\beta}\left(s, z_{n}\right)^{2}=\sum_{j=1}^{2 n-2} s_{j}^{2}+\left|z_{n}\right|^{2 \beta}$$
where $z=\left(s, z_{n}\right)$. Obviously, $d_{\beta}^{2}$ is a continuous plurisubharmonic function.
We fix an arbitrary point $q \in \partial B_{\beta}(0, r)$ and we will show that $u$ is continuous at $q$ with $u(q)=\varphi(q)$. We discuss two cases: $z_{n}(q)=0$ and $z_{n}(q) \neq 0$.
\begin{itemize}
\item[(1)] $z_{n}(q)=0$. In this case, $q \in \partial B_{\mathbb{C}^{n}}(0, r) \cap \partial B_{\beta}(0, r)$. We take the point $q^{\prime}=-q \in$ $\partial B_{\mathbb{C}^{n}}(0, r) . q$ is the unique furthest point of $q^{\prime}$ on $\partial B_{\beta}(0, r)$ with respect to the Euclidean distance. Then we define a barrier function $\Psi_{q}(z)$ by
$$\Psi_{q}(z)=d_{\mathbb{C}^{n}}\left(z, q^{\prime}\right)^{2}-4 r^{2} .$$
Clearly $\Psi_{q}(q)=0$ and $\Psi_{q}(p)<0$ for any other $p \in \partial B_{\beta}(0, r)$. For any small $\delta>0$, by the continuity of $\varphi$, there is a small open neighborhood $V$ of $q$, such that $\varphi(q)-\delta<\varphi(z)$ for any $z \in V \cap \partial B_{\beta}(0, r)$. On $\partial B_{\beta}(0, r) \backslash V$ the continuous function $\Psi_{q}$ is bounded above by a negative constant, hence for some sufficiently large $A>0$
$$\varphi(q)-\delta+A \Psi_{q}(z)<\varphi(z),$$
for all $z \in \partial B_{\beta}(0, r) \backslash V$. Let $\Phi_{q}^{-}(z)=\varphi(q)-\delta+A \Psi_{q}(z)$ then $\Phi_{q}^{-}(z)<\varphi(z)$ for all $z \in \partial B_{\beta}(0, r)$ and
$$\Delta_{g_{\epsilon}} \Phi_{q}^{-} \geq 0, \quad \text { in } B_{\beta}(0, r) .$$
It follows by the maximum principle that
$$u_{\epsilon}(z) \geq \Phi_{q}^{-}(z)=\varphi(q)-\delta+A \Psi_{q}(z)$$
for all $z \in B_{\beta}(0, r)$. Letting $\epsilon \rightarrow 0$, we have for all $z \in B_{\beta}(0, r)$
$$u(z) \geq \Phi_{q}^{-}(z)=\varphi(q)-\delta+A \Psi_{q}(z) .$$
By letting $B_{\beta}(0, r) \ni z \rightarrow q$ and then $\delta \rightarrow 0$, it follows that
$$\liminf _{z \rightarrow q} u(z) \geq \varphi(q) .$$
\end{itemize}
\begin{itemize}
\item[] On the other hand, by considering the function $\varphi_{q}^{+}(z)=\varphi(q)+\delta-A \Psi_{q}(z)$, we have
$$\limsup _{z \rightarrow q} u(z) \leq \varphi(q) .$$
Therefore $u$ is continuous at $q \in \partial B_{\beta}(0, r)$ and $u(q)=\varphi(q)$.
\item[(2)] $z_{n}(q) \neq 0$. As discussed above, the boundary $\partial B_{\beta}(0, r)$ is smooth at $q$. By a well-known result the boundary $\partial B_{\beta}(0, r)$ satisfies the exterior sphere condition at $q$. More precisely, there exists a Euclidean ball $B_{\mathbb{C}^{n}}\left(p, r_{q}\right)$ such that $\overline{B_{\beta}(0, r)} \cap \overline{B_{\mathbb{C}^{n}}\left(p, r_{q}\right)}=\{q\}$. In fact, $q$ is the unique closest point to $p$ under the Euclidean distance among all the points in $\partial B_{\beta}(0, r)$.
Let $G(z)=\frac{1}{d_{\mathbb{C}^{n}}(z, p)^{2 n-2}}=\frac{1}{|z-p|^{2 n-2}}$ be the Green function on $\mathbb{C}^{n}$. Then
$$G(z) \leq \frac{1}{|p-q|^{2 n-2}}$$
for $z \in \overline{B_{\beta}(0, r)}$ with equality only at $z=q$ and
$$\begin{aligned}
\Delta_{g_{\epsilon}} G(z) & =\sum_{j=1}^{2 n-2} \frac{\partial^{2}}{\partial s_{j}^{2}} G(z)+\beta^{-2}\left(\left|z_{n}\right|^{2}+\epsilon\right)^{1-\beta} \frac{\partial^{2}}{\partial z_{n} \partial \bar{z}_{n}} G(z) \\
& =(n-1)\left(\beta^{-2}\left(\left|z_{n}\right|^{2}+\epsilon\right)^{1-\beta}-1\right)\left(\frac{n\left|z_{n}-p_{n}\right|^{2}-1}{|z-p|^{2 n+2}}\right) \\
& \geq-C(n, r,|p-q|),
\end{aligned}$$
for some constant $C(n, r,|p-q|)>0$ and $p_{n}=z_{n}(p)$ is the $n$th coordinate of $p$. Consider the function
$$\Psi_{q}(z)=A\left(d_{\beta}^{2}(z)-r^{2}\right)+G(z)-\frac{1}{|p-q|^{2 n-2}} .$$
$\Psi_{q}(q)=0$ and $\Psi_{q}(z)<0$ for all other $z \in \partial B_{\beta}(0, r) . \Psi_{q}$ is a continuous sub-harmonic function of $\Delta_{g_{\epsilon}}$ on $B_{\beta}(0, r)$ for sufficiently large $A>0$. We can now argue similarly as in the case when $z_{n}(q)=0$ to show that $u$ is continuous at $q$ with $u(q)=\varphi(q)$.
\end{itemize}

We have completed the proof of the lemma. \(\square\)

Now we arrive at the main result in this section.
Proposition 2.2. There exists a unique solution $u \in C^{0}\left(\overline{B_{\beta}(0, r)}\right) \cap C^{2}\left(B_{\beta}(0, r) \backslash \mathcal{S}\right)$ of the equation (2.2). Furthermore, for any $k \in \mathbb{Z}^{+}$, there exists $C(n, k)>0$ such that
$$\begin{aligned}
\sup _{B_{\beta}(0, r / 2) \backslash \mathcal{S}}\left|\nabla_{g_{\beta}} u\right|_{g_{\beta}} & \leq C(n) \frac{\operatorname{osc}_{B_{\beta}(0, r)} u}{r} \\
\sup _{B_{\beta}(0, r / 2)}\left|\left(D^{\prime}\right)^{k} u\right|_{g_{\beta}} & \leq C(n, k) \frac{\operatorname{osc}_{B_{\beta}(0, r)} u}{r^{k}} \\
\sup _{B_{\beta}(0, r / 2) \backslash \mathcal{S}}\left|\left(D^{\prime}\right)^{k} D^{\prime \prime} u\right|_{g_{\beta}} & \leq C(n, k) \frac{\operatorname{osc}_{B_{\beta}(0, r)} u}{r^{k+1}}
\end{aligned}$$
Proof. (2.10) follows directly from Lemma 2.4 by letting $\epsilon \rightarrow 0$. (2.11) and (2.12) follow from the observation that if $u$ is $g_{\beta}$-harmonic, $D_{i} u$ is also $g_{\beta}$-harmonic for $i=1,2, \ldots, 2 n-2$. \(\square\)

Remark 2.1. If the RHS of (2.2) is a constant $c$, instead of 0 , the boundary value problem still admits a unique solution. To see this, we may consider $\tilde{\varphi}=\varphi-\frac{c}{2(n-1)} \sum_{j=1}^{2 n-2} s_{j}^{2}$, then let $\tilde{u}$ be the unique solution to (2.2) with boundary value $\tilde{\varphi}$, then it is easy to see the function $u=\tilde{u}+\frac{c}{2(n-1)} \sum_{j=1}^{2 n-2} s_{j}^{2}$ satisfies
$$\Delta_{g_{\beta}} u=c \quad \text { in } B_{\beta} \backslash \mathcal{S}, \quad \text { and }\left.\quad u\right|_{\partial B_{\beta}}=\left.\varphi\right|_{\partial B_{\beta}} .$$
2.5. Tangential estimates. In this subsection, we will prove the Hölder continuity of the $D_{i j}^{2} u$ for $i, j=1,2, \ldots, 2 n-2$, for the solution $u$ of (1.3), by modifying Wang's method ([31]). In particular, we will prove estimate (1.4) in Theorem 1.1. Throughout this subsection, we always assume that $\beta \in(1 / 2,1)$. We first define some notations for future conveniences.

Definition 2.4. For any point $p \in B_{\beta}(0,1 / 2) \backslash \mathcal{S}$, we define
$$r_{p}=d_{\beta}(p, \mathcal{S}) .$$
We fix the constant $\tau=1 / 2$ and let $k_{p}$ be the smallest integer such that
$$\tau^{k}<r_{p} .$$

We will consider a family of conical Laplace equations by different choices of $k$.
\begin{itemize}
\item[(1)] If $k \geq k_{p}$, the geodesic balls $B_{\beta}\left(p, \tau^{k}\right)$ has smooth boundary and there is no cut-locus point of $p$ with respect to the metric $g_{\beta}$. Since $B_{\beta}\left(p, \tau^{k}\right) \cap \mathcal{S}=\phi, g_{\beta}$ is a smooth Riemannian metric in $B_{\beta}\left(p, \tau^{k}\right)$. We can solve the following Dirichlet problem for all $k \geq k_{p}$
\end{itemize}
$$\left\{\begin{aligned}
\Delta_{g_{\beta}} u_{k}=f(p), & \text { in } B_{\beta}\left(p, \tau^{k}\right) \\
u_{k}=u, & \text { on } \partial B_{\beta}\left(p, \tau^{k}\right) .
\end{aligned}\right.$$
\begin{itemize}
\item[(2)] If $k<k_{p}$, we let $\tilde{p} \in \mathcal{S}$ be the unique closest point in $\mathcal{S}$ to with respect to $g_{\beta}$, which is the projection of $p$ to $\mathcal{S}$ under the map $\mathbb{C}^{n} \rightarrow \mathbb{C}^{n-1} \times\{0\}$. We consider the metric ball $B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)$ instead of $B_{\beta}\left(p, \tau^{k}\right)$ in (2.15). Clearly $B_{\beta}\left(p, r_{p}\right) \Subset B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)$ for $k<k_{p}$. The advantage of this choice is that $B_{\beta}\left(\tilde{p}, \tau^{k}\right)$ is geometrically simpler than $B_{\beta}\left(p, \tau^{k}\right)$. More precisely, when $k<k_{p}$, let $u_{k} \in C^{2}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)}\right)$ solve the problem
\end{itemize}
$$\left\{\begin{aligned}
\Delta_{g_{\beta}} u_{k}=f(p), & \text { in } B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right) \\
u_{k}=u, & \text { on } \partial B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)
\end{aligned}\right.$$

We remark that we may always assume $f(p)=0$ for the proof of Theorem 1.1 by considering the function $\hat{u}\left(s, z_{n}\right)=u\left(s, z_{n}\right)-\frac{f(p)}{2(n-1)}|s-s(p)|^{2}$. Then if estimate (2.30) holds for $\hat{u}$, it is still valid for $u$.

The following lemma immediately follows from the maximum principle.
Lemma 2.6. Let $u_{k}$ the solution of equation (2.15) or (2.16). Then there exists $C(n)>0$ such that for all $k \in \mathbb{Z}^{+}$,
$$\left\{\begin{aligned}
\left\|u_{k}-u\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k}\right)\right)} \leq C(n) \tau^{2 k} \omega\left(\tau^{k}\right), & \text { when } k \geq k_{p} \\
\left\|u_{k}-u\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)\right)} \leq C(n) \tau^{2 k} \omega\left(2 \tau^{k}\right), & \text { when } k<k_{p} .
\end{aligned}\right.$$

We immediately have the following estimates by triangle inequalities.
$$\left\{\begin{array}{cl}
\left\|u_{k}-u_{k+1}\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+1}\right)\right)} \leq C(n) \tau^{2 k} \omega\left(\tau^{k}\right), & \text { when } k \geq k_{p} \\
\left\|u_{k}-u_{k+1}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+1}\right)\right)} \leq C(n) \tau^{2 k} \omega\left(2 \tau^{k}\right), & \text { when } k<k_{p}-1 \\
\left\|u_{k_{p}}-u_{k_{p}-1}\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k_{p}}\right)\right)} \leq C(n) \tau^{2 k_{p}} \omega\left(2 \tau^{k_{p}}\right), & \text { when } k=k_{p}-1 .
\end{array}\right.$$
Combining the gradient estimates in Proposition 2.2 and the $L^{\infty}$-estimates (2.18), we have the following lemma.

Lemma 2.7. Then there exists $C(n)>0$ such that for all $k \in \mathbb{Z}^{+}$,
$$\left\{\begin{aligned}
\left\|D^{\prime} u_{k}-D^{\prime} u_{k+1}\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+2}\right)\right)} \leq C(n) \tau^{k} \omega\left(\tau^{k}\right), & \text { when } k \geq k_{p}, \\
\left\|D^{\prime} u_{k}-D^{\prime} u_{k+1}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+2}\right)\right)} \leq C(n) \tau^{k} \omega\left(2 \tau^{k}\right), & \text { when } k<k_{p},
\end{aligned}\right.$$
and
$$\left\{\begin{aligned}
\left\|\left(D^{\prime}\right)^{2} u_{k}-\left(D^{\prime}\right)^{2} u_{k+1}\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+2}\right)\right)} \leq C(n) \omega\left(\tau^{k}\right), & \text { when } k \geq k_{p}, \\
\left\|\left(D^{\prime}\right)^{2} u_{k}-\left(D^{\prime}\right)^{2} u_{k+1}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, \tau^{k+2}\right)\right)} \leq C(n) \omega\left(2 \tau^{k}\right), & \text { when } k<k_{p} .
\end{aligned}\right.$$

Lemma 2.8. We have
$$\lim _{k \rightarrow \infty} D^{\prime} u_{k}(p)=D^{\prime} u(p), \quad \lim _{k \rightarrow \infty}\left(D^{\prime}\right)^{2} u_{k}(p)=\left(D^{\prime}\right)^{2} u(p) .$$
Proof. When $k \geq k_{p}, w=\left(z_{n}\right)^{\beta}$ is well-defined by taking a single-value branch on $B_{g_{\beta}}\left(p, \tau^{k}\right)$. We can use $\left\{s_{i}, w\right\}$ as local complex coordinates. The cone metric $g_{\beta}$ becomes the standard Euclidean metric under $\left\{s_{j}, w\right\}$. By assumption $u$ is $C^{2}$ on $B_{\beta}\left(p, \tau^{k}\right)$, its Taylor expansion at $p$ is given by
$$\begin{aligned}
& u(s, w) \\
= & u(p)+\left.\left(D^{\prime} u\right)\right|_{p}(s-s(p))+2 \operatorname{Re}\left(\left.\left(\partial_{w} u\right)\right|_{p}(w-w(p))\right)+\left.\frac{1}{2}(s-s(p))\left(\left(D^{\prime}\right)^{2} u\right)\right|_{p}(s-s(p)) \\
& \quad+2 \operatorname{Re}\left(\left.\left(D^{\prime} \partial_{w} u\right)\right|_{p}(s-s(p))(w-w(p))\right)+\left.\left(\partial_{w} \partial_{\bar{w}} u\right)\right|_{p}|w-w(p)|^{2} \\
& \quad+\operatorname{Re}\left(\left.\left(\partial_{w} \partial_{w} u\right)\right|_{p}(w-w(p))^{2}\right)+o\left(|s-s(p)|^{2}+|w-w(p)|^{2}\right) \\
= & \tilde{u}(s, w)+o\left(|s-s(p)|^{2}+|w-w(p)|^{2}\right)
\end{aligned}$$
where $\widetilde{u}(s, w)$ is a quadratic polynomial in $(s, w)$ with constant coefficients. In particular, $\Delta_{g_{\beta}} \widetilde{u}=$ $\Delta_{s, w} \widetilde{u}=f(p)$, and so $\Delta_{g_{\beta}}\left(u_{k}-\tilde{u}\right)=0$ on $B_{\beta}\left(p, \tau^{k}\right)$ with
$$\left.\left(u_{k}-\tilde{u}\right)\right|_{\partial B_{\beta}\left(p, \tau^{k}\right)}=\left.o\left(|s-s(p)|^{2}+|w-w(p)|^{2}\right)\right|_{\partial B_{\beta}\left(p, \tau^{k}\right)}=o\left(\tau^{2 k}\right) .$$
By the derivatives estimates for conical harmonic functions in Proposition 2.2, we have
$$\left\{\begin{aligned}
\left|D^{\prime} u_{k}-D^{\prime} u\right|(p)=\left|D^{\prime} u_{k}-D^{\prime} \tilde{u}\right|(p) \mid \leq C \tau^{-k} o\left(\tau^{2 k}\right) \rightarrow 0, & \text { as } k \rightarrow \infty . \\
\left|\left(D^{\prime}\right)^{2} u_{k}-\left(D^{\prime}\right)^{2} u\right|(p)=\left|\left(D^{\prime}\right)^{2} u_{k}-\left(D^{\prime}\right)^{2} \tilde{u}\right|(p) \leq C \tau^{-2 k} o\left(\tau^{2 k}\right) \rightarrow 0, & \text { as } k \rightarrow \infty .
\end{aligned}\right.$$ \(\square\)

Combining Lemma 2.7 and Lemma 2.8, we have the following 2nd order estimate for $u$.

Corollary 2.1. There exists $C=C(n, \beta)>0$ such that
$$\sup _{B_{\beta}(0,1 / 2) \backslash \mathcal{S}}\left(\left|\left(D^{\prime}\right)^{2} u\right|(z)+|z|^{2-2 \beta}\left|\frac{\partial^{2} u}{\partial z_{n} \partial \overline{z_{n}}}\right|(z)\right) \leq C\left(\sup _{B_{\beta}(0,1)}|u|+\int_{0}^{1} \frac{\omega(r)}{r} d r+|f(0)|\right) .$$

We can apply the same argument for the point $q \in B_{g_{\beta}}(0,1 / 2) \backslash \mathcal{S}$ by solving the boundary problem
$$\Delta_{g_{\beta}} v_{k}=f(q), \quad v_{k}=u, \quad \text { on } \partial B_{\beta}\left(q, \tau^{k}\right) .$$

We can obtain similar estimates as those in (2.21), (2.19) and (2.20) for the functions $v_{k}$ on balls centered at the point $q$ or $\tilde{q}$.

Proposition 2.3. Let $d=d_{\beta}(p, q)$ for some $\beta \in(1 / 2,1)$. There exists $C=C(n)>0$ such that if $u \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \cap L^{\infty}\left(B_{\beta}(0,1)\right)$ solves the conical Laplace equation (1.3), then for any $p, q \in B_{\beta}(0,1 / 2) \backslash \mathcal{S}$,
$$\sum_{i, j=1}^{2 n-2}\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \leq C\left(d \sup _{B_{\beta}(0,1)}|u|+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right) .$$
Proof. We will first assume that
$$r_{p}=\min \left\{r_{p}, r_{q}\right\} \leq 2 d$$
and fix an integer $\ell \in \mathbb{N}$ satisfying
$$\tau^{\ell+4} \leq d<\tau^{\ell+3}, \quad \text { or } \tau^{\ell+1} \leq 8 d<\tau^{\ell} .$$
We observe that
$$\tau^{k_{p}} \leq 2 d<2 \tau^{\ell+3}=\tau^{\ell+2} \Rightarrow k_{p}>\ell+2 .$$
The triangle inequality implies that $r_{q} \leq d+r_{p} \leq 3 d$, so
$$\tau^{k_{q}} \leq 3 d<3 \tau^{\ell+3} \quad \Rightarrow \quad k_{q}>\ell+1 .$$
Our goal is to estimate
$$\begin{aligned}
\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \leq & \left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u_{\ell}(p)\right|+\left|\left(D^{\prime}\right)^{2} u_{\ell}(p)-\left(D^{\prime}\right)^{2} u_{\ell}(q)\right| \\
& +\left|\left(D^{\prime}\right)^{2} u_{\ell}(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right|+\left|\left(D^{\prime}\right)^{2} v_{\ell}(q)-\left(D^{\prime}\right)^{2} u(q)\right| \\
= & I_{1}+I_{2}+I_{3}+I_{4} .
\end{aligned}$$
We will now estimate $I_{1}, I_{2}, I_{3}$ and $I_{4}$ respectively.
Step 1. By (2.20) and (2.21) we have
$$I_{1}=\left|\left(D^{\prime}\right)^{2} u_{\ell}(p)-\left(D^{\prime}\right)^{2} u(p)\right| \leq C \sum_{k=k_{p}}^{\infty} \omega\left(\tau^{k}\right)+C \sum_{k=\ell}^{k_{p}-1} \omega\left(2 \tau^{k}\right) .$$
and similarly
$$I_{4}=\left|D_{i j}^{2} v_{\ell}(q)-D_{i j}^{2} u(q)\right| \leq C \sum_{k=k_{q}}^{\infty} \omega\left(\tau^{k}\right)+C \sum_{k=\ell}^{k_{q}-1} \omega\left(2 \tau^{k}\right) .$$
\begin{itemize}
\item[] Step 2. The triangle inequality implies $r_{q}=d_{\beta}(q, \tilde{q}) \leq 3 d, d_{\beta}(\tilde{p}, \tilde{q}) \leq d$ and $d_{\beta}(\tilde{p}, q) \leq 3 d$. Therefore by the choice of $\ell$ as in (2.25),
$$B_{\beta}\left(\tilde{q}, \tau^{\ell}\right) \subset B_{\beta}\left(\tilde{p}, 2 \tau^{\ell}\right),$$
and $u_{\ell}$ and $v_{\ell}$ are both defined on $B_{\beta}\left(\tilde{q}, \tau^{\ell}\right)$ satisfying
$$\Delta_{g_{\beta}} u_{\ell}=f(p), \quad \Delta_{g_{\beta}} v_{\ell}=f(q) .$$
(2.17) and Remark 2.1 imply that
$$\left\|u_{\ell}-v_{\ell}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{q}, \tau^{\ell}\right)\right)} \leq C \tau^{2 \ell} \omega\left(2 \tau^{\ell}\right) .$$
Consider the function
$$U\left(s, z_{n}\right)=u_{\ell}\left(s, z_{n}\right)-v_{\ell}\left(s, z_{n}\right)-\frac{f(p)-f(q)}{2(n-1)}|s-s(\tilde{q})|^{2} .$$
It is a $g_{\beta}$-harmonic function satisfying
$$\sup _{B_{\beta}\left(\tilde{q}, \tau^{\ell}\right)}|U| \leq C(n) \tau^{2 \ell} \omega\left(2 \tau^{\ell}\right)+C \tau^{2 \ell} \omega(d) \leq C \tau^{2 \ell} \omega\left(2 \tau^{\ell}\right) .$$
The derivative estimates immediately imply that
$$\left|\left(D^{\prime}\right)^{2} U(q)\right| \leq C \omega\left(2 \tau^{\ell}\right)$$
since $q \in B_{\beta}\left(\tilde{q}, \frac{1}{2} \tau^{\ell}\right)$ and so
$$I_{3}=\left|\left(D^{\prime}\right)^{2} u_{\ell}(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right| \leq C \omega\left(2 \tau^{\ell}\right),$$
which implies the estimate for $I_{3}$.
\item[] Step 3. To estimate $I_{2}$, we first define $h_{k}=u_{k-1}-u_{k}$ for any $2 \leq k \leq \ell . h_{k}$ is a $g_{\beta}$-harmonic function on $B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)$ with
$$\left\|h_{k}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)\right)} \leq C \tau^{2 k} \omega\left(2 \tau^{k}\right) .$$
In particular this implies that
$$\left\|\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+1}\right)\right)} \leq C \omega\left(2 \tau^{k}\right) .$$
On the other hand, $D_{i} D_{j} h_{k}$ is again a $g_{\beta}$-harmonic function on $B_{\beta}\left(\tilde{p}, 2 \tau^{k+1}\right)$ for $i, j=$ $1, \ldots, 2 n-2$. Therefore we have
$$\left\|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+2}\right)\right)} \leq C \tau^{-k} \omega\left(2 \tau^{k}\right) .$$
Integrating along the minimal geodesic $\gamma$ with respect to $g_{\beta}$ joining $p$ and $q$, we have
$$\left|\left(D^{\prime}\right)^{2} h_{k}(p)-\left(D^{\prime}\right)^{2} h_{k}(q)\right| \leq C d \tau^{-k} \omega\left(2 \tau^{k}\right) .$$
Such a minimal geodesic does not meet $\mathcal{S}$ because $p, q \notin \mathcal{S}$ and $\left(\mathbb{C}^{n} \backslash \mathcal{S}, g_{\beta}\right)$ is strictly geodesically convex in $\mathbb{C}^{n}$. Immediately, for all $2 \leq k \leq \ell$
$$\left|\left(D^{\prime}\right)^{2} u_{k}(p)-\left(D^{\prime}\right)^{2} u_{k}(q)\right| \leq\left|\left(D^{\prime}\right)^{2} u_{k-1}(p)-\left(D^{\prime}\right)^{2} u_{k-1}(q)\right|+C d \tau^{-k} \omega\left(2 \tau^{k}\right) .$$
and so
$$I_{2} \leq\left|\left(D^{\prime}\right)^{2} u_{2}(p)-\left(D^{\prime}\right)^{2} u_{2}(q)\right|+C d \sum_{k=3}^{\ell} \tau^{-k} \omega\left(2 \tau^{k}\right) .$$
To estimate the first term on the RHS, we recall from (2.17) that
$$\left\|u_{2}-u\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{2}\right)\right)} \leq C \tau^{4} \omega\left(2 \tau^{2}\right)$$
\end{itemize}
and so
$$\left\|u_{2}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{2}\right)\right)} \leq\|u\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{2}\right)\right)}+C \tau^{4} \omega\left(2 \tau^{2}\right) .$$
Since we can assume $f(p)=0$, the derivative estimates for $g_{\beta}$-harmonic functions implies that
$$\left\|\left(D^{\prime}\right)^{2} u_{2}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{3}\right)\right)} \leq C\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\omega\left(2 \tau^{2}\right)\right)$$
and by the gradient estimate,
$$\left\|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} u_{2}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{4}\right)\right)} \leq C\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\omega\left(2 \tau^{2}\right)\right),$$
integrating along the minimal geodesic $\gamma$ as before, we get
$$\left|\left(D^{\prime}\right)^{2} u_{2}(p)-\left(D^{\prime}\right)^{2} u_{2}(q)\right| \leq C d\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\omega\left(2 \tau^{2}\right)\right) .$$
Thus
$$I_{2} \leq C d\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+C d \sum_{k=2}^{\ell} \tau^{-k} \omega\left(2 \tau^{k}\right) .$$

Combining estimates from the above three steps and the fact that $\omega(2 r) \leq 2 \omega(r)$, we have
$$\begin{aligned}
& \left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \\
& \leq C\left(\sum_{k=k_{p}}^{\infty} \omega\left(\tau^{k}\right)+\sum_{k=\ell}^{k_{p}-1} \omega\left(2 \tau^{k}\right)+\sum_{k=k_{q}}^{\infty} \omega\left(\tau^{k}\right)+\sum_{k=\ell}^{k_{q}-1} \omega\left(2 \tau^{k}\right)\right. \\
& \left.\quad+\omega\left(2 \tau^{\ell}\right)+d\|u\|_{L^{\infty}}+d \sum_{k=2}^{\ell} \tau^{-k} \omega\left(2 \tau^{k}\right)\right) \\
& \leq C\left(d\|u\|_{L^{\infty}}+\int_{0}^{d} \frac{\omega(t)}{t} d t+d \int_{d}^{1} \frac{\omega(t)}{t^{2}} d t\right) .
\end{aligned}$$
This proves the proposition when $r_{p} \leq 2 d$.
It remains to prove the proposition for the case $r_{p}>2 d$. The argument is parallel to the case when $r_{p} \leq 2 d$ with minor differences. The main difference is that the $\ell$ in (2.25) may be greater than $k_{p}$. The estimates (2.17), (2.19) and (2.20) still hold. In fact $I_{1}+I_{4}$ is bounded as follows (in contrast with (2.26))
$$I_{1}+I_{4} \leq C \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right) .$$
The metric ball $B_{\beta}\left(q, \tau^{\ell+1}\right)$ is contained in $B_{\beta}\left(p, \tau^{\ell}\right) \cap B_{\beta}\left(q, \tau^{\ell}\right)$, so by the same argument in deriving (2.27), we have
$$I_{3} \leq C \omega\left(\tau^{\ell}\right) .$$
To estimate $I_{2}$, we define $h_{k}=u_{k-1}-u_{k}$ as before and the estimate follows from the same argument given before. Therefore we complete the proof for the proposition. \(\square\)
2.6. Transversal estimates. The proof is parallel to that in subsection 2.5, however there are some significantly more difficult technical differences arising from the singular behavior of $g_{\beta}$-harmonic functions near $\mathcal{S}$. We again assume that $\beta \in(1 / 2,1)$.

Following subsection 2.5, we fix two points $p, q \in B_{\beta}(0,1 / 2) \backslash \mathcal{S}$ and let
$$r_{p}=d_{\beta}(p, \mathcal{S}), \quad r_{q}=d_{\beta}(q, \mathcal{S}), \quad r_{p} \leq r_{q} .$$
Let us recall
$$\rho_{n}=\left|z_{n}\right|, \quad \theta_{n}=\arg z_{n}, \quad r_{n}=\rho_{n}^{\beta} .$$
The conical Laplace operator with respect to $\hat{g}_{\beta}$ on $\mathbb{C}$ can be expressed by
$$\left|z_{n}\right|^{2(1-\beta)} \frac{\partial^{2}}{\partial z_{n} \partial \bar{z}_{n}}=\frac{\partial^{2}}{\partial\left(r_{n}\right)^{2}}+\frac{1}{r_{n}} \frac{\partial}{\partial r_{n}}+\frac{1}{\beta^{2}\left(r_{n}\right)^{2}} \frac{\partial^{2}}{\partial\left(\theta_{n}\right)^{2}} .$$

We solve the equations (2.15) and (2.16). Applying estimate (2.18) and the derivatives estimates for the $g_{\beta}$-harmonic functions $u_{k}-u_{k+1}$, we have
$$\left\{\begin{aligned}
\left\|\left|z_{n}\right|^{1-\beta}\left(\frac{\partial u_{k}}{\partial z_{n}}-\frac{\partial u_{k+1}}{\partial z_{n}}\right)\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+2}\right)\right)} \leq C(n) \tau^{k} \omega\left(\tau^{k}\right), & \text { if } k \geq k_{p} \\
\left\|\left|z_{n}\right|^{1-\beta}\left(\frac{\partial u_{k}}{\partial z_{n}}-\frac{\partial u_{k+1}}{\partial z_{n}}\right)\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+2}\right)\right)} \leq C(n) \tau^{k} \omega\left(2 \tau^{k}\right), & \text { if } k<k_{p} .
\end{aligned}\right.$$
Combining (2.19) and gradient estimate for the harmonic function $D_{i} u_{k}-D_{i} u_{k+1}$ for $i=1, \ldots$ , $2 n-2$, we obtain the following lemma.

Lemma 2.9. There exists $C(n)>0$ such that for all $k \in \mathbb{Z}^{+}$,
$$\begin{cases}\left\|\left|z_{n}\right|^{1-\beta}\left(\left(\partial_{z_{n}} D^{\prime}\right) u_{k}-\left(\partial_{z_{n}} D^{\prime}\right) u_{k+1}\right)\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+3}\right)\right)} \leq C(n) \omega\left(\tau^{k}\right), & \text { if } k \geq k_{p} \\ \left\|\left|z_{n}\right|^{1-\beta}\left(\left(\partial_{z_{n}} D^{\prime}\right) u_{k}-\left(\partial_{z_{n}} D^{\prime}\right) u_{k+1}\right)\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, \tau^{k+3}\right)\right)} \leq C(n) \omega\left(2 \tau^{k}\right), & \text { if } k<k_{p}\end{cases}$$

We also have the following lemma similar to Lemma 2.8.
Lemma 2.10.
$$\begin{gathered}
\lim _{k \rightarrow \infty} \frac{\partial u_{k}}{\partial r_{n}}(p)=\frac{\partial u}{\partial r_{n}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial u_{k}}{r_{n} \partial \theta_{n}}(p)=\frac{\partial u}{r_{n} \partial \theta_{n}}(p) \\
\lim _{k \rightarrow \infty} \frac{\partial^{2} u_{k}}{\partial s_{i} \partial r_{n}}(p)=\frac{\partial^{2} u}{\partial s_{i} \partial r_{n}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial^{2} u_{k}}{r_{n} \partial s_{i} \partial \theta_{n}}(p)=\frac{\partial^{2} u}{r_{n} \partial s_{i} \partial \theta_{n}}(p) .
\end{gathered}$$
Proof. For sufficiently large $k$, we change coordinates by letting $w=\left(z_{n}\right)^{\beta}$ on $B_{\beta}\left(p, \tau^{k}\right)$. The function $u_{k}-\tilde{u}$ is harmonic on the ball $B_{\beta}\left(p, \tau^{k}\right)$ with respect to the Euclidean metric in $\left\{s_{i}, w\right\}$, where $\tilde{u}$ is defined in Lemma 2.8. It follows that
$$\left\{\begin{aligned}
\left|\partial_{w} u_{k}(p)-\partial_{w} u(p)\right| \leq C(n) \tau^{-k} o\left(\tau^{2 k}\right) \rightarrow 0, & \text { as } k \rightarrow \infty, \\
\left|\partial_{w} D^{\prime} u_{k}(p)-\partial_{w} D^{\prime} u(p)\right| \leq C(n) \tau^{-2 k} o\left(\tau^{2 k}\right) \rightarrow 0, & \text { as } k \rightarrow \infty .
\end{aligned}\right.$$
Since at $p$
$$\partial_{w} u=z_{n}^{1-\beta} \partial_{z_{n}} u, \quad \partial_{w} D^{\prime} u=z_{n}^{1-\beta} \partial_{w} D^{\prime} u,$$
we have the following estimates away from $\mathcal{S}$,
$$\begin{aligned}
\left|\left|z_{n}\right|^{1-\beta}\left(\frac{\partial u_{k}}{\partial z_{n}}-\frac{\partial u}{\partial z_{n}}\right)\right|^{2} & =\left|\frac{\partial}{\partial r_{n}}\left(u_{k}-u\right)-\frac{\sqrt{-1}}{\beta r_{n}} \frac{\partial}{\partial \theta_{n}}\left(u_{k}-u\right)\right|^{2} \\
& =\left(\frac{\partial}{\partial r_{n}}\left(u_{k}-u\right)\right)^{2}+\frac{1}{\beta^{2}\left(r_{n}\right)^{2}}\left(\frac{\partial}{\partial \theta_{n}}\left(u_{k}-u\right)\right)^{2},
\end{aligned}$$
$$\begin{aligned}
\left|\left|z_{n}\right|^{1-\beta}\left(\partial_{z_{n}} D^{\prime} u_{k}-\partial_{z_{n}} D^{\prime} u\right)\right|^{2} & =\left|\frac{\partial}{\partial r_{n}}\left(D^{\prime} u_{k}-D^{\prime} u\right)-\frac{\sqrt{-1}}{\beta r_{n}} \frac{\partial}{\partial \theta_{n}}\left(D^{\prime} u_{k}-D^{\prime} u\right)\right|^{2} \\
& =\left(\frac{\partial}{\partial r_{n}}\left(D^{\prime} u_{k}-D^{\prime} u\right)\right)^{2}+\frac{1}{\beta^{2}\left(r_{n}\right)^{2}}\left(\frac{\partial}{\partial \theta_{n}}\left(D^{\prime} u_{k}-D^{\prime} u\right)\right)^{2} .
\end{aligned}$$
The lemma then follows from (2.35). \(\square\)

Our goal is to estimate
$$J=\left|\partial_{r_{n}} D^{\prime} u(p)-\partial_{r_{n}} D^{\prime} u(q)\right|, \quad K=\left|\frac{\partial^{2} u}{r_{n} \partial s_{i} \partial \theta_{n}}(p)-\frac{\partial^{2} u}{r_{n} \partial s_{i} \partial \theta_{n}}(q)\right| .$$
We choose $\ell$ as in (2.25) and estimate $J$ in (2.37). The quantity $K$ can be similarly estimated. We follow the same argument as in subsection 2.5 by decomposing $J$ into $J_{1}, J_{2}, J_{3}$ and $J_{4}$.
$$\begin{aligned}
\left|\partial_{r_{n}} D^{\prime} u(p)-\partial_{r_{n}} D^{\prime} u(q)\right| \leq & \left|\partial_{r_{n}} D^{\prime} u(p)-\partial_{r_{n}} D^{\prime} u_{\ell}(p)\right|+\left|\partial_{r_{n}} D^{\prime} u_{\ell}(p)-\partial_{r_{n}} D^{\prime} u_{\ell}(q)\right| \\
& +\left|\partial_{r_{n}} D^{\prime} u_{\ell}(q)-\partial_{r_{n}} D^{\prime} v_{\ell}(q)\right|+\left|\partial_{r_{n}} D^{\prime} v_{\ell}(q)-\partial_{r_{n}} D^{\prime} u(q)\right| \\
= & J_{1}+J_{2}+J_{3}+J_{4},
\end{aligned}$$
where $v_{\ell}$ is defined as in (2.24).
Lemma 2.11. There exists $C=C(n)>0$ such that for all $p, q \in B_{\beta}(0,1 / 2) \backslash \mathcal{S}$,
$$\begin{aligned}
& J_{1}=\left|\partial_{r_{n}} D^{\prime} u(p)-\partial_{r_{n}} D^{\prime} u_{\ell}(p)\right| \leq C \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right), \\
& J_{4}=\left|\partial_{r_{n}} D^{\prime} u(q)-\partial_{r_{n}} D^{\prime} v_{\ell}(q)\right| \leq C \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right), \\
& J_{3}=\left|\partial_{r_{n}} D^{\prime} u_{\ell}(q)-\partial_{r_{n}} D^{\prime} v_{\ell}(q)\right| \leq C \omega\left(\tau^{\ell}\right) .
\end{aligned}$$
Proof. The estimate for $J_{1}$ and $J_{4}$ follow from similar argument for (2.26). The estimate for $J_{3}$ follows from similar argument for (2.27) by applying Lemmas 2.9 and 2.10. \(\square\)

However, we have to work harder to estimate $J_{2}$. We also consider two cases: $r_{p} \leq 2 d$ and $r_{p}>2 d$.

If $r_{p}=\min \left\{r_{p}, r_{q}\right\} \leq 2 d$, we will work on the geodesic ball $B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)$ as before and let $h_{k}=u_{k-1}-u_{k}$, for $2 \leq k \leq \ell . h_{k}$ is a harmonic function on $B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)$ with
$$\left\|h_{k}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k}\right)\right)} \leq C(n) \tau^{2 k} \omega\left(2 \tau^{k}\right) .$$
From (2.28) and (2.29), we have
$$\left\|\left(D^{\prime}\right)^{3} h_{k}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+2}\right)\right)}+\left\|\left|z_{n}\right|^{1-\beta} \frac{\partial}{\partial z_{n}}\left(\left(D^{\prime}\right)^{2} h_{k}\right)\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+2}\right) \backslash \mathcal{S}\right)} \leq C(n) \tau^{-k} \omega\left(2 \tau^{k}\right) .$$

Then the following lemma holds.
Lemma 2.12. There exists $C=C(n, \beta)>0$ such that for any $z \in B_{\beta}\left(\tilde{p}, 2 \tau^{k+4}\right) \backslash \mathcal{S}$,
$$\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}\right|(z)+\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{r_{n} \partial \theta_{n}}\right|(z) \leq C\left(r_{n}\right)^{\frac{1}{\beta}-1} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(\tau^{k}\right)$$
where $r_{n}=\left|z_{n}\right|^{\beta}$ and $\theta_{n}=\arg z_{n}$.

Proof. On $B_{\beta}\left(\tilde{p}, 2 \tau^{k+2}\right)$, we define $F$ by
$$F=\left|z_{n}\right|^{2(1-\beta)} \frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial z_{n} \partial \bar{z}_{n}}=-\sum_{j=1}^{2 n-2} \frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial s_{j}^{2}} .$$
Fix a point $x=\left(x_{1}, x_{2}, \ldots, x_{n}\right) \in \mathcal{S} \cap B_{\beta}\left(\tilde{p}, 2 \tau^{k+3}\right)$. Then $B_{\beta}\left(x, 2 \tau^{k+3}\right) \subset B_{\beta}\left(\tilde{p}, 2 \tau^{k+2}\right)$. Consider the intersection of $B_{\beta}\left(x, 2 \tau^{k+3}\right)$ with $\left\{z_{n}=x_{n}\right\}$, which is transversal to $\mathcal{S}$ at $x$ and lies in a metric ball of radius $2 \tau^{k+3}$ with respect to the cone metric $\hat{g}_{\beta}$ in $\mathbb{C}$.

We let
$$\hat{B}=B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta}\right) \subset \mathbb{C}$$
and view the equation (2.41) to be in $B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta}\right)$. By Proposition 2.1, we have in $B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta} / 2\right) \backslash\{0\}$,
$$\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial z_{n}}\right| \leq C \frac{\left\|\left(D^{\prime} h_{k}\right)\right\|_{L^{\infty}(\hat{B})}}{\left(2 \tau^{k+3}\right)^{1 / \beta}}+C\|F\|_{L^{\infty}(\hat{B})}\left(2 \tau^{k+3}\right)^{(2 \beta-1) / \beta} .$$
On the other hand, away from $\mathcal{S}$ it holds that
$$\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial z_{n}}\right|=\left|\beta\left(r_{n}\right)^{1-\frac{1}{\beta}} \frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}-\sqrt{-1}\left(r_{n}\right)^{1-\frac{1}{\beta}} \frac{\partial\left(D^{\prime} h_{k}\right)}{r_{n} \partial \theta_{n}}\right| .$$
Therefore in $B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta} / 2\right) \backslash\{0\}$,
$$\begin{aligned}
& \left|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}\right|+\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{r_{n} \partial \theta_{n}}\right| \\
\leq & \frac{C\left(r_{n}\right)^{\frac{1}{\beta}-1}\left\|\left(D^{\prime} h_{k}\right)\right\|_{L^{\infty}(\hat{B})}}{\left(2 \tau^{k+3}\right)^{1 / \beta}}+C\left(r_{n}\right)^{\frac{1}{\beta}-1}\left(2 \tau^{k+3}\right)^{(2 \beta-1) / \beta}\|F\|_{L^{\infty}(\hat{B})} \\
\leq & C\left(r_{n}\right)^{\frac{1}{\beta}-1} \tau^{k\left(1-\frac{1}{\beta}\right)} \omega\left(2 \tau^{k}\right)+C \omega\left(2 \tau^{k}\right)\left(r_{n}\right)^{\frac{1}{\beta}-1} \tau^{k\left(1-\frac{1}{\beta}\right)} .
\end{aligned}$$
Since $B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta} / 2\right)=B_{\hat{g}_{\beta}}\left(x, 2^{1-\beta} \tau^{k+3}\right)$,
$$B_{\beta}\left(\tilde{p}, 2 \tau^{k+4}\right) \subset \cup_{x \in \mathcal{S} \cap B_{\beta}\left(\tilde{p}, 2 \tau^{k+3}\right)} B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta} / 2\right) .$$
We complete the proof of Lemma 2.12 by combining (2.43) and the above observation. \(\square\)

Lemma 2.13. There exists $C=C(n, \beta)>0$ such that for all $2 \leq k \leq \ell$,
$$\begin{gathered}
\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{r_{n}^{2} \partial\left(\theta_{n}\right)^{2}}\right|(z)+\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{r_{n} \partial r_{n} \partial \theta_{n}}\right|(z) \leq C\left(r_{n}\right)^{\frac{1}{\beta}-2} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(\tau^{k}\right), \\
\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial\left(r_{n}\right)^{2}}\right|(z) \leq C\left(r_{n}\right)^{\frac{1}{\beta}-2} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(\tau^{k}\right) .
\end{gathered}$$
for all $z \in B_{\beta}\left(\tilde{p}, 2 \tau^{k+4}\right) \backslash \mathcal{S}$.
Proof. Applying the gradient estimate to the $g_{\beta}$-harmonic function $D^{\prime} h_{k}$, we have
$$\left\|\nabla_{g_{\beta}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+1}\right) \backslash \mathcal{S}\right)} \leq C(n) \omega\left(2 \tau^{k}\right) .$$
This implies
$$\left\|\frac{\partial\left(D^{\prime} h_{k}\right)}{r_{n} \partial \theta_{n}}\right\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+1}\right) \backslash \mathcal{S}\right)} \leq C(n) \omega\left(2 \tau^{k}\right) .$$

Since $\partial_{\theta_{n}} D^{\prime} h_{k}$ is continuous and $g_{\beta}$-harmonic in $B_{\beta}\left(\tilde{p}, 2 \tau^{k+1}\right)$, we define $G$ by
$$G=\left|z_{n}\right|^{2(1-\beta)} \frac{\partial^{2}\left(\partial_{\theta_{n}} D^{\prime} h_{k}\right)}{\partial z_{n} \partial \bar{z}_{n}}=-\sum_{j=1}^{2 n-2}\left(D_{j}\right)^{2} \partial_{\theta_{n}} D^{\prime} h_{k} .$$
Since
$$\|G\|_{L^{\infty}\left(B_{\beta}\left(\tilde{p}, 2 \tau^{k+1}\right)\right)} \leq C(n) \tau^{-k} \omega\left(2 \tau^{k}\right),$$
it follows from Proposition 2.1 that on $B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta} / 2\right) \backslash\{0\}$ by the same choice of $x$ as in the proof of Lemma 2.12 that
$$\left|\frac{\partial\left(\partial_{\theta_{n}} D^{\prime} h_{k}\right)}{\partial z_{n}}\right| \leq C \frac{\left\|\partial_{\theta_{n}} D^{\prime} h_{k}\right\|_{L^{\infty}(\hat{B})}}{\left(2 \tau^{k+3}\right)^{1 / \beta}}+C\|G\|_{L^{\infty}(\hat{B})}\left(2 \tau^{k+3}\right)^{(2 \beta-1) / \beta},$$
where $\hat{B}$ is defined in (2.42). Equivalently, on $B_{\mathbb{C}}\left(x,\left(2 \tau^{k+3}\right)^{1 / \beta} / 2\right) \backslash\{0\}$,
$$\begin{aligned}
& \left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{r_{n} \partial\left(\theta_{n}\right)^{2}}\right|+\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial r_{n} \partial \theta_{n}}\right| \\
\leq & C \frac{\left(r_{n}\right)^{\frac{1}{\beta}-1}\left\|\partial_{\theta} D^{\prime} h_{k}\right\|_{L^{\infty}(\hat{B})}}{\left(2 \tau^{k+3}\right)^{1 / \beta}}+C\left(r_{n}\right)^{\frac{1}{\beta}-1}\left(2 \tau^{k+3}\right)^{(2 \beta-1) / \beta}\|G\|_{L^{\infty}(\hat{B})} \\
\leq & C\left(r_{n}\right)^{\frac{1}{\beta}-1} \tau^{k\left(1-\frac{1}{\beta}\right)} \omega\left(2 \tau^{k}\right) .
\end{aligned}$$
We have now completed the proof of the estimate (2.44).
We now use (2.44) to show (2.45). From equation (2.41), we have
$$\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial\left(r_{n}\right)^{2}}=-\frac{1}{r_{n}} \frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}-\frac{1}{\beta^{2}\left(r_{n}\right)^{2}} \frac{\left.\partial^{2}\left(D^{\prime} h_{k}\right)\right)}{\partial\left(\theta_{n}\right)^{2}}+F .$$
Then (2.45) is proved by combining with (2.44), Lemma 2.12 and the estimate (2.40) on $F$. \(\square\)

Lemma 2.14. Let $p, q \in B_{\beta}(0,1 / 2) \backslash \mathcal{S}$ and $d=d_{\beta}(p, q)$ for some $\beta \in(1 / 2,1)$. There exists $C=C(n, \beta)>0$ such that for all $2 \leq k \leq \ell$,
$$\left|\partial_{r_{n}} D^{\prime} h_{k}(p)-\partial_{r_{n}} D^{\prime} h_{k}(q)\right| \leq C d^{\frac{1}{\beta}-1} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(\tau^{k}\right),$$
$$\left|\left(\left(r_{n}\right)^{-1} \partial_{\theta_{n}} D^{\prime} h_{k}\right)(p)-\left(\left(r_{n}\right)^{-1} \partial_{\theta_{n}} D^{\prime} h_{k}\right)(q)\right| \leq C d^{\frac{1}{\beta}-1} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(\tau^{k}\right) .$$
Proof. We first prove (2.48). Let $p=\left(s(p) ; r_{n}(p), \theta_{n}(p)\right)$ and $q=\left(s(q) ; r_{n}(q), \theta_{n}(q)\right)$, where $s=\left(s_{1}, \ldots, s_{2 n-2}\right)$ and $r_{n}=\left|z_{n}\right|^{\beta}, \theta_{n}=\arg z_{n}$. We choose a minimal $g_{\beta}$-geodesic $\gamma(t)=$ $\left(s(t) ; r_{n}(t), \theta_{n}(t)\right)$ for $t \in[0, d]$ connecting $p$ and $q$. Then by definition,
$$\left|\gamma^{\prime}(t)\right|_{g_{\beta}}^{2}=\left|s^{\prime}(t)\right|^{2}+\left(r_{n}^{\prime}(t)\right)^{2}+\beta^{2} r_{n}(t)^{2}\left(\theta_{n}^{\prime}(t)\right)^{2}=1,$$
and obviously $|s(p)-s(q)| \leq d, \quad\left|r_{n}(p)-r_{n}(q)\right| \leq d$.
\begin{itemize}
\item[(1)] $r_{p} \leq 2 d$. We will construct a piecewise smooth path $\gamma=\gamma_{1}+\gamma_{2}+\gamma_{3}$ joining $p$ and $q$ instead of a minimal geodesic. Let
$$q^{\prime}=\left(s(p) ; r_{n}(q), \theta_{n}(q)\right), \quad p^{\prime}=\left(s(p) ; r_{n}(p), \theta_{n}(q)\right)$$
and let $\gamma_{1}, \gamma_{2}, \gamma_{3}$ be the minimal geodesics joining $q$ and $q^{\prime}, q^{\prime}$ and $p^{\prime}, p^{\prime}$ and $p$ respectively (see Figure 1).
\end{itemize}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/66abaf56-3fb1-4378-8a4a-09c7ab4c0b30-20.jpg?height=417&width=570&top_left_y=297&top_left_x=774}
\captionsetup{labelformat=empty}
\caption{Figure 1.}
\end{figure}