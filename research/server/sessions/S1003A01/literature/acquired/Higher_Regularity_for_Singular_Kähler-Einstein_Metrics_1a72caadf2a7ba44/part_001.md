---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Higher Regularity for Singular Kähler-Einstein Metrics]

---
source_file: 2202_11083.pdf
converter: mathpix
format: mmd
---

\title{
HIGHER REGULARITY FOR SINGULAR KÄHLER-EINSTEIN METRICS
}

\author{
SHIH-KAI CHIU AND GÁBOR SZÉKELYHIDI
}

\begin{abstract}
We study singular Kähler-Einstein metrics that are obtained as non-collapsed limits of polarized Kähler-Einstein manifolds. Our main result is that if the metric tangent cone at a point is locally isomorphic to the germ of the singularity, then the metric converges to the metric on its tangent cone at a polynomial rate on the level of Kähler potentials. When the tangent cone at the point has a smooth cross section, then the result implies polynomial convergence of the metric in the usual sense, generalizing a result due to Hein-Sun. We show that a similar result holds even in certain cases where the tangent cone is not locally isomorphic to the germ of the singularity. Finally we prove a rigidity result for complete $\partial \bar{\partial}$-exact Calabi-Yau metrics with maximal volume growth. This generalizes a result of Conlon-Hein, which applies to the case of asymptotically conical manifolds.
\end{abstract}

\section*{1. Introduction}

Since the celebrated work of Yau [35] on the existence of Kähler-Einstein metrics there has been increasing interest in the understanding of singular Kähler-Einstein metrics. An early result in this direction is Kobayashi [25] on orbifold Kähler-Einstein metrics, while a definitive existence result for a large class of singularities was obtained by Eyssidieux-Guedj-Zeriahi [19]. These works focus on the case of non-positive Ricci curvature, however recently Li-Tian-Wang [26] extended Chen-Donaldson-Sun's solution [5, 6, 7, 8] of the Yau-Tian-Donaldson conjecture to general Q-Fano varieties. As a result we now have several sources of singular Kähler-Einstein manifolds on normal varieties.

For applications it is desirable to have control of the geometry of these singular metrics near the singularities, but so far little is known in general. The main progress in this direction is due to Hein-Sun [24], who showed that near a large class of smoothable isolated singularities that are locally isomorphic to a Calabi-Yau cone, the singular Calabi-Yau metric must be asymptotic in a strong sense to the Calabi-Yau cone metric. Recently an analogous result was shown by Datar-Fu-Song [15] in the case of isolated log canonical singularities using the bounded geometry method, and precise asymptotics were obtained shortly after by Fu-Hein-Jiang [20]. In more general settings the best results so far give some control of the Kähler potential, such as the work of Guedj-Guenancia-Zeriahi [22] showing continuity.

Our main result in this paper extends the work of Hein-Sun [24] to a large class of non-isolated singularities. In order to state the result, let us suppose that $(Z, p)$ is the non-collapsed pointed Gromov-Hausdorff limit of a sequence of complete polarized Kähler-Einstein manifolds $\left(M_{i}, g_{i}, p_{i}\right)$, satisfying $\operatorname{Ric}\left(g_{i}\right)=\lambda_{i} g_{i}$ with $\left|\lambda_{i}\right| \leq 1$. The results of Donaldson-Sun [17, 18], Li-Xu [28] and Li-Wang-Xu [27] imply that
$Z$ is a normal complex variety admitting a singular Kähler-Einstein metric $\omega_{Z}$, and the metric tangent cone $Z_{p}$ at $p$ is homeomorphic to a normal affine variety uniquely determined by the germ $(Z, p)$. The tangent cone $Z_{p}$ admits a singular Ricci flat cone metric $\omega_{Z_{p}}$. Our first result is the following.

Theorem 1.1. Suppose that the germ $\left(Z_{p}, o\right)$ is biholomorphic to $(Z, p)$, where $o$ denotes the vertex of the cone $Z_{p}$. Then for some $r_{0}>0$ there exists a biholomorphism $\phi: B\left(o, r_{0}\right) \rightarrow U$ from the unit ball in $Z_{p}$ to a neighborhood of $p \in Z$ with $\phi(o)=p$ satisfying the following. There are constants $C, \alpha>0$ and functions $u_{r}$ on $B(o, r)$ for $0<r<r_{0}$, satisfying
$$\phi^{*} \omega_{Z}=\omega_{Z_{p}}+\sqrt{-1} \partial \bar{\partial} u_{r}$$
on the smooth locus of $Z_{p}$, and
$$\sup _{B(o, r)}\left|u_{r}\right| \leq C r^{2+\alpha}$$
for all $0<r<r_{0}$.
Hein-Sun [24] consider the case of singular Calabi-Yau metrics where the tangent cone $Z_{p}$ has an isolated singularity at the vertex, and in addition is "strongly regular". Most likely the approach of Hein-Sun can be extended to the more general Kähler-Einstein setting, without the strongly regular assumption, by appealing to the more recent works [28, 27]. On the other hand their approach uses that the tangent cone $Z_{p}$ has a smooth cross section in an essential way, since they rely on analysis in weighted Hölder spaces. The main novelty in our approach is that by working on the level of $L^{\infty}$-bounds for the Kähler potential, we are able to treat tangent cones with arbitrary singular sets. We can then obtain estimates for derivatives of the metric away from the singular set, which in particular can be used to recover Hein-Sun's result in the setting of tangent cones with isolated singularities (see Corollary 4.3).

When the germ of the tangent cone $\left(Z_{p}, o\right)$ is not biholomorphic to $(Z, p)$, then the situation is more complicated, and has not been considered before. A family of examples given in [33] (also Hein-Naber [23]), are the hypersurfaces $A_{p-1} \subset \mathbf{C}^{n+1}$ defined by
$$z^{p}+x_{1}^{2}+\ldots+x_{n}^{2}=0,$$
where $p>2 \frac{n-1}{n-2}$. In [33] the second author constructed a Calabi-Yau metric $\omega_{A_{p-1}}$ on a neighborhood of $0 \in A_{p-1}$, with tangent cone given by $\mathbf{C} \times A_{1}$, where $A_{1} \subset \mathbf{C}^{n}$ is defined by $x_{1}^{2}+\ldots+x_{n}^{2}=0$ and is equipped with the Stenzel cone metric. Our result in this case is the following.

Theorem 1.2. Suppose that, as above, $(Z, p)$ is the pointed Gromov-Hausdorff limit of a non-collapsing sequence of polarized Kähler-Einstein manifolds, with singular Kähler-Einstein metric $\omega_{Z}$. Suppose that the germ $(Z, p)$ is isomorphic to the germ $\left(A_{p-1}, 0\right)$ at the origin. Then for some $r_{0}>0$ there is a biholomorphism $\phi$ : $B\left(0, r_{0}\right) \rightarrow U \subset Z$, with $\phi(0)=p$, and constants $\Lambda, C, \alpha>0$, such that
$$\phi^{*} \omega_{Z}=\Lambda \omega_{A_{p-1}}+\sqrt{-1} \partial \bar{\partial} u_{r}$$
for some $u_{r}$ defined on $B(0, r)$, and
$$\sup _{B(0, r)}\left|u_{r}\right| \leq C r^{2+\alpha}$$
for all $r<r_{0}$.
In other words the singular Kähler-Einstein metric $\omega_{Z}$ converges to a suitable scaling of the model metric $\omega_{A_{p-1}}$ at a polynomial rate, at the level of potentials. Note that in contrast with Theorem 1.1, where the model metrics were cones, here the rescalings of $\omega_{A_{p-1}}$ are not isometric to each other. In general we expect that for more complicated singularities it is possible to have higher dimensional families of model metrics, similarly to how in the first author's thesis [9] a two dimensional family of complete Ricci flat Kähler metrics was constructed on $\mathbf{C}^{3}$ with tangent cone $\mathbf{C} \times A_{2}$ at infinity.

Our last result is the following uniqueness theorem for solutions of the Monge-Ampère equation on complete manifolds.

Theorem 1.3. Let $(X, \omega)$ be a $\partial \bar{\partial}$-exact Calabi-Yau manifold with maximal volume growth. Suppose that $u$ is a smooth solution of the complex Monge-Ampère equation
$$(\omega+\sqrt{-1} \partial \bar{\partial} u)^{n}=\omega^{n} .$$
In addition suppose that $u$ has subquadratic growth in the sense that $|u| \leq C(1+$ $r)^{2-\delta}$ for some $C, \delta>0$, where $r$ is the distance from a fixed point in $X$. Then $\partial \bar{\partial} u=0$.

This result should be compared with the uniqueness result in Conlon-Hein [14, Theorem 3.1]. The main novelty is that in our result we do not need to assume that the tangent cone of $X$ at infinity has an isolated singularity, which is implied by the AC assumption of [14]. Note, however, that the $\partial \bar{\partial}$-exactness is not required in [14].

The main new technical ingredient in the proofs of these theorems is an estimate for solutions of the complex Monge-Ampère equation on non-collapsed balls in polarized Kähler manifolds with Ricci curvature bounds, or their Gromov-Hausdorff limits. This extends a related estimate from [34], where we considered balls that are Gromov-Hausdorff close to a metric cone of the form $\mathbf{C} \times C(Y)$, with smooth $Y$. Roughly speaking the result says that if a solution $u$ of a Monge-Ampère equation with sufficiently small $L^{\infty}$ norm concentrates near the (almost) singular set of such a ball, then the solution must decay by a definite amount when passing to a smaller ball. This is the key ingredient for showing that "small" solutions of the Monge-Ampère equation are modeled on harmonic functions We will discuss this estimate in Section 2 and we expect it to be of independent interest.

In Section 3 we define the notion of families of model metrics as well as a convergence result for the singular Kähler-Einstein metric $\omega_{Z}$ that can be approximated by these model metrics near the singularities. This unifies certain aspects of Theorems 1.1 and 1.2. We then prove these theorems by showing the existence of families of model metrics and the existence of approximations in the corresponding cases in Sections 4 and 5. Finally, in Section 6 we prove Theorem 1.3.

Acknowledgments. We would like to thank Hans-Joachim Hein for helpful discussions. SC is supported by the Simons Collaboration on Special Holonomy in Geometry, Analysis, and Physics (\#724071 Jason Lotay), and he would like to thank the National Center for Theoretical Sciences for their hospitality during Summer 2021. GSz is supported in part by NSF grant DMS-1906216.

\section*{2. Non-concentration}

In this section we study the complex Monge-Ampère equation on a ball in a non-collapsed Gromov-Hausdorff limit of Kähler-Einstein manifolds. More precisely, let $(Z, p)$ be the pointed Gromov-Hausdorff limit of a sequence of complete pointed Kähler manifolds $\left(M_{i}, g_{i}, p_{i}\right)$. We assume that the $\left(M_{i}, g_{i}\right)$ are polarized, i.e. the Kähler forms are given by the curvature of line bundles over the $M_{i}$, that the metrics are Einstein, i.e. $\operatorname{Ric}\left(g_{i}\right)=\lambda_{i} g_{i}$ for some $\left|\lambda_{i}\right| \leq 1$, and that the non-collapsing condition $\operatorname{vol}\left(B_{g_{i}}\left(p_{i}, 1\right)\right)>\nu>0$ holds for a fixed $v>0$. By the results of Donaldson-Sun [17, 18], $B(p, 2)$ is a normal algebraic variety, and the metric singular set coincides with the algebro-geometric singular set $\Sigma \subset B(p, 2)$. For $q \in B(p, 1)$ let us denote by $r_{h}(q)$ the harmonic radius at $q$, setting $r_{h}(q)=0$ for $q \in \Sigma$. We denote the limit metric on the regular part of $Z$ by $\omega$. The main result of this section is the following estimate for solutions of the complex Monge-Ampère equation on $B(p, 1)$.

Theorem 2.1. There is a constant $C=C(n, \nu)$, such that for all $\gamma>0$ there exist $\kappa, \delta>0$ depending on $n, \nu, \gamma$ with the following property. Suppose that we have smooth functions $u, f$ on $B(p, 1) \backslash \Sigma$, satisfying $|u|,|f|<\kappa$, and
$$(\omega+\sqrt{-1} \partial \bar{\partial} u)^{n}=e^{f} \omega^{n} .$$
Then
$$\sup _{B(p, 1 / 2)}|u| \leq C\left(\sup _{\left\{r_{h}>\delta\right\} \cap B(p, 1)}|u|+\sup _{B(p, 1)}|f|+\gamma \sup _{B(p, 1)}|u|\right) .$$

We prove this result by proving successively more general cases. We start with the following, which follows the approach of [34, Proposition 4.5].

Lemma 2.2. There is a $C_{1}=C_{1}(n, \nu)$ such that for any $\gamma \in(0,1)$ there are $\kappa, \delta, \epsilon>0$ depending on $n, \nu, \gamma$ satisfying the following. Suppose that $|u|,|f|<\kappa$ satisfy (2.1), and in addition $\operatorname{Ric}(\omega)>-\epsilon \omega$ and $d_{G H}\left(B\left(p, \epsilon^{-1}\right), B\left(o, \epsilon^{-1}\right)\right)<\epsilon$, where $o$ is the vertex of a cone that splits an isometric factor of $\mathbf{C}^{k}$ for some $k \geq 0$. Let us write $o \in \mathbf{C}^{k} \times C(Y)$. Then
$$\sup _{B(p, 1 / 2)}|u| \leq C_{1}\left(\sup _{B(p, 1) \backslash N_{\delta}}|u|+\sup _{B(p, 1)}|f|+\gamma \sup _{B(p, 1)}|u|\right),$$
where $N_{\delta}$ denotes the points $x$ at distance at most $\delta$ from $\mathbf{C}^{k} \times\{0\}$ under the Gromov-Hausdorff approximation.

In this result we do not assume, as we did in [34], that $Y$ is smooth. In addition, note that on the right hand side of (2.2) the supremum of $|u|$ is taken on the set $B(p, 1) \backslash N_{\delta}$ which is typically larger than the set $\left\{r_{h}>\delta\right\} \cap B(p, 1)$ if $Y$ has singularities.

Proof. We claim that by 34, Proposition 4.4] there exists a constant $D>0$ depending on $n, \nu$, and for any $\delta>0$ there exists $C_{\delta}>0$ depending on $\delta, n, \nu$ satisfying the following. If $\epsilon$ is sufficiently small (depending on $\delta, n, \nu$ ), then there exists a Lipschitz function $v$ on $B(p, 1-\delta)$ satisfying
\begin{itemize}
\item[(1)] $|\sqrt{-1} \partial \bar{\partial} v|_{\omega}<C_{\delta}$ on $B(p, 1-\delta / 2) \backslash \Sigma$.
\item[(2)] $v>D^{-1} \delta^{-1 / 2}$ on $\partial B(p, 1-\delta) \cap N_{\delta}$.
\item[(3)] $v>D^{-1}$ on $B(p, 1-\delta)$, and $v<D$ on $B(p, 1 / 2)$.
\end{itemize}
\begin{itemize}
\item[(4)] On $B(p, 1-\delta / 2) \backslash \Sigma, v$ satisfies the differential inequality:
$$\sum_{i} \mu_{i}+\mu_{\max }<-1 / 10,$$
where $\mu_{i}$ are the eigenvalues of $\sqrt{-1} \partial \bar{\partial} v$ relative to $\omega$, and $\mu_{\text {max }}$ is the largest eigenvalue.
\end{itemize}

To see this, recall that $B(p, 1)$ is a ball in the pointed Gromov-Hausdorff limit of polarized Kähler-Einstein manifolds $\left(M_{i}, p_{i}\right)$. Given $\epsilon>0$ we have
$$d_{G H}\left(B\left(p_{i}, \epsilon^{-1}\right), B\left(o, \epsilon^{-1}\right)\right)<\epsilon$$
for sufficiently large $i$, and so by [34, Proposition 4.4] we have functions $v_{i}$ satisfying the properties (1) - (4) on $B\left(p_{i}, 1\right)$. While in [34] the property (4) is stated as $\sum \mu_{i}+\mu_{\text {max }}<0$, from the proof the better bound -1/10 also follows (see Equation (4.3) and the inequality before it in [34]). From the construction we see that $v_{i}$ and $\nabla v_{i}$ are uniformly bounded on $B\left(p_{i}, 1-\delta\right)$ and on compact sets away from the singular set of $B(p, 1)$ (under Gromov-Hausdorff approximations) the functions $v_{i}$ have uniform higher derivative estimates as well, as they are constructed from Kähler potentials. We can therefore take a subsequential limit $v$ of $v_{i}$ on $B(p, 1-\delta)$, and conditions (1), (4) will follow from smooth convergence on the regular set. That the constants do not depend on the specific cone $C(Y)$, but only on $n, \nu$, can be seen using a compactness argument.

Let us define
$$E=\sup _{B(p, 1) \backslash N_{\delta}}|u|+\sup _{B(p, 1)}|f|+\gamma \sup _{B(p, 1)}|u| \leq 3 \kappa,$$
and set $\delta \leq \gamma^{2}$. Define $\tilde{v}=D E v$. By (2), (3) above, on $\partial B(p, 1-\delta)$ we have $\tilde{v}>u$.
We claim that once $\kappa$ is sufficiently small, then we have
$$\tilde{v} \geq u \text { on } B(p, 1-\delta) .$$
To see this, we argue as in [34], except we need to take care of the singular set $\Sigma$. Since $\Sigma$ is a subvariety, there exists a plurisubharmonic function $h$ on $B(p, 1)$ such that $\Sigma=h^{-1}(-\infty)$. We will show (2.3) by showing that we have $\tilde{v}>u+\epsilon^{\prime} h$ on $B(p, 1-\delta)$, for all $\epsilon^{\prime}>0$, and noting that $u, \tilde{v}$ are continuous. Suppose this is not the case. Write $B=B(p, 1-\delta)$ and for a fixed $\epsilon^{\prime}>0$ set
$$t_{0}=\inf \left\{t>0 \mid \tilde{v}+t>u+\epsilon^{\prime} h \text { on } B\right\} .$$
If $t_{0}>0$, then the graph of $\tilde{v}+t_{0}$ touches the graph of $u+\epsilon^{\prime} h$ from above at some point $q \in B$. If $q \in \Sigma$, then $\left(u+\epsilon^{\prime} h\right)(q)=-\infty$, so we must have $q \notin \Sigma$. At $q$ we have
$$\sqrt{-1} \partial \bar{\partial} u(q) \leq \sqrt{-1} \partial \bar{\partial} u(q)+\epsilon^{\prime} \sqrt{-1} \partial \bar{\partial} h(q) \leq \sqrt{-1} \partial \bar{\partial} \tilde{v}(q) \leq E D C_{\delta} \omega$$
by property (1) above and the fact that $h$ is plurisubharmonic. Let $\lambda_{i}$ be the eigenvalues of $\sqrt{-1} \partial \bar{\partial} u(q)$ relative to $\omega$. From (2.4) we have $\lambda_{i} \leq C_{\delta} D E$. By (2.1), and using $|f| \leq E$, we have
$$e^{-E} \leq \prod_{i=1}^{n}\left(1+\lambda_{i}\right) \leq e^{E} .$$
From (2.5) we have
$$1+\lambda_{j} \geq \frac{e^{-E}}{\prod_{i \neq j}\left(1+\lambda_{i}\right)} \geq e^{-E}\left(1+C_{\delta} E\right)^{-(n-1)} \geq 1-C_{2, \delta} E$$
for some constant $C_{2, \delta}>0$, once $E$ is sufficiently small. On the other hand, if $\lambda_{\text {max }}<0$ then (2.6) gives
$$\lambda_{\max } \geq-E .$$
Finally, (2.5) together with the bounds for $\lambda_{i}$ implies that
$$1-E \leq e^{-E} \leq \prod_{i=1}^{n}\left(1+\lambda_{i}\right) \leq 1+\sum_{i=1}^{n} \lambda_{i}+C_{3, \delta} E^{2},$$
so (2.4) and (2.8) imply that
$$-2 E-C_{3, \delta} E^{2} \leq \sum_{i=1}^{n} \lambda_{i}+\lambda_{\max } \leq D E\left(\sum_{i=1}^{n} \mu_{i}+\mu_{\max }\right) \leq-\frac{D E}{10} .$$
The first inequality above uses (2.7). We can assume that $D>30$. Since $E \leq 3 \kappa$, by letting $\kappa$ be sufficiently small, depending on $\delta$, we get a contradiction. For such $\kappa$ we have shown (2.3).

Using (2.3) and property (3) above, on $B(p, 1 / 2)$ we have
$$u \leq \tilde{v} \leq D^{2} E,$$
which implies the estimate from above for $u$ required by (2.2). For the corresponding lower bound we can argue in a similar way, comparing $u$ with $-\tilde{v}$ instead, to show that $u>-\tilde{v}+\epsilon^{\prime} h$ on $B$ for all $\epsilon^{\prime}>0$ once $\kappa$ is sufficiently small. \(\square\)

Next we have the following.
Lemma 2.3. There is a $C_{2}=C_{2}(n, \nu)$ such that for any $\gamma>0$ there are $\kappa, \delta, \epsilon>0$ depending on $n, \nu, \gamma$ satisfying the following. Suppose $|u|,|f|<\kappa$ satisfy (2.1), and $d_{G H}\left(B\left(p, \epsilon^{-1}\right), B\left(o, \epsilon^{-1}\right)\right)<\epsilon$ for the vertex $o \in C(Y)$ in a cone. Then
$$\sup _{B(p, 1 / 2)}|u| \leq C_{2}\left(\sup _{\left\{r_{h}>\delta\right\} \cap B(p, 1)}|u|+\sup _{B(p, 1)}|f|+\gamma \sup _{B(p, 1)}|u|\right) .$$
Proof. We prove this by decreasing induction on the dimension of the Euclidean factor that splits off from the cone $C(Y)$, starting with $C(Y)=\mathbf{C}^{n}$. In this case, by Cheeger-Colding [2, Theorem 7.3], we have $r_{h}>r_{0}$ on $B(p, 1)$ for a fixed $r_{0}>0$. The inequality (2.9) then holds if we choose $\delta<r_{0}$, and $C_{2}>1$.

Suppose now that the result holds whenever $B\left(p, \epsilon^{-1}\right)$ is $\epsilon$-close to a ball in a cone of the form $\mathbf{C}^{j} \times C(X)$ for $j \geq k+1$, and consider the case that
$$d_{G H}\left(B\left(p, \epsilon^{\prime-1}\right), B\left(o, \epsilon^{\prime-1}\right)\right)<\epsilon^{\prime},$$
where $o \in \mathbf{C}^{k} \times C(Y)$. By Lemma 2.2 there are $C_{1}(n, \nu)$ and $\kappa_{1}, \delta_{1}, \epsilon_{1}>0$ depending on $\gamma, n, \nu$, such that if $|u|,|f|<\kappa_{1}$ and $\epsilon^{\prime}<\epsilon_{1}$, then
$$\sup _{B(p, 1 / 2)}|u| \leq C_{1}\left(\sup _{B(p, 1) \backslash N_{\delta_{1}}}|u|+\sup _{B(p, 1)}|f|+\gamma \sup _{B(p, 1)}|u|\right) .$$
We will complete the proof by estimating $|u|$ outside of $N_{\delta_{1}}$ using the inductive hypothesis.

Given the $\epsilon>0$ from the inductive hypothesis, there are $r, \epsilon_{2}>0$ depending on $n, \nu, \gamma$ with the following property. If $\epsilon^{\prime}<\epsilon_{2}$ in (2.10), then for all $x \in B(p, 1) \backslash N_{\delta_{1}}$ there is an $r_{x}>r$ such that
$$d_{G H}\left(B\left(x, \epsilon^{-1} r_{x}\right), B\left(o^{\prime}, \epsilon^{-1} r_{x}\right)\right)<\epsilon r_{x},$$
for the origin $o^{\prime} \subset \mathbf{C}^{k+1} \times C\left(Y^{\prime}\right)$ in a cone that splits off an isometric factor of $\mathbf{C}^{k+1}$. The reason for this is that if $x \in \mathbf{C}^{k} \times C(Y)$ does not lie in $\mathbf{C}^{k} \times\{0\}$, then the tangent cones at $x$ split an additional Euclidean factor by Cheeger-Colding [1, Theorem 6.62] and Cheeger-Colding-Tian [3, Theorem 9.1].

At such a point $x \in B(p, 1) \backslash N_{\delta_{1}}$ consider a ball $B\left(x, r_{x}\right)$ scaled up to unit size, which we denote by $B\left(x^{\prime}, 1\right)$. We can assume that $r_{x}^{-1}$ is an integer, so the rescaled ball is also the limit of a sequence of polarized Kähler-Einstein manifolds. On the rescaled ball $B\left(x^{\prime}, 1\right)$ we have the equation
$$\left(\omega^{\prime}+\sqrt{-1} \partial \bar{\partial} u^{\prime}\right)^{n}=e^{f^{\prime}} \omega^{\prime n},$$
where $\omega^{\prime}=r_{x}^{-2} \omega, u^{\prime}=r_{x}^{-2} u$ and $f^{\prime}=f$. In particular
$$\begin{aligned}
& \sup _{B\left(x^{\prime}, 1\right)}\left|u^{\prime}\right| \leq r_{x}^{-2} \sup _{B(p, 1)}|u|, \\
& \sup _{B\left(x^{\prime}, 1\right)}\left|f^{\prime}\right| \leq \sup _{B(p, 1)}|f|,
\end{aligned}$$
and
$$d_{G H}\left(B\left(x^{\prime}, \epsilon^{-1}\right), B\left(o^{\prime}, \epsilon^{-1}\right)\right)<\epsilon .$$
We can now choose $\kappa, \delta, \epsilon$ small enough, depending on $n, \nu, \gamma$ (recall that $r_{x}>r$ and $r$ depends on $n, \nu, \gamma$ ) so that the inductive hypothesis applies, and therefore
$$\sup _{B\left(x^{\prime}, 1 / 2\right)}\left|u^{\prime}\right| \leq C\left(\sup _{\left\{r_{h}^{\prime}>\delta\right\} \cap B\left(x^{\prime}, 1\right)}\left|u^{\prime}\right|+\sup _{B\left(x^{\prime}, 1\right)}\left|f^{\prime}\right|+\gamma \sup _{B\left(x^{\prime}, 1\right)}\left|u^{\prime}\right|\right) .$$
Here we are writing $r_{h}^{\prime}$ for the harmonic radius in the scaled up metric. We have $r_{h}^{\prime}=r_{x}^{-1} r_{h}$. Scaling back down we have
$$\begin{aligned}
|u(x)| & \leq C\left(\sup _{\left\{r_{h}>r_{x} \delta\right\} \cap B\left(x, r_{x}\right)}|u|+\sup _{B\left(x, r_{x}\right)} r_{x}^{2}|f|+\gamma \sup _{B\left(x, r_{x}\right)}|u|\right) \\
& \leq C\left(\sup _{\left\{r_{h}>r \delta\right\} \cap B(p, 1)}|u|+\sup _{B(p, 1)}|f|+\gamma \sup _{B(p, 1)}|u|\right) .
\end{aligned}$$
Since $x \in B(p, 1) \backslash N_{\delta_{1}}$ was arbitrary, this inequality together with (2.11) implies the required result. \(\square\)

Finally we can give the proof of Theorem 2.1.
Proof of Theorem 2.1. Given $\epsilon>0$, by Cheeger-Colding [1] there exists a $\rho>0$, depending on $\epsilon, n, \nu$, with the following property: for all $x \in B(p, 1 / 2)$ we have some $\rho_{x}>\rho$ such that
$$d_{G H}\left(B\left(x, \epsilon^{-1} \rho_{x}\right), B\left(o, \epsilon^{-1} \rho_{x}\right)\right)<\epsilon \rho_{x},$$
for $o \in C(Y)$ in some metric cone $C(Y)$. We can then rescale the ball $B\left(x, \rho_{x}\right)$ to unit size, and if $\epsilon, \kappa, \delta$ is chosen sufficiently small, then we can apply Lemma 2.3 to bound $|u(x)|$ similarly to the argument in the proof of Lemma 2.3. \(\square\)

\section*{3. Decay estimate}

The goal of this section is to prove a convergence result, Proposition 3.7 below, which contains some common features of Theorem 1.1 and Theorem 1.2. Let $(Z, p)$ be the Gromov-Hausdorff limit of a non-collapsing sequence of polarized Kähler-Einstein manifolds of complex dimension $n$, and let $C(Y)$ be the tangent cone at $p$. We will define a family of model metrics in a neighborhood $\mathcal{U}$ of $p$ in $Z$ parametrized by small quadratic harmonic functions on $C(Y)$ which generate automorphisms of $C(Y)$, and prove an abstract decay estimate, Proposition 3.5 for the family. Throughout this section, as well as later on, we will denote by $\Psi(\epsilon)$ functions satisfying $\lim _{\epsilon \rightarrow 0} \Psi(\epsilon)=0$.

We first recall some important properties of subquadratic harmonic functions on $C(Y)$. The following lemma combines results going back to Cheeger-Tian [4, Section 7], Conlon-Hein [14, Corollary 3.6] and Hein-Sun [24, Theorem 2.14] when $C(Y)$ has an isolated singularity:

Lemma 3.1. Suppose $C(Y)$ is a metric tangent cone of a non-collapsed Gromov-Hausdorff limit of Kähler-Einstein manifolds. Let $r$ denote the radial coordinate so that $r \partial_{r}$ is the homothetic vector field. Let $J$ denote the complex structure. Suppose $u$ is a harmonic function on $C(Y)$. Then we have the following:
\begin{itemize}
\item[(1)] If $u$ is $s$-homogeneous $\left(\nabla_{r \partial_{r}} u=s u\right)$ with $s<2$, then $u$ is pluriharmonic.
\item[(2)] If $u$ is 2-homogeneous harmonic, then $u=u_{1}+u_{2}$, where $u_{1}$ is pluriharmonic, and $u_{2}$ is $J\left(r \partial_{r}\right)$-invariant.
\item[(3)] The space of real holomorphic vector fields that commute with $r \partial_{r}$ can be written as $\mathfrak{p} \oplus J \mathfrak{p}$, where $\mathfrak{p}$ is spanned by $r \partial_{r}$ and vector fields of the form $\nabla u$, where $u$ is a $J\left(r \partial_{r}\right)$-invariant harmonic function homogeneous of degree 2. Jp consists of real holomorphic Killing vector fields.
\end{itemize}

Proof. In our setting the singular set has Hausdorff codimension at least 4 [3]. To deal with the singular set we can use the cut-off functions for example in [10, Lemma 2.3]. (1) is proved in [10, Corollary 2.18]. For (2) and (3), see [9, Proposition 3.19] for more details. \(\square\)

On $\mathcal{U}$, we consider a family of Calabi-Yau metrics on the regular set of $\mathcal{U}$ with tangent cone $C(Y)$ at $p$, satisfying properties that enable a decay estimate. To proceed, let $H$ denote the space of quadratic harmonic functions $h$ such that $\nabla h$ generates a biholomorphism which commutes with scaling. $H$ as a vector space is equipped with the $L^{\infty}$ norm on $B(0,1) \subset C(Y)$. For $h \in H$ let us denote this norm simply by $\|h\|$.

Definition 3.2. Let $U \subset H$ be an open neighborhood of $0 \in H$. A family $\mathcal{F}$ of model Calabi-Yau metrics consists of a set of Calabi-Yau metrics $\omega_{h}$ on the regular set of $\mathcal{U}$, whose metric completion is homeomorphic to $\mathcal{U}$, parametrized by $h \in U$, with the following properties:
\begin{itemize}
\item[(1)] For sequences $h_{i} \in U$ and $r_{i} \rightarrow 0$, set $B_{i}=B_{r_{i}^{-2} \omega_{h_{i}}}(p, 1)$. Then there is a sequence of holomorphic maps $F_{i}: B_{i} \rightarrow \mathbf{C}^{N}$, and $\Psi\left(i^{-1}\right)$-Gromov-Hausdorff approximations $f_{i}: B_{i} \rightarrow B(0,1)$ such that $\left|F_{i}-F_{\infty} \circ f_{i}\right|<$ $\Psi\left(i^{-1}\right)$.
\item[(2)] The volume form $\omega_{h}^{n}$ is independent of $h \in U$.
\item[(3)] For $h, k \in U$ and $r>0$, we have $\left|d_{\omega_{h}}-d_{\omega_{k}}\right| \leq C(\|k\|+\|h\|) r$ on $B_{\omega_{h}}(p, r)$.
\end{itemize}
\begin{itemize}
\item[(4)] For $h, k \in U$, on $B_{\omega_{h}}(p, 2)$ we have $\omega_{k}=\omega_{h}+\sqrt{-1} \partial \bar{\partial} u$, and for every $r>0$, we have $|u| \leq C\|h-k\| r^{2}$ on $B_{\omega_{h}}(p, r)$.
\item[(5)] Suppose that there are $r_{i} \rightarrow 0$ and sequences $h_{i}, k_{i} \in U$ such that $\left\|h_{i}\right\|,\left\|k_{i}\right\| \rightarrow$ 0. Write $\omega_{k_{i}}=\omega_{h_{i}}+\sqrt{-1} \partial \bar{\partial} u_{i}$ as in (4). For any $\epsilon>0$ and $K$ a compact set in the regular set of $B(0,1) \subset C(Y)$, there exist compact sets $K_{i} \subset B_{r_{i}^{-2} \omega_{h_{i}}}(p, 1)$ such that $K_{i} \rightarrow K$ in the Gromov-Hausdorff sense, and
$$\left|r_{i}^{-2} u_{i}-f_{i}^{*}\left(k_{i}-h_{i}\right)\right| \leq \epsilon\left\|k_{i}-h_{i}\right\|$$
on $K$ for all sufficiently large $i$, where $f_{i}$ is the Gromov-Hausdorff approximation in (1).
\end{itemize}

The following lemma shows that we have higher regularity of the solutions to the complex Monge-Ampère equation if the $L^{\infty}$ norm is sufficiently small.

Lemma 3.3. Suppose that $B(p, 2)$ is a ball in a Kähler-Einstein manifold of complex dimension $n$, with metric $\omega$ satisfying $\operatorname{Ric}(\omega)=c^{\prime} \omega$, such that in suitable coordinates $z^{i}$ the components $\omega_{i \bar{j}}$ satisfy $\left|\partial^{3}\left(\delta_{i \bar{j}}-\omega_{i \bar{j}}\right)\right|<\frac{1}{100}$ in terms of the Euclidean metric $\delta_{i \bar{j}}$. If $\epsilon>0$ is sufficiently small, then we have the following.

Suppose that $\eta=\omega+\sqrt{-1} \partial \bar{\partial} u$ is another Kähler-Einstein metric on $B(p, 2)$ with $\operatorname{Ric}(\eta)=c \eta$ and $\eta^{n}=e^{f} \omega^{n}$, so that
$$|u|,|f|,|c|,\left|c^{\prime}\right|<\epsilon .$$
There exist $C_{k}>0$ depending on the dimension $n$ and on $k$, such that
$$\|u\|_{C^{k, \alpha}(B(p, 1))}<C_{k} \epsilon .$$
Proof. All the operators and norms below are taken with respect to $\omega$, and the constants $C_{k}$ may change from line to line. Note first that from elliptic regularity for the equation $\operatorname{Ric}(\omega)=c^{\prime} \omega$, we obtain higher order estimates $\left|\partial^{k} \omega_{i \bar{j}}\right|<C_{k}$ for the components of $\omega$. From the equation $\eta^{n}=e^{f} \omega^{n}$ and the Kähler-Einstein condition for $\omega$ and $\eta$, we have $c \eta=-\sqrt{-1} \partial \bar{\partial} f+c^{\prime} \omega$, so the function $v=c u+f$ satisfies $\sqrt{-1} \partial \bar{\partial} v=\left(c^{\prime}-c\right) \omega$. It follows that $\Delta v=\left(c^{\prime}-c\right) n$. Using the Schauder estimates we then have $\|v\|_{C^{k}}<C_{k} \epsilon$ on the ball where $\{|z|<1.9\}$.

We now rewrite the equation in a form so that Savin's small perturbation result [31] can be applied. Consider the equation
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} u_{0}\right)^{n}=e^{v-c u_{0}} \omega^{n}$$
for $u_{0}$, with $u_{0}=0$ on the boundary of the ball $\{|z|<1.9\}$ in our coordinates. Define
$$\begin{aligned}
F: C_{0}^{2, \alpha} \times C^{2, \alpha} \times \mathbf{R} & \rightarrow C^{0, \alpha} \\
\left(u_{0}, v, c\right) & \mapsto \log \operatorname{det}\left(\frac{\left(\omega+\sqrt{-1} \partial \bar{\partial} u_{0}\right)^{n}}{\omega^{n}}\right)-v+c u_{0}
\end{aligned}$$
where $C_{0}^{2, \alpha}, C^{2, \alpha}$ denote functions on the ball $\{|z|<1.9\}$, with zero boundary values in the first case. Note that $F(0,0,0)=0$, and the linearization at (0, 0, 0) in the $u_{0}$ direction is $\Delta+c$. As long as $c$ is sufficiently small, this operator is invertible. By the implicit function theorem, for sufficiently small $v \in C^{2, \alpha}$ and $c \in \mathbf{R}$ we can find $u_{0}$ that satisfies the equation, with $\left\|u_{0}\right\|_{C^{2, \alpha}}<\delta$, where $\delta>0$ can be made as small as we like by choosing $\epsilon$ small.

To write our equation in a different form, let $h=u-u_{0}$. Then $h$ satisfies
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} u_{0}+\sqrt{-1} \partial \bar{\partial} h\right)^{n}=e^{-c h} e^{v-c u_{0}} \omega^{n} .$$

Thanks to the bounds for $v$ and $u_{0}$, the above equation is uniformly elliptic, and $h=0$ is a solution of it. By Savin's theorem [31], for any given $\delta>0$ we have $\|h\|_{C^{2, \alpha}(B(p, 1))}<\delta$ once $h$ is sufficiently small in $L^{\infty}$. It follows that if $\epsilon$ is chosen sufficiently small, then $h$ and $u_{0}$, and therefore also $u$ will satisfy $|u|_{C^{2}}<\delta$ on the ball $\{|z|<1.8\}$.

Let us now write the equation $(\omega+\sqrt{-1} \partial \bar{\partial} u)^{n}=e^{f} \omega^{n}$ for $u$ as
$$\left(n \omega^{n-1}+\binom{n}{2} \omega^{n-2} \wedge(\sqrt{-1} \partial \bar{\partial} u)+\cdots+(\sqrt{-1} \partial \bar{\partial} u)^{n-1}\right) \wedge \sqrt{-1} \partial \bar{\partial} u=\left(e^{f}-1\right) \omega^{n} .$$
If $\delta$ is sufficiently small, then this can be written as a uniformly elliptic linear equation
$$P u=e^{f}-1,$$
where the coefficients of $P$ (which depend on $u$ ) are bounded in $C^{k}$. Note that if $|f|<\epsilon$ for small $\epsilon$, then $\left|e^{f}-1\right|<2 \epsilon$. We can now use standard $L^{p}$ and Schauder estimates, as well as bootstrapping using the estimates that we already have for $c u+f$, to obtain $|u|_{C^{k}}<C_{k} \epsilon$ on the smaller ball $\{|z|<1.7\}$. \(\square\)

We will need the following result, which allows us to estimate the difference between the distance functions of a model metric and a Gromov-Hausdorff limit. This will be used in the proof of Proposition 3.7 below, to ensure that along the iteration procedure the distance functions of the two metrics that we are comparing remain close to each other at smaller and smaller scales.

Lemma 3.4. Let $\lambda>0$. Then for all sufficiently small $\epsilon>0$ and $r>0$, the following holds. Let $\omega=\omega_{h} \in \mathcal{F}$ be a model metric with $\|h\| \leq \epsilon$. Now, suppose $\eta$ is another Kähler-Einstein metric on the regular set of $B_{\omega}(p, 2 r)$ obtained as the non-collapsed Gromov-Hausdorff limit of polarized Kähler-Einstein manifolds, with the following properties:
\begin{itemize}
\item[-] $\operatorname{Ric}(\eta)=c \eta$ with $|c|<r^{-2} \epsilon ;$
\item[-] $\eta^{n}=e^{f} \omega^{n}$ with $|f|<\epsilon$;
\item[-] $\omega=\eta+\sqrt{-1} \partial \bar{\partial} u$ with $|u|<r^{2} \epsilon$;
\item[-] $\left|d_{\omega}-d_{\eta}\right|<r / 100$.
\end{itemize}

Then we have $\left|d_{\omega}-d_{\eta}\right|<\lambda r$ on $B_{\omega}(p, r)$.
Proof. We argue by contradiction, supposing that we have $\epsilon_{i}, r_{i} \rightarrow 0$ and corresponding $\eta_{i}, f_{i}$ and $u_{i}$ such that the result fails. Let us rescale the metrics by setting $\tilde{\omega}_{i}=r_{i}^{-2} \omega, \tilde{\eta}_{i}=r_{i}^{-2} \eta_{i}$. Set $A_{i}=B_{\tilde{\eta}_{i}}(0,1)$ and $B_{i}=B_{\tilde{\omega}_{i}}(0,2)$. By the assumption on $\left|d_{\omega_{i}}-d_{\eta_{i}}\right|$ we have the inclusions $f_{i}: A_{i} \subset B_{i}$. To get a contradiction, we will show that $f_{i}$ is a $\Psi\left(i^{-1}\right)$-Gromov-Hausdorff approximation for sufficiently large $i$. Let us define $g_{i}=F_{i} \circ f_{i}$, where $F_{i}$ are the maps in property (1) of Definition 3.2. Then $g_{i}: A_{i} \rightarrow \mathbf{C}^{N}$ are holomorphic maps. By property (1) of Definition 3.2, we have $\left|g_{i}\right| \leq C$ for some constant $C>0$ once $i$ is sufficiently large. Then by the gradient estimate for holomorphic maps, we have $\left|\nabla g_{i}\right|_{\tilde{\eta}_{i}} \leq C$ for a uniform constant $C>0$. This implies that $g_{i}$ are equicontinuous.

We claim that for all $\epsilon>0$, there exists $\delta>0$ such that if $x, y \in B_{i}$ and $\left|F_{i}(x)-F_{i}(y)\right|<\delta$, then $d_{\tilde{\omega}_{i}}(x, y)<\epsilon$. If this is not the case, then there exist $x_{i}, y_{i} \in$ $B_{i}$ with $\left|F_{i}\left(x_{i}\right)-F_{i}\left(y_{i}\right)\right| \rightarrow 0$ but $d_{\tilde{\omega}_{i}}\left(x_{i}, y_{i}\right) \geq \epsilon$. By passing to a subsequence, we may assume that $x_{i} \rightarrow x$ and $y_{i} \rightarrow y$ for $x, y \in B(0,2)$ under the Gromov-Hausdorff
convergence $B_{i} \rightarrow B(0,2)$. The maps $F_{i}$ converge in the Gromov-Hausdorff sense to the standard embedding of $B(0,2) \subset \mathbf{C}^{N}$. It follows that $F(x)=F(y)$ but $d_{C(Y)}(x, y) \geq \epsilon$, contradicting the fact that $F$ is an embedding. This proves the claim.

It follows from the claim that the maps $f_{i}=F_{i}^{-1} \circ g_{i}$ form an equicontinuous family of maps from $A_{i}$ to $B_{i}$. Thus there exists a subsequence of $f_{i}$ converging to a map $f_{\infty}: A \rightarrow B$ under the Gromov-Hausdorff convergence $A_{i} \rightarrow A$ and $B_{i} \rightarrow B$. Let us denote the singular Kähler-Einstein metrics on $A$ and $B$ by $\omega_{A}$ and $\omega_{B}$, respectively. The proof can be concluded once we show that $f_{\infty}$ is an isometry onto its image. Since $A$ is the metric completion of its regular set $\mathcal{R}_{A}$, it is enough to show that for $x, y \in \mathcal{R}_{A}, d(x, y)=d\left(f_{\infty}(x), f_{\infty}(y)\right)$. Note that by property (1) in Definition 3.2 we have $B=B(0,2) \subset C(Y)$.

Let $\gamma$ be a minimal geodesic connecting $x, y$. By Colding-Naber [13], $\gamma$ lies entirely in $\mathcal{R}_{A}$. Let $V$ be an open set containing $\gamma$ such that the compact closure of $V$ is contained in $\mathcal{R}_{A}$, and let $V_{i} \subset A_{i}$ be the corresponding open sets converging to $V$ under the Gromov-Hausdorff convergence. On $V_{i}$ we have uniform bounds of the geometry of $\tilde{\eta}_{i}$, so by Lemma 3.3, we have bounds $\left|\nabla^{j}\left(\tilde{\eta}_{i}-f_{i}^{*} \tilde{\omega}_{i}\right)\right|<C \epsilon_{i}$ on $V_{i}$ for $j=0,1$. Letting $i \rightarrow \infty$, it follows that $f_{\infty}: V \rightarrow V^{\prime}$ is an isomorphism onto its image, and $f_{\infty}^{*} \omega_{B}=\omega_{A}$. So we have $d_{A}(x, y)=\operatorname{length}_{\omega_{A}}(\gamma)=\operatorname{length}_{\omega_{B}}\left(f_{\infty} \circ \gamma\right) \geq$ $d_{B}\left(f_{\infty}(x), f_{\infty}(y)\right)$. To prove the opposite inequality, let us now suppose that $\tilde{\gamma}$ is a minimal geodesic connecting $f_{\infty}(x)$ and $f_{\infty}(y)$. Since $B=B(0,2)$ by property (1) Definition 3.2, by Colding-Naber [13] $\tilde{\gamma}$ is contained in an open set $W$ with compact closure in the regular set of $B$. Let $W_{i}$ be open sets in $B_{i}$ corresponding to $W$ under the Gromov-Hausdorff convergence $B_{i} \rightarrow B$, and let $\gamma_{i} \subset W_{i}$ be curves converging to $\tilde{\gamma}$, with endpoints $x_{i} \rightarrow x, y_{i} \rightarrow y$. Over $W_{i}$ we have smooth convergence of the metrics $\tilde{\eta}_{i} \rightarrow \omega_{A}$ and $\tilde{\omega}_{i} \rightarrow \omega_{B}$ in the Gromov-Hausdorff sense. So we have $d_{B}\left(f_{\infty}(x), f_{\infty}(y)\right)=\operatorname{length}_{\omega_{B}}(\tilde{\gamma})=\lim _{i \rightarrow \infty} \operatorname{length}_{\tilde{\omega}_{i}}\left(\gamma_{i}\right)=\lim _{i \rightarrow \infty} \operatorname{length}_{\tilde{\eta}_{i}}\left(\gamma_{i}\right) \geq$ $\lim _{i \rightarrow \infty} d_{\tilde{\eta}_{i}}\left(x_{i}, y_{i}\right)=d_{A}(x, y)$. We have shown that $f_{\infty}$ is an isometry onto its image, so it follows that $f_{i}$ is a $\Psi\left(i^{-1}\right)$-Gromov-Hausdorff approximation. \(\square\)

The main result in this section is the following abstract decay estimate.
Proposition 3.5. There exist constants $C, \alpha, \lambda>0$ (depending on the cone $C(Y)$ ) such that for $\epsilon, r>0$ sufficiently small, we have the following. Fix a model metric $\omega_{h}$ with $\|h\| \leq \epsilon$. Let $\eta$ be another metric on $B_{\omega_{h}}(p, 2 r)$ obtained as the non-collapsed Gromov-Hausdorff limit of a sequence of polarized Kähler-Einstein manifolds. Suppose that $\eta=\omega_{h}+\sqrt{-1} \partial \bar{\partial} u$ on $B_{\omega_{h}}(p, 2 r)$ satisfies $\eta^{n}=e^{f} \omega_{h}^{n}$, and for some $\kappa<\epsilon$ we have $\operatorname{Ric}(\eta)=c \eta$ for $|c| \leq r^{-2} \kappa$, and
$$\begin{aligned}
\left|d_{\eta}-d_{\omega_{h}}\right| & <\frac{r}{100}, \\
|u| & <r^{2} \kappa, \\
|\nabla f|_{\eta} & <r^{-1} \kappa \epsilon, \\
f(p) & =0 .
\end{aligned}$$
Then we can find another model metric $\omega_{k}$ and a smooth function $u^{\prime}$ on $B_{\omega_{h}}(p, r)$ satisfying
\begin{itemize}
\item[(1)] $\omega_{h}+\sqrt{-1} \partial \bar{\partial} u=\omega_{k}+\sqrt{-1} \partial \bar{\partial} u^{\prime}$,
\item[(2)] $\|k-h\| \leq C \kappa$.
\item[(3)] $\sup _{B_{\omega_{k}}(p, 4 \lambda r)}\left|u^{\prime}\right| \leq \lambda^{2+\alpha} r^{2} \kappa$.
\end{itemize}

We remark that the advantage of working with a bound for the gradient $|\nabla f|_{\eta}$, rather than with the sup norm $|f|$, is that after scaling the gradient bound improves. At the same time, using the estimate for the distance function of $\eta$, the gradient bound together with the condition $f(p)=0$ implies a corresponding bound $|f|<$ $4 \kappa \epsilon$.

Proof. We argue by contradiction, so suppose there are $\epsilon_{i}, r_{i} \rightarrow 0, \kappa_{i}<\epsilon_{i}$ and corresponding $h_{i}, \eta_{i}, u_{i}, f_{i}$ with $\left\|h_{i}\right\| \leq \kappa_{i},\left|u_{i}\right|<r_{i}^{2} \kappa_{i},|\nabla f|_{\eta_{i}}<\kappa_{i} \epsilon_{i}$ such that no suitable $\alpha, \lambda$ exist. We will show by passing to a limit that for large enough $i$, the statement actually holds for some $\alpha, \lambda$, thus reaching a contradiction. The argument is similar to the proof of Proposition 4.1 in [34]. In the following $C>0$ will denote a uniform constant, whose value may change from line to line.

Let us scale up the metrics by defining $\tilde{\eta}_{i}=r_{i}^{-2} \eta_{i}, \omega_{i}=r_{i}^{-2} \omega_{h_{i}}$ and $\tilde{u}_{i}=r_{i}^{-2} u_{i}$. By the gradient bound for $f_{i}$ and the estimate for $\left|d_{\omega_{h_{i}}}-d_{\eta_{i}}\right|$ we see that $\left|f_{i}\right|<2 \kappa_{i} \epsilon_{i}$ on $B_{\omega_{i}}(p, 1.9)$. Note that $\tilde{u}_{i}$ satisfies
$$\left(\omega_{i}+\sqrt{-1} \partial \bar{\partial} \tilde{u}_{i}\right)^{n}=e^{f_{i}} \omega_{i}^{n},$$
with $\left|\tilde{u}_{i}\right| \leq \kappa_{i}$ on $B_{\omega_{i}}(p, 1.9)$. By Lemma 3.4, we have
$$\left|d_{\tilde{\eta}_{i}}-d_{\omega_{i}}\right|<\Psi\left(i^{-1}\right)$$
on $B_{\omega_{i}}(p, 1)$ once $i$ is sufficiently large. It follows from (3.2) and property (1) of Definition 3.2 that both $B_{\eta_{i}}(0,1)$ and $B_{\omega_{i}}(0,1)$ converge to $B(0,1)$ in the Gromov-Hausdorff sense.

By Lemma 3.3, for all sufficiently large $i$ we have $\left\|\tilde{u}_{i}\right\|_{C^{k, \alpha}(A)} \leq C_{k, A} \kappa_{i}$ on any compact subset $A$ of the regular set of $B_{\omega_{i}}(p, 1)$. So by passing to a subsequence, $\kappa_{i}^{-1} \tilde{u}_{i}$ converges locally smoothly to a function $h$ on the regular set, satisfying $|h| \leq 1$. On the other hand, writing the equation for $\tilde{u}_{i}$ in the form of Equation (3.1), we find that away from the singular set, $h$ is a harmonic function on $B(0,1)$ with respect to the cone metric $\omega_{C(Y)}=\frac{1}{2} \sqrt{-1} \partial \bar{\partial} r^{2}$. Since $|h| \leq 1$ and the singular set has codimension at least four, $h$ extends as a harmonic function across the singular set as well.

We can decompose $h$ into a sum of homogeneous harmonic functions on the cone $C(Y)$, and we write $h=h^{\leq 2}+h^{>2}$, where $h^{\leq 2}$ collects the components with at most quadratic growth and $h^{>2}$ is the rest. By Lemma 3.1 we can further decompose $h^{\leq 2}=h_{p h}+h_{\text {aut }}$, where $h_{p h}$ is pluriharmonic and $h_{\text {aut }} \in H$. Since $h_{p h}$ is pluriharmonic, $h_{p h}$ is the real part of a holomorphic function, which is a restriction of a holomorphic function on $\mathbf{C}^{N}$. Using the biholomorphisms in property (1) of Definition 3.2. it follows that $h_{p h}$ also defines a pluriharmonic function $h_{p h, i}$ on the scaled-up ball $B_{\omega_{i}}(p, 1)$ and $h_{p h, i}$ converges uniformly in the Gromov-Hausdorff sense to $h_{p h}$.

We now write down the new potential. For this let us define $k_{i}=h_{i}+\kappa_{i} h_{\text {aut }} \in H$. For sufficiently large $i$ we have $k_{i} \in U$. Consider the corresponding model metric $\omega_{k_{i}}$. By property (4) of Definition 3.2 we have $\omega_{k_{i}}=\omega_{h_{i}}+\sqrt{-1} \partial \bar{\partial} v_{i}$ with
$$\left|v_{i}\right| \leq C\left\|k_{i}-h_{i}\right\| r^{2} \leq C \kappa_{i} r^{2}$$
on $B_{\omega_{k_{i}}}(0, r)$. Let us define $\tilde{\omega}_{i}=r_{i}^{-2} \omega_{k_{i}}$. By property (3) of Definition 3.2, we have
$$\left|d_{\tilde{\omega}_{i}}-d_{\omega_{i}}\right| \leq C \epsilon_{i}$$
on $B_{\tilde{\omega}_{i}}(p, 1)$.

Now we switch our reference metric from $\omega_{h_{i}}$ to $\omega_{k_{i}}$. We have
$$\begin{aligned}
\eta_{i} & =\omega_{h_{i}}+\sqrt{-1} \partial \bar{\partial} u_{i} \\
& =\omega_{k_{i}}+\sqrt{-1} \partial \bar{\partial}\left(u_{i}-v_{i}-r_{i}^{2} \kappa_{i} h_{p h, i}\right) \\
& =\omega_{k_{i}}+\sqrt{-1} \partial \bar{\partial} u_{i}^{\prime},
\end{aligned}$$
where we define $u_{i}^{\prime}=u_{i}-v_{i}-r_{i}^{2} \kappa_{i} h_{p h, i}$. By the estimate (3.3) for $v_{i}$ and the assumption of $u_{i}$ it follows that on $B_{\omega_{h_{i}}}\left(p, 2 r_{i}\right)$ we have
$$\left|u_{i}^{\prime}\right| \leq C \kappa_{i} r_{i}^{2} .$$
By property (3) of Definition 3.2 it follows that the same estimate also holds on $B_{\omega_{k_{i}}}\left(p, r_{i}\right)$. Let us define $\tilde{u}_{i}^{\prime}=r_{i}^{-2} u_{i}^{\prime}$. Then $\kappa_{i}^{-1} \tilde{u}_{i}^{\prime}$ converges to $h^{>2}$ over compact subsets of the regular set of $B_{\tilde{\omega}_{i}}(p, 0.8)$. To see this, let $A$ be a compact subset of the regular set of $B_{\tilde{\omega}_{i}}(p, 0.8)$. Using the Gromov-Hausdorff approximations as in property (5) of Definition 3.2, we compute
$$\begin{aligned}
\left|\kappa_{i}^{-1} \tilde{u}_{i}^{\prime}-h^{>2}\right| & \leq\left|\kappa_{i}^{-1} \tilde{u}_{i}-h\right|+\left|h-r_{i}^{-2} \kappa_{i}^{-1} v_{i}-h_{p i, i}-h^{>2}\right| \\
& \leq \Psi\left(i^{-1}\right)+\left|h_{p h}-h_{p h, i}\right|+\left|r_{i}^{-2} \kappa_{i}^{-1} v_{i}-h_{a u t}\right| \\
& \leq \Psi\left(i^{-1}\right)+\kappa_{i}^{-1}\left|r_{i}^{-2} v_{i}-\kappa_{i} h_{a u t}\right| \\
& \leq \Psi\left(i^{-1}\right)+\kappa_{i}^{-1} \Psi\left(i^{-1}\right)\left|\kappa_{i} h_{a u t}\right| \\
& \leq \Psi\left(i^{-1}\right) .
\end{aligned}$$
The second inequality uses the fact that $\kappa_{i}^{-1} \tilde{u_{i}}$ converges to $h$, while the second to last inequality uses property (5) of Definition 3.2. We will show that $\tilde{u}_{i}^{\prime}$ is much smaller than $\kappa_{i}$ on a smaller ball, using that it is modeled on a harmonic function of growth rate strictly greater than 2. Away from the singular set this follows from the convergence $\kappa_{i}^{-1} \tilde{u}_{i}^{\prime} \rightarrow h^{>2}$ as shown above. To extend this estimate across the singular set we need to apply the non-concentration result in the previous section.

Let us first make precise the required decay for $h^{>2}$. Define the normalized $L^{2}$ norm of a function $f$ on a ball $B$ by $\|f\|_{B}^{2}=\operatorname{vol}(B)^{-1} \int_{B} f^{2}$. Since $h^{>2}$ has faster than quadratic growth, there is an $\alpha>0$ depending only on the cone $C(Y)$ such that
$$\left\|h^{>2}\right\|_{B(0,16 r)} \leq C r^{2+2 \alpha}\left\|h^{>2}\right\|_{B(0,1)}$$
for any small $r>0$. By the mean value inequality for harmonic functions,
$$\sup _{B(0,8 r)}\left|h^{>2}\right| \leq C\left\|h^{>2}\right\|_{B(0,16 r)} \leq C r^{2+2 \alpha} .$$
We think of $r$ as fixed, to be chosen below.
To apply the non-concentration result in the previous section, we need to work with respect to $\tilde{\eta}_{i}$ instead of $\tilde{\omega}_{i}$, since $\tilde{\omega}_{i}$ in general is not a Gromov-Hausdorff limit, while $\tilde{\eta}_{i}$ is. By property (3) of Definition 3.2 and the estimate (3.2), we see that for $i$ sufficiently large, on $B_{\tilde{\eta}_{i}}(p, 1)$ we have
$$\left|d_{\tilde{\eta}_{i}}-d_{\tilde{\omega}_{i}}\right|<r .$$

Let us now scale up by $(16 r)^{-1}$, replacing $\tilde{\omega}_{i}$ by $(16 r)^{-2} \tilde{\omega}_{i}$ and $\tilde{\eta}_{i}$ by $(16 r)^{-2} \tilde{\eta}_{i}$. Define $U_{i}^{\prime}=(16 r)^{-2} r_{i}^{-2} u_{i}^{\prime}$. From (3.5) we have $\left|U_{i}^{\prime}\right| \leq C \kappa_{i} r^{-2}$ on $B_{\tilde{\omega}_{i}}(p, 2)$. So by (3.6) we have $\left|U_{i}^{\prime}\right| \leq C \kappa_{i} r^{-2}$ on $B_{\tilde{\eta}_{i}}(p, 1)$. Let $r_{h}$ denote the harmonic radius of $\tilde{\omega}_{i}$,
and let $\delta>0$, whose value is to be determined later. On $\left\{r_{h}>\delta\right\}, U_{i}^{\prime}$ converges smoothly to $(16 r)^{-2} \kappa_{i} h^{>2}$. So on $\left\{r_{h}>\delta\right\} \cap B_{\tilde{\omega}_{i}}(p, 2)$ we have
$$\left|U_{i}^{\prime}\right|<C r^{2 \alpha} \kappa_{i} .$$
Let $\tilde{r}_{h}$ be the harmonic radius of the metric $\tilde{\eta}_{i}$. By Lemma 3.3, for $i$ sufficiently large we have $\left\{\tilde{r}_{h}>2 \delta\right\} \subset\left\{r_{h}>\delta\right\}$. It follows that
$$\sup _{B_{\tilde{\eta}_{i}}(p, 1) \cap\left\{\tilde{r}_{h}>2 \delta\right\}}\left|U_{i}^{\prime}\right| \leq C r^{2 \alpha} \kappa_{i} .$$

Note that on $B_{\tilde{\eta}_{i}}(p, 1)$, using property (2) of Definition 3.2 we see that $U_{i}^{\prime}$ satisfies the equation
$$\left(\tilde{\eta}_{i}-\sqrt{-1} \partial \bar{\partial} U_{i}^{\prime}\right)^{n}=e^{-f_{i}} \tilde{\eta}_{i}^{n},$$
and we have $\left|f_{i}\right|<2 \kappa_{i} \epsilon_{i}$. We are now ready to apply the non-concentration theorem, Theorem 2.1. Given $\gamma>0$, Theorem 2.1 implies that there exists $\delta>0$ such that
$$\begin{aligned}
\sup _{B_{\tilde{\eta}_{i}}(p, 0.5)}\left|U_{i}^{\prime}\right| & \leq C\left(\sup _{B_{\tilde{\eta}_{i}}(p, 1) \cap\left\{\tilde{r}_{h}>2 \delta\right\}}\left|U_{i}^{\prime}\right|+\sup _{B_{\tilde{\eta}_{i}}(p, 1)}\left|f_{i}\right|+\gamma \sup _{B_{\tilde{\eta}_{i}}(p, 1)}\left|U_{i}^{\prime}\right|\right) \\
& \leq C\left(\kappa_{i} r^{2 \alpha}+\kappa_{i} \epsilon_{i}+\gamma \kappa_{i} r^{-2}\right) .
\end{aligned}$$
Choosing $\gamma=r^{2+2 \alpha}$ and $i$ sufficiently large so that also $\epsilon_{i} \leq r^{2 \alpha}$, we then have
$$\sup _{B_{\tilde{\eta}_{i}}(p, 0.5)}\left|U_{i}^{\prime}\right| \leq C \kappa_{i} r^{2 \alpha} .$$
Scaling back this estimate, we find that for sufficiently large $i$ (depending on $r$ ), we have
$$\sup _{B_{\tilde{\eta}_{i}}(p, 8 r)}\left|U_{i}^{\prime}\right| \leq C \kappa_{i} r^{2+2 \alpha} .$$
By the distance estimates (3.2) and (3.4) it follows that
$$\sup _{B_{\tilde{\omega}_{i}}(p, 4 r)}\left|U_{i}^{\prime}\right| \leq C \kappa_{i} r^{2+2 \alpha}$$
once $i$ is sufficiently large. We can now choose $r=\lambda$ small enough so that
$$\sup _{B_{\tilde{\omega}_{i}}(p, 4 \lambda)}\left|U_{i}^{\prime}\right| \leq \kappa_{i} \lambda^{2+\alpha} .$$
Scaling down by $r_{i}$, we get
$$\sup _{B_{\omega_{k_{i}}}\left(p, 4 \lambda r_{i}\right)}\left|u_{i}^{\prime}\right| \leq \kappa_{i} \lambda^{2+\alpha} r_{i}^{2} .$$
This gives the required contradiction. \(\square\)

We can now state the abstract convergence result. To do so, we need the following definition. Recall that $Z$ is a non-collapsed Gromov-Hausdorff limit of polarized Kähler-Einstein manifolds, $\omega_{Z}$ is the singular Kähler-Einstein metric on $Z, p \in Z$, and the tangent cone at $p$ is $C(Y)$. Assume that $\mathcal{U}$ is a neighborhood of $p$, and on $\mathcal{U}$ there is a family $\mathcal{F}$ of model metrics.

Definition 3.6. We say that $\omega_{Z}$ can be approximated by $\mathcal{F}$ if the following holds. Fix any $0<\kappa<\epsilon$. Then for all $r>0$ sufficiently small, there exist $\Lambda>0$ and an embedding $F: B_{\omega}(p, 2 r) \subset \mathcal{U} \rightarrow Z$ from the ball with respect to $\omega=\omega_{0} \in \mathcal{F}$ such that $F(p)=0$ with the following properties. Let $\eta=\Lambda F^{*} \omega_{Z}$. Then on $B_{\omega}(p, 2 r)$, the following hold:
\begin{itemize}
\item[(1)] $\operatorname{Ric}(\eta)=c \eta$ with $|c|<r^{-2} \epsilon$.
\item[(2)] $\eta^{n}=e^{f} \omega^{n}$ and $\eta=\omega+\sqrt{-1} \partial \bar{\partial} u$, with
$$|u|<r^{2} \kappa, \quad f(p)=0, \quad|\nabla f|_{\eta}<r^{-1} \kappa \epsilon .$$
\item[(3)] $\left|d_{\eta}-d_{\omega}\right|<r / 100$.
\end{itemize}

Proposition 3.7. Suppose that at $p \in Z, \omega_{Z}$ can be approximated by a family of $\mathcal{F}$ of model metrics in a neighborhood $\mathcal{U} \subset Z$ of $p$. Then for some $r_{0}>0$, there is a model metric $\omega \in \mathcal{F}$ and a holomorphic embedding $F: B_{\omega}\left(p, r_{0}\right) \rightarrow Z$, with $F(p)=p$, and constants $\Lambda, C, \alpha>0$, such that
$$\Lambda F^{*} \omega_{Z}=\omega+\sqrt{-1} \partial \bar{\partial} u_{r}$$
for some $u_{r}$ defined on $B_{\omega}(p, r)$, and
$$\sup _{B_{\omega}(p, r)}\left|u_{r}\right| \leq C r^{2+\alpha}$$
for all $r<r_{0}$.
Proof. We iterate the decay estimate, Proposition 3.5, as well as the distance estimate, Lemma 3.4. Let $C, \alpha$ and $\lambda$ be the constants in Proposition 3.5, and let $\epsilon, r$ be sufficiently small so that both Lemma 3.4 and Proposition 3.5 hold. At the initial stage we let $\kappa<C^{-1}\left(1-\lambda^{\alpha}\right) \epsilon$. Exactly how small $\epsilon$ should be will be clear later. By letting $r$ be smaller if necessary (depending on $\kappa, \epsilon$ ), we have the corresponding approximation $F: B_{\omega}(p, 4 r) \rightarrow Z$, where $\omega=\omega_{0} \in \mathcal{F}$, with constant $\Lambda>0$. Write $\eta=\Lambda F^{*} \omega_{Z}$. Then Lemma 3.4 implies that we have $\left|d_{\eta}-d_{\omega}\right|<\lambda r / 200$ on the ball $B_{\omega}(p, 2 r)$. We write $h_{0}=0$.

Applying Proposition 3.5 we have a model metric $\omega_{1}=\omega_{h_{1}}$, with $\left\|h_{1}\right\| \leq C \kappa \leq \epsilon$, and a function $u_{1}$ on $B_{\omega}(p, r)$ such that $\eta=\omega_{h_{1}}+\sqrt{-1} \partial \bar{\partial} u_{1}$, and
$$\sup _{B_{\omega}(p, 4 \lambda r)}\left|u_{1}\right| \leq \lambda^{2+\alpha} r^{2} \kappa .$$
By property (3) of Definition 3.2, it follows that
$$\sup _{B_{\omega_{1}}(p, 2 \lambda r)}\left|u_{1}\right| \leq \lambda^{2+\alpha} r^{2} \kappa .$$
Also by property (3) of Definition 3.2, on $B_{\omega_{1}}(p, 2 \lambda r)$ we have
$$\left|d_{\omega_{0}}-d_{\omega_{1}}\right| \leq C_{1}\left(\left\|h_{1}\right\|+\left\|h_{0}\right\|\right) \lambda r \leq 2 C_{1} \epsilon \lambda r \leq \frac{\lambda r}{200}$$
if we choose $\epsilon$ to be sufficiently small. Consequently, on $B_{\omega_{1}}(p, 2 \lambda r)$ we have
$$\left|d_{\eta}-d_{\omega_{1}}\right| \leq\left|d_{\eta}-d_{\omega}\right|+\left|d_{\omega}-d_{\omega_{1}}\right| \leq \frac{\lambda r}{100} .$$
The metrics $\eta$ and $\omega_{1}$ now satisfy the conditions of Lemma 3.4 and Proposition 3.5 with $r$ replaced by $\lambda r$ and $\kappa$ by $\lambda^{\alpha} \kappa$. We can iterate this construction and we obtain
a sequence of model metrics $\omega_{i}=\omega_{h_{i}}$ with $\left\|h_{i+1}-h_{i}\right\| \leq C\left(\lambda^{\alpha}\right)^{i} \kappa$ such that on $B_{\omega_{i}}\left(p, 2 \lambda^{i} r\right)$ we have $\eta=\omega_{i}+\sqrt{-1} \partial \bar{\partial} u_{i}$ with
$$\sup _{B\left(p, 2 \lambda^{i} r\right)}\left|u_{i}\right| \leq\left(\lambda^{i}\right)^{2+\alpha} \kappa r^{2} .$$

The harmonic functions $h_{i}$ converge to a harmonic function $k$ satisfying $\|k\| \leq \epsilon$, so $k \in U$ if $\epsilon$ is chosen small enough. Let $\tilde{\omega}=\omega_{k}$ be the corresponding model metric. By property (4) of Definition 3.2, there exists $v_{i}$ on $B_{\tilde{\omega}}(0,1)$ such that
$$\omega_{i}-\tilde{\omega}=\sqrt{-1} \partial \bar{\partial} v_{i},$$
with
$$\sup _{B_{\tilde{\omega}}\left(p, \lambda^{i} r\right)}\left|v_{i}\right| \leq C_{2}\left\|k-h_{i}\right\|\left(\lambda^{i} r\right)^{2} \leq C_{3}\left(\lambda^{i}\right)^{2+\alpha} r^{2} \kappa .$$
So on $B_{\tilde{\omega}}\left(0, \lambda^{i} r\right)$ we have
$$\eta=\omega_{i}+\sqrt{-1} \partial \bar{\partial} u_{i}=\tilde{\omega}+\sqrt{-1} \partial \bar{\partial}\left(u_{i}+v_{i}\right)=\tilde{\omega}+\sqrt{-1} \partial \bar{\partial} \tilde{u}_{i},$$
where $\tilde{u}_{i}=u_{i}+v_{i}$. Then $\tilde{u}_{i}$ satisfies
$$\sup _{B_{\tilde{\omega}}\left(0, \lambda^{i} r\right)}\left|\tilde{u}_{i}\right| \leq\left(1+C_{3}\right) \kappa\left(\lambda^{i}\right)^{2+\alpha} r^{2} \leq C^{\prime}\left(\lambda^{i} r\right)^{2+\alpha},$$
where $C^{\prime}=\left(1+C_{3}\right) \kappa r^{-\alpha}$, and so $\tilde{\omega}$ and $\tilde{u}_{i}$ are as required. \(\square\)

\section*{4. K-polystable singularities}

Suppose, as above, that $(Z, p)$ is the non-collapsed pointed Gromov-Hausdorff limit of a sequence of polarized Kähler-Einstein manifolds, with its singular Kähler-Einstein metric denoted by $\omega_{Z}$. Let $C(Y)$ denote the metric tangent cone to $Z$ at $p$. In this section we assume that the germ $(Z, p)$ is isomorphic to the germ $(C(Y), o)$, where $o$ is the vertex of the cone $C(Y)$. In particular this means that the affine variety $C(Y)$, equipped with the homothetic vector field $\xi$ induced by the cone structure defines a K-polystable Fano cone singularity $(C(Y), \xi)$ in the terminology of Li-Wang-Xu [27].

In this section we prove our first main result, Theorem 1.1. by reducing it to Proposition 3.7. For this we need to construct a family $\mathcal{F}$ of model metrics on $C(Y)$ and then show that the Gromov-Hausdorff limit $\omega_{Z}$ can be approximated by $\mathcal{F}$.

The construction of $\mathcal{F}$ is fairly simple, since the model space $C(Y)$ is already a cone. Let $H$ denote the space of quadratic harmonic functions $h$ such that $\nabla h$ generates a biholomorphism which commutes with scaling (see Lemma 3.1). For $h \in H$, let $\phi(t)$ be the one-parameter group of biholomorphisms generated by $\frac{1}{2} \nabla h$. By the gradient estimate and $h$ being homogeneous with quadratic growth, we have
$$\sup _{B_{C(Y)}(0, r)}|\nabla h|_{\omega_{C(Y)}} \leq C \sup _{B_{C(Y)}(0,2 r)}|h| r^{-1} \leq C\|h\| r$$
for all $r>0$. Let $g=\phi(1)$ and define $\omega_{h}=g^{*} \omega_{C(Y)}$.
Lemma 4.1. There exists a neighborhood $0 \in U \subset H$ such that $\mathcal{F}=\left\{\omega_{h} \mid h \in U\right\}$ is a family of model metrics.

Proof. For simplicity let us write $\omega=\omega_{C(Y)}$. We verify the properties in Definition 3.2. Property (1) is automatic since $C(Y)$ is a cone itself. Property (2) is satisfied since the automorphism $g$ is generated by $\nabla h$ for a harmonic function $h$.

Let us consider property (3). Let $x, y \in B(0, r)$ be regular points. By differentiating $d_{\omega}(0, \phi(t) x)$ and using (4.1), we see that
$$d_{\omega}(0, \phi(t) x) \leq e^{C\|h\| t} d_{\omega}(0, x) .$$
Similarly, by differentiating $d_{\omega}(x, \phi(t) x)$ and using (4.1) and (4.2) we see that
$$d_{\omega}(x, g x) \leq C\left(e^{C\|h\|}-1\right) d_{\omega}(0, x) \leq C\|h\| d_{\omega}(0, x) .$$
For $x, y \in B_{\omega}(0, r)$, the triangle inequality together with (4.3) gives
$$\left|d_{\omega}(g x, g y)-d_{\omega}(x, y)\right| \leq\left|d_{\omega}(x, g x)+d_{\omega}(y, g y)\right| \leq C\|h\|\left(d_{\omega}(0, x)+d_{\omega}(0, y)\right) .$$
This proves property (3).
To see property (4), recall that $\omega$ as a cone metric is given by $\omega=\sqrt{-1} \partial \bar{\partial}\left(r^{2} / 2\right)$, where $r$ is the distance to the vertex 0. Differentiating $\phi(t)^{*} r^{2}$ and using (4.2), we get
$$\left|g^{*} r^{2}-r^{2}\right| \leq C\|h\| r^{2} .$$
Now, let $g_{h}$ and $g_{k}$ denote the automorphisms generated by $h$ and $k$, respectively. Define
$$u=g_{k}^{*} r^{2}-g_{h}^{*} r^{2}=g_{k}^{*}\left(r^{2}-g^{*} r^{2}\right),$$
where $g=g_{h} g_{k}^{-1}$. By standard Lie theory, for sufficiently small $h, k$, we have $g=g_{\tilde{h}}$ for some $\tilde{h} \in H$ with $\tilde{h}=h-k+O(\|h-k\|\|h\|)$. Then (4.2) and (4.4) together imply that
$$|u|=\left|g_{k}^{*}\left(r^{2}-g^{*} r^{2}\right)\right| \leq C\|h-k\| g_{k}^{*} r^{2} \leq C\|h-k\| r^{2}$$
once $h, k$ are sufficiently small. Since $\omega_{k}=\omega_{h}+\sqrt{-1} \partial \bar{\partial} u$, this proves property (4) of Definition 3.2 for a sufficiently small neighborhood $U$ of $0 \in H$.

Finally, let us prove (5). Fix $K$ a compact set in the regular set of $B(0,1)$. Let $r_{i} \rightarrow 0$ and $h_{i}, k_{i} \in H$ such that $\left\|h_{i}\right\|,\left\|k_{i}\right\| \rightarrow 0$. Let $K_{i}$ be compact sets in the regular set of $B_{r_{i}^{-2} \omega_{h_{i}}}(0,1)$ converging to $K$ in the Gromov-Hausdorff sense. Since $\omega_{h_{i}}$ is a cone metric, we may work as if $r_{i}=1$. Thus on $B_{\omega_{h_{i}}}(0,1)$ we can simply take $K_{i}=g_{i}^{-1} K$. To simplify the notations we suppress the subscript $i$ in what follows. Let $\phi(t)$ and $\psi(t)$ be the flows of $\nabla h$ and $\nabla k$, respectively, and set $g_{h}=\phi(1)$ and $g_{k}=\psi(1)$. Then we have $\omega_{k}=\omega_{h}+\sqrt{-1} \partial \bar{\partial} u$ with $u=g_{k}^{*}\left(r^{2} / 2\right)-g_{h}^{*}\left(r^{2} / 2\right)$. If $\|h\|,\|k\|$ are sufficiently small (depending on $K$ ), then we can expand $\psi(t)^{*} r^{2}$ and $\phi(t)^{*} r^{2}$ as power series in $t$ for $t \in[0,1]$, whose coefficients depend on $\nabla h, \nabla k$ and the derivatives of $r^{2}$. As a consequence we have an estimate of the form
$$\left|g_{h}^{*} r^{2}-r^{2}-\frac{1}{2} \nabla h\left(r^{2}\right)\right| \leq C|\nabla h|_{\omega_{h}}^{2} \leq C\|h\|^{2}$$
on $K$, where the last inequality follows from (4.1). Note that since $h$ is homogeneous with degree two, we have $\nabla h\left(r^{2}\right)=4 h$.

Now, if $h, k$ are sufficiently small, we have $\tilde{h} \in H$ as above. Using (4.5), we compute
$$\begin{aligned}
\left|g_{k}^{*} r^{2}-g_{h}^{*} r^{2}-2(k-h)\right| & \leq g_{k}^{*}\left|r^{2}-g_{\tilde{h}}^{*} r^{2}+2 \tilde{h}\right|+2\left|(h-k)-g_{k}^{*} \tilde{h}\right| \\
& \leq C\|\tilde{h}\|^{2}+C\|h-k\|\|h\| \\
& \leq \epsilon\|h-k\|
\end{aligned}$$
for any $\epsilon>0$ once $h, k$ are sufficiently small. This proves (5). \(\square\)

It remains to show that $\omega_{Z}$ can be approximated by $\mathcal{F}$. As in Donaldson-Sun [18], we let $\lambda=1 / \sqrt{2}$, and let $\left(Z_{i}, p_{i}\right)$ denote $(Z, p)$ scaled up by a factor of $\lambda^{-i}$, which is still a pointed Gromov-Hausdorff limit of polarized Kähler-Einstein manifolds. Let $B_{i}$ denote the unit ball around $p_{i}$, i.e. the ball $B\left(p, \lambda^{i}\right)$ scaled up to unit size. Let us denote the unit ball in $C(Y)$ by $B$, and let $F_{\infty}: B \rightarrow \mathbf{C}^{N}$ be an embedding given by an $L^{2}$-orthonormal set of homogeneous functions. Using this embedding we will also view $C(Y) \subset \mathbf{C}^{N}$. Since $C(Y)$ is the tangent cone at $p$, we have $B_{i} \rightarrow B$ in the Gromov-Hausdorff sense. We choose distance functions on the disjoint unions $B_{i} \sqcup B$ realizing the Gromov-Hausdorff convergence.

Proposition 4.2. For sufficiently large $i$ we have holomorphic maps $F_{i}: B_{i} \rightarrow \mathbf{C}^{N}$ satisfying the following properties, where $\Psi\left(i^{-1}\right)$ denotes a function converging to zero as $i \rightarrow \infty$.
\begin{itemize}
\item[(1)] Under the Gromov-Hausdorff approximations between $B_{i}$ and $B$ we have $\left|F_{i}-F_{\infty}\right|<\Psi\left(i^{-1}\right)$, and the image $F_{i}\left(B_{i}\right) \subset C(Y)$.
\item[(2)] Let $\omega_{i}=\left(F_{i}^{-1}\right)^{*}\left(\lambda^{-2 i} \omega_{Z}\right)$ denote the metric on the image $F_{i}\left(B_{i}\right)$ induced by $\lambda^{-2 i} \omega_{Z}$. Then we have $\operatorname{Ric}\left(\omega_{i}\right)=c_{i} \omega_{i}$ for some $\left|c_{i}\right|<\Psi\left(i^{-1}\right)$, and the distance functions $d_{\omega_{i}}, d_{\omega_{C(Y)}}$ satisfy $\left|d_{\omega_{i}}-d_{\omega_{C(Y)}}\right|<\Psi\left(i^{-1}\right)$.
\item[(3)] We have $\omega_{i}^{n}=e^{f_{i}} \omega_{C(Y)}^{n}$ and $\omega_{i}=\omega_{C(Y)}+\sqrt{-1} \partial \bar{\partial} u_{i}$ with $f_{i}(0)=0$ and $\left|\nabla f_{i}\right|_{\omega_{i}},\left|u_{i}\right|<\Psi\left(i^{-1}\right)$.
\end{itemize}
In particular $\omega_{Z}$ can be approximated by $\mathcal{F}$ in the sense of Definition 3.6.
Proof. Let $\mathcal{O}_{p}$ be the ring of germs of holomorphic functions on $Z$ at $p$. As in Donaldson-Sun [18], for $f \in \mathcal{O}_{p}$ we can define
$$d_{K E}(f)=\lim _{r \rightarrow 0} \frac{\sup _{B(p, r)} \log |f|}{\log r} .$$
By Li-Xu [28, Theorem 1.4], $d_{K E}$ is the unique $K$-semistable valuation in $\operatorname{Val}_{Z, p}$. On the other hand, $C(Y)$ admits a Ricci-flat Kähler cone metric, and so the homothetic scaling on $C(Y)$ gives rise to a $K$-polystable valuation by Li-Wang-Xu [27, Corollary A.4], which in particular is $K$-semistable. It follows that these two valuations coincide.

The coordinate ring $R(C(Y))$ is a sum of the homogeneous pieces
$$R(C(Y))=\bigoplus_{k \geq 0} R_{d_{k}}(C(Y)),$$
where $R_{d_{k}}$ is the degree $d_{k}$ piece under the homothetic action. Let us suppose that $R(C(Y))$ is generated by the functions of degree less than $D$, and let $k_{0}=\max \{k \geq$ $\left.0 \mid d_{k}<D\right\}$. We have a subspace $P \subset \mathcal{O}_{p}$, and an adapted sequence of bases for $P$ as in [18, Section 3.2], which for sufficiently large $i$ define holomorphic embeddings $F_{i}$ : $B_{i} \rightarrow \mathbf{C}^{N}$. Under the Gromov-Hausdorff convergence $B_{i} \rightarrow B \subset C(Y)$, the maps
$F_{i}$ converge to an embedding $B \rightarrow \mathbf{C}^{N}$ using an $L^{2}$-orthonormal set of homogeneous functions in $R(C(Y))$ and up to modifying our maps by unitary transformations we can assume that this embedding of $B$ coincides with our embedding $F_{\infty}$. We will denote the $L^{2}$-norm of functions on $B_{i}$ by $\|\cdot\|_{i}$.

Recall that the adapted sequence of bases are bases $\left\{G_{i}^{1}, \ldots, G_{i}^{m}\right\}$ of $P$ satisfying the following:
\begin{itemize}
\item[-] The $L^{2}$ norm on $B_{i}$ satisfies $\left\|G_{i}^{a}\right\|_{i}=1$, and $\left\langle G_{i}^{a}, G_{i}^{b}\right\rangle_{i} \rightarrow 0$ as $i \rightarrow \infty$.
\item[-] We have $G_{i}^{a}=\mu_{i a}^{-1} G_{i-1}^{a}+p_{i}^{a}$, with $\left\|p_{i}^{a}\right\|_{i} \rightarrow 0$ as $i \rightarrow \infty$.
\item[-] $\mu_{i a} \rightarrow \lambda^{d_{a}}$ as $i \rightarrow \infty$.
\end{itemize}

For each $a, i$ we can write
$$G_{i}^{a}=g_{i}^{a}+k_{i}^{a},$$
where $g_{i}^{a}$ is homogeneous of degree $d_{a}$ and $k_{i}^{a}$ has strictly greater degree. There exists an $\epsilon>0$ such that for all $a, i$ we have $d\left(k_{i}^{a}\right)>d_{a}+\epsilon$. Let us also decompose $p_{i}^{a}=\left(p_{i}^{a}\right)_{d_{a}}+\left(p_{i}^{a}\right)_{>d_{a}}$ into the homogeneous degree $d_{a}$ piece, and the remainder. We then have
$$G_{i}^{a}=\mu_{i a}^{-1}\left(g_{i-1}^{a}+k_{i-1}^{a}\right)+p_{i}^{a},$$
and so
$$\begin{aligned}
& g_{i}^{a}=\mu_{i a}^{-1} g_{i-1}^{a}+\left(p_{i}^{a}\right)_{d_{a}}, \\
& k_{i}^{a}=\mu_{i a}^{-1} k_{i-1}^{a}+\left(p_{i}^{a}\right)_{>d_{a}} .
\end{aligned}$$
Since $d\left(k_{i-1}^{a}\right)>d_{a}+\epsilon$ and $\mu_{i a} \rightarrow \lambda^{d_{a}}$, for sufficiently large $i$ we have
$$\left\|\mu_{i a}^{-1} k_{i-1}^{a}\right\|_{i} \leq \mu_{i a}^{-1} \lambda^{d_{a}+\epsilon / 2}\left\|k_{i-1}^{a}\right\|_{i-1} \leq \lambda^{\epsilon / 4}\left\|k_{i-1}^{a}\right\|_{i-1} .$$
It follows that $\left\|k_{i}^{a}\right\| \rightarrow 0$ as $i \rightarrow \infty$, and so if we define the functions $\tilde{F}_{i}$ to have components $g_{i}^{a}$, then $\sup _{B_{i}}\left|F_{i}-\tilde{F}_{i}\right| \rightarrow 0$. Therefore the $\tilde{F}_{i}$ also give embeddings of $B_{i}$ converging to the embedding $F_{\infty}$ of $B$.

We claim that further modifying the $\tilde{F}_{i}$ by elements in $G L(N)$ converging to the identity, and commuting with the homothetic action on $C(Y)$, we can assume that $\tilde{F}_{i}\left(B_{i}\right) \subset C(Y) \subset \mathbf{C}^{N}$. To see this, recall that the homothetic action on $C(Y)$ generates the algebraic action of a complex torus $T$ on $C(Y)$, which we can assume is given by a linear action on $\mathbf{C}^{N}$. By our construction each $F_{i}\left(B_{i}\right)$ lies in the image $g_{i} C(Y)$ of the cone by a matrix $g_{i} \in G L(N)^{T}$ commuting with $T$. We need to show that there are elements $h_{i} \in G L(N)^{T}$ converging to the identity such that $h_{i} g_{i} C(Y)=C(Y)$. Since $C(Y)$ admits a Ricci flat Kähler cone metric, the group of linear automorphisms of $C(Y)$ commuting with $T$ is reductive (see Donaldson-Sun [18]). Using this, we can apply the variant of Luna's slice theorem shown in Donaldson [16, Proof of Proposition 1] to the multigraded Hilbert scheme. In this Hilbert scheme we have $g_{i} C(Y) \rightarrow C(Y)$, and therefore there are some $h_{i} \rightarrow 1$ in $G L(N)^{T}$ such that $h_{i} g_{i} C(Y)$ lie in the slice at $C(Y)$. The orbit of $C(Y)$ can only meet the slice at finitely many points near $C(Y)$, therefore for sufficiently large $i$ we have $h_{i} g_{i} C(Y)=C(Y)$. Replacing the $F_{i}$ by $h_{i} \circ \tilde{F}_{i}$ we now have embeddings $F_{i}$ of the $B_{i}$, satisfying Condition (1) in the statement of the Proposition.

Regarding Condition (2), the estimate for the Ricci curvature is immediate since by construction $\operatorname{Ric}\left(\omega_{i}\right)=c \lambda^{2 i} \omega_{i}$ for some $|c| \leq 1$. The estimate $\left|d_{\omega_{i}}-d_{\omega_{C(Y)}}\right|<$ $\Psi\left(i^{-1}\right)$ follows from the estimate $\left|F_{i}-F_{\infty}\right|<\Psi\left(i^{-1}\right)$. More precisely, for any $\epsilon>0$ we need to show that for sufficiently large $i$ we have $\left|d_{\omega_{i}}-d_{\omega_{C(Y)}}\right|<\epsilon$. Let
$x, y \in F_{i}\left(B_{i}\right)$, so that $x=F_{i}\left(x_{i}\right), y=F_{i}\left(y_{i}\right)$. We can find $x_{i}^{\prime}, y_{i}^{\prime} \in B$ such that under the Gromov-Hausdorff approximations we have $d\left(x_{i}, x_{i}^{\prime}\right), d\left(y_{i}, y_{i}^{\prime}\right)<\Psi\left(i^{-1}\right)$, and then $\left|x-F_{\infty}\left(x_{i}^{\prime}\right)\right|,\left|y-F_{\infty}\left(y_{i}^{\prime}\right)\right|<\Psi\left(i^{-1}\right)$ by Condition (1). At the same time we also have points $x^{\prime}, y^{\prime} \in B$ such that $x=F_{\infty}\left(x^{\prime}\right), y=F_{\infty}\left(y^{\prime}\right)$. Our goal is to show that $\left|d_{B}\left(x^{\prime}, y^{\prime}\right)-d_{B_{i}}\left(x_{i}, y_{i}\right)\right|<\epsilon$ if $i$ is sufficiently large (independent of $x, y$ ), where we are emphasizing that we are taking the distance with respect to the $\omega_{C(Y)}$ and $\omega_{i}$ metrics by writing $d_{B}, d_{B_{i}}$. Using the metrics on $B_{i} \sqcup B$ realizing the Gromov-Hausdorff convergence, we have
$$\begin{aligned}
\left|d_{B}\left(x^{\prime}, y^{\prime}\right)-d_{B_{i}}\left(x_{i}, y_{i}\right)\right| & \leq d_{B}\left(x_{i}^{\prime}, x^{\prime}\right)+d_{B}\left(y_{i}^{\prime}, y^{\prime}\right)+d\left(x_{i}, x_{i}^{\prime}\right)+d\left(y_{i}, y_{i}^{\prime}\right) \\
& \leq d_{B}\left(x_{i}^{\prime}, x^{\prime}\right)+d_{B}\left(y_{i}^{\prime}, y^{\prime}\right)+\Psi\left(i^{-1}\right) .
\end{aligned}$$
Finally to see that $d_{B}\left(x_{i}^{\prime}, x^{\prime}\right)$ is small for large $i$, we can use that $\left|F_{\infty}\left(x_{i}^{\prime}\right)-F_{\infty}\left(x^{\prime}\right)\right|<$ $\Psi\left(i^{-1}\right)$ and the fact that $F_{\infty}^{-1}$ is uniformly continuous. It follows that for sufficiently large $i$ we have $d_{B}\left(x_{i}^{\prime}, x^{\prime}\right)<\epsilon / 2$, and the same holds for $d_{B}\left(y_{i}^{\prime}, y^{\prime}\right)$. Combining these results, we get $\left|d_{B}\left(x^{\prime}, y^{\prime}\right)-d_{B_{i}}\left(x_{i}, y_{i}\right)\right|<\epsilon$ for large $i$ as required.