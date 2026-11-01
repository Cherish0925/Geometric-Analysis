---
retention_scope: session
part: 3
total_parts: 5
---

[Part 3/5 of: Schauder estimates for equations with cone metrics, II]

In particular, at $q \in \frac{1}{3} \hat{B}_{\ell}(p)$,
$$L_{3}=\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right|=\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}(q)\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
Case 2: $k_{1, p} \geq \ell \geq k_{2, p}$. Here the ball $\hat{B}_{\ell}(p)$ is equal to $B_{\beta}\left(p_{1}, 2 \tau^{\ell}\right)$, the function $U$ defined in (3-55) is $g_{\beta}$-harmonic and well defined in a ball
$$B_{q}:=B_{\beta}\left(q, \frac{1}{10} \tau^{\ell}\right) \subset \frac{1}{2.2} \hat{B}_{\ell}(p),$$
and $\sup _{\hat{B}_{\ell}(p) / 2}|U| \leq C \omega^{2 \ell} \omega\left(\tau^{\ell}\right)$. Since $\frac{1}{2} \hat{B}_{\ell}(p)$ is disjoint from $\mathcal{S}_{2}$, we have that $w_{2}$ is well defined on $\frac{1}{2.2} \hat{B}_{\ell}(p)$, and thus we have the derivatives estimates
$$\sup _{B_{q} / 2}\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}\right| \leq \sup _{B_{q} / 2}\left|\frac{\partial}{\partial r_{1}} D_{w_{2}} U\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
In particular, at $q \in \frac{1}{2} B_{q}$, we have
$$L_{3}=\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right|=\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}(q)\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
Case 3: $\ell \leq k_{2, p}-1$. Here $r_{2}(p) \approx \tau^{k_{2, p}} \leq \tau^{\ell+1}<8 d$, so
$$r_{2}(q) \leq r_{2}(p)+d \leq \frac{5}{8} \tau^{\ell} \quad \text { and } \quad r_{1}(q) \leq d+r_{1}(p) \leq d+r_{2}(p) \leq \frac{5}{8} \tau^{\ell} .$$
Therefore the ball $\widetilde{B}_{\ell}(q)$ is centered at either $q_{1}, q_{2}$ or $q_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$, with radius $2 \tau^{\ell}$. It follows that the function $U$ defined in (3-55) is well defined on the ball $\frac{1}{1.8} \hat{B}_{\ell}(p)$.

By the same strategy as in the proof of Lemma 3.19, with the harmonic function $D^{\prime} h_{k}$ in that lemma replaced by $U$ on the metric ball $\frac{1}{1.8} \hat{B}_{\ell}(p)$, we can prove that, for any $z \in \frac{1}{2} \hat{B}_{\ell}(p) \backslash \mathcal{S}$,
$$\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}(z)\right| \leq C(n, \boldsymbol{\beta}) r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-\ell\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{\ell}\right) .$$
Applying this inequality at $q$, we get
$$L_{3}=\left|\frac{\partial^{2}\left(u_{\ell}-v_{\ell}\right)}{\partial r_{1} \partial r_{2}}(q)\right| \leq C(n, \boldsymbol{\beta}) r_{1}(q)^{1 / \beta_{1}-1} r_{2}(q)^{1 / \beta_{2}-1} \tau^{-\ell\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{\ell}\right) \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
In sum, in all cases $L_{3} \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right)$. \(\square\)

Lemma 3.24. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that, for all $k \leq \ell$ and $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
\left|\frac{\partial}{\partial \theta_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)(z)\right| & +\left|\left(\frac{\partial^{3} h_{k}}{r_{1} \partial \theta_{1}^{2} \partial r_{2}}\right)\right| \\
& \leq C \cdot \begin{cases}r_{1}^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$

Proof. The proof is parallel to that of Lemma 3.19. The function $\partial h_{k} / \partial \theta_{1}$ is $g_{\beta}$-harmonic on $\hat{B}_{k}(p)$, and by the Laplacian estimates (3-9), we have
$$\sup _{\hat{B}_{k}(p) / 1.2}\left(\left|\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{1}}\right|+\left|\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|\right) \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{k}\right) .$$
The function $\Delta_{2}\left(\partial h_{k} / \partial \theta_{1}\right)$ is also $g_{\beta}$-harmonic, so the Laplacian estimates (3-9) imply
$$\sup _{\hat{B}_{k}(p) / 1.4}\left(\left|\Delta_{1} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|+\left|\Delta_{2} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|+\left|\left(D^{\prime}\right)^{2} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|\right) \leq C \tau^{-2 k}\left(\operatorname{osc}_{\hat{B}_{k}(p) / 1.2} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right) \leq C \tau^{-2 k} \omega\left(\tau^{k}\right) .$$
We consider
$$\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)=-\Delta_{1} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}=: F_{5},$$
where the function $F_{5}$ satisfies $\sup _{\hat{B}_{k}(p) / 1.4}\left|F_{5}\right| \leq C \tau^{-2 k} \omega\left(\tau^{k}\right)$.
Case 1: $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right)$. Here we introduce the smooth coordinate $w_{2}=z_{2}^{\beta_{2}}$ in the ball $\frac{1}{1.5} \hat{B}_{k}(p)$ as before. Since this ball is disjoint from $\mathcal{S}_{2}$, under the coordinates $\left(r_{1}, \theta_{1} ; w_{2}, z_{3}, \ldots, z_{n}\right)$ we can use the usual standard gradient estimate to the $g \boldsymbol{\beta}$-harmonic function $\Delta_{2}\left(\partial h_{k} / \partial \theta_{1}\right)$ to obtain
$$\sup _{\hat{B}_{k}(p) / 2}\left|\frac{\partial}{\partial r_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$

Case 2: $k \leq k_{2, p}$. Here the ball $\hat{B}_{k}(p)$ is centered at $p_{1,2}$. We apply the usual estimate (2-3) to the function $\Delta_{2}\left(\partial h_{k} / \partial \theta_{1}\right)$, the solution to (3-94), on any $\mathbb{C}$-ball $A_{2}:=B_{\mathbb{C}}\left(y,\left(\tau^{k}\right)^{1 / \beta_{2}}\right)$ for any $y \in \mathcal{S}_{2} \cap \frac{1}{1.6} \hat{B}_{k}(p)$, where $A_{2}$ denotes the Euclidean ball in the complex plane orthogonal to $\mathcal{S}_{2}$ and passing through $y$. Then, for any $z \in B_{\mathbb{C}}\left(y,\left(\tau^{k}\right)^{1 / \beta_{2}} / 2\right) \backslash\{y\}$,
$$\left|\frac{\partial}{\partial z_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)(z)\right| \leq C \frac{\left\|\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right\|_{L^{\infty}\left(A_{2}\right)}}{\tau^{k / \beta_{2}}}+C\left\|F_{5}\right\|_{L^{\infty}\left(A_{2}\right)}\left(\tau^{k}\right)^{2-1 / \beta_{2}} \leq C \tau^{-k / \beta_{2}} \omega\left(\tau^{k}\right) .$$
This implies that, on $\frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\left|\frac{\partial}{\partial r_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right| \leq C r_{2}^{1 / \beta_{2}-1} \tau^{-k / \beta_{2}} \omega\left(\tau^{k}\right) .$$

Taking $\partial / \partial r_{2}$ on both sides of $\Delta_{\beta}\left(\partial h_{k} / \partial \theta_{1}\right)=0$, we get
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right)=-\frac{\partial}{\partial r_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}}=: F_{6} .$$
It is not hard to see from (3-95), (3-96) and standard derivatives estimates that, on $\frac{1}{1.8} \hat{B}_{k}(p) \backslash \mathcal{S}$,
\begin{itemize}
\item[-] in Case 1 when $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right)$, we have $\left|F_{6}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right)$,
\item[-] in Case 2 when $k \leq k_{2, p}$, we have $\left|F_{6}\right| \leq C r_{2}^{1 / \beta_{2}-1} \tau^{-k / \beta_{2}} \omega\left(\tau^{k}\right)$.
\end{itemize}

Then by applying estimate (2-3) to the function $\partial^{2} h_{k} / \partial r_{2} \partial \theta_{1}$ on any $\mathbb{C}$-ball $A_{3}:=B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}}\right)$ for any $x \in \frac{1}{1.8} \hat{B}_{k}(p) \cap \mathcal{S}_{1}$, we get that, on $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$,
$$\begin{aligned}
\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right)\right|+\left\lvert\, \frac{\partial}{r_{1} \partial \theta_{1}}\right. & \left.\left(\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right) \right\rvert\, \\
& \leq C r_{1}^{1 / \beta_{1}-1} \frac{\left\|\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right\|_{L^{\infty}\left(A_{3}\right)}}{\tau^{k / \beta_{1}}}+C r_{1}^{1 / \beta_{1}-1}\left\|F_{6}\right\|_{L^{\infty}\left(A_{3}\right)} \tau^{k\left(2-1 / \beta_{1}\right)} \\
& \leq C \cdot \begin{cases}r_{1}^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$
Therefore this estimate holds on $\frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$. \(\square\)

Lemma 3.25. For any $k \leq \ell$ and any point $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
& \left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(z)\right| \leq C \cdot \begin{cases}r_{1}^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) & \text { if } k \leq k_{2, p} .\end{cases} \\
& \left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1} \partial r_{2}}(z)\right| \leq C \cdot \begin{cases}r_{1}^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right) & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-k\left(-1+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$
Proof. This follows from almost the same argument as in the proof of Lemma 3.24, by studying the harmonic functions $h_{k}$ and $D^{\prime} h_{k}$ instead of $\partial h_{k} / \partial \theta_{1}$. \(\square\)

Lemma 3.26. For any $k \leq \ell$ and any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
& \left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|(z) \\
& \leq C \omega\left(\tau^{k}\right) \cdot \begin{cases}\tau^{-k}+r_{1}(z)^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)} & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{2}(z)^{1 / \beta_{2}-1} \tau^{-k / \beta_{2}}+r_{1}(z)^{1 / \beta_{1}-2} r_{2}(z)^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$
Proof. By the Laplacian estimates (3-9) we have
$$\sup _{\left(\hat{B}_{k}(p) / 1.2\right) \backslash \mathcal{S}}\left|\Delta_{1} h_{k}\right|+\left|\Delta_{2} h_{k}\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{k}\right) .$$
Applying again the Laplacian estimates (3-9) to the $g_{\beta}$-harmonic function $\Delta_{1} h_{k}$, we have
$$\sup _{\hat{B}_{k}(p) / 1.4}\left(\left|\Delta_{1} \Delta_{1} h_{k}\right|+\left|\Delta_{2} \Delta_{1} h_{k}\right|+\left|\left(D^{\prime}\right)^{2} \Delta_{1} h_{k}\right|\right) \leq C(n) \tau^{-2 k} \omega\left(\tau^{k}\right) .$$
We consider the equation
$$\left|z_{2}\right|^{2-2 \beta_{2}} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}} \Delta_{1} h_{k}=-\Delta_{1} \Delta_{1} h_{k}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}} \Delta_{1} h_{k}=: F_{7} .$$
From the estimates above, $\left\|F_{7}\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 1.8\right)} \leq C \tau^{-2 k} \omega\left(\tau^{k}\right)$.

Case 1: $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right)$. Here we directly apply the gradient estimate to $\Delta_{1} h_{k}$ to get
$$\sup _{\left(\hat{B}_{k}(p) / 1.5\right) \backslash \mathcal{S}}\left|\frac{\partial}{\partial r_{2}} \Delta_{1} h_{k}\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}} \Delta_{1} h_{k}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
Case 2: $k \leq k_{2, p}$. Here the balls $\hat{B}_{k}(p)$ are centered at $p_{1,2}$, and we can apply the usual $\mathbb{C}$-ball type estimate to get that, for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
\left|\frac{\partial}{\partial r_{2}} \Delta_{1} h_{k}\right|(z)+\left|\frac{\partial}{r_{2} \partial \theta_{2}} \Delta_{1} h_{k}\right| & \leq C r_{2}(z)^{1 / \beta_{2}-1} \frac{\left\|\Delta_{1} h_{k}\right\|_{L^{\infty}}}{\tau^{k / \beta_{2}}}+C r_{2}(z)^{1 / \beta_{2}-1}\left\|F_{7}\right\|_{L^{\infty}} \tau^{k\left(2-1 / \beta_{2}\right)} \\
& \leq C r_{2}(z)^{1 / \beta_{2}-1} \tau^{-k / \beta_{2}} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Recall that
$$\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)=\frac{\partial}{\partial r_{2}} \Delta_{1} h_{k}-\frac{1}{r_{1}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}-\frac{1}{\beta_{1}^{2} r_{1}^{2}} \frac{\partial^{3} h_{k}}{\partial \theta_{1}^{2} \partial r_{2}},$$
from which we derive that, for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
& \left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|(z) \\
& \leq C \omega\left(\tau^{k}\right) \begin{cases}\tau^{-k}+r_{1}(z)^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)} & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{2}(z)^{1 / \beta_{2}-1} \tau^{-k / \beta_{2}}+r_{1}(z)^{1 / \beta_{1}-2} r_{2}(z)^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$ \(\square\)

Lemma 3.27. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that, for all $k \leq \ell$ and $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
\left|\frac{\partial}{\partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)(z)\right| & +\left|\left(\frac{\partial^{3} h_{k}}{r_{2} \partial \theta_{2}^{2} \partial r_{1}}\right)(z)\right| \\
& \leq C \omega\left(\tau^{k}\right) \begin{cases}r_{1}^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$
Proof. It follows from the Laplacian estimates (3-9) that
$$\sup _{\hat{B}_{k}(p) / 1.2}\left(\left|\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|+\left|\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{2}}\right|\right) \leq C(n) \omega\left(\tau^{k}\right) .$$
Again by (3-9), we have
$$\sup _{\hat{B}_{k}(p) / 1.4}\left(\left|\Delta_{1} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|+\left|\Delta_{2} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|+\left|\left(D^{\prime}\right)^{2} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|\right) \leq C \tau^{-2 k} \omega\left(\omega^{k}\right) .$$
We look at the equation
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}}\left(\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right)=-\Delta_{2} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}}\left(\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right)=: F_{8}$$
and note that
$$\sup _{\hat{B}_{k}(p) / 1.4}\left|F_{8}\right| \leq C \tau^{-2 k} \omega\left(\tau^{k}\right) .$$

As we did before, by estimate (2-3) it follows that, for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$ (remember here $k \leq \min \left(\ell, k_{p}\right)$ ),
$$\begin{aligned}
\left|\frac{\partial}{\partial r_{1}} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|(z)+\left|\frac{\partial}{r_{1} \partial \theta_{1}} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|(z) & \leq C r_{1}(z)^{1 / \beta_{1}-1} \frac{\left\|\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right\|_{L^{\infty}}}{\tau^{k / \beta_{1}}}+C r_{1}(z)^{1 / \beta_{1}-1}\left\|F_{8}\right\|_{L^{\infty}} \tau^{k\left(2-1 / \beta_{1}\right)} \\
& \leq C r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right) .
\end{aligned}$$
Taking $\partial / \partial r_{1}$ on both sides of the equation $\Delta_{\beta}\left(\partial h_{k} / \partial \theta_{2}\right)=0$, we get
$$\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)=-\frac{\partial}{\partial r_{1}}\left(\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right)-\sum_{j} \frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2}}{\partial s_{j}^{2}} \frac{\partial h_{k}}{\partial \theta_{2}}\right)=: F_{9} .$$
Here $\left|F_{9}(z)\right| \leq C r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right)$ for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$. Therefore, by the usual $\mathbb{C}$-ball argument,
\begin{itemize}
\item[-] when $k \leq k_{2, p}$, for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$, we have
\end{itemize}
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right| \leq C r_{2}(z)^{1 / \beta_{2}-1} r_{1}(z)^{1 / \beta_{1}-1} \tau^{k\left(2-1 / \beta_{1}-1 / \beta_{2}\right)} \omega\left(\tau^{k}\right),$$
- when $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right)$, we have
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right| \leq C r_{1}(z)^{1 / \beta_{1}-1} \tau^{k\left(1-1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) .$$ \(\square\)

Lemma 3.28. For any $k \leq \ell$ and any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\begin{aligned}
& \left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)(z)\right| \\
& \leq C \omega\left(\tau^{k}\right) \begin{cases}r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}}+r_{1}^{1 / \beta_{1}-1} r_{2}^{-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}}+r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-2} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$
Proof. We first observe that
$$\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)=\frac{\partial}{\partial r_{1}} \Delta_{2} h_{k}-\frac{1}{r_{2}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}-\frac{1}{\beta_{2}^{2} r_{2}^{2}} \frac{\partial^{2}}{\partial \theta_{2}^{2}}\left(\frac{\partial h_{k}}{\partial r_{1}}\right) .$$
It can be shown by the $\mathbb{C}$-ball argument that, for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\left|\frac{\partial}{\partial r_{1}} \Delta_{2} h_{k}(z)\right| \leq C r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right) .$$
From Lemma 3.25, we have, for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\left|\frac{1}{r_{2}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(z)\right| \leq C \cdot \begin{cases}r_{1}^{1 / \beta_{1}-1} r_{2}^{-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} \omega\left(\tau^{k}\right) & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\ r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-2} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \omega\left(\tau^{k}\right) & \text { if } k \leq k_{2, p} .\end{cases}$$
From Lemma 3.27, we have, for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$,
$$\left|\frac{1}{r_{2}^{2}} \frac{\partial^{3} h_{k}}{\partial r_{1} \partial \theta_{2}^{2}}(z)\right| \leq C \omega\left(\tau^{k}\right) \cdot \begin{cases}r_{1}^{1 / \beta_{1}-1} r_{2}^{-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\ r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-2} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} & \text { if } k \leq k_{2, p} .\end{cases}$$

Therefore, for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$, we have
$$\begin{aligned}
& \left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)(z)\right| \\
& \quad \leq C \omega\left(\tau^{k}\right) \cdot \begin{cases}r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}}+r_{1}^{1 / \beta_{1}-1} r_{2}^{-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} & \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right], \\
r_{1}(z)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}}+r_{1}^{1 / \beta_{1}-1} r_{2}^{1 / \beta_{2}-2} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} & \text { if } k \leq k_{2, p} .\end{cases}
\end{aligned}$$ \(\square\)

It remains to estimate $L_{2}$. For simplicity, we write $h_{k}:=-u_{k}+u_{k-1}$ as before, where we take $k \leq \ell$. We will define $\beta_{\max }=\max \left(\beta_{1}, \beta_{2}\right)$.

Lemma 3.29. Let $d=d_{\boldsymbol{\beta}}(p, q)$. There exists a constant $C(n, \boldsymbol{\beta})>0$ such that, for all $k \leq \ell$,
$$\begin{aligned}
\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| & \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(1 / \beta_{1}-1\right)} d^{1 / \beta_{1}-1} \\
& \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(1 / \beta_{\max }-1\right)} d^{1 / \beta_{\max }-1} .
\end{aligned}$$
Proof. Case 1: First we assume that $r_{p} \leq 2 d$, so that $r_{q} \leq 3 d$ and $\ell+2 \leq k_{p}$. In particular, the balls $\hat{B}_{k}(p)$ are centered at either $p_{1} \in \mathcal{S}_{1}$ or 0, depending on whether $k \geq k_{2, p}+1$ or $k \leq k_{2, p}$. As in the proof of Lemma 3.20, let $\gamma:[0, d] \rightarrow B_{\beta}(0,1) \backslash S$ be the $g_{\beta}$-geodesic connecting $p$ and $q$, let the two points $q^{\prime}$ and $p^{\prime}$ be defined as in (3-80), and let $\gamma_{1}, \gamma_{2}, \gamma_{3}$ be the $g_{\boldsymbol{\beta}}$-geodesics defined in that lemma. By the triangle inequality we calculate
$$\begin{aligned}
& \left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \\
& \quad \leq\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(p^{\prime}\right)\right|+\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(p^{\prime}\right)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(q^{\prime}\right)\right|+\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(q^{\prime}\right)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right|=: L_{1}^{\prime}+L_{2}^{\prime}+L_{3}^{\prime} .
\end{aligned}$$
Integrating along $\gamma_{3}$, where the coordinates $\left(r_{1} ; r_{2}, \theta_{2} ; z_{3}, \ldots, z_{n}\right)$ are the same as $p$, we get (by (3-93))
$$L_{1}^{\prime}=\left|\int_{\gamma_{3}} \frac{\partial}{\partial \theta_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d \theta_{1}\right| \leq C \omega\left(\tau^{k}\right) \cdot \begin{cases}r_{1}(p)^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} & \text { if } k \in\left[k_{2, p}+1, \ell\right], \\ r_{1}(p)^{1 / \beta_{1}-1} r_{2}(p)^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} & \text { if } k \leq k_{2, p} .\end{cases}$$
Integrating along $\gamma_{2}$, where the coordinates $\left(\theta_{1} ; r_{2}, \theta_{2} ; z_{3}, \ldots, z_{n}\right)$ are the same as $p^{\prime}$ or $q^{\prime}$, we get by the estimate in Lemma 3.26 that
$$\begin{aligned}
& L_{2}^{\prime}=\left|\int_{\gamma_{2}} \frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d r_{1}\right| \\
& \leq C \omega\left(\tau^{k}\right) \cdot\left\{\begin{array}{cl}
\tau^{-k} d+\tau^{-k\left(1 / \beta_{1}-1\right)}\left|r_{1}(p)-r_{1}(q)\right|^{1 / \beta_{1}-1} & \text { if } k \in\left[k_{2, p}+1, \ell\right], \\
r_{2}(p)^{1 / \beta_{2}-1} \tau^{-k / \beta_{2}} d & \text { if } k \leq k_{2, p} \\
+r_{2}(p)^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)}\left|r_{1}(p)-r_{1}(q)\right|^{1 / \beta_{1}-1} & \text { if } k \in\left[k_{2, p}+1, \ell\right],
\end{array}\right. \\
& \leq C \omega\left(\tau^{k}\right) \cdot \begin{cases}\tau^{-k} d+\tau^{-k\left(1 / \beta_{1}-1\right)} d^{1 / \beta_{1}-1} & \text { if } k \leq k_{2, p} .\end{cases} \\
& r_{2}(p)^{1 / \beta_{2}-1} \tau^{-k / \beta_{2}} d+r_{2}(p)^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} d^{1 / \beta_{1}-1}
\end{aligned}$$
To deal with the term $L_{3}^{\prime}$, we consider two cases for $k: \ell \geq k \geq k_{2, p}+1$ and $k \leq k_{2, p}$.

Case 1a: $k_{2, p}+1 \leq k \leq \ell$. In this case the balls $\hat{B}_{k}(p)$ are centered at $p_{1} \in \mathcal{S}_{1}$. Here $\tau^{-k} \leq \tau^{-\ell} \leq 8^{-1} d^{-1}$ and $\tau^{k} \leq \tau^{k_{2, p}+1} \leq \frac{1}{2} r_{2}(p)$, so $r_{2}(q) \geq-d+r_{2}(p) \geq \tau^{k}$. The balls $\hat{B}_{k}(p)$ are disjoint from $\mathcal{S}_{2}$, and we can use the smooth coordinate $w_{2}=z_{2}^{\beta_{2}}$ as before. The functions $D_{w_{2}} D^{\prime} h_{k}$ are $g_{\beta}$-harmonic; hence by the gradient estimate we have
$$\sup _{\left(\hat{B}_{k}(p) / 1.2\right) \backslash \mathcal{S}_{1}}\left|\nabla_{g_{\beta}}\left(D_{w_{2}} D^{\prime} h_{k}\right)\right| \leq C(n) \frac{\left\|D_{w_{2}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\hat{B}_{k}(p) / 1.1\right)}}{\tau^{k}} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
From (3-88), we get
$$\sup _{\left(\hat{B}_{k}(p) / 1.2\right) \backslash \mathcal{S}_{1}}\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}} D^{\prime} h_{k}\right| \leq C(n) \tau^{-k} \omega\left(\tau^{k}\right) .$$
Recalling that $r_{1}(p)=r_{p} \leq 2 d \leq \frac{1}{2} \tau^{k}$, the triangle inequality implies $r_{1}(q) \leq 3 d \leq \frac{1}{2} \tau^{k}$. The points in $\gamma_{1}$ have fixed ( $r_{1}, \theta_{1}$ )-coordinates ( $r_{1}(q), \theta_{1}(q)$ ), so integrating along $\gamma_{1}$ we get (by (3-104) and (3-105))
$$\begin{aligned}
L_{3}^{\prime} & \leq \int_{\gamma_{1}}\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|+\left|D^{\prime}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \\
& \leq C d \omega\left(\tau^{k}\right)\left(r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}}+\tau_{1}(q)^{1 / \beta_{1}-1} \min \left(r_{2}(p), r_{2}(q)\right)^{-1} \tau^{-k\left(1 / \beta_{1}-1\right)}+\tau^{-k}\right) \\
& \leq C \tau^{-k} \omega\left(\tau^{k}\right) \cdot d \leq C \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} .
\end{aligned}$$
Case 1b: $k \leq k_{2, p}$. In this case $\tau^{k} \geq \tau^{k_{2, p}} \geq r_{2}(p)$ and $\tau^{k} \geq \tau^{\ell} \geq 8 d$. Thus $r_{2}(q) \leq r_{2}(p)+d \leq \frac{3}{2} \tau^{k}$. We choose points $\tilde{q}$ and $\hat{q}$ as in (3-84), and let $\tilde{\gamma}_{1}, \tilde{\gamma}$ and $\hat{\gamma}$ be $g_{\beta}$-geodesics defined as in the proof of Lemma 3.20. Then we have
$$L_{3}^{\prime} \leq\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(q^{\prime}\right)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\tilde{q})\right|+\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\tilde{q})-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\hat{q})\right|+\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\hat{q})-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right|=: L_{1}^{\prime \prime}+L_{2}^{\prime \prime}+L_{3}^{\prime \prime} .$$
We will estimate $L_{1}^{\prime \prime}, L_{2}^{\prime \prime}$ and $L_{3}^{\prime \prime}$ term by term by integrating appropriate functions along the geodesics $\tilde{\gamma}_{1}$, $\tilde{\gamma}$ and $\hat{\gamma}$ as follows: The points in $\hat{\gamma}$ have fixed ( $r_{1}, \theta_{1} ; r_{2} ; s$ )-coordinates ( $r_{1}(q), \theta_{1}(q) ; r_{2}(q) ; s(q)$ ), so (by (3-102))
$$\begin{aligned}
L_{3}^{\prime \prime}=\left|\int_{\hat{\gamma}} \frac{\partial}{\partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d \theta_{2}\right| & \leq C \omega\left(\tau^{k}\right) r_{1}(q)^{1 / \beta_{1}-1} r_{2}(q)^{1 / \beta_{2}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} \\
& \leq C \omega\left(\tau^{k}\right) r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} \leq C \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} .
\end{aligned}$$
Integrating along $\tilde{\gamma}$, where the points have constant $r_{1}$-coordinate $r_{1}(q)$, we get (by (3-104))
$$\begin{aligned}
L_{2}^{\prime \prime} & =\left|\int_{\tilde{\gamma}} \frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d r_{2}\right| \\
& \leq C \omega\left(\tau^{k}\right)\left(r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}}\left|r_{2}(q)-r_{2}(p)\right|\right. \\
& \left.\quad+r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)}\left|r_{2}(q)^{1 / \beta_{2}-1}-r_{2}(p)^{1 / \beta_{2}-1}\right|\right) \\
& \leq C \omega\left(\tau^{k}\right)\left(r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k / \beta_{1}} d+r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k\left(-2+1 / \beta_{1}+1 / \beta_{2}\right)} d^{1 / \beta_{2}-1}\right) \\
& \leq C \omega\left(\tau^{k}\right) r_{1}(q)^{1 / \beta_{1}-1} \tau^{-k\left(-1+1 / \beta_{1}\right)} \\
& \leq C \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} .
\end{aligned}$$

Integrating along $\tilde{\gamma}_{1}$, where the points have constant $\left(r_{1}, \theta_{1} ; r_{2}, \theta_{2}\right)$-coordinates, we have (by (3-71))
$$\begin{aligned}
L_{1}^{\prime \prime} \leq \int_{\tilde{\gamma}_{1}}\left|D^{\prime}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| & \leq C r_{1}(q)^{1 / \beta_{1}-1} r_{2}(p)^{1 / \beta_{2}-1} \tau^{-k\left(-1+1 / \beta_{1}+1 / \beta_{2}\right)} d \\
& \leq C d \tau^{-k} \omega\left(\tau^{k}\right) \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$

Combining both cases, we conclude that
$$L_{3}^{\prime} \leq C \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) d^{1 / \beta_{1}-1} .$$
Then by the estimates above for $L_{1}^{\prime}$ and $L_{2}^{\prime}$, we finally get, for all $k \leq \ell$,
$$\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(1 / \beta_{1}-1\right)} d^{1 / \beta_{1}-1} \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(1 / \beta_{\max }-1\right)} d^{1 / \beta_{\max }-1},$$
where in the last inequality we use the fact that $\tau^{-k} d \leq \frac{1}{8}<1$ when $k \leq \ell$. Hence we finish the proof of Lemma 3.29 in the case $r_{p} \leq 2 d$.

Now we deal with the remaining cases.
Case 2: Here we assume $\min \left(r_{p}, r_{q}\right)=r_{p} \geq 2 d$ and $\ell \leq k_{p}$. In this case $\tau^{k_{p}} \approx r_{p} \geq 2 d \geq \tau^{\ell+3}$, so $\ell+3 \geq k_{p}$. It follows by the triangle inequality that $d_{\boldsymbol{\beta}}(\gamma(t), \mathcal{S}) \geq d$, where $\gamma$ is the $g_{\boldsymbol{\beta}}$-geodesic joining $p$ to $q$ as before. In particular, this implies that $\min \left(r_{1}(\gamma(t)), r_{2}(\gamma(t))\right) \geq d$.

Since $\ell \leq k_{p}$, Lemmas 3.24-3.28 hold for all $k \leq \ell$ and $r_{1}(p) \approx \tau^{k_{p}} \leq \tau^{\ell}$, so
$$r_{1}(\gamma(t)) \leq d+r_{1}(p) \leq \frac{9}{8} \tau^{\ell} \leq \frac{9}{8} \tau^{k} .$$
We calculate the gradient of $\partial^{2} h_{k} / \partial r_{1} \partial r_{2}$ along the geodesic $\gamma$ as
$$\begin{aligned}
\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right|^{2}(\gamma(t))=\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2}+\left|\frac{1}{\beta_{1} r_{1} \partial \theta_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2}+\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2} \\
+\left|\frac{\partial}{\beta_{2} r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2}+\sum_{j}\left|\frac{\partial}{\partial s_{j}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2} .
\end{aligned}$$
Case 2a: $k_{2, p}+1 \leq k \leq \ell$. Here along $\gamma$ we have
$$r_{2}(\gamma(t)) \geq r_{2}(p)-d \geq \tau^{k}-d \geq \frac{7}{8} \tau^{k} .$$
Then by Lemmas 3.24-3.28, along $\gamma$ we have
$$\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\gamma(t))\right| \leq C \omega\left(\tau^{k}\right)\left(\tau^{-k}+d^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)}\right) .$$
Integrating this inequality along $\gamma$ we get
$$\begin{aligned}
\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| & \leq C \omega\left(\tau^{k}\right)\left(d \tau^{-k}+d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)}\right) \\
& \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$

Case 2b: $k \leq k_{2, p}$. Here along $\gamma$ we have
$$r_{2}(\gamma(t)) \leq r_{2}(p)+d \leq \tau^{k}+d \leq \frac{9}{8} \tau^{k} .$$
Then by Lemmas 3.24-3.28, along $\gamma$ we have
$$\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq C \omega\left(\tau^{k}\right)\left(\tau^{-k}+d^{1 / \beta_{1}-2} \tau^{-k\left(1 / \beta_{1}-1\right)}\right) .$$
Integrating this inequality along $\gamma$ we again get
$$\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .$$
Case 3: Here we assume $\min \left(r_{p}, r_{q}\right)=r_{p} \geq 2 d$ but $\ell \geq k_{p}+1$. The case when $k \leq k_{p}$ can be dealt with by the same argument as in Case 2, so we omit it and only consider the case when $k_{p}+1 \leq k \leq \ell$. Here $r_{2}(p) \geq r_{1}(p) \geq \tau^{k} \geq \tau^{\ell}>8 d$, and hence
$$r_{1}(\gamma(t)) \geq \frac{7}{8} \tau^{k} \quad \text { and } \quad r_{2}(\gamma(t)) \geq \frac{7}{8} \tau^{k}$$
for any point $\gamma(t)$ in the geodesic $\gamma$. By the triangle inequality it follows that $\gamma \subset \frac{1}{3} \hat{B}_{k}(p)=B_{\beta}\left(p, \frac{1}{3} \tau^{k}\right)$.
As before, we can introduce smooth coordinates $w_{1}=z_{1}^{\beta_{1}}$ and $w_{2}=z_{2}^{\beta_{2}}$, and $g_{\boldsymbol{\beta}}$ becomes the standard smooth Euclidean metric $g_{\mathbb{C}^{n}}$ under these coordinates. Moreover, $h_{k}$ is the usual Euclidean harmonic function $\Delta_{g_{C} n} h_{k}=0$ on $\hat{B}_{k}(p)$. By the standard derivatives estimates we have
$$\sup _{\hat{B}_{k}(p) / 2}\left(\left|D_{w_{1}, w_{2}}^{3} h_{k}\right|+\left|D^{\prime}\left(D_{w_{1}, w_{2}}^{2}\right) h_{k}\right|\right) \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
From the equation
$$\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}=\frac{w_{1} w_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial w_{1} \partial w_{2}}+\frac{\bar{w}_{1} w_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial \bar{w}_{1} \partial w_{2}}+\frac{w_{1} \bar{w}_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial w_{1} \partial \bar{w}_{2}}+\frac{\bar{w}_{1} \bar{w}_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial \bar{w}_{1} \partial \bar{w}_{2}}$$
we see that, for $i=1,2$,
$$\sup _{\hat{B}_{k}(p) / 2}\left|\frac{\partial}{\partial w_{i}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \leq \frac{C}{r_{i}} \omega\left(\tau^{k}\right)+C \tau^{-k} \omega\left(\tau^{k}\right) \quad \text { and } \quad \sup _{\hat{B}_{k}(p) / 2}\left|D^{\prime}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
From this we see that
$$\sup _{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq \sup _{\gamma}\left(C \tau^{-k} \omega\left(\tau^{k}\right)+\frac{C}{r_{1}} \omega\left(\tau^{k}\right)+\frac{C}{r_{2}} \omega\left(\tau^{k}\right)\right) \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
Integrating along $\gamma$ we get
$$\begin{aligned}
\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| & \leq C d \tau^{-k} \omega\left(\tau^{k}\right) \\
& \leq C d^{1 / \beta_{1}-1} \tau^{-k\left(1 / \beta_{1}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$

Combining the estimates in all three cases, we finish the proof of Lemma 3.29. \(\square\)

By Lemma 3.29,
$$\begin{aligned}
L_{2} & =\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right| \\
& \leq\left|\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(q)\right|+C d^{1 / \beta_{\max }-1} \sum_{k=3}^{\ell} \tau^{-k\left(1 / \beta_{\max }-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
To finish the proof, it suffices to estimate the first term on the right-hand side of the above equation. Recall that we assume $u_{2}$ is a $g_{\beta}$-harmonic function defined on the ball $\hat{B}_{2}(p)$, which is centered at $p_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ and has radius $2 \tau^{2}$. We also know $u_{2}$ satisfies the $L^{\infty}$-estimate by the maximum principle: there exists some $C=C(n)>0$ such that
$$\left\|u_{2}\right\|_{L^{\infty}\left(\hat{B}_{k}(p)\right)} \leq C\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\omega\left(\tau^{2}\right)\right) .$$
Recall that the proofs of the estimates in Lemmas 3.24-3.28 in the case when $k \leq k_{2, p}$ work for any $g_{\beta}$-harmonic functions defined on suitable balls, and we can repeat the arguments there replacing the $L^{\infty}$-estimate of $h_{k}$, namely $\left\|h_{k}\right\|_{L^{\infty}} \leq C \tau^{2 k} \omega\left(\tau^{k}\right)$, by the $L^{\infty}$-estimate of $u_{2}$ given in (3-107) to get similar estimates as in those lemmas. We will omit the details. Given these estimates, we can repeat the proof of Lemma 3.29 to prove the estimates
$$\left|\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(q)\right| \leq C d^{1 / \beta_{\max }-1}\left(\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\omega\left(\tau^{2}\right)\right) .$$
This inequality, combined with (3-106), gives the final estimate of the $L_{2}$ term, that is
$$L_{2} \leq C d^{1 / \beta_{\max }-1}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+C d^{1 / \beta_{\max }-1} \sum_{k=2}^{\ell} \tau^{-k\left(1 / \beta_{\max }-1\right)} \omega\left(\tau^{k}\right) .$$

By Lemmas 3.22 and 3.23 and the estimate (3-108) for $L_{2}$, we are ready to prove the following estimate; see (1-5).

Proposition 3.30. For given $p, q \in B_{\beta}\left(0, \frac{1}{2}\right) \backslash \mathcal{S}$, there is a constant $C=C(n, \boldsymbol{\beta})>0$ such that
$$\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| \leq C\left(d^{1 / \beta_{\max }-1}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{1 / \beta_{\max }-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\max }}} d r\right) .$$
Proof. From Lemmas 3.22 and 3.23 and the estimate (3-108) for $L_{2}$, we have
$$\begin{aligned}
\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| & \leq C\left(d^{1 / \beta_{\max }-1}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+d^{1 / \beta_{\max }-1} \sum_{k=2}^{\ell} \tau^{-k\left(1 / \beta_{\max }-1\right)} \omega\left(\tau^{k}\right)+\sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right)\right) \\
& \leq C\left(d^{1 / \beta_{\max }-1}\|u\|_{L^{\infty}\left(B_{\beta}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{1 / \beta_{\max }-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\max }}} d r\right),
\end{aligned}$$
where the last inequality follows from the fact that $\omega(r)$ is monotonically increasing. \(\square\)

Finally, we remark that the estimates for the other operators in (3-89) follow similarly; we omit the proofs and state that the estimates are the same as the estimates for $\partial^{2} u / \partial r_{1} \partial r_{2}$ in Proposition 3.30.

3E. Nonflat conical Kähler metrics. In this section, we will consider the Schauder estimates for general conical Kähler metrics on $B_{\beta}(0,2) \subset \mathbb{C}^{n}$ with cone angle $2 \pi \beta$ along the simple normal crossing hypersurface $\mathcal{S}$. Let $\omega$ be such a metric. By definition, there exists a constant $C \geq 1$ such that
$$C^{-1} \omega_{\beta} \leq \omega \leq C \omega_{\beta} \quad \text { in } B_{\beta}(0,2) \backslash \mathcal{S},$$
where $\omega_{\beta}$ is the standard flat conical metric as before. Since $\omega$ is closed and $B_{\beta}(0,2)$ is simply connected, we can write $\omega=\sqrt{-1} \partial \bar{\partial} \phi$ for some strictly plurisubharmonic function $\phi$. By elliptic regularity, $\phi$ is Hölder continuous under the Euclidean metric on $B_{\beta}(0,2)$.

We fix $\alpha \in\left(0, \min \left\{1 / \beta_{\text {max }}-1,1\right\}\right)$.
Definition 3.31. We say $\omega=g$ is a $C_{\beta}^{0, \alpha}$ Kähler metric on $B_{\beta}(0,2)$ if it satisfies (3-109) and the Kähler potential $\phi$ of $\omega$ belongs to $C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,2)\right)$.

We are interested in studying the Laplacian equation
$$\Delta_{g} u=f \quad \text { in } B_{\beta}(0,1),$$
where $f \in C_{\beta}^{0, \alpha}\left(\overline{B_{\beta}(0,1)}\right)$ and $u \in C_{\beta}^{2, \alpha}$. We will prove the following scaling-invariant interior Schauder estimates. The proof closely follows that of Theorem 6.6 in [18], so we mainly focus on the differences.

Proposition 3.32. There exists a constant $C=C\left(n, \boldsymbol{\beta},\|g\|_{C_{\boldsymbol{\beta}}^{0, \alpha}}^{*}\right)>0$ such that, if $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)$ satisfies (3-110), then
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}(0,1)\right)}^{*} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}(0,1)\right)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}^{(2)}\right) .$$
Proof. Given any points $x_{0} \neq y_{0} \in B_{\boldsymbol{\beta}}(0,1)$, assume $d_{x_{0}}=\min \left(d_{x_{0}}, d_{y_{0}}\right)$; recall $d_{x}=d_{\boldsymbol{\beta}}\left(x, \partial B_{\boldsymbol{\beta}}(0,1)\right)$. Let $\mu \in\left(0, \frac{1}{4}\right)$ be a small number to be determined later. Write $d=\mu d_{x_{0}}$, and define $B:=B_{\boldsymbol{\beta}}\left(x_{0}, d\right)$ and $\frac{1}{2} B:=B_{\beta}\left(x_{0}, \frac{1}{2} d\right)$.
Case 1: $d_{\beta}\left(x_{0}, y_{0}\right)<\frac{1}{2} d$.
Case 1a: $B_{\boldsymbol{\beta}}\left(x_{0}, d\right) \cap \mathcal{S}=\varnothing$. We introduce smooth complex coordinates $\left\{w_{1}=z_{1}^{\beta_{1}}, w_{2}=z_{2}^{\beta_{2}}, z_{3}, \ldots, z_{n}\right\}$ on $B_{\beta}\left(x_{0}, d\right)$, under which $g_{\beta}$ becomes the Euclidean metric and the components of $g$ become $C^{\alpha}$ in the usual sense. Equation (3-110) has $C^{\alpha}$ leading coefficients, and we can apply Theorem 6.6 in [18] to conclude that (the following inequality is understood in the new coordinates)
$$[u]_{C^{2, \alpha}(B)}^{*} \leq C\left(\|u\|_{C^{0}(B)}+\|f\|_{C^{0, \alpha}(B)}^{(2)}\right) .$$
Recall that $T$ denotes the second-order operators appearing in (2-2). Let $D$ denote the ordinary first-order operators in $\left\{w_{1}, w_{2}, z_{3}, \ldots, z_{n}\right\}$. We calculate
$$\begin{aligned}
\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right| & \leq\left|D^{2} u\left(x_{0}\right)-D^{2} u\left(y_{0}\right)\right|+\frac{d_{\beta}\left(x_{0}, y_{0}\right)}{d}\left(\left|D^{2} u\left(x_{0}\right)\right|+\left|D^{2} u\left(y_{0}\right)\right|\right) \\
& \leq \frac{4 d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}}{d^{2+\alpha}}[u]_{C^{2, \alpha}(B)}^{*}+\frac{4 d_{\beta}\left(x_{0}, y_{0}\right)}{d^{3}}[u]_{C^{2}(B)}^{*} \\
& \leq \frac{8 d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}}{d^{2+\alpha}}[u]_{C^{2, \alpha}(B)}^{*}+C \frac{d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}}{d^{2+\alpha}}\|u\|_{C^{0}(B)} \text { (by the interpolation inequality). }
\end{aligned}$$

Then we get
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}} \leq \frac{C}{\mu^{2+\alpha}}\|f\|_{C_{\beta}^{0, \alpha}(B)}^{(2)}+\frac{C}{\mu^{2+\alpha}}\|u\|_{C^{0}(B)} .$$
Case 1b: $B_{\boldsymbol{\beta}}\left(x_{0}, d\right) \cap \mathcal{S} \neq \varnothing$. Let $\hat{x}_{0} \in \mathcal{S}$ be the nearest possible point $x_{0}$ to $\mathcal{S}$. We consider the ball $\hat{B}:=B_{\beta}\left(\hat{x}_{0}, 2 d\right)$, which is contained in $B_{\beta}(0,1)$ by the triangle inequality. As in [14], we introduce a (nonholomorphic) basis of $T_{1,0}^{*}\left(\mathbb{C}^{n} \backslash \mathcal{S}\right)$
$$\left\{\epsilon_{j}:=d r_{j}+\sqrt{-1} \beta_{j} r_{j} d \theta_{j}, d z_{k}\right\}_{j=1,2 ; k=3, \ldots, n}$$
and the dual basis of $T_{1,0}\left(\mathbb{C}^{n} \backslash \mathcal{S}\right)$
$$\left\{\gamma_{j}:=\frac{\partial}{\partial r_{j}}-\sqrt{-1} \frac{1}{\beta_{j} r_{j}} \frac{\partial}{\partial \theta_{j}}, \frac{\partial}{\partial z_{k}}\right\}_{j=1,2 ; k=3, \ldots, n} .$$
We can write the (1, 1)-form $\omega$ in the basis $\left\{\epsilon_{j} \wedge \bar{\epsilon}_{k}, \epsilon_{j} \wedge d \bar{z}_{k}, d z_{k} \wedge \bar{\epsilon}_{j}, d z_{j} \wedge d \bar{z}_{k}\right\}$ as
$$\omega=g_{\epsilon_{j} \bar{\epsilon}_{k}} \epsilon_{j} \wedge \bar{\epsilon}_{k}+g_{\epsilon_{j} \bar{k}} \epsilon_{j} \wedge d \bar{z}_{k}+g_{k \bar{\epsilon}_{j}} d z_{k} \wedge \bar{\epsilon}_{j}+g_{j \bar{k}} d z_{j} \wedge d \bar{z}_{k},$$
where
$$\begin{array}{ll}
g_{\epsilon_{j} \bar{\epsilon}_{k}}=\sqrt{-1} \partial \bar{\partial} \phi\left(\gamma_{j}, \bar{\gamma}_{k}\right), & g_{\epsilon_{j} \bar{k}}=\sqrt{-1} \partial \bar{\partial} \phi\left(\gamma_{j}, \frac{\partial}{\partial \bar{z}_{k}}\right), \\
g_{k \bar{\epsilon}_{j}}=\sqrt{-1} \partial \bar{\partial} \phi\left(\frac{\partial}{\partial z_{k}}, \bar{\gamma}_{j}\right), & g_{k \bar{j}}=\frac{\partial^{2}}{\partial z_{k} \partial \bar{z}_{j}} \phi .
\end{array}$$
We remark that all the second-order derivatives of $\phi$ appearing in (3-115) are linear combinations of $\left|z_{j}\right|^{2-2 \beta_{j}}\left(\partial^{2} / \partial z_{j} \partial z_{\bar{j}}\right) N_{j} N_{k}(j \neq k), N_{j} D^{\prime}$ and $\left(D^{\prime}\right)^{2}$, which are studied in Theorem 1.2. The standard metric $\omega_{\beta}$ becomes the identity matrix under the basis above for (1, 1)-forms. If $\omega$ is $C_{\beta}^{0, \alpha}$, all the coefficients in the expression for $\omega$ in (3-114) are $C_{\boldsymbol{\beta}}^{0, \alpha}$-continuous, and the cross terms $g_{\epsilon_{j} \bar{\epsilon}_{k}}(j \neq k)$ and $g_{\epsilon_{j} \bar{k}}$ tend to zero when approaching the corresponding singular sets $\mathcal{S}_{j}$ or $\mathcal{S}_{k}$. Moreover, the limit of $g_{j \bar{k}} d z_{j} \wedge d \bar{z}_{k}$ when approaching $\mathcal{S}_{1} \cap \cdots \cap \mathcal{S}_{p}$ defines a Kähler metric on it. Rescaling or rotating the coordinates if necessary we may assume at $\hat{x}_{0} \in \mathcal{S}$ that $g_{\epsilon_{j} \bar{\epsilon}_{j}}\left(\hat{x}_{0}\right)=1, g_{j \bar{k}}\left(\hat{x}_{0}\right)=\delta_{j k}$ and the cross terms vanish at $\hat{x}_{0}$. Let $\omega_{\beta}$ be the standard cone metric under these new coordinates near $\hat{x}_{0}$. We can rewrite (3-110) as
$$\Delta_{g} u(z)=\Delta_{g_{\beta}} u(z)+\eta(z) \cdot i \partial \bar{\partial} u(z)=f(z) \quad \text { for all } z \notin \mathcal{S}$$
for some hermitian matrix $\eta(z)=\left(\eta^{j \bar{k}}\right)_{j, k=1}^{n}, \eta^{j \bar{k}}=g^{j \bar{k}}(z)-g_{\boldsymbol{\beta}}^{j \bar{k}}$. It is not hard to see the term $\eta(z) \cdot i \partial \bar{\partial} u$ can be written as
$$\sum_{j, k=1}^{2}\left(g^{\epsilon_{j} \bar{\epsilon}_{k}}(z)-\delta_{j k}\right) u_{\epsilon_{j} \bar{\epsilon}_{j}}+2 \operatorname{Re} \sum_{\substack{1 \leq j \leq 2 \\ 3 \leq k \leq n}} g^{\epsilon_{j} \bar{k}} u_{\epsilon_{j} \bar{k}}+\sum_{j, k=3}^{n}\left(g^{j \bar{k}}(z)-\delta_{j k}\right) u_{j \bar{k}},$$
where $g$ with the upper indices denotes the inverse matrix of $g$. We consider the equivalent form of (3-110) on $\hat{B}$ :
$$\Delta_{g_{\beta}} u=f-\eta \cdot \sqrt{-1} \partial \bar{\partial} u=: \hat{f}, \quad u \in C^{0}(\hat{B}) \cap C^{2}(\hat{B} \backslash \mathcal{S}) .$$

Observing that $x_{0}, y_{0} \in B_{\beta}\left(\hat{x}_{0}, \frac{3}{2} d\right)$, we can apply the scaled inequality (1-7) of Theorem 1.2 to conclude that
$$d^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}} \leq C\left(\|u\|_{C^{0}(\hat{B})}+\|\hat{f}\|_{C_{\beta}^{0, \alpha}(\hat{B})}^{(2)}\right) ;$$
thus
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}} \leq \frac{C}{\mu^{2+\alpha}}\left(\|u\|_{C^{0}(\hat{B})}+\|\hat{f}\|_{C_{\beta}^{0, \alpha}(\hat{B})}^{(2)}\right) .$$
Case 2: $d_{\beta}\left(x_{0}, y_{0}\right) \geq \frac{1}{2} d$.
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}} \leq 4 d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)\right|+\left|T u\left(y_{0}\right)\right|}{d^{\alpha}} \leq \frac{8}{\mu^{\alpha}}[u]_{C_{\beta}^{2}\left(B_{\beta}(0,1)\right)}^{*} .$$
Combining (3-113), (3-117) and (3-118) we get
$$\begin{aligned}
& d_{x_{0}}^{2+\alpha}\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right| \\
& d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha} \leq \frac{8}{\mu^{\alpha}}[u]_{C_{\beta}^{2}\left(B_{\beta}(0,1)\right)}^{*}+\frac{C}{\mu^{2+\alpha}}\left(\|u\|_{C^{0}(\hat{B})}+\|\hat{f}\|_{C_{\beta}^{0, \alpha}(\hat{B})}^{(2)}\right) \\
&+ \frac{C}{\mu^{2+\alpha}}\|f\|_{C_{\beta}^{0, \alpha}(B)}^{(2)}+\frac{C}{\mu^{2+\alpha}}\|u\|_{C^{0}(B)} .
\end{aligned}$$
By definition it is easy to see that (writing $B_{\beta}=B_{\beta}(0,1)$ )
$$\|f\|_{C_{\beta}^{0, \alpha}(B)}^{(2)} \leq C \mu^{2}\|f\|_{C^{0}\left(B_{\beta}\right)}^{(2)}+C \mu^{2+\alpha}[f]_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2)} \leq \mu^{2}\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2)} .$$
We calculate
$$\begin{aligned}
\|\hat{f}\|_{C_{\beta}^{0, \alpha}(\hat{B})}^{(2)} & \leq\|\eta\|_{C_{\beta}^{0, \alpha}(\hat{B})}^{(0)}\|T u\|_{C_{\beta}^{0, \alpha}(\hat{B})}^{(2)}+\|f\|_{C_{\beta}^{0, \alpha}(\hat{B})}^{(2)} \\
& \leq C_{0}[g]_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{*} \mu^{\alpha}\left(\mu^{2}[u]_{C_{\beta}^{2}\left(B_{\beta}\right)}^{*}+\mu^{2+\alpha}[u]_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{*}\right)+\mu^{2}\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2)} \\
& \leq C_{0}[g]_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{*} \mu^{\alpha}\left(C(\mu)\|u\|_{C^{0}\left(B_{\beta}\right)}+2 \mu^{2+\alpha}[u]_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{*}\right)+\mu^{2}\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2)}, \\
\frac{8}{\mu^{\alpha}}[u]_{C_{\beta}^{2}\left(B_{\beta}\right)}^{*} & \leq \mu^{\alpha}[u]_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{*}+C(\mu)\|u\|_{C^{0}\left(B_{\beta}\right)} .
\end{aligned}$$
If we choose $\mu>0$ small enough that $\mu^{\alpha}\left(2 C_{0}[g]_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{*}+1\right) \leq \frac{1}{2}$, then we get from (3-119) and the inequalities above that
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\beta}\left(x_{0}, y_{0}\right)^{\alpha}} \leq \frac{1}{2}[u]_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{*}+C(\mu)\left(\|u\|_{C^{0}\left(B_{\beta}\right)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2)}\right) .$$
Taking the supremum over $x_{0} \neq y_{0} \in B_{\boldsymbol{\beta}}(0,1)$, we conclude from the inequality above that
$$[u]_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{*} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}\right)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2)}\right) .$$
Proposition 3.32 then follows from interpolation inequalities. \(\square\)

Remark 3.33. It follows easily from the proof of Proposition 3.32 that estimate (3-111) also holds for metric balls $B_{\boldsymbol{\beta}}(p, R) \subset B_{\boldsymbol{\beta}}(0,1)$ whose center $p$ may not lie in $\mathcal{S}$.

Remark 3.34. The Schauder estimate was first established by Donaldson [14] for a background cone metric with singularity along a smooth divisor assuming $u \in C_{\beta}^{2, \alpha}$; this latter assumption was removed by Brendle [1] in the case $\beta \in\left(0, \frac{1}{2}\right)$ and by Jeffres, Mazzeo and Rubinstein [23], requiring only a weak solution. Jeffres, Mazzeo and Rubinstein [23] then extend the results to nonflat background metrics using a perturbation argument. This is the first time a Schauder estimate for the linear conic equation in the smooth divisor case appeared in the literature with a full proof.

An immediate corollary to Proposition 3.32 is the following interior Schauder estimate.
Corollary 3.35. Suppose u satisfies (3-110). For any compact subset $K \Subset B_{\beta}(0,1)$, there exists a constant $C=C\left(n, \boldsymbol{\beta}, K,\|g\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}\right)>0$ such that
$$\|u\|_{C_{\beta}^{2, \alpha}(K)} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}(0,1)\right)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}(0,1)\right)}\right) .$$

Next we will show that (3-110) admits a unique $C_{\boldsymbol{\beta}}^{2, \alpha}$-solution for any $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ and boundary value $\varphi \in C^{0}\left(\partial B_{\beta}(0,1)\right)$. We will follow the argument in Section 6.5 in [18]. In the following we write $B_{\beta}=B_{\beta}(0,1)$ for simplicity.
Lemma 3.36. Let $\sigma \in(0,1)$ be a given number. Suppose $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\right)$ solves $(3-110),\|u\|_{C^{0}\left(B_{\beta}\right)}^{(-\sigma)}<\infty$ and $\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2-\sigma)}<\infty$. Then there exists a $C=C(n, \boldsymbol{\beta}, \alpha, g, \sigma)>0$ such that
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{(-\sigma)} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}\right)}^{(-\sigma)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2-\sigma)}\right) .$$
Proof. Given the estimates in Proposition 3.32, the proof is identical to that of Lemma 6.20 in [18]. We omit the details. \(\square\)

Lemma 3.37. Let $u \in C_{\boldsymbol{\beta}}^{2}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ solve the equation $\Delta_{g} u=f$ and $u \equiv 0$ on $\partial B_{\boldsymbol{\beta}}$. For any $\sigma \in(0,1)$, there exists a constant $C=C(n, \boldsymbol{\beta}, \sigma, g)>0$ such that
$$\|u\|_{C^{0}\left(B_{\beta}\right)}^{(-\sigma)}=\sup _{x \in B_{\beta}} d_{x}^{-\sigma}|u(x)| \leq C \sup _{x \in B_{\beta}} d_{x}^{2-\sigma}|f(x)|=C\|f\|_{C^{0}\left(B_{\beta}\right)}^{(2-\sigma)},$$
where $d_{x}=d_{\boldsymbol{\beta}}\left(x, \partial B_{\boldsymbol{\beta}}\right)$ as before.
Proof. Consider the function $w_{1}=\left(1-d_{\boldsymbol{\beta}}^{2}\right)^{\sigma}$, where $d_{\boldsymbol{\beta}}(x)=d_{\boldsymbol{\beta}}(x, 0)$. We calculate
$$\begin{aligned}
\Delta_{g} w_{1} & =\sigma\left(1-d_{\beta}^{2}\right)^{\sigma-2}\left(-\left(1-d_{\beta}^{2}\right) \operatorname{tr}_{g} g_{\beta}-(1-\sigma)\left|\nabla d_{\beta}^{2}\right|_{g}^{2}\right) \\
& \leq \sigma\left(1-d_{\beta}^{2}\right)^{\sigma-2}\left(-C^{-1}\left(1-d_{\beta}^{2}\right)-4 C^{-1} d_{\beta}^{2}(1-\sigma)\right) \leq-c_{0} \sigma\left(1-d_{\beta}^{2}\right)^{\sigma-2} .
\end{aligned}$$
Take a large constant $A>1$ such that, for $w=A w_{1}$,
$$\Delta_{g} w \leq-\left(1-d_{\beta}\right)^{\sigma-2} \leq-\frac{|f|}{N} \text { in } B_{\beta},$$
where
$$N=\sup _{x \in B_{\beta}} d_{x}^{2-\sigma}|f(x)|=\sup _{x \in B_{\beta}}\left(1-d_{\beta}(x)\right)^{2-\sigma}|f(x)| .$$
Hence $\Delta_{g}(N w \pm u) \leq 0$, and from the definition of $w$ we also have $\left.w\right|_{\partial B_{\beta}} \equiv 0$. By the maximum principle we obtain $|u(x)| \leq N w \leq C N\left(1-d_{\beta}(x)\right)^{\sigma}=C N d_{x}^{\sigma}$, and hence the lemma is proved. \(\square\)

Proposition 3.38. Given any function $f \in C_{\beta}^{0, \alpha}\left(\overline{B_{\beta}}\right)$, the Dirichlet problem $\Delta_{g} u=f$ in $B_{\beta}$ and $u \equiv 0$ on $\partial B_{\beta}$ admits a unique solution $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\right) \cap C^{0}\left(\overline{B_{\beta}}\right)$.

Proof. The proof of this proposition is almost identical to that of Theorem 6.22 in [18]. For completeness, we provide the detailed argument. Fix $\sigma \in(0,1)$ and define a family of operators $\Delta_{t}=t \Delta_{g}+(1-t) \Delta_{g_{\beta}}$. It is straightforward to see that $\Delta_{t}$ is associated to some cone metric which also satisfies (3-109). We study the Dirichlet problem
$$\Delta_{t} u_{t}=f \quad \text { in } B_{\beta}, \quad u_{t} \equiv 0 \quad \text { on } \partial B_{\beta} .$$
Equation $\left(*_{0}\right)$ admits a unique solution $u_{0} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ by Proposition 3.7. By Theorem 5.2 in [18], in order to apply the continuity method to solve $\left(*_{1}\right)$, it suffices to show $\Delta_{t}^{-1}$ defines a bounded linear operator between some Banach spaces. More precisely, define
$$\begin{aligned}
& \mathcal{B}_{1}:=\left\{u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\right) \mid\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{(\sigma)}<\infty\right\}, \\
& \mathcal{B}_{2}:=\left\{f \in C_{\beta}^{0, \alpha}\left(B_{\beta}\right) \mid\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2-\sigma)}<\infty\right\} .
\end{aligned}$$
By definition any $u \in \mathcal{B}_{1}$ is continuous on $\overline{B_{\beta}}$ and $u=0$ on $\partial B_{\beta}$. By Lemmas 3.36 and 3.37, we have
$$\|u\|_{\mathcal{B}_{1}}=\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{(-\sigma)} \leq C\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2-\sigma)}=C\left\|\Delta_{t} u\right\|_{\mathcal{B}_{2}},$$
for some constant $C$ independent of $t \in[0,1]$. Thus $\left(*_{1}\right)$ admits a solution $u \in \mathcal{B}_{1}$. \(\square\)

Corollary 3.39. For any given $\varphi \in C^{0}\left(\partial B_{\beta}\right)$ and $f \in C_{\beta}^{0, \alpha}\left(\overline{B_{\beta}}\right)$, the Dirichlet problem
$$\Delta_{g} u=f \quad \text { in } B_{\beta} \quad \text { and } \quad u=\varphi \quad \text { on } \partial B_{\beta},$$
admits a unique solution $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\right) \cap C^{0}\left(\overline{B_{\beta}}\right)$.
Proof. We may extend $\varphi$ continuously to $B_{\beta}$ and assume $\varphi \in C^{0}\left(\overline{B_{\beta}}\right)$. Take a sequence of functions $\varphi_{k} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(\overline{B_{\boldsymbol{\beta}}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ which converges uniformly to $\varphi$ on $\overline{B_{\boldsymbol{\beta}}}$. The Dirichlet problem
$$\Delta_{g} v_{k}=f-\Delta_{g} \varphi_{k} \quad \text { in } B_{\beta} \quad \text { and } \quad v_{k}=0 \quad \text { on } \partial B_{\beta}$$
admits a unique solution $v_{k} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$. Thus the function $u_{k}:=v_{k}+\varphi_{k} \in C_{\boldsymbol{\beta}}^{2, \alpha}$ satisfies $\Delta_{g} u_{k}=f$ in $B_{\beta}$ and $u_{k}=\varphi_{k}$ on $\partial B_{\beta}$. By the maximum principle, $u_{k}$ is uniformly bounded in $C^{0}\left(\overline{B_{\beta}}\right)$. Corollary 3.35 gives uniformly $C_{\beta}^{2, \alpha}(K)$-bounds on any compact subset $K \Subset B_{\beta}$. Letting $k \rightarrow \infty$ and $K \rightarrow B_{\beta}$, by a diagonal argument and up to a subsequence, $u_{k} \rightarrow u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\right)$. On the other hand, from $\Delta_{g}\left(u_{k}-u_{l}\right)=0$, we see that $\left\{u_{k}\right\}$ is a Cauchy sequence in $C^{0}\left(\overline{B_{\beta}}\right)$; thus $u_{k}$ converges uniformly to $u$ on $\overline{B_{\beta}}$. Hence $u \in C^{0}\left(\overline{B_{\beta}}\right)$, and $u$ satisfies (3-120). \(\square\)

Corollary 3.40. Given $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)$, suppose $u$ is a weak solution to the equation $\Delta_{g} u=f$ in the sense that
$$\int_{B_{\beta}}\langle\nabla u, \nabla \varphi\rangle \omega_{g}^{n}=-\int_{B_{\beta}} f \varphi \omega_{g}^{n} \quad \text { for all } \varphi \in H_{0}^{1}\left(B_{\beta}\right),$$
then $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\right)$.

Proof. We first observe that the Sobolev inequality (3-43) also holds for the metric $g$, since $g$ is equivalent to $g_{\beta}$. The metric space ( $B_{\beta}, g$ ) also has maximal volume growth/decay, so we can apply the same proof of De Giorgi-Nash-Moser theory [22] to conclude that $u$ is continuous in $B_{\beta}$. The standard elliptic theory implies that $u \in C_{\text {loc }}^{2, \alpha}\left(B_{\beta} \backslash \mathcal{S}\right)$. For any $r \in(0,1)$, by Corollary 3.39, the Dirichlet problem $\Delta_{g} \tilde{u}=f$ in $B_{\beta}(0, r), \tilde{u}=u$ on $\partial B_{\beta}(0, r)$ admits a unique solution $\tilde{u} \in C_{\beta}^{2, \alpha}\left(B_{\beta}(0, r)\right) \cap C^{0}\left(\overline{B_{\beta}(0, r)}\right)$. Then $\Delta_{g}(u-\tilde{u})=0$ in $B_{\beta}(0, r)$ and $u-\tilde{u}=0$ on $\partial B_{\beta}(0, r)$. By the maximum principle, we get $u=\tilde{u}$ in $B_{\beta}(0, r)$, so we conclude $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}(0, r)\right)$. Since $r \in(0,1)$ is arbitrary, we get $u \in C_{\beta}^{2, \alpha}\left(B_{\beta}\right)$. \(\square\)

Corollary 3.41. Let $X$ be a compact Kähler manifold and $D=\sum_{j} D_{j}$ be a divisor with simple normal crossings. Let $g$ be a conical Kähler metric with cone angle $2 \pi \beta$ along D. Suppose $u \in H^{1}(g)$ is a weak solution to the equation $\Delta_{g} u=f$ in the sense that
$$\int_{X}\langle\nabla u, \nabla \varphi\rangle \omega_{g}^{n}=-\int_{X} f \varphi \omega_{g}^{n} \quad \text { for all } \varphi \in C^{1}(X)$$
for some $f \in C_{\boldsymbol{\beta}}^{0, \alpha}(X)$. Then $u \in C_{\boldsymbol{\beta}}^{2, \alpha}(X) \cap C^{0}(X)$ and there exists a constant $C=C(n, \boldsymbol{\beta}, g, \alpha)$ such that
$$\|u\|_{C_{\beta}^{2, \alpha}(X)} \leq C\left(\|u\|_{C^{0}(X)}+\|f\|_{C_{\beta}^{0, \alpha}(X)}\right) .$$
Proof. We choose finite covers of $D,\left\{B_{a}\right\}$ and $\left\{B_{a}^{\prime}\right\}$, with $B_{a}^{\prime} \Subset B_{a}$ and centers in $D$. By assumption $u$ is a weak solution to $\Delta_{g} u=f$ in each $B_{a}$, so by Corollary 3.40 we conclude that $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{a}\right)$ for each $B_{a}$. On $X \backslash \mathcal{S}$, the metric $g$ is smooth so standard elliptic theory implies that $u \in C_{\text {loc }}^{2, \alpha}(X \backslash \mathcal{S})$. Since $\left\{B_{a}\right\}$ covers $D$, we have $u \in C_{\boldsymbol{\beta}}^{2, \alpha}(X)$.

We can apply Corollary 3.35 to obtain that, for some constant $C>0$,
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{a}^{\prime}\right)} \leq C\left(\|u\|_{C^{0}\left(B_{a}\right)}+\|f\|_{C_{\beta}^{\alpha}\left(B_{a}\right)}\right) .$$
On $X \backslash \bigcup_{a}\left\{B_{a}^{\prime}\right\}$ the metric $g$ is smooth, so the usual Schauder estimates apply. We finish the proof of the corollary using the definition of $C_{\beta}^{2, \alpha}(X)$; see Definition 2.9. \(\square\)

Remark 3.42. Let $(X, D, g)$ be as in Corollary 3.41. It is easy to see by the variational method that weak solutions to $\Delta_{g} u=f$ always exist for any $f \in L^{2}\left(X, \omega_{g}^{n}\right)$ satisfying $\int_{X} f \omega_{g}^{n}=0$.

\section*{4. Parabolic estimates}

In this section, we will study the heat equation with background metric $\omega_{\beta}$ and prove the Schauder estimates for solutions $u \in C^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathscr{C}^{2,1}\left(\mathcal{Q}_{\boldsymbol{\beta}}^{\#}\right)$ to the equation
$$\frac{\partial u}{\partial t}=\Delta_{g_{\beta}} u+f$$
for a function $f \in \mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)$ with some better regularity.
4A. Conical heat equations. In this section, we will show that, for any $\varphi \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\beta}\right)$, the Dirichlet problem (4-2) admits a unique $\mathscr{C}^{2,1}\left(\mathcal{Q}_{\beta}^{\#}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$-solution in $\mathcal{Q}_{\beta}$. We first observe that a maximum principle argument yields the uniqueness of the solution.

Suppose $u \in \mathscr{C}^{2,1}\left(\mathcal{Q}_{\beta}^{\#}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$ solves the Dirichlet problem
$$\begin{cases}\frac{\partial u}{\partial t}=\Delta_{g_{\beta}} u & \text { in } \mathcal{Q}_{\beta} \\ u=\varphi & \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta}\end{cases}$$
for some given continuous function $\varphi \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\beta}\right)$. As in Lemma 3.1, it follows from the maximum principle that
$$\inf _{\partial_{\mathcal{P}} \mathcal{Q}_{\beta}} u \leq \inf _{\mathcal{Q}_{\beta}} u \leq \sup _{\mathcal{Q}_{\beta}} u \leq \sup _{\partial_{\mathcal{P}} \mathcal{Q}_{\beta}} u .$$
So the $\mathscr{C}^{2,1}\left(\mathcal{Q}_{\beta}^{\#}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$-solution to (4-2) is unique, if it exists.
We prove the existence of solutions to (4-2). As before, we use an approximation argument. Let $g_{\epsilon}$ be the smooth approximation metrics in $B_{\beta}$ from (3-3). Let $u_{\epsilon}$ be the $\mathscr{C}^{2,1}\left(\mathcal{Q}_{\beta}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$-solution to
$$\frac{\partial u_{\epsilon}}{\partial t}=\Delta_{g_{\epsilon}} u_{\epsilon} \quad \text { in } \mathcal{Q}_{\beta} \quad \text { and } \quad u_{\epsilon}=\varphi \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta} .$$
4A1. Estimates of $u_{\epsilon}$. We first recall the Li-Yau gradient estimates [26; 35] for positive solutions to the heat equations.

Lemma 4.1. Let $(M, g)$ be a complete manifold with $\operatorname{Ric}(g) \geq 0$ and $B(p, R)$ be the geodesic ball with center $p \in M$ and radius $R>0$. Let $u$ be a positive solution to the heat equation $\partial_{t} u-\Delta_{g} u=0$ on $B(p, R)$. Then there exists $C=C(n)>0$ such that, for all $t>0$,
$$\sup _{B(p, 2 R / 3)}\left(\frac{|\nabla u|^{2}}{u^{2}}-\frac{2 \dot{u}_{t}}{u}\right) \leq \frac{C}{R^{2}}+\frac{2 n}{t},$$
where $\dot{u}_{t}=\partial u / \partial t$.
By considering the functions $u_{\epsilon}-\inf u_{\epsilon}$ and $\sup u_{\epsilon}-u_{\epsilon}$, from Lemma 4.1, we see that there exists a constant $C=C(n)>0$ such that, for any $R \in(0,1)$ and $t \in\left(0, R^{2}\right)$,
$$\begin{gathered}
\sup _{B_{g \epsilon}(0,2 R / 3)}\left|\nabla u_{\epsilon}\right|_{g_{\epsilon}}^{2} \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right)\left(\operatorname{osc}_{R} u_{\epsilon}\right)^{2}, \\
\sup _{B_{g \epsilon}(0,2 R / 3)}\left|\Delta_{g_{\epsilon}} u_{\epsilon}\right|=\sup _{B_{g \epsilon}(0,2 R / 3)}\left|\frac{\partial u_{\epsilon}}{\partial t}\right| \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right) \operatorname{osc}_{R} u_{\epsilon},
\end{gathered}$$
where $\operatorname{osc}_{R} u_{\epsilon}:=\operatorname{osc}_{B_{g_{\epsilon}}(0, R) \times\left(0, R^{2}\right)} u_{\epsilon}$ is the oscillation of $u_{\epsilon}$ in the cylinder $B_{g_{\epsilon}}(0, R) \times\left(0, R^{2}\right)$. Replacing $u_{\epsilon}$ by $u_{\epsilon}-\inf u_{\epsilon}$, we may assume $u_{\epsilon}>0$ and define $f_{\epsilon}=\log u_{\epsilon}$. Then we have
$$\frac{\partial f_{\epsilon}}{\partial t}=\Delta_{g_{\epsilon}} f_{\epsilon}+\left|\nabla f_{\epsilon}\right|^{2} .$$
Let $\varphi(x)=\varphi(r(x) / R)$, where $\varphi$ is a cut-off function equal to 1 on $\left[0, \frac{3}{5}\right]$ and 0 on $\left[\frac{2}{3}, \infty\right)$ satisfying the inequalities $\left|\varphi^{\prime \prime}\right| \leq 10$ and $\left(\varphi^{\prime}\right)^{2} \leq 10 \varphi$. Let $r(x)$ be the distance function under $g_{\epsilon}$ to the center 0 .