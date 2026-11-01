---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: Limit behavior of the twistedconicalKähler-Ricci flow with change in...]

Proposition 4.2. For any $0<T<T_{\text {max }}^{\eta}$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$\log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma} \leqslant \frac{C}{t^{2}} .$$
for all $t \in(0, T]$ and $0<\gamma \ll 1$.
Proof. For any $0<\delta<T$ and $0<\epsilon \ll 1$, we define
$$L_{\gamma}(t)=(t-\delta) \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-A\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right)+A(t-\tau)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)+A n \log (t-\delta)+\epsilon \log |s|_{h}^{2},$$
where $A$ is a large positive uniform constant to be determined later, $\tau$ is a fixed uniform positive constant satisfying
$$(1-\tau) \omega+\tau \nu_{\gamma} \geqslant(1-\tau-C \tau) \omega \geqslant \frac{\omega}{2} \quad \text { and } \quad \tau \leqslant \sigma$$
for all $0<\gamma \ll 1$, and $\sigma$ is the constant in Corollary 3.11.
First, by Chern-Lu inequality [15, 45] (see also Proposition 7.1 in [26]), in $M \backslash D$, we have
$$\Delta_{\omega_{\gamma}(t)} \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma} \geqslant \frac{\left(\operatorname{Ric}\left(\omega_{\gamma}(t)\right), \omega_{\gamma}\right)_{\omega_{\gamma}(t)}}{\operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}}-C \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma},$$
where (, $)_{\omega_{\gamma}(t)}$ is the inner product with respect to $\omega_{\gamma}(t)$ and the constant $C$ depends on the upper bound on the holomorphic bisectional curvature of $\omega_{\gamma}$ which is uniformly bounded by Lemma 4.1. In $M \backslash D$, we also have
$$\frac{\partial}{\partial t} \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}=\frac{\left(\operatorname{Ric}\left(\omega_{\gamma}(t)\right)-\eta, \omega_{\gamma}\right)_{\omega_{\gamma}(t)}}{\operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}} .$$
By using (4.4) and (4.5), we have
$$\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma}(t)}\right) \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma} \leqslant C \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+C,$$
where constant $C$ independent of $\gamma$. Then direct computations combining with Corollary 3.11 show that
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma}(t)}\right) L_{\gamma}(t) \leqslant & \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+C \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-A\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)+A \Delta_{\omega_{\gamma}(t)} \varphi_{\gamma}(t)+\frac{A n}{t-\delta} \\
& -A t \Delta_{\omega_{\gamma}(t)} \psi_{\gamma}+A\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)+A(t-\tau) \operatorname{tr}_{\omega_{\gamma}(t)} \nu_{\gamma}+\epsilon \operatorname{tr}_{\omega_{\gamma}(t)} \theta \\
& +A(t-\tau) \Delta_{\omega_{\gamma}(t)} \psi_{\gamma}+C \\
\leqslant & \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+C \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+A n-A \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma t}-A \tau \Delta_{\omega_{\gamma}(t)} \psi_{\gamma}+\frac{A n}{t-\delta} \\
& +A(t-\tau) \operatorname{tr}_{\omega_{\gamma}(t)} \nu_{\gamma}+\epsilon \operatorname{tr}_{\omega_{\gamma}(t)} \theta+C \\
\leqslant & \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+C \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+A n+C+\epsilon \operatorname{tr}_{\omega_{\gamma}(t)} \theta+\frac{A n}{t-\delta} \\
& -A \operatorname{tr}_{\omega_{\gamma}(t)}\left(\omega+\tau \nu_{\gamma}+\tau \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}\right) .
\end{aligned}$$
We first deal with the last term in above inequality. By (4.3), there holds
$$\omega+\tau \nu_{\gamma}+\tau \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}=(1-\tau) \omega+\tau \nu_{\gamma}+\tau\left(\omega+\sqrt{-1} \partial \bar{\partial} \psi_{\gamma}\right) \geqslant \frac{\omega}{2}+\tau \omega_{\gamma} .$$
Hence
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\omega_{\gamma}(t)}\right) L_{\gamma}(t) \leqslant & \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+C \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-A \tau \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+\frac{C}{t-\delta} \\
& +\operatorname{tr}_{\omega_{\gamma}(t)}\left(\epsilon \theta-\frac{A}{2} \omega\right) \\
\leqslant & \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-2 \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+\frac{C}{t-\delta} \\
\leqslant & -\operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}+\frac{C}{t-\delta},
\end{aligned}$$
where we choose $A$ large enough in the second inequality, and we use $-x+\log x \leqslant 0$ on $(0,+\infty)$ in the last inequality.

Let $\left(t_{0}, x_{0}\right)$ be the maximum point of $L_{\gamma}(t)$ on $[\delta, T] \times(X \backslash D)$. From the authors' result ((3.58) in [42]), there exists a constant $C_{\gamma}$ such that for any $t \in[\delta, T]$,
$$\frac{1}{C_{\gamma}} \omega_{\gamma} \leqslant \omega_{\gamma}(t) \leqslant C_{\gamma} \omega_{\gamma} .$$
Combining this with Proposition 3.12, Corollaries 3.3 and 3.11, we have
$$\begin{aligned}
L_{\gamma}(t) & \leqslant T \log \left(C_{\gamma} n\right)+A n \log (t-\delta)-\frac{A \tau}{\sigma} n \log t+C+\epsilon \log |s|_{h}^{2} \\
& \leqslant T \log \left(C_{\gamma} n\right)+A n \log (t-\delta)-\frac{A \tau}{\sigma} n \log \delta+C+\epsilon \log |s|_{h}^{2} .
\end{aligned}$$
We conclude that $L_{\gamma}(t)$ tends to $-\infty$ as $x \rightarrow D$ or $x \rightarrow \delta$, hence the maximum point $\left(t_{0}, x_{0}\right)$ of $L_{\gamma}(t)$ must be in $(\delta, T] \times(X \backslash D)$. By the maximum principle, at $\left(t_{0}, x_{0}\right)$, we have
$$\operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma} \leqslant \frac{C}{t-\delta}+C,$$
where $C$ is a constant depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$. Then by using Propositions 3.1 and 3.12, and Corollaries 3.3 and 3.11 again, since $\tau \leqslant \sigma$, we have
$$\begin{aligned}
& (t-\delta) \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-\frac{C}{t-\delta}+A n \log (t-\delta)+\epsilon \log |s|_{h}^{2}-C \\
\leqslant & (t-\delta) \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-\frac{C}{t}+A n \log (t-\delta)+\epsilon \log |s|_{h}^{2}-C
\end{aligned}$$
$$\begin{aligned}
& \leqslant(t-\delta) \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}-A\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right)+A(t-\tau)\left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}\right)+A n \log (t-\delta)+\epsilon \log |s|_{h}^{2} \\
& \leqslant\left(t_{0}-\delta\right) \log \frac{C}{t_{0}-\delta}-\frac{A \tau}{\sigma} n \log t_{0}+A n \log \left(t_{0}-\delta\right)+\epsilon \log |s|_{h}^{2}\left(x_{0}\right)+C \\
& \leqslant-\left(t_{0}-\delta\right) \log \left(t_{0}-\delta\right)+\left(1-\frac{\tau}{\sigma}\right) A n \log \left(t_{0}-\delta\right)+\epsilon \log |s|_{h}^{2}\left(x_{0}\right)+C \\
& \leqslant\left(1-\frac{\tau}{\sigma}\right) A n \log T+C
\end{aligned}$$
and so
$$(t-\delta) \log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma} \leqslant \frac{C}{t-\delta}+C-\epsilon \log |s|_{h}^{2} \quad \text { in } \quad X \backslash D,$$
where $C$ is a constant depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$. After letting $\epsilon \rightarrow 0$, we have
$$\log \operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma} \leqslant \frac{C}{(t-\delta)^{2}} \quad \text { in } \quad X \backslash D .$$
Then we complete the proof after we let $\delta \rightarrow 0$. \(\square\)

Remark 4.3. The constant $\tau$ in the definition of $L_{\gamma}(t)$ in (4.2) can be chosen to be equal to $\sigma$ in Corollary 3.11. In fact, by the choosing of $\sigma$ in (3.35), we can also choose $\sigma$ satisfying (4.3).

Corollary 4.4. For any $0<T<T_{\text {max }}^{\eta}$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$e^{-\frac{C}{t^{2}}} \omega_{\gamma} \leqslant \omega_{\gamma}(t) \leqslant e^{\frac{C}{t^{2}}} \omega_{\gamma} \quad \text { in } \quad X \backslash D$$
for all $t \in(0, T]$ and $0<\gamma \ll 1$.
Proof. From Proposition 4.2, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n$, $\omega, \theta, \eta$ and $T$ such that for any $t \in(0, T]$ and $0<l \ll 1$,
$$\operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma} \leqslant e^{\frac{C}{t^{2}}} \quad \text { in } \quad X \backslash D .$$
Since
$$\operatorname{tr}_{\omega_{\gamma}} \omega_{\gamma}(t) \leqslant n\left(\frac{\omega_{\gamma}^{n}(t)}{\omega_{\gamma}^{n}}\right)\left(\operatorname{tr}_{\omega_{\gamma}(t)} \omega_{\gamma}\right)^{n-1}$$
and
$$\begin{aligned}
\frac{\omega_{\gamma}^{n}(t)}{\omega_{\gamma}^{n}} & =\exp \left(\dot{\varphi}_{\gamma}(t)-\log \frac{\omega_{\gamma}^{n}}{\omega^{n}}-h-(1-\gamma) \log |s|_{h}^{2}\right) \\
& =\exp \left(\dot{\varphi}_{\gamma}(t)-\psi_{\gamma}-\log \frac{\omega_{\gamma}^{n}}{\omega^{n}}-h-(1-\gamma) \log |s|_{h}^{2}+\psi_{\gamma}\right) \\
& \leqslant e^{\frac{C}{t}},
\end{aligned}$$
where we use (2.29) and Corollary 3.3 in the last inequality, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that for any $t \in(0, T]$ and $0<l \ll 1$,
$$\operatorname{tr}_{\omega_{\gamma}} \omega_{\gamma}(t) \leqslant e^{\frac{C}{t^{2}}} \quad \text { in } \quad X \backslash D .$$
Combining (4.17) and (4.20), we obtain (4.16). \(\square\)

Therefore, for any $0<\delta<T<T_{\text {max }}^{\eta}$ and $K \subset \subset X \backslash D$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta, \delta, T$ and $\operatorname{dist}_{\omega}(K, D)$ such that
$$\omega \leqslant \omega_{\gamma}(t) \leqslant \omega \quad \text { on } \quad[\delta, T] \times K .$$
Then Evans-Krylov-Safonov's estimates (see [31]) imply the high order uniform estimates.

Proposition 4.5. For any $0<\delta<T<T_{\text {max }}^{\eta}, k \in \mathbb{N}^{+}$and $K \subset \subset X \backslash D$, there exist uniform constants $C_{k}$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, k, n, \omega, \theta, \eta, \delta, T$ and $\operatorname{dist}_{\omega}(K, D)$, such that for any $0<\gamma \ll 1$,
$$\left\|\varphi_{\gamma}(t)\right\|_{C^{k}([\delta, T] \times K)} \leqslant C_{k} .$$

\section*{5. Existence}

In this section, we show the limit behavior flow of the conical Kähler-Ricci flow $\left(C K R F_{\gamma}^{\eta}\right)$ as its cone angle tends to zero. We prove the following convergence theorem.

Theorem 5.1. As the cone angle tends to 0, there exists a subsequence $\left(C K R F_{\gamma_{i}}^{\eta}\right)$ of the twisted conical Kähler-Ricci flow converging locally in the smooth sense outside the divisor and globally in the sense of currents to a Kähler-Ricci flow
$$\left\{\begin{array}{l}
\frac{\partial \omega(t)}{\partial t}=-\operatorname{Ric}(\omega(t))+[D]+\eta \\
\left.\omega(t)\right|_{t=0}=\hat{\omega}
\end{array},\right.$$
which exists on $\left[0, T_{\text {max }}^{\eta}\right) \times X$ in the following sense.
\begin{itemize}
\item[-] For any $0<T<T_{\text {max }}^{\eta}$, there exists a constant $C$ such that for any $t \in(0, T)$,
$$e^{-\frac{C}{t^{2}}} \omega_{o} \leqslant \omega(t) \leqslant e^{\frac{C}{t^{2}}} \omega_{o} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T_{\text {max }}^{\eta}\right) \times(X \backslash D), \omega(t)$ satisfies the smooth twisted Kähler-Ricci flow
$$\frac{\partial \omega(t)}{\partial t}=-\operatorname{Ric}(\omega(t))+\eta ;$$
\item[-] On $\left(0, T_{\max }^{\eta}\right) \times X, \omega(t)$ satisfies Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ in the sense of currents;
\item[-] There exists a metric potential $\varphi(t) \in \mathcal{C}^{\infty}\left(\left(0, T_{\max }^{\eta}\right) \times(X \backslash D)\right)$ with respect to $\omega_{t}$ such that $\omega(t)=\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi(t)$,
$$\lim _{t \rightarrow 0^{+}}\left\|\varphi(t)-\varphi_{0}\right\|_{L^{1}(X)}=0 \quad \text { and } \quad \lim _{t \rightarrow 0^{+}} \varphi(t)=\varphi_{0} \quad \text { in } \quad X \backslash D ;$$
\item[-] $O n\left[0, T_{\text {max }}^{\eta}\right),\left\|\varphi(t)-t \psi_{o}\right\|_{L^{\infty}(X)} \leqslant C$;
\item[-] For any $0<T<T_{\text {max }}^{\eta}$, there exist constants a and $C$ such that for any $t \in(0, T)$,
$$-C+a \log t \leqslant \dot{\varphi}(t)-\psi_{o} \leqslant \frac{C}{t} .$$
\end{itemize}
Proof. For any $[\delta, T] \times K \subset \subset\left(0, T_{\text {max }}^{\eta}\right) \times(X \backslash D)$, it is easy to see that $[\delta, T] \times K \subset \subset\left(0, T_{\gamma, \text { max }}^{\eta}\right) \times$ $(X \backslash D)$ for $0<\gamma \ll 1$. Then for any $k \in \mathbb{N}^{+},\left\|\varphi_{\gamma}(t)\right\|_{C^{k}([\delta, T] \times K)}$ is uniformly bounded according to Proposition 4.5. Let $\delta$ approximate to $0, T$ approximate to $T_{\max }^{\eta}$ and $K$ approximate to $X \backslash D$, by diagonal rule, we get a sequence $\left\{\gamma_{i}\right\}$, such that $\varphi_{\gamma_{i}}(t)$ converges in $C_{\text {loc }}^{\infty}$-topology in $\left(0, T_{\text {max }}^{\eta}\right) \times$ $(X \backslash D)$ to a function $\varphi(t)$ which is smooth in $\left(0, T_{\max }^{\eta}\right) \times(X \backslash D)$ and satisfies equation
$$\frac{\partial \varphi(t)}{\partial t}=\log \frac{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi(t)\right)^{n}}{\omega^{n}}+h+\log |s|_{h}^{2} .$$
Combining these arguments with Corollary 4.4, for any $0<T<T_{\text {max }}^{\eta}$, there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that for any $t \in(0, T]$,
$$e^{-\frac{C}{t^{2}}} \omega_{o} \leqslant \omega(t)=\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi(t) \leqslant e^{\frac{C}{t^{2}}} \omega_{o} \text { in } X \backslash D .$$
Hence we prove the first two conditions, and the last two conditions follow from Propositions 3.1 and 3.12, and Corollaries 3.3 and 3.11.

Next, we prove that $\omega(t)$ satisfies equation $\left(C K R F_{0}^{\eta}\right)$ in the sense of currents on $\left(0, T_{\text {max }}^{\eta}\right) \times X$. Let $\zeta:=\zeta(t, x)$ be a smooth $(n-1, n-1)$-form with compact support in $\left(0, T_{\text {max }}^{\eta}\right) \times X$. Without loss of generality, we assume that its compact support is included in $(\delta, T) \times X\left(0<\delta<T<T_{\text {max }}^{\eta}\right)$.

By using the definitions (2.22), (2.30) and the Dominated convergence theorem, we have
$$\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \zeta \xrightarrow{\gamma \rightarrow 0} \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \zeta .$$
On $[\delta, T] \times(X \backslash D)$, since $\log \frac{\omega_{\gamma}^{n}(t)}{\omega^{n}}+(1-\gamma) \log |s|_{h}^{2}-\psi_{\gamma}, \log \frac{\omega^{n}(t)}{\omega^{n}}+\log |s|_{h}^{2}-\psi_{o}, \varphi_{\gamma}(t)-t \psi_{\gamma}$ and $\varphi(t)-t \psi_{o}$ are uniformly bounded, by using the Dominated convergence theorem and integration by parts, we have
$$\begin{aligned}
& \int_{X} \frac{\partial \omega_{\gamma}(t)}{\partial t} \wedge \zeta=\int_{X}\left(\nu_{\gamma}+\sqrt{-1} \partial \bar{\partial} \frac{\partial \varphi_{\gamma}(t)}{\partial t}\right) \wedge \zeta \\
& =\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\frac{\partial \varphi_{\gamma}(t)}{\partial t}-\psi_{\gamma}\right) \wedge \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \zeta+\int_{X} \nu_{\gamma} \wedge \zeta \\
& =\int_{X}\left(\frac{\partial \varphi_{\gamma}(t)}{\partial t}-\psi_{\gamma}\right) \sqrt{-1} \partial \bar{\partial} \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \zeta+\int_{X} \nu_{\gamma} \wedge \zeta \\
& =\int_{X}\left(\log \frac{\omega_{\gamma}^{n}(t)}{\omega^{n}}+(1-\gamma) \log |s|_{h}^{2}+h-\psi_{\gamma}\right) \sqrt{-1} \partial \bar{\partial} \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \zeta+\int_{X} \nu_{\gamma} \wedge \zeta \\
& \xrightarrow{\gamma \rightarrow 0} \int_{X}\left(\log \frac{\omega^{n}(t)}{\omega^{n}}+\log |s|_{h}^{2}+h-\psi_{o}\right) \sqrt{-1} \partial \bar{\partial} \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \zeta+\int_{X} \nu \wedge \zeta \\
& =\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\log \frac{\omega^{n}(t)}{\omega^{n}}+\log |s|_{h}^{2}+h-\psi_{o}\right) \wedge \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \zeta+\int_{X} \nu \wedge \zeta \\
& =\int_{X}(-\operatorname{Ric}(\omega(t))+[D]+\eta) \wedge \zeta .
\end{aligned}$$
At the same time, there also holds
$$\begin{aligned}
\int_{X} \omega_{\gamma}(t) \wedge \frac{\partial \zeta}{\partial t} & =\int_{X}\left(\omega+t \nu_{\gamma}\right) \wedge \frac{\partial \zeta}{\partial t}+\int_{X} \sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}(t) \wedge \frac{\partial \zeta}{\partial t} \\
& =\int_{X}\left(\omega+t \nu_{\gamma}\right) \wedge \frac{\partial \zeta}{\partial t}+\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right) \wedge \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \frac{\partial \zeta}{\partial t} \\
& =\int_{X}\left(\omega+t \nu_{\gamma}\right) \wedge \frac{\partial \zeta}{\partial t}+\int_{X}\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right) \sqrt{-1} \partial \bar{\partial} \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \frac{\partial \zeta}{\partial t} \\
& \xrightarrow{\gamma \rightarrow 0} \int_{X}(\omega+t \nu) \wedge \frac{\partial \zeta}{\partial t}+\int_{X}\left(\varphi(t)-t \psi_{o}\right) \sqrt{-1} \partial \bar{\partial} \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \frac{\partial \zeta}{\partial t} \\
& =\int_{X}(\omega+t \nu) \wedge \frac{\partial \zeta}{\partial t}+\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\varphi(t)-t \psi_{o}\right) \wedge \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \frac{\partial \zeta}{\partial t} \\
& =\int_{X} \omega(t) \wedge \frac{\partial \zeta}{\partial t} .
\end{aligned}$$
On the other hand,
$$\begin{aligned}
\frac{\partial}{\partial t} \int_{X} \omega_{\gamma}(t) \wedge \zeta= & \int_{X} \omega_{\gamma}(t) \wedge \frac{\partial \zeta}{\partial t}+\int_{X}\left(\nu_{\gamma}+\sqrt{-1} \partial \bar{\partial} \frac{\partial \varphi_{\gamma}(t)}{\partial t}\right) \wedge \zeta \\
= & \int_{X} \omega_{\gamma t} \wedge \frac{\partial \zeta}{\partial t}+\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right) \wedge \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \frac{\partial \zeta}{\partial t} \\
& +\int_{X} \nu_{\gamma} \wedge \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\frac{\partial \varphi_{\gamma}(t)}{\partial t}-\psi_{\gamma}\right) \wedge \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \zeta
\end{aligned}$$
$$\begin{aligned}
&= \int_{X} \omega_{\gamma t} \wedge \frac{\partial \zeta}{\partial t}+\int_{X}\left(\varphi_{\gamma}(t)-t \psi_{\gamma}\right) \sqrt{-1} \partial \bar{\partial} \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \frac{\partial \zeta}{\partial t} \\
&+\int_{X} \nu_{\gamma} \wedge \zeta+\int_{X}\left(\frac{\partial \varphi_{\gamma}(t)}{\partial t}-\psi_{\gamma}\right) \sqrt{-1} \partial \bar{\partial} \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \wedge \zeta \\
& \xrightarrow{\gamma \rightarrow 0} \int_{X} \omega_{t} \wedge \frac{\partial \zeta}{\partial t}+\int_{X}\left(\varphi(t)-t \psi_{o}\right) \sqrt{-1} \partial \bar{\partial} \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \frac{\partial \zeta}{\partial t} \\
&+\int_{X} \nu \wedge \zeta+\int_{X}\left(\frac{\partial \varphi(t)}{\partial t}-\psi_{o}\right) \sqrt{-1} \partial \bar{\partial} \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \zeta \\
&= \int_{X} \omega_{t} \wedge \frac{\partial \zeta}{\partial t}+\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\varphi(t)-t \psi_{o}\right) \wedge \frac{\partial \zeta}{\partial t}+t \int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \frac{\partial \zeta}{\partial t} \\
&+\int_{X} \nu \wedge \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial}\left(\frac{\partial \varphi(t)}{\partial t}-\psi_{o}\right) \wedge \zeta+\int_{X} \sqrt{-1} \partial \bar{\partial} \psi_{o} \wedge \zeta \\
&= \int_{X} \omega(t) \wedge \frac{\partial \zeta}{\partial t}+\int_{X} \frac{\partial \omega(t)}{\partial t} \wedge \frac{\partial \zeta}{\partial t} \\
&= \frac{\partial}{\partial t} \int_{X} \omega(t) \wedge \zeta .
\end{aligned}$$
Combining equality
$$\frac{\partial}{\partial t} \int_{X} \omega_{\gamma}(t) \wedge \zeta=\int_{X} \frac{\partial \omega_{\gamma}(t)}{\partial t} \wedge \zeta+\int_{X} \omega_{\gamma}(t) \wedge \frac{\partial \zeta}{\partial t}$$
with equalities (5.8)-(5.10), on $[\delta, T]$, we have
$$\frac{\partial}{\partial t} \int_{X} \omega(t) \wedge \zeta=\int_{X}(-\operatorname{Ric}(\omega(t))+[D]+\eta) \wedge \zeta+\int_{X} \omega(t) \wedge \frac{\partial \zeta}{\partial t} .$$
Since $\operatorname{Supp} \zeta \subset(\delta, T) \times X$, we have
$$\int_{0}^{T_{\max }^{\eta}} \frac{d}{d t} \int_{X} \omega(t) \wedge \zeta d t=0$$
Then integrating form 0 to $\infty$ on both sides of equation (5.12),
$$\begin{aligned}
\int_{\left(0, T_{\text {max }}^{\eta}\right) \times X} \frac{\partial \omega(t)}{\partial t} \wedge \zeta d t & =-\int_{\left(0, T_{\text {max }}^{\eta}\right) \times X} \omega(t) \wedge \frac{\partial \zeta}{\partial t} d t=-\int_{0}^{T_{\text {max }}^{\eta}} \int_{X} \omega(t) \wedge \frac{\partial \zeta}{\partial t} d t \\
& =\int_{0}^{T_{\text {max }}^{\eta}} \int_{X}(-\operatorname{Ric}(\omega(t))+[D]+\eta) \wedge \zeta d t \\
& =\int_{\left(0, T_{\text {max }}^{\eta}\right) \times X}(-\operatorname{Ric}(\omega(t))+[D]+\eta) \wedge \zeta d t .
\end{aligned}$$
By the arbitrariness of $\zeta$, we prove that $\omega(t)$ satisfies Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ in the sense of currents on $\left(0, T_{\text {max }}^{\eta}\right) \times X$. We complete the proof of the third condition.

At last, we prove $\varphi(t)$ we just obtained converges to $\varphi_{0}$ globally in $L^{1}$-sense and point-wise in $X \backslash D$ as $t \rightarrow 0$. In [42], the authors and Zhang prove that
$$\lim _{t \rightarrow 0^{+}}\left\|\varphi_{\gamma}(t)-\varphi_{0}\right\|_{L^{1}(X)}=0 \quad \text { and } \quad \lim _{t \rightarrow 0^{+}} \varphi_{\gamma}(t)=\varphi_{0} \quad \text { in } \quad X \backslash D .$$
But all these limits depend on $\gamma$, so we can not let $\gamma$ tends to 0 directly. We need some new arguments to show the limit behavior of $\varphi(t)$ near $t=0$. More precisely, our method is to construct super-solution and sub-solution and then to study the limit behavior of these solutions near $t=0$.

We first give an upper bound on $\varphi(t)$. Fix $\varepsilon>0$, we consider the smooth parabolic Monge-Ampère equation
$$\left\{\begin{array}{l}
\frac{\partial \varphi_{\varepsilon j}(t)}{\partial t}=\log \frac{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\varepsilon j}(t)\right)^{n}}{\omega^{n}}+h+\log \left(\varepsilon^{2}+|s|_{h}^{2}\right) \\
\left.\varphi_{\varepsilon j}(t)\right|_{t=0}=\varphi_{j}
\end{array},\right.$$
where $\varphi_{j}$ is the smooth strictly $\omega$-psh function decreasing to $\varphi_{0}$ as $j \nearrow \infty$ in (2.42). From Tsuji [71] and Tian-Zhang's [67] results, there exists a unique smooth solution $\varphi_{\varepsilon j}(t)$ on $[0, T] \times X$ with $0<T<T_{\text {max }}^{\eta}$ for all $j$.

Proposition 5.2. In $(0, T] \times(X \backslash D)$, we have
$$\varphi_{\gamma}(t)+t \gamma \log |s|_{h}^{2} \leqslant \varphi_{\varepsilon j}(t)$$
for all $0<\gamma \ll 1$.
Proof. For any $0<\delta<T$, we consider the function
$$Z(t)=\varphi_{\gamma}(t)+t \gamma \log |s|_{h}^{2}-\varphi_{\varepsilon j}(t) \quad \text { on } \quad[\delta, T] \times X .$$
Direct computations show that, in $X \backslash D$,
$$\begin{aligned}
\frac{\partial}{\partial t} Z(t) & =\log \frac{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial}\left(\varphi_{\gamma}(t)+t \gamma \log |s|_{h}^{2}\right)\right)^{n}}{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\varepsilon j}(t)\right)^{n}}+\log |s|_{h}^{2}-\log \left(\varepsilon^{2}+|s|_{h}^{2}\right) \\
& \leqslant \log \frac{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial}\left(\varphi_{\gamma}(t)+t \gamma \log |s|_{h}^{2}\right)\right)^{n}}{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\varepsilon j}(t)\right)^{n}} \\
& =\log \frac{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\varepsilon j}(t)+\sqrt{-1} \partial \bar{\partial} Z(t)\right)^{n}}{\left(\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{\varepsilon j}(t)\right)^{n}} .
\end{aligned}$$
Let $\left(t_{0}, x_{0}\right)$ be the maximum point of $Z(t)$ on $[\delta, T] \times X$. Since $Z(t)$ tends to $-\infty$ as $x \rightarrow D, x_{0}$ must be in $X \backslash D$. Then by the maximum principle $t_{0}=\delta$, which implies that
$$\varphi_{\gamma}(t)+t \gamma \log |s|_{h}^{2}-\varphi_{\varepsilon j}(t) \leqslant \sup _{X}\left(\varphi_{\gamma}(\delta)+\delta \gamma \log |s|_{h}^{2}-\varphi_{\varepsilon j}(\delta)\right) \leqslant \sup _{X}\left(\varphi_{\gamma}(\delta)-\varphi_{\varepsilon j}(\delta)\right) .$$
It follow from Hartogs' Lemma that, as $\delta \rightarrow 0$,
$$\sup _{X}\left(\varphi_{\gamma}(\delta)-\varphi_{\varepsilon j}(\delta)\right) \rightarrow \sup _{X}\left(\varphi_{0}-\varphi_{j}\right) \leqslant 0,$$
we obtain (5.16) after letting $\delta \rightarrow 0$ in (5.19). \(\square\)

We obtain an upper bound for $\varphi(t)$ if we let $\gamma \rightarrow 0$ in (5.16).
Corollary 5.3. In $(0, T] \times(X \backslash D)$, we have
$$\varphi(t) \leqslant \varphi_{\varepsilon j}(t) .$$

For the lower bound on $\varphi(t)$, we construct a sub-solution to derive it.
Proposition 5.4. There exists a uniform constant $l \geqslant 1$ depending only on $\eta, \theta$ and $\omega$, and a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$\varphi_{0}+t \psi_{\gamma}+n(t \log t-t)-C t \leqslant \varphi_{\gamma}(t) \quad \text { in } \quad X \backslash D$$
for all $t \in\left(0, \frac{1}{2 l}\right)$ and $0<\gamma \ll 1$.

Proof. Fix $l \geqslant 1$ such that
$$\frac{1}{2 l-1}<T \quad \text { and } \quad(2 l-1) \omega+\nu_{\gamma} \geqslant \frac{\omega}{2}$$
for all $0<\gamma \ll 1$, and fix $0<t_{0} \ll 1$ such that
$$(2 l-1) \omega+\left(1+2 l t_{0}\right) \nu_{\gamma} \geqslant 0$$
and
$$\omega+\left(1+2 l t_{0}\right) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}=\omega_{\gamma}+2 l t_{0} \sqrt{-1} \partial \bar{\partial} \psi_{\gamma} \geqslant \frac{1}{2} \omega_{\gamma} .$$

We consider equation
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} u_{\gamma t_{0}}\right)^{n}=e^{u_{\gamma t_{0}}-h-2 l \varphi_{\gamma}\left(t_{0}\right)} \frac{\omega^{n}}{|s|_{h}^{2(1-\gamma)}} .$$
It follows from Kołodziej's results [29] that there exists a unique continuous solution $u_{\gamma t_{0}}$ to above equation. Now we write this equation as
$$\begin{aligned}
& \left(\omega+\left(1+2 l t_{0}\right) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}+\sqrt{-1} \partial \bar{\partial}\left(u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}\right)\right)^{n} \\
= & e^{\left(u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}\right)-h-2 l\left(\varphi_{\gamma}\left(t_{0}\right)-t_{0} \psi_{\gamma}\right)+\psi_{\gamma}+\log \frac{\omega^{n}}{\omega_{\gamma}^{\pi}}-(1-\gamma) \log |s|_{h}^{2}} \omega_{\gamma}^{n} .
\end{aligned}$$

We first prove that there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$\left\|u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}\right\|_{L^{\infty}(X)} \leqslant C .$$
For any $\epsilon>0$, we consider function
$$F(x)=u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}-\epsilon \log |s|_{h}^{2}$$
whose minimum point $x_{0}$ must be in $X \backslash D$ since $F(x)$ tends to $+\infty$ as $x \rightarrow D$. At point $x=x_{0}$, by the maximum principle and (5.25) we have
$$\begin{aligned}
& \left(\omega+\left(1+2 l t_{0}\right) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}+\sqrt{-1} \partial \bar{\partial}\left(u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}\right)\right)^{n} \\
= & \left(\omega+\left(1+2 l t_{0}\right) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta+\sqrt{-1} \partial \bar{\partial} F\left(x_{0}\right)\right)^{n} \\
\geqslant & \left(\omega+\left(1+2 l t_{0}\right) \sqrt{-1} \partial \bar{\partial} \psi_{\gamma}-\epsilon \theta\right)^{n} \\
\geqslant & \left(\frac{1}{2} \omega_{\gamma}-\epsilon \theta\right)^{n} \geqslant \frac{1}{4^{n}} \omega_{\gamma}^{n},
\end{aligned}$$
and by (2.29) and Proposition 3.5,
$$\begin{aligned}
& e^{\left(u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}\right)-h-2 l\left(\varphi_{\gamma}\left(t_{0}\right)-t_{0} \psi_{\gamma}\right)+\psi_{\gamma}+\log \frac{\omega^{n}}{\omega_{\gamma}^{n}}-(1-\gamma) \log |s|_{h}^{2}} \omega_{\gamma}^{n} \\
\leqslant & e^{\left(u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}\right)+C} \omega_{\gamma}^{n} .
\end{aligned}$$
Hence there exists a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$u_{\gamma t_{0}}\left(x_{0}\right)-\left(1+2 l t_{0}\right) \psi_{\gamma}\left(x_{0}\right) \geqslant C \quad \text { on } \quad X,$$
which implies
$$u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}-\epsilon \log |s|_{h}^{2} \geqslant C \quad \text { on } \quad X,$$
and
$$u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma} \geqslant C \quad \text { on } \quad X$$
after we let $\epsilon \rightarrow 0$. By similar arguments we can also obtain an upper bound on $u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}$.
Next, we set
$$M(t)=(1-2 l t) \varphi_{\gamma}\left(t_{0}\right)+t u_{\gamma t_{0}}+n(t \log t-t) .$$

Since $\varphi_{\gamma}\left(t_{0}\right)$ and $u_{\gamma t_{0}}$ are continuous,
$$\lim _{t \rightarrow 0^{+}}\left\|M(t)-\varphi_{\gamma}\left(t_{0}\right)\right\|_{L^{\infty}(X)}=0 .$$
For $0 \leqslant t \leqslant \frac{1}{2 l}-t_{0}$, by using (5.24), we have
$$\begin{aligned}
\omega_{\gamma\left(t+t_{0}\right)}+\sqrt{-1} \partial \bar{\partial} M(t) & =\omega+\left(t+t_{0}\right) \nu_{\gamma}+(1-2 l t) \sqrt{-1} \partial \bar{\partial} \varphi_{\gamma}\left(t_{0}\right)+t \sqrt{-1} \partial \bar{\partial} u_{\gamma t_{0}} \\
& =(1-2 l t) \omega_{\varphi_{\gamma}\left(t_{0}\right)}+t \omega_{u_{\gamma t_{0}}}+t\left((2 l-1) \omega+\left(1+2 l t_{0}\right) \nu_{\gamma}\right) \\
& \geqslant t \omega_{u_{\gamma t_{0}}} .
\end{aligned}$$
Hence
$$\left(\omega_{\gamma\left(t+t_{0}\right)}+\sqrt{-1} \partial \bar{\partial} M(t)\right)^{n} \geqslant t^{n} \omega_{u \gamma t_{0}}^{n}=t^{n} e^{u_{\gamma t_{0}}-h-2 l \varphi_{\gamma}\left(t_{0}\right)} \frac{\omega^{n}}{|s|_{h}^{2(1-\gamma)}},$$
which implies that
$$\begin{aligned}
& \log \frac{\left(\omega_{\gamma\left(t+t_{0}\right)}+\sqrt{-1} \partial \bar{\partial} M(t)\right)^{n}}{\omega^{n}}+h+(1-\gamma) \log |s|_{h}^{2} \\
\geqslant & n \log t+u_{\gamma t_{0}}-2 l \varphi_{\gamma}\left(t_{0}\right)=\frac{\partial M(t)}{\partial t} .
\end{aligned}$$
So $M(t)$ is a sub-solution to equation (2.20) with initial value $\varphi_{\gamma}\left(t_{0}\right)$. Since $\varphi_{\gamma}\left(t+t_{0}\right)$ is a solution with initial value $\varphi_{\gamma}\left(t_{0}\right)$, then by the maximum principle Proposition 2.14 we have
$$M(t) \leqslant \varphi_{\gamma}\left(t+t_{0}\right),$$
and by Proposition 3.1 and (5.34)
$$\begin{aligned}
\varphi_{\gamma}\left(t+t_{0}\right) & \geqslant(1-2 l t) \varphi_{\gamma}\left(t_{0}\right)+t u_{\gamma t_{0}}+n(t \log t-t) \\
& =\varphi_{\gamma}\left(t_{0}\right)-2 l t\left(\varphi_{\gamma}\left(t_{0}\right)-t_{0} \psi_{\gamma}\right)+t\left(u_{\gamma t_{0}}-\left(1+2 l t_{0}\right) \psi_{\gamma}\right)+n(t \log t-t)+t \psi_{\gamma} \\
& \geqslant \varphi_{\gamma}\left(t_{0}\right)+t \psi_{\gamma}+n(t \log t-t)-C t .
\end{aligned}$$
By using Theorem 2.7, (2.39) and Remark 2.8, after letting $t_{0} \rightarrow 0$, we have
$$\varphi_{0}+t \psi_{\gamma}+n(t \log t-t)-C t \leqslant \varphi_{\gamma}(t) \quad \text { in } \quad X \backslash D$$
for all $t \in\left(0, \frac{1}{2 l}\right)$ and $0<l \ll 1$. \(\square\)

Corollary 5.5. There exist a uniform constant $l \geqslant 1$ depending only on $\eta, \theta$ and $\omega$, and a uniform constant $C$ depending only on $\left\|\varphi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$\varphi_{0}+t \psi_{o}+n(t \log t-t)-C t \leqslant \varphi(t) \quad \text { in } \quad X \backslash D$$
for all $t \in\left(0, \frac{1}{2 l}\right)$.
Proposition 5.6. There holds
$$\lim _{t \rightarrow 0^{+}}\left\|\varphi(t)-\varphi_{0}\right\|_{L^{1}(X)}=0 .$$
and
$$\lim _{t \rightarrow 0^{+}} \varphi(t)=\varphi_{0} \quad \text { in } \quad X \backslash D .$$
Proof. By using Corollaries 5.3 and 5.5, we have
$$t \psi_{o}+n(t \log t-t)-C t \leqslant \varphi(t)-\varphi_{0} \leqslant \varphi_{\varepsilon j}(t)-\varphi_{j}+\varphi_{j}-\varphi_{0},$$
and so
$$\left\|\varphi(t)-\varphi_{0}\right\|_{L^{1}(X)} \leqslant\left\|\varphi_{\varepsilon j}(t)-\varphi_{j}\right\|_{L^{1}(X)}+\left\|\varphi_{j}-\varphi_{0}\right\|_{L^{1}(X)}+C t,$$
where we use the fact
$$\int_{X}\left|\psi_{o}\right| d V_{\omega} \leqslant C$$
for some uniform constant $C$ in the last inequality. Since
$$\left\|\varphi_{j}-\varphi_{0}\right\|_{L^{1}(X)} \rightarrow 0 \quad \text { as } \quad j \rightarrow+\infty \quad \text { and } \quad\left\|\varphi_{\varepsilon j}(t)-\varphi_{j}\right\|_{\mathcal{C}^{\infty}(X)} \rightarrow 0 \quad \text { as } \quad t \rightarrow 0,$$
for any $\epsilon>0$, there exists $j$ such that
$$\left\|\varphi_{j}-\varphi_{0}\right\|_{L^{1}(X)} \leqslant \frac{\epsilon}{2},$$
and for such $j$, there exists a $\delta>0$ such that for any $t \in(0, \delta)$,
$$\left\|\varphi_{\varepsilon j}(t)-\varphi_{j}\right\|_{\mathcal{C}^{\infty}(X)} \leqslant \frac{\epsilon}{4} \quad \text { and } \quad C t \leqslant \frac{\epsilon}{4} .$$
So for any $\epsilon>0$, there exists a $\delta>0$ such that for any $t \in(0, \delta)$
$$\left\|\varphi(t)-\varphi_{0}\right\|_{L^{1}(X)} \leqslant \epsilon,$$
which means
$$\lim _{t \rightarrow 0^{+}}\left\|\varphi(t)-\varphi_{0}\right\|_{L^{1}(X)}=0 .$$

On the other hand, since at any point $x \in X \backslash D, \varphi_{j}(x)$ decreases to $\varphi_{0}(x)$ as $j \rightarrow+\infty$, and $t \psi_{o}(x)$ and $\left\|\varphi_{\varepsilon j}(t)-\varphi_{j}\right\|_{\mathcal{C}^{\infty}(X)}$ converge to 0 as $t \rightarrow 0^{+}$, we also conclude that
$$\lim _{t \rightarrow 0^{+}} \varphi(t)=\varphi_{0} \quad \text { in } \quad X \backslash D .$$
We complete the proof of this proposition, which implies the forth condition in Theorem 5.1. \(\square\)

Combining all above arguments together, we complete the proof of Theorem 5.1. \(\square\)

Definition 5.7. Assume that $\hat{\omega} \in[\omega]$ is a positive closed current with potential $\varphi_{0} \in L^{\infty}(X)$. By saying $\omega(t)$ is a weak solution to the twisted cusp Kähler-Ricci flow
$$\left\{\begin{array}{l}
\frac{\partial \omega(t)}{\partial t}=-\operatorname{Ric}(\omega(t))+[D]+\eta \\
\left.\omega(t)\right|_{t=0}=\hat{\omega}
\end{array}\right.$$
on $\left(0, T^{\prime}\right) \times X$, we mean that it satisfies the following conditions.
\begin{itemize}
\item[-] For any $0<T<T^{\prime}$, there exists a constant $C$ such that for any $t \in(0, T)$,
$$e^{-\frac{C}{t^{2}}} \omega_{o} \leqslant \omega(t) \leqslant e^{\frac{C}{t^{2}}} \omega_{o} \quad \text { in } \quad X \backslash D ;$$
\item[-] In $\left(0, T^{\prime}\right) \times(X \backslash D), \omega(t)$ satisfies the smooth twisted Kähler-Ricci flow
$$\frac{\partial \omega(t)}{\partial t}=-\operatorname{Ric}(\omega(t))+\eta ;$$
\item[-] On $\left(0, T^{\prime}\right) \times X, \omega(t)$ satisfies Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ in the sense of currents;
\item[-] There exists a metric potential $\varphi(t) \in \mathcal{C}^{\infty}\left(\left(0, T^{\prime}\right) \times(X \backslash D)\right)$ with respect to $\omega_{t}$ such that $\omega(t)=\omega_{t}+\sqrt{-1} \partial \bar{\partial} \varphi(t)$,
$$\lim _{t \rightarrow 0^{+}}\left\|\varphi(t)-\varphi_{0}\right\|_{L^{1}(X)}=0 \quad \text { and } \quad \lim _{t \rightarrow 0^{+}} \varphi(t)=\varphi_{0} \quad \text { in } \quad X \backslash D ;$$
\item[-] On $\left[0, T^{\prime}\right),\left\|\varphi(t)-t \psi_{o}\right\|_{L^{\infty}(X)} \leqslant C$;
\item[-] For any $0<T<T^{\prime}$, there exist constants a and $C$ such that for any $t \in(0, T)$,
$$-C+a \log t \leqslant \dot{\varphi}(t)-\psi_{o} \leqslant \frac{C}{t} .$$
\end{itemize}

Theorem 5.8. There exists a weak solution $\omega(t)=\omega+\sqrt{-1} \partial \bar{\partial} \varphi(t)$ to the twisted cusp Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ on $\left(0, T_{\max }^{\eta}\right) \times X$, where $\varphi(t)$ is obtained in (5.5).

\section*{6. Uniqueness}

In this section, we consider the uniqueness of the cusp Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ in the sense of Definition 5.7. In order to overcome the problems from the weak initial metric and the singular term in the equation, we apply Di Nezza-Lu's idea in [19] which first considering positive time and then taking a limit to the initial time on smooth equation to the singular equation, and we also use the techniques introduced by the authors in [39], which ensure the maximum point always attained outside the divisor.

First, we show a lower bound on the solution to equation (2.14) near the initial time $t=0$.
Proposition 6.1. Assume that $\phi(t)$ is a weak solution to equation (2.14) with initial value $\phi_{0} \in$ $L^{\infty}(X)$ which is a $\omega$-psf function, that is, $\omega_{t}+\sqrt{-1} \partial \bar{\partial} \phi(t)$ is a weak solution to equation $\left(C K R F_{0}^{\eta}\right)$ in the sense of Definition 5.7. There exist a constant $l \geqslant 1$ depending only on $\eta, \theta$ and $\omega$, and a constant $C$ depending only on $\left\|\phi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$ such that
$$\phi_{0}+t \psi_{o}+n(t \log t-t)-C t \leqslant \phi(t) \quad \text { in } \quad X \backslash D$$
for all $t \in\left(0, \frac{1}{2 l}\right)$.
Proof. Fix $l \geqslant 1$ such that
$$\frac{1}{2 l-1}<T \quad \text { and } \quad(2 l-1) \omega+\nu \geqslant \frac{\omega}{2},$$
and fix $0<t_{0} \ll 1$ such that
$$\left(2 l-1-2 l t_{0}\right) \omega+\left(1+2 l t_{0}\right) \nu \geqslant 0 .$$

We consider equation
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} u_{t_{0}}\right)^{n}=e^{u_{t_{0}}-h} \frac{\omega^{n}}{|s|_{h}^{2}} .$$
It follows from Kobayashi [28] and Tian-Yau's results [64] that there exists a solution $u_{t_{0}} \in \mathcal{C}^{\infty}(X \backslash$ $D)$ to above equation. Furthermore, from Guenancia's results [24], there exists a uniform constant $C$ independent of $t_{0}$ such that
$$\left\|u_{t_{0}}-\psi_{o}\right\|_{L^{\infty}(X \backslash D)} \leqslant C .$$

We set
$$M(t)=(1-2 l t) \phi\left(t_{0}\right)+2 l t t_{0} \psi_{o}+t u_{t_{0}}+n(t \log t-t)-C t$$
for some uniform constant $C$ independent of $t_{0}$ and $t$. For $0 \leqslant t \leqslant \frac{1}{2 l}-t_{0}$, by using (6.3), we have
$$\begin{aligned}
& \omega_{\left(t+t_{0}\right)}+\sqrt{-1} \partial \bar{\partial} M(t) \\
= & \omega+\left(t+t_{0}\right) \nu+(1-2 l t) \sqrt{-1} \partial \bar{\partial} \phi\left(t_{0}\right)+2 l t t_{0} \sqrt{-1} \partial \bar{\partial} \psi_{o}+t \sqrt{-1} \partial \bar{\partial} u_{t_{0}} \\
= & (1-2 l t) \omega_{\phi\left(t_{0}\right)}+2 l t t_{0} \omega_{o}+t \omega_{u_{t_{0}}}+t\left(\left(2 l-1-2 l t_{0}\right) \omega+\left(1+2 l t_{0}\right) \nu\right) \\
\geqslant & 2 l t_{0} \omega_{\phi\left(t_{0}\right)}+t \omega_{u_{t_{0}}} .
\end{aligned}$$
Hence
$$\left(\omega_{t+t_{0}}+\sqrt{-1} \partial \bar{\partial} M(t)\right)^{n} \geqslant t^{n} \omega_{u_{t_{0}}}^{n}=t^{n} e^{u_{t_{0}}-h} \frac{\omega^{n}}{|s|_{h}^{2}},$$
which implies that
$$\begin{aligned}
& \log \frac{\left(\omega_{t+t_{0}}+\sqrt{-1} \partial \bar{\partial} M(t)\right)^{n}}{\omega^{n}}+h+\log |s|_{h}^{2} \\
\geqslant & n \log t+u_{t_{0}} \\
\geqslant & n \log t+u_{t_{0}}-2 l\left(\phi\left(t_{0}\right)-t_{0} \psi_{o}\right)-C \\
= & \frac{\partial M(t)}{\partial t} .
\end{aligned}$$

For any $a>0$. We consider $\Phi(t)=M(t)-\phi\left(t+t_{0}\right)+a \log |s|_{h}^{2}$ on $\left[0, \frac{1}{2 l}-t_{0}\right] \times(X \backslash D)$. Since
$$\begin{aligned}
\Phi(t)= & (1-2 l t) \phi\left(t_{0}\right)+2 l t t_{0} \psi_{o}+t u_{t_{0}}+n(t \log t-t)-C t-\phi\left(t+t_{0}\right)+a \log |s|_{h}^{2} \\
= & (1-2 l t)\left(\phi\left(t_{0}\right)-t_{0} \psi_{o}\right)+t\left(u_{t_{0}}-\psi_{o}\right)-\left(\phi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}\right) \\
& +n(t \log t-t)-C t+a \log |s|_{h}^{2}
\end{aligned}$$
and there exists a uniform constant $C$ such that
$$\left\|(1-2 l t)\left(\phi\left(t_{0}\right)-t_{0} \psi_{o}\right)+t\left(u_{t_{0}}-\psi_{0}\right)-\left(\phi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}\right)\right\|_{L^{\infty}(X \backslash D)} \leqslant C,$$
$\Phi(t)$ tends to $-\infty$ as $x \rightarrow D$.
If we denote
$$\hat{\Delta}=\int_{0}^{1} g_{s}^{i \bar{j}} \frac{\partial^{2}}{\partial z^{i} \partial \bar{z}^{j}} d s$$
where $g_{s}$ is the metric corresponding to $\omega_{s}=\omega_{\left(t+t_{0}\right)}+s \sqrt{-1} \partial \bar{\partial} M(t)+(1-s) \sqrt{-1} \partial \bar{\partial} \phi\left(t+t_{0}\right)$. Then $\Phi(t)$ evolves along the following equation
$$\frac{\partial \Phi(t)}{\partial t} \leqslant \hat{\Delta} \Phi(t)-a \hat{\Delta} \log |s|_{h}^{2} .$$
Since $\omega_{\left(t+t_{0}\right)}+\sqrt{-1} \partial \bar{\partial} M(t)$ and $\omega_{\phi(t)}$ are bounded from below by $c_{0} \omega_{o}$ and $\omega_{o} \geqslant c_{1} \omega$, we obtain
$$\omega_{s} \geqslant c \omega$$
for some constants $c_{0}$ and $c$ depending on $t_{0}$ and $T$. Combining this with $-\sqrt{-1} \partial \bar{\partial} \log |s|_{h}^{2}=\theta$, we conclude that there exists a constant $C\left(t_{0}, T\right)$ depending on $t_{0}$ and $T$ such that
$$-\hat{\Delta} \log |s|_{h}^{2}=\int_{0}^{1} \operatorname{tr}_{\omega_{s}} \theta d s \leq C\left(t_{0}, T\right)$$
in $X \backslash D$. Then
$$\frac{\partial \Phi(t)}{\partial t} \leqslant \hat{\Delta} \Phi(t)+a C\left(t_{0}, T\right) .$$

Let $\tilde{\Phi}=\Phi(t)-a t C\left(t_{0}, T\right)-\epsilon t$, and $\left(t_{1}, x_{1}\right)$ be it maximum point. Since $\Phi(t)$ tends to $-\infty$ as $x \rightarrow D$ and so the space maximum point $x_{1}$ of $\tilde{\Phi}(t)$ in $\left[0, \frac{1}{2 l}-t_{0}\right] \times(X \backslash D)$ attained away from $D$. If $t_{1}>0$, by the maximum principle, at $\left(t_{1}, x_{1}\right)$, we have
$$0 \leqslant\left(\frac{\partial}{\partial t}-\hat{\Delta}\right) \tilde{\Phi}(t) \leqslant-\epsilon$$
which is impossible, hence $t_{1}=0$. Since
$$\tilde{\Phi}\left(0, x_{1}\right)=\Phi\left(0, x_{1}\right) \leqslant M\left(0, x_{1}\right)-\phi\left(t_{0}, x_{1}\right)=0,$$
then for $(t, x) \in\left[0, \frac{1}{2 l}-t_{0}\right] \times X$, we obtain
$$M(t)-\phi\left(t+t_{0}\right) \leqslant a T C\left(t_{0}, T\right)+\epsilon T-a \log |s|_{h}^{2} .$$
We let $\epsilon \rightarrow 0$ and then $a \rightarrow 0$, there holds
$$\begin{aligned}
\phi\left(t+t_{0}\right) & \geqslant(1-2 l t) \phi\left(t_{0}\right)+2 l t t_{0} \psi_{o}+t u_{t_{0}}+n(t \log t-t)-C t \\
& =\phi\left(t_{0}\right)-2 l t\left(\phi\left(t_{0}\right)-t_{0} \psi_{o}\right)+t \psi_{o}+t\left(u_{t_{0}}-\psi_{0}\right)+n(t \log t-t)-C t \\
& \geqslant \phi\left(t_{0}\right)+t \psi_{o}-C t+n(t \log t-t)
\end{aligned}$$
for some uniform constant $C$ depending only on $\left\|\phi_{0}\right\|_{L^{\infty}(X)}, n, \omega, \theta, \eta$ and $T$.
Claim. For any $t \in(0, T]$, there holds
$$\lim _{s \rightarrow 0^{+}}\left\|\left(\phi(t+s)-(t+s) \psi_{o}\right)-\left(\phi(t)-t \psi_{o}\right)\right\|_{L^{\infty}(X \backslash D)}=0 .$$

Since by the last condition (5.58) in Definition 5.7, there exists a uniform constant $C$ such that
$$-C+a \log (t+\lambda) \leqslant \dot{\phi}(t+\lambda)-\psi_{o} \leqslant \frac{C}{t+\lambda} \quad \text { for } \lambda \in[0, T-t]$$
with $0<t<T$, by integrating above inequality from 0 to $s$ with respect to $\lambda$ on both sides, we have
$$\phi(t+s)-(t+s) \psi_{o}-\left(\phi(t)-t \psi_{o}\right) \leqslant C(\log (t+s)-\log t)$$
and
$$-C s+a((t+s) \log (t+s)-(t+s))-a(t \log t-t) \leqslant \phi(t+s)-(t+s) \psi_{o}-\left(\phi(t)-t \psi_{o}\right)$$
in $[0, T-t] \times(X \backslash D)$. Let $s \rightarrow 0$ in (6.23) and (6.24), for fix $0<t<T$, there holds
$$\lim _{s \rightarrow 0^{+}}\left\|\left(\phi(t+s)-(t+s) \psi_{o}\right)-\left(\phi(t)-t \psi_{o}\right)\right\|_{L^{\infty}(X \backslash D)}=0 .$$
We complete the proof of the Claim.
By using (6.20), we also have
$$\phi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o} \geqslant \phi\left(t_{0}\right)-t_{0} \psi_{o}-C t+n(t \log t-t) \geqslant \phi\left(t_{0}\right)-C t_{0}-C t+n(t \log t-t),$$
where we use the fact $\psi_{\gamma}$ decreasing to $\psi_{o}$ as $\gamma \rightarrow 0$ and $\psi_{\gamma}$ is a continuous function on $X$ for $\gamma>0$. By using (5.57) and (6.25), we have
$$\phi_{0}+n(t \log t-t)-C t \leqslant \phi(t)-t \psi_{o} \quad \text { in } \quad X \backslash D$$
for all $t \in\left(0, \frac{1}{2 l}\right)$ after letting $t_{0} \rightarrow 0$ in (6.26). \(\square\)

Next, we prove a maximum principle for the equation with cusp singualrity.
Theorem 6.2. Assume that $\varphi(t)$ and $\phi(t)$ are weak solutions to equation (2.14) with initial values $\varphi_{0}$ and $\phi_{0}$ on $(0, T) \times X$ respectively, where $\varphi_{0}, \phi_{0} \in \operatorname{PSH}(X, \omega) \cap L^{\infty}(X)$. Then
$$\varphi(t)-\phi(t) \leqslant \sup _{X}\left(\varphi_{0}-\phi_{0}\right) \quad \text { in } \quad X \backslash D$$
for all $t \in[0, T)$.
Proof. Fix $t_{0}>0$, we first consider
$$u(t)=\phi\left(t+t_{0}\right)+C_{t_{0}},$$
where $C_{t_{0}}=C t_{0}-n\left(t_{0} \log t_{0}-t_{0}\right)$ comes from (6.1). Hence $u(t)$ is a solution to equation
$$\frac{\partial u(t)}{\partial t}=\frac{\partial \phi\left(t+t_{0}\right)}{\partial t}=\log \frac{\left(\omega+\left(t+t_{0}\right) \nu+\sqrt{-1} \partial \bar{\partial} u(t)\right)^{n}}{\omega^{n}}+h+\log |s|_{h}^{2}$$
with initial value
$$u(0)=\phi\left(t_{0}\right)+C_{t_{0}} \geqslant \phi_{0}+t_{0} \psi_{o} .$$
On the other hand,
$$v(t)=\varphi\left(t+t_{0}\right)$$
satisfies equation
$$\frac{\partial v(t)}{\partial t}=\log \frac{\left(\omega+\left(t+t_{0}\right) \nu+\sqrt{-1} \partial \bar{\partial} v(t)\right)^{n}}{\omega^{n}}+h+\log |s|_{h}^{2}$$
with initial value $\varphi\left(t_{0}\right)$. If we denote
$$\hat{\Delta}=\int_{0}^{1} g_{s}^{i \bar{j}} \frac{\partial^{2}}{\partial z^{i} \partial \bar{z}^{j}} d s$$
where $g_{s}$ is the metric corresponding to $\omega_{s}=\omega_{\left(t+t_{0}\right)}+s \sqrt{-1} \partial \bar{\partial} v(t)+(1-s) \sqrt{-1} \partial \bar{\partial} u(t)$. Then
$$\Phi(t)=v(t)-u(t)+a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \log |s|_{h}^{2}$$
evolves along the following equation
$$\frac{\partial \Phi(t)}{\partial t} \leqslant \hat{\Delta} \Phi(t)-a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \hat{\Delta} \log |s|_{h}^{2} .$$
Since $\omega_{v(t)}$ and $\omega_{u(t)}$ are bounded from below by $e^{-\frac{C}{t_{0}^{2}}} \omega_{o}$ and $\omega_{o} \geqslant \frac{1}{2} \omega$, we obtain
$$\omega_{s} \geqslant e^{-\frac{C}{t_{0}^{2}}} \omega .$$
Combining this with $-\sqrt{-1} \partial \bar{\partial} \log |s|_{h}^{2}=\theta$, we conclude that there exists a uniform constant $C$ depending on $\theta$ and $\omega$ such that
$$-\hat{\Delta} \log |s|_{h}^{2}=\int_{0}^{1} \operatorname{tr}_{\omega_{s}} \theta d s \leq C e^{\frac{C}{t_{0}^{2}}}$$
in $X \backslash D$. Then
$$\frac{\partial \Phi(t)}{\partial t} \leqslant \hat{\Delta} \Phi(t)+a C e^{-\frac{C}{t_{0}^{2}}} .$$

Let $\tilde{\Phi}=\Phi(t)-a C e^{-\frac{C}{t_{0}^{2}}} t-\epsilon t$, and $\left(t_{1}, x_{1}\right)$ be its maximum point on $[0, T]$. Since
$$\begin{aligned}
\Phi(t) & =v(t)-u(t)+a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \log |s|_{h}^{2} \\
& =\varphi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}-\left(\phi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}\right)-C_{t_{0}}+a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \log |s|_{h}^{2}
\end{aligned}$$
and
$$\left\|\varphi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}\right\|_{L^{\infty}(X)} \quad \text { and } \quad\left\|\phi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}\right\|_{L^{\infty}(X)}$$
are bounded, $\Phi(t)$ and so $\tilde{\Phi}(t)$ converge to $-\infty$ as $x$ tends to $D$. Hence $x_{1}$ must be in $X \backslash D$. If $t_{1}>0$, by the maximum principle, at $\left(t_{1}, x_{1}\right)$, we have
$$0 \leqslant\left(\frac{\partial}{\partial t}-\hat{\Delta}\right) \tilde{\Phi}(t) \leqslant-\epsilon,$$
which is impossible, hence $t_{1}=0$. Since by Proposition 6.1,
$$\begin{aligned}
\tilde{\Phi}\left(0, x_{1}\right) & \leqslant v\left(0, x_{1}\right)-u\left(0, x_{1}\right)+a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \log |s|_{h}^{2}\left(x_{1}\right) \\
& =\varphi\left(t_{0}, x_{1}\right)-\phi\left(t_{0}, x_{1}\right)-C_{t_{0}}+a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \log |s|_{h}^{2}\left(x_{1}\right) \\
& \leqslant \varphi\left(t_{0}, x_{1}\right)-\phi_{0}\left(x_{1}\right)-t_{0} \psi_{o}\left(x_{1}\right)+a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \log |s|_{h}^{2}\left(x_{1}\right) \\
& \leqslant \varphi\left(t_{0}, x_{1}\right)-\phi_{0}\left(x_{1}\right)+t_{0} \log \left(|s|_{h}^{2 a e^{-\frac{2 C}{t_{0}^{2}}}} \log ^{2}|s|_{h}^{2}\right)\left(x_{1}\right) \\
& \leqslant \sup _{X}\left(\varphi\left(t_{0}\right)+t_{0} \log \left(|s|_{h}^{2 a e^{-\frac{2 C}{t_{0}^{2}}}} \log ^{2}|s|_{h}^{2}\right)-\phi_{0}\right)
\end{aligned}$$
Then for $(t, x) \in[\delta, T] \times(X \backslash D)$, we obtain
$$\begin{aligned}
\varphi\left(t+t_{0}\right)-\phi\left(t+t_{0}\right) \leqslant & \sup _{X}\left(\varphi\left(t_{0}\right)+t_{0} \log \left(|s|_{h}^{2 a e e^{-\frac{2 C}{t_{0}^{2}}}} \log ^{2}|s|_{h}^{2}\right)-\phi_{0}\right) \\
& +a C T e^{-\frac{C}{t_{0}^{2}}}+\epsilon T+C_{t_{0}}-a t_{0} e^{-\frac{2 C}{t_{0}^{2}}} \log |s|_{h}^{2} .
\end{aligned}$$

By using Claim (6.21),
$$\begin{aligned}
\varphi\left(t+t_{0}\right)-\phi\left(t+t_{0}\right) & =\varphi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}-\left(\phi\left(t+t_{0}\right)-\left(t+t_{0}\right) \psi_{o}\right) \\
& \xrightarrow{t_{0} \rightarrow 0} \varphi(t)-t \psi_{o}-\left(\phi(t)-t \psi_{o}\right) \\
& =\varphi(t)-\phi(t) .
\end{aligned}$$
We let $\epsilon \rightarrow 0$ and then $t_{0} \rightarrow 0$, since $\varphi\left(t_{0}\right)+t_{0} \log \left(|s|_{h}^{2 a e}{ }^{-\frac{2 C}{t_{0}^{2}}} \log ^{2}|s|_{h}^{2}\right)$ is a $3 \omega_{o}$-psh function which converges to $\varphi_{0}$ in $L^{1}$-sense as $t_{0} \rightarrow 0$ on $X$, by Hartogs' Lemma, there holds
$$\varphi(t)-\phi(t) \leqslant \sup _{X}\left(\varphi_{0}-\phi_{0}\right) .$$
We complete the proof. \(\square\)

As a corollary of above uniqueness and Theorem 5.8, we obtain the following uniqueness theorem for the twisted cusp Kähler-Ricci flow with initial metric.

Theorem 6.3. Assume that $\varphi_{0} \in \operatorname{PSH}(X, \omega) \cap L^{\infty}(X)$. Then there exists a unique weak solution to equation (2.14) with initial value $\varphi_{0}$, or equivalently, there exists a unique weak solution to the twisted cusp Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ on $\left(0, T_{\max }^{\eta}\right) \times X$.
Remark 6.4. In [32], by approximating $\log |s|_{h}^{2}$ by $\log \left(\varepsilon^{2}+|s|_{h}^{2}\right)$ as $\varepsilon$ decreases to zero, Li-Shen-Zheng constructed a sequence of solutions $\phi_{\varepsilon}(t)$ converging to a maximal weak solution $\phi_{\max }(t)$ (in the sense of potential) to the twisted cusp Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ on $\left(0, T_{\max }^{\eta}\right) \times X$ due to $\log |s|_{h}^{2} \leqslant \log \left(\varepsilon^{2}+|s|_{h}^{2}\right)$.

In this paper, we obtain a weak solution $\varphi(t)$ to the twisted cusp Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ on $\left(0, T_{\text {max }}^{\eta}\right) \times X$ by taking a limit on $\varphi_{\gamma}(t)$ as $\gamma$ tends to zero. Moreover, we can also prove that $\varphi_{\gamma}(t)+t \gamma \log |s|_{h}^{2}$ increases to a minimal weak solution $\phi_{\min }(t)$ to the twisted cusp Kähler-Ricci flow $\left(C K R F_{0}^{\eta}\right)$ on $\left(0, T_{\text {max }}^{\eta}\right) \times X$. Therefore,
$$\varphi_{\gamma}(t)+t \gamma \log |s|_{h}^{2} \leqslant \phi_{\min }(t)=\varphi(t) \leqslant \phi_{\max }(t) \leqslant \phi_{\varepsilon}(t) .$$
In fact, by using above uniqueness theorem Theorems 6.2 and 6.3, we conclude that the solutions obtained from above three different methods are the same, that is,
$$\phi_{\min }(t)=\varphi(t)=\phi_{\max }(t) .$$

Combining Theorem 5.1 and the uniqueness Theorem 6.3, we give the characterization of the limit flow of the twisted conical Kähler-Ricci flow as its cone angle tends to zero, which is exactly Theorem 1.1.

\section*{References}
\begin{itemize}
\item[] [1] R. Bamler, Convergence of Ricci flows with bounded scalar curvature, Annals of Mathematics, 188 (2018), 753-831.
\item[] [2] R. Berman, A thermodynamical formalism for Monge-Ampere equations, Moser-Trudinger inequalities and Kähler-Einstein metrics, Advances in Mathematics, 248 (2013), 1254-1297.
\item[] [3] R. Berman, S. Boucksom, P. Eyssidieux, V. Guedj and A. Zeriahi, Kähler-Einstein metrics and the Kähler-Ricci flow on log Fano varieties, Journal für die Reine und Angewandte Mathematik, 751 (2019), 27-89.
\item[] [4] O. Biquard and H. Guenancia, Degenerating Kähler-Einstein cones, locally symmetric cusps, and the Tian-Yau metric, Inventiones Mathematicae, 230 (2022), 1101-1163.
\item[] [5] S. Brendle and R. Schoen, Manifolds with 1/4-pinched curvature are space forms, Journal of the American Mathematical Society, 22 (2009), 287-307.
\item[] [6] H. D. Cao, Deformation of Kähler metrics to Kähler-Einstein metrics on compact Kähler manifolds, Inventiones Mathematicae, 81 (1985), 359-372.
\item[] [7] A. Chau, K. F. Li and L. M. Shen, Kähler-Ricci flow of cusp singularities on quasi projective varieties, Advances in Mathematics, 339 (2018), 310-335.
\end{itemize}
\begin{itemize}
\item[] [8] I. A. Cheltsov and Y. A. Rubinstein, Asymptotically log Fano varieties, Advances in Mathematics, 285 (2015), 1241-1300.
\item[] [9] X. X. Chen, S. K. Donaldson and S. Sun, Kähler-Einstein metric on Fano manifolds, I: approximation of metrics with cone singularities, Journal of the American Mathematical Society, 28 (2015), 183-197.
\item[] [10] X. X. Chen, S. K. Donaldson and S Sun, Kähler-Einstein metric on Fano man- ifolds, II: limits with cone angle less than $2 \pi$, Journal of the American Mathematical Society, 28 (2015), 199-234.
\item[] [11] X. X. Chen, S. K. Donaldson and S. Sun, Kähler-Einstein metric on Fano man- ifolds, III: limits with cone angle approaches $2 \pi$ and completion of the main proof, Journal of the American Mathematical Society, 28 (2015), 235-278.
\item[] [12] X. X. Chen and B. Wang, Space of Ricci flows (II)-Part B: Weak compactness of the flows, Journal of Differential Geometry, 116 (2020), 1-123.
\item[] [13] X. X. Chen and Y. Q. Wang, Bessel functions, Heat kernel and the Conical Kähler-Ricci flow, Journal of Functional Analysis, 269 (2015), 551-632.
\item[] [14] X. X. Chen and Y. Q. Wang, On the long-time behaviour of the Conical Kähler-Ricci flows, Journal für die reine und angewandte Mathematik, 744 (2018), 165-199.
\item[] [15] S. S. Chern, On holomorphic mappings of Hermitian manifolds of the same dimension, Proc. Symp. Pure Math., 11 (1968), 157-170.
\item[] [16] T. Collins and G. Székelyhidi, The twisted Kähler-Ricci flow, Journal für die Reine und Angewandte Mathematik, 716 (2016), 179-205.
\item[] [17] J. P. Demailly, Regularization of closed positive currents and intersection theory, Journal of Algebraic Geometry, 1 (1992), 361-409.
\item[] [18] R. Dervan and G. Székelyhidi, The Kähler-Ricci flow and optimal degenerations, Journal of Differential Geometry, 116 (2020), 187-203.
\item[] [19] E. Di Nezza and C. H. Lu, Uniqueness and short time regularity of the weak Kähler-Ricci flow, Advances in Mathematics, 305 (2017), 953-993.
\item[] [20] S. K. Donaldson, Discussion of the Kähler-Einstein problem, 2009, preprint. Available at http://www2. imperial.ac.uk/ skdona/KENOTES.PDF.
\item[] [21] G. Edwards, Metric contraction of the cone divisor by the conical Kähler-Ricci flow, Mathematische Annalen, 374 (2017), 1-33.
\item[] [22] G. Edwards, A scalar curvature bound along the conical Kähler-Ricci flow, The Journal of Geometric Analysis, 28 (2018), 225-252.
\item[] [23] V. Guedj and A. Zeriahi, Regularizing properties of the twisted Kähler-Ricci flow, Journal für die Reine und Angewandte Mathematik, 729 (2017), 275-304.
\item[] [24] H. Guenancia, Kähler-Einstein metrics: from cones to cusps, Journal für die Reine und Angewandte Mathematik, 759 (2020), 1-27.
\item[] [25] R. Hamilton, Three-manifolds with positive Ricci curvature, Journal of Differential Geometry, 17 (1982), 255-306.
\item[] [26] T. Jeffres, R. Mazzeo and Y. Rubinstein, Kähler-Einstein metrics with edge singularities, Annals of Mathematics, 183 (2016), 95-176.
\item[] [27] W. J. Jian, J. Song and G. Tian, Finite Time Singularities of the Kähler-Ricci flow, (2023), arXiv: 2310.07945.
\item[] [28] R. Kobayashi, Kähler-Einstein metric on an open algebraic manifolds, Osaka Journal of Mathematics, 21 (1984), 399-418.
\item[] [29] S. Kotodziej, The complex Monge-Ampère equation, Acta mathematica, 180 (1998), 69-117.
\item[] [30] S. Kotodziej, Hölder continuity of solutions to the complex Monge- Ampère equation with the right-hand side in $L^{p}$ : the case of compact Kähler manifolds, Mathematische Annalen, (2008), 379-386.
\item[] [31] N. V. Krylov, Lectures on elliptic and parabolic equations in Hölder spaces, American Mathematical Society, (1996).
\item[] [32] C. Li, L. M. Shen and T. Zheng, The Kähler-Ricci flow on log canonical pairs of general type, Journal of Functional Analysis, 285 (2023), 109984.
\item[] [33] C. Li and S. Sun, Conical Kähler-Einstein metric revisited, Communications in Mathematical Physics, 331 (2014), 927-973.
\item[] [34] J. W. Liu, The generalized Kähler Ricci flow, Journal of Mathematical Analysis and Applications, 408 (2013), 751-761.
\item[] [35] J. W. Liu, On the existence of the conical Kähler-Einstein metrics on Fano manifolds, accepted by Communications in Analysis and Geometry, 2021.
\item[] [36] J. W. Liu and C. J. Zhang, The conical complex Monge-Ampère equations on Kähler manifolds, Calculus of Variations and Partial Differential Equations, 57 (2018), 44.
\item[] [37] J. W. Liu and X. Zhang, Conical Kähler-Ricci flow on Fano manifolds, Advances in Mathematics, 307 (2017), 1324-1371.
\end{itemize}
[38] J. W. Liu and X. Zhang, The conical Kähler-Ricci flow with weak initial data on Fano manifold, International Mathematics Research Notices, 17 (2017), 5343-5384.
[39] J. W. Liu and X. Zhang, Cusp Kähler-Ricci flows on compact Kähler manifolds, Annali di Matematica Pura ed Applicata (1923-), 198 (2019), 289-306.
[40] J. W. Liu and X. Zhang, Stability of the conical Kähler-Ricci flows on Fano manifolds, Communications in Partial Differential Equations, 46 (2021), 953-1004.
[41] J. W. Liu and X. Zhang, The openness theorems on the convergence of the twisted Kähler-Ricci flows, preprint, 2023.
[42] J. W. Liu, S. Y. Zhang and X. Zhang, Regularizing property of the twisted conical Kähler-Ricci flow, preprint, 2024.
[43] J. Lott and Z. Zhang, Ricci flow on quasi-projective manifolds, Duke Mathematical Journal, 156 (2011), 87-123.
[44] J. Lott and Z. Zhang, Ricci flow on quasiprojective manifolds II, Journal of the European Mathematical Society, 18 (2016), 1813-1854.
[45] Y. C. Lu, Holomorphic mappings of complex manifolds, Journal of Differential Geometry, 2 (1968), 299-312.
[46] D. Phong, N. Sesum and J. Sturm, Multiplier ideal sheaves and the Kähler-Ricci flow, Communications in Analysis and Geometry, 15 (2007), 613-632.
[47] D. Phong, J. Song, J. Sturm and B. Weinkove, The Kähler-Ricci flow with positive bisectional curvature, Inventiones Mathematicae, 173 (2008), 651-665.
[48] D. Phong, J. Song, J. Sturm and B. Weinkove, The Kähler-Ricci flow and the $\bar{\partial}$ operator on vector fields, Journal of Differential Geometry, 81 (2009), 631-647.
[49] D. Phong and J. Sturm, On stability and the convergence of the Kähler-Ricci flow, Journal of Differential Geometry, 72 (2006), 149-168.
[50] R. Nomura, Blow-up behavior of the scalar curvature along the conical Kähler-Ricci flow with finite time singularities, Differential Geometry and its Applications, 58 (2018), 1-16.
[51] G. Perelman, The entropy formula for the Ricci flow and its geometric applications, arXiv: math.DG/0211159.
[52] G. Perelman, Ricci flow with surgery on three manifolds, arXiv: math.DG/0303109.
[53] Y. Rubinstein and K. W. Zhang, Small angle limits of Hamilton's footballs, Bulletin of the London Mathematical Society, 52 (2020), 189-199.
[54] Y. Rubinstein and K. W. Zhang, Angle deformation of Kähler-Einstein edge metrics on Hirzebruch surfaces, Pure and Applied Mathematics Quarterly, 18 (2022), 343-366.
[55] L. M. Shen, $C^{2, \alpha}$-estimate for conical Kähler-Ricci flow, Calculus of Variations and Partial Differential Equations, 57 (2018), 33.
[56] L. M. Shen, Maximal time existence of unnormalized conical Kähler-Ricci flow, Journal für die reine und angewandte Mathematik, 760 (2020), 169-193.
[57] J. Song and G. Tian, The Kähler-Ricci flow through singularities, Inventiones mathematicae, 207 (2017), 519-595.
[58] J. Song and X. W. Wang, The greatest Ricci lower bound, conical Einstein metrics and the Chern number inequality, Geometry \& Topology, 20 (2016), 49-102.
[59] G. Sźekelyhidi, The Kähler-Ricci flow and K-polystability, American Journal of Mathematics, 132 (2010), 1077-1090.
[60] G. Sźekelyhidi and V. Tosatti, Regularity of weak solutions of a complex Monge-Ampère equation, Analysis \& PDE, 4 (2011), 369-378.
[61] G. Tian, Kähler-Einstein metrics on algebraic manifolds, Transcendental methods in algebraic geometry (Cetraro 1994), Lecture Notes in Mathematics 1646, Springer-Verlag, New York, (1996), 143-185.
[62] G. Tian, Kähler-Einstein metrics with positive scalar curvature, Inventiones Mathematicae, 130 (1997), 1-37.
[63] G. Tian, K-stability and Kähler-Einstein metrics, Communications on Pure and Applied Mathematics, 68 (2015), 1085-1156.
[64] G. Tian and S. T. Yau, Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry, Advanced Series in Mathematical Physics 11 (1987), 574-628.
[65] G. Tian, S. J. Zhang, Z. L. Zhang and X. H. Zhu, Perelman's entropy and Kähler-Ricci flow on a Fano manifold, Transactions of the American Mathematical Society, 365 (2013), 6669-6695.
[66] G. Tian and Z. L. Zhang, Regularity of Kähler-Ricci flows on Fano manifolds, Acta Mathematica, 216 (2016), 127-176.
[67] G. Tian and Z. Zhang, On the Kähler-Ricci flow on projective manifolds of general type, Chinese Annals of Mathematics, Series B, 27 (2006), 179-192.
[68] G. Tian and X. H. Zhu, Convergence of Kähler-Ricci flow, Journal of the American Mathematical Society, 20 (2007), 675-699.
[69] G. Tian and X. H. Zhu, Convergence of the Kähler-Ricci flow on Fano manifolds, Journal für die Reine und Angewandte Mathematik, 678 (2013), 223-245.
\begin{itemize}
\item[] [70] V. Tosatti, Kähler-Ricci flow on stable Fano manifolds, Journal für die Reine und Angewandte Mathematik, 640 (2010), 67-84.
\item[] [71] H. Tsuji, Existence and degeneration of Kähler-Einstein metrics on minimal algebraic varieties of general type, Mathematische Annalen, 281 (1988), 123-133.
\item[] [72] F. Wang and X. H. Zhu, Tian's partial $C^{0}$-estimate implies Hamilton-Tian's conjecture, Advances in Mathematics, 381 (2021), Paper No. 107619, 29 pages.
\item[] [73] Y. Q. Wang, Smooth approximations of the conical Kähler-Ricci flows, Mathematische Annalen, 365 (2016), 835-856.
\item[] [74] K. W. Zhang, Some refinements of the partial $C^{0}$ estimate, Analysis \& PDE, 14 (2021), 2307-2326.
\item[] [75] Y. S. Zhang, A note on conical Kähler-Ricci flow on minimal elliptic Kähler surfaces, Acta Mathematica Scientia, 38 (2018), 169-176.
\item[] [76] Y. S. Zhang, On a twisted conical Kähler-Ricci flow, Annals of Global Analysis and Geometry, 55 (2019), 69-98.
\end{itemize}

Jiawei Liu, School of Mathematics and Statistics, Nanjing University of Science \& Technology, Xiaolingwei Street 200, Nanjing 210094, China.

Email address: jiawei.liu@njust.edu.cn
Xi Zhang, School of Mathematics and Statistics, Nanjing University of Science \& Technology, Xiaolingwei Street 200, Nanjing 210094, China.

Email address: mathzx@njust.edu.cn