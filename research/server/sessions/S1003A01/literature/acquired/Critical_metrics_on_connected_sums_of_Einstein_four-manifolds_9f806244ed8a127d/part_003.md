---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: Critical metrics on connected sums of Einstein four-manifolds]

For $b>0$ denote the annulus $A_{Z}(b, 2 b)=\{b \leq|z| \leq 2 b\} \subset Z$, and for $a>0$ denote the annulus $A_{N}\left(a^{-1}, 2 a^{-1}\right) \equiv\left\{a^{-1} \leq|x| \leq 2 a^{-1}\right\} \subset N$. Let $\iota: A_{N}\left(a^{-1}, 2 a^{-1}\right) \rightarrow$ $A_{Z}(b, 2 b)$ denote the map $\iota(x)=a b x=z$. Identify the annular region $A_{Z}(b, 2 b) \subset X$ with $A_{N}\left(a^{-1}, 2 a^{-1}\right) \subset N$ using the map $\iota$ to define a new manifold $X_{a, b}$.

Remark 9.1. With this choice of $\iota$, the manifold $X_{a, b}$ is diffeomorphic to $X \nexists \overline{N_{c}}$, where $N_{c}$ is the one-point compactification of $N$. If we instead choose $\iota$ to be defined by, for example, $\iota\left(x_{1}, x_{2}, x_{3}, x_{4}\right)=a b\left(-x_{1}, x_{2}, x_{3}, x_{4}\right), X_{a, b}$ will be diffeomorphic to $X \# N_{c}$, which can be different topologically.

In the case where $\left(Z, g_{Z}\right)$ is the Fubini-Study metric and $\left(N, g_{N}\right)$ is the Burns metric, the $U(2)$ action extends to $X_{a, b}$, since the actions agree in the coordinate systems. In all other cases, the torus action as well as the diagonal symmetry extend to actions on $X_{a, b}$. For convenience, we will now refer to this action as "the group action", keeping in mind that the group depends on the example.

We compute that
$$\begin{aligned}
\iota^{*}\left(a^{-2} b^{-2} g_{Z}\right) & =a^{-2} b^{-2}\left\{a^{2} b^{2} d x^{2}+\left(\iota^{*} \eta_{Z}\right)(x)\right\} \\
& =d x^{2}+\tilde{\eta}_{Z}(x),
\end{aligned}$$
where
$$\tilde{\eta}_{Z}(x)=a^{-2} b^{-2}\left(\iota^{*} \eta_{Z}\right)(x) .$$

Note that $\tilde{\eta}_{Z}$ admits the expansion $\tilde{\eta}_{Z}=\left(\tilde{\eta}_{Z}(x)\right)_{i j} d x^{i} d x^{j}$ with
$$\left(\tilde{\eta}_{Z}(x)\right)_{i j}=-\frac{1}{3} a^{2} b^{2} R_{i k j l}\left(z_{0}\right) x^{k} x^{l}+\text { (higher) }$$
as $b \rightarrow 0$ and for $x \in A_{N}\left(a^{-1}, 2 a^{-1}\right)$.
Define a metric $g_{a, b}^{(0)}$ on $X_{a, b}$ by
$$g_{a, b}^{(0)}= \begin{cases}a^{-2} b^{-2} g_{Z} & |z| \geq 2 b \\ d x^{2}+\phi(a|x|) \eta_{N}(x)+[1-\phi(a|x|)] \tilde{\eta}_{Z}(x) & a^{-1} \leq|x| \leq 2 a^{-1} \\ g_{N} & |x| \leq a^{-1} .\end{cases}$$
The group action is linear in the $\{x\}$-coordinates, and is contained in $S O(4)$. Since the cutoff function is radial, it is clear that $g_{a . b}^{(0)}$ is invariant under the group action.

On the damage zone $A_{N}\left(a^{-1}, 2 a^{-1}\right)$, we will also write the metric as
$$g_{a, b}^{(0)}=d x^{2}+\eta_{1}+\eta_{2},$$
where
$$\begin{aligned}
& \eta_{1}(x)=\phi(a|x|) \eta_{N}(x) \\
& \eta_{2}(x)=[1-\phi(a|x|)] \tilde{\eta}_{Z}(x) .
\end{aligned}$$
Notice that after scaling and identifying, we have
$$\left|\operatorname{Rm}\left(\iota^{*}\left(a^{-2} b^{-2} g_{Z}^{b}\right)\right)\right|= \begin{cases}a^{2} b^{2}\left(\left|R\left(g_{Z}\right)\right| \circ \iota\right) & |x| \geq 2 a^{-1} \\ O\left(a^{2} b^{2}\right) & a^{-1} \leq|x| \leq 2 a^{-1} \\ 0 & |x| \leq 2 a^{-1} .\end{cases}$$
This implies that
$$\left|B^{t}\left(\iota^{*}\left(a^{-2} b^{-2} g_{Z}^{b}\right)\right)\right|= \begin{cases}0 & |x| \geq 2 a^{-1} \\ O\left(a^{4} b^{2}\right) & a^{-1} \leq|x| \leq 2 a^{-1} \\ 0 & |x| \leq 2 a^{-1} .\end{cases}$$

Consequently,
$$\left|B^{t}\left(g_{a, b}^{(0)}\right)\right|= \begin{cases}0 & |x| \geq 2 a^{-1} \\ O\left(a^{4} b^{2}\right)+O\left(a^{6}\right) & a^{-1} \leq|x| \leq 2 a^{-1} \\ 0 & |x| \leq 2 a^{-1},\end{cases}$$
which is proved by using the expansion
$$B^{t}\left(g_{a, b}^{(0)}\right)=B^{t}\left(g_{0}\right)+\left(B^{t}\right)_{g_{0}}^{\prime}\left(\eta_{1}+\eta_{2}\right)+\mathcal{Q}\left(\eta_{1}+\eta_{2}\right),$$
where $g_{0}=d x^{2}$ in the damage zone; see Remark 3.8.
This estimate will not suffice for our purposes, and in Section 10 we will construct a "better" approximate metric.
9.1. Gluing with one basepoint. To summarize, ( $X_{a, b}, g_{a, b}^{(0)}$ ) is defined in the following cases:
\begin{itemize}
\item[-] (i) $\mathbb{C P}^{2} \# \overline{\mathbb{C P}}^{2}$; the Fubini-Study metric with a Burns metric attached at one fixed point. This case admits a $U(2)$-action.
\item[-] (ii) $S^{2} \times S^{2} \# \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 2 \overline{\mathbb{C P}}^{2}$; the product metric on $S^{2} \times S^{2}$ with a Burns metric attached at one fixed point. Alternatively, we can view this as the Fubini-Study metric on $\mathbb{C P}^{2}$, with a Green's function $S^{2} \times S^{2}$ metric attached at one fixed point. For this topology, we will therefore construct two different critical metrics.
\item[-] (iii) $2 \# S^{2} \times S^{2}$; the product metric on $S^{2} \times S^{2}$ with a Green's function $S^{2} \times S^{2}$ metric attached at one fixed point.
\end{itemize}

All of these cases are invariant under the torus action, and invariant under the diagonal symmetry.

As mentioned in the introduction, the product metric on $S^{2} \times S^{2}$ admits the Einstein quotient $S^{2} \times S^{2} / \mathbb{Z}_{2}$, where $\mathbb{Z}_{2}$ acts by the antipodal map on both factors, and the quotient $\mathbb{R P}^{2} \times \mathbb{R P}^{2}$. The diagonal symmetry clearly extends to these metrics. Using one of these metrics as the compact factor or the Green's function metric of one of these as the AF space, we obtain approximate metrics on the non-simply-connected topologies listed in Table 1.3. Note that in this table, the first special value of $t_{0}$ corresponds to the the first factor being the compact factor, and the second factor being the AF space, while the second value of $t_{0}$ corresponds to the reverse. From this, the approximate metric is clear and we need not detail every case here.
9.2. Gluing with multiple bubbles. We first consider the case when $\left(Z, g_{Z}\right)$ is $\left(S^{2} \times S^{2}, g_{S^{2} \times S^{2}}\right)$. We can glue on an AF space at both points $(n, n)$ and $(s, s)$, but we must take the same AF space for both points. In this case, we impose an additional symmetry. There is an orientation-preserving involution of $S^{2} \times S^{2}$ consisting of the product of antipodal maps. Since both AF spaces are the same, this involution obviously extends to an involution of $X_{a, b}$ which is an isometry of $g_{a, b}^{(0)}$, and which we will refer to as bilateral symmetry. As in the single bubble case, the toric action extends to an isometry of the approximate metric on the connect sum. We then have the following cases with toric invariance, diagonal symmetry, and bilateral symmetry:
\begin{itemize}
\item[-] (iv) $3 \# S^{2} \times S^{2}$; the product metric on $S^{2} \times S^{2}$ with Green's function $S^{2} \times S^{2}$ metrics attached at two fixed points.
\item[-] (v) $S^{2} \times S^{2} \# 2 \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$; the product metric on $S^{2} \times S^{2}$ with Burns metrics attached at two fixed points.
\end{itemize}

Next, we consider the case when $\left(Z, g_{Z}\right)$ is $\left(\mathbb{C P}^{2}, g_{F S}\right)$. Imposing trilateral symmetry (see Figure 2.1), allows us to attach the same AF space at all 3 fixed points. We then have the following cases with toric invariance, diagonal symmetry at each fixed point, and trilateral symmetry:
\begin{itemize}
\item[-] (vi) $\mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$; the Fubini-Study metric with Burns metrics attached at all fixed points.
\end{itemize}
\begin{itemize}
\item[-] (vii) $\mathbb{C P}^{2} \# 3\left(S^{2} \times S^{2}\right)=4 \mathbb{C P}^{2} \# 3 \overline{\mathbb{C P}}^{2}$; the Fubini-Study metric with Green's function $S^{2} \times S^{2}$ metrics attached at all fixed points.
\end{itemize}

Next, we return to the case that $\left(Z, g_{Z}\right)$ is $\left(S^{2} \times S^{2}, g_{S^{2} \times S^{2}}\right)$. Imposing quadrilateral symmetry (see Figure 2.2), allows us to attach the same AF space at all 4 fixed points. We then have the following cases with toric invariance, diagonal symmetry at each fixed point, and quadrilateral symmetry:
\begin{itemize}
\item[-] (viii) $S^{2} \times S^{2} \# 4 \overline{\mathbb{C P}}^{2}=\mathbb{C P}^{2} \# 5 \overline{\mathbb{C P}}^{2}$; the product metric on $S^{2} \times S^{2}$ with Burns metrics attached at all fixed points.
\item[-] (ix) $5 \# S^{2} \times S^{2}$ viewed as the product metric on $S^{2} \times S^{2}$ with Greens function $S^{2} \times S^{2}$ metrics attached at all fixed points.
\end{itemize}

For multiple bubbles in the non-orientable case, see Appendix B.
9.3. Weight function. For the weighted norms, we define the weight function on $X_{a, b}$ by
$$w=\left\{\begin{array}{ll}
a^{-1} b^{-1} & |z| \geq 1 \\
a^{-1} b^{-1}|z| & 1 \geq|z| \geq 2 b \\
|x| & 2 a^{-1} \geq|x| \geq 1 \\
1 & 1 \geq|x|
\end{array},\right.$$
where for simplicity we have assumed that the $x$ and $z$ coordinates contain the unit spheres. We record the inequalities
$$1 \leq w \leq a^{-1} b^{-1} .$$

\section*{10. Refined approximate metric}

Remark 10.1. We will now choose $\delta<0$ satisyfing $-\epsilon<\delta<0$, where $\epsilon$ was previously chosen (see Remark 7.6).

As pointed out above, the approximate metric defined in (9.9) is insufficient for our purposes, and needs to be refined. To define the new approximate metric, we replace $g_{N}$ with $g_{N}^{(1)}=g_{N}+a^{2} b^{2} \tilde{H}_{2}(x)$, so that
$$g_{N}^{(1)}=g_{0}+\eta_{N}(x)+a^{2} b^{2} \tilde{H}_{2}(x), \quad|x| \leq a^{-1} .$$
By Proposition 7.2, for $a, b$ sufficiently small
$$\begin{aligned}
\left|a^{2} b^{2} \tilde{H}_{2}(x)\right| & \lesssim a^{2} b^{2}|x|^{2} \\
& \lesssim b^{2}
\end{aligned}$$
so that $g_{N}^{(1)}$ is indeed a Riemannian metric when $|x|<a^{-1}$.
Next, replace the compact metric $g_{Z}$ with $g_{Z}^{(1)}=g_{Z}+a^{2} b^{2} \tilde{H}_{-2}(z)$, so that
$$g_{Z}^{(1)}=g_{0}+\eta_{Z}(z)+a^{2} b^{2} \tilde{H}_{-2}(z), \quad|z| \geq b .$$

By Proposition 7.5,
$$\begin{aligned}
\left|a^{2} b^{2} \tilde{H}_{-2}(z)\right| & \lesssim a^{2} b^{2} b^{-2} \\
& \lesssim a^{2}
\end{aligned}$$
hence $g_{Z}^{(1)}$ is a Riemannian metric for $|z| \geq b$.
Using these metrics, we then define the refined approximate metric $g_{a, b}^{(1)}$ on $X_{a, b}$ by
$$g_{a, b}^{(1)}= \begin{cases}a^{-2} b^{-2}\left(g_{Z}+a^{2} b^{2} \tilde{H}_{-2}(z)\right) & |z| \geq 2 b \\ g_{N}+a^{2} b^{2} \tilde{H}_{2}(x) & |x| \leq a^{-1}\end{cases}$$
while in the damage zone $a^{-1} \leq|x| \leq 2 a^{-1}$ the metric is given by
$$\begin{aligned}
g_{a, b}^{(1)}=d x^{2} & +\phi(a|x|)\left\{\eta_{N}(x)+a^{2} b^{2} \tilde{H}_{2}(x)\right\} \\
& +[1-\phi(a|x|)] \iota^{*}\left\{a^{-2} b^{-2}\left(\eta_{Z}(z)+a^{2} b^{2} \tilde{H}_{-2}(z)\right)\right\} .
\end{aligned}$$

Remark 10.2. From Propositions 7.2 and 7.5, it is clear that $g_{a, b}^{(1)}$ is invariant under the group action.
10.1. Damage zone estimate. We compute that
$$\begin{aligned}
\iota^{*}\left\{a^{-2} b^{-2}\left(g_{Z}+a^{2} b^{2} \tilde{H}_{-2}(z)\right)\right\} & =\iota^{*}\left\{a^{-2} b^{-2}\left(\delta_{i j}+\left(\eta_{Z}(z)\right)_{i j}+a^{2} b^{2} \tilde{H}_{-2}(z)_{i j}\right) d z^{i} d z^{j}\right\} \\
& =\left(\eta_{Z}(a b x)_{i j}+a^{2} b^{2} \tilde{H}_{-2}(a b x)_{i j}\right) d x^{i} d x^{j}
\end{aligned}$$
Consequently, in the damage zone, the metric is
$$\begin{aligned}
g_{a, b}^{(1)}=d x^{2} & +\phi(a|x|)\left\{\eta_{N}(x)+a^{2} b^{2} \tilde{H}_{2}(x)\right\} \\
& +[1-\phi(a|x|)]\left(\eta_{Z}(a b x)_{i j}+a^{2} b^{2} \tilde{H}_{-2}(a b x)_{i j}\right) d x^{i} d x^{j}
\end{aligned}$$
We next use the the expansions
$$\begin{aligned}
a^{2} b^{2} \tilde{H}_{2}(x)_{i j} & =-a^{2} b^{2}\left(\frac{1}{3} R_{i k j l}\left(z_{0}\right) x^{k} x^{l}+O^{(4)}\left(|x|^{\epsilon}\right)\right), \\
\eta_{Z}(a b x)_{i j} & =-a^{2} b^{2} \frac{1}{3} R_{i k j l}\left(z_{0}\right) x^{k} x^{l}+a^{4} b^{4} O^{(4)}\left(|x|^{4}\right),
\end{aligned}$$
$$\begin{aligned}
a^{2} b^{2} \tilde{H}_{-2}(a b x)_{i j} & =a^{2} b^{2}\left(H_{-2}(a b x)_{i j}+(a b)^{-\epsilon} O\left(|x|^{-\epsilon}\right)\right) \\
& =-\frac{1}{3} R_{i k j l}\left(y_{0}\right) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j}+(a b)^{2-\epsilon} O^{(4)}\left(|x|^{-\epsilon}\right),
\end{aligned}$$
and
$$\eta_{N}(x)_{i j}=-\frac{1}{3} R_{i k j l}\left(y_{0}\right) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j}+O^{(4)}\left(|x|^{-4+\epsilon}\right) .$$

Using (10.7)-(10.10), we obtain in the damage zone:
$$\begin{aligned}
\left(g_{a, b}^{(1)}\right)_{i j} & =\delta_{i j}-a^{2} b^{2} \frac{1}{3} R_{i k j l}\left(z_{0}\right) x^{k} x^{l}-\frac{1}{3} R_{i k j l}\left(y_{0}\right) \frac{x^{k} x^{l}}{|x|^{4}}+2 A \frac{1}{|x|^{2}} \delta_{i j} \\
& +a^{2} b^{2} O^{(4)}\left(|x|^{\epsilon}\right)+a^{4} b^{4} O^{(4)}\left(|x|^{4}\right)+(a b)^{2-\epsilon} O^{(4)}\left(|x|^{-\epsilon}\right)+O^{(4)}\left(|x|^{-4+\epsilon}\right) .
\end{aligned}$$

Proposition 10.3. The size of the $B^{t}$-tensor of the refined approximate metric in the damage zone is given by
$$\left|B^{t}\left(g_{a, b}^{(1)}\right)\right|_{g_{a, b}^{(1)}}=O\left(b^{2} a^{6-\epsilon}\right)+O\left(a^{4} b^{4}\right)+O\left(a^{6} b^{2-\epsilon}\right)+O\left(a^{8-\epsilon}\right)$$
as $a, b \rightarrow 0$.
Proof. By (10.11),
$$g_{a, b}^{(1)}=g_{0}+a^{2} b^{2} H_{2}+H_{-2}+\mathcal{E},$$
where
$$\mathcal{E}=a^{2} b^{2} O^{(4)}\left(|x|^{\epsilon}\right)+a^{4} b^{4} O^{(4)}\left(|x|^{4}\right)+(a b)^{2-\epsilon} O^{(4)}\left(|x|^{-\epsilon}\right)+O^{(4)}\left(|x|^{-4+\epsilon}\right) .$$
Let $\theta=g_{a, b}^{(1)}-g_{0}$; then using the expansion of the $B^{t}$-tensor in Proposition 3.8
$$\begin{aligned}
B^{t}\left(g_{a, b}^{(1)}\right) & =B^{t}\left(g_{0}\right)+\left(B_{0}^{t}\right)^{\prime}(\theta)+\mathcal{Q}_{0}(\theta) \\
& =\left(B_{0}^{t}\right)^{\prime}(\theta)+\mathcal{Q}_{0}(\theta)
\end{aligned}$$
By Lemma 7.3 and the fact that $\left(B_{0}^{t}\right)^{\prime}$ is fourth order,
$$\begin{aligned}
\left(B_{0}^{t}\right)^{\prime}(\theta) & =a^{2} b^{2}\left(B_{0}^{t}\right)^{\prime}\left(H_{2}\right)+\left(B_{0}^{t}\right)^{\prime}\left(H_{-2}\right)+\left(B_{0}^{t}\right)^{\prime}(\mathcal{E}) \\
& =\left(B_{0}^{t}\right)^{\prime}(\mathcal{E})
\end{aligned}$$
hence
$$B^{t}\left(g_{a, b}^{(1)}\right)=\left(B_{0}^{t}\right)^{\prime}(\mathcal{E})+\mathcal{Q}_{0}(\theta) .$$
If we estimate the norm of $B^{t}\left(g_{a, b}^{(1)}\right)$ in the flat metric, then (10.12) follows from the formula for $\mathcal{E}$ and the result of Proposition 3.8. However, by (10.11) it is clear that the same estimate holds if we use the norm with respect to $g_{a, b}^{(1)}$, since for any symmetric (0, 2)-tensor $T=T_{i j}$
$$\begin{aligned}
|T|_{g_{a, b}^{(1)}}^{2} & =\left\{g_{a, b}^{(1)}\right\}^{i k}\left\{g_{a, b}^{(1)}\right\}^{j \ell} T_{i j} T_{k \ell} \\
& =\left\{\delta_{i k}+O\left(a^{2}+b^{2}\right)\right\}\left\{\delta_{j \ell}+O\left(a^{2}+b^{2}\right)\right\}^{j \ell} T_{i j} T_{k \ell} \\
& =\left(1+O\left(a^{2}+b^{2}\right)\right)|T|_{0}^{2}
\end{aligned}$$ \(\square\)

Next, on the asymptotically flat piece we have

Proposition 10.4. On $\left\{|x|<a^{-1}\right\} \subset N$, the $B^{t}$-tensor satisfies
$$B^{t}\left(g_{a, b}^{(1)}\right)=a^{2} b^{2} \lambda k_{1}^{(0)}-a^{2} b^{2} \mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}+O\left(a^{4} b^{4}\right),$$
and
$$B^{t}\left(g_{a, b}^{(1)}\right)=a^{2} b^{2} \lambda k_{1}^{(0)}+a^{2} b^{2} O\left(|x|^{\epsilon-4}\right)+O\left(a^{4} b^{4}\right),$$
as $a, b \rightarrow 0$ and $|x| \rightarrow \infty$.
Proof. The proof proceeds along the same lines as the proof of Proposition 10.3. On $\left\{|x|<a^{-1}\right\} \subset N$ we have
$$g_{a, b}^{(1)}=g_{N}+a^{2} b^{2} \tilde{H}_{2} .$$
Let $\theta=g_{a, b}^{(1)}-g_{N}=a^{2} b^{2} \tilde{H}_{2}$. Using the expansion of the $B^{t}$-tensor again,
$$\begin{aligned}
B^{t}\left(g_{a, b}^{(1)}\right) & =B^{t}\left(g_{N}\right)+\left(B_{g_{N}}^{t}\right)^{\prime} \theta+\mathcal{Q}_{N}(\theta) \\
& =\left(B_{g_{N}}^{t}\right)^{\prime} \theta+\mathcal{Q}_{N}(\theta),
\end{aligned}$$
since $g_{N}$ is $B^{t}$-flat. From the formula for the linearized operator $S$ in (3.11) and Proposition 7.2 it follows that
$$\begin{aligned}
\left(B_{g_{N}}^{t}\right)^{\prime} \theta & =S_{g_{N}} \theta-\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\theta} \\
& =a^{2} b^{2} S\left(\tilde{H}_{2}\right)-a^{2} b^{2} \mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}_{2}} \\
& =a^{2} b^{2} \lambda k_{1}^{(0)}-a^{2} b^{2} \mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \tilde{H}_{2}^{\circ}
\end{aligned}$$
Substituting this into (10.20) gives
$$B^{t}\left(g_{a, b}^{(1)}\right)=a^{2} b^{2} \lambda k_{1}^{(0)}-a^{2} b^{2} \mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}+\mathcal{Q}_{N}(\theta) .$$

By part (i) of Proposition 3.7,
$$\left|Q_{N}\left(a^{2} b^{2} \tilde{H}_{2}\right)\right|_{g_{N}}=O\left(a^{4} b^{4}\right),$$
and from our observations above the same estimate holds if we estimate with respect to the norm induced by $g_{a, b}^{(1)}$. Therefore, (10.17) follows from this estimate and (10.22).

To estimate the gauge-fixing term in (10.22), we first observe that $\delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}}$ : $S^{2}\left(T^{*} N\right) \rightarrow T^{*} N$ is a third order differential operator, while
$$\nabla_{N}^{3}=\partial^{3}+\Gamma\left(g_{N}\right) \partial^{2}+\left[\partial \Gamma\left(g_{N}\right)+\Gamma\left(g_{N}\right)^{2}\right] \partial+\left[\partial^{2} \Gamma\left(g_{N}\right)+\Gamma\left(g_{N}\right) \partial \Gamma\left(g_{N}\right)\right],$$
where $\nabla_{N}$ denotes the covariant derivative and $\Gamma\left(g_{N}\right)$ the Christoffel symbols in the $g_{N}$-metric. Since
$$\begin{aligned}
\tilde{H}_{2} & =H_{2}+O^{(4)}\left(|x|^{\epsilon}\right), \\
\Gamma_{N} & =O^{(3)}\left(|x|^{-3}\right),
\end{aligned}$$
it follows that
$$a^{2} b^{2} \mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}=a^{2} b^{2} O\left(|x|^{\epsilon-4}\right),$$
and combining this with (10.23) and (10.22) we obtain (10.18). \(\square\)

Next, on the compact piece, we have
Proposition 10.5. On $\{|z| \geq 2 b\} \subset Z$, we have
$$\left|B^{t}\left(g_{a, b}^{(1)}\right)\right|_{g_{a, b}^{(1)}}=a^{6} b^{6} O\left(|z|^{-\epsilon-4}\right) .$$
as $a, b,|z| \rightarrow 0$.
Proof. Recall the metric $g_{Z}^{(1)}$ defined in (10.2):
$$g_{Z}^{(1)}=g_{0}+\eta_{Z}(z)+a^{2} b^{2} \tilde{H}_{-2}(z), \quad|z| \geq 2 b,$$
so that on the compact piece $\{|z| \geq 2 b\} \cap Z$ the refined approximate metric $g_{a, b}^{(1)}$ is just a rescaling of $g_{Z}^{(1)}$ :
$$g_{a, b}^{(1)}=a^{-2} b^{-2} g_{Z}^{(1)} .$$
We can then essentially repeat the arguments of the preceding propositions and write $g_{Z}^{(1)}=g_{Z}+\theta$, where $\theta=a^{2} b^{2} \tilde{H}_{-2}$, then expand $B^{t}$ :
$$\begin{aligned}
B^{t}\left(g_{Z}^{(1)}\right) & =B^{t}\left(g_{Z}\right)+\left(B_{Z}^{t}\right)^{\prime}(\theta)+\mathcal{Q}_{Z}(\theta) \\
& =\left(B_{Z}^{t}\right)^{\prime}(\theta)+\mathcal{Q}_{Z}(\theta),
\end{aligned}$$
where as usual the subscript $Z$ indicates that the tensor is with respect to the metric $g_{Z}$.

We first estimate the term involving the linearization of $B^{t}$, by comparing $\left(B_{Z}^{t}\right)^{\prime}(\theta)$ and $\left(B_{0}^{t}\right)^{\prime}(\theta)$, i.e., the linearized operator with respect to the flat metric acting on $\theta$. Recall from Lemma 7.3 and Proposition 7.5 that
$$\begin{aligned}
\left(B_{0}^{t}\right)^{\prime}(\theta) & =a^{2} b^{2}\left(B_{0}^{t}\right)^{\prime}\left(\tilde{H}_{-2}\right) \\
& =a^{2} b^{2}\left(B_{0}^{t}\right)^{\prime}\left(H_{-2}+O\left(|z|^{-\epsilon}\right)\right) \\
& =a^{2} b^{2} O\left(|z|^{-\epsilon-4}\right) .
\end{aligned}$$
Clearly, for any metric $g$ the operators $\left(B^{t}\right)^{\prime}$ and $S$ have the same general form, as given in (7.6):
$$\begin{aligned}
\left(B^{t}\right)^{\prime} \theta & =\left(g^{-2}+g * g^{-3}\right) * \nabla^{4} \theta+g * g^{-3} * R m * \nabla^{2} \theta+g * g^{-3} * \nabla R m * \nabla \theta \\
& +\left(g^{-2}+g * g^{-3}\right) *\left(\nabla^{2} R m+R m * R m\right) * \theta .
\end{aligned}$$
Using this, we can estimate the difference
$$\left[\left(B_{Z}^{t}\right)^{\prime}-\left(B_{0}^{t}\right)^{\prime}\right](\theta) .$$

We will need the following estimates, which follow from (3.35), (9.1), and (9.2):
$$\begin{aligned}
g_{Z}-g_{0} & =O\left(b^{2}\right), \\
\nabla_{Z}^{m} T-\nabla_{0}^{m} T & =O(b) * \nabla_{0}^{m-1} T+O(1) *\left\{\nabla_{0}^{m-2} T+\cdots+T\right\} .
\end{aligned}$$
Then by (10.28),
$$\left|\left[\left(B_{Z}^{t}\right)^{\prime}-\left(B_{0}^{t}\right)^{\prime}\right](\theta)\right|=a^{2} b^{2} O\left(|z|^{-4}\right) .$$
Combining with (10.27), we obtain
$$\left|\left(B_{Z}^{t}\right)^{\prime}(\theta)\right|_{0}=a^{2} b^{2} O\left(|z|^{-\epsilon-4}\right) .$$
It is easy to see that the same estimate holds if we estimate with respect to the norm induced by $g_{Z}^{(1)}$.

For the remainder term $\mathcal{Q}$ in (10.26) we use Proposition 3.8 to show
$$\left|\mathcal{Q}_{Z}(\theta)\right|_{g_{Z}}=a^{4} b^{4} O\left(|z|^{-8}\right),$$
with the same estimate in the $g_{Z}^{(1)}$-metric. Combining (10.31) and (10.32) gives
$$\left|B^{t}\left(g_{Z}^{(1)}\right)\right|_{g_{Z}^{(1)}}=a^{2} b^{2} O\left(|z|^{-\epsilon-4}\right)+a^{4} b^{4} O\left(|z|^{-6}\right)$$
Since $|z| \geq b$, this implies
$$\left|B^{t}\left(g_{Z}^{(1)}\right)\right|_{g_{Z}^{(1)}}=a^{2} b^{2} O\left(|z|^{-\epsilon-4}\right) .$$

By the scaling properties of the $B^{t}$-tensor,
$$\begin{aligned}
B^{t}\left(g_{a, b}^{(1)}\right) & =B^{t}\left(a^{-2} b^{-2} g_{Z}^{(1)}\right) \\
& =a^{2} b^{2} B^{t}\left(g_{Z}^{(1)}\right)
\end{aligned}$$
Using (10.34) and (10.25) we conclude
$$\begin{aligned}
\left|B^{t}\left(g_{a, b}^{(1)}\right)\right|_{g_{a, b}^{(1)}} & =\left|a^{2} b^{2} B^{t}\left(g_{Z}^{(1)}\right)\right|_{g_{a, b}^{(1)}} \\
& =a^{2} b^{2}\left|a^{2} b^{2} B^{t}\left(g_{Z}^{(1)}\right)\right|_{g_{Z}^{(1)}} \\
& =a^{4} b^{4}\left|B^{t}\left(g_{Z}^{(1)}\right)\right|_{g_{Z}^{(1)}} \\
& =a^{6} b^{6} O\left(|z|^{-\epsilon-4}\right) .
\end{aligned}$$ \(\square\)

Finally, we have
Proposition 10.6. Choosing $a=b$, we have
$$\left\|B^{t}\left(g_{a, a}^{(1)}\right)-a^{4} \lambda k_{1}^{(0)}\right\|_{C_{\delta-4}^{0, \alpha}\left(X_{a, a}\right)}=O\left(a^{4+\delta-\epsilon}\right)$$
as $a \rightarrow 0$.

Proof. We begin estimating the leading term in the $C_{\delta-4}^{0, \alpha}$-norm. On the damage zone, $k_{1}^{(0)}=0$, so by (10.12)
$$w^{4-\delta}\left|B^{t}\left(g_{a, a}^{(1)}\right)-a^{4} \lambda k_{1}^{(0)}\right|=O\left(a^{\delta-4} a^{8-\epsilon}\right)=O\left(a^{4+\delta-\epsilon}\right) .$$
By (10.18), on the AF piece
$$\begin{aligned}
w^{4-\delta}\left|B^{t}\left(g_{a, a}^{(1)}\right)-a^{4} \lambda k_{1}^{(0)}\right| & =|x|^{4-\delta}\left\{a^{4} O\left(|x|^{\epsilon-4}\right)+O\left(a^{8}\right)\right\} \\
& =a^{4} O\left(|x|^{\epsilon-\delta}\right)+a^{8} O\left(|x|^{4-\delta}\right) .
\end{aligned}$$

Recall from Remark 10.1 that $-\epsilon<\delta<0$; hence $\epsilon-\delta>0$ and
$$w^{4-\delta}\left|B^{t}\left(g_{a, a}^{(1)}\right)-a^{4} \lambda k_{1}^{(0)}\right|=O\left(a^{4+\delta-\epsilon}\right) .$$

On the compact piece, by (10.24)
$$\begin{aligned}
w^{4-\delta}\left|B^{t}\left(g_{a, a}^{(1)}\right)-a^{4} \lambda k_{1}^{(0)}\right| & =a^{2 \delta-8} O\left(|z|^{4-\delta}\right)\left\{a^{12} O\left(|z|^{-\epsilon-4}\right)\right\} \\
& =a^{2 \delta+4} O\left(|z|^{-\delta-\epsilon}\right) \\
& =O\left(a^{4+\delta-\epsilon}\right),
\end{aligned}$$
since $|z| \geq 2 a$ and $-\epsilon<\delta<0$ (see Remark 10.1).
For estimating the Hölder part of the weighted norm, one must use the formula (3.52) in the proof of Proposition 3.7. For example, the term with $h * \nabla^{4} h$ is estimated like
$$\begin{aligned}
& w^{4-\delta}\left(x_{0}\right) \frac{\left|\left(h * \nabla^{4} h\right)\left(x_{1}\right)-\left(h * \nabla^{4} h\right)\left(x_{2}\right)\right|}{\left|d\left(x_{1}, x_{2}\right)\right|^{\alpha}} \\
& \quad \leq w^{-\delta}\left(x_{0}\right)\left|h\left(x_{1}\right)\right| \cdot w^{4-\delta}\left(x_{0}\right) \frac{\left|\nabla^{4} h\left(x_{1}\right)-\nabla^{4} h\left(x_{2}\right)\right|}{d\left(x_{1}, x_{2}\right)^{\alpha}} \\
& \quad+w^{-\delta}\left(x_{0}\right) \frac{\left|h\left(x_{1}\right)-h\left(x_{2}\right)\right|}{\left|d\left(x_{1}, x_{2}\right)\right|^{\alpha}} \cdot w^{4-\delta}\left(x_{0}\right)\left|\nabla^{4} h\left(x_{2}\right)\right|
\end{aligned}$$
and all other terms are estimated similarly, the complete computation is lengthy but straightforward, so is omitted. \(\square\)
10.2. The approximate cokernel. In this subsection, we define tensors $o_{1}, o_{2}, o_{3}$ and $k_{1}, k_{2}, k_{3}$ which will be crucial in the Lyapunov-Schmidt reduction in Section 11.

Remark 10.7. It is clear that all of the tensors in this section may be chosen to be invariant under the group action, so we will do this automatically without mention in every case.

Recall from Section 5 we denoted the cokernel of the asymptotically flat manifold $\left(N, g_{N}\right)$ by $o_{1}$, and it is given by
$$o_{1}=\mathcal{K} \omega_{1}+f g_{N} .$$

In Section 7 we defined a compactly supported symmetric (0, 2)-tensor $k_{1}^{(0)} \in C_{\delta-4}$ which satisfies
$$\begin{aligned}
\left\|k_{1}^{(0)}\right\|_{C_{\delta-4}} & \leq C_{1} \\
\int\left\langle k_{1}^{(0)}, o_{1}\right\rangle_{g^{(0)}} d V_{g^{(0)}} & =1
\end{aligned}$$
where $C_{1}$ is independent of $a, b$. Note that the quantities in (10.42) and (10.43) are all computed with respect to the "naive" approximate metric $g^{(0)}$ defined in Section 9. Since from now on we will be working in the refined approximate metric $g^{(1)}$ defined in Section 10, we will need to slightly rescale $k_{1}^{(0)}$ so that (10.42) and (10.43) hold with respect to $g^{(1)}$. To this end, define
$$k_{1}=\left\{\int\left\langle k_{1}^{(0)}, o_{1}\right\rangle_{g^{(1)}} d V_{g^{(1)}}\right\}^{-1} k_{1}^{(0)}$$
Then by (10.43) and (10.44),
$$\int\left\langle k_{1}, o_{1}\right\rangle_{g^{(1)}} d V_{g^{(1)}}=1$$

Claim 10.8. We have
$$k_{1}^{(0)}=\left(1+O\left(b^{2}\right)\right) k_{1} .$$
Proof. By (10.3), on the support of $k_{1}^{(0)}$ we have
$$\begin{aligned}
g=g^{(1)} & =g_{N}+O\left(b^{2}\right) \\
& =g^{(0)}+O\left(b^{2}\right),
\end{aligned}$$
hence the volume forms satisfy
$$d V_{g^{(1)}}=\left(1+O\left(b^{2}\right)\right) d V_{g^{(0)}}$$
Therefore,
$$\begin{aligned}
\int\left\langle k_{1}^{(0)}, o_{1}\right\rangle_{g^{(1)}} & d V_{g^{(1)}}=\int\left[g^{(1)}\right]^{i k}\left[g^{(1)}\right]^{j \ell}\left[k_{1}^{(0)}\right]_{i j}\left[o_{1}\right]_{k \ell} d V_{g^{(1)}} \\
= & \int\left\{\left[g^{(0)}\right]^{i k}+O\left(b^{2}\right)\right\}\left\{\left[g^{(0)}\right]^{j \ell}+O\left(b^{2}\right)\right\}\left[k_{1}^{(0)}\right]_{i j}\left[o_{1}\right]_{k \ell}\left(1+O\left(b^{2}\right)\right) d V_{g^{(0)}} \\
= & \int\left\langle k_{1}^{(0)}, o_{1}\right\rangle_{g^{(0)}} d V_{g^{(0)}}+O\left(b^{2}\right) \\
= & 1+O\left(b^{2}\right)
\end{aligned}$$
Substituting this into (10.44) gives (10.46). \(\square\)

Remark 10.9. From now on, all metric-dependent quantities will be with respect to $g=g^{(1)}$. To simplify the notation, we will suppress the superscript.

Let $o_{3}$ denote the cokernel element on the compact manifold ( $Z, g_{Z}$ ) given by scaling of the metric:
$$o_{3}=(a b)^{-2+\delta} g_{Z} .$$
(The reason for the scale factor will become apparent in a moment). Fix a smooth positive cut-off function $\phi_{3}$ supported in $Z \backslash\left\{z_{0}\right\}$ with
$$\int \phi_{3}\left|g_{Z}\right|^{2} d V=1$$
where we again emphasize that the volume form and inner product are with respect to $g=g^{(1)}$. Define
$$k_{3}=(a b)^{2-\delta} \phi_{3} g_{Z} .$$
We claim that there is a constant $C_{2}$ such that
$$\left\|k_{3}\right\|_{C_{\delta-4}} \leq C_{2} .$$
To see this, first recall that by (10.3), (10.3), on the support of $\phi_{3}$ we have
$$\begin{aligned}
& {\left[g^{(1)}\right]_{i j}=(a b)^{-2}\left[\left(g_{Z}\right)_{i j}+O\left(b^{2}\right)\right],} \\
& {\left[g^{(1)}\right]^{i j}=(a b)^{2}\left[\left(g_{Z}\right)^{i j}+O\left(b^{2}\right)\right] .}
\end{aligned}$$
Also, on the support of $\phi_{3}$ the weight $w(x) \approx(a b)^{-2}$. It follows that
$$\begin{aligned}
\sup \left|k_{3}\right|_{g^{(1)}} w^{4-\delta}= & c_{2}(a b)^{2-\delta} \sup \left|\phi_{3}\right|\left|g_{Z}\right|_{g^{(1)}} w^{4-\delta} \\
= & c_{2}(a b)^{2-\delta} \sup \left|\phi_{3}\right|\left\{\left[g^{(1)}\right]^{i k}\left[g^{(1)}\right]^{j \ell}\left(g_{Z}\right)_{i j}\left(g_{Z}\right)_{k \ell}\right\}^{1 / 2} w^{4-\delta} \\
= & c_{2}(a b)^{2-\delta} \sup \left\{| \phi _ { 3 } | \left\{(a b)^{4}\left[\left(g_{Z}\right)^{i k}+O\left(b^{2}\right)\right]\right.\right. \\
& \left.\left.\times\left[\left(g_{Z}\right)^{j \ell}+O\left(b^{2}\right)\right]\left(g_{Z}\right)_{i j}\left(g_{Z}\right)_{k \ell}\right\}^{1 / 2} w^{4-\delta}\right\} \\
\leq & C_{2} .
\end{aligned}$$
This estimate clarifies the choice of scaling in the definitions of $k_{3}$ and $o_{3}$ : the scale factor $(a b)^{2-\delta}$ in (10.52) is necessary to get the bound (10.53), while the factor $(a b)^{-2+\delta}$ in the definition of $o_{3}$ was chosen to give the normalization
$$\begin{aligned}
\int\left\langle k_{3}, o_{3}\right\rangle d V & =\int\left\langle(a b)^{2-\delta} \phi_{3} g_{Z},(a b)^{-2+\delta} g_{Z}\right\rangle d V \\
& =\int \phi_{3}\left|g_{Z}\right|^{2} d V=1
\end{aligned}$$

Next, denote
$$o_{2}=g=g^{(1)} .$$
We claim that there is a tensor $k_{2}$, compactly supported in $N$, which satisfies the normalization
$$\int\left\langle k_{2}, o_{2}\right\rangle d V=\int \operatorname{tr}_{g} k_{2} d V=1$$
and the orthogonality condition
$$\int\left\langle k_{2}, o_{1}\right\rangle d V=0$$
(Note that the integral in (10.57) makes sense, since $k_{2}$ is compactly supported in $N$, even though $o_{1}$ is not globally defined.)

To see that such a tensor exists, just take two smooth, positive cut-off functions $\eta_{1}, \eta_{2}$ with compact support in $N$ and let
$$k_{2}=\left(c_{1} \eta_{1}+c_{2} \eta_{2}\right) o_{2}=\left(c_{1} \eta_{1}+c_{2} \eta_{2}\right) g,$$
where $c_{1}$ and $c_{2}$ are constants to be determined. Then
$$\begin{aligned}
& \int\left\langle k_{2}, o_{1}\right\rangle d V=c_{1} \int \eta_{1}\left(\operatorname{tr}_{g} o_{1}\right) d V+c_{2} \int \eta_{2}\left(\operatorname{tr}_{g} o_{1}\right) d V \\
& \int\left\langle k_{2}, o_{2}\right\rangle d V=4 c_{1} \int \eta_{1} d V+4 c_{2} \int \eta_{2} d V
\end{aligned}$$
By (10.47), on the support of $k_{2}$
$$g=g^{(1)}=g_{N}+O\left(b^{2}\right) .$$
Therefore,
$$\begin{aligned}
\operatorname{tr}_{g} o_{1} & =\left[g^{(1)}\right]^{k \ell}\left(o_{1}\right)_{k \ell} \\
& =\left[g_{N}+O\left(b^{2}\right)\right]^{k \ell}\left[\mathcal{K} \omega_{1}+f g_{N}\right]_{k \ell} \\
& =4 f+O\left(b^{2}\right)
\end{aligned}$$
Therefore, we can estimate the integrals in (10.58) by
$$\begin{aligned}
& \int\left\langle k_{2}, o_{1}\right\rangle d V=c_{1}\left\{4 \int \eta_{1} f d V+O\left(b^{2}\right)\right\}+c_{2}\left\{4 \int \eta_{2} f d V+O\left(b^{2}\right)\right\} \\
& \int\left\langle k_{2}, o_{2}\right\rangle d V=c_{1}\left\{4 \int \eta_{1} d V\right\}+c_{2}\left\{4 \int \eta_{2} d V\right\}
\end{aligned}$$
Consequently, once $a, b$ are small enough it is possible to choose the cut-off functions $\eta_{1}, \eta_{2}$ and the constants $c_{1}, c_{2}$ so that (10.56) and (10.57) hold.

\section*{11. Lyapunov-Schmidt reduction}

In this section, we perform the main reduction of the problem from an infinitedimensional problem to a finite-dimensional problem.

Remark 11.1. Since we are carrying out an equivariant gluing construction, from now on all operators are understood to act on sections of the relevant bundle which are invariant under the group actions described above.
11.1. The modified nonlinear map. Let
$$\mathcal{D}=\left\{h \in C_{\delta}^{4, \alpha}\left(X_{a, b}\right): \int\left\langle h, k_{1}\right\rangle=0, \int\left\langle h, k_{3}\right\rangle=0\right\} .$$
Define the mapping $H^{t}: \mathbb{R} \times \mathbb{R} \times \mathcal{D} \rightarrow C_{\delta-4}^{0, \alpha}\left(X_{a, b}\right)$ by
$$H^{t}\left(\lambda_{1}, \lambda_{2}, \theta\right)=P_{g^{(1)}}(\theta)-\lambda_{1} k_{1}-\lambda_{2} k_{2} .$$
Let $\left(H^{t}\right)^{\prime}: \mathbb{R} \times \mathbb{R} \times \mathcal{D} \rightarrow C_{\delta-4}^{0, \alpha}$ denote the linearization of $H$ at $(0,0,0)$ :
$$\left(H^{t}\right)^{\prime}\left(\lambda_{1}, \lambda_{2}, h\right)=\left.\frac{d}{d s} H^{t}\left(s \lambda_{1}, s \lambda_{2}, s h\right)\right|_{s=0} .$$
Then $\left(H^{t}\right)^{\prime}$ is given by
$$\left(H^{t}\right)^{\prime}\left(\lambda_{1}, \lambda_{2}, h\right)=S(h)-\lambda_{1} k_{1}-\lambda_{2} k_{2},$$
where $S=S^{t}$ is the linearization of $P$ at $g^{(1)}$.
Proposition 11.2. For $a, b$ sufficiently small, the map $\left(H^{t}\right)^{\prime}: \mathbb{R} \times \mathbb{R} \times \mathcal{D} \rightarrow C_{\delta-4}^{0, \alpha}$ is uniformly injective: i.e., there is a constant $\delta_{0}>0$ which is independent of $a, b$ such that
$$\left\|\left(H^{t}\right)^{\prime}\left(\lambda_{1}, \lambda_{2}, h\right)\right\|_{C_{\delta-4}^{\alpha}} \geq \delta_{0}\left(\left|\lambda_{1}\right|+\left|\lambda_{2}\right|+\|h\|_{C_{\delta}^{4, \alpha}}\right) .$$
Proof. We argue via contradiction: if (11.5) does not hold, then there is a sequence $\left(\lambda_{1}^{i}, \lambda_{2}^{i}, h_{i}\right) \in \mathcal{D}$ with
$$\begin{aligned}
& \left|\lambda_{1}^{i}\right|+\left|\lambda_{2}^{i}\right|+\left\|h_{i}\right\|_{C_{\delta}^{4, \alpha}}=1 \quad \forall i, \\
& \epsilon_{i} \equiv\left(H^{t}\right)^{\prime}\left(\lambda_{1}^{i}, \lambda_{2}^{i}, h_{i}\right) \rightarrow 0 \text { in } C_{\delta-4}^{0, \alpha} .
\end{aligned}$$
If we pair $\epsilon_{i}$ with $\eta o_{1}$ and integrate, where $\eta$ is a cut-off function with
$$\eta(x)= \begin{cases}1 & |x| \leq a^{-1} \\ 0 & |x|>2 a^{-1},\end{cases}$$
then
$$\int\left\langle\epsilon_{i}, \eta o_{1}\right\rangle d V=\int_{B}\left\langle S h_{i}, \eta o_{1}\right\rangle d V-\lambda_{1}^{i} \int\left\langle k_{1}, \eta o_{1}\right\rangle d V-\lambda_{2}^{i} \int\left\langle k_{2}, \eta o_{1}\right\rangle d V$$
Since $\eta \equiv 1$ on the support of $k_{1}$ and $k_{2}$, by the normalization (10.42) and the orthogonality condition (10.57) we can rewrite this as
$$\lambda_{1}^{i}=-\int\left\langle\epsilon_{i}, \eta o_{1}\right\rangle d V+\int\left\langle S h_{i}, \eta o_{1}\right\rangle d V$$
For the first term on the right-hand side, note that
$$\left\|\epsilon_{i}\right\|_{C_{\delta-4}^{0, \alpha}}^{0, \alpha} \geq \sup \left\{\left|\epsilon_{i}\right| w^{4-\delta}\right\},$$
where $w$ is the weight function. According to (9.16), on the support of $\eta$ the weight function is $w(x)=|x|$ (for $|x|$ large). Also, by Theorem 6.1 the cokernel $o_{1}$ satisfies
$$\left|o_{1}\right| \leq C|x|^{-2} .$$

Therefore,
$$\begin{aligned}
\left|\int\left\langle\epsilon_{i}, \eta o_{1}\right\rangle d V\right| & \leq \int\left|\epsilon_{i}\right| \| \eta o_{1} \mid d V \\
& \leq C\left\|\epsilon_{i}\right\|_{C_{\delta-4}^{0, \alpha}} \int_{1 \ll|x| \leq a^{-1} / 2}|x|^{\delta-4}|x|^{-2} d V \\
& \leq C\left\|\epsilon_{i}\right\|_{C_{\delta-4}^{0, \alpha}} \rightarrow 0
\end{aligned}$$
as $i \rightarrow \infty$.
For the second term on the right-hand side of (11.9) we integrate by parts, using the fact that $S$ is self-adjoint:
$$\int\left\langle S h_{i}, \eta o_{1}\right\rangle d V=\int\left\langle h_{i}, S\left(\eta o_{1}\right)\right\rangle d V$$
Using the formula for $S$ in (7.6) and the Leibniz rule, write
$$\begin{aligned}
S\left(\eta o_{1}\right)= & \left(g^{-2}+g * g^{-3}\right) * \nabla^{4}\left(\eta o_{1}\right)+g * g^{-3} * R m * \nabla^{2}\left(\eta o_{1}\right) \\
& +g * g^{-3} * \nabla R m * \nabla\left(\eta o_{1}\right)+\left(g^{-2}+g * g^{-3}\right) *\left(\nabla^{2} R m+R m * R m\right) *\left(\eta o_{1}\right) \\
= & \eta S o_{1}+\left(g^{-2}+g * g^{-3}\right) * \sum_{j \geq 1}^{4} \nabla^{4-j} o_{1} * \nabla^{j} \eta \\
& \quad+g * g^{-3} * R m * \sum_{j \geq 1}^{2} \nabla^{2-j} o_{1} * \nabla^{j} \eta+g * g^{-3} * \nabla R m * o_{1} * \nabla \eta .
\end{aligned}$$
By (5.45) and Theorem 6.1, on the support of $|\nabla \eta|$
$$\begin{aligned}
\left|\nabla^{m} o_{1}\right| & =O\left(a^{m+2}\right), \\
\left|\nabla^{m} \eta\right| & =O\left(a^{m}\right), \\
\left|\nabla^{m} R m\right| & =O\left(a^{m+4}\right) .
\end{aligned}$$
Therefore, from (11.13) we have
$$S\left(\eta o_{1}\right)=\eta S o_{1}+\{\text { Error }\},$$
where the error is supported on $\left\{a^{-1} / 4 \leq|x| \leq a^{-1} / 2\right\}$ and satisfies
$$\mid\{\text { Error }\} \mid=O\left(a^{6}\right) .$$
It follows from (11.12)
$$\int\left\langle S h_{i}, \eta o_{1}\right\rangle d V=\int\left\langle h_{i}, \eta S\left(o_{1}\right)\right\rangle d V+\int\left\langle h_{i},\{\text { Error }\}\right\rangle d V$$
Since $\left\|h_{i}\right\|_{C_{\delta}^{4, \alpha}} \leq 1$,
$$\left|h_{i}\right| \leq C w^{\delta},$$
hence on the support of Error
$$\left|h_{i}\right| \leq C a^{-\delta},$$
hence by (11.15)
$$\mid \int_{\left\{a^{-1} / 4 \leq|x| \leq a^{-1} / 2\right\}}\left\langle h_{i},\{\text { Error }\}\right\rangle d V \mid \leq C a^{2-\delta} .$$
Therefore,
$$\int\left\langle S h_{i}, \eta o_{1}\right\rangle d V=\int\left\langle h_{i}, \eta S o_{1}\right\rangle d V+O\left(a^{2-\delta}\right)$$

Let $S_{N}$ denote the linearized operator with respect to the metric $g_{N}$. Then $S_{N} o_{1}=$ 0, hence
$$\begin{aligned}
S o_{1} & =\left(S-S_{N}\right) o_{1}+S_{N} o_{1} \\
& =\left(S-S_{N}\right) o_{1}
\end{aligned}$$
Using (7.6) with (10.47), we can estimate
$$\begin{aligned}
\left|\left(S-S_{N}\right) o_{1}\right| & \lesssim b^{2}\left|\nabla^{4} o_{1}\right|+b^{2} a\left|\nabla^{3} o_{1}\right|+a^{2} b^{2}\left|\nabla^{2} o_{1}\right|+a^{3} b^{2}\left|\nabla o_{1}\right| \\
& +a^{4} b^{2}\left|o_{1}\right|+b^{2}|R m|\left|\nabla^{2} o_{1}\right|+b^{2}|\nabla R m|\left|\nabla o_{1}\right|+b^{2}\left(\left|\nabla^{2} R m\right|+|R m|^{2}\right)\left|o_{1}\right| .
\end{aligned}$$
Therefore, by (11.18),
$$\begin{aligned}
\left|\int\left\langle h_{i}, \eta S o_{1}\right\rangle d V\right| & =\left|\int\left\langle h_{i}, \eta\left(S-S_{N}\right) o_{1}\right\rangle d V\right| \\
& \leq C \int w^{\delta}\left|\left(S-S_{N}\right) o_{1}\right| d V \\
& \leq C b^{2} a^{2-\delta}
\end{aligned}$$
Combining the above, we conclude
$$\int\left\langle S h_{i}, \eta o_{1}\right\rangle d V=O\left(a^{2-\delta}\right),$$
hence by (11.9),
$$\lambda_{1}^{i} \rightarrow 0 \text { as } i \rightarrow \infty .$$

Next, pair $\epsilon_{i}$ with $\eta o_{2}$ and integrate:
$$\int\left\langle\epsilon_{i}, \eta o_{2}\right\rangle d V=\int\left\langle S h_{i}, \eta o_{2}\right\rangle d V-\lambda_{1}^{i} \int\left\langle k_{1}, \eta o_{2}\right\rangle d V-\lambda_{2}^{i} \int\left\langle k_{2}, \eta o_{2}\right\rangle d V$$
By the normalization (10.56), we can rewrite this as
$$\lambda_{2}^{i}=-\int\left\langle\epsilon_{i}, \eta o_{2}\right\rangle d V+\int\left\langle S h_{i}, \eta o_{2}\right\rangle d V-\lambda_{1}^{i} \int\left\langle k_{1}, \eta o_{2}\right\rangle d V$$

As in (11.11), we can estimate the first integral on the right as
$$\begin{aligned}
\left|\int\left\langle\epsilon_{i}, \eta o_{2}\right\rangle d V\right| & \leq \int\left|\epsilon_{i}\right|\left|\eta o_{2}\right| d V \\
& \leq C\left\|\epsilon_{i}\right\|_{C_{\delta-4}^{0, \alpha}} \int_{1<|x| \leq a^{-1} / 2}|x|^{\delta-4} d V \\
& \leq C_{\delta}\left\|\epsilon_{i}\right\|_{C_{\delta-4}^{0, \alpha}}(\text { since } \delta<0)
\end{aligned}$$
which limits to 0 as $i \rightarrow \infty$. The second term on the right we estimate as we did above; namely,
$$\int\left\langle S h_{i}, \eta o_{2}\right\rangle d V=\int\left\langle h_{i}, S\left(\eta o_{2}\right)\right\rangle d V$$
Using the fact that $\nabla o_{2}=0$, we can estimate as in (11.13):
$$\begin{aligned}
S\left(\eta o_{2}\right)= & \left(g^{-2}+g * g^{-3}\right) * \nabla^{4}\left(\eta o_{2}\right)+g * g^{-3} * R m * \nabla^{2}\left(\eta o_{2}\right) \\
+ & g * g^{-3} * \nabla R m * \nabla\left(\eta o_{2}\right)+\left(g^{-2}+g * g^{-3}\right) *\left(\nabla^{2} R m+R m * R m\right) *\left(\eta o_{2}\right) \\
= & \eta S o_{2}+\left(g^{-2}+g * g^{-3}\right) * \nabla^{4} \eta * o_{2}+g * g^{-3} * R m * \nabla^{2} \eta * o_{2} \\
& +g * g^{-3} * \nabla R m * o_{2} * \nabla \eta .
\end{aligned}$$
Since $S o_{2}=S g=0$,
$$\begin{aligned}
S\left(\eta o_{2}\right) & =\eta S o_{2}+\{\text { Error }\}, \\
& =\{\text { Error }\},
\end{aligned}$$
where the error is supported on $\left\{a^{-1} / 4 \leq|x| \leq a^{-1} / 2\right\}$ and satisfies
$$\mid\{\text { Error }\} \mid=O\left(a^{4}\right) .$$
Using (11.18), we can therefore estimate
$$\mid \int_{\left\{a^{-1} / 4 \leq|x| \leq a^{-1} / 2\right\}}\left\langle h_{i},\{\text { Error }\}\right\rangle d V \mid \leq C a^{-\delta}$$
Hence,
$$\int\left\langle S h_{i}, \eta o_{2}\right\rangle d V=O\left(a^{-\delta}\right)$$

For the last term in (11.27), we use the fact that $\lambda_{1}^{i} \rightarrow 0$, and that $k_{1}$ is compactly supported:
$$\begin{aligned}
\left|\lambda_{1}^{i} \int\left\langle k_{1}, \eta o_{2}\right\rangle d V\right| & \leq\left|\lambda_{1}^{i}\right| \int \eta\left|k_{1} \| o_{2}\right| d V \\
& \leq C\left|\lambda_{1}^{i}\right| \int_{\operatorname{supp}\left\{k_{1}\right\}} d V \\
& \leq C\left|\lambda_{1}^{i}\right| \rightarrow 0
\end{aligned}$$
as $i \rightarrow 0$. Combining with (11.32), (11.28), and (11.27), we see that
$$\lambda_{2}^{i} \rightarrow 0$$
as $i \rightarrow \infty$.
Consequently, by (11.6) we now know
$$\begin{aligned}
\left\|h_{i}\right\|_{C_{\delta}^{4, \alpha}} & \rightarrow 1, \\
\left\|S h_{i}\right\|_{C_{\delta-4}^{0, \alpha}}^{0, \alpha} & \rightarrow 0,
\end{aligned}$$
as $i \rightarrow \infty$.
The remainder of the proof is a standard "blow-up" argument, which we only briefly outline. Let $\left(a_{i}, b_{i}\right)$ be a sequence of gluing parameters with $\left(a_{i}, b_{i}\right) \rightarrow(0,0)$ as $i \rightarrow \infty$, and let $p_{i} \in X_{a_{i}, b_{i}}$ a sequence of points at which the supremum in (11.34) is attained. We have the three possibilities:
\begin{itemize}
\item[-] (1) $p_{i} \rightarrow p \in N$. In this case, standard elliptic estimates produce a nontrivial solution of the limiting equation $S h_{\infty}=0$ on $\left(N, g_{N}\right)$ with $h \in C_{\delta}^{4, \alpha}$. By Theorem 5.1, $h_{\infty}=c \cdot o_{1}$ for some $c \in \mathbb{R}$. Since
\end{itemize}
$$\int\left\langle h_{i}, k_{1}\right\rangle d V_{\left(a_{i}, b_{i}\right)}=0$$
$k_{1}$ has compact support on $N$, and $h_{i} \leq C w^{\delta}$, the integrand is bounded. Therefore,
$$\int\left\langle h_{\infty}, k_{1}\right\rangle d V_{g_{N}}=0$$
which implies that $c=0$, a contradiction.
\begin{itemize}
\item[-] (2) $p_{i} \rightarrow p \in Z \backslash\left\{z_{0}\right\}$. In this case, define $\tilde{h}_{i}=(a b)^{2+\delta} h_{i}$. It is easy to see that this scaling preserves the $C_{\delta}^{4, \alpha}$ norm, with respect to the metric $\tilde{g}_{a, b}^{(1)}=$ $(a b)^{2} g_{a, b}^{(1)}$. Standard elliptic estimates produce a nontrivial solution of the limiting equation $S \tilde{h}_{\infty}=0$ on $\left(Z, g_{Z}\right)$ with $h \in C_{\delta}^{4, \alpha}$. By Theorem 4.1, $h_{\infty}=c \cdot g_{Z}$ for some $c \in \mathbb{R}$. Since
\end{itemize}
$$\int\left\langle h_{i}, k_{3}\right\rangle d V_{\left(a_{i}, b_{i}\right)}=0$$
scaling shows that
$$\int\left\langle\tilde{h}_{i}, \phi_{3} g_{Z}\right\rangle_{\tilde{g}} d V_{\tilde{g}}=(a b)^{2 \delta} \cdot 0=0 .$$
Since $\phi_{3}$ has compact support on $Z \backslash\left\{z_{0}\right\}$, and $\tilde{h}_{i} \leq C \tilde{w}^{\delta}=C(a b w)^{\delta}$, the integrand is bounded, which implies that
$$\int\left\langle\tilde{h}_{\infty}, k_{3}\right\rangle d V_{g_{Z}}=0$$
which implies that $c=0$, a contradiction.
\begin{itemize}
\item[-] (3) If neither of the above cases happen, then there are two possibilities: a subsequence can approach the damage zone from the AF side, or from the
\end{itemize}
compact side. We give the argument in the former case, the proof of the latter case is similar. Fix a point $O \in N$ and let
$$d_{i}=\operatorname{dist}_{g_{a_{i}, b_{i}}^{(1)}}\left(O, p_{i}\right) .$$
Clearly, $d_{i} \rightarrow \infty$ as $i \rightarrow \infty$ (otherwise we are in case (1) above). For $i \gg 1$ we can view the sequence $\left\{p_{i}\right\} \subset N_{i}=N \cap A_{i}$, where $A_{i}$ is the annulus $\left\{R_{0}<|x|<2 a_{i}^{-1}\right\}$ and $N_{i}$ is equipped with the metric $g_{i}=g_{a_{i}, b_{i}}^{(1)}$. Let $\psi_{i}: A_{i} \rightarrow N$ denote dilation,
$$\psi_{i}: x \mapsto d_{i} x,$$
and define
$$\tilde{g}_{i}=\left.d_{i}^{-2} \psi_{i}^{*} g_{i}\right|_{\left\{m_{i} d_{i} \leq|x| \leq M_{i} d_{i}\right\}},$$
where $m_{i} \rightarrow 0$ and $M_{i} \rightarrow \infty$ are chosen so that the annulus $\left\{m_{i} d_{i} \leq|x| \leq\right.$ $\left.M_{i} d_{i}\right\} \subset N_{i}$. Denote the dilated coordinates by $\tilde{x}^{i}$; then $\tilde{g}_{i}$ is defined on the annulus $\left\{m_{i} \leq\left|\tilde{x}^{i}\right| \leq M_{i}\right\}$. Finally, define
$$\tilde{h}_{i}=d_{i}^{-2+\delta} \psi_{i}^{*} h_{i},$$
which preserves the $C_{\delta}^{4, \alpha}$-norm. Taking the limit as $i \rightarrow \infty$ we have $\tilde{g}_{i} \rightarrow d s^{2}$, the flat metric on $\mathbb{R}^{4} \backslash\{0\}, \tilde{h}_{i} \rightarrow h_{\infty}$, where $h_{\infty}$ satisfies
$$\begin{aligned}
S_{0} h_{\infty} & =0 \text { on } \mathbb{R}^{4} \backslash\{0\}, \\
h_{\infty} & \in C_{\delta}^{4, \alpha}\left(\mathbb{R}^{4} \backslash\{0\}\right),
\end{aligned}$$
and $S_{0}$ is the linearized operator with respect to the flat metric (see (3.13)). Note the weight function in the limit is given by $w=|x|$. Since $-1<\delta<0, \delta$ is not an indicial root by Proposition 4.4. This implies that $S_{0}: C_{\delta}^{4, \alpha} \rightarrow C_{\delta-4}^{0, \alpha}$ is an isomorphism (see [Bar86, LM85]), so $h_{\infty} \equiv 0$, which is a contradiction.
This contradiction argument finishes the proof of Proposition 11.2. \(\square\)

We next quote without proof the following standard implicit function theorem:
Lemma 11.3. Let $H: E \rightarrow F$ be a smooth map between Banach spaces. Define $Q=H-H(0)-H^{\prime}(0)$. Assume that there are positive constants $C_{1}, s_{0}, C_{2}$ so that the following are satisfied:
\begin{itemize}
\item[-] (1) The nonlinear term $Q$ satisfies
$$\|Q(x)-Q(y)\|_{F} \leq C_{1}\left(\|x\|_{E}+\|y\|_{E}\right)\|x-y\|_{E}$$
for every $x, y \in B_{E}\left(0, s_{0}\right)$.
\item[-] (2) The linearized operator at $0, H^{\prime}(0): E \rightarrow F$ is an isomorphism with inverse bounded by $C_{2}$.
\end{itemize}

If
$$s<\min \left(s_{0}, \frac{1}{2 C_{1} C_{2}}\right)$$
and
$$\|H(0)\|_{F}<\frac{s}{2 C_{2}},$$
Then there is a unique solution $x \in B_{E}(0, s)$ of the equation $H(x)=0$.
We end this section with the following existence theorem:
Theorem 11.4. Let $a=b$. Then for all a sufficiently small, there exist constants $\lambda_{1}, \lambda_{2} \in \mathbb{R}$ and $\theta \in \mathcal{D}$ satisyfying
$$\|\theta\|_{C_{\delta}^{4, \alpha}}<C a^{4+\delta-\epsilon}$$
so that
$$P_{g^{(1)}}(\theta)=\lambda_{1} k_{1}+\lambda_{2} k_{2} .$$
Proof. We denote the refined approximate metric by $g^{(1)}=g_{a}^{(1)}$, or by $g$ if the context is clear.

We will find a zero of $H$, so we need to verify the assumptions in Lemma 11.3 with $E=\mathbb{R} \times \mathbb{R} \times \mathcal{D}$ and $F=C_{\delta}^{0, \alpha}$, beginning with (1):

Lemma 11.5. The quadratic estimate (11.43) holds for $H: \mathbb{R} \times \mathbb{R} \times \mathcal{D} \rightarrow C_{\delta}^{0, \alpha}$.
Proof. This follows from Proposition 3.7, once we verify the assumptions (3.29) (the assumptions (3.28) clearly hold). We need to verify the estimate on each of the three regions: the asymptotically flat piece, the damage zone, and the compact piece. Recall that the weight is given by (9.16).

On the asymptotically flat piece, i.e., for $|x| \leq a^{-1}$,
$$g^{(1)}=g_{N}+a^{4} \tilde{H}_{2} .$$
Let $h_{1}=g^{(1)}-g_{N}=a^{4} \tilde{H}_{2}$, then using the formula (3.36) we have
$$R m_{g^{(1)}}=R m_{g_{N}}+\left(g^{(1)}\right)^{-1} * \nabla_{N}^{2} h_{1}+\left(g^{(1)}\right)^{-2} * \nabla_{N} h_{1} * \nabla h_{1} .$$
By Proposition 7.2 and the fact that $g_{N}$ is asymptotically flat of order 2,
$$\begin{aligned}
R m_{g^{(1)}} & =O\left(|x|^{-4}\right)+O\left(a^{4}\right)+O\left(a^{8}|x|^{2}\right) \\
& =O\left(|x|^{-4}\right)+O\left(a^{4}\right)
\end{aligned}$$
Since $w(x)=|x|$ for $|x| \gg 1$, it follows that
$$w(x)^{2}\left|R m_{g^{(1)}}\right| \leq C_{0} .$$
Similarly, using (3.37)
$$\nabla_{g^{(1)}} R m_{g^{(1)}}=O\left(|x|^{-5}\right)+O\left(a^{4}|x|^{-3}\right)+O\left(a^{4}|x|^{\epsilon-3}\right)+O\left(a^{8}|x|\right)+O\left(a^{12}|x|^{3}\right),$$
hence
$$w(x)^{3}\left|\nabla_{g^{(1)}} R m_{g^{(1)}}\right| \leq C_{1} .$$

Finally, (3.38)
$$\begin{aligned}
\nabla_{g^{(1)}}^{2} R m_{g^{(1)}} & =O\left(|x|^{-6}\right)+O\left(a^{4}|x|^{-4}\right)+O\left(a^{8}|x|^{-2}\right)+O\left(a^{4}|x|^{-4+\epsilon}\right) \\
& +O\left(a^{8}|x|^{\epsilon-2}\right)+O\left(a^{8}|x|^{2 \epsilon-4}\right)+O\left(a^{12}|x|^{2}\right)+O\left(a^{16}|x|^{4}\right) .
\end{aligned}$$
Therefore,
$$w(x)^{4}\left|\nabla_{g^{(1)}}^{2} R m_{g^{(1)}}\right| \leq C_{2} .$$

The estimates for the other regions are verified in a similar manner, so we omit the details. \(\square\)

It remains to show that
$$H^{\prime}: \mathbb{R} \times \mathbb{R} \times \mathcal{D} \rightarrow C_{\delta-4}^{0, \alpha}$$
is an isomorphism with bounded inverse. This will follow once we prove surjectivity; the bound on the inverse will then follow immediately from Proposition 11.2.

In the following, let us view $H^{\prime}$ as a map
$$H^{\prime}: \mathbb{R} \times \mathbb{R} \times C_{\delta}^{4, \alpha} \rightarrow C_{\delta-4}^{0, \alpha} .$$
Then the formal adjoint of $H^{\prime}$ maps from
$$\left(H^{\prime}\right)^{*}: C_{-\delta}^{4, \alpha} \rightarrow \mathbb{R} \times \mathbb{R} \times C_{-\delta-4}^{0, \alpha}$$
and is given by
$$\left(H^{\prime}\right)^{*}(h)=\left(\int\left\langle h, k_{1}\right\rangle d V, \int\left\langle h, k_{2}\right\rangle d V, S h\right)$$
since $S$ is self-adjoint (the duals of Hölder spaces are not Hölder spaces, but this slight abuse of notation should not cause confusion). We claim that for $a$ sufficiently small, $\operatorname{Ker}\left(\left(H^{\prime}\right)^{*}\right)=0$. To see this argue by contradiction: let $h_{i}$ be a sequence of kernel elements corresponding to a sequence $a_{i} \rightarrow 0$ as $i \rightarrow \infty$. Normalize $h_{i}$ so that $\left\|h_{i}\right\|_{C_{-\delta}^{4, \alpha}}=1$. We then have a sequence $h_{i}$ satisfying
$$\begin{aligned}
S h_{i}=0, \quad \int\left\langle h, k_{1}\right\rangle d V & =0, \quad \int\left\langle h, k_{2}\right\rangle d V=0 \\
\left\|h_{i}\right\|_{C_{-\delta}^{4, \alpha}} & =1
\end{aligned}$$
The limiting argument in the proof of Proposition 11.2 is then modified as follows. Let $p_{i}$ be a sequence of points in $X_{a_{i}, b_{i}}$ for a sequence $a_{i} \rightarrow 0$ as $i \rightarrow \infty$ at which the supremum in the norm (11.59) is attained. We have the three possibilities.
\begin{itemize}
\item[-] (1) $p_{i} \rightarrow p \in N$. In this case, standard elliptic estimates produce a nontrivial solution of the limiting equation $S h_{\infty}=0$ on $\left(N, g_{N}\right)$ with $h \in C_{-\delta}^{4, \alpha}$. By Theorem 5.1, $h_{\infty}=c_{1} \cdot o_{1}+c_{2} g_{N}$ for some $c_{1}, c_{2} \in \mathbb{R}$. Since
\end{itemize}
$$\int\left\langle h_{i}, k_{1}\right\rangle d V_{g_{a_{i}}^{(1)}}=0, \quad \int\left\langle h_{i}, k_{2}\right\rangle d V_{g_{a_{i}}^{(1)}}=0$$
\begin{itemize}
\item[] and $k_{1}, k_{2}$ both have compact support on $N$, and $h_{i} \leq C w^{-\delta}$, the integrand is bounded, which implies that
$$\int\left\langle h_{\infty}, k_{1}\right\rangle d V_{g_{N}}=0, \quad \int\left\langle h_{\infty}, k_{2}\right\rangle d V_{g_{N}}=0$$
which implies that $c_{1}=c_{2}=0$, a contradiction.
\item[-] (2) $p_{i} \rightarrow p \in Z \backslash\left\{z_{0}\right\}$. In this case, defined $\tilde{h}_{i}=\left(a_{i}\right)^{4+2 \delta} h_{i}$. It is easy to see that this scaling preserves the $C_{\delta}^{4, \alpha}$ norm, with respect to the metric $\tilde{g}_{a_{i}}^{(1)}=a^{4} g_{a_{i}}^{(1)}$. Standard elliptic estimates produce a nontrivial solution of the limiting equation $S \tilde{h}_{\infty}=0$ on $\left(Z, g_{Z}\right)$ with $h \in C_{-\delta}^{4, \alpha}$. By Theorem 4.1, $h_{\infty}=0$ which is a contradiction.
\item[-] (3) If neither of the above cases happen, then as above one can rescale both the metric and $h_{i}$ to find a solution $h_{\infty} \in C_{-\delta}^{4, \alpha}$ of the equation $S h_{\infty}=0$ on $\mathbb{R}^{4} \backslash\{0\}$ with weight function $w=r$. Since $0<-\delta<1, \delta$ is not an indicial root so $S: C_{\delta}^{4, \alpha} \rightarrow C_{\delta-4}^{0, \alpha}$ is an isomorphism, therefore $h_{\infty}=0$.
\end{itemize}
This contradiction proves that $\operatorname{Ker}\left(\left(H^{\prime}\right)^{*}\right)=\{0\}$, and by standard Fredholm Theory, we conclude that
$$H^{\prime}: \mathbb{R} \times \mathbb{R} \times C_{\delta}^{4, \alpha} \rightarrow C_{\delta-4}^{0, \alpha} .$$
is surjective.
Claim 11.6. For a sufficiently small, the dimension of the kernel of $H^{\prime}: \mathbb{R} \times \mathbb{R} \times$ $C_{\delta}^{4, \alpha} \rightarrow C_{\delta-4}^{0, \alpha}$ is at least 2.

Proof. To see this, we claim that $k_{1}$ and $k_{2}$ are not in the image of $S$. If, for example $S h_{i}=k_{1}$, then a limiting argument as above would produce a solution of $S\left(h_{\infty}\right)=k_{1}$ on $\left(N, g_{N}\right)$, which is a contradiction. Similarly, if $S h_{i}=k_{2}$, the same argument yields a contradiction. We have found 2 linearly independent elements not in the image of $S$; by Fredholm theory the cokernel of $S$ must be at least two-dimensional. Since $S$ is a self-adjoint operator, we must have $\operatorname{dim}(\operatorname{Ker}(S)) \geq 2$. Obviously $\{0\} \times\{0\} \times$ $\operatorname{Ker}(S) \subset \operatorname{Ker}\left(H^{\prime}\right)$, so the claim follows. \(\square\)

To finish, by standard $L^{2}$-decomposition
$$L^{2} \cap C_{\delta}^{4, \alpha}=\operatorname{span}\left\{k_{1}, k_{3}\right\} \oplus \mathcal{D},$$
where $\mathcal{D}=C_{\delta}^{4, \alpha} \cap\left(\operatorname{span}\left\{k_{1}, k_{3}\right\}\right)^{\perp}$. Let $h_{1}, h_{2}, \ldots h_{j}$ be a basis for $\operatorname{Ker}\left(H^{\prime}\right)$, where $j=\operatorname{dim}\left(\operatorname{Ker}\left(H^{\prime}\right)\right)$. Then we can write
$$h_{i}=c_{i 1} k_{1}+c_{i 2} k_{3}+m_{i},$$
where $m_{i} \in \mathcal{D}$. If $j>2$, then obviously we can take a nontrivial linear combination to obtain
$$\sum_{i} c_{i} h_{i}=\sum_{i} c_{i} m_{i}$$
for some constants $c_{i}$. The left hand side is in the kernel of $H^{\prime}$, but Proposition 11.2 shows that the left hand side cannot be, which is a contradiction. Consequently, from Claim 11.6 we conclude that $\operatorname{dim}\left(\operatorname{Ker}\left(H^{\prime}\right)\right)=2$. So we have the equations
$$\begin{aligned}
& h_{1}=c_{11} k_{1}+c_{12} k_{3}+m_{1} \\
& h_{2}=c_{21} k_{1}+c_{22} k_{3}+m_{2} .
\end{aligned}$$
The matrix of coefficients must be an invertible 2 × 2 matrix, since otherwise we could again find a nontrivial solution of (11.64). Consequently, we can solve
$$\begin{aligned}
& k_{1}=c_{11}^{\prime} h_{1}+c_{12}^{\prime} h_{2}+m_{1}^{\prime} \\
& k_{3}=c_{21}^{\prime} h_{1}+c_{22}^{\prime} h_{2}+m_{2}^{\prime} .
\end{aligned}$$
which, together with (11.62), proves the vector space decomposition
$$L^{2} \cap C_{\delta}^{4, \alpha}=\operatorname{Ker}\left(H^{\prime}\right) \oplus \mathcal{D} .$$
Clearly, this proves that $H^{\prime}: \mathbb{R} \times \mathbb{R} \times \mathcal{D} \rightarrow C_{\delta-4}^{0, \alpha}$ is also surjective.
Finally, the estimate on the size of $\theta$ follows from Proposition 10.6:
$$\begin{aligned}
\|H(0,0,0)\|_{C_{\delta-4}^{0, \alpha}} & =\|P(0)\|_{C_{\delta-4}^{0, \alpha}}=\left\|B^{t}\left(g_{a, b}^{(1)}\right)\right\|_{C_{\delta-4}^{0, \alpha}} \\
& \leq \lambda a^{4}\left\|k_{1}\right\|_{C_{\delta-4}^{0, \alpha}}+C a^{4+\delta-\epsilon} \leq C a^{4+\delta-\epsilon}
\end{aligned}$$ \(\square\)

\section*{12. Completion of proofs}

The following result immediately implies Theorem 1.1:
Theorem 12.1. Let $a=b$ and $\theta \in \mathcal{D}$ be the unique solution of (11.47):
$$P_{g^{(1)}}(\theta)=\lambda_{1} k_{1}+\lambda_{2} k_{2} .$$
Then
$$\lambda_{1}=\lambda a^{4}+O\left(a^{6-\epsilon}\right)$$
as $a \rightarrow 0$, where
$$\lambda=\left(\frac{2}{3} W\left(y_{0}\right) \circledast W\left(z_{0}\right)+4 t R\left(z_{0}\right) \operatorname{mass}\left(g_{N}\right)\right) \omega_{3} .$$
Proof. Let $\theta \in \mathcal{D}$ be a solution of (11.47):
$$P_{g^{(1)}}(\theta)=\lambda_{1} k_{1}+\lambda_{2} k_{2} .$$
Pairing both sides with $\eta o_{1}$, where $\eta$ is given in (11.7), and integrating (all with respect to the metric $g=g_{a}^{(1)}$ ) gives
$$\int\left\langle P(\theta), \eta o_{1}\right\rangle d V=\lambda_{1} \int\left\langle k_{1}, \eta o_{1}\right\rangle d V+\lambda_{2} \int\left\langle k_{2}, \eta o_{1}\right\rangle d V$$
The last integral is identically zero by (10.57), and by (10.43), we obtain
$$\lambda_{1}=\int\left\langle P(\theta), \eta o_{1}\right\rangle d V$$

Using Proposition 3.7 we expand $P(\theta)$ as
$$\begin{aligned}
P(\theta) & =P(0)+S(\theta)+Q(\theta) \\
& =B^{t}\left(g^{(1)}\right)+S(\theta)+Q(\theta) .
\end{aligned}$$
Substituting this into (12.4),
$$\lambda_{1}=\int\left\langle B^{t}\left(g^{(1)}\right), \eta o_{1}\right\rangle d V+\int\left\langle S(\theta), \eta o_{1}\right\rangle d V+\int\left\langle Q(\theta), \eta o_{1}\right\rangle d V$$
Using (11.24) (replacing $\tilde{h}_{i}$ with $\theta$ in that computation), we estimate
$$\int\left\langle S(\theta), \eta o_{1}\right\rangle d V=O\left(a^{2-\delta}\right) O\left(a^{4+\delta-\epsilon}\right)=O\left(a^{6-\epsilon}\right)$$
as $a \rightarrow 0$. The estimate (11.46) implies the pointwise estimates:
$$\left|\nabla^{m} \theta\right| \leq C a^{4+\delta-\epsilon} w^{\delta-m},$$
for $0 \leq m \leq 4$. Using Proposition 3.7, the nonlinear term in (12.5) is then estimated
$$\int\left\langle Q(\theta), \eta o_{1}\right\rangle d V=O\left(a^{8+2 \delta-2 \epsilon}\right)$$
We conclude
$$\lambda_{1}=\int\left\langle B^{t}\left(g^{(1)}\right), \eta o_{1}\right\rangle d V+O\left(a^{6-\epsilon}\right)$$
as $a \rightarrow 0$.
Notice that from (10.12),
$$\int_{D Z}\left\langle B^{t}\left(g^{(1)}\right), \eta o_{1}\right\rangle d V=O\left(a^{6-\epsilon}\right),$$
so we can rewrite (12.9) as
$$\lambda_{1}=\int_{B}\left\langle B^{t}\left(g^{(1)}\right), \eta o_{1}\right\rangle d V+O\left(a^{6-\epsilon}\right)$$
as $a \rightarrow 0$, where $B$ is the same as in (8.6).
On $B \subset N, \eta \equiv 1$, and from Proposition 10.4 we have
$$\begin{aligned}
\int_{B}\left\langle B^{t}\left(g^{(1)}\right), o_{1}\right\rangle d V= & \int_{B}\left\langle a^{4} \lambda k_{1}^{(0)}-a^{4} \mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}+O\left(a^{8}\right), o_{1}\right\rangle d V \\
= & a^{4} \lambda \int_{B}\left\langle k_{1}^{(0)}, o_{1}\right\rangle d V-a^{4} \int_{B}\left\langle\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}, o_{1}\right\rangle d V \\
& +\int_{B}\left\langle O\left(a^{8}\right), o_{1}\right\rangle d V
\end{aligned}$$

By Claim 10.8, the first integral in (12.12) is
$$\begin{aligned}
a^{4} \lambda \int_{B}\left\langle k_{1}^{(0)}, o_{1}\right\rangle d V & =a^{4} \lambda \int_{B}\left\langle\left(1+O\left(a^{2}\right)\right) k_{1}, o_{1}\right\rangle d V \\
& =a^{4} \lambda \int\left\langle k_{1}, o_{1}\right\rangle d V+O\left(a^{6}\right) \\
& =a^{4} \lambda+O\left(a^{6}\right)
\end{aligned}$$

To estimate the second integral in (12.12), we use the fact that on $B \subset N$,
$$g=g_{N}+O\left(a^{2}\right) .$$
In particular, for tensors $T_{1}, T_{2}$ we have
$$\begin{aligned}
\left\langle T_{1}, T_{2}\right\rangle & =\left(1+O\left(a^{2}\right)\right)\left\langle T_{1}, T_{2}\right\rangle_{g_{N}} \\
d V & =\left(1+O\left(a^{2}\right)\right) d V_{g_{N}}
\end{aligned}$$
Therefore,
$$\begin{aligned}
-a^{4} \int_{B} & \left\langle\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}, o_{1}\right\rangle d V \\
= & -a^{4} \int_{B}\left\langle\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}, o_{1}\right\rangle_{g_{N}} d V_{g_{N}} \\
& \quad+O\left(a^{6}\right) \int_{B}\left|\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}\right|_{g_{N}}\left|o_{1}\right|_{g_{N}} d V_{g_{N}}
\end{aligned}$$
For the second integral above on the right-hand side of (12.14), we note that
$$\left|\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}\right|_{g_{N}}=O\left(|x|^{\epsilon-4}\right),$$
see the proof of Proposition 10.4. Also, by Theorem 6.1, $o_{1}$ decays quadratically, hence
$$\int_{B}\left|\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}\right|_{g_{N}}\left|o_{1}\right|_{g_{N}} d V_{g_{N}}=O(1)$$

For the first integral on the right in (12.14) we recall from Theorems 5.1 and 6.1 that the trace-free part of $o_{1}$ is given by
$$\begin{aligned}
\mathcal{K}_{g_{N}} \omega_{1} & =\frac{2}{3} W_{i k j \ell}\left(y_{0}\right) \frac{x^{k} x^{\ell}}{|x|^{4}}+O\left(|x|^{-4+\epsilon}\right) \\
& =O\left(|x|^{-2}\right)
\end{aligned}$$
as $|x| \rightarrow \infty$. Moreover,
$$\square_{g_{N}} \omega_{1}=\delta_{g_{N}} \mathcal{K}_{g_{N}} \omega_{1}=0 .$$

Therefore, integration by parts gives
$$\begin{aligned}
-a^{4} \int_{B} & \left\langle\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}_{2}}, o_{1}\right\rangle_{g_{N}} d V_{g_{N}} \\
= & -a^{4} \int_{B}\left\langle\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}, \mathcal{K}_{g_{N}} \omega_{1}\right\rangle_{g_{N}} d V_{g_{N}} \\
= & 2 a^{4} \int_{B}\left\langle\delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}, \delta_{g_{N}} \mathcal{K}_{g_{N}} \omega_{1}\right\rangle_{g_{N}} d V_{g_{N}} \\
& -2 a^{4} \oint_{\partial B} \mathcal{K}_{g_{N}} \omega_{1}\left(N, \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}\right) d S \\
= & -2 a^{4} \oint_{\partial B} \mathcal{K}_{g_{N}} \omega_{1}\left(N, \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}\right) d S
\end{aligned}$$
Using (12.15), the integrand of the boundary integral above is
$$\left|\mathcal{K}_{g_{N}} \omega_{1}\left(N, \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}\right)\right|=O\left(|x|^{-2}\right) \cdot O\left(|x|^{\epsilon-3}\right)=O\left(|x|^{\epsilon-5}\right),$$
and it follows that the boundary integral in (12.17) is of the order
$$-2 a^{4} \oint_{\partial B} \mathcal{K}_{g_{N}} \omega_{1}\left(N, \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}\right) d S=O\left(a^{6-\epsilon}\right)$$
Consequently,
$$-a^{4} \int_{B}\left\langle\mathcal{K}_{g_{N}} \delta_{g_{N}} \mathcal{K}_{g_{N}} \delta_{g_{N}} \stackrel{\circ}{\tilde{H}}_{2}, o_{1}\right\rangle d V=O\left(a^{6-\epsilon}\right)$$

We can also use the fact that $o_{1}$ decays quadratically to estimate the last term in (12.12) as
$$\int_{B}\left\langle O\left(a^{8}\right), o_{1}\right\rangle d V=O\left(a^{6}\right)$$
Combining (12.12), (12.13), (12.18) , and (12.19) we obtain
$$\int_{B}\left\langle B^{t}\left(g^{(1)}\right), \eta o_{1}\right\rangle d V=\lambda a^{4}+O\left(a^{6-\epsilon}\right)$$
Proposition 8.1 then completes the proof. \(\square\)

Proof of Theorem 1.2. From Theorem 12.1, it is clear that for a sufficiently small, there are two possibilities. The first is that the remainder term in (12.1) is identically zero for all $a$ sufficiently small. Choosing $t_{0}$ as in (1.20), we have that $\lambda_{1}=0$. The second possibility is that the remainder term in (12.1) is not zero. In this case, by an application of the intermediate value theorem, we may perturb $t$ slightly to again conclude that $\lambda_{1}=0$. We now have a solution of the equation
$$P_{g^{(1)}}(\theta)=\lambda_{2} k_{2} .$$

Recalling the definition of $P$, this is
$$B^{t}\left(g^{(1)}+\theta\right)+\mathcal{K}_{g^{(1)}+\theta} \delta_{g^{(1)}} \mathcal{K}_{g^{(1)}} \delta_{g^{(1)}} \stackrel{\circ}{\theta}=\lambda_{2} k_{2} .$$
With respect to the metric $g^{(1)}+\theta$, the trace of the left hand side of this equation has mean value zero, so we have
$$0=\lambda_{2} \int t r_{g^{(1)}+\theta} k_{2} d V_{g^{(1)}+\theta}$$
Since $k_{2}$ has compact support in the region where the weight function is bounded, expanding the trace and volume element and using (12.7), we have
$$\left.0=\lambda_{2}\left(\int t r_{g^{(1)}} k_{2} d V_{g^{(1)}}+O\left(a^{4+\delta-\epsilon}\right)\right)\right)=\lambda_{2}\left(1+O\left(a^{4+\delta-\epsilon}\right)\right),$$
as $a \rightarrow 0$, by (10.56), which implies that $\lambda_{2}=0$. We have therefore found a solution of
$$P_{g^{(1)}}(\theta)=0,$$
which is a smooth $B^{t}$-flat metric from Proposition 3.5.
In the cases of multiple gluing points, imposing the bilateral, trilateral, or quadrilateral symmetries in the respective cases, reduces the argument to that of a single gluing point, so the argument is the same as above. \(\square\)

Proof of Theorem 1.4. In the Bach-flat case, we may restrict all above arguments to pointwise traceless tensors. The pure-trace kernel and cokernel elements are then not required in the Lyapunov-Schmidt reduction in Section 11. We then add a 1dimensional kernel parameter to the map $H$. That is, we let
$$\mathcal{D}=\left\{h \in C_{\delta}^{4, \alpha}: \int\left\langle h, k_{1}\right\rangle=0\right\} .$$
where $k_{1}$ is of compact support chosen to pair non-trivially with $\stackrel{\circ}{o}_{1}$, and define the mapping $H: \mathbb{R} \times \mathbb{R} \times \mathcal{D} \rightarrow C_{\delta-4}^{\alpha}$ by
$$H\left(s, \lambda_{1}, \theta\right)=P_{g^{(1)}}\left(\theta+s \eta \stackrel{\circ}{O}_{1}\right)-\lambda_{1} k_{1} .$$
For gluing parameter $a$ sufficiently small, the Kuranishi map is then the map
$$\Psi: s \mapsto \lambda_{1}(s)$$
Using the gauging argument from [GV11, Section 2.3], the fixed point argument in Section 11 is easily extended to show that any equivariant Bach-flat metric in a sufficiently small $C^{4, \alpha}$-neighborhood of the approximate metric will correspond to a zero of $\Psi$ for some $s$. If $W\left(y_{0}\right) \circledast W\left(z_{0}\right) \neq 0$, then the leading term of $\Psi$ is non-zero, so obviously there can be no equivariant Bach-flat metric in a sufficiently small $C^{4, \alpha}$ neighborhood of the approximate metric. \(\square\)
12.1. Computation of values in Table 1.1. Assume $W^{ \pm}, \widetilde{W}^{ \pm}$are trace-free endomorphisms of $\Lambda_{2}^{ \pm}\left(V^{*}\right)$, where $V$ is a real, oriented, four-dimensional inner product space, and write
$$\begin{aligned}
& W=W^{+}+W^{-}: \Lambda^{2}\left(V^{*}\right) \rightarrow \Lambda^{2}\left(V^{*}\right), \\
& \widetilde{W}=\widetilde{W}^{+}+\widetilde{W}^{-}: \Lambda^{2}\left(V^{*}\right) \rightarrow \Lambda^{2}\left(V^{*}\right) .
\end{aligned}$$
Assume further that $W$ and $\widetilde{W}$ can be simultaneously diagonalized: that is, there is an orthogonal basis of eigenvectors (two-forms) for $W$ and $\widetilde{W}$ denoted
$$\omega, \eta, \theta, \omega^{-}, \eta^{-}, \theta^{-},$$
where the first three are a basis of $\Lambda_{2}^{+}\left(V^{*}\right)$ and the last three a basis of $\Lambda_{2}^{-}\left(V^{*}\right)$. Denote the eigenvalues of $W$ and $\widetilde{W}$ as
$$\begin{aligned}
& \operatorname{spec}(W)=\left\{\lambda, \mu, \nu, \lambda^{-}, \mu^{-}, \nu^{-}\right\}, \\
& \operatorname{spec}(\widetilde{W})=\left\{\tilde{\lambda}, \tilde{\mu}, \tilde{\nu}, \tilde{\lambda}^{-}, \tilde{\mu}^{-}, \tilde{\nu}^{-}\right\} .
\end{aligned}$$
We will further assume that $W^{ \pm}$and $\widetilde{W}^{ \pm}$are trace-free; i.e.,
$$\begin{aligned}
& \lambda+\mu+\nu=0, \quad \lambda^{-}+\mu^{-}+\nu^{-}=0, \\
& \tilde{\lambda}+\tilde{\mu}+\tilde{\nu}=0, \quad \tilde{\lambda}^{-}+\tilde{\mu}^{-}+\tilde{\nu}^{-}=0 .
\end{aligned}$$
Using this basis in (12.29) we can write
$$\begin{aligned}
W= & \frac{1}{2}\{\lambda \omega \otimes \omega+\mu \eta \otimes \eta+\nu \theta \otimes \theta \\
& \left.+\lambda^{-} \omega^{-} \otimes \omega^{-}+\mu^{-} \eta^{-} \otimes \eta^{-}+\nu^{-} \theta^{-} \otimes \theta^{-}\right\}, \\
\widetilde{W}= & \frac{1}{2}\{\tilde{\lambda} \omega \otimes \omega+\tilde{\mu} \eta \otimes \eta+\tilde{\nu} \theta \otimes \theta \\
& \left.+\tilde{\lambda}^{-} \omega^{-} \otimes \omega^{-}+\tilde{\mu}^{-} \eta^{-} \otimes \eta^{-}+\tilde{\nu}^{-} \theta^{-} \otimes \theta^{-}\right\} .
\end{aligned}$$

We normalize the eigenforms to have length $\sqrt{2}$; this convention gives the identities
$$\omega^{2}=\eta^{2}=\cdots=\left(\theta^{-}\right)^{2}=I d .$$

We also point out two more important algebraic facts: first, the product of any SD basis element with any ASD basis element gives a symmetric trace-free two-tensor, whose square is the identity. Thus, for example,
$$h=\omega \omega^{-} \Rightarrow \operatorname{tr} h=0, h^{2}=I d,|h|^{2}=4 .$$
Also, the bases of $\Lambda_{2}^{ \pm}$give a quaternionic structure satisfying the following multiplication rules:
$$\omega \eta=\theta, \eta \theta=\omega, \theta \omega=\eta .$$