---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: Estimates_for_the_Complex_Monge-Ampère_Equation_on_Hermitian_and_Balanced_Manifo_1300a92025f8.pdf
converter: mathpix
format: mmd
---

\title{
ESTIMATES FOR THE COMPLEX MONGE-AMPÈRE EQUATION ON HERMITIAN AND BALANCED MANIFOLDS*
}

\author{
VALENTINO TOSATTI ${ }^{\dagger}$ AND BEN WEINKOVE ${ }^{\ddagger}$
}

\begin{abstract}
We generalize Yau's estimates for the complex Monge-Ampère equation on compact manifolds in the case when the background metric is no longer Kähler. We prove $C^{\infty}$ a priori estimates for a solution of the complex Monge-Ampère equation when the background metric is Hermitian (in complex dimension two) or balanced (in higher dimensions), giving an alternative proof of a theorem of Cherrier. We relate this to recent results of Guan-Li.
\end{abstract}

Key words. Complex Monge-Ampère equation, Hermitian manifold, balanced manifold.

AMS subject classifications. Primary 32W20; Secondary 53C55, 32Q25
1. Introduction. Let $(M, g)$ be a compact Hermitian manifold of complex dimension $n \geq 2$. Write $\omega$ for the real (1, 1)-form
$$\omega=\sqrt{-1} \sum_{i, j} g_{i \bar{j}} d z^{i} \wedge d \overline{z^{j}}$$
We consider the complex Monge-Ampère equation
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{F} \omega^{n}, \quad \text { with } \quad \omega+\sqrt{-1} \partial \bar{\partial} \varphi>0,$$
for a real-valued function $\varphi$, where $F$ is a given smooth real-valued function. Since (1.1) is invariant under the addition of constants to $\varphi$, we may assume for convenience that $\varphi$ satisfies the normalization condition,
$$\sup _{M} \varphi=0 .$$
When $\omega$ is Kähler (that is, $d \omega=0$ ), Calabi [Ca1] showed that solutions $\varphi$ to (1.1), (1.2), are unique. In fact, the same proof (see Remark 5.1 below) shows that this result can be extended for general Hermitian $\omega$.

In the seminal paper [Ya], Yau showed in the Kähler case that one can find a smooth solution $\varphi$ of (1.1) whenever $F$ satisfies the necessary condition
$$\int_{M} e^{F} \omega^{n}=\int_{M} \omega^{n} .$$
Yau proved this result using the continuity method. The problem easily reduces to proving uniform $C^{\infty}$ a priori estimates for a smooth solution $\varphi$ of (1.1), depending only on $(M, g)$ and $F$. It is natural to ask: to what extent can Yau's results be generalized to the case when $\omega$ is no longer Kähler?

\footnotetext{
*Received October 19, 2009; accepted for publication December 21, 2009. Research supported in part by National Science Foundation grant DMS-08-48193. The second-named author is also supported in part by a Sloan Foundation fellowship.
${ }^{\dagger}$ Mathematics Department, Columbia University, 2990 Broadway, New York, NY 10027, USA (tosatti@math.columbia.edu).
${ }^{\ddagger}$ Mathematics Department, University of California, San Diego, 9500 Gilman Drive \#0112, La Jolla CA 92093, USA (weinkove@math.ucsd.edu).
}

The current paper was motivated by the recent interesting work of B. Guan and Q. Li. In [GL], Guan-Li made a number of important advances, including the result that
$$\partial \bar{\partial} \omega^{k}=0, \quad k=1,2,$$
is a sufficient condition for solving equation (1.1). Note that (1.4) implies that $\partial \bar{\partial} \omega^{k}=0$ for all $1 \leq k \leq n-1$ (see, for example, [FT]). Also, Guan-Li apply their estimates to the problem of finding geodesics in the space of Hermitian metrics via the homogeneous complex Monge-Ampère equation (for some related works, see [CLN, BT, Ma, Se, Do1, GuB, Chn, GuP, PS], for example).

We focus now on the question of obtaining a priori estimates for solutions $\varphi$ of (1.1). In complex dimension two, we show that no assumption on $(M, \omega)$ is needed to obtain the a priori estimates. In higher dimensions we impose the condition
$$d\left(\omega^{n-1}\right)=0 .$$
Hermitian metrics $\omega$ that satisfy this equality are known as balanced metrics. The condition (1.5) appears to be a natural one and has been much studied, due in part to a role in string theory. We refer the reader to [AB, BBFTY, FIUV, FY, FLY, Mi] and the references therein for more details.

We give a proof of the following:
Main Theorem. Let $(M, \omega)$ be a compact Hermitian manifold of complex dimension $n$. Let $\varphi$ be a smooth solution of the complex Monge-Ampère equation (1.1), subject to (1.2). Assume that either
(a) $n=2$; or
(b) $n>2$ and $d\left(\omega^{n-1}\right)=0$.
Then there are uniform $C^{\infty}$ a priori estimates on $\varphi$ depending only on $(M, \omega)$ and $F$.
Shortly after writing the first version of this paper, the authors discovered that the result of the Main Theorem is contained in a paper of Cherrier [Chr]. However, since our methods differ from those of Cherrier at almost every stage of the argument, we believe that our alternative proof of the Main Theorem may still be of interest. We describe later in the introduction some new elements of our proof.

First we make a couple of small remarks. We note that it is not necessary to assume that the solution is a priori smooth ( $\varphi \in C^{2}$ would be enough, for example), but we have made this assumption for the sake of simplicity. Also, with some work, one could make explicit the dependence of the estimates on $\varphi$ in terms of $(M, g)$ and the bounds $\|F\|_{C^{k}}$ for $k \in \mathbb{N}$.

We now give two corollaries of the Main Theorem. The first is contained in [Chr] and states that one can solve (1.1) after possibly adding a constant to the function $F$.

Corollary 1. Let $(M, \omega)$ be a compact Hermitian manifold satisfying one of the conditions (a) or (b) of the Main Theorem. Then for any smooth function $F$ on $M$ there exists a constant $b$ and a smooth function $\varphi$ on $M$ solving
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{F+b} \omega^{n} .$$

If $\varphi$ satisfies the normalization condition (1.2) then the $\varphi$ and $b$ are unique (see Remark 5.1). Cherrier's proof of Corollary 1 makes use of a rather general result of Delanoë [De]. For the sake of completeness, we include a direct proof of Corollary 1 in Section 5.

Note that the result of Guan-Li does not require the addition of a constant $b$ to the function $F$. The basic reason for this difference is that, unlike the balanced condition, the assumption (1.4) implies
$$\int_{M}(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=\int_{M} \omega^{n} .$$
We also remark that, in general, the balanced condition is in some sense disjoint from the condition (1.4) of Guan-Li. Indeed, if a balanced metric $\omega$ satisfies $\partial \bar{\partial} \omega=0$ it has to be Kähler (see e.g. [FPS, Proposition 1.4]). There are many known examples of non-Kähler balanced metrics [AB, FIUV, FLY, Mi], that hence do not satisfy (1.4). There seem to be fewer examples in the literature of non-Kähler metrics satisfying (1.4) in dimensions $n>2$. However, an elementary such example is the product of a complex curve with a Kähler metric and a complex surface with a non-Kähler Gauduchon metric. More examples were recently constructed in [FT].

We also point out that Cherrier proves the Main Theorem (and thus Corollary 1) under a technical assumption on $\omega$ which is slightly weaker than balanced and can be regarded as 'close to balanced'. He also considers the case of conformally Kähler $\omega$.

Next we give an application of Corollary 1 to the first Chern class of the Hermitian manifold $(M, \omega)$. Recall that for Kähler manifolds, Yau's theorem implies the Calabi Conjecture, which states that any representative of the first Chern class can be written as the Ricci curvature of a Kähler metric in any given Kähler class. We restrict now to two complex dimensions, and show that an analogue of the Calabi Conjecture is true if and only if an integral condition holds. Denoting by $\operatorname{Ric}(\omega)$ the first Chern form of the canonical connection of $g$ (see Section 6), we show that:

Corollary 2. Let $(M, \omega)$ be a compact Hermitian manifold of complex dimension two. Denote by $\omega_{G}$ any Gauduchon metric on $M$ (see (3.13)). Given a closed real $(1,1)$ form $\psi$ cohomologous to $c_{1}(M)$, we can write
$$\psi=\operatorname{Ric}(\omega+\sqrt{-1} \partial \bar{\partial} \varphi),$$
for some Hermitian metric $\omega+\sqrt{-1} \partial \bar{\partial} \varphi$ if and only if
$$\int_{M}(\operatorname{Ric}(\omega)-\psi) \wedge \omega_{G}=0 .$$

We now briefly outline the strategy for our proof of the Main Theorem and point out how our approach differs from that of [Chr] and also [GL]. We begin by describing the methods of [Chr], [GL]. Both papers give an estimate on the quantity $\operatorname{tr}_{g} g^{\prime}$ in terms of $\varphi$, where $g^{\prime}$ is the Hermitian metric defined by
$$g_{i \bar{j}}^{\prime}=g_{i \bar{j}}+\partial_{i} \partial_{\bar{j}} \varphi>0 .$$
The precise form of the estimate on $\operatorname{tr}_{g} g^{\prime}$ is not important for the methods of [Chr] or [GL], but tracing through the arguments of [GL] one can see for example that
$$\operatorname{tr}_{g} g^{\prime} \leq C e^{\left(e^{A\left(\sup _{M} \varphi-\inf _{M} \varphi\right)}-e^{A\left(\sup _{M} \varphi-\varphi\right)}\right)} .$$

Note that (1.10) is proved without any conditions on $(M, \omega)$. Zhang [Zh] independently proved a similar estimate on $\operatorname{tr}_{g} g^{\prime}$ and he also considered a generalization of the complex Monge-Ampère equation.

From (1.10), the metric $g^{\prime}$ is uniformly bounded once we have a bound on $\varphi$. As remarked in [GL], it is not clear whether the $C^{0}$ estimate of $\varphi$ given in [Ya], or the alternative methods of [Ko] or [B11], can be extended to the general Hermitian case. But by making use of the assumptions (a) or (b) and (1.4) respectively, a $C^{0}$ bound on $\varphi$ is proved in [Chr] and [GL]. The argument for the $C^{0}$ estimate in [Chr] is particularly intricate, especially in the case (b).

Our approach is quite different. We also prove an estimate on $\mathrm{tr}_{g} g^{\prime}$ depending on $\varphi$, but we show that the assumptions (a) and (b) imply an improved version of (1.10) and then make use of this to obtain the $C^{0}$ bound of $\varphi$. We prove the following estimate in Section 2.

Theorem 2.1. Under the assumptions of the Main Theorem, there exist uniform constants $C$ and $A$ such that
$$\operatorname{tr}_{g} g^{\prime} \leq C e^{A\left(\varphi-\inf _{M} \varphi\right)}$$

We remark that our proof of this improved estimate was motivated by our reading the paper [GL]. We use and modify some key ideas from [GL] (variations of some of these ideas also appear in [Chr], [Zh]).

Observe that (1.11) is now of the same form as the second order estimate from [Ya]. We then prove the uniform $C^{0}$ bound on $\varphi$ by making use of an idea from [We1, We2] (see also [TWY]), where it was shown that in the Kähler case, the estimate (1.11) implies a uniform bound on $\varphi$. Indeed, we show in Section 3 that combining (1.11) with a Moser iteration argument applied to the exponential of $\varphi$ gives,
$$-\inf \varphi \leq C_{\alpha}+\log \left(\frac{1}{\int_{M} \omega^{n}} \int_{M} e^{-\alpha \varphi} \omega^{n}\right)^{\frac{1}{\alpha}},$$
for all $\alpha>0$. Some further work shows that (1.12) gives a uniform bound of $\|\varphi\|_{C^{0}}$ and hence $\operatorname{tr}_{g} g^{\prime}$. We note that our $C^{0}$ estimate follows from (1.11) and does not make use of the complex Monge-Ampère equation. It would be interesting to know whether one can prove an estimate similar to (1.11) for other equations on Hermitian manifolds, and then apply our $C^{0}$ estimate.

Remark 1.1. A consequence of our results is that if the improved second order estimate (1.11) could be shown to hold in the case of general Hermitian $\omega$, then one could remove the conditions (a), (b) in the statements of the Main Theorem and Corollary 1. Indeed, our argument for the zero order estimate can easily be seen to hold without assuming (a) or (b). The higher order estimates also do not require these assumptions.

In Section 4 we complete the proof of the Main Theorem. Once we have the bound on $\operatorname{tr}_{g} g^{\prime}$ it is a straightforward matter to finish the proof. Cherrier [Chr] obtains higher order estimates via a third order estimate on $\varphi$ analogous to that of [Ya], [Ca2]. It was shown in [GL] that the higher order estimates follow from a bound on the real Hessian of $\varphi$ and arguments of Evans [Ev] and Krylov [Kr]. In order to give a short and largely self-contained proof we adapt instead an estimate of Trudinger [Tr].

In Sections 5 and 6 we prove Corollaries 1 and 2 respectively.

Remark 1.2. It is perhaps worth pointing out that a different generalization of Yau's theorem to non-Kähler manifolds has recently been proposed by Donaldson [Do2]. If $\omega$ is instead a symplectic form on a compact real 4-dimensional manifold, compatible with an almost complex structure $J$, then one can ask whether there exists a symplectic form $\tilde{\omega}$ compatible with $J$ solving
$$\tilde{\omega}^{2}=e^{F} \omega^{2} .$$
This problem has a rather different nature to the study of (1.1), since in general one does not expect that $\tilde{\omega}$ is of the form $\omega+d(J d \varphi)$. For some recent developments on this, we refer the reader to [We2, TWY, TW1, TW2].
2. The second order estimate. Write $g^{\prime}$ for the Hermitian metric given by (1.9). In this section we prove the following estimate on $\operatorname{tr}_{g} g^{\prime}=g^{i \bar{j}} g_{\bar{i} \bar{j}}^{\prime}$, depending on $\varphi$.

Theorem 2.1. Under the assumptions of the Main Theorem, there exist uniform constants $C$ and $A$ such that
$$\operatorname{tr}_{g} g^{\prime} \leq C e^{A\left(\varphi-\inf _{M} \varphi\right)}$$

Note that here, and henceforth, when we say 'uniform constant' it should be understood that we mean a constant depending only on $(M, g)$ and bounds for $F$. We will often write $C$ or $C^{\prime}$ for such a constant, where the value of $C, C^{\prime}$ may differ from line to line.

Write $\Delta$ for the Laplace operator of the canonical connection (i.e. the Chern connection) associated to the Hermitian metric $g$. Namely, for a function $f$,
$$\Delta f=g^{i \bar{j}} \partial_{i} \partial_{\bar{j}} f=\frac{n \omega^{n-1} \wedge \sqrt{-1} \partial \bar{\partial} f}{\omega^{n}},$$
and similarly for $\Delta^{\prime}$. Note that $\operatorname{tr}_{g} g^{\prime}=n+\Delta \varphi$ and $\operatorname{tr}_{g^{\prime}} g=n-\Delta^{\prime} \varphi$.
Proof of Theorem 2.1. Following the basic method of Yau [Ya] (see also [Au]), we apply the maximum principle to the quantity
$$Q=\log \operatorname{tr}_{g} g^{\prime}-A \varphi,$$
for some suitably chosen large constant $A$. For convenience, we will write $E_{1}$ and $E_{2}$ for terms satisfying
$$\left|E_{1}\right| \leq C \operatorname{tr}_{g^{\prime}} g, \quad\left|E_{2}\right| \leq C^{\prime}\left(\operatorname{tr}_{g} g^{\prime}\right)\left(\operatorname{tr}_{g^{\prime}} g\right) .$$
Note that the equation (1.1), which can be written as,
$$\operatorname{det} g^{\prime}=e^{F} \operatorname{det} g,$$
implies that $\operatorname{tr}_{g} g^{\prime}$ and $\operatorname{tr}_{g^{\prime}} g$ are uniformly bounded from below away from zero. It follows that a uniform constant is itself of type $E_{1}$ and any term of type $E_{1}$ is also of type $E_{2}$. We also note here the elementary inequality
$$\operatorname{tr}_{g} g^{\prime} \leq \frac{1}{(n-1)!}\left(\operatorname{tr}_{g^{\prime}} g\right)^{n-1} \frac{\operatorname{det} g^{\prime}}{\operatorname{det} g}=\frac{1}{(n-1)!}\left(\operatorname{tr}_{g^{\prime}} g\right)^{n-1} e^{F},$$
and in the case of dimension $n=2$, the equality
$$\operatorname{tr}_{g} g^{\prime}=\left(\operatorname{tr}_{g^{\prime}} g\right) e^{F} .$$

We will show that in both cases (a) and (b) from the statement of the Main Theorem, we have the estimate
$$\Delta^{\prime} \log \operatorname{tr}_{g} g^{\prime} \geq E_{1} .$$
Given (2.4), the theorem follows immediately. Indeed, if $Q$ achieves its maximum at a point $p$, we obtain
$$0 \geq\left(\Delta^{\prime} Q\right)(p) \geq E_{1}-A n+A\left(\operatorname{tr}_{g^{\prime}} g\right)(p) \geq\left(\operatorname{tr}_{g^{\prime}} g\right)(p)-C,$$
if $A$ is chosen sufficiently large. Then $\left(\operatorname{tr}_{g^{\prime}} g\right)(p)$ is uniformly bounded from above, which implies by (2.2) that $\left(\operatorname{tr}_{g} g^{\prime}\right)(p)$ is too. Then for any $q \in M$,
$$Q(q) \leq Q(p) \leq \log C-A \inf _{M} \varphi,$$
and (2.1) follows after exponentiating.
We need the following lemma from [GL] (see also [ST] for a similar argument).
Lemma 2.1. At any point $p$ there exists a holomorphic coordinate system centered at $p$ such that for all $i, j$,
$$g_{i \bar{j}}(0)=\delta_{i j}, \quad \partial_{j} g_{i \bar{i}}(0)=0,$$
and also that the matrix $\left(\partial_{k} \partial_{\bar{\ell}} \varphi\right)(0)$ is diagonal.
When we perform local computations we will always assume we are using a coordinate system given by this lemma at a point $p$, and we will use lower indices to denote partial derivatives. We first compute:
$$\begin{aligned}
\Delta^{\prime} \operatorname{tr}_{g} g^{\prime}= & g^{\prime i \bar{j}} \partial_{i} \partial_{\bar{j}}\left(g^{k \bar{\ell}} \varphi_{k \bar{\ell}}\right) \\
= & \sum_{i, k} g^{\prime i \bar{i}} \varphi_{k \bar{k} i \bar{i}}-2 \operatorname{Re}\left(\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{\bar{i}} g_{j \bar{k}} \varphi_{k \bar{j} i}\right)+\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{i} g_{j \bar{k}} \partial_{\bar{i}} g_{k \bar{j}} \varphi_{k \bar{k}} \\
& +\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{i} g_{k \bar{j}} \partial_{\bar{i}} g_{j \bar{k}} \varphi_{k \bar{k}}-\sum_{i, k} g^{\prime i \bar{i}} \partial_{i} \partial_{\bar{i}} g_{k \bar{k}} \varphi_{k \bar{k}}
\end{aligned}$$
$$=\sum_{i, k} g^{\prime i \bar{i}} \varphi_{k \bar{k} i \bar{i}}-2 \operatorname{Re}\left(\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{\bar{i}} g_{j \bar{k}} \varphi_{k \bar{j} i}\right)+E_{2} .$$
We now apply the operator $\Delta \log (\cdot)$ to the equation (1.1), to get:
$$\begin{aligned}
& -g^{k \bar{\ell}} g^{\prime p \bar{j}} g^{\prime i \bar{q}} \partial_{k} g_{p \bar{q}}^{\prime} \partial_{\bar{\ell}} g_{i \bar{j}}^{\prime}+g^{k \bar{\ell}} g^{\prime i \bar{j}} \partial_{k} \partial_{\bar{\ell}} g_{i \bar{j}}^{\prime} \\
& =\Delta F-g^{k \bar{\ell}} g^{p \bar{j}} g^{i \bar{q}} \partial_{k} g_{p \bar{q}} \partial_{\bar{\ell}} g_{i \bar{j}}+g^{k \bar{\ell}} g^{i \bar{j}} \partial_{k} \partial_{\bar{\ell}} g_{i \bar{j}} .
\end{aligned}$$
We can rewrite this as:
$$\sum_{i, k} g^{\prime i \bar{i}} \varphi_{i \bar{i} k \bar{k}}=\sum_{i, j, k} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}+E_{1} .$$

Thus (2.6) and (2.8) give
$$\Delta^{\prime} \operatorname{tr}_{g} g^{\prime}=\sum_{i, j, k} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}-2 \operatorname{Re}\left(\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{\bar{i}} g_{j \bar{k}} \varphi_{k \bar{j} i}\right)+E_{2} .$$

A key trick in [GL] is to use part of the first term $\sum_{i, j, k} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}$ on the right hand side of (2.9) to deal with the troublesome second term. Calculate, using (2.5),
$$\begin{aligned}
\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{\bar{i}} g_{j \bar{k}} \varphi_{k \bar{j} i} & =\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{\bar{i}} g_{j \bar{k}}\left(\partial_{k} g_{i \bar{j}}+\varphi_{i \bar{j} k}\right)+E_{1} \\
& =\sum_{i} \sum_{j \neq k} g^{\prime i \bar{i}} \partial_{\bar{i}} g_{j \bar{k}} \partial_{k} g_{i \bar{j}}^{\prime}+E_{1} .
\end{aligned}$$
It follows that
$$\begin{aligned}
& \left|2 \operatorname{Re}\left(\sum_{i, j, k} g^{\prime i \bar{i}} \partial_{\bar{i}} g_{j \bar{k}} \varphi_{k \bar{j} i}\right)\right| \\
& \leq \frac{1}{2} \sum_{i} \sum_{j \neq k} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}+2 \sum_{i} \sum_{j \neq k} g^{\prime i \bar{i}} g_{j \bar{j}}^{\prime} \partial_{\bar{i}} g_{j \bar{k}} \partial_{i} g_{k \bar{j}}+E_{1} \\
& =\frac{1}{2} \sum_{i} \sum_{j \neq k} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}+E_{2} .
\end{aligned}$$
Note that the factor 1/2 in (2.11) differs from the corresponding factor 1 in [GL]. We will make use of this later. Combining (2.9) and (2.11) we have
$$\Delta^{\prime} \operatorname{tr}_{g} g^{\prime} \geq \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}^{\prime}+\frac{1}{2} \sum_{i} \sum_{j \neq k} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}+E_{2} .$$

We now claim that
$$\frac{\left|\partial \operatorname{tr}_{g} g^{\prime}\right|_{g^{\prime}}^{2}}{\operatorname{tr}_{g} g^{\prime}} \leq \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j i \bar{j}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}^{\prime}+\frac{1}{2} \sum_{i} \sum_{j \neq k} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}+E_{2} .$$
Given (2.13) we would then have (2.4) since
$$\Delta^{\prime} \log \operatorname{tr}_{g} g^{\prime}=\frac{\Delta^{\prime} \operatorname{tr}_{g} g^{\prime}}{\operatorname{tr}_{g} g^{\prime}}-\frac{\left|\partial \operatorname{tr}_{g} g^{\prime}\right|_{g^{\prime}}^{2}}{\left(\operatorname{tr}_{g} g^{\prime}\right)^{2}} \geq E_{1} .$$
Thus the proof of the theorem reduces to establishing (2.13). We split the proof of (2.13) into the two cases (a) and (b).

We remark that a different inequality from (2.13) is proved in [GL], where they make use of an alternative expression for $Q$. Indeed, it is not clear whether (2.13) holds in general without our assumptions (a) or (b).

Proof of (2.13) in the case (a). We prove (2.13) assuming that $n=2$. First, making use of (2.5), we have
$$\partial_{i} \operatorname{tr}_{g} g^{\prime}=\sum_{j} \partial_{i} g_{j \bar{j}}^{\prime}$$

We use an argument in Yau's second order estimate [Ya]. Applying the Cauchy-Schwarz inequality twice:
$$\begin{aligned}
\frac{\left.\partial \operatorname{tr}_{g} g^{\prime}\right|_{g^{\prime}} ^{2}}{\operatorname{tr}_{g} g^{\prime}} & =\frac{1}{\operatorname{tr}_{g} g^{\prime}} \sum_{i, j, k} g^{\prime i \bar{i}} \partial_{i} g_{j \bar{j}}^{\prime} \partial_{\bar{i}} g_{k \bar{k}}^{\prime} \\
& =\frac{1}{\operatorname{tr}_{g} g^{\prime}} \sum_{j, k} \sum_{i} \sqrt{g^{\prime i \bar{i}}} \partial_{i} g_{j \bar{j}}^{\prime} \sqrt{g^{\prime i \bar{i}}} \partial_{\bar{i}} g_{k \bar{k}}^{\prime} \\
& \leq \frac{1}{\operatorname{tr}_{g} g^{\prime}} \sum_{j, k}\left(\sum_{i} g^{\prime i \bar{i}}\left|\partial_{i} g_{j \bar{j}}^{\prime}\right|^{2}\right)^{1 / 2}\left(\sum_{i} g^{\prime i \bar{i}}\left|\partial_{i} g_{k \bar{k}}^{\prime}\right|^{2}\right)^{1 / 2} \\
& =\frac{1}{\operatorname{tr}_{g} g^{\prime}}\left(\sum_{j}\left(\sum_{i} g^{\prime i \bar{i}}\left|\partial_{i} g_{j \bar{j}}^{\prime}\right|^{2}\right)^{1 / 2}\right)^{2} \\
& =\frac{1}{\operatorname{tr}_{g} g^{\prime}}\left(\sum_{j} \sqrt{g_{j \bar{j}}^{\prime}}\left(\sum_{i} g^{\prime i \bar{i}} g^{\prime j \bar{j}}\left|\partial_{i} g_{j \bar{j}}^{\prime}\right|^{2}\right)^{1 / 2}\right)^{2} \\
& \leq \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{i} g_{j \bar{j}}^{\prime} \partial_{\bar{i}} g_{j \bar{j}}^{\prime} .
\end{aligned}$$

Using (2.5) again, we can rewrite this as,
$$\begin{aligned}
\frac{\left|\partial \operatorname{tr}_{g} g^{\prime}\right|_{g^{\prime}}^{2}}{\operatorname{tr}_{g} g^{\prime}} \leq & \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j i \bar{j}} \varphi_{j \bar{j} i} \varphi_{j j \bar{i}} \\
= & \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \varphi_{i \bar{j} j} \varphi_{j \overline{i j}} \\
= & \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}}\left(\partial_{j} g_{i \bar{j}}^{\prime}-\partial_{j} g_{i \bar{j}}\right)\left(\partial_{\bar{j}} g_{j \bar{i}}^{\prime}-\partial_{\bar{j}} g_{j \bar{i}}\right) \\
= & \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}^{\prime}-2 \operatorname{Re}\left(\sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}\right) \\
& +\sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}} \partial_{\bar{j}} g_{j \bar{i}} \\
= & \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}^{\prime}-2 \operatorname{Re}\left(\sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{i} g_{j \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}\right) \\
& -\sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}} \partial_{\bar{j}} g_{j \bar{i}}
\end{aligned}$$
$$\leq \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}^{\prime}-2 \operatorname{Re}\left(\sum_{i \neq j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{i} g_{j \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}\right) .$$

It remains to control the term
$$2 \operatorname{Re}\left(\sum_{i \neq j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{i} g_{j \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}\right) .$$

Using again (2.5) and also the fact that in dimension $n=2, \operatorname{tr}_{g} g^{\prime}$ and $\operatorname{tr}_{g^{\prime}} g$ are uniformly equivalent, which follows from (2.3), we see that
$$\begin{aligned}
\left|2 \operatorname{Re}\left(\sum_{i \neq j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{i} g_{j \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}\right)\right| & \leq \frac{1}{2} \sum_{i \neq j} g^{\prime j \bar{j}} g^{\prime j \bar{j}}\left|\partial_{i} g_{j \bar{j}}^{\prime}\right|^{2}+2 \sum_{i \neq j} g^{\prime i \bar{i}} g^{\prime i \bar{i}}\left|\partial_{j} g_{i \bar{j}}\right|^{2} \\
& =\frac{1}{2} \sum_{i \neq j} g^{\prime j \bar{j}} g^{\prime j \bar{j}}\left|\partial_{i} g_{j \bar{j}}^{\prime}\right|^{2}+E_{2} .
\end{aligned}$$
But notice that
$$\frac{1}{2} \sum_{i \neq j} g^{\prime j \bar{j}} g^{\prime j \bar{j}}\left|\partial_{i} g_{j \bar{j}}^{\prime}\right|^{2} \leq \frac{1}{2} \sum_{i} \sum_{j \neq k} g^{\prime i \bar{i}} g^{\prime j \vec{j}} \partial_{k} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{j \bar{i}}^{\prime}$$
Combining (2.16), (2.17) and (2.18) gives (2.13).
Proof of (2.13) in the case (b). We finish the proof of the theorem by establishing (2.13) when $n>2$ and $d\left(\omega^{n-1}\right)=0$. The condition $d\left(\omega^{n-1}\right)=0$ is equivalent to $\sum_{j} T_{j i}^{j}=0$, where $T_{j i}^{k}=g^{k \bar{\ell}}\left(\partial_{j} g_{i \bar{\ell}}-\partial_{i} g_{j \bar{\ell}}\right)$ is the torsion of $g$ (see e.g. [Ga2, Ga3]). Then we have, at $p$, using the coordinate system of Lemma 2.1,
$$0=\sum_{j} T_{j i}^{j}=\sum_{j} \partial_{j} g_{i \bar{j}}-\sum_{j} \partial_{i} g_{j \bar{j}}=\sum_{j} \partial_{j} g_{i \bar{j}} .$$
Then from (2.14) we have,
$$\partial_{i} \operatorname{tr}_{g} g^{\prime}=\sum_{j} \partial_{i} g_{j \bar{j}}^{\prime}=\sum_{j} \partial_{i} \varphi_{j \bar{j}}=\sum_{j}\left(\partial_{j} g_{i \bar{j}}+\partial_{j} \varphi_{i \bar{j}}\right)=\sum_{j} \partial_{j} g_{i \bar{j}}^{\prime} .$$
Repeating the argument we used in (2.15) we obtain
$$\begin{aligned}
\frac{\left|\partial \operatorname{tr}_{g} g^{\prime}\right|_{g^{\prime}}^{2}}{\operatorname{tr}_{g} g^{\prime}} & =\frac{1}{\operatorname{tr}_{g} g^{\prime}} \sum_{i, j, k} g^{\prime i \bar{i}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{k}} g_{k \bar{i}}^{\prime} \\
& \leq \sum_{i, j} g^{\prime i \bar{i}} g^{\prime j \bar{j}} \partial_{j} g_{i \bar{j}}^{\prime} \partial_{\bar{j}} g_{j \bar{i}}^{\prime}
\end{aligned}$$
and this immediately gives (2.13). □
3. The zeroth order estimate. In this section we will prove:

Theorem 3.1. Under the assumptions of the Main Theorem, there exists a uniform constant $C$ such that
$$\|\varphi\|_{C^{0}} \leq C .$$

Proof. We note that the proof of Theorem 3.1 crucially requires the precise form of Theorem 2.1, but does not again make use of the equation (1.1). In particular, if one could prove (2.1) without assumptions (a) or (b), Theorem 3.1 would also follow. We first prove two lemmas which we will use in both cases (a) and (b).

Lemma 3.1. For every $\alpha>0$ there exists a constant $C_{\alpha}$ such that
$$-\inf _{M} \varphi \leq C_{\alpha}+\log \left(\int_{M} e^{-\alpha \varphi} d \mu\right)^{\frac{1}{\alpha}}$$
where $d \mu=\omega^{n} / \int_{M} \omega^{n}$.
Proof. The argument is almost identical to the one given in [We2]. Let $\delta>0$ be a given small constant. Define $w=e^{-B \varphi}, \gamma=1-\delta, B=A / \gamma$, where $A$ is the constant given in (2.1). For $p \geq 1$, compute:
$$\begin{aligned}
\int_{M}\left|\partial w^{p / 2}\right|_{g}^{2} \omega^{n}= & n \int_{M} \sqrt{-1} \partial e^{-\frac{B p \varphi}{2}} \wedge \bar{\partial} e^{-\frac{B p \varphi}{2}} \wedge \omega^{n-1} \\
\leq & C n p^{2} \int_{M} e^{-B p \varphi} \sqrt{-1} \partial \varphi \wedge \bar{\partial} \varphi \wedge \omega^{n-1} \\
\leq & -C n p \int_{M} \sqrt{-1} \partial\left(e^{-B p \varphi}\right) \wedge \bar{\partial} \varphi \wedge \omega^{n-1} \\
= & C n p \int_{M} e^{-B p \varphi} \sqrt{-1} \partial \bar{\partial} \varphi \wedge \omega^{n-1} \\
& -C n p \int_{M} e^{-B p \varphi} \sqrt{-1} \bar{\partial} \varphi \wedge \partial \omega^{n-1} \\
= & C p \int_{M} e^{-B p \varphi} \Delta \varphi \omega^{n} \\
& +C^{\prime} \int_{M} \sqrt{-1} \bar{\partial}\left(e^{-B p \varphi}\right) \wedge \partial \omega^{n-1} \\
\leq & C p\|w\|_{C^{0}}^{\gamma} \int_{M} e^{-B(p-\gamma) \varphi} \omega^{n} \\
& +C p \int_{M} \sqrt{-1} e^{-B(p-\gamma) \varphi} e^{-B \gamma \varphi} \partial \bar{\partial}\left(\omega^{n-1}\right) \\
\leq & C p\|w\|_{C^{0}}^{\gamma} \int_{M} e^{-B(p-\gamma) \varphi} \omega^{n} \\
= & C p\|w\|_{C^{0}}^{\gamma} \int_{M} w^{p-\gamma} \omega^{n},
\end{aligned}$$
where we have used the fact that $\partial \bar{\partial}\left(\omega^{n-1}\right)$ is bounded and
$$\Delta \varphi=\operatorname{tr}_{g} g^{\prime}-n \leq C e^{A(\varphi-\inf \varphi)}=C e^{B \gamma(\varphi-\inf \varphi)} \leq C\|w\|_{C^{0}}^{\gamma} e^{B \gamma \varphi} .$$

Now, the Sobolev inequality gives us, for $\beta=n /(n-1)$, and any smooth $f$,
$$\left(\int_{M} f^{2 \beta} \omega^{n}\right)^{1 / \beta} \leq C\left(\int_{M}|\partial f|_{g}^{2} \omega^{n}+\int_{M} f^{2} \omega^{n}\right),$$
Applying this to $f=w^{p / 2}$ and raising to the power $1 / p$, we obtain
$$\|w\|_{p \beta} \leq C^{1 / p} p^{1 / p}\|w\|_{C^{0}}^{\gamma / p}\|w\|_{p-\gamma}^{(p-\gamma) / p},$$
where $\left\|\|_{q}\right.$ denotes the $L^{q}$ norm with respect to $d \mu$ (allowing $0<q<1$, defined in the obvious way). By the same iteration as in [We2] (see also [TWY]) we replace $p$ with $p \beta+\gamma$ in (3.4) to obtain for $k=1,2 \ldots$,
$$\|w\|_{p_{k} \beta} \leq C\|w\|_{C^{0}}^{1-a(k)}\|w\|_{p-\gamma}^{a(k)},$$
where $p(k) \rightarrow \infty$ and $a(k) \rightarrow a \in(0,1)$ as $k \rightarrow \infty$. We refer the reader to [We2] for the details. Letting $k \rightarrow \infty$ and setting $p=1$ in (3.5), we have
$$\|w\|_{C^{0}} \leq C\|w\|_{\delta} .$$

Choosing $\delta$ sufficiently small proves the lemma for $\alpha$ sufficiently small. It follows from Hölder's inequality that if Lemma 3.1 holds for all $\alpha>0$ sufficiently small then it holds for all $\alpha>0$. □

Denote by $|\cdot|$ the measure of a set with respect to the measure $d \mu=\omega^{n} / \int_{M} \omega^{n}$. Then we have the following.

Lemma 3.2. Let $C_{1}$ be the constant corresponding to $\alpha=1$ from Lemma 3.1. Then
$$\left|\left\{\varphi \leq \inf _{M} \varphi+C_{1}+1\right\}\right| \geq \frac{e^{-C_{1}}}{4} .$$

Proof. Suppose for a contradiction that
$$\left|\left\{\varphi \leq \inf _{M} \varphi+C_{1}+1\right\}\right|<\frac{e^{-C_{1}}}{4} .$$
First note that from Lemma 3.1 with $\alpha=1$, we have
$$e^{-\varphi} \leq e^{-\inf _{M} \varphi} \leq e^{C_{1}} \int_{M} e^{-\varphi}$$
where here and henceforth we are integrating with respect to $d \mu$. Now
$$\int_{M} e^{-\varphi}=\int_{\left\{e^{-\varphi} \geq \frac{1}{e} \int_{M} e^{-\varphi}\right\}} e^{-\varphi}+\int_{\left\{e^{-\varphi}<\frac{1}{e} \int_{M} e^{-\varphi}\right\}} e^{-\varphi} .$$
But
$$\begin{aligned}
\left|\left\{e^{-\varphi} \geq \frac{1}{e} \int_{M} e^{-\varphi}\right\}\right| & \leq\left|\left\{e^{-\varphi} \geq \frac{1}{e^{C_{1}+1}} e^{-\inf _{M} \varphi}\right\}\right| \\
& =\left|\left\{-\varphi \geq-\inf _{M} \varphi-C_{1}-1\right\}\right| \\
& <\frac{e^{-C_{1}}}{4},
\end{aligned}$$
from (3.7), (3.8). Then in (3.9), using (3.8) and the fact that the volume of $M$ is equal to 1 , we have
$$\int_{M} e^{-\varphi} \leq \frac{e^{-C_{1}}}{4} e^{C_{1}} \int_{M} e^{-\varphi}+\frac{1}{e} \int_{M} e^{-\varphi} \leq \frac{3}{4} \int_{M} e^{-\varphi},$$
a contradiction. □
Remark 3.1. We note that Lemma 3.2 can also be applied to improve Theorem 1.3 of [TWY], where it was shown that a conjecture of Donaldson [Do2] on a priori estimates for the Calabi-Yau equation reduces to estimating a quantity $\int_{M} e^{-\alpha \varphi}$ for $\alpha>0$, where $\varphi$ is a generalization of the Kähler potential function to the non-integrable setting. Lemma 3.2 can be used to show that it is sufficient to bound, for example, the $L^{1}$ norm of $\varphi$.

We now separate the proof of Theorem 3.1 into the two cases (a) and (b), dealing with (b) first.

Proof of Theorem 3.1 in the case (b) We have the following lemma.

Lemma 3.3. Suppose that $(M, g)$ is a balanced manifold and $\varphi$ satisfies $\sup _{M} \varphi=$ 0 and
$$g_{i \bar{j}}^{\prime}=g_{i \bar{j}}+\partial_{i} \partial_{\bar{j}} \varphi>0 .$$
Then there exists a uniform constant $C$ depending only on $(M, g)$ such that
$$\int_{M}|\varphi| d \mu \leq C .$$

Proof. Observe that this lemma does not require $\varphi$ to solve the complex Monge-Ampère equation (1.1). All we need is that $g$ is balanced and
$$\Delta \varphi>-n .$$
Since $g$ is balanced, the canonical Laplacian $\Delta$ coincides (up to a constant multiple) with the Laplace-Beltrami operator for the Riemannian metric associated to $g$ (see for example [To1, Lemma 3.2] or [Ga2, Proposition 1]). Let $G: M \times M \rightarrow \mathbb{R}$ be the associated Green's function. Then $G$ is uniformly bounded below by $K$, say, and satisfies for all $x$ in $M$,
$$\int_{y \in M} G(x, y) \omega^{n}(y)=0 .$$
Let $x$ in $M$ be a point such that $\varphi(x)=0$. Then
$$\begin{aligned}
0 & =\int_{M} \varphi d \mu+\int_{y \in M} G(x, y)(-\Delta \varphi)(y) \omega^{n}(y) \\
& <\int_{M} \varphi d \mu+n K \int_{M} \omega^{n},
\end{aligned}$$
and this proves the lemma. □
We now finish the proof of Theorem 3.1 in the case (b). From Lemma 3.2, we see that
$$|\varphi| \geq-\inf _{M} \varphi-C_{1}-1$$
on a set of measure at least $e^{-C_{1}} / 4$. Then
$$\int_{M}|\varphi| d \mu \geq \frac{e^{-C_{1}}}{4}\left(-\inf _{M} \varphi-C_{1}-1\right) .$$
But $\int_{M}|\varphi| d \mu$ is bounded from above by Lemma 3.3. This gives an upper bound for $-\inf _{M} \varphi$ and completes the proof of Theorem 3.1 in the case (b).

Proof of Theorem 3.1 in the case (a) Since we no longer have the balanced condition as in (b), we use a different, and slightly more involved argument, which in fact would also work in the higher dimensional case.

First recall a basic result of Gauduchon [Ga1]. For any compact Hermitian manifold $(M, \omega)$ of complex dimension $n>1$, there exists a smooth function $u$, unique up to addition of a constant, such that the Hermitian metric $\omega_{G}=e^{u} \omega$ satisfies
$$\partial \bar{\partial}\left(\omega_{G}^{n-1}\right)=0 .$$

A metric $\omega_{G}$ satisfying (3.13) is called Gauduchon. We will write $\Delta_{G}$ for the canonical Laplacian of $\omega_{G}$.

We will make use of a Moser iteration result for Gauduchon metrics which can be summarized in the following lemma. Since we are working in the case (a), we restrict now to two complex dimensions. However, the results given below easily generalize to higher dimensions.

Lemma 3.4. Let $M$ be a two-dimensional compact complex manifold with a Gauduchon metric $\omega_{G}$. If $\psi$ is a smooth nonnegative function on $M$ with
$$\Delta_{G} \psi \geq-C_{0}$$
then there exist constants $C_{1}$ and $C_{2}$ depending only on $\left(M, \omega_{G}\right)$ and $C_{0}$ such that:
$$\int_{M}\left|\partial \psi^{\frac{p+1}{2}}\right|_{\omega_{G}}^{2} \omega_{G}^{2} \leq C_{1} p \int_{M} \psi^{p} \omega_{G}^{2} \quad \text { for all } p \geq 1,$$
and
$$\sup _{M} \psi \leq C_{2} \max \left\{\int_{M} \psi \omega_{G}^{2}, 1\right\} .$$

Proof. Compute for $p \geq 1$,
$$\begin{aligned}
\int_{M}\left|\partial \psi^{\frac{p+1}{2}}\right|_{\omega_{G}}^{2} \omega_{G}^{2} & =2 \int_{M} \sqrt{-1} \partial \psi^{\frac{p+1}{2}} \wedge \bar{\partial} \psi^{\frac{p+1}{2}} \wedge \omega_{G} \\
& =\frac{(p+1)^{2}}{2} \int_{M} \sqrt{-1} \psi^{p-1} \partial \psi \wedge \bar{\partial} \psi \wedge \omega_{G} \\
& =\frac{(p+1)^{2}}{2 p} \int_{M} \sqrt{-1} \partial \psi^{p} \wedge \bar{\partial} \psi \wedge \omega_{G} \\
& =-\frac{(p+1)^{2}}{2 p} \int_{M} \psi^{p} \sqrt{-1} \partial \bar{\partial} \psi \wedge \omega_{G}+\frac{p+1}{2 p} \int_{M} \sqrt{-1} \bar{\partial} \psi^{p+1} \wedge \partial \omega_{G} \\
& =\frac{(p+1)^{2}}{4 p} \int_{M} \psi^{p}\left(-\Delta_{G} \psi\right) \omega_{G}^{2} \\
& \leq C \frac{(p+1)^{2}}{4 p} \int_{M} \psi^{p} \omega_{G}^{2}
\end{aligned}$$
thus establishing (3.14). Note that, to pass from the fourth to fifth lines, we have made use of the Gauduchon condition (3.13).

The inequality (3.15) then follows by a standard iteration argument, using the Sobolev inequality (3.3) with $\omega$ replaced by $\omega_{G}$. Indeed, write $q=p+1$ and apply (3.3) to $f=\psi^{q / 2}$ to obtain for $q \geq 2$,
$$\left(\int_{M} \psi^{2 q} \omega_{G}^{2}\right)^{1 / 2} \leq C q \max \left\{\int_{M} \psi^{q} \omega_{G}^{2}, 1\right\} .$$
By repeatedly replacing $q$ by $2 q$ and iterating we have, after setting $q=2$,
$$\sup _{M} \psi \leq C \max \left\{\left(\int_{M} \psi^{2} \omega_{G}^{2}\right)^{1 / 2}, 1\right\} .$$

Hence
$$\sup _{M} \psi \leq C \max \left\{\left(\sup _{M} \psi\right)^{1 / 2}\left(\int_{M} \psi \omega_{G}^{2}\right)^{1 / 2}, 1\right\},$$
and (3.15) follows. □
We will now apply Lemma 3.4 to the function
$$\psi=\varphi-\inf _{M} \varphi \geq 0,$$
which, since $\Delta \psi>-n$, satisfies
$$\Delta_{G} \psi=e^{-u} \Delta \psi>-C .$$
Thus, thanks to (3.15), to finish the proof of the theorem it suffices to bound the $L^{1}\left(\omega_{G}\right)$ norm of $\psi$. From (3.14) with $p=1$ we have
$$\int_{M}|\partial \psi|_{\omega_{G}}^{2} \omega_{G}^{2} \leq C\|\psi\|_{L^{1}\left(\omega_{G}\right)} .$$
Denote by $\underline{\psi}$ the average of $\psi$ with respect to $\omega_{G}^{2}$. From the Poincaré inequality we have
$$\|\psi-\underline{\psi}\|_{L^{2}\left(\omega_{G}\right)} \leq C\left(\int_{M}|\partial \psi|_{\omega_{G}}^{2} \omega_{G}^{2}\right)^{1 / 2} \leq C\|\psi\|_{L^{1}\left(\omega_{G}\right)}^{1 / 2} .$$
We will now make use of Lemma 3.2. For a uniform constant $K$, the set $S:=\{\psi \leq$ $K\} \subset M$ satisfies
$$|S| \geq \varepsilon,$$
for a uniform $\varepsilon>0$. On $S$ we have
$$\underline{\psi} \leq|\psi-\underline{\psi}|+K,$$
and integrating this over $S$ and making use of (3.19), we have
$$\frac{\varepsilon}{\int_{M} \omega_{G}^{2}} \int_{M} \psi \omega_{G}^{2}=\varepsilon \underline{\psi} \leq \int_{S} \underline{\psi} \omega_{G}^{2} \leq \int_{M}|\psi-\underline{\psi}| \omega_{G}^{2}+C .$$
Then, using (3.18),
$$\begin{aligned}
\|\psi\|_{L^{1}\left(\omega_{G}\right)} & \leq C\left(\|\psi-\underline{\psi}\|_{L^{1}\left(\omega_{G}\right)}+1\right) \\
& \leq C\left(\|\psi-\underline{\psi}\|_{L^{2}\left(\omega_{G}\right)}+1\right) \\
& \leq C\left(\|\psi\|_{L^{1}\left(\omega_{G}\right)}^{1 / 2}+1\right),
\end{aligned}$$
which shows that $\psi$ is uniformly bounded in $L^{1}\left(\omega_{G}\right)$. This completes the proof of the theorem. □
4. Proof of the Main Theorem. From Theorem 2.1 and Theorem 3.1, we have a uniform upper bound of $\operatorname{tr}_{g} g^{\prime}$. It follows from (1.1) that $g$ and $g^{\prime}$ are uniformly equivalent as Hermitian metrics. To finish the proof of the Main Theorem, it suffices to prove a $C^{\alpha}$ estimate on the metric $g_{i \bar{j}}^{\prime}$ for some $\alpha>0$. Indeed once we have this estimate, then differentiating (1.1) and applying the standard local elliptic estimates gives us uniform $C^{\infty}$ bounds on $\varphi$.

The $C^{\alpha}$ estimate on $g_{i \bar{j}}^{\prime}$ is proved in [GL] using a bound on the real Hessian of $\varphi$ (see also [Po, CKNS, Bł2]) and results of Evans [Ev] and Krylov [Kr]. Instead, we provide a self-contained and more direct proof following a complex version of the Evans-Krylov estimate, due to Trudinger [Tr]. We follow quite closely Trudinger's argument (see also the expositions of Siu [Si] and [GT], and also [We3] for a generalization of this argument to the case of $J$ non integrable). Since the argument in this case is very similar, we will be brief in places.

We work in a small open subset $U$ of $\mathbb{C}^{n}$ that contains a ball $B_{2 R}$ of radius $2 R$, and consider the equation
$$\log \operatorname{det}\left(g_{i \bar{j}}^{\prime}\right)=\log \operatorname{det}\left(g_{i \bar{j}}+\varphi_{i \bar{j}}\right)=F .$$
Consider the operator $\Phi$ on positive definite Hermitian matrices given by $\Phi(A)=$ $\log \operatorname{det} A$ for $A=\left(a_{i \bar{j}}\right)$. Observe that $\Phi$ is concave. Our equation (4.1) can be expressed as
$$\Phi\left(g^{\prime}\right)=F .$$
Differentiating (4.2) with respect to an arbitrary vector $\gamma \in \mathbb{C}^{n}$ and then $\bar{\gamma}$ we obtain
$$\sum_{i, j} \frac{\partial \Phi}{\partial a_{i \bar{j}}} g_{i \bar{j} \gamma}^{\prime}=F_{\gamma}$$
and
$$\sum_{i, j, k, \ell} \frac{\partial^{2} \Phi}{\partial a_{i \bar{j}} \partial a_{k \bar{\ell}}} g_{k \bar{\ell}}^{\prime} g_{i \bar{j} \gamma}^{\prime}+\sum_{i, j} \frac{\partial \Phi}{\partial a_{i \bar{j}}} g_{i \bar{j} \gamma \bar{\gamma}}^{\prime}=F_{\gamma \bar{\gamma}} .$$
Note that
$$\frac{\partial \Phi}{\partial a_{i \bar{j}}}\left(g^{\prime}\right)=g^{\prime i \bar{j}} .$$
Since $\Phi$ is concave, the first term on the left hand side is nonpositive and thus
$$g^{\prime i \bar{j}} \varphi_{i \bar{j} \gamma \bar{\gamma}} \geq F_{\gamma \bar{\gamma}}-g^{\prime i \bar{j}} g_{i \bar{j} \gamma \bar{\gamma}} .$$
Writing $w=\varphi_{\gamma \bar{\gamma}}$ and $H=F_{\gamma \bar{\gamma}}-g^{\prime i \bar{j}} g_{i \bar{j} \gamma \bar{\gamma}}$ we have
$$g^{\prime i \bar{j}} \partial_{i} \partial_{\bar{j}} w \geq H .$$
Note that for each fixed $\gamma, H$ is uniformly bounded.
Before we make use of (4.3), we observe that another consequence of the concavity of $\Phi$ is that for all $x, y$ in $U$,
$$\Phi\left(g^{\prime}(y)\right)+\sum_{i, j} \frac{\partial \Phi}{\partial a_{i \bar{j}}}\left(g^{\prime}(y)\right)\left(g_{i \bar{j}}^{\prime}(x)-g_{i \bar{j}}^{\prime}(y)\right) \geq \Phi\left(g^{\prime}(x)\right) .$$

It follows that
$$\sum_{i, j} \frac{\partial \Phi}{\partial a_{i \bar{j}}}\left(g^{\prime}(y)\right)\left(g_{i \bar{j}}^{\prime}(y)-g_{i \bar{j}}^{\prime}(x)\right) \leq F(y)-F(x) \leq C R$$
where for the last line we have used the mean value theorem. Since we have a priori estimates on $g^{\prime}$ and hence on $\partial \Phi / \partial a_{i \bar{j}}$, we can find unit vectors $\gamma_{1}, \ldots, \gamma_{N}$ in $\mathbb{C}^{n}$ and real-valued functions $\beta_{1}, \ldots, \beta_{N}$ satisfying
$$0<\frac{1}{C} \leq \beta_{\nu} \leq C, \quad \text { for } \nu=1, \ldots, N,$$
such that
$$\frac{\partial \Phi}{\partial a_{i \bar{j}}}\left(g^{\prime}(y)\right)=\sum_{\nu=1}^{N} \beta_{\nu}(y)\left(\gamma_{\nu}\right)^{i} \overline{\left(\gamma_{\nu}\right)^{j}} .$$
Moreover, we may assume that $\gamma_{1}, \ldots, \gamma_{N}$ contains an orthonormal basis for $\mathbb{C}^{n}$. From (4.4) and the mean value theorem again we obtain
$$\sum_{\nu=1}^{N} \beta_{\nu}\left(w_{\nu}(y)-w_{\nu}(x)\right) \leq C R, \quad \text { for } \quad w_{\nu}=\varphi_{\gamma_{\nu}} \overline{\gamma_{\nu}} .$$

We will obtain the desired estimate from (4.3), (4.6) and the following Harnack inequality (for its proof see Theorem 9.22 of [GT]).

Lemma 4.1. Let $g^{\prime}$ be a Hermitian metric on $U \subset \mathbb{C}^{n}$ which is uniformly equivalent to the Euclidean metric. Suppose that $v \geq 0$ satisfies
$$g^{\prime i \bar{j}} \partial_{i} \partial_{\bar{j}} v \leq \theta,$$
on $B_{2 R} \subset U$. Then there exist uniform constants $p>0$ and $C>0$ such that
$$\left(\frac{1}{R^{2 n}} \int_{B_{R}} v^{p}\right)^{1 / p} \leq C\left(\inf _{B_{R}} v+R\|\theta\|_{L^{2 n}\left(B_{2 R}\right)}\right) .$$

For $j=1,2$, write
$$M_{j \nu}=\sup _{B_{j R}} w_{\nu}, \quad m_{j \nu}=\inf _{B_{j R}} w_{\nu}, \quad \text { and } \quad \Omega(j R)=\sum_{\nu=1}^{N} \operatorname{osc}_{B_{j R}} w_{\nu}=\sum_{\nu=1}^{N}\left(M_{j \nu}-m_{j \nu}\right) .$$
Since each $w=w_{\nu}$ satisfies (4.3), we can apply Lemma 4.1 to $M_{2 \nu}-w_{\nu}$ to obtain
$$\left(\frac{1}{R^{2 n}} \int_{B_{R}}\left(M_{2 \nu}-w_{\nu}\right)^{p}\right)^{1 / p} \leq C\left(M_{2 \nu}-M_{1 \nu}+R^{2}\right) .$$
Thus for a fixed $\ell \in\{1, \ldots, N\}$, we have
$$\begin{aligned}
\left(\frac{1}{R^{2 n}} \int_{B_{R}}\left(\sum_{\nu \neq \ell}\left(M_{2 \nu}-w_{\nu}\right)\right)^{p}\right)^{1 / p} & \leq N^{1 / p} \sum_{\nu \neq \ell}\left(\frac{1}{R^{2 n}} \int_{B_{R}}\left(M_{2 \nu}-w_{\nu}\right)^{p}\right)^{1 / p} \\
& \leq C\left(\sum_{\nu \neq \ell}\left(M_{2 \nu}-M_{1 \nu}\right)+R^{2}\right) \\
& \leq C\left(\Omega(2 R)-\Omega(R)+R^{2}\right),
\end{aligned}$$
since
$$\left(M_{2 \nu}-m_{2 \nu}\right)-\left(M_{1 \nu}-m_{1 \nu}\right)=\left(M_{2 \nu}-M_{1 \nu}\right)+\left(m_{1 \nu}-m_{2 \nu}\right) \geq M_{2 \nu}-M_{1 \nu} .$$
But from (4.6), we have
$$\beta_{\ell}\left(w_{\ell}(y)-w_{\ell}(x)\right) \leq C R+\sum_{\nu \neq \ell} \beta_{\nu}\left(w_{\nu}(x)-w_{\nu}(y)\right) .$$
If we choose $x$ so that $w_{\ell}(x)$ approaches $m_{2 \ell}$ we obtain
$$w_{\ell}(y)-m_{2 \ell} \leq C\left(R+\sum_{\nu \neq \ell}\left(M_{2 \nu}-w_{\nu}(y)\right)\right) .$$
Integrating in $y$ over $B_{R}$ and applying (4.8) gives
$$\left(\frac{1}{R^{2 n}} \int_{B_{R}}\left(w_{\ell}-m_{2 \ell}\right)^{p}\right)^{1 / p} \leq C(\Omega(2 R)-\Omega(R)+R) .$$
On the other hand, from (4.7) we have
$$\left(\frac{1}{R^{2 n}} \int_{B_{R}}\left(M_{2 \ell}-w_{\ell}\right)^{p}\right)^{1 / p} \leq C(\Omega(2 R)-\Omega(R)+R) .$$
Adding (4.9) and (4.10) and summing over $\ell$ we have
$$\Omega(2 R) \leq C(\Omega(2 R)-\Omega(R)+R),$$
and hence
$$\Omega(R) \leq \delta \Omega(2 R)+C R$$
for a uniform $0<\delta<1$. It then follows by a standard argument (see [GT], Chapter 8) that there exist uniform constants $C$ and $\kappa>0$ such that
$$\Omega(R) \leq C R^{\kappa} .$$
The desired Hölder estimate on $\varphi_{i \bar{j}}$ and hence $g^{\prime}$ follows. This completes the proof of the main theorem.

Remark 4.1. In [Chr], Cherrier used the maximum principle to prove an analogue of Yau's [Ya] third order estimate of $\varphi$ for Hermitian $\omega$. For some related results, we refer the reader to: Calabi's paper [Ca2] which inspired Yau's computation; [PSS] for a concise proof of the parabolic version of this estimate; [To2] for a precise version of this estimate without assuming a $C^{2}$ estimate; and [TWY] for a generalization of the third order estimate in the setting of Donaldson's program [Do2].
5. Solving the Monge-Ampère equation. In this section we give a proof of Corollary 1. We use the continuity method and consider the family of equations
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=e^{t F+b_{t}} \omega^{n}, \quad \text { for } t \in[0,1],$$
with
$$\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}>0,$$
where $b_{t}$ is a constant for each $t$. Fix $\alpha$ with $0<\alpha<1$. We claim that (5.1), (5.2) can be solved for $\varphi_{t} \in C^{2, \alpha}(M)$ and $b_{t} \in \mathbb{R}$, for all $t \in[0,1]$. Consider the set
$$\begin{aligned}
\mathcal{T}=\left\{t^{\prime} \in[0,1] \mid\right. & \text { there exists } \varphi_{t} \in C^{2, \alpha}(M) \text { and } b_{t} \\
& \text { solving (5.1) and (5.2) for } \left.t \in\left[0, t^{\prime}\right]\right\} .
\end{aligned}$$

Clearly, $0 \in \mathcal{T}$. If we can show that $\mathcal{T}$ is both open and closed in [0, 1] then, using the higher order estimates given above, this proves the theorem. We first show that $\mathcal{T}$ is open. Assume $\hat{t}$ is in $\mathcal{T}$. We will show that there exists $\varepsilon>0$ such that $t \in \mathcal{T}$ for $t \in[\hat{t}, \hat{t}+\varepsilon)$.

Write $\hat{\omega}$ for the Hermitian metric
$$\hat{\omega}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{\hat{t}}>0 .$$
We wish to show that there exists $\psi_{t} \in C^{2, \alpha}$ for $t \in[\hat{t}, \hat{t}+\varepsilon)$ with $\psi_{\hat{t}}=0$, solving
$$\left(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi_{t}\right)^{n}=e^{(t-\hat{t}) F+b_{t}-b_{\hat{t}}} \hat{\omega}^{n},$$
for $b_{t}$ a function of $t$.
Applying Gauduchon's theorem to $\hat{\omega}$, we see that there is a function $\hat{u}$ such that $\hat{\omega}_{G}=e^{\hat{u}} \hat{\omega}$ is Gauduchon. We may assume by adding a constant to $\hat{u}$ that
$$\int_{M} e^{(n-1) \hat{u}} \hat{\omega}^{n}=1$$
We will show that we can find $\psi_{t} \in C^{2, \alpha}(M)$ for $t \in[\hat{t}, \hat{t}+\varepsilon)$ solving
$$\left(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi_{t}\right)^{n}=\left(\int_{M} e^{(n-1) \hat{u}}\left(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi_{t}\right)^{n}\right) e^{(t-\hat{t}) F+c_{t}} \hat{\omega}^{n}, \quad \text { for } t \in[\hat{t}, \hat{t}+\varepsilon)$$
where $c_{t}$ is chosen so that
$$\int_{M} e^{(t-\hat{t}) F+c_{t}} e^{(n-1) \hat{u}} \hat{\omega}^{n}=1$$
Notice that $c_{\hat{t}}=0$.
Define two Banach manifolds $B_{1}$ and $B_{2}$ by
$$B_{1}=\left\{\psi \in C^{2, \alpha}(M) \mid \int_{M} \psi e^{(n-1) \hat{u}} \hat{\omega}^{n}=0\right\}, B_{2}=\left\{h \in C^{\alpha}(M) \mid \int_{M} e^{h} e^{(n-1) \hat{u}} \hat{\omega}^{n}=1\right\} .$$
Define a linear operator $\Psi: B_{1} \rightarrow B_{2}$ by
$$\Psi(\psi)=\log \frac{(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi)^{n}}{\hat{\omega}^{n}}-\log \left(\int_{M} e^{(n-1) \hat{u}}(\hat{\omega}+\sqrt{-1} \partial \bar{\partial} \psi)^{n}\right) .$$
We wish to find $\psi_{t}$ solving $\Psi\left(\psi_{t}\right)=(t-\hat{t}) F+c_{t}$ for $t \in[\hat{t}, \hat{t}+\varepsilon)$.
Observe that $\Psi(0)=0$. By the inverse function theorem, to get openness of the equation (5.4) at $\psi=0$ we just need to show that
$$(D \Psi)_{0}: T_{0} B_{1}=B_{1} \longrightarrow T_{0} B_{2}=\left\{\rho \in C^{\alpha}(M) \mid \int_{M} \rho e^{(n-1) \hat{u}} \hat{\omega}^{n}=0\right\}$$
is invertible. Compute
$$(D \Psi)_{0}(\eta)=\Delta_{\hat{\omega}} \eta-n \int_{M} e^{(n-1) \hat{u}} \hat{\omega}^{n-1} \wedge \sqrt{-1} \partial \bar{\partial} \eta=\Delta_{\hat{\omega}} \eta,$$
where we are using the fact that
$$\partial \bar{\partial}\left(e^{(n-1) \hat{u}} \hat{\omega}^{n-1}\right)=\partial \bar{\partial}\left(\hat{\omega}_{\mathrm{G}}^{n-1}\right)=0 .$$
Recall that we can solve the equation $\Delta_{\hat{\omega}_{\mathrm{G}}} f=v$ as long as $\int_{M} v \hat{\omega}_{\mathrm{G}}^{n}=0$ (see e.g. [Bu]). Given $\rho \in T_{0} B_{2}$ we see that
$$\int_{M} \rho e^{-\hat{u}} \hat{\omega}_{\mathrm{G}}^{n}=0 .$$
Then if $\eta$ solves
$$e^{-\hat{u}} \Delta_{\hat{\omega}} \eta=\Delta_{\hat{\omega}_{\mathrm{G}}} \eta=\rho e^{-\hat{u}}$$
we have
$$\Delta_{\hat{\omega}} \eta=\rho,$$
as required. This shows that we can find $\psi_{t}$ solving (5.4) for $t \in[\hat{t}, \hat{t}+\varepsilon)$ as required. Thus $\mathcal{T}$ is open.

To prove that $\mathcal{T}$ is closed we need estimates on both $\varphi_{t}$ and $b_{t}$. Because of our Main Theorem, it suffices to show that $b_{t}$ is uniformly bounded. But from (5.1) we see that if $\varphi_{t}$ achieves a maximum at a point $x$ in $M$ we have $t F(x)+b_{t} \leq 0$. Combining this with a similar argument at minimum of $\varphi_{t}$, we obtain
$$\left|b_{t}\right| \leq \sup _{M}|F| .$$
This completes the proof of Corollary 1.
Remark 5.1. We end this section with a remark about uniqueness, that dates back to [Ca1]. Solutions $\varphi$ to (1.1), (1.2) are unique for a given fixed $F$. To see this, let $\varphi_{1}$ and $\varphi_{2}$ satisfy
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{1}\right)^{n}=\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{2}\right)^{n},$$
with $\sup _{M} \varphi_{1}=0=\sup _{M} \varphi_{2}$. Then, writing $\omega_{j}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{j}$ for $j=1,2$ and $\theta=\varphi_{1}-\varphi_{2}$, we see that
$$\sqrt{-1} \partial \bar{\partial} \theta \wedge \sum_{i=0}^{n-1} \omega_{1}^{i} \wedge \omega_{2}^{n-1-i}=0$$
and it follows by the strong maximum principle that $\theta=0$. Moreover, the constant $b$ in (1.6) is unique by a simple maximum principle argument (see [Chr]).
6. Prescribing the first Chern form. In this section, we prove Corollary 2. First we describe some terminology. If $g$ is a Hermitian metric and $\omega$ its associated (1, 1)-form, we will denote by $\operatorname{Ric}(\omega)$ the first Chern form of the canonical connection
of $g$, defined as follows: if $R_{j k \bar{\ell}}^{i}$ is the curvature of the canonical connection of $g$, we let $R_{k \bar{\ell}}=\sum_{i} R_{i k \bar{\ell}}^{i}$ and
$$\operatorname{Ric}(\omega)=\frac{\sqrt{-1}}{2 \pi} \sum_{k, \ell} R_{k \bar{\ell}} d z^{k} \wedge d \overline{z^{\ell}} .$$
$\operatorname{Ric}(\omega)$ is a closed real (1, 1)-form, cohomologous to the first Chern class $c_{1}(M)$.
We now give the proof of Corollary 2. First notice the standard transgression formula (see e.g. [TWY, (3.16)])
$$\operatorname{Ric}(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)-\operatorname{Ric}(\omega)=-\frac{\sqrt{-1}}{2 \pi} \partial \bar{\partial} \log \frac{(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{2}}{\omega^{2}},$$
and so integration by parts shows that (1.7) implies (1.8).
Conversely, assume that (1.8) holds. Let $\Delta_{G}$ be the canonical Laplacian of $\omega_{G}$. Because of (1.8), there exists a smooth function $f$ such that
$$\frac{\Delta_{G} f}{2 \pi}=\frac{2(\operatorname{Ric}(\omega)-\psi) \wedge \omega_{G}}{\omega_{G}^{2}} .$$
We claim that in fact we have
$$\operatorname{Ric}(\omega)=\psi+\frac{\sqrt{-1}}{2 \pi} \partial \bar{\partial} f .$$
To see this, call $a=\operatorname{Ric}(\omega)-\psi-\frac{\sqrt{-1}}{2 \pi} \partial \bar{\partial} f$, and notice that $a$ is an exact real $(1,1)$ form that satisfies
$$\omega_{G} \wedge a=0 .$$
Thus $a$ is $\omega_{G}$-anti-selfdual, and since it is exact it has to be zero because
$$0=\int_{M} a^{2}=-\|a\|_{L^{2}\left(\omega_{G}\right)}^{2}$$
By Corollary 1 there exist a constant $b$ and a Hermitian metric $\omega+\sqrt{-1} \partial \bar{\partial} \varphi$ such that
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{2}=e^{f+b} \omega^{2} .$$
Combining (6.3) with (6.1) and (6.2) gives (1.7). This completes the proof of Corollary 2.

Remark 6.1. It follows from the proof of Corollary 2 that (1.8) is equivalent to the statement that $\operatorname{Ric}(\omega)-\psi$ is $\partial \bar{\partial}$-exact, and thus if (1.8) holds for one Gauduchon metric then it holds for all. Clearly, in the Kähler case (1.8) is always satisfied.

Acknowledgements. The authors would like to thank S.-T. Yau for many useful discussions on the complex Monge-Ampère equation and also on the balanced condition. The authors express their gratitude to D.H. Phong for his support, encouragement and helpful suggestions. In addition the authors thank V. Apostolov, L. Ni, J. Song, G. Székelyhidi and L.-S. Tseng for some helpful discussions. We thank X. Zhang for sending us his related preprint [Zh], from which we also learned about the reference [Chr].

\section*{REFERENCES}
\begin{itemize}
\item[] [Au] T. Aubin, Équations du type Monge-Ampère sur les variétés kählériennes compactes, Bull. Sci. Math. (2), 102:1 (1978), pp. 63-95.
\item[] [AB] L. Alessandrini and G. Bassanelli, Modifications of compact balanced manifolds, C. R. Acad. Sci. Paris Sér. I Math., 320 (1995), pp. 1517-1522.
\item[] [BBFTY] K. Becker, M. Becker, J. Fu, L.-S. Tseng, and S.-T. Yau, Anomaly cancellation and smooth non-Kähler solutions in heterotic string theory, Nuclear Phys. B, 751:1-2 (2006), pp. 108-128.
\item[] [BT] E. Bedford and B. A. Taylor, Variational properties of the complex Monge-Ampère equation, II. Intrinsic norms, Amer. J. Math., 101 (1979), pp. 1131-1166.
\item[] [B11] Z. Blocki, On uniform estimate in Calabi-Yau theorem, Proc. SCV2004, Beijing, Science in China Series A Mathematics, 48 Supp. (2005), pp. 244-247.
\item[] [B12] Z. Blocki, On geodesics in the space of Kähler metrics, preprint 2009.
\item[] [Bu] N. Buchdahl, On compact Kähler surfaces, Ann. Inst. Fourier (Grenoble), 49:1 (1999), pp. 287-302.
\item[] [CKNS] L. Caffarelli, J. J. Kohn, L. Nirenberg, and J. Spruck, The Dirichlet problem for nonlinear second-order elliptic equations. II. Complex Monge-Ampère, and uniformly elliptic equations, Comm. Pure Appl. Math., 38:2 (1985), pp. 209-252.
\item[] [Ca1] E. Calabi, On Kähler manifolds with vanishing canonical class, in "Algebraic geometry and topology. A symposium in honor of S. Lefschetz", pp. 78-89. Princeton University Press, Princeton, N. J., 1957.
\item[] [Ca2] E. Calabi, Improper affine hyperspheres of convex type and a generalization of a theorem by K. Jörgens, Michigan Math. J., 5 (1958), pp. 105-126.
\item[] [Chn] X. X. Chen, The space of Kähler metrics, J. Differential Geom., 56 (2000), pp. 189-234.
\item[] [CLN] S. S. Chern, H. I. Levine, and L. Nirenberg, Intrinsic norms on a complex manifold, 1969 Global Analysis (Papers in Honor of K. Kodaira), pp. 119-139, Univ. Tokyo Press, Tokyo.
\item[] [Chr] P. Cherrier, Équations de Monge-Ampère sur les variétés Hermitiennes compactes, Bull. Sc. Math (2), 111 (1987), pp. 343-385.
\item[] [De] P. DelanoE, Équations du type de Monge-Ampère sur les variétés Riemanniennes compactes, II, J. Functional Anal., 41 (1981), pp. 341-353.
\item[] [Do1] S. K. Donaldson, Symmetric spaces, Kähler geometry and Hamiltonian dynamics, Northern California Symplectic Geometry Seminar, pp. 13-33, Amer. Math. Soc. Transl. Ser. 2, 196, Amer. Math. Soc., Providence, RI, 1999.
\item[] [Do2] S. K. Donaldson, Two-forms on four-manifolds and elliptic equations, in Inspired by S.S. Chern, World Scientific, 2006.
\item[] [Ev] L. C. Evans, Classical solutions of fully nonlinear, convex, second order elliptic equations, Comm. Pure Appl. Math, 25 (1982), pp. 333-363.
\item[] [FIUV] M. Fernández, S. Ivanov, L. Ugarte, R. Villacampa, Non-Kaehler heterotic string compactifications with non-zero fluxes and constant dilaton, Comm. Math. Phys., 288:2 (2009), pp. 677-697.
\item[] [FPS] A. Fino, M. Parton, and S. Salamon, Families of strong KT structures in six dimensions, Comment. Math. Helv., 79:2 (2004), pp. 317-340.
\item[] [FT] A. Fino and A. Tomassini, On astheno-Kähler metrics, preprint, arXiv:0806.0735.
\item[] [FLY] J. Fu, J. Li, and S.-T. Yau, Constructing balanced metrics on some families of non-Kähler Calabi-Yau threefolds, preprint, arXiv:0809.4748.
\item[] [FY] J. Fu and S.-T. Yau, The theory of superstring with flux on non-Kähler manifolds and the complex Monge-Ampère equation, J. Differential Geom., 78:3 (2008), pp. 369-428.
\item[] [Ga1] P. Gauduchon, Le théorème de l'excentricité nulle, C. R. Acad. Sci. Paris, 285 (1977), pp. 387-390.
\item[] [Ga2] P. Gauduchon, Fibrés hermitiens à endomorphisme de Ricci non négatif, Bull. Soc. Math. France, 105:2 (1977), pp. 113-140.
\item[] [Ga3] P. Gauduchon, La 1-forme de torsion d'une variété hermitienne compacte, Math. Ann., 267 (1984), pp. 495-518.
\item[] [GT] D. Gilbarg and N. S. Trudinger, Elliptic partial differential equations of second order, Springer-Verlag, 1983.
\item[] [GuB] B. Guan, The Dirichlet problem for the complex Monge-Ampère equation and regularity of the pluricomplex Green's function, Comm. Anal. Geom., 6:4 (1998), pp. 687-703; correction in Comm. Anal. Geom., 8:1 (2000), pp. 213-218.
\item[] [GuP] P.-F. Guan, Extremal functions related to intrinsic norms, Annals of Math., 156 (2002),
\end{itemize}
\begin{itemize}
\item[] pp. 197-211.
\item[] [GL] B. Guan and Q. Li, Complex Monge-Ampère equations on Hermitian manifolds, preprint, arXiv:0906.3548.
\item[] [Ko] S. Kolodziej, The complex Monge-Ampère equation, Acta Math., 180 (1998), pp. 69-117.
\item[] [Kr] N. V. Krylov, Boundedly nonhomogeneous elliptic and parabolic equations, Izvestia Akad. Nauk. SSSR, 46 (1982), pp. 487-523. English translation in Math. USSR Izv., 20:3 (1983), pp. 459-492.
\item[] [Ma] T. Mabuchi, Some symplectic geometry on compact Kähler manifolds. I, Osaka J. Math., 24 (1987), pp. 227-252.
\item[] [Mi] M. L. Michelsohn, On the existence of special metrics in complex geometry, Acta Math., 149 (1982), pp. 261-295.
\item[] [PSS] D. H. Phong, N. Šešum, and J. Sturm, Multiplier Ideal Sheaves and the Kähler-Ricci Flow, Comm. Anal. Geom., 15:3 (2007), pp. 613-632.
\item[] [PS] D. H. Phong and J. Sturm, The Dirichlet problem for degenerate complex Monge-Ampère equations, preprint, arXiv:0904.1898.
\item[] [Po] A. V. Pogorelov, The regularity of the generalized solutions of the equation $\operatorname{det}\left(\partial^{2} u / \partial x^{i} \partial x^{j}\right)=\varphi\left(x^{1}, x^{2}, \ldots, x^{n}\right)>0$, Dokl. Akad. Nauk SSSR, 200 (1971), pp. 534-537. English translation in Soviet Math. Dokl., 12 (1971), pp. 1436-1440.
\item[] [Se] S. Semmes, Complex Monge-Ampère and symplectic manifolds, Amer. J. Math., 114 (1992), pp. 495-550.
\item[] [Si] Y.-T. Siu, Lectures on Hermitian-Einstein metrics for stable bundles and Kähler-Einstein metrics, DMV Seminar, 8. Birkhäuser Verlag, Basel, 1987.
\item[] [ST] J. Streets and G. Tian, Hermitian curvature flow, preprint, arXiv:0804.4109.
\item[] [To1] V. Tosatti, A general Schwarz Lemma for almost-Hermitian manifolds, Comm. Anal. Geom., 15:5 (2007), pp.1063-1086.
\item[] [To2] V. Tosatti, Adiabatic limits of Ricci-flat Kähler metrics, preprint, arXiv:0905.4718, to appear in J. Differential Geom. 2010.
\item[] [TW1] V. Tosatti and B. Weinkove, The Calabi-Yau equation, symplectic forms and almost complex structures, preprint, arXiv:0901.1501, to appear in "Geometric Analysis: Present and Future", International Press, 2010.
\item[] [TW2] V. Tosatti and B. Weinkove, The Calabi-Yau equation on the Kodaira-Thurston manifold, preprint, arXiv:0906.0634.
\item[] [TWY] V. Tosatti, B. Weinkove, and S.-T. Yau, Taming symplectic forms and the Calabi-Yau equation, Proc. London Math. Soc., 97:2 (2008), pp. 401-424.
\item[] [Tr] N. S. Trudinger, Fully nonlinear, uniformly elliptic equations under natural structure conditions, Trans. Amer. Math. Soc., 278:2, (1983), pp. 751-769.
\item[] [We1] B. Weinkove, Convergence of the $J$-flow on Kähler surfaces, Comm. Anal. Geom., 12:4 (2004), pp. 949-965.
\item[] [We2] B. Weinkove, On the J-flow in higher dimensions and the lower boundedness of the Mabuchi energy, J. Differential Geom., 73:2 (2006), pp. 351-358.
\item[] [We3] B. Weinkove, The Calabi-Yau equation on almost-Kähler four-manifolds, J. Differential Geom., 76:2 (2007), pp. 317-349.
\item[] [Ya] S.-T. Yau, On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I, Comm. Pure Appl. Math., 31:3 (1978), pp. 339-411.
\item[] [Zh] X. Zhang, A priori estimates for complex Monge-Ampère equation on Hermitian manifolds, preprint.
\end{itemize}