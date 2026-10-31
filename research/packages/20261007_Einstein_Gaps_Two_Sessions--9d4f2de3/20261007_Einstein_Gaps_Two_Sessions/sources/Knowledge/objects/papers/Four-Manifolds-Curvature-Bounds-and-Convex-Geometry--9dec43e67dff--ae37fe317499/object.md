# Four-Manifolds, Curvature Bounds, and Convex Geometry

- Category: papers
- Identity: arxiv:math/0611450
- Content status: fulltext_ok

---

---
source_file: math_0611450v1.pdf
converter: mathpix
format: mmd
---

\title{
Four-Manifolds, Curvature Bounds, and Convex Geometry
}

\author{
Claude LeBrun* \\ SUNY Stony Brook
}

November 14, 2006

\section*{1 Introduction}

Seiberg-Witten theory leads to a remarkable family of curvature estimates governing the Riemannian geometry of compact 4-manifolds, and these, for example, imply interesting results concerning the existence and/or uniqueness of Einstein metrics on such spaces. The primary purpose of the present article is to introduce a simplified, user-friendly repackaging of the information conveyed by the Seiberg-Witten equations into a single, easily understood numerical invariant that appears to play the starring rôle in the relevant curvature estimates. In addition, this article contains some new results concerning boundary cases of the curvature estimates that strengthen what was previously known.

The gist of the matter can be summarized as follows. Suppose that $M$ is a smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$. By considering a geometrically rich system of PDE called the Seiberg-Witten equations, one may then define a certain finite subset $\mathfrak{C} \subset H^{2}(M, \mathbb{R})$ that depends only on the orientation and smooth structure of $M$. The elements of $\mathfrak{C}$ are called monopole classes, and are, by definition, the first Chern classes of those spin ${ }^{c}$ structures on $M$ for which the the Seiberg-Witten equations have solutions for all metrics. Now, while the elements of $\mathfrak{C}$ are all integer classes, we wish to focus here on the fact that $\mathfrak{C}$ sits in a real vector space, as this allows us to

\footnotetext{
*Supported in part by NSF grant DMS-0604735
}
consider its convex hull $\boldsymbol{\operatorname { H u l l }}(\mathfrak{C})$. Because $\mathfrak{C}$ is finite, $\boldsymbol{\operatorname { H u l l }}(\mathfrak{C})$ is necessarily compact. We can therefore define a real-valued invariant of $M$ by setting
$$\beta^{2}(M)=\max \left\{\mathbf{v}^{2} \mid \mathbf{v} \in \operatorname{Hull}(\mathfrak{C})\right\}$$
when $\mathfrak{C} \neq \varnothing$, while setting $\beta^{2}(M)=0$ if $\mathfrak{C}=\varnothing$. Here $\mathbf{v}^{2}=\langle\mathbf{v} \smile \mathbf{v},[M]\rangle$ denotes the intersection pairing of a class $\mathbf{v} \in H^{2}(M, \mathbb{R})$ with itself. Because $0 \in \operatorname{Hull}(\mathfrak{C})$ whenever $\mathfrak{C} \neq \varnothing$, one automatically has $\beta^{2}(M) \geq 0$; but, more importantly, there are actually many 4-manifolds $M$ for which $\beta^{2}(M)>0$. It is this last fact that gives the following result most of its interest:

Theorem A Let $M$ be a compact oriented 4 -manifold with $b_{+} \geq 2$. Then any metric $g$ on $M$ satisfies the curvature estimates
$$\begin{aligned}
\int_{M} s^{2} d \mu & \geq 32 \pi^{2} \beta^{2}(M) \\
\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu & \geq 72 \pi^{2} \beta^{2}(M)
\end{aligned}$$
where $s$ and $W_{+}$respectively denote the scalar and Weyl curvatures of $g$. Moreover, if $M$ carries a non-zero monopole class, equality occurs in either (1) or (2) if and only if $g$ is Kähler-Einstein, with negative Einstein constant.

Now, in an important respect, Theorem A is ostensibly weaker than a result that the author has published elsewhere [26]. Indeed, as we shall see below, there is a 'softer' invariant, called $\alpha^{2}(M)$, that can be defined in terms of $\mathfrak{C}(M)$ via a complicated minimax process; and naïve comparison of the definitions of $\alpha^{2}$ and $\beta^{2}$ would lead one merely to expect that
$$\beta^{2}(M) \leq \alpha^{2}(M) \leq b_{+}(M) \beta^{2}(M) .$$
Yet [26] inequalities (1) and (2) can still be shown to hold even when $\beta^{2}(M)$ is replaced by $\alpha^{2}(M)$, yielding an apparently stronger statement. Oddly enough, however, it seems that in practice one consistently has
$$\alpha^{2}(M)=\beta^{2}(M),$$
so that modifying (1) or (2) in this manner effectively seems to yield no added punch. The fact that $\alpha^{2}$ and $\beta^{2}$ typically coincide will only partially be explained here, via some simple results of distinctly limited scope. But the
upshot is that the finite configuration $\mathfrak{C} \subset H^{2}(M, \mathbb{R})$ consistently displays some unanticipated geometrical properties that ought to be understood more precisely.

In yet a different direction, Theorem A contains some essentially new geometric information, because the stated characterization of the equality case of (2) was not previously known. The issue boils down to a problem in almost-Kähler geometry, and is eventually resolved by Theorem 4.10.

Finally, it should be pointed out that the convex hull of the set of monopole classes first appeared in the context of 3-manifold theory, where Kronheimer and Mrowka [20] used it to provide a new characterization of the Thurston norm. Although these earlier results ultimately have little bearing on the ideas developed here, they undoubtedly exerted a powerful subconscious influence on the conceptualization of the present work. The author would therefore like to express his indebtedness to Kronheimer and Mrowka by drawing the reader's attention to their deep and beautiful paper.

\section*{2 Rudiments of 4-Dimensional Geometry}

This article will make frequent reference to a constellation of basic facts regarding 4-dimensional geometry which, though largely familiar to the cognoscenti, would completely confuse the neophyte if left unexplained. For clarity's sake, we will therefore begin with a quick review of the key points.

Many peculiar features of 4-dimensional geometry are directly attributable the fact that the bundle of 2-forms over an oriented Riemannian 4-manifold $(M, g)$ invariantly decomposes as the direct sum
$$\Lambda^{2}=\Lambda^{+} \oplus \Lambda^{-}$$
of the eigenspaces of the Hodge star operator
$$\star: \Lambda^{2} \rightarrow \Lambda^{2} .$$
The sections of $\Lambda^{+}$are called self-dual 2-forms, while the sections of $\Lambda^{-}$are called anti-self-dual 2-forms. The decomposition (3) is, moreover, conformally invariant, in the sense that it is left unchanged if $g$ is multiplied by an arbitrary smooth positive function. An arbitrary 2-form can thus be uniquely expressed as
$$\varphi=\varphi^{+}+\varphi^{-},$$
where $\varphi^{ \pm} \in \Lambda^{ \pm}$, and we then have
$$\varphi \wedge \varphi=\left(\left|\varphi^{+}\right|^{2}-\left|\varphi^{-}\right|^{2}\right) d \mu_{g}$$
where $d \mu_{g}$ denotes the metric volume form associated with the fixed orientation.

The decomposition (3) in turn leads to a decomposition of the Riemann curvature tensor. Indeed, identifying the curvature tensor of $g$ with the selfadjoint linear map
$$\begin{aligned}
\mathcal{R}: \Lambda^{2} & \longrightarrow \Lambda^{2} \\
\varphi_{j k} & \longmapsto \frac{1}{2} \varphi_{\ell m} R^{\ell m}{ }_{j k}
\end{aligned}$$
we obtain a decomposition
$$\mathcal{R}=\left(\begin{array}{c|c}
W_{+}+\frac{s}{12} & \stackrel{\circ}{r} \\
\hline \stackrel{\circ}{r} & W_{-}+\frac{s}{12}
\end{array}\right) .$$
where $W_{+}+\frac{s}{12}: \Lambda^{+} \rightarrow \Lambda^{+}$, etc. Here $W_{+}$is the trace-free piece of its block, and is the called the self-dual Weyl curvature of $(M, g)$; the anti-selfdual Weyl curvature $W_{-}$is defined analogously. Both of the objects are conformally invariant, in the sense that the tensors $\left(W_{ \pm}\right)^{j}{ }_{k \ell m}$ both remain unaltered if $g$ is multiplied by any smooth positive function. Note that the scalar curvature $s$ is understood to act in (4) by scalar multiplication, while the trace-free Ricci curvature $\stackrel{\circ}{r}_{j k}=R^{\ell}{ }_{j \ell k}-\frac{s}{4} g_{j k}$ acts on 2-forms by
$$\varphi_{j k} \mapsto \stackrel{\circ}{r}_{\ell j} \varphi^{\ell}{ }_{k j} .$$

Next, let us suppose that $(M, g)$ is a compact oriented Riemannian 4manifold. The Hodge theorem then tells us that every de Rham class on $M$ has a unique harmonic representative. In particular, we therefore have a canonical identification
$$H^{2}(M, \mathbb{R})=\left\{\varphi \in \Gamma\left(\Lambda^{2}\right) \mid d \varphi=0, d \star \varphi=0\right\} .$$

However, the Hodge star operator ★ defines an involution of the right-hand side, giving rise to an eigenspace decomposition
$$H^{2}(M, \mathbb{R})=\mathcal{H}_{g}^{+} \oplus \mathcal{H}_{g}^{-},$$
where
$$\mathcal{H}_{g}^{ \pm}=\left\{\varphi \in \Gamma\left(\Lambda^{ \pm}\right) \mid d \varphi=0\right\}$$
are the spaces of self-dual and anti-self-dual harmonic forms. The intersection form
$$\begin{array}{clc}
H^{2}(M, \mathbb{R}) \times H^{2}(M, \mathbb{R}) & \longrightarrow & \mathbb{R} \\
(\mathbf{b}, \mathbf{c}) & \longmapsto \mathbf{b} \cdot \mathbf{c}:=\langle\mathbf{b} \smile \mathbf{c},[M]\rangle
\end{array}$$
becomes positive-definite when restricted to $\mathcal{H}_{g}^{+}$, and negative-definite when restricted to $\mathcal{H}_{g}^{-}$. Moreover, these two subspaces are mutually orthogonal with respect to the intersection form. The numbers $b_{ \pm}(M)=\operatorname{dim} \mathcal{H}_{g}^{ \pm}$are therefore oriented homotopy invariants of $M$. Their difference
$$\tau(M)=b_{+}(M)-b_{-}(M)$$
is called the signature of $M$. By the Hirzebruch Signature Theorem, it coincides with $\left\langle\frac{1}{3} p_{1}(T M),[M]\right\rangle$, and so can be expressed as a curvature integral
$$\tau(M)=\frac{1}{12 \pi^{2}} \int_{M}\left(\left|W^{+}\right|^{2}-\left|W^{-}\right|^{2}\right) d \mu$$
for any Riemannian metric $g$ on $M$. This, of course, is analogous to the generalized Gauss-Bonnet formula
$$\chi(M)=\frac{1}{8 \pi^{2}} \int_{M}\left(\frac{s^{2}}{24}+\left|W^{+}\right|^{2}+\left|W^{-}\right|^{2}-\frac{|\stackrel{\circ}{r}|^{2}}{2}\right) d \mu$$
for the Euler characteristic.
Lemma 2.1 Let $\psi$ be a closed 2-form on a compact oriented Riemannian 4 -manifold $(M, g)$. Let $\mathbf{v}=[\psi]$ denote the de Rham class of $\psi$, and use (5) to write
$$\mathbf{v}=\mathbf{v}^{+}+\mathbf{v}^{-}$$
where $\mathbf{v}^{ \pm} \in \mathcal{H}_{g}^{ \pm}$. Then
$$\int_{M}\left|\psi^{+}\right|^{2} d \mu_{g} \geq\left(\mathbf{v}^{+}\right)^{2}$$
with equality iff $\psi^{+}$is a harmonic form.

Proof. Let $\phi$ be the unique harmonic form cohomologous to $\psi$. Since $\phi$ is then the de Rham representative of v of minimal $L^{2}$-norm, we therefore have
$$\int_{M}\left(\left|\psi^{+}\right|^{2}+\left|\psi^{-}\right|^{2}\right) d \mu \geq \int_{M}\left(\left|\phi^{+}\right|^{2}+\left|\phi^{-}\right|^{2}\right) d \mu$$
with equality iff $\psi=\phi$. However,
$$\int_{M}\left(\left|\psi^{+}\right|^{2}-\left|\psi^{-}\right|^{2}\right) d \mu=\int_{M}\left(\left|\phi^{+}\right|^{2}-\left|\phi^{-}\right|^{2}\right) d \mu$$
since $\int \psi \wedge \psi=\int \phi \wedge \phi$ by Stokes' theorem. Averaging these expressions, we therefore have
$$\int_{M}\left|\psi^{+}\right|^{2} d \mu \geq \int_{M}\left|\phi^{+}\right|^{2} d \mu=\int_{M} \phi^{+} \wedge \phi^{+}=\left(\mathbf{v}^{+}\right)^{2}$$
with equality iff $\psi^{+}=(\psi+\star \psi) / 2$ is closed. \(\square\)

When using this result, it is important to remember that the decomposition (5) depends on the metric $g$, as consequently does the number $\left(\mathbf{v}^{+}\right)^{2}$. This makes it vital to better understand the natural map
$$\begin{aligned}
\{\text { metrics on } M\} & \longrightarrow G r_{b_{+}}^{+}\left[H^{2}(M, \mathbb{R})\right] \\
g & \longmapsto \mathcal{H}_{g}^{+}
\end{aligned}$$
from the infinite-dimensional space of all metrics to the finite-dimensional Grassmannian of $b_{+}(M)$-dimensional subspaces of $H^{2}(M, \mathbb{R})$ on which the intersection form is positive-definite. This map is called the period map of $M$. It is easily seen to be invariant under both conformal rescaling and the identity component $\operatorname{Diff}_{0}(M)$ of the diffeomorphism group. A beautiful result of Donaldson [9, p. 336] asserts that the period map is not only smooth, but is actually transverse to the set of planes containing any given element of positive self-intersection. This has the following useful consequence:

Proposition 2.2 (Donaldson) Let $(M, g)$ be any smooth compact oriented 4-manifold with $b_{+}(M) \geq 1$, and let $\mathbf{b} \in \mathcal{H}_{g}^{+} \subset H^{2}(M, \mathbb{R})$ be the de Rham class of any non-zero harmonic self-dual 2-form on $(M, g)$. Then there is a smooth family of Riemannian metrics $g_{\mathbf{t}}, \mathbf{t} \in B_{\varepsilon}(\mathbf{0}) \subset \mathcal{H}_{g}^{-}$, with $g_{\mathbf{0}}=g$, such that $(\mathbf{b}+\mathbf{t}) \in \mathcal{H}_{g_{\mathbf{t}}}^{+}$for each and every $\mathbf{t}$.

As the above discussion makes clear, the Hodge Laplacian
$$\Delta_{d}=d d^{*}+d^{*} d=-\star d \star d-d \star d \star$$
is an operator of fundamental geometric importance. It is thus worth pointing out that if $\psi$ is a self-dual 2-form, then $\Delta_{d} \psi$ is also self-dual, and can, moreover, be re-expressed by means of the Weitzenböck formula [8]
$$\Delta_{d} \psi=\nabla^{*} \nabla \psi-2 W_{+}(\psi, \cdot)+\frac{s}{3} \psi .$$
Taking the $L^{2}$ inner product with $\psi$, we therefore have
$$\int_{M}\left(|\nabla \psi|^{2}-2 W_{+}(\psi, \psi)+\frac{s}{3}|\psi|^{2}\right) d \mu \geq 0$$
since $\Delta_{d}$ is a non-negative operator. On the other hand, since $W_{+}: \Lambda^{+} \rightarrow \Lambda^{+}$ is self-adjoint and trace-free,
$$\left|W_{+}(\psi, \psi)\right| \leq \sqrt{\frac{2}{3}}\left|W_{+} \| \psi\right|^{2},$$
so it follows that any self-dual 2-form $\psi$ satisfies
$$\int_{M}|\nabla \psi|^{2} d \mu \geq \int_{M}\left(-2 \sqrt{\frac{2}{3}}\left|W_{+}\right|-\frac{s}{3}\right)|\psi|^{2} d \mu$$
Moreover, assuming that $\psi \not \equiv 0$, equality holds iff $\psi$ is closed, belongs the lowest eigenspace of $W_{+}$at each point, and the two largest eigenvalues of $W_{+}$ are everywhere equal. Of course, this last assertion crucially depends on the fact [1, 3] that if $\Delta_{d} \psi=0$ and $\psi \not \equiv 0$, then $\psi \neq 0$ on a dense subset of $M$.

A rather special set of techniques can be applied when $(M, g)$ happens to admit a closed self-dual 2-form $\omega \in \mathcal{H}_{g}^{+}$with constant point-wise norm $|\omega|_{g} \equiv \sqrt{2}$. In this case, there is an almost-complex structure $J: T M \rightarrow T M$, $J^{2}=1$, defined by
$$g(J \cdot, \cdot)=\omega(\cdot, \cdot),$$
and this almost-complex structure then acts on $T M$ in a $g$-preserving fashion. The triple $(M, g, \omega)$ is then said to be an almost-Kähler 4-manifold. Because $J$ allows one to to think of $T M$ as a complex vector bundle, it is only natural
to look for a connection on its anti-canonical line bundle $L=\wedge^{2} T_{J}^{1,0} \cong \Lambda_{J}^{0,2}$ in order to use the Chern-Weil theorem in order to express $c_{1}^{\mathbb{R}}(M, J)$ as
$$c_{1}^{\mathbb{R}}(L)=\left[\frac{i}{2 \pi} F\right] \in H_{D R}^{2}(M, \mathbb{R}),$$
where $F$ is the curvature of the relevant connection on $L$. A particular choice of Hermitian connection on $L$ was first introduced by Blair [7], and is so geometrically natural that it was later rediscovered by Taubes [30] for entirely different reasons. The curvature $F_{B}=F_{B}^{+}+F_{B}^{-}$of this Blair connection is given [10, 27] by
$$\begin{aligned}
i F_{B}^{+} & =\frac{s+s^{*}}{8} \omega+W^{+}(\omega)^{\perp} \\
i F_{B}^{-} & =\frac{s-s^{\star}}{8} \hat{\omega}+\stackrel{\circ}{\varrho}
\end{aligned}$$
where the so-called star-scalar curvature is given by
$$s^{*}=s+|\nabla \omega|^{2}=2 W_{+}(\omega, \omega)+\frac{s}{3},$$
while $W^{+}(\omega)^{\perp}$ is the component of $W^{+}(\omega)$ orthogonal to $\omega$,
$$\stackrel{\circ}{\varrho}(\cdot, J \cdot)=\frac{\stackrel{\circ}{r}+J^{*} \stackrel{\circ}{r}}{2},$$
and where the anti-self-dual 2-form $\hat{\omega} \in \Lambda^{-}$is defined only on the open set where $s^{\star}-s \neq 0$, and satisfies $|\hat{\omega}| \equiv \sqrt{2}$.

An important special case occurs when $\nabla \omega=0$. This happens precisely when $J$ is integrable, and $g$ is a Kähler metric on the complex surface $(M, J)$. In this case, $s=s^{*}, \omega$ is an eigenvector of the $W_{+}$, and $r$ is $J$-invariant, so that $i F_{B}$ just becomes the Ricci form $\rho$ defined by $\rho(\cdot, \cdot)=r(J \cdot, \cdot)$. In fact, $\omega$ is an eigenvector of $W_{+}$with eigenvalue $s / 6$, whereas the elements of $\omega^{\perp}=\Re e \Lambda_{J}^{2,0}$ are eigenvectors of eigenvalue $-s / 12$.

Kähler manifolds with scalar curvature $s=$ const $<0$ will play an important rôle in this paper. By the above discussion, they belong to the following broader class of almost-Kähler manifolds:

Definition 2.3 An almost-Kähler 4-manifold ( $M^{4}, g, \omega$ ) will be said to be saturated if
\begin{itemize}
\item[-] $s+s^{*}$ is a negative constant;
\item[-] $\omega$ belongs to the lowest eigenspace of $W_{+}: \Lambda^{+} \rightarrow \Lambda^{+}$everywhere; and
\item[-] the two largest eigenvalues of $W_{+}: \Lambda^{+} \rightarrow \Lambda^{+}$are everywhere equal.
\end{itemize}

\section*{3 The Seiberg-Witten Equations}

This section is intended both to fix our terminological conventions and to provide streamlined proofs of the key preliminary curvature estimates. We note that, while all the main results in this section can be found elsewhere [16, 24, 25, 26], several of the proofs given here are considerably simpler than those published heretofore.

We begin with a discussion of spin ${ }^{c}$ structures. If $M$ is any smooth oriented 4-manifold, its second Stieffel-Whitney class $w_{2}(T M) \in H^{2}\left(M, \mathbb{Z}_{2}\right)$ is always [14, 17] in the image of the natural homomorphism
$$H^{2}(M, \mathbb{Z}) \rightarrow H^{2}\left(M, \mathbb{Z}_{2}\right),$$
and we can therefore always find Hermitian line bundles $L \rightarrow M$ such that
$$c_{1}(L) \equiv w_{2}(T M) \bmod 2 .$$
For any such $L$, and for any Riemannian metric $g$ on $M$, one can then find rank-2 Hermitian vector bundles $\mathbb{V}_{ \pm}$which formally satisfy
$$\mathbb{V}_{ \pm}=\mathbb{S}_{ \pm} \otimes L^{1 / 2}$$
where $\mathbb{S}_{ \pm}$are the locally defined left- and right-handed spinor bundles of $(M, g)$. Such a choice of $\mathbb{V}_{ \pm}$, up to isomorphism, is called a spin ${ }^{c}$ structure $\mathfrak{c}$ on $M$. Moreover, if $H_{1}(M, \mathbb{Z})$ does not contain elements of order 2, then $\mathfrak{c}$ is completely determined by
$$c_{1}(L)=c_{1}\left(\mathbb{V}_{ \pm}\right) \in H^{2}(M, \mathbb{Z}),$$
which is called the first Chern class of the spin ${ }^{c}$ structure $\mathfrak{c}$.
Every unitary connection $A$ on $L$ induces a connection
$$\nabla_{A}: \Gamma\left(\mathbb{V}_{+}\right) \rightarrow \Gamma\left(\Lambda^{1} \otimes \mathbb{V}_{+}\right),$$
and composition of this with the natural Clifford multiplication homomorphism
$$\Lambda^{1} \otimes \mathbb{V}_{+} \rightarrow \mathbb{V}_{-}$$
gives one a spin ${ }^{c}$ version
$$D_{A}: \Gamma\left(\mathbb{V}_{+}\right) \rightarrow \Gamma\left(\mathbb{V}_{-}\right)$$
of the Dirac operator [15, 21]. This is an elliptic first-order differential operator, and in many respects it closely resembles the usual Dirac operator of spin geometry. In particular, one has the so-called Weitzenböck formula
$$\left\langle\Phi, D_{A}^{*} D_{A} \Phi\right\rangle=\frac{1}{2} \Delta|\Phi|^{2}+\left|\nabla_{A} \Phi\right|^{2}+\frac{s}{4}|\Phi|^{2}+2\left\langle-i F_{A}^{+}, \sigma(\Phi)\right\rangle$$
for any $\Phi \in \Gamma\left(\mathbb{V}_{+}\right)$, where $F_{A}^{+}$is the self-dual part of the curvature of $A$, and where $\sigma: \mathbb{V}_{+} \rightarrow \Lambda^{+}$is a natural real-quadratic map satisfying
$$|\sigma(\Phi)|=\frac{1}{2 \sqrt{2}}|\Phi|^{2} .$$

Equation (12) is a natural generalization of the Weitzenböck formula used by Lichnerowicz [28] to prove that metrics with $s>0$ cannot exist when $M$ is spin and $\tau(M) \neq 0$. Unfortunately, however, one cannot hope to derive interesting geometric information about the Riemannian metric $g$ by just using (12) for an arbitrary connection $A$, since one would have no control at all over the $F_{A}^{+}$term. Witten [31], however, had the brilliant insight that one could remedy this by considering both $\Phi$ and $A$ as unknowns, subject to the Seiberg-Witten equations
$$\begin{aligned}
D_{A} \Phi & =0 \\
-i F_{A}^{+} & =\sigma(\Phi) .
\end{aligned}$$
These equations are non-linear, but they become an elliptic first-order system once one imposes the 'gauge-fixing' condition
$$d^{*}\left(A-A_{0}\right)=0,$$
where $A_{0}$ is an arbitrary 'background" connection on $L$, and $i\left(A-A_{0}\right)$ is simply treated as a real-valued 1-form on $M$. The eliminate the natural action of the 'gauge group' of automorphisms of the Hermitian line bundle $L \rightarrow M$.

Because the Seiberg-Witten equations are non-linear, one cannot use something like an index formula to predict that they must have solutions. Nonetheless, there exist spin ${ }^{c}$ structures on many 4-manifolds for which there is at least one solution for every metric $g$. This situation is conveniently described by the following terminology [19]:

Definition 3.1 Let $M$ be a smooth compact oriented 4-manifold with $b_{+} \geq 2$. An element $\mathbf{a} \in H^{2}(M, \mathbb{R})$ is called a monopole class of $M$ iff there exists a spin ${ }^{c}$ structure $\mathfrak{c}$ on $M$ with
$$c_{1}^{\mathbb{R}}(L)=\mathbf{a}$$
for which the Seiberg-Witten equations (13-14) have a solution for every Riemannian metric $g$ on $M$.

When the gauge-fixing condition (15) is imposed, the Seiberg-Witten equations amount to saying that $(\Phi, A)$ belongs to the pre-image of zero for a Fredholm map of Banach spaces. This so-called monopole map turns out to behave roughly like a proper map of finite-dimensional spaces [5]. When the 'expected dimension' of the moduli space of solutions modulo gauge equivalence, as determined by the Fredholm index of the monopole map, is zero, Witten [31] discovered that one can define an invariant analogous to the degree of a map between finite-dimensional manifolds of the same dimension. More recently, Bauer and Furuta [5, 4] discovered that the monopole map determines a well-defined class in an equivariant cohomotopy group. Either of these invariants can be used [16] to detect the presence of a monople class. Moreover, these invariants are often non-trivial; for example, a celebrated result of Taubes [30] shows that if $(M, \omega)$ is a symplectic 4-manifold with $b_{+} \geq 2$, then Witten's invariant is non-zero for the spin ${ }^{c}$ structure canoncially detemined by $\omega$, so that $\pm c_{1}(M, \omega)$ are both monopole classes. On the other hand, Kronheimer [19] has has used the Floer homology of 3-manifolds to show that some 4-manifolds admit monopole classes which are not detected by these invariants.

Equations (13-14) are precisely chosen so as to imply the Weitzenböck formula
$$0=2 \Delta|\Phi|^{2}+4\left|\nabla_{A} \Phi\right|^{2}+s|\Phi|^{2}+|\Phi|^{4} .$$
In particular, these Seiberg-Witten equations can never admit a solution $(\Phi, A)$ with $\Phi \not \equiv 0$ relative to a metric $g$ with $s>0$. This leads, in particular, to a cornucopia of simply connected non-spin 4-manifolds which do not admit positive-scalar-curvature metrics - in complete contrast to the situation in higher dimensions [13]. Even more strikingly, the Seiberg-Witten equations actually imply integral estimates for the scalar curvature [31, 23]:

Proposition 3.2 Let $(M, g)$ be a smooth compact oriented Riemannian manifold, and let $\mathbf{a} \in H^{2}(M, \mathbb{R})$ be a monopole class of $M$. Then the scalar curvature $s$ of $g$ satisfies
$$\int_{M} s^{2} d \mu_{g} \geq 32 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
If $\mathbf{a}^{+} \neq 0$, moreover, equality occurs iff there is an integrable complex structure $J$ with $c_{1}^{\mathbb{R}}(M, J)=\mathbf{a}$ such that $(M, g, J)$ is a Kähler manifold of constant negative scalar curvature.

Proof. By Definition 3.1, there must be a spin ${ }^{c}$ structure with $c_{1}^{\mathbb{R}}(L)=\mathbf{a}$ for which the Seiberg-Witen equations (13-14) have a solution $(\Phi, A)$ on $(M, g)$. However, given such a solution, $\Phi$ satisfies the Weitzenböck formula (16) with respect to $g$ and $A$, and integrating this then reveals that
$$0=\int\left[4\left|\nabla_{A} \Phi\right|^{2}+s|\Phi|^{2}+|\Phi|^{4}\right] d \mu$$
Hence
$$\int(-s)|\Phi|^{2} d \mu \geq \int|\Phi|^{4} d \mu$$
and applying the Cauchy-Schwarz inequality to the left-hand side yields
$$\left(\int s^{2} d \mu\right)^{1 / 2}\left(\int|\Phi|^{4} d \mu\right)^{1 / 2} \geq \int|\Phi|^{4} d \mu$$
Equation (14) therefore tells us that
$$\int s^{2} d \mu \geq \int|\Phi|^{4} d \mu=8 \int\left|F_{A}^{+}\right|^{2} d \mu$$
However, since $i F_{A} / 2 \pi$ represents a in de Rham cohomology, Lemma 2.1 tells us that
$$\int\left|F_{A}^{+}\right|^{2} d \mu \geq 4 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
It follows that
$$\int s^{2} d \mu \geq 32 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
exactly as claimed.

If equality holds, the inequalities in the above argument must all be equalities. Hence $\nabla_{A} \Phi=0$, and $i F_{A}^{+}=-\sigma(\Phi)$ is therefore a parallel self-dual 2-form with de Rham class $2 \pi \mathbf{a}^{+}$. When this cohomology class is non-zero, this form cannot vanish, and we therefore conclude that $(M, g)$ is Kähler. Inspection of (16) then reveals that $s$ must be a negative constant. Moreover, $\Phi \otimes \Phi$ is then a non-zero section of $\Lambda^{2,0} \otimes L$ with respect to the relevant complex structure, so $c_{1}^{\mathbb{R}}(M, J)=c_{1}^{\mathbb{R}}(L)=\mathbf{a}$. Conversely, any such Kähler metric would saturate the inequality because the self-dual part of the Ricci form of any Kähler metric on a Kähler surface is $s \omega / 4$, where $\omega=g(J \cdot, \cdot)$ is the Kähler form. \(\square\)

Proposition 3.3 Let $M$ be a compact oriented 4-manifold with $b_{+}(M) \geq 2$. If there is a non-zero monopole class $\mathbf{a} \in H^{2}(M, \mathbb{R})-\{\mathbf{0}\}$, then $M$ does not admit metrics of scalar curvature $s \geq 0$.

Proof. Let $M$ be a smooth compact 4-manifold with $b_{+}(M) \geq 2$, and suppose that $\mathbf{a} \in H^{2}(M, \mathbb{R})-\mathbf{0}$ is a non-zero monopole class. By definition, this means that here is a spin ${ }^{c}$ structure on $M$ with $c_{1}^{\mathbb{R}}(L)=\mathbf{a}$ for which the Seiberg-Witten equations have some solution $(\Phi, A)$ with respect to any metric $g$ on $M$. But if the metric in question has $s \geq 0$, the Weitzenböck formula (16) says that
$$0=2 \Delta|\Phi|^{2}+\left|\nabla_{A} \Phi\right|^{2}+s|\Phi|^{2}+|\Phi|^{4}$$
so that $s \geq 0$ implies that
$$0 \geq \int|\Phi|^{4} d \mu_{g}$$
and we therefore have $\Phi \equiv 0$. But this implies that $F_{A}^{+}=i \sigma(\Phi) \equiv 0$, too, so that $\mathbf{a}=\left[\frac{i}{2 \pi} F_{A}\right] \in \mathcal{H}_{g}^{-}$. In particular, if $g$ has scalar curvature $s \geq 0$ and if $\mathbf{b} \in \mathcal{H}_{g}^{+}$, then $\mathbf{a} \cdot \mathbf{b}=0$.

Next, suppose that we had some metric $g$ on $M$ with strictly positive scalar curvature $s>0$. Choose some $\mathbf{b} \in \mathcal{H}_{g}^{+}$with $\mathbf{b}^{2}=1$. The argument in the previous paragraph tells us that $\mathbf{a} \in \mathcal{H}_{g}^{-}$, so that the integer class $\mathbf{a} \neq \mathbf{0}$ must satisfy $\mathbf{a}^{2} \leq-1$. However, Proposition 2.2 now tells us we can now find a smooth 1-parameter family of metrics $g_{t}, t \in(-\varepsilon, \varepsilon)$, such that $g_{0}=g$, and such that $\mathbf{b}+t \mathbf{a} \in \mathcal{H}_{g_{t}}^{+}$for all $t$. Since we have assumed that $g$ has $s>0$, the same is necessarily true of all the metrics $g_{t}$ for sufficiently small $t$, and
we thus certainly have a contradiction, since the argument of the previous paragraph would now tell us that $\mathbf{a} \cdot(\mathbf{b}+t \mathbf{a})=t \mathbf{a}^{2}$ would have to vanish for all small values of $t$. It follows that $M$ cannot admit any metrics of positive scalar curvature.

Finally, let us suppose instead that $g$ is a metric on $M$ with $s \geq 0$. Since $M$ is now known not to admit metrics of positive scalar curvature, $g$ must then have $s \equiv 0$, since otherwise [2, 6] we would be able to produce a metric of strictly positive scalar curvature by conformally rescaling it. We may now proceed much as in the previous case. Once again, $s \equiv 0$ implies that $\mathbf{a} \in \mathcal{H}_{g}^{-}$. Again, choose some $\mathbf{b} \in \mathcal{H}_{g}^{+}$with $\mathbf{b}^{2}=1$, and observe that, once again, there exists a family of metrics $g_{t}, t \in(-\varepsilon, \varepsilon)$ with $g_{0}=g$ for which $\mathbf{b}+t \mathbf{a} \in \mathcal{H}_{g_{t}}^{+}$. But this time, we invoke a theorem of Koiso [6, 18] on the Yamabe problem with parameters, and thereby construct a smooth family of constant-scalar-curvature, unit-volume metrics $\tilde{g}_{t}$ by conformally rescaling each $g_{t}$. The conformal invariance of (3) then tells us that we still have $\mathbf{b}+t \mathbf{a} \in \mathcal{H}_{\tilde{g}_{t}}^{+}$. Since the family $\tilde{g}_{t}$ is smooth, the value $s_{\tilde{g}_{t}}$ of its scalar curvature is therefore a smooth function of $t$. But since $M$ does not admit metrics of positive scalar curvature, and since $s_{\tilde{g}_{0}}=0$, this smooth function must have a maximum at $t=0$. Hence there is a positive constant $C$ such that
$$0 \geq s_{\tilde{g}_{t}} \geq-C t^{2}$$
for all sufficiently small $t$, and we therefore have
$$C t^{4} \geq s_{\tilde{g}_{t}}^{2}=\int_{M} s_{\tilde{g}_{t}}^{2} d \mu_{\tilde{g}_{t}}$$
for $t$ in the same range. However, Proposition 3.2 and the Cauchy-Schwarz inequality tell us that
$$\int_{M} s_{\tilde{g}_{t}}^{2} d \mu_{\tilde{g}_{t}} \geq 32 \pi^{2}\left(\mathbf{a}_{\tilde{g}_{t}}^{+}\right)^{2} \geq 32 \pi^{2} \frac{[\mathbf{a} \cdot(\mathbf{b}+t \mathbf{a})]^{2}}{(\mathbf{b}+t \mathbf{a})^{2}}=32 \pi^{2} \frac{t^{2}\left|\mathbf{a}^{2}\right|^{2}}{1-t^{2}\left|\mathbf{a}^{2}\right|} \geq 32 \pi^{2} t^{2}$$
so we conclude that (const) $t^{4} \geq t^{2}$ for all small $t$, which is certainly a contradiction. Thus no metric with $s \geq 0$ can exist, and we are done. \(\square\)

Definition 3.4 For any smooth compact oriented 4-manifold $M$ with $b_{+} \geq$ 2, we set
$$\mathfrak{C}(M)=\left\{\text { monopole classes } \mathbf{a} \in H^{2}(M, \mathbb{R})\right\} .$$
We will often abbreviate $\mathfrak{C}(M)$ as $\mathfrak{C}$ when no confusion seems likely to result.

Lemma 3.5 For any smooth compact oriented 4-manifold $M$ with $b_{+} \geq 2$,
$$\mathfrak{C}(M)=-\mathfrak{C}(M) .$$
That is, $\mathbf{a} \in H^{2}(M, \mathbb{R})$ is a monopole class iff $-\mathbf{a} \in H^{2}(M, \mathbb{R})$ is a monopole class, too.

Proof. Let $g$ be any metric on $M$, and let $\mathbb{V}_{ \pm}$be the twisted spin bundles of some spin ${ }^{c}$ structure $\mathfrak{c}$. Then the conjugate vector bundles $\overline{\mathbb{V}}_{ \pm}$are the twisted spin bundles of a second spin ${ }^{c}$ structure $\overline{\mathfrak{c}}$, since we have natural isomorphisms
$$\overline{\mathbb{V}}_{ \pm} \cong \mathbb{V}_{ \pm} \otimes L^{-1}, \quad L=\operatorname{det}\left(\mathbb{V}_{ \pm}\right)$$
induced by the wedge and inner products. Since we locally have
$$\begin{aligned}
& \mathbb{V}_{ \pm}=\mathbb{S}_{ \pm} \otimes L^{1 / 2} \\
& \overline{\mathbb{V}}_{ \pm}=\mathbb{S}_{ \pm} \otimes L^{-1 / 2}
\end{aligned}$$
as bundles with connection, it follows that
$$\overline{D_{A} \Phi}=D_{\bar{A}} \bar{\Phi}$$
for any $\Phi \in \Gamma\left(\mathbb{V}_{+}\right)$and any Hermitian connection $A$ on $L$, where $\bar{A}$ denotes the dual connection on $L^{-1}$ induced by $A$. Moreover, since the associated anti-linear map
$$\mathbb{S}_{+} \rightarrow \mathbb{S}_{+}$$
acts by multiplying by the quaternion $j$, we also have
$$\sigma(\bar{\Phi})=-\sigma(\Phi) .$$
Since $F_{A *}=-F_{A}$, it follows that if $(\Phi, A)$ is a solution of (13-14) with respect to $(g, \mathfrak{c})$, then $(\bar{\Phi}, \bar{A})$ is a solution of (13-14) with respect to $(g, \overline{\mathfrak{c}})$. If, for every metric $g$ on $M$, there is a solution of the Seiberg-Witten equations for the spin ${ }^{c}$ structure $\mathfrak{c}$, the same is therefore also true of $\overline{\mathfrak{c}}$. Since $c_{1}(\overline{\mathfrak{c}})=c_{1}\left(\overline{\mathbb{V}}_{+}\right)=-c_{1}\left(\mathbb{V}_{+}\right)=-c_{1}(\mathfrak{c})$, it follows that the set of monopole classes is invariant under multiplication by -1. \(\square\)

A particularly important consequence of Proposition 3.2 is the following fundamental fact [16]:

Proposition 3.6 Let $M$ be any smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$. Then $\mathfrak{C}(M)$ is a finite set.

Proof. First, observe that one can always find a basis $\left\{e_{j} \mid j=1, \ldots, b_{2}\right\}$ for $H^{2}(M, \mathbb{R})$, together with a collection of metrics $g_{j}$ such that $e_{j} \in \mathcal{H}_{g_{j}}^{+}$. Indeed, let $g=g_{1}=\ldots=g_{b_{+}}$be any metric, let $e_{1}, \ldots, e_{b_{+}}$to be any basis for $\mathcal{H}_{g}^{+}$, and let $e_{b_{+}+1}, \ldots, e_{b_{2}}$ then be small perturbations of $e_{1}$ by linearly independent elements of $\mathcal{H}_{g}^{-}$, while using Proposition 2.2 to find compatible metrics $g_{b_{+}+1}, \ldots, g_{b_{2}}$. Alternatively, one can simply take the $e_{j}$ to be any collection of rational classes with $e_{j}^{2}>0$ which span $H^{2}(M, \mathbb{R})$, and then cite a remarkable recent construction of Gay and Kirby [11, Theorem 1], which shows that any rational cohomology class with positive self-intersection can be be represented by a closed 2-form which is self-dual with respect to some metric. Given this data, we now introduce a constant for each $j$ by setting
$$\kappa_{j}=\left(\frac{e_{j}^{2}}{32 \pi^{2}} \int_{M} s_{g_{j}}^{2} d \mu_{g_{j}}\right)^{1 / 2}$$

Let $L_{j}: H^{2}(M, \mathbb{R}) \rightarrow \mathbb{R}$ be the linear functionals $L_{j}(x)=e_{j} \cdot x$. Since the intersection form is positive-definite on each $\mathcal{H}_{g_{j}}^{+}$, the Cauchy-Schwarz inequality and Proposition 3.2 together imply that any monopole class $\mathbf{a} \in$ $H^{2}(M, \mathbb{R})$ must satisfy
$$\left|L_{j}(\mathbf{a})\right|=\left|e_{j} \cdot \mathbf{a}\right|=\left|e_{j} \cdot \mathbf{a}_{g_{j}}^{+}\right| \leq \sqrt{e_{j}^{2}} \sqrt{\left(\mathbf{a}^{+}\right)^{2}} \leq \kappa_{j}$$
for each $j$. Hence $\mathfrak{C} \subset H^{2}(M, \mathbb{R})$ is contained in the parallelepiped
$$\left\{x \in H^{2}(M, \mathbb{R})| | L_{j}(x) \mid \leq \kappa_{j} \forall j=1, \ldots, b_{2}(M)\right\},$$
which is a compact set. But $\mathfrak{C} \subset H^{2}(M, \mathbb{Z}) /$ torsion, and is therefore also discrete. Hence $\mathfrak{C}$ is finite, as claimed. \(\square\)

We now introduce a generalization of the Seiberg-Witten equations. Let $(M, g)$ be a smooth oriented Riemannian 4-manifold, let $\mathfrak{c}$ be a spin ${ }^{c}$-structure on $M$, and let $f: M \rightarrow \mathbb{R}^{+}$be a smooth positive function. Then we will say that $(\Phi, A)$ solves the rescaled Seiberg-Witten equations if
$$\begin{aligned}
D_{A} \Phi & =0 \\
-i F_{A}^{+} & =f \sigma(\Phi)
\end{aligned}$$

Lemma 3.7 Let $M$ be a smooth compact 4-manifold with $b_{+} \geq 2$, and let $\mathbf{a} \in H^{2}(M, \mathbb{R})$ be a monopole class. Then, for any smooth metric $g$ and any smooth positive function $f$, there is a solution of the rescaled Seiberg-Witten equations (17-18) for some spin ${ }^{c}$ structure on $M$ with $c_{1}^{\mathbb{R}}(L)=\mathbf{a}$.

Proof. Consider the conformally related metric $\hat{g}=f^{-2} g$. Because a is a monopole class, there must then be a solution $(\hat{\Phi}, A)$ of the Seiberg-Witten equations wtih respect to $\hat{g}$ and some spin ${ }^{c}$ structure with $c_{1}^{\mathbb{R}}(L)=\mathbf{a}$. However, the Dirac equation (13) is conformally invariant. More precisely, $\hat{\Phi}$ uniquely determines [21, 29] a solution $\Phi$ of (13) with respect to $g$, such that $|\Phi|_{g}=f^{-3 / 2}|\hat{\Phi}|_{\hat{g}}$, and such that $\sigma_{g}(\Phi)=f^{-1} \sigma_{\hat{g}}(\hat{\Phi})$. Hence $(\Phi, A)$ satisfies (17-18) with respect to $g$. \(\square\)

Given a solution $(\hat{\Phi}, A)$ of (17-18), substitution into (12) yields the Weitzenböck formula
$$0=2 \Delta|\Phi|^{2}+4\left|\nabla_{A} \Phi\right|^{2}+s|\Phi|^{2}+f|\Phi|^{4} .$$
Multiplying by $|\Phi|^{2}$ and integrating, we then obtain an inequality
$$0 \geq \int_{M}\left[4|\Phi|^{2}\left|\nabla_{A} \Phi\right|^{2}+s|\Phi|^{4}+f|\Phi|^{6}\right] d \mu$$
and we will now use this to prove our next result.
Proposition 3.8 Let $(M, g)$ be a smooth compact oriented Riemannian manifold, and let $\mathbf{a} \in H^{2}(M, \mathbb{R})$ be a monopole class of $M$. Then the scalar curvature $s$ and self-dual Weyl curvature $W_{+}$of $g$ satisfy
$$\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu_{g} \geq 72 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
If $\mathbf{a}^{+} \neq 0$, moreover, equality holds iff there is a symplectic form $\omega$, where $[\omega]$ is a negative multiple of $\mathbf{a}^{+}$and $c_{1}^{\mathbb{R}}(M, \omega)=\mathbf{a}$, such that $(M, g, \omega)$ is a saturated almost-Kähler manifold in the sense of Definition 2.3. .

Proof. For any smooth function $f>0$ on $M$, Lemma 3.7 guarantees that the corresponding rescaled Seiberg-Witten equations (17-18) must have some
solution $(\Phi, A)$. Set $\psi=2 \sqrt{2} \sigma(\Phi)$, and observe that the definition of $\sigma$ then implies that
$$|\Phi|^{4}=|\psi|^{2}, \quad 4|\Phi|^{2}\left|\nabla_{A} \Phi\right|^{2} \geq|\nabla \psi|^{2} .$$
Thus inequality (19) tells us that
$$0 \geq \int_{M}\left[|\nabla \psi|^{2}+s|\psi|^{2}+f|\psi|^{3}\right] d \mu$$
However, inequality (9) also tells us that
$$\int_{M}|\nabla \psi|^{2} d \mu \geq \int_{M}\left(-2 \sqrt{\frac{2}{3}}\left|W_{+}\right|-\frac{s}{3}\right)|\psi|^{2} d \mu$$
and combining these facts yields
$$0 \geq \int_{M}\left[\left(\frac{2}{3} s-2 \sqrt{\frac{2}{3}}\left|W_{+}\right|\right)|\psi|^{2}+f|\psi|^{3}\right] d \mu$$
Set $\varphi=\frac{3}{2} \psi=3 \sqrt{2} \sigma(\Phi)$. We then have
$$0 \geq \int_{M}\left[\left(s-\sqrt{6}\left|W_{+}\right|\right)|\varphi|^{2}+f|\varphi|^{3}\right] d \mu$$
Rewriting this as
$$\int_{M}\left[-\left(s-\sqrt{6}\left|W_{+}\right|\right) f^{-2 / 3}\right]\left(f^{2 / 3}|\varphi|^{2}\right) d \mu \geq \int_{M} f|\varphi|^{3} d \mu$$
and applying the Hölder inequality to the left-hand side then yields
$$\left[\int_{M}|s-\sqrt{6}| W_{+}| |^{3} f^{-2} d \mu\right]^{1 / 3}\left[\int_{M} f|\varphi|^{3} d \mu\right]^{2 / 3} d \mu \geq \int_{M} f|\varphi|^{3} d \mu$$
which is to say that
$$\int_{M}|s-\sqrt{6}| W_{+}| |^{3} f^{-2} d \mu \geq \int_{M} f|\varphi|^{3} d \mu$$
But the Hölder inequality also tells us that
$$\left(\int_{M} f^{4} d \mu\right)^{1 / 3}\left(\int_{M} f|\varphi|^{3} d \mu\right)^{2 / 3} \geq \int_{M} f^{4 / 3}\left[f^{2 / 3}|\varphi|^{2}\right] d \mu$$
where equality holds only if $|\varphi|$ is a constant multiple of $f$. Hence
$$\left(\int_{M} f^{4} d \mu\right)^{1 / 3}\left(\int_{M}|s-\sqrt{6}| W_{+}| |^{3} f^{-2} d \mu\right)^{2 / 3} \geq \int_{M} f^{2}|\varphi|^{2} d \mu$$
But since $f \varphi=3 \sqrt{2} f \sigma(\Phi)=3 \sqrt{2}\left(-i F_{A}^{+}\right)$, we also have
$$\int_{M} f^{2}|\varphi|^{2} d \mu=18 \int_{M}\left|F_{A}^{+}\right|^{2} d \mu \geq 18\left(2 \pi \mathbf{a}^{+}\right)^{2}=72 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
by Lemma 2.1, since $i F_{A} \in 2 \pi c_{1}^{\mathbb{R}}(L)=2 \pi \mathbf{a}$. Thus
$$\left(\int_{M} f^{4} d \mu_{g}\right)^{1 / 3}\left(\int_{M}|s-\sqrt{6}| W_{+}| |^{3} f^{-2} d \mu_{g}\right)^{2 / 3} \geq 72 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
for any smooth positive function $f$ on $M$.
Now choose a sequence of smooth positive functions $f_{j}$ on $M$ with
$$f_{j} \searrow \sqrt{|s-\sqrt{6}| W_{+}| |}$$
uniformly on $M$. Since the inequality $f_{j}^{2} \geq|s-\sqrt{6}| W_{+}| |$implies
$$\int_{M} f_{j}^{4} d \mu \geq\left(\int_{M} f_{j}^{4} d \mu_{g}\right)^{1 / 3}\left(\int_{M}|s-\sqrt{6}| W_{+}| |^{3} f_{j}^{-2} d \mu_{g}\right)^{2 / 3}$$
we then have
$$\int_{M} f_{j}^{4} d \mu \geq 72 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
by applying (20). But since
$$\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu=\lim _{j \rightarrow \infty} \int_{M} f_{j}^{4} d \mu$$
this shows that
$$\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu \geq 72 \pi^{2}\left(\mathbf{a}^{+}\right)^{2}$$
as desired.

Finally, we analyze the equality case. Suppose that $g$ is a metric such that equality holds in (21). Then $g$ must in particular minimize
$$\mathcal{A}(g)=\int\left(s_{g}-\sqrt{6}\left|W_{+}\right|_{g}\right)^{2} d \mu_{g}$$
in its conformal class. However, if $u$ is any smooth positive function, and if $\hat{g}=u^{2} g$, then
$$\mathcal{A}\left(u^{2} g\right)=\int\left(s_{g}+6 u^{-1} \Delta_{g} u-\sqrt{6}\left|W_{+}\right|_{g}\right)^{2} d \mu_{g}$$
so that, for the 1-parameter family of metrics given by
$$g_{t}=(1+t F)^{2} g$$
one has
$$\left.\frac{d}{d t} \mathcal{A}\left(g_{t}\right)\right|_{t=0}=12 \int\left[\Delta_{g} F\right]\left(s_{\hat{g}}-\sqrt{6}\left|W_{+}\right|_{\hat{g}}\right) d \mu_{g} .$$
If $g$ minimizes $\mathcal{A}$ in its conformal class, we must therefore have
$$\Delta_{g}\left(s-\sqrt{6}\left|W_{+}\right|\right)=0$$
in the weak (or distributional) sense. Elliptic regularity [12] therefore tells us that $s-\sqrt{6}\left|W_{+}\right|$is smooth, and integrating by parts
$$\int\left|\nabla\left(s-\sqrt{6}\left|W_{+}\right|\right)\right|^{2} d \mu=\int\left(s-\sqrt{6}\left|W_{+}\right|\right)\left[\Delta\left(s-\sqrt{6}\left|W_{+}\right|\right)\right] d \mu=0$$
therefore shows that
$$s-\sqrt{6}\left|W_{+}\right|=\text {constant } .$$
Assuming $\mathbf{a}^{+} \neq 0$, moreover, Proposition 3.3 tells us this constant must be negative. With this proviso, we can then set
$$f=\sqrt{|s-\sqrt{6}| W_{+}| |},$$
and equality in (21) then implies that equality occurs in (20) for this choice of $f>0$. But then, for this choice of $f$, we must therefore have equality at every step of the proof of (20). Since this $f$ is constant, it thus follows that $\varphi=3 \sqrt{2} \sigma(\Phi)$ is a closed self-dual 2-form of non-zero constant length.

Setting $\omega=\sqrt{2} \psi /|\psi|$, it follows that ( $M, g, \omega$ ) is an almost-Kähler manifold Moreover, since $\psi=\frac{2}{3} \varphi$ belongs to the lowest eigenspace of $W_{+}$at each point, while the two largest eigenvalues of $W_{+}$must be equal at every point, we have
$$\left|W_{+}\right|=\sqrt{\frac{3}{2}} \frac{\left[-W_{+}(\omega, \omega)\right]}{|\omega|^{2}}=-\frac{1}{2} \sqrt{\frac{3}{2}} W_{+}(\omega, \omega)$$
so that
$$s+s^{*}=s+\left[\frac{s}{3}+2 W_{+}(\omega, \omega)\right]=\frac{4}{3}\left(s-\sqrt{6}\left|W_{+}\right|\right),$$
which we already know to be a negative constant. The almost-Kähler manifold $(M, g, \omega)$ is therefore saturated in the sense of Definition 2.3. Moreover, since $\Phi \otimes \Phi$ is a non-zero section of $\Lambda_{J}^{2,0} \otimes L$ we have $c_{1}^{\mathbb{R}}(M, \omega)=c_{1}^{\mathbb{R}}(L)=\mathbf{a}$. Moreover, by construction, $\omega$ is a negative multiple of $i F_{A}^{+} / 2 \pi$, which is the harmonic representative of $\mathbf{a}^{+}$.

Conversely, if $(M, g, \omega)$ is an almost-Kähler manifold with $b_{+} \geq 2$, then $\mathbf{a}=c_{1}^{\mathbb{R}}(M, \omega)$ is a monopole class by Taubes' theorem [30], and in the saturated case our formula (10) then shows not only that the harmonic representative of $\mathbf{a}^{+}$is given by $i F_{B}^{+} / 2 \pi$, where $F_{B}$ is the curvature of the Blair connection, but also moreover that equality occurs in (21) for this choice of monopole class. The Proposition therefore follows. \(\square\)

\section*{4 Monopoles and Convex Hulls}

In the previous section, we saw that monopole classes lead to non-trivial lower bounds for the $L^{2}$-norms of certain curvature expressions. Unfortunately, however, these lower bounds still depend on the image of $g$ under the period map, and so are not yet uniform in the metric. We will now remedy this, using some simple tricks from convex geometry.

We begin by establishing a notational convention:
Definition 4.1 Let $\mathbb{V}$ be a vector space over $\mathbb{R}$, and let $S \subset \mathbb{V}$. Then $\operatorname{Hull}(S) \subset \mathbb{V}$ will denote the convex hull of $S$, meaning the smallest convex subset of $\mathbb{V}$ which contains $S$.

Lemma 4.2 Let $M$ be a smooth compact oriented 4-manifold with $b_{+} \geq 2$, and let $\mathfrak{C}=\mathfrak{C}(M) \subset H^{2}(M, \mathbb{R})$ be its set of non-zero monopole classes. Then
$\operatorname{Hull}(\mathfrak{C}) \subset H^{2}(M, \mathbb{R})$ is compact. Moreover, $\operatorname{Hull}(\mathfrak{C})$ is symmetric, in the sense that $\operatorname{Hull}(\mathfrak{C})=-\operatorname{Hull}(\mathfrak{C})$.

Proof. By definition, $\boldsymbol{\operatorname { H u l l }}(\mathfrak{C})$ is the smallest convex subset of $H^{2}(M, \mathbb{R})$ which contains $\mathfrak{C}(M)$. However, since $\mathfrak{C}(M)$ is a finite subset, say $\left\{\mathbf{a}_{1}, \ldots, \mathbf{a}_{n}\right\}$, we can explicitly express this convex hull as
$$\operatorname{Hull}(\mathfrak{C})=\left\{\sum_{j=1}^{n} t_{j} \mathbf{a}_{j} \mid t_{j} \in[0,1], \sum_{j=1}^{n} t_{j}=1\right\},$$
since the set on the right is certainly a convex subset containing the $\mathbf{a}_{j}$, and conversely is necessarily contained in any convex subset containing these points. In particular, this means that $\boldsymbol{\operatorname { H u l l }}(\boldsymbol{\mathfrak { C }})$ is the image of the standard $(n-1)$-simplex
$$\Delta^{n-1}=\left\{\left(t_{1}, \cdots, t_{n}\right) \in[0,1]^{n} \mid \sum_{j} t_{j}=1\right\}$$
under the continuous map
$$\left(t_{1}, \cdots, t_{n}\right) \longmapsto \sum_{j=1}^{n} t_{j} \mathbf{a}_{j},$$
and, since $\triangle^{n-1}$ is compact, it follows that $\boldsymbol{\operatorname { H u l l } ( \mathfrak { C } )}$ is, too.
On the other hand, Lemma 3.5 tells us that $\mathfrak{C}(M)$ is symmetric. Hence
$$\operatorname{Hull}(\mathfrak{C})=\operatorname{Hull}(-\mathfrak{C})=-\operatorname{Hull}(\mathfrak{C})$$
and $\mathbf{H u l l}(\mathfrak{C})$ is therefore symmetric, too. \(\square\)

Let us now consider the self-intersection function
$$\begin{aligned}
Q: H^{2}(M, \mathbb{R}) & \longrightarrow \mathbb{R} \\
\mathbf{v} & \longmapsto \mathbf{v}^{2}
\end{aligned}$$
where $\mathbf{v}^{2}$ is of course just short-hand for $\mathbf{v} \cdot \mathbf{v}=\langle\mathbf{v} v \mathbf{v},[M]\rangle$. Notice that $Q$ is a polynomial function, and therefore continuous. Since $\boldsymbol{\operatorname { H u l l }}(\mathfrak{C})$ is compact by Lemma 4.2, it thus follows that $\left.Q\right|_{\text {Hull }(\mathfrak{C})}$ necessarily achieves its maximum. We are thus entitled to make the following definition:

Definition 4.3 Let $M$ be a smooth compact oriented 4-manifold with $b_{+} \geq 2$, and let $\operatorname{Hull}(\mathfrak{C}) \subset H^{2}(M, \mathbb{R})$ denote the convex hull of the set $\mathfrak{C}=\mathfrak{C}(M)$ of monopole classes of $M$. If $\mathfrak{C} \neq \varnothing$, we define
$$\beta^{2}(M)=\max \left\{\mathbf{v}^{2} \mid \mathbf{v} \in \operatorname{Hull}(\mathfrak{C})\right\} .$$
If, on the other hand, $\mathfrak{C}=\varnothing$, we instead set $\beta^{2}(M)=0$.
Proposition 4.4 For any smooth $M^{4}$ with $b_{+} \geq 2, \beta^{2}(M) \geq 0$.
Proof. If $\mathfrak{C}=\varnothing$, we have $\beta^{2}(M)=0$ by Definition 4.3. Otherwise, let $\mathbf{a} \in \mathfrak{C}$, and observe that $-\mathbf{a} \in \mathfrak{C}$, too, by Lemma 3.5. Thus $\mathbf{0}=\frac{1}{2} \mathbf{a}+\frac{1}{2}(-\mathbf{a}) \in$ Hull( $\mathfrak{C}$ ). Hence
$$\beta^{2}(M)=\max \left\{\mathbf{v}^{2} \mid \mathbf{v} \in \operatorname{Hull}(\mathfrak{C})\right\} \geq \mathbf{0}^{2}=0,$$
exactly as claimed. \(\square\)

Proposition 4.5 Let $M$ be a smooth compact oriented 4-manifold with $\mathfrak{C}(M) \neq \varnothing$. Then, for any Riemannian metric $g$ on $M$, there is a monopole class $\mathbf{a} \in \mathfrak{C}(M)$ such that
$$\left(\mathbf{a}^{+}\right)^{2} \geq \beta^{2}(M) .$$

Proof. Let $\mathbf{v} \in \operatorname{Hull}(\mathfrak{C})$ be a maximum point of $Q$, so that $\mathbf{v}^{2}=\beta^{2}(M)$ by Definition 4.3. Let $\Pi: H^{2}(M, \mathbb{R}) \rightarrow \mathcal{H}_{g}^{+}$denote the orthogonal projection map. Since $\Pi$ is a linear map, we automatically have $\operatorname{Hull}(\Pi(\mathfrak{C}))=$ $\Pi(\mathbf{H u l l}(\mathfrak{C}))$. However, since the intersection form is positive definite on $\mathcal{H}_{g}^{+}$, $\left.Q\right|_{\mathcal{H}_{g}^{+}}$has positive-definite Hessian, and the maximum of $Q$ on a line segment $\overline{\mathbf{p q}} \subset \mathcal{H}_{g}^{+}$can therefore never occur at an interior point. The maximum points of $\left.Q\right|_{\Pi(\mathbf{H} u l l(\mathfrak{C}))}$ must therefore all belong to $\Pi(\mathfrak{C})$. In particular, there must be a monopole class $\mathbf{a} \in \mathfrak{C}$ such that
$$\left(\mathbf{a}^{+}\right)^{2}=Q(\Pi(\mathbf{a})) \geq Q(\Pi(\mathbf{v}))=\left(\mathbf{v}^{+}\right)^{2} .$$
On the other hand,
$$\mathbf{v}^{2}=\left(\mathbf{v}^{+}\right)^{2}-\left|\left(\mathbf{v}^{-}\right)^{2}\right|,$$
so we therefore have
$$\left(\mathbf{a}^{+}\right)^{2} \geq\left(\mathbf{v}^{+}\right)^{2} \geq \mathbf{v}^{2}=\beta^{2}(M),$$
and the monopole class a therefore fulfills our desideratum. \(\square\)

The first part of Theorem A now follows immediately:
Theorem 4.6 Let $M$ be a smooth compact oriented 4-manifold with $b_{+} \geq 2$. Then any metric $g$ on $M$ satisfies curvature estimates (1) and (2):
$$\begin{aligned}
\int_{M} s^{2} d \mu & \geq 32 \pi^{2} \beta^{2}(M) \\
\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu & \geq 72 \pi^{2} \beta^{2}(M)
\end{aligned}$$

Proof. For any metric $g$ on $M$, Proposition 4.5 tells us that there is a monopole class a such that $\left(\mathbf{a}^{+}\right)^{2} \geq \beta^{2}(M)$. Proposition 3.2 therefore tells us that
$$\int_{M} s^{2} d \mu \geq 32 \pi^{2}\left(\mathbf{a}^{+}\right)^{2} \geq 32 \pi^{2} \beta^{2}(M)$$
while Proposition 3.8 tells us that
$$\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu \geq 72 \pi^{2}\left(\mathbf{a}^{+}\right)^{2} \geq 72 \pi^{2} \beta^{2}(M)$$
and the Theorem therefore follows. \(\square\)

To prove Theorem A, we therefore merely need to understand the equality cases of the curvature estimates (1) and (2). To do this, we will first need the following simple observation:

Lemma 4.7 Suppose that $(M, g)$ is a Riemannian manifold with $b_{+} \geq 2$, and that $M$ carries a non-zero monopole class. If equality occurs in either (1) or (2), then $\beta^{2}(M)>0$.

Proof. If equality were to hold in (1) or (2), and if we also had $\beta^{2}(M)=0$, the metric in question would necessarily have $s \geq 0$. But Proposition 3.3 says that no such metric can exist in the presence of a non-zero monopole class. The claim thus follows by contradiction. \(\square\)

We will also need the following basic fact:

Lemma 4.8 If $M$ is a a smooth compact oriented 4-manifold with $b_{+}>1$, and if $g$ is a Kähler-Einstein metric on $M$ with negative scalar curvature, then equality is achieved in (1) by $g$.

Proof. For any compact Kähler surface $(M, J)$ with $b_{+}>1$, the classical Seiberg-Witten invariant is well-defined and non-zero [31] for the spin ${ }^{c}$ structure determined by $J$, and $\mathbf{a}=c_{1}^{\mathbb{R}}(M, J)$ is therefore a monopole class. Hence $c_{1}^{\mathbb{R}}(M, J) \in \mathfrak{C} \subset \operatorname{Hull}(\mathfrak{C})$, and
$$\beta^{2}(M)=\max \left\{\mathbf{v}^{2} \mid \mathbf{v} \in \operatorname{Hull}(\mathfrak{C})\right\} \geq c_{1}^{2}(M) .$$
On the other hand, the Ricci form $\rho=r(J \cdot, \cdot)$ represents $2 \pi c_{1}^{\mathbb{R}}(M, J)$ in de Rham cohomology, and just equals $s \omega / 4$ in the Kähler-Einstein case. Thus, since the volume form of a Kähler surface is given by $\omega^{2} / 2$, we have
$$\int_{M} s^{2} d \mu=\int \frac{(s \omega)^{2}}{2}=8 \int \rho \wedge \rho=32 \pi^{2} c_{1}^{2}(M)$$
Proposition 3.2 therefore tells us that
$$32 \pi^{2} c_{1}^{2}(M)=\int_{M} s^{2} d \mu \geq 32 \pi^{2} \beta^{2}(M) \geq 32 \pi^{2} c_{1}^{2}(M)$$
and equality must thus hold at every step. Hence $\beta^{2}(M)=c_{1}^{2}(M)$, and equality is achieved in (1) by $g$, as claimed. \(\square\)

Lemma 4.9 Let $M$ be a compact oriented 4-manifold with $b_{+} \geq 2$ which carries a non-zero monopole class. Then whenever equality holds in (1) for a metric $g$ on $M$, equality holds in (2), too.

Proof. If equality holds in (1), we have
$$32 \pi^{2} \beta^{2}(M)=\int_{M} s^{2} d \mu$$
so by Propositions 3.2 and 4.5, there is a monopole class a such that
$$32 \pi^{2} \beta^{2}(M)=\int_{M} s^{2} d \mu \geq 32 \pi^{2}\left(\mathbf{a}^{+}\right)^{2} \geq 32 \pi^{2} \beta^{2}(M)>0$$
and equality must therefore hold throughout. But Proposition 3.2 then asserts that there exists a complex structure $J$ such that $(M, g, J)$ is a a Kähler manifold of constant negative scalar curvature.

Now any Kähler metric on a complex surface automatically satisfies $\left|W_{+}\right|^{2}=s^{2} / 24$, so that $s-\sqrt{6}\left|W_{+}\right|=\frac{3}{2} s$ wherever $s \leq 0$. Our negativescalar-curvature Kähler metric $g$ thus satisfies
$$\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu=\left(\frac{3}{2}\right)^{2} \int_{M} s^{2} d \mu=72 \pi^{2} \beta^{2}(M)$$
and therefore also achieves equality in (2), as claimed. \(\square\)

We now analyze the boundary case of (2).
Theorem 4.10 Let $M$ be a compact oriented 4-manifold with $b_{+} \geq 2$ which carries a non-zero monopole class, and suppose that $g$ is a metric on $M$ such that equality holds in (2):
$$\int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu=72 \pi^{2} \beta^{2}(M)$$
Then $g$ is Kähler-Einstein, with negative Einstein constant.
Proof. Let $\mathbf{v} \in \operatorname{Hull}(\mathfrak{C})$ be a point where $\mathbf{v}^{2}=\mathbf{v} \cdot \mathbf{v}$ achieves its maximum value, namely $\beta^{2}(M)$. Let $\mathbf{a}_{1}, \ldots, \mathbf{a}_{n} \in \mathfrak{C}$ be a list of all the monopole classes, and express $\mathbf{v} \in \operatorname{Hull}(\mathfrak{C})$ as
$$\mathbf{v}=\sum_{j=1}^{n} t_{j} \mathbf{a}_{j}$$
where the coefficients $t_{j} \in[0,1]$ satisfy $\sum_{j} t_{j}=1$; and after permuting the $\mathbf{a}_{j}$ as necessary, we may henceforth assume that $t_{j}>0$ iff $j \leq m$, where $m$ is some integer, $1 \leq m \leq n$. By Propositions 3.8 and 4.5,
$$\begin{aligned}
\frac{1}{72 \pi^{2}} \int_{M}\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu & \geq \max \left\{\left(\mathbf{a}_{j}^{+}\right)^{2} \mid j=1, \ldots, n\right\} \\
& \geq\left(\mathbf{v}^{+}\right)^{2} \geq \mathbf{v}^{2}=\beta^{2}(M)
\end{aligned}$$
and our hypotheses therefore imply that equality holds at every step. In particular, it follows that $\mathbf{v}=\mathbf{v}^{+}$and that $\max _{j}\left(\mathbf{a}_{j}^{+}\right)^{2}=\beta^{2}(M)$. Since the
intersection form is positive definite on $\mathcal{H}_{g}^{+}$, the Cauchy-Schwarz inequality therefore tells us that
$$\mathbf{v} \cdot \mathbf{a}_{j}^{+} \leq \sqrt{\left(\mathbf{a}_{j}^{+}\right)^{2}} \sqrt{(\mathbf{v})^{2}} \leq \beta^{2}(M),$$
for all $j$, with equality iff $\mathbf{a}_{j}^{+}=\mathbf{v}$. Since
$$\begin{aligned}
\beta^{2}(M) & =\mathbf{v} \cdot \mathbf{v}=\mathbf{v} \cdot \mathbf{v}^{+} \\
& =\mathbf{v} \cdot\left(\sum_{j=1}^{m} t_{j} \mathbf{a}_{j}^{+}\right) \\
& =\sum_{j=1}^{m} t_{j}\left(\mathbf{v} \cdot \mathbf{a}_{j}^{+}\right) \\
& \leq \sum_{j=1}^{m} t_{j} \beta^{2}(M) \\
& =\beta^{2}(M)\left(\sum_{j=1}^{m} t_{j}\right) \\
& =\beta^{2}(M),
\end{aligned}$$
we must therefore have $\mathbf{a}_{j}^{+}=\mathbf{v}$ for every $j=1, \ldots, m$.
For each $j=1, \ldots, m$, we therefore have $\left(\mathbf{a}_{j}^{+}\right)^{2}=\beta^{2}(M)$. Moreover, $\beta^{2}(M)>0$ by Lemma 4.7. Our hypotheses thus imply that
$$\int\left(s-\sqrt{6}\left|W_{+}\right|\right)^{2} d \mu=72 \pi^{2}\left(\mathbf{a}_{j}^{+}\right)^{2}>0$$
and Proposition 3.8 therefore tells us that there is a $g$-compatible symplectic form $\omega_{j}$ such that $\left[\omega_{j}\right]$ is a negative multiple of $\mathbf{a}_{j}^{+}=\mathbf{v}$, and such that $c_{1}^{\mathbb{R}}\left(M, \omega_{j}\right)=\mathbf{a}_{j}$ for each $j=1, \ldots, m$. Since $\left[\omega_{j}\right]^{2} / 2=\operatorname{Vol}(M, g)$ for each $j$, it follows that $\left[\omega_{1}\right]=\cdots=\left[\omega_{m}\right] \in H^{2}(M, \mathbb{R})$. But each $\omega_{j}$ is harmonic with respect to $g$, and the harmonic representative of any de Rham class is unique. Hence $\omega_{1}=\cdots=\omega_{m}$. But since $c_{1}^{\mathbb{R}}\left(M, \omega_{j}\right)=\mathbf{a}_{j}$, this implies that $\mathbf{a}_{1}=\cdots=\mathbf{a}_{m}$. Hence $m=1$, and
$$\mathbf{v}=\sum_{j=1}^{m} t_{j} \mathbf{a}_{j}=\mathbf{a}_{1}=c_{1}^{\mathbb{R}}(M, \omega) .$$

Let us now simplify our notation by setting $\omega=\omega_{1}$. Since $-[\omega] \propto \mathbf{v}=$ $c_{1}(M, \omega)$, the curvature of any connection on the anti-canonical line bundle $L$ of $(M, \omega)$ must be cohomologous to a constant negative multiple of $\omega$. However, we saw in (10-11) that the curvature $F_{B}=F_{B}^{+}+F_{B}^{-}$of the Blair connection on $L$ is given by
$$\begin{aligned}
i F_{B}^{+} & =\frac{s+s^{*}}{8} \omega+W^{+}(\omega)^{\perp} \\
i F_{B}^{-} & =\frac{s-s^{\star}}{8} \hat{\omega}+\stackrel{\circ}{\varrho}
\end{aligned}$$
where $W^{+}(\omega)^{\perp}$ is the component of $W^{+}(\omega)$ orthogonal to $\omega$,
$$\grave{\varrho}(\cdot, J \cdot)=\frac{\grave{r}+J^{*} \grave{r}}{2},$$
and where the bounded anti-self-dual 2-form $\hat{\omega} \in \Lambda^{-}$is defined only on the open set where $s^{\star}-s \neq 0$, and satisfies $|\hat{\omega}| \equiv \sqrt{2}$. Here, the star-scalar curvature $s^{*}$ once again means the important quantity
$$s^{*}=s+|\nabla \omega|^{2}=2 W_{+}(\omega, \omega)+\frac{s}{3} .$$
Since Proposition 3.8 tells us that $(M, g, \omega)$ is saturated, $s+s^{*}$ is constant and $W^{+}(\omega)^{\perp}=0$. Hence $F_{B}^{+}$is closed, and therefore $\star F_{B}=2 F_{B}^{+}-F_{B}$ is closed, too. Thus $F_{B}$ is harmonic. But we also know that $F_{B}$ is cohomologous to a constant multiple of $\omega$, which is itself a self-dual harmonic form. Hence $F_{B}^{-} \equiv 0$, and
$$\varrho \equiv \frac{s^{\star}-s}{8} \hat{\omega} .$$
This shows that
$$|\stackrel{\circ}{r}|^{2} \geq \frac{\left(s^{*}-s\right)^{2}}{16}$$
at every point of $M$, with equality precisely at those points at which the Ricci tensor $r$ is $J$-invariant.

On the other hand, $W_{+}$has eigenvalues $(-\lambda / 2,-\lambda / 2, \lambda)$, where
$$\lambda=\frac{1}{2} W_{+}(\omega, \omega)=\frac{3 s^{*}-s}{12},$$
so
$$\left|W_{+}\right|^{2}=\frac{\left(3 s^{*}-s\right)^{2}}{96} .$$

Hence
$$\begin{aligned}
4 \pi^{2}(2 \chi+3 \tau)(M) & =\int_{M}\left(\frac{s^{2}}{24}+2\left|W_{+}\right|^{2}-\frac{|\stackrel{\circ}{r}|^{2}}{2}\right) d \mu \\
& =\int_{M}\left(\frac{s^{2}}{24}+\frac{2\left(3 s^{*}-s\right)^{2}}{96}-\frac{|\stackrel{\circ}{r}|^{2}}{2}\right) d \mu \\
& \leq \int_{M}\left(\frac{s^{2}}{24}+\frac{2\left(3 s^{*}-s\right)^{2}}{96}-\frac{\left(s^{*}-s\right)^{2}}{32}\right) d \mu \\
& =\frac{1}{32} \int_{M}\left(s^{2}-2 s s^{*}+5\left(s^{*}\right)^{2}\right) d \mu
\end{aligned}$$
with equality iff $|\dot{r}|^{2} \equiv\left(s^{*}-s\right)^{2} / 16$. On the other hand, since $F_{B}=F_{B}^{+}$,
$$\begin{aligned}
4 \pi^{2}(2 \chi+3 \tau)(M) & =4 \pi^{2} c_{1}^{2}(M) \\
& =\int_{M}\left(\frac{s+s^{*}}{8} \omega\right) \wedge\left(\frac{s+s^{*}}{8} \omega\right) \\
& =\frac{1}{32} \int_{M}\left(s^{2}+2 s s^{*}+\left(s^{*}\right)^{2}\right) d \mu
\end{aligned}$$
so we therefore have
$$\int_{M}\left(s^{2}-2 s s^{*}+5\left(s^{*}\right)^{2}\right) d \mu \geq\left(s^{2}+2 s s^{*}+\left(s^{*}\right)^{2}\right) d \mu$$
which we can rewrite as
$$\int_{M} 4 s^{*}\left(s^{*}-s\right) d \mu \geq 0$$
moreover, equality can hold only if $|\stackrel{\circ}{r}|^{2} \equiv\left(s^{*}-s\right)^{2} / 16$. However, since $(M, g, \omega)$ is saturated, $s^{*}+s$ is a negative constant, and $W_{+}(\omega, \omega) \leq 0$; hence $s^{*} \leq s / 3$, and $s^{*} \leq\left(s+s^{*}\right) / 4$ is therefore negative everywhere. On the other hand, $s^{*}-s=|\nabla \omega|^{2} \geq 0$ on any almost-Kähler manifold. Hence
$$s^{*}\left(s^{*}-s\right) \leq 0$$
everywhere on $M$, with equality only at points where $s=s^{*}$. The inequality (22) therefore implies that
$$|\nabla \omega|^{2}=s-s^{*} \equiv 0 .$$

Hence $(M, g, \omega)$ is Kähler. But equality in (22) only holds if $|\dot{r}|^{2} \equiv\left(s^{*}-s\right)^{2} / 16$, so we moreover must have $\stackrel{\circ}{r} \equiv 0$, and we therefore conclude that $(M, g)$ is Kähler-Einstein, as promised. \(\square\)

Our main result now follows easily:
Proof of Theorem A. Theorem 4.6 shows that (1) and (2) hold for any metric on any 4-manifold with $b_{+} \geq 2$. On the other hand, assuming there is at least one non-zero monopole class, Theorem 4.10 shows that any metric for which equality holds in (2) must be Kähler-Einstein. Lemma 4.9 thus implies that any metric for which equality holds in (1) must be Kähler-Einstein, too. Finally, Lemmas 4.8 and 4.9 show that equality actually does hold in (1) and (2) when the metric is Kähler-Einstein. \(\square\)

Of course, the method used here to treat the boundary case of (1) has a Rube Goldberg feel to it, since it proceeds by reducing an easy problem to a harder one. However, it is not difficult to winnow a simple, direct treatment of this case out of the above discussion. Details are left to the interested reader.

\section*{5 Concluding Remarks}

One apparent weakness of our definition of $\beta^{2}(M)$ is that there is no obvious way of exactly determining the entire set $\mathfrak{C}(M)$ of all monopole classes of a given 4-manifold $M$. However, we do have various criteria which serve to show that certain classes really do belong to $\mathfrak{C}(M)$. Thus, if $\mathfrak{S} \subset \mathfrak{C}(M)$ is some collection of known monopole classes, we then have
$$\beta^{2}(M) \geq \max \left\{\mathbf{v}^{2} \mid \mathbf{v} \in \operatorname{Hull}(\mathfrak{S})\right\} .$$
It is thus relatively easy to find lower bounds for $\beta^{2}$, even without knowing $\mathfrak{C}(M)$ exactly.

At the same time, our curvature estimates (1) and (2) provide upper bounds for $\beta^{2}(M)$ for each metric $g$ on $M$. By taking an infimum of such upper bounds for a carefully chosen sequence of metrics $g_{j}$ on $M$, one can, in practice, often determine $\beta^{2}(M)$ by showing that it is simultaneously no less than and no greater than some target value.

Example Let $X$ be a minimal complex surface of general type, and let $M=X \# k \overline{\mathbb{C P}}_{2}$ be its blow-up at $k$ points. Then
$$\beta^{2}(M)=c_{1}^{2}(X) .$$
Indeed, if $E_{1}, \ldots, E_{k}$ are generators for the various copies of $H^{2}\left(\overline{\mathbb{C P}}_{2}, \mathbb{Z}\right)$, then $\pm c_{1}(X) \pm E \pm \cdots \pm E_{k}$ are the first Chern classes of various complex structures of Kähler type on $M$, and so are monopole classes [31]. Hence $c_{1}(X) \in$ Hull $(\mathfrak{C}(M))$, and hence $\beta^{2}(M) \geq c_{1}^{2}(X)$. However, by approximating the Kähler-Einstein orbifold metric on the pluricanonical model for $X$, one can construct [24] sequences of metrics $g_{j}$ on $M$ with $\int s^{2} d \mu \searrow 32 \pi^{2} c_{1}^{2}(X)$. Thus (1) implies that we also have $c_{1}^{2}(X) \geq \beta^{2}(M)$, and the claim follows. \(\square\)

Example Let $X, Y$, and $Z$ be simply connected, minimal complex surfaces of general type with $h^{2,0}$ odd. Let $M=X \# Y \# Z \# k \overline{\mathbb{C P}}_{2}$. Then
$$\beta^{2}(M)=c_{1}^{2}(X)+c_{1}^{2}(Y)+c_{1}^{2}(Z) .$$
Indeed, using the Bauer-Furuta invariant, one can show that
$$\pm c_{1}(X) \pm c_{1}(Y) \pm c_{1}(Z) \pm E_{1} \pm \cdots \pm E_{k} \in \mathfrak{C}(M) .$$
Hence $\mathbf{v}=c_{1}(X)+c_{1}(Y)+c_{1}(Z) \in \mathbf{H u l l}(\mathfrak{C}(M))$, and
$$\beta^{2}(M) \geq\left[c_{1}(X)+c_{1}(Y)+c_{1}(Z)\right]^{2}=c_{1}^{2}(X)+c_{1}^{2}(Y)+c_{1}(Z) .$$
On the other hand, there exist [16] sequences of metrics $g_{j}$ on $M$ with $\int s^{2} d \mu \searrow 32 \pi^{2}\left[c_{1}^{2}(X)+c_{1}^{2}(Y)+c_{1}(Z)\right]$, so (1) therefore shows that we also have $c_{1}^{2}(X)+c_{1}^{2}(Y)+c_{1}^{2}(Z) \geq \beta^{2}(M)$. The claim therefore follows.

Similar techniques can also be used for connected sums involving two or four surfaces of general type. \(\square\)

Example Let $N$ be any oriented 3-manifold, and let $M=N \times S^{1}$. Then $\beta^{2}(M)=0$, because one has $\int s^{2} d \mu \searrow 0$ for product metrics on $M$ with shorter and shorter $S^{1}$ factors. However, that results of Kronheimer [19] imply that such manifolds typically carry many monopole classes, although these all belong to the isotropic subspace $H^{2}(N) \hookrightarrow H^{2}\left(N \times S^{1}\right)$. \(\square\)

By the arguments detailed in [22, 25], the estimates (1) and (2) have the following interesting consequences:

Theorem 5.1 Let $M$ be a smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$. If $M$ admits an Einstein metric $g$, then
$$(2 \chi-3 \tau)(M) \geq \frac{1}{3} \beta^{2}(M)$$
Moreover, if $M$ carries a non-zero monopole class, equality occurs only if $(M, g)$ is a compact quotient $\mathbb{C H}_{2} / \Gamma$ of the complex hyperbolic plane, equipped with a constant multiple of its standard Kähler-Einstein metric.

Theorem 5.2 Let $M$ be a smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$. If $M$ admits an Einstein metric $g$, then
$$(2 \chi+3 \tau)(M) \geq \frac{2}{3} \beta^{2}(M),$$
with equality only if both sides vanish, in which case $g$ must be a hyper-Kähler metric, and $M$ must be diffeomorphic to K3 or $T^{4}$.

Theorem 5.3 Let $M$ be a smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$. Then any metric $g$ on $M$ satisfies
$$\int_{M}|r|^{2} d \mu \geq 8 \pi^{2}\left[2 \beta^{2}-(2 \chi+3 \tau)\right](M)$$
with equality iff $g$ is Kähler-Einstein.
Now Proposition 4.4 entitles us to introduce the following definition:
Definition 5.4 If $M$ is any smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$, we set $\beta(M):=\sqrt{\beta^{2}(M)}$.

This invariant provides a natural yardstick with which to measure the Yamabe invariants of 4-manifolds:

Theorem 5.5 Let $M$ be a smooth compact oriented 4-manifold with $b_{+}(M) \geq 2$. If $M$ carries at least one non-zero monopole class, then the Yamabe invariant of $M$ satisfies
$$\mathcal{Y}(M) \leq-4 \sqrt{2} \pi \beta(M) .$$

We remark in passing that if $M$ does not admit a metric of positive scalar curvature, its Yamabe invariant $\mathcal{Y}(M)$ is just the supremum of the scalar curvatures of unit-volume constant-scalar-curvature metrics on $M$. This result is therefore an immediate consequence of (1). More intriguingly, though, Theorem 5.5 is actually sharp; equality actually holds [24, 16] for large classes of 4-manifolds, including those discussed on page 31.

Now, while we have seen that considering the convex hull of the set of monopole classes leads to an elegant invariant $\beta^{2}(M)$ which seems remarkably well adapted to the study of the curvature of 4-manifolds, it is still unclear whether this approach is optimal in all circumstances. Indeed, the basic forms of our estimates, seen in Propositions 3.2 and 3.8, involve the numbers $\left(\mathbf{a}^{+}\right)^{2}$ for the various monopole classes, and one can therefore [26] define an invariant which simply tries to make optimal use of this information. Indeed, consider the open Grassmannian $\mathbf{G r}=G r_{b_{+}}^{+}\left[H^{2}(M, \mathbb{R})\right]$ of all maximal linear subspaces H of the second cohomology on which the restriction of the intersection pairing is positive definite. Each element $\mathbf{H} \in \mathbf{G r}$ then determines an orthogonal decomposition
$$H^{2}(M, \mathbb{R})=\mathbf{H} \oplus \mathbf{H}^{\perp}$$
with respect to the intersection form. Given a monopole class $\mathbf{a} \in \mathfrak{C}$ and a positive subspace $\mathbf{H} \in \mathbf{G r}$, we may then define $\mathbf{a}^{+}$to be the orthogonal projection of a into H. Using this, we now define yet another orienteddiffeomorphism invariant.

Definition 5.6 Let $M$ be a smooth compact oriented manifold with $b_{+} \geq 2$. If $\mathfrak{C}=\varnothing$, set $\alpha^{2}(M)=0$. Otherwise, we set
$$\alpha^{2}(M)=\inf _{\mathbf{H} \in \mathbf{G r}}\left[\max _{a \in \mathfrak{C}}\left(\mathbf{a}^{+}\right)^{2}\right] .$$
Propositions (3.2) and (3.8) then easily imply that (1) and (2) still hold when $\beta^{2}(M)$ is replaced by $\alpha^{2}(M)$. Moreover, the proof of Proposition 4.5 shows that one always has
$$\alpha^{2}(M) \geq \beta^{2}(M) .$$

On the other hand, we have also seen that (1) and (2) are sharp for large classes of manifolds, such as those discussed on page 31. Thus $\alpha^{2}=\beta^{2}$ in all these cases. It is therefore only natural for us to ask whether this is a general phenomenon. In this direction, however, we can only give some partial results. We begin with the following:

Lemma 5.7 Let $M$ be a smooth oriented 4-manifold with $b_{+} \geq 2$. Then
$$\alpha^{2}(M)=0 \Longleftrightarrow \beta^{2}(M)=0 .$$

Proof. The ⟹ direction is obvious, since $\alpha^{2} \geq \beta^{2} \geq 0$. Conversely, if $\beta^{2}=0$, the intersection form must be negative-semi-definite on $\boldsymbol{\operatorname { s p a n }}(\mathfrak{C})$. Write this subspace as $\mathbf{N} \oplus \mathbf{I}$, where the intersection form is negative-definite on $\mathbf{N}$ and vanishes on $\mathbf{I}$. We can then choose a sequence $\mathbf{H}_{j} \in \mathbf{G r}$ which are all orthogonal to $\mathbf{N}$ and which decompose orthogonally as $\mathbf{P} \oplus \mathbf{J}_{j}$, where $\mathbf{P}$ is orthogonal to $\mathbf{I}$ and $\mathbf{J}_{j} \rightarrow \mathbf{I}$. Then each monopole class satisfies $\left(\mathbf{a}^{+}\right)^{2} \rightarrow 0$ for this sequence. It thus follows that $\alpha^{2}=0$, as claimed. \(\square\)

Next, we point out the following:
Proposition 5.8 Let $M$ be a smooth oriented 4-manifold with $b_{+} \geq 2$. Suppose, moreover, that there is a linear subspace $\mathbf{L} \subset H^{2}(M, \mathbb{R})$ on which the intersection form is of Lorentzian (+-…-) type, with
$$\mathfrak{C}(M) \subset \mathbf{L} \subset H^{2}(M, \mathbb{R}) .$$
Then $\alpha^{2}(M)=\beta^{2}(M)$.
Proof.By Lemma 5.7, we may assume that $\beta^{2}(M)>0$. Let $\mathbf{v} \in \operatorname{Hull}(\mathfrak{C}) \subset$ $\mathbf{L}$ be an element with $\mathbf{v}^{2}=\beta^{2}(M)>0$. Now, since $(1-t) \mathbf{v}+t \mathbf{a} \in \mathbf{H u l l}(\mathfrak{C})$ for any $\mathbf{a} \in \mathfrak{C}$ and any $t \in[0,1]$, we therefore have
$$\mathbf{v}^{2} \geq[(1-t) \mathbf{v}+t \mathbf{a}]^{2}=\mathbf{v}^{2}+2 t\left(\mathbf{v} \cdot \mathbf{a}-\mathbf{v}^{2}\right)+O\left(t^{2}\right)$$
for all small positive $t$, and it therefore follows that
$$\mathbf{v} \cdot \mathbf{a} \leq \mathbf{v}^{2}$$
for all monopole classes a. Since $\mathfrak{C}(M)$ is invariant under multiplication by -1, it moreover follows that
$$|\mathbf{v} \cdot \mathbf{a}| \leq \mathbf{v}^{2} \quad \forall \mathbf{a} \in \mathfrak{C}(M) .$$

Now let $\mathbf{P} \subset \mathbf{L}^{\perp}$ be a maximal positive subspace, and set $\mathbf{H}=\mathbf{P} \oplus$ span (v). Then for this choice of $\mathbf{H} \in \mathbf{G r}$ we have
$$\mathbf{a}^{+}=\frac{\mathbf{v} \cdot \mathbf{a}}{\mathbf{v}^{2}} \mathbf{v}$$
and hence
$$\left(\mathbf{a}^{+}\right)^{2}=\frac{(\mathbf{v} \cdot \mathbf{a})^{2}}{\mathbf{v}^{2}} \leq \mathbf{v}^{2}=\beta^{2}(M)$$
for all $\mathbf{a} \in \mathfrak{C}$. Hence
$$\alpha^{2}(M)=\inf _{\mathbf{H} \in \mathbf{G r}}\left[\max _{a \in \mathfrak{C}}\left(\mathbf{a}^{+}\right)^{2}\right] \leq \beta^{2}(M) .$$
But we also know that $\beta^{2} \leq \alpha^{2}$, so it follows that $\alpha^{2}=\beta^{2}$, as claimed. \(\square\)

Example If ( $M, J$ ) is a compact complex surface of Kähler type with $b_{+}>1$, we may take $\mathbf{L}=H^{1,1}(M, \mathbb{R}) \subset H^{2}(M, \mathbb{R})$. Since an argument due to Witten [31] shows that solutions of the Seiberg-Witten equations can exist with respect to a Kähler metric only when $c_{1}(L)$ is a (1, 1)-class, it follows that any monopole class must belong to $\mathbf{L}$. This provides one explanation of why $\alpha^{2}=\beta^{2}$ for complex algebraic surfaces. \(\square\)

In light of Proposition 5.8, the reader may be curious as to why we have systematically excluded the case of $b_{+}=1$ in this paper. In truth, most of the formal theory actually works perfectly well in this case. However, the Seiberg-Witten invariants have a chamber structure when $b_{+}=1$, and this has the effect that, for example, complex surfaces with $c_{1}^{2}<0$ will typically not carry any monopole classes at all. Nonetheless, Seiberg-Witten theory still gives rise [24] to non-trivial curvature bounds in this setting, even though this phenomenon cannot be explained in terms of monopole classes.

We now turn to a more complicated situation:
Proposition 5.9 Let $M$ be a smooth oriented 4-manifold with $b_{+} \geq 2$, and suppose that there is a collection of mutually orthogonal linear subspaces $\mathbf{L}_{j} \subset H^{2}(M, \mathbb{R}), j=1, \ldots, \ell$, on each of which the intersection form is of Lorentzian (+-…-) type. Moreover, suppose that
$$\mathfrak{C}(M)=\mathfrak{C}_{1} \times \cdots \times \mathfrak{C}_{\ell} \subset \mathbf{L}_{1} \oplus \cdots \oplus \mathbf{L}_{\ell},$$
for some subsets
$$\mathfrak{C}_{j} \subset \mathbf{L}_{j}, \quad j=1, \ldots, \ell .$$
Then $\alpha^{2}(M)=\beta^{2}(M)$.

Proof. Fix a maximal positive subspace $\mathbf{P} \subset\left(\mathbf{L}_{1} \oplus \cdots \oplus \mathbf{L}_{\ell}\right)^{\perp}$, and consider choices of $\mathbf{H} \in \mathbf{G r}$ of the form $\mathbf{H}=\mathbf{P} \oplus \operatorname{span}\left\{e_{1}, \ldots, e_{\ell}\right\}$, where $e_{j} \in \mathbf{L}_{j}$ is a non-zero time-like vector. If the intersection form on $\boldsymbol{\operatorname { s p a n }}\left(\mathfrak{C}_{j}\right)$ is negative-definite, moreover choose $e_{j} \in \mathbf{L}_{j}$ to be orthogonal to this subspace. If, on the other hand, $\boldsymbol{\operatorname { s p a n }}\left(\mathfrak{C}_{j}\right)$ is Lorentzian, set $e_{j}=\mathbf{v}_{j}$, where $\mathbf{v}_{j}$ maximizes $\mathbf{v}^{2}$ on $\operatorname{Hull}\left(\mathfrak{C}_{j}\right)$. Finally, if the intersection form is degenerate on span $\left(\mathfrak{C}_{j}\right)$, choose $\mathbf{v}_{j} \in \operatorname{Hull}\left(\mathfrak{C}_{j}\right)$ to be a non-zero null vector, and consider a sequence of different possible $e_{j}$ converging to $\mathbf{v}_{j}$. In this way, one obtains a sequence of choices of H for which $\max \left(\mathbf{a}^{+}\right)^{2} \rightarrow \sum\left(\mathbf{v}_{j}\right)^{2}=\beta^{2}(M)$. Hence $\alpha^{2} \leq \beta^{2} \leq \alpha^{2}$, and $\alpha^{2}(M)=\beta^{2}(M)$, as claimed. \(\square\)

This result gives a partial explanation of why $\alpha^{2}=\beta^{2}$ for the connected sums of complex surfaces we have considered, since the set of known monopole classes in this case constitutes a configuration of the described type, where the Lorentzian subspaces in question are given by $H^{1,1}$ of the various summands. Of course, this explanation still remains less than entirely satisfactory, since we cannot be absolutely certain that we currently have a full catalog of the monopole classes of these spaces.

Finally, let us point out that one cannot hope to prove that $\alpha^{2}=\beta^{2}$ if $\mathfrak{C}$ is simply replaced with an arbitrary finite, centrally symmetric set in an arbitrary finite-dimensional vector space with indefinite inner product. For example, let us just consider $\mathbb{R}^{3}$ equipped with the (++-) inner product $d x^{2}+d y^{2}-d z^{2}$, and consider the candidate for " $\mathfrak{C}$ " given by
$$\left\{ \pm(1,0,1), \pm\left(\frac{\sqrt{3}}{2},-\frac{1}{2}, 1\right), \pm\left(-\frac{\sqrt{3}}{2},-\frac{1}{2}, 1\right)\right\},$$
![](https://cdn.mathpix.com/cropped/872f37ef-b582-461d-a64c-f843b7540c84-36.jpg?height=372&width=299&top_left_y=1808&top_left_x=924)
Because the elements of this configuration " $\mathfrak{C}$ " are all null vectors, one can use Proposition 5.8 "upside-down" to show that " $\alpha^{2}$ " must then equal 1.

On the other hand, a simple symmetry argument shows that " $\beta^{2}$ " equals $\frac{3}{4}$ for this configuration. Of course, this this choice of " $\mathfrak{C}^{\prime \prime}$ does not consist of integer points, but one can easily remedy this by rational approximation and rescaling.

The upshot is that while one definitely has $\alpha^{2}(M)=\beta^{2}(M)$ for a remarkably large and interesting array of examples, this statement can generally hold only to the degree that the set $\mathfrak{C}$ of monopole classes satisfies some manifestly non-trivial geometric constraints. The precise extent to which these constraints hold or fail remains to be determined. It is hoped that some interested reader will find the challenge of fully fathoming this mystery both stimulating and fruitful.

\section*{References}
\begin{itemize}
\item[] [1] N. Aronszajn, A. Krzywicki, and J. Szarski, A unique continuation theorem for exterior differential forms on Riemannian manifolds, Ark. Mat., 4 (1962), pp. 417-453 (1962).
\item[] [2] T. Aubin, Some Nonlinear Problems in Riemannian Geometry, Springer Monographs in Mathematics, Springer-Verlag, Berlin, 1998.
\item[] [3] C. Bär, On nodal sets for Dirac and Laplace operators, Comm. Math. Phys., 188 (1997), pp. 709-721.
\item[] [4] S. Bauer, A stable cohomotopy refinement of Seiberg-Witten invariants. II, Invent. Math., 155 (2004), pp. 21-40.
\item[] [5] S. Bauer and M. Furuta, A stable cohomotopy refinement of Seiberg-Witten invariants. I, Invent. Math., 155 (2004), pp. 1-19.
\item[] [6] A. Besse, Einstein Manifolds, Springer-Verlag, 1987.
\item[] [7] D. E. Blair, The "total scalar curvature" as a symplectic invariant and related results, in Proceedings of the 3rd Congress of Geometry (Thessaloniki, 1991), Thessaloniki, 1992, Aristotle Univ. Thessaloniki, pp. 79-83.
\item[] [8] J.-P. Bourguignon, Les variétés de dimension 4 à signature non nulle dont la courbure est harmonique sont d'Einstein, Invent. Math., 63 (1981), pp. 263-286.
\end{itemize}
[9] S. K. Donaldson, Connections, cohomology and the intersection forms of 4-manifolds, J. Differential Geom., 24 (1986), pp. 275-341.
[10] T. C. Drăghici, On some 4-dimensional almost Kähler manifolds, Kodai Math. J., 18 (1995), pp. 156-168.
[11] D. T. Gay and R. Kirby, Constructing symplectic forms on 4manifolds which vanish on circles, Geom. Topol., 8 (2004), pp. 743-777 (electronic).
[12] D. Gilbarg and N. S. Trudinger, Elliptic Partial Differential Equations of Second Order, Springer-Verlag, Berlin, second ed., 1983.
[13] M. Gromov and H. B. Lawson, The classification of simply connected manifolds of positive scalar curvature, Ann. Math., 111 (1980), pp. 423-434.
[14] F. Hirzebruch and H. Hopf, Felder von Flächenelementen in 4dimensionalen Mannigfaltigkeiten, Math. Ann., 136 (1958), pp. 156-172.
[15] N. Hitchin, Harmonic spinors, Advances in Mathematics, 14 (1974), pp. 1-55.
[16] M. Ishida and C. LeBrun, Curvature, connected sums, and Seiberg-Witten theory, Comm. Anal. Geom., 11 (2003), pp. 809-836.
[17] T. P. Killingback and E. G. Rees, Spin ${ }^{c}$ structures on manifolds, Classical Quantum Gravity, 2 (1985), pp. 433-438.
[18] N. Koiso, A decomposition of the space $\mathcal{M}$ of Riemannian metrics on a manifold, Osaka J. Math., 16 (1979), pp. 423-429.
[19] P. B. Kronheimer, Minimal genus in $S^{1} \times M^{3}$, Invent. Math., 135 (1999), pp. 45-61.
[20] P. B. Kronheimer and T. S. Mrowka, Scalar curvature and the Thurston norm, Math. Res. Lett., 4 (1997), pp. 931-937.
[21] H. B. Lawson and M. Michelsohn, Spin Geometry, Princeton University Press, 1989.
[22] C. LeBrun, Einstein metrics and Mostow rigidity, Math. Res. Lett., 2 (1995), pp. 1-8.
[23] _, Polarized 4-manifolds, extremal Kähler metrics, and Seiberg-Witten theory, Math. Res. Lett., 2 (1995), pp. 653-662.
[24] -, Four-manifolds without Einstein metrics, Math. Res. Lett., 3 (1996), pp. 133-147.
[25] _, Ricci curvature, minimal volumes, and Seiberg-Witten theory, Inv. Math., 145 (2001), pp. 279-316.
[26] __, Einstein metrics, four-manifolds, and differential topology, in Surveys in differential geometry, Vol. VIII (Boston, MA, 2002), Surv. Differ. Geom., VIII, Int. Press, Somerville, MA, 2003, pp. 235-255.
[27] -, Einstein metrics, symplectic minimality, and pseudo-holomorphic curves, Ann. Global Anal. Geom., 28 (2005), pp. 157-177.
[28] A. Lichnerowicz, Spineurs harmoniques, C.R. Acad. Sci. Paris, 257 (1963), pp. 7-9.
[29] R. Penrose and W. Rindler, Spinors and space-time. Vol. 1, Cambridge University Press, Cambridge, 1984. Two-spinor calculus and relativistic fields.
[30] C. H. Taubes, The Seiberg-Witten invariants and symplectic forms, Math. Res. Lett., 1 (1994), pp. 809-822.
[31] E. Witten, Monopoles and four-manifolds, Math. Res. Lett., 1 (1994), pp. 809-822.
