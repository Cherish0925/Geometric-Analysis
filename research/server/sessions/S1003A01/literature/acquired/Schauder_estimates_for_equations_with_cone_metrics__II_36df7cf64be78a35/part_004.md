---
retention_scope: session
part: 4
total_parts: 5
---

[Part 4/5 of: Schauder estimates for equations with cone metrics, II]

Lemma 4.2. There exists a constant $C=C(n)>0$ such that, for any small $\epsilon>0$,
$$\sup _{B_{g_{\epsilon}}(0,3 R / 5)}\left|\Delta_{i} u_{\epsilon}\right| \leq C\left(\frac{1}{t}+\frac{1}{R^{2}}\right) \operatorname{osc}_{R} u_{\epsilon} \quad \text { for all } t \in\left(0, R^{2}\right),$$
where we write $\Delta_{i} u_{\epsilon}:=\left(\left|z_{i}\right|^{2}+\epsilon\right)^{1-\beta_{i}}\left(\partial^{2} u_{\epsilon} / \partial z_{i} \partial z_{i}\right)$ for $i=1, \ldots, p$.

Proof. We only prove the case when $i=1$. We define $F:=t \varphi\left(-\Delta_{1} f_{\epsilon}-2 \dot{f}_{\epsilon}\right)$, and we calculate
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right)\left(-\Delta_{1} f_{\epsilon}-2 \dot{f}_{\epsilon}\right) & =-\left|\nabla_{2} \nabla f_{\epsilon}\right|^{2}-\left|\nabla_{1} \bar{\nabla} f_{\epsilon}\right|^{2}-2 \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla}\left(-\Delta_{1} f_{\epsilon}-2 \dot{f}_{\epsilon}\right)\right\rangle-R_{1 \overline{1} j \bar{k}} f_{\epsilon, \bar{j}} f_{\epsilon, k} \\
& \leq-\left(-\Delta_{1} f_{\epsilon}\right)^{2}-2 \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla}\left(-\Delta_{1} f_{\epsilon}-2 \dot{f}_{\epsilon}\right)\right\rangle
\end{aligned}$$
$F$ achieves its maximum at a point $\left(p_{0}, t_{0}\right)$, where we may assume $F\left(p_{0}, t_{0}\right)>0$; otherwise we are already done. In particular, $p_{0} \in B_{g_{\epsilon}}\left(0, \frac{2}{3} r\right)$ by the definition of $\varphi$ and $t_{0}>0$. Then at $\left(p_{0}, t_{0}\right)$, we have
$$\begin{aligned}
0 & \leq\left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right) F \\
& =\frac{F}{t_{0}}+t_{0} \varphi\left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right)\left(-\Delta_{1} f_{\epsilon}-2 \dot{f}_{\epsilon}\right)-\frac{F}{\varphi} \Delta_{g_{\epsilon}} \varphi-2 t_{0} \operatorname{Re}\left\langle\nabla \varphi, \bar{\nabla}\left(\frac{F}{t_{0} \varphi}\right)\right\rangle \\
& \leq \frac{F}{t_{0}}+t_{0} \varphi\left(-\left(-\Delta_{1} f_{\epsilon}\right)^{2}-2 \frac{F}{t_{0} \varphi^{2}} \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla} \varphi\right\rangle\right)+C \frac{F}{R^{2} \varphi}\left(\varphi^{\prime}+\varphi^{\prime \prime}\right)+2 \frac{F}{R^{2} \varphi^{2}}\left(\varphi^{\prime}\right)^{2},
\end{aligned}$$
where we use the Laplacian comparison and the fact that $\nabla F=0$ at $\left(p_{0}, t_{0}\right)$. The second term on the right-hand side satisfies (we write $\widetilde{F}:=-\Delta_{1} f_{\epsilon}-2 \dot{f}_{\epsilon}$ for convenience of notation)
$$\begin{aligned}
t_{0} \varphi\left(-\left(-\Delta_{1} f_{\epsilon}\right)^{2}-2 \frac{F}{t_{0} \varphi^{2}} \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla} \varphi\right\rangle\right) & \leq t_{0} \varphi\left(-\widetilde{F}^{2}-4 \widetilde{F} \dot{f}_{\epsilon}-4\left(\dot{f}_{\epsilon}\right)^{2}+\frac{2 \widetilde{F}}{\varphi} \frac{\left|\nabla f_{\epsilon}\right|\left|\varphi^{\prime}\right|}{R}\right) \\
& \leq t_{0} \varphi\left(-\widetilde{F}^{2}-4 \widetilde{F} \dot{f}_{\epsilon}+2 \widetilde{F}\left|\nabla f_{\epsilon}\right|^{2}+\frac{\widetilde{F}\left|\varphi^{\prime}\right|^{2}}{2 R^{2} \varphi^{2}}\right) \\
& \leq t_{0} \varphi\left(-\widetilde{F}^{2}+\frac{\widetilde{F}\left|\varphi^{\prime}\right|^{2}}{2 R^{2} \varphi^{2}}+C \frac{\widetilde{F}}{t_{0}}+C \frac{\widetilde{F}}{R^{2}}\right) \\
& =-\frac{F^{2}}{t_{0} \varphi}+C \frac{F}{2 R^{2} \varphi}+C \frac{F}{t_{0}}+C \frac{F}{R^{2}} .
\end{aligned}$$
Inserting this into (4-7), we get, for some constant $C=C(n)>0$, at $\left(p_{0}, t_{0}\right)$,
$$-F^{2}+C \varphi F+\frac{t_{0} \varphi F}{R^{2}}+C t_{0} \frac{F}{R^{2}} \geq 0,$$
from which we obtain $F\left(p_{0}, t_{0}\right) \leq C t_{0} / R^{2}+C$. By the choice of $\left(p_{0}, t_{0}\right)$, we can see that
$$\sup _{B_{g \epsilon}(0, R / 2)}\left(-\Delta_{1} f_{\epsilon}-2 \dot{f}_{\epsilon}\right) \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right) \quad \text { for all } t \in\left(0, R^{2}\right),$$
which implies that, on $B_{g_{\epsilon}}\left(0, \frac{3}{5} R\right) \times\left(0, R^{2}\right)$,
$$-\Delta_{1} u_{\epsilon} \leq \dot{u}_{\epsilon}+C\left(\frac{1}{t}+\frac{1}{R^{2}}\right) u_{\epsilon} .$$
Applying (4-8) to the function $\sup u_{\epsilon}-u_{\epsilon}$, we obtain, on $B_{g_{\epsilon}}\left(0, \frac{3}{5} R\right) \times\left(0, R^{2}\right)$,
$$\left|\Delta_{1} u_{\epsilon}\right| \leq\left|\dot{u}_{\epsilon}\right|+C\left(\frac{1}{t}+\frac{1}{R^{2}}\right) \operatorname{osc}_{R} u_{\epsilon} \leq C\left(\frac{1}{t}+\frac{1}{R^{2}}\right) \operatorname{osc}_{R} u_{\epsilon}$$
by (4-6). Thus we finish the proof of the lemma. \(\square\)

Lemma 4.3. There exists a constant $C=C(n)>0$ such that
$$\sup _{i \neq j} \sup _{B_{g \epsilon}(0, R / 2)}\left(\left|\nabla_{i} \nabla_{j} u_{\epsilon}\right|+\left|\nabla_{i} \bar{\nabla}_{j} u_{\epsilon}\right|\right) \leq C\left(\frac{1}{t}+\frac{1}{R^{2}}\right) \operatorname{osc}_{R} u_{\epsilon}$$
for all $t \in\left(0, R^{2}\right)$. Recall, here $\left|\nabla_{i} \nabla_{j} u_{\epsilon}\right|^{2}=\nabla_{i} \nabla_{j} u_{\epsilon} \nabla_{\bar{i}} \nabla_{\bar{j}} u_{\epsilon} g_{\epsilon}^{i \bar{i}} g_{\epsilon}^{j \bar{j}}$ (no summation over $i, j$ is taken). Proof. We only prove the estimate for $\left|\nabla_{1} \nabla_{2} u_{\epsilon}\right|$. The other estimates are similar, so we omit their proofs.

By calculations similar to those used to derive (3-27), we have
$$\left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right)\left|\nabla_{1} \nabla_{2} f_{\epsilon}\right| \leq 2 \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla}\right| \nabla_{1} \nabla_{2} f_{\epsilon}| \rangle+\sum_{k}\left(\left|\nabla_{1} \nabla_{k} f_{\epsilon}\right|\left|\nabla_{2} \nabla_{\bar{k}} f_{\epsilon}\right|+\left|\nabla_{2} \nabla_{k} f_{\epsilon}\right|\left|\nabla_{1} \nabla_{\bar{k}} f_{\epsilon}\right|\right),$$
and similar to (3-20),
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right)\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right) \leq 2 & \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla}\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right)\right\rangle \\
& -\sum_{k}\left(\left|\nabla_{1} \nabla_{k} f_{\epsilon}\right|^{2}+\left|\nabla_{1} \nabla_{\bar{k}} f_{\epsilon}\right|^{2}+\left|\nabla_{2} \nabla_{k} f_{\epsilon}\right|^{2}+\left|\nabla_{2} \nabla_{\bar{k}} f_{\epsilon}\right|^{2}\right) .
\end{aligned}$$
Combining (4-10), (4-9) and the Cauchy-Schwarz inequality, we get
$$\begin{aligned}
& \left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right)\left(\left|\nabla_{1} \nabla_{2} f_{\epsilon}\right|+2\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right)\right) \\
& \leq 2 \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla}\left(\left|\nabla_{1} \nabla_{2} f_{\epsilon}\right|+2\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right)\right)\right\rangle-\sum_{k}\left(\left|\nabla_{1} \nabla_{k} f_{\epsilon}\right|^{2}+\left|\nabla_{1} \nabla_{\bar{k}} f_{\epsilon}\right|^{2}+\left|\nabla_{2} \nabla_{k} f_{\epsilon}\right|^{2}+\left|\nabla_{2} \nabla_{\bar{k}} f_{\epsilon}\right|^{2}\right) \\
& \leq 2 \operatorname{Re}\left\langle\nabla f_{\epsilon}, \bar{\nabla}\left(\left|\nabla_{1} \nabla_{2} f_{\epsilon}\right|+2\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right)\right)\right\rangle-\frac{1}{10}\left(\left|\nabla_{1} \nabla_{2} f_{\epsilon}\right|+2\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right)\right)^{2} .
\end{aligned}$$
We define a cut-off function $\eta$ similar to $\varphi$ in the proof of Lemma 4.2 such that $\eta=1$ on $B_{g_{\epsilon}}\left(0, \frac{1}{2} R\right)$ and $\eta$ vanishes outside $B_{g_{\epsilon}}\left(0, \frac{3}{5} R\right)$. We write
$$G=\operatorname{t\eta }\left(\left|\nabla_{1} \nabla_{2} f_{\epsilon}\right|+2\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right)-2 \dot{f}_{\epsilon}\right) .$$
Like we did for $F$ in the proof of Lemma 4.2, we argue similarly that at the maximum point $\left(p_{0}, t_{0}\right)$ of $G$, for which we assume $G\left(p_{0}, t_{0}\right)>0$,
$$\begin{aligned}
0 \leq\left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right) G & \leq \frac{G}{t_{0}}-\frac{G^{2}}{t_{0} \eta}+C \frac{G}{R^{2} \eta}+C \frac{G}{t_{0}}+C \frac{G}{R^{2}}+C \frac{G}{R^{2}} \frac{\eta^{\prime}+\eta^{\prime \prime}}{\eta}+\frac{2 G}{R^{2} \eta^{2}}\left(\eta^{\prime}\right)^{2} \\
& \leq \frac{1}{t_{0} \eta}\left(-G^{2}+C \eta G+\frac{t_{0} \eta G}{R^{2}}+C t_{0} \frac{G}{R^{2}}\right),
\end{aligned}$$
so it follows that $G\left(p_{0}, t_{0}\right) \leq C\left(1+t_{0} / R^{2}\right)$. Therefore by the definition of $G$, on $B_{g_{\epsilon}}\left(0, \frac{1}{2} R\right) \times\left(0, R^{2}\right)$,
$$\left|\nabla_{1} \nabla_{2} f_{\epsilon}\right|+2\left(-\Delta_{1} f_{\epsilon}-\Delta_{2} f_{\epsilon}\right)-2 \dot{f}_{\epsilon} \leq C\left(\frac{1}{R^{2}}+\frac{1}{t}\right),$$
and thus by Lemmas 4.1 and 4.2, we conclude that, on $B_{g_{\epsilon}}\left(0, \frac{1}{2} R\right) \times\left(0, R^{2}\right)$,
$$\left|\nabla_{1} \nabla_{2} u_{\epsilon}\right| \leq \dot{u}_{\epsilon}+2\left|\Delta_{1} u_{\epsilon}\right|+2\left|\Delta_{2} u_{\epsilon}\right|+\frac{\left|\nabla u_{\epsilon}\right|^{2}}{u_{\epsilon}}+C u_{\epsilon}\left(\frac{1}{R^{2}}+\frac{1}{t}\right) \leq C\left(\frac{1}{t}+\frac{1}{R^{2}}\right) \operatorname{osc}_{R} u_{\epsilon},$$
as desired. \(\square\)

4A2. Existence of a solution $u$ to (4-2). We will show the limit function of $u_{\epsilon}$ as $\epsilon \rightarrow 0$ solves (4-2).
Proposition 4.4. Given any $R \in(0,1)$ and any $\varphi \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\beta}(0, R)\right)$, there exists a unique function $u \in \mathscr{C}^{2,1}\left(\mathcal{Q}_{\beta}(0, R)^{\#}\right) \cap C^{0}\left(\overline{\mathcal{Q}_{\beta}(0, R)}\right)$ solving (4-2). Moreover, there exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that, for any $t \in\left(0, R^{2}\right)$ we have (defining $B_{\beta}(r)^{\#}:=B_{\beta}(0, r) \backslash \mathcal{S}$ ),
$$\begin{aligned}
\sup _{B_{\beta}(R / 2)^{\#}}\left(\sum_{j=1}^{p}\left|z_{j}\right|^{2-2 \beta_{j}}\left|\frac{\partial u}{\partial z_{j}}\right|^{2}+\left|D^{\prime} u\right|^{2}\right) & \leq C\left(\frac{1}{t}+\frac{1}{R^{2}}\right)\left(\operatorname{osc}_{R} u\right)^{2}, \\
\sup _{B_{\beta}(R / 2)^{\#}}\left(\sum_{i \neq j}\left(\left|\nabla_{i} \nabla_{j} u\right|_{g_{\beta}}+\left|\nabla_{i} \bar{\nabla}_{j} u\right|_{g_{\beta}}\right)+\left|\frac{\partial u}{\partial t}\right|\right) & \leq C\left(\frac{1}{t}+\frac{1}{R^{2}}\right) \operatorname{osc}_{R} u, \\
\sup _{B_{\beta}(R / 2)^{\#}}\left(\sum_{j=1}^{p}\left|\nabla_{g_{\beta}} \Delta_{j} u\right|+\left|\nabla_{g_{\beta}}\left(D^{\prime}\right)^{2} u\right|+\left|\nabla_{g_{\beta}} \frac{\partial u}{\partial t}\right|\right) & \leq C\left(\frac{1}{t}+\frac{1}{R^{2}}\right)^{3 / 2} \operatorname{osc}_{R} u,
\end{aligned}$$
where by abusing notation we write $\operatorname{osc}_{R} u:=\operatorname{osc}_{B_{\beta}(0, R) \times\left(0, R^{2}\right)} u$.
Proof. Let $u_{\epsilon}$ be the $\mathscr{C}^{2,1}$-solution to (4-4). The $\mathscr{C}^{0}$-norm of $u_{\epsilon}$ follows from the maximum principle (4-3).

To prove the higher-order estimates, for any fixed compact subset $K \Subset B_{\beta}(0, R)$ and $\delta>0$, standard parabolic Schauder theory yields uniform $\mathscr{C}^{4+\alpha,(4+\alpha) / 2}$-estimates of $u_{\epsilon}$ on $\left(K \backslash T_{\delta} \mathcal{S}\right) \times\left(\delta, R^{2}\right]$ for any $\alpha \in(0,1)$. As $\epsilon \rightarrow 0, u_{\epsilon}$ converges in $\mathscr{C}^{4+\alpha,(4+\alpha) / 2}\left(K \backslash T_{\delta} \mathcal{S} \cap\left(\delta, R^{2}\right]\right)$ to some function $u$ which is also $\mathscr{C}^{4+\alpha,(4+\alpha) / 2}$ in $\left(K \backslash T_{\delta} \mathcal{S}\right) \times\left(\delta, R^{2}\right]$. Letting $\delta \rightarrow 0$ and $K \rightarrow B_{\beta}(0, R)$ and using a diagonal argument, we can assume that
$$u_{\epsilon} \xrightarrow{\mathscr{C}_{\text {loc }}^{4+\alpha,(4+\alpha) / 2}\left(B_{\beta}(0, R)^{\#} \times\left(0, R^{2}\right]\right)} u \quad \text { as } \epsilon \rightarrow 0 .$$
Letting $\epsilon \rightarrow 0$, estimate (4-11) follows from (4-5); (4-12) is a consequence of Lemma 4.3; and (4-13) follows by applying the gradient estimate (4-5) to the $\Delta_{g_{\epsilon}}$-harmonic functions $\Delta_{j} u_{\epsilon},\left(D^{\prime}\right)^{2} u_{\epsilon}$ and $\partial u_{\epsilon} / \partial t$, and then letting $\epsilon \rightarrow 0$.

The gradient estimate (4-11) implies that, for any compact $K \Subset B_{\beta}(0, R)$,
$$\sup _{K \backslash \mathcal{S}_{j}}\left|\frac{\partial u}{\partial z_{j}}\right| \leq \frac{C(n, K, \boldsymbol{\beta})\left(\operatorname{osc}_{R} u\right)^{2}}{t}\left|z_{j}\right|^{\beta_{j}-1} \quad \text { for all } t \in\left(0, R^{2}\right) .$$
From this, for any $t \in\left(0, R^{2}\right)$, we see that $u(\cdot, t)$ can be continuously extended to $\mathcal{S}$, and thus we have $u \in C^{0}\left(B_{\beta}(0, R) \times\left(0, R^{2}\right)\right)$.

It only remains to show $u=\varphi$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}(0, R)$. Fix an arbitrary point $\left(q_{0}, t_{0}\right) \in \partial_{\mathcal{P}}\left(\mathcal{Q}_{\boldsymbol{\beta}}(0, R)\right)$.
Case 1: $t_{0}=0$ and $q_{0} \in \overline{B_{\beta}(0, R)}$. We define a barrier function $\phi_{1}(z, t)=e^{-d_{\mathbb{C}^{n}}\left(z, q_{0}\right)^{2}-\lambda t}-1$, where $\lambda>0$ is to be determined. If $\lambda \geq 4 n$, we calculate
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{g_{\epsilon}}\right) \phi_{1} & =-\lambda e^{-d_{\mathbb{C}^{n}}\left(z, q_{0}\right)^{2}-\lambda t}-\left(-\Delta_{g_{\epsilon}} d_{\mathbb{C}^{n}}^{2}+\left|\nabla d_{\mathbb{C}^{n}}^{2}\right|_{g_{\epsilon}}^{2}\right) e^{-d_{\mathbb{C}^{n}}\left(z, q_{0}\right)^{2}-\lambda t} \\
& \leq\left(-\lambda+\sum_{j=1}^{p}\left(\left|z_{j}\right|^{2}+\epsilon\right)^{1-\beta_{j}}+(n-p)\right) e^{-d_{\mathbb{C}^{n}}\left(z, q_{0}\right)^{2}-\lambda t}<0 .
\end{aligned}$$

On the other hand, $\phi_{1}\left(q_{0}, t_{0}\right)=0$ and $\phi_{1}(z, t)<0$ for any $(z, t) \neq\left(q_{0}, t_{0}\right)$. For any $\varepsilon>0$, we can find a small neighborhood $V \cap \partial_{\mathcal{P}}\left(\mathcal{Q}_{\boldsymbol{\beta}}(0, R)\right)$ of $\left(q_{0}, t_{0}\right)$ such that, on $V$, we have $\varphi\left(q_{0}, t_{0}\right)+\varepsilon>\varphi(z, t)>\varphi\left(q_{0}, t_{0}\right)-\varepsilon$, since $\varphi$ is continuous. On $\partial_{\mathcal{P}}\left(\mathcal{Q}_{\beta}(0, R)\right) \backslash V$, the function $\phi_{1}$ is bounded above by a negative constant. Therefore the function $\phi_{1}^{-}:=\varphi\left(q_{0}, t_{0}\right)-\varepsilon+A \phi_{1}(z, t) \leq \varphi(z, t)$ for any $(z, t) \in \partial_{\mathcal{P}}\left(\mathcal{Q}_{\boldsymbol{\beta}}(0, R)\right)$ if $A \gg 1$. Therefore, by the maximum principle, $\phi_{1}^{-}(z, t) \leq u_{\epsilon}(z, t)$ for any $(z, t) \in \mathcal{Q}_{\beta}(0, R)$. Letting $\epsilon \rightarrow 0$, we have $\phi_{1}^{-}(z, t) \leq u(z, t)$. Letting $(z, t) \rightarrow\left(q_{0}, t_{0}\right)$ yields $\varphi\left(q_{0}, t_{0}\right)-\varepsilon \leq \liminf _{(z, t) \rightarrow\left(q_{0}, t_{0}\right)} u(z, t)$. Setting $\varepsilon \rightarrow 0$, we conclude that $\varphi\left(q_{0}, t_{0}\right) \leq \liminf _{(z, t) \rightarrow\left(q_{0}, t_{0}\right)} u(z, t)$. Considering $\phi_{1}^{+}(z, t)=\varphi\left(q_{0}, t_{0}\right)+\varepsilon-A \phi_{1}(z, t)$ and using an argument similar to that above, we can get $\varphi\left(q_{0}, t_{0}\right) \geq \lim \sup _{(z, t) \rightarrow\left(q_{0}, t_{0}\right)} u(z, t)$. Thus $u$ coincides with $\varphi$ at $\left(q_{0}, t_{0}\right)$.

Case 2: $t_{0}>0$ and $q_{0} \in \partial B_{\boldsymbol{\beta}}(0, R) \cap\left(\mathcal{S}_{1} \cap \mathcal{S}_{2}\right)$. In this case $z_{1}\left(q_{0}\right)=z_{2}\left(q_{0}\right)=0$. We define $q_{0}^{\prime}=-q_{0} \in$ $\partial B_{\beta}(0, R)$ to be the (Euclidean) opposite point to $q_{0}$. For some small $\delta>0$, define
$$\phi_{2}(z, t)=d_{\mathbb{C}^{n}}\left(z, q_{0}^{\prime}\right)^{2}-4 R^{2}-\delta\left(t-t_{0}\right)^{2} .$$
Then $\phi_{2}\left(q_{0}, z_{0}\right)=0$ and $\phi(z, t)<0$ for any $(z, t) \neq\left(q_{0}, t_{0}\right)$. We calculate $\partial_{t} \phi_{2}-\Delta_{g_{\epsilon}} \phi_{2} \leq 0$. By an argument similar to Case 1, replacing $\phi_{1}$ by $\phi_{2}$ we get $\lim _{(z, t) \rightarrow\left(q_{0}, t_{0}\right)} u(z, t)=\varphi\left(q_{0}, t_{0}\right)$.

Case 3: $t_{0}>0$ and $q_{0} \in \partial B_{\beta}(0, R) \backslash\left(\mathcal{S}_{1} \cap \mathcal{S}_{2}\right)$. As in Case 2 in the proof of Proposition 3.5, we define a similar function $G$. Define $\phi_{3}(z, t)=A\left(d_{\boldsymbol{\beta}}(z, 0)^{2}-R^{2}\right)+G(z)-\delta\left(t-t_{0}\right)^{2}$ for $A \gg 1$ and small $\delta>0$. Then we can calculate that $\partial_{t} \phi_{3} \leq \Delta_{g_{\epsilon}} \phi_{3}, \phi_{3}\left(q_{0}, t_{0}\right)=0$ and $\phi_{3}(z, t)<0$ for any other $(z, t) \neq\left(q_{0}, t_{0}\right)$. Similar arguments to those in Case 1 proves that
$$\lim _{(z, t) \rightarrow\left(q_{0}, t_{0}\right)} u(z, t)=\varphi\left(q_{0}, t_{0}\right) .$$

Combining the three cases above, we obtain that $u$ coincides with $\varphi$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\beta}(0, R)$. Thus the Dirichlet problem (4-2) admits a unique solution $u \in \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}(0, R)}\right) \cap \mathscr{C}^{2,1}\left(\mathcal{Q}_{\beta}(0, R)^{\#}\right)$. \(\square\)

Corollary 4.5. Given any functions $f \in \mathscr{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ and $\varphi \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right)$, there exists a unique solution $v \in \mathscr{C}^{2,1}\left(\mathcal{Q}_{\boldsymbol{\beta}}^{\#}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ to the Dirichlet problem
$$\frac{\partial v}{\partial t}=\Delta_{g_{\beta}} v+f \quad \text { in } \mathcal{Q}_{\beta} \quad \text { and } \quad v=\varphi \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta} .$$
Proof. Let $v_{\epsilon} \in \mathscr{C}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right) \cap \mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)$ be the unique solution to the equations
$$\frac{\partial v_{\epsilon}}{\partial t}=\Delta_{g_{\epsilon}} v_{\epsilon}+f \quad \text { in } \mathscr{Q}_{\beta} \quad \text { and } \quad v_{\epsilon}=\varphi \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta} .$$
For any compact subset $K \Subset B_{\beta}(0,1)$ and $\delta \in(0,1)$, the standard Schauder estimates for parabolic equations provide uniform $\mathscr{C}^{2+\alpha,(2+\alpha) / 2}$-estimates for $v_{\epsilon}$ on $K \backslash T_{\delta} \mathcal{S} \times\left(\delta^{2}, 1\right)$. Then $v_{\epsilon} \rightarrow v$ for some $v \in \mathscr{C}^{2+\alpha,(2+\alpha) / 2}\left(K \backslash T_{\delta} \mathcal{S} \times\left(\delta^{2}, 1\right)\right)$. Taking $\delta \rightarrow 0$ and $K \rightarrow B_{\beta}(0,1)$ and using a diagonal argument, we get that $v_{\epsilon}$ converges in $\mathscr{C}_{\text {loc }}^{2+\alpha,(2+\alpha) / 2}\left(B_{\beta} \backslash \mathcal{S} \times(0,1)\right)$ to $v$ and $v$ satisfies the equation $\partial v / \partial t=\Delta_{g_{\beta}} v+f$ on $B_{\beta} \backslash \mathcal{S} \times(0,1)$.

It only remains to show $v \in \mathscr{C}^{0}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$ and $v=\varphi$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}$. The same proof as in Cases 1, 2 and 3 in Proposition 4.4 yields that $v$ must coincide with $\varphi$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}$, since we can always choose $A>1$ large enough that (for example in Case 1) $\partial \phi_{1}^{-} / \partial t-\Delta_{g_{\epsilon}} \phi_{1}^{-} \leq \inf _{\mathcal{Q}_{\beta}} f \leq \partial v_{\epsilon} / \partial t-\Delta_{g_{\epsilon}} v_{\epsilon}$. To see
the continuity of $v$ in $\mathcal{Q}_{\boldsymbol{\beta}}$, because of the Sobolev inequality (3-42) for metric spaces $\left(B_{\boldsymbol{\beta}}, g_{\epsilon}\right)$ and by the proof of the standard De Giorgi-Nash-Moser theory for parabolic equations, we conclude that, for any $p \in \mathcal{S}$ and $t_{0} \in(0,1)$, there exists a small number $R_{0}=R_{0}\left(p, t_{0}\right)$ such that, on the cylinder $\widetilde{\mathcal{Q}}_{R_{0}}:=B_{\beta}\left(p, R_{0}\right) \times\left(t_{0}-R_{0}^{2}, t_{0}\right)$, we have $\operatorname{osc}_{\widetilde{\mathcal{Q}}_{r}} v_{\epsilon} \leq C r^{\alpha^{\prime}}$ for any $r \in\left(0, R_{0}\right)$ and some $\alpha^{\prime} \in(0,1)$. Therefore $\operatorname{osc}_{\widetilde{\mathcal{Q}}_{r}} v \leq C r^{\alpha^{\prime}}$ and $v$ is continuous at $\left(p, t_{0}\right)$, as desired.

The uniqueness of the solution to (4-14) follows from the maximum principle. \(\square\)

Remark 4.6. Corollary 4.5 is not needed in the proof of Theorem 1.7. So by Theorem 1.7, the solution $u$ to (4-14) is in $\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$.

4B. Sketched proof of Theorem 1.7. With Proposition 4.4, we can prove the Schauder estimates for the solution $u \in \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right) \cap \mathscr{C}^{2,1}\left(\mathcal{Q}_{\beta}^{\#}\right)$ to (4-1) for a Dini-continuous function $f$ by making use of almost the same arguments as in the proof of Theorem 1.2. We will not provide the full details and only point out the main differences. For any given points $Q_{p}=\left(p, t_{p}\right), Q_{q}=\left(q, t_{q}\right) \in\left(B_{\beta}\left(0, \frac{1}{2}\right) \backslash \mathcal{S}\right) \times(\hat{t}, 1)$, to define the approximating functions $u_{k}$ as in (3-44), we define $u_{k}$ in this case as the solution to the heat equation
$$\frac{\partial u_{k}}{\partial t}=\Delta_{g_{\beta}} u_{k}+f\left(Q_{p}\right) \quad \text { in } \hat{B}_{k}(p) \times\left(t_{p}-\hat{t} \cdot \tau^{2 k}, t_{p}\right], \quad u_{k}=u \quad \text { on } \partial_{\mathcal{P}}\left(\hat{B}_{k}(p) \times\left(t_{p}-\hat{t} \cdot \tau^{2 k}, t_{p}\right]\right),$$
where $\hat{B}_{k}(p)$ is defined in (3-48). We can now apply the estimates in Proposition 4.4 to the functions $u_{k}$ or $u_{k}-u_{k-1}$, instead of those in Lemmas 3.3 and 3.4 as we did in Sections 3B, 3C and 3D, to prove the Schauder estimates for $u$. Thus we finish the proof of Theorem 1.7. \(\square\)

4C. Interior Schauder estimate for nonflat conical Kähler metrics. Let $g=\sqrt{-1} g_{j \bar{k}}(z, t) d z_{j} \wedge d z_{\bar{k}}$ be a $\mathscr{C}_{\beta}^{\alpha, \alpha / 2}$ conical Kähler metric on $\mathcal{Q}_{\beta}$ with conical singularity along $\mathcal{S}$; that is, $g(\cdot, t)$ is a $C_{\beta}^{0, \alpha}$ conical Kähler metric (from Section 3E) for any $t \in[0,1]$, and the coefficients of $g$ in the basis $\left\{\epsilon_{j} \wedge \bar{\epsilon}_{k}, \ldots\right\}$ are $\frac{1}{2} \alpha$-Hölder continuous in $t \in[0,1]$. Suppose $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(\mathscr{Q}_{\boldsymbol{\beta}}\right)$ satisfies the equation
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f \quad \text { in } \mathcal{Q}_{\beta}$$
for some $f \in \mathscr{C}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\beta}}\right)$.
Proposition 4.7. There exists a constant $C=C(n, \boldsymbol{\beta}, \alpha, g)$ such that
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)}^{*} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2)}\right) .$$
Proof. The proof is parallel to that of Proposition 3.32. Given any two points $P_{x}=\left(x, t_{x}\right), P_{y}=\left(y, t_{x}\right) \in \mathcal{Q}_{\beta}$, we may assume $d_{P_{x}}=\min \left\{d_{P_{x}}, d_{P_{y}}\right\}>0$, where $d_{P_{x}}:=d_{\mathcal{P}, \boldsymbol{\beta}}\left(P_{x}, \partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right)$ is the parabolic distance of $P_{x}$ to the parabolic boundary $\partial_{\mathcal{P}} \mathcal{Q}_{\beta}$. Let $\mu \in\left(0, \frac{1}{4}\right)$ be a positive number to be determined later. Define $d:=\mu d_{P_{x}}$, $\mathcal{Q}:=B_{\beta}(x, d) \times\left(t_{x}-d^{2}, t_{x}\right]$ the "parabolic ball" centered at $P_{x}$, and $\frac{1}{2} \mathcal{Q}:=B_{\beta}\left(x, \frac{1}{2} d\right) \times\left(t_{x}-\frac{1}{4} d^{2}, t_{x}\right]$.
Case 1: $d_{\mathcal{P}, \boldsymbol{\beta}}\left(P_{x}, P_{y}\right)<\frac{1}{2} d$. In this case we always have $P_{y} \in \frac{1}{2} \mathcal{Q}$.
Case 1a: $B_{\beta}(x, d) \cap \mathcal{S}=\varnothing$. As in the proof of Proposition 3.32, we can introduce smooth complex coordinates $\left\{w_{1}, w_{2}, z_{3}, \ldots, z_{n}\right\}$ on $B_{\boldsymbol{\beta}}(x, d)$ under which $g_{\boldsymbol{\beta}}$ becomes the standard Euclidean metric and the components of $g$ are $\mathscr{C}^{\alpha, \alpha / 2}$ in the usual sense on $\mathcal{Q}$. The leading coefficients and constant term $f$
in (4-15) are both $\mathscr{C}^{\alpha, \alpha / 2}$ in the usual sense, so we apply the standard parabolic Schauder estimates (see Theorem 4.9 in [27]) to get that there exists some constant $C=C(n, \boldsymbol{\beta}, \alpha, g)$ independent of $\mathcal{Q}$ such that
$$[u]_{\mathscr{C}^{2+\alpha,(2+\alpha) / 2}(\mathcal{Q})}^{*} \leq C\left(\|u\|_{\mathscr{C}^{0}(\mathcal{Q})}+\|f\|_{\mathscr{C}^{\alpha, \alpha / 2}(\mathcal{Q})}^{(2)}\right) .$$
Let $D$ denote the ordinary first-order operators in the coordinates $\left\{w_{1}, w_{2}, z_{3}, \ldots, z_{n}\right\}$. We calculate
$$\begin{aligned}
\left|T u\left(P_{x}\right)-T u\left(P_{y}\right)\right| & \leq\left|D^{2} u\left(P_{x}\right)-D^{2} u\left(P_{y}\right)\right|+\frac{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)}{d}\left(\left|D^{2} u\left(P_{x}\right)\right|+\left|D^{2} u\left(P_{y}\right)\right|\right) \\
& \leq \frac{4 d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}}{d^{2+\alpha}}[u]_{\mathscr{C}^{2+\alpha,(2+\alpha) / 2}(\mathcal{Q})}^{*}+\frac{4 d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)}{d^{3}}[u]_{\mathscr{C}^{2,1}(\mathcal{Q})}^{*} \\
& \leq \frac{8 d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}}{d^{2+\alpha}}[u]_{\mathscr{C}^{2+\alpha,(2+\alpha) / 2}(\mathcal{Q})}^{*}+C \frac{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}}{d^{2+\alpha}}\|u\|_{\mathscr{C}^{0}(\mathcal{Q})}
\end{aligned}$$
and
$$\left|\frac{\partial u}{\partial t}\left(P_{x}\right)-\frac{\partial u}{\partial t}\left(P_{y}\right)\right| \leq \frac{4 d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}}{d^{2+\alpha}}[u]_{\mathscr{C}^{2+\alpha,(2+\alpha) / 2}(\mathcal{Q})}^{*} .$$
Recall $\mathcal{T}$ denotes the operators in $T$ and $\partial / \partial t$; then by (4-16) it follows that
$$d_{P_{x}}^{2+\alpha} \frac{\left|\mathcal{T} u\left(P_{x}\right)-\mathcal{T} u\left(P_{y}\right)\right|}{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}} \leq \frac{C}{\mu^{2+\alpha}}\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\mathcal{Q})}^{(2)}+\frac{C}{\mu^{2+\alpha}}\|u\|_{\mathscr{C}^{0}(\mathcal{Q})} .$$
Case 1b: $B_{\beta}(x, d) \cap \mathcal{S} \neq \varnothing$. Let $\hat{x} \in \mathcal{S}$ be the projection of $x$ onto $\mathcal{S}$ and $\hat{P}_{x}=\left(\hat{x}, t_{x}\right)$ be the corresponding space-time point. Define $\hat{\mathcal{Q}}:=B_{\beta}(\hat{x}, 2 d) \times\left(t_{x}-4 d^{2}, t_{x}\right]$. As in Case 1b in the proof of Proposition 3.32, we may choose suitable enough complex coordinates that $g_{\epsilon_{j} \bar{\epsilon}_{k}}\left(\hat{P}_{x}\right)=\delta_{j k}$ and, for $j, k \geq p+1$, we have $g_{j \bar{k}}\left(\hat{P}_{x}\right)=\delta_{j k}$ and the cross terms in the expansion of $g$ in (3-114) vanish at $\hat{P}_{x}$. Thus (4-15) can be rewritten as
$$\frac{\partial u}{\partial t}=\Delta_{g_{\beta}} u+\eta \cdot \sqrt{-1} \partial \bar{\partial} u+f=: \Delta_{g_{\beta}} u+\tilde{f}, \quad u \in \mathscr{C}^{0}(\hat{\mathcal{Q}}) \cap \mathscr{C}^{2,1}\left(\hat{\mathcal{Q}}^{\#}\right),$$
for some (1, 1)-form $\eta$ as in the proof of Proposition 3.32. From the rescaled version of Theorem 1.7 we conclude that
$$d^{2+\alpha} \frac{\left|\mathcal{T} u\left(P_{x}\right)-\mathcal{T} u\left(P_{y}\right)\right|}{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}} \leq C\left(\|u\|_{\mathscr{C}^{0}(\hat{\mathcal{Q}})}+\|\tilde{f}\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\hat{\mathcal{Q}})}^{(2)}\right) .$$
Hence
$$d_{P_{x}}^{2+\alpha} \frac{\left|\mathcal{T} u\left(P_{x}\right)-\mathcal{T} u\left(P_{y}\right)\right|}{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}} \leq \frac{C}{\mu^{2+\alpha}}\left(\|u\|_{\mathscr{C}^{0}(\hat{\mathcal{Q}})}+\|\tilde{f}\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\hat{\mathcal{Q}})}^{(2)}\right) .$$
Case 2: $d_{\mathcal{P}, \boldsymbol{\beta}}\left(P_{x}, P_{y}\right) \geq \frac{1}{2} d$. Here we calculate (recall $\mathcal{Q}_{\boldsymbol{\beta}}:=B_{\boldsymbol{\beta}}(0,1) \times(0,1]$ )
$$d_{P_{x}}^{2+\alpha} \frac{\left|\mathcal{T} u\left(P_{x}\right)-\mathcal{T} u\left(P_{y}\right)\right|}{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}} \leq 4 d_{P_{x}}^{2+\alpha} \frac{|\mathcal{T} u|\left(P_{x}\right)+|\mathcal{T} u|\left(P_{y}\right)}{d^{\alpha}} \leq \frac{8}{\mu^{\alpha}}[u]_{\mathscr{C}_{\beta}^{2,1}\left(\mathcal{Q}_{\beta}\right)}^{*} .$$

Combining (4-17)-(4-19), we obtain
$$\begin{aligned}
d_{P_{x}}^{2+\alpha} \left\lvert\, \frac{\left|\mathcal{T} u\left(P_{x}\right)-\mathcal{T} u\left(P_{y}\right)\right|}{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}} \leq \frac{8}{\mu^{\alpha}}[u]_{\mathscr{C}_{\beta}^{2,1}\left(\mathcal{Q}_{\beta}\right)}^{*}+\frac{C}{\mu^{2+\alpha}}\left(\|u\|_{\mathscr{C}^{0}(\hat{\mathcal{Q}})}+\right.\right. & \left.\|\tilde{f}\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\hat{\mathcal{Q}})}^{(2)}\right) \\
& +\frac{C}{\mu^{2+\alpha}}\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\mathscr{Q})}^{(2)}+\frac{C}{\mu^{2+\alpha}}\|u\|_{\mathscr{C}^{0}(\mathcal{Q})} .
\end{aligned}$$

Observe that, for any $P \in \mathcal{Q}$ or $P \in \hat{\mathcal{Q}}$, we have $d_{\mathcal{P}, \boldsymbol{\beta}}\left(P, \partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right) \geq(1-2 \mu) d_{P_{x}}$. Then it follows from the definition that
$$\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\mathscr{Q})}^{(2)} \leq C \mu^{2}\|f\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}^{(2)}+C \mu^{2+\alpha}[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2)} \leq C \mu^{2}\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2)} .$$
We calculate
$$\begin{aligned}
\|\tilde{f}\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\hat{\mathcal{Q}})}^{(2)} & \leq\|\eta\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\hat{\mathcal{Q}})}^{(0)}\|T u\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\hat{\mathcal{Q}})}^{(2)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(\hat{\mathcal{Q}})}^{(2)} \\
& \leq C_{1}[g]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{*} \mu^{\alpha}\left(\mu^{2}[u]_{\mathscr{C}_{\beta}^{2,1}\left(\mathcal{Q}_{\beta}\right)}^{*}+\mu^{2+\alpha}[u]_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)}^{*}\right)+\mu^{2}\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathscr{Q}_{\beta}\right)}^{(2)} \\
& \leq C_{1}[g]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{*} \mu^{\alpha}\left(C(\mu)[u]_{\mathscr{C}_{\beta}^{2,1}\left(\mathcal{Q}_{\beta}\right)}^{*}+2 \mu^{2+\alpha}[u]_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)}^{*}\right)+\mu^{2}\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2)},
\end{aligned}$$
where in the last inequality we use the interpolation inequality, by which we also have
$$\frac{8}{\mu^{\alpha}}[u]_{\mathscr{C}_{\beta}^{2,1}\left(\mathcal{Q}_{\beta}\right)}^{*} \leq \mu^{\alpha}[u]_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)}^{*}+C(\mu)\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)} .$$
If $\mu$ is chosen small enough that $\mu^{\alpha}\left(2 C_{1}[g]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathscr{Q}_{\beta}\right)}^{*}+1\right)<\frac{1}{2}$, combining the above inequalities yields
$$d_{P_{x}}^{2+\alpha} \frac{\left|\mathcal{T} u\left(P_{x}\right)-\mathcal{T} u\left(P_{y}\right)\right|}{d_{\mathcal{P}, \beta}\left(P_{x}, P_{y}\right)^{\alpha}} \leq \frac{1}{2}[u]_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)}^{*}+C(\mu)\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2)}\right) .$$
Taking the supremum over all $P_{x} \neq P_{y} \in \mathcal{Q}_{\boldsymbol{\beta}}$, we obtain
$$[u]_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)}^{*} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2)}\right) .$$
The proposition is proved by invoking the interpolation inequalities. \(\square\)

Remark 4.8. It follows from the proof that the estimates in Proposition 4.7 also hold on $\mathcal{Q}_{\boldsymbol{\beta}}(p, R):=$ $B_{\beta}(p, R) \times\left(0, R^{2}\right) \subset \mathcal{Q}_{\beta}$, i.e., the cylinder whose spatial center $p$ may not lie in $\mathcal{S}$.

It is easy to derive the following local Schauder estimate for $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}$-solutions to (4-15) from Proposition 4.7.

Corollary 4.9. Let $K \Subset B_{\beta}(0,1)$ be a compact subset and $\varepsilon_{0} \in(0,1)$ be a given number. With the same assumptions as in Proposition 4.7, there exists a constant $C=C\left(n, \boldsymbol{\beta}, \alpha, g, K, \varepsilon_{0}\right)>0$ such that
$$\|u\|_{\mathscr{C}^{2+\alpha,(2+\alpha) / 2}\left(K \times\left[\varepsilon_{0}, 1\right]\right)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}\right) .$$

With the interior Schauder estimates in Proposition 4.7, we can show the existence of $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$ - solutions to the Dirichlet problem
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f \quad \text { in } \mathcal{Q}_{\beta} \quad \text { and } \quad u=\varphi \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta}$$
for any given $f \in \mathscr{C}_{\boldsymbol{\beta}}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ and $\varphi \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}\right)$. We first show the existence of solutions to (4-20) in the case $\varphi \equiv 0$.

Lemma 4.10. Let $\sigma \in(0,1)$ be given and $u \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)$ solve (4-20), with $\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}^{(-\sigma)}<\infty$ and $\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2-\sigma)}<\infty$. Then there is a constant $C=C(n, \alpha, \boldsymbol{\beta}, g, \sigma)>0$ such that
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathscr{Q}_{\beta}\right)}^{(-\sigma)} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}^{(-\sigma)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2-\sigma)}\right) .$$
Proof. The lemma follows from the definitions of the norms and the estimates in Proposition 4.7. \(\square\)

Lemma 4.11. Suppose $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2,1}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ satisfies $\partial u / \partial t=\Delta_{g} u+f$ and $u \equiv 0$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}$. For any $\sigma \in(0,1)$, there exists a constant $C=C(n, \boldsymbol{\beta}, g, \sigma)>0$ such that
$$\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}^{(-\sigma)}=\sup _{P_{x} \in \mathcal{Q}_{\beta}} d_{P_{x}}^{-\sigma}\left|u\left(P_{x}\right)\right| \leq C \sup _{P_{x} \in \mathcal{Q}_{\beta}} d_{P_{x}}^{2-\sigma}\left|f\left(P_{x}\right)\right|=C\|f\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}^{(2-\sigma)},$$
where $d_{P_{x}}=d_{\mathcal{P}, \beta}\left(P_{x}, \partial_{\mathcal{P}} \mathcal{Q}_{\beta}\right)$ is the parabolic distance of $P_{x}$ to the parabolic boundary $\partial_{\mathcal{P}} \mathcal{Q}_{\beta}$.
Proof. We write $N:=\|f\|_{C^{0}\left(\mathcal{Q}_{\beta}\right)}^{(2-\sigma)}<\infty$ and $P_{x}=\left(x, t_{x}\right)$. Define functions
$$w_{1}\left(P_{x}\right)=\left(1-d_{\beta}(x)^{2}\right)^{\sigma} \quad \text { and } \quad w_{2}\left(P_{x}\right)=t_{x}^{\sigma / 2},$$
where $d_{\boldsymbol{\beta}}(x)=d_{\boldsymbol{\beta}}(x, 0)$ is the $g_{\boldsymbol{\beta}}$-distance between $x$ and 0 . Observe that $d_{P_{x}}=\min \left\{1-d_{\boldsymbol{\beta}}(x), t_{x}^{1 / 2}\right\}$ by definition. By a straightforward calculation there is a constant $c_{0}>0$ such that
$$\left(\frac{\partial}{\partial t}-\Delta_{g}\right) w_{1} \geq c_{0}\left(1-d_{\beta}(x)\right)^{\sigma-2} \quad \text { and } \quad\left(\frac{\partial}{\partial t}-\Delta_{g}\right) w_{2} \geq c_{0}\left(t_{x}^{1 / 2}\right)^{\sigma-2} .$$
By the maximum principle we get
$$\left|u\left(P_{x}\right)\right| \leq N c_{0}^{-1}\left(w_{1}\left(P_{x}\right)+w_{2}\left(P_{x}\right)\right) \quad \text { for all } P_{x} \in \mathcal{Q}_{\beta} .$$
We take the decomposition of $\mathcal{Q}_{\beta}$ into different regions, $\mathcal{Q}_{\beta}=\Omega_{1} \cup \Omega_{2}$, where
$$\begin{aligned}
& \Omega_{1}:=\left\{P_{x} \in \mathcal{Q}_{\beta} \mid t_{x}^{1 / 2}>1-d_{\beta}(x)\right\}, \\
& \Omega_{2}:=\left\{P_{x} \in \mathcal{Q}_{\beta} \mid t_{x}^{1 / 2} \leq 1-d_{\beta}(x)\right\} .
\end{aligned}$$
Inequality (4-21) implies that, on the parabolic boundaries $\partial_{\mathcal{P}} \Omega_{1}$ and $\partial_{\mathcal{P}} \Omega_{2}$, we have $\left|u\left(P_{x}\right)\right| \leq 2 N c_{0}^{-1} d_{P_{x}}^{\sigma}$. On $\Omega_{1}$ we have $\left(\partial / \partial t-\Delta_{g}\right)\left(2 N c_{0}^{-1} w_{1} \pm u\right) \geq 0$ and $2 N c_{0}^{-1} w_{1} \pm u \geq 0$ on $\partial_{\mathcal{P}} \Omega_{1}$, so the maximum principle implies that $2 N c_{0}^{-1} w_{1} \pm u \geq 0$ in $\Omega_{1}$, i.e., $\left|u\left(P_{x}\right)\right| \leq 2 N c_{0}^{-1} d_{P_{x}}^{\sigma}$ in $\Omega_{1}$. Similarly we also have $2 N c_{0}^{-1} w_{2} \pm u \geq 0$ in $\Omega_{2}$, and thus $\left|u\left(P_{x}\right)\right| \leq 2 N c_{0}^{-1} d_{P_{x}}^{\sigma}$ in $\Omega_{2}$. In conclusion, we get
$$\left|u\left(P_{x}\right)\right| \leq 2 c_{0}^{-1} N d_{P_{x}}^{\sigma} \quad \text { for all } P_{x} \in \mathcal{Q}_{\beta} .$$ \(\square\)

Proposition 4.12. If $\varphi \equiv 0$, equation (4-20) admits a unique solution $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$ for any $f \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\beta}}\right)$.

Proof. Uniqueness follows from the maximum principle, so it suffices to show existence. We will use the continuity method. Define a continuous family of linear operators as follows: for $s \in[0,1]$, let $L_{s}:=s\left(\partial / \partial t-\Delta_{g}\right)+(1-s)\left(\partial / \partial t-\Delta_{g_{\beta}}\right)$. It can been seen that $L_{s}=\partial / \partial t-\Delta_{g_{s}}$ for some conical

Kähler metric $g_{s}$ which is uniformly equivalent to $g_{\beta}$ and has uniform $\mathscr{C}_{\beta}^{\alpha, \alpha / 2}$-estimate. So the interior Schauder estimates holds also for $L_{s}$. Fix $\sigma \in(0,1)$. Define
$$\begin{aligned}
& \mathcal{B}_{1}:=\left\{u \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right) \mid\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}\right)}^{(-\sigma)}<\infty\right\}, \\
& \mathcal{B}_{2}:=\left\{f \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right) \mid\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)}^{(2-\sigma)}<\infty\right\} .
\end{aligned}$$
Observe that any $u \in \mathcal{B}_{1}$ is continuous in $\overline{\mathcal{Q}_{\beta}}$ and vanishes on $\partial_{\mathcal{P}} \mathcal{Q}_{\beta}$. $L_{s}$ defines a continuous family of linear operators from $\mathcal{B}_{1}$ to $\mathcal{B}_{2}$. By Lemmas 4.10 and 4.11 we have
$$\|u\|_{\mathcal{B}_{1}} \leq C\left(\|u\|_{\mathscr{C}^{0}\left(\mathcal{Q}_{\beta}\right)}^{(-\sigma)}+\left\|L_{s} u\right\|_{\mathcal{B}_{2}}\right) \leq C\left\|L_{s} u\right\|_{\mathcal{B}_{2}} \quad \text { for all } s \in[0,1] \text { and for all } u \in \mathcal{B}_{1} .$$
By Corollary 4.5 and Remark 4.6, $L_{0}$ is invertible, thus by Theorem 5.2 in [18], $L_{1}$ is also invertible. \(\square\)

Corollary 4.13. For any $\varphi \in \mathscr{C}^{0}\left(\partial_{\mathcal{P}} \mathcal{Q}_{\beta}\right)$ and $f \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\beta}}\right)$, equation (4-20) admits a unique solution $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right) \cap \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\boldsymbol{\beta}}}\right)$.

Proof. The proof is identical to that of Corollary 3.39 by an approximation argument. We may assume $\varphi \in \mathscr{C}^{0}\left(\overline{\mathcal{Q}_{\beta}}\right)$ and choose a sequence $\varphi_{k} \in \mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}\left(\overline{\mathcal{Q}_{\beta}}\right)$ which converges uniformly to $\varphi$ on $\overline{\mathcal{Q}_{\beta}}$. The equations
$$\frac{\partial v_{k}}{\partial t}=\Delta_{g} v_{k}+f-\Delta_{g} \varphi_{k} \quad \text { and } \quad v_{k} \equiv 0 \quad \text { on } \partial_{\mathcal{P}} \mathcal{Q}_{\beta}$$
admit a unique $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}$-solution by Proposition 4.12. The interior Schauder estimates in Corollary 4.9 imply that $u_{k}:=v_{k}+\varphi_{k}$ converges in $\mathscr{C}_{\boldsymbol{\beta}, \text { loc }}^{2+\alpha,(\alpha+2) / 2}$ to some function $u$ in $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(\mathscr{Q}_{\boldsymbol{\beta}}\right)$ which solves (4-20). The $\mathscr{C}^{0}$-convergence $u_{k} \rightarrow u$ is uniform on $\overline{\mathcal{Q}_{\beta}}$ by the maximum principle, so $u=\varphi$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\boldsymbol{\beta}}$, as desired. \(\square\)

We recall the definition of weak solutions and refer to Section 7.1 in [17] for the notations.
Definition 4.14. We say a function $u$ on $\mathcal{Q}_{\beta}$ is a weak solution to the equation $\partial u / \partial t=\Delta_{g} u+f$ if:
\begin{itemize}
\item[(1)] $u \in L^{2}\left(0,1 ; H^{1}\left(B_{\beta}\right)\right)$ and $\partial u / \partial t \in L^{2}\left(0,1 ; H^{-1}\left(B_{\beta}\right)\right)$.
\item[(2)] For any $v \in H_{0}^{1}\left(B_{\beta}\right)$ and $t \in(0,1)$,
$$\int_{B_{\beta}} \frac{\partial u(x, t)}{\partial t} v(x) \omega_{g}^{n}=-\int_{B_{\beta}}\langle\nabla u(x, t), \nabla v(x)\rangle_{g} \omega_{g}^{n}+\int_{B_{\beta}} f(x, t) v(x) \omega_{g}^{n} .$$
\end{itemize}

On can use the classical Galerkin approximations to construct a weak solution to $\partial u / \partial t=\Delta_{g} u+f$ (see Section 7.1.2 in [17]). If $f$ has better regularity, so does the weak solution $u$.

Lemma 4.15. If $f \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\mathcal{Q}_{\beta}\right)$, then any weak solution to
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f$$
belongs to $\mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(\alpha+2) / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$.

Proof. The Sobolev inequality holds for the metric $g$, so by the proof of the standard De Giorgi-Nash-Moser theory for parabolic equations we have that $u$ is in fact continuous on $\mathcal{Q}_{\beta}$. Since the metric $g$ is smooth on $\mathcal{Q}_{\beta}^{\#}$, the weak solution $u$ is also a weak solution in $\mathcal{Q}_{\beta}^{\#}$ with the smooth background metric, so we have that $u \in \mathscr{C}_{\text {loc }}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\beta}^{\#}\right)$ in the usual sense by the classical Schauder estimates. Thus it suffices to consider points at $\mathcal{S}$. We choose the worst such point $0 \in \mathcal{S}$ only, since the case when centers are in other components of $\mathcal{S}$ is even simpler. We fix the point $P_{0}=\left(0, t_{0}\right) \in \mathcal{Q}_{\beta}$ with $t_{0}>0$. Fix $r \in\left(0, \sqrt{t_{0}}\right)$. By Corollary 4.13,
$$\frac{\partial v}{\partial t}=\Delta v+f \quad \text { in } \mathcal{Q}_{\beta}\left(P_{0}, r\right):=B_{\beta}(0, r) \times\left(t_{0}-r^{2}, t_{0}\right]$$
with boundary value $v=u$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\beta}\left(P_{0}, r\right)$ admits a unique solution $v \in \mathscr{C}^{2+\alpha,(\alpha+2) / 2_{\beta}\left(\mathcal{Q}_{\beta}\left(P_{0}, r\right)\right) \text {. Then by }}$ the maximum principle $u=v$ in $\mathcal{Q}_{\beta}\left(P_{0}, r\right)$. Thus $u \in \mathscr{C}_{\beta}^{2+\alpha,(\alpha+2) / 2}\left(\mathcal{Q}_{\beta}\left(P_{0}, r\right)\right)$ too. Since the argument also works at other space-time points in $\mathcal{S}_{\mathcal{P}}$, we see that $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}\left(\mathcal{Q}_{\boldsymbol{\beta}}\right)$, as desired. \(\square\)

Corollary 4.16. Let ( $X, g, D$ ) be as in Corollary 3.41, and let $u_{0} \in C^{0}(X)$ and $f \in \mathscr{C}_{\boldsymbol{\beta}}^{\boldsymbol{\alpha}, \alpha / 2}(X \times(0,1])$ be given functions. The weak solution $u$ to the equation
$$\frac{\partial u}{\partial t}=\Delta_{g} u+f \quad \text { in } X \times(0,1],\left.\quad u\right|_{t=0}=u_{0}$$
always exists. Moreover, $u \in \mathscr{C}_{\boldsymbol{\beta}}^{2+\alpha,(2+\alpha) / 2}(X \times(0,1])$, and there exists a constant $C=C(n, g, \boldsymbol{\beta}, \alpha)>0$ such that
$$\|u\|_{\mathscr{C}_{\beta}^{2+\alpha,(2+\alpha) / 2}(X \times(1 / 2,1])} \leq C\left(\left\|u_{0}\right\|_{C^{0}(X)}+\|f\|_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}(X \times(0,1])}\right) .$$
Proof. The weak equation can be constructed using the Galerkin approximations [17]. The uniqueness is an easy consequence of the maximum principle. The regularity of $u$ follows from the local results in Lemma 4.15. The estimate follows from the maximum principle, a covering argument as in Corollary 3.41, and the local estimates in Corollary 4.9. \(\square\)

The interior estimate in Corollary 4.16 is not good enough to show the existence of solutions to nonlinear partial differential equations since the estimate becomes worse as $t$ approaches 0 . We need some global estimates in the whole time interval $t \in[0,1]$ if the initial value $u_{0}$ has better regularity.

4D. Schauder estimate near $\boldsymbol{t}=\mathbf{0}$. In this subsection, we will prove a Schauder estimate in the whole time interval for the solutions to the heat equation when the initial value is 0 or has better regularity. We consider the model case with the background metric $g_{\beta}$ first, then we generalize the estimate to general nonflat conical Kähler metrics.

4D1. The model case. In this subsection, we will assume the background metric is $g_{\beta}$. Let $u$ be the solution to the equation
$$\frac{\partial u}{\partial t}=\Delta_{g_{\beta}} u+f \quad \text { in } \mathcal{Q}_{\beta},\left.\quad u\right|_{t=0} \equiv 0,$$
and $u=\varphi \in \mathscr{C}^{0}$ on $\partial B_{\beta} \times(0,1]$, where $f \in \mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(\overline{\mathcal{Q}_{\beta}}\right)$. In the calculations below, we should have used the smooth approximating solutions $u_{\epsilon}$, where $\partial_{t} u_{\epsilon}=\Delta_{g_{\epsilon}} u_{\epsilon}+f$ and $u_{\epsilon}=u$ on $\partial_{\mathcal{P}} \mathcal{Q}_{\beta}$. But by letting $\epsilon \rightarrow 0$, the corresponding estimates also hold for $u$. So for simplicity, we will work directly on $u$.

We fix $0<\rho<R \leq 1$ and define $B_{R}:=B_{\boldsymbol{\beta}}(0, R)$ and $Q_{R}:=B_{R} \times\left[0, R^{2}\right]$ in this section. Let $u$ be the solution to (4-22). We first have the following Caccioppoli inequalities.

Lemma 4.17. There exists a constant $C=C(n)>0$ such that
$$\sup _{t \in\left[0, \rho^{2}\right]} \int_{B_{\rho}} u^{2} \omega_{\beta}^{n}+\iint_{\mathcal{Q}_{\rho}}|\nabla u|_{g_{\beta}}^{2} \omega_{\beta}^{n} d t \leq C\left(\frac{1}{(R-\rho)^{2}} \iint_{Q_{R}} u^{2} \omega_{\beta}^{n} d t+(R-\rho)^{2} \iint_{Q_{R}} f^{2} \omega_{\beta}^{n} d t\right)$$
and
$$\begin{aligned}
\sup _{t \in\left[0, \rho^{2}\right]} \int_{B_{\rho}}|\nabla u|_{g_{\beta}}^{2} \omega_{\beta}^{n}+\iint_{Q_{\rho}}\left(|\nabla \nabla u|_{g_{\beta}}^{2}\right. & \left.+|\nabla \bar{\nabla} u|_{g_{\beta}}^{2}\right) \omega_{\beta}^{n} d t \\
& \leq C\left(\frac{1}{(R-\rho)^{2}} \iint_{Q_{R}}|\nabla u|_{g_{\beta}}^{2} \omega_{\beta}^{n} d t+\iint_{Q_{R}}\left(f-f_{R}\right)^{2} \omega_{\beta}^{n} d t\right),
\end{aligned}$$
where $f_{R}:=\left|Q_{R}\right|_{\omega_{\beta}}^{-1} \iint_{Q_{R}} f \omega_{\beta}^{n} d t$ is the average of $f$ over the cylinder $Q_{R}$.
Proof. We fix a cut-off function $\eta$ such that $\operatorname{supp} \eta \subset B_{R}, \eta=1$ on $B_{\rho}$, and $|\nabla \eta|_{g_{\beta}} \leq 2 /(R-\rho)$. Multiplying both sides of (4-22) by $\eta^{2} u$ and integrating by parts, we get
$$\begin{aligned}
\frac{d}{d t} \int_{B_{R}} \eta^{2} u^{2} & =\int_{B_{R}} 2 \eta^{2} u \Delta_{g_{\beta}} u+2 \eta^{2} u f=\int_{B_{R}}-2 \eta^{2}|\nabla u|_{g_{\beta}}^{2}-4 u \eta\langle\nabla u, \nabla \eta\rangle_{g_{\beta}}+2 \eta^{2} u f \\
& \leq \int_{B_{R}}-\eta^{2}|\nabla u|_{g_{\beta}}^{2}+4 u^{2}|\nabla \eta|_{g_{\beta}}^{2}+\eta^{2} \frac{u}{(R-\rho)^{2}}+\eta^{2}(R-\rho)^{2} f^{2} .
\end{aligned}$$
Equation (4-23) follows by integrating this inequality over $t \in\left[0, s^{2}\right]$ for all $s \leq \rho$. To see (4-24), observe that the Bochner formula yields
$$\frac{\partial}{\partial t}|\nabla u|^{2} \leq \Delta_{g_{\beta}}|\nabla u|^{2}-|\nabla \nabla u|_{g_{\beta}}^{2}-|\nabla \bar{\nabla} u|_{g_{\beta}}^{2}-2\langle\nabla u, \nabla f\rangle_{g_{\beta}} .$$
Multiplying both sides of this inequality by $\eta^{2}$ and integrating by parts, we get
$$\begin{aligned}
\frac{d}{d t} \int_{B_{R}} \eta^{2}|\nabla u|^{2} & \left.\leq \int_{B_{R}}-\left.2 \eta\langle\nabla \eta, \nabla| \nabla u\right|^{2}\right\rangle_{g_{\beta}}-\eta^{2}|\nabla \nabla u|^{2}-\eta^{2}|\nabla \bar{\nabla} u|^{2}-2 \eta^{2}\langle\nabla u, \nabla f\rangle \\
& \leq \int_{B_{R}} 4 \eta|\nabla u||\nabla \eta||\nabla| \nabla u| |-\eta^{2}|\nabla \nabla u|^{2}-\eta^{2}|\nabla \bar{\nabla} u|^{2} \\
& 4 \eta\left|f-f_{R}\right||\nabla \eta||\nabla u|+2 \eta^{2}\left|f-f_{R}\right|\left|\Delta_{g_{\beta}} u\right| \\
& \leq \int_{B_{R}}-\frac{1}{2} \eta^{2}\left(|\nabla \nabla u|^{2}+|\nabla \bar{\nabla} u|^{2}\right)+10 \eta^{2}|\nabla u|^{2}|\nabla \eta|^{2}+20 \eta^{2}\left(f-f_{R}\right)^{2} .
\end{aligned}$$
Then (4-24) follows by integrating this inequality over $t \in\left[0, s^{2}\right]$ for any $s \in[0, \rho]$. \(\square\)

Combining (4-23) and (4-24) we conclude that
$$\begin{aligned}
\sup _{t \in\left[0, R^{2} / 4\right]} \int_{B_{R / 2}}|\nabla u|^{2}+\iint_{Q_{R / 2}} & \left|\Delta_{g_{\beta}} u\right|^{2} \\
\leq & \frac{C}{R^{4}} \iint_{Q_{R}} u^{2}+C R^{2 n+2}\|f\|_{\mathscr{C}^{0}\left(Q_{R}\right)}^{2}+C R^{2 n+2+2 \alpha}\left([f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right)^{2} .
\end{aligned}$$
By a standard Moser iteration argument we get the following sub-mean-value inequality.

Lemma 4.18. If in addition $f \equiv 0$, then there exists a constant $C=C(n, \boldsymbol{\beta})>0$ such that
$$\sup _{Q_{\rho}}|u| \leq C\left(\frac{1}{(R-\rho)^{2 n+2}} \iint_{Q_{R}} u^{2} \omega_{\beta}^{n} d t\right)^{1 / 2} .$$
Proof. For any $p \geq 1$, multiplying both sides of the equation by $\eta^{2} u_{+}^{p}$, where $u_{+}=\max \{u, 0\}$, and integrating by parts, we get
$$\frac{d}{d t} \int_{B_{R}} \frac{\eta^{2}}{p+1} u_{+}^{p+1}=\int_{B_{R}}-p \eta^{2} u_{+}^{p-1}\left|\nabla u_{+}\right|^{2}-2 \eta u_{+}^{p}\left\langle\nabla u_{+}, \nabla \eta\right\rangle .$$
By the Cauchy-Schwarz inequality and integrating over $t \in\left[0, R^{2}\right]$, we conclude that
$$\left.\sup _{s \in\left[0, R^{2}\right]} \int_{B_{R}} \eta^{2} u_{+}^{p+1}\right|_{t=s}+\iint_{Q_{R}}\left|\nabla\left(\eta u_{+}^{(p+1) / 2}\right)\right|^{2} \leq \frac{C}{(R-\rho)^{2}} \iint_{Q_{R}} u_{+}^{p+1} \omega_{\beta}^{n} d t=: A$$
By the Sobolev inequality we get
$$\begin{aligned}
\int_{0}^{R^{2}} \int_{B_{R}}\left(\eta^{2} u_{+}^{p+1}\right)^{1+1 / n} & \leq \int_{0}^{R^{2}}\left(\int_{B_{R}} \eta^{2} u_{+}^{p+1}\right)^{1 / n}\left(\int_{B_{R}}\left(\eta u_{+}^{(p+1) / 2}\right)^{2 n /(n-1)}\right)^{(n-1) / n} \\
& \leq A^{1 / n} C \int_{0}^{R^{2}} \int_{B_{R}}\left|\nabla\left(\eta u_{+}^{(p+1) / 2}\right)\right|^{2} \leq C A^{(n+1) / n} .
\end{aligned}$$
If we write
$$H(p, \rho)=\left(\int_{0}^{\rho^{2}} \int_{B_{\rho}} u_{+}^{p}\right)^{1 / p},$$
the inequality above implies
$$H((p+1) \xi, \rho) \leq \frac{C^{1 /(p+1)}}{(R-\rho)^{2 /(p+1)}} H(p+1, R),$$
where $\xi=(n+1) / n>1$. Writing $p_{k}+1=2 \xi^{k}$ and $\rho_{k}=\rho+(R-\rho) 2^{-k}$, we then have $H\left(p_{k+1}+1, \rho_{k+1}\right) \leq$ $H\left(p_{k}+1, \rho_{k}\right)$. Iterating this inequality we get
$$H(\infty, \rho)=\sup _{Q_{\rho}} u_{+} \leq \frac{C}{(R-\rho)^{n+1}}\left(\iint_{Q_{R}} u_{+}^{2}\right)^{1 / 2} .$$
Similarly we get the same inequality for $u_{-}=\max \{-u, 0\}$. \(\square\)

Corollary 4.19. If in addition $f \equiv 0$, then there is a constant $C=C(n, \boldsymbol{\beta})>0$ such that
$$\iint_{Q_{\rho}} u^{2} \omega_{\beta}^{n} d t \leq C\left(\frac{\rho}{R}\right)^{2+2 n} \iint_{Q_{R}} u^{2} \omega_{\beta}^{n} d t$$
Proof. When $\rho \in\left[\frac{1}{2} R, R\right]$, the inequality is trivial; when $\rho \in\left[0, \frac{1}{2} R\right)$, it follows from Lemma 4.18. \(\square\)

Lemma 4.20. If in addition $f \equiv 0$, then there is a constant $C=C(n, \boldsymbol{\beta})>0$ such that, for any $\rho \in(0, R)$,
$$\iint_{Q_{\rho}} u^{2} \omega_{\beta}^{n} d t \leq C\left(\frac{\rho}{R}\right)^{2 n+4} \iint_{Q_{R}} u^{2} \omega_{\beta}^{n} d t$$

Proof. The inequality is trivial in the case $\rho \in\left[\frac{1}{2} R, R\right]$, so we assume $\rho<\frac{1}{2} R$. First we observe that $\Delta_{\beta} u$ also satisfies the equations $\partial_{t}\left(\Delta_{\beta} u\right)=\Delta_{\beta}\left(\Delta_{\beta} u\right)$ and $\left.\left(\Delta_{\beta} u\right)\right|_{t=0} \equiv 0$, so (4-26) holds with $u^{2}$ replaced by $\left(\Delta_{\boldsymbol{\beta}} u\right)^{2}$, i.e.,
$$\iint_{Q_{\rho}}\left(\Delta_{\beta} u\right)^{2} \omega_{\beta}^{n} d t \leq C\left(\frac{\rho}{R}\right)^{2+2 n} \iint_{Q_{R}}\left(\Delta_{\beta} u\right)^{2} \omega_{\beta}^{n} d t .$$
Since $\left.u\right|_{t=0}=0$, we have $u(x, t)=\int_{0}^{t} \partial_{s} u(x, s) d s$, and we calculate
$$\begin{aligned}
\iint_{Q_{\rho}} u^{2} \leq \rho^{4} \iint_{Q_{\rho}}\left|\frac{\partial u}{\partial t}\right|^{2}=\rho^{4} \iint_{Q_{\rho}}\left(\Delta_{\beta} u\right)^{2} & \leq C \rho^{4}\left(\frac{\rho}{R}\right)^{2 n+2} \iint_{Q_{R / 2}}\left(\Delta_{\beta} u\right)^{2} \\
& \leq C\left(\frac{\rho}{R}\right)^{2 n+6} \iint_{Q_{R}} u^{2} \omega_{\beta}^{n} d t
\end{aligned} \quad \text { (by (4-25)) }$$ \(\square\)

Lemma 4.21. Let $u$ be a solution to (4-22). There exists a constant $C=C(n, \boldsymbol{\beta}, \alpha)>0$ such that
$$\frac{1}{\rho^{2 n+2+2 \alpha}} \iint_{Q_{\rho}}\left(\Delta_{\beta} u\right)^{2} \leq \frac{C}{R^{2 n+2+2 \alpha}} \iint_{Q_{R}}\left(\Delta_{\beta} u\right)^{2} \omega_{\beta}^{n} d t+C\left([f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right)^{2} .$$
Proof. Let $u=u_{1}+u_{2}$, where
$$\frac{\partial u_{1}}{\partial t}=\Delta_{\beta} u_{1}+f_{R} \quad \text { in } Q_{R}, \quad u_{1}=u \quad \text { on } \partial_{\mathcal{P}} Q_{R},$$
and
$$\frac{\partial u_{2}}{\partial t}=\Delta_{\beta} u_{2}+f-f_{R} \quad \text { in } Q_{R}, \quad u_{2}=0 \quad \text { on } \partial_{\mathcal{P}} Q_{R} .$$
The function $\Delta_{\beta} u_{1}$ satisfies the assumptions of Lemma 4.20. Thus
$$\iint_{Q_{\rho}}\left(\Delta_{\beta} u_{1}\right)^{2} \omega_{\beta}^{n} d t \leq C\left(\frac{\rho}{R}\right)^{2 n+4} \iint_{Q_{R}}\left(\Delta_{\beta} u_{1}\right)^{2} \omega_{\beta}^{n} d t .$$
Multiplying both sides of the equation for $u_{2}$ by $\dot{u}_{2}=\partial u_{2} / \partial t$ and noting that $\dot{u}_{2}=0$ on $\partial B_{R} \times\left(0, R^{2}\right)$, we get
$$\begin{aligned}
\int_{B_{R}}\left(\dot{u}_{2}\right)^{2} & =\int_{B_{R}} \dot{u}_{2} \Delta_{\beta} u_{2}+\dot{u}_{2}\left(f-f_{R}\right)=\int_{B_{R}}-2\left\langle\nabla \dot{u}_{2}, \nabla u_{2}\right\rangle+\dot{u}\left(f-f_{R}\right) \\
& \leq \int_{B_{R}}-\frac{\partial}{\partial t}\left|\nabla u_{2}\right|^{2}+\frac{1}{2}\left(\dot{u}_{2}\right)^{2}+2\left(f-f_{R}\right)^{2} .
\end{aligned}$$
Integrating over $t \in\left[0, R^{2}\right]$, we obtain
$$\iint_{Q_{R}}\left(\dot{u}_{2}\right)^{2} \leq-\left.2 \int_{B_{R}}\left|\nabla u_{2}\right|^{2}\right|_{t=R^{2}}+4 \iint_{Q_{R}}\left(f-f_{R}\right)^{2},$$
therefore
$$\iint_{Q_{R}}\left(\Delta_{\beta} u_{2}\right)^{2} \leq 2 \iint_{Q_{R}}\left(\dot{u}_{2}\right)^{2}+2 \iint_{Q_{R}}\left(f-f_{R}\right)^{2} \leq C R^{2 n+2+2 \alpha}\left([f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right)^{2} .$$

Then for $\rho<R$ we have
$$\begin{aligned}
\iint_{Q_{\rho}}\left(\Delta_{\beta} u\right)^{2} & \leq 2 \iint_{Q_{\rho}}\left(\Delta_{\beta} u_{1}\right)^{2}+2 \iint_{Q_{\rho}}\left(\Delta_{\beta} u_{2}\right)^{2} \\
& \leq C\left(\frac{\rho}{R}\right)^{2 n+4} \iint_{Q_{R}}\left(\Delta_{\beta} u_{1}\right)^{2} \omega_{\beta}^{n} d t+C R^{2 n+2+2 \alpha}\left([f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right)^{2} .
\end{aligned}$$
The estimate is proved by an iteration lemma (see Lemma 3.4 in [22]). \(\square\)

Lemma 4.22. Suppose u satisfies (4-22). There exists a constant $C=C(n, \boldsymbol{\beta}, \alpha)>0$ such that, for any $\rho \in\left(0, \frac{1}{2} R\right)$,
$$\iint_{Q_{\rho}}\left(\Delta_{\beta} u-\left(\Delta_{\beta} u\right)_{\rho}\right)^{2} \omega_{\beta}^{n} d t \leq C M_{R} \rho^{2 n+2+2 \alpha}$$
where
$$M_{R}:=\frac{1}{R^{4+2 \alpha}}\|u\|_{\mathscr{C}^{0}\left(Q_{R}\right)}^{2}+\frac{1}{R^{2 \alpha}}\|f\|_{\mathscr{C}^{0}\left(Q_{R}\right)}^{2}+\left([f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right)^{2} .$$
Proof. From Lemma 4.21, we get
$$\begin{aligned}
\iint_{Q_{\rho}}\left(\Delta_{\beta} u\right)^{2} & \leq C \rho^{2+2 n+2 \alpha}\left(\frac{1}{R^{2 n+2+2 \alpha}} \iint_{Q_{2 R / 3}}\left(\Delta_{\beta} u\right)^{2}+\left([f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{2 R / 3}\right)}\right)^{2}\right) \\
& \leq C \rho^{2+2 n+2 \alpha}\left(\frac{1}{R^{2 n+6+2 \alpha}} \iint_{Q_{R}} u^{2}+\frac{1}{R^{2 \alpha}}\|f\|_{C^{0}\left(Q_{R}\right)}^{2}+\left([f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right)^{2}\right) \\
& \leq C \rho^{2+2 n+2 \alpha} M_{R} .
\end{aligned}$$
On the other hand, by the Hölder inequality,
$$\left(\Delta_{\beta} u\right)_{\rho}^{2}=\frac{1}{\left|Q_{\rho}\right|_{g_{\beta}}^{2}}\left(\iint_{Q_{\rho}}\left(\Delta_{\beta} u\right) \omega_{\beta}^{n} d t\right)^{2} \leq \frac{C}{\rho^{2+2 n}} \iint_{Q_{\rho}}\left(\Delta_{\beta} u\right)^{2} \leq C M_{R} \rho^{2 \alpha} .$$
The lemma is proved by combining the two inequalities above. \(\square\)

By Campanato's lemma (see Theorem 3.1 in Chapter 3 of [22]), we get the following.
Corollary 4.23. There is a constant $C=C(n, \boldsymbol{\beta}, \alpha)>0$ such that, for any $x \in B_{\boldsymbol{\beta}}\left(0, \frac{3}{4}\right)$ and $R<\frac{1}{10}$,
$$\begin{aligned}
& {\left[\Delta_{\beta} u\right]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(x, R / 2) \times\left[0, R^{2} / 4\right]\right)}} \\
& \quad \leq C\left(\frac{1}{R^{2+\alpha}}\|u\|_{\mathscr{C}^{0}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}+\frac{1}{R^{\alpha}}\|f\|_{\mathscr{C}^{0}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}+[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}\right) .
\end{aligned}$$

Lemma 4.24. There exists a constant $C=C(n, \boldsymbol{\beta}, \alpha)>0$ such that, for any $x \in B_{\boldsymbol{\beta}}\left(0, \frac{3}{4}\right)$ and $R<\frac{1}{10}$,
$$\begin{aligned}
& {[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(x, R / 2) \times\left[0, R^{2} / 4\right]\right)}+\left[\frac{\partial u}{\partial t}\right]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(x, R / 2) \times\left[0, R^{2} / 4\right]\right)}} \\
& \quad \leq C\left(\frac{1}{R^{2+\alpha}}\|u\|_{\mathscr{C}^{0}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}+\frac{1}{R^{\alpha}}\|f\|_{\mathscr{C}^{0}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}+[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}\right) .
\end{aligned}$$

Proof. It follows from (4-27) and the elliptic Schauder estimates in Theorem 1.2 by adjusting $R$ slightly that, for any $t \in\left[0, \frac{1}{4} R^{2}\right]$,
$$\begin{aligned}
& {[T u(\cdot, t)]_{C_{\beta}^{0, \alpha}\left(B_{\beta}(x, R / 2)\right)}} \\
& \quad \leq C\left(\frac{1}{R^{2+\alpha}}\|u\|_{\mathscr{C}^{0}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}+\frac{1}{R^{\alpha}}\|f\|_{\mathscr{C}^{0}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}+[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(x, R) \times\left[0, R^{2}\right]\right)}\right),
\end{aligned}$$
that is, in the spatial variables the estimate (4-28) holds. It only remains to show the Hölder continuity of $T u$ in the time-variable. For this, we fix any two times $0 \leq t_{1}<t_{2} \leq \frac{1}{4} R^{2}$ and denote $r:=\frac{1}{2} \sqrt{t_{2}-t_{1}}$. For any $x_{0} \in B_{\beta}\left(x, \frac{1}{4} R\right), B_{\beta}\left(x_{0}, r\right) \subset B_{\beta}\left(x, \frac{1}{2} R\right)$. By (4-27) and the equation for $u$, it is not hard to see that the inequality (4-27) holds when $\Delta_{\beta} u$ on the left-hand side is replaced by $\dot{u}=\partial u / \partial t$. In particular,
$$\frac{\left|\dot{u}(y, t)-\dot{u}\left(y, t_{1}\right)\right|}{\left|t-t_{1}\right|^{\alpha / 2}} \leq A_{R} \quad \text { for all } y \in B_{\beta}\left(x, \frac{1}{2} R\right),$$
where $A_{R}$ is defined to be the constant on the right-hand side of (4-27). Integrating over $t \in\left[t_{1}, t_{2}\right]$ we get
$$\left|u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(y, t_{1}\right)\left(t_{2}-t_{1}\right)\right| \leq C A_{R}\left(t_{2}-t_{1}\right)^{1+\alpha / 2} .$$
Thus, for any $y \in B_{\beta}\left(x_{0}, r\right)$,
$$\begin{aligned}
\mid u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(x_{0}, t_{1}\right)\left(t_{2}\right. & \left.-t_{1}\right) \mid \\
& \leq\left|u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(y, t_{1}\right)\left(t_{2}-t_{1}\right)\right|+\left|\dot{u}\left(x_{0}, t_{1}\right)-\dot{u}\left(y, t_{1}\right)\right|\left(t_{2}-t_{1}\right) \\
& \leq C A_{R}\left(t_{2}-t_{1}\right)^{1+\alpha / 2}+A_{R} r^{\alpha}\left(t_{2}-t_{1}\right) .
\end{aligned}$$
Write
$$\tilde{u}(y):=u\left(y, t_{2}\right)-u\left(y, t_{1}\right)-\dot{u}\left(x_{0}, t_{1}\right)\left(t_{2}-t_{1}\right),$$
which is a function on $B_{\beta}\left(x_{0}, r\right)$. We have that the function $\tilde{f}:=\Delta_{\beta} \tilde{u}=\Delta_{\beta} u\left(\cdot, t_{2}\right)-\Delta_{\beta} u\left(\cdot, t_{1}\right)$ satisfies the inequalities $\|\tilde{f}\|_{C^{0}\left(B_{\beta}\left(x_{0}, r\right)\right)} \leq A_{R}\left(t_{2}-t_{1}\right)^{\alpha}$ and $[\tilde{f}]_{C_{\beta}^{0, \alpha}\left(B_{\beta}\left(x_{0}, r\right)\right)} \leq A_{R}$ by (4-27). It follows from the rescaled version of Proposition 3.32 that
$$|T \tilde{u}|_{C^{0}\left(B_{\beta}\left(x_{0}, r / 2\right)\right)} \leq C(n, \boldsymbol{\beta}, \alpha)\left(\frac{\|\tilde{u}\|_{C^{0}\left(B_{\beta}\left(x_{0}, r\right)\right)}}{r^{2}}+\|\tilde{f}\|_{C^{0}\left(B_{\beta}\left(x_{0}, r\right)\right)}+r^{\alpha}[\tilde{f}]_{C^{0, \alpha}\left(B_{\beta}\left(x_{0}, r\right)\right)}\right) \leq C\left(t_{2}-t_{1}\right)^{\alpha / 2} A_{R} .$$
Therefore, for any $x_{0} \in B_{\beta}\left(x, \frac{1}{4} R\right)$,
$$\frac{\left|T u\left(x_{0}, t_{2}\right)-T u\left(x_{0}, t_{1}\right)\right|}{\left|t_{2}-t_{1}\right|^{\alpha / 2}} \leq C A_{R} .$$
It is then easy to see by the triangle inequality that (adjusting $R$ slightly if necessary)
$$[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(B_{\beta}(x, R / 2) \times\left[0, R^{2} / 4\right]\right)} \leq C A_{R},$$
as desired. The estimate for $\dot{u}$ follows from the equation $\dot{u}=\Delta_{g} u+f$. \(\square\)

Remark 4.25. By a simple parabolic rescaling of the metric and time, we see from (4-28) that, for any $0<r<R<\frac{1}{10}$,
$$[T u]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{r}\right)} \leq C\left(\frac{\|u\|_{\mathscr{C}^{0}\left(Q_{R}\right)}}{(R-r)^{2+\alpha}}+\frac{\|f\|_{\mathscr{C}^{0}\left(Q_{R}\right)}}{(R-r)^{\alpha}}+[f]_{\mathscr{C}_{\beta}^{\alpha, \alpha / 2}\left(Q_{R}\right)}\right) .$$