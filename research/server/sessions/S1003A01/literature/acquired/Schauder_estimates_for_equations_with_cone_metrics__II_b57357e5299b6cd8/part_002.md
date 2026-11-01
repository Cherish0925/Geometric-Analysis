---
retention_scope: session
part: 2
total_parts: 5
---

[Part 2/5 of: Schauder estimates for equations with cone metrics, II]

By considering the barrier function $\varphi(q)+\delta-A \Psi_{q}(z)$ and similar argument it is not hard to see that $\limsup _{z \rightarrow q} u(z) \leq \varphi(q)$, hence $\lim _{z \rightarrow q} u(z)=\varphi(q)$ and $u$ is continuous up to $q \in \partial B_{\boldsymbol{\beta}}(0,1)$.

Case 2: $q \in \partial B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}_{1} \cap \mathcal{S}_{2}$. We consider the case when $z_{1}(q) \neq 0$ and $z_{2}(q) \neq 0$. The boundary $\partial B_{\boldsymbol{\beta}}(0,1)$ is smooth near $q$, hence satisfies the exterior sphere condition. We choose an exterior Euclidean ball $B_{\mathbb{C}^{n}}\left(\tilde{q}, r_{q}\right)$ which is tangential with $\partial B_{\boldsymbol{\beta}}(0,1)$ (only) at $q$, i.e. under the Euclidean distance $q$ is the unique closest point to $\tilde{q}$ on $\partial B_{\boldsymbol{\beta}}(0,1)$. So the function $G(z)=\frac{1}{|z-\tilde{q}|^{2 n-2}}-\frac{1}{r_{q}^{2 n-2}}$ satisfies $G(q)=0$ and $G(z)<0$ for all $z \in \partial B_{\boldsymbol{\beta}}(0,1) \backslash\{q\}$. We calculate
$$\begin{aligned}
\Delta_{g_{\epsilon}} G & =\left(\left|z_{1}\right|^{2}+\epsilon\right)^{-\beta_{1}+1} \frac{\partial^{2} G}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left|z_{2}\right|^{2}+\epsilon\right)^{-\beta_{2}+1} \frac{\partial^{2} G}{\partial z_{2} \partial \bar{z}_{2}}+\sum_{k=3}^{n} \frac{\partial^{2} G}{\partial z_{k} \partial \bar{z}_{k}} \\
& =\left(\left(\left|z_{1}\right|^{2}+\epsilon\right)^{-\beta_{1}+1}-1\right) \frac{\partial^{2} G}{\partial z_{1} \partial \bar{z}_{1}}+\left(\left(\left|z_{2}\right|^{2}+\epsilon\right)^{-\beta_{2}+1}-1\right) \frac{\partial^{2} G}{\partial z_{2} \partial \bar{z}_{2}} \\
& =\sum_{k=1}^{2}(-n+1) \frac{\left(\left|z_{k}\right|^{2}+\epsilon\right)^{-\beta_{k}+1}-1}{|z-\tilde{q}|^{2 n}}\left(-\frac{n\left|z_{k}-\tilde{q}_{k}\right|^{2}}{|z-\tilde{q}|^{2}}+1\right) \\
& \geq-C\left(q, r_{q}\right) .
\end{aligned}$$
The function $\Psi_{q}(z)=A\left(d_{\boldsymbol{\beta}}(z, 0)^{2}-1\right)+G(z)$ is $\Delta_{g_{\epsilon}}$-subharmonic for $A \gg 1$ and $\Psi_{q}(q)=0$, $\Psi_{q}(z)<0$ for $\forall z \in \partial B_{\boldsymbol{\beta}}(0,1) \backslash\{q\}$. We are in the same situation as the Case 1, so by the same argument as above, we can show the continuity of $u$ at such boundary point $q$.

In case $z_{1}(q) \neq 0$ but $z_{2}(q)=0$. The boundary $\partial B_{\boldsymbol{\beta}}(0,1)$ is not smooth at $q$ and we cannot apply the exterior sphere condition to construct the barrier. Instead we will use the geometry of the metric ball $B_{\boldsymbol{\beta}}(0,1)$. Consider the standard cone metric $g_{\beta_{1}}=\beta_{1}^{2} \frac{d z_{1} \otimes d \bar{z}_{1}}{\left|z_{1}\right|^{2\left(1-\beta_{1}\right)}}+\sum_{k=2}^{n} d z_{k} \otimes d \bar{z}_{k}$ with cone singularity only along $\mathcal{S}_{1}=\left\{z_{1}=0\right\}$. The metric ball $B_{\boldsymbol{\beta}}(0,1)$ is strictly contained in $B_{g_{\beta_{1}}}(0,1)$, and their boundaries are tangential at the points with vanishing $z_{2}$-coordinate. Thus $q \in \partial B_{\boldsymbol{\beta}}(0,1) \cap \partial B_{g_{\beta_{1}}}(0,1)$ and $\partial B_{g_{\beta_{1}}}(0,1)$ is smooth at $q$ so there exists an exterior sphere for $\partial B_{g_{\beta_{1}}}(0,1)$ at $q$. We define similar function $G(z)$ as in the last paragraph, and by the strict inclusion of the metric balls $B_{\boldsymbol{\beta}}(0,1) \subset B_{g_{\beta_{1}}}(0,1)$, it follows that $G(q)=0$ and $G(z)<0$ for all $z \in \partial B_{\boldsymbol{\beta}}(0,1) \backslash\{q\}$. The remaining argument is the same as before. \(\square\)

Remark 3.1. For any constant $c \in \mathbb{R}$, the following Dirichlet boundary value problem
$$\Delta_{g_{\beta}} u=c, \text { in } B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}, \text { and } u=\varphi, \text { on } \partial B_{\boldsymbol{\beta}}(0,1),$$
admits a solution $u \in C^{2}\left(B_{\boldsymbol{\beta}} \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ for any given $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}\right)$. This follows from the solution $\tilde{u}$ of (3.1) with the boundary value $\tilde{\varphi}=\varphi-\frac{c}{2(n-2)} \sum_{j=5}^{2 n} s_{j}^{2}$. Then the function $u=\tilde{u}+\frac{c}{2(n-2)} \sum_{j} s_{j}^{2}$ solves the equation above.

For later application, we prove the existence of solution for a more general RHS of the Laplace equation with the standard background metric. Note that this result is not needed in the proof of Theorem 1.1.
Proposition 3.2. For any given $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$ and $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$, the Dirichlet boundary value problem
$$\left\{\begin{array}{l}
\Delta_{g_{\beta}} v=f, \text { in } B_{\beta}(0,1) \backslash \mathcal{S}, \\
v=\varphi, \text { on } \partial B_{\beta}(0,1)
\end{array}\right.$$
admits a unique solution $v \in C^{2}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$.
By Theorem 1.1, the solution $v$ to (3.38) belongs to $C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$.
Proof. The proof is similar to that of Proposition 3.1. As before let $g_{\epsilon}$ be the approximating metrics (3.3) of $g_{\boldsymbol{\beta}}$ which are smooth metrics on $B_{\boldsymbol{\beta}}(0,1)$. By standard elliptic theory we can solve the equations
$$\left\{\begin{array}{c}
\Delta_{g_{\epsilon}} v_{\epsilon}=f, \text { in } B_{\boldsymbol{\beta}}(0,1), \\
v_{\epsilon}=\varphi, \text { on } \partial B_{\boldsymbol{\beta}}(0,1) .
\end{array}\right.$$
For any compact subset $K \Subset B_{\boldsymbol{\beta}}(0,1)$ and small $\delta>0$, we have uniform $C^{2, \alpha^{\prime}}$-bound of $v_{\epsilon}$ on $K \backslash T_{\delta}(\mathcal{S})$ for some $\alpha^{\prime}<\alpha$. Thus $v_{\epsilon}$ converges in $C^{2, \alpha^{\prime}}$-norm to a function $v$ on $K \backslash T_{\delta}(\mathcal{S})$, as $\epsilon \rightarrow 0$. By a standard diagonal argument, setting $K \rightarrow B_{\boldsymbol{\beta}}(0,1)$ and $\delta \rightarrow 0$, we can achieve that
$$v_{\epsilon} \xrightarrow{C_{l o c}^{2, \alpha^{\prime}}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right)} v \in C_{l o c}^{2, \alpha^{\prime}}\left(B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}\right), \text { as } \epsilon \rightarrow 0 .$$
And clearly $v$ satisfies the equation (3.38) in $B_{\boldsymbol{\beta}}(0,1) \backslash \mathcal{S}$. It only remains to show the boundary value of $v$ coincides with $\varphi$ and $v$ is globally continuous in $B_{\boldsymbol{\beta}}(0,1)$.
- $v \in C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right)$. It suffices to show $v$ is continuous at any $p \in \mathcal{S} \cap B_{\boldsymbol{\beta}}(0,1)$. Fix such a point $p$ and take $R_{0}>0$ small so that $B_{\mathbb{C}^{n}}\left(p, 10 R_{0}\right) \cap \partial B_{\boldsymbol{\beta}}(0,1)=\emptyset$. We observe that $\frac{1}{2} g_{\mathbb{C}^{n}} \leq g_{\epsilon} \leq g_{\boldsymbol{\beta}}$, so for any $r \in(0,1 / 2)$
$$B_{g_{\beta}}(p, r) \subset B_{g_{\epsilon}}(p, r) \subset B_{\mathbb{C}^{n}}(p, 2 r),$$
in particular, the balls $B_{g_{\epsilon}}\left(p, 5 R_{0}\right)$ are also disjoint with $\partial B_{\boldsymbol{\beta}}(0,1)$.
Since $\operatorname{Ric}\left(g_{\epsilon}\right) \geq 0$ we have the following Sobolev inequality ([25]): there exists a constant $C=$ $C(n)>0$ such that for any $h \in C_{0}^{1}\left(B_{g_{\epsilon}}(p, r)\right)$, it holds that
$$\left(\int_{B_{g_{\epsilon}}(p, r)} h^{\frac{2 n}{n-1}} \omega_{\epsilon}^{n}\right)^{\frac{n-1}{n}} \leq C\left(\frac{r^{2 n}}{\operatorname{Vol}_{g_{\epsilon}}\left(B_{g_{\epsilon}}(p, r)\right)}\right)^{1 / n} \int_{B_{g_{\epsilon}}(p, r)}|\nabla h|_{g_{\epsilon}}^{2} \omega_{\epsilon}^{n} .$$
It can be checked by straightforward calculations that $\operatorname{Vol}_{g_{\epsilon}}\left(B_{g_{\epsilon}}(p, 1)\right) \geq c_{0}(n)>0$ for some constant $c_{0}$ independent of $\epsilon$. Then Bishop volume comparison yields that for any $r \in(0,1)$,
$$C_{1}(n) r^{2 n} \geq \operatorname{Vol}_{g_{\epsilon}}\left(B_{g_{\epsilon}}(p, r)\right) \geq c_{1}(n) r^{2 n} .$$
Thus the Sobolev inequality (3.41) is reduced to
$$\left(\int_{B_{g_{\epsilon}}(p, r)} h^{\frac{2 n}{n-1}} \omega_{\epsilon}^{n}\right)^{\frac{n-1}{n}} \leq C \int_{B_{g_{\epsilon}}(p, r)}|\nabla h|_{g_{\epsilon}}^{2} \omega_{\epsilon}^{n}, \quad \forall h \in C_{0}^{1}\left(B_{g_{\epsilon}}(p, r)\right) .$$

With (3.42) at hand, we can apply the same proof of the standard De Giorgi-Nash-Moser theory (see the proof of Corollary 4.18 of [22]) to derive the uniform Hölder continuity of $v_{\epsilon}$ at $p$, i.e. there exists a constant $C=C\left(n, \boldsymbol{\beta}, R_{0}\right)>0$ such that
$$\operatorname{osc}_{B_{\boldsymbol{\beta}}(p, r)} v_{\epsilon} \leq \operatorname{osc}_{B_{g_{\epsilon}}(p, r)} v_{\epsilon} \leq C r^{\alpha^{\prime \prime}}, \quad \forall r \in\left(0, R_{0}\right)$$
for some $\alpha^{\prime \prime}=\alpha^{\prime \prime}\left(n, \boldsymbol{\beta}, R_{0}\right) \in(0,1)$ where in the first inequality we use the relation (3.40). Letting $\epsilon \rightarrow 0$ we see the continuity of $v$ at $p$.
- $v=\varphi$ on $\partial B_{\boldsymbol{\beta}}(0,1)$. The proof is almost identical to that of Proposition 3.1. For example, the function $\varphi_{q}(z)=\varphi(q)-\delta+A \Psi_{q}(z)$ defined in Case 1 in the proof of Proposition 3.1 satisfies $\Delta_{g_{\epsilon}} \varphi_{q}(z) \geq \max _{X} f$ if $A>0$ is taken large enough. Then from $\Delta_{g_{\epsilon}}\left(\varphi_{q}-v_{\epsilon}\right) \geq 0$ in $B_{\boldsymbol{\beta}}$ and $\varphi_{q}-\varphi \leq 0$ on $\partial B_{\boldsymbol{\beta}}$, applying maximum principle we get $\varphi_{q} \leq v_{\epsilon}$ in $B_{\boldsymbol{\beta}}(0,1)$. The remaining are the same as in Proposition 3.1. The Case 2 can be dealt with similarly. \(\square\)

Remark 3.2. Let $H_{0}^{1}\left(B_{\boldsymbol{\beta}}(0,1), g_{\boldsymbol{\beta}}\right)$ be the completion of the space $C_{0}^{1}\left(B_{\boldsymbol{\beta}}(0,1)\right)$-functions under the norm
$$\|\nabla u\|_{L^{2}\left(g_{\boldsymbol{\beta}}\right)}=\left(\int_{B_{\boldsymbol{\beta}}(0,1)}|\nabla u|_{g_{\boldsymbol{\beta}}}^{2} \omega_{\boldsymbol{\beta}}^{n}\right)^{1 / 2} .$$
For any $h \in C_{0}^{1}\left(B_{\boldsymbol{\beta}}(0,1)\right)$, letting $\epsilon \rightarrow 0$ in (3.42) we get
$$\left(\int_{B_{\boldsymbol{\beta}}(p, r)}|h|^{\frac{2 n}{n-1}} \omega_{\boldsymbol{\beta}}^{n}\right)^{\frac{n-1}{n}} \leq C \int_{B_{\boldsymbol{\beta}}(p, r)}|\nabla h|_{g_{\boldsymbol{\beta}}}^{2} \omega_{\boldsymbol{\beta}}^{n},$$
for the same constant $C$ in (3.42). That is, Sobolev inequality also holds for the conical metric $\omega_{\boldsymbol{\beta}}$.

\subsection*{3.2. Tangential and Laplacian estimates}

In this section, we will prove the Hölder continuity of $\Delta_{k} u$ for $k=1,2$ and $\left(D^{\prime}\right)^{2} u$ for the solution $u$ to (1.2). The arguments of [20] can be adopted here. We recall that we assume $\beta_{1}, \beta_{2} \in\left(\frac{1}{2}, 1\right)$. We fix some notations first.

For a given point $p \notin \mathcal{S}$, we denote $r_{p}=d_{g_{\beta}}(p, \mathcal{S})$, the $g_{\beta}$-distance of $p$ to the singular set $\mathcal{S}$. For notation simplicity we will fix $\tau=1 / 2$ and an integer $k_{p} \in \mathbb{Z}_{+}$to be the smallest integer such that $\tau^{k}<r_{p}$, and $k_{i, p} \in \mathbb{Z}_{+}$the smallest integer $k$ such that $\tau^{k}<d_{\boldsymbol{\beta}}\left(p, \mathcal{S}_{i}\right)$, for $i=1,2$. So $k_{p}=\max \left\{k_{1, p}, k_{2, p}\right\}$ We denote $p_{1} \in \mathcal{S}_{1}$ and $p_{2} \in \mathcal{S}_{2}$ the projections of $p$ to $\mathcal{S}_{1}, \mathcal{S}_{2}$, respectively.

For $j=1,2$ we will write $\Delta_{j} u:=\left|z_{j}\right|^{2\left(1-\beta_{j}\right)} \frac{\partial^{2} u}{\partial z_{j} \partial \bar{z}_{j}}$.
We will consider a family of conical Laplace equations with different choices of $k \in \mathbb{Z}^{+}$.
\begin{itemize}
\item[(i)] If $k \geq k_{p}$, the geodesic balls $B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)$ are disjoint with $\mathcal{S}$ and have smooth boundaries. $g_{\boldsymbol{\beta}}$ is smooth on such balls. By standard theory we can solve the Dirichlet problem for $u_{k} \in C^{\infty}\left(B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)}\right)$
$$\left\{\begin{array}{lr}
\Delta_{\boldsymbol{\beta}} u_{k}=f(p), & \text { in } B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right) \\
u_{k}=u, & \text { on } \partial B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)
\end{array}\right.$$
\item[(ii)] Without loss of generality we assume $d_{\boldsymbol{\beta}}\left(p, \mathcal{S}_{1}\right) \leq d_{\boldsymbol{\beta}}\left(p, \mathcal{S}_{2}\right)$, i.e. $k_{1, p} \geq k_{2, p}$. We now solve the Dirichlet problem $u_{k} \in C^{2}\left(B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{k}\right) \backslash \mathcal{S}_{1}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{k}\right)}\right)$ for $k_{2, p}+2 \leq k<k_{1, p}$
$$\left\{\begin{array}{lr}
\Delta_{\boldsymbol{\beta}} u_{k}=f(p), & \text { in } B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{k}\right) \\
u_{k}=u, & \text { on } \partial B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{k}\right)
\end{array}\right.$$
\end{itemize}

By similar argument as in the proof of Proposition 3.1, such $u_{k}$ exists.
\begin{itemize}
\item[(iii)] For $2 \leq k \leq k_{2, p}+1$, let $u_{k} \in C^{2}\left(B_{\boldsymbol{\beta}}\left(p_{1,2}, 2 \tau^{k}\right) \backslash \mathcal{S}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}\left(p_{1,2}, 2 \tau^{k}\right)}\right)$ solve the equation
$$\left\{\begin{array}{lr}
\Delta_{\boldsymbol{\beta}} u_{k}=f(p), & \text { in } B_{\boldsymbol{\beta}}\left(p_{1,2}, 2 \tau^{k}\right) \\
u_{k}=u, & \text { on } \partial B_{\boldsymbol{\beta}}\left(p_{1,2}, 2 \tau^{k}\right)
\end{array}\right.$$
whose existence follows from Remark 3.1. Here $p_{1,2}=(0 ; 0 ; s(p)) \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ is the projection of $p_{1}$ to $\mathcal{S}_{2}$.
\end{itemize}

We remark that we may take $f(p)=0$ by considering $\tilde{u}=u-\frac{f(p)}{2(n-2)}|s-s(p)|^{2}$. If the estimate holds for $\tilde{u}$, it also holds for $u$. So from now on we assume $f(p)=0$.

Lemma 3.5. Let $u_{k}$ be the solutions to the equations (3.44), (3.45) and (3.46). There exists a constant $C=C(n)>0$ such that for all $k \in \mathbb{Z}_{+}$, the following estimates hold
$$\left\|u_{k}-u\right\|_{L^{\infty}\left(\hat{B}_{k}(p)\right)} \leq C(n) \tau^{2 k} \omega\left(\tau^{k}\right),$$
where we denote $\hat{B}_{k}(p)$ by
$$\hat{B}_{k}(p):=\left\{\begin{array}{l}
B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right), \text { if } k \geq k_{p} \\
B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{k}\right), \text { if } k_{2, p}+2 \leq k<k_{1, p} \\
B_{\boldsymbol{\beta}}\left(p_{1,2}, 2 \tau^{k}\right), \text { if } 1 \leq k \leq k_{2, p}+1,
\end{array}\right.$$
in different choices of $k \in \mathbb{Z}_{+}$.
We will also denote $\lambda \hat{B}_{k}(p)$ to the concentric ball with $\hat{B}_{k}(p)$ but the radius scaled by $\lambda \in(0,1)$. This lemma follows straightforwardly from Lemma 3.1 and the definition of $\omega(r)$. So we omit the proof. By triangle inequality, we get the following estimates
$$\left\|u_{k}-u_{k+1}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}\right)} \leq C(n) \tau^{2 k} \omega\left(\tau^{k}\right),$$

Since $u_{k}-u_{k+1}$ are $g_{\beta}$-harmonic functions on $\frac{1}{2} \hat{B}_{k}$, applying the gradient and Laplacian estimates (3.5) and (3.9) for harmonic functions, we get:

Lemma 3.6. There exists a constant $C(n)>0$ such that for all $k \in \mathbb{Z}_{+}$it holds that
$$\left\|D^{\prime} u_{k}-D^{\prime} u_{k+1}\right\|_{L^{\infty}\left(\frac{1}{3} \hat{B}_{k}\right)} \leq C(n) \tau^{k} \omega\left(\tau^{k}\right),$$
and
$$\sup _{\frac{1}{3} \hat{B}_{k} \backslash \mathcal{S}}\left(\sum_{i=1}^{2}\left|\Delta_{i}\left(u_{k}-u_{k+1}\right)\right|+\left|\left(D^{\prime}\right)^{2} u_{k}-\left(D^{\prime}\right)^{2} u_{k+1}\right|\right) \leq C(n) \omega\left(\tau^{k}\right),$$
where we recall that $D^{\prime}$ denotes the first order operators $\frac{\partial}{\partial s_{i}}$ for $i=5, \ldots, 2 n$.
The following lemma can be proved by looking at the Taylor expansion of $u_{k}$ at $p$ for $k \gg 1$ as in Lemma 2.8 of [20].

Lemma 3.7. The following limits hold:
$$\lim _{k \rightarrow \infty} D^{\prime} u_{k}(p)=D^{\prime} u(p), \lim _{k \rightarrow \infty}\left(D^{\prime}\right)^{2} u_{k}(p)=\left(D^{\prime}\right)^{2} u(p), \lim _{k \rightarrow \infty} \Delta_{i} u_{k}(p)=\Delta_{i} u(p),$$
where $i=1,2$.
Combining Lemmas 3.6 and 3.7, we obtain the following estimates on the 2nd-order (tangential) derivatives.

Proposition 3.3. There exists a constant $C=C(n, \beta)>0$ such that
$$\sup _{B_{\boldsymbol{\beta}}(0,1 / 2) \backslash \mathcal{S}}\left|\left(D^{\prime}\right)^{2} u\right|+\left|\Delta_{i} u\right| \leq C\left(\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\int_{0}^{1} \frac{\omega(r)}{r} d r+|f(0)|\right) .$$
Proof. From triangle inequality we have for any given $z \in B_{\boldsymbol{\beta}}(0,1 / 2) \backslash \mathcal{S}$
$$\begin{aligned}
\left|\left(D^{\prime}\right)^{2} u(z)\right| & \leq \sum_{k=0}^{\infty}\left|\left(D^{\prime}\right)^{2} u_{k}(z)-\left(D^{\prime}\right)^{2} u_{k+1}(z)\right|+\left|\left(D^{\prime}\right)^{2} u_{1}(z)\right| \\
& \leq C(n) \sum_{k=1}^{\infty} \omega\left(\tau^{k}\right)+C(n) \operatorname{osc}_{B_{\boldsymbol{\beta}}(0,1)} u_{0} \\
& \leq C(n, \boldsymbol{\beta})\left(\|u\|_{L^{\infty}}+\int_{0}^{1} \frac{\omega(r)}{r} d r+|f(0)|\right) .
\end{aligned}$$
The estimates for $\Delta_{i} u$ can be proved similarly. \(\square\)

For any other given point $q \in B_{\boldsymbol{\beta}}(0,1 / 2) \backslash \mathcal{S}$, we can solve Dirichlet boundary problems as $u_{k}$ with the metric balls centered at $q$, and we obtain a family of functions $v_{k}$ such that
$$\Delta_{\boldsymbol{\beta}} v_{k}=f(q), \quad \text { in } \tilde{B}_{k}(q), \quad v_{k}=u \text { on } \partial \tilde{B}_{k}(q),$$
where $\tilde{B}_{k}(q)$ are metrics balls centered at $q$ given by
$$\tilde{B}_{k}(q)=\tilde{B}_{k}:=\left\{\begin{array}{l}
B_{\boldsymbol{\beta}}\left(q, \tau^{k}\right), \text { if } k \geq k_{q}, \\
B_{\boldsymbol{\beta}}\left(q_{i}, 2 \tau^{k}\right), \text { if } k_{j, q}+2 \leq k<k_{q}, \text { here } k_{i, q}=\max \left(k_{1, q}, k_{2, q}\right) \text { and } j \neq i \\
B_{\boldsymbol{\beta}}\left(q_{i, j}, 2 \tau^{k}\right), \text { if } k \leq k_{j, q}+1 .
\end{array}\right.$$
Similar estimates as in Lemmas 3.5, 3.6 and 3.6 also hold for $v_{k}$ within the balls $\tilde{B}_{k}(q)$.
We are now ready to state the main result in this subsection on the continuity of second order derivatives.

Proposition 3.4. Let $d=d_{\boldsymbol{\beta}}(p, q)$. There exists a constant $C=C(n)>0$ such that if $u$ solves the conical Laplace equation (1.2), then the following holds for $i=1,2$ :
$$\left|\Delta_{i} u(p)-\Delta_{i} u(q)\right|+\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \leq C\left(d\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d \int_{d}^{1} \frac{\omega(r)}{r^{2}} d r\right) .$$
Proof. We only prove the estimate for $\left(D^{\prime}\right)^{2} u$, and the one for $\Delta_{i} u$ can be dealt with in the same way.

We may assume $r_{p}=\min \left(r_{p}, r_{q}\right)$. We fix an integer $\ell$ such that $\tau^{\ell}$ is comparable to $d$, more precisely, we take
$$\tau^{\ell+4} \leq d<\tau^{\ell+3}, \quad \text { or } \quad \tau^{\ell+1} \leq 8 d \leq \tau^{\ell} .$$
We calculate by triangle inequality
$$\begin{aligned}
\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \leq & \left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u_{\ell}(p)\right|+\left|\left(D^{\prime}\right)^{2} u_{\ell}(p)-\left(D^{\prime}\right)^{2} u_{\ell}(q)\right| \\
& +\left|\left(D^{\prime}\right)^{2} u_{\ell}(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right|+\left|\left(D^{\prime}\right)^{2} v_{\ell}(q)-\left(D^{\prime}\right)^{2} u(q)\right| \\
= & : I_{1}+I_{2}+I_{3}+I_{4} .
\end{aligned}$$
We will estimate $I_{1}-I_{4}$ one by one.
- $I_{1}$ and $I_{4}$ : by (3.51) and (3.52) we have
$$I_{1}=\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u_{\ell}(p)\right| \leq C(n) \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right),$$
and similar estimate holds for $I_{4}$ as well
$$I_{4}=\left|\left(D^{\prime}\right)^{2} u(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right| \leq C(n) \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right) .$$
- $I_{3}$ : by the choice of $\ell$, it is not hard to see that $\frac{2}{3} \tilde{B}_{\ell}(q) \subset \hat{B}_{\ell}(p)$. In particular $u_{\ell}$ and $v_{\ell}$ are both defined on $\frac{2}{3} \tilde{B}_{\ell}(q)$ and satisfy the equations
$$\Delta_{\boldsymbol{\beta}} u_{\ell}=f(p), \quad \Delta_{\boldsymbol{\beta}} v_{\ell}=f(q)$$
respectively on this ball. From (3.47) for $u_{\ell}$ and similar estimate for $v_{\ell}$ we get
$$\left\|u_{\ell}-v_{\ell}\right\|_{L^{\infty}\left(\frac{2}{3} \tilde{B}_{\ell}(q)\right)} \leq C \tau^{2 \ell} \omega\left(\tau^{\ell}\right) .$$
Consider the function
$$U:=u_{\ell}-v_{\ell}-\frac{f(p)-f(q)}{2(n-2)}|s-s(\tilde{q})|^{2}$$
where $\tilde{q}$ is the center of the ball $\tilde{B}_{\ell}(q) . U$ is $g_{\boldsymbol{\beta}}$-harmonic in $\frac{2}{3} \tilde{B}_{\ell}(q)$ and satisfies the estimate:
$$\|U\|_{L^{\infty}\left(\frac{2}{3} \tilde{B}_{\ell}(q)\right)} \leq C \tau^{2 \ell} \omega\left(\tau^{\ell}\right)+C \tau^{2 \ell} \omega(d) \leq C(n) \tau^{2 \ell} \omega\left(\tau^{\ell}\right) .$$
The derivatives estimates imply that
$$\left|\left(D^{\prime}\right)^{2} U(q)\right| \leq C \tau^{-2 \ell}\|U\|_{L^{\infty}\left(\frac{2}{3} \tilde{B}_{\ell}(q)\right)} \leq C(n) \omega\left(\tau^{\ell}\right) .$$
Hence
$$I_{3}=\left|\left(D^{\prime}\right)^{2} u_{\ell}(q)-\left(D^{\prime}\right)^{2} v_{\ell}(q)\right| \leq C(n) \omega\left(\tau^{\ell}\right) .$$
- $I_{2}$ : this is a little more complicated than the previous estimates. We define $h_{k}=u_{k-1}-u_{k}$ for $k \leq \ell$. $h_{k}$ is $g_{\boldsymbol{\beta}}$-harmonic on $\hat{B}_{k}(p)$ and by (3.47) $h_{k}$ satisfies the $L^{\infty}$-estimate $\left\|h_{k}\right\|_{\hat{B}_{k}(p)} \leq C \tau^{2 k} \omega\left(\tau^{k}\right)$ and the derivative estimates $\left\|\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(\frac{2}{3} \hat{B}_{k}(p)\right)} \leq C \omega\left(\tau^{k}\right)$. On the other hand, the function $\left(D^{\prime}\right)^{2} h_{k}$ is also $g_{\beta}$-harmonic on $\frac{2}{3} \hat{B}_{k}(p)$ so the gradient estimate implies that
$$\left\|\nabla_{g_{\boldsymbol{\beta}}}\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
Integrating this along the minimal $g_{\boldsymbol{\beta}}$-geodesic $\gamma$ connecting $p$ and $q$ and noting that $\gamma$ avoids $\mathcal{S}$ since $\left(\mathbb{C}^{n} \backslash \mathcal{S}, g_{\boldsymbol{\beta}}\right)$ is strictly geodesically convex, we get
$$\left|\left(D^{\prime}\right)^{2} h_{k}(p)-\left(D^{\prime}\right)^{2} h_{k}(q)\right| \leq d \cdot\left\|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}\right)} \leq d C \tau^{-k} \omega\left(\tau^{k}\right) .$$
By triangle inequality for each $k \leq \ell$
$$I_{2}=\left|\left(D^{\prime}\right)^{2} u_{\ell}(p)-\left(D^{\prime}\right)^{2} u_{\ell}(q)\right| \leq\left|\left(D^{\prime}\right)^{2} u_{2}(p)-\left(D^{\prime}\right)^{2} u_{2}(q)\right|+d C \sum_{k=2}^{\ell} \tau^{-k} \omega\left(\tau^{k}\right) .$$
Observe that $p, q \in \hat{B}_{2}(p)$ and the function $\left(D^{\prime}\right)^{2} u_{2}$ is $g_{\beta}$-harmonic on $\hat{B}_{2}(p)$. From (3.47) and derivative estimates we have
$$\left\|\left(D^{\prime}\right)^{2} u_{2}\right\|_{L^{\infty}\left(\frac{2}{3} \hat{B}_{2}(p)\right)} \leq C\left\|u_{2}\right\|_{L^{\infty}\left(\hat{B}_{2}(p)\right)} \leq C\left(\|u\|_{L^{\infty}}+\omega\left(\tau^{2}\right)\right) .$$

Again by gradient estimate we have
$$\left\|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} u_{2}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{2}(p)\right)} \leq C\left(\|u\|_{L^{\infty}}+\omega\left(\tau^{2}\right)\right) .$$
Integrating along the minimal geodesic $\gamma$ we arrive at
$$\left|\left(D^{\prime}\right)^{2} u_{2}(p)-\left(D^{\prime}\right)^{2} u_{2}(q)\right| \leq d C\left(\|u\|_{L^{\infty}}+\omega\left(\tau^{2}\right)\right) .$$
Combining (3.57), we obtain that
$$I_{2} \leq C d\left(\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\sum_{k=2}^{\ell} \tau^{-k} \omega\left(\tau^{k}\right)\right) .$$
Combing this with the estimates for $I_{1}, I_{2}, I_{3}, I_{4}$, we get
$$\left|\left(D^{\prime}\right)^{2} u(p)-\left(D^{\prime}\right)^{2} u(q)\right| \leq C\left(d\left(\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\sum_{k=2}^{\ell} \tau^{-k} \omega\left(\tau^{k}\right)\right)+\sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right)\right) .$$
Proposition 3.4 now follows from this and the fact that $\omega(r)$ is monotonically increasing. \(\square\)

\subsection*{3.3. Mixed normal-tangential estimates along the directions $\mathcal{S}$}

Throughout this section, we fix two points $p, q \in B_{\boldsymbol{\beta}}(0,1 / 2) \backslash \mathcal{S}$ and assume $r_{p} \leq r_{q}$. Recall that we introduce the weighted "polar coordinates" $\left(r_{i}, \theta_{i}\right)$ for $\left(z_{1}, z_{2}\right)$ as
$$\rho_{i}=\left|z_{i}\right|, r_{i}=\rho_{i}^{\beta_{i}}, \theta_{i}=\arg z_{i}, \quad i=1,2 .$$
Under these coordinates it holds that
$$\Delta_{i} u=\left|z_{i}\right|^{2\left(1-\beta_{i}\right)} \frac{\partial^{2} u}{\partial z_{i} \partial \bar{z}_{i}}=\frac{\partial^{2} u}{\partial r_{i}^{2}}+\frac{1}{r_{i}} \frac{\partial u}{\partial r_{i}}+\frac{1}{\beta_{i}^{2} r_{i}^{2}} \frac{\partial^{2} u}{\partial \theta_{i}^{2}} .$$
Let $u_{k}$ (resp. $v_{k}$ ) be the solutions to equations (3.44), (3.45) and (3.46) on $\hat{B}_{k}(p)$ (resp. $\tilde{B}_{k}(q)$ ). Recall $u_{k}-u_{k+1}$ satisfies (3.49) and apply gradient estimates to the $g_{\boldsymbol{\beta}}$-harmonic function $u_{k}-u_{k+1}$, we get the bound of $\left\|\nabla_{g_{\beta}}\left(u_{k}-u_{k+1}\right)\right\|_{L^{\infty}\left(\frac{1}{3} \hat{B}_{k}(p)\right)}$, which in particular implies that for $i=1$ or 2
$$\left\|\left|z_{i}\right|^{1-\beta_{i}}\left(\frac{\partial u_{k}}{\partial z_{i}}-\frac{\partial u_{k+1}}{\partial z_{i}}\right)\right\|_{L^{\infty}\left(\frac{1}{3} \hat{B}_{k}(p)\right)} \leq C \tau^{k} \omega\left(\tau^{k}\right) .$$
Similarly $D^{\prime} u_{k}-D^{\prime} u_{k+1}$ is also $g_{\beta}$-harmonic on $\frac{1}{2} \hat{B}_{k}(p)$ and apply gradient estimates to this function we get for $i=1,2$
$$\left\|\left|z_{i}\right|^{1-\beta_{i}}\left(\frac{\partial D^{\prime} u_{k}}{\partial z_{i}}-\frac{\partial D^{\prime} u_{k+1}}{\partial z_{i}}\right)\right\|_{\left.L^{\infty}\left(\frac{1}{3} \hat{B}_{k}(p)\right)\right)} \leq C \omega\left(\tau^{k}\right) .$$
The following lemma can be proved by the same way as in Lemma 2.10 of [20] since $p \notin \mathcal{S}$, so we omit the proof.

Lemma 3.8. The following limits hold: for $i=1$ or 2
$$\lim _{k \rightarrow \infty} \frac{\partial u_{k}}{\partial r_{i}}(p)=\frac{\partial u}{\partial r_{i}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial u_{k}}{r_{i} \partial \theta_{i}}(p)=\frac{\partial u}{r_{i} \partial \theta_{i}}(p)$$
and
$$\lim _{k \rightarrow \infty} \frac{\partial D^{\prime} u_{k}}{\partial r_{i}}(p)=\frac{\partial D^{\prime} u}{\partial r_{i}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial D^{\prime} u_{k}}{r_{i} \partial \theta_{i}}(p)=\frac{\partial D^{\prime} u}{r_{i} \partial \theta_{i}}(p) .$$
Similar formulas also hold for $v_{k}$ at the point $q$.

We are going to estimate the quantities
$$J:=\left|\frac{\partial D^{\prime} u}{\partial r_{i}}(p)-\frac{\partial D^{\prime} u}{\partial r_{i}}(q)\right|, \text { and } K:=\left|\frac{\partial D^{\prime} u}{r_{i} \partial \theta_{i}}(p)-\frac{\partial D^{\prime} u}{r_{i} \partial \theta_{i}}(q)\right|, \quad i=1,2 .$$
Note that $J, K$ correspond to $\left|N_{j} D^{\prime} u(p)-N_{j} D^{\prime} u(q)\right|$ in Theorem 1.1. We will estimate the case for $i=1$ and $J$, since the other cases are completely the same. By triangle inequality we have
$$\begin{aligned}
J \leq & \left|\frac{\partial D^{\prime} u}{\partial r_{i}}(p)-\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(p)\right|+\left|\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(p)-\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(q)\right| \\
& +\left|\frac{\partial D^{\prime} u_{\ell}}{\partial r_{i}}(q)-\frac{\partial D^{\prime} v_{\ell}}{\partial r_{i}}(q)\right|+\left|\frac{\partial D^{\prime} v_{\ell}}{\partial r_{i}}(q)-\frac{\partial D^{\prime} u}{\partial r_{i}}(q)\right| \\
=: & J_{1}+J_{2}+J_{3}+J_{4} .
\end{aligned}$$

Lemma 3.9. There exists a constant $C(n)>0$ such that $J_{1}, J_{3}$ and $J_{4}$ satisfy
$$J_{1}+J_{4} \leq C \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right), \quad J_{3} \leq C \omega\left(\tau^{\ell}\right) .$$
Proof. The estimates for $J_{1}$ and $J_{4}$ can be proved similarly as in proving those of $I_{1}$ and $I_{4}$ as in Section 3.2, using (3.60) and (3.61). $J_{3}$ can be estimated similar to that of $I_{3}$ as in Section 3.2, using (3.60). So we omit the details. \(\square\)

To estimate $J_{2}$, as in Section 3.2 we denote $h_{k}:=u_{k-1}-u_{k}$ for $2 \leq k \leq \ell$ which is $g_{\boldsymbol{\beta}}$-harmonic on $\hat{B}_{k}(p)$ and satisfies the $L^{\infty}$-estimate $\left\|h_{k}\right\|_{L^{\infty}\left(\hat{B}_{k}(p)\right)} \leq C \tau^{2 k} \omega\left(\tau^{k}\right)$ by (3.60). We rewrite (3.56) as
$$\left\|\left(D^{\prime}\right)^{3} h_{k}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}\right)}+\sum_{i=1}^{2}\left\|\left|z_{i}\right|^{1-\beta_{i}} \frac{\partial}{\partial z_{i}}\left(D^{\prime}\right)^{2} h_{k}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Lemma 3.10. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that for any $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}$, the following pointwise estimate holds for all $k \leq \min \left(\ell, k_{p}\right)$
$$\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(z)\right|+\left|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}(z)\right| \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .$$
Proof. We define a function $F$ as
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2} D^{\prime} h_{k}}{\partial z_{1} \partial \bar{z}_{1}}=-\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2} D^{\prime} h_{k}}{\partial z_{2} \partial \bar{z}_{2}}-\sum_{j=5}^{2 n} \frac{\partial^{2} D^{\prime} h_{k}}{\partial s_{j}^{2}}=: F .$$
The Laplacian estimates (3.9) and derivative estimates applied to the $g_{\boldsymbol{\beta}}$-harmonic function $D^{\prime} h_{k}$ implies that $F$ satisfies
$$\|F\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)} \leq C(n) \tau^{-k} \omega\left(\tau^{k}\right) .$$
For any $k \leq \min \left(\ell, k_{p}\right)$ and $x \in \mathcal{S}_{1} \cap \frac{1}{4} \hat{B}_{k}(p), B_{\boldsymbol{\beta}}\left(x, \tau^{k}\right) \subset \frac{1}{3} \hat{B}_{k}(p)$. The intersection of $B_{\boldsymbol{\beta}}\left(x, \tau^{k}\right)$ with complex plane $\mathbb{C}$ passing through $x$ and orthogonal to the hyperplane $\mathcal{S}_{1}$ lies in a metric ball of radius $\tau^{k}$ under the standard cone metric $\hat{g}_{\beta_{1}}$ on $\mathbb{C}$. We view the equation (3.63) as defined on the ball $\hat{B}:=B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}}\right) \subset \mathbb{C}$. The estimate (2.2) applied to the function $D^{\prime} h_{k}$ gives rise to
$$\sup _{B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}}\left|\frac{\partial D^{\prime} h_{k}}{\partial z_{1}}\right| \leq C \frac{\left\|D^{\prime} h_{k}\right\|_{L^{\infty}(\hat{B})}}{\left(\tau^{k}\right)^{1 / \beta_{1}}}+C\|F\|_{L^{\infty}(\hat{B})}\left(\tau^{k}\right)^{2-\frac{1}{\beta}} .$$

Therefore on $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$ the following holds
$$\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right|+\left|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}\right| \leq r_{1}^{\frac{1}{\beta_{1}}-1}\left|\frac{\partial D^{\prime} h_{k}}{\partial z_{1}}\right| \leq C r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{k\left(1-\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right)$$
On other hand, since $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right)=B_{\hat{g}_{\beta_{1}}}\left(x, 2^{-\beta_{1}} \tau^{k}\right)$
$$\frac{1}{4} \hat{B}_{k}(p) \subset \cup_{x \in \mathcal{S}_{1} \cap \frac{1}{4} \hat{B}_{k}} B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) .$$
equation (3.65) implies the desired estimate on the balls $\frac{1}{4} \hat{B}_{k}(p)$. \(\square\)

Remark 3.3. By similar arguments we can get the following estimates as well for any $k \leq \min \left(\ell, k_{p}\right)$ and $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}_{1}$
$$\left|\frac{\partial\left(D^{\prime}\right)^{2} h_{k}}{\partial r_{1}}(z)\right|+\left|\frac{\partial\left(D^{\prime}\right)^{2} h_{k}}{r_{1} \partial \theta_{1}}(z)\right| \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-\frac{k}{\beta_{1}}} \omega\left(\tau^{k}\right) .$$

Lemma 3.11. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that for all $k \leq \min \left(k_{p}, \ell\right)$ and $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}$ the following pointwise estimates hold
$$\begin{gathered}
\left|\frac{\partial^{2} D^{\prime} h_{k}}{r_{1}^{2} \partial \theta_{1}^{2}}(z)\right|+\left|\frac{\partial^{2} D^{\prime} h_{k}}{r_{1} \partial r_{1} \partial \theta_{1}}(z)\right| \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right), \\
\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1}^{2}}(z)\right| \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .
\end{gathered}$$
Proof. Applying the gradient estimate to the $g_{\boldsymbol{\beta}}$-harmonic function $D^{\prime} h_{k}$, we get
$$\left\|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)} \leq\left\|\nabla_{g_{\beta}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)} \leq C \omega\left(\tau^{k}\right) .$$
The function $\partial_{\theta_{1}} D^{\prime} h_{k}$ is also a continuous $g_{\beta}$-harmonic function so the derivatives estimates implies on $\frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|F_{1}\right| \leq\left|\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{2} \partial \bar{z}_{2}}\right|+\left|\frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial s_{j}^{2}}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right),$$
where $F_{1}$ is defined below
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{1} \partial \bar{z}_{1}}=-\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{2} \partial \bar{z}_{2}}-\sum_{j=5}^{2 n} \frac{\partial^{2}\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial s_{j}^{2}}=: F_{1} .$$
We apply similar arguments as in the proof of Lemma 3.10. For any $x \in \mathcal{S}_{1} \cap \frac{1}{4} \hat{B}_{k}(p)$, we view the equation (3.70) as defined on the $\mathbb{C}$-ball $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}}\right)$, and by the estimate (2.2) we have on $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$
$$\left|\frac{\partial\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{1}}\right| \leq C \frac{\left\|\partial_{\theta_{1}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\hat{B}_{\mathbb{C}}\right)}}{\left(\tau^{k}\right)^{1 / \beta_{1}}}+C\left\|F_{1}\right\|_{L^{\infty}\left(\hat{B}_{\mathbb{C}}\right)}\left(\tau^{k}\right)^{2-\frac{1}{\beta_{1}}} .$$
Equivalently, this means that on $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$
$$\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1} \partial \theta_{1}}\right|+\left|\frac{\partial^{2} D^{\prime} h_{k}}{r_{1} \partial \theta_{1}^{2}}\right| \leq r_{1}^{\frac{1}{\beta_{1}}-1}\left|\frac{\partial\left(\partial_{\theta_{1}} D^{\prime} h_{k}\right)}{\partial z_{1}}\right| \leq C r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{k\left(1-\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right) .$$

Again by the inclusion (3.66), we get (3.68). The estimate (3.69) follows from Lemma 3.10, (3.68), (3.64) and the equation (from (3.63)) below
$$\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1}^{2}}=\frac{1}{r_{1}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}-\frac{1}{\beta_{1}^{2} r_{1}^{2}} \frac{\partial^{2} D^{\prime} h_{k}}{\partial \theta_{1}^{2}}+F .$$ \(\square\)

Lemma 3.12. There exists a constant $C(n, \boldsymbol{\beta})>0$ for $k \leq \min \left(k_{2, p}, \ell\right)$, the following pointwise estimates hold for any $z \in \frac{1}{4} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right| \leq C(n, \boldsymbol{\beta}) r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right) .$$
Proof. By the Laplacian estimate in (3.9) for the harmonic function $D^{\prime} h_{k}$ on $\frac{1}{2} \hat{B}_{k}(p)$, we have
$$\sup _{\frac{1}{2.2} \hat{B}_{k}(p)}\left(\left|\Delta_{1} D^{\prime} h_{k}\right|+\left|\Delta_{2} D^{\prime} h_{k}\right|\right) \leq C(n) \tau^{-2 k} \operatorname{osc}_{\frac{1}{2} \hat{B}_{k}(p)}\left(D^{\prime} h_{k}\right) \leq C(n) \tau^{-k} \omega\left(\tau^{k}\right) .$$
Since $\Delta_{1}\left(D^{\prime} h_{k}\right)$ is also $g_{\boldsymbol{\beta}}$-harmonic, the Laplacian estimates (3.9) imply that
$$\sup _{\frac{1}{2.4} \hat{B}_{k}(p)}\left(\left|\Delta_{1} \Delta_{1} D^{\prime} h_{k}\right|+\left|\Delta_{2} \Delta_{1} D^{\prime} h_{k}\right|\right) \leq C(n, \boldsymbol{\beta}) \tau^{-2 k} \operatorname{osc}_{\frac{1}{2.2} \hat{B}_{k}(p)} \Delta_{1} D^{\prime} h_{k} \leq C \tau^{-3 k} \omega\left(\tau^{k}\right) .$$
Now from the equation $\Delta_{\boldsymbol{\beta}}\left(\Delta_{1} D^{\prime} h_{k}\right)=0$
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}} \Delta_{1} D^{\prime} h_{k}=-\Delta_{2} \Delta_{1} D^{\prime} h_{k}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}} \Delta_{1} D^{\prime} h_{k}=: F_{2} .$$
From (3.73) and the Laplacian estimates (3.9), we see that $\sup _{\frac{1}{2.4} \hat{B}_{k}(p)}\left|F_{2}\right| \leq C \tau^{-3 k} \omega\left(\tau^{k}\right)$. By similar argument by considering $x \in \frac{1}{3} \hat{B}_{k}(p) \cap \mathcal{S}_{1}$, we obtain from (3.74) that on $\hat{B}:=B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$
$$\left|\frac{\partial}{\partial z_{1}} \Delta_{1} D^{\prime} h_{k}\right| \leq C \frac{\left\|\Delta_{1} D^{\prime} h_{k}\right\|_{L^{\infty}(\hat{B})}}{\left(\tau^{k}\right)^{1 / \beta_{1}}}+C\left\|F_{2}\right\|_{L^{\infty}(\hat{B})}\left(\tau^{k}\right)^{2-\frac{1}{\beta_{1}}} \leq C \tau^{-k\left(1+\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right) .$$
This implies that for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial r_{1}} \Delta_{1} D^{\prime} h_{k}(z)\right|+\left|\frac{\partial}{r_{1} \partial \theta_{1}} \Delta_{1} D^{\prime} h_{k}(z)\right| \leq C r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(1+\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right) .$$
Now taking $\frac{\partial}{\partial r_{1}}$ on both sides of $\Delta_{\boldsymbol{\beta}} D^{\prime} h_{k}=0$, we get
$$\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)=-\frac{\partial}{\partial r_{1}}\left(\Delta_{1} D^{\prime} h_{k}\right)-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)=: F_{3} .$$
From (3.75), for any $z \in \frac{1}{3} \hat{B}_{k} \backslash \mathcal{S},\left|F_{3}\right|(z) \leq C r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(1+\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right)$. By similar argument for any $y \in \frac{1}{3.2} \hat{B}_{k}(p) \cap \mathcal{S}_{2}$, we apply the estimate (2.2) to $\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}$, we get on $A_{1}:=B_{\mathbb{C}}\left(y,\left(\tau^{k}\right)^{1 / \beta_{2}} / 2\right) \backslash\{y\}$, the punctured ball in the complex plane $\mathbb{C}$ of (Euclidean) radius $\left(\tau^{k}\right)^{1 / \beta_{2}} / 2$ and orthogonal to $\mathcal{S}_{2}$ passing through $y$,
$$\left|\frac{\partial}{\partial z_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right| \leq C \frac{\left\|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right\|_{L^{\infty}\left(A_{1}\right)}}{\left(\tau^{k}\right)^{1 / \beta_{2}}}+C\left\|F_{3}\right\|_{L^{\infty}\left(A_{1}\right)}\left(\tau^{k}\right)^{2-\frac{1}{\beta_{2}}} \leq C r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}-1\right)} \omega\left(\tau^{k}\right) .$$

Varying $y \in \frac{1}{3.2} \hat{B}_{k}(p) \cap \mathcal{S}_{2}$ we get for any $z \in \frac{1}{4} \hat{B}_{k} \backslash \mathcal{S}$, that the following pointwise estimate holds
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)(z)\right| \leq C r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}-1\right)} \omega\left(\tau^{k}\right) .$$ \(\square\)

Lemma 3.13. Let $d=d_{\boldsymbol{\beta}}(p, q)$. There exists a constant $C(n, \boldsymbol{\beta})$ such that for all $k \leq \ell$
$$\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right),$$
and
$$\left|\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{r_{1} \partial \theta_{1}}(q)\right| \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .$$
Proof. We will consider the different cases $r_{p}=\min \left(r_{p}, r_{q}\right) \leq 2 d$ and $r_{p}=\min \left(r_{p}, r_{q}\right)>2 d$.
- $r_{p} \leq 2 d$. In this case, it is clear by the choice of $\ell$ that $r_{p} \approx \tau^{k_{p}} \leq 2 d \leq \tau^{\ell+2}$, so $k_{p} \geq \ell+2$.

From our assumption when solving (3.45), $r_{p}=d_{\boldsymbol{\beta}}\left(p, \mathcal{S}_{1}\right)$, i.e. $r_{1}(p)=r_{p} \leq 2 d$. By triangle inequality we have $r_{1}(q) \leq 3 d$. We also remark that for $k \leq \ell, \tau^{k} \geq \tau^{\ell}>8 d$, in particular, the geodesics considered below all lie inside the balls $\frac{1}{4} \hat{B}_{k}(p)$, and the estimates in Lemma 3.10 - Lemma 3.12 holds for points on these geodesics.

Let $p=\left(r_{1}(p), \theta_{1}(p) ; r_{2}(p), \theta_{2}(p) ; s(p)\right)$ and $q=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(q), \theta_{2}(q) ; s(q)\right)$ be the coordinates of the points $p, q$. Let $\gamma:[0, d] \rightarrow B_{\boldsymbol{\beta}}(0, q) \backslash \mathcal{S}$ be the unique $g_{\boldsymbol{\beta}}$-geodesic connecting $p$ and $q$. We know the curve $\gamma$ is disjoint with $\mathcal{S}$, and we denote $\gamma(t)=\left(r_{1}(t), \theta_{1}(t) ; r_{2}(t), \theta_{2}(t) ; s(t)\right)$ be the coordinates of $\gamma(t)$ for $t \in[0, d]$. By definition we have for $\forall t \in[0, d]$
$$\left|\gamma^{\prime}(t)\right|_{g_{\beta}}^{2}=\left(r_{1}^{\prime}(t)\right)^{2}+\beta_{1}^{2} r_{1}(t)^{2}\left(\theta_{1}^{\prime}(t)\right)^{2}+\left(r_{2}^{\prime}(t)\right)^{2}+\beta_{2}^{2} r_{2}(t)^{2}\left(\theta_{2}^{\prime}(t)\right)^{2}+\left|s^{\prime}(t)\right|^{2}=1 .$$
So $|s(p)-s(q)| \leq d$ and $\left|r_{i}(p)-r_{i}(q)\right| \leq d$ for $i=1,2$. We denote
$$q^{\prime}:=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(p), \theta_{2}(p) ; s(p)\right), \quad p^{\prime}:=\left(r_{1}(p), \theta_{1}(q) ; r_{2}(p), \theta_{2}(p) ; s(p)\right)$$
the points with coordinates related to $p$ and $q$. Let $\gamma_{1}$ be the $g_{\boldsymbol{\beta}}$-geodesic connecting $q$ and $q^{\prime} ; \gamma_{2}$ the $g_{\boldsymbol{\beta}}$-geodesic joining $q^{\prime}$ to $p^{\prime} ; \gamma_{3}$ the $g_{\boldsymbol{\beta}}$-geodesic joining $p^{\prime}$ to $p$.

By triangle inequality, we have
$$\begin{gathered}
\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| \\
\leq\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(p^{\prime}\right)\right|+\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(p^{\prime}\right)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(q^{\prime}\right)\right| \\
+\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(q^{\prime}\right)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right|=: J_{1}^{\prime}+J_{2}^{\prime}+J_{3}^{\prime} .
\end{gathered}$$
Integrating along $\gamma_{3}$ on which the points have fixed $r_{1}$-coordinate $r_{1}(p)$, we get by (3.68)
$$J_{1}^{\prime}=\left|\int_{\gamma_{3}} \frac{\partial}{\partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d \theta_{1}\right| \leq C(n, \boldsymbol{\beta}) r_{1}(p)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .$$

Integrating along $\gamma_{2}$ and by (3.69) we get
$$\begin{aligned}
J_{2}^{\prime} & =\left|\int_{\gamma_{2}} \frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d r_{1}\right| \\
& \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right)\left|\int_{r_{1}(p)}^{r_{1}(q)} t^{\frac{1}{\beta_{1}}-2} d t\right| \\
& =C(n, \boldsymbol{\beta}) \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right)\left|r_{1}(p)^{\frac{1}{\beta_{1}}-1}-r_{1}(q)^{\frac{1}{\beta_{1}}-1}\right| \\
& \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right)\left|r_{1}(p)-r_{1}(q)\right|^{\frac{1}{\beta_{1}}-1} \\
& \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1} .
\end{aligned}$$
To deal with $J_{3}^{\prime}$, we need to consider different choices of $k \leq \ell$.
- If $k_{2, p}+1 \leq k \leq \ell$, the balls $\hat{B}_{k}(p)$ are centered at $p_{1} \in \mathcal{S}_{1}$ (recall $p_{1}$ is the projection of $p$ to $\mathcal{S}_{1}$, hence $p$ and $p_{1}$ have the same ( $r_{2}, \theta_{2} ; s$ )-coordinates). $\tau^{-k} \leq 8^{-1} d^{-1}$ by the choice of $\ell$. The balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}_{2}$, so we can introduce the smooth coordinates $w_{2}=z_{2}^{\beta_{2}}$, and under the coordinates $\left(r_{1}, \theta_{1} ; w_{2}, z_{3}, \ldots, z_{n}\right)$, the metric $g_{\boldsymbol{\beta}}$ become the smooth cone metric with conical singularity only along $\mathcal{S}_{1}$ with angle $2 \pi \beta_{1}$. Therefore we can derive the following estimate as in (3.62) that
$$\sup _{\frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}_{1}}\left|\frac{\partial\left(D^{\prime}\right)^{2} h_{k}}{\partial r_{1}}\right|+\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial w_{2}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Since $q$ and $q^{\prime}$ have the same $\left(r_{1}, \theta_{1}\right)$-coordinates and $g_{\boldsymbol{\beta}}$ is a product metric, $\gamma_{1}$ is in fact a straight line segment (under the coordinates $\left(w_{2}, z_{3}, \ldots, z_{n}\right)$ ) in the hyperplane with fixed $\left(r_{1}, \theta_{1}\right)$ -coordinates. Integrating over $\gamma_{1}$, we get
$$\begin{aligned}
J_{3}^{\prime} & \leq \int_{\gamma_{1}}\left|\frac{\partial}{\partial w_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|+\sum_{j}\left|\frac{\partial}{\partial s_{j}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right| \\
& \leq C \tau^{-k} \omega\left(\tau^{k}\right) d_{\boldsymbol{\beta}}\left(q, q^{\prime}\right) \leq C \tau^{-k} \omega\left(\tau^{k}\right) d \\
& \leq C(n, \boldsymbol{\beta}) \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1} .
\end{aligned}$$
- If $k \leq k_{2, p}$, the balls $\hat{B}_{k}(p)$ are centered at the $p_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ and $\tau^{k} \geq r_{2}(p)$. By triangle inequality $r_{2}(q) \leq d+r_{2}(p) \leq \frac{9}{8} \tau^{k}$. We choose points as follows
$$\tilde{q}=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(p), \theta_{2}(p) ; s(q)\right), \quad \hat{q}=\left(r_{1}(q), \theta_{1}(q) ; r_{2}(q), \theta_{2}(p) ; s(q)\right) .$$
Let $\tilde{\gamma}_{1}$ be the $g_{\beta}$-geodesic joining $q^{\prime}$ to $\tilde{q}$; $\tilde{\gamma}$ the $g_{\beta}$-geodesic joining $\tilde{q}$ to $\hat{q}$; and $\hat{\gamma}$ the $g_{\beta}$-geodesic joining $\hat{q}$ to $q$. The curves $\tilde{\gamma}_{1}, \tilde{\gamma}$ and $\hat{\gamma}$ all lie in the hyperplane with constant $\left(r_{1}, \theta_{1}\right)$-coordinates $\left(r_{1}(q), \theta_{1}(q)\right)$. Then by triangle inequality we have
$$\begin{aligned}
J_{3}^{\prime} \leq & \left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\left(q^{\prime}\right)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\tilde{q})\right|+\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\tilde{q})-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\hat{q})\right| \\
& +\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(\hat{q})-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right|=: J_{1}^{\prime \prime}+J_{2}^{\prime \prime}+J_{3}^{\prime \prime} .
\end{aligned}$$

We will use frequently the inequalities that $r_{1}(q) \leq 3 d$ and $\max \left(r_{2}(q), r_{2}(p)\right) \leq 2 \tau^{k}$ in the estimates below. Integrating along $\hat{\gamma}$ we get by (3.71)
$$J_{3}^{\prime \prime} \leq\left|\int_{\hat{\gamma}} \frac{\partial}{\partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d \theta_{2}\right| \leq C r_{1}(q)^{\frac{1}{\beta_{1}}-1} r_{2}(q)^{\frac{1}{\beta_{2}}} \tau^{-k\left(-1+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right) \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right)$$
Integrating along $\tilde{\gamma}$ we get again by (3.71)
$$\begin{aligned}
J_{2}^{\prime \prime} & \leq\left|\int_{\tilde{\gamma}} \frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d r_{2}\right| \\
& \leq C r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right)\left|\int_{r_{2}(q)}^{r_{2}(p)} t^{\frac{1}{\beta_{2}}-1} d t\right| \\
& \leq C r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right) \max \left(r_{2}(q), r_{2}(p)\right)^{\frac{1}{\beta_{2}}-1} d \\
& \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right)
\end{aligned}$$
Integrating along $\tilde{\gamma}_{1}$ we get by (3.67)
$$J_{1}^{\prime \prime} \leq\left|\int_{\tilde{\gamma}_{1}} \frac{\partial}{\partial s_{j}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right) d t\right| \leq C r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-\frac{k}{\beta_{1}}} \omega\left(\tau^{k}\right) d \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .$$
Combining the above three inequalities, we get in the case $k \leq k_{2, p}$ that
$$J_{3}^{\prime} \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .$$
Combining the estimates on $J_{1}^{\prime}, J_{2}^{\prime}, J_{3}^{\prime}$, we finish the proof of (3.78) in the case $r_{p} \leq 2 d$.
- $r_{p}>2 d$ and $\ell \leq k_{p}$. In this case $\tau^{k_{p}} \approx r_{p}>2 d \geq \tau^{\ell+3}$. From triangle inequality we get $d_{\boldsymbol{\beta}}(\gamma(t), \mathcal{S}) \geq d$, in particular, the $r_{1}$ and $r_{2}$ coordinates of $\gamma(t)$ are both bigger than $d$. In this case $k \leq \ell \leq k_{p}$, Lemma 3.10 - Lemma 3.12 hold for the points in $\gamma . r_{1}(\gamma(t)) \leq r_{1}(p)+d \leq 2 \tau^{k}$. We calculate the gradient of $\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}$ along $\gamma$
$$\begin{gathered}
\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right|^{2}=\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2}+\left|\frac{\partial}{\beta_{1} r_{1} \partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2}+\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2} \\
+\left|\frac{\partial}{\beta_{2} r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2}+\sum_{j}\left|\frac{\partial}{\partial s_{j}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|^{2} .
\end{gathered}$$
(1). When $k_{2, p}+1 \leq k \leq \ell$ we have by (3.83) that
$$\sup _{\frac{1}{2} \hat{B}_{k} \backslash \mathcal{S}_{1}}\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
Thus by Lemma 3.11, (3.67) and (3.85) along $\gamma$ we have
$$\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right| \leq C \omega\left(\tau^{k}\right)\left(d^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}+\tau^{-k}\right)$$
Integrating along $\gamma$ we get
$$\begin{aligned}
\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| & \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right| \leq C \omega\left(\tau^{k}\right)\left(d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}+d \tau^{-k}\right) \\
& \leq C \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} .
\end{aligned}$$
(2). When $k \leq k_{2, p}$, we have $r_{2}(\gamma(t)) \leq r_{2}(p)+d \leq \tau^{k}+d \leq \frac{9}{8} \tau^{k}$ and similar estimates hold for $r_{1}(\gamma(t))$ too. Then by Lemma 3.11, Lemma 3.12 and (3.67) along $\gamma$ the following estimate holds
$$\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right|(\gamma(t)) \leq C \omega\left(\tau^{k}\right)\left(d^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}+\tau^{-k}\right)$$
Integrating along $\gamma$ we get
$$\begin{aligned}
\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{1}}(q)\right| & \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{1}}\right| \leq C \omega\left(\tau^{k}\right)\left(d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}+d \tau^{-k}\right) \\
& \leq C \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} .
\end{aligned}$$
This finishes the proof of the lemma in this case.
- $r_{p}>2 d$ but $\ell \geq k_{p}+1$. When $k \leq k_{p}$, the estimate (3.78) follows in the same way as the case above. So it suffices to consider the case when $k_{p}+1 \leq k \leq \ell$. In this case the balls $\hat{B}_{k}(p)=B_{\boldsymbol{\beta}}\left(p, \tau^{k}\right)$ and it can be seen by triangle inequality that the geodesic $\gamma \subset \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$. Since the metric balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}$ we can use the smooth coordinates $w_{1}=z_{1}^{\beta_{1}}$ and $w_{2}=z_{2}^{\beta_{2}}$ as before, and everything becomes smooth under these coordinates in $\hat{B}_{k}(p)$.

The estimate (3.79) can be shown by the same argument, so we skip the details. \(\square\)

Iteratively applying (3.78) for $k \leq \ell$, we get
$$\begin{aligned}
J_{2} & =\left|\frac{\partial D^{\prime} u_{\ell}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} u_{\ell}}{\partial r_{1}}(q)\right| \leq\left|\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(q)\right|+C d^{\frac{1}{\beta_{1}}-1} \sum_{k=3}^{\ell} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) \\
& \leq C d^{\frac{1}{\beta_{1}}-1}\left(\|u\|_{C^{0}}+\sum_{k=2}^{\ell} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right)\right),
\end{aligned}$$
where the inequality
$$\left|\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(p)-\frac{\partial D^{\prime} u_{2}}{\partial r_{1}}(q)\right| \leq C d^{\frac{1}{\beta_{1}}-1}\|u\|_{C^{0}}$$
can be proved by the same argument as in proving (3.78).
Combining the estimates for $J_{1}, J_{2}, J_{3}, J_{4}$ we finish the proof of (1.4).
We remark that in solving (3.45), we assume $r_{1}(p) \leq r_{2}(p)$, we need also to deal with the following case, whose proof is more or less parallel to that of Lemma 3.13, so we just point out the differences and sketch the proof.

Lemma 3.14. Let $d=d_{\boldsymbol{\beta}}(p, q)>0$. There exists a constant $C(n, \boldsymbol{\beta})>0$ such that for all $k \leq \ell$,
$$\begin{aligned}
& \left|\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(q)\right| \leq C d^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(\frac{1}{\beta_{2}}-1\right)} \omega\left(\tau^{k}\right), \\
& \left|\frac{\partial D^{\prime} h_{k}}{r_{2} \partial \theta_{2}}(p)-\frac{\partial D^{\prime} h_{k}}{r_{2} \partial \theta_{2}}(q)\right| \leq C d^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(\frac{1}{\beta_{2}}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Proof. We consider two different cases on whether $k \leq k_{1, p}$ or $k_{1, p}+1 \leq k \leq \ell$.
- $k_{2, p}+1 \leq k \leq \ell$. The balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}_{2}$, so we can introduce the complex coordinate $w_{2}=z_{2}^{\beta_{2}}$ on these balls as before. Let $t_{1}, t_{2}$ be the real and imaginary parts of $w_{2}$, respectively. The derivatives estimates imply that
$$\left\|\partial_{w_{2}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)} \leq C \omega\left(\tau^{k}\right), \quad\left\|\partial_{w_{2}}^{2} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right),$$
where $\partial_{w_{2}}^{2}$ denotes the full second order derivatives in the $\left\{t_{1}, t_{2}\right\}$-directions. And
$$\left\|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial w_{2}}\right)\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)}+\left\|\frac{\partial}{r_{1} \partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial w_{2}}\right)\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Since
$$\frac{\partial}{\partial r_{2}}=\frac{w_{2}}{r_{2}} \frac{\partial}{\partial w_{2}}+\frac{\bar{w}_{2}}{r_{2}} \frac{\partial}{\partial \bar{w}_{2}},$$
it holds that
$$\frac{\partial}{\partial w_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)=\frac{1}{r_{2}} \frac{\partial D^{\prime} h_{k}}{\partial w_{2}}-\frac{\left|w_{2}\right|^{2}}{2 r_{2}^{3}} \frac{\partial D^{\prime} h_{k}}{\partial w_{2}}-\frac{\bar{w}_{2} \cdot \bar{w}_{2}}{2 r_{2}^{3}} \frac{\partial D^{\prime} h_{k}}{\partial \bar{w}_{2}}+\frac{w_{2}}{r_{2}} \partial_{w_{2}}^{2} D^{\prime} h_{k},$$
we have on $\frac{1}{2} \hat{B}_{k}(p)$
$$\left|\frac{\partial}{\partial w_{2}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)\right| \leq \frac{C}{r_{2}} \omega\left(\tau^{k}\right)+C \tau^{-k} \omega\left(\tau^{k}\right) .$$
And
$$\left\|\frac{\partial}{\partial r_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)}+\left\|\frac{\partial}{r_{1} \partial \theta_{1}}\left(\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right)\right\|_{L^{\infty}\left(\frac{1}{2} \hat{B}_{k}(p)\right)} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Therefore
$$\begin{aligned}
\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right|^{2} & =\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1} \partial r_{2}}\right|^{2}+\left|\frac{\partial^{2}}{r_{1} \partial \theta_{1} \partial r_{2}}\right|^{2}+\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial w_{2} \partial r_{2}}\right|^{2}+\sum_{j}\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial s_{j} \partial r_{2}}\right|^{2} \\
& \leq C\left(\tau^{-k} \omega\left(\tau^{k}\right)\right)^{2}+C \frac{1}{r_{2}^{2}} \omega\left(\tau^{k}\right)^{2} .
\end{aligned}$$
In this case we know that $r_{1}(p) \approx \tau^{k_{p}} \geq 2 \tau^{k} \geq \tau^{\ell}>8 d$, so along $\gamma$
$$r_{2}(\gamma(t)) \geq r_{2}(p)-d \geq r_{1}(p)-d \geq \frac{7}{4} \tau^{k} .$$
Integrating along $\gamma$ we get
$$\left|\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(p)-\frac{\partial D^{\prime} h_{k}}{\partial r_{2}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial D^{\prime} h_{k}}{\partial r_{2}}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) d \leq C \tau^{-k\left(\frac{1}{\beta_{2}}-1\right)} \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{2}}-1} .$$
\begin{itemize}
\item[-] $k \leq k_{2, p}$. This case is completely the same as in the proof of (3.78), by replacing $r_{1}$ by $r_{2}, \beta_{1}$ by $\beta_{2}$. So we omit the details.
\end{itemize}
(3.87) can be proved similarly. \(\square\)

\subsection*{3.4. Mixed normal directions}

In this section, we will deal with the Hölder continuity of the following four mixed derivatives:
$$\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}, \frac{\partial^{2} u}{r_{1} \partial \theta_{1} \partial r_{2}}, \frac{\partial^{2} u}{r_{2} \partial r_{1} \partial \theta_{2}}, \frac{\partial^{2} u}{r_{1} r_{2} \partial \theta_{1} \partial \theta_{2}},$$
which by our previous notation correspond to $N_{1} N_{2} u$. Since the proof for each of them is more or less the same, we will only prove the Hölder continuity for $\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}$. The following holds at $p$ and $q$ by the same reasoning of Lemma 3.7
$$\lim _{k \rightarrow \infty} \frac{\partial^{2} u_{k}}{\partial r_{1} \partial r_{2}}(p)=\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p), \quad \lim _{k \rightarrow \infty} \frac{\partial^{2} v_{k}}{\partial r_{1} \partial r_{2}}(q)=\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q) .$$
By triangle inequality
$$\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| \leq\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(p)\right|+\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right|$$
$$\begin{aligned}
& +\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right|+\left|\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| \\
=: & L_{1}+L_{2}+L_{3}+L_{4} .
\end{aligned}$$

Lemma 3.15. We have the following estimate
$$L_{1}+L_{4} \leq \sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right)$$

Proof. We consider the different cases that $k \geq k_{p}+1$ and $\ell \leq k \leq k_{p}$.
- $k \geq k_{p}+1$. In this case the balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}$ and we can introduce the smooth coordinates $w_{1}=z_{1}^{\beta_{1}}$ and $w_{2}=z_{2}^{\beta_{2}}$. Under the coordinates $\left\{w_{1}, w_{2}, z_{3}, \ldots, z_{n}\right\}, g_{\boldsymbol{\beta}}$ becomes the standard Euclidean metric $g_{\mathbb{C}^{n}}$ and the metric balls $\hat{B}_{k}(p)$ become the standard Euclidean ball with the same radius and center $p$. Since the $g_{\boldsymbol{\beta}}$-harmonic functions $u_{k}-u_{k+1}$ satisfy (3.49), by standard gradient estimates for Euclidean harmonic functions we get
$$\sup _{\frac{1}{2.1} \hat{B}_{k}(p)}\left|D_{w_{1}} D_{w_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right),$$
where we use $D_{w_{i}}$ to denote either $\frac{\partial}{\partial w_{i}}$ or $\frac{\partial}{\partial \bar{w}_{i}}$ for simplicity. From (3.88) and similar formula for $\frac{\partial}{\partial r_{1}}$, we get
$$\sup _{\frac{1}{2.1} \hat{B}_{k}(p)}\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right) .$$
- If $\ell \geq k_{2, p}+1$ and $\ell \leq k_{p}=k_{1, p}$. For all $\ell \leq k$, the balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}_{2}$ and center at $p_{1}$. We can still use $w_{2}=z_{2}^{\beta_{2}}$ as the smooth coordinate. The cone metric $g_{\boldsymbol{\beta}}$ becomes smooth in $w_{2}$-variable and we can apply the standard gradient estimate to the $g_{\boldsymbol{\beta}}$-harmonic function $D_{w_{2}}\left(u_{k}-u_{k-1}\right)$ to get
$$\sup _{\frac{1}{2.2} \hat{B}_{k}(p)}\left|\frac{\partial}{\partial r_{1}} D_{w_{2}}\left(u_{k}-u_{k-1}\right)\right|+\left|\frac{\partial}{r_{1} \partial \theta_{1}} D_{w_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right) .$$
Again by (3.88), we get
$$\sup _{\frac{1}{2.2} \hat{B}_{k}(p)}\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|+\left|\frac{\partial^{2}}{r_{1} \partial \theta_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right| \leq C \omega\left(\tau^{k}\right) .$$
- If $\ell \leq k_{2, p}$, the case when $k \geq k_{2, p}+1$ can be dealt with similarly as above. In the case $\ell \leq k \leq k_{2, p}$, $r_{2}(p) \approx \tau^{k_{2, p}} \leq \tau^{k} \leq \tau^{\ell} \approx 8 d$. Now the balls $\hat{B}_{k}(p)$ are centered at $p_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$. We can proceed as in the proof of Lemma 3.12 with the harmonic functions $u_{k}-u_{k-1}$ replacing $D^{\prime} h_{k}$ as in that lemma to prove that for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\begin{aligned}
& \left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(z)+\left|\frac{\partial^{2}}{r_{2} \partial \theta_{2} \partial r_{1}}\left(u_{k}-u_{k-1}\right)\right|(z) \\
& \leq C(n, \boldsymbol{\beta}) r_{1}(z)^{\frac{1}{\beta_{1}}-1} r_{2}(z)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
In particular, the estimate in each case holds at $p$ and from $r_{1}(p) \leq r_{2}(p) \leq \tau^{k}$, we obtain
$$\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(p)+\left|\frac{\partial^{2}}{r_{2} \partial \theta_{2} \partial r_{1}}\left(u_{k}-u_{k-1}\right)\right|(p) \leq C \omega\left(\tau^{k}\right) .$$

Combining each case above, by (3.90), (3.91) and (3.92), we get for all $k \geq \ell$
$$\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(p) \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{k}\right) .$$
Therefore by triangle inequality
$$L_{1} \leq \sum_{k=\ell+1}^{\infty}\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}\left(u_{k}-u_{k-1}\right)\right|(p) \leq C(n, \boldsymbol{\beta}) \sum_{k=\ell+1}^{\infty} \omega\left(\tau^{k}\right) .$$
The estimate for $L_{4}$ can be dealt with similarly by studying the derivatives of $v_{k}$ at $q$. \(\square\)