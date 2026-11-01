---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Self-dual Einstein ACH metrics and CR GJMS operators in dimension three]

---
source_file: Self-dual_Einstein_ACH_metrics_and_CR_GJMS_operators_in_dimension_three_3a640c168c17.pdf
converter: mathpix
format: mmd
---

\title{
SELF-DUAL EINSTEIN ACH METRICS AND CR GJMS OPERATORS IN DIMENSION THREE
}

\author{
TAIJI MARUGAME
}

\begin{abstract}
By refining Matsumoto's construction of Einstein ACH metrics, we construct a one parameter family of ACH metrics which solve the Einstein equation to infinite order and have a given three dimensional CR structure at infinity. When the parameter is 0, the metric is self-dual to infinite order. As an application, we give another proof of the fact that three dimensional CR manifolds admit CR invariant powers of the sublaplacian (CR GJMS operators) of all orders, which has been proved by Gover-Graham. We also prove the convergence of the formal solutions when the CR structure is real analytic.
\end{abstract}

\section*{1. Introduction}

The GJMS operator $\mathcal{P}_{2 k}$ on a conformal manifold of dimension $N$ is an invariant linear differential operator acting on conformal densities of weight $k-N / 2$ whose principal part is the power $\Delta^{k}$ of the Laplacian [13]. It plays an important role in geometric analysis on conformal manifolds, and is also related to a fundamental curvature quantity, called the $Q$-curvature, whose integral gives a global conformal invariant [7, 9, 14]. The GJMS operator is constructed via the (Fefferman-Graham) ambient metric [8] or equivalently via the Poincaré metric whose boundary at infinity is the given conformal manifold [7, 14]. The ambient metric is a formal solution to the Ricci flat equation, which corresponds to the Einstein equation for the Poincaré metric. When the dimension $N$ is odd, the equation can be solved to infinite order and $\mathcal{P}_{2 k}$ is defined for all $k \geq 1$. On the other hand, when $N$ is even, an obstruction to the existence of a formal solution appears, and $\mathcal{P}_{2 k}$ can only be defined for $1 \leq k \leq N / 2$ due to the ambiguity of the ambient metric at higher orders. Moreover, it is known that this result of the existence of $\mathcal{P}_{2 k}$ is sharp [11].

The CR counterpart of these operators are CR invariant powers of the sublaplacian
$$P_{2 k}: \mathcal{E}\left(\frac{k-n-1}{2}, \frac{k-n-1}{2}\right) \longrightarrow \mathcal{E}\left(\frac{-k-n-1}{2}, \frac{-k-n-1}{2}\right)$$
on a $(2 n+1)$-dimensional CR manifold $M$, which are called the CR GJMS operators or the Gover-Graham operators [10, 15]. Here, $\mathcal{E}\left(w, w^{\prime}\right)$ is a complex line bundle over $M$ called the CR density of weight $\left(w, w^{\prime}\right)$; see §2.1 for the definition. One can associate a conformal structure to a circle bundle over $M$, called the Fefferman conformal structure [6], and apply the GJMS construction to produce $P_{2 k}$ for $1 \leq$ $k \leq n+1$. Gover-Graham [10] gave more operators by using techniques of CR tractor calculus; they proved that for each $\left(w, w^{\prime}\right)$ such that $k=w+w^{\prime}+n+1 \in$ $\mathbb{N}_{+}$and $\left(w, w^{\prime}\right) \notin \mathbb{N} \times \mathbb{N}$, there exists a CR invariant linear differential operator $P_{w, w^{\prime}}: \mathcal{E}\left(w, w^{\prime}\right) \rightarrow \mathcal{E}\left(w-k, w^{\prime}-k\right)$ whose principal part is $\Delta_{b}^{k}$. In cases where $w=w^{\prime}$, these operators provide CR invariant modifications of $\Delta_{b}^{k}$ for all $k$ with $k \equiv n \bmod 2$. When $n=1$, even more operators can be constructed: CR structure is a Cartan geometry modeled on the CR sphere $S^{2 n+1}=S U(n+1,1) / P$, where $P$

\footnotetext{
2010 Mathematics Subject Classification. Primary 32V05, Secondary 53A55.
Key words and phrases. ACH metrics; the Einstein equation; self-duality; CR manifolds; CR invariant differential operators.
}
is the isotropy subgroup of a point in $S^{2 n+1}$, and three dimensional CR structure has a special feature from this viewpoint in that $P$ is a Borel subgroup. Then the BGG machinery developed in [3] gives operators $P_{w, w^{\prime}}$ for $\left(w, w^{\prime}\right) \in \mathbb{N} \times \mathbb{N}$ when $n=1$. Thus one has:

Theorem 1.1 ([10, Theorem 1.3]). Let $M$ be a three dimensional strictly pseudoconvex CR manifold. For each $\left(w, w^{\prime}\right)$ such that $k=w+w^{\prime}+2 \in \mathbb{N}_{+}$, there exists a CR invariant linear differential operator $P_{w, w^{\prime}}: \mathcal{E}\left(w, w^{\prime}\right) \rightarrow \mathcal{E}\left(w-k, w^{\prime}-k\right)$ on $M$, whose principal part is $\Delta_{b}^{k}$.

In this paper, we provide a unified proof of Theorem 1.1 for cases in which $w=$ $w^{\prime}$. To this end, we construct an ACH (asymptotically complex hyperbolic) metric on a manifold with boundary $M$ whose Taylor expansion along $M$ is completely determined by local data of $M$. Our ACH metric is a refinement of the ACH Einstein metric which Matsumoto [19, 20] constructed for partially integrable CR manifolds. To state the results, let us recall some basic notions related to ACH metrics. Let $M$ be a $(2 n+1)$-dimensional strictly pseudoconvex partially integrable CR manifold. Namely, $M$ has a contact distribution $H \subset T M$ together with an almost complex structure $J \in \operatorname{End}(H)$, and the eigenspace $T^{1,0} M \subset \mathbb{C} H$ with the eigenvalue $i$ satisfies the partial integrability: $\left[\Gamma\left(T^{1,0} M\right), \Gamma\left(T^{1,0} M\right)\right] \subset \Gamma(\mathbb{C} H)$. A $\Theta$-structure on a manifold $\bar{X}$ with boundary $M$ is a conformal class $[\Theta]$ of sections $\Theta \in \Gamma\left(M, T^{*} \bar{X}\right)$ such that $\left.\Theta\right|_{T M}$ is a contact form on $M$. A diffeomorphism which preserves a $\Theta$-structure is called a $\Theta$-diffeomorphism. On the product $M \times[0, \infty)_{\rho}$, we define the standard $\Theta$-structure by extending each contact form $\theta$ on $M$ to $\Theta$ so that $\Theta(\partial / \partial \rho)=0$. Fix a contact form $\theta$ on $M$ and let $\left\{T, Z_{\alpha}\right\}$ be an admissible frame. We take the local frame $\left\{\boldsymbol{Z}_{\infty}=\rho \partial_{\rho}, \boldsymbol{Z}_{0}=\rho^{2} T, \boldsymbol{Z}_{\alpha}=\rho Z_{\alpha}, \boldsymbol{Z}_{\bar{\alpha}}=\rho Z_{\bar{\alpha}}\right\}$ and its dual coframe $\left\{\boldsymbol{\theta}^{\infty}, \boldsymbol{\theta}^{0}, \boldsymbol{\theta}^{\alpha}, \boldsymbol{\theta}^{\bar{\alpha}}\right\}$ on $M \times(0, \infty)_{\rho}$. Then for any ACH metric $g$ on $X$, there exists a $\Theta$-diffeomorphism $\Phi: M \times[0, \infty)_{\rho} \rightarrow \bar{X}$ which is defined near $M$ and restricts to the identity on $M$, such that $\Phi^{*} g=g_{I J} \boldsymbol{\theta}^{I} \boldsymbol{\theta}^{J}$ satisfies
$$\begin{gathered}
g_{\infty \infty}=4, \quad g_{\infty 0}=g_{\infty \alpha}=0, \quad g_{00}=1+O(\rho), \quad g_{0 \alpha}=O(\rho), \\
g_{\alpha \beta}=O(\rho), \quad g_{\alpha \bar{\beta}}=h_{\alpha \bar{\beta}}+O(\rho),
\end{gathered}$$
where $h_{\alpha \bar{\beta}}$ is the Levi form on $M$. The CR manifold $M$ is called the CR structure at infinity of $g$. Matsumoto [19, 20] proved that for any partially integrable CR manifold $M$, there exists an ACH metric $g$ on $M \times[0, \infty)_{\rho}$ which satisfies
$$\begin{array}{r}
E_{I J}:=\operatorname{Ric}_{I J}+\frac{n+2}{2} g_{I J}=O\left(\rho^{2 n+2}\right), \\
\text { Scal }=-(n+1)(n+2)+O\left(\rho^{2 n+3}\right),
\end{array}$$
where Ric is the Ricci tensor and Scal is the scalar curvature. Up to the pullback by a $\Theta$-diffeomorphism which fixes $M$, such a metric is unique modulo tensors which have $O\left(\rho^{2 n+2}\right)$ coefficients and $O\left(\rho^{2 n+3}\right)$ trace in the frame $\left\{\boldsymbol{Z}_{I}\right\}$. The order $O\left(\rho^{2 n+2}\right)$ in the above equation is optimal in general since $\left.\left(\rho^{-2 n-2} E_{\alpha \beta}\right)\right|_{M}$ is independent of the choice of a solution $g$ and defines a CR invariant tensor $\mathcal{O}_{\alpha \beta} \in \mathcal{E}_{\alpha \beta}(-n,-n)$, called the CR obstruction tensor. Matsumoto [21] generalized the CR GJMS operators $P_{2 k}$ to the partially integrable case by using Dirichlet-to-Neumann type operator for the eigenvalue equations of the Laplacian of $g$, but the order is again restricted to $1 \leq k \leq n+1$ due to the presence of the obstruction.

If we confine ourselves to the case where $M$ is an integrable CR manifold, there is a possibility to refine the construction of ACH metrics. In fact, the CR obstruction tensor vanishes for integrable CR manifolds, in particular for three dimensional CR manifolds since the CR structure is always integrable in this dimension. However, we need an additional normalization condition on the metric to ensure the
uniqueness since the Einstein equation does not determine the $O\left(\rho^{2 n+2}\right)$-term of the metric. A possible normalization is the Kähler condition; Fefferman [6] constructed an approximate solution to the complex Monge-Ampère equation on a strictly pseudoconvex domain $\Omega$ with boundary $M$ and defined a Kähler metric which satisfies $E_{I J}=O\left(\rho^{2 n+4}\right)$ as an ACH metric on the 'square root' of $\Omega$. However, this construction also has an obstruction $\mathcal{O} \in \mathcal{E}(-n-2,-n-2)$, called the CR obstruction density, and the metric is only determined modulo $O\left(\rho^{2 n+4}\right)$.

In this paper, we show that the self-dual equation $W^{-}=0$ works as a better normalization when $M$ is three dimensional. The anti self-dual part $W^{-}$of the Weyl curvature is connected to the Ricci tensor by the Bianchi identity
$$\nabla^{I} W_{I J K L}^{-}=C_{J K L}^{-},$$
where $C_{I J K}^{-}$is the anti self-dual part of the Cotton tensor $C_{I J K}$, which is defined by $C_{I J K}:=\nabla_{K} P_{I J}-\nabla_{J} P_{I K}$ with the Schouten tensor $P_{I J}=\frac{1}{2} \operatorname{Ric}_{I J}-\frac{1}{12} \operatorname{Scal} g_{I J}$. It follows from (1.1) that the equation $E_{I J}=O\left(\rho^{4}\right)$ implies $W_{I J K L}^{-}=O\left(\rho^{4}\right)$, and it turns out that the further normalization $W_{I J K L}^{-}=O\left(\rho^{5}\right)$ determines $g_{I J}$ modulo $O\left(\rho^{5}\right)$. We can then solve $E_{I J}=O\left(\rho^{6}\right)$, which implies $W_{I J K L}^{-}=O\left(\rho^{6}\right)$. In the next step, besides the Einstein equation, we have freedom to prescribe the value of
$$\eta:=\left.\left(\rho^{-6} W_{\infty 0 \infty 0}^{-}\right)\right|_{M} .$$
If the Taylor coefficients of $g_{I J}$ along $M$ have universal expressions in terms of pseudo-hermitian structure, $\eta$ defines a CR invariant of weight (-3, -3) (see Lemma 4.1). Thus, we should prescribe $\eta$ to be a CR invariant in order to obtain a CR invariant normalization condition. It is known that a CR invariant in $\mathcal{E}(-3,-3)$ on a three dimensional CR manifold is unique up to a constant multiple [12], so there is no choice but to set $\eta=\lambda \mathcal{O}$ with a constant $\lambda \in \mathbb{R}$. After this step, the Einstein equation determines $g_{I J}$ to infinite order, and in the case $\lambda=0$ the self-duality follows automatically from (1.1). Thus our main theorem reads as follows:

Theorem 1.2. Let $M$ be a three dimensional strictly pseudoconvex $C R$ manifold, and let $\lambda \in \mathbb{R}$. Then there exists an ACH metric $g_{I J}^{\lambda}$ on $M \times[0, \infty)_{\rho}$ which has $M$ as the CR structure at infinity and satisfies
$$\operatorname{Ric}_{I J}+\frac{3}{2} g_{I J}^{\lambda}=O\left(\rho^{\infty}\right), \quad W_{I J K L}^{-}=O\left(\rho^{6}\right), \quad \eta=\lambda \mathcal{O},$$
where $\eta$ is the density defined by (4.1). The metric $g_{I J}^{\lambda}$ is unique modulo $O\left(\rho^{\infty}\right)$ up to the pull-back by a $\Theta$-diffeomorphism which fixes $M$. Moreover, $g_{I J}^{0}$ satisfies $W_{I J K L}^{-}=O\left(\rho^{\infty}\right)$.

The Taylor coefficients of $g_{I J}^{\lambda}$ along the boundary have universal expressions in terms of the pseudo-hermitian structure for a fixed contact form.

By applying the construction of the CR GJMS operators via the ACH metric [21], we obtain the following theorem, which is a special case of Theorem 1.1:

Theorem 1.3. Let $M$ be a three dimensional strictly pseudoconvex CR manifold, and let $\lambda \in \mathbb{R}$. Then, there exists a $C R$ invariant linear differential operator
$$P_{2 k}^{\lambda}: \mathcal{E}(k / 2-1, k / 2-1) \longrightarrow \mathcal{E}(-k / 2-1,-k / 2-1)$$
which is a polynomial in $\lambda$ of degree $\leq k / 3$, and has the principal part $\Delta_{b}^{k}$.
Let us mention a similar construction in conformal geometry. Fefferman-Graham [8] constructed a formal solution to the self-dual Einstein equation for the Poincaré metric with a given three dimensional conformal manifold $\mathcal{M}$ as its conformal infinity. Thus our result is a CR analogue of their construction. When $\mathcal{M}$ is real analytic, LeBrun [16] showed by twistor methods that there exists a real analytic self-dual Einstein metric on $\mathcal{M} \times(0, \epsilon)$ with the conformal infinity $\mathcal{M}$. The metric
of Fefferman-Graham gives the Taylor expansion of LeBrun's metric. In CR case, Biquard [2] showed the existence of a self-dual Einstein ACH metric with a given real analytic CR three-manifold as its infinity by using twistor methods. Thus our formal solution $g_{I J}^{0}$ gives the Taylor expansion of Biquard's metric. In this paper, we prove the convergence of $g_{I J}^{\lambda}$ by applying the results of Baouendi-Goulaouic [1] on singular nonlinear Cauchy problems.

Theorem 1.4. Suppose $M$ is a real analytic strictly pseudoconvex CR manifold of dimension three. Then the formal solution $g_{I J}^{\lambda}$ in Theorem 1.2 converges to a real analytic ACH metric near M.

This paper is organized as follows. In §2, we review pseudo-hermitian geometry on a CR manifold and basic notions on ACH metric. By following Matsumoto [19], we describe the Levi-Civita connection of an ACH metric in terms of the extended Tanaka-Webster connection. In §3, we clarify the relationship between the Einstein equation and the self-dual equation, and compute the variation of curvature quantities under a perturbation of the metric. §4 is devoted to the proof of Theorem 1.2; we construct a one parameter family of formal solutions to the Einstein equation and examine the dependence on the parameter. Then, in §5 we use these metrics to construct the CR GJMS operators and prove Theorem 1.3. Finally, in §6 we show the convergence of the formal solutions in case $M$ is a real analytic CR manifold.

Acknowledgements. The author is grateful to Kengo Hirachi and Yoshihiko Matsumoto for invaluable comments on the results. He also thanks Matsumoto for checking the author's suggestion of some minor corrections to the computation in his thesis [19].

\section*{2. CR structure and ACH metric}
2.1. Pseudo-hermitian geometry. Let $M$ be a $(2 n+1)$-dimensional $C^{\infty}$ manifold. A pair $(H, J)$ is called a $C R$ structure on $M$ if $H$ is a rank $2 n$ subbundle of $T M$ and $J$ is an almost complex structure on $H$ which satisfies the (formal) integrability condition
$$\left[\Gamma\left(T^{1,0} M\right), \Gamma\left(T^{1,0} M\right)\right] \subset \Gamma\left(T^{1,0} M\right),$$
where $T^{1,0} M \subset \mathbb{C} H$ is the eigenspace of $J$ with the eigenvalue $i$. We note that the integrability condition automatically holds when $M$ is three dimensional. For any real 1-form $\theta$ such that $\operatorname{Ker} \theta=H$, we define the Levi form $h_{\theta}$ by
$$h_{\theta}(Z, \bar{W})=-i d \theta(Z, \bar{W})$$
for $Z, W \in T^{1,0} M$. We say the CR structure is strictly pseudoconvex if $h_{\theta}$ is positive definite for some $\theta$. Since $h_{f \theta}=f h_{\theta}$ for any function $f$, such $\theta$ is determined up to a multiple by a positive function. When $M$ is strictly pseudoconvex, $H$ defines a contact structure, so we call $\theta$ a contact form. The Reeb vector field is the real vector field $T$ uniquely determined by the conditions
$$\theta(T)=1, \quad T\lrcorner d \theta=0 .$$
Let $\left\{Z_{\alpha}\right\}$ be a local frame for $T^{1,0} M$. If we put $Z_{\bar{\alpha}}:=\overline{Z_{\alpha}}$, then $\left\{T, Z_{\alpha}, Z_{\bar{\alpha}}\right\}$ gives a local frame for $\mathbb{C} T M$, which we call an admissible frame. The dual coframe $\left\{\theta, \theta^{\alpha}, \theta^{\bar{\alpha}}\right\}$ is called an admissible coframe and satisfies
$$d \theta=i h_{\alpha \bar{\beta}} \theta^{\alpha} \wedge \theta^{\bar{\beta}},$$
where $h_{\alpha \bar{\beta}}=h_{\theta}\left(Z_{\alpha}, Z_{\bar{\beta}}\right)$.

The $C R$ canonical bundle is defined by $K_{M}:=\wedge^{n+1}\left(T^{0,1} M\right)^{\perp} \subset \wedge^{n+1} \mathbb{C} T^{*} M$, where $T^{0,1} M:=\overline{T^{1,0} M}$. When $K_{M}^{-1}$ admits an $(n+2)$-nd root $\mathcal{E}(1,0)$, the $C R$ density bundle is defined by
$$\mathcal{E}\left(w, w^{\prime}\right)=\mathcal{E}(1,0)^{\otimes w} \otimes \overline{\mathcal{E}(1,0)}{ }^{\otimes w^{\prime}}$$
for each $\left(w, w^{\prime}\right) \in \mathbb{C}^{2}$ with $w-w^{\prime} \in \mathbb{Z}$. In this paper, we restrict ourselves to the cases $w=w^{\prime}$. In these cases, the definition (2.1) is independent of the choice of $\mathcal{E}(1,0)$ so we can define $\mathcal{E}(w, w)$ without assuming the global existence of $\mathcal{E}(1,0)$. We also denote the space of sections of these bundles by the same symbols, and call them CR densities.

For any contact form $\theta$, there exists a local nonvanishing section $\zeta$ of $K_{M}$, unique up to a multiple of a $U(1)$-valued function, which satisfies
$$\left.\left.\theta \wedge(d \theta)^{n}=i^{n^{2}} n!\theta \wedge(T\lrcorner \zeta\right) \wedge(T\lrcorner \bar{\zeta}\right) .$$
Then, the weighted contact form $\boldsymbol{\theta}:=\theta \otimes|\zeta|^{-2 /(n+2)} \in \Gamma\left(T^{*} M \otimes \mathcal{E}(1,1)\right)$ is defined globally and independent of the choice of $\theta$. Thus, there is a one to one correspondence between the set of contact forms and the set of positive sections $\tau \in \mathcal{E}(1,1)$, called CR scales. We define the CR invariant weighted Levi form $\boldsymbol{h}_{\alpha \bar{\beta}}:=\tau h_{\alpha \bar{\beta}}$ by putting a weight to $h_{\theta}$ with the CR scale $\tau$ corresponding to $\theta$. We raise and lower the indices of tensors on $\mathbb{C} H$ by $\boldsymbol{h}_{\alpha \bar{\beta}}$ and its inverse $\boldsymbol{h}^{\alpha \bar{\beta}}$, which has weight (-1, -1).

For a fixed contact form $\theta$, we can define a canonical linear connection ∇ on $T M$, called the Tanaka-Webster connection. It preserves $T^{1,0} M$ and satisfies $\nabla T=0$, $\nabla h_{\theta}=0$. In an admissible frame $\left\{T, Z_{\alpha}, Z_{\bar{\alpha}}\right\}$, the connection 1-forms $\omega_{\beta}{ }^{\alpha}$ satisfy the structure equation
$$d \theta^{\alpha}=\theta^{\beta} \wedge \omega_{\beta}^{\alpha}+A_{\bar{\beta}}^{\alpha} \boldsymbol{\theta} \wedge \theta^{\bar{\beta}} .$$
The tensor $A_{\alpha \beta}:=\overline{A_{\bar{\alpha} \bar{\beta}}}$ satisfies $A_{\alpha \beta}=A_{\beta \alpha}$ and is called the Tanaka-Webster torsion tensor. We use the index 0 for the direction of $T$, and we denote the components of covariant derivatives of a tensor by indices preceded by a comma, e.g., $A_{\alpha \gamma, \bar{\beta}}=\nabla_{\bar{\beta}} A_{\alpha \gamma}$. We omit the comma for covariant derivatives of a function. The curvature form $\Omega_{\alpha}{ }^{\beta}=d \omega_{\alpha}{ }^{\beta}-\omega_{\alpha}{ }^{\gamma} \wedge \omega_{\gamma}{ }^{\beta}$ is given by
$$\begin{aligned}
\Omega_{\alpha}{ }^{\beta}= & R_{\alpha}{ }^{\beta}{ }_{\gamma \bar{\mu}} \theta^{\gamma} \wedge \theta^{\bar{\mu}}+A_{\alpha \gamma,}{ }^{\beta} \theta^{\gamma} \wedge \boldsymbol{\theta}-A^{\beta} \bar{\gamma}, \alpha \theta^{\bar{\gamma}} \wedge \boldsymbol{\theta} \\
& -i A_{\alpha \gamma} \theta^{\gamma} \wedge \theta^{\beta}+i \boldsymbol{h}_{\alpha \bar{\gamma}} A^{\beta} \bar{\mu} \theta^{\bar{\gamma}} \wedge \theta^{\bar{\mu}} .
\end{aligned}$$
The tensor $R_{\alpha}{ }^{\beta}{ }_{\gamma \bar{\mu}}$ is called the Tanaka-Webster curvature tensor. Taking traces with the weighted Levi form, we define the Tanaka-Webster Ricici tensor $\operatorname{Ric}_{\alpha \bar{\beta}}:=$ $R_{\gamma}{ }^{\gamma}{ }_{\alpha \bar{\beta}}$ and the Tanaka-Webster scalar curvature Scal $:=\operatorname{Ric}_{\alpha}{ }^{\alpha}$. The sublaplacian is the differential operator $\Delta_{b}: \mathcal{E}\left(w, w^{\prime}\right) \rightarrow \mathcal{E}\left(w-1, w^{\prime}-1\right)$ defined by
$$\Delta_{b} f=-\boldsymbol{h}^{\alpha \bar{\beta}}\left(\nabla_{\alpha} \nabla_{\bar{\beta}}+\nabla_{\bar{\beta}} \nabla_{\alpha}\right) f .$$
If we rescale the contact form as $\widehat{\theta}=e^{\Upsilon} \theta$, the Tanaka-Webster connection and its curvature quantities satisfy transformation formulas involving the derivatives of the scaling factor $\Upsilon$; see e.g., [17]. We note that in dimension three the rank of $T^{1,0} M$ is 1 and the curvature form (2.2) is reduced to
$$\Omega_{1}{ }^{1}=\operatorname{Scal} \boldsymbol{h}_{1 \overline{1}} \theta^{1} \wedge \theta^{\overline{1}}+A_{11}{ }^{1} \theta^{1} \wedge \boldsymbol{\theta}-A_{\overline{1}, 1}^{1} \theta^{\overline{1}} \wedge \boldsymbol{\theta} .$$
Also, in this dimension, $M$ is locally CR diffeomorphic to the standard sphere $S^{3}$ if and only if the Cartan tensor
$$Q_{11}:=\frac{1}{6} \operatorname{Scal}_{11}+\frac{i}{2} \operatorname{Scal} A_{11}-A_{11,0}-\frac{2 i}{3} A_{11, \overline{1}}^{\overline{1}}$$
vanishes identically. The Cartan tensor is a CR invariant tensor of weight (-1, -1). We also have a CR invariant density defined by
$$\mathcal{O}:=\left(\nabla^{1} \nabla^{1}-i A^{11}\right) Q_{11} \in \mathcal{E}(-3,-3),$$
called the obstruction density. It follows from the Bianchi identity for the Cartan tensor that $\mathcal{O}$ is a real density [4]. There is also a CR invariant density, called the obstruction density, on higher dimensional CR manifolds and it appears as the logarithmic coefficient in the asymptotic expansion of the solution to the complex Monge-Ampère equation on strictly pseudoconvex domain [18]. In dimension three, a CR invariant of weight (-3, -3) is unique up to a constant multiple [12], so it is necessarily a multiple of $\mathcal{O}$.
2.2. ACH metrics. The ACH metric was introduced by Epstein-Melrose-Mendoza [5] as a generalization of the complex hyperbolic metric on the ball. In this paper, we define it by using the characterization via the normal form.

Let $X$ be the interior of a $(2 n+2)$-dimensional $C^{\infty}$ manifold whose boundary $M$ is equipped with a strictly pseudoconvex CR structure $(H, J)$. A conformal class $[\Theta]$ in $\Gamma\left(M, T^{*} \bar{X}\right)$ is called a $\Theta$-structure if $\left.\Theta\right|_{T M}$ gives a contact form on $M$ for each $\Theta \in[\Theta]$. We call $(\bar{X},[\Theta])$ a $\Theta$-manifold. Let $\left(\bar{X}^{\prime},\left[\Theta^{\prime}\right]\right)$ be another $\Theta$-manifold with the same boundary $M$. Then, a diffeomorphism $\Phi$ from a neighborhood of $M$ in $\bar{X}$ to a neighborhood of $M$ in $\bar{X}^{\prime}$ is called a $\Theta$-diffeomorphism if it fixes $M$ and satisfies $\left[\Phi^{*} \Theta^{\prime}\right]=[\Theta]$. We take a boundary defining function $\rho \in C^{\infty}(\bar{X})$ which is positive on $X$. A vector field $V$ on $\bar{X}$ is called a $\Theta$-vector field if it satisfies
$$\left.V\right|_{M}=0, \quad \widetilde{\Theta}(V)=O\left(\rho^{2}\right),$$
where $\widetilde{\Theta}$ is an arbitrary extension of a $\Theta \in[\Theta]$. Note that the definition is independent of the choice of $\Theta$ and $\widetilde{\Theta}$. We extend $\{d \rho, \widetilde{\Theta}\}$ to a local coframe $\left\{d \rho, \widetilde{\Theta}, \alpha^{1}, \ldots, \alpha^{2 n}\right\}$ for $T^{*} \bar{X}$ near $M$. Let $\left\{N, T, Y_{1}, \ldots, Y_{2 n}\right\}$ be the dual frame. Then, any $\Theta$-vector field $V$ can be written as
$$V=V^{\infty}(\rho N)+V^{0}\left(\rho^{2} T\right)+V^{i}\left(\rho Y_{i}\right), \quad V^{\infty}, V^{0}, V^{i} \in C^{\infty}(\bar{X}) .$$
If we take another local coframe $\left\{d \rho^{\prime}, \widetilde{\Theta}^{\prime}, \alpha^{\prime i}\right\}$ and its dual $\left\{N^{\prime}, T^{\prime}, Y_{i}^{\prime}\right\}$, then the transition function between $\left\{\rho N, \rho^{2} T, \rho Y_{i}\right\}$ and $\left\{\rho^{\prime} N^{\prime}, \rho^{\prime 2} T^{\prime}, \rho^{\prime} Y_{i}^{\prime}\right\}$ is smooth and nondegenerate up to $M$, so there exists a vector bundle ${ }^{\Theta} T \bar{X}$ over $\bar{X}$ for which $\left\{\rho N, \rho^{2} T, \rho Y_{i}\right\}$ gives a local frame. A $\Theta$-vector field is identified with a section of this bundle and we call ${ }^{\Theta} T \bar{X}$ the $\Theta$-tangent bundle. A fiber metric on ${ }^{\Theta} T \bar{X}$ is called a $\Theta$-metric. Since the restriction $\left.{ }^{\Theta} T \bar{X}\right|_{X}$ is canonically isomorphic to $T X$, a $\Theta$-metric defines a Riemannian metric on $X$. A local frame $\left\{\boldsymbol{Z}_{I}\right\}$ of ${ }^{\Theta} T \bar{X}$ is called a $\Theta$-frame. We also consider the dual ${ }^{\Theta} T^{*} \bar{X}$ of the $\Theta$-tangent bundle and various tensor bundles, whose sections are called $\Theta$-tensors. A $\Theta$-tensor is said to be $O\left(\rho^{m}\right)$ if each component in a $\Theta$-frame is $O\left(\rho^{m}\right)$. $\Theta$-vector fields are closed under the Lie bracket, and those which vanish at a fixed point $p \in M$ form an ideal. Thus the fiber ${ }^{\Theta} T_{p} \bar{X}$ becomes a Lie algebra, which we call the tangent algebra.

The product $M \times[0, \infty)_{\rho}$ has a canonical $\Theta$-structure, called the standard $\Theta$ -structure, which is defined by extending each contact form $\theta$ on $M$ to $\Theta \in \Gamma\left(M, T^{*} \bar{X}\right)$ with $\Theta(\partial / \partial \rho)=0$. Let $\theta$ be a contact form and $\left\{T, Z_{\alpha}, Z_{\bar{\alpha}}\right\}$ an admissible frame for $\mathbb{C} T M$. We extend $\left\{T, Z_{\alpha}, Z_{\bar{\alpha}}\right\}$ to $M \times[0, \infty)_{\rho}$ in the trivial way, and define a (complexified) $\Theta$-frame $\left\{\boldsymbol{Z}_{I}\right\}$ by
$$\boldsymbol{Z}_{\infty}=\rho \partial_{\rho}, \quad \boldsymbol{Z}_{0}=\rho^{2} T, \quad \boldsymbol{Z}_{\alpha}=\rho Z_{\alpha}, \quad \boldsymbol{Z}_{\bar{\alpha}}=\rho Z_{\bar{\alpha}},$$
where $\partial_{\rho}=\partial / \partial \rho$. A $\Theta$-metric $g$ on $M \times[0, \infty)_{\rho}$ is called a normal form $A C H$ metric if the components $g_{I J}=g\left(\boldsymbol{Z}_{I}, \boldsymbol{Z}_{J}\right)$ satisfy
$$\begin{gathered}
g_{\infty \infty}=4, \quad g_{\infty 0}=g_{\infty \alpha}=0, \quad g_{00}=1+O(\rho), \quad g_{0 \alpha}=O(\rho), \\
g_{\alpha \beta}=O(\rho), \quad g_{\alpha \bar{\beta}}=h_{\alpha \bar{\beta}}+O(\rho),
\end{gathered}$$
where $h_{\alpha \bar{\beta}}=h_{\theta}\left(Z_{\alpha}, Z_{\bar{\beta}}\right)$. On a general $\Theta$-manifold $(\bar{X},[\Theta])$, the ACH metric is defined as follows:

Definition 2.1. A $\Theta$-metric $g$ on $\bar{X}$ is called an ACH metric if for any contact form $\theta$ on $M$, there exist a neighborhood $U \subset \bar{X}$ of $M$ and a $\Theta$-diffeomorphism $\Phi_{\theta}: M \times[0, \infty)_{\rho} \rightarrow U$ such that $\Phi_{\theta}^{*} g$ is a normal form ACH metric.

We remark that there is an alternative definition of the ACH metric which involves only boundary value of $g$; see [19, Definition 4.6].

The germ of $\Phi_{\theta}$ along $M$ is unique, and we call $\rho \circ \Phi_{\theta}^{-1}$ the model defining function for $\theta$. We identify a neighborhood of $M$ in $\bar{X}$ with $M \times[0, \epsilon)_{\rho}$ through $\Phi_{\theta}$ and regard $\left\{\boldsymbol{Z}_{I}\right\}$ as a $\Theta$-frame on $\bar{X}$. The following proposition will be used in the proof of Lemma 4.1.

Proposition 2.2. The boundary values $\left.\boldsymbol{Z}_{\infty}\right|_{M},\left.\boldsymbol{Z}_{0}\right|_{M}$ are independent of $\theta$ and determined only by the ACH metric $g$.

Proof. By strict pseudoconvexity of $(H, J)$, the derived Lie algebras of the tangent algebra ${ }^{\ominus} T_{p} \bar{X}$ at a point $p \in M$ are given by
$$\begin{aligned}
& \mathcal{D}^{1}:=\left[{ }^{\Theta} T_{p} \bar{X},{ }^{\Theta} T_{p} \bar{X}\right]=\operatorname{span}\left\{\left(\boldsymbol{Z}_{0}\right)_{p},\left(\boldsymbol{Z}_{\alpha}\right)_{p},\left(\boldsymbol{Z}_{\bar{\alpha}}\right)_{p}\right\}, \\
& \mathcal{D}^{2}:=\left[\mathcal{D}^{1}, \mathcal{D}^{1}\right]=\operatorname{span}\left\{\left(\boldsymbol{Z}_{0}\right)_{p}\right\} .
\end{aligned}$$
Thus, $\left(\boldsymbol{Z}_{\infty}\right)_{p}$ and $\left(\boldsymbol{Z}_{0}\right)_{p}$ are oriented basis of $\left(\mathcal{D}^{1}\right)^{\perp}$ and $\mathcal{D}^{2}$ respectively. Since they are normalized by $\left|\left(\boldsymbol{Z}_{\infty}\right)_{p}\right|_{g}^{2}=4,\left|\left(\boldsymbol{Z}_{0}\right)_{p}\right|_{g}^{2}=1$, they are independent of $\theta$. □

Let $\theta, \widehat{\theta}=e^{\Upsilon} \theta$ be contact forms on $M$ and $\rho, \widehat{\rho}$ the corresponding model defining functions. Then there exists a positive function $f$ on $\bar{X}$ such that $\widehat{\rho}=f \rho$. Since the Reeb vector fields are related as $\widehat{T}=e^{-\Upsilon}\left(T-i h^{\alpha \bar{\gamma}} \Upsilon_{\bar{\gamma}} Z_{\alpha}+i h^{\gamma \bar{\alpha}} \Upsilon_{\gamma} Z_{\bar{\alpha}}\right)$, we have
$$\widehat{\boldsymbol{Z}}_{0}=\widehat{\rho}^{2} \widehat{T}=e^{-\Upsilon} f^{2} \boldsymbol{Z}_{0}+O(\rho)$$
as a $\Theta$-vector field, where we regard $\Upsilon$ as a function on a neighborhood of $M$. It follows from $\left.\widehat{\boldsymbol{Z}}_{0}\right|_{M}=\left.\boldsymbol{Z}_{0}\right|_{M}$ that $\left.f\right|_{M}=e^{\Upsilon / 2}$. Thus we have
$$\widehat{\rho}=e^{\Upsilon / 2} \rho+O\left(\rho^{2}\right) .$$
In particular, a contact form is recovered from the 1-jet of the corresponding model defining function along the boundary.
2.3. The Levi-Civita connection. Let $g$ be an ACH metric on a $\Theta$-manifold $(\bar{X},[\Theta])$ with boundary $M$. Here and after, we assume that $M$ is three dimensional. We lower and raise the indices of $\Theta$-tensors by $g_{I J}$ and its inverse $g^{I J}$. In order to describe the Levi-Civita connection of $g$, we introduce an extension of the Tanaka-Webster connection by following [19, 20]; we refer the reader to [19, §6.2] or [20, §4] for a more detailed exposition.

Let $\theta$ be a contact form on $M$. We identify a neighborhood of $M$ in $\bar{X}$ with $M \times[0, \epsilon)_{\rho}$ by the $\Theta$-diffeomorphism determined by $\theta$. We take an admissible frame $\left\{T, Z_{1}, Z_{\overline{1}}\right\}$ and define the extended Tanaka-Webster connection $\bar{\nabla}$ on $T \bar{X}$ by
$$\begin{gathered}
\bar{\nabla} \partial_{\rho}=0, \quad \bar{\nabla}_{\partial_{\rho}} T=\bar{\nabla}_{\partial_{\rho}} Z_{1}=0, \\
\bar{\nabla}_{T} Z_{1}=\nabla_{T}^{\mathrm{TW}} Z_{1}, \quad \bar{\nabla}_{Z_{1}} Z_{1}=\nabla_{Z_{1}}^{\mathrm{TW}} Z_{1}, \quad \bar{\nabla}_{Z_{\overline{1}}} Z_{1}=\nabla_{Z_{\mathrm{T}}}^{\mathrm{TW}} Z_{1},
\end{gathered}$$
where $\nabla^{\mathrm{TW}}$ denotes the Tanaka-Webster connection associated with $\theta$. Then, $\bar{\nabla}$ is a $\Theta$-connection in the sense that if $V, W$ are $\Theta$-vector fields, so is the covariant derivative $\bar{\nabla}_{V} W$. We take the $\Theta$-frame $\left\{\boldsymbol{Z}_{I}\right\}=\left\{\rho \partial_{\rho}, \rho^{2} T, \rho Z_{1}, \rho Z_{\overline{1}}\right\}$ and define the Christoffel symbols $\bar{\Gamma}_{I J}{ }^{K}$ by $\bar{\nabla}_{\boldsymbol{Z}_{I}} \boldsymbol{Z}_{J}=\bar{\Gamma}_{I J}{ }^{K} \boldsymbol{Z}_{K}$. A simple calculation shows that
$$\begin{array}{lll}
\bar{\Gamma}_{\infty \infty}^{\infty}=1, & \bar{\Gamma}_{\infty 0}^{0}=2, & \bar{\Gamma}_{\infty 1}{ }^{1}=1, \\
\bar{\Gamma}_{01}{ }^{1}=\rho^{2} \Gamma_{01}{ }^{1}, & \bar{\Gamma}_{11}{ }^{1}=\rho \Gamma_{11}{ }^{1}, & \bar{\Gamma}_{\overline{1} 1}{ }^{1}=\rho \Gamma_{\overline{1} 1}{ }^{1},
\end{array}$$
where $\Gamma_{i j}{ }^{k}$ are the Christoffel symbols of $\nabla^{\mathrm{TW}}$ with respect to $\left\{T, Z_{1}, Z_{\overline{1}}\right\}$; the components which cannot be obtained by taking complex conjugates of (2.6) are 0. It follows from (2.6) that the components of the covariant derivative of a $\Theta$-tensor $S_{I_{1} \cdots I_{p}}{ }^{J_{1} \cdots J_{q}}$ are computed as
$$\begin{aligned}
& \bar{\nabla}_{\infty} S_{I_{1} \cdots I_{p}}{ }^{J_{1} \cdots J_{q}}=\left(\rho \partial_{\rho}-\#\left(I_{1} \cdots I_{p}\right)+\#\left(J_{1} \cdots J_{q}\right)\right) S_{I_{1} \cdots I_{p}}{ }^{J_{1} \cdots J_{q}}, \\
& \bar{\nabla}_{0} S_{I_{1} \cdots I_{p}}{ }^{J_{1} \cdots J_{q}}=\rho^{2} \nabla_{0}^{\mathrm{TW}} S_{I_{1} \cdots I_{p}}{ }^{J_{1} \cdots J_{q}}, \\
& \bar{\nabla}_{1} S_{I_{1} \cdots I_{p}}{ }^{J_{1} \cdots J_{q}}=\rho \nabla_{1}^{\mathrm{TW}} S_{I_{1} \cdots I_{p}}{ }^{J_{1} \cdots J_{q}},
\end{aligned}$$
where $\#\left(I_{1} \cdots I_{p}\right):=p+$ (the number of $0 s$ ) and we regard $S$ as a tensor on $\mathbb{C} H$ when we apply $\nabla^{\mathrm{TW}}$ to it ([19, Lemma 6.2], [20, (4.9)]).

The torsion tensor $\bar{T}_{I J}{ }^{K}$ and the curvature tensor $\bar{R}_{I}{ }^{J}{ }_{K L}$ of $\bar{\nabla}$ are defined by
$$\begin{gathered}
\left(\bar{\nabla}_{V} W-\bar{\nabla}_{W} V-[V, W]\right)^{K}=\bar{T}_{I J}{ }^{K} V^{I} W^{J}, \\
\left(\bar{\nabla}_{V} \bar{\nabla}_{W} Y-\bar{\nabla}_{W} \bar{\nabla}_{V} Y-\bar{\nabla}_{[V, W]} Y\right)^{J}=\bar{R}_{I}{ }^{J}{ }_{K L} Y^{I} V^{K} W^{L}
\end{gathered}$$
respectively. In the $\Theta$-frame $\left\{\boldsymbol{Z}_{I}\right\}$, the components are given by
$$\bar{T}_{1 \overline{1}}^{0}=i h_{1 \overline{1}}, \quad \bar{T}_{01} \overline{1}=\rho^{2} A_{1}^{\overline{1}},$$
and
$$\bar{R}_{1}{ }^{1}{ }_{1 \overline{1}}=\rho^{2} \mathrm{Scal}^{\mathrm{TW}} h_{1 \overline{1}}, \quad \bar{R}_{1}{ }^{1}{ }_{01}=-\rho^{3} A_{11}{ }^{1}, \quad \bar{R}_{1}{ }^{1}{ }_{0 \overline{1}}=\rho^{3} A^{1}{ }_{\overline{1}, 1},$$
where Scal ${ }^{\text {TW }}$ denotes the Tanaka-Webster scalar curvature, and we have removed the CR weights in the Tanaka-Webster tensors by the CR scale corresponding to $\theta$. The components which cannot be obtained from (2.8), (2.9) by the symmetries of $\bar{T}, \bar{R}$ or by taking the complex conjugates are all 0 . The nonzero components of the Ricci tensor $\bar{R}_{I J}=\bar{R}_{I}{ }^{K}{ }_{K J}$ are given by
$$\bar{R}_{1 \overline{1}}=\rho^{2} \operatorname{Scal}^{\mathrm{TW}} h_{1 \overline{1}}, \quad \bar{R}_{10}=\rho^{2} A_{11},{ }^{1} .$$

Let ∇ be the Levi-Civita connection of $g$, which is also a $\Theta$-connection ([19, Proposition 4.4]). We define the difference $\Theta$-tensor $D_{I J}{ }^{K}$ by
$$\nabla_{I} V^{K}=\bar{\nabla}_{I} V^{K}+D_{I J}{ }^{K} V^{J} .$$
Since ∇ is torsion-free, we have
$$D_{I J}{ }^{K}=D_{J I}{ }^{K}+\bar{T}_{J I}{ }^{K} .$$
Using this relation and the fact $\nabla g=0$, we obtain
$$2 D_{I J K}=\bar{\nabla}_{I} g_{J K}+\bar{\nabla}_{J} g_{K I}-\bar{\nabla}_{K} g_{I J}-\bar{T}_{I J K}+\bar{T}_{J K I}-\bar{T}_{K I J} .$$
We will compute $D_{I J}{ }^{K}$ by these formulas. Since the components $g_{I J}$ satisfy (2.4), $g$ is described by $\rho$-dependent tensors $\varphi_{i j}$ on $M$ defined by
$$g_{00}=1+\varphi_{00}, \quad g_{01}=\varphi_{01}, \quad g_{11}=\varphi_{11}, \quad g_{1 \overline{1}}=h_{1 \overline{1}}+\varphi_{1 \overline{1}} .$$
In the construction of a formal solution to the self-dual Einstein equation, we need to examine the effect of a perturbation
$$\varphi_{i j} \longmapsto \varphi_{i j}+\psi_{i j}, \quad \psi_{i j}=O\left(\rho^{m}\right)$$
on the curvature quantities of $g$. Then it is useful in the computation to ignore irrelevant terms on which the perturbation causes only changes in higher orders. Such terms are of the form
$$O(\rho) \cdot\left(\rho \partial_{\rho}\right)^{l} \mathcal{D} \varphi_{i j},$$
where $\mathcal{D}$ is a $\rho$-dependent differential operator on $M$. These are called negligible terms. In fact, a negligible term changes by $O\left(\rho^{m+1}\right)$ under the perturbation (2.12). Thus, it suffices to compute $D_{I J}{ }^{K}$ modulo negligible terms. For simplicity, we assume that the admissible frame $\left\{Z_{1}\right\}$ is unitary with respect to the Levi form; namely $h_{1 \overline{1}}=1$. Noting that $\varphi_{i j}=O(\rho)$, we have
$$\begin{gathered}
g^{\infty \infty}=\frac{1}{4}, \quad g^{\infty 0}=g^{\infty 1}=0, \quad g^{00} \equiv 1-\varphi_{00}, \\
g^{1 \overline{1}} \equiv-\varphi_{1 \overline{1}}, \quad g^{11} \equiv-\varphi_{\overline{11}}
\end{gathered}$$
modulo negligible terms. By computing with (2.7), (2.8), (2.10), (2.11), (2.14) we obtain the following result:

Lemma 2.3 ([19, Lemma 6.4], [20, Table 1]). Let $\left\{T, Z_{1}, Z_{\overline{1}}\right\}$ be a unitary admissible frame and $\left\{\boldsymbol{Z}_{I}\right\}=\left\{\rho \partial_{\rho}, \rho^{2} T, \rho Z_{1}, \rho Z_{\overline{1}}\right\}$ the associated $\Theta$-frame. Then, modulo negligible terms, the components $D_{I J}{ }^{K}$ are given by
$$\begin{array}{lll}
D_{\infty} \infty^{\infty} \equiv-1, & D_{\infty 0^{\infty}} \equiv D_{\infty 1}{ }^{\infty} \equiv 0, & \\
D_{00}{ }^{\infty} \equiv \frac{1}{2}-\frac{1}{8}\left(\rho \partial_{\rho}-4\right) \varphi_{00}, & D_{01}^{\infty} \equiv-\frac{1}{8}\left(\rho \partial_{\rho}-3\right) \varphi_{01}, & \\
D_{1 \overline{1}}^{\infty} \equiv \frac{1}{4}-\frac{1}{8}\left(\rho \partial_{\rho}-2\right) \varphi_{1 \overline{1}}, & D_{11^{\infty}} \equiv-\frac{1}{8}\left(\rho \partial_{\rho}-2\right) \varphi_{11}, & \\
D_{\infty} \infty^{1} \equiv D_{00}{ }^{1} \equiv D_{\overline{11}}{ }^{1} \equiv 0, & D_{\infty \overline{1}^{1}} \equiv \frac{1}{2} \rho \partial_{\rho} \varphi_{\overline{11}}, & D_{0 \overline{1}}{ }^{1} \equiv \frac{i}{2} \varphi_{\overline{11}}, \\
D_{\infty 0^{1}} \equiv \frac{1}{2}\left(\rho \partial_{\rho}+1\right) \varphi_{0 \overline{1}}, & D_{01}{ }^{1} \equiv \frac{i}{2}\left(1+\varphi_{00}-\varphi_{1 \overline{1}}\right), & D_{1 \overline{1}^{1}} \equiv \frac{i}{2} \varphi_{0 \overline{1}}, \\
D_{\infty 1^{1}} \equiv-1+\frac{1}{2} \rho \partial_{\rho} \varphi_{1 \overline{1}}, & D_{\overline{1} 0}{ }^{1} \equiv \frac{i}{2} \varphi_{\overline{11}}+\rho^{2} A_{\overline{11}}, & D_{11}{ }^{1} \equiv i \varphi_{01}, \\
D_{\infty \infty^{0}} \equiv D_{00}{ }^{0} \equiv 0, & D_{1^{0}}{ }^{0} \equiv-\frac{i}{2}, & D_{11}{ }^{0} \equiv-\rho^{2} A_{11}, \\
D_{\infty 0}{ }^{0} \equiv-2+\frac{1}{2} \rho \partial_{\rho} \varphi_{00}, & D_{\infty 1}{ }^{0} \equiv \frac{1}{2}\left(\rho \partial_{\rho}-1\right) \varphi_{01}, & D_{01}{ }^{0} \equiv-\frac{i}{2} \varphi_{01} .
\end{array}$$
The components which are not displayed are obtained by taking the complex conjugates or using the relation (2.10).

Remark 2.4. We have modified a typographical error in [19, Table 6.2], [20, Table 1]; the value of $D_{01}{ }^{1}$ above differs by $-\frac{i}{2} \varphi_{1 \overline{1}}$ from that in [19, 20]. (Note that $D_{I J}{ }^{K}$ is denoted by $D^{K}{ }_{I J}$ in [19] and by $D_{J}{ }^{K}{ }_{I}$ in [20].) The correct value is used in the other computations in [19, 20].

\section*{3. The self-dual Einstein equation}

Let $g$ be an ACH metric on a four dimensional $\Theta$-manifold $(\bar{X},[\Theta])$ which has a strictly pseudoconvex CR manifold $M$ as its boundary. We fix a contact form $\theta$ on $M$ and identify a neighborhood of $M$ as $M \times[0, \epsilon)_{\rho}$, where $\rho$ is the model defining function for $\theta$. We take a unitary admissible frame $\left\{T, Z_{1}, Z_{\overline{1}}\right\}$ on $M$ and work in the associated $\Theta$-frame $\left\{\boldsymbol{Z}_{I}\right\}=\left\{\rho \partial_{\rho}, \rho^{2} T, \rho Z_{1}, \rho Z_{\overline{1}}\right\}$.
3.1. The Einstein equation. We will recall from [19, 20] the computation of the Einstein tensor modulo negligible terms which is needed in the construction of the Einstein ACH metric. We set
$$E_{I J}:=\operatorname{Ric}_{I J}+\frac{3}{2} g_{I J} .$$
In terms of the extended Tanaka-Webster connection and the difference $\Theta$-tensor, the curvature tensor of $g$ is expressed as
$$\begin{aligned}
R_{I}{ }^{J}{ }_{K L}= & \bar{R}_{I}{ }^{J}{ }_{K L}+\bar{\nabla}_{K} D_{L I}{ }^{J}-\bar{\nabla}_{L} D_{K I}{ }^{J} \\
& +D_{K M}{ }^{J} D_{L I}{ }^{M}-D_{L M}{ }^{J} D_{K I}{ }^{M}+\bar{T}_{K L}{ }^{M} D_{M I}{ }^{J} .
\end{aligned}$$
Hence, the Ricci tensor is given by
$$\begin{aligned}
\operatorname{Ric}_{I J}= & R_{J}{ }^{K}{ }_{K I} \\
= & \bar{R}_{J I}+\bar{\nabla}_{K} D_{I J}{ }^{K}-\bar{\nabla}_{I} D_{K J}{ }^{K} \\
& +D_{K M}{ }^{K} D_{I J}{ }^{M}-D_{I M}{ }^{K} D_{K J}{ }^{M}+\bar{T}_{K I}{ }^{M} D_{M J}{ }^{K} \\
= & \bar{R}_{J I}+\bar{\nabla}_{K} D_{I J}{ }^{K}-\bar{\nabla}_{I} D_{K J}{ }^{K}+D_{K M}{ }^{K} D_{I J}{ }^{M}-D_{M I}{ }^{K} D_{K J}{ }^{M} .
\end{aligned}$$
In the last equality, we have used (2.10). With this formula and Lemma 2.3, we can compute $E_{I J}$ modulo negligible terms:

Lemma 3.1 ([19, Lemma 6.5], [20, Lemma 4.2]). Let $\left\{T, Z_{1}, Z_{\overline{1}}\right\}$ be a unitary admissible frame and $\left\{\boldsymbol{Z}_{I}\right\}=\left\{\rho \partial_{\rho}, \rho^{2} T, \rho Z_{1}, \rho Z_{\overline{1}}\right\}$ the associated $\Theta$-frame. Then, modulo negligible terms, the components of the Einstein tensor $E_{I J}$ are given by
$$\begin{aligned}
& E_{\infty \infty} \equiv-\frac{1}{2} \rho \partial_{\rho}\left(\rho \partial_{\rho}-4\right) \varphi_{00}-\rho \partial_{\rho}\left(\rho \partial_{\rho}-2\right) \varphi_{1 \overline{1}}, \\
& E_{\infty 0} \equiv 0, \\
& E_{\infty 1} \equiv-\frac{i}{2}\left(\rho \partial_{\rho}+1\right) \varphi_{01}, \\
& E_{00} \equiv-2 \rho^{4}|A|^{2}-\frac{1}{8}\left(\left(\rho \partial_{\rho}\right)^{2}-6 \rho \partial_{\rho}-4\right) \varphi_{00}+\frac{1}{2}\left(\rho \partial_{\rho}-2\right) \varphi_{1 \overline{1}}, \\
& E_{01} \equiv \rho^{3} A_{11},^{1}-\frac{1}{8}\left(\rho \partial_{\rho}+1\right)\left(\rho \partial_{\rho}-5\right) \varphi_{01}, \\
& E_{1 \overline{1}} \equiv \rho^{2} \mathrm{Scal}^{\mathrm{TW}}-\frac{1}{8}\left(\left(\rho \partial_{\rho}\right)^{2}-6 \rho \partial_{\rho}-8\right) \varphi_{1 \overline{1}}+\frac{1}{8}\left(\rho \partial_{\rho}-4\right) \varphi_{00}, \\
& E_{11} \equiv i \rho^{2} A_{11}-\rho^{4} A_{11,0}-\frac{1}{8} \rho \partial_{\rho}\left(\rho \partial_{\rho}-4\right) \varphi_{11} .
\end{aligned}$$
The components which are not displayed are obtained by the symmetry or by taking the complex conjugates.

Remark 3.2. We have corrected the value of $E_{00}$ in [19, Lemma 6.5], [20, Lemma 4.2], where the term $-2 \rho^{4}|A|^{2}$ is missed, though this modification has no significant effect on the construction of Einstein ACH metric.
3.2. The self-dual equation. Let $\left\{\boldsymbol{\theta}^{I}\right\}$ be the dual $\Theta$-coframe of $\left\{\boldsymbol{Z}_{I}\right\}$. We take the orientation of $\bar{X}$ such that $\theta \wedge d \theta \wedge d \rho>0$, and define a skew symmetric $\Theta$-tensor $\varepsilon_{I J K L}$ by
$$v o l_{g}=\frac{1}{4!} \varepsilon_{I J K L} \boldsymbol{\theta}^{I} \wedge \boldsymbol{\theta}^{J} \wedge \boldsymbol{\theta}^{K} \wedge \boldsymbol{\theta}^{L},$$
where $\operatorname{vol}_{g}$ is the volume form of $g$. Since $\operatorname{det}\left(g_{I J}\right) \equiv-4\left(1+\varphi_{00}+2 \varphi_{1 \overline{1}}\right)$ modulo negligible terms, we have
$$\begin{aligned}
v o l_{g} & =\left|\operatorname{det}\left(g_{I J}\right)\right|^{1 / 2} i \boldsymbol{\theta}^{0} \wedge \boldsymbol{\theta}^{1} \wedge \boldsymbol{\theta}^{\overline{1}} \wedge \boldsymbol{\theta}^{\infty} \\
& \equiv\left(2 i+i \varphi_{00}+2 i \varphi_{1 \overline{1}}\right) \boldsymbol{\theta}^{0} \wedge \boldsymbol{\theta}^{1} \wedge \boldsymbol{\theta}^{\overline{1}} \wedge \boldsymbol{\theta}^{\infty},
\end{aligned}$$
and hence
$$\varepsilon_{01 \overline{1} \infty} \equiv 2 i+i \varphi_{00}+2 i \varphi_{1 \overline{1}} .$$
Let $P_{I J}=\frac{1}{2} \operatorname{Ric}_{I J}-\frac{1}{12} \operatorname{Scal} g_{I J}$ be the Schouten tensor, and let
$$W_{I J K L}=R_{I J K L}+g_{I K} P_{J L}-g_{J K} P_{I L}+g_{J L} P_{I K}-g_{I L} P_{J K}$$
be the Weyl curvature. Since $\bar{X}$ is four dimensional, we can define the anti self-dual part of the Weyl curvature, which is given by
$$W_{I J K L}^{-}=\frac{1}{2}\left(W_{I J K L}-\frac{1}{2} \varepsilon_{K L}{ }^{P Q} W_{I J P Q}\right) .$$
Note that $W_{I J K L}^{-}$has the same symmetry as the Weyl curvature and satisfies
$$\frac{1}{2} \varepsilon_{K L}{ }^{P Q} W_{I J P Q}^{-}=-W_{I J K L}^{-} .$$
Thus, by (2.14), (3.3), we have
$$\begin{aligned}
& W_{\infty 0 \infty 0}^{-} \equiv-W_{\infty 1 \infty \overline{1}}^{-}-W_{\infty \overline{1} \infty 1}^{-}=-2 W_{\infty 1 \infty \overline{1}}^{-}, \\
& W_{I J 01}^{-}=-\varepsilon_{01 \overline{1} \infty} W_{I J}^{-\overline{1} \infty} \equiv-\frac{i}{2} W_{I J 1 \infty}^{-}, \\
& W_{I J 1 \overline{1}}^{-}=-\varepsilon_{1 \overline{1} 0 \infty} W_{I J}^{-} 0 \infty \equiv-\frac{i}{2} W_{I J 0 \infty}^{-}
\end{aligned}$$
modulo $O(\rho) \cdot W_{I J K L}^{-}$. Since $W_{I J K L}^{-}=W_{K L I J}^{-}$, we also have
$$\begin{aligned}
W_{01 K L}^{-} & \equiv-\frac{i}{2} W_{1 \infty K L}^{-}, \\
W_{1 \overline{1} K L}^{-} & \equiv-\frac{i}{2} W_{0 \infty K L}^{-}
\end{aligned}$$
modulo $O(\rho) \cdot W_{I J K L}^{-}$. As a consequence, we have the following lemma:
Lemma 3.3. Let $m$ be a positive integer. If $W_{\infty 1 \infty 1}^{-}, W_{\infty 0 \infty 1}^{-}, W_{\infty 0 \infty 0}^{-}=O\left(\rho^{m}\right)$, then $W_{I J K L}^{-}=O\left(\rho^{m}\right)$.

Thus, in order to solve the self-dual equation $W_{I J K L}^{-}=O\left(\rho^{\infty}\right)$, we only have to deal with the three components indicated above.

Next, we consider the Bianchi identity which relates the self-dual equation to the Einstein equation. Let $C_{I J K}:=\nabla_{K} P_{I J}-\nabla_{J} P_{I K}$ be the Cotton tensor of $g$ and define the anti self-dual part $C_{I J K}^{-}$by
$$C_{I J K}^{-}=\frac{1}{2}\left(C_{I J K}-\frac{1}{2} \varepsilon_{J K}{ }^{P Q} C_{I P Q}\right) .$$
Then, since $\nabla_{I} \varepsilon_{J K L M}=0$, the Bianchi identity $\nabla^{I} W_{I J K L}=C_{J K L}$ yields
$$\nabla^{I} W_{I J K L}^{-}=C_{J K L}^{-} .$$
If $g$ satisfies $E_{I J}=O\left(\rho^{m}\right)$ for some $m \geq 1$, then we have $P_{I J}=-\frac{1}{4} g_{I J}+O\left(\rho^{m}\right)$ and hence $C_{I J K}^{-}=O\left(\rho^{m}\right)$ since the covariant differentiation does not decrease the vanishing order of a $\Theta$-tensor. Therefore, it holds that
$$E_{I J}=O\left(\rho^{m}\right) \Longrightarrow \nabla^{I} W_{I J K L}^{-}=O\left(\rho^{m}\right) .$$
To derive the consequence of the latter equation, we will compute
$$\begin{aligned}
\nabla^{I} W_{I J K L}^{-}= & \bar{\nabla}^{I} W_{I J K L}^{-}-W_{M J K L}^{-} D^{I}{ }_{I}{ }^{M}-W_{I M K L}^{-} D^{I}{ }_{J}{ }^{M} \\
& -W_{I J M L}^{-} D^{I}{ }_{K}{ }^{M}-W_{I J K M}^{-} D^{I}{ }_{L}{ }^{M}
\end{aligned}$$
modulo $O(\rho) \cdot \mathcal{D} W_{I J K L}^{-}$, where $\mathcal{D}$ is a $\rho$-dependent differential operator on $M$. By computations similar to (3.4), (3.5), (3.6), we have
$$\begin{aligned}
\nabla^{I} W_{I 0 \infty 0}^{-} & \equiv-2 \nabla^{I} W_{I 1 \infty \overline{1}}^{-}, \\
\nabla^{I} W_{I J 01}^{-} & \equiv-\frac{i}{2} \nabla^{I} W_{I J 1 \infty}^{-}, \\
\nabla^{I} W_{I J 1 \overline{1}}^{-} & \equiv-\frac{i}{2} \nabla^{I} W_{I J 0 \infty}^{-}
\end{aligned}$$
modulo $O(\rho) \cdot \mathcal{D} W_{I J K L}^{-}$. By (3.9) and (3.10), it suffices to consider the cases where $K=\infty$. Then, taking complex conjugates we may assume that $L=0,1$, and the case $(J, K, L)=(\overline{1}, \infty, 0)$ is reduced to the case $(J, K, L)=(1, \infty, 0)$. Moreover, by (3.8) the case $(J, K, L)=(\overline{1}, \infty, 1)$ is reduced to the case $(J, K, L)=(0, \infty, 0)$. Thus, it suffices to compute (3.7) for
$$(J, K, L)=(1, \infty, 1),(0, \infty, 0),(0, \infty, 1),(1, \infty, 0),(\infty, \infty, 1),(\infty, \infty, 0) .$$
By (2.7), we have
$$\begin{aligned}
\bar{\nabla}^{I} W_{I J K L}^{-} & =\bar{\nabla}^{\infty} W_{\infty J K L}^{-}+\bar{\nabla}^{1} W_{1 J K L}^{-}+\bar{\nabla}^{\overline{1}} W_{\overline{1} J K L}^{-}+\bar{\nabla}^{0} W_{0 J K L}^{-} \\
& \equiv \frac{1}{4}\left(\rho \partial_{\rho}-\#(\infty J K L)\right) W_{\infty J K L}^{-} .
\end{aligned}$$
The other terms in the right-hand side of (3.7) can be computed by Lemma 2.3. The final results are:
$$\begin{array}{ll}
\nabla^{I} W_{I 1 \infty 1}^{-} \equiv \frac{1}{4}\left(\rho \partial_{\rho}-4\right) W_{\infty 1 \infty 1}^{-}, & \nabla^{I} W_{I 0 \infty 0}^{-} \equiv \frac{1}{4}\left(\rho \partial_{\rho}-6\right) W_{\infty 0 \infty 0}^{-}, \\
\nabla^{I} W_{I 0 \infty 1}^{-} \equiv \frac{1}{4}\left(\rho \partial_{\rho}-6\right) W_{\infty 0 \infty 1}^{-}, & \nabla^{I} W_{I 1 \infty 0}^{-} \equiv \frac{1}{4}\left(\rho \partial_{\rho}-5\right) W_{\infty 1 \infty 0}^{-}, \\
\nabla^{I} W_{I \infty \infty 1}^{-} \equiv \frac{i}{2} W_{\infty 0 \infty 1}^{-}, & \nabla^{I} W_{I \infty \infty 0}^{-} \equiv 0 .
\end{array}$$

Consequently, by an inductive argument, we have the following implication:
$$E_{I J}=O\left(\rho^{4}\right) \Longrightarrow W_{I J K L}^{-}=O\left(\rho^{4}\right) .$$
Moreover, if $E_{I J}=O\left(\rho^{5}\right)$ then $W_{\infty 0 \infty 0}^{-}, W_{\infty 0 \infty 1}^{-}=O\left(\rho^{5}\right)$, but we cannot conclude that $W_{\infty 1 \infty 1}^{-}=O\left(\rho^{5}\right)$. Thus, we may use the equation $W_{\infty 1 \infty 1}^{-}=O\left(\rho^{5}\right)$ as a normalization on the metric which is independent of the Einstein equation. We will also use a normalization on the $\rho^{6}$-term in $W_{\infty 0^{\infty} 0}^{-}$whose vanishing is not imposed by the Einstein equation. To make sure that such normalizations in fact work, we must calculate the variations of $W_{\infty 1 \infty 1}^{-}$and $W_{\infty 0 \infty 0}^{-}$under the perturbation (2.12).

First, we calculate the relevant components of the curvature tensor modulo negligible terms. Since the curvature tensor is given by (2.9) and $R_{I J \infty K}=-4 R_{K}{ }^{\infty}{ }_{I J}$, we obtain the following result by a straightforward computation using (2.7) and Lemma 2.3:
$$\begin{array}{ll}
R_{\infty 0 \infty 0} \equiv 4+\frac{1}{2}\left(\left(\rho \partial_{\rho}\right)^{2}-4 \rho \partial_{\rho}+8\right) \varphi_{00}, & R_{01 \infty 0} \equiv \frac{i}{4}\left(\rho \partial_{\rho}+1\right) \varphi_{01}, \\
R_{\infty 1 \infty 1} \equiv \frac{1}{2}\left(\left(\rho \partial_{\rho}\right)^{2}-2 \rho \partial_{\rho}+2\right) \varphi_{11}, & R_{01 \infty 1} \equiv \rho^{2} A_{11}-\frac{i}{4} \rho \partial_{\rho} \varphi_{11}, \\
R_{0 \overline{1} \infty 1} \equiv-\frac{i}{2}+\frac{i}{4}\left(\rho \partial_{\rho}-2\right) \varphi_{00}-\frac{i}{4} \rho \partial_{\rho} \varphi_{1 \overline{1}}, & R_{1 \overline{1} \infty 1} \equiv \frac{3 i}{4}\left(\rho \partial_{\rho}-1\right) \varphi_{01}, \\
R_{1 \overline{1} \infty 0} \equiv-i+\frac{i}{2}\left(\rho \partial_{\rho}-2\right) \varphi_{00}-\frac{i}{2} \rho \partial_{\rho} \varphi_{1 \overline{1}} . &
\end{array}$$
These equations enable us to compute the variations of the curvature components under the perturbation (2.12), which we denote by putting ' $\delta$ ' to each component.

For example, by the first equation in (3.12), we have
$$\delta R_{\infty 0 \infty 0}=\frac{1}{2}\left(m^{2}-4 m+8\right) \psi_{00}+O\left(\rho^{m+1}\right) .$$
Next, we calculate the variation of the Schouten tensor
$$P_{I J}=\frac{1}{2} E_{I J}-\frac{1}{12}\left(E_{K}^{K}+3\right) g_{I J} .$$
Since $E_{I J}=O(\rho)$ by Lemma 3.1, we have
$$\delta P_{I J}=\frac{1}{2} \delta E_{I J}-\frac{1}{12} g^{K L}\left(\delta E_{K L}\right) g_{I J}-\frac{1}{4} \delta g_{I J}+O\left(\rho^{m+1}\right),$$
which yields
$$\begin{aligned}
& \delta P_{\infty \infty}=-\frac{1}{6}\left(m^{2}-3 m-1\right) \psi_{00}-\frac{1}{6}\left(2 m^{2}-m+2\right) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right), \\
& \delta P_{\infty 0}=O\left(\rho^{m+1}\right), \\
& \delta P_{\infty 1}=-\frac{i}{4}(m+1) \psi_{01}+O\left(\rho^{m+1}\right), \\
& \delta P_{00}=-\frac{1}{24}\left(m^{2}-6 m-1\right) \psi_{00}+\frac{1}{24}\left(m^{2}+m-14\right) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right), \\
& \delta P_{01}=-\frac{1}{16}\left(m^{2}-4 m-1\right) \psi_{01}+O\left(\rho^{m+1}\right), \\
& \delta P_{1 \overline{1}}=\frac{1}{48}\left(m^{2}-3 m-10\right) \psi_{00}-\frac{1}{48}\left(m^{2}-8 m-8\right) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right), \\
& \delta P_{11}=-\frac{1}{16}\left(m^{2}-4 m+4\right) \psi_{11}+O\left(\rho^{m+1}\right) .
\end{aligned}$$
From (2.14), (3.12), and (3.13), we have
$$\begin{aligned}
& W_{\infty 1}{ }^{0 \overline{1}}=O(\rho), \quad W_{\infty 0}{ }^{\overline{1} 1}=-i+O(\rho), \\
& \delta W_{\infty 1}{ }^{0 \overline{1}}=-\frac{i}{4}(m-2) \psi_{11}+O\left(\rho^{m+1}\right), \\
& \delta W_{\infty 0}{ }^{\overline{1} 1}=\frac{i}{2}(m-2) \psi_{00}-\frac{i}{2}(m-4) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right), \\
& \delta W_{\infty 1 \infty 1}=\frac{1}{4}\left(m^{2}-4\right) \psi_{11}+O\left(\rho^{m+1}\right), \\
& \delta W_{\infty 0 \infty 0}=\frac{1}{6}\left(m^{2}-3 m+20\right) \psi_{00}-\frac{1}{6}\left(m^{2}-2 m+16\right) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right) .
\end{aligned}$$
Finally, by (3.3) and (3.14), we obtain
$$\begin{aligned}
\delta W_{\infty 1 \infty 1}^{-} & =\frac{1}{2}\left(\delta W_{\infty 1 \infty 1}-\delta \varepsilon_{\infty 10 \overline{1}} \cdot W_{\infty 1}{ }^{0 \overline{1}}-\varepsilon_{\infty 10 \overline{1}} \cdot \delta W_{\infty 1}{ }^{0 \overline{1}}\right)+O\left(\rho^{m+1}\right) \\
& =\frac{1}{8}\left(m^{2}-2 m\right) \psi_{11}+O\left(\rho^{m+1}\right), \\
\delta W_{\infty 0 \infty 0}^{-} & =\frac{1}{2}\left(\delta W_{\infty 0 \infty 0}-\delta \varepsilon_{\infty 0 \overline{1} 1} \cdot W_{\infty 0}{ }^{\overline{1} 1}-\varepsilon_{\infty 0 \overline{1} 1} \cdot \delta W_{\infty 0}{ }^{\overline{1} 1}\right)+O\left(\rho^{m+1}\right) \\
& =\frac{1}{12}\left(m^{2}+3 m+2\right) \psi_{00}-\frac{1}{12}\left(m^{2}+4 m+4\right) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right) .
\end{aligned}$$
3.3. Bianchi identities. Since the Einstein equation is an overdetermined system, we need some relations which are satisfied by the components of the Einstein tensor in order to construct a formal solution to the Einstein equation. Some of them are given by the Bianchi identity $g^{I J} \nabla_{K} E_{I J}=2 g^{I J} \nabla_{I} E_{J K}$ :

Lemma 3.4 ([19, Lemma 6.6], [20, Lemma 6.1]). Suppose $g$ satisfies $E_{I J}=O\left(\rho^{m}\right)$ for an integer $m \geq 1$. Then, we have
$$\begin{aligned}
(m-8) E_{\infty \infty}-4(m-4) E_{00}-8(m-2) E_{1 \overline{1}} & =O\left(\rho^{m+1}\right), \\
(m-6) E_{\infty 0} & =O\left(\rho^{m+1}\right), \\
(m-5) E_{\infty 1}-4 i E_{01} & =O\left(\rho^{m+1}\right) .
\end{aligned}$$

We will also use some equations obtained from the Bianchi identity $\nabla^{I} W_{I J K L}^{-}=$ $C_{J K L}^{-}$in the construction of $g$. Since the Cotton tensor is given by
$$C_{I J K}=\frac{1}{2}\left(\nabla_{K} E_{I J}-\nabla_{J} E_{I K}\right)-\frac{1}{12}\left(\left(\nabla_{K} E_{L}{ }^{L}\right) g_{I J}-\left(\nabla_{J} E_{L}{ }^{L}\right) g_{I K}\right),$$
we can compute the components $C_{I J K}^{-}$in terms of $E_{I J}$ by using (2.7), (2.14), (3.3), and Lemma 2.3. As a result, we have the following lemma:

Lemma 3.5. Suppose $g$ satisfies $E_{I J}=O\left(\rho^{m}\right)$ for an integer $m \geq 1$. Then, we have
$$\begin{aligned}
C_{1 \infty 1}^{-} & =-\frac{1}{4}(m-2) E_{11}+O\left(\rho^{m+1}\right) \\
C_{0 \infty 0}^{-} & =-\frac{5}{24} m E_{00}+\frac{1}{96}(m-12) E_{\infty \infty}+\frac{1}{12}(m+6) E_{1 \overline{1}}+O\left(\rho^{m+1}\right), \\
C_{\infty \infty 0}^{-} & =-\frac{1}{4}(m-2) E_{\infty 0}+O\left(\rho^{m+1}\right) .
\end{aligned}$$

\section*{4. Construction of the metric}
4.1. Formal solution to the self-dual Einstein equation. Let $M$ be a three dimensional strictly pseudoconvex CR manifold. We fix a contact form $\theta$ and construct a one parameter family of ACH metrics $g^{\lambda}$ on $\bar{X}=M \times[0, \infty)_{\rho}$ which are in normal form with respect to $\theta$ and satisfy the Einstein equation to infinite order. The parameter $\lambda \in \mathbb{R}$ is involved in the normalization on the $\rho^{6}$-term in $g^{\lambda}$, and if $\lambda=0$ the metric is self-dual to infinite order. As in the previous section, we take the $\Theta$-frame $\left\{\boldsymbol{Z}_{I}\right\}=\left\{\rho \partial_{\rho}, \rho^{2} T, \rho Z_{1}, \rho Z_{\overline{1}}\right\}$ associated with a unitary admissible frame $\left\{T, Z_{1}, Z_{\overline{1}}\right\}$ on $M$. We suppress the superscript $\lambda$ in the following.

First we show a lemma which assures that our normalization condition is independent of the choice of $\theta$.
Lemma 4.1. Suppose that an ACH metric $g$ on $\bar{X}$ satisfies $W_{I J K L}^{-}=O\left(\rho^{6}\right)$, and let $\rho_{\theta}$ be the model defining function associated with a contact form $\theta$. Then,
$$\eta_{\theta}:=\left.\left(\rho_{\theta}^{-6} W_{\infty 0 \infty 0}^{-}\right)\right|_{M}$$
satisfies $\eta_{\widehat{\theta}}=e^{-3 \Upsilon} \eta_{\theta}$ for the rescaling $\widehat{\theta}=e^{\Upsilon} \theta$.
Proof. By Proposition 2.2, $\left.\boldsymbol{Z}_{\infty}\right|_{M}$ and $\left.\boldsymbol{Z}_{0}\right|_{M}$ are determined by $g$ and independent of $\theta$. Thus, we have $\widehat{W}_{\infty 0 \infty 0}^{-}=W_{\infty 0 \infty 0}^{-}+O\left(\rho^{7}\right)$. Since $\rho_{\widehat{\theta}}=e^{\Upsilon / 2} \rho_{\theta}+O\left(\rho^{2}\right)$ by (2.5), we obtain $\eta_{\widehat{\theta}}=e^{-3 \Upsilon} \eta_{\theta}$. \(\square\)

This lemma implies that if $\eta_{\theta}$ has a universal expression in terms of the Tanaka-Webster connection, then it defines a CR invariant $\eta \in \mathcal{E}(-3,-3)$. Since such a CR invariant is necessarily a multiple of the obstruction density [12], we are led to the CR invariant normalization $\eta=\lambda \mathcal{O}$.

Now we construct the metric and prove Theorem 1.2. We start with an arbitrary normal form ACH metric $g_{I J}^{(1)}$, which automatically satisfies $E_{I J}=O(\rho)$ by Lemma 3.1. Supposing that we have a normal form ACH metric $g_{I J}^{(m)}$ such that $E_{I J}=$ $O\left(\rho^{m}\right)$, we consider a perturbed metric
$$g_{I J}^{(m+1)}=g_{I J}^{(m)}+\psi_{I J}, \quad \psi_{\infty J}=0, \psi_{I J}=O\left(\rho^{m}\right)$$
and try to solve $E_{I J}=O\left(\rho^{m+1}\right)$. We also take $W_{I J K L}^{-}$into consideration in each inductive step by using the following equations modulo $O(\rho) \cdot \mathcal{D} W_{I J K L}^{-}$from (3.11):
$$\begin{aligned}
\nabla^{I} W_{I 1 \infty 1}^{-} & \equiv \frac{1}{4}\left(\rho \partial_{\rho}-4\right) W_{\infty 1 \infty 1}^{-}, \\
\nabla^{I} W_{I 0 \infty 0}^{-} & \equiv \frac{1}{4}\left(\rho \partial_{\rho}-6\right) W_{\infty 0 \infty 0}^{-}, \\
\nabla^{I} W_{I \infty \infty 1}^{-} & \equiv \frac{i}{2} W_{\infty 0 \infty 1}^{-}, \\
\nabla^{I} W_{I \infty \infty 0}^{-} & \equiv 0 .
\end{aligned}$$

By Lemma 3.1, the variation of $E_{I J}$ is given by
$$\begin{aligned}
& \delta E_{\infty \infty}=-\frac{1}{2} m(m-4) \psi_{00}-m(m-2) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right), \\
& \delta E_{\infty 0}=O\left(\rho^{m+1}\right), \\
& \delta E_{\infty 1}=-\frac{i}{2}(m+1) \psi_{01}+O\left(\rho^{m+1}\right), \\
& \delta E_{00}=-\frac{1}{8}\left(m^{2}-6 m-4\right) \psi_{00}+\frac{1}{2}(m-2) \psi_{1 \overline{1}}+O\left(\rho^{m+1}\right), \\
& \delta E_{01}=-\frac{1}{8}(m+1)(m-5) \psi_{01}+O\left(\rho^{m+1}\right), \\
& \delta E_{1 \overline{1}}=-\frac{1}{8}\left(m^{2}-6 m-8\right) \psi_{1 \overline{1}}+\frac{1}{8}(m-4) \psi_{00}+O\left(\rho^{m+1}\right), \\
& \delta E_{11}=-\frac{1}{8} m(m-4) \psi_{11}+O\left(\rho^{m+1}\right) .
\end{aligned}$$
The determinant of the coefficients of (4.9) and (4.11) as a system of linear equations for $\psi_{00}$ and $\psi_{1 \overline{1}}$ is
$$\operatorname{det}\left(\begin{array}{cc}
-\frac{1}{8}\left(m^{2}-6 m-4\right) & \frac{1}{2}(m-2) \\
\frac{1}{8}(m-4) & -\frac{1}{8}\left(m^{2}-6 m-8\right)
\end{array}\right)=\frac{1}{64} m(m+2)(m-6)(m-8) .$$

First we consider the case of $m \leq 5$, where the determinant is nonzero. We determine $\psi_{00}, \psi_{1 \overline{1}}$ (modulo $O\left(\rho^{m+1}\right)$ ) by (4.9), (4.11) so that $E_{00}, E_{1 \overline{1}}=O\left(\rho^{m+1}\right)$ holds. Then by the Bianchi identities (3.17), (3.18), we have $E_{\infty \infty}, E_{\infty 0}=O\left(\rho^{m+1}\right)$. We determine $\psi_{01}$ by (4.8) to obtain $E_{\infty 1}=O\left(\rho^{m+1}\right)$. Then, (3.19) gives $E_{01}=$ $O\left(\rho^{m+1}\right)$. When $m \leq 3$, (4.12) determines $\psi_{11}$ so that $E_{11}=O\left(\rho^{m+1}\right)$, thus we have $E_{I J}=O\left(\rho^{m+1}\right)$. Moreover, by (4.2)-(4.4) and Lemma 3.3, we also have $W_{I J K L}^{-}=O\left(\rho^{m+1}\right)$. When $m=4$, we cannot use (4.12) to obtain $E_{11}=O\left(\rho^{5}\right)$. However, since $W_{I J K L}^{-}=O\left(\rho^{4}\right)$, it follows from (4.2) that
$$C_{1 \infty 1}^{-}=\nabla^{I} W_{I 1 \infty 1}^{-}=\frac{1}{4}(4-4) W_{\infty 1 \infty 1}^{-}+O\left(\rho^{5}\right)=O\left(\rho^{5}\right),$$
so we have $E_{11}=O\left(\rho^{5}\right)$ by (3.20). (This also follows from the fact that the CR obstruction tensor $\mathcal{O}_{11}=\left.\left(\rho^{-4} E_{11}\right)\right|_{M}$ vanishes in three dimension; see [19, 20].) Thus, we have $E_{I J}=O\left(\rho^{5}\right)$ and by (4.2)-(4.4), it holds that
$$W_{\infty 1 \infty 1}^{-}=O\left(\rho^{4}\right), \quad W_{\infty 0 \infty 0}^{-}, W_{\infty 0 \infty 1}^{-}=O\left(\rho^{5}\right) .$$
We can choose $\psi_{11}$ so that $W_{\infty 1 \infty 1}^{-}=O\left(\rho^{5}\right)$ holds since
$$\delta W_{\infty 1 \infty 1}^{-}=\psi_{11}+O\left(\rho^{5}\right)$$
by (3.15). Thus we obtain $g_{I J}^{(5)}$ unique modulo $O\left(\rho^{5}\right)$ with $E_{I J}, W_{I J K L}^{-}=O\left(\rho^{5}\right)$. When $m=5$, we can construct $g_{I J}^{(6)}$ with $E_{I J}=O\left(\rho^{6}\right)$ in the same way for $m \leq 3$ and we also have $W_{I J K L}^{-}=O\left(\rho^{6}\right)$ by (4.2)-(4.4).

Next we consider the case of $m=6$, where the equations (4.6), (4.9), (4.11) are not pairwise independent. We determine $\psi_{01}$ by (4.8) so that $E_{\infty 1}=O\left(\rho^{7}\right)$.

Then we also have $E_{01}=O\left(\rho^{7}\right)$ by (3.19). We determine $\psi_{11}$ by (4.12) and obtain $E_{11}=O\left(\rho^{7}\right)$. By (3.16), we have
$$\delta W_{\infty 0 \infty 0}^{-}=\frac{14}{3} \psi_{00}-\frac{16}{3} \psi_{1 \overline{1}}+O\left(\rho^{7}\right) .$$
We use this equation and (4.6) to determine $\psi_{00}, \psi_{1 \overline{1}}$ so that
$$E_{\infty \infty}=O\left(\rho^{7}\right), \quad \eta=\lambda \mathcal{O}$$
holds. Thus we have determined $g_{I J}^{(7)}$ and we must check that it also satisfies $E_{00}, E_{1 \overline{1}}, E_{\infty 0}=O\left(\rho^{7}\right)$. Since $W_{I J K L}^{-}=O\left(\rho^{6}\right)$, by (4.3) we have
$$C_{0 \infty 0}^{-}=\frac{1}{4}(6-6) W_{\infty 0 \infty 0}^{-}+O\left(\rho^{7}\right)=O\left(\rho^{7}\right) .$$
Then it follows from (3.21) that
$$-\frac{5}{4} E_{00}+E_{1 \overline{1}}=O\left(\rho^{7}\right) .$$
Also, (3.17) gives
$$E_{00}+4 E_{1 \overline{1}}=O\left(\rho^{7}\right) .$$
Therefore, we have $E_{00}, E_{1 \overline{1}}=O\left(\rho^{7}\right)$. Moreover, by $W_{I J K L}^{-}=O\left(\rho^{6}\right)$ and the equation (4.5), it holds that $C_{\infty \infty 0}^{-}=O\left(\rho^{7}\right)$, which implies $E_{\infty 0}=O\left(\rho^{7}\right)$ by (3.22). Thus, $g_{I J}^{(7)}$ satisfies $E_{I J}=O\left(\rho^{7}\right), W_{I J K L}^{-}=O\left(\rho^{6}\right)$, and $\eta=\lambda \mathcal{O}$. We note that it satisfies $W_{I J K L}^{-}=O\left(\rho^{7}\right)$ when $\lambda=0$.

When $m=7$, we can determine $g_{I J}^{(8)}$ so that it satisfies $E_{I J}=O\left(\rho^{8}\right)$ in the same way as for $m \leq 3$. If $\lambda=0$, it also satisfies $W_{I J K L}^{-}=O\left(\rho^{8}\right)$ by (4.2)-(4.4).

Let us consider the case of $m=8$. In this case, the equations (4.9) and (4.11) are not independent. We use (4.6), (4.9) to determine $\psi_{00}, \psi_{1 \overline{1}}$ so that $E_{\infty \infty}, E_{00}=O\left(\rho^{9}\right)$. Then (3.17) gives $E_{1 \overline{1}}=O\left(\rho^{9}\right)$. We determine $\psi_{01}$ and $\psi_{11}$ by (4.8) and (4.12) respectively and obtain $E_{\infty 1}, E_{11}=O\left(\rho^{9}\right)$. By (3.18), (3.19), we have $E_{\infty 0}, E_{01}=O\left(\rho^{9}\right)$. Thus we have constructed $g_{I J}^{(9)}$ with $E_{I J}=O\left(\rho^{9}\right)$, which satisfies $W_{I J K L}^{-}=O\left(\rho^{9}\right)$ when $\lambda=0$ by (4.2)-(4.4).

Finally, let $m \geq 9$. In this case, the equation $E_{I J}=O\left(\rho^{m+1}\right)$ determines $g_{I J}^{(m+1)}$ in the same way as in $m \leq 3$, and it satisfies $W_{I J K L}^{-}=O\left(\rho^{m+1}\right)$ by (4.2)-(4.4) when $\lambda=0$.

Consequently, we can construct all $g_{I J}^{(m+1)}$ inductively, and by Borel's lemma we obtain a solution $g_{I J}^{\lambda}$ to
$$E_{I J}=O\left(\rho^{\infty}\right), \quad W_{I J K L}^{-}=O\left(\rho^{6}\right), \quad \eta=\lambda \mathcal{O},$$
which is unique modulo $O\left(\rho^{\infty}\right)$. By the construction, $g_{I J}^{0}$ satisfies $W_{I J K L}^{-}=O\left(\rho^{\infty}\right)$. Thus we complete the proof of Theorem 1.2.
4.2. Dependence on $\lambda$. We can read off the dependence of $g_{I J}^{\lambda}$ on the parameter $\lambda$ from the construction.

Proposition 4.2. The metric $g_{I J}^{\lambda}$ admits the following asymptotic expansion:
$$g_{I J}^{\lambda} \sim g_{I J}^{0}+\sum_{k=1}^{\infty} \lambda^{k} \rho^{6 k} \phi_{I J}^{(k)}(\rho), \quad \phi_{I \infty}^{(k)}=\phi_{01}^{(k)}=\phi_{11}^{(k)}=0 .$$
Here, $\phi_{I J}^{(k)}(\rho)$ is a formal power series in $\rho$.
Proof. We write the Taylor expansion of $g_{I J}^{\lambda}-g_{I J}^{0}$ as
$$g_{I J}^{\lambda}-g_{I J}^{0} \sim \sum_{k=0}^{\infty} \rho^{k} \Phi_{I J}^{\lambda, k}, \quad \Phi_{I \infty}^{\lambda, k}=0 .$$

Then, it suffices to show that $\Phi_{01}^{\lambda, k}=\Phi_{11}^{\lambda, k}=0$ and each $\Phi_{I J}^{\lambda, k}$ is a polynomial in $\lambda$ of degree $\leq k / 6$. First, we note that $g_{I J}^{\lambda}-g_{I J}^{0}=O\left(\rho^{6}\right)$ hence $\Phi_{I J}^{\lambda, k}=0$ for $k \leq 5$. Since both $g_{I J}^{\lambda}$ and $g_{I J}^{0}$ satisfy $E_{\infty 1}, E_{11}=O\left(\rho^{\infty}\right)$, we have $\Phi_{01}^{\lambda, k}=\Phi_{11}^{\lambda, k}=0$ also for $k \geq 6$ by (4.8), (4.12). From (4.6), (4.13), we see that $\Phi_{00}^{\lambda, 6}$ and $\Phi_{1 \overline{1}}^{\lambda, 6}$ are determined by
$$\begin{aligned}
& -6 \Phi_{00}^{\lambda, 6}-24 \Phi_{1 \overline{1}}^{\lambda, 6}=0 \\
& \frac{14}{3} \Phi_{00}^{\lambda, 6}-\frac{16}{3} \Phi_{1 \overline{1}}^{\lambda, 6}=\lambda \mathcal{O} .
\end{aligned}$$
Thus we have $\operatorname{deg} \Phi_{00}^{\lambda, 6}=\operatorname{deg} \Phi_{1 \overline{1}}^{\lambda, 6}=1$. Now we shall prove $\operatorname{deg} \Phi_{00}^{\lambda, k}, \operatorname{deg} \Phi_{1 \overline{1}}^{\lambda, k} \leq k / 6$ by the induction on $k$. When $k \geq 7, \Phi_{00}^{\lambda, k}$ and $\Phi_{1 \overline{1}}^{\lambda, k}$ are determined by the condition $\left.\partial_{\rho}^{k} E_{00}\right|_{\rho=0}=\left.\partial_{\rho}^{k} E_{1 \overline{1}}\right|_{\rho=0}=0$ for $k \neq 8$ and $\left.\partial_{\rho}^{k} E_{\infty \infty}\right|_{\rho=0}=\left.\partial_{\rho}^{k} E_{00}\right|_{\rho=0}=0$ for $k=8$. These conditions can be regarded as a system of linear equations for $\Phi_{00}^{\lambda, k}$ and $\Phi_{1 \overline{1}}^{\lambda, k}$, and in view of (2.7), (2.11), (3.2), the terms involving the other components are linear combinations of
$$\mathcal{D}_{1} \Phi_{I_{1} J_{1}}^{\lambda, l_{1}} \cdots \mathcal{D}_{p} \Phi_{I_{p} J_{p}}^{\lambda, l_{p}} \quad\left(l_{1}+\cdots+l_{p} \leq k, l_{j}<k\right),$$
where $\mathcal{D}_{j}$ is a differential operator on $M$. Then, by the induction hypothesis, we have
$$\operatorname{deg} \Phi_{I J}^{\lambda, k} \leq \frac{l_{1}+\cdots+l_{p}}{6} \leq \frac{k}{6} .$$
Thus, we complete the proof. \(\square\)
4.3. Evenness. Let $g$ be a normal form ACH metric on $M \times[0, \infty)_{\rho}$. Then it can be written in the form
$$g=\frac{h_{\rho}+4 d \rho^{2}}{\rho^{2}},$$
where $h_{\rho}$ is a family of Riemannian metrics on $M$. We say $g$ is even when $h_{\rho}$ has even Laurent expansion at $\rho=0$. In other words, $g$ is even if and only if the components $g_{00}, g_{11}, g_{1 \overline{1}}$ are even in $\rho$, and $g_{01}$ is odd in $\rho$. An ACH metric is said to be even if its normal form is even for any choice of $\theta$.

Proposition 4.3. The $A C H$ metric $g^{\lambda}$ is even.
Proof. Fix a contact form $\theta$ and suppose $g^{\lambda}$ is in the normal form as (4.14). By using the Laurent expansion of $h_{\rho}$, we can regard the right-hand side of (4.14) as an ACH metric $g_{-}^{\lambda}$ defined on $M \times(-\infty, 0]_{\rho}$. Then, $g_{-}^{\lambda}$ also satisfies
$$E_{I J}=O\left(\rho^{\infty}\right), \quad W_{I J K L}^{-}=O\left(\rho^{6}\right), \quad \eta=\lambda \mathcal{O}$$
with respect to the orientation satisfying
$$i \boldsymbol{\theta}^{0} \wedge \boldsymbol{\theta}^{1} \wedge \boldsymbol{\theta}^{\overline{1}} \wedge \boldsymbol{\theta}^{\infty}=i \rho^{-5} \theta \wedge \theta^{1} \wedge \theta^{\overline{1}} \wedge d \rho>0$$
We consider the ACH metric $\iota^{*} g_{-}^{\lambda}$ on $M \times[0, \infty)_{\rho}$, where $\iota(x, \rho):=(x,-\rho)$. Since $\iota$ preserves the orientation, $\iota^{*} g_{-}^{\lambda}$ satisfies
$$E_{I J}=O\left(\rho^{\infty}\right), \quad W_{I J K L}^{-}=O\left(\rho^{6}\right) .$$
Noting that $\iota_{*} \boldsymbol{Z}_{\infty}=\boldsymbol{Z}_{\infty}$ and $\iota_{*} \boldsymbol{Z}_{0}=\boldsymbol{Z}_{0}$, we have
$$\begin{aligned}
\rho^{-6} W^{-}\left[\iota^{*} g_{-}^{\lambda}\right]_{\infty 0 \infty 0} & =\left(\iota^{*} \rho\right)^{-6}\left(\iota^{*} W^{-}\left[g_{-}^{\lambda}\right]\right)\left(\boldsymbol{Z}_{\infty}, \boldsymbol{Z}_{0}, \boldsymbol{Z}_{\infty}, \boldsymbol{Z}_{0}\right) \\
& =\iota^{*}\left(\rho^{-6} W^{-}\left[g_{-}^{\lambda}\right]\left(\iota_{*} \boldsymbol{Z}_{\infty}, \iota_{*} \boldsymbol{Z}_{0}, \iota_{*} \boldsymbol{Z}_{\infty}, \iota_{*} \boldsymbol{Z}_{0}\right)\right) \\
& =\iota^{*}\left(\rho^{-6} W^{-}\left[g_{-}^{\lambda}\right]_{\infty 0 \infty 0}\right) .
\end{aligned}$$
Thus, $\iota^{*} g_{-}^{\lambda}$ also satisfies $\eta=\lambda \mathcal{O}$. Therefore, by the uniqueness we obtain $\iota^{*} g_{-}^{\lambda}=$ $g^{\lambda}+O\left(\rho^{\infty}\right)$, which implies that $g^{\lambda}$ is even. \(\square\)

\section*{5. CR GJMS operators}

Matsumoto [21] generalized the CR GJMS operators to partially integrable CR manifolds via Dirichlet-to-Neumann type operators associated with eigenvalue equations for the Laplacian of the ACH metric. In dimension three, it is stated as follows: