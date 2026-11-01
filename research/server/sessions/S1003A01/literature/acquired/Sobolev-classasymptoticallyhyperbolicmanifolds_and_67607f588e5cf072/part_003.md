---
retention_scope: session
part: 3
total_parts: 7
---

[Part 3/7 of: Sobolev-classasymptoticallyhyperbolicmanifolds and]

As a consequence, if $\Theta \in \mathscr{H}^{s, p ; m}(M)$ then
$$\begin{aligned}
\mathrm{R}\left[\Theta^{-2} g\right]-\breve{\mathrm{R}}_{n} & =R\left[(\Theta \rho)^{-2} \bar{g}\right]-\breve{\mathrm{R}}_{n} \\
& =\breve{\mathrm{R}}_{n}\left(|d(\Theta \rho)|_{\bar{g}}^{2}-1\right)+2(n-1)(\Theta \rho) \Delta_{\bar{g}} \Theta \rho+(\Theta \rho)^{2} \mathrm{R}[\bar{g}] .
\end{aligned}$$
We suppose that $\Theta$ is of the form $1+\rho^{k} u$, with $u \in \mathscr{H}^{\infty, p ; m-k}(M) \cap H_{\sigma-n / p}^{\infty, p}(M)$ to be chosen later, and gather a number of results to use when analyzing the terms of (6.22). From Lemma 4.3 and Proposition 4.6 we find
$$\begin{aligned}
\rho^{k} u & \in \mathscr{H}^{\infty, p ; m}(M) \cap H_{k+\sigma-n / p}^{\infty, p}(M) \cap X_{\alpha}^{\infty}(M), \\
\rho^{k+1} \hat{\nabla} u & \in \mathscr{H}^{\infty, p ; m}(M) \cap H_{k+2-n / p}^{\infty, p}(M) \cap X_{1}^{\infty}(M),
\end{aligned}$$
where in the second line we used also that $k<m$; note that the condition $\alpha \leq 1 / 2$ handles the boundary case in Proposition 4.6. In particular, $\hat{\nabla} u \in H_{1-n / p}^{\infty, p}(M)$ and therefore $\hat{\nabla}^{2} u \in H_{1-n / p}^{\infty, p}(M)$ as well. Proposition 4.6 also implies that $\bar{g}^{-1} \in X_{-2}^{s, p}(M)$ and $\hat{\nabla} \bar{g} \in X_{-1}^{s-1, p}(M)$. We use these latter facts to analyze $\Delta_{\bar{g}}(\Theta \rho)$, which is comprised of terms that are contractions of $\bar{g}^{-1} \otimes \hat{\nabla}^{2}(\Theta \rho)$ and $\bar{g}^{-1} \otimes \bar{g}^{-1} \otimes \hat{\nabla} \bar{g} \otimes \hat{\nabla}(\Theta \rho)$. Finally, from Lemmas 5.2-5.4 we have
$$|d \rho|_{\bar{g}}^{2}-1 \in X_{\alpha}^{s, p}(M), \quad \rho \Delta_{\bar{g}} \rho \in X_{\alpha}^{s-1, p}(M), \quad \rho^{2} \mathrm{R}[\bar{g}] \in X_{\alpha}^{s-2, p}(M) .$$
A lengthy computation using these facts and Proposition 3.11 results in
$$\begin{aligned}
|d(\Theta \rho)|_{\bar{g}}^{2} & =|d \rho|^{2}+2(k+1) \rho^{k} u+H_{k-n / p+\min (1, \sigma+\alpha)}^{s, p}(M), \\
(\Theta \rho) \Delta_{\bar{g}}(\Theta \rho) & =\rho \Delta_{\bar{g}} \rho+k(k+1) \rho^{k} u+H_{k-n / p+\min (1, \sigma+\alpha)}^{s-1, p}(M), \\
(\Theta \rho)^{2} \mathrm{R}[\bar{g}] & =\rho^{2} \mathrm{R}[\bar{g}]+H_{k-n / p+\sigma+\alpha}^{s-2, p}(M) .
\end{aligned}$$
Hence, from (6.21) and (6.20) we find
$$\begin{aligned}
\mathrm{R}\left[\Theta^{-2} g\right]-\breve{\mathrm{R}}_{n} & =\mathrm{R}[g]-\breve{\mathrm{R}}_{n}+2(k+1)(n-1)(k-n) \rho^{k} u+H_{k-n / p+\min (1, \sigma+\alpha)}^{s-2, p}(M), \\
& =\rho^{k}(\tau+2(k+1)(n-1)(k-n) u)+H_{k-n / p+\min (1, \sigma+\alpha)}^{s-2, p}(M) .
\end{aligned}$$
Since $k<m \leq n$, the coefficient on $u$ above does not vanish, and we can take
$$u=\frac{\tau}{2(k+1)(n-1)(n-k)}$$
in a neighborhood of $\partial M$, small enough to ensure $\Theta>0$, and obtain
$$\mathrm{R}\left[\Theta^{-2} g\right]-\breve{\mathrm{R}}_{n} \in H_{k-n / p+\min (1, \sigma+\alpha)}^{s-2, p}(M)$$
as claimed. \(\square\)
6.1.2. Candidate solution at low regularity. Suppose $g$ is a metric of class $\mathscr{H}^{s, p ; m}$ with $s \geq$ $m>n / p$. Hence $\rho^{2} g \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,2} M\right) \subset \mathscr{H}^{m, p ; m}\left(M ; T^{0,2} M\right)=H^{m, p}\left(\bar{M} ; T^{0,2} M\right)$. Choose $q \geq p$ such that
$$\frac{1}{p}-\frac{m}{n} \leq \frac{1}{q}-\frac{1}{n}<0 .$$
Sobolev embedding on $\bar{M}$ implies that $H^{m, p}\left(\bar{M} ; T^{0,2} M\right) \subset H^{1, q}\left(\bar{M} ; T^{0,2} M\right)$ and therefore $g$ is asymptotically hyperbolic of class $\mathscr{H}^{1, q ; 1}$. Throughout this stage we work with metrics at this level of regularity with the aim of finding a low-regularity solution of equation (6.18). In the process we make extensive use of the following maximum principle, which can be proved with straightforward modifications of the techniques of Lemmas 5.2 and 5.3 of [Max06].

Lemma 6.5. Let $g$ be asymptotically hyperbolic of class $\mathscr{H}^{1, q ; 1}$ or of class $\mathscr{X}^{1, q ; 1}$ with $q>n$.
\begin{itemize}
\item[(a)] Suppose $V \in X_{0}^{-1, q}(M ; \mathbb{R})$ with $V \geq 0$. If $u \in X_{\alpha}^{1, q}(M ; \mathbb{R})$ for some $\alpha>0$ and
$$-\Delta_{g} u+V u \geq 0$$
then $u \geq 0$.
\item[(b)] Suppose $V \in H_{\mathrm{loc}}^{-1, q}(M ; \mathbb{R})$ and that $u \in H_{\mathrm{loc}}^{1, q}(M ; \mathbb{R})$, is nonnegative, and satisfies
$$-\Delta_{g} u+V u \geq 0 .$$
If $u=0$ at some point then $u \equiv 0$.
\end{itemize}
The scalar curvature of a metric of class $\mathscr{H}^{1, q ; 1}$ only lies in $H_{\text {loc }}^{-1, q}(M ; \mathbb{R})$. The following lemma shows that we can conformally transform to a metric with continuous scalar curvature that also satisfies a bound from above needed for our subsequent barrier construction.

Lemma 6.6. Suppose $g$ is asymptotically hyperbolic of class $\mathscr{H}^{1, q ; 1}$ for some $q>n$. There exists $u \in H_{1-n / q}^{1, q}(M ; \mathbb{R})$ such that $\Theta=1+u>0$ and such that $\Theta^{q_{n}-2} g$ is asymptotically hyperbolic of class $\mathscr{H}^{1, q ; 1}$ with
$$\begin{aligned}
& \mathrm{R}\left[\Theta^{q_{n}-2} g\right]-\breve{\mathrm{R}}_{n} \in H_{1-n / q}^{1, q}(M ; \mathbb{R}), \\
& \mathrm{R}\left[\Theta^{q_{n}-2} g\right] \leq \breve{\mathrm{R}}_{n} .
\end{aligned}$$
Proof. The proof proceeds by two conformal transformations. The first attains the regularity criterion, and the second lowers the scalar curvature.

For ease of notation, set $\alpha=1-n / q$. Since $\alpha$ lies in the Fredholm range defined by inequality (6.14), Proposition 6.3 implies $\Delta_{g}: H_{\alpha}^{1, q}(M) \rightarrow H_{\alpha}^{-1, q}(M)$ is an isomorphism. Proposition 5.1 and Lemma 4.3(a) imply $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{\alpha}^{-1, q}(M)$.
Since $\alpha>0$, Proposition 3.11 implies that multiplication $H_{\alpha}^{-1, q}(M) \times H_{\alpha}^{1, q}(M) \rightarrow H_{\alpha}^{-1, q}(M)$ is bilinear and continuous. Thus, using Proposition A.5, we may choose $W \in H_{\alpha}^{1, q}(M)$ such
that $V_{1}=\mathrm{R}[g]-\breve{\mathrm{R}}_{n}-W$ is sufficiently small in $H_{\alpha}^{-1, q}(M)$ so that
$$-a_{n} \Delta_{g}+V_{1}: H_{\alpha}^{1, q}(M) \rightarrow H_{\alpha}^{-1, q}(M)$$
remains an isomorphism.
For each $\eta \in[0,1]$ let $u_{\eta} \in H_{\alpha}^{1, q}(M)$ be the unique solution of
$$-a_{n} \Delta_{g} u_{\eta}+\eta V_{1} u_{\eta}=-\eta V_{1} .$$
We claim that each $u_{\eta}$ satisfies $1+u_{\eta}>0$. Indeed, the map $\eta \mapsto u_{\eta}$ is continuous into $H_{\alpha}^{1, q}(M) \subset C_{\alpha}^{0, \alpha}(M)$. Since $u_{0} \equiv 0$, if the claim were false there would be some first value of $\eta$ such that $1+u_{\eta} \geq 0$ and $1+u_{\eta}=0$ at some point. Since $-a_{n} \Delta\left(1+u_{\eta}\right)+V_{1}\left(1+u_{\eta}\right)=0$, Lemma 6.5(b) implies $1+u_{\eta} \equiv 0$. But this is impossible since $\alpha>0$ and therefore since $1+u_{\eta} \rightarrow 1$ at $\partial M$.
Let $\Theta_{1}=1+u_{1}$. Lemma 6.1 implies $g_{1}=\Theta_{1}^{q_{n}-2} g$ is asympotically hyperbolic of class $\mathscr{H}^{1, q ; 1}$. From equation (6.2) it follows that
$$\mathrm{R}\left[g_{1}\right]=\Theta_{1}^{2-q_{n}}\left(\mathrm{R}[g]-V_{1}\right)=\Theta_{1}^{2-q_{n}}\left(\breve{\mathrm{R}}_{n}+W\right) .$$
Thus Proposition 3.19, and its following comments, applied to $F(x)=(1+x)^{2-q_{n}}-1$ imply
$$\mathrm{R}\left[g_{1}\right]-\breve{\mathrm{R}}_{n} \in H_{\alpha}^{1, q}(M) .$$
This completes the first conformal transformation.
We now construct $V_{2} \in H_{\alpha}^{1, q}(M)$ such that $V_{2} \geq 0$ and $V_{2} \geq \mathrm{R}\left[g_{1}\right]-\breve{\mathrm{R}}_{n}$. To accomplish this, let $\chi$ be a cutoff function that equals 1 on $B_{1}^{\mathbb{H}}$ and supported in $B_{2}^{\mathbb{H}}$. For each $i$ let $k_{i}=\max _{B_{1}^{\mathrm{H}}}\left|\Phi_{i}^{*}\left(\mathrm{R}\left[g_{1}\right]-\breve{\mathrm{R}}_{n}\right)\right|$. Since $q>n$, by Sobolev embedding we have $k_{i} \lesssim\left\|\Phi_{i}^{*}\left(\mathrm{R}\left[g_{1}\right]-\breve{\mathrm{R}}_{n}\right)\right\|_{H^{1, q}\left(B_{2}^{\text {H }}\right)}$. We define $V_{2}=\sum_{i} k_{i}\left(\left(\Phi_{i}\right)_{*} \chi\right)$, noting that a local uniform finiteness argument implies
$$\left\|V_{2}\right\|_{H_{\alpha}^{1, p}(M)} \lesssim\left\|\mathrm{R}\left[g_{1}\right]-\breve{\mathrm{R}}_{n}\right\|_{H_{\alpha}^{1, p}(M)} .$$
Multiplication by $V_{2}$ is continuous from $H_{\alpha}^{1, q}(M)$ to $H_{2 \alpha}^{1, q}(M)$ and therefore a compact operator $H_{\alpha}^{1, q}(M) \rightarrow H_{\alpha}^{0, q}(M)$; see Proposition 3.4. So $-a_{n} \Delta_{g_{1}}+V_{2}$ is a compact perturbation of $-a_{n} \Delta_{g_{1}}$ and hence a Fredholm map with index 0 from $H_{\alpha}^{1, q}(M)$ to $H_{\alpha}^{-1, q}(M)$. Moreover, since $V_{2} \geq 0$, an integration by parts argument using the density (see Proposition A.5) of smooth compactly supported functions in $H_{\alpha}^{1, q}(M)$ shows that the map has trivial kernel and hence $-a_{n} \Delta_{g_{1}}+V_{2}$ is an isomorphism. Let $u_{2} \in H_{\alpha}^{1, q}(M)$ be the solution of
$$-a_{n} \Delta_{g_{1}} u_{2}+V_{2} u_{2}=-V_{2} .$$
A homotopy argument as in the first conformal transformation shows $\Theta_{2}=1+u_{2}>0$. Since $V_{2} \geq 0$, and since $u_{2}$ and $V_{2}$ are in $H_{\alpha}^{1, q}(M) \subset X_{\alpha}^{1, q}(M)$, the maximum principle Lemma 6.5(a) implies $u_{2} \leq 0$ and hence $\Theta_{2}<1$.

Corollary 3.20 implies $\Theta_{2}^{2-q_{n}} \in X_{0}^{1, q}(M)$. Thus (6.23) and Proposition 3.19, applied to $F(x)=(1+x)^{2-q_{n}}-1$ as above, in combination with (6.2), imply that
$$\breve{\mathrm{R}}_{n} \mathrm{R}\left[g_{2}\right]-\breve{\mathrm{R}}_{n}=\Theta_{2}^{2-q_{n}}\left(\mathrm{R}\left[g_{1}\right]-\breve{\mathrm{R}}_{n}-V_{2}\right)+\left(\Theta_{2}^{2-q_{n}}-1\right) \breve{\mathrm{R}}_{n} \in H_{\alpha}^{1, q}(M) .$$
Furthermore, since $\mathrm{R}\left[g_{1}\right]-\breve{\mathrm{R}}_{n}-V_{2}<0$ and $\Theta_{2}<1$, we have $\mathrm{R}\left[g_{2}\right] \leq \breve{\mathrm{R}}_{n}$.
The result now follows from noting that Proposition 3.11 implies $\Theta_{1} \Theta_{2}-1 \in H_{\alpha}^{1, q}(M)$. \(\square\)

We now construct the low regularity candidate solution.
Proposition 6.7. Suppose $g$ is an asymptotically hyperbolic metric of class $\mathscr{H}^{1, q ; 1}$ for some $q>n$. There exists $u \in X_{1-n / q}^{1, q}(M ; \mathbb{R})$ solving equation (6.3).

Proof. For simplicity of notation, let $\alpha=1-n / q$; note $0<\alpha<1$. Due to Lemma 6.6 we can assume, without loss of generality, that $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{\alpha}^{1, q}(M)$ and that $\mathrm{R}[g] \leq \breve{\mathrm{R}}_{n}$. Indeed, if this is not the case, we first use the conformal factor $\Theta$ from Lemma 6.6 to transform to a metric satisfying these conditions. Then if $u \in X_{\alpha}^{1, q}(M)$ is a solution of equation (6.18) for the new metric, we find $\Theta(1+u)-1 \in X_{\alpha}^{1, q}(M)$ is a solution for the original metric.
We write (6.3) as
$$-a_{n} \Delta u=F(u),$$
where
$$F(u)=\breve{\mathrm{R}}_{n}(1+u)^{q_{n}-1}-\mathrm{R}[g](1+u) .$$
Since $\mathrm{R}[g] \leq \breve{\mathrm{R}}_{n}$ it follows that $u_{-}=0$ satisfies $-a_{n} \Delta u_{-}=0 \leq \breve{\mathrm{R}}_{n}-\mathrm{R}[g]=F\left(u_{-}\right)$and provides a lower barrier.
To find an upper barrier, we first let $v \in X_{\alpha}^{1, q}(M)$ be the solution of
$$-\Delta_{g} v=\alpha(n-1-\alpha) \rho^{\alpha},$$
which exists since $\alpha \in(0,1)$ lies in the Fredholm range defined by inequality (6.15) and since $\rho^{\alpha} \in X_{\alpha}^{1, q}(M)$. The maximum principle in Lemma 6.5(a) implies that $v \geq 0$.
A direct computation using $g=\rho^{-2} \bar{g}$ shows
$$-\Delta_{g} \rho^{\alpha}=-\alpha \rho^{\alpha+1} \Delta_{\bar{g}} \rho+\alpha(n-1-\alpha) \rho^{\alpha}|d \rho|_{\bar{g}}^{2}$$
and therefore Lemmas 5.2 and 5.3 imply
$$-\Delta_{g}\left(v-\rho^{\alpha}\right)=\alpha \rho^{\alpha}\left[(n-1-\alpha)\left(1-|d \rho|_{\bar{g}}^{2}\right)+\rho \Delta_{\bar{g}} \rho\right] \in X_{2 \alpha}^{0, q}(M) \subset X_{2 \alpha}^{-1, q}(M) .$$
Since $0<2 \alpha<2 \leq n-1$, we see that the weight $2 \alpha$ satisfies inequality (6.15) and thus Proposition 6.3 implies $-\Delta_{g}$ is an isomorphism $X_{2 \alpha}^{1, q}(M) \rightarrow X_{2 \alpha}^{-1, q}(M)$. Hence $v=\rho^{\alpha}+\xi$ for some $\xi \in X_{2 \alpha}^{1, q}(M) \subset C_{2 \alpha}^{0, \alpha}(M)$. Thus, since $\nu \geq 0$, we conclude that there exists $c>0$ such that $v \geq c \rho^{\alpha}$.

We claim that $u_{+}=K v$ forms an upper barrier for some $K$ sufficiently large, i.e. that $-a_{n} \Delta u_{+} \geq F\left(u_{+}\right)$. Since $-a_{n} \Delta K \nu>0$ it suffices to show that we may choose $K$ so that $F(K v) \leq 0$. To see this, first note that since $x \mapsto(1+x)^{q_{n}-2}$ is monotone increasing for $x \geq 0$,
$$F(k v) \leq(1+K v)\left(\breve{\mathrm{R}}_{n}(1+K c v)^{q_{n}-2}-\mathrm{R}[g]\right) .$$
Thus it suffices to show that
$$\left(1+K c \rho^{\alpha}\right)^{q_{n}-2} \geq \frac{\mathrm{R}[g]}{\breve{\mathrm{R}}_{n}} .$$
Since
$$\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{\alpha}^{1, q}(M) \subset \mathscr{H}^{1, q ; 1}(M) \subset C^{0, \alpha}(\bar{M})$$
we have $\mathrm{R}[g]=\breve{\mathrm{R}}_{n}+O\left(\rho^{\alpha}\right)$. The existence of $K$ satisfying (6.25) now follows from a direct computation, using the compactness of $\bar{M}$.
With barriers $u_{+}>u_{-}$in hand we now pick $\Lambda>0$ such that $F_{\Lambda}(z)=F(z)+\Lambda z$ is monotone increasing in $z$ for $0 \leq z \leq \max u_{+}$. Starting with $u_{0}=u_{+} \in X_{\alpha}^{1, q}(M)$ we iteratively construct a sequence $\left\{u_{k}\right\}$ in $X_{\alpha}^{1, q}(M)$ as follows. Assuming $u_{k} \in X_{\alpha}^{1, q}(M)$ has been found, observe that
$$F_{\Lambda}\left(u_{k}\right)=\breve{\mathrm{R}}_{n}\left[\left(1+u_{k}\right)^{q_{n}-1}-1\right]+\left(\breve{\mathrm{R}}_{n}-\mathrm{R}[g]\right)\left(1+u_{k}\right)+\left(\Lambda-\breve{\mathrm{R}}_{n}\right) u_{k} .$$
Since $\breve{\mathrm{R}}_{n}-\mathrm{R}[g] \in X_{\alpha}^{1, q}(M)$ and since $u_{k} \in X_{\alpha}^{1, q}(M)$, Proposition 3.11 and Proposition 3.19 imply $F_{\Lambda}\left(u_{k}\right) \in X_{\alpha}^{1, q}(M) \subset X_{\alpha}^{-1, q}(M)$. Note that $\alpha=1-n / q$ lies the Fredholm range of
$$-a_{n} \Delta_{g}+\Lambda: X_{\alpha}^{1, q}(M) \rightarrow X_{\alpha}^{-1, q}(M) ;$$
see (6.9) and (6.13). Hence Proposition 6.3 implies there exists $u_{k+1} \in X_{\alpha}^{1, q}(M)$ solving
$$-a_{n} \Delta_{g} u_{k+1}+\Lambda u_{k+1}=F_{\Lambda}\left(u_{k}\right) .$$
Note that by construction we have
$$\left(-a_{n} \Delta_{g}+\Lambda\right)\left(u_{1}-u_{0}\right)=F\left(u_{+}\right)+a_{n} \Delta_{g} u_{+} \leq 0 .$$
Thus the maximum principle Lemma 6.5(a) implies $u_{1} \leq u_{0}=u_{+}$. Furthermore, the monotonicity of $F_{\Lambda}$ implies
$$-a_{n} \Delta_{g} u_{1}+\Lambda u_{1}=F_{\Lambda}\left(u_{0}\right) \geq F_{\Lambda}(0)=\breve{\mathrm{R}}_{n}-\mathrm{R}[g] \geq 0,$$
and thus $u_{1} \geq 0=u_{-}$. Proceeding inductively, we find that $u_{-} \leq u_{k+1} \leq u_{k} \leq u_{+}$for all $k$.
From the monotonicity of $F_{\Lambda}$ and the fact that $u_{-} \leq u_{k} \leq u_{+}$for each $k$ it follows that $\left\{F_{\Lambda}\left(u_{k}\right)\right\}$ is bounded in $X_{\alpha}^{0, q}(M)$ and thus in $X_{\alpha}^{-1, q}(M)$. Proposition 6.3 then implies $\left\{u_{k}\right\}$ is bounded in $X_{\alpha}^{1, q}(M)$. We conclude from Proposition 3.2 that the sequence is bounded in $H_{\delta}^{1, q}(M)$ for any $\delta<\alpha-(n-1) / q$. Since $H_{\delta}^{1, q}(M)$ is reflexive, a subsequence $\left\{u_{k_{j}}\right\}$ converges weakly in $H_{\delta}^{1, q}(M)$ to a limit $u$ which, by monotonicity, is the pointwise limit of the full sequence and hence also lies in $X_{\alpha}^{0, q}(M)$. Now
$$-a_{n} \Delta_{g} u_{k_{j}}+\Lambda u_{k_{j}}=F_{\Lambda}\left(u_{\left(k_{j}\right)-1}\right)$$

Since $F_{\Lambda}\left(u_{\left(k_{j}\right)-1}\right) \rightarrow F_{\Lambda}(u)$ pointwise, the Dominated Convergence Theorem and the weak convergence of $\left\{u_{k_{j}}\right\}$ imply that $u$ is a distributional solution of $-a_{n} \Delta_{g} u+\Lambda u=F_{\Lambda}(u)$ and therefore also solves
$$-a_{n} \Delta_{g} u=F(u) .$$
Since $u \in X_{\alpha}^{0, q}(M)$, and since we can rewrite $F(u)$ in a form analogous to (6.26), it follows that $F(u) \in X_{\alpha}^{0, q}(M)$. Proposition 6.3 and the inclusion $X_{\alpha}^{1, q}(M) \subset H_{\delta}^{1, q}(M)$ then imply $u \in X_{\alpha}^{1, q}(M)$ as well. \(\square\)
6.1.3. Bootstrap. The following theorem implements the boostraps needed to assert full regularity from the candidate solution found in Proposition 6.7.

Theorem 6.8. Suppose $1<p<\infty, m \in \mathbb{N}, s \in \mathbb{R}$ with $s \geq m>n / p$ and $m \leq n$. Given an asymptotically hyperbolic metric $g$ of class $\mathscr{H}^{s, p ; m}$ there exists a unique conformal factor $\Theta \in \mathscr{H}^{s, p ; m}(M ; \mathbb{R})$ such that $\left.\Theta\right|_{\partial M}=1$ and such that
$$\mathrm{R}\left[\Theta^{q_{n}-2} g\right]=\breve{\mathrm{R}}_{n} .$$
Proof. In light of Lemma 6.1 and Propositions 4.11 and 4.13, using the the construction of Proposition 6.4 we may assume without loss of generality that $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{m-n / p}^{s-2, p}(M)$. As discussed prior to Lemma 6.6 we can choose $q \geq p$ such that
$$\frac{1}{p}-\frac{m}{n} \leq \frac{1}{q}-\frac{1}{n}<0 .$$
and such that $g$ is asymptotically hyperbolic of class $\mathscr{H}^{1, q ; 1}$. We set $\alpha=1-n / q$ and observe that $0<\alpha<1$ and that $m-n / p \geq \alpha$.
Proposition 6.7 implies there exists $u \in X_{\alpha}^{1, q}(M)$ that solves
$$-a_{n} \Delta_{g} u+\mathrm{R}[g](1+u)=\breve{\mathrm{R}}_{n}(1+u)^{q_{n}-1} .$$
We claim that in fact $u \in H_{m-n / p}^{s, p}(M)$. If this were true, then $u \in \mathscr{H}^{s, p ; m}(M)$ by Lemma 4.5 and $u=0$ at $\rho=0$ by Theorem 7.1. Consequently, $\Theta=1+u \in \mathscr{H}^{s, p ; m}(M)$ is the conformal factor we seek.

The proof of the claim follows from four bootstraps. In all cases we use the fact that equation (6.27) can be rewritten
$$-\Delta_{g} u+n u=\frac{\breve{\mathrm{R}}_{n}}{a_{n}}\left[(1+u)^{q_{n}-1}-1-\left(q_{n}-1\right) u\right]+\frac{\mathrm{R}[g]-\breve{\mathrm{R}}_{n}}{a_{n}}(1+u) .$$
Let $h$ be the smooth function on $(-1, \infty)$, vanishing at 0, such that
$$(1-x)^{q_{n}-1}-1-\left(q_{n}-1\right) x=h(x) x .$$
Then (6.28) can be expressed
$$-\Delta_{g} u+n u=\frac{\breve{\mathrm{R}}_{n}}{a_{n}} h(u) u+\frac{\mathrm{R}[g]-\breve{\mathrm{R}}_{n}}{a_{n}}(1+u) .$$

It is helpful to have sufficient conditions for
$$-\Delta_{g}+n: X_{\delta}^{\tau, r}(M) \rightarrow X_{\delta}^{\tau-2, r}(M)$$
to be an isomorphism. Recall the discussion of compatible Sobolev indicates $\mathcal{S}_{2}^{s, p}$ that follows Lemma 6.2: if ( $\tau, r$ ) satisfy (6.8), namely
$$1 \leq \tau \leq s \quad \text { and } \quad \frac{1}{p}-\frac{s}{n} \leq \frac{1}{r}-\frac{\tau}{n}<0,$$
then $(\tau, r) \in \mathcal{S}_{2}^{s, p}$ and thus the map (6.30) is continuous. If we furthermore have
$$-1<\delta<n$$
then Proposition 6.3 implies (6.30) is an isomorphism. Note that $\alpha$ satisfies (6.31).
First Bootstrap. Initially we know that $u \in X_{\alpha}^{1, q}(M)$ with $q \geq p$ and $1 / p-s / n \leq$ $1 / q-1 / n<0$. The goal at this step is to increase the number of derivatives to the maximum extent possible while leaving $q$ fixed. Suppose we have determined that $u \in X_{\alpha}^{\tau, q}(M)$ for some $1 \leq \tau \leq s$, and that $1 / p-s / n<1 / q-\tau / n<0$. Define $\hat{\tau}=\tau+2$ unless $1 / q-(\tau+2) / n<1 / p-s / n$, in which case we pick $\hat{\tau} \in(\tau, \tau+2]$ such that $1 / q-\hat{\tau} / n=$ $1 / p-s / n$. Then $1 / p-s / n \leq 1 / q-\hat{\tau} / n<0$. Moreover, since $q>p$, we find $1 \leq \hat{\tau} \leq s$ and we conclude $(\hat{\tau}, q) \in \mathcal{S}_{2}^{s, p}$. Thus, since $\alpha$ satisfies (6.31),
$$-\Delta+n: X_{\alpha}^{\hat{\tau}, q}(M) \rightarrow X_{\alpha}^{\hat{\tau}-2, q}(M)$$
is an isomorphism.
We now analyze the right side of (6.29). Since $u \in X_{\alpha}^{\tau, q}(M)$, Proposition 3.19 implies $h(u) \in X_{\alpha}^{\tau, q}(M)$ and, since $1 / q-\tau / n<0$, Proposition 3.11 implies $h(u) u \in X_{2 \alpha}^{\tau, q}(M)$. Because $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{m-n / p}^{s-2, p}(M) \subset X_{m-n / p}^{s-2, p}(M)$ we conclude that the right-hand side of equation (6.29) has the schematic form
$$X_{2 \alpha}^{\tau, q}(M)+X_{m-n / p}^{s-2, p}(M)+X_{m-n / p}^{s-2, p}(M) \cdot X_{\alpha}^{\tau, q}(M) .$$
Each of these terms lies in $X_{\alpha}^{\hat{\tau}-2, q}(M)$ : the first one is obvious; the second follows from Sobolev embedding along with the observation $\alpha \leq m-n / p$; and the third via Proposition 3.11 using the conditions $s>n / p, s \geq 1$, and the definition of $\hat{\tau}$. From Proposition 6.3, and the fact that $X_{\alpha}^{\hat{\tau}, q}(M)$ embeds in $X_{\alpha}^{\tau, q}(M)$, we conclude that $u \in X_{\alpha}^{\hat{\tau}, q}(M)$. Repeating this argument we can improve the number of derivatives to conclude that $u \in X_{\alpha}^{\tau, q}(M)$ for some $\tau$ with $1 / q-\tau / n=1 / p-s / n$.
Second Bootstrap. Suppose we have determined that $u \in X_{\alpha}^{\tau, r}(M)$ for some $r>p$ and $1 \leq \tau \leq s$, and that $1 / p-s / n=1 / r-\tau / n$. Let $\hat{\tau}=\min (\tau+2, s)$ and define $\hat{r}$ by
$$\frac{1}{\hat{r}}-\frac{\hat{\tau}}{n}=\frac{1}{p}-\frac{s}{n} .$$
Arguing as in the first bootstrap, the right-hand side of equation (6.29) has the schematic form
$$X_{2 \alpha}^{\tau, r}(M)+X_{m-n / p}^{s-2, p}(M)+X_{m-n / p}^{s-2, p}(M) \cdot X_{\alpha}^{\tau, r}(M) .$$

Each of these terms lies in $X_{\alpha}^{\hat{\tau}-2, \hat{r}}(M)$. This follows for the first two terms by Sobolev embedding whereas justifying this claim for third term requires a computation with Proposition 3.11 using the facts that $s>n / p, s \geq 1$, and $\hat{\tau}>n / \hat{r}$ along with the definition of $\hat{\tau}$ and $\hat{r}$. Proposition 6.3 and the fact that $X_{\alpha}^{\hat{\tau}, \hat{r}}(M)$ embeds in $X_{\alpha}^{\tau, r}(M)$ implies $u \in X_{\alpha}^{\hat{\tau}, \hat{r}}(M)$. This bootstrap terminates in finitely many steps when we conclude $u \in X_{\alpha}^{s, p}(M)$.
Third Bootstrap. We have found $u \in X_{\alpha}^{s, p}(M)$ for some $\alpha>0$. Arguing as in the first two bootstraps we find that the right-hand side of equation (6.28) has the form
$$X_{2 \alpha}^{s, p}(M)+X_{m-n / p}^{s-2, p}(M)+X_{m-n / p}^{s-2, p}(M) \cdot X_{\alpha}^{s, p}(M)$$
which lies in $X_{\min (2 \alpha, m-n / p)}^{s-2, p}(M)$. Since $\delta=\min (2 \alpha, m-n / p)$ satisfies inequality (6.31) we find that $u \in X_{\delta}^{s, p}(M)$. Repeating this procedure finitely many times we conclude $u \in X_{m-n / p}^{s, p}(M)$.
Final Bootstrap. At this stage we know that $u \in X_{m-n / p}^{s, p}(M)$ and we wish to show $u \in$ $H_{m-n / p}^{s, p}(M)$. Choose an initial $\delta$ such that $\delta<m-n / p-(n+1) / p$, in which case Lemma 3.2 implies $u \in H_{\delta}^{s, p}(M)$. Since $0<m-n / p<n$ we can nevertheless take $\delta$ sufficiently large so that
$$-1<\delta+\frac{n-1}{p}<n$$
and therefore $\delta$ lies in the Fredholm range from inequality (6.16) for $-\Delta_{g}+n$ mapping $H_{\delta}^{s, p}(M) \rightarrow H_{\delta}^{s-2, p}(M)$. As in the first bootstrap
$$(1+u)^{q_{n}-1}-1-\left(q_{n}-1\right) u=h(u) u$$
where Proposition 3.19 now implies $h(u) \in X_{m-n / p}^{s, p}(M)$ and we conclude from Proposition 3.11 that $h(u) u \in X_{m-n / p}^{s, p}(M) \cdot H_{\delta}^{s, p}(M) \subset H_{\delta+m-n / p}^{s, p}(M)$. Hence the right-hand side of equation (6.28) has the schematic form
$$H_{\delta+m-n / p}^{s, p}(M)+H_{m-n / p}^{s-2, p}(M) \subset H_{\delta^{\prime}}^{s-2, p}(M)$$
where $\delta^{\prime}=\min (m-n / p+\delta, m-n / p)$. We can then conclude $u \in H_{\delta^{\prime}}^{s, p}(M)$ so long as $\delta^{\prime}$ lies in the Fredholm range from inequality (6.16). But
$$-1<\delta+\frac{n-1}{p} \leq \delta^{\prime}+\frac{n-1}{p}$$
and
$$\delta^{\prime}+\frac{n-1}{p} \leq m-\frac{n}{p}+\frac{n-1}{p}=m-\frac{1}{p}<n$$
as required. Since $m-n / p>0$, repeating this argument finitely many times the bootstrap terminates when we conclude $u \in H_{m-n / p}^{s, p}(M)$.
Uniqueness. To investigate uniqueness, we are welcome to start the construction at one of the constant scalar curvature metrics in the conformal class, in which case equation (6.28) becomes
$$-\Delta_{g} u+n u=F(u)$$
with $F(u)=\frac{\breve{\mathrm{R}}_{n}}{a_{n}}\left[(1+u)^{q_{n}-1}-1-\left(q_{n}-1\right) u\right]$. Since $q_{n}>2, F^{\prime \prime}(x)<0$ for $x>-1$ and we find $F$ has a maximum on $(-1, \infty)$ at $x=0$ where $F(0)=0$. A solution of equation (6.32) in $H_{m-n / p}^{s, p}(M)$ then satisfies $-\Delta_{g} u+n u \leq 0$ and we can lower reguality so that the maximum principle Lemma 6.5 implies $u \leq 0$. It follows that any conformal factor $\Theta$ taking some constant scalar curvature metric to another satisfies $\Theta \leq 1$. But this is only possible if there is a single such metric. \(\square\)
6.2. Solution in the $\mathscr{X}^{s, p ; m}$ category. The strategy is parallel to that for $\mathscr{H}^{s, p ; m}$ but is somewhat less technical at every stage. We state the results obtained and briefly sketch the changes needed.

Proposition 6.9. Suppose $1<p<\infty, m \in \mathbb{N}, s \in \mathbb{R}$, with $s>n / p, s \geq m$ and $m \leq n$. Given an asymptotically hyperbolic metric $g$ on $M$ of class $\mathscr{X}^{s, p ; m}$ there exists a positive conformal factor $\Theta \in \mathscr{X}^{s, p ; m}(M ; \mathbb{R})$ such that $\left.\Theta\right|_{\partial M}=1$ and such that
$$\mathrm{R}\left[\Theta^{-2} g\right]-\breve{\mathrm{R}}_{n} \in X_{m}^{s-2, p}(M ; \mathbb{R}) .$$
Proof. When $m=1$ Proposition 5.1 implies immediately that $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in X_{1}^{s-2, p}(M)$. Otherwise we proceed as in Proposition 6.4 through a sequence of conformal transformations with conformal factors $\Theta \in \mathscr{X}^{s, p ; m}(M)$ so that if $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in X_{k}^{s-2, p}(M)$ for some integer $1 \leq k \leq n-1$, then $\mathrm{R}\left[\Theta^{2} g\right]-\breve{\mathrm{R}}_{n} \in X_{k+1}^{s-2, p}(M)$. The argument is somewhat simplified because we are able to improve the decay by a full power of $\rho$ at each step. When $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in X_{k}^{s-2, p}(M)$, Proposition 5.1 and Theorem 7.1 imply
$$\mathrm{R}[g]=\breve{\mathrm{R}}_{n}+\rho^{k} \tau+r$$
with $\tau \in \mathscr{X}^{\infty ; m-k}(M)$ and $r \in X_{m}^{s-2, p}(M)$. We take the conformal factor of the form $\Theta=1+\rho^{k} u$ with $u \in \mathscr{X}^{\infty ; m-k}(M)$, in which case
$$\rho^{k} u \in X_{k}^{\infty}(M), \quad \rho^{k+1} \hat{\nabla} u \in X_{k+2}^{\infty}(M), \quad \hat{\nabla}^{2} u \in X_{k+1}^{\infty}(M) .$$
Lemmas 5.2-5.4 imply
$$|d \rho|_{\bar{g}}^{2}-1 \in X_{1}^{s, p}(M), \quad \rho \Delta_{\bar{g}} \rho \in X_{1}^{s-1, p}(M), \quad \rho^{2} R[\bar{g}] \in X_{1}^{s-2, p}(M) .$$
A computation using these facts leads to
$$\mathrm{R}\left[\Theta^{2} g\right]-\breve{\mathrm{R}}_{n}=\rho^{k}(\tau+2(k+1)(n-1)(n-k) u)+X_{k+1}^{s-2, p}(M)$$
and since $k<n$ we can take $u=-\tau /(2(k+1)(n-1)(n-k))$ near $\partial M$. \(\square\)

Consider an asymptotically hyperbolic metric $g$ of class $\mathscr{X}^{s, p ; m}$ with $s>n / p, s \geq m$ and $m \geq 1$. Choose $q>1$ so that
$$\frac{1}{p}-\frac{s}{n} \leq \frac{1}{q}-\frac{1}{n}<0$$
which is possible since $s \geq 1$ and $s>n / p$. Lemma 4.2 and Proposition 4.7 imply $\bar{g}=$ $\rho^{2} g \in H^{1, q}(\bar{M})=\mathscr{H}^{1, q ; 1}(M)$ and hence $g$ is also asymptotically hyperbolic of class
$\mathscr{H}^{1, q ; 1}$. Thus, the second step of the $\mathscr{H}^{s, p ; m}$ construction applies without change and we need only establish the desired regularity of the candidate solution.

Theorem 6.10. Suppose $1<p<\infty, m \in \mathbb{N}, s \in \mathbb{R}$ with $s>n / p, s \geq m$ and $m<n$. Given an asymptotically hyperbolic metric $g$ of class $\mathscr{X}^{s, p ; m}$ there exists a unique conformal factor $\Theta \in \mathscr{X}^{s, p ; m}(M ; \mathbb{R})$ such that $\left.\Theta\right|_{\partial M}=1$ and such that
$$\mathrm{R}\left[\Theta^{q_{n}-2} g\right]=\breve{\mathrm{R}}_{n} .$$
Proof. The proof is a truncated version of the proof of Theorem 6.8. Using Proposition 6.9 we can assume $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in X_{m}^{s-2, p}(M)$, and from Proposition 6.7 and the comments above we know that there exists a solution $u \in X_{1-n / q}^{1, q}(M)$ of equation (6.18) for some $q$ with $1 / p-s / n \leq 1 / q-1 / n<0$. The first two bootstraps to improve the interior regularity of $u$ are essentially identical to those of Theorem 6.8, replacing some instances of $X_{m-n / p}^{s-2, p}(M)$ with the even more regular space $X_{m}^{s-2, p}(M)$ arising from scalar curvature terms, and we arrive at the conclusion $u \in X_{1-n / q}^{s, p}(M)$. In the course of the third bootstrap we find that if $u \in X_{\alpha}^{s, p}(M)$ for some $\alpha>0$ then
$$-\Delta_{g} u+n u \in X_{2 \alpha}^{s, p}(M)+X_{m}^{s-2, p}(M) .$$
Since $\alpha>0$ and $m<n, \delta=\min (2 \alpha, m)$ lies in the Fredholm range from inequality (6.17) and we conclude $u \in X_{\delta}^{s, p}(M)$. Since $\alpha>0$, this bootstrap terminates after finitely many steps when we conclude $u \in X_{m}^{s, p}(M) \subset \mathscr{X}^{s, p ; m}(M)$ and, by Theorem 7.1, vanishes at $\rho=0$. The fourth bootstrap of Theorem 6.8 is not needed and uniqueness follows from uniqueness in the $\mathscr{H}^{1, q ; 1}$ category. \(\square\)

Note that if $m=n$, the proof of Theorem 6.10 almost succeeds. The only failure occurs at the very end of the third bootstrap because $\delta=n$ just fails to lie in the Fredholm range from inequality (6.17), and we can only conclude that $u \in X_{\delta}^{s, p}(M)$ for any $\delta<n$. This is not enough to conclude that $u \in \mathscr{X}^{s, p ; n}(M ; \mathbb{R})$, however, as is needed to preserve the original metric's regularity class. As mentioned previously, for a smooth background metric when $n=3$ a generic solution will contain a term of the form $\rho^{3} \log (\rho)$. Such a term does not lie in $\mathscr{X}^{3, p ; 3}(M ; \mathbb{R})$, for otherwise after taking three $\partial_{\rho}$ derivatives we would conclude $\log (\rho) \in X_{0}^{0, p}(M ; \mathbb{R})$, which is false.

\section*{7. Boundary asymptotics in fortified spaces}

The aim of this section is to prove the following result from §4, which shows that a function in a fortified space can be decomposed into two pieces, one of which is smooth in the interior of $M$ and captures the asymptotic behavior, whereas the second piece is a nonsmooth remainder that decays as rapidly as the limited boundary regularity allows.

Theorem 7.1 (Asymptotic Structure Theorem). Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}, s \geq m$ and $E$ is a tensor bundle over $M$ of weight $w$.
\begin{itemize}
\item[(a)] If $u \in \mathscr{H}^{s, p ; m}(M ; E)$ then
$$u=\tau+r$$
where $\tau \in \mathscr{H}^{\infty, p ; m}(M ; E)$ and $r \in H_{w+m-n / p}^{s, p}(M ; E)$. Moreover, if $u \in H_{w+k+\alpha-n / p}^{s, p}(M ; E)$ for some integer $0 \leq k \leq m-1$ and some $\alpha \in[0,1)$, then $\tau=\rho^{k} \eta$ for some $\eta \in \mathscr{H}^{\infty, p ; m-k}(M ; E) \cap H_{w+\alpha-n / p}^{\infty, p}(M ; E)$.
Finally, if $m \geq 1$ then $\left.u\right|_{\partial M}=0$ if and only if $u \in H_{w+1-n / p}^{s, p}(M ; E)$.
\item[(b)] If $u \in \mathscr{X}^{s, p ; m}(M ; E)$ then
$$u=\tau+r$$
where $\tau \in \mathscr{X}^{\infty ; m}(M ; E)$ and $r \in X_{w+m}^{s, p}$. Moreover, if $u \in X_{w+k}^{s, p}$ for some integer $0 \leq k \leq m$ and some $\alpha \in[0,1)$, then $\tau=\rho^{k} \eta$ for some $\eta \in \mathscr{X}^{\infty ; m-k}(M ; E) \cap$ $X_{w+\alpha}^{\infty}(M ; E)$.
Finally, if $m \geq 1$ then $\left.u\right|_{\partial M}=0$ if and only if $u \in X_{w+1}^{s, p}(M ; E)$.
\end{itemize}

The proof of Theorem 7.1 relies on two technical tools.
\begin{itemize}
\item[(1)] For functions in fortified spaces, a vanishing boundary trace manifests itself as an additional rate of decay at the boundary. Moreover, higher-order $\partial_{\rho}$ derivatives vanishing at the boundary are quantitatively reflected in terms of higher-order decay. Section 7.1 contains precise statements of these facts, which generalize corresponding results in [AILSA18] for Hölder continuous functions.
\item[(2)] $\mathbb{H}$-mollification, introduced previously in [AILSA18] as group mollification, extends to the current setting and can be used to improve a function's interior regularity while leaving its boundary trace unchanged. Section 7.2 contains the details.
\end{itemize}

Section 7.3 uses these tools to establish Theorem 7.11, a variation of Taylor's Theorem for expansions at the conformal boundary, and Theorem 7.1 follows as a straightforward consequence.
$\mathbb{H}$-mollification is based on the half-space model of hyperbolic space and is better adapted to a subtly different class of function spaces than those used elsewhere in this paper; the key difference is that the boundary defining function $y$ on $\mathbb{H}$ is singular at a point on the boundary of the ball model. For functions on $\mathbb{H}$ supported in some fixed domain avoiding a neighborhood of the singularity the norms in the two classes of function spaces are equivalent, and this observation allows us to transfer facts from the half-space model when proving Theorem 7.1. Nevertheless, for the remainder of this section we work within this new framework and we begin by defining its associated function spaces and outlining their basic properties.
Let $\mathbb{R}_{+}^{n}$ be the Euclidean half space with coordinates $(x, y)$, where $x \in \mathbb{R}^{n-1}$ and $y \geq 0$, and metric
$$g_{\mathbb{E}}=\left(d x^{1}\right)^{2}+\cdots+\left(d x^{n-1}\right)^{2}+d y^{2} .$$
The Euclidean connection is $\nabla_{\mathbb{E}}$. As introduced in §2, $\mathbb{H}$ denotes the $n$-dimensional space half space model of hyperbolic space, corresponding to the interior of $\mathbb{R}_{+}^{n}$, and equipped
with the metric
$$\breve{g}=y^{-2} g_{\mathbb{E}}=y^{-2}\left(\left(d x^{1}\right)^{2}+\cdots+\left(d x^{n-1}\right)^{2}+d y^{2}\right) .$$
Let $\Phi_{i}: B_{2}^{\mathbb{H}} \rightarrow \mathbb{H}$, given by $\Phi_{i}:(\xi, \eta) \mapsto\left(x_{i}+y_{i} \xi, y_{i} \eta\right)$, be a countable collection of Möbius parametrizations with uniformly locally finite images such that the sets $\Phi_{i}\left(B_{1 / 2}^{\mathbb{H}}\right)$ cover $\mathbb{H}$. We define the half-space versions of the Sobolev and Gicquaud-Sakovich spaces of sections of a tensor bundle $E$ over $\mathbb{H}$ of scalar-valued functions via
$$\begin{gathered}
\|u\|_{H_{\delta}^{s, p}(\mathbb{H} ; E \mid y)}=\left(\sum_{i} y_{i}^{-\delta p}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)}^{p}\right)^{1 / p}, \\
\|u\|_{X_{\delta}^{s, p}(\mathbb{H} ; E \mid y)}=\sup _{i} y_{i}^{-\delta p}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} ;
\end{gathered}$$
here $H^{s, p}\left(B_{1}^{\mathbb{H}}\right)$ is computed as in §3. Uniformly equivalent norms are obtained if $B_{1}^{\mathbb{H}}$ is replaced by $B_{r}^{\mathbb{H}}$ for $1 / 2 \leq r \leq 2$ in (7.1). Throughout this section the bundle $E$ is easily inferred from context and we almost universally only consider scalar valued functions. Hence we usually drop the bundle from the notation and write $H_{\delta}^{s, p}(\mathbb{H} \mid y)$ instead, emphasizing the role of the singular boundary defining function $y$.
For fortified spaces in this setting we only work with scalar-valued functions and define
$$\begin{aligned}
\|u\|_{\mathscr{H} \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y)} & =\sum_{j=0}^{m}\left\|\nabla_{\mathbb{E}}^{j} u\right\|_{H_{j-n / p}^{s-j, p}(\mathbb{H} \mid y)}, \\
\|u\|_{\mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)} & =\sum_{j=0}^{m}\left\|\nabla_{\mathbb{E}}^{j} u\right\|_{X_{j}^{s-j, p}(\mathbb{H} \mid y)},
\end{aligned}$$
which should be compared with the definitions (4.2) and (4.3).
We make use of equivalent norms obtained from coordinate derivatives as follows. For a multiindex $\alpha=\left(\alpha_{1}, \ldots, \alpha_{n}\right) \in \mathbb{Z}_{\geq 0}^{n}$ we define
$$\partial^{\alpha}=\partial_{x^{1}}^{\alpha_{1}} \cdots \partial_{x^{n-1}}^{\alpha_{n-1}} \partial_{y}^{\alpha_{n}}, \quad \text { and } \quad(y \partial)^{\alpha}=\left(y \partial_{\theta^{1}}\right)^{\alpha_{1}} \cdots\left(y \partial_{\theta^{n-1}}\right)^{\alpha_{n-1}}\left(y \partial_{y}\right)^{\alpha_{n}}$$
and set $|\alpha|=\alpha_{1}+\cdots+\alpha_{n}$. For $1<p<\infty$ we have the norm equivalences for functions on $\mathbb{H}$ :
$$\begin{aligned}
& \|u\|_{\mathscr{H} \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y)} \sim \sum_{|\beta| \leq m}\left\|\partial^{\beta} u\right\|_{H_{-n / p}^{s-|\beta|, p}(\mathbb{H} \mid y)}, \\
& \|u\|_{\mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)} \sim \sum_{|\beta| \leq m}\left\|\partial^{\beta} u\right\|_{X_{0}^{s-|\beta|, p}(\mathbb{H} \mid y)} .
\end{aligned}$$
Furthermore, since $y$ is uniformly bounded above and below on $B_{2}^{\mathbb{H}}$, we have the local norm equivalences
$$\|u\|_{H^{k, p}\left(B_{r}^{\mathbb{H}}\right)} \sim \sum_{|\alpha| \leq k}\left\|(y \partial)^{\alpha} u\right\|_{L^{p}\left(B_{r}^{\mathbb{H}}\right)}$$
for all $k \in \mathbb{N}_{\geq 0}$ and $1 / 2 \leq r \leq 2$.

While many results for the weighted spaces and fortified spaces proved in Sections 3 and 4 transfer to the spaces here, not all facts do, and some care is needed because of the noncompactness of $\mathbb{R}_{+}^{n}$. For example, it is not true that $X_{0}^{s, p}(\mathbb{H} \mid y)$ embeds in $H_{-n / p}^{s, p}(\mathbb{H} \mid y)$. The following observations can be proved using straightforward modifications of earlier results.
\begin{itemize}
\item[-] The spaces are complete.
\item[-] For scalar-valued functions, the $H_{-n / p}^{0, p}(\mathbb{H} \mid y)$ norm is equivalent to the usual Lebesgue norm $L^{p}\left(\mathbb{R}_{+}^{n}\right)$ and $\mathscr{H}^{1, p ; 1}(\mathbb{H} \mid y)$ is the usual Sobolev space $H^{1, p}\left(\mathbb{R}_{+}^{n}\right)$.
\item[-] $y^{\beta} H_{\delta}^{s, p}(\mathbb{H} \mid y)=H_{\delta+\beta}^{s, p}(\mathbb{H} \mid y)$ for any $\beta \in \mathbb{R}$, and similarly for Gicquaud-Sakovich spaces.
\item[-] $\partial^{\alpha}: H_{\delta}^{s, p}(\mathbb{H} \mid y) \rightarrow H_{\delta-|\alpha|}^{s-|\alpha|, p}(\mathbb{H} \mid y)$ if $|\alpha| \leq s$, and similarly for the spaces $X_{\delta}^{s, p}(\mathbb{H} \mid y)$
\item[-] $\partial^{\alpha}: \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y) \rightarrow \mathscr{H}^{s-|\alpha|, p ; m-|\alpha|}(\mathbb{H} \mid y)$ if $|\alpha| \leq m$, and similarly for the spaces $\mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)$
\item[-] If $s \geq m+1$ then $y \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y) \subset H^{s, p ; m+1}(\mathbb{H} \mid y)$ and similarly for the spaces $\mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)$.
\item[-] The direct analog of Lemma 3.9, i.e. $\|u\|_{H_{\delta}^{s, p}(\mathbb{H} \mid y)} \sim\|u\|_{H_{\delta}^{0, p}(\mathbb{H} \mid y)}+\left\|\nabla_{\mathbb{E}}^{k} u\right\|_{H_{\delta}^{s-k, p}}$ and similarly for the spaces $X_{\delta}^{s, p}(\mathbb{H} \mid y)$.
\end{itemize}
7.1. Boundary traces and asymptotic decay. As a consequence of the elementary embeddings
$$\mathscr{X}^{s, p ; m}(\mathbb{H} \mid y) \hookrightarrow \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y) \hookrightarrow \mathscr{H}^{m, p ; m}(\mathbb{H} \mid y)=H^{m, p}\left(\mathbb{R}_{+}^{n}\right)$$
it follows that elements of fortified spaces admit boundary traces when $m \geq 1$. In this section we establish the connection between the rate of decay of a function $u$ in a fortified function space and the vanishing trace of its derivatives $\partial_{y}^{k} u$ at the boundary. As a first step, the next two lemmas show that if $u$ has a vanishing trace, the decay of $u$ at the boundary is one order better than the decay of $\partial_{y} u$. The first lemma treats Gicquaud-Sakovich spaces, and the second weighted Sobolev spaces.

Lemma 7.2. Suppose for some $1<p<\infty$ that $u$ is a real-valued distribution such that $u \in$ $\mathscr{X}^{1, p ; 1}(\mathbb{H} \mid y),\left.u\right|_{y=0}=0$, and $\partial_{y} u \in X_{\delta}^{0, p}(\mathbb{H} \mid y)$ for some real $\delta \geq 0$. Then $u \in X_{\delta+1}^{0, p}(\mathbb{H} \mid y)$ and
$$\|u\|_{X_{\delta+1}^{0, p}(\mathbb{H} \mid y)} \lesssim\left\|\partial_{y} u\right\|_{X_{\delta}^{0, p}(\mathbb{H} \mid y)} .$$
Proof. Let $\Phi_{i}$ be a Möbius parametrization. Let $Q_{i}=\Phi_{i}\left(Y_{5}\right)$ and observe that since $B_{1}^{\mathbb{H}} \subset$ $Y_{5}, \Phi_{i}\left(B_{1}\right)^{\mathbb{H}} \subset Q_{i}$. Since $\Phi_{i}^{*} d V_{g_{\mathbb{B}}}=y_{i}^{n} d V_{g_{\mathbb{B}}}$, and recalling from §3.1 that we compute norms on $B_{1}^{\mathbb{H}}$ using the Euclidean metric $g_{\mathbb{E}}$, we find
$$\left\|\Phi_{i}^{*} u\right\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)}^{p}=y_{i}^{-n}\|u\|_{L^{p}\left(\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)\right)}^{p} \leq y_{i}^{-n}\|u\|_{L^{p}\left(Q_{i}\right)}^{p} .$$

Assume for the moment that $u$ is smooth and vanishes on $\partial \mathbb{H}$. For $(x, y) \in Q_{i}$ we have
$$|u(x, y)|=\left|\int_{0}^{y} \partial_{y} u(x, \eta) d \eta\right| \leq y^{\frac{1}{p^{*}}}\left[\int_{0}^{y}\left|\left(\partial_{y} u\right)(x, \eta)\right|^{p} d \eta\right]^{\frac{1}{p}} .$$
Integrating $p^{\text {th }}$ powers and using the relation $p / p^{*}=p-1$
$$\begin{aligned}
\left.\int_{0}^{5 y_{i}}|u(x, y)|^{p} d y \leq\left(\int_{0}^{5 y_{i}} y^{\frac{p}{p^{*}}} d y\right) \int_{0}^{5 y_{i}} \right\rvert\,\left(\partial_{y} u\right) & \left.(x, \eta)\right|^{p} d \eta \\
& =\frac{1}{p}\left(5 y_{i}\right)^{p} \int_{0}^{5 y_{i}}\left|\left(\partial_{y} u\right)(x, \eta)\right|^{p} d \eta
\end{aligned}$$
Now integrating in $x$ we conclude
$$\int_{Q_{i}}|u|^{p} d V_{g_{\mathrm{B}}} \lesssim y_{i}^{p} \int_{Q_{i}}\left|\partial_{y} u\right|^{p} d V_{g_{\mathrm{B}}}$$
and a density argument shows that this same inequality holds for all $u$ in the usual Sobolev space $W^{1, p}\left(Q_{i}\right)$ that vanish at $y=0$. Moreover, since the volume of $Q_{i}$ is finite, a computation from the definition analogous to that of Lemma 3.16(c) shows that $\mathscr{X}^{1, p ; 1}(\mathbb{H} \mid y)$ restricts continuously into $W^{1, p}\left(Q_{z}^{*}\right)$ and hence inequality (7.6) applies to these functions as well.

A computation shows that if $B_{1}^{\mathbb{H}}(p) \cap Y_{5} \neq \emptyset$ then $B_{1}^{\mathbb{H}}(p) \subset Y_{100}$. Let $Q_{i}^{*}=\Phi_{i}\left(Y_{100}\right)$ and let $J=\left\{j: \Phi_{j}\left(B_{1}^{\mathbb{H}}\right) \cap Q_{i} \neq \emptyset\right\}$. Observe that if $j \in J$ then $y_{j} \leq 100 y_{i}$. Setting $A=\cup_{j \in J} \Phi_{j}\left(B_{1}^{\mathbb{H}}\right) \subset Q_{i}^{*}$ we compute
$$\begin{aligned}
\int_{Q_{i}}\left|\partial_{y} u\right|^{p} d V_{g_{\mathbb{E}}} & \leq \int_{A}\left|\partial_{y} u\right|^{p} d V_{g_{\mathbb{B}}} \\
& \leq \sum_{j \in J} \int_{\Phi_{j}\left(B_{1}^{\mathbb{H}}\right)}\left|\partial_{y} u\right|^{p} d V_{g_{\mathbb{B}}} \\
& =\sum_{j \in J} y_{j}^{n}\left\|\Phi_{j}^{*} \partial_{y} u\right\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)}^{p} \\
& \leq \sum_{j \in J} y_{j}^{n} y_{j}^{\delta p}\left\|\partial_{y} u\right\|_{X_{\delta}^{0, p}(\mathbb{H} \mid y)}^{p} \\
& \leq 100^{\delta p} y_{i}^{\delta p}\left\|\partial_{y} u\right\|_{X_{\delta}^{0, p}(\mathbb{H} \mid y)}^{p} \sum_{j \in J} y_{j}^{n} \\
& \lesssim y_{i}^{\delta p}\left\|\partial_{y} u\right\|_{X_{\delta}^{0, p}(\mathbb{H} \mid y)}^{p} \int_{A} d V_{g_{\mathbb{B}}}
\end{aligned}$$
where uniform local finiteness was used in the final step. Moreover, since $A \subset Q_{i}^{*}$,
$$\int_{A} d V_{g_{\mathbb{B}}} \leq \operatorname{Vol}_{g_{\mathbb{B}}}\left(Q_{i}^{*}\right)=y_{i}^{n} \operatorname{Vol}_{g_{\mathbb{B}}}\left(Y_{100}\right) .$$

Combining inequalities (7.5), (7.6), (7.7), (7.8) we find
$$y_{i}^{-\delta-1}\left\|\Phi_{i}^{*} u\right\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\partial_{y} u\right\|_{X_{\delta}^{0, p}(\mathbb{H} \mid y)} ;$$
taking a supremum over $i$ completes the proof. \(\square\)

Lemma 7.3. Suppose $u \in \mathscr{H}^{1, p ; 1}(\mathbb{H} \mid y)$ for some $1<p<\infty$ such that $\left.u\right|_{y=0}=0$ and such that $\partial_{\rho} u \in H_{\delta-n / p}^{0, p}(\mathbb{H} \mid y)$ for some $\delta \geq 0$. Then $u \in H_{\delta+1-n / p}^{0, p}(\mathbb{H} \mid y)$ and
$$\|u\|_{H_{\delta+1-n / p}^{0, p}}(\mathbb{H} \mid y) \lesssim\left\|\partial_{y} u\right\|_{H_{\delta-n / p}^{0, p}(\mathbb{H} \mid y)} .$$
Proof. The hypotheses on $u$ can be reformulated as $u \in W^{1, p}\left(\mathbb{R}_{+}^{n}\right),\left.u\right|_{y=0}=0$, and $y^{-\delta} \partial_{y} u \in$ $L^{p}\left(\mathbb{R}_{+}^{n}\right)$. We wish to show that $y^{-(\delta+1)} u \in L^{p}\left(\mathbb{R}_{+}^{n} \mid y\right)$ and indeed we will show
$$\left\|y^{-(\delta+1)} u\right\|_{L^{p}\left(\mathbb{R}_{+}^{n}\right)} \leq \frac{p}{(\delta+1) p-1}\left\|y^{-\delta} \partial_{y} u\right\|_{L^{p}\left(\mathbb{R}_{+}^{n}\right)} .$$
Note that since $p>1$ and $\delta \geq 0$ the coefficient on the right-hand side of equation (7.9) is finite.

First, suppose that $u$ is smooth, compactly supported on the interior of $\mathbb{R}_{+}^{n}$ and is non-negative. Then
$$\begin{aligned}
\int_{\mathbb{R}_{+}^{n}} y^{-(\delta+1) p} u^{p} d V_{\mathbb{E}} & =\frac{1}{1-(\delta+1) p} \int_{\mathbb{R}_{+}^{n}} \partial_{y}\left(y^{1-(\delta+1) p}\right) u^{p} d V_{g_{\mathbb{B}}} \\
& =\frac{p}{(\delta+1) p-1} \int_{\mathbb{R}_{+}^{n}}\left(y^{-(\delta+1)} u\right)^{p-1} y^{-\delta} \partial_{y} u d V_{g_{\mathbb{B}}} \\
& \leq \frac{p}{(\delta+1) p-1}\left\|y^{-(\delta+1)} u\right\|_{L^{p}\left(\mathbb{R}_{+}^{n}\right)}^{p / p^{*}}\left\|y^{-\delta} \partial_{y} u\right\|_{L^{p}\left(\mathbb{R}_{+}^{n}\right)} .
\end{aligned}$$
Noting that that $p / p^{*}=p-1$, we arrive at (7.9). In fact, inequality (7.9) holds for all functions in $W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$ that vanish for $y \leq \varepsilon$ for some $\varepsilon>0$. The smoothness hypothesis can be dropped by considering a sequence of smooth non-negative compactly supported functions that vanish for $y \leq \varepsilon / 2$ and converge to $u$ in $W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$. This argument requires the observation that the integrals appearing in (7.9) are continuous on the subspace of of functions in $W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$ that vanish for $y \leq \varepsilon / 2$. The non-negativity can be relaxed since $u \mapsto|u|$ is continuous on $W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$ and since $\left|\partial_{y} u\right|=\left|\partial_{y}\right| u| |$.
Now consider an arbitrary function $u \in W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$ such that $\left.u\right|_{y=0}=0$ and such that $y^{-\delta} \partial_{y} u \in L^{p}\left(\mathbb{R}_{+}^{n}\right)$. Let $\chi:[0, \infty) \rightarrow[0,1]$ be a monotone smooth function that equals 1 on $[0,1]$ and vanishes on $[2, \infty)$. For $m \in \mathbb{N}$ define $\kappa_{m}(y)=1-\chi(m y)$ and $\chi_{m}(x)=$ $\chi\left(|x|^{2} / m^{2}\right)$ so $\kappa_{m}$ vanishes for $y<1 / m$ and $\chi_{m}$ vanishes for $|x|^{2}>2 m^{2}$. Inequality (7.9)
applied to $\kappa_{m} \chi_{m} u$ yields
$$\begin{aligned}
& \left\|\chi_{m} \kappa_{m} y^{-(\delta+1)} u\right\|_{L^{p}\left(\mathbb{R}_{+}^{n}\right)} \leq \\
& \quad \frac{p}{(\delta+1) p-1}\left[\left\|\chi_{m} \kappa_{m} y^{-\delta} \partial_{y} u\right\|_{L^{p}\left(\mathbb{R}_{+}^{n}\right)}+K m\left(\int_{1 / m}^{2 / m} \int_{\mathbb{R}^{n-1}} \chi_{m}\left|y^{-\delta} u\right|^{p} d x d y\right)^{\frac{1}{p}}\right]
\end{aligned}$$
where $K$ is a constant depending on the choice of $\chi$ but is independent of $m$, and where we write $d V_{g_{\mathrm{E}}}=d x d y$. The result then follows from an application of the Monotone Convergence Theorem so long as we can show that the second term in the brackets on the right-hand side of (7.10) vanishes in the limit $m \rightarrow \infty$.
For smooth functions that vanish at $y=0$
$$\int_{\mathbb{R}^{n-1}} \chi_{m}|u(x, y)|^{p} d x=\int_{\mathbb{R}^{n-1}} \chi_{m}\left|\int_{0}^{y}\left(\partial_{y} u\right)(x, \eta) d \eta\right|^{p} d x$$
for any $y>0$. A density argument shows this same equality holds for all functions in $W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$ with zero boundary trace because both sides of the equality are continuous on $W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$; this last claim uses the compact support of $\chi_{m}$.
Consider the map $y \mapsto\left(\partial_{y} u\right)(x, y)$, which is an $L^{p}$ function of $y$ on $[0, y]$ for almost every $x \in \mathbb{R}^{n-1}$. Hölder's inequality implies
$$\begin{aligned}
\left|\int_{0}^{y}\left(\partial_{y} u\right)(x, \eta) d \eta\right|^{p} & \leq\left[\int_{0}^{y} \eta^{\delta p^{*}} d \eta\right]^{\frac{p}{p^{*}}} \int_{0}^{y} \eta^{-\delta p}\left|\left(\partial_{y} u\right)(x, \eta)\right|^{p} d \eta \\
& =\left(\frac{1}{\delta p^{*}+1}\right)^{\frac{p}{p^{*}}} y^{\delta p+p-1} \int_{0}^{y} \eta^{-\delta p}\left|\left(\partial_{y} u\right)(x, \eta)\right|^{p} d \eta .
\end{aligned}$$
Multiplying (7.11) by $m^{p} y^{-\delta p}$, integrating in $y$, and applying estimate (7.12) we conclude
$$\begin{aligned}
m^{p} \int_{0}^{2 / m} & \int_{\mathbb{R}^{n-1}} \chi_{m} y^{-\delta p}|u|^{p} d x d y \\
& \lesssim m^{p} \int_{0}^{2 / m} y^{p-1} \int_{\mathbb{R}^{n-1}} \chi_{m} \int_{0}^{y} \eta^{-\delta p}\left|\left(\partial_{y} u\right)(x, \eta)\right|^{p} d \eta d x d y \\
& \leq m^{p}\left(\int_{0}^{2 / m} y^{p-1} d y\right) \int_{\mathbb{R}^{n-1}} \int_{0}^{2 / m} y^{-\delta p}\left|\partial_{y} u\right|^{p} d y d x \\
& =\frac{2^{p}}{p} \int_{\mathbb{R}^{n-1}} \int_{0}^{2 / m} y^{-\delta p}\left|\partial_{y} u\right|^{p} d y d x
\end{aligned}$$
This final integral converges to 0 as $m \rightarrow \infty$, which establishes the desired limit. \(\square\)

We are now ready to quantitatively connect rates of decay at the boundary to vanishing boundary traces.

Proposition 7.4. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}$, and $s \geq m$.
\begin{itemize}
\item[(a)] Suppose $u \in \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y)$. Then $u \in H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$ if and only if then $\left.\partial_{y}^{k} u\right|_{y=0}=0$ for $0 \leq k \leq m-1$.
\item[(b)] Suppose $u \in \mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)$. Then $u \in X_{m}^{s, p}(\mathbb{H} \mid y)$ if and only if $\left.\partial_{y}^{k} u\right|_{y=0}=0$ for $0 \leq k \leq m-1$.
\end{itemize}

Proof. We begin with part (a). For the forward direction, suppose $u \in H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$; we wish to show $\left.\partial_{y}^{k} u\right|_{y=0}=0$ for $k \leq m-1$. Since
$$\partial_{y}: \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y) \cap H_{m-n / p}^{s, p}(\mathbb{H} \mid y) \rightarrow \mathscr{H}^{s-1, p ; m-1}(\mathbb{H} \mid y) \cap H_{m-1-n / p}^{s-1, p}(\mathbb{H} \mid y)$$
an iterative argument shows it suffices to prove the result assuming $m=1$, and there is no loss of generality assuming $s=1$ as well.
Let $\chi:[0, \infty) \rightarrow \mathbb{R}$ be a smooth function that equals 1 on [0, 1] and equals 0 on [2, $\infty$ ). For a smooth function in $u \in \mathscr{H}^{1, p ; 1}(\mathbb{H} \mid y)$ an easy computation using Lemma 7.3 implies
$$\left\|u-\chi(y) u_{0}\right\|_{H_{1-n / p}^{0, p}(\mathbb{H} \mid y)} \lesssim\left\|\partial_{y} u\right\|_{H_{-n / p}^{0, p}(\mathbb{H} \mid y)}+\left\|u_{0}\right\|_{L^{p}\left(\mathbb{R}^{n-1}\right)},$$
where $u_{0}=\left.u\right|_{y=0}$. Since the smooth functions in $\mathscr{H}^{1, p ; 1}(\mathbb{H} \mid y)=W^{1, p}\left(\mathbb{R}_{+}^{n}\right)$ are dense, and since the right-hand side of the previous inequality is continuous on $\mathscr{H}^{1, p ; 1}(\mathbb{H} \mid y)$, the inequality holds for arbitrary elements of $\mathscr{H}^{1, p ; 1}(\mathbb{H} \mid y)$.
Now suppose $u \in \mathscr{H}^{1, p ; 1}(\mathbb{H} ; \mathbb{R}) \cap H_{1-n / p}^{0, p}(\mathbb{H} \mid y)$ and let $u_{0}=\left.u\right|_{y=0}$. We have just seen that $u-\chi u_{0} \in H_{1-n / p}^{0, p}(\mathbb{H} \mid y)$ and therefore $\chi u_{0} \in H_{1-n / p}^{0, p}(\mathbb{H} \mid y)$ as well. That is, $y^{-1} \chi u_{0} \in$ $L^{p}\left(\mathbb{R}_{+}^{n}\right)$. But $\chi=1$ in a neighborhood of $y=0$, so this is only possible if $\left\|u_{0}\right\|_{L^{p}\left(\mathbb{R}^{n-1}\right)}=0$. This completes the proof of the forward direction of part (a).
For the converse we begin by showing that $u \in H_{m-n / p}^{0, p}(\mathbb{H} \mid y)$. The proof is by induction on $m$ and the case $m=1$ follows from Lemma 7.3 and the observation that if $u \in \mathscr{H}^{s, p ; 1}(\mathbb{H} \mid y)$ then $\partial_{y} u \in H_{-n / p}^{0, p}(\mathbb{H} \mid y)$. Suppose the result holds for some $m \leq s-1$ and consider some $u \in \mathscr{H}^{s, p ; m+1}(\mathbb{H} \mid y)$ such that $\left.\partial_{y}^{k} u\right|_{y=0}=0$ for $0 \leq k \leq m$. Applying the inductive hypothesis to $\partial_{y} u \in \mathscr{H}^{s-1, p ; m}(\mathbb{H} \mid y)$ satisfying $\left.\partial_{y}^{j}\left(\partial_{y} u\right)\right|_{y=0}=0$ for $0 \leq j \leq m-1$ we conclude $\partial_{y} u \in H_{m-n / p}^{0, p}(\mathbb{H} \mid y)$. Lemma 7.3 then implies $u \in H_{m+1-n / p}^{0, p}(\mathbb{H} \mid y)$ as required.
To address the higher derivatives we note that since $u \in \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y)$,
$$\nabla_{\mathbb{E}}^{m} u \in H_{m-n / p}^{s-m, p}(\mathbb{H} \mid y) .$$
Since $u \in H_{m-n / p}^{0, p}(\mathbb{H} \mid y)$ as well, the analog of Lemma 3.9 discussed at the beginning of this section implies that $u \in H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$. This completes the proof of part (a).
To establish part (b) we first observe that although $X_{m}^{s, p}(\mathbb{H} \mid y)$ does not embed in $H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$ as is the case for standard Gicquaud-Sakovich spaces, it is easy to see that a function in $X_{m}^{s, p}(\mathbb{H} \mid y)$ with bounded support in $\mathbb{R}_{+}^{n}$ does indeed lie in $H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$. Consequently a function in $\mathscr{X}^{s, p ; m}(\mathbb{H} \mid y) \cap X_{m}^{s, p}(\mathbb{H} \mid y)$ with bounded support in $\mathbb{R}_{+}^{n}$ belongs to $\mathscr{H}^{s, p ; m}(\mathbb{H} \mid y) \cap$
$H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$. The forward direction of part (b) therefore reduces to part (a) via a local-ization argument, noting that vanishing trace is a local property. The converse direction is proved identically to part (a) using Lemma 7.2 in place of Lemma 7.3. \(\square\)
7.2. $\mathbb{H}$-mollification. Our asymptotic analysis uses a mollification procedure based on the group structure on $\mathbb{H}$, described in [AILSA18], given by the multiplication $(\xi, \eta) \cdot(x, y)=$ $(\xi+\eta x, \eta y)$. The identity element is $(0,1)$ and $(x, y)^{-1}=\left(-y^{-1} x, y^{-1}\right)$. Note that the inverse map $w \mapsto w^{-1}$ is a diffeomorphism $B_{r}^{\mathbb{H}} \rightarrow B_{r}^{\mathbb{H}}$ for each $r>0$.
For $z \in \mathbb{H}$, we denote the left multiplication map by $\Phi_{z}: w \mapsto z \cdot w$. Thus the Möbius parametrization $\Phi_{i}$ centered at $\left(x_{i}, y_{i}\right)$ is the restriction of $\Phi_{\left(x_{i}, y_{i}\right)}$ to $B_{2}^{\mathbb{H}}$. Note that $\breve{g}$ and the vector fields $y \partial_{x}, y \partial_{y}$ are left-invariant with respect to this group structure: for all $z \in \mathbb{H}$ we have $\Phi_{z}^{*} \breve{g}=\breve{g}, \Phi_{z}^{*}\left(y \partial_{x}\right)=y \partial_{x}$, and $\Phi_{z}^{*}\left(y \partial_{y}\right)=y \partial_{y}$.
Following [AILSA18], we define $\mathbb{H}$-convolution of $u \in C^{\infty}(\mathbb{H})$ with $\psi$ by
$$\begin{aligned}
(u * \psi)(z) & =\int_{\mathbb{H}} u(w) \psi\left(w^{-1} \cdot z\right) d V_{\breve{g}}(w) \\
& =\int_{\mathbb{H}} u(z \cdot w) \psi\left(w^{-1}\right) d V_{\breve{g}}(w)
\end{aligned}$$
For notational convenience we define $\psi^{\dagger}(w)=\psi\left(w^{-1}\right)$ in which case these formulas can be written
$$(u * \psi)(z)=\left\langle\Phi_{z}^{*} u, \psi^{\dagger}\right\rangle_{\left(M, g_{\mathrm{H}}\right)}=\left\langle u, \Phi_{z^{-1}}^{*} \psi^{\dagger}\right\rangle_{\left(M, g_{\mathrm{H}}\right)} .$$

Lemma 7.5. Suppose $\psi \in C_{\mathrm{cpct}}^{\infty}(M)$ and $u \in C^{\infty}(M)$.
\begin{itemize}
\item[(a)] $\operatorname{supp} u * \psi \subset \operatorname{supp} u \cdot \operatorname{supp} \psi=\{a \cdot b: a \in \operatorname{supp} u, b \in \operatorname{supp} v\}$.
\item[(b)] $\Phi_{z}^{*}(u * \psi)=\left(\Phi_{z}^{*} u\right) * \psi$ for all $z \in \mathbb{H}$.
\item[(c)] $(y \partial)^{\alpha}(u * \phi)=u *\left((y \partial)^{\alpha} \phi\right)$ for all multiindices $\alpha$.
\item[(d)] $\langle u * \psi, \phi\rangle_{(\mathbb{H}, \breve{g})}=\left\langle u, \phi * \psi^{\dagger}\right\rangle_{(\mathbb{H}, \breve{g})}$ for all $\phi \in C_{\mathrm{cpct}}^{\infty}(M)$.
\end{itemize}

Now suppose that $\psi \in C_{\text {cpct }}^{\infty}(M)$ and that $u$ is a distribution on $M$. Motivated by equation (7.15) we define
$$(u * \psi)(z)=\left\langle u, \Phi_{z^{-1}}^{*} \psi^{\dagger}\right\rangle .$$
Note that this is well defined since $\Phi_{z^{-1}}^{*} \psi^{\dagger}$ is smooth and compactly supported. Moreover, the continuity of $z \mapsto \Phi_{z^{-1}}^{*} \psi^{\dagger}$ in any $C^{k}(M)$ implies that $u * \psi$ is a continuous function.
In order to investigate the local effects of $\mathbb{H}$-convolution, we suppose that $\psi \in C_{\text {cpct }}^{\infty}\left(B_{r}^{\mathbb{H}}\right)$ for some $r>0$. Given a distribution $u \in H^{s, p}\left(B_{R+r}^{\mathbb{H}}\right)$ we define $u * \psi$ on $B_{R}^{\mathbb{H}}$ by $(u * \psi)(z)=$ $(\widetilde{u} * \psi)(z)$ where $\widetilde{u}$ is any compactly supported extension of $u$ in $H^{s, p}(\mathbb{H})$. One readily verifies that Lemma (7.5)(a) also holds for distributions and hence $u * \psi$ is well defined on $B_{R}^{\mathbb{H}}$.
The following lemma shows that $\mathbb{H}$-convolution locally improves regularity.

Lemma 7.6. Suppose $\psi \in C_{\text {cpct }}^{\infty}\left(B_{r}^{\mathbb{H}}\right)$ and that $u \in H^{s_{0}, p_{0}}\left(B_{R+r}^{\mathbb{H}}\right)$ for some $r, R>0, s_{0} \in \mathbb{R}$ and $1<p_{0}<\infty$. Then $u * \psi \in H^{s, p}\left(B_{R}^{\mathbb{H}}\right)$ for all $s \in \mathbb{R}$ and $1<p<\infty$ with
$$\|u * \psi\|_{H^{s, p}\left(B_{R}^{\mathbb{H}}\right)} \lesssim\|u\|_{H^{s_{0}, p_{0}}\left(B_{R+r}^{\mathbb{H}}\right)} .$$
The implicit constant is independent of $u$ but depends on all other data.
Proof. Suppose $u$ is smooth on $B_{R+r}^{\mathbb{H}}$. Direct computation shows that for $k \in \mathbb{N}$ we have
$$\left\|\Phi_{w}^{*} \psi\right\|_{C^{k}\left(B_{R+r}^{\mathbb{H}}\right)} \lesssim\|\psi\|_{C^{k}\left(B_{r}^{\mathbb{H}}\right)} \lesssim 1 .$$
where the implicit constants are independent of $w \in B_{r}^{\mathbb{H}}$. Since $z \in B_{r}^{\mathbb{H}}$ implies $z^{-1} \in B_{r}^{\mathbb{H}}$ we have, for $k \geq\left|s_{0}\right|$, that
$$|(u * \psi)(z)|=\left|\left\langle u, \Phi_{z^{-1}}^{*} \psi^{\dagger}\right\rangle\right| \lesssim\|u\|_{H^{s_{0}, p_{0}}\left(B_{R+r}^{\mathbb{H}}\right)}\|\psi\|_{C^{k}\left(B_{r}^{\mathbb{H}}\right)} \lesssim\|u\|_{H^{s_{0}, p_{0}}\left(B_{R+r}^{\mathbb{H}}\right)} .$$
For each multiindex $\alpha$ we have
$$\begin{aligned}
\left\|\left(\rho \partial_{\Theta}\right)^{\alpha}(u * \psi)\right\|_{L^{\infty}\left(B_{R}^{\mathbb{H}}\right)} & =\left\|u *\left(\left(\rho \partial_{\Theta}\right)^{\alpha} \psi\right)\right\|_{L^{\infty}\left(B_{R}^{\mathbb{H}}\right)} \\
& \lesssim\|u\|_{H^{s_{0}, p_{0}}\left(B_{R+r}^{\mathbb{H}}\right)}\|\psi\|_{C^{k+|\alpha|}\left(B_{r}^{\mathbb{H}}\right)} \\
& \lesssim\|u\|_{H^{s_{0}, p_{0}}\left(B_{R+r}^{\mathbb{H}}\right)} .
\end{aligned}$$
The lemma now follows for smooth functions from the norm equivalence (7.4) and holds generally by a density argument. \(\square\)

Extending the previous result to the global setting, $\mathbb{H}$-convolution with smooth compactly supported functions improves regularity while leaving decay rates at the boundary unchanged. For convenience, we restrict $\psi$ to be supported in a small ball so that its local effects can be observed within the domains of individual Möbius parametrization.

Proposition 7.7. Let $\psi \in C_{\text {cpct }}^{\infty}\left(B_{1 / 2}^{\mathbb{H}}\right)$ and suppose $s_{0} \in \mathbb{R}, 1<p_{0}<\infty$ and $\delta \in \mathbb{R}$.
\begin{itemize}
\item[(a)] If $u \in H_{\delta}^{s_{0}, p_{0}}(\mathbb{H} \mid y)$ then $u * \psi \in H_{\delta}^{s, p}(\mathbb{H} \mid y)$ for all $s \in \mathbb{R}$ and $p \geq p_{0}$, with
$$\|u * \psi\|_{H_{\delta}^{s, p}(\mathbb{H} \mid y)} \lesssim\|u\|_{H_{\delta}^{s_{0}, p_{0}}(\mathbb{H} \mid y)} .$$
\item[(b)] If $u \in X_{\delta}^{s_{0}, p_{0}}(\mathbb{H} \mid y)$ then $u * \psi \in X_{\delta}^{s, p}(\mathbb{H} \mid y)$ for all $s \in \mathbb{R}$ and $1<p<\infty$, with
$$\|u * \psi\|_{X_{\delta}^{s, p}(\mathbb{H} \mid y)} \lesssim\|u\|_{X_{\delta}^{s_{0}, p_{0}}(\mathbb{H} \mid y)} .$$
\item[(c)] If $u \in \mathscr{H}^{m, p_{0} ; m}(\mathbb{H} \mid y)$ for some $m \in \mathbb{N}$, then $u * \psi \in \mathscr{H}^{s, p_{0} ; m}(\mathbb{H} \mid y)$ for all $s \geq m$, with
$$\|u * \psi\|_{\mathscr{H}^{s, p_{0} ; m}(\mathbb{H} \mid y)} \lesssim\|u\|_{\mathscr{H}^{m, p_{0} ; m}(\mathbb{H} \mid y) .} .$$
\item[(d)] If $u \in \mathscr{X}^{m, p_{0} ; m}(\mathbb{H} \mid y)$ for some $m \in \mathbb{N}$, then $u * \psi \in \mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)$ for all $s \geq m$ and $1<p<\infty$, with
$$\|u * \psi\|_{\mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)} \lesssim\|u\|_{\mathscr{X}^{m, p_{0} ; m}(\mathbb{H} \mid y)} .$$
\end{itemize}
The implicit constants above are independent of $u$ and $\delta$, but depend on $\psi, s_{0}, p_{0}, s, p$, and $m$.

Proof. For each Möbius parametrization $\Phi_{i}$, Lemmas 7.5(b) and 7.6 imply
$$\left\|\Phi_{i}^{*}(u * \psi)\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)}=\left\|\left(\Phi_{i}^{*} u\right) * \psi\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\Phi_{i}^{*} u\right\|_{H^{s_{0}, p_{0}}\left(B_{3 / 2}^{\mathbb{H}}\right)} .$$
Recalling (7.1), part (a) follows from the inclusion $\ell^{p_{0}} \hookrightarrow \ell^{p}$, while part (b) is immediate.
To establish part (c), we first apply coordinate derivatives $\partial_{x}$ and $\partial_{y}$ to (7.14) in order to see that for each multiindex $\alpha$ there exist functions $\psi^{\alpha, \beta} \in C_{\mathrm{cpct}}^{\infty}\left(B_{1 / 2}^{\mathbb{H}}\right)$ such that
$$\partial^{\alpha}(u * \psi)=\sum_{|\beta|=|\alpha|}\left(\partial^{\beta} u\right) * \psi^{\alpha, \beta} ;$$
see also [AILSA18, Lemma 2.7]. Thus the norm equivalences (7.3) imply
$$\begin{aligned}
\|u * \psi\|_{\mathscr{H} e^{s, p ; m}(\mathbb{H} \mid y)} & \lesssim \sum_{|\alpha| \leq m}\left\|\partial^{\alpha}(u * \psi)\right\|_{H_{-n / p}^{s-|\alpha|, p}(\mathbb{H} \mid y)} \\
& \leq \sum_{|\alpha| \leq m} \sum_{|\beta|=|\alpha|}\left\|\left(\partial^{\beta} u\right) * \psi^{\alpha, \beta}\right\|_{H_{-n / p}^{s-|\alpha|, p}(\mathbb{H} \mid y)} .
\end{aligned}$$
Applying part (a) yields the desired result; part (d) follows similarly. \(\square\)

We highlight the subtle changes in the hypotheses concerning the Lebesgue parameter $p$ in the various cases of Proposition 7.7. In part (a) the assumption $p \geq p_{0}$ arises simply because $\ell^{p_{0}} \not \subset \ell^{p}$ for $p<p_{0}$, and it is easy to verify that it is necessary. There is no analogous restriction in part (b) because $\ell^{\infty}$ replaces the role of $\ell^{p}$ regardless of the value of $p$. In part (c) the Lebesgue parameter is fixed at $p=p_{0}$ and this is also necessary. It cannot be lowered because of the obstacle in part (a), and considerations at the boundary imply that it cannot be raised. Indeed, first recall that $\mathscr{H}^{m, p_{0} ; m}(\mathbb{H} \mid y)=W^{m, p_{0}}\left(\mathbb{R}_{+}^{n}\right)$. If $\mathbb{H}$-mollification were able to improve $p_{0}$ to some $p>p_{0}$, this would imply an increase of boundary regularity to that of $W^{m, p}\left(\mathbb{R}_{+}^{n}\right)$ functions. But it follows from Proposition 7.4 along with Lemma 7.9 proved below that $\mathbb{H}$-convolution can modify boundary traces at most by multiplication by a constant. Hence no improvement in $p$ is possible. By contrast, the fact that $\mathbb{H}$-mollification takes $\mathscr{X}^{1, p_{0}, 1}(\mathbb{H} \mid y)$ to $\mathscr{X}^{\infty ; 1}(\mathbb{H} \mid y)$ regardless of the value of $p_{0}$ indicates that of elements of $\mathscr{X}^{1, p_{0} ; 1}(\mathbb{H} \mid y)$ intrinsically have a large amount of boundary regularity. See, e.g., Corollary 4.9.

To investigate the effect of $\mathbb{H}$-convolution at the boundary it is helpful to restrict our attention to functions $\psi \in C_{\text {cpct }}^{\infty}\left(B_{1 / 2}^{\mathbb{H}}\right)$ that additionally satisfy
$$\int_{B_{1 / 2}^{\mathrm{H}}} \psi^{\dagger} d V_{\breve{g}}=1$$
in which case we refer to $u * \psi$ as the II-mollification of $u$. Proposition 7.7 implies that $\mathbb{H}$-mollification is regularity improving inside $\mathbb{H}$, and we now wish to show that it simultaneously leaves boundary traces unaffected. As an initial step, we have the following analogue of a standard fact about ordinary mollification.

Lemma 7.8. Suppose $\psi \in C_{\mathrm{cpct}}^{\infty}\left(B_{1 / 2}^{\mathbb{H}}\right)$ and that $\int_{B_{1 / 2}^{\mathbb{H}}} \psi^{\dagger} d V_{\tilde{g}}=1$. For all $1<p<\infty$, if $u \in H^{1, p}\left(B_{3 / 2}^{\mathbb{H}}\right)$ then
$$\|u * \psi-u\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\|d u\|_{L^{p}\left(B_{3 / 2}^{\mathbb{H}}\right)} .$$
Proof. Let $R_{w}$ denote right multiplication by $w$. We claim that
$$\left\|R_{w}^{*} u-u\right\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\|d u\|_{L^{p}\left(B_{3 / 2}^{\mathbb{H}}\right)}$$
with the implicit constant independent of $w \in B_{1}^{\mathbb{H}}$. Assuming (7.16) for the moment, and using that $\int \psi^{\dagger} d V_{\check{g}}=1$, we find
$$\begin{aligned}
\int_{B_{1}^{\mathrm{H}}}|u * \psi-u|^{p} d V_{\breve{g}} & =\int_{B_{1}^{\mathbb{H}}}\left|\int_{B_{1 / 2}^{\mathbb{H}}}[u(y \cdot w)-u(y)] \psi\left(w^{-1}\right) d V_{\breve{g}}(w)\right|^{p} d V_{\breve{g}}(y) \\
& \leq \int_{B_{1 / 2}^{\mathbb{H}}} \int_{B_{1}^{\mathbb{H}}}\left|[u(y \cdot w)-u(y)] \psi\left(w^{-1}\right)\right|^{p} d V_{\breve{g}}(y) d V_{\breve{g}}(w) \\
& \lesssim \sup _{w \in B_{1 / 2}^{\mathbb{H}}}\left\|R_{w}^{*} u-u\right\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)}^{p} \\
& \lesssim\|d u\|_{L^{p}\left(B_{3 / 2}^{\mathbb{H}}\right)}^{p} .
\end{aligned}$$
So it only remains to establish inequality (7.16).
Suppose that $u$ is smooth. Fix $w=(x, y) \in B_{1 / 2}^{\mathbb{H}}$ and let $\gamma:[0,1] \rightarrow B_{1}^{\mathbb{H}}$ be the curve $\gamma(t)=\left(t x, y^{t}\right)$. Direct computation shows that
$$\left|R_{w}^{*} u(z)-u(z)\right|^{p}=\left|\int_{0}^{1} \frac{d}{d t} u(z \cdot \gamma(t)) d t\right|^{p} \lesssim \int_{0}^{1}\left|d u_{z \cdot \gamma(t)}\right|_{\breve{g}}^{p} d t$$
with implicit constant independent of $u \in W^{1, p}\left(B_{3 / 2}^{\mathbb{H}}\right), w \in B_{3 / 2}^{\mathbb{H}}$ and $z \in B_{1}^{\mathbb{H}}$. Although $\breve{g}$ is not invariant with respect to right multiplication, a compactness argument shows that $d V_{\breve{g}} \lesssim R_{w}^{*} d V_{\breve{g}}$ and $R_{w}^{*} \breve{g} \lesssim \breve{g} \lesssim R_{w}^{*} \breve{g}$ with implicit constants independent of $w \in B_{1 / 2}^{\mathbb{H}}$. Therefore
$$\begin{aligned}
\int_{B_{1}^{\mathrm{H}}}\left|R_{w}^{*} u-u\right|^{p} d V_{\breve{g}} & \lesssim \int_{B_{1}^{\mathrm{H}}} \int_{0}^{1}\left|d u_{z \cdot \gamma(t)}\right|_{\breve{g}}^{p} d t d V_{\breve{g}}(z) \\
& \lesssim \int_{0}^{1} \int_{R_{\gamma(t)}\left(B_{1}^{\mathbb{H}}\right)}\left|d u_{z}\right|_{\breve{g}}^{p} d V_{\breve{g}}(z) d t \\
& \lesssim \int_{B_{3 / 2}^{\mathrm{H}}}|d u|_{\breve{g}}^{p} d V_{\breve{g}} .
\end{aligned}$$
Hence inequality (7.16) holds for smooth functions and holds generally by a density argument. \(\square\)

The following result shows that $\mathbb{H}$-mollification preserves boundary values in the sense of an improved decay rate; in combination with Proposition 7.4 we conclude that $\mathbb{H}$-mollification preserves boundary traces.

Lemma 7.9. Suppose $\psi \in C_{\text {cpct }}^{\infty}(M)$ and that $\int_{B_{1 / 2}^{\mathbb{H}}} \psi^{\dagger} d V_{\breve{g}}=1$.
\begin{itemize}
\item[(a)] If $u \in \mathscr{H}^{s, p ; 1}(\mathbb{H} \mid y)$ for some $s \geq 1$ and $1<p<\infty$, then
$$u * \psi-u \in H_{1-n / p}^{s, p}(\mathbb{H} \mid y)$$
and
$$\|u * \psi-u\|_{H_{1-n / p}^{s, p}(\mathbb{H} \mid y)} \lesssim\|u\|_{\mathscr{H}^{s, p ; 1}(\mathbb{H} \mid y)} .$$
\item[(b)] If $u \in \mathscr{X}^{s, p ; 1}(\mathbb{H} \mid y)$ for some $s \geq 1$ and $1<p<\infty$ then
$$u * \psi-u \in X_{w+1}^{s, p}(\mathbb{H} \mid y)$$
and
$$\|u * \psi-u\|_{X_{1}^{s, p}(\mathbb{H} \mid y)} \lesssim\|u\|_{\mathscr{X}^{s, p ; 1}(\mathbb{H} \mid y)} .$$
\end{itemize}
Proof. We prove (a); the proof of (b) is similar and a bit simpler.
Suppose $u \in \mathscr{H}^{s, p ; 1}(\mathbb{H} \mid y)$, so $u \in H_{-n / p}^{s, p}(\mathbb{H} \mid y)$ and $d u \in H_{1-n / p}^{s-1, p}(\mathbb{H} \mid y)$. Then the properties of convolution and 7.8 imply
$$\begin{aligned}
\|u * \psi-u\|_{L_{1-n / p}^{p}(\mathbb{H} \mid y)}^{p} & \lesssim \sum_{i} y_{i}^{-p+n}\left\|\Phi_{i}^{*}(u * \psi)-\Phi_{i}^{*} u\right\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)}^{p} \\
& \left.\lesssim \sum_{i} y_{i}^{-p+n}\left\|\left(\Phi_{i}^{*} u\right) * \psi-\Phi_{i}^{*} u\right\|_{L^{p}\left(B_{1}^{\mathbb{H}}\right)}^{p}\right) \\
& \lesssim \sum_{i} y^{-p+n}\left\|d\left(\Phi_{i}^{*} u\right)\right\|_{L^{p}\left(B_{3 / 2}^{\mathbb{H}}\right)}^{p} \\
& =\sum_{i} y^{-p+n}\left\|\Phi_{i}^{*} d u\right\|_{L^{p}\left(B_{3 / 2}^{\mathbb{H}}\right)}^{p} \\
& \lesssim\|d u\|_{L_{1-n / p}^{p}(\mathbb{H} \mid y)}^{p} \\
& \lesssim\|u\|_{\mathscr{H}^{s, p ; 1}(\mathbb{H} \mid y)}^{p} .
\end{aligned}$$
On the other hand, since $u \in \mathscr{H}^{s, p ; 1}(\mathbb{H} \mid y)$, Proposition 7.7(a) implies $d(u * \psi) \in H_{1-n / p}^{s-1, p}(\mathbb{H} \mid y)$ with norm controlled by the $H_{1-n / p}^{s-1, p}$ norm of $u$. That is,
$$\begin{aligned}
u * \psi-u & \in H_{1-n / p}^{0, p}(\mathbb{H} \mid y) \\
d(u * \psi-u) & \in H_{1-n / p}^{s-1, p}(\mathbb{H} \mid y)
\end{aligned}$$
with both norms controlled by the $\mathscr{H}^{s, p ; 1}(\mathbb{H} \mid y)$ norm of $u$. The result now follows from the analog of Lemma 3.9 discussed at the beginning of this section. \(\square\)
7.3. Asymptotic structure. We now turn to the construction of asymptotic expansions and begin with a technical lemma used to ensure $\partial_{y}$ derivatives of coefficient functions appearing in the expansions can be arranged to vanish to high order.