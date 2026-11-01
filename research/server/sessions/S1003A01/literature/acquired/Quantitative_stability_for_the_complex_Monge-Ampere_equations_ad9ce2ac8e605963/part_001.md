---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Quantitative stability for the complex Monge-Ampere equations]

---
source_file: 2209_00248.pdf
converter: mathpix
format: mmd
---

\title{
Quantitative stability for the complex Monge-Ampère equations
}

\author{
Hoang-Son Do and Duc-Viet Vu
}

December 1, 2022

\begin{abstract}
We prove several quantitative stability estimates for solutions of complex Monge-Ampère equations when both the cohomology class and the prescribed singularity vary. In a broad sense, our results fit well into the study of degeneration of families of Kähler-Einstein metrics. The key mechanism in our method is the pluripotential theory in the space of potentials of finite lower energy.
\end{abstract}

Keywords: Monge-Ampère equation, convex weights, lower energy, non-pluripolar products.

Mathematics Subject Classification 2010: 32U15, 32Q15.

\section*{Contents}
1 Introduction ..... 2
1.1 Statement of main results ..... 5
1.2 Key components in our method ..... 9
2 Preliminaries ..... 11
2.1 Integration by parts ..... 11
2.2 Auxiliary facts on weights ..... 15
3 Stability estimates for fixed singularity type ..... 21
3.1 Main results ..... 21
3.2 Proof of Theorem 3.1 ..... 22
3.3 Proof of Theorem 3.2 ..... 30
3.4 Applications ..... 34
3.4.1 Quantitative version for the domination principle ..... 34
3.4.2 Quantitative version of Dinew's uniqueness theorem ..... 36
3.4.3 Relation to Darvas's metrics on the space of potentials of finite energy ..... 38
3.4.4 Comparison of capacities ..... 40
4 Stability estimates for varied singularity type and cohomology class ..... 42
4.1 Pseudo-metric on the space of singularity types ..... 42
4.2 The case of fixed cohomology ..... 45
4.2.1 Proof of Theorem 1.2 ..... 45
4.2.2 Proof of Theorems 1.3 and 1.4 ..... 51
4.3 Application to the space of singularity types ..... 55
4.4 The case of varied cohomology ..... 58

\section*{1 Introduction}

Let $(X, \omega)$ be a compact Kähler manifold of dimension $n$ and let $\alpha$ be a big cohomology $(1,1)$-class in $X$. Let $\theta$ be a closed smooth real ( 1,1 )-form in $\alpha$ and let $\mu$ be a non-pluripolar finite measure on $X$. Consider the complex Monge-Ampère equation
$$\theta_{u}^{n}=\mu,$$
where $u$ is a $\theta$-psh function, and $\theta_{u}:=d d^{c} u+\theta$, and the left-hand side of (1.1) denotes the non-pluripolar self-product of $\theta_{u}$ (see [1, 8, 34, 67]). By monotonicity of non-pluripolar products (see [16, 67, 69]), if (1.1) has a solution, then it is necessary that $\mu(X) \leq \operatorname{vol}(\alpha)$, where $\operatorname{vol}(\alpha)$ denotes the volume of the big class $\alpha$. When $\mu(X)=\operatorname{vol}(\alpha)$, the equation (1.1) admits a unique solution by [8, 9, 23, 41, 72], and this solution is of minimal singularity in $\alpha$ if $\mu$ is sufficiently regular (for example, $\mu$ has a $L^{p}(p>1)$ density with respect to a smooth volume form on $X$ ).

One expects that the regularity of solutions agrees well with that of the measure $\mu$. This expectation is true at least for the following two classes of extreme regularities. The first one is the class of measures which are Hölder continuous as a linear functional on the space $\mathrm{PSH}_{0}(X, \omega)$ of $\omega$-psh functions $u$ with $\int_{X} u \omega^{n}=0$ endowed with $L^{1}$-metric (we call such measures Hölder continuous ones). The second one is the class of measures of finite lower energy (i.e, non-pluripolar measures). These two classes are important because they are two regularities governing the range of measures where (1.1) is solvable (within the framework of the theory of non-pluripolar products of currents). We refer to [19, 25, 27, 32, 46, 44, 50, 52, 53, 58, 65, 66] and references therein for more informations in the setting where $\mu(X)=\operatorname{vol}(\alpha)$.

Consider now the case where the mass of $\mu$ is not necessarily equal to $\operatorname{vol}(\alpha)$, i.e, where $\mu(X) \leq \operatorname{vol}(\alpha)$. In this case one can still solve (1.1) by putting it in the context of prescribed singularity. We need several notions. Denote by $\operatorname{PSH}(X, \theta)$ the set of $\theta$-psh functions. Let $u_{1}, u_{2} \in \operatorname{PSH}(X, \theta)$. Recall that $u_{1}$ is more singular than $u_{2}$ if $u_{1} \leq u_{2}+O(1)$, and $u_{1}$ is of the same singularity type as $u_{2}$ if $u_{1}-u_{2}$ is bounded.

Let $\phi \in \operatorname{PSH}(X, \theta)$ such that $\phi \leq 0$ and $\int_{X} \theta_{\phi}^{n}>0$. Denote by $\operatorname{PSH}(X, \theta, \phi)$ the set of $\theta$-psh functions $u$ with $u \leq \phi$. Note that it is slightly different from the usual definition of $\operatorname{PSH}(X, \theta, \phi)$ in which $u$ is only required to be more singular than $\phi$. This difference is not essential. We say that $\phi$ is a model $\theta$-psh function (see [16, 54]) if $\phi=P_{\theta}[\phi]$ and $\int_{X} \theta_{\phi}^{n}>0$, where
$$P_{\theta}[\phi]:=(\sup \{\psi \in \operatorname{PSH}(X, \theta): \psi \leq 0, \psi \leq \phi+O(1)\})^{*} .$$

The function $P_{\theta}[\phi]$ is called a roof-top envelope in [16]. By [16], the function $P_{\theta}[u]$ is a model one for every $u \in \operatorname{PSH}(X, \theta)$ with $\int_{X} \theta_{u}^{n}>0$, and for every $u \in \operatorname{PSH}(X, \theta, \phi)$ with $\int_{X} \theta_{u}^{n}=\int_{X} \theta_{\phi}^{n}$ we have $P_{\theta}[u]=P_{\theta}[\phi]$.

Let $\phi$ be now a model $\theta$-psh function. Let $\mu$ be a non-pluripolar measure with $\mu(X)=$ $\int_{X} \theta_{\phi}^{n}$. We want to solve the equation
$$\left(d d^{c} u+\theta\right)^{n}=\mu,$$
for $u \in \operatorname{PSH}(X, \theta, \phi)$ and $\sup _{X}(u-\phi)=0$. We note that since $\phi$ is a model, if $u \in \operatorname{PSH}(X, \theta)$ such that $u \leq 0$ and $u \leq \phi+O(1)$, then $u \leq \phi$, and $\sup _{X}(u-\phi)=\sup _{X} u$. Thus the normalization condition $\sup _{X}(u-\phi)=0$ can be rewritten as $\sup _{X} u=0$.

The hypothesis that $\phi$ is model is a minimal requirement so that (1.2) is solvable in a meaningful way; see [16] for an explanation about the nature of this assumption. Let $\mathcal{E}(X, \theta, \phi)$ be the set of $u \in \operatorname{PSH}(X, \theta, \phi)$ such that $\int_{X} \theta_{u}^{n}=\int_{X} \theta_{\phi}^{n}$. By [17] (or [16, 32]), the equation (1.2) admits a unique solution in $\mathcal{E}(X, \theta, \phi)$, and if $\mu$ has $L^{p}$ density then the solution is of the same singularity type as $\phi$. Furthermore a characterization of the class of measures $\mu$ where (1.2) admits a solution of finite pluricomplex energy was given in [32].

A $\theta$-singularity type (in $\alpha$ ) is an equivalence class of $\theta$-psh functions of the same singularity type. The space of $\theta$-singularity types is denoted by $\mathcal{S}(\theta)$ (or $\mathcal{S}(\alpha)$ when $\theta$ is clear from the context). A natural pseudo-metric $d_{\mathcal{S}(\theta)}$ in $\mathcal{S}(\theta)$ was introduced in [18]. We refer to Section 4 for a recap of this pseudodistance. A model $\theta$-singularity type is by definition the class of a model $\theta$-psh function. By [16, Theorem 1.3], every model $\theta$-singularity type contains a unique model $\theta$-psh function. Hence there is a 1-1 correspondence between model $\theta$-singularity types and model $\theta$-psh functions. For $u \in \operatorname{PSH}(X, \theta)$, we denote by $[u]_{\theta}$ (or simply $[u]$ when $\theta$ is clear) the $\theta$-singularity type of $u$. To ease the notation we will denote by $d_{\mathcal{S}(\theta)}(u, v)$ the distance $d_{\mathcal{S}(\theta)}\left([u]_{\theta},[v]_{\theta}\right)$.

In Proposition 4.3 (in Section 4), we push further the study of metrics on the space of singularity types by observing that if we embed $\mathcal{S}(\theta)$ into a bigger space $\mathcal{S}\left(\theta^{\prime}\right)$ for $\theta^{\prime} \geq \theta$ (notice that $\theta^{\prime}$ is not necessarily in the cohomology class of $\theta$ ), then the pseudodistance $d_{\mathcal{S}(\theta)}$ is actually comparable with that induced by $d_{\mathcal{S}\left(\theta^{\prime}\right)}$. This allows us to compare singularity types in different cohomology classes without changing the nature of the distance $d_{\mathcal{S}(\theta)}$. By this we will sometimes ignore $\theta$ and only write $d_{\mathcal{S}}$. In view of the resolution of (1.2), we are led to the following natural stability question. We fix a $\mathscr{C}^{0}$-norm on the space of smooth (1, 1)-forms on $X$.

Problem 1.1. Let $\theta_{1}, \theta_{2}$ be closed smooth real (1, 1)-forms on $X$. Let $\phi_{j}$ be model $\theta_{j}$-psh functions and $\mu_{j}$ be a non-pluripolar measure of mass equal to $\int_{X} \theta_{\phi_{j}}^{n}$ for $j=1,2$. Let $u_{j}$ be the solution of (1.2) for $\mu_{j}, \phi_{j}$ for $j=1,2$. Compare $u_{1}$ with $u_{2}$ in terms of $d_{\mathcal{S}}\left(\phi_{1}, \phi_{2}\right)$, $\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}$, and a suitable distance between $\mu_{1}, \mu_{2}$ ?

Here by $d_{\mathcal{S}}\left(\phi_{1}, \phi_{2}\right)$, we mean $d_{\mathcal{S}(A \omega)}\left(\phi_{1}, \phi_{2}\right)$, where $A$ is a big constant so that $\theta_{j} \leq$ $A \omega$ for $j=1,2$. As discussed above, the condition that $d_{\mathcal{S}(A \omega)}\left(\phi_{1}, \phi_{2}\right)$ converges to 0 is independent of the choice of $A$. To get motivated about the above problem, let's consider the following simple situation. Let $\left(\alpha_{j}\right)_{j}$ be a sequence of cohomology Kähler $(1,1)$-classes converging to a big class $\alpha_{\infty}$ as $j \rightarrow \infty$. We know that there exists a unique closed positive
$(1,1)$-current $T_{j} \in \alpha_{j}$ such that $T_{j}^{n}=\operatorname{vol}\left(\alpha_{j}\right) \omega^{n} / \int_{X} \omega^{n}$. One thus asks further: what can we say about the convergence of the sequence $\left(T_{j}\right)_{j}$ ? Even when $\alpha_{\infty}$ is also Kähler, it seems that known methods are not sufficient to deal with such a question.

We will develop in this paper a quite satisfactory method to treat the above stability problem. The emphasis of our approach is the quantitative point of view. As it will be clear later, even when one is only interested in obtaining qualitative stability as in the above simplified situation (with varied cohomology classes), it is still essential in proofs to obtain beforehand quantitative stability estimates. To be more precise, one of the main protagonists in our work is a quantitative stability for solutions to (1.2) of finite lower energy in the setting where the cohomology class and the prescribed singularity are fixed, i.e, where $\theta$ and $\phi$ are fixed. To our best knowledge, no such estimate was established in the literature. Consider in the simplest setting when $\theta=\omega$ and $\phi=0$, and let $\mu_{j}=\left(d d^{c} u_{j}+\omega\right)^{n}$ be a non-pluripolar measure of mass equal to $\int_{X} \omega^{n}$ and $\sup _{X} u_{j}=0$ for $j=1,2$. If $\mu_{1}=\mu_{2}$, then it is well-known that $u_{1}=u_{2}$ by [23]. However there has been no available result comparing $u_{1}, u_{2}$ when $\mu_{1}, \mu_{2}$ are close to each other. This is due to the fact that arguments in [23] (and in other known proofs of this uniqueness property, see ([8, 16, 23, 50]) are non-quantitative.

In another aspect, the stability of solutions when the cohomology class varies is closely related to the question of degenerations of special Kähler metrics on manifolds, or more generally, families of Kähler-Einstein metrics. There is rich literature on this topic; see for example [20, 39, 38, 56, 55, 59]. We would like to stress that although in some typical model of degenerations of Ricci flat Kähler metric an optimal local $\mathscr{C}^{\infty}$ convergence of potentials (i.e, solutions) on some Zariski open subset of the ambient manifold was obtained in [39, 38, 56, 55], it seems that the global convergence of potentials (solutions) has not been well-studied. Our work fits well into this research direction.

The first stability result for varied prescribed singularities, which is not quantitative, was given in [18, Theorem 1.4]. Previously there were several stability results in the fixed prescribed singularity setting in the literature: some are quantitative and some are not. We refer to [2, 7, 24, 43, 45, 35, 50, 66] and references therein for more details. Key technical tools to obtain quantitative stability has been so far (variants of) Kołodziej's capacity method ([43]) and an integration by parts arguments originally in [7]. All of these cited results require the measures in the right-hand side of the Monge-Ampère equations to be sufficiently regular (to be more precise, measures must be at least the Monge-Ampère of $\theta$-psh functions in $\left.\mathcal{E}^{1}(X, \theta)\right)$.

Finally, we underline that our interest in the stability of solutions also comes from complex dynamics because equilibrium measures associated to holomorphic dynamical systems are, in many important cases, natural Monge-Ampère measures; see [28, 31]. Stability of solutions of (1.1) is hence relevant to the bifurcation theory of these holomorphic dynamical systems (see [5]). We refer [57] for a recent application of Monge-Ampère equations to dynamical systems and vice versa.

We would like to inform that in a forthcoming paper the second-named author will apply the method in this paper to attack the problem of degeneration of conic Kähler-Einstein metrics proposed in [6].

\subsection*{1.1 Statement of main results}

In order to motivate readers about our first main result, let us consider the following simple setting. Let $\omega$ be a Kähler form on $X$. Let $u, v$ bounded negative $\omega$-psh functions. For measures $\mu, \nu$ on $X$, we denote by $\|\mu-\nu\|$ the mass norm of $\mu-\nu$. It was proved by Błocki [7] that
$$\int_{X} d(u-v) \wedge d^{c}(u-v) \wedge \omega^{n-1} \leq C_{M, n}\left(\int_{X}(u-v)\left(\omega_{v}^{n}-\omega_{u}^{n}\right)\right)^{2^{1-n}},$$
where $M$ is an upper bound for $\|u\|_{L^{\infty}}+\|v\|_{L^{\infty}}$, and $C_{M, n}$ is a constant depending only on $n, M$. This combined with Poincaré's inequality gives
$$\|u-v\|_{L^{1}} \leq C_{\omega, M, n}\left\|\omega_{u}^{n}-\omega_{v}^{n}\right\|^{2^{-n}},$$
where $C_{\omega, M, n}$ is a constant depending on $\omega, M, n$. One can indeed make $C_{\omega, M, n}$ independent of $\omega$ (but dependent on $\int_{X} \omega^{n}$ ) but the exponent in the right-hand side of (1.4) must be changed a bit. We will ignore, for the moment, this detail. The stability estimate (1.4) is the starting point of our journey in this paper. Observe that the constant $C_{\omega, M, n}$ in the right-hand side of (1.4) depends both on $u$ and $v$, or more generally, on the regularity of both $\omega_{u}^{n}$ and $\omega_{v}^{n}$ (because for example if the latter measures have $L^{p}$ density for some $p>1$, then $u, v$ are bounded by constants depending only on the $L^{p}$-norm of the densities). An instance of our first main result, Theorem 1.2 below, is that an estimate similar to (1.4) still holds if only the information on the regularity of $\omega_{u}^{n}$ is available. Concretely a direct consequence of Theorem 1.2 (applied to $\tilde{\chi}(t)=t$ ) in the setting in consideration is that there exist an explicit constant $0<\gamma<1$ such that if $\omega_{u}^{n}=g \omega^{n}$ for some $g \in L^{p}$, then there is a constant $C_{g, \omega, n}$ depending on $\omega$ (and $n$ ), and an upper bound of $\|g\|_{L^{p}}$ so that
$$\|u-v\|_{L^{1}} \leq C_{g, \omega, n}\left\|\omega_{u}^{n}-\omega_{v}^{n}\right\|^{\gamma},$$
for every bounded $\omega$-psh function $v$ (notice $C_{g, \omega, n}$ is independent of $v$ ). The key ingredient of the proof of the last inequality is the following generalization of (1.3): for $u \leq v$ and for every bounded or not $\mathscr{C}^{1}$ convex functions $\chi, \tilde{\chi}$ with $\chi(0)=\tilde{\chi}(0)=0$ and $\tilde{\chi} \leq \chi$, there holds
$$\int_{X} \chi^{\prime}(u-v) d(u-v) \wedge d^{c}(u-v) \wedge \omega^{n-1} \leq C_{N} f_{\chi, \tilde{\chi}}\left(\int_{X}-\chi(u-v)\left(\omega_{v}^{n}-\omega_{u}^{n}\right)\right)$$
where $C_{N}$ is an explicit constant depending on $\tilde{\chi}$-energies of $u, v$, and $f_{\chi, \tilde{\chi}}$ is an explicit continuous function depending on $\chi, \tilde{\chi}$ and satisfying $f_{\chi, \tilde{\chi}}(0)=0$; see Proposition 3.5 in Section 3 or the next subsection for details. In order to prove (1.5), we apply (1.6) essentially to $\chi(t):=\max \{t,-1\}$, and $\tilde{\chi}(t)=\max \{t,-A\}$ for some suitable big constant $A>0$.

The proof of (1.6) reveals the core of our method and is not a direct generalization of the arguments in the proof of (1.3) in [7] which treats the case where $\chi(t)=\tilde{\chi}(t)=t$. We will explain more in the next subsection 1.2 about this point. With the above preparation,
we are now in position to state our first main result in full generality. To this end, we need some more notations.

For every Borel set $E$ in $X$, recall that the capacity of $E$ is given by
$$\operatorname{cap}(E)=\operatorname{cap}_{\omega}(E):=\sup _{\{w \in \operatorname{PSH}(X, \omega): 0 \leq w \leq 1\}} \int_{E} \omega_{w}^{n} .$$
We usually remove the subscript $\omega$ from $\operatorname{cap}_{\omega}$ if $\omega$ is clear from the context. There are generalizations of capacity in big cohomology classes, many of them are comparable; see Theorem 3.17 below and [48]. Recall that a sequence of Borel functions $\left(u_{j}\right)_{j}$ is said to converge to a Borel function $u$ in capacity if for every constant $\epsilon>0$, we have that $\operatorname{cap}\left(\left\{\left|u_{j}-u\right| \geq \epsilon\right\}\right)$ converges to 0 as $j \rightarrow \infty$. The convergence in capacity is of great importance in pluripotential theory in part because it implies the convergence of Monge-Ampère operators under reasonable circumstances. To study quantitatively the convergence in capacity, it is convenient to introduce the following distance function on $\operatorname{PSH}(X, \omega)$ :
$$d_{\text {cap }}(u, v):=\sup _{w \in \operatorname{PSH}(X, \omega): 0 \leq w \leq 1} \int_{X}|u-v|^{1 / 2} \omega_{w}^{n}$$
for every $u, v \in \operatorname{PSH}(X, \omega)$ (note that $d_{\text {cap }}(u, v)<\infty$ thanks to the Chern-Levine-Nirenberg inequality). The number $\frac{1}{2}$ in the definition of $d_{\text {cap }}$ can be replaced by any constant in (0, 1). One can see that for $u_{j}, u \in \operatorname{PSH}(X, \omega)$ for $j \in \mathbb{N}, d_{\text {cap }}\left(u_{j}, u\right) \rightarrow 0$ if and only if $\left|u_{j}-u\right| \rightarrow 0$ in capacity.

For $\theta$-psh functions $u, v$, we put
$$d_{\theta}(u, v):=2 \int_{X} \theta_{\max \{u, v\}}^{n}-\int_{X} \theta_{u}^{n}-\int_{X} \theta_{v}^{n} .$$
The function $d_{\theta}$ is comparable to $d_{\mathcal{S}(\theta)}$ (see Proposition 4.3). For quantitative estimates, it is more convenient to use $d_{\theta}$ than $d_{\mathcal{S}(\theta)}$. It is perhaps worth noting that our method to prove the stability results below also implies that $d_{\text {cap }}$ is bounded from above by a power of $d_{\theta}$ for model $\theta$-potentials (see Proposition 4.14 for details).

Let $\mathcal{W}^{-}$be the set of convex increasing functions $\chi: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ so that $\chi(0)=0$ and $\chi(-\infty)=-\infty$. It follows from [8, Proposition 3.2] that for every non-positive $\theta$-psh function $u$, there exists $\chi \in \mathcal{W}^{-}$and $C>0$ such that
$$-\int_{X} \psi \theta_{u}^{n} \leq C,$$
for every $\psi \in \operatorname{PSH}(X, \omega)$ with $\sup _{X} \psi=0$.
Theorem 1.2. Let $\theta$ be a closed smooth real (1, 1)-form such that $\theta \leq A \omega$ for a given constant $A \geq 1$. Let $u \in \operatorname{PSH}(X, \theta)$ such that $\sup _{X} u=0$ and $\int_{X} \theta_{u}^{n}:=\delta>0$. Let $B \geq A$ and $\tilde{\chi} \in \mathcal{W}^{-}$ with $\tilde{\chi}(-1)=-1$ such that
$$\int_{X}-\tilde{\chi}(\psi) \theta_{u}^{n} \leq B \delta,$$
for every $\psi \in \operatorname{PSH}(X,(A+1) \omega)$ with $\sup _{X} \psi=0$. Let $h(s):=(-\tilde{\chi}(-s))^{1 / 2}$ for $s \leq 0$. Then, for every constant $0<\gamma<1$, there exists a constant $C>0$ depending only on $n, X, \omega$ and $\gamma$ such that
$$d_{c a p}(u, v)^{2} \leq C(A B)^{2}\left(h^{\circ(n)}\left(\frac{\delta}{\left\|\theta_{u}^{n}-\eta_{v}^{n}\right\|+A^{n}\|\theta-\eta\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}(u, v)}\right)\right)^{-\gamma},$$
for every closed smooth real $(1,1)$-form $\eta \leq A \omega$ and for each $v \in \operatorname{PSH}(X, \eta)$ with $\sup _{X} v=0$.
Here, we denote by $\left\|\mu-\mu^{\prime}\right\|$ the mass norm of $\mu-\mu^{\prime}$. The condition that $\tilde{\chi}(-1)=-1$ is merely a normalization one. For an arbitrary $\tilde{\chi} \in \mathcal{W}^{-}$, we can consider $\tilde{\chi} /|\tilde{\chi}(-1)|$ which satisfies the last requirement. Theorem 1.2 says that under a very weak assumption on the regularity of the Monge-Ampère of $u$, one can bound from above the distance $d_{\text {cap }}$ of $u$ with any other quasi-psh function $v$.

We now turn our attention to the class of Hölder continuous measures whose definition is recalled below. Let $\mathrm{PSH}_{0}(X, \omega)$ be the set of $\omega$-psh functions $u$ with $\int_{X} u \omega^{n}=0$. We endow $\operatorname{PSH}_{0}(X, \omega)$ with the $L^{1}\left(\omega^{n}\right)$ distance. Let $\mu$ be a measure on $X$ such that quasipsh functions are $\mu$-integrable. We say that $\mu$ is Hölder continuous with Hölder constant $A$ and Hölder exponent $\gamma$ if it is so as a functional on $\operatorname{PSH}_{0}(X, \omega)$, in other words, for every $u_{1}, u_{2} \in \operatorname{PSH}_{0}(X, \omega)$, we have
$$\int_{X}\left|u_{1}-u_{2}\right| d \mu \leq A\left\|u_{1}-u_{2}\right\|_{L^{1}\left(\omega^{n}\right)}^{\gamma}$$
This notion was introduced in [27]. By expressing every $\omega$-psh function $u$ as $u=u-$ $\int_{X} u \omega^{n}+\int_{X} u \omega^{n}$, we deduce from (1.8) that
$$\int_{X}\left|u_{1}-u_{2}\right| d \mu \leq(A+\mu(X)) \max \left\{\left\|u_{1}-u_{2}\right\|_{L^{1}\left(\omega^{n}\right)}^{\gamma},\left\|u_{1}-u_{2}\right\|_{L^{1}\left(\omega^{n}\right)}\right\}$$
for every $\omega$-psh function $u_{1}, u_{2}$. Clearly the last inequality also implies that $\mu$ is Hölder with Hölder exponent $\gamma$ and with Hölder constant $\lambda(A+\mu(X))$, for some constant $\lambda$ depending only on $(X, \omega)$. Recall that a measure is Hölder continuous if and only if it can be written as $\left(d d^{c} u+\omega\right)^{n}$ for some Hölder continuous $\omega$-psh function $u$ on $X$; see [19, 27] and also [44]. We refer to these papers and [40, 47, 53, 65] for examples of Hölder continuous measures. Most basic examples are measures with $L^{p}$ density or smooth volume forms of (immersed) generic (real) Cauchy-Riemann submanifolds on $X$.

Recall that the set of Radon measures on $X$ endowed with the weak topology is a metric space with the distance $\operatorname{dist}_{-\delta}$ for $\delta \in[0, \infty)$ defined as follows: for measures $\mu, \mu^{\prime}$,
$$\operatorname{dist}_{-\delta}\left(\mu, \mu^{\prime}\right):=\sup _{\|v\|_{\mathscr{C} \delta} \leq 1}\left|\left\langle\mu-\mu^{\prime}, v\right\rangle\right|,$$
where $v$ is a smooth real-valued function on $X$ (see [64, Theorem 6.9]). Note that dist $_{-\delta}$ induces the same weak topology when $\delta>0$. When $\delta=0$, it is the mass norm of $\mu_{1}-\mu_{2}$. We also have the following interpolation inequality: for $0 \leq \beta_{0}<\beta_{1}<\beta_{2}$,
$$\operatorname{dist}_{-\beta_{1}} \leq \operatorname{dist}_{-\beta_{0}}^{\frac{\beta_{2}-\beta_{1}}{\beta_{2}-\beta_{0}}} \operatorname{dist}_{-\beta_{2}}^{\frac{\beta_{1}-\beta_{0}}{\beta_{2}-\beta_{0}}} .$$

We refer to [51, 60] for a proof (see also [65]). This kind of estimate is very important in complex dynamics since the appearance of [30] where a more general version of (1.11) for currents was introduced.

Our next main result is as follows:
Theorem 1.3. Let $\theta_{1}, \theta_{2}$ be closed smooth real (1, 1)-forms and $A$ be positive constant at least 1 such that $\theta_{j} \leq A \omega$ for $j=1,2$. Let $0<\delta \leq 1$ and $M \geq 1$ be constants and $u_{j} \in \operatorname{PSH}\left(X, \theta_{j}\right)$ $(j=1,2)$ such that
$$\sup _{X} u_{j}=0, \quad \int_{X} \theta_{u_{j}}^{n} \geq \delta,$$
and $\mu_{j}:=\left(\theta_{j}+d d^{c} u_{j}\right)^{n}(j=1,2)$ are Hölder continuous measures on $X$ with Hölder exponent $\beta$ and with Hölder constant $M \delta$. Then, for every $0<\gamma<1$, there exists a constant $C>0$ depending only on $n, X, \omega, A, M, \beta$ and $\gamma$ such that
$$\left(d_{c a p}\left(u_{1}, u_{2}\right)\right)^{2} \leq C\left(\frac{\tau^{\gamma \beta /(\beta+1)}+\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)}{\delta}\right)^{2^{-n} \gamma},$$
where $\tau:=\operatorname{dist}_{-1}\left(\mu_{1}, \mu_{2}\right)$.
By interpolation inequality (1.11), an analogous inequality also holds for dist $_{-\beta}$ in place of dist ${ }_{-1}$ for any constant $\beta>0$. Our last main result is a generalization of Cegrell-Kołodziej-Xing stability theorem ([10, 71]) which treated the case where $\theta=\omega$ and $\phi=0$ (and only for the class of potentials of full Monge-Ampère mass). We also underline that the original result in [10, 71] is non-quantitative and Theorem 1.4 already strengthens their results in their setting.

Theorem 1.4. Let $\theta_{1}, \theta_{2}$ be closed smooth real (1, 1)-forms and $A$ be positive constant at least 1 such that $\theta_{j} \leq A \omega$ for $j=1,2$. Let $0<\delta \leq 1$ and $u_{j} \in \operatorname{PSH}\left(X, \theta_{j}\right)(j=1,2)$ such that $\sup _{X} u_{j}=0$ and $\int_{X} \theta_{u_{j}}^{n} \geq \delta$. Assume that there exists a Radon measure $\mu$ on $X$ such that $\mu$ vanishes on pluripolar sets and $\left(\theta_{j}+d d^{c} u_{j}\right)^{n} \leq \mu$ for $j=1,2$. Then, there exists a continuous increasing function $f_{\mu}: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ depending only on $n, X, \omega, A, \delta$ and $\mu$ such that $f(0)=0$ and
$$d_{c a p}\left(u_{1}, u_{2}\right)^{2} \leq f_{\mu}\left(\operatorname{dist}_{-1}\left(\mu_{1}, \mu_{2}\right)+\left\|\theta_{1}-\theta_{2}\right\|_{\mathscr{C}^{0}}+d_{(A+1) \omega}\left(u_{1}, u_{2}\right)\right),$$
where $\mu_{j}:=\left(\theta_{j}+d d^{c} u_{j}\right)^{n}$ for $j=1,2$.
Theorem 1.4 implies particularly that for every model $\theta$-psh function $\phi$, the convergence in capacity or in $L^{1}$ and the weak convergence of Monge-Ampère measures are equivalent in the class of potentials in $\mathcal{E}(X, \theta, \phi)$ whose Monge-Ampère measures are bounded from above by a fixed non-pluripolar measure. This is more or less the original motivation of Cegrell-Kołodziej in [10].

Finally we note that as an application of Theorem 1.4 or 1.3, one can recover a main result in [18] that the pseudometric space of singularity types of volume bounded from below by a fixed positive constant is complete, we refer to Remark 4.21 in the end of the paper and Subsection 4.3 for details.

\subsection*{1.2 Key components in our method}

As mentioned above the core of the method developed in this paper is a solution to the quantitative stability for measures of lower energy in the setting where the cohomology class and the prescribed singularity are fixed. We underline that in what follows by convex weights we mean also bounded convex functions, although such functions were not usually considered as weights. This point of view is the key allowing us to treat the general setting when both the cohomology class and the prescribed singularity of solution vary.

Let $\widetilde{\mathcal{W}}^{-}$be the set of convex, non-decreasing functions $\chi: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ such that $\chi(0)=$ 0 and $\chi \neq 0$. Note that $\chi$ can be bounded. Obviously $\mathcal{W}^{-}$is contained in $\mathcal{W}^{-}$. It is crucial in our method that we consider also $\chi \in \widetilde{\mathcal{W}}^{-}$which is bounded. Let $M \geq 1$ be a constant and $\mathcal{W}_{M}^{+}$the usual space of increasing concave functions $\chi: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ such that $\chi(0)=0$, $\chi \not \equiv 0$, and $\left|t \chi^{\prime}(t)\right| \leq M|\chi(t)|$ for every $t \leq 0$.

Let $\varrho:=\int_{X} \theta_{\phi}^{n}$. For $\chi \in \mathcal{W}^{-} \cup \mathcal{W}_{M}^{+}$and $u \in \operatorname{PSH}(X, \theta, \phi)$, let
$$E_{\chi, \theta, \phi}^{0}(u):=-\varrho^{-1} \int_{X} \chi(u-\phi) \theta_{u}^{n}$$
which is called the (normalized) $\chi$-energy of $u$ (with respect to $\theta, \phi$ ). We denote
$$\mathcal{E}_{\chi}(X, \theta, \phi):=\left\{u \in \mathcal{E}(X, \theta, \phi): E_{\chi, \theta, \phi}(u)<\infty\right\},$$
where $\mathcal{E}(X, \theta, \phi)$ is the space of $\theta$-psh functions $u \leq \phi$ with $\int_{X} \theta_{u}^{n}=\int_{X} \theta_{\phi}^{n}$. Certainly if $\chi$ is bounded, then $\mathcal{E}_{\chi}(X, \theta, \phi)=\mathcal{E}(X, \theta, \phi)$. We would like to point out however that our method is not about the finiteness of $E_{\chi, \theta, \phi}^{0}(u)$ but estimating the size of that quantity. Thus whether $\chi$ is bounded or not does not make much difference for our later arguments. Put
$$I_{\chi}^{0}(u, v):=\varrho^{-1} \int_{\{u<v\}} \chi(u-v)\left(\theta_{v}^{n}-\theta_{u}^{n}\right)+\varrho^{-1} \int_{\{u>v\}} \chi(v-u)\left(\theta_{u}^{n}-\theta_{v}^{n}\right)$$
for $u, v \in \mathcal{E}_{\chi}(X, \theta, \phi)$. The factor $\varrho^{-1}$ in the defining formulae for $E_{\chi, \theta, \phi}^{0}(u)$ and $I_{\chi}^{0}(u, v)$ plays the role of a normalizing constant. In geometric applications it is important to treat the case where $\varrho \rightarrow 0$, i.e, to obtain estimates uniformly as $\varrho \rightarrow 0$ (here we allow $\theta$ or its cohomology class to vary).

Clearly if $\theta_{u}^{n}=\theta_{v}^{n}$, then $I_{\chi}^{0}(u, v)=0$. We will see later that each term in the sum defining $I_{\chi}^{0}(u, v)$ is nonnegative. We recall that there is a natural (quasi-)metric on the space $\mathcal{E}_{\chi}(X, \theta, \phi)$ constructed in [13, 14, 37], and see [15, 21, 62, 70] as well. The functional $I_{\chi}^{0}(u, v)$ has an intimate relation with these quasi-metrics. We refer to the end of Section 3 for details on this connection. Here is the first key ingredient in our proof of main results.

Theorem 1.5. Let $\theta$ be a closed smooth real (1, 1)-form and $\phi$ be a negative $\theta$-psh function such that $\varrho:=\int_{X} \theta_{\phi}^{n}>0$. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}} \cup \mathcal{W}_{M}^{+}(M \geq 1)$ such that $\tilde{\chi} \leq \chi$. Let $B \geq 1$ be a constant and let $u_{j}, \psi_{j} \in \mathcal{E}(X, \theta, \phi)$ satisfy $u_{1} \leq u_{2}$ and
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{j}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(\psi_{j}\right) \leq B,$$
for $j=1,2$. Then there exists a constant $C_{n}>0$ depending only on $n$ and $M$, and a continuous increasing function $f: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$ depending only on $\chi, \tilde{\chi}$ such that $f(0)=0$ and
$$\int_{X}-\chi\left(u_{1}-u_{2}\right)\left(\theta_{\psi_{1}}^{n}-\theta_{\psi_{2}}^{n}\right) \leq C_{n} \varrho B^{2} f\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right) .$$

The following result is the second key which is a consequence of the first one.
Theorem 1.6. Let $\theta$ be a closed smooth real (1, 1)-form, and let $A \geq 1$ be a constant such that $\theta \leq A \omega$. Let $\phi$ be a model $\theta$-psh function. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}(M \geq 1)$ such that $\tilde{\chi} \leq \chi$. Let $B \geq 1$ be a constant and $u_{1}, u_{2}, \psi \in \mathcal{E}(X, \theta, \phi)$ with $\sup _{X} u_{1}=\sup _{X} u_{2}$ satisfy
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{2}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}(\psi) \leq B .$$
Then, for every constant $m>0$ and $0<\gamma<1$, there exist a constant $C>0$ depending on $n, M, X, \omega, m$ and $\gamma$, and a function $f$ as in Theorem 1.5 such that
$$\int_{X}-\chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} \leq-\varrho \chi\left(-\lambda^{m}\right)+C \varrho B_{\gamma, m}^{2} \lambda^{\gamma},$$
where $\lambda:=f\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right)$ and $B_{\gamma, m}=A^{(1-\gamma) /(2 m)}(B-\tilde{\chi}(-A))(1-\tilde{\chi}(-1))$.
The condition $\sup _{X} u_{1}=\sup _{X} u_{2}$ is simply a normalization one. By Theorem 1.6, one sees in particular that if $I_{\chi}^{0}\left(u_{1}, u_{2}\right) \rightarrow 0$, then $\left|u_{1}-u_{2}\right| \rightarrow 0$ in $L^{p}$ for every $p>0$. The function $f$ can be made explicitly; see Theorems 3.1 and 3.2 below for more elaborated versions of these above results.

We note that the single theorem 1.5 contains the following three important results in pluripotential theory: uniqueness of solutions of complex Monge-Ampère equations, domination principle, and comparison of capacities. We obtain indeed quantitative (hence stronger) versions of these results for which we refer to Subsection 3.4. Readers also find there a quantitative version of the fact that the convergence in Darvas's metric in $\mathcal{E}_{\chi}(X, \theta, \phi)$ implies the convergence in capacity. Notice that such an estimate seems to be not reachable by using the usual plurisubharmonic envelope method.

The main novelty of Theorem 1.5 is that it deals with arbitrary weights. Similar statements was already known for $\chi(t)=t$ (see [7, 35]). However the proof there only work exclusively for this case. One should notice that the weight $\chi(t)=t$ is very special: it is linear and lies in the middle between higher energy weights and lower energy weights. As to the proof of Theorem 1.5, going up to the space of higher energy weights or going down to the space of lower energy weights are equally difficult. We will explain this point in more details in the paragraph after Theorem 1.7 below.

The key in the proof of Theorem 1.5 is Proposition 3.5 in Section 3 a simplified version of which we state here for readers' convenience.

Theorem 1.7. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}$such that $\tilde{\chi} \leq \chi$ and $\chi \in \mathscr{C}^{1}(\mathbb{R})$. Let $u_{1}, u_{2}, u_{3} \in$ $\mathcal{E}(X, \theta, \phi)$ such that $u_{1} \leq u_{2}$ and $u_{j}-\phi$ is bounded $(j=1,2,3)$, where $\phi$ is a negative $\theta$-psh
function satisfying $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Then there exist a constant $C_{n}>0$ depending only on $n$ and $M$, and a function $f$ as in Theorem 1.5 such that
$$\int_{X} \chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{2}\right) \wedge d^{c}\left(u_{1}-u_{2}\right) \wedge \theta_{u_{3}}^{n-1} \leq C_{n} \varrho B^{2} f\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right),$$
where $B:=\sum_{j=1}^{3} \max \left\{E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{j}\right), 1\right\}$.
As far as we know, all of previous works related to Theorem 1.7 only concern with $\chi(t)=t$. In this case, Theorem 1.7 was known with an explicit $f$ and without $\tilde{\chi}$ if $\phi$ is of minimal singularity in the cohomology class of $\theta$, by [7, 35].

The key ingredients in previous versions of Theorem 1.7 for $\chi(t)=t$ are integration by parts arguments. Direct generalization of such reasoning immediately break down if $\chi \neq \mathrm{id}$ : in a more precise but technical level, the integration by parts arguments give terms like $\chi^{\prime}\left(u_{1}-u_{2}\right) d\left(u_{1}-u_{3}\right) \wedge d^{c}\left(u_{1}-u_{3}\right)$, such quantity is easy to bound if $\chi=\mathrm{id}$ (hence $\chi^{\prime} \equiv 1$ ), but it is no longer the case if $\chi \neq \mathrm{id}$.

In order to prove Theorem 1.7, we still use this strategy but need to use a so-called "monotonicity argument" from [32, 67, 68] to deal with general $\chi$. In a nutshell it is about using intensively the pluri-locality of Monge-Ampère operators together with the monotonicity of pluricomplex energy which allow one to bound from above "Monge-Ampère quantities" of bad potentials by that of nicer potentials. This method is a flexible tool to deal with "low regularity", and was a key in the proof of the convexity of the class of potentials of finite $\chi$-energy in [68], as well as, giving a characterization of the class of Monge-Ampère measures with potentials of finite $\chi$-energy in [32]. Moreover in order to deduce Theorem 1.6 from Theorem 1.5, we use, among other things, an idea from [35] together with a very simple but crucial lower bound of the sublevel sets of $\omega$-psh functions; see Lemma 3.8 below. Such an estimate is of independent interest.

Organization of the paper. In Section 2, we recall the crucial integration by parts formula from [68], auxiliary facts about weights are also collected there. Theorems 1.5, 1.6, and 1.7 are proved in Section 3, We prove Theorems 4.17, 1.2, 1.3 and 1.4 in Subsection 4.4. Proposition 4.15 is proved at the end of the paper.

Acknowledgments. We would like to thank Tamás Darvas, Vincent Guedj, Henri Guenancia, Prakhar Gupta, Hoang Chinh Lu, Tat Dat Tô, Valentino Tosatti, and Ahmed Zeriahi for fruitful discussions. The research of D.-V. Vu is partly funded by the Deutsche Forschungsgemeinschaft (DFG, German Research Foundation)-Projektnummer 500055552.

\section*{2 Preliminaries}

\subsection*{2.1 Integration by parts}

In this subsection, we recall the integration by parts formula obtained in [68, Theorem 2.6]. This formula will play a key role in our proof of main results later.

Let $X$ be a compact Kähler manifold. Let $T_{1}, \ldots, T_{m}$ be closed positive $(1,1)$-currents on $X$. Let $T$ be a closed positive current of bi-degree $(p, p)$ on $X$. The $T$-relative non-pluripolar product $\left\langle\wedge_{j=1}^{m} T_{j} \dot{\wedge} T\right\rangle$ is defined in a way similar to that of the usual non-pluripolar product (see [67]). The product $\left\langle\wedge_{j=1}^{m} T_{j} \dot{\wedge} T\right\rangle$ is a closed positive current of bi-degree $(m+p, m+p)$; and the wedge product $\left\langle\wedge_{j=1}^{m} T_{j} \dot{\wedge} T\right\rangle$ as an operator on currents is symmetric with respect to $T_{1}, \ldots, T_{m}$ and is homogeneous. In latter applications, we will only use the case where $T$ is the non-pluripolar product of some closed positive (1, 1)-currents, say, $T=\left\langle T_{m+1} \wedge \cdots \wedge\right.$ $\left.T_{m+l}\right\rangle$, where $T_{j}$ is (1, 1)-currents for $m+1 \leq j \leq m+l$. In this case, $\left\langle T_{1} \wedge \cdots \wedge T_{m} \dot{\wedge} T\right\rangle$ is simply equal to $\left\langle\wedge_{j=1}^{m+l} T_{j}\right\rangle$. We usually remove the bracket $\rangle$ in the non-pluripolar product to ease the notation.

Recall that a $d s h$ function on $X$ is the difference of two quasi-plurisubharmonic (quasipsh for short) functions on $X$ (see [29]). These functions are well-defined outside pluripolar sets. Let $v$ be a dsh function on $X$. Let $T$ be a closed positive current on $X$. We say that $v$ is $T$-admissible if there exist quasi-psh functions $\varphi_{1}, \varphi_{2}$ such that $v=\varphi_{1}-\varphi_{2}$ and $T$ has no mass on $\left\{\varphi_{j}=-\infty\right\}$ for $j=1,2$. In particular, if $T$ has no mass on pluripolar sets, then every dsh function is $T$-admissible.

Assume now that $v$ is $T$-admissible. Let $\varphi_{1}, \varphi_{2}$ be quasi-psh functions such that $v=$ $\varphi_{1}-\varphi_{2}$ and $T$ has no mass on $\left\{\varphi_{j}=-\infty\right\}$ for $j=1,2$. Let
$$\varphi_{j, k}:=\max \left\{\varphi_{j},-k\right\}$$
for every $j=1,2$ and $k \in \mathbb{N}$. Put $v_{k}:=\varphi_{1, k}-\varphi_{2, k}$. Put
$$Q_{k}:=d v_{k} \wedge d^{c} v_{k} \wedge T=d d^{c} v_{k}^{2} \wedge T-v_{k} d d^{c} v_{k} \wedge T .$$
By the plurifine locality with respect to $T$ ([67, Theorem 2.9]) applied to the right-hand side of the last equality, we have
$$\mathbf{1}_{\cap_{j=1}^{2}\left\{\varphi_{j}>-k\right\}} Q_{k}=\mathbf{1}_{\cap_{j=1}^{2}\left\{\varphi_{j}>-k\right\}} Q_{s}$$
for every $s \geq k$. We say that $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle$ is well-defined if the mass of $\mathbf{1}_{\cap_{j=1}^{2}\left\{\varphi_{j}>-k\right\}} Q_{k}$ is uniformly bounded on $k$. In this case, using (2.1) implies that there exists a positive current $Q$ on $X$ such that for every bounded Borel form $\Phi$ with compact support on $X$ such that
$$\langle Q, \Phi\rangle=\lim _{k \rightarrow \infty}\left\langle\mathbf{1}_{\cap_{j=1}^{2}\left\{\varphi_{j}>-k\right\}} Q_{k}, \Phi\right\rangle,$$
and we define $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle$ to be the current $Q$. This agrees with the classical definition if $v$ is the difference of two bounded quasi-psh functions. One can check that this definition is independent of the choice of $\varphi_{1}, \varphi_{2}$. By [68, Lemma 2.5], if $v$ is bounded, then $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle$ is well-defined.

Let $w$ be another $T$-admissible dsh function. If $T$ is of bi-degree $(n-1, n-1)$, we can also define the current $\left\langle d v \wedge d^{c} w \dot{\wedge} T\right\rangle$ by a similar procedure as above. More precisely, we say $\left\langle d v \wedge d^{c} w \dot{\wedge} T\right\rangle$ is well-defined if $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle,\left\langle d w \wedge d^{c} w \dot{\wedge} T\right\rangle$, and $\left\langle d(v+w) \wedge d^{c}(v+w) \dot{\wedge} T\right\rangle$ are well-defined. In this case, as in the classical case of bounded potentials, the defining formula for $\left\langle d v \wedge d^{c} w \dot{\wedge} T\right\rangle$ is obvious:
$$2\left\langle d v \wedge d^{c} w \dot{\wedge} T\right\rangle=\left\langle d(v+w) \wedge d^{c}(v+w) \dot{\wedge} T\right\rangle-\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle-\left\langle d w \wedge d^{c} w \dot{\wedge} T\right\rangle .$$

As above, if $v, w$ are bounded $T$-admissible, then $\left\langle d v \wedge d^{c} w \dot{\wedge} T\right\rangle$ is well-defined and given by the above formula. The following Cauchy-Schwarz inequality is clear from definition.

Lemma 2.1. Assume that $\left\langle d v \wedge d^{c} w \dot{\wedge} T\right\rangle$ is well-defined. Then for every positive Borel function $\chi$, we have
$$\int_{X} \chi\left\langle d v \wedge d^{c} w \dot{\wedge} T\right\rangle \leq\left(\int_{X} \chi\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle\right)^{1 / 2}\left(\int_{X} \chi\left\langle d w \wedge d^{c} w \dot{\wedge} T\right\rangle\right)^{1 / 2} .$$

We put
$$\left\langle d d^{c} v \dot{\wedge} T\right\rangle:=\left\langle d d^{c} \varphi_{1} \dot{\wedge} T\right\rangle-\left\langle d d^{c} \varphi_{2} \dot{\wedge} T\right\rangle$$
which is independent of the choice of $\varphi_{1}, \varphi_{2}$. The following integration by parts formula is crucial for us later.

Theorem 2.2. ([68, Theorem 2.6] or [32, Theorem 3.1]) Let $T$ be a closed positive current of bi-degree $(n-1, n-1)$ on $X$. Let $v, w$ be bounded $T$-admissible dsh functions on $X$. If $\chi: \mathbb{R} \rightarrow \mathbb{R}$ is a $\mathscr{C}^{3}$ function then we have
$$\begin{aligned}
\int_{X} \chi(w)\left\langle d d^{c} v \dot{\wedge} T\right\rangle=\int_{X} v \chi^{\prime \prime}(w)\left\langle d w \wedge d^{c} w \dot{\wedge} T\right\rangle+\int_{X} v \chi^{\prime} & (w)\left\langle d d^{c} w \dot{\wedge} T\right\rangle \\
& =-\int_{X} \chi^{\prime}(w)\left\langle d w \wedge d^{c} v \dot{\wedge} T\right\rangle
\end{aligned}$$

Since the case where $T$ is a non-pluripolar product of (1, 1)-currents plays an important role in the study of the complex Monge-Ampère equation, we present below an equivalent natural way to define the current $\left\langle d \varphi \wedge d^{c} \varphi \dot{\lambda} T\right\rangle$ in this setting. It is just for the purpose of clarification.

Lemma 2.3. Let $u_{1}, \ldots, u_{m}$ be negative psh functions on an open subset $U$ in $\mathbb{C}^{n}$ such that $T:=\left\langle d d^{c} u_{1} \wedge \cdots \wedge d d^{c} u_{m}\right\rangle$ is well-defined. Let $v$ be the difference of two bounded psh functions on $U$. For $k \in \mathbb{N}$, put $u_{j, k}:=\max \left\{u_{j},-k\right\}$ and
$$T_{k}:=d d^{c} u_{1, k} \wedge \cdots \wedge d d^{c} u_{m, k} .$$
Then we have
$$d v \wedge d^{c} v \wedge T=d v \wedge d^{c} v \wedge T_{k}$$
on $\cap_{j=1}^{m}\left\{u_{j}>-k\right\}$.
Proof. Put
$$\psi_{k}:=k^{-1} \max \left\{u_{1}+\cdots+u_{m},-k\right\}+1 .$$
Observe $\psi_{k} T_{k}=\psi_{k} T$. Now regularizing $v$ and using the continuity of Monge-Ampère operators of bounded potentials, we obtain
$$\psi_{k} d v \wedge d^{c} v \wedge T=\psi_{k} d v \wedge d^{c} v \wedge T_{k} .$$

Hence
$$d v \wedge d^{c} v \wedge T=d v \wedge d^{c} v \wedge T_{k}$$
on $U:=\cap_{j=1}^{m}\left\{u_{j}>-k /(2 m)\right\}$ (for $\psi_{k} \geq 1 / 2$ on $U$ ). Note that $d v \wedge d^{c} v \wedge T_{k}=d v \wedge d^{c} v \wedge$ $T_{k /(2 m)}$ on $U$ by the plurifine locality. Thus the desired assertion follows. This finishes the proof. \(\square\)

Let $T_{1}, \ldots, T_{m}$ be closed positive (1,1)-currents on $X$. Let $n:=\operatorname{dim} X$. Consider now
$$T:=\left\langle T_{1} \wedge \cdots \wedge T_{m}\right\rangle .$$
Note that $T$ has no mass on pluripolar sets. Let $\varphi_{1}, \varphi_{2}$ be negative quasi-psh function on $X$. Let $\varphi_{j, k}(j=1,2)$ be as before and $v:=\varphi_{1}-\varphi_{2}$. In the moment, we work locally. Let $U$ be an open small enough local chart (biholomorphic to a polydisk in $\mathbb{C}^{n}$ ) in $X$ such that $T_{j}=d d^{c} u_{j}$ for $j=1, \ldots, m$, where $u_{j}$ is negative psh functions on $U$. Put $u_{j, k}:=\max \left\{u_{j},-k\right\}$ for $k \in \mathbb{N}$, and
$$T_{k}:=d d^{c} u_{1, k} \wedge \cdots \wedge d d^{c} u_{m, k}, \quad Q_{k}^{\prime}:=d v_{k} \wedge d^{c} v_{k} \wedge T_{k} .$$
Put $A_{k}:=\cap_{j=1}^{2}\left\{\varphi_{j}>-k\right\} \cap \cap_{j=1}^{m}\left\{u_{j}>-k\right\}$. By plurifine properties of Monge-Ampère operators, we have
$$\mathbf{1}_{A_{k}} Q_{k}^{\prime}=\mathbf{1}_{A_{k}} Q_{s}^{\prime}$$
for every $s \geq k$. One can check that the condition that $\left(\mathbf{1}_{A_{k}} Q_{k}^{\prime}\right)_{k}$ is of mass bounded uniformly (on compact subsets in $U$ ) in $k$ is independent of the choice of potentials.

Proposition 2.4. The current $\mathbf{1}_{A_{k}} Q_{k}^{\prime}$ is of mass bounded uniformly in $k$ on compact subsets in $U$ for every $U$ (small enough biholomorphic to a polydisk in $\mathbb{C}^{n}$ ) if and only if the current $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle$ is well-defined. In this case we have
$$\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle=\lim _{k \rightarrow \infty} \mathbf{1}_{A_{k}} Q_{k}^{\prime} .$$
Proof. By writing a smooth form of bi-degree $(n-m-1, n-m-1)$ as the difference of two smooth positive forms, we can assume without loss of generality that $T$ is of bi-degree $(n-1, n-1)$ (hence $m=n-1$ ). Assume that $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle$ is well-defined. We will check that $\mathbf{1}_{A_{k}} Q_{k}^{\prime}$ is of mass bounded uniformly in $k$ on compact subsets in $U$. Let $\chi$ be a nonnegative smooth function compactly supported on $U$. Put
$$\psi:=\varphi_{1}+\varphi_{2}+u_{1}+\cdots+u_{m}, \quad \psi_{k}:=k^{-1} \max \{\psi,-k\}+1 .$$
and $\varphi_{j k}:=\max \left\{\varphi_{j},-k\right\}$ for $1 \leq j \leq 2$. Observe that $0 \leq \psi_{k} \leq 1$ and if $\psi_{k}>0$, then $\varphi_{j}>-k$ for $1 \leq j \leq 2$; and
$$\psi_{k}(x) \geq 1-s / k$$
for every $x \in A_{s /(m+2)}$ and $1 \leq s \leq k$. Recall $v_{k}:=\varphi_{1 k}-\varphi_{2 k}$ which is bounded (but not necessarily uniformly in $k$ ). Observe that $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle$ has no mass on pluripolar sets
because $T$ is so (see for example [67, Lemma 2.1]). Put $Q_{k}^{\prime \prime}:=\psi_{k} Q_{k}=\psi_{k} \mathbf{1}_{A_{k}} Q_{k}^{\prime}$ By (2.4) and Lemma 2.3, we have
$$\begin{aligned}
\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle & =\lim _{k \rightarrow \infty} \psi_{k} d v_{k} \wedge d^{c} v_{k} \wedge T \\
& =\lim _{k \rightarrow \infty} \psi_{k} d v_{k} \wedge d^{c} v_{k} \wedge T_{k}=\lim _{k \rightarrow \infty} Q_{k}^{\prime \prime}
\end{aligned}$$
on $U$. On the other hand, by (2.4) again, we see that the claim that $Q_{k}^{\prime \prime}$ is of mass uniformly bounded on compact subsets in $U$ is equivalent to that $\mathbf{1}_{A_{k}} Q_{k}^{\prime}$ is so. This together with (2.5) yields the desired assertion.

Conversely, suppose now that $\mathbf{1}_{A_{k}} Q_{k}^{\prime}$ is of mass bounded uniformly in $k$ on compact subsets in $U$ for every $U$. Thus there exists a positive current $R$ on $U$ such that $\mathbf{1}_{A_{k}} R=$ $\mathbf{1}_{A_{k}} Q_{k}^{\prime}$ for every $k$ and $U$. Set
$$\tilde{\psi}:=\varphi_{1}+\varphi_{2}, \quad \tilde{\psi}_{k}:=k^{-1} \max \{\tilde{\psi},-k\}+1 .$$
Let $s \in \mathbb{N}$ with $s \geq k$. Observe
$$\psi_{s} R=\tilde{\psi}_{k} \psi_{s} R+\left(1-\tilde{\psi}_{k}\right) \psi_{s} R .$$
The second term in the right-hand side of the last inequality tends to 0 (uniformly in $s$ ) because $\tilde{\psi}_{k}$ converges pointwise to 1 outside a pluripolar set and $R$ has no mass on pluripolar sets. Using Lemma 2.3, we have
$$\begin{aligned}
\tilde{\psi}_{k} \psi_{s} R & =\tilde{\psi}_{k} \psi_{s} d v_{s} \wedge d^{c} v_{s} \wedge T_{s} \\
& =\tilde{\psi}_{k} \psi_{s} d v_{s} \wedge d^{c} v_{s} \wedge T=\tilde{\psi}_{k} \psi_{s} d v_{k} \wedge d^{c} v_{k} \wedge T,
\end{aligned}$$
here we used the plurifine topology properties with respect to $T$ (see [67, Theorem 2.9]), thanks to the fact that $\varphi_{j, k}=\varphi_{j, s}$ on $\left\{\tilde{\psi}_{k} \neq 0\right\}$ for $j=1,2$ (recall $s \geq k$ ), and they are bounded psh functions. Letting $s \rightarrow \infty$ gives
$$\tilde{\psi}_{k} R=\tilde{\psi}_{k} \mathbf{1}_{\cup_{j=1}^{m}\left\{u_{j}>-\infty\right\}} d v_{k} \wedge d^{c} v_{k} \wedge T=\tilde{\psi}_{k} d v_{k} \wedge d^{c} v_{k} \wedge T$$
because the current $d v_{k} \wedge d^{c} v_{k} \wedge T$ has no mass on pluripolar sets. Now letting $k \rightarrow \infty$ gives the desired assertion. This finishes the proof. \(\square\)

Thanks to Proposition 2.4, we can use the right-hand side of (2.3) to define $\left\langle d v \wedge d^{c} v \dot{\wedge} T\right\rangle$ in the case where $T$ is the non-pluripolar product of some closed positive (1,1)-currents. By the same reason, in this case, we will use the expression $d v \wedge d^{c} w \wedge T_{1} \wedge \ldots \wedge T_{n-1}$ to denote $\left\langle d v \wedge d^{c} w \dot{\wedge}\left\langle T_{1} \wedge \cdots \wedge T_{n-1}\right\rangle\right\rangle$ whenever it is well-defined.

\subsection*{2.2 Auxiliary facts on weights}

In this subsection, we present some facts about weights needed for the proofs of main results.

Recall that $\widetilde{\mathcal{W}}^{-}$is the set of all convex, non-decreasing functions $\chi: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ such that $\chi(0)=0$ and $\chi \not \equiv 0$. Let $M \geq 1$ be a constant and $\mathcal{W}_{M}^{+}$the usual space of increasing concave functions $\chi: \mathbb{R}_{\leq 0} \rightarrow \mathbb{R}_{\leq 0}$ such that $\chi(0)=0, \chi \not \equiv 0$, and $\left|t \chi^{\prime}(t)\right| \leq M|\chi(t)|$ for every $t \leq 0$. We have the following lemmas.

Lemma 2.5. Let $c>0,0<\delta<1$ and $\chi: \mathbb{R} \rightarrow \mathbb{R}$ such that $\chi(t)=c t$ for every $t \geq-\delta$ and $\left.\chi\right|_{(-\infty, 0]} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}(M \geq 1)$. Let $g$ be a smooth radial cut-off function supported in [-1, 1] on $\mathbb{R}$, i.e, $g(t)=g(-t)$ for $t \in \mathbb{R}, 0 \leq g \leq 1$ and $\int_{\mathbb{R}} g(t) d t=1$. Put $g_{\epsilon}(t):=\epsilon^{-1} g(\epsilon t)$ for every constant $\epsilon>0$ and $\chi_{\epsilon}:=\chi * g_{\epsilon}$ (the convolution of $\chi$ with $g_{\epsilon}$ ). Then the following assertions are true:
(i) if $\chi \in \widetilde{\mathcal{W}}^{-}$, then $\left.\chi_{\epsilon}\right|_{(-\infty, 0]} \in \widetilde{\mathcal{W}}^{-}$for every $0<\epsilon<\delta, \chi_{\epsilon} \searrow \chi$ as $\epsilon \searrow 0$ and $\sup \left(\chi_{\epsilon}-\chi\right) \leq c \epsilon ;$
(ii) if $\chi \in \mathcal{W}_{M}^{+}$and $0<\epsilon<\delta^{2} / 2$ then $\left.\chi_{\epsilon}\right|_{(-\infty, 0]} \in \mathcal{W}_{M /(1-\delta)}^{+}$. Moreover, if $0<\epsilon<\delta^{2} / 8$ then
$$\bar{\chi}_{\epsilon}:=\chi_{\epsilon}(\cdot+\epsilon)-c \epsilon \in \mathcal{W}_{M /(1-\delta)^{2}}^{+}, \quad \bar{\chi}_{\epsilon} \geq \chi-c \epsilon,$$
and $\bar{\chi}_{\epsilon}$ converges uniformly to $\chi$ as $\epsilon \rightarrow 0$ on compact subsets in $\mathbb{R}$.
Proof. The part (i) follows from [32, Lemma 2.1]. The part (ii) can be obtained more or less by similar arguments as in the last reference. We provide details for readers' convenience. It is clear that $\chi_{\epsilon}$ is a concave, increasing function with $\chi_{\epsilon}(0)=0$. We will show that
$$\chi_{\epsilon}^{\prime}(t) \leq \frac{M}{1-\delta} \frac{\chi_{\epsilon}(t)}{t},$$
for every $t<0$ and $0<\epsilon<\delta^{2} / 2$.
If $t<-\frac{\delta}{2}$ then we have
$$\begin{aligned}
\chi_{\epsilon}^{\prime}(t)=\int_{-\epsilon}^{\epsilon} \chi^{\prime}(t-s) g_{\epsilon}(s) d s \leq \int_{-\epsilon}^{\epsilon} \frac{M \chi(t-s)}{t-s} g_{\epsilon}(s) d s & \leq \int_{-\epsilon}^{\epsilon} \frac{M \chi(t-s)}{t+\epsilon} g_{\epsilon}(s) d s \\
& =\frac{M \chi_{\epsilon}(t)}{t+\epsilon} \\
& =\frac{M t}{t+\epsilon} \frac{\chi_{\epsilon}(t)}{t} \\
& \leq \frac{M}{1-\delta} \frac{\chi_{\epsilon}(t)}{t},
\end{aligned}$$
for every $0<\epsilon<\delta^{2} / 2$.
On the other hand, if $t \geq-\frac{\delta}{2}$, then $\chi_{\epsilon}(t)=\chi(t)=c t$ for every $0<\epsilon<\delta^{2} / 2$. As a consequence, we have
$$\chi_{\epsilon}^{\prime}(t)=\chi^{\prime}(t) \leq \frac{M \chi(t)}{t}=M \frac{\chi_{\epsilon}(t)}{t} .$$
Thus, (2.6) follows. Hence, $\left.\chi_{\epsilon}\right|_{(-\infty, 0]} \in \mathcal{W}_{M /(1-\delta)}^{+}$.
Now, we consider $\bar{\chi}_{\epsilon}$. Since $\chi$ is increasing, one sees that $\bar{\chi}_{\epsilon} \geq \chi-c \epsilon$ and $\bar{\chi}_{\epsilon}$ converges uniformly to $\chi$ as $\epsilon \rightarrow 0$ on compact subsets in $\mathbb{R}$. It remains to show that $\bar{\chi}_{\epsilon} \in$ $\mathcal{W}_{M(1+\delta) /(1-\delta)}^{+}$for every $0<\epsilon<\delta^{2} / 8$. Note that
$$\bar{\chi}_{\epsilon}=h_{\epsilon} * g_{\epsilon},$$
where $h_{\epsilon}(t)=\chi(t+\epsilon)-c \epsilon$. The function $\bar{\chi}_{\epsilon}(t)$ is concave, increasing and $\bar{\chi}+\epsilon(0)=0$.

If $-\delta / 2 \leq t<0$ then $h_{\epsilon}(t)=\chi(t)=c t$ for every $0<\epsilon<\delta^{2} / 2$. Therefore
$$h_{\epsilon}^{\prime}(t)=\chi^{\prime}(t) \leq \frac{M \chi(t)}{t}=M \frac{h_{\epsilon}(t)}{t} .$$
If $t<-\delta / 2$ then
$$\begin{aligned}
h_{\epsilon}^{\prime}(t)=\chi^{\prime}(t+\epsilon) \leq M \frac{\chi(t+\epsilon)}{t+\epsilon} \leq M \frac{\chi(t+\epsilon)-c \epsilon}{t+\epsilon}=M \frac{h_{\epsilon}(t)}{t+\epsilon} & =\frac{M t}{t+\epsilon} \frac{h_{\epsilon}(t)}{t} \\
& \leq \frac{M}{1-\delta} \frac{h_{\epsilon}(t)}{t},
\end{aligned}$$
for every $0<\epsilon<\delta^{2} / 2$.
Then, for every $0<\epsilon<\delta^{2} / 2$, we have $h_{\epsilon} \in \mathcal{W}_{M /(1-\delta)}^{+}$and $h_{\epsilon}=c t$ for every $t \geq-\delta / 2$. Hence, for every $0<\epsilon<\delta^{2} / 8$, we have
$$\bar{\chi}_{\epsilon}=h_{\epsilon} * g_{\epsilon} \in \mathcal{W}_{\frac{M}{(1-\delta)(1-\delta / 2)}}^{+} \subset \mathcal{W}_{\frac{M}{(1-\delta)^{2}}}^{+} .$$
The proof is completed. \(\square\)

Lemma 2.6. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}(M \geq 1)$ such that $\tilde{\chi} \leq \chi$. Then, there exist sequences of functions $\chi_{j}, \tilde{\chi}_{j} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M_{j}}^{+}$(with $M_{j} \searrow M$ as $j \rightarrow \infty$ ) satisfying the following conditions:
\begin{itemize}
\item[-] $\chi_{j} \in \mathscr{C}^{\infty}(\mathbb{R})$ for every $j$;
\item[-] $\chi_{j} \geq \tilde{\chi}_{j}$ and $\chi_{j} \geq \chi-2^{-j}$ for every $j$ big enough;
\item[-] $\tilde{\chi}-2^{-j} \leq \tilde{\chi}_{j} \leq \tilde{\chi}$ on $(-\infty,-1]$ for every $j$ big enough;
\item[-] $\chi_{j}$ converges uniformly to $\chi$ on compact subsets in $\mathbb{R}_{\leq 0}$.
\end{itemize}
Proof. We split the proof into two cases.
Case 1: $\chi \in \widetilde{\mathcal{W}}^{-}$.
For every $j \geq 1$, we denote
$$\bar{\chi}_{j}(t)=\left\{\begin{array}{l}
\max \left\{\chi(t), c_{j} t\right\}, \quad \text { if } \quad t<0, \\
c_{j} t \quad \text { if } \quad t \geq 0,
\end{array}\right.$$
where
$$c_{j}:=\frac{-\chi\left(-2^{-j}\right)}{2^{-j}} .$$
Then $\bar{\chi}_{j}$ satisfies the hypothesis of Lemma 2.5 for $\delta:=2^{-j}$. Let $g$ be a smooth radial cut-off function supported in [-1, 1] on $\mathbb{R}$, i.e, $g(t)=g(-t)$ for $t \in \mathbb{R}, 0 \leq g \leq 1$ and $\int_{\mathbb{R}} g(t) d t=1$. For every $j \geq 1$, we define
$$\chi_{j}=\bar{\chi}_{j} * g_{4^{-j-1}} \quad \text { and } \quad \tilde{\chi}_{j}=\tilde{\chi} .$$

By Lemma 2.5, we have $\chi_{j}$ and $\tilde{\chi}_{j}$ satisfy the desired conditions.
Case 2: $\chi \in \mathcal{W}_{M}^{+}$.
Since $\chi \geq \tilde{\chi}$, we also have $\tilde{\chi} \in \mathcal{W}_{M}^{+}$. Assume that $g$ and $c_{j}$ are as in Case 1. For every $j \geq 1$, we define
$$\bar{\chi}_{j}(t)=\left\{\begin{array}{l}
\min \left\{\chi(t), c_{j} t\right\}, \quad \text { if } \quad t<0, \\
c_{j} t \quad \text { if } \quad t \geq 0,
\end{array}\right.$$
and
$$\chi_{j}(t)=\left(\bar{\chi}_{j}\left(\cdot+4^{-j-1}\right) * g_{4^{-j-1}}\right)(t)-c_{j} 4^{-j-1} .$$
We also denote $\tilde{\chi}_{j}(t)=\min \left\{\tilde{\chi}(t), \chi_{j}(t)\right\}$. By Lemma 2.5, we have $\chi_{j}$ and $\tilde{\chi}_{j}$ satisfy the desired conditions. The proof is completed. \(\square\)

Let $\phi$ be a negative $\theta$-psh function. We denote by $\operatorname{PSH}(X, \theta, \phi)$ the set of $\theta$-psh functions $u \leq \phi$. Recall that by monotonicity, we always have $\int_{X} \theta_{u}^{n} \leq \int_{X} \theta_{\phi}^{n}$, where for every $\theta$-psh function $v$, we put $\theta_{v}:=d d^{c} v+\theta$. We also define by $\mathcal{E}(X, \theta, \phi)$ the set of $u \in \operatorname{PSH}(X, \theta, \phi)$ of full Monge-Ampère mass with respect to $\phi$, i.e, $\int_{X} \theta_{u}^{n}=\int_{X} \theta_{\phi}^{n}$.

Let $\chi \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}$, and $u \in \operatorname{PSH}(X, \theta, \phi)$. We put
$$E_{\chi, \theta, \phi}(u):=\int_{X}-\chi(u-\phi) \theta_{u}^{n} .$$
We also define by $\mathcal{E}_{\chi}(X, \theta, \phi)$ the set of $u \in \mathcal{E}(X, \theta, \phi)$ with $E_{\chi, \theta, \phi}(u)<\infty$.
Lemma 2.7. Let $\chi \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}$and $u_{1}, u_{2} \in \mathcal{E}_{\chi}(X, \theta, \phi)$. Then there exists a constant $C_{1}>0$ depending only on $n$ and $M$ such that
$$-\int_{X} \chi\left(u_{1}-\phi\right) \theta_{u_{2}}^{n} \leq C_{1} \sum_{j=1}^{2} E_{\chi, \phi, \theta}\left(u_{j}\right),$$
and
$$E_{\chi, \theta, \phi}\left(a u_{1}+(1-a)\right) u_{2} \leq C_{1} \sum_{j=1}^{2} E_{\chi, \phi, \theta}\left(u_{j}\right),$$
for every $0<a<1$. Furthermore if $u_{1} \geq u_{2}$, then
$$E_{\chi, \phi, \theta}\left(u_{1}\right) \leq C_{2} E_{\chi, \phi, \theta}\left(u_{2}\right),$$
for some constant $C_{2}$ depending only on $n$ and $M$.
Proof. The first and third inequalities are from [32, Lemma 3.2] (see also [34, Propositions 2.3, 2.5] for the case where $\phi=0$ and $\theta$ is a Kähler form). The second desired inequality was implicitly proved in the proof of convexity of finite energy classes in [68, Proposition 3.3] (in a much broader context). Alternatively one can use properties of envelopes in [16] to get the same conclusion. We prove here the second desired inequality using ideas from [68] for readers' convenience.

Considering $u_{j}-\epsilon$ for $\epsilon>0$ instead of $u_{j}$, and taking $\epsilon \rightarrow 0$ later, without loss of generality, we can assume that $u_{j}<\phi \leq 0$ for $j=1.2$. By replacing $u_{j}, \theta$ by $u_{j}-\phi, \theta_{\phi}$ respectively, we can assume that $\phi=0$, but $\theta$ is no longer a smooth form but a closed positive (1,1)-current. This change causes no trouble for us. Let $v:=a u_{1}+(1-a) u_{2}$. Observe that $X \subset\left\{u_{1}<u_{2}\right\} \cup\left\{u_{1}>2 u_{2}\right\}$. Hence
$$\begin{aligned}
E_{\chi, \theta}(v) \leq & \int_{\left\{u_{1}<u_{2}\right\}}-\chi(v) \theta_{v}^{n}+\int_{\left\{u_{1}>2 u_{2}\right\}}-\chi(v) \theta_{v}^{n} \\
\leq & \int_{\left\{u_{1}<u_{2}\right\}}-\chi(v) \theta_{v}^{n}+\int_{\left\{u_{1}>2 u_{2}\right\}}-\chi(v) \theta_{v}^{n} \\
\leq & \sum_{k=0}^{n}\left(\int_{\left\{u_{1}<u_{2}\right\}}-\chi\left(u_{1}\right) \theta_{u_{1}}^{k} \wedge \theta_{u_{2}}^{n-k}+\int_{\left\{u_{1}>2 u_{2}\right\}}-\chi\left((2-a / 2) u_{2}\right) \theta_{u_{1}}^{k} \wedge \theta_{u_{2}}^{n-k}\right) \\
\leq & \sum_{k=0}^{n} \int_{\left\{u_{1}<u_{2}\right\}}-\chi\left(u_{1}\right) \theta_{u_{1}}^{k} \wedge \theta_{\max \left\{u_{1}, u_{2}\right\}}^{n-k}+ \\
& +\sum_{k=0}^{n} \int_{\left\{u_{1}>2 u_{2}\right\}}-2^{k+1} \chi\left(u_{2}\right) \theta_{\max \left\{u_{1} / 2, u_{2}\right\}}^{k} \wedge \theta_{u_{2}}^{n-k} \\
\leq & \sum_{k=0}^{n}\left(\int_{X}-\chi\left(u_{1}\right) \theta_{u_{1}}^{k} \wedge \theta_{\max \left\{u_{1}, u_{2}\right\}}^{n-k}+2^{k+1} \int_{X}-\chi\left(u_{2}\right) \theta_{\max \left\{u_{1} / 2, u_{2}\right\}}^{k} \wedge \theta_{u_{2}}^{n-k}\right) \\
\lesssim & E_{\chi, \theta}\left(u_{1}\right)+E_{\chi, \theta}\left(\max \left\{u_{1},\left(u_{1}+u_{2}\right) / 2\right\}\right)+E_{\chi, \theta}\left(u_{2}\right)+E_{\chi, \theta}\left(\max \left\{u_{1} / 4+u_{2} / 2, u_{2}\right\}\right) \\
\lesssim & E_{\chi, \theta}\left(u_{1}\right)+E_{\chi, \theta}\left(u_{2}\right),
\end{aligned}$$
where the two last estimates hold due to the first and third inequalities of the lemma. This finishes the proof. \(\square\)

Lemma 2.8. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}$such that $\tilde{\chi} \leq \chi$ and let $u_{1}, u_{2}, \ldots, u_{n+1} \in \mathcal{E}(X, \theta, \phi)$. Denote $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)$. Then there exists a constant $C>0$ depending only on $n$ and $M$ such that
$$-\int_{X} \chi\left(\epsilon\left(u_{1}-\phi\right)\right) \theta_{u_{2}} \wedge \ldots \wedge \theta_{u_{n+1}} \leq C B \varrho(1-\tilde{\chi}(-1)) Q_{0}(\epsilon),$$
for every $0<\epsilon \leq 1$, where
$$B=1+\max _{1 \leq j \leq n+1} E_{\tilde{\chi}, \theta, \phi}\left(u_{j}\right) / \varrho \quad \text { and } \quad Q_{0}(\epsilon):=\sup _{\{t \leq-1\}} \frac{\chi(\epsilon t)}{\tilde{\chi}(t)} \text {. }$$

Proof. Let $L$ be the left-hand side of the desired inequality. We have
$$\begin{aligned}
L & \leq-\int_{\left\{u_{1} \geq \phi-1\right\}} \chi\left(\epsilon\left(u_{1}-\phi\right)\right) \theta_{u_{2}} \wedge \ldots \wedge \theta_{u_{n+1}}-\int_{\left\{u_{1}<\phi-1\right\}} \chi\left(\epsilon\left(u_{1}-\phi\right)\right) \theta_{u_{2}} \wedge \ldots \wedge \theta_{u_{n+1}} \\
& \leq-\chi(-\epsilon) \varrho-Q_{0}(\epsilon) \int_{\left\{u_{1}<\phi-1\right\}} \tilde{\chi}\left(u_{1}-\phi\right) \theta_{u_{2}} \wedge \ldots \wedge \theta_{u_{n+1}} \\
& \leq-\varrho Q_{0}(\epsilon) \tilde{\chi}(-1)-Q_{0}(\epsilon) \int_{X} \tilde{\chi}\left(u_{1}-\phi\right) \theta_{u_{2}} \wedge \ldots \wedge \theta_{u_{n+1}} \\
& \leq-\varrho Q_{0}(\epsilon) \tilde{\chi}(-1)+C Q_{0}(\epsilon) \max _{1 \leq j \leq n+1} E_{\tilde{\chi}, \theta, \phi}\left(u_{j}\right),
\end{aligned}$$
where $C>0$ depends only on $n$ and $M$. The last estimate holds due to Lemma 2.7. Thus the desired inequality follows. \(\square\)

By the convexity/concavity and by the assumption $\tilde{\chi} \leq \chi$, we have
$$\left\{\begin{array}{l}
Q_{0}(\epsilon) \geq \epsilon Q_{0}(1) \quad \text { if } \quad x \in \widetilde{\mathcal{W}}^{-}, \\
Q_{0}(\epsilon) \leq \epsilon Q_{0}(1) \quad \text { if } \quad x \in \mathcal{W}_{M}^{+},
\end{array}\right.$$
for every $0<\epsilon \leq 1$. Moreover, if $\chi \in \widetilde{\mathcal{W}}^{-}$and $\chi(t) / \tilde{\chi}(t) \rightarrow 0$ as $t \rightarrow-\infty$, then by the definition of $Q_{0}$, we also have
$$Q_{0}(\epsilon) \leq \frac{\chi\left(-\epsilon^{1 / 2}\right)}{\tilde{\chi}(-1)}+\sup _{\left\{t \leq-\epsilon^{-1 / 2}\right\}} \frac{\chi(t)}{\tilde{\chi}(t)} \xrightarrow{\epsilon \rightarrow 0^{+}} 0 .$$

Let $u_{1}, u_{2} \in \mathcal{E}_{\chi}(X, \theta, \phi)$, and $v:=\max \left\{u_{1}, u_{2}\right\}$. Put
$$\nu\left(u_{1}, u_{2}\right):=\chi\left(-\left|u_{1}-u_{2}\right|\right)\left(\theta_{u_{2}}^{n}-\theta_{u_{1}}^{n}\right),$$
and
$$I_{\chi}\left(u_{1}, u_{2}\right):=\int_{\left\{u_{1}<u_{2}\right\}} \nu\left(u_{1}, u_{2}\right)+\int_{\left\{u_{1}>u_{2}\right\}} \nu\left(u_{2}, u_{1}\right)=\int_{X} \nu\left(u_{1}, v\right)+\int_{X} \nu\left(u_{2}, v\right) .$$

Proposition 2.9. Let $\chi \in \widetilde{\mathcal{W}^{-}} \cup \mathcal{W}_{M}^{+}$. Let $\phi$ is a negative $\theta$-psh function and $u_{1}, u_{2} \in$ $\mathcal{E}_{\chi}(X, \theta, \phi)$. Then
$$I_{\chi}\left(u_{1}, u_{2}\right) \geq 0 .$$
Proof. Denote $\mu=\theta_{u_{2}}^{n}-\theta_{u_{1}}^{n}$. Since $\chi$ is absolutely continuous, we have $\chi$ is differentiable almost everywhere and $-\chi(t)=\int_{t}^{0} \chi^{\prime}(s) d s$ for every $t<0$. Hence
$$\begin{aligned}
\int_{\left\{u_{1}<u_{2}\right\}} \nu\left(u_{1}, u_{2}\right) & =-\int_{\left\{u_{1}<u_{2}\right\}}\left(\int_{u_{1}-u_{2}}^{0} \chi^{\prime}(t) d t\right) d \mu \\
& =-\int_{\left\{u_{1}<u_{2}\right\}}\left(\int_{-\infty}^{0} \chi^{\prime}(t) \mathbf{1}_{\left\{u_{1}<u_{2}+t\right\}} d t\right) d \mu \\
& =-\int_{-\infty}^{0} \chi^{\prime}(t) \mu\left\{u_{1}<u_{2}+t\right\} d t .
\end{aligned}$$

Moreover, it follows from [17, Lemma 2.3] that $\mu\left\{u_{1}<u_{2}+t\right\} \leq 0$ for every $t \leq 0$. Hence
$$\int_{\left\{u_{1}<u_{2}\right\}} \nu\left(u_{1}, u_{2}\right)=-\int_{-\infty}^{0} \chi^{\prime}(t) \mu\left\{u_{1}<u_{2}+t\right\} d t \geq 0$$
Similarly, we have
$$\int_{\left\{u_{2}<u_{1}\right\}} \nu\left(u_{2}, u_{1}\right) \geq 0 .$$
Thus
$$I_{\chi}\left(u_{1}, u_{2}\right)=\int_{\left\{u_{1}<u_{2}\right\}} \nu\left(u_{1}, u_{2}\right)+\int_{\left\{u_{2}<u_{1}\right\}} \nu\left(u_{2}, u_{1}\right) \geq 0 .$$ \(\square\)

\section*{3 Stability estimates for fixed singularity type}

\subsection*{3.1 Main results}

Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}(M \geq 1)$ such that $\tilde{\chi} \leq \chi$. For each constant $t \geq 0$, we denote
$$Q(t)=Q_{\chi, \tilde{\chi}}(t):=\left\{\begin{array}{l}
1 \quad \text { if } \quad t \geq 1, \\
\left(Q_{0}(t) / Q_{0}(1)\right)^{1 / 2} \quad \text { if } \quad 0<t<1 \quad \text { and } \quad \chi \in \widetilde{\mathcal{W}}^{-} \\
t^{1 / 2} \quad \text { if } \quad 0<t<1 \quad \text { and } \quad \chi \in \mathcal{W}_{M}^{+}, \\
\lim _{s \rightarrow 0^{+}} Q(s) \quad \text { if } \quad t=0 .
\end{array}\right.$$
where $Q_{0}$ is defined as in Lemma 2.8. We remove the subscript $\chi, \tilde{\chi}$ from $Q_{\chi, \tilde{\chi}}$ if $\chi, \tilde{\chi}$ are clear from the context. Note that $Q$ is increasing continuous function in $t$ and
$$Q(0)=0 \quad \text { if either } \quad \chi, \tilde{\chi} \in \mathcal{W}_{M}^{+} \quad \text { or } \quad \lim _{t \rightarrow-\infty} \frac{\chi(t)}{\tilde{\chi}(t)}=0 .$$

Now, we state the main results of this section. For the convenience, we normalize energies with respect to $\varrho:=\int_{X} \theta_{\phi}^{n}$ as follows
$$E_{\tilde{\chi}, \theta, \phi}^{0}:=\varrho^{-1} E_{\tilde{\chi}, \theta, \phi}, \quad I_{\chi}^{0}\left(u_{1}, u_{2}\right)=\varrho^{-1} I_{\chi}\left(u_{1}, u_{2}\right) .$$

Theorem 3.1. Let $\theta$ be a closed smooth real (1, 1)-form and $\phi$ be a negative $\theta$-psh function such that $\varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}(M \geq 1)$ such that $\tilde{\chi} \leq \chi$. Let $B \geq 1$ be a constant and let $u_{j}, \psi_{j} \in \mathcal{E}(X, \theta, \phi)$ satisfy $u_{1} \leq u_{2}$ and
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{j}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(\psi_{j}\right) \leq B,$$
for $j=1,2$. Then there exists a constant $C_{n}>0$ depending only on $n$ and $M$ such that
$$\int_{X}-\chi\left(u_{1}-u_{2}\right)\left(\theta_{\psi_{1}}^{n}-\theta_{\psi_{2}}^{n}\right) \leq C_{n} \varrho B^{2}(1-\tilde{\chi}(-1))^{2} Q^{\circ n}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right),$$
where $Q$ is defined by (3.1), and $Q^{\circ n}:=Q \circ Q \circ \cdots \circ Q$ ( $n$-iterate of $Q$ ).

Since the measure $\theta_{\psi_{1}}^{n}-\theta_{\psi_{2}}^{n}$ is not positive, we need the following consequence of the above theorem for later applications on stability estimates.

Theorem 3.2. Let $\theta$ be a closed smooth real (1, 1)-form and $\phi$ be a negative $\theta$-psh function such that $\phi=P_{\theta}[\phi], \varrho:=\operatorname{vol}\left(\theta_{\phi}\right)>0$ and $\theta \leq A \omega$ for some constant $A \geq 1$. Let $\chi, \tilde{\chi} \in \widetilde{\mathcal{W}}^{-} \cup \mathcal{W}_{M}^{+}$ ( $M \geq 1$ ) such that $\tilde{\chi} \leq \chi$. Let $B \geq 1$ be a constant and $u_{1}, u_{2}, \psi \in \mathcal{E}(X, \theta, \phi)$ satisfying
$$E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{1}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}\left(u_{2}\right)+E_{\tilde{\chi}, \theta, \phi}^{0}(\psi) \leq B,$$
for $j=1,2$. Then, for every constant $m>0$ and $0<\gamma<1$, there exists a constant $C>0$ depending on $n, M, X, \omega, m$ and $\gamma$ such that
$$\int_{X}-\chi\left(-\left|u_{1}-u_{2}\right|\right) \theta_{\psi}^{n} \leq-\varrho \chi\left(-\left|a_{1}-a_{2}\right|-\lambda^{m}\right)+C \varrho A^{(1-\gamma) / m}(B-\tilde{\chi}(-A))^{2}(1-\tilde{\chi}(-1))^{2} \lambda^{\gamma},$$
where $a_{j}:=\sup _{X} u_{j}$ and $\lambda=Q^{\circ n}\left(I_{\chi}^{0}\left(u_{1}, u_{2}\right)\right)$.

\subsection*{3.2 Proof of Theorem 3.1}

Here is the first step in the proof of Theorem 3.1.
Lemma 3.3. If Theorem 3.1 holds for $u_{j}, \psi_{j}$ of the same singularity type as $\phi$, then it holds for the general case.