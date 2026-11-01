---
retention_scope: session
part: 3
total_parts: 4
---

[Part 3/4 of: [1404.3118] Yamabe type equations with a sign-changing nonlinearity, and the prescribed curvature problem]

Now, $y(t)=\sqrt{\chi(t)}$ solves
$$y^{\prime}=2 y^{2}-y(m-1) \frac{g_{\kappa}^{\prime}}{g_{\kappa}} \quad \text { on } \mathbb{R}^{+},$$
Suppose that $\zeta(\bar{t}) \leq 0$ for some $\bar{t}>0$. Then, an inspection of (5.42) and the fact that $g_{\kappa}^{\prime} / g_{\kappa}$ is decreasing show that $y^{\prime}>0$ on $[\bar{t},+\infty)$, whence there exists $c>0$ such that
$$y>\frac{m-1}{2} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}+c \quad \text { on }[\bar{t},+\infty) .$$
But then
$$\lim _{t \rightarrow+\infty} \zeta(t)=m \kappa-\lim _{t \rightarrow+\infty} y(t) \leq m \kappa-c-\frac{m-1}{2} \kappa=\frac{m+1}{2} \kappa-c,$$
contradicting (5.41) and proving the claim. Next, by (5.40) we can use the estimate $\left|\bar{\nabla}^{T} \bar{r}_{q}\right| \leq 1$ to conclude
$$\Delta u_{1} \leq\left[-m \sqrt{\chi\left(\bar{r}_{q}\right)} \frac{g_{\kappa}^{\prime}}{g_{\kappa}}+\sqrt{\chi\left(\bar{r}_{q}\right)}\left(m \frac{g_{\kappa}^{\prime}}{g_{\kappa}}-\sqrt{\chi\left(\bar{r}_{q}\right)}\right)\right] u_{1}=-\chi\left(\bar{r}_{q}\right) u_{1} .$$
For $\varepsilon>0$, consider the truncated function $\chi_{\varepsilon}(t)$ given by $\chi_{\varepsilon}(t)=\chi(t)$ if $t \geq 2 \varepsilon$, and 0 otherwise. Then, $\chi_{\varepsilon}\left(\bar{r}_{q} \circ F\right) \in L_{\text {loc }}^{\infty}(M)$ and by (5.43)
$$\Delta u_{1}+\chi_{\varepsilon}\left(\bar{r}_{q}\right) u_{1} \leq 0 \quad \text { on } M \backslash F^{-1}\{q\} .$$
If $F^{-1}\{q\} \neq \emptyset$ observe that the constant function $u_{2} \doteq \sqrt{G_{q}(\varepsilon)}$ solves (5.44) on $F^{-1}\left\{B_{2 \varepsilon}(q)\right\}$. By the pasting Lemma 3.1 with the choices $\Omega_{1} \doteq F^{-1}\left\{B_{\varepsilon}(q)\right\} \backslash F^{-1}\{q\}$, $\Omega_{2} \doteq F^{-1}\left\{B_{2 \varepsilon}(q)\right\} \backslash F^{-1}\{q\}$, and since $h^{\prime}<0$, we deduce that
$$u \doteq \begin{cases}\sqrt{G_{q}(\varepsilon)} & \text { on } F^{-1}\left\{B_{\varepsilon}(q)\right\}, \\ \sqrt{G_{q}} & \text { on } M \backslash F^{-1}\left\{B_{\varepsilon}(q)\right\}\end{cases}$$
solves $\Delta u+\chi_{\varepsilon}\left(\bar{r}_{q}\right) u \leq 0$ on $\Omega_{2}=F^{-1}\left\{B_{2 \varepsilon}(q)\right\} \backslash F^{-1}\{q\}$. Since the pasting region $F^{-1}\left\{\partial B_{\varepsilon}(q)\right\}$ is internal to $\Omega_{2}$ and $u$ is smooth in a neighbourhood of $F^{-1}\{q\}$, then clearly $u$ solves
$$\Delta u+\chi_{\varepsilon}\left(\bar{r}_{q}\right) u \leq 0 \quad \text { on the whole } M .$$
By Proposition 3.4 with $p=2, f=1$ and $V=\chi_{\varepsilon}\left(\bar{r}_{q}\right)$ we deduce that $\lambda_{V}(M) \geq 0$, that is
$$\int_{M} \chi_{\varepsilon}\left(\bar{r}_{q} \circ F\right) \varphi^{2} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{2} \mathrm{~d} x \quad \text { for each } \varphi \in \operatorname{Lip}_{c}(M),$$
whence, letting $\varepsilon \rightarrow 0$ and using monotone convergence we deduce (5.31). The cases (5.33), (5.34), (5.35) follow by computing $\chi(r)$ according to Example 5.3, in particular see (5.21), (5.23), (5.24). \(\square\)
5.3. Specializing our main theorems: an example. To illustrate the results of the last two sections, by way of an example we specialize our Theorem 2.1 to the case of quasilinear Yamabe type equations on Cartan-Hadamard manifolds. We underline that all the assumptions in the next Corollary are explicit and easy to check. Clearly, analogous results can be stated using any of Theorems 5.1, 5.2, 5.3, as well as Theorem 2.2 instead of Theorem 2.1

Corollary 5.1. Let $M$ be a Cartan-Hadamard manifold of dimension $m \geq 3$, and let $p \in(1, m)$. Let $a, b \in L_{\text {loc }}^{\infty}(M)$, and suppose that, for some countable set of points $\left\{y_{j}\right\}_{j \in I} \subset M$ and $\left\{t_{j}\right\}_{j \in I} \subset[0,1]$ with $\sum_{j} t_{j} \leq 1$,
$$a(x) \leq\left(\frac{m-p}{p}\right)^{p} \sum_{j \in I} \frac{t_{j}}{\operatorname{dist}\left(x, y_{j}\right)^{p}} .$$
Furthermore, suppose that
\begin{itemize}
\item[i)] $b_{-}(x)$ has compact support;
\item[ii)] $a(x)=O(b(x))$ as $x$ diverges
\item[iii)] for some $\theta>0,\left(a(x)-\theta b_{+}(x)\right)_{-} \in L^{1}(M)$.
\end{itemize}
Fix a nonlinearity $F(t)$ satisfying (2.6). Then, there exists $\delta>0$ such that if
$$b(x) \geq-\delta \quad \text { on } M,$$
there exists a weak solution $u \in C_{\text {loc }}^{1, \mu}(M)$ of
$$\left\{\begin{array}{l}
\Delta_{p} u+a(x) u^{p-1}-b(x) F(u)=0 \quad \text { on } M, \\
0<u \leq\|u\|_{L^{\infty}(M)<+\infty .}
\end{array}\right.$$
Proof. In view of Theorem 2.1, it is enough to prove that $-\Delta_{p}$ and $Q_{a}$ are subcritical on $M$. By Theorem 5.2, the Hardy inequality
$$\left(\frac{m-p}{p}\right)^{p} \int_{M} \sum_{j \in I} \frac{t_{j}}{\operatorname{dist}\left(x, y_{j}\right)^{p}}|\varphi(x)|^{p} \mathrm{~d} x \leq \int_{M}|\nabla \varphi(x)|^{p} \mathrm{~d} x$$
holds for $\varphi \in \operatorname{Lip}_{c}(M)$. Therefore, by Proposition 4.4. $-\Delta_{p}$ is subcritical. Next, the fact that the inequality in (5.46) is strict on a set of positive measure (the right-hand side is essentially unbounded at each $y_{j}$ ) assures that $Q_{a}$ be subcritical by Proposition 4.5. \(\square\)

\section*{6. Proofs of Theorems 2.1 and 2.2}

We first address the local solvability of the Dirichlet problem for
$$\Delta_{p, f} u+A(x) u^{p-1}-B(x) F(u)=0$$
when $B \geq 0$.
Lemma 6.1. Let $M$ be a Riemannian manifold, $p \in(1,+\infty)$ and $f \in C^{\infty}(M)$. Let $\Omega \subseteq M$ be a smooth relatively compact open set, and let $A(x), B(x) \in L^{\infty}(\Omega)$ satisfy $\lambda_{A}(\Omega)>0$ and $B \geq 0$ a.e. on $\Omega$. Then, for each nonlinearity $F(t)$ that satisfies (2.6), and for each $\varphi \in C^{1, \alpha}(\partial \Omega), \alpha \in(0,1)$ such that $\varphi \geq 0, \varphi \not \equiv 0$, there exist $\mu \in(0,1)$ and a unique $0<z \in C^{1, \mu}(\bar{\Omega})$ solving
$$\begin{cases}\Delta_{p, f} z+A(x) z^{p-1}-B(x) F(z)=0 & \text { on } \Omega, \\ z=\varphi & \text { on } \partial \Omega .\end{cases}$$

Proof. Take the positive solution $z_{0} \in C^{1, \mu}(\bar{\Omega})$ of
$$\begin{cases}\Delta_{p, f} z_{0}+A\left|z_{0}\right|^{p-2} z_{0}=0 & \text { on } \Omega \\ z_{0}=\varphi & \text { on } \partial \Omega\end{cases}$$
which exists by Proposition 3.4. Since $B \geq 0, z_{0}$ gives rise to a supersolution for (6.1). To construct a subsolution with boundary value $\varphi$, we solve
$$\begin{cases}\Delta_{p, f} z_{1}+\left(A-B_{1}\right)\left|z_{1}\right|^{p-2} z_{1}=0 & \text { on } \Omega, \quad B_{1} \doteq B \frac{F\left(z_{0}\right)}{z_{0}^{p-1}} \\ z_{1}=\varphi & \text { on } \partial \Omega .\end{cases}$$
Since $A-B_{1} \leq A, \lambda_{A-B_{1}}(\Omega)>0$, thus $z_{1}$ exists and, by comparison, $z_{1} \leq z_{0}$. Since $F(t) / t^{p-1}$ is increasing,
$$\Delta_{p, f} z_{1}+\left(A-B \frac{F\left(z_{1}\right)}{z_{1}^{p-1}}\right) z_{1}^{p-1} \geq \Delta_{p, f} z_{1}+\left(A-B \frac{F\left(z_{0}\right)}{z_{0}^{p-1}}\right) z_{1}^{p-1}=0$$
Hence $z_{1}$ is a subsolution for (6.1). Applying the subsolution-supersolution method (see [25], Theorem 4.14 page 272) we obtain the existence of $z$ satisfying (6.1). The local Harnack inequality in Theorem 3.1 gives $z>0$ on $\bar{\Omega}$, and uniqueness follows from the comparison Proposition 3.3. \(\square\)

Next, we investigate the existence of local uniform lower bounds for solutions of the Dirichlet problem when $\Omega$ varies.

Lemma 6.2. Let ( $M,\langle$,$\rangle ) be a Riemannian manifold, f \in C^{\infty}(M), p \in(1,+\infty)$, and assume that $Q_{0}$ is subcritical on $M$. Let $A, B \in L_{\text {loc }}^{\infty}(M)$ such that
$$\left\{\begin{array}{l}
Q_{A} \text { is non-negative, } \\
(A(x)-\theta B(x))_{-} \in L^{1}\left(M, \mathrm{~d} \mu_{f}\right), \quad \text { for some constant } \theta>0 .
\end{array}\right.$$
Fix $\varepsilon>0$. Consider a triple of relatively compact, open sets $\Lambda \Subset \Lambda^{\prime} \Subset \Omega \subseteq M$, with $\partial \Omega$ smooth, and let $z \in C^{1, \mu}(\bar{\Omega})$ be a positive solution of
$$\begin{cases}\Delta_{p, f} z+A(x) z^{p-1}-B(x) F(z) \leq 0 & \text { on } \Omega ; \\ z=\varepsilon & \text { on } \partial \Omega\end{cases}$$
Then, there exists $C>0$ depending on $\varepsilon$, but independent of $\Omega$, such that
$$\inf _{\Lambda} z \geq C .$$
Proof. Observe that, by the half-Harnack inequality in Theorem 3.1, $z>0$ on $\Omega$. By comparison, we can also suppose that $z$ solves (6.3) with the equality sign, whence $z \in C^{1, \mu}(\bar{\Omega})$. Fix $\delta \in(0, \varepsilon)$ small enough that
$$\frac{F(t)}{t^{p-1}}<\theta \quad \text { if } t \in(0, \delta) .$$
This is possible by (2.6). Let $\eta \in \operatorname{Lip}_{\text {loc }}(\mathbb{R}), \eta(\log \varepsilon)=0$ to be specified later, and define $u=\log z$ on $\Omega$, so that, weakly,
$$\left\{\begin{array}{lr}
\Delta_{p, f} u=-A+B \frac{F(z)}{z^{p-1}}-(p-1)|\nabla u|^{p} & \text { on } \Omega \\
u=\log \varepsilon & \text { on } \partial \Omega .
\end{array}\right.$$
The function $\eta(u) \in \operatorname{Lip}_{0}(\Omega)$ can be used as a test function for (6.6) to obtain
$$\int_{\Omega}\left[(p-1) \eta(u)-\eta^{\prime}(u)\right]|\nabla u|^{p} \mathrm{~d} \mu_{f}=\int_{\Omega}\left[-A+B \frac{F(z)}{z^{p-1}}\right] \eta(u) \mathrm{d} \mu_{f} .$$

Let $L(\delta) \doteq\{x: u(x)<\log \delta\}$. Choose
$$\eta(t)=\left[1-\frac{e^{(p-1) t}}{\delta^{p-1}}\right] 1_{(-\infty, \log \delta)}(t) \in \operatorname{Lip}(\mathbb{R}) .$$
Then, from (6.7) and (6.2), and since $\delta \in(0, \varepsilon), \eta(\log \varepsilon)=0$. Plugging in (6.7) and using (6.5) we deduce
$$\int_{L(\delta)}|\nabla u|^{p} \mathrm{~d} \mu_{f} \leq \frac{1}{p-1} \int_{L(\delta)}\left[-A+B \frac{F(z)}{z^{p-1}}\right] \eta(u) \mathrm{d} \mu_{f} \leq \frac{1}{p-1}\left\|(A-\theta B)_{-}\right\|_{L^{1}\left(M, \mathrm{~d} \mu_{f}\right)}$$
Since $Q_{0}$ is subcritical on $M$, by Proposition 4.4 there exists $W \in C^{0}(M), W>0$ on $M$ such that
$$\int_{M} W|\varphi|^{p} \mathrm{~d} \mu_{f} \leq \int_{M}|\nabla \varphi|^{p} \mathrm{~d} \mu_{f} \quad \forall \varphi \in \operatorname{Lip}_{c}(M) .$$
Now the function $\varphi(x)=(u(x)-\log \delta) 1_{L(\delta)}(x)$, extended with 0 outside $\Omega$, is an admissible test function for (6.9) and with this choice of $\varphi$ we obtain
$$\int_{L(\delta)}|\nabla u|^{p} \mathrm{~d} \mu_{f} \geq \int_{L(\delta)} W|u-\log \delta|^{p} \mathrm{~d} \mu_{f} .$$
By contradiction assume that there exists a sequence of relatively compact open sets $\left\{\Omega_{j}\right\}$ with smooth boundary such that $\Lambda^{\prime} \Subset \Omega_{j}$ and a sequence of associated solutions $\varphi_{j}$ of (6.3), such that $\inf _{\Lambda} \varphi_{j} \rightarrow 0^{+}$as $j \rightarrow+\infty$. Using Harnack inequality of Theorem 3.13 ), $\phi_{j} \rightarrow 0$ uniformly on $\Lambda$ as $j \rightarrow+\infty$ (note that, to infer $\phi_{j} \rightarrow 0$, we need that each $\Omega_{j}$ contains a fixed domain larger than $\Lambda$, which accounts for the presence of $\Lambda^{\prime}$ ). Having fixed $N>0$, we choose $j_{0}$ large enough that $u_{j}=\log \varphi_{j}<-N+\log \delta$ on $\Lambda$ when $j \geq j_{0}$. Consequently, $\Lambda \subset\left\{u_{j}<\log \delta\right\} \doteq L_{j}(\delta)$, and from (6.8) and (6.10) we deduce
$$\begin{aligned}
N^{p} \int_{\Lambda} W \mathrm{~d} \mu_{f} & \leq \int_{L_{j}(\delta)} W\left|u_{j}-\log \delta\right|^{p} \mathrm{~d} \mu_{f} \leq \int_{L_{j}(\delta)}\left|\nabla u_{j}\right|^{p} \mathrm{~d} \mu_{f} \\
& \leq \frac{1}{p-1}\left\|(A-\theta B)_{-}\right\|_{L^{1}\left(M, \mathrm{~d} \mu_{f}\right)} .
\end{aligned}$$
This gives a contradiction provided $N$ is large enough, proving the validity of (6.4). \(\square\)

Remark 6.1. To guarantee (6.4), the second condition in (6.2) cannot be relaxed too much. To see this, let us suppose that $B \equiv 0$, for which the second in (6.2) reads $A_{-} \in L^{1}\left(M, \mathrm{~d} \mu_{f}\right)$. We first observe that the validity of (6.4) is granted provided that there exists a positive, bounded solution of $Q_{A}^{\prime}(u)=0$ on $M$. Indeed, if such a $u$ exists, comparing a solution $z$ of (6.3) with $\varepsilon u /\|u\|_{L^{\infty}(M)}$ with the aid of Proposition 3.3 yields (6.4). If, on the other hand, there exists a positive solution of $Q_{A}^{\prime}(u)=0$ with $u(x) \rightarrow+\infty$ as $x$ diverges, (6.4) fails: indeed, if we consider a smooth exhaustion $\left\{\Omega_{j}\right\}$ with $\partial \Omega_{j} \subset\{u \in[j, j+1)\}$, we compare the solution of (6.3) on $\Omega_{j}$ (with the equality sign) and the function $\varepsilon u / j$, and we let $j \rightarrow 0$, it is easy to see that the left-hand side of (6.4) is zero.
Now, consider the case $p=2, f \equiv 0$. In Theorem 3 of [13] we have shown that, if $M$ is a manifold with a pole $o$, dimension $m \geq 3$ and radial sectional curvature $K_{\text {rad }} \leq 0$,
and for $A \in L_{\text {loc }}^{\infty}(M)$, conditions
$$\left\{\begin{array}{l}
|A(x)| \leq \bar{A}(r(x)) \leq \frac{(m-2)^{2}}{4} \frac{1}{r(x)^{2}} \quad \text { on } M, \\
r \bar{A}(r) \in L^{1}(+\infty),
\end{array}\right.$$
imply the existence of a positive bounded solution $u \in C_{\text {loc }}^{1, \mu}(M)$ of $Q_{A}^{\prime}(u)=0$. Thus, in this case (6.4) holds true. On the other hand, by Theorem 11 of [13] if, for $A \in L_{\text {loc }}^{\infty}\left(\mathbb{R}^{m}\right)$
$$\left\{\begin{array}{l}
\bar{A}_{1}(r(x)) \leq A(x) \leq \bar{A}_{2}(r(x)) \leq \frac{(m-2)^{2}}{4} \frac{1}{r(x)^{2}} \quad \text { on } \mathbb{R}^{m}, \\
r\left[\bar{A}_{j}(r)-k \frac{(m-2)^{2}}{4 r^{2}}\right] \in L^{1}(+\infty),
\end{array}\right.$$
for some $k<0$ and $j \in\{1,2\}$, then there exists a positive solution $u$ of $Q_{A}^{\prime}(u)=0$ on $\mathbb{R}^{m}$ such that $u(x) \rightarrow+\infty$ as $x \rightarrow \infty$ and so (6.4) cannot hold. Note that (6.11) is weaker than $A_{-} \in L^{1}(M)$. However, we stress that it seems hard to find conditions analogous of (6.11) and (6.12) on more general manifolds and for nonlinear operators.

We now investigate the existence of uniform upper bounds, i.e. independent of $\Omega$, for the solutions of (6.1) with boundary data $\varphi=1$. The next lemma, Lemma 2.1 of the Introduction, ensures global $L^{\infty}$-estimates. In view of a subtle asymmetry between bounds from below and above, to reach our goal we had to find a new strategy.

Lemma 6.3. Let $M$ be a Riemannian manifold, $f \in C^{\infty}(M), p \in(1,+\infty)$ and fix $F(t)$ satisfying (2.6). Let $A, B \in L_{\text {loc }}^{\infty}(M)$ with $B \geq 0$ a.e. on $M$. Assume that either
\begin{itemize}
\item[(i)] $B \equiv 0$ and $Q_{A}$ is subcritical, or
\item[(ii)] $B \not \equiv 0$ and $Q_{A}$ is non-negative.
\end{itemize}
Suppose that there exist a smooth, relatively compact open set $\Lambda \Subset M$ and a constant $c>0$ such that
$$A \leq c B \quad \text { a.e. on } M \backslash \Lambda,$$
and fix a smooth, relatively compact open set $\Lambda^{\prime}$ such that $\Lambda \Subset \Lambda^{\prime}$, and a constant $\varepsilon>0$.
Then, there exists a constant $C_{\Lambda}>0$ depending on $\varepsilon, p, f, F, c, A, B, \Lambda, \Lambda^{\prime}$ but not on $\Omega$ such that for each smooth, relatively compact open set $\Omega$ with $\Lambda^{\prime} \Subset \Omega$, the solution $0<z \in C^{1, \mu}(\bar{\Omega})$ of
$$\begin{cases}\Delta_{p, f} z+A(x) z^{p-1}-B(x) F(z)=0 & \text { on } \Omega \\ z=\varepsilon & \text { on } \partial \Omega\end{cases}$$
satisfies
$$z \leq C_{\Lambda} \quad \text { on } \Omega .$$

Proof. Without loss of generality, we can suppose that $c>1$. Using that, by (2.6), $F(t) / t^{p-1} \rightarrow+\infty$ as $t \rightarrow+\infty$, we can fix $\alpha>\varepsilon$ such that
$$\frac{F(t)}{t^{p-1}} \geq c \quad \text { for } t \geq \alpha .$$
Consider the open set
$$U=\{x \in \Omega: z(x)>\alpha\} .$$

We note that $U \Subset \Omega$ and that, by (6.16), $z$ solves
$$\begin{cases}\Delta_{p, f} z+(A-c B) z^{p-1} \geq 0 & \text { on } U \\ z=\alpha & \text { on } \partial U,\end{cases}$$
If $U=\emptyset$, for each $\Omega, z$, then (6.15) trivially holds with $C_{\Lambda}=\alpha$. Therefore, suppose that $U \neq 0$ for some $\Omega, z$. By (6.17) and (6.13), $\Delta_{p, f} z \geq 0$ on $U \backslash \Lambda$. Thus, in the case $U \cap \Lambda=\emptyset, \Delta_{p, f} z \geq 0$ on $U$. For $\varepsilon>0$ small, choose a smooth increasing sequence $\left\{U_{\varepsilon}\right\}$ exhausting $U$ as $\varepsilon \rightarrow 0$ and such that $z \leq \alpha+\varepsilon$ on $\partial U_{\varepsilon}$. Applying Proposition 3.3 we infer that $z \leq \alpha+\varepsilon$ on $U_{\varepsilon}$, thus letting $\varepsilon \rightarrow 0$ we get $z \leq \alpha$ on $U$, contradicting its very definition. Hence, we conclude that $U \cap \Lambda \neq \emptyset$. Note that
$$\sup _{U \cap \Lambda} z \geq \alpha=z_{\mid \partial U},$$
and since $\Delta_{p, f} z \geq 0$ on $U \backslash \Lambda$, again via Proposition 3.3 we obtain
$$\sup _{U \backslash \Lambda} z=\sup _{\partial(U \backslash \Lambda)} z \leq \max \left\{\sup _{\partial U} z, \sup _{\partial \Lambda} z\right\}=\max \left\{\alpha, \sup _{\partial \Lambda \cap U} z\right\} \leq \sup _{U \cap \Lambda} z .$$
It follows that
$$\text { if } U=\{z>\alpha\} \neq \emptyset, \quad \text { then } \quad \sup _{U} z \equiv \sup _{\Lambda} z \text {. }$$
To prove (6.15) we proceed by contradiction: if it does not hold, and in view of (6.18) there exists a sequence of triples $\left(\Omega_{j}, z_{j}, U_{j}\right)$, where $\Omega_{j}$ is a smooth, relatively compact open set such that $\Lambda^{\prime} \Subset \Omega_{j}, z_{j}$ is a solution of
$$\left\{\begin{array}{l}
\Delta_{p, f} z_{j}+\left(A-B \frac{F\left(z_{j}\right)}{z_{j}^{p-1}}\right) z_{j}^{p-1}=0 \quad \text { on } \Omega_{j}, \\
z_{j}=\varepsilon \quad \text { on } \partial \Omega_{j},
\end{array}\right.$$
$U_{j}=\left\{x \in \Omega_{j}: z_{j}(x)>\alpha\right\}$, and
$$\left\|z_{j}\right\| \doteq\left\|z_{j}\right\|_{L^{\infty}(\Lambda)} \rightarrow+\infty \quad \text { as } j \rightarrow+\infty .$$
Up to taking $j$ large enough, we can suppose that $\left\|z_{j}\right\|>2 \alpha$. Consider the rescaled functions
$$h_{j} \doteq \frac{z_{j}}{\left\|z_{j}\right\|} \quad \text { on } \Omega_{j}$$
and note that they all solve
$$\left\{\begin{array}{l}
\Delta_{p, f} h_{j}+A h_{j}^{p-1} \geq 0 \quad \text { on } \Lambda^{\prime}, \\
\sup _{\Lambda} h_{j}=1, \quad h_{j} \leq \frac{\alpha}{\left\|z_{j}\right\|}<\frac{1}{2} \quad \text { on } \Omega_{j} \backslash U_{j} .
\end{array}\right.$$
By (6.22) and the half-Harnack inequality of Theorem 3.1 (3a) there exists $C_{H}>0$ such that
$$1=\left\|h_{j}\right\|_{L^{\infty}(\Lambda)} \leq C_{H}\left\|h_{j}\right\|_{L^{p}\left(\Lambda^{\prime}, \mathrm{d} \mu_{f}\right)} \quad \forall j .$$
Next we define
$$\eta_{j}(x)= \begin{cases}\frac{z_{j}(x)-\alpha}{\left\|z_{j}\right\|} & \text { on } U_{j} \\ 0 & \text { on } M \backslash U_{j} .\end{cases}$$

Then, $0 \leq \eta_{j} \in \operatorname{Lip}_{c}(M)$. Let $V=A-c B$. Thus, $V \leq 0$ on $M \backslash \Lambda$ and, by (6.17), $Q_{V}^{\prime}\left(z_{j}\right) \leq 0$ on $U_{j}$, therefore
$$\begin{aligned}
0 \leq Q_{V}\left(\eta_{j}\right) & =\frac{1}{p} Q_{V}^{\prime}\left(\eta_{j}\right)\left[\eta_{j}\right] \\
& =\frac{1}{p\left\|z_{j}\right\|^{p-1}} \int_{U_{j}}\left[\left|\nabla z_{j}\right|^{p-2}\left\langle\nabla z_{j}, \nabla \eta_{j}\right\rangle-V\left(z_{j}-\alpha\right)^{p-1} \eta_{j}\right] \mathrm{d} \mu_{f} \\
& \leq \frac{1}{p\left\|z_{j}\right\|^{p}} \int_{U_{j}} V\left\{z_{j}^{p-1}-\left(z_{j}-\alpha\right)^{p-1}\right\}\left(z_{j}-\alpha\right) \mathrm{d} \mu_{f} \\
& \leq \frac{1}{p\left\|z_{j}\right\|^{p}} \int_{U_{j} \cap \Lambda} V\left[z_{j}^{p-1}-\left(z_{j}-\alpha\right)^{p-1}\right]\left(z_{j}-\alpha\right) \mathrm{d} \mu_{f} \\
& \leq \frac{1}{p\left\|z_{j}\right\|^{p}} \int_{U_{j} \cap \Lambda} V_{+}(x)\left[z_{j}^{p}-\left(z_{j}-\alpha\right)^{p}\right] \mathrm{d} \mu_{f} .
\end{aligned}$$
We observe that on $[\alpha,+\infty)$, the function
$$\rho(t)=t^{p}-(t-\alpha)^{p}$$
is increasing and
$$\rho(t) \sim p \alpha t^{p-1} \quad \text { as } t \rightarrow+\infty .$$
We thus infer the existence of constants $c_{1}, c_{2}>0$ just depending on $\alpha$ and such that
$$\rho(t) \leq c_{1} t^{p-1}+c_{2} \quad \text { on }[\alpha,+\infty) .$$
Hence
$$\begin{aligned}
& \frac{1}{p\left\|z_{j}\right\|^{p}} \int_{U_{j} \cap \Lambda} V_{+}(x)\left[z_{j}^{p}-\left(z_{j}-\alpha\right)^{p}\right] \mathrm{d} \mu_{f} \leq \frac{\left\|V_{+}\right\|_{L^{\infty}(\Lambda)}}{p\left\|z_{j}\right\|^{p}} \int_{U_{j} \cap \Lambda}\left(c_{1} z_{j}^{p-1}+c_{2}\right) \mathrm{d} \mu_{f} \\
& \leq \frac{\left\|V_{+}\right\|_{L^{\infty}(\Lambda)}}{p\left\|z_{j}\right\|} \operatorname{vol}_{f}(\Lambda) c_{1}+\frac{\left\|V_{+}\right\|_{L^{\infty}(\Lambda)}}{p\left\|z_{j}\right\|^{p}} \operatorname{vol}_{f}(\Lambda) c_{2} \quad \longrightarrow 0 \quad \text { as } j \rightarrow+\infty .
\end{aligned}$$
This fact, together with inequality (6.25), implies that $Q_{V}\left(\eta_{j}\right) \rightarrow 0$ as $j \rightarrow+\infty$. Now, in both cases $(i)$ and (ii) in the statement of the lemma, $Q_{V}$ is subcritical on $M$. In fact, if $(i)$ holds, $V \equiv A$ and $Q_{A}$ is assumed to be subcritical, while under the validity of (ii) the subcriticality property (2.10) follows from
$$Q_{V}(\varphi)=Q_{A}(\varphi)+\int_{M}(c B)|\varphi|^{p} \mathrm{~d} \mu_{f} \geq \int_{M}(c B)|\varphi|^{p} \mathrm{~d} \mu_{f}$$
By Theorem 4.1, $Q_{V}$ has thus a weighted spectral gap, and in particular $\eta_{j} \rightarrow 0$ in $L_{\text {loc }}^{p}(M)$. Since, by definition (6.21),
$$h_{j}=\eta_{j}+\frac{\alpha}{\left\|z_{j}\right\|} \quad \text { on } U_{j},$$
we deduce that
$$\left\|h_{j}\right\|_{L^{p}\left(\Lambda^{\prime} \cap U_{j}, \mathrm{~d} \mu_{f}\right)} \rightarrow 0 \quad \text { as } j \rightarrow+\infty$$
and since $h_{j} \leq \frac{\alpha}{\left\|z_{j}\right\|}$ on $\Lambda^{\prime} \backslash U_{j}$ we conclude that
$$h_{j} \rightarrow 0 \quad \text { in } L^{p}\left(\Lambda^{\prime}, \mathrm{d} \mu_{f}\right) \quad \text { as } j \rightarrow+\infty .$$
This contradicts (6.23) and proves the claimed (6.15). \(\square\)

Lemmas 6.2 and 6.3 enable us to prove

Proposition 6.1. Let ( $M,\langle$,$\rangle ) be a Riemannian manifold, f \in C^{\infty}(M), p \in(1,+\infty)$ and suppose that $Q_{0}$ is subcritical on $M$. Let $V \in L^{\infty}(M)$ have compact support and assume that $Q_{V}$ is subcritical on $M$. Then, there exists a positive solution $g \in C_{\text {loc }}^{1, \mu}(M)$ of
$$-Q_{V}^{\prime}(g)=\Delta_{p, f} g+V|g|^{p-2} g=0 \quad \text { on } M$$
satisfying
$$C^{-1} \leq g(x) \leq C \quad \text { on } M$$
for some constant $C>1$.
Proof. Let $\Lambda$ be a smooth, relatively compact open set such that $V \equiv 0$ on $M \backslash \Lambda$, and consider an exhaustion $\left\{\Omega_{j}\right\}$ of $M$ by smooth, relatively compact open sets with $\bar{\Lambda} \subset \Omega_{1}$. We let $\varphi_{j} \in C^{1, \mu_{j}}\left(\bar{\Omega}_{j}\right)$ be the positive solution of
$$\begin{cases}Q_{V}^{\prime}\left(\varphi_{j}\right)=0 & \text { on } \Omega_{j}, \\ \varphi_{j}=1 & \text { on } \partial \Omega_{j},\end{cases}$$
whose existence is granted by iv) of Proposition 3.4. Our assumptions enable us to apply Lemma 6.2 and 6.3 and to conclude the existence of a constant $C>1$ independent of $j$, for which
$$C^{-1} \leq \varphi_{j}(x) \leq C \quad \text { on } \Lambda .$$
On the other hand, because of (6.28) and $V \equiv 0$ on $M \backslash \Lambda$, we have
$$\left\{\begin{array}{l}
\Delta_{p, f} \varphi_{j}=0 \quad \text { on } \Omega_{j} \backslash \bar{\Lambda} \\
\varphi_{j}=1 \quad \text { on } \partial \Omega_{j}, \quad C^{-1} \leq \varphi_{j} \leq C \quad \text { on } \partial \Lambda,
\end{array}\right.$$
and thus, by the comparison Proposition 3.3,
$$C^{-1} \leq \varphi_{j}(x) \leq C \quad \text { on } \Omega_{j} .$$
Hence, the $\varphi_{j}$ 's are uniformly bounded from above and below. By elliptic estimates $\varphi_{j} \rightarrow g$ for some $g \in C_{\text {loc }}^{1, \mu}(M)$ solving $Q_{V}^{\prime}(g)=0$ and satisfying (6.27). \(\square\)

We are ready to prove Theorem 2.1. We rewrite its statement for the convenience of the reader.

Theorem 6.1. Let $M^{m}$ be a Riemannian manifold, $f \in C^{\infty}(M), p \in(1,+\infty)$, and suppose that $Q_{0}$ is subcritical on $M$. Let $a, b \in L_{\text {loc }}^{\infty}(M)$. Assume that $Q_{a}$ is subcritical and that
\begin{itemize}
\item[i)] $b_{-}$has compact support;
\item[ii)] for some $\theta>0,\left(a-\theta b_{+}\right)_{-} \in L^{1}\left(M, \mathrm{~d} \mu_{f}\right)$;
\item[iii)] $a(x)=O\left(b_{+}(x)\right)$ as $x$ diverges.
\end{itemize}

Then, there exists $\delta>0$ such that, if
$$b(x) \geq-\delta \quad \text { on } M,$$
we can find a solution $u \in C_{\text {loc }}^{1, \mu}(M)$ of
$$\left\{\begin{array}{l}
\Delta_{p, f} u+a(x) u^{p-1}-b(x) F(u)=0 \quad \text { on } M, \\
0<u \leq\|u\|_{L^{\infty}(M)<+\infty} \quad \text { on } M .
\end{array}\right.$$

Moreover, if ii) and iii) are replaced by the stronger condition
$$a(x) \asymp b_{+}(x) \quad \text { as } x \text { diverges, }$$
then $u$ can be constructed with the further property that $\inf _{M} u>0$.
Proof. By assumption $i i i)$, there exists a relatively compact, open subset $\Lambda$ containing $\operatorname{supp}\left(b_{-}\right)$, and a constant $C \geq \theta$ such that
$$a(x) \leq C b_{+}(x) \quad \text { on } M \backslash \Lambda .$$
The subcriticality of $Q_{a}$ on $M$ implies, via Theorem 4.1, that $Q_{a}$ has a weighted spectral gap, that is, there exists $W \in C^{0}(M), W>0$ on $M$ such that
$$\int_{M} W(x)|\varphi|^{p} \mathrm{~d} \mu_{f} \leq Q_{a}(\varphi) \quad \forall \varphi \in \operatorname{Lip}_{c}(M) .$$
In particular, if $A(x)=a(x)+W(x) 1_{\Lambda}(x)$ then $Q_{A}$ is still subcritical on $M$. Fix $\varepsilon>0$ and a relatively compact subset $\Lambda^{\prime}$ with $\Lambda \Subset \Lambda^{\prime}$. Next, consider a smooth, relatively compact open set $\Omega$ with $\Lambda^{\prime} \Subset \Omega$. Applying Lemma 6.1 with the choices $A=a$ (respectively, $A=a+W 1_{\Lambda}$ ) and $B=b_{+}$, we produce solutions $\varphi_{\infty}, \varphi_{0}$ of
$$\begin{aligned}
& \begin{cases}\Delta_{p, f} \varphi_{\infty}+a \varphi_{\infty}^{p-1}-b_{+} F\left(\varphi_{\infty}\right)=0 & \text { on } \Omega, \\
\varphi_{\infty}=\varepsilon & \text { on } \partial \Omega,\end{cases} \\
& \begin{cases}\Delta_{p, f} \varphi_{0}+\left(a+W 1_{\Lambda}\right) \varphi_{0}^{p-1}-b_{+} F\left(\varphi_{0}\right)=0 & \text { on } \Omega, \\
\varphi_{0}=\varepsilon & \text { on } \partial \Omega .\end{cases}
\end{aligned}$$
By comparison, $\varphi_{\infty} \leq \varphi_{0}$. By Lemma 6.2, because of assumption $i i$ ) we can guarantee the existence of a constant $\bar{C}_{\Lambda}(\varepsilon)>0$ (we emphasize its dependence on $\varepsilon$ ), independent of $\Omega$, such that
$$\varphi_{\infty} \geq \bar{C}_{\Lambda}(\varepsilon) \quad \text { on } \Lambda .$$
On the other hand, (6.33) implies that $a+W 1_{\Lambda} \leq C b_{+}$outside of $\Lambda$. Hence, Lemma 6.3 ensures the existence of $C_{\Lambda}(\varepsilon)$ independent of $\Omega$ and such that
$$\left(\varphi_{\infty} \leq\right) \varphi_{0} \leq C_{\Lambda}(\varepsilon) \quad \text { on } \Omega,$$
and we can also consider the sharpest one, that is,
$$C_{\Lambda}(\varepsilon) \doteq \sup _{\substack{\Omega: \Omega \text { open smooth, } \\ \Lambda^{\prime} \Subset \Omega \Subset M}}\left\|\varphi_{0}\right\|_{L^{\infty}(\Omega)},$$
where $\varphi_{0}$ solves (6.36). As a consequence of the comparison Proposition 3.3, $C_{\Lambda}(\varepsilon)$ is non-increasing as a function of $\varepsilon$.

Define
$$\delta=\left(\min _{\bar{\Lambda}} W\right)\left[\frac{C_{\Lambda}(\varepsilon)^{p-1}}{F\left(C_{\Lambda}(\varepsilon)\right)}\right],$$
and observe that, by assumption (6.30), our definition (6.40) of $\delta$ and the fact that $F(t) / t^{p-1}$ is increasing,
$$b_{-}\left[\frac{F\left(\varphi_{0}\right)}{\varphi_{0}^{p-1}}\right] \leq \delta 1_{\Lambda}\left[\frac{F\left(C_{\Lambda}(\varepsilon)\right)}{C_{\Lambda}(\varepsilon)^{p-1}}\right]=\left(\min _{\bar{\Lambda}} W\right) 1_{\Lambda} \leq W 1_{\Lambda},$$
on $\Lambda$, and the same relation clearly holds on $\Omega \backslash \Lambda$ since there $b_{-} \equiv 0$. Inserting into (6.36) we obtain
$$\Delta_{p, f} \varphi_{0}+a \varphi_{0}^{p-1}-b F\left(\varphi_{0}\right) \leq 0 \quad \text { on } \Omega,$$
that is, $\varphi_{0}$ is a supersolution for the problem
$$\left\{\begin{array}{l}
\Delta_{p, f} u_{\Omega}+a u_{\Omega}^{p-1}-b F\left(u_{\Omega}\right)=0 \quad \text { on } \Omega, \\
u_{\Omega}=\varepsilon \quad \text { on } \partial \Omega .
\end{array}\right.$$
On the other hand, $\varphi_{\infty}$ is a subsolution for (6.42), and the subsolution-supersolution method (see [25], Theorem 4.14 page 272) gives the existence of $u_{\Omega}$ solving (6.42), satisfying
$$\varphi_{\infty} \leq u_{\Omega} \leq \varphi_{0} \leq C_{\Lambda}(\varepsilon),$$
and, by (6.37),
$$u_{\Omega} \geq \bar{C}_{\Lambda}(\varepsilon) \quad \text { on } \Lambda .$$
Indeed, in our setting we can describe a simple iteration scheme to produce $u_{\Omega}$ : set $V_{0}=a+W 1_{\Lambda}$. For $n \geq 1$, we inductively define $\varphi_{n} \in C^{1, \mu}(\bar{\Omega})$ as the positive solution of
$$\begin{cases}\Delta_{p, f} \varphi_{n}+V_{n} \varphi_{n}^{p-1}-b_{+} F\left(\varphi_{n}\right)=0 & \text { on } \Omega, \\ \varphi_{n}=\varepsilon & \text { on } \partial \Omega\end{cases}$$
where
$$V_{n} \doteq a+b_{-}\left(\frac{F\left(\varphi_{n-1}\right)}{\varphi_{n-1}^{p-1}}\right) .$$
We claim that each $\varphi_{n}$ exists and that $\left\{\varphi_{n}\right\}$ is a non-increasing sequence bounded below by $\varphi_{\infty}$. Indeed, by (6.41), $V_{1} \leq V_{0}$ and so $\lambda_{V_{1}}(\Omega)>0$, which ensures the existence of $\varphi_{1}$ by Proposition 6.1. Moreover, $\varphi_{1}$ solves
$$\begin{cases}\Delta_{p, f} \varphi_{1}+V_{0} \varphi_{1}^{p-1}-b_{+} F\left(\varphi_{1}\right) \geq 0 & \text { on } \Omega ; \\ \varphi_{1}=\varepsilon & \text { on } \partial \Omega,\end{cases}$$
whence by comparison $\varphi_{1} \leq \varphi_{0}$ on $\Omega$. Now, this last inequality (and the monotonicity of $\left.F(t) / t^{p-1}\right)$ gives $V_{2} \leq V_{1}$, so that $\lambda_{V_{2}}(\Omega)>0$ and $\left(P_{2}\right)$ admits a unique positive solution $\varphi_{2}$. Again from $V_{2} \leq V_{1}, \varphi_{2}$ turns out to be a subsolution of $\left(P_{1}\right)$, hence $\varphi_{2} \leq \varphi_{1}$ by comparison. Repeating the argument above shows the monotonicity of $\left\{\varphi_{n}\right\}$. The positivity of $\varphi_{n-1}$ ensures that $V_{n} \geq V_{\infty}$, so by comparison $\varphi_{n} \geq \varphi_{\infty}$ for each $n$. The inequalities $a \leq V_{n} \leq V$ and $\varphi_{\infty} \leq \varphi_{n} \leq \varphi_{0}$ for each $n$ then guarantee, via Theorem 3.1 (2), that there exists $\mu \in(0,1)$ such that the $C^{1, \mu}$-norm of $\varphi_{n}$ on $\Omega$ is uniformly bounded. Therefore, a subsequence of $\left\{\varphi_{n_{k}}\right\}_{k} \subset\left\{\varphi_{n}\right\}_{n}$ converges in the $C^{1}$-norm, as $k \rightarrow+\infty$, to some non-negative $v_{\Omega} \in C^{1}(\bar{\Omega})$, and since $\left\{\varphi_{n}\right\}$ is a non-increasing sequence the whole $\left\{\varphi_{n}\right\}$ converges to $v_{\Omega}$ uniformly. By letting $k \rightarrow+\infty$ in the weak definition of $\left(P_{n}\right)$ along the subsequence $\left\{n_{k}\right\}$, we deduce that $v_{\Omega}$ is a weak solution of (6.42). Now, we choose an exhaustion $\Omega_{j}$, and let $u_{j}=u_{\Omega_{j}}$ be the solution of (6.42) on $\Omega_{j}$ constructed above. Note that
$$\varphi_{\infty, j} \leq u_{j} \leq C_{\Lambda}(\varepsilon) \text { on } \Omega_{j}, \quad u_{j} \geq \bar{C}_{\Lambda}(\varepsilon) \text { on } \Lambda .$$
where $\varphi_{\infty, j}$ solves (6.35) on $\Omega_{j}$. Hence, by local elliptic estimates the sequence $\left\{u_{j}\right\}$ subconverges to some global solution $u \geq 0$ of (6.31) on the whole $M$, satisfying
$$u \leq C_{\Lambda}(\varepsilon) \text { on } M, \quad u \geq \bar{C}_{\Lambda}(\varepsilon) \text { on } \Lambda .$$
By Harnack inequality, $u>0$ on $M$, and we have proved the first part of our theorem. The final step is to guarantee that, when $a \asymp b_{+}, \inf _{M} u>0$.

This will be accomplished by proving corresponding lower bounds for $\varphi_{\infty, j}$. Up to reducing $\theta$, we can suppose that
$$a-\theta b_{+} \geq 0$$
outside some compact set. Using the assumption that $F(t) / t^{p-1} \rightarrow 0$ as $t \rightarrow 0$, fix $\alpha \in(0, \varepsilon)$ small enough that
$$\frac{F(t)}{t^{p-1}} \leq \theta \quad \text { for } t \in[0, \alpha] .$$
Inspecting problem (6.35) and noting that $\alpha<\varepsilon$, we deduce that on the subset $U_{j} \doteq$ $\left\{\varphi_{\infty, j}<\alpha\right\} \Subset \Omega_{j}$ the function $\varphi_{\infty, j}$ solves $\Delta_{p, f} \varphi_{\infty, j}+\left(a-\theta b_{+}\right) \varphi_{\infty, j}^{p-1} \leq 0$, hence in particular
$$\begin{cases}\Delta_{p, f} \varphi_{\infty, j}-\left(a-\theta b_{+}\right)_{-} \varphi_{\infty, j}^{p-1} \leq 0 & \text { on } U_{j} \\ \varphi_{\infty, j}=\alpha & \text { on } \partial U_{j}\end{cases}$$
In view of the boundary regularity requirements to apply Proposition 3.3, we fix a smooth open set $S_{j}$ satisfying
$$\left\{x: \varphi_{\infty, j} \leq \alpha / 2\right\} \Subset S_{j} \Subset U_{j},$$
so that
$$\begin{cases}\Delta_{p, f} \varphi_{\infty, j}-\left(a-\theta b_{+}\right)_{-} \varphi_{\infty, j}^{p-1} \leq 0 & \text { on } S_{j} \\ \varphi_{\infty, j} \geq \frac{\alpha}{2} & \text { on } \partial S_{j}\end{cases}$$
Next, we use the fact that $V \doteq-\left(a(x)-\theta b_{+}(x)\right)_{-}$is compactly supported and $Q_{V}$ is subcritical on $M$ (being $Q_{0}$ subcritical by assumption, and $V \leq 0$ ): by Proposition 6.1, there exists $g \in C_{\text {loc }}^{1, \mu}(M)$ solution of
$$\left\{\begin{array}{l}
\Delta_{p, f} g-\left(a-\theta b_{+}\right)_{-} g^{p-1}=0 \quad \text { on } M, \\
0<\inf _{M} g \leq\|g\|_{L^{\infty}(M)}<+\infty .
\end{array}\right.$$
Rescaling $g$ by multiplying by a positive constant we can assume that
$$0<\inf _{M} g \leq \sup _{M} g \leq \frac{\alpha}{2} .$$
Comparing (6.48) and (6.49) on $S_{j}$, by Proposition 3.3 we infer that $\varphi_{\infty, j} \geq g$ on $S_{j}$, and thus by (6.50)
$$u_{j} \geq \varphi_{\infty, j} \geq \min \left\{\frac{\alpha}{2}, g\right\}=g \quad \text { on } \Omega_{j}$$
Passing to the limit, we finally get
$$u(x) \geq g(x) \text { on } M,$$
and $\inf _{M} u>0$ follows since $\inf _{M} g>0$. \(\square\)

In the proof of the above result, the parameter $\varepsilon$ plays no role. However, a judicious choice of $\varepsilon$ is crucial in the following proof of Theorem 2.2.

Theorem 6.2. Let $M^{m}$ be a Riemannian manifold, $f \in C^{\infty}(M)$ and $p \in(1,+\infty)$. Suppose that $Q_{0}$ is subcritical on $M$ and let $a \in L_{\text {loc }}^{\infty}(M)$ be such that $Q_{a}$ is subcritical on $M$. Consider $b \in L_{\text {loc }}^{\infty}(M)$, and assume
i) $b_{-}(x)$ has compact support;
$\left.i i^{\prime}\right) a(x) \leq 0$ outside a compact set;
$\left.i i i^{\prime}\right) a(x), b(x) \in L^{1}\left(M, \mathrm{~d} \mu_{f}\right)$.
Fix a nonlinearity $F(t)$ satisfying (2.6). Then, there exists a sequence $\left\{u_{k}\right\} \subset C_{\text {loc }}^{1, \mu}(M)$ of distinct weak solutions of
$$\left\{\begin{array}{l}
\Delta_{p, f} u_{k}+a(x) u_{k}^{p-1}-b(x) F\left(u_{k}\right)=0 \quad \text { on } M \\
0<u_{k} \leq\left\|u_{k}\right\|_{L^{\infty}(M)}<+\infty,
\end{array}\right.$$
such that $\left\|u_{k}\right\|_{L^{\infty}(M)} \rightarrow 0$ as $k \rightarrow+\infty$. If we replace $i i^{\prime}$ ) and $i i i^{\prime}$ ) by the stronger condition
$$\left.i v^{\prime}\right) \quad a(x), b(x) \quad \text { have compact support },$$
then each $u_{k}$ also satisfies $\inf _{M} u_{k}>0$.
Proof. We first observe that our set of assumptions on $a$ and $b$ is a special case of the one in Theorem 6.1, namely we just include the requirement that $a \leq 0$ outside some compact set. Hence, the constructions in the previous theorem hold as well in our setting, and we will refer to the proof of Theorem 6.1 also for relevant definitions.

Up to enlarging $\Lambda$ we can assume that $a \leq 0$ on $M \backslash \Lambda$. Let $\Omega$ satisfy $\Lambda^{\prime} \subset \Omega$. By Lemma 6.3 applied with $A=a+W 1_{\Lambda}, B \equiv 0$ there exists a uniform constant $\hat{C}$, independent of $\Omega$, such that the solution $\psi$ of
$$\begin{cases}\Delta_{p, f} \psi+\left(a+W 1_{\Lambda}\right) \psi^{p-1}=0 & \text { on } \Omega, \\ \psi=1 & \text { on } \partial \Omega\end{cases}$$
satisfies $\psi \leq \hat{C}$ on $\Omega$. By comparison and recalling our definition of $\varphi_{0}$ in (6.36), we get $\varphi_{0} \leq \varepsilon \psi$. Therefore, by our definition of $C_{\Lambda}(\varepsilon)$,
$$C_{\Lambda}(\varepsilon) \leq \varepsilon \hat{C} \rightarrow 0 \quad \text { as } \varepsilon \rightarrow 0 .$$
Combining (6.53), the monotonicity of $C_{\Lambda}(\varepsilon)$ and property $F(t) / t^{p-1} \rightarrow 0$ as $t \rightarrow 0$ in (2.6), we deduce that, given any $b$ with $b_{-}$compactly supported, there exists $\varepsilon_{0}$ sufficiently small such that
$$b_{-} \leq\left(\min _{\bar{\Lambda}} W\right)\left[\frac{C_{\Lambda}(\varepsilon)^{p-1}}{F\left(C_{\Lambda}(\varepsilon)\right)}\right] \quad \text { for each } \varepsilon \leq \varepsilon_{0} .$$
Fix such $\varepsilon_{0}$ and follow the arguments in Theorem 6.1 with $\varepsilon=\varepsilon_{0}$. Note that, as in (6.41),
$$b_{-}(x)\left(\frac{F\left(\varphi_{0}(x)\right)}{\varphi_{0}(x)^{p-1}}\right) \leq b_{-}(x)\left[\frac{F\left(C_{\Lambda}(\varepsilon)\right)}{C_{\Lambda}(\varepsilon)^{p-1}}\right] \leq 1_{\Lambda}(x)\left(\min _{\bar{\Lambda}} W\right) \leq W(x) 1_{\Lambda}(x),$$
which is the key step to produce the local solutions of (6.42), and now it does not require (6.30). Proceeding with the construction, we get a solution $u_{0}$ of
$$\left\{\begin{array}{l}
\Delta_{p, f} u_{0}+a(x) u_{0}^{p-1}-b(x) F\left(u_{0}\right)=0 \quad \text { on } M, \\
0<u_{0} \leq C_{\Lambda}\left(\varepsilon_{0}\right) \quad \text { on } M,
\end{array}\right.$$
and $\inf _{M} u_{0}>0$ when $\left(i v^{\prime}\right)$ holds. Next, choose $\varepsilon_{1}<\varepsilon_{0}$ small enough that
$$C_{\Lambda}\left(\varepsilon_{1}\right)<\min _{\bar{\Lambda}} u_{0} .$$
Proceeding as above with $\varepsilon_{1}$ replacing $\varepsilon_{0}$ we get a solution $u_{1}$ of
$$\left\{\begin{array}{l}
\Delta_{p, f} u_{1}+a(x) u_{1}^{p-1}-b(x) F\left(u_{1}\right)=0 \quad \text { on } M, \\
0<u_{1} \leq C_{\Lambda}\left(\varepsilon_{1}\right) \quad \text { on } M,
\end{array}\right.$$
and $\inf _{M} u_{1}>0$ when $\left(i v^{\prime}\right)$ is in force. By our choice of $\varepsilon_{1}, u_{1}<u$ on $\Lambda$, thus in particular the two solutions are different. We can now repeat the procedure inductively by choosing, at each step, $\varepsilon_{k}<\varepsilon_{k-1}$ such that
$$C_{\Lambda}\left(\varepsilon_{k}\right)<\min _{\bar{\Lambda}} u_{k-1},$$
obtaining a solution $u_{k}$ of
$$\Delta_{p, f} u_{k}+a(x) u_{k}^{p-1}-b(x) F\left(u_{k}\right)=0 \quad \text { on } M$$
satisfying
$$0<u_{k} \leq C_{\Lambda}\left(\varepsilon_{k}\right) \text { on } M, \quad u_{k}<u_{k-1} \quad \text { on } \Lambda, \quad \inf _{M} u_{k}>0 \quad \text { when }\left(i v^{\prime}\right) \text { holds. }$$
By construction, $C_{\Lambda}\left(\varepsilon_{k}\right) \rightarrow 0$ as $k \rightarrow+\infty$, hence $\left\{u_{k}\right\}$ is the desired sequence. \(\square\)

Remark 6.2. The key point that allows, in Theorem 6.2. to get rid of (6.30) is the validity of the asymptotic relation
$$C_{\Lambda}(\varepsilon) \rightarrow 0^{+} \quad \text { as } \varepsilon \rightarrow 0^{+},$$
which is granted via the presence of an uniform $L^{\infty}$-bound for solutions $\psi$ of (6.52). For general $a, b$, just satisfying the assumptions of Proposition 6.1, (6.58) may not hold. As an example, consider the hyperbolic space $\mathbb{H}^{m}$ of sectional curvature -1. For each $\tau \geq 1$, the radial functions
$$u_{\tau}(x)=\left(2 \cosh ^{2}\left(\frac{r(x)}{2}\right)\right)^{-\frac{m-2}{2}} \beta_{\tau}\left(\tanh \left(\frac{r(x)}{2}\right)\right),$$
where
$$\beta_{\tau}(t)=\frac{\left(\tau^{2}-t^{2}\right)^{-\frac{m-2}{2}}}{m(m-2) \tau^{2}}$$
are all solutions of
$$\Delta u+\frac{m(m-2)}{4} u-u^{\frac{m+2}{m-2}}=0 \quad \text { on } \mathbb{H}^{m} .$$
Moreover, they are decreasing functions of $r(x)$, and the sequence $\left\{u_{\tau}\right\}$ is monotone decreasing. For each $\varepsilon>0$, consider $\Omega=u_{1}^{-1}\{(\varepsilon,+\infty)\}$. Then, for $\varepsilon$ small enough in such a way that $\Omega \neq \emptyset$, by the definition of $C_{\Lambda}(\varepsilon)$ in (6.39) we deduce
$$C_{\Lambda}(\varepsilon) \geq\left\|u_{1}\right\|_{L^{\infty}(\Omega)}=u_{1}(0)=\frac{2^{-\frac{m-2}{2}}}{m(m-2)},$$
preventing from the validity of (6.58).

We briefly comment on the sharpness of the subcriticality assumption for $Q_{a}$ in Theorem 2.1, and for this reason we now state a result that improves on a theorem in [48]. First of all, we extend definition (3.8) to arbitrary subsets $\Lambda \subset M$, that is, we define the fundamental tone $\lambda_{V}(\Lambda)$ by setting
$$\lambda_{V}(\Lambda)=\sup \lambda_{V}(\Omega)$$
where the supremum is taken over all open subsets $\Omega \subset M$ with smooth boundary such that $\bar{\Lambda} \subset \Omega$.

Proposition 6.2. Let $(M,\langle\rangle$,$) be a Riemannian manifold f \in C^{\infty}(M), p \in(1, \infty)$ and let $a(x) \in L_{\text {loc }}^{\infty}(M), b(x) \in C^{0}(M)$. Define
$$B_{0} \doteq\{x \in M: b(x) \leq 0\},$$
Let $\Omega$ be an open domain containing $\bar{B}_{0}$ and such that there exists a positive, bounded solution $u \in C^{0}(\bar{\Omega}) \cap W_{\text {loc }}^{1, p}(\Omega)$ of
$$\Delta_{p, f} u+a(x) u^{p-1}-b(x) F(u) \leq 0 \quad \text { on } \Omega,$$
for some nonlinearity $F(t)$ that satisfies (2.6). Then
$$\lambda_{a}\left(B_{0}\right) \geq 0 .$$

Remark 6.3. Let us consider the case $p=2, f \equiv 0$. The first Dirichlet eigenvalue of the Laplacian on a geodesic ball $B_{r}$ grows like $r^{-2}$ as $r \rightarrow 0^{+}$, thus $\lambda_{a}\left(B_{r}\right)>0$ provided $r$ is sufficiently small and one may think that condition (6.61) expresses the fact that $b_{-}$is, loosely speaking, small in a spectral sense.

Proof. Let $u$ be as above and by contradiction assume that $\lambda_{a}\left(B_{0}\right) \doteq \lambda<0$. Then, by definition (6.59) we can find a sequence $\left\{U_{i}\right\}$ of open sets with smooth boundaries such that
$$\bar{B}_{0} \subset U_{i} \subset \bar{U}_{i} \subset \Omega, \quad \lambda_{a}\left(U_{i}\right) \rightarrow \lambda \quad \text { as } i \rightarrow+\infty .$$
Take a nested sequence $\left\{V_{i}\right\}$ of smooth open sets shrinking to $B_{0}$ such that:
$$V_{i} \subset\left\{x: b(x)<\frac{1}{i}\right\}, \quad \bar{B}_{0} \subset V_{i+1} \subset \bar{V}_{i+1} \subset V_{i} \subset \Omega, \quad \bigcap_{i=1}^{+\infty} V_{i}=\bar{B}_{0} .$$
Then, up to replacing $U_{i}$ with $V_{i} \cap U_{i}$ and smoothing corners, by the monotonicity of eigenvalues we can further suppose that $\left\{U_{i}\right\}$ satisfies
$$\bigcap_{i=1}^{+\infty} U_{i}=\bar{B}_{0}, \quad b<\frac{1}{i} \text { on } U_{i} .$$
By the definition of $\lambda_{a}\left(U_{i}\right)$, there exists a smooth, relatively compact open set $\Omega_{i} \Subset$ $U_{i}$ for which $\lambda_{i} \doteq \lambda_{a}\left(\Omega_{i}\right) \leq \lambda_{a}\left(U_{i}\right)+1 / i$, so that clearly $\lambda_{i} \rightarrow \lambda$ as $i$ diverges. Corresponding to $\lambda_{i}$ there exists a positive eigenfunction $\varphi_{i} \in C^{1, \mu}\left(\bar{\Omega}_{i}\right)$ satisfying
$$\begin{cases}Q_{a}^{\prime}\left(\varphi_{i}\right)=\lambda_{i}\left|\varphi_{i}\right|^{p-2} \varphi_{i} & \text { on } \Omega_{i} \\ \varphi_{i}=0 & \text { on } \partial \Omega_{i} .\end{cases}$$
Setting $h=\log u$ using (3.14) and (6.60) we see that $h$ solves
$$\Delta_{p, f} h \leq-a(x)+b(x) \frac{F(u)}{u^{p-1}}-(p-1)|\nabla h|^{p} .$$

Integrating on $\Omega_{i}$ against $\varphi_{i}^{p}$ and proceeding as in the proof of $\left.\left.i\right) \Rightarrow i i i\right)$ in Proposition 3.4 we obtain
$$\int_{\Omega_{i}} a(x) \varphi_{i}^{p} \mathrm{~d} \mu_{f}-\int_{\Omega_{i}} b(x) \frac{F(u)}{u^{p-1}} \varphi_{i}^{p} \mathrm{~d} \mu_{f} \leq \int_{\Omega_{i}}\left|\nabla \varphi_{i}\right|^{p} \mathrm{~d} \mu_{f} .$$
Now, since the $\varphi_{i}$ 's are eigenfunctions, $p Q_{a}(\varphi)=\lambda_{i}\left\|\varphi_{i}\right\|_{L^{p}\left(\Omega_{i}, \mathrm{~d} \mu_{f}\right)}^{p}$. Therefore, inserting into the above, observing that $b<1 / i$ on $\Omega_{i}$ and using the monotonicity of $f(t) / t^{p-1}$ we deduce
$$0 \geq \int_{\Omega_{i}}\left[-\lambda_{i}-b(x) \frac{F(u)}{u^{p-1}}\right] \varphi_{i}^{p} \mathrm{~d} \mu_{f} \geq \int_{\Omega_{i}}\left[-\lambda_{i}-\frac{F\left(\|u\|_{L^{\infty}(\Omega)}\right)}{i\|u\|_{L^{\infty}(\Omega)}^{p-1}}\right] \varphi_{i}^{p} \mathrm{~d} \mu_{f} .$$
Concluding, as $\lambda_{i} \rightarrow \lambda<0$, taking $i$ sufficiently large the previous inequality yields the desired contradiction. \(\square\)

In view of Proposition 6.2, and since we made no assumptions on the size of the set $\{x: b(x)=0\}$ in Theorem 2.1, the existence of a bounded solution of (2.12) on $M$ when $b$ changes sign requires at least that $Q_{a} \geq 0$ on the whole $M$. We feel interesting to investigate the validity of Theorem 2.1 when assumption $i$ ) is replaced with the requirement that $Q_{a}$ be non-negative and with a ground state.

Remark 6.4. We conclude this section with a remark on the role of (2.11) in Theorem 2.1. that is, $\left\|b_{-}\right\|_{L^{\infty}(M)} \leq \delta$. Denote with $B_{0}$ the relatively compact set $\{x: b(x)<0\}$, and for each $\varepsilon \in(0,1)$ choose a smooth relatively compact set $\Omega_{\varepsilon} \subset\left\{x: b_{-}(x) \geq\right.$ $\left.(1-\varepsilon)\left\|b_{-}\right\|_{L^{\infty}(M)}\right\}$. Then we let $\varphi_{\varepsilon}$ be the positive eigenfunction of
$$\left\{\begin{array}{l}
Q_{a}^{\prime}\left(\varphi_{\varepsilon}\right)=\lambda_{a}\left(\Omega_{\varepsilon}\right) \varphi_{\epsilon}^{p-1} \quad \text { on } \Omega_{\varepsilon} \\
\varphi_{\varepsilon}=0 \quad \text { on } \partial \Omega_{\varepsilon}, \quad \varphi_{\varepsilon}>0 \quad \text { on } \Omega_{\varepsilon} .
\end{array}\right.$$
Note that $\lambda_{a}\left(\Omega_{\varepsilon}\right)>0$ by assumption. Reasoning as in Proposition 6.2 to get (6.63) we obtain
$$\lambda_{a}\left(\Omega_{\varepsilon}\right)\left\|\varphi_{\varepsilon}\right\|_{L^{p}\left(\Omega_{\varepsilon}\right)}^{p} \geq \int_{\Omega_{\varepsilon}} b_{-} \frac{F(u)}{u^{p-1}} \varphi_{\varepsilon}^{p} \mathrm{~d} \mu_{f},$$
hence using the definition of $\Omega_{\varepsilon}$
$$\lambda_{a}\left(\Omega_{\varepsilon}\right)\left\|\varphi_{\varepsilon}\right\|_{L^{p}\left(\Omega_{\varepsilon}\right)}^{p} \geq(1-\varepsilon)\left\|b_{-}\right\|_{L^{\infty}(M)}\left[\inf _{B_{0}} \frac{F(u)}{u^{p-1}}\right]\left\|\varphi_{\varepsilon}\right\|_{L^{p}\left(\Omega_{\varepsilon}\right)}^{p}$$
in other words
$$\left\|b_{-}\right\|_{L^{\infty}(M)}\left[\inf _{B_{0}} \frac{F(u)}{u^{p-1}}\right] \leq \inf _{\varepsilon \in(0,1)} \frac{\lambda_{a}\left(\Omega_{\varepsilon}\right)}{1-\varepsilon} .$$
The above inequality helps to understand the relationship between the $L^{\infty}$-norm of the negative part of $b$ and a lower bound for $u$ on $B_{0}$. In particular, in view of the relation $F(t) / t^{p-1} \rightarrow 0$ as $t \rightarrow 0$ in (2.6), a larger size of $b_{-}$forces $u$ to squeeze towards zero on $B_{0}$.

\section*{7. Proofs of our geometric corollaries, and concluding comments}

In this section, we prove Theorems 2.3, 1.5, 1.6 and their Corollaries 1.1 and 1.2.

Proof of Theorem 2.3. Taking into account that the conformal factor $u$ in the deformation
$$\widetilde{\langle,\rangle}=u^{\frac{4}{m-2}}\langle,\rangle$$
shall satisfy (1.2), the theorem follows immediately from Theorems 2.1 and 2.2. When the two-sided bound
$$C^{-1}\langle,\rangle \leq \widetilde{\langle,\rangle} \leq C\langle,\rangle$$
holds, $(M, \widetilde{\langle,\rangle})$ is complete if and only if $(M,\langle\rangle$,$) is so. Furthermore, because of (7.1)$ since $\langle$,$\rangle is non-parabolic the same holds for \langle$,$\rangle . Indeed, it is easy to see that (7.1)$ induces a similar two-sided bound between the capacities cap and cap of the Laplace-Beltrami operators of the two metrics (with, say, supersolution $g=1$ ), whence the preservation of parabolicity follows from Theorem 4.1. This concludes the proof. \(\square\)

Proof of Theorem 1.5. It follows directly from case (II) of Theorem 2.3; it is enough to observe that, if $s(x) \geq 0$ on the whole $M$ and $M$ is non-parabolic (i.e., - $\Delta$ is subcritical), then the conformal Laplacian $L_{\langle,\rangle}$is subcritical. \(\square\)

Proof of Corollary 1.1. We begin with performing a "reduction" argument that goes back to the original works of Schoen-Yau on the positive mass theorem, see [47], pp. 82-83. Via a cut-off procedure and a careful analysis of Schrödinger operators on weighted spaces, they showed that there exists a conformal deformation
$$\langle,\rangle_{1}=u_{1}^{\frac{4}{m-2}}\langle,\rangle$$
of the original asymptotically flat metric in such a way that $\left(M,\langle,\rangle_{1}\right)$ is still asymptotically flat and has zero scalar curvature outside a compact set. Moreover, $\langle,\rangle_{1}$ is uniformly equivalent to $\langle$,$\rangle (actually much more is true, but this is enough for our$ purposes). Next, by the very definition of asymptotic flatness, the metric $\langle,\rangle_{1}$ on each end $U_{j}$ with respect to the compact set $K$ is bi-Lipschitz equivalent to the Euclidean one on $\mathbb{R}^{m} \backslash B_{r}(0)$, hence proceeding as in the proof of Theorem 2.3 we deduce that $\left(M,\langle,\rangle_{1}\right)$ is non-parabolic. Consequently, since $\langle,\rangle_{1}$ has non-negative scalar curvature, the conformal Laplacian $L_{\langle,\rangle_{1}}$ is subcritical. Applying previous Theorem 1.5 to the background manifold $\left(M,\langle,\rangle_{1}\right)$, we get the existence of a family of conformal deformations to scalar curvature $\widetilde{s}(x)$ which, after composing with the deformation (7.2), concludes the proof of the corollary. \(\square\)

Proof of Theorem 1.6. It follows directly from $(I)$ of Theorem 2.3. Note that, according to Remark 4.6, $L_{\langle,\rangle}$is subcritical if and only if it admits a positive Green kernel. \(\square\)

Proof of Corollary 1.2. Condition $K \leq-\kappa^{2}$ implies, via Theorem 5.1, that the Hardy inequality
$$\int_{M}(\chi \circ r) \varphi^{2} \mathrm{~d} x \leq \int_{M}|\nabla \varphi|^{2} \mathrm{~d} x,$$
holds for each $\varphi \in \operatorname{Lip}_{c}(M)$, where
$$\chi(r)=\frac{1}{4}\left(g_{\kappa}(r)^{m-1} \int_{r}^{+\infty} \frac{\mathrm{d} s}{g_{\kappa}(s)^{m-1}}\right)^{-2} .$$
Now, since by (5.25) the Hardy weight satisfies
$$\chi(r) \geq \frac{(m-1)^{2} \kappa^{2}}{4} \quad \text { on } \mathbb{R}^{+},$$
using assumption (1.24) we deduce that
$$-\frac{s(x)}{c_{m}}=-\frac{m-2}{4(m-1)} s(x) \leq \frac{(m-1)^{2} \kappa^{2}}{4} \leq \chi(r(x)),$$
thus the conformal Laplacian $L_{\langle,\rangle}=-\Delta+s / c_{m}$ is subcritical by Proposition 4.5 (clearly, $-s / c_{m} \not \equiv(\chi \circ r)$ since this latter tends to infinity at $o$ ). Now, if (1.25) holds outside of a compact set, assumption i) of Theorem 2.3 is met. Tracing $K \leq-\kappa^{2}$ we deduce
$$s(x) \leq-m(m-1) \kappa^{2},$$
which coupled with (1.24) and (1.25) implies $s(x) \asymp \widetilde{s}(x)$ as $x$ diverges. Applying Theorem 1.6 we eventually have the desired conformal deformation to a uniformly equivalent metric $\langle$,$\rangle .$ \(\square\)

We conclude with a couple of remarks. In the Introduction, the prototype cases of Euclidean and hyperbolic space helped us to have a picture of the variety of phenomena concerning the prescribed curvature problem. We have seen that the uniqueness of the conformal deformation in Theorem 2.1 fails to hold for sign-changing $\widetilde{s}(x)$, and that fastly decaying solutions coexist with solutions bounded from below and above by positive constants. In particular, assumptions like (1.25) do not imply a control of the decay of the conformal factor from both sides by two comparable quantities. However, when $\widetilde{s}<0$ on the whole $M$, something more precise can be said about uniqueness and asymptotic behaviour of solutions $u$ of the Yamabe equation (1.2). As above, consider the prototype case of $\mathbb{H}_{\kappa}^{m}$, and suppose that
$$-C_{1} \leq \widetilde{s}(x) \leq-C_{2}<0 \quad \text { on } \mathbb{H}_{\kappa}^{m} .$$
By Theorem 3.4 in [74] with the choice $\beta=0$ (or even by Theorem 4 in [8]), assumption (7.3) guarantees that the conformal deformation given in Aviles-McOwen's Theorem 1.3 and in Corollary 1.2 is the unique conformal deformation realizing $\widetilde{s}(x)$ and such that the conformal factor satisfies $\inf _{\mathbb{H}_{\kappa}^{m}} u>0$. Moreover, by [71, 61] (a simpler form can also be found in Theorem 2.3 of [74]), in the same assumptions each solution of (1.2) satisfies $\sup _{\mathbb{H}_{\kappa}^{m}} u<+\infty$. On the other hand, since $\widetilde{s}<0$ on $\mathbb{H}_{\kappa}^{m}$, estimates from below for positive solutions of the Yamabe type equation (2.1) have been provided in [74]. Applying Theorem 2.4 of [74] with the choices
$$m>4, \quad \delta=0, \quad \beta=-1-\epsilon, \quad \alpha<0 \text { arbitrary, } \quad \sigma=\frac{m+2}{m-2}, \quad \gamma=\frac{m-2}{2} H>H$$
with $\epsilon>0$, we deduce that any solution $u$ of (1.2) satisfies
$$u(x) \geq C e^{-\frac{m-2}{2} \kappa r(x)} \quad \text { on } \mathbb{H}_{\kappa}^{m},$$
for some $C>0$. Indeed, the right-hand side in (7.4) is exactly the asymptotic decay of the solutions that create the conformally deformed metrics in Theorem 1.4, and in fact it is also the decay of a radial solution of $L_{\langle,\rangle} u=0$ on $\mathbb{H}_{\kappa}^{m}$. In summary, when (7.3) holds, the decay of the solutions $\left\{u_{j}\right\}$ in Theorem 1.4 is the minimal one that a solution of the Yamabe equation with (7.3) in force can have (if $m>4$ ), while the function $u$ produced in Corollary 1.2 (we call it $\hat{u}$ ) is the unique solution which is bounded below by a positive constant, and indeed it also has the maximal possible order at infinity, as each solution shall be bounded above by a constant. This intriguing scenario is
enriched by the fact that, by Theorem 1.1 in [71], the Yamabe equation on $\mathbb{H}_{\kappa}^{m}$ also admits a solution $u_{c}$ giving rise to a complete metric $\widetilde{\langle,\rangle}$ whenever
$$\widetilde{s}<0 \quad \text { on } M, \text { and } \quad \widetilde{s}(x) \geq-C r(x)^{2} \quad \text { as } r \rightarrow+\infty,$$
for some $C>0$. It is still not clear whether $u_{c}$ coincides with $\hat{u}$ or not, or even if (7.5) ensures the existence of a whole infinite family of solutions, distinct from $\left\{u_{j}\right\}$ and $\hat{u}$, giving rise to complete metrics.

Remark 7.1. Based on the hints in [72], we conjecture that there exists a conformal deformation of the hyperbolic metric that gives rise to a complete metric of scalar curvature $\widetilde{s}(x)$ whenever $|\widetilde{s}(x)| \leq C r(x)^{2}$, where $r(x)$ is the distance from a fixed origin of $\mathbb{H}_{\kappa}^{m}$ and $C>0$. See also [13] for some comments.

\section*{Appendix: the obstacle problem and the pasting lemma}

The aim of this section is to present a proof of the pasting Lemma 3.1. The argument is divided in three steps. First, observe that our assumptions in Lemma 3.1 imply $\lambda_{V}\left(\Omega_{2}\right) \geq 0$. Therefore, the obstacle problem that we shall consider below is solvable on relatively compact open subsets of $\Omega_{2}$. Secondly, the minimizing properties of its solutions yield a quick proof of the fact that the minimum of two positive supersolutions is still a supersolution. Finally we obtain Lemma 3.1 by refining the argument used in the second step. The idea of the proof is close to that in Section 3 of [53]. Hereafter, each $W^{1, p}$-norm is intended to be with respect to the measure $\mathrm{d} \mu_{f}$

Let $\Omega \Subset M$ be a relatively compact, open subset and $V \in L^{\infty}(\Omega)$. Given $\psi$ measurable and $\theta \in W^{1, p}(\Omega)$ such that $\psi \leq \theta$ a.e. on $\Omega$, we define the non-empty, closed, convex set
$$\mathcal{K}_{\psi, \theta} \doteq\left\{\varphi \in W^{1, p}(\Omega) \mid \varphi \geq \psi \text { a.e. and } \varphi-\theta \in W_{0}^{1, p}(\Omega)\right\} .$$
We say that $u \in \mathcal{K}_{\psi, \theta}$ solves the obstacle problem if
$$Q_{V}^{\prime}(u)[\varphi-u] \geq 0 \quad \text { for each } \varphi \in \mathcal{K}_{\psi, \theta},$$
that is, weakly,
$$\int_{\Omega}|\nabla u|^{p-2}\langle\nabla u, \nabla(\varphi-u)\rangle \mathrm{d} \mu_{f}-\int_{\Omega} V|u|^{p-2} u(\varphi-u) \mathrm{d} \mu_{f} \geq 0$$
Note that, for each non-negative $\widehat{\varphi} \in C_{c}^{1}(\Omega)$, the function $\varphi=u+\widehat{\varphi} \in \mathcal{K}_{\psi, \theta}$, and putting into (7.7) we get that $u$ solving (7.7) satisfies $Q_{V}^{\prime}(u) \geq 0$, that is, $u$ is a supersolution. We address the solvability of the obstacle problem in the next

Theorem 7.1. Let $M$ be a Riemannian manifold, $f \in C^{\infty}(M), p \in(1,+\infty)$ and $V \in L_{\mathrm{loc}}^{\infty}(M)$. Let $\Omega \Subset M$ be a relatively compact open set with Lipschitz boundary for which $\lambda_{V}(\Omega)>0$. Suppose that the obstacle $\psi$ satisfies $0 \leq \psi \leq \theta$ a.e. on $\Omega$, for some $\theta \in W^{1, p}(\Omega)$. Then, there exists a solution $u \in \mathcal{K}_{\psi, \theta}$ of (7.7).

Proof. We consider the translated set
$$\overline{\mathcal{K}}_{\psi, \theta} \doteq \mathcal{K}_{\psi, \theta}-\theta=\left\{\bar{g}: \bar{g}+\theta \in \mathcal{K}_{\psi, \theta}\right\} \subset W_{0}^{1, p}(\Omega) .$$
Note that, since $\psi \geq 0, \forall \bar{g} \in \overline{\mathcal{K}}_{\psi, \theta}$ we have $\bar{g}+\theta \geq 0$.
We now define the functional $\mathcal{F}: \overline{\mathcal{K}}_{\psi, \theta} \rightarrow W_{0}^{1, p}(\Omega)^{*}$ by setting: $\forall \bar{u} \in \overline{\mathcal{K}}_{\psi, \theta}$ and $\varphi \in W_{0}^{1, p}(\Omega)$,
$$\mathcal{F}(\bar{u})[\varphi] \doteq Q_{V}^{\prime}(\bar{u}+\theta)[\varphi]=\mathcal{A}(\bar{u})[\varphi]-\mathcal{B}(\bar{u})[\varphi]$$
with
$$\mathcal{A}(\bar{u})[\varphi]=\int_{\Omega}|\nabla(\bar{u}+\theta)|^{p-2}\langle\nabla(\bar{u}+\theta), \nabla \varphi\rangle \mathrm{d} \mu_{f}$$
and
$$\mathcal{B}(\bar{u})[\varphi]=\int_{\Omega} V|\bar{u}+\theta|^{p-2}(\bar{u}+\theta) \varphi \mathrm{d} \mu_{f}$$
Clearly, $\bar{u} \in \overline{\mathcal{K}}_{\psi, \theta}$ solves the obstacle problem
$$\mathcal{F}(\bar{u})[\bar{\varphi}-\bar{u}] \geq 0 \quad \forall \bar{\varphi} \in \overline{\mathcal{K}}_{\psi, \theta}$$
if and only if $u=\bar{u}+\theta \in \mathcal{K}_{\psi, \theta}$ is a solution of the obstacle problem (7.7).
According to Theorem 8.2, p. 247 in [51], to solve the obstacle problem it is enough to verify that:
\begin{itemize}
\item[1.] $\mathcal{F}$ is pseudo-monotone on $\overline{\mathcal{K}}_{\psi, \theta}$, that is,
\begin{itemize}
\item[i)]
$$\mathcal{F}:\left(W_{0}^{1, p}(\Omega),\|\cdot\|_{W_{0}^{1, p}(\Omega)}\right) \rightarrow\left(W_{0}^{1, p}(\Omega)^{*},\|\cdot\|_{W_{0}^{1, p}(\Omega)^{*}}\right)$$
is bounded.
\item[ii)] if $u_{i}, u \in \overline{\mathcal{K}}_{\psi, \theta}$ and $u_{i} \rightharpoonup u$ in $\left(W_{0}^{1, p}(\Omega)\right.$, weak $)$ as $i \rightarrow+\infty$ and
$$\limsup _{i \rightarrow+\infty} \mathcal{F}\left(u_{i}\right)\left[u_{i}-u\right] \leq 0$$
then
$$\liminf _{i \rightarrow+\infty} \mathcal{F}\left(u_{i}\right)\left[u_{i}-\varphi\right] \geq \mathcal{F}(u)[u-\varphi] \quad \forall \varphi \in W_{0}^{1, p}(\Omega) .$$
\end{itemize}
\item[2.] $\mathcal{F}$ is coercive on $\overline{\mathcal{K}}_{\psi, \theta}$, that is,
\begin{itemize}
\item[iii)] there exists $\bar{\varphi} \in \overline{\mathcal{K}}_{\psi, \theta}$ for which
$$\frac{\mathcal{F}(\bar{u})[\bar{u}-\bar{\varphi}]}{\|\bar{u}\|_{W_{0}^{1, p}(\Omega)}} \rightarrow+\infty$$
if $\|\bar{u}\|_{W_{0}^{1, p}(\Omega)} \rightarrow+\infty$ with $\bar{u} \in \overline{\mathcal{K}}_{\psi, \theta}$.
\end{itemize}
\end{itemize}
We first address the pseudo-monotonicity of $\mathcal{F}$.
\begin{itemize}
\item[i)] Boundedness follows since, for each $\varphi \in W_{0}^{1, p}(\Omega)$, by Hölder inequality we have
$$|\mathcal{F}(\bar{u})[\varphi]| \leq C\left(1+\|\bar{u}\|_{W^{1, p}(\Omega)}^{p-1}\right)\|\varphi\|_{W^{1, p}(\Omega)}$$
for some constant $C>0$.
\item[ii)] Let $u_{i} \rightharpoonup u$ weakly in $W_{0}^{1, p}(\Omega)$ with $u_{i}, u \in \overline{\mathcal{K}}_{\psi, \theta}$ and suppose (7.11). Since $u_{i} \rightharpoonup u,\left\{u_{i}\right\}$ is bounded in $W_{0}^{1, p}(\Omega)$; since $\partial \Omega$ is Lipschitz, by Rellich-Kondrachov compactness theorem $\left\|u_{i}-u\right\|_{L^{p}(\Omega)} \rightarrow 0$ and almost everywhere. Then, it is easy to see that $\mathcal{B}\left(u_{i}\right)\left[u_{i}-u\right] \rightarrow 0$. Therefore, by (7.11)
$$\limsup _{i} \mathcal{A}\left(u_{i}\right)\left[u_{i}-u\right] \leq 0 .$$
Since $\mathcal{A}$ is a monotone operator and $u_{i} \rightharpoonup u$, from (7.13) we have
$$\begin{aligned}
0 & \leq\left(\mathcal{A}\left(u_{i}\right)-\mathcal{A}(u)\right)\left[u_{i}-u\right]=\mathcal{A}\left(u_{i}\right)\left[u_{i}-u\right]-\mathcal{A}(u)\left[u_{i}-u\right] \\
& =\mathcal{A}\left(u_{i}\right)\left[u_{i}-u\right]+o(1)
\end{aligned}$$
\end{itemize}
as $i \rightarrow+\infty$, and we therefore deduce that $\lim _{i}\left(\mathcal{A}\left(u_{i}\right)-\mathcal{A}(u)\right)\left[u_{i}-u\right]=0$. By Browder lemma, see Lemma 3 in [18], since $\mathcal{A}$ is strictly monotone we obtain that $u_{i} \rightarrow u$ strongly in $W_{0}^{1, p}(\Omega)$. Now we show that $\mathcal{F}$ is sequentially continuous from $\left(W_{0}^{1, p}(\Omega),\|\cdot\|_{W_{0}^{1, p}(\Omega)}\right)$ to $\left(W_{0}^{1, p}(\Omega)^{*}\right.$, weak). Let $u_{i}$ be a sequence in $W_{0}^{1, p}(\Omega)$ which converges strongly to $u$. Up a subsequence we have $\left(u_{k}(x), \nabla u_{k}(x)\right) \rightarrow(u(x), \nabla u(x))$ for a.e. $x \in \Omega$. Set for convenience
$$X_{k}(x)=\nabla\left(u_{k}(x)+\theta(x)\right), \quad X(x)=\nabla(u(x)+\theta(x)) .$$
If $k \rightarrow \infty,\left(X_{k}(x),\left|X_{k}(x)\right|\right) \rightarrow(X(x),|X(x)|)$ for a.e. $x \in \Omega$. If we set $\nabla \varphi=Y$, we have
$$\left.\left(\mathcal{A}\left(u_{k}\right)-\mathcal{A}(u)\right)[\varphi]=\left.\int_{\Omega}\left\langle Y, X_{k}\right| X_{k}\right|^{p-2}-X|X|^{p-2}\right\rangle \mathrm{d} \mu_{f}=(I)+(I I),$$
where
$$\begin{aligned}
(I) & =\int_{\Omega} \frac{\left|X_{k}\right|^{p-2}\left\langle Y, X_{k}\right\rangle}{1+\left|X_{k}\right|^{p-1}}\left[\left|X_{k}\right|^{p-1}-|X|^{p-1}\right] \mathrm{d} \mu_{f} ; \\
(I I) & =\int_{\Omega}\left\langle Y, \frac{\left|X_{k}\right|^{p-2} X_{k}}{1+\left|X_{k}\right|^{p-1}}-\frac{|X|^{p-2} X}{1+|X|^{p-1}}\right\rangle\left(1+|X|^{p-1}\right) \mathrm{d} \mu_{f} .
\end{aligned}$$
Since the integrand in (II) is bounded by $2|Y|\left(1+|X|^{p-1}\right) \in L^{1}(\Omega)$, by Lebesgue theorem
$$(I I) \rightarrow 0 \quad \text { as } k \rightarrow+\infty .$$
We now consider $(I)$. Fix $\epsilon>0$. Then, by Egoroff theorem there exists $\Omega_{\epsilon} \subset \Omega$ such that $\mu_{f}\left(\Omega \backslash \Omega_{\epsilon}\right)<\epsilon$ and $\left|X_{k}\right| \rightarrow|X|$ uniformly on $\Omega_{\epsilon}$ as $k \rightarrow+\infty$. Since
$$\left|\frac{\left|X_{k}\right|^{p-2}\left\langle Y, X_{k}\right\rangle}{1+\left|X_{k}\right|^{p-1}}\right| \leq|Y| \quad \text { on } \Omega$$
we therefore obtain
$$\int_{\Omega_{\epsilon}}\left|\frac{\left|X_{k}\right|^{p-2}\left\langle Y, X_{k}\right\rangle}{1+\left|X_{k}\right|^{p-1}}\left(\left|X_{k}\right|^{p-1}-|X|^{p-1}\right)\right| \mathrm{d} \mu_{f} \rightarrow 0 \quad \text { as } k \rightarrow+\infty .$$
On the other hand, using Hölder inequality we deduce
$$\begin{aligned}
& \left|\int_{\Omega \backslash \Omega_{\epsilon}} \frac{\left|X_{k}\right|^{p-2}\left\langle Y, X_{k}\right\rangle}{1+\left|X_{k}\right|^{p-1}}\left(\left|X_{k}\right|^{p-1}-|X|^{p-1}\right)\right| \leq\|Y\|_{L^{p}(\Omega)}\left\|\left|X_{k}\right|^{p-1}-|X|^{p-1}\right\|_{L^{\frac{p}{p-1}}\left(\Omega \backslash \Omega_{\epsilon}\right)} \\
& \leq C\|Y\|_{L^{p}(\Omega)}\left\|\left|X_{k}\right|^{p}+|X|^{p}\right\|_{L^{1}\left(\Omega \backslash \Omega_{\epsilon}\right)}^{\frac{p-1}{p}} \leq C\|Y\|_{L^{p}(\Omega)}\left\|\left|X_{k}-X\right|+|X|^{p}+|X|^{p}\right\|_{L^{1}\left(\Omega \backslash \Omega_{\epsilon}\right)}^{\frac{p-1}{p}} \\
& \leq C\|Y\|_{L^{p}(\Omega)}\left(2^{p}\left\|\left|X_{k}-X\right|^{p}\right\|_{L^{1}(\Omega)}+\left(2^{p}+1\right)\left\||X|^{p}\right\|_{L^{1}\left(\Omega \backslash \Omega_{\varepsilon}\right)}\right)^{\frac{p-1}{p}} .
\end{aligned}$$
For some constant $C>0$ only depending on $p$. The first integral converges to 0 because $\left\|X_{k}-X\right\|_{p} \rightarrow 0$ as $k \rightarrow \infty$, while the second is infinitesimal, if $\epsilon \rightarrow 0$, by the absolute continuity of the integral. Thus
$$0 \leq \limsup _{k \rightarrow+\infty}|(I)| \leq C(\epsilon),$$
\begin{itemize}
\item[] where $C(\epsilon) \rightarrow 0^{+}$as $\epsilon \rightarrow 0$. By the arbitrariness of $\varepsilon,(I) \rightarrow 0$ as $k \rightarrow+\infty$ and, combining with (7.14), $\left(\mathcal{A}\left(u_{k}\right)-\mathcal{A}(u)\right)[\varphi] \rightarrow 0$ as $k \rightarrow+\infty$. Next, in an analogous way, it can be shown that
$$\left(\mathcal{B}\left(u_{k}\right)-\mathcal{B}(u)\right)[\varphi] \rightarrow 0 \quad \text { as } k \rightarrow+\infty .$$
We have thus proved that
$$\mathcal{F}\left(u_{k}\right) \rightharpoonup \mathcal{F}(u) \quad \text { in } W_{0}^{1, p}(\Omega)^{*} \quad \text { as } \quad k \rightarrow \infty,$$
for some subsequence $\left\{u_{k}\right\}$ of the original $\left\{u_{i}\right\}$. A simple reasoning by contradiction thus shows that the whole $\mathcal{F}\left(u_{i}\right) \rightharpoonup \mathcal{F}(u)$ weakly on $W_{0}^{1, p}(\Omega)^{*}$, proving the sequential continuity of $\mathcal{F}$. Therefore, since $\left\|u_{i}-u\right\|_{W_{0}^{1, p}(\Omega)} \rightarrow 0$ as $i \rightarrow+\infty$, for each $\varphi \in W_{0}^{1, p}(\Omega)$, we have:
$$\mathcal{F}\left(u_{i}\right)\left[u_{i}-\varphi\right]=\mathcal{F}\left(u_{i}\right)\left[u_{i}-u\right]+\mathcal{F}\left(u_{i}\right)[u-\varphi] \rightarrow 0+\mathcal{F}(u)[u-\varphi]$$
as $i \rightarrow+\infty$, which because of (7.11) proves the pseudo-monotonicity of $\mathcal{F}$.
\item[iii)] We are left to prove the coercivity of $\mathcal{F}$. This is a more or less predictable consequence of the assumption $\lambda_{V}(\Omega)>0$, but some technical details suggest to provide a full proof. We shall prove the validity of $i i i$ ) with the choice $\bar{\varphi} \equiv 0 \in \overline{\mathcal{K}}_{\psi, \theta}$.
First we observe that, by Cauchy-Schwarz inequality,
$$\mathcal{A}(\bar{u})[\bar{u}] \geq \int_{\Omega}|\nabla(\bar{u}+\theta)|^{p} \mathrm{~d} \mu_{f}-\int_{\Omega}|\nabla(\bar{u}+\theta)|^{p-1}|\nabla \theta| \mathrm{d} \mu_{f} .$$
Next, using
$$|X+Y|^{p} \geq|X|^{p}-p|X|^{p-1}|Y|, \quad|X+Y|^{p-1} \leq 2^{p-1}\left(|X|^{p-1}+|Y|^{p-1}\right)$$
and Hölder inequality into (7.15) we obtain
$$\mathcal{A}(\bar{u})[\bar{u}] \geq\|\nabla \bar{u}\|_{L^{p}(\Omega)}^{p}-C_{3}\|\nabla \bar{u}\|_{L^{p}(\Omega)}^{p-1}-C_{2}$$
for some constants $C_{2}, C_{3}>0$ independent of $\bar{u}$.
To deal with $\mathcal{B}(\bar{u})[\bar{u}]$ we first observe that, since $\theta \geq \psi \geq 0$ and $\bar{u}+\theta \geq 0$, we have
$$\begin{aligned}
-\mathcal{B}(\bar{u})[\bar{u}]= & -\int_{\Omega} V|\bar{u}|^{p} \mathrm{~d} \mu_{f}-\int_{\Omega} V\left[|\bar{u}+\theta|^{p-2}(\bar{u}+\theta)-|\bar{u}|^{p-2} \bar{u}\right] \bar{u} \mathrm{~d} \mu_{f} \\
\geq & -\int_{\Omega} V|\bar{u}|^{p} \mathrm{~d} \mu_{f}-\|V\|_{L^{\infty}(\Omega)} \int_{\{\bar{u} \geq \theta\}}\left[|\bar{u}+\theta|^{p-1}-|\bar{u}|^{p-1}\right] \bar{u} \mathrm{~d} \mu_{f} \\
& -\|V\|_{L^{\infty}(\Omega)} \int_{\{\bar{u}<\theta\}}\left[|\bar{u}+\theta|^{p-1}-|\bar{u}|^{p-1}\right] \bar{u} \mathrm{~d} \mu_{f}
\end{aligned}$$
Since $\bar{u} \geq-\theta$, on the set $\{x \in \Omega: \bar{u}(x) \leq \theta(x)\}$ we have $\bar{u}(x) \in[-\theta, \theta]$; hence the third integral in the right-hand side of the above is bounded above by $C_{5}=3^{p-1} 2\|V\|_{L^{\infty}(\Omega)}\|\theta\|_{L^{p}(\Omega)}^{p}$. As for the second integral, on $\{\bar{u} \geq \theta\}$, the following elementary inequality holds:
$$(\bar{u}+\theta)^{p-1}-\bar{u}^{p-1} \leq \begin{cases}\bar{u}^{p-1}+\theta^{p-1}-\bar{u}^{p-1}=\theta^{p-1} & \text { if } p-1 \leq 1, \\ \bar{u}^{p-1}\left[\left(1+\frac{\theta}{\bar{u}}\right)^{p-1}-1\right] \leq \bar{u}^{p-1}\left[p 2^{p-1} \frac{\theta}{\bar{u}}\right] & \text { if } p-1>1 .\end{cases}$$
\end{itemize}