---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The Greatest Ricci Lower Bound, Conical Einstein Metrics and the Chern Number Inequality]

Without loss of generality, we assume that $l_{1}(x)=l_{2}(x)=\ldots=l_{n}(x)=0$ with $l_{i}(x)=$ $v_{i} \cdot x+1,1 \leq i \leq n$ defines a vertex $p$ of $P$. Then there exists a smooth positive function $F(x)$ on any compact subset $U$ of $\bar{P}$ with $U \cap\left\{l_{j}(x)=0\right\}=\phi$ for all $j>n$, such that
$$\operatorname{det}\left(\nabla^{2} u\right)=\frac{F(x)}{l_{1}(x) l_{2}(x) \ldots l_{n}(x)} .$$

On the other hand,
$$u(x)-\left(x-P_{c}\right) \nabla u(x)=\sum_{j=1}^{N} \beta_{j}^{-1} l_{j}\left(P_{c}\right) \log l_{j}(x)-\sum_{j=1}^{N} \beta_{j}^{-1}\left(x-P_{c}\right) \cdot v_{j}-\left(x-P_{c}\right) \cdot \nabla f(x)$$
and so
$$e^{-\alpha\left(u-\left(x-P_{c}\right) \cdot \nabla u\right)}=\frac{e^{-\alpha\left(x-P_{c}\right) \cdot\left(\nabla f(x)+\sum_{j} \beta_{j}^{-1} v_{j}\right)}}{\prod_{j=1}^{N}\left(l_{j}(x)^{\alpha \beta_{j}^{-1} l_{j}\left(P_{c}\right)}\right)} .$$
By comparing the power of $l_{j}(x)$, we have
$$\beta_{j}=l_{j}\left(P_{c}\right) \alpha=\frac{l_{j}\left(P_{c}\right)}{l_{j}(0)} \alpha$$
since $l_{j}(0)=1$. This completes the proof of the lemma. \(\square\)

Lemma 3.3 tells us that we should consider the following Monge-Ampère equation
$$\operatorname{det}\left(\nabla^{2} \phi\right)^{n}=e^{-\alpha\left(\phi-P_{c} \cdot \rho\right)} .$$
The right hand side of equation (3.35) is always integrable because $P_{c}$ lies in $P$ and $\phi-$ $\log \left(\sum_{k} e^{p_{k} \cdot \rho}\right)$ is bounded on $\mathbb{R}^{n}$ where $p_{k}$ runs over all vertices of $P$.

For each $\alpha \in(0,1]$, we define $\beta=\beta(\alpha)=\left(\beta_{1}, \beta_{2}, \ldots, \beta_{N}\right)$ by $\beta_{j}=\frac{l_{j}\left(P_{c}\right)}{l_{j}(0)} \alpha$.
Lemma 3.4. For any $\alpha \in(0,1]$, there exists a $C_{\beta(\alpha)}^{\infty}$ conical toric Kähler metric $\omega$ such that
$$\operatorname{Ric}(\omega)=\alpha \theta+(1-\alpha)[D(\tau)],$$
where $\theta \in c_{1}(X)$ is a fixed $C_{\beta(\alpha)}^{\infty}$ toric Kähler metric and $\tau=\frac{\alpha}{1-\alpha} P_{c}$. In particular, $\operatorname{Ric}(\omega)>0$, if $\alpha \in(0, R(X))$.

Proof. It suffices to prove for $\alpha \in(0,1)$. Let $\hat{u}(x)=\sum_{j} \beta_{j}^{-1} l_{j}(x) \log l_{j}(x)$ for $\beta_{j}=\frac{l_{j}\left(P_{c}\right)}{l_{j}(0)} \alpha$. Let $\hat{\phi}=\mathcal{L} \hat{u}$ and $\hat{\omega}=\sqrt{-1} \partial \bar{\partial} \hat{\phi}$. Then there exists a $C_{\beta(\alpha)}^{\infty}$ real valued (1,1)-form $\eta \in c_{1}(X)$ and a divisor $D(\tau)$ with $\tau=-\frac{\alpha}{1-\alpha} P_{c}$ such that
$$\sqrt{-1} \partial \bar{\partial} \log \hat{\omega}^{n}=\alpha \eta+(1-\alpha)[D(\tau)] .$$
This is because along each $D_{j}$ defined by $l_{j}(x)=0, \hat{\omega}^{n}$ has a pole of order
$$1-\beta_{j}=1-l_{j}\left(P_{c}\right) \alpha$$
and
$$(1-\alpha) D(\tau)=(1-\alpha)\left(\sum_{j} l_{j}\left(\frac{\alpha}{1-\alpha} P_{c}\right) D_{j}\right)=\sum_{j}\left(1-l_{j}\left(P_{c}\right) \alpha\right) D_{j} .$$

Since $\eta \in c_{1}(X)$ is $C_{\beta(\alpha)}^{\infty}$, there exists $\psi \in C_{\beta(\alpha)}^{\infty}$ such that $\eta+\sqrt{-1} \partial \bar{\partial} \psi$ is a $C_{\beta(\alpha)}^{\infty}$ toric Kähler metric. We can assume that $\int_{X_{P}} e^{\psi} \hat{\omega}^{n}=\int_{X_{P}} \hat{\omega}^{n}$ after a constant translation.

Then by Proposition 3.2, the following equation
$$(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{\psi} \hat{\omega}^{n}, \sup _{X_{P}} \varphi=0$$
admits a unique $C_{\beta(\alpha)}^{\infty}$ solution $\varphi$. By letting $\omega=\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \varphi$ and $\theta=\eta+\sqrt{-1} \partial \bar{\partial} \psi$, we have
$$\left.\operatorname{Ric}(\omega)=\alpha \theta+(1-\alpha)\left[D_{( } \tau\right)\right] .$$ \(\square\)

By Lemma 3.4, we can choose a $C_{\beta(\alpha)}^{\infty}$ Kähler potential $\phi_{0}$ with $\omega_{0}=\sqrt{-1} \partial \bar{\partial} \phi_{0}$ such that
$$\operatorname{Ric}\left(\omega_{0}\right)=\alpha \theta+(1-\alpha) D(\tau)$$
for a $C_{\beta(\alpha)}^{\infty}\left(X_{P}\right)$ Kähler metric $\theta \in c_{1}\left(X_{P}\right)$ and $\tau=\frac{\alpha}{1-\alpha} P_{c}$ if $\alpha \neq 0$. Let
$$w=\frac{1}{\alpha}\left(-\alpha P_{c} \cdot \rho-\log \operatorname{det}\left(\nabla^{2} \phi_{0}\right)\right) .$$
Then
$$\sqrt{-1} \partial \bar{\partial} w=\theta$$
and $|w-\hat{\phi}|$ is uniformly bounded by the argument in Lemma 3.4. This implies that $w$ is a $C_{\beta(\alpha)}^{\infty}$ Kähler potential and we have
$$\operatorname{det}\left(\nabla^{2} \phi_{0}\right)=e^{-\alpha\left(w-P_{c} \cdot \rho\right)} .$$

We will then define the following continuity method for a family of Monge-Ampère equations for $t \in[0, \alpha]$
$$\operatorname{det}\left(\nabla^{2} \phi_{t}\right)=e^{-t\left(\phi_{t}-P_{c} \cdot \rho\right)-(\alpha-t) w} .$$
Let $\varphi_{t}=\phi_{t}-\phi_{0}$ and define $C_{\beta(\alpha)}^{\infty}$ functions $h_{\omega_{0}}$ and $h_{\theta}$ on $X_{P}$ by
$$-\sqrt{-1} \partial \bar{\partial} \log \omega_{0}^{n}-\sqrt{-1} \partial \bar{\partial} h_{\omega_{0}}=\alpha \omega_{0}+(1-\alpha)[D(\tau)]$$
and
$$-\sqrt{-1} \partial \bar{\partial} \log \theta^{n}-\sqrt{-1} \partial \bar{\partial} h_{\theta}=\alpha \theta+(1-\alpha)[D(\tau)], \int_{X_{P}} e^{h_{\theta}} \theta^{n}=\int_{X_{P}} \theta^{n}$$
Then equation (3.36) is equivalent to
$$\left(\sqrt{-1} \partial \bar{\partial} \omega_{0}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=e^{-t \varphi_{t}}\left(e^{h_{\omega_{0}} \omega_{0}}\right)^{\frac{t}{\alpha}}\left(e^{h_{\theta}} \theta\right)^{\frac{\alpha-t}{\alpha}},$$
where $h_{\omega_{0}}$ and $h_{\theta}$ are $C_{\beta(\alpha)}^{\infty}$ on $X_{P}$ with
$$-\sqrt{-1} \partial \bar{\partial} \log \omega_{0}^{n}-\sqrt{-1} \partial \bar{\partial} h_{\omega_{0}}=\alpha \omega_{0}+(1-\alpha)[D(\tau)],-\sqrt{-1} \partial \bar{\partial} \log \theta^{n}-\sqrt{-1} \partial \bar{\partial} h_{\theta_{0}}=\alpha \theta+(1-\alpha)[D(\tau)]$$
Let
$$S=\left\{t \in[0, \alpha] \mid \text { (3.36) is solvable for } t \text { with } \sqrt{-1} \partial \bar{\partial} \phi_{t} \in C_{\beta}^{\infty}\left(X_{P}\right)\right\} \text {. }$$
Obviously, $\phi_{0}$ solves (3.36) for $t=0$ and so $S \neq \phi$. Notice that
$$\operatorname{Ric}\left(\omega_{t}\right)=t \omega_{t}+(\alpha-t) \theta+(1-\alpha)[D(\tau)] \geq t \omega_{t}$$
for $t \in[0, \alpha]$ and $\tau=\frac{\alpha}{1-\alpha} P_{c}$ if $\alpha \neq 1$. It implies that the first eigenvalue of the Laplace operator $\Delta_{t}=\operatorname{tr}_{\omega_{t}}(\sqrt{-1} \partial \bar{\partial})$ is strictly greater than $t$. By the argument in Proposition 3.2, $S$ is open and it suffices to show that $S$ is closed by proving uniform a priori estimates for $\phi_{t}-\phi_{0}$.

Proposition 3.3. There exists $C>0$ such that for all $t \in[0, \alpha]$,
$$\left\|\phi_{t}-\phi_{0}\right\|_{L^{\infty}\left(\mathbb{R}^{n}\right)} \leq C .$$

Proof. We fix some positive $\epsilon_{0} \in S$. We let
$$\Phi_{t}=\alpha^{-1}\left(\phi_{t}-P_{c} \cdot \rho\right) \text { and } W=\alpha^{-1}\left(w-P_{c} \cdot \rho\right) .$$
Then the equation (3.36) becomes
$$\operatorname{det} \nabla^{2} \Phi_{t}=e^{-\left(\Phi_{t}+W\right)} .$$
Let $W_{t}=\Phi_{t}+W$. Immediately, we can see that the moment map with respect to $\Phi_{t}$ is given by
$$F_{t}: \nabla \Phi_{t} \rightarrow P-P_{c}$$
whose image is the translation of $P$ by $-P_{c}$. In particular, the Barycenter of the new polytope $P-P_{c}$ coincides with the origin.

Suppose
$$m_{t}=W_{t}\left(\rho_{t}\right)=\inf _{\mathbb{R}^{n}} W_{t}(\rho)$$
for a unique $\rho_{t} \in \mathbb{R}^{n}$ since $W_{t}$ is asymopotically equivalent to $\log \left(\sum e^{\left(p_{k}-P_{c}\right) \cdot \rho}\right)$ where $p_{k}$ are the vertices of $P$. We can apply the same argument by Wang-Zhu in [50]. First one can show by John's lemma and the maximum principle (see Lemma 3.1, 3.2 in [50]), that there exists $C>0$ such that for all $t \in\left[\epsilon_{0}, \alpha\right]$,
$$m_{t}=W_{t}\left(\rho_{t}\right)=\inf _{\mathbb{R}^{n}} W_{t}(\rho) \leq C .$$
Then by making use of the fact that the Barycenter of $P-P_{c}$ lies at the origin $O$, the same argument in [50] (Lemma 3.3) shows that there exists $C>0$ such that for all $t \in\left[\epsilon_{0}, \alpha\right]$,
$$\left|\rho_{t}\right| \leq C .$$
This then implies that
$$\varphi_{t}=\alpha^{-1}\left(\Phi_{t}-W\right)$$
is uniformly bounded above for $t \in\left[\epsilon_{0}, \alpha\right]$ by the same argument in Lemma 3.4 in [50].
The uniform lower bound of $\varphi_{t}$ can be obtained either by the Harnack inequality
$$-\inf _{X_{P}} \varphi_{t} \leq C\left(1+\sup _{X_{P}} \varphi_{t}\right)$$
adapted from the smooth case or directly by the argument in Lemma 3.5 in [50]. \(\square\)

Lemma 3.5. For any $k \geq 0$, there exists $C_{k}>0$ such that for all $t \in[0, \alpha]$,
$$\left\|\varphi_{t}\right\|_{C^{k}\left(X_{P}\right)} \leq C_{k} .$$

Proof. The Laplace $\Delta_{\beta(\alpha), t} \varphi_{t}$ is uniformly bounded by Yau's estimates after lifting the calculations to the $\beta(\alpha)$-covering space as in the proof of Proposition 3.2. The $C^{3}$-estimates and the Schauder estimates can be applied in the same way. \(\square\)

Theorem 3.3. Let $X_{P}$ be a toric Fano manifold.
\begin{itemize}
\item[(1)] For any $\beta \in\left(0, R\left(X_{P}\right)\right)$, there exist a unique smooth toric conical Kähler-Einstein metric $\omega$ and a unique effective toric $\mathbb{R}$-divisor $D_{\beta} \in\left|-K_{X}\right|$ satisfying
$$\operatorname{Ric}(\omega)=\beta \omega+(1-\beta)\left[D_{\beta}\right] .$$
\end{itemize}
\begin{itemize}
\item[(2)] For $\beta=R\left(X_{P}\right)$, there exists a unique smooth toric conical Kähler-Einstein metric $\omega$ satisfying
$$\operatorname{Ric}(\omega)=R\left(X_{P}\right) \omega+\left(1-R\left(X_{P}\right)\right)\left[D_{P}\right]$$
for an effective $\mathbb{Q}$-divisor $D_{P}$ in $c_{1}(X)$. In particular, if $D_{j}$ is the toric divisor associated to the face defined by $l_{j}(x)=v_{j} \cdot x+\lambda_{j}=0$, then
$$D_{P}=\sum_{j} \frac{1-\beta_{j}}{1-R(X)} D_{j}, \beta_{j}=\frac{l_{j}\left(P_{c}\right)}{l_{j}(0)} R\left(X_{P}\right)$$
and the cone angle of $\omega$ along $D_{j}$ is $2 \pi \beta_{i}$, if $R(X)<1$.
\item[(3)] For $\beta \in(R(X), 1]$, there does not exist a smooth toric conical Kähler-Einstein metric $\omega$ satisfying
$$\operatorname{Ric}(\omega)=\beta \omega+(1-\beta)[D],$$
with an effective $\mathbb{R}$-divisor $D_{\beta}$ in $\left[-K_{X}\right]$.
\end{itemize}

Proof. (1) and (2) are proved by the uniform estimates from Lemma 3.5. If $\beta>R\left(X_{P}\right)$, there still exists a smooth conical Kähler-Einstein metric satisfying $\operatorname{Ric}(\omega)=\beta \omega+(1-$ $\beta)\left[D_{\beta}\right]$ for some toric divisor $D$, however, by Lemma 3.2, $D$ is not effective and so (3) is proved. \(\square\)

Corollary 3.1. Let $X$ be a Fano toric manifold and $\omega \in c_{1}(X)$ be a smooth Kähler metric. We define
$$F_{\omega, \alpha}(\varphi)=J_{\omega}(\varphi)-\frac{1}{V} \int_{X} \varphi \omega^{n}-\frac{1}{\alpha} \log \frac{1}{V} \int_{X} e^{-\alpha \varphi} \omega^{n}$$
for all $\varphi \in C^{\infty}(X) \cap P S H(X, \omega)$. Suppose $R(X)<1$. Then
\begin{itemize}
\item[(1)] for $\alpha \in(0, R(X)), F_{\omega, \alpha}$ is $J$-proper.
\item[(2)] for $\alpha=R(X), F_{\omega, \alpha}$ is bounded below.
\item[(3)] for $\alpha \in(R(X), 1], \inf _{\varphi \in P S H(X, \omega) \cap C^{\infty}(X)} F_{\omega, \alpha}(\varphi)=-\infty$.
\end{itemize}

Proof. It suffices to prove (2) by Corollary 2.2 . This can be proved by modifying the argument in [7, 5]. By Theorem 3.3, there exists a unique $\left(S^{1}\right)^{n}$-invariant $\psi \in L^{\infty}\left(X_{P}\right) \cap$ $P S H\left(X_{P}, \omega\right)$ satisfying
$$(\omega+\sqrt{-1} \partial \bar{\partial} \psi)=e^{-\alpha \psi} \mu, \quad \mu=\left(\Omega_{\omega}\right)^{\alpha}\left(\Omega_{D}\right)^{1-\alpha},$$
where $\Omega_{\omega}$ is a smooth volume form with $\sqrt{-1} \partial \bar{\partial} \log \Omega_{\omega}=-\omega$ and $\Omega_{D}$ is a positive $(n, n)$ -current with $-\sqrt{-1} \partial \bar{\partial} \log \Omega_{D}=[D]$ and $D=D\left(\frac{\alpha}{1-\alpha} P_{c}\right)$. For any $\varphi \in \operatorname{PSH}(X, \omega) \cap$ $L^{\infty}(X)$, let $\varphi_{t}$ be the weak geodesic $\varphi_{t}$ joining $\psi$ and $\varphi$ with $\varphi_{0}=\psi$ and $\varphi_{1}=\varphi$. Then the modified functional
$$f(t)=\mathcal{F}_{\omega, \alpha}\left(\varphi_{t}\right)=J_{\omega}\left(\varphi_{t}\right)-\frac{1}{V} \int_{X_{P}} \varphi_{t} \omega^{n}-\frac{1}{\alpha} \log \frac{1}{V} \int_{X_{P}} e^{-\alpha \varphi} \mu$$
is convex on $[0,1]$ and $f^{\prime}(0) \geq 0$ by applying the same argument in Theorem 6.2 in [7]. This shows that $\mathcal{F}_{\omega, \alpha}$ is bounded below and since $\Omega_{D}$ is bounded below away from 0 , and therefore $F_{\omega, \alpha}$ is bounded from below as well. \(\square\)

Example 3.2. Let $X$ be $\mathbb{P}^{2}$ blown-up at one point. Then $R(X)=6 / 7$ shown in [40] and $X$ admits a holomorphic $\mathbb{P}^{1}$ fibre bundle $\pi: X \rightarrow \mathbb{P}^{1}$. Let $D_{\infty}$ be the infinity section of $\pi$ and $H_{1}$ and $H_{2}$ be the two toric $P^{1}$ fibre of $\pi$. Then the divisor $D_{P}$ in the equation (3.40) is given by
$$D_{P}=2 D_{\infty}+\left(H_{1}+H_{2}\right) / 2 .$$

We remark that for $\beta \in(R(X), 1]$, there exists a smooth toric conical Kähler-Einstein metric in $c_{1}\left(X_{P}\right)$ satisfying $\operatorname{Ric}(g)=\beta g+(1-\beta)\left[D_{\beta}\right]$ for some toric divisor $D_{\beta}$ in $c_{1}\left(X_{P}\right)$ which can not be effective. However, it is not a conical Kähler metric we are interested in, because the Ricci current of such Kähler-Einstein metric is not bounded below. We also notice that in the case of $\beta=R(X)<1$, the conical Kähler-Einstein metric is not necessarily invariant under the maximal compact subgroup of the automorphism group of $X$ by the following example.

Example 3.3. Let $X$ be $\mathbb{P}^{2}$ blown-up at one point. It is a compactification of $\mathbb{C}^{2} \backslash\{0\}$ by adding one divisor $D_{0}=\mathbb{P}^{1}$ at 0 and another divisor $D_{\infty}=\mathbb{P}^{1}$ at $\infty$. The maximum compact group of the automorphism group of $X$ is $U(2)$. The only divisor in $c_{1}(X)$ fixed by the U(2)-action is given by
$$D=3\left[D_{\infty}\right]-\left[D_{0}\right] .$$
Therefore, there does not exists a smooth conical Kähler-Einstein metric on $X$ with positive Ricci current. In fact, there does not exist any conical Kähler-Einstein metric for such D by the following observation, although one can look for complete conical Kähler-Einstein metric in this case.

Let $z=\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}$ and $\rho=\log |z|^{2}=\log \left|z_{1}\right|^{2}+\left|z_{2}\right|^{2} \in \mathbb{R}$. Then a convex function $u=u(\rho)$ satisfies the Calabi symmetry if
\begin{itemize}
\item[(1)] $u^{\prime \prime}>0$,
\item[(2)] there exists $0<a<b$ and $\beta_{1}, \beta_{2}>0$ such that $U_{0}^{\prime}(0)>0, U_{\infty}^{\prime}(0)>0$, where $U_{0}\left(e^{\beta_{1} \rho}\right)=u(\rho)-a \rho$ and $U_{\infty}\left(e^{-\beta_{2} \rho}\right)=u(\rho)-b \rho$.
\end{itemize}
Then $\sqrt{-1} \partial \bar{\partial} u$ extends to a smooth conical Kähler metric $\omega_{u}$ on $X$. In particular, if we choose $b=3$ and $a=1, \omega_{u} \in c_{1}(X)$. The conical Kähler-Einstein equation for $\omega_{u}$ is given by the following ODE
$$u^{\prime} u^{\prime \prime}=e^{2 \rho-\alpha u} .$$
Differentiating both sides after taking the log, we have
$$\frac{u^{\prime \prime \prime}}{u^{\prime \prime}}+\frac{u^{\prime \prime}}{u^{\prime}}=2-\alpha u^{\prime} .$$
Let $x=u^{\prime}$ and $Y(x)=u^{\prime \prime}(\rho)$. Then we have
$$Y^{\prime}(x)+\left(x^{-1}+\alpha\right) Y(x)=2, \quad Y(1)=Y(3)=0$$
and so
$$Y(x)=\frac{2}{\alpha}-\frac{2}{\alpha^{2} x}+\frac{c}{x e^{\alpha x}},(3 \alpha-1) e^{2 \alpha}-\alpha+1=0 .$$
Hence by the monotonicity of $(3 \alpha-1) e^{2 \alpha}-\alpha+1, \alpha=0$ but it contradicts the assumption $u^{\prime} u^{\prime \prime}(\infty)=0$. On the other hand, there exist smooth conical Kähler-Einstein metrics in $b\left[D_{\infty}\right]-a\left[D_{0}\right]$ for some $0<a<b$ by solving the above ODE in the same way.

\section*{4. The Chern number inequality}
4.1. Curvature estimates. In this section, we will derive some curvature estimates for a smooth conical Kähler metric whose Ricci curvature is bounded.

Let $D$ be the smooth simple divisor of $X$. At each point $p$ on $D$, we can use the following holomorphic local coordinates
$$z=(y, \xi)=\left(z_{1}, \ldots, z_{n-1}, z_{n}\right), y=\left(z_{1}, \ldots, z_{n-1}\right), \xi=z_{n}$$
and $D$ is locally defined by $\xi=0$. We write $\xi=r^{1 / \beta} e^{i \theta}$ for $\theta \in[0,2 \pi)$. We use Greek letters $\alpha, \beta, \ldots$ as indices for $1, \ldots, n$ and letters $i, j, \ldots$ for $1, \ldots, n-1$.

Let us recall the following result by Jeffres, Mazzeo and Rubinstein in [18] on a complete asymptotic expansion of smooth conical Kähler metrics. .

Proposition 4.1. ([18, Proposition 4.3]) Let $\omega$ be a smooth conical Kähler metric with conical singularity along a smooth simple divisor $D$ of angle $2 \pi \beta$. Suppose $\varphi$ is a local potential of $\omega$, i.e., $\omega=\sqrt{-1} \partial \bar{\partial} \varphi$ in a neighborhood of a conical point $(y, \xi)$, then the asymptotic exapansion of $\varphi$ takes the following form
$$\varphi(r, \theta, y) \sim \sum_{j, k, l \geq 0} a_{j k l}(\theta, z) r^{j+\frac{k}{\beta}}(\log r)^{l} .$$
In particular, if the Ricci curvature of $\omega$ is bounded and $\beta \in(1 / 2,1), \varphi$ has the following expansion
$$\varphi(r, \theta, y)=a_{00}(y)+\left(a_{01}(y) \sin \theta+b_{01}(y) \cos \theta\right) r^{1 / \beta}+a_{20}(y) r^{2}+O\left(r^{2+\epsilon}\right)$$
for some $\epsilon(\beta)>0$.
When the Ricci curvature is bounded and $\beta \in(1 / 2,1)$,
$$\varphi=a(y)+b(y)(\xi+\bar{\xi})+\sqrt{-1} c(y)(\xi-\bar{\xi})+d(y)|\xi|^{2 \beta}+o\left(|\xi|^{2 \beta+\epsilon}\right)$$
for some $\epsilon>0$. From now on in this section, we will always assume that $g$ is a conical Kähler metric on $X$ with cone angle $2 \pi \beta$ for $\beta \in(1 / 2,1)$ along the simple smooth divisor $D$, in addition, the Ricci curvature of $g$ is bounded.

The following lemma can be obtained by straightforward calculations.
Lemma 4.1. Let $g$ be a smooth conical Kähler metric with cone angle $2 \pi \beta$ along a smooth simple divisor $D$ for $\beta \in(0,1)$. Let $o(1)$ be the quantity satisfying $\lim _{|\xi| \rightarrow 0} o(1)=0$. Then
$$\begin{gathered}
g_{z_{i} \bar{z}_{j}} \sim \delta_{i j}+o(1) \\
g_{\xi \bar{\xi}} \sim|\xi|^{-2(1-\beta)}+o\left(|\xi|^{-2(1-\beta)}\right) . \\
g_{z_{i} \bar{\xi}} \sim O(1) .
\end{gathered}$$

By taking the inverse, we have the following corollary from Lemma 4.1.
Corollary 4.1. Let $g$ be a smooth conical Kähler metric with cone angle $2 \pi \beta$ along a smooth simple divisor $D$ for $\beta \in(0,1)$.
$$\begin{gathered}
g^{z_{i} \bar{z}_{j}} \sim \delta_{i j}+o(1) \\
g^{\xi \bar{\xi}} \sim|\xi|^{2(1-\beta)}+o\left(|\xi|^{2(1-\beta)}\right)
\end{gathered}$$
$$g^{z_{i} \bar{\xi}} \sim|\xi|^{2(1-\beta)} .$$

The following lemmas give the estimates for the curvature tensor of $g$.
Lemma 4.2. Let $g$ be a smooth conical Kähler metric with cone angle $2 \pi \beta$ along a smooth simple divisor $D$ for $\beta \in(0,1)$. If the Ricci curvature of $g$ is bounded, then
$$\begin{aligned}
R_{z_{i} \bar{z}_{j} z_{k} \bar{z}_{l}} & \sim R_{z_{i} \bar{z}_{j} z_{k} \bar{\xi}}=O(1) \\
R_{z_{i} \bar{z}_{j} \xi \bar{\xi}} & =O\left(|\xi|^{-2(1-\beta)}\right. \\
R_{\xi \bar{z}_{j} \xi \bar{z}_{l}} & =O\left(|\xi|^{-1}\right) \\
R_{\xi \bar{\xi} \xi \bar{z}_{l}} & =O\left(|\xi|^{-1}\right) \\
R_{\xi \bar{\xi} \xi \bar{\xi}} & =O\left(|\xi|^{-\max (1,4(1-\beta))}\right) .
\end{aligned}$$
Proof. The estimates (4.49), (4.50) and (4.51) can be shown by straightforward calculation using the curvature formula
$$R_{\alpha \bar{\beta} \gamma \bar{\zeta}}=-g_{\alpha \bar{\beta}, \gamma \bar{\zeta}}+g^{\mu \bar{\nu}} g_{\alpha \bar{\nu}, \gamma} g_{\mu \bar{\beta}, \bar{\zeta}} .$$
The estimates (4.52) and (4.53) follow by combining the boundness of the Ricci curvature and the estimates (4.50) and (4.51). \(\square\)

Corollary 4.2. Let $g$ be a smooth conical Kähler metric with cone angle $2 \pi \beta$ along a smooth simple divisor $D$ for $\beta \in[1 / 2,1)$. If the Ricci curvature of $g$ is bounded, then
$$\begin{gathered}
R_{\xi, z_{k} \bar{z}_{l}}^{z_{i}} \sim R_{\xi, z_{k} \bar{z}_{l}}^{\xi}=O(1) . \\
R_{z_{p}, z_{k} \bar{z}_{l}}^{z_{i}} \sim R_{z_{p}, z_{k} \bar{z}_{l}}^{\xi}=O\left(|\xi|^{2(1-\beta)}\right) .
\end{gathered}$$

From the curvature estimates, we immediately have the following proposition.
Theorem 4.1. Let $g$ be a smooth conical Kähler metric with cone angle $2 \pi \beta$ along a smooth simple divisor $D$ for $\beta \in(0,1)$. If the Ricci curvature of $g$ is bounded, then We have the following pointwise estimates for $\left|R_{m}\right|^{2}$
$$|R m(g)|_{g}^{2}=O\left(|\xi|^{-2+4(1-\beta)}\right)$$
Consequently, the $L^{2}$ - norm of $R m(g)$ is bounded, i.e., there exists $C>0$ such that
$$\int_{X}|\operatorname{Rm}(g)|_{g}^{2} d \operatorname{Vol}(g) \leq C .$$
4.2. Chern forms for conical Kähler metrics. Let $g$ be a smooth conical Kähler metric with cone angle $2 \pi \beta$ along a smooth simple divisor $D$. We let $\theta$ be the connection form on the tangent bundle $T X$ induced by $g$, so locally we may write
$$\theta_{\gamma}^{\alpha}=g^{\alpha \bar{\beta}} g_{\gamma \bar{\beta}, \eta} d z_{\eta}$$
and $\Omega_{\gamma}^{\alpha}=\bar{\partial} \theta_{\gamma}^{\alpha}$ be the curvature form of $\theta$. Then the total Chern class is defined by
$$\operatorname{det}(t I+\Omega)=\sum_{i=0}^{n} t^{2(n-i)} c_{i}(\Omega)$$
and let $P_{i}\left(\Omega_{1}, \ldots, \Omega_{n}\right)$ being the polarization of $c_{i}(\Omega)=c_{i}(X, g)$ for the conical metric $g$.
Let $g_{0}$ be a smooth Kähler metric and $\theta_{0}$ be the connection induced by $g_{0}$ as
$$\left(\theta_{0}\right)_{\gamma}^{\alpha}=\left(g_{0}\right)^{\alpha \bar{\beta}}\left(g_{0}\right)_{\gamma \bar{\beta}, \eta} d z_{\eta} .$$
Then $\Omega_{0}=\sqrt{-1} \partial \theta_{0}$ is the curvature form of $\theta_{0}$.
Let $\theta_{t}=t \theta+(1-t) \theta_{0}$ with curvature
$$\Omega_{t}=\bar{\partial} \theta_{t}=t \Omega+(1-t) \Omega_{0} .$$
Then we have
$$c_{2}(X, \omega)-c_{2}\left(X, \omega_{0}\right)=2 \sqrt{-1} \int_{0}^{1} \bar{\partial} P_{2}\left(\theta-\theta_{0}, \Omega_{t}\right) d t$$

We will construct connections on the divisor $D$ from $\theta$ and $\theta_{0}$. Let $p$ be a point in the divisor $D$. We can choose holomorphic local coordinates
$$z=\left(z_{1}, \ldots, z_{n}\right), \xi=z_{n}$$
such that $D$ is locally defined by $\xi=0$ as in section 4.1.
Definition 4.1. We define $H$ and $H_{0}$ locally by
$$H_{i \bar{j}}=g_{i \bar{j}}, H^{i \bar{j}}=\left(H^{-1}\right)_{i \bar{j}}, H_{n \bar{j}}=g_{n \bar{j}},$$
and
$$\left(H_{0}\right)_{i \bar{j}}=\left(g_{0}\right)_{i \bar{j}},\left(H_{0}\right)^{i \bar{j}}=\left(H_{0}^{-1}\right)_{i \bar{j}},\left(H_{0}\right)_{n \bar{j}}=\left(g_{0}\right)_{n \bar{j}} .$$

Definition 4.2. For each coordinate system $(z, \xi)$ chosen as above, we define $(1,0)$ - forms $\theta_{D}$ and $\theta_{0, D}$ locally by
$$\theta_{D}=\left.\left(\theta_{i}^{i}\right)\right|_{D}$$
and
$$\theta_{0, D}=\left.\left(\theta_{0}\right)_{i}^{i}\right|_{D}+\left.H^{i \bar{j}} H_{n \bar{j}}\left(\theta_{0}\right)_{i}^{n}\right|_{D} .$$

Lemma 4.3. The $(1,0)$-form
$$\theta_{D}=\left(\left.H^{i \bar{j}} H_{i \bar{j}, k}\right|_{D}\right) d z_{k}=\left.\partial \log \operatorname{det} H\right|_{D}$$
defines a global smooth Chern connection of the anti-canonical line bundle of $D$. In particular, its curvature form $\sqrt{-1} \bar{\partial} \theta_{D}$ is a smooth closed real (1, 1)-form in $c_{1}(D)$.

Proof. By Corollary 4.1, we have $\left.g^{i \bar{n}}\right|_{D}=0$ and hence
$$\left(\theta_{D}\right)_{i}^{i}=g^{i \bar{\beta}} g_{i \bar{\beta}, k} d z_{k}=\left(\left.H^{i \bar{j}} H_{i \bar{j}, k}\right|_{D}\right) d z_{k}=\partial\left(\left.\log \operatorname{det} H\right|_{D}\right)=\partial \log \left(\left.\omega\right|_{D}\right)^{n-1} .$$
By Proposition 4.1, the regular part of $\omega$ restricted to $D$ is a smooth Kähler form from the expansion in Proposition 4.1 and for different holomorphic local coordinates $z=$ $\left(z_{1}, \ldots, z_{n-1}\right)$ and $w=\left(w_{1}, \ldots, w_{n-1}\right)$ on $D$,
$$\theta_{D}(z)=\theta_{D}(w)+\partial \log \left|\operatorname{det}\left(\frac{\partial z_{i}}{\partial w_{j}}\right)\right|^{2} .$$

Therefore $\theta_{D}$ defines a smooth connection on anti-canonical bundle of $D$. \(\square\)

Lemma 4.4. The $(1,0)$-form
$$\begin{aligned}
\theta_{0, D} & =\left.\left(\left(\theta_{0}\right)_{i}^{i}+\left(H^{i \bar{j}} H_{n \bar{j}}\right)\left(\theta_{0}\right)_{i}^{n}\right)\right|_{D} \\
& =\left(\left.\left(g_{0}\right)^{i \bar{\beta}}\left(g_{0}\right)_{i \bar{\beta}, k}\right|_{D} d z_{k}+\left.\left(H^{i \bar{j}} H_{n \bar{j}}\right)\left(g_{0}\right)^{n \bar{\beta}}\left(g_{0}\right)_{i \bar{\beta}, k}\right|_{D} d z_{k}\right)
\end{aligned}$$
defines a smooth Chern connection of the anticanonical bundle of D. In particular, $\sqrt{-1} \partial \theta_{0, D}$ is a smooth closed real $(1,1)$ form in $c_{1}(D)$.

Proof. Since $g_{0}$ is smooth and the restriction of $H_{i \bar{j}}, H^{i \bar{j}}, H_{n, \bar{j}}$ to $D$ are all smooth by the asymptotic expansion in Proposition 4.1, $\theta_{0, D}$ is locally smooth. It suffices to show that they patch together give rise to a connection.

To do that we need to show that the transformation of $\theta_{0, D}$ under different coordinate charts satisfies the cocycle condition for the anticanonical bundle of $D$. Let $\left(z_{1}, \ldots, z_{n-1}\right)$ and $\left(w_{1}, \ldots, w_{n-1}\right)$ be two holomorphic local coordinates for some neighborhood of a point $p$ in $D$. Then they extend to two holomorphic coordinates $\left(z_{1}, . ., z_{n-1}, z_{n}=\xi\right),\left(w_{1}, \ldots, w_{n-1}, w_{n}=\right.$ $\eta$ ) in a neighborhood of $p$ in $X$, where $D$ is locally defined by $\xi=0$ and $\eta=0$. Therefore for $i=1, \ldots, n-1$,
$$\left.\frac{\partial \eta}{\partial z_{i}}\right|_{D}=\left.\frac{\partial \xi}{\partial w_{i}}\right|_{D}=0 .$$
By letting
$$A_{\gamma}^{\alpha}=\frac{\partial z_{\alpha}}{\partial w_{\gamma}}, \quad B_{\gamma}^{\alpha}=\frac{\partial w_{\alpha}}{\partial z_{\gamma}}, \tilde{A}_{k}^{i}=\frac{\partial z_{i}}{\partial w_{k}}, \quad \tilde{B}_{k}^{i}=\frac{\partial w_{i}}{\partial z_{k}},$$
we obtain along $D$,
$$A=\left(\begin{array}{cc}
\tilde{A} & * \\
0 & \frac{\partial \xi}{\partial \eta}
\end{array}\right), B=\left(\begin{array}{cc}
\tilde{B} & * \\
0 & \frac{\partial \eta}{\partial \xi}
\end{array}\right), A=B^{-1}, \tilde{A}=\tilde{B}^{-1} .$$
Straighforward computations show that
$$\theta_{0, D}(z)=\theta_{0, D}(w)+\partial \log |\operatorname{det} \tilde{A}|^{2}$$
which completes the proof. \(\square\)

For any smooth conical Kähler metric $\omega$ with cone angle $2 \pi \beta$ along a smooth divisor $D$, we can define the first and second Chern classes $c_{1}(X, \omega)$ and $c_{2}(X, \omega)$. A priori, the intersection numbers among $c_{1}(X, \omega)$ and $c_{2}(X, \omega)$ might depend on the choice of $\omega$ even if the Ricci curvature of $\omega$ is bounded. The following proposition relates the $c_{1}(X, \omega)$ and $c_{2}(X, \omega)$ to $c_{1}(X)$ and $c_{2}(X)$.

Proposition 4.2. Let $D$ be a smooth simple divisor on a Kähler manifold $D$. Suppose $\omega$ is a smooth conical Kähler metric with cone angle $2 \pi \beta$ along $D$ with bounded Ricci curvature. Then
$$\int_{X} c_{1}(X, \omega) \wedge \omega^{n-1}=\left(c_{1}(X)-(1-\beta)[D]\right) \cdot[\omega]^{n-1},$$
$$\int_{X} c_{2}(X, \omega) \wedge \omega^{n-2}=\left(c_{2}(X)+(1-\beta)\left(-c_{1}(X)+[D]\right) \cdot[D]\right) \cdot[\omega]^{n-2},$$
and
$$\int_{X} c_{1}^{2}(X, \omega) \wedge \omega^{n-2}=\left(c_{1}(X)-(1-\beta)[D]\right)^{2} \cdot[\omega]^{n-2}$$
Proof. We break the proof into the following steps.
Step 1. Equation (4.60) and ((4.62)) follow easily from that observation that $\operatorname{Ric}(\omega)$ is smooth on $X \backslash D$ and it continuously extends to a closed $(1,1)$ form on $X$, which lies in the class of $c_{1}(X)$. Therefre,
$$c_{1}(X, \omega)=c_{1}(X)-(1-\beta)[D] .$$
Step 2. We first introduce a few notations. Let $\omega_{0}$ be a smooth Kähler form in the same class of $[\omega]$. Since the curvature tensor can be viewed as the curvature in the tangent bundle, we write $\theta=\left(\theta_{j}^{i}\right), \theta_{0}=\left(\theta_{j}^{i}\right)$ as the Chern connections on the tangent bundle with respect to the Kähler metric $\omega$ and $\omega_{0}$. Their curvature forms are given by $\Omega$ and $\Omega_{0}$ with
$$\Omega=\sqrt{-1 \bar{\partial}} \theta, \Omega_{0}=\sqrt{-1 \bar{\partial}} \theta_{0} .$$

Let $s$ be a defining section of $D$ and $h$ be a smooth hermitian metric on the line bundle associated to $[D]$. We define
$$X_{\epsilon}=\left\{\left.p \in X| | s\right|_{h} ^{2}(p)>\epsilon^{2}\right\} .$$

Then locally $\xi=f S$ for some holomorphic function and on $\partial X_{\epsilon}$, we have
$$\xi=f s=|f s| e^{i \sigma}=\epsilon|f| h^{-1 / 2} e^{\sqrt{-1} \sigma}, \sigma \in[0,2 \pi),$$
and
$$d \xi=\sqrt{-1} \xi d \sigma+\epsilon e^{\sqrt{-1} \sigma} d\left(|f| h^{-1 / 2}\right)$$
Let $\tau=d\left(|f| h^{-1 / 2}\right)$. Then $\tau$ is a smooth 1-form and on $\partial X_{\epsilon}$,
$$d \xi=\sqrt{-1} \xi d \sigma+\left.\epsilon \tau\right|_{\partial X_{\epsilon}}$$
Step 3. At each point $p \in \partial X_{\epsilon}$, we can apply a linear transformation to $\left(z_{1}, \ldots, z_{n-1}\right)$ such that $g_{i \bar{j}}=\delta_{i j}$ at $p$ and by rescaling $\xi$ so that $g_{n \bar{n}}=|\xi|^{-2(1-\beta)}$ near $p$. Let
$$H_{i \bar{j}}=g_{i \bar{j}}, H^{i \bar{j}}=\left(H^{-1}\right)_{i \bar{j}}, H_{n \bar{j}}=g_{n \bar{j}} .$$
then we have
$$|\xi|^{-2(1-\beta)} g^{i \bar{n}}=|\xi|^{-2(1-\beta)}\left(g_{n \bar{i}}+o(1)\right)\left(\operatorname{det}\left(g_{\alpha \beta}\right)\right)^{-1}=g_{n \bar{i}}+o(1)=H^{i \bar{j}} H_{n \bar{j}}+o(1)$$
and the connection form $\theta$ has following estimates
$$\begin{aligned}
\theta_{n}^{n} & =\theta_{\xi}^{\xi}=\sum g^{n \bar{\beta}} g_{n \bar{\beta}, \alpha} d z_{\alpha}=-(1-\beta+o(1)) \xi^{-1} d \xi+\sum_{i} o(1) \cdot d z_{i} \\
& =-(1-\beta) \sqrt{-1} d \sigma+\sum_{i} O(1) \cdot d z_{i}\left(\text { since } \xi \sim \epsilon \text { on } \partial X_{\epsilon}\right)
\end{aligned}$$
$$\begin{aligned}
\theta_{n}^{i} & =\sum g^{i \bar{\beta}} g_{n \bar{\beta}, \alpha} d z_{\alpha}=g^{i \bar{n}} g_{n \bar{n}, n} d \xi+o(1) \xi^{-1} d \xi+\sum_{i} o(1) \cdot d z_{i} \\
& =g^{i \bar{n}}\left(|\xi|^{-2(1-\beta)}\right)_{\xi} d \xi+o(1) \cdot \xi^{-1} d \xi+\sum_{i} o(1) \cdot d z_{i} \\
& =-(1-\beta) H^{i \bar{j}} H_{n \bar{j}} \xi^{-1} d \xi+o(1) \cdot \xi^{-1} d \xi+\sum_{i} o(1) \cdot d z_{i} \\
& =-\sqrt{-1}(1-\beta) H^{i \bar{j}} H_{n \bar{j}} d \sigma+o(1) \cdot d \sigma+\sum_{i} O(1) \cdot d z_{i} \\
\theta_{i}^{n} & =O(1) \cdot d \xi+\sum_{i} o(1) \cdot d z_{i}=o(1) \cdot d \sigma+\sum_{i} o(1) \cdot d z_{i} \\
\theta_{k}^{i} & =\sum_{\alpha} O(1) \cdot d z_{\alpha}=o(1) \cdot d \sigma+\sum_{i} O(1) \cdot d z_{i} .
\end{aligned}$$
On $\partial X_{\epsilon}$, by our assumption that $\beta \in(1 / 2,1)$ and using (4.63) we deduce
$$\begin{aligned}
\Omega_{n}^{n} & =\sqrt{-1} \sum_{\alpha, \beta} R_{n, \alpha \bar{\beta}}^{n} d z_{\alpha} \wedge d \bar{z}_{\beta} \\
& =\sum_{\alpha} o(1) \cdot d \sigma \wedge d z_{\alpha}+\sum_{\beta} o(1) \cdot d \sigma \wedge d \bar{z}_{\beta}+\sum_{i, j} O(1) \cdot d z_{i} \wedge d \bar{z}_{j}
\end{aligned}$$
$$\begin{aligned}
\Omega_{n}^{i}= & \left(g^{i \bar{\gamma}} g_{n \bar{\gamma}, \alpha}\right)_{\bar{\beta}} d z_{\alpha} \wedge d \bar{z}_{\beta} \\
= & \sqrt{-1}\left(g^{i \bar{n}} g_{n \bar{n}, n}\right)_{\bar{z}_{k}} d z_{k} \wedge d \xi+\sqrt{-1}\left(g^{i \bar{j}} g_{n \bar{j}, n}\right)_{\bar{z}_{k}} d z_{k} \wedge d \xi+\sqrt{-1}\left(g^{i \bar{j}} g_{n \bar{j}, k}\right)_{\bar{\xi}} d \xi \wedge d z_{k} \\
& +\sqrt{-1}\left(g^{i \bar{j}} g_{n \bar{j}, k}\right)_{\bar{z}_{l}} d \bar{z}_{l} \wedge d z_{k}+\sum_{k, l} o(1) \cdot d z_{k} \wedge d \bar{z}_{l} \\
= & \sqrt{-1}(1-\beta)\left(H^{i \bar{j}} H_{n \bar{j}}\right) \bar{z}_{k} d z_{k} \wedge \xi^{-1} d \xi+\sum_{k} o(1) \cdot d z_{k} \wedge d \sigma+\sum_{k, l} O(1) \cdot d z_{k} \wedge d \bar{z}_{l} \\
= & \sqrt{-1}(1-\beta) \bar{\partial}\left(H^{i \bar{j}} H_{n \bar{j}}\right) \wedge d \sigma+\sum_{k} o(1) \cdot d z_{k} \wedge d \sigma+\sum_{k, l} O(1) \cdot d z_{k} \wedge d \bar{z}_{l}
\end{aligned}$$
$$\begin{aligned}
\Omega_{i}^{n}= & \sqrt{-1} R_{i, \alpha \bar{\beta}}^{n} d z_{\alpha} \wedge d \bar{z}_{\beta} \\
= & \sqrt{-1} R_{i, n \bar{l}}^{n} d \xi \wedge d \bar{z}_{l}+\sqrt{-1} R_{i, k \bar{n}}^{n} d z_{k} \wedge d \bar{\xi} \\
& +\sqrt{-1} R_{i, k \bar{l}}^{n} d z_{k} \wedge d \bar{z}_{l}+o(1) d z_{k} \wedge d \bar{z}_{l} \\
= & o(1) d z_{k} \wedge d \sigma+o(1) d z_{k} \wedge d \bar{z}_{l}
\end{aligned}$$
$$\begin{aligned}
\Omega_{p}^{i}= & \sqrt{-1} R_{p, \alpha \bar{\beta}}^{i} d z_{\alpha} \wedge d \bar{z}_{\beta} \\
= & \sqrt{-1} R_{p, n \bar{l}}^{i} d \xi \wedge d \bar{z}_{l}+\sqrt{-1} R_{p, k \bar{n}}^{i} d z_{k} \wedge d \bar{\xi} \\
& +\sqrt{-1} R_{p, k \bar{l}}^{i} d z_{k} \wedge d \bar{z}_{l}+o(1) d z_{k} \wedge d \bar{z}_{l} \\
= & o(1) d z_{k} \wedge d \sigma+O(1) d z_{k} \wedge d \bar{z}_{l}
\end{aligned}$$

Step 4. By our assumption, $\omega$ is a smooth Kähler metric with cone angle $2 \pi \beta$ along $D \in X$ such that it Ricci curvature is bounded on $X \backslash D$. This implies that
$$\Omega_{\alpha}^{\alpha}=\operatorname{Ric}(\omega)=\omega_{0}-(1-\beta) \sqrt{-1} \partial \bar{\partial} \log \left|s_{D}\right|_{h}^{2}$$
where $h$ is a smooth Hermitian metric on the line bundle $\mathcal{O}_{X}(D), \omega_{0}$ is a smooth Käher metric and $s_{D} \in H^{0}\left(X, \mathcal{O}_{X}(D)\right)$ is a defining section for $D$. This implies that
$$\int_{X \backslash X_{\epsilon}} \Omega_{\alpha}^{\alpha} \wedge \omega^{n-1}=\left(\left[\omega_{0}\right]-(1-\beta)[D]\right) \cdot \omega^{n-1}+o(\epsilon)$$
from which we obtain (4.60).
Let $\theta_{t}=t \theta+(1-t) \theta_{0}$ be the connection on the tangent bundle $T X$. The curvature
$$\Omega_{t}=\sqrt{-1} \bar{\partial} \theta_{t}=t \Omega+(1-t) \Omega_{0} .$$
The transgression formula gives
$$c_{2}(X, \omega)-c_{2}\left(X, \omega_{0}\right)=2 \sqrt{-1} \int_{0}^{1} \bar{\partial} P_{2}\left(\theta-\theta_{0}, \Omega_{t}\right) d t$$
and
$$\begin{aligned}
& 2 P_{2}\left(\theta-\theta_{0}, \Omega_{t}\right) \\
= & \left(\theta-\theta_{0}\right)_{n}^{n} \wedge\left(\Omega_{t}\right)_{i}^{i}-\left(\theta-\theta_{0}\right)_{n}^{i} \wedge\left(\Omega_{t}\right)_{i}^{n}+\left(\theta-\theta_{0}\right)_{i}^{i} \wedge\left(\Omega_{t}\right)_{n}^{n}-\left(\theta-\theta_{0}\right)_{i}^{n} \wedge\left(\Omega_{t}\right)_{n}^{i} \\
& -\left(\theta-\theta_{0}\right)_{k}^{i} \wedge\left(\Omega_{t}\right)_{i}^{k} \\
= & -\sqrt{-1}(1-\beta)\left(t \bar{\partial} \theta+(1-t) \bar{\partial} \theta_{0}\right)_{i}^{i} \wedge d \sigma \\
& -(1-t)(1-\beta) \sqrt{-1}\left(H^{i \bar{j}} H_{n} \bar{\partial}\left(\theta_{0}\right)_{i}^{n}-\left(\theta-\theta_{0}\right)_{i}^{n} \wedge \bar{\partial}\left(H^{i \bar{j}} H_{n \bar{j}}\right)\right) \wedge d \sigma \\
& +o(1) d \sigma \wedge d z_{k} \wedge d \bar{z}_{l}+O(1) d z_{i} \wedge d z_{k} \wedge d \bar{z}_{l} \\
= & \sqrt{-1}(1-\beta)\left(-t \bar{\partial}\left(\theta_{i}^{i}\right) \wedge d \sigma-(1-t) \bar{\partial}\left(\left(\theta_{0}\right)_{i}^{i}+H^{i \bar{j}} H_{n \bar{j}}\left(\theta_{0}\right)_{i}^{n}\right) \wedge d \sigma\right) \\
& +o(1) d \sigma \wedge d z_{k} \wedge d \bar{z}_{l}+O(1) d z_{i} \wedge d z_{k} \wedge d \bar{z}_{l} .
\end{aligned}$$

Now let $\eta$ be a smooth Kähler form. Then
$$\begin{aligned}
& \int_{X}\left(c_{2}(X, \omega)-c_{2}\left(X, \omega_{0}\right) \wedge \eta^{n-2}\right. \\
= & 2 \sqrt{-1} \int_{0}^{1}\left(\int_{X} \bar{\partial} P_{2}\left(\theta-\theta_{0}, t \Omega+(1-t) \Omega_{0}\right) \wedge \eta^{n-2}\right) d t \\
= & 2 \int_{0}^{1}\left(\int_{\partial X_{\epsilon}} P_{2}\left(\theta-\theta_{0}, t \Omega+(1-t) \Omega_{0}\right) \wedge \eta^{n-2}\right) d t+o(1) \\
= & (1-\beta) \sqrt{-1} \int_{0}^{1} \int_{\partial X_{\epsilon}}\left(-t \bar{\partial}\left(\theta_{i}^{i}\right)-(1-t) \bar{\partial}\left(\left(\theta_{0}\right)_{i}^{i}+H^{i \bar{j}} H_{n \bar{j}}\left(\theta_{0}\right)_{i}^{n}\right)\right) \wedge d \sigma \wedge \eta^{n-2} d t+o(1) \\
= & (1-\beta) \sqrt{-1} \int_{0}^{1} \int_{D}\left(-t \bar{\partial} \theta_{D}-(1-t) \bar{\partial} \theta_{0, D}\right) \wedge\left(\left.\eta\right|_{D}\right)^{n-2} d t \\
= & (1-\beta)\left(-c_{1}(D) / 2-c_{1}(D) / 2\right) \cdot[D] \cdot[\eta]^{n-2}+o(1) \\
= & (1-\beta)\left(-c_{1}(X)+[D]\right) \cdot[D] \cdot[\eta]^{n-2}+o(1) .
\end{aligned}$$
The last three equalities follow from Lemma 4.3, Lemma 4.4 and the adjunction formula. And similarly, we have
$$\begin{aligned}
& \int_{X}\left(c_{1}^{2}(X, \omega)-c_{1}^{2}\left(X, \omega_{0}\right) \wedge \eta^{n-2}\right. \\
= & \int_{0}^{1}\left(\int_{X} \bar{\partial} Q\left(\theta-\theta_{0}, t \Omega+(1-t) \Omega_{0}\right) \wedge \eta^{n-2}\right) d t \\
= & 2(1-\beta) \int_{0}^{1} \int_{\partial X_{\epsilon}}\left(-t \bar{\partial}\left(\theta_{\alpha}^{\alpha}\right)-(1-t) \bar{\partial}\left(\left(\theta_{0}\right)_{\alpha}^{\alpha}\right)\right) \wedge d \sigma \wedge \eta^{n-2} d t+o(1) \\
(\text { by (4.64) ) })= & (1-\beta)\left(-c_{1}(X)+(1-\beta)[D]-c_{1}(X)\right) \cdot[D] \cdot[\eta]^{n-2} \\
= & \left(-2(1-\beta) c_{1}(X) \cdot[D]+(1-\beta)^{2}[D]^{2}\right) \cdot[\eta]^{n-2}
\end{aligned}$$
which is equivalent to (4.62).
Step 5. Suppose that $\omega_{0} \in[\omega]$ is a smooth Kähler form. We want to show that
$$\int_{X} c_{2}(X, \omega) \wedge \omega^{n-2}=\int_{X} c_{2}(X, \omega) \wedge \omega_{0}^{n-2}$$
and
$$\int_{X} c_{1}^{2}(X, \omega) \wedge \omega^{n-2}=\int_{X} c_{1}^{2}(X, \omega) \wedge \omega_{0}^{n-2}$$
Since the proofs are parallel to each other, we will only prove the (4.65). Let $\varphi$ be defined by $\omega=\omega_{0}+\sqrt{-1} \partial \bar{\partial} \varphi$.
$$\int_{X} c_{2}(X, \omega) \wedge\left(\omega^{n-2}-\omega_{0}^{n-2}\right)=\sum_{i=0}^{n-3} \int_{X} \sqrt{-1} \partial \bar{\partial} \varphi \wedge c_{2}(X, \omega) \wedge \omega^{i} \wedge \omega_{0}^{n-3-i}$$
For any $i=0,1, \ldots, n-3$,
$$\begin{aligned}
& \int_{X} \sqrt{-1} \partial \bar{\partial} \varphi \wedge c_{2}(X, \omega) \wedge \omega^{i} \wedge \omega_{0}^{n-3-i} \\
= & \int_{\partial X_{\epsilon}} d^{c} \varphi \wedge c_{2}(X, \omega) \wedge \omega^{i} \wedge \omega_{0}^{n-3-i}+o(1) .
\end{aligned}$$
Note that
$$\begin{aligned}
d^{c} \varphi & =o(1) d \sigma+O(1) d z_{k} \\
\omega & =o(1) d \sigma \wedge d z_{k}+o(1) d \sigma \wedge d \bar{z}_{k}+O(1) d z_{k} \wedge d \bar{z}_{l}
\end{aligned}$$
and
$$\begin{aligned}
& \Omega_{i}^{i} \wedge \Omega_{j}^{j} \sim \Omega_{j}^{i} \wedge \Omega_{i}^{j} \sim \Omega_{n}^{n} \wedge \Omega_{j}^{j} \sim \Omega_{j}^{n} \wedge \Omega_{n}^{j} \\
= & o(1) d z_{k} \wedge d \bar{z}_{l} \wedge d z_{p} \wedge d \sigma+o(1) d z_{k} \wedge d \bar{z}_{l} \wedge d \bar{z}_{q} \wedge d \sigma+O(1) d z_{k} \wedge d \bar{z}_{l} \wedge d z_{p} \wedge d \bar{z}_{q} .
\end{aligned}$$
Therefore
$$\begin{aligned}
& \int_{X} \sqrt{-1} \partial \bar{\partial} \varphi \wedge c_{2}(X, \omega) \wedge \omega^{i} \wedge \omega_{0}^{n-3-i} \\
= & \int_{\partial X_{\epsilon}} d^{c} \varphi \wedge c_{2}(X, \omega) \wedge \omega^{i} \wedge \omega_{0}^{n-3-i}+o(1) \\
= & 0
\end{aligned}$$
after letting $\epsilon$ tend to 0 .
Step 6. Finally, combining the above estimates, we obtain (4.62) and the proof of the proposition is completed. \(\square\)

One can apply similar argument shows that if $\omega$ is a smooth conical Kähler metric $\omega$ with cone angle $2 \pi \beta$ along a smooth simple divisor $D$ and if the Ricci curvature of $\omega$ is bounded, then the $n^{\text {th }}$-Chern number $c_{n}(X, \omega)$ is well-defined and does not depend on the choice of $\omega$.
4.3. The Gauss-Bonnet and signature theorems for Kähler surfaces with conical singularities. We first introduce the following definition.

Definition 4.3. Let $X$ be a Kähler surface and $\Sigma$ be a smooth holomorphic curve on $X$. If $g$ is a smooth conical Kähler metric with cone angle $2 \pi \beta$ along $\Sigma$, we define the corresponding conical Euler number and signature by
$$\chi(X, g)=\int_{X \backslash \Sigma} \frac{1}{8 \pi^{2}}\left(\frac{S^{2}}{24}+|W|^{2}-\frac{|\mathrm{Ric}|^{2}}{2}\right) d g$$
and
$$\sigma(X, g)=\frac{1}{12 \pi^{2}} \int_{X \backslash \Sigma}\left(\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}\right) d g$$
where $S$ is the scalar curvature of metric $g, W$ is the Weyl tensor for $g$ and Ric is the traceless Ricci curvature. In particular, if $\beta=1$, we recover classical characteristic class.

The Gauss-Bonnet and the signature theorems are proved in [1] for smooth compact Riemannian 4-folds with specified conical metrics with cone angle $2 \pi \beta$ along a smooth embedded Riemann surface. In particular, As an immediate consequence of Proposition 4.2 and Definition 4.3 above, we obtain the following formulas related to the recent result by Atiyah and LeBrun [1] by removing the assumption $\beta \in(0,1 / 3)$ in the Kähler case.

Proposition 4.3. Let $g$ be a smooth conical Kähler metric with angle $2 \pi \beta$ for $\beta \in(0,1]$ along a holomorphic curve $\Sigma$. If the Ricci curvature of $g$ is bounded, we have
$$\begin{aligned}
\chi(X, g) & =\chi(X)-(1-\beta) \chi(D) \\
\sigma(X, g) & =\sigma(X)-\frac{1}{3}\left(1-\beta^{2}\right)[D]^{2} .
\end{aligned}$$
Proof. To prove the statement, we apply the identity (cf. [1] )
$$\frac{1}{8 \pi^{2}}\left(\frac{S^{2}}{24}+|W|^{2}-\frac{|\stackrel{\circ}{\operatorname{Ric}}|^{2}}{2}\right) d g=c_{2}(X, g)$$
and
$$\frac{1}{12 \pi^{2}}\left(\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}\right) d g=\frac{1}{3}\left(c_{1}^{2}(X, g)-2 c_{2}(X, g)\right)$$
and the statement follows from Proposition 4.2 \(\square\)
4.4. The Chern number inequality on Fano manifolds. In this section, we will prove Theorem 1.4.

Proposition 4.4. Let $X$ be an $n$-dimensional Fano manifold. If $R(X)=1$, then the Miyaoka-Yau type inequality holds
$$c_{2}(X) \cdot c_{1}(X)^{n-2} \geq \frac{n}{2(n+1)} c_{1}(X)^{n} .$$
Proof. We fix a smooth simple divisor $D \in\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$. Such a divisor always exists by Bertini's theorem. Then for any $\beta \in(0,1)$, there exists a smooth conical Käher-Einstein metric $\omega$ satisfying $\operatorname{Ric}(\omega)=\beta g \omega+(1-\beta) m^{-1}[D]$.

By Chern-Weil theory, if we let
$$\begin{gathered}
\stackrel{\circ}{R}_{i \bar{j} k \bar{l}}=R_{i \bar{j} k \bar{l}}-\frac{\operatorname{tr}(R)}{n(n+1)}\left(g_{i \bar{j}} g_{k \bar{l}}+g_{i \bar{l}} g_{k \bar{j}}\right), \\
\stackrel{\circ}{R i c}=\operatorname{Ric}-\frac{\operatorname{tr}(R i c)}{n} g
\end{gathered}$$
be the traceless curvature and Ricci curvature tensor, we have
$$\left(\frac{2(n+1)}{n} c_{2}(X, \omega)-c_{1}^{2}(X, \omega)\right) \cdot[\omega]^{n-2}=\frac{1}{n(n-1)} \int_{X}\left(\frac{n+1}{n}|\stackrel{\circ}{R}|^{2}-\frac{n^{2}-2}{n^{2}}|\stackrel{\circ}{R i c}|^{2}\right) \omega^{n} .$$
We then have
$$\left(\frac{2(n+1)}{n} c_{2}(X, \omega)-c_{1}^{2}(X, \omega)\right) \cdot[\omega]^{n-2} \geq 0 .$$
By Proposition 4.2, we have
$$c_{1}(X, \omega)=\beta c_{1}(X), c_{2}(X, \omega)=c_{2}(X)+(1-\beta)\left(-c_{1}(X)+[D]\right) \cdot[D] .$$
This implies that
$$\left(\frac{2(n+1)}{n} c_{2}(X)-\beta^{2} c_{1}^{2}(X)\right) \cdot\left(\beta c_{1}(X)\right)^{n-2} \geq 0 .$$
The theorem then follows by letting $\beta \rightarrow 1$. \(\square\)

We also have the following lemma when $R(X)<1$ with the same argument in the proof of Proposition 4.4.

Lemma 4.5. Let $D \in\left|-K_{X}\right|$ be a smooth simple divisor. If there exists a conical Kähler-Einstein metric $g_{\beta}$ for some $\beta \in(0, R(X))$ satisfying
$$\operatorname{Ric}(g)=\beta g+(1-\beta)[D],$$
then
$$c_{2}(X) \cdot c_{1}(X)^{n-2} \geq \frac{n \beta^{2}}{2(n+1)} c_{1}(X)^{n} .$$

Theorem 1.4 is proved by combining Proposition 4.4, Lemma 4.5 and Theorem 1.2.
4.5. The Chern number inequality on minimal manifolds of general type. The following proposition is first claimed in [49], although the analytic part in the proof does not seem to be complete. The first complete proof seems to be given by Zhang [54] using the Ricci flow. In this section, we apply Proposition 4.2 to complete Tsuji's original approach.

Proposition 4.5. Let $X$ be a smooth minimal model of general type. Then
$$\left(\frac{2(n+1)}{n} c_{2}(X)-c_{1}^{2}(X)\right) \cdot\left(-c_{1}(X)\right)^{n-2} \geq 0 .$$
In particular, if the equality holds, the canonical Kähler-Einstein metric is a complex hyperbolic metric on the smooth part of the canonical model of $X$.

Proof. Fix a smooth simple ample divisor $D$ on $X$. Since $\left[K_{X}\right]+\epsilon[D]$ is a Kähler class for any $\epsilon>0$, there exists a smooth conical Kähler-Einstein metric in $\left[K_{X}\right]+\epsilon[D]$ with conical singularity along $D$ satisfying
$$\operatorname{Ric}(\omega)=-\omega+\epsilon[D] .$$
By the same argument in the proof of Proposition 4.4,
$$\left(\frac{2(n+1)}{n} c_{2}(X, \omega)-c_{1}^{2}(X, \omega)\right) \cdot\left(-c_{1}(X, \omega)\right)^{n-2} \geq \int_{X}|\stackrel{\circ}{R}(\omega)|^{2} \omega^{n} \geq 0 .$$
By standard argument from [16, 55], $\omega$ converges as $\epsilon \rightarrow 0$ to the unique Kähler-Einstein metric $g_{\text {can }}$ on the canonical model $X_{\text {can }}$ of $X$ in $C^{\infty}$ local topology away from the exceptional locus the pluricanonical system. In particular, $\omega_{\text {can }}$ is smooth on the smooth part of $X_{\text {can }}$.

By letting $\epsilon$ tends to 0, we have
$$\left(\frac{2(n+1)}{n} c_{2}(X)-c_{1}^{2}(X)\right) \cdot\left(-c_{1}(X)\right)^{n-2} \geq \int_{X}\left|\stackrel{\circ}{R}\left(\omega_{c a n}\right)\right|^{2} \omega_{c a n}^{n} \geq 0,$$
where $X_{\text {can }}^{\circ}$ is the smooth part of $X_{\text {can }}$. When the equality holds, $\stackrel{\circ}{R}\left(g_{\text {can }}\right)$ vanishes on $X_{\text {can }}^{\circ}$ and so $g_{\text {can }}$ must a complex hyperbolic metric on $X_{\text {can }}^{\circ}$. \(\square\)

Then by the estimate (4.68), we immediately obtain an $L^{2}$-bound for the curvature tensor of the canonical Kähler-Einstein metric on the regular part of the canonical model associated to a smooth minimal model of general type.

\section*{5. Discussions}

In this section, we make some speculations on the limiting behavior of the conical KählerEinstein metrics as $\beta$ tends to $R(X)$.

Conjecture 5.1. Let $X$ be a Fano manifold with $R(X)=1$. Then by Proposition 1.1, there exists a smooth simple divisor $D \in\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$such that for any $\epsilon>0$, there exists a smooth conical Kähler-Einstein metric $g_{\epsilon}$ with $\operatorname{Ric}\left(g_{\epsilon}\right)=(1-\epsilon) g_{\epsilon}+\epsilon m^{-1}[D]$ for all $\epsilon \in(0,1)$. We conjecture that $\left(X, g_{\epsilon}\right)$ converges to a $\mathbb{Q}$-Fano variety $\left(X_{\infty}, g_{\infty}\right)$ coupled with a canonical Kähler-Einstein metric $g_{\infty}$ in Gromov-Hausdorff topology.

The above conjecture is related to the recent result in [45], where the Kähler-Ricci flow is combined with the continuity method to produce a limiting Einstein metric space when $R(X)=1$. We also make a more general conjecture when $R(X) \neq 1$.

Conjecture 5.2. Let $X$ be a Fano manifold and $D$ be a smooth simple divisor in $\left|-m K_{X}\right|$ for some $m \in \mathbb{Z}^{+}$. We consider the conical Ricci flow defined by
$$\frac{\partial g}{\partial t}=-\operatorname{Ric}(g)+\beta g+m^{-1}(1-\beta)[D]$$
starting with a smooth conical Kähler metric $g_{0} \in c_{1}(X)$ with cone angle $2 \pi\left(1-(1-\beta) m^{-1}\right)$ along $D$. Then for some $m \in \mathbb{Z}^{+}$and a generic choice of $D$, we have
\begin{itemize}
\item[(1)] If $\beta \in(0, R(X))$, the flow converges to a smooth conical Kähler Einstein metric on $X$ with conical singularity along $D$.
\item[(2)] If $\beta=R(X)$, the flow converges to a singular Kähler-Einstein metric on a paired $\mathbb{Q}$-Fano variety $\left(X_{\infty}, D_{\infty}\right)$ with conical singularities along an effective $\mathbb{Q}$-divisor $D_{\infty} \in\left[-K_{X_{\infty}}\right]$.
\item[(3)] If $\beta \in(R(X), 1]$, the flow converges to a singular Kähler-Ricci soliton on a paired $\mathbb{Q}$-Fano variety $\left(X_{\infty}, D_{\infty}\right)$ with conical singularities along an effective $\mathbb{Q}$-divisor $D_{\infty} \in\left[-K_{X_{\infty}}\right]$.
\end{itemize}

Acknowledgements We would like to thank D.H. Phong, Jacob Sturm, Valentino Tosatti, Ved Datar and Bin Guo for many stimulating discussions. After we finished the first draft of the paper, we were kindly informed by Tosatti that most of the results in Theorem 1.1 and 1.2 are independently obtained by Chi Li and Song Sun [24]. We would also like to thank Chi Li and Song Sun for sending us their preprint and for their interesting comments.

\section*{References}
\begin{itemize}
\item[] [1] Atiyah, M. and Lebrun, C. Curvature, Cones, and Characteristic Numbers, arXiv:1203.6389
\item[] [2] Aubin, T. Équations du type Monge-Ampère sur les variétés kählériennes compactes, Bull. Sci. Math. (2) 102 (1978), no. 1, 63-95
\item[] [3] Bando, S. The K-energy map, almost Einstein Kähler metrics and an inequality of the Miyaoka-Yau type, Tohuku Math. Journ. 39 (1987), 231-235
\item[] [4] Bando, S. and Mabuchi, T. Uniqueness of Einstein Kähler metrics modulo connected group actions, Adv. Stud. in Pure Math. 10 (1987), 11-40
\item[] [5] Berman, B. A thermodynamical formalism for Monge-Ampere equations, Moser-Trudinger inequalities and Kähler-Einstein metrics, arXiv:1011.3976
\item[] [6] Berman, B. K-polystability of Q-Fano varieties admitting Kähler-Einstein metrics, arXiv:1205.6214
\item[] [7] Berman, R., Boucksom, S, Guedj, V. and Zeriahi,, A. A variational approach to complex Monge-Ampere equations, arXiv:0907.4490
\item[] [8] Brendle, S. Ricci flat Kähler metrics with edge singularities, arXiv:1103.5454
\item[] [9] Demailly, J-P. Appendix to I. Cheltsov and C. Shramovs article Log canonical thresholds of smooth Fano threefolds : On Tians invariant and log canonical thresholds, Uspekhi Mat. Nauk, 63:5(383) (2008), 73-180
\item[] [10] Ding, W., Remarks on the existence problem of positive Kähler-Einstein metrics, Math. Ann. 282 (1988), no. 3, 463-471
\item[] [11] Donaldson, S.K. Scalar curvature and stability of toric varieties, J. Differential Geom. 62 (2002), 289-349
\item[] [12] Donaldson, S.K. Extremal metrics on toric surfaces: a continuity method, J. Differential Geom. 79 (2008), no. 3, 389-432
\item[] [13] Donaldson, S.K. Kähler geometry on toric manifolds, and some other manifolds with large symmetry, Handbook of geometric analysis. No. 1, 2975, Adv. Lect. Math. (ALM), 7, Int. Press, Somerville, MA, 2008
\end{itemize}
[14] Donaldson, S.K. Stability, birational transformations and the Kähler-Einstein problem, arXiv:1007.4220
[15] Donaldson, S.K. Kähler metrics with cone singularities along a divisor, arXiv:1102.1196
[16] Eyssidieux, P., Guedj, V. and Zeriahi, A. Singular Kähler-Einstein metrics, J. Amer. Math. Soc. 22 (2009), no. 3, 607-639
[17] Guillemin, V. Kähler structures on toric varieties, J. Differential Geom. 40 (1994), no. 2, 285-309
[18] Jeffres,T., Mazzeo,R. and Rubinstein, Y. Kähler-Einstein metrics with edge singularities with appendix by Rubinstein Y. and Li, C., arXiv:1105.5216
[19] Kobayashi, R. Kähler-Einstein metric on an open algebraic manifold, Osaka J. Math. 21 (1984), no. 2, 399-418
[20] Kolodziej,S. The complex Monge-Ampere equation, Acta Math. 180 (1998),69-117.
[21] Li, C. Greatest lower bounds on Ricci curvature for toric Fano manifolds Adv. Math. 226 (2011), no. 6, 4921-4932.
[22] Li, C. On the limit behavior of metrics in continuity method to Kähler-Einstein problem in toric Fano case, arXiv:1012.5229
[23] Li, C. Remarks on logarithmic K-stability, arXiv:1104.0428
[24] Li, C. and Sun, S. Conic Kähler-Einstein metric revisited, preprint
[25] Li, H. On the lower bound of the K-energy and F-functional, Osaka J. Math. 45 (2008), no. 1, 253-264
[26] Luo, F. and Tian, G. Liouville equation and spherical convex polytopes, Proc. Amer. Math. Soc. 116 (1992), 1119-1129
[27] Mabuchi, T. K-energy maps integrating Futaki invariants, Tôhoku Math. Journ. 38 (1986), 575-593
[28] McOwen, R.C. Point singularities and conformal metrics on Riemann surfaces, Proc. Amer. Math. Soc. 103 (1988), 222-224
[29] Miyaoka, Y. On the Chern numbers of surfaces of general type, Invent. Math., 42 (1977), 225-237.
[30] Munteanu, O. and Szekelyhidi, G. On convergence of the Kähler-Ricci flow , Comm. Anal. Geom. 19 (2011), n. 5, 887-904
[31] Odaka, Y. and Sun,S. Testing log K-stability by blowing up formalism, arXiv:1112.1353
[32] Phong, D.H., Sesum, N. and Sturm, J. Multiplier ideal sheaves and the Khler-Ricci flow, Comm. Anal. Geom. 15 (2007), no. 3, 613-632
[33] Phong, D.H., Sturm, J., Song, J. and Weinkove, B. The Moser-Trudinger inequality on Kähler-Einstein manifolds, Amer. J. Math. 130 (2008), no. 4, 1067-1085
[34] Rubinstein, Y. On energy functionals, Kähler-Einstein metrics, and the Moser-Trudinger-Onofri neighborhood, J. Funct. Anal. 255 (2008), no. 9, 2641-2660
[35] Siu, Y.-T. Lectures on Hermitian-Einstein metrics for stable bundles and Kähler-Einstein metrics. DMV Seminar, 8. Birkhäuser Verlag, Basel, 1987
[36] Song, J. The $\alpha$-invariant on certain surfaces with symmetry groups, Trans. Amer. Math. Soc. 357 (2005), no. 1, 45-57
[37] Song, J. and Tian, G. Canonical measures and Kähler-Ricci flow, J. Amer. Math. Soc. 25 (2012), no. 2, 303-353
[38] Song, J. and Weinkove, B. Energy functionals and canonical Kähler metrics, Duke Math. J. 137 (2007), no. 1, 159-184
[39] Sun, S. Note on $K$-stability of pairs, arXiv:1108.4603
[40] Szekelyhidi, G. Greatest lower bounds on the Ricci curvature of Fano manifolds, Compositio Math. 147 (2011), 319-331
[41] Tian, G. On Kähler-Einstein metrics on certain Kähler manifolds with $c_{1}(M)>0$, Invent. Math. 89 (1987), 225-246
[42] Tian, G. On stability of the tangent bundles of Fano varieties, Internat. J. Math. 3 (1992), no. 3, 401-413
[43] Tian, G. Kähler-Einstein metrics on algebraic manifolds. Transcendental methods in algebraic geometry, 143185, Lecture Notes in Math., 1646, Springer, Berlin, 1996
[44] Tian, G. Kähler-Einstein metrics with positive scalar curvature, Invent. Math. 137 (1997), 1-37
[45] Tian, G. and Wang, B. On the structure of almost Einstein manifolds, arXiv:1202.2912
[46] Tian, G. and Yau, S.T., Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry, Mathematical aspects of string theory (San Diego, Calif., 1986), 574628, Adv. Ser. Math. Phys., 1, World Sci. Publishing, Singapore, 1987
[47] Tian, G. and Zhu, X. A nonlinear inequality of Moser-Trudinger type, Calc. Var. 10 (2000), 349-354
[48] Troyanov, M. Prescribing curvature on compact surfaces with conic singularities, Trans. Amer. Math. Soc. 324 (1991), 793-821
[49] Tsuji, Stability of tangent bundles of minimal algebraic varieties, Topology 27 (1988), no. 4, 429-442
[50] Wang, X. and Zhu, X,, Kähler-Ricci solitons on toric manifolds with positive first Chern class, Adv. Math. 188 (2004), no. 1, 87-103
[51] Yau, S.-T. On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math. 31 (1978), no. 3, 339-411
[52] Yau, S.T. Calabi's conjecture and some new results in algebraic geometry, Proc. Natl. Acad. Sci. USA, 74 (1977), 1798-1799
[53] Yau, S.-T. Open problems in geometry, Proc. Symposia Pure Math. 54 (1993), 1-28 (problem 65)
[54] Zhang, Y. Miyaoka-Yau inequality for minimal projective manifolds of general type, Proc. Amer. Math. Soc. 137 (2009), no. 8, 2749-2754
[55] Zhang, Z. On degenerate Monge-Ampère equations over closed Kähler manifolds, Int. Math. Res. Not. 2006, Art. ID 63640, 18 pp

Department of Mathematics, Rutgers University, Piscataway, NJ 08854
E-mail address: jiansong@math.rutgers.edu
Department of Mathematics, Rutgers University, Newark, NJ 07102
E-mail address: xiaowwan@rutgers.edu