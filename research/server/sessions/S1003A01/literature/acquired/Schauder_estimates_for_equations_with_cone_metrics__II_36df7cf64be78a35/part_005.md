---
retention_scope: session
part: 5
total_parts: 5
---

[Part 5/5 of: Schauder estimates for equations with cone metrics, II]

4D2. The nonflat metric case. In this subsection, we will consider the case when the background metrics are general nonflat $\mathscr{C}_{\boldsymbol{\beta}}^{\boldsymbol{\alpha}, \boldsymbol{\alpha} / 2}$-conical Kähler metrics $g=g(z, t)$. Suppose $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$ satisfies the equation
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f \quad \text { in } \mathcal{Q}_{\beta},\left.\quad u\right|_{t=0}=0,$$
and $u \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right)$.
Proposition 4.26. There exists a constant $C=C(n, \boldsymbol{\beta}, \alpha, g)>0$ such that
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(B_{\beta}(0,1 / 2) \times[0,1 / 4]\right)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}\right) .$$
Proof. Choosing suitable complex coordinates at the origin $x=0$, we may assume the components of $g$ in the basis $\left\{\epsilon_{j} \wedge \bar{\epsilon}_{k}, \ldots\right\}$ satisfy $g_{\epsilon_{j} \bar{\epsilon}_{k}}(\cdot, 0)=\delta_{j k}$ and $g_{j \bar{k}}(\cdot, 0)=\delta_{j k}$ at the origin. As in the proof of Proposition 4.7, we can write (4-30) as
$$\frac{\partial u}{\partial t}=\Delta_{\beta} u+\eta \cdot \sqrt{-1} \partial \bar{\partial} u+f=: \Delta_{\beta} u+\hat{f},$$
where $\eta$ is given in the proof of Proposition 3.32. By (4-29) we get
$$[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{r}\right)} \leq C\left(\frac{\|u\|_{\mathscr{C}^{0}}\left(\widetilde{Q}_{R}\right)}{(R-r)^{2+\alpha}}+\frac{1}{(R-r)^{\alpha}}\|\hat{f}\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}+[\hat{f}]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}\right),$$
where $\widetilde{Q}_{R}:=B_{\beta}(0, R) \times\left[0, R^{2}\right]$. Observe that
$$\begin{aligned}
\frac{1}{(R-r)^{\alpha}}\|\hat{f}\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)} & \leq \frac{1}{(R-r)^{\alpha}}\|f\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}+\frac{1}{(R-r)^{\alpha}}\|\eta\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}\|T u\|_{C^{0}\left(\widetilde{Q}_{R}\right)} \\
& \leq \frac{1}{(R-r)^{\alpha}}\|f\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}+\frac{[\eta]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)} R^{\alpha}}{(R-r)^{\alpha}}\left(\varepsilon[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}+C(\varepsilon)\|u\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}\right)
\end{aligned}$$
and
$$\begin{aligned}
{[\hat{f}]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)} \leq } & {[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}+\|\eta\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}+\|T u\|_{\mathscr{C}^{0}}\left(\widetilde{Q}_{R}\right)[\eta]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)} } \\
\leq & {[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}+[\eta]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)} R^{\alpha}[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)} } \\
& \quad+[\eta]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}\left(\varepsilon[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}+C(\varepsilon)\|u\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}\right) .
\end{aligned}$$
By choosing $R_{0}=R_{0}(n, \boldsymbol{\beta}, \alpha, g)>0$ small enough and suitable $\varepsilon>0$, for any $0<r<R<R_{0}<\frac{1}{10}$, the combination of the above inequalities yields
$$[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{r}\right)} \leq \frac{1}{2}[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}+C\left(\frac{\|u\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}}{(R-r)^{2+\alpha}}+\frac{1}{(R-r)^{\alpha}}\|f\|_{\mathscr{C}^{0}\left(\widetilde{Q}_{R}\right)}+[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{R}\right)}\right) .$$
By Lemma 4.27 below (setting $\phi(r)=[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\widetilde{Q}_{r}\right)}$ ), we conclude that
$$[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}\left(0, R_{0} / 2\right) \times\left[0, R_{0}^{2} / 4\right]\right)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}\right) .$$
This is the desired estimate when the center of the ball is the worst possible. For the other balls $B_{\boldsymbol{\beta}}(x, r)$ with center $x \in B_{\beta}\left(0, \frac{1}{2}\right)$, we can repeat the above procedures and use the smooth coordinates $w_{j}=z_{j}^{\beta_{j}}$
in case the ball is disjoint from $\mathcal{S}_{j}$. Finitely many such balls cover $B_{\beta}\left(0, \frac{1}{2}\right)$, so we get
$$[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(0,1 / 2) \times[0,1 / 100]\right)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}\right) .$$
The proposition is proved by combining this inequality, the equation for $u$, interpolation inequalities, and the interior Schauder estimates in Corollary 4.9. \(\square\)

Lemma 4.27 [22, Lemma 4.3]. Let $\phi(t) \geq 0$ be bounded in [0, T]. Suppose, for any $0<t<s \leq T$, we have
$$\phi(t) \leq \frac{1}{2} \phi(s)+\frac{A}{(s-t)^{a}}+B$$
for some $a>0$ and $A, B>0$. Then it holds that, for any $0<t<s \leq T$,
$$\phi(t) \leq c(a)\left(\frac{A}{(s-t)^{a}}+B\right) .$$

Corollary 4.28. Suppose u satisfies the equations
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f \quad \text { in }\left.\mathcal{Q}_{\beta} \quad u\right|_{t=0}=u_{0} \in C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right) .$$
Then
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}\left(B_{\beta}(0,1 / 2) \times[0,1]\right)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}+\left\|u_{0}\right\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right)}\right)$$
for some constant $C=C(n, \boldsymbol{\beta}, \alpha, g)>0$.
Proof. We set $\hat{u}=u-u_{0}$ and $\hat{f}=f-\Delta_{g} u_{0} . \hat{u}$ satisfies the conditions in Proposition 4.26, so the corollary follows from Proposition 4.26 applied to $\hat{u}$ and triangle inequalities. \(\square\)

Corollary 4.29. In addition to the assumptions in Corollary 4.16, we also assume that $u_{0} \in C_{\beta}^{2, \alpha}(X)$. Then the weak solution to $\partial u / \partial t=\Delta_{g} u+f$ with $\left.u\right|_{t=0}=u_{0}$ exists and is in $\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}(X, \times[0,1])$. Moreover, there is a $C=C(n, \boldsymbol{\beta}, \alpha, g)>0$ such that
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}(X \times[0,1])} \leq C\left(\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(X \times[0,1])}+\left\|u_{0}\right\|_{C_{\beta}^{2, \alpha}(X)}\right) .$$
Proof. Observe that by the maximum principle we have
$$\|u\|_{\mathscr{C}^{0}(X \times[0,1])} \leq\|f\|_{\mathscr{C}^{0}(X \times[0,1])}+\left\|u_{0}\right\|_{C^{0}(X)} .$$
Then (4-31) follows from Corollary 4.28 and a covering argument as in the proof of Corollary 3.41. \(\square\)

\section*{5. Conical Kähler-Ricci flow}

Let $X$ be a compact Kähler manifold and $D=\sum_{j} D_{j}$ be a divisor with simple normal crossings. Let $\omega_{0}$ be a fixed $C_{\boldsymbol{\beta}}^{0, \alpha^{\prime}}(X)$ conical Kähler metric with cone angle $2 \pi \boldsymbol{\beta}$ along $D$ and $\hat{\omega}_{t}$ be a family of $\mathscr{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}$ conical metrics which are uniformly equivalent to $\omega_{0}$, with $\hat{\omega}_{0}=\omega_{0}$ and $\|\hat{\omega}\|_{\mathscr{C}_{\beta}^{\alpha^{\prime}, \alpha^{\prime} / 2}(X \times[0,1])} \leq C_{0}$. We consider the complex Monge-Ampère equation
$$\left\{\begin{array}{l}
\frac{\partial \varphi}{\partial t}=\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi\right)^{n}}{\omega_{0}^{n}}\right)+f, \\
\left.\varphi\right|_{t=0}=0,
\end{array}\right.$$
where $f \in \mathscr{C}^{\alpha^{\prime}, \alpha^{\prime} / 2_{\beta}(X \times[0,1])}$ is a given function. We will use an inverse function theorem argument from [4] which was outlined in [21] to show the short-time existence of the flow (5-1).

Theorem 5.1. There exists a small $T=T\left(n, \boldsymbol{\beta}, \omega_{0}, f, \alpha, \alpha^{\prime}\right)>0$ such that (5-1) admits a unique solution $\varphi \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}(X \times[0, T])$ for any $\alpha<\alpha^{\prime}$.
Proof. The uniqueness of the solution follows from the maximum principle. We will break the proof of short-time existence into three steps.
Step 1. Let $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha^{\prime},\left(2+\alpha^{\prime}\right) / 2}(X \times[0,1])$ be the solution to
$$\left\{\begin{array}{l}
\frac{\partial u}{\partial t}=\Delta_{g_{0}} u+f \quad \text { in } X \times[0,1], \\
\left.u\right|_{t=0}=0 .
\end{array}\right.$$
Thanks to Corollary 4.29, such a $u$ exists and satisfies the estimate (4-31). We fix $\varepsilon>0$, so that, as long as $\|\phi\|_{C_{\beta}^{2, \alpha}(X)} \leq \varepsilon$, we have that $\hat{\omega}_{t, \phi}:=\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \phi$ is equivalent to $\omega_{0}$, i.e.,
$$C_{0}^{-1} \omega_{0} \leq \omega_{0, \phi} \leq C_{0} \omega_{0} \quad \text { and } \quad\left\|\hat{\omega}_{t, \phi}\right\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}} \leq C_{0} .$$

We claim that, for $T_{1}>0$ small enough, $\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(X \times\left[0, T_{1}\right]\right)} \leq \varepsilon$. We first observe by (4-31) that
$$N:=\|u\|_{\mathscr{C}_{\beta}^{2+\alpha^{\prime},\left(\alpha^{\prime}+2\right) / 2}(X \times[0,1])} \leq C\|f\|_{\mathscr{C}_{\beta}^{\alpha^{\prime}, \alpha^{\prime} / 2}(X \times[0,1])} .$$
It suffices to show that $[u]_{\mathscr{C}_{\beta}^{2+\alpha^{\prime},\left(\alpha^{\prime}+2\right) / 2}}\left(X \times\left[0, T_{1}\right]\right)$ is small, since the lower-order derivatives are small because $\left.u\right|_{t=0}=0$. We calculate, for any $t_{1}, t_{2} \in\left[0, T_{1}\right]$,
$$\frac{\left|T u\left(x, t_{1}\right)-T u\left(x, t_{2}\right)\right|}{\left|t_{1}-t_{2}\right|^{\alpha / 2}}+\frac{\left|\dot{u}\left(x, t_{1}\right)-\dot{u}\left(x, t_{2}\right)\right|}{\left|t_{1}-t_{2}\right|^{\alpha / 2}} \leq N\left|t_{1}-t_{2}\right|^{\left(\alpha^{\prime}-\alpha\right) / 2} \leq \frac{1}{4} \varepsilon$$
if $N T_{1}^{\left(\alpha^{\prime}-\alpha\right) / 2}<\frac{1}{4} \varepsilon$. For any $x, y \in X$ and $t \in\left[0, T_{1}\right]$,
$$\frac{|T u(x, t)-T u(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} \leq N \min \left\{\frac{2 T_{1}^{\alpha^{\prime} / 2}}{d_{g_{0}}(x, y)^{\alpha}}, d_{g_{0}}(x, y)^{\alpha^{\prime}-\alpha}\right\} \leq \frac{1}{2} \varepsilon .$$
The claim then follows from the triangle inequality.
We define a function
$$w(x, t):=\frac{\partial u}{\partial t}(x, t)-\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} u\right)^{n}}{\omega_{0}^{n}}\right)(x, t)-f(x, t) \quad \text { for all }(x, t) \in X \times\left[0, T_{1}\right] \text {. }$$
It is clear that $w(x, 0) \equiv 0$.
Step 2: We consider the small ball
$$\mathcal{B}=\left\{\phi \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(X \times\left[0, T_{1}\right]\right) \mid\|\phi\|_{\mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}} \leq \varepsilon, \phi(\cdot, 0)=0\right\}$$
in the space $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(X \times\left[0, T_{1}\right]\right)$. Then $\left.u\right|_{t \in\left[0, T_{1}\right]} \in \mathcal{B}$ by the discussion in Step 1.
Define the differential map $\Psi: \mathcal{B} \rightarrow \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$ by
$$\Psi(\phi)=\frac{\partial \phi}{\partial t}-\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \phi\right)^{n}}{\omega_{0}^{n}}\right)-f .$$

The map $\Psi$ is well defined and $C^{1}$, where the differential $D \Psi_{\phi}$ at any $\phi \in \mathcal{B}$ is given by
$$D \Psi_{\phi}(v)=\frac{\partial v}{\partial t}-\left(\hat{g}_{\phi}\right)^{i \bar{j}} v_{i \bar{j}}=\frac{\partial v}{\partial t}-\Delta_{\hat{\omega}_{t, \phi}} v$$
for any
$$v \in T_{\phi} \mathcal{B}=\left\{v \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(X \times\left[0, T_{1}\right]\right) \mid v(\cdot, 0)=0\right\},$$
where $\left(\hat{g}_{\phi}\right)^{i \bar{j}}$ denotes the inverse of the metric $\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \phi$. As a linear map,
$$D \Psi_{\phi}: T_{\phi} \mathcal{B} \rightarrow \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$$
is injective by the maximum principle and surjective by Corollary 4.29. Thus $D \Psi_{\phi}$ is invertible at any $\phi \in \mathcal{B}$. In particular, $D \Psi_{u}$ is invertible, and by the inverse function theorem, $\Psi: \mathcal{B} \rightarrow \mathscr{C}_{\boldsymbol{\beta}}^{\boldsymbol{\alpha}, \boldsymbol{\alpha} / 2}\left(X \times\left[0, T_{1}\right]\right)$ defines a local diffeomorphism from a small neighborhood of $u \in \mathcal{B}$ to an open neighborhood of $w=\Psi(u)$ in $\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$. This implies that, for any $\tilde{w} \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$ with $\|w-\tilde{w}\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)}<\delta$ for some small $\delta>0$, there exists a unique $\varphi \in \mathcal{B}$ such that $\Psi(\varphi)=\tilde{w}$.

Step 3. For a small $T_{2}<T_{1}$ to be determined, we define a function
$$\tilde{w}(x, t)= \begin{cases}0, & t \in\left[0, T_{2}\right], \\ w\left(x, t-T_{2}\right), & t \in\left[T_{2}, T_{1}\right] .\end{cases}$$
Since $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha^{\prime},\left(2+\alpha^{\prime}\right) / 2}$, we see that $w \in \mathscr{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}\left(X \times\left[0, T_{1}\right]\right)$ with $M:=\|w\|_{\mathscr{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}}\left(X \times\left[0, T_{1}\right]\right)<\infty$. We claim that if $T_{2}$ is small enough, then $\|w-\tilde{w}\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)}<\delta$. We write $\eta=w-\tilde{w}$. It is clear from the fact that $w(\cdot, 0)=0$ that $\|\eta\|_{\mathscr{C}^{0}} \leq \frac{1}{2} \delta$ if $T_{2}$ is small enough.

Spatial directions: If $t<T_{2}$ then
$$\frac{|\eta(x, t)-\eta(y, t)|}{d_{g_{0}}(x, y)^{\alpha}}=\frac{|w(x, t)-w(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} \leq M \min \left\{\frac{2 T_{2}^{\alpha^{\prime} / 2}}{d_{g_{0}}(x, y)^{\alpha}}, d_{g_{0}}(x, y)^{\alpha^{\prime}-\alpha}\right\} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} .$$
If $t \in\left[T_{2}, T_{1}\right]$ then
$$\begin{aligned}
\frac{|\eta(x, t)-\eta(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} & =\frac{\left|w(x, t)-w(y, t)-w\left(x, t-T_{2}\right)+w\left(y, t-T_{2}\right)\right|}{d_{g_{0}}(x, y)^{\alpha}} \\
& \leq 2 M \min \left\{\frac{T_{2}^{\alpha^{\prime} / 2}}{d_{g_{0}}(x, y)^{\alpha}}, d_{g_{0}}(x, y)^{\alpha^{\prime}-\alpha}\right\} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} .
\end{aligned}$$
Time direction: If $t, t^{\prime}<T_{2}$ then
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}=\frac{\left|w(x, t)-w\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}} \leq M\left|t-t^{\prime}\right|^{\left(\alpha^{\prime}-\alpha\right) / 2} \leq M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} .$$
If $t, t^{\prime} \in\left[T_{2}, T_{1}\right]$ then
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}=\frac{\left|w(x, t)-w\left(x, t^{\prime}\right)-w\left(x, t-T_{2}\right)+w\left(x, t^{\prime}-T_{2}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} .$$

If $t<T_{2} \leq t^{\prime} \leq T_{1}$ then
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}=\frac{\left|w(x, t)-w\left(x, t^{\prime}\right)+w\left(x, t^{\prime}-T_{2}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} .$$

Therefore, if we choose $T_{2}>0$ small enough that $2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2}<\frac{1}{4} \delta$, then we have
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}+\frac{|\eta(x, t)-\eta(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} \leq \frac{1}{2} \delta \quad \text { for all } x \in X, \quad t, t^{\prime} \in\left[0, T_{1}\right] .$$
It then follows from the triangle inequality that
$$\begin{aligned}
\left|\eta(x, t)-\eta\left(y, t^{\prime}\right)\right| & \leq|\eta(x, t)-\eta(y, t)|+\left|\eta(y, t)-\eta\left(y, t^{\prime}\right)\right| \\
& \leq \frac{1}{2} \delta\left(d_{g_{0}}(x, y)^{\alpha}+\left|t-t^{\prime}\right|^{\alpha / 2}\right) \leq \frac{1}{2} \delta d_{\mathcal{P}, g_{0}}\left((x, t),\left(y, t^{\prime}\right)\right)^{\alpha} .
\end{aligned}$$

In conclusion, $\|\tilde{w}-w\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)}<\delta$, so by Step 2 we conclude that there exists a $\varphi \in \mathcal{B}$ such that $\Psi(\varphi)=\tilde{w}$. Since $\left.\tilde{w}\right|_{t \in\left[0, T_{2}\right]} \equiv 0$ by definition, $\left.\varphi\right|_{t \in\left[0, T_{2}\right]}$ satisfies (5-1) for $t \in[0, T]$, where $T:=T_{2}$. This shows the short-time existence of the flow (5-1). \(\square\)

Proof of Corollary 1.11. Recall that in (1-13) we wrote $\omega_{0}^{n}=\Omega / \prod_{j}\left(\left|s_{j}\right|_{h_{j}}^{2}\right)^{1-\beta_{j}}$, where $\Omega$ is a smooth volume form, $s_{j}$ and $h_{j}$ are holomorphic sections and hermitian metrics, respectively, of the line bundle associated to the component $D_{j}$. Choose a smooth reference form
$$\chi=\sqrt{-1} \partial \bar{\partial} \log \Omega-\sum_{j}\left(1-\beta_{j}\right) \sqrt{-1} \partial \bar{\partial} \log h_{j} .$$
Define the reference metrics $\hat{\omega}_{t}=\omega_{0}+t \chi$ which are $\mathscr{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}$-conical and Kähler for small $t>0$. Let $\varphi$ be the $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}$-solution to (1-11) with $f \equiv 0$. Then it is straightforward to check that $\omega_{t}=\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi$ satisfies the conical Kähler-Ricci flow equation (1-12) and $\omega \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}(X \times[0, T])$ for some small $T>0$.

The smoothness of $\omega$ in $X \backslash D \times(0, T]$ follows from the general smoothing properties of parabolic equations; see [37]. Taking $\partial / \partial t$ on both sides of (1-11) we get
$$\frac{\partial \dot{\varphi}}{\partial t}=\Delta_{\omega_{t}} \dot{\varphi}+\operatorname{tr}_{\omega_{t}} \chi \quad \text { and }\left.\quad \dot{\varphi}\right|_{t=0}=0 .$$
By Corollary 4.29, $\dot{\varphi} \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}(X \times[0, T])$ since $\operatorname{tr}_{\omega_{t}} \chi \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}(X \times[0, T])$. Therefore the normalized Ricci potential $\log \left(\omega_{t}^{n} / \omega_{0}^{n}\right)$ exists in $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}(X \times[0, T])$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] S. Brendle, "Ricci flat Kähler metrics with edge singularities", Int. Math. Res. Not. 2013:24 (2013), 5727-5766. MR Zbl
\item[] [2] L. A. Caffarelli, "Interior a priori estimates for solutions of fully nonlinear equations", Ann. of Math. (2) 130:1 (1989), 189-213. MR Zbl
\item[] [3] L. A. Caffarelli, "Interior $W^{2, p}$ estimates for solutions of the Monge-Ampère equation", Ann. of Math. (2) 131:1 (1990), 135-150. MR Zbl
\item[] [4] A. Chau and L.-F. Tam, "On a modified parabolic complex Monge-Ampère equation with applications", Math. Z. 269:3-4 (2011), 777-800. MR Zbl
\item[] [5] X. Chen and Y. Wang, "Bessel functions, heat kernel and the conical Kähler-Ricci flow", J. Funct. Anal. 269:2 (2015), 551-632. MR Zbl
\end{itemize}
\begin{itemize}
\item[] [6] X. Chen and Y. Wang, "On the long time behaviour of the conical Kähler-Ricci flows", J. Reine Angew. Math. 744 (2018), 165-199. MR Zbl
\item[] [7] X. Chen, S. Donaldson, and S. Sun, "Kähler-Einstein metrics on Fano manifolds, I: Approximation of metrics with cone singularities", J. Amer. Math. Soc. 28:1 (2015), 183-197. MR Zbl
\item[] [8] X. Chen, S. Donaldson, and S. Sun, "Kähler-Einstein metrics on Fano manifolds, II: Limits with cone angle less than $2 \pi$ ", J. Amer. Math. Soc. 28:1 (2015), 199-234. MR Zbl
\item[] [9] X. Chen, S. Donaldson, and S. Sun, "Kähler-Einstein metrics on Fano manifolds, III: Limits as cone angle approaches $2 \pi$ and completion of the main proof", J. Amer. Math. Soc. 28:1 (2015), 235-278. MR Zbl
\item[] [10] S. Y. Cheng and S. T. Yau, "Differential equations on Riemannian manifolds and their geometric applications", Comm. Pure Appl. Math. 28:3 (1975), 333-354. MR Zbl
\item[] [11] V. V. Datar, "On convexity of the regular set of conical Kähler-Einstein metrics", Math. Res. Lett. 23:1 (2016), 105-126. MR Zbl
\item[] [12] V. V. Datar and J. Song, "A remark on Kähler metrics with conical singularities along a simple normal crossing divisor", Bull. Lond. Math. Soc. 47:6 (2015), 1010-1013. MR Zbl
\item[] [13] V. Datar, B. Guo, J. Song, and X. Wang, "Connecting toric manifolds by conical Kähler-Einstein metrics", Adv. Math. 323 (2018), 38-83. MR Zbl
\item[] [14] S. K. Donaldson, "Kähler metrics with cone singularities along a divisor", pp. 49-79 in Essays in mathematics and its applications, edited by P. M. Pardalos and T. M. Rassias, Springer, 2012. MR Zbl
\item[] [15] G. Edwards, "A scalar curvature bound along the conical Kähler-Ricci flow", J. Geom. Anal. 28:1 (2018), 225-252. MR Zbl
\item[] [16] G. Edwards, "Metric contraction of the cone divisor by the conical Kähler-Ricci flow", Math. Ann. 374:3-4 (2019), 1525-1557. MR Zbl
\item[] [17] L. C. Evans, Partial differential equations, 2nd ed., Grad. Stud. Math. 19, Amer. Math. Soc., Providence, RI, 2010. MR Zbl
\item[] [18] D. Gilbarg and N. S. Trudinger, Elliptic partial differential equations of second order, Springer, 2001. MR Zbl
\item[] [19] H. Guenancia and M. Păun, "Conic singularities metrics with prescribed Ricci curvature: general cone angles along normal crossing divisors", J. Differential Geom. 103:1 (2016), 15-57. MR Zbl
\item[] [20] B. Guo and J. Song, "Schauder estimates for equations with cone metrics, I", Indiana Univ. Math. J. 70:5 (2021), 1639-1676. MR Zbl
\item[] [21] R. S. Hamilton, "Three-manifolds with positive Ricci curvature", J. Differential Geom. 17:2 (1982), 255-306. MR Zbl
\item[] [22] Q. Han and F. Lin, Elliptic partial differential equations, Courant Lect. Notes in Math. 1, Courant Inst. Math. Sci., New York, 1997. MR Zbl
\item[] [23] T. Jeffres, R. Mazzeo, and Y. A. Rubinstein, "Kähler-Einstein metrics with edge singularities", Ann. of Math. (2) 183:1 (2016), 95-176. MR Zbl
\item[] [24] X. Jin, J. Liu, and X. Zhang, "Twisted and conical Kähler-Ricci solitons on Fano manifolds", J. Funct. Anal. 271:9 (2016), 2396-2421. MR Zbl
\item[] [25] P. Li, Geometric analysis, Cambridge Stud. Adv. Math. 134, Cambridge Univ. Press, 2012. MR Zbl
\item[] [26] P. Li and S.-T. Yau, "On the parabolic kernel of the Schrödinger operator", Acta Math. 156:3-4 (1986), 153-201. MR Zbl
\item[] [27] G. M. Lieberman, Second order parabolic differential equations, World Sci., River Edge, NJ, 1996. MR Zbl
\item[] [28] F. Luo and G. Tian, "Liouville equation and spherical convex polytopes", Proc. Amer. Math. Soc. 116:4 (1992), 1119-1129. MR Zbl
\item[] [29] R. Mazzeo, "Kähler-Einstein metrics singular along a smooth divisor", exposé 6 in Journées équations aux dérivées partielles (Saint-Jean-de-Monts, France, 1999), Univ. Nantes, 1999. MR Zbl
\item[] [30] R. Mazzeo, Y. A. Rubinstein, and N. Sesum, "Ricci flow on surfaces with conic singularities", Anal. PDE 8:4 (2015), 839-882. MR Zbl
\end{itemize}
\begin{itemize}
\item[] [31] D. H. Phong, J. Song, J. Sturm, and X. Wang, "The Ricci flow on the sphere with marked points", J. Differential Geom. 114:1 (2020), 117-170. MR Zbl
\item[] [32] Y. A. Rubinstein, "Smooth and singular Kähler-Einstein metrics", pp. 45-138 in Geometric and spectral analysis (Montreal, 2012), edited by P. Albin et al., Contemp. Math. 630, Amer. Math. Soc., Providence, RI, 2014. MR Zbl
\item[] [33] M. V. Safonov, "The classical solution of the elliptic Bellman equation", Dokl. Akad. Nauk SSSR 278:4 (1984), 810-813. In Russian; translated in Soviet Math. Dokl. 30:2 (1984), 482-485. MR Zbl
\item[] [34] M. V. Safonov, "Classical solution of second-order nonlinear elliptic equations", Izv. Akad. Nauk SSSR Ser. Mat. 52:6 (1988), 1272-1287. In Russian; translated in Math. USSR-Izv. 33:3 (1989), 597-612. MR Zbl
\item[] [35] R. Schoen and S.-T. Yau, Lectures on differential geometry, Conf. Proc. Lect. Notes Geom. Topol. 1, International Press, Cambridge, MA, 1994. MR Zbl
\item[] [36] L. Simon, "Schauder estimates by scaling", Calc. Var. Partial Differential Equations 5:5 (1997), 391-407. MR Zbl
\item[] [37] J. Song and G. Tian, "The Kähler-Ricci flow through singularities", Invent. Math. 207:2 (2017), 519-595. MR Zbl
\item[] [38] J. Song and X. Wang, "The greatest Ricci lower bound, conical Einstein metrics and Chern number inequality", Geom. Topol. 20:1 (2016), 49-102. MR Zbl
\item[] [39] G. Tian, "Kähler-Einstein metrics on algebraic manifolds", pp. 143-185 in Transcendental methods in algebraic geometry (Cetraro, Italy, 1994), edited by F. Catanese and C. Ciliberto, Lecture Notes in Math. 1646, Springer, 1996. MR Zbl
\item[] [40] G. Tian, "K-stability and Kähler-Einstein metrics", Comm. Pure Appl. Math. 68:7 (2015), 1085-1156. MR Zbl
\item[] [41] M. Troyanov, "Prescribing curvature on compact surfaces with conical singularities", Trans. Amer. Math. Soc. 324:2 (1991), 793-821. MR Zbl
\item[] [42] X.-J. Wang, "Schauder estimates for elliptic and parabolic equations", Chinese Ann. Math. Ser. B 27:6 (2006), 637-642. MR Zbl
\item[] [43] S. T. Yau, "On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I", Comm. Pure Appl. Math. 31:3 (1978), 339-411. MR Zbl
\item[] [44] H. Yin, "Analysis aspects of Ricci flow on conical surfaces", Acta Math. Sin. (Engl. Ser.) 38:5 (2022), 807-857. MR Zbl
\item[] [45] H. Yin and K. Zheng, "Expansion formula for complex Monge-Ampère equation along cone singularities", Calc. Var. Partial Differential Equations 58:2 (2019), art. id. 50. MR Zbl
\end{itemize}

Received 23 Oct 2018. Revised 6 Jul 2022. Accepted 11 Aug 2022.
Bin Guo: bguo@rutgers.edu
Department of Mathematics, Columbia University, New York, NY, United States
Current address: Department of Mathematics \& Computer Science, Rutgers University, Newark, NJ, United States
Jian Song: jiansong@math.rutgers.edu
Department of Mathematics, Rutgers University, Piscataway, NJ, United States

\section*{Analysis \& PDE \\ msp.org/apde}

Editor-in-Chief
Clément Mouhot Cambridge University, UK
c.mouhot@dpmms.cam.ac.uk

Board of Editors

\begin{tabular}[t]{|l|l|l|l|}
\hline Massimiliano Berti & Scuola Intern. Sup. di Studi Avanzati, Italy berti@sissa.it & William Minicozzi II & Johns Hopkins University, USA minicozz@math.jhu.edu \\
\hline Zbigniew Błocki & Uniwersytet Jagielloński, Poland zbigniew.blocki@uj.edu.pl & Werner Müller & Universität Bonn, Germany mueller@math.uni-bonn.de \\
\hline Charles Fefferman & Princeton University, USA cf@math.princeton.edu & Igor Rodnianski & Princeton University, USA irod@math.princeton.edu \\
\hline David Gérard-Varet & Université de Paris, France david.gerard-varet@imj-prg.fr & Yum-Tong Siu & Harvard University, USA siu@math.harvard.edu \\
\hline Colin Guillarmou & Université Paris-Saclay, France colin.guillarmou@universite-paris-saclay.fr & Terence Tao & University of California, Los Angeles, USA tao@math.ucla.edu \\
\hline Ursula Hamenstaedt & Universität Bonn, Germany ursula@math.uni-bonn.de & Michael E. Taylor & Univ. of North Carolina, Chapel Hill, USA met@math.unc.edu \\
\hline Peter Hintz & ETH Zurich, Switzerland peter.hintz@math.ethz.ch & Gunther Uhlmann & University of Washington, USA gunther@math.washington.edu \\
\hline Vadim Kaloshin & Institute of Science and Technology, Austria vadim.kaloshin@gmail.com & András Vasy & Stanford University, USA andras@math.stanford.edu \\
\hline Izabella Laba & University of British Columbia, Canada ilaba@math.ubc.ca & Dan Virgil Voiculescu & University of California, Berkeley, USA dvv@math.berkeley.edu \\
\hline Anna L. Mazzucato & Penn State University, USA alm24@psu.edu & Jim Wright & University of Edinburgh, UK j.r.wright@ed.ac.uk \\
\hline Richard B. Melrose & Massachussets Inst. of Tech., USA rbm@math.mit.edu & Maciej Zworski & University of California, Berkeley, USA zworski@math.berkeley.edu \\
\hline Frank Merle & Université de Cergy-Pontoise, France merle@ihes.fr & & \\
\hline
\end{tabular}

\section*{PRODUCTION}
production@msp.org
Silvio Levy, Scientific Editor

See inside back cover or msp.org/apde for submission instructions.
The subscription price for 2024 is US $\$ 440 /$ year for the electronic version, and $\$ 690 /$ year ( $+\$ 65$, if shipping outside the US) for print and electronic. Subscriptions, requests for back issues from the last three years and changes of subscriber address should be sent to MSP.

Analysis \& PDE (ISSN 1948-206X electronic, 2157-5045 printed) at Mathematical Sciences Publishers, 798 Evans Hall \#3840, c/o University of California, Berkeley, CA 94720-3840, is published continuously online.

PUBLISHED BY
- mathematical sciences publishers nonprofit scientific publishing

\section*{Analysis \& PDE}

Volume 17 No. 32024
Schauder estimates for equations with cone metrics, II ..... 757
Bin Guo and Jian Song
The stability of simple plane-symmetric shock formation for three-dimensional compressible ..... 831
Euler flow with vorticity and entropy
Jonathan Luk and Jared Speck
Families of functionals representing Sobolev norms ..... 943
Haïm Brezis, Andreas Seeger, Jean Van Schaftingen and Po-Lam Yung
Schwarz-Pick lemma for harmonic maps which are conformal at a point ..... 981
Franc Forstnerič and David Kalaj
An improved regularity criterion and absence of splash-like singularities for g-SQG patches ..... 1005
Junekey Jeon and Andrej Zlatoš
Spectral gap for obstacle scattering in dimension 2 ..... 1019
Lucas Vacossin