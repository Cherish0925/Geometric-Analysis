---
retention_scope: session
part: 2
total_parts: 4
---

[Part 2/4 of: Peak sections and Bergman kernels on Kähler manifolds with complex hyperbolic cusps]

Lemma 4.1. Let $S_{U} \in X$ and $S_{M} \in X \cap H_{L^{2}}^{0}(M, \mathcal{L})$ be the peak sections on $U$ and $M$ respectively. Assume that $\left\|\left.T\right|_{X \cap H_{L^{2}}^{0}(M, \mathcal{L})}\right\| \geq(1-\epsilon)\|T\|>0$ for some $\epsilon>0$. Then
$$\int_{M \backslash U}\left\|S_{M}\right\|^{2} d \operatorname{Vol}_{\omega}+\int_{U}\left\|S_{U}-S_{M}\right\|^{2} d \operatorname{Vol}_{\omega} \leq 2 \epsilon$$
Proof. By definition, we have $T\left(S_{M}\right)=\left\|\left.T\right|_{X \cap H_{L^{2}}^{0}(M, \mathcal{L})}\right\| \leq\|T\|=T\left(S_{U}\right)$. Hence there exists a constant $\delta \in(0, \epsilon]$ such that $T\left(s_{M}\right)=(1-\delta) T\left(s_{U}\right)$. It follows that $s_{M}-(1-\delta) s_{U} \in \operatorname{ker} T$. Then we have
$$\int_{U}\left\langle S_{U}, S_{M}-(1-\delta) S_{U}\right\rangle d \operatorname{Vol}_{\omega}=0$$
Combining these, we can conclude that
$$\begin{aligned}
\int_{U}\left\|S_{U}-S_{M}\right\|^{2} d \operatorname{Vol}_{\omega} & =\int_{U}\left\|S_{U}\right\|^{2}+\left\|S_{M}\right\|^{2}-2 \operatorname{Re}\left\langle S_{U}, S_{M}\right\rangle d \operatorname{Vol}_{\omega} \\
& =\int_{U}\left\|S_{U}\right\|^{2}+\left\|S_{M}\right\|^{2}-2(1-\delta)\left\|S_{U}\right\|^{2} d \operatorname{Vol}_{\omega} \\
& =2 \delta-\int_{M \backslash U}\left\|S_{M}\right\|^{2} d \operatorname{Vol}_{\omega} \leq 2 \epsilon-\int_{M \backslash U}\left\|S_{M}\right\|^{2} d \operatorname{Vol}_{\omega}
\end{aligned}$$
and the lemma follows. \(\square\)

Now we show how to use the peak section to give some estimates about Bergman kernels. Taking a vector $e_{p} \in \mathcal{L}_{p}^{m}$ at $p \in U$ such that $\left\|e_{p}\right\|_{h^{m}}=1$. Then $T_{p}(S)=e_{p}^{*}(S)$ gives a bounded linear functional of $H_{L^{2}}^{0}\left(U, \mathcal{L}^{m}\right)$. If $T_{p} \neq 0$, then the peak section $S_{U} \in H_{L^{2}}^{0}\left(U, \mathcal{L}^{m}\right)$ satisfies that $B_{U}(p, x)=S_{U}(p) \otimes S_{U}(x)^{*}, \forall x \in U$, where $B_{U}$ is the Bergman kernel on $U$. So the Bergman kernel can be represented by a peak section. By combining Lemma 2.1, Theorem 2.1 and Lemma 4.1, we can give a proof of the following Agmon type estimate.

Corollary 4.1. Given constants $n, \delta, \Lambda, \epsilon, Q>0$ and $k \geq 0$, there exists a constant $C$ which depending only on $n, \delta, \Lambda, \epsilon, k, Q$ with the following property.

Let $(M, \omega)$ be a Kähler manifold, $\mathcal{L}$ be a holomorphic line bundle on $M$ equipped with a hermitian metric $h$ such that $\operatorname{Ric}(\omega) \geq-\Lambda \omega$, $\operatorname{Ric}(h) \geq \epsilon \omega$, and $x \in M$. If $(M, \omega)$ isn't complete, we suppose that $M$ is pseudoconvex.

Fix $m \geq C$. Write $U_{m}=B_{\frac{3 \delta \log m}{\sqrt{m}}}\left(x_{0}\right)$. Assume that $\bar{U}_{m}$ is compact, $\operatorname{Ric}(h)=\omega$ on $U_{m}$, $\inf _{y \in U_{m}} \operatorname{inj}(y) \geq \frac{\delta \log m}{\sqrt{m}}$, and $\sum_{j=0}^{2 k} \sup _{U_{m}}\left\|\nabla^{j} \operatorname{Ric}(\omega)\right\| \leq Q$. Then we have
$$\left\|B_{M, \omega, m}(x, y)\right\|_{C^{l} ; h^{m}, \omega} \leq C m^{-k+n+l},$$
for any $x, y \in B_{\frac{2 \delta \log m}{\sqrt{m}}}\left(x_{0}\right)$ satisfying that $\operatorname{dist}_{\omega}(x, y) \geq \frac{\delta \log m}{\sqrt{m}}$, where $B_{M, \omega, m}(x, y)$ is the $m$-th Bergman kernel on $(M, \omega, \mathcal{L}, h)$.

Proof. Without loss of generality, we can assume that $\delta=1$. For each $m \geq 2$, we denote $\frac{\log (m)}{\sqrt{m}}$ briefly by $\varepsilon_{m}$. By the theory of Cheeger-Gromov convergence, we can assume that for any point $y \in U_{m}$, there exists a biholomorphic map $\left(z_{1}, \cdots, z_{n}\right): B_{\mu \varepsilon_{m}}(y) \rightarrow W_{y} \subset \mathbb{C}^{n}$ around $y$ such that $z_{1}(y)=\cdots=z_{n}(y)=0, e^{-Q^{\prime}} \omega_{E u c} \leq \omega \leq e^{Q^{\prime}} \omega_{E u c}$, and the hermitian matrix $\left(g_{i \bar{j}}\right)$ satisfies that $g_{i \bar{j}}(0)=\delta_{i j}, d g_{i \bar{j}}(0)=0$, and $\left\|g_{i \bar{j}}\right\|_{2 k+2, \frac{1}{2} ; W_{y}}^{*} \leq Q^{\prime}$, where $\mu \in(0,1), Q^{\prime} \geq 10$ are constants depending only on $n, k, Q$, and $\|f\|_{k, \alpha}^{*}$ is the interior norms on a domain in $\mathbb{R}^{2 n}$. We further assume that there exists a holomorphic frame $e_{y}$ of $\mathcal{L}$ on this coordinate such that the local representation function of $h, a=\log h\left(e_{y}, e_{y}\right)$, satisfying that $a(0)=0, \frac{\partial^{|I|} a}{\partial z^{I}}(0)=0$ for each milti-index $I$ with $|I| \leq 3$, and $\|a\|_{2 k+4, \frac{1}{2} ; U_{y}}^{*} \leq Q^{\prime} \varepsilon_{m}^{2}$.

For notational convenience the same letter $C \geq 10$ will be used to denote large constants depending only on $n, \Lambda, k, \epsilon, Q$.

Let $\left\{S_{j}\right\}_{j \in J}$ be an orthonormal basis in $H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$, and $x, y$ be points in $B_{2 \varepsilon_{m}}\left(x_{0}\right)$ satisfying that $\operatorname{dist}_{\omega}(x, y) \geq \varepsilon_{m}$. Assume that $S_{j}=f_{j, x} e_{x}^{m}$ on $B_{\mu \varepsilon_{m}}(x)$, and $S_{j}=f_{j, y} e_{y}^{m}$ on $B_{\mu \varepsilon_{m}}(y)$. Then we have $B_{M, \omega, m}=a_{y}^{m}\left(\sum_{j} f_{j, x} \bar{f}_{j, y}\right) e_{x}^{m} \otimes e_{y}^{-m}$ on $B_{\mu \varepsilon_{m}}(x) \times B_{\mu \varepsilon_{m}}(y)$.

Since $\left\|g_{i \bar{j}}\right\|_{2 k+2, \frac{1}{2} ; W_{x}}^{*}+\left\|g_{i \bar{j}}\right\|_{2 k+2, \frac{1}{2} ; W_{y}}^{*} \leq 2 Q^{\prime}$ and $\|a\|_{2 k+4, \frac{1}{2} ; W_{x}}^{*}+\|a\|_{2 k+4, \frac{1}{2} ; W_{y}}^{*} \leq \frac{2 Q^{\prime}(\log m)^{2}}{m}$, it is sufficient to show that
$$\left|\sum_{j} \frac{\partial^{\left|P_{1}\right|} f_{j, x}}{\partial z_{x}^{P_{1}}} \frac{\partial^{\left|P_{2}\right|} \bar{f}_{j, y}}{\partial \bar{z}_{y}^{P_{2}}}\right| \leq C m^{-k+n+\left|P_{1}\right|+\left|P_{2}\right|}, \quad \forall\left|P_{1}\right|+\left|P_{2}\right| \leq k,$$
where $P_{i}=\left(p_{i, 1}, p_{i, 2}, \ldots, p_{i, n}\right) \in \mathbb{Z}_{+}^{n}$ are $n$-tuples of integers.
For each $S \in H^{0}\left(W_{y}, \mathcal{L}^{m}\right), f=e_{y}^{-m}(S)$ is a holomorphic function on $W_{y}$, and hence the map $T_{P, y}(S)=\frac{\partial^{|P|} f}{\partial z^{P}}(y)$ gives a linear functional $T_{P, y}$ on $H^{0}\left(W_{y}, \mathcal{L}^{m}\right)$, where $P=\left(p_{1}, p_{2}, \ldots, p_{n}\right) \in \mathbb{Z}_{+}^{n}$ is an $n$-tuple of integers. Then Lemma 2.1 shows that $\left.T_{P, y}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)} \neq 0$ for sufficiently large $m$. For any $y \in M$ and open neighborhood $U$ of $y$, let $S_{P, y, U}$ denotes the peak section of $\left.T_{P, y}\right|_{H_{L^{2}}^{0}\left(U, \mathcal{L}^{m}\right)} \neq 0$. Then we only need to show that
$$\left|T_{P_{1}, x, M}\left(S_{P_{1}, x, M}\right) \cdot T_{P_{2}, y, M}\left(S_{P_{1}, x, M}\right)\right| \leq C m^{-k+n+\left|P_{1}\right|+\left|P_{2}\right|}, \quad \forall\left|P_{1}\right|+\left|P_{2}\right| \leq k .$$

Combining Theorem 2.1 with Lemma 4.1, we can conclude that
$$\int_{M \backslash B_{\mu e^{-10 Q^{\prime}{ }_{\varepsilon_{m}}}}\left(y_{1}\right)}\left\|S_{0, y_{1}, M}\right\|^{2} d \operatorname{Vol}_{\omega} \leq C m^{-k}, \quad \forall m \geq C, \quad \forall y_{1} \in B_{\frac{11 \varepsilon_{m}}{4}}\left(x_{0}\right) .$$
Hence we see that
$$\begin{aligned}
\left|T_{P_{1}, y_{1}}\left(S_{0, y_{2}, M}\right)\right| & \leq\left(\int_{M \backslash B_{\frac{\varepsilon_{m}}{100}}\left(y_{2}\right)}\left\|S_{0, y_{2}, M}\right\|^{2} d \operatorname{Vol}_{\omega}\right)^{\frac{1}{2}}\left|T_{P_{1}, y_{1}}\left(S_{P_{1}, y_{1}, M \backslash B_{\frac{\varepsilon_{m}}{100}}\left(y_{2}\right)}\right)\right| \\
& \leq C m^{-\frac{k}{2}}\left|T_{P_{1}, y_{1}}\left(S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}}\left(y_{1}\right)\right)\right|
\end{aligned}$$
for any $m \geq C$, and $y_{1}, y_{2} \in B_{\frac{5 \varepsilon_{m}}{2}}\left(x_{0}\right)$ satisfying that $\operatorname{dist}_{\omega}\left(y_{1}, y_{2}\right) \geq \frac{\varepsilon_{m}}{40}$.
By Lemma 2.1, we can find a holomorphic section
$$S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}^{\prime}\left(y_{1}\right)} \in H_{L^{2}}^{0}\left(B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right), \omega, \mathcal{L}^{m}, h^{m}\right),$$
such that $\left\|S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}^{\prime}\left(y_{1}\right)}\right\|_{L^{2} ; h^{m}, \omega}=1,0<T_{P_{1}, y_{1}}\left(S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right)}^{\prime}\right) \leq C m^{\frac{n+\left|P_{1}\right|}{2}}$, and Corollary 2.1 now implies that
$$\left|\int_{B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right)}\left\langle S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}^{\prime}\left(y_{1}\right)}, S^{\prime \prime}\right\rangle_{h^{m}} d \operatorname{Vol}_{\omega}\right| \leq C m^{-\frac{1}{2}}\left\|S^{\prime \prime}\right\|_{L^{2} ; h^{m}, \omega},$$
for any $m \geq C$, and $S^{\prime \prime} \in \operatorname{ker} T_{P_{1}, y_{1}} \cap H_{L^{2}}^{0}\left(B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right), \omega, \mathcal{L}^{m}, h^{m}\right)$. Let
$$\vartheta_{P_{1}, y_{1}, \frac{\varepsilon m}{100}}=\int_{B \frac{\varepsilon_{m}}{100}\left(y_{1}\right)}\left\langle S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}^{\prime}\left(y_{1}\right)}, S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right)}\right\rangle_{h^{m}} d \operatorname{Vol}_{\omega} .$$
Then we have $S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}^{\prime}\left(y_{1}\right)}-\vartheta_{P_{1}, y_{1}, \frac{\varepsilon_{m}}{100}} S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right)} \in \operatorname{ker} T_{P_{1}, y_{1}}$, and we have
$$\begin{aligned}
1-\vartheta_{P_{1}, y_{1}, \frac{\varepsilon_{m}}{100}}^{2} & =\left\|S_{P_{1}, y_{1}, B \frac{\varepsilon_{m}}{100}\left(y_{1}\right)}^{\prime}-\vartheta_{P_{1}, y_{1}, \frac{\varepsilon_{m}}{100}} S_{P_{1}, y_{1}, B \frac{\varepsilon_{m}}{100}\left(y_{1}\right)}\right\|_{L^{2} ; h^{m}, \omega}^{2} \\
& =\left\langle S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right)}^{\prime}, S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right)}^{\prime}-\vartheta_{P_{1}, y_{1}, \frac{\varepsilon_{m}}{100}} S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}\left(y_{1}\right)}\right\rangle_{L^{2} ; h^{m}, \omega} \\
& \leq C m^{-\frac{1}{2}}, \quad \forall m \geq C .
\end{aligned}$$
We thus get $\vartheta_{P_{1}, y_{1}, \frac{\varepsilon_{m}}{100}} \geq 1-C m^{-\frac{1}{2}}, \forall m \geq C$. Now (27) becomes
$$\begin{aligned}
\left|T_{P_{1}, y_{1}}\left(S_{0, y_{2}, M}\right)\right| & \leq C m^{-\frac{k}{2}}\left|T_{P_{1}, y_{1}}\left(S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}}\left(y_{1}\right)\right)\right| \\
& =C m^{-\frac{k}{2}} \vartheta_{P_{1}, y_{1}, \frac{\varepsilon_{m}}{100}}^{-1}\left|T_{P_{1}, y_{1}}\left(S_{P_{1}, y_{1}, B_{\frac{\varepsilon_{m}}{100}}}^{\prime}\left(y_{1}\right)\right)\right| \leq C^{2} m^{-\frac{k}{2}+\frac{n+\left|P_{1}\right|}{2}},
\end{aligned}$$
for any $m \geq C$, and $y_{1}, y_{2} \in B_{\frac{5 \varepsilon_{m}}{2}}\left(x_{0}\right)$ satisfying that $\operatorname{dist}_{\omega}\left(y_{1}, y_{2}\right) \geq \frac{\varepsilon_{m}}{40}$.
It is easy to check that
$$\begin{aligned}
T_{P_{1}, y_{1}}\left(S_{0, y_{2}, M}\right) \overline{T_{0, y_{2}}\left(S_{0, y_{2}, M}\right)} & =\sum_{j} T_{P_{1}, y_{1}}\left(S_{j}\right) \overline{T_{0, y_{2}}\left(S_{j}\right)} \\
& =T_{P_{1}, y_{1}}\left(S_{P_{1}, y_{1}, M}\right) \overline{T_{0, y_{2}}\left(S_{P_{1}, y_{1}, M}\right)} .
\end{aligned}$$

Let $y_{1}=x$. Then we have
$$\begin{aligned}
\left\|S_{P_{1}, x, M}\left(y_{2}\right)\right\|_{h^{m}} & =\left|T_{0, y_{2}}\left(S_{P_{1}, x, M}\right)\right| \\
& =\left|T_{P_{1}, x}\left(S_{0, y_{2}, M}\right)\right| \cdot\left|T_{0, y_{2}}\left(S_{0, y_{2}, M}\right)\right| \cdot\left|T_{P_{1}, x}\left(S_{P_{1}, x, M}\right)\right|^{-1} \\
& \leq C m^{-\frac{k-n-\left|P_{1}\right|}{2}} \cdot m^{\frac{n}{2}} \cdot m^{-\frac{n+\left|P_{1}\right|}{2}} \\
& =C m^{\frac{-k+n}{2}}, \quad \forall m \geq C, \quad \forall y_{2} \in B_{\frac{5 \varepsilon_{m}}{2}}\left(x_{0}\right) \backslash B_{\frac{\varepsilon_{m}}{40}}(x) .
\end{aligned}$$
It follows that
$$\begin{aligned}
& \left|T_{P_{2}, y}\left(S_{P_{1}, x, M}\right)\right| \\
\leq & \left(\int_{B_{2 \varepsilon_{m}}(x) \backslash B_{\frac{\varepsilon_{m}}{40}}(x)}\left\|S_{P_{1}, x, M}\right\|^{2} d \operatorname{Vol}_{\omega}\right)^{\frac{1}{2}}\left|T_{P_{2}, y}\left(S_{P_{2}, y, M \backslash B_{\frac{\varepsilon_{m}}{100}}(x)}\right)\right| \\
\leq & C r_{m}^{n} m^{-\frac{k}{2}}\left|T_{P_{2}, y}\left(S_{P_{2}, y, B_{\frac{\varepsilon_{m}}{}}^{100}}(y)\right)\right| \\
\leq & C^{2} m^{\frac{-k+\left|P_{2}\right|}{2}}(\log m)^{n},
\end{aligned}$$
and (26) is proved. \(\square\)

Remark. It is also shown in the above argument that for each given constant $\mu \in(0,1)$, the peak section, $S_{P_{1}, x, M}$, satisfying that
$$\int_{B_{\frac{2 \delta \log m}{\sqrt{m}}}(x) \backslash B_{\frac{\mu \delta \log m}{\sqrt{m}}}(x)}\left\|S_{P_{1}, x, M}\right\|^{2} d \operatorname{Vol}_{\omega} \leq C m^{-\frac{k}{2}}(\log m)^{n}, \quad \forall m \geq C,$$
where $C$ is a constant depending only on $n, \Lambda, \epsilon, \delta, \mu, k, Q$.

\subsection*{4.2. Approximate the peak section by approximating the metric.}

Let $M$ be a Kähler manifold, $(\mathcal{L}, h)$ be a Hermitian line bundle on $M$, let $\omega$ and $\omega^{\prime}$ be Kähler metrics on $M$, and let $u$ be a smooth real-valued function on $M$. Suppose that there are constants $\delta, \epsilon>0$ such that $e^{-\epsilon} \omega^{n} \leq \omega^{\prime n} \leq e^{\epsilon} \omega^{n}$ and $|u| \leq \delta$. Write $h^{\prime}=e^{-u} h$. Clearly, we see that $H_{L^{2}}^{0}(M, \omega, \mathcal{L}, h)=H_{L^{2}}^{0}\left(M, \omega^{\prime}, \mathcal{L}, h^{\prime}\right)$ as linear subspaces of $H^{0}(M, \mathcal{L})$, and the $L^{2}$-norms are equivalent. So we can use the same notation $H_{L^{2}}^{0}(M, \mathcal{L})$ for them if we don't emphasize the norms. Let $X$ be a closed subspace of $H_{L^{2}}^{0}(M, \mathcal{L})$. Fix a bounded linear functional $0 \neq T: H_{L^{2}}^{0}(M, \mathcal{L}) \rightarrow \mathbb{C}$.

Let $S_{T}$ be the peak section of $T$ in $X \subset H_{L^{2}}^{0}(M, \omega, \mathcal{L}, h)$, and $S_{T}^{\prime}$ be the peak section of $T$ in $X \subset H_{L^{2}}^{0}\left(M, \omega^{\prime}, \mathcal{L}, h^{\prime}\right)$. Then we can estimate the $L^{2}$-norm of $S_{T}-S_{T}^{\prime}$ as follows.

Lemma 4.2. Under the above assumptions, we have
$$\left\|S_{T}-S_{T}^{\prime}\right\|_{L^{2} ; h, \omega}^{2} \leq e^{\delta+\epsilon}-e^{-\delta-\epsilon},$$
and
$$e^{-\frac{\delta+\epsilon}{2}} T\left(S_{T}^{\prime}\right) \leq T\left(S_{T}\right) \leq e^{\frac{\delta+\epsilon}{2}} T\left(S_{T}^{\prime}\right) .$$
Proof. By definition, we can obtain
$$\left\|S_{T}\right\|_{L^{2} ; h^{\prime}, \omega^{\prime}}^{2}=\frac{1}{n!} \int_{M}\left\|S_{T}\right\|_{h^{\prime}}^{2} \omega^{n} \leq \frac{e^{\delta+\epsilon}}{n!} \int_{M}\left\|S_{T}\right\|_{h}^{2} \omega^{n}=e^{\delta+\epsilon} .$$
Hence we have
$$T\left(S_{T}^{\prime}\right) \geq T\left(\left\|S_{T}\right\|_{L^{2} ; h^{\prime}, \omega^{\prime}}^{-1} S_{T}\right)=\left\|S_{T}\right\|_{L^{2} ; h^{\prime}, \omega^{\prime}}^{-1} T\left(S_{T}\right) \geq e^{-\frac{\delta+\epsilon}{2}} T\left(S_{T}\right) .$$

Similarly, we can conclude that
$$\left\|S_{T}^{\prime}\right\|_{L^{2} ; h, \omega}^{2}=\frac{1}{n!} \int_{M}\left\|S_{T}^{\prime}\right\|_{h}^{2} \omega^{n} \leq \frac{e^{\delta+\epsilon}}{n!} \int_{M}\left\|S_{T}^{\prime}\right\|_{h^{\prime}}^{2} \omega^{\prime n}=e^{\delta+\epsilon},$$
and then we see that
$$T\left(S_{T}\right) \geq T\left(\left\|S_{T}^{\prime}\right\|_{L^{2} ; h, \omega}^{-1} S_{T}^{\prime}\right)=\left\|S_{T}^{\prime}\right\|_{L^{2} ; h, \omega}^{-1} T\left(S_{T}^{\prime}\right) \geq e^{-\frac{\delta+\epsilon}{2}} T\left(S_{T}^{\prime}\right) .$$
Combining (36) with (38), we get
$$e^{-\frac{\delta+\epsilon}{2}} T\left(S_{T}^{\prime}\right) \leq T\left(S_{T}\right) \leq e^{\frac{\delta+\epsilon}{2}} T\left(S_{T}^{\prime}\right) .$$

Let $\lambda \in\left[e^{-\frac{\delta+\epsilon}{2}}, e^{\frac{\delta+\epsilon}{2}}\right]$ be the unique constant such that $T\left(S_{T}^{\prime}\right)=\lambda T\left(S_{T}\right)$. Then we have $S_{T}^{\prime}-\lambda S_{T} \in \operatorname{ker} \mathrm{~T} \cap X$. It follows that
$$\int_{M}\left\langle S_{T}^{\prime}, S_{T}\right\rangle_{h} d \operatorname{Vol}_{\omega}-\lambda=\int_{M}\left\langle S_{T}^{\prime}-\lambda S_{T}, S_{T}\right\rangle_{h} d \operatorname{Vol}_{\omega}=0$$
and hence
$$\begin{aligned}
\left\|S_{T}-S_{T}^{\prime}\right\|_{L^{2} ; h, \omega}^{2} & =\int_{M}\left\langle S_{T}^{\prime}-\lambda S_{T}, S_{T}^{\prime}-\lambda S_{T}\right\rangle_{h} d \operatorname{Vol}_{\omega} \\
& =\left\|S_{T}^{\prime}\right\|_{L^{2} ; h, \omega}^{2}-2 \lambda \int_{M}\left\langle S_{T}^{\prime}, S_{T}\right\rangle_{h} d \operatorname{Vol}_{\omega}+\lambda^{2} \\
& =\left\|S_{T}^{\prime}\right\|_{L^{2} ; h, \omega}^{2}-\lambda^{2} \leq e^{\delta+\epsilon}-e^{-\delta-\epsilon}
\end{aligned}$$
and the proof is complete. \(\square\)

\subsection*{4.3. Peak sections on asymptotic complex hyperbolic cusps.}

We will prove Theorem 1.1 in this part.
In this subsection, we let $(M, \omega)$ be a Kähler manifold with $\operatorname{Ric}(\omega) \geq-\Lambda \omega$ and let $(\mathcal{L}, h)$ be a Hermitian line bundle with $\operatorname{Ric}(h) \geq \epsilon \omega$, where $\epsilon, \Lambda>0$ are constants. Suppose that $M$ is pseudoconvex if $(M, \omega)$ is not complete. Assume that there exists an asymptotic complex hyperbolic $\operatorname{cusp}(U, \omega, \mathcal{L}, h) \cong\left(V_{r} / \Gamma_{V}, \omega_{V}-\sqrt{-1} \partial \bar{\partial} u, \mathcal{L}_{V} / \Gamma_{V}, e^{u} h_{V}\right)$ on $(M, \omega)$ such that $\bar{U}$ is complete, where $r \in(0,1)$ is a positive constant, and $u=o(1)$ as $h_{D} \rightarrow 0^{+}$to all orders with respect to $\omega_{V}$. Note that $\left(\mathcal{L}_{V}, h_{V}\right) \cong\left(\mathbb{C},\left|\log h_{D}\right|\right)$ on $V$.

It will cause no confusion if we use the same letter to designate a subset of $V_{r} / \Gamma_{V}$ and the open subset in $U$ corresponding to it. Assume that $\bar{U}$ is complete in $(M, \omega)$.

Since $u=o(1)$ as $h_{D} \rightarrow 0^{+}$to all orders with respect to $\omega_{V}$, we can estimate the lower bounds of injectivity radius on $U$. For any subset $W \subset M$, we write $\operatorname{inj}(W)=\inf _{x \in W} \operatorname{inj}_{M}(x)$.

Lemma 4.3. Let $r$ be the constant defined in above, and $k \in \mathbb{N}$ be a constant. Then there exists a constant $C=C(k, M, \omega)>0$ such that the curvature $\sum_{j=0}^{5 k+10 n}\left\|\nabla^{j} \operatorname{Ric}(\omega)\right\|_{\omega} \leq C$ on $U$, and for each $t \in(0, r)$, we have $\operatorname{inj}\left(U \backslash \pi_{V}\left(V_{t}\right)\right) \geq C^{-1}|\log t|^{-1}$, where $\pi_{V}: V \rightarrow V / \Gamma_{V}$ is the quotient map.

Proof. Since the holomorphic sectional curvature of $\omega_{V}$ is a constant, we can conclude that the sectional curvature of $\omega_{V}$ is bounded. Then $u=o(1)$ implies that the sectional curvature of $\omega$ is bounded on $U$. Similarly, for each $j \in \mathbb{Z}_{\geq 0},\left\|\nabla^{j} \operatorname{Ric}(\omega)\right\|_{\omega}$ is bounded on $U$. As in the proof of Lemma 3.3, Cheeger's lemma now shows that there exists a constant $\zeta>0$ depending only on $(M, \omega, L, h)$, such that $\operatorname{inj}(x) \geq \zeta|\log t|^{-1}$ on $U \backslash \pi_{V}\left(V_{t}\right)$, for any $t \in(0, r)$. Note that $\bar{U}$ is complete. \(\square\)

Now we can construct suitable quasi-plurisubharmonic functions for using $L^{2}$ estimate.
Lemma 4.4. Let $r$ be the constant defined in above, and $\beta>0, \delta \in\left(0, e^{-1}\right)$ be constants. Suppose that $\delta<\min \left\{e^{-1}, r\right\}$. Then for any point $y \in V_{\delta^{1+2 \beta}}$, there exists a quasi-plurisubharmonic function $\psi \in L^{1}(M, \omega)$ such that $\psi \leq 0, \lim _{x \rightarrow y}\left(\psi(x)-\log \left(\operatorname{dist}_{\omega}(x, y)\right)\right)=-\infty, \sqrt{-1} \partial \bar{\partial} \psi \geq-C|\log \delta| \omega$, and $\operatorname{supp} \psi \subset V_{\delta} / \Gamma_{V}$, where $C>0$ is a constant dependent only on $(M, \omega)$, and $\beta$.

Proof. We assume that $\Gamma_{V}=0$ at first. By Theorem 2.1, for sufficiently large integer $k$, we have $(2 \pi)^{n-2} \leq k^{1-n} \rho_{D, \omega_{D}, k} \leq(2 \pi)^{n}$. Choosing an $L^{2}$ orthonormal basis $\left\{S_{j}\right\}_{j=1}^{N_{k}}$ of $H_{L^{2}}^{0}\left(D, \mathcal{L}_{D}^{-k}\right)$ satisfying that $S_{j}\left(\pi_{D}(y)\right)=0, \forall j \geq 2$. Note that we can construct holomorphic functions $\widetilde{S}_{j}$ from $S_{j}$ as in Lemma 3.1. Let
$$f(x)=\left|\widetilde{S}_{1}(x)-\widetilde{S}_{1}(y)\right|^{2}+\sum_{j \geq 2}\left|\widetilde{S}_{j}(x)\right|^{2}, \quad \forall x \in V .$$
Then we have $f(x)=\rho_{D, k}\left(\pi_{D}(x)\right) h_{D}(x)^{k}+\left|\widetilde{S}_{1}(y)\right|^{2}-2 \operatorname{Re}\left(\widetilde{S}_{1}(x) \overline{\widetilde{S}}_{1}(y)\right)$. Clearly, we see that $\left|\widetilde{S}_{1}(y)\right|^{2} \leq \delta^{k(1+2 \beta)}(2 \pi)^{n}$. Since $u=o(1)$, we can conclude that there exists a constant $k_{0}>0$ depending only on $(M, \omega)$ and $\beta$, such that $\|\nabla \log f(x)\|_{\omega} \leq C_{1}|\log \delta|$, for any $x \in V_{\delta} \backslash V_{\delta^{1+\beta}}$ and $k \geq k_{0}$, where $C_{1}$ is a constant depending only on $(M, \omega), k$ and $\beta$. Fix a large integer $k$.

By a straightforward calculation, we see that $\operatorname{dist}_{\omega}\left(V_{\delta^{1+\beta}}, M \backslash V_{\delta}\right) \geq C_{2}^{-1} \log (1+\beta)$ for some constant $C_{2}$ depending only on $(M, \omega)$. Then we can choose a cut-off function $\eta \in C^{\infty}(M)$ such that $\eta=1$ on $V_{\delta^{1+\beta}}, \eta=0$ on $M \backslash V_{\delta}, 0 \leq \eta \leq 1$, and $\sum_{i=0}^{2}\left\|\nabla^{i} \eta\right\|_{\omega} \leq C_{3}$, where $C_{3}$ is a constant depending only on $(M, \omega)$.

Let $C_{f}=\sup _{V_{\delta}} f$, and $\psi_{0}(x)=\eta(x)\left(\log f(x)-\log C_{f}\right)$. It is easy to see that
$$\sup _{V_{\delta} \backslash V_{\delta^{1}+\beta}} \sum_{i=0}^{1}\left\|\nabla^{i}\left(\log f(x)-\log C_{f}\right)\right\|_{\omega} \leq C_{4}|\log \delta|,$$
where $C_{4}$ is a constant depending only on $(M, \omega)$ and $\beta$. Hence we have
$$\begin{aligned}
\sqrt{-1} \partial \bar{\partial} \psi_{0}(x)= & \sqrt{-1}\left(\log f(x)-\log C_{f}\right) \partial \bar{\partial} \eta(x)+\sqrt{-1} \partial \log f(x) \wedge \bar{\partial} \eta \\
& +\sqrt{-1} \partial \eta(x) \wedge \bar{\partial} \log f(x)+\sqrt{-1} \eta(x) \partial \bar{\partial} \log f(x) \\
& \geq-3 C_{3} C_{4}|\log \delta| \omega, \quad \forall x \in V_{\delta} \backslash V_{\delta^{1+\beta}} .
\end{aligned}$$
Here we used $\sqrt{-1} \partial \bar{\partial} \log f(x) \geq 0$ on $V$.
Now we consider the case $\Gamma_{V} \neq 0$. Let $\psi_{0}$ be the quasi-plurisubharmonic function constructed on $\left(V_{r}, \pi_{V}^{*} \omega\right)$. Since $\psi=\sum_{g \in \Gamma_{V}} \psi_{0} \circ g$ is invariant under the action of $\Gamma_{V}$, we see that $\psi$ gives the function we need. \(\square\)

Remark. If we choose $f(x)=\sum_{j=1}^{N_{k}}\left|S_{j}(x)\right|^{2}$ in the proof of Lemma 4.4, then we can find a quasi-plurisubharmonic function $\psi \in L^{1}(M, \omega)$ such that $\psi \leq 0, \lim _{h_{D}(x) \rightarrow 0}\left(\psi(x)-\log \left(h_{D}(x)\right)\right)=-\infty$, $\sqrt{-1} \partial \bar{\partial} \psi \geq-C|\log \delta| \omega, \operatorname{supp} \psi \subset V_{\delta}$, and $\psi$ is invariant under the action of $\Gamma_{V}$ on $V_{r} \cong U$, where $C>0$ is a constant dependent only on $(M, \omega)$, and $\beta$.

Since $(U, \omega, \mathcal{L}, h) \cong\left(V_{r} / \Gamma_{V}, \omega_{V}-\sqrt{-1} \partial \bar{\partial} u, \mathcal{L}_{V} / \Gamma_{V}, e^{u} h_{V}\right)$ and $\left(\mathcal{L}_{V}, h_{V}\right) \cong\left(\mathbb{C},\left|\log h_{D}\right|\right)$ on $V$, we can conclude that any $\mathcal{L}^{m}$-valued holomorphic section on $U$ can be represented by a $\Delta_{\Gamma_{V}, m^{-}}$ invariant holomorphic function on $V_{r}, \forall m \in \mathbb{N}$. It follows that any finite linear combination of $\delta_{x}$ and its derivatives gives a bounded linear functional on $H_{L^{2}}^{0}\left(U, \mathcal{L}^{m}\right)$, where $\delta_{x}$ is the Dirac function
at $x$. By applying Hörmander's $L^{2}$ estimate in a similar way as in [33, Proposition 1.1], we can give the following estimates for such peak sections. For abbreviation, we denote $e^{-\frac{\sqrt{m}}{\log m}}$ and $\frac{\log m}{\sqrt{m}}$ briefly by $r_{m}$ and $\varepsilon_{m}$, respectively, for any $m \geq 2$.

Proposition 4.1. Let $\kappa$ and $\delta$ be given positive constants. Then there are constants $C, m_{0}$ that depend only on $(M, \omega, \mathcal{L}, h), k, \kappa, \delta$ and $l$, and satisfies the following property.

Let $m \geq n+1$ be an integer satisfies that $r_{m}^{\kappa}<e^{-1} r$. Choosing a constant $\gamma_{m} \in\left[r_{m}^{\kappa}, e^{-1} r\right)$, a point $x_{m} \in \pi_{V}\left(V_{\gamma_{m}}\right)$, and a linear functional $T_{m}$ defined by finite linear combination of $\delta_{x_{m}}$ and its derivatives, where $\pi_{V}: V \rightarrow V / \Gamma_{V}$ is the quotient map. Assume that the order of derivatives contained in $T_{m}$ is at most $k$. Let $U_{m}$ be an open neighborhood of $x_{m} \in M$. Suppose that $U_{m} \subset U$ and $\operatorname{dist}_{\omega}\left(\pi_{V}\left(V_{\gamma_{m}}\right), M \backslash U_{m}\right) \geq \delta \varepsilon_{m}$. Then
$$\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}\right\| \geq\left(1-\frac{C}{m^{l}}\right)\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)}\right\| .$$
Proof. Without loss of generality, we can assume that $\kappa=\delta=1$. When $\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)}=0$, this proposition is obvious. So we can assume that $\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)} \neq 0$ from now.

The proof falls naturally into two parts by whether $x_{m}$ belongs to the set $\pi_{V}\left(V_{r_{m}^{e}}\right)$.
Part 1. We start by prove the estimate (42) when $x_{m} \in \pi_{V}\left(V_{\gamma_{m}}\right) \backslash \pi_{V}\left(V_{r_{m}^{e}}\right)$.
By Lemma 4.3, we see that $\left\|\left(M, \omega, x_{m}\right)\right\|_{C^{5 k+10, \frac{1}{2}, \varepsilon_{m}}}^{\text {holo }} \leq Q^{\prime}$, where $\|\cdot\|_{C^{k, \alpha}, r}^{\text {holo }}$ is the Cheeger-Gromov $C^{k, \alpha}$-norm defined in Definition 2.1, and $Q^{\prime}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), k$ and $r$. Then we can find a holomorphic coordinate $\phi_{x_{m}}:\left(z_{1}, \cdots, z_{n}\right): W_{\xi, x_{m}} \rightarrow B_{\xi \varepsilon_{m}}(0) \subset \mathbb{C}^{n}$ around $x_{m}$, such that the hermitian matrices $\left(g_{i \bar{j}}\right)$ satisfying that $g_{i \bar{j}}(0)=\delta_{i j}, d g_{i \bar{j}}(0)=0$, $e^{-Q} \omega_{E u c} \leq\left(\phi_{x_{m}}^{-1}\right)^{*} \omega \leq e^{Q} \omega_{E u c}$, and there are holomorphic frames $e_{1, m}$ of $\mathcal{L}_{V}$ on $W_{\xi, x_{m}}$ such that $a=\log h\left(e_{1, m}, e_{1, m}\right)$ satisfying that $a(0)=0, \frac{\partial^{|I|} a}{\partial z^{I}}(0)=0$ for each milti-index $I$ with $|I| \leq 3$, and $\|a\|_{5 k+10, \frac{1}{2} ; W_{\xi, x_{m}}}^{*} \leq Q \varepsilon_{m}^{2}$, where $\xi, Q>0$ are constants depending only on $(M, \omega, \mathcal{L}, h), k$ and $r$. For each $\lambda \in(0, \xi)$, the inverse image of $B_{\lambda \varepsilon_{m}}(0)$ about the map $\phi_{x_{m}}$ will be denoted by $W_{\lambda, x_{m}}$.

Let $\eta(t) \in C^{\infty}(\mathbb{R})$ be a cut-off function such that $\eta=1$ on $(-\infty, 1], \eta=0$ on $[2, \infty),-2 \leq$ $\eta^{\prime} \leq 0,\left|\eta^{\prime \prime}\right| \leq 8$. Set $\eta_{\lambda, m}(z)=\eta\left(\frac{4|z|^{2}}{\lambda^{2} \varepsilon_{m}^{2}}\right)$, and $\psi(z)=4(k+n) \log \left(\frac{4|z|^{2}}{\lambda^{2} \varepsilon_{m}^{2}}\right) \eta_{\lambda, m}(z)$. Then we have $\sqrt{1} \partial \bar{\partial} \psi \geq-C_{1} \lambda^{-2} \varepsilon_{m}^{-2} \omega_{E u c}$, where $C_{1}=C_{1}(n)>0$ is a constant. It will cause no confusion if we use the same letter to designate a function on $B_{\lambda \varepsilon_{m}}(0)$ and the composite of it with the map $\phi_{x_{m}}$.

Since $\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)} \neq 0$, there exists a peak section $S_{T_{m}, W_{\lambda, x_{m}}}$ of $T_{m}$ on $W_{\lambda, x_{m}}$. By the Hörmander's $L^{2}$ estimate, we can find a smooth $\mathcal{L}^{m}$-valued section $u_{1} \in L^{2}$ on $M$ such that $\bar{\partial} u_{1}=\bar{\partial}\left(\eta_{\lambda, m} S_{T_{m}, W_{\lambda, x_{m}}}\right)=\bar{\partial} \eta_{\lambda, m} \otimes S_{T_{m}, W_{\lambda, x_{m}}}$, and
$$\begin{aligned}
\int_{M}\left\|u_{1}\right\|_{h^{m}}^{2} e^{-\psi} d \operatorname{Vol}_{\omega} & \leq \frac{C_{2}}{\epsilon m-C_{1} e^{Q} \lambda^{-2} \varepsilon_{m}^{-2}} \int_{M}\left\|\bar{\partial} u_{1}\right\|_{h^{m}, \omega}^{2} e^{-\psi} d \operatorname{Vol}_{\omega} \\
& \leq C_{2}^{2}(\log m)^{-2} \int_{\operatorname{supp}\left\|\nabla \eta_{\lambda, m}\right\|}\left\|S_{T_{m}, W_{\lambda, x_{m}}}\right\|_{h^{m}}^{2} e^{-\psi} d \operatorname{Vol}_{\omega} \\
& \leq C_{2}^{3}(\log m)^{-2} \int_{W_{\lambda, x_{m}}}\left\|S_{T_{m}, W_{\lambda, x_{m}}}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega}=C_{2}^{3}(\log m)^{-2},
\end{aligned}$$
for any $m \geq 1+e^{10 C_{1} e^{Q} \lambda^{-2} \epsilon^{-1}}$, where $C_{2}>1$ is a constant depending only on $\epsilon, C_{1}, \Lambda, \lambda, k$ and $r$. We assume that $m \geq 1+e^{10 C_{1} e^{Q} \lambda^{-2} \epsilon^{-1}}$ from now. Then the integrability of $u_{1}$ implies that
$T_{m}\left(u_{1}\right)=0$, and hence we have
$$\begin{aligned}
\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}\right\| & \geq\left\|\eta_{\lambda, m} S_{T_{m}, W_{\lambda, x_{m}}}-u_{1}\right\|_{L^{2} ; h^{m}, \omega}^{-1}\left|T_{m}\left(\eta_{\lambda, m} S_{T_{m}, W_{\lambda, x_{m}}}-u_{1}\right)\right| \\
& \geq\left(\left\|\eta_{\lambda, m} S_{T_{m}, W_{\lambda, x_{m}}}\right\|_{L^{2} ; h^{m}, \omega}+\left\|u_{1}\right\|_{L^{2} ; h^{m}, \omega}\right)^{-1}\left|T_{m}\left(S_{T_{m}, W_{\lambda, x_{m}}}\right)\right| \\
& \geq\left(1+C_{2}^{3}(\log m)^{-1}\right)^{-1}\left|T_{m}\left(S_{T_{m}, W_{\lambda, x_{m}}}\right)\right| .
\end{aligned}$$

Analysis similar to that in the proof of Corollary 4.1 shows that for any $\lambda \in\left(0, \frac{\xi}{10}\right)$,
$$\begin{aligned}
& \| T_{m}\left(S_{\left.T_{m}, W_{9 \lambda, x_{m}}\right) S_{T_{m}, W_{9 \lambda, x_{m}}}(y) \|}\left\|T_{m}\left(S_{y, W_{9 \lambda, x_{m}}}\right) S_{y, W_{9 \lambda, x_{m}}}(y)\right\|\right. \\
\leq & \left(\int_{W_{\lambda, x_{m}}}\left\|S_{y, W_{9 \lambda, x_{m}}}\right\|^{2} d \operatorname{Vol}_{\omega}\right)^{\frac{1}{2}}\left|T_{m}\left(S_{T_{m}, W_{\lambda, x_{m}}}\right)\right|\left(\rho_{m, \omega, W_{9 \lambda, x_{m}}}(y)\right)^{\frac{1}{2}} \\
\leq & C_{3} m^{-2 k-4 n-l}\left|T_{m}\left(S_{T_{m}, W_{9 \lambda, x_{m}}}\right)\right|, \quad \forall y \in W_{8 \lambda, x_{m}} \backslash W_{3 \lambda, x_{m}},
\end{aligned}$$
where $C_{3}=C_{3}\left(\lambda, C_{1}, C_{2}, \epsilon, \Lambda, k, r\right)>0$ is a constant, and $S_{y, W}$ is the peak section of $\delta_{y}$ on $W$. It follows that $\left\|S_{T_{m}, W_{3 \lambda, x_{m}}}\right\| \leq C_{3} m^{-2 k-4 n-l}$ on $W_{8 \lambda, x_{m}} \backslash W_{3 \lambda, x_{m}}$. By applying the Hörmander's $L^{2}$ estimate on $W_{8 \lambda, x_{m}} \backslash W_{3 \lambda, x_{m}}$, we can conclude that
$$\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}\right\| \geq\left(1-C_{4} m^{-2 k-2 n-l}\right)\left|T_{m}\left(S_{T_{m}, W_{9 \lambda, x_{m}}}\right)\right|,$$
where $C_{4}=C_{4}\left(\lambda, C_{1}, C_{2}, \epsilon, \Lambda, k, r\right)>0$ is a constant. Fix $\lambda=\frac{\xi}{100}$. It is easy to see that
$$\left|T_{m}\left(S_{T_{m}, W_{9 \lambda, x_{m}}}\right)\right|=\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(W_{9 \lambda, x_{m}}, \mathcal{L}^{m}\right)}\right\| \geq\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m},\left.\mathcal{L}^{m}\right|_{U_{m}}\right)}\right\| .$$
Combining (46) with (47), we can conclude that the estimate (42) holds for $x_{m} \in V_{\gamma_{m}} \backslash V_{r_{m}^{e}}$ and $C=e^{(2 k+2 n+l)\left(C_{4}+10 C_{1} e^{Q} \lambda^{-2} \epsilon^{-1}\right)}$.

Part 2. To complete the proof, we need to prove the estimate (42) when $x_{m} \in \pi_{V}\left(V_{r_{m}^{e}}\right)$.
By Lemma 4.4, we can find a quasi-plurisubharmonic function $\psi_{m}$ on $M$ by choosing $\delta_{m}=r_{m}^{2}$ and $\beta_{m}=0.1$. Then we have $\sqrt{-1} \partial \bar{\partial} \psi_{m} \geq-C_{5} \varepsilon_{m}^{-1} \omega$, where $C_{5}>0$ is a constant depends only on $(M, \omega)$. Let $\eta_{m} \in C^{\infty}(M)$ be a cut-off function such that $\eta_{m}=1$ on $\pi_{V}\left(V_{\delta_{m}}\right), \eta_{m}=0$ on $M \backslash \pi_{V}\left(V_{r_{m}^{1.5}}\right)$, and $\sum_{i=1}^{i=2}\left\|\nabla^{i} \eta_{m}\right\|_{\omega} \leq C_{6}$, where $C_{6}>0$ is a constant depends only on $(M, \omega)$.

Choosing a large integer $m_{0}$ such that $m_{0}>2 C_{5} \sqrt{m_{0}}+1$. By the Hörmander's $L^{2}$ estimate, we can find a smooth $\mathcal{L}^{m}$-valued section $u_{2}$ on $M$ such that $\bar{\partial} u_{2}=\bar{\partial}\left(\eta_{m} S_{T_{m}, V_{r_{m}^{1} .5} / \Gamma_{V}}\right)$, and
$$\begin{aligned}
& \int_{M}\left\|u_{2}\right\|_{h^{m}}^{2} e^{-5(n+k) \psi_{m}} d \operatorname{Vol}_{\omega} \\
\leq & \frac{1}{m-C_{3} \varepsilon_{m}^{-1}} \int_{M}\left\|\bar{\partial} u_{2}\right\|_{h^{m}, \omega}^{2} e^{-5(n+k) \psi_{m}} d \operatorname{Vol}_{\omega} \\
\leq & \frac{C_{4}}{m-C_{3} \sqrt{m}} \int_{\pi_{V}\left(V_{r_{m}^{1} .5}\right) \backslash \pi_{V}\left(V_{\delta_{m}}\right)}\left\|S_{T_{m}, V_{r_{m^{1}} .5} / \Gamma_{V}}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega} \leq \frac{C_{7}}{m-C_{3} \sqrt{m}},
\end{aligned}$$
where $S_{T_{m}, V_{r_{m}^{1.5}} / \Gamma_{V}}$ is the peak section of $T_{m}$ on $V_{r_{m}^{1.5}} / \Gamma_{V}$, and $C_{7}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h)$ and $k$. Then there exists a constant $C_{8}>0$ depending only on $(M, \omega, \mathcal{L}, h)$
and $k$, such that $\int_{M}\left\|u_{2}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega} \leq C_{8} m^{-1}, \forall m \geq m_{0}$. By the integrability of $u_{2}$, we see that $T_{m}\left(u_{2}\right)=0$, and hence we have
$$\begin{aligned}
\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}\right\| & \geq\left(\int_{M}\left\|\eta_{m} S_{T_{m}, V_{r_{m}^{1,5}} / \Gamma_{V}}-u_{2}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega}\right)^{-\frac{1}{2}}\left|T_{m}\left(\eta_{m} S_{T_{m}, V_{r_{m}^{1,5} / \Gamma_{V}}}-u_{2}\right)\right| \\
& \geq\left(1+C_{8} m^{-1}\right)^{-\frac{1}{2}}\left|T_{m}\left(S_{T_{m}, V_{r_{m}^{1,5}} / \Gamma_{V}}\right)\right| .
\end{aligned}$$
Analysis similar to that in the Part 1 now shows that for any integer $l \geq 0$,
$$\begin{aligned}
& \left\|T_{m}\left(S_{T_{m}, U_{m}}\right) S_{T_{m}, U_{m}}(y)\right\|=\left\|T_{m}\left(S_{y, U_{m}}\right) S_{y, U_{m}}(y)\right\| \\
\leq & \left(\int_{V_{r_{m}^{1.5}} / \Gamma_{V}}\left\|S_{y, U_{m}}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega}\right)^{\frac{1}{2}}\left|T_{m}\left(S_{T_{m}, V_{r_{m}^{1.5} / \Gamma_{V}}}\right)\right|\left(\rho_{m, \omega, U_{m}}(y)\right)^{\frac{1}{2}} \\
\leq & C_{9} m^{-2 k-4 n-l}\left|T_{m}\left(S_{T_{m}, U_{m}}\right)\right|, \quad \forall y \in \pi_{V}\left(V_{r_{m}}\right) \backslash \pi_{V}\left(V_{r_{m}^{1.4}}\right),
\end{aligned}$$
where $C_{9}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), k$ and $l$, and $S_{y, W}$ is the peak section of $\delta_{y}$ on $W$. Since $\left.T_{m}\right|_{H_{L^{2}}^{0}\left(V_{\beta_{m}} / \Gamma_{V}, \mathcal{L}^{m}\right)} \neq 0$, we can see that $\left\|S_{T_{m}, U_{m}}(y)\right\| \leq C_{7} m^{-2 k-4 n-l}$, for any $y \in \pi_{V}\left(V_{r_{m}}\right) \backslash \pi_{V}\left(V_{r_{m}^{1.4}}\right)$.

Let $\chi_{m} \in C^{\infty}(M)$ be a cut-off function such that $\chi_{m}=1$ on $\pi_{V}\left(V_{r_{m}^{1.4}}\right), \chi_{m}=0$ on $M \backslash \pi_{V}\left(V_{r_{m}^{1.1}}\right)$, and $\sum_{i=1}^{2}\left\|\nabla^{i} \chi_{m}\right\| \leq C_{10}$, where $C_{10}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), k$ and $l$. By using the Hörmander's $L^{2}$ estimate to the weight function $e^{-5(n+k) \psi_{m}}$ and the smooth $\mathcal{L}^{m}$-valued (0, 1)-form $\bar{\partial}\left(\chi_{m} S_{T_{m}, U_{m}}\right)$, we can conclude that
$$\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}\right\| \geq\left(1-C_{11} m^{-2 k-2 n-l}\right)\left\|\left.T_{m}\right|_{H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)}\right\|,$$
where $C_{11}>0$ is a constant depending only on $(M, \omega, \mathcal{L}, h), k$ and $l$. This completes the proof. \(\square\)

We assume that $u=O\left(\left|\log h_{D}\right|^{-\alpha}\right)$ as $h_{D} \rightarrow 0^{+}$to all orders with respect to $\omega_{V}$ for some constant $\alpha>0$ from now. Then we can give an estimate for the derivatives of holomorphic sections.

Lemma 4.5. We follow the above assumption about $u$. Given constants $n, k \in \mathbb{N}$ and $Q>0$. There exists a constant $C>0$ with the following property.

Let $(M, \omega)$ be an $n$-dimensional Kähler manifold, $\mathcal{L}$ be a holomorphic line bundle on $M$ equipped with a hermitian metric $h$, and $x \in M$. Assume that $\operatorname{inj}\left(B_{r}(x)\right) \geq r, \operatorname{Ric}(h)=\omega$ on $B_{r}(x)$, and $\sum_{j=0}^{k} \sup _{B_{r}(x)}\left\|\nabla^{j} \operatorname{Ric}(\omega)\right\|_{\omega} \leq Q$, where $r>0$ is a constant. Then for any $k, m \in \mathbb{N}$ and $S \in H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$, we have $\left\|\nabla^{l} S(x)\right\|^{2}+\left\|\nabla^{* l} S^{*}(x)\right\|^{2} \leq C m^{n+k}(\min \{\sqrt{m} r, 1\})^{-2 n-2 k}\|S\|_{L^{2} ; B_{r}(x)}^{2}$.

Proof. Without loss of generality, we can assume that $\|S\|_{L^{2} ; B_{r}(x)} \neq 0$. By replacing $(M, \omega)$ with $(M, m \omega)$, we can reduce this lemma to the case of $m=1$. By the theory of Cheeger-Gromov $C^{k, \alpha}$-convergence, we can find a coordinate $\left(z_{1}, \cdots, z_{n}\right): B_{r}(x) \rightarrow U_{x} \subset \mathbb{C}^{n}$ such that the image of $x$ is $0, e^{-Q^{\prime}} \omega_{E u c} \leq \omega \leq e^{Q^{\prime}} \omega_{E u c}$, and the hermitian matrix $\left(g_{i \bar{j}}\right)$ satisfies that $g_{i \bar{j}}(0)=\delta_{i j}$, $d g_{i \bar{j}}(0)=0$, and $\left\|g_{i \bar{j}}\right\|_{k+1, \frac{1}{2} ; U_{x}}^{*} \leq Q^{\prime}$, where $\|f\|_{k, \alpha}^{*}$ is the interior norms on a domain in $\mathbb{R}^{2 n}$, and $Q^{\prime}=Q^{\prime}(n, k, Q)>0$ is a constant. We further assume that there exists a holomorphic frame $e_{x}$ of $\mathcal{L}$ on this coordinate such that the local representation function of $h, a=h\left(e_{x}, e_{x}\right)$, satisfying that $a(0)=1$ and $\|a-1\|_{k+1, \frac{1}{2} ; U_{x}}^{*} \leq Q^{\prime} r^{2}$.

Write $S=f e_{x}$, where $f \in \mathcal{O}\left(U_{x}\right)$ is a holomorphic function. Now we are reduced to establishing the estimate $\sum_{l=0}^{k}\left\|\nabla^{l} f(0)\right\|_{\omega_{E u c}}^{2} \leq C(\min \{r, 1\})^{-2 n-2 k} \int_{U_{x}}|f|^{2} d \operatorname{Vol}_{\mathbb{C}^{n}}$ on the Euclidean domain $U_{x} \subset \mathbb{C}^{n}$ containing $B_{e^{-Q^{\prime}}}(0)$. This is an immediate consequence of the standard interior estimates for derivatives of harmonic functions. This is our claim. \(\square\)

As a corollary of Lemma 4.5, we can give the following estimate of the derivatives of the holomorphic sections around the complex hyperbolic cusps. Here we denote $e^{-\frac{\sqrt{m}}{\log m}}$ and $\frac{\log m}{\sqrt{m}}$ briefly by $r_{m}$ and $\varepsilon_{m}$, respectively, for any $m \geq 2$.

Corollary 4.2. We follow the above assumption about $u$. Given $\delta, \kappa, \beta, k>0$, there exists a constant $C>1$ depending only on $(M, \omega, \mathcal{L}, h), \delta, \kappa, \beta$ and $k$ satisfying the following property.

Let $m \geq C$ be an integer such that $\pi_{V}\left(V_{r_{m}^{\kappa}}\right) \subset U, U_{m}$ be a sequence of open subsets of $U$ containing $\pi_{V}\left(V_{r_{m}^{\kappa}}\right)$, and $\widetilde{U}_{m}$ be open subsets of $U_{m}$ such that $\operatorname{dist}_{\omega}\left(\widetilde{U}_{m}, M \backslash U_{m}\right) \geq \delta \varepsilon_{m}$. Then for any $S \in H_{L^{2}}^{0}\left(U_{m}, \mathcal{L}^{m}\right)$, we have $\left\|\nabla^{k} S(x)\right\|_{h^{m}, \omega}^{2}+\left\|\nabla^{* k} S^{*}(x)\right\|_{h^{m}, \omega}^{2} \leq C m^{C}\left|\log h_{D}(x)\right|^{-\beta}\|S\|_{L^{2} ; h^{m}, \omega}^{2}$, $\forall x \in \widetilde{U}_{m}$, where $S^{*}$ is the smooth section of $\mathcal{L}^{-m}$ given by $S^{*}(e)=h^{m}(e, S)$, and $\nabla^{*}$ is the Chern conncection of the Hermitian line bundle $\left(\mathcal{L}^{-m}, h^{-m}\right)$.

Proof. Without loss of generality, we can assume that $\|S\|_{L^{2} ; h^{m}, \omega}=1$ and $\kappa=\delta=1$.
Note that that $u=O\left(\left|\log h_{D}\right|^{-\alpha}\right)$ as $h_{D} \rightarrow 0^{+}$to all orders with respect to $\omega_{V}$ for some constant $\alpha>0$. Let $\tau_{m}=e^{-m^{2+2 \alpha^{-1}}}$. By Lemma 4.3, we see that there exists a constant $C_{1}>1$ depending only on $(M, \omega)$ and $k$, such that for any $m \in \mathbb{N}$, we have inj $\left(U \backslash \pi_{V}\left(V_{\tau_{m}^{m}}\right)\right) \geq C_{1}^{-1} m^{-2-2 \alpha^{-1}-1}$, and $\sum_{j=0}^{2 k}\left\|\nabla^{j} \operatorname{Ric}(\omega)\right\|_{\omega} \leq C_{1}$ on $U$. Then we can use Lemma 4.5 to find a constant $C_{2}>0$ depending only on $(M, \omega)$ and $k$, such that
$$\sup _{\widetilde{U}_{m} \backslash \pi_{V}\left(V_{\tau_{m}^{m}}\right)}\left(\left\|\nabla^{k} S\right\|^{2}+\left\|\nabla^{* k} S^{*}\right\|^{2}\right) \leq C_{2} m^{C_{2}} .$$
Since $\left|\log h_{D}\right| \leq m^{2+2 \alpha^{-1}}$ on $\widetilde{U}_{m} \backslash \pi_{V}\left(V_{\tau_{m}^{m}}\right)$, we can conclude that
$$\left\|\nabla^{k} S(x)\right\|^{2}+\left\|\nabla^{* k} S^{*}(x)\right\|^{2} \leq C_{2} m^{C_{2}+2 \beta+2 \alpha^{-1} \beta}\left|\log h_{D}(x)\right|^{-\beta}, \quad \forall x \in \widetilde{U}_{m} \backslash \pi_{V}\left(V_{\tau_{m}^{m}}\right) .$$
By the definition, we have $\|S\|^{2} \leq \rho_{U_{m}, \omega, \mathcal{L}, h, m}$ on $U_{m}$. Since $h=\left|\log h_{D}\right| e^{u}, \omega=\omega_{V}-\sqrt{-1} \partial \bar{\partial} u$ and $u=O\left(\left|\log h_{D}\right|^{-\alpha}\right)$, we see that
$$\sup _{V_{\tau_{m}} / \Gamma_{V}}\left(\left|\log \left(\frac{h^{m}}{\left|\log h_{D}\right|^{m}}\right)\right|+\left|\log \left(\frac{\omega^{n}}{\omega_{V}^{n}}\right)\right|\right) \leq C_{3} m\left|\log \tau_{m}\right|^{-m \alpha} \leq C_{3} m^{-1},$$
where $C_{3}>1$ is a constant depending only on ( $M, \omega$ ). Lemma 4.2 now shows that
$$\rho_{V_{\tau_{m}} / \Gamma_{V}, \omega, m}(x) \leq e^{C_{3}} \rho_{V_{\tau_{m}} / \Gamma_{V}, \omega_{V}, m}(x), \quad \forall x \in V_{\tau_{m}} / \Gamma_{V},$$
where $\rho_{V_{\tau_{m}} / \Gamma_{V}, \omega, m}$ is the $m$-th Bergman kernel on $\left(V_{\tau_{m}} / \Gamma_{V}, \omega, \mathcal{L}, h\right)$.
Analysis similar to that in the proof of Proposition 3.1 shows that for any $m \geq n+1$,
$$\rho_{V_{\tau_{m}} / \Gamma_{V}, \omega_{V}, m}(x) \leq C_{4}\left|\log h_{D}(x)\right|^{m} \sum_{q=1}^{\infty} q^{n+1} \tau_{m}^{-q} h_{D}(x)^{q}, \quad \forall x \in V_{\tau_{m}} / \Gamma_{V},$$
where $C_{4}>1$ is a constant depending only on $(M, \omega)$. Then we can conclude that
$$\begin{aligned}
\rho_{V_{\tau_{m}} / \Gamma_{V}, \omega_{V}, m}(x) & \leq C_{4} h_{D}(x)^{\frac{1}{2}}\left|\log h_{D}(x)\right|^{m} \sum_{q=1}^{\infty} q^{n}\left(\tau_{m}^{-q} h_{D}(x)^{\frac{1}{2}}\right)^{q} \\
& \leq C_{5}\left|\log h_{D}(x)\right|^{m} h_{D}(x)^{\frac{1}{2}} \leq C_{5}^{2}\left(\tau_{m}^{\frac{m}{4}}\left|m \log \tau_{m}\right|^{m}\right) h_{D}(x)^{\frac{1}{4}} \leq C_{5}^{3} h_{D}(x)^{\frac{1}{4}},
\end{aligned}$$
for any $m \geq n+1$ and $x \in V_{\tau_{m}^{m}} / \Gamma_{V}$, where $C_{5}>1$ is a constant depending only on $(M, \omega)$.
It follows that there exists a constant $C_{6}>1$ depending only on $(M, \omega)$, such that for any $x \in$ $V_{\tau_{m}^{m}} / \Gamma_{m}$, we have $\|S\|_{L^{2}, B_{1}(x) ; h^{m}, \omega}^{2} \leq C_{6} h_{D}(x)^{C_{6}^{-1}}$. Applying Lemma 4.5 again, we can find a constant $C_{7}$ depending only on $(M, \omega), k$ and $\beta$ such that $\left\|\nabla^{k} S(x)\right\|^{2}+\left\|\nabla^{* k} S^{*}(x)\right\|^{2} \leq C_{7}\left|\log h_{D}(x)\right|^{-\beta}$ on $V_{\tau_{m}^{m}}$. This completes the proof. \(\square\)

Before proving Theorem 1.1, we now prove that $\rho_{V_{\sigma_{m}} / \Gamma_{V}, \omega, m}>0$ everywhere. Hence the fraction in inequality (3) is well defined.
Lemma 4.6. Let $x \in V / \Gamma_{V}, m_{0} \geq n+1$ be an integer, and $T \in H^{0}\left(V / \Gamma_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{m_{0}}\right)^{*}$ be a linear functional defined by finite linear combination of $\delta_{x}$. Assume that $T \neq 0$ as a distribution, and the quotient space $V / \Gamma_{V}$ is a manifold. Then $\left.T\right|_{H_{L^{2}}^{0}\left(V / \Gamma_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{m_{0}}\right)} \neq 0$.
Proof. To shorten notation, we write $N$ instead of $\left|\Gamma_{V}\right|$.
Since $\Theta_{\Gamma_{V}}\left(g^{N}\right)=1, \forall g \in \Gamma_{V}$, we see that $\left(V / \Gamma_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{N}\right) \cong\left(\mathbb{C},\left|\log h_{D}\right|^{N}\right)$. Then there exists a holomorphic section $e \in H^{0}\left(V / \Gamma_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{N}\right)$ such that $\|e\|_{h_{V}^{N}}^{2}=\left|\log h_{D}\right|^{N}$. For each $p \in \mathbb{Z}_{\geq 0}$, we can define $T_{p} \in H^{0}\left(V / \Gamma_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{m}\right)^{*}$ by
$$T_{p}(S)=T\left(e^{-p}(S)\right) e^{p}, \quad \forall S \in H^{0}\left(V / \Gamma_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{m_{0}+p N}\right) .$$

Since $\left(V / \Gamma_{V}, \omega_{V}, \mathcal{L}_{V} / \Gamma_{V}, h_{V}\right)$ is a polarized complete Kähler manifold with constant Ricci curvature $\operatorname{Ric}\left(\omega_{V}\right)=-(n+1) \omega_{V}$, we see that Lemma 2.1 implies that there exist a large integer $p_{1}$ and a section $S_{p_{1}} \in H_{L^{2}}^{0}\left(V / \Gamma_{V},\left(\mathcal{L}_{V} / \Gamma_{V}\right)^{m_{0}+p_{1} N}\right)$ such that $T_{p_{1}}\left(S_{p_{1}}\right) \neq 0$. It follows that $T\left(e^{-p_{1}}(S)\right) \neq 0$.

Let $S^{\prime}=f e_{\mathcal{L}_{V}}^{m_{0}} \in H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m_{0}}\right)_{\Gamma_{V}}$ be the pullback of $e^{-p_{1}}(S)$. By the statement above Proposition 3.1, we can find constants $a_{q, j}$ such that $\sum_{q=1}^{\infty} \sum_{j=1}^{N_{m_{0}, q}^{\prime}} a_{q, j} \widetilde{S}_{m_{0}, q, j}^{\prime}$ converge to $f$ uniformly on a neighborhood of $x$, where $\left\{S_{m_{0}, q, j}^{\prime}\right\}_{j=1}^{N_{m_{0}, q}^{\prime}}$ is an $L^{2}$ orthonormal set in the Hilbert space $H_{L^{2}}^{0}\left(D, \mathcal{L}_{D}^{-q}\right)$, and $\widetilde{S}_{m_{0}, q, j}^{\prime}$ denote the holomorphic function corresponding to $S_{m_{0}, q, j}^{\prime}$ defined in Lemma 3.1. Now we see that there exists a holomorphic function $\widetilde{S}_{m_{0}, q, j}$ such that $T\left(\widetilde{S}_{m_{0}, q, j}^{\prime} e_{\mathcal{L}_{V}}^{m_{0}}\right) \neq$ 0, and the lemma follows. \(\square\)

Now we are ready to prove Theorem 1.1.
Proof of Theorem 1.1: Take a fixed $l \in \mathbb{N}$ at first. We only need to show this theorem in the case where $\xi=\kappa=1$, the more general case is then a fairly immediate consequence.

The proof will be divided into three parts, proving estimates (1), (2) and (3) respectively.
Part 1: First, we need to prove (1).
Set $\left(x_{m}, y_{m}\right) \in \pi_{V}\left(V_{\gamma_{m}}\right) \times\left(U \backslash \pi_{V}\left(V_{\sigma_{m}}\right)\right)$. Choosing vectors $\left.e_{x_{m}} \in \mathcal{L}^{m}\right|_{x_{m}}$ and $\left.e_{y_{m}} \in \mathcal{L}^{m}\right|_{y_{m}}$ such that $\left\|e_{x_{m}}\right\|_{h^{m}}=\left\|e_{y_{m}}\right\|_{h^{m}}=1$. Let $k_{1}, k_{2} \in \mathbb{Z}_{\geq 0}$ such that $k_{1}+k_{2} \leq k$. Consider the unit tangent
vectors $v_{1, m}, \cdots, v_{k_{1}, m} \in T_{x_{m}} M \oplus 0 \subset T_{\left(x_{m}, y_{m}\right)}(M \times M)$ and $v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m} \in 0 \oplus T_{y_{m}} M \subset$ $T_{\left(x_{m}, y_{m}\right)}(M \times M)$. Now we can define linear functionals on the space of holomorphic sections on small neighborhoods of $x_{m}$ and $y_{m}$ as following:
$$\begin{aligned}
\nabla^{k_{1}} S\left(v_{1, m}, \cdots, v_{k_{1}, m}\right) & =T_{1, m}(S) e_{x_{m}}, \\
\nabla^{* k_{2}} S^{*}\left(v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m}\right) & =\overline{T_{2, m}(S)} e_{y_{m}}^{*},
\end{aligned}$$
for any holomorphic section $S$ of $\mathcal{L}^{m}$ around $x_{m}$ and $y_{m}$, respectively. Then we have
$$\begin{aligned}
& \left\|\nabla_{x}^{k_{1}} \nabla_{y}^{* k_{2}} B_{\omega, m}\left(x_{m}, y_{m}\right)\left(v_{1, m}, \cdots, v_{k_{1}+k_{2}, m}\right)\right\|_{h^{m}, \omega} \\
= & \left\|\left.\left|\sum_{j} \nabla^{k_{1}} S_{j}\right|_{x_{m}}\left(v_{1, m}, \cdots, v_{k_{1}, m}\right) \otimes \nabla^{* k_{2}} S_{j}^{*}\right|_{y_{m}}\left(v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m}\right)\right\|_{h^{m}, \omega} \\
= & \left\|\left(\sum_{j} T_{1, m}\left(S_{j}\right) \overline{T_{2, m}\left(S_{j}\right)}\right) e_{x_{m}} \otimes e_{y_{m}}^{*}\right\|_{h^{m}}=\left|T_{1, m}\left(S_{T_{1, m}}\right) \overline{T_{2, m}\left(S_{T_{1, m}}\right)}\right|,
\end{aligned}$$
where $\|\cdot\|_{h^{m}, \omega}$ means the norms corresponding to the Hermitian metric $\pi_{1}^{*} h^{m} \otimes \pi_{2}^{*} h^{-m}$ and Kähler metric $\pi_{1}^{*} \omega+\pi_{2}^{*} \omega$ on $M \times M$, the family $\left\{S_{j}\right\}_{j \in J}$ is an $L^{2}$-orthonormal basis of $H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$, and $S_{T_{1, m}} \in H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$ is the peak section of the functional $T_{1, m}$ on $M$. Since $u=o(1)$ as $h_{D} \rightarrow 0^{+}$, we can find a constant $\epsilon^{\prime}>0$ depending only on $(M, \omega, \mathcal{L}, h)$ such that
$$\begin{aligned}
\min \left\{\operatorname{dist}_{\omega}\right. & \left(\pi_{V}\left(V_{\gamma_{m}}\right), M \backslash \pi_{V}\left(V_{\sqrt{\gamma_{m} \sigma_{m}}}\right)\right), \\
& \left.\operatorname{dist}_{\omega}\left(M \backslash \pi_{V}\left(V_{\sigma_{m}}\right), \pi_{V}\left(V_{\sqrt{\gamma_{m} \sigma_{m}}}\right)\right)\right\} \geq \epsilon^{\prime} \varepsilon_{m},
\end{aligned}$$
and Lemma 4.3 now shows that there exists a constant $\delta \in\left(0, \epsilon^{\prime}\right)$ depending only on $(M, \omega)$, such that $\operatorname{inj}\left(U \backslash \pi_{V}\left(V_{\gamma_{m}}\right)\right) \geq \delta \varepsilon_{m}$. By Corollary 4.2, we see that there exists a constant $C_{0}>0$ depending only on $(M, \omega, \mathcal{L}, h), k$ and $\beta$, such that
$$\begin{aligned}
\left|\log h_{D}\left(x_{m}\right)\right|^{2 \beta} & \left\|\left.T_{1, m}\right|_{H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)}\right\| \\
& \quad+\left|\log h_{D}\left(y_{m}\right)\right|^{2 \beta}\left\|\left.T_{2, m}\right|_{H_{L^{2}}^{0}\left(B_{\delta \varepsilon_{m}}\left(y_{m}\right), \mathcal{L}^{m}\right)}\right\| \leq C_{0} m^{C_{0}} .
\end{aligned}$$
By using Lemma 4.1 and Proposition 4.1 to $V_{\gamma_{m}}$ and $V_{\sqrt{\gamma_{m} \sigma_{m}}}$, we can conclude that for each integer $q \in \mathbb{N}$, there exists a constant $C_{1}>0$ depending only on $(M, \omega, \mathcal{L}, h), k$ and $q$, such that
$$\int_{M \backslash \pi_{V}\left(V_{\sqrt{\gamma_{m} \sigma_{m}}}\right)}\left\|S_{T_{1, m}}\right\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega} \leq C_{1} m^{-q}$$
Choosing $q=2 l+4+4\left\lfloor C_{0}\right\rfloor$, where $\lfloor\cdot\rfloor$ is the greatest integer function. It follows that
$$\begin{aligned}
\left|T_{1, m}\left(S_{T_{1, m}}\right) \overline{T_{2, m}\left(S_{T_{1, m}}\right)}\right| & \leq\left\|T_{1, m}\right\| \cdot\left\|\left.T_{2, m}\right|_{H_{L^{2}}^{0}\left(B_{\delta \varepsilon_{m}}\left(y_{m}\right), \mathcal{L}^{m}\right)}\right\| \cdot\left\|S_{T_{1, m}}\right\|_{L^{2}, B_{\delta \varepsilon_{m}}\left(y_{m}\right) ; h^{m}} \\
& \leq C_{0}^{2} C_{1} m^{2 C_{0}} m^{-l-2-2\left\lfloor C_{0}\right\rfloor}\left|\log h_{D}\left(x_{m}\right)\right|^{-\beta}\left|\log h_{D}\left(y_{m}\right)\right|^{-\beta} \\
& \leq C_{0}^{2} C_{1} m^{-l}\left|\log h_{D}\left(x_{m}\right)\right|^{-\beta}\left|\log h_{D}\left(y_{m}\right)\right|^{-\beta} .
\end{aligned}$$
Hence we can conclude that
$$\sup _{\pi_{V}\left(V_{\gamma_{m}}\right) \times\left(U \backslash \pi_{V}\left(V_{\sigma_{m}}\right)\right)}\left|\log h_{D}(x)\right|^{\beta}\left|\log h_{D}(y)\right|^{\beta}\left\|B_{\omega, m}(x, y)\right\|_{C^{k} ; h^{m}, \omega} \leq C_{2} m^{-l} .$$
where a constant $C_{2}>0$ depending only on $(M, \omega, \mathcal{L}, h), k, l$ and $\beta$. By exchanging $x_{m}$ and $y_{m}$, one can see that
$$\sup _{\left(U \backslash \pi_{V}\left(V_{\sigma_{m}}\right)\right) \times \pi_{V}\left(V_{\gamma_{m}}\right)}\left|\log h_{D}(x)\right|^{\beta}\left|\log h_{D}(y)\right|^{\beta}\left\|B_{\omega, m}(x, y)\right\|_{C^{k} ; h^{m}, \omega} \leq C_{2} m^{-l} .$$

Part 2. Our task now is to prove (2).
Set $\left(x_{m}, y_{m}\right) \in \pi_{V}\left(V_{\gamma_{m}}\right) \times \pi_{V}\left(V_{\gamma_{m}}\right)$. Let $\left.e_{x_{m}} \in \mathcal{L}^{m}\right|_{x_{m}}$ and $\left.e_{y_{m}} \in \mathcal{L}^{m}\right|_{y_{m}}$ such that $\left\|e_{x_{m}}\right\|_{h^{m}}=$ $\left\|e_{y_{m}}\right\|_{h^{m}}=1$. Choosing $k_{1}, k_{2} \in \mathbb{Z}_{\geq 0}$ such that $k_{1}+k_{2} \leq k$, unit tangent vectors $v_{1, m}, \cdots, v_{k_{1}, m} \in$ $T_{x_{m}} M \oplus 0 \subset T_{\left(x_{m}, y_{m}\right)}(M \times M)$, and unit tangent vectors $v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m} \in 0 \oplus T_{y_{m}} M \subset$ $T_{\left(x_{m}, y_{m}\right)}(M \times M)$. Now we can define a linear functional on $H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\gamma_{m}}\right), \mathcal{L}^{m}\right)$ as following:
$$\begin{aligned}
\nabla^{k_{1}} S\left(v_{1, m}, \cdots, v_{k_{1}, m}\right) & =T_{1, m}(S) e_{x_{m}}, \\
\nabla^{* k_{2}} S^{*}\left(v_{k_{1}+1, m}, \cdots, v_{k_{1}+k_{2}, m}\right) & =\overline{T_{2, m}(S)} e_{y_{m}}^{*},
\end{aligned}$$
for any $S \in H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\gamma_{m}}\right), \mathcal{L}^{m}\right)$. Let $S_{T_{i, m, \sigma_{m}}} \in H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$ and $S_{T_{i, m}} \in H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)$ denote the peak sections of the functional $T_{i, m}$ on $\pi_{V}\left(V_{\sigma_{m}}\right)$ and $M$, respectively. As in the argument in Part 1, a straightforward computation shows that
$$\begin{aligned}
& \left\|\nabla_{x}^{k_{1}} \nabla_{y}^{* k_{2}}\left(B_{\omega, m}\left(x_{m}, y_{m}\right)-B_{\omega, m, \sigma_{m}}\right)\left(x_{m}, y_{m}\right)\left(v_{1, m}, \cdots, v_{k_{1}+k_{2}, m}\right)\right\|_{h^{m}, \omega} \\
= & \left\|\left(T_{1, m}\left(S_{T_{1, m}}\right) \overline{T_{2, m}\left(S_{T_{1, m}}\right)}-T_{1, m}\left(S_{T_{1, m, \sigma_{m}}}\right) \overline{T_{2, m}\left(S_{T_{1, m, \sigma_{m}}}\right)}\right) e_{x_{m}} \otimes e_{y_{m}}^{*}\right\|_{h^{m}} \\
\leq & \left|T_{1, m}\left(S_{T_{1, m}}-S_{T_{1, m, \sigma_{m}}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m, \sigma_{m}}}\right)\right|+\left|T_{1, m}\left(S_{T_{1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}-S_{T_{1, m, \sigma_{m}}}\right)\right| .
\end{aligned}$$
By Corollary 4.2, we see that there exists a constant $C_{3}>0$ depending only on $(M, \omega, \mathcal{L}, h)$ and $k$, such that
$$\begin{aligned}
\left|\log h_{D}\left(x_{m}\right)\right|^{2 \beta} & \left\|\left.T_{1, m}\right|_{H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\sigma_{m}}\right), \mathcal{L}^{m}\right)}\right\| \\
& +\left|\log h_{D}\left(y_{m}\right)\right|^{2 \beta}\left\|\left.T_{2, m}\right|_{H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\sigma_{m}}\right), \mathcal{L}^{m}\right)}\right\| \leq C_{3} m^{C_{3}} .
\end{aligned}$$
Combining Lemma 4.1 and Proposition 4.1, we see that for each given integer $q \in \mathbb{N}$, there exists a constant $C_{4}>0$ depending only on $(M, \omega, \mathcal{L}, h), k$ and $q$, such that
$$\int_{\pi_{V}\left(V_{\sigma_{m}}\right)}\left\|S_{T_{1, m}}-S_{T_{1, m, \sigma_{m}}}\right\|^{2} d \operatorname{Vol}_{\omega} \leq C_{3} m^{-q}$$
Choosing $q=2 l+4+4\left\lfloor C_{2}\right\rfloor$, where $\lfloor\cdot\rfloor$ is the greatest integer function. Then we have
$$\begin{aligned}
& \left|T_{1, m}\left(S_{T_{1, m}}-S_{T_{1, m, \sigma_{m}}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m, \sigma_{m}}}\right)\right|+\left|T_{1, m}\left(S_{T_{1, m}}\right)\right| \cdot\left|T_{2, m}\left(S_{T_{1, m}}-S_{T_{1, m, \sigma_{m}}}\right)\right| \\
\leq & 2\left\|\left.T_{1, m}\right|_{H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\sigma_{m}}\right), \mathcal{L}^{m}\right)}\right\| \cdot\left\|\left.T_{2, m}\right|_{H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\sigma_{m}}\right), \mathcal{L}^{m}\right)}\right\| \cdot\left\|S_{T_{1, m}}-S_{T_{1, m, \sigma_{m}}}\right\|_{L^{2} ; V_{\sigma_{m}}} \\
\leq & 2 C_{2}^{2} C_{3} m^{2 C_{0}} m^{-l-2-2\left\lfloor C_{2}\right\rfloor}\left|\log h_{D}\left(x_{m}\right)\right|^{-\beta}\left|\log h_{D}\left(y_{m}\right)\right|^{-\beta} \\
\leq & 2 C_{2}^{2} C_{3} m^{-l}\left|\log h_{D}\left(x_{m}\right)\right|^{-\beta}\left|\log h_{D}\left(y_{m}\right)\right|^{-\beta} .
\end{aligned}$$
Then we can obtain the estimate (2), and the theorem follows.
Part 3. It remains to prove (3).
Let $x_{m} \in \pi_{V}\left(V_{\gamma_{m}}\right)$, and $\left.e_{x_{m}} \in \mathcal{L}^{m}\right|_{x_{m}}$ such that $\left\|e_{x_{m}}\right\|_{h^{m}}=1$. Then we can define a linear functional $T_{0, m}: H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\gamma_{m}}\right), \mathcal{L}^{m}\right) \rightarrow \mathbb{C}$ by $S\left(x_{m}\right)=T_{0, m}(S) e_{x_{m}}, \forall S \in H_{L^{2}}^{0}\left(\pi_{V}\left(V_{\gamma_{m}}\right), \mathcal{L}^{m}\right)$.

Then we have
$$\frac{\rho_{M, \omega, m}(x)}{\rho_{V_{\sigma_{m}} / \Gamma_{V}, \omega, m}(x)}=\frac{\left\|\left.T_{0, m}\right|_{H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)}\right\|}{\left\|\left.T_{0, m}\right|_{H_{L^{2}}^{0}\left(V_{\sigma_{m}} / \Gamma_{V}, \omega, \mathcal{L}^{m}, h^{m}\right)}\right\|},$$
and (3) follows from Proposition 4.1. \(\square\)

\subsection*{4.4. Peak sections on Poincaré type cusps.}

Now we consider the peak sections on Poincaré type cusps. This subsection is an analogy of the previous subsection on Poincaré type cusp. Let $\bar{M}$ be a compact Kähler manifold, $D$ be a simple normal crossing divisor, and $(M, \omega)=(\bar{M} \backslash D, \omega)$ be a complete Kähler manifold with Poincaré type cusp along $D$. Fix a Riemannian metric $\bar{g}$ on $\bar{M}$. Write $\bar{d}(x)=\operatorname{dist}_{\bar{g}}(x, D), \forall x \in M$. Assume that $(M, \omega)$ is a complete Kähler manifold with $\operatorname{Ric}(\omega) \geq-\Lambda \omega$ and $(\mathcal{L}, h)$ is a Hermitian line bundle with $\operatorname{Ric}(h) \geq \epsilon \omega$, where $\epsilon, \Lambda>0$ are constants.

The proof of the following estimate of the injectivity radius on $M$ is similar to that of Lemma 4.3, so we omit it.

Lemma 4.7. Given an integer $k \in \mathbb{N}$. Then there exists a constant $C=C(k, M, \omega)>0$ such that the curvature $\sum_{j=0}^{5 k+10 n}\left\|\nabla^{j} \operatorname{Ric}(\omega)\right\|_{\omega} \leq C$ on $M$, and for any $x \in M$, the injectivity radius $\operatorname{inj}_{M}(x) \geq C^{-1}(|\log \bar{d}(x)|+1)^{-1}$.

Choosing $x \in D$. By definition, we can find a neighborhooda $U_{x}$ of $x$ and a biholomorphic map
$$\varphi_{x}: U_{x} \backslash D \rightarrow \prod_{i=1}^{k_{x}} \mathbb{D}_{r_{x, i}}^{*} \times B_{r_{x, k_{x}, n}}^{2 n-2 k_{x}}(0) \subset\left(\mathbb{D}_{1}^{*}\right)^{k_{x}} \times \mathbb{C}^{n-k_{x}},$$
such that $\left(\varphi_{x}^{-1}\right)^{*} \omega=-\sqrt{-1} \sum_{i=1}^{k_{x}} \partial \bar{\partial} \log \left(\log \left|z_{i}\right|^{2}\right)+\pi_{k_{x}, n}^{*} \omega_{x, k_{x}, n}+\sqrt{-1} \partial \bar{\partial} u_{x}$, where $r_{x, j}, r_{x, k_{x}, n}$ are positive constants, $\omega_{x, k_{x}, n}$ is a Kähler metric on $B_{r_{x, k_{x}, n}}^{2 n-2 k_{x}}(0), u_{x}$ is a smooth function on $U_{x} \backslash D$, and there exists a constant $\alpha>0$ such that $u_{x} \circ \varphi_{x}^{-1} \in \cap_{i=1}^{k_{x}} O\left(|\log | z_{i}| |^{-\alpha}\right)$ as $\inf _{1 \leq i \leq k_{x}}\left|z_{j, i}\right| \rightarrow 0^{+}$ to all orders with respect to $\omega_{\text {mod }}$ on $\prod_{i=1}^{k_{x}} \mathbb{D}_{r_{x, i}}^{*} \times B_{r_{x, k_{x}, n}}^{2 n-2 k_{x}}(0)$.

Let us denote by $U_{x, t, s}$ the domain $\left(\mathbb{D}_{t}^{*}\right)^{k_{x}} \times B_{s}^{2 n-2 k_{x}}(0)$ for any constants $t, s \in(0,1)$. It will cause no confusion if we use the same letter to designate a subset of $U_{x} \backslash D$ and its image under $\varphi_{x}$. Now we can construct quasi-plurisubharmonic functions on $U_{x} \backslash D$. This is an analogy of Lemma 4.4 on Poincarè type cusp.
Lemma 4.8. Let $\beta, \delta, \epsilon>0$ be constants. Assume that $\delta<e^{-2} n^{-2} r_{x, j}, j=1, \cdots, k_{x}$, and $\epsilon \leq e^{-2} n^{-2} r_{x, n}$. Then for any $p \in U_{x, \delta^{1+2 \beta}, \epsilon}$, there exists a quasi-plurisubharmonic function $\psi \in$ $L^{1}(M, \omega) \cap C^{\infty}(M \backslash\{p\})$ such that $\psi \leq 0, \operatorname{supp} \psi \subset U_{x, \delta, 4 \epsilon}, \sqrt{-1} \partial \bar{\partial} \psi \geq-C\left(|\log \delta|+\epsilon^{-2}\right) \omega$ and $\lim _{y \rightarrow p}\left(\psi(y)-\log \left(\operatorname{dist}_{\omega}(p, y)\right)\right)=-\infty$, where $C>0$ is a constant dependent only on $(M, \omega)$, and $\beta$.
Proof. Fix a point $p=\left(p_{1}, \cdots, p_{n}\right) \in\left(\mathbb{D}_{\delta^{1+2 \beta}}^{*}\right)^{k_{x}} \times B_{\epsilon}^{2 n-2 k_{x}}(0)=U_{x, \delta^{1+2 \beta}, \epsilon}$. Let
$$f(y)=\sum_{i=1}^{k_{x}} \delta^{-2}\left|y_{i}-p_{i}\right|^{2}+\sum_{i=k_{x}+1}^{n} \epsilon^{-2}\left|y_{i}-p_{i}\right|^{2}, \quad \forall y=\left(y_{1}, \cdots, y_{n}\right) \in U_{x} .$$
It is easy to see that $f(y) \geq \min \left\{\delta^{2 \beta}, e^{-2}\right\}, \forall y \in U_{x} \backslash U_{x, \delta^{1+\beta}, 2 \epsilon}$, and $f(y) \leq 16 n, \forall y \in U_{x, \delta, 4 \epsilon}$.

Since $u=o(1)$, we can conclude that $|\nabla \log f(x)| \leq C_{1}\left(|\log \delta|+\epsilon^{-1}\right), \forall x \in U_{x, \delta, 4 \epsilon} \backslash U_{x, \delta^{1+\beta}, 2 \epsilon}$, where $C_{1}$ is a constant depending only on $(M, \omega)$ and $\beta$.

Now we consider the model metric $\omega_{\text {mod }}=-\left.\sum_{i=1}^{k_{x}} \partial \bar{\partial} \log |\log | z_{i}\right|^{2} \mid$ on $\left(\mathbb{D}_{\delta}^{*}\right)^{k_{x}}$. By a straightforward calculation, we see that $\operatorname{dist}_{\omega_{\text {mod }}}\left(\left(\mathbb{D}_{\delta^{1+\beta}}^{*}\right)^{k_{x}},\left(\mathbb{D}_{1}^{*}\right)^{k_{x}} \backslash\left(\mathbb{D}_{\delta}^{*}\right)^{k_{x}}\right) \geq C_{2}^{-1} \log (1+\beta)$ for some constant $C_{2}$ depending only on $(M, \omega)$. Then we can choose a cut-off function $\eta_{1} \in C^{\infty}\left(\left(\mathbb{D}_{1}^{*}\right)^{k_{x}}\right)$ such that $\eta_{1}=1$ on $\left(\mathbb{D}_{\delta^{1+\beta}}^{*}\right)^{k_{x}}, \eta_{1}=0$ on $\left(\mathbb{D}_{1}^{*}\right)^{k_{x}} \backslash\left(\mathbb{D}_{\delta}^{*}\right)^{k_{x}}, 0 \leq \eta_{1} \leq 1$, and $\sum_{i=0}^{2}\left\|\nabla^{i} \eta_{1}\right\|_{\omega_{\text {mod }}} \leq C_{3}$, where $C_{3}>0$ is a constant depending only on $n$ and $\beta$. Choosing another cut-off function $\eta_{2} \in C_{0}^{\infty}\left(B_{4 \epsilon}^{2 n-2 k_{x}}(0)\right)$ such that $\eta_{2}=1$ on $B_{2 \epsilon}^{2 n-2 k_{x}}(0), 0 \leq \eta_{2} \leq 1$, and $\sum_{i=0}^{2} \epsilon^{i}\left\|\nabla^{i} \eta_{2}\right\|_{\omega_{E u c}} \leq C_{4}$, where $C_{4}$ is a constant depending only on $n$. By the biholomorphic map $\varphi_{x}$, we see that $\eta_{1}$ and $\eta_{2}$ can be viewed as functions on $U_{x}$.

Let $M=\sup _{U_{x, \delta, 4 \epsilon}} f$, and $\psi(x)=\eta_{1}(x) \eta_{2}(x)(\log f(x)-\log M)$. Analysis similar to that in the proof of Lemma 4.4 shows that $\varphi_{x}$ satisfies the properties we need. \(\square\)

We will denote by $W_{r}$ the domain $\{x \in M \mid \bar{d}(x, D)<r\} \subset M=\bar{M} \backslash D$. Now we consider the peak sections around Poincaré type cusps. To apply Lemma 4.8 to points around $D$, we need the following decomposition result for the manifold $(M, \omega)$. For abbreviation, we denote $e^{-\frac{\sqrt{m}}{\log m}}$ and $\frac{\log m}{\sqrt{m}}$ briefly by $r_{m}$ and $\varepsilon_{m}$, respectively, for any $m \geq 2$.

Lemma 4.9. There are constants $m_{0}, b_{1}, b_{2}, b_{3}, C_{1}, C_{2}>0$, and a decreasing sequence $\left\{\xi_{m}\right\}_{m=1}^{\infty}$ that converges to 0 as $m \rightarrow \infty$ satisfying the following property.

Let $m>m_{0}$ be a constant. Then there are points $y_{i, m} \in D, i=1, \cdots, N_{m}$, positive constants $C_{1, i, m} \leq C_{1}, C_{2, i, m} \leq C_{2}$, open neighborhoods $U_{i, m}$ of $y_{i, m}$ in $\bar{M}$ and biholomorphic maps
$$\varphi_{i, m}: U_{i, m} \backslash D \rightarrow\left(\mathbb{D}_{r_{m}^{b_{1}}}^{*}\right)^{k_{i, m}} \times B_{b_{2} \varepsilon_{m}}^{2 n-2 k_{x}}(0)$$
such that $U_{i, m} \backslash D \subset W_{r_{m}}, W_{r_{m}^{b_{3}}} \subset \cup_{i=1}^{N_{m}} \varphi_{i, m}^{-1}\left(\left(\mathbb{D}_{r_{m}^{C_{1, i, m} b_{1}}}^{*}\right)^{k_{i, m}} \times B_{\frac{b_{2} \varepsilon_{m}}{C_{2, i, m}}}^{2 n-2 k_{x}}(0)\right)$, and the Kähler metrics $\left(\varphi_{i, m}^{-1}\right)^{*} \omega=\omega_{\bmod , k_{i, m}, n}+\sqrt{-1} \partial \bar{\partial} u_{i, m}$ on $U_{i, m} \backslash D$ for some real valued function $u_{i, m}$ satisfying that $\left\|u_{i, m}\right\|_{C^{2} ; \omega} \leq \xi_{m}$ on $U_{i, m} \backslash D, i=1, \cdots, N_{m}$.

Proof. By the compactness of the divisor $D \subset \bar{M}$, we can find points $\widetilde{y}_{j} \in D, j=1, \cdots, N$, open neighborhoods $\widetilde{U}_{j}$ of $\widetilde{y}_{j}$ in $\bar{M}$, and biholomorphic maps
$$\varphi_{j}=\left(z_{j, 1} \cdots, z_{j, n}\right): \widetilde{U}_{j} \rightarrow\left(\mathbb{D}_{\epsilon_{j}}\right)^{k_{j}} \times B_{\epsilon_{j}}^{2 n-2 k_{j}}(0)$$
such that $\varphi_{j}\left(\widetilde{y}_{j}\right)=0, \varphi_{j}\left(\widetilde{U}_{j} \backslash D\right)=\left(\mathbb{D}_{\epsilon_{j}}^{*}\right)^{k_{j}} \times B_{\epsilon_{j}}^{2 n-2 k_{j}}(0), D \subset \cup_{j=1}^{N} \varphi_{j}^{-1}\left(\left(\mathbb{D}_{\epsilon_{j}^{2}}\right)^{k_{j}} \times B_{\frac{\epsilon_{j}}{2}}^{2 n-2 k_{j}}(0)\right)$, and $\left(\varphi_{j}^{-1}\right)^{*} \omega=-\sqrt{-1} \sum_{i=1}^{k_{j}} \partial \bar{\partial} \log \left(\log \left|z_{i}\right|^{2}\right)+\pi_{k_{j}, n}^{*} \omega_{j}+\sqrt{-1} \partial \bar{\partial} u_{j}$, where $\pi_{i}$ is the projection of $\mathbb{C}^{n}$ onto the $i$-th component, $\epsilon_{j}>0$ are constants, $\omega_{j}$ is a Kähler metric on $B_{\epsilon_{j}}^{2 n-2 k_{j}}(0)$, and $u_{j}=o(1)$ as $\inf _{1 \leq i \leq k_{x}}\left|z_{j, i}\right| \rightarrow 0^{+}$to all orders with respect to $\omega$.

Fix $j \in\{1, \cdots, N\}$. It is sufficient to construct the open subsets and biholomorphic maps on $\widetilde{U}_{j}$. Without loss of generality, we can assume that $\omega=\varphi_{j}^{*} \omega_{\text {mod }}$. For each nonnegative integer $q \leq k_{j}$,
we consider the set
$$Z_{q}=\bigcup_{\left\{i_{1}, \cdots, i_{q}\right\} \subset\left\{1, \cdots, k_{j}\right\}}\left(\bigcap_{l=1}^{q}\left\{z_{j, i_{l}}=0\right\} \bigcup_{l \in\left\{1, \cdots, k_{j}\right\} \backslash\left\{i_{1}, \cdots, i_{q}\right\}}\left\{z_{j, l}=0\right\}\right) \subset \widetilde{U}_{j} .$$
Then we have $\cup_{q=0}^{k_{j}} Z_{q}=\widetilde{U}_{j} \cap D$, and $Z_{q} \cap Z_{q^{\prime}}=$ for each $q \neq q^{\prime}$.
By Lemma 4.7, we can find a constant $\delta>0$ such that for any point $z \in \mathbb{D}_{1}^{*}$, there exist an open neighborhood $U_{z}$ of $z$ in $\mathbb{D}_{1}^{*}$, an increasing function $\varrho(t)$ on ( 0,1 ), and a biholomorphic map $\phi_{z}: U_{z} \rightarrow \mathbb{D}_{\delta|\log | z| |^{-1}}$ such that $\phi_{z}(z)=0, \lim _{t \rightarrow 0^{+}} \varrho(t)=0$, and $\omega_{\text {mod,1,1 }}-\phi_{z}^{*} \omega_{E u c}=\sqrt{-1} \partial \bar{\partial} u_{U_{z}}$ for some function $u_{U_{z}}$ satisfying that $\left\|u_{U_{z}}\right\|_{C^{2} ; \omega_{1,1}} \leq \varrho(|z|)$ on $U_{z}$, where $\omega_{E u c}$ is the Euclidean Kähler form on $\mathbb{C}^{n}$.

Choosing $y \in Z_{q} \cap \varphi_{j}^{-1}\left(\left(\mathbb{D}_{\epsilon_{j}^{2}}\right)^{k_{j}} \times B_{\frac{\epsilon_{j}}{2}}^{2 n-2 k_{j}}(0)\right)$. Without loss of generality, we can assume that $y \in \cap_{l=1}^{q}\left\{z_{j, l}=0\right\}$. Let $t \leq n^{-2} e^{-2} \epsilon_{j}^{2}$ be a positive constant. When $y \notin B_{t}^{E u c, n}\left(\cup_{k=p+1}^{n} Z_{k}\right)$, then we can find an increasing function $\widetilde{\varrho}(t)$ on ( 0,1 ), an open neighborhood $\widetilde{U}_{y, t}$ of $y$ in $\widetilde{U}_{j}$ and a biholomorphic map
$$\widetilde{\phi}_{y, t}=\left(z_{y, t, 1}, \cdots, z_{y, t, n}\right): \widetilde{U}_{y, t} \rightarrow\left(\mathbb{D}_{\delta t}\right)^{p} \times B_{\delta|\log t|^{-1}}^{2 n-2 p}$$
such that $\lim _{t \rightarrow 0^{+}} \widetilde{\varrho}(t)=0, \widetilde{\phi}_{y, t}(y)=0, \widetilde{U}_{y, t} \backslash D=\cup_{l=1}^{p}\left\{z_{y, t, l}=0\right\}$, and $\widetilde{\phi}_{y, t}^{*} \omega_{\bmod }-\omega=\sqrt{-1} \partial \bar{\partial} u_{\widetilde{U}_{y, t}}$ for some function $u_{\widetilde{U}_{y, t}}$ satisfying that $\left\|u_{\widetilde{U}_{y, t}}\right\|_{C^{2} ; \omega} \leq \varrho(t)$ on $U_{y, t}$, where $B_{t}^{\text {Euc, } n}(x)$ is the Euclidean ball in $\mathbb{C}^{n}$ with radius $t$ and center $x \in \mathbb{C}^{n}$, and $B_{t}^{\text {Euc, } n}(A)=\cup_{x \in A} B_{t}^{\text {Euc,n }}(x)$.