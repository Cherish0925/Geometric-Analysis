---
retention_scope: session
part: 5
total_parts: 7
---

[Part 5/7 of: Sobolev-classasymptoticallyhyperbolicmanifolds and]

The mapping property of $Q_{r}$ follows from the fact that $\delta \in \mathcal{D}_{q}(R)$ and therefore by Theorem B. $3 \breve{\mathcal{P}}: H_{\delta}^{\sigma, q}(\mathbb{H}) \rightarrow H_{\delta}^{\sigma-d, q}(\mathbb{H})$ is an isomorphism. This fact also implies the mapping property for $S_{r}$. To verify the mapping property for $T_{r}$, note that Lemma 8.4 implies $\left[\varphi_{j}, \mathcal{P}\right]: H_{\delta-1}^{\sigma, q}(M) \rightarrow H_{\delta}^{\sigma-d+1, q}(M)$.
To verify the identity (9.1) first note that, analogous to the proof of Proposition 8.16, the cutoff functions $\eta_{\hat{p}_{j}, r}$ appearing in (8.16) satisfy $\eta_{\hat{p}_{j}, r} \varphi_{j}=\varphi_{j}$. The identity then follows by direct computation, noting that $\sum_{j \geq 1} \varphi_{j}^{2}=1$ on $A_{r / 4}$.
It remains to establish the estimate (9.2). For each Möbius parametrization $\Phi_{i}$, let $\mathcal{N}(i)$ be the set of indices $j$ such that the support of $\varphi_{j}$ intersects the image of $\Phi_{i}$. Using the uniform bound to the size of $\mathcal{N}(i)$ from Lemma 8.13 we find
$$\left\|\Phi_{i}^{*} S_{r} u\right\|_{H^{\sigma, q}\left(B_{2}^{\mathbb{H}}\right)}^{q} \lesssim \sum_{j \in \mathcal{N}(i)}\left\|\Phi_{i}^{*} S_{j, r}\left(\varphi_{j} u\right)\right\|_{H^{\sigma, q}\left(B_{2}^{\mathbb{H}}\right)}^{q},$$
where $S_{j, r}=\varphi_{j} \Xi_{j}^{-1} \breve{\mathcal{P}}^{-1} \Xi_{j}\left(\mathcal{P}_{j}-\breve{\mathcal{P}}_{j}\right)$. After multiplying by $\rho_{i}^{-\delta q}$ and summing over $i$ we obtain
$$\left\|S_{r} u\right\|_{H_{\delta}^{\sigma, q}(M)}^{q} \lesssim \sum_{i} \sum_{j \in \mathcal{N}(i)} \rho_{i}^{-\delta q}\left\|\Phi_{i}^{*} S_{j, r}\left(\varphi_{j} u\right)\right\|_{H^{\sigma, q}\left(B_{2}^{\mathbb{H}}\right)}^{q} \lesssim \sum_{j}\left\|S_{j, r}\left(\varphi_{j} u\right)\right\|_{H_{\delta}^{\sigma, q}(M)}^{q} .$$
Lemmas 8.15 and 8.10 imply
$$\left\|S_{j, r}\left(\varphi_{j} u\right)\right\|_{H_{\delta}^{\sigma, q}(M)}^{q} \lesssim r^{\alpha q} \sum_{j}\left\|\varphi_{j} u\right\|_{H_{\delta}^{\sigma, q}(M)}^{q} .$$
Let $\mathcal{N}^{*}(j)$ be the set of indices $i$ such that the support of $\varphi_{j}$ intersects the image of $\Phi_{i}$. Then
$$\begin{aligned}
\sum_{j}\left\|\varphi_{j} u\right\|_{H_{\delta}^{\sigma, q}(M)}^{q} & =\sum_{j} \sum_{i \in \mathcal{N}^{*}(j)} \rho_{i}^{-\delta q}\left\|\Phi_{i}^{*}\left(\varphi_{j} u\right)\right\|_{H^{\sigma, q}\left(B_{2}^{\mathbb{H}}\right)}^{q} \\
& =\sum_{i} \sum_{j \in \mathcal{N}(i)} \rho_{i}^{-\delta q}\left\|\Phi_{i}^{*}\left(\varphi_{j} u\right)\right\|_{H^{\sigma, q}\left(B_{2}^{\mathbb{H}}\right)}^{q} .
\end{aligned}$$
From the uniform bound on the size of each $\mathcal{N}(i)$ and uniform control on the smooth functions $\varphi_{j}$ we conclude
$$\sum_{j}\left\|\varphi_{j} u\right\|_{H_{\delta}^{\sigma, q}(M)}^{q} \lesssim\|u\|_{H_{\delta}^{\sigma, q}(M)}^{q},$$
where, critically, the implicit constant is independent of the fineness $r$ and the associated number of terms on the left-hand side of this inequality. The desired estimate (9.2) now follows from inequalities (9.3) and (9.4). \(\square\)

Estimate (9.2) implies that for a fixed $(\sigma, q) \in S_{d}^{s, p}$ the map id $+S_{r}$ is invertible when $r$ is sufficiently small and we define
$$\widetilde{Q}_{r}=\left(\mathrm{id}+S_{r}\right)^{-1} \circ Q_{r} \quad \text { and } \quad \widetilde{T}_{r}=\left(\mathrm{id}+S_{r}\right)^{-1} \circ T_{r} .$$
Proposition 9.1 immediately implies the following.
Corollary 9.2.
\begin{itemize}
\item[(a)] Suppose $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta, \delta^{\prime} \in \mathcal{D}_{q}(R)$ with $\delta^{\prime} \leq \delta+1$ and that $r$ is sufficiently small that $\left(\mathrm{id}+S_{r}\right)^{-1}$ is well defined on $H_{\delta}^{\sigma, q}(M ; E)$ and on $H_{\delta^{\prime}}^{\sigma, q}(M ; E)$. The operators
$$\begin{aligned}
& \widetilde{Q}_{r}: H_{\delta}^{\sigma-d, q}(M ; E) \rightarrow H_{\delta}^{\sigma, q}(M ; E), \\
& \widetilde{T}_{r}: H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta^{\prime}}^{\sigma+1, q}(M ; E)
\end{aligned}$$
are bounded. Moreover, for all $u \in H_{\delta}^{\sigma, q}(M ; E)$ having support in $A_{r / 4}$
$$\widetilde{Q}_{r} \mathcal{P} u=u+\widetilde{T}_{r} u .$$
\item[(b)] The same statement is true replacing weighted Sobolev spaces $H$ with Gicquaud-Sakovich spaces $X$ having the same parameters, and replacing the weight range $\mathcal{D}_{q}(R)$ with $\mathcal{D}_{\infty}(R)$.
\end{itemize}
9.2. Fredholm theorem for weighted Sobolev spaces. The argument that $\mathcal{P}$ is Fredholm on general spaces relies on two key facts. First, $\mathcal{P}$ is Fredholm when acting on the $L^{2}$-based space $H_{0}^{d / 2,2}(M ; E)$, and second, that its kernel is independent of the space that it is acting on. This second fact relies on elliptic regularity up to the boundary at infinity accounting for the weight $\delta$. As a first step toward the Fredholm theorem, we establish smoothing properties of $\widetilde{T}_{r}$.

Lemma 9.3. Suppose $u \in H_{\delta_{0}}^{\sigma_{0}, q_{0}}(M ; E)$ for some $\left(\sigma_{0}, q_{0}\right) \in \mathcal{S}_{d}^{s, p}$ and $\delta_{0} \in \mathcal{D}_{q_{0}}(R)$. Given $(\sigma, q)$ in $\mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$, there exists $\ell \in \mathbb{N}$ such that $\widetilde{T}_{r}^{\ell}(u) \in H_{\delta}^{\sigma, q}(M ; E)$ so long as $r$ is sufficiently small.
The same statement is true, for the same values of $r$, replacing $\widetilde{T}_{r}$ with $\eta \widetilde{T}_{r}$ for any $\eta \in$ $C^{\infty}(\bar{M} ; \mathbb{R})$.

Proof. We prove the result assuming $\eta \equiv 1$; because multiplying by $\eta$ does not alter the mapping properties of $\widetilde{T}_{r}$, there is no change to the proof in the general case. The proof is accomplished by applying $\widetilde{T}_{r}$ to a finite sequence of spaces and we need to ensure that $r$ is small enough that $\widetilde{T}_{r}$ is well defined on all of them. After an initial reading, one verifies that the sequence of spaces is independent of $r$, and we are therefore free to assume $r$ is small enough that $\widetilde{T}_{r}$ can be applied to all of them.

The idea of the proof is that the operator $\widetilde{T}_{r}$ improves both the Sobolev indices and the weight, but that these improvements are constrained both by the condition that the Sobolev indices be in $\mathcal{S}_{d}^{s, p}$ and by the condition that the weight be in $\mathcal{D}_{q}(R)$, which changes depending on the Lebesgue parameter $q$. We navigate these restrictions by combining the use of $\widetilde{T}_{r}$ with the basic inclusion of Lemma 3.2, which allows one to 'trade' weight for Lebesgue parameter, and with using the Sobolev embedding of Proposition 3.3, which allows one to 'trade' differentiability for Lebesgue parameter. To facilitate our argument we introduce the following notation: for any $t \in(1, \infty)$, let $\sigma_{t}=\sup \left\{\sigma:(\sigma, t) \in \mathcal{S}_{d}^{s, p}\right\}$ and let
$$\delta_{t}=\sup \mathcal{D}_{t}(R)=R+\frac{n-1}{2}-\frac{n-1}{t} .$$
We first address the case where $q \geq q_{0}$. Noting that $\delta_{q_{0}}-R \in \mathcal{D}_{q_{0}}(R)$, the mapping property (9.6) implies we can apply $\widetilde{T}_{r}$ a finite number of times to $u$ to arrive at some $\hat{u} \in H_{\delta_{q_{0}}-R}^{\sigma_{q_{0}}+1, q_{0}}(M ; E)$. Now fix $t$ to satisfy
$$\frac{1}{t}=\max \left(\frac{1}{q}, \frac{1}{q_{0}}-\frac{1}{n}, \frac{1}{q_{0}}-\frac{R / 2}{n-1}\right) .$$
Sobolev embedding implies $\hat{u} \in H_{\delta_{0}-R / 2}^{\sigma_{q}, t}(M)$. Moreover, since $t \geq q$, one readily verifies that $\sigma_{q} \geq \sigma_{t}$, see Figure 2, and therefore $\hat{u} \in H_{\delta_{q_{0}}-R / 2}^{\sigma_{t}, t}(M)$ as well.
We claim that $\delta_{q_{0}}-R \in \mathcal{D}_{t}(R)$. Indeed, by construction
$$-\frac{R}{2} \leq \frac{n-1}{t}-\frac{n-1}{q_{0}} \leq 0$$
and hence
$$\delta_{q_{0}}-R+\frac{n-1}{t}-\frac{n-1}{2}=\frac{n-1}{t}-\frac{n-1}{q} \in[-R / 2,0] .$$
Thus $\delta_{q_{0}}-R \in \mathcal{D}_{t}(R)$ as claimed.
We have shown that we can apply $\widetilde{T}_{r}$ to $u$ finitely many times to obtain an element in $H_{\delta^{*}}^{\sigma_{t}, t}(M)$ for some $\delta^{*} \in \mathcal{D}_{t}(R)$ where either $t=q$ or $1 / t$ is a decrease of $1 / q_{0}$ by $\min \left(\frac{1}{n}, \frac{R / 2}{n-1}\right)$. Repeating this argument finitely many times we obtain an element of $H_{\delta^{*}}^{s_{q}, q}(M)$, and therefore also of $H_{\delta^{*}}^{\sigma, q}(M)$, for some $\delta^{*} \in \mathcal{D}_{q}(R)$. Finally, if needed, we can apply $\widetilde{T}_{r}$ finitely many more times to improve the weight and obtain an element in $H_{\delta}^{\sigma, q}(M)$ as required.
Now consider the case $q<q_{0}$ and let $\delta^{\prime}=\frac{n-1}{2}-\frac{n-1}{q_{0}} \in \mathcal{D}_{q_{0}}(R)$. We can apply $\widetilde{T}_{r}$ finitely many times to $u$ to obtain some $\hat{u} \in H_{\delta^{\prime}}^{s_{q_{0}}+1, q_{0}}(M)$. Now fix $t$ to satisfy
$$\frac{1}{t}=\min \left(\frac{1}{q}, \frac{1}{q_{0}}+\frac{1}{n}\right) .$$
Since $q_{0}>t$ and since $\delta^{\prime} \in \mathcal{D}_{q_{0}}(R)$ there exists $\delta^{*} \in \mathcal{D}_{t}(R)$ such that $\delta^{*}<\delta^{\prime}$. Moreover, since $1 / t \leq 1 / q_{0}+1 / n$, a computation shows $s_{t} \leq s_{q_{0}}+1$ and Lemma 3.2 implies $\hat{u} \in$
$H_{\delta^{*}}^{\sigma_{t}, t}(M)$. That is, we have shown we can apply $\widetilde{T}_{r}$ to $u$ finitely many times to arrive in $H_{\delta^{*}}^{\sigma_{t}, t}(M)$ where $\delta^{*} \in \mathcal{D}_{t}(R)$ and where either $t=q$ or $1 / t$ is an increase of $1 / q_{0}$ by $1 / n$. Repeating this argument finitely many times we can arrive in $H_{\delta^{*}}^{\sigma_{q}, q}(M)$ for some $\delta^{*} \in \mathcal{D}_{q}(R)$ and the argument is now finished as in the case when $q_{0} \leq q$. \(\square\)

Lemma 9.3 implies the desired regularity up to the boundary at infinity, at least for functions supported sufficiently near it.

Corollary 9.4. Suppose $u \in H_{\delta_{0}}^{\sigma_{0}, q_{0}}(M ; E)$ for some $\left(\sigma_{0}, q_{0}\right) \in \mathcal{S}_{d}^{s, p}$ and $\delta_{0} \in \mathcal{D}_{q_{0}}(R)$. If $\mathcal{P} u \in H_{\delta}^{\sigma-d, q}(M ; E)$ for some $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$, and if $u$ is supported in some $A_{r}$ with $r$ sufficiently small, then $u \in H_{\delta}^{\sigma, q}(M ; E)$.

Proof. Take $r$ small enough so that the conclusions of Lemma 9.3 and Corollary 9.2 hold for the given choice of parameters $\sigma_{0}, q_{0}$, etc. Let $\eta$ be a smooth function on $\bar{M}$ that equals 1 on $A_{r / 8}$ and vanishes outside $A_{r / 4}$.
We assume that $u$ is supported in $A_{r / 8}$ and that $\mathcal{P} u \in H_{\delta}^{\sigma, q}(M)$. Since $\eta$ is supported in $A_{r / 4}$ equation (9.7) implies
$$\left(-\eta \widetilde{T}_{r}\right)^{k} u=\left(\eta\left(\mathrm{id}-\widetilde{Q}_{r} \mathcal{P}\right)\right)^{k} u$$
for any $k \in \mathbb{N}$, and in particular for the value $k=\ell$ from Lemma 9.3. Note that both $\widetilde{Q}_{r} \mathcal{P}$ and multiplication by $\eta$ map $H_{\delta}^{\sigma, q}(M) \rightarrow H_{\delta}^{\sigma, q}(M)$. Thus expanding (9.8), and using $\eta u=u$, it follows from $\left(-\eta \widetilde{T}_{r}\right)^{\ell} u \in H_{\delta}^{\sigma, q}(M)$ and $\widetilde{Q}_{r} \mathcal{P} u \in H_{\delta}^{\sigma, q}(M)$ that $u \in H_{\delta}^{\sigma, q}(M)$. \(\square\)

Corollary 9.4, and interior elliptic regularity estimates, imply the following regularity result for $\mathcal{P}$.

Proposition 9.5. Suppose $u \in H_{\delta_{0}}^{\sigma_{0}, q_{0}}(M ; E)$ for some $\left(\sigma_{0}, q_{0}\right) \in \mathcal{S}_{d}^{s, p}$ and $\delta_{0} \in \mathcal{D}_{q_{0}}(R)$. If $\mathcal{P} u \in H_{\delta}^{\sigma-d, q}(M ; E)$ for some $\delta \in \mathcal{D}_{q}(R)$ then $u \in H_{\delta}^{\sigma, q}(M ; E)$.

Proof. Using Lemma 3.2 if $q_{0} \geq p^{*}$, or Proposition 3.3 if $q_{0}<p^{*}$, we see that $u \in$ $H_{\text {loc }}^{d-s, p^{*}}(M)$. Thus Proposition 8.3 implies $u \in H_{\text {loc }}^{\sigma, q}(M)$.
Select $r$ sufficiently small so that the conclusion of Corollary 9.4 holds and let $\eta$ be a smooth function on $\bar{M}$ that equals 1 in a neighborhood of $\partial M$ and that vanishes outside $A_{r}$. Since $[\mathcal{P}, \eta] u$ is supported in the complement of the region where $\eta=1$, Lemma 8.4 implies that $[\mathcal{P}, \eta] u \in H_{\delta}^{\sigma-d+1, q}(M)$. By hypothesis, $\eta \mathcal{P} u \in H_{\delta}^{\sigma-d, q}(M)$ and thus $\mathcal{P}(\eta u) \in H_{\delta}^{\sigma-d, q}(M)$. Corollary 9.4 thus implies $\eta u \in H_{\delta}^{\sigma, q}(M)$.
The interior regularity $u \in H_{\text {loc }}^{\sigma, q}(M)$ implies $(1-\eta) u \in H_{\delta}^{\sigma, q}(M)$, from which the desired result follows. \(\square\)

Having established the needed elliptic estimates of Proposition 9.5, we proceed to show that $\mathcal{P}$ is Fredholm using $L^{2}$ argument. Recall that Assumption P implies that $(\sigma, q)=$ $(d / 2,2)$ lies in $\mathcal{S}_{d}^{s, p}$ and implies that $0 \in \mathcal{D}_{2}(R)$, since $R>0$. Let $Z$ be the kernel of
$\mathcal{P}: H_{0}^{d / 2,2}(M ; E) \rightarrow H_{0}^{-d / 2,2}(M ; E)$. Proposition 9.5 implies $Z$ is the common kernel of $\mathcal{P}: H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma-d, q}(M ; E)$ for all $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$. Furthermore, Proposition 8.16 implies that $Z$ is finite dimensional, and that the image of $\mathcal{P}$ in each $H_{\delta}^{\sigma-d, q}(M ; E)$ is closed.
For a section $v \in Z$ and for a smooth compactly supported section $w$ of $E$ define
$$L_{v}(w)=\langle v, w\rangle_{(M, g)}=\int_{M}\langle v, w\rangle_{g} d V_{g} .$$

Lemma 9.6. Suppose $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$. For each $v \in Z, L_{v}$ extends to a continuous linear functional on $H_{\delta}^{\sigma-d, q}(M ; E)$ for each $\delta \in \mathcal{D}_{q}(R)$ and on $X_{\delta}^{\sigma-d, q}(M ; E)$ for each $\delta \in \mathcal{D}_{\infty}(R)$.

Proof. Let $v \in Z$. A computation shows that $\mathcal{S}_{d}^{s, p}$ is invariant under the transformation $(\sigma, q) \mapsto\left(d-\sigma, q^{*}\right)$, and that $\delta \in \mathcal{D}_{q}(R)$ if and only if $-\delta \in \mathcal{D}_{q^{*}}(R)$. Thus $v \in Z$ is an element of $H_{-\delta}^{d-\sigma, q^{*}}(M)$. Continuity of $L_{v}$ now follows from Proposition 3.18.
Note that if $\delta \in \mathcal{D}_{\infty}(R)$ then $\delta-\frac{n-1}{q}-\varepsilon \in \mathcal{D}_{q}(R)$ for $\varepsilon$ sufficiently small. Thus the continuity of $L_{v}$ on $X_{\delta}^{\sigma-d, q}(M)$, where $\delta \in \mathcal{D}_{\infty}(R)$, follows from the embedding $X_{\delta}^{\sigma-d, q}(M) \hookrightarrow H_{\delta-(n-1) / q-\varepsilon}^{\sigma-d, q}(M)$ provided by Lemma 3.2. \(\square\)

Theorem 9.7. Suppose $g$ is an asymptotically hyperbolic metric of either class (1.3) or class (1.4). Let $\mathcal{P}=\mathcal{P}[g]$ be a $d^{\text {th }}$-order elliptic operator satisfying Assumptions $P$ and $I$. Set $Z=\operatorname{ker}\left(\mathcal{P}: H_{0}^{d / 2,2}(M ; E) \rightarrow H_{0}^{-d / 2,2}(M ; E)\right)$.
Let $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$. Given $f \in H_{\delta}^{\sigma-d, q}(M ; E)$, there exists $u \in H_{\delta}^{\sigma, q}(M ; E)$ solving $\mathcal{P} u=f$ if and only if $L_{v}(f)=0$ for all $v \in Z$. In particular,
$$\mathcal{P}: H_{\delta}^{\sigma, q}(M ; E) \rightarrow H_{\delta}^{\sigma-d, q}(M ; E)$$
is Fredholm with index zero.
Proof. Let $Y \subset H_{\delta}^{\sigma-d, q}(M ; E)$ be the image of $\mathcal{P}$ acting on $H_{\delta}^{\sigma, q}(M ; E)$. Since $Y$ is closed by Proposition 8.16, it is the intersection of the kernels of all continuous linear functionals on $H_{\delta}^{\sigma-d, q}(M)$ vanishing on $Y$. We establish the theorem by showing that such linear functionals aisely those the form $L_{v}$ for some $v \in Z$.

First, a density argument and the self-adjointedness of $\mathcal{P}$ implies that if $v \in Z$, and if $f=\mathcal{P} u$ for some $u \in H_{\delta}^{\sigma, q}(M)$, then
$$L_{v}(f)=\langle v, \mathcal{P} u\rangle_{(M, g)}=\langle\mathcal{P} v, u\rangle_{(M, g)}=0 .$$
Thus the functionals $L_{v}$ indeed all vanish on $Y$.
Conversely, suppose $F \in\left(H_{\delta}^{\sigma-d, q}(M ; E)\right)^{*}$ vanishes on $Y$. Proposition 3.18 implies there exists $v \in H_{-\delta}^{d-\sigma, q^{*}}(M ; E)$ such that
$$F(\cdot)=\langle\nu, \cdot\rangle_{(M, g)} .$$

Since $F$ vanishes on $Y$ it follows that $\langle v, \mathcal{P} u\rangle_{g}=0$ for all sufficiently smooth, compactly supported $u$ and we conclude, again from self-adjointedness, that $\mathcal{P} v=0$ in the sense of distributions. As $\mathcal{S}_{d}^{s, p}$ is invariant under $\sigma \rightarrow d-\sigma$ and $q \rightarrow q^{*}$, and since $\delta \in \mathcal{D}_{q}(R)$ if and only if $-\delta \in \mathcal{D}_{q^{*}}(R)$, we conclude $\left(d-\sigma, q^{*}\right) \in \mathcal{S}_{d}^{s, p}$ and $-\delta \in \mathcal{D}_{q^{*}}(R)$. Thus $v$ is in the kernel of $\mathcal{P}$ acting on $H_{-\delta}^{d-\sigma, q^{*}}(M)$. Hence $v \in Z$ and $F=L_{v}$. \(\square\)
9.3. Fredholm theorem for Gicquaud-Sakovich spaces. Our approach to establishing Fredholm theorems for operators acting in Gicquaud-Sakovich spaces is to initially solve in some weighted Sobolev space $H_{\delta^{\prime}}^{\sigma, q}(M ; E)$ and then show via a bootstrap that the solution in fact lies in the desired Gicquaud-Sakovich space $X_{\delta}^{\sigma, q}(M ; E)$. The bootstrap relies on the fact some of the weighted Sobolev spaces are, in fact, also Gicquaud-Sakovich spaces on which $\mathcal{P}$ has good mapping properties. For a low regularity metric, however, the parameters $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$ may be so limited that this overlap does not occur. Presumably this difficulty could be overcome by introducing a scale of spaces that transition continuously between $H_{\delta}^{s, p}(M ; E)$ and $X_{\delta}^{s, p}(M ; E)$. We overcome this obstacle instead by first assuming additional regularity from the metric, namely that $s \geq d$, and then using an index-theoretic argument.

Lemma 9.8. Assume that $s \geq d$.
If $u \in H_{\delta_{0}}^{\sigma_{0}, q_{0}}(M ; E)$ for some $\left(\sigma_{0}, q_{0}\right) \in \mathcal{S}_{d}^{s, p}$ and $\delta_{0} \in \mathcal{D}_{q_{0}}(R)$, then for each $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{\infty}(R)$ there exists $\ell \in \mathbb{N}$ such that $\widetilde{T}_{r}^{\ell}(u) \in X_{\delta}^{\sigma, q}(M ; E)$ so long as $r$ is sufficiently small. The same statement for the same values of $r$ is true replacing $\widetilde{T}_{r}$ with $\eta \widetilde{T}_{r}$ for any $\eta \in C^{\infty}(\bar{M} ; \mathbb{R})$.

Proof. As in the proof of Lemma 9.3 we can assume $\eta \equiv 1$ and that $r$ is small enough that $\widetilde{T}_{r}$ is well-defined on the finitely many spaces visited in the bootstrap.
Since $\delta \in \mathcal{D}_{\infty}(R)$, we can find $\widetilde{q} \in(1, \infty)$ sufficiently large such that $\delta \in \mathcal{D}_{\widetilde{q}}(R)$. Increasing $\widetilde{q}$ if needed we can assume that $\widetilde{q}>p$. Now pick $\widetilde{\sigma} \in \mathbb{R}$ according to
$$\frac{1}{\widetilde{q}}-\frac{\widetilde{\sigma}}{n}=\frac{1}{p}-\frac{s}{n} .$$
We claim that $(\widetilde{\sigma}, \widetilde{q}) \in \mathcal{S}_{d}^{s, p}$, which involves verifying conditions (8.2). First, since $\widetilde{q}>p$ and since $1 / p-s / n<0$, we conclude from equation (9.10) that $s>\widetilde{\sigma}>0$. Since $s \geq d$ we conclude $\widetilde{\sigma} \in[d-s, s]$ which is the first of the conditions (8.2). The second condition follows from equation (9.10) and the fact that the weak $L^{2}$ condition ensures $1 / p-s / n<1 / p^{*}-(d-s) / n$.
Since $(\widetilde{\sigma}, \widetilde{q}) \in \mathcal{S}_{d}^{s, p}$ and since $\delta \in \mathcal{D}_{\widetilde{q}}(R)$, Lemma 9.3 implies there exists $\ell \in \mathbb{N}$ such that
$$\widetilde{T}_{r}^{\ell} u \in H_{\delta}^{\widetilde{\sigma}, \widetilde{q}}(M ; E) \subset X_{\delta}^{\widetilde{\sigma}, \widetilde{q}}(M ; E) .$$
The bootstrap from here to $X_{\delta}^{\sigma, q}(M ; E)$ now follows the procedure of Lemma 9.3, using the Giquaud-Sakovich variation of Corollary 9.2 for the smoothing properties of $\widetilde{T}_{r}$. The
argument is indeed somewhat simpler because there is no need to further adjust $\delta$ now that it is set to its target value. \(\square\)

The following variation of Proposition 9.5 now follows from Lemma 9.8 using identical arguments now based on the Gicquaud-Sakovich variation of Corollary 9.2. Note that we still assume additional regularity of the metric.

Proposition 9.9. Assume that $s \geq d$.
Suppose $u \in H_{\hat{\delta}}^{\hat{\sigma}, \hat{q}}(M ; E)$ for some $(\hat{\sigma}, \hat{q}) \in \mathcal{S}_{d}^{s, p}$ and some $\hat{\delta} \in \mathcal{D}_{\hat{q}}(R)$. If $\mathcal{P} u \in$ $X_{\delta}^{\sigma-d, q}(M ; E)$ for some $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{\infty}(R)$, then $u \in X_{\delta}^{\sigma, q}(M ; E)$.

We now establish the main Fredholm theorem for operators acting on Gicquaud-Sakovich spaces. For regular metrics, meaning those for which $s \geq d$, we use Theorem 9.7, along with Proposition 9.9, to refine the mapping properties of $\mathcal{P}$. For metrics with regularity involving $s<d$, the proof below relies on the we use an index theory argument as follows. Given an asymptotically hyperbolic metric $g$ of class $\mathscr{H}^{s, p ; m}$, where $s<d$, we use Corollary C. 2 to approximate $g$ by smooth, asymptotically hyperbolic metrics that are close to $g$ in the $X_{0}^{s, p}$ topology. Theorem 9.7 implies the corresponding operators are Fredholm of index zero. Since, due to Proposition 8.1 and Lemma 8.5, geometric operators are continuous with respect to this norm, approximation in $X_{0}^{s, p}$ suffices to use index-theoretic arguments in order to conclude that the operator corresponding to $g$ is also Fredholm of index zero.

Recall the definition of $L_{v}$ from (9.9).
Theorem 9.10. Suppose $g$ is an asymptotically hyperbolic metric, of either class (1.3) or class (1.4). Let $\mathcal{P}=\mathcal{P}[g]$ be a $d^{\text {th }}$-order elliptic operator satisfying Assumptions $P$ and $I$. Set $Z=\operatorname{ker}\left(\mathcal{P}: H_{0}^{d / 2,2}(M ; E) \rightarrow H_{0}^{-d / 2,2}(M ; E)\right)$.
Let $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{\infty}(R)$. Given $f \in X_{\delta}^{\sigma-d, q}(M ; E)$ there exists $u \in X_{\delta}^{\sigma, q}(M ; E)$ solving $\mathcal{P} u=f$ if and only if $L_{v}(f)=0$ for all $v \in Z$. In particular,
$$\mathcal{P}: X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma-d, q}(M ; E)$$
is Fredholm with index 0 and kernel $Z$.

Proof. First suppose $s \geq d$. Let $f \in X_{\delta}^{\sigma-d, q}(M)$. Since $\delta \in \mathcal{D}_{\infty}(R)$ we can choose $\widetilde{\delta}<$ $\delta-(n-1) / q$ sufficiently large so that $\widetilde{\delta} \in \mathcal{D}_{q}(R)$. Lemma 3.2 implies $X_{\delta}^{t, q}(M) \subset H_{\widetilde{\delta}}^{t, q}(M)$ for all $t \in \mathbb{R}$.
Suppose $\mathcal{P} u=f$ for some $u \in X_{\delta}^{\sigma, q}(M)$. Then $u \in H_{\widetilde{\delta}}^{\sigma, q}(M)$ and Theorem 9.7 implies that $L_{v}(f)=0$ for all $v \in Z$. Conversely, suppose $L_{v}(f)=0$ for all $v \in Z$. Since $f \in X_{\delta}^{\sigma-d, q}(M) \subset H_{\widetilde{\delta}}^{\sigma-d, q}(M)$, Theorem 9.7 implies the existence of $u \in H_{\widetilde{\delta}}^{\sigma, q}(M)$ with $\mathcal{P} u=f$. Proposition 9.9 implies that $u \in X_{\delta}^{\sigma, q}(M)$.

Proposition 9.9 further implies $Z \subset X_{\delta}^{\sigma, q}(M)$ and thus $\operatorname{dim}(\operatorname{ker} \mathcal{P})=\operatorname{dim}(Z)$. Moreover, if $L_{v}$ vanishes on $X_{\delta}^{\sigma-d, q}(M)$ then $L_{v}(v)=0$ and therefore $v=0$. Thus coker $\mathcal{P}=\operatorname{dim}(Z)$ as well and $\mathcal{P}: X_{\delta}^{\sigma, q}(M) \rightarrow X_{\delta}^{\sigma-d, q}(M)$ has index 0.
Now relax the assumption that $s \geq d$ and let $g_{n}$ be a sequence of asymptotically hyperbolic metrics such that $\bar{g}_{n} \in C^{\infty}(\bar{M})$ and such that $g_{n} \rightarrow g$ in $X_{0}^{s, p}(M)$ as provided by Corollary C.2. Let $F$ be the tensor bundle ambient to $E$ and let $\Pi_{E}$ denote $g$-orthogonal projection of sections of $F$ onto sections of $E$. For each $n$, let $E_{n}$ be the geometric tensor bundle associated with $g_{n}$ corresponding to $E$ and let $\Pi_{E_{n}}$ be the $g_{n}$ orthogonal projection onto $E_{n}$. We claim that $\Pi_{E_{n}} \rightarrow \Pi_{E}$ as a map on $X_{\delta}^{\sigma, q}(M ; F)$ and that
$$\begin{aligned}
& \Pi_{E_{n}}: X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma, q}\left(M ; E_{n}\right), \\
& \Pi_{E}: X_{\delta}^{\sigma-d, q}\left(M ; E_{n}\right) \rightarrow X_{\delta}^{\sigma-d, q}(M ; E)
\end{aligned}$$
are isomorphisms for $n$ sufficiently large. Assuming this claim for the moment, observe from Lemma 8.5 and Proposition 8.1 that the operators $\mathcal{P}_{n}$ converge to $\mathcal{P}$ as maps $X_{\delta}^{\sigma, q}(M ; F) \rightarrow$ $X_{\delta}^{\sigma-d, q}(M ; F)$. Hence $\Pi_{E} \circ \mathcal{P}_{n} \circ \Pi_{E_{n}} \rightarrow \mathcal{P}$ as maps $X_{\delta}^{\sigma, q}(M ; E) \rightarrow X_{\delta}^{\sigma-d, q}(M ; E)$. Because the maps $\Pi_{E}$ and $\Pi_{E_{n}}$ are isomorphisms between sections of their respective geometric tensor bundles, each $\Pi_{E} \circ \mathcal{P}_{n} \circ \Pi_{E_{n}}$ is Fredholm with index zero. Recall from Proposition 8.16 that $\mathcal{P}$ is semi-Fredholm. Since the index of a semi-Fredholm map is locally constant [Sch01] it follows that $\mathcal{P}$ is also Fredholm with index zero.

To establish the claim, using local orthonormal frames constructed via Lemma A. 13 one readily verifies that the operator norm of $\Pi_{E_{n}}-\Pi_{E}$ as a map on $X_{\delta}^{\sigma, q}(M ; F)$ is controlled by $\left\|g_{n}-g\right\|_{X_{0}^{s, p}(M)}$ and hence converges to zero. On $X_{\delta}^{\sigma, q}(M ; E)$ we have id $-\Pi_{E} \circ \Pi_{E_{n}}=$ $\Pi_{E} \circ\left(\Pi_{E}-\Pi_{E_{n}}\right)$ and hence for $n$ sufficiently large $\Pi_{E} \circ \Pi_{E_{n}}$ is invertible on $X^{\sigma, q}(M ; E)$ and $\Pi_{E_{n}}$ is therefore injective. A parallel argument shows that for $n$ large enough $\Pi_{E_{n}}$ is also surjective, and similar considerations show that $\Pi_{E}: X_{\delta}^{\sigma-d, q}\left(M ; E_{n}\right) \rightarrow X_{\delta}^{\sigma-d, q}(M ; E)$ is also an isomorphism for $n$ sufficiently large.
It remains in the low regularity case to show $\operatorname{ker} \mathcal{P}=Z$, and to identify the image of $\mathcal{P}$. First, picking $\widetilde{\delta}$ as above, we have the straightforward inclusion
$$\begin{aligned}
\operatorname{ker}\left(\mathcal{P}: X_{\delta}^{\sigma, q}(M) \rightarrow X_{\delta}^{\sigma-d, q}(M)\right) & \subset \operatorname{ker}\left(\mathcal{P}: H_{\widetilde{\delta}}^{\sigma, q}(M) \rightarrow H_{\widetilde{\delta}}^{\sigma-d, q}(M)\right) \\
& =Z .
\end{aligned}$$
Regarding the image, let
$$Y=\left\{w \in X_{\delta}^{\sigma-d, q}(M ; E): L_{v}(w)=0 \text { for all } v \in Z\right\} .$$
We claim that $v \mapsto L_{v}$ is injective from $Z$ to $\left(X_{\delta}^{\sigma-d, q}(M)\right)^{*}$, in which case $\operatorname{codim} Y=$ $\operatorname{dim} Z$. If $v \in Z$ is not zero, the density of smooth compactly supported sections in $H_{0}^{d / 2,2}(M)$ implies we can find such a section $\psi$ with $L_{v}(\psi) \neq 0$. The claim follows from observing $\psi \in X_{\delta}^{\sigma-d, q}(M)$ as well.

Theorem 9.7 implies
$$\operatorname{im}\left(\mathcal{P}: X_{\delta}^{\sigma, q}(M) \rightarrow X_{\delta}^{\sigma-d, q}(M)\right) \subset Y .$$
Recalling that $\mathcal{P}$ has index zero we compute
$$\operatorname{dim} Z \geq \operatorname{dim}(\operatorname{ker} \mathcal{P})=\operatorname{codim}(\operatorname{im} \mathcal{P}) \geq \operatorname{codim} Y=\operatorname{dim} Z .$$
So all the intermediate inequalities are equalities, which is only possible if the containments (9.11) and (9.12) are equalities. \(\square\)

As a consequence of Theorem 9.10, we can now show that Proposition 9.9 holds without making the smooth metric hypothesis.

Corollary 9.11. Suppose $u \in H_{\delta_{0}}^{\sigma_{0}, q_{0}}(M ; E)$ for some $\left(\sigma_{0}, q_{0}\right) \in \mathcal{S}_{d}^{s, p}$ and some $\delta_{0} \in$ $\mathcal{D}_{q_{0}}(R)$. If $\mathcal{P} u \in X_{\delta}^{\sigma-d, q}(M ; E)$ for some $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{\infty}(R)$, then $u \in$ $X_{\delta}^{\sigma, q}(M ; E)$.

Proof. Observe that $\mathcal{P} u \in X_{\delta}^{\sigma-d, q}(M) \subset H_{\delta}^{\sigma-d, q}(M)$ for some $\widetilde{\delta} \in \mathcal{D}_{q}(R)$. Proposition 9.5 implies $u \in H_{\widetilde{\delta}}^{\sigma, q}(M)$ and we wish to improve to $X_{\delta}^{\sigma, q}(M)$.
Since $\mathcal{P} u$ satisfies $\langle v, \mathcal{P} u\rangle_{g}=0$ for all $v \in Z$, Theorem 9.10 implies there exists $w \in X_{\delta}^{\sigma, q}$ such that $\mathcal{P} w=\mathcal{P} u$. Moreover,
$$u-w \in \operatorname{ker} \mathcal{P}: H_{\delta^{*}}^{\sigma, q}(M) \rightarrow H_{\delta^{*}}^{\sigma-d, q}(M)=Z .$$
Theorem 9.10 implies $Z \subset X_{\delta}^{s, p}(M)$ and therefore $u=w+(u-w) \in X_{\delta}^{s, p}(M)$ as well. \(\square\)
9.4. Structure theorems. We now present structure theorems for elliptic operators satisfying Assumptions P and I. For such an operator $\mathcal{P}[g]$, and for asymptotically hyperbolic metric $g$ of class $\mathscr{H}^{s, p ; m}$ satisfying (1.3) or class $\mathscr{X}^{s, p ; m}$ satisfying (1.4), let
$$Z=\operatorname{ker}\left(\mathcal{P}[g]: H_{0}^{d / 2,2}(M ; E) \rightarrow H_{0}^{-d / 2,2}(M ; E)\right) .$$
For each $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$, we invoke Lemma 9.6 to define
$$Y\left(H_{\delta}^{\sigma, q}\right)=\left\{u \in H_{\delta}^{\sigma, q}(M ; E): L_{v}(u)=0 \text { for all } v \in Z\right\} .$$
For $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{\infty}(R)$, the space $Y\left(X_{\delta}^{\sigma, q}\right)$ is defined analogously.
Theorem 9.12. Suppose $g$ is an asymptotically hyperbolic metric, of either class (1.3) or class (1.4). Let $\mathcal{P}=\mathcal{P}[g]$ be a $d^{\text {th }}$-order elliptic operator satisfying Assumptions $P$ and $I$.

Let $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{q}(R)$. There exist bounded operators $G, H: H_{\delta}^{\sigma-d, q}(M ; E) \rightarrow$ $H_{\delta}^{\sigma, d}(M ; E)$ that satisfy
$$\begin{aligned}
& \operatorname{ker} H=Y\left(H_{\delta}^{\sigma-d, q}\right), \\
& \operatorname{im} H=Z, \\
& u=G \mathcal{P} u+H u \quad \text { for all } u \in H_{\delta}^{\sigma, q}(M ; E), \\
& w=\mathcal{P} G w+H w \quad \text { for all } w \in H_{\delta}^{\sigma-d, q}(M ; E) .
\end{aligned}$$

Proof. Recall that $Z \subset L^{2}(M)$ and let $\left\{v_{j}\right\}_{j=1}^{m}$ be an $L^{2}$ orthonormal basis for $Z$. For $u \in$ $H_{\delta}^{\sigma, q}(M)$, we use Lemma 9.6 to define the continuous map $H: H_{\delta}^{\sigma-d, q}(M) \rightarrow H_{\delta}^{\sigma, q}(M)$ by
$$H(u)=\sum_{j=1}^{m} L_{v_{j}}(u) v_{j}=\sum_{j=1}^{m}\left\langle v_{j}, u\right\rangle_{(M, g)} v_{j} .$$
It follows immediately from the definition that $\operatorname{im} H=Z$ and that $\operatorname{ker} H=Y\left(H_{\delta}^{\sigma-d, q}\right)$.
We now claim that $\mathcal{P}$ is a bijection $Y\left(H_{\delta}^{\sigma, q}\right) \rightarrow Y\left(H_{\delta}^{\sigma-d, q}\right)$. That the image of $Y\left(H_{\delta}^{\sigma, q}\right)$ under $\mathcal{P}$ lies in $Y\left(H_{\delta}^{\sigma-d, q}\right)$ follows from the facts that $\mathcal{P}$ is self-adjoint and that, as noted in the proof of Lemma 9.6, $Z \subset H_{-\delta}^{d-\sigma, q^{*}}(M)$. The injectivity is a consequence of the definition of $Y\left(H_{\delta}^{\sigma-d, q}\right)$, and thus it remains to show surjectivity. For $f \in Y\left(H_{\delta}^{\sigma-d, q}\right)$, Theorem 9.7 implies the existence of $\widetilde{u} \in H_{\delta}^{\sigma, q}(M)$ with $\mathcal{P} \widetilde{u}=f$. Let $u=\widetilde{u}-H \widetilde{u}$. Since $H \widetilde{u} \in Z$, and since $Z$ is the kernel of $\mathcal{P}$ acting on $H_{\delta}^{\sigma, q}(M)$, we have
$$\mathcal{P} u=\mathcal{P} \widetilde{u}=f .$$
Define $G: Y\left(H_{\delta}^{\sigma-d, q}\right) \rightarrow Y\left(H_{\delta}^{\sigma, q}\right)$ to be the inverse of $\left.\mathcal{P}\right|_{Y\left(H_{\delta}^{\sigma, q}\right)}$, so that $G \mathcal{P} u=u$ for all $u \in Y\left(H_{\delta}^{\sigma, q}\right)$. The Inverse Mapping Theorem implies $G$ is continuous, and since $Z$ is finite-dimensional, we may extend $G$ continuously to all of $H_{\delta}^{\sigma-d, q}(M)$ by declaring $\left.G\right|_{Z}=0$.
Direct computation now shows that for $u \in H_{\delta}^{\sigma, q}(M)$ we have
$$u-H u=G(\mathcal{P}(u-H u))=G \mathcal{P} u .$$
Furthermore, for $w \in H_{\delta}^{\sigma-d, q}(M)$ we have $u-H u \in Y\left(H_{\delta}^{\sigma-d, q}\right)$ and thus
$$u-H u=\mathcal{P} G(u-H u)=\mathcal{P} G u,$$
where we have used that $H u \in Z$ and $\left.G\right|_{Z}=0$. \(\square\)

The analogous result for Gicquaud-Sakovich spaces is proved identically using Theorem 9.10 in place of Theorem 9.7.

Theorem 9.13. Suppose $g$ is an asymptotically hyperbolic metric, of either class (1.3) or class (1.4). Let $\mathcal{P}=\mathcal{P}[g]$ be a $d^{\text {th }}$-order elliptic operator satisfying Assumptions $P$ and $I$.
\begin{lstlisting}[mathescape=true]
Suppose $(\sigma, q) \in \mathcal{S}_{d}^{s, p}$ and $\delta \in \mathcal{D}_{\infty}(R)$. There exist bounded operators $G, H: X_{\delta}^{\sigma-d, q}(M ; E) \rightarrow$
$X_{\delta}^{\sigma, d}(M ; E)$ that satisfy
    $\operatorname{ker} H=Y\left(X_{\delta}^{\sigma-d, q}\right)$,
    $\operatorname{im} H=Z$,
    $u=G \mathcal{P} u+H u \quad$ for all $u \in X^{\sigma, q},_{\delta}(M ; E)$
    $w=\mathcal{P} G w+H w \quad$ for all $w \in X_{\delta}^{\sigma-d, q}(M ; E)$.
\end{lstlisting}

9.5. Regularity bootstrapping and polyhomogeneity. While stated for metrics with Sobolevscale regularity, the theorems above apply to more regular metrics as well. Thus one application of our work is the following regularity bootstrapping principle. Given a lowregularity solution to an elliptic PDE arising from a more regular metric (perhaps, for example, from variational methods), then one expects that this solution has as much regularity as the metric allows. The following results illustrate this principle in three common regularity settings: Hölder-regular metrics, metrics smooth on $M$, and polyhomogeneous metrics. For simplicity of exposition, we restrict attention to second-order geometric operators acting on scalar-valued functions; more general results can be obtained from analogous reasoning.

We first consider the case of metrics with Hölder regularity, and suppose that $g$ is an asymptotically hyperbolic metric of class $\mathscr{C}^{k, \alpha ; m}$, meaning that
$$\bar{g}=\rho^{2} g \in \mathscr{C}^{k, \alpha ; m}(M) \quad \text { with } 1 \leq m \leq k, \quad \alpha \in(0,1),$$
which implies $\bar{g} \in C^{0}(\bar{M})$, and that
$$|d \rho|_{\bar{g}}=1 \quad \text { along } \partial M .$$

Theorem 9.14. Suppose that $\mathcal{P}[g]$ is a second-order elliptic operator satisfying Assumptions $P$ and $I$, and having indicial radius $R$. Let $g$ be an asymptotically hyperbolic metric of class $\mathscr{C}^{k, \alpha ; m}$, and assume that (9.13) holds with $k \geq 2$.
Suppose that $u \in H_{\delta^{\prime}}^{\sigma, q}(M ; \mathbb{R})$, where $\delta^{\prime} \in \mathcal{D}_{q}(R)$ and where $(\sigma, q) \in S_{2}^{k, p}$ for some $p>1$. Suppose also that $\mathcal{P}[g] u=f$, where $f \in C_{\delta}^{k-2, \alpha}(M ; \mathbb{R})$ with $\delta \in \mathcal{D}_{\infty}(R)$. Then $u \in C_{\delta}^{k, \alpha}(M ; \mathbb{R})$.

Proof. First, note that we may increase $p$ as needed and still retain $(\sigma, q) \in S_{2}^{k, p}$; see (8.2). From (4.20), we have $\bar{g} \in \mathscr{X}^{k, p ; m}(M)$ for all $p>1$, and thus we may choose $p$ sufficiently large that $g$ is an asymptotically hyperbolic metric of class (1.4).
The basic inclusion of Lemma 3.2 implies that $f \in X_{\delta}^{k-2, p}(M)$. Proposition 9.9 implies $u \in X_{\delta}^{k, p}(M)$. With $p$ sufficiently large, the Sobolev embedding of Proposition 3.3 implies
that $u \in C_{\delta}^{k-1, \beta}(M)$ for some $0<\beta<1$. Finally, [AILSA18, Lemma 5.6] implies that $u \in C_{\delta}^{k, \alpha}(M)$. \(\square\)

An immediate consequence is the following result for metrics which are smooth on $M$, but have limited regularity on $\bar{M}$.

Corollary 9.15. Suppose that $\mathcal{P}[g]$ is a second-order elliptic operator satisfying Assumptions $P$ and $I$, and having indicial radius $R$. Let $g$ be an asymptotically hyperbolic metric of class $\mathscr{C}^{\infty ; m}$, and assume that (9.13) holds for all $k \in \mathbb{N}$.
Suppose that $u \in H_{\delta^{\prime}}^{\sigma, q}(M ; \mathbb{R})$, where $\delta^{\prime} \in \mathcal{D}_{q}(R)$ and where $(\sigma, q) \in S_{2}^{k, p}$ for some $p>1$. Suppose also that $\mathcal{P}[g] u=f$, where $f \in C_{\delta}^{\infty}(M ; \mathbb{R})$ with $\delta \in \mathcal{D}_{\infty}(R)$. Then $u \in C_{\delta}^{\infty}(M ; \mathbb{R})$.

A second consequence of Theorem 9.14 concerns metrics in the polyhomogeneous category. Such metrics are smooth in the interior $M$ and admit a formal expansion near $\partial M$ of the form
$$g \sim \sum_{i=0}^{\infty} \sum_{j=0}^{N_{i}} \rho^{s_{i}}(\log \rho)^{j} \bar{g}_{i j},$$
where $s_{i}$ is a sequence diverging to $+\infty, N_{i} \in \mathbb{N}_{\geq 0}$, and $\bar{g}_{i j}$ are smooth tensor fields on $\bar{M}$; see Appendix A of [AILSA18] for a detailed definition and a discussion of elliptic operators in the polyhomogeneous category.

The following consequence of Theorem 9.14 and [AILSA18, Theorem A.14] is stated for $m=2$. Adapting the proof of [AILSA18, Proposition A.14], as done in [AILSA18, Theorem A.18], can relax this restriction to $m \geq 1$.

Corollary 9.16. Suppose that $\mathcal{P}[g]$ is a second-order elliptic operator satisfying Assumptions $P$ and $I$, and having indicial radius $R$. Let $g$ be an asymptotically hyperbolic metric of class $\mathscr{C}^{2, \alpha ; 2}$, and further assume that $g$ is polyhomogeneous.
Suppose that $u \in H_{\delta^{\prime}}^{\sigma, q}(M ; \mathbb{R})$, where $\delta^{\prime} \in \mathcal{D}_{q}(R)$ and where $(\sigma, q) \in S_{2}^{k, p}$ for some $p>1$. Suppose also that $\mathcal{P}[g] u=f$, where $f \in C_{\delta}^{2, \alpha}(M ; \mathbb{R})$ with $\delta \in \mathcal{D}_{\infty}(R)$, and that $f$ is polyhomogeneous. Then $u$ is polyhomogeneous as well.

\section*{Appendix A. Weighted function spaces}

This section concerns weighted function spaces on a manifold $M$ admitting a continuous conformal compactification $\bar{M}$. These spaces generalize the classical weighted Sobolev spaces $W_{\delta}^{k, p}(M ; E)$ from, e.g., [Lee06] and as well as the Gicquaud-Sakovich spaces $X_{\delta}^{k, p}(M ; E)$ from [GS12] to real scales of differentiability.
A tensor bundle $E$ over $\bar{M}$ is a bundle $T^{k_{1}, k_{2}} \bar{M}$ with contravariant rank $k_{1}$ and covariant rank $k_{2}$, and we use the same notation $E$ for the induced bundle over $M$. More generally, when $\bar{M}$ is equipped with a metric a geometric tensor bundle over $\bar{M}$ is a subbundle of
a tensor bundle $T^{k_{1}, k_{2}} \bar{M}$ that is associated with an invariant subspace of the standard representation of $O(n)$ (or $S O(n)$ if $\bar{M}$ is orientable) on $T^{k_{1}, k_{2}} \mathbb{R}^{n}$. Because geometric tensor bundles potentially depend on the regularity of the underlying metric on $\bar{M}$ we focus for the moment on the foundation case where $E$ is a tensor bundle over $\bar{M}$. Section A. 5 contains the details needed to treat the full case of geometric tensor bundles.
Recall that for $s \in \mathbb{R}$ and $1<p<\infty$ the Bessel potential space $H^{s, p}\left(\mathbb{R}^{n}\right)$ is defined by
$$H^{s, p}\left(\mathbb{R}^{n}\right)=\left\{u \in \mathcal{S}^{\prime}\left(\mathbb{R}^{n}\right):\left\|\mathcal{F}^{-1} \Lambda^{s} \mathcal{F} u\right\|_{L^{p}\left(\mathbb{R}^{n}\right)}\right\}<\infty,$$
where $S^{\prime}\left(\mathbb{R}^{n}\right)$ is the dual space of the rapidly decaying smooth functions, $\Lambda(\xi)=(1+$ $\left.|\xi|^{2}\right)^{s / 2}$ and where $\mathcal{F}$ is the Fourier transform. When $s \in \mathbb{Z}$ then $H^{s, p}\left(\mathbb{R}^{n}\right)=W^{k, p}\left(\mathbb{R}^{n}\right)$. If $\Omega$ is an open subset of $\mathbb{R}^{n}, H^{s, p}(\Omega)$ is the quotient space of $H^{s, p}\left(\mathbb{R}^{n}\right)$ where two distributions are equivalent if they agree on $\Omega$, and $H^{s, p}(\Omega)$ is given the quotient norm $\|u\|_{H^{s, p}(\Omega)}=$ $\inf _{\left.w\right|_{\Omega}=u}\|w\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}$.
To define corresponding asymptotically hyperbolic weighted spaces, we fix a cutoff function $\chi$ that is equal to 1 on $B_{1 / 2}^{\mathbb{H}}$ and vanishes outside $B_{r}^{\mathbb{H}}$ for some $1 / 2<r<2$. Let $\left\{\Phi_{i}\right\}$ be the collection of preferred Möbius parametrizations of $M$ defined at the end of §2.

Definition A.1. Let $E$ be a tensor bundle over $M$. For $s \in \mathbb{R}, \delta \in \mathbb{R}$ and $1<p<\infty$ the weighted Bessel potential space $H_{\delta}^{s, p}(M ; E)$ is the set of all $E$-valued distributions u such that
$$\|u\|_{H_{\delta}^{s, p}(M ; E)}=\left[\sum_{i} \rho_{i}^{-\delta p}\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}\right]^{\frac{1}{p}}<\infty$$
where the norms over $\mathbb{R}^{n}$ involve the vector of coefficients of $\Phi_{i}^{*} u$ with respect to the standard basis.

The Gicquaud-Sakovich space $X_{\delta}^{s, p}(M ; E)$ is the set of all $E$-valued distributions $u$ with
$$\|u\|_{X_{\delta}^{s, p}(M ; E)}=\sup _{i} \rho_{i}^{-\delta}\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}<\infty .$$

To simplify notation, when $E=T^{0,0} \bar{M}$ we denote the associated spaces by $H_{\delta}^{s, p}(M ; \mathbb{R})$ and $X_{\delta}^{s, p}(M ; \mathbb{R})$.

The definition of $H_{\delta}^{s, p}(M ; E)$ is analogous to the definition of weighted Bessel potential spaces in Euclidean spaces found in [Tri76] and several of the proofs below rely on generalizations of techniques found there.
The following lemma is fundamental and shows we can build functions in weighted spaces in a controlled fashion by adding functions supported in the images of Möbius charts.

Lemma A.2. Let $E$ be a tensor bundle over $M$. Suppose $u=\sum_{i} u_{i}$ where each $u_{i} \in$ $D^{\prime}(M ; E)$ is a distribution supported in $\Phi_{i}\left(B_{r}^{\mathbb{H}}\right)$ for some $r<2$. Then
\begin{itemize}
\item[(a)] If $s, \delta \in \mathbb{R}$ and $1<p<\infty$
$$\|u\|_{H_{\delta}^{s, p}(M ; E)}^{p} \lesssim \sum_{i=1}^{\infty} \rho_{i}^{-p \delta}\left\|\Phi_{i}^{*} u_{i}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}$$
and $\sum_{i} u_{i}$ converges in norm.
\item[(b)] If $s, \delta \in \mathbb{R}$ and $1<p<\infty$
$$\|u\|_{X_{\delta}^{s, p}(M ; E)} \lesssim \sup _{i=1} \rho_{i}^{-p \delta}\left\|\Phi_{i}^{*} u_{i}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} .$$
\item[(c)] If $k \in \mathbb{N}_{\geq 0}$ and $0<\alpha<1$,
$$\|u\|_{C_{\delta}^{k, \alpha}(M ; E)} \lesssim \sup _{i=1} \rho_{i}^{-p \delta}\left\|\Phi_{i}^{*} u_{i}\right\|_{C^{k, \alpha}\left(\mathbb{R}^{n}\right)} .$$
\end{itemize}

Proof. The transition Jacobians $\mathrm{D}\left(\Phi_{j}^{-1} \circ \Phi_{i}\right)$ admit uniform $C^{k}$ bounds for any choice of $k$. Indeed if $\Theta_{a_{i}}$ and $\Theta_{a_{j}}$ are background coordinates associated with two Möbius parametrizations
$$\mathrm{D}\left(\Phi_{j}^{-1} \circ \Phi_{i}\right)_{(x, y)}=\frac{\rho_{i}}{\rho_{j}}\left(\mathrm{D}\left(\Theta_{a_{j}}^{-1} \circ \Theta_{a_{i}}\right)\right)_{\left(\theta_{i}+\rho_{i} y, \rho_{i} y\right)}$$
and the uniform bounds follow from uniform estimates for background coordinate transition functions the fact that $\rho_{i} / \rho_{j} \leq 8$ if the images of $\Phi_{i}$ and $\Phi_{j}$ have nontrivial intersection. With this obsrvation in hand we establish inequality (A.3); inequality (A.4) is demonstrated using similar techniques and inequality (A.5) is a straightforward consequence of the $C^{k}$ estimates for transition Jacobians along with uniform local finiteness.
Consider indices $i$ and $j$ with $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right) \cap \Phi_{j}\left(B_{2}^{\mathbb{H}}\right) \neq \emptyset$ and let $U_{j, i}=\Phi_{j}^{*} \Phi_{i, *}\left(B_{2}^{\mathbb{H}}\right)$. If $w$ is a smooth, compactly supported function on $\mathbb{R}^{n}$ we define
$$T w=\left.\chi\left(\Phi_{j}^{-1} \circ \Phi_{i}\right)^{*} w\right|_{U_{j, i}}$$
and extend this function by zero off of $U_{i, j}=\Phi_{i}^{*} \Phi_{j, *}\left(B_{2}^{\mathbb{H}}\right)$. Uniform $C^{k}$ bounds on the transition Jacobian $D\left(\Phi_{j}^{-1} \circ \Phi_{i}\right)$ imply that for each $k \in \mathbb{N}_{\geq 0}$ that $T$ determines a continuous map $H^{k, p}\left(\mathbb{R}^{n}\right) \rightarrow H^{k, p}\left(\mathbb{R}^{n}\right)$ with norm controlled by a constant independent of $i$ and $j$. By interpolation and duality this same statement holds replacing $k$ with any $s \in \mathbb{R}$. As a consequence we conclude
$$\left\|\chi \Phi_{i}^{*} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \lesssim\left\|\Phi_{j}^{*} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}$$
with implicit constant independent of $i$ and $j$.

Now fix $i$ and recall that the size of the neighbor index set $N(i)=\left\{j: \Phi_{i}\left(B_{2}^{\mathbb{H}}\right) \cap \Phi_{j}\left(B_{2}^{\mathbb{H}}\right) \neq\right.$ $\emptyset\}$ admits a uniform upper bound. Then
$$\begin{aligned}
\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} & =\left\|\chi \Phi_{i}^{*} \sum_{j \in N(i)} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \\
& \lesssim \sum_{j \in N(i)}\left\|\chi \Phi_{i}^{*} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \\
& \lesssim \sum_{j \in N(i)}\left\|\Phi_{j}^{*} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}
\end{aligned}$$
with implicit constant independent of $i$. Moreover, since $\rho_{i} / \rho_{j} \leq 8$ if $j \in N(i)$,
$$\begin{aligned}
\|u\|_{H_{\delta}^{s, p}(M ; E)}^{p} & =\sum_{i=1}^{\infty} \rho_{i}^{-\delta p}\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \\
& \lesssim \sum_{i=1}^{\infty} \rho_{i}^{-\delta p} \sum_{j \in N(i)}\left\|\Phi_{j}^{*} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \\
& \lesssim \sum_{i=1}^{\infty} 8^{-\delta p} \sum_{j \in N(i)} \rho_{j}^{-\delta p}\left\|\Phi_{j}^{*} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \\
& \lesssim \sum_{j=1}^{\infty} \rho_{j}^{-\delta p}\left\|\Phi_{j}^{*} u_{j}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}
\end{aligned}$$
as required. \(\square\)

As a first application, Lemma A. 2 allows us to construct a convenient partition of unity based on the cutoff function $\chi$. Specifically, let $\chi_{i}=\left(\Phi_{i}\right)_{*} \chi$, which we extend by zero to all of $M$. Lemma A.2(c) implies
$$\bar{\chi}=\sum_{i=1}^{\infty} \chi_{i} \in C_{0}^{k, \alpha}(M ; \mathbb{R})$$
for every $k \in \mathbb{N}$ and $0<\alpha<1$. Moreover, since the sets $\Phi_{i}\left(B_{1 / 2}^{\mathbb{H}}\right)$ cover $M$ it follows that $\bar{\chi} \geq 1$ and we conclude $1 / \bar{\chi} \in C_{0}^{k, \alpha}(M ; \mathbb{R})$ as well. The functions $\chi_{i} / \bar{\chi}$ then evidently form a smooth partition of unity admitting uniform $C_{0}^{k, \alpha}(M ; \mathbb{R})$ bounds.
Definition A. 1 relies on a number of choices, and §A. 6 shows that the spaces are independent of these choices. For the moment, we use Lemma A. 2 to show that the choice of cutoff function is unimportant and to establish an alternative formulation of the norms that does not employ a cutoff function. In light of Lemma 3.1, the following result also shows that when $s \in \mathbb{N}_{\geq 0}$ the weighted Bessel potential spaces agree with the weighted Sobolev spaces $W_{\delta}^{k, p}(M ; E)$.

Lemma A.3. Let $E$ be a tensor bundle over $\bar{M}$. For all $s, \delta \in \mathbb{R}$ and $1<p<\infty$ the space $H_{\delta}^{s, p}(M ; E)$ is independent of the choice of cutoff function and the norms for any two choices are equivalent. Moreover, for each $1 / 2<r \leq 2$
$$\begin{aligned}
& \|u\|_{H_{\delta}^{s, p}(M ; E)} \sim\left[\sum_{i} \rho_{i}^{-\delta p}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)}^{p}\right]^{\frac{1}{p}}, \\
& \|u\|_{X_{\delta}^{s, p}(M ; E)} \sim \sup _{i} \rho_{i}^{-\delta p}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)} .
\end{aligned}$$
Proof. Let $\chi$ and $\eta$ be two choices of cutoff functions, and let $H_{\delta}^{s, p}(M ; \chi)$ and $H_{\delta}^{s, p}(M ; \eta)$ be the corresponding spaces. Suppose $u \in H_{\delta}^{s, p}(M ; \eta)$ and let $u_{i}=\left(\left(\Phi_{i}\right)_{*} \eta\right) u$ which we extend by zero outside of $\Phi_{i}\left(B_{2}\right)$. Then each $u_{i} \in H_{\text {loc }}^{s, p}(M)$ and from the definition of the norm on $H_{\delta}^{s, p}(M ; \eta)$ it follows that $\sum_{i} \rho_{i}^{-p \delta}\left\|\eta \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}$ is finite. But then Lemma A.2(a) implies $\hat{u}:=\sum_{i} u_{i} \in H_{\delta}^{s, p}(M ; \chi)$ and
$$\|\hat{u}\|_{H_{\delta}^{s, p}(M ; \chi)}^{p} \lesssim \sum_{i} \rho_{i}^{-p \delta}\left\|\eta \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}=\|u\|_{H_{\delta}^{s, p}(M ; \eta)}^{p} .$$
Let $\bar{\eta}=\sum_{i} \Phi_{i, *} \eta$ and observe that $\hat{u}=\bar{\eta} u$. Following the construction that leads to (A.7), but using $\eta$ in place of $\chi$, we obtain $\bar{\eta} \in C_{0}^{k, \alpha}(M)$ with $1 / \bar{\eta} \in C_{0}^{k, \alpha}(M)$ for every $k \in \mathbb{N}$ and $0<\alpha<1$. In particular, choosing $k>s$, it is an easy consequence of Definition A. 1 that multiplication by $\bar{\eta}$ or $1 / \bar{\eta}$ is a continuous automorphism of $H_{\delta}^{s, p}(M ; \chi)$ and therefore
$$\|u\|_{H_{\delta}^{s, p}(M ; \chi)}^{p} \lesssim\|\bar{\eta} u\|_{H_{\delta}^{s, p}(M ; \chi)}^{p} .$$
The continuous inclusion $H_{\delta}^{s, p}(M ; \eta) \hookrightarrow H_{\delta}^{s, p}(M ; \chi)$ follows from inequalities (A.10) and (A.11) and the reverse inclusion follows from symmetry.
Suppose $1 / 2<r<2$. Pick two cutoff functions $\eta_{1}$ and $\eta_{2}$ supported on $B_{2}^{\mathbb{H}}$ that both equal 1 on $B_{1 / 2}^{\mathbb{H}}$ and such that $\eta_{1}$ is supported in $B_{r}^{\mathbb{H}}$ whereas $\eta_{2}=1$ on $B_{r}^{\mathbb{H}}$. Suppose $u \in H_{\delta}^{s, p}(M)$. For each $i$
$$\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)} \leq\left\|\eta_{2} \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} .$$
On the other hand, we can pick an extension $w$ of $\Phi_{i}^{*} u$ such that $\|w\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \leq 2\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)}$ in which case
$$\left\|\eta_{1} \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}=\left\|\eta_{1} w\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \lesssim\|w\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \leq 2\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{H}}\right)} .$$
The alternative norms (A.8) and (A.9) now follow from inequalites (A.12) and (A.13) along with the norm equivalence just established for different choices of cutoff functions. \(\square\)
A.1. Elementary properties. A standard diagonalization argument using Lemma A. 2 as a component shows that the spaces $H^{s, p}(M ; E)$ and $X^{s, p}(M ; E)$ are complete.

In light of the equivalent norms (A.8) and (A.9) from Lemma A.3, the elementary inclusions from Lemma 3.2 as well as Sobolev embedding from Proposition 3.3 are established using standard embedding properties of Sobolev spaces [Tri10] and identical techniques as used for weighted spaces with integral degrees of differentiability (see, e.g., [Lee06]

Lemma 3.6(b,c) and its associated references). For example, suppose $u \in X_{\delta}^{s, p}(M ; E)$. Then if $\delta^{\prime}+(n-1) / p<\delta$ we find
$$\sum_{i} \rho_{i}^{-\delta^{\prime} p}\left\|\Phi_{i}^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{H}}\right)}^{p} \lesssim\|u\|_{X_{\delta}^{s, p}(M ; E)}^{p} \sum_{i} \rho_{i}^{\left(\delta-\delta^{\prime}\right) p} \lesssim\|u\|_{X_{\delta}^{s, p}(M ; E)}^{p}\left\|\rho^{\delta-\delta^{\prime}}\right\|_{L^{1}(M ; \mathbb{R})} .$$
As $\rho^{a}$ is integrable on $M$ precisely when $a>n-1$, and in particular for $a=\delta-\delta^{\prime}$, we conclude that $X_{\delta}^{s, p}(M ; E)$ embeds into $H_{\delta^{\prime}}^{s, p}(M ; E)$.
Proposition 3.11 concerning multiplication is similarly proved using the alternative norms (A.8) and (A.9) along with the analogous multiplication results for unweighted spaces from, e.g., the appendix of [HMT22].

Lemma A. 4 (Rellich Lemma). Let $E$ be a tensor bundle over M. Suppose $1<p<\infty$, $s, s^{\prime} \in \mathbb{R}$ and $\delta, \delta^{\prime} \in \mathbb{R}$. Then
$$\begin{array}{lll}
H_{\delta}^{s, p}(M ; E) \rightarrow H_{\delta^{\prime}}^{s^{\prime}, p}(M ; E), & s>s^{\prime}, & \delta>\delta^{\prime} ; \\
X_{\delta}^{s, p}(M ; E) \rightarrow X_{\delta^{\prime}}^{s^{\prime}, p}(M ; E), & s>s^{\prime}, & \delta>\delta^{\prime} .
\end{array}$$
Proof. Suppose $\left\{u_{k}\right\}$ is a bounded sequence in $H_{\delta}^{s, p}(M)$ and let $B$ be a bound for the norm of the elements of the sequence. By a diagonalization argument and the usual Rellich Lemma on unweighted spaces we can reduce to a subsequence and assume that each $\chi \Phi_{i}^{*} u_{k}$ converges to some $w_{i} \in H^{s^{\prime}, p}\left(\mathbb{R}^{n}\right)$. Since each $w_{i}$ is supported in some $B_{r}^{\mathbb{H}}$, we can extend $\Phi_{i}^{*} w_{i}$ by zero to all of $M$ and $w=\sum_{i} \Phi_{i}^{*} w_{i}$ is a distribution on $M$. Fatou's Lemma and Lemma 3.2 imply
$$\sum_{i} \rho_{i}^{-\delta p}\left\|w_{i}\right\|_{H^{s^{\prime}, p}\left(\mathbb{R}^{n}\right)}^{p} \leq \lim _{n} \sum_{i} \rho_{i}^{-\delta p}\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s^{\prime}, p}\left(\mathbb{R}^{n}\right)}^{p} \lesssim B^{p}$$
and we conclude from Lemma A. 2 that $w \in H_{\delta}^{s^{\prime}, p}(M)$ with $\|w\|_{H_{\delta}^{s^{\prime}, p}(M ; \mathbb{R})} \lesssim B$.
Recalling the function $\bar{\chi}$ from equation (A.7) we claim that $\bar{\chi} u_{n} \rightarrow w$ in $H_{\delta^{\prime}}^{s^{\prime}, p}(M)$ for $\delta^{\prime}<\delta$. Indeed, let $\varepsilon>0$ and pick $K$ so that if $i \geq K$ then $\rho_{i}^{\delta-\delta^{\prime}}<\varepsilon$. Using Lemma A. 2 we find
$$\sum_{i \geq I} \rho_{i}^{-\delta^{\prime} p}\left\|w_{i}-\chi \Phi_{i}^{*} u_{n}\right\|_{H^{s^{\prime}, p}\left(\mathbb{R}^{n}\right)}^{p} \lesssim\left(\sup _{i \geq I} \rho_{i}^{\left(\delta-\delta^{\prime}\right) p}\right)\left\|w-\bar{\chi} u_{n}\right\|_{H^{s^{\prime}, p}(M)}^{p} \lesssim \varepsilon^{p} B^{p} .$$
On the other hand, by taking $n$ sufficiently large we can ensure
$$\sum_{i<I} \rho_{i}^{-\delta^{\prime} p}\left\|w_{i}-\chi \Phi_{i}^{*} u_{n}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}<\varepsilon^{p}$$
and hence for $n$ sufficiently large
$$\left\|w-\bar{\chi} u_{n}\right\|_{H_{\delta^{\prime}}^{s, p}(M ; E)} \lesssim \varepsilon .$$
That is, $\bar{\chi} u_{n} \rightarrow w$ in $H_{\delta^{\prime}}^{s^{\prime}, p}(M)$ and therefore $u_{n} \rightarrow(\bar{\chi})^{-1} w$ in the same topology.
The analogous proof in the Gicquaud-Sakovich case is similar and is indeed easier because there is no tail to manage. \(\square\)
A.2. Density of smooth tensors. The following result, a variation of [GS12] Lemma 2.1, establishes the density of certain classes of smooth tensors.

Proposition A.5. Suppose $E$ is a tensor bundle over $\bar{M}$. Let $s, \delta \in \mathbb{R}$ and $1<p<\infty$.
\begin{itemize}
\item[(a)] The compactly supported smooth sections of $E$ are dense in $H_{\delta}^{s, p}(M ; E)$.
\item[(b)] The set $C_{\text {loc }}^{\infty}(M ; E) \cap X_{\delta}^{s, p}(M ; E)$ is dense in $X_{\delta}^{s, p}(M ;)$.
\end{itemize}

Proof. Suppose $u \in X_{\delta}^{s, p}(M)$ and let $\varepsilon>0$. For each $i$, let $w_{i}$ be a smooth compactly supported tensor field on $\mathbb{R}^{n}$ such that
$$\rho_{i}^{-\delta p}\left\|\chi \Phi_{i}^{*} u-w_{i}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}<\varepsilon .$$
Since $\chi \Phi_{i}^{*} u$ is compactly supported in $B_{r}^{\mathbb{H}}$ for some $r<2$ we can assume without loss of generality that each $w_{i}$ is supported in $B_{r^{\prime}}^{\mathbb{H}}$ for some $r<r^{\prime}<2$ as well. Observe that $\rho_{i}^{-\delta}\left\|w_{i}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \leq\|u\|_{X_{\delta}^{s, p}}+\varepsilon$. Lemma A.2(b) then implies that $w=\sum_{i}\left(\Phi_{i}\right)_{*} w_{i} \in X^{s, p}(M)$ and it is evidently smooth. Moreover, Lemma A.2(b) also implies
$$\|\bar{\chi} u-w\|_{X_{\delta}^{s, p}} \lesssim \sup _{i} \rho_{i}^{-\delta}\left\|\chi \Phi_{i}^{*} u-w_{i}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}<\varepsilon .$$
Since multiplication by $\bar{\chi}^{-1}$ is a continuous automorphism of $X_{\delta}^{s, p}(M)$ we conclude
$$\left\|u-\bar{\chi}^{-1} w\right\|_{X_{\delta}^{s, p}(M)} \lesssim \varepsilon .$$
Noting that $\bar{\chi}^{-1} w$ is smooth, the proof of part (b) is complete.
Part (a) is proved similarly, noting that we first ignore a tail satisfying
$$\sum_{i \geq K} \rho_{i}^{-\delta p}\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}<\varepsilon^{p}$$
and smoothly approximate finitely many terms to obtain a compactly supported smooth approximating function. \(\square\)

As a consequence of Proposition A.5, $C_{\delta}^{k, \alpha}(M ; \mathbb{R})$ is dense in $H_{\delta}^{k, p}(M ; \mathbb{R})$ for each $k \in \mathbb{N}_{\geq 0}$. The question of whether $C_{\delta}^{k, \alpha}(M ; \mathbb{R})$ is also dense in $X_{\delta}^{k, p}(M ; \mathbb{R})$ was raised in [GS12], and we show here that this is false in general.
Proposition A.6. Let $1<p<\infty$. For each $0<\alpha<1, C_{0}^{0, \alpha}(M ; \mathbb{R})$ is not dense in $X_{0}^{0, p}(M ; \mathbb{R})$.

Proof. Consider a sequence of sets $U_{k} \subset B_{1 / 2}^{\mathbb{H}}$ with Euclidean measures $\left|U_{k}\right|=\left|B_{1 / 2}^{\mathbb{H}}\right| / k$ and let $a_{k}=\left|U_{k}\right|^{-1 / p}$. Let $u_{k}$ be a function on $B_{1 / 2}^{\mathbb{H}}$ that equals $a_{k}$ on $U_{k}$ and is otherwise zero and observe that $\left\|u_{k}\right\|_{L^{p}\left(B_{1 / 2}^{\mathrm{H}}\right)}=1$.
Now suppose we have a second sequence of functions $v_{k} \in C^{0, \alpha}\left(B_{1 / 2}^{\mathbb{H}}\right)$ such that $\| v_{k}-$ $u_{k} \|_{L^{p}\left(B_{1 / 2}^{\mathbb{H}}\right)}<\min \left(1 / 2,\left(\left|B_{1 / 2}^{\mathbb{H}}\right| / 2\right)^{1 / p}\right)$ for every $k$. We claim that for $k \geq 2$ that $\min v_{k}<$ 1 and that $\max v_{k}>a_{k} / 2$. Indeed, if $\min v_{k} \geq 1$ then an easy computation using the
condition $k \geq 2$ shows $\left\|v_{k}-u_{k}\right\|_{L^{p}\left(B_{1 / 2}^{\mathbb{H}}\right)} \geq\left(\left|B_{1 / 2}^{\mathbb{H}}\right| / 2\right)^{1 / p}$. On the other hand if $\max v_{k}<$ $a_{k} / 2$ a similar computation shows that $\left\|v_{k}-u_{k}\right\|_{L^{p}\left(B_{1 / 2}^{\mathbb{H}}\right)} \geq 1 / 2$. As a consequence of these constraints, $\left\|v_{k}\right\|_{C^{0, \alpha}\left(B_{1 / 2}^{\mathrm{H}}\right)} \rightarrow \infty$ as $k \rightarrow \infty$.
The result now follows from selecting Möbius parametrizations $\Phi_{i_{k}}$ with disjoint images and a function $u \in X_{0}^{0, p}(M)$ with $\Phi_{i_{k}}^{*} u=u_{k}$ on $B_{1 / 2}^{\mathbb{H}}$. The argument above shows that if $v \in X_{0}^{0, p}(M ; \mathbb{R})$ is locally Hölder continuous and if $\|u-v\|_{X_{0}^{0, p}(M)}$ is sufficiently small then $\|v\|_{C_{0}^{0, \alpha}(M)}=\infty$. \(\square\)
A.3. Interpolation. We rapidly review some facts from complex interpolation theory from which, unless otherwise noted, can be found in [Tri10]. An interpolation couple is a pair $\left(X_{0}, X_{1}\right)$ of Banach spaces that are continuously embedded subspaces of a common Hausdorff topological vector space. For any $0<\theta<1$ there is an interpolation Banach space $[X, Y]_{\theta}$ that satisfies continuous inclusions
$$X_{0} \cap X_{1} \subset\left[X_{0}, X_{1}\right]_{\theta} \subset X_{0}+X_{1}$$
where $X_{0} \cap X_{1}$ and $X_{0}+X_{1}$ are endowed with the natural optimal topologies such that each inclusion $X_{0} \cap X_{1} \hookrightarrow X_{i} \hookrightarrow X_{0}+X_{1}$ is continuous. Moreover
$$\|x\|_{\left[X_{0}, X_{1}\right]_{\theta}} \leq\|x\|_{X_{0}}^{1-\theta}\|x\|_{X_{1}}^{\theta}$$
for all $x \in X_{0} \cap X_{1}$.
If ( $X_{0}, X_{1}$ ) and ( $Y_{0}, Y_{1}$ ) are interpolation couples and $T_{i}: X_{i} \rightarrow Y_{i}, i=0,1$, are continuous linear maps with $T_{0}=T_{1}$ on $X_{0} \cap X_{1}$ then we have an associated continuous linear map $T:\left[X_{0}, X_{1}\right]_{\theta} \rightarrow\left[Y_{0}, Y_{1}\right]_{\theta}$ for all $\theta \in(0,1)$.
Given a Banach space $X$, let $c X$ be the same set $X$ with its norm scaled by $c$. If $X$ and $Y$ are Banach spaces and $X^{\prime}=a X_{1}$ and $Y^{\prime}=b Y$ for $a, b>0$ then $\left[X^{\prime}, Y^{\prime}\right]_{\theta}=a^{1-\theta} b^{\theta}[X, Y]$; see [Tri76] Lemma 5.

Given a sequence $Y=\left\{Y_{j}\right\}_{j=1}^{\infty}$ of Banach spaces let $\ell^{p}\left(\left\{Y_{j}\right\}_{j=1}^{\infty}\right)$ be the set of sequences $y \in \Pi Y_{j}$ such that
$$\sum_{j}\left\|y_{j}\right\|_{Y_{j}}^{p}<\infty .$$
This is a Banach space with the obvious norm. If $X=\left\{X_{j}\right\}_{j=1}^{\infty}$ and $Y=\left\{Y_{j}\right\}_{j=1}^{\infty}$ are sequences of Banach spaces, $1<p_{1}, p_{2}<\infty$ and $0<\theta<1$ then
$$\left[\ell^{p_{1}}(X), \ell^{p_{2}}(Y)\right]_{\theta}=\ell^{p}\left([X, Y]_{\theta}\right)$$
where $(1 / p)=(1-\theta)\left(1 / p_{1}\right)+\theta\left(1 / p_{2}\right)$ and where $[X, Y]_{\theta}$ is the sequence of spaces with elements $\left([X, Y]_{\theta}\right)_{j}=\left[X_{j}, Y_{j}\right]_{\theta}$.
The following interpolation theorem for weighted Bessel potential spaces is modeled on [Tri76] Theorem 3 for weighted function spaces on Euclidean $\mathbb{R}^{n}$.

Theorem A.7. Let $E$ be a tensor bundle over $\bar{M}$. Consider spaces $H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)$ with $s_{1}, s_{2} \in \mathbb{R}, 1<p_{1}, p_{2}<\infty$, and $\delta_{1}, \delta_{2} \in \mathbb{R}$. Let $\theta \in(0,1)$ and let
$$\begin{aligned}
s & =(1-\theta) s_{1}+\theta s_{2} \\
p & =(1-\theta) \frac{1}{p_{1}}+\theta \frac{1}{p_{2}} \\
\delta & =(1-\theta) \delta_{1}+\theta \delta_{2} .
\end{aligned}$$
Then
$$\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta}=H_{\delta}^{s, p}(M ; E) .$$
Proof. For simplicity we treat the case $E=\mathbb{R}$; the general case is proved verbatim with some additional notation needed to denote spaces of vector-valued functions over $\mathbb{R}^{n}$.

For the moment fix $t, \sigma \in \mathbb{R}$ and $1<p<\infty$. For $j \in \mathbb{N}$ define
$$H_{\sigma,(j)}^{t, q}\left(\mathbb{R}^{n}\right)=\rho_{j}^{-\sigma} H^{t, q}\left(\mathbb{R}^{n}\right)$$
and let
$$Z_{\sigma}^{t, q}=\ell^{q}\left(\left\{H_{\sigma,(j)}^{t, q}\left(\mathbb{R}^{n}\right)\right\}_{j=1}^{\infty}\right) .$$
Define $S_{j}: H_{\sigma}^{t, q}(M) \rightarrow H_{\sigma,(j)}^{t, q}\left(\mathbb{R}^{n}\right)$ by
$$S_{j}(u)=\chi \Phi_{j}^{*} u .$$
A straightforward computation shows
$$u \mapsto\left(S_{1} u, S_{2} u, \ldots\right)$$
defines a continuous linear map $S: H_{\sigma}^{t, q}(M) \rightarrow Z_{\sigma}^{t, q}$.
Let $\eta$ be a cutoff function that equals 1 on the support of $\chi$ and equals 0 outside $B_{2}$ and define
$$T: Z_{\sigma}^{t, q} \rightarrow H_{\sigma}^{t, q}(M)$$
by
$$T\left(w_{1}, w_{2}, \ldots\right)=\sum_{i} \Phi_{i, *}\left(\eta w_{i}\right) .$$
Lemma A. 2 implies $T$ is continuous. Since $\eta \chi=\chi$,
$$(T \circ S)(u)=\bar{\chi} \cdot u,$$
where $\bar{\chi}$ is defined in equation (A.7). Finally let $R u=\bar{\chi}^{-1} \cdot T u$, which is again a continuous linear map
$$Z_{\sigma}^{t, q} \rightarrow H_{\sigma}^{t, q}(M)$$
and moreover $R \circ S=\mathrm{Id}$.
We now apply interpolation to the maps $R$ and $S$. From [Tri76] Lemma 6, $R$ and $S$ determine continuous linear maps
$$\begin{aligned}
& S:\left[H_{\delta_{1}}^{S_{1}, p_{1}}(M), H_{\delta_{2}}^{S_{2}, p_{2}}(M)\right]_{\theta} \rightarrow\left[Z_{\delta_{1}}^{S_{1}, p_{1}}, Z_{\delta_{2}}^{S_{2}, p_{2}}\right]_{\theta} \\
& R:\left[Z_{\delta_{1}}^{S_{1}, p_{1}}, Z_{\delta_{2}}^{S_{2}, p_{2}}\right]_{\theta} \rightarrow\left[H_{\delta_{1}}^{S_{1}, p_{1}}(M), H_{\delta_{2}}^{S_{2}, p_{2}}(M)\right]_{\theta}
\end{aligned}$$
such that $R \circ S=\mathrm{Id}$.
From interpolation of vector-valued $\ell^{q}$ spaces we find
$$\begin{aligned}
{\left[Z_{\delta_{1}}^{S_{1}, p_{1}}, Z_{\delta_{2}}^{S_{2}, p_{2}}\right]_{\theta} } & =\left[\ell^{p_{1}}\left(\left\{H_{\delta_{1},(j)}^{S_{1}, p_{1}}\left(\mathbb{R}^{n}\right)\right\}_{j}\right), \ell^{p_{2}}\left(\left\{H_{\delta_{2},(j)}^{S_{2}, p_{2}}\left(\mathbb{R}^{n}\right)\right\}_{j}\right)\right]_{\theta} \\
& =\ell^{p}\left(\left\{\left[H_{\delta_{1},(j)}^{S_{1}, p_{1}}\left(\mathbb{R}^{n}\right), H_{\delta_{2},(j)}^{S_{2}, p_{2}}\left(\mathbb{R}^{n}\right)\right]_{\theta}\right\}_{p}\right) .
\end{aligned}$$
Moreover,
$$\begin{aligned}
{\left[H_{\delta_{1},(j)}^{s_{1}, p_{1}}\left(\mathbb{R}^{n}\right), H_{\delta_{2},(j)}^{s_{2}, p_{2}}\left(\mathbb{R}^{n}\right)\right]_{\theta} } & =\left[\rho_{j}^{-\delta_{1}} H^{s_{1}, p_{1}}\left(\mathbb{R}^{n}\right), \rho_{j}^{-\delta_{2}} H^{s_{2}, p_{2}}\left(\mathbb{R}^{n}\right)\right]_{\theta} \\
& =\rho_{j}^{-\left[(1-\theta) \delta_{1}+\theta \delta_{2}\right]}\left[H^{s_{1}, p_{1}}\left(\mathbb{R}^{n}\right), H^{s_{2}, p_{2}}\left(\mathbb{R}^{n}\right)\right]_{\theta} \\
& =\rho_{j}^{-\delta} H^{s, p}\left(\mathbb{R}^{n}\right) .
\end{aligned}$$
That is, $\left[Z_{\delta_{1}}^{S_{1}, p_{1}}, Z_{\delta_{2}}^{S_{2}, p_{2}}\right]_{\theta}=Z_{\delta}^{s, p}$.
Now $S:\left[H_{\delta_{1}}^{S_{1}, p_{1}}(M), H_{\delta_{2}}^{S_{2}, p_{2}}(M)\right]_{\theta} \rightarrow Z_{\delta}^{s, p}$ is an isomorphism onto its image since it admits a continuous inverse, namely the restriction of $R$. Hence
$$\|u\|_{\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M), H_{\delta_{2}}^{s_{2}, p_{2}}(M)\right]_{\theta}}^{p} \sim \sum_{i} \rho_{i}^{-\delta p}\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}=\|u\|_{H_{\delta}^{s, p}(M)}^{p} .$$
Equation (A.15) establishes equivalence of norms, but leaves open the possibility that the interpolation space $\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M), H_{\delta_{2}}^{s_{2}, p_{2}}(M)\right]_{\theta}$ is a closed subspace of $H_{\delta}^{s, p}(M)$. However, Proposition A. 5 shows that the smooth compactly supported functions are contained in $H_{\delta_{1}}^{s_{1}, p_{1}}(M) \cap H_{\delta_{2}}^{s_{2}, p_{2}}(M) \subset\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M), H_{\delta_{2}}^{s_{2}, p_{2}}(M)\right]_{\theta}$ and are dense in $H_{\delta}^{s, p}(M)$. \(\square\)

Gicquaud-Sakovtich spaces are more technical from the perspective of interpolation than the weighted Bessel potential spaces are because they are based on $\ell^{\infty}$ rather than $\ell^{p}$ with $1<p<\infty$. The following partial result suffices for the purposes of our work.

Proposition A.8. Let $E$ be a tensor bundle over $\bar{M}$. Suppose $\left(A_{0}, A_{1}\right)$ is an interpolation couple and that $T$ is a linear map
$$T: A_{0}+A_{1} \rightarrow X_{\delta_{0}}^{S_{0}, p_{0}}(M ; E)+X_{\delta_{1}}^{S_{1}, p_{1}}(M ; E)$$
for some $s_{0}, s_{1} \in \mathbb{R}, \delta_{0}, \delta_{1} \in \mathbb{R}$, and $1<p_{0}, p_{1}<\infty$. If $T$ restricts to continuous maps $T_{k}: A_{k} \rightarrow X_{\delta_{k}}^{S_{k}, p_{k}}(M ; E)$ for $k=0,1$, then for each $\theta \in(0,1)$, then $T$ also restricts to a continuous map
$$T_{\theta}:\left[A_{0}, A_{1}\right]_{\theta} \rightarrow X_{\delta}^{s, p}(M ; E),$$
where $s, p$ and $\delta$ are given by equations (A.14). Moreover,
$$\left\|T_{\theta}\right\| \leq\left\|T_{0}\right\|^{1-\theta}\left\|T_{1}\right\|^{\theta}$$
with implicit constant independent of $T_{0}, T_{1}$.
Proof. Consider a preferred Möbius chart $\Phi_{i}$ and let
$$T_{(i)}=\chi \cdot\left(\Phi_{i}^{*} \circ T\right) .$$
Recall that if $Y$ is a normed space and $r>0$, the $r Y$ norm is $\|\cdot\|_{r Y}=r\|\cdot\|_{Y}$. Then $T_{(i)}$ determines continuous linear maps $A_{k} \rightarrow \rho_{i}^{-\delta_{k}} H^{s_{k}, p_{k}}\left(\mathbb{R}^{n}\right)$ for $k=0,1$ with norm bounded
by $\left\|T_{k}\right\|$; note that $H^{s_{k}, p_{k}}(\mathbb{R})$ denotes a space of vector-valued functions here. It therefore also determines a continuous linear map
$$\left[A_{0}, A_{1}\right]_{\theta} \rightarrow\left[\rho_{i}^{-\delta_{0}} H^{s_{0}, p_{0}}\left(\mathbb{R}^{n}\right), \rho_{i}^{-\delta_{1}} H^{s_{1}, p_{1}}\left(\mathbb{R}^{n}\right)\right]_{\theta}=\rho_{i}^{-\delta} H^{s, p}\left(\mathbb{R}^{n}\right)$$
with norm bounded by $\left\|T_{0}\right\|^{1-\theta}\left\|T_{1}\right\|^{\theta}$. But the norm of $T:\left[A_{0}, A_{1}\right]_{\theta} \rightarrow X_{\delta}^{s, p}(M)$ is exactly the supremum of all such norms. \(\square\)
A.4. Duality. Let $g_{\mathbb{E}}$ be the Euclidean metric on $\mathbb{R}^{n}$. The $L^{2}$ inner product
$$\langle v, u\rangle_{\left(\mathbb{R}^{n}, g_{\mathbb{E}}\right)}=\int_{\mathbb{R}^{n}} v u d V_{g_{\mathbb{B}}}$$
on smooth, compactly supported functions $v$ and $u$ extends to a continuous bilinear form on $H^{-s, p^{*}}\left(\mathbb{R}^{n}\right) \times H^{s, p}\left(\mathbb{R}^{n}\right)$ where $\frac{1}{p}+\frac{1}{p^{*}}=1$, and the map $v \mapsto\langle v, \cdot\rangle_{\mathbb{R}^{n}}$ is an isomorphism between $H^{-s, p}\left(\mathbb{R}^{n}\right)$ and $\left(H^{s, p}\left(\mathbb{R}^{n}\right)\right)^{*}$. In this section we establish analogous results for weighted Bessel potential spaces. Because Gicquaud-Sakovich spaces are based on $\ell^{\infty}$ their duality theory is more complex and is beyond the scope of our work.
Let $\check{g}$ denote a metric on $M$ with smooth compactification $\rho^{2} \check{g}$ on $\bar{M}$ and let $d V_{\check{g}}$ be its volume element. We use the notation
$$\langle v, u\rangle_{(M, \check{g})}=\int_{M} v u d V_{\check{g}}$$
for smooth compactly supported functions $v$ and $u$ on $M$. In this section we show that $\langle\cdot, \cdot\rangle_{(M, \check{g})}$ induces a corresponding isomorphism between $H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R})$ and $\left(H_{\delta}^{s, p}(M ; \mathbb{R})\right)^{*}$. Theorem A. 19 in §A. 5 builds on this result to obtain a duality statement for general geometric tensor bundles and less regular metrics.

We begin by showing the map $\langle\cdot, \cdot\rangle_{(M, \check{g})}$ is well defined between nominally dual weighted spaces.