---
retention_scope: session
part: 5
total_parts: 5
---

[Part 5/5 of: Schauder estimates for equations with cone metrics, II]

Proof. It follows from (4.27) and the elliptic Schauder estimates in Theorem 1.1 by adjusting $R$ slightly that for any $t \in\left[0, R^{2} / 4\right]$
$$\begin{aligned}
& \quad[T u(\cdot, t)]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(x, R / 2)\right)} \\
& \leq C\left(\frac{1}{R^{2+\alpha}}\|u\|_{\mathcal{C}^{0}\left(B_{\boldsymbol{\beta}}(x, R) \times\left[0, R^{2}\right]\right)}+\frac{1}{R^{\alpha}}\|f\|_{\mathcal{C}^{0}\left(B_{\boldsymbol{\beta}}(x, R) \times\left[0, R^{2}\right]\right)}+[f]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(B_{\boldsymbol{\beta}}(x, R) \times\left[0, R^{2}\right]\right)}\right),
\end{aligned}$$
that is, in the spatial variables the estimate (4.28) holds. It only remains to show the Hölder continuity of $T u$ in the time-variable. For this, we fix any two times $0 \leq t_{1}<t_{2} \leq R^{2} / 4$ and denote $r:=\sqrt{t_{2}-t_{1}} / 2$. For any $x_{0} \in B_{\boldsymbol{\beta}}(x, R / 4), B_{\boldsymbol{\beta}}\left(x_{0}, r\right) \subset B_{\boldsymbol{\beta}}(x, R / 2)$. By (4.27) and the equation for $u$, it is not hard to see that the inequality (4.27) holds when the $\Delta_{\boldsymbol{\beta}} u$ on LHS is replaced by $\dot{u}=\frac{\partial u}{\partial t}$. In particular
$$\frac{\mid \dot{u}(y, t)-\dot{u}\left(y, t_{1}\right)}{\left|t-t_{1}\right|^{\alpha / 2}} \leq A_{R}, \forall y \in B_{\boldsymbol{\beta}}(x, R / 2)$$
where $A_{R}:=$ the constant on the RHS of (4.27). Integrating over $t \in\left[t_{1}, t_{2}\right]$ we get
$$\left|u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(y, t_{1}\right)\left(t_{2}-t_{1}\right)\right| \leq C A_{R}\left(t_{2}-t_{1}\right)^{1+\frac{\alpha}{2}},$$
thus for any $y \in B_{\boldsymbol{\beta}}\left(x_{0}, r\right)$
$$\begin{aligned}
& \left|u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(x_{0}, t_{1}\right)\left(t_{2}-t_{1}\right)\right| \\
\leq & \left|u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(y, t_{1}\right)\left(t_{2}-t_{1}\right)\right|+\left|\dot{u}\left(x_{0}, t_{1}\right)-\dot{u}\left(y, t_{1}\right)\right|\left(t_{2}-t_{1}\right) \\
\leq & C A_{R}\left(t_{2}-t_{1}\right)^{1+\frac{\alpha}{2}}+A_{R} r^{\alpha}\left(t_{2}-t_{1}\right) .
\end{aligned}$$
Denote $\tilde{u}(y):=u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(x_{0}, t_{1}\right)\left(t_{2}-t_{1}\right)$, which is a function on $B_{\boldsymbol{\beta}}\left(x_{0}, r\right)$ and $\tilde{f}:=$ $\Delta_{\boldsymbol{\beta}} \tilde{u}=\Delta_{\boldsymbol{\beta}} u\left(\cdot, t_{2}\right)-\Delta_{\boldsymbol{\beta}} u\left(\cdot, t_{1}\right)$ satisfies $\|\tilde{f}\|_{C^{0}\left(B_{\boldsymbol{\beta}}\left(x_{0}, r\right)\right)} \leq A_{R}\left(t_{2}-t_{1}\right)^{\alpha}$ and $[\tilde{f}]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\left(x_{0}, r\right)\right)} \leq A_{R}$ by (4.27). It follows from the rescaled version of Proposition 3.6 that
$$\begin{aligned}
|T \tilde{u}|_{C^{0}\left(B_{\boldsymbol{\beta}}\left(x_{0}, r / 2\right)\right)} & \leq C(n, \boldsymbol{\beta}, \alpha)\left(\frac{\|\tilde{u}\|_{C^{0}\left(B_{\boldsymbol{\beta}}\left(x_{0}, r\right)\right)}}{r^{2}}+\|\tilde{f}\|_{C^{0}\left(B_{\boldsymbol{\beta}}\left(x_{0}, r\right)\right)}+r^{\alpha}[\tilde{f}]_{C^{0, \alpha}\left(B_{\boldsymbol{\beta}}\left(x_{0}, r\right)\right)}\right) \\
& \leq C\left(t_{2}-t_{1}\right)^{\alpha / 2} A_{R} .
\end{aligned}$$
Therefore for any $x_{0} \in B_{\boldsymbol{\beta}}(x, R / 4)$
$$\frac{\left|T u\left(x_{0}, t_{2}\right)-T u\left(x_{0}, t_{1}\right)\right|}{\left|t_{2}-t_{1}\right|^{\alpha / 2}} \leq C A_{R} .$$
It is then elementary to see by triangle inequality that (by adjusting $R$ slightly if necessary)
$$[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}}\left(B_{\boldsymbol{\beta}}(x, R / 2) \times\left[0, R^{2} / 4\right]\right) \leq C A_{R},$$
as desired. The estimate for $\dot{u}$ follows from the equation $\dot{u}=\Delta_{g} u+f$. \(\square\)

Remark 4.3. By a simple parabolic rescaling of the metric and time, we see from (4.28) that for any $0<r<R<1 / 10$ that
$$[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(Q_{r}\right)} \leq C\left(\frac{\|u\|_{\mathcal{C}^{0}\left(Q_{R}\right)}}{(R-r)^{2+\alpha}}+\frac{\|f\|_{\mathcal{C}^{0}\left(Q_{R}\right)}}{(R-r)^{\alpha}}+[f]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right) .$$
4.4.2. the non-flat metric case. In this subsection, we will consider the case when the background metrics are general non-flat $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}$-conical Kähler metrics $g=g(z, t)$. Suppose $u \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$ satisfies the equation
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f, \text { in } \mathcal{Q}_{\boldsymbol{\beta}},\left.\quad u\right|_{t=0}=0,$$
and $u \in \mathcal{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right)$.
Proposition 4.4. There exists a constant $C=C(n, \boldsymbol{\beta}, \alpha, g)>0$ such that
$$\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}}\left(B_{\boldsymbol{\beta}}(0,1 / 2) \times[0,1 / 4]\right) 0 \leq C\left(\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\|f\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}\right) .$$
Proof. Choose suitable complex coordinates at the origin $x=0$, we may assume the components of $g$ in the basis $\left\{\epsilon_{j} \wedge \bar{\epsilon}_{k}, \cdots\right\}$ satisfies $g_{\epsilon_{j} \bar{\epsilon}_{k}}(\cdot, 0)=\delta_{j k}$ and $g_{j \bar{k}}(\cdot, 0)=\delta_{j k}$ at the origin 0. As in the proof of Proposition 4.2, we can write the equation (4.30) as
$$\frac{\partial u}{\partial t}=\Delta_{\boldsymbol{\beta}} u+\eta \cdot \sqrt{-1} \partial \bar{\partial} u+f=: \Delta_{\boldsymbol{\beta}} u+\hat{f},$$
where $\eta$ is given in the proof of Proposition 3.6. By (4.29) we get
$$[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\tilde{Q}_{r}\right)} \leq C\left(\frac{\|u\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}}{(R-r)^{2+\alpha}}+\frac{1}{(R-r)^{\alpha}}\|\hat{f}\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}+[\hat{f}]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}\right),$$
where $\tilde{Q}_{R}:=B_{\boldsymbol{\beta}}(0, R) \times\left[0, R^{2}\right]$. Observe that
$$\begin{aligned}
\frac{1}{(R-r)^{\alpha}}\|\hat{f}\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)} & \leq \frac{1}{(R-r)^{\alpha}}\|f\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}+\frac{1}{(R-r)^{\alpha}}\|\eta\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}\|T u\|_{C^{0}\left(\tilde{Q}_{R}\right)} \\
& \leq \frac{1}{(R-r)^{\alpha}}\|f\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}+\frac{[\eta]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)} R^{\alpha}}{(R-r)^{\alpha}}\left(\varepsilon[T u]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}+C(\varepsilon)\|u\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}\right)
\end{aligned}$$
and
$$\begin{gathered}
{[\hat{f}]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)} \leq[f]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}+\|\eta\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}[T u]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}+\|T u\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}[\eta]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)} \leq[f]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}+[\eta]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)} R^{\alpha}[T u]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}} \\
+[\eta]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}\left(\varepsilon[T u]_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}+C(\varepsilon)\|u\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}\right) .
\end{gathered}$$
By choosing $R_{0}=R_{0}(n, \boldsymbol{\beta}, \alpha, g)>0$ small enough and suitable $\varepsilon>0$, for any $0<r<R<R_{0}<$ 1/10, the combination of the above inequalities yields that
$$[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\tilde{Q}_{r}\right)} \leq \frac{1}{2}[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}+C\left(\frac{\|u\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}}{(R-r)^{2+\alpha}}+\frac{1}{(R-r)^{\alpha}}\|f\|_{\mathcal{C}^{0}\left(\tilde{Q}_{R}\right)}+[f]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\tilde{Q}_{R}\right)}\right),$$
By Lemma 4.13 below (setting $\phi(r)=[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\tilde{Q}_{r}\right)}$ ), we conclude that
$$[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(B_{\boldsymbol{\beta}}\left(0, R_{0} / 2\right) \times\left[0, R_{0}^{2} / 4\right]\right)} \leq C\left(\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\|f\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}\right) .$$
This is the desired estimate when the center of the ball is the worst possible. For the other balls $B_{\boldsymbol{\beta}}(x, r)$ with center $x \in B_{\boldsymbol{\beta}}(0,1 / 2)$, we can repeat the above procedures and use the smooth coordinates $w_{j}=z_{j}^{\beta_{j}}$ in case the ball is disjoint with $\mathcal{S}_{j}$. Finitely many such balls cover $B_{\boldsymbol{\beta}}(0,1 / 2)$ so we get the
$$[T u]_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(B_{\boldsymbol{\beta}}(0,1 / 2) \times[0,1 / 100]\right)} \leq C\left(\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\|f\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}\right) .$$

The proposition is proved by combining this inequality, the equation for $u$, interpolation inequalities, and the interior Schauder estimates in Corollary 4.2. \(\square\)

Lemma 4.13 (Lemma 4.3 in [22]). Let $\phi(t) \geq 0$ be bounded in $[0, T]$. Suppose for any $0<t<s \leq T$ we have
$$\phi(t) \leq \frac{1}{2} \phi(s)+\frac{A}{(s-t)^{a}}+B$$
for some $a>0, A, B>0$. Then it holds that for any $0<t<s \leq T$
$$\phi(t) \leq c(a)\left(\frac{A}{(s-t)^{a}}+B\right) .$$

Corollary 4.7. Suppose $u$ satisfies the equation
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f, \text { in } \mathcal{Q}_{\boldsymbol{\beta}},\left.\quad u\right|_{t=0}=u_{0} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right),$$
then
$$\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}\left(B_{\boldsymbol{\beta}}(0,1 / 2) \times[0,1]\right)}} \leq C\left(\|u\|_{\mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\|f\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)}+\left\|u_{0}\right\|_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}\right),$$
for some constant $C=C(n, \boldsymbol{\beta}, \alpha, g)>0$.
Proof. We set $\hat{u}=u-u_{0}$ and $\hat{f}=f-\Delta_{g} u_{0}$. $\hat{u}$ satisfies the conditions in Proposition 4.4, so the corollary follows from Proposition 4.4 applied to $\hat{u}$ and triangle inequalities. \(\square\)

Corollary 4.8. Let the assumptions be as in Corollary 4.4 except that in addition we assume $u_{0} \in C_{\boldsymbol{\beta}}^{2, \alpha}(X)$. Then the weak solution to $\frac{\partial u}{\partial t}=\Delta_{g} u+f$ with $\left.u\right|_{t=0}=u_{0}$ exists and is in $\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}(X, \times[0,1])$. Moreover there is a $C=C(n, \boldsymbol{\beta}, \alpha, g)>0$ such that
$$\|u\|_{\mathcal{C}_{\beta}^{2+\alpha, \frac{2+\alpha}{2}}(X \times[0,1])} \leq C\left(\|f\|_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}(X \times[0,1])}+\left\|u_{0}\right\|_{C_{\beta}^{2, \alpha}(X)}\right) .$$

Proof. Observe that by maximum principle we have
$$\|u\|_{\mathcal{C}^{0}(X \times[0,1])} \leq\|f\|_{\mathcal{C}^{0}(X \times[0,1])}+\left\|u_{0}\right\|_{C^{0}(X)} .$$
Then the estimate (4.31) follows from Corollary 4.7 and a covering argument as in the proof of Corollary 3.4. \(\square\)

\section*{5. Conical Kähler-Ricci flow}

Let $X$ be a compact Kähler manifold and $D=\sum_{j} D_{j}$ be a divisor with simple normal crossings. Let $\omega_{0}$ be a fixed $C_{\boldsymbol{\beta}}^{0, \alpha^{\prime}}(X)$ conical Kähler metric with cone angle $2 \pi \boldsymbol{\beta}$ along $D$ and $\hat{\omega}_{t}$ be a family of $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \frac{\alpha^{\prime}}{2}}$ conical metrics which are uniformly equivalent to $\omega_{0}, \hat{\omega}_{0}=\omega_{0}$ and $\|\hat{\omega}\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}}(X \times[0,1]) \leq C_{0}$. We consider the complex Monge-Ampère equation:
$$\left\{\begin{array}{l}
\frac{\partial \varphi}{\partial t}=\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi\right)^{n}}{\omega_{0}^{n}}\right)+f \\
\left.\varphi\right|_{t=0} ^{n}=0,
\end{array}\right.$$
where $f \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}(X \times[0,1])$ is a given function. We will use an inverse function theorem argument in [4] which was outlined in [21] to show the short time existence of the flow (5.1).

Theorem 5.1. There exists a small $T=T\left(n, \boldsymbol{\beta}, \omega_{0}, f, \alpha, \alpha^{\prime}\right)>0$ such that the equation (5.1) admits a unique solution $\varphi \in \mathcal{C}_{\beta}^{2+\alpha, \frac{2+\alpha}{2}}(X \times[0, T])$, for any $\alpha<\alpha^{\prime}$.
Proof. The uniqueness of the solution follows from maximum principle. We will break the proof of short-time existence into three steps.
Step 1. Let $u \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha^{\prime}, \frac{2+\alpha^{\prime}}{2}}(X \times[0,1])$ be the solution to the equation
$$\left\{\begin{array}{l}
\frac{\partial u}{\partial t}=\Delta_{g_{0}} u+f, \quad \text { in } X \times[0,1] \\
\left.u\right|_{t=0}=0 .
\end{array}\right.$$
Thanks to Corollary 4.8 such $u$ exists and satisfies the estimate (4.31). We fix an $\varepsilon>0$ so that as long as $\|\phi\|_{C_{\boldsymbol{\beta}}^{2, \alpha}(X)} \leq \varepsilon, \hat{\omega}_{t, \phi}:=\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \phi$ is equivalent to $\omega_{0}$, i.e. $C_{0}^{-1} \omega_{0} \leq \omega_{0, \phi} \leq C_{0} \omega_{0}$, and $\left\|\hat{\omega}_{t, \phi}\right\|_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}} \leq C_{0}$.
We claim that for $T_{1}>0$ small enough, $\|u\|_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(X \times\left[0, T_{1}\right]\right)} \leq \varepsilon$. We firs observe that by (4.31) that
$$N:=\|u\|_{\mathcal{C}_{\beta}^{2+\alpha^{\prime}, \frac{\alpha^{\prime}+2}{2}(X \times[0,1])}} \leq C\|f\|_{\mathcal{C}_{\beta}^{\alpha^{\prime}, \alpha^{\prime} / 2}(X \times[0,1])} .$$
It suffices to show that $[u]_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha^{\prime}}, \frac{\alpha^{\prime}+2}{2}\left(X \times\left[0, T_{1}\right]\right)}$ is small since the lower order derivatives are small since $\left.u\right|_{t=0}=0$. We calculate for any $t_{1}, t_{2} \in\left[0, T_{1}\right]$
$$\frac{\left|T u\left(x, t_{1}\right)-T u\left(x, t_{2}\right)\right|}{\left|t_{1}-t_{2}\right|^{\alpha / 2}}+\frac{\left|\dot{u}\left(x, t_{1}\right)-\dot{u}\left(x, t_{2}\right)\right|}{\left|t_{1}-t_{2}\right|^{\alpha / 2}} \leq N\left|t_{1}-t_{2}\right|^{\left(\alpha^{\prime}-\alpha\right) / 2} \leq \varepsilon / 4,$$
if $N T_{1}^{\left(\alpha^{\prime}-\alpha\right) / 2}<\varepsilon / 4$. For any $x, y \in X$ and $t \in\left[0, T_{1}\right]$
$$\frac{|T u(x, t)-T u(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} \leq N \min \left\{\frac{2 T_{1}^{\alpha^{\prime} / 2}}{d_{g_{0}}(x, y)^{\alpha}}, d_{g_{0}}(x, y)^{\alpha^{\prime}-\alpha}\right\} \leq \frac{\varepsilon}{2} .$$
The claim then follows from triangle inequality.
We define a function
$$w(x, t):=\frac{\partial u}{\partial t}(x, t)-\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} u\right)^{n}}{\omega_{0}^{n}}\right)(x, t)-f(x, t), \forall(x, t) \in X \times\left[0, T_{1}\right] .$$
It is clear that $w(x, 0) \equiv 0$.
Step 2. We consider the small ball
$$\mathcal{B}=\left\{\left.\phi \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}\left(X \times\left[0, T_{1}\right]\right) \right\rvert\,\|\phi\|_{\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{\alpha+2}{2}}} \leq \varepsilon, \phi(\cdot, 0)=0\right\}$$
in the space $\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}\left(X \times\left[0, T_{1}\right]\right) .\left.u\right|_{t \in\left[0, T_{1}\right]} \in \mathcal{B}$ by the discussion in Step 1.
Define the differential map $\Psi: \mathcal{B} \rightarrow \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$ by
$$\Psi(\phi)=\frac{\partial \phi}{\partial t}-\log \left(\frac{\left(\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \phi\right)^{n}}{\omega_{0}^{n}}\right)-f .$$
The map $\Psi$ is well-defined and $C^{1}$ with the differential $D \Psi_{\phi}$ at any $\phi \in \mathcal{B}$ is given by
$$D \Psi_{\phi}(v)=\frac{\partial v}{\partial t}-\left(\hat{g}_{\phi}\right)^{i \bar{j}} v_{i \bar{j}}=\frac{\partial v}{\partial t}-\Delta_{\hat{\omega}_{t, \phi}} v,$$
for any $v \in T_{\phi} \mathcal{B}=\left\{\left.v \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}\left(X \times\left[0, T_{1}\right]\right) \right\rvert\, v(\cdot, 0)=0\right\}$, where $\left(\hat{g}_{\phi}\right)^{i \bar{j}}$ denotes the inverse of the metric $\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \phi$. As a linear map, $D \Psi_{\phi}: T_{\phi} \mathcal{B} \rightarrow \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$ is injective by maximum principle; is surjective by Corollary 4.8. Thus $D \Psi_{\phi}$ is invertible at any $\phi \in \mathcal{B}$. In particular $D \Psi_{u}$ is invertible and by inverse function theorem $\Psi: \mathcal{B} \rightarrow \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$ defines a local diffeomorphism from a small neighborhood of $u \in \mathcal{B}$ to an open neighborhood of $w=\Psi(u)$ in $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$. This implies that for any $\tilde{w} \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)$ with $\|w-\tilde{w}\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)}<\delta$ for some small $\delta>0$, there exists a unique $\varphi \in \mathcal{B}$ such that $\Psi(\varphi)=\tilde{w}$.

Step 3. For a small $T_{2}<T_{1}$ to be determined, we define a function
$$\tilde{w}(x, t)=\left\{\begin{array}{l}
0, \quad t \in\left[0, T_{2}\right] \\
w\left(x, t-T_{2}\right), \quad t \in\left[T_{2}, T_{1}\right] .
\end{array}\right.$$
Since $u \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha^{\prime}, \frac{2+\alpha^{\prime}}{2}}$, we see that $w \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}\left(X \times\left[0, T_{1}\right]\right)$ with $M:=\|w\|_{\mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}\left(X \times\left[0, T_{1}\right]\right)}<\infty$. We claim that if $T_{2}$ is small enough, then $\|w-\tilde{w}\|_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)}<\delta$. We denote $\eta=w-\tilde{w}$. It is clear from the fact that $w(\cdot, 0)=0$ that $\|\eta\|_{\mathcal{C}^{0}} \leq \delta / 2$ if $T_{2}$ is small enough.
Spatial directions: If $t<T_{2}$ then
$$\frac{|\eta(x, t)-\eta(y, t)|}{d_{g_{0}}(x, y)^{\alpha}}=\frac{|w(x, t)-w(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} \leq M \min \left\{\frac{2 T_{2}^{\alpha^{\prime} / 2}}{d_{g_{0}}(x, y)^{\alpha}}, d_{g_{0}}(x, y)^{\alpha^{\prime}-\alpha}\right\} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2},$$
if $t \in\left[T_{2}, T_{1}\right]$ then
$$\begin{aligned}
\frac{|\eta(x, t)-\eta(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} & =\frac{\left|w(x, t)-w(y, t)-w\left(x, t-T_{2}\right)+w\left(y, t-T_{2}\right)\right|}{d_{g_{0}}(x, y)^{\alpha}} \\
& \leq 2 M \min \left\{\frac{T_{2}^{\alpha^{\prime} / 2}}{d_{g_{0}}(x, y)^{\alpha}}, d_{g_{0}}(x, y)^{\alpha^{\prime}-\alpha}\right\} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2}
\end{aligned}$$
Time direction: If $t, t^{\prime}<T_{2}$, then
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}=\frac{\left|w(x, t)-w\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}} \leq M\left|t-t^{\prime}\right|^{\left(\alpha^{\prime}-\alpha\right) / 2} \leq M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} ;$$
If $t, t^{\prime} \in\left[T_{2}, T_{1}\right]$, then
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}=\frac{\left|w(x, t)-w\left(x, t^{\prime}\right)-w\left(x, t-T_{2}\right)+w\left(x, t^{\prime}-T_{2}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} ;$$
If $t<T_{2} \leq t^{\prime} \leq T_{1}$, then
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}=\frac{\left|w(x, t)-w\left(x, t^{\prime}\right)+w\left(x, t^{\prime}-T_{2}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}} \leq 2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2} .$$

Therefore if we choose $T_{2}>0$ small so that $2 M T_{2}^{\left(\alpha^{\prime}-\alpha\right) / 2}<\delta / 4$, then we have
$$\frac{\left|\eta(x, t)-\eta\left(x, t^{\prime}\right)\right|}{\left|t-t^{\prime}\right|^{\alpha / 2}}+\frac{|\eta(x, t)-\eta(y, t)|}{d_{g_{0}}(x, y)^{\alpha}} \leq \frac{\delta}{2}, \forall x \in X, t, t^{\prime} \in\left[0, T_{1}\right] .$$
It then follows from triangle inequality that
$$\left|\eta(x, t)-\eta\left(y, t^{\prime}\right)\right| \leq|\eta(x, t)-\eta(y, t)|+\left|\eta(y, t)-\eta\left(y, t^{\prime}\right)\right|$$
$$\begin{aligned}
& \leq \frac{\delta}{2}\left(d_{g_{0}}(x, y)^{\alpha}+\left|t-t^{\prime}\right|^{\alpha / 2}\right) \\
& \leq \delta / 2 d_{\mathcal{P}, g_{0}}\left((x, t),\left(y, t^{\prime}\right)\right)^{\alpha} .
\end{aligned}$$

In conclusion, $\|\tilde{w}-w\|_{\mathcal{C}_{\beta}^{\alpha, \alpha / 2}\left(X \times\left[0, T_{1}\right]\right)}<\delta$ so by Step 2, we conclude that there exists a $\varphi \in \mathcal{B}$ such that $\Psi(\varphi)=\tilde{w}$. Since $\left.\tilde{w}\right|_{t \in\left[0, T_{2}\right]} \equiv 0$ by definition, $\left.\varphi\right|_{t \in\left[0, T_{2}\right]}$ satisfies the equation (5.1) for $t \in[0, T]$, where $T:=T_{2}$. This shows the short-time existence of the flow (5.1). \(\square\)

Proof of Corollary 1.3. Recall in (1.13) we write $\omega_{0}^{n}=\frac{\Omega}{\prod_{j}\left(\left|s_{j}\right|_{h_{j}}^{2}\right)^{1-\beta_{j}}}$ where $\Omega$ is a smooth volume form, $s_{j}$ and $h_{j}$ are holomorphic sections and hermtian metrics of the line bundle associated to the component $D_{j}$, respectively. Choose a smooth reference form $\chi=\sqrt{-1} \partial \bar{\partial} \log \Omega-\sum_{j}(1-$ $\left.\beta_{j}\right) \sqrt{-1} \partial \bar{\partial} \log h_{j}$. Define the reference metrics $\hat{\omega}_{t}=\omega_{0}+t \chi$ which are $\mathcal{C}_{\boldsymbol{\beta}}^{\alpha^{\prime}, \alpha^{\prime} / 2}$-conical and Kähler for small $t>0$. Let $\varphi$ be the $\mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}$-solution to the equation (1.11) with $f \equiv 0$. Then it is straightforward to check that $\omega_{t}=\hat{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi$ satisfies the conical Kähler-Ricci flow equation (1.12) and $\omega \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}(X \times[0, T])$ for some small $T>0$.

The smoothness of $\omega$ in $X \backslash D \times(0, T]$ follows from the general smoothing properties of parabolic equations (see [37]). Taking $\frac{\partial}{\partial t}$ on both sides of (1.11) we get
$$\frac{\partial \dot{\varphi}}{\partial t}=\Delta_{\omega_{t}} \dot{\varphi}+\operatorname{tr}_{\omega_{t}} \chi, \text { and }\left.\dot{\varphi}\right|_{t=0}=0 .$$
By Corollary 4.8, $\dot{\varphi} \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}(X \times[0, T])$ since $\operatorname{tr}_{\omega_{t}} \chi \in \mathcal{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}(X \times[0, T])$. Therefore the normalized Ricci potential $\log \left(\frac{\omega_{t}^{n}}{\omega_{0}^{n}}\right) \in \mathcal{C}_{\boldsymbol{\beta}}^{2+\alpha, \frac{2+\alpha}{2}}(X \times[0, T])$. \(\square\)

Acknowledgements: Both authors thank Duong H. Phong and Ved Datar for many insightful discussions.

\section*{References}
\begin{itemize}
\item[] [1] Brendle, S. Ricci flat Kähler metrics with edge singularities, Int. Math. Res. Not. IMRN 2013, no. 24, 5727-5766
\item[] [2] Caffarelli, L.A. Interior a priori estimates for solutions of fully nonlinear equations, Ann. of Math. (2) 130 (1989), 189-213
\item[] [3] Caffarelli, L.A. Interior $W^{2, p}$ estimates for solutions of Monge-Ampère equations, Ann. Math., 131(1990), 135-150
\item[] [4] Chau, A., Tam, L.-F. On a modified parabolic complex Monge-Ampère equation with applications. Math. Z. 269 (2011), no. 3-4, 777-800.
\item[] [5] Chen, X.X., Donaldson, S.K. and Sun, S. Kähler-Einstein metrics on Fano manifolds, I: approximation of metrics with cone singularities, J. Amer. Math. Soc. 28 (2015), no. 1, 183-197.
\item[] [6] Chen, X.X., Donaldson, S.K. and Sun, S. Kähler-Einstein metrics on Fano manifolds, II: limits with cone angle less than $2 \pi$, J. Amer. Math. Soc. 28 (2015), no. 1, 199-234
\item[] [7] Chen, X.X., Donaldson, S.K. and Sun, S. Kähler-Einstein metrics on Fano manifolds, III: limits as cone angle approaches $2 \pi$ and completion of the main proof, J. Amer. Math. Soc. 28 (2015), no. 1, 235-278
\item[] [8] Chen, X.X. and Wang, Y. Bessel functions, heat kernel and the conical Kähler-Ricci flow. J. Funct. Anal. 269 (2015), no. 2, 551-632
\item[] [9] Chen, X.X. and Wang, Y. On the long time behaviour of the Conical Kähler-Ricci flows Journal für die reine und angewandte Mathematik (Crelles Journal), DOI: 10.1515/crelle-2015-0103
\end{itemize}
[10] Cheng, S.-Y. and Yau, S.-T. Differential equations on Riemannian manifolds and their geometric applications. Comm. Pure Appl. Math. 28 (1975), no. 3, 333-354
[11] Datar, V. On convexity of the regular set of conical Kähler-Einstein metrics, Math. Res. Lett. 23 (2016), no. 1, 105-126
[12] Datar, V. and Song, J. A remark on Kähler metrics with conical singularities along a simple normal crossing divisor, Bull. Lond. Math. Soc. 47 (2015), no. 6, 1010-1013
[13] Datar, V., Guo, B., Song, J. and Wang, X. Connecting toric manifolds by conical Kähler-Einstein metrics. Adv. Math. 323 (2018), 38-83.
[14] Donaldson, S. K. Kähler metrics with cone singularities along a divisor. Essays in mathematics and its applications, 49-79, Springer, Heidelberg, 2012
[15] Edwards, G. A scalar curvature bound along the conical Kähler-Ricci flow, J. Geom. Anal. 28 (2018), no. 1, 225-252.
[16] Edwards, G. Metric contraction of the cone divisor by the conical Kähler-Ricci flow. arXiv: 1704.00360.
[17] Evans, L. C. Partial differential equations. Second edition. Graduate Studies in Mathematics, 19. American Mathematical Society, Providence, RI, 2010. xxii+749 pp.
[18] Guenancia, H. and Paun, M. Conic singularities metrics with prescribed Ricci curvature: general cone angles along normal crossing divisors, J. Differential Geom. 103 (2016), no. 1, 15-57
[19] Gilbarg, D. and Trudinger, N. S. Elliptic partial differential equations of second order. Reprint of the 1998 edition. Classics in Mathematics. Springer-Verlag, Berlin, 2001. xiv+517 pp.
[20] Guo, B. and Song, J. Schauder estimates for equations with cone metrics, I, arXiv:1612.00075
[21] Hamilton, R.S. Three-manifolds with positive Ricci curvature. J. Differ. Geom. 17, 255-306 (1982)
[22] Han, Q. and Lin, F. Elliptic partial differential equations. Second edition. Courant Lecture Notes in Mathematics, 1. Courant Institute of Mathematical Sciences, New York; American Mathematical Society, Providence, RI, 2011. x+147 pp.
[23] Jeffres, T., Mazzeo, R. and Rubinstein, Y. Kähler-Einstein metrics with edge singularities with appendix by Rubinstein Y. and Li, C., Ann. of Math. (2) 183 (2016), no. 1, 95-176
[24] Jin, X., Liu, J. and Zhang, X. Twisted and conical Kähler-Ricci solitons on Fano manifolds, J. Funct. Anal. 271 (2016), no. 9, 2396-2421
[25] Li, P. Geometric analysis. Cambridge Studies in Advanced Mathematics, 134. Cambridge University Press, Cambridge, 2012. x+406 pp.
[26] Li, P. and Yau, S.-T. On the parabolic kernel of the Schrödinger operator. Acta Math. 156 (1986), no. 3-4, 153-201
[27] Lieberman, G. M. Second order parabolic differential equations. World Scientific, 1996. xii+439 pp.
[28] Luo, F. and Tian, G. Liouville equation and spherical convex polytopes, Proc. Amer. Math. Soc. 116 (1992), 1119-1129
[29] Mazzeo, R. Kähler-Einstein metrics singular along a smooth divisor, Journées Eq́uations aux dérivées partielles (1999), 1-10
[30] Phong, D. H., Song, J., Sturm, J. and Wang, X. The Ricci flow on the sphere with marked points, preprint arXiv:1407.1118.
[31] Rubinstein, Y. Smooth and singular Kähler-Einstein metrics, Geometric and spectral analysis, 45-138, Contemp. Math., 630, Amer. Math. Soc., Providence, RI, 2014
[32] Mazzeo, R., Rubinstein, Y. and Sesum, N. Ricci flow on surfaces with conic singularities, Anal. PDE 8 (2015), no. 4, 839-882
[33] Safonov, M.V. The classical solution of the elliptic Bellman equation, Dokl. Akad. Nauk SSSR 278(1984), 810-813; English translation in Soviet Math Doklady 30(1984), 482-485
[34] Safonov, M.V. Classical solution of second-order nonlinear elliptic equations, Izv. Akad. Nauk SSSR Ser. Mat. 52(1988), 1272-1287; English translation in Math. USSR-Izv. 33(1989), 597-612
[35] Schoen, R. and Yau, S.-T. Lectures on differential geometry, Conference Proceedings and Lecture Notes in Geometry and Topology, I. International Press, Cambridge, MA, 1994. v+235 pp.
[36] Simon, L. Schauder estimates by scaling, Calc. Var. PDE, 5(1997), 391-407
[37] Song, J. and Tian, G. The Kähler-Ricci flow through singularities. Invent. Math. 207 (2017), no. 2, 519-595.
[38] Song, J. and Wang, X. The greatest Ricci lower bound, conical Einstein metrics and Chern number inequality, Geom. Topol. 20 (2016), no. 1, 49-102
\begin{itemize}
\item[] [39] Tian, G. Kähler-Einstein metrics on algebraic manifolds, Transcendental methods in algebraic geometry, 143 - 185, Lecture Notes in Math., 1646, Springer, Berlin, 1996
\item[] [40] Tian, G. K-stability and Kähler-Einstein metrics, Comm. Pure Appl. Math. 68 (2015), no. 7, 1085-1156
\item[] [41] Troyanov, M. Prescribing curvature on compact surfaces with conic singularities, Trans. Amer. Math. Soc. 324 (1991), 793-821
\item[] [42] Wang, X.-J. Schauder estimates for elliptic and parabolic equations, Chinese Ann. Math. Ser. B 27 (2006), no. 6, 637-642
\item[] [43] Yau, S.-T. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411
\item[] [44] Yin, H. Analysis aspects of Ricci flow on conical surfaces, preprint arXiv:1605.08836
\item[] [45] Yin, H. and Zheng, K. Expansion formula for complex Monge-Ampère equation along cone singularities, preprint arXiv:1609.03111
\item[] Department of Mathematics, Columbia University, New York, NY 10027
E-mail address: bguo@math.columbia.edu
\item[] Department of Mathematics, Rutgers University, Piscataway, NJ 08854
E-mail address: jiansong@math.rutgers.edu
\end{itemize}