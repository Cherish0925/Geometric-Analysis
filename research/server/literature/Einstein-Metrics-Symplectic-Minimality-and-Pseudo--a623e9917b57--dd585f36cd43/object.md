# Einstein Metrics, Symplectic Minimality, and Pseudo ...

- Category: papers
- Identity: arxiv:math/0409290
- Content status: fulltext_ok

---

---
source_file: math_0409290.pdf
converter: mathpix
format: mmd
---

\title{
Einstein Metrics, Symplectic Minimality, and Pseudo-Holomorphic Curves
}

\author{
Claude LeBrun* \\ SUNY Stony Brook
}

\begin{abstract}
Let $\left(M^{4}, g, \omega\right)$ be a compact, almost-Kähler Einstein manifold of negative star-scalar curvature. Then $(M, \omega)$ is a minimal symplectic 4-manifold of general type. In particular, $M$ cannot be differentiably decomposed as a connected sum $N \# \overline{\mathbb{C P}}_{2}$.
\end{abstract}

\section*{1 Introduction}

A smooth Riemannian $n$-manifold $(M, g)$ is said to be Einstein if its Ricci curvature, considered as a function on the unit tangent bundle of $M$, is constant. If $n \geq 3$, this is equivalent [6] to saying that $g$ satisfies
$$r=\frac{s}{n} g,$$
where $r$ and $s$ respectively denote the Ricci tensor and scalar curvature of $g$, because equation (1) and the contracted Bianchi identity $2 \operatorname{div} r=d s$ together imply that $s$ must be constant if $n \neq 2$. As will be emphasized below, the sign of this constant plays an important rôle in much of the theory of Einstein manifolds.

Kähler geometry provides one of our richest sources of compact Einstein manifolds. Recall that a Riemannian manifold is said to be Kähler if it admits a non-degenerate 2-form with vanishing covariant derivative. When this happens, there must in fact be a non-degenerate closed 2-form $\omega$ which

\footnotetext{
*Supported in part by NSF grant DMS-.
}
can be expressed as $\omega=g(J \cdot, \cdot)$ for some integrable almost-complex structure $J$ on $M$. One then says that the closed 2-form $\omega$ is the Kähler form of $(M, g, J)$, and its de Rham class $[\omega] \in H^{2}(M, \mathbb{R})$ is called the Kähler class. A celebrated result of Aubin [4] and Yau [32] tells us precisely when a compact complex manifold $(M, J)$ admits a compatible Kähler-Einstein metric with $s<0$; namely, this happens if and only if there is a holomorphic projective embedding $M \hookrightarrow \mathbb{C P}_{k}$ for which the generic hyperplane section $M \cap \mathbb{C P}_{k-1}$ is Poincaré dual to a negative multiple of $c_{1}(M, J)$.

When $n=4$, a Kähler-Einstein metric $g$ with $s<0$ can consequently exist only if $(M, J)$ is a minimal complex surface of general type [5]. Recall that if ( $N, J_{N}$ ) is any complex surface, and $p \in N$ is any point, one may obtain a new complex surface ( $\tilde{N}, J_{\tilde{N}}$ ) by replacing $p$ with a $\mathbb{C P}_{1}$ of self-intersection -1. The resulting complex surface $N$ is called the blow-up of $N$ at $p$, and is diffeomorphic to the connected sum $N \# \overline{\mathbb{C P}}_{2}$. A complex surface is said to be minimal if it is not the blow-up of some other complex surface. Any compact complex surface $M$ can be obtained from some minimal complex surface $X$, called a minimal model for $M$, by blowing up a finite number of times. A compact complex surface is said to be of general type if the dimension of the space of holomorphic sections of $K^{\otimes j}$ is quadratic in $j \gg 0$, where $K=\Lambda^{2,0}$ denotes the canonical line bundle of the complex surface. A key facet of Kodaira's classification theory [5] is the assertion that a complex surface is of general type iff it has a minimal model with $c_{1}^{2}>0$ and with $c_{1} \cdot[\omega]<0$ for some (and hence any) Kähler class.

The purpose of the present article is to explore a symplectic generalization of the aforementioned link between complex-surface minimality and the existence of Kähler-Einstein metrics. Recall that a closed non-degenerate 2-form $\omega$ on a smooth manifold $M$ is called a symplectic form, and the pair $(M, \omega)$ is then called a symplectic manifold [23]. The modern theory of 4-dimensional symplectic manifolds substantially parallels the theory of compact complex surfaces. In particular, if $\left(N, \omega_{0}\right)$ is a symplectic 4-manifold, one can construct a 1-parameter family of symplectic structures $\omega_{\epsilon}$ on the connect sum $\tilde{N}=N \# \overline{\mathbb{C P}}_{2}$ by removing a standard ball of volume $\epsilon^{2} / 2$ from $\left(N, \omega_{0}\right)$, and replacing it with a symplectic 2-sphere of area $\epsilon$ and self-intersection -1; any of the symplectic manifolds $\left(\tilde{N}, \omega_{\epsilon}\right)$ obtained by this construction is then called [21, 22] a symplectic blow-up of $(N, \omega)$. As in the complex case, every symplectic 4-manifold can be obtained from a minimal model by blowing up a finite number of times, and, in keeping with the complex case, a symplectic 4-manifold is said to be of general type [15, 18] iff it has a minimal model
satisfying $c_{1}^{2}>0$ and $c_{1} \cdot[\omega]<0$.
One of the most striking consequences of the existence of a symplectic structure on a 4-manifold is that it implies the existence of solutions of suitable perturbations of the Seiberg-Witten equations, for any Riemannian metric [28]. This in turn leads to non-trivial constraints on the Riemann curvature tensor [15, 16, 17, 31], so the existence of a symplectic structure exerts a ghostly influence over ostensibly unrelated Riemannian geometries on a 4-manifold. In particular, one obtains the following obstruction to the existence of Einstein metrics [17]:

Theorem 1.1 Suppose that $\left(X, \omega_{X}\right)$ is a minimal symplectic 4-manifold of general type. Then the differentiable manifold $M=X \# k \overline{\mathbb{C P}}_{2}$ does not admit Einstein metrics if $k \geq c_{1}^{2}(X) / 3$.

Thus, the existence of Einstein metrics is obstructed on symplectic manifolds which are "sufficiently non-minimal," even without requiring that the putative metric be in any way related to the symplectic form. In this article, we will see that one can do distinctly better if the metric and symplectic form are required to be related in a manner reminiscent of Kähler geometry.

Any symplectic manifold $(M, \omega)$ admits almost-complex structures
$$J: T M \rightarrow T M, \quad J^{2}=\mathbf{- 1},$$
such that the tensor field $g$ defined by
$$g(v, w)=\omega(v, J w)$$
is a Riemannian metric. One then says that the metric $g$ is adapted to $\omega$, and the triple $(M, g, \omega)$ is called an almost-Kähler manifold. If $(M, g)$ is a Riemannian 4-manifold, then $(M, g, \omega)$ is almost-Kähler iff, for an appropriate orientation of $M, \omega$ is a self-dual harmonic 2-form with $|\omega| \equiv \sqrt{2}$. If $(M, g)$ is an oriented compact Riemannian 4-manifold with $b_{+}(M) \neq 0$, the Hodge theorem therefore tells us that there is an open dense set of $M$ on which $g$ is conformally related to an almost-Kähler metric, since the harmonicity and self-duality of $\omega$ are conformally invariant in dimension 4. In other words, the almost-Kähler condition imposes no constraint at all on the local conformal geometry of a 4-manifold. It might therefore seem implausible for such a weak condition to have a ponderable Riemannian impact.

Nevertheless, the so-called Goldberg conjecture [10], that every compact almost-Kähler Einstein manifold is actually Kähler, remains completely
open. Moreover, Sekigawa [27] has shown that the conjecture is actually true for metrics with $s \geq 0$. The $s<0$ case remains a mystery, even in dimension 4, although some encouraging results have recently been obtained concerning restricted versions of the problem in which the curvature tensor is also required to satisfy supplementary algebraic conditions [1, 2, 3]. On the other hand, it should be emphasized that, although Goldberg did not clearly stipulate that the manifolds in question are required to be compact, counter-examples [3] due to K.P. Tod show that the naïve local version of the conjecture is certainly false in all dimensions $\geq 4$.

If one believed the 4-dimensional case of the Goldberg conjecture to be true, one would consequently expect almost-Kähler Einstein metrics with $s<0$ to only exist on minimal complex surfaces. On the other hand, if one believed the conjecture to be false, it might be helpful to know whether it would be a waste of time to look for counter-examples on non-minimal symplectic 4-manifolds. Thus, even for those who, like the author, remain agnostic as to the ultimate validity of the conjecture, it must seem reasonable to ask what current technology can tell us regarding the symplectic minimality of 4-dimensional almost-Kähler Einstein manifolds.

The main results of this paper involve the so-called star-scalar curvature $s^{\star}$ of an almost-Kähler 4-manifold ( $M, g, \omega$ ), as defined by
$$s^{\star}=2 R(\omega, \omega),$$
where $R$ is the Riemann curvature tensor of $g$. For a Kähler manifold, this coincides with the usual scalar curvature $s$ of $g$, but for a general almost-Kähler manifold one merely has $s^{\star} \geq s$. Our first main result is the following:

Theorem A Suppose that $(M, g, \omega)$ is a compact almost-Kähler Einstein 4-manifold with $s^{\star}<0$. Then $(M, \omega)$ is a minimal symplectic 4-manifold of general type. Moreover, $M$ cannot be differentiably decomposed as a connect sum $N \# \overline{\mathbb{C P}}_{2}$.

As is the case for Theorem 1.1 the proof of Theorem A ultimately rests on a foundation of Seiberg-Witten theory, but in the present case the Seiberg-Witten equations enter only very indirectly, via Taubes' existence theorem for pseudo-holomorphic curves [30]. Let us now recall the definition of these last objects, which were first introduced into symplectic geometry by Gromov [12]. Suppose that $(M, g, \omega)$ is an almost-Kähler manifold, and let $J$ be the associated almost-complex structure on $M$, as determined by equation (2). If
$\Sigma$ is a compact (but possibly disconnected) Riemann surface, with complex structure tensor $J_{\Sigma}: T \Sigma \rightarrow T \Sigma$, one says that a smooth, locally non-constant map $\psi: \Sigma \rightarrow M$ is a pseudo-holomorphic curve (or, to emphasize the fixed choice of almost-complex structure, a J-holomorphic curve) if its differential $\psi_{*}$ is almost-complex-linear, in the sense that
$$J \circ \psi_{*}=\psi_{*} \circ J_{\Sigma} .$$
Taubes' results allow one to predict the existence of a certain pseudoholomorphic curve in any symplectic manifold $M$ that can be decomposed as a connect sum $N \# \overline{\mathbb{C P}}_{2}$, and Theorem A is then proved by calculating the evaluation of $c_{1}(M, J)$ on the homology class of this Riemann surface in two different ways, with contradictory results.

In the absence of some a priori reason why a compact almost-Kähler Einstein 4-manifold with $s<0$ should necessarily also have $s^{\star}<0$ everywhere, however, Theorem A can be of only limited interest. Nonetheless, the same techniques used to prove Theorem A lead to similar conclusions even when the maximum of $s^{\star}$ is allowed to be positive:

Theorem B Suppose that $(M, g, \omega)$ is an almost-Kähler Einstein 4-manifold with $s<0$ and with
$$s^{\star} \leq-\frac{s}{m}$$
for some constant $m>1$. Suppose, moreover, that $b_{+}(M)>1$. Let $\left(X, \omega^{\prime}\right)$ be a symplectic minimal model for $M$, and let $k$ denote the number of blow-ups used to obtain $M$ from $X$. Then
$$k<\frac{1}{m+2} c_{1}^{2}(X) .$$

Now Oguri and Sekigawa [24] claim that any almost-Kähler Einstein 4manifold with $s<0$ automatically satisfies $s^{\star} \leq-s / 6$. If this is correct, the hypotheses of Theorem B should always hold for $m=6$, thereby allowing one to conclude that blow-ups $X \nexists k \overline{\mathbb{C P}}_{2}$ of symplectic manifolds $X^{4}$ with $b_{+}(X)>1$ never admit almost-Kähler Einstein metrics when $k \geq c_{1}^{2}(X) / 8$. This would certainly represent a considerable sharpening of Theorem 1.1 in the almost-Kähler case. Better estimates for the global maximum of $s^{\star}$ might thus appear to represent a compelling topic for future research.

\section*{2 Almost-Kähler Geometry}

Suppose that $(M, g, \omega)$ is an almost-Kähler 4-manifold. That is, we suppose that $g$ is a Riemannian metric, that $\omega$ is a symplectic form, and that $J_{a}{ }^{b}=$ $\omega_{a c} g^{b c}$ is an almost-complex structure. Orienting our 4-manifold $M$ so that the 4-form $\omega \wedge \omega$ is positive, this is equivalent to saying that $\omega$ is a closed self-dual 2-form on $(M, g)$ whose point-wise norm is everywhere $\sqrt{2}$.

The star-scalar curvature of $(M, g, \omega)$ is defined to be
$$s^{\star}=2 R(\omega, \omega)=\frac{1}{2} R^{a b c d} \omega_{a b} \omega_{c d},$$
where $R$ denotes the Riemann curvature tensor of $g$. This will coincide with the usual scalar curvature $s$ of $g$ if and only if $(M, g, J)$ is a Kähler manifold. Indeed, the Weitzenböck formula for a closed self-dual 2-form tells us that
$$0=\frac{1}{2} \Delta|\omega|^{2}+|\nabla \omega|^{2}-2 W^{+}(\omega, \omega)+\frac{s}{3}|\omega|^{2},$$
and plugging in $|\omega|^{2} \equiv 2$ thus yields
$$s^{\star}=2\left[W^{+}(\omega, \omega)+\frac{s}{12}|\omega|^{2}\right]=s+|\nabla \omega|^{2},$$
so that $s^{\star} \geq s$, with equality everywhere precisely when $(M, g, \omega)$ is Kähler.
The almost-complex structure $J$ induces a decomposition
$$\Lambda_{\mathbb{C}}^{2}=\Lambda^{1,1} \oplus \Lambda^{2,0} \oplus \Lambda^{0,2}$$
of the complex-valued 2-forms, and this is related to the self-dual/anti-selfdual decomposition
$$\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$$
induced by $g$ and the orientation by
$$\begin{aligned}
\Lambda_{\mathbb{C}}^{+} & =\mathbb{C} \omega \oplus \Lambda^{2,0} \oplus \Lambda^{0,2} \\
\Lambda^{1,1} & =\mathbb{C} \omega \oplus \Lambda_{\mathbb{C}}^{-}
\end{aligned}$$
In all these formulæ, the summands are mutually orthogonal with respect to the Hermitian inner product induced by $g$. The line bundle $\Lambda^{2,0}$ is of particular interest, and is called the canonical line bundle $K$ of $(M, J)$. Its
dual $L=K^{-1}$ is called the anti-canonical line bundle, and may be naturally identified with $\bar{K}=\Lambda^{0,2}$ by using the Hermitian inner product induced by $g$.

The anti-canonical line bundle $L$ of an almost-Kähler 4-manifold turns out to carry a natural connection, originally discovered by Blair [7], and later rediscovered by Taubes [28] via a completely different line of reasoning. The purpose of this section is to point out a remarkable curvature property of this connection that holds when the metric $g$ is also Einstein.

Proposition 2.1 Let ( $M, g, \omega$ ) be an almost-Kähler Einstein 4-manifold. Then the anti-canonical line bundle $L=K^{-1}$ of $M$ carries a natural Hermitian connection whose curvature 2-form $F$ satisfies
$$i F=\eta+\frac{s+s^{\star}}{8} \omega+\frac{s-s^{\star}}{8} \hat{\omega},$$
where
$$\eta=W^{+}(\omega)^{\perp} \in \Lambda^{2,0} \oplus \Lambda^{0,2}$$
while
$$\hat{\omega} \in \Lambda^{-}$$
is defined only on the open set $U=\left\{p \in M \mid\left(s^{\star}-s\right)(p) \neq 0\right\}$, satisfies
$$|\hat{\omega}|=|\omega| \equiv \sqrt{2},$$
and corresponds to an almost-complex structure $\hat{J}$ on $U \subset M$ which is compatible with the anti-symplectic orientation of $M$.

We now give a concise proof of this result in terms of the Penrose spinor calculus [25, 26, 31], a brief summary of which may be found in Appendix A below. On any spin open subset of $M$, we can uniquely express our self-dual harmonic 2-form as
$$\omega_{a b}=\omega_{A B} \varepsilon_{A^{\prime} B^{\prime}}$$
where
$$\omega_{A B}=\bar{\omega}_{A B}=\omega_{(A B)}, \quad \omega^{A B} \omega_{A B}=2 .$$
Factoring $\omega$, we therefore locally have
$$\omega_{A B}=2 i \phi_{(A} \bar{\phi}_{B)},$$
where
$$\phi_{A} \bar{\phi}^{A}=1 .$$

Now $\omega$ is co-closed, so
$$\nabla^{A A^{\prime}} \omega_{A B}=0 .$$
But we also have
$$\nabla^{A A^{\prime}} \varepsilon_{A B}=0,$$
and
$$\varepsilon_{A B}=2 \phi_{[A} \bar{\phi}_{B]},$$
so it follows that
$$0=\frac{1}{2} \nabla^{A A^{\prime}}\left(-i \omega_{A B}+\varepsilon_{A B}\right)=\nabla^{A A^{\prime}} \phi_{A} \bar{\phi}_{B} .$$
Contracting with $\phi^{B}$, we thus have
$$0=\phi^{B} \nabla^{A A^{\prime}} \phi_{A} \bar{\phi}_{B}=-\nabla^{A A^{\prime}} \phi_{A}+\phi_{A} \phi^{B} \nabla^{A A^{\prime}} \bar{\phi}_{B} .$$
That is,
$$\left(\nabla^{A A^{\prime}}+\frac{i}{2} \vartheta^{A A^{\prime}}\right) \phi_{A}=0,$$
where
$$\vartheta_{A A^{\prime}}=2 i \phi^{B} \nabla_{A A^{\prime}} \bar{\phi}_{B}=2 i \bar{\phi}^{B} \nabla_{A A^{\prime}} \phi_{B} .$$
Notice that $\vartheta=\bar{\vartheta}$, since $\bar{\phi}_{A}=-\phi_{A}$. We interpret this as saying that $\phi$ solves the Dirac equation $\not D^{\theta} \phi=0$ for a specific spin ${ }^{c}$ structure and a specific U(1) connection $\theta$ on its determinant line bundle $L=\Lambda^{2} \mathbb{V}_{+}$. We can then view the local ambiguity $\phi_{A} \leadsto e^{i u / 2} \phi_{A}$ in choosing $\phi$ as simply stemming from a change of local trivialization in the Hermitian line bundle $L$, so that $\phi$ becomes a global unit section of
$$\mathbb{V}_{+}=\mathbb{S}_{+} \otimes L^{1 / 2}$$
where $L$ is concretely the anti-canonical line bundle of $J_{a}{ }^{b}=\omega_{a c} g^{b c}$, and is endowed with a standard connection $\theta$, with connection 1-form given by $i \vartheta$ in our system of local trivializations.

Now $\nabla|\omega|^{2}=0$, so
$$\omega^{B C} \nabla_{A A^{\prime}} \omega_{B C}=0,$$
and hence
$$\phi^{B} \bar{\phi}^{C} \nabla_{A A^{\prime}} \omega_{B C}=0 .$$

But since $\omega$ is co-closed, we have
$$\nabla_{A A^{\prime}} \omega_{B C}=\nabla_{A^{\prime}(A} \omega_{B C)},$$
and, since $\phi$ and $\bar{\phi}$ form a basis for $\mathbb{S}_{+}$, it follows that
$$\nabla_{A A^{\prime}} \omega_{B C}=\alpha_{A^{\prime}} \phi_{A} \phi_{B} \phi_{C}+\bar{\alpha}_{A^{\prime}} \bar{\phi}_{A} \bar{\phi}_{B} \bar{\phi}_{C}$$
for some unique $\alpha_{A^{\prime}}$. Notice that the substitution $\phi \leadsto e^{i u / 2} \phi$ results in the transformation $\alpha \leadsto e^{-3 i u / 2} \alpha$, so that $\alpha$ can invariantly be interpreted as a section of $S S_{-} \otimes L^{-3 / 2}$. In particular, the anti-self-dual 2-form
$$\hat{\omega}_{a b}=\frac{2 i}{|\alpha|^{2}} \alpha_{\left(A^{\prime}\right.} \bar{\alpha}_{\left.B^{\prime}\right)} \varepsilon_{A B}$$
induces an almost-complex structure $\hat{J}_{a}{ }^{b}=\hat{\omega}_{a c} g^{b c}$ on the open set $U \subset M$ where $\nabla \omega \neq 0$. Since equation (3) implies that $|\nabla \omega|^{2}=2|\alpha|^{2}$, it now follows that
$$|\alpha|^{2}=\frac{s^{\star}-s}{2} .$$

The twisted spinor field $\alpha$ also completely encodes the covariant derivative of $\phi$. Indeed,
$$\phi^{B} \nabla_{A A^{\prime}} \phi_{B}=-\phi^{B} \phi^{C} \nabla_{A A^{\prime}} \phi_{B} \bar{\phi}_{C}=\frac{i}{2} \phi^{B} \phi^{C} \nabla_{A A^{\prime}} \omega_{B C}=\frac{i}{2} \bar{\alpha}_{A^{\prime}} \bar{\phi}_{A}$$
and hence
$$\nabla_{A A^{\prime}} \phi_{B}=-\frac{i}{2}\left[\bar{\alpha}_{A^{\prime}} \bar{\phi}_{A} \bar{\phi}_{B}+\vartheta_{A A^{\prime}} \phi_{B}\right] .$$
In other words,
$$\hat{\nabla}_{A A^{\prime}} \phi_{B}=-\frac{i}{2} \bar{\alpha}_{A^{\prime}} \bar{\phi}_{A} \bar{\phi}_{B}$$
where $\hat{\nabla}$ is the spin ${ }^{c}$ connection on $\mathbb{V}_{+}=S S_{+} \otimes L^{1 / 2}$ induced by the U(1) connection $\theta=i \vartheta$ on $L$.

Let us now calculate the curvature of $L$; cf. [2, 9]. Since $L$ carries the connection form $i \vartheta$, its curvature is given by $F=i d \vartheta$, so that
$$\begin{aligned}
i F^{+} & =\varepsilon_{A^{\prime} B^{\prime}} \nabla_{(A}^{\prime} \vartheta_{B) C^{\prime}} \\
i F^{-} & =\varepsilon_{A B} \nabla_{\left(A^{\prime}\right.}^{C} \vartheta_{\left.B^{\prime}\right) C}
\end{aligned}$$

Hence
$$\begin{aligned}
i F_{A B}^{+}= & \nabla_{(A}^{A^{\prime}} \vartheta_{B) A^{\prime}} \\
= & \nabla_{(A}^{A^{\prime}} 2 i \phi^{C} \nabla_{B) A^{\prime}} \bar{\phi}_{C} \\
= & -2 i \phi^{C} \square_{A B} \bar{\phi}_{C}+2 i\left[\nabla_{(A}^{A^{\prime}} \phi^{C}\right] \nabla_{B) A^{\prime}} \bar{\phi}_{C} \\
= & -2 i \phi^{C} W_{A B C}^{+}{ }^{D} \bar{\phi}_{D}-2 i \phi^{C} \frac{s}{24}\left(\varepsilon_{A C} \bar{\phi}_{B}+\varepsilon_{B C} \bar{\phi}_{A}\right) \\
& +2 i\left(-\frac{i}{2}\right)\left[\bar{\alpha}^{A^{\prime}} \bar{\phi}_{(A \mid} \bar{\phi}^{C}+\vartheta_{(A \mid}^{A^{\prime}} \phi^{C}\right]\left(\frac{i}{2}\right)\left[\overline{\bar{\alpha}}_{A^{\prime}} \overline{\bar{\phi}}_{\mid B)} \overline{\bar{\phi}}_{C}+\vartheta_{\mid B) A^{\prime}} \bar{\phi}_{C}\right] \\
= & W_{A B}^{+}{ }^{C D} \omega_{C D}+\frac{s}{12} \omega_{A B}-\frac{1}{4}|\alpha|^{2} \omega_{A B} \\
= & \frac{s+s^{\star}}{8} \omega_{A B}+\eta_{A B}
\end{aligned}$$
where $\eta=\left[W^{+}(\omega)\right]^{\perp}$ is orthogonal to $\omega$.
Similarly, we compute the anti-self-dual part of the curvature of $L$ :
$$\begin{aligned}
i F_{A^{\prime} B^{\prime}}^{-} \quad= & \nabla_{\left(A^{\prime}\right.}^{A} \vartheta_{\left.B^{\prime}\right) A} \\
= & \nabla_{\left(A^{\prime}\right.}^{A} 2 i \phi^{C} \nabla_{\left.B^{\prime}\right) A} \bar{\phi}_{C} \\
= & -2 i \phi^{C} \square_{A^{\prime} B^{\prime}} \bar{\phi}_{C}+2 i\left[\nabla_{\left(A^{\prime}\right.}^{A} \phi^{C}\right] \nabla_{\left.B^{\prime}\right) A} \bar{\phi}_{C} \\
= & i \phi^{C} \stackrel{\circ}{r}_{A^{\prime} B^{\prime} C}^{D} \bar{\phi}_{D} \\
& +2 i\left(-\frac{i}{2}\right)\left[\bar{\alpha}_{\left(A^{\prime} \mid\right.} \bar{\phi}^{A} \bar{\phi}^{C}+\vartheta_{\left(A^{\prime} \mid\right.}^{A} \phi^{C}\right]\left(\frac{i}{2}\right)\left[-\alpha_{\left.\mid B^{\prime}\right)} \phi_{A} \phi_{C}+\vartheta_{\left.\mid B^{\prime}\right) A} \bar{\phi}_{C}\right] \\
= & -\frac{1}{2} \stackrel{\circ}{r}_{A^{\prime} B^{\prime}}^{C D}\left(2 i \phi_{(C} \bar{\phi}_{D)}\right)-\frac{i}{2} \bar{\alpha}_{\left(A^{\prime}\right.} \alpha_{\left.B^{\prime}\right)} \\
= & -\frac{1}{2} \stackrel{\circ}{r}_{A^{\prime} B^{\prime}}^{A B} \omega_{A B}-\frac{i}{2} \alpha_{\left(A^{\prime}\right.} \bar{\alpha}_{\left.B^{\prime}\right)}
\end{aligned}$$
When $g$ is Einstein, $\stackrel{\circ}{r}=0$, and we thus have
$$i F^{+}=\eta+\frac{s+s^{\star}}{8} \omega, \quad i F^{-}=\frac{s-s^{\star}}{8} \hat{\omega},$$
and Proposition 2.1 follows.
Another remarkable consequence of these formulæ is the following [7]:
Proposition 2.2 (Blair) Let $(M, g, \omega)$ be any 4-dimensional compact almost-Kähler manifold. Then
$$\int_{M} \frac{s+s^{\star}}{2} d \mu=4 \pi c_{1} \cdot[\omega] .$$

Proof. Either side can be rewritten as $2 \int_{M} i F^{+} \wedge \omega$. \(\square\)

In particular, since $s^{\star} \geq s$, this implies
Corollary 2.3 For any compact almost-Kähler 4-manifold $(M, g, \omega)$,
$$\int_{M} s^{\star} d \mu \geq 4 \pi c_{1} \cdot[\omega] \geq \int_{M} s d \mu$$

The inequality $s^{\star} \geq s$ is a repetitive motif underlying much of almostKähler geometry, like a basso ostinato. In light of our formulation of Proposition 2.1, it would seem very natural to ask whether one can ever actually have strict inequality $s^{\star}>s$ everywhere. In fact, this never happens in the Einstein case [2]:

Proposition 2.4 (Armstrong) If $(M, g, \omega)$ is a compact 4-dimensional almost-Kähler Einstein manifold, there must be at least one point $p \in M$ at which $s^{\star}=s$.

Proof. Suppose not. Then $\alpha \neq 0$ on all of $M$, and (4) defines an almostcomplex structure $\hat{J}$ on the entire manifold. Moreover, since $\alpha \in \mathbb{S}_{-} \otimes L^{-3 / 2}$, the anti-canonical line bundle of $\hat{J}$ is $L^{-3}$. Thus the reverse-oriented manifold $\bar{M}$ has an almost-complex structure $\hat{J}$ with anti-canonical line bundle $L^{-3}$, whereas $M$ has an almost-complex structure $J$ with anti-canonical line bundle $L$. Hence
$$(2 \chi+3 \tau)(M)=\int_{M} c_{1}^{2}(L)=c_{1}^{2}(M)$$
while
$$\begin{aligned}
(2 \chi-3 \tau)(M) & =(2 \chi+3 \tau)(\bar{M}) \\
& =\int_{\bar{M}} c_{1}^{2}\left(L^{-3}\right) \\
& =-\int_{M}\left[-3 c_{1}(L)\right]^{2} \\
& =-9 \int_{M} c_{1}^{2}(L)=-9 c_{1}^{2}(M),
\end{aligned}$$
so these two homotopy invariants of $M$ must have opposite signs. But, on the other hand, the Hitchin-Thorpe inequality [6, 14] tells us that these
characteristic numbers must both be non-negative; indeed, since $g$ satisfies $\stackrel{\circ}{r}=0$, the Gauss-Bonnet and signature formulæ tell us that
$$(2 \chi \pm 3 \tau)(M)=\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+2\left|W^{ \pm}\right|^{2}\right) d \mu$$
Hence $(M, g)$ must be flat! In particular, $s \equiv 0$ and $s^{\star}=2 W^{+}(\omega, \omega)+\frac{s}{3}=0$, so $s^{\star} \equiv s$, in contradiction to our assumption. \(\square\)

We will specifically make use of the following consequence:
Corollary 2.5 On any compact almost-Kähler Einstein 4-manifold, there is some point at which $\left|W^{+}\right|^{2} \geq s^{2} / 24$.

Proof. Since $2 W^{+}(\omega, \omega)=s^{\star}-\frac{s}{3}$, and since $|\omega|^{2}=2$, there is always an eigenvalue $\lambda$ of $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$with $|\lambda| \geq\left|3 s^{\star}-s\right| / 12$. Since $W^{+}$is trace-free, this implies that
$$\left|W^{+}\right|^{2} \geq \frac{3}{2} \lambda^{2} \geq \frac{\left(3 s^{\star}-s\right)^{2}}{96},$$
and at any point where $s^{\star}=s$ we therefore must have $\left|W^{+}\right|^{2} \geq s^{2} / 24$. \(\square\)

\section*{3 Pseudo-Holomorphic Curves}

We will now use Proposition 2.1 to estimate the pull-back of the curvature of $L$ to a pseudo-holomorphic curve.

Proposition 3.1 Let $(M, g, \omega)$ be a 4-dimensional almost-Kähler Einstein manifold, and let $\psi: \Sigma \rightarrow M$ be a $J$-holomorphic curve in $M$. Then the pull-back $\psi^{*} F$ of the curvature of the anti-canonical line bundle $L \rightarrow M$ satisfies
$$\frac{s}{4} \psi^{*} \omega \leq i \psi^{*} F \leq \psi^{*} \frac{s^{\star}}{4} \omega$$
at each point of the oriented 2-manifold $\Sigma$.

Proof. By Proposition 2.1, the curvature of $L$ satisfies
$$i F=\eta+\frac{s+s^{\star}}{8} \omega+\frac{s-s^{\star}}{8} \hat{\omega},$$
where $\eta \in \Lambda^{2,0} \oplus \Lambda^{0,2}$, and where the last term is understood to mean zero at the locus $s^{\star}=s$ (even though the bounded 2-form $\hat{\omega}$ is undefined there). Since $\psi$ is assumed to be $J$-holomorphic, we therefore have $\psi^{*} \eta \equiv 0$, and hence
$$i \psi^{*} F=\psi^{*}\left[\frac{s}{4}\left(\frac{\omega+\hat{\omega}}{2}\right)+\frac{s^{\star}}{4}\left(\frac{\omega-\hat{\omega}}{2}\right)\right],$$
Now $\omega \in \Lambda^{+}$and $\hat{\omega} \in \Lambda^{-}$correspond to almost-complex structures $J$ and $\hat{J}$ via index-lowering with $g$. Since $\Sigma$ is $J$-holomorphic, $\psi^{*} \omega$ is exactly the area form of the (possibly degenerate) metric $\psi^{*} g$, and we therefore have
$$-\psi^{*} \omega \leq \psi^{*} \hat{\omega} \leq \psi^{*} \omega$$
by applying Wirtinger's inequality [11, 13] to $\hat{\omega}$. We may therefore write
$$\psi^{*} \hat{\omega}=(1-2 t) \psi^{*} \omega$$
for some $t \in[0,1]$ at any point where $s^{\star} \neq s$, and it therefore follows that
$$i \psi^{*} F=\frac{(1-t) s+t s^{\star}}{4} \psi^{*} \omega, \quad \exists t \in[0,1],$$
at each point of $\Sigma$. The inequality $s \leq s^{\star}$ therefore implies that
$$\frac{s}{4} \psi^{*} \omega \leq i \psi^{*} F \leq \psi^{*} \frac{s^{\star}}{4} \omega$$
everywhere, exactly as claimed. \(\square\)

Corollary 3.2 Let $(M, g, \omega)$ be a compact 4-dimensional almost-Kähler Einstein manifold, and suppose that $\psi: \Sigma \rightarrow M$ is a J-holomorphic curve. Let $[\Sigma]$ denote, interchangeably, either the image of the fundamental cycle of $\Sigma$ in $H_{2}(M, \mathbb{Z})$ or its Poincaré dual in $H^{2}(M, \mathbb{Z})$. Then
$$s[\omega] \cdot[\Sigma] \leq 8 \pi c_{1} \cdot[\Sigma] \leq \int_{\Sigma} s^{\star} \omega .$$

Proof. By the Chern-Weil theorem, the closed 2-form $i F$ represents $2 \pi c_{1}=2 \pi c_{1}(L)$ in de Rham cohomology. Now integrate on $\Sigma$, and apply Proposition 3.1. \(\square\)

In particular, this implies the following:
Corollary 3.3 Let $(M, g, \omega)$ be an almost-Kähler Einstein 4-manifold with $s^{\star} \leq 0$, and let $\psi: \Sigma \rightarrow M$ be any $J$-holomorphic curve. Then
$$c_{1} \cdot[\Sigma] \leq 0 .$$

We will now invoke Taubes' existence results for pseudo-holomorphic curves [30]. One of Taubes' most striking and fundamental technical results may be stated as follows:

Theorem 3.4 (Taubes) Let $(M, g, \omega)$ be an almost-Kähler 4-manifold, and let $F_{0}$ denote the curvature of its anti-canonical line bundle $L$. Let $\ell \rightarrow M$ be some Hermitian complex line bundle, and consider the spin ${ }^{c}$-structure with determinant line bundle $L \otimes \ell^{2}$ obtained by setting $\tilde{\mathbb{V}}_{+}=\mathbb{V}_{+} \otimes \ell=\mathbb{S}_{+} \otimes L^{1 / 2} \otimes \ell$. If, for this spin ${ }^{c}$ structure, there exists a sequence $\left(\Phi_{j}, \theta_{j}\right)$ of solutions of the perturbed Seiberg-Witten equations
$$\begin{aligned}
\not D^{\theta_{j}} \Phi & =0 \\
i F_{\theta_{j}}^{+}+\sigma(\Phi) & =i F_{0}^{+}+t_{j} \omega
\end{aligned}$$
for some sequence of real numbers $t_{j} \rightarrow \infty$, then there is a $J$-holomorphic curve $\psi: \Sigma \rightarrow M$ in $(M, g, \omega)$ such that $[\Sigma]=c_{1}(\ell)$.

In fact, Taubes shows that a subsequence of $\left\{i\left(F_{\theta_{j}}-F_{0}\right) / 4 \pi\right\}$ converges as a current to the desired pseudo-holomorphic curve.

The consequences of this result are particularly clean and dramatic when $b_{+}(M)>1$. In this setting, each spin ${ }^{c}$ structure has a well-defined number attached to it, called its Seiberg-Witten invariant [30], which roughly speaking counts the number of solutions, modulo gauge equivalence, of the perturbed Seiberg-Witten equations
$$\begin{aligned}
\not D^{\tilde{\theta}} \Phi & =0 \\
i F_{\tilde{\theta}}^{+}+\sigma(\Phi) & =\varphi
\end{aligned}$$
associated with a generic self-dual 2-form $\varphi$. When this invariant is nonzero, the Chern class of the given spin ${ }^{c}$ structure is called a Seiberg-Witten basic class 31, and the perturbed Seiberg-Witten equations are certainly guaranteed to have solutions for the choices of $\varphi$ used by Taubes. Thus:

Corollary 3.5 Let $(M, g, \omega)$ be a compact almost-Kähler 4-manifold with $b_{+} \geq 2$, and suppose that $c_{1}+2 a \in H^{2}(M, \mathbb{Z})$ /torsion is a Seiberg-Witten basic class of the oriented 4-manifold $M$. Then there is a $J$-holomorphic curve $\psi: \Sigma \rightarrow M$ in $(M, g, \omega)$ such that $[\Sigma]=a$.

When $b_{+}(M)=1$, the situation is a bit more subtle. If one considers only those perturbations $\varphi$ for which the harmonic part $\varphi_{H}$ has huge norm, the same recipe used to define the Seiberg-Witten invariant in the previous case works perfectly well in most respects; however, the value of the answer now depends not only on the oriented smooth 4-manifold $M$, but also on the nappe (connected component) $\mathcal{C}^{+}$of the cone
$$\mathcal{C}=\left\{h \in H^{2}(M, \mathbb{R}) \mid h \cdot h>0\right\}$$
which contains the de Rham class $\left[\varphi_{H}\right]$. To apply Taubes' work when $b_{+}(M)=1$, one thus consider the so-called perturbed Seiberg-Witten invariants [16, 19, 20] of $\left(M, \mathcal{C}^{+}\right)$, where $\mathcal{C}^{+}$is the nappe of $\mathcal{C}$ containing the symplectic class $[\omega] \in H^{2}(M, \mathbb{R})$.

Now let $(M, \omega)$ be any compact symplectic 4-manifold, and consider the standard spin ${ }^{c}$ structure on $M$ induced by $\omega$. Another result of Taubes [28] tells us that the Seiberg-Witten invariant of $M$ (respectively, the perturbed Seiberg-Witten invariant of $\left.\left(M, \mathcal{C}^{+}\right)\right)$is non-zero for this spin ${ }^{c}$ structure, provided that $b_{+}(M) \geq 2$ (respectively, provided that $b_{+}(M)=1$ ). Now if $M$ can be expressed as a connected sum $M \approx N \# \overline{\mathbb{C P}}_{2}$, there are self-diffeomorphism $\Psi: M \rightarrow M$ which, away from the neck connecting the two summands, is given by the identity on $N$, and by complex conjugation on $\overline{\mathbb{C P}}_{2}$. If $b_{+}(M)=b_{+}(N)=1$, such a diffeomorphism moreover sends $\mathcal{C}^{+}$to itself, since the positive sector of $H^{2}(M)$ actually arises from $H^{2}(N)$. Moving the standard spin ${ }^{c}$ structure via $\Psi$ thus gives rise to a new spin ${ }^{c}$ structure for which the relevant version of the Seiberg-Witten invariant is non-zero, and we thus obtain the following [19, 20, 30]:

Corollary 3.6 Let $(M, g, \omega)$ be a compact almost-Kähler 4-manifold. If $M$ is diffeomorphic to a connected sum $N \# \overline{\mathbb{C P}}_{2}$, then there is a $J$-holomorphic curve $\psi: \Sigma \rightarrow M$ in $(M, g, \omega)$ such that $c_{1} \cdot[\Sigma]=+1$.

For a generic choice of $\omega$-compatible metric $g$, the $J$-holomorphic curve $\Sigma$ of Corollary 3.6 will be an embedded symplectic 2-sphere of self-intersection -1; this then allows one to symplectically blow down $M$ to obtain a symplectic structure on $N$. A symplectic 4-manifold $M$ is said to be minimal if it cannot be obtained from another symplectic manifold $N$ by blowing up [22]. As we have just seen, $(M, \omega)$ is minimal iff it contains no symplectic 2-sphere of self-intersection -1, and this occurs iff $M$ cannot be differentiably decomposed as a connected sum $N \# \overline{\mathbb{C P}}_{2}$. Any compact symplectic 4-manifold can be obtained from a minimal one by blowing up a finite number of times.

For our purposes, it is important to emphasize that Corollaries 3.5 and 3.6 produce pseudo-holomorphic curves for a fixed almost-Kähler metric $g$, and not just for its generic perturbations; the price that must be paid for this is simply that the images $\psi(\Sigma)$ of these curves may in principle be rather singular. With this in mind, we now easily obtain the following result:

Theorem 3.7 Let $\left(M^{4}, g, \omega\right)$ be an almost-Kähler Einstein manifold with $s^{\star} \leq 0$. Then $(M, \omega)$ is symplectically minimal.

Proof. If $M$ were non-minimal, Corollary 3.6 would predict the existence of a $J$-holomorphic curve $\psi: \Sigma \rightarrow M$ with $c_{1} \cdot[\Sigma]=+1$. But since we have assumed that $(M, g, \omega)$ is almost-Kähler and Einstein, with $s^{\star} \leq 0$, Corollary 3.3 says we must have $c_{1} \cdot[\Sigma] \leq 0$, so this is a contradiction. \(\square\)

A symplectic 4-manifold is said to be of general type [15, 18] if it has a minimal model with $c_{1}^{2}>0$ and $c_{1} \cdot[\omega]<0$. This definition is chosen so that it coincides with Kodaira's notion of general type when $M$ admits a complex structure. Note that the the condition that $c_{1} \cdot[\omega]<0$ is actually redundant [29] when $b_{+}(M) \geq 2$.

Theorem A If $(M, g, \omega)$ is a 4-dimensional almost-Kähler Einstein manifold with $s^{\star}<0$, then $(M, \omega)$ is a minimal symplectic manifold of general type, and $M$ cannot be differentiably decomposed as a connect sum $N \# \overline{\mathbb{C P}}_{2}$.

Proof. Since $s^{\star}<0$, Corollary 2.3 tells us that $c_{1} \cdot[\omega]<0$. Because $g$ is assumed to be Einstein, and since the assumption that $s^{\star}<0$ implies that $g$ has $s<0$, we also know that $c_{1}^{2}=(2 \chi+3 \tau)(M)>0$ by the Hitchin-Thorpe inequality. The claim thus follows from Theorem 3.7. \(\square\)

We now consider the case when $s^{\star}$ is allowed to have a positive maximum.

Theorem B Suppose that $(M, g, \omega)$ is an almost-Kähler Einstein 4-manifold with $s<0$ and with
$$s^{\star} \leq-\frac{s}{m}$$
for some constant $m>1$. Suppose, moreover, that $b_{+}(M)>1$. Let $\left(X, \omega^{\prime}\right)$ be a symplectic minimal model for $M$, and let $k$ denote the number of blow-ups used to obtain $M$ from $X$. Then
$$k<\frac{1}{m+2} c_{1}^{2}(X) .$$

Proof. By assumption, $M$ contains $k$ disjoint symplectic 2-spheres of selfintersection -1 ; we we will use $E_{1}, \ldots, E_{k}$ to denote, interchangeably, either the homology classes $\in H_{2}(M, \mathbb{Z})$ of these 2-spheres, or their Poincaré duals $\in H^{2}(M, \mathbb{Z})$. Let $D \in H^{2}(M, \mathbb{Z})$ denote the pull-back of $-c_{1}\left(X, \omega^{\prime}\right)$ via the blowing-down map $M \rightarrow X$. Then $\pm D \pm E_{1} \pm \cdots \pm E_{k}$ are all Seiberg-Witten basic classes of $M$, for all possible choices of the various ± signs in this expression. Since the first Chern class of $(M, \omega)$ is given by $c_{1}=$ $-D-E_{1}-\cdots-E_{k}$, it thus follows that $c_{1}+2 D, c_{1}+2 E_{1}, \ldots, c_{1}+2 E_{k}$ are all basic classes. Corollary 3.5 therefore tells us that $D, E_{1}, \ldots, E_{k}$ are all represented by $J$-holomorphic curves in $(M, g, \omega)$. Since our assumptions include the point-wise estimate $s \leq-m s^{\star}$, Proposition 3.1 thus tells us that
$$\begin{aligned}
c_{1}^{2}(X) & =D \cdot D \\
& =-c_{1} \cdot D \\
& \leq-\frac{s}{8 \pi}[\omega] \cdot D \\
& =-\frac{s}{8 \pi}[\omega] \cdot\left(-c_{1}-\sum_{j=1}^{k} E_{j}\right) \\
& =\frac{s}{8 \pi} \int_{M} \frac{s+s^{\star}}{8 \pi} d \mu+\frac{1}{8 \pi} \sum_{j=1}^{k} \int_{E_{j}} s \omega \\
& \leq \frac{1}{64 \pi^{2}} \int_{M} s^{2} d \mu+\frac{1}{64 \pi^{2}} \int_{M} s s^{\star} d \mu-\frac{m}{8 \pi} \sum_{j=1}^{k} \int_{E_{j}} s^{\star} \omega \\
& \leq \frac{1}{64 \pi^{2}} \int_{M} s^{2} d \mu+\frac{1}{64 \pi^{2}} \int_{M} s s^{\star} d \mu-m \sum_{j=1}^{k} c_{1} \cdot E_{j} \\
& \leq \frac{1}{64 \pi^{2}} \int_{M} s^{2} d \mu+\frac{1}{64 \pi^{2}} \int_{M} s s^{\star} d \mu-m k
\end{aligned}$$

However, Proposition 2.1 tells us that
$$\begin{aligned}
c_{1}^{2}(M) & =\frac{1}{4 \pi^{2}} \int_{M}\left(\left|F^{+}\right|^{2}-\left|F^{-}\right|^{2}\right) d \mu \\
& =\frac{1}{4 \pi^{2}} \int_{M}\left(|\eta|^{2}+\left[\frac{s+s^{\star}}{8}\right]^{2}|\omega|^{2}-\left[\frac{s-s^{\star}}{8}\right]^{2}|\hat{\omega}|^{2}\right) d \mu \\
& =\frac{1}{4 \pi^{2}} \int_{M}\left(|\eta|^{2}+\frac{s s^{\star}}{8}\right) d \mu \\
& \geq \frac{1}{32 \pi^{2}} \int_{M} s s^{\star} d \mu
\end{aligned}$$
while the Gauss-Bonnet and signature theorems tell us that
$$\begin{aligned}
c_{1}^{2}(M) & =(2 \chi+3 \tau)(M) \\
& =\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+2\left|W^{+}\right|^{2}-\frac{|\stackrel{\circ}{r}|^{2}}{2}\right) d \mu \\
& =\frac{1}{4 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+2\left|W^{+}\right|^{2}\right) d \mu \\
& >\frac{1}{96 \pi^{2}} \int_{M} s^{2} d \mu
\end{aligned}$$
where in the last step we have used Corollary 2.5, which asserts that our almost-Kähler Einstein manifold $s<0$ cannot have $W^{+} \equiv 0$. Hence
$$\begin{aligned}
c_{1}^{2}(X) & \leq \frac{1}{64 \pi^{2}} \int_{M} s^{2} d \mu+\frac{1}{64 \pi^{2}} \int_{M} s s^{\star} d \mu-m k \\
& <\frac{3}{2} c_{1}^{2}(M)+\frac{1}{2} c_{1}^{2}(M)-m k \\
& =2 c_{1}^{2}(M)-m k \\
& =2 c_{1}^{2}(X)-2 k-m k,
\end{aligned}$$
and it follows that
$$k<\frac{c_{1}^{2}(X)}{m+2},$$
exactly as claimed. \(\square\)

\section*{A Appendix: Spinor Calculus}

If ( $M, g$ ) is an oriented Riemannian 4 -manifold, and if $U \subset M$ is contractible open subset, then $U$ carries spinor bundles $\mathbb{S}_{ \pm}$such that
$$\mathbb{C} \otimes T U=\mathbb{S}_{+} \otimes \mathbb{S}_{-} .$$
These bundles have structure group $S U(2)$, and carry standard connections induced by the Levi-Civita connection of $(M, g)$. Because the representation theory of $S U(2)$ is so remarkably simple, it is often convenient to derive facts about Riemannian 4-manifolds by exploiting these local spinors, even if $M$ itself is not spin. This is particularly true when, as in the present article, $M$ carries some natural spin ${ }^{c}$ structure, so that one has global bundles $\mathbb{V}_{ \pm} \rightarrow M$ which are formally given by
$$\mathbb{V}_{ \pm}=\mathbb{S}_{ \pm} \otimes L^{1 / 2}$$
for some Hermitian line bundle $L$ with
$$c_{1}(L) \equiv w_{2}(M) \bmod 2 .$$

The spinor calculations in this paper are carried out using a modified version of Penrose's spinor calculus [25, 26]. This notation makes use of abstract indices, which are best understood as simply "addresses" which label the various input "mailboxes" of a spinor or tensor field. Upstairs lower-case Roman indices $a, b, c, \ldots$ refer to the tangent bundle, upper-case unprimedprimed capital Roman indices $A, B, C, \ldots$ refer to the spin bundle $\mathbb{S}_{+}$, and upper-case unprimed-primed capital Roman indices $A^{\prime}, B^{\prime}, C^{\prime}, \ldots$ refer to the spin bundle $\mathbb{S}_{-}$. Downstairs indices refer to the dual of the relevant bundle. Square brackets "[ ]" indicate skew-symmetrization
$$\varphi_{[\underbrace{a b \cdots c}_{n}]}:=\frac{1}{n!} \sum_{\sigma \in S_{n}}(-1)^{\sigma} \varphi_{\sigma(a) \sigma(b) \cdots \sigma(c)},$$
whereas round brackets "( )" indicate symmetrization:
$$\varphi_{(\underbrace{a b \cdots c}_{n})}:=\frac{1}{n!} \sum_{\sigma \in S_{n}} \varphi_{\sigma(a) \sigma(b) \cdots \sigma(c)} .$$
The repetition of an index, once upstairs and once downstairs, indicates contraction. The fundamental isomorphism $\mathbb{C} \otimes T=\mathbb{S}_{+} \otimes \mathbb{S}_{-}$is invoked
by the convention that lower case Roman indices $a, b, c, \ldots$ are to be viewed as equal to the corresponding pairs $A A^{\prime}, B B^{\prime}, C C^{\prime}, \ldots$ For convenience, we allow ourselves to shuffle primed indices through unprimed indices, so that $A^{\prime} A B, A A^{\prime} B$, and $A B A^{\prime}$ are all regarded as the same; however, it should be emphasized that these are a priori different from e.g. $A^{\prime} B A$.

Because the bundles $\mathbb{S}_{ \pm}$have structure group $S U(2)=S p(1)$, they may be viewed as quaternionic line bundles. However, we instead choose to view them as 2-dimensional complex vector bundles equipped with complex antilinear maps
$$\begin{array}{lllll}
\mathbb{S}_{+} & \longrightarrow & \mathbb{S}_{+} & \mathbb{S}_{-} & \longrightarrow \\
\beta^{A} & \mapsto & \bar{\beta}^{A} & \gamma^{A^{\prime}} & \mapsto \\
\bar{\gamma}^{A^{\prime}} & &
\end{array}$$
which satisfy
$$\overline{\bar{\beta}}^{A}=-\beta^{A}, \quad \overline{\bar{\gamma}}^{A^{\prime}}=-\gamma^{A^{\prime}} .$$
and correspond to multiplication by the quaternion $j$. Since $S U(2) \subset$ $S L(2, \mathbb{C})$, the bundles $\Lambda^{2} \mathbb{S}_{ \pm}^{*}$ also admit canonical parallel sections $\varepsilon_{A B}=\varepsilon_{[A B]}$ and $\varepsilon_{A^{\prime} B^{\prime}}=\varepsilon_{\left[A^{\prime} B^{\prime}\right]}$, which are real
$$\varepsilon_{A B}=\bar{\varepsilon}_{A B}, \quad \varepsilon_{A^{\prime} B^{\prime}}=\bar{\varepsilon}_{A^{\prime} B^{\prime}}$$
with respect to the induced real structure, and which are related to the Riemannian metric $g$ by
$$g_{a b}=\varepsilon_{A B} \varepsilon_{A^{\prime} B^{\prime}}$$
There are also inverse sections $\varepsilon^{A B}$ and $\varepsilon^{A^{\prime} B^{\prime}}$ of $\Lambda^{2} \mathbb{S}_{ \pm}$, defined so that
$$\varepsilon_{A}{ }^{B}=\varepsilon_{A C} \varepsilon^{B C}, \quad \varepsilon_{A^{\prime}}{ }^{B^{\prime}}=\varepsilon_{A^{\prime} C^{\prime}} \varepsilon^{B^{\prime} C^{\prime}}$$
are the identity endomorphisms of $\mathbb{S}_{ \pm}$. Spinor indices are raised and lowered according to the convention that
$$\beta_{B}=\beta^{A} \varepsilon_{A B}, \quad \beta^{A}=\varepsilon^{A B} \beta_{B},$$
etc. The norm of the spinor $\beta^{A}$ is defined by
$$|\beta|^{2}=\beta_{A} \bar{\beta}^{A}=-\beta^{A} \bar{\beta}_{A} \geq 0,$$
and the norm of $\gamma^{A^{\prime}}$ is defined analogously.
Any two form $\varphi_{a b}=\varphi_{[a b]}$ can be uniquely expressed as
$$\varphi_{a b}=\varphi_{A B}^{+} \varepsilon_{A^{\prime} B^{\prime}}+\varphi_{A^{\prime} B^{\prime}}^{-} \varepsilon_{A B},$$
where $\varphi_{A B}^{+}=\varphi_{(A B)}^{+}$and $\varphi_{A^{\prime} B^{\prime}}^{-}=\varphi_{\left(A^{\prime} B^{\prime}\right)}^{-}$. With our orientation conventions, the 2-forms
$$\varphi_{a b}^{+}=\varphi_{A B^{\prime}}^{+} \varepsilon_{A^{\prime} B^{\prime}}$$
and
$$\overline{\varphi_{a b}^{-}}=\varphi_{A^{\prime} B^{\prime}}^{-} \varepsilon_{A B}$$
are then respectively the self-dual and anti-self-dual parts of $\varphi$, in accordance with the decomposition
$$\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$$
of the 2-forms into the eigenspaces of Hodge star operator ★. Also notice that the usual convention on the norm of a 2-form simplifies in a rather pleasant way: for a real self-dual 2 form $\psi_{a b}$, one has
$$|\psi|^{2}:=\frac{1}{2} \psi_{a b} \psi^{a b}=\frac{1}{2} \psi_{A B} \varepsilon_{A^{\prime} B^{\prime}} \psi^{A B} \varepsilon^{A^{\prime} B^{\prime}}=\psi_{A B} \psi^{A B},$$
since $\varepsilon_{A^{\prime}}{ }^{A^{\prime}}=2$. Of course, the expression for the norm of an anti-self-dual 2-form simplifies in a similar manner.

In much the same way, the Riemann curvature tensor decomposes as
$$\begin{aligned}
R_{a b c d}= & W_{A B C D}^{+} \varepsilon_{A^{\prime} B^{\prime}} \varepsilon_{C^{\prime} D^{\prime}}+W_{A^{\prime} B^{\prime} C^{\prime} D^{\prime}}^{-} \varepsilon_{A B} \varepsilon_{C D} \\
& -\frac{1}{2} \stackrel{\circ}{r}_{A B C^{\prime} D^{\prime}} \varepsilon_{A^{\prime} B^{\prime}} \varepsilon_{C D}-\frac{1}{2}{\stackrel{r}{r_{A^{\prime} B^{\prime} C D}}}^{\varepsilon_{A B} \varepsilon_{C^{\prime} D^{\prime}}} \\
& +\frac{s}{12}\left(\varepsilon_{A C} \varepsilon_{B D} \varepsilon_{A^{\prime} C^{\prime}} \varepsilon_{B^{\prime} D^{\prime}}-\varepsilon_{A D} \varepsilon_{B C} \varepsilon_{A^{\prime} D^{\prime}} \varepsilon_{B^{\prime} C^{\prime}}\right)
\end{aligned}$$
where $W_{A B C D}^{+}=W_{(A B C D)}^{+}, W_{A^{\prime} B^{\prime} C^{\prime} D^{\prime}}^{-}=W_{\left(A^{\prime} B^{\prime} C^{\prime} D^{\prime}\right)}^{-}$, and $\stackrel{\circ}{r}_{A B A^{\prime} B^{\prime}}^{-}=$ $\stackrel{\circ}{r}_{(A B)\left(A^{\prime} B^{\prime}\right)}$. Here
$$W_{a b c d}^{+}=W_{A B C D}^{+} \varepsilon_{A^{\prime} B^{\prime}} \varepsilon_{C^{\prime} D^{\prime}}$$
is the self-dual Weyl curvature,
$$W_{a b c d}^{-}=W_{A^{\prime} B^{\prime} C^{\prime} D^{\prime}}^{-} \varepsilon_{A B} \varepsilon_{C D}$$
is the anti-self-dual Weyl curvature,
$$s=R^{a b}{ }_{a b}$$
is the scalar curvature, and
$$\stackrel{\circ}{r}_{a b}=\stackrel{\circ}{r}_{A B A^{\prime} B^{\prime}}=R_{a c b}^{c}-\frac{s}{4} g_{a b}$$
is the trace-free part of the Ricci curvature. Note that $W_{a b c d}^{+}$is usually considered [6] as a section of $\Lambda^{+} \otimes \Lambda^{+}$, so that its standard norm is defined by
$$\left|W^{+}\right|^{2}=\left(\frac{1}{2}\right)^{2} W_{a b c d}^{+} W^{+a b c d}=W_{A B C D}^{+} W^{+A B C D},$$
where we have again used the fact that $\varepsilon_{A}{ }^{A}=2$. For the same reason, the usual [6] map $W^{+}: \Lambda^{+} \rightarrow \Lambda^{+}$is explicitly given by
$$\psi_{a b} \mapsto \frac{1}{2} W_{a b}^{+c d} \psi_{c d},$$
and so corresponds to the map
$$\psi_{A B} \mapsto W_{A B}^{+C D} \psi_{C D} .$$
Similarly, the usual [8] expression $W^{+}(\psi, \psi)$ is actually short-hand for
$$\left(\frac{1}{2}\right)^{2} W_{a b c d}^{+} \psi^{a b} \psi^{c d}=W_{A B C D}^{+} \psi^{A B} \psi^{C D} .$$

The bundles $\mathbb{S}_{ \pm}$carry natural connections induced by the Levi-Civita connection of $g$. These satisfy
$$\nabla_{A A^{\prime}} \varepsilon_{B C}=0, \quad \nabla_{A A^{\prime}} \varepsilon_{B^{\prime} C^{\prime}}=0,$$
so the raising and lowering of spinor indices commutes with covariant differentiation. The curvatures of the bundles are described by the so-called Ricci identities:
$$\begin{aligned}
\square_{A B} \beta_{C} & =W_{A B C}^{+}{ }^{D} \beta_{D}+\frac{s}{24}\left(\varepsilon_{A C} \beta_{B}+\varepsilon_{B C} \beta_{A}\right) \\
\square_{A^{\prime} B^{\prime}} \beta_{C} & =-\frac{1}{2} \grave{r}_{A^{\prime} B^{\prime} C}^{D} \beta_{D} \\
\square_{A B} \gamma_{C^{\prime}} & =-\frac{1}{2} \grave{r}_{A B C^{\prime}}^{\prime} \gamma_{D^{\prime}} \\
\square_{A^{\prime} B^{\prime}} \gamma_{C^{\prime}} & =W_{A^{\prime} B^{\prime} C^{\prime}}^{-}{D^{\prime}}^{\prime} \gamma_{D^{\prime}}+\frac{s}{24}\left(\varepsilon_{A^{\prime} C^{\prime}} \gamma_{B^{\prime}}+\varepsilon_{B^{\prime} C^{\prime}} \gamma_{A^{\prime}}\right)
\end{aligned}$$
where
$$\begin{aligned}
\square_{A B} & =\nabla_{E^{\prime}(A} \nabla_{B)}^{E^{\prime}}, \\
\square_{A^{\prime} B^{\prime}} & =\nabla_{E\left(A^{\prime}\right.} \nabla_{\left.B^{\prime}\right)}^{E},
\end{aligned}$$
so that
$$2 \nabla_{[a} \nabla_{b]}=\varepsilon_{A^{\prime} B^{\prime}} \square_{A B}+\varepsilon_{A B} \square_{A^{\prime} B^{\prime}} .$$

\section*{References}
\begin{itemize}
\item[] [1] V. Apostolov, J. Armstrong, and T. Drăghici, Local models and integrability of certain almost Kähler 4-manifolds, Math. Ann., 323 (2002), pp. 633-666.
\item[] [2] J. Armstrong, On four-dimensional almost Kähler manifolds, Quart. J. Math. Oxford Ser. (2), 48 (1997), pp. 405-415.
\item[] [3] -, An ansatz for almost-Kähler, Einstein 4-manifolds, J. Reine Angew. Math., 542 (2002), pp. 53-84.
\item[] [4] T. Aubin, Equations du type Monge-Ampère sur les variétés Kählériennes compactes, C. R. Acad. Sci. Paris, 283A (1976), pp. 119-121.
\item[] [5] W. Barth, C. Peters, and A. V. de Ven, Compact Complex Surfaces, Springer-Verlag, 1984.
\item[] [6] A. Besse, Einstein Manifolds, Springer-Verlag, 1987.
\item[] [7] D. E. Blair, The "total scalar curvature" as a symplectic invariant and related results, in Proceedings of the 3rd Congress of Geometry (Thessaloniki, 1991), Thessaloniki, 1992, Aristotle Univ. Thessaloniki, pp. 79-83.
\item[] [8] J.-P. Bourguignon, Les variétés de dimension 4 à signature non nulle dont la courbure est harmonique sont d'Einstein, Invent. Math., 63 (1981), pp. 263-286.
\item[] [9] T. C. Drăghici, On some 4-dimensional almost Kähler manifolds, Kodai Math. J., 18 (1995), pp. 156-168.
\item[] [10] S. I. Goldberg, Integrability of almost Kaehler manifolds, Proc. Amer. Math. Soc., 21 (1969), pp. 96-100.
\item[] [11] P. Griffiths and J. Harris, Principles of Algebraic Geometry, Wiley-Interscience [John Wiley \& Sons], New York, 1978. Pure and Applied Mathematics.
\item[] [12] M. Gromov, Pseudoholomorphic curves in symplectic manifolds, Invent. Math., 82 (1985), pp. 307-347.
\end{itemize}
\begin{itemize}
\item[] [13] R. Harvey and H. B. Lawson, Jr., Calibrated geometries, Acta Math., 148 (1982), pp. 47-157.
\item[] [14] N. J. Hitchin, On compact four-dimensional Einstein manifolds, J. Differential Geom., 9 (1974), pp. 435-442.
\item[] [15] C. LeBrun, Four-manifolds without Einstein metrics, Math. Res. Lett., 3 (1996), pp. 133-147.
\item[] [16] -, Yamabe constants and the perturbed Seiberg-Witten equations, Comm. An. Geom., 5 (1997), pp. 535-553.
\item[] [17] _, Ricci curvature, minimal volumes, and Seiberg-Witten theory, Inv. Math., 145 (2001), pp. 279-316.
\item[] [18] T.-J. Li, Symplectic Parshin-Arakelov inequality, Internat. Math. Res. Notices, (2000), pp. 941-954.
\item[] [19] T.-J. Li and A.-K. Liu, Symplectic structure on ruled surfaces and a generalized adjunction formula, Math. Res. Lett., 2 (1995), pp. 453-471.
\item[] [20] -, The equivalence between SW and Gr in the case where $b^{+}=1$, Internat. Math. Res. Notices, (1999), pp. 335-345.
\item[] [21] D. McDuff, The structure of rational and ruled symplectic 4-manifolds, J. Amer. Math. Soc., 3 (1990), pp. 679-712.
\item[] [22] -, Blow ups and symplectic embeddings in dimension 4, Topology, 30 (1991), pp. 409-421.
\item[] [23] D. McDuff and D. Salamon, Introduction to Symplectic Topology, Oxford University Press, New York, 1995.
\item[] [24] T. Oguro and K. Sekigawa, On some four-dimensional almost Kähler Einstein manifolds, Kodai Math. J., 24 (2001), pp. 226-258.
\item[] [25] R. Penrose and W. Rindler, Spinors and space-time. Vol. 1, Cambridge University Press, Cambridge, 1984. Two-spinor calculus and relativistic fields.
\item[] [26] -, Spinors and space-time. Vol. 2, Cambridge University Press, Cambridge, 1986. Spinor and twistor methods in space-time geometry.
\end{itemize}
[27] K. Sekigawa, On some compact Einstein almost Kähler manifolds, J. Math. Soc. Japan, 39 (1987), pp. 677-684.
[28] C. H. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett., 1 (1994), pp. 809-822.
[29] -, More constraints on symplectic forms from Seiberg-Witten invariants, Math. Res. Lett., 2 (1995), pp. 9-14.
[30] -, The Seiberg-Witten and Gromov invariants, Math. Res. Lett., 2 (1995), pp. 221-238.
[31] E. Witten, Monopoles and four-manifolds, Math. Res. Lett., 1 (1994), pp. 809-822.
[32] S. T. Yau, Calabi's conjecture and some new results in algebraic geometry, Proc. Nat. Acad. USA, 74 (1977), pp. 1789-1799.
