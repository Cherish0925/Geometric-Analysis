---
retention_scope: session
part: 2
total_parts: 5
---

[Part 2/5 of: A continuous cusp closing process for negative Kähler- ...]

It remains to show that $H(0)=1$. To see that this is true, we approach the origin along a sequence of points in $T Y_{0} \backslash\{0\}$. Along this sequence, $\left[\left(\Psi_{0}^{-1}\right)^{*} \Omega_{0}\right] / \Omega_{\mathcal{C}} \rightarrow 1$ by the normalization chosen after the proof of Lemma 2.12, so we need to show that $\Omega_{T Y_{0}} / \Omega_{\mathcal{C}} \rightarrow 1$ as well. In fact, $\Omega_{T Y_{0}}=\Omega_{\mathcal{C}}$ on $T Y_{0} \backslash\{0\}$. The reason is that these forms are scale-invariant on the cone $T Y_{0} \backslash\{0\}$ and have the same residue at the infinity divisor $E$; compare the general construction of $\Omega_{X}$ before Theorem 2.16. \(\square\)
2.4. A new neck region between a Tian-Yau end and a hyperbolic cusp. We now return to the radial Kähler-Einstein equation (2.42) on a general $n$-dimensional cusp singularity, which already gave us the asymptotic model $\psi_{\text {cusp }}$ for the unique complete Kähler-Einstein potential on the regular part of our 2-dimensional example $\mathcal{X}_{0}$. In general, (2.42) is equivalent to
$$\frac{1}{n+1}\left(\psi^{\prime}\right)^{n+1}=e^{\psi+a}+b$$
for some constant $b$. Then we have, for any $t<t_{0}$,
$$\int_{\psi(t)}^{\psi\left(t_{0}\right)}\left(e^{\xi+a}+b\right)^{-\frac{1}{n+1}} d \xi=(n+1)^{\frac{1}{n+1}}\left(t_{0}-t\right) .$$
The case $b=0$ yields the cusp solution $\psi_{\text {cusp }}$. The case $b>0$ yields solutions that are still defined on an entire negative half-line but are not metrically complete as $t \rightarrow-\infty$. In [4, Sect 2] and [13, Ex 2.7], it was shown that the completions of these metrics may be viewed as Kähler-Einstein edge metrics on
the total space of $L$, with conical singularities along the zero section that get pushed off to infinity as $b \rightarrow 0$ while the diameter of the zero section shrinks to zero. Since we are now considering smoothings rather than resolutions of singularities, it is natural to try to use the case $b<0$.

We showed in [13] that when $b<0$, there are solutions to (2.80) which correspond to incomplete Kähler-Einstein metrics on $\left\{\delta^{-}<h \leqslant \delta^{+}\right\}$, where $\delta^{-}, \delta^{+}>0$ are constants that depend on $a, b$. In fact, (2.41) and (2.79) imply that $e^{\psi+a}+b>0$. When $b<0$, the integral on the left-hand side of (2.80) is bounded and the bound is independent of $t, t_{0}$. The purpose of this section is to study these solutions in detail. They give rise to "horn metrics" $\omega_{T}$ approximating $\omega_{\text {cusp }}$ as in Figure 2.

Convention 2.21. We will introduce geometric parameters $T<T+2 T_{0}<2 \tau<0$, and $b, T, T_{0}, \tau$ will eventually be made to depend on $\sigma$. The standing assumption is that as $\sigma \rightarrow 0$ we have that
$$T \rightarrow-\infty, \quad T_{0} \rightarrow+\infty, \quad T_{0} / T \rightarrow 0, \quad \tau \rightarrow-\infty, \quad \tau / T \rightarrow 0, \quad b \rightarrow 0, \quad b|\tau|^{n+1} \rightarrow 0 .$$
We will be proving many $O(\ldots)$ type estimates for various different quantities, and the understanding will always be that the $O(\ldots)$ holds as $\sigma \rightarrow 0$, so that (2.81) is in force.

We assume $\psi_{T}(t)$ is the solution of (2.42) such that
$$e^{\psi_{T}(T)+a}+b=0, \quad \psi_{T}(\tau)=\psi_{\text {cusp }}(\tau) .$$
Then
$$\psi_{T}(T)=\log |b|-a, \quad \psi_{T}(\tau)=-(n+1) \log (-\tau)+n \log (n+1)-a .$$
We note here that with $\omega_{T}:=i \partial \bar{\partial} \psi_{T}$ it holds that
$$e^{-\psi_{T}} \omega_{T}^{n}=i^{n^{2}} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}} .$$
Indeed, radial pluriharmonic functions are constant (cf. (2.48)), so there is a constant $C_{T}$ such that
$$e^{-\psi_{T}+C_{T}} \omega_{T}^{n}=i^{n^{2}} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}} .$$
Now by taking $t=\tau$ and noting that $\psi_{T}(\tau)=\psi_{\text {cusp }}(\tau)$ (cf. (2.82)), one has
$$i^{n^{2}} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}=e^{-\psi_{T}(\tau)+C_{T}} \omega_{T}^{n}=e^{-\psi_{\text {cusp }}(\tau)+C_{T}} \omega_{T}^{n}=e^{C_{T}} i^{n^{2}} \Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}$$
as before. So indeed $C_{T}=0$.

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Figure 2. Cusp metric $\omega_{\text {cusp }}$, horn metric $\omega_{T}$, gluing regions.}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a0f996e3-fe3b-459a-a543-f9d8a2350896-17.jpg?height=587&width=1416&top_left_y=1912&top_left_x=362}
\end{figure}

Remark 2.22. We show the relationship between $\omega_{T}$ and $\omega_{\text {cusp }}$ in Figure 2. The metric $\omega_{T}$ has a horn singularity at $t=T$, which evolves into the cusp singularity as $T \rightarrow-\infty$. Later we will see that for a fixed $T$, the horn of $\omega_{T}$ is asymptotic to a scaled copy of the Calabi model space, which allows us to carry out a gluing construction in the region $t \in\left[T+T_{0}, T+2 T_{0}\right]$ that we shaded orange in the figure ( $T_{0} \rightarrow+\infty$ but $T_{0} / T \rightarrow 0$ ). Similarly, in the green region, $t \in[2 \tau, \tau](\tau \rightarrow-\infty$ but $\tau / T \rightarrow 0)$, we can glue $\omega_{T}$ with $\omega_{\text {cusp }}$. We often refer to the region $T+2 T_{0}<t<2 \tau$ as the "new" or "middle" neck.

By (2.80),
$$\int_{\psi_{T}(T)}^{\psi_{T}(\tau)}\left(e^{\xi+a}+b\right)^{-\frac{1}{n+1}} d \xi=(n+1)^{\frac{1}{n+1}}(\tau-T)$$
(2.80) and (2.83) show that, by setting $\xi=s+\log |b|-a$,
$$\int_{0}^{-(n+1) \log |\tau|-\log |b|+n \log (n+1)}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s=(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}(\tau-T)$$
Hence we obtain the crucial relation between $T$ and $b$ :
$$T=-(n+1)^{-\frac{1}{n+1}} c(n)|b|^{-\frac{1}{n+1}}+O(\tau),$$
where
$$c(n):=\int_{0}^{\infty}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s .$$
We conclude that
$$\psi_{\text {cusp }}(T)=\log |b|-(n+1) \log c(n)+O\left(|b|^{\frac{1}{n+1}} \tau\right) .$$
Hence,
$$\psi_{c u s p}(T)-\psi_{T}(T)=-(n+1) \log c(n)+a+O\left(|b|^{\frac{1}{n+1}} \tau\right),$$
which tends to a constant as $\sigma \rightarrow 0$ by (2.81).
2.4.1. Estimates asymptotically close to the cusp (green region). Similarly to (2.80), one has
$$\int_{\psi_{T}(t)}^{\psi_{T}(\tau)}\left(e^{\xi+a}+b\right)^{-\frac{1}{n+1}} d \xi=(n+1)^{\frac{1}{n+1}}(\tau-t) .$$
Substitute $\xi=s+\psi_{T}(\tau)$. By (2.83),
$$\int_{\psi_{T}(t)-\psi_{T}(\tau)}^{0}\left(e^{s}+(n+1)^{-n} b|\tau|^{n+1}\right)^{-\frac{1}{n+1}} d s=-(n+1)\left(1-\tau^{-1} t\right) .$$
Let $c_{1}>0$ be the unique constant such that
$$\int_{-c_{1}}^{0}\left(e^{s}\right)^{-\frac{1}{n+1}} d s=n+1$$
When $t=2 \tau$, the right-hand side of (2.94) equals $n+1$. As $b<0$, we have
$$\left(e^{s}+e^{-a} b|\tau|^{n+1}\right)^{-\frac{1}{n+1}}>\left(e^{s}\right)^{-\frac{1}{n+1}}>0 .$$
By comparing (2.94) and (2.95), we derive that $\psi_{T}(2 \tau)-\psi_{T}(\tau)>-c_{1}$. By taking $b \rightarrow 0^{-}$in (2.94), we see that $\psi_{T}(t)-\psi_{T}(\tau)$ must decrease to a constant. On the other hand,
$$\int_{\psi_{\text {cusp }}(2 \tau)-\psi_{\text {cusp }}(\tau)}^{0}\left(e^{s}\right)^{-\frac{1}{n+1}} d s=n+1$$

By (2.81) and all the discussions above, $\psi_{T}(2 \tau)-\psi_{T}(\tau)$ converges to $\psi_{\text {cusp }}(2 \tau)-\psi_{\text {cusp }}(\tau)$. By (2.82), $\psi_{T}(2 \tau) \rightarrow \psi_{\text {cusp }}(2 \tau)$. Replacing $2 \tau$ by any constant in $(2 \tau, \tau)$, the same argument implies that,
$$\psi_{T}(t)-\psi_{\text {cusp }}(t)=o(1)$$
as $b \rightarrow 0^{-}$if we fix $\frac{t}{\tau}$ as a constant in [1, 2].
When $t=c \tau$ for some constant $c \in[1,2], s \geqslant \psi_{T}(t)-\psi_{T}(\tau) \geqslant-c_{1}$ in (2.94). Using that
$$\begin{aligned}
\int_{\psi_{T}(t)-\psi_{T}(\tau)}^{0}\left(e^{s}+(n+1)^{-n} b|\tau|^{n+1}\right)^{-\frac{1}{n+1}} d s & =(n+1)(c-1) \\
& =\int_{\psi_{\text {cusp }}(t)-\psi_{\text {cusp }}(\tau)}^{0}\left(e^{s}\right)^{-\frac{1}{n+1}} d s
\end{aligned}$$
we derive
$$\int_{\psi_{T}(t)-\psi_{T}(\tau)}^{0}\left(\left(e^{s}+(n+1)^{-n} b|\tau|^{n+1}\right)^{-\frac{1}{n+1}}-\left(e^{s}\right)^{-\frac{1}{n+1}}\right) d s=\int_{\psi_{c u s p}(t)-\psi_{T}(t)}^{0}\left(e^{s}\right)^{-\frac{1}{n+1}} d s$$
which shows that, for $t \in[2 \tau, \tau]$,
$$\psi_{T}(t)-\psi_{\text {cusp }}(t)=O\left(|b||\tau|^{n+1}\right) .$$

Let $\rho:=\sqrt{(n+1) / 2} \log (-t)$, which is a Busemann function of $\omega_{\text {cusp }}$. For $t \in[2 \tau, \tau], \rho$ varies by an additive constant independent of $b$. Set the normalized Busemann function
$$\tilde{\rho}(t):=\rho(t)-\rho(\tau)=\sqrt{\frac{n+1}{2}} \log \left(\frac{t}{\tau}\right),$$
whose range is $I=[0, \sqrt{(n+1) / 2} \log 2]$. Regard $t \psi_{T}^{\prime}, t^{2} \psi_{T}^{\prime \prime}$ as functions of $\tilde{\rho}$. As $b \rightarrow 0^{-}$,
$$\begin{aligned}
t \psi_{T}^{\prime} & =t(n+1)^{\frac{1}{n+1}}\left(e^{\psi_{T}+a}+b\right)^{\frac{1}{n+1}} \\
& =-e^{\sqrt{\frac{2}{n+1}} \tilde{\rho}}(n+1)^{\frac{1}{n+1}}\left(e^{\psi_{T}-\psi_{T}(\tau)+a}+b|\tau|^{n+1}\right)^{\frac{1}{n+1}} \\
& =-(n+1)+O\left(|b||\tau|^{n+1}\right),
\end{aligned}$$
uniformly for $\tilde{\rho} \in I$, where we have applied the fact that
$$\psi_{T}-\psi_{T}(\tau)=\psi_{\text {cusp }}-\psi_{\text {cusp }}(\tau)+O\left(|b||\tau|^{n+1}\right)=-(n+1) \log |t / \tau|+O\left(|b \| \tau|^{n+1}\right) .$$
A similar computation shows that
$$t^{2} \psi_{T}^{\prime \prime}=t^{2} e^{\psi_{T}+a}\left(\psi_{T}^{\prime}\right)^{1-n}=e^{\psi_{T}-\psi_{\text {cusp }}+n \log (n+1)}\left(-t \psi_{T}^{\prime}\right)^{1-n}=n+1+O\left(|b||\tau|^{n+1}\right)$$
as $b \rightarrow 0^{-}$. By differentiating
$$t^{2} \psi_{T}^{\prime \prime}=(n+1)^{n} e^{\psi_{T}-\psi_{\text {cusp }}}\left(-t \psi_{T}^{\prime}\right)^{1-n}$$
multiple times and multiplying by $t$ each time, we derive the following lemma.
Lemma 2.23. For $k \geqslant 1$,
$$t^{k} \psi_{T}^{(k)}=(-1)^{k}(n+1)(k-1)!+O_{k}\left(|b||\tau|^{n+1}\right)$$
on $\{\tilde{\rho} \in I\}$ as $b \rightarrow 0^{-}$. Here $(-1)^{k}(n+1)(k-1)!=t^{k} \psi_{\text {cusp }}^{(k)}$.
Introduce a local bundle chart $\left(z_{1}, \ldots, z_{n}\right)$ on the total space of $L$ such that $z_{n}=0$ cuts out the zero section. Write the Hermitian metric as $h=e^{-\varphi}\left|z_{n}\right|^{2}$, where $\varphi$ depends only on $z_{1}, \ldots, z_{n-1}$. Then for any radial potential $\psi=\psi(t), t=\log h$, the associated (1,1)-form can be written as
$$\omega=i \partial \bar{\partial} \psi=-\psi^{\prime} i \partial \bar{\partial} \varphi+\psi^{\prime \prime} i\left(\partial \varphi-\partial \log z_{n}\right) \wedge\left(\bar{\partial} \varphi-\bar{\partial} \log \bar{z}_{n}\right) .$$

We now assume that the Calabi-Yau $\left(E, \omega_{E}\right), \omega_{E}=-i \partial \bar{\partial} \varphi$, is flat and $z_{1}, \ldots, z_{n-1}$ are the standard linear coordinates on the universal cover $\mathbb{C}^{n-1} \rightarrow E$. We also write $z_{\alpha}=x_{\alpha}+i y_{\alpha}$ for $1 \leqslant \alpha \leqslant n-1$, $\theta=\arg z_{n}$ and $x=-1 / t$. Then, on the universal cover of $\left\{2 \tau \leqslant t \leqslant \frac{1}{2} \tau\right\}$, we define a new chart via
$$\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{x}, \check{\theta}\right):=\left(|\tau|^{-\frac{1}{2}} x_{\alpha},|\tau|^{-\frac{1}{2}} y_{\alpha},|\tau| x,|\tau|^{-1} \theta\right)$$
which takes the value $p=(0, \ldots, 0,1,0)$ at a point $q$ such that $t(q)=\tau$. Under this chart, the metric $\omega_{\text {cusp }}$ is equivalent to $\delta_{i j}$ and in addition, for all $k, \alpha$,
$$\psi_{\text {cusp }}^{\prime} i \partial \bar{\partial} \varphi, \quad \psi_{\text {cusp }}^{\prime \prime} i\left(\partial \varphi-\partial \log z_{n}\right) \wedge\left(\bar{\partial} \varphi-\bar{\partial} \log \bar{z}_{n}\right)$$
have bounded $C^{k}$ norms on a fixed size ball centered at $p$, with bounds that are independent of $\tau$. Also, $\psi_{T}, \psi_{\text {cusp }}$ are independent of $x_{\alpha}, y_{\alpha}, \theta$. Applying this chart, Lemma 2.23 implies that, for $t \in[2 \tau, \tau]$,
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\psi_{T}-\psi_{\text {cusp }}\right)\right|_{\omega_{\text {cusp }}}=O_{k}\left(|b||\tau|^{n+1}\right) .$$
Meanwhile, to prove higher order derivative estimates of $\omega_{T}$ under the coordinates (2.109), we only have to check that
$$\frac{\psi_{T}^{\prime}}{\psi_{\text {cusp }}^{\prime}}, \frac{\psi_{T}^{\prime \prime}}{\psi_{\text {cusp }}^{\prime \prime}}$$
have uniformly bounded $C^{k}$ norm with respect to (2.109). For example,
$$\frac{\partial}{\partial \breve{x}} \frac{\psi_{T}^{\prime \prime}}{\psi_{c u s p}^{\prime \prime}}=-|\tau|^{-1} \frac{\partial t}{\partial x} \cdot \frac{\psi_{T}^{\prime \prime \prime} \psi_{c u s p}^{\prime \prime}-\psi_{T}^{\prime \prime} \psi_{c u s p}^{\prime \prime \prime}}{\left(\psi_{c u s p}^{\prime \prime}\right)^{2}},$$
where
$$t^{5}\left(\psi_{T}^{\prime \prime \prime} \psi_{\text {cusp }}^{\prime \prime}-\psi_{T}^{\prime \prime} \psi_{\text {cusp }}^{\prime \prime \prime}\right)=\left(t^{3} \psi_{T}^{\prime \prime \prime}-t^{3} \psi_{\text {cusp }}^{\prime \prime \prime}\right) t^{2} \psi_{\text {cusp }}^{\prime \prime}-\left(t^{2} \psi_{T}^{\prime \prime}-t^{2} \psi_{\text {cusp }}^{\prime \prime}\right) t^{3} \psi_{\text {cusp }}^{\prime \prime \prime},$$
which is $O\left(|b||\tau|^{n+1}\right)$ by Lemma 2.23. This shows that
$$\frac{\partial}{\partial \breve{x}} \frac{\psi_{T}^{\prime \prime}}{\psi_{\text {cusp }}^{\prime \prime}}=O\left(|b \| \tau|^{n+1}\right) .$$
We can estimate the $C^{k}$ norm of (2.112) with $k \geqslant 1$ by induction, using the formula
$$\left(\frac{f}{g}\right)^{(k)}=\frac{1}{g}\left(f^{(k)}-k!\sum_{j=1}^{k} \frac{g^{(k+1-j)}}{(k+1-j)!} \frac{\left(\frac{f}{g}\right)^{(j-1)}}{(j-1)!}\right)$$
with
$$f=\psi_{T}^{\prime}-\psi_{\text {cusp }}^{\prime}, \quad g=\psi_{\text {cusp }}^{\prime}$$
or with
$$f=\psi_{T}^{\prime \prime}-\psi_{\text {cusp }}^{\prime \prime}, \quad g=\psi_{\text {cusp }}^{\prime \prime} .$$
By Lemma 2.23 and (2.44), we have for any $k \geqslant 1$ that $f^{(k)}=O\left(|b||\tau|^{n+1}\right)$.
Thus, in conclusion, we have proved the following lemma.
Lemma 2.24. Let $\psi_{T}$ be the solution of (2.42) satisfying (2.88) and assume that (2.81) is in force. Then for any $k \in \mathbb{N}$ and for all $t \in[2 \tau, \tau]$,
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\omega_{T}-\omega_{\text {cusp }}\right)\right|_{\omega_{\text {cusp }}}=O\left(|b||\tau|^{n+1}\right) .$$
2.4.2. Estimates on the middle neck.

Proposition 2.25. Assume that $b \in\left(-\frac{1}{2}, 0\right)$. Let $\psi_{T}$ be the solution of (2.42) satisfying (2.88). Then:
\begin{itemize}
\item[(1)] For $t \in[T, \tau]$,
$$0 \leqslant \psi_{T}(t)-\psi_{\text {cusp }}(t)<C,$$
where $C$ does not depend on $b$.
\item[(2)] $\psi_{T}(t)-\psi_{\text {cusp }}(t)$ is a decreasing function on $[T, \tau]$.
\item[(3)] $\psi_{T}^{\prime}(t)<\psi_{\text {cusp }}^{\prime}(t)$ for $t \in[T, \tau]$.
\end{itemize}

Proof. By (2.82), (2.92), when $t=\tau$ or $T, 0 \leqslant \psi_{T}-\psi_{\text {cusp }}<C$, where $C$ is independent of $b$. Now assume that $\psi_{T}-\psi_{\text {cusp }}$ has a positive local maximum at $p \in(T, \tau)$. Then
$$\begin{aligned}
& \psi_{T}(p)>\psi_{\text {cusp }}(p), \\
& 0<\psi_{T}^{\prime}(p)=\psi_{\text {cusp }}^{\prime}(p), \\
& 0<\psi_{T}^{\prime \prime}(p) \leqslant \psi_{\text {cusp }}^{\prime \prime}(p),
\end{aligned}$$
which contradicts the fact that $\psi_{T}$ and $\psi_{\text {cusp }}$ both satisfy equation (2.42). Similarly, $\psi_{T}-\psi_{\text {cusp }}$ does not have a negative local minimum in $(T, \log |b|)$. Part (1) of the lemma is proved.

Notice that $\psi_{T}-\psi_{\text {cusp }}=0$ at $\tau$. If $\psi_{T}-\psi_{\text {cusp }}$ is not monotone, then it has either a positive local maximum or a negative local minimum in $(T, \tau)$, which contradicts the above discussion. At $\tau$, $\psi_{T}^{\prime}<\psi_{\text {cusp }}^{\prime}$ by (2.79). So $\psi_{T}-\psi_{\text {cusp }}$ is a decreasing function.

For part (3), we assume that it is not true and set
$$t_{0}:=\sup \left\{t \in[T, \tau]: \psi_{T}^{\prime}(t) \geqslant \psi_{\text {cusp }}^{\prime}(t)\right\} .$$
Then $t_{0}<\tau$. At $t_{0}$, we have
$$\begin{aligned}
& 0<\psi_{T}^{\prime}\left(t_{0}\right)=\psi_{\text {cusp }}^{\prime}\left(t_{0}\right), \\
& 0<\psi_{T}^{\prime \prime}\left(t_{0}\right) \leqslant \psi_{\text {cusp }}^{\prime \prime}\left(t_{0}\right),
\end{aligned}$$
By part (2), $\psi_{T}\left(t_{0}\right)>\psi_{\text {cusp }}\left(t_{0}\right)$. This contradicts equation (2.42). \(\square\)

Proposition 2.26. Fix $\delta \in(0,1)$. Then for all $\eta \in(0, \delta]$ we have that
$$\psi_{T}(\eta T)=\psi_{\text {cusp }}(\eta T)+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O_{\delta}\left(\eta^{n+1}\right) .$$
In addition,
$$\begin{aligned}
& \psi_{T}^{\prime}(\eta T)=\psi_{\text {cusp }}^{\prime}(\eta T) e^{O_{\delta}\left(\eta^{n+1}\right)}\left(1+O\left(|b|^{\frac{1}{n+1}} \tau\right)\right), \\
& \psi_{T}^{\prime \prime}(\eta T)=\psi_{\text {cusp }}^{\prime \prime}(\eta T) e^{O_{\delta}\left(\eta^{n+1}\right)}\left(1+O\left(|b|^{\frac{1}{n+1}} \tau\right)\right) .
\end{aligned}$$
Proof. Taking $t_{0}=\eta T$ and $t=T$ and substituting $\xi=s+\psi_{T}(T)$ in (2.80), we get
$$\int_{0}^{\psi_{T}(\eta T)-\psi_{T}(T)}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s=(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}(\eta T-T)$$
By part (2) of Proposition 2.25, as $\eta \rightarrow 0^{+}$,
$$\psi_{T}(\eta T)-\psi_{T}(T)>\psi_{\text {cusp }}(\eta T)-\psi_{\text {cusp }}(T)-C \rightarrow \infty .$$
Taking $\eta \rightarrow 0^{+}$in (2.130),
$$\int_{0}^{\infty}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s=(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}|T|$$

Subtracting it from (2.130),
$$\begin{aligned}
\int_{\psi_{T}(\eta T)-\psi_{T}(T)}^{\infty}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s & =(n+1)^{\frac{1}{n+1}} \eta|b|^{\frac{1}{n+1}}|T| \\
& =\eta\left(\int_{0}^{\infty}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s+O\left(|b|^{\frac{1}{n+1}} \tau\right)\right)
\end{aligned}$$
where we applied (2.89) for the last step. When $s>0$ is bounded away from 0,
$$\left(e^{s}-1\right)^{-\frac{1}{n+1}}=e^{-\frac{s}{n+1}}\left(1-e^{-s}\right)^{-\frac{1}{n+1}}=e^{-\frac{s}{n+1}}+O\left(e^{-\frac{(n+2) s}{n+1}}\right) .$$
Thus,
$$\begin{aligned}
\psi_{T}(\eta T)-\psi_{T}(T) & =(n+1) \log (n+1)-(n+1) \log \eta \\
& -(n+1) \log \left(\int_{0}^{\infty}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s\right)+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(\eta^{n+1}\right)
\end{aligned}$$
Comparing this to
$$\begin{aligned}
\psi_{\text {cusp }}(\eta T)-\psi_{T}(T) & =-(n+1) \log (-\eta T)-\log |b|+n \log (n+1) \\
& =-(n+1) \log \eta+(n+1) \log (n+1) \\
& -(n+1) \log \left(\int_{0}^{\infty}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s\right)+O\left(|b|^{\frac{1}{n+1}} \tau\right),
\end{aligned}$$
we obtain that
$$\psi_{T}(\eta T)-\psi_{\text {cusp }}(\eta T)=O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(\eta^{n+1}\right) .$$
The rest of the proposition follows by analyzing (2.79) and (2.42). \(\square\)

Definition 2.27 (Perturbation of differential operators). Given a function $\varepsilon(\mathbf{x})>0$ on a local chart x, we say that $f(\mathbf{x})=O(\varepsilon(\mathbf{x}))$ if $|f(\mathbf{x})| \leqslant C \varepsilon(\mathbf{x})$ for some $C>0$ independent of x and of $b, T$. Let
$$\begin{aligned}
L & =\sum_{i, j=1}^{m} a_{i j}(\mathbf{x}) \partial_{i j}^{2}+\sum_{i=1}^{m} b_{i}(\mathbf{x}) \partial_{i}, \\
\tilde{L} & =\sum_{i, j=1}^{m} \tilde{a}_{i j}(\mathbf{x}) \partial_{i j}^{2}+\sum_{i=1}^{m} \tilde{b}_{i}(\mathbf{x}) \partial_{i},
\end{aligned}$$
be two differential operators. We say that $\tilde{L}=L+O(\varepsilon(\mathbf{x}))$ if
$$\tilde{a}_{i j}=(1+O(\varepsilon(\mathbf{x}))) a_{i j}, \quad \tilde{b}_{i}=(1+O(\varepsilon(\mathbf{x}))) b_{i},$$
for all $1 \leqslant i, j \leqslant m$. Similarly, we say that $\tilde{L}=L \cdot e^{O(\varepsilon(\mathbf{x}))}$ if
$$\tilde{a}_{i j}=e^{O(\varepsilon(\mathbf{x}))} a_{i j}, \quad \tilde{b}_{i}=e^{O(\varepsilon(\mathbf{x}))} b_{i} .$$

Lemma 2.28. Recall the local holomorphic chart $\left(z_{1}, \ldots, z_{n}\right)$ introduced after Lemma 2.23. Assume that in this chart a Kähler metric $g$ is given by
$$g_{i \bar{j}}=-F \varphi_{i \bar{j}}+G\left(\varphi_{i}-\frac{\delta_{i n}}{z_{n}}\right)\left(\varphi_{\bar{j}}-\frac{\delta_{j n}}{\bar{z}_{n}}\right),$$
where $F, G$ are positive functions and $\varphi$ is a function of $z_{1}, \ldots, z_{n-1}$. Then its inverse $g^{\bar{j} k}$ is given by
$$g^{\bar{\beta} \alpha}=-\frac{\varphi^{\bar{\beta} \alpha}}{F}(1 \leqslant \alpha, \beta \leqslant n-1), g^{\bar{\alpha} n}=-\frac{\varphi^{\bar{\alpha} \gamma} \varphi_{\gamma} z_{n}}{F}, g^{\bar{n} n}=\frac{\left|z_{n}\right|^{2}\left(F-G \varphi^{\bar{\beta} \alpha} \varphi_{\alpha} \varphi_{\bar{\beta}}\right)}{F G} .$$

The next corollary follows from Proposition 2.26.

Corollary 2.29. Fix $\delta \in(0,1)$ and let $\eta \in(0, \delta]$. Then at $t=\eta T$,
$$\Delta_{\omega_{T}}=\left(L_{h}+O\left(|b|^{\frac{1}{n+1}} \tau\right)\right) \cdot e^{O_{\delta}\left(\eta^{n+1}\right)}$$
where the cuspidal Laplacian $L_{h}$ was introduced in [13, Lemma 2.5]. Using the notation $x=-1 / t$ and $\theta=\arg z_{n}$ from [13], an explicit formula for $L_{h}$ is
$$\begin{array}{r}
L_{h} u=\frac{1}{n+1}\left(x^{2} u_{x x}+(n+1) x u_{x}-(n+1) u-x^{-1} \varphi^{\bar{\beta} \alpha} u_{\alpha \bar{\beta}}+(2 x)^{-1} u_{\theta \theta}\right)+F, \\
F=F\left(x_{\alpha}, y_{\alpha}, x^{-1} u_{\theta \alpha}, x^{-1} u_{\theta \bar{\alpha}}, x^{-1} u_{\theta \theta}\right),
\end{array}$$
with $F$ smooth in $x_{\alpha}, y_{\alpha}$ and linear homogeneous in the other arguments. In addition, for all $k \geqslant 0$,
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\omega_{T}-\omega_{\text {cusp }}\right)\right|_{\omega_{\text {cusp }}}=O_{\delta, k}\left(|b|^{\frac{1}{n+1}}|\tau|+\eta^{n+1}\right) .$$
Proof. (2.144) follows from Proposition 2.26, Lemma 2.28, and the proof of Lemma 2.5 in [13].
To prove (2.146), we first rewrite (2.106) as
$$\psi_{T}^{\prime \prime}=(n+1)^{n} e^{\psi_{T}-\psi_{\text {cusp }}}(-t)^{-n-1}\left(\psi_{T}^{\prime}\right)^{1-n}$$
and differentiate it multiple times to inductively show that
$$\psi_{T}^{(k)}(\eta T)=\psi_{\text {cusp }}^{(k)}(\eta T)\left(1+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(\eta^{n+1}\right)\right) .$$
In fact, cases $k=1,2$ follow directly from Proposition 2.26. For $k \geqslant 3$, when we differentiate (2.147) $k-2$ times using the product rule, every term on the right-hand side is of the form
$$(-t)^{-k}\left(C+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(\eta^{n+1}\right)\right) .$$
By formally writing $1=e^{\psi_{\text {cusp }}-\psi_{\text {cusp }}}$ and differentiating
$$\psi_{\text {cusp }}^{\prime \prime}=(n+1)^{n} e^{\psi_{\text {cusp }}-\psi_{\text {cusp }}}(-t)^{-n-1}\left(\psi_{\text {cusp }}^{\prime}\right)^{1-n}$$
$k-2$ times, we know that the constants $C$ add up to $(n+1)(k-1)!$ as
$$\psi_{c u s p}^{(k)}(t)=(n+1)(k-1)!(-t)^{-k} .$$
Here we use the fact that the ( $k-2$ )-th derivatives of (2.147) and ( $k-2$ )-th derivatives of (2.150) are in similar forms. With this, we derive (2.148). Near a point $q$ with $t_{*}:=t(q) \in[\delta T, \tau]$, we then consider quasi-coordinates for $\omega_{\text {cusp }}$ as in (2.109):
$$\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{x}, \check{\theta}\right):=\left(\left(-t_{*}\right)^{-\frac{1}{2}} x_{\alpha},\left(-t_{*}\right)^{-\frac{1}{2}} y_{\alpha},-t_{*} x,\left(-t_{*}\right)^{-1} \theta\right) .$$
Similarly as in the proof of Lemma 2.23, we need to show that the $C^{k}$ norm of
$$\frac{\psi_{T}^{\prime}-\psi_{\text {cusp }}^{\prime}}{\psi_{\text {cusp }}^{\prime}}, \frac{\psi_{T}^{\prime \prime}-\psi_{\text {cusp }}^{\prime \prime}}{\psi_{\text {cusp }}^{\prime \prime}}$$
with respect to (2.152) on $\left\{2 t_{*}<t<\frac{1}{2} t_{*}\right\}$ is bounded by $C_{k}\left(|b|^{\frac{1}{n+1}}|\tau|+\eta^{n+1}\right)$. For $k=0$, this follows directly from (2.148). For $k \geqslant 1$, we prove it by induction by applying (2.116)-(2.118). \(\square\)

Proposition 2.30. Let $\delta \in(0,1)$ be a small dimensional constant. Define the coordinate $s:=1-t / T$ and restrict it to $s \in\left[2|T|^{\alpha-1}, \delta\right]$ for some $\alpha \in(0,1)$. Then $\Delta_{\omega_{T}}$ is of the form
$$\Delta_{\omega_{T}}=L+O\left(|b|^{-\frac{1}{n+1}} s^{-\frac{1}{n}}\right) \cdot \partial_{\theta \theta}^{2}+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(s^{\frac{n+1}{n}}\right) .$$

Here the $O$ notation is understood in the sense of Definition 2.27 with respect to the local chart $s, \theta, z_{\alpha}$ and the model operator $L$ takes the following form:
$$\begin{aligned}
L u & =\left(\frac{n+1}{n}\right)^{\frac{1}{n}} c(n)^{-\frac{n+1}{n}}\left(n s^{\frac{n-1}{n}} u_{s s}+(n-1) s^{-\frac{1}{n}} u_{s}\right)+|b|^{-\frac{1}{n+1}} s^{-\frac{1}{n}} \mathcal{T} u \\
& +C|b|^{-\frac{2}{n+1}} s^{\frac{n-1}{n}} u_{\theta \theta}+s^{-\frac{1}{n}} \mathcal{H} u,
\end{aligned}$$
where $C>0$ is a constant, $\mathcal{T}$ is an elliptic operator on $E$ and $\mathcal{H}$ is linear homogeneous in
$$u_{s \alpha}, u_{s \bar{\beta}}, u_{s \theta},|b|^{-\frac{1}{n+1}} u_{\alpha \theta},|b|^{-\frac{1}{n+1}} u_{\bar{\beta} \theta}$$
with coefficients that are smooth in $x_{\alpha}, y_{\alpha}$ and independent of $b, T$.
The term $O\left(s^{\frac{n+1}{n}}\right)$ in (2.154) stands for a comparison of differential operators as in (2.140), so for applications it is important to know that this term is > -1. This is ensured by our assumption $s \leqslant \delta$. Similarly, given the condition $s \geqslant 2|T|^{\alpha-1}$, we can observe that the term with $\partial_{\theta \theta}^{2}$ in (2.154) is
$$O\left(|b|^{-\frac{1}{n+1}} s^{-\frac{1}{n}}\right) \cdot \partial_{\theta \theta}^{2}=O\left(|b|^{\frac{\alpha}{n+1}}\right) \cdot|b|^{-\frac{2}{n+1}} s^{\frac{n-1}{n}} u_{\theta \theta} .$$
Hence, this term represents a higher-order contribution compared to the operator $L$.
Proof of Proposition 2.30. By (2.130) and (2.89),
$$\begin{aligned}
\int_{0}^{\psi_{T}(\eta T)-\psi_{T}(T)}\left(e^{\xi}-1\right)^{-\frac{1}{n+1}} d \xi & =(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}(1-\eta)|T| \\
& =\left(c(n)+O\left(|b|^{\frac{1}{n+1}} \tau\right)\right)(1-\eta),
\end{aligned}$$
where $1-\eta=s$ and the $O\left(|b|^{\frac{1}{n+1}} \tau\right)$ term is independent of $s$. When $\xi>0$ is bounded,
$$\left(e^{\xi}-1\right)^{-\frac{1}{n+1}}=\xi^{-\frac{1}{n+1}}(1+O(\xi))=\xi^{-\frac{1}{n+1}}+O\left(\xi^{\frac{n}{n+1}}\right) .$$
Thus, we have that
$$\int_{0}^{\psi_{T}(\eta T)-\psi_{T}(T)}\left(e^{\xi}-1\right)^{-\frac{1}{n+1}} d \xi=\frac{n+1}{n}\left(\psi_{T}(\eta T)-\psi_{T}(T)\right)^{\frac{n}{n+1}}\left(1+O\left(\psi_{T}(\eta T)-\psi_{T}(T)\right)\right) .$$
By (2.158),
$$\psi_{T}(\eta T)-\psi_{T}(T)=\left(\frac{n}{n+1}\right)^{\frac{n+1}{n}}\left(c(n)+O\left(|b|^{\frac{1}{n+1}} \tau\right)\right)^{\frac{n+1}{n}} s^{\frac{n+1}{n}}\left(1+O\left(\psi_{T}(\eta T)-\psi_{T}(T)\right)\right),$$
which further implies that
$$\psi_{T}(\eta T)-\psi_{T}(T)=\left(\frac{n}{n+1}\right)^{\frac{n+1}{n}}\left(c(n)+O\left(|b|^{\frac{1}{n+1}} \tau\right)\right)^{\frac{n+1}{n}} s^{\frac{n+1}{n}}\left(1+O\left(s^{\frac{n+1}{n}}\right)\right) .$$
The metric $\omega_{T}$ is given by
$$\omega_{T}=-\psi_{T}^{\prime} i \partial \bar{\partial} \varphi+\psi_{T}^{\prime \prime} i\left(-\partial \varphi+\partial \log z_{n}\right) \wedge\left(-\bar{\partial} \varphi+\bar{\partial} \log z_{n}\right) .$$

Thanks to (2.162), we can evaluate the coefficients as follows:
$$\begin{aligned}
\psi_{T}^{\prime}(\eta T) & =(n+1)^{\frac{1}{n+1}}\left(e^{\psi_{T}(\eta T)+a}+b\right)^{\frac{1}{n+1}} \\
& =(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}\left(e^{\psi_{T}(\eta T)-\psi_{T}(T)}-1\right)^{\frac{1}{n+1}} \\
& =(n+1)^{\frac{1}{n+1}}\left(\frac{n}{n+1}\right)^{\frac{1}{n}}|b|^{\frac{1}{n+1}} s^{\frac{1}{n}}\left(c(n)^{\frac{1}{n}}+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(s^{\frac{n+1}{n}}\right)\right), \\
\psi_{T}^{\prime \prime}(\eta T) & =\frac{e^{\psi_{T}(\eta T)+a}}{\left(\psi_{T}^{\prime}(\eta T)\right)^{n-1}}=\frac{|b| e^{\psi_{T}(\eta T)-\psi_{T}(T)}}{\left(\psi_{T}^{\prime}(\eta T)\right)^{n-1}} \\
& =(n+1)^{\frac{1-n}{n+1}}\left(\frac{n}{n+1}\right)^{\frac{1-n}{n}}|b|^{\frac{2}{n+1}} s^{\frac{1-n}{n}}\left(c(n)^{\frac{1-n}{n}}+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(s^{\frac{n+1}{n}}\right)\right) .
\end{aligned}$$

Setting $x=-1 / t$, we have $x=(1-s)^{-1}|T|^{-1}$ and
$$\partial_{x}=|T|(1-s)^{2} \partial_{s}, \quad \partial_{x x}^{2}=|T|^{2}(1-s)^{4} \partial_{s}^{2}-2|T|^{2}(1-s)^{3} \partial_{s} .$$
Given this conversion formula, it will be enough to express $\Delta_{\omega_{T}}$ in terms of $\partial_{x}, \partial_{x x}^{2}$. This can be done by a computation similar to the proof of [13, Lemma 2.5]. Set
$$Q:=\varphi^{\bar{\beta} \alpha} \varphi_{\alpha} \varphi_{\bar{\beta}},$$
which is uniformly bounded. Applying Lemma 2.28 with $F=\psi^{\prime}(\eta T), G=\psi^{\prime \prime}(\eta T)$, we have that
$$\begin{aligned}
g^{\bar{n} n} \partial_{n} \partial_{\bar{n}} & =\frac{r^{2}(F-G Q)}{F G}\left(\frac{x^{2}}{z_{n}} \partial_{x}-\frac{i}{2 z_{n}} \partial_{\theta}\right)\left(\frac{x^{2}}{\bar{z}_{n}} \partial_{x}+\frac{i}{2 \bar{z}_{n}} \partial_{\theta}\right) \\
& =\left(\frac{1}{G}-\frac{Q}{F}\right)\left(x^{4} \partial_{x x}^{2}+2 x^{3} \partial_{x}+\frac{1}{4} \partial_{\theta \theta}^{2}\right) \\
& =(n+1)^{\frac{n-1}{n+1}}\left(\frac{n}{n+1}\right)^{\frac{n-1}{n}} c(n)^{\frac{n-1}{n}}|b|^{-\frac{2}{n+1}} s^{\frac{n-1}{n}}\left(x^{4} \partial_{x x}^{2}+2 x^{3} \partial_{x}+\frac{1}{4} \partial_{\theta \theta}^{2}\right) \\
& -\frac{Q}{F}\left(x^{4} \partial_{x x}^{2}+2 x^{3} \partial_{x}\right)+O\left(|b|^{-\frac{1}{n+1}} s^{-\frac{1}{n}}\right) \partial_{\theta \theta}^{2}+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(s^{\frac{n+1}{n}}\right) \\
& =(n+1)\left(\frac{n}{n+1}\right)^{\frac{n-1}{n}} c(n)^{-\frac{n+1}{n}} s^{\frac{n-1}{n}} \partial_{s s}^{2}+C|b|^{-\frac{2}{n+1}} s^{\frac{n-1}{n}} \partial_{\theta \theta}^{2} \\
& -\frac{Q}{F}\left(x^{4} \partial_{x x}^{2}+2 x^{3} \partial_{x}\right)+O\left(|b|^{-\frac{1}{n+1}} s^{-\frac{1}{n}}\right) \partial_{\theta \theta}^{2}+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(s^{\frac{n+1}{n}}\right), \\
g^{\bar{\alpha} n} \partial_{n} \partial_{\bar{\alpha}} & =-\frac{\varphi^{\bar{\alpha} \gamma} \varphi_{\gamma} z_{n}}{F}\left(\frac{x^{2}}{z_{n}} \partial_{x}-\frac{i}{2 z_{n}} \partial_{\theta}\right)\left(\partial_{\bar{\alpha}}-x^{2} \varphi_{\bar{\alpha}} \partial_{x}\right) \\
& =-\frac{x^{2}}{F} \varphi^{\bar{\alpha} \gamma} \varphi_{\gamma} \partial_{x \bar{\alpha}}^{2}+\frac{Q}{F}\left(x^{4} \partial_{x x}^{2}+2 x^{3} \partial_{x}\right)-\frac{i x^{2} Q \partial_{x \theta}^{2}}{2 F}+\frac{i \varphi^{\bar{\alpha} \gamma} \varphi_{\gamma} \partial_{\bar{\alpha} \theta}^{2}}{F} \\
& =s^{-\frac{1}{n}} H_{1}\left(x_{\alpha}, y_{\alpha}, \partial_{s \bar{\alpha}}^{2},|b|^{\frac{1}{n+1}} \partial_{s s}^{2},|b|^{\frac{1}{n+1}} \partial_{s}, \partial_{s \theta}^{2},|b|^{-\frac{1}{n+1}} \partial_{\bar{\alpha} \theta}^{2}\right)+O\left(b^{n+1} \tau\right)+O\left(s^{\frac{n+1}{n}}\right), \\
g^{\bar{\beta} \alpha} \partial_{\alpha} \partial_{\bar{\beta}} & =-\frac{\varphi^{\bar{\beta} \alpha}}{F}\left(\partial_{z_{\alpha}}-x^{2} \varphi_{\alpha} \partial_{x}\right)\left(\partial_{\bar{\beta}}^{2}-x^{2} \varphi_{\bar{\beta}} \partial_{x}\right) \\
& =-\frac{\varphi^{\bar{\beta} \alpha}}{F} \partial_{\alpha \bar{\beta}}^{2}+(n-1) \frac{x^{2} \partial_{x}}{F}+\frac{x^{2} \varphi^{\bar{\beta} \alpha}\left(\varphi_{\alpha} \partial_{x \bar{\beta}}^{2}+\varphi_{\bar{\beta}} \partial_{x \alpha}^{2}\right)}{F}-\frac{Q\left(x^{4} \partial_{x x}^{2}+2 x^{3} \partial_{x}\right)}{F} \\
& =|b|^{-\frac{1}{n+1}} s^{-\frac{1}{n}} T+(n-1)\left(\frac{n}{n+1}\right)^{-\frac{1}{n}} c(n)^{-\frac{n+1}{n}} s^{-\frac{1}{n}} \partial_{s} \\
& +s^{-\frac{1}{n}} H_{2}\left(x_{\alpha}, y_{\alpha}, \partial_{s \alpha}^{2}, \partial_{s \bar{\beta}}^{2},|b|^{\frac{1}{n+1}} \partial_{s s}^{2},|b|^{\frac{1}{n+1}} \partial_{s}\right)+O\left(b^{n+1} \tau\right)+O\left(s^{\frac{n+1}{n}}\right),
\end{aligned}$$
where $H_{1}, H_{2}$ are smooth in $x_{\alpha}, y_{\alpha}$ and linear homogeneous with respect to their differential operator arguments. As $\Delta_{\omega_{T}}$ is a real operator, all terms with an $i$ must cancel out. In addition, the terms
$$\frac{Q}{F}\left(x^{4} \partial_{x x}^{2}+2 x^{3} \partial_{x}\right)$$
in (2.168)-(2.170) cancel out. So the terms $|b|^{\frac{1}{n+1}} \partial_{s s}^{2},|b|^{\frac{1}{n+1}} \partial_{s}$ in $H_{1}, H_{2}$ cancel out as well. \(\square\)

Let us also note the following formulas for later use. By repeatedly differentiating (2.164)-(2.165), we may prove inductively that, when $k>2$, there are some constants $C_{j, l}$ such that
$$\begin{aligned}
\psi_{T}^{(k)}(\eta T) & =\sum_{j=-(k-2)}^{n(k-2)} \sum_{l=1}^{k-1} \frac{C_{j, l} e^{l\left(\psi_{T}(\eta T)+a\right)}}{\left(\psi_{T}^{\prime}(\eta T)\right)^{n-1+j}} \\
& =\sum_{j=-(k-2)}^{n(k-2)} \sum_{l=1}^{k-1} \frac{C_{j, l}|b|^{l} e^{l\left(\psi_{T}(\eta T)-\psi_{T}(T)\right)}}{\left(\psi_{T}^{\prime}(\eta T)\right)^{n-1+j}} \\
& =\sum_{j=-(k-2)}^{n(k-2)} \sum_{l=1}^{k-1} C_{n, j, l}|b|^{l-\frac{n-1+j}{n+1}} s^{\frac{1-n-j}{n}}\left(c(n)^{\frac{1-n}{n}}+O\left(|b|^{\frac{1}{n+1}} \tau\right)+O\left(s^{\frac{n+1}{n}}\right)\right) .
\end{aligned}$$

The following lemma about the shape of the volume form of $\omega_{T}$ is also an easy consequence of the computations in this section.

Lemma 2.31. Write $s=1-\frac{t}{T}$ as before. Then for every $\eta \in(0,1)$ we have that
$$\left.\omega_{T}^{n}\right|_{t=\eta T}=|T|^{-n} \mu_{T}(1-\eta) d s \wedge d \theta \wedge d \operatorname{Vol}_{E},$$
where the radial volume density $\mu_{T}:(0,1) \rightarrow \mathbb{R}^{+}$satisfies the following properties:
\begin{itemize}
\item[(1)] There are constants $e(n), e^{\prime}(n)>0$ with $e(n) \leqslant \mu_{T}(1-\eta) \leqslant e^{\prime}(n) \eta^{-(n+1)}$ for all $\eta, T$.
\item[(2)] $\mu_{\infty}:=\lim _{T \rightarrow-\infty} \mu_{T}$ exists pointwise and is smooth.
\item[(3)] $\mu_{\infty}(s) \rightarrow$ const $>0$ as $s \rightarrow 0^{+}$and $\eta^{n+1} \mu_{\infty}(1-\eta) \rightarrow$ const $>0$ as $\eta \rightarrow 0^{+}$.
\end{itemize}

Proof. From the Kähler-Einstein equation, it is straightforward to see that
$$\left.\omega_{T}^{n}\right|_{t=\eta T}=e^{\prime \prime}(n)|T|^{-n} e^{\psi_{T}(\eta T)-\psi_{T}(T)} d s \wedge d \theta \wedge d \operatorname{Vol}_{E}$$
for some constant $e^{\prime \prime}(n)>0$. For item (1), we use (2.120) to estimate
$$\begin{aligned}
0 \leqslant \psi_{T}(\eta T)-\psi_{T}(T) & \leqslant \psi_{\text {cusp }}(\eta T)+C-\psi_{T}(T) \\
& \leqslant-(n+1) \log \eta-(n+1) \log (-T)+C-\psi_{T}(T) \\
& \leqslant-(n+1) \log \eta+C .
\end{aligned}$$
For items (2) and (3), we use the more precise formula (2.127), which is valid for all $\eta \in(0,1)$. This tells us that $\psi_{T}(\eta T)-\psi_{T}(T)$ has a pointwise limit as $T \rightarrow-\infty$, which is a smooth function of $\eta$ and which moreover differs from $-(n+1) \log \eta+C$ by $O\left(\eta^{n+1}\right)$ as $\eta \rightarrow 0^{+}$. This also establishes the limit as $\eta \rightarrow 0^{+}$in item (3). For the limit as $s \rightarrow 0^{+}$in item (3), we can instead look at (2.162). \(\square\)
2.4.3. Estimates asymptotically close to the Tian-Yau end (orange region). Recall from Remark 2.22 that the orange gluing region takes the form $t \in\left[T+T_{0}, T+2 T_{0}\right]$ for some positive $T_{0}$ depending on $\sigma$ such that $T_{0} \rightarrow+\infty$ but $T_{0} / T \rightarrow 0^{-}$as $b \rightarrow 0^{-}$. From now on we fix an $\alpha \in(0,1)$ and set
$$T_{0}:=|T|^{\alpha} .$$

In this section we will prove decay estimates for the difference of the Tian-Yau metric and the neck metric $\omega_{T}$ in the orange region. We slightly abuse notation by writing
$$\psi_{\mathcal{C}}(t)=\frac{n}{n+1}(t-T)^{\frac{n+1}{n}}$$
for the Calabi model potential shifted by $T$. We also set
$$\mathfrak{c}:=n^{\frac{1}{n}} .$$
We wish to glue $\omega_{T}$ with $\mathfrak{c}|b|^{\frac{1}{n}} \omega_{\mathcal{C}}$. To this end, we introduce the error term
$$E(t):=\psi_{T}(t)-\psi_{T}(T)-\mathfrak{c}|b|^{\frac{1}{n}} \psi_{\mathcal{C}} .$$
Notice that
$$\int_{\psi_{T}(T)}^{\psi_{T}(t)}\left(e^{\xi+a}+b\right)^{-\frac{1}{n+1}} d \xi=(n+1)^{\frac{1}{n+1}}(t-T) .$$
Taking $s=\xi-\psi_{T}(T)$, we have that for $t-T \in\left[T_{0}, 2 T_{0}\right]$,
$$\int_{0}^{\psi_{T}(t)-\psi_{T}(T)}\left(e^{s}-1\right)^{-\frac{1}{n+1}} d s=(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}(t-T)=O\left(T_{0}|T|^{-1}\right)$$
Then $\psi_{T}(t)-\psi_{T}(T)=o(1)$ as $T \rightarrow-\infty$. When $s$ is small,
$$\left(e^{s}-1\right)^{-\frac{1}{n+1}}=s^{-\frac{1}{n+1}}+O\left(s^{\frac{n}{n+1}}\right) .$$
We have that
$$\frac{n+1}{n}\left(\psi_{T}(t)-\psi_{T}(T)\right)^{\frac{n}{n+1}}\left(1+O\left(\psi_{T}(t)-\psi_{T}(T)\right)\right)=(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}(t-T) .$$
In sum, for $t-T \in\left[T_{0}, 2 T_{0}\right]$,
$$\psi_{T}(t)-\psi_{T}(T)=\mathfrak{c}|b|^{\frac{1}{n}} \psi_{\mathcal{C}}+O\left(|b|^{\frac{2}{n}} T_{0}^{\frac{2(n+1)}{n}}\right),$$
which shows that
$$E(t)=O\left(|b|^{\frac{2}{n}} T_{0}^{\frac{2(n+1)}{n}}\right) .$$
We can actually expand $E(t)$ in terms of powers of $|b|^{\frac{1}{n}} \psi_{\mathcal{C}}$ up to any finite order. For example,
$$E(t)=\frac{\mathfrak{c}^{2}}{4 n+2}|b|^{\frac{2}{n}} \psi_{\mathcal{C}}^{2}+O\left(|b|^{\frac{3}{n}} \psi_{\mathcal{C}}^{3}\right) \text { as }|b|^{\frac{1}{n}} \psi_{\mathcal{C}} \rightarrow 0$$
More precisely, we have the following statement.
Lemma 2.32. $E(t)$ is an analytic function of $|b|^{\frac{1}{n}}(t-T)^{\frac{n+1}{n}}$ at $|b|^{\frac{1}{n}}(t-T)^{\frac{n+1}{n}}=0$.
Proof. Applying the Maclaurin series of $e^{s}$,
$$\left(e^{s}-1\right)^{-\frac{1}{n+1}}=s^{-\frac{1}{n+1}}\left(\sum_{i=0}^{\infty} \frac{s^{i}}{(i+1)!}\right)^{-\frac{1}{n+1}}=s^{-\frac{1}{n+1}} \sum_{i=0}^{\infty} a_{i} s^{i},$$
where $a_{0}=1$ and $C^{i} a_{i} \rightarrow 0$ for some $C>0$. Indeed, $\left(\frac{e^{s}-1}{s}\right)^{-\frac{1}{n+1}}$ is analytic at $s=0$. By (2.181),
$$\sum_{i=0}^{\infty} \tilde{a}_{i}\left(\psi_{T}(t)-\psi_{T}(T)\right)^{i+\frac{n}{n+1}}=(n+1)^{\frac{1}{n+1}}|b|^{\frac{1}{n+1}}(t-T),$$
where again $\tilde{a}_{0}>0$ and $C^{i} \tilde{a}_{i} \rightarrow 0$ for some $C>0$. Taking the $\frac{n+1}{n}$-th power of both sides, we get
$$\left(\psi_{T}(t)-\psi_{T}(T)\right)\left(\sum_{i=0}^{\infty} \tilde{a}_{i}\left(\psi_{T}(t)-\psi_{T}(T)\right)^{i}\right)^{\frac{n+1}{n}}=(n+1)^{\frac{1}{n}}|b|^{\frac{1}{n}}(t-T)^{\frac{n+1}{n}} .$$
The left-hand side is obviously analytic in $\psi_{T}(t)-\psi_{T}(T)$ around $\psi_{T}(t)-\psi_{T}(T)=0$. Then the lemma follows from the Lagrange inversion theorem. \(\square\)

Lastly, we estimate the derivatives of $i \partial \bar{\partial} E$ under the scaled Calabi metric $|b|^{\frac{1}{n}} \omega_{\mathcal{C}}$. For this we need one more lemma establishing quasi-coordinates for this metric. Following our work after Lemma 2.23, we define real coordinates on the universal cover of the annulus $\left\{y:=t-T \in\left[T_{0}, 2 T_{0}\right]\right\}$ via
$$\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{y}^{\prime}, \check{\theta}\right):=\left(T_{0}^{\frac{1}{2 n}} x_{\alpha}, T_{0}^{\frac{1}{2 n}} y_{\alpha}, T_{0}^{\frac{1-n}{2 n}} y, T_{0}^{\frac{1-n}{2 n}} \theta\right) .$$
We also introduce the corresponding holomorphic coordinates, with $w=\log z_{n}$ :
$$\left(\check{z}_{\alpha}, \check{w}\right):=\left(T_{0}^{\frac{1}{2 n}} z_{\alpha}, T_{0}^{\frac{1-n}{2 n}} w\right) .$$
Lemma 2.33. The un-scaled Calabi metric $\omega_{\mathcal{C}}$ is uniformly equivalent to $\left(\delta_{j k}\right)$ under (2.190)-(2.191). For all $k \geqslant 1$ its entries under (2.190)-(2.191) satisfy a uniform $C^{k}$ bound independent of $T, T_{0}$.

Proof. Because $w=\log z_{n}$, we locally have that
$$t=\log h=-\varphi+w+\bar{w} .$$
This implies that
$$\begin{aligned}
\omega_{\mathcal{C}}=\frac{n}{n+1} i \partial \bar{\partial}(t-T)^{\frac{n+1}{n}} & =\frac{1}{n}(t-T)^{\frac{1-n}{n}} i \partial t \wedge \bar{\partial} t+(t-T)^{\frac{1}{n}} i \partial \bar{\partial} t \\
& =\frac{1}{n}(t-T)^{\frac{1-n}{n}} i \partial(-\varphi+w) \wedge \bar{\partial}(-\varphi+\bar{w})-(t-T)^{\frac{1}{n}} i \partial \bar{\partial} \varphi,
\end{aligned}$$
where $\varphi$ is a quadratic polynomial in $z_{\alpha}, \bar{z}_{\alpha}$ for $\alpha=1, \ldots, n-1$. Under the coordinates $\left(\check{z}_{\alpha}, \check{w}\right)$ given in (2.191), it follows that
$$\begin{aligned}
\omega_{\mathcal{C}} & =\frac{1}{n}\left((t-T) T_{0}^{-1}\right)^{\frac{1-n}{n}} i\left(-T_{0}^{-\frac{1}{2}} \varphi_{z_{\alpha}} d \check{z}_{\alpha}+d \check{w}\right) \wedge\left(-T_{0}^{-\frac{1}{2}} \varphi_{\bar{z}_{\alpha}} d \bar{z}_{\alpha}+d \bar{w}\right) \\
& -\left((t-T) T_{0}^{-1}\right)^{\frac{1}{n}} \varphi_{z_{\alpha} \bar{z}_{\beta}} i d \check{z}_{\alpha} \wedge d \bar{z}_{\beta} .
\end{aligned}$$
This is uniformly equivalent to the Euclidean metric in the chart (2.191) for $y=t-T \in\left[T_{0}, 2 T_{0}\right]$. To check the desired $C^{k}$ bound for $k=1$, note that $\varphi_{z_{\alpha} \bar{z}_{\beta}}$ is a constant, that $\varphi_{\bar{z}_{\alpha}}$ satisfies
$$\frac{\partial \varphi_{\bar{z}_{\alpha}}}{\partial \bar{z}_{\beta}}=T_{0}^{-\frac{1}{2 n}} \frac{\partial \varphi_{\bar{z}_{\alpha}}}{\partial z_{\beta}}=T_{0}^{-\frac{1}{2 n}} \varphi_{z_{\beta} \bar{z}_{\alpha}},$$
and that, by (2.192),
$$\frac{\partial\left((t-T) T_{0}^{-1}\right)}{\partial \breve{w}}=T_{0}^{\frac{n-1}{2 n}} \frac{\partial\left((t-T) T_{0}^{-1}\right)}{\partial w}=T_{0}^{-\frac{n+1}{2 n}} .$$
Thus, the first coordinate derivatives of $\omega_{\mathcal{C}}$ are uniformly decaying. This pattern persists for all $k$. \(\square\)

Proposition 2.34. For $t \in\left[T+T_{0}, T+2 T_{0}\right]$ and $j=1,2$,
$$\left|\nabla_{|b|^{\frac{1}{n}} \omega_{\mathcal{C}}}^{j}(i \partial \bar{\partial} E)\right|_{|b|^{\frac{1}{n}} \omega_{\mathcal{C}}}^{2} \leqslant C|b|^{\frac{2-j}{n}} T_{0}^{\frac{(2-j)(n+1)}{n}} .$$

Proof. Define $y:=t-T$. By deriving the Taylor expansion of $\psi_{T}(t)-\psi_{T}(T)$ with respect to $|b|^{\frac{1}{n}} y^{\frac{n+1}{n}}$ using (2.183), we obtain that for $y \in\left[T_{0}, 2 T_{0}\right]$ and $j \geqslant 0$,
$$\left|\left(y \partial_{t}\right)^{j} E(t)\right| \leqslant C_{j}|b|^{\frac{2}{n}} T_{0}^{\frac{2(n+1)}{n}},$$
where the constants $C_{j}$ are independent of $b$.
Recall the real chart $\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{y}_{,} \check{\theta}\right)$ and the holomorphic chart $\left(\check{z}_{\alpha}, \check{w}\right)$ on the universal cover of the annulus $\left\{y \in\left[T_{0}, 2 T_{0}\right]\right\}$ defined in (2.190)-(2.191) above. By Lemma 2.33, these are quasi-coordinates for $\omega_{\mathcal{C}}$, i.e., the pullback of $\omega_{\mathcal{C}}$ to the universal cover is uniformly smoothly comparable to the Euclidean metric in these coordinates and its $C^{k}$ norms are bounded independently of $T_{0}$.

Now we are ready to estimate the derivatives of $i \partial \bar{\partial} E$. In fact,
$$i \partial \bar{\partial} E=E^{\prime} i \partial \bar{\partial} t+E^{\prime \prime} i \partial t \wedge \bar{\partial} t=-E^{\prime} i \partial \bar{\partial} \varphi+E^{\prime \prime} i(\partial \varphi-\partial w) \wedge(\bar{\partial} \varphi-\bar{\partial} \bar{w}),$$
where
$$T_{0}^{\frac{1}{n}} i \partial \bar{\partial} \varphi, \quad T_{0}^{\frac{1-n}{n}} i(\partial \varphi-\partial w) \wedge(\bar{\partial} \varphi-\bar{\partial} \bar{w})$$
are uniformly smoothly bounded under (2.191). So we need to check the regularity of
$$E^{\prime} / T_{0}^{\frac{1}{n}}, \quad E^{\prime \prime} / T_{0}^{\frac{1-n}{n}} .$$
Because these are radial functions, we just need to check the derivatives of (2.201) with respect to $\check{y}$. Applying (2.198), we obtain that
$$\begin{array}{r}
\left|\frac{\partial\left(E^{\prime} / T_{0}^{\frac{1}{n}}\right)}{\partial \breve{y}}\right|+\left|\frac{\partial\left(E^{\prime \prime} / T_{0}^{\frac{1-n}{n}}\right)}{\partial \breve{y}}\right| \leqslant C|b|^{\frac{2}{n}} T_{0}^{\frac{n+1}{2 n}}, \\
\left|\frac{\partial^{2}\left(E^{\prime} / T_{0}^{\frac{1}{n}}\right)}{\partial \check{y}^{2}}\right|+\left|\frac{\partial^{2}\left(E^{\prime \prime} / T_{0}^{\frac{1-n}{n}}\right)}{\partial \check{y}^{2}}\right| \leqslant C|b|^{\frac{2}{n}} .
\end{array}$$
We conclude that the 2-form $i \partial \bar{\partial} E$ satisfies for $j=1,2$ that
$$\left|\nabla_{\omega_{\mathcal{C}}}^{j}(i \partial \bar{\partial} E)\right|_{\omega_{\mathcal{C}}} \leqslant C|b|^{\frac{2}{n}} T_{0}^{\frac{n+1}{2 n}(2-j)} .$$
Now the metric $|b|^{\frac{1}{n}} \omega_{\mathcal{C}}$ in the statement of the proposition is simply a rescaling of $\omega_{\mathcal{C}}$. If $\tilde{\omega}=A \omega$ for some constant $A>0$, then for any 2-form T,
$$\left|\nabla_{\tilde{\omega}}^{j} \mathbf{T}\right|_{\tilde{\omega}}^{2}=A^{-2-j}\left|\nabla_{\omega}^{j} \mathbf{T}\right|_{\omega}^{2} .$$
The proposition follows from (2.204)-(2.205). \(\square\)

\section*{3. The glued approximate Kähler-Einstein metric}
3.1. Setting up the glued metric and the Monge-Ampère equation. Before defining the glued metric, we briefly review some material from previous sections and fix some parameters.

First, we have a family of Tian-Yau spaces $T Y_{\sigma}$ as our singularity models, see (2.6). We have smooth embeddings $\Phi_{\sigma}: T Y_{0} \backslash \bar{B}_{|\sigma|^{1 / 3} R} \rightarrow T Y_{\sigma}$ onto a neighborhood of infinity in $T Y_{\sigma}$ for $\sigma \neq 0$, see (2.73). In Section 2.3 we review the Tian-Yau construction $\left(\psi_{T Y_{1}}, \omega_{T Y_{1}}, \Omega_{T Y_{1}}\right)$ on $T Y_{1}$ and its decay towards the Calabi model data $\left(\psi_{\mathcal{C}}, \omega_{\mathcal{C}}, \Omega_{\mathcal{C}}\right)$ on $T Y_{0}$ via $\Phi_{1}$. This gives rise to a family $\left(\psi_{T Y_{\sigma}}, \omega_{T Y_{\sigma}}, \Omega_{T Y_{\sigma}}\right)$ via the biholomorphism $m_{\sigma}: T Y_{\sigma} \rightarrow T Y_{1}$ of (2.73). A tricky point here is that, in the Tian-Yau construction, there is a unique choice of a Hermitian metric $h$ on the line bundle such that the Calabi model potential $\psi_{\mathcal{C}}$ defined using $h$ (see (2.65)) differs from $\psi_{T Y_{1}}$ by an exponentially decaying term. We shall fix this
choice of $h$, i.e., no rescalings of $h$ are allowed. Another point that we hope will aid clarity is that we are not allowing any rescalings of $\Omega_{\mathcal{C}}$. This also fixes the scale of $\omega_{\mathcal{C}}$ because $\omega_{\mathcal{C}}^{2}=\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}$.

Secondly, we have a family of canonically polarized surfaces $\mathcal{X}_{\sigma} \subset \mathbb{C P}^{3}$ and hyperplane sections $\mathcal{D}_{\sigma}$ with $\left[2 \mathcal{D}_{\sigma}\right]=K_{\mathcal{X}_{\sigma}}$, see (2.1) and (2.5). We have a family of algebraic holomorphic volume forms $\Omega_{\sigma}$ on the affine surfaces $\mathcal{Y}_{\sigma}=\mathcal{X}_{\sigma} \backslash \mathcal{D}_{\sigma}$, which are unique up to scaling (Remark 2.1). On the regular part of $\mathcal{Y}_{0}$, i.e., on the complement of the origin, we have a Kähler-Einstein metric $\omega_{K E, 0}=i \partial \bar{\partial} \psi_{K E, 0}$ with $e^{-\psi_{K E, 0} \omega_{K E, 0}^{2}}=\Omega_{0} \wedge \bar{\Omega}_{0}$ (Lemma 2.10). We remark that the additive normalization of $\psi_{K E, 0}$ depends on the choice of a scale of $\Omega_{0}$, which we will fix in a moment.

Third, we fix a local holomorphic identification $\Psi_{\sigma}$ of $T Y_{\sigma}$ and $\mathcal{X}_{\sigma}$, see (2.9). By Lemma 2.12, by a suitable (unique) rescaling of $\Omega_{0}$ we can achieve that $\left(\Psi_{0}^{-1}\right)^{*}\left(\Omega_{0} \wedge \bar{\Omega}_{0}\right)=\left(1+O\left(e^{\frac{t}{2}}\right)\right)\left(\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}\right)$ as $t=\log h \rightarrow-\infty$. We remark that there is no scaling ambiguity for $\Omega_{\sigma}$ any more since $\Omega_{0}$ is fixed. To get rid of the term $-3 \log (1-\mathfrak{s} / t)$ in the expansion of $\left(\Psi_{0}^{-1}\right)^{*} \psi_{K E, 0}-\psi_{\text {cusp }}$, we have to compose $\Psi_{\sigma}$ with scale $_{e^{-\mathfrak{s}}}$, but it is harmless for our purposes to assume directly that $\mathfrak{s}=0$ (see Remark 2.15). Thus we achieve that $\left(\Psi_{0}^{-1}\right)^{*} \psi_{K E, 0}-\psi_{\text {cusp }}=O\left(e^{-\delta_{0} \sqrt{-t}}\right)$ as $t \rightarrow-\infty$ for some $\delta_{0}>0$. Here, $\psi_{\text {cusp }}$ has already been normalized by adding a constant such that $e^{-\psi_{\text {cusp }}} \omega_{\text {cusp }}^{2}=\Omega_{\mathcal{C}} \wedge \bar{\Omega}_{\mathcal{C}}$. The same relation holds for the horn metrics $\left(\psi_{T}, \omega_{T}\right)$ of Section 2.4 instead of $\left(\psi_{\text {cusp }}, \omega_{\text {cusp }}\right)$.

We review the relations between different parameters. The position of the horn is fixed via
$$T:=\frac{2}{3} \log |\sigma| .$$
This is motivated by the discussion in Section 1.3. By (2.132), the parameter $b<0$ satisfies that $|b|$ is uniformly comparable to $|T|^{-3}$. Our preferred radius coordinate $t=\log h$ differs from $\log |z|^{2}$ by a uniformly bounded function, see again the discussion before (1.3). Here, $|z|$ is the standard radius in $\mathbb{C}^{3}$, where $T Y_{\sigma}$ and $\mathcal{Y}_{\sigma}$ are embedded by definition. Thus, $|\sigma||z|^{-3}$ is comparable to $e^{-(3 / 2)(t-T)}$.

The orange gluing region, where the end of the Tian-Yau space is attached to the left end of the new neck, is parametrized by $t \in\left[T+T_{0}, T+2 T_{0}\right]$ (see Figure 2 and Remark 2.22). Here, as in (2.176),
$$T_{0}:=|T|^{\alpha} \text { for some fixed } \alpha \in(0,1) .$$
The limit $\alpha \rightarrow 1$ corresponds to the naive gluing of the cusp metric and the Tian-Yau metric described after (1.3), whereas in this paper we will always fix $\alpha$ to be arbitrarily close to zero. It is also worth noting that we do not glue with the Tian-Yau metric normalized exactly as above but, rather, with a scaled copy of it, where the scaling factor $\mathfrak{c}$ equals $\sqrt{2}$ for $n=2$; see (2.178). We could have hidden this factor in our normalization of $\Omega_{\mathcal{C}}$, but we chose not to do so because $\mathfrak{c}$ appears much later in the paper than $\Omega_{\mathcal{C}}$, and a lot of other choices depend on the initial choice of $\Omega_{\mathcal{C}}$.

Lastly, the green gluing region between the neck and the cusp is parametrized by $t \in[2 \tau, \tau]$ (see Remark 2.22). The only requirement so far was that $\tau / T \rightarrow 0$ as $\sigma \rightarrow 0$. We now fix $\tau$ such that
$$|b||\tau|^{3}=e^{-\delta_{0} \sqrt{-\tau}},$$
hence in particular $\tau \sim-\left(\left(3 / \delta_{0}\right) \log |T|\right)^{2}$. This is the classical choice of making the two gluing errors on the left side and on the right side of the gluing region comparable to each other ((3.11), line 3).

Definition 3.1. We now define our glued approximate Kähler-Einstein metric $\omega_{\text {glue }, \sigma}$ on $\mathcal{X}_{\sigma}$. On the affine surface $\mathcal{Y}_{\sigma}=\mathcal{X}_{\sigma} \backslash \mathcal{D}_{\sigma}$ we set $\omega_{\text {glue }, \sigma}:=i \partial_{\sigma} \bar{\partial}_{\sigma} \psi_{\text {glue }, \sigma}$, where $\psi_{\text {glue }, \sigma}$ is defined as follows. We need to distinguish 7 different regions $\Re_{1}, \ldots, \Re_{7}$; see Table 1 and Figure 3. We begin by setting
$$\psi_{\text {glue }, \sigma}:=\psi_{F S, \sigma}+\left(G_{\sigma}^{-1}\right)^{*} \psi_{0} \text { on } \Re_{1}:=\Psi_{\sigma}^{-1}\left(\Phi_{\sigma}(\{t>-N\})\right) \cup\left(\mathcal{Y}_{\sigma} \backslash \operatorname{dom} \Psi_{\sigma}\right) .$$
Here $\psi_{F S, \sigma}$ was defined in (2.31), $\psi_{0}=\psi_{K E, 0}-\psi_{F S, 0}$ (Lemma 2.9), and $G_{\sigma}$ is the $C^{5}$ diffeomorphism from Lemma 2.7, while $N$ is an arbitrary but fixed large positive constant such that $\Phi_{\sigma}(\{t<-N / 2\})$ is contained in $\operatorname{dom} \Psi_{\sigma}^{-1}$. Clearly $\omega_{\text {glue }, \sigma}$ is then at least $C^{3}$ at the divisor $\mathcal{D}_{\sigma}$.

\begin{table}
\captionsetup{labelformat=empty}
\caption{Table 1. Properties of $\omega_{\text {glue }, \sigma}$. The estimates are sharp up to constant factors.}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline \backslashbox{Property}{Region} & \multirow[t]{2}{*}{\begin{tabular}[t]{l}
$\Re_{1}$ \\
compact part of $\mathcal{X}_{\sigma}$
\end{tabular}} &
\begin{tabular}[t]{l}
$\Re_{2}$ \\
hyperbolic cusp
\end{tabular} &
\begin{tabular}[t]{l}
$\Re_{3}$ \\
green gluing
\end{tabular} &
\begin{tabular}[t]{l}
$\Re_{4}$ \\
middle neck
\end{tabular} \\
\hline Range of $t=\log h$ & & $\tau<t<-N$ & $2 \tau<t<\tau$ & $T+2 T_{0}<t<2 \tau$ \\
\hline Diameter & 1 & $\log \log |T|$ & 1 & $\log |T|$ \\
\hline Curvature & 1 & 1 & 1 & $|b|^{-\frac{1}{2}}(t-T)^{-\frac{3}{2}}$ \\
\hline \backslashbox{Property}{Region} &
\begin{tabular}[t]{l}
$\Re_{5}$ \\
orange gluing
\end{tabular} &
\begin{tabular}[t]{l}
$\Re_{6}$ \\
Tian-Yau end
\end{tabular} & \multirow[t]{2}{*}{\begin{tabular}[t]{l}
$\Re_{7}$ \\
Tian-Yau cap
\end{tabular}} & \multirow[t]{4}{*}{\begin{tabular}[t]{l}
$$\begin{aligned}
& |T| \sim|\log | \sigma|\mid \\
& T_{0}=|T|^{\alpha}(\alpha \ll 1) \\
& |b| \sim|T|^{-3} \\
& \tau \sim(\log |T|)^{2}
\end{aligned}$$ \\
$N, R$ const $\gg 1$
\end{tabular}} \\
\hline Range of $t=\log h$ & $T_{0}<t-T<2 T_{0}$ & $\log R<t-T<T_{0}$ & & \\
\hline Diameter & $|T|^{-\frac{3}{4}(1-\alpha)}$ & $|T|^{-\frac{3}{4}(1-\alpha)}$ & $|T|^{-\frac{3}{4}}$ & \\
\hline Curvature & $|b|^{-\frac{1}{2}}(t-T)^{-\frac{3}{2}}$ & $|b|^{-\frac{1}{2}}(t-T)^{-\frac{3}{2}}$ & $|b|^{-\frac{1}{2}}$ & \\
\hline
\end{tabular}
\end{table}

\begin{figure}
\captionsetup{labelformat=empty}
\caption{Figure 3. The seven regions of $\mathcal{X}_{\sigma}$. For the middle neck $\Re_{4}$ see also Figure 2.}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/a0f996e3-fe3b-459a-a543-f9d8a2350896-31.jpg?height=637&width=1386&top_left_y=1153&top_left_x=364}
\end{figure}

For the remaining 6 regions we prefer to write down formulas for $\left(\Psi_{\sigma}^{-1}\right)^{*} \psi_{g l u e, \sigma}$ on $T Y_{\sigma}$ rather than for $\psi_{\text {glue }, \sigma}$ on $\mathcal{X}_{\sigma}$. To this end, let $\chi_{1}(t)$ be smooth and increasing with $\chi_{1}(t)=0$ for $t \leqslant T+T_{0}$ and $\chi_{1}(t)=1$ for $t \geqslant T+2 T_{0}$, and with $\left|\partial_{t}^{j} \chi_{1}\right|=O_{j}\left(T_{0}^{-j}\right)$ for all $j \geqslant 0$. Similarly, let $\chi_{2}(t)$ be smooth and increasing with $\chi_{2}(t)=0$ for $t \leqslant 2 \tau$ and $\chi_{2}(t)=1$ for $t \geqslant \tau$, and with $\left|\partial_{t}^{j} \chi_{2}\right|=O_{j}\left(|\tau|^{-j}\right)$ for all $j \geqslant 0$. Then the desired formulas for $\left(\Psi_{\sigma}^{-1}\right)^{*} \psi_{g l u e, \sigma}$ are as follows:
$$\begin{aligned}
\left(\Psi_{\sigma}^{-1}\right)^{*} \psi_{F S, \sigma}+\left(\left(\Psi_{\sigma} \circ G_{\sigma}\right)^{-1}\right)^{*} \psi_{0} \text { on } \Psi_{\sigma}\left(\Re_{2}\right) & :=\Phi_{\sigma}(\{\tau<t<-N\}), \\
\left(\Phi_{\sigma}^{-1}\right)^{*}\left(\chi_{2}\left(\Psi_{0}^{-1}\right)^{*}\left(G_{\sigma}^{*} \psi_{F S, \sigma}+\psi_{0}\right)+\left(1-\chi_{2}\right) \psi_{T}\right) \text { on } \Psi_{\sigma}\left(\Re_{3}\right) & :=\Phi_{\sigma}(\{2 \tau<t<\tau\}), \\
\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T} \text { on } \Psi_{\sigma}\left(\Re_{4}\right) & :=\Phi_{\sigma}\left(\left\{T+2 T_{0}<t<2 \tau\right\}\right), \\
\left(\Phi_{\sigma}^{-1}\right)^{*}\left(\chi_{1} \psi_{T}+\left(1-\chi_{1}\right) \Phi_{\sigma}^{*}\left(\mathfrak{c}|b|^{\frac{1}{2}} \psi_{T Y_{\sigma}}+\psi_{T}(T)\right)\right) \text { on } \Psi_{\sigma}\left(\Re_{5}\right) & :=\Phi_{\sigma}\left(\left\{T_{0}<t-T<2 T_{0}\right\}\right), \\
\mathfrak{c}|b|^{\frac{1}{2}} \psi_{T Y_{\sigma}}+\psi_{T}(T) \text { on } \Psi_{\sigma}\left(\Re_{6}\right) & :=\Phi_{\sigma}\left(\left\{t<T+T_{0}\right\}\right), \\
\mathfrak{c}|b|^{\frac{1}{2}} \psi_{T Y_{\sigma}}+\psi_{T}(T) \text { on } \Psi_{\sigma}\left(\Re_{7}\right) & :=\left(\operatorname{dom} \Psi_{\sigma}^{-1}\right) \backslash\left(\mathrm{im} \Phi_{\sigma}\right) .
\end{aligned}$$

This concludes our definition of the glued approximate Kähler-Einstein manifold $\left(\mathcal{X}_{\sigma}, \omega_{g l u e, \sigma}\right)$.
The Monge-Ampère equation that we want to solve is
$$\left(\omega_{\text {glue }, \sigma}+i \partial \bar{\partial} u_{\sigma}\right)^{2}=e^{u_{\sigma}-f_{\sigma}} \omega_{g l u e, \sigma}^{2},$$
where $f_{\sigma}$ is the Ricci potential, defined up to a constant by the condition that
$$\operatorname{Ric}\left(\omega_{\text {glue }, \sigma}\right)+\omega_{\text {glue }, \sigma}+i \partial \bar{\partial} f_{\sigma}=0 .$$

Lemma 3.2. Up to an arbitrary constant,
$$\left.f_{\sigma}\right|_{\mathcal{Y}_{\sigma}}=\log \left(\frac{\omega_{g l u e, \sigma}^{2}}{\Omega_{\sigma} \wedge \bar{\Omega}_{\sigma}}\right)-\psi_{g l u e, \sigma} .$$
Proof. Denote the right-hand side of (3.8) by $g_{\sigma}$.
Claim 3.3. $g_{\sigma}$ extends at least $C^{3}$ to $\mathcal{X}_{\sigma}$.
Proof of Claim 3.3. We know that $\omega_{\text {glue }, \sigma}^{2}$ is at least $C^{3}$ on $\mathcal{X}_{\sigma}$ and $\Omega_{\sigma} \wedge \bar{\Omega}_{\sigma}=\left|H_{\mathcal{D}_{\sigma}}\right|^{4} \cdot\left(\right.$ smooth on $\left.\mathcal{X}_{\sigma}\right)$, where $H_{\mathcal{D}_{\sigma}}$ is a defining section of the line bundle $\left[\mathcal{D}_{\sigma}\right]$ and $|\cdot|$ is any smooth Hermitian metric on this line bundle. Thus, the log volume ratio in (3.8) is of the form $\log \left|H_{\mathcal{D}_{\sigma}}\right|^{-4}+\left(\right.$ at least $C^{3}$ on $\left.\mathcal{X}_{\sigma}\right)$. Finally, since the reference Kähler form $\omega_{F S, \sigma}$ represents the Poincaré dual of the divisor class $\left[2 \mathcal{D}_{\sigma}\right]$, we have that $\psi_{\text {glue }, \sigma}=\psi_{F S, \sigma}+\left(\right.$ at least $C^{5}$ on $\left.\mathcal{X}_{\sigma}\right)=\log \left|H_{\mathcal{D}_{\sigma}}\right|^{-4}+\left(\right.$ at least $C^{5}$ on $\left.\mathcal{X}_{\sigma}\right)$. Thus, the two log terms in the definition of $g_{\sigma}$ cancel each other out and the remainder is at least $C^{3}$. \(\square\)

From its definition, (3.7), and by elliptic regularity, $f_{\sigma}$ is at least $C^{2, \alpha}$ on $\mathcal{X}_{\sigma}$. Hence, by Claim 3.3, so is $f_{\sigma}-g_{\sigma}$. From the definition of $g_{\sigma}$ and from the standard formula for the Ricci curvature of a Kähler metric, $g_{\sigma}$ satisfies $\operatorname{Ric}\left(\omega_{\text {glue }, \sigma}\right)+\omega_{\text {glue }, \sigma}+i \partial \bar{\partial} g_{\sigma}=0$ (on $\mathcal{Y}_{\sigma}$ and thus, by Claim 3.3, on $\mathcal{X}_{\sigma}$ ). Thus, $f_{\sigma}-g_{\sigma}$ is pluriharmonic on $\mathcal{X}_{\sigma}$ and hence constant. \(\square\)

Of course, we already know that, given $f_{\sigma}$, the Monge-Ampère equation (3.6) has a unique solution $u_{\sigma}$ by the Aubin-Yau theorem [2, 40], and if we change $f_{\sigma}$ by a constant then $u_{\sigma}$ changes by the same constant. Our main goal in this paper is to prove that $u_{\sigma}$ is actually small modulo constants, meaning at the very least that $\sup _{\mathcal{X}_{\sigma}}\left|i \partial \bar{\partial} u_{\sigma}\right|_{\omega_{\text {glue }, \sigma}} \rightarrow 0$ as $\sigma \rightarrow 0$. Clearly, the first step here is to prove that $f_{\sigma}$ is sufficiently small modulo constants, using the expression in (3.8). This estimate is the main result of Section 3 and we record it in Theorem 3.5. To state the theorem, we need one other definition.

Definition 3.4. The regularity scale function $\mathbf{r}_{\sigma}: \mathcal{X}_{\sigma} \rightarrow \mathbb{R}^{+}$of $\omega_{\text {glue }, \sigma}$ is defined as follows:
$$\mathbf{r}_{\sigma}:= \begin{cases}1 & \text { on } \Psi_{\sigma}^{-1}\left(\Phi_{\sigma}(\{t>T / 2\})\right) \cup\left(\mathcal{X}_{\sigma} \backslash \operatorname{dom} \Psi_{\sigma}\right), \\ \Psi_{\sigma}^{*}\left(\Phi_{\sigma}^{-1}\right)^{*}\left(|b|^{\frac{1}{4}}(t-T)^{\frac{3}{4}}\right) & \text { on } \Psi_{\sigma}^{-1}\left(\Phi_{\sigma}(\{t<T / 2\})\right), \\ |b|^{\frac{1}{4}} & \text { on } \Re_{7} .\end{cases}$$
Up to bounded factors that we suppress, $\mathbf{r}_{\sigma}(p)$ is the maximal radius of an $\omega_{g l u e, \sigma}$-ball $B_{r}(p)$ such that $r^{-2} \omega_{\text {glue }, \sigma}$ is $C^{\infty}$ bounded in coordinates on the universal cover of $B_{r}(p)$. In particular, the curvature of $\omega_{\text {glue }, \sigma}$ is uniformly $O\left(\mathbf{r}_{\sigma}^{-2}\right)$. This is the curvature estimate recorded in Table 1 and it is sharp.

We are now able to state our main result in this section. The proof is deferred to Section 3.2.
Theorem 3.5. Let $f_{\sigma}$ be the Ricci potential defined in (3.8). Then for all $\varepsilon>0$ the function
$$\left|f_{\sigma}\right|+\mathbf{r}_{\sigma}\left|\nabla_{\omega_{\text {glue }, \sigma}} f_{\sigma}\right|_{\omega_{\text {glue }, \sigma}}$$
satisfies the following pointwise estimates as $\sigma \rightarrow 0$ :
$$\begin{cases}O(|\sigma|) & \text { on } \mathfrak{R}_{1}, \\ O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) & \text { on } \mathfrak{R}_{2}, \\ O\left(|b||\tau|^{3}\right)+O\left(e^{-\delta_{0} \sqrt{-t}}\right) & \text { on } \Re_{3}, \\ O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right)+O\left(e^{\left(\frac{1}{2}-\varepsilon\right) t}\right) & \text { on } \Re_{4}, \\ O\left(\left(T_{0} /|T|\right)^{\frac{3}{2}}\right) & \text { on } \Re_{5} \cup \Re_{6} \cup \Re_{7} .\end{cases}$$
Here we abuse notation by writing $t$ instead of the correct $\Psi_{\sigma}^{*}\left(\Phi_{\sigma}^{-1}\right)^{*} t$.
Remark 3.6. The shape of (3.11) makes sense intuitively: $f_{\sigma}$ decays faster than any polynomial in $|T|$ on $\Re_{1} \cup \Re_{2} \cup \Re_{4}$ because $\omega_{g l u e, \sigma}$ is almost an exact solution of the negative Kähler-Einstein equation in these regions. On the other hand, on $\Re_{5} \cup \Re_{6} \cup \Re_{7}$ we are gluing with the scaled Tian-Yau metric, which is Ricci-flat, so up to some additive constant $f_{\sigma}$ then equals minus the Kähler potential of this metric, whose oscillation is $\sim\left(T_{0} /|T|\right)^{3 / 2}$. The error in the gluing region $\Re_{3}$ is also polynomial in $|T|$ but it is $O\left(|T|^{-3}|\log | T| |^{6}\right.$ ), i.e., almost quadratic compared to the error in the Tian-Yau region.

Remark 3.7. Using only (3.11) and standard facts from the theory of the complex Monge-Ampère equation, one can already deduce quite a bit of information about the solution $u_{\sigma}$. For example, the maximum principle applied to (3.6) immediately yields that
$$\sup _{\mathcal{X}_{\sigma}}\left|u_{\sigma}\right| \leqslant \sup _{\mathcal{X}_{\sigma}}\left|f_{\sigma}\right|=O\left(|b|^{\frac{1-\alpha}{2}}\right) .$$
On $\Re_{1} \cup \Re_{2} \cup \Re_{3}$ and on a large portion of the middle neck $\Re_{4}$, the regularity scale $\mathbf{r}_{\sigma}$ is uniformly bounded below, i.e., we have uniform $C^{\infty}$ bounds for $\omega_{\text {glue }, \sigma}$ on the universal cover of a geodesic ball of definite size centered at any point. Thus, on all of these regions, $\left|i \partial \bar{\partial} u_{\sigma}\right|_{\omega_{\text {glue }, \sigma}}=O\left(|b|^{(1-\alpha) / 2}\right)$ by combining (3.12) and Savin's small perturbation theorem [32, Thm 1.3]. This estimate already implies $C_{\text {loc }}^{\infty}$ convergence of $\omega_{K E, \sigma}$ to $\omega_{K E, 0}$ away from any fixed neighborhood of the origin in $\mathbb{C}^{3}$.

On the other hand, moving towards the left boundary of the middle neck $\Re_{4}$ and into $\Re_{5} \cup \Re_{6} \cup \Re_{7}$, the regularity scale $\mathbf{r}_{\sigma}$ decays until it reaches its minimum of $|b|^{1 / 4}$ on the Tian-Yau cap $\Re_{7}$. To be able to apply Savin's theorem in this situation we would need that $\left|u_{\sigma}\right| \ll \mathbf{r}_{\sigma}^{2}$, i.e., $\left|u_{\sigma}\right| \ll|b|^{1 / 2}$ on $\Re_{7}$. This is obviously out of reach of (3.12) no matter how small we make $\alpha$.

The point of the weighted Hölder space theory developed in the rest of the paper (after the proof of Theorem 3.5) is precisely to improve the naive $C^{0}$ estimate (3.12) in the Tian-Yau region. We will for instance be able to prove that $\sup _{\Re_{7}}\left|u_{\sigma}\right|=O_{\varepsilon}\left(|b|^{(5 / 6)-\varepsilon}\right)$ for all $\varepsilon>0$. This is enough to obtain $C^{1, \beta}$ closeness of $\omega_{K E, \sigma}$ to the scaled Tian-Yau metric on $\Re_{7}$ for all $\beta<\frac{1}{3}$, which in particular proves the Main Theorem. In fact, we conjecture that a more systematic approach to the obstruction theory in Section 5.2 would even yield $\sup _{\Re_{7}}\left|u_{\sigma}\right|=O_{\varepsilon}\left(|b|^{1-\varepsilon}\right)$ and thus $C^{1, \beta}$ closeness for all $\beta<1$. This would then be optimal because a Ricci-flat metric cannot be $C^{1,1}$ close to a metric with Ricci = -1.
3.2. Proof of the Ricci potential estimate. This section is dedicated to the proof of Theorem 3.5. This will be done at the end of this section, as a consequence of a long sequence of lemmas.

We shall pull back everything back to $T Y_{0}$ and then estimate.
Lemma 3.8. On $T Y_{0}$, the following hold.
\begin{itemize}
\item[(1)] If $t \in\left[T+T_{0}, \tau\right]$, one has
$$\left|\nabla_{\omega_{T}}^{k}\left(\Phi_{\sigma}^{*} J_{T Y_{\sigma}}-J_{\mathcal{C}}\right)\right|_{\omega_{T}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) \text { for all } k \geqslant 0, \varepsilon>0 .$$
\item[(2)] If $t \in[2 \tau,-N]$, one has
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\Phi_{\sigma}^{*} J_{T Y_{\sigma}}-J_{\mathcal{C}}\right)\right|_{\omega_{\text {cusp }}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) \text { for all } k \geqslant 0, \varepsilon>0 .$$
\end{itemize}

Proof. In Lemma 2.18 we have proved that this holds for the reference metric $|b|^{1 / 2} \omega_{\mathcal{C}, \sigma}$ instead of $\omega_{T}$ or $\omega_{\text {cusp }}$, assuming only that $t-T \rightarrow \infty$. To compare these reference metrics, we now estimate
$$\left|\nabla_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}}^{k} \omega_{T}\right|_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}} \text { and }\left|\nabla_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}}^{k} \omega_{\text {cusp }}\right|_{|b|^{\frac{1}{2}} \omega_{\mathcal{C}, \sigma}} \text { for all } k \geqslant 0 .$$

For $\delta>0$ fixed and $t / T \geqslant 1-\delta$, (2.164)-(2.165) say that $\omega_{T}$ is uniformly comparable to $|b|^{1 / 2} \omega_{\mathcal{C}, \sigma}$. For $k>0$, first notice that by (2.172), the $t$-derivatives of $\psi_{T}$ blow up at worst polynomially in $|T|$. Using the quasi-coordinates (2.190) for $\omega_{\mathcal{C}, \sigma}$ and $|b| \sim|T|^{-3}$, we deduce that the $k$-th derivative of $\omega_{T}$ with respect to $|b|^{1 / 2} \omega_{\mathcal{C}, \sigma}$ is bounded by $|T|^{N_{k}}$ for some $N_{k} \in \mathbb{N}$. The exponential term $e^{-(1 / 2-\varepsilon)(t-T)}$ absorbs these polynomial factors because $t-T \geqslant T_{0}=|T|^{\alpha}$. This proves (1) for $t / T \geqslant 1-\delta$.

Now assume $t / T \leqslant 1-\delta$ and $t \leqslant-N$. We first compare $\omega_{T}$ to $\omega_{\text {cusp }}$ in a similar fashion, using Proposition 2.26. Then we compare $\omega_{\text {cusp }}$ to $|b|^{1 / 2} \omega_{\mathcal{C}, \sigma}$ using the fact that these metrics are explicit. This yields the remaining case of (1) $(t / T \leqslant 1-\delta, t \leqslant \tau)$ and all cases of (2) $(2 \tau \leqslant t \leqslant-N)$. \(\square\)

Similar arguments yield:
Lemma 3.9. On $T Y_{0}$, the following hold.
\begin{itemize}
\item[(1)] If $t \in\left[T+T_{0}, \tau\right]$, then for all $k \geqslant 0$ there exists a positive integer $N_{k}$ such that
$$\left|\nabla_{\omega_{T}}^{k} \psi_{T}\right|_{\omega_{T}}=O\left(|T|^{N_{k}}\right) .$$
\item[(2)] If $t \in[2 \tau,-N]$, then for all $k \geqslant 0$ there exists a positive integer $N_{k}$ such that
$$\left|\nabla_{\omega_{\text {cusp }}}^{k} \psi_{\text {cusp }}\right|_{\omega_{\text {cusp }}}=O\left(|T|^{N_{k}}\right) .$$
\end{itemize}

Now we combine Lemma 3.9 and Lemma 3.8 to get the following lemma, which essentially measures the non-holomorphicity of $\Phi_{\sigma}$.

Lemma 3.10. On $T Y_{0}$, the following hold for all $k \geqslant 0, \varepsilon>0$.
\begin{itemize}
\item[(1)] If $t \in\left[T+T_{0}, \tau\right]$, we have that
$$\left|\nabla_{\omega_{T}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T}-\omega_{T}\right)\right|_{\omega_{T}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) .$$
\item[(2)] If $t \in[2 \tau,-N]$, we have that
$$\left|\nabla_{\omega_{\text {cusp }}}^{k}\left(\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma}\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{\text {cusp }}-\omega_{\text {cusp }}\right)\right|_{\omega_{\text {cusp }}}=O\left(e^{-\left(\frac{1}{2}-\varepsilon\right)(t-T)}\right) .$$
\end{itemize}
Proof. Let $A_{\sigma}:=\Phi_{\sigma}^{*} J_{\sigma}-J_{0}$. Then for all functions $f$ on $T Y_{\sigma}$ and Kähler metrics $\omega$ on $T Y_{0}$,
$$\begin{aligned}
\Phi_{\sigma}^{*} i \partial_{\sigma} \bar{\partial}_{\sigma} f-i \partial_{0} \bar{\partial}_{0} \Phi_{\sigma}^{*} f & =\Phi_{\sigma}^{*} d d_{\sigma}^{c} f-d d_{0}^{c} \Phi_{\sigma}^{*} f \\
& =d \Phi_{\sigma}^{*} J_{\sigma} d f-d J_{0} d \Phi_{\sigma}^{*} f \\
& =d\left(\left(A_{\sigma}+J_{0}\right) \Phi_{\sigma}^{*}(d f)\right)-d J_{0} d \Phi_{\sigma}^{*} f \\
& =\left(\nabla_{\omega} A_{\sigma}\right) \circledast\left(\nabla_{\omega}\left(\Phi_{\sigma}^{*} f\right)\right)+A_{\sigma} \circledast\left(\nabla_{\omega}^{2}\left(\Phi_{\sigma}^{*} f\right)\right) .
\end{aligned}$$
Here $\circledast$ denotes a tensorial contraction involving also the reference metric $\omega$. Now we apply this with $\omega=\omega_{T}, \omega_{\text {cusp }}$ and with $f=\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{T},\left(\Phi_{\sigma}^{-1}\right)^{*} \psi_{\text {cusp }}$, respectively. By Lemma 3.8, $A_{\sigma}$ and its covariant derivatives are bounded by $e^{-(1 / 2-\varepsilon)(t-T)}$. On the other hand, $\psi_{\text {cusp }}, \psi_{T}$ and their covariant derivatives blow up at worst polynomially in $|T|$ by Lemma 3.9. Since $t-T \geqslant T_{0}=|T|^{\alpha}$, these polynomial factors are again absorbed by the exponential decay as in the proof of Lemma 3.8. \(\square\)

The following auxiliary lemma will be used in Lemma 3.13.