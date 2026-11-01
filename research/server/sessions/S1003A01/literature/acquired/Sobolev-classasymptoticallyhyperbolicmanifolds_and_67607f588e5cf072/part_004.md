---
retention_scope: session
part: 4
total_parts: 7
---

[Part 4/7 of: Sobolev-classasymptoticallyhyperbolicmanifolds and]

Lemma 7.10. Suppose $1<p<\infty$ and $k \in \mathbb{N}$. For $u \in C^{\infty}(\mathbb{H})$ define
$$S_{k}(u)=\sum_{j=0}^{k-1} \frac{(-1)^{j} y^{j}}{j!} \partial_{y}^{j} u .$$
\begin{itemize}
\item[(a)] If $u \in \mathscr{H}^{\infty, p ; k}(\mathbb{H} \mid y)$ then $S_{k}(u) \in \mathscr{H}^{\infty, p ; k}(\mathbb{H} \mid y)$.
\item[(b)] If $u \in \mathscr{X}^{\infty ; k}(\mathbb{H} \mid y)$ then $S_{k}(u) \in \mathscr{X}^{\infty ; k}(\mathbb{H} \mid y)$.
\item[(c)] In either case (a) or case (b) we have
$$\left.\partial_{y}^{j}\left[\frac{y^{\ell}}{\ell!} S_{k}(u)\right]\right|_{y=0}= \begin{cases}0 & 0 \leq j \leq k+\ell-1, \quad j \neq \ell \\ \left.u\right|_{y=0} & j=\ell\end{cases}$$
for each $\ell \in \mathbb{Z}_{\geq 0}$.
\end{itemize}

Proof. Parts (a) and (b) follow from the properties of $\mathscr{H}^{s, p ; k}(\mathbb{H} \mid y)$ and $\mathscr{X}^{s, p ; k}(\mathbb{H} \mid y)$ discussed at the beginning of §7. We prove part (c) in the case that $u \in \mathscr{H}^{\infty, p ; k}(\mathbb{H} \mid y)$; the proof of the other case follows from analogous logic.
First consider the case $\ell=0$. If $1 \leq j \leq k-1$ then
$$y^{j} \partial_{y}^{j} u \in \mathscr{H}^{\infty, p ; k}(\mathbb{H} \mid y) \cap H_{j-n / p}^{\infty, p}(\mathbb{H} \mid y)$$
and Proposition 7.4 implies $\left.y^{j} \partial_{y}^{j} u\right|_{y=0}=0$. Hence $\left.S_{k}(u)\right|_{y=0}=\left.u\right|_{y=0}$. Moreover, direct computation shows that, since $\partial_{y}^{k} u \in \mathscr{H}^{\infty, p ; 0}(\mathbb{H} \mid y)=H_{-n / p}^{\infty, p}(\mathbb{H} \mid y)$, we have
$$\partial_{y} S_{k}(u)=\frac{(-1)^{k-1}}{(k-1)!} y^{k-1} \partial_{y}^{k} u \in H_{k-1-n / p}^{\infty, p}(\mathbb{H} \mid y) .$$
So Proposition 7.4 implies $\left.\partial_{y}^{k} S_{k}(u)\right|_{y=0}=0$ for $1 \leq j \leq k-1$. This proves the result for $\ell=0$, and the result for $\ell>0$ is a straightforward inductive argument with the $\ell=0$ case as the base case. \(\square\)

Theorem 7.11. Suppose $1<p<\infty, m \in \mathbb{N}, s \in \mathbb{R}$ with $s \geq m$.
\begin{itemize}
\item[(a)] Given $u \in \mathscr{H}^{s, p ; m}(\mathbb{H} \mid y)$ there exist $u_{0}, \ldots, u_{m-1}$ such that for each $0 \leq k \leq m-1$
\begin{itemize}
\item[(i)] $u_{k} \in \mathscr{H}^{\infty, p ; m-k}(\mathbb{H} \mid y)$,
\item[(ii)] $\left.u_{k}\right|_{y=0}=\left.\partial_{y}^{k} u\right|_{y=0}$,
\item[(iii)] $u_{k}=0$ if $\left.\partial_{y}^{k} u\right|_{y=0}=0$,
\item[(iv)] The function $P_{k}[u]=\sum_{j=0}^{k}\left(y^{j} / j!\right) u_{j} \in \mathscr{H}^{\infty, p ; m}(\mathbb{H} \mid y)$ and
\begin{itemize}
\item[(i)] $u-P_{k}[u] \in H_{k+1-n / p}^{s, p}(\mathbb{H} \mid y)$,
\item[(ii)] $\left.\partial_{y}^{j} P_{k}[u]\right|_{y=0}=0, k+1 \leq j \leq m-1$.
\end{itemize}
\item[(iii)] If $u \in H_{\sigma-n / p}^{s, p}(\mathbb{H} \mid y)$ for some $\sigma \in \mathbb{R}$ then then $P_{k}[u] \in H_{\sigma-n / p}^{\infty, p}(\mathbb{H} \mid y)$.
\end{itemize}
In particular, $P_{m-1}[u] \in \mathscr{H}^{\infty, p ; m}(\mathbb{H} \mid y)$ and $u=P_{m-1}[u]+H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$.
\end{itemize}
\begin{itemize}
\item[(b)] Given $u \in \mathscr{X}^{s, p ; m}(\mathbb{H} \mid y)$ there exist $u_{0}, \ldots, u_{m-1}$ such that for each $0 \leq k \leq m-1$
\begin{itemize}
\item[(i)] $u_{k} \in \mathscr{X}^{\infty ; m-k}(\mathbb{H} \mid y)$,
\item[(ii)] $\left.u_{k}\right|_{y=0}=\left.\partial_{y}^{k} u\right|_{y=0}$,
\item[(iii)] $u_{k}=0$ if $\left.\partial_{y}^{k} u\right|_{y=0}=0$,
\item[(iv)] The function $P_{k}[u]=\sum_{j=0}^{k}\left(y^{j} / j!\right) u_{j} \in \mathscr{X}^{\infty ; m}(\mathbb{H} \mid y)$ and
\begin{itemize}
\item[(i)] $u-P_{k}[u] \in X_{k+1}^{s, p}(\mathbb{H} \mid y)$,
\item[(ii)] $\left.\partial_{y}^{j} P_{k}[u]\right|_{y=0}=0, k+1 \leq j \leq m-1$.
\item[(iii)] If $u \in X_{\sigma}^{s, p}(\mathbb{H} \mid y)$ for some $\sigma \in \mathbb{R}$ then then $P_{k}[u] \in X_{\sigma}^{\infty}(\mathbb{H} \mid y)$. In particular, $P_{m-1}[u] \in \mathscr{X}^{\infty ; m}(\mathbb{H} \mid y)$ and $u=P_{m-1}[u]+X_{m}^{s, p}(\mathbb{H} \mid y)$.
\end{itemize}
\end{itemize}
\end{itemize}

Proof. The proofs of parts (a) and (b) are essentially the same, and we focus on part (a). For $0 \leq k \leq m-1$ define
$$u_{k}= \begin{cases}0 & \left.\partial_{y}^{k} u\right|_{\partial H} \equiv 0 \\ S_{m-k}\left(\partial_{y}^{k} u * \psi\right) & \text { otherwise }\end{cases}$$
Here $S_{m-k}$ is the map defined in Lemma 7.10. Note that $\partial_{y}^{k} u \in \mathscr{H}^{s-k, p ; m-k}(\mathbb{H} \mid y)$, so Proposition 7.7 (c) and Lemma 7.10 ensure $u_{k} \in \mathscr{H}^{\infty, p ; m-k}(\mathbb{H} \mid y)$. Since $m-k \geq 1$, Lemma 7.9, Proposition 7.4 and Lemma 7.10 imply $\left.u_{k}\right|_{y=0}=\left.\partial_{y}^{k} u\right|_{y=0}$.
The properties of $\mathscr{H}^{s, p ; m}(\mathbb{H} \mid y)$ at the beginning of this section imply that $P_{k}[u]=\sum_{j=0}^{k}\left(y^{j} / j!\right) u_{j} \in$ $\mathscr{H}^{\infty, p ; m}(\mathbb{H} \mid y)$ for $0 \leq k \leq m-1$. Thus using Lemma 7.10 we compute
$$\left.\partial_{y}^{j} P_{k}[u]\right|_{y=0}= \begin{cases}\left.\partial_{y}^{j} u\right|_{y=0} & 0 \leq j \leq k \\ 0 & k+1 \leq j \leq m-1 .\end{cases}$$
Note that the above computation remains valid even for those values of $j$ where $\left.\partial_{y}^{j} u\right|_{y=0} \equiv$ 0 . As a consequence we find $\left.\partial_{y}^{j}\left(u-P_{k}[u]\right)\right|_{y=0}=0$ for $0 \leq j \leq k$, and Proposition 7.4 implies $u-P_{k}[u] \in H_{k+1-n / p}^{s, p}(\mathbb{H} \mid y)$.
Concerning the decay rate of $P_{k}[u]$, suppose $u \in H_{\sigma-n / p}^{s, p}(\mathbb{H} \mid y)$. If $\sigma \leq 0$ then $P_{k}[u] \in$ $H_{\sigma-n / p}^{\infty, p}(\mathbb{H} \mid y)$ trivially and if $\sigma \geq m$ then Proposition 7.4 implies $\left.\partial_{j} u\right|_{\partial \mathbb{H}}=0,0 \leq j \leq m-1$ and therefore $P_{k}[u]=0 \in H_{\sigma-n / p}^{\infty, p}(\mathbb{H} \mid y)$.
If $0<\sigma<m$, let $j=\lfloor\sigma\rfloor$ and observe that $0 \leq j \leq m-1$. Proposition 7.4 implies $u_{i} \equiv 0$ if $i<j$, whereas if $j<i \leq m-1$ then $y^{i} u_{i} \in H_{i-n / p}^{\infty, p}(\mathbb{H} \mid y) \subset H_{\sigma-n / p}^{\infty, p}(\mathbb{H} \mid y)$. So it suffices to show that $y^{j} u_{j} \in H_{\sigma-n / p}^{\infty, p}(\mathbb{H} \mid y)$.
Recall $u_{j}=S_{m-j}\left(\left(\partial_{j} u\right) * \psi\right)$. Since $\partial_{j} u \in H_{\sigma-j-n / p}^{s-j, p}(\mathbb{H} \mid y)$ Proposition 7.7(a) implies $\left(\partial_{j} u\right) * \psi \in H_{\sigma-j-n / p}^{\infty, p}(\mathbb{H} \mid y)$. The proof of Lemma 7.10 shows
$$S_{m-j}\left(\left(\partial_{j} u\right) * \psi\right)=\left(\partial_{j} u\right) * \psi+H_{1-n / p}^{\infty, p}(\mathbb{H} \mid y)$$
and since $\sigma-j \leq 1$ we conclude $u_{j} \in H_{\sigma-j-n / p}^{\infty, p}(\mathbb{H} \mid y)$ and $y^{j} u_{j} \in H_{\sigma-n / p}^{\infty, p}(\mathbb{H} \mid y)$ as required. \(\square\)

The fine details of the asymptotic expansions of Theorem 7.11 do not translate to to general manifolds without assuming additional structure near $\partial M$ to make sense of higher order derivatives. Nevertheless, we obtain Theorem 7.1.

Proof of Theorem 7.1. We prove part (a) concerning $\mathscr{H}^{s, p ; m}(M ; E)$; the Gicquaud-Sakovich case is proved similarly. Using a partition of unity it suffices to show that the result holds for tensors with bounded support in a single coordinate chart at infinity. When $m=0$, we can take $\tau=0$ and $r=u$ and the result is simply a consequence of the definition of the space $\mathscr{H}^{s, p ; 0}(M ; E)$. Otherwise, the technique of Lemma A. 21 implies each of the components $u_{A}^{B}$ of $u$ relative to the coordinates at infinity lie in $\mathscr{H}^{s, p ; m}(\mathbb{H} \mid y)$ with $m \geq 1$ and Theorem 7.11 implies we can write
$$u_{A}^{B}=\tau_{A}^{B}+r_{A}^{B}$$
with $\tau_{A}^{B}=P_{m}\left[u_{A}^{B}\right] \in \mathscr{H}^{\infty, p ; m}(\mathbb{H} \mid y)$ and $r_{A}^{B} \in H_{m-n / p}^{s, p}(\mathbb{H} \mid y)$.
Suppose now that $u$ has additional decay, specifically that each $u_{A}^{B} \in H_{k+\alpha-n / p}^{s, p}(\mathbb{H} \mid y)$ for some integer $0 \leq k \leq m-1$ and some $\alpha \in[0,1)$. We wish to show that $\tau_{A}^{B} \in$ $y^{k}\left(\mathscr{H}^{s, p ; m-k}(\mathbb{H} \mid y) \cap H_{\alpha}^{\infty, p}(\mathbb{H} \mid y)\right.$ Theorem 7.11 implies $\tau_{A}^{B}=P_{m}\left[u_{A}^{B}\right] \in H_{k+\alpha}^{\infty, p}(\mathbb{H} \mid y)=$ $y^{k} H_{\alpha}^{\infty, p}(\mathbb{H} \mid y)$ which finishes the proof if $k=0$. If $k>0$ then Proposition 7.4 implies that the traces $\left.\partial_{y}^{j} u_{A}^{B}\right|_{y=0}$ vanish for $0 \leq j \leq k-1$. But then $\tau_{A}^{B}$ has the form $\sum_{j=k}^{m}\left(y^{j} / j!\right) a_{j}$ where each $a_{j} \in \mathscr{H}^{\infty, p ; m-j}(\mathbb{H} \mid y)$. Observe that for each $j \geq k$
$$y^{-k} y^{j} a_{j} \in \mathscr{H}^{\infty, p ; m-j+(j-k)}(\mathbb{H} \mid y)=\mathscr{H}^{\infty, p ; m-k}(\mathbb{H} \mid y)$$
and hence $\tau_{A}^{B} \in y^{k} \mathscr{H}^{\infty, p ; m-k}(\mathbb{H} \mid y)$ as required.
Finally, the fact that for $m \geq 1$ that $\left.u\right|_{\partial M}=0$ if and only if $u \in H_{1-n / p}^{s, p}(\mathbb{H} \mid y)$ follows from Proposition 7.4. \(\square\)

\section*{8. Elliptic Differential operators}

In this section, we establish a priori estimates for operators $\mathcal{P}[g]$ satisfying Assumptions P and I of the introduction, where $g$ is an asymptotically hyperbolic metric of either class (1.3) or class (1.4). The main result is Proposition 8.16, which implies that these operators are semi-Fredholm and which is used in §9 to obtain a Fredholm theory for such operators. In the course of obtaining Proposition 8.16 we also develop some of the machinery needed to build the parametrices used to obtain the full Fredholm theory; see especially §8.5.

Many of the results leading to Proposition 8.16 do not require every point in Assumptions P. For example, the self-adjoint property is not required by any of the intermediate results. However, for simplicity of exposition, we frequently invoke Assumption P in its entirety.
8.1. Linear differential operators. We begin with a discussion of the mapping properties of a rather general class of differential operators having coefficients in Gicquaud-Sakovich spaces. Recall from §3 the reference connection $\hat{\nabla}$ on $\bar{M}$. We say that a linear differential operator $L$, taking sections of a tensor bundle $E$ to sections of tensor bundle $F$ over $M$, is of class $\mathcal{L}_{\boldsymbol{d}}^{\boldsymbol{s}, \boldsymbol{p}}$ for some $s \in \mathbb{R}$ and $1<p<\infty$ if it has the form
$$L=\sum_{0 \leq k \leq d} a_{k} \cdot \hat{\nabla}^{k},$$
where the dot indicates tensor contraction, and where each $a_{k} \in X_{0}^{s-d+k, p}\left(M ; T^{*, *} M\right)$ as a section of its $k$-dependent bundle. These operators determine maps from $C^{\infty}(M ; E)$ to distributions $\mathcal{D}^{\prime}(M ; F)$ and we would like to expand the domain to various Sobolev spaces. When $s>n / p$, and hence $X_{0}^{s, p}(M ; \mathbb{R})$ is an algebra, repeated applications of Proposition 3.11 yield the following.

Proposition 8.1. Suppose $1<p, q<\infty, \delta \in \mathbb{R}, s>n / p, \sigma \in \mathbb{R}$ and $d \in \mathbb{N}_{\geq 0}$. An operator $L=\sum_{k=0}^{d} a_{k} \cdot \hat{\nabla}^{k}$ of class $\mathcal{L}_{d}^{s, p}$ extends to continuous linear maps
$$\begin{aligned}
& H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma-d, q}(M ; F), \\
& X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma-d, q}(M ; F)
\end{aligned}$$
so long as
$$\begin{gathered}
d-s \leq \sigma \leq s, \\
\frac{1}{p}-\frac{s}{n} \leq \frac{1}{q}-\frac{\sigma}{n} \leq \frac{1}{p^{*}}-\frac{d-s}{n} .
\end{gathered}$$
Moreover, viewed as a map between these spaces, $L$ depends continuously on its coefficients $a_{k} \in X_{0}^{s-d+k}\left(M ; T^{*, *} M\right)$.

It is convenient to have notation for the Sobolev indices satisfying conditions (8.2). Given $1<p<\infty, s \in \mathbb{R}$ and $d \in \mathbb{N}_{\geq 0}$, the compatible Sobolev indices $\mathcal{S}_{d}^{s, p}$ for an operator of class $\mathcal{L}_{d}^{s, p}$ is the set of tuples $(\sigma, q) \in \mathbb{R} \times(1, \infty)$ satisfying (8.2).
For a general choice of $s, p, d$, the set $\mathcal{S}_{d}^{s, p}$ may be empty. The following lemma provides conditions that guarantee that $\mathcal{S}_{d}^{s, p}$ is nontrivial and is proved identically to its counterpart in [HMT22], using Lemma 3.2 and Proposition 3.3 to establish the embeddings.

Lemma 8.2. Suppose $1<p<\infty, s \in \mathbb{R}$ and $d \in \mathbb{N}_{\geq 0}$. Then $\mathcal{S}_{d}^{s, p}$ is nonempty if and only if
$$s \geq \frac{d}{2} \quad \text { and } \quad \frac{1}{p}-\frac{s}{n} \leq \frac{1}{2}-\frac{d / 2}{n} .$$
Consequently:
\begin{itemize}
\item[(a)] If $n \geq 2, s \geq 1$, and $s>n / p$, then $\mathcal{S}_{2}^{s, p}$ is non-empty.
\item[(b)] If $\mathcal{S}_{d}^{s, p}$ is non-empty, then it contains $(s, p),\left(d-s, p^{*}\right)$, and $(d / 2,2)$.
\end{itemize}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/ef5a0d66-5cf7-49a6-8baf-1ceeba55704c-073.jpg?height=749&width=1029&top_left_y=357&top_left_x=547}
\captionsetup{labelformat=empty}
\caption{Figure 2. The region $\mathcal{S}_{d}^{s, p}$ for $n=3, d_{0}=0, d=2, p=1.7$ and $s=\frac{n}{p}+\frac{1}{2}$.}
\end{figure}
\begin{itemize}
\item[(c)] If $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$, then for any $\delta \in \mathbb{R}$ and $\varepsilon>0$ we have the continuous inclusions for any tensor bundle $E$ over $M$
$$\begin{aligned}
H_{\delta+\frac{n-1}{p}}^{s, p} & (M ; E) \hookrightarrow H_{\delta+\frac{n-1}{q}+\varepsilon}^{\sigma, q}(M ; E) \hookrightarrow H_{\delta+\frac{n-1}{p^{*}}+2 \varepsilon}^{d-s, p^{*}}(M ; E), \\
& X_{\delta}^{s, p}(M ; E) \hookrightarrow X_{\delta}^{\sigma, q}(M ; E) \hookrightarrow X_{\delta}^{d-s, p^{*}}(M ; E) .
\end{aligned}$$
\end{itemize}
The main conclusion of Lemma 8.2 is striking: $\mathcal{S}_{d}^{s, p}$ is nonempty if and only if it contains $(d / 2,2)$, which corresponds to a weak $L^{2}$ theory (e.g., $W^{1,2}$ for a second-order operator). We therefore call (8.3) the weak $\boldsymbol{L}^{\mathbf{2}}$ condition and reiterate that it always holds for a secondorder operator when $n \geq 2, s \geq 1$, and $s>n / p$.
If $s>n / p$ then the highest-order coefficients of an operator $L \in \mathcal{L}_{d}^{s, p}$ are continuous. We say that $L$ is elliptic on open set $U$ if at each point the principle operator $a_{d} \cdot \hat{\nabla}^{d}$ is elliptic in the usual sense. If $U$ is an open set in $M$, we let $H^{s, p}(U ; E)$ be the quotient space of $H_{0}^{s, p}(M ; E)$, where two sections are identified if they agree as distributions on $U$; this construction is analogous to the definition of Bessel potential spaces on open subsets of $\mathbb{R}^{n}$. The local elliptic regularity theorem of [HMT22] then readily implies the following interior estimate.

Proposition 8.3. Suppose $1<p<\infty, s \in \mathbb{R}$ with $s>n / p$, and $d \in \mathbb{N}_{\geq 0}$. Suppose $L$ is a differential operator of class $\mathcal{L}_{d}^{s, p}$, acting sections of tensor bundle $E$ over $M$, that is elliptic on some precompact open set $U$. If $u \in H^{d-s, p^{*}}(U ; E)$ and $L u \in H^{\sigma-d, q}(U ; E)$ for some $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$, then for any open set $V$ with $\bar{V} \subset U$, we have $u \in H^{\sigma, q}(V ; E)$ and
$$\|u\|_{H^{\sigma, q}(V ; E)} \lesssim\|L u\|_{H^{\sigma-d, q}(U ; E)}+\|u\|_{H^{d-s-1, p^{*}}(U ; E)},$$
where the implicit constant depends on $U$ and $V$.
We have the following commutator result; note the factor of $\rho^{-1}$, which is essential in our applications.
Lemma 8.4. Suppose $L$ is a differential operator of class $\mathcal{L}_{d}^{s, p}$ on sections of tensor bundle $E$ over $M$. If $\phi$ is a smooth function on $\bar{M}$ then
$$\rho^{-1}[L, \phi] \in \mathcal{L}_{d-1}^{s, p} .$$
between the same bundles. In particular, if $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$, it determines continuous linear maps $H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma-d+1, q}(M ; E)$ and $X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma-d+1, q}(M ; E)$.

Proof. Since $\phi \in C^{\infty}(\bar{M})$, and since $\hat{\nabla}^{k} \phi$ is a tensor of weight $k$, Lemma 3.15 implies $\rho^{-1} \hat{\nabla}^{k} \phi \in C_{k-1}^{\infty}(M) \subset C_{0}^{\infty}(M)$ for any $k \geq 1$. Noting that all the coefficients of $[L, \phi]$ involve at least one derivative of $\phi$, the sum decomposition (8.1) of $[L, \phi]$ is then a straightforward computation. Verification of the mapping property follows from the fact that $\mathcal{S}_{d-1}^{s, p} \supset \mathcal{S}_{d}^{s, p}$. \(\square\)
8.2. Geometric operators and Assumption P. We now discuss the contents of Assumption P in more detail, and show that results of §8.1 apply to such operators. We assume that $g$ is an asymptotically hyperbolic metric satisfying either
\begin{itemize}
\item[-] assumption (1.3), in which $\bar{g} \in \mathscr{H}^{s, p ; m}\left(M ; T^{0,2} M\right)$ with $s \geq m>n / p$ and $1<p<$ $\infty$; or
\item[-] assumption (1.4), in which $\bar{g} \in \mathscr{X}^{s, p ; m}\left(M ; T^{0,2} M\right)$ with $s \geq m \geq 1, s>n / p$, and $1<p<\infty$.
\end{itemize}
For such a metric, we consider $d^{\text {th }}$-order differential operator $\mathcal{P}[g]$ satisfying a list of assumptions that we now explain.
The first part of Assumption P is that $\mathcal{P}[g]$ acts on sections of a geometric tensor bundle $E$ over $M$, yielding sections of that same bundle. It is important that, as noted in (1.6), under either of the regularity conditions above imply we have $\bar{g} \in C^{0, \alpha}\left(\bar{M} ; T^{0,2} M\right)$ for some $0<\alpha \leq 1$, and thus the discussion of geometric tensor bundles in §3.7 applies. That $\bar{g}$ is Hölder continuous on $\bar{M}$ for positive $\alpha$, and not merely continuous, is essential for estimates of §8.3, and subsequent Fredholm theory of §9.

The second part of Assumption P is that $\mathcal{P}[g]$ is geometric, so that in any coordinate system $\mathcal{P}[g] u$ is a linear function of the components of $u$ and their derivatives up to order $d$, and such that the coefficients are universal polynomials in the components of $g$, their derivatives, and $\operatorname{det}\left(g_{i j}\right)^{-1 / 2}$. It is further required that the coefficient of any $k^{\text {th }}$ derivative of $u$ involves at most the the first $d-k$ derivatives of $g$. As is discussed §8.3 below, this assumption allows us to compare $\mathcal{P}[g]$ with the corresponding operator defined on hyperbolic space.

Due to restrictions imposed by multiplication in Sobolev spaces (see Proposition 3.11) we are obliged to consider a smaller class of operators, in order to ensure that $\mathcal{P}[g]$ be of class
$\mathcal{L}_{d}^{s, p}$. This motivates the third part of Assumption P, that $\mathcal{P}[g]$ be scale natural. Thus each term in the polynomial comprising the coefficient of any $k^{\text {th }}$ derivative of $u$ has a total of at most $d-k$ metric derivatives distributed over all the factors comprising the coefficient. As noted in the introduction, although $\Delta_{g}+\mathrm{R}[g]^{2}$ is a geometric second-order operator, it is not scale natural because the low-order coefficient contains terms with a total of four metric derivatives ( $\partial^{2} g \partial^{2} g$, etc.). On the other hand, $\Delta_{g}+\mathrm{R}[g]$ is scale natural.
Using these assumptions, along with the fifth point of Assumption P, which is that the weak $L^{2}$ condition is satisfied, we see $\mathcal{P}[g]$ is indeed an operator of class $\mathcal{L}_{d}^{s, p}$.

Lemma 8.5. Let $g$ be an asymptotically hyperbolic metric of either class (1.3) or class (1.4), and suppose that $\mathcal{P}[g]$ satisfies Assumption $P$. Then $\mathcal{P}[g]$ is of class $\mathcal{L}_{d}^{s, p}$.
Furthermore, writing
$$\mathcal{P}[g]=\sum_{k=0}^{d} a_{k}[g] \cdot \hat{\nabla}^{k},$$
each map $g \mapsto a_{k}[g]$ is Lipschitz continuous at $g$ as a map taking a neighborhood of $g$ in $X_{0}^{s, p}\left(M ; T^{0,2} M\right)$ to $X_{0}^{s-d+k, p}\left(M ; T^{*, *} M\right)$.

Proof. Consider a Möbius parametrization $\Phi_{i}$. From the definition of a geometric operator
$$\Phi_{i}^{*} \mathcal{P}[g]=\sum_{k=0}^{d} \Phi_{i}^{*}\left(a_{k}\left[\Phi_{i}^{*} g\right]\right) \cdot\left(\Phi_{i}^{*} \hat{\nabla}\right)^{k}=\sum_{k=0}^{d} b_{k}\left[\Phi_{i}^{*} g\right] \cdot \nabla_{\mathbb{E}}^{k}=\sum_{k=0}^{d} b_{k}\left[\Phi_{i}^{*} g\right] \cdot\left(\Phi_{i}^{*} \hat{\nabla}-D\right)^{k},$$
where $D$ is the difference tensor $\Phi_{i}^{*} \hat{\nabla}-\nabla_{\mathbb{E}}$ and where each component of $b_{k}\left[g_{i}\right]$ is a polynomial in components of $g_{i}=\Phi_{i}^{*} g$, their derivatives, and $\operatorname{det}\left(g_{i}\right)^{-1 / 2}$. The uniform estimates for $D$ from Lemma 3.6 allows us to ignore these terms and the result follows if we can establish uniform bounds for the coefficients
$$\left\|b_{k}\left[g_{i}\right]\right\|_{H^{s-d+k, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim 1$$
along with a Lipschitz estimate
$$\| b_{k}\left[g_{i}+\delta g_{i}\right]-b_{k}\left[g_{i}\left\|_{H^{s-d+k, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\right\| \delta g_{i} \|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)},\right.$$
where the implicit constants are independent of $i$, and where inequality (8.8) holds when $\left\|\delta g_{i}\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \leq c$ for some $c$ independent of $i$.
Let $c\left[g_{i}\right]\left(\operatorname{det} g_{i}\right)^{-\ell / 2}$ be a term of the polynomial defining a component of $b_{k}\left[g_{i}\right]$, where $\ell \in$ $\mathbb{N}_{\geq 0}$ and where $c\left[g_{i}\right]$ consists of a product of components of $g_{i}$ and their derivatives. Since $s>n / p$, since no more than $d-k$ derivatives appear among the factors of $c\left[g_{i}\right]$, and since the weak $L^{2}$ condition holds, the local coordinate equivalent of Corollary 3.12 shows that $c\left[g_{i}\right] \in H^{s-d+k, p}\left(B_{1}^{\mathbb{H}}\right)$ with a norm that is uniformly estimated in terms of $\|g\|_{X_{0}^{s, p}\left(M ; T^{0,2} M\right)}$, and that the map $g_{i} \rightarrow c\left[g_{i}\right]$ is Lipschitz at $g_{i}$ with a constant estimated in terms of an upper bound for $\left\|g_{i}\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)}$ so long as the perturbation $\delta g_{i}$ satisfies $\left\|\delta g_{i}\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \leq K$ for any fixed choice of $K$.

Since $s>n / p$, (and since the weak $L^{2}$ condition is satisfied and since $k \leq d$ ), a multiplication argument shows that the proof is complete if we can show that $\delta g \mapsto \operatorname{det}\left(g_{i}+\delta g\right)^{-1 / 2}$ is Lipschitz continuous into $H^{s, p}\left(B_{1}^{\mathbb{H}}\right)$ on a ball containing 0 of size independent of $i$. To do so, first observe that $\operatorname{det}\left(g_{i}\right) \geq \varepsilon>0$ for some $\varepsilon$ independent of $i$. Indeed, writing $\bar{g}=$ $\bar{g}_{a b} d \Theta^{a} d \Theta^{b}$ in the coordinates near infinity corresponding to $\Phi_{i}, \operatorname{det}\left(g_{i}\right)=y^{-n} \operatorname{det}\left(\bar{g}_{a b} \circ \Phi_{i}\right)$ which along with the continuity of $\bar{g}$ establishes the desired lower bound on $B_{1}^{\mathbb{H}}$. Since $H^{s, p}\left(B_{1}^{\mathbb{H}}\right)$ embeds into the continuous functions on $B_{1}^{\mathbb{H}}$, if $\|\delta g\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \leq c$ for some $c$ sufficiently small (depending on $\varepsilon$ but independent of $i$ ), we can ensure that $\operatorname{det}\left(g_{i}+\delta g\right)>\varepsilon / 2$. This lower bound, along with the obvious control of $\operatorname{det}\left(g_{i}+\delta g\right)$ in $H^{s, p}\left(B_{1}^{\mathbb{H}}\right)$, allows us to apply Lemma A. 12 to conclude $\delta g \mapsto \operatorname{det}\left(g_{i}+\delta g\right)^{-1 / 2}$ is Lipschitz continuous in $\delta g$ if $\|\delta g\|_{H^{s, p}\left(B_{1}^{\mathrm{H}}\right)} \leq c$ as required. \(\square\)

Assumption P concludes with one final hypothesis, that $\mathcal{P}[g]$ is formally self-adjoint in the sense that for all sections $u, v \in H_{0}^{s, p}(M ; E)$ we have
$$\int_{M}\langle u, \mathcal{P}[g] v\rangle_{g} d V_{g}=\int_{M}\langle\mathcal{P}[g] u, v\rangle_{g} d V_{g} .$$
Note that if $s<d$ the integrals above should be interpreted in the sense of the duality pairing from §3.8, and a computation using the weak $L^{2}$ condition shows that the pairing is well defined for $u, v \in H_{0}^{s, p}(M ; E)$. We emphasize that the self-adjoint assumption is not, in fact, used until §8.6. However, for simplicity of exposition we invoke Assumption P in its entirety in the intervening results.
8.3. Boundary decay estimates. Our technique for obtaining semi-Fredholm estimates for $\mathcal{P}[g]$ involves localizing the operator at points at infinity where elliptic estimates for $\mathcal{P}[\breve{g}]$ are used instead. In order to accomplish this, we require that $g$ can be approximated by a metric isometric to $\breve{g}$ at points of $M$ sufficiently close to $\partial M$. The following lemma is the key technical tool needed to ensure the requisite decay, and in the $\mathscr{H}^{s, p ; m}$ case can be thought of as a refinement of Proposition 4.6.

Lemma 8.6 (cf. Lemma 6.1 in [Lee06] ). Let $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}, s \geq m>$ $n / p$. Suppose $u \in \mathscr{H}^{s, p ; m}(M ; E)$ is a tensor of weight $w$ and thus by Proposition 4.7 $u \in C^{0, \alpha}(\bar{M} ; E)$ for some $\alpha \in(0,1]$. If $\Phi_{i}$ is a Möbius parametrization with image $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ intersecting $Z_{r}(\hat{p})$ for some $0<r<r_{0}$ then
$$\rho_{i}^{-w}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim r^{\alpha}\|u\|_{\mathscr{H}^{s, p ; m}(M ; E)},$$
with implicit constant independent of $i, \hat{p}, r$ and $u$.
An analogous statement holds if instead $s>n / p$ and $s \geq m \geq 1$ and $u \in \mathscr{X}^{s, p ; m}(M ; E)$.
Proof. Lemma 3.8, which follows from the Gagliardi-Nirenberg inequality, implies
$$\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\Phi_{i}^{*} u\right\|_{H^{0, p}\left(B_{1}^{\mathbb{H}}\right)}+\left\|\nabla_{\mathbb{E}}^{m} \Phi_{i}^{*} u\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{H}}\right)} .$$
To estimate the first term on the right-hand side of equation (8.9) we rely on the embedding $\mathscr{H}^{s, p ; m}(M) \hookrightarrow C^{0, \alpha}(\bar{M})$.

Since the geodesic distance from $\hat{p}$ to a point in $Z_{r}(\hat{p})$ is controlled uniformly by $r$, and since $\operatorname{diam}_{\hat{g}} \Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \lesssim r$,
$$|u|_{\hat{g}} \lesssim r^{\alpha}\|u\|_{\mathscr{H}^{s, p ; m}(M)}$$
on $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$. Using the fact that $\Phi_{i}^{*} \check{g}$ is uniformly close to the Euclidean metric on $B_{1}^{\mathbb{H}}$ and the identity $|u|_{\check{g}}=\rho^{w}|u|_{\hat{g}} \sim \rho_{i}^{w}|u|_{\hat{g}}$ on $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ we find
$$\left\|\Phi_{i}^{*} u\right\|_{H^{0, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\Phi_{i}^{*}|u|_{\vec{g}}\right\|_{H^{0, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim \rho_{i}^{w}\left\|\Phi_{i}^{*}|u|_{\hat{g}}\right\|_{H^{0, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim \rho_{i}^{w} r^{\alpha}\|u\|_{\mathscr{H} \mathscr{E}^{s, p ; m}(M)}$$
as required.
To estimate the second term on the right-hand side of equation, we claim that for each $0 \leq k \leq m$ that $\left\|\nabla_{\mathbb{E}}^{k} \Phi_{i}^{*} u\right\|_{H^{s-k, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim \rho_{i}^{w+k-n / p}\|u\|_{\mathscr{H}^{s, p ; m}(M)}$. Assuming the claim is true, then
$$\rho_{i}^{-w}\left\|\nabla_{\mathbb{E}}^{m} \Phi_{i}^{*} u\right\|_{H^{s-k, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim r^{m-n / p}\|u\|_{\mathscr{H}^{s, p ; m}(M)} \lesssim r^{\alpha}\|u\|_{\mathscr{H}^{s, p ; m}(M)}$$
since $m-n / p \geq \alpha>0$ (Proposition 4.7) and since $\rho_{i} \lesssim r$, which completes the desired estimate.

The claim is proved inductively with the base case being obvious. Suppose for some $k<m$ that the claim holds for each $0 \leq j \leq k$. Then
$$\nabla_{\mathbb{E}}^{k+1} \Phi_{i}^{*} u=\Phi_{i}^{*} \hat{\nabla}^{k+1} u+A u,$$
where $A u$ is a sum of contractions of tensors of the form $A_{j} \nabla_{\mathbb{E}}^{j} u$ with $j \leq k$, and where each $A_{j}$ is a sum of contractions of tensors of the form $\nabla_{\mathbb{E}}^{a_{1}} D \otimes \cdots \otimes \nabla_{\mathbb{E}}^{a_{\ell}} D$ with $a_{1}+\cdots+$ $a_{\ell}+\ell=k+1-j$ where $D=\Phi_{i}^{*} \hat{\nabla}-\nabla_{\mathbb{E}}$. The claim then follows from the induction hypothesis, the uniform estimates on derivatives of $D$ from Lemma 3.6, and the fact that $\left\|\Phi_{i}^{*} \hat{\nabla}^{k+1} u\right\|_{H^{s-k-1, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim \rho_{i}^{w+k+1-n / p}\|u\|_{\mathscr{H}^{s, p ; m}(M)}$.
The proof in the $\mathscr{X}^{s, p ; m}$ category is similar. With the new hypotheses on the parameters and with the new definition of $\alpha$ it follows that $\mathscr{X}^{s, p ; m}(M)$ embeds in $C^{0, \alpha}(\bar{M})$ and the estimate of the first term on the right-hand side of equation (8.9) proceeds identically. An analogous argument for the second term shows $\left\|\Phi_{i}^{*} \nabla_{\mathbb{E}}^{m} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim \rho_{i}^{w+m}\|u\|_{\mathscr{X}^{s, p, m}(M)}$. But then
$$\rho_{i}^{-w}\left\|\Phi_{i}^{*} \nabla_{\mathbb{E}}^{m} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim r\|u\|_{\mathscr{X}^{s, p ; m}(M)}$$
since $m \geq 1$ and since $\rho_{i} \lesssim r$. \(\square\)
8.4. Localized approximate operators at infinity. Let $g=\rho^{-2} \bar{g}$ be an asymptotically hyperbolic metric of class (1.3) or class (1.4), and let $\mathcal{P}[g]$ satisfy Assumption P acting on sections of geometric tensor bundle $E$. Our goal is to approximate, close to points $\hat{p} \in \partial M$, the operator $\mathcal{P}[g]$ by an operator constructed from $\mathcal{P}[\breve{g}]$.
To accomplish this, we first construct coordinates at $\hat{p} \in \partial M$ adapted to $\bar{g}$, following the construction in Chapter 6 of [Lee06]. Recall from §2 the coordinates near infinity $\Theta_{\hat{p}}: Z_{r_{0}}(\hat{p}) \rightarrow Y_{r_{0}}$ defined where $\rho \leq r_{0}$. Let $K_{\hat{p}} \in T^{1,1} \bar{M}$ be the tensor at $\hat{p}$ obtained by the Gram-Schmidt algorithm such that the forms $\beta^{i}=\left(K_{\hat{p}}\right)_{j}^{i} d \Theta^{j}$ form a $\bar{g}$-orthonormal coframe at $\hat{p}$ and such that $\beta^{n}=|d \rho|_{\bar{g}}^{-1} d \rho$. We define the adapted coordinates near infinity
$\widetilde{\boldsymbol{\Theta}}_{\hat{p}}$ by $\widetilde{\Theta}_{\hat{p}}^{i}=\left(K_{\hat{p}}\right)_{j}^{i} \Theta_{\hat{p}}^{j}$. Observe that $\widetilde{\Theta}_{\hat{p}}^{n}=\Theta_{\hat{p}}^{n}=\rho$, and also that in adapted coordinates we have $\bar{g}(\hat{p})=\delta_{i j} d \widetilde{\Theta}_{\hat{p}}^{i} \widetilde{\Theta}_{\hat{p}}^{j}$. The continuity of $\bar{g}$ on the compact boundary ensures that the values $\left(K_{\hat{p}}\right)_{j}^{i}$ and $\left(K_{\hat{p}}^{-1}\right)_{i}^{j}$ are bounded independent of $\hat{p}$ and these estimates ensure that the Jacobians $D\left(\widetilde{\Theta} \circ \Theta^{-1}\right)$ and their inverses admit uniform $C^{k}$ estimates for any boundary coordinates $\Theta$.
We now show that the metrics $\widetilde{\Theta}_{\hat{p}}^{*} \stackrel{\breve{\sigma}}{g}$ and $g$ are uniformly close in a neighborhood of $\hat{p}$ and, consequently, that geometric differential operators built from each are comparable.

Lemma 8.7. Suppose $g$ is an asymptotically hyperbolic metric of class (1.3) or (1.4), and let $\alpha$ be as in (1.6). Let $\mathcal{P}[g]$ satisfy Assumption $P$. There exists $r_{0}^{\prime} \leq r_{0}$ depending on $g$ and $\mathcal{P}$ such that for all $\hat{p} \in \partial M$, if $\Phi_{i}$ is a Möbius parametrization with $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ intersects $Z_{r}(\hat{p})$ for some $0<r<r_{0}^{\prime}$, then
\begin{itemize}
\item[(a)] $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \subset Z_{r_{0}}(\hat{p})$ and hence $\Phi_{i}^{*} \widetilde{\Theta}_{\hat{p}}^{*} \breve{g}$ is well defined,
\item[(b)] $\left\|\Phi_{i}^{*}\left(\left(\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right)-g\right)\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim r^{\alpha}$,
\item[(c)] if $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $u \in H^{\sigma, q}\left(B_{1}^{\mathbb{H}}\right)$ we have
\end{itemize}
$$\begin{gathered}
\left\|\Phi_{i}^{*}\left(\mathcal{P}\left[\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right)\right] u\right\|_{H^{\sigma-d, q}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\|u\|_{H^{\sigma, q}\left(B_{1}^{\mathbb{H}}\right)}, \\
\left.\| \Phi_{i}^{*}\left(\mathcal{P}\left[\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right]-\mathcal{P}[g]\right) u\right)\left\|_{H^{\sigma-d, q}\left(B_{2}^{\mathbb{H}}\right)} \lesssim r^{\alpha}\right\| u \|_{H^{\sigma, q}\left(B_{1}^{\mathbb{H}}\right)} .
\end{gathered}$$
The implicit constants are independent of $i, \hat{p}, r$ and $u$.
Proof. For part (a), a compactness argument shows that we can take $r_{0}^{\prime}$ sufficiently small independent of $\hat{p}$ so that if $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ intersects $Z_{r_{0}^{\prime}}(\hat{p})$ then $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \subset Z_{r_{0}}(\hat{p})$; see also Lemma 8.11 where a stronger fact is proved.
Let $\widetilde{g}$ be a smooth tensor on $\bar{M}$ that agrees with $\widetilde{\Theta}^{*} g_{\mathbb{E}}$ on $Z_{r_{0}}$ and such that $\widetilde{g}$ is bounded in any $C^{k}(\bar{M})$ independent of $\hat{p}$; uniform bounds for transition Jacobians permit this. Part (b) follows by applying Lemma 8.6 to $\bar{g}-\widetilde{g}$ and noting that since $\widetilde{\Theta}_{\hat{p}}^{n}=\rho$,
$$\Phi_{i}^{*}\left(g-\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right)=\left(\rho_{i} y\right)^{-2} \Phi_{i}^{*}\left(\bar{g}-\widetilde{\Theta}_{\hat{p}}^{*} g_{\mathbb{E}}\right) .$$
Note that the implicit constant of part (b) arises from Lemma 8.6 and is independent of $i$ and $\hat{p}$ in addition to $r$.
In order to obtain estimate (8.11) of part (c), write $\Phi_{i}^{*} \mathcal{P}[g]=\sum_{k} b_{k}\left[\Phi_{i}^{*} g\right] \cdot \nabla_{\mathbb{E}}^{k}$ as in the proof of Lemma 8.5. The Lipschitz estimate (8.8) from that proof implies that if $\Phi_{i}^{*} \widetilde{\Theta}_{\hat{p}}^{*} \breve{g}$ is close enough to $\Phi_{i}^{*} g$ in $H^{s, p}\left(B_{1}^{\mathbb{H}}\right)$, with a closeness bound independent of $i$, then
$$\left\|b_{k}\left[\Phi_{i}^{*} \widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right]-b_{k}\left[\Phi_{i}^{*} g\right]\right\|_{H^{s-d+k, p}\left(B_{1}^{\mathbb{H}}\right)} \lesssim\left\|\Phi_{i}^{*} \widetilde{\Theta}_{\hat{p}}^{*} \breve{g}-\Phi_{i}^{*} g\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)}$$
with an implicit constant that does depend on $g$ but can be arranged as in Lemma 8.5 to be independent of $i$; note that $\hat{p}$ plays no role. The closeness bound can be satisfied part (b) and shrinking $r_{0}^{\prime}$ if needed by a quantity independent of $i$ and $\hat{p}$. Inequality (8.11) then follows
from estimate (8.12), part (b) and the local version of the product estimates in Proposition 3.11, and inequality (8.11) and the uniform estimates (8.7) from Lemma 8.5. \(\square\)

We seek to compare the operator $\mathcal{P}[g]$, which acts on sections of bundle $E$, to the operator $\mathcal{P}[\breve{g}]$. However, the geometric tensor bundle $\breve{E} \rightarrow \mathbb{H}$ on which $\mathcal{P}[\breve{g}]$ acts might not pull back under $\widetilde{\Theta}_{\hat{p}}$ to the bundle $E \rightarrow M$ on which $\mathcal{P}[g]$ acts; this occurs, for example, if the definition of $E$ is contingent upon the metric $g$, in which case $\breve{E}$ would be defined using $\breve{g}$ instead; see §3.7 for a more detailed discussion. For such bundles, the comparison in Lemma 8.7 is not sufficient for the Fredholm theory of §9, where we use the fact that $\mathcal{P}[\breve{g}]$ is invertible on $\breve{E}$.
In order to address this situation, we construct a locally-defined tensor $\left.A[g] \in T^{1,1} \bar{M}\right|_{Z_{r_{0}}(\hat{p})}$, again applying the Gram-Schmidt algorithm but now starting with the $\widetilde{\Theta}^{*} \breve{g}$-orthonormal co-frame $\rho^{-1} d \widetilde{\Theta}^{j}$ and resulting in a $g$-orthonormal co-frame $\omega^{i}=(A[g])_{j}^{i} \rho^{-1} d \widetilde{\Theta}^{j}$. Let $T^{k_{1}, k_{2}} M$ be the ambient tensor bundle of $E$. Then $A_{\hat{p}}[g]$ gives rise to a bundle automorphism tensor $\left.\Pi_{\hat{p}}[g] \in T^{k_{1}+k_{2}, k_{1}+k_{2}} M\right|_{Z_{r_{0}}(\hat{p})}$, formed from tensor products of $A_{\hat{p}}[g]$ and $A_{\hat{p}}^{-1}[g]$, such that contraction $u \mapsto \Pi_{\hat{p}}[g] \cdot u$ takes $g$ orthonormal frames to $\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}$ orthonormal frames. As a consequence, if $u$ is a section of $E$, then the contraction $\Pi_{\hat{p}}[\bar{g}] \cdot u$ is a section of $\widetilde{\Theta}_{\hat{p}}^{*} \breve{E}$, where $\breve{E}$ is the bundle over $\mathbb{H}$ corresponding to $E$. Moreover, from the invertibility of $A_{\hat{p}}[g], \Pi_{\hat{p}}[g]$ admits an inverse $\Pi_{\hat{p}}^{-1}[g]$ that reverses this process. The bundle automorphisms $\Pi_{\hat{p}}[g]$ satisfy estimates analogous to those of Lemma 8.7.

Lemma 8.8. Suppose $g$ is an asymptotically hyperbolic metric of class (1.3) or (1.4), and let $\alpha$ be as in (1.6). Suppose $E$ is a geometric tensor bundle over $M$. For the same constant $r_{0}^{\prime}$ as in Lemma 8.7, for all $\hat{p} \in \partial M$, and for all $0<r \leq r_{0}^{\prime}$, if $\Phi_{i}$ is a Möbius parametrization with $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ intersecting $Z_{r}(\hat{p})$, then the pullbacks $\Phi_{i}^{*} \Pi_{\hat{p}}[g]$ and $\Phi_{i}^{*} \Pi_{\hat{p}}[g]^{-1}$ are uniformly bounded in $H^{s, p}\left(B_{1}^{\mathbb{H}}\right)$ independent of $i$. Furthermore we have
$$\begin{aligned}
\left\|\Phi_{i}^{*} \Pi_{\hat{p}}[g]-\operatorname{id}\right\|_{H^{s, p}\left(B_{2}^{\mathbb{H}}\right)} & \lesssim r^{\alpha}, \\
\left\|\Phi_{i}^{*} \Pi_{\hat{p}}^{-1}[g]-\operatorname{id}\right\|_{H^{s, p}\left(B_{2}^{\mathbb{H}}\right)} & \lesssim r^{\alpha} .
\end{aligned}$$
The implicit constants are independent of $i, \hat{p}$, and $r$.
Proof. From the construction of $\Pi_{\hat{p}}[g]$ it suffices to show that the pullbacks $\Phi_{i}^{*} A_{\hat{p}}[g]$ and $\Phi_{i}^{*} A_{\hat{p}}^{-1}[g]$ are uniformly bounded (independent of $i, \hat{p}$ and $r$ ) in $H^{s, p}\left(B_{2}^{\mathbb{H}}\right)$ and that
$$\begin{aligned}
\left\|\Phi_{i}^{*} A_{\hat{p}}[g]-\operatorname{id}\right\|_{H^{s, p}\left(B_{2}\right)} & \lesssim r^{\alpha} \\
\left\|\Phi_{i}^{*} A_{\hat{p}}^{-1}[g]-\operatorname{id}\right\|_{H^{s, p}\left(B_{2}\right)} & \lesssim r^{\alpha} .
\end{aligned}$$
To obtain the estimates (8.13) let $\Theta$ be the boundary coordinates associated with $\Phi_{i}$ and for $1 \leq k \leq n$ let $\omega^{k}=\omega_{j}^{k} d x^{j}=\Phi_{i}^{*}\left(\rho^{-1} d \widetilde{\Theta}^{k}\right)=y^{-1} d\left(\widetilde{\Theta}^{k} \circ \Theta^{-1}\right)$. Given a metric $h$ on $B_{2}^{\mathbb{H}}$ let $\left\{\left(C_{(i)}[h]\right)_{j}^{k} d x^{j}\right\}$ be the orthonormal coframe obtained from the Gram-Schmidt algorithm applied to $h$ and the coframe $\left\{\omega^{k}\right\}$.

Using uniform $C^{k}$ bounds for the transition Jacobians $D\left(\widetilde{\Theta} \circ \Theta^{-1}\right)$ and and their inverses to control the frame $\left\{\omega^{k}\right\}$ independent of $i$, Lemma A. 13 implies $h \mapsto C_{(i)}[h]$ is Lipshitz $X^{s, p}\left(B_{2}^{\mathbb{H}}\right) \rightarrow X^{s, p}\left(B_{2}^{\mathbb{H}}\right)$ with a Lipschitz constant independent of $i$ so long as $h$ is constrained to lie in a bounded region of $X^{s, p}\left(B_{2}^{\mathbb{H}}\right)$ with determinant uniformly bounded below. Arguing as in Lemma 8.5 we can find such bounds for $\Phi_{i}^{*} g$ and the analogous bounds for $\Phi_{i}^{*} \widetilde{\Theta}^{*} \breve{g}$ follow easily from estimates for transition Jacobians. Inequalities (8.13) now follow from Lemma 8.10(b) and the observation that
$$\begin{gathered}
C_{(k)}\left[\Phi_{i}^{*} g\right]=\Phi_{k}^{*} A[g], \\
C_{(k)}\left[\Phi_{k}^{*} \widetilde{\Theta}^{*} \check{g}\right]=\mathrm{id} .
\end{gathered}$$ \(\square\)
We are now ready to compare operators in a neighborhood of a point along the boundary, and we use cutoff functions from the following lemma to perform the localization.

Lemma 8.9. Let $\hat{p} \in \partial M$, let $0<r \leq r_{0} / 2$. There exists a nonnegative function $\eta_{\hat{p}, r} \in$ $C^{\infty}(\bar{M} ; \mathbb{R})$ that equals 1 on $Z_{r}(\hat{p})$ and has support in $M$ contained in $Z_{2 r}(\hat{p})$. Moreover, $\eta_{\hat{p}, r}$ can be chosen such that for each $\ell \in \mathbb{N}_{\geq 0}$ there is $K>0$ independent of $\hat{p}$ and $r$, but depending on the parameter a, such that $\left\|\eta_{\hat{p}, r}\right\|_{C_{0}^{\ell}(M ; \mathbb{R})} \leq K$.

Proof. Let $\psi: \overline{\mathbb{H}} \rightarrow[0,1]$ be a smooth function that vanishes outside $\overline{Y_{1}}$ and equals 1 on $Y_{1 / 2}$ and define cutoff function $\eta_{\hat{p}, r}$ on $M$, supported in $Z_{r}(\hat{p})$, by $\eta_{\hat{p}, r}(\theta, \rho)=\psi(\theta /(2 r), \rho /(2 r))$. Since the transition functions between background coordinate charts are uniformly bounded, it is straightforward to show that for any Möbius parametrization $\Phi_{i}$ we have $\left\|\Phi_{i}^{*} \eta_{\hat{p}, r}\right\|_{C^{l}\left(B_{2}^{\mathbb{H}}\right)}$ is bounded independent of $r$ and $\hat{p}$, which yields the desired bound. \(\square\)

Suppose $r \leq r_{0}^{\prime}$ from Lemma 8.10 and additionally that $r \leq r_{0} / 2$ so that the cutoff functions $\eta_{\hat{p}, r}$ from Lemma 8.9 are well-defined. We define localized operators $\mathcal{P}_{\hat{p}, r}$ and $\breve{P}_{\hat{p}, r}$ of scale $r$ at the point $\hat{p}$ by
$$\mathcal{P}_{\hat{p}, r} u=\mathcal{P}[g]\left(\eta_{\hat{p}, r} u\right)$$
and
$$\breve{\mathcal{P}}_{\hat{p}, r} u=\Pi_{\hat{p}}^{-1}[g] \cdot \mathcal{P}\left[\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right]\left(\Pi_{\hat{p}}[g] \cdot\left(\eta_{\hat{p}, r} u\right)\right) .$$
The bundle automorphism tensor $\Pi_{\hat{p}}[g]$ gives rise to the map
$$u \mapsto \Xi_{\hat{p}} u:=\left(\widetilde{\Theta}_{\hat{p}}\right)_{*} \Pi_{\hat{p}}[g] u,$$
which is a local bundle isomorphism $\left.\left.E\right|_{Z_{\hat{r}}(\hat{p})} \rightarrow \breve{E}\right|_{Y_{\hat{r}}}$, and we can alternatively write
$$\breve{\mathcal{P}}_{\hat{p}, r} u=\Xi_{\hat{p}}^{-1} \mathcal{P}[\breve{g}] \Xi_{\hat{p}}\left(\eta_{\hat{p}, r} u\right) .$$
The two localized operators are comparable in the following sense.
Lemma 8.10. Suppose $g$ is an asymptotically hyperbolic metric of class (1.3) or (1.4), and let $\alpha$ be as in (1.6). Suppose $\mathcal{P}[g]$ acts on sections of bundle $E$ and satisfies Assumption $P$.

For any $\hat{p} \in \partial M,(\sigma, q) \in \mathcal{S}_{d}^{s, p}$, and $\delta \in \mathbb{R}$ the operator norms of
$$\begin{aligned}
& \breve{\mathcal{P}}_{\hat{p}, r}-\mathcal{P}_{\hat{p}, r}: H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma-d, q}(M ; E), \\
& \breve{\mathcal{P}}_{\hat{p}, r}-\mathcal{P}_{\hat{p}, r}: X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma-d, q}(M ; E)
\end{aligned}$$
satisfy
$$\left\|\breve{\mathcal{P}}_{\hat{p}, r}-\mathcal{P}_{\hat{p}, r}\right\| \lesssim r^{\alpha} .$$
The implicit constants are independent of $\hat{p}$ and $r \leq \min \left(r_{0}^{\prime}, r_{0} / 2\right)$, where $r_{0}^{\prime}$ is the constant from Lemma 8.7.

Proof. Consider the case (8.17) and write
$$\begin{aligned}
\breve{\mathcal{P}}_{\hat{p}, r} u-\mathcal{P}_{\hat{p}, r} u= & \left(\Pi_{\hat{p}}[g]^{-1}-\mathrm{id}\right) \cdot \mathcal{P}\left[\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right]\left(\Pi_{\hat{p}}[g] \cdot\left(\eta_{\hat{p}, r} u\right)\right) \\
& +\mathcal{P}\left[\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right]\left(\left(\Pi_{\hat{p}}[g]-\mathrm{id}\right) \cdot\left(\eta_{\hat{p}, r} u\right)\right)+\left(\mathcal{P}\left[\widetilde{\Theta}_{\hat{p}}^{*} \breve{g}\right]-\mathcal{P}[g]\right)\left(\eta_{\hat{p}, r} u\right),
\end{aligned}$$
for $u \in H_{\delta}^{\sigma, q}(M)$.
Suppose $\Phi_{i}$ is a Möbius parametrization such that $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ intersects the support of $\eta_{\hat{p}, r}$. The estimates of Lemmas 8.7 and 8.8 together with the local versions of the product estimates in Proposition 3.11 then imply
$$\begin{aligned}
\left\|\Phi_{i}^{*}\left(\breve{\mathcal{P}}_{\hat{p}, r} u-\mathcal{P}_{\hat{p}, r} u\right)\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)} & \lesssim r^{\alpha}\left\|\Phi_{i}^{*}\left(\eta_{\hat{p}, r} u\right)\right\|_{H^{\sigma, q}\left(B_{1}^{\mathbb{H}}\right)} \\
& \lesssim r^{\alpha}\left\|\eta_{\hat{p}, r}\right\|_{X^{s, p}(M ; \mathbb{R})}\left\|\Phi_{i}^{*} u\right\|_{H^{\sigma, q}\left(B_{1}^{\mathbb{H}}\right)}
\end{aligned}$$
with implicit constant independent of $i, \hat{p}$, and $r \leq \min \left(r_{0}^{\prime}, r_{0} / 2\right)$. The proof is completed by summing $q^{\text {th }}$ powers, noting that $\left\|\eta_{\hat{p}, r}\right\|_{X^{s, p}(M)}$ is bounded independent of $r$ and $\hat{p}$. The case (8.18) is proved similarly replacing the sum with a supremum. \(\square\)
8.5. Interpolations of $\mathcal{P}$ at infinity. The semi-Fredholm estimates of §8.6 and the parametrix construction of §9 rely on approximating $\mathcal{P}$ on a collar neighborhood $A_{r}$ of $\partial M$ with a collection of 'hyperbolic space' operators $\breve{\mathcal{P}}_{\hat{p}_{j}, r}$ localized at points $\hat{p}_{j} \in \partial M$, which are then stitched together with a suitable partition of unity. We call this approximating collection an interpolation of $\mathcal{P}$ at infinity; see Definition 8.14 below.

As $r \rightarrow 0$, the number of points $p_{j}$ associated with the interpolation increases without bound. For the applications of §9, we need to mitigate against this and ensure that every Möbius parametrization $\Phi_{i}$ has an image that intersects a bounded number of regions on which some $\breve{\mathcal{P}}_{\hat{p}_{j}, r}$ acts non-trivialy, with a fixed bound as $r \rightarrow 0$. The following two technical results are the tools needed to obtain the bound and address a gap in the parametrix construction of [Lee06].

The first step is to show that if the image of a Möbius parametrization intersects some $Z_{r}(\hat{p})$, then it is contained in a larger neighborhood of infinity with a size that scales naturally in $r$.

Lemma 8.11. There exists $\kappa \in(0,1)$ such that for all $r \leq r_{0}$, all $\hat{p} \in \partial M$, and all Möbius parametrizations $\Phi_{i}$, if $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \cap Z_{\kappa r}(\hat{p}) \neq \emptyset$ then $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \subset Z_{r}(\hat{p})$.

Proof. A compactness argument shows that there exists a constant $C \geq 1$ such that if $\theta$ and $\widetilde{\theta}$ two boundary charts with $\hat{a}$ and $\hat{b}$ in the domains of both, then $|\theta(\hat{a})-\theta(\hat{b})|_{\mathbb{R}^{n-1}} \leq$ $C|\widetilde{\theta}(\hat{a})-\widetilde{\theta}(\hat{b})|_{\mathbb{R}^{n-1}}$. Let $\kappa=(1+100 C)^{-1} / 2$.
Suppose for some $r \leq r_{0}$ and Möbius parametrization $\Phi_{i}$ that $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \cap Z_{\kappa r}(\hat{p}) \neq \emptyset$. We will show that $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \cap Z_{r}(\hat{p})$ is both open and closed in $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$, which proves the desired containment. The intersection is clearly open, and to show that it is closed it suffices to show $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \cap Z_{r}(\hat{p}) \subset Z_{r / 2}(\hat{p})$. Let $a \in \Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \cap Z_{\kappa r}(\hat{p})$ and let $b \in \Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \cap Z_{r}(\hat{p})$.
Since $a, b \in \Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ and since $a \in Z_{\kappa r}(\hat{p})$, we conclude $\rho(b)<\exp (2) \rho(a)<9 \kappa r<r / 2$. So to show $b \in Z_{r / 2}(\hat{p})$ we need only demonstrate $\left|\theta(\hat{p})-\theta \circ \Pi_{\partial}(b)\right|_{\mathbb{R}^{n-1}}<r / 2$ where $\theta$ is the boundary chart associated with $\hat{p}$. Let $\widetilde{\theta}$ be the boundary chart associated with $\Phi_{i}$. Then
$$\begin{aligned}
\left|\theta(\hat{p})-\theta \circ \Pi_{\partial}(b)\right|_{\mathbb{R}^{n-1}} & \leq\left|\theta(\hat{p})-\theta \circ \Pi_{\partial}(a)\right|_{\mathbb{R}^{n-1}}+\left|\theta \circ \Pi_{\partial}(a)-\theta \circ \Pi_{\partial}(b)\right|_{\mathbb{R}^{n-1}} \\
& <\kappa r+C\left|\widetilde{\theta} \circ \Pi_{\partial}(a)-\widetilde{\theta} \circ \Pi_{\partial}(b)\right|_{\mathbb{R}^{n-1}} \\
& <\kappa r+2 C \sinh (1) \rho\left(p_{i}\right) \\
& <\kappa r+10 C \kappa r<r / 2 .
\end{aligned}$$
where we have used the fact that $\rho(a)<\kappa r$ implies $\rho\left(p_{i}\right)<3 \kappa r$. \(\square\)

The following variation of Lemma 2.2 of [Lee06] ensures that for any choice of $r \leq r_{0}$ we can find a uniform (in $r$ ) locally finite family of neighborhoods at infinity at scale $r$ that cover a collar neighborhood at the same scale. We will subsequently see that a suitable choice of the parameter $a$ appearing in it will, in combination with Lemma 8.11, ensure that uniform local finiteness for the neighborhoods at infinity extends to the images of Möbius parametrizations that intersect the collar neighborhood.

Lemma 8.12. Suppose $0<a<1$. For any $0<r \leq r_{0}$ there exist finitely many points $\hat{p}_{j} \in \partial M$ such that:
\begin{itemize}
\item[(a)] the sets $\left\{Z_{a r}\left(\hat{p}_{j}\right)\right\}$ cover $A_{a r}$, and
\item[(b)] the neighborhoods $\left\{Z_{r}\left(\hat{p}_{j}\right)\right\}$ are uniformly locally finite independent of $r$.
\end{itemize}

Proof. Recall the smooth reference metric $\hat{g}$ on $\bar{M}$ and let $\gamma=\left.\hat{g}\right|_{\partial M}$. Given $\hat{p} \in \partial M$, let $\theta$ be the boundary coordinates associated with $Z_{r_{0}}(\hat{p})$; see §2. Let $C_{r}(\hat{p})$ be the $\theta$ coordinate ball of radius $r \leq r_{0}$ centered at $\hat{p}$. Similarly, let $B_{r}^{\gamma}(\hat{p})$ be the $\gamma$-geodesic ball in centered at $\hat{p}$ of radius $r$.

Since the geometry of $\gamma$ is uniformly close to Euclidean in any of the finitely many boundary coordinate systems there exist constants $m$ and $M$ such that for any $r \leq r_{0}$ we have
$$B_{m r}^{\gamma}(\hat{p}) \subset C_{r}(\hat{p}) \subset B_{M r}^{\gamma}(\hat{p}) .$$

Since $\partial M$ is compact, standard volume comparison theorems imply there exists constants $C_{1}, C_{2}$, independent of $\hat{p} \in \partial M$ and $r \leq r_{0}$, such that
$$\begin{gathered}
C_{1} r^{n-1} \leq \operatorname{Vol} B_{m r}(\hat{p}), \\
\operatorname{Vol} B_{2 M r} \leq C_{2} r^{n-1} .
\end{gathered}$$
Fixing $r \leq r_{0}$, choose a maximal disjoint collection $\left\{B_{\text {mar } / 2}\left(\hat{p}_{j}\right)\right\}_{j=1}^{J}$; a volume comparison argument shows the collection is finite. The maximality, by means of the triangle inequality, implies that $\left\{B_{\text {mar }}\left(\hat{p}_{j}\right)\right\}_{j=1}^{J}$ covers $\partial M$. The inclusion (8.20), together with the assumed product structure of coordinates near infinity shows that $\left\{Z_{a r}\left(\hat{p}_{j}\right)\right\}_{j=1}^{J}$ covers $A_{a r}$. The uniform (in $r$ ) estimate of the number of sets $Z_{r}\left(\hat{p}_{j}\right)$ that can intersect follows from the relations (8.21), their common scaling in $r$, and the argument of [Lee06] Lemma 2.2. \(\square\)

With the two previous technical results in hand, we can now construct the requisite partitions of unity used to stitch together localized operators at infinity. The key point is item (f).

Lemma 8.13. There exists $r_{0}^{\prime \prime} \leq r_{0}$ such that for each $r \leq r_{0}^{\prime \prime}$ there exist boundary points $\left\{\hat{p}_{j}\right\}_{j=1}^{J}$ and smooth functions $\varphi_{0}, \varphi_{1}, \ldots, \varphi_{J}$ on $\bar{M}$ such that:
\begin{itemize}
\item[(a)] The support of $\varphi_{0}$ in $M$ is contained in $M \backslash A_{r / 4}$.
\item[(b)] For $1 \leq j \leq J$, the support in $M$ of $\varphi_{j}$ is contained in $Z_{r}\left(\hat{p}_{j}\right)$.
\item[(c)] The functions $\psi_{j}=\varphi_{j}^{2}$ form a partition of unity on $\bar{M}$.
\item[(d)] For any choice of $\ell \in \mathbb{N}_{\geq 0}$, the functions $\varphi_{j}$ are uniformly bounded in $C_{0}^{\ell, 0}(M ; \mathbb{R})$ independent of $r$.
\item[(e)] There is a bound $K$, independent of $r$, such that for each $j \geq 1$ there are at most $K$ indices $k \geq 1$ such that the support of $\varphi_{k}$ overlaps that of $\varphi_{j}$.
\item[(f)] Given a Möbius parametrization $\Phi_{i}$, there are at most $K$ indices $j \geq 1$ such that $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right)$ intersects $Z_{r}\left(\hat{p}_{j}\right)$. Consequently, there are at most $K+1$ functions $\varphi_{j}, j \geq 0$, with support intersecting the image of $\Phi_{i}$.
\end{itemize}

Proof. Let $r_{0}^{\prime \prime}=\kappa r_{0}$ where $\kappa$ is the parameter from Lemma 8.11 and suppose $r \leq r_{0}^{\prime \prime}$. Applying Lemma 8.12 with its parameter $a=\kappa / 2$ implies we can find boundary points $\hat{p}_{j}$ such that the sets $Z_{r / 2}\left(\hat{p}_{j}\right)$ cover $A_{r / 2}$ and such that the sets $Z_{K^{-1} r}\left(\hat{p}_{j}\right)$ are uniformly locally finite: there exists $K>0$ such that each of these sets intersects no more than $K$ sets in the collection, with $K$ independent of $r$.
From Lemma 8.9, for each $j$ we can choose a smooth cutoff function $\chi_{j}$ on $\bar{M}$ that equals 1 on $Z_{r / 2}\left(\hat{p}_{j}\right)$ and which has a restriction to $M$ with support contained in $Z_{r}\left(\hat{p}_{j}\right)$. Moreover, we can ensure that for any choice of $\ell$ the $C_{0}^{\ell}$ norms of the functions $\chi_{j}$ are bounded independent of $r$ and the choice of points $\hat{p}_{j}$. Choose a smooth function $\chi:[0, \infty) \rightarrow$ $[0, \infty)$ such that $\chi=0$ on $[0,1 / 4]$ and $\chi=1$ on $[1 / 2, \infty)$ and define $\chi_{0}=\chi \circ(\rho / r)$, which is smooth on $\bar{M}$. A scaling argument shows that $\chi_{0}$ is uniformly bounded in $C_{0}^{\ell}(M)$ for each $\ell \in \mathbb{N}_{\geq 0}$ independent of $r \leq r_{0}$.

By construction, for $j \geq 1$ the function $\chi_{j}$ is supported in $M$ on $Z_{r}\left(\hat{p}_{j}\right) \subset Z_{\kappa^{-1} r}\left(\hat{p}_{j}\right)$ and hence its support can overlap with that of at most $K$ functions $\chi_{k}$ with $k \geq 1$. Taking $\chi_{0}$ into account, its support can therefore overlap at most $K+1$ functions $\chi_{k}$. Moreover, if $\Phi_{i}$ is a Möbius parametrization, and if for some $j \geq 1$ the function $\chi_{j}$ has support intersecting $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$, Lemma 8.11 implies $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right) \subset Z_{K^{-1} r}\left(\hat{p}_{j}\right)$ and it follows from the uniform local finiteness of the sets $Z_{K^{-1} r}\left(\hat{p}_{i}\right)$ that $\Phi_{i}\left(B_{1}^{\mathbb{H}}\right)$ can intersect at most $K$ total of these.
The function $\sum_{j=0}^{J} \chi_{j}^{2} \geq 1$ and uniform local finiteness implies it is bounded in $C_{0}^{\ell}(M)$ for each $\ell \in \mathbb{N}_{\geq 0}$ independent of $r$ and the choice of points $\hat{p}_{j}$. Hence, defining
$$\varphi_{i}=\frac{\chi_{i}}{\sqrt{\sum_{j=0}^{J} \chi_{j}^{2}}},$$
the functions $\psi_{i}=\varphi_{i}^{2}$ form a partition of unity of $\bar{M}$ that satisfy the desired $C_{0}^{\ell}$ bounds. \(\square\)

Definition 8.14. Let $g$ be an asymptotically hyperbolic metric of class (1.3) or (1.4) and let $\mathcal{P}[g]$ be an operator satisfying Assumption $P$. Recall the constants $r_{0}^{\prime}$ and $r_{0}^{\prime \prime}$ from Lemmas (8.7) and 8.13, respectively. For positive $r \leq \min \left(r_{0} / 2, r_{0}^{\prime}, r_{0}^{\prime \prime}\right)$ apply Lemma 8.13 to construct a partition of unity $\psi_{j}=\varphi_{j}^{2}$, with $0 \leq j \leq J$, for this choice of $r$ and associated boundary points $\hat{p}_{j}$.
An interpolation of $\mathcal{P}[\boldsymbol{g}]$ at infinity with scale $\boldsymbol{r}$ is comprised of the corresponding collection of bundle automorphism tensors $\Xi_{j}=\Xi_{\hat{p}_{j}}$, defined for $1 \leq j \leq J$ by (8.15); localized approximation operators $\breve{\mathcal{P}}_{j}:=\breve{\mathcal{P}}_{\hat{p}_{j}, r}$, defined for $1 \leq j \leq J$ by (8.16); and the partition of unity $\left\{\varphi_{j}\right\}_{j=0}^{J}$.
8.6. A priori estimates. We are now able to prove a-priori estimates for elliptic geometric operators arising from asymptotically hyperbolic metrics of class (1.3) and (1.4). Our estimates rely on the isomorphism property of $\mathcal{P}[g]$, recorded in Assumption I of the introduction. This assumption allows us to invoke Theorems B. 3 and B.6, which establish isomorphism properties of $\mathcal{P}\left[g_{\mathbb{B}}\right]$ on the ball model ( $\mathbb{B}, g_{\mathbb{B}}$ ) of hyperbolic space. In our application here, and subsequently in §9, we use the fact that the isomorphism results on the ball model give rise to corresponding isomorphism theorems for $\mathcal{P}[\breve{g}]$ on the half space model ( $\mathbb{H}, \breve{g}$ ). To do so, we choose an isometry $\mathcal{I}: \mathbb{H} \rightarrow \mathbb{B}$ and simply define norms on $\mathbb{H}$ in terms of the norms on $\mathbb{B}$ defined in Appendix B:
$$\|u\|_{H_{\delta}^{\sigma, q}(\mathbb{H} ; \breve{E})}:=\left\|\mathcal{I}_{*} u\right\|_{H_{\delta}^{\sigma, q}\left(\mathbb{B} ; \mathcal{I}_{*} \breve{E}\right)}$$
for any $1<q<\infty$ and $s, \delta \in \mathbb{R}$. It is easy to see that the norms defined this way are equivalent for any choice of $I$. The following lemma allows us to transfer between sections of geometric bundles on $M$ and bundles on $\mathbb{H}$.
Lemma 8.15. Suppose $g$ is an asymptotically hyperbolic metric of class (1.3) or (1.4), and suppose $\hat{p} \in \partial M$. Let $E$ is a geometric tensor bundle over $M$ and let $\breve{E}$ be the corresponding bundle over $\mathbb{H}$. Let $(\sigma, q) \in \mathcal{S}_{0}^{s, p}$ and $\delta \in \mathbb{R}$. Recalling the cutoff functions $\eta_{\hat{p}, r}$ from Lemma 8.9, for each $0<r \leq \bar{r}$ from Lemma 8.10 we have the norm equivalence
$$\left\|\Xi_{\hat{p}}\left(\eta_{\hat{p}, r} u\right)\right\|_{H_{\delta}^{\sigma, q}(\mathbb{H} ; \check{E})} \sim\left\|\eta_{\hat{p}, r} u\right\|_{H_{\delta}^{\sigma, q}(M ; E)}$$
for all $u \in H_{\delta}^{\sigma, q}(M ; E)$, with the implicit constants independent of $\hat{p}$ and $r$.
Proof. In view of the estimates of Lemma 8.8, it suffices to show that
$$\left\|\widetilde{\Theta}_{\hat{p}}^{*}\left(\eta_{\hat{p}, r} u\right)\right\|_{H_{\delta}^{\sigma, q}(\mathbb{H} ; \breve{F})} \sim\left\|\eta_{\hat{p}, r} u\right\|_{H_{\delta}^{\sigma, q}(M ; F)}$$
for any tensor bundle $F$. The proof of this is a straightforward variation of the proof of Lemma A.21, using the following facts:
\begin{itemize}
\item[-] We can pick $\bar{r}$ sufficiently large so that $\widetilde{\Theta}_{\hat{p}}\left(Z_{\hat{p}}\left(r_{0}\right) \subset Y_{\bar{r}}\right.$ for any $\hat{p} \in \partial M$.
\item[-] Writing $\rho_{\mathbb{B}}$ for the defining function on $\mathbb{B},\left(\mathcal{I}^{*} \rho_{\mathbb{B}}\right) / y$ is bounded above and below on $Y_{\bar{r}}$
\item[-] On $Y_{\bar{r}}$, the Jacobians of $\Theta^{\mathbb{B}} \circ \mathcal{I}$ and its inverse admit uniform $C^{k}$ bounds for any boundary chart $\Theta^{\mathbb{B}}$ on $\mathbb{B}$.
\item[-] For any boundary chart $\Theta$ on $M$, the Jacobians of $\widetilde{\Theta}_{\hat{p}} \circ \Theta^{-1}$ and its inverse admit uniform $C^{k}$ bounds independent of $\hat{p}$.
\end{itemize}
See also the proof of Lemma B.1. \(\square\)

We now establish the a priori estimates that imply $\mathcal{P}[g]$ is semi-Fredholm. Recall that Assumption I implies the positive of the indicial radius $R$ of $\mathcal{P}[\breve{g}]$; see [Lee06]. Recall also, from (1.9), the notation
$$D_{q}(R)=\left\{\delta \in \mathbb{R}:\left|\delta-\frac{n-1}{q}+\frac{n-1}{2}\right|<R\right\} .$$

Proposition 8.16. Suppose $g$ be an asymptotically hyperbolic metric of class (1.3) or (1.4). Let $\mathcal{P}[g]$ be an operator on sections of geometric tensor bundle $E$ that satisfies Assumptions $P$ and $I$. Let $R>0$ be the indicial radius of the corresponding operator $\breve{\mathcal{P}}$ on hyperbolic space.
\begin{itemize}
\item[(a)] If $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and if $\delta \in D_{q}(R)$ then for all $u \in H_{\delta}^{\sigma, q}(M ; E)$
$$\|u\|_{H_{\delta}^{\sigma, q}(M ; E)} \lesssim\|\mathcal{P} u\|_{H_{\delta}^{\sigma-d, q}(M ; E)}+\|u\|_{H_{\delta-1}^{\sigma-1, q}(M ; E)} .$$
\item[(b)] If $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and if $\delta \in D_{\infty}(R)$ then for all $u \in X_{\delta}^{\sigma, q}(M ; E)$
$$\|u\|_{X_{\delta}^{\sigma, q}(M ; E)} \lesssim\|\mathcal{P} u\|_{X_{\delta}^{\sigma-d, q}(M ; E)}+\|u\|_{X_{\delta-1}^{\sigma-1, q}(M ; E)} .$$
\end{itemize}
Consequently, $\mathcal{P}$ thus has finite-dimensional kernel and closed range (i.e. is semi-Fredholm) as a map $H_{\delta}^{\sigma, p}(M ; E) \rightarrow H_{\delta}^{\sigma-d, p}(M ; E)$ or $X_{\delta}^{\sigma, p}(M ; E) \rightarrow X_{\delta}^{\sigma-d, p}(M ; E)$ under the stated restrictions on the parameters $\sigma, p$ and $\delta$.

Proof. We first address the Sobolev case. Let $\left\{\breve{\mathcal{P}}_{j}\right\}$ be an interpolation of $\mathcal{P}$ at infinity with scale $r$ to be chosen sufficiently small below and let $\left\{\psi_{j}\right\}$ be the associated partition of unity.
Consider some $j \geq 1$; let $\widetilde{\Theta}_{j}=\widetilde{\Theta}_{\hat{p}_{j}}$ and $\Xi_{j}=\Xi_{\hat{p}_{j}}$ be the corresponding adapted coordinates and local bundle isomorphism. Since $\delta \in \mathcal{D}_{q}(R)$ and since the cutoff function $\eta_{\hat{p}_{j}, r}$
appearing in equation (8.14) satisfies $\eta_{\hat{p}, j} \psi_{j}=\psi_{j}$ we can apply Lemma 8.15 and Theorem B. 3 to obtain
$$\begin{aligned}
\left\|\psi_{j} u\right\|_{H_{\delta}^{\sigma, q}(M)} & \lesssim\left\|\Xi_{j}\left(\psi_{j} u\right)\right\|_{H_{\delta}^{\sigma, q}(\mathbb{H})} \\
& \lesssim\left\|\mathcal{P}[\breve{g}] \Xi_{j}\left(\psi_{j} u\right)\right\|_{H_{\delta}^{\sigma-d, q}(\mathbb{H})} \\
& \lesssim\left\|\Xi_{j}^{-1} \mathcal{P}[\breve{g}] \Xi_{j}\left(\psi_{j} u\right)\right\|_{H_{\delta}^{\sigma-d, q}(M)} \\
& =\left\|\breve{\mathcal{P}}_{j}\left(\psi_{j} u\right)\right\|_{H_{\delta}^{\sigma-d, q}(M)} .
\end{aligned}$$
Again using the identity $\eta_{\hat{p}_{j}, r} \psi_{j}=\psi_{j}$, we have $\mathcal{P}_{j} u=\mathcal{P}[g]\left(\psi_{j} u\right)$ and hence the triangle inequality implies that the right side of (8.24) is bounded by
$$\left\|\psi_{j} \mathcal{P}[g] u\right\|_{H_{\delta}^{\sigma-d, q}(M)}+\left\|\left[\mathcal{P}[g], \psi_{j}\right] u\right\|_{H_{\delta}^{\sigma-d, q}(M)}+\left\|\left(\breve{\mathcal{P}}_{j}-\mathcal{P}_{j}\right)\left(\psi_{j} u\right)\right\|_{H_{\delta}^{\sigma-d, q}(M)} .$$
Moreover, Lemma 8.10 implies
$$\left\|\left(\breve{\mathcal{P}}_{j}-\mathcal{P}_{j}\right)\left(\psi_{j} u\right)\right\|_{H_{\delta}^{\sigma-d, q}(M)} \lesssim r^{\alpha}\left\|\psi_{j} u\right\|_{H_{\delta}^{\sigma, q}(M)} .$$
All of the implicit constants thus far are independent of $\hat{p}_{j}$ and $r$, so at this point we can select $r$ sufficiently small so that for all $j$ this term can be absorbed into the left side of (8.24). Lemma 8.4 implies that
$$\begin{aligned}
\left\|\left[\mathcal{P}[g], \psi_{j}\right] u\right\|_{H_{\delta}^{\sigma-d, q}(M)} & \lesssim\left\|\rho^{-1}\left[\mathcal{P}[g], \psi_{j}\right] u\right\|_{H_{\delta-1}^{\sigma-d, q}(M)} \\
& \lesssim\left\|\rho^{-1}\left[\mathcal{P}[g], \psi_{j}\right] u\right\|_{H_{\delta-1}^{\sigma-d, q}(M)} \\
& \lesssim\|u\|_{H_{\delta-1}^{\sigma-1, q}(M)}
\end{aligned}$$
and combining the inequalities thus far we find that for each $j \geq 1$ that
$$\left\|\psi_{j} u\right\|_{H_{\delta}^{\sigma, q}(M)} \lesssim\|\mathcal{P}[g] u\|_{H_{\delta}^{\sigma-d, q}(M)}+\|u\|_{H_{\delta-1}^{\sigma-1, q}(M)} .$$
In order to estimate $\psi_{0} u$ we pick precompact open sets $V$ and $U$ with smooth boundaries such that $\operatorname{supp} \psi_{0} \subset V \subset \bar{V} \subset U$. Since $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$, Sobolev embedding on $U$ implies $H^{\sigma-1-d, q}(U ; E) \hookrightarrow H^{d-s-1, p^{*}}(U ; E)$. Hence Proposition 8.3 and straightforward arguments relating weighted spaces on $M$ and their restrictions to domains imply
$$\begin{aligned}
\left\|\psi_{0} u\right\|_{H_{\delta}^{\sigma, q}(M)} \lesssim\|u\|_{H^{\sigma, q}(V)} & \lesssim\|\mathcal{P}[g] u\|_{H^{\sigma-d, q}(U)}+\|u\|_{H^{d-s-1, p^{*}}(U)} \\
& \lesssim\|\mathcal{P}[g] u\|_{H_{\delta}^{\sigma-d, q}(M)}+\|u\|_{H_{\delta-1}^{\sigma-1, q}(M)} .
\end{aligned}$$
Estimate (8.22) now follows by summing over the partition of unity. The proof of (8.23) follows from analogous logic, using Theorem B. 6 in place of Theorem B.3.

The fact that $\mathcal{P}$ has finite dimensional kernel follows from inequalities (8.22) and (8.23) and the fact that the maps $H_{\delta}^{\sigma, q}(M) \hookrightarrow H_{\delta-1}^{\sigma-1, q}(M)$ and $X_{\delta}^{\sigma, q}(M) \hookrightarrow X_{\delta-1}^{\sigma-1, q}(M)$ are compact by Proposition 3.4. The closedness of the image follows from this; see, for example, [Lee06, Lemma 4.10]. \(\square\)

\section*{9. Fredholm theory}

In this section we establish the Fredholm results of Theorem 1.2 for elliptic operators associated to asymptotically hyperbolic metrics. To this end, let $g$ be a asymptotically hyperbolic metric of class (1.3) or (1.4) Let $\mathcal{P}=\mathcal{P}[g]$ be a differential operator on sections of geometric tensor bundle $E$ that satisfies Assumption P. Recall that Lemma 8.2, together with the assumptions on $g$, imply that the set of compatible Sobolev indices $\mathcal{S}_{d}^{s, p}$ is nonempty.
Let $R$ be the indicial radius of $\breve{\mathcal{P}}=\mathcal{P}[\breve{g}]$, the associated operator on hyperbolic space, which acts on sections of corresponding bundle $\breve{E}$. Theorem B. 3 implies that $\breve{\mathcal{P}}: H_{\delta}^{\sigma, q}(\mathbb{H} ; \breve{E}) \rightarrow$ $H_{\delta}^{\sigma-d, q}(\mathbb{H} ; \breve{E})$ is an isomorphism for $\delta \in \mathcal{D}_{q}(R)$, while Theorem B. 6 indicates that $\breve{\mathcal{P}}: X_{\delta}^{\sigma, q}(\mathbb{H} ; \breve{E}) \rightarrow$ $X_{\delta}^{\sigma-d, q}(\mathbb{H} ; \breve{E})$ is an isomorphism if $\delta \in \mathcal{D}_{\infty}(R)$. Thus our primary goal is to show that $\mathcal{P}$ is Fredholm of index zero for those exact weight parameters $\delta$ for which $\breve{\mathcal{P}}$ is an isomorphism.
9.1. Parametrix construction. Adapting the strategy of [Lee06], we establish the Fredholm properties of $\mathcal{P}$ using a parametrix, the operator $\widetilde{Q}_{r}$ defined below, based on the inverse $\breve{\mathcal{P}}^{-1}$ applied to sections supported near $\partial M$. To that end, let $\left\{\breve{\mathcal{P}}_{j}\right\}_{j=1}^{J}$ be an interpolation of $\mathcal{P}$ satisfying Definition 8.14 with associated bundle automorphism tensors $\left\{\Xi_{j}\right\}_{j=1}^{J}$ and cutoff function $\left\{\varphi_{j}\right\}_{j=1}^{J}$. For $1 \leq j \leq J$, define operators $\mathcal{P}_{j}$ by $\mathcal{P}_{j} u=\mathcal{P}\left(\varphi_{j} u\right)$. Finally, define the maps
$$\begin{aligned}
Q_{r} u & =\sum_{j \geq 1} \varphi_{j} \Xi_{j}^{-1} \breve{\mathcal{P}}^{-1} \Xi_{j}\left(\varphi_{j} u\right), \\
S_{r} u & =\sum_{j \geq 1} \varphi_{j} \Xi_{j}^{-1} \breve{\mathcal{P}}^{-1} \Xi_{j}\left(\left(\mathcal{P}_{j}-\breve{\mathcal{P}}_{j}\right) \varphi_{j} u\right), \\
T_{r} u & =\sum_{j \geq 1} \varphi_{j} \Xi_{j}^{-1} \breve{\mathcal{P}}^{-1} \Xi_{j}\left(\left[\varphi_{j}, \mathcal{P}\right] u\right)
\end{aligned}$$
for sufficiently regular, compactly supported sections $u$ of $E$.
Proposition 9.1.
\begin{itemize}
\item[(a)] If $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$ then $Q_{r}, S_{r}, T_{r}$ extend to bounded maps as follows:
$$\begin{aligned}
& Q_{r}: H_{\delta}^{\sigma-d, q}(M ; E) \rightarrow H_{\delta}^{\sigma, q}(M ; E), \\
& S_{r}: H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma, q}(M ; E), \\
& T_{r}: H_{\delta-1}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma+1, q}(M ; E) .
\end{aligned}$$
If $u$ is supported in $A_{r / 4}$ then
$$Q_{r} \mathcal{P} u=u+S_{r} u+T_{r} u .$$
Moreover
$$\left\|S_{r} u\right\|_{H_{\delta}^{\sigma, q}(M)} \lesssim r^{\alpha}\|u\|_{H_{\delta}^{\sigma, q}(M)},$$
\end{itemize}
\begin{itemize}
\item[] where $\alpha \in(0,1]$ is the constant from (1.6).
\item[(b)] The same statement is true replacing weighted Sobolev spaces $H$ with Gicquaud-Sakovich spaces $X$ having the same parameters, and replacing the weight range $\mathcal{D}_{q}(R)$ with $\mathcal{D}_{\infty}(R)$.
\end{itemize}

Proof. We demonstrate the proof for weighted Sobolev spaces; the proof for Gicquad-Sakovich spaces is similar but easier.