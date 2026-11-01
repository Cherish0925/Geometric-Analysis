---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Kähler-Ricci flow, Ricci-flat metrics and collapsing limits]

---
source_file: 1408_0161.pdf
converter: mathpix
format: mmd
---

\title{
THE KÄHLER-RICCI FLOW, RICCI-FLAT METRICS AND COLLAPSING LIMITS
}

\author{
VALENTINO TOSATTI, BEN WEINKOVE, AND XIAOKUI YANG
}

\begin{abstract}
We investigate the Kähler-Ricci flow on holomorphic fiber spaces whose generic fiber is a Calabi-Yau manifold. We establish uniform metric convergence to a metric on the base, away from the singular fibers, and show that the rescaled metrics on the fibers converge to Ricci-flat Kähler metrics. This strengthens previous work of Song-Tian and others. We obtain analogous results for degenerations of Ricci-flat Kähler metrics.
\end{abstract}

\section*{1. Introduction}
1.1. Background. This paper establishes convergence results for collapsing metrics along the Kähler-Ricci flow and along families of Ricci-flat Kähler metrics. We give now some background and motivation for these results, glossing over some technicalities for the moment.

Let $X$ be a compact Kähler manifold, and suppose we have a holomorphic surjective map $\pi: X \rightarrow B$ onto another compact Kähler manifold $B$, with $0<\operatorname{dim} B<\operatorname{dim} X$. We consider a family of Kähler metrics $(\omega(t))_{t \in[0, \infty)}$ on $X$ with the property that the cohomology classes $[\omega(t)] \in H^{1,1}(X, \mathbb{R})$ have the limiting behavior:
$$[\omega(t)] \rightarrow \pi^{*} \alpha, \quad \text { in } H^{1,1}(X, \mathbb{R}),$$
where $\alpha$ is a Kähler class on $B$. Moreover, we suppose that the Kähler metrics $\omega(t)$ solve one of the two natural PDEs: the Kähler-Ricci flow or the Calabi-Yau equation. Note that from topological considerations, the metrics $\omega(t)$ are automatically volume collapsing, meaning that
$$\int_{X} \omega(t)^{\operatorname{dim} X}=[\omega(t)]^{\operatorname{dim} X} \rightarrow 0, \quad \text { as } t \rightarrow \infty,$$
since $B$ has dimension strictly less than $\operatorname{dim} X$.
A natural question is: does $(X, \omega(t))$ converge to $\left(B, \omega_{B}\right)$, where $\omega_{B}$ is a unique canonical metric in the class $\alpha$ ?

In the cases we consider, the existence of the "canonical metric" has already been established, and the remaining point is to establish convergence in the strongest possible sense. There are weak notions of convergence, such as convergence of $\omega(t)$ to $\omega_{B}$ as currents, or convergence at the level of Kähler

\footnotetext{
Research supported in part by NSF grants DMS-1308988, DMS-1332196 and DMS-1406164. The first-named author is supported in part by a Sloan Research Fellowship.
}
potentials in $C^{1, \alpha}$, say, for $\alpha \in(0,1)$. A stronger notion of convergence is convergence of $\omega(t)$ to $\omega_{B}$ in the $C^{0}$ norm. This kind of convergence implies global Gromov-Hausdorff convergence. The main point of this paper is that we can obtain, in many cases, convergence of the stronger type when before only weaker convergence was known.

To be more explicit, we discuss now the simplest case of such collapsing for the Kähler-Ricci flow, which is already completely understood. Let $X$ be a product $X=E \times B$ where $B$ is a compact Riemann surface of genus larger than 1 and $E$ is a one-dimensional torus (an elliptic curve). We consider the Kähler-Ricci flow [21, 6]
$$\frac{\partial}{\partial t} \omega=-\operatorname{Ric}(\omega)-\omega,\left.\quad \omega\right|_{t=0}=\omega_{0},$$
starting at an arbitrary initial Kähler metric $\omega_{0}$ on $X$. A solution to (1.1) exists for all time [51]. Note that (1.1) is really the normalized Kähler-Ricci flow. It has the property that as $t \rightarrow \infty$ the Kähler classes $[\omega(t)] \in$ $H^{1,1}(X, \mathbb{R})$ converge to the class $\pi^{*} \alpha$ where $\alpha=\left[\omega_{B}\right]$, for $\omega_{B}$ the unique Kähler-Einstein metric on $B$ satisfying
$$\operatorname{Ric}\left(\omega_{B}\right)=-\omega_{B} .$$
Here $\pi: X \rightarrow B$ is the projection map.
This example was first studied by Song-Tian [39] who considered the much more general situation of a holomorphic fiber space $\pi: X \rightarrow B$ of Kodaira dimension one, whose generic fibers are elliptic curves. For the product $X=E \times B$, the results of [39, 45, 15, 12] show that one obtains $C^{\infty}$ convergence of $\omega(t)$ to $\omega_{B}$. Moreover, the curvature of $\omega(t)$ and its covariant derivatives remain bounded as $t \rightarrow \infty$. Geometrically, the metrics shrink in the directions of $E$ and we obtain convergence to the Kähler-Einstein metric $\omega_{B}$ on $B$. Moreover, if we look at the evolving metrics restricted to any given fiber $E$ and rescale appropriately, they converge to a flat metric on $E$.

A natural generalization of this result is to consider $X=E \times B$ where now $E$ is a Calabi-Yau manifold (i.e. $c_{1}(E)=0$ in $H^{1,1}(E, \mathbb{R})$ ) and $B$ is a compact Kähler manifold with $c_{1}(B)<0$. The behavior of the Kähler-Ricci flow on the manifolds $E$ and $B$ separately is well-known by the results of Cao [6]: on $E$ the unnormalized Kähler-Ricci flow $\frac{\partial}{\partial t} \omega=-\operatorname{Ric}(\omega)$ converges to a Kähler Ricci-flat metric, and on $B$ the normalized Kähler-Ricci flow (1.1) converges to the unique Kähler-Einstein metric satisfying (1.2). However, the behavior of the flow on the product $X=E \times B$ is in general harder to understand than the two-dimensional example above. A source of difficulty is that, except in dimension one, Calabi-Yau manifolds may not admit flat metrics.

In the case when $E$ does admit a flat Kähler metric, it was shown by Gill [15], Fong-Zhang [12] that the same results hold as in the case of a product of Riemann surfaces. In particular, the curvature remains bounded along the flow. These methods fail for a general $E$. Indeed, by starting the flow
at a product of a non-flat Ricci-flat metric on $E$ with a Kähler-Einstein metric on $B$, it is easy to check that the curvature along the Kähler-Ricci flow (1.1) must blow up. One can still obtain "weak" convergence of the metrics [40, 12]. Indeed, the evolving metrics along the flow are comparable to the "model" collapsing metrics, which implies in particular that the fibers shrink and one obtains convergence to $\omega_{B}$ at the level of potentials in the $C^{1, \alpha}$ norm. However, until now the question of whether the metrics $\omega(t)$ converge (in $C^{0}$ say) to $\omega_{B}$ has remained open.

Our results show that in fact the metrics $\omega(t)$ converge exponentially fast in the $C^{0}$ norm to $\omega_{B}$, which implies in particular Gromov-Hausdorff convergence of $(X, \omega(t))$ to $\left(B, \omega_{B}\right)$. Moreover, we show that if one restricts to a fiber $E$ over $y \in B$ then the metrics $\omega(t)$, appropriately rescaled, converge exponentially fast to a Ricci-flat Kähler metric on $E$ and this convergence is uniform in $y$. All of these statements are new in this setting, and require new estimates, which we explain later.

Of course, the assumption that $X$ is a product is rather restrictive. In fact, the same results hold when $\pi: X \rightarrow B$ is a holomorphic submersion, except that the Kähler-Einstein equation (1.2) is replaced by the twisted Kähler-Einstein equation [39, 40, 11]. But even this is not sufficiently general, since we also need to allow $\pi: X \rightarrow B$ to admit singular fibers, and for $B$ itself to be possibly singular. More precisely, we assume that $\pi: X \rightarrow B$ is a fiber space, namely a surjective holomorphic map with connected fibers, and $B$ is an irreducible normal projective variety. In this case we obtain the same metric convergence results on compact subsets away from the singular fibers (but this time not exponential). Again it was only known before that convergence occurs at the level of potentials [40].

The latter situation is really quite general. Indeed, if one believes the Abundance Conjecture from algebraic geometry (that on a compact Kähler manifold the canonical bundle $K_{X}$ is nef implies $K_{X}$ is semiample) then whenever the Kähler-Ricci flow has a long-time solution, there exists such a fiber space map $\pi: X \rightarrow B$. For the above discussion to apply, we also need to remove the two extreme cases: when $B$ has dimension 0 or $\operatorname{dim} X$. In the first case $X$ is Calabi-Yau and it is known by the work of Cao [6] that the Kähler-Ricci flow (unnormalized) converges smoothly to Yau's Ricci-flat Kähler metric [62]. In the second case $X$ is of general type (in particular, $X$ is projective), and the normalized Kähler-Ricci flow converges to a Kähler-Einstein current on $X$ [61, 51, 65], smoothly away from a subvariety.

On a general projective variety $X$, the Kähler-Ricci flow may encounter finite time singularities. According to the analytic minimal model program [39, 50, 40, 42] the Kähler-Ricci flow will perform a surgery at each finite time singularity, corresponding to a birational operation of the minimal model program from algebraic geometry, and arrive at the minimal model $X_{\text {min }}$ with nef canonical bundle (see also [5, 9, 10, 12, 26, 36, 38, 41, 43, 44, 46, 47, 51, 61]). It is then expected that the flow on $X_{\text {min }}$ will converge at infinity to a canonical metric on the lower dimensional canonical model
$X_{\text {can }}$. Our results here are concerned with a special case of this last step, where $X_{\text {min }}=X$ is smooth with semiample canonical bundle and $X_{\text {can }}$ is what we call $B$.

Finally, we discuss the Ricci-flat Kähler metrics. A similar situation arises here, where one considers a Calabi-Yau manifold $X$ which admits a holomorphic fiber space structure $\pi: X \rightarrow B$ as above (possibly with singular fibers and with $B$ singular), and studies the collapsing behavior of the Ricciflat Kähler metrics $\omega(t)$ in the class $\left[\pi^{*} \chi\right]+e^{-t}\left[\omega_{X}\right]$ (where $\omega_{X}$ is a Kähler metric on $X$ and $\chi$ on $B$ ), as $t$ tends to infinity. Again one expects to have collapsing to a canonical Kähler metric $\omega_{B}$ on $B \backslash S^{\prime}$ (where $S^{\prime}$ denotes the singularities of $B$ together with the images of the singular fibers). Furthermore, one would like to understand if a Gromov-Hausdorff limit $\left(X_{\infty}, d_{\infty}\right)$ of $(X, \omega(t))$ exists (without passing to subsequences), whether it is sufficiently regular, and how it is related to $\left(B \backslash S^{\prime}, \omega_{B}\right)$. It is expected [55, 56] that $\left(X_{\infty}, d_{\infty}\right)$ contains an open and dense subset which is a smooth Riemannian manifold, that $\left(X_{\infty}, d_{\infty}\right)$ is isometric to the metric completion of $\left(B \backslash S^{\prime}, \omega_{B}\right)$, and that $X_{\infty}$ is homeomorphic to $B$. By comparison, in the case when the volume of the Ricci-flat metrics is non-collapsing, we have a very thorough understanding of their limiting behavior, thanks to the results in [8, 31, 32, 33, 37, 53], and all the analogous questions have affirmative answers.

This setup is also related to the Strominger-Yau-Zaslow picture of mirror symmetry [48]. Indeed, Kontsevich-Soibelman [25], Gross-Wilson [20] and Todorov (see [28, p. 66]) formulated a conjecture about certain collapsed limits of Ricci-flat Kähler metrics on Calabi-Yau manifolds, where the Kähler class is fixed but the complex structure degenerates (to a socalled large complex structure limit). This might seem very different from what we are considering here, where the complex structure is fixed and the Kähler class degenerates, but in the case when the Calabi-Yau manifolds are actually hyperkähler, one may perform a hyperkähler rotation and often reduce this conjecture to studying the collapsed limits of Ricci-flat metrics in the precise setup of Theorem 1.3 (see [18]), although in this case the smooth fibers are always tori. This approach was pioneered by Gross-Wilson [20], who solved this conjecture for certain elliptically fibered $K 3$ surfaces (see also the discussion after Theorem 1.3).

Going back to our discussion, our new results imply that the Ricci-flat metrics $\omega(t)$ converge in the $C^{0}$ norm to $\pi^{*} \omega_{B}$ on compact sets away from the singular fibers, improving earlier results of the first-named author [54] who proved weak convergence as currents and in the $C^{1, \alpha}$ norm of potentials. Also, the rescaled metrics along the fibers converge to Ricci-flat metrics. Furthermore, we are able to show in Corollary 1.4 that any Gromov-Hausdorff limit contains an open and dense subset which is a smooth Riemannian manifold (this fact in itself is quite interesting and does not follow from the general structure theory of Cheeger-Colding [7]). These new results solve some questions in [55, 56].
1.2. Metric collapsing along Kähler-Ricci flow. Let $\left(X, \omega_{0}\right)$ be a compact Kähler manifold with canonical bundle $K_{X}$ semiample. By definition this means that there exists $\ell \geqslant 1$ such that the line bundle $K_{X}^{\ell}$ is globally generated. If we choose $\ell$ sufficiently large and divisible, the sections in $H^{0}\left(X, K_{X}^{\ell}\right)$ give a holomorphic map to projective space, with image $B$ an irreducible normal projective variety, and we obtain a surjective holomorphic map $\pi: X \rightarrow B$ with connected fibers (see e.g. [27, Theorem 2.1.27]). The dimension of $B$ is the Kodaira dimension of $X$, written $\kappa(X)$. We assume $0<\kappa(X)<\operatorname{dim} X$.

We let $m=\kappa(X)=\operatorname{dim} B$ and $n+m=\operatorname{dim} X$. The generic fiber $X_{y}=\pi^{-1}(y)$ of $\pi$ has $K_{X_{y}}^{\ell}$ holomorphically trivial, so it is a Calabi-Yau manifold of dimension $n$.

We first consider a special case, where some technicalities disappear and for which our results are stronger. Assume:
$$\begin{aligned}
& \pi: X \rightarrow B \text { is a holomorphic submersion onto } \\
& \text { a compact Kähler manifold } B \text { with } c_{1}(B)<0, \\
& \text { with fibers Calabi-Yau manifolds. }
\end{aligned}$$
As we will see in Section 2, this assumption implies that the canonical bundle of $X$ is semiample. In this case, all the fibers $X_{y}=\pi^{-1}(y)$ are Calabi-Yau manifolds of dimension $n$ (there are no singular fibers). Song-Tian [40] (see also [11]) showed that $B$ admits a unique smooth twisted Kähler-Einstein metric $\omega_{B}$ solving
$$\operatorname{Ric}\left(\omega_{B}\right)=-\omega_{B}+\omega_{\mathrm{WP}},$$
where $\omega_{\mathrm{WP}}$ is the Weil-Petersson form on $B$ (see Section 2.1 below). We will often write $\omega_{B}$ for $\pi^{*} \omega_{B}$.

By Yau's theorem [62], each of the fibers $X_{y}$ of $\pi: X \rightarrow B$ admits a unique Ricci-flat Kähler metric cohomologous to $\left.\omega_{0}\right|_{X_{y}}$. Write $\omega_{\text {SRF }, y}$ for this metric on $X_{y}$. To explain this notation: later we will define a semi Ricci-flat form $\omega_{\mathrm{SRF}}$ on $X$ which restricts to $\omega_{\mathrm{SRF}, y}$ on $X_{y}$.

Our first result concerns the normalized Kähler-Ricci flow
$$\frac{\partial}{\partial t} \omega=-\operatorname{Ric}(\omega)-\omega, \quad \omega(0)=\omega_{0},$$
on $X$, starting at $\omega_{0}$. We show that in this case we obtain exponentially fast metric collapsing of $(X, \omega(t))$ to $\left(B, \omega_{B}\right)$ along the Kähler-Ricci flow.

Theorem 1.1. Let $\omega=\omega(t)$ be the solution of the Kähler-Ricci flow (1.4) on $X$ satisfying assumption (*). Then the following hold:
\begin{itemize}
\item[(i)] As $t \rightarrow \infty, \omega$ converges exponentially fast to $\omega_{B}$. Namely, there exist positive constants $C, \eta>0$ such that
\end{itemize}
$$\left\|\omega-\omega_{B}\right\|_{C^{0}\left(X, \omega_{0}\right)} \leqslant C e^{-\eta t}, \quad \text { for all } t \geqslant 0 .$$
\begin{itemize}
\item[(ii)] The rescaled metrics $\left.e^{t} \omega\right|_{X_{y}}$ converge exponentially fast to $\omega_{\mathrm{SRF}, y}$ on each fiber $X_{y}$, uniformly in $y$. Namely, there exist positive constants
\end{itemize}
$C, \eta>0$ such that
$$\left\|\left.e^{t} \omega\right|_{X_{y}}-\omega_{\mathrm{SRF}, y}\right\|_{C^{0}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \leqslant C e^{-\eta t}, \quad \text { for all } t \geqslant 0, y \in B .$$
Moreover, if we fix $\alpha \in(0,1)$ then for each $y \in B,\left.e^{t} \omega\right|_{X_{y}}$ converges to $\omega_{\mathrm{SRF}, y}$ in $C^{\alpha}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)$.
(iii) As $t \rightarrow \infty,(X, \omega)$ converges in the Gromov-Hausdorff sense to $\left(B, \omega_{B}\right)$.

Next, we consider the general case of $\left(X, \omega_{0}\right)$ with canonical bundle $K_{X}$ semiample and $0<\kappa(X)<\operatorname{dim} X$. As above, we have a surjective holomorphic map $\pi: X \rightarrow B$ with connected fibers (i.e. a fiber space), but now $B$ is only an irreducible normal projective variety (possibly singular). In addition, $\pi$ may have critical values. If $S^{\prime} \subset B$ denotes the singular set of $B$ together with the set of critical values of $\pi$, and we define $S=\pi^{-1}\left(S^{\prime}\right)$, then $S^{\prime}$ is a proper analytic subvariety of $B, S$ is a proper analytic subvariety of $X$, and $\pi: X \backslash S \rightarrow B \backslash S^{\prime}$ is a submersion between smooth manifolds. Therefore all fibers $X_{y}=\pi^{-1}(y)$ with $y \in B \backslash S^{\prime}$ are smooth $n$-folds (all diffeomorphic to each other) with torsion canonical bundle.

As shown in [40, Theorem 3.1], there is a smooth Kähler metric $\omega_{B}$ on $B \backslash S^{\prime}$ satisfying the twisted Kähler-Einstein equation
$$\operatorname{Ric}\left(\omega_{B}\right)=-\omega_{B}+\omega_{\mathrm{WP}}, \quad \text { on } B \backslash S^{\prime},$$
for $\omega_{\mathrm{WP}}$ the (smooth) Weil-Petersson form on $B \backslash S^{\prime}$. For $y \in B \backslash S^{\prime}$, let $\omega_{\mathrm{SRF}, y}$ be the unique Ricci-flat Kähler metric on the fiber $X_{y}$ cohomologous to $\left.\omega_{0}\right|_{X_{y}}$.

Our result is that, in this more general setting, we obtain metric collapsing of the normalized Kähler-Ricci flow $\omega(t)$ to $\omega_{B}$ on compact subsets away from the singular set $S$.

Theorem 1.2. Let $\omega=\omega(t)$ be the solution of the Kähler-Ricci flow (1.4) on $X$. Then the following hold:
\begin{itemize}
\item[(i)] For each compact subset $K \subset X \backslash S$,
$$\left\|\omega-\omega_{B}\right\|_{C^{0}\left(K, \omega_{0}\right)} \rightarrow 0, \quad \text { as } t \rightarrow \infty .$$
\item[(ii)] The rescaled metrics $\left.e^{t} \omega\right|_{X_{y}}$ converge to $\omega_{\mathrm{SRF}, y}$ on each fiber $X_{y}$ uniformly in $y$ for compact subsets of $B \backslash S^{\prime}$. Namely, for each compact set $K^{\prime} \subset B \backslash S^{\prime}$
$$\sup _{y \in K^{\prime}}\left\|\left.e^{t} \omega\right|_{X_{y}}-\omega_{\mathrm{SRF}, y}\right\|_{C^{0}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \rightarrow 0, \quad \text { as } t \rightarrow \infty .$$
Moreover, if we fix $\alpha \in(0,1)$ then for each $y \in B \backslash S^{\prime},\left.e^{t} \omega\right|_{X_{y}}$ converges to $\omega_{\mathrm{SRF}, y}$ in $C^{\alpha}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)$.
\end{itemize}

An interesting, but still open, question is whether the convergence results of Theorems 1.1 and 1.2 hold with the $C^{0}$ norms replaced by the $C^{\infty}$ norms. This was conjectured by Song-Tian [39] in the case of elliptic surfaces. Moreover, one expects the convergence to be always exponentially fast. Smooth
convergence has indeed been proved by Fong-Zhang [12] in the case when the smooth fibers are tori, adapting the techniques of Gross-Tosatti-Zhang [18] for Calabi-Yau metrics.
1.3. Collapsing of Ricci-flat metrics. Let $X$ be a compact Kähler ( $n+$ $m$ )-manifold with $c_{1}(X)=0$ in $H^{2}(X, \mathbb{R})$ (i.e. a Calabi-Yau manifold), and let $\omega_{X}$ be a Ricci-flat Kähler metric on $X$. Suppose that we have a holomorphic map $\pi: X \rightarrow Z$ with connected fibers, where $\left(Z, \omega_{Z}\right)$ is a compact Kähler manifold, with image $B=\pi(X) \subset Z$ an irreducible normal subvariety of $Z$ of dimension $m>0$. Then the induced surjective map $\pi: X \rightarrow B$ is a fiber space, and if $S^{\prime} \subset B$ denotes the singular set of $B$ together with the set of critical values of $\pi$, and $S=\pi^{-1}\left(S^{\prime}\right)$, then $S^{\prime}$ is a proper analytic subvariety of $B, S$ is a proper analytic subvariety of $X$, and $\pi: X \backslash S \rightarrow B \backslash S^{\prime}$ is a submersion between smooth manifolds. This is the same setup as in [54, 18, 19, 22]. The manifold $Z$ here plays only an auxiliary role, and in practice there are two natural choices for $Z$, namely $Z=B$ if $B$ is smooth, or $Z=\mathbb{C P}^{N}$ if $B$ is a projective variety (like in the setup of the Kähler-Ricci flow).

The fibers $X_{y}=\pi^{-1}(y)$ with $y \in B \backslash S^{\prime}$ are smooth Calabi-Yau $n$-folds (all diffeomorphic to each other). As in the previous section, we write $\omega_{\text {SRF }, y}$ for the unique Ricci-flat Kähler metric on $X_{y}$ cohomologous to $\left.\omega_{X}\right|_{X_{y}}$, for $y \in B \backslash S^{\prime}$.

Write $\chi=\pi^{*} \omega_{Z}$, which is a smooth nonnegative $(1,1)$ form on $X$. Then the cohomology class
$$\alpha_{t}=[\chi]+e^{-t}\left[\omega_{X}\right], \quad 0 \leqslant t<\infty,$$
is Kähler. By Yau's Theorem [62] there exists a unique Ricci-flat Kähler metric $\omega=\omega(t) \in \alpha_{t}$ on $X$. On the other hand, the class $[\chi]$ is not Kähler and hence the family of metrics $\omega(t)$ must degenerate as $t \rightarrow \infty$.

Note that in [54, 18, 19, 22] the class $\alpha_{t}$ was replaced by $[\chi]+t\left[\omega_{X}\right], 0<$ $t \leqslant 1$. This is of course only a cosmetic difference, which we have made to highlight the similarity between this setup and the one considered above for the Kähler-Ricci flow.

There is a Kähler metric $\omega_{B}=\chi+\sqrt{-1} \partial \bar{\partial} v$ on $B \backslash S^{\prime}$, for $v$ a unique solution of a certain complex Monge-Ampère equation (see (4.1)) such that
$$\operatorname{Ric}\left(\omega_{B}\right)=\omega_{\mathrm{WP}} \quad \text { on } B \backslash S^{\prime},$$
where $\omega_{\mathrm{WP}}$ is the Weil-Petersson form.
We prove that the Ricci-flat metrics $\omega \in \alpha_{t}$ collapse as $t \rightarrow \infty$. Note that the limiting behavior of these metrics is similar to solutions of the Kähler-Ricci flow in Theorem 1.2 above.

Theorem 1.3. Let $\omega=\omega(t) \in \alpha_{t}$ be Ricci-flat Kähler metrics on $X$ as described above. Then the following hold:
\begin{itemize}
\item[(i)] For each compact set $K \subset X \backslash S$,
$$\left\|\omega-\omega_{B}\right\|_{C^{0}\left(K, \omega_{0}\right)} \rightarrow 0, \quad \text { as } t \rightarrow \infty .$$
\end{itemize}
\begin{itemize}
\item[(ii)] The rescaled metrics $\left.e^{t} \omega\right|_{X_{y}}$ converge to $\omega_{\mathrm{SRF}, y}$ on each fiber $X_{y}$ uniformly in $y$ for compact subsets of $B \backslash S^{\prime}$. Namely, for each compact set $K^{\prime} \subset B \backslash S^{\prime}$,
$$\sup _{y \in K^{\prime}}\left\|\left.e^{t} \omega\right|_{X_{y}}-\omega_{\mathrm{SRF}, y}\right\|_{C^{0}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \rightarrow 0, \quad \text { as } t \rightarrow \infty .$$
Furthermore, if we fix $\alpha \in(0,1)$ then for each $y \in B \backslash S^{\prime},\left.e^{t} \omega\right|_{X_{y}}$ converges to $\omega_{\mathrm{SRF}, y}$ in $C^{\alpha}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)$.
\end{itemize}

The statement that $\left.e^{t} \omega\right|_{X_{y}} \rightarrow \omega_{\text {SRF }, y}$ (which can be improved to the smooth topology [60]) solves [55, Question 4.1] and [56, Question 3]. As in the case of the Kähler-Ricci flow, it remains an interesting open question (cf. [55, Question 4.2], [56, Question 4]) whether the collapsing in (1.9) is in the smooth topology.

Theorem 1.3 was first proved by Gross-Wilson [20] in the case when $X$ is a $K 3$ surface, $B$ is $\mathbb{C P}^{1}$ and the only singular fibers of $\pi$ are of type $I_{1}$. In fact they also proved that the collapsing in (1.9) is in the smooth topology. Their proof is of a completely different flavor, constructing explicit almost Ricci-flat metrics on $X$ by gluing $\omega_{B}+e^{-t} \omega_{\text {SRF }}$ away from $S$ with a suitable model metric near the singularities, and then perturbing this to the honest Ricci-flat metrics $\omega(t)$ (for $t$ large). In higher dimensions when there are no singular fibers $(S=\emptyset)$ a similar perturbation result was obtained by Fine [11]. However it seems hopeless to pursue this strategy in higher dimensions when there are singular fibers, since in general there is no good local model metric near the singularities. Note that such fibrations with $S=\emptyset$ are very special, thanks to the results in [59].

In [39, Theorem 7.1] Song-Tian took a different approach, and by proving a priori estimates for the Ricci-flat metrics $\omega(t)$ they showed that they collapse to $\omega_{B}$ in the $C^{1, \alpha}$ topology of Kähler potentials $(0<\alpha<1)$, in the case when $X$ is $K 3$ and $B$ is $\mathbb{C P}^{1}$. This was generalized to all dimensions by the first-named author in [54], who also proved that the fibers shrink in the $C^{1}$ topology of metrics.

When $X$ is projective and the smooth fibers $X_{y}$ are tori, Theorem 1.3 was proved by Gross-Tosatti-Zhang in [18], together with the improvement of (1.9) to the smooth topology. The projectivity assumption was recently removed in [22]. In this case (and only in this case) the Ricci-flat metrics also have locally uniformly bounded sectional curvature on $X \backslash S$. The assumption that the smooth fibers are tori is used crucially to derive higher-order estimates for the pullback of $\omega$ to the universal cover of $\pi^{-1}(U)$, which is biholomorphic to $U \times \mathbb{C}^{n}$, where $U$ is a small ball in $B \backslash S^{\prime}$. It is unclear how to obtain similar estimates in our general setup.

In the setup of Theorem 1.3 we can also derive some consequences about Gromov-Hausdorff limits of the Calabi-Yau metrics $\omega(t)$. In fact, given the uniform convergence proved in (1.9), we can directly apply existing arguments in the literature. For example, using the arguments in [18, Theorem 1.2] we obtain the following corollary.

Corollary 1.4. Assume the same setup as above, and let $\left(X_{\infty}, d_{\infty}\right)$ be a metric space which is the Gromov-Hausdorff limit of $\left(X, \omega\left(t_{i}\right)\right)$ for some sequence $t_{i} \rightarrow \infty$. Then there is an open dense subset $X_{0} \subset X_{\infty}$ and a homeomorphism $\phi: B \backslash S^{\prime} \rightarrow X_{0}$ which is a local isometry between $\left(B \backslash S^{\prime}, \omega_{B}\right)$ and $\left(X_{0}, d_{\infty}\right)$. In particular, $\left(X_{\infty}, d_{\infty}\right)$ has an open dense subset which is a smooth Riemannian manifold.

Similarly, the arguments in [19, Theorem 1.1] give:
Corollary 1.5. Assume furthermore that $X$ is projective and $B$ is a smooth Riemann surface. Then $(X, \omega(t))$ have a Gromov-Hausdorff limit $\left(X_{\infty}, d_{\infty}\right)$ as $t \rightarrow \infty$, which is isometric to the metric completion of $\left(B \backslash S^{\prime}, \omega_{B}\right)$ and $X_{\infty}$ is homeomorphic to $B$. Lastly, $X_{\infty} \backslash X_{0}$ is a finite number of points.

This answers questions in [19, 55, 56], in this setup.
1.4. Remarks on the proofs. We end the introduction by describing briefly some key elements in the proofs. For simplicity of the discussion, suppose that $X$ is a product $X=E \times B$ with $\omega_{E}$ a Ricci-flat metric on $E$ and $\omega_{B}$ a Kähler-Einstein metric on $B$, and assume that $\omega_{0}$ is cohomologous to the product metric. Write $\tilde{\omega}=\omega_{B}+e^{-t} \omega_{E}$. It is already known [12] that $\omega$ and $\tilde{\omega}$ are uniformly equivalent. Our goal is to show that $\|\omega-\tilde{\omega}\|_{C^{0}\left(X, \omega_{0}\right)}$ converges to zero. We first show that (cf. Lemma 2.2.(iv))
$$\frac{\omega^{n+m}}{\tilde{\omega}^{n+m}} \rightarrow 1, \quad \text { as } t \rightarrow \infty,$$
exponentially fast. In fact this statement is easily derived from existing arguments in the literature [39, 40, 45, 41, 58].

The next step is the estimate (Lemma 2.8)
$$\operatorname{tr}_{\omega} \omega_{B}-m \leqslant C e^{-\eta t},$$
for uniform positive constants $C$ and $\eta$. This uses a maximum principle argument similar to that in the authors' recent work [58, Proposition 7.3] on the Chern-Ricci flow [14, 57]. Indeed, [58] established in particular exponential convergence of solutions to the Kähler-Ricci flow on elliptic surfaces and, as we show here, these ideas can be applied here for the case of more general Calabi-Yau fibers.

Finally, we have a Calabi-type estimate in the fibers $X_{y}$ for $y \in B$ (Lemma 2.9) which gives
$$\left\|\left.e^{t} \omega\right|_{X_{y}}\right\|_{C^{1}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \leqslant C .$$

Then the exponential convergence of $\omega$ to $\omega_{B}$, and the other results of Theorem 1.1 are almost a formal consequence of the three estimates (1.11), (1.12), (1.13). When $X$ is a holomorphic submersion rather than a product, the analogous estimates still hold.

When $\pi: X \rightarrow B$ has singular fibers then there are a number of technical complications and in particular we are not able to obtain exponential convergence (see Lemma 3.1.(iv)). For the case of collapsing Ricci-flat Kähler metrics, there are even more difficulties. A parabolic maximum principle argument has to be replaced by a global argument using the Green's function and the diameter bound of [53, 64] (see Lemma 4.4). Nevertheless, the basic outlines of the proofs remain the same.

This paper is organized as follows. In Section 2 we study the collapsing of the Kähler-Ricci flow on holomorphic submersions, and prove Theorem 1.1. In Section 3 we deal with the case with singular fibers and prove Theorem 1.2. The collapsing of Ricci-flat metrics on Calabi-Yau manifolds is discussed in Section 4 where we give the proof of Theorem 1.3.

Acknowledgments. We are grateful to the referee for useful comments.

\section*{2. The Kähler-Ricci flow on a holomorphic submersion}

In this section, we give a proof of Theorem 1.1. We assume that $X$ satisfies assumption $(*)$ from the introduction.
2.1. Holomorphic submersions. We begin with some preliminary facts about submersions $\pi: X \rightarrow B$ satisfying (*) as in the introduction. The content of this section is essentially well-known (see e.g. [39, 40, 54, 12]). We include this brief account for the sake of completeness.

Let $\left(X^{n+m}, \omega_{0}\right)$ be a compact Kähler manifold which admits a submersion $\pi: X \rightarrow B$ onto a compact Kähler manifold $B^{m}$ with $c_{1}(B)<0$, and connected fibers $X_{y}=\pi^{-1}(y)$ which are all Calabi-Yau $n$-manifolds. Thanks to Yau's theorem [62], there is a smooth function $\rho_{y}$ on $X_{y}$ such that $\left.\omega_{0}\right|_{X_{y}}+\sqrt{-1} \partial \bar{\partial} \rho_{y}=\omega_{\text {SRF }, y}$ is the unique Ricci-flat Kähler metric on $X_{y}$ cohomologous to $\left.\omega_{0}\right|_{X_{y}}$. If we normalize by $\left.\int_{X_{y}} \rho_{y} \omega_{0}^{n}\right|_{X_{y}}=0$, then $\rho_{y}$ varies smoothly in $y$ and defines a smooth function $\rho$ on $X$ and we let
$$\omega_{\mathrm{SRF}}=\omega_{0}+\sqrt{-1} \partial \bar{\partial} \rho .$$
This is called a semi Ricci-flat form, because it restricts to a Ricci-flat Kähler metric on each fiber $X_{y}$. It was first introduced by Greene-Shapere-Vafa-Yau [16] in the context of elliptically fibered $K 3$ surfaces (in which case it is a semiflat form). Note that while $\omega_{\text {SRF }}$ need not be positive definite, nevertheless for any Kähler metric $\chi$ on $B$ we have that $\omega_{\text {SRF }}^{n} \wedge \pi^{*} \chi^{m}$ is a strictly positive volume form on $X$. Now recall that the relative pluricanonical bundle of $\pi$ is $K_{X / B}^{\ell}=K_{X}^{\ell} \otimes\left(\pi^{*} K_{B}^{\ell}\right)^{*}$, where $\ell$ is any positive integer. Thanks to the projection formula, we have
$$\pi_{*}\left(K_{X}^{\ell}\right)=\left(\pi_{*}\left(K_{X / B}^{\ell}\right)\right) \otimes K_{B}^{\ell},$$
and when restricted to any fiber $X_{y},\left.K_{X / B}^{\ell}\right|_{X_{y}} \cong K_{X_{y}}^{\ell}$. The fact that $X_{y}$ is Calabi-Yau implies that there is a positive integer $\ell$ such that $K_{X_{y}}^{\ell}$ is trivial,
for all $y \in B$, and from now on we fix such a value of $\ell$. Then Grauert's theorem on direct images [3, Theorem I.8.5] shows that
$$L:=\pi_{*}\left(K_{X / B}^{\ell}\right),$$
is a line bundle on $B$. Since all the fibers of $\pi$ have trivial $K_{X_{y}}^{\ell}$, it follows that $K_{X}^{\ell} \cong \pi^{*} \pi_{*}\left(K_{X}^{\ell}\right)$ (see [3, Theorem V.12.1]). We conclude that
$$K_{X}^{\ell}=\pi^{*}\left(K_{B}^{\ell} \otimes L\right) .$$
The line bundle $L=\pi_{*}\left(K_{X / B}^{\ell}\right)$ is Hermitian semipositive, and the Weil-Petersson form $\omega_{\mathrm{WP}}$ on $B$ is a semipositive representative of $\frac{1}{\ell} c_{1}(L)$. This is defined as follows. Choose any local nonvanishing holomorphic section $\Psi_{y}$ of $\pi_{*}\left(K_{X / B}^{\ell}\right)$, i.e. a family $\Psi_{y}$ of nonvanishing holomorphic $\ell$-pluricanonical forms on $X_{y}$, which vary holomorphically in $y$. The forms $\Psi_{y}$ are defined on the whole fiber $X_{y}$, but only for $y$ in a small ball in $B$. Then the Weil-Petersson (1, 1)-form on this ball
$$\omega_{\mathrm{WP}}=-\sqrt{-1} \partial_{y} \bar{\partial}_{y} \log \left((\sqrt{-1})^{n^{2}} \int_{X_{y}}\left(\Psi_{y} \wedge \bar{\Psi}_{y}\right)^{\frac{1}{\ell}}\right)$$
is actually globally defined on $B$ (this is because the fibers have trivial $\ell$ -pluricanonical bundle, so different choices of $\Psi_{y}$ differ by multiplication by a local holomorphic function in $y$, and so $\omega_{\mathrm{WP}}$ is globally defined) and is semipositive definite (this was originally proved by Griffiths [17], and is a by now standard calculation in Hodge theory). One can view $\omega_{\mathrm{WP}}$ as the pullback of the Weil-Petersson metric from the moduli space of polarized Calabi-Yau fibers of $\pi$, thanks to [13, 49, 52]. From this construction, we see that $\ell \omega_{\mathrm{WP}}$ is the curvature form of a singular $L^{2}$ metric on $\pi_{*}\left(K_{X / B}^{\ell}\right)$, so $\left[\omega_{\mathrm{WP}}\right]=\frac{1}{\ell} c_{1}(L)$. Notice that here and henceforth, we omit the usual factor of $2 \pi$ in the definition of the first Chern class.

From (2.1) we see that $K_{X}^{\ell}$ is the pullback of an ample line bundle, hence $K_{X}$ is semiample. It follows also that
$$c_{1}(X)=\pi^{*} c_{1}(B)-\left[\pi^{*} \omega_{\mathrm{WP}}\right] .$$
In our setup the class $-c_{1}(B)$ is Kähler, and therefore so is the class $-c_{1}(B)+$ $\left[\omega_{\mathrm{WP}}\right]$. Fix a Kähler metric $\chi$ in this class. From (2.2) we see that $-\pi^{*} \chi$ is cohomologous to $c_{1}(X)$, and so there exists a unique smooth positive volume form $\Omega_{1}$ on $X$ with
$$\sqrt{-1} \partial \bar{\partial} \log \left(\Omega_{1}\right)=\chi, \quad \int_{X} \Omega_{1}=\binom{n+m}{n} \int_{X} \omega_{0}^{n} \wedge \chi^{m},$$
where from now on we abbreviate $\pi^{*} \chi$ by $\chi$.
We now show the existence of a unique twisted Kähler-Einstein metric on $B$.

Theorem 2.1. There is a unique Kähler metric $\omega_{B}$ on $B$ which satisfies
$$\operatorname{Ric}\left(\omega_{B}\right)=-\omega_{B}+\omega_{\mathrm{WP}} .$$

Proof. The proof is identical to 39, Theorem 3.1] or [40, Theorem 3.1], [54, Section 4], so we will just briefly indicate the main points. First, set
$$F=\frac{\Omega_{1}}{\binom{n+m}{n} \omega_{\mathrm{SRF}}^{n} \wedge \chi^{m}},$$
which is a positive function on $X$. The argument on [54, p.445] shows that for every $y \in B$ the restriction $\left.F\right|_{X_{y}}$ is constant, and so $F$ is the pullback of a function on $B$. Now solve the complex Monge-Ampère equation on $B$
$$(\chi+\sqrt{-1} \partial \bar{\partial} v)^{m}=F e^{v} \chi^{m},$$
where $\omega_{B}=\chi+\sqrt{-1} \partial \bar{\partial} v$ is a Kähler metric on $B$. This equation can be solved thanks to work of Aubin [1] and Yau[62]. We claim that $\omega_{B}$ satisfies (2.3) (the converse implication, that every solution of (2.3) must also satisfy (2.4), and therefore must equal $\omega_{B}$, is a simple exercise). Indeed,
$$\operatorname{Ric}\left(\omega_{B}\right)=\operatorname{Ric}(\chi)-\sqrt{-1} \partial \bar{\partial} v-\sqrt{-1} \partial \bar{\partial} \log F,$$
so it is enough to prove that
$$-\sqrt{-1} \partial \bar{\partial} \log F=-\chi-\operatorname{Ric}(\chi)+\omega_{\mathrm{WP}} .$$
This can be proved by the same calculation as in [54, Proposition 4.1]. \(\square\)

Now that we have our twisted Kähler-Einstein metric $\omega_{B}$ on $B$, we can use (2.2) again to see that $-\pi^{*} \omega_{B}$ is cohomologous to $c_{1}(X)$. Define now a smooth positive volume form
$$\Omega=\binom{n+m}{n} \omega_{\mathrm{SRF}}^{n} \wedge \omega_{B}^{m} .$$
on $X$. A simple calculation as in [54, Proposition 4.1] shows that
$$\sqrt{-1} \partial \bar{\partial} \log (\Omega)=\omega_{B},$$
where from now on we abbreviate $\pi^{*} \omega_{B}$ by $\omega_{B}$.
2.2. Preliminary estimates for the Kähler-Ricci flow. Let now $\omega=$ $\omega(t)$ be a solution of the Kähler-Ricci flow
$$\frac{\partial}{\partial t} \omega=-\operatorname{Ric}(\omega)-\omega, \quad \omega(0)=\omega_{0} .$$
We know that a solution exists for all time [51], because $K_{X}$ is semiample (see Section 2.1). Define reference forms $\tilde{\omega}=\tilde{\omega}(t)$ by
$$\tilde{\omega}=e^{-t} \omega_{\mathrm{SRF}}+\left(1-e^{-t}\right) \omega_{B},$$
for $\omega_{\text {SRF }}$ and $\omega_{B}$ as above.
There exists a uniform constant $T_{I} \geqslant 0$ such that for $t \geqslant T_{I}$ we have that $\tilde{\omega}$ is Kähler. Then the Kähler-Ricci flow is equivalent to the parabolic complex Monge-Ampère equation
$$\frac{\partial}{\partial t} \varphi=\log \frac{e^{n t}(\tilde{\omega}+\sqrt{-1} \partial \bar{\partial} \varphi)^{n+m}}{\Omega}-\varphi, \quad \varphi(0)=-\rho, \quad \tilde{\omega}+\sqrt{-1} \partial \bar{\partial} \varphi>0,$$
where $\rho$ and $\Omega$ are defined as above. Indeed, if $\varphi$ solves (2.8) then $\omega=$ $\tilde{\omega}+\sqrt{-1} \partial \bar{\partial} \varphi$ solves (2.7). Conversely, if $\omega$ solves (2.7) then we can write $\omega=\tilde{\omega}+\sqrt{-1} \partial \bar{\partial} \varphi$ with $\varphi$ solving (2.8).

We have the following preliminary estimates for the Kähler-Ricci flow, most of which are already known by the results in [39, 45, 12, 15].

Lemma 2.2. Let $\omega=\omega(t)$ solve the Kähler-Ricci flow as above, and write $\varphi=\varphi(t)$ for the solution of (2.8). Then there exists a uniform constant $C>0$ such that the following hold.
\begin{itemize}
\item[(i)] $C^{-1} \tilde{\omega} \leqslant \omega \leqslant C \tilde{\omega}$, on $X \times\left[T_{I}, \infty\right)$, and $\omega_{B} \leqslant C \omega$ on $X \times[0, \infty)$.
\item[(ii)] $|\varphi| \leqslant C(1+t) e^{-t}$ on $X \times[0, \infty)$.
\item[(iii)] The scalar curvature $R$ of $\omega$ satisfies $|R| \leqslant C$ on $X \times[0, \infty)$.
\item[(iv)] For any $0<\varepsilon<1 / 2$ there exists $C_{\varepsilon}$ such that $|\dot{\varphi}| \leqslant C_{\varepsilon} e^{-\varepsilon t}$ and $|\varphi+\dot{\varphi}| \leqslant C_{\varepsilon} e^{-\varepsilon t}$ on $X \times[0, \infty)$.
\end{itemize}

Proof. For (i), the estimate $\omega_{B} \leqslant C \omega$ follows from the Schwarz Lemma argument of Song-Tian [39, 63]. The bound $C^{-1} \tilde{\omega} \leqslant \omega \leqslant C \tilde{\omega}$ was proved by Fong-Zhang [12, Theorem 1.1] (see also [39] for the case of elliptic surfaces).

Part (ii) follows from exactly the same argument as in [15, Lemma 4.1], which is a generalization of [45, Lemma 6.7] (see also [58, Lemma 3.4], [12, Theorem 4.1]). Indeed, we claim that for $t \geqslant T_{I}$,
$$\left|e^{t} \log \frac{e^{n t} \tilde{\omega}^{n+m}}{\Omega}\right| \leqslant C .$$
To see the claim, we have, using (2.6),
$$\begin{aligned}
& e^{t} \log \frac{e^{n t} \tilde{\omega}^{n+m}}{\Omega} \\
= & e^{t} \log \frac{e^{n t}\left(\binom{n+m}{n} e^{-n t}\left(1-e^{-t}\right)^{m} \omega_{\text {SRF }}^{n} \wedge \omega_{B}^{m}+\cdots+e^{-(n+m) t} \omega_{\text {SRF }}^{n+m}\right)}{\binom{n+m}{n} \omega_{\text {SRF }}^{n} \wedge \omega_{B}^{m}} \\
= & e^{t} \log \left(1+O\left(e^{-t}\right)\right),
\end{aligned}$$
which is bounded.
Define now $Q=e^{t} \varphi+A t$, for $A$ a large positive constant to be determined. Then
$$\frac{\partial Q}{\partial t}=e^{t} \log \left(\frac{e^{n t}(\tilde{\omega}+\sqrt{-1} \partial \bar{\partial} \varphi)^{n+m}}{\Omega}\right)+A .$$
We wish to bound $Q$ from below. Suppose that $\left(x_{0}, t_{0}\right)$ is a point with $t_{0}>T_{I}$ at which $Q$ achieves a minimum. At this point we have
$$0 \geqslant \frac{\partial Q}{\partial t} \geqslant e^{t} \log \frac{e^{n t} \tilde{\omega}^{n+m}}{\Omega}+A \geqslant-C^{\prime}+A,$$
for a uniform $C^{\prime}$, thanks to (2.9). Choosing $A>C^{\prime}$ gives contradiction. Hence $Q$ is bounded from below and it follows that $\varphi \geqslant-C(1+t) e^{-t}$ for a uniform $C$. The upper bound for $\varphi$ is similar.

Part (iii) is due to Song-Tian [42], who proved a uniform scalar curvature bound along the Kähler-Ricci flow whenever the canonical bundle of $X$ is semiample.

Part (iv) follows from the argument of [58, Lemma 6.4] (see also [45, Lemma 6.8]). We include the argument for the sake of completeness. First note that $\dot{\varphi}$ satisfies
$$\frac{\partial}{\partial t} \dot{\varphi}=-R-m-\dot{\varphi} .$$
Then the bound on scalar curvature (iii) implies that $\dot{\varphi}$ is bounded (in fact the bound on $\dot{\varphi}$ is proved first in [42] in order to bound scalar curvature). Hence we have a bound $\left|\frac{\partial}{\partial t} \dot{\varphi}\right| \leqslant C_{0}$. Now fix $\varepsilon \in(0,1 / 2)$ and suppose for a contradiction that the estimate $\dot{\varphi} \leqslant C_{\varepsilon} e^{-\varepsilon t}$ fails. Then there exists a sequence $\left(x_{k}, t_{k}\right) \in X \times[0, \infty)$ with $t_{k} \rightarrow \infty$ and $\dot{\varphi}\left(x_{k}, t_{k}\right) \geqslant k e^{-\varepsilon t_{k}}$. Define $\gamma_{k}=\frac{k}{2 C_{0}} e^{-\varepsilon t_{k}}$. Working at the point $x_{k}$, it follows that $\dot{\varphi} \geqslant \frac{k}{2} e^{-\varepsilon t_{k}}$ on $\left[t_{k}, t_{k}+\gamma_{k}\right]$. Then using the bound (ii),
$$C\left(1+t_{k}\right) e^{-t_{k}} \geqslant \int_{t_{k}}^{t_{k}+\gamma_{k}} \dot{\varphi} d t \geqslant \gamma_{k} \frac{k}{2} e^{-\varepsilon t_{k}}=\frac{k^{2}}{4 C_{0}} e^{-2 \varepsilon t_{k}} .$$
Since $2 \varepsilon<1$ we obtain a contradiction as $k \rightarrow \infty$. The lower bound $\dot{\varphi} \geqslant$ $-C_{\varepsilon} e^{-\varepsilon t}$ is similar. The bound on $|\varphi+\dot{\varphi}|$ follows from this and part (ii). □

The following lemma is easily derived from Song-Tian [39].
Lemma 2.3. We have
$$\left(\frac{\partial}{\partial t}-\Delta\right)(\varphi+\dot{\varphi})=\operatorname{tr}_{\omega} \omega_{B}-m,$$
and
$$\left(\frac{\partial}{\partial t}-\Delta\right) \operatorname{tr}_{\omega} \omega_{B} \leqslant \operatorname{tr}_{\omega} \omega_{B}+C\left(\operatorname{tr}_{\omega} \omega_{B}\right)^{2} \leqslant C .$$
Proof. The evolution equation (2.11) follows from the two well-known calculations:
$$\left(\frac{\partial}{\partial t}-\Delta\right) \varphi=\dot{\varphi}-(n+m)+\operatorname{tr}_{\omega} \tilde{\omega}$$
and
$$\left(\frac{\partial}{\partial t}-\Delta\right) \dot{\varphi}=\operatorname{tr}_{\omega}\left(\omega_{B}-\tilde{\omega}\right)+n-\dot{\varphi} .$$
The first inequality of (2.12) is the Schwarz Lemma computation from 39, Theorem 4.3]. The second inequality of (2.12) follows from part (i) of Lemma 2.2 \(\square\)
2.3. Two elementary lemmas. In this section, we state and prove two elementary lemmas which we will need later in our proofs of the collapsing estimates. The first is as follows:

Lemma 2.4. Consider a smooth function $f: X \times[0, \infty) \rightarrow \mathbb{R}$ which satisfies the following conditions:
\begin{itemize}
\item[(a)] There is a constant $A$ such that for all $y \in B$ and all $t \geqslant 0$
$$\left|\nabla\left(\left.f\right|_{X_{y}}\right)\right|_{\left.\omega_{0}\right|_{X_{y}}} \leqslant A .$$
\item[(b)] For all $y \in B$ and all $t \geqslant 0$ we have
$$\int_{x \in X_{y}} f(x, t) \omega_{\mathrm{SRF}, y}^{n}=0 .$$
\item[(c)] There exists a function $h:[0, \infty) \rightarrow[0, \infty)$ such that $h(t) \rightarrow 0$ as $t \rightarrow \infty$ such that
$$\sup _{x \in X} f(x, t) \leqslant h(t),$$
for all $t \geqslant 0$.
\end{itemize}
Then there is a constant $C$ such that
$$\sup _{x \in X}|f(x, t)| \leqslant C(h(t))^{1 /(2 n+1)}$$
for all $t$ sufficiently large.
Proof. Arguing by contradiction, suppose that there exist $t_{k} \rightarrow \infty$ and $x_{k} \in$ $X$ with
$$\sup _{X}\left|f\left(t_{k}\right)\right|=\left|f\left(x_{k}, t_{k}\right)\right| \geqslant k\left(h\left(t_{k}\right)\right)^{1 /(2 n+1)},$$
for all $k$. We may also assume that $t_{k}$ is sufficiently large so that the quantity $k\left(h\left(t_{k}\right)\right)^{1 /(2 n+1)}$ is less than or equal to 1 for all $k$. Let $y_{k}=\pi\left(x_{k}\right)$, so $x_{k} \in X_{y_{k}}$. Thanks to assumption (c), for all $k$ large, we must have
$$f\left(x_{k}, t_{k}\right) \leqslant-k\left(h\left(t_{k}\right)\right)^{1 /(2 n+1)} .$$
This together with assumption (a) implies that for all $x$ in the $\omega_{0}$-geodesic ball $B_{r}\left(x_{k}\right)$ in $X_{y_{k}}$ centered at $x_{k}$ and of radius
$$r=\frac{k\left(h\left(t_{k}\right)\right)^{1 /(2 n+1)}}{2 A} \leqslant \frac{1}{2 A},$$
we have
$$f\left(x, t_{k}\right) \leqslant-\frac{k\left(h\left(t_{k}\right)\right)^{1 /(2 n+1)}}{2} .$$
Therefore, using assumptions (b) and (c),
$$0=\int_{x \in X_{y_{k}}} f\left(x, t_{k}\right) \omega_{\mathrm{SRF}, y_{k}}^{n} \leqslant-\frac{k\left(h\left(t_{k}\right)\right)^{1 /(2 n+1)}}{2} \int_{B_{r}\left(x_{k}\right)} \omega_{\mathrm{SRF}, y_{k}}^{n}+C h\left(t_{k}\right) .$$

Now the metrics $\omega_{\mathrm{SRF}, y_{k}}$ are all uniformly equivalent to each other, and in particular,
$$\int_{B_{r}\left(x_{k}\right)} \omega_{\mathrm{SRF}, y_{k}}^{n} \geqslant C^{-1} k^{2 n}\left(h\left(t_{k}\right)\right)^{2 n /(2 n+1)},$$
using that $k\left(h\left(t_{k}\right)\right)^{1 /(2 n+1)} \leqslant 1$ and that small balls for $\omega_{\text {SRF }, y_{k}}$ have volume comparable to Euclidean balls. Thus we get
$$k^{2 n+1} \leqslant C,$$
which gives a contradiction when $k$ is large. \(\square\)

Remark 2.5. Note that Lemma 2.4 also holds with the same proof if $X$ is replaced by $K=\pi^{-1}\left(K^{\prime}\right)$ for $K^{\prime}$ a compact subset of $B$. Hence the result holds for our more general holomorphic fiber spaces $\pi: X \rightarrow B$ as discussed in the introduction, if we restrict to $\pi^{-1}\left(K^{\prime}\right)$ for a compact set $K^{\prime} \subset B \backslash S^{\prime}$.

The second lemma is an elementary observation from linear algebra.
Lemma 2.6. Let $A$ be an $N \times N$ positive definite symmetric matrix. Assume that there exists $\varepsilon \in(0,1)$ with
$$\operatorname{tr} A \leqslant N+\varepsilon, \quad \operatorname{det} A \geqslant 1-\varepsilon .$$
Then there exists a constant $C_{N}$ depending only on $N$ such that
$$\|A-I\| \leqslant C_{N} \sqrt{\varepsilon},$$
where $\|\cdot\|$ is the Hilbert-Schmidt norm, and $I$ is the $N \times N$ identity matrix.
Proof. We may assume that $N \geqslant 2$. Let $\lambda_{1}, \ldots, \lambda_{N}$ be the eigenvalues of $A$. Define the (normalized) elementary symmetric polynomials $S_{k}$ by
$$S_{k}=\binom{N}{k}^{-1} \sum_{1 \leqslant i_{1}<\cdots<i_{k} \leqslant N} \lambda_{i_{1}} \cdots \lambda_{i_{k}}, \quad \text { for } k=1, \ldots, N .$$
By assumption, $S_{1} \leqslant 1+N^{-1} \varepsilon$ and $S_{N} \geqslant 1-\varepsilon$. The Maclaurin inequalities
$$S_{1} \geqslant \sqrt{S_{2}} \geqslant S_{N}^{1 / N},$$
imply that $\left|S_{1}-1\right|+\left|S_{2}-1\right| \leqslant C \varepsilon$ for $C$ depending only on $N$. Compute
$$\|A-I\|^{2}=\sum_{j=1}^{N}\left(\lambda_{j}-1\right)^{2}=N^{2} S_{1}^{2}-2 N S_{1}-N(N-1) S_{2}+N \leqslant C^{\prime} \varepsilon,$$
for $C^{\prime}$ depending only on $N$, and the result follows. \(\square\)
2.4. A local Calabi estimate for collapsing metrics. Later we will need a local Calabi estimate for solutions of the Kähler-Ricci flow which are collapsing exponentially in specified directions. The Calabi estimate for the elliptic complex Monge-Ampère equation, giving third order estimates for the potential function depending on the second order estimates, first appeared in the paper of Yau [62], and was used in the parabolic case by Cao [6]. In the following we use a formulation due to Phong-Sesum-Sturm [29], together with a cut-off function argument similar to that used in [34].

Proposition 2.7. Let $B_{1}(0)$ be the unit polydisc in $\mathbb{C}^{n+m}$ and let $\omega_{E}^{(n+m)}=$ $\sum_{k=1}^{m+n} \sqrt{-1} d z^{k} \wedge d \bar{z}^{k}$ be the Euclidean metric. Write $\mathbb{C}^{n+m}=\mathbb{C}^{m} \oplus \mathbb{C}^{n}$ and define $\omega_{E, t}=\omega_{E}^{(m)}+e^{-t} \omega_{E}^{(n)}$, for $\omega_{E}^{(m)}$ and $\omega_{E}^{(n)}$ Euclidean metrics on the two factors $\mathbb{C}^{m}$ and $\mathbb{C}^{n}$ respectively. Assume that $\omega=\omega(t)$ is a solution of the Kähler-Ricci flow
$$\frac{\partial \omega}{\partial t}=-\operatorname{Ric}(\omega)-\omega, \quad \omega(0)=\omega_{0},$$
on $B_{1}(0) \times[0, \infty)$ which satisfies
$$A^{-1} \omega_{E, t} \leqslant \omega \leqslant A \omega_{E, t},$$
for some positive constant $A$. Then there is a constant $C$ that depends only on $n, m, A$ and $\omega_{0}$ such that for all $t \geqslant 0$ on $B_{1 / 2}(0)$ we have
$$S=\left|\nabla^{E} g\right|_{g}^{2} \leqslant C e^{t},$$
where $g$ is the metric associated to $\omega$ and $\nabla^{E}$ is the covariant derivative of $\omega_{E}^{(n+m)}$.

Proof. In the following $C$ will denote a generic constant that depends only on $n, m, A$ and $\omega_{0}$. For simplicity of notation, we write simply $\omega_{E}=\omega_{E}^{(n+m)}$. Following Yau [62], define
$$S=\left|\nabla^{E} g\right|_{g}^{2}=g^{i \bar{\ell}} g^{p \bar{k}} g^{j \bar{q}} \nabla_{i}^{E} g_{j \bar{k}} \nabla_{\bar{\ell}}^{E} g_{p \bar{q}} .$$
If $T_{i j}^{k}$ denotes the difference of the Christoffel symbols of $\omega$ and $\omega_{E}$, then $T$ is a tensor and it is easy to see that $S=|T|_{g}^{2}$. Since $\omega_{E, t}$ is also a flat metric, the quantity $S$ is the same if we use its connection $\nabla^{E, t}$. The parabolic Calabi computation gives (cfr. [29])
$$\left(\frac{\partial}{\partial t}-\Delta\right) S \leqslant S-|\nabla T|^{2}-|\bar{\nabla} T|^{2},$$
where here and in the rest of the proof we suppress the subscript $g$ from the norms.

Take $\psi$ a nonnegative smooth cutoff function supported in $B_{1}(0)$ with $\psi \equiv 1$ on $B_{1 / 2}(0)$ and with
$$\sqrt{-1} \partial \psi \wedge \bar{\partial} \psi \leqslant C \omega_{E}, \quad-C \omega_{E} \leqslant \sqrt{-1} \partial \bar{\partial}\left(\psi^{2}\right) \leqslant C \omega_{E} .$$

From (2.14) it then follows that
$$|\nabla \psi|^{2} \leqslant C e^{t}, \quad \Delta\left(\psi^{2}\right) \geqslant-C e^{t} .$$
We can then compute
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta\right)\left(\psi^{2} S\right) & \leqslant \psi^{2}\left(\frac{\partial}{\partial t}-\Delta\right) S+C S e^{t}+2\left|\left\langle\nabla \psi^{2}, \nabla S\right\rangle\right| \\
& \leqslant \psi^{2} S-\psi^{2}\left(|\nabla T|^{2}+|\bar{\nabla} T|^{2}\right)+C S e^{t}+2\left|\left\langle\nabla \psi^{2}, \nabla S\right\rangle\right| .
\end{aligned}$$
On the other hand, using the Young inequality
$$\begin{aligned}
2\left|\left\langle\nabla \psi^{2}, \nabla S\right\rangle\right| & \left.=4 \psi|\langle\nabla \psi, \nabla| T|^{2}\right\rangle|\leqslant 4 \psi| \nabla \psi|\cdot| \nabla|T|^{2} \mid \\
& \leqslant \psi^{2}\left(|\nabla T|^{2}+|\bar{\nabla} T|^{2}\right)+C S|\nabla \psi|^{2} \\
& \leqslant \psi^{2}\left(|\nabla T|^{2}+|\bar{\nabla} T|^{2}\right)+C S e^{t},
\end{aligned}$$
and so
$$\begin{aligned}
& \left(\frac{\partial}{\partial t}-\Delta\right)\left(\psi^{2} S\right) \leqslant C S e^{t}, \\
& \left(\frac{\partial}{\partial t}-\Delta\right)\left(e^{-t} \psi^{2} S\right) \leqslant C S .
\end{aligned}$$
On the other hand, the second order estimate of Cao [6] (the parabolic version of the estimate of [62, 1]) gives
$$\begin{aligned}
\left(\frac{\partial}{\partial t}-\Delta\right) \operatorname{tr}_{\omega_{E, t}} \omega= & -\operatorname{tr}_{\omega_{E, t}} \omega+e^{-t} g_{E, t}^{i \bar{q}} g_{E, t}^{p \bar{j}}\left(g_{E}^{(n)}\right)_{p \bar{q}} g_{i \bar{j}} \\
& -g_{E, t}^{i \bar{\ell}} g^{p \bar{j}} g^{k \bar{q}} \nabla_{i}^{E} g_{k \bar{j}} \nabla_{\bar{\ell}}^{E} g_{p \bar{q}} \\
\leqslant & -A^{-1} S,
\end{aligned}$$
using (2.14). It follows that if we take $C_{0}$ large enough, then we have
$$\left(\frac{\partial}{\partial t}-\Delta\right)\left(e^{-t} \psi^{2} S+C_{0} \operatorname{tr}_{\omega_{E, t}} \omega\right)<0 .$$
It follows that the maximum of $e^{-t} \psi^{2} S+C_{0} \operatorname{tr}_{\omega_{E, t}} \omega$ on $\overline{B_{1}(0)} \times[0, T]$ (for any finite $T$ ) can only occur at $t=0$ or on the boundary of $\overline{B_{1}(0)}$, where $\psi=0$. Since by (2.14) we have $\operatorname{tr}_{\omega_{E, t}} \omega \leqslant(n+m) A$, we conclude that $\sup _{B_{1 / 2}(0)} S \leqslant C e^{t}$, as required. \(\square\)
2.5. Collapsing estimates for the Kähler-Ricci flow. In this section, we give the proof of Theorem 1.1, which establishes the metric collapsing for the Kähler-Ricci flow in the case of a holomorphic submersion. We will make use of the lemmas and observations above.

We begin with a simple but crucial lemma, which is a generalization of [58, Proposition 7.3]. We will need it later.

Lemma 2.8. For any $\eta \in(0,1 / 4)$, there is a constant $C$ such that
$$\operatorname{tr}_{\omega} \omega_{B}-m \leqslant C e^{-\eta t} .$$

Proof. Let
$$Q=e^{\eta t}\left(\operatorname{tr}_{\omega} \omega_{B}-m\right)-e^{2 \eta t}(\varphi+\dot{\varphi}) .$$
Then from Lemma 2.3,
$$\left(\frac{\partial}{\partial t}-\Delta\right) Q \leqslant \eta e^{\eta t}\left(\operatorname{tr}_{\omega} \omega_{B}-m\right)+C e^{\eta t}-2 \eta e^{2 \eta t}(\varphi+\dot{\varphi})-e^{2 \eta t}\left(\operatorname{tr}_{\omega} \omega_{B}-m\right) .$$
From Lemma 2.2, we have $\operatorname{tr}_{\omega} \omega_{B} \leqslant C$ and $\left|e^{2 \eta t}(\varphi+\dot{\varphi})\right| \leqslant C$. Then
$$\left(\frac{\partial}{\partial t}-\Delta\right) Q \leqslant C e^{\eta t}-e^{2 \eta t}\left(\operatorname{tr}_{\omega} \omega_{B}-m\right),$$
and so at a maximum point of $Q$ we have an upper bound for $e^{\eta t}\left(\operatorname{tr}_{\omega} \omega_{B}-m\right)$ and hence for $Q$. The result follows. \(\square\)

We will now establish part (ii) of Theorem 1.1. We have the following estimate in the fibers $X_{y}$ of $\pi$.

Lemma 2.9. There is a constant $C>0$ such that for all $t \geqslant 0$ and all $y \in B$,
$$\left\|\left.e^{t} \omega\right|_{X_{y}}\right\|_{C^{1}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \leqslant C,\left.\quad e^{t} \omega\right|_{X_{y}} \geqslant\left. C^{-1} \omega_{0}\right|_{X_{y}} .$$
Proof. Fix a point $y \in B$ and a point $x \in X_{y}$. Since $\pi: X \rightarrow B$ is a holomorphic submersion, we can find a $U \subset X$ a local holomorphic product coordinate chart for $\pi$ centered at $x$, which equals the unit polydisc in $\mathbb{C}^{n+m}$ (see e.g. [23, p.60]). Thanks to part (i) of Lemma 2.2, we see that the hypotheses of Proposition 2.7 are satisfied, and so we conclude that on the half-sized polydisc we have
$$\left|\nabla^{E} \omega\right|_{\omega}^{2} \leqslant C e^{t},$$
where $\nabla^{E}$ is the covariant derivative of the Euclidean metric $\omega_{E}$ on $U$. We may assume that $\omega_{E}$ is uniformly equivalent to $\omega_{0}$ on $U$. Again using Lemma 2.2.(i), we see that on $U$ the metric $\left.\omega\right|_{X_{y}}$ is uniformly equivalent to $\left.e^{-t} \omega_{E}\right|_{X_{y}}$, and so on $U$ we have (cf. [54, Section 3] or [45, Lemma 3.6.9])
$$\begin{aligned}
& \left|\nabla^{E}\left(\left.e^{t} \omega\right|_{X_{y}}\right)\right|_{\omega_{E}}^{2}=e^{-t}\left|\nabla^{E}\left(\left.\omega\right|_{X_{y}}\right)\right|_{e^{-t} \omega_{E}}^{2} \\
& \quad \leqslant C e^{-t}\left|\nabla^{E}\left(\omega \mid X_{y}\right)\right|_{\omega}^{2} \leqslant C e^{-t}\left|\nabla^{E} \omega\right|_{\omega}^{2} \leqslant C .
\end{aligned}$$
Furthermore, all these estimates are uniform in $y \in B$. The uniform $C^{1}$ bound as well as the uniform lower bound for $\left.e^{t} \omega\right|_{X_{y}}$ follows at once. \(\square\)

Thanks to Lemma 2.9, for any fixed $y \in B$ and $0<\alpha<1$, given any sequence $t_{k} \rightarrow \infty$ we can extract a subsequence such that
$$\left.e^{t_{k}} \omega\right|_{X_{y}} \rightarrow \omega_{\infty, y},$$
in $C^{\alpha}$ on $X_{y}$, where $\omega_{\infty, y}$ is a $C^{\alpha}$ Kähler metric on $X_{y}$ cohomologous to $\left.\omega_{0}\right|_{X_{y}}$.

We can now prove the last statement in Theorem 1.1,(ii).

Lemma 2.10. Given any $y \in B$, as $t \rightarrow \infty$ we have that
$$\left.e^{t} \omega\right|_{X_{y}} \rightarrow \omega_{\mathrm{SRF}, y},$$
in $C^{\alpha}$ on $X_{y}$, for any $0<\alpha<1$.
Proof. Write
$$\begin{aligned}
\left(\left.e^{t} \omega\right|_{X_{y}}\right)^{n} & =e^{n t} \frac{\left(\left.\omega\right|_{X_{y}}\right)^{n}}{\left(\omega_{\mathrm{SRF}, y}\right)^{n}}\left(\omega_{\mathrm{SRF}, y}\right)^{n}=e^{n t} \frac{\omega^{n} \wedge \omega_{B}^{m}}{\omega_{\mathrm{SRF}}^{n} \wedge \omega_{B}^{m}}\left(\omega_{\mathrm{SRF}, y}\right)^{n} \\
& =e^{n t}\binom{n+m}{n} \frac{\omega^{n} \wedge \omega_{B}^{m}}{\Omega}\left(\omega_{\mathrm{SRF}, y}\right)^{n} \\
& =e^{\varphi+\dot{\varphi}}\binom{n+m}{n} \frac{\omega^{n} \wedge \omega_{B}^{m}}{\omega^{n+m}}\left(\omega_{\mathrm{SRF}, y}\right)^{n} .
\end{aligned}$$
Consider the function on $X$, depending on $t$, defined by
$$f=e^{\varphi+\dot{\varphi}}\binom{n+m}{n} \frac{\omega^{n} \wedge \omega_{B}^{m}}{\omega^{n+m}},$$
which when restricted to the fiber $X_{y}$ equals
$$\left.f\right|_{X_{y}}=\frac{\left(\left.e^{t} \omega\right|_{X_{y}}\right)^{n}}{\left(\omega_{\mathrm{SRF}, y}\right)^{n}} .$$
We have that
$$\int_{X_{y}} f\left(\omega_{\mathrm{SRF}, y}\right)^{n}=\int_{X_{y}}\left(\left.e^{t} \omega\right|_{X_{y}}\right)^{n}=\int_{X_{y}}\left(\left.\omega_{0}\right|_{X_{y}}\right)^{n}=\int_{X_{y}}\left(\omega_{\mathrm{SRF}, y}\right)^{n},$$
so that $f-1$ satisfies condition (b) of Lemma 2.4. From Lemma 2.2.(iv), for $t$ large we have that
$$\left|e^{\varphi+\dot{\varphi}}-1\right| \leqslant C e^{-\eta t},$$
as long as $\eta<1 / 2$. On the other hand, if at a point on $X_{y}$ we choose coordinates so that $\omega$ is the identity and $\omega_{B}$ is diagonal with eigenvalues $\lambda_{1}, \ldots, \lambda_{m}$, then at that point
$$\binom{n+m}{n} \frac{\omega^{n} \wedge \omega_{B}^{m}}{\omega^{n+m}}=\prod_{j} \lambda_{j} \leqslant\left(\sum_{j} \lambda_{j} / m\right)^{m}=\left(\operatorname{tr}_{\omega} \omega_{B} / m\right)^{m} .$$
By Lemma 2.8, $\sup _{X} \operatorname{tr}_{\omega} \omega_{B} / m \leqslant 1+C e^{-\eta t}$, for $\eta<1 / 4$. Then (2.18) and (2.19) imply that $\sup _{X} f \leqslant 1+C e^{-\eta t}$, for some $\eta>0$. This shows that $f-1$ satisfies condition (c) of Lemma 2.4. Lastly, $f-1$ also satisfies condition (a) because of (2.16) and the estimates in Lemma 2.9. Therefore Lemma 2.4 shows that $f$ converges to 1 uniformly on $X$ and exponentially fast as $t \rightarrow \infty$, i.e.
$$\left\|\left(\left.e^{t} \omega\right|_{X_{y}}\right)^{n}-\omega_{\mathrm{SRF}, y}^{n}\right\|_{C^{0}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \leqslant C e^{-\eta t},$$
for some $\eta>0$, for all $y \in B$.

If we choose a sequence $t_{k} \rightarrow \infty$ such that $\left.e^{t_{k}} \omega\right|_{X_{y}} \rightarrow \omega_{\infty, y}$, in $C^{\alpha}$ on $X_{y}$, then the $C^{\alpha}$ metric $\omega_{\infty, y}$ on $X_{y}$ satisfies
$$\omega_{\infty, y}^{n}=\omega_{\mathrm{SRF}, y}^{n} .$$
Standard bootstrap estimates give that $\omega_{\infty, y}$ is a smooth Kähler metric, and the uniqueness of the solution of this equation (originally due to Calabi) implies that $\omega_{\infty, y}=\omega_{\mathrm{SRF}, y}$. From this it follows that $\left.e^{t} \omega\right|_{X_{y}} \rightarrow \omega_{\mathrm{SRF}, y}$ in $C^{\alpha}$, as required. \(\square\)

Note that in the previous lemma, since we only have derivative bounds on $\omega$ in the fiber directions, we are not able to conclude that the $C^{\alpha}$ convergence is uniform in $y \in B$. However, we can now establish uniformity of the fiberwise convergence in the $C^{0}$ norm and complete the proof of Theorem 1.1(ii). Namely, we will prove the estimate (1.6):
$$\left\|\left.e^{t} \omega\right|_{X_{y}}-\omega_{\mathrm{SRF}, y}\right\|_{C^{0}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \leqslant C e^{-\eta t}, \quad \text { for all } y \in B .$$
Proof of (1.6). Consider the function
$$\left.f\right|_{X_{y}}=\frac{\left(\left.e^{t} \omega\right|_{X_{y}}\right) \wedge \omega_{\mathrm{SRF}, y}^{n-1}}{\omega_{\mathrm{SRF}, y}^{n}} .$$
While this is defined on $X_{y}$, it is clearly smooth in $y$ and so defines a smooth function $f$ on $X$, which equals
$$\begin{aligned}
f & =\frac{\left(e^{t} \omega\right) \wedge \omega_{\text {SRF }}^{n-1} \wedge \omega_{B}^{m}}{\omega_{\text {SRF }}^{n} \wedge \omega_{B}^{m}}=\binom{n+m}{n} \frac{\left(e^{t} \omega\right) \wedge \omega_{\text {SRF }}^{n-1} \wedge \omega_{B}^{m}}{\Omega} \\
& =e^{\varphi+\dot{\varphi}}\binom{n+m}{n} \frac{\omega \wedge\left(e^{-t} \omega_{\text {SRF }}\right)^{n-1} \wedge \omega_{B}^{m}}{\omega^{n+m}} .
\end{aligned}$$
We wish to show that $f$ converges to 1 uniformly on $X$ and exponentially fast. By the arithmetic-geometric means inequality we have
$$\left(\left.f\right|_{X_{y}}\right)^{n} \geqslant \frac{\left(\left.e^{t} \omega\right|_{X_{y}}\right)^{n}}{\omega_{\mathrm{SRF}, y}^{n}},$$
and the right hand side converges uniformly to 1 and exponentially fast by (2.20). Therefore $1-f$ satisfies condition (c) in Lemma 2.4. Condition (b) is trivial, and condition (a) holds thanks to Lemma 2.9. Therefore we conclude that
$$\left\|\left(\left.e^{t} \omega\right|_{X_{y}}\right) \wedge \omega_{\mathrm{SRF}, y}^{n-1}-\omega_{\mathrm{SRF}, y}^{n}\right\|_{C^{0}\left(X_{y},\left.\omega_{0}\right|_{X_{y}}\right)} \leqslant C e^{-\eta t},$$
for some $C, \eta>0$ and all $y \in B$.
Choosing local fiber coordinates at a point $x \in X_{y}$ so that $\omega_{\mathrm{SRF}, y}$ is the identity and $\left.e^{t} \omega\right|_{X_{y}}$ is given by the positive definite $n \times n$ matrix $A$ we see that (2.20) and (2.21) give $|\operatorname{det} A-1| \leqslant C e^{-\eta t}$ and $|\operatorname{tr} A-n| \leqslant C e^{-\eta t}$ respectively. Applying Lemma 2.6 we obtain $\|A-I\| \leqslant C e^{-\eta t / 2}$. This implies the estimate (1.6). \(\square\)

We now turn to the proof of part (i) of Theorem 1.1.

Proof of Theorem 1.1. (i). Fix a point $x \in X$ with $y=\pi(x) \in B$. We have
$$\operatorname{tr}_{\omega} \tilde{\omega}=\operatorname{tr}_{\omega} \omega_{B}+\operatorname{tr}_{\omega}\left(e^{-t} \omega_{\mathrm{SRF}, y}\right)+e^{-t}\left(-\operatorname{tr}_{\omega} \omega_{B}+\operatorname{tr}_{\omega}\left(\omega_{\mathrm{SRF}}-\omega_{\mathrm{SRF}, y}\right)\right) .$$
From Lemma 2.2, $\operatorname{tr}_{\omega} \omega_{B}$ is uniformly bounded. We claim that
$$\left|\operatorname{tr}_{\omega}\left(\omega_{\mathrm{SRF}}-\omega_{\mathrm{SRF}, y}\right)\right| \leqslant C e^{t / 2} .$$
Indeed, since $\pi$ is a submersion there are coordinates $z^{1}, \ldots, z^{m+n}$ near $x$ and $z^{1}, \ldots, z^{m}$ near $\pi(x)$ so that $\pi$ is given by the map $\left(z^{1}, \ldots, z^{m+n}\right) \mapsto$ $\left(z^{1}, \ldots, z^{m}\right)$ (see e.g. [23, p.60]). In particular, $z^{m+1}, \ldots, z^{m+n}$ restrict to local coordinates along the fibers of $\pi$. Then we can write at $x$,
$$\omega_{\mathrm{SRF}}-\omega_{\mathrm{SRF}, y}=2 \operatorname{Re}\left(\sqrt{-1} \sum_{\alpha=1}^{m} \sum_{j=1}^{m+n} \Psi_{\alpha \bar{j}} d z^{\alpha} \wedge d \bar{z}^{j}\right),$$
for $\Psi_{\alpha \bar{j}} \in \mathbb{C}$. We can do this because the form $\omega_{\text {SRF }}-\omega_{\text {SRF }, y}$ vanishes when restricted to the fiber $X_{y}$. Then
$$\left|\operatorname{tr}_{\omega}\left(\omega_{\mathrm{SRF}}-\omega_{\mathrm{SRF}, y}\right)\right|=2\left|\operatorname{Re}\left(\sum_{\alpha=1}^{m} \sum_{j=1}^{m+n} g^{\alpha \bar{j}} \Psi_{\alpha \bar{j}}\right)\right| \leqslant C e^{t / 2},$$
since thanks to estimate in Lemma 2.2.(i) we have that $\left|g^{j \bar{j}}\right| \leqslant C e^{t}$ and $\left|g^{\alpha \bar{\alpha}}\right| \leqslant C$ whenever $1 \leqslant \alpha \leqslant m$, and so the Cauchy-Schwarz inequality gives $\left|g^{\alpha \bar{j}}\right| \leqslant\left|g^{\alpha \bar{\alpha}} g^{j \bar{j}}\right|^{\frac{1}{2}} \leqslant C e^{t / 2}$. Moreover, by compactness, we may assume that the constant $C$ is independent of the point $x$ and the choice of coordinates. Thus the claim (2.23) is proved.

Hence
$$\left|e^{-t}\left(-\operatorname{tr}_{\omega} \omega_{B}+\operatorname{tr}_{\omega}\left(\omega_{\mathrm{SRF}}-\omega_{\mathrm{SRF}, y}\right)\right)\right| \leqslant C e^{-t / 2} .$$
On the other hand, the estimate (1.6) implies that
$$\operatorname{tr}_{\omega}\left(e^{-t} \omega_{\mathrm{SRF}, y}\right)=\operatorname{tr}_{\left(\left.e^{t} \omega\right|_{X_{y}}\right)} \omega_{\mathrm{SRF}, y} \leqslant n+C e^{-\eta t} .$$
From (2.22), (2.24), (2.25) and Lemma 2.8, we have
$$\operatorname{tr}_{\omega} \tilde{\omega} \leqslant n+m+C e^{-\eta t},$$
for some $\eta>0$. Moreover, the constants $C$ and $\eta$ are independent of the choice of $x \in X$. On the other hand, for $t \geqslant T_{I}$,
$$\begin{aligned}
\frac{\tilde{\omega}^{n+m}}{\omega^{n+m}} & =\frac{\left(e^{-t} \omega_{\mathrm{SRF}}+\left(1-e^{-t}\right) \omega_{B}\right)^{n+m}}{\binom{n+m}{n} \omega_{\mathrm{SRF}}^{n} \wedge \omega_{B}^{m}} e^{n t} e^{-\varphi-\dot{\varphi}} \\
& \geqslant e^{-\varphi-\dot{\varphi}}-C e^{-t} \\
& \geqslant 1-C^{\prime} e^{-\eta t},
\end{aligned}$$
for some $\eta>0$. Here we used Lemma 2.2. (iv) for the last inequality, and the fact that for $k \geqslant 1$ the term
$$\frac{e^{-(n+k) t} \omega_{\mathrm{SF}}^{n+k} \wedge \omega_{B}^{m-k}}{\omega_{\mathrm{SRF}}^{n} \wedge \omega_{B}^{m}} e^{n t},$$
is of the order of $e^{-k t}$.
From (2.26) and (2.27) we can apply Lemma 2.6 (choose coordinates so that $\omega$ is the identity and $\tilde{\omega}$ is given by a matrix $A$ ) to obtain
$$\|\omega-\tilde{\omega}\|_{C^{0}(X, \omega)} \leqslant C e^{-\eta t},$$
for a uniform $C, \eta>0$. Since $\omega \leqslant C \omega_{0}$, we have
$$\|\omega-\tilde{\omega}\|_{C^{0}\left(X, \omega_{0}\right)} \leqslant C e^{-\eta t},$$
and since $\tilde{\omega}=\omega_{B}+e^{-t}\left(\omega_{\text {SRF }}-\omega_{B}\right)$ we obtain the estimate (1.5) as required. \(\square\)

Finally, part (iii) of Theorem 1.1 follows from part (i) and the definition of Gromov-Hausdorff convergence, for example using [58, Lemma 9.1] (note that our submersion $\pi: X \rightarrow B$ is a smooth fiber bundle).

\section*{3. The Kähler-Ricci flow in the case of singular fibers}

In this section we give the proof of Theorem 1.2.
3.1. Preliminaries: the case of singular fibers. Let us first recall the general setup of Song-Tian [39, 40, 42] where our results will apply. Let $\left(X^{m+n}, \omega_{0}\right)$ be a compact Kähler manifold with canonical bundle $K_{X}$ semiample and $0<m:=\kappa(X)<\operatorname{dim} X$.

The map $\pi: X \rightarrow B$ is a surjective holomorphic map given by sections of $H^{0}\left(X, K_{X}^{\ell}\right)$ where $B^{m}$ is a normal projective variety and the generic fiber $X_{y}=\pi^{-1}(y)$ of $\pi$ has $K_{X_{y}}^{\ell}$ holomorphically trivial (so it is in particular a Calabi-Yau manifold of dimension $n$ ). Recall that we denote by $S^{\prime} \subset B$ the singular set of $B$ together with the set of critical values of $\pi$, and we define $S=\pi^{-1}\left(S^{\prime}\right) \subset X$.

Since the map $\pi: X \rightarrow B \subset \mathbb{P} H^{0}\left(X, K_{X}^{\ell}\right)$ is induced by the space of global sections of $K_{X}^{\ell}$, we have that $\pi^{*} \mathcal{O}(1)=K_{X}^{\ell}$. Therefore, if we let $\chi$ be $\frac{1}{\ell} \omega_{\mathrm{FS}}$ on $\mathbb{P} H^{0}\left(X, K_{X}^{\ell}\right)$, we have that $\pi^{*} \chi$ (later, denoted by $\chi$ ) is a smooth semipositive representative of $-c_{1}(X)$. Here, $\omega_{\mathrm{FS}}$ denotes the Fubini-Study metric. We will also denote by $\chi$ the restriction of $\chi$ to $B \backslash S^{\prime}$.

As in the submersion case, we can define the semi Ricci-flat form $\omega_{\text {SRF }}$ on $X \backslash S$, so that $\omega_{\mathrm{SRF}, y}=\left.\omega_{\mathrm{SRF}}\right|_{X_{y}}$ is the unique Ricci-flat Kähler metric on $X_{y}$ cohomologous to $\left.\omega_{0}\right|_{X_{y}}$, for all $y \in B \backslash S^{\prime}$. Let $\Omega_{1}$ be the volume form on $X$ with
$$\sqrt{-1} \partial \bar{\partial} \log \Omega_{1}=\chi, \quad \int_{X} \Omega_{1}=\binom{n+m}{n} \int_{X} \omega_{0}^{n} \wedge \chi^{m} .$$
Define a function $F$ on $X \backslash S$ by
$$F=\frac{\Omega_{1}}{\binom{n+m}{n} \omega_{\mathrm{SRF}}^{n} \wedge \chi^{m}} .$$