---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Asymptotics of Kähler-Einstein metrics on complex hyperbolic cusps]

---
source_file: 2108_13390.pdf
converter: mathpix
format: mmd
---

\title{
ASYMPTOTICS OF KÄHLER-EINSTEIN METRICS ON COMPLEX HYPERBOLIC CUSPS
}

\author{
XIN FU, HANS-JOACHIM HEIN, AND XUMIN JIANG
}

\begin{abstract}
Let $L$ be a negative holomorphic line bundle over an $(n-1)$-dimensional complex torus $D$. Let $h$ be a Hermitian metric on $L$ such that the curvature form of the dual Hermitian metric defines a flat Kähler metric on $D$. Then $h$ is unique up to scaling, and, for some closed tubular neighborhood $V$ of the zero section $D \subset L$, the form $\omega_{h}=-(n+1) i \partial \bar{\partial} \log (-\log h)$ defines a complete Kähler-Einstein metric on $V \backslash D$ with $\operatorname{Ric}\left(\omega_{h}\right)=-\omega_{h}$. In fact, $\omega_{h}$ is complex hyperbolic, i.e., the holomorphic sectional curvature of $\omega_{h}$ is constant, and $\omega_{h}$ has the usual doubly-warped cusp structure familiar from complex hyperbolic geometry. In this paper, we prove that if $U$ is another closed tubular neighborhood of the zero section and if $\omega$ is a complete Kähler-Einstein metric with $\operatorname{Ric}(\omega)=-\omega$ on $U \backslash D$, then there exist a Hermitian metric $h$ as above and a $\delta \in \mathbb{R}^{+}$such that $\omega-\omega_{h}=O\left(e^{-\delta \sqrt{-\log h}}\right)$ to all orders with respect to $\omega_{h}$ as $h \rightarrow 0$. This rate is doubly exponential in the distance from a fixed point, and is sharp.
\end{abstract}

\section*{1. Introduction}

Background and main result. Complex hyperbolic $n$-space $\mathbb{C} H^{n}$ is the model space uniformizing Kähler manifolds of complex dimension $n \geqslant 2$ with constant negative holomorphic sectional curvature. $\mathbb{C} H^{n}$ is most conveniently realized as the unit ball in $\mathbb{C}^{n}$ together with the Bergman metric, and is one of the first examples of a Kähler-Einstein manifold [13, 22]. Finite-volume quotients of $\mathbb{C} H^{n}$ are either compact or have cuspidal ends. See [2, 17] for good introductions to complex hyperbolic cusps. In this paper, we are interested in a stability property of these cusps as Kähler-Einstein manifolds.

We begin by explaining an alternative description of complex hyperbolic cusps in terms of the Calabi ansatz [8, 9]. Let $D$ be a (necessarily projective) complex torus of complex dimension $n-1$ together with a negative holomorphic line bundle $L \rightarrow D$. Let $h$ be any Hermitian metric on $L$ such that the curvature form of the Hermitian metric dual to $h$ is a flat Kähler metric on $D$. Then $h$ is unique up to scaling, i.e., up to replacing $h$ by $\lambda h$ for some $\lambda \in \mathbb{R}^{+}$. This scaling freedom can also be understood as a consequence of the natural action of $\mathbb{C}^{*}$ on the total space of $L$. Viewing $h$ as a smooth function on the total space which is homogeneous of degree 2 along every fiber, we define $\sigma=-\log h$ and $\omega_{h}=$ $-(n+1) i \partial \bar{\partial} \log \sigma$. Then $\omega_{h}$ is a Kähler form on $\{0<h<1\}$ with $\operatorname{Ric}\left(\omega_{h}\right)=-\omega_{h}$. If $V$ is any closed tubular neighborhood of the zero section $D \subset L$ of the form $V=\{h \leqslant \delta\}$ for some $\delta \in(0,1)$, then the Riemannian manifold-with-boundary $\left(V \backslash D, \omega_{h}\right)$ is complete of finite volume. In fact, it is a complex hyperbolic cusp, and any complex hyperbolic cusp arises in this way up to a finite cover. Define $x=\frac{1}{\sigma}$ and $\rho=-\sqrt{(n+1) / 2} \log x$. Then $\rho$ is a Busemann function (its gradient has constant length 1). Also, on the level set $Y_{\varepsilon}=\left\{x=\varepsilon^{2}\right\}$, the metric tensor is proportional to $\varepsilon^{4}$ in the $S^{1}$-directions and to $\varepsilon^{2}$ in the $D$-directions. Here we use the Chern connection of $h$ to define a complement to the $S^{1}$-directions inside the tangent bundle $T Y_{\varepsilon}$, and this decomposition is orthogonal with respect to $\omega_{h}$.

Write $Y=\partial V$. Datar-Fu-Song [7] have proved that for any smooth function $\beta: Y \rightarrow \mathbb{R}$ there exists a unique complete Kähler-Einstein metric $\omega=\omega_{h}+i \partial \bar{\partial} u$ on $V$ such that $\omega^{n}=e^{u} \omega_{h}^{n}$ on $V$, hence in particular $\operatorname{Ric}(\omega)=-\omega$ on $V$, and $u=\beta$ on $Y$. Moreover, $u$ and all of its covariant derivatives with respect to $\omega_{h}$ decay like $O\left((-\log x)^{-1}\right)$, i.e., linearly in terms of the distance function $\rho$. This improves a more global construction of [6, 14, 23] on projective varieties with cusp singularities.

\footnotetext{
Date: November 10, 2021.
}

In this paper, we determine the precise asymptotics of the Datar-Fu-Song solutions [7].
Main Theorem. Fix a Hermitian metric $h$ on $L$ as above. Let $U$ be a closed tubular neighborhood of the zero section $D \subset L$. Let $\omega$ be a complete Kähler-Einstein metric on $U \backslash D$ such that $\operatorname{Ric}(\omega)=-\omega$. Let $u=\log \left(\omega^{n} / \omega_{h}^{n}\right)$, so that $\omega=\omega_{h}+i \partial \bar{\partial} u$ and, by [7], $u=O\left((-\log x)^{-1}\right)$ as $x \rightarrow 0^{+}$to all orders with respect to $\omega_{h}$. Then there exists a constant $c \in \mathbb{R}$ such that for all $k \in \mathbb{N}_{0}$,
$$\left|\nabla_{\omega_{h}}^{k}(u+(n+1) \log (1+c x))\right|_{\omega_{h}}=O_{k}\left(x^{-\frac{n}{2}+\frac{1}{4}-\frac{k}{2}} e^{-\frac{2 \sqrt{\lambda_{1}}}{\sqrt{x}}}\right) \text { as } x \rightarrow 0^{+} .$$
Here $\lambda_{1}$ denotes the first eigenvalue of $D$ with respect to the flat Kähler metric given by the curvature form of $h^{-1}$, and neither the power $-\frac{n}{2}+\frac{1}{4}-\frac{k}{2}$ nor the exponent $2 \sqrt{\lambda_{1}}$ can be improved.

In particular, $\omega$ is asymptotic to the shifted Calabi model metric $\omega_{\lambda h}\left(\lambda=e^{-c}\right)$ at a rate which is exponentially faster than the rate at which $\omega_{\lambda h}$ is asymptotic to $\omega_{h}$, i.e., exponential vs. polynomial in terms of $x$, or doubly vs. singly exponential in terms of the distance function $\rho$.

Overview of the proof. The function $x$ is the unique decaying radial solution to the homogeneous linearized Kähler-Einstein equation. We expand $u$ according to powers of $x$, which results in a formal power series solution differing from $u$ by $O\left(x^{\infty}\right)$. This is similar to asymptotic expansion arguments as in [12, 16, 18, 19, 25], with our proof being closest in spirit to [12]. The coefficients of our expansion are actually constants, the first coefficient determines all the others, and the formal series converges to $-(n+1) \log (1+c x)$ for some $c \in \mathbb{R}$. We think of this expression as the "tangent cone" of $u$.

Asymptotic expansion methods [12, 16, 18, 19, 25] stop at the statement that the difference between $u$ and some formal (in this case, convergent) power series in $x$ is $O\left(x^{\infty}\right)$. A new point here is that we go further and prove an explicit estimate, (1.1), for this difference, which is actually completely sharp as evidenced by the next generation of solutions to the homogeneous linearized PDE. This estimate is exponential in $x$. In situations with conical or cylindrical geometry, i.e., with an asymptotic scaling or translation symmetry, this kind of statement is reminiscent of the unique tangent cone theorem of [1]; see [20, p.270] for a simplification of [1] using rescaling arguments, and see [4] for an application of [20] in the context of Einstein metrics. There are no useful scaling symmetries in our setting because our geometry is cuspidal (with two different collapsing scales) rather than conical or cylindrical.

We therefore develop a more effective version of the unique tangent cone argument, which is possible in our situation because we already have an explicit decay rate, $O\left(x^{\infty}\right)$, and our goal is to boost this to the decay rate of the next generation of solutions, $O\left(e^{-\delta / \sqrt{x}}\right)$. The two main ingredients are (A) an explicit integral operator in terms of Bessel functions, which serves as a right inverse to the linearized operator, and which we need to bound with respect to weighted norms that are piecewise polynomial and piecewise exponential in $x$ (this is the most novel ingredient), and (B) uniform Schauder estimates on metric balls of radius ~ 1. These Schauder estimates are nontrivial because the geometry scale of $\omega_{h}$, where Schauder estimates follow from the standard theory on balls in $\mathbb{C}^{n}$, is only $\sim x$. Since $D$ is a torus, we can work around this problem in a fairly standard manner by using local universal covers, or quasi-coordinates [6], although in principle there is now a way of proving uniform Schauder estimates at large scales even if the local fundamental groups are trivial at all scales [11].

Organization of the paper. In Section 2 we carefully review the geometry of the model metrics $\omega_{h}$, compute the linearized operator in convenient coordinates, and state the necessary results from [7]. In Section 3, after some preliminary estimates on the solution $u$, we expand $u$ according to powers of $x$, which determines the tangent cone. In Section 4, we construct a suitable bounded right inverse to the linearized operator as an explicit integral operator in terms of Bessel functions and then carry out the "unique tangent cone" argument, which leads to the desired sharp estimate of the remainder.

Acknowledgments. HJH was partially supported by the DFG under Germany's Excellence Strategy EXC 2044-390685587 "Mathematics Münster: Dynamics-Geometry-Structure" as well as by the CRC 1442 "Geometry: Deformations and Rigidity" of the DFG.

We would also like to point out the related, nearly simultaneous but independent papers [3, 21]. In [3], the analysis of complex hyperbolic cusps is studied from a different point of view with the aim of constructing complex hyperbolic Dehn filling type metrics. This is related to our Example 2.7. In [21, Section 6.5], unique tangent cone arguments in the spirit of Simon's method [20] are carried out in a different geometry with two-scale collapsing, resulting in estimates similar to our Main Theorem.

\section*{2. Preliminaries}

All the work in Sections 2.1-2.2 (computational properties of the model metric and of the linearized operator) goes through in a more general setting where $D$ is a compact $(n-1)$-dimensional Ricci-flat Kähler manifold rather than a flat complex torus. In this setting, the model metric $\omega_{h}$ is still Kähler-Einstein, but unless $D$ is a finite quotient of a complex torus it is not complex hyperbolic, and indeed its holomorphic sectional curvature is unbounded above and below. Unboundedness of the curvature would start causing problems in Section 2.3 (results of Datar-Fu-Song [7]) but also at various points later in the paper. Except for generalizing the Monge-Ampère $C^{2}$ estimate of [7, 14], these problems should be solvable along the lines of [11], but the $C^{2}$ estimate remains a fundamental obstacle. Thus, overall, in this paper we chose to restrict ourselves to the case where $D$ is a torus.
2.1. The model metric. Let $\pi: L \rightarrow D$ be a negative holomorphic line bundle over a complex torus of complex dimension $n-1$ for $n \geqslant 2$. Let $h$ be a Hermitian metric on $L$ such that the curvature form of the dual Hermitian metric is a flat Kähler metric on $D$. Then $h$ is unique up to scaling. We view $h$ as a smooth function on the total space of $L$ which is fiberwise homogeneous of degree 2. In other words, we identify $h$ with the function $\left(\pi^{*} h\right)(s, s)$, where $s$ denotes the tautological section of the line bundle $\pi^{*} L \rightarrow L$. It is also helpful to introduce the three functions
$$\sigma:=-\log h, x:=\frac{1}{\sigma}, \quad \rho:=-\sqrt{\frac{n+1}{2}} \log x .$$
With this understood, we define the well-known Kähler-Einstein model metric
$$\omega_{h}:=-(n+1) i \partial \bar{\partial} \log \sigma$$
on the region $\{0<h<1\}$. See [8,9] for two recent treatments of this metric in the literature. Fixing an arbitrary point $p \in D \subset L$, we choose local holomorphic coordinates $\left(z_{1}, \ldots, z_{n}\right)=\left(z^{\prime}, z_{n}\right)$ around $p$ on $L$ such that $\pi=z^{\prime}$ in this chart and $z_{i}(p)=0$ for all $i=1, \ldots, n$. In particular, $D=\left\{z_{n}=0\right\}$. We can also assume without loss of generality that the range of $z^{\prime}$ is the unit ball $B \subset \mathbb{C}^{n-1}$ centered at the origin. Then $h=e^{-\varphi\left(z^{\prime}\right)}\left|z_{n}\right|^{2}$, and a simple computation yields the following lemma.

Lemma 2.1. In any local holomorphic chart $\left(z^{\prime}, z_{n}\right)$ as above,
$$\omega_{h}=(n+1)\left[-i x \partial \bar{\partial} \varphi+i x^{2}\left(\partial \varphi-\partial \log z_{n}\right) \wedge\left(\bar{\partial} \varphi-\bar{\partial} \log \bar{z}_{n}\right)\right] .$$
Thus, under the convention that
$$\omega_{h}=i \sum g_{j \bar{k}} d z^{j} \wedge d \bar{z}^{k},$$
the metric coefficients are given by
$$g_{j \bar{k}}=-i \omega_{h}\left(\partial_{j}, \partial_{\bar{k}}\right)=(n+1)\left[-x \varphi_{j \bar{k}}+x^{2}\left(\varphi_{j}-\frac{\delta_{j n}}{z_{n}}\right)\left(\varphi_{\bar{k}}-\frac{\delta_{k n}}{\bar{z}_{n}}\right)\right] .$$

Using (2.5) and the Ricci-flatness of the Kähler metric $-i \partial \bar{\partial} \varphi$ on $D$, one checks that $\omega_{h}$ is indeed a Kähler form on the whole region $\{0<h<1\}$ and that $\operatorname{Ric}\left(\omega_{h}\right)=-\omega_{h}$. Because the metric $-i \partial \bar{\partial} \varphi$ is actually flat in our setting, $\omega_{h}$ is complex hyperbolic, and its holomorphic sectional curvature, i.e., the Riemannian sectional curvature of $J$-invariant 2-planes, is constant equal to $-\frac{2}{n+1}$. This is the only formal property of $\omega_{h}$ that changes if we allow for $D$ to be a general Calabi-Yau manifold.

We now study the natural foliation of our model space by the level sets
$$Y_{\varepsilon}:=\left\{x=\varepsilon^{2}\right\}=\left\{\varphi\left(z^{\prime}\right)-\log \left|z_{n}\right|^{2}=\varepsilon^{-2}\right\} .$$
We introduce a smooth real-valued coordinate chart $\left(x_{\alpha}, y_{\alpha}, \theta\right)$ on $Y_{\varepsilon}$ by writing $z^{\prime}=\left(z_{1}, \ldots, z_{n-1}\right)$, $x_{\alpha}=\operatorname{Re}\left(z_{\alpha}\right)$ and $y_{\alpha}=\operatorname{Im}\left(z_{\alpha}\right)$ for all $\alpha \in\{1, \ldots, n-1\}$, and $z_{n}=r e^{i \theta}$ as usual.

Lemma 2.2. Let $g_{h}$ denote the Riemannian metric associated with $\omega_{h}$ and define
$$g_{\varepsilon}:=\left.\frac{1}{n+1} \varepsilon^{-2} g_{h}\right|_{Y_{\varepsilon}} .$$
Then, with respect to the chart $\left(x_{\alpha}, y_{\alpha}, \theta\right)$, the metric $g_{\varepsilon}$ is represented by
$$\begin{aligned}
g_{\varepsilon}= & \left(\begin{array}{ccc}
\left(g_{\varepsilon}\right)_{x_{\alpha} x_{\beta}} & \left(g_{\varepsilon}\right)_{x_{\alpha} y_{\beta}} & \left(g_{\varepsilon}\right)_{x_{\alpha} \theta} \\
\left(g_{\varepsilon}\right)_{y_{\alpha} x_{\beta}} & \left(g_{\varepsilon}\right)_{y_{\alpha} y_{\beta}} & \left(g_{\varepsilon}\right)_{y_{\alpha} \theta} \\
\left(g_{\varepsilon}\right)_{\theta x_{\beta}} & \left(g_{\varepsilon}\right)_{\theta y_{\beta}} & \left(g_{\varepsilon}\right)_{\theta \theta}
\end{array}\right) \\
= & \left(\begin{array}{ccc}
-\frac{1}{2}\left(\varphi_{x_{\alpha} x_{\beta}}+\varphi_{y_{\alpha} y_{\beta}}\right)+\frac{1}{2} \varepsilon^{2} \varphi_{y_{\alpha}} \varphi_{y_{\beta}} & -\frac{1}{2}\left(\varphi_{x_{\alpha} y_{\beta}}-\varphi_{y_{\alpha} x_{\beta}}\right)-\frac{1}{2} \varepsilon^{2} \varphi_{y_{\alpha}} \varphi_{x_{\beta}} & \varepsilon^{2} \varphi_{y_{\alpha}} \\
-\frac{1}{2}\left(\varphi_{y_{\alpha} x_{\beta}}-\varphi_{x_{\alpha} y_{\beta}}\right)-\frac{1}{2} \varepsilon^{2} \varphi_{x_{\alpha}} \varphi_{y_{\beta}} & -\frac{1}{2}\left(\varphi_{y_{\alpha} y_{\beta}}+\varphi_{x_{\alpha} x_{\beta}}\right)+\frac{1}{2} \varepsilon^{2} \varphi_{x_{\alpha}} \varphi_{x_{\beta}} & -\varepsilon^{2} \varphi_{x_{\alpha}} \\
\varepsilon^{2} \varphi_{y_{\beta}} & -\varepsilon^{2} \varphi_{x_{\beta}} & 2 \varepsilon^{2}
\end{array}\right) .
\end{aligned}$$
Proof. Let $\tilde{g}_{h}:=\frac{1}{n+1} g_{h}$ and $\tilde{\omega}_{h}:=\frac{1}{n+1} \omega_{h}$. Let $\Pi: B \times S^{1} \rightarrow Y_{\varepsilon}$ denote the fiberwise radial projection, which is a diffeomorphism. Then we need to compute the matrix representing the Riemannian metric $\Pi^{*}\left(\left.\varepsilon^{-2} \tilde{g}_{h}\right|_{Y_{\varepsilon}}\right)$ with respect to the product coordinate frame $\partial_{x_{\alpha}}, \partial_{y_{\alpha}}, \partial_{\theta}$ on $B \times S^{1}$.

The $\theta \theta$ component. Here we use that $\Pi$ is $S^{1}$-equivariant, which implies that
$$\Pi_{*}\left(\partial_{\theta}\right)=\partial_{\theta} .$$
Thus, using also (2.3) and the formula $\partial \log z_{n}=\frac{d r}{r}+i d \theta$,
$$\begin{aligned}
\Pi^{*}\left(\left.\varepsilon^{-2} \tilde{g}_{h}\right|_{Y_{\varepsilon}}\right)\left(\partial_{\theta}, \partial_{\theta}\right) & =\varepsilon^{-2} \tilde{\omega}_{h}\left(\partial_{\theta}, J \partial_{\theta}\right) \\
& =2 \varepsilon^{2} \operatorname{Im}\left[\left(\partial \log z_{n}\right)\left(\partial_{\theta}\right) \cdot\left(\bar{\partial} \log \bar{z}_{n}\right)\left(r \partial_{r}\right)\right] \\
& =2 \varepsilon^{2} .
\end{aligned}$$
The $\theta x_{\alpha}$ and $\theta y_{\alpha}$ components. Again because $\Pi$ is $S^{1}$-equivariant, we must have that
$$\Pi_{*}\left(\partial_{x_{\alpha}}\right)=\partial_{x_{\alpha}}+F_{\alpha} r \partial_{r}, \Pi_{*}\left(\partial_{y_{\alpha}}\right)=\partial_{y_{\alpha}}+G_{\alpha} r \partial_{r}$$
for some real-valued functions $F_{\alpha}, G_{\alpha}$. Therefore,
$$\begin{aligned}
\Pi^{*}\left(\left.\varepsilon^{-2} \tilde{g}_{h}\right|_{Y_{\varepsilon}}\right)\left(\partial_{\theta}, \partial_{x_{\alpha}}\right) & =\varepsilon^{-2} \tilde{\omega}_{h}\left(\partial_{\theta}, J\left(\partial_{x_{\alpha}}+\operatorname{Fr} \partial_{r}\right)\right) \\
& =\varepsilon^{-2} \tilde{\omega}_{h}\left(\partial_{\theta}, \partial_{y_{\alpha}}\right) \\
& =-2 \varepsilon^{2} \operatorname{Im}\left[(\partial \varphi)\left(\partial_{y_{\alpha}}\right) \cdot\left(\bar{\partial} \log \bar{z}_{n}\right)\left(\partial_{\theta}\right)\right] \\
& =\varepsilon^{2} \varphi_{y_{\alpha}} .
\end{aligned}$$
Here we have used the general formula $\partial \varphi=\frac{1}{2}(d \varphi-i d \varphi \circ J)$. Similarly,
$$\Pi^{*}\left(\left.\varepsilon^{-2} \tilde{g}_{h}\right|_{Y_{\varepsilon}}\right)\left(\partial_{\theta}, \partial_{y_{\alpha}}\right)=-\varepsilon^{2} \varphi_{x_{\alpha}} .$$

The $x_{\alpha} x_{\beta}, x_{\alpha} y_{\beta}$ and $y_{\alpha} y_{\beta}$ components. Here we first need to determine the functions $F_{\alpha}, G_{\alpha}$ of (2.11). Notice that $\Pi_{*}\left(\partial_{x_{\alpha}}\right), \Pi_{*}\left(\partial_{y_{\alpha}}\right)$ must be tangent to $Y_{\varepsilon}$ and the tangent bundle of $Y_{\varepsilon}$ is the kernel of the differential of the function $\varphi\left(z^{\prime}\right)-\log \left|z_{n}\right|^{2}$. Using this, it is easy to see that
$$F_{\alpha}=\frac{1}{2} \varphi_{x_{\alpha}}, G_{\alpha}=\frac{1}{2} \varphi_{y_{\alpha}} .$$
Thus,
$$\begin{aligned}
& \Pi^{*}\left(\left.\varepsilon^{-2} \tilde{g}_{h}\right|_{Y_{\varepsilon}}\right)\left(\partial_{x_{\alpha}}, \partial_{x_{\beta}}\right)=\varepsilon^{-2} \tilde{\omega}_{h}\left(\partial_{x_{\alpha}}+F_{\alpha} r \partial_{r}, \partial_{y_{\beta}}+F_{\beta} \partial_{\theta}\right) \\
& \quad=(-i \partial \bar{\partial} \varphi)\left(\partial_{x_{\alpha}}, \partial_{y_{\beta}}\right)-2 \varepsilon^{2} \operatorname{Im}\left[\left((\partial \varphi)\left(\partial_{x_{\alpha}}\right)-\frac{1}{2} \varphi_{x_{\alpha}}\right) \cdot\left((\bar{\partial} \varphi)\left(\partial_{y_{\beta}}\right)+\frac{i}{2} \varphi_{x_{\beta}}\right)\right] \\
& \quad=-\frac{1}{2}\left(\varphi_{x_{\alpha} x_{\beta}}+\varphi_{y_{\alpha} y_{\beta}}\right)+\frac{1}{2} \varepsilon^{2} \varphi_{y_{\alpha}} \varphi_{y_{\beta}} .
\end{aligned}$$
Here we have applied the general Kähler geometry formula
$$(i \partial \bar{\partial} \varphi)(U, J V)=\frac{1}{2}\left(\left(\nabla^{2} \varphi\right)(U, V)+\left(\nabla^{2} \varphi\right)(J U, J V)\right)$$
with respect to the standard Euclidean Kähler metric on $B$. Similarly,
$$\begin{aligned}
\Pi^{*}\left(\varepsilon^{-2}\right. & \left.\left.\tilde{g}_{h}\right|_{Y_{\varepsilon}}\right)\left(\partial_{x_{\alpha}}, \partial_{y_{\beta}}\right)=\varepsilon^{-2} \tilde{\omega}_{h}\left(\partial_{x_{\alpha}}+F_{\alpha} r \partial_{r},-\partial_{x_{\beta}}+G_{\beta} \partial_{\theta}\right) \\
& =(-i \partial \bar{\partial} \varphi)\left(\partial_{x_{\alpha}},-\partial_{x_{\beta}}\right)-2 \varepsilon^{2} \operatorname{Im}\left[\left((\partial \varphi)\left(\partial_{x_{\alpha}}\right)-\frac{1}{2} \varphi_{x_{\alpha}}\right) \cdot\left((\bar{\partial} \varphi)\left(-\partial_{x_{\beta}}\right)+\frac{i}{2} \varphi_{y_{\beta}}\right)\right] \\
& =-\frac{1}{2}\left(\varphi_{x_{\alpha} y_{\beta}}-\varphi_{y_{\alpha} x_{\beta}}\right)-\frac{1}{2} \varepsilon^{2} \varphi_{y_{\alpha}} \varphi_{x_{\beta}},
\end{aligned}$$
as well as
$$\begin{aligned}
\Pi^{*}\left(\varepsilon^{-2}\right. & \left.\tilde{g}_{h} \mid Y_{\varepsilon}\right)\left(\partial_{y_{\alpha}}, \partial_{y_{\beta}}\right)=\varepsilon^{-2} \tilde{\omega}_{h}\left(\partial_{y_{\alpha}}+G_{\alpha} r \partial_{r},-\partial_{x_{\beta}}+G_{\beta} \partial_{\theta}\right) \\
& =(-i \partial \bar{\partial} \varphi)\left(\partial_{y_{\alpha}},-\partial_{x_{\beta}}\right)-2 \varepsilon^{2} \operatorname{Im}\left[\left((\partial \varphi)\left(\partial_{y_{\alpha}}\right)-\frac{1}{2} \varphi_{y_{\alpha}}\right) \cdot\left((\bar{\partial} \varphi)\left(-\partial_{x_{\beta}}\right)+\frac{i}{2} \varphi_{y_{\beta}}\right)\right] \\
& =-\frac{1}{2}\left(\varphi_{y_{\alpha} y_{\beta}}+\varphi_{x_{\alpha} x_{\beta}}\right)+\frac{1}{2} \varepsilon^{2} \varphi_{x_{\alpha}} \varphi_{x_{\beta}} .
\end{aligned}$$
This concludes the proof of the lemma. \(\square\)

So far we have described the restriction of the metric $g_{h}$ from the total space $L$ to the level sets $Y_{\varepsilon}$. We still need to calculate the $g_{h}$-unit normal of $Y_{\varepsilon}$ in the given coordinates on $L$. This turns out to be straightforward. The answer also tells us that the $g_{h}$-gradient of the function $\rho=-\sqrt{(n+1) / 2} \log x$ has constant length 1 , so in particular the leaves of our foliation are equidistant.

Lemma 2.3. The $g_{h}$-unit normal of $Y_{\varepsilon}$ pointing towards the cuspidal end is
$$\mathbf{n}=-\frac{\varepsilon^{-2}}{\sqrt{2(n+1)}} r \partial_{r} .$$
Here $r \partial_{r}=-J \partial_{\theta}$ is globally defined because $\partial_{\theta}$ generates the canonical $S^{1}$-action on $L$.
Proof. We first prove that $r \partial_{r}$ is $g_{h}$-orthogonal to the tangent space of $Y_{\varepsilon}$, which is locally spanned by the vector fields $\Pi_{*}\left(\partial_{\theta}\right), \Pi_{*}\left(\partial_{x_{\alpha}}\right), \Pi_{*}\left(\partial_{y_{\alpha}}\right)$ from the proof of Lemma 2.2. Indeed, by (2.9),
$$g_{h}\left(r \partial_{r}, \Pi_{*}\left(\partial_{\theta}\right)\right)=-\omega_{h}\left(\partial_{\theta}, \partial_{\theta}\right)=0 .$$
Secondly, by (2.11), (2.14) and (2.13), (2.10),
$$g_{h}\left(r \partial_{r}, \Pi_{*}\left(\partial_{x_{\alpha}}\right)\right)=\omega_{h}\left(\partial_{x_{\alpha}}+\frac{1}{2} \varphi_{x_{\alpha}} r \partial_{r}, \partial_{\theta}\right)=(n+1)\left(-\varepsilon^{4} \varphi_{x_{\alpha}}+\frac{1}{2} \varphi_{x_{\alpha}} \cdot 2 \varepsilon^{4}\right)=0,$$
and orthogonality to $\Pi_{*}\left(\partial_{y_{\alpha}}\right)$ is similar. Thus, $\mathbf{n}=f r \partial_{r}$ for some function $f$, where
$$1=\omega_{h}(\mathbf{n}, J \mathbf{n})=f^{2}(n+1) \tilde{\omega}_{h}\left(\partial_{\theta}, J \partial_{\theta}\right)=2(n+1) \varepsilon^{4} f^{2}$$
again thanks to (2.10). \(\square\)

The following lemma is not necessary for this paper but we find it helpful for intuition. It says that the orbits of the unit normal field n of our foliation are geodesics and the leaves have constant mean curvature independent of $\varepsilon$. This also holds if $D$ is a non-flat Calabi-Yau manifold. If $D$ is flat, these are well-known properties of the universal covers of the leaves, which are horospheres in $\mathbb{C} H^{n}$.

Lemma 2.4. We have $\nabla_{\mathbf{n}} \mathbf{n}=0$ and the mean curvature of $Y_{\varepsilon}$ with respect to $\mathbf{n}$ is $-n / \sqrt{2(n+1)}$.
Proof. Replacing $\varepsilon^{-2}=\sigma$ in (2.19), differentiating, and using that $\left(r \partial_{r}\right)(\sigma)=-2$, we get
$$2(n+1) \nabla_{\mathbf{n}} \mathbf{n}=-2 \sigma r \partial_{r}+\sigma^{2} \nabla_{r \partial_{r}}\left(r \partial_{r}\right) .$$
On the other hand, $\left\langle\nabla_{\mathbf{n}} \mathbf{n}, \mathbf{n}\right\rangle=0$. Thus, it suffices to prove that $\nabla_{r \partial_{r}}\left(r \partial_{r}\right)$ is orthogonal to the tangent space of $Y_{\varepsilon}$. For this, note that $r \partial_{r}$ is a holomorphic vector field, so its covariant derivative is $J$-linear. Because $\nabla J=0$, we conclude that $\nabla_{r \partial_{r}}\left(r \partial_{r}\right)=-\nabla_{\partial_{\theta}} \partial_{\theta}$, so it suffices to prove that $\left\langle\nabla_{\partial_{\theta}} \partial_{\theta}, \mathbf{t}\right\rangle=0$ for all vectors t tangent to $Y_{\varepsilon}$. This can be done as follows. Since $\partial_{\theta}$ is a Killing vector field,
$$\left\langle\nabla_{\partial_{\theta}} \partial_{\theta}, \mathbf{t}\right\rangle=-\left\langle\nabla_{\mathbf{t}} \partial_{\theta}, \partial_{\theta}\right\rangle=-\frac{1}{2} \mathbf{t}\left\langle\partial_{\theta}, \partial_{\theta}\right\rangle=-(n+1) \mathbf{t}\left(\sigma^{2}\right)=0,$$
as desired, using also (2.10). This proves that $\nabla_{\mathbf{n}} \mathbf{n}=0$.
Next, we compute the mean curvature of $Y_{\varepsilon}$. The unoriented area element of $Y_{\varepsilon}$ is
$$d A=\sqrt{\operatorname{det}\left(\left.g_{h}\right|_{Y_{\varepsilon}}\right)} d \theta d x_{\alpha} d y_{\alpha}=(n+1)^{\frac{n-1}{2}} \varepsilon^{n-1} \sqrt{\operatorname{det}\left(g_{\varepsilon}\right)} d \theta d x_{\alpha} d y_{\alpha} .$$
By (2.8) and column operations, $\operatorname{det}\left(g_{\varepsilon}\right)$ equals the determinant of
$$\left(\begin{array}{ccc}
-\frac{1}{2}\left(\varphi_{x_{\alpha} x_{\beta}}+\varphi_{y_{\alpha} y_{\beta}}\right) & -\frac{1}{2}\left(\varphi_{x_{\alpha} y_{\beta}}-\varphi_{y_{\alpha} x_{\beta}}\right) & \varepsilon^{2} \varphi_{y_{\alpha}} \\
-\frac{1}{2}\left(\varphi_{y_{\alpha} x_{\beta}}-\varphi_{x_{\alpha} y_{\beta}}\right) & -\frac{1}{2}\left(\varphi_{y_{\alpha} y_{\beta}}+\varphi_{x_{\alpha} x_{\beta}}\right) & -\varepsilon^{2} \varphi_{x_{\alpha}} \\
0 & 0 & 2 \varepsilon^{2}
\end{array}\right),$$
which equals $\varepsilon^{2} f\left(x_{\alpha}, y_{\alpha}\right)$ with $f$ smooth and independent of $\varepsilon$. Thus,
$$\frac{\mathcal{L}_{\mathbf{n}} d A}{d A}=\frac{\mathbf{n}\left(\sigma^{-\frac{n}{2}}\right)}{\sigma^{-\frac{n}{2}}}=\frac{\frac{n}{2} \cdot\left(r \partial_{r}\right)(\sigma)}{\sqrt{2(n+1)}}=-\frac{n}{\sqrt{2(n+1)}},$$
and this is the mean curvature of $Y_{\varepsilon}$ with respect to $\mathbf{n}$. \(\square\)
2.2. The model operator. We now compute the linearization of the Monge-Ampère operator at our model metric $\omega_{h}$. With $\left(g_{j \bar{k}}\right)$ as in (2.5), this is the operator
$$L_{h}(u):=\left.\frac{d}{d t}\right|_{t=0} \frac{\left(\omega_{h}+i \partial \bar{\partial}(t u)\right)^{n}}{e^{t u} \omega_{h}^{n}}=g^{\bar{k} j} u_{j \bar{k}}-u .$$
Fix any local holomorphic chart $\left(z^{\prime}, z_{n}\right)$ on the total space as in Section 2.1, so that $h=e^{-\varphi\left(z^{\prime}\right)}\left|z_{n}\right|^{2}$. Consider the associated smooth chart $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$, where $x=\frac{1}{\sigma}$. In this chart, we can still define the complex partials $u_{\alpha}=\partial_{z_{\alpha}} u$ and $u_{\bar{\alpha}}=\partial_{\bar{z}_{\alpha}} u$ in the usual way for all $\alpha \in\{1, \ldots, n-1\}$.

Lemma 2.5. In any chart $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$ as above, the linearized operator is given by
$$\begin{array}{r}
L_{h}(u)=\frac{1}{n+1}\left(x^{2} u_{x x}+(n+1) x u_{x}-(n+1) u-x^{-1} \varphi^{\bar{\beta} \alpha} u_{\alpha \bar{\beta}}+(2 x)^{-2} u_{\theta \theta}\right)+F, \\
F=F\left(x_{\alpha}, y_{\alpha}, x^{-1} u_{\theta \alpha}, x^{-1} u_{\theta \bar{\alpha}}, x^{-1} u_{\theta \theta}\right),
\end{array}$$
where $F$ is smooth in $x_{\alpha}, y_{\alpha}$ and linear homogeneous in the other arguments.

Proof. In the chart $\left(z^{\prime}, z_{n}\right)$, the definition (2.28) of $L_{h}$ can be expanded into
$$L_{h}(u)=g^{\bar{k} j} u_{j \bar{k}}-u=g^{\bar{\beta} \alpha} u_{\alpha \bar{\beta}}+2 \operatorname{Re}\left(g^{\bar{\alpha} n} u_{\bar{\alpha} n}\right)+g^{\bar{n} n} u_{n \bar{n}}-u .$$
With $Q:=\varphi^{\bar{\beta} \gamma} \varphi_{\bar{\beta}} \varphi_{\gamma}$, the inverse of the metric tensor is given for $\alpha, \beta \in\{1, \ldots, n-1\}$ by
$$g^{\bar{\beta} \alpha}=-\frac{\varphi^{\bar{\beta} \alpha}}{(n+1) x}, g^{\bar{\alpha} n}=-\frac{\varphi^{\bar{\alpha} \gamma} \varphi_{\gamma} z_{n}}{(n+1) x}, g^{\bar{n} n}=\frac{r^{2}(1-Q x)}{(n+1) x^{2}} .$$
This can be checked by direct multiplication, using (2.5).
Consider the change of coordinates $\left(z^{\prime}, z_{n}\right) \mapsto\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$. A simple calculation shows that
$$\partial_{z_{\alpha}} \mapsto \partial_{z_{\alpha}}-x^{2} \varphi_{\alpha} \partial_{x}, \quad \partial_{z_{n}} \mapsto \frac{x^{2}}{z_{n}} \partial_{x}-\frac{i}{2 z_{n}} \partial_{\theta} .$$
Thus, under the new coordinates $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$,
$$\begin{aligned}
(n+1) g^{\bar{\beta} \alpha} u_{\alpha \bar{\beta}} & =-x^{-1} \varphi^{\bar{\beta} \alpha}\left(\partial_{z_{\alpha}}-x^{2} \varphi_{\alpha} \partial_{x}\right)\left(u_{\bar{\beta}}-x^{2} \varphi_{\bar{\beta}} u_{x}\right) \\
& =-x^{-1} \varphi^{\bar{\beta} \alpha} u_{\alpha \bar{\beta}}+(n-1) x u_{x}+x \varphi^{\bar{\beta} \alpha}\left(\varphi_{\alpha} u_{x \bar{\beta}}+\varphi_{\bar{\beta}} u_{x \alpha}\right)-\underline{\underline{Q}\left(x^{3} u_{x x}+2 x^{2} u_{x}\right)} .
\end{aligned}$$
Similarly, with $F_{1}$ as in the statement of the lemma,
$$\begin{aligned}
(n+1) g^{\bar{\alpha} n} u_{n \bar{\alpha}} & =-\frac{z_{n}}{x} \varphi^{\bar{\alpha} \gamma} \varphi_{\gamma}\left(\frac{x^{2}}{z_{n}} \partial_{x}-\frac{i}{2 z_{n}} \partial_{\theta}\right)\left(u_{\bar{\alpha}}-x^{2} \varphi_{\bar{\alpha}} u_{x}\right) \\
& =-x \varphi^{\bar{\alpha} \gamma} \varphi_{\gamma} u_{x \bar{\alpha}}+\underline{\underline{Q\left(x^{3} u_{x x}+2 x^{2} u_{x}\right)}}-\frac{i}{2} Q x u_{x \theta}+F_{1}\left(x_{\alpha}, y_{\alpha}, x^{-1} u_{\theta \bar{\alpha}}\right) .
\end{aligned}$$
The last contribution is slightly more complicated:
$$\begin{aligned}
(n+1) g^{\bar{n} n} u_{n \bar{n}} & =\frac{r^{2}}{x^{2}}(1-Q x)\left(\frac{x^{2}}{z_{n}} \partial_{x}-\frac{i}{2 z_{n}} \partial_{\theta}\right)\left(\frac{x^{2}}{\bar{z}_{n}} u_{x}+\frac{i}{2 \bar{z}_{n}} u_{\theta}\right) \\
& =x^{2} u_{x x}+2 x u_{x}+(2 x)^{-2} u_{\theta \theta}-\underline{Q\left(x^{3} u_{x x}+2 x^{2} u_{x}\right)}+F_{2}\left(x_{\alpha}, y_{\alpha}, x^{-1} u_{\theta \theta}\right) .
\end{aligned}$$
The delicate part here is the coefficients of $u_{x}$ and $u_{\theta}$, which arise as follows:
$$\frac{r^{2}}{x^{2}}\left(\frac{x^{2}}{z_{n}} \partial_{x}-\frac{i}{2 z_{n}} \partial_{\theta}\right)\left(\frac{x^{2}}{\bar{z}_{n}}\right)=\frac{r^{2}}{x^{2}} \partial_{z_{n}}\left(\frac{x^{2}}{\bar{z}_{n}}\right)=\frac{r^{2}}{x^{2}} \frac{1}{\bar{z}_{n}} \partial_{z_{n}}\left(\varphi-\log \left|z_{n}\right|^{2}\right)^{-2}=2 x$$
for $u_{x}$, and similarly the coefficient of $u_{\theta}$ vanishes.
When we add the contributions of (2.33), (2.34) and (2.35) according to (2.30), the boxed and the underlined terms cancel. Cancellation of the boxed terms will be important in Section 4. \(\square\)
2.3. Results of Datar-Fu-Song. In the setting of the Main Theorem, consider a member $h$ of the canonical 1-parameter family of Hermitian metrics on $L \rightarrow D$ and its associated model metric $\omega_{h}$. For any tubular neighborhood $V$ of the zero section $D \subset L$ of the form $V=\{h \leqslant \delta\}$ for some $\delta \in(0,1)$, a special case of Datar-Fu-Song [7, Thm 4.1] says that for all $\beta \in C^{\infty}(\partial V)$, the Dirichlet problem
$$\begin{array}{r}
\left(\omega_{h}+i \partial \bar{\partial} u\right)^{n}=e^{u} \omega_{h}^{n} \text { on } V \backslash D, \\
u=\beta \text { on } \partial V,
\end{array}$$
has a smooth solution $u$ such that the Kähler-Einstein metric $\omega_{h}+i \partial \bar{\partial} u$ on $V \backslash D$ is complete.
Conversely assume that for some closed tubular neighborhood $U$ of the zero section, there exists a Kähler-Einstein metric $\omega$ on $U \backslash D$ such that $\operatorname{Ric}(\omega)=-\omega$. Thanks to the Kähler-Einstein equation, we have that $\omega=\omega_{h}+i \partial \bar{\partial} u$, where $u$ is the log volume ratio of the two metrics. Equivalently,
$$\left(\omega_{h}+i \partial \bar{\partial} u\right)^{n}=e^{u} \omega_{h}^{n} .$$

Then the following result is a special case of [7, Thm 1.3]. This still holds in the unbounded curvature setting where $D$ is a non-flat Calabi-Yau manifold.

Theorem 2.6. If $\omega$ is complete, then there exists a constant $C$ such that for all $0<\eta \leqslant 1$ we have that $|u(p)| \leqslant C \eta$ for all $p \in U \backslash D$ such that $\operatorname{dist}_{\omega_{h}}(p, \partial U) \geqslant \eta^{-1}$ and $\operatorname{dist}_{\omega}(p, \partial U) \geqslant \eta^{-1}$.

In particular, the maximum principle can now be applied to prove that $u$ is the unique solution to the Dirichlet problem (2.37) such that $\omega_{h}+i \partial \bar{\partial} u$ is complete, where $\beta$ is defined to be the restriction of $u$ to $\partial V$ for any $V$ as above such that $V \subset U$. This completeness assumption cannot be dropped, and (2.38) does not guarantee by itself that $u$ is bounded, as the following example shows.

Example 2.7. We use the Calabi ansatz to construct Kähler-Einstein metrics on $V \backslash D=\{0<h \leqslant \delta\}$ for some $\delta>0$. Let $\omega=i \partial \bar{\partial} \psi(-\sigma)$, where $\psi:(-\infty, \log \delta] \rightarrow \mathbb{R}$ is smooth. Then $\omega$ is positive definite if and only if $\psi^{\prime}>0$ and $\psi^{\prime \prime}>0$, and the equation $\operatorname{Ric}(\omega)=-\omega$ is equivalent to
$$\left(\psi^{\prime}\right)^{n-1} \psi^{\prime \prime}=e^{\psi+a}$$
for some constant $a \in \mathbb{R}$. Our standard solutions $\omega=\omega_{\lambda h}\left(\lambda \in \mathbb{R}^{+}\right)$in this paper correspond to
$$\psi(t)=-(n+1) \log (-(t+\log \lambda)), e^{a}=(n+1)^{n},$$
for $\delta \in\left(0, \frac{1}{\lambda}\right)$. However, there do exist other solutions which are defined on all of $V \backslash D$.
In fact, by multiplying (2.39) by $\psi^{\prime}>0$ and integrating, we see that (2.39) is equivalent to
$$\frac{1}{n+1}\left(\psi^{\prime}\right)^{n+1}=e^{\psi+a}+b$$
for some constant $b \in \mathbb{R}$. This is in turn equivalent to
$$\int_{\psi(t)}^{\psi\left(t_{0}\right)}\left(e^{\xi+a}+b\right)^{-\frac{1}{n+1}} d \xi=(n+1)^{\frac{1}{n+1}}\left(t_{0}-t\right)$$
for all $t \leqslant t_{0}$ such that $\psi$ exists on $\left[t, t_{0}\right]$ and $e^{\psi+a}+b$ is strictly positive. If $b=0$, then (2.42) implies (2.40) up to an additive constant. For $b<0$, the integral in (2.42) is uniformly bounded independently of $\psi(t)$, so the interval of allowed $t$-values has a finite lower bound. For $b>0$, this obstruction does not arise, so $\psi$ exists on $(-\infty, \log \delta]$ for some $\delta>0$ and $\psi^{\prime}>c:=((n+1) b)^{1 /(n+1)}>0$ and $\psi^{\prime \prime}>0$.

The property $\psi^{\prime}>c$ together with the mean value theorem tells us that $\psi(t) \leqslant \psi\left(t_{0}\right)+c\left(t-t_{0}\right)$ for all $t \leqslant t_{0}$. Then (2.39) implies $\psi^{\prime \prime}(t)=O\left(e^{c t}\right)$ and (2.41) implies $\psi^{\prime}(t)-c=O\left(e^{c t}\right)$ as $t \rightarrow-\infty$. Using this, one can check that $(V \backslash D, \omega)$ has finite diameter. In fact, $\omega$ defines a singular metric on $V$ with conical singularities along $D$, where $D$ has diameter proportional to $\sqrt{c}$ and the cone angle is $2 \pi c$. To see that the angle is exactly $2 \pi c$, notice that $\psi^{\prime}(t)=c+O\left(e^{c t}\right)$ implies $\psi(t)=c t+d+O\left(e^{c t}\right)$ for some constant $d \in \mathbb{R}$, and then $\psi^{\prime \prime}(t)$ is asymptotic to a constant multiple of $e^{c t}$ by (2.39).

Corollary 2.8. If $\omega$ is complete and if in addition $\sup _{U \backslash D}|\omega|_{\omega_{h}}<\infty$, then $\omega$ is uniformly equivalent to $\omega_{h}$ and we have that $|u|=O\left((-\log x)^{-1}\right)$ as $x \rightarrow 0^{+}$.

Proof. By Theorem 2.6, $u$ is bounded, i.e., the volume forms $\omega_{h}^{n}$ and $\omega^{n}$ are uniformly comparable to each other. Since $|\omega|_{\omega_{h}}$ is bounded, it follows that $\omega$ and $\omega_{h}$ are themselves uniformly equivalent. Then $|u(p)|=O\left((-\log x(p))^{-1}\right)$ follows for all $p \in U \backslash D$ by taking $\eta$ in Theorem 2.6 to be comparable to $(-\log x(p))^{-1}$ because the gradient of $-\log x(\cdot)$ has constant $\omega_{h}$-length by Lemma 2.4. \(\square\)

If $D$ is a finite quotient of a complex torus, then the bound $\sup _{U \backslash D}|\omega|_{\omega_{h}}<\infty$ can actually be proved [7, 14], which is also the reason why the Dirichlet problem (2.37) can be proved to admit a complete solution in this case [7]. Applying the standard local regularity theory of the complex Monge-Ampère equation in quasi-coordinates [5], we thus obtain the following slight refinement of [7, Thm 1.4].

Theorem 2.9. If $D$ is a finite quotient of a torus and if $\omega$ is complete, then $\omega$ is uniformly equivalent to $\omega_{h}$ and we have for all $k \in \mathbb{N}_{0}$ that $\left|\nabla_{\omega_{h}}^{k} u\right|_{\omega_{h}}=O_{k}\left((-\log x)^{-1}\right)$ as $x \rightarrow 0^{+}$.

\section*{3. Expansion according to powers of $x$}

Assume the same setup as in the Main Theorem. Since $\omega_{h}$ and $\omega$ are Kähler-Einstein with the same Einstein constant, it follows that $\omega=\omega_{h}+i \partial \bar{\partial} u$, where $u$ is the log volume ratio. Since $\omega$ is complete, it follows from Theorem 2.9 that $|u|=O\left((-\log x)^{-1}\right)$ with all derivatives. Also, by definition,
$$\left(\omega_{h}+i \partial \bar{\partial} u\right)^{n}=e^{u} \omega_{h}^{n} .$$
In this section we prove the following theorem, which is our first step towards the Main Theorem.
Theorem 3.1. There exists a constant $c \in \mathbb{R}$ such that
$$u+(n+1) \log (1+c x)=O\left(x^{\infty}\right) .$$

The proof will be given in Section 3.2 after some preliminary estimates in Section 3.1.
Note that if (3.2) holds in the pointwise sense, then it automatically holds for all derivatives. This follows from the classical regularity theory of the Monge-Ampère equation. For this it actually suffices to work at the scale of the injectivity radius because the constants in the elliptic estimates only blow up like fixed negative powers of $x$ even at this scale. However, during the proof of Theorem 3.1, it is helpful to work with a more specific $O$ notation, which we will now define; cf. [12, Thm 1.1].

Definition 3.2. After shrinking $U$ if necessary, choose a finite cover of $U \backslash D$ by charts $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$ as in Sections 2.1-2.2. Given this, we say that a function $f \in C^{\infty}(U \backslash D)$ is $\mathbf{O}\left(x^{k}\right)$ for some $k \in \mathbb{R}$ if, under all local charts of this cover, for all $c \in \mathbb{N}_{0}$ there exists a constant $C$ such that
$$\left|x^{c} \partial_{x}^{c} f\right| \leqslant C x^{k},$$
and for all $a, b, c, d, N \in \mathbb{N}_{0}$ with $a+b+d \geqslant 1$ there exists a constant $C^{\prime}$ such that
$$\left|\partial_{x^{\alpha}}^{a} \partial_{y^{\alpha}}^{b} \partial_{x}^{c} \partial_{\theta}^{d} f\right| \leqslant C^{\prime} x^{N} .$$
3.1. Preliminary estimates. We begin by proving that $|u|=O(x)$ as $x \rightarrow 0^{+}$. This bound is sharp because $x$ is the unique decaying radial solution to the homogeneous linearized PDE, as one can easily check using Lemma 2.5. Our proof uses a barrier argument as in [12, Lemma 2.2], and this argument would go through for an arbitrary compact Calabi-Yau manifold $D$.

Lemma 3.3. Assuming only that $|u|=o(1)$ as $x \rightarrow 0^{+}$, we obtain that $|u|=O(x)$.
Proof. Define $U_{\delta}=\{0<x \leqslant \delta\} \subset L \backslash D$ with $\delta \in(0,1)$ small enough so that $U_{\delta} \subset U \backslash D$. We will prove the lemma in two steps, using a suitable barrier function in each step. The key is that $x^{1-\varepsilon}$ is a supersolution of the linearized operator $L_{h}$ for all $\varepsilon \in(0,1)$ (in fact, for all $\varepsilon \in(0, n+2)$, but we are only interested in functions that go to zero as $x \rightarrow 0^{+}$) and $x^{1+\varepsilon}$ is a subsolution for all $\varepsilon>0$.

In the first step, we consider the barrier $B:=x^{1-\varepsilon}$ for an arbitrary but fixed $\varepsilon \in(0,1)$. Let
$$a_{\delta}:=\max _{\partial U_{\delta}} \frac{|u|}{B}=o\left(\delta^{\varepsilon-1}\right) \text { as } \delta \rightarrow 0 .$$
Then $u-a_{\delta} B \leqslant 0$ on $\partial U_{\delta}$. We now prove that $u-a_{\delta} B \leqslant 0$ on $U_{\delta}$ if $\delta$ is small. If this was false, then, because $u=o(1)$ as $x \rightarrow 0^{+}$, for arbitrarily small values of $\delta$ there would exist a point $p_{\delta} \in \operatorname{int} U_{\delta}$ such that $u-a_{\delta} B$ attains a positive global maximum at $p_{\delta}$. Thus, at $p_{\delta}$,
$$0=\log \left(\frac{\left(\omega_{h}+i \partial \bar{\partial} u\right)^{n}}{\omega_{h}^{n}}\right)-u<\log \left(\frac{\left(\omega_{h}+i \partial \bar{\partial}\left(a_{\delta} B\right)\right)^{n}}{\omega_{h}^{n}}\right)-a_{\delta} B .$$

Now $|i \partial \bar{\partial} B|_{\omega_{h}}=c B$ for some constant $c=c(n, \varepsilon)$, so by (3.5) we have $\left|i \partial \bar{\partial}\left(a_{\delta} B\right)\right|_{\omega_{h}}=o\left(\delta^{\varepsilon-1}\right) B=o(1)$ uniformly on $U_{\delta}$ as $\delta \rightarrow 0$. This allows us to linearize the right-hand side of (3.6) if $\delta$ is small enough. Thus, there exists a constant $C=C(n)$ such that if $\delta$ is small, then, uniformly on $U_{\delta}$,
$$\begin{aligned}
\log \left(\frac{\left(\omega_{h}+i \partial \bar{\partial}\left(a_{\delta} B\right)\right)^{n}}{\omega_{h}^{n}}\right)-a_{\delta} B & \leqslant L_{h}\left(a_{\delta} B\right)+C\left|i \partial \bar{\partial}\left(a_{\delta} B\right)\right|_{\omega_{h}}^{2} \\
& =-\varepsilon(n+2-\varepsilon)\left(a_{\delta} B\right)+c^{2} C\left(a_{\delta} B\right)^{2} .
\end{aligned}$$
Again because $\sup _{U_{\delta}}\left(a_{\delta} B\right)=o(1)$ as $\delta \rightarrow 0$, this is eventually nonpositive on all of $U_{\delta}$, contradicting (3.6) at $p_{\delta}$. Thus, fixing $\delta$ small enough depending on $u, n, \varepsilon$, we have that $u \leqslant a_{\delta} x^{1-\varepsilon}$ on $U_{\delta}$.

A lower bound can be proved in the same way. The only difference is that the uniform smallness of $a_{\delta} B$ on $U_{\delta}$ is then also needed to ensure that $\omega_{h}-i \partial \bar{\partial}\left(a_{\delta} B\right)>0$. Notice also that, in the proof of the upper bound, the quadratic terms on the right-hand side of (3.7) were actually unnecessary because the Monge-Ampère operator is concave, but they are necessary in the proof of the lower bound.

In the second step, we carry out the same argument using $B:=x-x^{1+\varepsilon}$ as a barrier for any fixed $\varepsilon \in(0,1)$. This is a positive supersolution to $L_{h}$ on $U_{\delta}$ for all $\varepsilon>0$ because $x$ is a solution and $x^{1+\varepsilon}$ is a subsolution. The only difference to the first step is that the good linear term on the right-hand side of (3.7) is now comparable to $x^{\varepsilon}\left(a_{\delta} B\right)$, but the nonlinearities are still only bounded by $\left(a_{\delta} B\right)^{2}$. Thus, we can complete the argument only if we know that $\sup _{U_{\delta}}\left(x^{-\varepsilon}\left(a_{\delta} B\right)\right)=o(1)$ as $\delta \rightarrow 0$. But this is true as long as $\varepsilon<1$. The reason is that $|u|=O\left(x^{\mu}\right)$ as $x \rightarrow 0^{+}$for all $\mu \in(0,1)$ from the first step, which implies $a_{\delta}=\max _{\partial U_{\delta}}(|u| / B)=O\left(\delta^{\mu-1}\right)$ as $\delta \rightarrow 0$. Thus, it suffices to choose $\mu \in(\varepsilon, 1)$. \(\square\)

Sharp higher-order bounds for $u$ are now almost immediate as in [12, Lemma 2.4]. Here we use the flatness of $D$ although it seems likely that this can be avoided using the methods of [11].

Lemma 3.4. Assuming only that $|u|=O(x)$ as $x \rightarrow 0^{+}$and that $\omega$ is uniformly equivalent to $\omega_{h}$, we obtain that $\left|\nabla_{\omega_{h}}^{k} u\right|_{\omega_{h}}=O_{k}(x)$ for all $k \in \mathbb{N}$.

Proof. Shrinking $U$ slightly if necessary, we can assume that $\partial U=\{h=\delta\}$ for some $\delta \in(0,1)$.
Consider a local chart $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$ on $U \backslash D$ as in Sections 2.1-2.2. Thus, for some $p \in D \subset U$, we have local holomorphic coordinates $\left(z^{\prime}, z_{n}\right)$ on $U$ mapping $p$ to $0 \in \mathbb{C}^{n}$ such that the bundle projection $\pi$ is given by $z \mapsto z^{\prime}=\left(z_{1}, \ldots, z_{n-1}\right)$. In terms of these coordinates, $x_{\alpha}=\operatorname{Re}\left(z_{\alpha}\right)$ and $y_{\alpha}=\operatorname{Im}\left(z_{\alpha}\right)$ for all $\alpha \in\{1, \ldots, n-1\}$, and $z_{n}=r e^{i \theta}$ and $x=(-\log h)^{-1}=\left(\varphi\left(z^{\prime}\right)-\log r^{2}\right)^{-1}$.

Because $D$ is flat, there exists a holomorphic covering map $\mathbb{C}^{n-1} \rightarrow D$. The line bundle $L$ becomes holomorphically trivial after pulling back under this map. We can then assume that $z^{\prime}$ is the standard coordinate vector on $\mathbb{C}^{n-1}$ and that $L$ has been trivialized in such a way that $\varphi\left(z^{\prime}\right)$ is a homogeneous quadratic polynomial. Moreover, after passing to the universal cover of the set $\left\{z_{n} \neq 0\right\}$, we may view $\theta$ as a globally defined function. In this way, we realize the universal cover of $U \backslash D$ as a subset of $\mathbb{C}^{n}$ with holomorphic coordinates $\left(z^{\prime}, w\right)$, where $w:=\log r+i \theta$. We also get a smooth chart $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$ identifying the universal cover of $U \backslash D$ with $\mathbb{R}^{2 n-2} \times\left(0, x_{\delta}\right] \times \mathbb{R}$, where $x_{\delta}:=(-\log \delta)^{-1}$.

Fix $q \in U \backslash D$ such that $c_{n} x(q)<x_{\delta}$, where $c_{n}:=\exp (\sqrt{2 /(n+1)})$. Let $B_{1}(q)$ be the Riemannian unit ball with respect to $\omega_{h}$ centered at $q$. Then, using our distance function $\rho$ from (2.1),
$$B_{1}(q) \subset\{\rho(q)-1<\rho<\rho(q)+1\}=\left\{c_{n}^{-1} x(q)<x<c_{n} x(q)\right\} \subset U \backslash D .$$
On the universal cover of $U \backslash D$, we define a new chart via
$$\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{x}, \check{\theta}\right):=\left(x(q)^{\frac{1}{2}} x_{\alpha}, x(q)^{\frac{1}{2}} y_{\alpha}, x(q)^{-1} x, x(q) \theta\right) .$$
Then, on the preimage of $B_{1}(q)$, uniformly as $x(q) \rightarrow 0^{+}$, the Riemannian metric associated with $\omega_{h}$ is $C^{\infty}$ equivalent to the standard Euclidean metric in the chart $\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{x}, \check{\theta}\right)$. This is easy to check using Lemmas 2.2-2.3, equation (3.8), and the fact that $\varphi\left(z^{\prime}\right)$ is a homogeneous quadratic polynomial.

We also introduce new holomorphic coordinates
$$\check{z}_{\alpha}:=x(q)^{\frac{1}{2}} z_{\alpha}=\check{x}_{\alpha}+i \check{y}_{\alpha}, \quad \check{w}:=x(q) w=\frac{1}{2}\left(\varphi\left(\check{z}^{\prime}\right)-\frac{1}{\check{x}}\right)+i \check{\theta} .$$
Using indices with respect to $\left(\check{z}^{\prime}, \check{w}\right)$, the Monge-Ampère equation (3.1) can be written as
$$\int_{0}^{1}\left(\omega_{h}+t i \partial \bar{\partial} u\right)^{\bar{k} j} d t \cdot \partial_{j} \partial_{\bar{k}} u=u$$
on a fixed ball in $\mathbb{C}^{n}$, where the coefficient matrix of $\omega_{h}$ is uniformly comparable to the identity to all orders. Since $\omega=\omega_{h}+i \partial \bar{\partial} u$ is uniformly equivalent to $\omega_{h}$ and $|u|$ is in particular $O(1)$, the standard theory of the Monge-Ampère equation now tells us that $u$ is bounded to all orders. Using this and the fact that $|u|=O(x)$, the lemma follows from Schauder theory applied to (3.11). \(\square\)

By interpolation, we will now show that all derivatives of $u$ with at least one $x_{\alpha}, y_{\alpha}, \theta$-direction are actually $O\left(x^{\infty}\right)$ because all of these directions are small under our metric $\omega_{h}$. For this and for the rest of the paper, it is helpful to directly prove an even stronger estimate in the $\theta$-directions. We do this using an argument similar to [10, Prop 2.9(i)], which does not rely on the flatness of $D$.

Lemma 3.5. Assuming only that $\left|\nabla_{\omega_{h}} u\right|_{\omega_{h}}=O(x)$ as $x \rightarrow 0^{+}$and that $\omega$ is uniformly equivalent to $\omega_{h}$, we obtain an $\varepsilon>0$ such that $\left|\nabla_{\omega_{h}}^{k}\left(\mathcal{L}_{\partial_{\theta}} u\right)\right|_{\omega_{h}}=O_{k}\left(e^{-\varepsilon / x}\right)$ for all $k \in \mathbb{N}_{0}$.

Proof. Recall that $\partial_{\theta}$ is a globally defined holomorphic vector field with $\mathcal{L}_{\partial_{\theta}} \omega_{h}=0$. Define $v=\mathcal{L}_{\partial_{\theta}} u$. Applying the operator $\mathcal{L}_{\partial_{\theta}}$ to the Monge-Ampère equation (3.1), we thus obtain that
$$\Delta_{\omega} v=v,$$
where $\omega=\omega_{h}+i \partial \bar{\partial} u$ is by assumption uniformly equivalent to $\omega_{h}$.
The first step is to prove that $v \in H^{1}\left(U \backslash D, \omega_{h}\right)$. We have $|v|=O\left(x^{2}\right)$ because $\left|\nabla_{\omega_{h}} u\right|_{\omega_{h}}=O(x)$ and $\left|\partial_{\theta}\right|_{\omega_{h}}=O(x)$. Thus, $v \in L^{2}\left(U \backslash D, \omega_{h}\right)$ because $\operatorname{Vol}\left(U \backslash D, \omega_{h}\right)<\infty$. It is also not difficult to estimate the gradient of $v$ with respect to $\omega_{h}$. For example, this can easily be done using quasi-coordinates as in the proof of Lemma 3.4. The following method also works if $D$ is not flat. Assume that $\partial U=\left\{\rho=\rho_{0}\right\}$ for some $\rho_{0}>0$. For $k \in \mathbb{N}, k \geqslant \rho_{0}+1$, take a cutoff function $\eta_{k}=\eta_{k}(\rho)$ that equals 1 for $\rho_{0} \leqslant \rho \leqslant k$ and 0 for $\rho \geqslant k+1$, with $\left|\nabla_{\omega_{h}} \eta_{k}\right|_{\omega_{h}} \leqslant 2$. Then, by (3.12),
$$\int_{U \backslash D} \eta_{k}^{2} v \Delta_{\omega} v d V_{\omega}=\int_{U \backslash D} \eta_{k}^{2} v^{2} d V_{\omega} .$$
By integration by parts,
$$\int_{U \backslash D} \eta_{k}^{2} v \Delta_{\omega} v d V_{\omega}=-\int_{U \backslash D} \eta_{k}^{2}\left|\nabla_{\omega} v\right|_{\omega}^{2} d V_{\omega}-\int_{U \backslash D} 2 \eta_{k} v\left\langle\nabla_{\omega} \eta_{k}, \nabla_{\omega} v\right\rangle_{\omega} d V_{\omega} .$$
After combining (3.13)-(3.14) and applying Cauchy-Schwarz in the obvious way, we can replace $\omega$ by $\omega_{h}$ because $\omega$ is uniformly equivalent to $\omega_{h}$. Letting $k \rightarrow \infty$, we obtain the desired $H^{1}$ bound.

For the main step of the proof, define $U_{\rho}=\{q \in U \backslash D: \rho(q) \geqslant \rho\}$. Then, by (3.12),
$$E(\rho):=\int_{U_{\rho}}\left(\left|\nabla_{\omega} v\right|_{\omega}^{2}+v^{2}\right) d V_{\omega}=-\int_{\partial U_{\rho}} v \mathbf{n}_{\omega}(v) d A_{\omega},$$
where $\mathbf{n}_{\omega}$ denotes the $\omega$-unit normal of $\partial U_{\rho}$ pointing towards the cuspidal end. Thus,
$$E(\rho) \leqslant\left(\int_{\partial U_{\rho}} v^{2} d A_{\omega}\right)^{\frac{1}{2}}\left(\int_{\partial U_{\rho}}\left(\mathbf{n}_{\omega}(v)\right)^{2} d A_{\omega}\right)^{\frac{1}{2}} .$$
We will now develop a Poincaré inequality to deal with the first factor.

By Lemma 2.2, the restriction of $g_{h}$ to $Y:=\partial U_{\rho}$ is given by
$$\left.g_{h}\right|_{Y}=2(n+1) x\left(g_{D}+x \alpha^{2}\right),$$
where $\rho=-\sqrt{(n+1) / 2} \log x$ as usual, $g_{D}$ is a fixed metric on $D$ pulled back under the $S^{1}$-orbit map $Y \rightarrow D$, and $\alpha:=d \theta-\frac{1}{2} d^{c} \varphi$ is an $S^{1}$-connection form, i.e., $\alpha\left(\partial_{\theta}\right)=1$ and $\mathcal{L}_{\partial_{\theta}} \alpha=0$. The $S^{1}$-action preserves the metric $g:=g_{D}+x \alpha^{2}$, so all eigenspaces of the Laplacian of $g$ are $S^{1}$-invariant. Thus, by the representation theory of $S^{1}$, every eigenspace $E=\left\{\phi \in L^{2}(Y, \mathbb{R}): \Delta_{g} \phi=-\lambda \phi\right\}$ can be written as the $L^{2}$-orthogonal sum of a space $E_{0}$ of $S^{1}$-invariant functions and of planes $\mathbb{R} \phi_{1}+\mathbb{R} \phi_{2}$, where $\phi_{1}, \phi_{2}$ are $L^{2}$-orthonormal and $\mathcal{L}_{\partial_{\theta}} \phi_{1}=-k \phi_{2}, \mathcal{L}_{\partial_{\theta}} \phi_{2}=k \phi_{1}$ for some $k \in \mathbb{N}_{\geqslant 1}$. Then, for all $\phi \in E$,
$$\lambda \int_{Y} \phi^{2}=\int_{Y}|\nabla \phi|^{2} \geqslant \int_{Y}\left(\mathcal{L}_{x^{-1 / 2} \partial_{\theta}} \phi\right)^{2}=x^{-1} \int_{Y}\left(\mathcal{L}_{\partial_{\theta}} \phi\right)^{2} \geqslant x^{-1} \int_{Y}\left(\operatorname{proj}_{E_{0}^{\perp}} \phi\right)^{2},$$
where all metric quantities are understood in terms of $g$. The first inequality holds because $x^{-1 / 2} \partial_{\theta}$ is a $g$-unit vector, and the second inequality follows by splitting $\phi$ into its components in $E_{0}$ and in the planes of frequency $k \in \mathbb{N}_{\geqslant 1}$ described above. See [15, pp.447-448] for a related argument.

In our situation, $v=\mathcal{L}_{\partial_{\theta}} u$ is $L^{2}$-orthogonal to all $S^{1}$-invariant functions on $Y$. Thus, if $\phi=\operatorname{proj}_{E} v$, then $\phi=\operatorname{proj}_{E_{0}^{\perp}} \phi$, so either $\phi=0$ or $\lambda \geqslant x^{-1}$ by (3.18). Thus, because $\left.g_{h}\right|_{Y}=2(n+1) x g$,
$$\int_{\partial U_{\rho}} v^{2} d A_{\omega_{h}} \leqslant 2(n+1) x^{2} \int_{\partial U_{\rho}}\left(\left|\nabla_{\omega_{h}} v\right|_{\omega_{h}}^{2}-\left(\mathbf{n}_{\omega_{h}}(v)\right)^{2}\right) d A_{\omega_{h}} .$$
We now drop the $\left(\mathbf{\mathbf { n }}_{\omega_{h}}(v)\right)^{2}$ term from (3.19), replace $\omega_{h}$ by $\omega$ as the reference metric, plug the resulting inequality into (3.16), and trivially bound the $\left(\mathbf{n}_{\omega}(v)\right)^{2}$ term in (3.16) above by $\left|\nabla_{\omega} v\right|_{\omega}^{2}$. Thus,
$$E(\rho) \leqslant C x \int_{\partial U_{\rho}}\left|\nabla_{\omega} v\right|_{\omega}^{2} d A_{\omega} \leqslant-C x\left(\sup _{\partial U_{\rho}}\left|\nabla_{\omega} \rho\right|_{\omega}\right) E^{\prime}(\rho) \leqslant-C x E^{\prime}(\rho)$$
for some uniform constant $C$, where the second inequality follows from the coarea formula. Dividing both sides of (3.20) by $E(\rho)$ and integrating from $\rho_{0}$ to $\rho$, we derive that for some $\varepsilon>0$,
$$E(\rho) \leqslant E\left(\rho_{0}\right) \exp \left(-\frac{1}{C} \int_{\rho_{0}}^{\rho} \frac{d \rho}{x(\rho)}\right) \leqslant C e^{-\varepsilon / x} .$$

This decay rate is so fast that it now suffices to use elliptic regularity at the scale of the injectivity radius. Indeed, Moser iteration applied to (3.12) on $\omega_{h}$-balls of radius $x$ yields a pointwise bound for $v$ which is $O\left(x^{-N} e^{-\varepsilon / x}\right)$ for some $N>0$, and $O\left(x^{-N} e^{-\varepsilon / x}\right)=O\left(e^{-(\varepsilon / 2) / x}\right)$. Then higher-order estimates for $v$ follow from Schauder theory applied to (3.12) on balls of radius $x$. Here we also need higher-order estimates for the coefficient metric $\omega$, which follow from the standard regularity theory of the Monge-Ampère equation on $\omega_{h}$-balls of radius $x$. Indeed, by assumption, $\left|\nabla_{\omega_{h}} u\right|_{\omega_{h}}$ decays exponentially fast in terms of the distance function $\rho$, so $u$ converges to a constant exponentially fast in terms of $\rho$, and $\omega$ is uniformly equivalent to $\omega_{h}$, so $\left|\nabla_{\omega_{h}}^{k} u\right|_{\omega_{h}}=O_{k}\left(x^{-k}\right)$ from the standard theory. \(\square\)

Finally, we obtain the following self-improvement of Lemma 3.4. This is similar to [12, Lemma 2.5], although in [12] this improvement only applies to the $\theta$-derivatives because the $x_{\alpha}, y_{\alpha}$-directions have length $O(1)$, and here we already have a better estimate for the $\theta$-derivatives.

Lemma 3.6. Assuming the conclusions of Lemmas 3.4 and 3.5, we obtain that $u=\mathbf{O}(x)$.
The O notation is as in Definition 3.2. For this we need to choose a finite cover of $U \backslash D$ by charts $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$, and we will use the ones constructed in the proof of Lemma 3.4 using the flatness of $D$. It again seems likely that, using [11], the proof can be made to work even if $D$ is not flat.

Proof. Fix any point $q \in U \backslash D$. Using the rescaled chart $\left(\check{x}_{\alpha}, \check{y}_{\alpha}, \check{x}, \check{\theta}\right)$ of (3.9) on the preimage of the set $\left\{c_{n}^{-1} x(q)<x<c_{n} x(q)\right\} \supset B_{1}(q)$, which makes the pullback of $\omega_{h}$ Euclidean to all orders uniformly as $x(q) \rightarrow 0^{+}$, we can state the results of Lemmas 3.4-3.5 as follows: for all $a, b, c, d \in \mathbb{N}_{0}$,
$$\left|\partial_{\check{x}_{\alpha}}^{a} \partial_{\check{y}_{\alpha}}^{b} \partial_{\check{x}}^{c} \partial_{\check{\theta}}^{d} u\right|=\left\{\begin{array}{ll}
O_{a, b, c}(x(q)) & \text { if } d=0 \\
O_{a, b, c, d}\left(x(q)^{-d} e^{-\varepsilon / x(q)}\right) & \text { if } d \geqslant 1
\end{array} \quad \text { as } x(q) \rightarrow 0^{+} .\right.$$
Converting these estimates back to the unrescaled chart $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$, we gain a factor of $x(q)^{\frac{a+b}{2}-c+d}$ on the right-hand side. This implies property (3.3) for $k=1$ as well as property (3.4) for $d \geqslant 1$. Thus, it remains to verify (3.4) for $d=0$ and $a+b \geqslant 1$. For this it suffices to prove the implication
$$\begin{aligned}
& \forall A, B, C, D \in \mathbb{N}_{0}:\left|\partial_{x_{\alpha}}^{A} \partial_{y_{\alpha}}^{B} \partial_{x}^{C} \partial_{\theta}^{D} u\right|=O_{A, B, C}\left(x^{\frac{A+B}{2}-C}\right) \cdot \begin{cases}O(x) & \text { if } D=0 \\
O_{D}\left(e^{-\varepsilon / x}\right) & \text { if } D \geqslant 1\end{cases} \\
\Longrightarrow & \forall a, b, c \in \mathbb{N}_{0}:\left|\partial_{x_{\alpha}}^{a} \partial_{y_{\alpha}}^{b} \partial_{x}^{c} u\right|=O_{a, b, c}\left(x^{\infty}\right) \text { if } a+b \geqslant 1 .
\end{aligned}$$

To prove (3.23), first note that $v:=\partial_{x_{\alpha}}^{a} \partial_{y_{\alpha}}^{b} \partial_{x}^{c} u$ satisfies $\left|\partial_{\theta} v\right|=O\left(e^{-\varepsilon^{\prime} / x}\right)$ for any $0<\varepsilon^{\prime}<\varepsilon$ thanks to the left-hand side of (3.23). Thus, if $\bar{v}$ denotes the average of $v$ with respect to $\theta$ over $[0,2 \pi]$, then $|v-\bar{v}|=O\left(e^{-\varepsilon^{\prime} / x}\right)$, so it is actually enough to prove that $|\bar{v}|=O\left(x^{\infty}\right)$. Let $\bar{u}$ denote the average of $u$ with respect to $\theta$ over $[0,2 \pi]$, so that $\bar{v}=\partial_{x_{\alpha}}^{a} \partial_{y_{\alpha}}^{b} \partial_{x}^{c} \bar{u}$. Fixing the $x$-variable, we can view $\partial_{x}^{c} \bar{u}$ as a function on the flat torus $D$. Similarly, we can view $\partial_{x_{\alpha}}, \partial_{y_{\alpha}}$ as commuting Killing vector fields on $D$. Because $a+b \geqslant 1$ and $D$ is a compact manifold without boundary, it follows that the average of $\bar{v}$ over $D$ is zero, so $\bar{v}(o)=0$ for some point $o \in D$. Without loss, $o$ is the image of 0 under the covering map $\mathbb{C}^{n-1} \rightarrow D$. Then, for a fixed convex fundamental domain $\Omega \ni 0$ of the deck group action,
$$\sup _{z^{\prime} \in \Omega}\left|\bar{v}\left(z^{\prime}\right)\right|=\sup _{z^{\prime} \in \Omega}\left|\int_{0}^{1} \frac{d}{d t} \bar{v}\left(t z^{\prime}\right) d t\right| \leqslant \operatorname{diam}(\Omega)\left(\sup _{\Omega}\left|\partial_{x_{\alpha}} \bar{v}\right|+\sup _{\Omega}\left|\partial_{y_{\alpha}} \bar{v}\right|\right) .$$
Iterating this argument $k$ times and applying the left-hand side of (3.23) with $A+B=a+b+k$ (and $C=c, D=0$ ), we obtain that $|\bar{v}|=O_{k}\left(x^{k_{0}+(k / 2)}\right)$ for all $k \in \mathbb{N}_{0}$, where $k_{0}:=\frac{a+b}{2}-c+1$. \(\square\)
3.2. Proof of Theorem 3.1. Throughout this section, assuming the conclusion of Lemma 3.6, $D$ can again be an arbitrary compact Calabi-Yau manifold rather than a flat complex torus.

The following definition is modeled after [12, Defn 5.1].
Definition 3.7. After shrinking $U$ if necessary, consider the finite cover of $U \backslash D$ by local charts of the form $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$ that was used in Lemma 3.6 via Definition 3.2. For any $k \in \mathbb{N}_{0}$, we say that a function $f \in C^{\infty}(U \backslash D)$ has an expansion of order $x^{k}$ if, under all charts of this cover,
$$f=\sum_{i=0}^{k} C_{i} x^{i}+R_{k},$$
where the $C_{i}$ are constants and there exists an $\varepsilon>0$ such that $R_{k}=\mathbf{O}\left(x^{k+\varepsilon}\right)$.
Thus, Lemma 3.6 implies that $u$ has an expansion of order $x^{0}$ with $C_{0}=0$ and with $\varepsilon=1$.
Lemma 3.8. If $\psi$ is a $C^{2}$ function which only depends on $x$, then
$$\frac{\left(\omega_{h}+i \partial \bar{\partial} \psi\right)^{n}}{\omega_{h}^{n}}=\frac{\left(n+1+x \psi^{\prime}\right)^{n-1}\left(n+1+x(x \psi)^{\prime \prime}\right)}{(n+1)^{n}} .$$

Proof. Consider the holomorphic chart $\left(z^{\prime}, z_{n}\right)$ underlying the given smooth chart $\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$ as in Section 2.1. Then, by (2.5), the metric coefficients of $\omega_{h}$ are given by
$$\begin{aligned}
& g_{\alpha \bar{\beta}}=(n+1)\left(-x \varphi_{\alpha \bar{\beta}}+x^{2} \varphi_{\alpha} \varphi_{\bar{\beta}}\right), \\
& g_{\alpha \bar{n}}=-(n+1) \frac{x^{2}}{\bar{z}_{n}} \varphi_{\alpha}, \\
& g_{n \bar{n}}=(n+1) \frac{x^{2}}{\left|z_{n}\right|^{2}} .
\end{aligned}$$
On the other hand, using (2.32) we compute
$$\begin{aligned}
& \psi_{\alpha \bar{\beta}}=x^{3}\left(2 \psi^{\prime}+x \psi^{\prime \prime}\right) \varphi_{\alpha} \varphi_{\bar{\beta}}-x^{2} \psi^{\prime} \varphi_{\alpha \bar{\beta}}, \\
& \psi_{\alpha \bar{n}}=-\frac{x^{3}}{\bar{z}_{n}}\left(2 \psi^{\prime}+x \psi^{\prime \prime}\right) \varphi_{\alpha}, \\
& \psi_{n \bar{n}}=\frac{x^{3}}{\left|z_{n}\right|^{2}}\left(2 \psi^{\prime}+x \psi^{\prime \prime}\right) .
\end{aligned}$$
With this, we can now compute the ratio of $\operatorname{det}\left(g_{j \bar{k}}+\psi_{j \bar{k}}\right)$ and $\operatorname{det}\left(g_{j \bar{k}}\right)$. In both of these determinants, we can take out common factors of $\bar{z}_{n}^{-1}$ in the $n$-th column and $z_{n}^{-1}$ in the $n$-th row. Then, by adding a $\varphi_{\bar{\beta}}$ multiple of the $n$-th column of each matrix to its $\beta$-th column, we create a block triangular matrix in each case. A simple calculation concludes the proof of the lemma. \(\square\)

We now rewrite the complex Monge-Ampère equation (3.1) as
$$M_{h}(u):=\log \left(\frac{\left(\omega_{h}+i \partial \bar{\partial} u\right)^{n}}{\omega_{h}^{n}}\right)-u=0,$$
and we decompose $M_{h}$ into its linearization at $\omega_{h}$ and its nonlinear parts via
$$M_{h}=L_{h}+Q_{h} .$$
Here, $L_{h}$ was already defined in (2.28), and $Q_{h}$ is a convergent power series in $i \partial \bar{\partial} u$ without constant or linear terms. Using Lemma 2.5, we can further rewrite this as
$$x^{2} u_{x x}+(n+1) x u_{x}-(n+1) u=G$$
in every local chart of our chosen cover of $U \backslash D$, where
$$\begin{array}{r}
G:=x^{-1} \varphi^{\bar{\beta} \alpha} u_{\alpha \bar{\beta}}-(2 x)^{-2} u_{\theta \theta}-(n+1)\left(F+Q_{h}(u)\right), \\
F=F\left(x_{\alpha}, y_{\alpha}, x^{-1} u_{\theta \alpha}, x^{-1} u_{\theta \bar{\alpha}}, x^{-1} u_{\theta \theta}\right),
\end{array}$$
and $F$ is smooth in $x_{\alpha}, y_{\alpha}$ and linear homogeneous in the remaining arguments.
We have the following lemma, which is analogous to [12, Lemma 5.1].
Lemma 3.9. For all $k \in \mathbb{N}_{0}$, if $u$ has an expansion of order $x^{k}$, with $\varepsilon>\frac{1}{2}$ if $k=0$, then $G$ has an expansion of order $x^{k+1}$.

Proof. Those contributions to $G$ that are linear in $u$ can be written in terms of tangential derivatives of $u$. Thus, by Lemma 3.6, they are $\mathbf{O}\left(x^{\infty}\right)$, i.e., $\mathbf{O}\left(x^{N}\right)$ for any given $N \in \mathbb{N}$. In particular, they have an expansion to any given order, and the polynomial part of this expansion is zero.

It remains to discuss the term $Q_{h}(u)$. For this we need to use our assumption that $u=\psi_{k}+R_{k}$, where $\psi_{k}$ is a degree $k$ polynomial in $x$ and the remainder $R_{k}$ is $\mathbf{O}\left(x^{k+\varepsilon}\right)$. We first observe that
$$R_{k}=\rho_{k}(x)+\mathbf{O}\left(x^{\infty}\right),$$
where $\rho_{k}(x)=\mathbf{O}\left(x^{k+\varepsilon}\right)$ is a smooth radial function. Indeed, for $0<t \ll 1$ we can simply define $\rho_{k}(t)$ to be the average of $R_{k}$ over the level set $\{x=t\}$ with respect to the restriction of the Riemannian
metric associated with $\omega_{h}$. Then the properties $\rho_{k}(x)=\mathbf{O}\left(x^{k+\varepsilon}\right)$ and (3.33) follow from the fact that $R_{k}=\mathbf{O}\left(x^{k+\varepsilon}\right)$, which implies in particular that all tangential derivatives of $R_{k}$ are $\mathbf{O}\left(x^{\infty}\right)$.

Now, also by definition,
$$Q_{h}(u)=\log \left(\frac{\left(\omega_{h}+i \partial \bar{\partial} u\right)^{n}}{\omega_{h}^{n}}\right)-\left.\frac{d}{d t}\right|_{t=0} \log \left(\frac{\left(\omega_{h}+t i \partial \bar{\partial} u\right)^{n}}{\omega_{h}^{n}}\right) .$$
Writing $u=\psi_{k}+\rho_{k}+\mathbf{O}\left(x^{\infty}\right)$ in this formula, using Lemma 3.8, and defining
$$\mathbf{q}(t):=\log \left(1+\frac{t}{n+1}\right)-\frac{t}{n+1},$$
we obtain that
$$Q_{h}(u)=(n-1) \mathbf{q}\left(x \psi_{k}^{\prime}+x \rho_{k}^{\prime}\right)+\mathbf{q}\left(x\left(x \psi_{k}\right)^{\prime \prime}+x\left(x \rho_{k}\right)^{\prime \prime}\right)+\mathbf{O}\left(x^{\infty}\right) .$$
From this we can now deduce that $Q_{h}(u)$ has an expansion of order $x^{k+1}$.
Indeed, q is a convergent power series without constant or linear terms. Thus, if we expand (3.36) as a convergent power series in the four variables $a=x \psi_{k}^{\prime}, b=x \rho_{k}^{\prime}, c=x\left(x \psi_{k}\right)^{\prime \prime}$ and $d=x\left(x \rho_{k}\right)^{\prime \prime}$, then each monomial will be divisible by $a^{2}, a b, b^{2}, c^{2}, c d$ or $d^{2}$. Now observe that $a, c$ are polynomials in $x$ without constant terms while $b, d$ are smooth functions of $x$ which are $\mathbf{O}\left(x^{k+\varepsilon}\right)$. Thus, all monomials in $a, b, c, d$ that appear in the expansion of (3.36) are either polynomials in $x$ or $\mathbf{O}\left(x^{\min \{1+k+\varepsilon, 2 k+2 \varepsilon\}}\right)$ smooth functions of $x$. Because $\varepsilon>\frac{1}{2}$ if $k=0$ and because the sum of these monomials converges as a power series in $a, b, c, d$, it follows that $Q_{h}(u)$ has an expansion of order $x^{k+1}$, as desired. \(\square\)

Since we know from Lemma 3.6 that $u$ has an expansion of order $x^{0}$ with $\varepsilon=1$, Lemma 3.9 tells us that $G$ has an expansion of order $x^{1}$. More precisely, $G=\mathbf{O}\left(x^{2}\right)$ by the proof of Lemma 3.9.

The following lemma is analogous to but much simpler than [12, Proposition 5.1].
Lemma 3.10. Let $\ell \in \mathbb{N}_{\geqslant 1}$. If $G$ has an expansion of order $x^{\ell}$, then $u$ has an expansion of order $x^{\ell}$.
Proof. Fix any chart. Fix an arbitrary point $\left(x_{\alpha}, y_{\alpha}, \theta\right) \in D \times S^{1}$ and let $0<x_{0} \ll 1$. View (3.31) as a second-order ODE for $u\left(x_{\alpha}, y_{\alpha}, x, \theta\right)$ with initial values at $x=x_{0}$. The corresponding homogeneous ODE has the two linearly independent solutions $x$ and $x^{-n-1}$. Using variation of parameters and the fact that $u=O(1)$ and $G=O\left(x^{1+\varepsilon}\right)$ for some $\varepsilon>0$, we derive that
$$u(x)=\left(\frac{u\left(x_{0}\right)}{x_{0}}+\frac{x_{0}^{-n-2}}{n+2} \int_{0}^{x_{0}} t^{n} G(t) d t\right) x-\frac{x^{-n-1}}{n+2} \int_{0}^{x} t^{n} G(t) d t-\frac{x}{n+2} \int_{x}^{x_{0}} t^{-2} G(t) d t .$$
Evaluation at $\left(x_{\alpha}, y_{\alpha}, \theta\right)$ is implicit in this formula.
If $G$ is a degree $\ell$ polynomial in $x$ without constant or linear terms, then (3.37) implies that $u$ is a degree $\ell$ polynomial in $x$ without constant terms.

If $G=\mathbf{O}\left(x^{\ell+\varepsilon}\right)$, then we can deduce from (3.37) that
$$u(x)=\left(\frac{u\left(x_{0}\right)}{x_{0}}+\frac{x_{0}^{-n-2}}{n+2} \int_{0}^{x_{0}} t^{n} G(t) d t-\frac{1}{n+2} \int_{0}^{x_{0}} t^{-2} G(t) d t\right) x+\mathbf{O}\left(x^{\ell+\varepsilon}\right)$$
by splitting the last integral in (3.37) into an integral from 0 to $x_{0}$ and an integral from 0 to $x$. The term in parentheses in (3.38) is by definition independent of $x$, and all of its tangential derivatives are $\mathbf{O}\left(x^{\infty}\right)$ by Lemma 3.6. Thus, this term is constant, and so $u=$ const $\cdot x+\mathbf{O}\left(x^{\ell+\varepsilon}\right)$. \(\square\)

Iterating Lemmas 3.9-3.10, we obtain that $u$ has an expansion to any order, i.e., for all $k \in \mathbb{N}_{0}$ there exists a degree $k$ polynomial $\psi_{k}(x)$ without a constant term such that $u=\psi_{k}(x)+\mathbf{O}\left(x^{k+\varepsilon}\right)$ for some $\varepsilon>0$. In fact, the above arguments show that this holds for $\varepsilon=1$. Moreover, the polynomials $\psi_{k}(x)$ obviously stabilize in the sense that $\psi_{k}(x)=\psi_{k-1}(x)+C_{k} x^{k}$ for all $k \in \mathbb{N}_{\geqslant 1}$. Thus, we may pass to a limit $\psi=\lim _{k} \psi_{k}$ in the ring of all formal power series in $x$ without constant terms.