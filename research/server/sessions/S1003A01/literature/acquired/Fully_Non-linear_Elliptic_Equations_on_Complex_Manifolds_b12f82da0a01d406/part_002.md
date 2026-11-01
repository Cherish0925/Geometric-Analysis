---
retention_scope: session
part: 2
total_parts: 3
---

[Part 2/3 of: Fully Non-linear Elliptic Equations on Complex Manifolds]

Proposition 7.2. Assume (1.3), (1.4) and (1.5) hold. Suppose that Dirichlet problem (1.7) admits an admissible subsolution $\underline{u} \in C^{2}(\bar{M})$. Then for any admissible solution $u \in C^{3}(M) \cap C^{2}(\bar{M})$ to the Dirichlet problem, we have
$$\left|g_{\alpha \bar{n}}\left(z_{0}\right)\right| \leqslant C\left(1+\sup _{M}|\nabla u|\right) \text { for any } z_{0} \in \partial M \text {, }$$
where $C$ a positive constant depending on $|\varphi|_{C^{3}(\bar{M})},|\psi|_{C^{1}(M)},|\nabla u|_{C^{0}(\partial M)},|\underline{u}|_{C^{2}(\bar{M})}$, $\partial M$ up to third derivatives and other known data (but neither on $\left(\delta_{\psi, f}\right)^{-1}$ nor on $\left.\sup _{M}|\nabla u|\right)$.
7.1. $C^{0}$-estimate and boundary gradient estimate. Now we derive $C^{0}$-estimate, and boundary gradient estimates. Let $\check{u}$ be the solution to
$$\Delta \check{u}+\operatorname{tr}_{\omega}(\chi)=0 \text { in } M, \quad \check{u}=\varphi \text { on } \partial M .$$
The existence of $\check{u}$ follows from standard theory of elliptic equations of second order. Such $\check{u}$ is a supersolution of (1.7). By the maximum principle one derives
$$\underline{u} \leqslant u \leqslant \check{u} \text { in } M,$$
$$\underline{u}_{x^{n}}(0) \leqslant u_{x^{n}}(0) \leqslant \check{u}_{x^{n}}(0), u_{\beta}(0)=\underline{u}_{\beta}(0), 1 \leqslant \beta \leqslant n-1 .$$
This simply gives the following lemma.
Lemma 7.3. There is a uniform positive constant $C$ such that
$$\sup _{M}|u|+\sup _{\partial M}|\nabla u| \leqslant C .$$
7.2. A key lemma. The boundary value condition yields
$$u_{\alpha \bar{\beta}}(0)=\underline{u}_{\alpha \bar{\beta}}(0)+(u-\underline{u})_{x^{n}}(0) \sigma_{\alpha \bar{\beta}}(0) .$$
At $z_{0} \in \partial M(z=0)$, by (7.11) we have
$$\mathfrak{g}_{\alpha \bar{\beta}}=(1-t) \underline{\mathfrak{g}}_{\alpha \bar{\beta}}+\left\{t \underline{\underline{g}}_{\alpha \bar{\beta}}+(u-\underline{u})_{x^{n}} \sigma_{\alpha \bar{\beta}}\right\} .$$
For simplicity, denote
$$A_{t}=\sqrt{-1}\left[\operatorname{t} \underline{\underline{g}}_{\alpha \bar{\beta}}+(u-\underline{u})_{x^{n}} \sigma_{\alpha \bar{\beta}}\right] d z^{\alpha} \wedge d \bar{z}^{\beta} .$$
Clearly, $\left(A_{1}\right)_{\alpha \bar{\beta}}=\mathfrak{g}_{\alpha \bar{\beta}}$. Let $t_{0}$ be the first $t$ as we decrease $t$ from 1 such that
$$\lambda_{\omega^{\prime}}\left(A_{t_{0}}\right) \in \partial \Gamma_{\infty}$$
at $z_{0}$, where $\partial \Gamma_{\infty}$ is the boundary of $\Gamma_{\infty}$, as above
$$\Gamma_{\infty}=\left\{\left(\lambda_{1}, \cdots, \lambda_{n-1}\right):\left(\lambda_{1}, \cdots, \lambda_{n-1}, R\right) \in \Gamma \text { for some } R>0\right\} .$$
Henceforth, $\lambda_{\omega^{\prime}}\left(\chi^{\prime}\right)$ denotes the eigenvalues of $\chi^{\prime}$ with respect to $\omega^{\prime}=\sqrt{-1} g_{\alpha \bar{\beta}} d z^{\alpha} \wedge$ $d \bar{z}^{\beta}$. (Note that $g_{\alpha \bar{\beta}}(0)=\delta_{\alpha \beta}$ under the coordinate (7.2)). Such $t_{0}$ exists, since $\lambda_{\omega^{\prime}}\left(A_{1}\right) \in \Gamma_{\infty}$ and $\lambda_{\omega^{\prime}}\left(A_{t}\right) \in \mathbb{R}^{n-1} \backslash \Gamma_{\infty}$ for $t \ll-1$. Furthermore,
$$-T_{0}<t_{0}<1$$
for some uniform positive constant $T_{0}$ under control. Denote
$$\begin{aligned}
& \underline{\lambda}^{\prime}=\left(\underline{\lambda}_{1}^{\prime}, \cdots, \underline{\lambda}_{n-1}^{\prime}\right) \equiv \lambda_{\omega^{\prime}}\left(\underline{g}_{\alpha \bar{\beta}}\right), \\
& \tilde{\lambda}^{\prime}=\left(\tilde{\lambda}_{1}^{\prime}, \cdots, \tilde{\lambda}_{n-1}^{\prime}\right) \equiv \lambda_{\omega^{\prime}}\left(A_{t_{0}}\right) .
\end{aligned}$$

To complete the proof of Proposition 7.1, it requires to prove the following lemma.

Lemma 7.4. Let $t_{0}$ be as defined in (7.14). There is a uniform positive constant $C$ depending on $|u|_{C^{0}(M)},|\nabla u|_{C^{0}(\partial M)},|\underline{u}|_{C^{2}(M)}$, $\sup _{M} \psi,\left(\delta_{\psi, f}\right)^{-1}, \partial M$ up to third derivatives and other known data, such that
$$\left(1-t_{0}\right)^{-1} \leqslant C .$$
7.3. Proof of Lemma 7.4. The proof is based on some idea of Caffarelli-Nirenberg-Spruck [7]. We assume that $\Gamma$ is of type 1. Then $\Gamma_{\infty}$ is a symmetric convex cone as noted in [7]. (The type 2 cone case is much more simpler since $\Gamma_{\infty}=\mathbb{R}^{n-1}$ ).

We follow closely [40]. For simplicity, we set
$$\eta=(u-\underline{u})_{x^{n}}(0) .$$
From (7.9), we know $\eta \geqslant 0$. Without loss of generality, we assume
$$t_{0}>\frac{1}{2} \text { and } \tilde{\lambda}_{1}^{\prime} \leqslant \cdots \leqslant \tilde{\lambda}_{n-1}^{\prime} .$$

It was proved in [7, Lemma 6.1] that for $\tilde{\lambda}^{\prime} \in \partial \Gamma_{\infty}$ there is a supporting plane for $\Gamma_{\infty}$ and one can choose $\mu_{j}$ with $\mu_{1} \geqslant \cdots \geqslant \mu_{n-1} \geqslant 0$ so that
$$\Gamma_{\infty} \subset\left\{\lambda^{\prime} \in \mathbb{R}^{n-1}: \sum_{\alpha=1}^{n-1} \mu_{\alpha} \lambda_{\alpha}^{\prime}>0\right\}, \quad \sum_{\alpha=1}^{n-1} \mu_{\alpha}=1, \sum_{\alpha=1}^{n-1} \mu_{\alpha} \tilde{\lambda}_{\alpha}^{\prime}=0 .$$

Since $\underline{u}$ is an admissible function, there is $\varepsilon_{0}>0$ small such that
$$\underline{\lambda}-\varepsilon_{0} \overrightarrow{\mathbf{1}} \in \Gamma .$$
Then we know that
$$\sum_{\alpha=1}^{n-1} \mu_{\alpha} \underline{\lambda}_{\alpha}^{\prime} \geqslant \varepsilon_{0}>0 .$$
Combining [7, Lemma 6.2] (without loss of generality, assume $\underline{\lambda}_{1}^{\prime} \leqslant \cdots \leqslant \underline{\lambda}_{n-1}^{\prime}$ ),
$$\sum_{\alpha=1}^{n-1} \mu_{\alpha} \underline{\mathfrak{g}}_{\alpha \bar{\alpha}} \geqslant \sum_{\alpha=1}^{n-1} \mu_{\alpha} \underline{\lambda}_{\alpha}^{\prime} \geqslant \varepsilon_{0} .$$
Without loss of generality, we may assume $\left(A_{t_{0}}\right)_{\alpha \bar{\beta}}=t_{0} \underline{\mathfrak{g}}_{\alpha \bar{\beta}}+\eta \sigma_{\alpha \bar{\beta}}$ is diagonal at the origin $z_{0}(z=0)$. From (7.19) one has at the origin
$$0=t_{0} \sum_{\alpha=1}^{n-1} \mu_{\alpha} \underline{\mathfrak{g}}_{\alpha \bar{\alpha}}+\eta \sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}} \geqslant \varepsilon_{0} t_{0}+\eta \sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}}>\frac{\varepsilon_{0}}{2}+\eta \sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}} .$$
Together with (7.9), we see that $\eta>0$ and
$$-\sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}} \geqslant \frac{\varepsilon_{0}}{2 \sup _{\partial M}|\nabla(\check{u}-\underline{u})|}=: a_{1}>0,$$
where $\check{u}$ and $\underline{u}$ are respectively supersolution and subsolution.
On $\Omega_{\delta}=M \cap B_{\delta}(0)$, we take
$$d(z)=\sigma(z)+\tau|z|^{2}$$
where $\tau$ is a positive constant to be determined. Let
$$w(z)=\underline{u}(z)+\left(\eta / t_{0}\right) \sigma(z)+l(z) \sigma(z)+A d(z)^{2},$$
where $l(z)=\sum_{i=1}^{n}\left(l_{i} z^{i}+\bar{l}_{i} \bar{z}^{i}\right), l_{i} \in \mathbb{C}, \bar{l}_{i}=l_{\bar{i}}$, to be chosen as in (7.29), and $A$ is a positive constant to be determined. As above $\eta=(u-\underline{u})_{x^{n}}(0)$. Furthermore, on $\partial M \cap \bar{\Omega}_{\delta}, u(z)-w(z)=-A \tau^{2}|z|^{4}$. On $M \cap \partial B_{\delta}(0)$,
$$u(z)-w(z) \leqslant-\left(2 A \tau \delta^{2}+\frac{\eta}{t_{0}}-2 n \sup _{i}\left|l_{i}\right| \delta\right) \sigma(z)-A \tau^{2} \delta^{4} \leqslant-\frac{A \tau^{2} \delta^{4}}{2}$$
provided $A \gg 1$.
Let $T_{1}(z), \cdots, T_{n-1}(z)$ be an orthonormal basis for holomorphic tangent space of level hypersurface $\{w: d(w)=d(z)\}$ at $z$, so that for each $1 \leqslant \alpha \leqslant n-1, T_{\alpha}$ is of $C^{1}$ class and $T_{\alpha}(0)=\frac{\partial}{\partial z^{\alpha}}$. Such a basis exists and the holomorphic tangent space can be characterized as $\left\{\xi=\xi^{i} \frac{\partial}{\partial z^{i}}:\left(\sigma_{i}+\tau \bar{z}^{i}\right) \xi^{i}=0\right\}$, see e.g. [15].

By [7, Lemma 6.2], we have the following lemma.
Lemma 7.5. Let $T_{1}(z), \cdots, T_{n-1}(z)$ be as above, and let $T_{n}=\frac{\partial d}{|\partial d|}$. For a real $(1,1)$-form $\Theta=\sqrt{-1} \Theta_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j}$, we denote by $\lambda\left(\omega^{-1} \Theta\right)=\left(\lambda_{1}(\Theta), \cdots, \lambda_{n}(\Theta)\right)$ with $\lambda_{1}(\Theta) \leqslant \cdots \leqslant \lambda_{n}(\Theta)$. Then for any $\mu_{1} \geqslant \cdots \geqslant \mu_{n}$,
$$\sum_{i=1}^{n} \mu_{i} \lambda_{i}(\Theta) \leqslant \sum_{i=1}^{n} \mu_{i} \Theta\left(T_{i}, J \bar{T}_{i}\right) .$$
Here $J$ is the complex structure.
Let $\mu_{1}, \cdots, \mu_{n-1}$ be as in (7.19), and we set $\mu_{n}=0$. Let's denote $T_{\alpha}=\sum_{k=1}^{n} T_{\alpha}^{k} \frac{\partial}{\partial z^{k}}$. For $\Theta=\sqrt{-1} \Theta_{i \bar{j}} d z^{i} \wedge d \bar{z}^{j}$, define
$$\Lambda_{\mu}(\Theta) \equiv \sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j} \Theta_{i \bar{j}} .$$

Lemma 7.6. Let $w$ be as in (7.26). There are parameters $\tau, A, l_{i}, \delta$ depending only on $|u|_{C^{0}(M)},|\nabla u|_{C^{0}(\partial M)},|\underline{u}|_{C^{2}(M)}, \partial M$ up to third derivatives and other known data, such that
$$\Lambda_{\mu}(\mathfrak{g}[w]) \leqslant 0 \text { in } \Omega_{\delta}, u \leqslant w \text { on } \partial \Omega_{\delta} .$$
Proof. By direct computation
$$\begin{aligned}
\Lambda_{\mu}(\mathfrak{g}[w])= & \sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}\left(\chi_{i \bar{j}}+\underline{u}_{i \bar{j}}+\frac{\eta}{t_{0}} \sigma_{i \bar{j}}\right)+2 A d(z) \sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j} d_{i \bar{j}} \\
& +\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}\left(l(z) \sigma_{i \bar{j}}+l_{i} \sigma_{\bar{j}}+\sigma_{i} l_{\bar{j}}\right) .
\end{aligned}$$
Here we use $T_{\alpha} d=0$ for $1 \leqslant \alpha \leqslant n-1$.
Next, we plan to estimate the quantity $\Lambda_{\mu}(\mathfrak{g}[w])$ in $\Omega_{\delta}$.
\begin{itemize}
\item[-] At the origin $(z=0), T_{\alpha}^{i}=\delta_{\alpha i}$,
$$\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}\left(\chi_{i \bar{j}}+\underline{u}_{i \bar{j}}+\frac{\eta}{t_{0}} \sigma_{i \bar{j}}\right)(0)=\frac{1}{t_{0}} \sum_{\alpha=1}^{n-1} \mu_{\alpha}\left(A_{t_{0}}\right)_{\alpha \bar{\alpha}}=0 .$$
\end{itemize}
\begin{itemize}
\item[] So there are complex constants $k_{i}$ such that
$$\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}\left(\chi_{i \bar{j}}+\underline{u}_{i \bar{j}}+\frac{\eta}{t_{0}} \sigma_{i \bar{j}}\right)(z)=\sum_{i=1}^{n}\left(k_{i} z^{i}+\bar{k}_{i} \bar{z}^{i}\right)+O\left(|z|^{2}\right) .$$
\item[-] Note that
$$\begin{gathered}
\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}(z)=\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}(0)+O(|z|)=\sum_{\alpha=1}^{n-1} \mu_{\alpha} \delta_{\alpha i} \delta_{\alpha j}+O(|z|), \\
\sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}}(z)=\sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}}(0)+O(|z|) .
\end{gathered}$$
Combining with (7.24), one can pick $\delta, \tau$ sufficiently small such that
$$\begin{aligned}
\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j} d_{i \bar{j}} & =\sum_{\alpha=1}^{n-1} \mu_{\alpha}\left(\sigma_{\alpha \bar{\alpha}}(z)+\tau\right)+\sum_{\alpha=1}^{n-1} \mu_{\alpha}\left(T_{\alpha}^{i} \bar{T}_{\alpha}^{j}(z)-T_{\alpha}^{i} \bar{T}_{\alpha}^{j}(0)\right) d_{i \bar{j}} \\
& \leqslant-a_{1}+\tau+O(|z|) \leqslant-\frac{a_{1}}{4} .
\end{aligned}$$
Consequently, we get
$$2 A d(z) \sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j} d_{i \bar{j}} \leqslant-\frac{a_{1} A}{2} d(z) .$$
\item[-] From $\sum_{i=1}^{n} T_{\alpha}^{i} \sigma_{i}=-\tau \sum_{i=1}^{n} T_{\alpha}^{i} \bar{z}^{i}$ we have
$$\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}\left(l_{i} \sigma_{\bar{j}}+\sigma_{i} l_{\bar{j}}\right)=-\tau \sum_{\alpha=1}^{n-1} \mu_{\alpha}\left(\bar{l}_{\alpha} \bar{z}^{\alpha}+l_{\alpha} z^{\alpha}\right)+O\left(|z|^{2}\right) .$$
On the other hand, by (7.27),
$$l(z) \sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j} \sigma_{i \bar{j}}=l(z) \sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}}(0)+O\left(|z|^{2}\right) .$$
Thus
$$\begin{aligned}
& l(z) \sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j} \sigma_{i \bar{j}}+\sum_{\alpha=1}^{n-1} \mu_{\alpha} T_{\alpha}^{i} \bar{T}_{\alpha}^{j}\left(l_{i} \sigma_{\bar{j}}+\sigma_{i} l_{\bar{j}}\right) \\
= & l(z) \sum_{\alpha=1}^{n-1} \mu_{\alpha} \sigma_{\alpha \bar{\alpha}}(0)-\tau \sum_{\alpha=1}^{n-1} \mu_{\alpha}\left(z^{\alpha} l_{\alpha}+\bar{z}^{\alpha} \bar{l}_{\alpha}\right)+O\left(|z|^{2}\right) .
\end{aligned}$$
\end{itemize}
Putting these together,
$$\begin{aligned}
\Lambda_{\mu}(\mathfrak{g}[w]) \leqslant & \sum_{\alpha=1}^{n-1} 2 \operatorname{Re}\left\{z^{\alpha}\left(k_{\alpha}-\tau \mu_{\alpha} l_{\alpha}+l_{\alpha} \sum_{\beta=1}^{n-1} \mu_{\beta} \sigma_{\beta \bar{\beta}}(0)\right)\right\} \\
& +2 \operatorname{Re}\left\{z^{n}\left(k_{n}+l_{n} \sum_{\beta=1}^{n-1} \mu_{\beta} \sigma_{\beta \bar{\beta}}(0)\right)\right\}-\frac{A a_{1}}{2} d(z)+O\left(|z|^{2}\right)
\end{aligned}$$

Let $l_{n}=-\frac{k_{n}}{\sum_{\beta=1}^{n-1} \mu_{\beta} \sigma_{\beta \bar{\beta}}(0)}$. For $1 \leqslant \alpha \leqslant n-1$, we set
$$l_{\alpha}=-\frac{k_{\alpha}}{\sum_{\beta=1}^{n-1} \mu_{\beta} \sigma_{\beta \bar{\beta}}(0)-\tau \mu_{\alpha}} .$$
From $\mu_{\alpha} \geqslant 0$ and (7.24), we see such $l_{i}$ (or equivalently the $l(z)$ ) are all well-defined and uniformly bounded. We thus complete the proof if $0<\tau, \delta \ll 1, A \gg 1$. \(\square\)

Completion of the proof of Lemma 7.4. Let $w$ be as in Lemma 7.6. From the construction above, we know that there is a uniform positive constant $C_{1}^{\prime}$ such that
$$|\mathfrak{g}[w]|_{C^{0}\left(\Omega_{\delta}\right)} \leqslant C_{1}^{\prime} .$$
Denote $\lambda[w]=\lambda\left(\omega^{-1} \mathfrak{g}[w]\right)$ and assume $\lambda_{1}[w] \leqslant \cdots \leqslant \lambda_{n}[w]$. Together with Lemma 7.5, Lemma 7.6 implies
$$\sum_{\alpha=1}^{n-1} \mu_{\alpha} \lambda_{\alpha}[w] \leqslant 0 \text { in } \Omega_{\delta} .$$
So by (7.19) $\left(\lambda_{1}[w], \cdots, \lambda_{n-1}[w]\right) \notin \Gamma_{\infty}$. In other words, $\lambda[w] \in X$, where
$$X=\left\{\lambda \in \mathbb{R}^{n} \backslash \Gamma:|\lambda| \leqslant C_{1}^{\prime}\right\} .$$

Notice that $X$ is a compact subset; furthermore $X \cap \bar{\Gamma}^{\inf _{M} \psi}=\emptyset$. (Note $\bar{\Gamma}^{\inf _{M} \psi}=$ $\left\{\lambda \in \Gamma: f(\lambda) \geqslant \inf _{M} \psi\right\}$ ). So we can deduce that the distance between $\bar{\Gamma}^{\inf _{M} \psi}$ and $X$ is greater than some positive constant depending on $\delta_{\psi, f}$ and other known data. Therefore, there exists a positive constant $\epsilon_{0}$ such that for any $z \in \Omega_{\delta}$
$$\epsilon_{0} \overrightarrow{\mathbf{1}}+\lambda[w] \notin \bar{\Gamma}^{\inf _{M} \psi} .$$

Near the origin $z_{0}(z=0)$, under the coordinates (7.2) the distance can be expressed as
$$\sigma(z)=x^{n}+\sum_{i, j=1}^{2 n} a_{i j} t^{i} t^{j}+O\left(|t|^{3}\right) .$$
Thus one can choose a positive constant $C^{\prime}$ such that $x^{n} \leqslant C^{\prime}|z|^{2}$ on $\partial M \cap \bar{\Omega}_{\delta}$. As a result, there is a positive constant $C_{2}$ depending only on $\partial M$ and $\delta$ so that
$$x^{n} \leqslant C_{2}|z|^{2} \text { on } \partial \Omega_{\delta} .$$

Let $C_{2}$ be as above, define $h(z)=w(z)+\epsilon\left(|z|^{2}-\frac{x^{n}}{C_{2}}\right)$. Thus
$$u \leqslant h \text { on } \partial \Omega_{\delta} .$$
From (7.30) we can choose $0<\epsilon \ll 1$ so that $\lambda[h] \notin \bar{\Gamma}^{\inf _{M} \psi}$ in $\bar{\Omega}_{\delta}$. By [7, Lemma B], we have
$$u \leqslant h \text { in } \Omega_{\delta} .$$
Notice $u(0)=\varphi(0)=h(0)$, we have $u_{x^{n}}(0) \leqslant h_{x^{n}}(0)$. Thus
$$t_{0} \leqslant \frac{1}{1+\epsilon /\left(\eta C_{2}\right)} \text {, i.e., }\left(1-t_{0}\right)^{-1} \leqslant 1+\frac{\eta C_{2}}{\epsilon} \text {. }$$

\section*{8. Quantitative boundary estimate and proof of Theorem 1.7}
8.1. Double normal derivative case. Fix $z_{0} \in \partial M$. We use local coordinate (7.2) with origin at $z_{0}(z=0)$. Let $t_{0}$ be as defined in (7.14). Fix $\varepsilon_{0}$ as in (7.20), i.e.,
$$\underline{\lambda}-\varepsilon_{0} \overrightarrow{\mathbf{1}} \in \Gamma .$$
In what follows the discussion will be given at $z_{0}$, where $g_{i \bar{j}}(0)=\delta_{i j},\left.\frac{\partial}{\partial x^{n}}\right|_{z=0}$ is the interior normal to $\partial M$. For $R>0$, define the matrix
$$A(R)=\left(\begin{array}{cc}
\mathfrak{g}_{\alpha \bar{\beta}} & \mathfrak{g}_{\alpha \bar{n}} \\
\mathfrak{g}_{n \bar{\beta}} & R
\end{array}\right)$$
By (7.12) we can decompose $A(R)$ into
$$A(R)=A^{\prime}(R)+A^{\prime \prime}(R)$$
where
$$A^{\prime}(R)=\left(\begin{array}{cc}
\left(1-t_{0}\right)\left(\underline{\mathfrak{g}}_{\alpha \bar{\beta}}-\frac{\varepsilon_{0}}{4} \delta_{\alpha \beta}\right) & \mathfrak{g}_{\alpha \bar{n}} \\
\mathfrak{g}_{n \bar{\beta}} & R / 2
\end{array}\right), A^{\prime \prime}(R)=\left(\begin{array}{cc}
\left(A_{t_{0}}\right)_{\alpha \bar{\beta}}+\frac{\left(1-t_{0}\right) \varepsilon_{0}}{4} \delta_{\alpha \beta} & 0 \\
0 & R / 2
\end{array}\right) .$$

In order to complete the proof, we need to prove that
Lemma 8.1. There exist uniform constants $R_{3}$ and $C_{A^{\prime \prime}}$ depending on $\left(1-t_{0}\right)^{-1}$, $\varepsilon_{0}^{-1}, f$ and other known data under control, such that
$$f\left(2 \lambda\left[A^{\prime \prime}\left(R_{3}\right)\right]\right) \geqslant-C_{A^{\prime \prime}} .$$

Proof. Let $\underline{\lambda}^{\prime}$ and $\tilde{\lambda}^{\prime}$ be as in (7.16) and (7.17), respectively. One can see that there is a uniform constant $C_{0}>0$ depending on $\left|t_{0}\right|, \sup _{\partial M}|\nabla u|$ and other known data, such that $\left|\tilde{\lambda}^{\prime}\right| \leqslant C_{0}$, that is $\tilde{\lambda}^{\prime}$ is contained in a compact subset of $\bar{\Gamma}_{\infty}$, i.e.,
$$\tilde{\lambda}^{\prime} \in K \equiv\left\{\lambda^{\prime} \in \bar{\Gamma}_{\infty}:\left|\lambda^{\prime}\right| \leqslant C_{0}\right\} .$$
Thus there is a positive constant $R_{2}$ depending on $\left(\left(1-t_{0}\right) \varepsilon_{0}\right)^{-1}, K$ and other known data, such that
$$\lambda\left[\left(\left(A_{t_{0}}\right)_{\alpha \bar{\beta}}+\frac{\left(1-t_{0}\right) \varepsilon_{0}}{8} \delta_{\alpha \beta} \quad 0\right.\right. \text {. }$$
Let $R_{3}=R_{2}+\frac{\left(1-t_{0}\right) \varepsilon_{0}}{4}$, we have
$$\lambda\left[A^{\prime \prime}\left(R_{3}\right)\right] \in \Gamma+\frac{\left(1-t_{0}\right) \varepsilon_{0}}{8} \overrightarrow{\mathbf{1}} .$$
Notice that $A^{\prime \prime}\left(R_{3}\right)$ is bounded. There exists a uniform constant $C_{A^{\prime \prime}}$ depending on $\left(1-t_{0}\right)^{-1}, \varepsilon_{0}^{-1}, R_{3}$ and $f$, such that (8.3) holds. \(\square\)

Proof of Proposition 7.1. By the unbounded condition (1.8), there is a positive constant $R_{1}$ depending on $\left(1-t_{0}\right)^{-1}, \varepsilon_{0}, \underline{\lambda}^{\prime}$ and $\sup _{\partial M} \psi, C_{A^{\prime \prime}}$ such that
$$\frac{1}{2} f\left(2\left(1-t_{0}\right)\left(\underline{\lambda}_{1}^{\prime}-\varepsilon_{0} / 2\right), \cdots, 2\left(1-t_{0}\right)\left(\underline{\lambda}_{n-1}^{\prime}-\varepsilon_{0} / 2\right), 2 R_{1}\right) \geqslant f(\underline{\lambda})+\frac{C_{A^{\prime \prime}}}{2},$$
and $\left(\underline{\lambda}_{1}^{\prime}-\varepsilon_{0} / 2, \cdots, \underline{\lambda}_{n-1}^{\prime}-\varepsilon_{0} / 2,\left(1-t_{0}\right)^{-1} R_{1}\right) \in \Gamma$.

Let's pick $\epsilon=\frac{\left(1-t_{0}\right) \varepsilon_{0}}{4}$ in Lemma 3.12. And then we set
$$\begin{aligned}
R_{c} \equiv & \frac{8(2 n-3)}{\left(1-t_{0}\right) \varepsilon_{0}} \sum_{\alpha=1}^{n-1}\left|\mathfrak{g}_{\alpha \bar{n}}\right|^{2}+2(n-1)\left(1-t_{0}\right) \sum_{\alpha=1}^{n-1}\left|\underline{\lambda}_{\alpha}^{\prime}\right| \\
& +\frac{n(n-1)\left(1-t_{0}\right) \varepsilon_{0}}{2}+2 R_{1}+2 R_{2},
\end{aligned}$$
where $\varepsilon_{0}, R_{1}$ and $R_{2}$ are the constants as we fixed in (8.6) and (8.5).
According to Lemma 3.12, the eigenvalues $\lambda\left[A^{\prime}\left(R_{c}\right)\right]$ of $A^{\prime}\left(R_{c}\right)$ (possibly with an appropriate order) shall behave like
$$\begin{gathered}
\lambda_{\alpha}\left[A^{\prime}\left(R_{c}\right)\right] \geqslant\left(1-t_{0}\right)\left(\underline{\lambda}_{\alpha}^{\prime}-\varepsilon_{0} / 2\right), 1 \leqslant \alpha \leqslant n-1, \\
\lambda_{n}\left[A^{\prime}\left(R_{c}\right)\right] \geqslant R_{c} / 2 .
\end{gathered}$$
In particular, $\lambda\left[A^{\prime}\left(R_{c}\right)\right] \in \Gamma$. So $\lambda\left[A\left(R_{c}\right)\right] \in \Gamma$. By the concavity, Lemma 8.1 and (8.6), (8.8), (8.9), we deduce that
$$f\left(\lambda\left[A\left(R_{c}\right)\right]\right) \geqslant \frac{1}{2} f\left(2 \lambda\left[A^{\prime}\left(R_{c}\right)\right]\right)+\frac{1}{2} f\left(2 \lambda\left[A^{\prime \prime}\left(R_{c}\right)\right]\right) \geqslant f(\underline{\lambda}) \geqslant \psi .$$
Thus $\mathfrak{g}_{n \bar{n}} \leqslant R_{c}$. By Lemma 7.4, $\left(1-t_{0}\right)^{-1}$ is bounded. We complete the proof. \(\square\)

When $f$ satisfies (1.6), applying Lemma 3.11 we have immediately
Lemma 8.2. Let $R_{c}$ be as in (8.7). Assume in addition that $f$ satisfies (1.6). Then
$$f\left(\lambda\left[A\left(R_{c}\right)\right]\right) \geqslant f\left(\lambda\left[A^{\prime}\left(R_{c}\right)\right]\right) .$$

Corollary 8.3. When $f$ further satisfies (1.6), the unbounded condition (1.8) imposed in Theorems 1.6 and 1.7 can be replaced by a slightly broader condition
$$\lim _{t \rightarrow+\infty} f\left(\lambda_{1}, \cdots, \lambda_{n-1}, \lambda_{n}+t\right)=\sup _{\Gamma} f, \forall \lambda=\left(\lambda_{1}, \cdots, \lambda_{n}\right) \in \Gamma .$$

Proof. The unbounded condition (8.12) implies that
$$f\left(\left(1-t_{0}\right)\left(\underline{\lambda}_{1}^{\prime}-\varepsilon_{0}\right), \cdots,\left(1-t_{0}\right)\left(\underline{\lambda}_{n-1}^{\prime}-\varepsilon_{0}\right), R_{1}\right) \geqslant f(\underline{\lambda}) .$$
So when $f$ satisfies (1.6), we can use (8.13) and (8.11), in place of (8.6) and (8.10) respectively. Consequently, in this case (1.8) can be replaced by (8.12). \(\square\)
8.2. Tangential-Normal derivatives case. We use the usual subsolution method of [28, 24] (further refined by [25, 26]). In order to derive (7.6), we shall construct more delicate local barriers near boundary. The specific instance of such local barriers was investigated by [5, 9, 44] for complex Monge-Ampère equation, and further by [14] for more general complex $k$-Hessian equations. The utilization of local barriers for general equations was introduced by [63, 65] in some case.

We will highlight that the expression $\left|\sum f_{i} \lambda_{i}\right|$ in Lemma 3.1 offers a simplified method for managing the problematic terms that incorporate $\sum f_{i}\left|\lambda_{i}\right|$. This enhances some of the techniques mentioned earlier.

Under the local coordinate (7.2) with origin at $z_{0} \in \partial M$. As in (7.3) we set
$$t^{2 \alpha-1}=x^{\alpha}, t^{2 \alpha}=y^{\alpha}, 1 \leqslant \alpha \leqslant n-1 ; t^{2 n-1}=y^{n}, t^{2 n}=x^{n} .$$

As we denoted in (4.2),
$$K=1+\sup _{M}\left(|\nabla u|_{\omega}^{2}+|\nabla(u-\underline{u})|_{\omega}^{2}\right) .$$

We use the notation in (2.1). By direct calculations, one derives
$$\begin{gathered}
\left(u_{x^{k}}\right)_{\bar{j}}=u_{\bar{j} x^{k}}+\overline{\Gamma_{k j}^{l}} u_{\bar{l}}, \quad\left(u_{y^{k}}\right)_{\bar{j}}=u_{\bar{j} y^{k}}-\sqrt{-1} \overline{\Gamma_{k j}^{l}} u_{\bar{l}}, \\
\left(u_{x^{k}}\right)_{i \bar{j}}=u_{i \bar{j} x^{k}}+\Gamma_{k i}^{l} u_{l \bar{j}}+\overline{\Gamma_{k j}^{l}} u_{i \bar{l}}, \quad\left(u_{y^{k}}\right)_{i \bar{j}}=u_{i \bar{j} y^{k}}+\sqrt{-1}\left(\Gamma_{k i}^{l} u_{l \bar{j}}-\overline{\Gamma_{k j}^{l}} u_{i \bar{l}}\right) .
\end{gathered}$$

We set
$$w=(\underline{u}-u)-t \sigma+N \sigma^{2} \text { in } \Omega_{\delta} .$$
Here $N$ is a positive constant to be determined, $\delta$ and $t$ are small enough such that
$$\begin{gathered}
\sigma \text { is smooth, } \frac{1}{4} \leqslant|\nabla \sigma| \leqslant 2,|\mathcal{L} \sigma| \leqslant C_{\sigma} \sum_{i=1}^{n} f_{i} \text { in } \Omega_{\delta}, \\
N \delta-t \leqslant 0, \max \{|2 N \delta-t|, t\} \leqslant \frac{\varepsilon}{32 C_{\sigma}}
\end{gathered}$$
for some constant $C_{\sigma}>0$, where $\varepsilon$ is the constant asserted in Lemma 3.3. Clearly,
$$\begin{gathered}
w \leqslant 0 \text { in } \Omega_{\delta}, \\
\mathcal{L} w=F^{i \bar{j}}\left(\underline{\mathfrak{g}}_{i \bar{j}}-\mathfrak{g}_{i \bar{j}}\right)+2 N F^{i \bar{j}} \sigma_{i} \sigma_{\bar{j}}+(2 N \sigma-t) \mathcal{L} \sigma \text { in } \Omega_{\delta} .
\end{gathered}$$

Define the tangential operator on the boundary
$$\mathcal{T}=\nabla_{\frac{\partial}{\partial t^{\alpha}}}-\widetilde{\eta} \nabla_{\frac{\partial}{\partial x^{n}}} \text {, for each fixed } 1 \leqslant \alpha<2 n \text {, }$$
where $\widetilde{\eta}=\sigma_{t^{\alpha}} / \sigma_{x^{n}}$. One has $\mathcal{T}(u-\varphi)=0$ on $\partial M \cap \bar{\Omega}_{\delta}$. By $\widetilde{\eta}(0)=0$ one derives $|\widetilde{\eta}| \leqslant C^{\prime}|z|$ on $\bar{\Omega}_{\delta}$. Since $\left.(u-\varphi)\right|_{\partial M}=0$ we obtain $\left.\mathcal{T}(u-\varphi)\right|_{\partial M}=0$. Together with the boundary gradient estimate contained in Lemma 7.3, one has
$$\left|(u-\varphi)_{t^{\alpha}}\right| \leqslant C|z| \text { on } \partial M \cap \bar{\Omega}_{\delta}, \forall 1 \leqslant \alpha<2 n .$$

Take
$$\Phi= \pm \mathcal{T}(u-\varphi)+\frac{1}{\sqrt{K}}\left(u_{y^{n}}-\varphi_{y^{n}}\right)^{2} \text { in } \Omega_{\delta} .$$
Note that $u_{x_{n}}=2 u_{n}+\sqrt{-1} u_{y_{n}}$ and $u_{x_{n}}=2 u_{\bar{n}}-\sqrt{-1} u_{y_{n}}$. Combining Cauchy-Schwarz inequality, we can prove
$$\mathcal{L} \Phi \geqslant-C_{\Phi} \sqrt{K} \sum_{i=1}^{n} f_{i}-C_{\Phi} \sum_{i=1}^{n} f_{i}\left|\lambda_{i}\right|-C_{\Phi} \text { on } \Omega_{\delta} .$$
In the proof of (8.19) we use
$$2\left|\Re \mathfrak{e}\left(F^{i \bar{j}}(\widetilde{\eta})_{i}\left(u_{x^{n}}\right)_{\bar{j}}\right)\right| \leqslant \frac{1}{\sqrt{K}} F^{i \bar{j}}\left(u_{y^{n}}\right)_{i}\left(u_{y^{n}}\right)_{\bar{j}}+C \sum_{i=1}^{n} f_{i}\left|\lambda_{i}\right|+C \sqrt{K} \sum_{i=1}^{n} f_{i} .$$

By straightforward computations and [25, Proposition 2.19], there is an index $r$ with $1 \leqslant r \leqslant n$ such that
$$\begin{aligned}
\mathcal{L}\left(\sum_{\tau<n}\left|(u-\varphi)_{\tau}\right|^{2}\right) & \geqslant \frac{1}{2} \sum_{\tau<n} F^{i \bar{j}} \mathfrak{g}_{\bar{\tau} i} \mathfrak{g}_{\tau \bar{j}}-C_{1} \sqrt{K}\left(\sum_{i=1}^{n} f_{i}\left|\lambda_{i}\right|+\sum_{i=1}^{n} f_{i}\right)+2 \sum_{\tau<n} \Re \mathfrak{e}\left(u_{\tau} \psi_{\bar{\tau}}\right) \\
& \geqslant \frac{1}{4} \sum_{i \neq r} f_{i} \lambda_{i}^{2}-C_{1}^{\prime} \sqrt{K}\left(1+\sum_{i=1}^{n} f_{i}+\sum_{i=1}^{n} f_{i}\left|\lambda_{i}\right|\right) .
\end{aligned}$$

In order to treat the terms involving $\sum f_{i}\left|\lambda_{i}\right|$, applying Cauchy-Schwarz inequality, we can derive
$$\begin{aligned}
\sum f_{i}\left|\lambda_{i}\right| & =\sum_{i=1}^{n} f_{i} \lambda_{i}-2 \sum_{\lambda_{i}<0} f_{i} \lambda_{i}=2 \sum_{\lambda_{i} \geq 0} f_{i} \lambda_{i}-\sum_{i=1}^{n} f_{i} \lambda_{i} \\
& \leqslant \epsilon \sum_{i \neq r} f_{i} \lambda_{i}^{2}+\epsilon^{-1} \sum f_{i}+\left|\sum_{i=1}^{n} f_{i} \lambda_{i}\right|, \forall \epsilon>0 .
\end{aligned}$$

The local barrier function in $\Omega_{\delta}$ is as follows:
$$\widetilde{\Psi}=A_{1} \sqrt{K} w-A_{2} \sqrt{K}|z|^{2}+A_{3} \Phi+\frac{1}{\sqrt{K}} \sum_{\tau<n}\left|(u-\varphi)_{\tau}\right|^{2} .$$
Putting the above inequalities and (2.2) together, we obtain in $\Omega_{\delta}$
$$\begin{aligned}
\mathcal{L} \widetilde{\Psi} \geqslant & A_{1} \sqrt{K} F^{i \bar{j}}\left(\underline{g}_{i \bar{j}}-\mathfrak{g}_{i \bar{j}}\right)+2 A_{1} N \sqrt{K} F^{i \bar{j}} \sigma_{i} \sigma_{\bar{j}} \\
& -\left(A_{2}+A_{3} C_{\Phi}+A_{1} C_{\sigma}|2 N \sigma-t|+4\left(C_{1}^{\prime}+A_{3} C_{\Phi}\right)^{2}\right) \sqrt{K} \sum_{i=1}^{n} f_{i} \\
& -\left(C_{1}^{\prime}+A_{3} C_{\Phi}\right)\left(1+\left|\sum f_{i} \lambda_{i}\right|\right)-C_{1}^{\prime} \sum_{i=1}^{n} f_{i} .
\end{aligned}$$
Here we set $\epsilon=\frac{1}{4 \sqrt{K}\left(A_{3} C_{\Phi}+C_{1}^{\prime}\right)}$ in (8.20).
Proposition 7.2 then follows from the following lemma.
Lemma 8.4. There are constants $A_{1} \gg A_{2} \gg A_{3}^{2} \gg 1,0<\delta \ll 1, N \gg 1$ such that $\widetilde{\Psi}(0)=0,\left.\widetilde{\Psi}\right|_{\partial \Omega_{\delta}} \leqslant 0$, and
$$\mathcal{L} \widetilde{\Psi}>0 \text { on } \Omega_{\delta} .$$
Proof. Obviously $\widetilde{\Psi}(0)=0$. Using (8.16), (8.18) and $\left.\mathcal{T}(u-\varphi)\right|_{\partial M}=0$ we can infer that $\left.\widetilde{\Psi}\right|_{\partial \Omega_{\delta}} \leqslant 0$.

Next we will prove (8.22). The discussion can be divided into two cases according to Lemma 3.3.
Case 1: In the first case we have
$$F^{i \bar{j}}\left(\underline{\mathfrak{g}}_{i \bar{j}}-\mathfrak{g}_{i \bar{j}}\right) \geqslant \varepsilon+\varepsilon F^{i \bar{j}} g_{i \bar{j}}+\varepsilon\left|F^{i \bar{j}} \mathfrak{g}_{i \bar{j}}\right| .$$
Furthermore, by (8.15) we see that $C_{\sigma}|2 N \sigma-t| \leqslant \frac{\varepsilon}{32}$.
From (8.21) we know that (8.22) holds if $A_{1} \gg A_{3}^{2} \gg 1$ and $A_{1} \gg A_{2} \gg 1$.

Case 2: In the rest case, by Lemma 3.3 we have
$$F^{i \bar{j}} \geqslant \varepsilon\left(1+F^{p \bar{q}} g_{p \bar{q}}+\left|F^{p \bar{q}} \mathfrak{g}_{p \bar{q}}\right|\right) g^{i \bar{j}} .$$
From (8.14), we have $|\nabla \sigma| \geqslant \frac{1}{4}$ in $\Omega_{\delta}$, and then
$$F^{i \bar{j}} \sigma_{i} \sigma_{\bar{j}} \geqslant \frac{\varepsilon}{16}\left(1+\sum_{i=1}^{n} f_{i}+\left|\sum_{i=1}^{n} f_{i} \lambda_{i}\right|\right) \text { on } \Omega_{\delta}$$
for sufficiently small $\delta>0$. Note that $F^{i \bar{j}}\left(\underline{\mathfrak{g}}_{i \bar{j}}-\mathfrak{g}_{i \bar{j}}\right) \geqslant 0$. From (8.21) and (8.15), we can conclude that
$$\begin{aligned}
\mathcal{L} \widetilde{\Psi} \geqslant & \frac{A_{1} N \varepsilon}{8} \sqrt{K}\left(1+\sum_{i=1}^{n} f_{i}+\left|\sum_{i=1}^{n} f_{i} \lambda_{i}\right|\right)-\left(C_{1}^{\prime}+A_{3} C_{\Phi}\right)\left(1+\left|\sum_{i=1}^{n} f_{i} \lambda_{i}\right|\right) \\
& -C_{1}^{\prime} \sum_{i=1}^{n} f_{i}-\left(A_{2}+A_{3} C_{\Phi}+\frac{A_{1} \varepsilon}{32}+4\left(C_{1}^{\prime}+A_{3} C_{\Phi}\right)^{2}\right) \sqrt{K} \sum_{i=1}^{n} f_{i}>0
\end{aligned}$$
on $\Omega_{\delta}$, provided $A_{1} \gg A_{3}^{2} \gg 1, A_{1} \gg A_{2} \gg 1,0<\delta \ll 1$ and $N \geqslant 1$. \(\square\)
8.3. Tangential-Normal derivatives case revisited. We say that $\partial M$ is holomorphically flat, if for any $z_{0} \in \partial M$ one can pick local complex coordinates
$$\left(z^{1}, \cdots, z^{n}\right), z^{i}=x^{i}+\sqrt{-1} y^{i},$$
centered at $z_{0}$ such that $\partial M$ is locally of the form $\Re \mathfrak{e}\left(z^{n}\right)=0$.
In this case, we have a delicate result: The estimate depends on $\partial M$ up to second derivatives, rather than third derivatives.

Proposition 8.5. In addition to (1.3), (1.4), (1.5) and (1.12), we assume that $\partial M$ is holomorphically flat. Then for any admissible solution $u \in C^{3}(M) \cap C^{2}(\bar{M})$ to the Dirichlet problem (1.7) satisfies
$$\left|\mathfrak{g}_{\alpha \bar{n}}\left(z_{0}\right)\right| \leqslant C\left(1+\sup _{M}|\nabla u|\right), \forall z_{0} \in \partial M .$$
where $C$ depends on $|\psi|_{C^{1}(\bar{M})},|\underline{u}|_{C^{2}(\bar{M})},|\varphi|_{C^{3}(\bar{M})}, \partial M$ up to second derivatives and other known data (but neither on $\left(\delta_{\psi, f}\right)^{-1}$ nor on $\sup _{M}|\nabla u|$ ).

Sketch of the proof. Under the complex coordinates (8.23), we can take
$$D=\frac{\partial}{\partial x^{\alpha}}, \frac{\partial}{\partial y^{\alpha}}, 1 \leqslant \alpha \leqslant n-1 .$$
(Furthermore, we may assume $g_{i \bar{j}}=\delta_{i j}$ at $z_{0}$ ). We use the local barriers
$$\widetilde{\Psi}=A_{1} \sqrt{K} w-A_{2} \sqrt{K}|z|^{2}+\frac{1}{\sqrt{K}} \sum_{\tau<n}\left|(u-\varphi)_{\tau}\right|^{2} \pm A_{3} D(u-\varphi) .$$
The rest proof is similar to that of Subsection 8.2. \(\square\)

\section*{9. The Dirichlet problem for degenerate equations}

In this section, we consider the Dirichlet problem for degenerate equations.
Definition 9.1. We call $\underline{u}$ a strict subsolution to (1.7), if for some $\delta>0$
$$F(\mathfrak{g}[\underline{u}]) \geqslant \psi+\delta \text { in } \bar{M}, \underline{u}=\varphi \text { on } \partial M .$$

Let $\Gamma_{\mathcal{G}}^{f}$ be as in (1.10). As denoted in Introduction, Let $\Gamma_{\mathcal{G}, \infty}^{f}$ be the projection of $\stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f}$ to the subspace of former $n-1$ subscripts, that is
$$\Gamma_{\mathcal{G}, \infty}^{f}=\left\{\left(\lambda_{1}, \cdots, \lambda_{n-1}\right):\left(\lambda_{1}, \cdots, \lambda_{n-1}, R\right) \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f} \text { for some } R>0\right\} .$$
Also, $\bar{\Gamma}_{\mathcal{G}, \infty}^{f}$ denotes the closure of $\Gamma_{\mathcal{G}, \infty}^{f}$.
Throughout this section we assume that the boundary satisfies
$$\left(-\kappa_{1}, \cdots,-\kappa_{n-1}\right) \in \bar{\Gamma}_{\mathcal{G}, \infty}^{f} \text { on } \partial M,$$
where $\kappa_{1}, \cdots, \kappa_{n-1}$ denote the eigenvalues of Levi form $L_{\partial M}$ of $\partial M$ with respect to $\omega^{\prime}=\left.\omega\right|_{T_{\partial M} \cap J T_{\partial M}}$. As above, $J$ denotes the underlying complex structure.

We first drop the unbounded condition imposed in Theorem 1.6.
Theorem 9.2. In Theorem 1.6 the hypothesis (1.8) on $f$ can be dropped if the Levi form $L_{\partial M}$ satisfies (9.2) and $f$ obeys (1.3).

It is a remarkable fact that the boundary estimate is independent of $\left(\delta_{\psi, f}\right)^{-1}$ when $\partial M$ satisfies (9.2), as shown in Theorem 9.5. As a result, we can treat the Dirichlet problem for degenerate equations.

Theorem 9.3. Let $(M, \omega)$ be a compact Hermitian manifold with smooth boundary subject to (9.2), and let $f$ satisfy (1.3), (1.4) and (1.15). Assume $\varphi \in C^{2,1}(\partial M)$ and $\psi \in C^{1,1}(\bar{M})$ satisfy (1.14) and support a strict, admissible subsolution $\underline{u} \in$ $C^{2,1}(\bar{M})$. Then there exists a (weak) solution $u \in C^{1, \alpha}(\bar{M})$ to the Dirichlet problem (1.7) with $\forall 0<\alpha<1$ such that
$$\lambda\left(\omega^{-1} \mathfrak{g}[u]\right) \in \bar{\Gamma} \text { in } \bar{M}, \Delta u \in L^{\infty}(\bar{M}) .$$

This shows that one may solve the Dirichlet problem for degenerate equations on manifolds with $C^{2,1}$ boundary data. Moreover, the weak solution to Dirichlet problem of degenerate equations on products was also obtained in Theorem 10.3 below, where both boundary and boundary data are in class of $C^{2,1}$. This is in contrast with bounded domain $\Omega \subseteq \mathbb{R}^{n}$ case, in which Caffarelli-Nirenberg-Spruck [8] showed that $C^{3,1}$-regularity assumptions on boundary and boundary value are optimal for $C^{1,1}$ global regularity of weak solution to homogeneous real Monge-Ampère equation. Note also that the principal curvatures of bounded domain do not satisfy one similar to (9.2). Hence we believe that the assumption (9.2) is reasonable.
9.1. Quantitative boundary estimate revisited. The boundary estimate for double normal derivative is fairly delicate when the boundary satisfies (9.2).

Proposition 9.4. Let $(M, \omega)$ be a compact Hermitian manifold with $C^{2}$ boundary satisfying (9.2). Suppose, in addition to (1.3), (1.4) and (1.5), that the Dirichlet problem (1.7) admits a $C^{2}$ admissible subsolution $\underline{u}$. Let $u \in C^{2}(\bar{M})$ be an admissible solution to the Dirichlet problem, then
$$\mathfrak{g}_{n \bar{n}}\left(z_{0}\right) \leqslant C\left(1+\sum_{\alpha=1}^{n-1}\left|\mathfrak{g}_{\alpha \bar{n}}\left(z_{0}\right)\right|^{2}\right), \quad \forall z_{0} \in \partial M .$$
where $C$ depends only on $|u|_{C^{0}(\bar{M})},|\nabla u|_{C^{0}(\partial M)},|\underline{u}|_{C^{2}(\bar{M})}, \partial M$ up to second order derivatives and other known data. Moreover, the constant is independent of $\left(\delta_{\psi, f}\right)^{-1}$.

Proof. The proof is based on Lemma 3.7. Near $z_{0} \in \partial M$, we choose the local complex coordinate (7.2) with origin at $z_{0}(z=0)$. In what follows, the discussion will be given at $z_{0}$. As in (7.18), we denote $\eta=(u-\underline{u})_{x^{n}}(0)$. The maximum principle tells us that $\eta \geqslant 0$.

First, there exist uniform positive constants $\varepsilon_{1}$ and $R_{1}$ such that
$$f\left(\underline{\lambda}_{1}^{\prime}-\varepsilon_{1}, \cdots, \underline{\lambda}_{n-1}^{\prime}-\varepsilon_{1}, R_{1}\right) \geqslant f(\underline{\lambda}),$$
and $\left(\underline{\lambda}_{1}^{\prime}-\varepsilon_{1}, \cdots, \underline{\lambda}_{n-1}^{\prime}-\varepsilon_{1}, R_{1}\right) \in \Gamma$. Take $\epsilon_{1}>0$ sufficiently small such that
$$\epsilon_{1} \sup _{\partial M}|\nabla(u-\underline{u})| \leqslant \frac{\varepsilon_{1}}{4} .$$
Such an $\epsilon_{1}$ exists according to Lemma 7.3. Fix such constants above. Denote
$$B^{\prime}(R)=\left(\begin{array}{cc}
\underline{\mathfrak{g}}_{\alpha \bar{\beta}}-\epsilon_{1} \eta \delta_{\alpha \beta} & \mathfrak{g}_{\alpha \bar{n}} \\
\mathfrak{g}_{n \bar{\beta}} & R
\end{array}\right), B^{\prime \prime}(R)=\left(\begin{array}{cc}
\sigma_{\alpha \bar{\beta}}+\epsilon_{1} \delta_{\alpha \beta} & 0 \\
0 & R
\end{array}\right) .$$
Under the assumption (9.2), there exists a uniform constant $R_{4}$ such that
$$\lambda\left[B^{\prime \prime}\left(R_{4}\right)\right] \in \stackrel{\circ}{\Gamma}_{\mathcal{G}}^{f} .$$

Let $A(R)$ be as in (8.1), i.e.,
$$A(R)=\left(\begin{array}{cc}
\mathfrak{g}_{\alpha \bar{\beta}} & \mathfrak{g}_{\alpha \bar{n}} \\
\mathfrak{g}_{n \bar{\beta}} & R
\end{array}\right)$$
By the boundary value condition we have (7.11), i.e., $\mathfrak{g}_{\alpha \bar{\beta}}=\underline{\mathfrak{g}}_{\alpha \bar{\beta}}+\eta \sigma_{\alpha \bar{\beta}}$. Obviously,
$$A(R)=B^{\prime}\left(R-\eta R_{4}\right)+\eta B^{\prime \prime}\left(R_{4}\right) .$$

Let's pick $\epsilon=\frac{\varepsilon_{1}}{4}$ in Lemma 3.12. In analogy with (8.7), we take
$$R_{c}^{\prime} \equiv \frac{4(2 n-3)}{\varepsilon_{1}} \sum_{\alpha=1}^{n-1}\left|\mathfrak{g}_{\alpha \bar{n}}\right|^{2}+(n-1) \sum_{\alpha=1}^{n-1}\left|\underline{\lambda}_{\alpha}^{\prime}\right|+\frac{n(n-1) \varepsilon_{1}}{2}+R_{1}+\eta R_{4} .$$
According to Lemma 3.12, the eigenvalues of $B^{\prime}\left(R_{c}-\eta R_{4}\right)$ behave like
$$\begin{gathered}
\lambda_{\alpha}\left[B^{\prime}\left(R_{c}-\eta R_{4}\right)\right] \geqslant\left(\underline{\lambda}_{\alpha}^{\prime}-\varepsilon_{1} / 2\right), 1 \leqslant \alpha \leqslant n-1, \\
\lambda_{n}\left[B^{\prime}\left(R_{c}-\eta R_{4}\right)\right] \geqslant R_{c}^{\prime}-\eta R_{4} .
\end{gathered}$$

In particular, $\lambda\left[B^{\prime}\left(R_{c}^{\prime}-\eta R_{4}\right)\right] \in \Gamma$ and so $\lambda\left[A\left(R_{c}^{\prime}\right)\right] \in \Gamma$. Combining with (9.3), we conclude that
$$f\left(\lambda\left[B^{\prime}\left(R_{c}^{\prime}-\eta R_{4}\right)\right]\right) \geqslant f(\underline{\lambda}) \geqslant \psi .$$
Together with (9.6), (9.7) and $\eta \geqslant 0$, Lemma 3.7 implies that
$$f\left(\lambda\left[A\left(R_{c}^{\prime}\right)\right]\right) \geqslant f\left(\lambda\left[B^{\prime}\left(R_{c}^{\prime}-\eta R_{4}\right)\right]\right) .$$
This gives that $\mathfrak{g}_{n \bar{n}} \leqslant R_{c}^{\prime}$. \(\square\)

Combining Propositions 9.4 and 7.2, we conclude that
Theorem 9.5. In Theorem 1.7 the constant $C$ is independent of $\left(\delta_{\psi, f}\right)^{-1}$ and the hypothesis (1.8) can be dropped, provided that $\partial M$ satisfies (9.2) and $f$ obeys (1.3).

When $\partial M$ is holomorphically flat, combining Propositions 9.4 and 8.5, we obtain some more delicate result.

Theorem 9.6. In addition to (1.3), (1.4), (1.5), (1.12), $\varphi \in C^{3}(\partial M)$ and $\psi \in C^{1}(\bar{M})$, we assume that $\partial M$ is holomorphically flat. Then for any admissible solution $u \in$ $C^{3}(M) \cap C^{2}(\bar{M})$ to the Dirichlet problem (1.7), we have
$$\sup _{\partial M}|\partial \bar{\partial} u|_{\omega} \leqslant C\left(1+\sup _{M}|\nabla u|_{\omega}^{2}\right) .$$
Here $C$ is a uniform positive constant depending only on $|\psi|_{C^{1}(\bar{M})},|\nabla u|_{C^{0}(\partial M)},|\underline{u}|_{C^{2}(\bar{M})}$, $|\varphi|_{C^{3}(\bar{M})}$, $\partial M$ up to second derivatives and other known data. In addition, the constant is independent of $\left(\delta_{\psi, f}\right)^{-1}$.
9.2. Uniqueness of weak solution. Following Chen [9], we define

Definition 9.7. A continuous function $u \in C(\bar{M})$ is a weak $C^{0}$-solution to the degenerate equation (1.7) with prescribed boundary data $\varphi$, if for any sufficiently small positive constant $\epsilon$ there is a $C^{2}$-admissible function $\widetilde{u}$ such that
$$|u-\widetilde{u}|<C(\epsilon),$$
where $\widetilde{u}$ solves
$$F(\mathfrak{g}[\widetilde{u}])=\psi+\rho_{\epsilon} \text { in } M, \quad \widetilde{u}=\varphi \text { on } \partial M .$$
Here $\rho_{\epsilon}$ is a function satisfying $0<\rho_{\epsilon}<\epsilon$, and $C(\epsilon) \rightarrow 0$ as $\epsilon \rightarrow 0$.
We first obtain the stability of weak $C^{0}$-solutions. The proof is almost parallel to that of [9, Theorem 4]. We omit the proof here.

Theorem 9.8. Suppose $u^{1}, u^{2}$ are two weak $C^{0}$-solutions to the degenerate equation (1.7) with boundary data $\varphi^{1}, \varphi^{2}$. Then
$$\sup _{M}\left|u^{1}-u^{2}\right| \leqslant \sup _{\partial M}\left|\varphi^{1}-\varphi^{2}\right| .$$

As a corollary, we derive the uniqueness of weak $C^{0}$-solution.
Corollary 9.9. The weak $C^{0}$-solution to the Dirichlet problem (1.7) for degenerate equation is unique, provided the boundary data is fixed.

\section*{10. Dirichlet problem on products}

The Dirichlet problem for degenerate equations have important applications in complex geometry and analysis. There are many challenging open problems.

In this section we study a special problem on certain product of the form
$$(M, \omega)=(X \times S, \omega),$$
where and hereafter, $\left(X, \omega_{X}\right)$ is a closed Hermitian manifold of complex dimension $n-1$, and $\left(S, \omega_{S}\right)$ is a compact Riemann surface with sufficiently smooth boundary $\partial S$, and $\omega$ is a Hermitian metric being compatible with the induced complex structure $J$. (We remark that $\omega$ is not necessarily the product metric).

Let $\vec{v}$ be the unit inner normal vector along the boundary.
10.1. Construction of subsolutions. The Dirichlet problem is insolvable without subsolution assumption. Therefore, one natural question is to construct subsolutions. Unfortunately, beyond on certain domains in Euclidean spaces [6, 7] (see also [40]), few progress has been made on curved manifolds.

In this section, on the product $M=X \times S$ we construct strict admissible subsolutions with $\left.\frac{\partial \underline{u}}{\partial \vec{v}}\right|_{\partial M}<0$, provided that
$$\lambda\left[\omega^{-1}\left(\mathfrak{g}[\varphi]+t \pi_{2}^{*} \omega_{S}\right)\right] \in \Gamma \text { in } \bar{M},$$
for some $t>0$, and
$$\lim _{t \rightarrow+\infty} f\left(\lambda\left[\omega^{-1}\left(\mathfrak{g}[\varphi]+t \pi_{2}^{*} \omega_{S}\right)\right]\right)>\psi \text { in } \bar{M} .$$
Henceforth $\pi_{1}: X \times S \rightarrow X$ and $\pi_{2}: X \times S \rightarrow S$ stand for the natural projections, (Here $\varphi$ is an appropriate extension of boundary data to $\bar{M}$ ).

To do this, we begin with the solution $h$ to
$$\Delta_{S} h=1 \text { in } S, h=0 \text { on } \partial S,$$
where $\Delta_{S}$ is the Laplacian operator of $\left(S, J_{S}, \omega_{S}\right)$. The existence and regularity can be found in standard monographs; see e.g. [23]. More precisely, when $\partial S \in C^{\infty}$, $h \in C^{\infty}(\bar{S})$; while $h \in C^{\infty}(S) \cap C^{2, \beta}(\bar{S})$ if $\partial S \in C^{2, \beta}(0<\beta<1)$. Moreover, $\left.\frac{\partial h}{\partial \vec{v}}\right|_{\partial S}<0$. The subsolution is precisely given by
$$\underline{u}=\varphi+t \pi_{2}^{*} h$$
for $t \gg 1$ ( $\pi_{2}^{*} h=h \circ \pi_{2}$, still denoted by $h$ for simplicity), then
$$\mathfrak{g}[\underline{u}]=\mathfrak{g}[\varphi]+t \pi_{2}^{*} \omega_{S},\left.\quad \frac{\partial \underline{u}}{\partial \vec{v}}\right|_{\partial M}<0 \text { for } t \gg 1 .$$
Therefore, $\underline{u}$ is the subsolution if (10.2) and (10.3) hold. Furthermore, the condition (10.3) always holds when $f$ satisfies (1.8) and $\varphi$ is admissible.

Significantly, if $\omega=\pi_{1}^{*} \omega_{X}+\pi_{2}^{*} \omega_{S}$ and $\chi$ splits by $\chi=\pi_{1}^{*} \chi_{1}+\pi_{2}^{*} \chi_{2}$, then according to Lemma 3.12, conditions (10.2) and (10.3) reduce to
$$\lim _{t \rightarrow+\infty} f\left(\lambda\left(\omega_{X}^{-1} \chi_{1}\right), t\right)>\psi \text { and } \lambda\left(\omega_{X}^{-1} \chi_{1}\right) \in \Gamma_{\infty} \text { in } \bar{M},$$
where $\chi_{1}$ is a real ( 1,1 )-form on $X, \chi_{2}$ is a real ( 1,1 )-form on $S$. This indicates that, for $\chi=\pi_{1}^{*} \chi_{1}+\pi_{2}^{*} \chi_{2}$ the solvability of Dirichlet problem is determined by $\chi_{1}$.

Remark 10.1. Let ( $Y, \omega_{Y}$ ) be a closed Hermitian manifold of complex dimension $n-m$, let $\Omega$ be a smooth bounded strictly pseudoconvex domain in $\mathbb{C}^{m}, 2 \leqslant m \leqslant$ $n-1$. Under the assumption that
$$\lim _{t \rightarrow+\infty} f\left(\lambda_{1}, \cdots, \lambda_{n-m}, \lambda_{n-m+1}+t, \cdots \lambda_{n}+t\right)=\sup _{\Gamma} f, \forall\left(\lambda_{1}, \cdots, \lambda_{n}\right) \in \Gamma,$$
we can construct subsolutions on more general product $(M, \omega)=(Y \times \Omega, \omega)$.
10.2 The Dirichlet problem with less regular boundary assumption. Theorem 9.6 implies that in the product case, the quantitative boundary estimate (1.13) depends only on $\partial M$ up to second derivatives and other known data. With the bound of complex Hessian of $u$ at hand, the equation becomes uniformly elliptic. And then as in [27] we can bound the real Hessian by maximum principle. (Also, as shown in [57] using a trick from [60], one can convert (1.7) to a real uniformly elliptic concave equation). Thus a result due to Silvestre-Sirakov [48] allows one to derive $C^{2, \alpha}$ boundary regularity with only assuming $C^{2, \beta}$ boundary. Consequently, we can study the Dirichlet problem on the products with less regular boundary* and obtain some delicate result in analogy with a theorem of Savin [46] on real non-degenerate Monge-Ampère equation with homogeneous boundary value condition on bounded $C^{2, \alpha}$ strictly convex domains.

Theorem 10.2. Let $(M, \omega)=(X \times S, \omega)$ be as in (10.1) with $\partial S \in C^{2, \beta}$ for some $0<\beta<1$. Let $\varphi \equiv 0$. Suppose, in addition to (1.3) and (1.4), that
$$f\left(\lambda\left[\omega^{-1}\left(\chi+t \pi_{2}^{*} \omega_{S}\right)\right]\right)>\psi, \lambda\left[\omega^{-1}\left(\chi+t \pi_{2}^{*} \omega_{S}\right)\right] \in \Gamma \text { in } \bar{M}, t \gg 1 .$$
Then we have two conclusions:
\begin{itemize}
\item[-] The Dirichlet problem (1.7) has a unique $C^{2, \alpha}$ admissible solution for some $0<\alpha \leqslant \beta$, provided that $\psi \in C^{2}(\bar{M}), \inf _{M} \psi>\sup _{\partial \Gamma} f$.
\item[-] Suppose in addition that $f \in C^{\infty}(\Gamma) \cap C(\bar{\Gamma}), \psi \in C^{1,1}(\bar{M})$ and $\inf _{M} \psi=$ $\sup _{\partial \Gamma} f$. Then the Dirichlet problem (1.7) has a weak solution with $u \in$ $C^{1, \alpha}(\bar{M}), \forall 0<\alpha<1 \lambda\left(\omega^{-1} \mathfrak{g}[u]\right) \in \bar{\Gamma}$ and $\Delta u \in L^{\infty}(\bar{M})$.
\end{itemize}
Proof. It suffices to consider the nondegenerate case: There is some $\delta_{0}>0$ so that
$$\psi \geqslant \sup _{\partial \Gamma} f+\delta_{0} \text { in } \bar{M} .$$

The first step is to construct approximate Dirichlet problems with constant boundary data. Let $h$ be the solution to (10.4). For $t \gg 1, \underline{u}=t h$ satisfies
$$F(\mathfrak{g}[\underline{u}])=f\left(\lambda\left(\omega^{-1} \mathfrak{g}[\underline{u}]\right)\right) \geqslant \psi+\delta_{1} \text { in } \bar{M}$$
for some $\delta_{1}>0$, and $-t \operatorname{tr}_{\omega}\left(\pi_{2}^{*} \omega_{S}\right)+\operatorname{tr}_{\omega} \chi \leqslant 0$ in $\bar{M}$. Note that
$$h \in C^{\infty}(S) \cap C^{2, \beta}(\bar{S}) \text { and }\left.\frac{\partial h}{\partial \vec{v}}\right|_{\partial S}<0,$$

\footnotetext{
*We emphasize that the geometric quantities of $(M, \omega)$ (curvature $R_{i \bar{j} k \bar{l}}$ and the torsion $T_{i j}^{k}$ ) keep bounded as approximating to $\partial M$, and all derivatives of $\chi_{i \bar{j}}$ has continues extensions to $\bar{M}$, whenever $M$ has less regularity boundary. Typical examples are as follows: $M \subset M^{\prime}, \operatorname{dim}_{\mathbb{C}} M^{\prime}=n, \omega=\left.\omega_{M^{\prime}}\right|_{M}$ and the given data $\chi$ can be smoothly defined on $M^{\prime}$.
}
we get a sequence of level sets of $h$, say $\left\{h=-\alpha_{k}\right\}$, and a family of smooth Riemann surfaces $S_{k}$ enclosed by $\left\{h=-\alpha_{k}\right\}$, such that $\cup S_{k}=S$ and $\partial S_{k}$ converge to $\partial S$ in the norm of $C^{2, \beta}$. Denote $M_{k}=X \times S_{k}$.

For any $k \geqslant 1$, there exists a $\psi^{(k)} \in C^{\infty}\left(\bar{M}_{k}\right)$ such that
$$\left|\psi-\psi^{(k)}\right|_{C^{2}\left(\bar{M}_{k}\right)} \leqslant 1 / k .$$
For $k \gg 1$ we have
$$F(\mathrm{~g}[\underline{u}]) \geqslant \psi^{(k)}+\delta_{1} / 2 \text { in } M_{k}, \underline{u}=-t \alpha_{k} \text { on } \partial M_{k}$$
which is a strict, admissible subsolution to approximate Dirichlet problem
$$F(\mathfrak{g}[u])=\psi^{(k)} \text { in } M_{k}, u=-t \alpha_{k} \text { on } \partial M_{k} .$$
According to Theorem 9.2, the Dirichlet problem (10.10) admits a unique smooth admissible solution $u^{(k)} \in C^{\infty}\left(\bar{M}_{k}\right)$. Notice that $M_{k}$ is a product and the boundary data in (10.10) is a constant, Theorem 9.6 applies. Therefore,
$$\sup _{M_{k}}\left|\partial \bar{\partial} u^{(k)}\right|_{\omega} \leqslant C_{k}\left(1+\sup _{M_{k}}\left|\nabla u^{(k)}\right|_{\omega}^{2}\right)$$
where $C_{k}$ is a constant depending on $\left|u^{(k)}\right|_{C^{0}\left(M_{k}\right)},\left|\nabla u^{(k)}\right|_{C^{0}\left(\partial M_{k}\right)},|\underline{u}|_{C^{2}\left(M_{k}\right)},\left|\psi^{(k)}\right|_{C^{2}\left(M_{k}\right)}$, $\partial S_{k}$ up to second order derivatives and other known data (but not on $\left(\delta_{\psi^{(k)}, f}\right)^{-1}$ ).

It requires to prove
$$\sup _{M_{k}}\left|u^{(k)}\right|+\sup _{\partial M_{k}}\left|\nabla u^{(k)}\right| \leqslant C, \text { independent of } k .$$
Let $w^{(k)}$ be the solution of
$$\Delta w^{(k)}+\operatorname{tr}_{\omega} \chi=0 \text { in } M_{k}, w^{(k)}=-t \alpha_{k} \text { on } \partial M_{k} .$$
By the maximum principle and the boundary value condition, one has
$$\underline{u} \leqslant u^{(k)} \leqslant w^{(k)} \text { in } M_{k}, \frac{\partial \underline{u}}{\partial \vec{v}} \leqslant \frac{\partial u^{(k)}}{\partial \vec{v}} \leqslant \frac{\partial w^{(k)}}{\partial \vec{v}} \text { on } \partial M_{k} .$$
Here $\vec{v}$ denotes the unit inner normal vector along the boundary $\partial M_{k}$.
On the other hand, we have
$$\begin{array}{rlr}
\Delta\left(-\underline{u}-2 t \alpha_{k}\right)+\operatorname{tr}_{\omega} \chi & =-t \operatorname{tr}_{\omega}\left(\pi_{2}^{*} \omega_{S}\right)+\operatorname{tr}_{\omega} \chi \leqslant 0 & \text { in } M_{k}, \\
-\underline{u}-2 t \alpha_{k} & =-t \alpha_{k} & \text { on } \partial M_{k} .
\end{array}$$
As a result, we have
$$w^{(k)} \leqslant-\underline{u}-2 t \alpha_{k} \text { in } M_{k}, w^{(k)}=-\underline{u}-2 t \alpha_{k} \text { on } \partial M_{k},$$
which further implies
$$\frac{\partial w^{(k)}}{\partial \vec{v}} \leqslant-\frac{\partial \underline{u}}{\partial \vec{v}} \text { on } \partial M_{k}$$
as required. Consequently, (10.11) holds for a uniform constant $C^{\prime}$ which does not depend on $k$. Thus
$$|u|_{C^{2}\left(M_{k}\right)} \leqslant C, \text { independent of } k .$$

To complete the proof, we apply Silvestre-Sirakov's [48] result to derive $C^{2, \alpha^{\prime}}$ estimates on the boundary, while the convergence of $\partial S_{k}$ in the norm $C^{2, \beta}$ allows us to take a limit ( $\alpha^{\prime}$ can be uniformly chosen). \(\square\)

In the proof of Theorem 10.2, we use the domains enclosed by level sets to approximate the background space. Such an approximation gives a bound of (10.12) explicitly. Similarly, we can prove that

Theorem 10.3. Let $(M, \omega)=(X \times S, \omega)$ be as above with $\partial S \in C^{2,1}$, and let $f$ satisfy (1.3), (1.4) and (1.15). Given the data $\varphi \in C^{2,1}(\bar{M}), \psi \in C^{1,1}(\bar{M})$ satisfying (10.2), (10.3) and (1.14), the Dirichlet problem (1.7) has a weak solution $u$ with
$$u \in C^{1, \alpha}(\bar{M}), \forall 0<\alpha<1, \Delta u \in L^{\infty}(\bar{M}), \lambda\left[\omega^{-1}(\chi+\sqrt{-1} \partial \bar{\partial} u)\right] \in \bar{\Gamma} \text { in } \bar{M} .$$
Remark 10.4. The Dirichlet problem for homogeneous complex Monge-Ampère equation on $X \times S$ is closely connected with the geodesics in the space of Kähler potentials $\mathcal{H}_{\omega_{X}}$ [17, 47, 42]; see e.g. [4, 9, 44]. We also refer to the monograph [33] for more results regarding to degenerated Monge-Ampère equation.

\section*{11. Proof of Lemma 3.12}

In this section we complete the proof of Lemma 3.12. We start with the case $n=2$. For $n=2$, the eigenvalues of $A$ are precisely as follows
$$\lambda_{1}=\frac{\mathbf{a}+d_{1}-\sqrt{\left(\mathbf{a}-d_{1}\right)^{2}+4\left|a_{1}\right|^{2}}}{2}, \lambda_{2}=\frac{\mathbf{a}+d_{1}+\sqrt{\left(\mathbf{a}-d_{1}\right)^{2}+4\left|a_{1}\right|^{2}}}{2} .$$
We assume $a_{1} \neq 0$; otherwise we are done. If $\mathbf{a} \geqslant \frac{\left|a_{1}\right|^{2}}{\epsilon}+d_{1}$ then one has
$$0 \leqslant d_{1}-\lambda_{1}=\lambda_{2}-\mathbf{a}=\frac{2\left|a_{1}\right|^{2}}{\sqrt{\left(\mathbf{a}-d_{1}\right)^{2}+4\left|a_{1}\right|^{2}}+\left(\mathbf{a}-d_{1}\right)}<\frac{\left|a_{1}\right|^{2}}{\mathbf{a}-d_{1}} \leqslant \epsilon .$$
Here we use $a_{1} \neq 0$ to confirm the strictly inequality in the above formula.
The following lemma enables us to count the eigenvalues near the diagonal elements via a deformation argument. It is an essential ingredient in the proof of Lemma 3.12 for general $n$.

Lemma 11.1. Let $A$ be a Hermitian $n$ by $n$ matrix
$$\left(\begin{array}{ccccc}
d_{1} & & & & a_{1} \\
& d_{2} & & & a_{2} \\
& & \ddots & & \vdots \\
& & & d_{n-1} & a_{n-1} \\
\bar{a}_{1} & \bar{a}_{2} & \cdots & \bar{a}_{n-1} & \mathbf{a}
\end{array}\right)$$
with $d_{1}, \cdots, d_{n-1}, a_{1}, \cdots, a_{n-1}$ fixed, and with $\mathbf{a}$ variable. Denote $\lambda=\left(\lambda_{1}, \cdots, \lambda_{n}\right)$ the eigenvalues of $A$ with the order $\lambda_{1} \leqslant \lambda_{2} \leqslant \cdots \leqslant \lambda_{n}$. Fix $\epsilon$ a positive constant.

Suppose that the parameter a satisfies the following quadratic growth condition
$$\mathbf{a} \geqslant \frac{1}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}+\sum_{i=1}^{n-1}\left(d_{i}+(n-2)\left|d_{i}\right|\right)+(n-2) \epsilon .$$
Then for any $\lambda_{\alpha}(1 \leqslant \alpha \leqslant n-1)$ there exists a $d_{i_{\alpha}}$ with $1 \leqslant i_{\alpha} \leqslant n-1$ such that
$$\begin{gathered}
\left|\lambda_{\alpha}-d_{i_{\alpha}}\right|<\epsilon \\
0 \leqslant \lambda_{n}-\mathbf{a}<(n-1) \epsilon+\left|\sum_{\alpha=1}^{n-1}\left(d_{\alpha}-d_{i_{\alpha}}\right)\right| .
\end{gathered}$$
Proof. Without loss of generality, we assume $\sum_{i=1}^{n-1}\left|a_{i}\right|^{2}>0$ and $n \geqslant 3$ (otherwise we are done). Note that the eigenvalues have the order $\lambda_{1} \leqslant \lambda_{2} \leqslant \cdots \leqslant \lambda_{n}$, as in the assumption of lemma. It is well known that, for a Hermitian matrix, any diagonal element is less than or equals to the largest eigenvalue. In particular,
$$\lambda_{n} \geqslant \mathbf{a} .$$

We only need to prove (11.2), since (11.3) is a consequence of (11.2), (11.4) and
$$\sum_{i=1}^{n} \lambda_{i}=\operatorname{tr}(A)=\sum_{\alpha=1}^{n-1} d_{\alpha}+\mathbf{a} .$$

Let's denote $I=\{1,2, \cdots, n-1\}$. We divide the index set $I$ into two subsets:
$$\begin{gathered}
\mathbf{B}=\left\{\alpha \in I:\left|\lambda_{\alpha}-d_{i}\right| \geqslant \epsilon, \forall i \in I\right\}, \\
\mathbf{G}=I \backslash \mathbf{B}=\left\{\alpha \in I: \text { There exists } i \in I \text { such that }\left|\lambda_{\alpha}-d_{i}\right|<\epsilon\right\} .
\end{gathered}$$

To complete the proof, it suffices to prove $\mathbf{G}=I$ or equivalently $\mathbf{B}=\emptyset$. It is easy to see that for any $\alpha \in \mathbf{G}$, one has
$$\left|\lambda_{\alpha}\right|<\sum_{i=1}^{n-1}\left|d_{i}\right|+\epsilon .$$

Fix $\alpha \in \mathbf{B}$, we are going to give the estimate for $\lambda_{\alpha}$. The eigenvalue $\lambda_{\alpha}$ satisfies
$$\left(\lambda_{\alpha}-\mathbf{a}\right) \prod_{i=1}^{n-1}\left(\lambda_{\alpha}-d_{i}\right)=\sum_{i=1}^{n-1}\left|a_{i}\right|^{2} \prod_{j \neq i}\left(\lambda_{\alpha}-d_{j}\right) .$$
By the definition of B, for $\alpha \in \mathbf{B}$ one then has $\left|\lambda_{\alpha}-d_{i}\right| \geqslant \epsilon$ for any $i \in I$. We therefore derive
$$\left|\lambda_{\alpha}-\mathbf{a}\right| \leqslant \sum_{i=1}^{n-1} \frac{\left|a_{i}\right|^{2}}{\left|\lambda_{\alpha}-d_{i}\right|} \leqslant \frac{1}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}, \quad \text { if } \alpha \in \mathbf{B} .$$
Hence, for $\alpha \in \mathbf{B}$, we obtain
$$\lambda_{\alpha} \geqslant \mathbf{a}-\frac{1}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2} .$$

For a set $\mathbf{S}$, we denote $|\mathbf{S}|$ the cardinality of $\mathbf{S}$. We shall use proof by contradiction to prove $\mathbf{B}=\emptyset$. Assume by contradiction $\mathbf{B} \neq \emptyset$. Then $|\mathbf{B}| \geqslant 1$, and so $|\mathbf{G}|=n-1-|\mathbf{B}| \leqslant n-2$.

We compute the trace of the matrix $A$ as follows:
$$\begin{aligned}
\operatorname{tr}(A) & =\lambda_{n}+\sum_{\alpha \in \mathbf{B}} \lambda_{\alpha}+\sum_{\alpha \in \mathbf{G}} \lambda_{\alpha} \\
& \geqslant \lambda_{n}+|\mathbf{B}|\left(\mathbf{a}-\frac{1}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}\right)-|\mathbf{G}|\left(\sum_{i=1}^{n-1}\left|d_{i}\right|+\epsilon\right) \\
& >2 \mathbf{a}-\frac{1}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}-(n-2)\left(\sum_{i=1}^{n-1}\left|d_{i}\right|+\epsilon\right) \\
& \geqslant \sum_{i=1}^{n-1} d_{i}+\mathbf{a}=\operatorname{tr}(A),
\end{aligned}$$
where we use (11.1), (11.4), (11.6) and (11.9). This is a contradiction. We have $\mathbf{B}=\emptyset$. Therefore, $\mathbf{G}=I$ and the proof is complete. \(\square\)

Consequently we obtain
Lemma 11.2. Let $A(\mathbf{a})$ be an $n \times n$ Hermitian matrix
$$A(\mathbf{a})=\left(\begin{array}{ccccc}
d_{1} & & & & a_{1} \\
& d_{2} & & & a_{2} \\
& & \ddots & & \vdots \\
& & & d_{n-1} & a_{n-1} \\
\bar{a}_{1} & \bar{a}_{2} & \cdots & \bar{a}_{n-1} & \mathbf{a}
\end{array}\right)$$
with $d_{1}, \cdots, d_{n-1}, a_{1}, \cdots, a_{n-1}$ fixed, and with $\mathbf{a}$ variable. Assume that $d_{1}, d_{2}, \cdots, d_{n-1}$ are distinct with each other, i.e. $d_{i} \neq d_{j}, \forall i \neq j$. Denote $\lambda=\left(\lambda_{1}, \cdots, \lambda_{n}\right)$ as the the eigenvalues of $A(\mathbf{a})$. Given a positive constant $\epsilon$ with $0<\epsilon \leqslant \frac{1}{2} \min \left\{\left|d_{i}-d_{j}\right|: \forall i \neq\right.$ $j\}$, if the parameter a satisfies the quadratic growth condition
$$\mathbf{a} \geqslant \frac{1}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}+(n-1) \sum_{i=1}^{n-1}\left|d_{i}\right|+(n-2) \epsilon,$$
then the eigenvalues behave like
$$\begin{gathered}
\left|d_{\alpha}-\lambda_{\alpha}\right|<\epsilon, \forall 1 \leqslant \alpha \leqslant n-1, \\
0 \leqslant \lambda_{n}-\mathbf{a}<(n-1) \epsilon .
\end{gathered}$$
Proof. The proof is based on Lemma 11.1 and a deformation argument. Without loss of generality, we assume $n \geqslant 3$ and $\sum_{i=1}^{n-1}\left|a_{i}\right|^{2}>0$ (otherwise we are done). Moreover, we assume in addition that $d_{1}<d_{2} \cdots<d_{n-1}$ and the eigenvalues have the order $\lambda_{1} \leqslant \lambda_{2} \leqslant \cdots \leqslant \lambda_{n-1} \leqslant \lambda_{n}$.

Fix $\epsilon \in\left(0, \mu_{0}\right]$, where $\mu_{0}=\frac{1}{2} \min \left\{\left|d_{i}-d_{j}\right|: \forall i \neq j\right\}$. Denote
$$I_{i}=\left(d_{i}-\epsilon, d_{i}+\epsilon\right),$$
and
$$P_{0}=\frac{1}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}+(n-1) \sum_{i=1}^{n-1}\left|d_{i}\right|+(n-2) \epsilon .$$
Since $0<\epsilon \leqslant \mu_{0}$, the intervals disjoint each other
$$I_{\alpha} \bigcap I_{\beta}=\emptyset \text { for } 1 \leqslant \alpha<\beta \leqslant n-1 .$$

In what follows, we assume that the parameter a satisfies (11.11) and the Greek letters $\alpha, \beta$ range from 1 to $n-1$. Define a function
$$\mathbf{C a r d}_{\alpha}:\left[P_{0},+\infty\right) \rightarrow \mathbb{N}$$
to count the eigenvalues which lie in $I_{\alpha}$. (Note that when the eigenvalues are not distinct, the function $\mathbf{C a r d}_{\alpha}$ means the summation of all the algebraic multiplicities of distinct eigenvalues which lie in $I_{\alpha}$ ). This function measures the number of the eigenvalues which lie in $I_{\alpha}$.

We are going to prove that $\mathbf{C a r d}_{\alpha}$ is continuous on $\left[P_{0},+\infty\right)$. First, Lemma 11.1 asserts that if $\mathbf{a} \geqslant P_{0}$ then
$$\lambda_{\alpha} \in \bigcup_{i=1}^{n-1} I_{i}, \forall 1 \leqslant \alpha \leqslant n-1 .$$

It is well known that the largest eigenvalue $\lambda_{n} \geqslant \mathbf{a}$, while the smallest eigenvalue $\lambda_{1} \leqslant d_{1}$. Combining with (11.13) one has
$$\lambda_{n} \geqslant \mathbf{a}>\sum_{i=1}^{n-1}\left|d_{i}\right|+\epsilon .$$
Thus $\lambda_{n} \in \mathbb{R} \backslash\left(\bigcup_{i=1}^{n-1} \overline{I_{i}}\right)$ where $\overline{I_{i}}$ denotes the closure of $I_{i}$. Therefore, the function $\operatorname{Card}_{\alpha}$ is continuous (thus it is a constant), since (11.13), (11.12), $\lambda_{n} \in \mathbb{R} \backslash\left(\overline{\bigcup_{i=1}^{n-1} I_{i}}\right)$ and the eigenvalues of $A(\mathbf{a})$ depend continuously on the parameter a.

The continuity of $\operatorname{Card}_{\alpha}(\mathbf{a})$ plays a crucial role in this proof. Following the outline of the proof of [7, Lemma 1.2], in the setting of Hermitian matrices, one can show that for $1 \leqslant \alpha \leqslant n-1$,
$$\lim _{\mathbf{a} \rightarrow+\infty} \operatorname{Card}_{\alpha}(\mathbf{a}) \geqslant 1 .$$
It follows from (11.14), (11.15) and the continuity of $\mathbf{C a r d}_{\alpha}$ that
$$\operatorname{Card}_{\alpha}(\mathbf{a})=1, \forall \mathbf{a} \in\left[P_{0},+\infty\right), 1 \leqslant \alpha \leqslant n-1 .$$
Together with (11.13), we prove that, for any $1 \leqslant \alpha \leqslant n-1$, the interval $I_{\alpha}=$ $\left(d_{\alpha}-\epsilon, d_{\alpha}+\epsilon\right)$ contains the eigenvalue $\lambda_{\alpha}$. We thus complete the proof. \(\square\)

Suppose that there are two distinct indices $i_{0}, j_{0}\left(i_{0} \neq j_{0}\right)$ such that $d_{i_{0}}=d_{j_{0}}$. Then the characteristic polynomial of $A$ can be rewritten as the following
$$\left(\lambda-d_{i_{0}}\right)\left[(\lambda-\mathbf{a}) \prod_{i \neq i_{0}}\left(\lambda-d_{i}\right)-\left|a_{i_{0}}\right|^{2} \prod_{j \neq j_{0}, j \neq i_{0}}\left(\lambda-d_{j}\right)-\sum_{i \neq i_{0}}\left|a_{i}\right|^{2} \prod_{j \neq i, j \neq i_{0}}\left(\lambda-d_{j}\right)\right] .$$

So $\lambda_{i_{0}}=d_{i_{0}}$ is an eigenvalue of $A$ for any $a \in \mathbb{R}$. Notice that
$$(\lambda-\mathbf{a}) \prod_{i \neq i_{0}}\left(\lambda-d_{i}\right)-\left|a_{i_{0}}\right|^{2} \prod_{j \neq j_{0}, j \neq i_{0}}\left(\lambda-d_{j}\right)-\sum_{i \neq i_{0}}\left|a_{i}\right|^{2} \prod_{j \neq i, j \neq i_{0}}\left(\lambda-d_{j}\right)$$
is the characteristic polynomial of the $(n-1) \times(n-1)$ Hermitian matrix
$$\left(\begin{array}{ccccccc}
d_{1} & & & & & & a_{1} \\
& \ddots & & & & & \vdots \\
& & \widehat{d_{i_{0}}} & & & & \widehat{a_{i_{0}}} \\
& & & \ddots & & & \vdots \\
& & & d_{j_{0}} & & \left(\left|a_{j_{0}}\right|^{2}+\left|a_{i_{0}}\right|^{2}\right)^{\frac{1}{2}} \\
\bar{a}_{1} & \cdots & \widehat{\bar{a}_{i_{0}}} & \cdots & \left(\left|a_{j_{0}}\right|^{2}+\left|a_{i_{0}}\right|^{2}\right)^{\frac{1}{2}} & \cdots & \underline{a}
\end{array}\right)$$
where $\widehat{*}$ indicates deletion. Therefore, $\left(\lambda_{1}, \cdots, \widehat{\lambda_{i_{0}}}, \cdots, \lambda_{n}\right)$ are the eigenvalues of the above $(n-1) \times(n-1)$ Hermitian matrix. Hence, we obtain

Lemma 11.3. Let $A$ be as in Lemma 3.12 an $n \times n$ Hermitian matrix. Let
$$I= \begin{cases}\mathbb{R}^{+}=(0,+\infty) & \text { if } d_{i}=d_{1}, \forall 2 \leqslant i \leqslant n-1, \\ \left(0, \mu_{0}\right), \mu_{0}=\frac{1}{2} \min \left\{\left|d_{i}-d_{j}\right|: d_{i} \neq d_{j}\right\} & \text { otherwise. }\end{cases}$$
Denote $\lambda=\left(\lambda_{1}, \cdots, \lambda_{n}\right)$ the the eigenvalues of $A$. Fix $\epsilon \in \mathcal{I}$. Suppose that the parameter $\mathbf{a}$ in $A$ satisfies (11.11). Then the eigenvalues behave like
$$\left|d_{\alpha}-\lambda_{\alpha}\right|<\epsilon, \forall 1 \leqslant \alpha \leqslant n-1,0 \leqslant \lambda_{n}-\mathbf{a}<(n-1) \epsilon .$$

Applying Lemmas 11.1 and 11.3, we complete the proof of Lemma 3.12 without restriction to the applicable scope of $\epsilon$.

Proof of Lemma 3.12. We follow the outline of the proof of Lemma 11.2. Without loss of generality, we may assume
$$n \geqslant 3, \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}>0, d_{1} \leqslant d_{2} \leqslant \cdots \leqslant d_{n-1} \text { and } \lambda_{1} \leqslant \lambda_{2} \leqslant \cdots \lambda_{n-1} \leqslant \lambda_{n} .$$

Fix $\epsilon>0$. Let $I_{\alpha}^{\prime}=\left(d_{\alpha}-\frac{\epsilon}{2 n-3}, d_{\alpha}+\frac{\epsilon}{2 n-3}\right)$ and
$$P_{0}^{\prime}=\frac{2 n-3}{\epsilon} \sum_{i=1}^{n-1}\left|a_{i}\right|^{2}+(n-1) \sum_{i=1}^{n-1}\left|d_{i}\right|+\frac{(n-2) \epsilon}{2 n-3} .$$
In what follows we assume (3.17) holds. The connected components of $\bigcup_{\alpha=1}^{n-1} I_{\alpha}^{\prime}$ are denoted as in the following:
$$J_{1}=\bigcup_{\alpha=1}^{j_{1}} I_{\alpha}^{\prime}, J_{2}=\bigcup_{\alpha=j_{1}+1}^{j_{2}} I_{\alpha}^{\prime}, \cdots, J_{i}=\bigcup_{\alpha=j_{i-1}+1}^{j_{i}} I_{\alpha}^{\prime}, \cdots, J_{m}=\bigcup_{\alpha=j_{m-1}+1}^{n-1} I_{\alpha}^{\prime} .$$
Moreover
$$J_{i} \bigcap J_{k}=\emptyset \text {, for } 1 \leqslant i<k \leqslant m \text {. }$$

It plays formally the role of (11.12) in the proof of Lemma 11.2.
As in the proof of Lemma 11.2, let
$${\widetilde{\mathbf{C a r d}_{k}}}_{k}:\left[P_{0}^{\prime},+\infty\right) \rightarrow \mathbb{N}$$
be the function counting the eigenvalues that lie in $J_{k}$. (Note that when the eigenvalues are not distinct, the function $\widehat{\text { Card }}_{k}$ denotes the summation of all the algebraic multiplicities of distinct eigenvalues which lie in $J_{k}$ ). By Lemma 11.1 and
$$\lambda_{n} \geqslant \mathbf{a} \geqslant P_{0}^{\prime}>\sum_{i=1}^{n-1}\left|d_{i}\right|+\frac{\epsilon}{2 n-3},$$
we conclude that if the parameter a satisfies the growth condition (3.17) then
$$\lambda_{n} \in \mathbb{R} \backslash\left(\bigcup_{k=1}^{n-1} \overline{I_{k}^{\prime}}\right)=\mathbb{R} \backslash\left(\bigcup_{i=1}^{m} \overline{J_{i}}\right), \lambda_{\alpha} \in \bigcup_{i=1}^{n-1} I_{i}^{\prime}=\bigcup_{i=1}^{m} J_{i} \text { for } 1 \leqslant \alpha \leqslant n-1 .$$
Similarly, ${\widetilde{\mathbf{C a r d}_{i}}}_{(\mathbf{a})}$ is a continuous function with respect to the variable a when $\mathbf{a} \geqslant P_{0}^{\prime}$. So it is a constant. Combining it with Lemma 11.3, we see that
$$\widehat{\operatorname{Card}}_{i}(\mathbf{a})=j_{i}-j_{i-1}$$
for $\mathbf{a} \geqslant P_{0}^{\prime}$. Here we denote $j_{0}=0$ and $j_{m}=n-1$. We thus know that
$$\lambda_{j_{i-1}+1}, \lambda_{j_{i-1}+2}, \cdots, \lambda_{j_{i}}$$
lie in the connected component $J_{i}$. Thus, for any $j_{i-1}+1 \leqslant \gamma \leqslant j_{i}$, we see $I_{\gamma}^{\prime} \subset J_{i}$ and $\lambda_{\gamma}$ lies in the connected component $J_{i}$. Therefore,
$$\left|\lambda_{\gamma}-d_{\gamma}\right|<\frac{\left(2\left(j_{i}-j_{i-1}\right)-1\right) \epsilon}{2 n-3} \leqslant \epsilon .$$
Here we use the fact that $d_{\gamma}$ is the midpoint of $I_{\gamma}^{\prime}$ and $J_{i} \subset \mathbb{R}$ is an open subset.
To be brief, if for fixed index $1 \leqslant i \leqslant n-1$ the eigenvalue $\lambda_{i}\left(P_{0}^{\prime}\right)$ lies in $J_{\alpha}$ for some $\alpha$, then Lemma 11.1 implies that, for any $\mathbf{a}>P_{0}^{\prime}$, the corresponding eigenvalue $\lambda_{i}(\mathbf{a})$ lies in the same interval $J_{\alpha}$. The computation of $\widetilde{\mathbf{C a r d}}_{k}$ can be done by setting $\mathbf{a} \rightarrow+\infty$. \(\square\)

Acknowledgements. The author was partially supported by the National Natural Science Foundation of China (Grant No. 11801587), Guangzhou Science and Technology Program (Grant No. 202201010451), and Guangdong Basic and Applied Basic Research Foundation (Grant No. 2023A1515012121).