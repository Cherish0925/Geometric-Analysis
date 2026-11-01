---
retention_scope: session
part: 2
total_parts: 5
---

[Part 2/5 of: Schauder estimates for equations with cone metrics, II]

Case 1: $q \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$, i.e., $z_{1}(q)=z_{2}(q)=0$. Consider the point
$$q^{\prime}=-q \in \partial B_{\beta}(0,1) \cap \partial B_{\mathbb{C}^{n}}(0,1) .$$
Since $q$ is the unique farthest point from $q^{\prime}$ on $\partial B_{\beta}(0,1)$ under the Euclidean distance, the function $\Psi_{q}(z):=d_{\mathbb{C}^{n}}\left(z, q^{\prime}\right)^{2}-4$ satisfies $\Psi_{q}(q)=0$ and $\Psi_{q}(z)<0$ for all $z \in \partial B_{\beta}(0,1) \backslash\{q\}$. By the continuity of $\varphi$ for any $\delta>0$, there is a small neighborhood $V$ of $q$ such that $\varphi(q)-\delta<\varphi(z)<\varphi(q)+\delta$ for all $z \in \partial B_{\beta}(0,1) \cap V$, and, on $\partial B_{\beta}(0,1) \backslash V$, we have that $\Psi_{q}$ is bounded above by a negative constant. Hence we can define
$$\varphi_{q}(z):=\varphi(q)-\delta+A \Psi_{q}(z)<\varphi(z)$$
for all $z \in \partial B_{\beta}(0,1)$ if $A$ is chosen large enough. The function $\varphi_{q}$ is $\Delta_{g_{\epsilon}}$-subharmonic; hence by the maximum principle we have $u_{\epsilon}(z) \geq \varphi_{q}(z)$ for all $z \in B_{\beta}(0,1)$. Letting $\epsilon \rightarrow 0$ we get $u(z) \geq \varphi_{q}(z)$, taking $z \rightarrow q$ we have $\liminf _{z \rightarrow q} u(z) \geq \varphi(q)-\delta$, and since $\delta>0$ is arbitrary we have $\liminf _{z \rightarrow q} u(z) \geq \varphi(q)$.

By considering the barrier function $\varphi(q)+\delta-A \Psi_{q}(z)$ and using a similar argument it is not hard to see that $\limsup _{z \rightarrow q} u(z) \leq \varphi(q)$; hence $\lim _{z \rightarrow q} u(z)=\varphi(q)$ and $u$ is continuous up to $q \in \partial B_{\beta}(0,1)$.

Case 2: $q \in \partial B_{\beta}(0,1) \backslash \mathcal{S}_{1} \cap \mathcal{S}_{2}$. We first consider the case when $z_{1}(q) \neq 0$ and $z_{2}(q) \neq 0$. The boundary $\partial B_{\beta}(0,1)$ is smooth near $q$, and hence satisfies the exterior sphere condition. We choose an exterior Euclidean ball $B_{\mathbb{C}^{n}}\left(\tilde{q}, r_{q}\right)$ which is tangential to $\partial B_{\beta}(0,1)$ (only) at $q$, i.e., under the Euclidean distance, $q$ is the unique closest point to $\tilde{q}$ on $\partial B_{\beta}(0,1)$. So the function
$$G(z)=\frac{1}{|z-\tilde{q}|^{2 n-2}}-\frac{1}{r_{q}^{2 n-2}}$$
satisfies $G(q)=0$ and $G(z)<0$ for all $z \in \partial B_{\beta}(0,1) \backslash\{q\}$. We calculate
$$\begin{aligned}
\Delta_{g_{\epsilon}} G & =\left(\left|z_{1}\right|^{2}+\epsilon\right)^{-\beta_{1}+1} \frac{\partial^{2} G}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{-\beta_{2}+1} \frac{\partial^{2} G}{\partial z_{2} \partial \bar{z}_{2}}+\sum_{k=3}^{n} \frac{\partial^{2} G}{\partial z_{k} \partial \bar{z}_{k}} \\
& =\left(\left(\left|z_{1}\right|^{2}+\epsilon\right)^{-\beta_{1}+1}-1\right) \frac{\partial^{2} G}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left(\left|z_{2}\right|^{2}+\epsilon\right)^{-\beta_{2}+1}-1\right) \frac{\partial^{2} G}{\partial z_{2} \partial \bar{z}_{2}} \\
& =\sum_{k=1}^{2}(-n+1) \frac{\left(\left|z_{k}\right|^{2}+\epsilon\right)^{-\beta_{k}+1}-1}{|z-\tilde{q}|^{2 n}}\left(-\frac{n\left|z_{k}-\tilde{q}_{k}\right|^{2}}{|z-\tilde{q}|^{2}}+1\right) \geq-C\left(q, r_{q}\right) .
\end{aligned}$$
The function
$$\Psi_{q}(z)=A\left(d_{\beta}(z, 0)^{2}-1\right)+G(z)$$
is $\Delta_{g_{\epsilon}}$-subharmonic for $A \gg 1$, and $\Psi_{q}(q)=0$ and $\Psi_{q}(z)<0$ for all $z \in \partial B_{\boldsymbol{\beta}}(0,1) \backslash\{q\}$. We are in the same situation as Case 1, so by the same argument as above, we can show the continuity of $u$ at such a boundary point $q$.

In the case when $z_{1}(q) \neq 0$ and $z_{2}(q)=0$, the boundary $\partial B_{\beta}(0,1)$ is not smooth at $q$ and we cannot apply the exterior sphere condition to construct the barrier. Instead we use the geometry of the metric ball $B_{\beta}(0,1)$. Consider the standard cone metric
$$g_{\beta_{1}}=\beta_{1}^{2} \frac{d z_{1} \otimes d \bar{z}_{1}}{\left|z_{1}\right|^{2\left(1-\beta_{1}\right)}}+\sum_{k=2}^{n} d z_{k} \otimes d \bar{z}_{k}$$
with cone singularity only along $\mathcal{S}_{1}=\left\{z_{1}=0\right\}$. We observe that the metric ball $B_{\boldsymbol{\beta}}(0,1)$ is strictly contained in $B_{g_{\beta_{1}}}(0,1)$, and the boundaries of these balls are tangential at the points with vanishing $z_{2}$-coordinate. Thus $q \in \partial B_{\beta}(0,1) \cap \partial B_{g_{\beta_{1}}}(0,1)$ and $\partial B_{g_{\beta_{1}}}(0,1)$ is smooth at $q$, so there exists an exterior sphere for $\partial B_{g_{\beta_{1}}}(0,1)$ at $q$. We define a similar function $G(z)$ as in (3-37), and, by the strict inclusion of the metric balls $B_{\beta}(0,1) \subset B_{g_{\beta_{1}}}(0,1)$, it follows that $G(q)=0$ and $G(z)<0$ for all $z \in \partial B_{\beta}(0,1) \backslash\{q\}$. The remaining argument is the same as before. \(\square\)

Remark 3.6. For any constant $c \in \mathbb{R}$, the Dirichlet boundary value problem
$$\Delta_{g_{\beta}} u=c \quad \text { in } B_{\beta}(0,1) \backslash \mathcal{S} \quad \text { and } \quad u=\varphi \quad \text { on } \partial B_{\beta}(0,1)$$
admits a solution $u \in C^{2}\left(B_{\beta} \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\beta}}\right)$ for any given $\varphi \in C^{0}\left(\partial B_{\beta}\right)$. This follows from the solution $\tilde{u}$ of (3-1) with boundary value $\tilde{\varphi}=\varphi-\frac{1}{2} c(n-2)^{-1} \sum_{j=5}^{2 n} s_{j}^{2}$. Then the function $u=\tilde{u}+\frac{1}{2} c(n-2)^{-1} \sum_{j} s_{j}^{2}$ solves the equation above.

For later application, we prove the existence of solutions for a more general right-hand side of the Laplace equation with the standard background metric. This result is not needed to prove Theorem 1.2.
Proposition 3.7. For any given $\varphi \in C^{0}\left(\partial B_{\beta}(0,1)\right)$ and $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$, the Dirichlet boundary value problem
$$\begin{cases}\Delta_{g_{\beta}} v=f & \text { in } B_{\beta}(0,1) \backslash \mathcal{S}, \\ v=\varphi & \text { on } \partial B_{\beta}(0,1)\end{cases}$$
admits a unique solution $v \in C^{2}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\beta}(0,1)}\right)$.
By Theorem 1.2, the solution $v$ to (3-38) belongs to $C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$.
Proof. The proof is similar to that of Proposition 3.5. As before, let $g_{\epsilon}$ be the approximating metrics (3-3) of $g_{\beta}$ which are smooth metrics on $B_{\beta}(0,1)$. By standard elliptic theory we can solve the equations
$$\begin{cases}\Delta_{g_{\epsilon}} v_{\epsilon}=f & \text { in } B_{\beta}(0,1), \\ v_{\epsilon}=\varphi & \text { on } \partial B_{\beta}(0,1) .\end{cases}$$
For any compact subset $K \Subset B_{\beta}(0,1)$ and small $\delta>0$, we have a uniform $C^{2, \alpha^{\prime}}$-bound of $v_{\epsilon}$ on $K \backslash T_{\delta}(\mathcal{S})$ for some $\alpha^{\prime}<\alpha$. Thus $v_{\epsilon}$ converges in the $C^{2, \alpha^{\prime}}$-norm to a function $v$ on $K \backslash T_{\delta}(\mathcal{S})$ as $\epsilon \rightarrow 0$. By a standard diagonal argument, letting $K \rightarrow B_{\beta}(0,1)$ and $\delta \rightarrow 0$, we can achieve
$$v_{\epsilon} \xrightarrow{C_{\text {loc }}^{2, \alpha^{\prime}}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right)} v \in C_{\text {loc }}^{2, \alpha^{\prime}}\left(B_{\beta}(0,1) \backslash \mathcal{S}\right) \quad \text { as } \epsilon \rightarrow 0 .$$
Clearly $v$ satisfies (3-38) in $B_{\beta}(0,1) \backslash \mathcal{S}$. It only remains to show the boundary value of $v$ coincides with $\varphi$ and $v$ is globally continuous in $B_{\beta}(0,1)$.
Global continuity: $v \in C^{0}\left(B_{\beta}(0,1)\right)$. It suffices to show $v$ is continuous at any $p \in \mathcal{S} \cap B_{\beta}(0,1)$. Fix such a point $p$ and take $R_{0}>0$ small enough that $B_{\mathbb{C}^{n}}\left(p, 10 R_{0}\right) \cap \partial B_{\beta}(0,1)=\varnothing$. We observe that $\frac{1}{2} g_{\mathbb{C}^{n}} \leq g_{\epsilon} \leq g_{\boldsymbol{\beta}}$, so for any $r \in\left(0, \frac{1}{2}\right)$,
$$B_{g_{\beta}}(p, r) \subset B_{g_{\epsilon}}(p, r) \subset B_{\mathbb{C}^{n}}(p, 2 r) .$$
In particular, the balls $B_{g_{\epsilon}}\left(p, 5 R_{0}\right)$ are also disjoint with $\partial B_{\beta}(0,1)$.
Since $\operatorname{Ric}\left(g_{\epsilon}\right) \geq 0$, we have the following Sobolev inequality [25]: there exists a constant $C=C(n)>0$ such that, for any $h \in C_{0}^{1}\left(B_{g_{\epsilon}}(p, r)\right)$,
$$\left(\int_{B_{g_{\epsilon}}(p, r)} h^{2 n /(n-1)} \omega_{\epsilon}^{n}\right)^{(n-1) / n} \leq C\left(\frac{r^{2 n}}{\operatorname{Vol}_{g_{\epsilon}}\left(B_{g_{\epsilon}}(p, r)\right)}\right)^{1 / n} \int_{B_{g \epsilon}(p, r)}|\nabla h|_{g_{\epsilon}}^{2} \omega_{\epsilon}^{n} .$$
It can be checked by straightforward calculations that $\operatorname{Vol}_{g_{\epsilon}}\left(B_{g_{\epsilon}}(p, 1)\right) \geq c_{0}(n)>0$ for some constant $c_{0}$ independent of $\epsilon$. Then Bishop's volume comparison yields, for any $r \in(0,1)$,
$$C_{1}(n) r^{2 n} \geq \operatorname{Vol}_{g_{\epsilon}}\left(B_{g_{\epsilon}}(p, r)\right) \geq c_{1}(n) r^{2 n} .$$
Thus the Sobolev inequality ( $3-41$ ) is reduced to
$$\left(\int_{B_{g_{\epsilon}}(p, r)} h^{2 n /(n-1)} \omega_{\epsilon}^{n}\right)^{(n-1) / n} \leq C \int_{B_{g_{\epsilon}}(p, r)}|\nabla h|_{g_{\epsilon}}^{2} \omega_{\epsilon}^{n} \quad \text { for all } h \in C_{0}^{1}\left(B_{g_{\epsilon}}(p, r)\right) .$$

With (3-42) at hand, we can apply the same proof of the standard De Giorgi-Nash-Moser theory (see the proof of Corollary 4.18 in [22]) to derive the uniform Hölder continuity of $v_{\epsilon}$ at $p$, i.e., there exists a constant $C=C\left(n, \boldsymbol{\beta}, R_{0}\right)>0$ such that
$$\operatorname{osc}_{B_{\beta}(p, r)} v_{\epsilon} \leq \operatorname{osc}_{B_{g \epsilon}(p, r)} v_{\epsilon} \leq C r^{\alpha^{\prime \prime}} \quad \text { for all } r \in\left(0, R_{0}\right)$$
for some $\alpha^{\prime \prime}=\alpha^{\prime \prime}\left(n, \boldsymbol{\beta}, R_{0}\right) \in(0,1)$, where in the first inequality we use the relation (3-40). Letting $\epsilon \rightarrow 0$ we see the continuity of $v$ at $p$.

Boundary value: $v=\varphi$ on $\partial B_{\beta}(0,1)$. The proof is almost identical to that of Proposition 3.5. For example, the function $\varphi_{q}(z)=\varphi(q)-\delta+A \Psi_{q}(z)$ defined in Case 1 in the proof of Proposition 3.5 satisfies $\Delta_{g_{\epsilon}} \varphi_{q}(z) \geq \max _{X} f$ if $A>0$ is taken large enough. Then from $\Delta_{g_{\epsilon}}\left(\varphi_{q}-v_{\epsilon}\right) \geq 0$ in $B_{\beta}$ and $\varphi_{q}-\varphi \leq 0$ on $\partial B_{\boldsymbol{\beta}}$, applying the maximum principle we get $\varphi_{q} \leq v_{\epsilon}$ in $B_{\boldsymbol{\beta}}(0,1)$. The remaining arguments are the same as in Proposition 3.5. Case 2 can be dealt with similarly. \(\square\)

Remark 3.8. Let $H_{0}^{1}\left(B_{\beta}(0,1), g_{\beta}\right)$ be the completion of the space of $C_{0}^{1}\left(B_{\beta}(0,1)\right)$-functions under the norm
$$\|\nabla u\|_{L^{2}\left(g_{\beta}\right)}=\left(\int_{B_{\beta}(0,1)}|\nabla u|_{g_{\beta}}^{2} \omega_{\beta}^{n}\right)^{1 / 2} .$$
For any $h \in C_{0}^{1}\left(B_{\beta}(0,1)\right)$, letting $\epsilon \rightarrow 0$ in (3-42), we get
$$\left(\int_{B_{\beta}(p, r)}|h|^{2 n / n-1} \omega_{\beta}^{n}\right)^{(n-1) / n} \leq C \int_{B_{\beta}(p, r)}|\nabla h|_{g_{\beta}}^{2} \omega_{\beta}^{n}$$
for the same constant $C$ in (3-42). That is, the Sobolev inequality also holds for the conical metric $\omega_{\beta}$.
3B. Tangential and Laplacian estimates. In this section, we will prove the Hölder continuity of $\Delta_{k} u$ for $k=1,2$ and $\left(D^{\prime}\right)^{2} u$ for the solution $u$ to (1-2). The arguments of [20] can be adopted here. We recall that we assume $\beta_{1}, \beta_{2} \in\left(\frac{1}{2}, 1\right)$. We fix some notations first.

For a given point $p \notin \mathcal{S}$, we define $r_{p}=d_{g_{\beta}}(p, \mathcal{S})$, the $g_{\beta}$-distance of $p$ to the singular set $\mathcal{S}$. For simplicity of notation we will fix $\tau=\frac{1}{2}$ and an integer $k_{p} \in \mathbb{Z}_{+}$to be the smallest integer such that $\tau^{k_{p}}<r_{p}$, and $k_{i, p} \in \mathbb{Z}_{+}$the smallest integer $k_{i, p}$ such that $\tau^{k_{i, p}}<d_{\beta}\left(p, \mathcal{S}_{i}\right)$ for $i=1,2$. So $k_{p}=\max \left\{k_{1, p}, k_{2, p}\right\}$. We write $p_{1} \in \mathcal{S}_{1}$ and $p_{2} \in \mathcal{S}_{2}$ for the projections of $p$ to $\mathcal{S}_{1}$ and $\mathcal{S}_{2}$, respectively.

For $j=1,2$, we will write
$$\Delta_{j} u:=\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}} .$$

We will consider a family of conical Laplace equations with different choices of $k \in \mathbb{Z}^{+}$.
(i) If $k \geq k_{p}$, the geodesic balls $B_{\beta}\left(p, \tau^{k}\right)$ are disjoint from $\mathcal{S}$ and have smooth boundaries. We note that $g_{\beta}$ is smooth on such balls. By standard theory we can solve the following Dirichlet problem for $u_{k} \in C^{\infty}\left(B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)}\right)$ :
$$\begin{cases}\Delta_{\beta} u_{k}=f(p) & \text { in } B_{\beta}\left(p, \tau^{k}\right), \\ u_{k}=u & \text { on } \partial B_{\beta}\left(p, \tau^{k}\right) .\end{cases}$$
(ii) Without loss of generality, we assume $d_{\boldsymbol{\beta}}\left(p, \mathcal{S}_{1}\right) \leq d_{\boldsymbol{\beta}}\left(p, \mathcal{S}_{2}\right)$, i.e., $k_{1, p} \geq k_{2, p}$. We now solve the following Dirichlet problem for $u_{k} \in C^{2}\left(B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{k}\right) \backslash \mathcal{S}_{1}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{k}\right)}\right)$ for $k_{2, p}+2 \leq k<k_{1, p}$ :
$$\begin{cases}\Delta_{\beta} u_{k}=f(p) & \text { in } B_{\beta}\left(p_{1}, 2 \tau^{k}\right) \backslash \mathcal{S}_{1}, \\ u_{k}=u & \text { on } \partial B_{\beta}\left(p_{1}, 2 \tau^{k}\right) .\end{cases}$$
By similar arguments to those in the proof of Proposition 3.5 and Remark 3.6, such $u_{k}$ exists.
(iii) For $2 \leq k \leq k_{2, p}+1$, let $u_{k} \in C^{2}\left(B_{\beta}\left(p_{1,2}, 2 \tau^{k}\right) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\beta}\left(p_{1,2}, 2 \tau^{k}\right)}\right)$ solve the equation
$$\begin{cases}\Delta_{\beta} u_{k}=f(p) & \text { in } B_{\beta}\left(p_{1,2}, 2 \tau^{k}\right), \\ u_{k}=u & \text { on } \partial B_{\beta}\left(p_{1,2}, 2 \tau^{k}\right),\end{cases}$$
whose existence follows from Remark 3.6. Here $p_{1,2}=(0 ; 0 ; s(p)) \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ is the projection of $p_{1}$ to $\mathcal{S}_{2}$. We remark that we may take $f(p)=0$ by considering $\tilde{u}=u-\frac{1}{2} f(p)(n-2)^{-1}|s-s(p)|^{2}$. If the estimate holds for $\tilde{u}$, it also holds for $u$. So from now on we assume $f(p)=0$.

Lemma 3.9. Let $u_{k}$ be the solutions to (3-44)-(3-46). There exists a constant $C=C(n)>0$ such that, for all $k \in \mathbb{Z}_{+}$, we have the estimates
$$\left\|u_{k}-u\right\|_{L^{\infty}\left(\hat{B}_{k}(p)\right)} \leq C(n) \tau^{2 k} \omega\left(\tau^{k}\right),$$
where we define $\hat{B}_{k}(p)$ as
$$\hat{B}_{k}(p):= \begin{cases}B_{\beta}\left(p, \tau^{k}\right) & \text { if } k \geq k_{p}, \\ B_{\beta}\left(p_{1}, 2 \tau^{k}\right) & \text { if } k_{2, p}+2 \leq k<k_{1, p}, \\ B_{\beta}\left(p_{1,2}, 2 \tau^{k}\right) & \text { if } 2 \leq k \leq k_{2, p}+1\end{cases}$$
for different choices of $k \in \mathbb{Z}_{+}$.
We will also define $\lambda \hat{B}_{k}(p)$ to be the ball concentric with $\hat{B}_{k}(p)$ with radius scaled by $\lambda \in(0,1)$.
This lemma follows straightforwardly from Lemma 3.1 and the definition of $\omega(r)$, so we omit the proof. By the triangle inequality, we get the estimates
$$\left\|u_{k}-u_{k+1}\right\|_{L^{\infty}\left(\hat{B}_{k} / 2\right)} \leq C(n) \tau^{2 k} \omega\left(\tau^{k}\right) .$$

Since $u_{k}-u_{k+1}$ are $g_{\beta}$-harmonic functions on $\frac{1}{2} \hat{B}_{k}$, applying the gradient and Laplacian estimates (3-5) and (3-9) for harmonic functions, we get the following lemma.

Lemma 3.10. There exists a constant $C(n)>0$ such that, for all $k \in \mathbb{Z}_{+}$,
$$\left\|D^{\prime} u_{k}-D^{\prime} u_{k+1}\right\|_{L^{\infty}\left(\hat{B}_{k} / 3\right)} \leq C(n) \tau^{k} \omega\left(\tau^{k}\right)$$
and
$$\sup _{\left(\hat{B}_{k} / 3\right) \backslash \mathcal{S}}\left(\sum_{i=1}^{2}\left|\Delta_{i}\left(u_{k}-u_{k+1}\right)\right|+\left|\left(D^{\prime}\right)^{2} u_{k}-\left(D^{\prime}\right)^{2} u_{k+1}\right|\right) \leq C(n) \omega\left(\tau^{k}\right),$$
where we recall that $D^{\prime}$ denotes the first-order operators $\partial / \partial s_{i}$ for $i=5, \ldots, 2 n$.
The following lemma can be proved by looking at the Taylor expansion of $u_{k}$ at $p$ for $k \gg 1$ as in Lemma 2.8 of [20].

Lemma 3.11. For $i=1,2$, we have the limits
$$\lim _{k \rightarrow \infty} D^{\prime} u_{k}(p)=D^{\prime} u(p), \quad \lim _{k \rightarrow \infty}\left(D^{\prime}\right)^{2} u_{k}(p)=\left(D^{\prime}\right)^{2} u(p), \quad \lim _{k \rightarrow \infty} \Delta_{i} u_{k}(p)=\Delta_{i} u(p) .$$

Combining Lemmas 3.10 and 3.11, we obtain estimates on the second-order (tangential) derivatives.
Proposition 3.12. There exists a constant $C=C(n, \beta)>0$ such that
$$\sup _{B_{\beta}(0,1 / 2) \backslash \mathcal{S}}\left|\left(D^{\prime}\right)^{2} u\right|+\left|\Delta_{i} u\right| \leq C\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\int_{0}^{1} \frac{\omega(r)}{r} d r+|f(0)|\right) .$$
Proof. From the triangle inequality we have, for any given $z \in B_{\beta}\left(0, \frac{1}{2}\right) \backslash \mathcal{S}$,
$$\begin{aligned}
\left|\left(D^{\prime}\right)^{2} u(z)\right| & \leq \sum_{k=2}^{\infty}\left|\left(D^{\prime}\right)^{2} u_{k}(z)-\left(D^{\prime}\right)^{2} u_{k+1}(z)\right|+\left|\left(D^{\prime}\right)^{2} u_{2}(z)\right| \\
& \leq C(n) \sum_{k=2}^{\infty} \omega\left(\tau^{k}\right)+C(n) \operatorname{osc}_{B_{\beta}(0,1)} u_{0} \leq C(n, \boldsymbol{\beta})\left(\|u\|_{L^{\infty}}+\int_{0}^{1} \frac{\omega(r)}{r} d r+|f(0)|\right) .
\end{aligned}$$
The estimates for $\Delta_{i} u$ can be proved similarly. \(\square\)

For any other given point $q \in B_{\beta}\left(0, \frac{1}{2}\right) \backslash \mathcal{S}$, we can solve a similar Dirichlet boundary problems as $u_{k}$ with the metric balls centered at $q$, and we obtain a family of functions $v_{k}$ such that
$$\Delta_{\beta} v_{k}=f(q) \quad \text { in } \widetilde{B}_{k}(q), \quad v_{k}=u \quad \text { on } \partial \widetilde{B}_{k}(q),$$
where $\widetilde{B}_{k}(q)$ are metrics balls centered at $q$ given by
$$\widetilde{B}_{k}(q)=\widetilde{B}_{k}:=\left\{\begin{array}{ll}
B_{\beta}\left(q, \tau^{k}\right) & \text { if } k \geq k_{q}, \\
B_{\beta}\left(q_{i}, 2 \tau^{k}\right) & \text { if } k_{j, q}+2 \leq k<k_{q} \\
B_{\beta}\left(q_{i, j}, 2 \tau^{k}\right) & \text { if } k \leq k_{j, q}+1 .
\end{array} \text { (here } k_{i, q}=\max \left(k_{1, q}, k_{2, q}\right) \text { and } j \neq i\right) \text {, }$$
Similar estimates as in Lemmas 3.9-3.11 also hold for $v_{k}$ within the balls $\widetilde{B}_{k}(q)$.
We are now ready to state the main result in this subsection on the continuity of second-order derivatives.
Proposition 3.13. Let $d=d_{\boldsymbol{\beta}}(p, q)<\frac{1}{16}$. There exists a constant $C=C(n)>0$ such that if $u$ solves the conical Laplace equation (1-2), then the following holds for $i=1,2$ :
$$\left|\Delta_{i} u(p)-\Delta_{i} u(q)\right|+\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \leq C\left(d\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right) .$$
Proof. We only prove the estimate for $\left(D^{\prime}\right)^{2} u$; the estimates for $\Delta_{i} u$ can be dealt with in the same way.
We may assume $r_{p}=\min \left(r_{p}, r_{q}\right)$. We fix $\ell \in \mathbb{Z}$ such that $\tau^{\ell}$ is comparable to $d$; more precisely, take
$$\tau^{\ell+4} \leq d<\tau^{\ell+3} \quad \text { or } \quad \tau^{\ell+1} \leq 8 d \leq \tau^{\ell} \text {. }$$
We calculate by the triangle inequality
$$\begin{aligned}
\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| & \leq\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u_{\ell}(p)\right|+\left|\left(D^{\prime}\right)^{2} u_{\ell}(p)-\left(D^{\prime}\right)^{2} u_{\ell}(q)\right| \\
& +\left|\left(D^{\prime}\right)^{2} u_{\ell}(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right|+\left|\left(D^{\prime}\right)^{2} v_{\ell}(q)-\left(D^{\prime}\right)^{2} u(q)\right| \\
& =: I_{1}+I_{2}+I_{3}+I_{4} .
\end{aligned}$$

We will estimate $I_{1}-I_{4}$ one by one.
$I_{1}$ and $I_{4}$ : By (3-51) and (3-52), we have
$$I_{1}=\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u_{\ell}(p)\right| \leq C(n) \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right),$$
and a similar estimate holds for $I_{4}$ as well:
$$I_{4}=\left|\left(D^{\prime}\right)^{2} u(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right| \leq C(n) \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right) .$$
$\underline{I_{3}}$ : By the choice of $\ell$, it is not hard to see that $\frac{2}{3} \widetilde{B}_{\ell}(q) \subset \hat{B}_{\ell}(p)$. In particular, $u_{\ell}$ and $v_{\ell}$ are both defined on $\frac{2}{3} \widetilde{B}_{\ell}(q)$ and satisfy the equations
$$\Delta_{\beta} u_{\ell}=f(p) \quad \text { and } \quad \Delta_{\beta} v_{\ell}=f(q),$$
respectively, on this ball. From (3-47) for $u_{\ell}$ and from a similar estimate for $v_{\ell}$, we get
$$\left\|u_{\ell}-v_{\ell}\right\|_{L^{\infty}\left(2 \tilde{B}_{\ell}(q) / 3\right)} \leq C \tau^{2 \ell} \omega\left(\tau^{\ell}\right) .$$
Consider the function
$$U:=u_{\ell}-v_{\ell}-\frac{f(p)-f(q)}{2(n-2)}|s-s(\tilde{q})|^{2},$$
where $\tilde{q}$ is the center of the ball $\widetilde{B}_{\ell}(q) . U$ is $g_{\beta}$-harmonic in $\frac{2}{3} \widetilde{B}_{\ell}(q)$ and satisfies the estimate
$$\|U\|_{L^{\infty}\left(2 \widetilde{B} / \beta_{\ell}(q)\right)} \leq C \tau^{2 \ell} \omega\left(\tau^{\ell}\right)+C \tau^{2 \ell} \omega(d) \leq C(n) \tau^{2 \ell} \omega\left(\tau^{\ell}\right) .$$
The derivatives estimates imply that
$$\left|\left(D^{\prime}\right)^{2} U(q)\right| \leq C \tau^{-2 \ell}\|U\|_{L^{\infty}\left(2 \widetilde{B} / 3_{\ell}(q)\right)} \leq C(n) \omega\left(\tau^{\ell}\right) .$$
Hence
$$I_{3}=\left|\left(D^{\prime}\right)^{2} u_{\ell}(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right| \leq C(n) \omega\left(\tau^{\ell}\right) .$$
$\underline{I_{2}}$ : This is a little more complicated than the previous estimates. We define $h_{k}=u_{k-1}-u_{k}$ for $k \leq \ell$. We observe that $h_{k}$ is $g_{\beta}$-harmonic on $\hat{B}_{k}(p)$ and by (3-47) satisfies the $L^{\infty}$-estimate $\left\|h_{k}\right\|_{\hat{B}_{k}(p)} \leq C \tau^{2 k} \omega\left(\tau^{k}\right)$ and the derivatives estimates $\left\|\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(2 \hat{B}_{k}(p) / 3\right)} \omega\left(\tau^{k}\right)$. On the other hand, the function $\left(D^{\prime}\right)^{2} h_{k}$ is also $g_{\beta}$-harmonic on $\frac{2}{3} \hat{B}_{k}(p)$, so the gradient estimate implies that
$$\left\|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(\left(\hat{B}_{k}(p) / 2\right) \backslash \mathcal{S}\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
Integrating this along the minimal $g_{\beta}$-geodesic $\gamma$ connecting $p$ and $q$ and noting that $\gamma$ avoids $\mathcal{S}$ since $\left(\mathbb{C}^{n} \backslash \mathcal{S}, g_{\boldsymbol{\beta}}\right)$ is strictly geodesically convex, we get
$$\left|\left(D^{\prime}\right)^{2} h_{k}(p)-\left(D^{\prime}\right)^{2} h_{k}(q)\right| \leq d \cdot\left\|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(\left(\hat{B}_{k}(p) / 2\right) \backslash \mathcal{S}\right)} \leq d C \tau^{-k} \omega\left(\tau^{k}\right) .$$
By the triangle inequality, for each $k \leq \ell$,
$$I_{2}=\left|\left(D^{\prime}\right)^{2} u_{\ell}(p)-\left(D^{\prime}\right)^{2} u_{\ell}(q)\right| \leq\left|\left(D^{\prime}\right)^{2} u_{2}(p)-\left(D^{\prime}\right)^{2} u_{2}(q)\right|+d C \sum_{k=2}^{\ell} \tau^{-k} \omega\left(\tau^{k}\right) .$$

Observe that $p, q \in \hat{B}_{2}(p)$ and the function $\left(D^{\prime}\right)^{2} u_{2}$ is $g_{\beta}$-harmonic on $\hat{B}_{2}(p)$. From (3-47) and derivatives estimates we have
$$\left\|\left(D^{\prime}\right)^{2} u_{2}\right\|_{L^{\infty}\left(2 \hat{B}_{2}(p) / 3\right)} \leq C\left\|u_{2}\right\|_{L^{\infty}\left(\hat{B}_{2}(p)\right)} \leq C\left(\|u\|_{L^{\infty}}+\omega\left(\tau^{2}\right)\right) .$$
Again by the gradient estimate we have
$$\left\|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} u_{2}\right\|_{L^{\infty}\left(\hat{B}_{2}(p) / 2\right)} \leq C\left(\|u\|_{L^{\infty}}+\omega\left(\tau^{2}\right)\right) .$$
Integrating along the minimal geodesic $\gamma$ we arrive at
$$\left|\left(D^{\prime}\right)^{2} u_{2}(p)-\left(D^{\prime}\right)^{2} u_{2}(q)\right| \leq d C\left(\|u\|_{L^{\infty}}+\omega\left(\tau^{2}\right)\right) .$$
Combining this with (3-57), we obtain
$$I_{2} \leq C d\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\sum_{k=2}^{\ell} \tau^{-k} \omega\left(\tau^{k}\right)\right) .$$
Combing the estimates for $I_{1}-I_{4}$, we get
$$\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \leq C\left(d\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\sum_{k=2}^{\ell} \tau^{-k} \omega\left(\tau^{k}\right)\right)+\sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right)\right) .$$
Proposition 3.13 now follows from this and the fact that $\omega(r)$ is monotonically increasing. \(\square\)

3C. Mixed normal-tangential estimates along the directions $\mathcal{S}$. Throughout this section, we fix two points $p, q \in B_{\beta}\left(0, \frac{1}{2}\right) \backslash \mathcal{S}$ and assume $r_{p} \leq r_{q}$. Recall that we defined the weighted "polar coordinates" $\left(r_{i}, \theta_{i}\right)$ for $\left(z_{1}, z_{2}\right)$ :
$$\rho_{i}=\left|z_{i}\right|, \quad r_{i}=\rho_{i}^{\beta_{i}}, \quad \theta_{i}=\arg z_{i}, \quad i=1,2 .$$
Under these coordinates,
$$\Delta_{i} u=\left|z_{i}\right|^{2\left(1-\beta_{i}\right)} \frac{\partial^{2} u}{\partial z_{i} \partial \bar{z}_{i}}=\frac{\partial^{2} u}{\partial r_{i}^{2}}+\frac{1}{r_{i}} \frac{\partial u}{\partial r_{i}}+\frac{1}{\beta_{i}^{2} r_{i}^{2}} \frac{\partial^{2} u}{\partial \theta_{i}^{2}} .$$
Let $u_{k}$ and $v_{k}$ be the solutions to (3-44)-(3-46) on $\hat{B}_{k}(p)$ and $\widetilde{B}_{k}(q)$, respectively. Recalling that $u_{k}-u_{k+1}$ satisfies (3-49) and applying gradient estimates to the $g_{\beta}$-harmonic function $u_{k}-u_{k+1}$, we get the bound of $\left\|\nabla_{g_{\beta}}\left(u_{k}-u_{k+1}\right)\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 3\right)}$, which in particular implies that, for $i=1,2$,
$$\left\|\left|z_{i}\right|^{1-\beta_{i}}\left(\frac{\partial u_{k}}{\partial z_{i}}-\frac{\partial u_{k+1}}{\partial z_{i}}\right)\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 3\right)} \leq C \tau^{k} \omega\left(\tau^{k}\right) .$$
Similarly, $D^{\prime} u_{k}-D^{\prime} u_{k+1}$ is also $g_{\beta}$-harmonic on $\frac{1}{2} \hat{B}_{k}(p)$, and applying gradient estimates to this function we get, for $i=1,2$,
$$\left\|\left|z_{i}\right|^{1-\beta_{i}}\left(\frac{\partial D^{\prime} u_{k}}{\partial z_{i}}-\frac{\partial D^{\prime} u_{k+1}}{\partial z_{i}}\right)\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 3\right)} \leq C \omega\left(\tau^{k}\right) .$$
The next lemma can be proved in the same way as Lemma 2.10 of [20] since $p \notin \mathcal{S}$; we omit the proof.

Lemma 3.14. For $i=1,2$, we have the limits
$$\lim _{k \rightarrow \infty} \frac{\partial u_{k}}{\partial r_{i}}(p)=\frac{\partial u}{\partial r_{i}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial u_{k}}{r_{i} \partial \theta_{i}}(p)=\frac{\partial u}{r_{i} \partial \theta_{i}}(p)$$
and
$$\lim _{k \rightarrow \infty} \frac{\partial D^{\prime} u_{k}}{\partial r_{i}}(p)=\frac{\partial D^{\prime} u}{\partial r_{i}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial D^{\prime} u_{k}}{r_{i} \partial \theta_{i}}(p)=\frac{\partial D^{\prime} u}{r_{i} \partial \theta_{i}}(p) .$$
Similar formulas also hold for $v_{k}$ at the point $q$.
We are going to estimate the quantities
$$J:=\left|\frac{\partial D^{\prime} u}{\partial r_{i}}(p)-\frac{\partial D^{\prime} u}{\partial r_{i}}(q)\right| \quad \text { and } \quad K:=\left|\frac{\partial D^{\prime} u}{r_{i} \partial \theta_{i}}(p)-\frac{\partial D^{\prime} u}{r_{i} \partial \theta_{i}}(q)\right|, \quad i=1,2 .$$
Note that $J, K$ correspond to $\left|N_{j} D^{\prime} u(p)-N_{j} D^{\prime} u(q)\right|$ in Theorem 1.2. We will estimate the case for $i=1$ and $J$, since the other cases are completely the same. By the triangle inequality we have
$$\begin{aligned}
J \leq & \left|\frac{\partial D^{\prime} u}{\partial r_{i}}(p)-\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(p)\right|+\left|\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(p)-\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(q)\right| \\
& \quad+\left|\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(q)-\frac{\partial D^{\prime} v_{\ell}}{\partial r_{i}}(q)\right|+\left|\frac{\partial D^{\prime} v_{\ell}}{\partial r_{i}}(q)-\frac{\partial D^{\prime} u}{\partial r_{i}}(q)\right| \\
=: J_{1}+J_{2}+J_{3}+J_{4} . &
\end{aligned}$$

Lemma 3.15. There exists a constant $C(n)>0$ such that $J_{1}, J_{3}$ and $J_{4}$ satisfy
$$J_{1}+J_{4} \leq C \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right), \quad J_{3} \leq C \omega\left(\tau^{\ell}\right) .$$
Proof. The estimates for $J_{1}$ and $J_{4}$ can be proved similarly to those of $I_{1}$ and $I_{4}$ in Section 3B, using (3-60) and (3-61). $J_{3}$ can be estimated in a similar way to $I_{3}$ in Section 3B, using (3-60). We omit the details. \(\square\)

To estimate $J_{2}$, as in Section 3B we define $h_{k}:=u_{k-1}-u_{k}$ for $2 \leq k \leq \ell$ which is $g_{\beta}$-harmonic on $\hat{B}_{k}(p)$ and satisfies the $L^{\infty}$-estimate $\left\|h_{k}\right\|_{L^{\infty}\left(\hat{B}_{k}(p)\right)} \leq C \tau^{2 k} \omega\left(\tau^{k}\right)$ by (3-60). We rewrite (3-56) as
$$\left\|\left(D^{\prime}\right)^{3} h_{k}\right\|_{L^{\infty}\left(\left(\hat{B}_{k}(p) / 2\right) \backslash \mathcal{S}\right)}+\sum_{i=1}^{2}\left\|\left|z_{i}\right|^{1-\beta_{i}} \frac{\partial}{\partial z_{i}}\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(\left(\hat{B}_{k}(p) / 2\right) \backslash \mathcal{S}\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Lemma 3.16. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that, for any $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}$, the following pointwise estimate holds for all $k \leq \min \left(\ell, k_{p}\right)$ :
$$\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(z)\right|+\left|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}(z)\right| \leq C r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .$$
Proof. We define a function $F$ as
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2} D^{\prime} h_{k}}{\partial z_{1} \partial \bar{z}_{1}}=-\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2} D^{\prime} h_{k}}{\partial z_{2} \partial \bar{z}_{2}}-\sum_{j=5}^{2 n} \frac{\partial^{2} D^{\prime} h_{k}}{\partial s_{j}^{2}}=: F .$$

The Laplacian estimates (3-9) and derivatives estimates applied to the $g_{\beta}$-harmonic function $D^{\prime} h_{k}$ imply that $F$ satisfies
$$\|F\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)} \leq C(n) \tau^{-k} \omega\left(\tau^{k}\right) .$$
For any $k \leq \min \left(\ell, k_{p}\right)$ and $x \in \mathcal{S}_{1} \cap \frac{1}{4} \hat{B}_{k}(p)$, we have that $B_{\beta}\left(x, \tau^{k}\right) \subset \frac{1}{3} \hat{B}_{k}(p)$. The intersection of $B_{\beta}\left(x, \tau^{k}\right)$ with the complex plane $\mathbb{C}$ passing through $x$ and orthogonal to the hyperplane $\mathcal{S}_{1}$ lies in a metric ball of radius $\tau^{k}$ under the standard cone metric $\hat{g}_{\beta_{1}}$ on $\mathbb{C}$. We view (3-63) as defined on the ball $\hat{B}:=B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}}\right) \subset \mathbb{C}$. The estimate (2-3) applied to the function $D^{\prime} h_{k}$ gives rise to
$$\sup _{B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}}\left|\frac{\partial D^{\prime} h_{k}}{\partial z_{1}}\right| \leq C \frac{\left\|D^{\prime} h_{k}\right\|_{L^{\infty}(\hat{B})}}{\left(\tau^{k}\right)^{1 / \beta_{1}}}+C\|F\|_{L^{\infty}(\hat{B})}\left(\tau^{k}\right)^{2-1 / \beta_{1}} .$$
Therefore, on $B_{\mathbb{C}}\left(x, \frac{1}{2}\left(\tau^{k}\right)^{1 / \beta_{1}}\right) \backslash\{x\}$,
$$\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(z)\right|+\left|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}(z)\right| \leq \frac{1}{\beta_{1}} r_{1}^{1 / \beta_{1}-1}\left|\frac{\partial D^{\prime} h_{k}}{\partial z_{1}}(z)\right| \leq C r_{1}^{1 / \beta_{1}-1} \tau^{k\left(1-1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) .$$
On other hand, since $B_{\mathbb{C}}\left(x, \frac{1}{2}\left(\tau^{k}\right)^{1 / \beta_{1}}\right)=B_{\hat{g}_{\beta_{1}}}\left(x, 2^{-\beta_{1}} \tau^{k}\right)$,
$$\frac{1}{4} \hat{B}_{k}(p) \subset \bigcup_{x \in \mathcal{S}_{1} \cap \hat{B}_{k} / 4} B_{\mathbb{C}}\left(x, \frac{1}{2}\left(\tau^{k}\right)^{1 / \beta_{1}}\right) .$$
Equation (3-65) implies the desired estimate on the balls $\frac{1}{4} \hat{B}_{k}(p)$. \(\square\)

Remark 3.17. By similar arguments we also get the following estimates for any $k \leq \min \left(\ell, k_{p}\right)$ and $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}_{1}$ :
$$\left|\frac{\partial\left(D^{\prime}\right)^{2} h_{k}}{\partial r_{1}}(z)\right|+\left|\frac{\partial\left(D^{\prime}\right)^{2} h_{k}}{r_{1} \partial \theta_{1}}(z)\right| \leq C r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right) .$$

Lemma 3.18. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that, for all $k \leq \min \left(k_{p}, \ell\right)$ and $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}$, the following pointwise estimates hold:
$$\begin{aligned}
\left|\frac{\partial^{2} D^{\prime} h_{k}}{r_{1}^{2} \partial \theta_{1}^{2}}(z)\right|+\left|\frac{\partial^{2} D^{\prime} h_{k}}{r_{1} \partial r_{1} \partial \theta_{1}}(z)\right| & \leq C r_{1}(z)^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right), \\
\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1}^{2}}(z)\right| & \leq C r_{1}(z)^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Proof. Applying the gradient estimate to the $g_{\beta}$-harmonic function $D^{\prime} h_{k}$, we get
$$\left\|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)} \leq\left\|\nabla_{g_{\beta}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)} \leq C \omega\left(\tau^{k}\right) .$$
The function $\partial_{\theta_{1}} D^{\prime} h_{k}$ is also a continuous $g_{\beta}$-harmonic function, so the derivatives estimates implies, on $\frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\left|F_{1}\right| \leq\left|\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{2} \partial \bar{z}_{2}}\right|+\left|\frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial s_{j}^{2}}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right),$$
where $F_{1}$ is defined as
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{1} \partial \bar{z}_{1}}=-\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{2} \partial \bar{z}_{2}}-\sum_{j=5}^{2 n} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial s_{j}^{2}}=: F_{1} .$$
We apply similar arguments as in the proof of Lemma 3.16. For any $x \in \mathcal{S}_{1} \cap \frac{1}{4} \hat{B}_{k}(p)$, we view (3-70) as defined on the $\mathbb{C}$-ball $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}}\right)$, and by the estimate (2-3) we have, on $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$,
$$\left|\frac{\partial\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{1}}\right| \leq C \frac{\left\|\partial_{\theta_{1}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\hat{B}_{\mathbb{C}}\right)}}{\left(\tau^{k}\right)^{1 / \beta_{1}}}+C\left\|F_{1}\right\|_{L^{\infty}\left(\hat{B}_{\mathbb{C}}\right)}\left(\tau^{k}\right)^{2-1 / \beta_{1}} .$$
Equivalently, this means that, on $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$,
$$\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1} \partial \theta_{1}}\right|+\left|\frac{\partial^{2} D^{\prime} h_{k}}{r_{1} \partial \theta_{1}^{2}}\right| \leq r_{1}^{1 / \beta_{1}-1}\left|\frac{\partial\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{1}}\right| \leq C r_{1}^{1 / \beta_{1}-1} \tau^{k\left(1-1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) .$$
Again by the inclusion (3-66), we get (3-68). The estimate (3-69) follows from Lemma 3.16, (3-68), (3-64) and the equation (from (3-63))
$$\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1}^{2}}=\frac{1}{r_{1}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}-\frac{1}{\beta_{1}^{2} r_{1}^{2}} \frac{\partial^{2} D^{\prime} h_{k}}{\partial \theta_{1}^{2}}+F .$$ \(\square\)

Lemma 3.19. There exists a constant $C(n, \boldsymbol{\beta})>0$ such that, for $k \leq \min \left(k_{2, p}, \ell\right)$, the following pointwise estimates hold for any $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}$ :
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right| \leq C(n, \boldsymbol{\beta}) r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-k\left(-1+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) .$$
Proof. By the Laplacian estimate in (3-9) for the harmonic function $D^{\prime} h_{k}$ on $\frac{1}{2} \hat{B}_{k}(p)$, we have
$$\sup _{\hat{B}_{k}(p) / 2.2}\left(\left|\Delta_{1} D^{\prime} h_{k}\right|+\left|\Delta_{2} D^{\prime} h_{k}\right|\right) \leq C(n) \tau^{-2 k} \operatorname{osc}_{\hat{B}_{k}(p) / 2}\left(D^{\prime} h_{k}\right) \leq C(n) \tau^{-k} \omega\left(\tau^{k}\right) .$$
Since $\Delta_{1}\left(D^{\prime} h_{k}\right)$ is also $g_{\beta}$-harmonic, the Laplacian estimates (3-9) imply
$$\sup _{\hat{B}_{k}(p) / 2.4}\left(\left|\Delta_{1} \Delta_{1} D^{\prime} h_{k}\right|+\left|\Delta_{2} \Delta_{1} D^{\prime} h_{k}\right|\right) \leq C(n) \tau^{-2 k} \operatorname{osc}_{\hat{B}_{k}(p) / 2.2} \Delta_{1} D^{\prime} h_{k} \leq C \tau^{-3 k} \omega\left(\tau^{k}\right) .$$
Now from the equation $\Delta_{\beta}\left(\Delta_{1} D^{\prime} h_{k}\right)=0$, we get
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}} \Delta_{1} D^{\prime} h_{k}=-\Delta_{2} \Delta_{1} D^{\prime} h_{k}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}} \Delta_{1} D^{\prime} h_{k}=: F_{2} .$$
From (3-73) and the Laplacian estimates (3-9), we see that $\sup _{\hat{B}_{k}(p) / 2.4}\left|F_{2}\right| \leq C \tau^{-3 k} \omega\left(\tau^{k}\right)$. Using similar arguments, by considering $x \in \frac{1}{3} \hat{B}_{k}(p) \cap \mathcal{S}_{1}$, we obtain from (3-74) that, on $\hat{B}:=B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{\left.1 / \beta_{1} / 2\right) \backslash\{x\} \text {, }}\right.$
$$\left|\frac{\partial}{\partial z_{1}} \Delta_{1} D^{\prime} h_{k}\right| \leq C \frac{\left\|\Delta_{1} D^{\prime} h_{k}\right\|_{L^{\infty}(\hat{B})}}{\left(\tau^{k}\right)^{1 / \beta_{1}}}+C\left\|F_{2}\right\|_{L^{\infty}(\hat{B})}\left(\tau^{k}\right)^{2-1 / \beta_{1}} \leq C \tau^{-k\left(1+1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) .$$

This implies that, for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\left|\frac{\partial}{\partial r_{1}} \Delta_{1} D^{\prime} h_{k}(z)\right|+\left|\frac{\partial}{r_{1} \partial \theta_{1}} \Delta_{1} D^{\prime} h_{k}(z)\right| \leq C r_{1}^{1 / \beta_{1}-1} \tau^{-k\left(1+1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) .$$
Now taking $\partial / \partial r_{1}$ on both sides of $\Delta_{\beta} D^{\prime} h_{k}=0$, we get
$$\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)=-\frac{\partial}{\partial r_{1}}\left(\Delta_{1} D^{\prime} h_{k}\right)-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)=: F_{3} .$$
From (3-75), for any $z \in \frac{1}{3} \hat{B}_{k} \backslash \mathcal{S}$, we have $\left|F_{3}\right|(z) \leq C r_{1}^{1 / \beta_{1}-1} \tau^{-k\left(1+1 / \beta_{1}\right)} \omega\left(\tau^{k}\right)$. By a similar argument, for any $y \in \frac{1}{3.2} \hat{B}_{k}(p) \cap \mathcal{S}_{2}$, we apply estimate (2-3) to $\partial D^{\prime} h_{k} / \partial r_{1}$ and get, on $A_{1}:=B_{\mathbb{C}}\left(y, \frac{1}{2}\left(\tau^{k}\right)^{1 / \beta_{2}}\right) \backslash\{y\}$ - the punctured ball in the complex plane $\mathbb{C}$ of (Euclidean) radius $\frac{1}{2}\left(\tau^{k}\right)^{1 / \beta_{2}}$ and orthogonal to $\mathcal{S}_{2}$ passing through $y$-that
$$\begin{aligned}
\left|\frac{\partial}{\partial z_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right| & \leq C \frac{\left\|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right\|_{L^{\infty}\left(A_{1}\right)}\left(\tau^{k}\right)^{1 / \beta_{2}}}{}+C\left\|F_{3}\right\|_{L^{\infty}\left(A_{1}\right)}\left(\tau^{k}\right)^{2-1 / \beta_{2}} \\
& \leq C r_{1}^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}+1 / \beta_{2}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Varying $y \in \frac{1}{3.2} \hat{B}_{k}(p) \cap \mathcal{S}_{2}$ we get, for any $z \in \frac{1}{4} \hat{B}_{k} \backslash \mathcal{S}$, that the following pointwise estimate holds:
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right| \leq C r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-k\left(1 / \beta_{1}+1 / \beta_{2}-1\right)} \omega\left(\tau^{k}\right) .$$ \(\square\)

Lemma 3.20. Let $d=d_{\boldsymbol{\beta}}(p, q)$. There exists a constant $C(n, \boldsymbol{\beta})$ such that, for all $k \leq \ell$,
$$\begin{array}{|l}
\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right), \\
\left|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}(q)\right| \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .
\end{array}$$
Proof. We will consider the different cases $r_{p}=\min \left(r_{p}, r_{q}\right) \leq 2 d$ and $r_{p}=\min \left(r_{p}, r_{q}\right)>2 d$.
Case 1: $r_{p} \leq 2 d$. In this case, it is clear by the choice of $\ell$ that $r_{p} \approx \tau^{k_{p}} \leq 2 d \leq \tau^{\ell+2}$, so $k_{p} \geq \ell+2$.
From our assumption when solving (3-45), $r_{p}=d_{\boldsymbol{\beta}}\left(p, \mathcal{S}_{1}\right)$, i.e., $r_{1}(p)=r_{p} \leq 2 d$. By the triangle inequality we have $r_{1}(q) \leq 3 d$. We also remark that, for $k \leq \ell$, we have $\tau^{k} \geq \tau^{\ell}>8 d$. In particular, the geodesics considered below all lie inside the balls $\frac{1}{4} \hat{B}_{k}(p)$, and the estimates in Lemmas 3.16-3.19 hold for points on these geodesics.

Let the coordinates of the points $p$ and $q$ be given by
$$p=\left(r_{1}(p), \theta_{1}(p) ; r_{2}(p), \theta_{2}(p) ; s(p)\right) \quad \text { and } \quad q=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(q), \theta_{2}(q) ; s(q)\right) .$$
Let $\gamma:[0, d] \rightarrow B_{\beta}(0, q) \backslash \mathcal{S}$ be the unique $g_{\beta}$-geodesic connecting $p$ and $q$. We know the curve $\gamma$ is disjoint from $\mathcal{S}$, and we write
$$\gamma(t)=\left(r_{1}(t), \theta_{1}(t) ; r_{2}(t), \theta_{2}(t) ; s(t)\right)$$
for the coordinates of $\gamma(t)$ for $t \in[0, d]$. By definition we have, for all $t \in[0, d]$,
$$\left|\gamma^{\prime}(t)\right|_{g_{\beta}}^{2}=\left(r_{1}^{\prime}(t)\right)^{2}+\beta_{1}^{2} r_{1}(t)^{2}\left(\theta_{1}^{\prime}(t)\right)^{2}+\left(r_{2}^{\prime}(t)\right)^{2}+\beta_{2}^{2} r_{2}(t)^{2}\left(\theta_{2}^{\prime}(t)\right)^{2}+\left|s^{\prime}(t)\right|^{2}=1 .$$

So $|s(p)-s(q)| \leq d$ and $\left|r_{i}(p)-r_{i}(q)\right| \leq d$ for $i=1,2$. We define
$$q^{\prime}:=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(p), \theta_{2}(p) ; s(p)\right) \quad \text { and } \quad p^{\prime}:=\left(r_{1}(p), \theta_{1}(q) ; r_{2}(p), \theta_{2}(p) ; s(p)\right),$$
the points with coordinates related to $p$ and $q$. Let $\gamma_{1}$ be the $g_{\beta}$-geodesic connecting $q$ and $q^{\prime}, \gamma_{2}$ be the $g_{\beta}$-geodesic joining $q^{\prime}$ to $p^{\prime}$, and $\gamma_{3}$ be the $g_{\beta}$-geodesic joining $p^{\prime}$ to $p$.

By the triangle inequality, we have
$$\begin{aligned}
& \left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| \\
& \quad \leq\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(p^{\prime}\right)\right|+\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(p^{\prime}\right)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(q^{\prime}\right)\right|+\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(q^{\prime}\right)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| \\
& \quad=: J_{1}^{\prime}+J_{2}^{\prime}+J_{3}^{\prime} .
\end{aligned}$$
Integrating along $\gamma_{3}$, on which the points have fixed $r_{1}$-coordinate $r_{1}(p)$, we get (by (3-68))
$$J_{1}^{\prime}=\left|\int_{\gamma_{3}} \frac{\partial}{\partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d \theta_{1}\right| \leq C(n, \boldsymbol{\beta}) r_{1}(p)^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .$$
Integrating along $\gamma_{2}$, we get (by (3-69))
$$\begin{aligned}
J_{2}^{\prime} & =\left|\int_{\gamma_{2}} \frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d r_{1}\right| \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right)\left|\int_{r_{1}(p)}^{r_{1}(q)} t^{1 / \beta_{1}-2} d t\right| \\
& =C(n, \boldsymbol{\beta}) \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right)\left|r_{1}(p)^{1 / \beta_{1}-1}-r_{1}(q)^{1 / \beta_{1}-1}\right| \\
& \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right)\left|r_{1}(p)-r_{1}(q)\right|^{1 / \beta_{1}-1} \\
& \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} .
\end{aligned}$$
To deal with $J_{3}^{\prime}$, we need to consider different choices of $k \leq \ell$.
Case 1a: $k_{2, p}+1 \leq k \leq \ell$. In this case, the balls $\hat{B}_{k}(p)$ are centered at $p_{1} \in \mathcal{S}_{1}$ (recall $p_{1}$ is the projection of $p$ to $\mathcal{S}_{1}$; hence $p$ and $p_{1}$ have the same ( $r_{2}, \theta_{2} ; s$ )-coordinates). We have $\tau^{-k} \leq 8^{-1} d^{-1}$ by the choice of $\ell$. The balls $\hat{B}_{k}(p)$ are disjoint from $\mathcal{S}_{2}$, so we can introduce the smooth coordinates $w_{2}=z_{2}^{\beta_{2}}$, and under the coordinates $\left(r_{1}, \theta_{1} ; w_{2}, z_{3}, \ldots, z_{n}\right)$, the metric $g_{\beta}$ becomes the smooth cone metric with conical singularity only along $\mathcal{S}_{1}$ with angle $2 \pi \beta_{1}$. Therefore we can derive the following estimate as in (3-62):
$$\sup _{\left(\hat{B}_{k}(p) / 2\right) \backslash \mathcal{S}_{1}}\left|\frac{\partial\left(D^{\prime}\right)^{2} h_{k}}{\partial r_{1}}\right|+\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial w_{2}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Since $q$ and $q^{\prime}$ have the same ( $r_{1}, \theta_{1}$ )-coordinates and $g_{\beta}$ is a product metric, $\gamma_{1}$ is in fact a straight line segment (under the coordinates $\left(w_{2}, z_{3}, \ldots, z_{n}\right)$ ) in the hyperplane with fixed $\left(r_{1}, \theta_{1}\right)$-coordinates. Integrating over $\gamma_{1}$, we get
$$\begin{aligned}
J_{3}^{\prime} \leq \int_{\gamma_{1}}\left|\frac{\partial}{\partial w_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|+\sum_{j}\left|\frac{\partial}{\partial s_{j}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right| & \leq C \tau^{-k} \omega\left(\tau^{k}\right) d_{\beta}\left(q, q^{\prime}\right) \leq C \tau^{-k} \omega\left(\tau^{k}\right) d \\
& \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} .
\end{aligned}$$

Case 1b: $k \leq k_{2, p}$. In this case, the balls $\hat{B}_{k}(p)$ are centered at $p_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ and $\tau^{k} \geq r_{2}(p)$. By the triangle inequality, $r_{2}(q) \leq d+r_{2}(p) \leq \frac{9}{8} \tau^{k}$. We choose the points
$$\tilde{q}=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(p), \theta_{2}(p) ; s(q)\right) \quad \text { and } \quad \hat{q}=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(q), \theta_{2}(p) ; s(q)\right) .$$
Let $\tilde{\gamma}_{1}$ be the $g_{\beta}$-geodesic joining $q^{\prime}$ to $\tilde{q}, \tilde{\gamma}$ the $g_{\beta}$-geodesic joining $\tilde{q}$ to $\hat{q}$, and $\hat{\gamma}$ the $g_{\beta}$-geodesic joining $\hat{q}$ to $q$. The curves $\tilde{\gamma}_{1}, \tilde{\gamma}$ and $\hat{\gamma}$ all lie in the hyperplane with constant $\left(r_{1}, \theta_{1}\right)$-coordinates $\left(r_{1}(q), \theta_{1}(q)\right)$. Then by the triangle inequality we have
$$J_{3}^{\prime} \leq\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(q^{\prime}\right)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\tilde{q})\right|+\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\tilde{q})-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\hat{q})\right|+\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\hat{q})-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right|=: J_{1}^{\prime \prime}+J_{2}^{\prime \prime}+J_{3}^{\prime \prime} .$$
We will use frequently the inequalities $r_{1}(q) \leq 3 d$ and $\max \left(r_{2}(q), r_{2}(p)\right) \leq 2 \tau^{k}$ in the estimates below. Integrating along $\hat{\gamma}$ we get (by (3-71))
$$\begin{aligned}
J_{3}^{\prime \prime} \leq\left|\int_{\hat{\gamma}} \frac{\partial}{\partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d \theta_{2}\right| & \leq C r_{1}(q)^{1 / \beta_{1}-1} r_{2}(q)^{1 / \beta_{2}} \tau^{-k\left(-1+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) \\
& \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Integrating along $\tilde{\gamma}$ we get (again by (3-71))
$$\begin{aligned}
J_{2}^{\prime \prime} \leq\left|\int_{\tilde{\gamma}} \frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d r_{2}\right| & \leq C r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right)\left|\int_{r_{2}(q)}^{r_{2}(p)} t^{1 / \beta_{2}-1} d t\right| \\
& \leq C r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) \max \left(r_{2}(q), r_{2}(p)\right)^{1 / \beta_{2}-1} d \\
& \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Integrating along $\tilde{\gamma}_{1}$ we get (by (3-67))
$$J_{1}^{\prime \prime} \leq\left|\int_{\tilde{\gamma}_{1}} \frac{\partial}{\partial s_{j}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d t\right| \leq C r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right) d \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .$$
Combining the three inequalities above, we get, in the case $k \leq k_{2, p}$,
$$J_{3}^{\prime} \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .$$
Combining the estimates on $J_{1}^{\prime}, J_{2}^{\prime}$ and $J_{3}^{\prime}$, we finish the proof of (3-78) in the case $r_{p} \leq 2 d$.
Case 2a: $r_{p}>2 d$ and $\ell \leq k_{p}$. In this case $\tau^{k_{p}} \approx r_{p}>2 d \geq \tau^{\ell+3}$. From the triangle inequality we get $d_{\boldsymbol{\beta}}(\gamma(t), \mathcal{S}) \geq d$. In particular, the $r_{1}$ and $r_{2}$ coordinates of $\gamma(t)$ are both bigger than $d$. In this case $k \leq \ell \leq k_{p}$, and Lemmas 3.16-3.19 hold for the points in $\gamma$. So $r_{1}(\gamma(t)) \leq r_{1}(p)+d \leq 2 \tau^{k}$. We calculate the gradient of $\partial D^{\prime} h_{k} / \partial r_{1}$ along $\gamma$ :
$$\begin{aligned}
\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right|^{2}=\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2}+\left|\frac{\partial}{\beta_{1} r_{1} \partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2} & +\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2} \\
& +\left|\frac{\partial}{\beta_{2} r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2}+\sum_{j}\left|\frac{\partial}{\partial s_{j}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2} .
\end{aligned}$$
(1) When $k_{2, p}+1 \leq k \leq \ell$ we have by (3-83) that
$$\sup _{\left(\hat{B}_{k} / 2\right) \backslash \mathcal{S}_{1}}\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
Thus by Lemma 3.18, (3-67) and (3-85), along $\gamma$ we have
$$\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right| \leq C \omega\left(\tau^{k}\right)\left(d^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)}+\tau^{-k}\right)$$
Integrating along $\gamma$ we get
$$\begin{aligned}
\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right| & \leq C \omega\left(\tau^{k}\right)\left(d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)}+d \tau^{-k}\right) \\
& \leq C \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} .
\end{aligned}$$
(2) When $k \leq k_{2, p}$, we have $r_{2}(\gamma(t)) \leq r_{2}(p)+d \leq \tau^{k}+d \leq \frac{9}{8} \tau^{k}$ and similar estimates hold for $r_{1}(\gamma(t))$ too. Then by Lemma 3.18, Lemma 3.19 and (3-67) along $\gamma$ the following estimate holds
$$\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right|(\gamma(t)) \leq C \omega\left(\tau^{k}\right)\left(d^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)}+\tau^{-k}\right)$$
Integrating along $\gamma$ we get
$$\begin{aligned}
\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right| & \leq C \omega\left(\tau^{k}\right)\left(d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)}+d \tau^{-k}\right) \\
& \leq C \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} .
\end{aligned}$$

This finishes the proof of the lemma in this case.
Case 2b: $r_{p}>2 d$ but $\ell \geq k_{p}+1$. When $k \leq k_{p}$, the estimate (3-78) follows in the same way as the case above. Hence it suffices to consider the case when $k_{p}+1 \leq k \leq \ell$. In this case the balls $\hat{B}_{k}(p)=B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)$ and it can be seen by triangle inequality that the geodesic $\gamma \subset \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$. Since the metric balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}$ we can use the smooth coordinates $w_{1}=z_{1}^{\beta_{1}}$ and $w_{2}=z_{2}^{\beta_{2}}$ as before, and everything becomes smooth under these coordinates in $\hat{B}_{k}(p)$.

The estimate (3-79) can be shown by the same argument, so we skip the details. \(\square\)

Iteratively applying (3-78) for $k \leq \ell$, we get
$$\begin{aligned}
J_{2}=\left|\frac{\partial D^{\prime} u_{\ell}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} u_{\ell}}{\partial r_{1}}(q)\right| & \leq\left|\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(q)\right|+C d^{1 / \beta_{1}-1} \sum_{k=3}^{\ell} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) \\
& \leq C d^{1 / \beta_{1}-1}\left(\|u\|_{C^{0}}+\sum_{k=2}^{\ell} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right)\right),
\end{aligned}$$
where the inequality
$$\left|\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(q)\right| \leq C d^{1 / \beta_{1}-1}\|u\|_{C^{0}}$$
can be proved by the same argument as in proving (3-78).
Combining the estimates for $J_{1}, J_{2}, J_{3}, J_{4}$ we finish the proof of (1-4).

We remark that in solving (3-45) we assume $r_{1}(p) \leq r_{2}(p)$, so we need also to deal with the following case, whose proof is more or less parallel to that of Lemma 3.20, so we just point out the differences and sketch the proof.

Lemma 3.21. Let $d=d_{\boldsymbol{\beta}}(p, q)>0$. There exists a constant $C(n, \boldsymbol{\beta})>0$ such that, for all $k \leq \ell$,
$$\begin{array}{|l}
\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(q)\right| \leq C d^{1 / \beta_{2}-1} \tau^{-k\left(1 / \beta_{2}-1\right)} \omega\left(\tau^{k}\right), \\
\left|\frac{\partial D^{\prime} h_{k}}{r_{2} \partial \theta_{2}}(p)-\frac{\partial D^{\prime} h_{k}}{r_{2} \partial \theta_{2}}(q)\right| \leq C d^{1 / \beta_{2}-1} \tau^{-k\left(1 / \beta_{2}-1\right)} \omega\left(\tau^{k}\right) .
\end{array}$$
Proof. We consider the cases when $k \leq k_{1, p}$ and $k_{1, p}+1 \leq k \leq \ell$.
Case 1: $k_{1, p}+1 \leq k \leq \ell$. The balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}_{2}$, so we can introduce the complex coordinate $w_{2}=z_{2}^{\beta_{2}}$ on these balls as before. Let $t_{1}$ and $t_{2}$ be the real and imaginary parts of $w_{2}$, respectively. The derivatives estimates imply that
$$\left\|\partial_{w_{2}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)} \leq C \omega\left(\tau^{k}\right) \quad \text { and } \quad\left\|\partial_{w_{2}}^{2} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right),$$
where $\partial_{w_{2}}^{2}$ denotes the full second-order derivatives in the $\left\{t_{1}, t_{2}\right\}$-directions. Also
$$\left\|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial w_{2}}\right)\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)}+\left\|\frac{\partial}{r_{1} \partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial w_{2}}\right)\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Since
$$\frac{\partial}{\partial r_{2}}=\frac{w_{2}}{\beta_{2} r_{2}} \frac{\partial}{\partial w_{2}}+\frac{\bar{w}_{2}}{\beta_{2} r_{2}} \frac{\partial}{\partial \bar{w}_{2}},$$
we have
$$\frac{\partial}{\partial w_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)=\frac{1}{r_{2}} \frac{\partial D^{\prime} h_{k}}{\partial w_{2}}-\frac{\left|w_{2}\right|^{2}}{2 r_{2}^{3}} \frac{\partial D^{\prime} h_{k}}{\partial w_{2}}-\frac{\bar{w}_{2} \cdot \bar{w}_{2}}{2 r_{2}^{3}} \frac{\partial D^{\prime} h_{k}}{\partial \bar{w}_{2}}+\frac{w_{2}}{r_{2}} \partial_{w_{2}}^{2} D^{\prime} h_{k},$$
and we have, on $\frac{1}{2} \hat{B}_{k}(p)$,
$$\left|\frac{\partial}{\partial w_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)\right| \leq \frac{C}{r_{2}} \omega\left(\tau^{k}\right)+C \tau^{-k} \omega\left(\tau^{k}\right)$$
and
$$\left\|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)}+\left\|\frac{\partial}{r_{1} \partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 2\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Therefore,
$$\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right|^{2}=\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1} \partial r_{2}}\right|^{2}+\left|\frac{\partial^{2}}{r_{1} \partial \theta_{1} \partial r_{2}}\right|^{2}+\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial w_{2} \partial r_{2}}\right|^{2}+\sum_{j}\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial s_{j} \partial r_{2}}\right|^{2} \leq C\left(\tau^{-k} \omega\left(\tau^{k}\right)\right)^{2}+C \frac{1}{r_{2}^{2}} \omega\left(\tau^{k}\right)^{2} .$$
In this case we know that $r_{1}(p) \approx \tau^{k_{p}} \geq 2 \tau^{k} \geq \tau^{\ell}>8 d$, so along $\gamma$
$$r_{2}(\gamma(t)) \geq r_{2}(p)-d \geq r_{1}(p)-d \geq \frac{7}{4} \tau^{k} .$$

Integrating along $\gamma$ we get
$$\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) d \leq C \tau^{-k\left(1 / \beta_{2}-1\right)} \omega\left(\tau^{k}\right) d^{1 / \beta_{2}-1} .$$
Case 2: $k \leq k_{1, p}$. This case is the same as in the proof of (3-78), replacing $r_{1}$ by $r_{2}$ and $\beta_{1}$ by $\beta_{2}$. We omit the details.

We can prove (3-87) similarly. \(\square\)

3D. Mixed normal directions. In this section, we deal with Hölder continuity of the four mixed derivatives
$$\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}, \quad \frac{\partial^{2} u}{r_{1} \partial \theta_{1} \partial r_{2}}, \quad \frac{\partial^{2} u}{r_{2} \partial r_{1} \partial \theta_{2}}, \quad \frac{\partial^{2} u}{r_{1} r_{2} \partial \theta_{1} \partial \theta_{2}},$$
which by our previous notation correspond to $N_{1} N_{2} u$. Since the proof for each of them is more or less the same, we will only prove Hölder continuity for $\partial^{2} u / \partial r_{1} \partial r_{2}$. The following holds at $p$ and $q$ by the same reasoning of Lemma 3.11:
$$\lim _{k \rightarrow \infty} \frac{\partial^{2} u_{k}}{\partial r_{1} \partial r_{2}}(p)=\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial^{2} v_{k}}{\partial r_{1} \partial r_{2}}(q)=\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q) .$$
By the triangle inequality,
$$\begin{aligned}
\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| & \leq\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(p)\right|+\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right| \\
& +\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right|+\left|\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| \\
& =: L_{1}+L_{2}+L_{3}+L_{4} .
\end{aligned}$$
Lemma 3.22. We have the estimate
$$L_{1}+L_{4} \leq \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right) .$$
Proof. We consider the cases when $k \geq k_{p}+1$ and $\ell \leq k \leq k_{p}$.
Case 1: $k \geq k_{p}+1$. In this case the balls $\hat{B}_{k}(p)$ are disjoint from $\mathcal{S}$ and we can introduce the smooth coordinates $w_{1}=z_{1}^{\beta_{1}}$ and $w_{2}=z_{2}^{\beta_{2}}$. Under the coordinates $\left\{w_{1}, w_{2}, z_{3}, \ldots, z_{n}\right\}$, the cone metric $g_{\boldsymbol{\beta}}$ becomes the standard Euclidean metric $g_{\mathbb{C}^{n}}$ and the metric balls $\hat{B}_{k}(p)$ become the standard Euclidean balls with the same radius and center $p$. Since the $g_{\beta}$-harmonic functions $u_{k}-u_{k+1}$ satisfy (3-49), by standard gradient estimates for Euclidean harmonic functions, we get
$$\sup _{\hat{B}_{k}(p) / 2.1}\left|D_{w_{1}} D_{w_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right),$$
where we use $D_{w_{i}}$ to denote either $\partial / \partial w_{i}$ or $\partial / \partial \bar{w}_{i}$ for simplicity. From (3-88) and a similar formula for $\partial / \partial r_{1}$, we get
$$\sup _{\hat{B}_{k}(p) / 2.1}\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right) .$$

Case 2a: $\ell \geq k_{2, p}+1$ and $\ell \leq k_{p}=k_{1, p}$. For all $\ell \leq k$, the balls $\hat{B}_{k}(p)$ are disjoint from $\mathcal{S}_{2}$ and centered at $p_{1}$. We can still use $w_{2}=z_{2}^{\beta_{2}}$ as the smooth coordinate. The cone metric $g_{\beta}$ becomes smooth in the $w_{2}$-variable, and we can apply the standard gradient estimate to the $g_{\beta}$-harmonic function $D_{w_{2}}\left(u_{k}-u_{k-1}\right)$ to get
$$\sup _{\hat{B}_{k}(p) / 2.2}\left|\frac{\partial}{\partial r_{1}} D_{w_{2}}\left(u_{k}-u_{k-1}\right)\right|+\left|\frac{\partial}{r_{1} \partial \theta_{1}} D_{w_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right) .$$
Again by (3-88), we get
$$\sup _{\hat{B}_{k}(p) / 2.2}\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|+\left|\frac{\partial^{2}}{r_{1} \partial \theta_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right) .$$
Case 2b: $\ell \leq k_{2, p}$ and $k \geq k_{2, p}+1$. This case can be dealt with similarly as above.
Case 2c: $\ell \leq k \leq k_{2, p}$. In this case $r_{2}(p) \approx \tau^{k_{2, p}} \leq \tau^{k} \leq \tau^{\ell} \approx 8 d$. Now the balls $\hat{B}_{k}(p)$ are centered at $p_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$. We can proceed as in the proof of Lemma 3.19, with the harmonic functions $u_{k}-u_{k-1}$ replacing the $D^{\prime} h_{k}$ in that lemma to prove that, for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(z)+\left|\frac{\partial^{2}}{r_{2} \partial \theta_{2} \partial r_{1}}\left(u_{k}-u_{k-1}\right)\right| & (z) \\
& \leq C(n, \boldsymbol{\beta}) r_{1}(z)^{1 / \beta_{1}-1} r_{2}(z)^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
In particular, the estimate in each case holds at $p$, and from $r_{1}(p) \leq r_{2}(p) \leq \tau^{k}$ we obtain
$$\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(p)+\left|\frac{\partial^{2}}{r_{2} \partial \theta_{2} \partial r_{1}}\left(u_{k}-u_{k-1}\right)\right|(p) \leq C \omega\left(\tau^{k}\right) .$$
Combining each case above, by (3-90)-(3-92), we get, for all $k \geq \ell$,
$$\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(p) \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{k}\right) .$$
Therefore, by the triangle inequality,
$$L_{1} \leq \sum_{k=\ell+1}^{\infty}\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(p) \leq C(n, \boldsymbol{\beta}) \sum_{k=\ell+1}^{\infty} \omega\left(\tau^{k}\right) .$$
The estimate for $L_{4}$ can be dealt with similarly by studying the derivatives of $v_{k}$ at $q$. \(\square\)

Lemma 3.23.
$$L_{3} \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$

Proof. As in the proof of Lemma 3.22, we consider the cases $\ell \geq k_{1, p}+1, k_{1, p} \geq \ell \geq k_{2, p}$ and $\ell \leq k_{2, p}-1$.
Case 1: $\ell \geq k_{1, p}+1$. Here the ball $\hat{B}_{\ell}(p)$ is equal to $B_{\beta}\left(p, \tau^{\ell}\right)$, the function $U$ defined in (3-55) is $g_{\beta}$-harmonic in $\frac{1}{2} \hat{B}_{\ell}(p)$, and $\sup _{\hat{B}_{\ell}(p) / 2}|U| \leq C \omega^{2 \ell} \omega\left(\tau^{\ell}\right)$. Since the ball $\frac{1}{2} \hat{B}_{\ell}(p)$ is disjoint from $\mathcal{S}$, we have that $w_{1}$ and $w_{2}$ are well defined on $\frac{1}{2} \hat{B}_{\ell}(p)$, and thus we have the derivatives estimates
$$\sup _{\hat{B}_{\ell}(p) / 3}\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}\right| \leq \sup _{\hat{B}_{\ell}(p) / 3}\left|D_{w_{1}} D_{w_{2}} U\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$