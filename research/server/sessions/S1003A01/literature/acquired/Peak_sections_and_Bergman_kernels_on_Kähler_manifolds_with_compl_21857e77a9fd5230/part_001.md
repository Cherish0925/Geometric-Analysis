---
retention_scope: session
part: 1
total_parts: 4
---

[Part 1/4 of: Peak sections and Bergman kernels on Kähler manifolds with complex hyperbolic cusps]

---
source_file: 2211_04091.pdf
converter: mathpix
format: mmd
---

\title{
PEAK SECTIONS AND BERGMAN KERNELS ON KÄHLER MANIFOLDS WITH COMPLEX HYPERBOLIC CUSPS
}

\author{
SHENGXUAN ZHOU
}

\begin{abstract}
By revisiting Tian's peak section method, we obtain a localization principle of the Bergman kernels on Kähler manifolds with complex hyperbolic cusps, which is a generalization of Auvray-Ma-Marinescu's localization result Bergman kernels on punctured Riemann surfaces [3]. Then we give some further estimates when the metric on the complex hyperbolic cusp is a Kähler-Einstein metric or when the manifold is a quotient of the complex ball. By applying our method directly to Poincaré type cusps, we also get a partial localization result.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. Preliminaries ..... 7
3. Bergman kernels on complex hyperbolic cusp ..... 10
3.1. Expression of the Bergman kernels on complex hyperbolic cusps ..... 10
3.2. Asymptotic behavior of Bergman kernel functions on complex hyperbolic cusps ..... 15
4. Localization of Bergman kernels ..... 19
4.1. Localization of peak sections ..... 19
4.2. Approximate the peak section by approximating the metric ..... 22
4.3. Peak sections on asymptotic complex hyperbolic cusps ..... 23
4.4. Peak sections on Poincaré type cusps ..... 32
5. Bergman kernels in two special cases ..... 38
5.1. Bergman kernels on complex hyperbolic cusps with Kähler-Einstein metrics ..... 38
5.2. Bergman kernels on quotients of complex ball ..... 47
6. Conflict of interest statement ..... 55
7. Data availability statements ..... 55
References ..... 55

\section*{1. Introduction}

Let $(M, \omega)$ be an $n$-dimensional Kähler manifold, and $\mathcal{L}$ be a positive line bundle on $M$ equipped with a hermitian metric $h$. Then we can define the Bergman space for each $m \in \mathbb{N}$ as the following Hilbert space
$$H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)=\left\{S \in H^{0}\left(M, \mathcal{L}^{m}\right): \int_{M}\|S\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega}<\infty\right\},$$
with the $L^{2}$ inner product $\left\langle S_{1}, S_{2}\right\rangle_{L^{2}, M ; \omega, h^{m}}=\int_{M}\left\langle S_{1}, S_{2}\right\rangle_{h^{m}} d \operatorname{Vol}_{\omega}$. Clearly, this space will also have a standard $L^{2}$ norm $\|S\|_{L^{2}, M ; h^{m}, \omega}=\left(\langle S, S\rangle_{L^{2}, M ; h^{m}, \omega}\right)^{\frac{1}{2}}$. Sometimes we denote the inner product and norm briefly by $\left\langle s_{1}, s_{2}\right\rangle_{L^{2}}$ and $\|s\|_{L^{2}}$, respectively. Hence the Bergman kernel can be defined as
$$B_{M, \omega, \mathcal{L}, h, m}(x, y)=\sum_{i \in I} S_{m, i}(x) \otimes\left(S_{m, i}(y)\right)^{*}, \quad \forall x, y \in M,$$
and the Bergman kernel function can be defined as
$$\rho_{M, \mathcal{L}, h, \omega, m}(x)=B_{M, \omega, \mathcal{L}, h, m}(x, x)=\sup _{S \in H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right)} \frac{\|S(x)\|_{h^{m}}^{2}}{\int_{M}\|S\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega}}=\sum_{i \in I}\left\|S_{m, i}(x)\right\|_{h^{m}}^{2},$$
for any $x \in M$, where $\left\{S_{m, i}\right\}_{i \in I}$ is an $L^{2}$ orthonormal basis associated with $h^{m}$ and $d \operatorname{Vol}_{\omega}=\frac{\omega^{n}}{n!}$ in the Hilbert space $H_{L^{2}}^{0}\left(M, \omega, \mathcal{L}^{m}, h^{m}\right)$. For abbreviation, we denote the Bergman space, Bergman kernel and Bergman kernel function briefly by $H_{L^{2}}^{0}\left(M, \mathcal{L}^{m}\right), B_{\omega, m}$ and $\rho_{\omega, m}$, respectively. Note that $B_{\omega, m}$ is a $\left(\pi_{1}^{*} \mathcal{L}^{m} \otimes \pi_{2}^{*} \mathcal{L}^{-m}\right)$-valued function on $M \times M$, and $\rho_{\omega, m}$ are functions on $M$, where $\pi_{i}$ is the projection of $M \times M$ onto the $i$-th component.

The Bergman kernel plays an important role in Kähler geometry. In the pioneering work [33], Tian used his peak section method to prove that Bergman metrics converge to the original polarized metric in the $C^{2}$-topology. By a similar method, Ruan [29] proved that this convergence is $C^{\infty}$. Later, Zelditch [35], also Catlin [5] independently, used the Szegö kernel to obtain an alternative proof of the $C^{\infty}$-convergence of Bergman metrics, moreover, they gave an asymptotic expansion of Bergman kernel function, which is the Kähler potential of the Bergman metric, on polarized Kähler manifolds. Such an asymptotic expansion is called the Tian-Yau-Zelditch expansion. This expansion can be also obtained by Tian's peak section method, see Liu-Lu [20]. By using the heat kernel, Dai-Liu-Ma [6] gave another proof of the Tian-Yau-Zelditch expansion and they further considered the asymptotic behavior of Bergman kernels on symplectic manifolds and Kähler orbifolds (see also Ma-Marinescu's book [24]). There are many important applications of the Tian-Yau-Zelditch expansion, for example, [9] and [34].

More recently, Auvray-Ma-Marinescu [3, 4] and Sun-Sun [31] independently considered the asymptotic behavior of the Bergman kernels on punctured Riemann surfaces. Sun-Sun also discusses the logarithmic K-semistability of punctured Riemann surfaces by considering the asymptotic behavior of the Bergman kernels in [31]. Through revisiting Tian's peak section method, we generalize the results of Auvray-Ma-Marinescu to Kähler manifolds with complex hyperbolic cusps. The results and methods presented in this paper can be applied to more general cases and may be helpful in understanding log-K stability or the geometry of Shimura varieties.

In this paper, an $n$-dimensional $(n \geq 1)$ complex hyperbolic cusp is defined in terms of a collection of data $\left(V / \Gamma_{V}, \omega_{V}, \mathcal{L}_{V} / \Gamma_{V}, h_{V}\right)$ with the following property. Let $\left(D, \omega_{D}\right)$ be a flat Abelian variety of complex dimension $n-1$, and $\left(\mathcal{L}_{D}, h_{D}\right)$ be a negative Hermitian line bundle on $D$ whose curvature form is $-\omega_{D}$. If $n=1$, the space $D$ becomes a point, and $\mathcal{L}_{D} \cong D \times \mathbb{C}$. Then $\partial \bar{\partial}$-lemma implies that $h_{D}$ is unique up to scaling. It is clear that $v \mapsto h_{D}(v, v)$ gives a smooth function on the total space $\mathcal{L}_{D}$. By a straightforward computation, we see that $\omega_{V}=-\sqrt{-1} \partial \bar{\partial} \log \left(-\log h_{D}\right)$ is a Kähler form on $V=\left\{0<h_{D}<1\right\}$ with $\operatorname{Ric}\left(\omega_{V}\right)=-(n+1) \omega_{V}$, where $\pi_{D}: \mathcal{L}_{D} \rightarrow D$ is the projection of line bundle. For $r>0$, we will denote by $V_{r}$ the open subset $\left\{0<h_{D}<r\right\}$ of the total space of $\mathcal{L}_{D}$. Let $\mathcal{L}_{V}$ be a trivial line bundle on $V$ with a Hermitian metric $h_{V}$, such that there exists a section $e_{\mathcal{L}_{V}} \in H^{0}\left(V, \mathcal{L}_{V}\right)$ satisfying that $\left\|e_{\mathcal{L}_{V}}\right\|_{h_{V}}^{2}=\left|\log h_{D}\right|$. Let $\Gamma_{V}$ be a finite subgroup of $\operatorname{Aut}\left(V, \omega_{V}\right)$. Since $h_{D}$ is invariant under the action of $\operatorname{Aut}\left(V, \omega_{V}\right)$ on $V$, the action of $\Gamma_{V}$ on $V$ can be extended
to the total space of $\mathcal{L}_{D}$ (see also Lemma 3.3). Now we further extend the action of $\Gamma_{V}$ on $V$ to the total space of the line bundle $\mathcal{L}_{V}$ such that the biholomorphic maps corresponding to the action are automorphisms of the line bundle $\mathcal{L}_{V}$, and $h_{V}$ is invariant under this action. Then there exists a homomorphism $\Theta_{\Gamma_{V}}: \Gamma_{V} \rightarrow U(1) \subset \mathbb{C}^{*}$ such that $g\left(e_{\mathcal{L}_{V}}\right)=\Theta_{\Gamma_{V}}(g) e_{\mathcal{L}_{V}}, \forall g \in \Gamma_{V}$. If $\Gamma_{V}=0$, we can omit it in the notations. More details about complex hyperbolic cusps can be found in Mok's paper [26].

Now we define the asymptotic complex hyperbolic cusp, which is our main local model in this paper.

Definition 1.1 (Asymptotic complex hyperbolic cusp). Let $(M, \omega)$ be a Kähler manifold, let $(\mathcal{L}, h)$ be a Hermitian line bundle on $M$ and let $\alpha>0$ be a constant. We say that an open subset $U$ of $M$ is an asymptotic complex hyperbolic cusp of order $\alpha$ if it satisfies that:
\begin{itemize}
\item[1)] $\operatorname{Ric}(h)=\omega$ on $U$.
\item[2)] There exist a complex hyperbolic cusp $\left(V / \Gamma_{V}, \omega_{V}, \mathcal{L}_{V} / \Gamma_{V}, h_{V}\right)$, a constant $r \in\left(0, e^{-1}\right)$, a biholomorphic map $\varphi_{U}: V_{r} / \Gamma_{V} \rightarrow U$ and a section $e_{\mathcal{L}} \in H^{0}\left(U,\left.\mathcal{L}\right|_{U}\right)$ such that $\left\|e_{\mathcal{L}}\right\|_{h}^{2} \circ \varphi_{U}=$ $e^{u}\left|\log h_{D}\right|$, where $u=O\left(\left|\log h_{D}\right|^{-\alpha}\right)$ as $h_{D} \rightarrow 0^{+}$to all orders with respect to $\omega_{V}$.
\end{itemize}
Moreover, we say that $U$ is an asymptotic complex hyperbolic cusp of order $\infty$ if for any $p \in \mathbb{N}$, $u=O\left(\left|\log h_{D}\right|^{-p}\right)$ as $h_{D} \rightarrow 0^{+}$to all orders with respect to $\omega_{V}$.

By abuse of notation, it is sometimes convenient to write $V_{r} / \Gamma_{V}$ instead of $U$.
Since $M$ is a manifold, we see that the action of the group $\Gamma_{V}$ on $V$ is free in Definition 1.1, and $\mathcal{L}_{V} / \Gamma_{V}$ is a line bundle. In general, the quotient space $V / \Gamma_{V}$ is only an orbifold, and $\mathcal{L}_{V} / \Gamma_{V}$ is only a line orbibundle. Before we state our first main result, we need the following assumption.

Definition 1.2 (Admissible pair). Let $m \in \mathbb{N}$ and $\xi, \kappa, r>0$. Then a pair $(\gamma, \sigma) \in \mathbb{R}_{+}^{2}$ is said to be $(m, \xi, \kappa, r)$-admissible if $r \geq \sigma, \gamma \geq e^{-\kappa \frac{\sqrt{m}}{\log m}}$ and $\log \sigma \geq e^{-\xi \frac{\log m}{\sqrt{m}}} \log \gamma$.

For using Hörmander's $L^{2}$-estimate, we need the following condition for non-complete Kähler manifold. This is a modification of the standard pseudoconvex, i.e., the existence of a psh exhaustion function.

Definition 1.3 (Pseudoconvex). In this paper, we say that a Kähler manifold $(M, \omega)$ is pseudoconvex if there exists a proper plurisubharmonic function $\psi \in C^{\infty}(M ; \mathbb{R})$ such that $\psi^{-1}((-\infty, k])$ is the union of a compact subset and finitely many complex hyperbolic cusps for any $k \in \mathbb{R}$, and $M=\cup_{k=1}^{\infty} \psi^{-1}((-\infty, k])$.

Remark. Note that complex hyperbolic cusp $V_{r}$ is always complete as $h_{D} \rightarrow 0$, so Hörmander's $L^{2}$-estimate holds for $\bar{\partial}$-closed (0, 1)-form with compact support on pseudoconvex manifold. Let $\psi=-\log \left(r-\log h_{D}\right)$. We see that $\left(V_{r}, \omega\right)$ are pseudoconvex in this sense.

Now we can state our first main result, which is the following localization principle. The following result is the higher dimensional analogue of [3, Theorem 1.1-2] and [4, Theorem 1.2].

Theorem 1.1. Let $(M, \omega)$ be a Kähler manifold, let $(\mathcal{L}, h)$ be a Hermitian line bundle on $M$ and $\alpha>0$ be a constant such that $U \cong V_{r} / \Gamma_{V}$ is an asymptotic complex hyperbolic cusp of order $\alpha$, and $\operatorname{Ric}(h) \geq \epsilon \omega$ and $\operatorname{Ric}(\omega) \geq-\Lambda \omega$ for some constants $\epsilon, \Lambda>0$. Suppose that if $(M, \omega)$ is not complete, then $M$ is pseudoconvex and $\bar{U}$ is complete.

Let $B_{V_{t} / \Gamma_{V}, \omega, m}(x, y)$ denotes the Bergman kernel on $\left(V_{t} / \Gamma_{V}, \omega, \mathcal{L}, h\right)$. Given constants $\xi, \kappa, \beta>0$. Then there exists a large constant $C>1$ satisfying the following property.

Let $m \in \mathbb{N}$, and $\left(\gamma_{m}, \sigma_{m}\right)$ be an $(m, \xi, \kappa, r)$-admissible. Then for any $m \in \mathbb{N}$, the Bergman kernel satisfying that
$$\left\|B_{M, \omega, m}(x, y)\right\|_{C^{k} ; h^{m}, \omega} \leq C m^{-l}\left|\log h_{D}(x)\right|^{-\beta}\left|\log h_{D}(y)\right|^{-\beta},$$
for any $(x, y) \in\left(\pi_{V}\left(V_{\gamma_{m}}\right) \times\left(U \backslash \pi_{V}\left(V_{\sigma_{m}}\right)\right)\right) \cup\left(\left(U \backslash \pi_{V}\left(V_{\gamma_{m}}\right)\right) \times \pi_{V}\left(V_{\gamma_{m}}\right)\right)$, and
$$\left\|B_{V_{\sigma_{m}} / \Gamma_{V}, \omega, m}(x, y)-B_{M, \omega, m}(x, y)\right\|_{C^{k} ; h^{m}, \omega} \leq C m^{-l}\left|\log h_{D}(x)\right|^{-\beta}\left|\log h_{D}(y)\right|^{-\beta},$$
for any $(x, y) \in \pi_{V}\left(V_{\gamma_{m}}\right) \times \pi_{V}\left(V_{\gamma_{m}}\right)$, where $\pi_{V}$ is the quotient map $V \rightarrow V / \Gamma_{V} \cong U,\|\cdot\|_{C^{k} ; h^{m}, \omega}$ is the $C^{k}$-norm associate with the Hermitian metric $\pi_{1}^{*} h^{m} \otimes \pi_{2}^{*} h^{-m}$ and the Kähler metric $\omega$ on $U \times U$.

Moreover, when $m \geq C$, the Bergman kernel functions satisfying that
$$\sup _{V_{\gamma_{m}} / \Gamma_{V}}\left|\frac{\rho_{M, \omega, m}(x)}{\rho_{V_{\sigma_{m}} / \Gamma_{V}, \omega, m}(x)}-1\right| \leq C m^{-l} .$$
Remark. Since there exists a constant $\delta>0$ independent of $m$ such that inj $\left(U \backslash V_{\gamma_{m}}\right) \geq \delta \frac{\log m}{\sqrt{m}}$ (see Lemma 4.3), we see that the asymptotic behavior of $B_{M, \omega, m}(x, y)$ on $\left(U \backslash V_{\gamma_{m}}\right) \times\left(U \backslash V_{\gamma_{m}}\right)$ is same to the standard case. See [14, p. 2242] or [24, Chapter 4] for details in the standard case.

Our proof of Theorem 1.1 is based on Tian's Peak section method. The key step, Proposition 4.1, is to show that the decay speed of the peak sections is sufficiently fast at a distance. We can use the Agmon type estimate (see Corollary 4.1) to obtain this estimate by observing the Bergman kernels can be represented simply by the peak sections.

Now we will give some refinements of Theorem 1.1 in two special cases. The first case is about the complex hyperbolic cusps with Kähler-Einstein metrics. We now recall some properties of it.

Fix a polarized $(n-1)$-dimensional flat Abelian variety $\left(D, \omega_{D}\right)$ with polarization $\left(\mathcal{L}_{D}^{-1}, h_{D}^{-1}\right)$. Now we can construct an $n$-dimensional complex hyperbolic cusp $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$ by the statement before Theorem 1.1, where $V=\left\{0<h_{D}<1\right\}$ is an open subset of the total space of the line bundle $\mathcal{L}_{D}, \omega_{V}=-\sqrt{-1} \partial \bar{\partial} \log \left(-\log h_{D}\right)$, and $\left(\mathcal{L}_{V}, h_{V}\right) \cong\left(\mathbb{C},-\log h_{D}\right)$ is a Hermitian line bundle on $V$. Let $r \in(0,1)$ be a constant.

For any given smooth real-valued function $f \in C^{\infty}\left(\partial \bar{V}_{r}\right)$, Datar-Fu-Song [7, Theorem 1.1, Theorem 1.3] proved that there exists a unique complete Kähler-Einstein metric $\omega_{r, f}=\omega_{V}+$ $\sqrt{-1} \partial \bar{\partial} u_{r, f}$ on $V_{r}$ by considering the Dirichlet problem of the Monge-Ampére equation, where $V_{r}=\left\{0<h_{D}<r\right\} \subset V$, and $u_{r, f} \in C\left(\bar{V}_{r}\right)$ is a smooth real-valued function on $V_{r}$ such that $\left.u_{r, f}\right|_{\partial \bar{V}_{r}}=f$, and $\left|u_{r, f}\right|=o(1)$ as $h_{D} \rightarrow 0^{+}$. When $n \geq 2$, Fu-Hein-Jiang [10, Main Theorem] further studied the asymptotic behavior of $\omega_{r, f}$ and $u_{r, f}$ by establishing sharper estimates. For any $k \in \mathbb{Z}_{\geq 0}$, they proved that there exists a constant $c_{r, f} \in \mathbb{R}$ such that
$$\left\|\nabla^{k}\left(u_{r, f}+\log \left(1+c_{r, f}\left|\log h_{D}\right|^{-1}\right)\right)\right\|_{\omega_{V}}=O\left(\left|\log h_{D}\right|^{\frac{n+k}{2}-\frac{1}{4}} e^{-2 \sqrt{\lambda_{1, D}\left|\log h_{D}\right|}}\right)$$
as $h_{D} \rightarrow 0^{+}$, where $\lambda_{1, D}>0$ denotes the first eigenvalue of $(D, \omega)$. See [10, Main Theorem] for more details. By considering the change of the Hermitian line bundle under the scalar multiplication $v \mapsto e^{-\frac{c_{r, f}}{2}} v$ on the total space of $\mathcal{L}_{D}$, (4) implies that the data $\left(V_{r}, \omega_{r, f}, \mathcal{L}_{V}, e^{-u_{r, f}} h_{V}\right)$ is an asymptotic hyperbolic cusp of order $\infty$. See also Lemma 5.1. Since the Kähler metrics on asymptotic hyperbolic cusps can always be expressed as $\omega_{V}+\sqrt{-1} \partial \partial u$ for some function $u$, Fu-Hein-Jiang's estimate holds for all asymptotic hyperbolic cusps with Kähler-Einstein metrics.

Now we can state our result for the Bergman kernels on asymptotic complex hyperbolic cusps with Kähler-Einstein metric. For abbreviation, we denote $e^{-\frac{\sqrt{m}}{\log (m)}}$ briefly by $r_{m}$ for any $m \geq 2$. When $\Gamma_{V}=0$ and $\mathcal{L}_{D}^{-1}$ is globally generated, the $C^{0}$-estimates for the quotients between Bergman kernel functions, (7) and (9), can be improved to the $C^{k}$ estimates. We will prove them in Proposition 5.2 and Proposition 5.4, respectively. Note that the $C^{k}$ estimates (7) and (9) is given in [4, Theorem 1.3] in the 1-dimensional case.

Theorem 1.2. Let $(M, \omega)$ be a Kähler manifold and let $(\mathcal{L}, h)$ be a Hermitian line bundle on $M$ such that $\operatorname{Ric}(h) \geq \epsilon \omega$ and $\operatorname{Ric}(\omega) \geq-\Lambda \omega$ for some constants $\epsilon, \Lambda>0$. Suppose that $M$ is pseudoconvex if $(M, \omega)$ is not complete.

Assume that $U \cong V_{r} / \Gamma_{V}$ is an asymptotic complex hyperbolic cusp of order $\infty$ on $(M, \omega, \mathcal{L}, h)$ such that $\bar{U}$ is complete. Then for any given constants $k, l \in \mathbb{N}$ and $\beta>0$, there are constants $m_{0}, C>0$ such that for any integer $m \geq m_{0}$, the Bergman kernels satisfying that
$$\left\|B_{M, \omega, m}(x, y)\right\|_{C^{k} ; h_{V}^{m}, \omega_{V}} \leq C m^{-l}\left|\log h_{D}(x)\right|^{-\beta}\left|\log h_{D}(y)\right|^{-\beta},$$
for any $(x, y) \in\left(\pi_{V}\left(V_{r_{m}^{e}}\right) \times\left(U \backslash \pi_{V}\left(V_{r_{m}}\right)\right)\right) \cup\left(\left(U \backslash \pi_{V}\left(V_{r_{m}}\right)\right) \times \pi_{V}\left(V_{r_{m}^{e}}\right)\right)$, and
$$\left\|B_{M, \omega, m}(x, y)-B_{V / \Gamma_{V}, \omega_{V}, m}(x, y)\right\|_{C^{k} ; h_{V}^{m}, \omega_{V}} \leq C m^{-l}\left|\log h_{D}(x)\right|^{-\beta}\left|\log h_{D}(y)\right|^{-\beta},$$
for any $(x, y) \in \pi_{V}\left(V_{r_{m}}\right) \times \pi_{V}\left(V_{r_{m}}\right)$. Moreover, the Bergman kernel functions satisfying that
$$\sup _{V_{r_{m}}}\left|\frac{\rho_{M, \omega, m}(x)}{\rho_{V / \Gamma_{V}, \omega_{V}, m}(x)}-1\right| \leq C m^{-l},$$
where $\|\cdot\|_{C^{k} ; h^{m}, \omega}$ is the $C^{k}$-norm associate with the Hermitian metric $\pi_{1}^{*} h^{m} \otimes \pi_{2}^{*} h^{-m}$ and the Kähler metric $\pi_{1}^{*} \omega+\pi_{2}^{*} \omega$ on $V \times V$.

The next case is about the quotients of the complex hyperbolic ball. Let $\left(\mathbb{B}^{n}, \omega_{\mathbb{B}}\right)$ be the $n$ -dimensional complex hyperbolic ball with constant bisectional curvature -1, and let $\Gamma$ be a lattice in $\operatorname{Aut}\left(\mathbb{B}^{n}, \omega_{\mathbb{B}}\right) \cong P U(n, 1)$. Here $\Gamma$ is a lattice means that $\Gamma$ is a discrete subgroup of $P U(n, 1)$ such that $\left(\mathbb{B}^{n} / \Gamma, \omega_{\mathbb{B}}\right)$ has finite volume. When all parabolic elements of $\Gamma$ are unipotent, there exist a finite collection of disjoint open subsets $U_{i} \subset \mathbb{B}^{n} / \Gamma, i=1, \cdots, N$, and complex hyperbolic cusps $\left(V_{i}, \omega_{V_{i}}, \mathcal{L}_{V_{i}}, h_{V_{i}}\right)$ such that $\left(U_{i}, \omega_{\mathbb{B}^{n}}\right) \cong\left(V_{i}, \omega_{V_{i}}\right)$, and $\left(\mathbb{B}^{n} / \Gamma\right) \backslash\left(\cup_{i=1}^{N} U_{i}\right)$ is compact. See [26, Theorem 1] for more details. Note that any neat lattice in $P U(n, 1)$ satisfies the above condition, and hence $\mathbb{B}^{n} / \Gamma$ can be decomposed as above when $\Gamma \subset P U(n, 1)$ is a neat lattice.

Recall that any lattice admits a finite index neat normal sublattice [28, Theorem 6.11]. Let $\Gamma_{\text {neat }} \unlhd \Gamma$ be a neat normal sublattice such that $\Gamma^{\prime}=\Gamma / \Gamma_{\text {neat }}$ is a finite group. It follows that $\mathbb{B}^{n} / \Gamma \cong\left(\mathbb{B}^{n} / \Gamma_{\text {neat }}\right) / \Gamma^{\prime}$. The decomposition result of $\mathbb{B}^{n} / \Gamma_{\text {neat }}$ now implies that there exist a finite collection of disjoint open subsets $U_{i} \subset \mathbb{B}^{n} / \Gamma, i=1, \cdots, N$, and complex hyperbolic cusps $\left(V_{i} / \Gamma_{V_{i}}, \omega_{V_{i}}, \mathcal{L}_{V_{i}} / \Gamma_{V_{i}}, h_{V_{i}}\right)$ such that $\left(U_{i}, \omega_{\mathbb{B}^{n}}\right) \cong\left(V_{i} / \Gamma_{V_{i}}, \omega_{V_{i}}\right)$, and $\left(\mathbb{B}^{n} / \Gamma\right) \backslash\left(\cup_{i=1}^{N} U_{i}\right)$ is compact. Now we suppose that $\mathbb{B}^{n} / \Gamma$ is a manifold, that is to say the lattice $\Gamma$ is torsion free. At this time, $\mathbb{B}^{n} / \Gamma$ satisfies the following assumptions at infinity.

Theorem 1.3. Let $(M, \omega)$ be a Kähler manifold and let $(\mathcal{L}, h)$ be a Hermitian line bundle on $M$ such that $\operatorname{Ric}(h) \geq \epsilon \omega$ and $\operatorname{Ric}(\omega) \geq-\Lambda \omega$ for some constants $\epsilon, \Lambda>0$. Suppose that $M$ is pseudoconvex if $(M, \omega)$ is not complete.

We follow the notations used in Definition 1.1. Assume that $U \cong V_{r}$ is an asymptotic complex hyperbolic cusp on $(M, \omega, \mathcal{L}, h)$ that satisfies $u=0$ and $\bar{U}$ is complete. Then for any given constants
$k, l \in \mathbb{N}$ and $\beta>0$, there are constants $m_{0}, C>0$ such that for any integer $m \geq m_{0}$, the Bergman kernels satisfying that
$$\sup _{V_{r^{2}} \times V_{r^{2}}}\left|\log h_{D}(x)\right|^{\beta}\left|\log h_{D}(y)\right|^{\beta}\left\|B_{M, \omega, m}(x, y)-B_{V / \Gamma_{V}, \omega_{V}, m}(x, y)\right\|_{C^{k} ; h_{V}^{m}, \omega_{V}} \leq C m^{-l},$$
and the Bergman kernel functions satisfying that
$$\sup _{V_{r}^{2}}\left|\frac{\rho_{M, \omega, m}(x)}{\rho_{V / \Gamma_{V}, \omega_{V}, m}(x)}-1\right| \leq C m^{-l},$$
where $\|\cdot\|_{C^{k} ; h^{m}, \omega}$ is the $C^{k}$-norm associate with the Hermitian metric $\pi_{1}^{*} h^{m} \otimes \pi_{2}^{*} h^{-m}$ and the Kähler metric $\pi_{1}^{*} \omega+\pi_{2}^{*} \omega$ on $\left(V / \Gamma_{V}\right) \times\left(V / \Gamma_{V}\right)$.

Remark. In the case $n=1$, we give a new proof of Auvray-Ma-Marinescu's estimate for Bergman kernels on punctured Riemann surfaces [3, Theorem 1.1] that relies on Tian's peak section method.

Let $X=\mathbb{B}^{n} / \Gamma$, and let $\mathcal{K}_{X}$ be the canonical bundle on $X$. Then the Kähler metric $\omega_{\mathbb{B}^{n}}$ gives a Hermitian metric $h_{X}$ on $\mathcal{K}_{X}$. Since Ric $\left(\omega_{\mathbb{B}^{n}}\right)=-(n+1) \omega_{\mathbb{B}^{n}}$, we have $\operatorname{Ric}\left(h_{X}\right)=(n+1) \omega_{\mathbb{B}^{n}}$, and hence $\left(X,(n+1) \omega_{\mathbb{B}^{n}}, \mathcal{K}_{X}, h_{X}\right)$ is a polarized complete Kähler orbifold. Now we can describe the asymptotic behavior of the supremum of the Bergman kernel functions of $\left(X, \omega_{\mathbb{B}^{n}}, \mathcal{K}_{X}, h_{X}\right)$. This is the higher dimensional analogue of [3, Corollary 1.4]. Note that Theorem 1.1 also holds for Kähler orbifolds with asymptotic complex hyperbolic cusps, so we don't need to assume that $\Gamma$ is torsion free here.

Theorem 1.4. Under the conditions stated above, there exist an integer $\mathcal{N}=\mathcal{N}(n, \Gamma) \in \mathbb{N}$, a constant $C=C(n, \Gamma)>0$, and a sequence of positive constants $\left\{c_{i}\right\}_{i=1}^{\infty}$, such that $c_{i}=c_{i+\mathcal{N}}$, $\forall i \in \mathbb{N}$, and satisfy the following properties.

If $\Gamma$ is cocompact, then
$$\sup _{X} \rho_{X, \omega_{\mathbb{B}} n}, \mathcal{K}_{X}, h_{X}, m=c_{m} m^{n}+O\left(m^{n-1}\right), \text { as } m \rightarrow \infty .$$

If $\Gamma$ is not cocompact, then
$$\sup _{X} \rho_{X, \omega_{\mathbb{B}} n}, \mathcal{K}_{X}, h_{X}, m=c_{m} m^{n+\frac{1}{2}}+O\left(m^{n}\right), \text { as } m \rightarrow \infty .$$

Moreover, if $\Gamma$ is neat, then $\mathcal{N}=1$.
Estimates for the upper bound of the Bergman kernel functions of the Shimura varieties are relevant in arithmetic geometry [1, 3, 18, 25]. It is possible to generalize our argument for Theorem 1.4 to the more general Shimura varieties, and possibly useful for arithmetic geometry.

Now we apply the arguments in the proof of Theorem 1.1 to Poincaré type cusps. The basic model of the Poincaré type cusp consists of a Kähler manifold $\left(\mathbb{D}_{r}^{*}\right)^{k} \times B_{r}^{2 n-2 k}(0)$ and a Kahler metric $-\sqrt{-1} \sum_{i=1}^{k} \partial \bar{\partial} \log \left(\log \left|z_{i}\right|^{2}\right)+\pi_{k, n}^{*} \omega_{k, n}$ on $\left(\mathbb{D}_{r}^{*}\right)^{k} \times B_{r}^{2 n-2 k}(0)$, where $\pi_{k, n}$ is the projection of $\left(\mathbb{D}_{r}^{*}\right)^{k} \times B_{r}^{2 n-2 k}(0) \subset \mathbb{C}^{n}$ onto $B_{r}^{2 n-2 k}(0), \omega_{k, n}$ is a Kähler metric on $B_{r}^{2 n-2 k}(0)$, and $\mathbb{D}_{r}=$ $\left\{z \in \mathbb{C}||z|<r\}, \mathbb{D}_{r}^{*}=\{z \in \mathbb{C}|0<|z|<r\}\right.$ for any $r>0$. By abuse of notation, we will write the Kähler metric $-\sqrt{-1} \sum_{i=1}^{k} \partial \bar{\partial} \log \left(\log \left|z_{i}\right|^{2}\right)+\pi_{k, n}^{*} \omega_{k, n}$ above simply $\omega_{\text {mod }, k, n}$ when $\omega_{k, n}$ is an Euclidean metric.

Fix a simple normal crossing divisor $D$ in an $n$-dimensional compact Kähler manifold $\bar{M}$. By definition, we see that for each $x \in D$, there exists a neighborhood $U_{x}$ of $x$ and a biholomorphic
map
$$\varphi_{x}: U_{x} \backslash D \rightarrow \prod_{i=1}^{k_{x}} \mathbb{D}_{r_{x, i}}^{*} \times B_{r_{x, k, n}}^{2 n-2 k_{x}}(0) \subset\left(\mathbb{D}_{1}^{*}\right)^{k_{x}} \times \mathbb{C}^{n-k_{x}},$$
where $r_{x, j} \in(0,1]$ and $r_{x, k, n}>0$ are constants. Let $\omega$ be a Kähler metric on $\bar{M} \backslash D$. Then we say that $\omega$ is a metric with Poincaré type cusp along $D$ if for any $x \in U$, the data $\left(U_{x}, \varphi_{x}\right)$ constructed above satisfying that
$$\left(\varphi_{x}^{-1}\right)^{*} \omega=-\sqrt{-1} \sum_{i=1}^{k} \partial \bar{\partial} \log \left(\log \left|z_{i}\right|^{2}\right)+\pi_{k, n}^{*} \omega_{k, n}+\sqrt{-1} \partial \bar{\partial} u_{x}$$
where $u_{x}$ is a smooth function on $\prod_{i=1}^{k_{x}} \mathbb{D}_{r_{x, i}}^{*} \times B_{r_{x, k, n}}^{2 n-2 k_{x}}(0)$, and there exists a constant $\alpha>0$ such that $u_{x} \in \cap_{i=1}^{k_{x}} O\left(|\log | z_{i}| |^{-\alpha}\right)$ as $\inf _{1 \leq i \leq k_{x}}\left|z_{i}\right| \rightarrow 0^{+}$to all orders with respect to $\left(\varphi_{x}^{-1}\right)^{*} \omega$.

Let $M$ denote the manifold $\bar{M} \backslash D$. Suppose that $(M, \omega)$ is a complete Kähler manifold with Poincaré type cusp along $D$ and $(\mathcal{L}, h)$ is a Hermitian line bundle on $M$ such that $\operatorname{Ric}(h) \geq \epsilon \omega$ and $\operatorname{Ric}(\omega) \geq-\Lambda \omega$ for some constants $\epsilon, \Lambda>0$. We further assume that for any $x \in D$, there exists a local frame $e_{x} \in H^{0}\left(U_{x} \backslash D, \mathcal{L}\right)$ such that $\left\|e_{x}\right\|^{2}=e^{-u_{x}-\tau_{k, n} \circ \pi_{k, n}}\left(\left.\prod_{i=1}^{k_{x}}|\log | z_{i}\right|^{2} \mid\right)$, where $\pi_{k, n}$ is the projection of $\left(\mathbb{D}_{1}^{*}\right)^{k} \times \mathbb{C}^{n-k}$ onto $\mathbb{C}^{n-k}$, and $\tau_{k, n}$ is a Kähler potential of $\omega_{k, n}$. It follows that $\operatorname{Ric}(h)=\omega$ on a neighborhood of $D$.

By imitating the argument in the proof of Theorem 1.1, one can give an analogy of Theorem 1.1 on Kähler manifolds with Poincaré type cusps.

Proposition 1.1. Let $\bar{M}$ be a compact Kähler manifold, $D$ be a simple normal crossing divisor, and $(M, \omega)=(\bar{M} \backslash D, \omega)$ be a complete Kähler manifold with Poincaré type cusp along $D$. Assume that $(\mathcal{L}, h)$ be a positive line bundle on $M$ that satisfies the above conditions. For any open subset $U \subset M$, we will denote by $B_{U, \omega, m}(x, y)$ the Bergman kernel on ( $U, \omega, \mathcal{L}, h$ ). Fix a Riemannian metric $\bar{g}$ on $\bar{M}$. Write $\bar{d}(x)=\operatorname{dist}_{\bar{g}}(x, D), \forall x \in M$. Given constants $\xi, \kappa, \beta>0$. Then there exists a constant $C>0$ satisfying the following property.

Let $m \geq C$ be an integer, and $\left(U_{m}, U_{m}^{\prime}\right)$ be a pair of open subsets of $M$ such that the distance $\operatorname{dist}_{\omega}\left(U_{m}^{\prime}, M \backslash U_{m}\right) \geq \xi \frac{\log m}{\sqrt{m}}$, and $\left\{x \in M \left\lvert\, \bar{d}(x) \leq e^{-\kappa \frac{\sqrt{m}}{\log m}}\right.\right\} \subset U_{m}^{\prime}$. Then the Bergman kernel satisfying that
$$\begin{aligned}
\sup _{U_{m}^{\prime} \times\left(M \backslash U_{m}\right) \cup\left(M \backslash U_{m}\right) \times U_{m}^{\prime}}|\log \bar{d}(x)|^{\beta}|\log \bar{d}(y)|^{\beta}\left\|B_{\omega, m}(x, y)\right\|_{C^{k}} & \leq C m^{-l}, \\
\sup _{U_{m}^{\prime} \times U_{m}^{\prime}}|\log \bar{d}(x)|^{\beta}|\log \bar{d}(y)|^{\beta}\left\|B_{U_{m}, \omega, m}(x, y)-B_{\omega, m}(x, y)\right\|_{C^{k}} & \leq C m^{-l} .
\end{aligned}$$

This paper is organized as follows. In Section 2, we collect some preliminary results that will be used many times. Then we will calculate the Bergman kernels on the complex hyperbolic cusp in Section 3. The proofs of Theorem 1.1 and Proposition 1.1 are presented in Section 4. Finally, the proofs of Theorem 1.2, Theorem 1.3, and Theorem 1.4 are contained in Section 5.

Acknowledgement. I would like to express my deepest gratitude to Professor Gang Tian, my supervisor, for his constant encouragement and guidance.

\section*{2. Preliminaries}

Now we state the Hömander's $L^{2}$ estimate as follows without proof.

Proposition 2.1. Let $(M, \omega)$ be an $n$-dimensional complete Kähler manifold. Let $(\mathcal{L}, h)$ be a hermitian holomorphic line bundle, and let $\psi$ be a function on $M$, which can be approximated by a decreasing sequence of smooth function $\left\{\psi_{i}\right\}_{i=1}^{\infty}$. Suppose that
$$\sqrt{-1} \partial \bar{\partial} \psi_{i}+\operatorname{Ric}(\omega)+\operatorname{Ric}(h) \geq \gamma \omega$$
for some positive continuous function $\gamma$ on $M, \forall i \in \mathbb{N}$. Then for any $\mathcal{L}$-valued (0, 1)-form $\zeta \in L^{2}$ on $M$ with $\bar{\partial} \zeta=0$ and $\int_{M}\|\zeta\|^{2} e^{-\psi} \omega^{n}$ finite, there exists a $\mathcal{L}$-valued function $u \in L^{2}$ such that $\bar{\partial} u=\zeta$ and
$$\int_{M}\|u\|^{2} e^{-\psi} \omega^{n} \leq \int_{M} \gamma^{-1}\|\zeta\|^{2} e^{-\psi} \omega^{n},$$
where $\|\cdot\|$ denotes the norms associated with $h$ and $\omega$.
The proof of Hömander's $L^{2}$ estimate can be found in [8, Chapter 5] or [15, Chapter IV]. Note that the $L^{2}$ estimate also holds for complete Kähler orbifolds [23, Proposition 2] and weakly pseudoconvex Kähler manifolds [8, Corollary 5.3].

We introduce the Cheeger-Gromov $C^{m, \alpha}$-norm for Kähler manifolds now.
Definition 2.1 (Holomorphic Norms). Let $(M, \omega, x)$ be a pointed Kähler manifold. We say that the holomorphic $C^{m, \alpha}$-norm on the scale of $r$ at $x$ :
$$\|(M, \omega, x)\|_{C^{m, \alpha}, r}^{\text {holo }} \leq Q,$$
provided there exists a biholomorphic chart $\phi: B_{r}(0) \rightarrow(U, x) \subset M$ such that $\phi(0)=x,|D \phi| \leq$ $e^{Q}$ on $B_{r}(0)$ and $\left|D \phi^{-1}\right| \leq e^{Q}$ on $U$, and for all multi-indices $I$ with $0 \leq|I| \leq m, r^{|I|+\alpha}\left\|D^{I} \omega_{i \bar{j}}\right\|_{\alpha} \leq$ $Q$. Globally we define
$$\|(M, \omega)\|_{C^{m, \alpha}, r}^{\text {holo }}=\sup _{x \in M}\|(M, \omega, x)\|_{C^{m, \alpha}, r}^{\text {holo }} .$$

By using Hörmander's $L^{2}$ estimate appropriately, Tian initiate his peak section method in [33]. One of the key steps of Tian's peak section method is to construct the following global section.

Lemma 2.1 ([33, Lemma 1.2, Lemma 2.3]). For an $n$-tuple of integers $P=\left(p_{1}, p_{2}, \ldots, p_{n}\right) \in \mathbb{Z}_{+}^{n}$, an integer $p^{\prime}>p=\sum_{j=1}^{n} p_{j}$, and constants $\Lambda, \epsilon, Q>0$, there are constants $m_{0}, C$ which depending on $\Lambda, n, p, p^{\prime}, \epsilon, Q$ with the following property.

Let ( $M, \omega, \mathcal{L}, h$ ) be a polarized manifold such that $\operatorname{Ric}(\omega) \geq-\Lambda \omega$, $\operatorname{Ric}(h) \geq \epsilon \omega$, and $x \in M$. Suppose that $M$ is pseudoconvex if $(M, \omega)$ isn't complete. Assume that there exists a local coordinate $\left(z_{1}, \cdots, z_{n}\right): B_{\frac{\log m}{Q \sqrt{m}}}(x) \rightarrow U \subset \mathbb{C}^{n}$, such that $x=(0, \cdots, 0), e^{-Q} \omega_{E u c} \leq \omega \leq e^{Q} \omega_{E u c}$, and the hermitian matrix $\left(g_{i \bar{j}}\right)$ satisfies that $g_{i \bar{j}}(0)=\delta_{i j}$, dgi ${ }_{\bar{j}}(0)=0$, and $\left\|g_{i \bar{j}}\right\|_{1, \frac{1}{2} ; U}^{*} \leq Q$, where $\|f\|_{k, \alpha}^{*}$ is the interior norms on a domain in $\mathbb{R}^{2 n}$. We further assume that there exists a holomorphic frame $e_{\mathcal{L}}$ of $\mathcal{L}$ on this coordinate such that the local representation function of $h, a=h\left(e_{\mathcal{L}}, e_{\mathcal{L}}\right)$, satisfying that $a(0)=1, \frac{\partial^{|I|} a}{\partial z^{T}}(0)=0$ for each milti-index $I$ with $|I| \leq 3$, and $\|a\|_{3, \frac{1}{2} ; U}^{*} \leq \frac{Q(\log m)^{2}}{m}$.

Then there are sequences $a_{m}$ and $b_{m}$, smooth $\mathcal{L}$-valued sections $\varphi_{m}$, and holomorphic global sections $S_{m}$ in $H^{0}\left(M, \mathcal{L}^{m}\right), \forall m>m_{0}$, satisfying
$$\begin{aligned}
& \int_{M}\left\|\varphi_{m}\right\|_{h^{m}}^{2} d V_{\omega} \leq \frac{C}{m^{8 p^{\prime}+2 n}}, \\
& \int_{M}\left\|S_{m}\right\|_{h^{m}}^{2} d V_{\omega}=1, \\
& \int_{M} \backslash\left\{|z| \leq \frac{\log (m)}{Q \sqrt{m}}\right\} \\
&=S_{m} \|_{h^{m}}^{2} d V_{\omega} \\
& \leq \frac{C}{m^{2 p^{\prime}}},
\end{aligned}$$
and locally at $x$,
$$S_{m}(z)=\lambda_{P}\left(1+\frac{a_{m}}{m^{2 p^{\prime}}}\right)\left(z_{1}^{p_{1}} \cdots z_{n}^{p_{n}}+\varphi_{m}\right) e_{L}^{m},$$
where $\|\cdot\|_{h^{m}}$ is the norm on $\mathcal{L}^{m}$ given by $h^{m},\left|a_{m}\right| \leq C, \varphi_{m}$ is holomorphic on $\left\{|z| \leq \frac{\log (m)}{Q \sqrt{m}}\right\}$, and $\left\|\varphi_{m}\right\|_{h^{m}} \leq b_{m}|z|^{2 p^{\prime}}$ on $U$, moreover
$$\lambda_{P}^{-2}=\int_{\left\{|z| \leq \frac{\log (m)}{Q \sqrt{m}}\right\}}\left|z_{1}^{p_{1}} \cdots z_{n}^{p_{n}}\right|^{2} a^{m} d V_{\omega},$$
and hence we can assume that $\left|m^{n+p} \lambda_{P}^{-2}-\pi^{n} P!\right| \leq C m^{-\frac{1}{2}}$, where $d V_{\omega}=\left(\frac{\sqrt{-1}}{2}\right)^{n} \operatorname{det}\left(g_{i \bar{j}}\right) d z_{1} \wedge$ $d \bar{z}_{1} \wedge \cdots \wedge d z_{n} \wedge d \bar{z}_{n}$ is the volume form.

Remark. By the theory of Cheeger-Gromov convergence, we can find such coordinates and holomorphic frames on polarized manifolds with a bound of Ricci curvature and a lower bound of injective radius. See [2, Theorem 1.1] or [27, Chapter 11] for details.

As a corollary, Tian shows that the global holomorphic sections constructed above have the following almost-orthogonal property.

Corollary 2.1 ([33], Lemma 3.1). Let $S_{m}$ be a holomorphic global section constructed in Lemma 2.1, and $T$ be another holomorphic global section of $\mathcal{L}^{m}$ with $\int_{M}\|T\|_{h^{m}}^{2} d \operatorname{Vol}_{\omega}=1$, which contains no term $z^{P}$ in its Taylor expansion at $x_{0}$. Then
$$\left|\int_{M}\left\langle S_{m}, T\right\rangle_{h^{m}} d \operatorname{Vol}_{\omega}\right| \leq C m^{-\frac{1}{2}}, \quad \forall m \geq m_{0},$$
where $m_{0}, C$ are positive constants depending on $\epsilon, \Lambda, Q$.
Then we recall the Tian-Yau-Zelditch expansion theorem of Bergman kernels on a given manifold. The proof can be found in [5, 6, 20, 35]. Note that Liu-Lu's proof in [20] only relies on Tian's peak section method.

Theorem 2.1. For constants $\Lambda, \epsilon, \xi, \delta k, Q>0$, there are constants $m_{0}, m_{1}, C$ which depending on $\Lambda, \epsilon, \xi, \delta, k, Q$ with the following property.

Let $(M, \omega)$ be a Kähler manifold such that $\operatorname{Ric}(\omega) \geq-\Lambda \omega$, let $(\mathcal{L}, h)$ be a Hermitian line bundle on $(M, \omega)$ such that $\operatorname{Ric}(h) \geq \epsilon \omega$, and let $U$ be an open subset of $M$. If $(M, \omega)$ isn't complete, we suppose that $M$ is pseudoconvex. Write $U_{m}=\left\{y \in M \left\lvert\, \operatorname{dist}_{\omega}(y, U)<\frac{\xi \log m}{\sqrt{m}}\right.\right\}$ for each $m>m_{0}$. Assume that $\bar{U}_{m_{0}}$ is complete, $\operatorname{Ric}(h)=\omega$ on $U_{m}, \inf _{x \in U_{m}} \operatorname{inj}(x) \geq \frac{\delta \log m}{\sqrt{m}}$, and $\sum_{j=0}^{2 k} \sup _{U_{m}}\left\|\nabla^{j} \operatorname{Ric}(\omega)\right\| \leq Q$.

Then there exist coefficients $a_{j} \in C^{\infty}(M), \forall j \in \mathbb{N}$, such that
$$\left\|\rho_{\omega, m}-\sum_{j=0}^{k} a_{j} m^{n-j}\right\|_{C^{k}(U)} \leq C m^{n-k-1}, \forall m>m_{1} .$$
Remark. In Lemma 2.1, Corollary 2.1 and Theorem 2.1, we assume the complete and pseudoconvex condition just so that Hörmander's $L^{2}$ estimate can be used. So these results still hold when $M$ is replaced by an open subset of $M$.

\section*{3. Bergman kernels on complex hyperbolic cusp}

In this section, we calculate the Bergman kernels on the complex hyperbolic cusp by find a special $L^{2}$ orthonormal basis, and then we consider the asymptotic behavior of Bergman kernels. We only consider the case $n \geq 2$ in this section, because the expression of Bergman kernels on the punctured unit disc is known. For more details, see Subsection 3.1 in [3].

\subsection*{3.1. Expression of the Bergman kernels on complex hyperbolic cusps.}

First we consider the expansion of holomorphic functions on the total space of line bundle. We will use the letter $\mathcal{L}$ to denote a holomorphic line bundle on a complex manifold $X$. Let $V$ be a connected open neighborhood of $X$ in the total space $\mathcal{L}$. Since $\mathcal{L}^{-1} \otimes \mathcal{L} \cong \mathbb{C}$, we see that for each section $S \in H^{0}\left(X, \mathcal{L}^{-1}\right)$, the map $v \mapsto S(v)$ gives a holomorphic function on the total space of $\mathcal{L}$. Then we show that any holomorphic function on $V \backslash X$ has a similar structure.

Lemma 3.1. Let $f$ be a holomorphic function on $V \backslash X$. Then there exists a sequence of holomorphic sections $S_{k} \in H^{0}\left(M, \mathcal{L}^{-k}\right), \forall k \in \mathbb{Z}$, such that $f$ has the following power series expansion on $V \backslash X$ :
$$f(v)=\sum_{k \in \mathbb{Z}} f_{S_{k}}(v)=\sum_{k \in \mathbb{Z}} S_{k}\left(v^{k}\right), \quad \forall v \in V \backslash X \subset \mathcal{L},$$
where $v^{k}=v^{\otimes k}$ is a point in the total space of $\mathcal{L}^{k}$.
Moreover, if $X$ is compact and $\mathcal{L}$ is a negative line bundle, then we have $S_{k}=0, \forall k<0$.
Proof. Let $\left\{U_{j}\right\}_{j \in J}$ be an open neighborhood of $X$ such that for each $j$, there exists a trivialization $\psi_{j}:\left.\mathcal{L}\right|_{U_{j}} \cong U_{j} \times \mathbb{C}$ satisfies that $U_{j} \times \mathbb{D}_{1} \subset \psi_{j}\left(\left.V \cap \mathcal{L}\right|_{U_{j}}\right)$, where $\mathbb{D}_{1}$ is the unit disc in $\mathbb{C}$. By the Laurent series expansion on $\mathbb{D}_{1}^{*}=\mathbb{D}_{1} \backslash\{0\}$, we can find a sequence of holomorphic functions $\left\{\varphi_{j, k}\right\}_{k \in \mathbb{Z}} \subset \mathcal{O}\left(U_{j}\right)$ for each $j$, such that
$$f \circ \psi_{j}^{-1}\left(z, w_{j}\right)=\sum_{k \in \mathbb{Z}} \varphi_{j, k}(z) w_{j}^{k}, \forall z \in U_{j}, w_{j} \in \mathbb{D}_{1}^{*},$$
and the coefficients satisfy
$$\varphi_{j, k}(z)=\frac{1}{2 \pi \sqrt{-1}} \int_{\partial \mathbb{D}_{1}} \frac{f \circ \psi_{j}^{-1}\left(z, w_{j}\right)}{w_{j}^{k+1}} d w_{j} .$$

Assume that $U_{j_{1}} \cap U_{j_{2}} \neq \emptyset$ for some $j_{1}, j_{2} \in J$. Then the transition function of $\mathcal{L}$ on $U_{j_{1}} \cap U_{j_{2}}$ is a holomorphic function $\psi_{j_{2} j_{1}} \in \mathcal{O}\left(U_{j_{1}} \cap U_{j_{2}}\right)$ defined by $\psi_{j_{2}}^{-1}\left(z, \psi_{j_{2} j_{1}}(z)\right)=\psi_{j_{1}}^{-1}(z, 1), \forall z \in U_{j_{1}} \cap U_{j_{2}}$.

The Cauchy integral formula now shows that
$$\begin{aligned}
\varphi_{j_{1}, k}(z) & =\frac{1}{2 \pi \sqrt{-1}} \int_{\partial \mathbb{D}_{1}} \frac{f \circ \psi_{j_{1}}^{-1}\left(z, w_{j_{1}}\right)}{w_{j_{1}}^{k+1}} d w_{j_{1}} \\
& =\frac{1}{2 \pi \sqrt{-1}} \int_{\partial \mathbb{D}_{1}} \frac{f \circ \psi_{j_{2}}^{-1}\left(z, \psi_{j_{2} j_{1}}(z) w_{j_{1}}\right)}{w_{j_{1}}^{k+1}} d w_{j_{1}} \\
& =\frac{1}{2 \pi \sqrt{-1}} \int_{\partial \mathbb{D}_{\psi_{j_{2} j_{1}}(z)}} \frac{f \circ \psi_{j_{2}}^{-1}\left(z, w_{j_{2}}\right)}{\psi_{j_{2} j_{1}}^{-k-1}(z) w_{j_{2}}^{k+1}} d\left(\psi_{j_{2} j_{1}}^{-1}(z) w_{j_{2}}\right) \\
& =\frac{\psi_{j_{2} j_{1}}^{k}(z)}{2 \pi \sqrt{-1}} \int_{\partial \mathbb{D}_{1}} \frac{f \circ \psi_{j_{2}}^{-1}\left(z, w_{j_{2}}\right)}{w_{j_{2}}^{k+1}} d w_{j_{2}} \\
& =\psi_{j_{2} j_{1}}^{k}(z) \varphi_{j_{2}, k}(z) .
\end{aligned}$$

It follows that $\left\{\varphi_{j, k}\right\}_{j \in J}$ gives a holomorphic section $S_{k} \in H^{0}\left(X, \mathcal{L}^{-k}\right)$. Then we can find an open neighborhood $V_{1}$ of $X$ in $V$, such that $f$ has the above expansion in $V_{1} \backslash X$. Then the connectedness of $V$ implies that $f$ has this expansion in the whole $V \backslash X$.

Now we assume that $X$ is compact and $\mathcal{L}$ is negative. By the Kodaira embedding theorem, we can find a constant $k_{0}>0$ such that $H^{0}\left(X, \mathcal{L}^{-k}\right) \neq 0$ for each $k>k_{0}$. If $H^{0}\left(X, \mathcal{L}^{k}\right) \neq 0$ for some $k>0$, then there exists an integer $k_{1}>k_{0}$ such that $H^{0}\left(X, \mathcal{L}^{k_{1}}\right) \neq 0$. It follows that we can find a holomorphic function $\phi=S \otimes S^{\prime} \in H^{0}\left(X, \mathcal{L}^{-k_{1}} \otimes \mathcal{L}^{k_{1}}\right) \cong H^{0}(X, \mathbb{C})$ such that $\phi \neq 0$, but $\phi(x)=0$ for some $x$. But the compactness of $X$ implies that $H^{0}(X, \mathbb{C}) \cong \mathbb{C}$, contradiction. Hence we have $H^{0}\left(X, \mathcal{L}^{k}\right) \neq 0, \forall k>0$. This gives $S_{k}=0, \forall k<0$. This completes the proof. \(\square\)

Let $\left(\mathcal{L}_{D}, h_{D}\right)$ be a negative line bundle on $D$, and $\left(V, \omega_{V}, \mathcal{L}_{V}, h_{V}\right)$ be an $n$-dimensional $(n \geq 2)$ complex hyperbolic cusp defined in Section 1 now.

For each $x \in D$, we can find an open neighborhood $U$ of $x$ in $D$, a biholomorphic chart $z=$ $\left(z_{1}, \cdots, z_{n-1}\right): U \cong \mathbb{B}_{1}^{n-1} \subset \mathbb{C}^{n-1}$, and a non-vanishing section $e_{U} \in H^{0}\left(U, \mathcal{L}_{D}\right)$. Let $w$ be a holomorphic map defined by $v=w(v) e_{U},\left.\forall v \in \mathcal{L}_{D}\right|_{U}$. Recall that $V$ is a subset of the total space of $\mathcal{L}_{D}$, we see that the holomorphic map $(z, w)$ gives a holomorphic chart:
$$(z, w):\left.\mathcal{L}_{D}\right|_{U} \cap V \cong\left\{(z, w) \in \mathbb{B}_{1}^{n-1} \times \mathbb{C}\left|0<|w| \cdot\left\|e_{U}\right\|_{h_{D}}<1\right\} .\right.$$

Set $\varphi=\log \left(\left\|e_{U}\right\|_{h_{D}}^{2}\right)$. Then the volume form on $\pi_{D}^{-1}(U) \cap V, d \operatorname{Vol}_{\omega_{V}}$, can be calculated as following:
$$\begin{aligned}
d \operatorname{Vol}_{\omega_{V}} & =\frac{\left(-\sqrt{-1} \partial \bar{\partial} \log \left(-\log h_{D}\right)\right)^{n}}{n!} \\
& =\frac{1}{n!}\left(\sqrt{-1} \frac{\partial \bar{\partial} \log h_{D}}{\left|\log h_{D}\right|}+\sqrt{-1} \frac{\partial \log h_{D} \wedge \bar{\partial} \log h_{D}}{\left|\log h_{D}\right|^{2}}\right)^{n} \\
& =\frac{1}{n!}\left(\sqrt{-1} \frac{\partial \bar{\partial} \varphi}{\left|\log h_{D}\right|}+\sqrt{-1} \frac{\partial \log h_{D} \wedge \bar{\partial} \log h_{D}}{\left|\log h_{D}\right|^{2}}\right)^{n} \\
& =\frac{(\sqrt{-1})^{n}}{n!} \cdot \frac{(\partial \bar{\partial} \varphi)^{n-1} \wedge \partial\left(\log |w|^{2}+\varphi\right) \wedge \bar{\partial}\left(\log |w|^{2}+\varphi\right)}{\left|\log h_{D}\right|^{n+1}} \\
& =\frac{\sqrt{-1} \pi_{D}^{*}\left(d \operatorname{Vol}_{\omega_{D}}\right) \wedge d w \wedge d \bar{w}}{n|w|^{2}\left|\log h_{D}\right|^{n+1}}=\frac{\pi_{D}^{*}\left(d \operatorname{Vol}_{\omega_{D}}\right) \wedge \omega_{V}}{n\left|\log h_{D}\right|^{n-1}} .
\end{aligned}$$

Now we can find an orthonormal basis of $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)$.
Lemma 3.2. For $m \geq n+1$, the set
$$\left\{\left.\left(\frac{n \cdot q^{m-n}}{2 \pi(m-n-1)!}\right)^{\frac{1}{2}} f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m} \right\rvert\, 1 \leq j \leq N_{q}, q \geq 1\right\}$$
forms an orthonormal basis of $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)$, where $\left\{S_{q, j}\right\}_{j=1}^{N_{q}}$ is an $L^{2}$ orthonormal basis in the Hilbert space $H_{L^{2}}^{0}\left(D, \mathcal{L}_{D}^{-q}\right)$, and $f_{S_{q, j}}$ denote the holomorphic function corresponding to $S_{q, j}$ defined in Lemma 3.1.

Proof. Let $\widetilde{S}_{1}$ and $\widetilde{S}_{2}$ be the holomorphic functions corresponding to the holomorphic sections $S_{1} \in H^{0}\left(D, \mathcal{L}_{D}^{-q_{1}}\right)$ and $S_{2} \in H^{0}\left(D, \mathcal{L}_{D}^{-q_{2}}\right)$, respectively. Then we have
$$\begin{aligned}
\int_{V}\left\langle f_{S_{1}} e_{\mathcal{L}_{V}}^{m}, f_{S_{2}} e_{\mathcal{L}_{V}}^{m}\right\rangle_{h_{V}^{m}} d \operatorname{Vol}_{\omega_{V}} & =\int_{V} f_{S_{1}} \bar{f}_{S_{2}}\left|\log h_{D}\right|^{m} d \operatorname{Vol}_{\omega_{V}} \\
& =\frac{1}{n} \int_{V} f_{S_{1}} \bar{f}_{S_{2}}\left|\log h_{D}\right|^{m+1-n} d \operatorname{Vol}_{\omega_{D}} \wedge \omega_{V} \\
& =\int_{D}\left(\frac{1}{n} \int_{V_{z}} f_{S_{1}} \bar{f}_{S_{2}}\left|\log h_{D}\right|^{m+1-n} \omega_{V}\right) d \operatorname{Vol}_{\omega_{D}},
\end{aligned}$$
where $V_{z}=\pi_{D}^{-1}(x) \cap V, z \in D$, and $\pi_{D}: \mathcal{L}_{D} \rightarrow D$ is the projection of line bundle. For each $z \in D$, we can find $e \in \pi_{D}^{-1}(x)$ such that $h_{D}(e)=1$. Then we have
$$\begin{aligned}
\frac{1}{n} \int_{V_{z}} f_{S_{1}} \bar{f}_{S_{2}}\left|\log h_{D}\right|^{m+1-n} \omega_{V} & =\sqrt{-1} S_{1}\left(e^{q_{1}}\right) \overline{S_{2}\left(e^{q_{2}}\right)} \int_{\mathbb{D}_{1}^{*}} \frac{\left.\left.w^{q_{1}} \bar{w}^{q_{2}}|\log | w\right|^{2}\right|^{m-1-n}}{n|w|^{2}} d w \wedge d \bar{w} \\
& =\sqrt{-1} \delta_{q_{1}, q_{2}} h^{-q_{1}}\left(S_{1}, S_{2}\right) \int_{\mathbb{D}_{1}^{*}} \frac{\left.\left.|w|^{2 q_{1}-2}|\log | w\right|^{2}\right|^{m-1-n}}{n} d w \wedge d \bar{w},
\end{aligned}$$
where $\delta_{q_{1}, q_{2}}$ is the Kronecker symbol. It follows that
$$\int_{V}\left\langle f_{S_{1}} e_{\mathcal{L}_{V}}^{m}, f_{S_{2}} e_{\mathcal{L}_{V}}^{m}\right\rangle_{h_{V}^{m}} d \operatorname{Vol}_{\omega_{V}}=0$$
if $q_{1} \neq q_{2}$. Now we assume that $q_{1}=q_{2}=q$. Since $m \geq n+1$, we have
$$\left.\left.\int_{\mathbb{D}_{1}^{*}} \sqrt{-1}|w|^{-2}|\log | w\right|^{2}\right|^{m-1-n} d w \wedge d \bar{w}=\int_{0}^{2 \pi} 2^{m-n-1} d \theta \int_{0}^{1} r^{-1}|\log r|^{m-1-n} d r=\infty$$
and hence $e_{\mathcal{L}_{V}}^{m} \notin H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)$. When $q \geq 1$, by a direct computation, we obtain
$$\begin{aligned}
\int_{\mathbb{D}_{1}^{*}} \frac{\left.\left.|w|^{2 q-2}|\log | w\right|^{2}\right|^{m-1-n}}{-\sqrt{-1}} d w \wedge d \bar{w} & =\int_{0}^{2 \pi} 2^{m-n} d \theta \int_{0}^{1} r^{2 q-1}|\log r|^{m-1-n} d r \\
& =2^{m-n+1} \pi \int_{0}^{\infty} e^{-2 q t} t^{m-1-n} d t \\
& =2^{m-n+1} \pi \cdot(2 q)^{n-m} \cdot(m-n-1)!=\frac{2 \pi(m-n-1)!}{q^{m-n}} .
\end{aligned}$$
Then we have
$$\begin{aligned}
\int_{V}\left\langle f_{S_{1}} e_{\mathcal{L}_{V}}^{m}, f_{S_{2}} e_{\mathcal{L}_{V}}^{m}\right\rangle_{h_{V}^{m}} d V_{\omega_{V}} & =\int_{D}\left(\frac{1}{n} \int_{V_{z}} f_{S_{1}} \bar{f}_{S_{2}}\left|\log h_{D}\right|^{m+1-n} \omega_{V}\right) d V_{\omega_{D}} \\
& =\int_{D} h^{-q}\left(S_{1}, S_{2}\right) d V_{\omega_{D}} \int_{\mathbb{D}_{1}^{*}} \frac{\left.\left.\sqrt{-1}|w|^{2 q-2}|\log | w\right|^{2}\right|^{m-1-n}}{n} d w \wedge d \bar{w} \\
& =\frac{2 \pi(m-n-1)!}{n \cdot q^{m-n}} \int_{D} h_{D}^{-q}\left(S_{1}, S_{2}\right) d \operatorname{Vol}_{\omega_{D}} .
\end{aligned}$$
Combining Lemma 3.1 and the above calculation, we can conclude that the set (15) forms an orthonormal basis of $H_{L^{2}}^{0}\left(D, \mathcal{L}_{D}^{-q}\right)$. \(\square\)

Remark. In the case $n=1$, analysis similar to that in the proof of Lemma 3.2 shows that the set
$$\left\{\left.\left(\frac{n \cdot q^{m-1}}{2 \pi(m-2)!}\right)^{\frac{1}{2}} e_{\mathcal{L}_{V}}^{m} \right\rvert\, q \geq 1\right\}$$
forms an orthonormal basis of $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)$ when $m \geq 2$.
As another application of the calculation of the volume form on $\left(V, \omega_{V}\right)$, we can estimate the injectivity radius on $\left(V, \omega_{V}\right)$.

Lemma 3.3. There exists a constant $\delta=\delta(D)>0$, such that the injectivity radius $\operatorname{inj}_{V}(x)$ becomes a strictly increasing function of $h_{D}(x)$ on $V_{\delta}$, and $-\frac{\delta}{\log \left(h_{D}(x)\right)} \leq \operatorname{inj}_{V}(x) \leq-\frac{\pi}{\log \left(h_{D}(x)\right)}, \forall v \in V_{\delta}$, where $\operatorname{inj}_{V}(x)$ is the injectivity radius at $x \in V$.

Proof. Let $\pi_{Q}: \mathbb{C}^{n-1} \rightarrow D$ be the universal covering map of $D$. Then the morphism $\pi_{Q}^{*} \mathcal{L}_{D} \rightarrow \mathcal{L}_{D}$ induced by $\pi_{Q}$ is also a universal covering map. For abbreviation, we use the same letter $\pi_{Q}$ to designate it. Since $\operatorname{Pic}\left(\mathbb{C}^{n-1}\right)=0$, we have $\left(\pi_{Q}^{*} \mathcal{L}_{D}, \pi^{*} h_{D}\right) \cong\left(\mathbb{C}, e^{|z|^{2}}\right)$, and the isomorphism gives a holomorphic chart $(z, w) \in \mathbb{C}^{n-1} \times \mathbb{C}$ of $\pi_{Q}^{-1}(V)$. It is easy to shows that $\operatorname{inj}_{\pi_{Q}^{-1}(V)}(z, w)$ is a function of $h_{D} \circ \pi_{Q}(z, w)$ on $\pi_{Q}^{-1}(V)$. For each smooth curve $\gamma:[0,1] \rightarrow \pi_{Q}^{-1}(V)$, we can construct a family of curves by $\gamma_{t}(s)=(z(\gamma(s)), t w(\gamma(s))), \forall t \in(0,1)$. By a straightforward computation, we obtain $\left|\gamma_{t}^{\prime}(s)\right| \leq\left|\gamma^{\prime}(s)\right|$, and equality holds only when $\left|\gamma^{\prime}(s)\right|=0$. It follows that $\operatorname{inj}(z, w)$ is a strictly increasing function of $h_{D} \circ \pi_{Q}(z, w)$ on $\pi_{Q}^{-1}(V)$.

Let $\gamma(s)=\left(0, e^{\sqrt{-1} s} w\right), s \in[0,2 \pi]$. Clearly, $[\gamma] \neq 0$ in the fundamental group $\pi_{1}\left(\pi_{Q}^{-1}(V)\right)$. Then $L(\gamma)=\frac{2 \pi}{-\log \left(|w|^{2}\right)}$ implies that $\operatorname{inj}_{\pi_{Q}^{-1}(V)}(z, w) \leq-\frac{\pi}{\log \left(h_{D}(v)\right)}$. Choosing $x_{1}, x_{2} \in \pi_{Q}^{-1}(x)$ and a smooth curve $\gamma:[0,1] \rightarrow \pi_{Q}^{-1}(V)$ such that $x_{1} \neq x_{2}, \gamma(0)=x_{1}$ and $\gamma(1)=x_{2}$. Assume that $L(\gamma) \leq 1$. Then we have $\inf _{\gamma}|w(\gamma)|^{2} \geq\left|h_{D}(x)\right|^{e}$, and there exists a constant $\epsilon=\epsilon(n)>0$ such that $\operatorname{dist}_{\omega_{V}}\left(x_{1}, x_{2}\right) \geq \frac{\epsilon\left|z\left(x_{1}\right)-z\left(x_{2}\right)\right|}{\sqrt{-e \log \left(h_{D}(x)\right)}}$. Then we can find a constant $\delta_{1}=\delta_{1}(D)>0$ such that $\operatorname{inj}_{\pi_{Q}^{-1}(V)}=\operatorname{inj}_{V} \circ \pi_{Q}$ on $\pi_{Q}^{-1}\left(V_{\delta_{1}}\right)$.

Since the holomorphic sectional curvature of $\omega_{V}$ is a constant, we can conclude that the sectional curvature of $\omega_{V}$ is bounded. Recall that the volume form on $V$ can be expressed as
$$d \operatorname{Vol}_{\omega_{V}}=\frac{\pi_{D}^{*}\left(d \operatorname{Vol}_{\omega_{D}}\right) \wedge \omega_{V}}{n\left|\log h_{D}\right|^{n-1}} .$$
Thus we can find a constant $\delta_{2}>0$ depending only on $\left(V, \omega_{V}\right)$, such that
$$\operatorname{Vol}_{\omega_{V}}\left(B \frac{-1}{\log \left(h_{D}(x)\right)}(x)\right) \geq \delta_{2}\left(\frac{-1}{\log \left(h_{D}(x)\right)}\right)^{2 n}, \forall x \in V_{\delta_{2}} .$$
Then the Cheeger's lemma implies this lemma. \(\square\)

Let $\Gamma_{V}$ be a finite subgroup of $\operatorname{Aut}\left(V, \omega_{V}\right)$. Then we see that the injectivity radius function is invariant under the action of $\Gamma_{V}$. Hence $h_{D}$ is invariant under the action of $\operatorname{Aut}\left(V, \omega_{V}\right)$ on $V$, and the action of $\Gamma_{V}$ on $V$ can be extended to the total space of $\mathcal{L}_{D}$. Now we further extend the action of $\Gamma_{V}$ on $V$ to the line bundle $\mathcal{L}_{V}$ such that $h_{V}$ is invariant under this action. Notice that by the invariance of $h_{V}$ under the action of $\Gamma_{V}$, we have a homomorphism $\Theta_{\Gamma_{V}}: \Gamma_{V} \rightarrow U(1) \subset \mathbb{C}^{*}$ such that $g\left(e_{\mathcal{L}_{V}}\right)=\Theta_{\Gamma_{V}}(g) e_{\mathcal{L}_{V}}, \forall g \in \Gamma_{V}$.

Fix $m \geq n+1$. Now we consider the group action $\Gamma_{V} \times H^{0}\left(V, \mathcal{L}_{V}^{m}\right) \rightarrow H^{0}\left(V, \mathcal{L}_{V}^{m}\right)$ given by
$$\Delta_{\Gamma_{V}, m}:\left\{\begin{array}{clc}
\Gamma_{V} \times H^{0}\left(V, \mathcal{L}_{V}^{m}\right) & \rightarrow & H^{0}\left(V, \mathcal{L}_{V}^{m}\right) \\
\left(g, f e_{\mathcal{L}_{V}}^{m}\right) & \mapsto \Theta_{\Gamma_{V}}(g)^{m}\left(f \circ g^{-1}\right) e_{\mathcal{L}_{V}}^{m}
\end{array},\right.$$
for any $g \in \Gamma_{V} \subset \operatorname{Aut}\left(V, \omega_{V}\right)$ and $f \in \mathcal{O}(V)$.
Let $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)_{q}$ be the subspace of $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)$ generated by $\left\{f_{S_{q, j}} e_{\mathcal{L}_{V}}^{m}\right\}_{j=1}^{N_{q}}$, and $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)_{\Gamma_{V}}$ be the subspace of $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)$ containing all holomorphic sections that are invariant under the action $\Delta_{\Gamma_{V}, m}$. Since $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)_{q}$ is invariant under the action $\Delta_{\Gamma_{V}, m}$, we see that the Hilbert space $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)_{\Gamma_{V}}$ can be generated by $\oplus_{q=1}^{\infty}\left(H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)_{\Gamma_{V}} \cap H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)_{q}\right)$. Then there are non-negative integers $N_{m, q}^{\prime} \leq N_{q}$ and $L^{2}$ orthonormal sets $\left\{S_{m, q, j}^{\prime}\right\}_{j=1}^{N_{m, q}^{\prime}} \subset H_{L^{2}}^{0}\left(D, \mathcal{L}_{D}^{-q}\right)_{\Gamma_{V}}$ such that the set
$$\left\{\left.\left(\frac{n \cdot q^{m-n}}{2 \pi(m-n-1)!}\right)^{\frac{1}{2}} f_{S_{m, q, j}^{\prime}} e_{\mathcal{L}_{V}}^{m} \right\rvert\, 1 \leq j \leq N_{m, q}^{\prime}, q \geq 1\right\}$$
forms an orthonormal basis of $H_{L^{2}}^{0}\left(V, \mathcal{L}_{V}^{m}\right)_{\Gamma_{V}}$. Now we can define the $\Delta_{\Gamma_{V}, m}$-invariant Bergman kernel functions by $\rho_{D, \omega_{D}, \Delta_{\Gamma_{V}}, m, q}=\sum_{j=1}^{N_{m, q}^{\prime}}\left\|S_{m, q, j}^{\prime}\right\|_{h_{D}^{-q}}^{2}$.

Then we can obtain the expression of Bergman kernel functions on $V / \Gamma_{V}$ for $m \geq n+1$.

Proposition 3.1. For $m \geq n+1$, the Bergman kernel functions on $\left(V / \Gamma_{V}, \omega_{V}, \mathcal{L}_{V} / \Gamma_{V}, h_{V}\right)$ can be expressed as
$$\rho_{V / \Gamma_{V}, \omega_{V}, m}\left(\pi_{V}(x)\right)=\frac{n\left|\Gamma_{V}\right|\left|\log h_{D}(x)\right|^{m}}{2 \pi(m-n-1)!} \sum_{q=1}^{\infty} q^{m-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}\left(\pi_{D}(x)\right) h_{D}(x)^{q},$$
where $x \in V, \pi_{V}: V \rightarrow V / \Gamma_{V}$ is the quotient map, and $\pi_{D}: V \subset \mathcal{L}_{D} \rightarrow D$ is the projection.
Proof. By Lemma 3.2, we have
$$\begin{aligned}
\rho_{V / \Gamma_{V}, \omega_{V}, m}\left(\pi_{V}(x)\right) & =\left|\Gamma_{V}\right| \sum_{q=1}^{\infty} \frac{n q^{m-n}}{2 \pi(m-n-1)!}\left(\sum_{j=1}^{N_{m, q}^{\prime}}\left|\widetilde{S}_{m, j, q}^{\prime}(x)\right|^{2} \cdot\left\|e_{\mathcal{L}_{V}}^{m}\right\|_{h_{\mathcal{L}}^{m}}^{2}\right) \\
& =\left|\Gamma_{V}\right| \sum_{q=1}^{\infty} \frac{n q^{m-n} h_{D}(x)^{q}\left|\log h_{D}(x)\right|^{m}}{2 \pi(m-n-1)!}\left(\sum_{j=1}^{N_{m, q}^{\prime}}\left\|S_{m, q, j}^{\prime}\left(\pi_{D}(x)\right)\right\|_{h_{D}^{-q}}^{2}\right) \\
& =\frac{n\left|\Gamma_{V}\right|\left|\log h_{D}(x)\right|^{m}}{2 \pi(m-n-1)!} \sum_{q=1}^{\infty} q^{m-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}\left(\pi_{D}(x)\right) h_{D}(x)^{q},
\end{aligned}$$
which proves the proposition. \(\square\)

Remark. As in the proof of Proposition 3.1, we see that for any integer $k \geq 0$ and $m \geq n+1$, the Bergman kernel functions on $\left(V / \Gamma_{V}, \omega_{V}, \mathcal{L}_{V} / \Gamma_{V},\left|\log h_{D}\right|^{k} h_{V}\right)$ can be expressed as
$$\rho_{V / \Gamma_{V}, \omega_{V}, m}^{(k)}\left(\pi_{V}(x)\right)=\frac{n\left|\Gamma_{V}\right|\left|\log h_{D}(x)\right|^{m(k+1)}}{2 \pi(m(k+1)-n-1)!} \sum_{q=1}^{\infty} q^{m(k+1)-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}\left(\pi_{D}(x)\right) h_{D}(x)^{q},$$
where $x \in V, \pi_{V}: V \rightarrow V / \Gamma_{V}$ is the quotient map, and $\pi_{D}: V \subset \mathcal{L}_{D} \rightarrow D$ is the projection.

\subsection*{3.2. Asymptotic behavior of Bergman kernel functions on complex hyperbolic cusps.}

In this subsection, we will consider the asymptotic behavior of Bergman kernel functions on complex hyperbolic cusp.

Let $\left(V / \Gamma_{V}, \omega_{V}, \mathcal{L}_{V} / \Gamma_{V}, h_{V}\right)$ be a complex hyperbolic cusp defined on an polarized flat Abelian variety $\left(D, \omega_{D}\right)$ with a polarization $\left(\mathcal{L}_{D}^{-1}, h_{D}^{-1}\right)$. Now we consider the Bergman kernel function near cusp. We can use an argument similar to that in [3, Section 3].

For each integer $m \geq n+1$, set
$$b_{m}(a, t)=\frac{n\left|\Gamma_{V}\right| t^{m}}{2 \pi(m-n-1)!} \sum_{q=1}^{\infty} q^{m-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a) e^{-q t}, \quad \forall a \in D, \forall t \in(0, \infty) .$$
It is clear that $\rho_{V / \Gamma_{V}, \omega_{V}, m}(x)=b_{m}\left(\pi_{D}(x),-\log h_{D}(x)\right)$, for any $x \in V$. Then we consider the Taylor expansion of each term in this series.

Let $f(t)=(1+t) e^{-t}$. Then we see that
$$b_{m}(a, m t)=\frac{n\left|\Gamma_{V}\right| m^{m} e^{-m}}{2 \pi(m-n-1)!} \sum_{q=1}^{\infty} q^{-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a)(f(q t-1))^{m}, \forall x \in D, \forall t \in(0, \infty) .$$

Now we consider the asymptotic behavior of $f_{m}$ as $m \rightarrow \infty$. We can assume that
$$\sum_{j=1}^{\infty} \frac{1}{j!}\left[m \sum_{k=3}^{\infty} \frac{(-1)^{k-1}}{k} t^{k}\right]^{j}=\sum_{l=3}^{\infty} \lambda_{m, l} t^{l} \in \mathbb{R}[[t]],$$
where $\lambda_{m, l} \in \mathbb{R}$, and $\mathbb{R}[[t]]$ is the formal power series ring over $\mathbb{R}$. Clearly, we have $\lambda_{m, 3}=\frac{m}{3}$.
Lemma 3.4. Let $N \geq 3$ be an integer. Then we can find a constant $C=C(N)>0$ such that
$$\left|(f(t))^{m}-\left(1+\sum_{l=3}^{N} \lambda_{m, l} t^{l}\right) e^{-\frac{m t^{2}}{2}}\right| \leq \frac{C}{m^{\frac{N+1}{2}-\left\lfloor\frac{N+1}{3}\right\rfloor}\left(1+|t+1|^{2 N}\right)},$$
for any integer $m \geq n+1$ and constant $t \in(-1, \infty)$.
Proof. It is easy to see that for each given $m \in \mathbb{N}$, there exists a constant $C=C(m, N)>0$ such that (20) holds. So we only need to prove it for sufficiently large $m \geq e^{10 N^{2}}$. We will divide the proof into three parts according to the value of $t$.

When $|t| \leq \frac{\log (m)}{\sqrt{m}}$, the Taylor expansion gives a constant $C_{1}=C_{1}(N)>0$ such that
$$\begin{aligned}
\left|(f(t))^{m}-\left(1+\sum_{l=3}^{N} \lambda_{m, l} t^{l}\right) e^{-\frac{m t^{2}}{2}}\right| & =e^{-\frac{m t^{2}}{2}}\left|e^{m\left(\log (1+t)-t+\frac{t^{2}}{2}\right)}-\left(1+\sum_{l=3}^{N} \lambda_{m, l} t^{l}\right)\right| \\
& \leq C_{1} m^{\left\lfloor\frac{N+1}{3}\right\rfloor-\frac{N+1}{2}}\left(m t^{2}\right)^{\frac{N+1}{2}} e^{-\frac{m t^{2}}{2}} \leq C_{1}^{2} m\left\lfloor\frac{N+1}{3}\right\rfloor-\frac{N+1}{2},
\end{aligned}$$
where $\lfloor\cdot\rfloor$ is the greatest integer function.
By a straightforward computation, we see that $t^{l} e^{-\frac{m t^{2}}{2}} \leq C_{2} e^{-\frac{m t^{2}}{4}}$ for $|t| \geq \frac{\log (m)}{\sqrt{m}}$ and $l=$ $3, \cdots, N$, where $C_{2}=C_{2}(N)>0$ is a constant. It is sufficient to prove that there are constants $m_{0}, C>0$ depending only on $N$, such that $(f(t))^{m} \leq C m^{-N}(1+t)^{-N}$ for $m \geq m_{0}$, and $|t| \geq \frac{\log (m)}{\sqrt{m}}$.

When $t \leq-\frac{\log (m)}{\sqrt{m}}$, wee see that $f(t)$ is increasing, and hence the Taylor expansion implies that
$$(f(t))^{m} \leq\left(f\left(-\frac{\log (m)}{\sqrt{m}}\right)\right)^{m}=e^{m \log \left(1-\frac{\log (m)}{\sqrt{m}}\right)+m \frac{\log (m)}{\sqrt{m}}} \leq e^{-|\log (m)|^{2}+C_{3} \frac{|\log (m)|^{3}}{\sqrt{m}}},$$
where $C_{3}=C_{3}(N)>0$ is a constant. Clearly, we can find a constant $m_{0}=m_{0}(N)>0$ such that $(f(t))^{m} \leq m^{-N}$ for $m \geq m_{0}$ and $t \leq-\frac{\log (m)}{\sqrt{m}}$.

Now we assume that $t \geq \frac{\log (m)}{\sqrt{m}}$. By a direct calculation, we can conclude that $f_{m, N}(t)=$ $(1+t)^{N}(f(t))^{m}$ is descending for $t \geq \frac{N}{m}$, and hence we can assume that $(1+t)^{N} f_{m}$ is descending for $t \geq \frac{\log (m)}{\sqrt{m}}$. Apply the Taylor expansion again, we have
$$f_{m, N}(t) \leq f_{m, N}\left(\frac{\log (m)}{\sqrt{m}}\right)=e^{(m+N) \log \left(1+\frac{\log (m)}{\sqrt{m}}\right)+m \frac{\log (m)}{\sqrt{m}}} \leq e^{-|\log (m)|^{2}+C_{4} \frac{|\log (m)|^{3}}{\sqrt{m}}+N \frac{\log (m)}{\sqrt{m}}},$$
where $C_{4}=C_{4}(N)>0$ is a constant. Clearly, we can find a constant $m_{1}=m_{1}(N)>0$ such that $f_{m}(t) \leq m^{-N}(1+t)^{-N}$ for $m \geq m_{0}$ and $t \geq \frac{\log (m)}{\sqrt{m}}$. This completes the proof. \(\square\)

Write $G_{m, N}(t)=\left(1+\sum_{k=3}^{N} \lambda_{m, k} t^{k}\right) e^{-\frac{m t^{2}}{2}}$ for each $N \geq 3$. Then we can approximate the function $b_{m}$ by suitable combinations of the functions $G_{m, N}$ as follows.

Lemma 3.5. There exists a constant $C=C\left(N, V,\left|\Gamma_{V}\right|\right)>0$, such that
$$\begin{aligned}
& \sup _{a \in D} \left\lvert\, \frac{2 \pi(m-n-1)!}{n\left|\Gamma_{V}\right| m^{m} e^{1-m}} b_{m}(a, m t)\right. \\
& \quad-t \sum_{q=1}^{\infty} q^{1-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a) e^{-q t} G_{m-1, N}(q t-1) \left\lvert\, \leq \frac{C}{m^{\frac{N+1}{2}-\left\lfloor\frac{N+1}{3}\right\rfloor}}\right.,
\end{aligned}$$
for any integer $m \geq n+1$ and $t \in(0, \infty)$.
Proof. By Lemma 3.4, we see that
$$\begin{aligned}
& \left|\frac{2 \pi(m-n-1)!}{n\left|\Gamma_{V}\right| m^{m} e^{1-m}} b_{m}(a, m t)-t \sum_{q=1}^{\infty} q^{1-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a) e^{-q t} G_{m-1, N}(t)\right| \\
\leq & t \sum_{q=1}^{\infty} q^{1-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a) e^{-q t}\left|(f(q t-1))^{m-1}-G_{m-1, N}(q t-1)\right| \\
\leq & C m^{-\frac{N+1}{2}+\left\lfloor\frac{N+1}{3}\right\rfloor} \sum_{q=1}^{\infty} t e^{-q t}\left(1+|q t|^{2 N}\right)^{-1} \\
\leq & C^{2} m^{-\frac{N+1}{2}+\left\lfloor\frac{N+1}{3}\right\rfloor} e^{-t} \int_{0}^{\infty} t\left(1+t^{N} \xi^{N}\right)^{-1} d \xi \\
\leq & C^{2} m^{-\frac{N+1}{2}+\left\lfloor\frac{N+1}{3}\right\rfloor} e^{-t} \int_{0}^{\infty}\left(1+\xi^{N}\right)^{-1} d \xi \leq C^{3} m^{-\frac{N+1}{2}+\left\lfloor\frac{N+1}{3}\right\rfloor} e^{-t},
\end{aligned}$$
where $C=C\left(N, V,\left|\Gamma_{V}\right|\right)>0$ is a constant, and then we get (21). \(\square\)

As a corollary, we can estimate the sup of Bergman kernel functions.
Corollary 3.1. There exists a constant $C=C\left(N, V,\left|\Gamma_{V}\right|\right)>0$, such that
$$\left|(2 \pi)^{\frac{3}{2}} n^{-1} m^{-n-\frac{1}{2}} \sup _{x \in V / \Gamma_{V}} \rho_{V / \Gamma_{V}, \omega_{V}, m}(x)-\left|\Gamma_{V}\right| \alpha_{D, m}\right| \leq \frac{C}{\sqrt{m}},$$
where $\alpha_{D, m}=\sup _{a \in D} \sup _{q \in \mathbb{N}} q^{-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a)$. Moreover, $\alpha_{D, m}=\alpha_{D, m+\left|\Gamma_{V}\right|}, \forall m \in \mathbb{N}$, and hence there are constants $c_{1}, \cdots, c_{\left|\Gamma_{V}\right|}>0$ depending only on $\left(D, \mathcal{L}_{D}\right), \Gamma_{V}$ and $\Theta_{\Gamma_{V}}$, such that
$$\left|c_{j}\left(k\left|\Gamma_{V}\right|+j\right)^{-n-\frac{1}{2}} \sup _{V} \rho_{V / \Gamma_{V}, \omega_{V}, k\left|\Gamma_{V}\right|+j}-1\right| \leq \frac{C}{\sqrt{k}}, \quad \forall k \in \mathbb{N},$$
for $j=1, \cdots,\left|\Gamma_{V}\right|$.
Remark. By the standard Tian-Yau-Zelditch expansion, we see that
$$\limsup _{q \rightarrow \infty} q^{-n}\left(\sup _{a \in D} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}}, m, q}(a)\right) \leq\left|\Gamma_{V}\right| \limsup _{q \rightarrow \infty} q^{-n}\left(\sup _{a \in D} \rho_{D, \omega_{D}, q}(a)\right)=\lim _{l \rightarrow \infty}(2 \pi)^{n-1} l^{-1}=0 .$$
Hence we can find an integer $q_{m} \in \mathbb{N}$ and a point $a \in D$, such that $\alpha_{D, m}=q_{m}^{-n} \rho_{D, \omega_{D}, \Gamma_{V}, q_{a}}(a)$.

Proof. Let $t=q_{m}^{-1}$ such that $\alpha_{D, m}=q_{m}^{-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q_{m}}(a)$. Then Stirling's formula implies that
$$\begin{aligned}
& (2 \pi)^{\frac{3}{2}} n^{-1} m^{-n-\frac{1}{2}} \sup _{x \in V / \Gamma_{V}} \rho_{V / \Gamma_{V}, \omega_{V}, m}(x) \\
\geq & (2 \pi)^{\frac{3}{2}} n^{-1} m^{-n-\frac{1}{2}} b_{m}\left(a, m q_{m}^{-1}\right) \\
\geq & \left(1-C m^{-1}\right)\left|\Gamma_{V}\right| \sum_{j=1}^{\infty} j^{-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, j}(a)\left(f\left(j q_{a}^{-1}-1\right)\right)^{m} \\
\geq & \left(1-C m^{-1}\right)\left|\Gamma_{V}\right| \alpha_{D, m}(a),
\end{aligned}$$
where $C>0$ is a constant independent of $m$. For abbreviation, we use the same letter $C$ for constants independent of $m$. By Lemma 3.5, to prove (22), we only need to prove that
$$\sup _{t>0}\left(t \sum_{q=1}^{\infty} q^{1-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a) e^{1-q t} G_{m-1,3}(q t-1)\right) \leq \alpha_{D, m}(a)+\frac{C}{\sqrt{m}} .$$
Note that the standard Tian-Yau-Zelditch expansion implies that $\rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m}, q}(a) \leq C^{\prime} q^{n-1}$ for some constant $C^{\prime}>0$ independent of $m$ and $q$. An easy computation now shows that
$$\begin{aligned}
& \sup _{t>0}\left(t \sum_{\left\lfloor t^{-1}\right\rfloor-1 \leq q \leq\left\lfloor t^{-1}\right\rfloor+1} q^{1-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m, q}}(a) e^{1-q t} G_{m-1,3}(q t-1)\right) \\
\leq & \alpha_{D, m}+\sup _{t>0}\left(C e^{-\frac{(m-1) t^{2}}{10}}+C m t^{3}+C m t^{3} e^{-\frac{(m-1) t^{2}}{10}}\right) \leq \alpha_{D, m}+\frac{C}{\sqrt{m}} .
\end{aligned}$$
Then we estimate the remaining terms as follows.
$$\begin{aligned}
& \sup _{t>0}\left(t \sum_{\left|q-\left\lfloor t^{-1}\right\rfloor\right| \geq 2} q^{1-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m, q}}(a) e^{1-q t} G_{m-1,3}(q t-1)\right) \\
\leq & \sup _{t>0}\left(C t \sum_{q=1}^{\infty}\left(1+m|q t|^{3}\right) e^{-\frac{(m-1)|q t|^{2}}{2}}\right) \leq C \int_{0}^{\infty} t\left(1+m|t \xi|^{3}\right) e^{-\frac{(m-1)|t \xi|^{2}}{2}} d \xi \\
= & C \int_{0}^{\infty}\left(1+m y^{3}\right) e^{-\frac{(m-1) \zeta^{2}}{2}} d \zeta+C \sup _{\zeta>0}\left(m \zeta^{3} e^{-\frac{(m-1) \zeta^{2}}{2}}\right) \leq \frac{C}{\sqrt{m}},
\end{aligned}$$
and (22) is proved.
Since $\Theta_{\Gamma_{V}}(g)^{\left|\Gamma_{V}\right|}=1, \forall g \in \Gamma_{V}$, we see that $\rho_{D, \omega_{D}, \Delta_{\Gamma_{V}}, m, q}=\rho_{D, \omega_{D}, \Delta_{\Gamma_{V}, m+\left|\Gamma_{V}\right|}, q}, \forall m \in \mathbb{N}$. It follows that $\alpha_{D, m}=\alpha_{D, m+\left|\Gamma_{V}\right|}, \forall m \in \mathbb{N}$, which completes the proof. \(\square\)

Remark. For any integer $k \geq 0$ and $m \in \mathbb{N}$, let $\rho_{V / \Gamma_{V}, \omega_{V}, m}^{(k)}(x)$ be the $m$-th Bergman kernel function on $\left(V / \Gamma_{V}, \omega_{V}, \mathcal{L}_{V} / \Gamma_{V},\left|\log h_{D}\right|^{k} h_{V}\right)$.

As in the proof of Corollary 23, the series expansion (19) shows that there exists a constant $C=C\left(k, N, V,\left|\Gamma_{V}\right|\right)>0$, such that
$$\left|(2 \pi)^{\frac{3}{2}} n^{-1}(m k+m)^{-n-\frac{1}{2}} \sup _{x \in V / \Gamma_{V}} \rho_{V / \Gamma_{V}, \omega_{V}, m}^{(k)}(x)-\left|\Gamma_{V}\right| \alpha_{D, m}\right| \leq \frac{C}{\sqrt{m}},$$
where $\alpha_{D, m}=\sup _{a \in D} \sup _{q \in \mathbb{N}} q^{-n} \rho_{D, \omega_{D}, \Delta_{\Gamma_{V}}, m, q}(a)$.

\section*{4. Localization of Bergman kernels}

In this section, we establish some basic estimates for peak sections, and then use it to estimate the distance of global Bergman kernel and the Bergman kernel on asymptotic complex hyperbolic cusp. We will also show that this localization approach is also valid for the Poincaré type metrics.

\subsection*{4.1. Localization of peak sections.}

Let $(M, \omega)$ be a Kähler manifold, $\mathcal{L}$ be a holomorphic line bundle on $M$ equipped with a hermitian metric $h$ whose curvature form is $\omega$. For any closed subspace $X \subset H_{L^{2}}^{0}(M, \mathcal{L})$ and complex bounded linear functional $0 \neq T \in X^{*}$, we say that a section $S \in X$ is the peak section of $T$, if $\int_{M}\|S\|^{2} d \operatorname{Vol}_{\omega}=1$, and $T(S)=\|T\|$. By the Riesz representation theorem, $S$ is the peak section of $T$ if and only if $T(S) \in \mathbb{R}$, and $S \perp \operatorname{ker} T$ in $X \subset H_{L^{2}}^{0}(M, \mathcal{L})$. Note that $H_{L^{2}}^{0}(M, \mathcal{L})$ is a Hilbert space, and so is $X$. It follows that there exists a unique peak section of $T$ in $X$.

Let $U$ be an open subset of $M, X \subset H_{L^{2}}^{0}(U, \mathcal{L})$ be a closed subspace, and $0 \neq T \in X^{*}$. Then the restriction map gives a bounded linear embedding $H_{L^{2}}^{0}(M, \mathcal{L}) \rightarrow H_{L^{2}}^{0}(U, \mathcal{L})$. When $X \cap H_{L^{2}}^{0}(M, \mathcal{L}) \nsubseteq \operatorname{ker} T$, we see that $T \neq 0$ on $X \cap H_{L^{2}}^{0}(M, \mathcal{L})$, and hence we can find a unique peak section of $\left.T\right|_{X \cap H_{L^{2}}^{0}(M, \mathcal{L})}$ in $X \cap H_{L^{2}}^{0}(M, \mathcal{L})$. The peak section of $\left.T\right|_{X \cap H_{L^{2}}^{0}(M, \mathcal{L})}$ is called the peak section on $M$. The following lemma gives an estimate of the $L^{2}$ distance between the peak sections of $T \in X^{*}$ on $U$ and on $M$.