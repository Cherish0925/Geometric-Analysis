---
retention_scope: session
part: 2
total_parts: 7
---

[Part 2/7 of: Sobolev-classasymptoticallyhyperbolicmanifolds and]

Proof. We prove the result for $H_{\delta}^{s, p}(M)$; the Gicquaud-Sakovich case is proved analogously.
Let $\chi$ be a cutoff function that equals 1 on $B_{1 / 2}^{\mathbb{H}}$ that is supported on $B_{1}^{\mathbb{H}}$ and let $\eta$ be a cutoff function that equals 1 on $B_{1}^{\mathbb{H}}$ that is supported in $B_{2}^{\mathbb{H}}$. Part (b) is a consequence of Theorem

1 of [Sic96] (see also §3.1 of [Tay91]), which implies that for a Möbius parametrization $\Phi_{i}$
$$\begin{aligned}
\left\|\chi \Phi_{i}^{*} F(u)\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} & =\left\|\chi F\left(\eta \Phi_{i}^{*} u\right)\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \\
& \lesssim\left\|F\left(\eta \Phi_{i}^{*} u\right)\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \\
& \lesssim\left\|\eta \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}\left(1+\left\|\eta \Phi_{i}^{*} u\right\|_{L^{o}\left(\mathbb{R}^{n}\right)}^{k+\alpha}\right),
\end{aligned}$$
where the implicit constants depend on $\chi$ and on a choice of interval $[-K, K]$ containing $u(M)$. Since $\delta \geq 0$ and $s>n / p$, Sobolev embedding implies $H_{\delta}^{s, p}(M ; E) \hookrightarrow C_{0}^{0}(M ; E)$ and hence the $L^{\infty}$ norms appearing in this expression are uniformly bounded independent of $i$. Part (a) now follows from multiplying by $\rho_{i}$ and summing $p^{\text {th }}$ powers. \(\square\)

If the domain of $F$ in Proposition 3.19 is only an interval containing 0, it is easy to see that the conclusion still holds for a function $u$ having image contained in a compact set in the domain of $F$. We will use this variation of Proposition 3.19 without comment.

Proposition 3.19 requires the hypothesis $F(0)=0$ to ensure $F(u)$ decays at infinity when $u$ does. If we drop this hypothesis we find instead $F(u)$ lies in a Gicquaud-Sakovich space.

Corollary 3.20. Suppose $1<p<\infty, s \geq 1, s>n / p$ and $\delta \geq 0$. Let $F \in C^{k, \alpha}(\mathbb{R})$ for some $k \in \mathbb{N}$ and $\alpha \in[0,1)$ with $k+\alpha>s$.
\begin{itemize}
\item[(a)] If $u \in H_{\delta}^{s, p}(M ; \mathbb{R})$ then $F(u) \in X_{0}^{s, p}(M ; \mathbb{R})$.
\item[(b)] If $u \in X_{\delta}^{s, p}(M ; \mathbb{R})$ then $F(u) \in X_{0}^{s, p}(M ; \mathbb{R})$.
\end{itemize}

Proof. From the continuous embedding $H_{\delta}^{s, p}(M) \subset X_{\delta}^{s, p}(M)$ from Lemma 3.2, it suffices to establish part (b) and we assume $u \in X_{\delta}^{s, p}(M)$ Write $F=F(0)+\hat{F}$, so $\hat{F}(0)=0$. Proposition 3.19(b) shows $\hat{F}(u) \in X_{\delta}^{s, p}(M) \subset X_{0}^{s, p}(M)$. But then $F(u)=\hat{F}(u)+F(0) \in$ $X_{0}^{s, p}(M)$ as well. \(\square\)

\section*{4. Fortified spaces on $\bar{M}$}

As discussed in the introduction, elliptic problems on asymptotically hyperbolic manifolds lead to the consideration of metrics on $M$ that have a high level of regularity, but whose compactifications have a lesser amount of regularity up to the boundary of $\bar{M}$. In this section, building on prior work in [AILSA18] in the Hölder category, we describe two new families of function spaces on $\bar{M}$ that are suitable for describing such compactified metrics. Each of these spaces resides in some $H^{m, p}(\bar{M})$, which can be thought of as a baseline level of smoothness, and then possesses additional regularity measured using weighted spaces on $M$.

We begin by recalling the spaces constructed in [AILSA18]. For a tensor bundle $E$ over $\bar{M}$ of weight $w$, Lemma 3.15 implies that $C^{k, \alpha}(\bar{M} ; E) \subset C_{w}^{k, \alpha}(M ; E)$. Both of these spaces ensure their elements have $k+\alpha$ interior derivatives and can be thought of as two endpoints with respect to a spectrum of boundary regularity. Whereas functions in $C^{k, \alpha}(\bar{M} ; E)$ have $k+\alpha$ derivatives up to the boundary, a traveling bump argument shows that functions in
$C_{w}^{k, \alpha}(M ; E)$ need not admit even a continuous extension to $\bar{M}$. Building on these observations, we have a family of of function spaces that are intermediate between $C_{w}^{k, \alpha}(M ; E)$ and $C^{k, \alpha}(\bar{M} ; E)$ : given $\alpha \in[0,1]$ and $k, m \in \mathbb{N}_{\geq 0}$ with $m \leq k$, the space $\mathscr{C}^{k, \alpha ; m}(M ; E)$ is defined by the norm
$$\|u\|_{\mathscr{C}^{k, \alpha ; m}(M ; E)}=\sum_{j=0}^{m}\left\|\hat{\nabla}^{j} u\right\|_{C_{w+j}^{k-j, \alpha}\left(M ; T^{0, j} M \otimes E\right)} .$$
The parameter $k$ controls the amount of interior regularity, while $m$ allows for a limited amount of regularity at the boundary. When $m \geq 1$, functions in $\mathscr{C}^{k, \alpha ; m}(M ; E)$ lie in $C^{m-1,1}(\bar{M} ; E)$ [AILSA18, Lemma 2.3(c)] and hence nearly possess $m$ derivatives up to the boundary.

We introduce two related families of functions spaces motivated by the embeddings from Proposition 3.17:
$$\begin{aligned}
& H^{s, p}(\bar{M} ; E) \hookrightarrow H_{w-n / p}^{s, p}(M ; E), \\
& H^{s, p}(\bar{M} ; E) \hookrightarrow X_{w}^{s, p}(M ; E) .
\end{aligned}$$

Definition 4.1. Suppose $1<p<\infty, s \in \mathbb{R}$, and $m \in \mathbb{N}_{\geq 0}$ with $s \geq m$. Let $E$ be a tensor bundle over $M$ with weight $w$. The fortified spaces $\mathscr{H}^{s, p ; m}(M ; E)$ and $\mathscr{X}^{s, p ; m}(M ; E)$ consist of the distributional-valued sections of $E$ such that the following norms are finite:
$$\begin{aligned}
& \|u\|_{\mathscr{H} \mathscr{E}^{s, p ; m}(M ; E)}=\sum_{j=0}^{m}\left\|\hat{\nabla}^{j} u\right\|_{H_{w+j-n / p}^{s-j, p}}\left(M ; T^{0, j} M \otimes E\right), \\
& \|u\|_{\mathscr{X}^{s, p ; m}(M ; E)}=\sum_{j=0}^{m}\left\|\hat{\nabla}^{j} u\right\|_{X_{w+j}^{s-j, p}\left(M ; T^{0, j} M \otimes E\right)} .
\end{aligned}$$
We obtain spaces of smooth functions in the usual way by intersecting the corresponding spaces with finite regularity. Specifically,
$$\begin{aligned}
\mathscr{H}^{\infty, p ; m}(M ; E) & =\bigcap_{s \in \mathbb{R}} \mathscr{H}^{s, p ; m}(M ; E), \\
\mathscr{C}^{\infty ; m}(M ; E) & =\bigcap_{\substack{k \in \mathbb{N} \\
\alpha \in[0,1]}} \mathscr{C}^{k, \alpha ; m}(M ; E) .
\end{aligned}$$
In the same way that the Hölder parameter $\alpha$ plays no essential role in this latter intersection, an easy application of Sobolev embedding shows that the Lebesgue parameter $p$ is irrelevant in the Gicquaud-Sakovitch case; thus we define
$$\mathscr{X}^{\infty ; m}(M ; E)=\bigcap_{s \in \mathbb{R}} \mathscr{X}^{s, p ; m}(M ; E)$$
regardless of the value of $p$. In fact, $\mathscr{X}^{\infty ; m}(M ; E)=\mathscr{C}^{\infty ; m}(M ; E)$ but we use the notation $\mathscr{X}^{\infty ; m}(M ; E)$ in settings where it is helpful to emphasize the space's origins.

Fortified spaces can be thought of as weighted interior spaces with enhanced regularity at the boundary. The baseline interior regularity follows from the inclusions $\mathscr{H}^{s, p ; m}(M ; E) \hookrightarrow$ $H_{w-n / p}^{s, p}(M ; E)$ and $\mathscr{X}^{s, p ; m}(M ; E) \hookrightarrow X_{w}^{s, p}(M ; E)$ which are immediate from the definition. The following elementary relations, which are easy consequences of Lemmas 3.2 and 3.9, demonstrate one facet of the enhanced boundary regularity.

Lemma 4.2. Suppose $1<p<\infty, m \in \mathbb{N}_{\geq 0}$, and $s \in \mathbb{R}$ with $s \geq m$. For any tensor bundle E over $\bar{M}$,
$$\mathscr{X}^{s, p ; m}(M ; E) \hookrightarrow \mathscr{H}^{s, p ; m}(M ; E) \hookrightarrow \mathscr{H}^{m, p ; m}(M ; E)=H^{m, p}(\bar{M} ; E) .$$
Additionally, if $k \in \mathbb{N}_{\geq 0}$ with $k \geq m$, then
$$\mathscr{C}^{k, \alpha ; m}(M ; E) \hookrightarrow \mathscr{X}^{k, p ; m}(M ; E)$$
for all $0 \leq \alpha \leq 1$.
As a consequence, every fortified space is a subspace of some $H^{m, p}(\bar{M} ; E)$. Thus we can interpret fortified spaces as being a Sobolev space on $\bar{M}$ supplemented with additional smoothness in the interior. For $\mathscr{H}^{k, p ; m}(M ; E)$ with $k \in \mathbb{N}$ it is straightforward to interpret this additional regularity. Lemmas 4.3 and 4.4 below imply
$$\|u\|_{\mathscr{H} k, p ; m(M ; E)} \sim \sum_{j=0}^{k-m}\left\|(\rho \hat{\nabla})^{j} u\right\|_{H^{m, p}\left(\bar{M} ; T^{0, j} \bar{M} \otimes E\right)},$$
and therefore an element of $\mathscr{H}^{k, p ; m}(M ; E)$ has $m$ derivatives up to the boundary, and an additional $k-m$ interior derivatives that are each allowed to blow up by a factor of $\rho^{-1}$ beyond what $L^{p}(\bar{M} ; E)$ allows. The additional regularity afforded by $\mathscr{X}^{s, p ; m}(M ; E)$, beyond what its inclusion in $\mathscr{H}^{s, p ; m}(M ; E)$ implies, is less transparent but is remarkably strong. For example, we show in Corollary 4.9 that the boundary trace of $u \in \mathscr{X}^{1, p ; 1}(M ; E)$ is Lipschitz regardless of the value of $1<p<\infty$.
4.1. Mapping properties of $\hat{\nabla}$ and $\rho$. The following lemma justifies the following general principles: multiplication by $\rho$ improves boundary regularity, $\hat{\nabla}$ removes a degree of both interior and boundary differentiability, and $\rho \hat{\nabla}$ only removes interior regularity.

Lemma 4.3. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}$ and $s \geq m$, and let $E$ be a tensor bundle of weight $w$ over $M$. The following maps are continuous between the spaces indicated.
\begin{itemize}
\item[(a)] $u \mapsto \rho u$ :
$$\begin{aligned}
& \mathscr{H}^{s, p ; m-1}(M ; E) \rightarrow \mathscr{H}^{s, p ; m}(M ; E), \\
& \mathscr{X}^{s, p ; m-1}(M ; E) \rightarrow \mathscr{X}^{s, p ; m}(M ; E) .
\end{aligned}$$
\item[(b)] $u \mapsto \hat{\nabla} u$ :
$$\begin{aligned}
& \mathscr{H}^{s, p ; m}(M ; E) \rightarrow \mathscr{H}^{s-1, p ; m-1}\left(M ; T^{0,1} M \otimes E\right), \\
& \mathscr{X}^{s, p ; m}(M ; E) \rightarrow \mathscr{X}^{s-1, p ; m-1}\left(M ; T^{0,1} M \otimes E\right) .
\end{aligned}$$
\end{itemize}
\begin{itemize}
\item[(c)] $u \mapsto \rho \hat{\nabla} u$ :
$$\begin{aligned}
& \mathscr{H}^{s, p ; m-1}(M ; E) \rightarrow \mathscr{H}^{s-1, p ; m-1}\left(M ; T^{0,1} M \otimes E\right), \\
& \mathscr{X}^{s, p ; m-1}(M ; E) \rightarrow \mathscr{X}^{s-1, p ; m-1}\left(M ; T^{0,1} M \otimes E\right) .
\end{aligned}$$
\end{itemize}
Proof. The proofs for the Sobolev and Gicquaud-Sakovich cases are similar and we treat the Sobolev case. For part (a) consider some $0 \leq j \leq m$ and observe that
$$\hat{\nabla}^{j}(\rho u)=\sum_{a+b=j}\binom{j}{a} \hat{\nabla}^{a} \rho \hat{\nabla}^{b} u .$$
Since $\hat{\nabla}^{a} \rho$ is a tensor of weight $a$ and smooth on $\bar{M}$, it lies in $C_{a}^{\infty}(M)$
Consequently, Lemma 3.2 and Proposition 3.11 imply
$$\left\|\hat{\nabla}^{a} \rho \hat{\nabla}^{b} u\right\|_{H_{w+j-n / p}^{s-j, p}}(M) \lesssim\left\|\hat{\nabla}^{b} u\right\|_{H_{w+b-n / p}^{s-j, p}}(M) \lesssim\left\|\hat{\nabla}^{b} u\right\|_{H_{w+b-n / p}^{s-b, p}}(M) \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M)},$$
which proves the result.
Part (b) is immediate from the definition. Part (c) follows from parts (a) and (b) except in the case $m=1$, which uses Lemma 3.7 in place of part (b). \(\square\)

Note that $\mathscr{H}^{s, p ; 0}(M ; E)=H_{w-n / p}^{s, p}(M ; E)$ and that $\mathscr{X}^{s, p ; 0}(M ; E)=X_{w-n / p}^{s, p}(M ; E)$, the least regular spaces in the spectrum measured by the parameter $m$. Starting from $\mathscr{H}^{s, p ; 0}(M ; E)=$ $H_{w-n / p}^{s, p}(M ; E)$ and multiplying by $\rho^{m}$ it follows from repeated applications of Lemma 4.3(a) that $H_{w+m-n / p}^{s, p}(M ; E) \subset \mathscr{H}^{s, p ; m}(M ; E)$, so long as $s \geq m$. This inclusion is strict, however, and in §4.4 we show that $H_{w+1-n / p}^{s, p}(M ; E)$ is exactly the subset of $\mathscr{H}^{s, p ; m}(M ; E)$ that vanishes on the boundary.

The following variation of Lemma 3.9 emphasizes the principle that interior regularity is measured by applying $\rho \hat{\nabla}$.

Lemma 4.4. Let $E$ be a tensor bundle over $M$. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}_{\geq 0}$, and $s \geq m$.
\begin{itemize}
\item[(a)] Suppose $u \in \mathscr{H}^{s, p ; m}(M ; E)$ and $\rho \hat{\nabla} u \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,1} M \otimes E\right)$. Then $u \in$ $\mathscr{H}^{s+1, p ; m}(M ; E)$ and
$$\|u\|_{\mathscr{H}^{s+1, p ; m}(M ; E)} \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M ; E)}+\|\rho \hat{\nabla} u\|_{\mathscr{H}^{s, p ; m}\left(M ; T^{0,1} M \otimes E\right)} .$$
\item[(b)] Suppose $u \in \mathscr{X}^{s, p ; m}(M ; E)$ and $\rho \hat{\nabla} u \in \mathscr{X}^{s, p ; m}\left(M ; T^{0,1} M \otimes E\right)$. Then $u \in \mathscr{X}^{s+1, p ; m}(M ; E)$ and
$$\|u\|_{\mathscr{X}^{s+1, p ; m}(M ; E)} \lesssim\|u\|_{\mathscr{X}^{s, p ; m}(M ; E)}+\|\rho \hat{\nabla} u\|_{\mathscr{X}^{s, p ; m}\left(M ; T^{0,1} M \otimes E\right)} .$$
\end{itemize}

Proof. Suppose $0 \leq k \leq m$. From Lemma 3.9 we have
$$\begin{aligned}
\left\|\hat{\nabla}^{k} u\right\|_{H_{w+k-n / p}^{s-k+1-n / p, p}(M)} & \lesssim\left\|\hat{\nabla}^{k} u\right\|_{H_{w+k-n / p}^{s-k, p}}(M)+\left\|\hat{\nabla}^{k+1} u\right\|_{H_{w+k-n / p}^{s-k, p}}(M) \\
& \leq\|u\|_{\mathscr{H}^{s, p ; m}(M)}+\left\|\hat{\nabla}^{k+1} u\right\|_{H_{w+k-n / p}^{s-k, p}}(M)
\end{aligned}$$

So to establish part (a) it suffices to show
$$\left\|\hat{\nabla}^{k+1} u\right\|_{H_{w+k-n / p}^{s-k, p}(M)} \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M)}+\|\rho \hat{\nabla} u\|_{\mathscr{H}^{s, p ; m}(M)} .$$
Since $\left[\hat{\nabla}^{k}, \rho\right]=\sum_{j=0}^{k-1}\binom{k}{j} \hat{\nabla}^{k-j} \rho \hat{\nabla}^{j}$ and since, as argued in Lemma 4.3, each $\hat{\nabla}^{k-j} \rho \in$ $C_{k-j}^{\infty}\left(M ; T^{0, k-j} M\right)$ we find
$$\begin{aligned}
\left\|\left[\hat{\nabla}^{k}, \rho\right] \hat{\nabla} u\right\|_{H_{w+k+1-n / p}^{s-k, p}}(M) & \lesssim \sum_{j=0}^{k-1}\left\|\hat{\nabla}^{j+1} u\right\|_{H_{w+j+1-n / p}^{s-k, p}}(M) \\
& \lesssim \sum_{j=0}^{k-1}\left\|\hat{\nabla}^{j+1} u\right\|_{H_{w+j+1-n / p}^{s-(j+1), p}}(M) \\
& \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M)} .
\end{aligned}$$
Hence
$$\begin{aligned}
\left\|\hat{\nabla}^{k+1} u\right\|_{H_{w+k-n / p}^{s-k, p}(M)} & =\left\|\rho \hat{\nabla}^{k+1} u\right\|_{H_{w+k+1-n / p}^{s-k, p}}(M) \\
& \lesssim\left\|\hat{\nabla}^{k}(\rho \hat{\nabla} u)\right\|_{H_{w+1+k-n / p}^{s-k, p}}(M)+\|u\|_{\mathscr{H}^{s, p ; m}(M)} \\
& \lesssim\|\rho \hat{\nabla} u\|_{\mathscr{H}^{s, p ; m}(M)}+\|u\|_{\mathscr{H}^{s, p ; m}(M)},
\end{aligned}$$
which establishes the desired estimate (4.5). Part (b)is proved similarly. \(\square\)
4.2. Relationships with weighted spaces on $M$. The following elementary embeddings follow from the definition of the spaces and the discussion following Lemma 4.3.

Lemma 4.5. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}_{\geq 0}$, and $s \geq m$; let $E$ be a tensor bundle of weight $w$ over $M$. Then
$$\begin{aligned}
H_{w+m-n / p}^{s, p}(M ; E) & \subset \mathscr{H}^{s, p ; m}(M ; E) \subset H_{w-n / p}^{s, p}(M ; E), \\
X_{w+m}^{s, p}(M ; E) & \subset \mathscr{X}^{s, p ; m}(M ; E) \subset X_{w}^{s, p}(M ; E) .
\end{aligned}$$
In our applications, embeddings into $X_{w}^{s, p}(M ; E)$ are especially important. Recall that in §3.7 we developed function spaces of sections of a geometric tangent bundle associated with a metric $g$ so long as the metric satisfied the following regularity conditions:
\begin{itemize}
\item[(a)] $g \in X_{0}^{s, p}\left(M ; T^{0,2} M\right)$ with $s>n / p$ and $s \geq 1$,
\item[(b)] $\bar{g}=\rho^{2} g$ admits a continuous extension to $\bar{M}$.
\end{itemize}
We now establish that asymptotically hyperbolic metrics of class (1.3) or (1.4) satisfy these conditions. Continuity at the boundary is addressed in §4.3, thus we focus here on condition (a). Lemma 4.5 implies that if $\bar{g} \in \mathscr{X}^{s, p ; m}\left(M ; T^{0,2} M\right)$ then $g=\rho^{-2} \bar{g} \in X_{0}^{s, p}\left(M ; T^{0,2} M\right)$. Thus $g$ satisfies (a) if $s>n / p$ and $s \geq m \geq 1$.
The situation for a metric with $\bar{g} \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,2} M\right)$ is somewhat different. In this case, Lemma 4.5, in combination with Lemma 3.2, only yields $g \in H_{-n / p}^{s, p}\left(M ; T^{0,2} M\right)$, which
embeds into $X_{-n / p}^{s, p}\left(M ; T^{0,2} M\right)$, the key issue being the decay parameter $-n / p$. One would like to raise this value to 0, not only for the considerations above, but also to obtain good mapping properties of associated differential operators. For example, a computation using Proposition 3.11 shows that if $s>n / p$ then the Laplacian of a metric in $X_{-n / p}^{s, p}\left(M ; T^{0,2} M\right)$ takes $H_{\delta}^{s, p}(M) \rightarrow H_{\delta-n / p}^{s-2, p}(M)$ resulting in an undesired loss of decay.
The following result shows that the embedding of $\mathscr{H}^{s, p ; m}(M ; E)$ into Gicquaud-Sakovich spaces is better than a simple application of Lemma 4.5 would suggest, so long as $m$ is sufficiently large. In particular, if $\bar{g} \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,2} M\right)$ with $m>n / p$ then $g \in$ $X_{0}^{s, p}\left(M ; T^{0,2} M\right)$ as desired.
Proposition 4.6. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}_{\geq 0}, s \geq m$. Let $E$ be a tensor bundle of weight $w$ over $M$. We have the continuous embedding
$$\mathscr{H}^{s, p ; m}(M ; E) \hookrightarrow X_{w+\beta}^{s, p}(M ; E),$$
where $\beta=\min (m-n / p, 0)$ unless $m=n / p$, in which case (4.6) holds with any $\beta<0$.
Proof. Since $s \geq m$, Lemma 3.9 implies that
$$\|u\|_{X_{w+\beta}^{s, p}(M)} \lesssim\|u\|_{X_{w+\beta}^{0, p}(M)}+\left\|\hat{\nabla}^{m} u\right\|_{X_{w+\beta}^{s-m, p}(M)} .$$
But then, using the condition $\beta \leq m-n / p$, we obtain from Lemma 3.2
$$\left\|\hat{\nabla}^{m} u\right\|_{X_{w+\beta}^{s-m, p}(M)} \lesssim\left\|\hat{\nabla}^{m} u\right\|_{X_{w+m-n / p}^{s-m, p}}(M) \lesssim\left\|\hat{\nabla}^{m} u\right\|_{H_{w+m}^{s-m, p}(M)} \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M)} .$$
Hence to show embedding (4.6) holds it suffices to establish the low-order estimate
$$\|u\|_{X_{w+\beta}^{0, p}(M ; E)} \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M)} .$$
Moreover, $\mathscr{H}^{s, p ; m}(M) \hookrightarrow \mathscr{H}^{m, p ; m}(M)=H^{m, p}(\bar{M})$ and we show instead that
$$\|u\|_{X_{w+\beta}^{0, p}(M ; E)} \lesssim\|u\|_{\mathscr{H}^{m, p}(\bar{M})} .$$
Suppose first $m<n / p$, so $\beta=m-n / p<0$. Sobolev embedding on $\bar{M}$ and (3.14) provide continuous inclusions
$$H^{m, p}(\bar{M}) \hookrightarrow L^{q}(\bar{M} ; E)=H_{w-n / q}^{0, q}(M) \hookrightarrow X_{w-n / q}^{0, p}(M),$$
where
$$\frac{1}{q}=\frac{1}{p}-\frac{m}{n},$$
and where we have used $q \geq p$ in the final embedding. Estimate (4.7) now follows noting that $w-n / q=w+m-n / p=w+\beta$.
The proof of estimate (4.7) in the boundary case $m=n / p$ is argued the same way as above, except the choice of $q \geq p$ in (4.9) is arbitrary. So suppose $m>n / p$ and therefore $\beta=0$. Sobolev embedding on $\bar{M}$ along with Lemmas 3.15 and 3.2 implies there exists $\alpha \in(0,1)$ such that
$$H^{m, p}(\bar{M}) \hookrightarrow C^{0, \alpha}(\bar{M}) \hookrightarrow C_{w}^{0, \alpha}(M) \hookrightarrow X_{w}^{0, p}(M)=X_{w+\beta}^{0, p}(M)$$
as desired. \(\square\)
4.3. Relationships with spaces on $\bar{M}$. We work with metrics admitting conformal compactifications in fortified spaces and the following embeddings into spaces on $\bar{M}$ play a central role in determining which spaces are suitable for this purpose.

Proposition 4.7 (Inclusion into spaces on $\bar{M}$ ). Suppose $1<p, q<\infty, s \in \mathbb{R}, m, k \in \mathbb{N}_{\geq 0}$ with $s \geq m$, anbd $0<\alpha<1$. Let $E$ be a tensor bundle over $\bar{M}$. We have the following embeddings:
$$\begin{aligned}
\mathscr{H}^{s, p ; m}(M ; E) & \hookrightarrow H^{m, p}(\bar{M} ; E) ; & & \\
\mathscr{X}^{s, p ; m}(M ; E) & \hookrightarrow H^{m, q}(\bar{M} ; E), & & \frac{1}{p}-\frac{s}{n} \leq \frac{1}{q}-\frac{m}{n} ; \\
\mathscr{H}^{s, p ; m}(M ; E) & \hookrightarrow C^{k, \alpha}(\bar{M} ; E), & & m \geq k+\alpha+\frac{n}{p} ; \\
\mathscr{X}^{s, p ; m}(M ; E) & \hookrightarrow C^{k, \alpha}(\bar{M} ; E), & & s \geq k+\alpha+\frac{n}{p} \text { and } m \geq k+1 .
\end{aligned}$$
Proof. Inclusion (4.11) follows immediately from equation (4.2) defining the norm and Lemma 3.16(c). Sobolev embedding on $\bar{M}$ then implies under the hypotheses of (4.13)
$$\mathscr{H}^{s, p ; m}(M) \hookrightarrow H^{m, p}(\bar{M}) \hookrightarrow C^{k, \alpha}(\bar{M})$$
as desired.
Turning to (4.12), the identity (3.14) implies that for a tensor $u$ of weight $w$ and for $0 \leq$ $j \leq m$,
$$\left\|\hat{\nabla}^{j} u\right\|_{L^{q}(\bar{M})}^{q} \lesssim\left\|\hat{\nabla}^{j} u\right\|_{L_{w+j-n / q}^{q}}^{q}(M) \lesssim \sum_{i} \rho_{i}^{-(w+j) q+n}\left\|\Phi_{i}^{*}\left(\hat{\nabla}^{j} u\right)\right\|_{L^{q}\left(B_{1}^{\mathbb{H}}\right)}^{q} .$$
Sobolev embedding on $B_{1}^{\mathbb{H}}$ implies
$$\left\|\Phi_{i}^{*}\left(\hat{\nabla}^{j} u\right)\right\|_{L^{q}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\Phi_{i}^{*}\left(\hat{\nabla}^{j} u\right)\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim \rho_{i}^{w+j}\left\|\hat{\nabla}^{j} u\right\|_{X_{w+j}^{s, p}(M)} \leq \rho_{i}^{w+j}\|u\|_{\mathscr{X}^{s, p ; m}(M)}$$
and we conclude
$$\left\|\hat{\nabla}^{j} u\right\|_{L^{q}(\bar{M} ; E)}^{q} \lesssim \sum_{i} \rho_{i}^{n}\|u\|_{\mathscr{X}^{s, p ; m}(M)}^{q} \lesssim\|1\|_{L^{q}(\bar{M}) ; E}^{q}\|u\|_{\mathscr{X}^{s, p ; m}(M)}^{q} ;$$
note that the estimate $\sum \rho_{i}^{q} \lesssim\|1\|_{L^{q}(\bar{M})}$ is a consequence of Lemma 3.1 and (3.14). This establishes (4.12).
Inclusion (4.14) is a consequence of (4.12) using Sobolev embedding on $\bar{M}$ as follows. First consider the case $k=0$, in which case we can assume $m=1$. Lowering $s \geq 1$ (and additionally lowering $p$ if $s=1$ is not sufficient) we can assume $s=\alpha+n / p$ and we pick $q$ satisfying
$$\frac{1}{q}-\frac{1}{n}=\frac{1}{p}-\frac{s}{n}=-\frac{\alpha}{n} .$$

Since $s \geq 1$, and since $0<\alpha<1$, a computation shows $1<p \leq q<\infty$. Thus Sobolev embedding on $\bar{M}$ yields
$$\mathscr{X}^{s, p ; 1}(M ; E) \hookrightarrow H^{1, q}(\bar{M}) \hookrightarrow C^{0, \alpha}(\bar{M}) .$$
The embedding $\mathscr{X}^{s, p ; m}(M) \subset C^{k, \alpha}(\bar{M})$ when $s \geq k+\alpha-n / p$ and $m \geq k+1$ follows from the $k=0$ case using Lemma 4.3(b). \(\square\)

Proposition 4.7 demonstrates that some of the additional regularity possessed by elements of $\mathscr{X}^{s, p ; m}(M ; E)$, as compared to their $\mathscr{H}^{s, p ; m}(M ; E)$ counterparts, continues up to the boundary. For example, although both spaces embed in $H^{m ; p}(M ; E)$, the inclusion (4.12) shows that if $s>m$ then $X^{s, p ; m}(M ; E)$ embeds in a space $H^{m, q}(\bar{M} ; E)$ with $q>p$. Indeed the embedding is as good as if the initial space were $H^{s, p}(\bar{M} ; E)$ rather than $\mathscr{X}^{s, p ; m}(M ; E)$.

As discussed in §4.2, we wish to work with metrics $g$ admitting continuous compactifications $\bar{g}$. If $\bar{g} \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,2} M\right)$ then the inclusion (4.13) of Proposition 4.7 leads to the condition $m>n / p$. But if $\bar{g} \in \mathscr{X}^{s, p ; m}\left(M ; T^{0,2} M\right)$, then this can be substantially weakened to $s>n / p$ and $m \geq 1$. In both cases, the compactified metric is in fact Hölder continuous up to the boundary, and this additional regularity is essential in the parametrix construction of §9.
Sufficiently regular spaces on $\bar{M}$ are contained in fortified spaces, and the following inclusions are an easy application of Proposition 3.17.

Proposition 4.8 (Containment of spaces on $\bar{M}$ ). Let $E$ be a tensor bundle over $M$. Suppose $s \in \mathbb{R}, m \in \mathbb{N}_{\geq 0}, 1<p<\infty$ and $s \geq m$. Then
$$\begin{aligned}
& H^{s, p}(\bar{M} ; E) \hookrightarrow \mathscr{H}^{s, p ; m}(M ; E) ; \\
& H^{s, p}(\bar{M} ; E) \hookrightarrow \mathscr{X}^{s, p ; m}(M ; E), \quad s>\frac{n}{p}+m \text { and } s \geq m+1 .
\end{aligned}$$
Note that the hypothesis $s \geq m+1$ in embedding (4.17) is superfluous if $s \in \mathbb{N}$, and an improvement to Proposition 3.17 would be needed to remove it in the general case. The requirement $s>n / p+m$ is fundamental, however, and can be thought of as arising from additional boundary regularity possessed by elements of $\mathscr{X}^{s, p ; m}(M ; E)$. For example, Corollary 4.9 below shows that functions in $\mathscr{X}^{1, p ; 1}(M ; E)$ have Lipschitz boundary traces regardless of the value of $p$. But $H^{s, p}(\bar{M} ; E)$ guarantees Lipschitz boundary traces only when $s>n / p+1$.
4.4. Boundary asymptotics. Elements of fortified spaces admit asymptotic expansions at the boundary, a central feature that permits their use in geometric analysis. See §5 where these expansions are used to precisely describe the sense in which asymptotically hyperbolic metrics have curvatures that decay to those of $\breve{g}$ when their compactifications lie in sufficiently regular fortified spaces. These curvature expansions play a central role in solving the Yamabe problem, where an initial asymptotic scalar curvature correction is necessary to first bring the scalar curvature anomaly into the Fredholm range of the
requisite PDE. The somewhat involved proof establishing these expansions is the subject of §7, which culminates in the following.

Theorem 7.1 (Asymptotic Structure Theorem). Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}_{\geq 0}$, $s \geq m$ and $E$ is a tensor bundle over $M$ of weight $w$.
\begin{itemize}
\item[(a)] If $u \in \mathscr{H}^{s, p ; m}(M ; E)$ then $u=\tau+r$, where $\tau \in \mathscr{H}^{\infty, p ; m}(M ; E)$ and $r \in H_{w+m-n / p}^{s, p}(M ; E)$.
Moreover, if $u \in H_{w+k+\alpha-n / p}^{s, p}(M ; E)$ for some integer $0 \leq k \leq m-1$ and some $\alpha \in[0,1)$, then $\tau=\rho^{k} \eta$ for some $\eta \in \mathscr{H}^{\infty, p ; m-k}(M ; E) \cap H_{w+\alpha-n / p}^{\infty, p}(M ; E)$.
Finally, if $m \geq 1$ then $\left.u\right|_{\partial M}=0$ if and only if $u \in H_{w+1-n / p}^{s, p}(M ; E)$.
\item[(b)] If $u \in \mathscr{X}^{s, p ; m}(M ; E)$ then $u=\tau+r$, where $\tau \in \mathscr{X}^{\infty ; m}(M ; E)$ and $r \in X_{w+m}^{s, p}(M ; E)$.
Moreover, if $u \in X_{w+k}^{s, p}(M ; E)$ for some integer $0 \leq k \leq m$ and some $\alpha \in[0,1)$, then $\tau=\rho^{k} \eta$ for some $\eta \in \mathscr{X}^{\infty ; m-k}(M ; E) \cap X_{w+\alpha}^{\infty}(M ; E)$.
Finally, if $m \geq 1$ then $\left.u\right|_{\partial M}=0$ if and only if $u \in X_{w+1}^{s, p}(M ; E)$.
\end{itemize}
Theorem 7.1 is a consequence of Theorem 7.11, which establishes a finer-grained Taylor expansion in a coordinate-dependent setting. The decomposition $u=\tau+r$ should be thought of as a split into a component $\tau$ that carries boundary information and which is smooth in the interior, along with a remainder $r$ that is less regular in the interior and that vanishes on the boundary at a rate controlled by $u$ 's limited boundary regularity. Indeed, to see that $\left.r\right|_{\partial M}=0$ observe
$$H_{w+m-n / p}^{s, p}(M ; E) \hookrightarrow H_{w+1-n / p}^{1, p}(M ; E) \hookrightarrow \mathscr{H}^{1, p ; 1}(M ; E)=H^{1, p}(M ; E)$$
and hence $r$ admits a trace. Moreover, since the smooth compactly supported sections are dense, the trace vanishes for all elements of $H_{w+m-n / p}^{s, p}(M ; E)$. The same conclusion holds if $r \in X_{w+m}^{s, p}(M ; E)$, since $X_{w+m}^{s, p}(M ; E) \hookrightarrow H_{w+m-n / p}^{s, p}(M ; E)$.
Our earlier claim that elements of $\mathscr{X}^{1, p ; 1}(M ; E)$ have Lipschitz traces follows from Theorem 7.1 and the regularity of $\mathscr{X}^{\infty ; 1}(M ; E)$.

Corollary 4.9. Suppose $1<p<\infty$ and $E$ is a tensor bundle over $M$. If $u \in \mathscr{X}^{1, p ; 1}(M ; E)$ then $\left.u\right|_{\partial M}$ is Lipschitz continuous.

Proof. Suppose $u \in \mathscr{X}^{1, p ; 1}(M)$. Theorem 7.1 implies $\left.u\right|_{\partial M}=\left.\tau\right|_{\partial M}$ for some $\tau \in \mathscr{X}^{\infty ; m}(M)$. But we observed at the start of the section that $\mathscr{X}^{\infty ; m}(M)=\mathscr{C}^{\infty ; m}(M)$, and [AILSA18] Lemma 2.3(c) implies $\mathscr{C}^{\infty ; m}(M) \subset C^{0,1}(\bar{M} ; E)$. \(\square\)
4.5. Relationships between fortified spaces. The following result enumerates relationships between fortified spaces. Some of these have been mentioned earlier and are reiterated now for convenience. The important new principle is that embedding $\mathscr{H}^{s, p ; m}(M ; E)$ into $\mathscr{X}^{s, q ; \ell}(M ; E)$ entails a loss of boundary regularity and is possible only if $m>\ell$.

Lemma 4.10. Suppose $1<p, q<\infty, k, \ell, m \in \mathbb{N}_{\geq 0}, k \geq m, 0 \leq \alpha \leq 1, s \in \mathbb{R}$, and $s \geq m$. The following relationships hold, and all stated inclusions are continuous.
$$\begin{aligned}
& \mathscr{X}^{s, p ; m}(M ; E) \hookrightarrow \mathscr{H}^{s, p ; m}(M ; E) ; \\
& \mathscr{H}^{s, p ; m}(M ; E) \hookrightarrow \mathscr{X}^{s, p ; \ell}(M ; E), \quad m>\ell+\frac{n}{p} \text {; } \\
& \mathscr{C}^{k, \alpha ; m}(M ; E) \hookrightarrow \mathscr{X}^{k, p ; m}(M ; E) ; \\
& \mathscr{X}^{s, p ; m}(M ; E) \hookrightarrow \mathscr{C}^{k, \alpha ; m}(M ; E), \quad \frac{1}{p}-\frac{s}{n} \leq-\frac{k+\alpha}{n}, \quad \alpha>0 \text {; } \\
& \mathscr{C}^{\infty ; m}(M ; E)=\mathscr{X}^{\infty ; m}(M ; E) ; \\
& \mathscr{H}^{\infty ; m}(M ; E) \hookrightarrow \mathscr{C}^{\infty ; \ell}(M ; E), \quad m>\ell+\frac{n}{p} \text {; } \\
& \mathscr{H}^{s, p ; 1}(M ; E) \not \subset \mathscr{X}^{1, q ; 1}(M ; E), \quad s \geq 1 \text {; } \\
& \mathscr{H}^{\infty, p ; 1}(M ; E) \not \subset \mathscr{C}^{\infty ; 1}(M ; E) .
\end{aligned}$$
Proof. Embeddings (4.18), (4.20), and (4.21) follow from Lemma 3.2 and Proposition 3.3. To establish (4.19), suppose that $u \in \mathscr{H}^{s, p ; m}(M ; E)$ and $m>\ell+n / p$. For each $0 \leq j \leq m$ we apply Proposition 4.6 and the inequality $m>\ell-n / p \geq j-n / p$ to find
$$\left\|\hat{\nabla}^{j} u\right\|_{X_{w+j}^{s-j, p}(M)} \lesssim\left\|\hat{\nabla}^{j} u\right\|_{\mathscr{H}^{s-j, p ; m-j}(M)} \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M)} .$$
Embedding (4.22) follows from embeddings (4.20) and (4.21), whereas equality (4.23) stems from embeddings (4.19) and (4.21).

The non-containments (4.24) and (4.25) come from a single example. Consider the function $u=\rho^{1-1 / p+\varepsilon}$ for some $0<\varepsilon<1 / p$. For any $s$ and $p$ we have
$$1 \in X_{0}^{s, p}(M) \hookrightarrow H_{1 / p-n / p-\varepsilon}^{s, p}(M),$$
and a similar inclusion yields $\rho^{-1} d \rho \in H_{1 / p-n / p-\varepsilon}^{s, p}(M)$. Hence $u \in H_{1-1 / p}^{s, p}(M)$ and $\hat{\nabla} u \in$ $H_{1-n / p}^{s, p}(M)$, implying $u \in \mathscr{H}^{s, p ; m}(M)$. Since $1-1 / p<1$, and since each
$$\Phi_{i}^{*} \hat{\nabla} u=\rho_{i}^{1-1 / p+\varepsilon} d y,$$
we find $\hat{\nabla} u \notin X_{1}^{1, q}(M)$ for any choice of $q$ and therefore $u \notin \mathscr{X}^{1, q ; 1}(M)$. This establishes (4.24), and the non-containment (4.25) follows from the observation in the proof of Corollary 4.9 that elements of $\mathscr{C}^{\infty ; 1}(M)$ are Lipschitz on $\bar{M}$ whereas $u$ is not. \(\square\)
4.6. Multiplication and nonlinearities. The following variation of Corollary 3.12, suffices for the limited circumstances where we multiply elements of fortified spaces. Much of the work in the proof stems from managing terms of the form $-n / p$ appearing in weights in the Sobolev case; the inclusion provided by Proposition 4.6 and asymptotic structure of Theorem 7.1 play central roles.

Proposition 4.11. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}, s \geq m$, and $s>n / p$. Moreover, suppose that for each $j=1, \ldots, \ell$ we have a tensor bundle $E_{j}$ of weight $w_{j}$ over $M$ and a nonnegative integer $k_{j}$ such that $k_{1}+\cdots+k_{\ell}=k \leq m$.
\begin{itemize}
\item[(a)] Assume in addition that $m>n / p$. If $u_{j} \in \mathscr{H}^{s, p ; m}\left(M ; E_{j}\right)$, then $\hat{\nabla}^{k_{1}} u_{1} \otimes \cdots \otimes$ $\hat{\nabla}^{k t} u_{\ell} \in \mathscr{H}^{s-k, p ; m-k}\left(M ; \otimes_{j} E_{j}\right)$.
\item[(b)] If $u_{j} \in \mathscr{X}^{s, p ; m}\left(M ; E_{j}\right)$, then $\hat{\nabla}^{k_{1}} u_{1} \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u_{\ell} \in \mathscr{X}^{s-k, p ; m-k}\left(M ; \otimes_{j} E_{j}\right)$.
\end{itemize}
In both cases $\left(u_{1}, \ldots, u_{\ell}\right) \mapsto \hat{\nabla}^{k_{1}} u_{1} \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u_{\ell}$ is continuous between the stated spaces.
Proof. We prove the first claim, which is harder, and outline the changes needed for the second claim at the end of the proof. Let $w_{1}, \ldots, w_{\ell}$ be the weights of $u_{1}, \ldots, u_{\ell}$; set $w=w_{1}+\cdots+w_{\ell}$. From Theorem 7.1 we have
$$u_{j}=\tau_{j}+r_{j},$$
where $\tau_{j} \in \mathscr{H}^{\infty, p ; m}(M)$ and $r_{j} \in H_{w_{j}+m-n / p}^{s, p}(M)$. Write the product $\nabla^{k_{1}} u_{1} \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u_{\ell}$ as the sum of
$$\tau=\hat{\nabla}^{k_{1}} \tau_{1} \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} \tau_{\ell}$$
and $r$, which is the sum of products containing at least one factor $\hat{\nabla}^{k_{j}} r_{j}$; both $\tau$ and $r$ are tensors of weight $w+k$.

First we analyze $\tau$. For each $j$, Proposition 4.7 implies
$$\hat{\nabla}^{k_{j}} \boldsymbol{\tau}_{j} \in \mathscr{H}^{\infty, p ; m-k_{j}}(M) \subset H^{m-k_{j}, p}(\bar{M}) .$$
Because $s>n / p$, standard multiplication properties of Sobolev spaces on $\bar{M}$ analogous to those of Proposition 3.11 together with Proposition 4.8 imply
$$\tau \in H^{m-k, p}(\bar{M}) \subset \mathscr{H}^{m-k, p ; m-k}(M) .$$
Applying $\rho \hat{\nabla}$ to $\tau$, and using that $\rho \hat{\nabla} \hat{\nabla}^{k_{j}} \tau_{j} \in \mathscr{H}^{\infty, p ; m-k_{j}}(M)$ for each $j$, we find $\rho \hat{\nabla} \tau \in$ $\mathscr{H}^{m-k, p ; m-k}(M)$ as well. Thus Lemma 4.4 implies $\tau \in \mathscr{H}^{m-k+1, p ; m-k}(M)$. Iterating this argument, we find $\tau \in \mathscr{H}^{\infty, p ; m-k}(M)$.
We show that $r \in \mathscr{H}^{s-k, p ; m-k}(M)$ by establishing $\hat{\nabla}^{i} r \in H_{w+k+i-n / p}^{s-k-i, p}(M)$ for each $i \leq m-k$. Consider first those terms of $\hat{\nabla}^{i} r$ of the form
$$\hat{\nabla}^{a_{1}} r_{1} \otimes \hat{\nabla}^{a_{2}} \tau_{2} \otimes \cdots \otimes \hat{\nabla}^{a_{\ell}} \tau_{\ell},$$
where $a_{1}+\cdots+a_{\ell}=i+k \leq m$. Recall $r_{1} \in H_{w_{1}+m-n / p}^{s, p}(M)$ and therefore $\hat{\nabla}^{a_{1}} r_{1} \in$ $H_{w_{1}+m-n / p}^{s-a_{1}, p}(M)$. For $j=2, \ldots, \ell$, we use Proposition 4.6 and the hypothesis $m>n / p$ to obtain $\tau_{j} \in X_{w_{j}}^{\infty}(M)$ and thus $\hat{\nabla}^{a_{j}} \tau_{j} \in X_{w_{j}}^{\infty}(M)$. The expression (4.28) is thus an element of
$$H_{w_{1}+m-n / p}^{s-a_{1}, p}(M) \times X_{w_{2}}^{\infty}(M) \times \cdots \times X_{w_{\ell}}^{\infty}(M),$$
which by Proposition 3.11 is contained in $H_{w+m-n / p}^{s-k-i, p}(M) \subset H_{w+k_{i}-n / p}^{s-k-i, p}(M)$ as desired. Terms of $\hat{\nabla}^{i} r$ containing exactly one $r_{j}$ factor are similarly in $H_{w+k_{i}-n / p}^{s-k-i, p}(M)$.

The remaining terms of $\hat{\nabla}^{i} r$ arise from taking terms analogous to (4.28) and replacing some of the $\hat{\nabla}^{a_{j}} \tau_{j}$ with $\hat{\nabla}^{a_{j}} r_{j}$. This results in the replacement of $X_{w_{j}}^{\infty}(M)$ by $H_{w_{j}+m-n / p}^{s-a_{j}, p}(M)$ in (4.29). As $m-n / p>0$, one may use Proposition 3.11 to show these products are also included in $H_{w+m-n / p}^{s-k-i, p}(M) \subset H_{w+k_{i}-n / p}^{s-k-i, p}(M)$. Thus $r$, and hence $\tau+r$, is in $\mathscr{H}^{s-k, p ; m-k}(M)$.
It remains to establish continuity, and we employ the Closed Graph Theorem. Suppose $v_{a}$ is a sequence in $\mathscr{H}^{s, p ; m}(M)$ converging to $u_{1}$, and that
$$\hat{\nabla}^{k_{1}} v_{a} \otimes \hat{\nabla}^{k_{2}} u_{2} \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u_{\ell} \rightarrow w \in \mathscr{H}^{s-k, p ; m-k}(M) .$$
Reducing to subsequences, since $m-k \geq 0$, we can assume that the above convergence, as well as $\hat{\nabla}^{k_{1}} v_{a} \rightarrow \hat{\nabla}^{k_{1}} u$ occurs pointwise almost everywhere. But then $w=\hat{\nabla}^{k_{1}} u_{1} \otimes \cdots \otimes$ $\hat{\nabla}^{k_{\ell}} u_{\ell}$, which proves the continuity of the map
$$v \mapsto \hat{\nabla}^{k_{1}} v \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u_{\ell} .$$
The same argument works for each factor, and continuity of the multilinear map then follows from the Uniform Boundedness Principle.

In the Gicquaud-Sakovich case the argument above can be simplified. One can show that $\tau$ in equation (4.27) belongs to $\mathscr{X}^{\infty ; m-k}(M)$ as above or directly from the definition of $\mathscr{X}^{\infty ; m-k}(M)$ and Proposition 3.11 using only the hypothesis $s>n / p$. In mixed expressions such as (4.28), terms of the form $\hat{\nabla}^{a_{i}} \tau_{i}$ lie in $X_{w_{i}+a_{i}}^{s-a_{i}, p}(M)$ and each $\hat{\nabla}^{a_{i}} r_{i}$ lies in $X_{w_{i}+m}^{s-a_{i}, p}(M ; *) \subset X_{w_{i}+a_{i}}^{s-a_{i}, p}(M)$, again by virtue of the definition in equation (4.3). The product then belongs to $X_{w+k}^{s-k, p}(M)$ by application of Proposition 3.11. There is no use of Proposition 4.6 and hence the additional hypothesis $m>n / p$ is not needed. \(\square\)

There are two important consequences of Proposition 4.11. First, specializing to two factors and taking no derivatives we have the following Banach algebra property.

Proposition 4.12. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}, s \geq m$, and $s>n / p$. Let $E_{1}$ and $E_{2}$ be tensor bundles over $M$. Then the tensor product yields continuous bilinear maps
$$\begin{aligned}
& \mathscr{H}^{s, p ; m}\left(M ; E_{1}\right) \times \mathscr{H}^{s, p ; m}\left(M ; E_{2}\right) \rightarrow \mathscr{H}^{s, p ; m}\left(M ; E_{1} \otimes E_{2}\right), \\
& \mathscr{X}^{s, p ; m}\left(M ; E_{1}\right) \times \mathscr{X}^{s, p ; m}\left(M ; E_{2}\right) \rightarrow \mathscr{X}^{s, p ; m}\left(M ; E_{1} \otimes E_{2}\right),
\end{aligned}$$
where the first claim requires additionally $m>n / p$.
The second important consequence of Proposition (4.11) is that smooth nonlinear functions determine well-defined maps on $\mathscr{H}^{s, p ; m}(M ; \mathbb{R})$ whenever the Banach algebra condition $s \geq m>n / p$ holds and $s \geq 1$.

Proposition 4.13. Suppose $1<p<\infty, m \in \mathbb{N}$ and $s>n / p$, and $s \geq m$. Let $F \in C^{\infty}(\mathbb{R})$.
\begin{itemize}
\item[(a)] Assume additionally $m>n / p$. If $u \in \mathscr{H}^{s, p ; m}(M ; \mathbb{R})$ then $F(u) \in \mathscr{H}^{s, p ; m}(M ; \mathbb{R})$.
\item[(b)] If $u \in \mathscr{X}^{s, p ; m}(M ; \mathbb{R})$ then $F(u) \in \mathscr{X}^{s, p ; m}(M ; \mathbb{R})$.
\end{itemize}

Proof. The two results are proved similarly and we assume that $u \in \mathscr{H}^{s, p ; m}(M)$. We need to show that
$$\hat{\nabla}^{k} f(u) \in H_{k-n / p}^{s, p}(M)$$
for each $0 \leq k \leq m$. Now $\hat{\nabla}^{k} f(u)$ is a sum of terms of the form
$$f^{(a)}(u) \hat{\nabla}^{k_{1}} u \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u,$$
where $k_{1}+\cdots+k_{\ell}=k$ and where $a \leq k$. Corollary 3.20 implies $f^{(a)}(u) \in X_{0}^{s, p}(M)$ whereas Proposition 4.11 implies $\hat{\nabla}^{k_{1}} u \otimes \cdots \otimes \hat{\nabla}^{k_{t}} u \in \mathscr{H}^{s-k, p ; m-k}(M ; *) \subset H_{k-n / p}^{s-k, p}(M)$; we have used the fact that $\hat{\nabla}^{k_{1}} u \otimes \cdots \otimes \hat{\nabla}^{k_{\ell}} u$ has weight $k$. An application of Proposition 3.11 finishes the proof. \(\square\)

\section*{5. Asymptotically hyperbolic metrics}

In the introduction, we motivated the definition of asymptotically hyperbolic metrics with the identity
$$\operatorname{Riem}[g]=-|d \rho|_{\bar{g}}^{2} \operatorname{id}+2 \rho \delta * \operatorname{Hess} \bar{g}(\rho)^{\sharp}+\rho^{2} \operatorname{Riem}[\bar{g}]$$
relating the curvature operator Riem $[g]$ of metric $g$ with that of $\bar{g}=\rho^{2} g$. (Recall that we view Riem $[g]$ as a $(2,2)$ tensor, that id and $\delta$ are the identity operators on $\Lambda^{2}(T M)$ and $\Lambda^{1}(T M)$, and that $*$ is the Kulkarni-Nomizu product; see [AILSA18].) In particular, the identity (5.1) indicates that if $\bar{g}$ is sufficiently regular, then curvatures of $g$ are asymptotically determined by the value of $|d \rho|_{\bar{g}}$ along $\partial M$. The main result of this section, Proposition 5.1 below, shows that the regularity assumptions of the introduction are sufficient to conclude that if $|d \rho|_{\bar{g}}=1$ along $\partial M$, then the curvatures of $g$ approach those of hyperbolic space as $\rho \rightarrow 0$.
To this end, recall from the introduction our assumption that $g$ satisfies either
\begin{itemize}
\item[-] condition (1.3), in which case $\bar{g} \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,2} M\right)$ with $s \in \mathbb{R}$ and $m \in \mathbb{N}$ satisfying $s \geq m>n / p$ and $1<p<\infty$; or
\item[-] condition (1.4), in which case $\bar{g} \in \mathscr{X}^{s, p ; m}\left(M ; T^{0,2} M\right)$ with $s \in \mathbb{R}$ and $m \in \mathbb{N}$ satisfying $s \geq m \geq 1, s<n / p$, and $1<p<\infty$.
\end{itemize}

In either case, Proposition 4.7 implies that $\bar{g}$ extends continuously to $\bar{M}$. We say that $g$ is asymptotically hyperbolic of class $\mathscr{H}^{s, p ; m}$ or $\mathscr{X}^{s, p ; m}$, respectively, if the relevant regularity assumption above is satisfied, if $g$ is conformally compact (so that $\bar{g}$ extends to a Riemannian metric on $\bar{M}$ ), and if $|d \rho|_{\bar{g}}=1$ along $\partial M$.

Proposition 5.1.
\begin{itemize}
\item[(a)] Suppose $g$ is an asymptotically hyperbolic metric of class $\mathscr{H}^{s, p ; m}$ satisfying (1.3). Then the curvature operator of $g$ satisfies
$$\operatorname{Riem}[g]=-\mathrm{id}+\rho \tau_{\text {Riem }}+r_{\text {Riem }},$$
where $\tau_{\text {Riem }} \in \mathscr{H}^{\infty, p ; m-1}\left(M ; T^{2,2} M\right)$ and $r_{\text {Riem }} \in H_{m-n / p}^{s-2, p}\left(M ; T^{2,2} M\right)$.
\end{itemize}

Consequently, the scalar curvature of $g$ satisfies
$$\mathrm{R}[g]=-n(n-1)+\rho \tau_{\mathrm{R}}+r_{\mathrm{R}},$$
where $\tau_{\mathrm{R}} \in \mathscr{H}^{\infty, p ; m-1}(M ; \mathbb{R})$ and where $r_{\mathrm{R}} \in H_{m-n / p}^{s-2, p}(M ; \mathbb{R})$.
Moreover
$$\mathrm{R}[g]+n(n-1) \in X_{\beta}^{s-2, p}(M ; \mathbb{R}),$$
where $\beta=\min (m-n / p, 1)$ unless $m=n / p+1$, in which case inclusion (5.2) holds for any $\beta<1$.
\begin{itemize}
\item[(b)] Suppose $g$ is an asymptotically hyperbolic metric of class $\mathscr{X}^{s, p ; m}$ satisfying (1.4). Then the curvature operator of $g$ satisfies
$$\operatorname{Riem}[g]=-\mathrm{id}+\rho \tau_{\text {Riem }}+r_{\text {Riem }},$$
where $\tau_{\text {Riem }} \in \mathscr{X}^{\infty ; m-1}\left(M ; T^{2,2} M\right)$ and $r_{\text {Riem }} \in X_{m}^{s-2, p}\left(M ; T^{2,2} M\right)$.
Consequently, the scalar curvature of $g$ satisfies
$$\mathrm{R}[g]=-n(n-1)+\rho \tau_{\mathrm{R}}+r_{\mathrm{R}},$$
where $\tau_{\mathrm{R}} \in \mathscr{X}^{\infty ; m-1}(M ; \mathbb{R})$ and where $r_{\mathrm{R}} \in X_{m}^{s-2, p}(M ; \mathbb{R})$.
Moreover
$$\mathrm{R}[g]+n(n-1) \in X_{1}^{s-2, p}(M ; \mathbb{R}) .$$
\end{itemize}

Proof. The result follows immediately from Lemmas 5.2-5.4 below, the identity (5.1), and its consequence
$$\mathrm{R}[g]=-n(n-1)|d \rho|_{\bar{g}}^{2}+2(n-1) \rho \Delta_{\bar{g}} \rho+\rho^{2} \mathrm{R}[\bar{g}] .$$ \(\square\)

The following lemmas repeatedly use that $\hat{\nabla}^{k} \rho$ is an element of both $\mathscr{H}^{s, p ; m}\left(M ; T^{0, k} M\right)$ and $\mathscr{X}^{s, p ; m}\left(M ; T^{0, k} M\right)$ for all $k$; this follows from Proposition 4.8. We furthermore use that if $\bar{g} \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,2} M\right)$, then $\bar{g}^{-1} \in \mathscr{H}^{s, p ; m}\left(M ; T^{2,0} M\right)$ and, similarly, that if $\bar{g} \in$ $\mathscr{X}^{s, p ; m}\left(M ; T^{0,2} M\right)$, then $\bar{g}^{-1} \in \mathscr{X}^{s, p ; m}\left(M ; T^{2,0} M\right)$. These latter facts follow from $\bar{g}$ being continuous on $\bar{M}$, the determinant being a polynomial, and Proposition 4.11.

Lemma 5.2.
\begin{itemize}
\item[(a)] Suppose $g=\rho^{-2}$ is an asymptotically hyperbolic metric of class $\mathscr{H}^{s, p ; m}$ satisfying (1.3). Then
$$|d \rho|_{\bar{g}}^{2}=1+\rho \tau+r,$$
where $\tau \in \mathscr{H}^{\infty, p ; m-1}(M ; \mathbb{R})$ and $r \in H_{m-n / p}^{s, p}(M ; \mathbb{R})$.
Moreover
$$|d \rho|_{\bar{g}}^{2}-1 \in X_{\beta}^{s, p}(M ; \mathbb{R}),$$
where $\beta=\min (m-n / p, 1)$ unless $m=n / p+1$, in which case (5.3) holds for any $\beta<1$.
\end{itemize}
\begin{itemize}
\item[(b)] Suppose $g=\rho^{-2} \bar{g}$ is an asymptotically hyperbolic metric of class $\mathscr{X}^{s, p ; m}$ satisfying (1.4). Then
$$|d \rho|_{\bar{g}}^{2}=1+\rho \tau+r,$$
where $\tau \in \mathscr{X}^{\infty ; m-1}(M ; \mathbb{R})$ and $r \in X_{m}^{s, p}(M ; \mathbb{R})$.
Moreover
$$|d \rho|_{\bar{g}}^{2}-1 \in X_{1}^{s, p}(M ; \mathbb{R}) .$$
\end{itemize}

Proof. Suppose first that $\bar{g} \in \mathscr{H}^{s, p ; m}(M)$ and consider $f=|d \rho|_{\bar{g}}^{2}-1$. Since $|d \rho|_{\bar{g}}^{2}$ is a contraction of $\bar{g}^{-1} \otimes \hat{\nabla} \rho \otimes \hat{\nabla} \rho$, Proposition 4.11 implies $f \in \mathscr{H}^{s, p ; m}(M)$. By Proposition $4.7 f \in C^{0, \alpha}(\bar{M}), \alpha=m-n / p$, and by assumption $f=0$ along $\partial M$. Thus Theorem 7.1 implies that $f \in H_{1-n / p}^{s, p}(M)$ and implies further that $f=\rho \tau+r$ with $r=H_{m-n / p}^{s, p}(M)$, and with $\tau \in \mathscr{H}^{\infty, p ; m-1}(M)$. Applying Proposition 4.6 to $\tau$, and subsequently multiplying by $\rho$, yields $\rho \tau \in X_{\beta}^{s, p}(M)$, where $\beta=\min (m-n / p, 1)$, unless $m=n / p+1$, in which case any $\beta<1$ suffices.
If instead $\bar{g} \in \mathscr{X}^{s, p ; m}(M)$, then Proposition 4.11 implies $f \in \mathscr{X}^{s, p ; m}(M)$ and Proposition 4.7 again shows $f \in C^{0, \alpha}(\bar{M})$ with zero trace along $\partial M$. Hence Theorem 7.1 implies $f \in X_{1}^{s, p}(M)$ and moreover that $f=\rho \tau+r$ with $r \in X_{m}^{s, p}(M)$ and $\tau \in \mathscr{X}^{\infty ; m-1}(M)$. This immediately yields the remaining claims of this case. \(\square\)

Lemma 5.3.
\begin{itemize}
\item[(a)] Suppose $g=\rho^{-2} \bar{g}$ is an asymptotically hyperbolic metric of class $\mathscr{H}^{s, p ; m}$ satisfying (1.3). Then
\begin{itemize}
\item[(i)] $\operatorname{Hess}_{\bar{g}}(\rho)^{\sharp}=\tau_{H}+r_{H}$ with
$$\begin{aligned}
& \tau_{H} \in \mathscr{H}^{\infty, p ; m-1}\left(M ; T^{1,1} M\right), \\
& r_{H} \in H_{m-1-n / p}^{s-1, p}\left(M ; T^{1,1} M\right) .
\end{aligned}$$
\item[(ii)] $\rho \Delta_{\bar{g}} \rho=\rho \tau_{L}+r_{L}$ with $\tau_{L} \in \mathscr{H}^{\infty, p ; m-1}(M ; \mathbb{R})$ and $r_{L} \in H_{m-n / p}^{s-1, p}(M ; \mathbb{R})$. In particular,
$$\rho \Delta_{\bar{g}} \rho \in X_{\beta}^{s-1, p}(M ; \mathbb{R}),$$
where $\beta=\min (m-n / p, 1)$ unless $m=n / p+1$, in which case (5.4) holds with any $\beta<1$.
\end{itemize}
\item[(b)] Suppose $g=\rho^{-2} \bar{g}$ is an asymptotically hyperbolic metric of class $\mathscr{X}^{s, p ; m}$ satisfying (1.4). Then
\begin{itemize}
\item[(i)] $\operatorname{Hess}_{\bar{g}}(\rho)^{\sharp}=\tau_{H}+r_{H}$ with
$$\begin{aligned}
& \tau_{H} \in \mathscr{X}^{\infty ; m-1}\left(M ; T^{1,1} M\right), \\
& r_{H} \in X_{m-1}^{s-1, p}\left(M ; T^{1,1} M\right) .
\end{aligned}$$
\item[(ii)] $\rho \Delta_{\bar{g}} \rho=\rho_{L} \tau+r_{L}$ where $\tau_{L} \in \mathscr{X}^{\infty ; m-1}(M ; \mathbb{R})$ and $r_{L} \in X_{m}^{s-1, p}(M ; \mathbb{R})$. In particular
$$\rho \Delta_{\bar{g}} \rho \in X_{1}^{s-1, p}(M ; \mathbb{R}) .$$
\end{itemize}
\end{itemize}

Proof. First consider the case when $\bar{g} \in \mathscr{H}^{s, p ; m}(M)$ and write $\operatorname{Hess}_{\bar{g}}(\rho)^{\sharp}$ as a linear combination of contractions of $\bar{g}^{-1} \otimes \hat{\nabla}^{2} \rho$ and $\bar{g}^{-1} \otimes \bar{g}^{-1} \otimes \hat{\nabla} \bar{g} \otimes \hat{\nabla} \rho$. At most one derivative of $\bar{g}$ appears in these expressions; thus Proposition 4.11 and the smoothness of $\rho$ implies $\operatorname{Hess}_{\bar{g}}(\rho)^{\sharp} \in \mathscr{H}^{s-1, p ; m-1}(M)$. Theorem 7.1 then implies the first claim in this case. Contracting and multiplying by $\rho$ yields the second claim from the first. The embedding (5.4) follows from applying Proposition 4.6 to $\Delta_{\bar{g}} \rho \in \mathscr{H}^{s-1, p ; m-1}(M)$ and then multiplying by $\rho$.
The argument when $\bar{g} \in \mathscr{X}^{s, p ; m}(M)$ follows from analogous logic, except that Proposition 4.6 is not needed to establish (5.5), which follows immediately from $\Delta_{\bar{g}} \rho \in \mathscr{X}^{s-1, p ; m-1}(M)$. \(\square\)

Lemma 5.4.
\begin{itemize}
\item[(a)] Suppose that $g=\rho^{-2} \bar{g}$ is an asymptotically hyperbolic metric of class $\mathscr{H}^{s, p ; m}$ satisfying (1.3). If $m \geq 2$ then
\begin{itemize}
\item[(i)] $\operatorname{Riem}[\bar{g}]=\tau_{\text {Riem }}+r_{\text {Riem }}$, where
$$\begin{aligned}
& \tau_{\text {Riem }} \in \mathscr{H}^{\infty, p ; m-2}\left(M ; T^{2,2} M\right), \\
& r_{\text {Riem }} \in H_{m-2-n / p}^{s-2, p}\left(M ; T^{2,2} M\right) .
\end{aligned}$$
\end{itemize}
\end{itemize}
(ii) $\rho^{2} \mathrm{R}[\bar{g}]=\rho^{2} \tau_{\mathrm{R}}+r_{\mathrm{R}}$, where $\tau_{\mathrm{R}} \in \mathscr{H}^{\infty, p, m-2}(M ; \mathbb{R})$ and $r_{\mathrm{R}} \in H_{m-n / p}^{s-2, p}(M ; \mathbb{R})$. If $m=1$, in which case $\mathscr{H}^{\infty, p ; m-2}(M)$ is not defined, then (i) and (ii) remain true setting $\tau_{\text {Riem }}=0$ and $\tau_{\mathrm{R}}=0$. In all cases
$$\rho^{2} \mathrm{R}[\bar{g}] \in X_{\beta}^{s-2, p}(M ; \mathbb{R}),$$
where $\beta=\min (m-n / p, 2)$ unless $m=n / p+2$ in which case (5.6) holds with any $\beta<2$.
\begin{itemize}
\item[(b)] Suppose $g=\rho^{-2} \bar{g}$ is an asymptotically hyperbolic metric of class $\mathscr{X}^{s, p ; m}$ satisfying (1.4). If $m \geq 2$ then
\begin{itemize}
\item[(i)] $\operatorname{Riem}[\bar{g}]=\tau_{\text {Riem }}+r_{\text {Riem }}$, where
$$\begin{aligned}
& \tau_{\text {Riem }} \in \mathscr{X}^{\infty ; m-2}\left(M ; T^{2,2} M\right), \\
& r_{\text {Riem }} \in X_{m-2}^{s-2, p}\left(M ; T^{2,2} M\right) .
\end{aligned}$$
\end{itemize}
\end{itemize}
(ii) $\rho^{2} \mathrm{R}[\bar{g}]=\rho^{2} \tau_{\mathrm{R}}+r_{\mathrm{R}}$ where $\tau_{\mathrm{R}} \in \mathscr{X}^{\infty ; m-2}(M ; \mathbb{R})$ and $r_{\mathrm{R}} \in X_{m}^{s-2, p}(M ; \mathbb{R})$. If instead $m=1$, then (i) and (ii) remain true setting $\tau_{\text {Riem }}=0$ and $\tau_{\mathrm{R}}=0$. In all cases
$$\rho^{2} \mathrm{R}[\bar{g}] \in X_{\min (m, 2)}^{s-2, p}(M ; \mathbb{R}) .$$

Proof. The proof relies on writing the curvature operator $\operatorname{Riem}[\bar{g}]$ as a linear combination of contractions of
$$\bar{g}^{-1} \otimes \bar{g}^{-1} \otimes \hat{\nabla}^{2} \bar{g} \quad \text { and } \quad \bar{g}^{-1} \otimes \bar{g}^{-1} \otimes \hat{\nabla} \bar{g} \otimes \bar{g}^{-1} \otimes \hat{\nabla} \bar{g} .$$

If $\bar{g} \in \mathscr{H}^{s, p ; m}(M)$ with $m \geq 2$ then we can apply Proposition 4.11 to conclude each of these terms lies in $\mathscr{H}^{s-2, p ; m-2}(M)$, and hence so does Riem $[\bar{g}]$. Theorem 7.1 then implies the first claim of this case; the second claim follows from the first via contraction and multiplication by $\rho^{2}$. The final claim of the lemma follows from applying Proposition 4.6 to $\mathrm{R}[\bar{g}] \in \mathscr{H}^{s-2, p ; m-2}(M)$ and then multiplying by $\rho^{2}$.
If $\bar{g} \in \mathscr{H}^{s, p ; 1}(M)$ so that $m=1>n / p$, then Proposition 4.6 implies $\bar{g}^{-1} \in X_{-2}^{s, p}(M)$, while by definition we have $\hat{\nabla} \bar{g} \in H_{3-n / p}^{s-1, p}(M)$ and thus $\hat{\nabla}^{2} \bar{g} \in H_{3-n / p}^{s-2, p}(M)$. We then obtain $\operatorname{Riem}[\bar{g}] \in H_{-1-n / p}^{2-s, p}(M)$, which is the first claim in this case; the second claim follows from contraction and multiplying by $\rho^{2}$. The final claim follows from Lemma 3.2.
The cases where $\bar{g} \in \mathscr{X}^{s, p ; m}(M)$ follow from analogous, though simpler, logic. \(\square\)

\section*{6. The Yamabe problem}

The Yamabe problem in the asymptotically hyperbolic setting amounts to the following: starting from an asymptotically hyperbolic metric $g$ we wish to find a conformally related metric that is also asymptotically hyperbolic and that has constant scalar curvature equal to that of hyperbolic space: $\breve{\mathrm{R}}_{n}:=-n(n-1)$. Concretely, we seek a conformal factor $\Theta>0$ such that $\Theta^{q_{n}-2} g$ is asymptotically hyperbolic and such that
$$\mathrm{R}\left[\Theta^{q_{n}-2} g\right]=\breve{\mathrm{R}}_{n} ;$$
here $q_{n}=2 n /(n-2)$ is the critical exponent associated with the Sobolev embedding of $W^{1,2}$ into $L^{q}$ and its use simplifies some later expressions. The standard formula for the conformal change of scalar curvature
$$\mathrm{R}\left[\Theta^{q_{n}-2}\right]=\left(-\left(q_{n}+2\right) \Delta_{g} \Theta+\mathrm{R}[g] \Theta\right) \Theta^{1-q_{n}}$$
allows us to rewrite equation (6.1) as a semilinear PDE for $\Theta$.
One readily verifies that the requirement that $\Theta^{q_{n}-2} g$ be asymptotically hyperbolic imposes the boundary condition $\left.\Theta\right|_{\partial M}=1$. Writing $\Theta=1+u$ with $u$ vanishing on $\partial M$, we rewrite equation (6.1) as a semilinear PDE
$$-a_{n} \Delta_{g} u+\mathrm{R}[g] u=\breve{\mathrm{R}}_{n}\left[(1+u)^{q_{n}-1}-1\right]-\left(\mathrm{R}[g]-\breve{\mathrm{R}}_{n}\right),$$
where $a_{n}=q_{n}+2$, that we wish to solve for $u$.
An important consideration is that the regularity class of the metric should not be changed under the conformal transformation. In particular, the solution metric should be as acceptable a starting point for the construction as the metric we began with. In this section we obtain a unique solution, within the regularity class, of the Yamabe problem for asymptotically hyperbolic metrics of the following classes
$$\begin{aligned}
& \mathscr{H}^{s, p ; m} \text { with } s \geq m>n / p, \\
& \mathscr{X}^{s, p ; m} \text { with } s \geq m \geq 1 \text { and } s>n / p .
\end{aligned}$$

In both cases the restrictions on the parameters ensure the important condition that the compactified metric $\bar{g}=\rho^{2} g$ be Hölder continuous up to the boundary on $\bar{M}$.

To begin, we observe that these classes of metric behave well under conformal changes.
Lemma 6.1. Let $1<p<\infty, s \in \mathbb{R}$ and $m \in \mathbb{N}$.
\begin{itemize}
\item[(a)] Suppose $g$ is an asymptotically hyperbolic metric of class $\mathscr{H}^{s, p ; m}$ with $s \geq m>$ $n / p$. If $\Theta \in \mathscr{H}^{s, p ; m}(M ; \mathbb{R})$ is a conformal factor such that $\left.\Theta\right|_{\partial M}=1$, then $\Theta^{q_{n}-2} g$ is an asymptotically hyperbolic metric of class $\mathscr{H}^{s, p ; m}$. In particular, this holds for $\Theta=1+u$ with $u \in H_{m-n / p}^{s, p}(M ; \mathbb{R})$.
\item[(b)] Suppose $g$ is an asymptotically hyperbolic metric of class $\mathscr{X}^{s, p ; m}$ with $s>n / p$ and $s \geq m \geq 1$. If $\Theta \in \mathscr{X}^{s, p ; m}(M ; \mathbb{R})$ is a conformal factor such that $\left.\Theta\right|_{\partial M}=1$, then $\Theta^{q_{n}-2} g$ is an asymptotically hyperbolic metric of class $\mathscr{X}^{s, p ; m}$. In particular, this holds for $\Theta=1+u$ with $u \in X_{m}^{s, p}(M ; \mathbb{R})$.
\end{itemize}

Proof. The invariance of the regularity classes under the given conformal changes is an easy consequence of Propositions 4.12 and 4.13; the resulting metric is asympotically hyperbolic because $\left.\Theta\right|_{\partial M}=1$ and hence the norm of $d \rho$ with respect to to the new compactified metric is unchanged on $\partial M$. If $u \in H_{m-n / p}^{s, p}(M)$, Lemma 4.5 implies $u \in \mathscr{H}^{s, p ; m}(M)$ and Theorem 7.1 implies $\left.u\right|_{\partial M}=0$. Hence $\Theta=1+u \in \mathscr{H}^{s, p ; m}(M)$ and $\left.\Theta\right|_{\partial M}=1$. An analogous argument works in the $\mathscr{X}^{s, p ; m}$ category if $u \in X_{m}^{s, p}(M)$. \(\square\)

When $g$ is an asymptotically hyperbolic metric of one of the regularity classes (6.4)-(6.5), the Laplacian $\Delta_{g}$ has excellent mapping properties between weighted Sobolev spaces. The limited regularity of the metric restricts the spaces on which the Laplacian can naturally operate, however, and we have the following consequence of Proposition 8.1 and Lemma 8.5 below.

Lemma 6.2. Suppose $1<p<\infty, m \in \mathbb{N}, s \in \mathbb{R}$ and that $g$ is an asymptotically hyperbolic metric in one of the two regularity classes (6.4) and (6.5). Then the Laplacian $\Delta_{g}$ determines continuous maps
$$\begin{aligned}
& H_{\delta}^{\sigma, q}(M ; \mathbb{R}) \rightarrow H_{\delta}^{\sigma-2, q}(M ; \mathbb{R}), \\
& X_{\delta}^{\sigma, q}(M ; \mathbb{R}) \rightarrow X_{\delta}^{\sigma-2, q}(M ; \mathbb{R})
\end{aligned}$$
for any $\delta \in \mathbb{R}$ so long as $(\sigma, q) \in \mathbb{R} \times(1, \infty)$ satisfy
$$\begin{gathered}
2-s \leq \sigma \leq s, t, \\
\frac{1}{p}-\frac{s}{n} \leq \frac{1}{q}-\frac{\sigma}{n} \leq \frac{1}{p^{*}}-\frac{2-s}{n},
\end{gathered}$$
where $p^{*}$ is the Lebesgue exponent conjugate to $p$, i.e. $1 / p+1 / p^{*}=1$.

The restrictions (6.7) arise as a consequence of Proposition 3.11 concerning multiplication in Sobolev spaces ${ }^{1}$. Following the notation of §8, we define the compatible Sobolev indices $\mathcal{S}_{2}^{s, p}$ of $\Delta_{g}$ to be the pairs $(\sigma, q) \in \mathbb{R} \times(1, \infty)$ satisfying conditions (6.7); the subscript 2 in the notation is associated with the fact that the Laplacian is a second-order operator.

The regularity classes (6.4) and (6.5) both require $s \geq 1$ and $s>n / p$. A simple computation shows that under these conditions $\mathcal{S}_{2}^{s, p}$ is non-empty and indeed always contains $(\sigma, q)=(1,2)$ corresponding to $H_{\delta}^{1,2}$. When $s=1$ and $p>n,(\sigma, q) \in \mathcal{S}_{2}^{s, p}$ if and only if $\sigma=1$ and $p^{*} \leq q \leq p$. This minimal level of regularity forms the baseline of our construction. Using the conditions $s \geq 1$ and $s>n / p$ it is easy to see that $2-s \leq 1$ and $1 / p^{*}-(2-s) / n>0$. Hence we find that if $(\sigma, q)$ satisfies
$$\begin{aligned}
1 & \leq \sigma \leq s, \\
\frac{1}{p}-\frac{s}{n} & \leq \frac{1}{q}-\frac{\sigma}{n}<0,
\end{aligned}$$
then $(\sigma, q) \in \mathcal{S}_{2}^{s, p}$. This restricted sufficient condition suffices for all of our purposes in this section and has an easy interpretation: if $\sigma \geq 1$, then $H_{\text {loc }}^{\sigma, q}(M ; \mathbb{R})$ consists of Hölder continuous functions, and $H_{\text {loc }}^{\sigma, q}(M ; \mathbb{R})$ contains $H_{\text {loc }}^{S, p}(M ; \mathbb{R})$.
Our construction employs operators of the form $-\Delta_{g}+\Lambda$, where $\Lambda \in \mathbb{R}$; these evidently also define continuous actions (6.6) for $(\sigma, q) \in \mathcal{S}_{2}^{s, p}$. On hyperbolic space these are Fredholm maps only for a limited range of weights $\delta$ depending on $\Lambda$. Identical restrictions on $\delta$ apply for asymptotically hyperbolic metrics of one of the regularity classes (6.4) and (6.5). Thus we have following consequence of our main results of §9.

Proposition 6.3. Suppose $1<p<\infty, m \in \mathbb{N}, s \in \mathbb{R}$ and that $g$ is an asymptotically hyperbolic metric in one of the regularity classes (6.4), (6.5). Let $\Lambda \geq 0$ and define
$$R=\sqrt{\left(\frac{n-1}{2}\right)^{2}+\Lambda} .$$
Then $-\Delta_{g}+\Lambda$ is an isomorphism
$$H_{\delta}^{\sigma, q}(M ; \mathbb{R}) \rightarrow H_{\delta}^{\sigma-2, q}(M ; \mathbb{R})$$
so long as $(\sigma, q) \in S_{2}^{s, p}$ and
$$\left|\delta+\frac{n-1}{q}-\frac{n-1}{2}\right|<R .$$
Similarly, $-\Delta_{g}+\Lambda$ is an isomorphism
$$X_{\delta}^{\sigma, q}(M) \rightarrow X_{\delta}^{\sigma-2, q}(M)$$

\footnotetext{
${ }^{1}$ In fact, because the Laplacian is missing a low-order term compared to a more general geometric operator such as the conformal Laplacian, conditions (6.7) appearing in Lemma 6.6 could be weakened; see Appendix D.
}
if $(\sigma, q) \in S_{2}^{s, p}$ and
$$\left|\delta-\frac{n-1}{2}\right|<R .$$

Proof. Lemma 7.1 of [Lee06] implies that $R$ defined by equation (6.9) is the indicial radius of $-\Delta_{\check{g}}+\Lambda$ acting on hyperbolic space. So we can apply Theorems 9.7 and 9.10 to find that $-\Delta_{g}+\Lambda$ is a Fredholm map with index zero when acting as in (6.10) or (6.12), so long as $(\sigma, q)$ and $\delta$ satisfy the stated restrictions.
To show these maps are isomorphisms it is enough to show they have trivial kernel. Suppose $u$ is in the kernel of $-\Delta_{g}+\Lambda$. Then $u \in H_{0}^{1,2}(M)$ by Proposition 9.5. A density argument shows integration by parts applies on $H_{0}^{1,2}(M)$ and therefore
$$\int_{M}\left[|d u|_{g}^{2}+\Lambda u^{2}\right] d V_{g}=0$$
Since $\Lambda \geq 0$ we conclude that $u$ is a constant element of $H_{0}^{1,2}(M)$ and therefore 0. \(\square\)

As the constant $R$ defined in (6.9) is the indicial radius for the operator $\mathcal{P}[g]=-\Delta_{g}+\Lambda$, the inequalities (6.11)and (6.13) define the Fredholm ranges of the associated operators, and correspond to (1.9) from the introduction. Note that $R$ is increasing in $\Lambda$, and hence the Fredholm range of the operators grows as $\Lambda$ increases. Two choices of $\Lambda$ play central roles in our construction. First, when $\Lambda=0$ inequalities (6.11)and (6.13) become
$$\begin{aligned}
0< & \delta+\frac{n-1}{q}<n-1, \\
0 & <\delta<n-1,
\end{aligned}$$
respectively. Second, when $\Lambda=n$ a computation shows inequalities (6.11)and (6.13) become
$$\begin{aligned}
-1< & \delta+\frac{n-1}{q}<n, \\
-1 & <\delta<n .
\end{aligned}$$
The Fredholm ranges for $-\Delta+n$ play an especially important role in the construction because equation (6.1) can be rewritten
$$\left(-\Delta_{g}+n\right) u=\frac{\breve{\mathrm{R}}_{n}}{a_{n}}\left[(1+u)^{q_{n}-1}-1-\left(q_{n}-1\right) u\right]+\frac{\breve{\mathrm{R}}_{n}-\mathrm{R}[g]}{a_{n}}(1+u) .$$
If $u$ has some decay at infinity, the first expression on the right-hand side of equation (6.18) vanishes $O\left(u^{2}\right)$ at infinity and hence the known decay of $u$ can be improved up to that of $\mathrm{R}[g]-\breve{\mathrm{R}}_{n}$, but only within the limits imposed by the Fredholm range of $-\Delta_{g}+n$.
6.1. Solution in the $\mathscr{H}^{s, p ; m}$ category. In this section we present the solution of the Yamabe problem for asymptotically hyperbolic metrics of class $\mathscr{H}^{s, p ; m}$. This case is mildly more technical than the corresponding $\mathscr{X}^{s, p ; m}$ construction, and we summarize the changes needed in the $\mathscr{X}^{s, p ; m}$ in the following section.

The construction the consists of three steps:
\begin{itemize}
\item[-] Conditioning at infinity. We perform an initial conformal transformation so that $\mathrm{R}[g]-\breve{\mathrm{R}}_{n}$ has 'rapid' decay: $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{m-n / p}^{s-2, p}(M ; \mathbb{R})$. The notion of rapidity is limited by the regularity of $g$ at infinity. Indeed the decomposition in Proposition 5.1, based on Theorem 7.1, implies that
$$\mathrm{R}[g]=\breve{\mathrm{R}}_{n}+\rho \tau+r,$$
where $\tau \in \mathscr{H}^{\infty, p ; m-1}(M ; \mathbb{R}), r \in H_{m-n / p}^{s-2, p}(M ; \mathbb{R})$, and $\rho \tau \in H_{1-n / p}^{\infty, p}(M ; \mathbb{R})$. In effect, this stage is an asymptotic correction to the scalar curvature to eliminate $\rho \tau$ in this expansion, and no PDEs are solved. Nevertheless the Fredholm range from inequality (6.16) manifests itself and we are able to accomplish the desired correction only if $m \leq n$. Note that this first step is needed only if $m>1$; when $m=1$ then $\rho \tau+r$ from equation (6.19) already lies in $H_{1-n / p}^{s-2, p}(M ; \mathbb{R})$.
\item[-] Candidate solution at low regularity. Having made the conformal change to rapid scalar curvature decay, the comments following equation (6.18) suggest that it is reasonable to seek a solution $u$ of equation (6.18) in $H_{m-n / p}^{s, p}(M ; \mathbb{R})$. If we can find such a solution, the rapid decay of $u$ implies $u \in \mathscr{H}^{s, p ; m}(M ; \mathbb{R})$ and therefore $1+u$ is a suitable conformal factor; see Lemma 6.1. At this stage we seek a somewhat less regular solution. Sobolev embedding implies that asympototically hyperbolic metrics of class $\mathscr{H}^{s, p ; m}$ are also asymptotically hyperbolic of class $\mathscr{H}^{1, q ; 1}$ for some $q>n$ (see details below). Moreover, if there exists a solution of equation (6.18) in $H_{m-n / p}^{s, p}(M ; \mathbb{R})$, then it also lies in $X_{1-n / q}^{1, q}(M ; \mathbb{R})$. Using a barrier method, we construct a solution at this limited level of regularity. As an initial step, we perform a conformal change to continuous scalar curvature satisfying $\mathrm{R}[g] \leq \breve{\mathrm{R}}_{n}$, which facilitates finding suitable barriers.
\item[-] Bootstrap. Having found a solution in $X_{1-n / q}^{1, q}(M ; \mathbb{R})$, a bootstrap is used to improve the regularity up to $X_{1-n / q}^{s, p}(M ; \mathbb{R})$, and then improve the decay to $X_{m-n / p}^{s, p}(M ; \mathbb{R})$ and finally to upgrade to $H_{m-n / p}^{s, p}(M ; \mathbb{R})$. This step uses the structural form of the right-hand side of equation (6.18) to improve the weights and again encounters the restriction $m \leq n$ arising from the Fredholm range.
\end{itemize}

We remark that the obstruction $m \leq n$ is real. In three dimensions, for smooth metrics $g$ a generic solution of (6.3) will be polyhomogeous and contains a term $\rho^{3} \log \rho$, which lies in $H^{3, p}(\bar{M} ; \mathbb{R})$ for all $1<p<\infty$ but does not lie in $H^{4, p}(\bar{M} ; \mathbb{R})$ for any $p>1$; see [ACF92b].
6.1.1. Conditioning at infinity. The following proposition implements the first step of the construction outlined and increases the decay of $\mathrm{R}[g]-\breve{\mathrm{R}}_{n}$ up to a threshold determined
jointly by the regularity of the metric at infinity and the Fredholm range of the shifted Laplacian $-\Delta_{g}+n$.

Proposition 6.4. Suppose $1<p<\infty, m \in \mathbb{N}, s \in \mathbb{R}$, with $s \geq m>n / p$ and $m \leq n$. Given an asymptotically hyperbolic metric $g$ on $M$ of class $\mathscr{H}^{s, p ; m}$ there exists a positive conformal factor $\Theta \in \mathscr{H}^{s, p ; m}(M)$ such that $\left.\Theta\right|_{\partial M}=1$ and such that
$$\mathrm{R}\left[\Theta^{-2} g\right]-\breve{\mathrm{R}}_{n} \in H_{m-n / p}^{s-2, p}(M ; \mathbb{R})$$
Proof. First, if $m=1$ then Proposition 5.1 implies $\mathrm{R}[g] \in H_{m-n / p}^{s-2, p}(M)$ without any additional work. So we can assume $m \geq 2$.
Let $\alpha=\min (1 / 2, m-n / p)$; by hypothesis $\alpha>0$. We claim that if $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in$ $H_{k+\sigma-n / p}^{s-2, p}(M)$ for some integer $0 \leq k \leq m-1$ and some $0 \leq \sigma<1$, then there exists a positive conformal factor $\Theta \in \mathscr{H}^{\infty, p ; m}$ such that $\Theta=1$ along $\partial M$ and such that
$$\mathrm{R}\left[\Theta^{-2} g\right]-\breve{\mathrm{R}}_{n} \in H_{k-n / p+\min (1, \sigma+\alpha)}^{s-2, p}(M) .$$
That is, the decay of $\mathrm{R}\left[\Theta^{-2} g\right]$ can be improved by the amount $\alpha$, up to the next integer above $k$. Assuming the claim, the result now follows by an inductive construction. Proposition 5.1 implies $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{1-n / p}^{s-2, p}(M)$, so we can initially take $k=1$ and $\sigma=0$; note that $k \leq m-1$. Applying the the claim iteratively we can find a sequence of finitely many conformal factors, each in $\mathscr{H}^{s, p ; m}(M)$ and equal to 1 on the boundary, that improve the scalar curvature decay rate to the next integer, and then repeat the process $m-2$ more times until the final scalar curvature lies in $H_{m-n / p}^{s-2, p}(M)$. At each step Lemma 6.1 and Proposition 4.13 ensure that the new metric is asymptotically hyperbolic of class $\mathscr{H}^{s, p ; m}$.

To prove the claim, suppose that for some $1 \leq k \leq m-1$ and $\sigma \in[0,1)$ we have $\mathrm{R}[g]-\breve{\mathrm{R}}_{n} \in H_{k+\sigma-n / p}^{s-2, p}(M)$. From Proposition 5.1 we have $\mathrm{R}[g]=\breve{\mathrm{R}}_{n}+\rho \tau_{0}+r_{0}$, where $r_{0} \in H_{m-n / p}^{s-2, p}(M)$ and $\tau_{0} \in \mathscr{H}^{\infty, p ; m-1}(M)$. Hence
$$\rho \tau_{0}=\mathrm{R}[g]-\breve{\mathrm{R}}_{n}-r_{0} \in H_{k+\sigma-n / p}^{s-2, p}(M) .$$
Lemma 4.3 implies $\rho \widetilde{\tau}_{0} \in \mathscr{H}^{\infty, p ; m}(M)$ as well and therefore Theorem 7.1 implies $\rho \tau_{0}=$ $\rho^{k} \tau+r_{1}$, where $\tau \in \mathscr{H}^{\infty, p, m-k}(M) \cap H_{\sigma-n / p}^{\infty, p}(M)$ and $r_{1} \in H_{m-n / p}^{s-2, p}(M)$. We conclude finally that
$$\mathrm{R}[g]=\breve{\mathrm{R}}_{n}+\rho^{k} \tau+r$$
with $\tau \in \mathscr{H}^{\infty, p ; m-k}(M) \cap H_{\sigma-n / p}^{\infty, p}(M)$ and $r \in H_{m-n / p}^{s-2, p}(M)$, and we seek a conformal change that increases the weight $\sigma-n / p$ appearing in this expression.

For a sufficiently smooth conformal factor $\omega$, possibly vanishing on $\partial M$, a computation shows
$$\mathrm{R}\left[\omega^{-2} \bar{g}\right]-\breve{\mathrm{R}}_{n}=\breve{\mathrm{R}}_{n}\left(|d \omega|_{\bar{g}}^{2}-1\right)+2(n-1) \omega \Delta_{\bar{g}} \omega+\omega^{2} \mathrm{R}[\bar{g}] .$$