---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Connected sum construction for $σ_k$-Yamabe metrics]

To state the result, we have to introduce the functional setting. For $m \in \mathbb{N}$ and $\delta \in \mathbb{R}$, we consider the weighted $C_{\delta}^{m}$-norm defined by
$$\|u\|_{C_{\delta}^{m}\left(\Omega_{1, \varepsilon}\right)}:=\|u\|_{C^{m}\left(M_{1} \backslash B\left(p_{1}, 1\right)\right)}+\sum_{j=0}^{m} \sup _{(t, \theta) \in N_{1, \varepsilon}}(\varepsilon \cosh t)^{\delta+j}\left|\nabla_{g_{\varepsilon}}^{j} u\right|_{g_{\varepsilon}}(t, \theta),$$
where $N_{1, \varepsilon}:=(\log \varepsilon, 0) \times \mathbb{S}^{n-1}$ and the first term is computed with respected to the metric $g_{1}$. Analogously, for $\beta \in(0,1)$, we introduce the weighted Hölder $C_{\delta}^{m, \beta}$-seminorm
$$[u]_{C_{\delta}^{m, \beta}\left(\Omega_{1, \varepsilon}\right)}:=[u]_{C^{m, \beta}\left(M_{1} \backslash B\left(p_{1}, 1\right)\right)}+\sup _{(t, \theta) \in T_{\varepsilon}}\left\{(\varepsilon \cosh t)^{\delta+m} \sup _{(t, \theta) \neq\left(t^{\prime}, \theta^{\prime}\right)} \frac{\left|\nabla_{g_{\varepsilon}}^{m} u(t, \theta)-\nabla_{g_{\varepsilon}}^{m} u\left(t^{\prime}, \theta^{\prime}\right)\right|_{g_{\varepsilon}}}{\left|\operatorname{dist}_{g_{\varepsilon}}\left((t, \theta),\left(t^{\prime}, \theta^{\prime}\right)\right)\right|^{\beta}}\right\},$$
where, with the standard convention, the difference between the covariant derivatives is justified up to taking the parallel transport of one of them. The Banach space $C_{\delta}^{m, \beta}\left(\Omega_{1, \varepsilon}\right)$ is defined by
$$C_{\delta}^{m, \beta}\left(\Omega_{1, \varepsilon}\right):=\left\{u \in C_{\text {loc }}^{m, \beta}\left(\Omega_{1, \varepsilon}\right):\|u\|_{C_{\delta}^{m, \beta}\left(\Omega_{1, \varepsilon}\right)}:=\|u\|_{C_{\delta}^{m}\left(\Omega_{1, \varepsilon}\right)}+[u]_{C_{\delta}^{m, \beta}\left(\Omega_{1, \varepsilon}\right)}<+\infty\right\} .$$
We notice that the weighted Banach spaces $C_{\delta}^{m, \beta}\left(M_{\varepsilon}\right)$, which will be used in the global analysis, can be defined in the same way, replacing $N_{1, \varepsilon}$ by $T_{\varepsilon}$ and $M_{1} \backslash B_{p_{1}, 1 / 2}$ by $\left(M_{1} \backslash B_{p_{1}, 1 / 2}\right) \cup\left(M_{2} \backslash B_{p_{2}, 1 / 2}\right)$. With these definitions at hand we are now ready to prove the uniform a priori estimate for solutions to the linear problem (4.2) on $\Omega_{1, \varepsilon}$.
Proposition 4.4. Suppose that $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$ and let $w \in C^{2, \beta}\left(\Omega_{1, \varepsilon}\right)$ and $f \in C^{0, \beta}\left(\Omega_{1, \varepsilon}\right)$ be two functions satisfying
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[w] & =f & & \Omega_{1, \varepsilon} \\
w & =0 & & \partial \Omega_{1, \varepsilon}
\end{aligned}\right.$$
Then there exist $C=C(n, k, \delta, \beta)>0$ and $\varepsilon_{0}=\varepsilon_{0}(n, k, \delta)$ such that, for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$, we have
$$\|w\|_{C_{\delta}^{2, \beta}\left(\Omega_{1, \varepsilon}\right)} \leq C\|f\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0, \beta}\left(\Omega_{1, \varepsilon}\right)} .$$

Proof. Here we just provide the uniform weighted $C^{0}$-bound
$$\|w\|_{C_{\delta}^{0}\left(\Omega_{1, \varepsilon}\right)} \leq C\|f\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0}\left(\Omega_{1, \varepsilon}\right)},$$
since the uniform weighted $C^{2, \beta}$-bound will follows easily from sandard scaling argument, see [25].
To prove (4.9) we argue by contradiction. Suppose that there exist a sequence $\left(\varepsilon_{i}, w_{i}, f_{i}\right)$ such that
\begin{itemize}
\item[-] $\varepsilon_{i} \longrightarrow 0, \quad$ as $i \rightarrow+\infty$,
\item[-] $\left\|w_{i}\right\|_{C_{\delta}^{0}\left(\Omega_{1, \varepsilon_{i}}\right)} \equiv 1, \quad i \in \mathbb{N}$,
\item[-] $\left\|f_{i}\right\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0}\left(\Omega_{1, \varepsilon_{i}}\right)} \longrightarrow 0, \quad$ as $i \rightarrow+\infty$
\end{itemize}
and
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon_{i}}\right)\left[w_{i}\right] & =f_{i} & \Omega_{1, \varepsilon_{i}} \\
w_{i} & =0 & \partial \Omega_{1, \varepsilon_{i}}
\end{aligned}\right.$$
To simplify the argument we introduce the function
$$\zeta_{\varepsilon}(q):=\left\{\begin{aligned}
\varepsilon \cosh (t(q)) & B\left(p_{1}, 1\right) \backslash B\left(p_{1}, \varepsilon\right) \\
1 & M_{1} \backslash B\left(p_{1}, 1\right)
\end{aligned}\right.$$
where, according to Section (3), $t(q):=\log \varepsilon-\log \left(\operatorname{dist}_{g_{1}}\left(q, p_{1}\right)\right)$. With this notation we oberve that the weighted norms are equivalent to
$$\|u\|_{C_{\delta}^{m, \beta}\left(\Omega_{1, \varepsilon}\right)}:=\sum_{j=0}^{m} \sup _{\Omega_{1, \varepsilon}} \zeta_{\varepsilon}^{\delta+j}\left|\nabla_{g_{\varepsilon}}^{j} u\right|_{g_{\varepsilon}}+\sup _{p \neq q}\left|\min \left\{\zeta_{\varepsilon}(p), \zeta_{\varepsilon}(q)\right\}\right|^{\delta+m} \frac{\left|\nabla_{g_{\varepsilon}}^{m} u(p)-\nabla_{g_{\varepsilon}}^{m} u(q)\right|_{g_{\varepsilon}}}{\left.\mid \operatorname{dist}_{g_{\varepsilon}}(p, q)\right)\left.\right|^{\beta}} .$$
Now we consider a sequence of points $q_{i} \in \Omega_{1, \varepsilon_{i}}, i \in \mathbb{N}$, where the maximum of the weighted norm of the functions $w_{i}$ is achieved, i.e.,
$$\zeta_{\varepsilon_{i}}^{\delta}\left(q_{i}\right)\left|w_{i}\left(q_{i}\right)\right|=1 .$$
Depending on the behavior of the $q_{i}$ 's, we have to distinguish three possible cases.
Case 1: There exists a subsequence of $q_{i}$ 's such that
$$q_{i} \longrightarrow q_{\infty} \in M_{1} \backslash\left\{p_{1}\right\} .$$
From the conformal equivariance property we have that
$$f_{i}=\mathbb{L}_{\bar{g}}\left(u_{\varepsilon_{i}}\right)\left[w_{i}\right]=u_{\varepsilon_{i}}^{-\frac{2 k n}{n-2 k}} \mathbb{L}_{g_{\varepsilon_{i}}}(1)\left[u_{\varepsilon_{i}}^{-1} w_{i}\right] .$$
From the fact that the approximate solution metrics $g_{\varepsilon_{i}}$ converge to $g_{1}$ on the compact subsets of $M_{1} \backslash\left\{p_{1}\right\}$ with respect to the $C^{r}$-topology, $r \in \mathbb{N}$, and from the standard elliptic regularity theory, we get that the functions $w_{i}$ converge in the $C^{2}$-norm (computed with respect to the metric $g_{1}$ ) on each compact subsets of $M_{1} \backslash\left\{p_{1}\right\}$ to a function $w_{\infty}$ which satisfies
$$\mathbb{L}_{g_{1}}(1)\left[u_{1}^{-1} w_{\infty}\right]=0 \quad \text { on } M_{1} \backslash\left\{p_{1}\right\},$$
in the sense of distributions. Moreover, in the limit point, we have $\left|w_{\infty}\left(q_{\infty}\right)\right|>0$, which means that $w_{\infty}$ is nontrivial. Using that $\left\|w_{i}\right\|_{C_{\delta}^{0}\left(\Omega_{1, \varepsilon_{i}}\right)}=1$ and passing to the limit on the compact subsets we obtain the estimate
$$\left|w_{\infty}(q)\right| \leq C\left|\operatorname{dist}_{g_{1}}\left(p_{1}, q\right)\right|^{-\delta}, \quad q \in B^{*}\left(p_{1}, 1\right),$$
with $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$ and $C>0$ a positive constant. This is due to the fact that the weighting functions $\zeta_{\varepsilon_{i}}$ are uniformly comparable to the Riemannian $g_{1}$-distance to $p_{1}$. We are going to prove that, in force of this latter feature, the function $u_{1}^{-1} w_{\infty}$ can be extended to a nontrivial solution of (4.10) on the whole $M_{1}$. Using the conformal equivariance property (1.4) and the fact that, thanks to the assumption 3.1, we can always write on $B\left(p_{1}, 1\right)$
$$g_{1}=\left(1+b_{1}\right)^{\frac{4 k}{n-2 k}} g_{\mathbb{R}^{n}},$$
with $b_{1}(q)=\mathcal{O}\left(\mid\right.$ dist $\left.\left._{g_{1}}\left(q, p_{1}\right)\right|^{2}\right)$, we have that equation above implies
$$\mathbb{L}_{\mathbb{R}^{n}}\left(1+b_{1}\right)\left[\left(1+b_{1}\right) u_{1}^{-1} w_{\infty}\right]=0 \quad \text { on } \quad B^{*}\left(p_{1}, 1\right) .$$
Recalling that $g_{1}$ solves the $\sigma_{k}$-Yamabe equation, and that
$$\left|\left(1+b_{1}\right) u_{1}^{-1} w_{\infty}\right|(q) \leq C\left|\operatorname{dist}_{g_{1}}\left(q, p_{1}\right)\right|^{-\frac{n-2 k}{2 k}-\delta}$$
we can apply Corollary 4.3 to obtain that $u_{1}^{-1} w_{\infty}$ extends through $p_{1}$ to a nontrivial smooth solution of
$$\mathbb{L}_{g_{1}}(1)\left[u_{1}^{-1} w_{\infty}\right]=0 \quad \text { on } \quad M_{1} .$$
But this contradicts the non degeneracy of the metric $g_{1}$ on $M_{1}$ according to Definition 1.1.
Case 2: There exists a subsequence of $q_{i}$ 's such that
$$q_{i} \longrightarrow q_{\infty}=p_{1}, \quad \alpha_{i} / \varepsilon_{i}=\mathcal{O}(1) \quad \text { as } \quad i \rightarrow+\infty$$
where $\alpha_{i}:=\zeta_{\varepsilon_{i}}\left(q_{i}\right) \simeq \operatorname{dist}_{g_{1}}\left(q_{i}, p_{1}\right)$. Notice that $\alpha_{i} / \varepsilon_{i} \simeq \cosh \left(t_{i}\right)$, where $t_{i}:=t\left(q_{i}\right)$. Since $q_{i} \rightarrow p_{1}$, the sequence of points $q_{i}$ will stay definitely in the annulus $A\left(p_{1}, 1, \varepsilon_{i}\right)$, which is mapped to $\left(\log \varepsilon_{i}, 0\right) \times \mathbb{S}^{n-1}$ via the asymptotic cylindrical coordinates $(t, \theta)$. For this reason, with abuse of notation, we can say that $w_{i}(q)=w_{i}(t(q), \theta(q))$. Hence, we have $\left|w_{i}\left(q_{i}\right)\right|=\left|w_{i}\left(t_{i}, \theta_{i}\right)\right|=\alpha_{i}^{-\delta}$. So, if we define
$$\bar{w}_{i}:=\alpha_{i}^{\delta} w_{i},$$
we have $\left|\bar{w}_{i}\left(t_{i}, \theta_{i}\right)\right|=1,\left|\bar{w}_{i}(t, \theta)\right| \leq(\cosh t)^{-\delta}$, for all $(t, \theta) \in\left(-\log \varepsilon_{i}, 0\right] \times \mathbb{S}^{n-1}$. For all $C>0$, we observe that the sequence of points $\left(t_{i}, \theta_{i}\right)$ will stay definitely in a compact set of the type $[-C,-1] \times \mathbb{S}^{n-1}$ and, up to a subsequence, they converge to a limit point $\left(t_{\infty}, \theta_{\infty}\right)$.

In order to investigate the limit problem we introduce an auxiliary function $b$ defined on $T_{\varepsilon_{i}}=\left(\log \varepsilon_{i},-\log \varepsilon_{i}\right) \times$ $\mathbb{S}^{n-1}$ in such a way that the following identity is satisfied
$$\bar{g}=(1+b)^{\frac{4 k}{n-2 k}} g_{c y l} .$$
It is immediate to verify that $b=\mathcal{O}\left(\varepsilon_{i}^{2}\right)$ on the compact subset of $T_{\varepsilon_{i}}$. From the conformal equivariance property (1.4) applied to the problem
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon_{i}}\right)\left[w_{i}\right] & =f_{i} & & \left(\log \varepsilon_{i}, 0\right) \times \mathbb{S}^{n-1} \\
w & =0 & & \{0\} \times \mathbb{S}^{n-1}
\end{aligned}\right.$$
we get
$$\left[\mathbb{L}_{c y l}^{0}\left(v_{\Sigma}(1+b)\right)-\varepsilon_{i}^{2 k}\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} \frac{2 k n}{n-2 k}\left(v_{\Sigma}(1+b)\right)^{\frac{2 k n}{n-2 k}-1}\right]\left[(1+b) \bar{w}_{i}\right]=(1+b)^{\frac{2 k n}{n-2 k}} \varepsilon_{i}^{-\frac{n-2 k}{2 k}(2 k-1)} \alpha_{i}^{\delta} f_{i}$$
with $\bar{w}_{i}(0, \theta)=0$, for every $i \in \mathbb{N}$ and $\theta \in \mathbb{S}^{n-1}$. Since by hypothesis we have supposed that
$$\left\|f_{i}\right\|_{\mathcal{C}_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0}}\left(\Omega_{\left.1, \varepsilon_{i}\right)} \longrightarrow 0\right.$$
and $\alpha_{i} / \varepsilon_{i}=\mathcal{O}(1)$, as $i \rightarrow+\infty$, we deduce that the right hand side of the expression above tends to zero in $C_{\text {loc }}^{0}\left((-\infty, 0) \times \mathbb{S}^{n-1}\right)$. Moreover it is easy to see that the coefficients of the linear operator on the left hand side tends to the ones of
$$\mathbb{L}_{c y l}^{0}\left(v_{\Sigma}\right)=-C_{n, k} v_{\Sigma}\left[\partial_{t}^{2}+\frac{n-k}{k(n-1)} \Delta_{\theta}-\left(\frac{n-2 k}{2 k}\right)^{2}\right]$$
in $C_{\text {loc }}^{0}\left((-\infty, 0) \times \mathbb{S}^{n-1}\right)$. By elliptic regularity we obtain the convergence of $\bar{w}_{i}$ to a function $\bar{w}_{\infty}$ in $C_{\text {loc }}^{2}\left((-\infty, 0) \times \mathbb{S}^{n-1}\right)$, which satisfies in the sense of distributions
$$\left\{\begin{aligned}
{\left[\partial_{t}^{2}+\frac{n-k}{k(n-1)} \Delta_{\theta}-\left(\frac{n-2 k}{2 k}\right)^{2}\right] \bar{w}_{\infty} } & =0 & & (-\infty, 0) \times \mathbb{S}^{n-1} \\
\bar{w}_{\infty} & =0 & & \{0\} \times \mathbb{S}^{n-1}
\end{aligned}\right.$$
Moreover $\bar{w}_{\infty}$ is nontrivial since, in the limit point, $\left|\bar{w}_{\infty}\left(t_{\infty}, \theta_{\infty}\right)\right|>0$, and clearly verifies the inequality $\left|\bar{w}_{\infty}(t, \theta)\right| \leq(\cosh t)^{-\delta}$. Expanding $\bar{w}_{\infty}$ as
$$\bar{w}_{\infty}(t, \theta)=\sum_{j=0}^{+\infty} \bar{w}_{\infty}^{j}(t) \phi_{j}(\theta),$$
where $\phi_{j}$ are the eigenfunctions of $\Delta_{\theta}$ satisfying $-\Delta_{\theta} \phi_{j}=\lambda_{j} \phi_{j}, j \in \mathbb{N}$, we obtain from (4.11) that the components $\bar{w}_{\infty}^{j}$ are of the form
$$\bar{w}_{\infty}^{j}(t)=A e^{-\mu_{j} t}+B e^{\mu_{j} t},$$
where $A, B \in \mathbb{R}$ and
$$\mu_{j}:=\left[\frac{n-k}{k(n-1)} \lambda_{j}+\left(\frac{n-2 k}{2 k}\right)^{2}\right]^{1 / 2} .$$
Since $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$ and $\mu_{j} \geq \frac{n-2 k}{2 k}>|\delta|$, we have that $A$ must be zero. On the other hand the boundary condition implies that $B$ must be zero as well. Hence, $\bar{w}_{\infty} \equiv 0$, which contradicts the nontriviality.

Case 3: There exists a subsequence such that
$$q_{i} \longrightarrow q_{\infty}=p_{1}, \quad \alpha_{i} / \varepsilon_{i} \rightarrow+\infty \quad \text { as } \quad i \rightarrow+\infty,$$
where $\alpha_{i}:=\zeta_{\varepsilon_{i}}\left(q_{i}\right) \simeq \operatorname{dist}_{g_{1}}\left(q_{i}, p_{1}\right)$ as before. Again, since $q_{i} \rightarrow p_{1}$, the sequence of points $q_{i}$ will stay definitely in the annulus $A\left(p_{1}, 1, \varepsilon_{i}\right)$, which is mapped to $N_{1, \varepsilon_{i}}=\left(\log \varepsilon_{i}, 0\right) \times \mathbb{S}^{n-1}$ via the asymptotic cylindrical coordinates $(t, \theta)$. With the same abuse of notations as in case 2, we have $\left|w_{i}\left(q_{i}\right)\right|=\left|w_{i}\left(t_{i}, \theta_{i}\right)\right|=\alpha_{i}^{-\delta}$. To keep track of the nontriviality of the functions $w_{i}$ in the limit, it is convenient to set
$$\hat{w}_{i}(t, \theta):=\alpha_{i}^{\delta} w_{i}\left(t+t_{i}, \theta\right) .$$
Clearly, we have $\left|\hat{w}_{i}\left(0, \theta_{i}\right)\right|=1,\left|\hat{w}_{i}(t, \theta)\right| \leq 2(\cosh t)^{-\delta}$, for all $(t, \theta) \in\left(\log \varepsilon_{i}-t_{i},-t_{i}\right) \times \mathbb{S}^{n-1}$. To study the limit problem, we first observe that in this case, due to our definitions, we have $t_{i} \rightarrow-\infty$ and $\log \varepsilon_{i}-t_{i} \rightarrow-\infty$ as $i \rightarrow+\infty$. Hence, in the limit, the domain becomes $\mathbb{R} \times \mathbb{S}^{n-1}$. We define
$$\hat{u}_{\varepsilon_{i}}(t):=u_{\varepsilon_{i}}\left(t+t_{i}\right) \quad \text { and } \quad \hat{g}(t, \theta):=[1+\hat{b}(t, \theta)] g_{c y l},$$
where $\hat{b}(t, \theta):=b\left(t+t_{i}, \theta\right)$ and we recall that $u_{\varepsilon_{i}}\left(t+t_{i}\right)=\varepsilon^{(n-2 k) / 2 k} \cosh \left(\frac{n-2 k}{2 k}\left(t+t_{i}\right)\right)$ in this region. In particular we have that
$$\left\{\begin{aligned}
\mathbb{L}_{\hat{g}}\left(\hat{u}_{\varepsilon_{i}}\right)\left[\hat{w}_{i}\right] & =\alpha_{i}^{\delta} f_{i}\left(\cdot+t_{i}, \cdot \cdot\right) & & \left(\log \varepsilon_{i}-t_{i},-t_{i}\right) \times \mathbb{S}^{n-1} \\
\hat{w}_{i} & =0 & & \left\{-t_{i}\right\} \times \mathbb{S}^{n-1}
\end{aligned}\right.$$
Setting $\hat{v}_{i}(t):=\left(\varepsilon_{i} / \alpha_{i}\right)^{(n-2 k) / 2 k} \cosh \left(\frac{n-2 k}{2 k}\left(t+t_{i}\right)\right)$ and using the conformal equivariance property (1.4) we get
$$\left[\mathbb{L}_{c y l}^{0}\left(\hat{v}_{i}(1+\hat{b})\right)-\alpha_{i}^{2 k}\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} \frac{2 k n}{n-2 k}\left(\hat{v}_{i}(1+\hat{b})\right)^{\frac{2 k n}{n-2 k}-1}\right]\left[(1+\hat{b}) \hat{w}_{i}\right]=(1+\hat{b})^{\frac{2 k n}{n-2 k}} \alpha_{i}^{-\frac{n-2 k}{2 k}(2 k-1)+\delta} f_{i}\left(\cdot+t_{i}, \cdot \cdot\right)$$
with $\hat{w}_{i}\left(-t_{i}, \theta\right)=0$, for every $i \in \mathbb{N}$ and $\theta \in \mathbb{S}^{n-1}$. Since we have that the functions $\hat{w}_{i}$ are uniformly far from zero at $t=0$, we are interested in the limit behavior of the coefficients of our problem on the compact subset of $\mathbb{R} \times \mathbb{S}^{n-1}$ of the form $[-C, C] \times \mathbb{S}^{n-1}$. In this type of region it is immediate to verify that $\hat{b}=\mathcal{O}\left(\alpha_{i}^{2}\right)$ and $\hat{v}_{i}$ are uniformly converging to 1 . Since by hypothesis we have supposed that
$$\left\|f_{i}\right\|_{\mathcal{C}_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0}}\left(\Omega_{\left.1, \varepsilon_{i}\right)}\right) \longrightarrow 0,$$
we deduce that the right hand side of the expression above tends to zero in $C_{\text {loc }}^{0}\left(\mathbb{R} \times \mathbb{S}^{n-1}\right)$. Again by elliptic regularity we have the convergence of $\hat{w}_{i}$ to a function $\hat{w}_{\infty}$ in $C_{\text {loc }}^{2}\left(\mathbb{R} \times \mathbb{S}^{n-1}\right)$, which satisfies in the sense of distributions
$$\mathbb{L}_{c y l}^{0}(1)\left[\hat{w}_{\infty}\right]=-C_{n, k}\left[\partial_{t}^{2}+\frac{n-2 k+1}{(n-1)} \Delta_{\theta}-\frac{(n-2 k)^{2}}{2 k}\right] \hat{w}_{\infty}=0 \quad \mathbb{R} \times \mathbb{S}^{n-1}$$
Moreover, up to a subsequence, we have that $\theta_{i} \rightarrow \theta_{\infty} \in \mathbb{S}^{n-1}$ and $\left|\hat{w}_{\infty}\left(0, \theta_{\infty}\right)\right|=1$, hence $\hat{w}_{\infty}$ is nontrivial and clearly verifies the inequality $\left|\hat{w}_{\infty}(t, \theta)\right| \leq 2(\cosh t)^{-\delta}$. Using the separation of variables as in case 2, we have for $\hat{w}_{\infty}$ the following expansion
$$\hat{w}_{\infty}(t, \theta)=\sum_{j=0}^{+\infty} \hat{w}_{\infty}^{j}(t) \phi_{j}(\theta) .$$
Hence, we infer from (4.12) that the components $\hat{w}_{\infty}^{j}$ are of the form
$$\hat{w}_{\infty}^{j}(t)=A e^{-\nu_{j} t}+B e^{\nu_{j} t},$$
where $A, B \in \mathbb{R}$ and
$$\nu_{j}:=\left[\frac{n-2 k+1}{(n-1)} \lambda_{j}+\frac{(n-2 k)^{2}}{2 k}\right]^{1 / 2} .$$
Since $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$ and $\nu_{j} \geq \frac{n-2 k}{\sqrt{2 k}}>|\delta|$, we have that both $A$ and $B$ must be zero. Hence, $\hat{w}_{\infty} \equiv 0$, which contradicts the nontriviality. \(\square\)

We point out that thanks to the Fredholm alternative, see [6], the previous proposition also provides existence and uniqueness of solutions to problem (4.2), for sufficiently small values of the parameter $\varepsilon$.

As an easy consequence of Proposition 4.4 we get the following
Corollary 4.5. Suppose that $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$ and let $\bar{w} \in C^{2, \beta}\left(\Omega_{1, \varepsilon}\right)$ and $\psi \in C^{2, \beta}\left(\partial \Omega_{1, \varepsilon}\right)$ be two functions satisfying
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[\bar{w}] & =0 & & \Omega_{1, \varepsilon} \\
w & =\psi & & \partial \Omega_{1, \varepsilon}
\end{aligned}\right.$$
Then there exist $C=C(n, k, \delta, \beta)>0$ and $\varepsilon_{0}=\varepsilon_{0}(n, k, \delta)$ such that, for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$, we have
$$\|\bar{w}\|_{C_{\delta}^{2, \beta}\left(\Omega_{1, \varepsilon}\right)} \leq C \varepsilon^{\delta}\|\psi\|_{C^{2, \beta}\left(\partial \Omega_{1, \varepsilon}\right)} .$$
Proof. It is sufficient to observe that it is always possible to define the extension of $\psi$ as $\widetilde{\psi}(t, \theta):=\chi(t) \psi(\theta)$, where $\chi$ is a smooth nondecreasing cut-off supported in $[-1,0]$ with $\chi(0)=1$. Now we just apply the previous proposition to the function $v:=\bar{w}-\widetilde{\psi}$. The desired estimate follows from the fact that $\|\widetilde{\psi}\|_{C_{\delta}^{2, \beta}\left(\Omega_{1, \varepsilon}\right)} \leq 2 \varepsilon^{\delta}\|\psi\|_{C^{2, \beta}\left(\partial \Omega_{1, \varepsilon}\right)}$ by construction. \(\square\)

\subsection*{4.3 Dirichlet to Neumann map}

We introduce now the Dirichlet to Neumann map for the operator $\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)$ on $\Omega_{1, \varepsilon}$. For any Dirichlet data $\psi \in \mathcal{C}^{2, \beta}\left(\partial \Omega_{1, \varepsilon}\right)$, we consider the problem
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right) \bar{w} & =0 & & \Omega_{1, \varepsilon} \\
\bar{w} & =\psi & & \partial \Omega_{1, \varepsilon}
\end{aligned}\right.$$
Thanks to Corollary 4.5 for $\varepsilon$ sufficiently small, we have (uniform) a priori estimates, existence and uniqueness of a solution $\bar{w}_{1}(\psi)$ to this problem. In force of these considerations, we define the Dirichlet to Neumann map for the problem (4.13) as
$$T_{\varepsilon}: C^{2, \beta}\left(\mathbb{S}^{n-1}\right) \longrightarrow C^{1, \beta}\left(\mathbb{S}^{n-1}\right), \quad T_{\varepsilon}: \psi \longmapsto \partial_{t} \bar{w}_{1}(\psi)_{\mid \partial \Omega_{1, \varepsilon}}=: \partial_{\nu} \bar{w}_{1}(\psi)_{\mid \partial \Omega_{1, \varepsilon}},$$
where $\partial_{\nu}$ will denote the outward normal derivative to $\Omega_{1, \varepsilon}$. It follows from the considerations above that this is a well defined linear operator, which is uniformly bounded in $\varepsilon$, for $\varepsilon$ sufficiently small. The definition can be obviously extended to an operator (denoted in the same manner) acting between $H^{1}\left(\mathbb{S}^{n-1}\right)$ and $L^{2}\left(\mathbb{S}^{n-1}\right)$. In this context we will show the following
Proposition 4.6. As $\varepsilon \rightarrow 0$, the operators $T_{\varepsilon}$ converge in norm to a limit operator $T_{0}$ acting between $H^{1}\left(\mathbb{S}^{n-1}\right)$ and $L^{2}\left(\mathbb{S}^{n-1}\right)$. Moreover the operator $T_{0}$ is determined by its values on the eigenfunctions $\phi_{j}$ of the Laplacian on $\mathbb{S}^{n-1}$, namely
$$T_{0} \phi_{j}=\sqrt{\frac{n-k}{k(n-1)} \lambda_{j}+\left(\frac{n-2 k}{2 k}\right)^{2}} \phi_{j} \quad j \in \mathbb{N}$$
Proof. Let $\bar{w}$ be the solution to the homogeneous problem (4.13) with boundary datum $\psi=\phi_{j}$. Using the conformal equivariance property (1.4) on $(\gamma \log \varepsilon, 0) \times \mathbb{S}^{n-1}$, with $\gamma \in(0,1)$, we obtain the equation
$$\left[\mathbb{L}_{c y l}^{0}\left(v_{\Sigma}(1+b)\right)-\varepsilon^{2 k}\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} \frac{2 k n}{n-2 k}\left(v_{\Sigma}(1+b)\right)^{\frac{2 k n}{n-2 k}-1}\right][(1+b) \bar{w}]=0 .$$
Since $b$ can be estimated in this region as $b=\mathcal{O}\left(\varepsilon^{2(1-\gamma)}\right)$, we have that the linear operator on the left hand side can be written as
$$-C_{n, k} v_{\Sigma}\left[\partial_{t}^{2}+\frac{n-k}{k(n-1)} \Delta_{\theta}-\left(\frac{n-2 k}{2 k}\right)^{2}+\varepsilon^{2(1-\gamma)} \mathcal{P}\right]$$
where $\mathcal{P}$ is a linear second order partial differential operator with bounded coefficients. Using separation of variables we write $\bar{w}$ as
$$\bar{w}=\sum_{i=0}^{+\infty} \bar{w}^{i}(t) \cdot \phi_{i}(\theta) .$$
Projecting along the $j$-th component, we obtain
$$\left\{\begin{aligned}
\partial_{t}^{2} \bar{w}^{j}-\left[\frac{n-k}{k(n-1)} \lambda_{j}+\left(\frac{n-2 k}{2 k}\right)^{2}\right] \bar{w}^{j}+\varepsilon^{2(1-\gamma)}\left\langle\mathcal{P} \bar{w}, \phi_{j}\right\rangle_{L^{2}\left(\mathbb{S}^{n-1}\right)} & =0 \quad t \in[\gamma \log \varepsilon, 0) \\
\bar{w}^{j}(0) & =1
\end{aligned}\right.$$
As in previous subsection we let $\mu_{i}$ be the real number
$$\mu_{i}:=\sqrt{\frac{n-k}{k(n-1)} \lambda_{i}+\left(\frac{n-2 k}{2 k}\right)^{2}} \quad i \in \mathbb{N} .$$
Let $\chi$ be a positive smooth non decreasing cutoff function defined on $[\log \varepsilon, 0]$, such that $\chi(t)=1$ for all $t \in[\gamma \log \varepsilon+1,0]$ and $\chi(t)=0$ for all $t \in[\log \varepsilon, \gamma \log \varepsilon]$. Multplying the equation above by $\chi(t) e^{\mu_{j} t}$ and integrating by parts, yields
$$\begin{aligned}
\partial_{t} \bar{w}^{j}(0)-\mu_{j} & =\int_{\gamma \log \varepsilon}^{0}\left[\frac{n-k}{k(n-1)} \lambda_{j}+\left(\frac{n-2 k}{2 k}\right)^{2}-\mu_{j}^{2}\right] \bar{w}^{j}(t) \chi(t) e^{\mu_{j} t} d t \\
& -2 \mu_{j} \int_{\gamma \log \varepsilon}^{\gamma \log \varepsilon+1} \bar{w}^{j}(t)\left(\partial_{t} \chi\right)(t) e^{\mu_{j} t} d t-\int_{\gamma \log \varepsilon}^{\gamma \log \varepsilon+1} \bar{w}^{j}(t)\left(\partial_{t}^{2} \chi\right)(t) e^{\mu_{j} t} d t \\
& +\varepsilon^{2(1-\gamma)} \int_{\gamma \log \varepsilon}^{0}\left\langle\mathcal{P} \bar{w}, \phi_{j}\right\rangle_{L^{2}\left(\mathbb{S}^{n-1}\right)} \chi(t) e^{\mu_{j} t} d t .
\end{aligned}$$

We claim that the right hand side tends to zero as $\varepsilon \rightarrow 0$. By Proposition 4.4 we have that for every fixed $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$ and every $\varepsilon \in\left(0, \varepsilon_{0}\right]$
$$\left|\bar{w}^{j}(t)\right| \leq C e^{-\delta t} \quad t \in \mathbb{R},$$
where $C>0$ is a uniform positive constant. Since $\mu_{j}>|\delta|$, we get that there exist a positive constant $B=B(n, k, \delta, \gamma)$ such that
$$\left|\partial_{t} \bar{w}^{j}(0)-\mu_{j}\right| \leq B \varepsilon^{\nu},$$
where $\nu:=\min \left\{2(1-\gamma), \gamma\left(\mu_{0}-\delta\right)\right\}>0$. Now, the converge in norm of the operator $T_{\varepsilon}$ to $T_{0}$ for $\varepsilon \rightarrow 0$ follows easily. Infact, using separation of variables and writing $\psi$ as $\psi=\sum_{j=0}^{+\infty} \psi^{j} \phi_{j}(\theta)$, we get
$$\begin{aligned}
\left\|\left(T_{\varepsilon}-T_{0}\right) \psi\right\|_{L^{2}\left(\mathbb{S}^{n-1}\right)}^{2} & =\left\|\sum_{j=0}^{+\infty} \psi^{j}\left(T_{\varepsilon}-T_{0}\right)\left(\phi_{j}\right)\right\|_{L^{2}\left(\mathbb{S}^{n-1}\right)}^{2}=\left\|\sum_{j=0}^{+\infty} \psi^{j}\left(\partial_{t} \bar{w}^{j}(0)-\mu_{j}\right) \phi_{j}\right\|_{L^{2}\left(\mathbb{S}^{n-1}\right)}^{2} \\
& =\sum_{j=0}^{+\infty}\left|\psi^{j}\left(\partial_{t} \bar{w}^{j}(0)-\mu_{j}\right)\right|^{2} \leq B^{2} \varepsilon^{2 \nu}\|\psi\|_{H^{1}\left(\mathbb{S}^{n-1}\right)}^{2},
\end{aligned}$$
which ends the proof of the proposition. \(\square\)

In the same way, we can define the Dirichlet to Neumann map for the problem
$$\left\{\begin{aligned}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right) \bar{w} & =0 & & \Omega_{2, \varepsilon} \\
\bar{w} & =\psi & & \partial \Omega_{2, \varepsilon}
\end{aligned}\right.$$
as
$$S_{\varepsilon}: C^{2, \beta}\left(\mathbb{S}^{n-1}\right) \longrightarrow C^{1, \beta}\left(\mathbb{S}^{n-1}\right), \quad S_{\varepsilon}:\left.\psi \longmapsto \partial_{t} \bar{w}_{\psi}\right|_{\partial \Omega_{2, \varepsilon}}=-\left.\partial_{\nu} \bar{w}_{\psi}\right|_{\partial \Omega_{2, \varepsilon}},$$
where $\partial_{\nu}$ is the outward normal derivative to $\Omega_{1, \varepsilon}$, as before.
Proposition 4.7. As $\varepsilon \rightarrow 0$, the operators $S_{\varepsilon}$ converge in norm to a limit operator $S_{0}$ acting between $H^{1}\left(\mathbb{S}^{n-1}\right)$ and $L^{2}\left(\mathbb{S}^{n-1}\right)$. Moreover the operator $S_{0}$ is determined by its values on the eigenfunctions $\phi_{j}$ of the Laplacian on $\mathbb{S}^{n-1}$, namely
$$S_{0} \phi_{j}=-\sqrt{\frac{n-k}{k(n-1)} \lambda_{j}+\left(\frac{n-2 k}{2 k}\right)^{2}} \phi_{j} \quad j \in \mathbb{N} .$$
The proof is identical to the one of Proposition 4.6.

\subsection*{4.4 Cauchy data matching}

Let $w_{i}$ and $\bar{w}_{i}=\bar{w}_{i}(\psi), i=1,2$, be the solutions to the problems
$$\left\{\begin{array} { r l } 
{ \mathbb { L } _ { \overline { g } } ( u _ { \varepsilon } ) w _ { i } = f } & { \Omega _ { i , \varepsilon } } \\
{ w _ { i } = 0 } & { \partial \Omega _ { i , \varepsilon } }
\end{array} \quad \text { and } \quad \left\{\begin{array}{rl}
\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right) \bar{w}_{i}=0 & \Omega_{i, \varepsilon} \\
\bar{w}_{i}=\psi & \partial \Omega_{i, \varepsilon}
\end{array}\right.\right.$$
We define the global function $w$ as
$$w:= \begin{cases}w_{1}+\bar{w}_{1}(\psi) & \Omega_{1, \varepsilon} \\ w_{2}+\bar{w}_{2}(\psi) & \Omega_{2, \varepsilon}\end{cases}$$
We claim that for $\varepsilon$ sufficiently small, there exists a function $\psi$, such that
$$\partial_{\nu}\left(w_{1}+\bar{w}_{1}(\psi)\right)=-\partial_{\nu}\left(w_{2}+\bar{w}_{2}(\psi)\right) .$$
This is equivalent to
$$\partial_{\nu} w_{1}+\partial_{\nu} w_{2}=-\left(T_{\varepsilon}-S_{\varepsilon}\right)(\psi) .$$
Hence, we need to invert the operator
$$\left(T_{\varepsilon}-S_{\varepsilon}\right): C^{2, \beta}\left(\mathbb{S}^{n-1}\right) \longrightarrow C^{1, \beta}\left(\mathbb{S}^{n-1}\right)$$

Lemma 4.8. There exists a positive real number $\varepsilon_{0}=\varepsilon_{0}(n, k, \delta)>0$ such that for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$ and for every $\eta \in C^{1, \beta}\left(\mathbb{S}^{n-1}\right)$ there exists a unique $\psi \in C^{2, \beta}\left(\mathbb{S}^{n-1}\right)$ such that
$$\left(T_{\varepsilon}-S_{\varepsilon}\right)(\psi)=\eta .$$
Moreover, there exist a positive constant $C=C(n, k, \delta)>0$ such that
$$\|\psi\|_{C^{2, \beta}\left(\mathbb{S}^{n-1}\right)} \leq C\|\eta\|_{C^{1, \beta}\left(\mathbb{S}^{n-1}\right)} .$$
Proof. As a first step, for $\varepsilon$ sufficiently small, we will prove the invertibility of $\left(T_{\varepsilon}-S_{\varepsilon}\right)$ as operator acting between $H^{1}\left(\mathbb{S}^{n-1}\right)$ and $L^{2}\left(\mathbb{S}^{n-1}\right)$ and in this context we will provide uniform a priori estimates for solutions to
$$\left(T_{\varepsilon}-S_{\varepsilon}\right)(\psi)=\eta .$$
The analogous result in Hölder spaces will follow from the standard elliptic theory for first order pseudodifferential operators with bounded spectrum.

From Proposition 4.6 and Proposition 4.7 we deduce that the operators $\left(T_{\varepsilon}-S_{\varepsilon}\right)$ converge in norm to the linear operator $T_{0}-S_{0}$, defined as follows
$$\left(T_{0}-S_{0}\right)\left(\phi_{j}\right)=2 \mu_{j} \phi_{j} \quad \mu_{j}=\sqrt{\frac{n-k}{k(n-1)} \lambda_{j}+\left(\frac{n-2 k}{2 k}\right)^{2}} \quad j \in \mathbb{N}$$
where, as usual, the functions $\phi_{j}$ 's are the eigenfunctions of $\Delta_{\mathbb{S}^{n-1}}$ and verify $-\Delta \phi_{j}=\lambda_{j} \phi_{j}, j \in \mathbb{N}$. Hence it is sufficient to show that the limit operator $\left(T_{0}-S_{0}\right)$ is invertible and verifies the a priori estimates. Using the Fourier expansion for $\eta$, namely $\eta=\sum_{j=0}^{+\infty} \eta^{j} \phi_{j}$, we have that the ansatz for $\psi$ is given by $\sum_{j=0}^{+\infty}\left(\eta^{j} / 2 \mu_{j}\right) \phi_{j}$. Now we need to verify that this function lies in $H^{1}\left(\mathbb{S}^{n-1}\right)$, in other words we need to test that
$$\sum_{j=0}^{+\infty}\left(1+\lambda_{j}\right)\left|\left(\eta^{j} / 2 \mu_{j}\right)\right|^{2}<+\infty .$$
From the definition of the $\mu_{j}$ 's it is straightforward to deduce that there exists a positive constant $C=C(n, k)>0$ such that $\left(1+\lambda_{j}\right) / 4 \mu_{j}^{2} \leq C$. Thus
$$\sum_{j=0}^{+\infty}\left(1+\lambda_{j}\right)\left|\left(\eta^{j} / 2 \mu_{j}\right)\right|^{2} \leq C\|\eta\|_{L^{2}\left(\mathbb{S}^{n-1}\right)}^{2} .$$
Setting $\psi:=\sum_{j=0}^{+\infty}\left(\eta^{j} / 2 \mu_{j}\right) \phi_{j} \in H^{1}\left(\mathbb{S}^{n-1}\right)$ we have that $\psi$ solves the desired equation with the estimate
$$\|\psi\|_{H^{1}\left(\mathbb{S}^{n-1}\right)} \leq C^{1 / 2}\|\eta\|_{L^{2}\left(\mathbb{S}^{n-1}\right)} .$$
This completes the proof. \(\square\)

So now we can define the function $\psi$ as
$$\psi:=\left(T_{\varepsilon}-S_{\varepsilon}\right)^{-1}\left[-\partial_{\nu} w_{1}-\partial_{\nu} w_{2}\right] .$$
Moreover, using the previous lemma and Proposition 4.4, for $\varepsilon$ sufficiently small, we have the uniform bound
$$\begin{aligned}
\|\psi\|_{C^{2, \beta}\left(\mathbb{S}^{n-1}\right)} & \leq C\left[\left\|\partial_{\nu} w_{1}\right\|_{C^{1, \beta}\left(\mathbb{S}^{n-1}\right)}+\left\|\partial_{\nu} w_{2}\right\|_{C^{1, \beta}\left(\mathbb{S}^{n-1}\right)}\right] \\
& \leq C_{1} \varepsilon^{-\delta}\left[\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(\Omega_{1, \varepsilon}\right)}+\left\|w_{2}\right\|_{C_{\delta}^{2, \beta}\left(\Omega_{2, \varepsilon}\right)}\right] \\
& \leq C_{2} \varepsilon^{-\delta}\|f\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0, \beta}\left(M_{\varepsilon}\right)}
\end{aligned}$$
where the positive constant $C_{1}>0$ and $C_{2}>0$ only depend on $n, k$ and $\delta$. From this estimate, together with Proposition 4.4 and Proposition 4.5 we obtain
$$\begin{aligned}
\|w\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} & \leq\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(\Omega_{1, \varepsilon}\right)}+\left\|\bar{w}_{1}(\psi)\right\|_{C_{\delta}^{2, \beta}\left(\Omega_{1, \varepsilon}\right)}+\left\|w_{2}\right\|_{C_{\delta}^{2, \beta}\left(\Omega_{2, \varepsilon}\right)}+\left\|\bar{w}_{2}(\psi)\right\|_{C_{\delta}^{2, \beta}\left(\Omega_{2, \varepsilon}\right)} \\
& \leq C_{3}\left[\|f\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0, \beta}\left(M_{\varepsilon}\right)}+\varepsilon^{\delta}\|\psi\|_{C^{2, \beta}\left(\mathbb{S}^{n-1}\right)}\right] \\
& \leq C_{4}\|f\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0, \beta}\left(M_{\varepsilon}\right)},
\end{aligned}$$
where the positive constant $C_{3}>0$ and $C_{4}>0$ only depend on $n, k$ and $\delta$.
We collect all the results of this section in the following
Proposition 4.9. Let $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$, then there exists a real number $\varepsilon_{0}=\varepsilon_{0}(n, k, \delta)>0$ such that for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$ and every $f \in C^{0, \beta}\left(M_{\varepsilon}\right)$ there exists a unique solution $w \in C^{2, \beta}\left(M_{\varepsilon}\right)$ to the problem
$$\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)[w]=f \quad M_{\varepsilon} .$$
Moreover, there exists a positive constant $C=C(n, k, \delta)>0$ such that for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$
$$\|w\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} \leq C\|f\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0, \beta}\left(M_{\varepsilon}\right)} .$$
Remark 4.10. We point out that using standard elliptic theory it is possible to extend the estimates above to higher order derivatives, without changing the weight parameters. The only difference is that the constant $C$ will possibly depend on the number of the derivatives involved.

\section*{5 Nonlinear analysis}

Now we are ready to solve the fully nonlinear equation
$$\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}+w\right)=0 .$$
Thanks to Proposition 4.9, which provides invertibility for the operator $\mathbb{L} \bar{g}\left(u_{\varepsilon}\right)$, this amounts to solve the fixed point problem
$$w=\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)^{-1}\left[-\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)-\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)(w)\right],$$
where we recall that the quadratic remainder is given by
$$\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)(w):=-\int_{0}^{1}\left[\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)-\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}+s w\right)\right][w] d s$$
We will find the fixed point $w$ as the limit of the sequence $\left\{w_{i}\right\}_{i \in \mathbb{N}}$ defined by means of the following Newton iteration scheme
$$\begin{cases}w_{0} & :=0 \\ w_{i+1} & :=\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)^{-1}\left[-\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)-\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{i}\right)\right], \quad i \in \mathbb{N} .\end{cases}$$

\subsection*{5.1 Estimate of the proper error}

As a first step we estimate the proper error term $\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)$, which is supported in the neck region $T_{\varepsilon}$. It is convenient to divide this region into three subdomains $T_{1, \varepsilon}:=[\log \varepsilon,(2 k / n) \log \varepsilon] \times \mathbb{S}^{n-1}, T_{2, \varepsilon}:=$ $[-(2 k / n) \log \varepsilon,-\log \varepsilon] \times \mathbb{S}^{n-1}$ and $T_{\Sigma, \varepsilon}:=[(2 k / n) \log \varepsilon,-(2 k / n) \log \varepsilon] \times \mathbb{S}^{n-1}$. We start by considering the proper error on $T_{1, \varepsilon}$. With the only exception of the annulus $[\log \varepsilon, \log \varepsilon+1] \times \mathbb{S}^{n-1}$ (where it is easy to verify that the estimate that we are going to obtain is even better), on this region we can write
$$g_{1}=u_{1}^{\frac{4 k}{n-2 k}}\left(1+b_{1}\right)^{\frac{4 k}{n-2 k}} g_{\text {cyl }} \quad \text { and } \quad u_{\varepsilon}=u_{1}\left(1+e^{\frac{n-2 k}{2 k} t}\right) .$$
Combining these two expression with the conformal equivariance property (1.4), we obtain
$$\begin{aligned}
\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right) & =u_{1}^{\frac{2 k n}{n-2 k}} \mathcal{N}_{g_{1}}\left(1+e^{\frac{n-2 k}{k} t}\right) \\
& =u_{1}^{\frac{2 k n}{n-2 k}}\left\{\mathbb{L}_{g_{1}}(1)\left[e^{\frac{n-2 k}{k} t}\right]+\mathcal{Q}_{g_{1}}(1)\left(e^{\frac{n-2 k}{k} t}\right)\right\} \\
& =\left(1+b_{1}\right)^{-\frac{2 k n}{n-2 k}}\left\{\mathbb{L}_{c y l}\left(\left(1+b_{1}\right) u_{1}\right)\left[\left(1+b_{1}\right) u_{1} e^{\frac{n-2 k}{k} t}\right]+\mathcal{Q}_{c y l}\left(\left(1+b_{1}\right) u_{1}\right)\left(\left(1+b_{1}\right) u_{1} e^{\frac{n-2 k}{k} t}\right)\right\},
\end{aligned}$$
since $\mathcal{N}_{g_{1}}(1)=0$. Due to the fact that the coefficients of $\mathbb{L}_{\text {cyl }}\left(\left(1+b_{1}\right) u_{1}\right)[\cdot]$ are readily estimated as $\mathcal{O}\left(\varepsilon^{\frac{n-2 k}{2 k}(2 k-1)} e^{-\frac{n-2 k}{2 k}(2 k-1) t}\right)$, we obtain
$$\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right) \simeq(\varepsilon \cosh t)^{n-2 k} e^{\frac{n-2 k}{k} t} \text { in } T_{1, \varepsilon} .$$
Using the same argument it is straightforward to verify that
$$\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right) \simeq(\varepsilon \cosh t)^{n-2 k} e^{-\frac{n-2 k}{k} t} \quad \text { in } T_{2, \varepsilon} .$$
In the remaining region, namely $T_{\Sigma, \varepsilon}$, we set $g_{\Sigma, \varepsilon}:=u_{\varepsilon}^{4 k /(n-2 k)} g_{\text {cyl }}$ and we write $\bar{g}=(1+b)^{4 k /(n-2 k)} g_{\text {cyl }}$. From the conformal equivariance (1.4), we obtain
$$\begin{aligned}
\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right) & =\left((1+b) u_{\varepsilon}^{-1}\right)^{-\frac{2 k n}{n-2 k}} \mathcal{N}_{\Sigma, \varepsilon}(1+b) \\
& =\left((1+b) u_{\varepsilon}^{-1}\right)^{-\frac{2 k n}{n-2 k}}\left\{\mathcal{N}_{\Sigma, \varepsilon}(1)+\mathbb{L}_{\Sigma, \varepsilon}(1)[b]+\mathcal{Q}_{\Sigma, \varepsilon}(1)(b)\right\} \\
& =(1+b)^{-\frac{2 k n}{n-2 k}}\left\{-\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} u_{\varepsilon}^{\frac{2 k n}{n-2 k}}+\mathbb{L}_{c y l}\left(u_{\varepsilon}\right)\left[u_{\varepsilon} b\right]+\mathcal{Q}_{c y l}\left(u_{\varepsilon}\right)\left(u_{\varepsilon} b\right)\right\},
\end{aligned}$$
since $\sigma_{k}\left(B_{\Sigma, \varepsilon}\right)=0$. Recalling the expression of the (homogeneous) linearized operator around a $\sigma_{k}-$ Schwarzschild metric, we have
$$\mathbb{L}_{c y l}\left(u_{\varepsilon}\right)\left[u_{\varepsilon} b\right]=-C_{n, k} \varepsilon^{\frac{n-2 k}{k}(k-1)} u_{\varepsilon}\left[\partial_{t}^{2}+\frac{n-k}{k(n-1)} \Delta_{\theta}-\left(\frac{n-2 k}{2 k}\right)^{2}\right]\left[u_{\varepsilon} b\right]-\binom{n}{k}\left(\frac{n-2 k}{4 k}\right)^{k} \frac{2 k n}{n-2 k} u_{\varepsilon}^{\frac{2 k n}{n-2 k}} b .$$
Due to the fact that in $T_{\Sigma, \varepsilon}$ one has $b=\mathcal{O}\left(\varepsilon^{2} e^{-2 t}\right)$ and $u_{\varepsilon}=\mathcal{O}\left((\varepsilon \cosh t)^{(n-2 k) / 2 k}\right)$, we infer that
$$\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right) \simeq \varepsilon^{n-2 k+2}(\cosh t)^{\frac{n}{k}} \quad \text { in } T_{\Sigma, \varepsilon} .$$
From these computations and from the definition of the weighted Hölder spaces it follows at once the following

Lemma 5.1. There exists a positive constant $A=A(n, k)>0$ such that for every $\delta \in\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$ the proper error is estimated as
$$\left\|\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)\right\|_{C_{\delta-\frac{n-2 k}{2 k}(2 k-1)}^{0, \beta}\left(M_{\varepsilon}\right)} \leq A \varepsilon^{\frac{n-2 k}{n}\left(\frac{n+2 k}{2 k}+\delta\right)} \text {. }$$

\subsection*{5.2 Fixed point argument}

To simplify the notations of this subsection we define the two real numbers $\mu=\mu(n, k, \delta)$ and $\nu=\nu(n, k, \delta)$ as
$$\begin{aligned}
& \mu:=\delta-\frac{(n-2 k)(2 k-1)}{2 k} \\
& \nu:=\frac{n-2 k}{n}\left(\frac{n+2 k}{2 k}+\delta\right)
\end{aligned}$$
since $\delta$ varies in $\left(-\frac{n-2 k}{2 k}, \frac{n-2 k}{2 k}\right)$, we have that $\mu$ varies in $\left(2 k-n,-\frac{(n-2 k)(k-1)}{k}\right)$ and $\nu$ varies in $\left(\frac{2(n-2 k)}{n}, \frac{n-2 k}{k}\right)$.

To prove the convergence of the Newton iteration scheme (5.3) we start by estimating $w_{1}$. Thanks to $a$ priori estimate for the linearized equation and to the estimate of the proper error term, we immediately get
$$\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} \leq A C \varepsilon^{\nu},$$
where the positive constants $A=A(n, k, \delta)>0$ and $C=C(n, k, \delta)>0$ are the ones given in Lemma 5.1 and Proposition 4.9, respectively. Since to achieve our goal it is important to keep track of the precise
role played by these constants in the estimate, we point out that all through this section the letters $A$ and $C$ will represent the constants obtained in the estimate of Lemma 5.1 and Proposition 4.9.

We pass now to estimate the term $w_{2}$. From its definition it follows at once that
$$\begin{aligned}
\left\|w_{2}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} & \leq C\left\|\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)+\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right\|_{C_{\mu}^{0, \beta}\left(M_{\varepsilon}\right)} \\
& \leq A C \varepsilon^{\nu}+C\left\|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right\|_{C_{\mu}^{0, \beta}\left(M_{\varepsilon}\right)} .
\end{aligned}$$
Now we need to estimate the quadratic remainder. Recalling the definition of the weighted norm we have
$$\begin{aligned}
\left\|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right\|_{C_{\mu}^{0, \beta}\left(M_{\varepsilon}\right)}:= & \sum_{i=1}^{2}\left\|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{i}\right)\right\|_{C^{0, \beta}\left(M_{i} \backslash B\left(p_{i}, 1\right)\right)}+\sup _{T_{\varepsilon}}(\varepsilon \cosh t)^{\mu}\left|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right| \\
& +\sup _{(t, \theta) \in T_{\varepsilon}}\left\{(\varepsilon \cosh t)^{\mu} \sup _{(t, \theta) \neq\left(t^{\prime}, \theta^{\prime}\right)} \frac{\left|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)(t, \theta)-\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\left(t^{\prime}, \theta^{\prime}\right)\right|}{\left|\operatorname{dist}_{g_{\varepsilon}}\left((t, \theta),\left(t^{\prime}, \theta^{\prime}\right)\right)\right|^{\beta}}\right\}
\end{aligned}$$
The first term readily estimated as
$$\sum_{i=1}^{2}\left\|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right\|_{C^{0, \beta}\left(M_{i} \backslash B\left(p_{i}, 1\right)\right)} \leq D_{0}\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} \leq A C D_{0} \varepsilon^{\nu},$$
where the positive constant $D_{0}>0$ only depends on $n, k$ and the $C^{2}$-norm of the coefficients of the metrics $g_{1}$ and $g_{2}$. We pass now to consider the term $(\varepsilon \cosh t)^{\mu}\left|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right|$. Applying the conformal equivariance property, we get
$$\begin{aligned}
(\varepsilon \cosh t)^{\mu}\left|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right| & \leq(\varepsilon \cosh t)^{\mu} \int_{0}^{1}\left|\left[\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\right)-\mathbb{L}_{\bar{g}}\left(u_{\varepsilon}\left(1+s u_{\varepsilon}^{-1} w_{1}\right)\right)\right]\left[u_{\varepsilon}^{-1} w_{1}\right]\right| d s \\
& \leq(\varepsilon \cosh t)^{\mu} \varepsilon^{\frac{n-2 k}{2 k}(2 k-1)} \int_{0}^{1}\left|\left[\mathbb{L}_{\bar{g}}\left(v_{\Sigma}\right)-\mathbb{L}_{\bar{g}}\left(v_{\Sigma}\left(1+s u_{\varepsilon}^{-1} w_{1}\right)\right)\right]\left[u_{\varepsilon}^{-1} w_{1}\right]\right| d s
\end{aligned}$$
To estimate the right hand side on $T_{\varepsilon}$, we observe that there exists a positive constant $D_{1}>0$ only depending on $n$ and $k$ such that, for $j=0,1,2$, we have
$$\left|\nabla_{\bar{g}}^{j}\left(u_{\varepsilon}^{-1} w_{1}\right)\right|_{\bar{g}} \leq D_{1}(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}}\left\|w_{1}\right\|_{C_{\delta}^{2}\left(M_{\varepsilon}\right)} \leq A C D_{1}(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}} \varepsilon^{\nu} .$$
Since $-\delta-(n-2 k) / 2 k<\nu$ we infer that the coefficients of the linear operator $\mathbb{L}_{\bar{g}}\left(v_{\Sigma}\right)-\mathbb{L}_{\bar{g}}\left(v_{\Sigma}\left(1+s u_{\varepsilon}^{-1} w_{1}\right)\right)$ can be estimated on $T_{\varepsilon}$ as $\mathcal{O}\left(v_{\Sigma}^{2 k-1}\left[\left|u_{\varepsilon}^{-1} w_{1}\right|+\left|\nabla_{\bar{g}}\left(u_{\varepsilon}^{-1} w_{1}\right)\right|_{\bar{g}}+\left|\nabla_{\bar{g}}^{2}\left(u_{\varepsilon}^{-1} w_{1}\right)\right|_{\bar{g}}\right]\right)$. We deduce that there exists a positive constant $D_{2}$ only depending on $n$ and $k$ such that
$$\left|\left[\mathbb{L}_{\bar{g}}\left(v_{\Sigma}\right)-\mathbb{L}_{\bar{g}}\left(v_{\Sigma}\left(1+s u_{\varepsilon}^{-1} w_{1}\right)\right)\right]\left[u_{\varepsilon}^{-1} w_{1}\right]\right| \leq D_{2}(\cosh t)^{\frac{n-2 k}{2 k}(2 k-1)}(\varepsilon \cosh t)^{-2 \delta-\frac{n-2 k}{2 k}}\left\|w_{1}\right\|_{C_{\delta}^{2}\left(M_{\varepsilon}\right)}^{2} .$$
We end up with
$$(\varepsilon \cosh t)^{\mu}\left|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right| \leq D_{3}(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}}\left\|w_{1}\right\|_{C_{\delta}^{2}\left(M_{\varepsilon}\right)}^{2} .$$
Using the same argument one can deduce the analogous bound for the Hölder ratio, namely
$$(\varepsilon \cosh t)^{\mu} \sup _{(t, \theta) \neq\left(t^{\prime}, \theta^{\prime}\right)} \frac{\left|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)(t, \theta)-\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\left(t^{\prime}, \theta^{\prime}\right)\right|}{\left|\operatorname{dist}_{g_{\varepsilon}}\left((t, \theta),\left(t^{\prime}, \theta^{\prime}\right)\right)\right|^{\beta}} \leq D_{4}(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}}\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)}^{2},$$
for some positive constant $D_{3}$ and $D_{4}$ only depending on $n$ and $k$. Collecting these estimates one can conclude that the quadratic remainder $\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)$ verifies
$$\left\|\mathcal{Q}_{\bar{g}}\left(u_{\varepsilon}\right)\left(w_{1}\right)\right\|_{C_{\mu}^{0, \beta}\left(M_{\varepsilon}\right)} \leq D \cdot(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}}\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)}^{2},$$
where the positive constant $D>0$ only depends on $n, k$ and the $C^{2}$-norm of the coefficients of the metrics $g_{1}$ and $g_{2}$. Continuing the estimate in (5.5), we get
$$\begin{aligned}
\left\|w_{2}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} & \leq A C \varepsilon^{\nu}+C D(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}}\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)}^{2} \\
& \leq A C \varepsilon^{\nu}+A C^{2} D(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}} \varepsilon^{\nu}\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} \\
& =A C \varepsilon^{\nu}+B\left\|w_{1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)},
\end{aligned}$$
where in the second inequality we have used (5.4) and we have set
$$B:=A C^{2} D(\varepsilon \cosh t)^{-\delta-\frac{n-2 k}{2 k}} \varepsilon^{\nu} .$$
Since $-\delta-(n-2 k) / 2 k<\nu$, there exists a real number $\varepsilon_{0}=\varepsilon_{0}(n, k, \delta, D)>0$ such that, for every $\varepsilon \in\left(0, \varepsilon_{0}\right]$, one can choose $B \leq \frac{1}{4}$. In general we obtain for every $j \geq 1$
$$\left\|w_{j+1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} \leq A C \varepsilon^{\nu} a_{j+1},$$
where the sequence $a_{j}$ is inductively defined as
$$\left\{\begin{aligned}
a_{1} & :=1 \\
a_{j+1} & :=1+\frac{1}{4} a_{j}^{2}, \quad j \in \mathbb{N} .
\end{aligned}\right.$$
Since $\sup _{j} a_{j} \leq 2$, one has
$$\left\|w_{j+1}\right\|_{C_{\delta}^{2, \beta}\left(M_{\varepsilon}\right)} \leq 2 A C \varepsilon^{\nu} .$$
Exploiting once again the definition of the weighted norm, we obtain
$$\left\|w_{j+1}\right\|_{C^{2, \beta}\left(M_{\varepsilon}\right)} \leq E \varepsilon^{\nu-\delta},$$
for some positive constant $E=E(n, k, \delta, D)>0$. From this inequality, we have that the $w_{i}$ 's are equibounded in $C^{2, \beta}\left(M_{\varepsilon}\right)$ and then, up to a subsequence, they converge in $C^{2}\left(M_{\varepsilon}\right)$ to a fixed point $w_{\varepsilon}$ for the problem (5.2). To conclude, we have that there exists a number $\varepsilon_{0}=\varepsilon_{0}(n, k, \delta, D)>0$ such that for $\varepsilon \in\left(0, \varepsilon_{0}\right]$ the metrics
$$\widetilde{g}_{\varepsilon}:=\left(1+u_{\varepsilon}^{-1} w_{\varepsilon}\right)^{\frac{4 k}{n-2 k}} g_{\varepsilon},$$
where $g_{\varepsilon}$ are the explicit approximate solution metrics given in Section 3, have positive constant $\sigma_{k}-$ curvature equal to $2^{-k}\binom{n}{k}$. Finally we recall that by construction the approximate solutions metrics $g_{\varepsilon}$ were converging to the initial metric $g_{i}$ with respect to the $C^{2}$-topology on the compact subsets of $M_{i} \backslash\left\{p_{i}\right\}$, for $i=1,2$, as $\varepsilon \rightarrow 0$. On the other hand we have that
$$\left\|u_{\varepsilon}^{-1} w_{\varepsilon}\right\|_{C^{2}\left(M_{\varepsilon}\right)} \leq F \varepsilon^{\nu-\delta-\frac{n-2 k}{2 k}}$$
for some positive constant $F=F(n, k, \delta, D)>0$. Since $\nu-\delta-(n-2 k) / 2 k>0$ we have that also the exact solutions $\widetilde{g}_{\varepsilon}$ tend to the initial metric $g_{i}$ with respect to the $C^{2}$-topology on the compact subsets of $M_{i} \backslash\left\{p_{i}\right\}$, for $i=1,2$, as $\varepsilon \rightarrow 0$.

Concerning the regularity of our solution $w_{\varepsilon}$, so far we have obtained that it belongs to $C^{2}\left(M_{\varepsilon}\right)$. On the other hand, as observed in Remark 4.10, it is possible to obtain uniform $C_{\delta}^{m, \beta}$-estimates for solutions to the linearized equation, for every $m \in \mathbb{N}$. Since the proper error term which appears in first step of the Newton iteration scheme is clearly smooth by construction, one can extend (5.6) to
$$\left\|w_{j+1}\right\|_{C^{m, \beta}\left(M_{\varepsilon}\right)} \leq E \varepsilon^{\nu-\delta},$$
where the positive constant $E$ may possibly depend also on $m$. The fact that $m$ is arbitrary in $\mathbb{N}$ implies that $w_{\varepsilon}$ is smooth.

We observe now $\widetilde{g}_{\varepsilon}$ lies in the positive cone $\Gamma_{k}^{+}$, as stated in Theorem 1. To see this fact we just need to show that $\sigma_{j}\left(\widetilde{g}_{\varepsilon}^{-1} A_{\widetilde{g}_{\varepsilon}}\right)>0$ for every $j=1, \ldots, k-1$, since $\widetilde{g}_{\varepsilon}$ has constant $\sigma_{k}$-curvature equal to $2^{-k}\binom{n}{k}$. This follows from (5.7) together with the fact that the approximate solutions $g_{\varepsilon}$ 's belong to $\Gamma_{k-1}^{+}$, for $\varepsilon$ small enough, see Lemma 3.2.

To conclude, we need to discuss how to remove Assumption 3.1. Going through the proof it can be seen that all the analysis (uniform a priori estimate, estimate of the error term, etc.) is essentially based on blow-up techniques. For instance in the linear analysis this fact has allowed us to overcome the computational difficulty of writing down a global expression for the linearized operator about the approximate solution metrics $g_{\varepsilon}$ (which due to the fully nonlinear nature of our problem is rather intricate for $k>1$ ), letting us concentrate only on its limit behavior around the blow-up points. As a consequence one can realize that the only important features of our approximate solutions are the ones which become relevant in the limit for $\varepsilon \rightarrow 0$. It is in this limit for example that the use of the $\sigma_{k}$-Schwarzschild metric as a model metric on the neck reveals to be a clever choice. Having this in mind and looking at the expressions (3.4) and (3.2), it is now straightforward to verify that all the limit features of our approximates solutions are not affected when the Assumption 3.1 is not in force, since the coefficients $a$ 's which measure the discrepancy from the model metric in the general construction are of the same size of the $c$ 's in 3.4. This shows that the linear analysis issues still hold true in the general case. Concerning the estimate of the error term, which is the crucial step in the implementation of the Newton scheme once the uniform a priori estimates are provided, one can see reasoning as above that the only place where the proper error may possibly have a worse behavior is in the regions of the type $[\log \varepsilon, \log \varepsilon+C] \times \mathbb{S}^{n-1}$, for some positive constant $C>0$. In fact the general $g_{\varepsilon}$ 's are close enough to the model $\sigma_{k}$-Schwarzschild metric elsewhere and one can reproduce the desired estimate, arguing as in the proof of Lemma 5.1. On the other hand, using the fact that $\mathcal{N}_{g_{1}}(1)=0$, one has that
$$\mathcal{N}_{\bar{g}}\left(u_{\varepsilon}\right)=u_{1}^{\frac{2 k n}{n-2 k}}\left\{\mathbb{L}_{g_{1}}(1)\left[e^{\frac{n-2 k}{k} t}\right]+\mathcal{Q}_{g_{1}}(1)\left(e^{\frac{n-2 k}{k} t}\right)\right\} \simeq \varepsilon^{\frac{n-2 k}{k}} \quad \text { in }[\log \varepsilon, \log \varepsilon+C] \times \mathbb{S}^{n-1} \text {. }$$
Thus the estimates of the proper error as well are not affected by the removal of Assumption 3.1, and we can definitely drop it out. This concludes the proof of Theorem 1.

\section*{6 Obstructions to the connected sum for $2 k \geq n$}

We present now briefly two counterexamples to the possibility to extend Theorem 1 in the case where $2 k \geq n$.

Counterexample 1: $n=3, k=2$. Let $\left(M_{i}, g_{i}\right)=\left(\mathbb{R P}^{3}, g_{s t d}\right), i=1,2$, where $g_{s t d}$ is the standard metric on $\mathbb{R P}^{3}$, i.e., the one who lifts to the round metric of $\mathbb{S}^{3}$. Clearly we have that $g_{\text {std }} \in \Gamma_{2}^{+}$and has positive constant $\sigma_{2}$-curvature equal to 3/4. Moreover $\left(\mathbb{R P}^{3}, g_{\text {std }}\right)$ is non degenerate. In fact, if $w$ is a function defined on $\mathbb{R P}^{3}$ which verifies
$$\mathbb{L}_{g_{s t d}}(1)[w]=0 \quad \text { in } \mathbb{R} \mathbb{P}^{3}$$
then it lifts to a function $\widetilde{w}$ defined on the universal cover $\mathbb{S}^{3}$ such that $\widetilde{w}(p)=\widetilde{w}(-p)$ for every $p \in \mathbb{S}^{3}$ and
$$\left(\Delta_{\mathbb{S}^{3}}+3\right) \widetilde{w}=0 \quad \text { in } \mathbb{S}^{3} .$$
This clearly implies $\widetilde{w} \equiv 0$, since the solutions to this equation are linear combinations of the restriction to $\mathbb{S}^{3}$ of the coordinate functions of $\mathbb{R}^{4}$. Hence, $w \equiv 0$. At this point all the hypothesis of Theorem 1 are in force, with the only exception of the inequality $2 k<n$. On the other hand the connected sum $\mathbb{R}^{3} \sharp \mathbb{R} \mathbb{P}^{3}$ cannot be endowed with a 2-admissible metric. In fact such a metric would have positive Ricci curvature, as shown in [9], and this would contradict for instance Hamilton's theorem for 3-manifolds [13].

Counterexample 2: $n=4, k=2$. Let $\left(M_{i}, g_{i}\right)=\left(\mathbb{R P}^{4}, g_{\text {std }}\right), i=1,2$, where $g_{\text {std }}$ is the standard metric on $\mathbb{R P}^{4}$ as above. Clearly we have that $g_{\text {std }} \in \Gamma_{2}^{+}$and has positive constant $\sigma_{2}$-curvature equal to 3/2. The same argument as in Counterexample 1 shows that $\left(\mathbb{R P}^{4}, g_{\text {std }}\right)$ is non degenerate. If the Theorem 1 would apply to this situation, we would end up with a locally conformally flat 2 -admissible metric $\widetilde{g}$ on the connected sum $M^{4}:=\mathbb{R P}^{4} \sharp \mathbb{R} \mathbb{P}^{4}$, since the locally conformally flatness is clearly preserved by
both the explicit construction of the approximate solutions and the conformal perturbation that we use to get the exact solutions. On the other hand a conformally flat 2-admissible metric on a 4-manifold has positive scalar curvature and fulfills the pinching conditions
$$2\left|\operatorname{Ric}_{\widetilde{g}}\right|<(1 / 6) R_{\widetilde{g}}^{2} .$$
The Margerin's result [19] implies now that $M^{4}$ is diffeomorphic to either $\mathbb{S}^{4}$ or $\mathbb{R} \mathbb{P}^{4}$.

\section*{References}
\begin{itemize}
\item[] [1] T. Aubin, Equations différentielles non linéaires et probléme de Yamabe concernant la corbure scalaire, J. Math. Pures Appl. 55 (1976), 269-296.
\item[] [2] T. Branson and A. R. Gover, Variational status of a class of fully nonlinear curvature prescription problems, Calc. Var. Part. Diff. Eq. 32 (2008), 253-262.
\item[] [3] G. Catino and L. Mazzieri Dipole type metrics with constant $\sigma_{k}$-curvature, in preparation.
\item[] [4] S.-Y. A. Chang, M. J. Gursky and P. C. Yang, An equation of Monge-Ampère type in conformal geometry and four-manifolds of positive Ricci curvature, Ann. of Math. 155 (2002), 709-787.
\item[] [5] S.-Y. A. Chang, M. J. Gursky and P. C. Yang, An a priori estimate for a fully nonlinear equation on four-manifolds, J. Anal. Math. 87 (2002), 151-186.
\item[] [6] D. Gilbarg and N. Trudinger, Elliptic Partial Differential Equation of Second Order, Springer, 1983.
\item[] [7] M. Gromov and H. B. Lawson, The classification of simply connected manifolds of positive scalar curvature, Ann. of Math. 111 (1980), 423-434.
\item[] [8] P. Guan, C. S. Lin and G. Wang, Schouten tensor and some topological properties, Comm. Anal. Geom. 13 (2005), 887-902.
\item[] [9] P. Guan, J. Viaclovsky and G. Wang, Some properties of the Schouten tensor and applications to conformal geometry, Trans. Amer. Math. Soc. 355 (2003), 925-933.
\item[] [10] P. Guan and G. Wang, A fully nonlinear conformal flow on locally conformally flat manifolds, J. Reine Angew. Math. 557 (2003), 219-238.
\item[] [11] M. J. Gursky and J. Viaclovsky, Fully nonlinear equations on Riemannian manifolds with negative curvature, Indiana Univ. Math. J. 52 (2003), 399-420.
\item[] [12] M. Gursky and J. Viaclovsky, Prescribing symmetric functions of the eigenvalues of the Ricci tensor, Ann. Math. 166 (2007), 475-531.
\item[] [13] R. S. Hamilton, Three-manifolds with positive Ricci curvature, J. Diff. Geom. 17 (1982), 255-306.
\item[] [14] D. Joyce, Constant scalar curvature metrics on connected sums, Int. J. Math. Math. Sci. 7 (2003), 405-450.
\item[] [15] N. Kapouleas, Complete constant mean curvature surfaces in Euclidean three-space, Ann. of Math. 131 (1990), 239-330.
\item[] [16] N. Kapouleas, Compact constant mean curvature surfaces in Euclidean three-space, J. Diff. Geom. 33 (1991), 683-715.
\item[] [17] J. M. Lee and T. H. Parker, The Yamabe Problem, Bull. Amer. Math. Soc. 17 (1987), 37-91.
\end{itemize}
\begin{itemize}
\item[] [18] A. Li and Y. Y. Li, On some conformally invariant fully nonlinear equations, Comm. Pure Appl. Math. 56 (2003), 1416-1464.
\item[] [19] C. Margerin, Pointwise pinched manifolds are space forms, A. M. S. Proc. of Symp. in Pure Math. 44 (1986), 307-328.
\item[] [20] R. Mazzeo and F. Pacard, Constant scalar curvature metrics with isolated singularities, Duke Math. J. 99 (1999), 353-418.
\item[] [21] R. Mazzeo, D. Pollack and K. Uhlenbeck, Connected sums constructions for constant scalar curvature metrics, Topol. Method in Nonlinear Anal. 6 (1995), 207-233.
\item[] [22] L. Mazzieri, Generalized connected sum construction for nonzero constant scalar curvature metrics, Comm. in Part. Diff. Eq. 33 (2008), 1-17.
\item[] [23] L. Mazzieri, Generalized connected sum construction for scalar flat metrics, Manuscripta Math. 129 (2009), 137-168.
\item[] [24] L. Mazzieri and C. B. Ndiaye, Existence of solutions for the singular $\sigma_{k}$-Yamabe problem, preprint.
\item[] [25] F. Pacard, Connected sum constructions in geometry and nonlinear analysis, http://perso-math.univ-mlv.fr/users/pacard.frank/pacard\%20\%28prepublications\%29.html.
\item[] [26] R. M. Schoen, Conformal deformation of a Riemannian metric to constant scalar curvature, J. Diff. Geom. 20 (1984), 479-495.
\item[] [27] R. M. Schoen, The existence of weak solutions with prescribed singular behavior for a conformally invariant scalar equation, Comm. Pure Appl. Math., 41 (1988), 317-392.
\item[] [28] R. M. Schoen and S. T. Yau, On the structure of manifolds with positive scalar curvature, Manuscripta Math. 28 (1979), 159-183.
\item[] [29] W.-M. Sheng, N. S. Trudinger and X.-J. Wang, The Yamabe problem for higher order curvatures, J. Diff. Geom. 77 (2007), 515-553.
\item[] [30] N.S. Trudinger, Remarks concerning the conformal deformation of Riemannian structures on compact manifolds, Ann. Scuola Norm. Sup. Pisa 22 (1968), 265-274.
\item[] [31] H. Yamabe, On a deformation of Riemannian structures on compact manifolds, Osaka Math. J. 12 (1960), 21-37.
\end{itemize}