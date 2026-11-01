---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: Regularity_of_weak_solutions_of_a_complex_Monge_Ampère_equation_8d11ed95c88a.pdf
converter: mathpix
format: mmd
---

\title{
Analysis \& PDE
}

Volume 4 No. 3 2011

Gábor Székelyhidi and Valentino Tosatti

REGULARITY OF WEAK SOLUTIONS OF A COMPLEX MONGE-AMPÈRE EQUATION
\begin{itemize}
\item[] ■ mathematical sciences publishers
\end{itemize}

\title{
REGULARITY OF WEAK SOLUTIONS OF A COMPLEX MONGE-AMPÈRE EQUATION
}

\author{
Gábor Székelyhidi and Valentino Tosatti
}

\begin{abstract}
We prove the smoothness of weak solutions to an elliptic complex Monge-Ampère equation, using the smoothing property of the corresponding parabolic flow.
\end{abstract}

\section*{1. Introduction}

Let $(M, \omega)$ be a compact Kähler manifold. Our main result is the following.
Theorem 1. Suppose that $\varphi \in P S H(M, \omega) \cap L^{\infty}(M)$ is a solution of the equation
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{-F(\varphi, z)} \omega^{n}$$
in the sense of pluripotential theory [Bedford and Taylor 1976], where $F: \mathbb{R} \times M \rightarrow \mathbb{R}$ is smooth. Then $\varphi$ is smooth.

In particular, if $M$ is Fano, $\omega \in c_{1}(M)$, and $h_{\omega}$ satisfies $\sqrt{-1} \partial \bar{\partial} h_{\omega}=\operatorname{Ric}(\omega)-\omega$, then we can set $F(\varphi, z)=\varphi-h_{\omega}$. The result then implies that Kähler-Einstein currents with bounded potentials are in fact smooth. Such weak Kähler-Einstein metrics were studied by Berman, Boucksom, Guedj, and Zeriahi in [Berman et al. 2009], as part of their variational approach to complex Monge-Ampère equations.

It follows from [Kołodziej 2008] (see also [Guedj et al. 2008]) that the solution $\varphi$ in Theorem 1 is automatically $C^{\alpha}$ for some $\alpha>0$, but it does not seem possible to use this directly to get further regularity. The difficulty is that in the equation
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{f} \omega^{n},$$
the $C^{1}$ estimate for $\varphi$ (due to Błocki [2009] and Hanani [1996]) depends on a $C^{1}$ bound for $f$, and in turn the Laplacian estimate for $\varphi$ (due to Yau [1978] and Aubin [1976]) depends on the Laplacian of $f$.

To get around this difficulty we look at the corresponding parabolic flow
$$\frac{\partial \varphi}{\partial t}=\log \frac{(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}}{\omega^{n}}+F(\varphi, z) .$$
Following the construction of [Song and Tian 2009] for the Kähler-Ricci flow, we show that to find a solution for a short time, it is enough to have a $C^{0}$ initial condition $\varphi_{0}$ for which $\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{0}\right)^{n}$ is bounded (see also [Chen and Ding 2007; Chen and Tian 2008; Chen et al. 2011] for earlier results, as well as [Simon 2002] for a weaker statement in the Riemannian case). The solution of the flow will be smooth at any positive time. Then we need to argue that if the initial condition $\varphi_{0}$ is a weak solution of the elliptic problem then the flow is stationary, so in fact $\varphi_{0}$ is smooth.

\footnotetext{
MSC2000: primary 32Q20, 32W20, 35J60; secondary 53C44.
Keywords: complex Monge-Ampère equations, regularity of weak solutions, parabolic flows.
}

In Section 2 we show that the flow (with smooth initial data) exists for a short time, which only depends on a bound for sup $\left|\varphi_{0}\right|$ and sup $\left|\dot{\varphi}_{0}\right|$. In Section 3 we use this to construct a solution to the flow with rough initial data, and we prove Theorem 1.

\section*{2. Existence for the parabolic equation}

In this section we consider the parabolic equation
$$\frac{\partial \varphi}{\partial t}=\log \frac{(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}}{\omega^{n}}+F(\varphi, z),$$
where $F: \mathbb{R} \times M \rightarrow \mathbb{R}$ is smooth and we have the smooth initial condition $\left.\varphi\right|_{t=0}=\varphi_{0}$. We write $\dot{\varphi}_{0}$ for $\partial \varphi / \partial t$ at $t=0$.

The main result of this section is the following:
Proposition 2. There exist $T>0$ depending only on $\sup \left|\varphi_{0}\right|$, sup $\left|\dot{\varphi}_{0}\right|$ (and $\omega$ and $F$ ), such that there is a smooth solution $\varphi(t, z):[0, T] \times M \rightarrow \mathbb{R}$ to (1). We also have smooth functions $C_{k}:(0, T] \rightarrow \mathbb{R}$ depending only on $\sup \left|\varphi_{0}\right|, \sup \left|\dot{\varphi}_{0}\right|$ such that
$$\|\varphi(t)\|_{C^{k}(M)}<C_{k}(t)$$
as long as $t \leqslant T$. (Note that $C_{k}(t) \rightarrow \infty$ as $t \rightarrow 0$.)
The proof of the $C^{1}$ estimate is based on the arguments in [Błocki 2009] (see also [Hanani 1996; Phong and Sturm 2010]), whereas the $C^{2}$ estimate is based on the Aubin-Yau second order estimate [Aubin 1976; Yau 1978] (see also [Song and Tian 2009] for the parabolic version we need here). The $C^{3}$ and higher order estimates follow the standard arguments in [Yau 1978; Cao 1985; Phong et al. 2007], although there are a few new terms to control.

The existence of a smooth solution for $t \in\left[0, T^{\prime}\right)$ for some $T^{\prime}>0$ that depends on the $C^{2, \alpha}$ norm of $\varphi_{0}$ is standard. The aim is to obtain the estimates (2), which allow us to extend the solution up to a time $T$, which only depends on the initial condition in a weaker way. We will write $\varphi(t)$ for the short time solution.

Lemma 3. There exists $T, C>0$ depending only on $\sup \left|\varphi_{0}\right|$ and sup $\left|\dot{\varphi}_{0}\right|$ such that
$$|\varphi(t)|,|\dot{\varphi}(t)|<C,$$
as long as the solution exists and $t \leqslant T$. In particular,
$$\left|\log \frac{(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}}{\omega^{n}}\right|<C$$
for $t \leqslant T$.
Proof. For all $s$, define
$$\bar{F}(s)=\sup _{z \in M} F(s, z),$$
which is a continuous function. At any given time $t$ where $\varphi$ exists, the maximum of $\varphi(t, \cdot)$ is achieved at some point $z \in M$, and at $z$ we have
$$\log \frac{(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}}{\omega^{n}} \leqslant 0 .$$

It follows that
$$\frac{d \varphi_{\max }}{d t} \leqslant F\left(\varphi_{\max }, z\right) \leqslant \bar{F}\left(\varphi_{\max }\right),$$
where the derivative is interpreted as the limsup of the forward difference quotients at the points where it does not exist (compare [Hamilton 1986, Lemma 3.5]). Comparing with the solution of the corresponding ODE, we find that there exist $T, C>0$ depending only on sup $\left|\varphi_{0}\right|$ such that as long as our solution exists, and $t \leqslant T$, we have $\sup \varphi(t)<C$. In a similar way we get a lower bound on $\varphi(t, \cdot)$, so we have $|\varphi(t)|<C$ as long as the solution exists and $t \leqslant T$.

Differentiating the equation we obtain
$$\frac{\partial \dot{\varphi}}{\partial t}=\Delta_{\varphi} \dot{\varphi}+F^{\prime}(\varphi, z) \dot{\varphi},$$
where $F^{\prime}$ is the derivative of $F$ with respect to the $\varphi$ variable. Since $F^{\prime}(\varphi, z)$ is bounded as long as $\varphi$ is bounded, from the maximum principle we get
$$\sup |\dot{\varphi}(t)|<\sup |\dot{\varphi}(0)| e^{\kappa t},$$
where $\kappa$ depends on $F$ and $\sup |\varphi(0)|$. Hence for our choice of $T$, we get
$$\sup |\dot{\varphi}(t)|<C,$$
for $t \leqslant T$, where $C$ depends on $\sup \left|\varphi_{0}\right|$ and $\sup \left|\dot{\varphi}_{0}\right|$. \(\square\)

In the lemmas below $T$ will be the same as in the previous lemma.
Lemma 4. There exists $C>0$ depending on $\sup \left|\varphi_{0}\right|$ and sup $\left|\dot{\varphi}_{0}\right|$ such that
$$|\nabla \varphi(t)|_{\omega}^{2}<e^{C / t},$$
as long as the solution exists and $t \leqslant T$ for the $T$ in Lemma 3.
Proof. We modify Błocki's estimate [2009] for the complex Monge-Ampère equation (compare [Hanani 1996]). Define
$$K=t \log |\nabla \varphi|_{\omega}^{2}-\gamma(\varphi),$$
where $\gamma$ will be chosen later. Suppose that $\sup _{(0, t] \times M} K=K(t, z)$ is achieved. Pick normal coordinates for $\omega$ at $z$, such that $\varphi_{i \bar{j}}$ is diagonal at this point (here and henceforth, indices will denote covariant derivatives with respect to the metric $\omega$ ). We write $\beta=|\nabla \varphi|_{\omega}^{2}$ and $\Delta_{\varphi}$ for the Laplacian of the metric $\omega+\sqrt{-1} \partial \bar{\partial} \varphi$. There exists $B>0$ such that
$$\begin{gathered}
0 \leqslant\left(\frac{\partial}{\partial t}-\Delta_{\varphi}\right) K \leqslant-\frac{t}{\beta} \sum_{i, p} \frac{\left|\varphi_{i p}\right|^{2}+\left|\varphi_{i \bar{p}}\right|^{2}}{1+\varphi_{p \bar{p}}}+\left(t^{-1}\left(\gamma^{\prime}\right)^{2}+\gamma^{\prime \prime}\right) \sum_{p} \frac{\left|\varphi_{p}\right|^{2}}{1+\varphi_{p \bar{p}}} \\
-\left(\gamma^{\prime}-B t\right) \sum_{p} \frac{1}{1+\varphi_{p \bar{p}}}+\log \beta+\frac{C t}{\beta}-\gamma^{\prime} \dot{\varphi}+n \gamma^{\prime}+C t .
\end{gathered}$$
The constant $C$ depends on bounds for $F$ and $F^{\prime}$, and also we used that $\nabla K=0$ at $(t, z)$.
Now we apply Błocki's trick to get rid of the term containing $\left(\gamma^{\prime}\right)^{2}$. At $(t, z)$ we have
$$t \beta_{p}=\gamma^{\prime} \beta \varphi_{p},$$
where
$$\beta_{p}=\varphi_{p} \varphi_{p \bar{p}}+\sum_{j} \varphi_{j p} \varphi_{\bar{j}},$$
remembering that $\varphi_{j \bar{p}}$ is diagonal. It follows that
$$\sum_{j} \varphi_{j p} \varphi_{\bar{j}}=\left(t^{-1} \gamma^{\prime} \beta-\varphi_{p \bar{p}}\right) \varphi_{p},$$
and so
$$\frac{t}{\beta} \sum_{j, p} \frac{\left|\varphi_{j p}\right|^{2}}{1+\varphi_{p \bar{p}}} \geqslant \frac{t}{\beta^{2}} \sum_{p} \frac{\left|\sum_{j} \varphi_{j p} \varphi_{\bar{j}}\right|^{2}}{1+\varphi_{p \bar{p}}}=\frac{t}{\beta^{2}} \sum_{p} \frac{\left|t^{-1} \gamma^{\prime} \beta-\varphi_{p \bar{p}}\right|^{2}\left|\varphi_{p}\right|^{2}}{1+\varphi_{p \bar{p}}} \geqslant t^{-1}\left(\gamma^{\prime}\right)^{2} \sum_{p} \frac{\left|\varphi_{p}\right|^{2}}{1+\varphi_{p \bar{p}}}-2 \gamma^{\prime},$$
where we assume that $\gamma^{\prime}>0$. Also from Lemma 3 we know that $\dot{\varphi}$ is bounded. Combining these estimates we obtain
$$0 \leqslant \gamma^{\prime \prime} \sum_{p} \frac{\left|\varphi_{p}\right|^{2}}{1+\varphi_{p \bar{p}}}-\left(\gamma^{\prime}-B t\right) \sum_{p} \frac{1}{1+\varphi_{p \bar{p}}}+\log \beta+\frac{C t}{\beta}+C \gamma^{\prime}+C t .$$
We now choose $\gamma(s)=A s-\frac{1}{A} s^{2}$. We can assume that $\log \beta>1$ at $(t, z)$, so in particular $\frac{t}{\beta}$ is bounded above as long as $t<T$. Then if $A$ is chosen sufficiently large, we get a constant $C^{\prime}>0$ such that
$$\sum_{p} \frac{1}{1+\varphi_{p \bar{p}}}+\sum_{p} \frac{\left|\varphi_{p}\right|^{2}}{1+\varphi_{p \bar{p}}} \leqslant C^{\prime} \log \beta,$$
so in particular $\left(1+\varphi_{p \bar{p}}\right)^{-1} \leqslant C^{\prime} \log \beta$ for each $p$. From (4) we know that
$$\prod_{p}\left(1+\varphi_{p \bar{p}}\right)<C,$$
so
$$1+\varphi_{p \bar{p}} \leqslant C\left(C^{\prime} \log \beta\right)^{n-1},$$
and using (8) we get
$$\beta=\sum_{p}\left|\varphi_{p}\right|^{2} \leqslant C\left(C^{\prime} \log \beta\right)^{n} .$$
This shows that $\beta<C$ and in turn $K<C$ for some constant $C$. So either $K$ achieves a maximum for some $t>0$ in which case we have just bounded it, or it achieves its maximum for $t=0$, which is bounded in terms of $\sup \left|\varphi_{0}\right|$. \(\square\)

From now on, we write $g$ for the metric $\omega$ and $g_{\varphi}$ for the metric $\omega+\sqrt{-1} \partial \bar{\partial} \varphi$.
Lemma 5. There exists $C>0$ depending on $\sup \left|\varphi_{0}\right|$ and $\sup \left|\dot{\varphi}_{0}\right|$ such that
$$0<\operatorname{tr}_{g}\left(g_{\varphi}\right)=n+\Delta_{g} \varphi(t)<e^{C e^{C / t}},$$
as long as the solution exists and $t \leqslant T$, where $T$ is as in Lemma 3.
Proof. We let
$$H=e^{-\alpha / t} \log \operatorname{tr}_{g}\left(g_{\varphi}\right)-A \varphi,$$
where $\alpha=C$ from Lemma 4 and $A$ is chosen later. In particular we will use that $e^{-\alpha / t}|\nabla \varphi|_{g}^{2}<1$. Standard calculations (from [Aubin 1976; Yau 1978]) show that there exist $B>0$ such that
$$\Delta_{\varphi} \log \operatorname{tr}_{g}\left(g_{\varphi}\right) \geqslant-B \operatorname{tr}_{g_{\varphi}} g-\frac{\operatorname{tr}_{g} \operatorname{Ric}\left(g_{\varphi}\right)}{\operatorname{tr}_{g}\left(g_{\varphi}\right)} .$$
Using this we can compute
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\right. & \left.\Delta_{\varphi}\right) H \\
& \leqslant \frac{\alpha e^{-\alpha / t}}{t^{2}} \log \operatorname{tr}_{g}\left(g_{\varphi}\right)+\frac{C e^{-\alpha / t}}{\operatorname{tr}_{g}\left(g_{\varphi}\right)}+\frac{e^{-\alpha / t} \Delta_{g} F(\varphi, z)}{\operatorname{tr}_{g}\left(g_{\varphi}\right)}+B e^{-\alpha / t} \operatorname{tr}_{g_{\varphi}} g-A \dot{\varphi}+A n-A \operatorname{tr}_{g_{\varphi}} g
\end{aligned}$$
Here
$$\Delta_{g} F(\varphi, z)=\Delta_{g} F+2 \operatorname{Re}\left(g^{i \bar{j}} F_{i}^{\prime} \varphi_{\bar{j}}\right)+F^{\prime} \Delta_{g} \varphi+F^{\prime \prime}|\nabla \varphi|_{g}^{2},$$
where $F^{\prime}$ is the derivative in the $\varphi$ variable, and $\Delta_{g} F$ is the Laplacian of $F(\varphi, z)$ in the $z$ variable. So we have constants $C_{1}, C_{2}, C_{3}$ such that
$$\Delta_{g} F(\varphi, z) \leqslant C_{1}+C_{2}|\nabla \varphi|_{g}^{2}+C_{3} \operatorname{tr}_{g}\left(g_{\varphi}\right) .$$
From (4) we have bounds on above and below on $\frac{\operatorname{det} g_{\varphi}}{\operatorname{det} g}$, so for some constant $C$ we have $\operatorname{tr}_{g}\left(g_{\varphi}\right)>C^{-1}$ and also $\operatorname{tr}_{g}\left(g_{\varphi}\right) \leqslant C\left(\operatorname{tr}_{g_{\varphi}} g\right)^{n-1}$. Using these in (10) we get
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\varphi}\right) H & \leqslant-\left(A-B e^{-\alpha / t}\right) \operatorname{tr}_{g_{\varphi}} g+C \log \operatorname{tr}_{g_{\varphi}} g+C \\
& \leqslant-\left(A-C-B e^{-\alpha / t}\right) \operatorname{tr}_{g_{\varphi}} g+C^{\prime},
\end{aligned}$$
as long as $t \leqslant T$. Choosing $A$ large enough, we can use the maximum principle to bound $H$ in terms of its value for $t=0$, which is bounded by $\sup \left|\varphi_{0}\right|$. \(\square\)

We note here that if one is interested in the special case of weak Kähler-Einstein currents (i.e., $F=$ $\varphi-h_{\omega}$ ), then the gradient estimate in Lemma 4 is not needed. We now describe how to get the higher order estimates, as long as the solution exists and $t \leqslant T$, for the $T$ from Lemma 3. As in [Yau 1978], we let $\varphi_{i \bar{j} k}$ be the third covariant derivative of $\varphi$ with respect to the Levi-Civita connection of $\omega$, and we define
$$S=g_{\varphi}^{i \bar{p}} g_{\varphi}^{q \bar{j}} g_{\varphi}^{k \bar{r}} \varphi_{i \bar{j} k} \varphi_{\bar{p} q \bar{r}} .$$
From now on, we will denote by $C(t)$ a smooth real function defined on $(0, T]$, which is allowed to blow up when $t$ approaches zero, which depends only on $\sup \left|\varphi_{0}\right|$, sup $\left|\dot{\varphi}_{0}\right|$ and which may vary from line to line. These functions $C(t)$ can be made completely explicit. Using (9) it is clear that an estimate of the form $S \leqslant C(t)$ implies an estimate of the form $\|\varphi(t)\|_{C^{2+\alpha}(g)} \leqslant C(t)$, for any $0<\alpha<1$. To estimate $S$ we first compute its evolution. It is convenient to use the general computation by Phong, Šešum, and Sturm [Phong et al. 2007], which uses the following notation. We denote by $h_{j}^{i}=g^{i \bar{k}}\left(g_{j \bar{k}}+\varphi_{j \bar{k}}\right)$, which is an endomorphism of the tangent bundle. Then $S$ can be written in terms of the connection $\nabla h h^{-1}$ as
$$S=g_{\varphi}^{p \bar{q}} g_{\varphi, i j} g_{\varphi}^{k \bar{\ell}}\left(\nabla_{p} h h^{-1}\right)_{k}^{i} \overline{\left(\nabla_{q} h h^{-1}\right)_{\ell}^{j}}=\left|\nabla h h^{-1}\right|_{g_{\varphi}}^{2},$$
where ∇ is the Levi-Civita connection of $\omega_{\varphi}$. Then the computations in [Phong et al. 2007] yield
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\varphi}\right) S=-\left|\nabla\left(\nabla h h^{-1}\right)\right|_{g_{\varphi}}^{2}-\mid & \left.\bar{\nabla}\left(\nabla h h^{-1}\right)\right|_{g_{\varphi}} ^{2}+2 \operatorname{Re}\left\langle\left(\nabla T-\nabla R, \nabla h h^{-1}\right\rangle_{g_{\varphi}}\right. \\
& +\left(\nabla_{p} h h^{-1}\right)_{k}^{i}\left(\nabla_{q} h h^{-1}\right)_{\ell}^{j}\left(T^{p \bar{q}} g_{\varphi, i \bar{j}} g_{\varphi}^{k \bar{\ell}}-g_{\varphi}^{p \bar{q}} T_{i \bar{j}} g_{\varphi}^{k \bar{\ell}}+g_{\varphi}^{p \bar{q}} g_{\varphi, i \bar{j}} T^{k \bar{\ell}}\right),
\end{aligned}$$
where $T_{i \bar{j}}=-\left(\partial g_{\varphi} / \partial t+\operatorname{Ric}\left(g_{\varphi}\right)\right)_{i \bar{j}},(\nabla T)_{q r}^{p}=g_{\varphi}^{p \bar{s}} \nabla_{q} T_{r \bar{s}},(\nabla R)_{q r}^{p}=g_{\varphi}^{s \bar{t}} \nabla_{s} R_{r q \bar{t}}^{p}$ and $R_{r q \bar{t}}^{p}$ is the curvature of the fixed metric $g$. Along the standard Kähler-Ricci flow the tensor $T$ vanishes, while in our case differentiating (1) we get
$$-T_{i \bar{j}}=\operatorname{Ric}(g)_{i \bar{j}}+F^{\prime \prime} \varphi_{i} \varphi_{\bar{j}}+F^{\prime} \varphi_{i \bar{j}}+F_{i \bar{j}}+2 \operatorname{Re}\left(F_{i}^{\prime} \varphi_{\bar{j}}\right) .$$
Using (7) and (9) we can then estimate
$$\left|\left(\nabla_{p} h h^{-1}\right)_{k}^{i} \overline{\left(\nabla_{q} h h^{-1}\right)_{\ell}^{j}}\left(T^{p \bar{q}} g_{\varphi, i \bar{j}} g_{\varphi}^{k \bar{\ell}}-g_{\varphi}^{p \bar{q}} T_{i j} g_{\varphi}^{k \bar{\ell}}+g_{\varphi}^{p \bar{q}} g_{\varphi, i \bar{j}} T^{k \bar{\ell}}\right)\right| \leqslant C(t) S .$$
The term $2 \operatorname{Re}\left\langle\nabla R, \nabla h h^{-1}\right\rangle_{g_{\varphi}}$ is comparable to $S$, but bounding $2 \operatorname{Re}\left\langle\nabla T, \nabla h h^{-1}\right\rangle_{g_{\varphi}}$ requires a bit more work. Differentiating (11) and using (3), (7) and (9) we see that all the terms in $2 \operatorname{Re}\left\langle\nabla T, \nabla h h^{-1}\right\rangle_{g_{\varphi}}$ are comparable to $C(t) S$ except for two terms of the form
$$\left\langle\varphi_{i j} g_{\varphi}^{k \bar{\ell}} \varphi_{\bar{\ell}},\left(\nabla_{i} h h^{-1}\right)_{j}^{k}\right\rangle_{g_{\varphi}} .$$
We bound these by $\left|\varphi_{i j}\right|_{g_{\varphi}}^{2}+C(t) S$, so overall we get
$$\left(\frac{\partial}{\partial t}-\Delta_{\varphi}\right) S \leqslant C(t) S+\left|\varphi_{i j}\right|_{g_{\varphi}}^{2}+C .$$
The term $C(t) S$ can be controlled by using $\operatorname{tr}_{g}\left(g_{\varphi}\right)$ in the usual way [Phong et al. 2007]. For the term $\left|\varphi_{i j}\right|_{g_{\varphi}}^{2}$ we note that using (3), (7) and (9) we have
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta_{\varphi}\right)|\nabla \varphi|_{g}^{2} & \leqslant-\sum_{i, p} \frac{\left|\varphi_{i p}\right|^{2}+\left|\varphi_{i \bar{p}}\right|^{2}}{1+\varphi_{p \bar{p}}}+2 \operatorname{Re}\left\langle\nabla \varphi, F^{\prime} \nabla \varphi+\nabla F\right\rangle_{g}+C \operatorname{tr}_{g_{\varphi}} g|\nabla \varphi|_{g}^{2} \\
& \leqslant-\frac{\left|\varphi_{i j}\right|_{g_{\varphi}}^{2}}{C(t)}+C(t) .
\end{aligned}$$
We can then apply the maximum principle to the quantity
$$G=\frac{S}{C_{1}(t)}+\frac{\operatorname{tr}_{g}\left(g_{\varphi}\right)}{C_{2}(t)}+\frac{|\nabla \varphi|_{g}^{2}}{C_{3}(t)},$$
for suitable functions $C_{i}(t)$ that depend only on the given data, and get $G \leqslant C$, which implies the desired estimate for $S$. This means that as long as the solution exists and $0<t \leqslant T$ we have a bound on $\|\varphi(t)\|_{C^{2+\alpha}(M)}$. Since by standard parabolic theory one can start the flow with initial data in $C^{2+\alpha}$, this shows that the flow has a $C^{2+\alpha}$ solution defined on $[0, T]$.

The next step is to estimate $\sup |\ddot{\varphi}(t)|$ and $\sup \left|\partial_{i} \partial_{\bar{j}} \dot{\varphi}(t)\right|$. It is easy to see that both of these quantities are bounded if we bound $\left|\operatorname{Ric}\left(g_{\varphi}\right)\right|_{g_{\varphi}}$. Following the computation in [Phong et al. 2011, p. 107] one can derive the following estimate (there are essentially no new bad terms in this case)
$$\left(\frac{\partial}{\partial t}-\Delta_{\varphi}\right)\left|\operatorname{Ric}\left(g_{\varphi}\right)\right|_{g_{\varphi}} \leqslant C(t)\left|\operatorname{Rm}\left(g_{\varphi}\right)\right|^{2}+C(t) .$$

From one of the two good positive terms in the evolution of $S$ we get
$$\left(\frac{\partial}{\partial t}-\Delta_{\varphi}\right) S \leqslant-\frac{\left|\operatorname{Rm}\left(g_{\varphi}\right)\right|^{2}}{C(t)}+C(t)$$
and so the maximum principle applied to the quantity
$$\frac{\left|\operatorname{Ric}\left(g_{\varphi}\right)\right|_{g_{\varphi}}}{C_{1}(t)}+\frac{S}{C_{2}(t)}$$
gives the desired bound $\left|\operatorname{Ric}\left(g_{\varphi}\right)\right|_{g_{\varphi}} \leqslant C(t)$.
It now follows from the parabolic Schauder estimates applied to (5) that we have bounds for $\varphi$ in the parabolic Hölder space $C^{2+\alpha, 1+\alpha / 2}(M \times[\varepsilon, T])$ for any $\varepsilon>0$, with the bounds only depending on $\varepsilon$, $\sup \left|\varphi_{0}\right|$ and sup $\left|\dot{\varphi}_{0}\right|$. By the parabolic Schauder estimates we then also get bounds on all higher order derivatives for $\varphi$, and letting $\varepsilon \rightarrow 0$ we get the required bounds on $\varphi(t)$ that blow up as $t$ goes to zero. In particular, we get a smooth solution $\varphi(t)$ that exists on $[0, T]$, with bounds as in (2). This completes the proof of Proposition 2.

\section*{3. Proof of Theorem 1}

Suppose that $\varphi$ is a bounded $\omega$-plurisubharmonic solution of the equation
$$(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}=e^{-F(\varphi, z)} \omega^{n},$$
where $F$ is a smooth function. First of all we want to prove existence of the flow (1) with rough initial data $\varphi$. For this, we follow the proof in [Song and Tian 2009] in the case of Kähler-Ricci flow.

It follows from [Kołodziej 1998] that in this case $\varphi$ is continuous (in fact it is even $C^{\alpha}$; see [Guedj et al. 2008; Kołodziej 2008]). Let us approximate $\varphi$ with a sequence of smooth functions $u_{k}$, such that
$$\sup _{M}\left|\varphi-u_{k}\right| \rightarrow 0,$$
as $k \rightarrow \infty$. By the theorem in [Yau 1978] there are smooth functions $\psi_{k}$ such that
$$\left(\omega+\sqrt{-1} \partial \bar{\partial} \psi_{k}\right)^{n}=c_{k} e^{-F\left(u_{k}, z\right)} \omega^{n},$$
where the positive constants $c_{k}$ are chosen so that the integrals of both sides of (14) match. When $k$ is large we see that $c_{k}$ approaches 1 . Moreover, we can normalize the solution $\psi_{k}$ so that
$$\sup _{M}\left(\psi_{k}-\varphi\right)=\sup _{M}\left(\varphi-\psi_{k}\right) .$$
Using (13) together with Kołodziej's stability result [2003] we obtain
$$\lim _{k \rightarrow \infty}\left\|\psi_{k}-\varphi\right\|_{L^{\infty}}=0 .$$
Using Proposition 2 we can solve the equation
$$\frac{\partial \varphi_{k}}{\partial t}=\log \frac{\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{k}\right)^{n}}{\omega^{n}}+F\left(\varphi_{k}, z\right)-\log c_{k},$$
with initial condition $\left.\varphi_{k}\right|_{t=0}=\psi_{k}$ for a short time $t \in[0, T]$ independent of $k$, since by (13), (14) and (15) we have uniform bounds on the initial data $\sup \left|\psi_{k}\right|$ and $\sup \left|\dot{\varphi}_{k}(0)\right|$. As in [Song and Tian 2009] we have:

Lemma 6. The sequence $\varphi_{k}$ is a Cauchy sequence in $C^{0}([0, T] \times M)$, ie.
$$\lim _{j, k \rightarrow \infty}\left\|\varphi_{j}-\varphi_{k}\right\|_{L^{\infty}([0, T] \times M)}=0 .$$
Proof. Fix $j, k$ and let $\mu=\varphi_{j}-\varphi_{k}$. Then
$$\frac{\partial \mu}{\partial t}=\log \frac{\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{k}+\sqrt{-1} \partial \bar{\partial} \mu\right)^{n}}{\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{k}\right)^{n}}+F\left(\varphi_{j}, z\right)-F\left(\varphi_{k}, z\right)+\log \frac{c_{k}}{c_{j}},$$
and $\left.\mu\right|_{t=0}=\psi_{j}-\psi_{k}$. At any time given time $t$, the maximum of $\mu$ is achieved at some point $z \in M$, and at $z$ we have
$$\frac{d \mu_{\max }}{d t} \leqslant F\left(\varphi_{j}(t, z), z\right)-F\left(\varphi_{k}(t, z), z\right)+\log \frac{c_{k}}{c_{j}} \leqslant \kappa|\mu(z)|+\log \frac{c_{k}}{c_{j}},$$
where $\kappa$ is independent of $j, k$. Here and henceforth the derivative is interpreted as the limsup of the forward difference quotients at the points where it does not exist [Hamilton 1986, Lemma 3.5]. Similarly, at the point $z^{\prime}$ where the minimum of $\mu$ is achieved, we have
$$\frac{d \mu_{\min }}{d t} \geqslant-\kappa\left|\mu\left(z^{\prime}\right)\right|+\log \frac{c_{k}}{c_{j}} .$$
Putting these together we see that
$$\frac{d|\mu|_{\max }}{d t} \leqslant \kappa|\mu|_{\max }+\left|\log \frac{c_{k}}{c_{j}}\right| .$$
It follows that
$$\sup _{[0, T] \times M}\left|\varphi_{j}-\varphi_{k}\right| \leqslant e^{\kappa T}\left(\left\|\psi_{j}-\psi_{k}\right\|_{L^{\infty}(M)}+\frac{1}{\kappa}\left|\log \frac{c_{k}}{c_{j}}\right|\right)-\frac{1}{\kappa}\left|\log \frac{c_{k}}{c_{j}}\right| .$$
Now (15) and the fact that $c_{k}$ converges to 1 imply the result. \(\square\)

Using this lemma we can define
$$\Phi=\lim _{j \rightarrow \infty} \varphi_{j},$$
which is in $C^{0}([0, T] \times M)$. Moreover from Proposition 2 for any $\varepsilon>0$ we have uniform bounds on all derivatives of the $\varphi_{j}$ for $t \in[\varepsilon, T]$, so in fact for all $k$ we have
$$\lim _{j \rightarrow \infty}\left\|\Phi-\varphi_{j}\right\|_{C^{k}(M \times[\varepsilon, T])}=0 .$$
From (6) we get
$$\sup _{M}\left|\dot{\varphi}_{k}(t)\right|<C \sup _{M}\left|\dot{\varphi}_{k}(0)\right|$$
for $t \in[0, T)$, but from (16) we have
$$\dot{\varphi}_{k}(0)=\log \frac{\left(\omega+\sqrt{-1} \partial \bar{\partial} \psi_{k}\right)^{n}}{\omega^{n}}+F\left(\psi_{k}, z\right)-\log c_{k}=F\left(\psi_{k}, z\right)-F\left(\varphi_{k}, z\right)-\log c_{k},$$
which converges to zero when $k$ goes to infinity. It follows that for any $t>0$ we have
$$\dot{\Phi}(t)=\lim _{j \rightarrow \infty} \dot{\varphi}_{j}(t)=0 .$$
Hence $\Phi$ is constant on ( $0, T$ ), but since it is continuous on $[0, T]$ it follows that $\Phi(t)=\Phi(0)$ for all $t \leqslant T$. But $\Phi(0)$ is our solution $\varphi$ of (12), whereas $\Phi(t)$ is smooth for $t>0$. Hence $\varphi$ is smooth.

\section*{Acknowledgements}

We thank D. H. Phong for support and encouragement as well as J. Song and J. Sturm for very valuable help and B. Weinkove for useful comments. Tosatti is also grateful to S.-T. Yau for his support.

The question answered in Theorem 1 arose after R. Berman's talk at the workshop "Complex Monge-Ampère Equation" at Banff in October 2009, and we would like to thank him as well as the participants and organizers of that workshop for providing a stimulating working environment.

Székelyhidi was supported in part by National Science Foundation grant DMS-0904223.

\section*{References}
[Aubin 1976] T. Aubin, "Équations du type Monge-Ampère sur les variétés kähleriennes compactes", C. R. Acad. Sci. Paris Sér. A-B 283:3 (1976), A119-A121. MR 55 \#6496
[Bedford and Taylor 1976] E. Bedford and B. A. Taylor, "The Dirichlet problem for a complex Monge-Ampère equation", Invent. Math. 37:1 (1976), 1-44. MR 56 \#3351 Zbl 0315.31007
[Berman et al. 2009] R. Berman, S. Boucksom, V. Guedj, and A. Zeriahi, "A variational approach to complex Monge-Ampère equations", preprint, 2009. arXiv 0907.4490
[Błocki 2009] Z. Błocki, "A gradient estimate in the Calabi-Yau theorem", Math. Ann. 344:2 (2009), 317-327. MR 2010d: 32046 Zbl 1167.32023
[Cao 1985] H. D. Cao, "Deformation of Kähler metrics to Kähler-Einstein metrics on compact Kähler manifolds", Invent. Math. 81:2 (1985), 359-372. MR 87d:58051
[Chen and Ding 2007] X. X. Chen and W. Ding, "Ricci flow on surfaces with degenerate initial metrics", J. Partial Differential Equations 20:3 (2007), 193-202. MR 2008g:53081 Zbl 1174.53025
[Chen and Tian 2008] X. X. Chen and G. Tian, "Geometry of Kähler metrics and foliations by holomorphic discs", Publ. Math. Inst. Hautes Études Sci. 107 (2008), 1-107. MR 2009g:32048
[Chen et al. 2011] X. X. Chen, G. Tian, and Z. Zhang, "On the weak Kähler-Ricci flow", Trans. Amer. Math. Soc. 363:6 (2011), 2849-2863. MR 2775789
[Guedj et al. 2008] V. Guedj, S. Kolodziej, and A. Zeriahi, "Hölder continuous solutions to Monge-Ampére equations", Bull. Lond. Math. Soc. 40:6 (2008), 1070-1080. MR 2010a:32066
[Hamilton 1986] R. S. Hamilton, "Four-manifolds with positive curvature operator", J. Differential Geom. 24:2 (1986), 153-179. MR 87m:53055 Zbl 0628.53042
[Hanani 1996] A. Hanani, "Équations du type de Monge-Ampère sur les variétés hermitiennes compactes", J. Funct. Anal. 137:1 (1996), 49-75. MR 97c:32018 Zbl 0847.53045
[Kołodziej 1998] S. Kołodziej, "The complex Monge-Ampère equation", Acta Math. 180:1 (1998), 69-117. MR 99h:32017 Zbl 0913.35043
[Kołodziej 2003] S. Kołodziej, "The Monge-Ampère equation on compact Kähler manifolds", Indiana Univ. Math. J. 52:3 (2003), 667-686. MR 2004i:32062
[Kołodziej 2008] S. Kołodziej, "Hölder continuity of solutions to the complex Monge-Ampère equation with the right-hand side in $L^{p}$ : the case of compact Kähler manifolds", Math. Ann. 342:2 (2008), 379-386. MR 2009g:32079
[Phong and Sturm 2010] D. H. Phong and J. Sturm, "The Dirichlet problem for degenerate complex Monge-Ampère equations", Comm. Anal. Geom. 18:1 (2010), 145-170. MR 2011i:32039 Zbl 1222.32044
[Phong et al. 2007] D. H. Phong, N. Sesum, and J. Sturm, "Multiplier ideal sheaves and the Kähler-Ricci flow", Comm. Anal. Geom. 15:3 (2007), 613-632. MR 2009a:32037
[Phong et al. 2011] D. H. Phong, J. Song, J. Sturm, and B. Weinkove, "On the convergence of the modified Kähler-Ricci flow and solitons", Comment. Math. Helv. 86:1 (2011), 91-112. MR 2745277
[Simon 2002] M. Simon, "Deformation of $C^{0}$ Riemannian metrics in the direction of their Ricci curvature", Comm. Anal. Geom. 10:5 (2002), 1033-1074. MR 2003j:53107 Zbl 1034.58008
[Song and Tian 2009] J. Song and G. Tian, "The Kähler-Ricci flow through singularities", preprint, 2009. arXiv 0909.4898
[Yau 1978] S. T. Yau, "On the Ricci curvature of a compact Kähler manifold and the complex Monge-Ampère equation, I", Comm. Pure Appl. Math. 31:3 (1978), 339-411. MR 81d:53045

Received 11 Dec 2009. Accepted 13 Jul 2010.
GÁBOR Székelyhidi: gszekely@nd.edu
Department of Mathematics, University of Notre Dame, Notre Dame, IN 46556, United States
http://www.nd.edu/~gszekely
Valentino Tosatti: tosatti@math.columbia.edu
Department of Mathematics, Columbia University, 2990 Broadway, New York, NY 10027, United States
http://www.math.columbia.edu/~tosatti

\section*{Analysis \& PDE}
pjm.math.berkeley.edu/apde

\section*{EDITORS}

Editor-in-Chief
Maciej Zworski
University of California
Berkeley, USA
Board of Editors

\begin{tabular}[t]{|l|l|l|l|}
\hline Michael Aizenman & Princeton University, USA aizenman@math.princeton.edu & Nicolas Burq & Université Paris-Sud 11, France nicolas.burq@math.u-psud.fr \\
\hline Luis A. Caffarelli & University of Texas, USA caffarel@math.utexas.edu & Sun-Yung Alice Chang & Princeton University, USA chang@math.princeton.edu \\
\hline Michael Christ & University of California, Berkeley, USA mchrist@math.berkeley.edu & Charles Fefferman & Princeton University, USA cf@math.princeton.edu \\
\hline Ursula Hamenstaedt & Universität Bonn, Germany ursula@math.uni-bonn.de & Nigel Higson & Pennsylvania State Univesity, USA higson@math.psu.edu \\
\hline Vaughan Jones & University of California, Berkeley, USA vfr@math.berkeley.edu & Herbert Koch & Universität Bonn, Germany koch@math.uni-bonn.de \\
\hline Izabella Laba & University of British Columbia, Canada ilaba@math.ubc.ca & Gilles Lebeau & Université de Nice Sophia Antipolis, France lebeau@unice.fr \\
\hline László Lempert & Purdue University, USA lempert@math.purdue.edu & Richard B. Melrose & Massachussets Institute of Technology, USA rbm@math.mit.edu \\
\hline Frank Merle & Université de Cergy-Pontoise, France Frank.Merle@u-cergy.fr & William Minicozzi II & Johns Hopkins University, USA minicozz@math.jhu.edu \\
\hline Werner Müller & Universität Bonn, Germany mueller@math.uni-bonn.de & Yuval Peres & University of California, Berkeley, USA peres@stat.berkeley.edu \\
\hline Gilles Pisier & Texas A\&M University, and Paris 6 pisier@math.tamu.edu & Tristan Rivière & ETH, Switzerland riviere@math.ethz.ch \\
\hline Igor Rodnianski & Princeton University, USA irod@math.princeton.edu & Wilhelm Schlag & University of Chicago, USA schlag@math.uchicago.edu \\
\hline Sylvia Serfaty & New York University, USA serfaty@cims.nyu.edu & Yum-Tong Siu & Harvard University, USA siu@math.harvard.edu \\
\hline Terence Tao & University of California, Los Angeles, USA tao@math.ucla.edu & Michael E. Taylor & Univ. of North Carolina, Chapel Hill, USA met@math.unc.edu \\
\hline Gunther Uhlmann & University of Washington, USA gunther@math.washington.edu & András Vasy & Stanford University, USA andras@math.stanford.edu \\
\hline Dan Virgil Voiculescu & University of California, Berkeley, USA dvv@math.berkeley.edu & Steven Zelditch & Northwestern University, USA zelditch@math.northwestern.edu \\
\hline
\end{tabular}

\section*{PRODUCTION}
contact@msp.org
Silvio Levy, Scientific Editor
Sheila Newbery, Senior Production Editor
See inside back cover or pjm.math.berkeley.edu/apde for submission instructions.
The subscription price for 2011 is US \$120/year for the electronic version, and \$180/year for print and electronic. Subscriptions, requests for back issues from the last three years and changes of subscribers address should be sent to Mathematical Sciences Publishers, Department of Mathematics, University of California, Berkeley, CA 94720-3840, USA.

Analysis \& PDE, at Mathematical Sciences Publishers, Department of Mathematics, University of California, Berkeley, CA 94720-3840 is published continuously online. Periodical rate postage paid at Berkeley, CA 94704, and additional mailing offices.

APDE peer review and production are managed by EditFLow™ from Mathematical Sciences Publishers.

\section*{Analysis \& PDE}
Volume 4 No. 3 ..... 2011
Regularity of weak solutions of a complex Monge-Ampère equation ..... 369 Gábor Székelyhidi and Valentino Tosatti
Traveling waves for the cubic Szegő equation on the real line ..... 379 Oana Pocovnicu
Scattering threshold for the focusing nonlinear Klein-Gordon equation ..... 405 Slim Ibrahim, Nader Masmoudi and Kenji Nakanishi
Rayleigh-type surface quasimodes in general linear elasticity ..... 463 Sönke Hansen