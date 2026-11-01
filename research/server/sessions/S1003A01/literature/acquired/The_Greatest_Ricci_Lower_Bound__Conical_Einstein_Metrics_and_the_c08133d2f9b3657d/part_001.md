---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Greatest Ricci Lower Bound, Conical Einstein Metrics and the Chern Number Inequality]

---
source_file: 1207_4839v1.pdf
converter: mathpix
format: mmd
---

\title{
THE GREATEST RICCI LOWER BOUND, CONICAL EINSTEIN METRICS AND THE CHERN NUMBER INEQUALITY
}

\author{
JIAN SONG AND XIAOWEI WANG
}

\begin{abstract}
We partially confirm a conjecture of Donaldson relating the greatest Ricci lower bound $R(X)$ to the existence of conical Kähler-Einstein metrics on a Fano manifold $X$. In particular, if $D \in\left|-K_{X}\right|$ is a smooth simple divisor and the Mabuchi $K$-energy is bounded below, then there exists a unique conical Kähler-Einstein metric satisfying $\operatorname{Ric}(g)=\beta g+(1-\beta)[D]$ for any $\beta \in(0,1)$. We also construct unique smooth conical toric Kähler-Einstein metrics with $\beta=R(X)$ and a unique effective $\mathbb{Q}$-divisor $D \in\left[-K_{X}\right]$ for all toric Fano manifolds. Finally we prove a Miyaoka-Yau type inequality for Fano manifolds with $R(X)=1$.
\end{abstract}

Contents
\begin{itemize}
\item[1.] Introduction
\item[2.] $R(X)$ and conical Kähler-Einstein metrics
\item[2.1.] Paired energy functionals
\item[2.2.] Pluri-anticanonical system
\item[2.3.] The $\alpha$-invariant and the Moser-Trudinger inequality
\item[2.4.] An interpolation formula
\item[2.5.] Proof of Theorem 1.1
\item[2.6.] Proof of Theorem 1.2
\item[3.] Conical toric Käher-Einstein metrics
\item[3.1.] Conical toric Kähler metrics
\item[3.2.] Proof of Theorem 1.3
\item[4.] The Chern number inequality
\item[4.1.] Curvature estimates
\item[4.2.] Chern forms for conical Kähler metrics
\item[4.3.] The Gauss-Bonnet and signature theorems for Kähler surfaces with conical singularities
\item[4.4.] The Chern number inequality on Fano manifolds
\item[4.5.] The Chern number inequality on minimal manifolds of general type
\item[5.] Discussions
\item[] References
\end{itemize}

\section*{1. Introduction}

The existence of Kähler-Einstein metrics has been a central problem in Kähler geometry since Yau's celebrated solution [51] to the Calabi conjecture. Constant scalar curvature metrics with conical singularities have been extensively studied in [28, 48, 26] for Riemann surfaces. In general, we can consider a pair $(X, D)$ for an $n$-dimensional compact Kähler

\footnotetext{
The first named author is supported by National Science Foundation grants DMS-0847524 and a Sloan Foundation Fellowship.
}
manifold and a smooth complex hypersurface $D$ of $X$. A conical Kähler metric $g$ on $X$ with cone angle $2 \pi \beta$ along $D$ is locally equivalent to the following model edge metric
$$g=\sum_{j=1}^{n-1} d z_{j} \otimes d \bar{z}_{j}+\left|z_{n}\right|^{-2(1-\beta)} d z_{n} \otimes d \bar{z}_{n}$$
if $D$ is defined by $z_{n}=0$. Applications of conical Kähler metrics are proposed [49, 43] to obtain various Chern number inequalities. Recently, Donaldson developed the linear theory to study the existence of canonical conical Kähler metrics in [15]. And Brendle in [8] solved Yau's Monge-Ampère equations for conical Kähler metrics with cone angle $2 \pi \beta$ for $\beta \in(0,1 / 2)$ along a smooth divisor $D$. The general case is settled by Jeffres, Mazzeo and Rubinstein [18] for all $\beta \in(0,1)$. As an immediate consequence, there always exists conical Kähler-Einstein metrics with negative or zero constant scalar curvature with cone angle $2 \pi \beta$ along a smooth divisor $D$ for $\beta \in(0,1)$. When $X$ is a Fano manifold, Donaldson'proposes to study the conical Kähler-Einstein equation
$$\operatorname{Ric}(\omega)=\beta \omega+(1-\beta)[D],$$
where $D$ is smooth simple divisor in the anticanonical class $\left[-K_{X}\right]$ and $\beta \in(0,1)$. One of the motivations is that one can study the existence problem for smooth Kähler-Einstein metrics on $X$ by deforming the cone angle. Such an approach can be regarded as a variant of the standard continuity method.

In particular, since Tian and Yau have already established the existence of a complete Ricci-flat Kähler metric on the non-compact manifold $X \backslash D$ in [46], one would expect that (1.1) is solvable for $\beta$ sufficient small. This is comfirmed successfully by Berman in [5]. Now the question is how large $\beta$ can be. The largest $\beta$ is closely related to the following holomorphic invariant known as the greatest Ricci lower bound first introduced by Tian in [42].

Definition 1.1. Let $X$ be a Fano manifold. The greatest Ricci lower bound $R(X)$ is defined by
$$R(X)=\sup \left\{\beta \mid \operatorname{Ric}(\omega) \geq \beta \omega, \text { for some smooth Kähler metric } \omega \in c_{1}(X)\right\} .$$

It is proved by Szekelyhidi in [40] that $[0, R(X))$ is the maximal interval for the continuity method to solve the Kähler-Einstein equation on a Fano manifold $X$. In particular, it is independent of the choice for the initial Kähler metric when applying the continuity method. The invariant $R(X)$ is explicitly calculated for $\mathbb{P}^{2}$ blown up at one point by Szekelyhidi [40], and for all toric Fano manifolds by Li [21]. It is well-known that Mabuchi $K$-energy being bounded from below implies $R(X)=1$ and it is proved in [30] that $R(X)=1$ implies $X$ being $K$-semistable. The following conjecture is proposed by Donaldson in [15] to relate $R(X)$ to the existence of conical Kähler-Einstein metrics.

Conjecture 1.1. There does not exist a conical Kähler-Einstein metric solving (1.1) if $\beta \in(R(X), 1]$, while there exists one if $\beta \in(0, R(X))$.

This conjecture can be considered as a different geometric interpretation of the invariant $R(X)$. Another importance of the conjecture lies in the fact that it supplies a new approach to the Yau's conjecture [53] on the equivalence of existence of Kähler-Einstein metric for Fano manifolds and certain algebro-geometric stability condition, which is refined and extended by Tian 44 and Donaldson [11]. The algebro-geometric aspect of Conjecture 1.1
has been studied by Li [23], Sun [39], Odaka-Sun [31] and Berman [6]. In particular, the notion of Log $K$-stability is introduced in [23] and [39] as the algebro-geometric obstruction to solve equation (1.1). In particular, $R(X)$ can be applied to test the $\log K$-stability of $X$ when it is toric Fano. In [6], Berman proves that Log $K$-stability is a necessary condition to the solution of (1.1). This naturally leads to the Log version of Yau-Tian-Donaldson conjecture, that is, to establish the equivalence of the solvability of (1.1) and the Log K-stability of $(X, D)$ (cf.[23] and [31]). An interesting observation made by Sun in [39] is that $K$-stability implies $\log K$-stability.

Now we describe the main results of the present work. The first one is to partially confirm Conjecture 1.1. We consider a more general class of conical Kähler-Einstein metrics with smooth simple divisors in any pluricanonical systems, and remove the assumption in [15] on $D$ by showing there exists no holomorphic vector field tangential to $D$ (c.f. Theorem 2.1).

Theorem 1.1. Let $X$ be a Fano manifold and $R(X)$ be the greatest lower bound of Ricci curvature of $X$.
\begin{itemize}
\item[(1)] For any $\beta \in[R(X), 1]$ and any smooth simple divisor $D \in\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$, there does not exist a smooth conical Kähler-Einstein metric $\omega$ satisfying
\end{itemize}
$$\operatorname{Ric}(\omega)=\beta \omega+\frac{1-\beta}{m}[D],$$
if $R(X)<1$.
\begin{itemize}
\item[(2)] For any $\beta \in(0, R(X))$, there exist a smooth simple divisor $D \in\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$and a smooth conical Kähler-Einstein metric $\omega$ satisfying (1.3).
\end{itemize}

The second part of the theorem is not completely satisfactory in the sense that one would like to have an $m$ that is independent of $\beta \in(0, R(X))$. In the case when the Mabuchi $K$-energy is bounded below, or more generally $R(X)=1$, we show that $D$ and $\beta$ do not rely on $\beta$.

Theorem 1.2. Let $X$ be a Fano manifold. If the Mabuchi $K$-energy $\mathcal{M}$ is bounded below and if $D \in\left|-K_{X}\right|$ is a smooth simple divisor, then for any $\beta \in(0,1)$ there exists a smooth conical Kähler-Einstein metric satisfying the conical Kähler-Einstein equation
$$\operatorname{Ric}(\omega)=\beta \omega+(1-\beta)[D] .$$

In general, if the paired Mabuchi $K$-energy $\mathcal{M}_{D, R(X)}$ is bounded below for a smooth simple divisor $D \in\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$, then for any $\beta \in(0, R(X))$ there exists a smooth conical Kähler-Einstein metric satisfying equation (1.3).

We would like to remark that most results of Theorem 1.1 and 1.2 are independently obtained by Li and Sun [24]. Theorem 1.2 might have many applications. In particular, if the Mabuchi $K$-energy is bounded below, there exists a sequence of conical Kähler-Einstein metrics $\operatorname{Ric}\left(g_{\epsilon}\right)=(1-\epsilon) g+\epsilon[D]$ as $\epsilon \rightarrow 0$. ( $X, g_{\epsilon}$ ) might converge in Gromov-Hausdorff topology to a $\mathbb{Q}$-Fano variety $X_{\infty}$ coupled with a canonical Kähler-Einstein metric. Theorem 1.2 also holds if $R(X)=1$ and $D \in\left|-m K_{X}\right|$ for some $m \geq 2$ as in the following proposition. By Bertini's theorem, there always exists a smooth simple divisor $D \in\left|-m K_{X}\right|$ for $m$ sufficiently large.

Proposition 1.1. Let $X$ be a Fano manifold and $D \in\left|-m K_{X}\right|$ be a smooth simple divisor for some $m \geq 2$. Then for any $\beta \in\left(0, \frac{(m-1) \cdot R(X)}{m-R(X)}\right)$, there exists a smooth conical Kähler-Einstein metric $\omega$ satisfying (1.3) for $D$. In particular, when $R(X)=1$, equation (1.3) with $D$ is solvable for any $\beta \in(0,1)$.

The invariant $R(X)$ can also be identified as the optimal constant for the nonlinear Moser-Trudinger inequality. Let $X$ be a Fano manifold and $\omega \in c_{1}(X)$ be a smooth Kähler metric on $X$. One can define the following $F$-functional by
$$F_{\omega, \beta}=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X} e^{-\beta \varphi} \omega^{n},$$
where
$$J_{\omega}(\varphi)=\frac{\sqrt{-1}}{V} \sum_{i=0}^{n-1} \frac{i+1}{n+1} \int_{X} \partial \varphi \wedge \bar{\partial} \varphi \wedge \omega^{i} \wedge \omega_{\varphi}^{n-1-i}$$
is the Aubin-Yau functional, $\omega_{\varphi}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0$ and $V=\int_{X} \omega^{n}$. As a corollary of Theorem 1.1, we can establish a connection between $R(X)$ and the Moser-Trudinger inequality.
\begin{itemize}
\item[(1)] If $\beta \in(0, R(X)), F_{\omega, \beta}$ is bounded below and $J$-proper (see Definition 2.2) on $P S H(X, \omega) \cap L^{\infty}(X)$, or equivalently, there exist $\epsilon, C_{\epsilon}>0$ such that the following Moser-Truding inequality holds
$$\int_{X} e^{-\beta \varphi} \omega^{n} \leq C_{\epsilon} e^{(\beta-\epsilon) J_{\omega}(\varphi)-\frac{\beta}{V} \int_{X} \varphi \omega^{n}}$$
for $\varphi \in P S H(X, \omega) \cap L^{\infty}(X)$.
\item[(2)] If $\beta \in(R(X), 1)$, then
$$\inf _{P S H(X, \omega) \cap L^{\infty}(X)} F_{\omega, \beta}(\cdot)=-\infty .$$
\end{itemize}

It is first proved in [44, 47] for the properness of $F$-functional on Fano Kähler-Einstein manifolds without holomorphic vector fields. The $J$-properness for $F$ is conjectured in this case in [44] and is later proved in [33]. The presence of the smooth divisor $D$ for $\beta \in(0,1]$ blocks holomorphic vector fields as shown in Theorem 2.1. It is interesting to ask if $F_{\omega, \beta}$ is always bounded below on $P S H(X, \omega) \cap L^{\infty}(X)$ if $\beta=R(X)$. In the case of toric Fano manifolds, $F_{\omega, \beta}$ is indeed bounded from below if $\beta=R(X)$ as a corollary of the following theorem (Corollary 3.1). A more interesting problem will be to understand the limiting behavior of the conical Kähler-Einstein metrics as $\beta \rightarrow R(X)$ as the holomorphic vector field will appear in the limiting space. The following theorem serves an example for the above speculation.

Theorem 1.3. Let $X$ be a toric Fano manifold. Then there exist a unique effective toric $\mathbb{Q}$-divisor $D \in\left|-K_{X}\right|$ and a unique smooth toric conical Kähler metric $\omega$ satisfying
$$\operatorname{Ric}(\omega)=R(X) \omega+(1-R(X))[D] .$$
Furthermore, $R(X)$ is the largest number for $\beta \in(0,1]$ such that
$$\operatorname{Ric}(\omega)=\beta \omega+(1-\beta)\left[D_{\beta}\right]$$
admits a smooth conical toric solution $\omega_{\beta}$ for an effective toric $\mathbb{R}$-divisor $D_{\beta}$ in $\left[-K_{X}\right]$.

We remark that the divisor $D$ can not be smooth, instead it is a union of effective smooth toric $\mathbb{Q}$-divisors with simple normal crossings. Theorem 1.3 is closely related to the results of [22] with a different approach for the limiting behavior of the continuity method. The proof of Theorem 1.3 relies on the toric setting introduced in [12, 13] and the estimates in [50]. For $\beta>R(X)$, there still exists a smooth conical solution for equation (1.6), however, $D_{\beta}$ won't be effective and so the Ricci current of the conical metric cannot be positive. In Theorem 1.3, $R(X)$ will be explicitly calculated as in [21] and $D$ is determined by Lemma 3.2 and Lemma 3.3 . For example, when $X$ is $\mathbb{P}^{2}$ blown up at one point, it admits a toric $\mathbb{P}^{1}$ bundle $\pi: X \rightarrow \mathbb{P}^{1}$, then $R(X)=6 / 7$ and $D=2 D_{\infty}+\left(H_{1}+H_{2}\right) / 2$, where $D_{\infty}$ is the section at the infinity, $H_{1}$ and $H_{2}$ are the two $\mathbb{P}^{1}$ fibres invariant under the torus action. This seems to suggest that Donaldson's conjecture might only hold for smooth simple divisors lying in the pluri-anti-canonical system. In fact, it is shown in [24] Theorem 1.3 can be applied to prove Conjecture 1.1 in the toric case when one is allowed to replace $\left|-K_{X}\right|$ by the linear system of a suitable power of $-K_{X}$.

Finally, we will give some applications of Theorem 1.2. In general, the conical Kähler metrics do not have bounded curvature tensors, as they might blow up near the conical divisor, particularly when the cone angle is greater than $\pi$. However, we can show that if the Ricci curvature of a conical Kähler metric is bounded, its curvature tensors are always bounded in $L^{2}$-norm.

Proposition 1.2. Let $X$ be a Kähler manifold and $D$ be a smooth simple divisor on $X$. Let $g$ be a smooth conical Kähler metric on $X$ with cone angle $2 \pi \beta$ along $D$ with $\beta \in(0,1)$. If the Ricci curvature of $g$ is bounded, the $L^{2}$-norm of the curvature tensors of $g$ is also bounded.

When we say the Ricci curvature of a conical Kähler metric $g$ is bounded, it means that the Ricci curvature of $g$ is uniformly bounded on $X \backslash D$ by ignoring the mass along $D$ in the Ricci current. Proposition 1.2 enables us to define Chern characters, and in particular the Chern numbers for those conical Kähler metrics and derive corresponding Gauss-Bonnet and signature formulas for Kähler surfaces with conical singularities along a smooth holomorphic curve $\Sigma$. This is related to recent results of Atiyah and Lebrun [1] for smooth Riemannian 4 -folds. In fact, the bound of $L^{2}$-norm of the curvature tensors only depend on the scalar curvature bound and topological invariants such as intersection numbers among $D$, the first, second Chern classes. When the greatest Ricci lower bound $R(X)$ is 1, we have the Miyaoka-Yau type inequality holds for $X$ as in the Kähler-Einstein case [29, 52]. In such a case, $X$ is $K$-semistable [30] and the result below reflects the general perspective connecting $K$-semistability and the Chern number inequality.

Theorem 1.4. Let $X$ be a Fano manifold. If $R(X)=1$, then the Miyaoka-Yau type inequality holds
$$c_{2}(X) \cdot c_{1}(X)^{n-2} \geq \frac{n}{2(n+1)} c_{1}(X)^{n} .$$
In general, if $D \in\left|-K_{X}\right|$ is a smooth simple divisor and if the paired Mabuchi $K$-energy $\mathcal{M}_{D, \beta}$ is bounded below, then
$$c_{2}(X) \cdot c_{1}(X)^{n-2} \geq \frac{n \beta^{2}}{2(n+1)} c_{1}(X)^{n} .$$

Parallel argument can be applied to give a complete proof of the Chern number inequality for smooth minimal models of general type using conical Kähler-Einstein metrics. This approach is first proposed by Tsuji [49], while the analytic estimates seem missing. We remark that the first complete proof for smooth minimal models of general type is due to Zhang [54] by using the Kähler-Ricci flow.

\section*{2. $R(X)$ and conical Kähler-Einstein metrics}
2.1. Paired energy functionals. In this section, we recall the paired energy functionals originally introduced in [5].

Definition 2.1. Let $X$ be a Fano manifold and $\omega \in c_{1}(X)$ be a Kähler current with bounded local potential and $\Omega_{\theta}$ be a nonnegative real $(n, n)$-current on $X$ whose curvature
$$\theta=-\sqrt{-1} \partial \bar{\partial} \log \Omega_{\theta} \in c_{1}(X)$$
is a nonnegative (1, 1)-current. Let $\Omega_{\omega}$ be a nonnegative real $(n, n)$-current on $X$ defined by
$$\sqrt{-1} \partial \bar{\partial} \log \Omega_{\omega}=\omega .$$
Suppose that for some $\beta \in(0,1]$,
$$\int_{X}\left(\Omega_{\omega}\right)^{\beta}\left(\Omega_{\theta}\right)^{1-\beta}=V=c_{1}(X)^{n} .$$
We define the paired F-functional by
$$F_{\omega, \theta, \beta}(\varphi)=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \Omega_{\omega}\right)^{\beta}\left(\Omega_{\theta}\right)^{1-\beta},$$
for $\varphi \in P S H(X, \omega) \cap L^{\infty}(X)$, where
$$J_{\omega}(\varphi)=\frac{\sqrt{-1}}{V} \sum_{i=0}^{n-1} \frac{i+1}{n+1} \int_{X} \partial \varphi \wedge \bar{\partial} \varphi \wedge \omega^{i} \wedge \omega_{\varphi}^{n-1-i}$$
is the Aubin-Yau $J$-functional and $\omega_{\varphi}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi \geq 0$.
The Euler-Lagrangian equation for (2.9) is given by
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=\left(e^{-\varphi} \Omega_{\omega}\right)^{\beta}\left(\Omega_{\theta}\right)^{1-\beta},$$
and the corresponding curvature equation is
$$\operatorname{Ric}\left(\omega_{\varphi}\right)=\beta \omega_{\varphi}+(1-\beta) \theta .$$

When $\beta=1, F_{\omega, \theta, \beta}(\varphi)=F_{\omega}$ is the original Ding's functional [10]. The paired $F$ -functional also satisfies the cocycle condition by slightly modifying the proof for the original $F$-functional.

Lemma 2.1. $F_{\omega, \theta, \beta}$ satisfies the following cocycle condition
$$F_{\omega, \theta, \beta}(\varphi)-F_{\omega_{\psi}, \theta, \beta}(\varphi-\psi)=F_{\omega, \theta, \beta}(\psi)$$
for any $\varphi, \psi \in P S H(X, \omega) \cap L^{\infty}(X)$.
If we write $F\left(\omega, \omega_{\varphi}\right)=F_{\omega, \theta, \beta}(\varphi)$, then the cocycle condition is equivalent to the following
$$F\left(\omega, \omega_{\varphi}\right)+F\left(\omega_{\varphi}, \omega_{\psi}\right)+F\left(\omega_{\psi}, \omega\right)=0 .$$

Definition 2.2. We say a functional $G(\cdot)$ is $J$-proper on $P S H(X, \omega) \cap L^{\infty}(X)$ if there exist $\delta, C_{\delta}>0$ such that
$$G(\varphi) \geq \delta J_{\omega}(\varphi)-C_{\delta}$$
for all $\varphi \in \operatorname{PSH}(X, \omega) \cap L^{\infty}(X)$.
Let $X$ be a Fano manifold and $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$. Let $s$ be a defining section of $[D]$. Since $s \in H^{0}\left(X,-m K_{X}\right)$,
$$\Omega_{D}=|s|^{-\frac{2}{m}}=(s \otimes \bar{s})^{-\frac{1}{m}}$$
can be considered as a smooth nonnegative real $(n, n)$-form with poles along $D$ of order $m^{-1}$. Obviously, $\operatorname{Ric}\left(\Omega_{D}\right)=-\sqrt{-1} \partial \bar{\partial} \log \Omega_{D}=m^{-1}[D]$. We then define the following notations for conveniences.

Definition 2.3. Let $D \in\left|-m K_{X}\right|$ be a smooth simple divisor for some $m \in \mathbb{Z}^{+}$. We define
$$\begin{aligned}
\mathcal{F}_{\omega, \beta}(\varphi) & =F_{\omega, m^{-1}[D], \beta}(\varphi) \\
& =J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X} e^{-\beta \varphi}\left(\Omega_{\omega}\right)^{\beta}\left(\Omega_{D}\right)^{1-\beta}
\end{aligned}$$
and
$$F_{\omega, \beta}(\varphi)=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X} e^{-\beta \varphi} \omega^{n} .$$

In order to relate the Moser-Trudinger inequality to $R(X)$, we introduce
Definition 2.4. Let $X$ be a Fano manifold and $\omega \in c_{1}(X)$ be a smooth Kähler metric. We define the optimal Moser-Trudinger constant by
$$\mathfrak{m t}(X)=\sup \left\{\beta \in(0,1] \mid \inf _{P S H(X, \omega) \cap L^{\infty}(X)} F_{\omega, \beta}(\cdot)>-\infty\right\} .$$

It is straightforward to verify that the invariant $\mathfrak{m t}(X)$ does not depend on the choice of the Kähler metric $\omega \in c_{1}(X)$.

We also define the following paired Mabuchi $K$-energy for conical Kähler metrics first introduced in [5]. Here a conical Kähler metric is called smooth if it a polyhomogenous Kähler edge metric defined by Jeffres, Mazzeo and Rubinstein in [18] and we let $C_{D, \beta}^{\infty}(X)$ denote the set of all smooth conical Kähler metrics with cone angle $2 \pi \beta$ along the smooth divisor $D$.

Definition 2.5. Let $X$ be a Fano manifold. Suppose $\omega$ and $\omega_{\varphi}$ are two smooth conical Kähler metrics in $c_{1}(X)$ with cone angle $2 \pi(1-(1-\beta) / m)$ along a smooth simple divisor $D \in\left|-m K_{X}\right|$. The paired Mabuchi $K$-energy is defined by
$$\mathcal{M}_{\omega, \beta}(\varphi)=\frac{1}{V} \int_{X} \log \frac{\omega_{\varphi}^{n}}{\omega_{n}}-\beta\left(I_{\omega}-J_{\omega}\right)_{\omega}(\varphi)+\frac{1}{V} \int_{X} h_{\omega}\left(\omega^{n}-\omega_{\varphi}^{n}\right),$$
where $h_{\omega}$ is the Ricci potential of $\omega$ defined by $\sqrt{-1} \partial \bar{\partial} h_{\omega}=\operatorname{Ric}(\omega)-\omega$, and
$$I_{\omega}(\varphi)=\sqrt{-1} \sum_{i=0}^{n-1} \int_{X} \partial \varphi \wedge \bar{\partial} \varphi \wedge \omega^{i} \wedge \omega_{\varphi}^{n-i-1}$$
is the Aubin-Yau $I$-functional.

It is proved in [5] that if the conical Kähelr-Einstein equation is solvable for the data $(D, \beta)$, both $\mathcal{F}_{\omega, \beta}$ and $\mathcal{M}_{\omega, \beta}$ are bounded below $P S H(X, \omega) \cap C^{\infty}(X)_{D, \beta}$. Furthermore, if one is bounded below, the other must also be bounded below, and conversely, if either of the functionals is $J$-proper, the Monge-Ampère equation associated to the conical Kähler-Einstein equation admits a bounded solution [5]. Moreover, the solution is a smooth conical Kähler-Einstein metric in the sense of [18].
2.2. Pluri-anticanonical system. In this section, we will remove the assumption on the smooth simple divisor $D$ in [15] and construct conical Kähler-Einstein metrics by deforming the angle along the continuity method.

The following lemma is an immediate consequence of the adjunction formula and Bertini's Theorem.

Lemma 2.2. Let $X$ be a Fano manifold of $\operatorname{dim} X \geq 2$. For any sufficiently large $m \in \mathbb{Z}^{+}$, there exists a smooth simple divisor $D \in\left|-m K_{X}\right|$. In particular,
$$c_{1}(D)=\left.(1-m) c_{1}(X)\right|_{D}=\left.\frac{1-m}{m}[D]\right|_{D} .$$

This shows that the smooth simple divisor $D$ lies in $\left|-m K_{X}\right|$ is a Calabi-Yau manifold if and only if $m=1$.
Theorem 2.1. Let $X$ be a Fano manifold of $\operatorname{dim} X \geq 2$ and $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$. Then there does not exist any holomorphic vector field tangential to $D$.

Proof. For $\operatorname{dim} X=2$ it follows from the classification that if $X$ admits a nontrivial holomorphic vector field, $X$ is isomorphic to $\mathbb{P}^{2}, \mathbb{P}^{1} \times \mathbb{P}^{1}$ or $\mathbb{P}^{2}$ blown up at 1,2 or 3 points. $D \in\left|-m K_{X}\right|$ implies that $g(D) \geq 1$. For $\mathbb{P}^{2}$ blown up at $0,1,2$ or 3 points, any holomorphic vector field on $X$ is the lifting of a holomorphic vector field on $\mathbb{P}^{2}$ fixing the blown-up points. Hence any smooth invariant divisor of such holomorphic vector fields on $X$ must be $\mathbb{P}^{1}$ with $g(D)=0$. It is also straightforward to check that any invariant divisor on $\mathbb{P}^{1} \times \mathbb{P}^{1}$ must also be $P^{1}$. So from now on let us assume that $\operatorname{dim} X \geq 3$.

First, we claim that if there exists such a holomorphic vector field, it must vanish along $D$. Since $X$ is Fano, we have $\pi_{1}(X)=0$ and hence $\pi_{1}(D)=0$ by Lefschetz hyperplane theorem and our assumption that $\operatorname{dim} X \geq 3$. Since $m>0$, either $c_{1}(D)<0$ or $D$ is a simply connected Calabi-Yau manifold by Lemma 2.2. In both cases $D$ does not admit any nontrivial holomorphic vector field. So our claim is proved.

Second, we claim there is no holomorphic vector field vanishing along $D$. It suffices to show that
$$H^{0}\left(X, T X \otimes K_{X}^{m}\right)=0$$
thanks to the following exact sequence
$$\left.0 \longrightarrow T X \otimes K_{X}^{m} \longrightarrow T X \longrightarrow T X\right|_{D} \longrightarrow 0 .$$
Since $T X \otimes K_{X} \cong \Omega_{X}^{n-1}$, we have
$$\left.H^{0}\left(X, T X \otimes K_{X}^{m}\right)=H^{0}\left(X, \Omega_{X}^{n-1} \otimes K_{X}^{\otimes(m-1)}\right)\right) .$$
Now if $m>1$ then the right hand side is 0 by Kodaira-Akizuki-Nakano vanishing theorem and the fact that $K_{X}$ is negative. For $m=1$, equation (2.16) follows from $H^{0}\left(X, \Omega_{X}^{n-1}\right) \cong$ $H^{n-1}\left(X, \mathcal{O}_{X}\right)=0$ by Kodaira vanishing theorem and $X$ being Fano. \(\square\)

Remark 2.1. Theorem 2.1 is speculated by Donaldson [15] and is proved in [5] for the special case when the holomorphic vector field is Hamiltonian and $m=1$.

Combined with the openness result in [15], we immediately have the following corollary.
Corollary 2.1. Let $X$ be a Fano manifold and $D \in|-m K|$ be a smooth simple divisor for some $m \in \mathbb{Z}^{+}$. If there exists a smooth conical Kähler-Einstein metric satisfying
$$\operatorname{Ric}(g)=\beta g+\frac{1-\beta}{m}[D]$$
for some $\beta \in(0,1)$, then there exists $\epsilon>0$ such that for any $\beta^{\prime}$ with $\left|\beta-\beta^{\prime}\right|<\epsilon$, there exists a smooth conical Kähler-Einstein metric $g^{\prime}$ satisfying $\operatorname{Ric}\left(g^{\prime}\right)=\beta^{\prime} g+\frac{1-\beta^{\prime}}{m}[D]$.
2.3. The $\alpha$-invariant and the Moser-Trudinger inequality. Let $X$ be a Fano manifold and $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$. Let $\omega^{\prime} \in c_{1}(X)$ be a smooth Kähler form and let $\Omega_{\omega^{\prime}}$ be a smooth volume form on $X$ such that
$$\operatorname{Ric}\left(\Omega_{\omega^{\prime}}\right)=-\sqrt{-1} \partial \bar{\partial} \log \Omega_{\omega^{\prime}}=\omega^{\prime} .$$

We now apply the continuity method and consider the following family of equations for $\beta \in[0,1]$.
$$\left(\omega^{\prime}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=e^{-t \varphi_{t}}\left(\Omega_{\omega^{\prime}}\right)^{\beta}\left(\Omega_{D}\right)^{1-\beta}, t \in[0, \beta] .$$
We let
$$S=\left\{t \in[0, \beta] \mid \text { (2.17) is solvable for some } t \text { with } \omega_{t} \text { a smooth conical Kähler metric }\right\} \text {. }$$
By the results in [18], $0 \in S$ and $S$ is open. Let $\omega_{t}=\omega+\varphi_{t}$ for any $t \in S$. The curvature equation of (2.17) is given by
$$\operatorname{Ric}\left(\omega_{t}\right)=t \omega_{t}+(\beta-t) \omega^{\prime}+\frac{1-\beta}{m}[D] \geq t \omega_{t} .$$
Hence the Green's function for $\omega_{t}$ is uniformly bounded below by $t$ for all $t \in S$ [18]. Furthermore, let $\Delta_{t}$ be the Laplace operator associated to $\omega_{t}$. Then
$$\Delta_{t} \dot{\varphi}_{t}=-\varphi_{t}-t \dot{\varphi}_{t} .$$

Following the argument for smooth case with slight modification to the conical Kähler metrics, one can show the following proposition. It is proved in a more general setting in [5].

Proposition 2.1. Let $X$ be a Fano manifold and $D \in\left|-m K_{X}\right|$ be a smooth simple divisor.
\begin{itemize}
\item[(1)] If there exists $\beta \in(0,1]$ and a smooth conical Kähler-Einstein metric $\omega_{K E}$ satisfying
$$\operatorname{Ric}\left(\omega_{K E}\right)=\beta \omega_{K E}+\frac{1-\beta}{m}[D],$$
then the paired $F$-functional
$$\mathcal{F}_{\omega_{K E}, \beta}(\varphi)=J_{\omega_{K E}}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega_{K E}^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \Omega_{\omega_{K E}}\right)^{\beta}\left(\Omega_{D}\right)^{1-\beta} .$$
is uniformly bounded below for all $\varphi \in P S H\left(X, \omega_{K E}\right) \cap L^{\infty}(X)$.
\end{itemize}
\begin{itemize}
\item[(2)] If $\omega \in c_{1}(X)$ is a smooth Kähler metric and $\mathcal{F}_{\omega, \beta}(\varphi)$ is $J$-proper on $\operatorname{PSH}(X, \omega) \cap$ $L^{\infty}(X)$ for some $\beta \in(0,1]$, then there exists a unique smooth conical Kähler metric $\omega_{K E}$ solving
$$\operatorname{Ric}\left(\omega_{K E}\right)=\beta \omega_{K E}+\frac{1-\beta}{m}[D] .$$
\end{itemize}

Same argument in the proof of Proposition 2.1 can be applied to prove the following lemma if replacing $m^{-1}[D]$ by a smooth Kähler metric $\theta \in c_{1}(X)$.

Lemma 2.3. Let $X$ be a Fano manifold and $\theta$ be a smooth Kähler metric in $c_{1}(X)$.
\begin{itemize}
\item[(1)] If there exists a smooth Kähler metric $\omega_{\theta}$ on $X$ satisfying
$$\operatorname{Ric}\left(\omega_{\theta}\right)=\beta \omega_{\theta}+(1-\beta) \theta$$
for some $\beta \in(0,1]$. Then
$$F_{\omega_{\theta}, \theta, \beta}(\varphi)=J_{\omega_{\theta}}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega_{\theta}^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X} e^{-\beta \varphi}\left(\Omega_{\omega_{\theta}}\right)^{\beta}\left(\Omega_{\theta}\right)^{1-\beta}$$
is uniformly bounded below on $P S H(X, \omega) \cap L^{\infty}(X)$.
\item[(2)] If $\omega \in c_{1}(X)$ is a smooth Kähler metric and $F_{\omega, \theta, \beta}(\varphi)$ is J-proper on $\operatorname{PSH}(X, \omega) \cap$ $L^{\infty}(X)$ for some $\beta \in(0,1]$, then there exists a unique smooth Kähler metric $\omega_{\theta}$ solving
$$\operatorname{Ric}\left(\omega_{\theta}\right)=\beta \omega_{\theta}+(1-\beta) \theta .$$
\end{itemize}

The $\alpha$-invariant is introduced by Tian [41] to obtain a sufficient condition for the existence of Kähler-Einstein metrics on Fano manifolds. It is shown by Demailly [9] that the $\alpha$-invariant coincides with the log canonical threshold in birational geometry. It is natural to relate the log canonical threshold for pairs to the paired $\alpha$-invariant. It is first introduced in [5] as a generalization for the $\alpha$-invariant.

Definition 2.6. Let $X$ be a Fano manifold and $D \in\left|-m K_{X}\right|$ be a smooth simple divisor. Let $s$ be the defining section of $[D]$ and $h$ be a smooth hermitian metric for $-m K_{X}$. Let $\omega \in c_{1}(X)$ be a smooth Kähler metric. Then we define the paired $\alpha$-invariant for $\beta \in(0,1]$ by
$$\alpha_{D, \beta}(X)=\sup \left\{\alpha>\left.0\left|\sup _{\varphi \in P S H(X, \omega) \cap L^{\infty}(X)} \int_{X}\right| s\right|_{h} ^{-\frac{2(1-\beta)}{m}} e^{-\alpha \beta(\varphi-\sup \varphi)} \omega^{n}<\infty\right\} .$$

It is straightforward to check that the invariant $\alpha_{D, \beta}$ does not depend on the choice of $\omega \in c_{1}(X)$. The following theorem is due to Berman [5] for an effective bound on $\alpha_{D, \beta}$ to construct conical Kähler-Einstein metrics by combining the results in [18].

Theorem 2.2. There exists $\beta_{D} \in(0,1]$ such that for all $\beta \in\left(0, \beta_{D}\right]$ we have
$$\alpha_{D, \beta}(X)>\frac{n}{n+1} .$$
In particular, there exists a smooth conical Kähler-Einstein metric $\omega \in c_{1}(X)$ satisfying
$$\operatorname{Ric}(\omega)=\beta \omega+\frac{1-\beta}{m}[D]$$
for $\beta \in\left(0, \beta_{D}\right)$.

In [36], the first author proves that if the $\alpha$-invariant on an $n$-dimensional Fano manifold is greater $n /(n+1)$, then the $F$-functional is $J$-proper. The following theorem is a generalization for the conical case.

Theorem 2.3. Let $X$ be a Fano manifold and $\omega \in c_{1}(X)$ be a smooth Kähler metric. If $D \in\left|-m K_{X}\right|$ is a smooth simple divisor and if there exists $\beta \in(0,1]$ such that
$$\alpha_{D, \beta}(X)>\frac{n}{n+1},$$
then the functional
$$\mathcal{F}_{\omega, \beta}(\varphi)=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \Omega_{\omega}\right)^{\beta}\left(\Omega_{D}\right)^{1-\beta}$$
as in Definition 2.3, is $J$-proper on $P S H(X, \omega) \cap L^{\infty}(X)$.
Proof. We break the proof into the following two steps.
Step 1. Since $\alpha_{D, \beta}(X)>n /(n+1)$, by Theorem 2.2 there exists a smooth conical Kähler-Einstein metric $\omega_{K E}$ satisfying
$$\operatorname{Ric}\left(\omega_{K E}\right)=\beta \omega_{K E}+\frac{1-\beta}{m}[D] .$$
Let $P S H\left(X, \omega_{K E}, K\right)$ be the set of all $\varphi \in P S H\left(X, \omega_{K E}\right) \cap L^{\infty}(X)$ such that
$$\operatorname{osc}_{X} \varphi=\sup _{X} \varphi-\inf _{X} \varphi \leq(n+1) J_{\omega_{K E}}(\varphi)+K .$$
We claim that $\mathcal{F}_{\omega_{K E}, \beta}$ is $J$-proper for all $\varphi \in P S H\left(X, \omega_{K E}, K\right)$. To see that, take $\alpha$ satisfying
$$\frac{n \beta}{n+1}<\alpha<\beta \min \left(\alpha_{D, \beta}, 1\right)$$
and let $\Omega_{D}=|s|^{2 / m}$ then we have
$$\begin{aligned}
\int_{X} e^{-\beta \varphi} \Omega_{\beta} & =\int_{X} e^{-\alpha(\varphi-\sup \varphi)+(\alpha-\beta) \phi-\alpha \sup \varphi} \Omega_{D} \\
& \leq C e^{(\alpha-\beta) \inf \varphi-\alpha \sup \varphi} \int_{X} e^{-\alpha(\varphi-\sup \varphi)} \Omega_{D} \\
& \leq C e^{(\alpha-\beta) \inf \varphi-\alpha \sup \varphi}
\end{aligned}$$
by the definition of $\alpha_{D, \beta}$. By assumption (2.20), we have
$$\begin{aligned}
\int_{X} e^{-\beta \varphi} \Omega_{D} & \leq C e^{\left.(\beta-\alpha)(n+1) J_{\omega_{K E}}(\varphi)-\beta \sup \varphi\right)} \\
& \leq C e^{(n+1)(\beta-\alpha) J_{\omega_{K E}}(\varphi)-\frac{\beta}{V} \int_{X} \varphi \omega_{K E}^{n}} \\
& =C e^{\beta J_{\omega_{K E}}(\varphi)-((n+1) \alpha-n \beta) J_{\omega_{K E}}(\varphi)-\frac{\beta}{V} \int_{X} \varphi \omega_{K E}^{n}},
\end{aligned}$$
and our claim follows by taking logarithm of both sides of the above inequality.
Step 2. Now we will remove the assumption (2.20) for $\varphi \in P S H(X, \omega) \cap L^{\infty}(X)$. We first consider all $\varphi \in P S H(X, \omega)$ such that $\omega^{\prime}=\omega_{K E}+\sqrt{-1} \partial \bar{\partial} \varphi$ is a smooth conical Kähler metric with cone angle $2 \pi\left(1-\frac{1-\beta}{m}\right)$ along $D$. By applying the same argument
for smooth Kähler-Einstein metrics to solve the continuity method backward, one can show that
$$\left(\omega^{\prime}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=\left(e^{-t \varphi_{t}} \Omega_{\omega^{\prime}}\right)^{\beta} \Omega_{D}^{1-\beta}$$
admits a smooth conical solution for $t \in[0,1]$ because the implicit function theorem can be applied at $t=1$ due to Theorem 2.1. In particular, $\varphi_{1}=-\varphi$.

Let $\omega_{t}=\omega^{\prime}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}$. Note that for $t \geq 1 / 2$, the Ricci curvature of $\omega_{K E}+$ $\sqrt{-1} \partial \bar{\partial}\left(\varphi_{t}-\varphi_{1}\right)=\omega_{t}$ is no less than $\beta / 2$. Then the Green's functions for both $\omega$ and $\omega_{t}$ are uniformly bounded from below by $-G$ for some positive number $G$, and
$$\Delta_{\omega_{K E}}\left(\varphi-\varphi_{1}\right)=\operatorname{tr}_{\omega_{K E}}\left(\omega_{t}-\omega_{K E}\right) \geq-n, \Delta_{\omega_{t}}\left(\varphi_{t}-\varphi_{1}\right) \leq n .$$
Then by the Green's formula, for $t \geq \beta / 2$, we have
$$\frac{1}{V} \int_{X}\left(\varphi_{t}-\varphi_{1}\right) \omega_{K E}^{n}-n G \leq\left(\varphi_{t}-\varphi_{1}\right) \leq \frac{1}{V} \int_{X}\left(\varphi_{t}-\varphi_{1}\right) \omega_{t}^{n}+n G .$$
Hence
$$\operatorname{osc}_{X}\left(\varphi_{t}-\varphi_{1}\right) \leq I_{\omega_{K E}}\left(\varphi_{t}-\varphi_{1}\right)+2 n G \leq(n+1) J_{\omega_{K E}}\left(\varphi_{t}-\varphi_{1}\right)+2 n G .$$
This implies that $\varphi_{t}-\varphi_{1} \in P S H\left(X, \omega_{K E}, 2 n G\right)$ and then the $J$-properness holds for $\varphi_{t}-\varphi_{1}$, and there exist $\delta, C_{1}, C_{2}>0$ such that
$$\begin{aligned}
\mathcal{F}_{\omega_{K E}, \beta}\left(\varphi_{t}-\varphi_{1}\right) & \geq \delta J_{\omega_{K E}}\left(\varphi_{t}-\varphi_{1}\right)-C_{1} \\
& \geq \frac{\delta}{n+1} \operatorname{osc}_{X}\left(\varphi_{t}-\varphi_{1}\right)-C_{2} .
\end{aligned}$$
Consequently, there exist $C_{3}>0$ such that
$$\begin{aligned}
n(1-t) J_{\omega_{K E}}(\varphi) & \geq(1-t) J_{\omega^{\prime}}\left(\varphi_{1}\right) \\
& \geq(1-t)\left(I_{\omega^{\prime}}\left(\varphi_{1}\right)-J_{\omega^{\prime}}\left(\varphi_{1}\right)\right) \\
& \geq \int_{t}^{1}\left(I_{\omega^{\prime}}\left(\varphi_{s}\right)-J_{\omega^{\prime}}\left(\varphi_{s}\right)\right) d s \\
& =\mathcal{F}_{\omega^{\prime}, \beta}\left(\varphi_{t}\right)-\mathcal{F}_{\omega^{\prime}, \beta}\left(\varphi_{1}\right) \\
& =\mathcal{F}_{\omega_{K E}, \beta}\left(\varphi_{t}-\varphi_{1}\right) \\
& \geq\left(\frac{\alpha}{\beta}-\frac{n}{n+1}\right) \operatorname{osc}_{X}\left(\varphi_{t}-\varphi_{1}\right)-C_{3}
\end{aligned}$$
The third inequality follows by the increasing monotonicity for $\left(I_{\omega^{\prime}}-J_{\omega^{\prime}}\right)\left(\varphi_{t}\right)$ for $t \in[0,1]$. Then by applying the cocycle condition and the same argument in the
smooth case in [44, 47], we have
$$\begin{aligned}
\mathcal{F}_{\omega_{K E}, \beta}(\varphi) & =-\mathcal{F}_{\omega^{\prime}, \beta}\left(\varphi_{1}\right) \\
& =\int_{0}^{1}\left(I_{\omega^{\prime}}\left(\varphi_{t}\right)-J_{\omega^{\prime}}\left(\varphi_{t}\right)\right) d t \\
& \geq(1-t)\left(I_{\omega^{\prime}}\left(\varphi_{t}\right)-J_{\omega^{\prime}}\left(\varphi_{t}\right)\right) \\
& \geq \frac{1-t}{n} J_{\omega^{\prime}}\left(\varphi_{t}\right) \\
& \geq \frac{1-t}{n} J_{\omega^{\prime}}\left(\varphi_{1}\right)-\frac{2(1-t)}{n} \operatorname{osc}_{X}\left(\varphi_{t}-\varphi_{1}\right)-C_{4} \\
& \geq \frac{1-t}{n^{2}} J_{\omega_{K E}}(\varphi)-C_{5}(1-t)^{2} J_{\omega_{K E}}(\varphi)-C_{6}
\end{aligned}$$

Since $C_{5}$ and $C_{6}$ are independent of the choice for $t \geq 1 / 2$, by choosing $t$ sufficiently close to 1 , we can find $\epsilon^{\prime}, C_{\epsilon^{\prime}}>0$, such that
$$\mathcal{F}_{\omega_{K E}, \beta}(\varphi) \geq \epsilon^{\prime} J_{\omega, \beta}(\varphi)-C_{\epsilon^{\prime}}$$
for all $\varphi \in P S H\left(X, \omega_{K E}\right)$ such that $\omega_{\varphi}$ is a smooth conical Kähler metric with cone angle $2 \pi\left(1-\frac{1-\beta}{m}\right)$ along $D$. The set of such $\varphi$ is dense in $P S H\left(X, \omega_{K E}\right) \cap L^{\infty}(X)$ and so the $J$-properness holds for $P S H\left(X, \omega_{K E}\right) \cap L^{\infty}(X)$.

Step 3. Finally, the $J$-properness for any $\omega$ follows from Lemma 2.1 and the fact the Green's function for $\omega_{K E}$ is bounded from below. \(\square\)
2.4. An interpolation formula. In this section, we will prove the following interpolation formula for the $F$-functional to obtain $J$-properness.

Proposition 2.2. Let $X$ be a Fano manifold and $D$ a smooth simple divisor in $\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$. Let $\omega$ be a smooth Kähler metric in $c_{1}(X)$. If there exists $\alpha \in(0,1]$ such that
$$\inf _{P S H(X, \omega) \cap L^{\infty}(X)} \mathcal{F}_{\omega, \alpha}(\cdot)>-\infty$$
then $\mathcal{F}_{\omega, \beta}(\varphi)$ is $J$-proper on $\operatorname{PSH}(X, \omega) \cap L^{\infty}(X)$ for all $\beta \in(0, \alpha)$.
Proof. We want to show that
$$\mathcal{F}_{\omega, \beta}(\varphi)=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\beta} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \Omega_{\omega}\right)^{\beta}\left(\Omega_{D}\right)^{1-\beta}$$
is $J$-proper for all $\beta \in(0, \alpha)$.

First for $0<\tau<\beta<\alpha$, we write $\beta=\tau / p+\alpha / q$ for some $1 / p+1 / q=1$. Then Hölder inequality implies the interpolation
$$\begin{aligned}
\mathcal{F}_{\omega, \beta}(\varphi) & =J_{\omega}(\varphi)-\frac{1}{\beta} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \Omega_{\omega}\right)^{\beta} \Omega_{D}^{1-\beta} \\
& =\left(\frac{\tau}{\beta p}+\frac{\alpha}{\beta q}\right) J_{\omega}(\varphi)-\frac{1}{\beta} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \frac{\Omega_{\omega}}{\Omega_{D}}\right)^{\tau / p+\alpha / q} \cdot \Omega_{D} \\
& \geq \frac{\tau}{\beta p}\left(J_{\omega}(\varphi)-\frac{1}{\tau} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \Omega_{\omega}\right)^{\tau} \Omega_{D}^{1-\tau}\right)+\frac{\alpha}{\beta q}\left(J_{\omega}(\varphi)-\frac{1}{\alpha} \log \frac{1}{V} \int_{X}\left(e^{-\varphi} \Omega_{\omega}\right)^{\tau} \Omega_{D}^{1-\tau}\right) \\
& =\frac{\tau}{\beta p} \cdot \mathcal{F}_{\omega, \tau}(\varphi)+\frac{\alpha}{\beta q} \cdot \mathcal{F}_{\omega, \alpha}(\varphi) \\
& \geq \frac{\tau}{\beta p} \cdot \mathcal{F}_{\omega, \tau}(\varphi)-C_{1} \\
& \geq \epsilon J_{\omega}(\varphi)-C
\end{aligned}$$
The last inequality follows from Theorem 2.3 by choosing $\tau$ sufficiently small so that $\alpha_{D, \tau}>$ $n /(n+1)$. \(\square\)

The same argument in the proof of Proposition 2.2 can be applied to prove the following lemma after replacing $m^{-1}[D]$ by a smooth Kähler metric $\theta \in c_{1}(X)$.

Lemma 2.4. Let $X$ be a Fano manifold and $\theta$ be a smooth Kähler metric in $c_{1}(X)$. Let $\omega$ be a smooth Kähler metric in $c_{1}(X)$. If there exists $\alpha \in(0,1]$ such that
$$F_{\omega, \alpha}(\varphi)=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\alpha} \log \frac{1}{V} \int_{X} e^{-\alpha \varphi}\left(\Omega_{\omega}\right)^{1-\alpha}\left(\Omega_{\theta}\right)^{1-\alpha}$$
is bounded below on $P S H(X, \omega) \cap L^{\infty}(X)$, then $F_{\omega, \beta}(\varphi)$ is $J$-proper on $P S H(X, \omega) \cap L^{\infty}(X)$ for all $\beta \in(0, \alpha)$.

We remark that Lemma 2.4 also serves as an alternative proof for Theorem 1.1 in [40] relating $R(X)$ and the continuity method.
2.5. Proof of Theorem 1.1. Let us prove the first part of Theorem 1.1.

Proposition 2.3. Let $X$ be a Fano manifold and $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$. If there exist $\beta \in(0,1]$ and a smooth conical Kähler-Einstein metric $\omega$ satisfying
$$\operatorname{Ric}(\omega)=\beta \omega+\frac{1-\beta}{m}[D],$$
then
$$\beta \leq R(X) .$$
In particular, the inequality holds if and only if $\beta=1$.
Proof. Let $\omega_{K E}$ be a smooth conical Kähler-Einstein metric on $X$ satisfying $\operatorname{Ric}\left(\omega_{K E}\right)=$ $\beta \omega_{K E}+\frac{1-\beta}{m}[D]$. By Proposition 2.1, we know that $\mathcal{F}_{\omega_{K E}, \beta}$ is bounded below. By Proposition 2.2. $\mathcal{F}_{\omega, \beta^{\prime}}$ is $J$-proper for all $\beta^{\prime} \in(0, \beta)$.

Let $\omega, \theta \in c_{1}(X)$ be two smooth Kähler metrics on $X$. The $J$-properness of $\mathcal{F}_{\omega, \beta^{\prime}}$ immediately implies the $J$-properness for
$$F_{\omega, \theta, \beta^{\prime}}(\varphi)=J_{\omega}(\varphi)-\frac{1}{v} \int_{X} \varphi \omega^{n}-\frac{1}{\beta^{\prime}} \log \frac{1}{V} \int_{X} e^{-\beta^{\prime} \varphi}\left(\Omega_{\omega}\right)^{\beta^{\prime}}\left(\Omega_{\theta}\right)^{1-\beta^{\prime}}$$
because $\Omega_{D}$ is strictly bounded below from 0 . Then by Lemma 2.3, there exists a minimizer of $F_{\omega, \theta, \beta^{\prime}}$ which soloves the equaiton
$$\operatorname{Ric}(\omega)=\beta^{\prime} \omega+\left(1-\beta^{\prime}\right) \theta \geq \beta^{\prime} \omega .$$
This shows that $R(X) \geq \beta^{\prime}$ and so $R(X) \geq \beta$.
If $\beta=R(X)<1$, there must exist $\epsilon>0$ and a smooth conical Kähler-Einstein metric $g$ such that $\operatorname{Ric}(g)=(\beta+\epsilon) g+(1-\beta-\epsilon) m^{-1}[D]$ by Corollary 2.1. Then it is a contradiction to the definition of $R(X)$ by repeating the previous argument. \(\square\)

We now prove the second part of Theorem 1.1.
Proposition 2.4. Let $X$ be a Fano manifold. Then for any $\beta \in(0, R(X))$, there exist a smooth simple divisor $D \in\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$and a smooth conical Kähler-Einstein metric $g$ satisfying
$$\operatorname{Ric}(\omega)=\beta \omega+\frac{1-\beta}{m}[D] .$$

Proof. We break the proof into the following steps.
Step 1. Let $\omega$ and $\theta$ be two smooth Kähler metrics in $c_{1}(X)$. For any $\beta \in(0, R(X))$, by Szeklyhidi's result [40], the following family of Monge-Ampère equation
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=\left(e^{-t \varphi} \Omega_{\omega}\right)^{\beta}\left(\Omega_{\theta}\right)^{1-\beta}, \int_{X}\left(\Omega_{\omega}\right)^{\beta}\left(\Omega_{\theta}\right)^{1-\beta}=V$$
is solvable for all $t \in[0,1]$. Then by Lemma 2.3,
$$F_{\omega, \beta}(\varphi)=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\beta} \log \int_{X} e^{-\beta \varphi}\left(\Omega_{\omega}\right)^{\beta}\left(\Omega_{\theta}\right)^{1-\beta}$$
is bounded below on $P S H(X, \omega) \cap L^{\infty}(X)$. By Lemma 2.4, for any $\beta^{\prime} \in(0, \beta)$, $F_{\omega, \beta^{\prime}}(\varphi)$ is $J$-proper. It immediately follows that for any $\beta \in(0, R(X))$, there exist $\epsilon, C_{\epsilon}>0$ such that for all $\varphi \in P S H(X, \omega) \cap L^{\infty}(X)$,
$$\int_{X} e^{-\beta \varphi} \omega^{n} \leq C_{\epsilon} e^{(\beta-\epsilon) J_{\omega}(\varphi)-\frac{\beta}{V} \int_{X} \varphi \omega^{n}} .$$

Step 2. Let $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$. We will later choose $m$ sufficiently large. Let $s$ be a defining section of $D$ and $h$ be a smooth hermitian metric on $-m K_{X}$. For any $\beta \in(0, R(X))$, there exists $\delta>0$ such that $\beta+\delta<R(X)$. Then
$$\begin{aligned}
\int_{X}|s|_{h}^{-\frac{2(1-\beta)}{m}} e^{-\beta \varphi} \omega^{n} & \leq\left(\int_{X} e^{-(\beta+\delta) \varphi} \omega^{n}\right)^{\frac{\beta}{\beta+\delta}}\left(\int_{X}|s|_{h}^{-\frac{2(1-\beta)(\beta+\delta)}{m \delta}} \omega^{n}\right)^{\frac{\delta}{\beta+\delta}} \\
& \leq C_{\delta}\left(\int_{X} e^{-(\beta+\delta) \varphi} \omega^{n}\right)^{\frac{\alpha}{\alpha+\delta}}
\end{aligned}$$
if we choose $m>\frac{\delta}{(1-\beta)(\beta+\delta)}$. By the conclusion in Step 1, there exist $\epsilon, C_{\epsilon}>0$ such that
$$\int_{X}|s|^{-\frac{2(1-\beta)}{m}} e^{-\beta \varphi} \omega^{n} \leq C_{\epsilon} e^{(\beta-\epsilon) J_{\omega}(\varphi)-\frac{\beta}{V} \int_{X} \varphi \omega^{n}} .$$
Equivalently, $\mathcal{F}_{\omega, \beta}(\varphi)$ is $J$-proper on $P S H(X, \omega) \cap L^{\infty}(X)$. By Proposition 2.1, there exists a unique smooth conical Kähler-Einstein metric $\omega_{\beta}$ solving
$$\operatorname{Ric}\left(\omega_{\beta}\right)=\beta \omega_{\beta}+\frac{1-\beta}{m}[D] .$$ \(\square\)

Now we can relate the optimal Moser-Tridinger constant to the invariant $R(X)$.
Corollary 2.2. Let $X$ be a Fano manifold and $\omega \in c_{1}(X)$ be a smooth Kähler metric.
\begin{itemize}
\item[(1)] If $\beta \in(0, R(X)), F_{\omega, \beta}$ is J-proper on $P S H(X, \omega) \cap L^{\infty}(X)$. Equivalently, there exist $\epsilon, C_{\epsilon}>0$ such that the following Moser-Trudinger inequality holds for all $\varphi \in P S H(X, \omega) \cap L^{\infty}(X)$
$$\int_{X} e^{-\beta \varphi} \omega^{n} \leq C_{\epsilon} e^{(\beta-\epsilon) J_{\omega}(\varphi)-\frac{\beta}{V} \int_{X} \varphi \omega^{n}} .$$
\item[(2)] If $\beta \in(R(X), 1)$, then
$$\inf _{P S H(X, \omega) \cap L^{\infty}(X)} F_{\omega, \beta}(\cdot)=-\infty .$$
\end{itemize}

Proof. For $\beta \in(0, R(X))$ and a fixed smooth Kähler metric $\theta \in c_{1}(X)$, there exists a smooth Kähler metric $\omega$ satisfying $\operatorname{Ric}(\omega)=\beta \omega+(1-\beta) \theta$. The corollary is an immediate consequence of by modifying the interpolation formula in Proposition 2.2, after replacing $m^{-1}[D]$ by $\theta$. \(\square\)

Immediately, we can show that $R(X)$ and $\mathfrak{m t}(X)$ take the same value for a Fano manifold $X$.

Corollary 2.3. Let $X$ be a Fano manifold. Then
$$\mathfrak{m t}(X)=R(X)=\sup \left\{\beta \in(0,1) \mid F_{\omega, \beta} \text { is } J \text {-proper on } P S H(X, \omega) \cap L^{\infty}(X)\right\},$$
where $\omega \in c_{1}(X)$ is a smooth Kähler metric.
2.6. Proof of Theorem 1.2. Before proving Theorem 1.2, we first quote the following proposition establishing the equivalence for the Mabuchi $K$-energy and the $F$-functional when either of them is bounded below proved in [25] by applying the Kähler-Ricci flow and Perelman's estimates for the scalar curvature.

Proposition 2.5. Let $X$ be a Fano manifold and $\omega \in c_{1}(X)$ be a smooth Kähler metric. Then Ding's functional $F_{\omega}$ is bounded below on $P S H(X, \omega) \cap C^{\infty}(X)$ if and only if the Mabuchi $K$-energy is bounded below.

Proposition 2.5 holds for the paired Mabuchi $K$-energy and the paired $F$-functional as shown in [5]. One can also apply the continuity method for the conical Kähler metrics with positive Ricci curvature as in [34]. Let $P S H(X, \omega) \cap C_{D, \beta}^{\infty}(X)$ be the set of all bounded $\varphi$ such that $\omega+\sqrt{-1} \partial \bar{\partial} \varphi$ is a smooth conical Kähler metric with cone angle $2 \pi \beta$ along $D$.

Proposition 2.6. Let $X$ be a Fano manifold and $D \in\left|-m K_{X}\right|$ be a smooth simple divisor. Let $\omega$ be a smooth conical Kähler metric in $c_{1}(X)$ with cone angle $2 \pi(1-\beta) / m$ along $D$. Then
$$\inf _{\operatorname{PSH}(X, \omega) \cap C_{D, \frac{1-\beta}{m}}^{\infty}(X)} \mathcal{M}_{\omega, \beta}(\cdot)>-\infty$$
is equivalent to
$$\inf _{P S H(X, \omega) \cap L^{\infty}(X)} \mathcal{F}_{\omega, \beta}(\cdot)>t-\infty .$$

We can now prove Theorem 1.2.
Theorem 2.4. Let $X$ be a Fano manifold and $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$. If the paired Mabuchi $K$-energy $\mathcal{M}_{\omega, R(X)}$ on $X$ is bounded below, then for any $\beta \in(0, R(X))$ there exists a smooth conical Kähler-Einstein metric satisfying
$$\operatorname{Ric}(g)=\beta g+\frac{1-\beta}{m}[D] .$$
Proof. Let $\omega \in c_{1}(X)$ be a smooth Kähler metric. Then by Proposition 2.6, $\mathcal{F}_{\omega, R(X)}(\varphi)$ is bounded below on $P S H(X, \omega) \cap L^{\infty}(X)$. Applying the interpolation formula in Proposition 2.2. $\mathcal{F}_{\omega, \beta}$ is $J$-proper on $P S H(X, \omega) \cap L^{\infty}(X)$ for all $\beta \in(0, R(X))$. The theorem follows by Proposition 2.1. \(\square\)

When the Mabuchi $K$-energy is bounded below on $X$, for any $\beta \in(0,1)$, there exists a conical Kähler-Einstein metric satisfying equation (2.23) for $m=1$. In this case, $D$ is a smooth Calabi-Yau hypersurface of $X$. If we only assume $R(X)=1$, we have the same conclusion in Theorem 2.4 for the linear systems $\left|-m K_{X}\right|$ with $m \geq 2$.

Proposition 2.7. Let $X$ be a Fano manifold and $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$ for some $m \geq 2$. Then for any $\beta \in\left(0, \frac{(m-1) \cdot R(X)}{m-R(X)}\right)$, there exists a smooth conical Kähler-Einstein metric $\omega$ satisfying
$$\operatorname{Ric}(\omega)=\beta \omega+\frac{1-\beta}{m}[D] .$$
In particular, when $R(X)=1$, we have conical Kähler-Einstein metric for any $\beta \in(0,1)$.
Proof. We prove the case for $R(X)=1$ and the general case follows from the same argument. Let $s$ be the defining section of $\left|-m K_{X}\right|$ and $h$ be a smooth hermitian metric of $-m K_{X}$. Then $|s|_{h}^{-(2-\epsilon)}$ is integrable for any $\epsilon>0$. Furthermore, $F_{\omega,(1-\beta) m^{-1}[D], \beta}$ is proper for any smooth Kähler forms $\omega, \theta \in c_{1}(X)$ if $\beta \in(0,1)$, Then the proposition can be proved by similar interpolation argument in the proof of Theorem 2.4. \(\square\)

\section*{3. Conical toric Käher-Einstein metrics}
3.1. Conical toric Kähler metrics. In this section, we will introduce toric conical Kähler metrics on toric Kähler manifolds and corresponding toric Kähler and symplectic potentials as in [12, 13]. We begin with some basic definitions for toric manifolds.

Definition 3.1. A convex polytope $P$ in $\mathbb{R}^{n}$ is called a Delzant polytope if a neighborhood of any vertex of $P$ is $S L(n, \mathbb{Z})$ equivalent to $\left\{x_{j} \geq 0, j=1, \ldots, n\right\} \subset \mathbb{R}^{n} . P$ is called an integral Delzant polytope if each vertex of $P$ is a lattice point in $\mathbb{Z}^{n}$.

Let $P$ be an integral Delzant polytope in $\mathbb{R}^{n}$ defined by
$$P=\left\{x \in \mathbb{R}^{n} \mid l_{j}(x)>0, j=1, \ldots, N\right\},$$
where
$$l_{j}(x)=v_{j} \cdot x+\lambda_{j}$$
and $v_{i}$ a primitive integral vector in $\mathbb{Z}^{n}$ and $\lambda_{j} \in \mathbb{Z}$ for all $j=1, \ldots, N$. Then $P$ defines an $n$-dimensional nonsingular toric variety by the following observation.

For each $n$-dimensional integral Delzant polytope $P$, as in [12, 13], we consider the set of pairs $\left\{p, v_{p, i}\right\}$, where $p$ is a vertex of $P$ and the neighboring faces are given by $l_{p, i}(x)=v_{p, i} \cdot x-\lambda_{p, i}>0$ for $i=1, \ldots, n$. For each $p$, we choose a coordinate chart $\mathbb{C}^{n}$ with $z=\left(z_{1}, \ldots, z_{n}\right)$. Then for any two vertices $p$ and $p^{\prime}$, there exists $\sigma_{p, p^{\prime}} \in G L(n, \mathbb{Z})$ such that
$$\sigma_{p, p^{\prime}} \cdot v_{p, i}=v_{p^{\prime}, i} .$$
Furthermore, we have
$$\sigma_{p, p^{\prime}} \cdot \sigma_{p^{\prime}, p^{\prime \prime}} \cdot \sigma_{p^{\prime \prime}, p}=1 .$$
Therefore $\sigma_{p, p^{\prime}}$ serves as the transition function for two coordinate charts over $\left(\mathbb{C}^{*}\right)^{n}$.
More precisely, let $z=\left(z_{1}, \ldots, z_{n}\right)$ and $z^{\prime}=\left(z_{1}^{\prime}, \ldots, z_{n}^{\prime}\right) \in \mathbb{C}^{n}$ be the coordinates for the chart associated to $p$ and $p^{\prime}$ respectively. Suppose $\sigma_{p, p^{\prime}}=\left(\alpha_{i j}\right)$. Then
$$z_{i}^{\prime}=\prod_{j} z_{j}^{\alpha_{i j}} .$$
Each integral Delzant polytope uniquely determines a nonsingular toric variety $X_{P}$ by such a construction with the data $\left(p,\left\{v_{p, i}\right\}_{i=1}^{n}\right)$. The constant $\lambda_{p, i}$ determines an ample line bundle $L$ over $X_{P}$, and moreover,
$$H^{0}\left(X_{P}, L\right)=\operatorname{span}\left\{z^{\alpha}\right\}_{\alpha \in \mathbb{Z}^{n} \cap \bar{P}} .$$

Let $\varphi_{P}=\log \left(\sum_{\alpha \in \mathbb{Z}^{n} \cap \bar{P}}|z|^{2 \alpha}\right)$. Then $\omega_{P}=\sqrt{-1} \partial \bar{\partial} \varphi_{P}$ is a smooth Kähler metric on $\left(\mathbb{C}^{*}\right)^{n}$ and it can be smoothly extended to a smooth global toric Kähler metric on $X_{P}$ in $c_{1}(L)$. Then the space of toric Kähler metrics in $c_{1}(L)$ is equivalent to the set of all smooth plurisubharmonic function $\varphi$ on $\left(\mathbb{C}^{*}\right)^{n}$ such that $\varphi-\varphi_{P}$ is bounded and $\sqrt{-1} \partial \bar{\partial} \varphi$ extends to a smooth Kähler metric on $X_{P}$. If we consider the toric Kähler potential $\varphi$ which is invariant under the real torus action, we can view $\varphi$ as a function in $\mathbb{R}^{n}$ by
$$\varphi=\varphi(\rho), \rho=\left(\rho_{1}, \ldots, \rho_{n}\right), \rho_{i}=\log \left|z_{i}\right|^{2} .$$
One can also define a symplectic potential $u$ on $P$ by
$$u(x)=\sum_{j=1}^{N} l_{j}(x) \log l_{j}(x)+f(x)$$
such that $f(x) \in C^{\infty}(\bar{P})$ and $u(x)$ is strictly convex in $P$. It is due to Guillemin [17] that the toric Kähler potential and the symplectic potential are related by the Legendre transform
$$\varphi(\rho)=\mathcal{L} u(\rho)=\sup _{x \in P}(x \cdot \rho-u(x)), u(x)=\mathcal{L} \varphi(x)=\sup _{\rho \in \mathbb{R}^{n}}(x \cdot \rho-\varphi(\rho))$$
or equivalently
$$\varphi(\rho)=x \cdot \rho-u(x), u(x)=x \cdot \rho-\varphi(\rho), x=\nabla_{\rho} \varphi(\rho), \rho=\nabla_{x} u(x) .$$

Now we would like to generalize the Guillemin condition to toric conical Kähler metrics on $X_{P}$. This can be considered as a generalization of orbifold Kähler metrics by replacing the finite subgroup by possibly infinite non-discrete subgroup of $\left(S^{1}\right)^{n}$. Suppose that the integral Delzant polytope is defined by
$$P=\left\{x \in \mathbb{R}^{n} \mid l_{j}(x)=v_{j} \cdot x+\lambda_{j}>0, j=1, \ldots, N\right\}$$
with $v_{j} \in \mathbb{Z}^{n}$ being a primitive lattice point and $\lambda_{j} \in \mathbb{Z}$.
On each coordinate chart determined by the pair $\left(p,\left\{v_{p, i}\right\}_{i=1}^{n}\right)$ associated to a vertex of $P$, we let $z=\left(z_{1}, \ldots, z_{n}\right)$ be the coordinates on $\mathbb{Z}^{n} .\left\{z_{i}=0\right\}$ extends to a smooth toric divisor of $X_{P}$. Let $D$ be a toric divisor of $X_{P}$ and suppose $D$ restricted to this coordinate chart is given by
$$\sum_{i=1}^{n} a_{i}\left[z_{i}=0\right] .$$
For any function $f(z)$ invariant under the $\left(S^{1}\right)^{n}$-action, we can lift it to a function
$$\tilde{f}(w)=f(z)$$
by letting
$$\left|w_{i}\right|=\left|z_{i}\right|^{1 / \beta_{i}}, w=\left(w_{1}, \ldots, w_{n}\right) \in \mathbb{C}^{n},$$
and clearly $\tilde{f}(w)$ is also $\left(S^{1}\right)^{n}$-invariant. $w \in \mathbb{C}^{n}$ is then a $\beta$-covering of $z \in \mathbb{C}^{n}$. Then we can consider the $\left(S^{1}\right)^{n}$-invariant function space for $k \in \mathbb{Z}^{\geq 0}$ and $\alpha \in[0,1]$
$$C_{\beta, p}^{k, \alpha}=\left\{f(z)=f\left(\left|z_{1}\right|, \ldots,\left|z_{n}\right|\right) \mid \tilde{f}(w) \in C^{k, \alpha}\left(\mathbb{C}^{n}\right)\right\} .$$
This in turn defines the weighted function space
$$C_{\beta}^{k, \alpha}\left(X_{P}\right), \beta=\left(\beta_{1}, \ldots, \beta_{N}\right) \in\left(\mathbb{R}^{+}\right)^{N}$$
whose restriction on each chart belongs to $C_{\beta}^{k, \alpha}$ with respect to the weight $\beta$ and $\beta_{j}$ corresponding to the divisor induced by $l_{j}(x)=0$. Then we can define the space of weighted toric Kähler metrics on $X_{P}$ by considering a Kähler current $\omega$ whose restriction on each chart is given by
$$\omega=\sqrt{-1} \partial \bar{\partial} \varphi_{p}$$
such that $\varphi_{p} \in C_{\beta, p}^{\infty}$. Such a weighted toric Kähler metric is naturally a smooth conical Kähler metric with cone angle $2 \pi \beta_{i}$ along $\left[z_{i}=0\right]$ and is called a smooth $\beta$-weighted Kähler metric. The local lifting $\tilde{\varphi}(w)$ is a smooth plurisubharmonic function on the lifting space $w \in \mathbb{C}^{n}$.

We can also define the space of weighted toric Kähler potential $\varphi$ on $\left(\mathbb{C}^{*}\right)^{n}$ such that $\varphi-\varphi_{P}$ is bounded and $\sqrt{-1} \partial \bar{\partial} \varphi$ extends to a smooth weighted Kähler metric on $X_{P}$.

We now define a weighted $C_{\beta}^{\infty}$ symplectic potential
$$u(x)=\sum_{j=1}^{N} \beta_{j}^{-1} l_{j}(x) \log l_{j}(x)+f(x)$$
for $f \in C^{\infty}(\bar{P})$ for $j=1, \ldots, n$ such that $f \in C^{\infty}(\bar{P})$ and $u$ is strictly convex in $P$. Then the weighted Kähler potentials and the weighted symplectic potential determine each other
uniquely. The following is a straightforward generalization of the Guillemin condition for conical toric Kähler metrics.

Proposition 3.1. The weighted $C_{\beta}^{\infty}$ toric potential $\varphi$ and the weighted $C_{\beta}^{\infty}$ symplectic potential are related by the Legendre transform
$$\varphi(\rho)=\mathcal{L} u(\rho)=\sup _{x \in P}(x \cdot \rho-u(x)), u(x)=\mathcal{L} \varphi(x)=\sup _{\rho \in \mathbb{R}^{n}}(x \cdot \rho-\varphi(\rho))$$
or equivalently
$$\varphi(\rho)=x \cdot \rho-u(x) \text { with } x=\nabla_{\rho} \varphi(\rho) \text { and } u(x)=x \cdot \rho-\varphi(\rho) \text { with } \rho=\nabla_{x} u(x) \text {. }$$

In particular, if $u(x)=\beta_{j}^{-1} l_{j}(x) \log l_{j}(x)+f(x)$, then the cone angle of the corresponding conical toric Kähler metric is $2 \pi \beta_{j}$ along the toric divisor determined by $l_{j}(x)=0$.

Let $\omega=\sqrt{-1} \partial \bar{\partial} \phi$ be a smooth $\beta$-weighted Kähler metric and let $u=\mathcal{L} \phi$. Then $u(x)=$ $\sum_{j} \beta_{j}^{-1} l_{j}(x) \log l_{j}(x)+f(x)$ for some $f \in C^{\infty}(\bar{P})$.

Example 3.1. Let $P=[0,1]$ then the associated toric manifold is $X=\mathbb{P}^{1}$ with the polarization $\mathcal{O}(1)$. We consider the symplectic potential by
$$u=\left(\beta_{1}\right)^{-1} x \log x+\beta_{2}^{-1}(1-x) \log (1-x) .$$
Then
$$\rho=\log |z|^{2}=u^{\prime}(x)=\left(\beta_{1}^{-1}-\beta_{2}^{-1}\right)+\log \frac{x^{\beta_{1}^{-1}}}{(1-x)^{\beta_{2}^{-1}}}, \text { or }|z|^{2}=\frac{x^{\beta_{1}^{-1}}}{(1-x)^{\beta_{2}^{-1}}} e^{\beta_{1}^{-1}-\beta_{2}^{-1}}$$
and so
$$x \sim|z|^{2 \beta_{1}} \text { near } 0,(1-x) \sim|z|^{-2 \beta_{2}} \text { near } \infty .$$
In particular, $x$ is a smooth function in $|z|^{2 \beta_{1}}$ near $z=0$ and $(1-x)$ is a smooth function in $|z|^{-2 \beta_{2}}$ near $z=\infty$. The Kähler potential $\varphi$ is given by
$$\varphi(\rho)=x\left(\beta_{1}^{-1}-\beta_{2}^{-1}\right)-\beta_{2}^{-1} \log (1-x) .$$
Hence $\sqrt{-1} \partial \bar{\partial} \varphi$ extends to a conical metric with cone angle $2 \pi \beta_{1}$ and $2 \pi \beta_{2}$ at $[z=0]$ and $[z=\infty]$ respectively. When $\beta=\beta_{1}=\beta_{2}, \varphi=\beta^{-1} \log \left(1+|z|^{2 \beta}\right)$ and the $\omega=2 \sqrt{-1} \partial \bar{\partial} \varphi$ is a smooth conical Kähler-Einstein metric in $c_{1}\left(\mathbb{P}^{1}\right)$ satisfying
$$\operatorname{Ric}(\omega)=\beta \omega+(1-\beta)([z=0]+[z=\infty]) .$$

Lemma 3.1. Let $g$ be a smooth $\beta$-weighted toric Kähler metric on a toric manifold $X_{P}$. Let $D$ be the toric divisor such that $g$ is a smooth toric Kähler metric on $X \backslash D$. Then for any $k \geq 0$, there exists $C_{k}>0$ such that for any point $p \in X \backslash D$,
$$\left|\nabla_{g}^{k} R m(g)\right|_{g}(p) \leq C_{k} .$$

Proof. The calculation of $\left|\nabla_{g}^{k} R m(g)\right|_{g}(p)$ can be locally carried out on the $\beta$-covering space for each coordinate chart $\left(p,\left\{v_{i}\right\}_{i=1}^{n}\right)$ as in the orbifold case. All the quantities must be bounded because the $g$ is a smooth toric Kähler metric after being lifted on the covering space. \(\square\)

We now can solve a Monge-Ampère equation with smooth $\beta$-weighted data.

Proposition 3.2. Let $\omega$ be a smooth $\beta$-weighted toric Kähler metric on a toric manifold $X_{P}$. Then for any smooth $\beta$-weighted function $f$ on $X_{P}$ with $\int_{X_{P}} e^{-f} \omega^{n}=\int_{X_{P}} \omega^{n}$, there exists a unique $\beta$-weighted smooth function $\varphi$ satisfying
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{f} \omega^{n}, \sup _{X_{P}} \varphi=0$$
Proof. We consider the following continuity method for $t \in[0,1]$
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=e^{t f+c_{t}} \omega^{n},$$
where $c_{t}$ is determined by $\int_{X_{P}} e^{t f+c_{t}} \omega^{n}=\int_{X_{P}} \omega^{n}$. Let
$$S=\left\{t \in[0,1] \mid \text { (3.28) is solvable for } t \text { with } \varphi_{t} \in C_{\beta}^{\infty}\left(X_{P}\right)\right\} \text {. }$$
Obviously, $0 \in S$. $S$ is open by applying the implicit function theorem for the linearized operator
$$\Delta_{\beta, t}: C_{\beta}^{k+2, \alpha}\left(X_{P}\right) \rightarrow C_{\beta}^{k, \alpha}\left(X_{P}\right) .$$
All the local calculation can be carried out in the $\beta$-covering space on each coordinate chart $\left(p,\left\{v_{i}\right\}_{i=1}^{n}\right)$ because all the data involved are invariant under $\left(S^{1}\right)^{n}$-action. It suffices to prove uniform a priori estimates for $\varphi_{t}$ in $C_{\beta}^{k}\left(X_{P}\right)$ for $t \in[0,1]$.
$C^{0}$-estimates. Let $\Omega$ be a smooth volume form on $X_{P}$. Then $\frac{e^{t f+c_{t} \omega^{n}}}{\Omega}$ lies in $L^{1+\epsilon}\left(X_{P}, \Omega\right)$ for some $\epsilon>0$. By Yau's Moser iteration [51] adapted to the conical case or by Kolodziej's $L^{\infty}$-estimate [20], there exists $C>0$ such that for all $t \in[0,1]$, if $\varphi_{t} \in C_{\beta}^{\infty}(X)$ solves (3.28),
$$\left\|\varphi_{t}\right\|_{L^{\infty}\left(X_{P}\right)} \leq C .$$
Second order estimates. We consider
$$H_{t}=\log t r_{\omega}\left(\omega_{t}\right)-A \varphi_{t} .$$
Suppose at $t \in[0,1], \sup _{X_{P}} H_{t}=H_{t}(q)$. We lift all the calculation on the $\left(S^{1}\right)^{n}$-invariant $\beta$-covering space in a fixed local coordinate chart $w \in \mathbb{C}^{n}$. Standard calculations show that near $\tilde{q}$, there exists $C>0$ such that
$$\begin{aligned}
\tilde{\Delta}_{t, \beta} \tilde{H}_{t} & \geq-\operatorname{Ctr}_{\tilde{\omega}_{t}}(\tilde{\omega})-A n+A \operatorname{tr}_{\tilde{\omega}_{t}}(\tilde{\omega}) \\
& \geq \frac{A}{2} \operatorname{tr}_{\tilde{\omega}_{t}}(\tilde{\omega})-C,
\end{aligned}$$
where $\tilde{q}, \tilde{\omega}$ and $\tilde{\omega}_{t}$ are the lifting of $q, \omega$ and $\omega_{t}$. By the maximum principle, at $\tilde{q}, t r_{\tilde{\omega}_{t}}(\tilde{\omega})$ is bounded above by a constant independent of $t \in[0,1]$. Combining the equation (3.27), $\operatorname{tr}_{\tilde{\omega}}\left(\tilde{\omega}_{t}\right)$ is also bounded above by a constant independent of $t$. Hence there exists $C>0$ such that for for all $t \in[0,1]$, if $\varphi_{t} \in C_{\beta}^{\infty}(X)$ solves (3.28),
$$C^{-1} \omega \leq \omega_{t} \leq C \omega .$$
Higher order estimates. Calabi's third order estimates can be applied the way as in [51, 32] by the maximum principle after lifting all the local calculations on the $\left(S^{1}\right)^{n}$-invariant covering space. The Schauder estimates can also be applied by the bootstrap argument. Eventually, for any $k>0$, there exists $C_{k}$ such that for all $t \in[0,1]$, if $\varphi_{t} \in C_{\beta}^{\infty}(X)$ solves (3.28),
$$\left\|\varphi_{t}\right\|_{C_{\beta}^{k}\left(X_{P}\right)} \leq C_{k} .$$ \(\square\)
3.2. Proof of Theorem 1.3. An $n$-dimensional integral polytope $P$ is called a Fano polytope if it is a Delzant polytope and $\lambda_{i}=1$ for each defining function $l_{i}(x)=v_{i} \cdot x+\lambda_{i}$. Immediately, we have $0 \in P$. The toric manifold $X_{P}$ associated to $P$ is a Fano manifold. Each $(n-1)$-face of $P$ corresponds to a toric divisor of $P$. Then the union $D_{P}=\sum_{j} D_{j}$ for all the boundary divisors lies in $c_{1}(X)=c_{1}\left(-K_{X}\right)$, where $D_{j}$ is the toric divisor induced by the face $\left\{l_{j}(x)=0\right\}$. In particular, [D] is very ample.

The Futaki invariant of $X_{P}$ with respect to $\left(S^{1}\right)^{n}$-action is shown in [27] exactly the Barycenter of $P$ defined by
$$P_{c}=\frac{\int_{P} x d V}{\int_{P} d V},$$
where $d V=d x_{1} d x_{2} \ldots d x_{n}$ is the standard Euclidean volume form.
The following theorem is due to Wang and Zhu [50] for the existence of Kähler-Einstein metrics on toric Fano manifolds.

Theorem 3.1. There exists a smooth toric Kähler-Einstein metric on a toric Fano manifold $X_{P}$ if and only if the Barycenter of $P$ coincides with 0.

If the Barycenter is not at the origin, it is also proved in [50] that there exists a toric Kähler-Ricci soliton on $X_{P}$. The following theorem is proved by Li [21] to calculate the the greatest Ricci lower bound $R(X)$.

Theorem 3.2. Let $X_{P}$ be a toric Fano manifold associated to a Fano Delzant polytop $P$. Let $P_{c}$ be the Barycenter of $P$ and $Q \in \partial P$ such that the origin $O \in \overline{P_{c} Q}$. Then the greatest Ricci lower bound of $X_{P}$ is given by
$$R\left(X_{P}\right)=\frac{|\overline{O Q}|}{\left|\overline{P_{c} Q}\right|} .$$

For any $\tau \in \mathbb{R}^{n}$, we define the divisor $D(\tau)$ by
$$D(\tau)=\sum_{j=1}^{N} l_{j}(\tau) D_{j} .$$
$D(\tau)$ is a Cartier $\mathbb{R}$-divisor in $c_{1}(X)$ and it is effective if and only if $\tau \in \bar{P}$. The defining section $s_{\tau}$ of $D(\tau)$ is given by the monomial
$$s_{\tau}=z^{\tau} .$$
Although $s_{\tau}$ is only locally defined,
$$\left|s_{\tau}\right|^{2}=|z|^{2 \tau}=e^{\tau \cdot \rho}$$
is globally defined and $\left|s_{\tau}\right|^{-2}$ induces a singular hermitian metric on $-K_{X}$ and can be viewed as a singular volume form with poles along $D_{j}$ of order $l_{j}(\tau)$. We immediately have the following lemma.

Lemma 3.2. If $R(X)<1$, then the $\mathbb{R}$-divisor $D(\tau)$ with $\tau=-\frac{\alpha}{1-\alpha} P_{c}$ is effective if and only if $\alpha \in[0, R(X)]$.

We consider the following real Monge-Ampère equation on $\mathbb{R}^{n}$ for a convex function $\phi$
$$\operatorname{det}\left(\nabla^{2} \phi\right)=e^{-\alpha \phi-(1-\alpha) \tau \cdot \rho} .$$

Let $u=\mathcal{L} \phi$ be the symplectic potential. Then
$$\operatorname{det}\left(\nabla^{2} u\right)=\left(\operatorname{det}\left(\nabla^{2} \phi\right)^{n}\right)^{-1}$$
and dual Monge-Ampère equation for $u$ is given by
$$\operatorname{det}\left(\nabla^{2} u\right)=e^{-\alpha u+(\alpha x+(1-\alpha) \tau) \cdot \nabla u} .$$
If we let $\omega=\sqrt{-1} \partial \bar{\partial} \phi$, the corresponding curvature equation is given by
$$\operatorname{Ric}(\omega)=\alpha \omega+(1-\alpha)[D(\tau)] .$$

Lemma 3.3. Suppose there exists a smooth conical Kähler-Einstein metric $\omega=\sqrt{-1} \partial \bar{\partial} \phi$ satisfying
$$\operatorname{Ric}(\omega)=\alpha \omega+(1-\alpha)[D(\tau)]$$
for some $\alpha \in(0, R(X)]$ and $\tau \in \bar{P}$. Then
$$\tau=-\frac{\alpha}{1-\alpha} P_{c}, \text { for } \alpha \neq 1, \quad \tau=0, \text { for } \alpha=1 \text {. }$$
Furthermore, there exists $f \in C^{\infty}(\bar{P})$ such that
$$\mathcal{L} \phi(x)=\sum_{j=1}^{N} \beta_{j}^{-1} l_{j}(x) \log l_{j}(x)+f(x), \quad \beta_{j}=\frac{l_{j}\left(P_{c}\right)}{l_{j}(0)} \alpha .$$
Proof. Consider the corresponding Monge-Ampère equation $\left(\operatorname{det} \nabla^{2} \phi\right)^{n}=e^{-\alpha \phi-(1-\alpha) \tau \cdot \rho}$. The right hand side $e^{-\alpha \phi-(1-\alpha) \tau \cdot \rho}$ is integrable on $\mathbb{R}^{n}$ and in fact
$$\int_{\mathbb{R}^{n}} e^{-\alpha \phi-(1-\alpha) \tau \cdot \rho} d \rho=\int_{\mathbb{R}^{n}} \operatorname{det}\left(\nabla^{2} \phi\right) d \rho=\int_{X} \omega^{n}=c_{1}(X)^{n}$$
Then the Monge-Ampère mass $\operatorname{det}\left(\nabla^{2} \phi\right) d \rho$ becomes $d x$ by the moment map and
$$\begin{aligned}
0 & =\int_{\mathbb{R}^{n}} \nabla\left(e^{-\alpha \phi-(1-\alpha) \tau \cdot \rho}\right) d \rho \\
& =-\int_{\mathbb{R}^{n}}(\alpha \nabla \phi+(1-\alpha) \tau) e^{-\alpha \phi-(1-\alpha) \tau \cdot \rho} d \rho \\
& =-\int_{P}(\alpha x+(1-\alpha) \tau) d x \\
& =-\left(\alpha P_{c}+(1-\alpha) \tau\right) \int_{P} d x
\end{aligned}$$
Therefore $\tau=\frac{\alpha}{1-\alpha} P_{c}$ for $\alpha \neq 1$.
Suppose $u(x)=\mathcal{L} \phi(x)=\sum_{j=1}^{N} \beta_{j}^{-1} l_{j}(x) \log l_{j}(x)+f(x)$. The Monge-Ampère equations for $\phi$ and $u$ are given by
$$\operatorname{det}\left(\nabla^{2} \phi\right)=e^{-\alpha\left(\phi+P_{c} \cdot \rho\right)}, \operatorname{det}\left(\nabla^{2} u\right)=e^{-\alpha\left(u-\left(x-P_{c}\right) \cdot \nabla u\right)} .$$