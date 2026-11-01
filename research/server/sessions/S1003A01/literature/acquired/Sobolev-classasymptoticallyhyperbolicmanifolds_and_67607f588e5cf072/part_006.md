---
retention_scope: session
part: 6
total_parts: 7
---

[Part 6/7 of: Sobolev-classasymptoticallyhyperbolicmanifolds and]

Lemma A.9. Let $s, \delta \in \mathbb{R}$ and $1<p<\infty$ and let $p^{*}$ be the dual exponent of $p$. Then
$$\langle v, u\rangle_{(M, \check{g})} \lesssim\|v\|_{H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R})}\|u\|_{H_{\delta}^{s, p}(M ; \mathbb{R})}$$
for all $u, v \in C_{\mathrm{c}}^{\infty}(M ; \mathbb{R})$ and hence $\langle\cdot, \cdot\rangle_{(M, \check{g})}$ extends to a continuous bilinear form on $H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R}) \times H_{\delta}^{s, p}(M ; \mathbb{R})$.

Proof. For each Möbius parametrization $\Phi_{i}$ define $\omega_{i}$ by $\Phi_{i}^{*} d V_{\check{g}}=\omega_{i} d V_{g_{\mathrm{E}}}$. Since $g$ admits a smooth compactification, an easy computation shows that for any $k \in \mathbb{N}$,
$$\sup _{i}\left\|\omega_{i}\right\|_{C^{k}\left(B_{2}\right)}<\infty, \quad \sup _{i}\left\|\left(\omega_{i}\right)^{-1}\right\|_{C^{k}\left(B_{2}\right)}<\infty .$$
The usual change of variables formula shows that if $u$ and $v$ are smooth functions supported in $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right)$ then
$$\langle v, u\rangle_{(M, \check{g})}=\left\langle\Phi_{i}^{*} v, \omega_{i} \Phi_{i}^{*} u\right\rangle_{\left(\mathbb{R}^{n}, g_{\mathrm{E}}\right)} .$$

Suppose $u$ and $v$ are smooth compactly supported functions. Let $\eta$ be a cutoff function on $B_{2}^{\mathbb{H}}$ that equals 1 on the support of $\chi$, and pick an integer $k>|s|$. Then recalling the function $\bar{\chi}$ from equation (A.7) we find
$$\begin{aligned}
\left|\langle v, u\rangle_{(M, \check{g})}\right| & =\left|\left\langle\bar{\chi} v,(\bar{\chi})^{-1} u\right\rangle_{(M, \check{g})}\right| \\
& \leq \sum_{i}\left|\left\langle\chi_{i} v,(\bar{\chi})^{-1} u\right\rangle_{(M, \check{g})}\right| \\
& =\sum_{i}\left|\left\langle\chi \Phi_{i}^{*} v, \omega_{i} \eta \Phi_{i}^{*}\left((\bar{\chi})^{-1} u\right)\right\rangle_{\left(\mathbb{R}^{n}, g_{\mathbb{B}}\right)}\right| \\
& \lesssim \sum_{i}\left\|\chi \Phi_{i}^{*} v\right\|_{H^{-s, p^{*}}\left(\mathbb{R}^{n}\right)}\left\|\omega_{i}\right\|_{C^{k}\left(B_{2}\right)}\left\|\eta \Phi_{i}^{*}\left((\bar{\chi})^{-1} u\right)\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \\
& \left.\leq\|v\|_{H_{-\delta}^{-s, p^{*}}}\left[\sum_{i} \rho_{i}^{-\delta p} \| \eta \Phi_{i}^{*}\left((\bar{\chi})^{-1}\right) u\right) \|_{H^{s, p}\left(\mathbb{R}^{n}\right)}\right]^{1 / p}
\end{aligned}$$
where we have used Sobolev duality on $\mathbb{R}^{n}$ along with uniform $C^{k}$ bounds on $\omega_{i}$. To finish the proof it suffices to show that
$$\left[\sum_{i} \rho_{i}^{-\delta p}\left\|\eta \Phi_{i}^{*}\left((\bar{\chi})^{-1} u\right)\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p}\right]^{1 / p} \lesssim\|u\|_{H_{\delta}^{s, p}(M)} .$$
But this follows from Lemma A. 3 and our earlier observation that $u \mapsto(\bar{\chi})^{-1} u$ is continuous on $H_{\delta}^{s, p}(M)$. \(\square\)

Theorem A.10. Let $s, \delta \in \mathbb{R}$ and $1<p<\infty$ and let $p^{*}$ be the Lebesgue dual exponent of $p$. The map
$$v \mapsto\langle v, \cdot\rangle_{(M, \check{g})}$$
is an isomorphism between $H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R})$ and $\left(H_{\delta}^{s, p}(M ; \mathbb{R})\right)^{*}$.
Proof. Suppose $F \in\left(H_{\delta}^{s, p}(M)\right)^{*}$. Fix $i \in \mathbb{N}$ for the moment and define $F_{i} \in\left(H^{s, p}\left(\mathbb{R}^{n}\right)\right)^{*}$ by
$$F_{i}(u)=F\left(\left(\Phi_{i}\right)_{*}(\chi u)\right)=F\left(\chi_{i}\left(\Phi_{i}\right)_{*} u\right) .$$
Since $F_{i}$ is supported on $B_{r}^{\mathbb{H}}$ for some $r<2$ there exists $w_{i} \in H^{-s, p^{*}}\left(\mathbb{R}^{n}\right)$ supported on $B_{r^{\prime}}^{\mathbb{H}}$, where $r^{\prime}<2$, such that
$$F_{i}(u)=\left\langle w_{i}, u\right\rangle_{\left(\mathbb{R}^{n}, g_{\mathbb{E}}\right)}$$
for all $u \in H^{s, p}\left(\mathbb{R}^{n}\right)$. Using the usual isomorphism between $H^{-s, p *}\left(\mathbb{R}^{n}\right)$ and $\left(H^{s, p}\left(\mathbb{R}^{n}\right)\right)^{*}$ there exists a constant $c>0$ arising from the isomorphism and a function $z_{i} \in H^{s, p}\left(\mathbb{R}^{n}\right)$ such that $\left\|z_{i}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}=1$ and such that
$$\left\langle w_{i}, z_{i}\right\rangle_{\left(\mathbb{R}^{n}, g^{\mathbb{E}}\right)} \geq c\left\|w_{i}\right\|_{H^{-s, p^{*}}\left(\mathbb{R}^{n}\right)} .$$
Moreover, since $w_{i}$ is supported in $B_{r^{\prime}}^{\mathbb{H}}$ we can assume, after multiplication by a cutoff function depending only on $r^{\prime}$, that $z_{i}$ is supported in $B_{r^{\prime \prime}}^{\mathbb{H}}$ for some $r^{\prime \prime}$, and that the functions
$z_{i}$ remain uniformly bounded in $H^{s, p}\left(\mathbb{R}^{n}\right)$. As in the proof of Lemma A. 9 define $\omega_{i}$ by $\Phi_{i}^{*} d V_{\check{g}}=\omega_{i} d V_{g_{\mathbb{B}}}$ and let
$$\begin{aligned}
& v_{i}=\left(\Phi_{i}\right)_{*}\left(\omega_{i}^{-1} w_{i}\right) \\
& u_{i}=\left(\Phi_{i}\right)_{*} z_{i} .
\end{aligned}$$
Recalling that $\omega_{i}^{-1}$ admits the uniform bounds (A.16) we find that $v_{i}$ and $u_{i}$ are well-defined elements of $H_{0}^{-s, p^{*}}(M)$ and $H_{0}^{s, p}(M)$ respectively.
Partition $\mathbb{N}$ into sets finitely many sets $N_{a}$ such that if $i, j \in N_{a}$ with $i \neq j$ then $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right) \cap$ $\Phi_{j}\left(B_{2}^{\mathbb{H}}\right)=\emptyset$; the existence of such a partition is an easy consequence of local finiteness. Fix a partition index $a$ and let $\left\{b_{i}\right\}_{i \in N_{a}}$ be a sequence of real numbers such that $\sum_{i \in N_{a}}\left|b_{i}\right|^{p} \leq 1$. Let $u_{(a)}=\sum_{i \in N_{a}} b_{i} \rho_{i}^{\delta} u_{i}$. Then
$$\sum_{i \in N_{a}} \rho_{i}^{-\delta p}\left\|b_{i} \rho_{i}^{\delta} \Phi_{i}^{*} u_{i}\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \lesssim \sum_{i \in N_{a}}\left|b_{i}\right|^{p} \lesssim 1$$
where we have used uniform $H^{s, p}\left(\mathbb{R}^{n}\right)$ bounds for the functions $z_{i}=\Phi_{i}^{*} u_{i}$. Lemma A. 2 implies that $u_{(a)}$ belongs to $H_{\delta}^{s, p}\left(\mathbb{R}^{n}\right)$ and its norm is bounded independent of the choice of sequence $\left\{b_{j}\right\}$. From continuity of the map $F$ and this uniform bound we find
$$\begin{aligned}
\|F\| z F\left(u_{(a)}\right) & =F\left(\sum_{i \in N_{a}} \chi_{i} \rho_{i}^{\delta} b_{i} u_{i}\right) \\
& =\sum_{i \in N_{a}} \rho_{i}^{\delta} b_{i} F_{i}\left(\Phi_{i}^{*} u_{i}\right) \\
& =\sum_{i \in N_{a}} \rho_{i}^{\delta} b_{i}\left\langle w_{i}, z_{i}\right\rangle_{\left(\mathbb{R}^{n}, g^{\mathbb{B}}\right)} \\
& \geq \sum_{i \in N_{a}} \rho_{i}^{\delta} b_{i} \alpha\left\|w_{i}\right\|_{H^{-s, p^{*}}\left(\mathbb{R}^{n}\right)},
\end{aligned}$$
where the second equality relies on the fact that we only sum over $i \in N_{a}$. Since the choice of sequence $\left\{b_{i}\right\} \in \ell^{p}$ with norm less than one is arbitrary we conclude $\left\{\rho_{i}^{\delta}\left\|w_{i}\right\|_{H^{-s, p}\left(\mathbb{R}^{n}\right)}\right\}_{i \in N_{a}} \in$ $\ell^{p^{*}}$. Recall that $v_{i}=\left(\Phi_{i}\right)_{*}\left(\omega_{i}^{-1} w_{i}\right)$. The uniform $C^{k}$ bounds on the functions $\left(\omega_{i}\right)^{-1}$ and Lemma A. 2 imply $v_{(a)}:=\sum_{i \in N_{a}} v_{i} \in H_{-\delta}^{-s, p^{*}}(M)$ and consequently $v$ defined by
$$v=\sum_{a} v_{(a)}=\sum_{i} v_{i}$$
also belongs to $H_{-\delta}^{-s, p^{*}}(M)$. Moreover, for any $u \in H_{\delta}^{s, p}(M)$
$$\begin{aligned}
\langle v, u\rangle_{(M, \check{g})} & =\sum_{i}\left\langle v_{i}, u\right\rangle_{(M, \check{g})} \\
& =\sum_{i}\left\langle\omega_{i}^{-1} w_{i}, \eta \omega_{i} \Phi_{i}^{*} u\right\rangle_{\left(\mathbb{R}^{n}, g_{\mathbb{E}}\right)} \\
& =\sum_{i} F\left(\chi_{i} u\right)=F(\bar{\chi} u)
\end{aligned}$$
where $\eta$ is a cutoff function on $B_{2}^{\mathbb{H}}$ with $\eta \chi=1$ and with $\eta w_{i}=w_{i}$ for all $i$. But then $\bar{\chi}^{-1} v \in H_{\delta}^{-s, p^{*}}(M ; \mathbb{R})$ and
$$\left\langle\bar{\chi}^{-1} v, u\right\rangle_{(M, \check{g})}=F(u)$$
for all $u \in H_{\delta}^{s, p}(M)$.
We have now established surjectivity of the map in (A.17). To show the map is injective, suppose $v \neq 0$. Then $\chi \Phi_{i}^{*} v \neq 0$ for some $i$ and we can find $w \in H^{s, p}\left(\mathbb{R}^{n}\right)$, supported in $B_{2}$, such that $\left\langle\chi \Phi_{i}^{*} v, w\right\rangle_{\mathbb{R}^{n}} \neq 0$. Let $u=\left(\Phi_{i}\right)_{*}\left(\left(\omega_{i}\right)^{-1} \chi w\right)$. Then
$$\langle v, u\rangle_{(M, \check{g})}=\left\langle\chi \Phi_{i}^{*} v, \omega_{i}\left(\omega_{i}\right)^{-1} w\right\rangle_{\left(\mathbb{R}^{n}, g_{\mathbb{B}}\right)}=\left\langle\Phi_{i}^{*} v, \chi u\right\rangle_{\mathbb{R}^{n}} \neq 0 .$$
Thus the map is a linear isomorphism (A.17) and its continuity follows from Lemma A.9. \(\square\)
A.5. Geometric tensor bundles. Until this point we have only considered tensor bundles $E=T^{k_{1}, k_{2}} M$ and now turn our attention to geometric tensor bundles, which are subbundles of tensor bundles and which potentially depend on a metric for their definition. In fact, subbundles such as the symmetric tensors in $T^{2,0} \bar{M}$ which are associated with $G L(n ; \mathbb{R})$ representations could have largely been treated earlier with very minor modifications to the proofs. In the general case, however, the regularity of the metric plays a role in the results. Moreover, even for tensor bundles, the generalization of the duality result Theorem A. 10 requires a choice of (perhaps not smooth) reference metric. Therefore, throughout this section we fix a metric $h \in X_{0}^{s_{0}, p_{0}}(M)$ with $1<p_{0}<\infty$ and $s_{0}>n / p_{0}$ (and consequently is locally Hölder continuous) that admits a compactification $\rho^{2} h$ having an extension to a continuous metric on $\bar{M}$. We also fix a particular geometric tensor bundle $E$ over $\bar{M}$ with ambient tensor bundle F. For technical reasons we assume additionally that $s_{0} \geq 1$. In the event that $E$ happens to be a subbundle associated with a $G L(n ; \mathbb{R})$ representation (and therefore does not require a metric for its definition) we can simply select an arbitrary metric $h$ with smooth conformal compactification for use in the constructions below.

The regularity of the metric restricts the permissible regularity classes of sections of $E$. Using the notation of §8, let $\mathcal{S}_{0}^{s_{0}, p_{0}}$ be the set of pairs $(s, p) \in \mathbb{R} \times(1, \infty)$ satisfying
$$\begin{gathered}
-s_{0} \leq s \leq s_{0} \\
\frac{1}{p_{0}}-\frac{s}{n} \leq \frac{1}{p}-\frac{s}{n} \leq \frac{1}{p_{0}^{*}}+\frac{s}{n} .
\end{gathered}$$
The significance of these conditions comes from multiplication in Sobolev spaces: since $s_{0}>n / p_{0}$, multiplication is continuous $H^{s_{0}, p_{0}}\left(\mathbb{R}^{n}\right) \times H^{s, p}\left(\mathbb{R}^{n}\right) \rightarrow H^{s, p}\left(\mathbb{R}^{n}\right)$ when $(s, p) \in$ $\mathcal{S}_{0}^{s_{0}, p_{0}}$. Similarly, Proposition 3.11. shows that when $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$, multiplication is continuous
$$\begin{aligned}
& H_{\delta}^{s, p}(M ; \mathbb{R}) \times X_{0}^{s_{0}, p_{0}}(M ; F) \rightarrow H_{\delta}^{s, p}(M ; F), \\
& X_{\delta}^{s, p}(M ; \mathbb{R}) \times X_{0}^{s_{0}, p_{0}}(M ; F) \rightarrow X_{\delta}^{s, p}(M ; F) .
\end{aligned}$$

Definition A.11. Suppose $(s, p) \in S_{0}^{s_{0}, p_{0}}$ and $\delta \in \mathbb{R}$. Let $E$ be a geometric tensor bundle over $\bar{M}$ with ambient tensor bundle $F$. The space $H_{\delta}^{s, p}(M ; E)$ is the subspace of $H_{\delta}^{s, p}(M ; F)$ consisting of the elements $u$ for which there exist finitely many sections $\sigma_{\alpha}$ in $X_{0}^{s_{0}, p_{0}}(M ; F)$ that are also (continuous) sections of $E$, along with coefficients $u_{\alpha} \in$ $H_{\delta}^{s, p}(M ; \mathbb{R})$, such that
$$u=\sum_{\alpha} u_{\alpha} \sigma_{\alpha} .$$
The space $X_{\delta}^{s, p}(M ; E)$ is defined similarly, with coefficients in $X_{\delta}^{s, p}(M ; \mathbb{R})$. The spaces $H_{\delta}^{s, p}(M ; E)$ and $X_{\delta}^{s, p}(M ; E)$ inherit their norms from the ambient spaces $H_{\delta}^{s, p}(M ; F)$ and $X_{\delta}^{s, p}(M ; F)$, respectively.

The main strategy for the remainder of this section is to find a single collection of basis sections in $X_{0}^{s, p}(M ; E)$ and then apply earlier results to coefficients with respect to this basis. The basis sections themselves are obtained using well-controlled local orthonormal frames for the tangent bundle, and to build these we start with a local coordinate version of the frame construction. Let $\operatorname{Sym}_{+}^{2}\left(\mathbb{R}^{n}\right)$ denote the the set of symmetric, positive definite $n \times n$ matrices which we identify with the set of metrics on $\mathbb{R}^{n}$. Let GS : $\operatorname{Sym}_{+}^{2}\left(\mathbb{R}^{n}\right) \times$ $\operatorname{GL}(n, \mathbb{R}) \rightarrow \operatorname{GL}(n, \mathbb{R})$ be the map taking a metric $g$ and a matrix $A$ to the matrix with columns consisting of a $g$-orthonormal frame obtained via the Gram-Schmidt procedure starting at the columns of $A$. We extend GS to sections of metrics and frames in the obvious way and use the same notation.
The following sequence of results are used to build well controlled local frames for $E$ using GS.

Lemma A.12. Suppose $1<p<\infty$ and $s \geq 1$ with $s>n / p$, and that $U \subset \mathbb{R}^{n}$ is open and bounded. Let $I=[a, b]$ with $0<a<b$, and let
$$Z_{I}=\left\{u \in H^{s, p}(U): u(x) \in I \text { for all } x \in U\right\} .$$
For each $a \in \mathbb{R}$ the map $u \mapsto u^{a}$ is globally Lipschitz continuous as a map $Z_{I} \rightarrow H^{s, p}(U)$.
Proof. We first recall a fact about nonlinearities and Sobolev spaces. A straightforward bootstrap using the inequalities $s>n / p$ and $s \geq 1$ shows that if $F: \mathbb{R} \rightarrow \mathbb{R}$ is smooth and $u \in H^{s, p}(U)$, then $F(u) \in H^{s, p}(U)$ with its norm is controlled by a bound depending on $F$ and $\|u\|_{H^{s, p}(U)}$. Alternatively, this fact is also a consequence of the more sophisticated estimates of [Sic96, Theorem 1] and [Tay91, Section 3.1].

Suppose $u_{0}, u_{1} \in Z_{\varepsilon, K}$ and let $\delta u=u_{1}-u_{0}$. Then
$$\left(u_{1}\right)^{a}-\left(u_{0}\right)^{a}=\left(u_{0}\right)^{a}\left[\left(1+\frac{\delta u}{u_{0}}\right)^{a}-1\right]=\left(u_{0}\right)^{a-1} G_{a}\left(\frac{\delta u}{u_{0}}\right) \delta u$$
where $G_{a}$ is a smooth function on $\mathbb{R}_{>0}$. Our initial remarks about nonlinearities show that the $H^{s, p}(U)$ norms of $u_{0}, u_{0}^{a-1}, \delta u / u_{0}$ and $G_{a}\left(u / u_{0}\right)$ are all uniformly bounded by a constant depending on $a$ and $I$, and the result follows the fact that $H^{s, p}(U)$ is an algebra. \(\square\)

Lemma A.13. Let $U \subset \mathbb{R}^{n}$ be open and bounded, let $1<p<\infty$, and let $s \in \mathbb{R}$ with $s \geq 1$ and $s>n / p$. Let $\varepsilon>0$ and $K>0$ and define
$$\begin{aligned}
Z_{K}=\left\{(g, A): g \in H^{s, p}(U ;\right. & \left.\operatorname{Sym}_{+}^{2}\left(\mathbb{R}^{n}\right)\right), A \in H^{s, p}(U ; G L(n ; \mathbb{R})) \\
& \left.\operatorname{det} g \geq \varepsilon, \operatorname{det} A \geq \varepsilon,\|g\|_{H^{s, p}(U)} \leq K,\|A\|_{H^{s, p}(U)} \leq K\right\} .
\end{aligned}$$
Then $G S: Z_{\varepsilon, K} \rightarrow H^{s, p}(U ; \operatorname{GL}(n, \mathbb{R}))$ and is globally Lipschitz continuous. Moreover the map $(g, A) \mapsto(G S(g, A))^{-1}$ similarly determines a globally Lipschitz map $Z_{K} \rightarrow$ $H^{s, p}(U ; \operatorname{GL}(n, \mathbb{R}))$.

Proof. The coefficients of $\operatorname{GS}(g, A)$ are constructed iteratively from those of $g$ and $A$ using addition, multiplication, and the map $x \mapsto x^{-1 / 2}$. Since $\{(g(x), A(x)): x \in U\}$ is contained in a compact subset of $\operatorname{Sym}_{+}^{2} \times G L(n ; \mathbb{R})$ we can find a compact interval $I$ of positive real numbers, depending only on $\varepsilon$ and $K$, such that each application of $x \mapsto x^{-1 / 2}$ needed to compute $\mathrm{GS}(g(x), A(x))$ for all $x \in U$ involves an argument in $I$. Hence using Lemma A.12, and the fact that $H^{s, p}(U)$ is an algebra, we find that $\mathrm{GS}: Z_{\varepsilon, K} \rightarrow H^{s, p}(U ; G L(n ; \mathbb{R}))$ and indeed globally Lipschitz continuous. Moreover, $\{\mathrm{GS}(g(x), A(x)): x \in U\}$ is contained in a compact subset of $\operatorname{GL}(n, \mathbb{R})$ determined by $\varepsilon$ and $K$, and therefore there exist bounds $C \geq c>0$, depending only on $\varepsilon$ and $K$, such that $c \leq \operatorname{det} \operatorname{GS}(g(x), A(x)) \leq C$ for all $x \in U$; recall that the Gram Schmidt procedure is orientation preserving. Lemma A.12, and the fact that $H^{s, p}(U)$ is an algebra, then imply that $g \mapsto(\operatorname{GS}(g, A))^{-1}$ is also globally Lipschitz continuous. \(\square\)

The previous lemma allows us to find a local orthonormal frame for $E$ with support in the image of each Möbius parametrization.

Lemma A.14. Let $d$ be the fiber dimension of $E$, and recall the cutoff function $\chi$ used in (A.1). For each Möbius parametrization $\Phi_{i}$ there exist sections $\sigma_{\alpha, i} \in X^{s_{0}, p_{0}}(M ; E)$, $1 \leq \alpha \leq d$, supported in $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right)$ such that for each $x$ in a neighborhood of the support of $\left(\Phi_{i}\right)_{*} \chi$, the collection $\left\{\sigma_{\alpha, a}(x)\right\}_{\alpha}$ is an $h$-orthonormal basis for the fiber of $E$ over $x$. Moreover, $\left\|\sigma_{\alpha, i}\right\|_{X_{0}^{s_{0}, p_{0}}(M ; E)}$ is bounded independent of $\alpha$ and $i$.

Proof. The collection of metrics $\Phi_{i}^{*} h$ are uniformly bounded in $H^{s, p}\left(B_{r}^{\mathbb{H}}\right)$. Moreover, using the fact that $h$ has a continuous compactification, the argument of Lemma 8.5 shows that $\operatorname{det}\left(\Phi_{i}^{*} h\right)$ is uniformly bounded away from zero. So Lemma A. 13 implies that for each $i$ we can find a section of matrices $A_{i} \in H^{s_{0}, p_{0}}\left(B_{r}^{\mathbb{H}}\right)$, with columns consisting of an $h$ -orthonormal frame, such that the norms $\left\|A_{i}\right\|_{H^{s_{0}, p_{0}}\left(B_{r}^{\mathbb{H}}\right)}$ and $\left\|\left(A_{i}\right)^{-1}\right\|_{H^{s_{0}, p_{0}}\left(B_{r}^{\mathbb{H}}\right)}$ are uniformly bounded in $i$.

Let $\eta$ be a cutoff function supported in some $B_{r}^{\mathbb{H}}$, with $r<2$, that equals 1 in a neighborhood of the support of $\chi$. Let $\sigma_{\alpha}^{\mathbb{E}}, 1 \leq \alpha \leq d$ be a Euclidean orthonormal frame for the subspace of the tensor bundle over $\mathbb{R}^{n}$ associated with $E$. From the bounds on $A_{i}$ and $A_{i}^{*}$ we find that the sections $\left(A_{i}\right)_{*} \sigma_{\alpha}^{\mathbb{E}}$ induced from the tensor bundle automorphism determined by $A_{i}$ are bounded in $H^{s, p}\left(B_{r}^{\mathbb{H}}\right)$ independent of $i$ and $\alpha$. Lemma A. 2 implies that the sections
$\sigma_{\alpha, i}=\left(\Phi_{i}\right)_{*}\left(\eta\left(A_{i}\right)_{*} \sigma_{\alpha}^{\mathbb{E}}\right)$ are uniformly bounded in $X_{0}^{s, p}(M ; E)$. Since $\eta \chi=\chi$, for each $i$ the sections $\sigma_{\alpha, i}$ form a pointwise $h$-orthonormal frame for $x$ in the support of $\left(\Phi_{i}\right)_{*} \chi$. \(\square\)

As in the proof of Theorem A.10, partition $\mathbb{N}$ into finitely many sets $\left\{N_{a}\right\}$ with finite so that if if $i, j \in N_{a}$ and if $i \neq j$ then $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right) \cap \Phi_{j}\left(B_{2}^{\mathbb{H}}\right)=\emptyset$. Let $\chi_{(a)}=\bar{\chi}^{-1} \sum_{i \in N_{a}}\left(\Phi_{i}\right)_{*} \chi$ so that the collection $\chi_{(a)}$ is a partition of unity in $C_{0}^{k}\left(M ; \mathbb{R}^{n}\right)$ for any $k$. Similarly, for each bundle index $\alpha$ let $\sigma_{\alpha,(a)}=\sum_{i \in N_{a}} \sigma_{\alpha, i}$, so each $\sigma_{\alpha,(a)} \in X_{0}^{s_{0}, p_{0}}(M ; E)$. For each index $(\alpha,(a))$ we define projections
$$\pi_{\alpha,(a)}(u)=\left\langle\chi_{(a)} u, \sigma_{\alpha,(a)}\right\rangle_{h} .$$
Proposition 3.11 ensures that the projections are continuous $H_{\delta}^{s, p}(M ; F) \rightarrow H_{\delta}^{s, p}(M ; \mathbb{R})$ and $X_{\delta}^{s, p}(M ; F) \rightarrow X_{\delta}^{s, p}(M ; \mathbb{R})$ so long as $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$.

Lemma A.15. Suppose $\delta \in \mathbb{R}$ and $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$. If $u \in H_{\delta}^{s, p}(M ; E)$ or $u \in X_{\delta}^{s, p}(M ; E)$ then
$$u=\sum_{\alpha, a} \pi_{\alpha,(a)}(u) \sigma_{\alpha,(a)} .$$

Proof. Suppose that $w \in X_{0}^{s_{0}, p_{0}}(M)$. On each fiber over the support of $\chi_{(a)}$ the sections $\left\{\sigma_{\alpha,(a)}\right\}$ form an orthonormal frame for $E$ and hence a pointwise computation shows
$$\chi_{(a)} w=\sum_{\alpha}\left\langle\chi_{(a)} w, \sigma_{\alpha,(a)}\right\rangle_{h} \sigma_{\alpha,(a)} .$$
But then
$$w=\sum_{a} \chi_{(a)} w=\sum_{a, \alpha}\left\langle\chi_{(a)} w, \sigma_{\alpha,(a)}\right\rangle_{h} \sigma_{\alpha,(a)}$$
as required. The general case now follows from linearity. \(\square\)

At this point, the generalizations of all the results discussed in Section A. 1 (completeness, the basic inclusions of Lemma 3.2, Sobolev embedding (Proposition 3.3), Proposition 3.11) concerning multiplication, and the Rellich Lemma A.4) are easy consequences of their tensor space counterparts, Lemma A. 15 and Definition A.11, and we leave these details to the reader.

Regarding density of 'smooth' sections, the regularity of the metric provides a cap to the amount of regularity that can be expected from a dense subset.

Proposition A.16. Suppose $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$ and $\delta \in \mathbb{R}$.
\begin{itemize}
\item[(a)] The compactly supported elements of $H_{\delta}^{s_{0}, p_{0}}(M ; E)$ are dense in $H_{\delta}^{s, p}(M ; E)$.
\item[(b)] The set $H_{\text {loc }}^{s_{0}, p_{0}}(M ; E) \cap X_{\delta}^{s, p}(M ; E)$ is dense in $X_{\delta}^{s, p}(M ; E)$.
\end{itemize}

Proof. Let $u \in H_{\delta}^{s_{0}, p_{0}}(M ; E)$ and use Lemma A. 15 to decompose
$$u=\sum_{\alpha, a} u_{\alpha,(a)} \sigma_{\alpha,(a)}$$
for functions $u_{\alpha,(a)} \in H_{\delta}^{s, p}(M)$. Let $\varepsilon>0$ and use Proposition A. 5 to find a smooth compactly supported function $\widetilde{u}_{\alpha,(a)}$ with $\left\|u_{\alpha,(a)}-\widetilde{u}_{\alpha,(a)}\right\|_{H_{\delta}^{s, p}(M ; E)}<\varepsilon$. Setting $\widetilde{u}=$ $\sum_{\alpha, a} \widetilde{u}_{\alpha,(a)} \sigma_{\alpha,(a)}$ we find $\widetilde{u} \in H_{\delta}^{S_{0}, p_{0}}(M)$ and $\|u-\widetilde{u}\|_{H_{\delta}^{s, p}(M)} \lesssim \varepsilon$.
The Gicquaud-Sakovich case is proved similarly. \(\square\)

Interpolation for sections of geometric tensor bundles essentially follows from applying interpolation to the coefficients of a section.

Proposition A.17. Consider spaces $H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E)$ and $H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)$, with $\left(s_{1}, p_{1}\right)$ and $\left(s_{2}, p_{2}\right)$ in $S_{0}^{s_{0}, p_{0}}$, and with $\delta_{1}, \delta_{2} \in \mathbb{R}$. Let $\theta \in(0,1)$ and let $s, p, d$ be given by (A.14). Then $(s, p) \in S_{0}^{s_{0}, p_{0}}$ and
$$\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta}=H_{\delta}^{s, p}(M ; E) .$$
Proof. For $(s, p) \in S_{0}^{s_{0}, p_{0}} \operatorname{define} S: H_{\delta}^{s, p}(M ; E) \rightarrow \prod_{\alpha, a} H_{\delta}^{s, p}(M ; \mathbb{R})$ by $S(u)=\left(\pi_{\alpha,(a)}(u)\right)$ and observe that $S$ is continuous. Define $R: \prod_{\alpha, a} H_{\delta}^{s, p}(M ; \mathbb{R}) \rightarrow H_{\delta}^{s, p}(M ; E)$ to be the map taking $\left(u_{\alpha,(a)}\right)$ to $\sum_{\alpha,(a)} u_{\alpha,(a)} \sigma_{\alpha,(a)}$, which is again continuous. Moreover, Lemma A. 15 implies $R \circ S=\mathrm{id}$.

Using the fact that
$$\left[\prod_{\alpha, a} H_{\delta_{1}}^{s_{1}, p_{1}}(M ; \mathbb{R}), \prod_{\alpha, a} H_{\delta_{2}}^{s_{2}, p_{2}}(M ; \mathbb{R})\right]_{\theta}=\prod_{\alpha, a} H_{\delta}^{s, p}(M ; \mathbb{R})$$
we find that
$$\begin{aligned}
& S:\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta} \rightarrow \prod_{\alpha, a} H_{\delta}^{s, p}(M ; \mathbb{R}), \\
& R: \prod_{\alpha, a} H_{\delta}^{s, p}(M ; \mathbb{R}) \rightarrow\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta},
\end{aligned}$$
and that $R \circ S=\mathrm{id}$. The image of $R$ with domain $\prod_{\alpha, a} H_{\delta}^{s, p}(M ; \mathbb{R})$ is contained in $H_{\delta}^{s, p}(M ; E)$ and hence $\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta} \subset H_{\delta}^{s, p}(M ; E)$. Moreover,
$$S:\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta} \rightarrow \prod_{\alpha, a} H_{\delta}^{s, p}(M ; \mathbb{R})$$
is an isomorphism onto its image since it admits a continuous inverse, the restriction of $R$. Hence
$$\|u\|_{\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta}} \sim \sum_{\alpha, a}\left\|u_{\alpha,(a)}\right\|_{H_{\delta}^{s, p}(M ; \mathbb{R})} \sim\|u\|_{H_{\delta}^{s, p}(M ; E)},$$
and we conclude $\left[H_{\delta_{1}}^{s_{1}, p_{1}}(M ; E), H_{\delta_{2}}^{s_{2}, p_{2}}(M ; E)\right]_{\theta}$ is a closed subspace of $H_{\delta}^{s, p}(M ; E)$. Since it contains the dense subspace of compactly supported elements of $H_{\delta}^{S_{0}, p_{0}}(M ; E)$ we obtain the desired equality. \(\square\)

The limited interpolation result Lemma 3.14 for Gicquaud-Sakovich spaces generalizes to geometric tensor bundles by using the identity
$$T u=\sum_{\alpha_{a}}\left(\pi_{\alpha,(a)} \circ T\right)(u)$$
and applying Lemma 3.14 to the maps $\pi_{\alpha,(a)} \circ T$.
The only remaining task is to generalize the duality results of Theorem A. 10 , which only treated the scalar functions and only with a smooth background metric, to tensors defined by rough metric $h$. We first relax the regularity of the metric.

Lemma A.18. Suppose $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$. The map
$$\langle v, u\rangle_{(M, h)}=\int_{M} v u d V_{h},$$
defined for smooth compactly supported functions $u, v$ on $M$, extends to a continuous bilinear map $H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R}) \times H_{\delta}^{s, p}(M ; \mathbb{R}) \rightarrow \mathbb{R}$. Moreover, the map
$$v \mapsto\langle v, \cdot\rangle_{(M, h)}$$
is a continuous isomorphism $H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R}) \rightarrow\left(H_{\delta}^{s, p}(M ; \mathbb{R})\right)^{*}$.
Proof. Let $\check{g}$ be a smooth background metric as in Theorem A.10. Working in the domains of Möbius parametrizations, using the fact that $h$ admits a continuous compactification, one readily verifies that $d V_{h}=\omega d V_{\check{g}}$ where $\omega \in X_{0}^{S_{0}, p_{0}}(M)$ and where $\omega$ is uniformly bounded below away from zero. Proposition 3.19 ensures that $\omega^{-1} \in X_{0}^{s_{0}, p_{0}}(M)$ as well. Since
$$\langle\cdot, \cdot\rangle_{(M, h)}=\langle\cdot, \cdot \omega\rangle_{(M, \check{g})}$$
for smooth functions, continuity of multiplication $X_{0}^{s_{0}, p_{0}}(M) \times H_{\delta}^{s, p}(M) \rightarrow H_{\delta}^{s, p}(M ; \mathbb{R})$ implies that $\langle\cdot, \cdot\rangle_{(M, h)}$ extends to a continuous bilinear map $H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R}) \times H_{\delta}^{s, p}(M ; \mathbb{R}) \rightarrow$ $\mathbb{R}$. If $L \in\left(H_{\delta}^{s, p}(M)\right)^{*}$ we can find a unique $v \in H_{\delta}^{-s, p^{*}}(M)$ with $L=\langle v, \cdot\rangle_{(M, \check{g})}$. Since $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$ a simple computation shows $\left(-s, p^{*}\right) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$ as well and hence $v \mapsto \omega^{-1} v$ is a continuous automorphism of $H_{-\delta}^{-s, p^{*}}(M)$. But then
$$L(\cdot)=\left\langle\omega^{-1} v, \cdot \omega\right\rangle_{(M, \check{g})}=\left\langle\omega^{-1} v, \cdot\right\rangle_{(M, h)} .$$
Since $L \mapsto v \mapsto \omega^{-1} v$ is a chain of isomorphisms, the proof is complete. \(\square\)

Turning now to sections of geometric tensor bundles, define
$$\langle u, v\rangle_{(M, h)}=\int_{M}\langle u, v\rangle_{h} d V_{h}$$
for compactly supported sections $u, v \in H_{0}^{s_{0}, p_{0}}(M ; E)$. For such sections we have
$$\langle u, v\rangle_{(M, h)}=\sum_{\alpha, a, \alpha^{\prime}, a^{\prime}} \int_{M} \pi_{\alpha,(a)}(u) \pi_{\alpha^{\prime},\left(a^{\prime}\right)}(v)\left\langle\sigma_{\alpha,(a)}, \sigma_{\alpha^{\prime},\left(a^{\prime}\right)}\right\rangle_{h} d V_{h}$$

Noting that each $\left\langle\sigma_{\alpha,(a)}, \sigma_{\alpha^{\prime},\left(a^{\prime}\right)}\right\rangle_{h} \in X_{0}^{s_{0}, p_{0}}(M ; \mathbb{R})$ it follows from Lemma A.18, Propositions A. 16 and 3.11, and the continuity of the projections that $\langle\cdot, \cdot\rangle_{(M, h)}$ extends to a continuous, bilinear functional on $H_{-\delta}^{-s, p^{*}}(M ; E) \times H_{\delta}^{s, p}(M ; E)$.

Theorem A.19. Suppose $(s, p) \in \mathcal{S}_{0}^{s_{0}, p_{0}}$. The map
$$v \mapsto\langle v, \cdot\rangle_{(M, h)}$$
is a continuous isomorphism $H_{-\delta}^{-s, p^{*}}(M ; E) \rightarrow\left(H_{\delta}^{s, p}(M ; E)\right)^{*}$.
Proof. Let $L \in H_{\delta}^{s, p}(M ; E)$. For each index $(\alpha,(a))$ Lemma A. 18 implies there exists $v_{\alpha,(a)} \in H_{-\delta}^{-s, p^{*}}(M ; \mathbb{R})$ with $L\left(w \sigma_{\alpha,(a)}\right)=\langle v, u\rangle_{(M, h)}$ for all $w \in H_{\delta}^{s, p}(M ; \mathbb{R})$. The proof of Lemma A. 15 shows that for each $a$,
$$\chi_{(a)} u=\sum_{\alpha} \pi_{\alpha,(a)}(u) \sigma_{\alpha,(a)} .$$
Using the fact that on the support of $\chi_{(a)}$ the sections $\sigma_{\alpha,(a)}$ form an orthonormal frame we then find
$$\begin{aligned}
L\left(\chi_{(a)} u\right) & =\sum_{\alpha}\left\langle v_{\alpha,(a)}, \pi_{\alpha,(a)}(u)\right\rangle \\
& =\sum_{\alpha}\left\langle v_{\alpha,(a)}, \chi_{(a)}\left\langle u, \sigma_{\alpha,(a)}\right\rangle_{h}\right\rangle_{(M, h)} \\
& =\sum_{\alpha}\left\langle v_{\alpha,(a)} \sigma_{\alpha,(a)}, \chi_{(a)}\left\langle u, \sigma_{\alpha,(a)}\right\rangle_{h} \sigma_{\alpha,(a)}\right\rangle_{(M, h)} \\
& =\left\langle v_{(a)}, \chi_{(a)} u\right\rangle_{(M, h)}
\end{aligned}$$
where $v_{(a)}=\sum_{\alpha} v_{\alpha,(a)} \sigma_{\alpha,(a)} \in H_{-\delta}^{-s, p^{*}}(M ; E)$. Summing over $a$ we find
$$L(u)=\left\langle\sum_{a} \chi_{(a)} v_{(a)}, u\right\rangle_{(M, h)} .$$
Since $\sum_{a} v_{(a)} \in H_{-\delta}^{-s, p^{*}}(M ; E)$ we find $v \mapsto\langle v, \cdot\rangle_{(M, h)}$ is a surjection $H_{-\delta}^{-s, p^{*}}(M ; E) \rightarrow$ $\left(H_{\delta}^{s, p}(M ; E)\right)^{*}$. The continuity of the map follows from the remarks preceding the statement of the theorem. To see that it has trivial kernel, suppose $v \in H_{-\delta}^{-s, p^{*}}(M ; E) \neq 0$. Appealing to Lemma A. 15 there is are indices $(\alpha,(a))$ with $\pi_{\alpha,(a)}(v) \neq 0$. Choose a smooth compactly supported function $\phi$ such that $\left\langle\pi_{\alpha,(a)}(v), \phi\right\rangle_{(M, h)} \neq 0$. Since $\chi_{(a)} v=$ $\sum_{\alpha} \pi_{\alpha,(a)}(v) \sigma_{\alpha,(a)}$,
$$\left\langle v, \chi_{(a)} \phi \sigma_{\alpha,(a)}\right\rangle_{(M, h)}=\left\langle\sum_{\alpha^{\prime}} \pi_{\alpha^{\prime},(a)}(v) \sigma_{\alpha^{\prime},(a)}, \phi \sigma_{\alpha,(a)}\right\rangle_{(M, h)}=\left\langle\pi_{\alpha,(a)}(v), \phi\right\rangle_{(M, h)} \neq 0 .$$ \(\square\)
A.6. Equivalent norms. The weighted space norms depend implicitly on a number of choices:
\begin{itemize}
\item[-] A boundary defining function $\rho$.
\item[-] A projection from a collar neighborhood of $\partial M$ onto the boundary.
\item[-] A choice of finitely many charts for the boundary.
\item[-] A selection of preferred Möbius parametrizations $\Phi_{i}$.
\end{itemize}

We call these collective choices Möbius data and now show that the function spaces are independent of the choice of Möbius data. These considerations also lead to Corollary A.23, which establishes an equivalent norm for the Gicquaud-Sakovich spaces that is comparable to the authors' original definition. Since spaces of sections of geometric tensor bundles inherit their norms from their ambient spaces of sections of tensor bundles, throughout this section we work in the simpler setting of tensor bundles, and thus the regularity of a defining metric is not a consideration. The resulting norm equivalences extend to geometric tensor bundles automatically.
Proposition A.20. Let $E$ be a tensor bundle over $\bar{M}$. For each $s, \delta \in \mathbb{R}$ and $1<p<\infty$ the space $H_{\delta}^{s, p}(M ; E)$ is independent of the choice of Möbius data and the norms determined by two choices are equivalent.

Proof. From the density of smooth compactly supported sections (Proposition A.5), to show two spaces are the same it suffices to show that the norms corresponding to different choices are equivalent.
First, consider the case $s=k \in \mathbb{N}_{\geq 0}$. Lemma A. 3 and Lemma 3.1 show that any choice of $H_{\delta}^{k, p}(M)$ norm is equivalent to a $W_{\delta}^{k, p}(M)$ norm from (3.3), which depends only on a (separate, independent) choice of reference metric $\check{g}$ and the boundary defining function $\rho$. Moreover, the $W_{\delta}^{k, p}(M)$ norm for two choices $\rho$ and $\widetilde{\rho}$ are equivalent because $(\widetilde{\rho} / \rho)^{\delta}$ is smooth on $\bar{M}$ and hence multiplication by this function is an automorphism of $W_{\delta}^{k, p}(M)$. Thus any two choices of Möbius data lead to equivalent $H_{\delta}^{k, p}(M)$ norms.
Turning to the general case, the result for $s \geq 0$ follows from what we have shown for $s \in \mathbb{N}_{\geq 0}$ and the the characterization of $H_{\delta}^{s, p}(M)$ as an interpolation space. Suppose instead $s<0$. Choosing a reference metric $\check{g}$ with smooth compactification, the identification of $H_{\delta}^{s, p}(M)$ with $\left(H_{-\delta}^{-s, p^{*}}(M)\right)^{*}$ via Theorem A. 19 establishes the result in this case. \(\square\)

The analogue of Proposition A. 20 for Gicquaud-Sakovich spaces is an easy consequence of the following lemma, which is independently used in Section B concerning elliptic operators on the ball model of hyperbolic space.
Lemma A.21. Let $E$ be a tensor bundle over $\bar{M}$ and let $(\widetilde{\Omega}, \widetilde{\Theta})$ be a boundary chart associated with some boundary projection and some boundary defining function $\widetilde{\rho}$. Suppose $s, \delta \in \mathbb{R}$ and $1<p<\infty$. For all Möbius parametrizations $\widetilde{\Phi}$ associated with $\widetilde{\Theta}$ and all $u \in H_{\mathrm{loc}}^{s, p}(M)$,
$$\widetilde{\rho}(\widetilde{\Phi}(0))^{-\delta}\left\|\chi \widetilde{\Phi}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \lesssim\|u\|_{X_{\delta}^{s, p}(M)}$$
with implicit constant independent of $u$ but depending on the remaining data.

Proof. Let $I$ be the set of indices $i$ such that $\widetilde{\Phi}\left(B_{2}\right) \cap \Phi_{i}\left(B_{2}\right) \neq \emptyset$. From Lee [Lee06] Lemma 2.1 the $\check{g}$ diameter of $\widetilde{\Phi}\left(B_{2}\right)$ is bounded independent of $\widetilde{\Phi}$ and hence from property (c) of the parametrizations $\Phi_{i}$ enumerated at the end of Section 2 we obtain a uniform upper bound for the size of $I$.

An argument essentially similar to the one from Lemma A.2, using the fact that $\widetilde{\rho}_{0} / \rho_{0}$ is uniformly bounded above and below, shows that the transition Jacobians $D\left(\Phi_{i}^{-1} \circ \widetilde{\Phi}\right)$ admit $C^{k}$ bounds for each $k$ that are uniform in $i$.

Recalling the function $\bar{\chi}$ from equation (A.7) we have
$$\left\|\chi \widetilde{\Phi}^{*}(\bar{\chi} u)\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}=\left\|\chi \widetilde{\Phi}^{*} \sum_{i \in I}\left(\left(\Phi_{i}\right)_{*} \chi\right) u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} \lesssim \sum_{i \in I}\left\|\chi\left(\Phi_{i}^{-1} \circ \Phi\right)^{*}\left(\chi \Phi_{i}^{*} u\right)\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)} .$$
The uniform bound for the size of $I$, the uniform $C^{k}$ control of the transition functions, and the fact that $\widetilde{\rho}(\widetilde{\Phi}(0)) / \rho_{i}$ is uniformly bounded above and below for all $i \in I$ then imply
$$\rho(\Phi(0))^{-\delta}\left\|\Phi^{*}(\bar{\chi} u)\right\|_{H^{s, p}\left(B_{r}\right)} \lesssim\|u\|_{X_{\delta}^{s, p}(M)} .$$
Since $u \mapsto u / \bar{\chi}$ is continuous on $H_{\delta}^{s, p}(M)$ the proof is complete. \(\square\)

Lemma A. 21 immediately implies the following.
Corollary A.22. Let $E$ be a tensor bundle over $\bar{M}$. For each $s, \delta \in \mathbb{R}$ and $1<p<\infty$, the space $X_{\delta}^{s, p}(M ; E)$ is independent of the choice of Möbius data and any two choices lead to equivalent norms.

We also obtain from Lemma A. 21 the following equivalent norm for Gicquaud-Sakovich spaces which can be compared with the original definition of 'weighted local Sobolev spaces' from [GS12] as well as the Hölder analogue, equation (3.2) of [Lee06].

Corollary A.23. Let E be a tensor bundle over $\bar{M}$. Suppose $s, \delta \in \mathbb{R}$ and $1<p<\infty$. For any $1 / 2<r<2$ the $X_{\delta}^{s, p}$ norm is equivalent to
$$\sup _{\Phi} \rho(\Phi(0))^{-\delta}\left\|\Phi^{*} u\right\|_{H^{s, p}\left(B_{r}\right)}$$
where the supremum is taken over all Möbius parametrizations.

Proof. One direction follows immediately from Lemma A. 3 and the converse is a consequence of Lemma (A.21) and the fact that we can take our cutoff function $\chi$ to equal 1 on $B_{r}^{\mathbb{H}}$. \(\square\)

\section*{Appendix B. Elliptic theory for hyperbolic space}

Following [Lee06] Chapter 5, we work with the Poincaré ball model $\mathbb{B}$ of hyperbolic space, so $\mathbb{B}$ is the unit ball in $\mathbb{R}^{n}$ with metric
$$g_{\mathbb{B}}=4(1-|\xi|)^{-2} \sum_{i}\left(d \xi^{i}\right)^{2} .$$
For $\xi, \eta \in \mathbb{B}$ we define $\rho(\xi, \eta)=1 / \cosh \left(d_{g_{\mathbb{B}}}(\xi, \eta)\right)$ and set
$$\rho(\xi)=\rho(\xi, 0)=\frac{1-|\xi|^{2}}{1+|\xi|^{2}},$$
which is a defining function on $\mathbb{B}$.
Throughout this section we consider a fixed operator $\mathcal{P}=\mathcal{P}\left[g_{\mathbb{B}}\right]$ acting on a geometric tensor bundle $E \rightarrow \mathbb{B}$ and satisfying Assumption P. We assume moreover that, Assumption I holds, so that $\mathcal{P}: H_{0}^{d, 2}(\mathbb{B} ; E) \rightarrow H_{0}^{0,2}(\mathbb{B} ; E)$ is an isomorphism. From [Lee06] Lemma 4.10 this is equivalent to assuming $\mathcal{P}$ satisfies the $L^{2}$ estimate at infinity, namely there exists a compact set $K \subset \mathbb{B}$ and a constant $C$ such that for all $u \in C_{\text {cpct }}^{\infty}(\mathbb{B} \backslash K ; E)$,
$$\|u\|_{L^{2}(\mathbb{B} ; E)} \leq C\|\mathcal{P} u\|_{L^{2}(\mathbb{B} ; E)} .$$
The symmetries of $\mathbb{B}$ allow for a convenient alternative formulation of weighted space norms. Following the construction of [Lee06] Lemma 2.2 we can find a positive integer $N$ and a countable collection of points $p_{i} \in \mathbb{B}$ such that the balls $B_{1 / 2}^{\mathbb{B}}\left(p_{i}\right)$ cover $\mathbb{B}$ and such that each $B_{2}^{\mathbb{B}}\left(p_{i}\right)$ intersects at most $N$ others. Moreover, for any diameter $\ell>0$ there is a bound $K_{\ell}$ such that if $U \subset \mathbb{B}$ has diameter at most $\ell$, then $B_{2}^{\mathbb{B}}\left(p_{i}\right) \cap U=\emptyset$ for all but at most $K_{\ell}$ points $p_{i}$. For each $i$ we select a hyperbolic isometry $\Gamma_{i}$ with $\Gamma_{i}(0)=p_{i}$.

Lemma B.1. Suppose $s, \delta \in \mathbb{R}$ and $1<p<\infty$. For each $1 / 2<r<2$, we have the following norm equivalences:
$$\|u\|_{H_{\delta}^{s, p}(\mathbb{B} ; E)}^{p} \sim \sum_{i} \rho\left(\Gamma_{i}(0)\right)^{-\delta p}\left\|\Gamma_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{B}}\right)}^{p} .$$
(b)
$$\|u\|_{X_{\delta}^{s, p}(\mathbb{B} ; E)} \sim \sup _{i} \rho\left(\Gamma_{i}(0)\right)^{-\delta}\left\|\Gamma_{i}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{B}}\right)} .$$
(c)
$$\|u\|_{X_{\delta}^{s, p}(\mathbb{B} ; E)} \sim \sup _{\Gamma} \rho(\Gamma(0))^{-\delta}\left\|\Gamma^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{B}}\right)},$$
where the supremum is taken over all hyperbolic isometries of $\mathbb{B}$.
Proof. The central issue is that the coordinate function $y$ in the half space model $\mathbb{H}$ of hyperbolic space does not arise from a smooth boundary defining function on $\mathbb{B}$; it is singular at a point of $\partial \mathbb{B}$. To mitigate this, choose open cover $\left\{\Omega_{\alpha}\right\}_{\alpha \in\{1,2\}}$ for $\mathbb{B}$ and isometries $\Theta_{\alpha}: \mathbb{B} \rightarrow \mathbb{H}$ such that $\Theta_{\alpha}\left(\Omega_{\alpha}\right)=Y_{r}$ for some number $r$ and such that for each $p \in \mathbb{B}$ we can select an index $\alpha$ so that $B_{2}(p) \subset \Omega_{\alpha}$.

Fix an isometry $\Psi_{\mathbb{H}}^{\mathbb{B}}: B_{2}^{\mathbb{H}} \rightarrow B_{2}^{\mathbb{B}}$. For each $\alpha$ we can select a boundary defining function $\rho_{\alpha}$ that equals $\Theta_{\alpha}^{*} y$ on $\Omega_{\alpha}$. Let $\Gamma: \mathbb{B} \rightarrow \mathbb{B}$ be an isometry and pick $\alpha$ so that $\Gamma\left(B_{2}^{\mathbb{H}}\right) \subset \Omega_{\alpha}$. Choosing a suitable Euclidean rotation $R_{\Gamma}$ we can arrange so that
$$\left(\Theta_{\alpha} \circ \Gamma \circ R_{\Gamma} \circ \Psi_{\mathbb{H}}^{\mathbb{B}}\right)(x, y)=\left(\theta_{0}+\rho_{\Gamma} x, \rho_{\Gamma} y\right)$$
for some $\theta_{0}$, where $\rho_{\Gamma}=\rho_{\alpha}(\Gamma(0))$. Let $\Phi_{\Gamma}=\Gamma \circ R \circ \Psi$ so that in effect, $\Phi_{\Gamma}$ is a Möbius parametrization with respect to the chart $\Omega_{\alpha}$ and the boundary defining function $\rho_{\alpha}$. Hence, arguing as in the proof of Lemma A.21, and using the fact that $\rho / \rho_{\alpha}$ is uniformly bounded above and bounded below away from zero, we find that the Jacobians $D\left(\Phi^{-1} \circ \Phi_{\Gamma}\right)$ and $D\left(\Phi_{\Gamma}^{-1} \circ \Phi\right)$ admit uniform $C^{k}$ bounds independent of $\Phi$ and $\Gamma$.
Let $\eta$ be a cutoff function with support in $B_{r}^{\mathbb{H}}$ that equals 1 on $B_{1 / 2}^{\mathbb{H}}$. For each $i$, let $N(i)$ be the set of indices $j$ such that $\Gamma_{j}\left(B_{2}^{\mathbb{B}}\right) \cap \Phi_{i}\left(B_{2}^{\mathbb{H}}\right) \neq \emptyset$. Since the sets $\Phi_{i}\left(B_{2}^{\mathbb{H}}\right)$ admits an upper bound on their diameters, the size of $N(i)$ is bounded above independent of $i$. The function
$$\sum_{j \in N(i)} \Phi_{i}^{*}\left(\Phi_{\Gamma_{j}}\right)_{*} \eta$$
is bounded below on $B_{2}^{\mathbb{H}}$ and admits uniform $C^{k}$ bounds independent of $i$. Hence, using the uniform $C^{k}$ bounds for the transition Jacobians,
$$\left\|\chi \Phi_{i}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \lesssim\left\|\chi \Phi_{i}^{*}\left(\sum_{j \in N(i)}\left(\Phi_{\Gamma_{j}}\right)_{*} \eta\right) u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \lesssim \sum_{j \in N(i)}\left\|\eta \Phi_{\Gamma_{j}}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} .$$
Since $\rho\left(\Gamma_{j}(0)\right) / \rho_{i}$ is uniformly bounded above and below independent of $i$ and $j$, and using the fact that that there is a uniform upper bound for the number of indices $i$ such that $\Gamma_{j}\left(B_{2}\right) \cap \Phi_{i}\left(B_{2}\right) \neq \emptyset$ we find
$$\|u\|_{H_{\delta}^{s, p}(\mathbb{B})}^{p} \lesssim \sum_{i} \sum_{j \in N(i)} \rho\left(\Gamma_{j}(0)\right)^{-\delta p}\left\|\eta \Phi_{\Gamma_{j}}^{*} u\right\|_{H^{s, p}\left(\mathbb{R}^{n}\right)}^{p} \lesssim \sum_{j} \rho\left(\Gamma_{j}(0)\right)^{-\delta p}\left\|\Phi_{\Gamma_{j}}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathrm{H}}\right)}^{p} .$$
From uniform $C^{k}$ estimates for $R_{\Gamma_{k}} \circ \Psi_{\mathbb{H}}^{\mathbb{B}}$ we then find
$$\|u\|_{H_{\delta}^{s, p}(\mathbb{B})}^{p} \lesssim \sum_{j} \rho\left(\Gamma_{j}(0)\right)^{-\delta p}\left\|\Gamma_{j}^{*} u\right\|_{H^{s, p}\left(B_{r}^{\mathbb{B}}\right)}^{p} .$$
The reverse inequality is proved by analogous arguments, which establishes the equivalence (B.2). The equivalences (b) and (c) are proved with similar, easier techniques; see also Lemma A.21. \(\square\)

The following elliptic regularity result is a straightforward consequence of the alternative norms of Lemma B. 1 and local elliptic regularity (Proposition 8.3), noting that the operator $\Gamma_{i}^{*} \mathcal{P}$ is independent of $i$ and hence the implicit constant from equation (8.5) is also independent of $i$.

Lemma B.2. Suppose $s, s^{\prime}, \delta \in \mathbb{R}$ and $1<p<\infty$.
\begin{itemize}
\item[(a)] Suppose $u \in H_{\delta}^{s, p}(\mathbb{B} ; E)$ and $\mathcal{P} u \in H_{\delta}^{s^{\prime}-d, p}(\mathbb{B} ; E)$. Then $u \in H_{\delta}^{s^{\prime}, p^{*}}(\mathbb{B} ; E)$.
\item[(b)] Suppose $u \in X_{\delta}^{s, p}(\mathbb{B} ; E)$ and $\mathcal{P} u \in X_{\delta}^{s^{\prime}-d, p}(\mathbb{B} ; E)$. Then $u \in X_{\delta}^{s^{\prime}, p}(\mathbb{B} ; E)$.
\end{itemize}

The mapping properties of $\mathcal{P}$ on the weighted Sobolev spaces is a straightforward consequence interpolation and duality arguments; see, for example [Max06, Lemma 3.5]. We now establish the main isomorphism theorem; recall the definition of $\mathcal{D}_{q}(R)$ from (1.9).

Theorem B.3. Suppose $s \in \mathbb{R}, 1<p<\infty$ and that $\delta \in \mathcal{D}_{q}(R)$, where $R$ is the indicial radius of $\mathcal{P}$. Then $\mathcal{P}: H_{\delta}^{s, p}(\mathbb{B}) \rightarrow H_{\delta}^{s-d, p}(\mathbb{B})$ is an isomorphism.

Proof. The proof proceeds in three cases, $s \geq d, s \leq 0$ and $s \in[0, d]$.
For $s \in \mathbb{R}$, let $\mathcal{P}_{s}$ denote $\mathcal{P}$ as a map from $H_{\delta}^{s, p}(\mathbb{B} ; E)$ to $H_{\delta}^{s-d, p}(\mathbb{B} ; E)$. Suppose $s \geq d$ and let $k$ be the integer such that $d \leq k \leq s<k+1$. From [Lee06] Theorem 5.6, $\mathcal{P}_{k}$ and $\mathcal{P}_{k+1}$ are isomorphisms. Hence so is $\mathcal{P}_{s}$ by interpolation.
Now suppose $s \leq 0$. Given $v \in H_{\delta}^{s-d, p}(\mathbb{B})$ we wish to solve $\mathcal{P} u=v$. To this end we apply Theorem A. 19 with background metric $g_{\mathbb{B}}$ to obtain a unique $u \in H_{-\delta}^{s, p}(\mathbb{B})$ satisfying
$$\langle u, w\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}=\left\langle v,\left(\mathcal{P}_{d-s}\right)^{-1} w\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}$$
for all $w \in H_{-\delta}^{-s, p^{*}}\left(\mathbb{B}, g_{\mathbb{B}}\right)$. Note that in this context $\mathcal{P}_{d-s}^{-1}: H_{-\delta}^{-s, p^{*}}(\mathbb{B}) \rightarrow H_{-\delta}^{d-s, p^{*}}(\mathbb{B})$, which is well-defined by our work in the first case since $d-s \geq d$ and since $-\delta \in \mathcal{D}_{p^{*}}(R)$ if and only if $\delta \in \mathcal{D}_{q}(R)$.
Since $\mathcal{P}_{s}$ is formally self-adjoint with respect to $g^{\mathbb{B}}$, if $w$ is any compactly supported smooth section,
$$\left\langle\mathcal{P}_{s} u, w\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}=\left\langle u, \mathcal{P}_{d-s} w\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}=\left\langle v, \mathcal{P}_{d-s}^{-1} \mathcal{P}_{d-s} w\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}=\langle v, w\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)} .$$
Thus $\mathcal{P}_{s} u=v$ in the sense of distributions, and $\mathcal{P}_{s}$ is surjective. That it is injective follows from the injectivity of $\mathcal{P}_{d}$ and Lemma B.2.

Finally, suppose $s \in[0, d]$. Then $\mathcal{P}_{0}$ and $\mathcal{P}_{d}$ are isomorphisms, and thus by interpolation $\mathcal{P}_{s}$ is an isomorphism as well. \(\square\)

We now turn to the analogue of Theorem B. 3 for Gicquaud-Sakovich spaces, which requires additional labor due to the absence of good interpolation/duality tools. The following lemma from [GS12] is the crucial ingredient for obtaining mapping properties on spaces $X_{\delta}^{s, p}(\mathbb{B} ; E)$ when $s \geq m$. In it, $\mathcal{P}^{-1}$ refers to convolution against the Greens function of $\mathcal{P}$ discussed in [Lee06, Chapter 5].

Lemma B. 4 ([GS12] Lemma A.3). Suppose $1<p<\infty$ and $\delta \in \mathcal{D}_{\infty}(R)$. Then
$$\left\|\mathcal{P}^{-1} f\right\|_{X_{\delta}^{0, p}(\mathbb{B} ; E)} \lesssim\|f\|_{X_{\delta}^{0, p}(\mathbb{B} ; E)}$$
for all $f \in X_{\delta}^{0, p}(M ; \mathbb{B})$.
The following discrete analogue of [Lee06] Lemma 5.4 is the main tool needed for establishing mapping properties for spaces with $s<0$. In it, the points $p_{j}$ are those associated with the isometries $\Gamma_{j}$ discussed in Proposition B.1.

Lemma B.5. Suppose $\delta, \delta^{*}$ are real numbers such that $\delta<\delta *$ and $\delta+\delta^{*}>n-1$. For all $q \in \mathbb{B}$,
$$\sum_{j} \rho\left(0, p_{j}\right)^{\delta} \rho\left(p_{j}, q\right)^{\delta^{*}} \lesssim \rho(0, q)^{\delta}$$
with implicit constant independent of $q$.
Proof. From local finiteness we can partition the centers $\left\{p_{j}\right\}$ into finitely many sets $J_{1}, \ldots, J_{N+1}$ such that if $p_{i}, p_{j} \in J_{k}$, then $B_{2}\left(p_{i}\right) \cap B_{2}\left(p_{j}\right)=\emptyset$. It is then enough to show that each
$$\sum_{j \in J_{k}} \rho\left(0, p_{j}\right)^{\delta} \rho\left(p_{j}, q\right)^{\delta^{*}} \lesssim \rho(0, q),$$
where the implicit constant $C$ independent of $q$.
Fix one of the partitions $J_{k}$ and consider the function $\chi$ that equals $\rho\left(0, p_{j}\right)^{\delta}$ on $B_{1}^{\mathbb{B}}\left(p_{j}\right)$ for each $j \in J_{k}$ and is otherwise zero. Define $\hat{\chi}$ similarly with $\hat{\chi}=\rho\left(p_{j}, q\right)$ on each $B_{1}^{\mathbb{B}}\left(p_{j}\right)$. A straightforward computation shows there is a constant $C>0$ such that $C \rho(x, 0) \geq \chi(x)$ and $C \rho(x, q) \geq \hat{\chi}(x)$ for all $x \in \mathbb{B}$; indeed, $C=\exp (1)=\sup _{x \geq 0} \cosh (x+1) / \cosh (x)$ suffices.

Now
$$\begin{aligned}
\sum_{j \in P_{k}} \rho\left(0, p_{j}\right)^{\delta} \rho\left(p_{j}, q\right)^{\delta^{*}} & =\frac{1}{\operatorname{Vol} B_{1}^{\mathbb{B}}} \int \chi \hat{\chi} d V_{g_{\mathbb{B}}} \\
& \leq \frac{C^{2}}{\operatorname{Vol} B_{1}^{\mathbb{B}}} \int \rho(0, x)^{\delta} \rho(x, q)^{\delta^{*}} d V_{g_{\mathbb{B}}}(x)
\end{aligned}$$
Lemma 5.4 of [Lee06] implies there is a constant $c$, independent of $q$, such that
$$\int \rho(0, x)^{\delta} \rho(x, q)^{\delta^{*}} d V_{g_{\mathrm{B}}}(x) \leq c \rho(0, q)^{\delta},$$
which proves the result. \(\square\)

Theorem B.6. Suppose $s \in \mathbb{R}, 1<p<\infty$, and $\delta \in \mathcal{D}_{\infty}(R)$. Then $\mathcal{P}: X_{\delta}^{s, p}(\mathbb{B} ; E) \rightarrow$ $X_{\delta}^{s-d, p}(\mathbb{B} ; E)$ is an isomorphism.

Proof. Let $\mathcal{P}_{s}$ denote $\mathcal{P}$ as a map from $X_{\delta}^{s, p}(\mathbb{B})$ to $X_{\delta}^{s-d, p}(\mathbb{B})$. Pick $\delta^{\prime}$ such that $-R<$ $\delta^{\prime}+\frac{n-1}{p}-\frac{n-1}{2}<\delta-\frac{n-1}{2}<R$. Noting that $\delta^{\prime} \in \mathcal{D}_{p}(R)$, the injectivity of $\mathcal{P}_{s}$ follows from the embedding of $X_{\delta}^{s, p}(\mathbb{B})$ into $H_{\delta^{\prime}}^{s, p}(\mathbb{B})$ given by Lemma 3.2 along with the injectivity of $\mathcal{P}$ on this latter space. Hence, by the Closed Graph Theorem, to show that $\mathcal{P}_{s}$ is an isomorphism it suffices to show that $\mathcal{P}_{s}$ is surjective.
Let $f \in X_{\delta}^{s-m, p}(\mathbb{B}) \subset H_{\delta^{\prime}}^{s-m, p}(\mathbb{B})$. Theorem B. 3 implies there exists $u \in H_{\delta^{\prime}}^{s, p}(\mathbb{B})$ such that $\mathcal{P} u=f$. Hence the main issue is to prove that in fact $u \in X_{\delta}^{s, p}(\mathbb{B})$.
Suppose first that $s \geq m$. Then [Lee06] Chapter 5 shows that $u \in H_{\delta^{\prime}}^{m, p}(\mathbb{B})$ is obtained by convolving $f \in H_{\delta^{\prime}}^{0, p}(\mathbb{H})$ against the Greens function of $\mathcal{P}$ and Lemma B. 4 therefore
implies $u \in X_{\delta}^{0, p}(\mathbb{B})$. We conclude from Lemma B. 2 that $u \in X_{\delta}^{s, p}(\mathbb{B})$ and hence $\mathcal{P}_{s}$ is surjective.
Now suppose $s \leq 0$. Given a smooth section $\phi$ of $E$ that is compactly supported in $B_{1}^{\mathbb{B}}(0)$ we compute for any hyperbolic isometry $\Gamma$
$$\left\langle\Gamma^{*} u, \phi\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}=\left\langle\mathcal{P}_{s}^{-1} f, \Gamma_{*} \phi\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}=\left\langle f, \mathcal{P}_{-s+m}^{-1} \Gamma_{*} \phi\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}=\left\langle f, \Gamma_{*} \mathcal{P}_{-s+m}^{-1} \phi\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}$$
where $\langle\cdot, \cdot\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)}$ denotes duality pairing on weighted Bessel potential spaces and where each step is obvious when $f$ is smooth and compactly supported and is hence justified by a density argument.

Let $\left\{\Gamma_{i}\right\}$ be the collection of isometries considered in Lemma B. 1 and set $p_{i}=\Gamma_{i}(0)$. Making straightforward adjustments, Lemma A. 2 can be generalized to the current setting. and using it we can then construct a partition of unity $\left\{\chi_{i}\right\}$ subordinate to $\left\{B_{1}^{\mathbb{B}}\left(p_{i}\right)\right\}$ that is uniformly bounded in $C_{0}^{k}(\mathbb{B})$ for any choice of $k$. Pick $\delta^{*}>\delta$ such that $\delta^{*} \in \mathcal{D}_{\infty}(R)$ and such that $\delta+\delta^{*}>n-1$. Then
$$\begin{aligned}
\left\langle f, \Gamma_{*} \mathcal{P}_{m-s}^{-1} \phi\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)} & =\sum_{j}\left\langle f, \chi_{j} \Gamma_{*} \mathcal{P}_{m-s}^{-1} \phi\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)} \\
& =\sum_{j}\left\langle\Gamma_{j}^{*} f,\left(\Gamma_{j}^{*} \chi_{j}\right)\left(\Gamma_{j}^{*} \Gamma_{*} \mathcal{P}_{m-s}^{-1} \phi\right)\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)} \\
& \lesssim \sum_{j}\left\|\Gamma_{j}^{*} f\right\|_{H^{s-m, p}\left(B_{1}^{\mathbb{B}}\right)}\left\|\left(\Gamma_{j}^{*} \Gamma_{*} \mathcal{P}_{m-s}^{-1} \phi\right)\right\|_{H^{m-s, p^{*}}\left(B_{1}^{\mathbb{B}}\right)} \\
& \leq\|f\|_{X_{\delta}^{s-m, p}(\mathbb{B})} \sum_{j} \rho\left(p_{j}\right)^{\delta}\left\|\left(\Gamma_{j}^{*} \Gamma_{*} \mathcal{P}_{m-s}^{-1} \phi\right)\right\|_{H^{m-s, p^{*}}\left(B_{1}^{\mathbb{B}}\right)} .
\end{aligned}$$
From the alternate norm of Lemma B.1, the fact that $\rho(\cdot, \cdot)$ is invariant under hyperbolic isometries, and the fact that $m-s \geq m$ (and therefore $\mathcal{P}_{m-s}$ is an isomorphism) we compute
$$\begin{aligned}
\left\|\Gamma_{j}^{*} \Gamma_{*} \mathcal{P}_{m-s}^{-1} \phi\right\|_{H^{m-s, p^{*}}\left(B_{1}(0 ; \mathbb{B})\right)} & \leq\left\|\mathcal{P}_{m-s}^{-1} \phi\right\|_{X_{\delta^{*}}^{m-s, p^{*}}(\mathbb{B} ; E)} \rho\left(\left(\Gamma^{-1} \circ \Gamma_{j}\right)(0), 0\right)^{\delta^{*}} \\
& \leq\left\|\mathcal{P}_{m-s}^{-1} \phi\right\|_{X_{\delta^{*}}^{m-s, p^{*}}(\mathbb{B} ; E)} \rho\left(\Gamma_{j}(0), \Gamma(0)\right)^{\delta^{*}} \\
& \lesssim\|\phi\|_{X_{\delta^{*}}^{-s, p^{*}}(\mathbb{B} ; E)} \rho\left(p_{j}, \Gamma(0)\right)^{\delta^{*}} \\
& \lesssim\|\phi\|_{H^{-s, p^{*}}\left(B_{1}^{\mathbb{B}}\right)} \rho\left(p_{j}, \Gamma(0)\right)^{\delta^{*}}
\end{aligned}$$
Combining these inequalities and applying Lemma B. 5 we conclude
$$\begin{aligned}
\left\langle\Gamma^{*} u, \phi\right\rangle_{\left(\mathbb{B}, g_{\mathbb{B}}\right)} & \lesssim\|\phi\|_{H^{-s, p^{*}}\left(B_{1}^{\mathbb{B}}\right)}\|f\|_{X_{\delta}^{s-m, p}(\mathbb{B})} \sum_{j} \rho\left(p_{j}\right)^{\delta} \rho\left(p_{j}, \Gamma(0)\right)^{\delta^{*}} \\
& \lesssim\|\phi\|_{H^{-s, p^{*}}\left(B_{1}^{\mathbb{B}}\right)}\|f\|_{X_{\delta}^{s-m, p}(\mathbb{B})} \rho(0, \Gamma(0))^{\delta}
\end{aligned}$$
for all smooth sections $\phi$ that are compactly supported in $B_{1}^{\mathbb{B}}$. Hence
$$\left\|\Gamma^{*} u\right\|_{H^{s, p}\left(B_{1}^{\mathbb{B}}\right)} \lesssim\|f\|_{X_{\delta}^{s-m, p}(\mathbb{B})} \rho(0, \Gamma(0))^{\delta}$$
and we conclude $u \in X_{\delta}^{s, p}(\mathbb{B})$. Thus $\mathcal{P}_{s}$ is surjective.

Finally, suppose $s \in[0, m]$. Given $f \in X_{\delta}^{s-m, p}(\mathbb{B}) \subset X_{\delta}^{-m, p}(\mathbb{B})$ we can find $u \in X_{\delta}^{0, p}(\mathbb{B})$ with $\mathcal{P}_{0} u=f$. Lemma B. 2 then implies $u \in X_{\delta}^{0, p}(\mathbb{B})$. \(\square\)

\section*{Appendix C. Smooth approximation of metrics in fortified spaces}

The proof of Theorem 9.10 concerning Fredholm mapping properties of elliptic operators acting on Gicquaud-Sakovich spaces makes use, at least for asympotically hyperbolic metrics having very low regularity, of the fact that these metrics can be approximated in a limited sense by smooth asymptotically hyperbolic metrics. This section contains the construction.

First, we show that if $u$ is a tensor of weight $w$ in some space $\mathscr{H}^{s, p ; m}(M ; E)$ with parameters good enough to imply Hölder continuity on $\bar{M}$, we can find a nearby smooth tensor on $\bar{M}$, but only with respect to the $X_{w}^{s, p}(M ; E)$ norm. In the case of a metric $g$, the compactified metric $\bar{g}$ is approximated by some smooth $\widetilde{g}$ in $X_{w}^{s, p}(M)$ and hence $\rho^{-2} \widetilde{g}$ is smooth on $M$ and is close to $g$ in $X_{0}^{s, p}(M)$. Although the approximation is not in the topology of the fortified space, the result is sufficient to show that differential operators derived from $\rho^{-2} \widetilde{g}$ are close to those derived from $g$.

Proposition C.1. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}, s>n / p$ and $s \geq m \geq 1$. Let $E$ be a tensor bundle of weight $w$ over $M$ and suppose either $u \in \mathscr{H}^{s, p ; m}(M ; E)$ with $m>n / p$ or $u \in \mathscr{X}^{s, p ; m}(M ; E)$. For every $\varepsilon>0$ there exists $u_{\varepsilon} \in C^{\infty}(\bar{M} ; E)$ such that
$$\left\|u-\bar{u}_{\varepsilon}\right\|_{X_{w}^{s, p}(M ; E)}<\varepsilon .$$
Proof. For definiteness, suppose $u \in \mathscr{H}^{s, p ; m}(M ; E)$; the proof in the Gicquaud-Sakovich case is similar. Let $\left\{\hat{p}_{j}\right\}_{j=1}^{J}$ and $\left\{\psi_{j}\right\}_{j=0}^{J}$ be the boundary points and partition of unity of $M$ constructed by Lemma 8.13 for some $r \leq r_{0} / 2$ chosen small enough so that the Lemma applies.
For $j \geq 1$ let $u_{B}^{A}\left[\hat{p}_{j}\right]$ be the components of $u$ at $\hat{p}_{j}$ in the local coordinates $\Theta$ associated with $\hat{p}_{j}$ and let $u_{j}$ be a smooth tensor on $\bar{M}$ that equals
$$u_{B}^{A}\left[\hat{p}_{j}\right] \partial_{\Theta^{A}} d \Theta^{B}$$
on $Z_{r_{0} / 2}\left(\hat{p}_{j}\right)$ and that vanishes outside $Z_{r_{0}}\left(p_{j}\right)$. From the boundary continuity of $u$ we can arrange to do this so
$$\left\|u_{j}\right\|_{\mathscr{H}^{s, p ; m}(M)} \lesssim\|u\|_{\mathscr{H}^{s, p ; m}(M)} .$$
Pick a smooth compactly supported tensor $v_{0}$ on $M$ such that $\left\|\psi_{0} u-v_{0}\right\|_{X_{0}^{s, p}} \leq r^{\alpha}$ and define $v=\sum_{j=0}^{J} \psi_{j} u_{j}$. We claim that
$$\|\bar{u}-v\|_{X_{w}^{s, p}(M)} \lesssim r^{\alpha}$$
with implicit constant independent of $r$. Since $v$ has the desired smoothness, we are done once the claim is demonstrated.

Consider a Möbius parametrization $\Phi_{i}$ and let $\mathcal{N}(i)$ be the set of indices $j$ such that $v_{j}$ is not identically 0 on the image of $\Phi_{i}$. The uniform local finiteness provided by Lemma 8.13 ensures that the size of $\mathcal{N}(i)$ is uniformly bounded with respect to $r$ and hence
$$\begin{aligned}
\rho_{i}^{-w}\left\|\Phi_{i}^{*}(u-v)\right\|_{H^{s, p}\left(B_{2}^{\mathbb{H}}\right)} & \lesssim \sum_{j \in \mathcal{N}(i)} \rho_{i}^{-w}\left\|\Phi_{i}^{*}\left(\psi_{j} u-v_{j}\right)\right\|_{H^{s, p}\left(B_{2}^{\mathbb{H}}\right)} \\
& \lesssim \max _{j}\left\|\psi_{j} u-v_{j}\right\|_{X_{w}^{s, p}(M)} .
\end{aligned}$$
For $i \geq 1$, Lemma 8.6 and the observation (C.1) imply
$$\left\|\psi_{i} u-v_{i}\right\|_{X_{w}^{s, p}(M)}=\left\|\psi_{i}\left(u-u_{i}\right)\right\|_{X_{w}^{s, p}(M)} \lesssim r^{\alpha}\|u\|_{\mathscr{H}^{s, p ; m}(M)} .$$
A similar inequality holds for $i=0$ by construction, and the result follows from taking a supremum in inequality (C.2). \(\square\)

Corollary C.2. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}, s>n / p$ and $s \geq m$. Suppose $g$ is an asymptotically hyperbolic metric on $M$ of class $\mathscr{H}^{s, p ; m}$ with $m>n / p$ or of class $\mathscr{X}^{s, p ; m}$. Given $\varepsilon>0$ there is an asymptotically hyperbolic metric $g_{\varepsilon}$ with $\rho^{2} g_{\varepsilon} \in C^{\infty}(\bar{M})$ and
$$\left\|g-g_{\varepsilon}\right\|_{X_{0}^{s, p}\left(M ; T^{0,2} M\right)}<\varepsilon .$$

Proof. We assume that $g$ is of class $\mathscr{H}^{s, p ; m}$; the $\mathscr{X}^{s, p ; m}$ case is proved similarly. Let $\bar{g}^{-1}$ be the contravariant tensor dual to $\bar{g}=\rho^{2} g$ and recall, as discussed in §5, that $\bar{g}^{-1} \in \mathscr{H}^{s, p ; m}(M)$. Let $\widetilde{g}^{-1}$ be an approximating tensor obtained by the construction of the proof of Proposition C.1. So in a neighborhood of $\partial M, \widetilde{g}^{-1}=\sum_{j=1}^{J} \psi_{j} \bar{g}^{-1}\left[\hat{p}_{j}\right]$ for some collection of boundary points $\hat{p}_{j}$ and partition of unity $\left\{\psi_{j}\right\}$ provided by Lemma 8.13. At each $\hat{p}_{j}, \bar{g}^{-1}(d \rho, d \rho)=1$ and from the partition of unity construction it follows that $\widetilde{g}^{-1}(d \rho, d \rho)=1$ along all of $\partial M$. Thus $\rho^{2} \widetilde{g}^{-1}$ is dual to an asymptotically hyperbolic metric with smooth compactification and can be made as close to $g^{-1}$ as we want in $X_{0}^{s, p}(M)$. The result now follows, noting from the technique of Lemma 8.5 that the map between metrics and their duals is continuous on $X_{0}^{s, p}(M)$. \(\square\)

\section*{Appendix D. Improved regularity for Laplacians}

The general Fredholm mapping properties from Theorems (9.7) and (9.10) can be improved in some settings with respect to the Sobolev parameters. Consider the case of an asymptotically hyperbolic metric $g$ of class $\mathscr{H}^{1, p ; 1}$ with $p>n$ and its conformal Laplacian $L=-a_{n} \Delta_{g}+\mathrm{R}[g]$. Proposition 8.1 indicates that the operator is continuous $H_{\delta}^{\sigma, q}(M ; \mathbb{R}) \rightarrow H_{\delta}^{\sigma-2, q}(M ; \mathbb{R})$ so long as $\sigma=1$ and $1 / p \leq 1 / q \leq 1 / p^{*}$. The source of the very strong restriction on $\sigma$ is the scalar curvature term. First, since $\mathrm{R}[g] \in H_{\mathrm{loc}}^{-1, p}(M ; \mathbb{R})$, in order for $\mathrm{R}[g] u$ to be well defined, $u$ needs at least 1 derivative and therefore $\sigma \geq 1$. On the other hand, we cannot expect $L u$ to have more derivatives than the low order term, which leads to the condition $\sigma-2 \geq-1$ and hence $\sigma \geq 1$ as well.

For the standard Laplacian without the scalar curvature term the mapping range can be improved. Indeed for a metric of class $\mathscr{H}^{s, p ; m}$ with $s>n / p$ and $s \geq m \geq 1$ a computation using Proposition 3.11 shows that $\Delta_{g}: H_{\delta}^{\sigma, q}(M ; \mathbb{R}) \rightarrow H_{\delta}^{\sigma-2, q}(M ; \mathbb{R})$ is continuous so long as
$$\begin{aligned}
\sigma & \in[2-s, s+1] \\
\frac{1}{q}-\frac{\sigma}{n} & \in\left[\frac{1}{p}-\frac{s+1}{n}, \frac{1}{p^{*}}-\frac{2-s}{n}\right]
\end{aligned}$$
which should be compared with the standard restrictions (8.2) defining $\mathcal{S}_{2}^{s, p}$. Whereas for a general second order operator the most regular allowable spaces are $H_{\delta}^{s, p}(M ; \mathbb{R})$, for the Laplacian they are $H_{\delta}^{s+1, p}(M ; \mathbb{R})$. This distinction can matter in applications, for example, where conformal factors obtained using the Laplacian are required to have more regularity than the metric itself.

A Fredholm theory is possible for the Laplacian where the hypothesis $(\sigma, q) \in S_{2}^{s, p}$ in Theorems 9.7 and 9.10 is replaced with $(\sigma, q)$ satisfying (D.1). To see this , we first observe that the only role that $S_{2}^{s, p}$ plays in Section 8 is to ensure continuity of the differential operator as a map $H_{\delta}^{\sigma, q}(M) \rightarrow H_{\delta}^{\sigma-2, q}(M)$. With a missing low-order term this range can be increased to $(\sigma, q)$ satisfying (D.1) instead; the proofs of the results of Section 8 with the weaker hypothesis on ( $\sigma, q$ ) then go through unchanged. In particular, we obtain a variation of Proposition 8.16 specific to the Laplacian by replacing the condition $(\sigma, q) \in S_{2}^{s, p}$ with $(\sigma, q)$ satisfying (D.1), nothing that in this case the indicial radius $R$ appearing in the Proposition is that of the Laplacian on hyperbolic space, $(n-1) / 2$. With this semi-Fredholm result in hand, we obtain the following Fredholm theorem with the larger range of parameters (D.1) by using a variation of the approximation technique from Theorem 9.10.

Proposition D.1. Suppose $1<p<\infty, s \in \mathbb{R}, m \in \mathbb{N}$, with $s>n / p$ and $s \geq m \geq 1$. Let $g$ be an asymptotically hyperbolic metric on $M$ that is either
\begin{itemize}
\item[-] of class $\mathscr{H}^{s, p ; m}$ with $m>n / p$ or
\item[-] of class $\mathscr{X}^{s, p ; m}$.
\end{itemize}

Then $-\Delta_{g}$ is an isomorphism
$$H_{\delta}^{\sigma, q}(M ; \mathbb{R}) \rightarrow H_{\delta}^{\sigma-2, q}(M ; \mathbb{R})$$
so long as $(\sigma, q)$ satisfy (D.1) and
$$\left|\delta+\frac{n-1}{q}-\frac{n-1}{2}\right|<\frac{n-1}{2} .$$
Similarly, $-\Delta_{g}$ is an isomorphism
$$X_{\delta}^{s+1, p}(M ; \mathbb{R}) \rightarrow X_{\delta}^{s-1, p}(M ; \mathbb{R})$$
so long as ( $\sigma, q$ ) satisfy (D.1) and
$$\left|\delta-\frac{n-1}{2}\right|<\frac{n-1}{2} .$$

Proof. Fix some ( $\sigma, q$ ) satisfying (D.1) and some $\delta$ satisfying (D.2). As in the proof of Theorem 9.10, let $g_{n}$ be a sequence of metrics obtained from Corollary C. 2 with compactifications $\bar{g}_{n} \in C^{\infty}(\bar{M})$ that converge to $g$ in $X_{0}^{s, p}(M)$. As discussed in the proof of Proposition 6.3, the indicial radius of the Laplacian on hyperbolic space is $(n-1) / 2$ and hence for the smooth metrics $g_{n}, \Delta_{g_{n}}: H_{\delta}^{\sigma, q}(M) \rightarrow H_{\delta}^{\sigma-2, q}(M)$ is an isomorphism. The operators $\Delta_{g_{n}}$ converge to $\Delta_{g}$, which is semi-Fredholm by the variation of Proposition 8.16 discussed above. Thus $\Delta_{g}: H_{\delta}^{\sigma, q}(M) \rightarrow H_{\delta}^{\sigma-2, q}(M)$ is Fredholm with index zero.
It remains to show that the kernel is trivial. But if $u \in H_{\delta}^{\sigma, q}(M)$ is in the kernel and if ( $\sigma, q$ ) does not already satisfy $(\sigma, q) \in S_{2}^{p, s}$ then either by lowering $\sigma$ or by applying Lemma 3.2 and lowering $q$ while simultaneously lowering $\delta$ suitably we have $u \in H_{\delta^{\prime}}^{\sigma^{\prime}, q^{\prime}}(M)$ with $\left(\sigma^{\prime}, q^{\prime}\right) \in \mathcal{S}_{2}^{s, p}$ and $\left|\delta^{\prime}+(n-1) / q^{\prime}-(n-1) / 2\right|<(n-1) / 2$. At this point the parameters are within the range covered by Proposition 6.3 and we conclude $u=0$.

The Gicquad-Sakovich case is proved similarly. \(\square\)

Results analogous to Proposition D. 1 can be proved by similar techniques for other secondorder operators with either a missing low order term such as the vector Laplacian or with a manifestly smooth low-order term such as $-\Delta_{g}+\Lambda$ with $\Lambda$ a constant.

\section*{References}
\begin{itemize}
\item[] [AC96] Lars Andersson and Piotr T. Chruściel, Solutions of the constraint equations in general relativity satisfying "hyperboloidal boundary conditions", Dissertationes Math. (Rozprawy Mat.) 355 (1996), 100. MR 1405962 (97e:58217)
\item[] [ACF92a] Lars Andersson, Piotr T. Chruściel, and Helmut Friedrich, On the regularity of solutions to the Yamabe equation and the existence of smooth hyperboloidal initial data for Einstein's field equations, Comm. Math. Phys. 149 (1992), no. 3, 587-612. MR 1186044 (93i:53040)
\item[] [ACF92b] Lars Andersson, Piotr T. Chruściel, and Helmut Friedrich, On the regularity of solutions to the Yamabe equation and the existence of smooth hyperboloidal initial data for Einstein's field equations, Comm. Math. Phys. 149 (1992), no. 3, 587-612. MR 1186044
\item[] [AILSA16] Paul T. Allen, James Isenberg, John M. Lee, and Iva Stavrov Allen, The shear-free condition and constant-mean-curvature hyperboloidal initial data, Classical Quantum Gravity 33 (2016), no. 11, 115015, 28. MR 3502695
\item[] [AILSA18] \_\_\_\_, Weakly asymptotically hyperbolic manifolds, Comm. Anal. Geom. 26 (2018), no. 1, 1-61. MR 3761652
\item[] [AM03] Lars Andersson and Vincent Moncrief, Elliptic-hyperbolic systems and the Einstein equations, Ann. Henri Poincaré 4 (2003), no. 1, 1-34. MR 1967177 (2004c:58060)
\item[] [And93] Lars Andersson, Elliptic systems on manifolds with asymptotically negative curvature, Indiana Univ. Math. J. 42 (1993), no. 4, 1359-1388. MR 1266098 (94m:58231)
\item[] [CDLS05] Piotr T. Chruściel, Erwann Delay, John M. Lee, and Dale N. Skinner, Boundary regularity of conformally compact Einstein metrics, J. Differential Geom. 69 (2005), no. 1, 111-136. MR 2169584
\item[] [Fri18] Helmut Friedrich, Peeling or not peeling-is that the question?, Classical Quantum Gravity 35 (2018), no. 8, 083001, 18. MR 3789507
\item[] [GS12] Romain Gicquaud and Anna Sakovich, A large class of non-constant mean curvature solutions of the Einstein constraint equations on an asymptotically hyperbolic manifold, Comm. Math. Phys. 310 (2012), no. 3, 705-763. MR 2891872
\end{itemize}
[HMT22] Michael Holst, David Maxwell, and Gantumur Tsogterel, Interior elliptic estimates for operators with rough coefficients, in preparation, 2022.
[Lee06] John M. Lee, Fredholm operators and Einstein metrics on conformally compact manifolds, Mem. Amer. Math. Soc. 183 (2006), no. 864, vi+83. MR 2252687
[LP87] John M. Lee and Thomas H. Parker, The Yamabe problem, Bull. Amer. Math. Soc. (N.S.) 17 (1987), no. 1, 37-91. MR 888880
[Max06] David Maxwell, Rough solutions of the Einstein constraint equations, J. Reine Angew. Math. 590 (2006), 1-29. MR 2208126 (2006j:58044)
[Maz91] Rafe Mazzeo, Regularity for the singular Yamabe problem, Indiana Univ. Math. J. 40 (1991), no. 4, 1277-1299. MR 1142715
[Rin09] Hans Ringström, The Cauchy problem in general relativity, ESI Lectures in Mathematics and Physics, European Mathematical Society (EMS), Zürich, 2009. MR 2527641
[Sch01] Martin Schechter, Principles of functional analysis, Graduate studies in mathematics, American Mathematical Society, 2001.
[Sic96] Winfried Sickel, Composition operators acting on sobolev spaces of fractional order-a survey on sufficient and necessary conditions, Function spaces, differential operators and nonlinear analysis, Prometheus, 1996, pp. 159-182.
[Tay91] Michael E. Taylor, Pseudodifferential Operators and Nonlinear PDE, Birkhäuser Boston, Boston, MA, 1991 (en).
[Tay10] M.E. Taylor, Partial differential equations i: Basic theory, Applied Mathematical Sciences, Springer New York, 2010.
[Tri76] Hans Triebel, Spaces of Kudrjavcev type I. Interpolation, embedding, and structure, Journal of Mathematical Analysis and Applications 56 (1976), no. 2, 253-277.
[Tri10] \_\_\_\_, Theory of function spaces, Modern Birkhäuser Classics, Springer Basel, 2010.

Lewis \& Clark College, Portland, OR, USA
Email address: ptallen@lclark.edu