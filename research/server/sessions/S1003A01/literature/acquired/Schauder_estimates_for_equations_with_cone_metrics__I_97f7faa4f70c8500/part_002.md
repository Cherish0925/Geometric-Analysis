---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Schauder estimates for equations with cone metrics, I]

By the triangle inequality,
$$\begin{aligned}
& \left|\partial_{r_{n}} D^{\prime} h_{k}(p)-\partial_{r_{n}} D^{\prime} h_{k}(q)\right| \\
\leq & \left|\partial_{r_{n}} D^{\prime} h_{k}(p)-\partial_{r_{n}} D^{\prime} h_{k}\left(p^{\prime}\right)\right|+\left|\partial_{r_{n}} D^{\prime} h_{k}\left(p^{\prime}\right)-\partial_{r_{n}} D^{\prime} h_{k}\left(q^{\prime}\right)\right| \\
& +\left|\partial_{r_{n}} D^{\prime} h_{k}\left(q^{\prime}\right)-\partial_{r_{n}} D^{\prime} h_{k}(q)\right| .
\end{aligned}$$
Along $\gamma_{3}(\theta)$, we have (for notation convenience we write below $h_{k, i r_{n}}=\partial_{r_{n}} D_{i}^{\prime} h_{k}$ )
$$\left|\partial_{r_{n}} D^{\prime} h_{k}(p)-\partial_{r_{n}} D^{\prime} h_{k}\left(p^{\prime}\right)\right|=\left|\int_{\theta_{n}(p)}^{\theta_{n}(q)} \frac{\partial h_{k, i r_{n}}}{\partial \theta_{n}} d \theta_{n}\right| \leq C r_{n}(p)^{\frac{1}{\beta}-1} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right) .$$
Along $\gamma_{2}(t)$, we have
$$\begin{aligned}
& \left|\partial_{r_{n}} D^{\prime} h_{k}\left(p^{\prime}\right)-\partial_{r_{n}} D^{\prime} h_{k}\left(q^{\prime}\right)\right|=\left|\int_{r_{n}(p)}^{r_{n}(q)} \frac{\partial h_{k, i r_{n}}}{\partial r_{n}} d t\right| \\
\leq & C \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right) \int_{r_{n}(p)}^{r_{n}(q)} t^{\frac{1}{\beta}-2} d t \\
\leq & C \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right)\left|r_{n}(q)^{\frac{1}{\beta}-1}-r_{n}(p)^{\frac{1}{\beta}-1}\right| \\
\leq & C \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right)\left|r_{n}(q)-r_{n}(p)\right|^{\frac{1}{\beta}-1} \\
\leq & C \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right) d^{\frac{1}{\beta}-1},
\end{aligned}$$
where we make use of the elementary inequality that for any $a, b>0$ and $\kappa \in(0,1)$,
$$\left|a^{\kappa}-b^{\kappa}\right| \leq|a-b|^{\kappa} .$$
Along $\gamma_{1}(t)$,
$$\begin{aligned}
\left|\partial_{r_{n}} D^{\prime} h_{k}(q)-\partial_{r_{n}} D^{\prime} h_{k}\left(q^{\prime}\right)\right| & \leq\left|\left(D^{\prime}\right)^{2} \partial_{r_{n}} h_{k}\right| d \\
& \leq C \tau^{-k} \omega\left(2 \tau^{k}\right) d \\
& \leq C \tau^{-k\left(\frac{1}{\beta}-1\right)} d^{\frac{1}{\beta}-1} \omega\left(2 \tau^{k}\right) .
\end{aligned}$$
\begin{itemize}
\item[(2)] $r_{p} \geq 2 d$ and $\ell \leq k_{p}$. This case is relatively easier. By the triangle inequality, $r_{n}(t)=$ $r_{n}(\gamma(t)) \geq d$ for all $t \in[0, d]$. Along $\gamma(t)$,
$$\left|\nabla_{g_{\beta}}\left(\partial_{r_{n}} D^{\prime} h_{k}\right)\right|_{g_{\beta}}$$
\end{itemize}
$$\begin{aligned}
& =\left(\sum_{j=1}^{2 n-2}\left(\frac{\partial\left(\partial_{r_{n}} D^{\prime} h_{k}\right)}{\partial s_{j}}\right)^{2}+\left(\frac{\partial\left(\partial_{r_{n}} D^{\prime} h_{k}\right)}{\partial r_{n}}\right)^{2}+\frac{1}{\beta^{2} r_{n}(t)^{2}}\left(\frac{\partial\left(\partial_{r_{n}} D^{\prime} h_{k}\right)}{\partial \theta_{n}}\right)^{2}\right)^{1 / 2} \\
& \leq C(n) \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right)\left(r_{n}(t)^{\frac{1}{\beta}-2}\right) \\
& \leq C(n) \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right) d^{\frac{1}{\beta}-2} .
\end{aligned}$$
Integrating along the geodesic $\gamma$, we obtain the following desired estimate
$$\left|\left(\partial_{r_{n}} D^{\prime} h_{k}\right)(p)-\left(\partial_{r_{n}} D^{\prime} h_{k}\right)(q)\right| \leq C(n) d^{\frac{1}{\beta}-1} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(2 \tau^{k}\right) .$$
\begin{itemize}
\item[(3)] $r_{p} \geq 2 d$ and $\ell>k_{p}$. In this case, we will replace $\left(s, z_{n}\right)$ by $(s, w)$ for $w=\left(z_{n}\right)^{\beta}$ in $B_{\beta}\left(p, \tau^{k}\right)$, by taking a single-value branch, when $k_{p}<k \leq \ell$. The cone metric $g_{\beta}$ becomes the standard Euclidean metric in $(s, w)$ and
$$\Delta_{g_{\beta}}\left(D^{\prime} h_{k}\right)=\sum_{j=1}^{2 n-2} \frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial\left(s_{j}\right)^{2}}+\sqrt{-1} \frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial w \partial \bar{w}}=0, \text { in } B_{\beta}\left(p, \tau^{k+1}\right) .$$
It then follows from the derivative estimates for Euclidean harmonic functions that
$$\begin{aligned}
& \left\|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial w}\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+2}\right)\right)} \leq C \omega\left(\tau^{k}\right), \\
& \left\|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial w \partial w}\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+2}\right)\right)}+\left\|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial w \partial \bar{w}}\right\|_{L^{\infty}\left(B_{\beta}\left(p, \tau^{k+2}\right)\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Since
$$2 w \frac{\partial}{\partial w}=r_{n} \frac{\partial}{\partial r_{n}}-\frac{\sqrt{-1}}{\beta} \frac{\partial}{\partial \theta_{n}}, \quad \frac{\partial}{\partial r_{n}}=\frac{w}{r_{n}} \frac{\partial}{\partial w}+\frac{\bar{w}}{r_{n}} \frac{\partial}{\partial \bar{w}},$$
we have (denote $h_{k, i}=D_{i}^{\prime} h_{k}$ )
$$\begin{aligned}
\frac{\partial}{\partial w}\left(\frac{\partial h_{k, i}}{\partial r_{n}}\right)= & \frac{1}{r_{n}} \frac{\partial h_{k, i}}{\partial w}-\frac{w}{r_{n}^{2}} \frac{\bar{w}}{2 r_{n}} \frac{\partial h_{k, i}}{\partial w}+\frac{w}{r_{n}} \frac{\partial^{2} h_{k, i}}{\partial w^{2}} \\
& -\frac{\bar{w}}{r_{n}^{2}} \frac{\bar{w}}{2 r_{n}} \frac{\partial h_{k, i}}{\partial \bar{w}}+\frac{\bar{w}}{r_{n}} \frac{\partial^{2} h_{k, i}}{\partial w \partial \bar{w}} .
\end{aligned}$$
Therefore
$$\begin{aligned}
& \left|\nabla \frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}\right|_{g_{\beta}} \\
\leq & C\left(\frac{1}{r_{n}}\left|\frac{\left(D^{\prime} h_{k}\right)}{\partial w}\right|+\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial w \partial w}\right|+\frac{1}{r_{n}}\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial w}\right|+\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial w \partial \bar{w}}\right|+\tau^{-k} \omega\left(\tau^{k}\right)\right) \\
\leq & C \frac{1}{r_{n}} \omega\left(\tau^{k}\right)+C \tau^{-k} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Let $\gamma$ be the minimal geodesic connecting $p$ and $q$ with respect to $g_{\beta}$. Then along $\gamma$, there exists $C>0$ such that
$$r_{n}(\gamma(t)) \geq C r_{p} .$$
After integrating along $\gamma$, it follows that
$$\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}(p)-\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}(q)\right| \leq C(n, \beta) d^{\frac{1}{\beta}-1} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(\tau^{k}\right) .$$
\end{itemize}

The estimate (2.48) is then proved by combining the above three cases. (2.49) can be proved by similar argument. \(\square\)

Corollary 2.2. There exists $C=C(n, \beta)>0$ such that
$$\begin{aligned}
& \left|\partial_{r_{n}} D^{\prime} u_{\ell}(p)-\partial_{r_{n}} D^{\prime} u_{\ell}(q)\right|+\left|\left(\left(r_{n}\right)^{-1} \partial_{\theta_{n}} D^{\prime} u_{\ell}\right)(p)-\left(\left(r_{n}\right)^{-1} \partial_{\theta_{n}} D^{\prime} u_{\ell}\right)(q)\right| \\
\leq & C d^{\frac{1}{\beta}-1}\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\sum_{k=2}^{\ell} \tau^{-k\left(\frac{1}{\beta}-1\right)} \omega\left(\tau^{k}\right)\right) .
\end{aligned}$$
Proof. The Corollary follows from (2.48) by similar argument in the proof to estimate $I_{2}$ in Proposition 2.3. \(\square\)

The following proposition is the main result in this subsection.
Proposition 2.4. Let $\beta \in(1 / 2,1)$. There exists $C=C(n, \beta)>0$ such that for all $p, q \in$ $B_{\beta}(0,1 / 2) \backslash \mathcal{S}$,
$$\begin{aligned}
& \sum_{i=2 n-1}^{2 n} \sum_{j=1}^{2 n-2}\left|D_{i} D_{j} u(p)-D_{i} D_{j} u(q)\right| \\
\leq & C\left(d^{\frac{1}{\beta}-1} \sup _{B_{\beta}(0,1)}|u|+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{\frac{1}{\beta}-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta}} d r\right),
\end{aligned}$$
where $d=d_{\beta}(p, q)$.
Proof. The proposition is an immediate consequence of Lemma 2.11 and Corollary 2.2. \(\square\)
2.7. Proof of Theorem 1.1. Theorem 1.1 immediately follows by combining Proposition 2.3 and Proposition 2.4.
2.8. The case of $\beta \in(0,1 / 2)$. If $\beta \in(0,1 / 2)$, Theorem 1.1 can be proved by parallel arguments for the case of $\beta \in(1 / 2,1)$ with slight modifications.

Proposition 2.5. Suppose $\beta \in(0,1 / 2)$ and $f(x)$ is Dini continuous on $B_{\beta}(0,1)$ with respect to $g_{\beta}$ for some $\beta \in(0,1)$. Let
$$\omega(r)=\sup _{d_{\beta}(z, w)<r, z, w \in B_{\beta}(0,1)}|f(z)-f(w)| .$$
If $u \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \cap L^{\infty}\left(B_{\beta}(0,1)\right)$ is a solution of the conical Laplace equation (1.3), then there exists $C=C(n, \beta)>0$ such that
$$\begin{aligned}
& \sum_{i=2 n-1}^{2 n} \sum_{j=1}^{2 n-2}\left|D_{i} D_{j} u(p)-D_{i} D_{j} u(q)\right|+\sum_{i, j=1}^{2 n-2}\left|D_{i} D_{j} u(p)-D_{i} D_{j} u(q)\right| \\
\leq & C\left(d \sup _{B_{\beta}(0,1)}|u|+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right),
\end{aligned}$$
where $d=d_{\beta}(p, q)$.

Proof. Let us point out the major differences in the proof from that of Theorem 1.1. The estimate in Proposition 2.1 is pointwise:
$$\left|\frac{\partial u}{\partial z}(z)\right| \leq C \frac{\|u\|_{L^{\infty}\left(B_{\rho}(0)\right)}^{\rho}}{\rho}+C\|F\|_{L^{\infty}\left(B_{\rho}(0)\right)}|z|^{2 \beta-1}, \quad \forall z \in B_{\rho / 2}(0) \backslash\{0\} .$$
With this estimate, the statements in Lemmas 2.12 and Lemma 2.13 are revised as follows.
(1) Lemma 2.12:
$$\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{\partial r_{n}}\right|(z)+\left|\frac{\partial\left(D^{\prime} h_{k}\right)}{r_{n} \partial \theta_{n}}\right|(z) \leq C r_{n} \tau^{-k} \omega\left(2 \tau^{k}\right) .$$
(2) Lemma 2.13:
$$\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{r_{n}^{2} \partial\left(\theta_{n}\right)^{2}}\right|(z)+\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{r_{n} \partial r_{n} \partial \theta_{n}}\right|(z)+\left|\frac{\partial^{2}\left(D^{\prime} h_{k}\right)}{\partial\left(r_{n}\right)^{2}}\right|(z) \leq C \tau^{-k} \omega\left(2 \tau^{k}\right) .$$ \(\square\)
2.9. The case of $\beta=1 / 2$. In this case, $g_{\beta}$ is an orbifold metric. We can lift the equation on the double cover with $z_{n}=w^{2}$. Then the conical Laplace equation becomes the standard Laplace equation and one can directly apply the Schauder estimate on $\mathbb{R}^{2 n}$. We obtain the same estimate as (2.58).

\section*{3. Parabolic Schauder estimates}

The goal of this section is to derive the $\mathcal{P}_{\beta}^{2, \alpha}$-estimate of the parabolic equation
$$\frac{\partial u}{\partial t}-\Delta_{g_{\beta}} u=f, \quad \text { in } \mathcal{Q}_{\beta},$$
where $f$ is a given Dini continuous function on $\overline{\mathcal{Q}_{\beta}}$ with respect to the conical parabolic distance.
3.1. Notations. We denote $\mathcal{Q}_{\beta}=B_{\beta}(0,1) \times(0,1]$ to be the space-time cylinder, and
$$\partial_{\mathcal{P}} \mathcal{Q}_{\beta}=\left(\overline{B_{\beta}(0,1)} \times\{0\}\right) \cup\left(\partial B_{\beta}(0,1) \times(0,1)\right)$$
to be the parabolic boundary of the cylinder $\mathcal{Q}_{\beta}$. Let
$$\mathcal{S}_{\mathcal{P}}=\{(p, t) \mid p \in \mathcal{S}, t \in \mathbb{R}\}$$
be the parabolic singular set. The conical parabolic distance of two points $Q_{1}=\left(z_{1}, t_{1}\right)$ and $Q_{2}=\left(z_{2}, t_{2}\right)$ in $\mathcal{Q}_{\beta}$ as
$$d_{\mathcal{P}, \beta}\left(Q_{1}, Q_{2}\right)=\max \left\{d_{\beta}\left(z_{1}, z_{2}\right), \sqrt{\left|t_{1}-t_{2}\right|}\right\} .$$
We denote
$$\omega(r)=\sup \left\{\left|f\left(Q_{1}\right)-f\left(Q_{2}\right)\right|: Q_{1}, Q_{2} \in \overline{\mathcal{Q}_{\beta}}, d_{P, \beta}\left(Q_{1}, Q_{2}\right) \leq r\right\}$$
to be the oscillation function of $f$ over the cylinder $\overline{\mathcal{Q}_{\beta}}$.
Definition 3.1. We say a function $u$ is $\mathcal{P}^{2}$ in the cylinder $\mathcal{O}_{\beta}$, if for each time $t \in(0,1]$, $u(\cdot, t) \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right)$, and $\frac{\partial u}{\partial t} \in C^{0}\left(\mathcal{Q}_{\beta}\right)$.

We define the $\mathcal{P}_{\beta}^{0, \alpha}$ norm of a function in $\mathcal{Q}_{\beta}$ similar to that in Definition 2.1, using the parabolic distance $d_{\mathcal{P}, \beta}$. We define the $\mathcal{P}_{\beta}^{2, \alpha}$ norm in $\mathcal{Q}_{\beta}$ as
$$\begin{aligned}
\|u\|_{\mathcal{P}_{\beta}^{2, \alpha}}= & \|u\|_{C^{0}\left(\mathcal{Q}_{\beta}\right)}+\sum_{i=1}^{2 n}\left\|D_{i} u\right\|_{C^{0}\left(\mathcal{Q}_{\beta}\right)}+\left\|\partial_{t} u\right\|_{\mathcal{P}_{\beta}^{0, \alpha}\left(\mathcal{Q}_{\beta}\right)} \\
& +\sum_{i=1}^{2 n} \sum_{j=1}^{2 n-2}\left\|D_{i} D_{j} u\right\|_{\mathcal{P}_{\beta}^{0, \alpha}\left(\mathcal{Q}_{\beta}\right)}+\left\|\left|z_{n}\right|^{2-2 \beta} \frac{\partial^{2} u}{\partial z_{n} \partial \bar{z}_{n}}\right\|_{\mathcal{P}_{\beta}^{0, \alpha}\left(\mathcal{Q}_{\beta}\right)}
\end{aligned}$$

Suppose $u \in \mathcal{P}^{2}\left(\mathcal{Q}_{\beta} \backslash \mathcal{S}_{\mathcal{P}}\right) \cap C^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$ solves the Dirichlet problem for the conical heat equation
$$\left\{\begin{array}{c}
\frac{\partial u}{\partial t}-\Delta_{g_{\beta}} u=0, \quad \text { in } \mathcal{Q}_{\beta} \\
u(z, t)=\varphi(z, t), \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta},
\end{array}\right.$$
for some given continuous function $\varphi \in C^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\beta}\right)$. Without loss of generality, we assume $\varphi$ can be continuously extended to $\overline{\mathcal{Q}_{\beta}}$.

Applying the same barrier function as in Lemma 2.1, we have the following maximum principle for the conical heat equation.

Lemma 3.1. Suppose $u \in \mathcal{P}^{2}\left(\mathcal{Q}_{\beta} \backslash \mathcal{S}_{\mathcal{P}}\right) \cap C^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$ solves the equation (3.2), then
$$\inf _{\overline{\mathcal{Q}_{\beta}}} \varphi \leq \inf _{\mathcal{Q}_{\beta}} u \leq \sup _{\mathcal{Q}_{\beta}} u \leq \sup _{\overline{\mathcal{Q}_{\beta}}} \varphi .$$

In particular, the conical heat equation (3.2) admits a unique solution.
Corollary 3.1. If the Dirichlet boundary value problem (3.2) is solvable in $\mathcal{P}^{2}\left(\mathcal{Q}_{\beta} \backslash \mathcal{S}_{\mathcal{P}}\right) \cap C^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$, the solution must be unique.
3.2. Conical heat equations. In this subsection, we will obtain a parabolic gradient estimate of Li-Yau for conical heat equation. The following proposition is the standard Li-Yau gradient estimate for positive solution to the heat equation ([16], see also Theorem 4.2 in [26]).

Proposition 3.1. Let $(M, g)$ be a complete manifold with $\operatorname{Ric}(g) \geq 0$, and $B(p, R)$ be the geodesic ball with center $p \in M$ and radius $R>0$. Let $u$ be a positive solution to the heat equation $\partial_{t} u-\Delta_{g} u=0$ on $B(p, R)$, then there exists $C=C(n)>0$ such that for all $t>0$,
$$\sup _{B(p, R / 2)}\left(\frac{|\nabla u|^{2}}{u^{2}}-\frac{2 u_{t}}{u}\right) \leq \frac{C}{R^{2}}+\frac{2 n}{t},$$
where $u_{t}=\frac{\partial u}{\partial t}$.
The following corollary is a straightforward consequence of Proposition 3.1.
Corollary 3.2. With the same assumptions in Proposition 3.1, there exists $C=C(n)>0$ such that for all $t \in\left(0, R^{2}\right)$
$$\sup _{B(p, R / 2)}|\nabla u|^{2}(t) \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right)\left(\operatorname{osc}_{B(p, R) \times\left[0, R^{2}\right]} u\right)^{2}$$
and
$$\sup _{B(p, R / 2)}\left|\Delta_{g} u\right|(t)=\sup _{B(p, R / 2)}\left|\frac{\partial u}{\partial t}\right| \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right)\left(\operatorname{osc}_{B(p, R) \times\left[0, R^{2}\right]} u\right) .$$

Proof. Replacing the positive solution $u$ by $u-\inf u$ if necessary, we may assume that $u \leq \operatorname{osc} u$. We let $A=\sup _{B(p, R) \times\left[0, R^{2}\right]} u$ and $v=A-u$. Clearly $v$ also satisfies the heat equation and by Li-Yau gradient estimates we have on $B(p, R / 2)$,
$$\frac{|\nabla u|^{2}}{v} \leq 2 v_{t}+C\left(\frac{1}{R^{2}}+\frac{1}{t}\right) v=-2 u_{t}+C\left(\frac{1}{R^{2}}+\frac{1}{t}\right) v,$$
and by Proposition 3.1 we also have
$$\frac{|\nabla u|^{2}}{u} \leq 2 u_{t}+C\left(\frac{1}{R^{2}}+\frac{1}{t}\right) u .$$
Adding (3.3) and (3.4), we have
$$\left(\frac{1}{u}+\frac{1}{v}\right)|\nabla u|^{2} \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right)(u+v),$$
from which it follows that on $B(p, R / 2)$
$$|\nabla u|^{2} \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right) u(A-u) \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right)\left(\operatorname{osc}_{B(p, R) \times\left[0, R^{2}\right]} u\right)^{2} .$$
The estimate for $\Delta u$ follows easily from the fact that $\frac{\partial u}{\partial t}=\Delta u$. \(\square\)

Given Corollary 3.2, we are ready to show the existence of solution to the equation (3.2).
Proposition 3.2. Given any $\varphi \in C^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$, there exists a unique $u \in \mathcal{P}^{2}\left(\mathcal{Q}_{\beta} \backslash \mathcal{S}_{\mathcal{P}}\right) \times C^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$ solving equation (3.2).

Proof. The strategy is to solve the Dirichlet boundary problem for the smooth metrics $g_{\epsilon}$ approximating the conical metric $g_{\beta}$ and the limiting solution will solve (3.2).

Let $u_{\epsilon} \in \mathcal{P}^{2}\left(\mathcal{Q}_{\beta}\right) \cap C^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$ solve the Dirichlet boundary problem
$$\left\{\begin{aligned}
\frac{\partial u_{\epsilon}}{\partial t} & =\Delta_{g_{\epsilon}} u_{\epsilon}, \quad \text { in } \mathcal{Q}_{\beta} \\
u_{\epsilon} & =\varphi, \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta},
\end{aligned}\right.$$
where $g_{\epsilon}$ is a smooth Riemannian metric defined in (2.6) to approximate $g_{\beta}$ for $\epsilon \in(0,1)$. We immediately have following estimate by the maximum principle.
$$\left\|u_{\epsilon}\right\|_{L^{\infty}\left(\mathcal{Q}_{\beta}\right)} \leq\|\varphi\|_{L^{\infty}\left(\overline{\mathcal{Q}_{\beta}}\right.} .$$
Let $K \subset \subset K^{\prime} \subset \subset B_{\beta}(0,1)$ be arbitrarily compact subsets in $B_{\beta}(0,1)$. Applying Corollary 3.2, we have
$$\begin{gathered}
\sup _{K^{\prime}}\left|\nabla u_{\epsilon}\right|_{g_{\epsilon}}^{2}(\cdot, t) \leq C\left(n, K^{\prime},\|\varphi\|_{\infty}\right)\left(1+t^{-1}\right), \\
\sup _{K^{\prime}}\left|\frac{\partial u_{\epsilon}}{\partial t}\right| \leq C\left(n, K^{\prime},\|\varphi\|_{\infty}\right)\left(1+t^{-1}\right)
\end{gathered}$$
Similarly we have
$$\sup _{K}\left|\nabla\left(D^{\prime} u_{\epsilon}\right)\right|_{g_{\epsilon}}^{2} \leq C\left(n, K, K^{\prime},\|\varphi\|_{\infty}\right)\left(1+t^{-2}\right),$$
and
$$\sup _{K}\left|\nabla\left(\left(D^{\prime}\right)^{2} u_{\epsilon}\right)\right|_{g_{\epsilon}}^{2} \leq C\left(n, K, K^{\prime},\|\varphi\|_{\infty}\right)\left(1+t^{-3}\right) .$$
It follows from the standard elliptic estimates that the functions $u_{\epsilon}$ have uniform $\mathcal{P}^{2, \alpha}$ estimates on $K \backslash T_{\delta}(\mathcal{S}) \times[\delta, 1]$, for a fixed $\delta>0$. So $u_{\epsilon}$ converges uniformly in $\mathcal{P}^{2, \alpha}\left(K \backslash T_{\delta}(\mathcal{S}) \times[\delta, 1]\right)$-topology
to a function $u \in \mathcal{P}^{2, \alpha}\left(K \backslash T_{\delta}(\mathcal{S}) \times[\delta, 1]\right)$. Since $K$ is arbitrary, by taking a diagonal sequence, we may assume $u_{\epsilon}$ converges to $u$ uniformly on any compact subset of $B_{\beta}(0,1) \backslash \mathcal{S} \times(0,1]$. Clearly $u$ satisfies the equation $\partial_{t} u=\Delta_{g_{\beta}} u$ on $B_{\beta} \backslash \mathcal{S} \times(0,1]$ and the estimates (3.6), (3.7) and (3.8). In particular (3.6) implies that $u$ can be continuously extended over $\mathcal{S}$, so $u \in C^{0}\left(B_{\beta} \times(0,1]\right)$.

It remains to show $u$ is continuous up to boundary and it coincides with $\varphi$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\beta}$. We will show that for any $\left(q, t_{0}\right) \in \partial_{\mathcal{P}} \mathcal{Q}_{\beta}$,
$$\lim _{\mathcal{Q}_{\beta} \ni(z, t) \rightarrow\left(q, t_{0}\right)} u(z, t)=\varphi\left(q, t_{0}\right) .$$
Case 1: $t_{0}=0$ and $q \in \overline{B_{\beta}(0,1)}$. We will construct the barrier function
$$\phi_{q, 1}(z, t)=e^{-d_{\mathbb{C}^{n}}(z, q)^{2}-\lambda t}-1,$$
where $d_{\mathbb{C}^{n}}$ is the Euclidean distance and $\lambda>0$ is a constant to be determined. Direct calculations show that
$$\begin{aligned}
\Delta_{g_{\epsilon}} \phi_{q, 1} & =\left(-\Delta_{\epsilon} d_{\mathbb{C}^{n}}^{2}+\left|\nabla d_{\mathbb{C}^{n}}^{2}\right|_{g_{\epsilon}}^{2}\right) e^{-d_{\mathbb{C}^{n}}(z, q)^{2}-\lambda t} \\
& =\left(-(n-1)-\left(\left|z_{n}\right|^{2}+\epsilon\right)^{1-\beta}+\left|\nabla d_{\mathbb{C}^{n}}^{2}\right|_{g_{\epsilon}}^{2}\right) e^{-d_{\mathbb{C}^{n}}(z, q)^{2}-\lambda t} \\
& \geq-(n+1) e^{-d_{\mathbb{C}^{n}}(z, q)^{2}-\lambda t} \\
& \geq-\lambda e^{-d_{\mathbb{C}^{n}}(z, q)^{2}-\lambda t}=\frac{\partial \phi_{q, 1}}{\partial t},
\end{aligned}$$
if we choose $\lambda \geq n+1 . \phi_{q, 1}$ is a continuous function on $\overline{\mathcal{Q}_{\beta}}$ with $\phi_{q, 1}\left(q, t_{0}\right)=0$ and $\phi_{q, 1}(z, t)<0$ for any other $(z, t) \in \overline{\mathcal{Q}_{\beta}}$.

For any fixed $\delta>0$, by the continuity of $\varphi$ it follows that there exists a small space-time neighborhood $V$ of $\left(q, t_{0}\right)$ such that $\varphi\left(q, t_{0}\right)-\delta \leq \varphi(z, t)$ for all $(z, t) \in V$. Moreover, on $\overline{\mathcal{Q}_{\beta}} \backslash V$ the function $\phi_{q}$ is bounded above by a negative constant, so by taking sufficiently large $A>0$, the function $\varphi_{q}^{-}$defined by
$$\varphi_{q}^{-}(z, t):=\varphi\left(q, t_{0}\right)-\delta+A \phi_{q, 1}(z, t) \leq \varphi(z, t),$$
is a sub-solution of the heat equation, i.e. $\frac{\partial \varphi_{q}^{-}}{\partial t} \leq \Delta_{\epsilon} \varphi_{q}^{-}$. Then $\varphi_{q}^{-}(z, t) \leq u_{\epsilon}(z, t)$ for all $(z, t) \in \mathcal{Q}_{\beta}$ by the maximum priniciple. Letting $\epsilon \rightarrow 0$, we also have $\varphi_{q}^{-}(z, t) \leq u(z, t)$ and so
$$\varphi\left(q, t_{0}\right)-\delta=\lim _{(z, t) \rightarrow\left(q, t_{0}\right)} \varphi_{q}^{-}(z, t) \leq \liminf _{(z, t) \rightarrow\left(q, t_{0}\right)} u(z, t) .$$
Letting $\delta \rightarrow 0, \varphi\left(q, t_{0}\right) \leq \liminf _{(z, t) \rightarrow\left(q, t_{0}\right)} u(z, t)$.
By similar argument we can show that $\varphi\left(q, t_{0}\right) \geq \limsup _{(z, t) \rightarrow\left(q, t_{0}\right)} u(z, t)$ by considering the super-solution $\varphi_{q}^{+}(z, t)=\varphi\left(q, t_{0}\right)+\delta-A \phi_{q}(z, t)$ for appropriate $A>0$. Therefore,
$$\lim _{(z, t) \rightarrow\left(q, t_{0}\right)} u(z, t)=\varphi\left(q, t_{0}\right) .$$
Case 2: $t_{0}>0$ and $q \in \partial B_{\beta}(0,1)$ with $z_{n}(q)=0$. Let $q^{\prime}=-q \in \mathbb{C}^{n}$ be the opposite point of $q$ with respect to $0 \in \mathbb{C}^{n}$. We define the barrier function
$$\phi_{q, 2}(z, t)=d_{\mathbb{C}^{n}}\left(z, q^{\prime}\right)^{2}-4-\delta\left(t-t_{0}\right)^{2}$$
for a small $\delta>0$ to be determined. Since $q$ is the unique furthest point in $B_{\beta}(0,1)$ to $q^{\prime}$ under Euclidean distance, hence $\phi_{q, 2}\left(q, t_{0}\right)=0$ and $\phi_{q, 2}(z, t)<0$ for all other $(z, t) \in \overline{\mathcal{Q}_{\beta}}$. Straightforward calculations show that
$$\frac{\partial \phi_{q, 2}}{\partial t}=-2 \delta\left(t-t_{0}\right),$$
and
$$\Delta_{\epsilon} \phi_{q, 2}=(n-1)+\beta^{-2}\left(\left|z_{n}\right|^{2}+\epsilon\right)^{1-\beta} \geq n-1 .$$
Then $\partial_{t} \phi_{q, 2} \leq \Delta_{\epsilon} \phi_{q, 2}$ for $\delta \leq(n-1) / 2$. By the same argument as in Case 1, we see that $u$ is also continuous at $\left(q, t_{0}\right) \in \partial_{\mathcal{P}} \mathcal{Q}_{\beta}$ and $\lim _{(z, t) \rightarrow\left(q, t_{0}\right)} u(z, t)=\varphi\left(q, t_{0}\right)$.
Case 3: $t_{0}>0$ and $q \in \partial B_{\beta}(0,1)$ with $z_{n}(q) \neq 0$. We are in the same situation as the case 2 in the proof of Proposition 2.2, and we use the same notations as in Proposition 2.2. We construct the following barrier function
$$\phi_{q, 3}(z, t)=A\left(d_{\beta}(z)^{2}-1\right)+\left(G(z)-\frac{1}{r_{q}^{2 n-2}}\right)-\delta^{\prime}\left(t-t_{0}\right)^{2} .$$
The remaining argument is the same as in Case 1 and Case 2.
Combining the results in the above three cases, we have completed the proof of the proposition. \(\square\)

Furthermore, we also obtaine the conical gradient and Laplace estimates for $u$.
Corollary 3.3. Let $u \in \mathcal{P}^{2}\left(B_{\beta}(0, R) \times\left(0, R^{2}\right]\right) \cap L^{\infty}\left(\overline{B_{\beta}(0, R)} \times\left[0, R^{2}\right]\right)$ solve the heat equation $\partial_{t} u=\Delta_{\beta} u$ in $B_{\beta}(0, R) \backslash \mathcal{S} \times\left(0, R^{2}\right]$. There exists a constant $C=C(n)$ such that
$$\begin{gathered}
\sup _{B_{\beta}(0, R / 2) \backslash \mathcal{S}}|\nabla u|_{g_{\beta}}^{2} \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right)\|u\|_{L^{\infty}\left(B_{\beta}(0, R) \times\left[0, R^{2}\right]\right)}^{2}, \\
\sup _{B_{\beta}(0, R / 2) \backslash \mathcal{S}}\left|\Delta_{\beta} u\right|=\sup _{B_{\beta}(0, R / 2) \backslash \mathcal{S}}\left|\frac{\partial u}{\partial t}\right| \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right)\|u\|_{L^{\infty}\left(B_{\beta}(0, R) \times\left[0, R^{2}\right]\right)} .
\end{gathered}$$
Moreover, the function $\frac{\partial u}{\partial t}$ can be continuously extended to $B_{\beta}(0,1)$.
3.3. Proof of Theorem 1.2. We can now prove Theorem 1.2 by the same argument in the proof of Theorem 1.1, replacing the $g_{\beta}$-harmonic functions by solutions of $g_{\beta}$-heat equation, since we have obtained existence and gradient estimate for solutions of conical heat equation (3.2) from Proposition 3.2 and Corollary 3.3.

Acknowledgements: Both authors thank Duong H. Phong and Qing Han for many insightful discussions.

\section*{References}
\begin{itemize}
\item[] [1] Brendle, S. Ricci flat Kähler metrics with edge singularities, Int. Math. Res. Not. IMRN 2013, no. 24, 5727-5766
\item[] [2] Caffarelli, L.A. Interior a priori estimates for solutions of fully nonlinear equations, Ann. of Math. (2) 130 (1989), 189-213
\item[] [3] Caffarelli, L.A. Interior W2,p estimates for solutions of Monge-Ampère equations, Ann. Math., 131(1990), 135-150
\item[] [4] Chen, X.X., Donaldson, S.K. and Sun, S. Kähler-Einstein metrics on Fano manifolds, I: approximation of metrics with cone singularities, J. Amer. Math. Soc. 28 (2015), no. 1, 183-197.
\item[] [5] Chen, X.X., Donaldson, S.K. and Sun, S. Kähler-Einstein metrics on Fano manifolds, II: limits with cone angle less than $2 \pi$, J. Amer. Math. Soc. 28 (2015), no. 1, 199-234
\item[] [6] Chen, X.X., Donaldson, S.K. and Sun, S. Kähler-Einstein metrics on Fano manifolds, III: limits as cone angle approaches $2 \pi$ and completion of the main proof, J. Amer. Math. Soc. 28 (2015), no. 1, 235-278
\item[] [7] Chen, X.X. and Wang, Y. Bessel functions, heat kernel and the conical Kähler-Ricci flow. J. Funct. Anal. 269 (2015), no. 2, 551-632
\item[] [8] Cheng and Yau, Differential equations on Riemannian manifolds and their geometric applications. Comm. Pure Appl. Math. 28 (1975), no. 3, 333-354
\end{itemize}
\begin{itemize}
\item[] [9] Donaldson, S. K. Kähler metrics with cone singularities along a divisor. Essays in mathematics and its applications, 49-79, Springer, Heidelberg, 2012
\item[] [10] Edwards, G. A scalar curvature bound along the conical Kähler-Ricci flow, preprint arXiv:1505.02083.
\item[] [11] Han, Q., and Lin, F. Elliptic partial differential equations (Vol. 2), American Mathematical Soc.
\item[] [12] Hormander, L. An introduction to complex analysis in several variables. Second revised edition. North-Holland Mathematical Library, Vol. 7. North-Holland Publishing Co., Amsterdam-London; American Elsevier Publishing Co., Inc., New York, 1973. x+213 pp.
\item[] [13] Jeffres, T., Mazzeo, R. and Rubinstein, Y. Kähler-Einstein metrics with edge singularities with appendix by Rubinstein Y. and Li, C., Ann. of Math. (2) 183 (2016), no. 1, 95-176
\item[] [14] Jin, X., Liu, J. and Zhang, X. Twisted and conical Kähler-Ricci solitons on Fano manifolds, J. Funct. Anal. 271 (2016), no. 9, 2396-2421
\item[] [15] Kolodziej, S. The complex Monge-Ampère equation, Acta Math. 180 (1998),69-117
\item[] [16] Li, P. and Yau, S.-T. On the parabolic kernel of the Schrödinger operator. Acta Math. 156 (1986), no. 3-4, 153-201
\item[] [17] Luo, F. and Tian, G. Liouville equation and spherical convex polytopes, Proc. Amer. Math. Soc. 116 (1992), 1119-1129
\item[] [18] Mazzeo, R. Kähler-Einstein metrics singular along a smooth divisor, Journées Eq́uations aux dérivées partielles (1999), 1-10
\item[] [19] Phong, D. H., Song, J., Sturm, J. and Wang, X. The Ricci flow on the sphere with marked points, preprint arXiv:1407.1118
\item[] [20] Rubinstein, Y. Smooth and singular Kähler-Einstein metrics, Geometric and spectral analysis, 45-138, Contemp. Math., 630, Amer. Math. Soc., Providence, RI, 2014
\item[] [21] Mazzeo, R, Rubinstein, Y. and Sesum, N. Ricci flow on surfaces with conic singularities. Anal. PDE 8 (2015), no. 4, 839-882
\item[] [22] Safonov, M.V. The classical solution of the elliptic Bellman equation , Dokl. Akad. Nauk SSSR 278(1984), 810-813; English translation in Soviet Math Doklady 30(1984), 482-485
\item[] [23] Safonov, M.V. Classical solution of second-order nonlinear elliptic equations, Izv. Akad. Nauk SSSR Ser. Mat. 52(1988), 1272-1287; English translation in Math. USSR-Izv. 33(1989), 597-612
\item[] [24] Simon, L. Schauder estimates by scaling, Calc. Var. PDE, 5(1997), 391-407
\item[] [25] Song, J. and Wang, X. The greatest Ricci lower bound, conical Einstein metrics and Chern number inequality. Geom. Topol. 20 (2016), no. 1, 49-102
\item[] [26] Schoen, R. and Yau, S.-T. Lectures on differential geometry. Conference Proceedings and Lecture Notes in Geometry and Topology, I. International Press, Cambridge, MA, 1994. v+235 pp.
\item[] [27] Tian, G. On Kähler-Einstein metrics on certain Kähler manifolds with $C_{1}(M)>0$. Invent. Math. 89 (1987), no. 2, 225-246
\item[] [28] Tian, G. Kähler-Einstein metrics on algebraic manifolds. Transcendental methods in algebraic geometry, 14385, Lecture Notes in Math., 1646, Springer, Berlin, 1996
\item[] [29] Tian, G. K-stability and Kähler-Einstein metrics, Comm. Pure Appl. Math. 68 (2015), no. 7, 1085-1156
\item[] [30] Troyanov, M. Prescribing curvature on compact surfaces with conic singularities, Trans. Amer. Math. Soc. 324 (1991), 793-821
\item[] [31] Wang, X.-J. Schauder estimates for elliptic and parabolic equations. Chinese Ann. Math. Ser. B 27 (2006), no. 6, 637-642
\item[] [32] Yau, S.-T. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, $I$, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411
\item[] [33] Yin, H. Analysis aspects of Ricci flow on conical surfaces, preprint arXiv:1605.08836
\item[] [34] Yin, H. and Zheng, K. Expansion formula for complex Monge-Ampère equation along cone singularities, preprint arXiv:1609.03111
\end{itemize}

Department of Mathematics, Columbia University, New York, NY 10027
E-mail address: bguo@math.columbia.edu
Department of Mathematics, Rutgers University, Piscataway, NJ 08854
E-mail address: jiansong@math.rutgers.edu