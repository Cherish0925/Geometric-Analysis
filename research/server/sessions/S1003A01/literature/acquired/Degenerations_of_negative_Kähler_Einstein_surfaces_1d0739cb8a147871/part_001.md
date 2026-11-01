---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Degenerations of negative Kähler–Einstein surfaces]

---
source_file: Degenerations_of_negative_Kähler_Einstein_surfaces_3fa869312be7.pdf
converter: mathpix
format: mmd
---

\title{
DEGENERATIONS OF NEGATIVE KÄHLER-EINSTEIN SURFACES
}

\author{
HOLLY MANDEL
}

\begin{abstract}
Every compact Kähler manifold with negative first Chern class admits a unique metric $g$ such that $\operatorname{Ric}(g)=-g$. Understanding how families of these metrics degenerate gives insight into their geometry and is important for understanding the compactification of the moduli space of negative Kähler-Einstein metrics. I study a special class of such families in complex dimension two. Following the work of Sun and Zhang (2019) in the Calabi-Yau case, I construct a KählerEinstein neck region interpolating between canonical metrics on components of the central fiber. This provides a model for the limiting geometry of metrics in the family.
\end{abstract}

\section*{1. Introduction}
1.1. Kähler-Einstein metrics. Kähler-Einstein metrics sit at the intersection of physics, differential geometry, and algebraic geometry. In physics, they form a class of solutions to the Einstein field equations. In differential geometry, they are higherdimensional analogues of constant curvature metrics on Riemann surfaces that are more rigid than constant scalar curvature metrics and less rigid than constant curvature metrics. In algebraic geometry, they are canonical objects associated to certain complex varieties whose properties reflect the underlying algebraic structure.

The existence theory of Kähler-Einstein metrics on compact manifolds dates back to Yau's theorem [23] but was partially open until 2014. Since the Ricci curvature of a manifold $X$ represents its first Chern class, the existence of a Kähler-Einstein metric on $X$ implies that $c_{1}(X)$ has a representative that is either positive definite, negative definite, or identically zero. Conversely, if $c_{1}(X)=0$, the existence of a Ricci flat metric in any Kähler class of $X$ follows from Yau's theorem, while if $c_{1}(X)$ has a negative representative, the existence of a unique (up to rescaling) Kähler-Einstein metric with negative scalar curvature was proved by Aubin and Yau in 1978 [2, 23]. If $c_{1}(X)$ is positive, however, there are nontrivial obstructions to existence [10, 13, 15]. A full understanding was not achieved until 2014, when Chen-Donaldson-Sun proved that existence is equivalent to the algebraic condition of K-stability [6, 7, 8].

In this paper I study the case $c_{1}(X)<0$. I call a Kähler-Einstein metric on such a space a negative Kähler-Einstein metric, since the constant of proportionality between the metric and its Ricci curvature is negative. Though existence and uniqueness in this case have long been established, the proof is implicit and provides little geometric information. It remains a challenge in Kähler geometry to characterize these metrics.

One goal is to describe the compactification of the moduli space of negative KählerEinstein metrics. Since limits in this space will not always be smooth, a key question is how families of such metrics degenerate. For instance, given a manifold $X$, we

\footnotetext{
Date: June 22, 2022.
Key words and phrases. Kähler geometry, Kähler-Einstein metrics.
}
can vary the complex structure on $X$ to produce a family of Kähler-Einstein metrics. If the complex manifold develops a singularity, the limit space does not have a Kähler-Einstein metric in the usual sense, but we can try to define a generalization to compactify the family.

A first step in this direction is to characterize the convergence of the family outside a singular set. Previous work has explicitly demonstrated convergence to known metrics. If $X=\bar{X} \backslash D$ for a projective manifold $\bar{X}$ and smooth divisor $D$ such that $c_{1}(X)<0$, there exists a unique complete, finite-volume negative Kähler-Einstein metric on $X$ [3, 9, 11, 21]. Tian [20] showed that a degenerating family of Kähler-Einstein metrics will Gromov-Hausdorff converge to this metric on the smooth locus of the central fiber under the assumptions that the total space of the degeneration is smooth, the central fiber has only normal crossing singularities, and its components intersect only pairwise. The pairwise intersection assumption was later removed by Ruan [17]. Greater generality was achieved by Song [18], who used results from birational geometry to obtain convergence without loss of volume for a general algebraic degeneration and to further characterize the structure of the central fiber.

I aim to investigate the geometry that collapses to the singular set. This perspective will be necessary for understanding what types of spaces are needed to compactify the moduli space of negative Kähler-Einstein metrics. In addition, the techniques I use give an explicit description of the nonsingular metrics close to the central fiber. This allows us to "see" the negative Kähler-Einstein metrics whose existence has long been established but whose geometry is mostly unknown.
1.2. Degenerations of negative Kähler-Einstein metrics. A degeneration of negative Kähler-Einstein metrics is defined as a flat family $\pi: \mathcal{X} \rightarrow \Delta$ of algebraic varities over the complex disc $\Delta$ such that $X_{t}=\pi^{-1}(t)$ is smooth for $t \neq 0$ and $K_{\mathcal{X} / \Delta}$ is positive. For generic $t \in \Delta,\left.K_{\mathcal{X} / \Delta}\right|_{X_{t}} \simeq K_{X_{t}}$, so there is a unique Kähler-Einstein metric $\omega_{t}$ in $2 \pi c_{1}\left(\left.K_{\mathcal{X} / \Delta}\right|_{X_{t}}\right)$.

In this paper we investigate a specific family of the above type. For $i=1,2,3$, let $f_{i}$ be a homogeneous polynomial in 4 variables of degree $d_{i}$ such that $d_{1}+d_{2}=d_{3}>4$. Let $\mathcal{X} \subseteq \mathbb{C} P^{3} \times \Delta$ be the variety
$$X_{t}=V\left(f_{1} f_{2}-t f_{3}\right),$$
where the $f_{i}$ are interpreted as polynomials on $\mathbb{C} P^{3}$ and $t$ is the coordinate on $\Delta$. Say that $Y_{i}=V\left(f_{i}\right)$ is smooth for $i=1,2$ and $X_{t}$ is smooth for $t \neq 0$. Finally, assume that $D=V\left(f_{1}\right) \cap V\left(f_{2}\right)$ and $D \cap V\left(f_{3}\right)$ are complete intersections. By the adjunction formula, $K_{X_{t}}$ is ample for generic $t$.

Sun and Zhang [19] have characterized the Calabi-Yau case $\left(d_{1}+d_{2}=4\right)$. They found that after rescaling to unit diameter, $X_{t}$ converges in the Gromov-Hausdorff topology to an interval in $\mathbb{R}$. The interior of the interval reflects the geometry of an infinitesimal neighborhood of the singular point but contains all of the rescaled volume of the space. Meanwhile, rescaled limits at the end points converge to the complete Calabi-Yau metrics on $Y_{i} \backslash D$ constructed by Tian and Yau [22]. An interesting corollary is that these Tian-Yau metrics, though not known to be unique as solutions to a prescribed Ricci curvature problem, are canonical in the sense they arise from degenerating families.

In our case, $Y_{i} \backslash D$ admits a unique complete Kähler-Einstein metric [3, 9, 11, 21]. We hypothesize that as in [19], $\left(X_{t}, \omega_{t}\right)$ will degenerate to a space with three parts: one component for $Y_{i}, i=1,2$, equipped with the Kähler-Einstein metric on $Y_{i} \backslash D$,
plus a neck region gluing these spaces near $D$. Like the Tian-Yau metric, the Kähler-Einstein metric on $Y_{i} \backslash D$ resembles a Calabi model space over the normal bundle of $D$ in $Y_{i}$ near $D$, so a suitable neck region would be a Kähler-Einstein interpolation between these two Calabi model spaces. Indeed the bulk of [19] is the construction of an analogous neck region in the Calabi-Yau case.

The main result of this paper is the succesful construction of this neck region. We will give a precise definition of $\left(\mathcal{C}_{ \pm}, g_{\mathcal{C}_{ \pm}}\right)$in Section 4.1.2.
Theorem 1.1. Fix a complex curve $D$ with $c_{1}(D)<0$ and integers $k_{-} \geq 0, k_{+} \leq 0$. Let $\left(\mathcal{C}_{ \pm}, g_{\mathcal{C}_{ \pm}}\right)$be the Calabi model space over $k_{-} \mathcal{N}_{D}$ and $-k_{+} \mathcal{N}_{D}$, respectively. Then there exists $\alpha_{0} \in(0,1)$, a manifold $\mathcal{M}$ with boundary components $\partial \mathcal{M}_{ \pm}$that gives a singular $S^{1}$ fibration over $D \times I$ for some interval $I \subset \mathbb{R}$, and a family of $S^{1}$-invariant negative Kähler-Einstein metrics $\omega_{K E, T}$ on $\mathcal{M}$, such that the following holds: for any $\alpha \in\left(0, \alpha_{0}\right), \epsilon>0, k \in \mathbb{Z}_{\geq 0}$, and $R>0, B_{R}\left(\partial \mathcal{M}_{-}\right)$is $\epsilon$-close in $C^{k, \alpha}$ to a ball in $\mathcal{C}_{-}$, and similarly for $\partial \mathcal{M}_{+}$, for $T \gg 0$.

Our proof yields a detailed description of the geometry of $\left(\mathcal{M}, \omega_{\mathrm{KE}, T}\right)$ for large $T$. The diameter of $\left(\mathcal{M}, \omega_{\mathrm{KE}, T}\right)$ grows without bound as $T \rightarrow \infty$, and if we rescale the diameter to a constant, the resulting spaces collapse to an interval in $\mathbb{R}$. We can say more, however, about the pointed convergence of $\left(\mathcal{M}, \omega_{\mathrm{KE}, T}\right)$.
Theorem 1.2. Under the assumptions of Theorem 1.1, there exists a family of functions $W_{T}: \mathcal{M} \rightarrow \mathbb{R}_{>0}$ with the following property: Let $\left(x_{j}\right)_{j=1}^{\infty}$ be a sequence of points in $\mathcal{M}$ and choose a sequence $T_{j} \rightarrow \infty$. Then there exists a subsequence of $\left(\mathcal{M}, W_{T_{j}}\left(x_{j}\right)^{-2} \omega_{K E, T_{j}}, x_{j}\right)$ that converges in the pointed Gromov-Hausdorff topology to one of the following:
\begin{itemize}
\item[(1)] the Taub-NUT space $\left(\mathbb{C}_{T N}^{2}, g_{T N}\right)$,
\item[(2)] the Riemannian product $\mathbb{C} \times \mathbb{R}$,
\item[(3)] the Riemannian cylinder $D \times \mathbb{R}$,
\item[(4)] the Calabi model space $\left(\mathcal{C}_{ \pm}, g_{\mathcal{C}_{ \pm}}\right)$.
\end{itemize}
In cases 1 and 4, convergence is smooth. In cases 2 and 3, there is collapsing with bounded curvature away from finitely many points.

The rescaling factor $W_{T}$ is related to the local regularity scales of $\omega_{\mathrm{KE}, T}$. In cases 2 and 3, there is smooth convergence without collapsing on local universal covers. Thus the theorem provides an explicit pointwise description of $\omega_{\mathrm{KE}, T}$ up to error terms that decay as $T \rightarrow \infty$.

To construct $\left(\mathcal{M}, \omega_{\mathrm{KE}, T}\right)$, we guess that the desired metric can be approximated by a Kähler metric with $S^{1}$ symmetry on a singular $S^{1}$ fibration over $D \times I$ for some interval $I \subset \mathbb{R}$. The constraints on the end behavior of the metric determine the topology of $\mathcal{M}$. The Kähler-Einstein equation on $\mathcal{M}$ can then be expressed in terms of the fiber size $h^{-1}$ and a scaling $\chi$ of a fixed metric on $D$ (Section 2). We solve the linearization of this reduced equation to construct a family of approximately Kähler-Einstein metrics $\omega_{T}$ (Sections 3 and 4). By adding an inhomogeneous delta function term to the linearized equation, we change the degree of the restriction of the $S^{1}$ bundle to $D$ to match the Calabi model spaces at either end of $\mathcal{M}$. Once we have solved the inhomogeneous linearized equation, we investigate the local rescaled geometry of $\omega_{T}$ as $T \rightarrow \infty$ (Section 5). The resulting description, reflected in Theorem 1.2, allows us to derive weighted Schauder estimates that are independent of $T$. Finally, we use these estimates to correct $\omega_{T}$ to a Kähler-Einstein metric $\omega_{\mathrm{KE}, T}$ by the implicit function theorem (Section 6).

Our techniques follow [19], but major differences from the Calabi-Yau case appear in Sections 3, 5, and 6. These differences result from the fact that the linearization of the negative Kähler-Einstein equation is $\Delta-1$ rather than $\Delta$. In Section 3, this implies that the linearization of the Kähler-Einstein equation results (after separation of variables) in an ordinary differential equation whose solutions are qualitatively different from the exponential functions in [19]. In Section 6, this requires us to adopt a different framework for our use of the implicit function theorem. As a result, we must derive different Schauder estimates in Section 5.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d4154eb1-3a30-4a5c-835a-c3559a1012ab-04.jpg?height=841&width=1361&top_left_y=738&top_left_x=352}
\captionsetup{labelformat=empty}
\caption{Figure 1. The construction of $\left(\mathcal{M}, \omega_{\mathrm{KE}, T}\right)$. The base space is the manifold $D \times I_{z}$. The diameter of $D$ is bounded below independently of $T$ and blows up near the singular points. $\mathcal{M}$ is a singular $S^{1}$ fibration over $D \times I$. The size of the $S^{1}$ fiber, given by $h^{-1}$, decreases to 0 near the singular points. The degree of the restriction of the $S^{1}$ fibration to $D$ is given by $k_{-}$for $z<0$ and $-k_{+}$for $z>0$ and changes at $z=0$ because there are $k_{-}-k_{+}$singular points.}
\end{figure}

\section*{2. Kähler Reduction}
2.1. Kähler metrics with Hamiltonian symmetry. Our first step toward the construction of $\left(\mathcal{M}, \omega_{\mathrm{KE}, T}\right)$ is to create an approximately Kähler-Einstein space with the desired end behavior. We attempt to build such a space under the added assumption of $S^{1}$ symmetry. In the Calabi-Yau case this is the Gibbons-Hawkings ansatz. The discussion in this section is based on Section 2.1 in [19] .

First, let's assume we already have such a space and see how our calculations are simplified. Let $(X, \omega, J)$ be a Kähler manifold of complex dimension $n$. We say that $X$ has a holomorphic $S^{1}$ symmetry if there is an action $\varphi: S^{1} \times X \rightarrow X$ such that $\varphi_{\theta}$ is holomorphic and $\varphi_{\theta}^{*} \omega=\omega$ for each $\theta \in S^{1}$, where $\varphi_{\theta}(x)=\varphi(\theta, x)$. In this case
let $\xi$ be the vector field generating the action, so
$$\left.\frac{\partial}{\partial \theta} \varphi(\theta, x)\right|_{\theta=\theta_{0}}=\xi(x) .$$
We say that $X$ is Hamiltonian if there exists a function $z$ such that
$$d z=i_{\xi} \omega .$$

If the holomorphic Hamiltonian $S^{1}$ action on $X$ is also free, we can simplify the description of $\omega$ and $J$ by dividing out the $S^{1}$ symmetry. Locally we can quotient by the orbits of the complexified action, generated by $\xi^{1,0}=\xi-i J \xi$, to form an $(n-1)$ dimension complex manifold $D$. Then we can identify $X$ with an $S^{1}$ bundle over $D \times I$ for some interval $I \subset \mathbb{R}$ with coordinate $z$. Since $\omega$ is $S^{1}$ invariant it can be parameterized by the base space $D \times I$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d4154eb1-3a30-4a5c-835a-c3559a1012ab-05.jpg?height=813&width=1083&top_left_y=955&top_left_x=489}
\captionsetup{labelformat=empty}
\caption{Figure 2. Kähler reduction. Locally, the total space is decomposed into an $S^{1}$ fibration over $D \times I_{z}$. The $S^{1}$-invariant metric on $X$ is specified by the fiber size, given by $h^{-1}$, and the $z$-family $\tilde{\omega}(z)$ of metrics on $D$.}
\end{figure}

Let $y$ be a local holomorphic coordinate on $D$ with the convention that $J d y=$ $-i d y, J d \bar{y}=i d \bar{y}$. Let $t$ be a function such that $\xi(t)=1$. Then $y, \bar{y}, t, z$ form a local coordinate system for $X$, but the coordinates $z$ and $t$ are not holomorphic. We write
$$J d z=h^{-1}(-d t+\theta)$$
where $h$ is a function and $\theta$ is an $S^{1}$-invariant one-form without a $d t$ component. We can determine $h$ by observing that by our choice of $z$,
$$J d z\left(\partial_{t}\right)=-d z\left(J \partial_{t}\right)=-\omega(\xi, J \xi)=-\|\xi\|^{2} .$$
Therefore $h=\|\xi\|^{-2}$.
Write $\Theta=-d t+\theta$ and define
$$\tilde{\omega}=\omega-d z \wedge \Theta .$$

The form $\tilde{\omega}$ does not have components in $d z$ or $d t$. In addition,
$$\mathcal{L}_{\xi} \tilde{\omega}=\mathcal{L}_{\xi} \omega-\mathcal{L}_{\xi}(d z \wedge \Theta) .$$
The first term on the right vanishes due to $S^{1}$ invariance, and Cartan's formula can be used to show that $\mathcal{L}_{\xi}(d z \wedge \Theta)=0$ as well. Thus $\tilde{\omega}$ can be thought of as a $z$-family of (1, 1)-forms on $D$.

The integrability of $J$ and the Kähler condition on $\omega$ imply (see [19] 2.1) that $h$ and $\tilde{\omega}$ satisfy the system
$$\left\{\begin{array}{l}
\partial_{z}^{2} \tilde{\omega}+d_{D} d_{D}^{c} h=0 \\
\partial_{z} \tilde{\omega}-d z \wedge d_{D}^{c} h=d \Theta
\end{array}\right.$$

\subsection*{2.2. The reduced Kähler-Einstein equation.}
2.2.1. From $X$ to $(\chi, h)$. We now assume that $n=2$ and $D$ is a Riemann surface of genus at least two. Let $\omega_{D}$ be a Kähler-Einstein metric on $D$ normalized so that Ric $\omega_{D}=-\omega_{D}$. For the remainder of this paper, we assume that all Kähler-Einsten metrics are negative and normalized this way. Because $D$ has complex dimension one, we can write $\tilde{\omega}=\chi \omega_{D}$ for some function $\chi$ on $D \times I$. Our goal is to reduce the equation Ric $\omega=-\omega$ to a simpler collection of equations on $\chi$ and $h$.

Let $\Omega$ be a local $S^{1}$-invariant holomorphic volume form on $X$ and let $\kappa=i(h d z+$ $\left.i \Theta+\kappa^{\prime}\right)$ be the $(1,0)$ form dual to $\xi^{1,0}$, where $\kappa^{\prime}$ does not have a $d z$ or $d t$ component. We can write
$$\Omega=\kappa \wedge \tilde{\Omega}$$
for $\tilde{\Omega}=i_{\xi^{1,0}} \Omega$ also $S^{1}$ invariant and compute that
$$\Omega \wedge \bar{\Omega}=-2 i h d z \wedge d t \wedge \tilde{\Omega} \wedge \overline{\tilde{\Omega}} .$$
There are functions $\chi$ and $\sigma$ such that
$$\omega_{D}=\sigma i \tilde{\Omega} \wedge \overline{\tilde{\Omega}} \quad \tilde{\omega}=\chi \omega_{D},$$
so
$$\frac{\omega^{2}}{\Omega \wedge \bar{\Omega}}=\frac{\tilde{\omega}}{i h \tilde{\Omega} \wedge \tilde{\Omega}}=\frac{\chi \sigma}{h},$$
and so
$$\operatorname{Ric} \omega=-i \partial \bar{\partial} \log \operatorname{det} \frac{\omega^{2}}{\Omega \wedge \bar{\Omega}}=-i \partial \bar{\partial}(\log (\chi)+\log (\sigma)-\log (h)) .$$
Thus the assumption that $\omega$ is Kähler-Einstein gives that
$$-\omega=-\frac{1}{2} d d^{c} \log \chi-i \partial_{D} \bar{\partial}_{D} \log \sigma+\frac{1}{2} d d^{c} \log h .$$
For clarity we have replaced $i \partial \bar{\partial}$ with $\frac{1}{2} d d^{c}$ for functions that vary in $z$ and $i \partial_{D} \bar{\partial}_{D}$ for functions that do not.

We expand out this relation and separate into components to derive four equations relating $\chi$ and $h$. On the one hand,
$$-\omega=-(d z \wedge(-d t+\theta)+\tilde{\omega}) .$$

On the other hand, for any $t$-invariant function $F$ on $X$ we have
$$\begin{aligned}
d d^{c} F= & d J\left(F_{z} d z+d_{D} F\right) \\
= & d\left(F_{z} h^{-1}(-d t+\theta)+d_{D}^{c} F\right) \\
= & \left(F_{z} h^{-1}\right)_{z} d z \wedge(-d t+\theta)+d_{D}\left(F_{z} h^{-1}\right) \wedge(-d t+\theta) \\
& \quad+\left(F_{z} h^{-1}\right)\left(d z \wedge \partial_{z} \theta_{z}+d_{D} \theta\right)+d z \wedge d_{D}^{c}\left(F_{z}\right)+d_{D} d_{D}^{c} F \\
= & \left(F_{z} h^{-1}\right)_{z} d z \wedge(-d t+\theta)+d_{D}\left(F_{z} h^{-1}\right) \wedge(-d t+\theta) \\
& \quad+\left(F_{z} h^{-1}\right)\left(d z \wedge-d_{D}^{c} h+\partial_{z} \tilde{\omega}\right)+d z \wedge d_{D}^{c}\left(F_{z}\right)+d_{D} d_{D}^{c} F .
\end{aligned}$$
Let $F=\log h-\log \chi$. Then Equation 2.4 becomes
$$\begin{aligned}
-2(d z \wedge(-d t+\theta)+\tilde{\omega})=(( & \left.\log h-\log \chi)_{z} h^{-1}\right)_{z} d z \wedge(-d t+\theta) \\
& +d_{D}\left((\log h-\log \chi)_{z} h^{-1}\right) \wedge(-d t+\theta) \\
& +(\log h-\log \chi)_{z} h^{-1}\left(d z \wedge-d_{D}^{c} h+\partial_{z} \tilde{\omega}\right) \\
& +d z \wedge d_{D}^{c}\left((\log h-\log \chi)_{z}\right) \\
& +d_{D} d_{D}^{c}(\log h-\log \chi)-2 i \partial_{D} \bar{\partial}_{D} \log \sigma .
\end{aligned}$$
The covector fields $d z, d t, d y$ and $d \bar{y}$ form a local basis for forms on $X$. Collecting components involving only $d z \wedge d t$ yields
$$\left((\log h-\log \chi)_{z} h^{-1}\right)_{z}=-2 .$$
Since $\theta$ does not have a $d t$ component, collecting components involving only $d t$ wedged with either $d y$ or $d \bar{y}$ yields
$$d_{D}\left((\log h-\log \chi)_{z} h^{-1}\right)=0 .$$
Collecting terms in only $d y$ and $d \bar{y}$ yields
$$(\log h-\log \chi)_{z} h^{-1} \partial_{z} \tilde{\omega}+d_{D} d_{D}^{c}(\log h-\log \chi)-2 i \partial_{D} \bar{\partial}_{D} \sigma=-2 \tilde{\omega}$$
Finally, cancelling all of these terms and "dividing" by $d z$, we have
$$-(\log h-\log \chi)_{z} h^{-1} d_{D}^{c} h+d_{D}^{c}(\log h-\log \chi)_{z}=0,$$
but this is trivial by Equation 2.6.
2.2.2. From $(\chi, h)$ to $X$. The key point is that we can also work backwards from these equations. Fix $\left(D, \omega_{D}\right)$ a complex curve with Ric $\omega_{D}=-\omega_{D}$. For the remainder of this paper we will assume that $k_{-}=0$ and $k_{+}=-1$. We will discuss this simplification further in Section 4.2.

Fix a point $p_{D} \in D$ and let $\delta_{p}$ be a delta function at $\left(p_{D}, 0\right) \in D \times[-1,1 / 2]$, i.e.
$$\int_{D \times[-1,1 / 2]} f \delta_{p} d z \wedge \omega_{D}=f\left(p_{D}, 0\right)$$
Since we are free to add a constant to the moment map $z$, it is sufficient to find a pair $(\chi, h)$ solving the following equations:
$$\begin{gathered}
(\log h-\log \chi)_{z}=-2 h z \\
\partial_{z}^{2} \chi+\Delta_{D} h=2 \pi \delta_{p} \\
\tilde{\omega}-\left(\omega_{D}+z \partial_{z} \tilde{\omega}\right)=-\frac{1}{2} d_{D} d_{D}^{c}(\log h-\log \chi) .
\end{gathered}$$

Equation 2.10 comes from integrating Equations 2.5 and 2.6. Equation 2.11 is part of Equation 2.2, except that we have added a delta function at $z=0$. We will explain this choice in Section 4. Equation 2.12 is the result of substituting Equation 2.10 into Equation 2.7.

The second line of Equation 2.2 gives an additional constraint. Define
$$\Gamma=\partial_{z} \tilde{\omega}-d z \wedge d_{D}^{c} h .$$
If $\frac{1}{2 \pi} \Gamma$ is an integral (1, 1)-form and $z$ is defined on [-1, 1/2], there exists an $S^{1}$ bundle $\pi: \mathcal{M} \rightarrow D \times[-1,1 / 2]$ with connection form $-i \Theta$ and curvature $-i \Gamma$. Choices of such $\Theta$ modulo gauge equivalence are parameterized by $\operatorname{Hom}\left(H^{1}(\mathcal{M}), S^{1}\right)$ and yield distinct complex structures on $\mathcal{M}$.

Given such a $\chi, h$, and $\Gamma$, and fixing a choice of $\Theta$, the metric on $\mathcal{M}$ is given by $\omega=\tilde{\omega}+d z \wedge \Theta$. The computation above shows that $\mathcal{L}_{\xi} \omega=0$. Equations 2.11 and the second line in Equation 2.2 give that the complex structure defined by the complex structure on $D$ and the condition that $J d z=h \Theta$ is integrable and also that $\tilde{\omega}$ is Kähler. Finally, Equations 2.10 and 2.12 ensure that $\tilde{\omega}$ is Kähler-Einstein.

Note that by our addition of a delta function to Equation 2.11, $\chi$ and $h$ will be singular at a fixed $p=\left(p_{D}, 0\right) \in D \times[-1,1 / 2]$. Since all of our computations have been pointwise, our construction goes through without change on $D \times[-1,1 / 2] \backslash\{p\}$. Though a priori the $S^{1}$ bundle $\mathcal{M}$ is defined only over $D \times[-1,1 / 2] \backslash\{p\}$, we will see in Section 4.3 that it can be completed over the singular point. The singularity in Equation 2.11 causes a change in the degree of the $S^{1}$ bundle restricted to $D$ as we pass through $z=0$. This is necessary to match the Calabi model spaces at either end.
2.3. Deriving a linearized equation for $\delta h$. We may ask whether there is a solution such that $h$ and $\chi$ are constant over $D$ for each $z$. In this case Equation 2.11 tells us that away from the singularity,
$$\chi=a z+b$$
for constants $a$ and $b$. In fact, Equation 2.12 tells us that $b=1$. Now if we write $u=\frac{h}{a z+1}$, then we can rewrite Equation 2.10 as
$$(\log u)_{z}=-2 u(a z+1) z .$$
We find that
$$h=\frac{a z+1}{\frac{2}{3} a z^{3}+z^{2}+c}$$
for some constant $c$.
Motivated by this observation, we guess that a nontrivial approximate solution takes the form
$$h=h_{0}+\delta h, \quad \chi=1+\delta \chi$$
for $h_{0}=\frac{1}{z^{2}+T^{-2}}$, functions $\delta h$ and $\delta \chi$ that are small in some sense, and $T$ a large constant. Then Equation 2.10 becomes
$$\partial_{z}\left(\log \left(h_{0}\right)+\log \left(1+\frac{\delta h}{h_{0}}\right)-\log (1+\delta \chi)\right)=-2\left(h_{0}+\delta h\right) z .$$
Since $h_{0}$ solves Equation 2.10 with $\chi \equiv 1$, it follows that
$$\partial_{z}\left(\log \left(1+\frac{\delta h}{h_{0}}\right)-\log (1+\delta \chi)\right)=-2 z \delta h .$$

Expanding the logarithmic terms into a power series and keeping only terms linear in $\delta h$ and $\delta \chi$, we derive that
$$\partial_{z}\left(\frac{\delta h}{h_{0}}\right)-\delta \chi_{z}=-2 z \delta h .$$
Taking another derivative yields that
$$\left(z^{2}+T^{-2}\right) \delta h_{z z}+4 z \delta h_{z}+2 \delta h-\delta \chi_{z z}=-2 \delta h-2 z \delta h_{z} .$$
By Equation 2.11, this becomes
$$\left(z^{2}+T^{-2}\right) \delta h_{z z}+6 z \delta h_{z}+\left(4+\Delta_{D}\right) \delta h=2 \pi \delta_{p} .$$
Equation 2.15 is the linearization of the Kähler-Einstein equation under $S^{1}$ symmetry.

\section*{3. Constructing an Approximate Solution}

In this section we solve Equation 2.15. In the notation introduced in Section 2, this gives us a candidate for $h$, and we can define $\chi$ using Equation 2.11. Since the resulting pair $(\chi, h)$ gives an exact solution to Equation 2.11, the resulting space is Kähler, but since we have linearized Equation 2.10, it is not Einstein. In Section 6 we will check that the discrepancy between the metric and a negative multiple of its Ricci curvature is not too large and then correct to an honest Kähler-Einstein space.

\subsection*{3.1. Solving the linearized equation for $\delta h$.}
3.1.1. Separation of variables. We assume that the solution can be expanded in the eigenfunctions of $\Delta_{D}$ and write
$$\delta h=\sum_{\lambda \geq 0} f_{\lambda} \psi_{\lambda}$$
where $\Delta_{D} \psi_{\lambda}=-\lambda^{2} \psi_{\lambda}, \psi_{\lambda}\left(p_{D}\right) \geq 0$, and $\int_{D}\left|\psi_{\lambda}\right|^{2} \omega_{D}=1$. We then have the formal expansion
$$\delta_{p}=\sum_{\lambda} \psi_{\lambda}\left(p_{D}\right) \psi_{\lambda} \delta_{0},$$
where $\delta_{0}=\delta_{0}(z)$ is a delta function at 0 on [-1, 1/2]. Matching terms, Equation 2.15 then gives an ordinary differential equation
$$\left(z^{2}+T^{-2}\right) f_{\lambda}^{\prime \prime}(z)+6 z f_{\lambda}^{\prime}(z)+\left(4-\lambda^{2}\right) f_{\lambda}(z)=2 \pi \psi_{\lambda}\left(p_{D}\right) \delta_{0}(z)$$
for each eigenvalue $\lambda$.
Now if $\left\|f_{\lambda}\right\|_{L^{2}(\mathbb{R})}<\infty$ for some $\lambda>0$ then for each test function $\chi \in C_{0}^{\infty}(D \times$ $[-1,1 / 2])$,
$$\left\langle f_{\lambda} \psi_{\lambda}, \chi\right\rangle=\int_{-1}^{1 / 2} f_{\lambda}(z)\left(\int_{D} \psi_{\lambda}(\cdot) \chi(\cdot, z) \omega_{D}\right) d z$$
But by elliptic regularity,
$$\left\|\psi_{\lambda}\right\|_{C^{0}}=\mathcal{O}(\sqrt{\lambda}) .$$

Therefore
$$\begin{aligned}
\left|\int_{D} \psi_{\lambda}(\cdot) \chi(\cdot, z) \omega_{D}\right| & =\left|\frac{1}{\lambda^{2 \ell}} \int_{D} \Delta_{D}^{\ell} \psi_{\lambda}(\cdot) \chi(\cdot, z) \omega_{D}\right| \\
& =\left|\frac{1}{\lambda^{2 \ell}} \int_{D} \psi_{\lambda}(\cdot) \Delta_{D}^{\ell} \chi(\cdot, z) \omega_{D}\right| \\
& \leq \frac{C}{\lambda^{2 \ell-\frac{1}{2}}}\|\chi\|_{C^{2 \ell}(D \times I)},
\end{aligned}$$
where $C$ does not depend on $\lambda$. Now say that $\left\|f_{\lambda}\right\|_{L^{2}(\mathbb{R})}$ grows slower than $\lambda^{N}$ for some $N$. Weyl's law guarantees that
$$\#\left\{\lambda \text { an eigenvalue of } \Delta_{D}: \lambda \in[k-1, k)\right\} \leq C k$$
for some $C>0$. Therefore for any $M>0$,
$$\begin{aligned}
\left\langle\sum_{1 \leq \lambda \leq M} f_{\lambda} \psi_{\lambda}, \chi\right\rangle & \leq C \sum_{1 \leq \lambda \leq M} \frac{\left\|f_{\lambda}\right\|_{L^{2}(\mathbb{R})}}{\lambda^{2 \ell-\frac{1}{2}}}\|\chi\|_{C^{2 \ell}(D \times I)} \\
& \leq C \sum_{k=2}^{\infty} k^{N+\frac{3}{2}-2 \ell}\|\chi\|_{C^{2 \ell}(D \times I)} .
\end{aligned}$$
Since there are only finitely many independent eigenvectors with $\lambda<1$, choosing $\ell$ large enough proves that $\sum f_{\lambda} \psi_{\lambda}$ gives a well-defined distribution solving Equation 2.15. It remains to show that each $f_{\lambda}$ is defined on [-1, 1/2] and that $\left\|f_{\lambda}\right\|_{L^{2}(-1,1 / 2)}$ has polynomial growth in $\lambda$.
3.1.2. ODE solution for each eigenvalue. To do this, we solve Equation 3.2 explicitly. The change of variables $x(z)=\frac{1}{2}(1+i T z)$ converts Equation 3.2 to the hypergeometric equation
$$x(x-1) f^{\prime \prime}(x)+(6 x-3) f^{\prime}(x)+\left(4-\lambda^{2}\right) f(x)=T \pi \psi_{\lambda}\left(p_{D}\right) \delta_{0}(x) .$$
Note that
$$1-x(z)=\overline{x(z)}, \quad z \in \mathbb{R}$$

For $n \in \mathbb{R}$, define
$$(n)_{k}=\left\{\begin{array}{ll}
\prod_{j=0}^{k-1}(n+j) & k \in \mathbb{Z}_{>0} \\
1 & k=0
\end{array} .\right.$$
Let $F$ be the hypergeometric series
$$F(\alpha, \beta, \gamma ; x)=\sum_{k=0}^{\infty} \frac{(\alpha)_{k}(\beta)_{k}}{k!(\gamma)_{k}} x^{k}$$
For any $\alpha, \beta, \gamma \in \mathbb{R}$ with $\gamma \notin \mathbb{Z}_{<0}, F$ is absolutely convergent on the open unit disk in $\mathbb{C}$. Now let
$$\alpha(\lambda)=\frac{5+\sqrt{9+4 \lambda^{2}}}{2} \quad \beta(\lambda)=\frac{5-\sqrt{9+4 \lambda^{2}}}{2} \quad \gamma=3 .$$
Using the recursion in the coefficents of $F$, it is checked that for all $\lambda$, the functions
$$v_{1}^{\lambda}=F(\alpha(\lambda), \beta(\lambda), \gamma(\lambda) ; x(z)) \quad \text { and } \quad v_{2}^{\lambda}=F(\alpha(\lambda), \beta(\lambda), \gamma(\lambda) ; \overline{x(z)})$$
solve the homogeneous version of Equation 3.2. Now it is easily observed from the definition that
$$\frac{d}{d x} F(\alpha(\lambda), \beta(\lambda), \gamma ; x)=\frac{\alpha(\lambda) \beta(\lambda)}{\gamma} F(\alpha(\lambda)+1, \beta(\lambda)+1, \gamma+1 ; x),$$
so the Wronskian $W\left[v_{1}^{\lambda}, v_{2}^{\lambda}\right](0)=v_{1}^{\lambda}(0) v_{2}^{\lambda^{\prime}}(0)-v_{1}^{\lambda^{\prime}}(0) v_{2}^{\lambda}(0)$ is evaluated as
$$-\frac{i T \alpha(\lambda) \beta(\lambda)}{\gamma} F\left(\alpha+1, \beta+1, \gamma+1, \frac{1}{2}\right) F\left(\alpha, \beta, \gamma, \frac{1}{2}\right) .$$
An identity due to Gauss states that
$$F\left(\alpha, \beta, \frac{1+\alpha+\beta}{2} ; \frac{1}{2}\right)=\frac{\Gamma\left(\frac{1}{2}\right) \Gamma\left(\frac{1+\alpha+\beta}{2}\right)}{\Gamma\left(\frac{1+\alpha}{2}\right) \Gamma\left(\frac{1+\beta}{2}\right)}$$
where $\Gamma$ is the gamma function ([14] 3.13.2). Thus for our choices of $\alpha, \beta$, and $\gamma$,
$$W\left[v_{1}^{\lambda}, v_{2}^{\lambda}\right](0)=-\frac{i T \alpha(\lambda) \beta(\lambda)}{\gamma} \frac{\Gamma\left(\frac{1}{2}\right)^{2} \Gamma\left(\frac{1+\alpha(\lambda)+\beta(\lambda)}{2}\right) \Gamma\left(\frac{3+\alpha(\lambda)+\beta(\lambda)}{2}\right)}{\Gamma\left(\frac{1+\alpha(\lambda)}{2}\right) \Gamma\left(\frac{2+\alpha(\lambda)}{2}\right) \Gamma\left(\frac{1+\beta(\lambda)}{2}\right) \Gamma\left(\frac{2+\beta(\lambda)}{2}\right)} .$$
Now $\Gamma$ has no roots but has a simple pole with residue $\frac{(-1)^{k}}{k!}$ at $-k$ for $k=0,1,2 \ldots$. The sum $\alpha(\lambda)+\beta(\lambda)=5$ for all $\lambda$, so the numerator of the second term in the above product is constant in $\lambda$. For all $\lambda, \alpha(\lambda)$ is positive, so the $\Gamma$ terms involving $\alpha(\lambda)$ are finite positive numbers. However, we may have that $\frac{1+\beta(\lambda)}{2}$ or $\frac{2+\beta(\lambda)}{2}$ is equal to a negative integer for infinitely many $\lambda$.

Let
$$\Sigma=\left\{\lambda>0: \lambda \text { is an eigenvalue of } \Delta_{D} \text { and } \sqrt{9+4 \lambda^{2}} \in \mathbb{Z}\right\} .$$
Then $\Sigma$ is discrete but possibly infinite. For $\lambda \notin \Sigma, v_{1}^{\lambda}$ and $v_{2}^{\lambda}$ give independent solutions to the homogeneous version of Equation 3.2. In this case, we can solve the non-homogeneous equation by variation of parameters. We write
$$v_{\lambda}=c_{1} v_{1}^{\lambda}+c_{2} v_{2}^{\lambda},$$
where
$$\begin{aligned}
c_{1}(z) & =-\int_{-\infty}^{z} \frac{2 \pi \psi_{\lambda}\left(p_{D}\right) \delta_{0}}{s^{2}+T^{-2}} \frac{v_{2}^{\lambda}(s)}{W\left[v_{1}^{\lambda}, v_{2}^{\lambda}\right](s)} d s \\
& =-2 \pi i \psi_{\lambda}\left(p_{D}\right) \sigma_{0}(z) \frac{T \gamma}{\alpha(\lambda) \beta(\lambda)} \frac{\Gamma\left(\frac{2+\alpha(\lambda)}{2}\right) \Gamma\left(\frac{2+\beta(\lambda)}{2}\right)}{\Gamma\left(\frac{1}{2}\right) \Gamma\left(\frac{3+\alpha(\lambda)+\beta(\lambda)}{2}\right)}
\end{aligned}$$
and
$$\begin{aligned}
c_{2}(z) & =\int_{-\infty}^{z} \frac{2 \pi \psi_{\lambda}\left(p_{D}\right) \delta_{0}}{s^{2}+T^{-2}} \frac{v_{1}^{\lambda}(s)}{W\left[v_{1}^{\lambda}, v_{2}^{\lambda}\right](s)} d s \\
& =2 \pi i \psi_{\lambda}\left(p_{D}\right) \sigma_{0}(z) \frac{T \gamma}{\alpha(\lambda) \beta(\lambda)} \frac{\Gamma\left(\frac{2+\alpha(\lambda)}{2}\right) \Gamma\left(\frac{2+\beta(\lambda)}{2}\right)}{\Gamma\left(\frac{1}{2}\right) \Gamma\left(\frac{3+\alpha(\lambda)+\beta(\lambda)}{2}\right)} \\
& =-c_{1}(z)
\end{aligned}$$
Since $v_{1}(z)=\overline{v_{2}(z)}$, this gives that
$$v_{\lambda}=2 i c_{1}(z) \operatorname{Im} v_{1}^{\lambda}(z)=12 \pi \sigma_{0}(z) \frac{T \psi_{\lambda}\left(p_{D}\right)}{\alpha(\lambda) \beta(\lambda)} \frac{\Gamma\left(\frac{2+\alpha(\lambda)}{2}\right) \Gamma\left(\frac{2+\beta(\lambda)}{2}\right)}{\Gamma\left(\frac{1}{2}\right) \Gamma\left(\frac{3+\alpha(\lambda)+\beta(\lambda)}{2}\right)} \operatorname{Im} v_{1}^{\lambda}(z),$$
where
$$\sigma_{0}(z)=\left\{\begin{array}{ll}
0 & \text { if } z<0 \\
1 & \text { if } z \geq 0
\end{array} .\right.$$
It is verified that $v_{\lambda}$ is a solution to Equation 3.2 in the distributional sense.
3.1.3. Finding a decaying solution for $\lambda \notin \Sigma$. We would like to define $f_{\lambda}=v_{\lambda}$, but for Equation 3.1 to converge we must modify $v_{\lambda}$ by a linear combination of homogeneous solutions to Equation 3.2 so that $f_{\lambda}(z)$ grows at worst like a fixed polynomial in $\lambda$ for all $z$. In this section we write $\alpha$ for $\alpha(\lambda)$ and $\beta$ for $\beta(\lambda)$ for brevity.

Fix a branch of the complex logarithm cut along the negative real axis. We have that for $\lambda \notin \Sigma, F(\alpha, \beta, \gamma ; x)$ has the analytic extension
$$\begin{aligned}
F(\alpha, \beta, \gamma ; x)=\frac{\Gamma(\beta-\alpha) \Gamma(\gamma)}{\Gamma(\beta) \Gamma(\gamma-\alpha)} & (-x)^{-\alpha} F\left(\alpha, \alpha+1-\gamma, \alpha+1-\beta ; x^{-1}\right) \\
& +\frac{\Gamma(\alpha-\beta) \Gamma(\gamma)}{\Gamma(\beta) \Gamma(\gamma-\beta)}(-x)^{-\beta} F\left(\beta, \beta+1-\gamma, \beta+1-\alpha ; x^{-1}\right),
\end{aligned}$$
which is defined for all $x$ such that $-x$ is in the domain of $\log$ (see 14 3.6(28)-(30)). For clarity, define
$$f_{1}(x)=\frac{\Gamma(\beta-\alpha) \Gamma(\gamma)}{\Gamma(\beta) \Gamma(\gamma-\alpha)}|x|^{-\alpha} e^{-\alpha i(\arg (x)-\pi)} F\left(\alpha, \alpha+1-\gamma, \alpha+1-\beta ; x^{-1}\right)$$
and
$$f_{2}(x)=\frac{\Gamma(\alpha-\beta) \Gamma(\gamma)}{\Gamma(\beta) \Gamma(\gamma-\beta)}|x|^{-\beta} e^{-\beta i(\arg (x)-\pi)} F\left(\beta, \beta+1-\gamma, \beta+1-\alpha ; x^{-1}\right)$$
on $\mathbb{C} \backslash \mathbb{R}$. Then if $z>0$,
$$F(\alpha, \beta, \gamma ; x)=f_{1}(x)+f_{2}(x),$$
while if $z<0$,
$$F(\alpha, \beta, \gamma ; x)=e^{-2 \pi i \alpha} f_{1}(x)+e^{-2 \pi i \beta} f_{2}(x) .$$
Now because $f_{1}$ and $f_{2}$ are linearly independent solutions to the homogeneous version of Equation 3.2 ([14] 3.7) and $F(\alpha, \beta, \gamma ; 1-x)$ is defined on the upper half-plane, there exist $\mu_{1}$ and $\mu_{2}$ such that
$$F(\alpha, \beta, \gamma ; 1-x(z))=\mu_{1} f_{1}(x(z))+\mu_{2} f_{2}(x(z))$$
for $z>0$. But by Equations 3.6 and 3.9 we have that if $z>0$,
$$F(\alpha, \beta, \gamma ; 1-x(z))=e^{-2 \pi i \alpha} f_{1}(\bar{x}(z))+e^{-2 \pi i \beta} f_{2}(\bar{x}(z)) .$$
Let $z \rightarrow+\infty$ and divide Equation 3.10 by Equation 3.11. Note that as $|z| \rightarrow \infty$, $F\left(\beta, \beta+1-\gamma, \beta+1-\alpha ; x^{-1}\right) \rightarrow 1$ and likewise for the conjugate. Since $\beta<\alpha,|x|^{-\beta}$ dominates $|x|^{-\alpha}$, while the phase of $x$ goes to $\pi / 2$, so we have that
$$e^{2 \pi i \beta} \mu_{2}=\lim _{z \rightarrow+\infty} \frac{f_{2}(\bar{x}(z))}{f_{2}(x(z))}=e^{\pi i \beta}$$
But since $F(\alpha, \beta, \gamma ; x)$ is a real power series, $F(\alpha, \beta, \gamma ; 1-x(z))=\overline{F(\alpha, \beta, \gamma ; x(z))}$. Thus Equations 3.8 and 3.10 give that
$$\lim _{z \rightarrow \infty} \frac{\operatorname{Im}(F(\alpha, \beta, \gamma ; x(z)))}{\operatorname{Re}(F(\alpha, \beta, \gamma ; x(z)))}=\tan \left(\frac{\pi}{2} \beta\right) .$$

Taking the complex conjugate, we must have that
$$\lim _{z \rightarrow-\infty} \frac{\operatorname{Im}(F(\alpha, \beta, \gamma ; x(z)))}{\operatorname{Re}(F(\alpha, \beta, \gamma ; x(z)))}=-\tan \left(\frac{\pi}{2} \beta\right) .$$
Thus if we let $\rho=-\tan \left(\frac{\pi}{2} \beta\right)$, we have that
$$\left(\sigma_{0}(z)-\frac{1}{2}\right) \operatorname{Im}\left(v_{1}^{\lambda}\right)(z)+\frac{\rho}{2} \operatorname{Re}\left(v_{1}^{\lambda}\right)(z)=\mathcal{O}\left((T z)^{-\alpha}\right)$$

Now let
$$C_{1}=\frac{12 \pi \psi_{\lambda}\left(p_{D}\right) T}{\alpha \beta} \frac{\Gamma\left(\frac{2+\alpha}{2}\right) \Gamma\left(\frac{2+\beta}{2}\right)}{\Gamma\left(\frac{1}{2}\right) \Gamma\left(\frac{3+\alpha+\beta}{2}\right)},$$
so that
$$v_{\lambda}(z)=C_{1} \sigma_{0}(z) \operatorname{Im}\left(v_{1}^{\lambda}(z)\right) .$$
Define
$$f_{\lambda}(z)=\frac{C_{1}}{2}\left(-\operatorname{Im}\left(v_{1}^{\lambda}\right)(z)+\rho \operatorname{Re}\left(v_{1}^{\lambda}\right)(z)\right)+v_{\lambda}(z) .$$
By our discussion above,
$$f_{\lambda}(z)=\mathcal{O}\left((T z)^{-\alpha}\right) .$$
Indeed our choice of $f_{\lambda}$ is the unique decaying solution to the inhomogeneous equation 3.2.
3.1.4. Extension to $\Sigma$. By Equation 3.6, we can replace $\operatorname{Im}(F)$ and $\operatorname{Re}(F)$ in Equation 3.12 with appropriate linear combinations of $F(\alpha, \beta, \gamma, x)$ and $F(\alpha, \beta, \gamma, 1-x)$. It can be checked that both of these functions are locally holomorphic in $x, \alpha$ and $\beta$. Checking all other terms in Equation 3.12, we find that if we ignore the step function term, the function
$$\frac{f_{\lambda}(x)}{\psi_{\lambda}\left(p_{D}\right)},$$
extends to a meromorphic function of $\alpha$ (recall that $\beta=5-\alpha$ ) and of $x$ away from $x=1$. Call this function $g(\alpha, x)$. Now in Section 3.1.6 we will show that away from $\lambda=0, f_{\lambda}(z)$ is uniformly bounded by a polynomial in $\lambda$ for $\lambda \notin \Sigma$ and $z \in \mathbb{R}$. Therefore for $\lambda^{*} \in \Sigma, g$ is holomorphic in a neighborhood of
$$\left\{\alpha\left(\lambda^{*}\right)\right\} \times\{x(z): z \in[-1,0]\} \subset \mathbb{C}^{2},$$
and so $g(\alpha(\lambda), x(z))$ converges smoothly to a function of $z \in(-1,0)$ as $\lambda \rightarrow \lambda^{*}$. Note that convergence holds up to the boundary, i.e. $\partial_{z}^{k} g(\alpha(\lambda), x(0)) \rightarrow \partial_{z}^{k} g^{k}\left(\alpha\left(\lambda^{*}\right), x(0)\right)$ for all integers $k \geq 0$.

By a similar argument, $g(\alpha, x)$ converges smoothly to a function for $z \in[0,1 / 2]$. We define
$$f_{\lambda^{*}}(z)=\psi_{\lambda^{*}}\left(p_{D}\right) g\left(\alpha\left(\lambda^{*}\right), z\right) .$$
Smooth convergence up to the boundary on $[-1,0]$ and $[0,1 / 2]$ ensures that $f_{\lambda^{*}}$ satisfies Equation 3.2.
3.1.5. Solution for $\lambda=0$. This convergence argument does not give the solution at $\lambda=0$ because the uniform bound on $g$ does not hold as $\lambda \rightarrow 0$. In this case, however, the general solution to the homogeneous version of Equation 3.2 is given by
$$\frac{1}{\left(1+(T z)^{2}\right)^{2}}\left(\mu_{1}+\mu_{2}\left(z+\frac{T^{2} z^{3}}{3}\right)\right)$$
for $\mu_{1}, \mu_{2} \in \mathbb{R}$.
Variation of parameters yields an inhomogeneous solution
$$v_{0}=2 \pi \sigma_{0}(z) T^{2} \psi_{0}\left(p_{D}\right) \frac{z+\frac{T^{2} z^{3}}{3}}{\left(1+(T z)^{2}\right)^{2}} .$$
We add a homogeneous solution to define the even function
$$f_{0}(z)=\left(2 \sigma_{0}(z)-1\right) \pi T^{2} \psi_{0}\left(p_{D}\right) \frac{z+\frac{T^{2} z^{3}}{3}}{\left(1+(T z)^{2}\right)^{2}} .$$
3.1.6. $L^{2}$ estimates of the ODE solutions. To show the convergence of Equation 3.1, we first control the growth of the solutions to Equation 3.2 at the origin. Then we use the maximum principle to show that the value at the origin bounds the value everywhere.

Proposition 3.1. For all $\lambda>2$ and $T>0$, let $f_{\lambda}^{T}$ be the unique decaying solution to Equation 3.2. Then $f_{\lambda}^{T}(0) \leq 0$. Further, there exists $N>0$ independent of $T$ and $\lambda$ such that
$$\left|f_{\lambda}^{T}(0)\right|=T \mathcal{O}\left(\lambda^{N}\right)$$
as $\lambda \rightarrow \infty$.
Proof. Using Equation 3.7 to evaluate $v_{1}^{\lambda}(0)$ and noticing that $v_{1}^{\lambda}(0)$ is a real power series with a real argument, we see that if $\lambda \notin \Sigma$ then
$$\begin{aligned}
f_{\lambda}^{T}(0) & =-\frac{12 \pi T \psi_{\lambda}\left(p_{D}\right)}{2 \alpha \beta} \frac{\Gamma\left(\frac{2+\alpha}{2}\right) \Gamma\left(\frac{2+\beta}{2}\right)}{\Gamma\left(\frac{1}{2}\right) \Gamma(4)} \frac{\Gamma\left(\frac{1}{2}\right) \Gamma(3)}{\Gamma\left(\frac{1+\alpha}{2}\right) \Gamma\left(\frac{1+\beta}{2}\right)} \tan \left(\frac{\pi}{2} \beta\right) \\
& =-C \frac{T \psi_{\lambda}\left(p_{D}\right)}{\alpha \beta} \frac{\Gamma\left(\frac{2+\alpha}{2}\right) \Gamma\left(\frac{2+\beta}{2}\right)}{\Gamma\left(\frac{1+\alpha}{2}\right) \Gamma\left(\frac{1+\beta}{2}\right)} \tan \left(\frac{\pi}{2} \beta\right)
\end{aligned}$$
for some $C>0$ independent of $\lambda$ and $T$. First we note that by elliptic regularity,
$$\psi_{\lambda}\left(p_{D}\right)=\mathcal{O}(\sqrt{\lambda})$$
as $\lambda \rightarrow \infty$. To understand the gamma function terms, we note that for $x \geq 3$,
$$\lfloor x-1\rfloor!\leq \Gamma(x) \leq\lceil x-1\rceil!.$$
In addition, we have the following identities (see [14] 2.2).
Lemma 3.2. For $x \in \mathbb{R}$ and $N \in \mathbb{Z}_{>0}$,
$$\begin{gathered}
\Gamma(x+N)=(x)_{N} \Gamma(x), \\
\Gamma(x) \Gamma(1-x)=\pi \csc \pi x,
\end{gathered}$$
and
$$\Gamma\left(\frac{1}{2}+x\right) \Gamma\left(\frac{1}{2}-x\right)=\pi \sec \pi x .$$

Equation 3.17 and 3.18 give that
$$\frac{\Gamma\left(\frac{2+\alpha}{2}\right) \Gamma\left(\frac{2+\beta}{2}\right)}{\Gamma\left(\frac{1+\alpha}{2}\right) \Gamma\left(\frac{1+\beta}{2}\right)}=-\frac{\Gamma\left(\frac{2+\alpha}{2}\right) \Gamma\left(\frac{1-\beta}{2}\right)}{\Gamma\left(\frac{1+\alpha}{2}\right) \Gamma\left(\frac{-\beta}{2}\right)} \cot \left(\frac{\pi \beta}{2}\right) .$$
Cancelling the tangent terms and noting that $\beta<0$ as long as $\lambda>2$, this proves that $f_{\lambda}^{T}(0) \leq 0$. Further, since $a \rightarrow \infty$ as $\lambda \rightarrow \infty$ and $\beta=5-\alpha$, Equation 3.15 gives that for large enough $\lambda$,
$$\frac{\Gamma\left(\frac{2+\alpha}{2}\right) \Gamma\left(\frac{1-\beta}{2}\right)}{\Gamma\left(\frac{1+\alpha}{2}\right) \Gamma\left(\frac{-\beta}{2}\right)} \leq \frac{\left\lceil\frac{\alpha}{2}\right\rceil!\left\lceil\frac{\alpha-6}{2}\right\rceil!}{\left\lfloor\frac{\alpha-1}{2}\right\rfloor!\left\lfloor\frac{\alpha-7}{2}\right\rfloor!},$$
which by Equation 3.16 is bounded by a polynomial in $\alpha$ as $\alpha \rightarrow \infty$. But $\alpha=\mathcal{O}(\lambda)$ as $\lambda \rightarrow \infty$. \(\square\)

Proposition 3.3. Take $f_{\lambda}^{T}$ as in Proposition 3.1. Then $f_{\lambda}^{T}(z)$ is nonincreasing on $(-\infty, 0]$ and nondecreasing on $[0, \infty)$.
Proof. We first note that $f_{\lambda}^{T}(z) \leq 0$ for all $z$ and $\lambda>2$. For away from $z=0$, $f_{\lambda}^{T}$ is a smooth solution to the homogeneous version of Equation 3.2. Therefore by Proposition 3.1 and Equation 3.13, if $f_{\lambda}^{T}(z)>0$ for any $z<0$ then $f_{\lambda}^{T}$ has a positive local maximum at some $z^{*} \in(-\infty, 0)$. But then $\left(f_{\lambda}^{T}\right)^{\prime \prime}\left(z^{*}\right) \leq 0,\left(f_{\lambda}^{T}\right)^{\prime}\left(z^{*}\right)=0$, and $f_{\lambda}^{T}\left(z^{*}\right)>0$, contradicting Equation 3.2. An identical argument shows that $f_{\lambda}^{T}$ is nonpositive on $(0, \infty)$.

Now we show that for $\lambda>2, f_{\lambda}^{T}(z)$ is nonincreasing on $(-\infty, 0]$. An argument as in the previous paragraph shows that $f_{\lambda}^{T}(z)$ cannot have a negative local minimum on $(-\infty, 0)$. But if $f_{\lambda}\left(z_{1}\right)<f_{\lambda}\left(z_{2}\right)$ for $z_{1}<z_{2}<0$, there must be a negative local minimum on $\left(-\infty, z_{2}\right)$.

A similar argument gives that $f_{\lambda}^{T}$ is nondecreasing from 0 to $\infty$. \(\square\)

Propositions 3.1 and 3.3 give the desired $L^{2}$ growth control.
Proposition 3.4. Fix $T>0$. Then
$$\left\|f_{\lambda}^{T}(z)\right\|_{L^{2}(-1,1)}=\mathcal{O}\left(\lambda^{N}\right)$$
for some $N>0$.
Remark 3.5. The solutions $f_{\lambda}^{T}$ are defined on all of $\mathbb{R}$, and the convergence arguments of this section apply to any compact interval. Therefore it is justified to speak of $\delta h$ as a function on $\mathbb{R}$.
3.1.7. Decay of $\delta h$. Away from the singular point, the behavior of $\delta h$ is controlled by the zero mode which is constant over $D$.

Proposition 3.6. Let $\delta h^{T}=\sum_{\lambda \geq 0} f_{\lambda}^{T} \psi_{\lambda}$. Then there exists $\rho>0$ such that
$$\delta h^{T}=f_{0}^{T} \psi_{0}+T \mathcal{O}\left((T z)^{-4}\right)$$
and
$$\Delta_{D} \delta h^{T}=T \mathcal{O}\left((T z)^{-4}\right)$$
on $|z| \geq \rho T^{-1}$ as $T \rightarrow \infty$.
Proof. We see from Equation 3.2 that $\frac{1}{T} \delta h^{T}(z)=\delta h^{1}(T z)$. Therefore it is sufficient to show that
$$\delta h^{1}(z)=f_{0}^{1} \psi_{0}+\mathcal{O}\left(z^{-4}\right)$$
for $|z| \geq \rho$. By Remark 3.5 we may treat $\delta h^{1}$ as a function on $\mathbb{R}$. If $\lambda>0$ then $\alpha(\lambda)>4$, so by Equation 3.13 each $\psi_{\lambda} f_{\lambda}(z)$ is dominated by $z^{-4} C_{\lambda}$ for some $C_{\lambda}>0$. It remains to show that the series $\sum_{\lambda} C_{\lambda}$ converges.

Now for $z \in(0, \infty)$ and $\epsilon \in(0,1)$ let
$$g_{\lambda}(z)=z^{\epsilon \lambda+4} \max _{D}\left|\psi_{\lambda}\right| f_{\lambda}(z)$$
Then Equation 3.2 gives that
$$z^{2}\left(1+z^{2}\right) g_{\lambda}^{\prime \prime}(z)+\ldots+\left(\lambda^{2}\left(\epsilon^{2}+\left(\epsilon^{2}-1\right) z^{2}\right)+\lambda\left(3 \epsilon z^{2}+9 \epsilon\right)+20\right) g_{\lambda}(z) \equiv 0,$$
on $D$, where we have omitted the $g_{\lambda}^{\prime}(z)$ term. The coefficient of $g_{\lambda}^{\prime \prime}(z)$ and the coefficient of $g_{\lambda}(z)$ are positive for all $|z|<1$ for $\epsilon$ close enough to 1.

Assume that $\lambda \gg 0$. By Proposition 3.1, $g_{\lambda}(z)<0$ for all $z>0$. Equation 3.13 gives that $\lim _{z \rightarrow \pm \infty}\left|g_{\lambda}(z)\right|=0$, since
$$\alpha(\lambda)>4+\epsilon \lambda, \quad \lambda \gg 0 .$$
Also, since $f_{\lambda}$ is continuous, $\lim _{z \rightarrow 0} g_{\lambda}(z)=0$. But by Equation 3.21 and the arguments from Proposition 3.3, $g_{\lambda}(z)$ cannot have a negative local maximum in $(0, \infty)$. Therefore there exists $\eta>0$ such that $g_{\lambda}(z)$ is nondecreasing on $(\eta, \infty)$.

Fix $\rho$ and $\rho_{1}$ such that $\eta<\rho_{1}<\rho$. By Proposition 3.1, Proposition 3.3, and Equation 3.3,
$$\left|\max _{D} \psi_{\lambda} f_{\lambda}\left(\rho_{1}\right)\right|=\mathcal{O}\left(\lambda^{k}\right)$$
for some $k<\infty$. Then
$$\left|\rho^{4} \max _{D} \psi_{\lambda} f_{\lambda}(\rho)\right| \leq\left|\left(\frac{\rho_{1}}{\rho}\right)^{\epsilon \lambda} \rho_{1}^{4} \max _{D} \psi_{\lambda} f_{\lambda}\left(\rho_{1}\right)\right| \leq C\left(\frac{\rho_{1}}{\rho}\right)^{\epsilon \lambda} \lambda^{k},$$
where $C$ depends on $\rho_{1}$ but not $\lambda$. Using Equation 3.4, the right hand side is summable, so we can take $C_{\lambda}=C\left(\frac{\rho_{1}}{\rho}\right)^{\epsilon \lambda} \lambda^{k}$ with $C$ as above. By nondecreasingness, this bound holds for all $z>\rho$. Meanwhile, because $f_{\lambda}$ is even-symmetric, the bound holds for $z<-\rho$ as well.

Since $\Delta_{D} \delta h=\sum_{\lambda>0}-\lambda^{2} \psi_{\lambda} f_{\lambda}$, the proof for $\Delta_{D} \delta h^{T}(z)$ follows with $C_{\lambda}=C\left(\frac{\rho_{1}}{\rho}\right)^{\epsilon \lambda} \lambda^{k+2}$. \(\square\)
3.2. Correction to $h$. Given the solution $h=h_{0}+\delta h$ to the linearization of Equation 2.10 that we have just constructed, we can define $\chi$ by integrating Equation 2.11 and choosing $a=k_{-}=0$. Having done so, we see that $(\chi, h+q(z))$ also solves Equation 2.11 for $q$ a smooth function of $z$. We make use of this freedom to construct another solution $\tilde{h}$ that has the desired behavior near the ends of the $z$-interval [-1, 1/2].

Fix a constant $C_{2}>0$ as in Proposition 3.6. Then we have that for $|z| \geq \frac{C_{2}}{2 T}$,
$$h=T^{2}\left(\frac{1}{1+(T z)^{2}}+\left(2 \sigma_{0}(z)-1\right) \pi \psi_{0}\left(p_{D}\right) \frac{z+\frac{T^{2} z^{3}}{3}}{\left(1+(T z)^{2}\right)^{2}}+\mathcal{O}\left(T^{-1}\right)\right) .$$
Now for each $T$ let $\tilde{h}$ be a smooth function satisfying
$$T^{-2} \tilde{h}= \begin{cases}T^{-2} h & |z|<\frac{C_{2}}{2 T} \\ T^{-2} h+\mathcal{O}\left(T^{-1}\right) & \frac{C_{2}}{2 T} \leq|z|<\frac{C_{2}}{T} \\ \frac{k_{ \pm} z+1}{\frac{2}{3} T^{2} k_{ \pm} z^{3}+T^{2} z^{2}+1}+\mathcal{O}\left(T^{-5} z^{-4}\right) & \frac{C_{2}}{T} \leq|z|<1\end{cases}$$
with $k_{ \pm}$interpreted as $k_{-}$for $z<0$ and $k_{+}$for $z>0$. This is possible because for $\frac{C_{2}}{2 T} \leq|z| \leq \frac{C_{2}}{T}$,
$$\frac{k_{ \pm} z+1}{\frac{2}{3} T^{2} k_{ \pm} z^{3}+T^{2} z^{2}+1}=\frac{1}{1+(T z)^{2}} \pm \pi \psi_{0}\left(p_{D}\right) \frac{z+\frac{T^{2} z^{3}}{3}}{\left(1+(T z)^{2}\right)^{2}}+\mathcal{O}\left(T^{-1}\right) .$$
Therefore a smooth interpolation of $T^{-2} h$ and $\frac{k_{ \pm} z+1}{\frac{2}{3} T^{2} k_{ \pm} z^{3}+T^{2} z^{2}+1}$ in this region differs from $T^{-2} h$ by a function that is $\mathcal{O}\left(T^{-1}\right)$. But the zero eigenfunction $\psi_{0}$ is constant, so by Equation 3.19, the $D$-dependent terms of $\delta h$ are $T \mathcal{O}\left((T z)^{-4}\right)$ for $|z|>\frac{C_{2}}{2 T}$. Therefore after a $T^{-1} \mathcal{O}\left((T z)^{-4}\right)$ correction, we can take $T^{-2}(\tilde{h}-h)$ to be a function of $z$ only.

For simplicity of notation, the symbol $h$ will refer to the function $\tilde{h}$ for the remainder of this paper.
3.3. Expansion near the singular point. Equation 2.15 and the linearization of Equation 2.11 yield a useful expansion of the metric near the singular point.

First, we introduce a notation for describing the regularity of functions defined near a singularity. For $\ell \in \mathbb{N}$ and $U \subseteq \mathbb{R}_{a, b, w}^{3}$ containing 0 , let
$$r_{w}(a, b, w)=\sqrt{a^{2}+b^{2}+w^{2}}$$
and
$$\mathcal{W}^{\ell}(U)=\left\{f \in C^{\infty}(U \backslash\{0\}): \nabla^{j} f=\mathcal{O}\left(r_{w}^{\ell-j} \log \left(r_{w}\right)\right) \text { as } r_{w} \rightarrow 0, \forall j \geq 0\right\} .$$
Now for any $\ell \in \mathbb{N}$ and $U \subset \mathbb{R}_{a, b, w}^{3}$ containing 0 we take $w^{\ell}$ to be a function in $W^{\ell}(U)$. Similarly, for any $k \in \mathbb{Z}_{\geq 0}$ and $\alpha \in(0,1)$, we take $g^{k, \alpha}$ to be a function in $C^{\infty}(U \backslash\{p\}) \cap C^{k, \alpha}(U)$. We allow $g^{k, \alpha}, w^{\ell}$, and the corresponding domains $U$ to change in each invocation (as is convention for the constant $C$ ), but it will always be assumed that they have no dependence on $T$.

The following elementary result will provide the desired regularity for an expansion around the singular point.

Lemma 3.7. Let $f(a, b, w)$ be a homogeneous polynomial of degree $k$ and $\mathcal{L}^{\prime}$ a differential operator such that $\mathcal{L}^{\prime}\left(\mathcal{W}^{1}\right) \subseteq \mathcal{W}^{1}$. Then there exist $u, v^{\prime} \in \mathcal{W}^{1}$ such that
$$\left(\Delta_{\mathbb{R}^{3}}+\mathcal{L}^{\prime}\right) u=\frac{f}{r_{w}^{k+1}}+v^{\prime}$$
Proof. Since $\mathcal{L}^{\prime}\left(\mathcal{W}^{1}\right) \subseteq \mathcal{W}^{1}$, we may assume $\mathcal{L}^{\prime}=0$. Now let $p^{(k)}$ be a homogeneous polynomial of degree $k$. Then
$$\Delta_{\mathbb{R}^{3}} \frac{p^{(k)}}{r_{w}^{k-1}}=-(k-1)(k+2) \frac{p^{(k)}}{r_{w}^{k+1}}+\frac{\Delta_{\mathbb{R}^{3}} p^{(k)}}{r_{w}^{k-1}} .$$
But $\nabla\left(\frac{p^{(k)}}{r_{w}^{j}}\right)=\frac{p^{(k+1)}}{r_{w}^{j+2}}$ for $p^{(k+1)}$ a homogeneous polynomial of degree $k+1$, so $\frac{p^{(k)}}{r_{w}^{k-1}} \in$ $\mathcal{W}^{1}$. In particular, $\frac{f}{r_{w}^{k-1}} \in \mathcal{W}^{1}$, so taking $u=\frac{-1}{(k-1)(k+2)} \frac{f}{r_{w}^{k-1}}$, we see that if $k>1$ and the result holds for $k^{\prime}<k$, it holds for $k$ as well.

To establish the base cases $k=0,1$, we note that
$$\Delta_{\mathbb{R}^{3}} r_{w}=\frac{2}{r_{w}}$$
and
$$\Delta_{\mathbb{R}^{3}}\left(a \log \left(r_{w}\right)\right)=\frac{3 a}{r_{w}^{2}}$$ \(\square\)

Now return to the space constructed above and assume that in the notation of Section 3.2, $|z|<\frac{C_{2}}{2 T}$. If we let
$$\mathcal{L}_{T, z}^{h}=\left(\Delta_{D}+T^{-2} \partial_{z}^{2}\right)+z^{2} \partial_{z}^{2}+6 z \partial_{z}+4$$
then Equation 2.15 gives that
$$\mathcal{L}_{T, z}^{h}(\delta h)=2 \pi \delta_{p} .$$
Define a new coordinate
$$w=T z .$$
Changing coordinates, we have that
$$\mathcal{L}_{T, z}^{h}=\left(\Delta_{D}+\partial_{w}^{2}\right)+w^{2} \partial_{w}^{2}+6 w \partial_{w}+4=\Delta_{\mathrm{cyl}}+w^{2} \partial_{w}^{2}+6 w \partial_{w}+4=\mathcal{L}_{1, w}^{h}$$
where $\Delta_{\text {cyl }}$ is the Laplacian on the Riemannian product $D \times \mathbb{R}_{w}$, and
$$\mathcal{L}_{1, w}^{h}(\delta h)=T 2 \pi \delta_{p},$$
where $\delta_{p}$ now refers to a delta function with respect to the coordinate $w$.
Now let $y=a+i b$ be a Kähler normal coordinate on $D$ in a neighborhood $U$ of the singular point $p_{D}$ and define
$$r_{w}=\sqrt{|y|^{2}+w^{2}}=\sqrt{a^{2}+b^{2}+w^{2}}$$
on $U$. Then if $\omega_{0}$ is the standard metric and $\Delta_{0}=\left(\partial_{a}^{2}+\partial_{b}^{2}\right)$ is the standard Laplacian in these coordinates,
$$\Delta_{D}-\Delta_{0}=\mathcal{O}\left(r_{w}^{2}\right) \mathcal{D},$$
where $\mathcal{D}$ is a second-order differential operator with continuous coefficients with respect to $y$ and $w$. Let $\mathcal{R}=w^{2} \partial_{w}^{2}+6 w \partial_{w}+4$. Since
$$\Delta_{\mathrm{cyl}}\left(r_{w}^{-1}\right)=4 \pi \delta_{p}$$
in the sense of distributions, we find that
$$\begin{aligned}
\mathcal{L}_{1, w}^{h}\left(\delta h-\frac{T}{2 r_{w}}\right) & =\mathcal{L}_{1, w}^{h}(\delta h)-\left(\Delta_{0}+\partial_{w}^{2}\right)\left(\frac{T}{2 r_{w}}\right)-\left(\Delta_{D}-\Delta_{0}\right)\left(\frac{T}{2 r_{w}}\right)-\mathcal{R}\left(\frac{T}{2 r_{w}}\right) \\
& =T g^{0, \alpha}(a, b, w)+\frac{T p^{3}(a, b, w)}{r_{w}^{4}}+\frac{T p^{4}(a, b, w)}{r_{w}^{5}},
\end{aligned}$$
where $p^{k}(a, b, w)$ is a homogeneous polynomial of degree $k$ in $a, b, w$ with coefficients independent of $T$. Lemma 3.7 plus Schauder regularity give that
$$\delta h=\frac{T}{2 r_{w}}+T g^{2, \alpha}+T w^{1}$$

Equation 3.26 yields a similar expression for $\delta \chi$. By Equation 2.14, we have that for some smooth function $g^{\infty}$ on $D$,
$$\begin{aligned}
\delta \chi & =h_{0}^{-1} \delta h+2 \int z \delta h d z+z g^{\infty} \\
& =\frac{w^{2}+1}{T^{2}}\left(\frac{T}{2 r_{w}}+T g^{2, \alpha}+T w^{1}\right)+\frac{2}{T} \int\left(\frac{w}{2 r_{w}}+w g^{2, \alpha}+w w^{1}\right) d w+z g^{\infty} \\
& =\frac{1}{2 T r_{w}}+\frac{r_{w}}{T}+T^{-1} g^{2, \alpha}+T^{-1} w^{1}
\end{aligned}$$
Since $r_{w} \in \mathcal{W}^{1}$, this implies that
$$\delta \chi=\frac{1}{2 T r_{w}}+T^{-1} g^{2, \alpha}+T^{-1} w^{1}$$
Remark 3.8. We can repeat the above analysis on an arbitrary coordinate path $U$ on $D$. If $U$ does not contain the singular point, we find that
$$\left.\delta h\right|_{U}=T g^{2, \alpha}+T w^{1} .$$
Since $D$ is compact, this implies that
$$\delta h=\frac{T}{2 r_{w}}+T g^{2, \alpha}+T w^{1} \quad \text { on } D \times\left[-C_{2}, C_{2}\right]_{w} .$$
Similarly,
$$\delta \chi=\frac{1}{2 T r_{w}}+T^{-1} g^{2, \alpha}+T^{-1} w^{1} \quad \text { on } D \times\left[-C_{2}, C_{2}\right]_{w} .$$

\section*{4. Construction of the Singular $S^{1}$ Fibration Over $D \times[-1,1 / 2]$}

In Section 2, we derived a system of equations sufficient to define a Kähler-Einstein metric on an $S^{1}$ fibration over $D \times[-1,1 / 2] \backslash\{p\}$. In Section 3, we constructed the data $(\chi, h)=\left(\chi^{T}, h^{T}\right)$ of a family of approximate solutions to this system parameterized by $T \gg 0$. As noted in Section 2.2, there is a gauge freedom in the choice of connection on the resulting $S^{1}$ fibration. Now we will make a choice of connection such that the $S^{1}$ fibration can be completed over the singular point to a $C^{2, \alpha}$ fibration $\mathcal{M}$, allowing us to define the family $\omega_{T}$ of approximately Kähler-Einstein metrics on $\mathcal{M}$. To motivate this choice, we first consider two spaces on which we aim to model the geometry of $\mathcal{M}$ : the Taub-NUT space, to describe the behavior near $p$, and the Calabi model space, to describe the behavior as $z$ approahces the ends of the interval [-1, 1/2]. Our techniques in this section follow [19] Section 4.1.

\subsection*{4.1. Two model spaces.}
4.1.1. The Taub-NUT space. Let $u_{1}, u_{2}$ be coordinates on $\mathbb{C}^{2}$ and $y, \bar{y}, w$ coordinates on $\mathbb{R}^{3}=\mathbb{C} \oplus \mathbb{R}$. The Hopf fibration $\pi_{H}: \mathbb{C}^{2} \backslash\{(0,0)\} \rightarrow \mathbb{R}^{3} \backslash\{(0,0,0)\}$ is an $S^{1}$ fibration given by
$$\pi_{H}\left(u_{1}, u_{2}\right)=\left(u_{1} u_{2}, \frac{1}{2}\left(\left|u_{1}\right|-\left|u_{2}\right|^{2}\right)\right)=(y, w) .$$
It is checked that if $r=\sqrt{|y|^{2}+w^{2}}$, then
$$g_{\mathbb{C}^{2}}=\frac{1}{2 r} \pi_{H}^{*} g_{\mathbb{R}^{3}}+2 r \Theta_{0}^{2},$$
where
$$\Theta_{0}=\frac{1}{2 r} J \pi_{H}^{*} d w,$$
and $J$ is the standard complex structure on $\mathbb{C}^{2}$ with the convention $J d y=-i d y$. The Taub-NUT space is constructed by changing $\frac{1}{2 r} \rightarrow \frac{1}{2 r}+a$ for some constant $a>0$. The resulting metric is still complete and Ricci flat.

Definition 4.1. Fix $a>0$. The Taub-NUT space with parameter $a$ on $\mathbb{C}^{2}$ is
$$g_{T N, a}=\left(\frac{1}{2 r}+a\right) \pi_{H}^{*} g_{\mathbb{R}^{3}}+\left(\frac{1}{2 r}+a\right)^{-1} \Theta^{2},$$
where
$$\Theta=\left(\frac{1}{2 r}+a\right) J \pi_{H}^{*} d w .$$

The Taub-NUT space is invariant under the $S^{1}$ action on $\mathbb{C}^{2}$ that the rotates the fibers of $\pi_{H}$, so as in the discussion in Section 2.2, the Kähler form of the Taub-NUT space $g_{T N, a}$ is
$$\omega_{T N, a}=\left(\frac{1}{2 r_{w}}+a\right) \pi_{H}^{*} \omega_{\mathbb{C}}+d w \wedge \Theta$$
and
$$d \Theta=\partial_{w} \pi^{*} \omega_{0}-d w \wedge d^{c}\left(\frac{1}{2 r}+a\right)$$
where $\omega_{0}=\left(\frac{1}{2 r}+a\right) \frac{i}{2} d y \wedge d \bar{y}$ and $d^{c}$ is computed with respect to the complex structure on $\mathbb{C} \subset \mathbb{C} \oplus \mathbb{R}$ (see [19] 2.3).

Note that if we make the change of coordinates $\underline{y}=\frac{a}{b} y, \underline{w}=\frac{a}{b} w$, and $r_{\underline{w}}=$ $\sqrt{|\underline{y}|^{2}+|\underline{w}|^{2}}$, then we have
$$a g_{T N, a}=b \underline{g}_{T N, b}$$
where $\underline{g}_{T N, b}$ is the Taub-NUT metric with parameter $b$ with respect to the new coordinates.
4.1.2. The Calabi model space. Let $\left(D, \omega_{D}\right)$ be a compact curve with $K_{D}$ ample and $\omega_{D}$ negative Kähler-Einstein normalized such that $\omega_{D} \in 2 \pi c_{1}\left(K_{D}\right)$. We can choose a Hermitian metric $\|\cdot\|_{D}$ on $K_{D}$ such that
$$-i \partial \bar{\partial} \log \|\cdot\|_{D}^{2}=\omega_{D} .$$
Our goal is to construct a negative Kähler-Einstein metric with constant -1 on a subset of the total space of $n K_{D}$ for some $n \in \mathbb{Q}$. We hypothesize that there exists such a metric of the form
$$\omega=i \partial \bar{\partial} F\left(-\log \|\cdot\|_{D}^{2 n}\right)$$
for some function $F$. We write $x=-\log \|\cdot\|_{D}^{2 n}$ and view $F$ as a function of $x$.
If locally $\|\cdot\|_{D}^{2}=h|u|^{2}$ for a real function $h(y)$ of a local $D$ coordinate $y$ and fiber coordinate $u$, then by Equation 4.5.
$$-i \partial \bar{\partial} \log \left(\frac{-i \partial \bar{\partial} \log (h)}{\frac{i}{2} d y \wedge d \bar{y}}\right)=i \partial \bar{\partial} \log (h),$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d4154eb1-3a30-4a5c-835a-c3559a1012ab-21.jpg?height=516&width=1409&top_left_y=379&top_left_x=423}
\captionsetup{labelformat=empty}
\caption{Figure 3. The Calabi model space. Let $\left(D, \omega_{D}\right)$ be a compact negative Kähler-Einstein curve with canonical bundle $K_{D}$ and $\|\cdot\|_{D}$ a Hermitian metric on $K_{D}$ with curvature $\omega_{D}$. The Calabi model space is the tubular neighborhood $T_{D}=\{-1 / 2 n<z<0\} \subset n K_{D}$ equipped with the metric $\omega=i \partial \bar{\partial} F\left(-\|\cdot\|_{D}^{2 n}\right)$.}
\end{figure}
which will be satisfied if
$$-\frac{h \partial \bar{\partial} h-\partial h \wedge \bar{\partial} h}{h^{2}}=\frac{i}{2 h} d y \wedge d \bar{y},$$
or equivalently
$$i \partial \bar{\partial} x=n \frac{i}{2 h} d y \wedge d \bar{y}$$
Taking the Ricci curvature of $\omega$ and applying Equation 4.7, we find that it is sufficient to solve the ordinary differential equation
$$\log \left(F^{\prime} F^{\prime \prime}\right)+\frac{x}{n}-F=C$$
for any constant $C$.
The generator of the natural $S^{1}$ action on $n K_{D}$ is
$$\xi=i\left(u \partial_{u}-\bar{u} \partial_{\bar{u}}\right),$$
so if a metric is defined by Equation 4.6,
$$h^{-1}=\|\xi\|_{\omega}^{2}=2 \frac{d^{2} F}{d x^{2}} .$$
In addition, by Cartan's formula, $\left.\iota_{\xi} \omega=i d \xi\right\lrcorner \bar{\partial} F(x)$, so
$$z(x)=\frac{d F}{d x}-\frac{1}{n}$$
is a moment map for such a metric. Let
$$\mu(z)=\frac{n z(x)^{3}}{3}+\frac{z(x)^{2}}{2}$$
and define
$$F(x)=\log (\mu(z(x)))+\frac{x}{n} .$$

Then
$$z(x)=\left(\frac{\mu^{\prime}}{\mu}\right) \frac{d z}{d x},$$
while
$$h^{-1}=2 \frac{d z}{d x}=2\left(\frac{z \mu}{\mu^{\prime}}\right),$$
and it is easily verified that $F$ satifies Equation 4.8.
By the discussion in Section 2, $\omega$ satisfies Equation 2.1. A computation with Equations 2.1 and 4.6 then gives that $\tilde{\omega}=(1+n z) \omega_{D}$.

Note that
$$x=\int^{z} \frac{n s+1}{\frac{n s^{3}}{3}+\frac{s^{2}}{2}} d s+C$$
The integrand is positive for $-1 / n<z<0$. Restricting $z$ to this interval, we see that since $x \rightarrow \infty$ near the zero section, $z$ increases towards the zero section as well. We define the Calabi model space as the subset
$$T_{D}=\{-1 / 2 n<z<0\} \subset n K_{D}$$
equipped with the metric $\omega$. This space is punctured along the zero section and has a "tubular" boundary.

For convenience of notation we consider the $n=0$ case as part of this family. In this case the metric takes the $D$-invariant form described in Equation 2.13 and we define $T_{D}=\{-1<z<0\}$.
4.2. Construction of $\mathcal{M}^{*}$. Our neck region $\mathcal{M}$ should resemble a Calabi model space at each end, but the two Calabi model spaces have different degrees and are oriented in opposite directions. Concretely, if $\Theta=h J d z$ as in Equation 2.2 and taking $k_{ \pm}$as in the statement of Theorem 1.1, near $\partial \mathcal{M}_{-}$we must have that
$$h=\frac{k_{-} z+1}{\frac{2}{3} k_{-} z^{3}+z^{2}+T^{-2}}$$
while near $\partial \mathcal{M}_{+}$, we must have that
$$h=\frac{k_{+} z+1}{\frac{2}{3} k_{+} z^{3}+z^{2}+T^{-2}} .$$
Note that if we interpret the negative sign of $k_{+}$as part of the $z$ coordinate, $\Theta$ behaves as if $z$ increases towards the zero section, as in our discussion of the Calabi model space. This explains why $k_{-} \geq 0$ and $k_{+} \leq 0$.

Recall the 2-form $\Gamma=\partial_{z} \tilde{\omega}-d z \wedge d^{c} h$ on $D \times[-1,1 / 2] \backslash\{p\}$. By Equation 2.2. $d \Theta=\Gamma$, so $\Gamma$ is closed. By Lemma 4.2, $\frac{1}{2 \pi} \Gamma$ is the curvature of a connection form of a singular $S^{1}$ bundle over $D \times[-1,1 / 2]$. This $S^{1}$ bundle will become the manifold $\mathcal{M}$ underlying our family of metrics, and the change from $k_{-}$to $k_{+}$will correspond to a change in the degree of its restriction to $D$.

In Section 2.2.2 we made the choice to add a singularity of the form $2 \pi \delta_{p}$ to Equation 2.11. We can now see that this singularity increments the degree of the circle bundle corresponding to $\Gamma$ by one, corresponding to the assumption that $k_{-}-k_{+}=1$. Larger increments between $k_{-}$and $-k_{+}$are achieved by adding multiple separate singular points to the neck region, for instance by choosing several points $p_{1}, \ldots, p_{n}$ on $D \times\{0\}$ and changing the inhomogeneous term to $2 \pi \sum_{i=1}^{n} \delta_{p_{i}}$. We then add the linearized solutions constructed in Section 3 and the analysis goes through without change.

Lemma 4.2. For all $T>0, \frac{1}{2 \pi} \Gamma \in H^{2}(D \times[-1,1 / 2] \backslash\{p\} ; \mathbb{R})$ is integral.
Proof. By a Mayer-Vietoris argument it suffices to show that $\frac{1}{2 \pi} \Gamma$ integrates to an integer over a slice $D \times\left\{z_{0}\right\}$ for some $z_{0} \neq 0$ and over the boundary of a ball
$$S_{\epsilon}(p)=\left\{q: r_{w}(q) \leq \epsilon\right\}$$
for some sufficiently small $\epsilon>0$.
For the first integral, note that since
$$\partial_{z}^{2} \tilde{\omega}=-\left(\Delta_{D} h\right) \omega_{D},$$
away from $z=0$, we have that
$$\partial_{z}\left[\partial_{z} \tilde{\omega}\right]=\left[\partial_{z}^{2} \tilde{\omega}\right]=0 \in H^{2}(D ; \mathbb{R}),$$
and therefore $\left[\partial_{z} \tilde{\omega}\right]$ is constant in $z$. However, by Proposition 3.6,
$$\partial_{z} \tilde{\omega}=\left(k_{ \pm}+\mathcal{O}\left(T^{-3}\right)\right) \omega_{D}$$
for large $z$. Thus letting $|z| \rightarrow \infty$ (see Remark 3.5) shows that $\left[\partial_{z} \tilde{\omega}\right]=k_{ \pm}\left[\omega_{D}\right]$. The component $d z \wedge d^{c} h$ does not contribute to the integral of $\Gamma$ over $D$.

For the second integral, observe that by Stokes' theorem,
$$\int_{\partial S_{\epsilon}(p)} \frac{1}{2 \pi} \Gamma=\lim _{\epsilon^{\prime} \rightarrow 0} \int_{\partial S_{\epsilon^{\prime}}(p)} \frac{1}{2 \pi} \Gamma .$$
Now by Equation 3.27 we have for $r_{w}$ small that
$$\partial_{z} \tilde{\omega}=\left(-\frac{T z}{4 r_{w}^{3}}\right) i d y \wedge d \bar{y}+\mathcal{O}\left(\log \left(r_{w}\right)\right)$$
and by Equation 3.26 we have that
$$d z \wedge d^{c} h=\frac{-i T}{4 r_{w}^{3}} d z \wedge(y d \bar{y}-\bar{y} d y)+\mathcal{O}\left(\log \left(r_{w}\right)\right)$$
But
$$d(z d y \wedge d \bar{y}-y d z \wedge d \bar{y}+\bar{y} d z \wedge d y)=3 d z \wedge d y \wedge d \bar{y},$$
so
$$\begin{aligned}
\lim _{\epsilon^{\prime} \rightarrow 0} \int_{\partial S_{\epsilon^{\prime}}(p)} \frac{1}{2 \pi} \Gamma & =\lim _{\epsilon^{\prime} \rightarrow 0} \int_{S_{\epsilon^{\prime}}(p)}-\frac{3 i T}{8 \pi\left(\epsilon^{\prime}\right)^{3}} d z \wedge d y \wedge d \bar{y}+\mathcal{O}\left(\left(\epsilon^{\prime}\right)^{2} \log \left(\epsilon^{\prime}\right)\right) \\
& =-\lim _{\epsilon^{\prime} \rightarrow 0} \int_{S_{\epsilon^{\prime}}(p)} \frac{3}{4 \pi\left(\epsilon^{\prime}\right)^{3}}\left(\frac{i}{2} d y \wedge d \bar{y}\right) \wedge d w \\
& =-1
\end{aligned}$$
as desired. \(\square\)

By Lemma 4.2, there is an $S^{1}$ bundle $\pi: \mathcal{M}^{*} \rightarrow D \times[-1,1 / 2] \backslash\{p\}$ with connection form $-i \Theta^{\prime}$ whose curvature is $-i \Gamma$. The connection form $-i \Theta^{\prime}$ is not unique, but we fix an arbitrary choice. Note that the spaces $\mathcal{M}^{*}$ are diffeomorphic for all $T$, since changing $T$ only rescales all data with respect to the $z$ coordinate.
4.3. Compactification of $\mathcal{M}^{*}$. Now we can construct a compactification of $\mathcal{M}^{*}$ modeled on the Taub-NUT space. As manifolds this only involves adding a point to $\mathcal{M}^{*}$ and it is easily seen that the resulting spaces will be diffeomorphic for all $T$. Let $(y, \bar{y}, w)$ be the coordinates on $D \times[-1,1 / 2]$ in the punctured neighborhood $U^{\prime}=U \times[-1,1 / 2] \backslash\{p\}$, where $U$ is as defined in Section 3.3. If $V=\pi^{-1}\left(U^{\prime}\right)$, then in some coordinates $u_{1}, u_{2}, V$ gives a subset of $\mathbb{C}^{2} \backslash\{0\}$, and we can define the Hopf fibration $\pi^{\prime}: V \rightarrow U^{\prime}$ by
$$\left(u_{1}, u_{2}\right) \rightarrow\left(u_{1} u_{2}, \frac{1}{2}\left(\left|u_{1}\right|^{2}-\left|u_{2}\right|^{2}\right)\right) .$$
Now $\pi$ and $\pi^{\prime}$ are $S^{1}$ fibrations of the same degree, so there is an $S^{1}$-equivariant smooth map $\phi: V \rightarrow \mathcal{M}$, diffeomorphic with its image, such that $\phi^{*} \pi=\pi^{\prime}$. In other words, we can choose complex-valued (though not necessarily holomorphic) coordinates $u_{1}$ and $u_{2}$ such that $\pi$ is the Hopf fibration given in coordinates by Equation 4.9, i.e. $y=u_{1} u_{2}, w=\frac{1}{2}\left(\left|u_{1}\right|^{2}-\left|u_{2}\right|^{2}\right)$, and the connection is given by $\phi^{*}\left(-i \Theta^{\prime}\right)$.

From now on we will assume we have made such a transformation and take $u_{1}, u_{2}$, and $\pi$ as in the Hopf fibration. In addition, we define in these coordinates
$$s^{2}=\left|u_{1}\right|^{2}+\left|u_{2}\right|^{2} .$$
Notice that
$$\pi^{*} r_{w}=\frac{1}{2} s^{2} .$$

The connection form determines the metric on $\mathcal{M}^{*}$ via Equation 2.1. However, our arbitrary choice of connection may not have the desired behavior near $p$. Now we modify $\mathcal{M}^{*}$ by a Gauge transformation so that near $p$ the metric on $\mathcal{M}^{*}$ differs from the Taub-NUT space by a form of sufficiently high regularity. This will give a $C^{2, \alpha}$ compactification of $\mathcal{M}^{*}$ over $p$, completing our construction of the singular $S^{1}$ fibration $\mathcal{M}$ and its $C^{2, \alpha}$ Kähler structure.