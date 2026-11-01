---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: [math/0105046] Fredholm Operators and Einstein Metrics on Conformally Compact Manifolds]

Proof. Because $Y_{1}$ is not precompact in $\mathbb{H}$, we have to interpret the $C^{l, \beta}$ norm on the left-hand side of (6.1) as an intrinsic Hölder norm, defined by (3.2). For each point $\left(x_{0}, y_{0}\right) \in Y_{1}$, we have a Möbius chart $\Phi_{\left(x_{0}, y_{0}\right)}: B_{2} \rightarrow V_{2}\left(x_{0}, y_{0}\right) \subset \mathbb{H}$ defined by
$$\Phi_{\left(x_{0}, y_{0}\right)}(x, y)=\left(x_{0}+y_{0} x, y_{0} y\right) .$$
Then we need to get an upper bound for
$$\sup _{\left(x_{0}, y_{0}\right) \in Y_{1}}\left\|\Phi_{\left(x_{0}, y_{0}\right)}^{*}\left(\Psi_{\widehat{p}, r}^{*} g-\breve{g}\right)\right\|_{C^{l, \beta}\left(B_{2}\right)} .$$
Since $\Phi_{\left(x_{0}, y_{0}\right)}$ is a hyperbolic isometry, the norm above is the same as
$$\left\|\left(\Psi_{\widehat{p}, r} \circ \Phi_{\left(x_{0}, y_{0}\right)}\right)^{*} g-\breve{g}\right\|_{C^{l, \beta}\left(B_{2}\right)} .$$
In $(\widetilde{\theta}, \rho)$ coordinates, we have
$$\Psi_{\widehat{p}, r} \circ \Phi_{\left(x_{0}, y_{0}\right)}(x, y)=\left(r x_{0}+r y_{0} x, r y_{0} y\right) .$$
Let us abbreviate this composite map as $\zeta(x, y)=\left(r x_{0}+r y_{0} x, r y_{0} y\right)$, so that
$$\left(\Psi_{\widehat{p}, r} \circ \Phi_{\left(x_{0}, y_{0}\right)}\right)^{*} g-\breve{g}=y^{-2} \zeta^{*}\left(\bar{g}_{i j}-\delta_{i j}\right) d x^{i} d x^{j}$$
Since the $C^{l, \beta}\left(B_{2}\right)$ norm in (6.2) is just the norm of the components in $(x, y)$ -coordinates, and $y^{-2}$ is uniformly bounded on $B_{2}$ together with all its derivatives, it suffices to show that
$$\left\|\zeta^{*} f\right\|_{C^{l, \beta}\left(B_{2}\right)} \leq C r\|f\|_{C_{(0)}^{l, \beta}}$$
for any function $f \in C_{(0)}^{l, \beta}(\Omega)$ that vanishes at $\widehat{p}$. Moreover, the $(\widetilde{\theta}, \rho)$ coordinates are uniformly $C^{l+1, \beta}$-equivalent to the original background coordinates $(\theta, \rho)$, because the coefficients $B^{\alpha}$, the matrix ( $A_{\beta}^{\alpha}$ ), and its inverse are uniformly bounded. Thus the $C_{(0)}^{l, \beta}$ norm of $f$ in $(\widetilde{\theta}, \rho)$ coordinates is uniformly bounded by the global norm $\|f\|_{C_{(0)}^{l, \beta}}$.

To bound the sup norm of $\zeta^{*} f$, we use the mean value theorem and the fact that $f(0,0)=f(\widehat{p})=0$ to estimate
$$\begin{aligned}
\left|\zeta^{*} f(x, y)\right| & =\left|f\left(r x_{0}+r y_{0} x, r y_{0} y\right)-f(0,0)\right| \\
& =\left|d f_{\left(a_{0}, b_{0}\right)}\left(r x_{0}+r y_{0} x, r y_{0} y\right)\right| \\
& \leq C r\|f\|_{C_{(0)}^{1,0}}
\end{aligned}$$
where $\left(a_{0}, b_{0}\right)$ is some point on the line between $(0,0)$ and $\left(r x_{0}+r y_{0} x, r y_{0} y\right)$. For any coordinate $x^{k}(k=1, \ldots, n+1)$, we have
$$\begin{aligned}
\left|\partial_{x^{k}}\left(\zeta^{*} f\right)(x, y)\right| & =\left|r y_{0} \partial_{\theta^{k}} f\left(r x_{0}+r y_{0} x, r y_{0} y\right)\right| \\
& \leq r\|f\|_{C_{(0)}^{1,0}} .
\end{aligned}$$

The Hölder norm of the first derivatives is estimated as follows:
$$\begin{aligned}
& \frac{\left|\partial_{x^{k}}\left(\zeta^{*} f\right)(x, y)-\partial_{x^{k}}\left(\zeta^{*} f\right)\left(x^{\prime}, y^{\prime}\right)\right|}{\left|(x, y)-\left(x^{\prime}, y^{\prime}\right)\right|^{\alpha}} \\
& \quad=\frac{\left|r y_{0} \partial_{\theta^{k}} f\left(r x_{0}+r y_{0} x, r y_{0} y\right)-r y_{0} \partial_{\theta^{k}} f\left(r x_{0}+r y_{0} x^{\prime}, r y_{0} y^{\prime}\right)\right|}{\left|(x, y)-\left(x^{\prime}, y^{\prime}\right)\right|^{\alpha}} \\
& \quad \leq \frac{r\|f\|_{C_{(0)}^{1, \alpha}}\left|\left(r x_{0}+r y_{0} x, r y_{0} y\right)-\left(r x_{0}+r y_{0} x^{\prime}, r y_{0} y^{\prime}\right)\right|^{\alpha}}{\left|(x, y)-\left(x^{\prime}, y^{\prime}\right)\right|^{\alpha}} \\
& \quad \leq C r^{1+\alpha}\|f\|_{C_{(0)}^{1, \alpha}}
\end{aligned}$$
The general case now follows by induction on $l$, using the fact that $\partial_{x^{k}}\left(\zeta^{*} f\right)=$ $r y_{0} \Phi_{\widehat{p}}^{*}\left(\partial_{\theta^{k}} f\right)$. \(\square\)

We need to explore how the weighted Sobolev and Hölder norms behave under boundary Möbius charts. The function $y$ is not a defining function for hyperbolic space because it blows up at infinity; however, by patching together via a partition of unity, it is easy to construct a smooth defining function $\rho_{0}$ for hyperbolic space that is equal to $y$ on $Y_{1}$. Then for any boundary Möbius chart $\Psi_{\widehat{p}, r}$, it follows that $\Psi_{\widehat{p}, r}^{*} \rho=y=\rho_{0}$ on $Y_{1}$ for $r$ sufficiently small, so by the same reasoning that led to (3.4) and (3.5), the weighted norms have the following scaling behavior under boundary Möbius charts:
$$\begin{aligned}
& C^{-1} r^{-\delta}\left\|\Psi_{\widehat{p}, r}^{*} u\right\|_{k, \alpha ; Y_{1}} \leq\|u\|_{k, \alpha, \delta ; Z_{r}(\widehat{p})} \leq C r^{-\delta}\left\|\Psi_{\widehat{p}, r}^{*} u\right\|_{k, \alpha ; Y_{1}} \\
& C^{-1} r^{-\delta}\left\|\Psi_{\widehat{p}, r}^{*} u\right\|_{k, p ; Y_{1}} \leq\|u\|_{k, p, \delta ; Z_{r}(\widehat{p})} \leq C r^{-\delta}\left\|\Psi_{\widehat{p}, r}^{*} u\right\|_{k, p ; Y_{1}}
\end{aligned}$$

Choose a specific smooth bump function $\psi: \mathbb{H} \rightarrow[0,1]$ that is equal to 1 on $A_{1 / 2}$ and supported in $A_{1}$. For any $\widehat{p} \in \partial M$ and any $r>0$, let $(\widetilde{\theta}, \rho)$ be the coordinates on a neighborhood $\Omega$ of $\widehat{p}$ constructed above, and define $\psi_{\widehat{p}, r} \in C^{l, \beta}(\Omega)$ by
$$\psi_{\widehat{p}, r}(\widetilde{\theta}, \rho)=\left(\Psi_{\widehat{p}, r}^{-1}\right)^{*} \psi=\psi(\widetilde{\theta} / r, \rho / r) .$$
Because the different choices of $(\widetilde{\theta}, \rho)$ coordinates are all uniformly bounded in $C_{(0)}^{l+1, \beta}(\Omega)$ with respect to each other, and $|d \rho|_{g},\left|d \widetilde{\theta}^{\alpha}\right|_{g}$ are both in $C_{1}^{l, \beta}(M)$ with norms independent of $\widehat{p}$, it follows that the functions $\psi_{\widehat{p}, r}$ are uniformly bounded in $C^{l, \beta}(\Omega)$, independently of $\widehat{p}$ and $r$.

By the same argument as in Lemma 2.2, there is a number $N$ such that for any $r>0$ we can choose (necessarily finitely many) points $\left\{\widehat{p}_{1}, \ldots, \widehat{p}_{m}\right\} \subset \partial M$ such that the sets $\left\{Z_{r / 2}\left(\widehat{p}_{i}\right)\right\}$ cover $A_{r / 2}=\{p \in M: \rho(p)<r / 2\}$ and no more than $N$ of the sets $\left\{Z_{r}\left(\widehat{p}_{i}\right)\right\}$ intersect nontrivially at any point. For any such covering, let $\Psi_{i}=\Psi_{\hat{p}_{i}, r}$ and $\psi_{i}=\psi_{\hat{p}_{i}, r}$. Let $\psi_{0} \in C_{c}^{\infty}(M)$ be a smooth bump function that is supported in $M \backslash A_{r / 4}$ and equal to 1 on $M \backslash A_{r / 2}$, and define
$$\varphi_{i}=\frac{\psi_{i}}{\left(\sum_{j=0}^{m} \psi_{i}^{2}\right)^{1 / 2}} .$$
It follows that $\left\{\varphi_{i}^{2}\right\}$ is a partition of unity for $\bar{M}$ subordinate to the cover $\{M \backslash$ $\left.A_{r / 4}, Z_{r}\left(\widehat{p}_{i}\right)\right\}$. Moreover, at each point of $\bar{M}$, at least one of the functions $\psi_{i}$ is equal to 1 at and at most $N$ of them are nonzero, so the functions $\varphi_{i}$ are still uniformly bounded in $C_{(0)}^{l, \beta}(\bar{M})$.

Let $\breve{E}$ be the tensor bundle over hyperbolic space associated with the same $\mathrm{O}(n+1)$ or $\mathrm{SO}(n+1)$ representation as $E$, and let $\breve{P}$ be the operator on hyperbolic space with the same local coordinate expression as $P$. For each boundary Möbius chart $\Psi_{i}$, let $g_{i}$ be the metric $\Psi_{i}^{*} g$ defined on $Y_{1} \subset \mathbb{H}$, and let $P_{i}: C^{\infty}\left(Y_{1} ; E\right) \rightarrow$ $C^{\infty}\left(Y_{1} ; E\right)$ be the operator defined by
$$P_{i} u:=\Psi_{i}^{*} P\left(\Psi_{i}^{-1 *} u\right) .$$
Then Lemma 6.1 implies that $P_{i}$ is close to $P$ in the following sense: For each $\delta \in \mathbb{R}, 0<\alpha<\overline{1}, 1<p<\infty$, and $k$ such that $m \leq k \leq l$ and $m<k+\alpha \leq l+\beta$, there is a constant $C$ (independent of $r$ or $i$ ) such that for all $u \in C^{k, \alpha, \delta}(M ; E)$,
$$\left\|P_{i} u-P u\right\|_{k-m, \alpha, \delta} \leq C r\|u\|_{k, \alpha, \delta},$$
and for all $u \in H^{k, p, \delta}(M ; E)$,
$$\left\|P_{i} u-P u\right\|_{k-m, p, \delta} \leq C r\|u\|_{k, p, \delta} .$$

Now assume that $P$ satisfies the hypotheses of Theorem In particular, there is some constant $C$ such that the $L^{2}$ estimate (1.4) holds on the complement of some compact set. Choosing $\widehat{p} \in \partial M$ arbitrarily and $r$ sufficiently small, (6.6) and (6.4) together imply that $\breve{P}$ satisfies an analogous estimate (perhaps with a larger constant) for all smooth sections $u$ of $\breve{E}$ compactly supported in $Y_{1}$. But if $u \in C_{c}^{\infty}(\mathbb{H} ; E)$ is arbitrary, there is a Möbius transformation that takes $\operatorname{supp} u$ into $Y_{1}$, so the same estimate holds globally on $\mathbb{H}$. Therefore, by the results of Chapter $\stackrel{\rightharpoonup}{P}$ is invertible on $C_{\delta}^{k, \alpha}(\mathbb{H} ; E)$ for $|\delta-n / 2|<R$, and on $H_{\delta}^{k, p}(\mathbb{H} ; E)$ for $|\delta+n / p-n / 2|<R$.

For any sufficiently small $r>0$, define operators $Q_{r}, S_{r}, T_{r}: C_{c}^{\infty}(M ; E) \rightarrow$ $C_{c}^{\infty}(M ; E)$ by
$$\begin{aligned}
Q_{r} u & =\sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1} \Psi_{i}^{*}\left(\varphi_{i} u\right), \\
S_{r} u & =\sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1}\left(P_{i}-\breve{P}\right) \Psi_{i}^{*}\left(\varphi_{i} u\right), \\
T_{r} u & =\sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1} \Psi_{i}^{*}\left(\left[\varphi_{i}, P\right] u\right) .
\end{aligned}$$

Proposition 6.2. Let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ satisfy the hypotheses of Theorem $i$.
\begin{itemize}
\item[(a)] If $|\delta+n / p-n / 2|<R$ and $1<p<\infty$, then $Q_{r}, S_{r}$, and $T_{r}$ extend to bounded maps as follows:
$$\begin{aligned}
& Q_{r}: H_{\delta}^{0, p}(M ; E) \rightarrow H_{\delta}^{m, p}(M ; E), \\
& S_{r}: H_{\delta}^{m, p}(M ; E) \rightarrow H_{\delta}^{m, p}(M ; E), \\
& T_{r}: H_{\delta}^{m-1, p}(M ; E) \rightarrow H_{\delta_{1}}^{m, p}(M ; E),
\end{aligned}$$
for any $\delta_{1}$ such that $\delta \leq \delta_{1} \leq \delta+1$ and $\left|\delta_{1}+n / p-n / 2\right|<R$. Moreover, there exists $r_{0}>0$ such that if $u \in H_{\delta}^{m, p}(M ; E)$ is supported in $A_{r}$ for $0<r<r_{0}$, then
$$Q_{r} P u=u+S_{r} u+T_{r} u$$
\end{itemize}
and
$$\left\|S_{r} u\right\|_{m, p, \delta} \leq C r\|u\|_{m, p, \delta}$$
for some constant $C$ independent of $r$ and $u$.
\begin{itemize}
\item[(b)] If $|\delta-n / 2|<R, 0<\alpha<1$, and $m+\alpha \leq l+\beta$, then $Q_{r}, S_{r}$, and $T_{r}$ extend to bounded maps as follows:
$$\begin{aligned}
& Q_{r}: C_{\delta}^{0, \alpha}(M ; E) \rightarrow C_{\delta}^{m, \alpha}(M ; E) \\
& S_{r}: C_{\delta}^{m, \alpha}(M ; E) \rightarrow C_{\delta}^{m, \alpha}(M ; E) \\
& T_{r}: C_{\delta}^{m-1, \alpha}(M ; E) \rightarrow C_{\delta_{1}}^{m, \alpha}(M ; E)
\end{aligned}$$
for any $\delta_{1}$ such that $\delta \leq \delta_{1} \leq \delta+1$ and $\left|\delta_{1}-n / 2\right|<R$. Moreover, there exists $r_{0}>0$ such that if $u \in C_{\delta}^{m, \alpha}(M ; E)$ is supported in $A_{r}$ for $0<r<r_{0}$, then
$$Q_{r} P u=u+S_{r} u+T_{r} u$$
and
$$\left\|S_{r} u\right\|_{m, \alpha, \delta} \leq C r\|u\|_{m, \alpha, \delta}$$
for some constant $C$ independent of $r$ and $u$.
\end{itemize}

Proof. The fact that $Q_{r} P u=u+S_{r} u+T_{r} u$ in $A_{r}$ is just a computation:
$$\begin{aligned}
Q_{r} P u= & \sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1} \Psi_{i}^{*}\left(\varphi_{i} P u\right) \\
= & \sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1} \Psi_{i}^{*}\left(P\left(\varphi_{i} u\right)\right)+\sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1} \Psi_{i}^{*}\left(\left[\varphi_{i}, P\right] u\right) \\
= & \sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1} P_{i} \Psi_{i}^{*}\left(\varphi_{i} u\right)+T_{r} u \\
= & \sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1} \breve{P} \Psi_{i}^{*}\left(\varphi_{i} u\right) \\
& \quad+\sum_{i} \varphi_{i}\left(\Psi_{i}^{-1}\right)^{*} \breve{P}^{-1}\left(P_{i}-\breve{P}\right) \Psi_{i}^{*}\left(\varphi_{i} u\right)+T_{r} u \\
= & u+S_{r} u+T_{r} u .
\end{aligned}$$

To check the mapping properties of $S_{r}$, we begin by observing that the fact that the functions $\varphi_{i}$ are uniformly bounded in $C_{(0)}^{l, \beta}(\bar{M}) \subset C^{l, \beta}(M)$ implies by Lemma itself for each $i$ and all $0 \leq j \leq l$, with norm bounded independently of $i$ and $r$. The fact that $S_{r}$ maps $H_{\delta}^{m, p}(M ; E)$ to itself then follows from Proposition 5.8 and (6.4), because the factors of $r^{\delta}$ and $r^{-\delta}$ introduced by $\Psi_{i}^{*}$ and its inverse cancel each other. Moreover, (6.5) implies (6.8!) whenever $u$ is supported in $A_{r}$, for some constant $C$ independent of $r$ and $u$.

The mapping properties of $T_{r}$ will follow from a similar argument once we show that the commutator $\left[\varphi_{i}, P\right]$ maps $H_{\delta}^{m-1, p}(M ; E)$ to $H_{\delta_{1}}^{m, p}(M ; E)$. Observe that each term in the coordinate expression for $\left[\varphi_{i}, P\right] u$ is a product of four factors: a constant, a $p$ th covariant derivative of $u$, a $q$ th covariant derivative of $\varphi_{i}$, and a polynomial in the components of $g$, $(\operatorname{det} g)^{-1 / 2}$, and their derivatives up through order $r$, with $p+q+r \leq m$ and $q \geq 1$. Since $\varphi_{i}$ is uniformly bounded in $C^{l, \beta}(M)$, the result follows. The argument for the Hölder case is identical. \(\square\)

Corollary 6.3. Let $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ satisfy the hypotheses of Theorem $i$.
\begin{itemize}
\item[(a)] If $|\delta+n / p-n / 2|<R,\left|\delta_{1}+n / p-n / 2\right|<R, \delta \leq \delta_{1} \leq \delta+1$, and $1<p<\infty$, then there exist $r>0$ and bounded operators
$$\begin{aligned}
& \widetilde{Q}: H_{\delta}^{0, p}(M ; E) \rightarrow H_{\delta}^{m, p}(M ; E) \\
& \widetilde{T}: H_{\delta}^{m-1, p}(M ; E) \rightarrow H_{\delta_{1}}^{m, p}(M ; E)
\end{aligned}$$
such that
$$\widetilde{Q} P u=u+\widetilde{T} u$$
whenever $u \in H_{\delta}^{m, p}(M ; E)$ is supported in $A_{r}$.
\item[(b)] If $|\delta-n / 2|<R,\left|\delta_{1}-n / 2\right|<R, \delta \leq \delta_{1} \leq \delta+1,0<\alpha<1$, and $m+\alpha \leq l+\beta$, then there exist $r>0$ and bounded operators
$$\begin{aligned}
& \widetilde{Q}: C_{\delta}^{0, \alpha}(M ; E) \rightarrow C_{\delta}^{m, \alpha}(M ; E) \\
& \widetilde{T}: C_{\delta}^{m-1, \alpha}(M ; E) \rightarrow C_{\delta_{1}}^{m, \alpha}(M ; E)
\end{aligned}$$
such that
$$\widetilde{Q} P u=u+\widetilde{T} u$$
whenever $u \in C_{\delta}^{m, \alpha}(M ; E)$ is supported in $A_{r}$.
\end{itemize}

Proof. Just choose $r$ small enough that (6.8!) holds with $C r<1 / 2$. It then follows that $\mathrm{Id}+S_{r}: H_{\delta}^{m, p}(M ; E) \rightarrow H_{\delta}^{m, p}(M ; E)$ has a bounded inverse. We just set
$$\begin{aligned}
\widetilde{Q} & =\left(\mathrm{Id}+S_{r}\right)^{-1} \circ Q_{r}, \\
\widetilde{T} & =\left(\mathrm{Id}+S_{r}\right)^{-1} \circ T_{r},
\end{aligned}$$
and then ( 6.71 ) follows immediately from (6.7). Once again, the argument for the Hölder case is identical. \(\square\)

Our first application of this parametrix construction is a significant strengthening of Lemma 4.8, giving improved decay for solutions to $P u=f$ when $u$ and $f$ are in appropriate spaces. We begin with a special case.

Lemma 6.4. Assume $P$ satisfies the hypotheses of Theorem
\begin{itemize}
\item[(a)] Suppose that $1<p<\infty, m \leq k \leq l,|\delta+n / p-n / 2|<R$, and $\mid \delta^{\prime}+$ $n / p-n / 2 \mid<R$. If $u \in H_{\delta}^{0, p}(M ; E)$ and $P u \in H_{\delta^{\prime}}^{k-m, p}(M ; E)$, then $u \in$ $H_{\delta^{\prime}}^{k, p}(M ; E)$.
\item[(b)] Suppose that $0<\alpha<1, m<k+\alpha \leq l+\beta,|\delta-n / 2|<R$, and $\left|\delta^{\prime}-n / 2\right|<R$. If $u \in C_{\delta}^{0,0}(M ; E)$ and $P u \in C_{\delta^{\prime}}^{k-m, \alpha}(M ; E)$, then $u \in C_{\delta^{\prime}}^{k, \alpha}(M ; E)$.
\end{itemize}

Proof. If $\delta^{\prime} \leq \delta$, the result is a trivial consequence of Lemmas 4.81 and 3.6 (bi), so assume $\delta^{\prime}>\delta$. Consider part ( ). By Lemma $u \in H_{\delta^{\prime}}^{0, p}(M ; E)$. For any small $r>0$, by means of a bump function we can write $u=u_{0}+u_{\infty}$, where $\operatorname{supp} u_{0}$ is compact and $\operatorname{supp} u_{\infty} \subset A_{r}$. Local elliptic regularity gives $u_{0} \in H_{\delta^{\prime}}^{k, p}(M ; E)$. Since $P u_{\infty}$ agrees with $P u$ off of a compact set,
$P u_{\infty} \in H_{\delta^{\prime}}^{0, p}(M ; E)$, so by Corollary $r$ is small enough,
$$\begin{aligned}
u_{\infty} & =\widetilde{Q} P u_{\infty}-\widetilde{T} u_{\infty} \\
& \in H_{\delta^{\prime}}^{m, p}(M ; E)+H_{\delta_{1}}^{1, p}(M ; E) \\
& \subset H_{\delta_{1}}^{0, p}(M ; E)
\end{aligned}$$
where $\delta_{1}=\min \left(\delta^{\prime}, \delta+1\right)$. Iterating this argument finitely many times, we conclude that $u_{\infty} \in H_{\delta^{\prime}}^{0, p}(M ; E)$. By Lemma ${ }^{\mathbf{3}}$. this implies that $u \in H_{\delta^{\prime}}^{k, p}(M ; E)$ as claimed. The argument for the Hölder case is the same. \(\square\)

Proposition 6.5. Suppose $P$ satisfies the hypotheses of Theorem ${ }_{1}^{-} \bar{C}$, and $u$ is either in $H_{\delta_{0}}^{0, p_{0}}(M ; E)$ for some $\left|\delta_{0}+n / p_{0}-n / 2\right|<R$ and $1<p_{0}<\infty$, or in $C_{\delta_{0}}^{0,0}(M ; E)$ for some $\left|\delta_{0}-n / 2\right|<R$.
\begin{itemize}
\item[(a)] If $P u \in H_{\delta}^{k-m, p}(M ; E)$ for $|\delta+n / p-n / 2|<R, 1<p<\infty$, and $m \leq k \leq l$, then $u \in H_{\delta}^{k, p}(M ; E)$.
\item[(b)] If $P u \in C_{\delta}^{k-m, \alpha}(M ; E)$ for $|\delta-n / 2|<R, 0<\alpha<1$, and $m<k+\alpha \leq l+\beta$, then $u \in C_{\delta}^{k, \alpha}(M ; E)$.
\end{itemize}

Proof. If $u \in C_{\delta_{0}}^{0,0}(M ; E)$ with $\left|\delta_{0}-n / 2\right|<R$, then $u \in H_{\delta}^{0, p}(M ; E)$ whenever $\delta+n / p<\delta_{0}$ by Lemma $\overline{3} . \overline{6}$. Since such $\delta$ and $p$ can be chosen that also satisfy $|\delta+n / p-n / 2|<R$, it suffices to prove the proposition under the hypothesis that $u \in H_{\delta_{0}}^{0, p_{0}}(M ; E)$ with $\left|\delta_{0}+n / p_{0}-n / 2\right|<R$. For the rest of the proof, we assume this.

First we treat case ( assume that $P u \in H_{\delta}^{k-m, p}(M ; E)$ with $|\delta+n / p-n / 2|<$ $R$, and let $\mathscr{P}$ be the following set:
$$\mathscr{P}=\left\{p^{\prime} \in(1, \infty): u \in H_{\delta^{\prime}}^{0, p^{\prime}}(M ; E) \text { for some } \delta^{\prime} \text { with }\left|\delta^{\prime}+n / p^{\prime}-n / 2\right|<R\right\} .$$
Clearly $p_{0} \in \mathscr{P}$ by hypothesis. We will show that $p \in \mathscr{P}$. It will then follow from Lemma 6.4 that $u \in H_{\delta}^{k, p}(M ; E)$, which will prove case ( ).

Claim 1: If $p_{1} \in \mathscr{P}$, then $\left(1, p_{1}\right] \subset \mathscr{P}$. To prove this, assume $p_{1} \in \mathscr{P}$ and $1<$ $p^{\prime}<p_{1}$. The fact that $p_{1} \in \mathscr{P}$ means that there is some $\delta_{1}$ with $\left|\delta_{1}+n / p_{1}-n / 2\right|<R$ such that $u \in H_{\delta_{1}}^{0, p_{1}}(M ; E)$. By Lemma $\delta^{\prime}, u \in H_{\delta^{\prime}}^{0, p^{\prime}}(M ; E)$ for any $\delta^{\prime}$ such that $\delta_{1}+n / p_{1}>\delta^{\prime}+n / p^{\prime}$. Choosing $\delta^{\prime}$ so that $\delta^{\prime}+n / p^{\prime}$ is sufficiently close to $\delta_{1}+n / p_{1}$, we can ensure that $\left|\delta^{\prime}+n / p^{\prime}-n / 2\right|<R$. This implies that $p^{\prime} \in \mathscr{P}$ as desired.

Claim 2: If $p_{1} \in \mathscr{P}$ and $p_{2}$ satisfies $p_{1}<p_{2} \leq p$ and
$$\frac{p_{2}}{p_{1}} \leq \min \left(\frac{n+2}{n+1}, 1+\frac{\varepsilon}{2 n}\right),$$
where
$$\varepsilon=\delta+\frac{n}{p}-\frac{n}{2}+R>0$$
then $p_{2} \in \mathscr{P}$. The assumption that $p_{1} \in \mathscr{P}$ means that $u \in H_{\delta_{1}}^{0, p_{1}}(M ; E)$ for some $\delta_{1}$ with $\left|\delta_{1}+n / p_{1}-n / 2\right|<R$. Choose $\delta^{\prime}$ satisfying
$$\delta+\frac{n}{p}>\delta^{\prime}+\frac{n}{p_{1}}>\delta+\frac{n}{p}-\frac{\varepsilon}{2} .$$
By virtue of the first inequality above, Lemma 3.6 implies that
$$P u \in H_{\delta}^{k-m, p}(M ; E) \subset H_{\delta^{\prime}}^{k-m, p_{1}}(M ; E) .$$

Since the two inequalities of (6.13) guarantee that $\left|\delta^{\prime}+n / p_{1}-n / 2\right|<R$, Lemma 6.4 shows that $u \in H_{\delta^{\prime}}^{k, p_{1}}(M ; E)$. Our restriction on $p_{2}$ guarantees that
$$\begin{aligned}
\frac{n+1}{p_{1}} & \leq \frac{n+2}{p_{2}} \\
& =\frac{n+1}{p_{2}}+\frac{1}{p_{2}} \\
& \leq \frac{n+1}{p_{2}}+k,
\end{aligned}$$
so Lemma $3.6\left(\frac{\mathrm{c}}{\mathrm{c}}\right)$ implies that $u \in H_{\delta^{\prime}}^{0, p_{2}}(M ; E)$. Now $(\overline{6}-\overline{12})$ implies that
$$\begin{aligned}
\frac{n}{p_{1}}-\frac{n}{p_{2}} & =\frac{n}{p_{2}}\left(\frac{p_{2}}{p_{1}}-1\right) \\
& \leq \frac{n}{p_{2}}\left(\frac{\varepsilon}{2 n}\right) \\
& <\frac{\varepsilon}{2} .
\end{aligned}$$
Therefore, using ( 6.13 ), we obtain
$$\begin{aligned}
\delta^{\prime}+\frac{n}{p_{2}}-\frac{n}{2} & =\left(\delta^{\prime}+\frac{n}{p_{1}}-\frac{n}{2}\right)-\left(\frac{n}{p_{1}}-\frac{n}{p_{2}}\right) \\
& >\left(\delta+\frac{n}{p}-\frac{n}{2}-\frac{\varepsilon}{2}\right)-\left(\frac{\varepsilon}{2}\right) \\
& =-R, \\
\delta^{\prime}+\frac{n}{p_{2}}-\frac{n}{2} & <\delta+\frac{n}{p}-\frac{n}{2} \\
& <R,
\end{aligned}$$
which proves that $p_{2} \in \mathscr{P}$ as claimed.
Claim 3: $p \in \mathscr{P}$. If $p \leq p_{0}$, this follows immediately from Claim 1 together with the obvious fact that $p_{0} \in \mathscr{P}$. Otherwise, just iterate Claim 2, starting with $p_{0} \in \mathscr{P}$. After finitely many iterations, we can conclude that $p \in \mathscr{P}$.

Finally we turn to case ( ibi ). Suppose $P u \in C_{\delta}^{k-m, \alpha}(M ; E)$ with $|\delta-n / 2|<R$, and choose $p^{\prime}$ large and $\delta^{\prime}$ close to $\delta$ satisfying
$$\delta>\delta^{\prime}+\frac{n}{p^{\prime}}$$
Then by Lemma $P u \in H_{\delta^{\prime}}^{k-m, p^{\prime}}(M ; E)$. If we choose $\delta^{\prime}+n / p^{\prime}$ sufficiently close to $\delta$, we have $\left|\delta^{\prime}+n / p^{\prime}-n / 2\right|<R$, and thus $u \in H_{\delta^{\prime}}^{k, p^{\prime}}(M ; E)$ by part (°a) above. If $p$ is also chosen large enough that $(n+1) / p^{\prime} \leq k-\alpha$, the Sobolev embedding theorem (Theorem . $\delta$ we will have $\left|\delta^{\prime}-n / 2\right|<R$. Then Lemma 6.4 implies $u \in C_{\delta}^{k, \alpha}(M ; E)$. \(\square\)

Now suppose $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ satisfies the hypotheses of Theorem By Lemma 4.10 estimate (1.4) implies that $P: H^{m, 2}(M ; E) \rightarrow H^{0,2}(M ; E)$ is Fredholm. Let $\bar{Z}=\operatorname{Ker} P \cap L^{2}(M ; E)$, which is equal to $\operatorname{Ker} P \cap H^{m, 2}(M ; E)$ by Lemma 4.8. Then $Z$ is finite-dimensional, and Proposition 6.5 shows that $Z \subset$
$H_{\delta}^{k, p}(M ; E)$ whenever $1<p<\infty, m \leq k \leq l$, and $|\delta+n / p-n / 2|<R$. In fact,
$$Z=\operatorname{Ker} P: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k-m, p}(M ; E),$$
because any $u \in \operatorname{Ker} P \cap H_{\delta}^{k, p}(M ; E)$ is also in $L^{2}(M ; E)$ by Proposition 6.5. Similarly, if $0<\alpha<1, m<k+\alpha \leq l+\beta$, and $|\delta-n / 2|<R$, then $Z=\operatorname{Ker} P: C_{\delta}^{k, \alpha}(M ; E) \rightarrow C_{\delta}^{k-m, \alpha}(M ; E)$.

Because of these observations, whenever $1<p<\infty, m \leq k \leq l$, and $\mid \delta+n / p-$ $n / 2 \mid<R$, we can define a subspace $Y_{\delta}^{k, p} \subset H_{\delta}^{k, p}(M ; E)$ by
$$Y_{\delta}^{k, p}=\left\{u \in H_{\delta}^{k, p}(M ; E):(u, v)=0 \text { for all } v \in Z\right\},$$
where $(u, v)$ represents the standard $L^{2}$ pairing. Since $Z \subset H_{-\delta}^{0, p^{*}}(M ; E)=$ $\left(H_{\delta}^{0, p}(M ; E)\right)^{*} \subset\left(H_{\delta}^{k, p}(M ; E)\right)^{*}$, it follows that $Y_{\delta}^{k, p}$ is a well-defined closed subspace of $H_{\delta}^{k, p}(M ; E)$. Similarly, if $0<\alpha<1, m<k+\alpha \leq l+\beta$, and $|\delta-n / 2|<R$, we can define
$$Y_{\delta}^{k, \alpha}=\left\{u \in C_{\delta}^{k, \alpha}(M ; E):(u, v)=0 \text { for all } v \in Z\right\},$$
since $C_{\delta}^{k, \alpha}(M ; E) \subset H_{\delta^{\prime}}^{0, p}(M ; E)$ for $\delta>\delta^{\prime}+n / p>n / 2-R$ implies $Z \subset$ $H_{-\delta^{\prime}}^{0, p^{*}}(M ; E)=\left(H_{\delta^{\prime}}^{0, p}(M ; E)\right)^{*} \subset\left(C_{\delta}^{k, \alpha}(M ; E)\right)^{*}$.

The next result is the main structure theorem for operators satisfying the hypotheses of Theorem ${ }^{\overline{1}} \mathbf{C}$ !

Theorem 6.6. Suppose $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ satisfies the hypotheses of Theorem
\begin{itemize}
\item[(a)] If $1<p<\infty, 0 \leq k \leq l$, and $|\delta+n / p-n / 2|<R$, there exist bounded operators $G, H: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k, p}(M ; E)$ such that $G\left(H_{\delta}^{k-m, p}(M ; E)\right) \subset$ $H_{\delta}^{k, p}(M ; E)$ for $k \geq m$, and
$$\begin{aligned}
Y_{\delta}^{k, p} & =\operatorname{Ker} H \\
Z & =\operatorname{Im} H \\
u & =G P u+H u \text { for } u \in H_{\delta}^{k, p}(M ; E), m \leq k \leq l, \\
u & =P G u+H u \text { for } u \in H_{\delta}^{k, p}(M ; E), 0 \leq k \leq l
\end{aligned}$$
\item[(b)] If $0<\alpha<1,0<k+\alpha \leq l+\beta$, and $|\delta-n / 2|<R$, there exist bounded operators $G, H: C_{\delta}^{k, \alpha}(M ; E) \rightarrow C_{\delta}^{k, \alpha}(M ; E)$ such that $G\left(C_{\delta}^{k-m, \alpha}(M ; E)\right) \subset$ $C_{\delta}^{k, \alpha}(M ; E)$ for $k \geq m$, and
$$\begin{aligned}
Y_{\delta}^{k, \alpha} & =\operatorname{Ker} H \\
Z & =\operatorname{Im} H \\
u & =G P u+H u \text { for } u \in C_{\delta}^{k, \alpha}(M ; E), m \leq k \leq l, \\
u & =P G u+H u \text { for } u \in C_{\delta}^{k, \alpha}(M ; E), 0 \leq k \leq l .
\end{aligned}$$
Proof. We begin with the Sobolev case, part ( ). First consider the special case $p=2, k=0$, and $\delta=0$ (in which case this is basically the standard construction of a partial inverse for a Fredholm operator on $L^{2}$ ). As noted above, the assumption of an $L^{2}$ estimate (1.4) near the boundary implies that $P: H_{0}^{m, 2}(M ; E) \rightarrow L^{2}(M ; E)$ is Fredholm by Lemma
\end{itemize}

By definition, $Y_{0}^{0,2} \subset L^{2}(M ; E)$ is precisely the orthogonal complement of $Z=$ $\operatorname{Ker} P$ in $L^{2}(M ; E)$, so we have an orthogonal direct sum decomposition $L^{2}(M ; E)=$ $Z \oplus Y_{0}^{0,2}$. Since $P$ is formally self-adjoint, any $u \in H^{m, 2}(M ; E)$ satisfies $(P u, v)=$ $(u, P v)=0$ for all $v \in Z$, so $P\left(H^{m, 2}(M ; E)\right) \subset Y_{0}^{0,2}$. On the other hand, if $v \in L^{2}(M ; E)$ is orthogonal to $P\left(H^{m, 2}(M ; E)\right)$, then for any smooth, compactly supported section $u$ of $E$ we have $(v, P u)=0$, so $v$ is a distributional solution to $P v=0$, which means $v \in Z$. This shows that $\left(P\left(H^{m, 2}(M ; E)\right)\right)^{\perp}=Z$, and since $P\left(H^{m, 2}(M ; E)\right)$ is closed in $L^{2}(M ; E)$ we have $P\left(H^{m, 2}(M ; E)\right)=Y_{0}^{0,2}$.

Now $P: Y_{0}^{m, 2} \rightarrow Y_{0}^{0,2}$ is bijective and bounded, so by the open mapping theorem it has a bounded inverse $\left(\left.P\right|_{Y_{0}^{m, 2}}\right)^{-1}: Y_{0}^{0,2} \rightarrow Y_{0}^{m, 2}$. Define $G: L^{2}(M ; E) \rightarrow$ $L^{2}(M ; E)$ by
$$G u= \begin{cases}\left(\left.P\right|_{Y_{0}^{m, 2}}\right)^{-1} u & u \in Y_{0}^{0,2} \\ 0 & u \in Z\end{cases}$$
and define $H: L^{2}(M ; E) \rightarrow L^{2}(M ; E)$ to be the orthogonal projection onto $Z$. Then $(6.17)$ and $(6.18)$ are immediate from the definition of $H$, and $(6.19)$ (for $u \in H^{m, 2}(M ; E)$ ) and (6.20) (for all $u$ ) follow by considering $u \in Y_{0}^{0,2}$ and $u \in Z$ separately.

Next consider the case of arbitrary $\delta$ satisfying $|\delta|<R$, still with $p=2$ and $k=$ 0 . If $\delta>0$ and $u \in H_{\delta}^{0,2}(M ; E) \subset L^{2}(M ; E)$, then $P G u=u-H u \in H_{\delta}^{0,2}(M ; E)$, so $G u \in H_{\delta}^{m, 2}(M ; E)$ by Lemma 6.4. Thus the restriction of $G$ to $H_{\delta}^{0,2}(M ; E)$ takes its values in $H_{\delta}^{m, 2}(M ; E)$, as does $H$ by $(\overline{6} . \overline{1})$. In this case, $(\overline{6} . \overline{1})-(\overline{6} . \overline{2})$ are satisfied because they are already satisfied on the bigger space $L^{2} \bar{M} ; E \overline{)}$ (or $H^{m, 2}(M ; E)$ in case of $\left.(\overline{6} . \overline{1} \overline{9})\right)$, and $Y_{\delta}^{0,2}=Y_{0}^{0,2} \cap H_{\delta}^{0,2}(M ; E)$.

On the other hand, if $\delta<0$, we can use the fact that $H_{\delta}^{0,2}(M ; E)=$ $\left(H_{-\delta}^{0,2}(M ; E)\right)^{*}$ to extend the definition of $G$ and $H$ to $H_{\delta}^{0,2}(M ; E)$ by duality: For any $u \in H_{\delta}^{0,2}(M ; E)$, let $G u$ and $H u$ be the elements of $H_{\delta}^{0,2}(M ; E)$ defined uniquely by
$$\begin{aligned}
& (G u, v)=(u, G v), \\
& (H u, v)=(u, H v)
\end{aligned}$$
for all $v \in H_{-\delta}^{0,2}(M ; E)$. In other words, $G, H: H_{\delta}^{0,2}(M ; E) \rightarrow H_{\delta}^{0,2}(M ; E)$ are defined to be the dual maps of $G, H: H_{-\delta}^{0,2}(M ; E) \rightarrow H_{-\delta}^{0,2}(M ; E)$. Since $H$ and $G$ are self-adjoint on $L^{2}(M ; E)$ ( $H$ because it is an orthogonal projection, and $G$ because $P$ is self-adjoint as an unbounded operator), these are indeed extensions of the original maps $G$ and $H$.

To see that these extended operators satisfy $(\overline{6} \cdot \overline{1} \overline{7})-(\overline{6} \cdot \overline{2} \overline{0})$, we observe that ( 6.26 ) implies that $H u=0$ for $u \in H_{\delta}^{0,2}(M ; E)$ exactly when $(u, v)=0$ for all $v$ in the image of $H: H_{-\delta}^{0,2}(M ; E) \rightarrow H_{-\delta}^{0,2}(M ; E)$; since this image is exactly $Z$, it follows that $\operatorname{Ker} H=Y_{\delta}^{0,2}$, which is $(\overline{6}-\overline{17})$. Since the restriction of $H$ to $Z \subset$ $L^{2}(M ; E) \subset H_{\delta}^{0,2}(M ; E)$ is the identity, it follows that $Z \subset \operatorname{Im} H$. On the other hand, for any $u \in H_{\delta}^{0,2}(M ; E)$, we have $(H u, P v)=(u, H P v)=0$ for all $v \in$ $C_{c}^{\infty}(M ; E) \subset H_{-\delta}^{0,2}(M ; E)$, which means that $H u$ is a weak solution to $P(H u)=0$. Thus $\operatorname{Im} H \subset \operatorname{Ker} P=Z$, which proves (6.18). Equations (6.19) and (6.20) then follow easily from our definitions by duality.

Next we generalize to $1<p<\infty$ and $|\delta+n / p-n / 2|<R$, still with $k=0$. If $p>2$, we can choose $\delta^{\prime}$ such that $\left|\delta^{\prime}\right|<R$ and $\delta+n / p>\delta^{\prime}+n / 2$, so that $H_{\delta}^{0, p}(M ; E) \subset H_{\delta^{\prime}}^{0,2}(M ; E)$. Arguing as above, we see that the restrictions of $G$ and $H$ map $H_{\delta}^{0, p}(M ; E)$ to $H_{\delta}^{m, p}(M ; E)$. On the other hand, for $p<2$, we can extend $G$ and $H$ to maps from $H_{\delta}^{0, p}(M ; E)=\left(H_{-\delta}^{0, p^{*}}(M ; E)\right)^{*}$ to itself by duality as above. In both cases (6.17)-(6.20) are satisfied, by restriction or duality as appropriate.

Now consider the general case of $H_{\delta}^{k, p}(M ; E)$ with $0 \leq k \leq l, 1<p<\infty$, and $|\delta+n / p-n / 2|<R$. Since $Z \subset H_{\delta}^{k, p}(M ; E)$, it is clear that $H$ restricts to a map of $H_{\delta}^{k, p}(M ; E)$ to itself. If $u \in H_{\delta}^{k, p}(M ; E) \subset H_{\delta}^{0, p}(M ; E)$ for $0 \leq k \leq l-m$, observe as above that $P G u=u-H u \in H_{\delta}^{k, p}(M ; E)$, so $G u \in H_{\delta}^{k+m, p}(M ; E)$ by Lemma 4.8. For $l-m \leq k \leq l$, we have $G\left(H_{\delta}^{k, p}(M ; E)\right) \subset G\left(H_{\delta}^{l-m, p}(M ; E)\right) \subset$ $H_{\delta}^{l, p}(M ; E) \subset H_{\delta}^{k, p}(M ; E)$. Thus in each case $G$ and $H$ restrict to maps from $H_{\delta}^{k, p}(M ; E)$ to itself, and properties $(\overline{6} . \overline{17})-(7.20)$ are satisfied by restriction.

Finally, consider case (b), and assume that $0<\alpha<1,0<k+\alpha \leq l+\beta$, and $|\delta-n / 2|<R$. We can choose $\delta^{\prime} \in \mathbb{R}$ satisfying $\left|\delta^{\prime}\right|<R$ and $\delta>\delta^{\prime}+n / 2$, so that $C_{\delta}^{k, \alpha}(M ; E) \subset H_{\delta^{\prime}}^{k, 2}(M ; E)$ and the results of part $\left(a_{1}^{-}\right)$apply to $H_{\delta^{\prime}}^{k, 2}(M ; E)$. Then the restrictions of $G$ and $H$ map $C_{\delta}^{k, \alpha}(M ; E)$ to itself by the same argument as above, and properties $(6.21)-(6.24)$ are automatically satisfied by restriction. \(\square\)

The next construction will be useful in proving that $P$ is not Fredholm outside the expected range of weights.

Lemma 6.7. Suppose $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ satisfies the hypotheses of Theorem $\bar{O}$, where $E$ is a bundle of tensors of weight $r$. Let $s_{0}$ be a characteristic exponent of $P$, and let $\delta_{0}=\operatorname{Re} s_{0}+r$. Given any compact subset $K \subset M$, there is an infinite-dimensional subspace $W \subset C_{\delta_{0}}^{l, \beta}(M ; E)$ such that every nonzero $w \in W$ has the following properties.
\begin{itemize}
\item[(a)] $\operatorname{supp} w \subset M \backslash K$.
\item[(b)] $P w \in C_{\delta_{0}+1}^{0,0}(M ; E)$.
\item[(c)] If $1<p<\infty$ and $\delta \geq \delta_{0}-n / p$, then $w \notin H_{\delta}^{0, p}(M ; E)$.
\end{itemize}

Proof. Let $\widehat{p} \in \partial M$ be arbitrary, and let $V$ be any neighborhood of $\widehat{p}$ in $\bar{M}$. Since the characteristic exponents are constant on $\partial M$ by Lemma 4.3 , there is a tensor $\bar{w}_{\widehat{p}} \in E_{\widehat{p}}$ such that $I_{s_{0}}(P) \bar{w}_{\widehat{p}}=0$. We can extend $\bar{w}_{\widehat{p}}$ to a $C^{l, \beta^{2}}$ tensor field $\bar{w}$ on a neighborhood of $\widehat{p}$ in $\partial M$, still satisfying $I_{s_{0}}(P) \bar{w}=0$, as follows. Shrinking $V$ if necessary, we can choose background coordinates on $V$, and for each $\widehat{q} \in V \cap \partial M$, let $A(\widehat{q})$ be the matrix of $I_{s_{0}}(P): E_{\widehat{q}} \rightarrow E_{\widehat{q}}$. By Lemma 4.2 , the matrix entries of $A(\widehat{q})$ are $C^{l, \beta}$ functions of $\widehat{q}$. If $\gamma$ is any smooth, positively-oriented closed curve in $\mathbb{C}$ whose interior contains 0 but no other eigenvalues of $A(\widehat{p})$, then the projection onto the kernel of $A(\widehat{q})$ can be written as $-1 /(2 \pi i) \int_{\gamma}(A(\widehat{q})-z \mathrm{Id})^{-1} d z$. (Here we use the fact that the eigenvalues of $A(\widehat{q})$ and their multiplicities are independent of $\widehat{q}$.) We define $\bar{w}$ to be the tensor field on $V \cap \partial M$ whose coordinate expression is
$$\bar{w}_{\widehat{q}}=\frac{-1}{2 \pi i} \int_{\gamma}(A(\widehat{q})-z \mathrm{Id})^{-1} \bar{w}_{\widehat{p}} d z$$
which is a $C^{l, \beta}$ tensor field along $\partial M$ satisfying $I_{s_{0}}(P) \bar{w}=0$. If we extend $\bar{w}$ arbitrarily to a $C^{l, \beta}$ tensor field on $V$, and let $w=\rho^{s_{0}} \varphi \bar{w}$ where $\varphi$ is any smooth
cutoff function that is positive at $\widehat{p}$ and supported in $V$, then $w \in C_{\delta}^{l, \beta}(M ; E)$, and
$$|P w|_{\bar{g}}=O\left(\rho^{\operatorname{Re} s_{0}+1}\right),$$
which implies
$$|P w|_{g}=O\left(\rho^{\delta_{0}+1}\right),$$
so $P w \in C_{\delta_{0}+1}^{0,0}(M ; E)$. On the other hand, $w \notin H_{\delta}^{0, p}(M ; E)$ for $\delta \geq \delta_{0}-n / p$ by Lemma 3.2.

Now choose countably many points $\widehat{p}_{i} \in \partial M$ and disjoint neighborhoods $V_{i}$ of $\widehat{p}_{i}$. For each $i$ we can construct $w_{i}$ as above with support in $V_{i}$, so the space spanned by $\left\{w_{i}\right\}$ is clearly infinite-dimensional. \(\square\)

Proof of Proposition 1 . It follows immediately from Lemma that $P$ is Fredholm as a map from $H^{m, 2}(M ; E)$ to $H^{0,2}(M ; E)$ if and only if $\bar{P}$ satisfies an estimate of the form (1.4). By Lemma $P$ as an unbounded operator on $L^{2}(M ; E)$ are the same as those of $P: H^{m, 2}(M ; E) \rightarrow$ $H^{0,2}(M ; E)$. The proposition follows. \(\square\)

Finally, we are in a position to prove our main Fredholm theorem, Theorem from the Introduction.

Proof of Theorem . We will prove parts $(\mathrm{p})$ and $(\overline{\mathrm{c}})$ together. The proof of sufficiency is identical for the Sobolev and Hölder cases, so we do only the Sobolev case.

Suppose $1<p<\infty, m \leq k \leq l$, and $|\delta+n / p-n / 2|<R$, and let $G, H: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k, p}(M ; E)$ be as in Theorem 6.6. We have already remarked that the kernel of $P: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k-m, p}(M ; E)$ is equal to $Z$, which is finitedimensional, and in fact is the same as the $L^{2}$ kernel. We will show that the range of $P$ is closed by showing that it is equal to $Y_{\delta}^{k-m, p}$. If $f=P u \in P\left(H_{\delta}^{k, p}(M ; E)\right)$, then clearly $(f, v)=(P u, v)=(u, P v)=0$ for all $v \in Z$, so $f \in Y_{\delta}^{k-m, p}$. On the other hand, if $f \in Y_{\delta}^{k-m, p}$, then $f=P G f+H f=P G f$ by ( 6.20 ) and $(\overline{6} . \overline{1})$, so $f \in P\left(H_{\delta}^{k, p}(M ; E)\right)$. Since every $f \in H_{\delta}^{k-m, p}(M ; E)$ can be written $f=P G f+H f$, where $P G f \in P\left(H_{\delta}^{k, p}(M ; E)\right)=Y_{\delta}^{k-m, p}$ and $H f \in Z$, it follows that $H_{\delta}^{k-m, p}(M ; E)=Y_{\delta}^{k-m, p} \oplus Z$. Therefore,
$$\frac{H_{\delta}^{k-m, p}(M ; E)}{P\left(H_{\delta}^{k, p}(M ; E)\right)}=\frac{Y_{\delta}^{k-m, p} \oplus Z}{Y_{\delta}^{k-m, p}} \cong Z,$$
which is finite-dimensional. This also shows that the cokernel and kernel of $P$ have the same dimension, so $P$ has index zero.

Next we will prove the necessity of the stated conditions on $\delta$. In fact, we will show that $P$ has infinite-dimensional kernel when $\delta$ is strictly below the Fredholm range, and infinite-dimensional cokernel when $\delta$ is strictly above; in the borderline case $C_{n / 2-R}^{k, \alpha}$, we will also show that $P$ has infinite-dimensional kernel, and in all other borderline cases, we will show that it fails to have closed range.

First we address the Hölder case below the Fredholm range. Assume $0<\alpha<1$, $m<k+\alpha \leq l+\beta$, and $\delta \leq n / 2-R$, and consider $P: C_{\delta}^{k, \alpha}(M ; E) \rightarrow C_{\delta}^{k-m, \alpha}(M ; E)$. We will prove that $P$ is not Fredholm in this case by showing that it has an infinitedimensional kernel.

The definition of the indicial radius $R$ and the symmetry of the characteristic exponents about $\operatorname{Re} s=n / 2-r$ imply that $P$ has a characteristic exponent $s_{0}$ with Re $s_{0}=n / 2-r-R$. Let $W$ be the subspace of $C_{n / 2-R}^{l, \beta}(M ; E)$ given by Lemma 6.7 for this characteristic exponent. (The compact set $K$ is irrelevant in this case.) For any $p>n, P(W) \subset C_{n / 2-R+1}^{0,0}(M ; E) \subset H_{n / 2-R}^{0, p}(M ; E)$ by Lemma 3.6. If we choose $p$ large enough, then $\delta=n / 2-R$ will satisfy $|\delta+n / p-n / 2|=|n / p-R|<R$, so there exist operators $G, H: H_{n / 2-R}^{0, p}(M ; E) \rightarrow H_{n / 2-R}^{0, p}(M ; E)$ satisfying $\left({ }^{1} 6{ }^{1} 1\right)-$ ( 6.20 ). Let $W_{0} \subset W$ be the linear subspace defined by
$$W_{0}=\{w \in W: H P w=0\} .$$
Because $H$ takes its values in the finite-dimensional space $Z$, the space $W_{0}$ is also infinite-dimensional. Note that for $w \in W_{0}, P w \in H_{n / 2-R}^{0, p}(M ; E)$ implies $G P w \in H_{n / 2-R}^{m, p}(M ; E) \subset C_{n / 2-R}^{0,0}(M ; E)$ by Lemma $3.6(c)$. Define $X: W_{0} \rightarrow$ $C_{n / 2-R}^{0,0}(M ; E)$ by $X w=w-G P w$. It follows from $(\overline{6} . \overline{2} \overline{0})$ that
$$P X w=P w-P G P w=H P w=0 \quad \text { for all } w \in W_{0} .$$
Therefore,
$$X\left(W_{0}\right) \subset \operatorname{Ker} P \cap C_{n / 2-R}^{0,0}(M ; E) \subset C_{n / 2-R}^{l, \beta}(M ; E)$$
by Lemma 4.8. Moreover, $X$ is injective because $X w=0$ implies $w=$ $G P w \in H_{n / 2-R}^{0, p-1}(M ; E)$, which implies that $w=0$ by assertion $(\bar{c})$ of Lemma 6.7. Thus we have shown that $X\left(W_{0}\right)$ is an infinite-dimensional subspace of $\operatorname{Ker} P \cap C_{n / 2-R}^{l, \beta}(M ; E)$. Since $C_{n / 2-R}^{l, \beta}(M ; E) \subset C_{\delta}^{k, \alpha}(M ; E)$ whenever $\delta \leq n / 2-R$ and $m<k+\alpha \leq l+\beta$, it follows that $P$ has infinite-dimensional kernel on $C_{\delta}^{k, \alpha}(M ; E)$ in all such cases.

Next consider the Sobolev case below the Fredholm range. When $1<p<\infty$, $m \leq k \leq l$, and $\delta<n / 2-n / p-R$, we have $C_{n / 2-R}^{l, \beta}(M ; E) \subset H_{\delta}^{k, p}(M ; E)$ by Lemma 3.6, so $P$ has infinite-dimensional kernel in $H_{\delta}^{k, p}(M ; E)$ as well.

Now we consider the exponents strictly above the Fredholm range, beginning with the Sobolev case. Suppose $1<p<\infty, m<k+\alpha \leq l+\beta$, and $\delta>n / 2-n / p+$ $R$. Recall that the dual space to $H_{\delta}^{0, p}$ is $H_{-\delta}^{0, p^{*}}$ (where $p^{*}$ is the conjugate exponent, $1 / p+1 / p^{*}=1$ ), acting by way of the standard $L^{2}$ pairing. Since $-\delta<n / 2-n / p^{*}-$ $R$, the argument above shows that $P^{*}=P: H_{-\delta}^{m, p^{*}}(M ; E) \rightarrow H_{-\delta}^{0, p^{*}}(M ; E)$ has infinite-dimensional kernel. Each element $v$ of the infinite-dimensional space $\operatorname{Ker} P \cap$ $H_{-\delta}^{m, p^{*}}(M ; E)$ thus defines a continuous linear functional on $H_{\delta}^{k-m, p}(M ; E)$ by $u \mapsto$ $(u, v)$, and each such linear functional annihilates $P\left(H_{\delta}^{k, p}(M ; E)\right)$ by Lemma It follows that the range of $P$ has infinite codimension in $H_{\delta}^{k-m, p}(M ; E)$.

For the Hölder case, suppose $0<\alpha<1, m<k+\alpha \leq l+\beta$, and $\delta>n / 2+R$. Choose $\delta^{\prime}$ close to $\delta$ and $p$ sufficiently large that $n / 2+R<\delta^{\prime}+n / p<\delta$. It follows that $-\delta^{\prime}<n / 2-n / p^{*}-R$, which implies as above that $P$ has an infinitedimensional kernel in $H_{-\delta^{\prime}}^{m, p^{*}}(M ; E)$. The fact that $C_{\delta}^{k-m, \alpha}(M ; E) \subset H_{\delta^{\prime}}^{0, p}(M ; E)$ implies that $H_{-\delta^{\prime}}^{0, p^{*}}(M ; E)=\left(H_{\delta^{\prime}}^{0, p}(M ; E)\right)^{*} \subset\left(C_{\delta}^{k-m, \alpha}(M ; E)\right)^{*}$. As above, each linear functional on $C_{\delta}^{k-m, \alpha}(M ; E)$ defined by an element of $\operatorname{Ker} P \cap H_{-\delta^{\prime}}^{m, p^{*}}(M ; E)$ annihilates the range of $P$, so once again we conclude that $P: C_{\delta}^{k, \alpha}(M ; E) \rightarrow$ $C_{\delta}^{k-m, \alpha}(M ; E)$ has infinite-dimensional cokernel.

Next we consider the borderline cases. The lower borderline Hölder case $\delta=$ $n / 2-R$ was already treated above, when we showed that $P$ has infinite-dimensional kernel in $C_{\delta}^{k, \alpha}(M ; E)$ whenever $\delta \leq n / 2-R$. In all remaining cases, we will show that $P$ does not have closed range.

We begin with the upper borderline Sobolev case, $H_{\delta_{p}}^{k, p}(M ; E)$ with $\delta_{p}=$ $n / 2-n / p+R$. Let us assume that $P: H_{\delta_{p}}^{k, p}(M ; E) \rightarrow H_{\delta_{p}}^{k-m, p}(M ; E)$ has closed range and derive a contradiction. If $\delta<\delta_{p}$ is chosen sufficiently close to $\delta_{p}$ that $|\delta-n / 2+n / p|<R$, the argument at the beginning of this proof showed that $\operatorname{Ker} P \cap H_{\delta}^{k, p}(M ; E)$ is finite-dimensional. Since $H_{\delta_{p}}^{k, p}(M ; E) \subset H_{\delta}^{k, p}(M ; E)$, we see that $\operatorname{Ker} P \cap H_{\delta_{p}}^{k, p}(M ; E)$ is finite-dimensional as well, so $P: H_{\delta_{p}}^{k, p}(M ; E) \rightarrow$ $H_{\delta_{p}}^{k-m, p}(M ; E)$ is semi-Fredholm. It follows from Lemma 4.10 that there is a compact set $K \subset M$ and a constant $C$ such that
$$\|u\|_{0, p, \delta_{p}} \leq C\|P u\|_{0, p, \delta_{p}}$$
when $u \in H_{\delta_{p}}^{m, p}(M ; E)$ is supported in $M \backslash K$.
By definition of $R, P$ has a characteristic exponent $s_{0}$ whose real part is equal to $n / 2-r+R$. Let $w$ be any element of the space $W$ defined in Lemma 6.7 corresponding to this characteristic exponent, with $\operatorname{supp} w \subset M \backslash K, w \notin H_{\delta_{p}}^{0, p}(M ; E)$, but $P w \in C_{n / 2+R+1}^{0,0}(M ; E) \subset H_{\delta_{p}}^{0, p}(M ; E)$. Let $\left\{\psi_{\varepsilon}\right\}$ be a family of cutoff functions as in Lemma 3.8 , and define $w_{\varepsilon}=\left(1-\psi_{\varepsilon}\right) w$. Note that for any $\varepsilon>0, w_{\varepsilon}$ is in $C_{\text {loc }}^{l, \beta}(M ; E)$ and compactly supported, so it is in $H_{\delta_{p}}^{k, p}(M ; E)$ for all $k \leq l$. Because $w \notin H_{\delta_{p}}^{0, p}(M ; E)$ and $w_{\varepsilon} \rightarrow w$ uniformly on compact sets as $\varepsilon \rightarrow 0$, we have $\left\|w_{\varepsilon}\right\|_{0, p, \delta_{p}} \rightarrow \infty$. On the other hand,
$$P w_{\varepsilon}=\left(1-\psi_{\varepsilon}\right) P w-\left[P, \psi_{\varepsilon}\right] w \in H_{\delta_{p}}^{0, p}(M ; E) .$$
If we can show that $\left\|P w_{\varepsilon}\right\|_{0, p, \delta_{p}}$ remains bounded as $\varepsilon \rightarrow 0$, we will have a contradiction to (6.29).

The fact that $P w \in H_{\delta_{p}}^{0, p}(M ; E)$ implies that $\left(1-\psi_{\varepsilon}\right) P w \rightarrow P w$ in the $H_{\delta_{p}}^{0, p}$ norm, so the first term in $(6.30)$ is clearly bounded in $H_{\delta_{p}}^{0, p}$. For the second term, observe that the commutator $\left[\nabla, \psi_{\varepsilon}\right] w=w \otimes d \psi_{\varepsilon}$ is an operator of order zero with coefficients that are uniformly bounded in $C^{l, \beta}(M)$ and supported on the set where $\varepsilon / 2 \leq \rho \leq \varepsilon$. It follows by induction that $\left[P, \psi_{\varepsilon}\right]$ is an operator of order $m-1$ with bounded coefficients supported in the same set, and therefore
$$\left\|\left[P, \psi_{\varepsilon}\right] w\right\|_{0, p, \delta_{p}}^{p} \leq C \sum_{0 \leq j \leq m-1} \int_{\varepsilon / 2 \leq \rho \leq \varepsilon}\left|\nabla^{j} w\right|^{p} d V_{g}$$
Since $\left|\nabla^{j} w\right|^{p}$ is integrable for $0 \leq j \leq m$, each integral above goes to zero as $\varepsilon \rightarrow 0$ by the dominated convergence theorem. This contradicts (6.29) and completes the proof that $P$ does not have closed range in this case.

Next consider the upper borderline Hölder case, $\delta=n / 2+R$. The argument is almost the same as in the Sobolev case, except in this case we have to set $w_{\varepsilon}=\psi_{\varepsilon} w$ and show that $\left\|P w_{\varepsilon}\right\|_{0, \alpha, n / 2+R} \rightarrow 0$ while $\left\|w_{\varepsilon}\right\|_{0, \alpha, n / 2+R}$ remains bounded below by a positive constant. The details are left to the reader.

The only case left is the lower borderline Sobolev case, $H_{\delta}^{k, p}(M ; E)$ with $\delta=$ $n / 2-n / p-R$. Since $-\delta=n / 2-n / p^{*}+R$, we showed above that $P: H_{-\delta}^{m, p^{*}}(M ; E) \rightarrow$
$H_{-\delta}^{0, p^{*}}(M ; E)$ does not have closed range, and thus neither does $P: H_{-\delta}^{0, p^{*}}(M ; E) \rightarrow$ $H_{-\delta}^{0, p^{*}}(M ; E)$ considered as an unbounded operator (since its domain is exactly $\left.H_{-\delta}^{m, p^{*}}(M ; E)\right)$. Since a closed, densely defined operator has closed range if and only if its adjoint does (cf. [4], Theorem IV.5.13]), this implies that $P: H_{\delta}^{0, p}(M ; E) \rightarrow$ $H_{\delta}^{0, p}(M ; E)$ does not have closed range, and then it follows from the regularity results of Proposition 6.5 that $P: H_{\delta}^{k, p}(M ; E) \rightarrow H_{\delta}^{k-m, p}(M ; E)$ does not either.

Finally, to prove part (a), just observe that $P$ being Fredholm on $L^{2}(M ; E)$ implies that it is Fredholm from $H_{0}^{m, 2}(M ; E)$ to $H_{0}^{0,2}(M ; E)$. By part $\left(\overline{b^{\prime}}\right)$, this in turn implies that $|0|<R$. \(\square\)

\section*{CHAPTER 7}

\section*{Laplace Operators}

In this chapter we specialize to Laplace operators. Throughout this chapter, $(M, g)$ will be a connected asymptotically hyperbolic $(n+1)$-manifold of class $C^{l, \beta}$ for some $l \geq 2$ and $0 \leq \beta<1$.

Let $E$ be a geometric tensor bundle of weight $r$ over $M$. A Laplace operator is a second-order geometric operator $P: C^{\infty}(M ; E) \rightarrow C^{\infty}(M ; E)$ that can be written in the form $P=\nabla^{*} \nabla+\mathscr{K}$, where $\nabla^{*} \nabla$ is the covariant Laplacian and $\mathscr{K}: E \rightarrow E$ is a bundle endomorphism (i.e., a differential operator of order zero). Note that our definition of geometric operators guarantees that the coefficients of $\mathscr{K}$ in any local frame are contractions of tensor products of $g, g^{-1}, d V_{g}$, and the curvature tensor.

To get sharp Fredholm results for a specific Laplace operator, we need to compute its indicial radius. In general, this is just a straightforward computation in coordinates near the boundary. Here are some of the results.

Lemma 7.1. The covariant Laplacian $\nabla^{*} \nabla$ on trace-free symmetric $r$-tensors has indicial radius
$$R=\sqrt{\frac{n^{2}}{4}+r} .$$

We will postpone the proof of this lemma until after Proposition 7.3 below. For the record, we also note the following, which is proved in [39, 40].

Lemma 7.2 (Mazzeo). The Laplace-Beltrami operator $\Delta=d d^{*}+d^{*} d$ on $q$ forms has the following indicial radius:
$$R= \begin{cases}\frac{n}{2}-q, & 0 \leq q \leq \frac{n}{2} \\ \frac{1}{2}, & q=\frac{n+1}{2} \\ q-\frac{n+2}{2}, & \frac{n+2}{2} \leq q \leq n+1\end{cases}$$

The following lemma greatly simplifies the computation of the indicial radius of a Laplace operator.

Proposition 7.3. Let $P=\nabla^{*} \nabla+\mathscr{K}$ be a Laplace operator acting on a geometric tensor bundle of weight $r$. For any $s \in \mathbb{C}$,
$$I_{s}(P)=I_{0}(P)+s(n-s-2 r) .$$

Proof. Since $I_{s}(\mathscr{K})=\left.\mathscr{K}\right|_{\partial M}$ is independent of $s$, we need only consider the case $P=\nabla^{*} \nabla$. As in the proof of Proposition 2.7 of [29], we compute (in
background coordinates)
$$\begin{aligned}
\rho_{; i j} & =\partial_{i} \partial_{j} \rho-\Gamma_{i j}^{k} \partial_{k} \rho \\
& =\rho^{-1}\left(2 \partial_{i} \rho \partial_{j} \rho-\bar{g}_{i j}\right)+o\left(\rho^{-1}\right) ; \\
\Delta\left(\rho^{s}\right) & =-s(s-1) \rho^{s-2} g^{j k} \rho_{; j} \rho_{; k}-s \rho^{s-1} \rho_{; k}^{k} \\
& =s(n-s) \rho^{s}+o\left(\rho^{s}\right) ; \\
|\nabla \rho|_{g}^{2} & =|d \rho|_{g}^{2} \\
& =\rho^{2}|d \rho|_{\bar{g}}^{2}=\rho^{2}+o\left(\rho^{2}\right) .
\end{aligned}$$
Therefore,
$$\begin{aligned}
\rho^{-s} \nabla^{*} \nabla\left(\rho^{s} \bar{u}\right)= & -\rho^{-s} \operatorname{Tr}_{g} \nabla^{2}\left(\rho^{s} \bar{u}\right) \\
= & -\rho^{-s} \operatorname{Tr}_{g} \nabla\left(s \rho^{s-1} \bar{u} \otimes \nabla \rho+\rho^{s} \nabla \bar{u}\right) \\
= & -\rho^{-s} \operatorname{Tr}_{g}\left(s(s-1) \rho^{s-2} \bar{u} \otimes \nabla \rho \otimes \nabla \rho+2 s \rho^{s-1} \nabla \bar{u} \otimes \nabla \rho\right. \\
& \left.+s \rho^{s-1} \bar{u} \otimes \nabla^{2} \rho+\rho^{s} \nabla^{2} \bar{u}\right) \\
= & -s(s-1) \rho^{-2}|\nabla \rho|_{g}^{2} \bar{u}-2 s \rho^{-1} \nabla \operatorname{grad} \rho \bar{u} \\
& +s \rho^{-1} \Delta \rho \bar{u}+\nabla^{*} \nabla \bar{u} \\
= & -s(s-1) \bar{u}-2 s \rho^{-1} \nabla_{\operatorname{grad} \rho} \bar{u}+s(n-1) \bar{u}+\nabla^{*} \nabla \bar{u}+o(1) .
\end{aligned}$$
To compute the second term above, assume $\bar{u}$ is a tensor of type $\binom{q}{p}$ with $q-p=r$, and let $D$ be the difference tensor $D=\nabla-\bar{\nabla}$. The components of $\nabla \bar{u}$ are
$$\begin{aligned}
\bar{u}_{j_{1} \ldots j_{q} k}^{i_{1} \ldots i_{p}} & =\partial_{k} \bar{u}_{j_{1} \ldots j_{q}}^{i_{1} \ldots i_{p}}+\sum_{s=1}^{p} \Gamma_{m k}^{i_{s}} \bar{u}_{j_{1} \ldots j_{q}}^{i_{1} \ldots m \ldots i_{p}}-\sum_{s=1}^{q} \Gamma_{j_{s} k}^{m} \bar{u}_{j_{1} \ldots i_{p} \ldots j_{q}}^{i_{1} \ldots i_{p}} \\
& =O(1)+\sum_{s=1}^{p} D_{m k}^{i_{s}} \bar{u}_{j_{1} \ldots j_{q}}^{i_{1} \ldots m \ldots i_{p}}-\sum_{s=1}^{q} D_{j_{s} k}^{m} \bar{u}_{j_{1} \ldots m \ldots j_{q}}^{i_{1} \ldots i_{p}} .
\end{aligned}$$
Let us introduce the shorthand notations $\rho_{i}=\partial_{i} \rho$ and $\bar{\rho}^{i}=\bar{g}^{i j} \partial_{j} \rho$. Using formula (3.1 ) for the components of $D$, together with the fact that $\rho_{i} \bar{\rho}^{i}=1+O(\rho)$, we obtain
$$\rho^{-1} g^{k l} \rho_{l} D_{j k}^{i}=-\bar{\rho}^{k}\left(\delta_{j}^{i} \rho_{k}+\delta_{k}^{i} \rho_{j}-\bar{g}_{j k} \bar{\rho}^{i}\right)=-\delta_{j}^{i}+O(\rho) .$$
Therefore,
$$\begin{aligned}
\rho^{-1}\left(\nabla_{\operatorname{grad} \rho} \bar{u}\right)_{j_{1} \ldots j_{q}}^{i_{1} \ldots i_{p}} & =\rho^{-1} g^{k l} \rho_{l} \bar{u}_{j_{1} \ldots j_{q} ; k}^{i_{1} \ldots i_{p}} \\
& =-\sum_{s=1}^{p} \delta_{m}^{i_{s}} \bar{u}_{j_{1} \ldots j_{q}}^{i_{1} \ldots m \ldots i_{p}}+\sum_{s=1}^{q} \delta_{j_{s}}^{m} \bar{u}_{j_{1} \ldots m \ldots j_{q}}^{i_{1} \ldots i_{p}}+O(\rho) \\
& =r \bar{u}_{j_{1} \ldots j_{q}}^{i_{1} \ldots i_{p}}+O(\rho) .
\end{aligned}$$
Inserting this back into (7.2), we obtain
$$\rho^{-s} \nabla^{*} \nabla\left(\rho^{s} \bar{u}\right)=s(n-s-2 r) \bar{u}+\nabla^{*} \nabla \bar{u}+o(1),$$
which implies the result. \(\square\)

Proof of Lemma By Prop. 7.31 to determine $I_{s}\left(\nabla^{*} \nabla\right)$ it suffices to compute $I_{0}\left(\nabla^{*} \nabla\right)$. The cases $r=0$ and $r=2$ follow from Corollary 2.8 and Lemma 2.9 of [29]. For the general case, suppose $r \geq 1$. Assuming $\bar{u}$ is trace-free, symmetric,
and smooth up to the boundary, and using the notation of the preceding proof, we compute
$$\begin{aligned}
\left(\nabla^{*} \nabla \bar{u}\right)_{i_{1} \ldots i_{r}} & =-\bar{u}_{i_{1} \ldots i_{r} ; l}^{l} \\
& =-g^{l m}\left(\partial_{m} \bar{u}_{i_{1} \ldots i_{r} ; l}-D_{l m}^{j} \bar{u}_{i_{1} \ldots i_{r} ; j}-\sum_{s=1}^{r} D_{i_{s} m}^{j} \bar{u}_{i_{1} \ldots j \ldots i_{r} ; l}\right)+O(\rho) .
\end{aligned}$$
As in the preceding proof, we have
$$\bar{u}_{i_{1} \ldots i_{r} ; l}=-\sum_{t=1}^{r} D_{i_{t} l}^{k} \bar{u}_{i_{1} \ldots k \ldots i_{r}}+O(1),$$
and therefore,
$$\begin{aligned}
\left(\nabla^{*} \nabla \bar{u}\right)_{i_{1} \ldots i_{r}}= & \sum_{t=1}^{r} g^{l m}\left(\partial_{m} D_{i_{t} l}^{k}\right) \bar{u}_{i_{1} \ldots k \ldots i_{r}}-\sum_{t=1}^{r} g^{l m} D_{l m}^{j} D_{i_{t} j}^{k} \bar{u}_{i_{1} \ldots k \ldots i_{r}} \\
& -\sum_{\substack{1 \leq s, t \leq r \\
s \neq t}} g^{l m} D_{i_{s} m}^{j} D_{i_{t} l}^{k} \bar{u}_{i_{1} \ldots j \ldots k \ldots i_{r}}-\sum_{s=1}^{r} g^{l m} D_{i_{s} m}^{j} D_{j l}^{k} \bar{u}_{i_{1} \ldots k \ldots i_{r}} \\
& +O(\rho)
\end{aligned}$$
Using (3.10) again, we compute
$$\begin{aligned}
g^{l m} \partial_{m} D_{i_{t} l}^{k} & =g^{l m} \rho^{-2} \rho_{m}\left(\delta_{i_{t}}^{k} \rho_{l}+\delta_{l}^{k} \rho_{i_{t}}-\bar{g}_{i_{t} l} \bar{\rho}^{k}\right)+O(\rho)=\delta_{i_{t}}^{k}+O(\rho) ; \\
g^{l m} D_{l m}^{j} D_{i_{t} j}^{k} & =-(n-1) \delta_{i_{t}}^{k}+O(\rho) ; \\
g^{l m} D_{i_{s} m}^{j} D_{i_{t} l}^{k} & =\delta_{i_{s}}^{j} \delta_{i_{t}}^{k}+\bar{g}^{j k} \rho_{i_{s}} \rho_{i_{t}}-\delta_{i_{s}}^{k} \rho_{i_{t}} \bar{\rho}^{j}-\delta_{i_{t}}^{j} \rho_{i_{s}} \bar{\rho}^{k}+\bar{g}_{i_{s} i_{t}} \bar{\rho}^{j} \bar{\rho}^{k}+O(\rho) ; \\
g^{l m} D_{i_{s} m}^{j} D_{j l}^{k} & =-(n-1) \rho_{i_{s}} \bar{\rho}^{k}+O(\rho) .
\end{aligned}$$
Inserting these above and using the fact that $\bar{u}$ is symmetric and trace-free, we obtain
$$\begin{aligned}
\left(\nabla^{*} \nabla \bar{u}\right)_{i_{1} \ldots i_{r}}= & r \bar{u}_{i_{1} \ldots i_{r}}+r(n-1) \bar{u}_{i_{1} \ldots i_{r}}-r(r-1) \bar{u}_{i_{1} \ldots i_{r}}-0 \\
& +(r-1) \sum_{t=1}^{r} \rho_{i_{t}} \bar{\rho}^{j} \bar{u}_{i_{1} \ldots j \ldots i_{r}}+(r-1) \sum_{s=1}^{r} \rho_{i_{s}} \bar{\rho}^{k} \bar{u}_{i_{1} \ldots k \ldots i_{r}} \\
& -\sum_{\substack{1 \leq s, t \leq r \\
s \neq t}} \bar{g}_{i_{s} i_{t}} \bar{\rho}^{j} \bar{\rho}^{k} \bar{u}_{i_{1} \ldots j \ldots k \ldots i_{r}}+(n-1) \sum_{s=1}^{r} \rho_{i_{s}} \bar{\rho}^{k} \bar{u}_{i_{1} \ldots k \ldots i_{r}}+O(\rho) \\
= & r(n+1-r) \bar{u}_{i_{1} \ldots i_{r}}+(2 r+n-3) \sum_{t=1}^{r} \rho_{i_{t}} \bar{\rho}^{j} \bar{u}_{i_{1} \ldots j \ldots i_{r}} \\
& -\sum_{\substack{1 \leq s, t \leq r \\
s \neq t}} \bar{g}_{i_{s} i_{t}} \bar{\rho}^{j} \bar{\rho}^{k} \bar{u}_{i_{1} \ldots j \ldots k \ldots i_{r}}+O(\rho) .
\end{aligned}$$

Suppose $s$ is any indicial root of $\nabla^{*} \nabla$ and $\bar{u}$ is a corresponding unit eigentensor. Using the formula above for $\nabla^{*} \nabla \bar{u}$ together with Proposition $\overline{7} .3$, and observing
that $\bar{u}$ is trace-free, we compute
$$\begin{aligned}
0 & =\left\langle\bar{u}, I_{s}\left(\nabla^{*} \nabla\right) \bar{u}\right\rangle_{\bar{g}} \\
& \left.=r(n+1-r)|\bar{u}|_{\bar{g}}^{2}+(2 r+n-3) \mid \operatorname{grad}_{\bar{g}} \rho\right\lrcorner\left.\bar{u}\right|_{\bar{g}} ^{2}+s(n-s-2 r)|\bar{u}|_{\bar{g}}^{2} \\
& \geq r(n+1-r)+s(n-s-2 r)
\end{aligned}$$
which implies that each indicial root satisfies
$$\left|s-\left(\frac{n}{2}-r\right)\right|^{2} \geq \frac{n^{2}}{4}+r .$$
It follows that the indicial radius of $\nabla^{*} \nabla$ is at least $\sqrt{n^{2} / 4+r}$.
On the other hand, if $\bar{u}$ is chosen so that $\left.\operatorname{grad}_{\bar{g}} \rho\right\lrcorner \bar{u}=0$ along $\partial M$ (i.e., $\bar{u}$ is purely tangential), we find that $I_{s}\left(\nabla^{*} \nabla\right) \bar{u}=(r(n+1-r)+s(n-s-2 r)) \bar{u}$. Solving $I_{s}\left(\nabla^{*} \nabla\right) \bar{u}=0$ for $s$, we find that two of the indicial roots of $\nabla^{*} \nabla$ are
$$s=\frac{n}{2}-r \pm \sqrt{\frac{n^{2}}{4}+r} .$$
This proves that the indicial radius is exactly $\sqrt{n^{2} / 4+r}$ as claimed. \(\square\)

Corollary 7.4. Let $P=\nabla^{*} \nabla+\mathscr{K}$ be a Laplace operator acting on a geometric tensor bundle of weight $r$, and suppose $P$ has indicial radius $R>0$. For $c \in \mathbb{R}$, the indicial radius $R^{\prime}$ of $P+c$ is positive if and only if $c+R^{2}>0$, in which case
$$R^{\prime}=\sqrt{c+R^{2}} .$$

Proof. Comparing the formulas given by Proposition 7.3 for $I_{s}(P)$ and $I_{n / 2-r}(P)$, we find that
$$I_{s}(P)=I_{n / 2-r}(P)-(s-n / 2+r)^{2} .$$
Observe that $I_{n / 2-r}(P)$ is self-adjoint by Proposition 4.4, so it has real eigenvalues. Now $s$ is a characteristic root of $P$ precisely when $s$ is a solution to the quadratic equation $(s-n / 2+r)^{2}=\mu$ for some eigenvalue $\mu$ of $I_{n / 2-r}(P)$. If some eigenvalue were nonpositive, this equation would have a root with real part equal to $n / 2-r$, which would imply $R=0$. Therefore, the assumption $R>0$ means that all of the eigenvalues $\left\{\mu_{i}\right\}$ of $I_{n / 2-r}(P)$ are strictly positive, and therefore the characteristic roots of $P$ are $s=n / 2-r \pm \sqrt{\mu_{i}}$, with $R^{2}=\min \left\{\mu_{i}\right\}$.

Since $I_{s}(P+c)=I_{s}(P)+c$, the characteristic roots of $P+c$ are $s=n / 2-$ $r \pm \sqrt{c+\mu_{i}}$, and the one with smallest real part greater than $n / 2-r$ is $s=$ $n / 2-r \pm \sqrt{c+R^{2}}$. Thus the indicial radius of $P+c$ is $\sqrt{c+R^{2}}$ as claimed. \(\square\)

Lemma 7.5. Let $\Delta_{\mathrm{L}}$ be the Lichnerowicz Laplacian, and let $c$ be a real constant. If $n^{2} / 4-2 n+c>0$, then the indicial radius of $\Delta_{\mathrm{L}}+c$ acting on symmetric 2-tensors is
$$R=\sqrt{\frac{n^{2}}{4}-2 n+c} .$$

Proof. Observe first that $\Delta_{\mathrm{L}}$ preserves the splitting of symmetric 2-tensors into trace and trace-free parts:
$$\Sigma^{2} M=\mathbb{R} g \oplus \Sigma_{0}^{2} M,$$
where $\Sigma^{2} M$ is the bundle of symmetric covariant 2-tensors, $\Sigma_{0}^{2} M$ is the subbundle of tensors that are trace-free with respect to $g$, and $\mathbb{R} g \subset \Sigma^{2} M$ is the real line bundle of multiples of $g$. On $\mathbb{R} g, \stackrel{\circ}{R} c(u g)={ }_{R} \stackrel{\circ}{R m}(u g)$, so $\Delta_{\mathrm{L}}$ acts as the ordinary Laplacian:
$$\Delta_{\mathrm{L}}(u g)=\left(\nabla^{*} \nabla u\right) g .$$
It follows from Lemma (or Lemma that the indicial radius of $\nabla^{*} \nabla$ on functions is $R=n / 2$, so the indicial radius of $\nabla^{*} \nabla+c$ is $\sqrt{n^{2} / 4+c}$, which is greater than (7.3). Therefore, it suffices to show that $\Delta_{\mathrm{L}}+c$ acting on trace-free symmetric 2-tensors has indicial radius given by (7.3).

The asymptotic formula (4.31) for the Riemann curvature tensor implies that the action of $\stackrel{\circ}{R m}$ and $\stackrel{\circ}{R} c$ on $\Sigma_{0}^{2} M$ near the boundary is given by
$$\begin{aligned}
\stackrel{\circ}{R c}(u) & =-n u+O(\rho|u|) ; \\
\stackrel{\circ}{R m}(u) & =u+O(\rho|u|) .
\end{aligned}$$
Thus the indicial radius of $\Delta_{\mathrm{L}}+c$ on $\Sigma_{0}^{2} M$ is the same as that of $\nabla^{*} \nabla-2 n-2+c$, which is $\sqrt{n^{2} / 4-2 n+c}$ by Lemma and Corollary \(\square\)

The main thing that needs to be checked in order to apply Theorem ${ }^{,} \mathbf{C}$ is the $L^{2}$ estimate (1.4). For some operators, an appropriate asymptotic estimate follows from an obvious integration by parts, such as $\nabla^{*} \nabla+c$ when $c$ is a positive constant:
$$\left(u, \nabla^{*} \nabla u+c u\right)=\|\nabla u\|^{2}+c\|u\|^{2} \geq c\|u\|^{2},$$
from which $\|u\| \leq c^{-1}\left\|\left(\nabla^{*} \nabla+c\right) u\right\|$ follows by the Cauchy-Schwartz inequality. However, when the zero-order term is not strictly positive, we need to work a bit harder.

As a warmup for the general $L^{2}$ estimates we will prove below, consider first the ordinary Laplacian $\Delta=d^{*} d$ on functions. The use of positive eigenfunctions, and more generally positive functions satisfying differential inequalities, is a common tool for estimating the lower bound of the spectrum of elliptic operators; see for example [20, 38, 43] and especially [56], where such functions play a central role. The following lemma was proved originally by Cheng and Yau [20, p. 345].

Lemma 7.6 (Cheng-Yau). Let $M$ be any Riemannian manifold. If there exists a positive, locally $C^{2}$ function $\varphi$ on $M$ such that $\Delta \varphi / \varphi \geq \lambda$, then
$$(u, \Delta u) \geq \lambda\|u\|^{2}$$
for all smooth compactly supported functions $u$.
The proof of this lemma in uses the maximum principle. Here is a simple proof based on integration by parts, which serves to motivate the somewhat more delicate estimates below.

Proof. Let $u \in C_{c}^{\infty}(M)$. The divergence theorem gives
$$\begin{aligned}
0 & =\int_{M} d^{*}\left(u^{2} \varphi^{-1} d \varphi\right) d V_{g} \\
& =\int_{M}\left(-2 u \varphi^{-1}\langle d u, d \varphi\rangle_{g}+u^{2} \varphi^{-2}|d \varphi|^{2}+u^{2} \varphi^{-1} \Delta \varphi\right) d V_{g}
\end{aligned}$$

Thus
$$\begin{aligned}
0 & \leq \int_{M}\left|\varphi d\left(\varphi^{-1} u\right)\right|^{2} d V_{g} \\
& =\int_{M}\left|d u-u \varphi^{-1} d \varphi\right|^{2} d V_{g} \\
& =\int_{M}\left(|d u|^{2}-2 u \varphi^{-1}\langle d u, d \varphi\rangle_{g}+u^{2} \varphi^{-2}|d \varphi|^{2}\right) d V_{g} \\
& =\int_{M}\left(u \Delta u-u^{2} \varphi^{-1} \Delta \varphi\right) d V_{g} \leq \int_{M}\left(u \Delta u-\lambda u^{2}\right) d V_{g}
\end{aligned}$$
which is equivalent to (7.5) \(\square\)

Lemma 7.6 is a global result; but for proving asymptotic estimates, we need only find a function $\varphi$ that satisfies $\Delta \varphi / \varphi \geq \lambda$ on the complement of a compact set. In particular, on an asymptotically hyperbolic $(n+1)$-manifold, asymptotic computations show that $\Delta\left(\rho^{n / 2}\right) / \rho^{n / 2}$ can be made arbitrarily close to $n^{2} / 4$ near $\partial M$. From this it will follow, for example, that $\Delta-\lambda$ on functions satisfies the hypotheses of Theorem for any constant $\lambda<n^{2} / 4$.

It is interesting to note that this simple estimate immediately yields a (rather crude) estimate for the covariant Laplacian on tensor fields.

Lemma 7.7. If (7.5) holds for smooth functions compactly supported in some open set $U \subset M$, then for any smooth tensor field $w$ compactly supported in $U$, we have
$$\left(w, \nabla^{*} \nabla w\right) \geq \lambda\|w\|^{2}$$
with the same constant $\lambda$.
Proof. Inequality (7.5) implies
$$\lambda\|u\|^{2} \leq\|\nabla u\|^{2},$$
which extends continuously to compactly supported functions in $H^{1,2}(U)$. If $w$ is a smooth, compactly supported tensor field, the function $|w|$ is Lipschitz, hence in $H^{1,2}(U)$. Kato's inequality says that $|\nabla| w\left|\left|\leq|\nabla w|\right.\right.$ almost everywhere (see ${ }^{1} \mathbf{1 0}$ Prop. 3.49], where this is proved for scalar functions; the proof extends easily to tensors). Therefore
$$\lambda\|w\|^{2} \leq\|\nabla|w|\|^{2} \leq\|\nabla w\|^{2}=\left(w, \nabla^{*} \nabla w\right) .$$ \(\square\)

A version of this argument (using the maximum principle instead of integration by parts) was used implicitly in our proof that the linearized Einstein operator is invertible on weighted Hölder spaces over hyperbolic space [29]. Unfortunately, as we noted there, this estimate was not sharp, and led to less-than-optimal Fredholm results for tensors. For the application to Einstein metrics in this monograph, we no longer need a sharp asymptotic estimate, because of the sharp Fredholm theorems of the preceding chapter. However, with other applications in mind, it is useful to see how far the asymptotic estimates can be pushed.

The key to finding improved asymptotic estimates on tensors turns out to be to consider $r$-tensor fields as $(r-1)$-tensor-valued 1 -forms. Therefore we must make a short digression to discuss the properties of tensor-valued differential forms.

Let $E$ be any geometric tensor bundle over $M$, and let $\Lambda^{q} E:=E \otimes \Lambda^{q} M$ denote the bundle of $E$-valued $q$-forms on $M$. Let $D: C^{\infty}\left(M ; \Lambda^{q} E\right) \rightarrow C^{\infty}\left(M ; \Lambda^{q+1} E\right)$ denote the exterior covariant differential on $E$-valued forms, defined by
$$D(\sigma \otimes \alpha)=\nabla \sigma \wedge \alpha+\sigma \otimes d \alpha,$$
for $\alpha \in C^{\infty}\left(M ; \Lambda^{q} M\right)$ and $\sigma \in C^{\infty}(M ; E)$. (The wedge product above is computed by wedging the 1 -form component of $\nabla \sigma$ with $\alpha$ to yield a section of $\Lambda^{q+1} E$.) We will study the covariant Laplace-Beltrami operator on $E$-valued forms, defined by $\Delta=D D^{*}+D^{*} D$, where $D^{*}$ is the formal adjoint of $D$.

For a scalar 1-form $\alpha$, we let $\alpha \vee: \Lambda^{q+1} E \rightarrow \Lambda^{q} E$ denote the (pointwise) adjoint of the operator $\alpha \wedge: \Lambda^{q} E \rightarrow \Lambda^{q+1} E$ with respect to $g$, so that $\langle\alpha \wedge \omega, \eta\rangle_{g}=$ $\langle\omega, \alpha \vee \eta\rangle_{g}$. In particular, if $\beta$ is also a scalar 1-form, then $\alpha \vee \beta=\langle\alpha, \beta\rangle_{g}$.

For any function $u \in C^{2}(M)$, let $H(u)$ denote the covariant Hessian of $u$ acting as bundle endomorphism $H(u): \Lambda^{1} M \rightarrow \Lambda^{1} M$, and extended to $\Lambda^{q} M$ as a derivation. In terms of any orthonormal basis,
$$H(u) \omega=u_{; i j} e^{i} \wedge\left(e^{j} \vee \omega\right)$$
(where $u_{; i j}$ are the components of $\nabla^{2} u$ ), since both sides are derivations that agree on $\Lambda^{1} M$. We extend this endomorphism to $\Lambda^{q} E$ by letting it act on the differential form component alone.

Lemma 7.8. Suppose $\alpha$ and $\beta$ are scalar 1 -forms, $\omega$ is an $E$-valued $q$-form, and $u$ is a function. For any local orthonormal frame $\left\{e_{j}\right\}$ for $T M$ and dual coframe $\left\{e^{j}\right\}$, we have the following facts:
\begin{itemize}
\item[(a)] $D \omega=e^{j} \wedge \nabla_{e_{j}} \omega$.
\item[(b)] $D^{*} \omega=-e^{j} \vee \nabla_{e_{j}} \omega$.
\item[(c)] $D(u \omega)=u D \omega+d u \wedge \omega$.
\item[(d)] $D^{*}(u \omega)=u D^{*} \omega-d u \vee \omega$.
\item[(e)] $\alpha \wedge(\beta \vee \omega)+\beta \vee(\alpha \wedge \omega)=\langle\alpha, \beta\rangle_{g} \omega$.
\item[(f)] $D(d u \vee \omega)=-d u \vee D \omega+H(u) \omega+\nabla_{\operatorname{grad} u} \omega$.
\item[(g)] $D^{*}(d u \wedge \omega)=-d u \wedge D^{*} \omega+H(u) \omega-\nabla_{\operatorname{grad} u} \omega+(\Delta u) \omega$.
\end{itemize}

Proof. Parts (a) through (el ) are standard, and can be found, for example, in [60, Ch. 2 and Section 6.1]. For ( ), choose a point $p \in M$ and a frame $\left\{e_{j}\right\}$ such that $\nabla e_{j}=\nabla e^{j}=0$ at $p$. Then, computing at $p$ and using (a), and (7.6), we have
$$\begin{aligned}
D(d u \vee \omega) & =e^{j} \wedge \nabla_{j}\left(u_{; k} e^{k} \vee \omega\right) \\
& =e^{j} \wedge\left(u_{; j k} e^{k} \vee \omega\right)+u_{; k} e^{j} \wedge\left(e^{k} \vee \nabla_{j} \omega\right) \\
& =H(u) \omega+u_{; k} g^{j k} \nabla_{j} \omega-u_{; k} e^{k} \vee\left(e^{j} \wedge \nabla_{j} \omega\right) \\
& =H(u) \omega+\nabla_{\operatorname{grad} u} \omega-d u \vee D \omega .
\end{aligned}$$
The computation for $(\mathrm{g})$ is similar. \(\square\)

The integral formula in the next lemma, a tensor analogue of (7.5), is the key to proving sharp asymptotic $L^{2}$ estimates. It unifies and generalizes Bochner-type formulas that have been used in various settings, such as the weighted Bochner formula introduced by Witten [58] to prove the Morse inequalities, and a closely related formula for scalar differential forms used by Donnelly and Xavier [25] to analyze the spectrum of the scalar Laplace-Beltrami operator on negatively-curved
manifolds, and by Lars Andersson for the same operator on asymptotically hyperbolic manifolds. Later Andersson and Chruściel [8] used the formula presented here (based on an early draft of the present monograph) to obtain Fredholm results for the "vector Laplacian" $L^{*} L$ that arises in the constraint equations of general relativity (see the Introduction).

Lemma 7.9. For any smooth, compactly supported section $\omega$ of $\Lambda^{q} E$, and any positive $C^{2}$ function $\varphi$ on $M$, the following integral formula holds:
$$\begin{aligned}
(\omega, \Delta \omega)= & \int_{M} \varphi^{-1} \Delta \varphi|\omega|_{g}^{2}+2\langle\omega, H(\log \varphi) \omega\rangle_{g} \\
& \quad+\left|\varphi D\left(\varphi^{-1} \omega\right)\right|_{g}^{2}+\left|\varphi^{-1} D^{*}(\varphi \omega)\right|_{g}^{2} d V_{g} \\
\geq & \int_{M}\left\langle\omega,\left(\varphi^{-1} \Delta \varphi+2 H(\log \varphi)\right) \omega\right\rangle_{g} d V_{g}
\end{aligned}$$