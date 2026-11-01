---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Peak sections and Bergman kernels on Kähler manifolds with complex hyperbolic cusps]

Now we see that for each constant $\mu>0$, there are constants $C_{j}>0$ and $\epsilon_{l, j}>0, l=1,2, \cdots, k_{j}$, such that
$$\begin{aligned}
\varphi_{j}^{-1}\left(\left(\mathbb{D}_{r_{m} C_{j}}\right)^{k_{j}} \times B_{\frac{\epsilon_{j}}{2}}^{2 n-2 k_{j}}(0)\right) & \subset \bigcup_{l=1}^{k_{j}}\left(\bigcup_{y \in Z_{l} \backslash B_{\epsilon_{l, j} r_{m}}^{E u c, n}\left(\bigcup_{q>l} Z_{q}\right)} \widetilde{U}_{y, \epsilon_{l, j} r_{m}}\right) \\
& \subset \varphi_{j}^{-1}\left(\left(\mathbb{D}_{\mu r_{m}}\right)^{k_{j}} \times B_{\epsilon_{j}}^{2 n-2 k_{j}}(0)\right),
\end{aligned}$$
for sufficiently large $m$.
Clearly, we can find a small constant $\mu>0$ such that $\varphi_{j}^{-1}\left(\left(\mathbb{D}_{\mu r_{m}}^{*}\right)^{k_{j}} \times B_{\epsilon_{j}}^{2 n-2 k_{j}}(0)\right) \subset W_{r_{m}}$, for sufficiently large $m$. Then the open $\widetilde{U}_{y, \epsilon_{l}, j} r_{m}$ subsets in (74) are the open subsets we need.

Then we can prove the lemma by choosing $j=1, \cdots, N$ in the above argument. \(\square\)

This is the Poincarè type cusp version of Proposition 4.1. The proof of this proposition is similar to the proof of Proposition 4.1, except that Lemma 4.4 is replaced by Lemma 4.8.

Proposition 4.2. Given constants $k, \delta, \kappa, l>0$, there exists a constant $C>0$ depending only on $(M, \omega, \mathcal{L}, h), k, \delta, \kappa$ and $l$, satisfying the following property.

For any integer $m \in \mathbb{N}$, choose a constant $\gamma_{m} \geq r_{m}^{\kappa}$, a point $p_{m} \in W_{\gamma_{m}}$, and a linear functional $T_{m}$ defined by finite linear combination of $\delta_{p_{m}}$ and its derivatives. Assume that the order of derivatives contained in $T_{m}$ is at most $k, \forall m \in \mathbb{N}$. Suppose that there exists a sequence of open subsets $\left\{U_{m}\right\}_{m=1}^{\infty}$ of $M$ such that $\operatorname{dist}_{\omega}\left(W_{\gamma_{m}}, M \backslash U_{m}\right) \geq \delta \varepsilon_{m}, \forall m \in \mathbb{N}$. Then we have
$$\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}\right\| \geq\left(1-\frac{C}{m^{l}}\right)\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m},\left.\mathcal{L}^{m}\right|_{U_{m}}\right)}\right\| .$$

Remark. Note that for any point $p$ on the manifold $M$, we can choose a trivialization of $\mathcal{L}$ around $p$, so $\delta_{p}$ can still represent a linear functional on $H_{L^{2}}^{0}(M, \mathcal{L})$.

Proof. Without loss of generality, we can assume that $\kappa=\delta=1$. When $\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)}=0$, this proposition is obvious. So we can assume that $\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)} \neq 0$ from now.

Let $\beta>0$ be a large constant. When $p_{m} \notin W_{\gamma_{m}^{\beta}}$, analysis similar to that in the first part of the proof of Proposition 4.1 shows that (75) holds for some constant $C$ depending only on $(M, \omega, \mathcal{L}, h), k, \delta, \beta, \kappa$ and $l$.

Now we assume that $p_{m} \in W_{\gamma_{m}^{\beta}}$. In this case, by replacing Lemma 4.4 with Lemma 4.8, we can apply the argument in the second part in the proof of Proposition 4.1 to give a proof of this proposition, and the proof is complete. \(\square\)

The next result is an analogy of Corollary 4.2 on Kähler manifolds with Poincarè type cusps, and it is also a corollary of Lemma 4.5.

Corollary 4.3. Given $\epsilon, \kappa, \beta, k>0$, there exists a constant $C>0$ depending only on $(M, \omega), \epsilon, \kappa$, $\beta$ and $k$ satisfying the following property.

Let $U_{m}$ be an open subset of $M$ containing $W_{r_{m}^{\kappa}}$ for some integer $m \geq C$, and $\widetilde{U}_{m}$ be an open subset of $U_{m}$ such that $\operatorname{dist}_{\omega}\left(\widetilde{U}_{m}, M \backslash U_{m}\right) \geq \epsilon \varepsilon_{m}$. Then for any $S \in H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)$, we have $\left\|\nabla^{k} S(x)\right\|^{2}+\left\|\nabla^{* k} S^{*}(x)\right\|^{2} \leq C m^{C}|\log \bar{d}(x)|^{-\beta}\|S\|_{L^{2} ; U_{m}}^{2}, \forall x \in \widetilde{U}_{m}$, where $S^{*}$ is the smooth section of $\mathcal{L}^{-m}$ given by $S^{*}(e)=h^{m}(e, S)$, and $\nabla^{*}$ is the Chern conncection of the Hermitian line bundle $\left(\mathcal{L}^{-m}, h^{-m}\right)$.

Proof. By the compactness of the divisor $D \subset \bar{M}$, we can find points $\widetilde{y}_{j} \in D, j=1, \cdots, N$, open neighborhoods $\widetilde{U}_{j}$ of $\widetilde{y}_{j}$ in $\bar{M}$, and biholomorphic maps
$$\varphi_{j}=\left(z_{j, 1} \cdots, z_{j, n}\right): \widetilde{U}_{j} \rightarrow\left(\mathbb{D}_{\epsilon_{j}}\right)^{k_{j}} \times B_{\epsilon_{j}}^{2 n-2 k_{j}}(0)$$
such that $\varphi_{j}\left(\widetilde{y}_{j}\right)=0, \varphi_{j}\left(\widetilde{U}_{j} \backslash D\right)=\left(\mathbb{D}_{\epsilon_{j}}^{*}\right)^{k_{j}} \times B_{\epsilon_{j}}^{2 n-2 k_{j}}(0), D \subset \cup_{j=1}^{N} \varphi_{j}^{-1}\left(\left(\mathbb{D}_{\epsilon_{j}^{2}}\right)^{k_{j}} \times B_{\epsilon_{j}^{2}}^{2 n-2 k_{j}}(0)\right)$, and $\left(\varphi_{j}^{-1}\right)^{*} \omega=-\sqrt{-1} \sum_{i=1}^{k_{j}} \partial \bar{\partial} \log \left(\log \left|z_{i}\right|^{2}\right)+\pi_{k_{j}, n}^{*} \omega_{j}+\sqrt{-1} \partial \bar{\partial} u_{j}$, where $\epsilon_{j}>0$ are constants, $\omega_{j}$ is a Kähler metric on $B_{\epsilon_{j}}^{2 n-2 k_{j}}(0)$, and $u_{j}=\cap_{i=1}^{k_{j}} O\left(|\log | z_{j, i}| |^{-\alpha}\right)$ as $\inf _{1 \leq i \leq k_{x}}\left|z_{j, i}\right| \rightarrow 0^{+}$to all orders with respect to $\omega_{\text {mod }}$.

Fix $j \in\{1, \cdots, N\}$. Let $\gamma_{m}=e^{-m^{2+2 \alpha^{-1}}}$. Now we consider the Bergman kernel functions on $\widetilde{U}_{\widetilde{y}_{j}, \gamma_{m}, \epsilon, l}=\varphi_{j}^{-1}\left(\left(\mathbb{D}_{\epsilon}^{*}\right)^{l-1} \times \mathbb{D}_{\gamma_{m}}^{*} \times\left(\mathbb{D}_{\epsilon}^{*}\right)^{k_{j}-l} \times B_{\epsilon}^{2 n-2 k_{j}}(0)\right) \subset \widetilde{U}_{j} \backslash D, l=1, \cdots, k_{j}$.

As in the proof of Corollary 4.2, we only need to find a constant $C_{j, l, \beta}>0$ independent of $m$, such that for sufficiently large integer $m$,
$$\rho_{\widetilde{U}_{\widetilde{y}_{j}, \gamma m, \epsilon_{j}, l}, \varphi_{j}^{*} \omega_{\bmod }, m}(x) \leq C_{j, l, \beta} m^{C_{j, l, \beta}}|\log | z_{j, l}(x)| |^{-\beta-2 n}, \quad \forall x \in \widetilde{U}_{\widetilde{y}_{j}, \gamma_{m}^{e}, \epsilon_{j}^{2}, l} .$$

By a straightforward calculation, one can obtain
$$\begin{aligned}
\rho_{\widetilde{U}_{\widetilde{y}_{j}}, \gamma_{m}, \epsilon_{j}, l, \varphi_{j}^{*} \omega_{\text {mod }}, m}(x)= & \left(\prod_{\substack{1 \leq i \leq k_{j} \\
i \neq l}} \rho_{\mathbb{D}_{\epsilon_{j}}^{*}, \omega_{\text {mod }}, m}\left(z_{j, i}(x)\right)\right) \cdot \rho_{\mathbb{D}_{\gamma m}^{*}, \omega_{\text {mod }}, m}\left(z_{j, l}(x)\right) \\
& \cdot \rho_{B_{\epsilon_{j}}^{2 n-2 k_{j}}(0), \omega_{E u c}, m}\left(z_{j, k_{j}+1}(x), \cdots, z_{j, n}(x)\right) .
\end{aligned}$$
Combining Corollary 3.1 with Tian-Yau-Zelditch expansion, we see that there exists a constant $C_{1}=C_{1}(n)>0$ such that $\rho_{\widetilde{U}_{\widetilde{y}_{j}, \gamma m, \epsilon_{j}, l}, \varphi_{j}^{*} \omega_{\text {mod }}, m}(x) \leq C_{1} m^{\frac{3 n}{2}} \rho_{\mathbb{D}_{\gamma_{m}}^{*}, \omega_{\text {mod }}, m}\left(z_{j, l}(x)\right)$ for sufficiently large $m$. It is sufficient to show that $\rho_{\mathbb{D}_{\gamma m}^{*}, \omega_{\text {mod }}, m}(z) \leq C_{2} m^{C_{2}}|\log | z| |^{-\beta-2 n}, \forall z \in \mathbb{D}_{\gamma_{m}^{e}}^{*}$, which is shown in the proof of Corollary 4.2. This completes the proof. \(\square\)

We conclude this section by proving Proposition 1.1.
Proof of Theorem 1.1: Fix $l \in \mathbb{N}$ at first. We only need to show this theorem in the case where $\xi=\kappa=1$, the more general case is then a fairly immediate consequence.

Similar to the proof of Proposition 1.1, we also split the proof of this theorem into two parts, proving estimates (12) and (13) respectively.

Part 1: First, we need to prove (12).
Set $\left(x_{m}, y_{m}\right) \in V_{m} \times\left(M \backslash U_{m}\right)$. Choosing vectors $\left.e_{x_{m}} \in \mathcal{L}^{m}\right|_{x_{m}}$ and $\left.e_{y_{m}} \in \mathcal{L}^{m}\right|_{y_{m}}$ such that $\left\|e_{x_{m}}\right\|=\left\|e_{y_{m}}\right\|=1$. Let $k_{1}, k_{2} \in \mathbb{Z}_{\geq 0}$ such that $k_{1}+k_{2} \leq k$. Consider the unit tangent vectors $v_{1, m}, \cdots, v_{k_{1}, m} \in T_{x_{m}} M \oplus 0 \subset T_{\left(x_{m}, y_{m}\right)}(M \times M)$, and $v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m} \in 0 \oplus T_{y_{m}} M \subset$ $T_{\left(x_{m}, y_{m}\right)}(M \times M)$. Now we can define bounded linear functionals on small neighborhoods of $x_{m}$ and $y_{m}$ as following:
$$\begin{aligned}
\nabla^{k_{1}} S\left(v_{1, m}, \cdots, v_{k_{1}, m}\right) & =T_{1, m}(S) e_{x_{m}}, \\
\nabla^{* k_{2}} S^{*}\left(v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m}\right) & =T_{2, m}(S) e_{y_{m}}^{*},
\end{aligned}$$
for any holomorphic section $S$ of $\mathcal{L}^{m}$ around $x_{m}$ and $y_{m}$, respectively. Then we have
$$\left\|\nabla_{x}^{k_{1}} \nabla_{y}^{* k_{2}} B_{\omega, m}\left(x_{m}, y_{m}\right)\left(v_{1, m}, \cdots, v_{k_{1}+k_{2}, m}\right)\right\|=\left|T_{1, m}\left(S_{T_{1, m}}\right) \overline{T_{2, m}\left(S_{T_{1, m}}\right)}\right|,$$
where $\left\{S_{j}\right\}_{j \in J}$ is an $L^{2}$-orthonormal basis of $H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$, and $S_{T_{1, m}} \in H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$ is the peak section of the functional $T_{1, m}$ on $M$. Since $u=o(1)$ as $h_{D} \rightarrow 0^{+}$, we can find a sequence of open subsets $\left\{\widetilde{U}_{m}\right\}_{m=2}^{\infty}$ and a constant $\epsilon>0$ independent of $m$ such that
$$\inf \left(\operatorname{dist}_{\omega}\left(V_{m}, M \backslash \widetilde{U}_{m}\right), \operatorname{dist}_{\omega}\left(\widetilde{U}_{m}, M \backslash U_{m}\right)\right) \geq \epsilon \frac{\log m}{\sqrt{m}}, \quad \forall m \in \mathbb{N},$$
and Lemma 4.7 now shows that there exists a constant $\delta \in(0, \epsilon)$ independent of $m$ such that $\operatorname{inj}\left(M \backslash V_{m}\right) \geq \delta \frac{\log (m)}{\sqrt{m}}$. By Corollary 4.3, we see that there exists a constant $C_{0}>0$ depending only on $(M, \omega, \mathcal{L}, h)$ and $k$, such that
$$\left.\left|\log \bar{d}\left(x_{m}\right)\right|^{2 \beta}| | T_{1, m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}| |+\left.\left|\log \bar{d}\left(y_{m}\right)\right|^{2 \beta}| | T_{2, m}\right|_{H_{L^{2}}^{0}\left(B_{\frac{\delta \log _{\frac{m}{3}}^{m}}{}, \mathcal{L}^{m}}\right)} \| \leq C_{0} m^{C_{0}}, \quad \forall m \in \mathbb{N},$$
where $\epsilon>0$ is a constant independent of $m$. By using Lemma 4.1 and Proposition 4.2 to $V_{m}$ and $\widetilde{U}_{m}$, we can conclude that for each integer $q \in \mathbb{N}$, there exists a constant $C_{1}>0$ depending only on $(M, \omega, \mathcal{L}, h), k$ and $q$, such that
$$\int_{M \backslash \widetilde{U}_{m}}\left\|S_{T_{1, m}}\right\|^{2} d \operatorname{Vol}_{\omega} \leq C_{1} m^{-q}, \quad \forall m \in \mathbb{N} .$$
Choosing $q=2 l+4+4\left\lfloor C_{0}\right\rfloor$, where $\lfloor\cdot\rfloor$ is the greatest integer function. It follows that
$$\begin{aligned}
\left|T_{1, m}\left(S_{T_{1, m}}\right) \overline{T_{2, m}\left(S_{T_{1, m}}\right)}\right| & \leq\left\|T_{1, m}\right\| \cdot\left\|\left.T_{2, m}\right|_{H_{L^{2}}^{0}\left(B_{\frac{\delta 1 \log m}{\sqrt{m}}}, \mathcal{L}^{m}\right)}\right\| \cdot\left\|S_{T_{1, m}}\right\|_{L^{2} ; B_{\frac{\delta 1 \log m}{\sqrt{m}}}} \\
& \leq C_{0}^{2} C_{1} m^{2 C_{0}} m^{-l-2-2\left\lfloor C_{0}\right\rfloor}\left|\log \bar{d}\left(x_{m}\right)\right|^{-\beta}\left|\log \bar{d}\left(y_{m}\right)\right|^{-\beta} \\
& \leq C_{0}^{2} C_{1} m^{-l}\left|\log \bar{d}\left(x_{m}\right)\right|^{-\beta}\left|\log \bar{d}\left(y_{m}\right)\right|^{-\beta} .
\end{aligned}$$
Hence we can conclude that
$$\sup _{V_{m} \times\left(M \backslash U_{m}\right)}|\log \bar{d}(x)|^{\beta}|\log \bar{d}(y)|^{\beta}\left\|B_{\omega, m}(x, y)\right\|_{C^{k}} \leq C m^{-l} .$$
By exchanging $x_{m}$ and $y_{m}$, one can see that the proof of
$$\sup _{\left(M \backslash U_{m}\right) \times V_{m}}|\log \bar{d}(x)|^{\beta}|\log \bar{d}(y)|^{\beta}\left\|B_{\omega, m}(x, y)\right\|_{C^{k}} \leq C m^{-l}$$
is similar to the argument above.
Part 2. It remains to prove (13).
Set $\left(x_{m}, y_{m}\right) \in V_{m} \times V_{m}$. Let $\left.e_{x_{m}} \in \mathcal{L}^{m}\right|_{x_{m}}$ and $\left.e_{y_{m}} \in \mathcal{L}^{m}\right|_{y_{m}}$ such that $\left\|e_{x_{m}}\right\|=\left\|e_{y_{m}}\right\|=1$. Choosing $k_{1}, k_{2} \in \mathbb{Z}_{\geq 0}$ such that $k_{1}+k_{2} \leq k$, unit tangent vectors $v_{1, m}, \cdots, v_{k_{1}, m} \in T_{x_{m}} M \oplus 0 \subset$ $T_{\left(x_{m}, y_{m}\right)}(M \times M)$, and $v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m} \in 0 \oplus T_{y_{m}} M \subset T_{\left(x_{m}, y_{m}\right)}(M \times M)$. Now we can define bounded linear functionals on $V_{\gamma_{m}}$ as following:
$$\begin{aligned}
\nabla^{k_{1}} S\left(v_{1, m}, \cdots, v_{k_{1}, m}\right) & =T_{1, m}(S) e_{x_{m}}, \\
\nabla^{* k_{2}} S^{*}\left(v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m}\right) & =T_{2, m}(S) e_{y_{m}}^{*},
\end{aligned}$$
for any $S \in H_{L^{2}}^{0}\left(V_{m}, \mathcal{L}^{m}\right)$. Let $S_{T_{U_{m}, 1, m}} \in H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)$ and $S_{T_{1, m}} \in H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$ denote the peak sections of the functional $T_{1, m}$ on $U_{m}$ and $M$, respectively. As in the argument in Part 1, a straightforward computation shows that
$$\begin{aligned}
& \left\|\nabla_{x}^{k_{1}} \nabla_{y}^{* k_{2}}\left(B_{\omega, m}\left(x_{m}, y_{m}\right)-B_{U_{m}, \omega, m}\right)\left(x_{m}, y_{m}\right)\left(v_{1, m}, \cdots, v_{k_{1}+k_{2}, m}\right)\right\| \\
= & \left\|\left(T_{1, m}\left(S_{T_{1, m}}\right) \overline{T_{2, m}\left(S_{T_{1, m}}\right)}-T_{1, m}\left(S_{T_{U_{m}, 1, m}}\right) \overline{T_{2, m}\left(S_{T_{U_{m}, 1, m}}\right)}\right) e_{x_{m}} \otimes e_{y_{m}}^{*}\right\| \\
\leq & \left|T_{1, m}\left(S_{T_{1, m}}-S_{T_{U_{m}, 1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{U_{m}, 1, m}}\right)\right|+\left|T_{1, m}\left(S_{T_{1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}-S_{T_{U_{m}, 1, m}}\right)\right| .
\end{aligned}$$
By Corollary 4.3, we see that there exists a constant $C_{2}>0$ depending only on $(M, \omega, \mathcal{L}, h)$ and $k$, such that
$$\left.\left|\log \bar{d}\left(x_{m}\right)\right|^{2 \beta}| | T_{1, m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)}| |+\left.\left|\log \bar{d}\left(y_{m}\right)\right|^{2 \beta}| | T_{2, m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)} \| \leq C_{2} m^{C_{2}}, \quad \forall m \in \mathbb{N},$$
where $\epsilon>0$ is a constant independent of $m$. Combining Lemma 4.1 and Proposition 4.2, we see that for each given integer $q \in \mathbb{N}$, there exists a constant $C_{3}>0$ depending only on $(M, \omega, \mathcal{L}, h), k$
and $q$, such that
$$\int_{V_{\sigma_{m}}}\left\|S_{T_{1, m}}-S_{T_{U_{m}, 1, m}}\right\|^{2} d \operatorname{Vol}_{\omega} \leq C_{3} m^{-q}, \quad \forall m \in \mathbb{N} .$$
Choosing $q=2 l+4+4\left\lfloor C_{2}\right\rfloor$, where $\lfloor\cdot\rfloor$ is the greatest integer function. Then we have
$$\begin{aligned}
& \left|T_{1, m}\left(S_{T_{1, m}}-S_{T_{U_{m}, 1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{U_{m}, 1, m}}\right)\right|+\left|T_{1, m}\left(S_{T_{1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}-S_{T_{U_{m}, 1, m}}\right)\right| \\
\leq & 2\left\|\left.T_{1, m}\right|_{H_{L^{2}}^{0}\left(U_{M}, \mathcal{L}^{m}\right)}\right\| \cdot\left\|\left.T_{2, m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)}\right\| \cdot\left\|S_{T_{1, m}}-S_{T_{U_{m}, 1, m}}\right\|_{L^{2} ; U_{m}} \\
\leq & 2 C_{2}^{2} C_{3} m^{2 C_{0}} m^{-l-2-2\left\lfloor C_{2}\right\rfloor}\left|\log \bar{d}\left(x_{m}\right)\right|^{-\beta}\left|\log \bar{d}\left(y_{m}\right)\right|^{-\beta} \\
\leq & 2 C_{2}^{2} C_{3} m^{-l}\left|\log \bar{d}\left(x_{m}\right)\right|^{-\beta}\left|\log \bar{d}\left(y_{m}\right)\right|^{-\beta} .
\end{aligned}$$
Then we can obtain the estimate (13), and the theorem follows. \(\square\)

\section*{5. Bergman kernels in two special cases}

In this section, we consider the Bergman kernels on complex hyperbolic cusps with Kähler-Einstein metrics and quotients of complex ball.

\subsection*{5.1. Bergman kernels on complex hyperbolic cusps with Kähler-Einstein metrics.}

Let $(M, \omega)$ be a Kähler manifold and let $(\mathcal{L}, h)$ be a Hermitian line bundle on $M$ such that $\operatorname{Ric}(h) \geq \epsilon \omega$ and $\operatorname{Ric}(\omega) \geq-\Lambda \omega$ for some constants $\epsilon, \Lambda>0$. Suppose that $M$ is pseudoconvex if $(M, \omega)$ is not complete. Assume that $U \cong V_{r} / \Gamma_{V}$ is an asymptotic complex hyperbolic cusp on $(M, \omega, \mathcal{L}, h)$ such that $(U, \omega)$ is a Kähler-Einstein manifold with $\operatorname{Ric}(\omega)=-(n+1) \omega$, and $\bar{U}$ is complete. By definition, $\omega=\omega_{V}-\sqrt{-1} \partial \bar{\partial} f$ for some function $f \in C^{\infty}\left(\bar{V}_{r} / \Gamma_{V}\right)$.

First, we show that $U$ is an asymptotic complex hyperbolic cusp of order $\infty$. Since $\pi_{V}^{*} \omega$ is a Kähler-Einstein metric on $V_{r}$, we only need to consider the case $\Gamma_{V}=0$.

For each constant $t>0$, we denote the restriction of the scalar multiplication $v \rightarrow t v$ on the domain $V_{t^{-1}} \subset \mathcal{L}_{D}$ as $\Phi_{t}$. By definition, $\Phi_{t}: V_{t^{-1}} \rightarrow V_{1}=V$ is a biholomorphic map. The pullbacks $\Phi_{t}^{*} \mathcal{L}_{V}$ and $\Phi_{t}^{*} \mathcal{L}_{V}^{-1}$ are holomorphic line bundles on $V_{t^{-1}}$, and the Bergman kernels satisfying that $\Phi_{t}^{*} B_{V, \omega_{V}, m}=B_{V_{t-1}, \Phi_{t}^{*} \omega_{V}, m}$ on $V_{t^{-1}} \times V_{t^{-1}}$. Note that $\Phi_{t}^{*} e_{\mathcal{L}_{V}}$ is a non-vanishing holomorphic section on $V_{t^{-1}}$ and $\left\|\Phi_{t}^{*} e_{\mathcal{L}_{V}}\right\|=\left|\log h_{D} \circ \Phi_{t}\right|$, so we see that $\Phi_{t}^{*} \mathcal{L}_{V}$ and $\Phi_{t}^{*} \mathcal{L}_{V}^{-1}$ are trivial line bundles on $V_{t^{-1}}$. Now we regard $\left(\Phi_{t}^{*} \mathcal{L}_{V}, \Phi_{t}^{*} h_{V}\right)$ and $\left(\Phi_{t}^{*} \mathcal{L}_{V}^{-1}, \Phi_{t}^{*} h_{V}^{-1}\right)$ as the restriction of holomorphic line bundles $\mathcal{L}_{V}$ and $\mathcal{L}_{V}^{-1}$ on $V \cap V_{t^{-1}}$ respectively, just replace the Hermitian metrics $h_{V}$ and $h_{V}^{-1}$ with the Hermitian metrics $\left\|\Phi_{t}^{*} e_{\mathcal{L}_{V}}\right\| \cdot\left\|e_{\mathcal{L}_{V}}\right\|^{-1} h_{V}$ and $\left\|e_{\mathcal{L}_{V}}\right\| \cdot\left\|\Phi_{t}^{*} e_{\mathcal{L}_{V}}\right\|^{-1} h_{V}^{-1}$, respectively. Therefore, the pull back of the Bergman kernels, $\Phi_{t}^{*} B_{V, \omega_{V}, m}$, can be regarded as the $\pi_{1}^{*} \mathcal{L}_{V} \otimes \pi_{2}^{*} \mathcal{L}_{V}^{-1}$-valued functions on $\left(V \cap V_{t^{-1}}\right) \times\left(V \cap V_{t^{-1}}\right)$. By considering the change of the Hermitian line bundle under the mapping $\Phi_{t}$, we can prove the following lemma.

Lemma 5.1. Let $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$ be an $n$-dimensional complex hyperbolic cusp, $t>0$ be a constant, and $\Phi_{t}: V_{t^{-1}} \rightarrow V$ be the restriction of the scalar multiplication $v \mapsto t v$ on $V_{t^{-1}} \subset \mathcal{L}_{D}$.

Then we have $\Phi_{t}^{*} \omega_{V}=\omega_{V}-\sqrt{-1} \partial \bar{\partial} \log \left(1-2 \log t\left|\log h_{D}\right|^{-1}\right)$ on $V \cap V_{t^{-1}}$.

Proof. By definition, we have $\omega_{V}=-\sqrt{-1} \partial \bar{\partial} \log \left|\log h_{D}\right|$, and hence
$$\begin{aligned}
\Phi_{t}^{*} \omega_{V} & =-\sqrt{-1} \Phi_{t}^{*}\left(\partial \bar{\partial} \log \left|\log h_{D}\right|\right)=-\sqrt{-1} \partial \bar{\partial} \log \left|\log h_{D} \circ \Phi_{t}\right| \\
& =-\sqrt{-1} \partial \bar{\partial} \log \left|\log t^{2} h_{D}\right|=-\sqrt{-1} \partial \bar{\partial} \log \left(\left|\log h_{D}\right|-2 \log t\right) \\
& =-\sqrt{-1} \partial \bar{\partial} \log \left|\log h_{D}\right|-\sqrt{-1} \partial \bar{\partial} \log \left(1-2 \log t\left|\log h_{D}\right|^{-1}\right) \\
& =\omega_{V}-\sqrt{-1} \partial \bar{\partial} \log \left(1-2 \log t\left|\log h_{D}\right|^{-1}\right), \text { on } V \cap V_{t^{-1}} .
\end{aligned}$$
This establishes the formula. \(\square\)

Combining Lemma 5.1 with Fu-Hein-Jiang's estimate (4), we see that $U$ is an asymptotic complex hyperbolic cusp of order $\infty$ by choosing $t=e^{-\frac{c_{r}, f}{2}}$, where $c_{r, f}$ is the constant in (4).

We now come to the proof of Theorem 1.2. Here $r_{m}$ denotes $e^{-\frac{\sqrt{m}}{\log m}}$ for $m \geq 2$.
Proof of Theorem 1.2: Without loss of generality, we can assume that $\Gamma_{V}=0$. By definition, there exists a smooth function $u$ on $U$ such that $(U, \omega, \mathcal{L}, h) \cong\left(V_{r}, \omega_{V}-\sqrt{-1} \partial \bar{\partial} u, \mathcal{L}_{V}, e^{u} h_{V}\right)$ and for any $\alpha>0, u=O\left(\left|\log h_{D}\right|^{-\alpha}\right)$ as $h_{D} \rightarrow 0^{+}$to all orders with respect to $\omega_{V}$.

We divide our proof into three parts.
Part 1. At first, we prove estimate (5).
By definition, we see that $U$ is an asymptotic complex hyperbolic cusp on $(M, \omega, \mathcal{L}, h)$, and hence the estimate (5) is a consequence of the localization principle (1).

Part 2. We now start to consider estimate (6).
By the localization principle (2), one can see that the estimate (6) can be localized, and hence we only need to show that there are constants $m_{0}, C>0$ independent of $m$, such that
$$\sup _{V_{r_{m}} \times V_{r_{m}}}\left|\log h_{D}(x)\right|^{\beta}\left|\log h_{D}(y)\right|^{\beta}\left\|B_{V_{\sqrt{r_{m}}}, \omega, m}(x, y)-B_{V_{\sqrt{r_{m}}}, \omega_{V}, m}(x, y)\right\|_{C^{k} ; h_{V}^{m}, \omega_{V}} \leq C m^{-l},$$
for any $m \geq m_{0}$. Choosing a large integer $m_{1}$ such that $r_{m} \leq r^{4}, \forall m \geq m_{1}$. Fix an integer $m \geq m_{1}$ and a point $\left(x_{m}, y_{m}\right) \in V_{r_{m}} \times V_{r_{m}}$. Let $\left.e_{x_{m}} \in \mathcal{L}_{V}^{m}\right|_{x_{m}}$ and $\left.e_{y_{m}} \in \mathcal{L}_{V}^{m}\right|_{y_{m}}$ such that $\left\|e_{x_{m}}\right\|_{h_{V}^{m}}=\left\|e_{y_{m}}\right\|_{h_{V}^{m}}=1$. Choosing nonnegative integers $k_{1}, k_{2}$ such that $k_{1}+k_{2} \leq k$, unit tangent vectors $v_{1, m}, \cdots, v_{k_{1}, m} \in T_{x_{m}} V \oplus 0 \subset T_{\left(x_{m}, y_{m}\right)}(V \times V)$, and unit tangent vectors $v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m} \in 0 \oplus T_{y_{m}} V \subset T_{\left(x_{m}, y_{m}\right)}(V \times V)$. Here the metric we consider is $\omega_{V}$. It is easy to see that $H_{L^{2}}^{0}\left(V_{\sqrt{\gamma_{m}}}, \omega, \mathcal{L}_{V}^{m}, h^{m}\right)=H_{L^{2}}^{0}\left(V_{\sqrt{\gamma_{m}}}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$ as vector subspaces of $H^{0}\left(V_{\sqrt{\gamma_{m}}}, \mathcal{L}_{V}^{m}\right)$, and the $L^{2}$-norms are equivalent. Now we can define bounded linear functionals on $V_{\gamma_{m}}$ as following:
$$\begin{aligned}
\nabla^{k_{1}} S\left(v_{1, m}, \cdots, v_{k_{1}, m}\right) & =T_{1, m}(S) e_{x_{m}}, \\
\nabla^{* k_{2}} S^{*}\left(v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m}\right) & =T_{2, m}(S) e_{y_{m}}^{*},
\end{aligned}$$
for any $S \in H_{L^{2}}^{0}\left(V_{\gamma_{m}}, \mathcal{L}_{V}^{m}\right)$. Let $S_{T_{i, m}} \in H_{L^{2}}^{0}\left(V_{\sqrt{\gamma_{m}}}, \mathcal{L}_{V}^{m}\right)$ and $S_{T_{i, m}}^{\prime} \in H_{L^{2}}^{0}\left(V_{\sqrt{\gamma_{m}}}, \mathcal{L}_{V}^{m}\right)$ denote the peak sections of the functional $T_{i, m}$ on $V_{\sqrt{\gamma_{m}}}$ associated with $(h, \omega)$ and $\left(h_{V}, \omega_{V}\right)$, respectively. By
a straightforward computation, we can conclude that
$$\begin{aligned}
& \left\|\nabla_{x}^{k_{1}} \nabla_{y}^{* k_{2}}\left(B_{V_{\sqrt{m} m}, \omega, m}(x, y)-B_{V_{\sqrt{m} m}, \omega_{V}, m}(x, y)\right)\left(x_{m}, y_{m}\right)\left(v_{1, m}, \cdots, v_{k_{1}+k_{2}, m}\right)\right\|_{h_{V}^{m}} \\
= & \left\|\left(T_{1, m}\left(S_{T_{1, m}}\right) \overline{T_{2, m}\left(S_{T_{1, m}}\right)}-T_{1, m}\left(S_{T_{1, m}}^{\prime}\right) \overline{T_{2, m}\left(S_{T_{1, m}}^{\prime}\right)}\right) e_{x_{m}} \otimes e_{y_{m}}^{*}\right\|_{h_{V}^{m}} \\
\leq & \left|T_{1, m}\left(S_{T_{1, m}}-S_{T_{1, m}}^{\prime}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}^{\prime}\right)\right|+\left|T_{1, m}\left(S_{T_{1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}-S_{T_{1, m}}^{\prime}\right)\right| .
\end{aligned}$$
By Corollary 4.2, we see that there exists a constant $C_{1}>0$ independent of $m$, such that
$$\left.\left|\log h_{D}\left(x_{m}\right)\right|^{2 \beta}| | T_{1, m}\right|_{H_{L^{2}}^{0}\left(V_{\sqrt{r_{m}}}, \mathcal{L}_{V}^{m}\right)}| |+\left.\left|\log h_{D}\left(y_{m}\right)\right|^{2 \beta}| | T_{2, m}\right|_{H_{L^{2}}^{0}\left(V_{\sqrt{r_{m}}}, \mathcal{L}_{V}^{m}\right)} \| \leq C_{1} m^{C_{1}}, \quad \forall m \in \mathbb{N},$$
where $\epsilon>0$ is a constant independent of $m$. The norm we used here is the norm associated with the metric $\omega_{V}$ and the Hermitian metric $h_{V}^{m}$. Combining Fu-Hein-Jiang's estimate (4) with Lemma 4.2, we see that for each given integer $q \in \mathbb{N}$, there exists a constant $C_{2}>0$ depending only on $V, r$ and $q$, such that
$$\int_{V_{\sqrt{r_{m}}}}\left\|S_{T_{1, m}}-S_{T_{1, m}}^{\prime}\right\|_{h_{V}^{m}}^{2} d \operatorname{Vol}_{\omega_{V}} \leq C_{2} m^{-q}, \quad \forall m \in \mathbb{N} .$$
Choosing $q=2 l+4+4\left\lfloor C_{2}\right\rfloor$, where $\lfloor\cdot\rfloor$ is the greatest integer function. Then we have
$$\begin{aligned}
& \left|T_{1, m}\left(S_{T_{1, m}}-S_{T_{1, m}}^{\prime}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}^{\prime}\right)\right|+\left|T_{1, m}\left(S_{T_{1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}-S_{T_{1, m}}^{\prime}\right)\right| \\
\leq & 2\left\|\left.T_{1, m}\right|_{H_{L^{2}}^{0}\left(V_{\sqrt{r_{m}}}, \mathcal{L}^{m}\right)}\right\| \cdot\left\|\left.T_{2, m}\right|_{H_{L^{2}}^{0}\left(V_{\sqrt{r_{m}}}, \mathcal{L}^{m}\right)}\right\| \cdot\left\|S_{T_{1, m}}-S_{T_{1, m}}^{\prime}\right\|_{L^{2} ; V_{\sqrt{r_{m}}}, h_{V}^{m}, \omega_{V}} \\
\leq & 2 C_{1}^{2} C_{2} m^{2 C_{0}} m^{-l-2-2\left\lfloor C_{2}\right\rfloor}\left|\log h_{D}\left(x_{m}\right)\right|^{-\beta}\left|\log h_{D}\left(y_{m}\right)\right|^{-\beta} \\
\leq & 2 C_{1}^{2} C_{2} m^{-l}\left|\log h_{D}\left(x_{m}\right)\right|^{-\beta}\left|\log h_{D}\left(y_{m}\right)\right|^{-\beta} .
\end{aligned}$$
Then we can obtain the estimate (6).
Part 3. In this part, we prove the inequality (7).
For any point $x \in V_{r}$, we choose a vector $\left.e_{x} \in \mathcal{L}_{V}\right|_{x}$ such that $\left\|e_{x}\right\|_{h_{V}}=1$. Hence we can define bounded linear functionals $T_{x, m} \in H_{L^{2}}^{0}\left(V_{r_{m}}, \mathcal{L}_{V}^{m}\right)^{*}$ by $\left.S\right|_{x}=T_{x, m}(S) e_{x}^{m}, \forall S \in H_{L^{2}}^{0}\left(V_{r_{m}}, \mathcal{L}_{V}^{m}\right)$, where $m>0$ is an integer such that $r_{m} \leq r^{4}$, and $x \in V_{r_{m}}$. For any open subset $U^{\prime}$ of $V$ containing $x$, we denote the peak sections of $T_{x, m}$ on $H_{L^{2}}^{0}\left(U^{\prime}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$ as $S_{U^{\prime}, x, m}^{\prime}$. Similarly, for any open subset $U^{\prime}$ of $M$ containing $x$, we will denote by $S_{U^{\prime}, x, m}$ the peak sections of $T_{x, m}$ on $H_{L^{2}}^{0}\left(U^{\prime}, \omega, \mathcal{L}^{m}, h^{m}\right)$. It is easy to see that
$$\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}=\left|\frac{T_{x, m}\left(S_{M, x, m}\right)}{T_{x, m}\left(S_{V, x, m}^{\prime}\right)}\right|^{2} e^{m u} .$$

By definition, there are constants $m_{2}, C_{3}>0$ depending only on $V, r$ and $l$, such that
$$\sup _{V_{r_{m}}}\left|e^{m u}-1\right| \leq C_{3} m^{-l}, \quad \forall m \geq m_{2} .$$

Applying Proposition 4.1 to $T_{x, m}\left(S_{M, x, m}\right)$ and $T_{x, m}\left(S_{V, x, m}^{\prime}\right)$, one can see that there are constants $m_{3}, C_{4}>0$ depending only on $V, r, f$ and $l$, such that
$$\sup _{x \in V_{r_{m}}}\left(\left|\frac{T_{x, m}\left(S_{M, x, m}\right)}{T_{x, m}\left(S_{V_{\sqrt{r_{m}}}}, x, m\right)}-1\right|+\left|\frac{T_{x, m}\left(S_{V, x, m}^{\prime}\right)}{T_{x, m}\left(S_{V_{\sqrt{r_{m}}}}^{\prime}, x, m\right)}-1\right|\right) \leq C_{4} m^{-l}, \quad \forall m \geq m_{3} .$$

By definition, $\omega=\omega_{V}-\sqrt{-1} \partial \bar{\partial} u$, and $h=e^{u} h_{V}$. Lemma 4.2 now implies that that there are constants $m_{4}, C_{5}>0$ depending only on $V, r$ and $l$, such that
$$\sup _{x \in V_{r_{m}}}\left|\frac{T_{x, m}\left(S_{V_{\sqrt{r_{m}}}}, x, m\right)}{T_{x, m}\left(S_{V_{\sqrt{r_{m}}}}^{\prime}, x, m\right)}-1\right| \leq C_{5} m^{-l}, \quad \forall m \geq m_{4} .$$
It follows that
$$\begin{aligned}
& \left.\sup _{x \in V_{r_{m}}}\left|\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}-1\right|=\left.\sup _{x \in V_{r_{m}}}| | \frac{T_{x, m}\left(S_{M, x, m}\right)}{T_{x, m}\left(S_{V, x, m}^{\prime}\right)}\right|^{2} e^{m u}-1 \right\rvert\, \\
= & \left.\left.\sup _{x \in V_{r_{m}}}| | \frac{T_{x, m}\left(S_{M, x, m}\right)}{T_{x, m}\left(S_{V_{\sqrt{r_{m}}}}, x, m\right)}\right|^{2} \cdot\left|\frac{T_{x, m}\left(S_{V_{\sqrt{r_{m}}}, x, m}\right)}{T_{x, m}\left(S_{V_{\sqrt{m}^{m}}}^{\prime}, x, m\right)}\right|^{2} \cdot\left|\frac{T_{x, m}\left(S_{V_{\sqrt{m}_{m}}}^{\prime}, x, m\right)}{T_{x, m}\left(S_{V, x, m}^{\prime}\right)}\right|^{2} \cdot e^{m u}-1 \right\rvert\, \\
\leq & \left(1+2 C_{4} m^{-l}\right)^{4}\left(1+2 C_{5} m^{-l}\right)^{2}\left(1+2 C_{3} m^{-l}\right)-1 \leq\left(1+2 C_{4}\right)^{4}\left(1+2 C_{5}\right)^{2}\left(1+2 C_{3}\right) m^{-l},
\end{aligned}$$
for any integer $m \geq \sum_{j=2}^{4}\left(m_{j}+10 C_{j+1}\right)$. \(\square\)

Before considering the $C^{k}$-estimate of the quotients of Bergman kernel functions, we need the following lemma.

Lemma 5.2. Let $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$ be a complex hyperbolic cusp defined in Section 1, and $S \in$ $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}\right)$ such that $\|S\|_{L^{2} ; h_{V}^{m}, \omega_{V}}^{2}=1$. Then for each $k \in \mathbb{N}$, there exists a constant $C>0$ depending only on $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$ and $k$, such that
$$\|S(x)\|_{C^{k} ; h_{V}^{m}, \omega_{V}}^{2} \leq C m^{C}\left|\log h_{D}(x)\right|^{C} \rho_{\mathbb{D}_{1}^{*}, m}\left(\sqrt{h_{D}(x)}\right),$$
for any $x \in V_{e^{-2}}$ and integer $m \geq C$, where $\rho_{\mathbb{D}_{1}^{*}, m}$ is $m$-th Bergman kernel on the polarized punctured unit disc $\left(\mathbb{D}_{1}^{*}, \omega_{\mathbb{D}^{*}}, \mathbb{C},\left.|\log | z\right|^{2} \mid\right)$.

Proof. Combining Lemma 4.3 with Lemma 4.5, we can find a constant $C_{1}>0$ depending only on $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$ and $k$, such that
$$\left\|\nabla^{k} S(x)\right\|_{C^{k} ; h_{V}^{m}, \omega_{V}}^{2} \leq C_{1} m^{C_{1}}\left|\log h_{D}(x)\right|^{C_{1}} \int_{B_{C_{1}^{-1}\left|\log h_{D}(x)\right|^{-10}}(x)} \rho_{\omega_{V}, m}(y) d \operatorname{Vol}_{\omega_{V}},$$
for any $x \in V_{e^{-2}}$ and integer $m \geq C_{1}$. By a direct computation, we can conclude that there exists a constant $C_{2}>0$ depending only on $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that
$$B_{C_{1}^{-1}\left|\log h_{D}(x)\right|^{-10}}(x) \subset\left\{y \in V \mid h_{D}(x)^{1+C_{2}\left|\log h_{D}(x)\right|^{-10}} \leq h_{D}(y) \leq h_{D}(x)^{1-C_{2}\left|\log h_{D}(x)\right|^{-10}}\right\},$$
for any $x \in V_{e^{-2}}$. Combining Theorem thmregularpart with Lemma 4.3, we see that there exists a constant $\epsilon \in\left(0, e^{-1}\right)$ depending only on $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that
$$\frac{(m+n)!}{(2 \pi)^{n+1} m!} \leq \rho_{\omega_{V}, m}(x) \leq \frac{(m+n)!}{(2 \pi)^{n-1} m!},$$
for any $x \in V_{e^{-2}} \backslash V_{e^{-\sqrt{\epsilon m}}}$ and integer $m \geq \epsilon^{-1}$. Hence there exists a constant $C_{3}>0$ depending only on $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that
$$\left\|\nabla^{k} S(x)\right\|_{C^{k} ; h_{V}^{m}, \omega_{V}}^{2} \leq C_{3} m^{C_{3}}\left|\log h_{D}(x)\right|^{C_{3}} \leq C_{2}^{3} m^{2 C_{3}}\left|\log h_{D}(x)\right|^{2 C_{3}} \rho_{\mathbb{D}_{1}^{*}, m}\left(\sqrt{h_{D}(x)}\right),$$
for any $x \in V_{e^{-2}} \backslash V_{e^{-\epsilon} \sqrt{m}}$ and integer $m \geq C_{3}$.
Now we will give an estimate of $\rho_{\omega_{V}, m}(y)$ for $y \in B_{C_{1}^{-1}\left|\log h_{D}(x)\right|^{-10}}(x)$ and $x \in V_{e^{-\epsilon \sqrt{m}}}$. By Proposition 3.1, we can conclude that
$$\begin{aligned}
\rho_{\omega_{V}, m}(y) & =\frac{n\left|\log h_{D}(y)\right|^{m}}{2 \pi(m-n-1)!} \sum_{l=1}^{\infty} l^{m-n} \rho_{\omega_{D}, l}\left(\pi_{D}(y)\right) h_{D}(y)^{l} \\
& \leq C_{4} \frac{n\left|\log h_{D}(x)\right|^{m}\left(1+C_{2}\left|\log h_{D}(x)\right|^{-10}\right)^{m}}{2 \pi(m-n-1)!} \sum_{l=1}^{\infty} l^{m-1} h_{D}(x)^{l\left(1-C_{2}\left|\log h_{D}(x)\right|^{-10}\right)} \\
& \leq C_{4}^{2} \frac{n\left|\log h_{D}(x)\right|^{m}}{2 \pi(m-n-1)!} \sum_{l=1}^{\infty} l^{m-1} h_{D}(x)^{l\left(1-C_{2}\left|\log h_{D}(x)\right|^{-10}\right)} \\
& \leq C_{4}^{3} m^{n} \rho_{\mathbb{D}_{1}^{*}, m}\left(\sqrt{h_{D}(x)}\right),
\end{aligned}$$
for any $m \geq C_{4}$, where $C_{4}>0$ is a constant depending only on $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$. Combining these inequalities, we can prove this lemma. \(\square\)

Now we need to estimate the $C^{k}$ norm on $\left(V, \omega_{V}+\pi_{D}^{*} \omega_{D}\right)$. Let $\mathfrak{a} \in D$ and $z=\left(z_{1}, \cdots, z_{n-1}\right)$ : $U_{\mathfrak{a}} \rightarrow \mathbb{C}^{n-1}$ be a holomorphic coordinate around $\mathfrak{a} \in D$ such that $z(\mathfrak{a})=0$ and $\omega_{D}=z^{*} \omega_{E u c}$. Fix a holomorphic section $e_{\mathcal{L}_{D}} \in H^{0}\left(U_{\mathfrak{a}}, \mathcal{L}_{D}\right)$ satisfying that $\left\|e_{\mathcal{L}_{D}}\right\|_{h_{D}}^{2}=e^{|z|^{2}}$ on $U_{\mathfrak{a}}$. Now we can construct a holomorphic map $\varphi: U_{\mathfrak{a}} \times \mathbb{R}_{+} \times \mathbb{R} \rightarrow \pi_{D}^{-1}\left(U_{\mathfrak{a}}\right)$ by $\varphi(z, r, \theta)=r e^{\sqrt{-1} \theta} e_{\mathcal{L}_{D}}(z)$, $\forall(z, r, \theta) \in U_{\mathfrak{a}} \times \mathbb{R}_{+} \times \mathbb{R}$. It is clear that $\operatorname{rank}_{(z, r, x)}(d \varphi)=2 n, \forall(z, r, \theta) \in U_{\mathfrak{a}} \times \mathbb{R}_{+} \times \mathbb{R}$, and
$$\varphi^{-1}\left(\pi_{D}^{-1}\left(U_{\mathfrak{a}}\right) \cap V\right)=\left\{(z, r, \theta) \in U_{\mathfrak{a}} \times \mathbb{R}_{+} \times \mathbb{R} \mid r^{2}<e^{-|z|^{2}}\right\} .$$
Write $x_{2 i-1}=\operatorname{Re} z_{i}$ and $x_{2 i}=\operatorname{Im} z_{i}, i=1, \cdots, n-1$. Let
$$\begin{aligned}
\mathcal{X}_{j} & =\left|\log h_{D}\right|^{\frac{1}{2}} \mathcal{Y}_{j}=\mathcal{Z}_{j}=\frac{\partial}{\partial x_{j}}, \quad j=1, \cdots, 2 n-2, \\
\mathcal{X}_{2 n-1} & =\mathcal{Y}_{2 n-1}=\left.r| | z\right|^{2}+\log r^{2}\left|\mathcal{Z}_{2 n-1}=r\right||z|^{2}+\log r^{2} \left\lvert\, \frac{\partial}{\partial r}\right., \\
\mathcal{X}_{2 n} & =\mathcal{Y}_{2 n}=\left.r| | z\right|^{2}+\log r^{2}\left|\mathcal{Z}_{2 n}=\left||z|^{2}+\log r^{2}\right| \frac{\partial}{\partial \theta} .\right.
\end{aligned}$$
Then we can obtain the following estimate.
Lemma 5.3. Under the above assumptions, for any given $k \in \mathbb{N}$, there exists a constant $C>0$ depending only on $\left(V, \omega_{V}\right)$ and $U_{\mathfrak{a}}$, such that for any point $x \in V_{e^{-2}} \cap \pi_{D}^{-1}\left(U_{\mathfrak{a}}\right)$ and function
$f \in C^{k}(V ; \mathbb{R})$, we have
$$\begin{gathered}
\left\|\nabla^{k} f(x)\right\|_{\omega_{V}+\pi_{D}^{*} \omega_{D}} \leq C\left|\log h_{D}(x)\right|^{C} \sum_{l=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{l} \leq 2 n}\left|\mathcal{X}_{i_{1}}\left(\cdots\left(\mathcal{X}_{i_{l}}(f)\right) \cdots\right)(x)\right| \\
\leq C^{2}\left|\log h_{D}(x)\right|^{2 C} \sum_{p=0}^{k}\left\|\nabla^{p} f(x)\right\|_{\omega_{V}+\pi_{D}^{*} \omega_{D}}, \\
\left\|\nabla^{k} f(x)\right\|_{\omega_{V}+\pi_{D}^{*} \omega_{D}}+\left\|\nabla^{k} f(x)\right\|_{\omega_{V}} \\
\leq C\left|\log h_{D}(x)\right|^{C} \sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n}\left|\mathcal{Y}_{i_{1}}\left(\cdots\left(\mathcal{Y}_{i_{p}}(f)\right) \cdots\right)(x)\right| \\
\leq C^{2}\left|\log h_{D}(x)\right|^{2 C} \sum_{p=0}^{k}\left\|\nabla^{p} f(x)\right\|_{\omega_{V}}
\end{gathered}$$
and
$$\begin{aligned}
\sum_{p=0}^{k}\left\|\nabla^{p} f(x)\right\|_{\pi_{D}^{*} \omega_{D}+\sqrt{-1} \partial \bar{\partial} h_{D}} & \leq C \sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n}\left|\mathcal{Z}_{i_{1}}\left(\cdots\left(\mathcal{Z}_{i_{p}}(f)\right) \cdots\right)(x)\right| \\
& \leq C^{2} \sum_{p=0}^{k}\left|h_{D}(x)\right|^{-C}\left\|\nabla^{p} f(x)\right\|_{\omega_{V}} .
\end{aligned}$$

Moreover, if $f=f_{D} \circ \pi_{D}$ for some function $f_{D} \in C^{k}(D ; \mathbb{R})$, then
$$\left\|\nabla^{k} f(x)\right\|_{\omega_{V}+\pi_{D}^{*} \omega_{D}} \leq C \sum_{l=0}^{k}\left\|\nabla^{l} f_{D}\left(\pi_{D}(x)\right)\right\|_{\omega_{D}} .$$

The proof of this lemma is not difficult but is too long to give it.
Then we can give an estimate for the $C^{k}$-norm of the quotient of Bergman kernel functions on $V_{r_{m}}$ with respect to the Kähler metric $\omega_{V}$.

Proposition 5.1. Let $(M, \omega, \mathcal{L}, h)$ and $U \cong V_{r}$ be as in Theorem 1.2. Assume that $\Gamma_{V}=0$ and $\mathcal{L}_{D}^{-1}$ is globally generated. Then there exists a constant $b>0$, such that for any given integer $l \geq 0$,
$$\left\|\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}-1\right\|_{C^{k} ; \omega_{V}} \leq C\left|\log h_{D}\right|^{b} m^{-l}, \quad \forall m \geq C, \quad \forall x \in V_{r_{m}},$$
where $C>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), V, k$ and $l$.
Proof. By choosing open subsets $U_{\mathfrak{a}}$ of $D$ as stated before Lemma 5.3, we can find a finite covering $\left\{\pi_{D}^{-1}\left(U_{\mathfrak{a}}\right)\right\}_{\mathfrak{a} \in \mathfrak{A}}$ of $V$. Fix $x \in V_{r_{m}}$. Then there are vector fields $\mathcal{X}_{i}$ and $\mathcal{Y}_{i}$ around $x$ satisfying the estimates in Lemma 5.3. Let $\left\{S_{M, m, j}\right\}_{j \in I_{m}}$ and $\left\{S_{M, m, j}^{\prime}\right\}_{j \in I_{m}^{\prime}}$ be $L^{2}$ orthonormal bases in the spaces $H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)$ and $H_{L^{2}}^{0}\left(V, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$, respectively. Then we have
$$\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}=\frac{\sum_{j \in I_{m}}\left\|S_{M, m, j}(x)\right\|_{h^{m}}^{2}}{\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}(x)\right\|_{h_{V}^{m}}^{2}}=e^{m u} \frac{\sum_{j \in I_{m}}\left\|S_{M, m, j}(x)\right\|_{h_{V}^{m}}^{2}}{\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}(x)\right\|_{h_{V}^{m}}^{2}}, \forall x \in U \cong V_{r} .$$

By Lemma 5.3, we can conclude that for any constant $l>0$, there exists a constant $C_{1}>0$ depending only on $(M, \omega, \mathcal{L}, h), V, l$ and $k$, such that
$$\sum_{p=0}^{k} \sup _{V_{r_{m}}}\left\|\nabla^{p}\left(e^{m u}-1\right)(x)\right\|_{\omega_{V}} \leq C_{1} m^{-l}, \quad \forall m \geq C_{1} .$$

For abbreviation, we write $\mathfrak{Y}_{i_{1}, \cdots, i_{p}}$ instead of $\mathcal{Y}_{i_{1}}\left(\cdots\left(\mathcal{Y}_{i_{p}}\left(\sum_{j \in I_{m}}\left\|S_{M, m, j}\right\|_{h_{V}^{m}}^{2}\right)\right) \cdots\right)(x)$, and we write $\mathfrak{Y}_{i_{1}, \cdots, i_{p}}^{\prime}$ instead of $\mathcal{Y}_{i_{1}}\left(\cdots\left(\mathcal{Y}_{i_{p}}\left(\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}\right\|_{h_{V}^{m}}^{2}\right)\right) \cdots\right)(x)$. By induction on $k$, for any integer $k \geq 1$, one can conclude that
$$\begin{aligned}
& \sum_{1 \leq i_{1}, \cdots, i_{k} \leq 2 n} \mathcal{Y}_{i_{1}}\left(\cdots\left(\mathcal{Y}_{i_{k}}\left(\frac{\sum_{j \in I_{m}}\left\|S_{M, m, j}\right\|_{h_{V}^{m}}^{2}}{\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}\right\|_{h_{V}^{m}}^{2}}\right)\right) \cdots\right)(x) \\
= & \sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n}\left(\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}(x)\right\|_{h_{V}^{m}}^{2}\right)^{-k} P_{k, p} \cdot\left(\mathfrak{Y}_{i_{1}, \cdots, i_{p}}-\widetilde{\mathfrak{Y}}_{i_{1}, \cdots, i_{p}}\right)
\end{aligned}$$
where $p \leq k$ is a nonnegative integer, $P_{k, p}$ are polynomials in variables $\mathfrak{Y}_{i_{1}, \cdots, i_{p}}, \mathfrak{Y}_{i_{1}, \cdots, i_{p}}^{\prime}$ and of degree $k-1$, and $1 \leq i_{1}, \cdots, i_{p} \leq 2 n$ are integers. Since $\mathcal{L}_{D}^{-1}$ is globally generated, we can find a constant $C_{2}>0$ depending only on $V$, such that $\rho_{\mathbb{D}_{1}^{*}, m}\left(\sqrt{h_{D}(x)}\right) \leq C_{2} \rho_{V, \omega_{V}, m}(x), \forall x \in V$, $\forall m \geq n+1$. By Lemma 5.2, we see that for any integer $k \in \mathbb{N}$ and point $x \in V_{e^{-2}}$,
$$\left\|\nabla^{k}\left(\frac{\sum_{j \in I_{m}}\left\|S_{M, m, j}\right\|_{h_{V}^{m}}^{2}-1}{\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}\right\|_{h_{V}^{m}}^{2}}\right)\right\|_{\omega_{V}} \leq C_{3} m^{C_{3}}\left|\log h_{D}\right|^{C_{3}} \sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n} \frac{\left|\mathfrak{Y}_{i_{1}, \cdots, i_{p}}-\mathfrak{Y}_{i_{1}, \cdots, i_{p}}^{\prime}\right|}{\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}\right\|_{h_{V}^{m}}^{2 k}},$$
for any $m \geq C_{3}$, where $C_{3}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), V$ and $k$. Now we estimate the function $\left|\mathfrak{Y}_{i_{1}, \cdots, i_{p}}-\mathfrak{Y}_{i_{1}, \cdots, i_{p}}^{\prime}\right|$. Since Chern connection is compatible with the Hermitian metric $h_{V}^{m}$, we have
$$\begin{aligned}
& \sum_{p=0}^{k} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n}\left|\mathfrak{Y}_{i_{1}, \cdots, i_{p}}-\mathfrak{Y}_{i_{1}, \cdots, i_{p}}^{\prime}\right| \\
\leq & \sum_{p=0}^{k} \sum_{p^{\prime}=0}^{p} \sum_{1 \leq i_{1}, \cdots, i_{p} \leq 2 n} \mid \sum_{j \in I_{m}}\left\langle\nabla_{\mathcal{Y}_{i_{1}}} \cdots \nabla_{\mathcal{Y}_{i_{p^{\prime}}}} S_{M, m, j}, \nabla_{\mathcal{Y}_{i_{p^{\prime}+1}}} \cdots \nabla_{\mathcal{Y}_{i_{p}}} S_{M, m, j}\right\rangle_{h_{V}^{m}} \\
& -\sum_{j \in I_{m}^{\prime}}\left\langle\nabla_{\mathcal{Y}_{i_{1}}} \cdots \nabla_{\mathcal{Y}_{i_{p^{\prime}}}} S_{M, m, j}^{\prime}, \nabla_{\mathcal{Y}_{i_{p^{\prime}+1}}} \cdots \nabla_{\mathcal{Y}_{i_{p}}} S_{M, m, j}^{\prime}\right\rangle_{h_{V}^{m}} \mid .
\end{aligned}$$
For any point $x \in U \cong V_{r}$ and finite sequence of integers $1 \leq i_{1}, \cdots, i_{p} \leq 2 n$, we can define a linear functional $T_{x, m, i_{1}, \cdots, i_{p}}$ on $H_{L^{2}}^{0}\left(V_{r}, \mathcal{L}_{V}^{m}\right)$ by
$$\nabla_{\mathcal{Y}_{i_{1}}} \cdots \nabla_{\mathcal{Y}_{i_{p}}} S(x)=T_{x, m, i_{1}, \cdots, i_{p}}(S) e_{x}^{m}, \forall S \in H_{L^{2}}^{0}\left(V_{r}, \mathcal{L}_{V}^{m}\right),$$
where $\left.e_{x} \in \mathcal{L}_{V}\right|_{x}$ is a vector such that $\left\|e_{x}\right\|_{h_{V}}=1$. Let $S_{x, m, i_{1}, \cdots, i_{p}}$ and $S_{x, m, i_{1}, \cdots, i_{p}}^{\prime}$ be the peak sections of $T_{x, m, i_{1}, \cdots, i_{p}}$ in $H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)$ and $H_{L^{2}}^{0}\left(V, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$, respectively. Then we have
$$\begin{gathered}
\mid \sum_{j \in I_{m}}\left\langle\nabla_{\mathcal{Y}_{i_{1}}} \cdots \nabla_{\mathcal{Y}_{i_{p^{\prime}}}} S_{M, m, j}, \nabla_{\mathcal{Y}_{i_{p^{\prime}+1}}} \cdots \nabla_{\mathcal{Y}_{i_{p}}} S_{M, m, j}\right\rangle_{h_{V}^{m}} \\
-\sum_{j \in I_{m}^{\prime}}\left\langle\nabla_{\mathcal{Y}_{i_{1}}} \cdots \nabla_{\mathcal{Y}_{i_{p^{\prime}}}} S_{M, m, j}^{\prime}, \nabla_{\mathcal{Y}_{i_{p^{\prime}+1}}} \cdots \nabla_{\mathcal{Y}_{i_{p}}} S_{M, m, j}^{\prime}\right\rangle_{h_{V}^{m}} \mid \\
=\mid\left\langle T_{x, m, i_{1}, \cdots, i_{p^{\prime}}}\left(S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}-S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}^{\prime}\right) e_{x}^{m}, T_{x, m, i_{p^{\prime}+1}, \cdots, i_{p^{\prime}}}\left(S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}\right) e_{x}^{m}\right\rangle_{h_{V}^{m}} \\
-\left\langle T_{x, m, i_{1}, \cdots, i_{p^{\prime}}}\left(S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}^{\prime}\right) e_{x}^{m}, T_{x, m, i_{p^{\prime}+1}, \cdots, i_{p^{\prime}}}\left(S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}-S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}^{\prime}\right) e_{x}^{m}\right\rangle_{h_{V}^{m}}| |\left|S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}\right||\cdot|\left|T_{x, m, i_{p^{\prime}+1}, \cdots, i_{p^{\prime}}}\right||\cdot|\left|S_{x, m, i_{p^{\prime}}}-S_{x, m, i_{1}, \cdots, i_{p^{\prime}}}^{\prime}\right| \mid,
\end{gathered}$$
where $\|\cdot\|$ are norms corresponding to the Hilbert space $H_{L^{2}}^{0}\left(V_{\sqrt{r_{m}}}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$. Combining Lemma 4.1, Proposition 4.1 and Lemma 4.2, we can assert that for any integer $l>0$, there exists a constant $C_{4}>0$ depending only on $(M, \omega, \mathcal{L}, h), V, k$ and $l$, such that
$$\int_{V_{\sqrt{r_{m}}}}\left\|S_{x, m, i_{1}, \cdots, i_{p}}-S_{x, m, i_{1}, \cdots, i_{p}}^{\prime}\right\|_{h_{V}^{m}}^{2} d \operatorname{Vol}_{\omega_{V}} \leq C_{4} m^{-l}, \quad \forall m \geq C_{4}, \forall x \in V_{r_{m}} .$$
Hence for any integers $k, l \in \mathbb{N}$,
$$\left\|\nabla^{k}\left(\frac{\sum_{j \in I_{m}}\left\|S_{M, m, j}\right\|_{h_{V}^{m}}^{2}}{\sum_{j \in I_{m}^{\prime}}\left\|S_{M, m, j}^{\prime}\right\|_{h_{V}^{m}}^{2}}-1\right)\right\|_{\omega_{V}} \leq C_{6} m^{-l}\left|\log h_{D}\right|^{C_{5}}, \forall m \geq C_{6}, \forall x \in V_{r_{m}},$$
where $C_{5}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), V$ and $k$, and $C_{6}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), V, k$ and $l$. This is our claim. \(\square\)

Now we are ready to prove the $C^{k}$-estimate of the quotients of Bergman kernel functions.
Proposition 5.2. Let $(M, \omega, \mathcal{L}, h)$ and $U \cong V_{r}$ be as in Theorem 1.2. Assume that $\Gamma_{V}=0$ and $\mathcal{L}_{D}^{-1}$ is globally generated. Then for any given integer $l \geq 0$, there exists a constant $C>0$ depending only on $(M, \omega, \mathcal{L}, h), V, k$ and $l$, such that
$$\sup _{V_{r_{m}}}\left\|\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}-1\right\|_{C^{k} ; \omega_{V}+\pi_{D}^{*} \omega_{D}} \leq C m^{-l}, \forall m \geq C .$$
Proof. By Proposition 5.1, we only need to prove it when $x \in V_{e^{-m^{10}}}$. Without loss of generality, we can assume that $m$ is sufficiently large such that $r_{m}<r^{2}$.

Let $X_{m}=H_{L^{2}}^{0}\left(V_{r_{m}^{4}}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)_{2}$ be the subspace of $H_{L^{2}}^{0}\left(V_{r_{m}^{4}}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$ generated by the orthogonal set $\left\{f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m} \mid 1 \leq j \leq N_{q}, q \geq 2\right\}$, where $\left\{S_{q, j}\right\}_{j=1}^{N_{q}}$ is an orthonormal basis of the Hilbert space $H_{L^{2}}^{0}\left(D, \omega_{D}, \mathcal{L}_{D}^{-q}, h_{D}^{-q}\right)$, and $f_{S_{q, j}}$ denote the holomorphic function corresponding to $S_{q, j}$ defined in Lemma 3.1. Then we define $Y_{m}=X_{m} \cap H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)$, and $Z_{m}=$ $X_{m} \cap H_{L^{2}}^{0}\left(V, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$. Note that $\left(V_{r}, \mathcal{L}_{V}\right) \cong(U, \mathcal{L})$, and hence $H_{L^{2}}^{0}\left(V_{r}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)=$
$H_{L^{2}}^{0}\left(U, \omega, \mathcal{L}^{m}, h^{m}\right)$ as subspaces of $H^{0}\left(V_{r}, \mathcal{L}_{V}^{m}\right) \cong H^{0}\left(U, \mathcal{L}^{m}\right), \forall m \in \mathbb{N}$. Let $X_{m}^{\perp}, Y_{m}^{\perp}$ and $Z_{m}^{\perp}$ be the orthogonal complements of $X_{m}, Y_{m}$ and $Z_{m}$ in $H_{L^{2}}^{0}\left(V_{r_{m}}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right), H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)$ and $H_{L^{2}}^{0}\left(V, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$, respectively. By applying Lemma 3.2 to $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right), \forall m \geq n+1$, we see that $\left\{f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m} \mid 1 \leq j \leq N_{q}\right\}$ is an orthogonal basis of $X_{m}^{\perp}$ and $Z_{m}^{\perp}$ at the same time. Let $a_{m}=\left(\frac{n}{2 \pi(m-n-1)!}\right)^{\frac{1}{2}}$. It is easy to see that for any integer $l>0$, we have
$$\left|\int_{V_{r_{m}^{4}}^{4}}\left\|a_{m} f_{S_{1, j}} e_{\mathcal{L}_{V}}^{m}\right\|_{h_{V}^{m}}^{2} d \operatorname{Vol}_{\omega_{V}}-1\right|+\sup _{V_{r_{m}} \backslash V_{r_{m}^{4}}^{4}}\left\|a_{m} f_{S_{1, j}} e_{\mathcal{L}_{V}}^{m}\right\|_{h_{V}^{m}}^{2} \leq C_{1} m^{-l},$$
where $C_{1}>0$ is a constant depending only on $V$ and $l$.
Analysis similar to that in the proof of Lemma 4.4 shows that there are quasi-plurisubharmonic functions $\psi_{m} \in L^{1}\left(V, \omega_{V}\right)$ such that $\psi_{m} \leq 0, \operatorname{supp} \psi_{m} \subset V_{r_{m}^{4}}, \sqrt{-1} \partial \bar{\partial} \psi_{m} \geq-C_{2} \sqrt{m} \omega_{V}$, and $\lim _{h_{D}(x) \rightarrow 0}\left(\psi_{m}(x)-\log \left(h_{D}(x)\right)\right)=-\infty$, where $C_{2}>0$ is a constant dependent only on $V$. See also the remark below Lemma 4.4. Let $\eta_{m} \in C^{\infty}(V)$ such that $\eta_{m}=1$ on $V_{r_{m}^{4}}, \eta_{m}=0$ on $V \backslash V_{r_{m}^{2}}$, and $\left\|\nabla \eta_{m}\right\|_{\omega_{V}} \leq C_{3}$, where $C_{3}>0$ is a constant dependent only on $V$. By Hörmander's $L^{2}$ estimate, we can find a smooth $\mathcal{L}^{m}$-valued function $\zeta_{j, m}$ on $M$ such that $\bar{\partial}\left(a_{m} \eta_{m} f_{S_{1, j}} e_{\mathcal{L}}^{m}-\zeta_{j, m}\right)=0$, and for each given integer $l>0$,
$$\int_{M}\left\|\zeta_{j, m}\right\|_{h^{m}}^{2} e^{-10 \psi_{m}} d \operatorname{Vol}_{\omega} \leq \frac{C_{4}}{m} \int_{M}\left\|\bar{\partial}\left(a_{m} \eta_{m} f_{S_{1, j}} e_{\mathcal{L}}^{m}\right)\right\|_{h^{m}, \omega}^{2} e^{-10 \psi_{m}} d \operatorname{Vol}_{\omega} \leq C_{4} m^{-l},$$
for any integer $m \geq C_{4}$, where $C_{4}>0$ is a constant depending only on ( $M, \omega, \mathcal{L}, h$ ) and $l$. It follows that $\left.\zeta_{j, m}\right|_{V_{r_{m}^{4}}} \in X_{m}$, and $\left\|\zeta_{j, m}\right\|_{L^{2} ; h^{m}, \omega}^{2} \leq C_{4} m^{-l}$. Similarly, there are holomorphic sections $\zeta_{j, m}^{\prime} \in Y_{m}$ such that $a_{m} \eta_{m} f_{S_{1, j}} e_{\mathcal{L}}^{m}-\zeta_{j, m}-\zeta_{j, m}^{\prime} \in Y_{m}^{\perp}$, and for any given integer $l$, we have $\left\|\zeta_{j, m}\right\|_{L^{2} ; h^{m}, \omega}^{2} \leq C_{5} m^{-l}, \forall m \geq C_{5}$, where $C_{5}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h)$ and $l$. By Schmidt orthonormalization process, we can find constants $b_{i, j, m}$ such that the set $\left\{\sum_{j=1}^{N_{1}} b_{i, j, m}\left(a_{m} \eta_{m} f_{S_{1, j}} e_{\mathcal{L}}^{m}-\zeta_{j, m}-\zeta_{j, m}^{\prime}\right)\right\}_{i=1}^{N_{1}}$ becomes a orthonormal basis of $Y_{m}^{\perp}$, and for each given integer $l$, there exists a constant $C_{6}>0$ depending only on $(M, \omega, \mathcal{L}, h)$ and $l$, such that $\left|b_{i, j, m}-\delta_{i, j}\right| \leq C_{6} m^{-l}, \forall m \geq C_{6}$.

An argument similar to the one used in Lemma 5.2 shows that for each integer $k>0$, there exists a constant $C_{7}>0$ depending only on $V$ and $k$, such that
$$\|S(x)\|_{C^{k} ; h_{V}^{m}, \omega_{V}}^{2} \leq C_{7} m^{C_{7}}\left|\log h_{D}(x)\right|^{C_{7}} \rho_{\mathbb{D}_{1}^{*}, m}\left(\sqrt{h_{D}(x)}\right)^{2}\|S\|_{L^{2} ; h_{V}^{m}, \omega_{V}}^{2},$$
for any $m \geq C_{7}, S \in X_{m}$ and $x \in V_{r_{m}^{10}}$. As in Proposition 5.1, this estimate shows that for any integer $k \geq 0$, we have
$$\begin{aligned}
& \left\|\nabla^{k}\left(\frac{\sum_{j=1}^{N_{1}}\left\|a_{m} f_{S_{1, j}} e_{\mathcal{L}_{V}}^{m}\right\|_{h_{V}^{m}}^{2}-1}{\rho_{V, \omega_{V}, m}}\right)\right\|_{\omega_{V}}+\left\|\nabla^{k}\left(\frac{\sum_{j=1}^{N_{1}}\left\|\sum_{j=1}^{N_{1}} b_{i, j, m} a_{m} f_{S_{1, j}} e_{\mathcal{L}}^{m}\right\|_{h^{m}}^{2}}{\rho_{M, \omega, m}}-1\right)\right\|_{\omega_{V}} \\
& \leq C_{8} m^{-l}\left|\log h_{D}\right|^{C_{8}} \rho_{\mathbb{D}_{1}^{*}, m}\left(\sqrt{h_{D}(x)}\right), \quad \forall m \geq C_{8}, \quad \forall x \in V_{r_{m}^{10}},
\end{aligned}$$
where $C_{8}>0$ is a constant depending only on ( $M, \omega, \mathcal{L}$ ) and $k$. Since $\left|b_{i, j, m}-\delta_{i, j}\right| \leq C_{6} m^{-l}$, we can apply Lemma 5.3 to show that for any given integers $k, l>0$, there exists a constant $C_{9}>0$
depending only on $(M, \omega, \mathcal{L}), k$ and $l$, such that
$$\left\|\nabla^{k}\left(\frac{\sum_{j=1}^{N_{1}}\left\|\sum_{j=1}^{N_{1}} b_{i, j, m} a_{m} f_{S_{1, j}} e_{\mathcal{L}_{V}}^{m}\right\|_{h_{V}^{m}}^{2}-1}{\sum_{j=1}^{N_{1}}\left\|a_{m} f_{S_{1, j}} e_{\mathcal{L}_{V}}^{m}\right\|_{h_{V}^{m}}^{2}}\right)\right\|_{\omega_{V}+\pi_{D}^{*}} \leq C_{9} m^{-l}, \forall m \geq C_{9}, \forall x \in V_{r_{m}^{10}} .$$
Combining these inequalities, one can conclude that there exists a constant $C_{10}>0$ depending only on $(M, \omega, \mathcal{L}, h), k$ and $l$, such that
$$\left\|\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}-1\right\|_{C^{k} ; \omega_{V}+\pi^{*} \omega_{D}} \leq C_{10} m^{-l}, \forall m \geq C_{10}, \forall x \in V_{e^{-m^{10}}},$$
which completes the proof. \(\square\)

\subsection*{5.2. Bergman kernels on quotients of complex ball.}

Let $\left(\mathbb{B}^{n}, \omega_{\mathbb{B}}\right)$ be the $n$-dimensional complex hyperbolic ball with constant bisectional curvature -1 , and let $\Gamma$ be a torsion free lattice in $\operatorname{Aut}\left(\mathbb{B}^{n}, \omega_{\mathbb{B}}\right) \cong P U(n, 1)$. Then the quotient space $\mathbb{B}^{n} / \Gamma$ is a manifold, and there exist a finite collection of disjoint open subsets $U_{i} \subset \mathbb{B}^{n} / \Gamma, i=1, \cdots, N$, and complex hyperbolic cusps $\left(V_{i} / \Gamma_{V_{i}}, \omega_{V_{i}}, \mathcal{L}_{V_{i}} / \Gamma_{V_{i}}, h_{V_{i}}\right)$ such that $\left(U_{i}, \omega_{\mathbb{B}^{n}}\right) \cong\left(V_{i} / \Gamma_{V_{i}}, \omega_{V_{i}}\right)$, and $\left(\mathbb{B}^{n} / \Gamma\right) \backslash\left(\cup_{i=1}^{N} U_{i}\right)$ is compact.

Now we consider the Bergman kernels on $U_{i}$. Since $U_{i}$ and $\mathbb{B}^{n} / \Gamma$ satisfy the conditions of Theorem 1.3, we see that Theorem 1.3 describes the asymptotic behavior of the Bergman kernels on $U_{i}$.

Proof of Theorem 1.3: Let $\gamma_{m}=r^{2}$ and $\sigma_{m}=r$ in Theorem 1.1. Note that $U \cong V_{r} / \Gamma_{V}$. By applying Theorem 1.1 to $U \subset M$ and $V_{r} / \Gamma_{V} \subset V / \Gamma_{V}$, respectively, we can prove the theorem. \(\square\)

Our next goal is to prove the $C^{k}$-estimate of the quotients of Bergman kernel functions.
By combining Lemma 5.3 with Proposition 5.1, one can get the following proposition.
Proposition 5.3. Let $(M, \omega, \mathcal{L}, h)$ and $U \cong V_{r}$ be as in Theorem 1.3. Assume that $\Gamma_{V}=0$ and $\mathcal{L}_{D}^{-1}$ is globally generated. Then there exists a constant $b>0$ depending only on $(M, \omega, \mathcal{L}, h)$, such that for any given integer $l \geq 0$,
$$\left\|\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}-1\right\|_{C^{k} ; \omega_{0}} \leq C\left|h_{D}(x)\right|^{-b} m^{-l}, \quad \forall x \in V_{r^{2}}, \quad \forall m \geq C,$$
where $\omega_{0}=\pi_{D}^{*} \omega_{D}+\sqrt{-1} \partial \bar{\partial} h_{D}$ is a Kähler metric on the total space of $\mathcal{L}_{D}$, and $C>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), V, k$ and $l$.

When $h_{D}$ is small, we cannot derive the estimate we need from Proposition 5.3. In this case, we need to make some finer estimates by approximating the $L^{2}$ orthonormal basis of $H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)$ using the $L^{2}$ orthonormal basis of $H_{L^{2}}^{0}\left(V / \Gamma_{V}, \omega_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{m}, h_{V}^{m}\right)$. Suppose that $\Gamma_{V}=0$. The following lemma gives an estimate about the norm of holomorphic sections on $V$.

Lemma 5.4. Let $\left(V, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$ be a complex hyperbolic cusp, and $\kappa \in\left(0, e^{-1}\right)$ be a constant. Then for any given constant $\mathfrak{K}>0$, there exists a constant $C>0$ depending only on $\kappa$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that
$$\left\|a_{m, q} f_{S_{q}} e_{\mathcal{L}_{V}}^{m}\right\|_{L^{2}, V \backslash V_{\kappa} ; h_{V}^{m}, \omega_{V}}^{2} \leq C e^{-4 \mathfrak{K} m}\left\|S_{q}\right\|_{L^{2}, D ; h_{D}^{-q}, \omega_{D}}^{2},$$
for any positive integers $m \geq n+1, q \leq e^{-4(\mathfrak{K}+|\log | \log \kappa| |+n+4)} m$ and holomorphic sections $S_{p} \in$ $H^{0}\left(D, \mathcal{L}_{D}^{-p}\right)$, where $a_{m, q}=\sqrt{\frac{n q^{m-n}}{2 \pi(m-n-1)!}}$, and $f_{S_{q}}$ is the holomorphic function on $V$ defined in Lemma 3.1.

Remark. Since $q \in \mathbb{N}$, we see that Lemma 5.4 is trivial when $m \leq e^{4(\mathfrak{K}+|\log | \log \kappa| |+n+4)}$.
Proof. Without loss of generality, we can assume that $\left\|S_{q}\right\|_{L^{2}, D ; h_{D}^{-q}, \omega_{D}}=1$. Fix $x \in V \backslash V_{\kappa}$. Let $t=$ $h_{D}(x) \in(\kappa, 1)$. By Theorem 2.1, there exists a constant $C_{1}>0$ depending only on $\left(D, \omega, \mathcal{L}_{D}, h_{D}\right)$, such that $\rho_{D, \omega_{D}, \mathcal{L}_{D}^{-1}, h_{D}^{-1}, q} \leq C_{1} q^{n-1}, \forall q \in \mathbb{N}$. Hence
$$\left|f_{S_{q}}(x)\right|^{2}=h_{D}(x)^{q}\left\|S_{q}\left(\pi_{D}(x)\right)\right\|_{h_{D}^{-q}}^{2} \leq t^{q} \rho_{D, \omega_{D}, \mathcal{L}_{D}^{-1}, h_{D}^{-1}, q}\left(\pi_{D}(x)\right) \leq C_{1} t^{q} q^{n-1} .$$
By Stirling's formula, we can conclude that
$$\begin{aligned}
\left\|a_{m, q} f_{S_{q}}(x) e_{\mathcal{L}_{V}}^{m}(x)\right\|_{h_{V}^{m}}^{2} & \leq C_{1} \frac{n q^{m-1}}{2 \pi(m-n-1)!} t^{q}|\log t|^{m} \leq C_{1} \frac{n m^{n+1} q^{m-1} e^{m}}{2 \pi \sqrt{2 \pi} m^{m}} t^{q}|\log t|^{m} \\
& =\frac{n C_{1}}{2 \pi \sqrt{2 \pi}} e^{(n+1) \log m+(m-1) \log q+m-m \log m+q \log t+m \log |\log t|} \\
& \leq \frac{n C_{1}}{2 \pi \sqrt{2 \pi}} e^{n \log m-4(m-1)(\mathfrak{K}+|\log | \log r| |+n+4)+m \log |\log t|} \\
& \leq C_{1} e^{-4 \mathfrak{K} m-m|\log | \log t| |}
\end{aligned}$$
for any positive integers $m \geq n+1$ and $q \leq e^{-4(\mathfrak{K}+|\log | \log r| |+n+4)} m$. Now (14) implies that
$$\begin{aligned}
\left\|a_{m, q} f_{S_{q}} e_{\mathcal{L}_{V}}^{m}\right\|_{L^{2}, V \backslash V_{\kappa} ; h_{V}^{m}, \omega_{V}}^{2} & \leq C_{1} e^{-4 \mathfrak{K} m}\left(\operatorname{Vol}_{\omega_{V}}\left(V_{e^{-1}} \backslash V_{\kappa}\right)+\int_{V \backslash V_{e}-1}\left|\log h_{D}\right|^{m} d \operatorname{Vol}_{\omega_{V}}\right) \\
& \leq C_{2} e^{-4 \mathfrak{K} m}\left(1+\left.\int_{\mathbb{D} \backslash \mathbb{D}_{e^{-1}}} \sqrt{-1}|z|^{-2}|\log | z\right|^{m-n-1} d z \wedge d \bar{z}\right) \\
& \leq C_{3} e^{-4 \mathfrak{K} m},
\end{aligned}$$
where $C_{2}, C_{3}$ are positive constants depending only on $r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$. This is our assertion \(\square\)

The following basic fact of linear algebra will also be used in the proof of the $C^{k}$-estimate of the quotients of Bergman kernel functions.
Lemma 5.5. Let $N \in \mathbb{N}$, and let $A=\left(a_{i j}\right)_{i, j=1}^{N}$ be an $N \times N$ Hermitian matrix. Suppose that there exists a positive constant $\delta \leq \frac{1}{100 N}$ such that $\max _{1 \leq i, j \leq N}\left|a_{i j}-\delta_{i, j}\right| \leq \delta$. Then there exists an $N \times N$ Hermitian matrix $B=\left(b_{i j}\right)_{i, j=1}^{N}$ such that $A=B \bar{B}^{T}$, and $\max _{1 \leq i, j \leq N}\left|b_{i j}-\delta_{i, j}\right| \leq 2 N \delta$.
Proof. Recall that any Hermitian matrix can be diagonalized by a unitary matrix, so we can find $Q \in U(N)$ such that $A=Q \Lambda \bar{Q}^{T}$, where $\Lambda=\operatorname{diag}\left(\lambda_{1}, \cdots, \lambda_{N}\right)$ be a diagonal matrix. Since $\max _{1 \leq i, j \leq N}\left|a_{i j}-\delta_{i, j}\right| \leq \delta$, the characteristic polynomial of $A-I, p_{A}(\lambda)=\lambda^{n}+c_{1} \lambda^{n-1}+\cdots+c_{n}$, satisfying that $c_{i} \leq N^{i} \delta^{i}, i=1, \cdots, n$. Note that $p_{A}\left(\lambda_{1}\right)=\cdots=p_{A}\left(\lambda_{N}\right)=0$. Then we can conclude that $\max _{1 \leq j \leq N}\left|\lambda_{j}-1\right| \leq 2 N \delta \leq \frac{1}{50}$. Clearly, $\Lambda$ is real matrix. Let $B=Q \sqrt{\Lambda} \bar{Q}^{T}$, where $\sqrt{\Lambda}=\operatorname{diag}\left(\sqrt{\lambda_{1}}, \cdots, \sqrt{\lambda_{N}}\right)$ is a diagonal matrix. Then we have $A=B \bar{B}^{T}$, and $\left|\sqrt{\lambda_{i}}-1\right| \leq\left|\lambda_{i}-1\right|$ implies that $\max _{1 \leq i, j \leq N}\left|b_{i j}-\delta_{i, j}\right| \leq 2 N \delta$. \(\square\)

Now we are ready to prove the $C^{k}$-estimate of the quotients of Bergman kernel functions.

Proposition 5.4. Let $(M, \omega, \mathcal{L}, h)$ and $U \cong V_{r}$ be as in Theorem 1.3. Assume that $\Gamma_{V}=0$ and $\mathcal{L}_{D}^{-1}$ is globally generated. Then
$$\sup _{V^{2}}\left\|\frac{\rho_{M, \omega, m}(x)}{\rho_{V, \omega_{V}, m}(x)}-1\right\|_{C^{k} ; \omega_{0}} \leq C m^{-l}, \forall m \geq C,$$
where $\omega_{0}=\pi_{D}^{*} \omega_{D}+\sqrt{-1} \partial \bar{\partial} h_{D}$ is a Kähler metric on the total space of $\mathcal{L}_{D}$, and $C>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), \omega_{0}, V, k$ and $l$.

Proof. For each integer $\mathfrak{q} \geq 1$, we use $X_{m, \mathfrak{q}}$ to denote the linear subspace of $H_{L^{2}}^{0}\left(V_{r}, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$ generated by $\left\{f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m} \mid q \geq \mathfrak{q}, 1 \leq j \leq N_{q}\right\}$, where $\left\{S_{q, j}\right\}_{j=1}^{N_{q}}$ is an $L^{2}$ orthonormal basis in the Hilbert space $H_{L^{2}}^{0}\left(D, \mathcal{L}_{D}^{-q}\right)$, and $f_{S_{q, j}}$ denote the holomorphic function corresponding to $S_{q, j}$ defined in Lemma 3.1. Write $Y_{m, \mathfrak{q}}=X_{m, \mathfrak{q}} \cap H_{L^{2}}^{0}\left(V, \omega_{V}, \mathcal{L}_{V}^{m}, h_{V}^{m}\right)$, and $Z_{m, \mathfrak{q}}=X_{m, \mathfrak{q}} \cap H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)$. Let $\mathfrak{K} \geq 10$ be a constant that will be determined later. Set $q_{m, \mathfrak{K}}=\left\lfloor e^{-4(\mathfrak{K}+|\log | \log r| |+n+6)} m\right\rfloor$, for any integer $m \geq e^{4(\mathfrak{K}+|\log | \log r| |+n+6)}$. Then Lemma 5.4 shows that there exists a constant $C_{1} \geq 1$ depending only on $r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that
$$\left\|a_{m, q} f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}\right\|_{L^{2}, V \backslash V_{r^{2}} ; h_{V}^{m}, \omega_{V}}^{2} \leq C_{1} e^{-4 \mathfrak{K} m}, \quad \forall q \leq q_{m, \mathfrak{K}}, \quad 1 \leq j \leq N_{q},$$
where $a_{m, q}=\sqrt{\frac{n q^{m-n}}{2 \pi(m-n-1)!}}$. Let $\eta \in C^{\infty}(V)$ such that $0 \leq \eta \leq 1,|\nabla \eta|_{\omega_{V}} \leq 10, \eta=1$ on $V_{r^{2}}$ and $\eta=0$ on $V \backslash V_{r}$. Then we can apply Hörmander's $L^{2}$ estimate to show that there are $\mathcal{L}^{m}$-valued smooth functions $u_{m, q, j}$ on $M$, such that $\bar{\partial} u_{m, q, j}=\bar{\partial}\left(a_{m, q} \eta f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}\right)$, and
$$\int_{M}\left\|u_{m, q, j}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega} \leq \int_{M}\left\|\bar{\partial}\left(a_{m, q} \eta f_{S_{q, j}} e_{\mathcal{L}}^{m}\right)\right\|_{h^{m}, \omega}^{2} d \operatorname{Vol}_{\omega} \leq 100 C_{1} e^{-4 \mathfrak{K} m},$$
for any integers $q \leq q_{m, \mathfrak{K}}$ and $1 \leq j \leq N_{q}$. Write $\widetilde{S}_{m, q, j}^{\prime}=a_{m, q} \eta f_{S_{q, j}} e_{\mathcal{L}}^{m}-u_{m, q, j}$ for any integers $q \leq q_{m, \mathfrak{K}}$ and $1 \leq j \leq N_{q}$. Since $a_{m, q} f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m} \perp X_{m, q_{m, \mathfrak{K}}+1}, \forall q \leq q_{m, \mathfrak{K}}$, we see that the image of $\widetilde{S}_{m, q, j}^{\prime}$ under the orthogonal projection of $H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$ onto $Z_{m, q_{m, \mathfrak{K}}+1}, \widetilde{S}_{m, q, j}^{\prime Z}$, satisfying that
$$\left\|\widetilde{S}_{m, q, j}^{\prime Z}\right\|_{L^{2}, M ; h^{m}, \omega}^{2} \leq\left\|u_{m, q, j}\right\|_{L^{2}, M ; h^{m}, \omega}+\left\|a_{m, q} f_{S_{q, j}} e_{\mathcal{L}}^{m}\right\|_{L^{2}, M \backslash V_{r^{2}} ; h^{m}, \omega} \leq 200 C_{1} e^{-2 \mathfrak{K} m} .$$
Set $\widetilde{S}_{m, q, j}^{\prime \prime}=\widetilde{S}_{m, q, j}^{\prime}-\widetilde{S}_{m, q, j}^{\prime Z}$, and $N_{\text {sum }, m, \mathfrak{K}}=\sum_{q=1}^{q_{m, \mathfrak{K}}} N_{q}$. Then $v_{m, q, j, q^{\prime}, j^{\prime}}=\left\langle\widetilde{S}_{m, q, j}^{\prime \prime}, \widetilde{S}_{m, q^{\prime}, j^{\prime}}^{\prime \prime}\right\rangle$ gives an $N_{\text {sum }, m, \mathfrak{K}} \times N_{\text {sum }, m, \mathfrak{K}}$ Hermitian matrix $\Upsilon_{m}$ such that $\left|v_{m, q, j, q^{\prime}, j^{\prime}}-\delta_{q, q^{\prime}} \delta_{j, j^{\prime}}\right| \leq 400 C_{1} e^{-\kappa m}$. Note that $N_{\text {sum }, m, \mathfrak{K}} \leq C_{2} q^{n}$ for some constant $C_{2}>0$ depending only on $\left(D, \omega_{D}, \mathcal{L}_{D}, h_{D}\right)$. So we can assume that $e^{\mathfrak{K} m} \geq e^{400\left(C_{1}+C_{2}\right)} q^{4 n}$ by increasing $m$ if necessary. Lemma 5.5 now shows that there exists a constant $C_{3} \geq 1$ depending only on $r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that we can find constants $b_{m, q, j, q^{\prime}, j^{\prime}}$ satisfying that $\left|b_{m, q, j, q^{\prime}, j^{\prime}}\right| \leq C_{3} q^{n} e^{-\kappa m}$, and
$$\left\{\widetilde{S}_{m, q, j}=\widetilde{S}_{m, q, j}^{\prime \prime}+\sum_{q^{\prime}=1}^{q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q^{\prime}}} b_{m, q, j, q^{\prime}, j^{\prime}} \widetilde{S}_{m, q^{\prime}, j^{\prime}}^{\prime \prime} \mid 1 \leq q \leq q_{m, \mathfrak{K}}, 1 \leq j \leq N_{q}\right\}$$
forms an orthonormal basis of $X_{m, q_{m, \mathfrak{K}}+1}^{\perp}$. It follows that
$$\widetilde{S}_{m, q, j}=a_{m, q} f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}+\sum_{q^{\prime}=1}^{q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q^{\prime}}} c_{m, q, j, q^{\prime}, j^{\prime}} a_{m, q^{\prime}} f_{S_{q^{\prime}, j^{\prime}}} e_{\mathcal{L}_{V}}^{m}+\widetilde{S}_{m, q, j}^{Z},$$
where $c_{m, q, j, q^{\prime}, j^{\prime}}$ are constants satisfying that $\left|c_{m, q, j, q^{\prime}, j^{\prime}}\right| \leq 200 C_{3} q^{3 n} e^{-\kappa m}$, and $\widetilde{S}_{m, q, j}^{Z} \in Z_{m, q_{m, \mathfrak{K}}+1}$ satisfying that $\left\|\widetilde{S}_{m, q, j}^{Z}\right\|_{L^{2}, M ; h^{m}, \omega}^{2} \leq 200 C_{3} q^{3 n} e^{-\mathfrak{K} m}$.

Fix $k \in \mathbb{N}$ and $x \in V_{r^{3}}$. Then there are vector fields $\mathcal{Z}_{i}$ around $x$ satisfying the estimates in Lemma 5.3. For any finite sequence of integers $1 \leq i_{1}, \cdots, i_{p} \leq 2 n$, we can define a linear functional $T_{x, m, i_{1}, \cdots, i_{p}}$ on $H_{L^{2}}^{0}\left(V_{r}, \mathcal{L}_{V}^{m}\right)$ by
$$T_{x, m, i_{1}, \cdots, i_{p}}(S)=\mathcal{Z}_{i_{1}}\left(\cdots\left(\mathcal{Z}_{i_{p}}\left(h_{D}^{-\frac{1}{2}} e_{\mathcal{L}_{V}}^{-m}(S)\right)\right) \cdots\right), \forall S \in H_{L^{2}}^{0}\left(V_{r}, \mathcal{L}_{V}^{m}\right) .$$
By a straightforward calculation, one can obtain
$$\left|T_{x, m, i_{1}, \cdots, i_{p}}\left(f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}\right)\right|^{2} \leq C_{4} q^{p+n-1} h_{D}(x)^{\max \{0, q-p-1\}},$$
for any integers $q \in \mathbb{N}$ and $1 \leq j \leq N_{q}$, where $C_{4}>0$ is a constant depending only on $r, p$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$. Suppose that $q_{m, \mathfrak{K}} \geq p+1$. Then
$$\begin{aligned}
\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y_{m, q_{m, \mathfrak{K}}+1}}\right\|^{2} & =\sum_{q>q_{m, \mathfrak{K}}} \sum_{j=1}^{N_{q}}\left|T_{x, m, i_{1}, \cdots, i_{p}}\left(a_{m, q} f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}\right)\right|^{2} \\
& \leq \sum_{q>q_{m, \mathfrak{K}}} C_{4} N_{q} a_{m, q}^{2} q^{p+n+1} h_{D}(x)^{q-p-1} \\
& \leq \sum_{q>q_{m, \mathfrak{K}}} \frac{n C_{2} C_{4}}{2 \pi(m-n-1)!} q^{m+p+n} h_{D}(x)^{q-p-1} .
\end{aligned}$$
When $\log h_{D}(x) \leq-10-\frac{m+p+n}{q_{m, \mathfrak{K}}}$, (105) implies that
$$\left\|\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y_{m, q_{m, \mathfrak{K}}+1}}\right\|^{2} \leq \frac{n C_{2} C_{4}}{\pi(m-n-1)!} q_{m, \mathfrak{K}}^{m+p+n} h_{D}(x)^{q_{m, \mathfrak{K}}-p-1} .$$

Note that $\rho_{\omega_{D}, 1}>0$ on $D$. Then we can conclude that
$$\left|T_{x, m, i_{1}, \cdots, i_{p}}\left(a_{m, q} f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}\right)\right|^{2} \leq C_{4} e^{k m} q_{m, \mathfrak{K}}^{2 k+2 n} \sum_{q^{\prime}=1}^{q_{m, \mathfrak{K}}} \sum_{j^{\prime}=1}^{N_{q^{\prime}}}\left|a_{m, q^{\prime}} f_{S_{q^{\prime}, j^{\prime}}} h_{D}^{-\frac{1}{2}}\right|^{2},$$
for any integers $q \leq q_{m, \mathfrak{K}}$ and $1 \leq j \leq N_{q}$.
By the construction in much the same way as in the proof of Lemma 4.4, we see that there exist a quasi-plurisubharmonic function $\psi \in L^{1}\left(V, \omega_{V}\right)$ and a constant $C_{5}$ depending only on $r$ and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$, such that $\psi \leq 0, \sqrt{-1} \partial \bar{\partial} \psi \geq-C_{5} \omega_{V}, \operatorname{supp} \psi \subset V_{r^{2}}$, and
$$\lim _{h_{D}(y) \rightarrow 0}\left(\psi(y)-\log \left(\operatorname{dist}_{\omega_{V}}(x, y)\right)\right)=\lim _{y \rightarrow x}\left(\psi(y)-\log \left(h_{D}(y)\right)\right)=-\infty .$$
Assume that $m-n-2 \geq C_{5}\left(q_{m, \mathfrak{K}}+4 n+4 p\right)$. Then $\sqrt{-1}\left(2 n+2 k+q_{m, \mathfrak{K}}\right) \partial \bar{\partial} \psi+m \omega+\operatorname{Ric}(\omega) \geq \omega$. Let $S_{x, m, Y, i_{1}, \cdots, i_{p}}$ be the peak section of $\left.T_{x, m, i_{1}, \cdots, i_{p}}\right|_{Y_{m, q_{m, \mathfrak{K}}+1}}$. Hence we can use Hörmander's $L^{2}$ estimate to show that there exists a smooth $\mathcal{L}^{m}$-values $u_{x, m, Y, i_{1}, \cdots, i_{p}}$ on $M$ such that $\bar{\partial} u_{x, m, Y, i_{1}, \cdots, i_{p}}=$ $\bar{\partial}\left(\eta S_{x, m, Y, i_{1}, \cdots, i_{p}}\right)$, and
$$\begin{aligned}
\int_{M}\left\|u_{x, m, Y, i_{1}, \cdots, i_{p}}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega} & \leq \int_{M}\left\|\bar{\partial}\left(\eta S_{x, m, Y, i_{1}, \cdots, i_{p}}\right)\right\|_{h^{m}, \omega}^{2} d \operatorname{Vol}_{\omega} \\
& =\int_{M}\left\|\bar{\partial} \eta \otimes S_{x, m, Y, i_{1}, \cdots, i_{p}}\right\|_{h^{m}, \omega}^{2} d \operatorname{Vol}_{\omega} \leq 100 .
\end{aligned}$$