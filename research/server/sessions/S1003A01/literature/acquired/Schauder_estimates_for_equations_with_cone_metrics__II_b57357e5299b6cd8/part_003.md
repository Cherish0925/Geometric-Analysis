---
retention_scope: session
part: 3
total_parts: 5
---

[Part 3/5 of: Schauder estimates for equations with cone metrics, II]

Lemma 3.16. $L_{3}$ satisfies
$$L_{3} \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
Proof. As in the proof of previous lemma, we need to consider different cases: $\ell \geq k_{1, p}+1, \ell \geq k_{2, p}+1$ or $\ell \leq k_{2, p}$.
- If $\ell \geq k_{1, p}+1$, then the ball $\hat{B}_{\ell}(p)=B_{\boldsymbol{\beta}}\left(p, \tau^{\ell}\right)$ and the function $U$ defined in (3.55) is $g_{\boldsymbol{\beta}^{-}}$harmonic in $\frac{1}{2} \hat{B}_{\ell}(p)$, and $\sup _{\frac{1}{2} \hat{B}_{\ell}(p)}|U| \leq C \omega^{2 \ell} \omega\left(\tau^{\ell}\right)$. Since $\frac{1}{2} \hat{B}_{\ell}(p)$ is disjoint with $\mathcal{S}, w_{1}$ and $w_{2}$ are well-defined on $\frac{1}{2} \hat{B}_{\ell}(p)$ and thus we have the derivative estimate:
$$\sup _{\frac{1}{3} \hat{B}_{\ell}(p)}\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}\right| \leq \sup _{\frac{1}{3} \hat{B}_{\ell}(p)}\left|D_{w_{1}} D_{w_{2}} U\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
In particular, at $q \in \frac{1}{3} \hat{B}_{\ell}(p)$
$$L_{3}=\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right|=\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}(q)\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
- If $k_{1, p} \geq \ell \geq k_{2, p}$, then the ball $\hat{B}_{\ell}(p)=B_{\boldsymbol{\beta}}\left(p_{1}, 2 \tau^{\ell}\right)$ and the function $U$ defined in (3.55) is $g_{\boldsymbol{\beta}^{-}}$harmonic and well-defined in a ball $B_{q}:=B_{\boldsymbol{\beta}}\left(q, \tau^{\ell} / 10\right) \subset \frac{1}{2.2} \hat{B}_{\ell}(p)$, and $\sup _{\frac{1}{2} \hat{B}_{\ell}(p)}|U| \leq C \omega^{2 \ell} \omega\left(\tau^{\ell}\right)$. Since $\frac{1}{2} \hat{B}_{\ell}(p)$ is disjoint with $\mathcal{S}_{2}, w_{2}$ is well-defined on $\frac{1}{2.2} \hat{B}_{\ell}(p)$ and thus we have the derivatives estimates:
$$\sup _{\frac{1}{2} B_{q}}\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}\right| \leq \sup _{\frac{1}{2} B_{q}}\left|\frac{\partial}{\partial r_{1}} D_{w_{2}} U\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
In particular, at $q \in \frac{1}{2} B_{q}$, we have
$$L_{3}=\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)-\frac{\partial^{2} v_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right|=\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}(q)\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right) .$$
- If $\ell \leq k_{2, p}-1$, then $r_{2}(p) \approx \tau^{k_{2, p}} \leq \tau^{\ell+1}<8 d$, so $r_{2}(q) \leq r_{2}(p)+d \leq \frac{5}{8} \tau^{\ell}$ and $r_{1}(q) \leq d+r_{1}(p) \leq$ $d+r_{2}(p) \leq \frac{5}{8} \tau^{\ell}$. Therefore the ball $\tilde{B}_{\ell}(q)$ is centered at $q_{1}$, or $q_{2}$ or $q_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ with radius $2 \tau^{\ell}$. It follows from this that the function $U$ defined in (3.55) is well-defined on the ball $\frac{1}{1.8} \hat{B}_{\ell}(p)$.

By the same strategy as in the proof of Lemma 3.12, with the harmonic function $D^{\prime} h_{k}$ in that lemma replaced by $U$ on the metric ball $\frac{1}{1.8} \hat{B}_{\ell}(p)$, we can prove that for any $z \in \frac{1}{2} \hat{B}_{\ell}(p) \backslash \mathcal{S}$ the following holds:
$$\left|\frac{\partial^{2} U}{\partial r_{1} \partial r_{2}}(z)\right| \leq C(n, \boldsymbol{\beta}) r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-\ell\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{\ell}\right) .$$

Applying this inequality at $q$ we get
$$L_{3}=\left|\frac{\partial^{2}\left(u_{\ell}-v_{\ell}\right)}{\partial r_{1} \partial r_{2}}(q)\right| \leq C(n, \boldsymbol{\beta}) r_{1}(q)^{\frac{1}{\beta_{1}}-1} r_{2}(q)^{\frac{1}{\beta_{2}}-1} \tau^{-\ell\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{\ell}\right) \leq C \omega\left(\tau^{\ell}\right) .$$
In sum, in all cases $L_{3} \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{\ell}\right)$. \(\square\)

Lemma 3.17. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that for all $k \leq \ell$ and $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial \theta_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)(z)\right|+\left|\left(\frac{\partial^{3} h_{k}}{r_{1} \partial \theta_{1}^{2} \partial r_{2}}\right)\right| \leq C \cdot\left\{\begin{array}{l}
r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right), \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right), \text { if } k \leq k_{2, p} .
\end{array}\right.$$
Proof. The proof is parallel to that of Lemma 3.12. The function $\frac{\partial h_{k}}{\partial \theta_{1}}$ is $g_{\beta}$-harmonic on $\hat{B}_{k}(p)$, and by the Laplacian estimate (3.9), we have
$$\sup _{\frac{1}{1.2} \hat{B}_{k}(p)}\left(\left|\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{1}}\right|+\left|\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|\right) \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{k}\right) .$$
The function $\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}$ is also $g_{\beta}$-harmonic, so the Laplacian estimates (3.9) imply
$$\sup _{\frac{1}{1.4} \hat{B}_{k}(p)}\left(\left|\Delta_{1} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|+\left|\Delta_{2} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|+\left|\left(D^{\prime}\right)^{2} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right|\right) \leq C \tau^{-2 k}\left(\operatorname{osc}_{\frac{1}{1.2} \hat{B}_{k}(p)} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right) \leq C \tau^{-2 k} \omega\left(\tau^{k}\right) .$$
We consider the equation
$$\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)=-\Delta_{1} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}} \Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}=: F_{5},$$
where the function $F_{5}$ satisfies $\sup _{\frac{1}{1.4} \hat{B}_{k}(p)}\left|F_{5}\right| \leq C \tau^{-2 k} \omega\left(\tau^{k}\right)$.
- In case $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right)$, we can introduce the smooth coordinate $w_{2}=z_{2}^{\beta_{2}}$ in the ball $\frac{1}{1.5} \hat{B}_{k}(p)$ as before, since this ball is disjoint with $\mathcal{S}_{2}$ and under the coordinates $\left(r_{1}, \theta_{1} ; w_{2}, z_{3}, \ldots, z_{n}\right)$ we can use the usual standard gradient estimate to the $g_{\beta}$-harmonic function $\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}$ to obtain that
$$\sup _{\frac{1}{2} \hat{B}_{k}(p)}\left|\frac{\partial}{\partial r_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
- In case $k \leq k_{2, p}$, the ball $\hat{B}_{k}(p)$ is centered at $p_{1,2}$. We apply the usual estimate (2.2) to the function $\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}$, the solution to the equation (3.94), on any $\mathbb{C}$-ball $A_{2}:=B_{\mathbb{C}}\left(y,\left(\tau^{k}\right)^{1 / \beta_{2}}\right)$ for any $y \in \mathcal{S}_{2} \cap \frac{1}{1.6} \hat{B}_{k}(p)$ where $A_{2}$ denotes the Euclidean ball in the complex plane orthogonal to $\mathcal{S}_{2}$ and passing through $y$. Then for any $z \in B_{\mathbb{C}}\left(y,\left(\tau^{k}\right)^{1 / \beta_{2}} / 2\right) \backslash\{y\}$
$$\left|\frac{\partial}{\partial z_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)(z)\right| \leq C \frac{\left\|\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right\|_{L^{\infty}\left(A_{2}\right)}}{\tau^{k / \beta_{2}}}+C\left\|F_{5}\right\|_{L^{\infty}\left(A_{2}\right)}\left(\tau^{k}\right)^{2-\frac{1}{\beta_{2}}} \leq C \tau^{-k / \beta_{2}} \omega\left(\tau^{k}\right) .$$
This implies that on $\frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial r_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)\right| \leq C r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k / \beta_{2}} \omega\left(\tau^{k}\right) .$$

Taking $\frac{\partial}{\partial r_{2}}$ on both sides of $\Delta_{\boldsymbol{\beta}} \frac{\partial h_{k}}{\partial \theta_{1}}=0$, we get
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right)=-\frac{\partial}{\partial r_{2}}\left(\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{1}}\right)-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right)=: F_{6} .$$
It is not hard to see from (3.95) and (3.96) and standard derivative estimates that on $\frac{1}{1.8} \hat{B}_{k}(p) \backslash \mathcal{S}$ (i) in case $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right),\left|F_{6}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right)$;
(ii) in case $k \leq k_{2, p}\left|F_{6}\right| \leq C r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-\frac{k}{\beta_{2}}} \omega\left(\tau^{k}\right)$.
Then by applying estimate (2.2) to the function $\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}$ on any $\mathbb{C}$-ball $A_{3}:=B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}}\right)$ for any $x \in \frac{1}{1.8} \hat{B}_{k}(p) \cap \mathcal{S}_{1}$ we get that on $B_{\mathbb{C}}\left(x,\left(\tau^{k}\right)^{1 / \beta_{1}} / 2\right) \backslash\{x\}$
$$\begin{aligned}
\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right)\right|+ & \left|\frac{\partial}{r_{1} \partial \theta_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right)\right| \leq C r_{1}^{\frac{1}{\beta_{1}}-1} \frac{\left\|\frac{\partial^{2} h_{k}}{\partial r_{2} \partial \theta_{1}}\right\|_{L^{\infty}\left(A_{3}\right)}}{\tau^{k / \beta_{1}}}+C r_{1}^{\frac{1}{\beta_{1}}-1}\left\|F_{6}\right\|_{L^{\infty}\left(A_{3}\right)} \tau^{k\left(2-\frac{1}{\beta_{1}}\right)} \\
& \leq C \cdot\left\{\begin{array}{l}
r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right), \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right), \text { if } k \leq k_{2, p} .
\end{array}\right.
\end{aligned}$$
Therefore this estimate holds on $\frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$. \(\square\)

Lemma 3.18. For any $k \leq \ell$ and any point $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$ the following estimates hold
$$\begin{gathered}
\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(z)\right| \leq C \cdot\left\{\begin{array}{l}
r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right), \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right), \text { if } k \leq k_{2, p} .
\end{array}\right. \\
\left|\frac{\partial^{2} D^{\prime} h_{k}}{\partial r_{1} \partial r_{2}}(z)\right| \leq C \cdot\left\{\begin{array}{l}
r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right), \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right), \text { if } k \leq k_{2, p} .
\end{array}\right.
\end{gathered}$$
Proof. This follows from almost the same argument as in the proof of Lemma 3.17, by studying the harmonic functions $h_{k}$ and $D^{\prime} h_{k}$ instead of $\frac{\partial h_{k}}{\partial \theta_{1}}$. \(\square\)

Lemma 3.19. The following estimate holds for any $k \leq \ell$ and any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|(z) \leq C \omega\left(\tau^{k}\right) \cdot\left\{\begin{array}{l}
\tau^{-k}+r_{1}(z)^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}, \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{2}(z)^{\frac{1}{\beta_{2}}-1} \tau^{-\frac{k}{\beta_{2}}}+r_{1}(z)^{\frac{1}{\beta_{1}}-2} r_{2}(z)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}, \text { if } k \leq k_{2, p}
\end{array}\right.$$

Proof. By the Laplacian estimates (3.9) we have
$$\sup _{\frac{1}{1.2} \hat{B}_{k}(p) \backslash \mathcal{S}}\left|\Delta_{1} h_{k}\right|+\left|\Delta_{2} h_{k}\right| \leq C(n, \boldsymbol{\beta}) \omega\left(\tau^{k}\right) .$$
Applying again the Laplacian estimate (3.9) to the $g_{\boldsymbol{\beta}}$-harmonic function $\Delta_{1} h_{k}$,
$$\sup _{\frac{1}{1.4} \hat{B}_{k}(p)}\left(\left|\Delta_{1} \Delta_{1} h_{k}\right|+\left|\Delta_{2} \Delta_{1} h_{k}\right|+\left|\left(D^{\prime}\right)^{2} \Delta_{1} h_{k}\right|\right) \leq C(n, \boldsymbol{\beta}) \tau^{-2 k} \omega\left(\tau^{k}\right) .$$

We consider the equation
$$\left|z_{2}\right|^{2-2 \beta_{2}} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}} \Delta_{1} h_{k}=-\Delta_{1} \Delta_{1} h_{k}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}} \Delta_{1} h_{k}=: F_{7} .$$
From the estimates above, we see $\left\|F_{7}\right\|_{L^{\infty}\left(\frac{1}{1.8} \hat{B}_{k}(p)\right)} \leq C \tau^{-2 k} \omega\left(\tau^{k}\right)$.
\begin{itemize}
\item[-] When $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right)$, we directly apply gradient estimate to $\Delta_{1} h_{k}$ to get
$$\sup _{\frac{1}{1.5} \hat{B}_{k}(p) \backslash \mathcal{S}}\left|\frac{\partial}{\partial r_{2}} \Delta_{1} h_{k}\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}} \Delta_{1} h_{k}\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
\item[-] When $k \leq k_{2, p}$, the balls $\hat{B}_{k}(p)$ are centered at $p_{1,2}$, and we can apply the usual $\mathbb{C}$-ball type estimate to get that for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\begin{aligned}
\left|\frac{\partial}{\partial r_{2}} \Delta_{1} h_{k}\right|(z)+\left|\frac{\partial}{r_{2} \partial \theta_{2}} \Delta_{1} h_{k}\right| & \leq C r_{2}(z)^{\frac{1}{\beta_{2}}-1} \frac{\left\|\Delta_{1} h_{k}\right\|_{L^{\infty}}}{\tau^{k / \beta_{2}}}+C r_{2}(z)^{\frac{1}{\beta_{2}}-1}\left\|F_{7}\right\|_{L^{\infty}} \tau^{k\left(2-\frac{1}{\beta_{2}}\right)} \\
& \leq C r_{2}(z)^{\frac{1}{\beta_{2}}-1} \tau^{-k / \beta_{2}} \omega\left(\tau^{k}\right) .
\end{aligned}$$
\end{itemize}
Recall the following equation holds
$$\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)=\frac{\partial}{\partial r_{2}} \Delta_{1} h_{k}-\frac{1}{r_{1}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}-\frac{1}{\beta_{1}^{2} r_{1}^{2}} \frac{\partial^{3} h_{k}}{\partial \theta_{1}^{2} \partial r_{2}}$$
from which we derive that for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|(z) \leq C \omega\left(\tau^{k}\right)\left\{\begin{array}{l}
\tau^{-k}+r_{1}(z)^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}, \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{2}(z)^{\frac{1}{\beta_{2}}-1} \tau^{-\frac{k}{\beta_{2}}}+r_{1}(z)^{\frac{1}{\beta_{1}}-2} r_{2}(z)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}, \text { if } k \leq k_{2, p}
\end{array}\right.$$ \(\square\)

Lemma 3.20. There exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that for all $k \leq \ell$ and $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)(z)\right|+\left|\left(\frac{\partial^{3} h_{k}}{r_{2} \partial \theta_{2}^{2} \partial r_{1}}\right)(z)\right| \leq C \omega\left(\tau^{k}\right)\left\{\begin{array}{l}
r_{1}^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)}, \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}, \text { if } k \leq k_{2, p} .
\end{array}\right.$$
Proof. It follows from the Laplacian estimate (3.9) that
$$\sup _{\frac{1}{1.2} \hat{B}_{k}(p)}\left(\left|\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|+\left|\Delta_{2} \frac{\partial h_{k}}{\partial \theta_{2}}\right|\right) \leq C(n) \omega\left(\tau^{k}\right) .$$
And by (3.9) again we have
$$\sup _{\frac{1}{1.4} \hat{B}_{k}(p)}\left(\left|\Delta_{1} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|+\left|\Delta_{2} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|+\left|\left(D^{\prime}\right)^{2} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|\right) \leq C \tau^{-2 k} \omega\left(\omega^{k}\right) .$$
We look at the equation
$$\left|z_{1}\right|^{2\left(1-\beta_{1}\right)} \frac{\partial^{2}}{\partial z_{1} \partial \bar{z}_{1}}\left(\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right)=-\Delta_{2} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}-\sum_{j} \frac{\partial^{2}}{\partial s_{j}^{2}}\left(\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right)=: F_{8},$$
and $F_{8}$ satisfies $\sup _{\frac{1}{1.4} \hat{B}_{k}(p)}\left|F_{8}\right| \leq C \tau^{-2 k} \omega\left(\tau^{k}\right)$. By the estimate (2.2) as we did before it follows that for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$ (remember here $k \leq \min \left(\ell, k_{p}\right)$ )
$$\begin{aligned}
\left|\frac{\partial}{\partial r_{1}} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|(z)+\left|\frac{\partial}{r_{1} \partial \theta_{1}} \Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right|(z) & \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-1} \frac{\left\|\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right\|_{L^{\infty}}}{\tau^{k / \beta_{1}}}+C r_{1}(z)^{\frac{1}{\beta_{1}}-1}\left\|F_{8}\right\|_{L^{\infty}} \tau^{k\left(2-\frac{1}{\beta_{1}}\right)} \\
& \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right)
\end{aligned}$$
Taking $\frac{\partial}{\partial r_{1}}$ on both sides of the equation $\Delta_{\boldsymbol{\beta}} \frac{\partial h_{k}}{\partial \theta_{2}}=0$, we get
$$\left|z_{2}\right|^{2\left(1-\beta_{2}\right)} \frac{\partial^{2}}{\partial z_{2} \partial \bar{z}_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)=-\frac{\partial}{\partial r_{1}}\left(\Delta_{1} \frac{\partial h_{k}}{\partial \theta_{2}}\right)-\sum_{j} \frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2}}{\partial s_{j}^{2}} \frac{\partial h_{k}}{\partial \theta_{2}}\right)=: F_{9} .$$
Here $\left|F_{9}(z)\right| \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right)$ for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$. Therefore we get by the usual $\mathbb{C}$-ball argument that
\begin{itemize}
\item[-] If $k \leq k_{2, p}$, then for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right| \leq C r_{2}(z)^{\frac{1}{\beta_{2}}-1} r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{k\left(2-\frac{1}{\beta_{1}}-\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right)$$
\item[-] If $k_{2, p}+1 \leq k \leq \min \left(\ell, k_{p}\right)$, then
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial \theta_{2}}\right)(z)\right| \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{k\left(1-\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right) .$$
\end{itemize} \(\square\)

Lemma 3.21. The following estimate holds for any $k \leq \ell$ and any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \leq C \omega\left(\tau^{k}\right)\left\{\begin{array}{l}
r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}}+r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)}, \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}}+r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-2} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}, \text { if } k \leq k_{2, p} .
\end{array}\right.$$

Proof. We first observe the following equation
$$\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)=\frac{\partial}{\partial r_{1}} \Delta_{2} h_{k}-\frac{1}{r_{2}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}-\frac{1}{\beta_{2}^{2} r_{2}^{2}} \frac{\partial^{2}}{\partial \theta_{2}^{2}}\left(\frac{\partial h_{k}}{\partial r_{1}}\right) .$$
It can be shown that for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$ by the $\mathbb{C}$-ball argument that
$$\left|\frac{\partial}{\partial r_{1}} \Delta_{2} h_{k}(z)\right| \leq C r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}} \omega\left(\tau^{k}\right) .$$
From Lemma 3.18, we have for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{1}{r_{2}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(z)\right| \leq C \cdot\left\{\begin{array}{l}
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)} \omega\left(\tau^{k}\right), \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-2} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \omega\left(\tau^{k}\right), \text { if } k \leq k_{2, p} .
\end{array}\right.$$
From Lemma 3.20, we have for any $z \in \frac{1}{2} \hat{B}_{k}(p) \backslash \mathcal{S}$
$$\left|\frac{1}{r_{2}^{2}} \frac{\partial^{3} h_{k}}{\partial r_{1} \partial \theta_{2}^{2}}(z)\right| \leq C \omega\left(\tau^{k}\right) \cdot\left\{\begin{array}{l}
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)}, \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-2} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}, \text { if } k \leq k_{2, p} .
\end{array}\right.$$

Therefore for any $z \in \frac{1}{3} \hat{B}_{k}(p) \backslash \mathcal{S}$ we have
$$\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)(z)\right| \leq C \omega\left(\tau^{k}\right) \cdot\left\{\begin{array}{l}
r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}}+r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)}, \text { if } k \in\left[k_{2, p}+1, \min \left(\ell, k_{p}\right)\right] \\
r_{1}(z)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}}+r_{1}^{\frac{1}{\beta_{1}}-1} r_{2}^{\frac{1}{\beta_{2}}-2} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}, \text { if } k \leq k_{2, p} .
\end{array}\right.$$ \(\square\)

It remains to estimate $L_{2}$. For simplicity, we denote $h_{k}:=-u_{k}+u_{k-1}$ as before, where we take $k \leq \ell$. We will denote $\beta_{\text {max }}=\max \left(\beta_{1}, \beta_{2}\right)$.

Lemma 3.22. Let $d=d_{\boldsymbol{\beta}}(p, q)$. There exists a constant $C(n, \boldsymbol{\beta})>0$ such that for all $k \leq \ell$
$$\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} d^{\frac{1}{\beta_{1}}-1} \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(\frac{1}{\beta_{\max }}-1\right)} d^{\frac{1}{\beta_{\max }}-1} .$$
Proof. - Case 1: First we assume that $r_{p} \leq 2 d$ so $r_{q} \leq 3 d$ and $\ell+2 \leq k_{p}$, in particular, the balls $\hat{B}_{k}(p)$ are centered at either $p_{1} \in \mathcal{S}_{1}$ or 0, depending on whether $k \geq k_{2, p}+1$ or $k \leq k_{2, p}$. As in the proof of Lemma 3.13, let $\gamma:[0, d] \rightarrow B_{\boldsymbol{\beta}}(0,1) \backslash S$ be the $g_{\boldsymbol{\beta}}$-geodesic connecting $p$ and $q$. The two points $q^{\prime}$ and $p^{\prime}$ are defined as in (3.80), $\gamma_{1}, \gamma_{2}, \gamma_{3}$ the $g_{\boldsymbol{\beta}}$-geodesics as defined in that lemma. We calculate by triangle inequality that
$$\begin{aligned}
& \left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \\
& \leq\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(p^{\prime}\right)\right|+\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(p^{\prime}\right)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(q^{\prime}\right)\right| \\
& \quad+\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(q^{\prime}\right)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right|=: L_{1}^{\prime}+L_{2}^{\prime}+L_{3}^{\prime} .
\end{aligned}$$
Integrating along $\gamma_{3}$ on which the coordinates $\left(r_{1} ; r_{2}, \theta_{2} ; z_{3}, \ldots, z_{n}\right)$ are the same as $p$, we get by (3.93)
$$\begin{aligned}
L_{1}^{\prime} & =\left|\int_{\gamma_{3}} \frac{\partial}{\partial \theta_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d \theta_{1}\right| \\
& \leq C \omega\left(\tau^{k}\right) \cdot\left\{\begin{array}{l}
r_{1}(p)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)}, \text { if } k \in\left[k_{2, p}+1, \ell\right] \\
r_{1}(p)^{\frac{1}{\beta_{1}}-1} r_{2}(p)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}, \text { if } k \leq k_{2, p}
\end{array} .\right.
\end{aligned}$$
Integrating along $\gamma_{2}$ along which the coordinates $\left(\theta_{1} ; r_{2}, \theta_{2} ; z_{3}, \ldots, z_{n}\right)$ are the same as $p^{\prime}$ or $q^{\prime}$, we get by (3.99) that
$$\begin{aligned}
L_{2}^{\prime}= & \left|\int_{\gamma_{2}} \frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d r_{1}\right| \\
& \leq C \omega\left(\tau^{k}\right) \cdot\left\{\begin{array}{l}
\tau^{-k} d+\tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}\left|r_{1}(p)-r_{1}(q)\right|^{\frac{1}{\beta_{1}}-1}, \text { if } k \in\left[k_{2, p}+1, \ell\right] \\
r_{2}(p)^{\frac{1}{\beta_{2}}-1} \tau^{-\frac{k}{\beta_{2}}} d+r_{2}(p)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}\left|r_{1}(p)-r_{1}(q)\right|^{\frac{1}{\beta_{1}}-1}, \text { if } k \leq k_{2, p}
\end{array}\right. \\
& \leq C \omega\left(\tau^{k}\right) \cdot\left\{\begin{array}{l}
\tau^{-k} d+\tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} d^{\frac{1}{\beta_{1}}-1}, \text { if } k \in\left[k_{2, p}+1, \ell\right] \\
r_{2}(p)^{\frac{1}{\beta_{2}}-1} \tau^{-\frac{k}{\beta_{2}}} d+r_{2}(p)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} d^{\frac{1}{\beta_{1}}-1}, \text { if } k \leq k_{2, p}
\end{array}\right.
\end{aligned}$$
To deal with the term $L_{3}^{\prime}$, we consider different cases of $k$, either $\ell \geq k \geq k_{2, p}+1$ or $k \leq k_{2, p}$.
- If $k_{2, p}+1 \leq k \leq \ell$, the balls $\hat{B}_{k}(p)$ are centered at $p_{1} \in \mathcal{S}_{1}$. Here $\tau^{-k} \leq \tau^{-\ell} \leq 8^{-1} d^{-1}$ and $\tau^{k} \leq \tau^{k_{2, p}+1} \leq \frac{1}{2} r_{2}(p)$, so $r_{2}(q) \geq-d+r_{2}(p) \geq \tau^{k}$. The balls $\hat{B}_{k}(p)$ are disjoint with $\mathcal{S}_{2}$, we can use the smooth coordinate $w_{2}=z_{2}^{\beta_{2}}$ as before. The functions $D_{w_{2}} D^{\prime} h_{k}$ are $g_{\beta}$-harmonic, hence by gradient estimate we have
$$\sup _{\frac{1}{1.2} \hat{B}_{k}(p) \backslash \mathcal{S}_{1}}\left|\nabla_{g_{\beta}}\left(D_{w_{2}} D^{\prime} h_{k}\right)\right| \leq C(n) \frac{\left\|D_{w_{2}} D^{\prime} h_{k}\right\|_{L^{\infty}\left(\frac{1}{1.1} \hat{B}_{k}(p)\right)}}{\tau^{k}} \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
From (3.88), we get that
$$\sup _{\frac{1}{1.2} \hat{B}_{k}(p) \backslash \mathcal{S}_{1}}\left|\frac{\partial^{2}}{\partial r_{1} \partial r_{2}} D^{\prime} h_{k}\right| \leq C(n) \tau^{-k} \omega\left(\tau^{k}\right) .$$
Recall $r_{1}(p)=r_{p} \leq 2 d \leq \frac{1}{2} \tau^{k}$, triangle inequality implies that $r_{1}(q) \leq 3 d \leq \frac{1}{2} \tau^{k}$. The points in $\gamma_{1}$ have the fixed $\left(r_{1}, \theta_{1}\right)$-coordinates $\left(r_{1}(q), \theta_{1}(q)\right)$, so integrating along $\gamma_{1}$ we get by (3.104) and (3.105) that
$$\begin{aligned}
L_{3}^{\prime} & \leq \int_{\gamma_{1}}\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|+\left|\frac{\partial}{r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|+\left|D^{\prime}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \\
& \leq C d \omega\left(\tau^{k}\right)\left(r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-k / \beta_{1}}+\tau_{1}(q)^{\frac{1}{\beta_{1}}-1} \min \left(r_{2}(p), r_{2}(q)\right)^{-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}+\tau^{-k}\right) \\
& \leq C \tau^{-k} \omega\left(\tau^{k}\right) \cdot d \leq C \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1} .
\end{aligned}$$
- If $k \leq k_{2, p}$, the $\tau^{k} \geq \tau^{k_{2, p}} \geq r_{2}(p)$ and $\tau^{k} \geq \tau^{\ell} \geq 8 d$. Thus $r_{2}(q) \leq r_{2}(p)+d \leq \frac{3}{2} \tau^{k}$. We choose points $\tilde{q}, \hat{q}$ as in (3.84), and let $\tilde{\gamma}_{1}, \tilde{\gamma}$ and $\hat{\gamma}$ be $g_{\boldsymbol{\beta}}$-geodesics defined as in the proof of Lemma 3.13. Then we have
$$\begin{aligned}
L_{3}^{\prime} \leq & \left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\left(q^{\prime}\right)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\tilde{q})\right|+\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\tilde{q})-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\hat{q})\right| \\
& +\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\hat{q})-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right|=: L_{1}^{\prime \prime}+L_{2}^{\prime \prime}+L_{3}^{\prime \prime} .
\end{aligned}$$
We will estimate $L_{1}^{\prime \prime}, L_{2}^{\prime \prime}$ and $L_{3}^{\prime \prime}$ term by term by integrating appropriate functions along the geodesics $\tilde{\gamma}_{1}, \tilde{\gamma}$ and $\hat{\gamma}$ as follows: The points in $\hat{\gamma}$ have fixed $\left(r_{1}, \theta_{1} ; r_{2} ; s\right)$-coordinates $\left(r_{1}(q), \theta_{1}(q) ; r_{2}(q) ; s(q)\right)$ and by (3.102)
$$\begin{aligned}
L_{3}^{\prime \prime} & =\left|\int_{\hat{\gamma}} \frac{\partial}{\partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d \theta_{2}\right| \leq C \omega\left(\tau^{k}\right) r_{1}(q)^{\frac{1}{\beta_{1}}-1} r_{2}(q)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} \\
& \leq C \omega\left(\tau^{k}\right) r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)} \leq C \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1} .
\end{aligned}$$
Integrating along $\tilde{\gamma}$ on which the points have constant $r_{1}$-coordinate $r_{1}(q)$, we get by (3.104)
$$\begin{aligned}
L_{2}^{\prime \prime} & =\left|\int_{\tilde{\gamma}} \frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right) d r_{2}\right| \\
& \leq C \omega\left(\tau^{k}\right)\left(r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-\frac{k}{\beta_{1}}}\left|r_{2}(q)-r_{2}(p)\right|+r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)}\left|r_{2}(q)^{\frac{1}{\beta_{2}}-1}-r_{2}(p)^{\frac{1}{\beta_{2}}-1}\right|\right) \\
& \leq C \omega\left(\tau^{k}\right)\left(r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-\frac{k}{\beta_{1}}} d+r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-2+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} d^{\frac{1}{\beta_{2}}-1}\right) \\
& \leq C \omega\left(\tau^{k}\right) r_{1}(q)^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}\right)} \leq C \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1} .
\end{aligned}$$

Integrating along $\tilde{\gamma}_{1}$ on which the points have constant $\left(r_{1}, \theta_{1} ; r_{2}, \theta_{2}\right)$-coordinates, we have by (3.71) that
$$\begin{aligned}
L_{1}^{\prime \prime} & \leq \int_{\tilde{\gamma}_{1}}\left|D^{\prime}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \leq C r_{1}(q)^{\frac{1}{\beta_{1}}-1} r_{2}(p)^{\frac{1}{\beta_{2}}-1} \tau^{-k\left(-1+\frac{1}{\beta_{1}}+\frac{1}{\beta_{2}}\right)} d \\
& \leq C d \tau^{-k} \omega\left(\tau^{k}\right) \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$

Combining both cases, we conclude that $L_{3}^{\prime} \leq C \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) d^{\frac{1}{\beta_{1}}-1}$. Then by the estimates above for $L_{1}^{\prime}$ and $L_{2}^{\prime}$, we finally get for all $k \leq \ell$
$$\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} d^{\frac{1}{\beta_{1}}-1} \leq C \omega\left(\tau^{k}\right) \tau^{-k\left(\frac{1}{\beta_{\max }}-1\right)} d^{\frac{1}{\beta_{\max }}-1},$$
where in the last inequality we use the fact that $\tau^{-k} d \leq 1 / 8<1$, when $k \leq \ell$. Hence we finish the proof of Lemma 3.22 in case $r_{p} \leq 2 d$.

Now we deal with the remaining cases.
- Case 2: here we assume $\min \left(r_{p}, r_{q}\right)=r_{p} \geq 2 d$ and $\ell \leq k_{p}$. In this case $\tau^{k_{p}} \approx r_{p} \geq 2 d \geq \tau^{\ell+3}$, so $\ell+3 \geq k_{p}$. It follows by triangle inequality that $d_{\boldsymbol{\beta}}(\gamma(t), \mathcal{S}) \geq d$, where $\gamma$ is the $g_{\boldsymbol{\beta}}$-geodesic joining $p$ to $q$ as before. In particular this implies that $\min \left(r_{1}(\gamma(t)), r_{2}(\gamma(t))\right) \geq d$.

In this case $\ell \leq k_{p}$, Lemmas 3.17-3.21 hold for all $k \leq \ell$ and $r_{1}(p) \approx \tau^{k_{p}} \leq \tau^{\ell}$, so $r_{1}(\gamma(t)) \leq$ $d+r_{1}(p) \leq \frac{9}{8} \tau^{\ell} \leq \frac{9}{8} \tau^{k}$. We calculate the gradient of $\frac{\partial^{2} h_{k}}{\partial r_{1} \partial 2}$ along the geodesic $\gamma$ as follows
$$\begin{aligned}
\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right|^{2}(\gamma(t))= & \left|\frac{\partial}{\partial r_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2}+\left|\frac{1}{\beta_{1} r_{1} \partial \theta_{1}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2}+\left|\frac{\partial}{\partial r_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2} \\
& +\left|\frac{\partial}{\beta_{2} r_{2} \partial \theta_{2}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2}+\sum_{j}\left|\frac{\partial}{\partial s_{j}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right|^{2} .
\end{aligned}$$
(1). When $k_{2, p}+1 \leq k \leq \ell$ we have along $\gamma$
$$r_{2}(\gamma(t)) \geq r_{2}(p)-d \geq \tau^{k}-d \geq \frac{7}{8} \tau^{k} .$$
Then by Lemmas 3.17-3.21 we have along $\gamma$ that
$$\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(\gamma(t))\right| \leq C \omega\left(\tau^{k}\right)\left(\tau^{-k}+d^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}\right)$$
Integrating this inequality along $\gamma$ we get
$$\begin{aligned}
\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| & \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq C \omega\left(\tau^{k}\right)\left(d \tau^{-k}+d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}\right) \\
& \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .
\end{aligned}$$
(2). When $k \leq k_{2, p}$, we have along $\gamma$
$$r_{2}(\gamma(t)) \leq r_{2}(p)+d \leq \tau^{k}+d \leq \frac{9}{8} \tau^{k} .$$
Then by Lemmas 3.17-3.21 we have along $\gamma$ that
$$\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq C \omega\left(\tau^{k}\right)\left(\tau^{-k}+d^{\frac{1}{\beta_{1}}-2} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)}\right)$$

Integrating this inequality along $\gamma$ we again get
$$\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .$$
- Case 3: here we assume $\min \left(r_{p}, r_{q}\right)=r_{p} \geq 2 d$, but $\ell \geq k_{p}+1$. The case when $k \leq k_{p}$ can be dealt with by the same argument as in Case 2, so we omit it and only consider the cases when $k_{p}+1 \leq k \leq \ell$, so here $r_{2}(p) \geq r_{1}(p) \geq \tau^{k} \geq \tau^{\ell}>8 d$ so $r_{1}(\gamma(t)) \geq \frac{7}{8} \tau^{k}$ and $r_{2}(\gamma(t)) \geq \frac{7}{8} \tau^{k}$ for any point $\gamma(t)$ in the geodesic $\gamma$. By triangle inequality it follows that $\gamma \subset \frac{1}{3} \hat{B}_{k}(p)=B_{\boldsymbol{\beta}}\left(p, \tau^{k} / 3\right)$.

As before, we can introduce smooth coordinates $w_{1}=z_{1}^{\beta_{1}}$ and $w_{2}=z_{2}^{\beta_{2}}$, and $g_{\boldsymbol{\beta}}$ becomes the standard smooth Euclidean metric $g_{\mathbb{C}^{n}}$ under these coordinates. Moreover, $h_{k}$ are the usual Euclidean harmonic function $\Delta_{g_{\mathrm{C}} n} h_{k}=0$ on $\hat{B}_{k}(p)$. By the standard derivative estimates we have
$$\sup _{\frac{1}{2} \hat{B}_{k}(p)}\left(\left|D_{w_{1}, w_{2}}^{3} h_{k}\right|+\left|D^{\prime}\left(D_{w_{1}, w_{2}}^{2}\right) h_{k}\right|\right) \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
From the equation
$$\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}=\frac{w_{1} w_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial w_{1} \partial w_{2}}+\frac{\bar{w}_{1} w_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial \bar{w}_{1} \partial w_{2}}+\frac{w_{1} \bar{w}_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial w_{1} \partial \bar{w}_{2}}+\frac{\bar{w}_{1} \bar{w}_{2}}{r_{1} r_{2}} \frac{\partial^{2} h_{k}}{\partial \bar{w}_{1} \partial \bar{w}_{2}}$$
we see that for $i=1,2$
$$\sup _{\frac{1}{2} \hat{B}_{k}(p)}\left|\frac{\partial}{\partial w_{i}}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \leq \frac{C}{r_{i}} \omega\left(\tau^{k}\right)+C \tau^{-k} \omega\left(\tau^{k}\right), \quad \sup _{\frac{1}{2} \hat{B}_{k}(p)}\left|D^{\prime}\left(\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right)\right| \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
From this we see that
$$\sup _{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq \sup _{\gamma}\left(C \tau^{-k} \omega\left(\tau^{k}\right)+\frac{C}{r_{1}} \omega\left(\tau^{k}\right)+\frac{C}{r_{2}} \omega\left(\tau^{k}\right)\right) \leq C \tau^{-k} \omega\left(\tau^{k}\right) .$$
Integrating along $\gamma$ we see that
$$\left|\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}(q)\right| \leq \int_{\gamma}\left|\nabla_{g_{\beta}} \frac{\partial^{2} h_{k}}{\partial r_{1} \partial r_{2}}\right| \leq C d \tau^{-k} \omega\left(\tau^{k}\right) \leq C d^{\frac{1}{\beta_{1}}-1} \tau^{-k\left(\frac{1}{\beta_{1}}-1\right)} \omega\left(\tau^{k}\right) .$$

Combining the estimates in all three cases, we finish the proof of Lemma 3.22. \(\square\)

By Lemma 3.22 it follows that
$$L_{2}=\left|\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{\ell}}{\partial r_{1} \partial r_{2}}(q)\right| \leq\left|\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(q)\right|+C d^{\frac{1}{\beta_{\max }}-1} \sum_{k=3}^{\ell} \tau^{-k\left(\frac{1}{\beta_{\max }}-1\right)} \omega\left(\tau^{k}\right) .$$
To finish the proof, it suffices to estimate the first term on the RHS of the above equation. Recall we assume $u_{2}$ is a $g_{\beta}$-harmonic function defined on the ball $\hat{B}_{2}(p)$, which is centered at $p_{1,2} \in \mathcal{S}_{1} \cap \mathcal{S}_{2}$ and has radius $2 \tau^{2} . u_{2}$ satsifies the $L^{\infty}$ estimate by maximum principle: there exists some $C=C(n)>0$ such that
$$\left\|u_{2}\right\|_{L^{\infty}\left(\hat{B}_{k}(p)\right)} \leq C\left(\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\omega\left(\tau^{2}\right)\right) .$$
Recall that the proofs of the estimates in Lemmas 3.17-3.21 in the case when $k \leq k_{2, p}$ work for any $g_{\boldsymbol{\beta}}$-harmonic functions defined on suitable balls, and we can repeat the arguments there replacing the $L^{\infty}$-estimates of $h_{k}$ that $\left\|h_{k}\right\|_{L^{\infty}} \leq C \tau^{2 k} \omega\left(\tau^{k}\right)$, by the $L^{\infty}$-estimate of $u_{2}$ as in (3.107), to get
similar estimates as in those lemmas, which we will not repeat here. Given these estimates, we can repeat the proof of Lemma 3.22 to prove the following estimates
$$\left|\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u_{2}}{\partial r_{1} \partial r_{2}}(q)\right| \leq C d^{\frac{1}{\beta_{\max }}-1}\left(\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\omega\left(\tau^{2}\right)\right) .$$
This inequality, combined with (3.106) give the final estimate of the term $L_{2}$, that
$$L_{2} \leq C d^{\frac{1}{\beta_{\max }}-1}\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+C d^{\frac{1}{\beta_{\max }}-1} \sum_{k=2}^{\ell} \tau^{-k\left(\frac{1}{\beta_{\max }}-1\right)} \omega\left(\tau^{k}\right) .$$

By Lemma 3.15, Lemma 3.16 and the estimate (3.108) for $L_{2}$, we are ready to prove the following estimate (see the equation (1.5))

Proposition 3.5. For the given $p, q \in B_{\boldsymbol{\beta}}(0,1 / 2) \backslash \mathcal{S}$, there is a constant $C=C(n, \boldsymbol{\beta})>0$ such that
$$\left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| \leq C\left(d^{\frac{1}{\beta_{\max }}-1}\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{\frac{1}{\beta_{\max }}}-1 \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\max }}} d r\right) .$$
Proof. From Lemma 3.15, Lemma 3.16 and the estimate (3.108) for $L_{2}$, we have
$$\begin{aligned}
& \left|\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(p)-\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}(q)\right| \\
\leq & C\left(d^{\frac{1}{\beta_{\text {max }}}}-1\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+d^{\frac{1}{\beta_{\text {max }}}}-1 \sum_{k=2}^{\ell} \tau^{-k\left(\frac{1}{\beta_{\text {max }}}-1\right)} \omega\left(\tau^{k}\right)+\sum_{k=\ell}^{\infty} \omega\left(\tau^{k}\right)\right) \\
\leq & C\left(d^{\frac{1}{\beta_{\text {max }}}}-1\|u\|_{L^{\infty}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\int_{0}^{d} \frac{\omega(r)}{r} d r+d^{\frac{1}{\beta_{\text {max }}}-1} \int_{d}^{1} \frac{\omega(r)}{r^{1 / \beta_{\text {max }}}} d r\right),
\end{aligned}$$
where the last inequality follows from the fact that $\omega(r)$ is monotonically increasing. \(\square\)

Finally, we remark that the estimates for the other operators in (3.89) follows similarly, so we omit the detailed proof and just state that the estimates are the same as the estimates for $\frac{\partial^{2} u}{\partial r_{1} \partial r_{2}}$ as in Proposition 3.5.

\subsection*{3.5. Non-flat conical Kähler metrics}

In this section, we will consider the Schauder estimates for general conical Kähler metrics on $B_{\boldsymbol{\beta}}(0,2) \subset \mathbb{C}^{n}$ with cone angle $2 \pi \boldsymbol{\beta}$ along the simple normal crossing hyper-surface $\mathcal{S}$. Let $\omega$ be such a metric. By definition, there exists a constant $C \geq 1$ such that
$$C^{-1} \omega_{\boldsymbol{\beta}} \leq \omega \leq C \omega_{\boldsymbol{\beta}}, \quad \text { in } B_{\boldsymbol{\beta}}(0,2) \backslash \mathcal{S},$$
where $\omega_{\boldsymbol{\beta}}$ is the standard flat conical metric as before. Since $\omega$ is closed and $B_{\boldsymbol{\beta}}(0,2)$ is simply connected, we can write $\omega=\sqrt{-1} \partial \bar{\partial} \phi$ for some strictly pluri-subharmonic function $\phi$. By elliptic regularity, $\phi$ is Holder continuous under the Euclidean metric on $B_{\boldsymbol{\beta}}(0,2)$.

We fix an $\alpha \in\left(0, \min \left\{\frac{1}{\beta_{\text {max }}}-1,1\right\}\right)$.
Definition 3.1. We say $\omega=g$ a $C_{\boldsymbol{\beta}}^{0, \alpha}$ Kähler metric on $B_{\boldsymbol{\beta}}(0,2)$ if it satisfies (3.109) and the Kähler potential $\phi$ of $\omega$ belongs to $C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,2)\right)$.

Our interest is to study the Laplacian equation
$$\Delta_{g} u=f, \quad \text { in } B_{\boldsymbol{\beta}}(0,1),$$
where $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ and $u \in C_{\boldsymbol{\beta}}^{2, \alpha}$. We will prove the following scaling-invariant interior Schauder estimates, and the proof follows closely from that of Theorem 6.6 in [19]. So we mainly focus on the differences.

Proposition 3.6. There exists a constant $C=C\left(n, \boldsymbol{\beta},\|g\|_{C_{\boldsymbol{\beta}}^{0, \alpha}}^{*}\right)>0$ such that if $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)$ satisfies the equation (3.110), then
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}^{*} \leq C\left(\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}^{(2)}\right) .$$
Proof. Given any points $x_{0} \neq y_{0} \in B_{\boldsymbol{\beta}}(0,1)$, assume $d_{x_{0}}=\min \left(d_{x_{0}}, d_{y_{0}}\right)$ (recall $d_{x}=d_{\boldsymbol{\beta}}\left(x, \partial B_{\boldsymbol{\beta}}(0,1)\right)$ ). Let $\mu \in(0,1 / 4)$ be a small number to be determined later. Denote $d=\mu d_{x_{0}}$ and $B:=B_{\boldsymbol{\beta}}\left(x_{0}, d\right)$, and $\frac{1}{2} B:=B_{\boldsymbol{\beta}}\left(x_{0}, d / 2\right)$.
- Case 1. $d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)<d / 2$.

Case 1.1. $B_{\boldsymbol{\beta}}\left(x_{0}, d\right) \cap \mathcal{S}=\emptyset$. On $B_{\boldsymbol{\beta}}\left(x_{0}, d\right)$ we can introduce the smooth complex coordinates $\left\{w_{1}=z_{1}^{\beta_{1}}, w_{2}=z_{2}^{\beta_{2}}, z_{3}, \ldots, z_{n}\right\}$, under which $g_{\boldsymbol{\beta}}$ becomes the Euclidean one and the components of $g$ become $C^{\alpha}$ in the usual sense. The equation (3.110) has $C^{\alpha}$ leading coefficients and we can apply Theorem 6.6 in [19] to conclude that (the following inequality is understood in the new coordinates)
$$[u]_{C^{2, \alpha}(B)}^{*} \leq C\left(\|u\|_{C^{0}(B)}+\|f\|_{C^{0, \alpha}(B)}^{(2)}\right) .$$
Recall $T$ denotes the second order operators appearing in (2.1). Let $D$ denote the ordinary first order operators in $\left\{w_{1}, w_{2}, z_{3}, \ldots, z_{n}\right\}$. Then we calculate
$$\begin{aligned}
\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right| & \leq\left|D^{2} u\left(x_{0}\right)-D^{2} u\left(y_{0}\right)\right|+\frac{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)}{d}\left(\left|D^{2} u\left(x_{0}\right)\right|+\left|D^{2} u\left(y_{0}\right)\right|\right) \\
& \leq \frac{4 d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}}{d^{2+\alpha}}[u]_{C^{2, \alpha}(B)}^{*}+\frac{4 d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)}{d^{3}}[u]_{C^{2}(B)}^{*}
\end{aligned}$$
$($ by interpolation inequality $) \leq \frac{8 d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}}{d^{2+\alpha}}[u]_{C^{2, \alpha}(B)}^{*}+C \frac{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}}{d^{2+\alpha}}\|u\|_{C^{0}(B)}$.
Then we get
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}} \leq \frac{C}{\mu^{2+\alpha}}\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(B)}^{(2)}+\frac{C}{\mu^{2+\alpha}}\|u\|_{C^{0}(B)} .$$

Case 1.2: $B_{\boldsymbol{\beta}}\left(x_{0}, d\right) \cap \mathcal{S} \neq \emptyset$. Let $\hat{x}_{0} \in \mathcal{S}$ be the nearest point of $x_{0}$ to $\mathcal{S}$. We consider the balls $\hat{B}:=B_{\boldsymbol{\beta}}\left(\hat{x}_{0}, 2 d\right)$ which is contained in $B_{\boldsymbol{\beta}}(0,1)$ by triangle inequality. As in [14], we introduce a (non-holomorphic) basis of $T_{1,0}^{*}\left(\mathbb{C}^{n} \backslash \mathcal{S}\right)$ as
$$\left\{\epsilon_{j}:=d r_{j}+\sqrt{-1} \beta_{j} r_{j} d \theta_{j}, d z_{k}\right\}_{j=1,2 ; k=3, \ldots, n}$$
and the dual basis of $T_{1,0}\left(\mathbb{C}^{n} \backslash \mathcal{S}\right)$ :
$$\left\{\gamma_{j}:=\frac{\partial}{\partial r_{j}}-\sqrt{-1} \frac{1}{\beta_{j} r_{j}} \frac{\partial}{\partial \theta_{j}}, \frac{\partial}{\partial z_{k}}\right\}_{j=1,2 ; k=3, \ldots, n} .$$
We can write the (1,1)-form $\omega$ in the basis $\left\{\epsilon_{j} \wedge \bar{\epsilon}_{k}, \epsilon_{j} \wedge d \bar{z}_{k}, d z_{k} \wedge \bar{\epsilon}_{j}, d z_{j} \wedge d \bar{z}_{k}\right\}$ as
$$\omega=g_{\epsilon_{j} \bar{\epsilon}_{k}} \epsilon_{j} \wedge \bar{\epsilon}_{k}+g_{\epsilon_{j} \bar{k}} \epsilon_{j} \wedge d \bar{z}_{k}+g_{k \bar{\epsilon}_{j}} d z_{k} \wedge \bar{\epsilon}_{j}+g_{j \bar{k}} d z_{j} \wedge d \bar{z}_{k},$$
where
$$g_{\epsilon_{j} \bar{\epsilon}_{k}}=\sqrt{-1} \partial \bar{\partial} \phi\left(\gamma_{j}, \bar{\gamma}_{k}\right), g_{\epsilon_{j} \bar{k}}=\sqrt{-1} \partial \bar{\partial} \phi\left(\gamma_{j}, \frac{\partial}{\partial \bar{z}_{k}}\right), g_{k \bar{\epsilon}_{j}}=\sqrt{-1} \partial \bar{\partial}\left(\frac{\partial}{\partial z_{k}}, \bar{\gamma}_{j}\right), g_{k \bar{j}}=\frac{\partial^{2}}{\partial z_{k} \partial \bar{z}_{j}} \phi .$$
We remark that all the second order derivatives of $\phi$ appearing in (3.115) are linear combination of $\left|z_{j}\right|^{2-2 \beta_{j}} \frac{\partial^{2}}{\partial z_{j} \partial z_{\bar{j}}} N_{j} N_{k}(j \neq k), N_{j} D^{\prime}$ and $\left(D^{\prime}\right)^{2}$, which are studied in Theorem 1.1. The standard metric $\omega_{\boldsymbol{\beta}}$ becomes the identity matrix under the basis above for (1, 1)-forms. If $\omega$ is $C_{\boldsymbol{\beta}}^{0, \alpha}$, all the coefficients in the expression of $\omega$ in (3.114) are $C_{\boldsymbol{\beta}}^{0, \alpha}$ continuous and the cross terms $g_{\epsilon_{j} \bar{\epsilon}_{k}}$ with $j \neq k, g_{\epsilon_{j} \bar{k}}$ tend to zero when approaching the corresponding singular sets $\mathcal{S}_{j}$ or $\mathcal{S}_{k}$. Moreover, the limit of $g_{j \bar{k}} d z_{j} \wedge d \bar{z}_{k}$ as tending to $\mathcal{S}_{1} \cap \ldots \cap \mathcal{S}_{p}$ defines a Kähler metric on it. Rescaling or rotating the coordinates if necessary we may assume at $\hat{x}_{0} \in \mathcal{S}, g_{\epsilon_{j} \bar{\epsilon}_{j}}\left(\hat{x}_{0}\right)=1, g_{j \bar{k}}\left(\hat{x}_{0}\right)=\delta_{j k}$ and the cross terms vanish at $\hat{x}_{0}$. Let $\omega_{\boldsymbol{\beta}}$ be the standard cone metric under these new coordinates near $\hat{x}_{0}$, and we can write the equation (3.110) as
$$\Delta_{g} u(z)=\Delta_{g_{\beta}} u(z)+\eta(z) \cdot i \partial \bar{\partial} u(z)=f(z), \quad \forall z \notin \mathcal{S}$$
for some Hermtian matrix $\eta(z)=\left(\eta^{j \bar{k}}\right)_{j, k=1}^{n}, \eta^{j \bar{k}}=g^{j \bar{k}}(z)-g_{\boldsymbol{\beta}}^{j \bar{k}}$. It is not hard to see the term $\eta(z) . i \partial \bar{\partial} u$ can be written as
$$\sum_{j, k=1}^{2}\left(g^{\epsilon_{j} \bar{\epsilon}_{k}}(z)-\delta_{j k}\right) u_{\epsilon_{j} \bar{\epsilon}_{j}}+2 \operatorname{Re} \sum_{1 \leq j \leq 2,3 \leq k \leq n} g^{\epsilon_{j} \bar{k}} u_{\epsilon_{j} \bar{k}}+\sum_{j, k=3}^{n}\left(g^{j \bar{k}}(z)-\delta_{j k}\right) u_{j \bar{k}},$$
and $g$ with the upper indices denotes the inverse matrix of $g$. We consider the equivalent form of the equation (3.110) on $\hat{B}$,
$$\Delta_{g_{\beta}} u=f-\eta \cdot \sqrt{-1} \partial \bar{\partial} u=: \hat{f}, \quad u \in C^{0}(\hat{B}) \cap C^{2}(\hat{B} \backslash \mathcal{S}) .$$
Observe that $x_{0}, y_{0} \in B_{\boldsymbol{\beta}}\left(\hat{x}_{0}, 3 d / 2\right)$ we can apply the scaled inequality (1.7) of Theorem 1.1 to conclude that
$$d^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}} \leq C\left(\|u\|_{C^{0}(\hat{B})}+\|\hat{f}\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(\hat{B})}^{(2)}\right),$$
thus
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}} \leq \frac{C}{\mu^{2+\alpha}}\left(\|u\|_{C^{0}(\hat{B})}+\|\hat{f}\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(\hat{B})}^{(2)}\right) .$$
- Case 2. $d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right) \geq d / 2$.
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}} \leq 4 d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)\right|+\left|T u\left(y_{0}\right)\right|}{d^{\alpha}} \leq \frac{8}{\mu^{\alpha}}[u]_{C_{\boldsymbol{\beta}}^{2}\left(B_{\boldsymbol{\beta}}(0,1)\right)}^{*} .$$
Combining (3.113), (3.117) and (3.118) we get
$$\begin{aligned}
d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}} \leq & \frac{8}{\mu^{\alpha}}[u]_{C_{\boldsymbol{\beta}}^{2}\left(B_{\boldsymbol{\beta}}(0,1)\right)}^{*}+\frac{C}{\mu^{2+\alpha}}\left(\|u\|_{C^{0}(\hat{B})}+\|\hat{f}\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(\hat{B})}^{(2)}\right) \\
& +\frac{C}{\mu^{2+\alpha}}\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(B)}^{(2)}+\frac{C}{\mu^{2+\alpha}}\|u\|_{C^{0}(B)} .
\end{aligned}$$
By definition it is easy to see that (we denote $B_{\boldsymbol{\beta}}=B_{\boldsymbol{\beta}}(0,1)$ )
$$\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(B)}^{(2)} \leq C \mu^{2}\|f\|_{C^{0}\left(B_{\boldsymbol{\beta}}\right)}^{(2)}+C \mu^{2+\alpha}[f]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2)} \leq \mu^{2}\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2)} .$$

We calculate
$$\begin{aligned}
\|\hat{f}\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(\hat{B})}^{(2)} \leq & \|\eta\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(\hat{B})}^{(0)}\|T u\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(\hat{B})}^{(2)}+\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}(\hat{B})}^{(2)} \\
\leq & C_{0}[g]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*} \mu^{\alpha}\left(\mu^{2}[u]_{C_{\boldsymbol{\beta}}^{2}\left(B_{\boldsymbol{\beta}}\right)}^{*}+\mu^{2+\alpha}[u]_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*}\right)+\mu^{2}\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2)} \\
\leq & C_{0}[g]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*} \mu^{\alpha}\left(C(\mu)\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}\right)}+2 \mu^{2+\alpha}[u]_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*}\right)+\mu^{2}\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2)} . \\
& \quad \frac{8}{\mu^{\alpha}}[u]_{C_{\boldsymbol{\beta}}^{2}\left(B_{\boldsymbol{\beta}}\right)}^{*} \leq \mu^{\alpha}[u]_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*}+C(\mu)\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}\right)} .
\end{aligned}$$
If we choose $\mu>0$ small such that $\mu^{\alpha}\left(2 C_{0}[g]_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*}+1\right) \leq 1 / 2$, then we get from (3.119) and the inequalities above that
$$d_{x_{0}}^{2+\alpha} \frac{\left|T u\left(x_{0}\right)-T u\left(y_{0}\right)\right|}{d_{\boldsymbol{\beta}}\left(x_{0}, y_{0}\right)^{\alpha}} \leq \frac{1}{2}[u]_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*}+C(\mu)\left(\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}\right)}+\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2)}\right) .$$
Taking supremum over $x_{0} \neq y_{0} \in B_{\boldsymbol{\beta}}(0,1)$ we conclude from the inequality above that
$$[u]_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{*} \leq C\left(\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}\right)}+\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2)}\right) .$$
Proposition 3.6 then follows from interpolation inequalities. \(\square\)

Remark 3.4. It follows easily from the proof of Proposition 3.6 that the estimate (3.111) also holds for metric balls $B_{\boldsymbol{\beta}}(p, R) \subset B_{\boldsymbol{\beta}}(0,1)$ whose center $p$ may not lie at $\mathcal{S}$.

An immediate corollary to Proposition 3.6 is the following interior Schauder estimate.
Corollary 3.1. Suppose $u$ satisfies the equation (3.110). For any compact subset $K \Subset B_{\boldsymbol{\beta}}(0,1)$, there exists a constant $C=C\left(n, \boldsymbol{\beta}, K,\|g\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}\right)>0$ such that
$$\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}(K)} \leq C\left(\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}(0,1)\right)}+\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}(0,1)\right)}\right) .$$
Next we will show that the equation (3.110) admits a unique $C_{\boldsymbol{\beta}}^{2, \alpha}$-solution for any $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}(0,1)}\right)$ and boundary value $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}(0,1)\right)$. We will follow the argument in Section 6.5 in [19]. In the following we will write $B_{\boldsymbol{\beta}}=B_{\boldsymbol{\beta}}(0,1)$ for simplicity.

Lemma 3.23. Let $\sigma \in(0,1)$ be a given number. Suppose $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)$ solves (3.110) and $\|u\|_{C^{0}\left(B_{\boldsymbol{\beta}}\right)}^{(-\sigma)}<\infty$ and $\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2-\sigma)}<\infty$. Then there exists a $C=C(n, \boldsymbol{\beta}, \alpha, g, \sigma)>0$ such that
$$\|u\|_{C_{\beta}^{2, \alpha}\left(B_{\beta}\right)}^{(-\sigma)} \leq C\left(\|u\|_{C^{0}\left(B_{\beta}\right)}^{(-\sigma)}+\|f\|_{C_{\beta}^{0, \alpha}\left(B_{\beta}\right)}^{(2 \sigma)}\right) .$$
Proof. Given the estimates in Proposition 3.6, the proof is identical to that of Lemma 6.20 in [19]. So we omit the details. \(\square\)

Lemma 3.24. Let $u \in C_{\boldsymbol{\beta}}^{2}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ solve the equation $\Delta_{g} u=f$ and $u \equiv 0$ on $\partial B_{\boldsymbol{\beta}}$. For any $\sigma \in(0,1)$, there exists a constant $C=C(n, \boldsymbol{\beta}, \sigma, g)>0$ such that
$$\|u\|_{C^{0}\left(B_{\beta}\right)}^{(-\sigma)}=\sup _{x \in B_{\beta}} d_{x}^{-\sigma}|u(x)| \leq C \sup _{x \in B_{\beta}} d_{x}^{2-\sigma}|f(x)|=C\|f\|_{C^{0}\left(B_{\beta}\right)}^{(2-\sigma)},$$
where as before $d_{x}=d_{\boldsymbol{\beta}}\left(x, \partial B_{\boldsymbol{\beta}}\right)$.

Proof. Consider the function $w_{1}=\left(1-d_{\boldsymbol{\beta}}^{2}\right)^{\sigma}$ where $d_{\boldsymbol{\beta}}(x)=d_{\boldsymbol{\beta}}(x, 0)$. We calculate
$$\begin{aligned}
\Delta_{g} w_{1} & =\sigma\left(1-d_{\boldsymbol{\beta}}^{2}\right)^{\sigma-2}\left(-\left(1-d_{\boldsymbol{\beta}}^{2}\right) \operatorname{tr}_{g} g_{\boldsymbol{\beta}}-(1-\sigma)\left|\nabla d_{\boldsymbol{\beta}}^{2}\right|_{g}^{2}\right) \\
& \leq \sigma\left(1-d_{\boldsymbol{\beta}}^{2}\right)^{\sigma-2}\left(-C^{-1}\left(1-d_{\boldsymbol{\beta}}^{2}\right)-4 C^{-1} d_{\boldsymbol{\beta}}^{2}(1-\sigma)\right) \\
& \leq-c_{0} \sigma\left(1-d_{\boldsymbol{\beta}}^{2}\right)^{\sigma-2} .
\end{aligned}$$
Take a large constant $A>1$ such that for $w=A w_{1}$
$$\Delta_{g} w \leq-\left(1-d_{\boldsymbol{\beta}}\right)^{\sigma-2} \leq-|f| / N, \quad \text { in } B_{\boldsymbol{\beta}},$$
where $N=\sup _{x \in B_{\boldsymbol{\beta}}} d_{x}^{2-\sigma}|f(x)|=\sup _{x \in B_{\boldsymbol{\beta}}}\left(1-d_{\boldsymbol{\beta}}(x)\right)^{2-\sigma}|f(x)|$. Hence $\Delta_{g}(N w \pm u) \leq 0$ and from the definition of $w$ we also have $\left.w\right|_{\partial B_{\beta}} \equiv 0$, by maximum principle we obtain that $|u(x)| \leq N w \leq$ $C N\left(1-d_{\boldsymbol{\beta}}(x)\right)^{\sigma}=C N d_{x}^{\sigma}$, hence the lemma is proved. \(\square\)

Proposition 3.7. Given any function $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}}\right)$, the Dirichlet problem $\Delta_{g} u=f$ in $B_{\boldsymbol{\beta}}$ and $u \equiv 0$ on $\partial B_{\boldsymbol{\beta}}$ admits a unique solution $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$.

Proof. The proof of this proposition is almost identical to that of Theorem 6.22 in [19]. For completeness, we provide the detailed argument. Fix a $\sigma \in(0,1)$. We define a family of operators $\Delta_{t}=t \Delta_{g}+(1-t) \Delta_{g_{\beta}}$ and it is straightforward to see that $\Delta_{t}$ is associated to some cone metric which also satisfies (3.109). We study the Dirichlet problem
$$\Delta_{t} u_{t}=f, \text { in } B_{\boldsymbol{\beta}}, \quad u_{t} \equiv 0 \text { on } \partial B_{\boldsymbol{\beta}} .$$
Equation $\left(*_{0}\right)$ admits a unique solution $u_{0} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ by Proposition 3.2. By Theorem 5.2 in [19], in order to apply the continuity method to solve $\left(*_{1}\right)$, it suffices to show $\Delta_{t}^{-1}$ defines a bounded linear operator between some Banach spaces. More precisely, define
$$\begin{aligned}
& \mathcal{B}_{1}:=\left\{u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right) \mid\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(\sigma)}<\infty\right\}, \\
& \mathcal{B}_{2}:=\left\{f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right) \mid\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2-\sigma)}<\infty\right\} .
\end{aligned}$$
By definition any $u \in \mathcal{B}_{1}$ is continuous on $\overline{B_{\boldsymbol{\beta}}}$ and $u=0$ on $\partial B_{\boldsymbol{\beta}}$. By Lemmas 3.23 and 3.24, we have
$$\|u\|_{\mathcal{B}_{1}}=\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(-\sigma)} \leq C\|f\|_{C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)}^{(2 \sigma)}=C\left\|\Delta_{t} u\right\|_{\mathcal{B}_{2}},$$
for some constant $C$ independent of $t \in[0,1]$. Thus ( $*_{1}$ ) admits a solution $u \in \mathcal{B}_{1}$. \(\square\)

Corollary 3.2. For any given $\varphi \in C^{0}\left(\partial B_{\boldsymbol{\beta}}\right)$ and $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(\overline{B_{\boldsymbol{\beta}}}\right)$, the Dirichlet problem
$$\Delta_{g} u=f, \text { in } B_{\boldsymbol{\beta}}, \text { and } u=\varphi \text {, on } \partial B_{\boldsymbol{\beta}},$$
admits a unique solution $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$.
Proof. We may extend $\varphi$ continuously to $B_{\boldsymbol{\beta}}$ and assume $\varphi \in C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$. Take a sequence of functions $\varphi_{k} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(\overline{B_{\boldsymbol{\beta}}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ which converges uniformly to $\varphi$ on $\overline{B_{\boldsymbol{\beta}}}$. The Dirichlet problem $\Delta_{g} v_{k}=$ $f-\Delta_{g} \varphi_{k}$ in $B_{\boldsymbol{\beta}}$ and $v_{k}=0$ on $\partial B_{\boldsymbol{\beta}}$ admits a unique solution $v_{k} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$. Thus the function $u_{k}:=v_{k}+\varphi_{k} \in C_{\boldsymbol{\beta}}^{2, \alpha}$ satisfies $\Delta_{g} u_{k}=f$ in $B_{\boldsymbol{\beta}}$ and $u_{k}=\varphi_{k}$ on $\partial B_{\boldsymbol{\beta}}$. $u_{k}$ is uniformly bounded in $C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ by maximum principle. Corollary 3.1 gives uniformly $C_{\boldsymbol{\beta}}^{2, \alpha}(K)$-bound on any compact subset $K \Subset B_{\boldsymbol{\beta}}$. Letting $k \rightarrow \infty$ and $K \rightarrow B_{\boldsymbol{\beta}}$, by a diagonal argument and up to a subsequence $u_{k} \rightarrow u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)$. On the other hand, from $\Delta_{g}\left(u_{k}-u_{l}\right)=0$ we see that $\left\{u_{k}\right\}$ is
a Cauchy sequence in $C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ thus $u_{k}$ converges uniformly to $u$ on $\overline{B_{\boldsymbol{\beta}}}$. Hence $u \in C^{0}\left(\overline{B_{\boldsymbol{\beta}}}\right)$ and satisfies the equation (3.120). \(\square\)

Corollary 3.3. Given $f \in C_{\boldsymbol{\beta}}^{0, \alpha}\left(B_{\boldsymbol{\beta}}\right)$, suppose $u$ is a weak solution to the equation $\Delta_{g} u=f$ in the sense that
$$\int_{B_{\boldsymbol{\beta}}}\langle\nabla u, \nabla \varphi\rangle \omega_{g}^{n}=-\int_{B_{\boldsymbol{\beta}}} f \varphi \omega_{g}^{n}, \quad \forall \varphi \in H_{0}^{1}\left(B_{\boldsymbol{\beta}}\right),$$
then $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)$.
Proof. We first observe that the Sobolev inequality (3.43) also holds for the metric $g$, since $g$ is equivalent to $g_{\boldsymbol{\beta}}$. The metric space $\left(B_{\boldsymbol{\beta}}, g\right)$ also has maximal volume growth/decay, so we can apply the same proof of De Giorgi-Nash-Moser theory ([22]) to conclude that $u$ is continuous in $B_{\boldsymbol{\beta}}$. The standard elliptic theory implies that $u \in C_{\text {loc }}^{2, \alpha}\left(B_{\boldsymbol{\beta}} \backslash \mathcal{S}\right)$. For any $r \in(0,1)$, by Corollary 3.2, the Dirichlet problem $\Delta_{g} \tilde{u}=f$ in $B_{\boldsymbol{\beta}}(0, r), \tilde{u}=u$ on $\partial B_{\boldsymbol{\beta}}(0, r)$ admits a unique solution $\tilde{u} \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right) \cap C^{0}\left(\overline{B_{\boldsymbol{\beta}}(0, r)}\right)$. Then $\Delta_{g}(u-\tilde{u})=0$ in $B_{\boldsymbol{\beta}}(0, r)$ and $u-\tilde{u}=0$ on $\partial B_{\boldsymbol{\beta}}(0, r)$. By maximum principle we get $u=\tilde{u}$ in $B_{\boldsymbol{\beta}}(0, r)$, so we conclude $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}(0, r)\right)$. Since $r \in(0,1)$ is arbitrary, we get $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{\boldsymbol{\beta}}\right)$. \(\square\)

Corollary 3.4. Let $X$ be a compact Kähler manifold and $D=\sum_{j} D_{j}$ be a divisor with simple normal crossings. Let $g$ be a conical Kähler metric with cone angle $2 \pi \boldsymbol{\beta}$ along $D$. Suppose $u \in H^{1}(g)$ is a weak solution to the equation $\Delta_{g} u=f$ in the sense that
$$\int_{X}\langle\nabla u, \nabla \varphi\rangle \omega_{g}^{n}=-\int_{X} f \varphi \omega_{g}^{n}, \quad \forall \varphi \in C^{1}(X)$$
for some $f \in C_{\boldsymbol{\beta}}^{0, \alpha}(X)$. Then $u \in C_{\boldsymbol{\beta}}^{2, \alpha}(X) \cap C^{0}(X)$ and there exists a constant $C=C(n, \boldsymbol{\beta}, g, \alpha)$ such that
$$\|u\|_{C_{\beta}^{2, \alpha}(X)} \leq C\left(\|u\|_{C^{0}(X)}+\|f\|_{C_{\beta}^{0, \alpha}(X)}\right) .$$
Proof. We can choose finite covers of $D,\left\{B_{a}\right\},\left\{B_{a}^{\prime}\right\}$ with $B_{a}^{\prime} \Subset B_{a}$ and centers at $D$. By assumption $u$ is a weak solution to the equation $\Delta_{g} u=f$ in each $B_{a}$, then by Corollary 3.3 we conclude that $u \in C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{a}\right)$ for each $B_{a}$. On $X \backslash \mathcal{S}$, the metric $g$ is smooth so standard elliptic theory implies that $u \in C_{\text {loc }}^{2, \alpha}(X \backslash \mathcal{S})$. Since $\left\{B_{a}\right\}$ covers $D, u \in C_{\boldsymbol{\beta}}^{2, \alpha}(X)$.

We can apply Corollary 3.1 to obtain that for some constant $C>0$
$$\|u\|_{C_{\boldsymbol{\beta}}^{2, \alpha}\left(B_{a}^{\prime}\right)} \leq C\left(\|u\|_{C^{0}\left(B_{a}\right)}+\|f\|_{C_{\boldsymbol{\beta}}^{\alpha}\left(B_{a}\right)}\right) .$$
On $X \backslash \cup_{a}\left\{B_{a}^{\prime}\right\}$ the metric $g$ is smooth, the usual Schauder estimates apply. We finish the proof of the Corollary by the definition of $C_{\boldsymbol{\beta}}^{2, \alpha}(X)$ (c.f. Definition 2.8). \(\square\)

Remark 3.5. Let $(X, D, g)$ be as in Corollary 3.4. It is easy to see by variational method weak solutions to $\Delta_{g} u=f$ always exist for any $f \in L^{2}\left(X, \omega_{g}^{n}\right)$ satisfying $\int_{X} f \omega_{g}^{n}=0$.

\section*{4. Parabolic estimates}

In this section, we will study the heat equation with background metric $\omega_{\boldsymbol{\beta}}$ and prove the Schauder estimates for such solution $u \in C^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathcal{C}^{2,1}\left(\mathcal{Q}_{\boldsymbol{\beta}}^{\#}\right)$ to the equation
$$\frac{\partial u}{\partial t}=\Delta_{g_{\beta}} u+f,$$
for a function $f \in \mathcal{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$ with some better regularity.