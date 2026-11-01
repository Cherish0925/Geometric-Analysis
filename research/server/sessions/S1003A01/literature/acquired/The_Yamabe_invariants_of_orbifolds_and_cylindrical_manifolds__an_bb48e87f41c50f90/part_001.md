---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: The Yamabe invariants of orbifolds and cylindrical manifolds, and 𝐿^2-harmonic spinors]

---
source_file: math_0204072v3.pdf
converter: mathpix
format: mmd
---

\title{
The Yamabe invariants of orbifolds and cylindrical manifolds, and $L^{2}$-harmonic spinors
}

\author{
Kazuo Akutagawa *, Boris Botvinnik *
}

\begin{abstract}
We study the Yamabe invariants of cylindrical manifolds and compact orbifolds with a finite number of singularities, by means of conformal geometry and the Atiyah-Patodi-Singer $L^{2}$-index theory. For an $n$-orbifold $M$ with singularities $\Sigma_{\Gamma}=\left\{\left(\check{p}_{1}, \Gamma_{1}\right), \ldots,\left(\check{p}_{s}, \Gamma_{s}\right)\right\}$ (where each group $\Gamma_{j}<O(n)$ is of finite order), we define and study the orbifold Yamabe invariant $Y^{\text {orb }}(M)$. We prove that $Y^{\text {orb }}(M)$ coincides with the corresponding $h$-cylindrical Yamabe invariant $Y^{h \text {-cy } \ell}\left(M \backslash\left\{\check{p}_{1}, \ldots, \check{p}_{s}\right\}\right)$ defined by the authors [3], where $h=h_{\Gamma_{j}}$ is the standard metric on the slice $S^{n-1} / \Gamma_{j}$ of each end with infinity $\check{p}_{j}$. Using this, we show that $Y^{\text {orb }}(M)$ is bounded by $Y\left(S^{n}\right) / d$ from above, where $d=\max _{j}\left|\Gamma_{j}\right|^{\frac{2}{n}}$. For a cylindrical 4-manifold $X$ with a general slice metric $h$ on the end, we also establish a method for estimating the $h$-cylindrical Yamabe invariant $Y^{h-c y \ell}(X)$ from above, in terms of the geometry and topology of $X$. We conclude by an explicit estimate of $Y^{h-c y \ell}(X)$ for particular cylindrical 4-manifolds $X$, including that of $Y^{\text {orb }}(M)$ for 4-orbifolds $M$.
\end{abstract}

\section*{1 Introduction}

In this paper, we study the Yamabe invariant of compact orbifolds with a finite number of singularities (i.e., the orbifold Yamabe invariant) and its relationship to the Yamabe invariant of cylindrical manifolds (i.e., the cylindrical Yamabe invariant). In the 4-dimensional case, we also establish a method for estimating the cylindrical Yamabe invariant (including the orbifold Yamabe invariant) from above, by means of conformal geometry and the Atiyah-Patodi-Singer $L^{2}$-index theory.
1.1. The orbifold Yamabe invariant. First, we define the Yamabe invariant of such orbifolds, that is, the orbifold Yamabe invariant, and then we study some fundamental properties on the orbifold Yamabe invariant. An orbifold $M$ under consideration here is a relatively compact smooth manifold outside of a finite number of singular points $\check{p}_{1}, \ldots, \check{p}_{s} \in M$, and near each point $\check{p}_{j}$ it is locally homeomorphic to the orbit space $\mathbf{R}^{n} / \Gamma_{j}$, where $\Gamma_{j}(<O(n))$ is a finite group acting freely on $\mathbf{R}^{n} \backslash\{0\}$. We use the notation

\footnotetext{
*Partially supported by the Grants-in-Aid for Scientific Research (C), Japan Society for the Promotion of Science, No. 14540072.
}
$\Sigma_{\Gamma}=\left\{\left(\check{p}_{1}, \Gamma_{1}\right), \ldots,\left(\check{p}_{s}, \Gamma_{s}\right)\right\}$ and $\Sigma=\left\{\check{p}_{1}, \ldots, \check{p}_{s}\right\}, \Gamma=\left\{\Gamma_{1}, \ldots, \Gamma_{s}\right\}$ for the singularities of $M$. Throught this paper, we assume that $\operatorname{dim} M=n \geq 3$.

There are natural orbifold Riemannian metrics compatible with the orbifold structure. We denote the space of such metrics by $\mathcal{R i e m}^{\text {orb }}(M)$. Let $R_{g}$, $d \sigma_{g}$ and $\operatorname{Vol}_{g}(M)$ denote respectively the scalar curvature, the volume form and the volume corresponding to $g \in \mathcal{R} \operatorname{iem}^{\text {orb }}(M)$. To start with, we note that the (normalized) Einstein-Hilbert functional
$$I: \mathcal{R} \mathrm{iem}^{\text {orb }}(M) \rightarrow \mathbf{R}, \quad \text { where } \quad g \mapsto \frac{\int_{M} R_{g} d \sigma_{g}}{\operatorname{Vol}_{g}(M)^{\frac{n-2}{n}}},$$
has exactly the same property as in the case of compact manifolds: the set of critical points $\operatorname{Crit}(I)$ coincides with the space of orbifold Einstein metrics (see Proposition 2.1).

We also observe that the functional $I$ restricted on each orbifold conformal class $[g]_{\text {orb }} \in \mathcal{C}^{\text {orb }}(M)$ has the same basic properties as in the case of compact manifolds (cf. [18]), where $\mathcal{C}^{\text {orb }}(M)$ denotes the space of orbifold conformal classes on $M$. This leads us to the definitions of the orbifold Yamabe constant $Y_{[g]_{\text {orb }}}(M)$ and the orbifold Yamabe invariant $Y^{\text {orb }}(M)$ respectively:
$$Y_{[g]_{\mathrm{orb}}}(M):=\inf _{\tilde{g} \in[g]_{\mathrm{orb}}} I(\tilde{g}), \quad Y^{\mathrm{orb}}(M):=\sup _{C \in \mathcal{C}^{\mathrm{orb}}(M)} Y_{C}(M) .$$
1.2. The orbifold and the cylindrical Yamabe invariants. Next, we study the relationship between the oribifold Yamabe invariant and the corresponding $h$-cylindrical Yamabe invariant. Consider, for simplicity, the case when a compact orbifold $M$ has only one singularity $\Sigma_{\Gamma}=\{(\check{p}, \Gamma)\}$. We observe that, in the category of smooth manifolds, the open manifold $X:=M \backslash\{\check{p}\}$ could be considered as the underlying smooth manifold of a cylindrical manifold ( $X, \bar{g}$ ) with the cylindrical end ( $\left(S^{n-1} / \Gamma\right) \times[1, \infty), \bar{g}=h_{\Gamma}+d t^{2}$ ), where $\left(S^{n-1} / \Gamma, h_{\Gamma}\right)$ is the corresponding spherical space form equipped with the standard metric $h_{\Gamma}$ of constant curvature one. As an object in the category of Riemannian manifolds, the orbifold $M$ equipped with an orbifold metric $g$ is quite different from the cylindrical manifold $(X, \bar{g})$. Even from the viewpoint of conformal geometry, there is no "cylindrical metric" within the conformal class $[g]$, in general. However, the following holds (Theorem 2.9).
Theorem A. Let $M$ be a compact orbifold with one singularity $\Sigma_{\Gamma}=\{(\check{p}, \Gamma)\}$. Then $Y^{\text {orb }}(M)=Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\})$. Here, $Y^{h_{\Gamma}-c y \ell}(X)$ denotes the $h_{\Gamma}$-cylindrical Yamabe invariant of $X$ (see Section 2.6 or [3, Section 2] for the definition of $\left.Y^{h_{\Gamma}-c y \ell}(X)\right)$.
Using this, we prove the following estimate of the orbifold Yamabe invariant (Corollary 2.10).
Theorem B. Let $M$ be a compact orbifold of $\operatorname{dim} M=n \geq 3$ with singularities $\Sigma_{\Gamma}=\left\{\left(\check{p}_{1}, \Gamma_{1}\right), \ldots,\left(\check{p}_{s}, \Gamma_{s}\right)\right\}$. Then
$$Y^{\text {orb }}(M)=Y^{h_{\Gamma}-c y \ell}\left(M \backslash\left\{\check{p}_{1}, \ldots, \check{p}_{s}\right\}\right) \leq \min _{1 \leq j \leq s} \frac{Y\left(S^{n}\right)}{\left|\Gamma_{j}\right|^{\frac{2}{n}}},$$
where $h_{\Gamma}=h_{\Gamma_{j}}$ on the slice $S^{n-1} / \Gamma_{j}$ of each end $\left(S^{n-1} / \Gamma_{j}\right) \times[1, \infty)$, and $\left|\Gamma_{j}\right|$ denotes the order of $\Gamma_{j}$.
1.3. Harmonic spinors on cylindrical 4-manifolds. Our main goal is to obtain an estimate of the $h$-cylindrical Yamabe invariant for a general slice metric $h$ and, via Theorem A, the orbifold Yamabe invariant, by means of the Atiyah-Patodi-Singer $L^{2}$-index theory for cylindrical 4-manifolds. Indeed, in Section 3, we will give some estimates for the $h$-cylindrical Yamabe invariant from above, which can be regarded as a natural generalization of those for the Yamabe invariant obtained in Gursky-LeBrun [14].

Let $(X, \bar{g})$ be a cylindrical 4-manifold modeled by $(Z, h)$ for a metric $h$ on the slice $Z$. It means that on the end $Z \times[1, \infty)$, the metric $\bar{g}(z, t)=h(z)+d t^{2}$ is cylindrical with respect to a product coordinate system ( $z, t$ ). Then we use the notation that $\partial_{\infty} \bar{g}=h$. Now, we assume that there exists a spin ${ }^{c}$-structure on $(X, \bar{g})$ given by an element
$$a \in H^{2}(X ; \mathbf{Z}) \cap \operatorname{Im}\left[H_{c}^{2}(X ; \mathbf{R}) \rightarrow H^{2}(X ; \mathbf{R})\right]$$
which is not a torsion class, where $H_{c}^{2}(X ; \mathbf{R})$ denotes the second cohomology with compact support. Let L $\rightarrow X$ be the C-line bundle with $c_{1}(\mathrm{~L})=a$ and with the restriction $\mathrm{L}_{\mid Z \times[1, \infty)}$ being "cylindrical". Similarly to the case of compact manifolds, there exists a unique $L^{2}$-harmonic form $\zeta \in \mathcal{H}_{\bar{g}}^{2}(X)$ representing the cohomology class $a$. Note that the form $\zeta$ does not have compact support unless $a=0 \in H^{2}(X ; \mathbf{R})$. However, there exists a sequence $\left\{\zeta_{j}\right\}_{j=1}^{\infty}$ of closed 2-forms with compact support such that $\left[\zeta_{j}\right]=a$ and $\zeta_{j} \rightarrow \zeta$ in an appropriate topology. We choose $U(1)$-connections $A_{j}$ (with compact support) on $\mathrm{L} \rightarrow X$ such that $\frac{\sqrt{-1}}{2 \pi} F_{A_{j}}=\frac{\sqrt{-1}}{2 \pi} d A_{j}=\zeta_{j}$. Then, for each $j$, the associated twisted Dirac operator
$$\not \supset_{A_{j}}=\not \varnothing_{A_{j}}^{+}: \Gamma\left(\mathbf{S}_{\mathbf{C}}^{+}(a)\right) \rightarrow \Gamma\left(\mathbf{S}_{\mathbf{C}}^{-}(a)\right)$$
is defined, where $\mathrm{S}_{\mathrm{C}}^{ \pm}(a):=\mathrm{S}_{\mathrm{C}}^{ \pm} \otimes \mathrm{L}^{1 / 2}$ stands for the plus/minus spin bundle associated to L. Note that the $L^{2}$-index of $\not \partial_{A_{j}}$ is independent of $j$. We denote by $b_{2}^{-}(X)$ the total dimension of the negative eigenspaces of the intersection form on $H_{c}^{2}(X ; \mathbf{R})$. The following is the main result of Section 3 (Theorem 3.8).
Theorem C. Let $(X, \bar{g})$ be a cylindrical 4-manifold modeled by $(Z, h)$ with $b_{2}^{-}(X)=0$. Assume that the $L^{2}$-index of $\not \varnothing_{A_{j}}$ is positive. Then
$$Y^{h-c y \ell}(X) \leq \min \left\{4 \pi \sqrt{2 a^{2}}, Y_{\left[h+d t^{2}\right]}^{c y \ell}(Z \times \mathbf{R})\right\} .$$

The proof of Theorem C is subtle. We modify the argument due to Gursky-LeBrun [14], involving the Bochner technique and a generalization of the modified scalar curvature to the case of noncompact manifolds. One of the difficulties in the proof is the following: It turns out that a suitable conformal metric $\check{g}=u^{2} \cdot \bar{g}$ (where $u \in L_{\bar{g}}^{,,^{2}}(X)$ ) for this argument never provides a complete
metric on $X$ (see Lemmas 3.2 3.4 and the estimate (3.7) in Section 3). The main technical difficulty arises from this point. In order to overcome the difficulty, we have to estimate, for instance, the function $u^{-1}|d u|_{\bar{g}}$ uniformly on the cylindrical end $Z \times[1, \infty)$ (see Lemma 3.11).

We remark that the Hodge theorem and the Atiyah-Singer index theorem still hold for compact orbifolds (under some modifications) (cf. [19], [11]). Hence, if one considers only compact 4-orbifolds and their orbifold Yamabe invariants, the arguments for the estimate are more direct with the aid of these theorems. However, we establish here an estimate of the cylindrical Yamabe invariant for cylindrical 4-manifolds modeled by general compact Riemannian 3-manifolds. Moreover, the combination of conformal geometry and analysis on cylindrical manifolds is of independent value and leads to new interesting results (cf. [2], [3], [4]). Therefore, we rather deal with conformal geometry and analysis on cylindrical manifolds by means of the $L^{2}$-Hodge theory and the Atiyah-Patodi-Singer $L^{2}$-index theory.
14. Examples. Here we present particular cylindrical 4-manifolds $X_{\ell}$ defined as follows. Let $\mathrm{L} \rightarrow \mathbf{C P}^{1}$ be the anti-canonical $\mathbf{C}$-line bundle over $\mathbf{C P}^{1}$, and $\mathrm{L}_{\ell}:=\mathrm{L}^{\otimes \ell} \rightarrow \mathbf{C P}^{1}$ for $\ell \geq 1$. Then, let $X_{\ell}$ denote the total space of the bundle $\mathrm{L}_{\ell} \rightarrow \mathbf{C P}^{1}$, which will be naturally the underlying smooth open manifold (with a connected tame end) of a cylindrical manifold. For any cylindrical metric $\bar{g}$ on $X_{\ell}$, the cylindrical end of $X_{\ell}$ is reprented by ( $\left(S^{3} / \Gamma_{\ell}\right) \times[1, \infty), h+$ $d t^{2}$ ) with a metric $h$ on $S^{3} / \Gamma_{\ell}$, where $\Gamma_{\ell}:=\mathbf{Z} / \ell \mathbf{Z}$. Note that the one-point compactification $M_{\ell}:=X_{\ell} \cup\left\{\check{p}_{\infty}\right\}$ of $X_{\ell}$ has a natural orbifold structure with one singularity $\Sigma_{\Gamma}=\left\{\left(\check{p}_{\infty}, \Gamma_{\ell}\right)\right\}$. The main result of Section 4 is the following estimate (Theorem 4.1):
Theorem D. With the above understood, let $\mathcal{R i e m}^{+}\left(S^{3} / \Gamma_{\ell}\right)$ denote the space of metrics of positive scalar curvature on $S^{3} / \Gamma_{\ell}$.
\begin{itemize}
\item[(1)] For $\ell \geq 1$ and any metric $h \in \mathcal{R i e m}^{+}\left(S^{3} / \Gamma_{\ell}\right)$ homotopic to $h_{\Gamma_{\ell}}$ in $\operatorname{Riem}^{+}\left(S^{3} / \Gamma_{\ell}\right)$,
$$0<Y^{h-c y \ell}\left(X_{\ell}\right) \leq \min \left\{4 \pi(\ell+2) \sqrt{\frac{2}{\ell}}, Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(\left(S^{3} / \Gamma_{\ell}\right) \times \mathbf{R}\right)\right\} .$$
\item[(2)] For any metric $h \in \mathcal{R}$ iem $\left(S^{3} / \Gamma_{\ell}\right)$ which is sufficiently $C^{2}$-close to $h_{\Gamma_{\ell}}$,
$$\begin{array}{r}
0<Y^{h-c y \ell}\left(X_{\ell}\right) \leq \begin{cases}12 \sqrt{2} \pi=Y\left(\mathbf{C P}^{2}\right) & \text { if } \quad \ell=1, \\
Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(\left(S^{3} / \Gamma_{\ell}\right) \times \mathbf{R}\right) & \text { if } \quad \ell \geq 2 .\end{cases} \\
\text { In particular, } 0<Y^{\text {orb }}\left(M_{\ell}\right)=Y^{h_{\Gamma_{\ell}-c y \ell}}\left(X_{\ell}\right) \leq 8 \sqrt{\frac{6}{\ell}} \pi \text { for } \ell \geq 2 .
\end{array}$$
\end{itemize}
1.5. The plan of the paper. In Section 2 we define and study the orbifold Yamabe constant/invariant and prove Theorems A and B (Theorem 2.9 and Corollary 2.10). In Section 3 we define and study the modified scalar curvature. Then we review the necessary part of the $L^{2}$-index theory and prove

Theorem C (Theorem 3.8). Section 4 is devoted to the above examples and Theorem D (Theorem 4.1).
1.6. Acknowledgements. Both authors are grateful to Harish Seshadri for interesting discussions. The first author is grateful to the Department of Mathematics at the University of Oregon for kind hospitality. The first author also would like to thank Tosiaki Kori and Mikio Furuta for useful comments on eta invariants and the Atiyah-Singer index theorem over orbifolds, respectively.

\section*{2 Orbifold Yamabe constants/invariants}
2.1. Orbifolds with a finite number of singularities: definitions. There are several different approaches to and definitions of orbifolds (cf. [28], [17]). Since we work here with orbifolds of a particular type, i.e., with only a finite number of singularities, we give suitable definitions (cf. [21]). We assume here that a finite group $\Gamma$ of the $n$-dimensional orthogonal group $O(n)$ inherits the standard $O(n)$-action on $\mathbf{R}^{n}$. We always assume that $n \geq 3$.

First we define orbifolds with a finite number of singularities as an object in smooth category.

Definition 2.1 Let $M$ be a locally compact Hausdorff space. We say that $M$ is an $n$-dimensional orbifold with singularities
$$\Sigma_{\Gamma}=\left\{\left(\check{p}_{1}, \Gamma_{1}\right), \ldots,\left(\check{p}_{s}, \Gamma_{s}\right)\right\}$$
if the following conditions are satisfied:
\begin{itemize}
\item[(1)] $\Sigma=\left\{\check{p}_{1}, \ldots, \check{p}_{s}\right\} \subset M$, and $M \backslash \Sigma$ is a smooth manifold of dimension $n$.
\item[(2)] $\Gamma=\left\{\Gamma_{1}, \ldots, \Gamma_{s}\right\}$ is the collection of subgroups $\Gamma_{j}$ of $O(n)$. Each group $\Gamma_{j}(j=1, \ldots, s)$ is a nontrivial finite subgroup of $O(n)$ acting freely on $\mathbf{R}^{n} \backslash\{0\}$.
\item[(3)] For each $j(j=1, \ldots, s)$, there exist an open neighborhood $U_{j}$ of $\check{p}_{j}$ and a homeomorphism $\varphi_{j}: U_{j} \rightarrow \mathbf{B}_{\tau_{j}}(0) / \Gamma_{j}$ for some $\tau_{j}>0$ such that the restriction $\varphi_{j}: U_{j} \backslash\left\{\check{p}_{j}\right\} \rightarrow\left(\mathbf{B}_{\tau_{j}}(0) / \Gamma_{j}\right) \backslash\{0\}$ is a diffeomorphism. Here $\mathbf{B}_{\tau_{j}}(0)=\left\{x=\left(x^{1}, \ldots, x^{n}\right) \in \mathbf{R}^{n}| | x \mid<\tau_{j}\right\}$.
\end{itemize}

We refer to the pair $\left(\check{p}_{j}, \Gamma_{j}\right)$ as a singular point with the structure group $\Gamma_{j}$ and the pair $\left(U_{j}, \varphi_{j}\right)$ as a local uniformization. Let $\pi_{j}: \mathbf{B}_{\tau_{j}}(0) \rightarrow \mathbf{B}_{\tau_{j}}(0) / \Gamma_{j}$ denote the canonical projection.

Definition 2.2 Let $\widetilde{U}_{j}$ be an open neighborhood of $\check{p}_{j}$ and $\widetilde{\varphi}_{j}: \widetilde{U}_{j} \rightarrow \mathbf{B}_{\tilde{\tau}_{j}}(0) / \Gamma_{j}$ a homeomorphism (for some $\tilde{\tau}_{j}>0$ ). We call the pair $\left(\widetilde{U}_{j}, \widetilde{\varphi}_{j}\right)$ a compatible local uniformization of $\left(\check{p}_{j}, \Gamma_{j}\right)$ if the following conditions are satisfied:
\begin{itemize}
\item[(1)] The restriction $\widetilde{\varphi}_{j}: \widetilde{U}_{j} \backslash\left\{\check{p}_{j}\right\} \rightarrow\left(\mathbf{B}_{\widetilde{\tau}_{j}}(0) \backslash\{0\}\right) / \Gamma_{j} \quad$ is a diffeomorphism.
\end{itemize}
\begin{itemize}
\item[(2)] There exists a $\Gamma_{j}$-equivariant diffeomorphism $\Phi_{j}: \mathbf{B}_{\hat{\tau}_{j}}(0) \rightarrow \mathbf{B}_{\widetilde{\tau}_{j}}(0)$ for some $0<\hat{\tau}_{j} \leq \tau_{j}$ (possibly not onto) such that
$$\pi_{j}^{*}\left(\widetilde{\varphi}_{j} \circ \varphi_{j}^{-1}\right)=\tilde{\pi}_{j} \circ \Phi_{j} \quad \text { on } \quad \mathbf{B}_{\hat{\tau}_{j}}(0) \backslash\{0\},$$
where $\tilde{\pi}_{j}: \mathbf{B}_{\tilde{\tau_{j}}}(0) \rightarrow \mathbf{B}_{\tilde{\tau_{j}}}(0) / \Gamma_{j}$ denotes also the canonical projection.
\end{itemize}

To simplify the presentation, we assume, without particular mention, that an orbifold $M$ has only one singularity, i.e., $\Sigma_{\Gamma}=\{(\check{p}, \Gamma)\}$. Let $\varphi: U \rightarrow \mathbf{B}_{\tau}(0) / \Gamma$ be a local uniformization and $\pi: \mathbf{B}_{\tau}(0) \rightarrow \mathbf{B}_{\tau}(0) / \Gamma$ the canonical projection. We also always assume that $M$ is compact. Now we give the definition of orbifold metrics.

Definition 2.3 A Riemannian metric $g \in \mathcal{R} \operatorname{iem}(M \backslash\{\check{p}\})$ is an orbifold metric if there exists a $\Gamma$-invariant smooth metric $\hat{g}$ on the disk $\mathbf{B}_{\tau}(0)$ such that $\left(\varphi^{-1} \circ \pi\right)^{*} g=\hat{g}$ on $\mathbf{B}_{\tau}(0) \backslash\{0\}$.

We denote by $\mathcal{R} \operatorname{iem}^{\text {orb }}(M)$ the space of all orbifold metrics on $M$.
Remark 2.1 We note that if $g \in \mathcal{R} i e m{ }^{\text {orb }}(M)$, then $R_{\hat{g}} \in C^{\infty}\left(\mathbf{B}_{\tau}(0)\right)$, and hence the scalar curvature $R_{g}$ extends to a continuous function on $M$. \(\square\)

In the case when $\Sigma_{\Gamma}=\left\{\left(\check{p}_{1}, \Gamma_{1}\right), \ldots,\left(\check{p}_{s}, \Gamma_{s}\right)\right\}$, the space $\mathcal{R} \operatorname{iem}^{\text {orb }}(M)$ of orbifold metrics is defined similarly.
2. 2. Einstein orbifold metrics. Let $M$ be a compact orbifold with a singularity $\Sigma_{\Gamma}=\{(\check{p}, \Gamma)\}$. Consider the (normalized) Einstein-Hilbert functional
$$I: \mathcal{R} \mathrm{iem}^{\text {orb }}(M) \rightarrow \mathbf{R}, \quad g \mapsto \frac{\int_{M} R_{g} d \sigma_{g}}{\operatorname{Vol}_{g}(M)^{\frac{n-2}{n}}} .$$
As in the case of smooth compact manifolds, we have the following fundamental result since the Stokes formula and the divergence theorem still hold over orbifolds.

Proposition 2.1 The set of critical points of $I: \mathcal{R i e m}^{\text {orb }}(M) \rightarrow \mathbf{R}$ coincides with the set of Einstein orbifold metrics on $M$.
2. 3. Orbifold conformal classes. We say that two orbifold metrics $g, \widetilde{g} \in$ $\mathcal{R} \operatorname{iem}^{\text {orb }}(M)$ are pointwise conformal if there exists a function $f \in C^{0}(M) \cap$ $C^{\infty}(M \backslash\{\check{p}\})$ such that
$$\left\{\begin{array}{l}
\widetilde{g}=e^{2 f} \cdot g \text { on } M \backslash\{\check{p}\} \\
\left(\varphi^{-1} \circ \pi\right)^{*} f \in C^{\infty}\left(\mathbf{B}_{\tau}(0)\right) .
\end{array}\right.$$
Here we used the composition of the maps $\mathbf{B}_{\tau}(0) \xrightarrow{\pi} \mathbf{B}_{\tau}(0) / \Gamma \xrightarrow{\varphi^{-1}} U \xrightarrow{f} \mathbf{R}$. Then we define an orbifold conformal class of $g$ as follows:
$$[g]_{\text {orb }}:=[g] \cap \mathcal{R i e m}^{\text {orb }}(M)=\left\{\begin{array}{l|l}
e^{2 f} \cdot g & \begin{array}{l}
f \in C^{0}(M) \cap C^{\infty}(M \backslash\{\check{p}\}), \\
\left(\varphi^{-1} \circ \pi\right)^{*} f \in C^{\infty}\left(\mathbf{B}_{\tau}(0)\right)
\end{array}
\end{array}\right\} .$$

Let $\mathcal{C}^{\text {orb }}(M)$ denote the space of all orbifold conformal classes. The proofs of the following two lemmas are similar to the case of smooth compact manifolds (see [6, 18]).

Lemma 2.2 Let $g \in \mathcal{R i e m}^{\text {orb }}(M)$ be a metric satisfying one of the following conditions: $R_{g}>0, R_{g} \equiv 0$ or $R_{g}<0$ everywhere on $M$. Then for another such metric $\tilde{g} \in[g]_{\text {orb }}$, the sign of $R_{\tilde{g}}$ is identical with the sign of $R_{g}$.

Lemma 2.3 Let $g \in \mathcal{R i e m}^{\text {orb }}(M)$ be a metric with $R_{g} \equiv$ const. $\leq 0$. Then for any metric $\tilde{g} \in[g]_{\text {orb }}$ with $R_{\tilde{g}} \equiv$ const., there exists a constant $k>0$ such that $\tilde{g}=k \cdot g$.

An orbifold $M$ is called good if its universal cover $\widetilde{M}$ is a smooth manifold (cf. [17]). Let $\pi: \widetilde{M} \rightarrow M$ be the projection.

Proposition 2.4 Let $g \in \mathcal{R i e m}^{\text {orb }}(M)$ be an Einstein metric with $R_{g} \equiv$ const. $>0$. Then any metric $\tilde{g} \in[g]_{\text {orb }}$ with $R_{\tilde{g}} \equiv$ const . is also Einstein. Furthermore, if $M$ is a good orbifold, then $\tilde{g}=k \cdot g$ for a constant $k>0$ unless $\left(\widetilde{M}, \pi^{*} g\right)$ is isometric to $\left(S^{n}, g_{S}\right)$, where $g_{S} \in \operatorname{Riem}\left(S^{n}\right)$ denotes the standard metric of constant curvature one.

Proof. The first statement follows directly from the proof of Proposition 1.4 in [29] combined with the divergence theorem for orbifolds (see also [12, Section 2]).

Now assume that the universal cover $\widetilde{M}$ is a smooth manifold. Let $\pi$ : $\widetilde{M} \rightarrow M$ denote the projection. Let $\widetilde{g}=u^{\frac{4}{n-2}} \cdot g$ be an orbifold metric with $R_{\tilde{g}} \equiv$ const. on $M$. Then unless $\left(\widetilde{M}, \pi^{*} g\right) \cong\left(S^{n}, g_{S}\right)$, [26, Theorem A] implies that $\pi^{*} u \equiv$ const. $>0$ on $\widetilde{M}$, and hence $u \equiv$ const. $>0$ on $M$. \(\square\)
2.4. Orbifold Yamabe constants/invariants. We define the orbifold Yamabe constant $Y_{[g]_{\text {orb }}}(M)$ of ( $M,[g]_{\text {orb }}$ ) as follows:
$$Y_{[g]_{\mathrm{orb}}}(M):=\inf _{\widetilde{g} \in[g]_{\mathrm{orb}}} \frac{\int_{M} R_{\widetilde{g}} d \sigma_{\widetilde{g}}}{\operatorname{Vol}_{\widetilde{g}}(M)^{\frac{n-2}{n}}} .$$
Similarly to the case of smooth compact manifolds, we have Aubin's inequality $-\infty<Y_{[g]_{\text {orb }}}(M) \leq Y\left(S^{n}\right)$ (cf. [6]). Then we define the orbifold Yamabe invariant of $M$
$$Y^{\text {orb }}(M):=\sup _{C \in \mathcal{C}^{\text {orb }}(M)} Y_{C}(M) \quad\left(\leq Y\left(S^{n}\right)\right) .$$
Now we state some technical facts without proofs. The following result also follows from the divergence theorem for orbifolds.

Lemma 2.5 For an orbifold metric $\widetilde{g} \in[g]_{\text {orb }}$ with $\widetilde{g}=u^{\frac{4}{n-2}} g$, then
$$\int_{M} R_{\widetilde{g}} d \sigma_{\widetilde{g}}=\int_{M}\left(\alpha_{n}|d u|_{g}^{2}+R_{g} u^{2}\right) d \sigma_{g}, \quad \text { where } \quad \alpha_{n}=\frac{4(n-1)}{n-2}>0 .$$

We consider the Yamabe functional
$$Q_{g}(u):=\frac{E_{g}(u)}{\left(\int_{M}|u|^{\frac{2 n}{n-2}} d \sigma_{g}\right)^{\frac{n-2}{n}}}=\frac{\int_{M}\left(\alpha_{n}|d u|_{g}^{2}+R_{g} u^{2}\right) d \sigma_{g}}{\left(\int_{M}|u|^{\frac{2 n}{n-2}} d \sigma_{g}\right)^{\frac{n-2}{n}}}$$
for any $u \in C^{0}(M) \cap C^{\infty}(M \backslash\{p\})$ with $u \not \equiv 0$ and $\left(\varphi^{-1} \circ \pi\right)^{*} u \in C^{\infty}\left(\mathbf{B}_{\tau}(0)\right)$.

Remark 2.2 We recall that for a compact smooth manifold $N$ of $\operatorname{dim} N \geq 3$, any point $q \in N$ and any metric $h \in \mathcal{R} \operatorname{iem}(N)$, the Yamabe constant $Y_{[h]}(N)$ satisfies
$$Y_{[h]}(N)=\inf _{\substack{u \in C_{c}^{\infty}(N \backslash\{q\}) \\ u \not \equiv 0}} Q_{h}(u) .$$
The orbifold Yamabe constant has a similar property.
Lemma 2.6 The orbifold Yamabe constant $Y_{[g]_{\text {orb }}}(M)$ satisfies
$$Y_{[g]_{\text {orb }}}(M)=\inf _{\substack{u \in C_{c}^{\infty}(M \backslash\{\check{p}\}) \\ u \not \equiv 0}} Q_{g}(u) .$$
Here $\check{p}$ is the singular point of $M$.
2.5. Approximation for orbifold metrics. At the singular point $\check{p} \in$ $U(\subset M)$, we prove the following approximation, which is an orbifold version of Kobayashi's approximation lemma ([20, Lemma 3.2]). This approximation is a crucial tool linking the orbifold Yamabe invariant to the corresponding $h$-cylindrical Yamabe invariant.

Proposition 2.7 Let $g \in \mathcal{R i e m}^{\text {orb }}(M)$ be an orbifold metric and $\hat{g} \in \mathcal{R} \operatorname{iem}\left(\mathbf{B}_{\tau}(0)\right)$ the lifting metric with $\hat{g}=\left(\varphi^{-1} \circ \pi\right)^{*} g$ on $\mathbf{B}_{\tau}(0) \backslash\{0\}$. Let $y=\left(y^{1}, \ldots, y^{n}\right) d e-$ note normal coordinates with respect to $\hat{g}$ on an open neighborhood $\mathbf{U}\left(\subset \mathbf{B}_{\tau}(0)\right)$ of 0, and $\mathbf{U}_{\rho}=\left\{y \in \mathbf{U}\left|\operatorname{dist}_{\hat{g}}(0, y)=|y|<\rho\right\}\right.$ for small $\rho>0$. Then for any small $\delta>0$ there exists a metric $g_{\delta} \in \mathcal{R} \operatorname{iem}^{\text {orb }}(M)$ such that:
\begin{itemize}
\item[(1)] $g_{\delta}=g$ on $M \backslash V_{\delta}$, where $V_{\delta}=\left\{q \in M \mid \operatorname{dist}_{g}(\check{p}, q)<\delta\right\}$,
\item[(2)] $\hat{g}_{\delta}=\left(\varphi^{-1} \circ \pi\right)^{*} g_{\delta}$ is pointwise conformal to the flat metric $\sum_{i=1}^{n}\left(d y^{i}\right)^{2}$ on $\mathbf{U}_{\varepsilon(\delta)}(0) \backslash\{0\}$ for a constant $\varepsilon(\delta)(0<\varepsilon(\delta)<\delta)$, where $\hat{g}_{\delta} \in \operatorname{Riem}\left(\mathbf{B}_{\tau}(0)\right)$ denotes the corresponding lifting metric to $g_{\delta}$,
\item[(3)] $g_{\delta} \rightarrow g$ uniformly on $M \backslash\{\check{p}\}$ and $\hat{g}_{\delta} \rightarrow \hat{g}$ uniformly on $\mathbf{B}_{\tau}(0)$ as $\delta \rightarrow 0$,
\item[(4)] $R_{g_{\delta}} \rightarrow R_{g}$ uniformly on $M$ as $\delta \rightarrow 0$.
\end{itemize}

Proof. Let $g_{0}=\sum_{i=1}^{n}\left(d y^{i}\right)^{2}$ be the flat metric on U. Then
$$\hat{g}(y)=g_{0}(y)+O\left(|y|^{2}\right) \quad \text { on } \quad \mathbf{U} .$$
Since $\hat{g}$ is $\Gamma$-invariant, the exponential map (with respect to $\hat{g}$ ) commutes with $\Gamma$, and hence the flat metric $g_{0}$ and the distance function $\operatorname{dist}_{\hat{g}}(0, y)=|y|$ from 0 to $y$ are also $\Gamma$-invariant. Moreover, ( $\mathbf{U}, y=\left(y^{1}, \ldots, y^{n}\right)$ ) is a compatible local uniformization. We denote $\kappa:=R_{\hat{g}}(0)$, and consider the metric
$$\tilde{g}:=\left(1-\frac{\kappa}{2 \alpha_{n}}|y|^{2}\right)^{\frac{4}{n-2}} \cdot g_{0} \quad \text { on } \quad \mathbf{U} .$$
Then it follows that $R_{\tilde{g}}(0)=\kappa=R_{\hat{g}}(0)$. Now we use the cut-off function $w_{\delta}$ (given in [20]) to construct the following approximation $\hat{g}_{\delta}$ :
$$\hat{g}_{\delta}:=\hat{g}+w_{\delta}(r)(\tilde{g}-\hat{g}) \quad \text { on } \quad \mathbf{B}_{\tau}(0), \quad r=|y| .$$
Since $j_{0}^{1}(\tilde{g})=j_{0}^{1}(\hat{g})$ and $R_{\tilde{g}}(0)=R_{\hat{g}}(0)$, Kobayashi's approximation technique [20] implies that $\hat{g}_{\delta}$ satisfies the above conditions (1)-(4) on $\mathbf{B}_{\tau}(0)$. By the construction, the metrics $\hat{g}, \tilde{g}$ and the function $w_{\delta}$ are $\Gamma$-invariant, and hence the metric $\hat{g}_{\delta}$ is also $\Gamma$-invariant. This implies that there exists an orbifold metric $g_{\delta} \in \mathcal{R} \operatorname{iem}^{\text {orb }}(M)$ such that $\hat{g}_{\delta}=\left(\varphi^{-1} \circ \pi\right)^{*} g_{\delta}$. Then the metric $g_{\delta}$ satisfies the above conditions (1)-(4). \(\square\)

The following lemma is an analogue of the case of smooth compact manifolds (cf. [7, 20]).

Lemma 2.8 Let $g_{\delta}, g \in \mathcal{R i e m}^{\text {orb }}(M)$ be metrics satisfying
$$g_{\delta} \rightarrow g \quad \text { and } \quad R_{g_{\delta}} \rightarrow R_{g} \quad \text { uniformly on } M \text { as } \delta \rightarrow 0 .$$
Then $Y_{\left[g_{\delta}\right]_{\text {orb }}}(M) \rightarrow Y_{[g]_{\text {orb }}}(M)$ as $\delta \rightarrow 0$.
2.6. Orbifold and $h$-cylindrical Yamabe invariants. We recall briefly the following: The open manifold $M \backslash\{\check{p}\}$ equipped with an appropriate cylindrical metric can be considered as a cylindrical manifold (see 3 or Section 3). For a complete metric $\bar{g} \in \mathcal{R} i e m(M \backslash\{\check{p}\})$, the open manifold $(M \backslash\{\check{p}\}, \bar{g})$ is called a cylindrical manifold modeled by $\left(S^{n-1} / \Gamma, h_{\Gamma}\right)$ if there exist an open neighborhood $V(\subset U)$ of $\check{p}$ and a coordinate system $(z, t) \in\left(S^{n-1} / \Gamma\right) \times[0, \infty) \cong V \backslash\{\check{p}\}$ such that
$$\bar{g}(z, t)=h_{\Gamma}(z)+d t^{2} \quad \text { on } \quad\left(S^{n-1} / \Gamma\right) \times[1, \infty) .$$
The cylindrical Yamabe constant $Y_{[\bar{g}]}^{c y \ell}(M \backslash\{\check{p}\})$ is defined by
$$Y_{[\bar{g}]}^{c y \ell}(M \backslash\{\check{p}\}):=\inf _{\substack{u \in C_{c}^{\infty}(M \backslash\{\check{p}\}) \\ u \not \equiv 0}} Q_{\bar{g}}(u) \quad\left(\leq Y\left(S^{n}\right)\right) .$$

Let $\operatorname{Riem}^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\})(\subset \mathcal{R} i e m(M \backslash\{\check{p}\}))$ be the space of cylindrical metrics modeled by $\left(S^{n-1} / \Gamma, h_{\Gamma}\right)$. Then the $h_{\Gamma}$-cylindrical Yamabe invariant $Y^{h_{\Gamma^{-} c y \ell}}(M \backslash\{\check{p}\})$ is also defined by
$$Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\}):=\sup _{\bar{g} \in \mathcal{R}_{i \operatorname{em}^{h^{-}}{ }^{-c y \ell}}(M \backslash\{\check{p}\})} Y_{[\bar{g}]}^{c y \ell}(M \backslash\{\check{p}\}) \quad\left(\leq Y\left(S^{n}\right)\right) .$$

Theorem 2.9 Let $M$ be a compact orbifold with a singularity $\Sigma_{\Gamma}=\{(\check{p}, \Gamma)\}$. Then $Y^{\text {orb }}(M)=Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\})$.

Theorem 2.9 and 3, Propositions 2.11, 2.12, 6.5] imply the following result.
Corollary 2.10 Let $M$ be a compact orbifold with singularities $\Sigma_{\Gamma}=$ $\left\{\left(\check{p}_{1}, \Gamma_{1}\right), \ldots,\left(\check{p}_{s}, \Gamma_{s}\right)\right\}$. Then
$$Y^{\text {orb }}(M)=Y^{h_{\Gamma}-c y \ell}\left(M \backslash\left\{\check{p}_{1}, \ldots, \check{p}_{s}\right\}\right) \leq \min _{1 \leq j \leq s} \frac{Y\left(S^{n}\right)}{\left|\Gamma_{j}\right|^{\frac{2}{n}}} .$$
Proof of Theorem 2.9 First we prove that $Y^{\text {orb }}(M) \leq Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\})$. By Proposition 2.7 and Lemma 2.8 for any $\varepsilon>0$ and any metric $g \in \mathcal{R} \operatorname{iem}^{\text {orb }}(M)$ there exists a metric $g_{\varepsilon} \in \mathcal{R} \operatorname{iem}^{\text {orb }}(M)$ such that
$$\left\{\begin{array}{l}
\left|Y_{[g]_{\mathrm{orb}}}(M)-Y_{\left[g_{\varepsilon}\right]_{\mathrm{orb}}}(M)\right|<\varepsilon \\
\left(\varphi^{-1} \circ \pi\right)^{*} g_{\varepsilon} \simeq g_{0}=\sum_{i=1}^{n}\left(d x^{i}\right)^{2}: \text { pointwise conformal near } 0 \in \mathbf{B}_{\tau}(0) .
\end{array}\right.$$
Let $\bar{g}_{\varepsilon} \in[g]_{\text {orb }}$ be a cylindrical metric on $M \backslash\{\check{p}\}$ with $\bar{g}_{\varepsilon}(z, t)=h_{\Gamma}(z)+d t^{2}$ on the end $\left(S^{n-1} / \Gamma\right) \times[1, \infty) \cong V \backslash\{\check{p}\}$. Then we use Lemma 2.6 to show
$$\begin{aligned}
Y_{\left[g_{\varepsilon}\right]_{\text {orb }}}(M)= & \inf _{\substack{u \in C_{c}^{\infty}(M \backslash\{\check{p}\}) \\
u \not \equiv 0}} Q_{g_{\varepsilon}}(u)=\inf _{\substack{u \in C_{c}^{\infty}(M \backslash\{\check{p}\}) \\
u \not \equiv 0}} Q_{\bar{g}_{\varepsilon}}(u) \\
= & Y_{\left[\bar{g}_{\varepsilon}\right]}^{c y \ell}(M \backslash\{\check{p}\}) \leq Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\}) .
\end{aligned}$$
This implies that $Y^{\text {orb }}(M) \leq Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\})$.
Second we prove that $Y^{\text {orb }}(M) \geq Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\})$. We start with an arbitrary cylindrical metric $\bar{g} \in \mathcal{R i e m}^{h_{\Gamma^{-}} c y \ell}(M \backslash\{\check{p}\})$ and a cylindrical coordinate system $(z, t) \in\left(S^{n-1} / \Gamma\right) \times[1, \infty) \cong V \backslash\{\check{p}\}$ as above.

Set $r=e^{-t}$, then $\bar{g}(z, t)=r^{-2}\left(d r^{2}+r^{2} \cdot h_{\Gamma}(z)\right)$ on the cylinder $\left(S^{n-1} / \Gamma\right) \times$ $[1, \infty)$. Note that on $\left(S^{n-1} / \Gamma\right) \times[1, \infty)$ the metric $r^{2} \cdot \bar{g}(z, t)=d r^{2}+r^{2} \cdot h_{\Gamma}(z)$ is flat and is extended to a smooth metric $g_{0}$ on $M \backslash\{\check{p}\}$. This implies that there exists a homeomorphism $\tilde{\varphi}: \tilde{U} \rightarrow \mathbf{B}_{\tilde{\tau}}(0) / \Gamma$ for a constant $\tilde{\tau}>0$ such that
\begin{itemize}
\item[(1)] $\tilde{\varphi}:(\tilde{U} \backslash\{\check{p}\}) \rightarrow\left(\mathbf{B}_{\tilde{\tau}}(0) \backslash\{0\}\right) / \Gamma$ is a diffeomorphism,
\end{itemize}
\begin{itemize}
\item[(2)] $\left(\tilde{\varphi}^{-1} \circ \tilde{\pi}\right)^{*} g_{0}=\sum_{i=1}^{n}\left(d y^{i}\right)^{2}$, where $y=\left(y^{1}, \ldots, y^{n}\right) \in \tilde{U}$ are normal coordinates around $\check{p}$ with respect to $g_{0}$,
\item[(3)] the diffeomorphism $\tilde{\varphi} \circ \varphi^{-1}$ is lifted to a $\Gamma$-equivariant diffeomorphism $\Phi: \mathbf{B}_{\hat{\tau}}(0) \rightarrow \mathbf{B}_{\tilde{\tau}}(0)$ onto its image for a constant $0<\hat{\tau} \leq \tau$.
\end{itemize}
In other words, $(\tilde{U}, \tilde{\varphi})$ is a compatible local uniformization, and the above metric $g_{0}$ is an orbifold metric on $M$. ¿From Lemma 2.6 we obtain that
$$Y_{\left[g_{0}\right]_{\text {orb }}}(M)=\inf _{\substack{u \in C_{c}^{\infty}(M \backslash\{\check{p}\}) \\ u \not \equiv 0}} Q_{g_{0}}(u)=\inf _{\substack{u \in C_{c}^{\infty}(M \backslash\{\check{p}\}) \\ u \not \equiv 0}} Q_{\bar{g}}(u)=Y_{[\bar{g}]}^{c y \ell}(M \backslash\{\check{p}\}) .$$
This implies that $Y^{\text {orb }}(M) \geq Y^{h_{\Gamma}-c y \ell}(M \backslash\{\check{p}\})$. \(\square\)

\section*{$3 L^{2}$-harmonic spinors and Yamabe invariant}
3.1. Modified scalar curvature. Throughout the rest of the paper, we consider only 4-manifolds. Let $X$ be an open smooth 4-manifold with tame ends, i.e., it is diffeomorphic to $W \cup_{Z}(Z \times[0, \infty))$, where $W(\subset X)$ is a compact submanifold of $\operatorname{dim} W=4$ with boundary $\partial W \cong Z \times\{0\}$ (possibly disconnected), see Fig. 31.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/1263542e-b2a8-4701-ae56-b4f3796ca39c-11.jpg?height=299&width=1086&top_left_y=1381&top_left_x=531}
\captionsetup{labelformat=empty}
\caption{Fig. 31. Cylindrical manifold $(X, \bar{g})$.}
\end{figure}
Let $\mathcal{R} \mathrm{iem}^{c y \ell}(X)$ denote the space of all cylindrical metrics on $X$. We choose a cylindrical metric $\bar{g} \in \mathcal{R i e m}^{\text {cyl }}(X)$. In terms of [3], $(X, \bar{g})$ is a cylindrical 4-manifold modeled by $(Z, h)$ for $h \in \mathcal{R}$ iem $(Z)$ if there exists a product coordinate system ( $z, t$ ) on the end $Z \times[0, \infty)$ such that $\bar{g}(z, t)=h(z)+d t^{2}$ on $Z \times[1, \infty)$. Below we use the notation that $\partial_{\infty} \bar{g}=h$.

Let $\omega \in \Omega^{2}(X)$ be a 2-form. We denote by $\mathbb{L}_{\bar{g}}=-6 \Delta_{\bar{g}}+R_{\bar{g}}$ the conformal Laplacian of $\bar{g}$. We define the modified conformal Laplacian $\mathbb{L}_{(\bar{g}, \omega)}$ of $(\bar{g}, \omega)$ by
$$\mathbb{L}_{(\bar{g}, \omega)}:=\mathbb{L}_{\bar{g}}-|\omega|_{\bar{g}}=-6 \Delta_{\bar{g}}+\left(R_{\bar{g}}-|\omega|_{\bar{g}}\right) .$$
Note that the pointwise norm $|\omega|_{\bar{g}}$ is only of $C^{1,0}$ class on $X$, in general.
Fact 3.1 (cf. [14]) Set $\check{g}=u^{2} \cdot \bar{g}$ for $u \in C_{+}^{\infty}(X)$. Then $\mathbb{L}_{\check{g}}(f)=u^{-3} \cdot \mathbb{L}_{\bar{g}}(u f)$ for $f \in C^{2}(X)$.

Definition 3.1 (Gursky-LeBrun [13, 14]) For $\bar{g} \in \mathcal{R i e m}^{c y \ell}(X)$, let $\check{g}=u^{2} \cdot \bar{g}$ be a conformal metric, where $u \in C_{+}^{\infty}(X)$. We call the function $R_{(\check{g}, \omega)}:=R_{\check{g}}-|\omega|_{\check{g}}$ the modified scalar curvature of $(\check{g}, \omega)$.

Set $E_{(\bar{g}, \omega)}(f):=\int_{X}\left[6|d f|_{\bar{g}}^{2}+\left(R_{\bar{g}}-|\omega|_{\bar{g}}\right) f^{2}\right] d \sigma_{\bar{g}}$ for $f \in L_{\bar{g}}^{1,2}(X)$, where $L_{\bar{g}}^{1,2}(X)$ denotes the Sobolev space of square-integrable functions on $X$ (with respect to $\bar{g}$ ) up to their first weak derivatives. Then we consider the functional
$$\mathbb{Q}_{(\bar{g}, \omega)}(f):=\frac{E_{(\bar{g}, \omega)}(f)}{\int_{X} f^{2} d \sigma_{\bar{g}}} \quad \text { for } \quad f \in L_{\bar{g}}^{1,2}(X) \text { with } f \not \equiv 0$$
and the bottom of the spectrum of the operator $\mathbb{L}_{(\bar{g}, \omega)}$
$$\lambda_{(\bar{g}, \omega)}:=\inf _{\substack{f \in L_{\bar{g}}^{1,2}(X) \\ f \not \equiv 0}} \mathbb{Q}_{(\bar{g}, \omega)}(f) .$$
¿From now on we assume that the 2-form $\omega$ has a compact support.
Lemma 3.1 For $\bar{g} \in \mathcal{R i e m}^{c y \ell}(X)$ and $\omega \in \Omega_{\mathrm{c}}^{2}(X)$ as above, $\lambda_{(\bar{g}, \omega)}>-\infty$.
Proof. Indeed, $\lambda_{(\bar{g}, \omega)} \geq \inf _{X}\left(R_{\bar{g}}-|\omega|_{\bar{g}}\right)>-\infty$ since $\bar{g} \in \operatorname{Riem}^{c y \ell}(X)$ and $\omega \in \Omega_{\mathrm{c}}^{2}(X)$. \(\square\)

On the slice manifold $(Z, h)$, we consider the almost conformal Laplacian $\mathcal{L}_{h}:=-6 \Delta_{h}+R_{h}$ (see [3]).

Convention 1. From now on we always assume that $\lambda_{h}:=\lambda\left(\mathcal{L}_{h}\right)>0$, where $\lambda\left(\mathcal{L}_{h}\right)$ denotes the first eigenvalue of $\mathcal{L}_{h}$.

Remark 3.1 ([3, Section 2]) It is easy to see that the condition $R_{h}>0$ everywhere on $Z$ provides a sufficient condition for $\lambda_{h}>0$. On the other hand, if $\lambda_{h} \leq 0$, then $Y_{[\bar{g}]}^{c y \ell}(X) \leq 0$. Moreover, if $\lambda_{h}<0$, then $Y_{[\bar{g}]}^{c y \ell}(X)=-\infty$.

Lemma 3.2 Assume that $\lambda_{(\bar{g}, \omega)}<\lambda_{h}$. Then there exists a function $u \in$ $C_{+}^{2, \alpha}(X) \cap L_{\bar{g}}^{1,2}(X)$ (for any $0<\alpha<1$ ) such that $\mathbb{L}_{(\bar{g}, \omega)} u=\lambda_{(\bar{g}, \omega)} u$.

Proof. Consider the cylinder $Z \times[\ell, \infty)$ with $\ell \geq 1$ and denote $X(\ell):=$ $W \cup_{Z}(Z \times[0, \ell])$. Note that if there exists a constant $\ell \geq 1$ satisfying
$$\lambda(\ell):=\inf _{\substack{f \in C_{c}^{\infty}(Z \times[\ell, \infty)) \\ f \not \equiv 0}} \mathbb{Q}(\bar{g}, \omega)(f)>\lambda_{(\bar{g}, \omega)},$$
then the standard argument implies the existence of a non-zero minimizer $u \in C_{+}^{2, \alpha}(X) \cap L_{\bar{g}}^{1,2}(X)$ of the functional $\mathbb{Q}_{(\bar{g}, \omega)}$. Hence it is enough to prove
that $\lambda(\ell) \geq \lambda_{h}$ for a constant $\ell \geq 1$. We choose $\ell$ satisfying $\operatorname{Supp}(\omega) \subset X(\ell)$. Then $R_{\bar{g}}=R_{h}$ and $|\omega|_{\bar{g}}=0$ on $Z \times[\ell, \infty)$. Hence for any $f \in C_{c}^{\infty}(Z \times[\ell, \infty))$,
$$\begin{aligned}
\left.E_{(\bar{g}, \omega)}\right|_{Z \times[\ell, \infty)}(f) & =\int_{Z \times[\ell, \infty)}\left(6|d f|^{2}+\left(R_{\bar{g}}-|\omega|_{\bar{g}}\right) f^{2}\right) d \sigma_{\bar{g}} \\
& =\int_{[\ell, \infty)} d t \int_{Z}\left[6\left(\partial_{t} f\right)^{2}+6\left|\nabla^{Z} f\right|_{h}^{2}+R_{h} f^{2}\right] d \sigma_{h} \\
& \geq \int_{[\ell, \infty)} d t\left(\lambda_{h} \cdot \int_{Z} f^{2} d \sigma_{h}\right) \geq \lambda_{h} \cdot \int_{Z \times[\ell, \infty)} f^{2} d \sigma_{\bar{g}}
\end{aligned}$$
The next lemma shows that we may always assume the condition of Lemma 3.2 without loss of generality. The technique below of changing the given metric conformally within a compact set is known as the conformal-rescaling argument (see also the proofs of [2, Theorem 3] and [3, Proposition 7.3]).

Lemma 3.3 There exists a metric $\tilde{g} \in[\bar{g}]$ with $\tilde{g} \equiv \bar{g}$ on $X \backslash X(1)$ such that $\lambda_{(\tilde{g}, \omega)}<\lambda_{h}$. In particular, $\tilde{g} \in \operatorname{Riem}^{c y \ell}(X)$.

Proof. When $\lambda_{(\bar{g}, \omega)} \leq 0$, the inequality $\lambda_{(\bar{g}, \omega)}<\lambda_{h}$ is trivial. Hence we consider only the case when $\lambda_{(\bar{g}, \omega)}>0$. We change the cylindrical metric $\bar{g}$ to another cylindrical metric $\bar{g}_{v}=e^{2 v} \cdot \bar{g}$, where $v \in C^{\infty}(X)$ with
$$v=\left\{\begin{array}{l}
k \equiv \text { const. }>0 \text { on } W=X \backslash(Z \times(0, \infty)), \\
0 \text { on } Z \times[1, \infty) .
\end{array}\right.$$
In particular, $\mathbb{L}_{\left(\bar{g}_{v}, \omega\right)}=e^{-2 k} \cdot \mathbb{L}_{\left(\bar{g}_{v}, \omega\right)}$ on $W$. We choose $k \gg 1$ sufficiently large. Then the Dirichlet first eigenvalue $\lambda_{\left(\bar{g}_{v}, \omega\right)}(W)$ on $W$ satisfies that $\lambda_{\left(\bar{g}_{v}, \omega\right)}(W)<\lambda_{h}$. Hence by the domain monotonicity of the Dirichlet eigenvalues, we then obtain that $\lambda_{\left(\bar{g}_{v}, \omega\right)} \leq \lambda_{\left(\bar{g}_{v}, \omega\right)}(W)<\lambda_{h}$. To complete the proof, we let $\tilde{g}=\bar{g}_{v}$. \(\square\)

Convention 2. From now on we always assume that $\lambda_{(\bar{g}, \omega)}<\lambda_{h}$ since $Y_{[\tilde{g}]}^{c y \ell}(X)=Y_{[\bar{g}]}^{c y \ell}(X)$.
Lemmas 3.23 .3 imply the following lemma, whose proof is similar to the case of compact smooth manifolds (see [14]).

Lemma 3.4 There exists a function $u \in C_{+}^{2, \alpha}(X) \cap L_{\bar{g}}^{1,2}(X)$ (where $0<\alpha<1$ ) such that for the metric $\check{g}=u^{2} \cdot \bar{g}$
$$R_{(\check{g}, \omega)}\left\{\begin{array}{l}
>0 \\
\equiv 0 \\
<0
\end{array} \quad \text { everywhere on } X .\right.$$
Furthermore, these cases are mutually exclusive.

The next result follows from [3, Proposition 7.1].
Fact 3.2 Let $\bar{g}, \tilde{g} \in \bar{C} \cap \mathcal{R i e m}^{c y \ell}(X)$ be two cylindrical metrics which are pointwise conformal. Then $\operatorname{sign}\left(\lambda_{(\bar{g}, \omega)}\right)=\operatorname{sign}\left(\lambda_{(\tilde{g}, \omega)}\right)$.
Now for $\bar{g} \in \mathcal{R i e m}^{c y \ell}(X)$, let $[\bar{g}]_{L_{\bar{g}}^{1,2}}(\subset[\bar{g}])$ denote the $L_{\bar{g}}^{1,2}$-conformal class of $\bar{g}$ consisting of all metrics $u^{2} \cdot \bar{g}$, where $u \in C_{+}^{\infty}(X) \cap L_{\bar{g}}^{1,2}(X)$ (see 3). Note that the $L_{\bar{g}}^{2}$-norm $\|\zeta\|_{L_{\bar{g}}^{2}}:=\left(\int_{X}|\zeta| \frac{2}{\bar{g}} d \sigma_{\bar{g}}\right)^{\frac{1}{2}}$ of $\zeta \in \Omega^{2}(X)$ depends only on the conformal class $[\bar{g}]$, and hence set $\|\zeta\|_{L_{[\bar{g}]}^{2}}:=\|\zeta\|_{L_{\bar{g}}^{2}}$. Then, Fact 3.2 combined with the argument given in [14, Corollary 4] implies the following assertion.

Proposition 3.5 Let $\bar{g}$ be a cylindrical metric on $X$, and $\omega \in \Omega_{\mathrm{c}}^{2}(X)$ as above. Then one of the following (1)-(3) holds:
\begin{itemize}
\item[(1)] There exists a metric $\check{g} \in[\bar{g}]_{L_{\tilde{g}}^{1,2}}$ such that $R_{\check{g}}>|\omega|_{\check{g}}$ on $X$,
\item[(2)] $Y_{\bar{C}}^{c y \ell}(X)<\|\omega\|_{L_{\bar{C}}^{2}}^{2}$,
\item[(3)] $Y_{\bar{C}}^{c y \ell}(X)=\|\omega\|_{L_{\bar{C}}^{2}}=0$, and there exists a metric $\check{g} \in[\bar{g}]_{L_{\bar{g}}^{1,2}}$ such that $R_{\breve{g}} \equiv 0$ on $X$.
\end{itemize}
3.2. $L^{2}$-harmonic 2-forms. Let $(X, \bar{g})$ be a cylindrical 4-manifold modeled by $(Z, h)$. A 2-form $\zeta \in \Omega^{2}(X)$ is an $L_{\bar{g}}^{2}$-harmonic 2-form on $X$, i.e., $\zeta$ satisfies
$$\left\{\begin{array}{l}
d \zeta=d^{*} \zeta=0 \\
\|\zeta\|_{L_{\bar{g}}^{2}}^{2}:=\int_{X}|\zeta|_{\bar{g}}^{2} d \sigma_{\bar{g}}<\infty
\end{array}\right.$$
Here $d^{*}$ stands for the codifferential with respect to the metric $\bar{g}$. We consider the space of $L_{\bar{g}}^{2}$-harmonic 2-forms
$$\mathcal{H}_{\bar{g}}^{2}(X):=\left\{\zeta \in \Omega^{2}(X) \mid \zeta \text { is } L_{\bar{g}}^{2} \text {-harmonic }\right\} .$$
We recall the following well-known facts.
Fact 3.3 (cf. [10]) Let $\zeta \in \mathcal{H}_{\bar{g}}^{2}(X)$ be an $L_{\bar{g}}^{2}$-harmonic 2-form. Then the function $|\zeta|_{\bar{g}}$ decays exponentially on $Z \times[0, \infty)$.

Fact 3.4
\begin{itemize}
\item[(1)] (Atiyah-Patodi-Singer [5]) There is an isomorphism:
$$\mathcal{H}_{\bar{g}}^{2}(X) \cong \operatorname{Im}\left[H_{c}^{2}(X ; \mathbf{R}) \rightarrow H^{2}(X ; \mathbf{R})\right],$$
where $H_{c}^{2}(X ; \mathbf{R})$ denotes the second cohomology with compact support.
\item[(2)] (Dodziuk [9]) For any $L_{\bar{g}}^{2}$-harmonic 2-form $\zeta \in \mathcal{H}_{\bar{g}}^{2}(X)$, there exists a sequence of closed 2-forms $\left\{\zeta_{j}\right\} \subset \Omega_{c}^{2}(X)$ such that
$$\left\{\begin{array}{l}
{\left[\zeta_{j}\right]=[\zeta] \in H^{2}(X ; \mathbf{R}),} \\
\zeta_{j} \rightarrow \zeta \text { in the } L_{\bar{g}}^{k, 2} \text {-topology on } X \text { for all } k \geq 0 \text { as } j \rightarrow \infty .
\end{array}\right.$$
\end{itemize}

Recall that the Sobolev embedding $L_{\bar{g}}^{3,2}(X) \subset C^{0, \alpha}(X)$ holds for all $0 \leq \alpha<1$. This implies that $\sup _{X}\left|\zeta_{j}-\zeta\right|_{\bar{g}} \rightarrow 0$ as $j \rightarrow \infty$. Hence each closed 2-form $\zeta_{j}$ is not harmonic but almost-harmonic for $j \gg 1$ unless $\zeta \equiv 0$.
3.3. $L^{2}$-harmonic spinors. ¿From now on we assume that $(X, \bar{g})$ is an oriented cylindrical 4-manifold. An element $a \in H^{2}(X ; \mathbf{Z})$ is a characteristic element if $a \equiv w_{2}(X) \bmod 2$ (where $w_{2}(X) \in H^{2}\left(X ; \mathbf{Z}_{2}\right)$ is the second Stiefel-Whitney class). We will identify $a$ with its image in $H^{2}(X ; \mathbf{R})$. Let $P_{Z}: Z \times$ $[1, \infty) \rightarrow Z \times\{1\}$ denote the canonical projection. We choose a characteristic element $a \in H^{2}(X ; \mathbf{Z}) \cap \operatorname{Im}\left[H_{c}^{2}(X ; \mathbf{R}) \rightarrow H^{2}(X ; \mathbf{R})\right]$ which is not a torsion class. Then there exists a Hermitian cylindrical C-line bundle L over $X$ such that
$$\left\{\begin{array}{l}
c_{1}(\mathrm{~L})=a, \\
\left.\mathrm{~L}\right|_{Z \times[1, \infty)}=P_{Z}^{*}\left(\left.\mathrm{~L}\right|_{Z \times\{1\}}\right) .
\end{array}\right.$$
Here $c_{1}(\mathrm{~L})$ is the first Chern class of L.
Let $\mathrm{S}_{\mathrm{C}}^{ \pm}(a):=\mathrm{S}_{\mathrm{C}}^{ \pm} \otimes \mathrm{L}^{1 / 2}$ denote the plus/minus spin bundle associated to L. Here $\mathrm{S}_{\mathrm{C}}^{ \pm}$is the (virtual) plus/minus bundle. Then we have, as a Hermitian vector bundle,
$$\left.\mathrm{S}_{\mathbf{C}}^{ \pm}(a)\right|_{Z \times[1, \infty)}=P_{Z}^{*}\left(\left.\mathrm{~S}_{\mathbf{C}}^{ \pm}(a)\right|_{Z \times\{1\}}\right) .$$
¿From [9] Theorem 2.7], there exists a unique $L_{\bar{g}}^{2}$-harmonic 2-form $\zeta \in \mathcal{H}_{\bar{g}}^{2}(X)$ such that its cohomology class $[\zeta]=a \in H^{2}(X ; \mathbf{R})$. In particular, from Fact 3.4 (2), there exists a sequence of closed 2-forms $\left\{\zeta_{j}\right\} \subset \Omega_{\mathrm{c}}^{2}(X)$ such that
$$\left\{\begin{array}{l}
{\left[\zeta_{j}\right]=a \in H^{2}(X ; \mathbf{R})} \\
\zeta_{j} \rightarrow \zeta \text { in } L_{\bar{g}}^{3,2}(X) \cap C^{0, \alpha}(X) \text { as } j \rightarrow \infty .
\end{array}\right.$$
Let $\mathcal{A}(\mathrm{L})$ denote the space of $U(1)$-connections on L. Then there exists a sequence of $U(1)$-connections $\left\{A_{j}\right\} \subset \mathcal{A}(\mathrm{L})$ with compact support such that
$$\frac{\sqrt{-1}}{2 \pi} F_{A_{j}}:=\frac{\sqrt{-1}}{2 \pi} d A_{j}=\zeta_{j} .$$
We also denote by $\not \partial_{A_{j}}=\not \supset_{A_{j}}^{+}: \Gamma\left(\mathrm{S}_{\mathbf{C}}^{+}(a)\right) \rightarrow \Gamma\left(\mathrm{S}_{\mathbf{C}}^{-}(a)\right)$ the associated (twisted) Dirac operator.

Assumption A1. ¿From now on we assume that, for a fixed cylindrical metric $\bar{g}_{0} \in \mathcal{R i e m}^{c y \ell}(X)$ with $\partial_{\infty} \bar{g}_{0}=h$,
$$L^{2}-\operatorname{ind} \not \partial_{A_{j}}:=\operatorname{dim}_{\mathbf{C}}\left(L^{2}-\operatorname{Ker} \not \partial_{A_{j}}\right)-\operatorname{dim}_{\mathbf{C}}\left(L_{\text {ext }}^{2}-\operatorname{Ker} \not \partial_{A_{j}}^{*}\right)>0 .$$
Here $L^{2}$-ind $\not \varnothing_{A_{j}}$ stands for the $L^{2}$-index of $\not \varnothing_{A_{j}}$ and $L_{\text {ext }}^{2}$-Ker $\not \varnothing_{A_{j}}^{*}$ for the extended $L^{2}$-kernel of the adjoint operator $\mathscr{A}_{A_{j}}^{*}$ (cf. [5, 8]). We emphasize that the above index is independent of $j$ (cf. [8, 25]).

Proposition 3.6 For any $\bar{g} \in \mathcal{R i e m}^{c y \ell}(X)$ with $\partial_{\infty} \bar{g}=h$, let $a \in H^{2}(X ; \mathbf{Z})$ be a non-torsion characteristic element and $\zeta \in \mathcal{H}_{\bar{g}}^{2}(X)$ its $L_{\bar{g}}^{2}$-harmonic representative. Then, under the assumption A1,
$$Y_{[\bar{g}]}^{c y \ell}(X) \leq \min \left\{4 \pi \sqrt{2\left(a^{+}\right)^{2}}, Y_{\left[h+d t^{2}\right]}^{c y \ell}(Z \times \mathbf{R})\right\} .$$
Here $\left(a^{+}\right)^{2}:=\int_{X}\left|\zeta^{+}\right|_{\bar{g}}^{2} d \sigma_{\bar{g}}$, and $\zeta^{+} \in \mathcal{H}_{\bar{g}}^{2,+}(X)$ stands for the self-dual part of $\zeta$ with respect to $\bar{g}$.
Proof. Recall that $Y_{[\bar{g}]}^{c y \ell}(X) \leq Y_{\left[h+d t^{2}\right]}^{c y \ell}(Z \times \mathbf{R})$ (see [3]). Hence it is enough to show that $Y_{[\bar{g}]}^{c y \ell}(X) \leq 4 \pi \sqrt{2\left(a^{+}\right)^{2}}$. Set $\omega:=4 \sqrt{2} \zeta_{j}^{+}$in Proposition 3.5. As we have seen, the form $\omega$ is not closed in general. We postpone the proof of the following assertion to the end of this section.

Proposition 3.7 For any $\bar{g} \in \mathcal{R i e m}^{c y \ell}(X)$ with $\partial_{\infty} \bar{g}=h$, let $a \in H^{2}(X ; \mathbf{Z})$ be a non-torsion characteristic element and $\zeta \in \mathcal{H}_{\bar{g}}^{2}(X)$ its $L_{\bar{g}}^{2}$-harmonic representative. Then, under the assumption A1, the following inequality holds:
$$Y_{[\bar{g}]}^{c y \ell}(X) \leq\left\|4 \sqrt{2} \pi \zeta_{j}^{+}\right\|_{L_{\bar{g}}^{2}}=4 \pi\left(2 \int_{X}\left|\zeta_{j}^{+}\right|_{\bar{g}}^{2} d \sigma_{\bar{g}}\right)^{\frac{1}{2}} \quad \text { for any } j .$$
By taking $j \rightarrow \infty$ in (3.1), Proposition 3.7 implies that
$$Y_{[\bar{g}]}^{c y \ell}(X) \leq 4 \pi\left(2 \int_{X}\left|\zeta^{+}\right| \frac{2}{\bar{g}} d \sigma_{\bar{g}}\right)^{\frac{1}{2}}=4 \pi \sqrt{2\left(a^{+}\right)^{2}}$$
This completes the proof of Proposition 3.6 \(\square\)

Assumption A2. We assume that $b_{2}^{-}(X)=0$. This implies that $\mathcal{H}_{\bar{g}}^{2,+}(X)=$ $\mathcal{H}_{\bar{g}}^{2}(X)$ for any $\bar{g} \in \mathcal{R i e m}^{c y \ell}(X)$.

Theorem 3.8 Let $(X, \bar{g})$ be a cylindrical 4-manifold modeled by $(Z, h)$. Then, under the assumptions A1 and A2,
$$Y^{h-c y \ell}(X) \leq \min \left\{4 \pi \sqrt{2 a^{2}}, Y_{\left[h+d t^{2}\right]}^{c y \ell}(Z \times \mathbf{R})\right\} .$$
Proof. Let $\bar{g} \in \mathcal{R i e m}^{\text {cyl }}(X)$ be any cylindrical metric with $\partial_{\infty} \bar{g}=h$. For the 2-forms $\zeta, \zeta_{j}$ and the $U(1)$-connections $A_{j}$ as above, Fact 3.5 and Assumption A1 imply that $L^{2}$-ind $\not \partial_{A_{j}, \bar{g}}>0$ for any $j$. Then, Proposition 3.6 and Assumption A2 give the inequality $Y_{[\bar{g}]}^{c y \ell}(X) \leq 4 \pi \sqrt{2\left(a^{+}\right)^{2}}=4 \pi \sqrt{2 a^{2}}$. Therefore, $Y^{h-c y \ell}(X) \leq 4 \pi \sqrt{2 a^{2}}$. \(\square\)

Now we consider the following subspace of $\mathcal{R}$ iem $(Z)$
$$\operatorname{Riem}^{*}(Z):=\left\{h \in \mathcal{R i e m}(Z) \mid \lambda\left(\mathcal{L}_{h}\right)>0\right\}\left(\subset \mathcal{R} \operatorname{iem}^{+}(Z)\right) .$$

Fact 3.5 (cf. [8, 25]) Let $A \in \mathcal{A}(\mathrm{~L})$ be a $U(1)$-connection with compact support $\operatorname{Supp}(A) \subset X$. Let $h \simeq h^{\prime}$ be two metrics homotopic in $\operatorname{Riem}^{*}(Z)$. For any two cylindrical metrics $\bar{g}, \bar{g}^{\prime} \in \mathcal{R i e m}^{\text {cyl }}(X)$ with $\partial_{\infty} \bar{g}=h$ and $\partial_{\infty} \bar{g}^{\prime}=h^{\prime}$, then $L^{2}$-ind $\not \varnothing_{A, \bar{g}}=L^{2}$-ind $\varnothing_{A, \bar{g}^{\prime}}$.

Then, Theorem 3.8 combined with Fact 3.5 implies the following.
Corollary 3.9 Let $h^{\prime} \in \operatorname{Riem}^{*}(Z)$ be a metric homotopic to $h$ in $\operatorname{Riem}^{*}(Z)$. Then
$$Y^{h^{\prime}-c y \ell}(X) \leq \min \left\{4 \pi \sqrt{2 a^{2}}, Y_{\left[h^{\prime}+d t^{2}\right]}^{c y \ell}\left(Z^{3} \times \mathbf{R}\right)\right\} .$$
3.4. Behavior of $L^{2}$-harmonic spinors on the cylindrical ends. Here we modify the Bochner techinque given in [15], [16] and [23] to our case. Let $\bar{g} \in \mathcal{R i e m}^{\text {cyl }}(X)$ be a cylindrical metric with $\partial_{\infty} \bar{g}=h$ and $\check{g}=u^{2} \cdot \bar{g}$ a conformal metric on $X$ with $u \in C_{+}^{\infty}(X) \cap L_{\bar{g}}^{1,2}(X)$. Then the Dirac operators $\not \varnothing_{A, \check{g}}$ and $\not \partial_{A, \bar{g}}$ on $\mathrm{S}_{\mathbf{C}}^{+}(a)$ are related as follows (cf. [23, Proposition 2]):
$$\not \varnothing_{A, \check{g}}(\psi)=u^{-\frac{5}{2}} \cdot \not \varnothing_{A, \bar{g}}\left(u^{\frac{3}{2}} \psi\right) .$$
For any $\psi \in \operatorname{Ker} \not \partial_{A, \bar{g}}$, then we also obtain the harmonic spinor $\check{\psi}:=u^{-\frac{3}{2}} \cdot \psi \in$ $\operatorname{Ker} \mathscr{A}_{A, \check{g}}$. Now let $\psi \in L_{\bar{g}}^{2}$-Ker $\not \varnothing_{A, \bar{g}}$ be a non-zero $L_{\bar{g}}^{2}$-harmonic plus-spinor. Then $\check{\psi}:=u^{-\frac{3}{2}} \cdot \psi \in \operatorname{Ker} \not \partial_{A, \check{g}}$ is a non-zero harmonic spinor with respect to $(A, \check{g})$, and hence the Bochner formula gives that
$$0=\not \varnothing_{A, \check{g}}^{2} \check{\psi}=-\Delta_{A, \check{g}} \check{\psi}+\frac{1}{4} R_{\check{g}} \check{\psi}+\frac{1}{2} F_{A}^{+} \check{\psi} .$$
Here and below " • " and " • " stand for the Clifford multiplication corresponding to the metrics $\bar{g}$ and $\check{g}$, respectively. Then we have on $X(\ell)=$ $X \backslash(Z \times(\ell, \infty))$ (for $\ell>1$ ):
$$\begin{gathered}
0=\int_{X(\ell)}\left[\left\langle-\Delta_{A, \check{g}} \breve{\psi}, \check{\psi}\right\rangle+\frac{1}{4} R_{\check{g}}|\check{\psi}|^{2}+\frac{1}{2}\left\langle F_{A}^{+} \check{\psi}, \check{\psi}\right\rangle\right] d \sigma_{\check{g}} \\
=\int_{X(\ell)}\left[\left|\nabla^{A, \check{g}} \check{\psi}\right|^{2}+\frac{1}{4} R_{\check{g}}|\check{\psi}|^{2}+\frac{1}{2}\left\langle F_{A}^{+} \check{\psi}, \check{\psi}\right\rangle\right] d \sigma_{\check{g}} \\
\quad-\left.\int_{\partial X(\ell)}\left\langle\nabla_{\check{\nu}}^{A, \check{g}} \check{\psi}, \check{\psi}\right\rangle d \sigma_{\check{g}}\right|_{\partial X(\ell)} \\
\geq \int_{X(\ell)}\left[\left|\nabla^{A, \check{g}} \check{\psi}\right|^{2}+\frac{1}{4}\left(R_{\check{g}}-2 \sqrt{2}\left|F_{A}^{+}\right|_{\check{g}}\right)|\check{\psi}|^{2}\right] d \sigma_{\check{g}} \\
\quad-\left.\int_{\partial X(\ell)}\left|\nabla_{\check{\nu}}^{A, \check{g}} \check{\psi}\right| \cdot|\check{\psi}| d \sigma_{\check{g}}\right|_{\partial X(\ell)} .
\end{gathered}$$

Here $\check{\nu}=u^{-1} \frac{\partial}{\partial t}$ is the outer unit normal vector field on $\partial X(\ell)$ with respect to $\check{g}$. Since $\check{g}=u^{2} \cdot \bar{g}$, we have
$$d \sigma_{\check{g}}=u^{4} d \sigma_{\bar{g}}, \quad|\check{\psi}|=u^{-\frac{3}{2}}|\psi| .$$
Then, for certain positive constants $K, K^{\prime}$, we have the estimate:
$$\begin{aligned}
\left|\nabla_{\check{\nu}}^{A, \check{g}} \check{\psi}\right| & =u^{-1}\left|\nabla_{\partial_{t}}^{A, \check{g}}\left(u^{-\frac{3}{2}} \psi\right)\right|=u^{-1}\left|-\frac{3}{2}\left(u^{-\frac{5}{2}} \partial_{t} u\right) \psi+u^{-\frac{3}{2}} \nabla_{\partial_{t}}^{A, \check{g}} \psi\right| \\
& =u^{-\frac{5}{2}}\left|-\frac{3}{2}\left(u^{-1} \partial_{t} u\right) \psi+\nabla_{\partial_{t}}^{A, \bar{g}} \psi-\frac{1}{4} \sum_{j=1}^{4} e_{j}(u)\left[\left(\frac{\partial}{\partial t}\right) \cdot, e_{j} \bullet\right] \psi\right| \\
& \leq K \cdot u^{-\frac{5}{2}}\left(u^{-1}\left|\partial_{t} u\right| \cdot|\psi|+\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right|+u^{-1}|d u|_{\bar{g}} \cdot|\psi|\right) \\
& \leq K^{\prime} \cdot u^{-\frac{5}{2}}\left(u^{-1}|d u|_{\bar{g}} \cdot|\psi|+\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right|\right),
\end{aligned}$$
where $\left\{e_{1}=\frac{\partial}{\partial t}, e_{2}, e_{3}, e_{4}\right\}$ is a local orthonormal frame on $\partial X(\ell)$ with respect to $\bar{g}$. We use (3.3) to obtain that
$$\begin{aligned}
& \left.\int_{\partial X(\ell)}\left|\nabla_{\check{\nu}}^{A, \check{g}} \check{\psi}\right| \cdot|\check{\psi}| d \sigma_{\check{g}}\right|_{\partial X(\ell)} \\
& \quad \leq\left. K \int_{\partial X(\ell)} u^{-\frac{5}{2}}\left(u^{-1}|d u|_{\bar{g}} \cdot|\psi|+\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right|\right) u^{-\frac{3}{2}}|\psi| u^{4} d \sigma_{\bar{g}}\right|_{\partial X(\ell)} \\
& \quad \leq\left. K \int_{\partial X(\ell)}\left(u^{-1}|d u|_{\bar{g}} \cdot|\psi|^{2}+\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right| \cdot|\psi|\right) d \sigma_{\bar{g}}\right|_{\partial X(\ell)}
\end{aligned}$$

Lemma 3.10 Let $u \in C_{+}^{\infty}(X) \cap L_{\bar{g}}^{1,2}(X)$ be a function satisfying $\mathbb{L}_{(\bar{g}, \omega)} u=$ $\lambda_{(\bar{g}, \omega)} u$ on $Z \times\left[\ell_{0}, \infty\right)$ for a fixed $\ell_{0} \geq 1$. Then
$$B_{\ell}:=\left.\int_{\partial X(\ell)}\left(u^{-1}|d u|_{\bar{g}} \cdot|\psi|^{2}+\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right| \cdot|\psi|\right) d \sigma_{\bar{g}}\right|_{\partial X(\ell)} \rightarrow 0 \quad \text { as } \ell \rightarrow \infty .$$
Proof of Proposition 3.7 Set $\omega:=4 \sqrt{2} \pi \zeta_{j}^{+}=\sqrt{-1} \cdot 2 \sqrt{2} F_{A_{j}}^{+}$and let $u$ be the same function as in Lemma 3.4. Suppose that the $C^{2, \alpha}$-metric $\check{g}=u^{2} \cdot \bar{g}$ satisfies that $R_{\check{g}}>|\omega|_{\check{g}}$. Perturbing $u$ on a compact set, we may assume that $u$ is smooth and that $R_{\check{g}}>|\omega|_{\check{g}}$. Then, the inequality (3.2) combined with the estimate (3.4) and Lemma 3.10 implies that
$$0 \geq \int_{X}\left[\left|\nabla^{A_{j}, \check{g}} \check{\psi}\right|^{2}+\frac{1}{4}\left(R_{\check{g}}-2 \sqrt{2}\left|F_{A_{j}}^{+}\right| \check{g}\right)|\check{\psi}|^{2}\right] d \sigma_{\check{g}} .$$
Hence the condition $R_{\check{g}}>|\omega|_{\check{g}}=2 \sqrt{2}\left|F_{A_{j}}^{+}\right|_{\check{g}}$ contradicts the inequality (3.5). Finally, from Proposition 3.5 $Y_{[\bar{g}]}^{c y \ell}(X) \leq\left\|2 \sqrt{2} F_{A_{j}}^{+}\right\|_{L_{\bar{g}}^{2}}=\left\|4 \sqrt{2} \pi \zeta_{j}^{+}\right\|_{L_{\bar{g}}^{2}}$. \(\square\)

Now we have to prove Lemma 3.10 There are two independent tasks here to deal with, i.e., the decay of the function $u$ and the pointwise norms $|\psi|$, $\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right|$. The spinor norms are taken care by the following result.

Fact 3.6 (5) Let $\psi$ be an $L_{\bar{g}}^{2}$-harmonic spinor as above. Then the pointwise norms $|\psi|,\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right|$ decay exponentially on the cylinder $Z \times[1, \infty)$.

To complete the proof of Lemma 3.10 we need the following technical result.
Lemma 3.11 There exists a positive constant $K$ such that $u^{-1}|d u|_{\bar{g}} \leq K$ on the cylinder $Z \times[1, \infty)$.

Proof of Lemma 3.10. By Fact 3.6 and Lemma 3.11 there exist positive constants $K_{1}, K_{2}, K$ and $\kappa$ such that
$$B_{\ell} \leq K_{1} \cdot \operatorname{Vol}_{h}(Z)\left(K_{2} \cdot|\psi|^{2}+\left|\nabla_{\partial_{t}}^{A, \bar{g}} \psi\right| \cdot|\psi|\right) \leq K \cdot e^{-\kappa \ell} \rightarrow 0$$
as $\ell \rightarrow \infty$. \(\square\)

Proof of Lemma 3.11. Recall that the support $\operatorname{Supp}(\omega)(\subset X)$ is compact. Hence there exists $\ell_{1}\left(\geq \ell_{0}\right)$ such that the restriction of $\omega$ is zero on the cylinder $Z \times\left[\ell_{1}-1, \infty\right)$. In particular, the operator $\mathbb{L}_{(\bar{g}, \omega)}=\mathbb{L}_{\bar{g}}$ on $Z \times\left[\ell_{1}-1, \infty\right)$. Recall that $\lambda_{h}$ and $\lambda_{(\bar{g}, \omega)}$ denote respectively the first eigenvalue of the operator $\mathcal{L}_{h}$ and the bottom of the spectrum of $\mathbb{L}_{(\bar{g}, \omega)}$. Then, we consider the following operator $L_{h}$ on $Z$
$$L_{h}:=-6 \Delta_{h}+\left(R_{h}-\lambda_{(\bar{g}, \omega)}\right)=\mathcal{L}_{h}-\lambda_{(\bar{g}, \omega)} .$$
Let $\left\{\left(\mu_{j}, \varphi_{j}\right)\right\}$ be the eigenvalues and eigenfunctions of $L_{h}$, i.e.,
$$L_{h} \varphi_{j}=\mu_{j} \varphi_{j} \quad \text { with } \quad \int_{Z} \varphi_{j} \cdot \varphi_{k} d \sigma_{h}=\delta_{j k} \quad \text { for } \quad j, k=1,2, \ldots,$$
and $\mu_{1}<\mu_{2} \leq \mu_{3} \leq \cdots$. Here we may assume that $\varphi_{1}>0$ on $Z$. Since $\lambda_{h}>\lambda_{(\bar{g}, \omega)}$, we obtain that $\mu_{1}>0$.

Let $(z, t) \in Z \times\left[\ell_{1}, \infty\right)$ be a product coordinate system associated to $\bar{g}$. Note that $\mathbb{L}_{(\bar{g}, \omega)}=-6 \cdot \partial_{t}^{2}+\mathcal{L}_{h}$ on $Z \times\left[\ell_{1}, \infty\right)$. Then on the cylinder $Z \times\left[\ell_{1}, \infty\right)$,
$$\begin{gathered}
\left(\mathbb{L}_{(\bar{g}, \omega)}-\lambda_{(\bar{g}, \omega)}\right)\left(e^{-\sqrt{\mu_{j} / 6} \cdot t} \varphi_{j}(z)\right)=L_{h}\left(e^{-\sqrt{\mu_{j} / 6} \cdot t} \varphi_{j}(z)\right)-6 \cdot \partial_{t}^{2}\left(e^{-\sqrt{\mu_{j} / 6} \cdot} \varphi_{j}(z)\right) \\
=\mu_{j} \cdot\left(e^{-\sqrt{\mu_{j} / 6} \cdot t} \varphi_{j}(z)\right)-\mu_{j} \cdot\left(e^{-\sqrt{\mu_{j} / 6} \cdot t} \varphi_{j}(z)\right)=0 .
\end{gathered}$$
Hence $\mathbb{L}_{(\bar{g}, \omega)}\left(e^{-\sqrt{\mu_{j} / 6} \cdot t} \varphi_{j}(z)\right)=\lambda_{(\bar{g}, \omega)} \cdot e^{-\sqrt{\mu_{j} / 6} \cdot t} \varphi_{j}(z)$ on $Z \times\left[\ell_{1}, \infty\right)$. Then the function $u \in C_{+}^{\infty}(X) \cap L_{\bar{g}}^{1,2}(X)$ restricted on $Z \times\left[\ell_{1}, \infty\right)$ can be represented as
$$\left\{\begin{array}{l}
u(z, t)=\sum_{j \geq 1} a_{j} \cdot e^{-\sqrt{\mu_{j} / 6} \cdot t} \varphi_{j}(z), \\
\sum_{j \geq 1} a_{j}^{2}<\infty .
\end{array}\right.$$

We set $\mu:=\mu_{j_{0}}=\min \left\{\mu_{j} \mid a_{j} \neq 0\right\}$ and $v_{j}:=\sqrt{\mu_{j} / 6}-\sqrt{\mu / 6}>0$ for $\mu_{j}>\mu$. Let $k+1(\geq 1)$ be the multiplicity of the $j_{0}$-th eigenvalue. Then
$$u(z, t)=e^{-\sqrt{\mu / 6} \cdot t}\left(a_{j_{0}} \varphi_{j_{0}}(z)+\cdots+a_{j_{0}+k} \varphi_{j_{0}+k}(z)+\sum_{\mu_{j}>\mu} a_{j} \cdot e^{-v_{j} \cdot t} \varphi_{j}(z)\right) .$$
It then follows that there exists a positive constant $K$ such that
$$\left|\partial_{t} u\right| \leq K \cdot e^{-\sqrt{\mu / 6} \cdot t}, \quad\left|\nabla^{Z} u\right|_{h} \leq K \cdot e^{-\sqrt{\mu / 6} \cdot t} .$$
This implies the estimate
$$|d u|_{\bar{g}} \leq \bar{K} \cdot e^{-\sqrt{\mu / 6} \cdot t}$$
for a constant $\bar{K}>0$. Now we set $v(z):=a_{j_{0}} \varphi_{j_{0}}(z)+\cdots+a_{j_{0}+k} \varphi_{j_{0}+k}(z)$. Here we need the following fact.

Claim 3.12 With the above understood, then
$$\left\{\begin{array}{l}
\mu=\mu_{1} \text { is the first eigenvalue of } L_{h}, \\
v(z)=a_{1} \varphi_{1}(z)>0 \text { on } Z .
\end{array}\right.$$
Proof. Note that if there exists $z_{0} \in Z$ such that $v\left(z_{0}\right)<0$, then $u\left(z_{0}, t\right)<0$ for sufficiently large $t \gg \ell_{1}$. This contradicts the positivity of $u$ everywhere on $X$. Hence $v(z) \geq 0$ and $v(z) \not \equiv 0$ on $Z$. Now suppose that $\mu$ is not the first eigenvalue. Note that the function $v(z)$ itself is an eigenfunction corresponding to $\mu$. The condition $\mu \neq \mu_{1}$ implies that $\int_{Z} \varphi_{1}(z) \cdot v(z) d \sigma_{h}=0$, which contradicts that $\varphi_{1}(z)>0, v(z) \geq 0$ and $v(z) \not \equiv 0$ on $Z$. Therefore, $\mu=\mu_{1}$. \(\square\)

Note that Claim 3.12 implies the estimate
$$0<\tilde{K}^{-1} \cdot e^{-\sqrt{\mu / 6} \cdot t} \leq u(z, t) \leq \tilde{K} \cdot e^{-\sqrt{\mu / 6} \cdot t}$$
on $Z \times\left[\ell_{1}, \infty\right)$ for a constant $\tilde{K}>0$. Then the estimates (3.6) and (3.7) imply that $u^{-1}|d u|_{\bar{g}} \leq K$ on $X$ for a constant $K>0$. This completes the proof of Lemma 3.11 \(\square\)

\section*{4 Examples}

Let $\mathbf{C P}^{2}$ denote the complex projective plane. In [22] (cf. [14]), LeBrun proved that $Y\left(\mathbf{C P}^{2}\right)=12 \sqrt{2} \pi\left(<8 \sqrt{6} \pi=Y\left(S^{4}\right)\right)$, and that $Y\left(\mathbf{C P}^{2}\right)$ is achieved by a conformal class $C$ if and only if $C$ coincides with the pullback $\Phi^{*}\left[g_{F S}\right]$ of the conformal class $\left[g_{F S}\right]$ by a diffeomorphism $\Phi$. Here $g_{F S}$ denotes the Fubini-Study metric on $\mathbf{C P}^{2}$. In this section, we give some estimates of $Y^{h-c y \ell}(X)$ for particular cylindrical 4-manifolds $X$, which are generalizations of part of the above result.
4.1. Example 1. Let denote by $\mathrm{L} \rightarrow \mathbf{C P}^{1}$ the anti-canonical C-line bundle over the complex projective line $\mathbf{C P}^{1}$ and by $\mathrm{L}_{\ell}:=\mathrm{L}^{\otimes \ell} \rightarrow \mathbf{C P}^{1}$ the C-line bundle of degree $\ell \geq 1$. Then we choose a Hermitian metric $H$ on the bundle $\mathrm{L}_{\ell}$, and consider the disk and the circle bundles of $\mathrm{L}_{\ell}$ :
$$\begin{aligned}
D_{\ell} & :=D\left(\mathrm{~L}_{\ell}\right)=\left\{v \in \mathrm{~L}_{\ell} \mid H(v, v) \leq 1\right\}, \\
Z_{\ell} & :=S\left(\mathrm{~L}_{\ell}\right)=\partial D\left(\mathrm{~L}_{\ell}\right) \cong S^{3} / \Gamma_{\ell}=L(\ell, 1) .
\end{aligned}$$
Here $\Gamma_{\ell}=\mathbf{Z} / \ell \mathbf{Z} \subset\{\xi \in \mathbf{C}| | \xi \mid=1\}$ with the generator $\xi_{\ell}=e^{\frac{2 \pi \sqrt{-1}}{\ell}}$ and the group $\Gamma_{\ell}$ acts on the sphere $S^{3}=S^{3}(1) \subset \mathbf{C}^{2}$ by $\left(w^{1}, w^{2}\right) \mapsto\left(\xi_{\ell} \cdot w^{1}, \xi_{\ell} \cdot w^{2}\right)$. We also denote by $X_{\ell}$ the total space of $\mathrm{L}_{\ell}$. We consider $X_{\ell}$ as an open 4-manifold with a tame end:
$$X_{\ell} \cong D_{\ell} \cup_{Z_{\ell}}\left(Z_{\ell} \times[0, \infty)\right) .$$
First we note some necessary facts.
Fact 4.1
\begin{itemize}
\item[(1)] When $\ell=1$, then $X_{1}$ is diffeomorphic to $\mathbf{C P}^{2} \backslash\{q\}$, and hence $X_{1}$ is an open 4-manifold with tame end $S^{3} \times[0, \infty)$, where $q$ is a point in $\mathbf{C P}^{2}$. When $\ell \geq 2$, then the one-point compactification $M_{\ell}:=X_{\ell} \cup\left\{\check{p}_{\infty}\right\}$ has a natural orbifold structure with $\Sigma_{\Gamma}=\left\{\left(\check{p}_{\infty}, \Gamma_{\ell}\right)\right\}$.
\item[(2)] (cf. [25, Example 4.1.27]) There exists a cylindrical metric $\bar{g}_{0} \in$ Riem ${ }^{c y \ell}\left(X_{\ell}\right)$ with $\partial_{\infty} \bar{g}_{0}=h_{\Gamma_{\ell}} \in \mathcal{R} ن \mathrm{iem}\left(Z_{\ell}\right)$ such that $R_{\bar{g}_{0}}>0$ on $X_{\ell}$.
\item[(3)] $H^{2}\left(X_{\ell} ; \mathbf{Z}\right) \cap \operatorname{Im}\left[H_{c}^{2}\left(X_{\ell} ; \mathbf{R}\right) \rightarrow H^{2}\left(X_{\ell} ; \mathbf{R}\right)\right] \cong \mathbf{Z}$, and $b_{2}^{-}\left(X_{\ell}\right)=0$ for an appropriate orientation of $X_{\ell}$.
\end{itemize}
¿From 3, Lemma 2.14], we note that $Y^{h_{S}-c y l}\left(X_{1}\right)=Y\left(\mathbf{C P}^{2}\right)$, where $h_{S}=$ $h_{\Gamma_{1}} \in \mathcal{R} i e m\left(S^{3}\right)$ denotes the standard metric of constant curvature one. With these understood, we prove the following more general result.

Theorem 4.1
\begin{itemize}
\item[(1)]
$$0<Y^{h-c y \ell}\left(X_{\ell}\right) \leq \min \left\{4(\ell+2) \sqrt{\frac{2}{\ell}} \pi, Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(Z_{\ell} \times \mathbf{R}\right)\right\}$$
for $\ell \geq 1$ and any metric $h \in \mathcal{R i e m}^{*}\left(Z_{\ell}\right)$ homotopic to $h_{\Gamma_{\ell}}$ in $\mathcal{R i e m}^{*}\left(Z_{\ell}\right)$.
\item[(2)] For any metric $h \in \mathcal{R} \operatorname{iem}\left(Z_{\ell}\right)$ which is sufficiently $C^{2}$-close to $h_{\Gamma_{\ell}}$,
$$0<Y^{h-c y \ell}\left(X_{\ell}\right) \leq \begin{cases}12 \sqrt{2} \pi=Y\left(\mathbf{C P}^{2}\right) & \text { if } \ell=1, \\ Y_{\left[h+d t^{2}\right]}^{c y \ell}\left(Z_{\ell} \times \mathbf{R}\right) & \text { if } \ell \geq 2 .\end{cases}$$
In particular, $0<Y^{\text {orb }}\left(M_{\ell}\right)=Y^{h_{\Gamma_{\ell}}-c y \ell}\left(X_{\ell}\right) \leq 8 \sqrt{\frac{6}{\ell}} \pi$ for $\ell \geq 2$.
\end{itemize}

Remark 4.1 We note the following:
\begin{itemize}
\item[(1)] The inequality $4(\ell+2) \sqrt{\frac{2}{\ell}} \pi<8 \sqrt{6} \pi\left(=Y\left(S^{4}\right)\right)$ holds only if $1 \leq \ell \leq 7$.
\item[(2)] Let $M$ be a closed 4-manifold. For any $\ell \geq 2$ and a positive integer $k$, then $Y^{\text {orb }}\left(M \# k M_{\ell}\right) \leq 8 \sqrt{\frac{6}{\ell}} \pi$.
\item[(3)] If we replace $X_{1}=\mathbf{C P}^{2} \backslash\{q\}$ by $\mathbf{C P}^{2} \backslash\left\{q_{1}, \ldots, q_{s}\right\}$, a similar result still holds for $\mathbf{C P}^{2} \backslash\left\{q_{1}, \ldots, q_{s}\right\}$.
\item[(4)] Unfortunately, the estimate $Y^{h-c y \ell}(X) \leq 4 \pi \sqrt{2 a^{2}}$ in Theorem 3.8 is not effective for $X=X_{\ell}(\ell \geq 2)$ and $h=h_{\Gamma_{\ell}}$ since $4(\ell+2) \sqrt{\frac{2}{\ell}} \pi>8 \sqrt{\frac{6}{\ell}} \pi$ for $\ell \geq 2$.
\end{itemize}