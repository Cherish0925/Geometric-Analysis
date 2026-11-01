---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Monge–Ampère equation for non-integrable almost complex structures]

---
source_file: The_Monge_Ampère_equation_for_non-integrable_almost_complex_structures_dcae0e3d6eb2.pdf
converter: mathpix
format: mmd
---

\title{
THE MONGE-AMPÈRE EQUATION FOR NON-INTEGRABLE ALMOST COMPLEX STRUCTURES
}

\author{
JIANCHUN CHU, VALENTINO TOSATTI, AND BEN WEINKOVE
}

\begin{abstract}
We show existence and uniqueness of solutions to the Monge-Ampère equation on compact almost complex manifolds with non-integrable almost complex structure.
\end{abstract}

\section*{1. Introduction}

Yau's Theorem for compact Kähler manifolds [56] states that one can prescribe the volume form of a Kähler metric within a given Kähler class. This result, proved forty years ago, occupies a central place in the theory of Kähler manifolds, with wide-ranging applications in geometry and mathematical physics.

More precisely, Yau's Theorem is as follows. Let $\left(M^{2 n}, \omega, J\right)$ be a compact Kähler manifold of complex dimension $n$, where $\omega$ denotes the Kähler form and $J$ the complex structure. Then given a smooth volume form $e^{F} \omega^{n}$ on $M$ there exists a unique smooth function $\varphi$ satisfying
$$\begin{aligned}
(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}= & e^{F} \omega^{n}, \\
\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0, & \sup _{M} \varphi=0 .
\end{aligned}$$
as long as $F$ satisfies the necessary normalization condition that $\int_{M} e^{F} \omega^{n}=$ $\int_{M} \omega^{n}$. The equation (1.1) is known as the complex Monge-Ampère equation for Kähler manifolds.

There has been great interest in extending Yau's Theorem to non-Kähler settings. Recall that a Kähler metric is a positive definite real $(1,1)$ form $\omega$, namely a Hermitian metric, which satisfies
$$d \omega=0 .$$
One extension of Yau's Theorem, initiated by Cherrier [8] in the 1980s, is to remove this closedness condition. This was carried out in full generality in [46] where it was shown that (1.1) has a unique solution for $\omega$ Hermitian, up to adding a (unique) constant to $F$ (see also [45, 24], as well as [4, 9, 14, 29, [30, 32, 35, 40, 49, 57, 58] for later developments). A different recent extension on complex manifolds [41], confirming a conjecture of Gauduchon [21], is that one can prescribe the volume form of a Gauduchon metric (satisfying $\partial \bar{\partial}\left(\omega^{n-1}\right)=0$ ). In this case, (1.1) is replaced by a Monge-Ampère type equation for $(n-1)$-plurisubharmonic functions [26, 17, 18, 38, 50, 51].

Within this circle of ideas remain some open conjectures, such as a version of Yau's Theorem for balanced metrics (satisfying $d\left(\omega^{n-1}\right)=0$ ) [17, 50, [51]. This is related to the some questions about the Strominger system of mathematical physics, see e.g. [19, 31, 34] and the references therein.

A different type of extension of Yau's Theorem is to the case when $J$ is a non-integrable almost complex structure, and this is subject of the current paper. Around twenty years ago, Gromov posed the following problem to P. Delanöe [12]: let $\left(M^{2 n}, \omega\right)$ be a compact symplectic manifold, $J$ an almost complex structure compatible with $\omega$ and $F$ a smooth function on $M$ with $\int_{M} e^{F} \omega^{n}=\int_{M} \omega^{n}$. Can one find a smooth function $\varphi$ on $M$ such that $\omega+d(J d \varphi)$ is a symplectic form taming $J$ and satisfying
$$(\omega+d(J d \varphi))^{n}=e^{F} \omega^{n} ?$$
However, Delanöe [12] showed that when $n=2$ the answer to this question is negative, and this was later extended to all dimensions by Wang-Zhu [53]. The key ingredient of their results is the construction of a smooth function $\varphi_{0}$ such that $\omega+d\left(J d \varphi_{0}\right)$ is on the boundary of the set of taming symplectic forms (so its $(1,1)$ part is semipositive definite but not strictly positive), and yet $\left(\omega+d\left(J d \varphi_{0}\right)\right)^{n}>0$. This is possible because in this case the $(2,0)+(0,2)$ part of $d\left(J d \varphi_{0}\right)$ contributes a strictly positive amount.

This indicates that the problem with Gromov's suggestion is that the 2-form $d(J d \varphi)$ is in general not of type $(1,1)$ with respect to $J$, due to the fact that $J$ may not be integrable (in fact, $d(J d f)$ is of type $(1,1)$ for all functions $f$ if and only if $J$ is integrable). Its $(1,1)$ part (up to an unimportant factor of 2) will be denoted by
$$\sqrt{-1} \partial \bar{\partial} \varphi=\frac{1}{2}(d(J d \varphi))^{(1,1)},$$
which agrees with the standard notation when $J$ is integrable (see also section 2 for more explanations). This quantity was apparently first explicitly considered in [25].

We show that an analogue of Gromov's problem does hold after replacing $d(J d \varphi)$ with $\sqrt{-1} \partial \bar{\partial} \varphi$. In fact we do not even require the manifold to be symplectic. We obtain the following result for almost complex manifolds equipped with an almost Hermitian metric $\omega$.

Our main theorem is the following:
Theorem 1.1. Let $(M, \omega, J)$ be a compact almost Hermitian manifold of real dimension $2 n$. Given a smooth function $F$ there exists a unique pair $(\varphi, b)$ where $\varphi \in C^{\infty}(M)$ and $b \in \mathbb{R}$, solving
$$\begin{aligned}
(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}= & e^{F+b} \omega^{n}, \\
\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0, & \sup _{M} \varphi=0 .
\end{aligned}$$

Namely, this says that the main result of [46] holds even when $J$ is a non-integrable almost complex structure. The equation (1.3) was first considered by Harvey-Lawson [27] and Pliś [36] in the setting of the Dirichlet problem for $J$-pseudoconvex domains (see Remark 5 below). We note here that there has been a renewed interest recently in the theory of $J$ -plurisubharmonic functions on almost complex manifolds, i.e. functions $\varphi$ for which $\sqrt{-1} \partial \bar{\partial} \varphi>0$ (see e.g. [11, 25, 27, 28, 33, 36, 37]), and our main theorem fits well into this picture.

The key ingredients for proving Theorem 1.1 are the following new a priori estimates:

Theorem 1.2. Let $(M, \omega, J)$ be a compact almost Hermitian manifold of real dimension $2 n$. Given smooth functions $F$ and $\varphi$ satisfying
$$\begin{aligned}
(\omega+\sqrt{-1} \partial \bar{\partial} \varphi)^{n}= & e^{F} \omega^{n}, \\
\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0, & \sup _{M} \varphi=0,
\end{aligned}$$
then there are uniform $C^{\infty}$ a priori estimates on $\varphi$ depending only on $(M, \omega, J)$ and bounds for $F$.

We make now a few remarks about our results:
1. We can also interpret the Monge-Ampère equation (1.3) in terms of Ricci curvature forms. More precisely, we can associate to an almost Hermitian metric $\omega$ a canonical connection (see e.g. [52]), whose curvature form can be expressed as a skew-Hermitian matrix of 2-forms $\left\{\Omega_{j}^{i}\right\}(1 \leqslant i, j \leqslant n)$ in any local unitary frame, and defining
$$\operatorname{Ric}(\omega):=\sqrt{-1} \sum_{i=1}^{n} \Omega_{i}^{i},$$
we obtain a globally defined closed real 2-form, which is cohomologous to the first Chern class $2 \pi c_{1}(M, J)$ in $H^{2}(M, \mathbb{R})$. If $\varphi$ is a smooth function with $\tilde{\omega}:=\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0$ then (1.3) holds for some constant $b$ if and only if
$$\operatorname{Ric}(\tilde{\omega})=\operatorname{Ric}(\omega)-\frac{1}{2} d(J d F),$$
as follows easily from [52, (3.16)]. Note however that in general there are representatives of the first Chern class $2 \pi c_{1}(M, J)$ in $H^{2}(M, \mathbb{R})$ which cannot be written in the form $\operatorname{Ric}(\omega)-\frac{1}{2} d(J d F)$ for any $\omega$ and $F$, even when $J$ is integrable (cf. [45, Corollary 2]). Note also that in general $\operatorname{Ric}(\omega)$ is different from the Riemannian Ricci curvature of the Levi-Civita connection of the Riemannian metric induced by $\omega$. For example, when $(M, J)$ is the Kodaira-Thurston 4-manifold with a certain explicit almost complex structure, then one can construct an explicit almost Hermitian metric $\omega$ with $\operatorname{Ric}(\omega)=$ 0 (see e.g. [48, Theorem 4.1]), and yet $M$ does not admit any Ricci-flat Riemannian metrics. Indeed, four-dimensional Einstein manifolds satisfy
$\chi(M) \geqslant 0$ with equality only when the metric is flat [2, 6.32]. The Kodaira-Thurston manifold is a $T^{2}$-bundle over $T^{2}$ and therefore has $\chi(M)=0$, so if $M$ admitted an Einstein metric, $M$ would be finitely covered by a torus, which is not the case.
2. Suppose now that $\left(M^{2 n}, \omega, J\right)$ is a compact symplectic manifold with $J$ an almost complex structure tamed by $\omega$. In this case $\omega^{(1,1)}$ is an almost Hermitian metric. Given a smooth function $F$ we obtain a pair $(\varphi, b)$ solving
$$\begin{gathered}
\left(\omega^{(1,1)}+\sqrt{-1} \partial \bar{\partial} \varphi\right)^{n}=e^{F+b} \omega^{n}, \\
\omega^{(1,1)}+\sqrt{-1} \partial \bar{\partial} \varphi>0, \quad \sup _{M} \varphi=0 .
\end{gathered}$$
If we define $\tilde{\omega}=\omega+\frac{1}{2} d(J d \varphi)$, then a simple calculation (cf. [12, Proposition 5]) shows that $\tilde{\omega}$ is a symplectic form taming $J$ and
$$\tilde{\omega}^{n} \geqslant\left(\omega^{(1,1)}+\sqrt{-1} \partial \bar{\partial} \varphi\right)^{n}=e^{F+b} \omega^{n} .$$
3. A different extension of Yau's Theorem to the symplectic setting was proposed by Donaldson [15]. He considered a symplectic 4-manifold $(M, \omega, J)$ with $J$ a tamed almost complex structure, and conjectured that, given a smooth function $F$, and given a symplectic form $\tilde{\omega}$ cohomologous to $\omega$, compatible with $J$ and solving
$$\tilde{\omega}^{2}=e^{F} \omega^{2},$$
then $\tilde{\omega}$ should have uniform $C^{\infty}$ a priori estimates. Donaldson showed that this conjecture and various extensions of it would have consequences for symplectic topology. This problem is fundamentally different from our setup, since here the difference $\tilde{\omega}-\omega$ is not given by a simple operator applied to a function $\varphi$. Donaldson's conjecture remains open in general, but it is known to hold in some special cases [55, 52, 47, 48, 16, 6].
4. One can also consider the parabolic Monge-Ampère equation
$$\frac{\partial \varphi_{t}}{\partial t}=\log \frac{\left(\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}}{\omega^{n}}-F, \quad \varphi_{0}=0,$$
where we require that $\omega+\sqrt{-1} \partial \bar{\partial} \varphi_{t}>0$. Analogously to the result proved by Cao [7] in the Kähler case and Gill [23] in the Hermitian case, we expect that the techniques developed in this paper can be used to show that a smooth solution $\varphi_{t}$ exists for all $t \geqslant 0$, and after suitable normalization converges smoothly to the solution of (1.3).

Similarly, we can consider the equation
$$\frac{\partial \varphi_{t}}{\partial t}=\log \frac{\left(\omega-t \operatorname{Ric}(\omega)^{(1,1)}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}}{\omega^{n}}, \quad \varphi_{0}=0,$$
where now we require that $\omega-t \operatorname{Ric}(\omega)^{(1,1)}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}>0$. This is in fact equivalent to the evolution equation for almost Hermitian forms
$$\frac{\partial \omega_{t}}{\partial t}=-\operatorname{Ric}\left(\omega_{t}\right)^{(1,1)}, \quad \omega_{0}=\omega,$$
which is the Kähler-Ricci flow if $J$ is integrable and $\omega_{0}$ is Kähler, and the Chern-Ricci flow [23, 49] if $J$ is integrable. Again, using the techniques developed in this paper one should be able to characterize the maximal existence time of this flow, exactly as in [42, 49].
5. As in the Hermitian case treated in [50], the constant $b$ that appears in Theorem 1.1 is in general a bit mysterious, and cannot be obtained from $\omega$ and $F$ via a simple formula (unless $J$ is integrable and $\partial \bar{\partial} \omega=0=\partial \bar{\partial}\left(\omega^{2}\right)$, in which case $b=\log \frac{\int_{M} \omega^{n}}{\int_{M} e^{F} \omega^{n}}$ ). One should really think of the pair $(\varphi, b)$ as the unique solution of the PDE (1.3), and in general one cannot expect solutions of PDEs to have simple expressions. What we do know nevertheless is that $|b| \leqslant \sup _{M}|F|$, which follows from a simple maximum principle argument.
Outline of the proof. We now discuss the proof of our main results, and relate this to the work of Pliś [36] who, as noted above, investigated this problem on $J$-pseudoconvex domains (Harvey-Lawson [27] obtained weak solutions in the viscosity sense, and in a more general setting). We prove the a priori estimates of Theorem 1.2 in four steps: the zero order estimate for $\varphi$, the first order estimate, the real Hessian bound and then higher order estimates.

For the zero order estimate we adapt an approach of Székelyhidi [40], which in turn uses ideas of Błocki [3, 4]. The idea is to work locally near the infimum of $\varphi$ and use a modification of the Alexandrov-Bakelman-Pucci maximum principle. Székelyhidi's argument holds for a large class of equations, but assuming an integrable complex structure. We show that the extra terms arising from the non-integrability can be controlled. This argument is contained in Section 3.

The next step is to bound the first derivatives of $\varphi$, and we carry this out in Section 4. We use a maximum principle argument, adapted from Pliś [36]. In particular we compute using a unitary frame $e_{1}, \ldots, e_{n}$, which turns out to be quite convenient for this problem. The difference with [36] is that, as would be expected in the compact case, we need to replace Plis's auxiliary global plurisubharmonic function with a certain choice of "barrier function" involving $\varphi$ itself.

The heart of the paper is Section 5, where we prove a bound on the real Hessian of $\varphi$. Here, the argument diverges substantially from the study of other similar nonlinear PDEs on complex manifolds where the approach is to bound first the complex Hessian of $\varphi$ (see e.g. [5, 24] for instances where a real Hessian bound is obtained for the complex Monge-Ampère equation, with $J$ integrable, after having first obtained a complex Hessian bound). There are difficulties in carrying out the analogous computation for
the complex Hessian here, because of some linear third order terms which, roughly speaking, involve three "barred" or "unbarred" partial derivatives of $\varphi$ and cannot be controlled by the usual squares of third order terms. Instead, we use an important idea of Pliś [36], which is to directly bound the real Hessian of $\varphi$. However, as acknowledged by Pliś in a private communication, there is an error in this argument in [36] (in obtaining the first displayed equation of page 981 from the previous lines). We take a different approach, which corrects [36], and turns out to be substantially more intricate. We apply the maximum principle to a quantity involving the largest eigenvalue $\lambda_{1}$ (cf. [54, 40, 41]) of the real Hessian of $\varphi$. This gives us some good third order terms which are sufficient, after a series of rather technical lemmas, to push the argument through. One source of complication is the need to rule out the case when the largest eigenvector of the real Hessian of $\varphi$ is in a direction where the complex Hessian is very small (see Lemma 5.6 below).

Once we have the real Hessian of $\varphi$ bounded, it is then straightforward to obtain the higher order estimates by applying directly an Evans-Krylov type result from [44] and then some standard bootstrapping arguments. In Section 6 we describe how to obtain the main result Theorem 1.1 using a continuity argument similar to that of [45].

Before we start with the proofs of the main results, we describe first some basic results, and notation, on almost complex manifolds.

Acknowledgments. We thank S. Pliś and G. Székelyhidi for some useful communications, and the referees for pertinent comments. The firstnamed author would like to thank his advisor G. Tian for encouragement and support. The second-named author was partially supported by a Sloan Research Fellowship and NSF grant DMS-1308988, and the third-named author by NSF grant DMS-1406164. This work was carried out while the first-named author was visiting the Department of Mathematics at Northwestern University, supported by the China Scholarship Council (File No. 201506010010), and partly while the second-named author was visiting the Center for Mathematical Sciences and Applications at Harvard University. We would like to thank these institutions for their hospitality and support.

\section*{2. Basic results and notation}

Let $M^{2 n}$ be a compact manifold of real dimension $2 n$ (without boundary) equipped with an almost complex structure $J$, namely an endomorphism of the tangent bundle satisfying $J^{2}=-\mathrm{Id}$. The complexified tangent space $T^{\mathbb{C}} M$ can be decomposed as a direct sum of the two eigenspaces $T^{(1,0)} M$ and $T^{(0,1)} M$ of $J$, corresponding to eigenvalues $\sqrt{-1}$ and $-\sqrt{-1}$ respectively. Similarly, extending $J$ to 1-forms $\alpha$ by $(J \alpha)(X)=-\alpha(J X)$, we obtain a decomposition of $T^{\mathbb{C}} M^{*}$ into the $\sqrt{-1}$ and $-\sqrt{-1}$ eigenspaces, spanned by the $(0,1)$ and $(1,0)$ forms respectively. Thus, with the obvious definitions,
any complex differential form of degree $k$ can be expressed uniquely as a linear combination of ( $p, q$ ) forms with $p+q=k$.

An almost Hermitian metric $g$ on $\left(M^{2 n}, J\right)$ is a Riemannian metric satisfying
$$g(J X, J Y)=g(X, Y), \quad \text { for all } X, Y \in T M .$$
Such metrics always exist in abundance on almost complex manifolds. The metric $g$ defines a positive definite real $(1,1)$ form $\omega$, given by
$$\omega(X, Y)=g(J X, Y) .$$
Conversely, such an $\omega$ defines an almost Hermitian metric $g$ by
$$g(X, Y)=\omega(X, J Y) .$$
As we have already done in the introduction, we abuse terminology by referring to the positive definite $(1,1)$ form $\omega$ as an almost Hermitian metric.

The exterior derivative acting on ( $p, q$ ) forms splits as
$$d=\partial+\bar{\partial}+T+\bar{T},$$
where $T$ changes the bidegree by $(2,-1)$ and $\bar{T}$ by (-1, 2) (these are essentially given by the Nijenhuis tensor) and so we can define
$$\sqrt{-1} \partial \bar{\partial} \varphi:=\sqrt{-1} \partial(\bar{\partial} \varphi) .$$
It is immediate to see that this is indeed a real $(1,1)$ form. A simple calculation shows that
$$\sqrt{-1} \partial \bar{\partial} \varphi=\frac{1}{2}(d(J d \varphi))^{(1,1)} .$$
We also have (see e.g. [27, (2.5)]) that for any two $(1,0)$ vector fields $V, W$,
$$(\partial \bar{\partial} \varphi)(V, \bar{W})=V \bar{W}(\varphi)-[V, \bar{W}]^{(0,1)}(\varphi) .$$

We extend the action of $J$ to $p$-forms by
$$(J \alpha)\left(X_{1}, \ldots, X_{p}\right):=(-1)^{p} \alpha\left(J X_{1}, \ldots, J X_{p}\right),$$
which satisfies $J^{2}=(-1)^{p}$. If $*$ is the Hodge star operator of the Riemannian metric $g$ defined by $\omega$ then the actions of * and $J$ on $p$-forms commute (see e.g. [22, Lemma 1.10.1]). We will say that $\omega$ is Gauduchon if
$$d^{*}\left(J d^{*} \omega\right)=0,$$
where $d^{*}$ is the adjoint of $d$ with respect to $g$. A short calculation shows that (2.2) is equivalent to
$$d\left(J d\left(\omega^{n-1}\right)\right)=0,$$
so we see that when $J$ is integrable this condition reduces to the well-known one.

Theorem 2.1 (Gauduchon [20]). Let $\left(M^{2 n}, \omega, J\right), n \geqslant 2$, be a compact almost Hermitian manifold. Then there exists a smooth function $u$, unique up to addition of a constant, such that the conformal almost Hermitian metric $e^{u} \omega$ is Gauduchon.

For convenience, we will give a brief sketch of the proof of this result in the proof of Theorem 2.2.

Let now $\left(M^{2 n}, \omega, J\right)$ be almost Hermitian, and $f$ a smooth function on $M$. We define the canonical Laplacian of $f$ by
$$\Delta^{C} f=\frac{n \omega^{n-1} \wedge \sqrt{-1} \partial \bar{\partial} f}{\omega^{n}}=\frac{n \omega^{n-1} \wedge d(J d f)}{2 \omega^{n}} .$$
If $\Delta$ denotes the usual Laplace-Beltrami operator of $g$ then we have the relation
$$\Delta f=2 \Delta^{C} f+\tau(d f),$$
where $\tau$ is the "torsion vector field" of $(\omega, J)$ (the dual of its Lee form), see e.g. [43, Lemma 3.2].

For the "openness" part of the continuity method, we will need the following result:
Theorem 2.2 (Gauduchon [20]). Let $\left(M^{2 n}, \omega, J\right), n \geqslant 2$, be a compact almost Hermitian manifold. Fix a nonnegative integer $k$, and $0<\alpha<1$. Given a function $h \in C^{k, \alpha}(M)$, there exists a function $f \in C^{k+2, \alpha}(M)$ solving
$$\Delta^{C} f=h,$$
if and only if
$$\int_{M} h e^{(n-1) u} \omega^{n}=0,$$
where $u$ is as in Theorem 2.1. In this case the solution $f$ is unique up to addition of a constant.

Proof. Although this result is not explicitly stated there, the proof is contained in [20]. For the convenience of the reader we give a brief sketch, referring to [20] for details. Let $\Delta^{*}$ be the formal $L^{2}$ adjoint of $\Delta^{C}$, which is given by
$$\Delta^{*} f=-\frac{1}{2} d^{*}\left(J d^{*}(f \omega)\right),$$
where $f \in C^{\infty}(X, \mathbb{R})$. This is an elliptic second order real differential operator, whose index, like the index of $\Delta^{C}$, is zero. Since the kernel of $\Delta^{C}$ consists just of constants, it follows that $\operatorname{dim}_{\mathbb{R}} \operatorname{ker} \Delta^{*}=1$. The strong maximum principle implies that the only smooth real function in the image of $\Delta^{C}$ which has constant sign is the zero function, and this implies that every function in the kernel of $\Delta^{*}$ has constant sign. Thus we can choose a smooth function $f \not \equiv 0$ with $\Delta^{*} f=0$ and $f \geqslant 0$, and then another application of the strong maximum principle shows that in fact $f>0$. Therefore we can write $f=e^{(n-1) u}$, for some $u \in C^{\infty}(X, \mathbb{R})$, and the fact that $\Delta^{*} f=0$ exactly says that $e^{u} \omega$ is Gauduchon.

The theorem now follows from the Fredholm alternative, since (2.7) means that $h$ is orthogonal to $\operatorname{ker} \Delta^{*}$, which is then equivalent to $h$ being in the image of $\Delta^{C}$. \(\square\)

For later use, we have the following result.
Proposition 2.3. Let $\left(M^{2 n}, \omega, J\right)$ be a compact almost Hermitian manifold, with $\omega$ its associated real $(1,1)$ form. Then there is a constant $C>0$ depending only on $(M, \omega, J)$ such that every smooth function $\varphi$ on $M$ which satisfies
$$\omega+\sqrt{-1} \partial \bar{\partial} \varphi>0, \quad \sup _{M} \varphi=0,$$
also satisfies
$$\int_{M}(-\varphi) \omega^{n} \leqslant C .$$
Proof. Applying Theorem 2.1 we obtain a smooth function $u$ such that the almost Hermitian metric $\omega^{\prime}=e^{u} \omega$ is Gauduchon. Let $\Delta^{\prime C}$ be the canonical Laplacian of $\omega^{\prime}$, which is an elliptic second order differential operator with the kernel consisting of just constants. Standard linear PDE theory (see e.g. [1, Appendix A]) shows that there exists a Green function $G$ for $\Delta^{\prime C}$ which satisfies $G(x, y) \geqslant-C,\|G(x, \cdot)\|_{L^{1}(M, g)} \leqslant C$, for a constant $C>0$, and
$$\varphi(x)=\frac{1}{\int_{M} \omega^{\prime n}} \int_{M} \varphi \omega^{\prime n}-\int_{M} \Delta^{\prime C} \varphi(y) G(x, y) \omega^{\prime n}(y),$$
for all smooth functions $\varphi$ and all $x \in M$. On the other hand we have
$$\int_{M} \Delta^{\prime C} \varphi \omega^{\prime n}=\frac{n}{2} \int_{M} \omega^{\prime n-1} \wedge d(J d \varphi)=\frac{n}{2} \int_{M}\left(d\left(J d \omega^{\prime n-1}\right)\right) \varphi=0$$
since $\omega^{\prime}$ is Gauduchon. For the "integration by parts" step above, we have used the elementary pointwise equality
$$\alpha \wedge(J \beta)=(-1)^{p}(J \alpha) \wedge \beta,$$
which holds for any $(2 n-p)$-form $\alpha$ and $p$-form $\beta$.
Therefore, we are free to add a large uniform constant to $G(x, y)$ to make it nonnegative, while preserving the same Green formula. If $\varphi$ satisfies (2.8) then we have
$$\Delta^{\prime C} \varphi=e^{-u} \Delta^{C} \varphi \geqslant-n e^{-u},$$
and so we immediately deduce that $\int_{M}(-\varphi) \omega^{\prime n} \leqslant C$, from which (2.9) follows. \(\square\)

We end this section with a remark about the use of the maximum principle. Consider a function $f \in C^{2}(M)$. Then
$$\sqrt{-1} \partial \bar{\partial} f\left(x_{0}\right) \leqslant 0 \quad \text { if } f \text { has a local maximum at } x_{0} \text {, }$$
and the reverse inequality holds at a local minimum. Indeed, the only difference from the integrable case is a first order term which vanishes at $x_{0}$.

\section*{3. Zero order estimate}

Here we follow the argument given in [40, Proposition 10] when $J$ is integrable, which is a modification and improvement of an earlier argument by Błocki [3, 4].

Proposition 3.1. Let $\varphi$ solve the Monge-Ampère equation (1.4). Then there exists a constant $C$, depending only on $(M, \omega, J)$ and bounds for $F$ such that
$$|\varphi| \leqslant C .$$
Proof. Since $\sup _{M} \varphi=0$, it suffices to derive a uniform lower bound for $I:=\inf _{M} \varphi$. Let $p \in M$ be a point where this infimum is achieved, and choose local coordinates $\left\{x^{1}, \ldots, x^{2 n}\right\}$ centered at $p$ defined on an open set containing the unit ball $B \subset \mathbb{R}^{2 n}$ in its interior. On $B$ let
$$v(x)=\varphi(x)+\varepsilon \sum_{i=1}^{2 n}\left(x^{i}\right)^{2},$$
where $\varepsilon>0$ will be chosen later. Then
$$\begin{aligned}
& v(0)=I=\inf _{B} v, \\
& \inf _{\partial B} v \geqslant v(0)+\varepsilon .
\end{aligned}$$
We define a set $P$ by
$$P=\{x \in B| | D v(x) \mid<\varepsilon / 2, \text { and } v(y) \geqslant v(x)+D v(x) \cdot(y-x), \forall y \in B\} .$$
Note that $0 \in P$, and that $D^{2} v(x) \geqslant 0$ as well as $|D \varphi(x)| \leqslant \frac{5}{2} \varepsilon$ for all $x \in P$. Now at any $x \in B$ the symmetric bilinear form $H(v)(X, Y):=$ $(\sqrt{-1} \partial \bar{\partial} v)(X, J Y)$ is equal to
$$H(v)=\frac{1}{2}\left(D^{2} v\right)^{J}+E(v),$$
where $\left(D^{2} v\right)^{J}$ is the $J$-invariant part of $D^{2} v(x)$,
$$\left(D^{2} v\right)^{J}(x):=\frac{1}{2}\left(D^{2} v+J^{T} \cdot D^{2} v \cdot J\right)(x),$$
and $E(v)$ is an error matrix which depends linearly on $D v(x)$ (see e.g. [44, p.443]). Therefore, using the fact that $\operatorname{det}(A+B) \geqslant \operatorname{det} A+\operatorname{det} B$ for symmetric nonnegative definite matrices $A, B$, we have for all $x \in P$,
$$\operatorname{det}\left(D^{2} v\right)(x) \leqslant 2^{2 n-1} \operatorname{det}\left(\left(D^{2} v\right)^{J}\right)(x)=2^{4 n-1} \operatorname{det}(H(v)-E(v))(x) .$$
(or, one can argue as in [3]). Moreover,
$$\left(D^{2} \varphi\right)^{J}(x) \geqslant\left(D^{2} v\right)^{J}(x)-C \varepsilon \mathrm{Id} \geqslant-C \varepsilon \mathrm{Id},$$
and using that $|D \varphi(x)| \leqslant 5 \varepsilon / 2$, together with (3.2), we obtain
$$H(\varphi)(x) \geqslant-C \varepsilon \text { Id, }$$
for a uniform constant $C$. Therefore at any $x \in P$ we have
$$\omega+\sqrt{-1} \partial \bar{\partial} \varphi \geqslant \frac{1}{2} \omega,$$
provided $\varepsilon$ is sufficiently small (this fixes the value of $\varepsilon$ ), but the Monge-Ampère equation (1.4) then gives us
$$\omega+\sqrt{-1} \partial \bar{\partial} \varphi \leqslant C \omega .$$
From this, using again (3.1) and $|D v(x)|<\varepsilon / 2$, we conclude that for all $x \in P$ we have
$$0 \leqslant(H(v)-E(v))(x) \leqslant C \mathrm{Id},$$
and (3.3) gives
$$\operatorname{det}\left(D^{2} v\right)(x) \leqslant C .$$
Applying the modified Alexandrov-Bakelman-Pucci maximum principle in [40, Proposition 11] we obtain
$$\varepsilon^{2 n} \leqslant C_{2 n} \int_{P} \operatorname{det}\left(D^{2} v\right),$$
for a constant $C_{2 n}$ which depends only on the dimension of $M$, and so
$$\varepsilon^{2 n} \leqslant C|P|,$$
where $|P|$ denotes the Lebesgue measure of $P$. But for any $x \in P$ we also have
$$v(x) \leqslant v(0)+\frac{\varepsilon}{2}=I+\frac{\varepsilon}{2},$$
and we may assume that $I+\frac{\varepsilon}{2}<0$, so
$$|P| \leqslant \frac{\int_{P}(-v)}{\left|I+\frac{\varepsilon}{2}\right|} \leqslant \frac{C}{\left|I+\frac{\varepsilon}{2}\right|},$$
using Proposition 2.3, and so
$$\left|I+\frac{\varepsilon}{2}\right| \leqslant \frac{C}{\varepsilon^{2 n}},$$
which gives us the desired uniform lower bound for $I$. \(\square\)

We remark that it is also possible to prove the zero order estimate in our case by the method of Moser iteration [56], much like in [46] (where $J$ is integrable), but the calculations are longer. The Moser iteration method was also used by Delanöe [13] for the equation suggested by Gromov (as discussed in the introduction), but in that case the argument is more similar to that of the Kähler case.

\section*{4. First order estimate}

In this section, we prove a first order a priori estimate for $\varphi$, which uses the zero order estimate of Section 3. This part of the argument is similar to [36, Lemma 3.3], except that here we replace Plis's auxiliary plurisubharmonic function by a barrier function involving the solution $\varphi$.

Proposition 4.1. Let $\varphi$ solve the Monge-Ampère equation (1.4). Then there exists a constant $C$, depending only on $(M, g, J)$ and bounds for $F$ such that
$$|\partial \varphi|_{g} \leqslant C .$$
Proof. We will prove this estimate by applying the maximum principle to the quantity $Q=e^{f(\varphi)}|\partial \varphi|_{g}^{2}$, for a function $f=f(\varphi)$ to be determined later. We will show that at the maximum point of $Q,|\partial \varphi|_{g}$ is uniformly bounded from above.

First we discuss coordinates. Let $\left\{e_{1}, \ldots, e_{n}\right\}$ be a local frame for $T^{(1,0)} M$ and let $\left\{\theta^{1}, \ldots, \theta^{n}\right\}$ be a dual coframe. We write $g_{i \bar{j}}=g\left(e_{i}, \bar{e}_{j}\right)$. The $(1,1)$ form $\omega$ is given by
$$\omega=\sqrt{-1} g_{i \bar{j}} \theta^{i} \wedge \bar{\theta}^{j},$$
where here and henceforth, as should be clear from the context, we are summing over repeated indices (on occasion, for clarity, we will include the summation). We define
$$\tilde{\omega}=\omega+\sqrt{-1} \partial \bar{\partial} \varphi,$$
and write $\tilde{g}_{i \bar{j}}$ for the associated metric, defined by $\tilde{\omega}=\sqrt{-1} \tilde{g}_{i \bar{j}} \theta^{i} \wedge \bar{\theta}^{j}$. Equation (2.1) immediately implies that
$$\sqrt{-1} \partial \bar{\partial} \varphi=\sqrt{-1}\left(e_{i} \bar{e}_{j}(\varphi)-\left[e_{i}, \bar{e}_{j}\right]^{(0,1)}(\varphi)\right) \theta^{i} \wedge \bar{\theta}^{j},$$
and hence
$$\tilde{g}_{i \bar{j}}=g_{i \bar{j}}+e_{i} \bar{e}_{j}(\varphi)-\left[e_{i}, \bar{e}_{j}\right]^{(0,1)}(\varphi) .$$
We now assume for the rest of this section that our local frame $\left\{e_{1}, \ldots, e_{n}\right\}$ is unitary with respect to $g$, so that $g_{i \bar{j}}=\delta_{i j}$. Therefore in these coordinates, $|\partial \varphi|_{g}^{2}=\sum_{k} \varphi_{k} \varphi_{\bar{k}}$, where we are writing $\varphi_{k}=e_{k}(\varphi)$ and $\varphi_{\bar{k}}=\bar{e}_{k}(\varphi)$.

Fix a point $x_{0}$ at which $Q$ achieves its maximum on $M$. Then, after making a unitary transformation, we may and do assume that $\tilde{g}_{i \bar{j}}$ is diagonal at $x_{0}$.

Define a second order elliptic operator
$$L:=\tilde{g}^{i \bar{j}}\left(e_{i} \bar{e}_{j}-\left[e_{i}, \bar{e}_{j}\right]^{(0,1)}\right) .$$

Compute at $x_{0}$, using (2.11),
$$\begin{aligned}
0 \geqslant & L(Q) \\
= & \tilde{g}^{i \bar{i}}\left\{e_{i} \bar{e}_{i}\left(e^{f}|\partial \varphi|_{g}^{2}\right)-\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(e^{f}|\partial \varphi|_{g}^{2}\right)\right\} \\
= & \tilde{g}^{i \bar{i}}\left\{|\partial \varphi|_{g}^{2} e_{i} \bar{e}_{i}\left(e^{f}\right)+e^{f} e_{i} \bar{e}_{i}\left(|\partial \varphi|_{g}^{2}\right)+2 \operatorname{Re}\left(e_{i}\left(e^{f}\right) \bar{e}_{i}\left(|\partial \varphi|_{g}^{2}\right)\right)\right. \\
& \left.-|\partial \varphi|_{g}^{2}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(e^{f}\right)-e^{f}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(|\partial \varphi|_{g}^{2}\right)\right\} \\
= & |\partial \varphi|_{g}^{2} L\left(e^{f}\right)+e^{f} L\left(|\partial \varphi|_{g}^{2}\right)+2 \operatorname{Re}\left(\tilde{g}^{i \bar{i}} e_{i}\left(e^{f}\right) \bar{e}_{i}\left(|\partial \varphi|_{g}^{2}\right)\right) .
\end{aligned}$$
We now compute each of these three terms in turn. First
$$\begin{aligned}
L\left(e^{f}\right) & =\tilde{g}^{i \bar{i}}\left\{e_{i} \bar{e}_{i}\left(e^{f}\right)-\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(e^{f}\right)\right\} \\
& =\tilde{g}^{i \bar{i}}\left\{e^{f}\left(f^{\prime}\right)^{2}\left|\varphi_{i}\right|^{2}+e^{f} f^{\prime \prime}\left|\varphi_{i}\right|^{2}+e^{f} f^{\prime} e_{i} \bar{e}_{i}(\varphi)-e^{f} f^{\prime}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right\} \\
& =e^{f}\left(\left(f^{\prime}\right)^{2}+f^{\prime \prime}\right)|\partial \varphi|_{\tilde{g}}^{2}+n e^{f} f^{\prime}-e^{f} f^{\prime} \sum_{i} \tilde{g}^{\bar{i} \bar{i}},
\end{aligned}$$
where we have used (4.1) for the last line.
Next,
$$\begin{aligned}
L\left(|\partial \varphi|_{g}^{2}\right)= & \sum_{k} \tilde{g}^{i \bar{i}}\left\{e_{i} \bar{e}_{i}\left(\varphi_{k} \varphi_{\bar{k}}\right)-\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\varphi_{k} \varphi_{\bar{k}}\right)\right\} \\
= & \sum_{k} \tilde{g}^{i \bar{i}}\left\{\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}+\varphi_{k} e_{i} \bar{e}_{i} \bar{e}_{k}(\varphi)-\varphi_{k}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} \bar{e}_{k}(\varphi)\right. \\
& \left.+\varphi_{\bar{k}} e_{i} \bar{e}_{i} e_{k}(\varphi)-\varphi_{\bar{k}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} e_{k}(\varphi)\right\} .
\end{aligned}$$
To deal with the terms involving three derivatives of $\varphi$, we use the equation (1.4), which we can rewrite in our coordinates as
$$\log \operatorname{det}\left(\tilde{g}_{i \bar{j}}\right)=F .$$
Applying $e_{k}$, we obtain $\tilde{g}^{i \bar{j}} e_{k}\left(\tilde{g}_{i \bar{j}}\right)=F_{k}$, which at the point $x_{0}$ gives us
$$\begin{aligned}
& \tilde{g}^{i \bar{i}}\left(e_{k} e_{i} \bar{e}_{i}(\varphi)-e_{k}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right)=F_{k} \\
& \tilde{g}^{i \bar{i}}\left(\bar{e}_{k} e_{i} \bar{e}_{i}(\varphi)-\bar{e}_{k}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right)=F_{\bar{k}} .
\end{aligned}$$

Hence
$$\begin{aligned}
& \sum_{k} \tilde{g}^{i \bar{i}}\left\{\varphi_{k} e_{i} \bar{e}_{i} \bar{e}_{k}(\varphi)-\varphi_{k}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} \bar{e}_{k}(\varphi)\right\} \\
= & \sum_{k} \tilde{g}^{i \bar{i}} \varphi_{k}\left\{e_{i} \bar{e}_{k} \bar{e}_{i}(\varphi)-e_{i}\left[\bar{e}_{k}, \bar{e}_{i}\right](\varphi)-\bar{e}_{k}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)+\left[\bar{e}_{k},\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\right](\varphi)\right\} \\
= & \sum_{k} \tilde{g}^{i \bar{i}} \varphi_{k}\left\{\bar{e}_{k} e_{i} \bar{e}_{i}(\varphi)-\left[\bar{e}_{k}, e_{i}\right] \bar{e}_{i}(\varphi)-e_{i}\left[\bar{e}_{k}, \bar{e}_{i}\right](\varphi)-\bar{e}_{k}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right. \\
& \left.+\left[\bar{e}_{k},\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\right](\varphi)\right\} \\
= & \sum_{k} \varphi_{k} F_{\bar{k}}+\sum_{k} \tilde{g}^{i \bar{i}} \varphi_{k}\left\{-\bar{e}_{i}\left[\bar{e}_{k}, e_{i}\right](\varphi)+\left[\bar{e}_{i},\left[\bar{e}_{k}, e_{i}\right]\right](\varphi)-e_{i}\left[\bar{e}_{k}, \bar{e}_{i}\right](\varphi)\right. \\
& \left.+\left[\bar{e}_{k},\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\right](\varphi)\right\} \\
\geqslant & \sum_{k} \varphi_{k} F_{\bar{k}}-C|\partial \varphi|_{g} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|\bar{e}_{i} e_{k}(\varphi)\right|+\left|e_{i} e_{k}(\varphi)\right|\right)-C|\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{i \bar{i}},
\end{aligned}$$
where for the last inequality, we have used the fact that commutators of first order operators, such as $\left[\bar{e}_{k}, e_{i}\right]$, are first order operators.

Similarly,
$$\begin{aligned}
& \sum_{k} \tilde{g}^{i \bar{i}}\left\{\varphi_{\bar{k}} e_{i} \bar{e}_{i} e_{k}(\varphi)-\varphi_{\bar{k}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} e_{k}(\varphi)\right\} \\
\geqslant & \sum_{k} \varphi_{\bar{k}} F_{k}-C|\partial \varphi|_{g} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|\bar{e}_{i} e_{k}(\varphi)\right|+\left|e_{i} e_{k}(\varphi)\right|\right)-C|\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{i \bar{i}} .
\end{aligned}$$

Using these last two inequalities in (4.4), and combining with Young's inequality, we obtain for $\varepsilon \in(0,1 / 2]$ (to be determined later),
$$\begin{aligned}
L\left(|\partial \varphi|_{g}^{2}\right) \geqslant & (1-\varepsilon) \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \\
& -C \varepsilon^{-1}|\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{i \bar{i}}+2 \operatorname{Re}\left(\sum_{k} \varphi_{k} F_{\bar{k}}\right) .
\end{aligned}$$

We now deal with the third term on the right hand side of (4.2),
$$\begin{aligned}
& 2 \operatorname{Re}\left(\tilde{g}^{\bar{i}} e_{i}\left(e^{f}\right) \bar{e}_{i}\left(|\partial \varphi|_{g}^{2}\right)\right) \\
= & 2 \operatorname{Re}\left(\sum_{k} \tilde{g}^{i \bar{i}} e^{f} f^{\prime} \varphi_{i} \varphi_{\bar{k}} \bar{e}_{i} e_{k}(\varphi)\right)+2 \operatorname{Re}\left(\sum_{k} \tilde{g}^{\bar{i}} e^{f} f^{\prime} \varphi_{i} \varphi_{k} \bar{e}_{i} \bar{e}_{k}(\varphi)\right) .
\end{aligned}$$

For the first of these terms, we have
$$\begin{aligned}
& 2 \operatorname{Re}\left(\sum_{k} \tilde{g}^{i \bar{i}} e^{f} f^{\prime} \varphi_{i} \varphi_{\bar{k}} \bar{e}_{i} e_{k}(\varphi)\right) \\
= & 2 \operatorname{Re}\left\{\sum_{k} \tilde{g}^{i \bar{i}} e^{f} f^{\prime} \varphi_{i} \varphi_{\bar{k}}\left(e_{k} \bar{e}_{i}(\varphi)-\left[e_{k}, \bar{e}_{i}\right]^{(0,1)}(\varphi)-\left[e_{k}, \bar{e}_{i}\right]^{(1,0)}(\varphi)\right)\right\} \\
\geqslant & 2 \operatorname{Re}\left\{\sum_{k} \tilde{g}^{i \bar{i}} e^{f} f^{\prime} \varphi_{i} \varphi_{\bar{k}}\left(\tilde{g}_{k \bar{i}}-\delta_{k i}\right)\right\}-C e^{f}\left|f^{\prime}\right||\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{i \bar{i}}\left|\varphi_{i}\right| \\
\geqslant & 2 e^{f} f^{\prime}|\partial \varphi|_{g}^{2}-2 e^{f} f^{\prime}|\partial \varphi|_{\tilde{g}}^{2}-\varepsilon e^{f}\left(f^{\prime}\right)^{2}|\partial \varphi|_{g}^{2}|\partial \varphi|_{\tilde{g}}^{2}-C \varepsilon^{-1} e^{f}|\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{\bar{i}} .
\end{aligned}$$
For the second term of (4.9),
$$\begin{aligned}
& 2 \operatorname{Re}\left(\sum_{k} \tilde{g}^{i \bar{i}} e^{f} f^{\prime} \varphi_{i} \varphi_{k} \bar{e}_{i} \bar{e}_{k}(\varphi)\right) \\
\geqslant & -(1-\varepsilon) \sum_{k} \tilde{g}^{i \bar{i}} e^{f}\left|\bar{e}_{i} \bar{e}_{k}(\varphi)\right|^{2}-(1+2 \varepsilon) e^{f}\left(f^{\prime}\right)^{2}|\partial \varphi|_{g}^{2}|\partial \varphi|_{\tilde{g}}^{2},
\end{aligned}$$
using the fact that for any real numbers $a$ and $b$, and $\varepsilon \in(0,1 / 2]$,
$$2 a b \geqslant-(1-\varepsilon) a^{2}-(1+2 \varepsilon) b^{2} .$$
Combining (4.9), (4.10), (4.11),
$$\begin{aligned}
& 2 \operatorname{Re}\left(\tilde{g}^{i \bar{i}} e_{i}\left(e^{f}\right) \bar{e}_{i}\left(|\partial \varphi|_{g}^{2}\right)\right) \\
\geqslant & 2 e^{f} f^{\prime}|\partial \varphi|_{g}^{2}-2 e^{f} f^{\prime}|\partial \varphi|_{\tilde{g}}^{2}-(1+3 \varepsilon) e^{f}\left(f^{\prime}\right)^{2}|\partial \varphi|_{g}^{2}|\partial \varphi|_{\tilde{g}}^{2} \\
& -C \varepsilon^{-1} e^{f}|\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{i \bar{i}}-(1-\varepsilon) \sum_{k} \tilde{g}^{i \bar{i}} e^{f}\left|\bar{e}_{i} \bar{e}_{k}(\varphi)\right|^{2}
\end{aligned}$$

We now put together (4.2), (4.3), (4.8), (4.12) to obtain, at $x_{0}$,
$$\begin{aligned}
0 \geqslant & e^{f}\left(f^{\prime \prime}-3 \varepsilon\left(f^{\prime}\right)^{2}\right)|\partial \varphi|_{g}^{2}|\partial \varphi|_{\tilde{g}}^{2}+e^{f}\left(-f^{\prime}-C_{0} \varepsilon^{-1}\right)|\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{i \bar{i}} \\
& +2 e^{f} \operatorname{Re}\left(\sum_{k} \varphi_{k} F_{\bar{k}}\right)+(2+n) e^{f} f^{\prime}|\partial \varphi|_{g}^{2}-2 e^{f} f^{\prime}|\partial \varphi|_{\tilde{g}}^{2}
\end{aligned}$$
for a uniform constant $C_{0}$. We now choose the function $f=f(\varphi)$ and constant $\varepsilon>0$ as follows. Define
$$f(\varphi)=\frac{e^{-A(\varphi-1)}}{A}, \quad \varepsilon=\frac{A e^{A\left(\varphi\left(x_{0}\right)-1\right)}}{6} .$$
for a large constant $A$ to be determined shortly. Note that since $\sup _{M} \varphi=0$, the constant $\varepsilon$ is small. Compute, at $x_{0}$,
$$\begin{aligned}
f^{\prime \prime}-3 \varepsilon\left(f^{\prime}\right)^{2} & =\frac{A e^{-A\left(\varphi\left(x_{0}\right)-1\right)}}{2} \\
-f^{\prime}-C_{0} \varepsilon^{-1} & =\left(1-\frac{6 C_{0}}{A}\right) e^{-A\left(\varphi\left(x_{0}\right)-1\right)} .
\end{aligned}$$
In particular, note that $f^{\prime}$ is negative. Choosing $A=12 C_{0}$ we obtain lower bounds, at $x_{0}$,
$$f^{\prime \prime}-3 \varepsilon\left(f^{\prime}\right)^{2} \geqslant C^{-1}, \quad-f^{\prime}-C_{0} \varepsilon^{-1} \geqslant C^{-1},$$
for a uniform constant $C>0$. In (4.13), after dividing by $e^{f}$, and increasing $C$ if necessary, we obtain
$$0 \geqslant C^{-1}|\partial \varphi|_{g}^{2}|\partial \varphi|_{\tilde{g}}^{2}+C^{-1}|\partial \varphi|_{g}^{2} \sum_{i} \tilde{g}^{i \bar{i}}-C|\partial \varphi|_{g}^{2}-C .$$
Dividing by $|\partial \varphi|_{g}^{2}$ (which we may assume is larger than 1, without loss of generality), we obtain uniform upper bounds for $\sum_{i} \tilde{g}^{i \bar{i}}$ and $|\partial \varphi|_{\tilde{g}}^{2}$ at $x_{0}$. Combining the upper bound of $\sum_{i} \tilde{g}^{i \bar{i}}$ with the equation $\operatorname{det} \tilde{g}=e^{F}$, we obtain a uniform upper bound for $\tilde{g}_{i \bar{i}}$ for each $i$. Then
$$|\partial \varphi|_{g}^{2}=\sum_{i}\left|\varphi_{i}\right|^{2}=\left.\sum_{i} \tilde{g}_{i \bar{i}} \tilde{g}^{\bar{i}} \overline{\mid} \varphi_{i}\right|^{2} \leqslant C|\partial \varphi|_{\tilde{g}}^{2} \leqslant C^{\prime},$$
as required. This completes the proof of the proposition. \(\square\)

Before we end this section, we state the following lemma which we will need later. It is an immediate consequence of the previous proposition, and the estimate (4.8), (but taking now $\varepsilon=1 / 2$ ).

Lemma 4.2. For a uniform constant $C$,
$$L\left(|\partial \varphi|_{g}^{2}\right) \geqslant \frac{1}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right)-C \sum_{i} \tilde{g}^{i \bar{i}}-C .$$

\section*{5. Second order estimate}

In this section we prove:
Proposition 5.1. Let $\varphi$ solve the Monge-Ampère equation (1.4). Then there exists a constant $C$, depending only on $(M, g, J)$ and bounds for $F$ such that
$$\left|\nabla^{2} \varphi\right|_{g} \leqslant C,$$
where $\nabla^{2} \varphi$ denotes the real Hessian of $\varphi$ with respect to the metric $g$ (using its Levi-Civita connection).

To be precise, the dependence of the constant $C$ on $F$ is as follows: $C$ depends only on upper bounds for $\sup _{M} F, \sup _{M}|\partial F|_{g}$, and a lower bound for $\nabla^{2} F$ w.r.t. $g$. It does not depend on $\inf _{M} F$.

Proof. We first make the preliminary observation that
$$\left|\nabla^{2} \varphi\right|_{g} \leqslant C \lambda_{1}\left(\nabla^{2} \varphi\right)+C^{\prime},$$
everywhere on $M$, where $\lambda_{1}\left(\nabla^{2} \varphi\right)$ is the largest eigenvalue of the real Hessian $\nabla^{2} \varphi$ (with respect to the metric $g$ ). Indeed, if we write $\lambda_{1}\left(\nabla^{2} \varphi\right) \geqslant$ $\lambda_{2}\left(\nabla^{2} \varphi\right) \geqslant \ldots \geqslant \lambda_{2 n}\left(\nabla^{2} \varphi\right)$ for all the eigenvalues, then
$$\left|\nabla^{2} \varphi\right|_{g}=\left(\sum_{\alpha=1}^{2 n} \lambda_{\alpha}^{2}\right)^{\frac{1}{2}} \leqslant C\left(\left|\lambda_{1}\right|+\left|\lambda_{2 n}\right|\right) .$$
On the other hand (2.5) gives
$$\sum_{\alpha=1}^{2 n} \lambda_{\alpha}=\Delta \varphi=2 \Delta^{C} \varphi+\tau(d \varphi) \geqslant-2 n+\tau(d \varphi) \geqslant-C,$$
using Proposition 4.1. This inequality implies that $\lambda_{1} \geqslant-C$, and so
$$\left|\lambda_{1}\right| \leqslant \lambda_{1}+C,$$
and it also implies that
$$\left|\lambda_{2 n}\right| \leqslant C \lambda_{1}+C,$$
and (5.1) follows. Therefore it suffices to bound $\lambda_{1}\left(\nabla^{2} \varphi\right)$ from above. To achieve this we apply the maximum principle to the quantity
$$Q=\log \lambda_{1}\left(\nabla^{2} \varphi\right)+h\left(|\partial \varphi|_{g}^{2}\right)+e^{-A \varphi},$$
on the set $\left\{x \in M \mid \lambda_{1}\left(\nabla^{2} \varphi(x)\right)>0\right\}$, which we may assume is nonempty, without loss of generality. Here $h$ is given by
$$h(s)=-\frac{1}{2} \log \left(1+\sup _{M}|\partial \varphi|_{g}^{2}-s\right),$$
and $A>1$ is a constant to be determined (which will be uniform, in the sense that it will depend only on the background data). Observe that $h\left(|\partial \varphi|_{g}^{2}\right)$ is uniformly bounded, and we have
$$\frac{1}{2} \geqslant h^{\prime} \geqslant \frac{1}{2+2 \sup _{M}|\partial \varphi|_{g}^{2}}>0, \quad \text { and } h^{\prime \prime}=2\left(h^{\prime}\right)^{2},$$
where we evaluate $h$ and its derivatives at $|\partial \varphi|_{g}^{2}$.
Note that $Q$ is a continuous function on its domain, and goes to $-\infty$ on its boundary (if this is nonempty), and hence achieves a maximum at a point $x_{0} \in M$ with $\lambda_{1}\left(\nabla^{2} \varphi\left(x_{0}\right)\right)>0$. However, $Q$ is not smooth in general, since the eigenspace associated to $\lambda_{1}$ may have dimension strictly larger than 1. We deal with this using a perturbation argument, as in [40, 41].

First we discuss the choice of coordinate system in a neighborhood of $x_{0}$. Let $V_{1}$ be a unit vector (with respect to $g$ ) corresponding to the largest eigenvalue $\lambda_{1}$ of $\nabla^{2} \varphi$, so that at $x_{0}$,
$$\nabla^{2} \varphi\left(V_{1}, V_{1}\right)=\lambda_{1} .$$

Since $g$ is almost Hermitian, it follows easily that we can find a coordinate system $x^{1}, x^{2}, \ldots, x^{2 n}$ centered at $x_{0}$, such that in the frame $\partial_{1}, \ldots, \partial_{2 n}$ the almost complex structure $J$ is standard at $x_{0}$ (i.e. $J \partial_{1}=\partial_{2}$, etc.) and the vectors $\partial_{1}, \ldots, \partial_{2 n}$ are $g$-orthonormal at $x_{0}$. Furthermore, after making a quadratic change of coordinates, we assume that the first derivatives of $g$ vanish at $x_{0}$ :
$$\left.\partial_{\gamma} g_{\alpha \beta}\right|_{x_{0}}=0, \quad \text { for all } \alpha, \beta, \gamma=1, \ldots, 2 n .$$
If at $x_{0}$ we let
$$e_{1}=\frac{1}{\sqrt{2}}\left(\partial_{1}-\sqrt{-1} \partial_{2}\right), e_{2}=\frac{1}{\sqrt{2}}\left(\partial_{3}-\sqrt{-1} \partial_{4}\right), \ldots, e_{n}=\frac{1}{\sqrt{2}}\left(\partial_{2 n-1}-\sqrt{-1} \partial_{2 n}\right),$$
then these form a frame of $(1,0)$ vectors at $x_{0}$, and we have that $g_{i \bar{j}}:=$ $g\left(e_{i}, \bar{e}_{j}\right)=\delta_{i j}$ (i.e. the frame is $g$-unitary). By performing a further linear change of coordinates at $x_{0}$, which commutes with $J$, we may assume that at $x_{0}$ we have $g_{i \bar{j}}=\delta_{i j}$ and $\left(\tilde{g}_{i \bar{j}}\right)$ is diagonal with
$$\tilde{g}_{1 \overline{1}} \geqslant \tilde{g}_{2 \overline{2}} \geqslant \cdots \geqslant \tilde{g}_{n \bar{n}} .$$
This does not affect condition (5.5), or the fact that $J$ is standard at $x_{0}$, and since $g$ is almost Hermitian we see that the (new) real vectors $\partial_{1}, \ldots, \partial_{2 n}$ are still $g$-orthonormal at $x_{0}$.

We extend $e_{1}, \ldots, e_{n}$ smoothly to a $g$-unitary frame of $(1,0)$ vectors in a neighborhood of $x_{0}$. The coordinate system and the local unitary frame are now fixed. Extend $V_{1}$ to an orthonormal basis $V_{1}, \ldots, V_{2 n}$ of eigenvectors of $\nabla^{2} \varphi$ (with respect to $g$ ) at $x_{0}$, corresponding to eigenvalues $\lambda_{1}\left(\nabla^{2} \varphi\right) \geqslant$ $\lambda_{2}\left(\nabla^{2} \varphi\right) \geqslant \ldots \geqslant \lambda_{2 n}\left(\nabla^{2} \varphi\right)$. Write $\left\{V_{\beta}^{\alpha}\right\}_{\alpha=1}^{2 n}$ for the components of the vector $V_{\beta}$ at $x_{0}$, with respect to the coordinates $x^{1}, \ldots, x^{2 n}$ described above. We extend $V_{1}, V_{2}, \ldots, V_{2 n}$ to be vector fields in a neighborhood of $x_{0}$ by taking the components to be constant. Note that we do not assert that the $V_{i}$ are eigenvectors for $\nabla^{2} \varphi$ outside $x_{0}$.

We apply a perturbation argument. We define near $x_{0}$ a smooth section $B=\left(B_{\alpha \beta}\right)$ of $T^{*} M \otimes T^{*} M$ by setting its value in our coordinates $x^{1}, \ldots, x^{2 n}$ at $x_{0}$ to be
$$B_{\alpha \beta}=\delta_{\alpha \beta}-V_{1}^{\alpha} V_{1}^{\beta},$$
and extending it to be constant in these coordinates nearby $x_{0}$. At $x_{0}$,
$$B\left(V_{1}, V_{1}\right)=\sum_{\alpha, \beta=1}^{2 n} B_{\alpha \beta} V_{1}^{\alpha} V_{1}^{\beta}=0$$
and $B(Y, Y)=1$ for any unit vector $Y g$-orthogonal to $V_{1}$.
It is convenient to work with endomorphisms of $T M$ instead of symmetric sections of $T^{*} M \otimes T^{*} M$. We define a local endomorphism $\Phi=\left(\Phi^{\alpha}{ }_{\beta}\right)$ of $T M$ by
$$\Phi^{\alpha}{ }_{\beta}=g^{\alpha \gamma} \nabla_{\gamma \beta}^{2} \varphi-g^{\alpha \gamma} B_{\gamma \beta} .$$

Now instead of $\lambda_{1}\left(\nabla^{2} \varphi\right)$, we consider $\lambda_{1}(\Phi)$, the largest eigenvalue of the endomorphism $\Phi$.

Note that $B_{\alpha \beta}$ is nonnegative definite and hence $\lambda_{1}(\Phi) \leqslant \lambda_{1}\left(\nabla^{2} \varphi\right)$ in a neighborhood of $x_{0}$ while, by definition of $B$ and $V_{1}, \lambda_{1}(\Phi)=\lambda_{1}\left(\nabla^{2} \varphi\right)$ at $x_{0}$. Moreover, at $x_{0}$, the eigenspace of $\Phi$ corresponding to the largest eigenvalue now has dimension 1, and hence $\lambda_{1}=\lambda_{1}(\Phi)$ is smooth in a neighborhood of $x_{0}$.

We can now consider the perturbed quantity $\hat{Q}$ defined in a neighborhood of $x_{0}$ by
$$\hat{Q}=\log \lambda_{1}(\Phi)+h\left(|\partial \varphi|_{g}^{2}\right)+e^{-A \varphi},$$
which still obtains a local maximum at $x_{0} . V_{1}, \ldots, V_{2 n}$ are eigenvectors for $\Phi$ at $x_{0}$, corresponding to eigenvalues $\lambda_{1}(\Phi)>\lambda_{2}(\Phi) \geqslant \ldots \geqslant \lambda_{2 n}(\Phi)$. In what follows we write $\lambda_{\alpha}$ for $\lambda_{\alpha}(\Phi)$.

The first and second derivatives of $\lambda_{1}$ at $x_{0}$ are given by the following lemma.

Lemma 5.2. At $x_{0}$, we have
$$\begin{aligned}
\lambda_{1}^{\alpha \beta}: & =\frac{\partial \lambda_{1}}{\partial \Phi_{\beta}^{\alpha}}=V_{1}^{\alpha} V_{1}^{\beta} \\
\lambda_{1}^{\alpha \beta, \gamma \delta}: & =\frac{\partial^{2} \lambda_{1}}{\partial \Phi_{\beta}^{\alpha} \partial \Phi_{\delta}^{\gamma}}=\sum_{\mu>1} \frac{V_{1}^{\alpha} V_{\mu}^{\beta} V_{\mu}^{\gamma} V_{1}^{\delta}+V_{\mu}^{\alpha} V_{1}^{\beta} V_{1}^{\gamma} V_{\mu}^{\delta}}{\lambda_{1}-\lambda_{\mu}},
\end{aligned}$$
where Greek indices $\alpha, \beta, \ldots$ go from 1 to $2 n$, unless otherwise indicated.
Proof. Consider the constant orthogonal matrix $V=\left(V_{\beta}^{\alpha}\right)$, where $V_{\beta}^{\alpha}$ were defined above. It has the property that $V^{T} \Phi V$ is diagonal at $x_{0}$. Define $\Theta=\left(\Theta^{\alpha}{ }_{\beta}\right):=V^{T} \Phi V$, which has the same eigenvalues as $\Phi$. Since $\Theta$ is diagonal at $x_{0}$, with $\lambda_{1}$ distinct from all the other eigenvalues, we have the following well-known formulas (see e.g. [39]):
$$\begin{aligned}
\frac{\partial \lambda_{1}(\Theta)}{\partial \Theta^{\nu}{ }_{\mu}} & =\delta_{1 \nu} \delta_{1 \mu} \\
\frac{\partial^{2} \lambda_{1}(\Theta)}{\partial \Theta^{\nu}{ }_{\mu} \partial \Theta^{\theta}{ }_{\eta}} & =\left(1-\delta_{1 \mu}\right) \frac{\delta_{1 \nu} \delta_{1 \eta} \delta_{\mu \theta}}{\lambda_{1}-\lambda_{\mu}}+\left(1-\delta_{1 \eta}\right) \frac{\delta_{1 \theta} \delta_{1 \mu} \delta_{\nu \eta}}{\lambda_{1}-\lambda_{\eta}} .
\end{aligned}$$
Hence, by the chain rule, we compute at $x_{0}$,
$$\frac{\partial \lambda_{1}(\Phi)}{\partial \Phi_{\beta}^{\alpha}}=\frac{\partial \lambda_{1}(\Theta)}{\partial \Phi_{\beta}^{\alpha}}=\frac{\partial \lambda_{1}(\Theta)}{\partial \Theta_{\mu}^{\nu}} \cdot \frac{\partial \Theta_{\mu}^{\nu}}{\partial \Phi_{\beta}^{\alpha}}=\delta_{1 \nu} \delta_{1 \mu} V_{\nu}^{\alpha} V_{\mu}^{\beta}=V_{1}^{\alpha} V_{1}^{\beta} .$$

Similarly,
$$\begin{aligned}
\frac{\partial^{2} \lambda_{1}(\Phi)}{\partial \Phi^{\alpha}{ }_{\beta} \partial \Phi_{\delta}^{\gamma}} & =\frac{\partial^{2} \lambda_{1}(\Theta)}{\partial \Theta^{\nu}{ }_{\mu} \partial \Theta_{\eta}^{\theta}} \cdot \frac{\partial \Theta_{\mu}^{\nu}}{\partial \Phi_{\beta}^{\alpha}} \cdot \frac{\partial \Theta_{\eta}^{\theta}}{\partial \Phi_{\delta}^{\gamma}} \\
& =\left(\left(1-\delta_{1 \mu}\right) \frac{\delta_{1 \nu} \delta_{1 \eta} \delta_{\mu \theta}}{\lambda_{1}-\lambda_{\mu}}+\left(1-\delta_{1 \eta}\right) \frac{\delta_{1 \theta} \delta_{1 \mu} \delta_{\nu \eta}}{\lambda_{1}-\lambda_{\eta}}\right) V_{\nu}^{\alpha} V_{\mu}^{\beta} V_{\theta}^{\gamma} V_{\eta}^{\delta} \\
& =\left(1-\delta_{1 \mu}\right) \frac{V_{1}^{\alpha} V_{\mu}^{\beta} V_{\mu}^{\gamma} V_{1}^{\delta}}{\lambda_{1}-\lambda_{\mu}}+\left(1-\delta_{1 \eta}\right) \frac{V_{\eta}^{\alpha} V_{1}^{\beta} V_{1}^{\gamma} V_{\eta}^{\delta}}{\lambda_{1}-\lambda_{\eta}},
\end{aligned}$$
as required. \(\square\)

As in the previous section, we denote by $L$ the operator
$$L=\tilde{g}^{i \bar{j}}\left(e_{i} \bar{e}_{j}-\left[e_{i}, \bar{e}_{j}\right]^{(0,1)}\right) .$$
We first prove a lower bound for $L\left(\lambda_{1}\right)$. In what follows, we assume without loss of generality that $\lambda_{1} \gg 1$ at $x_{0}$. We also note that from (1.4) and the arithmetic-geometric mean inequality,
$$\sum_{i} \tilde{g}^{i \bar{i}} \geqslant c,$$
for a uniform $c>0$.
Lemma 5.3. At $x_{0}$, we have
$$\begin{aligned}
L\left(\lambda_{1}\right) \geqslant 2 & \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}-\lambda_{\alpha}}+\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2} \\
& -2 \tilde{g}^{i \bar{i}}\left[V_{1}, e_{i}\right] V_{1} \bar{e}_{i}(\varphi)-2 \tilde{g}^{i \bar{i}}\left[V_{1}, \bar{e}_{i}\right] V_{1} e_{i}(\varphi)-C \lambda_{1} \sum_{i} \tilde{g}^{i \bar{i}},
\end{aligned}$$
where we are writing
$$\varphi_{\alpha \beta}=\nabla_{\alpha \beta}^{2} \varphi, \quad \varphi_{V_{\alpha} V_{\beta}}=\varphi_{\gamma \delta} V_{\alpha}^{\gamma} V_{\beta}^{\delta}=\nabla^{2} \varphi\left(V_{\alpha}, V_{\beta}\right) .$$
Proof. Using (5.5), (5.8) and the fact that $\tilde{g}$ is diagonal at $x_{0}$,
$$\begin{aligned}
L\left(\lambda_{1}\right)= & \tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta, \gamma \delta} e_{i}\left(\Phi^{\gamma}{ }_{\delta}\right) \bar{e}_{i}\left(\Phi^{\alpha}{ }_{\beta}\right)+\tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta} e_{i} \bar{e}_{i}\left(\Phi^{\alpha}{ }_{\beta}\right)-\tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\Phi^{\alpha}{ }_{\beta}\right) \\
= & \tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta, \gamma \delta} e_{i}\left(\varphi_{\gamma \delta}\right) \bar{e}_{i}\left(\varphi_{\alpha \beta}\right)+\tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta} e_{i} \bar{e}_{i}\left(\varphi_{\alpha \beta}\right)+\tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta} \varphi_{\gamma \beta} e_{i} \bar{e}_{i}\left(g^{\alpha \gamma}\right) \\
& -\tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta} B_{\gamma \beta} e_{i} \bar{e}_{i}\left(g^{\alpha \gamma}\right)-\tilde{g}^{i \bar{i}} \lambda_{1}^{\alpha \beta}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\varphi_{\alpha \beta}\right) \\
\geqslant & 2 \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}-\lambda_{\alpha}}+\tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i}\left(\varphi_{V_{1} V_{1}}\right)-\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\varphi_{V_{1} V_{1}}\right) \\
& -C \lambda_{1} \sum_{i} \tilde{g}^{i \bar{i}} .
\end{aligned}$$

Next, we claim that
$$\begin{aligned}
& \tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i}\left(\varphi_{V_{1}} V_{1}\right)-\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\varphi_{V_{1} V_{1}}\right) \geqslant \\
& \quad=\tilde{g}^{i \bar{i}} V_{1} V_{1}\left(\tilde{g}_{i \bar{i}}\right)-2 \tilde{g}^{i \bar{i}}\left[V_{1}, e_{i}\right] V_{1} \bar{e}_{i}(\varphi)-2 \tilde{g}^{i \bar{i}}\left[V_{1}, \bar{e}_{i}\right] V_{1} e_{i}(\varphi)-C \lambda_{1} \sum_{i} \tilde{g}^{i \bar{i}} .
\end{aligned}$$
Given this, the lemma follows, since in our coordinates, our equation (1.4) is
$$\log \operatorname{det} \tilde{g}=\log \operatorname{det} g+F .$$
Hence, recalling that $g_{i \bar{j}}=g\left(e_{i}, \bar{e}_{j}\right)=\delta_{i j}$ near $x_{0}$,
$$\tilde{g}^{i \bar{j}} V_{1}\left(\tilde{g}_{i \bar{j}}\right)=V_{1}(F),$$
and applying $V_{1}$ again,
$$\tilde{g}^{i \bar{i}} V_{1} V_{1}\left(\tilde{g}_{i \bar{i}}\right)=\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}+V_{1} V_{1}(F),$$
and then (5.10) follows from (5.11), (5.12) and (5.9).
We now give the proof of (5.12). We have
$$\tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i}\left(\varphi_{V_{1} V_{1}}\right)=\tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i} V_{1} V_{1}(\varphi)-\tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i}\left(\nabla_{V_{1}} V_{1}\right)(\varphi),$$
since, for any $\alpha, \beta$,
$$\varphi_{V_{\alpha} V_{\beta}}=V_{\alpha} V_{\beta}(\varphi)-\left(\nabla_{V_{\alpha}} V_{\beta}\right)(\varphi) .$$
First we deal with the second term of (5.14). We claim that
$$\left|\tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i}\left(\nabla_{V_{1}} V_{1}\right)(\varphi)\right| \leqslant C \lambda_{1} \sum_{i} \tilde{g}^{i \bar{i}} .$$

For simplicity of notation let $W=\nabla_{V_{1}} V_{1}$. Then at $x_{0}$ we have, using (4.1),
$$\begin{aligned}
e_{i} \bar{e}_{i} W(\varphi) & =e_{i} W \bar{e}_{i}(\varphi)+e_{i}\left[\bar{e}_{i}, W\right](\varphi) \\
& =W e_{i} \bar{e}_{i}(\varphi)+\left[e_{i}, W\right] \bar{e}_{i}(\varphi)+e_{i}\left[\bar{e}_{i}, W\right](\varphi) \\
& =W\left(\tilde{g}_{i ̄}\right)+W\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)+\left[e_{i}, W\right] \bar{e}_{i}(\varphi)+e_{i}\left[\bar{e}_{i}, W\right](\varphi) .
\end{aligned}$$
Applying $W$ to (1.4) we have
$$\tilde{g}^{i \bar{i}} W\left(\tilde{g}_{i \bar{i}}\right)=W(F),$$
and (5.15) now follows from (5.1) and (5.9).
Next we note that
$$\begin{aligned}
-\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\varphi_{V_{1} V_{1}}\right) & =-\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} V_{1} V_{1}(\varphi)+\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\nabla_{V_{1}} V_{1}\right)(\varphi) \\
& \geqslant-\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} V_{1} V_{1}(\varphi)-C \lambda_{1} \sum_{i} \tilde{g}^{i \bar{i}},
\end{aligned}$$
for a uniform constant $C$, and so combining this with (5.14), (5.15),
$$\begin{aligned}
& \tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i}\left(\varphi_{V_{1} V_{1}}\right)-\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}\left(\varphi_{V_{1} V_{1}}\right) \\
& \quad \geqslant \tilde{g}^{i \bar{i}} e_{i} \bar{e}_{i} V_{1} V_{1}(\varphi)-\tilde{g}^{i \bar{i}}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} V_{1} V_{1}(\varphi)-C \lambda_{1} \sum_{i} \tilde{g}^{i \bar{i}} .
\end{aligned}$$
In what follows, we write $E$ for a term (which may change from line to line) which can be bounded by $C \lambda_{1} \sum_{i} \tilde{g}^{i \bar{i}}$. We have
$$\begin{aligned}
\tilde{g}^{i \bar{i}} & \left\{e_{i} \bar{e}_{i} V_{1} V_{1}(\varphi)-\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} V_{1} V_{1}(\varphi)\right\} \\
= & \tilde{g}^{i \bar{i}}\left\{e_{i} V_{1} \bar{e}_{i} V_{1}(\varphi)-e_{i}\left[V_{1}, \bar{e}_{i}\right] V_{1}(\varphi)-V_{1}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)} V_{1}(\varphi)\right\}+E \\
= & \tilde{g}^{i \bar{i}}\left\{V_{1} e_{i} \bar{e}_{i} V_{1}(\varphi)+\left[e_{i}, V_{1}\right] \bar{e}_{i} V_{1}(\varphi)-\left[V_{1}, \bar{e}_{i}\right] e_{i} V_{1}(\varphi)-V_{1} V_{1}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right\}+E \\
= & \tilde{g}^{i \bar{i}}\left\{V_{1} e_{i} V_{1} \bar{e}_{i}(\varphi)-V_{1} e_{i}\left[V_{1}, \bar{e}_{i}\right](\varphi)+\left[e_{i}, V_{1}\right] \bar{e}_{i} V_{1}(\varphi)-\left[V_{1}, \bar{e}_{i}\right] e_{i} V_{1}(\varphi)\right. \\
& \left.-V_{1} V_{1}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right\}+E \\
= & \tilde{g}^{i \bar{i}}\left\{V_{1} V_{1} e_{i} \bar{e}_{i}(\varphi)-V_{1}\left[V_{1}, e_{i}\right] \bar{e}_{i}(\varphi)-V_{1} e_{i}\left[V_{1}, \bar{e}_{i}\right](\varphi)+\left[e_{i}, V_{1}\right] \bar{e}_{i} V_{1}(\varphi)\right. \\
& \left.-\left[V_{1}, \bar{e}_{i}\right] e_{i} V_{1}(\varphi)-V_{1} V_{1}\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right\}+E \\
= & \tilde{g}^{i \bar{i}} V_{1} V_{1}\left(e_{i} \bar{e}_{i}(\varphi)-\left[e_{i}, \bar{e}_{i}\right]^{(0,1)}(\varphi)\right)-2 \tilde{g}^{i \bar{i}}\left[V_{1}, e_{i}\right] V_{1} \bar{e}_{i}(\varphi)-2 \tilde{g}^{i \bar{i}}\left[V_{1}, \bar{e}_{i}\right] V_{1} e_{i}(\varphi)+E .
\end{aligned}$$
Recalling (4.1), and combining this with (5.16), we obtain (5.12). \(\square\)

We use the above lemma to obtain a lower bound for $L(\hat{Q})$ at $x_{0}$ :
Lemma 5.4. For any $\varepsilon$ with $0<\varepsilon \leqslant 1 / 2$, we have at $x_{0}$,
$$\begin{aligned}
0 \geqslant & L(\hat{Q}) \\
\geqslant & (2-\varepsilon) \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}} \\
& -(1+\varepsilon) \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}+\frac{h^{\prime}}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \\
& +\left.\left.h^{\prime \prime} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2}+\left(A e^{-A \varphi}-\frac{C}{\varepsilon}\right) \sum_{i} \tilde{g}^{i \bar{i}}+A^{2} e^{-A \varphi} \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2} \\
& -A n e^{-A \varphi} .
\end{aligned}$$

Proof. Compute, using Lemma 5.3, Lemma 4.2 and the inequalities (5.4) and (5.9),
$$\begin{aligned}
0 \geqslant & L(\hat{Q}) \\
= & \frac{L\left(\lambda_{1}\right)}{\lambda_{1}}-\frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\lambda_{1}\right)\right|^{2}}{\lambda_{1}^{2}}+h^{\prime} L\left(|\partial \varphi|_{g}^{2}\right)+\left.\left.h^{\prime \prime} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} \\
& -A e^{-A \varphi} L(\varphi)+A^{2} e^{-A \varphi} \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2} \\
\geqslant & 2 \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi V_{\alpha} V_{1}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{\tilde{g}^{p \bar{p}} \tilde{g}^{q \bar{q}}\left|V_{1}\left(\tilde{g}_{p \bar{q}}\right)\right|^{2}}{\lambda_{1}}-\frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}} \\
& -2 \frac{\tilde{g}^{i \bar{i}}\left[V_{1}, e_{i}\right] V_{1} \bar{e}_{i}(\varphi)+\tilde{g}^{i \bar{i}}\left[V_{1}, \bar{e}_{i}\right] V_{1} e_{i}(\varphi)}{\lambda_{1}} \\
& +\frac{h^{\prime}}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right)+\left.\left.h^{\prime \prime} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} \\
& +\left(A e^{-A \varphi}-C\right) \sum_{i} \tilde{g}^{i \bar{i}}+A^{2} e^{-A \varphi} \tilde{g}^{i \bar{i}}\left|e_{i}(\varphi)\right|^{2}-A n e^{-A \varphi} .
\end{aligned}$$
We deal with the bad third order terms on the second line. At $x_{0}$ we can write
$$\left[V_{1}, e_{i}\right]=\sum_{\alpha=1}^{2 n} \nu_{i \alpha} V_{\alpha},$$
for some complex numbers $\nu_{i \alpha}$ which are uniformly bounded, hence
$$\left|\left[V_{1}, e_{i}\right] V_{1} \bar{e}_{i}(\varphi)+\left[V_{1}, \bar{e}_{i}\right] V_{1} e_{i}(\varphi)\right| \leqslant C \sum_{\alpha=1}^{2 n}\left|V_{\alpha} V_{1} e_{i}(\varphi)\right|,$$
and
$$\begin{aligned}
V_{\alpha} V_{1} e_{i}(\varphi) & =e_{i} V_{\alpha} V_{1}(\varphi)+V_{\alpha}\left[V_{1}, e_{i}\right](\varphi)+\left[V_{\alpha}, e_{i}\right] V_{1}(\varphi) \\
& =e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)+e_{i}\left(\nabla_{V_{\alpha}} V_{1}\right)(\varphi)+V_{\alpha}\left[V_{1}, e_{i}\right](\varphi)+\left[V_{\alpha}, e_{i}\right] V_{1}(\varphi),
\end{aligned}$$
and so
$$\begin{aligned}
2 & \frac{\tilde{g}^{i \bar{i}}\left[V_{1}, e_{i}\right] V_{1} \bar{e}_{i}(\varphi)+\tilde{g}^{i \bar{i}}\left[V_{1}, \bar{e}_{i}\right] V_{1} e_{i}(\varphi)}{\lambda_{1}} \\
& \leqslant C \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi V_{1} V_{1}\right)\right|}{\lambda_{1}}+C \sum_{\alpha>1} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|}{\lambda_{1}}+C \sum_{i} \tilde{g}^{i \bar{i}} \\
& \leqslant \varepsilon \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}+\varepsilon \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}}+\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}} \sum_{\alpha>1} \frac{\lambda_{1}-\lambda_{\alpha}}{\lambda_{1}} \\
& \leqslant \varepsilon \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}+\varepsilon \sum_{\alpha>1} \tilde{g}^{i \bar{i}} \frac{\left|e_{i}\left(\varphi_{V_{\alpha} V_{1}}\right)\right|^{2}}{\lambda_{1}\left(\lambda_{1}-\lambda_{\alpha}\right)}+\frac{C}{\varepsilon} \sum_{i} \tilde{g}^{i \bar{i}},
\end{aligned}$$
where we used (5.2). Thus the lemma follows from (5.18). \(\square\)

We need to deal with the "bad" negative term
$$-(1+\varepsilon) \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}$$
in (5.17). We split up into different cases. The constant $\varepsilon>0$ will be different in each case.

Case 1. Assume that, at $x_{0}$,
\begin{itemize}
\item[(a)] $\tilde{g}_{1 \overline{1}}<A^{3} e^{-2 A \varphi} \tilde{g}_{n \bar{n}}$, or
\item[(b)] we have
$$\frac{h^{\prime}}{4} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right)>6\left(\sup _{M}|\partial \varphi|_{g}^{2}\right) A^{2} e^{-2 A \varphi} \sum_{i} \tilde{g}^{i \bar{i}} .$$
\end{itemize}

In this case we just choose $\varepsilon=\frac{1}{2}$. We use the fact that, at $x_{0}$, the first derivative of $\hat{Q}$ vanishes. Hence, using the elementary inequality $|a+b|^{2} \leqslant$ $4|a|^{2}+\frac{4}{3}|b|^{2}$, for $a, b \in \mathbb{C}$,
$$\begin{aligned}
-\frac{3}{2} \frac{\tilde{g}^{i \bar{i}}\left|e_{i}\left(\varphi_{V_{1} V_{1}}\right)\right|^{2}}{\lambda_{1}^{2}}= & -\frac{3}{2} \tilde{g}^{i \bar{i}}\left|A e^{-A \varphi} e_{i}(\varphi)-h^{\prime} e_{i}\left(|\partial \varphi|_{g}^{2}\right)\right|^{2} \\
\geqslant & -6\left(\sup _{M}|\partial \varphi|_{g}^{2}\right) A^{2} e^{-2 A \varphi} \sum_{i} \tilde{g}^{i \bar{i}} \\
& -\left.\left.2\left(h^{\prime}\right)^{2} \tilde{g}^{i \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} .
\end{aligned}$$

Hence from (5.17), discarding some positive terms, we obtain at $x_{0}$,
$$\begin{aligned}
0 \geqslant & -6\left(\sup _{M}|\partial \varphi|_{g}^{2}\right) A^{2} e^{-2 A \varphi} \sum_{i} \tilde{g}^{i \bar{i}}+\left.\left.\left(h^{\prime \prime}-2\left(h^{\prime}\right)^{2}\right) \tilde{g}^{\bar{i} \bar{i}}\left|e_{i}\right| \partial \varphi\right|_{g} ^{2}\right|^{2} \\
& +\frac{h^{\prime}}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right)+\left(A e^{-A \varphi}-C\right) \sum_{i} \tilde{g}^{i \bar{i}}-A n e^{-A \varphi} .
\end{aligned}$$
But from (5.4), we have $h^{\prime \prime}=2\left(h^{\prime}\right)^{2}$. In case (a) note that all the numbers $\tilde{g}_{\bar{i} \bar{i}}, 1 \leqslant i \leqslant n$, are comparable to each other up to a uniform constant (which depends on $A$ ). Using again (5.9), as well as Propositions 3.1 and 4.1, we have
$$0 \geqslant \frac{h^{\prime}}{2} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right)-C_{A} \sum_{i} \tilde{g}^{i \bar{i}},$$
for a uniform constant $C_{A}$ (depending on the uniform constant $A$ ), and since all the $\tilde{g}^{i \bar{i}}$ are comparable to each other this gives
$$\sum_{i, k}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right) \leqslant C_{A} .$$
But at $x_{0}$ we can define the complex covariant derivatives $\varphi_{e_{i} \bar{e}_{k}}$ and $\varphi_{e_{i} e_{k}}$ in the obvious way, which satisfy
$$\varphi_{e_{i} \bar{e}_{k}}-e_{i} \bar{e}_{k}(\varphi)=-\left(\nabla_{e_{i}} \bar{e}_{k}\right)(\varphi), \quad \varphi_{e_{i} e_{k}}-e_{i} e_{k}(\varphi)=-\left(\nabla_{e_{i}} e_{k}\right)(\varphi),$$
and these differences are uniformly bounded thanks to Proposition 4.1. Therefore
$$\sum_{i, k}\left(\left|\varphi_{e_{i} e_{k}}\right|^{2}+\left|\varphi_{e_{i} \bar{e}_{k}}\right|^{2}\right) \leqslant C_{A},$$
and recalling (5.6), we see that
$$\sum_{\alpha, \beta}\left|\nabla_{\alpha \beta}^{2} \varphi\right| \leqslant C_{A},$$
and so $\lambda_{1}\left(x_{0}\right)$ is uniformly bounded. Thanks to Propositions 3.1 and 4.1, this shows that $Q$ is bounded from above at $x_{0}$, and hence everywhere.

On the other hand, in case (b), we obtain
$$0 \geqslant \frac{h^{\prime}}{4} \sum_{k} \tilde{g}^{i \bar{i}}\left(\left|e_{i} e_{k}(\varphi)\right|^{2}+\left|e_{i} \bar{e}_{k}(\varphi)\right|^{2}\right)+\left(A-C_{0}\right) \sum_{i} \tilde{g}^{i \bar{i}}-A n e^{-A \varphi},$$
for a uniform $C_{0}$. Then as long as
$$A \geqslant C_{0}+1,$$
we see that at $x_{0}$ we have $\sum_{i} \tilde{g}^{i \bar{i}} \leqslant C$, and so also
$$\operatorname{tr}_{g} \tilde{g} \leqslant\left(\operatorname{tr}_{\tilde{g}} g\right)^{n-1} \frac{\tilde{\omega}^{n}}{\omega^{n}} \leqslant C .$$
Therefore at $x_{0}$ we have that $\tilde{g}$ is uniformly equivalent to $g$, and (5.24) then shows that (5.21) holds again, and so $Q$ is bounded from above at $x_{0}$. This completes Case 1.

Case 2. Neither (a) nor (b) of Case 1 hold.

This is the difficult case, and it will take up the rest of this section. Let
$$I=\left\{i \in\{1, \ldots, n\} \mid \tilde{g}_{i \bar{i}}\left(x_{0}\right) \geqslant A^{3} e^{-2 A \varphi\left(x_{0}\right)} \tilde{g}_{n \bar{n}}\left(x_{0}\right)\right\} .$$
We have $n \notin I$ (since $A>1$ ), and $1 \in I$ (otherwise we are in part (a) of Case 1). So for example when $n=2$ we have $I=\{1\}$.