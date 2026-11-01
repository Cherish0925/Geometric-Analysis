---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1808_06370.pdf
converter: mathpix
format: mmd
---

\title{
STABILITY OF QUADRATIC CURVATURE FUNCTIONALS AT PRODUCT OF EINSTEIN MANIFOLDS
}

\author{
ATREYEE BHATTACHARYA AND SOMA MAITY
}

\begin{abstract}
Consider Riemannian functionals defined by $L^{2}$-norms of Ricci curvature, scalar curvature, Weyl curvature and Riemannian curvature. Rigidity, stability and local minimizing properties of Eistein metrics as critical metrics of these quadratic functionals have been studied in [8]. In this paper, we study the same for products of Einstein metrics with Einstein constants of possibly opposite signs. In particular, we prove that the product of a spherical space form and a compact hyperbolic manifold is unstable for certain quadratic functionals if the first eigenvalue of the Laplacian of the hyperbolic manifold is sufficiently small. We also prove the stability of $L^{\frac{n}{2}}$-norm of Weyl curvature at compact quotients of $S^{n} \times \mathbb{H}^{m}$.
\end{abstract}

\section*{1. Introduction}

Let $M^{n}$ be a closed smooth manifold of dimension $n \geq 3$. We consider quadratic Riemannian functionals $\mathcal{R}, \mathcal{R} i c, \mathcal{S}$ and $\mathcal{W}_{2}$ defined on the space of Riemannian metrics on $M$ by
$$\mathcal{R}(g)=\int_{M}\left|R_{g}\right|^{2} d v_{g}, \quad \mathcal{R} i c(g)=\int_{M}\left|r_{g}\right|^{2} d v_{g}, \quad \mathcal{S}(g)=\int_{M} s_{g}^{2} d v_{g}, \quad \mathcal{W}_{2}(g)=\int_{M}|W|^{2} d v_{g}$$
where $R_{g}, r_{g}, s_{g}$ and $W$ denote the Riemannian curvature, Ricci curvature , scalar curvature and Weyl curvature of the Riemannian manifold $(M, g)$ respectively. If $(M, g)$ is not the standard sphere, the space of symmetric two tensors $S^{2} M$ on $M$ admits the following orthogonal decomposition (see Lemma (4.57) in [1]).
$$S^{2} M=I m \delta_{g}^{*} \oplus C^{\infty} M g \oplus\left(\delta_{g}^{-1}(0) \cap t r^{-1}(0)\right)$$
As the Riemannian functionals above are invariant under the action of the diffeomorphism group of $M$ on the space of Riemannian metrics, gradients of these functionals have no component along $I m \delta_{g}^{*}$. Also, since these functionals are not scale invariant, we restrict them to the space of Riemannian metrics with constant volume.

Definition 1. Let $(M, g)$ be a closed Riemannian manifold which is not the standard sphere. If $g$ is a critical metric of a Riemannian functional $\mathcal{F}$ then $g$ is called stable for $\mathcal{F}$ if there exists a constant $C>0$ such that
$$H_{F}(h, h) \geq C\|h\|^{2} \text { for all } h \in\left\{f g: f \in C^{\infty} M \text { and } \int_{M} f d v_{g}=0\right\} \oplus \delta_{g}^{-1}(0) \cap t r^{-1}(0)$$
where $H_{F}$ denotes the Hessian of $\mathcal{F}$ at $g$.
Riemannian functionals and their critical points have been topics of interest both in Riemannian geometry and physics. A complete classification of irreducible symmetric spaces of compact type as stable critical points of the total scalar curvature functional is available due to N. Koiso (see [10], [11], [12]). Besson, Courtois and Gallois proved that compact quotients of rank one symmetric spaces of non-compact type are global minima for the $L^{\frac{n}{2}}$-norm of scalar curvature ([2]). In [8] Gursky and Viaclovsky studied rigidity, stability and local minimizing properties of Einstein metrics for the quadratic Riemannian functional $\mathcal{F}_{t}$ defined by
$$\mathcal{F}_{t}(g)=\operatorname{Ric}(g)+t \mathcal{S}(g), \quad \text { for } \quad t \in \mathbb{R} .$$
In this paper, we focus on understanding stability of products of closed Einstein manifolds of the curvature functionals $\mathcal{R}, \mathcal{R} i c, \mathcal{F}_{t}$ and $\mathcal{W}_{2}$.

\footnotetext{
2010 Mathematics Subject Classification. Primary 53C21, 58E11.
Key words and phrases. Riemannian functionals, critical metrics, stability, local minima.
}

Let $(M, g)$ be the product of closed Einstein manifolds $\left(M_{0}, g_{0}\right)$ and $\left(M_{1}, g_{1}\right)$ with respective Einstein constants $\lambda_{0}$ and $\lambda_{1}$. Then $(M, g)$ is a critical metric of $\mathcal{R} i c$ if and only if $\left|\lambda_{0}\right|=\left|\lambda_{1}\right|$. This condition can always be achieved after suitable rescaling of $g_{1}$ or $g_{2}$, provided both $\lambda_{1}, \lambda_{2} \neq 0$. Let $\mathcal{M}_{W}$ denote the space of doubly warped product metrics on $M$ with constant volume. The warped product variations play an important role in determining the stability of $\mathcal{R} i c$ at products of Einstein metrics. The tangent space of $\mathcal{M}_{W}$ at $g$ is given by $\left(C^{\infty} M_{0} . g_{1}+C^{\infty} M_{1} . g_{0}\right)$. If $g$ is a critical metric of $\mathcal{R} i c$ and $H_{\text {Ric }}$ restricted to $\left(C^{\infty} M_{0} . g_{1}+C^{\infty} M_{1} . g_{0}\right)$ satisfies (1.2), then we say that $g$ is stable for $\mathcal{R} i c$ restricted to $\mathcal{M}_{W}$.

Theorem 1. Let $(M, g)$ be the product of two closed Einstein manifolds $\left(M_{0}, g_{0}\right)$ and $\left(M_{1}, g_{1}\right)$ with respective dimensions $n_{0}, n_{1} \geq 3$, Einstein constants $\lambda_{0}, \lambda_{1}$ and first eigenvalues of the Laplacian $\mu_{0}$, $\mu_{1} \cdot(M, g)$ is stable for $\mathcal{R}$ ic restricted to $\mathcal{M}_{W}$ if and only if one of the following conditions is satisfied.
(i) $\lambda_{0}=\lambda_{1}>0$.
(ii) $\lambda_{0}=\lambda_{1}<0$ and for each $j \in\{0,1\}$ either $n_{j}=3,4$ or $\frac{\mu_{j}}{\left|\lambda_{j}\right|}>c\left(n_{[j+1]}\right)$ where $c(a)=\frac{a-6+\sqrt{9 a^{2}-36 a+4}}{2(a+1)}$ and $[j]=j \bmod 2$.
(ii) $\lambda_{0}=-\lambda_{1}>0$ and either $n_{0}=3$, or $\frac{\mu_{1}}{\left|\lambda_{1}\right|}>\frac{\left(n_{0}+2\right)+\sqrt{9 n_{0}^{2}-20 n_{0}-28}}{2\left(n_{0}+1\right)}$.

If $\left(M_{0}, g_{0}\right)$ and $\left(M_{1}, g_{1}\right)$ are stable for $\mathcal{R} i c$, then we prove that $H_{\text {Ric }}$ restricted to TT-tensors on $M$ satisfies the condition for stability stated in (1.2). Consequently, we have the following theorem.

Theorem 2. Let $(M, g)$ be the product of two closed Einstein manifolds $\left(M_{0}, g_{0}\right)$ and $\left(M_{1}, g_{1}\right)$ with respective dimensions $n_{0}, n_{1} \geq 3$. If $\left(M_{0}, g_{0}\right)$ and $\left(M_{1}, g_{1}\right)$ are stable for $\mathcal{R}$ ic then $(M, g)$ is stable if and only if $(M, g)$ is stable for $\mathcal{R}$ ic restricted to $\mathcal{M}_{W}$.

For instance, the sphere $\left(S^{n}\right)$, complex projective space $\left(\mathbb{C} P^{n}\right)$ and $S^{n} \times S^{n}$ with standard Riemannian metrics are stable for $\mathcal{R} i c$ [8]. As a consequence of the above theorem $S^{n} \times \mathbb{C} P^{m}$, product of finitly many $S^{n}$ and $\mathbb{C} P^{m}$ possibly with different dimensions are stable for $\mathcal{R} i c$. A compact hyperbolic manifold $H^{n}$ is stable for $\mathcal{R} i c$ if, the first eigenvalue of the laplacian $\mu>\frac{2(n-4)(n-1)}{n}$ (see Remark 7.4, [8]).

Theorem 3. Let $(M, g)$ be the product of $S^{n}$ and a compact hyperbolic manifold $H^{m}$, then $(M, g)$ is stable for $\mathcal{R}$ ic if and only if either $m=3$ or the first eigenvalue of the Laplacian $\mu$ of $H^{m}$ satisfies
$$\frac{\mu}{m-1}>\max \left\{\frac{2(m-4)}{m}, \frac{(n+2)+\sqrt{9 n^{2}-20 n-28}}{2(n+1)}\right\}$$

In particular, if $\mu>2(m-1)$, then $S^{n} \times H^{m}$ is always stable for $\mathcal{R} i c$. A compact hyperbolic manifold with dimension 4 is always stable for $\mathcal{R} i c$ (Remark 7.4, [8]). The above theorem implies that if $\mu<6$ and $n$ sufficiently large then $S^{n} \times H^{4}$ is not stable for $\mathcal{R} i c$. More generally, if $M=S^{n} \times H^{m}$ and
$$\frac{2(m-4)}{m}<\frac{\mu}{m-1}<\frac{(n+2)+\sqrt{9 n^{2}-20 n-28}}{2(n+1)}$$
then $S^{n}$ and $H^{m}$ both are individually stable for $\mathcal{R} i c$ but the product $S^{n} \times H^{m}$ is not stable for $\mathcal{R} i c$. Similar results also hold for products of $\mathbb{C} P^{n}$ and compact quotients of its non-compact dual.

We also prove similar stability criteria for critical metrics of $\mathcal{F}_{t}$ those are products of Einstein metrics with Einstein constants of opposite signs (see Theorem 6 for details) thereby generalizing the work of Gursky and Viaclovsky [8]. Due to Chern-Gauss-Bonnet theorem $\mathcal{W}_{2}$ is equivalent to $\mathcal{F}_{-\frac{1}{3}}$ in dimension 4. Hence rigidity or stability of $\mathcal{F}_{-\frac{1}{3}}$ implies rigidity or stability of Bach flat metrics in this case [8]. Since $\mathcal{W}_{2}$ is not conformally invariant for $n>4$ we consider the conformally invariant Riemannian functional $\mathcal{W}_{\frac{n}{2}}$ defined by
$$\mathcal{W}_{\frac{n}{2}}(g)=\int_{M}\left|W_{g}\right|^{\frac{n}{2}} d v_{g} .$$
Stability of $S^{p} \times S^{q}$ and $\mathbb{C} P^{n}$ for $\mathcal{W}_{\frac{n}{2}}$ has been studied in [9], [7], [6]. We prove the following result.
Theorem 4. Let $\left(M^{n}, g\right)$ be a closed manifold with dimension $n \geq 6$. If the Riemannian universal cover of $(M, g)$ is the product of a sphere $S^{k}$ and a hyperbolic space $\mathbb{H}^{n-k}(k, n-k \geq 3)$ with the standard product metric, then $\left(M^{n}, g\right)$ is stable for $\mathcal{W}_{\frac{n}{2}}$.

Locally conformally flat manifolds are global minima for $\mathcal{W}_{\frac{n}{2}}$. Topology and rigidity of these metrics with non-negative curvature conditions have been studied in [15], [16]. Whereas some examples of locally conformally flat metrics with negative ricci curvature are constructed in [5] using warped product metrics with constant curvature manifolds as base manifolds. Theorem 4 implies that $S^{n} \times H^{m}$ with standard product metric $g$ is a strict local minimizer for $\mathcal{W}_{\frac{n}{2}}$. Hence there exists a neighbourhood $\mathcal{U}$ of $g$ in $C^{k, \alpha}$-topology such that if $\tilde{g} \in \mathcal{U}$ is a locally conformally flat metric then $c \tilde{g},(c>0)$ is isometric to a metric conformal to $g$. Here $k$ is sufficiently large. $S^{n} \times H^{n}$ is also stable for $\mathcal{R}_{2}$ when the first eigenvalue of the laplacian of $H^{n}$ is sufficiently large (see Section 5.3).

\section*{2. Preliminaries}

In this section, we setup the notations and recall a few definitions to be followed throughout this paper. Let $\left(M^{n}, g\right)$ be a closed Riemannian manifold of dimension $n .\langle\rangle,,\langle,\rangle_{L^{2}}$ respectively denote the point-wise and global inner products induced by $g$ on tensors and $||,.\|$.$\| be the corresponding norms.$ Consider an orthonormal frame $\left\{e_{i}\right\}$ around a point on $M$.
$\check{R}$ is a symmetric 2-tensor defined by
$$\check{R}(x, y)=\sum_{i, j, k} R\left(x, e_{i}, e_{j}, e_{k}\right) R\left(y, e_{i}, e_{j}, e_{k}\right) .$$

The self-adjoint operator $\stackrel{\circ}{R}: S^{2} M \rightarrow S^{2} M$ is given by
$$\stackrel{\circ}{R}(h)(x, y):=\sum_{i, j} R\left(e_{i}, x, e_{j}, y\right) h\left(e_{i}, e_{j}\right) .$$

The Kulkarni-Nomizu product of $h_{1}, h_{2} \in S^{2} M$ is defined as
$$h_{1} \wedge h_{2}(x, y, z, w)=\frac{1}{2}\left[h_{1}(x, z) h_{2}(y, w)+h_{1}(y, w) h_{2}(x, z)-h_{1}(x, w) h_{2}(y, z)-h_{1}(y, z) h_{2}(x, w)\right] .$$
Let $D$ be the Riemannian connection on $(M, g)$ and $D^{*}$ its formal adjoint. The divergence operator $\delta_{g}: S^{2}(M) \rightarrow \Omega^{1}(M)$ is defined by $\delta_{g}(h)(x)=-\sum_{i} D_{e_{i}} h\left(e_{i}, x\right)$. For $h \in S^{2} M$ define
$$d^{D} h(x, y, z)=D_{x} h(y, z)-D_{y} h(x, z) .$$
$\delta_{g}^{*}$ and $\delta^{D}$ denote the adjoints of $\delta_{g}^{*}$ and $d^{D}$ respectively. Then from [3] we have,
$$\delta^{D} d^{D} h=2 D^{*} D h+r \circ h+h \circ r-2 \stackrel{\circ}{R}(h)-\delta_{g}^{*} \delta_{g} h .$$
$h \in S^{2}(M)$ is said to be a transverse traceless tensor (or a TT-tensor) if $\delta_{g}(h)=0$ and $\operatorname{tr}(h)=0$. The Lichnerowicz Laplacian defined on TT-tensors is given by
$$\Delta_{L} h=D^{*} D h+r \circ h+h \circ r-2 \stackrel{\circ}{R}(h) .$$
Let $\Delta$ denote the Hodge-Laplcian acting on differential forms. Then the Böchner-Weitzenböck formula for differential 1-forms is given by
$$\Delta \alpha=D^{*} D \alpha+r(\alpha) \quad \forall \alpha \in \Omega^{1}(M) \quad \text { where } \quad \Delta f=-\operatorname{tr} D d f \quad \forall f \in C^{\infty} M .$$
If $\delta_{g} \alpha=0$ and $(M, g)$ is Einstein, then Böchner-Weitzenböck formula implies that,
$$\|d \alpha\|^{2}=\langle\Delta \alpha, \alpha\rangle_{L^{2}}=\left\langle D^{*} D \alpha, \alpha\right\rangle_{L^{2}}+\lambda\|\alpha\|^{2}=\|D \alpha\|^{2}+\lambda\|\alpha\|^{2}$$
We conclude this section by stating some first variational formulae from [1] Theorem 1.174. Given a oneparameter family $g(t)$ of Riemannian metrics with $g^{\prime}(0)=\left.\frac{d}{d t}(g(t))\right|_{t=0}=h$, let $T_{g}^{\prime}(h)=\left.\frac{d}{d t}(T(t))\right|_{t=0}$,
where $T(t)=T(g(t))$ is a tensor depending on $g(t)$. Then $D_{g}^{\prime}(h), R_{g}^{\prime}(h), r_{g}^{\prime}(h)$ and $s_{g}^{\prime}(h)$ are given by
$$\begin{aligned}
& \text { (i) } \quad C_{h}(x, y, z)=g\left(D_{g}^{\prime}(h)(x, y), z\right)=\frac{1}{2}\left(D_{x} h(y, z)+D_{y} h(x, z)-D_{z} h(x, y)\right) \\
& \text { (ii) } \quad R_{g}^{\prime}(h)(x, y, z, w)=\frac{1}{2}\left[D_{y, z}^{2} h(x, w)+D_{x, w}^{2} h(y, z)-D_{x, z}^{2} h(y, w)-D_{y, w}^{2} h(x, z)\right. \\
& \quad+h(R(x, y, z), w)-h(R(x, y, w), z)] \\
& \text { (iii) } \quad r_{g}^{\prime}(h)=\frac{1}{2}\left(D^{*} D h+r \circ h+h \circ r-2 \stackrel{\circ}{R}(h)-2 \delta_{g}^{*} \delta_{g} h-D d(t r h)\right) \\
& \text { (iv) } \quad s_{g}^{\prime}(h)=\Delta t r h+\delta_{g}^{2}(h)-(r, h)
\end{aligned}$$

\section*{3. Some variational formulae at products of Einstein manifolds}

In this section we compute first variational formulae for tensors associated to gradients of $\mathcal{R}, \mathcal{R} i c$, $\mathcal{S}$ and $\mathcal{W}_{2}$ at products of Einstein manifolds. Gradients of these functionals restricted to the space of Riemannian metrics with constant volume are given below [1].
$$\begin{aligned}
& \nabla \mathcal{R}(g)=2 \delta^{D} d^{D} r-2 \check{R}+\frac{1}{2}|R|^{2} g+\left(\frac{2}{n}-\frac{1}{2}\right)\|R\|^{2} g, \\
& \nabla \mathcal{R} i c(g)=\delta^{D} d^{D} r-D^{*} D r-2 r \circ r+\frac{1}{2}(\Delta s) g+\frac{1}{2}|r|^{2} g+\left(\frac{2}{n}-\frac{1}{2}\right)\|r\|^{2} g, \\
& \nabla \mathcal{S}(g)=2 D d s+2(\Delta s) g-2 s . r+\frac{1}{2}|s|^{2} g+\left(\frac{2}{n}-\frac{1}{2}\right)\|s\|^{2} g .
\end{aligned}$$
From the decomposition of Riemannian curvature tensor $R=\frac{s}{n(n-1)} g \wedge g+\frac{2}{n-2}\left(r-\frac{s}{n} g\right) \wedge g+W$
$$\left|W_{g}\right|^{2}=\left|R_{g}\right|^{2}-\frac{4}{(n-2)}\left(|r|^{2}-\frac{s^{2}}{2(n-1)}\right) .$$
Consequently,
$$\nabla \mathcal{W}_{2}(g)=\nabla \mathcal{R}(g)-\frac{4}{n-2}\left(\nabla \mathcal{R} i c(g)-\frac{1}{2(n-1)} \nabla \mathcal{S}(g)\right) .$$
Let $\left(M^{n_{0}+n_{1}}, g\right)\left(n_{0}+n_{1} \geq 4\right)$ be the product of closed Einstein manifolds $\left(M_{0}^{n_{0}}, g_{0}\right)$ and $\left(M_{1}^{n_{1}}, g_{1}\right)$ with respective Einstein constants $\lambda_{0}$ and $\lambda_{1}$. Consider divergence free one forms $\alpha_{i}$ on $M_{i}$ such that $\|\alpha\|=1$ for each $i=0,1$. Then $h=\alpha_{0} \odot \alpha_{1}=\alpha_{0} \otimes \alpha_{1}+\alpha_{1} \otimes \alpha_{0} \in S^{2}(M)$ survives only on mixed two planes. As
$$\delta_{g}(h)=\delta_{g_{0}}\left(\alpha_{0}\right) \alpha_{1}+\delta_{g_{1}}\left(\alpha_{1}\right) \alpha_{0}$$
$h$ is also divergence free. Hence $h$ is a TT-tensor on $M$. Let $f \in C^{\infty} M_{i+1}$ with $\int_{M_{i+1}} f=0$ for $i=0,1$ and indices are taken modulo 2. Then $\delta_{g}\left(f g_{i}\right)=0, \operatorname{Tr}_{g}\left(f g_{i}\right)=\int_{M} \operatorname{tr}_{g}\left(f g_{i}\right)=0$ and the following identities hold
$$D\left(f g_{i}\right)=d f \otimes g_{i}, D^{2}\left(f g_{i}\right)=D d f \otimes g_{i}, D^{*} D\left(f g_{i}\right)=(\Delta f) g_{i} .$$
$\alpha_{0} \odot \alpha_{1}$ and $f g_{i}$ as described above satisfy following Lemmas. We use Einstein summation convention.
Lemma 1.
$$\begin{aligned}
\text { (i) }\left\langle\left(\delta^{D} d^{D} r\right)^{\prime}\left(f g_{i}\right), f g_{i}\right\rangle_{L^{2}}=n_{i}\left(\|\Delta f\|^{2}\right. & \left.-\left(\lambda_{0}+\lambda_{1}\right)\|d f\|^{2}\right) \\
(i i)\left\langle\left(\delta^{D} d^{D} r\right)^{\prime}\left(\alpha_{0} \odot \alpha_{1}\right), \alpha_{0} \odot \alpha_{1}\right\rangle_{L^{2}}= & 2\left(\left\|\Delta \alpha_{0}\right\|^{2}+\left\|\Delta \alpha_{1}\right\|^{2}+2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle\right) \\
& -\frac{5}{2}\left(\lambda_{0}+\lambda_{1}\right)\left(\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle+\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle\right)+4 \lambda_{0} \lambda_{1}
\end{aligned}$$
Proof. Since $r$ is parallel $\left(\left(\delta^{D}\right)^{\prime} h\right) d^{D} r=0$. Hence,
$$\left\langle\left(\delta^{D} d^{D} r\right)^{\prime}(h), h\right\rangle_{L^{2}}=\left\langle\delta^{D}\left(d^{D}\right)^{\prime}(h) r+\delta^{D} d^{D}\left(r^{\prime}(h)\right), h\right\rangle_{L^{2}}=\left\langle\left(d^{D}\right)^{\prime}(h) r, d^{D} h\right\rangle_{L^{2}}+\left\langle r^{\prime}(h), \delta^{D} d^{D} h\right\rangle_{L^{2}}$$
$\left(d^{D}\right)^{\prime}(h) r$ can be expressed in terms of an orthonormal basis $\left\{e_{i}\right\}$ as
$$\left(\left(d^{D}\right)^{\prime}(h) r\right)_{p q l}=r_{i p} C_{h}\left(e_{q}, e_{l}, e_{i}\right)-r_{i q} C_{h}\left(e_{p}, e_{l}, e_{i}\right)$$

Therefore,
$$\begin{aligned}
\left\langle\left(d^{D}\right)^{\prime}(h) r, d^{D} h\right\rangle & =\left[r_{p i} C_{j k p}-r_{j p} C_{i k p}\right]\left[D h_{i j k}-D h_{j i k}\right] \\
& =2\left[r_{p i} C_{j k p}-r_{j p} C_{i k p}\right] D h_{i j k} \\
& =D h_{i j k}\left\{r_{p i}\left(D h_{j k p}+D h_{k j p}-D h_{p j k}\right)-r_{j p}\left(D h_{i k p}+D h_{k i p}-D h_{p i k}\right)\right\} \\
& =\left[-r_{i i}\left(D h_{i j k}\right)^{2}-r_{j j}\left(D h_{i j k}\right)^{2}+3 r_{i i} D h_{i j k} D h_{j i k}-r_{j j} D h_{i j k} D h_{k i j}\right] \\
& =\left(3 r_{i i}-r_{k k}\right) D h_{j i k} D h_{i j k}-\left(r_{i i}+r_{j j}\right)\left(D h_{i j k}\right)^{2}
\end{aligned}$$
Putting $h=f g_{1}$ and using formulae in (3.3) we have,
$$\begin{aligned}
\left(\left(d^{D}\right)^{\prime}\left(f g_{1}\right) r, d^{D}\left(f g_{1}\right)\right) & =\left(3 r_{i i}-r_{k k}\right) d f_{j} g_{1 i k} d f_{i} g_{1 j k}-\left(r_{i i}+r_{k k}\right)\left[d f_{i} g_{1 k j}\right]^{2} \\
& =-n_{1}\left(\lambda_{0}+\lambda_{1}\right)|d f|^{2}
\end{aligned}$$
From (2.2) and (3.3) one obtains $\left\langle r^{\prime}\left(f g_{1}\right), \delta^{D} d^{D}\left(f g_{1}\right)\right\rangle_{L^{2}}=n_{1}\|\Delta f\|^{2}$. Therefore,
$$\left.\left\langle\left(\delta^{D} d^{D} r\right)^{\prime}\left(f g_{1}\right), f g_{1}\right)\right\rangle_{L^{2}}=n_{1}\|\Delta f\|^{2}-n_{1}\left(\lambda_{0}+\lambda_{0}\right)\|d f\|^{2} .$$
Considering $h=\alpha_{0} \odot \alpha_{1}$ in (3.4),
$$\begin{aligned}
\left\langle r^{\prime}\left(\alpha_{0} \odot \alpha_{1}\right), \delta^{D} d^{D}\left(\alpha_{0} \odot \alpha_{1}\right)\right\rangle_{L^{2}}= & \left\|D^{*} D\left(\alpha_{0} \odot \alpha_{1}\right)\right\|^{2}+\frac{1}{2}\left(\lambda_{0}+\lambda_{1}\right)^{2}\left\|\alpha_{0} \odot \alpha_{1}\right\|^{2} \\
& +\frac{3}{2}\left(\lambda_{0}+\lambda_{1}\right)\left\langle D^{*} D\left(\alpha_{0} \odot \alpha_{1}\right), \alpha_{0} \odot \alpha_{1}\right\rangle_{L^{2}}
\end{aligned}$$
$$\begin{aligned}
\left\langle\left(d^{D}\right)^{\prime}\left(\alpha_{0} \odot \alpha_{1}\right) r, d^{D}\left(\alpha_{0} \odot \alpha_{1}\right)\right\rangle= & \left(3 r_{i i}-r_{k k}\right) D h_{j i k} D h_{i j k}-\left(r_{i i}+r_{j j}\right)\left(D h_{i j k}\right)^{2} \\
= & \left(3 \lambda_{0}-\lambda_{1}\right)\left|\alpha_{1}\right|^{2} D\left(\alpha_{0}\right)_{i j} D\left(\alpha_{0}\right)_{j i}+\left(3 \lambda_{1}-\lambda_{0}\right)\left|\alpha_{0}\right|^{2} D\left(\alpha_{1}\right)_{i j} D\left(\alpha_{1}\right)_{j i} \\
& -\left(3 \lambda_{0}+\lambda_{1}\right)\left|\alpha_{1}\right|^{2}\left|D \alpha_{0}\right|^{2}-\left(3 \lambda_{1}+\lambda_{0}\right)\left|\alpha_{0}\right|^{2}\left|D \alpha_{1}\right|^{2} .
\end{aligned}$$
Since $D\left(\alpha_{i}\right)_{p q} D\left(\alpha_{i}\right)_{q p}=\left|D \alpha_{i}\right|^{2}-\frac{1}{2}\left|d \alpha_{i}\right|^{2}$ one obtains,
$$\begin{aligned}
\left\langle\left(d^{D}\right)^{\prime}\left(\alpha_{0} \odot \alpha_{1}\right) r, d^{D}\left(\alpha_{0} \odot \alpha_{1}\right)\right\rangle= & -\frac{1}{2}\left(3 \lambda_{0}-\lambda_{1}\right)\left|\alpha_{1}\right|^{2}\left|d \alpha_{0}\right|^{2}-2 \lambda_{1}\left|\alpha_{1}\right|^{2}\left|D \alpha_{0}\right|^{2} \\
& -\frac{1}{2}\left(3 \lambda_{1}-\lambda_{0}\right)\left|\alpha_{0}\right|^{2}\left|d \alpha_{1}\right|^{2}-2 \lambda_{0}\left|\alpha_{0}\right|^{2}\left|D \alpha_{1}\right|^{2}
\end{aligned}$$
Using (2.1) we have,
$$\left\langle\left(d^{D}\right)^{\prime}(h) r, d^{D} h\right\rangle_{L^{2}}=-\frac{1}{2}\left(3 \lambda_{0}^{2}+3 \lambda_{1}-2 \lambda_{0} \lambda_{1}\right)\left\|\alpha_{0}\right\|^{2}\left\|\alpha_{1}\right\|^{2}-\frac{3}{2}\left(\lambda_{0}+\lambda_{1}\right)\left(\left\|D \alpha_{0}\right\|^{2}+\left\|D \alpha_{1}\right\|^{2}\right)$$
Putting $\left\|\alpha_{i}\right\|=1$ and combining all the expressions above, the result follows. \(\square\)

Lemma 2.
\begin{itemize}
\item[(i)] $\left\langle\left(D^{*} D r\right)^{\prime}\left(f g_{i}\right), f g_{i}\right\rangle_{L^{2}}=\frac{n_{i}}{2}\left(\|\Delta f\|^{2}-2 \lambda_{i}\|d f\|^{2}\right)$
\item[(ii)] $\left\langle\left(D^{*} D r\right)^{\prime}\left(\alpha_{1} \odot \alpha_{2}\right), \alpha_{1} \odot \alpha_{2}\right\rangle_{L^{2}}=\left\|\Delta \alpha_{1}\right\|^{2}+\left\|\Delta \alpha_{2}\right\|^{2}+2\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\left\langle\Delta \alpha_{2}, \alpha_{2}\right\rangle_{L^{2}}+4 \lambda_{1} \lambda_{2}$
$$-\frac{1}{2}\left(3 \lambda_{1}+5 \lambda_{2}\right)\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}-\frac{1}{2}\left(3 \lambda_{2}+5 \lambda_{1}\right)\left\langle\Delta \alpha_{2}, \alpha_{2}\right\rangle_{L^{2}}$$
\end{itemize}
Proof. Since the Ricci tensor is parallel $D^{*}\left(D^{\prime}(h) r\right)=0$. Therefore,
$$\left\langle\left(D^{*} D r\right)^{\prime}(h), h\right\rangle_{L^{2}}=\left\langle D^{*}\left(D^{\prime}(h) r\right)+D^{*} D\left(r^{\prime}(h)\right), h\right\rangle_{L^{2}}=\left\langle(D)^{\prime}(h) r, D h\right\rangle_{L^{2}}+\left\langle r^{\prime}(h), D^{*} D h\right\rangle_{L^{2}}$$
With respect to an orthonormal basis $D_{g}^{\prime}(h) r$ can be written as,
$$\left(D^{\prime}(h) r\right)_{p q l}=-r_{i l} C_{p q i}-r_{i q} C_{p l i}=-r_{l l} C_{p q l}-r_{q q} C_{p l q}=-2 r_{q q} C_{p l q}$$
For $h=f g_{1}$ one has $\left\langle r^{\prime}(h), D^{*} D h\right\rangle_{L^{2}}=\frac{1}{2}\|\Delta f\|^{2}$.
$$\left\langle\left(D^{\prime}\left(f g_{1}\right) r\right), D\left(f g_{1}\right)\right\rangle=-2 r_{q q} C_{p l q} d f_{p} g_{1 q l}=-r_{q q}\left(d f_{p}\right)^{2} g_{1 q q}=-n_{1} \lambda_{1}|d f|^{2} .$$
Therefore,
$$\left\langle\left(D^{*} D r\right)^{\prime}\left(f g_{1}\right), f g_{1}\right\rangle_{L^{2}}=\frac{n_{1}}{2}\|\Delta f\|^{2}-n_{1} \lambda_{1}\|d f\|^{2} .$$

Considering $h=\alpha_{1} \odot \alpha_{2}$ we have,
$$\left\langle r^{\prime}\left(\alpha_{1} \odot \alpha_{2}\right), D^{*} D\left(\alpha_{1} \odot \alpha_{2}\right)\right\rangle_{L^{2}}=\frac{1}{2}\left\|D^{*} D\left(\alpha_{1} \odot \alpha_{2}\right)\right\|^{2}+\frac{1}{2}\left\|D\left(\alpha_{1} \odot \alpha_{2}\right)\right\|^{2}$$
Also in this case, $\left\langle\left(D^{\prime}(h) r\right), D h\right\rangle=-r_{k k}\left(D h_{i j k}+D h_{j i k}-D h_{k j i}\right) D h_{i j k}$. Hence,
$$\begin{aligned}
\left\langle\left(D^{\prime}\left(\alpha_{0} \odot \alpha_{1}\right) r\right), D\left(\alpha_{0} \odot \alpha_{1}\right)\right\rangle= & -\left(\lambda_{0}-\lambda_{1}\right)\left(\left|\alpha_{1}\right|^{2}\left(D \alpha_{0 i j} D \alpha_{0 j i}\right)-\left|\alpha_{0}\right|^{2}\left(D \alpha_{1 i j} D \alpha_{1 j i}\right)\right) \\
& -\frac{1}{2}\left(\lambda_{0}+\lambda_{1}\right)\left|D\left(\alpha_{0} \odot \alpha_{1}\right)\right|^{2} \\
= & -\frac{3 \lambda_{0}+\lambda_{1}}{2}\left|D \alpha_{0}\right|^{2}\left|\alpha_{1}\right|^{2}-\frac{3 \lambda_{2}+\lambda_{1}}{2}\left|D \alpha_{1}\right|^{2}\left|\alpha_{0}\right|^{2} \\
& +\frac{1}{2}\left(\lambda_{0}-\lambda_{1}\right)^{2}\left|\alpha_{0}\right|^{2}\left|\alpha_{1}\right|^{2}
\end{aligned}$$
Putting $\left\|\alpha_{i}\right\|=1(i=1,2)$ and using (2.1) we obtain the desired result. \(\square\)

Lemma 3.
$$\begin{aligned}
& (i)\left\langle(r \circ r)^{\prime}\left(f g_{i}\right), f g_{i}\right\rangle_{L^{2}}=\lambda_{i} n_{i}\left(\|d f\|^{2}-\lambda_{i}\|f\|^{2}\right) \\
& (i i)\left\langle(r \circ r)^{\prime}\left(\alpha_{1} \odot \alpha_{2}\right), \alpha_{1} \odot \alpha_{2}\right\rangle_{L^{2}}=\left(\lambda_{1}+\lambda_{2}\right)\left(\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}+\left\langle\Delta \alpha_{2}, \alpha_{2}\right\rangle_{L^{2}}\right)-2 \lambda_{1} \lambda_{2}
\end{aligned}$$
Proof. In local coordinates $r \circ r$ can be described as $(r \circ r)_{p q}=g^{i j} r_{p i} r_{q j}$. Therefore,
$$\begin{aligned}
{\left[(r \circ r)^{\prime}(h)\right]_{p q} } & =\left(g^{i j}\right)^{\prime} r_{p i} r_{q j}+g^{i j} r_{p i}^{\prime} r_{q j}+g^{i j} r_{p i} r_{q j}^{\prime} \\
& =-g^{i k} h_{k l} g^{l j} r_{p i} r_{q j}+\left(r^{\prime}(h) \circ r\right)_{p q}+\left(r \circ r^{\prime}(h)\right)_{p q} \\
& =-(r \circ h \circ r)_{p q}+\left(r^{\prime}(h) \circ r+r \circ r^{\prime}(h)\right)_{p q} .
\end{aligned}$$
Hence, $\left\langle(r \circ r)^{\prime}(h), h\right\rangle=-r_{p p} r_{q q}\left(h_{p q}\right)^{2}+\left\langle r^{\prime}(h), h \circ r+r \circ h\right\rangle$.
Putting $h=f g_{1}$ in the above equation we have,
$$\left\langle(r \circ r)^{\prime}\left(f g_{1}\right), f g_{1}\right\rangle_{L^{2}}=-\lambda_{1}^{2} n_{1}\|f\|^{2}+n_{1} \lambda_{1}\|d f\|^{2}$$
When $h=\alpha_{0} \odot \alpha_{1}$, one has
$$\left\langle(r \circ r)^{\prime}\left(\alpha_{0} \odot \alpha_{1}\right), \alpha_{0} \odot \alpha_{1}\right\rangle_{L^{2}}=\frac{1}{2}\left(\lambda_{0}^{2}+\lambda_{1}^{2}\right)\left\|\alpha_{0} \odot \alpha_{1}\right\|^{2}+\frac{1}{2}\left\|D\left(\alpha_{0} \odot \alpha_{1}\right)\right\|^{2}$$
The Lemma now follows from (2.1). \(\square\)

Lemma 4. Let $\left(M^{n_{0}+n_{1}}, g\right)$ be the product of a spherical space form $\left(M_{0}, g_{0}\right)$ and a compact hyperbolic manifold $\left(M_{1}, g_{1}\right)$ with constant sectional curvatures 1 and -1 respectively. Then
\begin{itemize}
\item[(i)] $\left\langle(\check{R})^{\prime}\left(f g_{i}\right), f g_{i}\right\rangle_{L^{2}}=-\left\|R^{i}\right\|^{2}\|f\|^{2}$;
\item[(ii)] $\left(|R|^{2}\right)^{\prime}\left(f g_{i}\right)=-2 f\left|R^{i}\right|^{2}$;
\item[(iii)] $\left\langle(\check{R})^{\prime}\left(\alpha_{0} \odot \alpha_{1}\right), \alpha_{0} \odot \alpha_{1}\right\rangle_{L^{2}}=2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}-2\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}-4\left(n_{0}+n_{1}-2\right)$
\end{itemize}
where $R^{i}$ denotes the Riemannian curvature tensor of $\left(M_{i}, g_{i}\right)$.
Proof. With respect to an arbitrary basis $\check{R}$ can be written as
$$\check{R}_{p q}=g^{i_{1} i_{2}} g^{j_{1} j_{2}} g^{k_{1} k_{2}} R_{p i_{1} j_{1} k_{1}} R_{q i_{2} j_{2} k_{2}} .$$
Differentiating each terms and putting $\left(g^{i j}\right)^{\prime}=-g^{i m} h_{m n} g^{n j}$ we have,
$$\begin{aligned}
\left(\check{R}_{g}\right)^{\prime}(h)_{p q} & =-h_{m n}\left(R_{p m i j} R_{q n i j}+R_{p i m j} R_{q i n j}+R_{p i j m} R_{q i j n}\right)+\left(R_{g}^{\prime}(h)\right)_{p i j k} R_{q i j k}+R_{p i j k}\left(R_{g}^{\prime}(h)\right)_{q i j k} \\
& =-h_{m n}\left[R_{p m i j} R_{q n i j}+2 R_{p i m j} R_{q i n j}\right]+\left(R_{g}^{\prime}(h)\right)_{p i j k} R_{q i j k}+R_{p i j k}\left(R_{g}^{\prime}(h)\right)_{q i j k}
\end{aligned}$$
Setting
$$L(x, y, z, w)=L_{h}(x, y, z, w)=D_{y, z}^{2} h(x, w)+D_{x, w}^{2} h(y, z)-D_{x, z}^{2} h(y, w)-D_{y, w}^{2} h(x, z)$$
and using symmetries of $R$ and $h$, one obtains
$$\left(\left(R_{g}^{\prime}(h)\right)_{\text {pijk }} R_{q i j k}+R_{p i j k}\left(R_{g}^{\prime}(h)\right)_{q i j k}\right) h_{p q}=2 h_{p q}\left(R_{g}^{\prime}(h)\right)_{p i j k} R_{q i j k}=\left\{L_{p i j k} h_{p q} R_{q i j k}+2 R_{p i m j} R_{q i n j} h_{m n}\right\}$$

Therefore,
$$\begin{aligned}
\left\langle(\check{R})^{\prime}(h), h\right\rangle & =\left(\check{R}_{g}\right)^{\prime}(h)_{p q} h_{p q} \\
& =\left\{L_{p i j k} R_{q i j k} h_{p q}-h_{m n} h_{p q} R_{p m i j} R_{q n i j}\right\}
\end{aligned}$$
Let $h=f g_{i}$. Using (3.3) we have $L=D d f \wedge g_{i}$ and
$$\left\langle(\check{R})^{\prime}\left(f g_{i}\right), f g_{i}\right\rangle=\left\{f L_{p q j k} R_{p q j k}^{1}-f^{2} R_{p m q j}^{i} R_{p m q j}^{i}\right\}=\left\langle D d f \wedge g_{i}, f R^{i}\right\rangle-|f|^{2}\left|R^{i}\right|^{2}=-|f|^{2}\left|R^{i}\right|^{2} .$$
Also, since $|R|^{2}=\operatorname{tr}(\check{R})$, one has
$$\left(|R|^{2}\right)^{\prime}\left(f g_{i}\right)=\left\langle(\check{R})^{\prime}\left(f g_{i}\right), g\right\rangle-\left\langle\check{R}, f g_{i}\right\rangle=-2 f\left|R^{i}\right|^{2}$$
If $h=\alpha_{0} \odot \alpha_{1}$ then
$$h_{m n} h_{p q} R_{p m i j} R_{q n i j}=R\left(\alpha_{0}, \alpha_{1}, e_{i}, e_{j}\right) R\left(\alpha_{0}, \alpha_{1}, e_{i}, e_{j}\right)=0$$
Also,
$$h_{p q} L_{p i j k} R_{q i j k}=h_{p q}\left[D^{2} h_{p k i j}+D^{2} h_{i j p k}-D^{2} h_{p j i k}-D^{2} h_{i k p j}\right] R_{q i j k}=2 h_{p q}\left[D^{2} h_{p k i j}-D^{2} h_{i k p j}\right] R_{q i j k}$$
Since $R$ is parallel, $\left.h_{p q} D^{2} h_{p k i j} R_{q i j k}=-\left\langle\delta_{g}^{*} \delta_{g} \stackrel{\circ}{R}(h)\right), h\right\rangle=0$. Finally, one obtains
$$\begin{aligned}
L_{p i j k} R_{q i j k} h_{p q} & =2 D^{2} h_{i j p k} R_{q i j k} h_{p q} \\
& =2\left[\left(\left(\alpha_{0}\right)_{p}\right)^{2}\left(\alpha_{1}\right)_{q}\left(D^{2} \alpha_{1}\right)_{i j k} R_{q i j k}+\left(\left(\alpha_{1}\right)_{p}\right)^{2}\left(\alpha_{0}\right)_{q}\left(D^{2} \alpha_{0}\right)_{i j k} R_{q i j k}\right] \\
& =2\left|\alpha_{1}\right|^{2}\left(D^{2}\left(\alpha_{0}\right)_{i j i}-D^{2}\left(\alpha_{0}\right)_{i i j}\right)\left(\alpha_{0}\right)_{j}-2\left|\alpha_{0}\right|^{2}\left(D^{2}\left(\alpha_{1}\right)_{i j i}-D^{2}\left(\alpha_{1}\right)_{i i j}\right)\left(\alpha_{1}\right)_{j} \\
& =2\left(\left|\alpha_{1}\right|^{2}\left|D \alpha_{0}\right|^{2}-\left|\alpha_{1}\right|^{2}\left|D \alpha_{0}\right|^{2}\right)+2\left|\alpha_{1}\right|^{2} D^{2}\left(\alpha_{0}\right)_{i j i}\left(\alpha_{0}\right)_{j}-2\left|\alpha_{0}\right|^{2} D^{2}\left(\alpha_{1}\right)_{i j i}\left(\alpha_{1}\right)_{j}
\end{aligned}$$
The Ricci-identity for 1 -forms implies,
$$D^{2}\left(\alpha_{k}\right)_{i j i}\left(\alpha_{k}\right)_{j}=\left(\left(D^{2}\left(\alpha_{k}\right)_{j i i}-\alpha_{k}\left(R_{j i i}\right)\right)\left(\alpha_{k}\right)_{j}=-e_{j}\left(\delta \alpha_{k}\right)\left(\alpha_{k}\right)_{j}-\left(r_{k}\right)_{j j}\left(\alpha_{k}\right)_{j}^{2}\right.$$
Using $\delta\left(\alpha_{k}\right)=0$ and putting $r_{0}=n_{0}-1, r_{1}=-\left(n_{1}-1\right)$ one obtains
$$\left\langle(\check{R})^{\prime}(h), h\right\rangle_{L^{2}}=2\left(\left\|\alpha_{1}\right\|^{2}\left\|D \alpha_{0}\right\|^{2}-\left\|\alpha_{0}\right\|^{2}\left\|D \alpha_{1}\right\|^{2}\right)-2\left(n_{0}+n_{1}-2\right)\left\|\alpha_{0}\right\|^{2}\left\|\alpha_{1}\right\|^{2}$$
Finally, putting $\left\|\alpha_{0}\right\|=1=\left\|\alpha_{1}\right\|$, and using (2.1) the result follows. \(\square\)

\section*{4. Second variations of Ric}

Let $(M, g)=\left(M_{0} \times M_{1}, g_{0}+g_{1}\right)$ be as described in Section 3 with $\left|\lambda_{0}\right|=\left|\lambda_{1}\right|$. A traceless symmetric 2-tensor $h$ on $M$ decomposes as [9]
$$h=h_{1}+\hat{h}+h_{2}+f\left(n_{1} g_{0}-n_{0} g_{1}\right)$$
where $h_{1}, h_{2}$ are TT-tensors tangent to $M_{1}$ and $M_{2}$ respectively, $\hat{h}$ is a TT-tensor on $M$ surviving only on mixed planes, and $f \in C^{\infty} M$. This decomposition is orthogonal. Let $S_{1}^{2} M, S_{0}^{2} M, S_{2}^{2} M$ denote the first three components of the above decomposition respectively. Then
$$S^{2} M=I m \delta_{g}^{*} \oplus S_{1}^{2} M \oplus S_{0}^{2} M \oplus S_{2}^{2} M \oplus\left(C^{\infty} M g_{1}+C^{\infty} M g_{2}\right)$$
4.1. Transverse-traceless variations : From the above decomposition it is easy to see that if $h$ is a TT-tensor on $M$ then $h \in S_{1}^{2} M \oplus S_{0}^{2} M \oplus S_{2}^{2} M \oplus \mathbb{R} .\left(n_{1} g_{0}-n_{0} g_{1}\right)$. The last component is the span of parallel tensor $n_{1} g_{0}-n_{0} g_{1}$.

Theorem 5. Let $\left(M^{n_{0}+n_{1}}, g\right)\left(n_{0}, n_{1} \geq 3\right)$ be the product of two closed Einstein manifolds $\left(M_{0}^{n_{0}}, g_{0}\right)$ and $\left(M_{1}^{n_{1}}, g_{1}\right)$ with respective Einstein constants $\lambda_{0}, \lambda_{1}$. If $(M, g)$ is a critical metric of $\mathcal{R}$ ic then there exists a constant $C>0$ such that for any $T T$-tensor $h$ on $M$,
$$\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}} \geq C\|h\|^{2}$$
if and only if the Hessian of $\mathcal{R}$ ic restricted to the $T T$-tensors on $\left(M_{i}, g_{i}\right)$ satisfies the same condition for each $i=0,1$.

Proof. Let $H$ denote the Hessian of Ric at $g$. Using Lemmas 12 and 3, it is easy to see that the decomposition given by (1.1) is orthogonal with respect to $H$. Therefore, it is sufficient to prove (4.2) component-wise.

The standard projection map from $M$ to $M_{i}$ induce an isomorphism between $S_{i}^{2} M$ to the space of TT-tensors on $M_{i}$ for each $i$. For any $h \in S_{1}^{2} M$ there exists a two parameter family of metrics $g_{s, t}$ on $M_{0}$ with $g_{0,0}=g_{0}$ such that
$$H(h, h)=\frac{\partial}{\partial s} \frac{\partial}{\partial t} \mathcal{R} i c\left(g_{s, t}+g_{2}\right)_{\mid(0,0)} .$$
Using Riemannian product structure we see that $H$ restricted to $S_{1}^{2} M$ has a positive lower bound if and only if the Hessian of $\mathcal{R} i c$ on $\left(M_{1}, g_{1}\right)$ acting on TT -tensors satisfies (4.2). Similar argument holds for $S_{2}^{2} M$.

Let $\alpha_{0}$ and $\alpha_{1}$ be two divergence free 1-forms on $M_{0}$ and $M_{1}$ with $\left\|\alpha_{0}\right\|=\left\|\alpha_{1}\right\|=1$. Define, $h=\alpha_{0} \odot \alpha_{1}$. The set of all two tensors of this type is dense in $S_{0}^{2} M$. Therefore to prove that $H$ satisfies (4.2) on $S_{0}^{2} M$, it is sufficient to prove that $H$ satisfies the same for tensors of type $\alpha_{0} \odot \alpha_{1}$. The following possibilities arise.

Case $\left(\lambda_{0}=-\lambda_{1}=\lambda>0\right)$ : If $\mu_{0}$ denotes the first eigenvalue of the laplacian on $\Omega^{1}\left(M_{0}\right)$. (2.1) implies that $\mu_{0}>\lambda$. Now using Lemmas 1, 2 and 3 we have,
$$\begin{aligned}
\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}} & =\left\langle\left(\delta^{D} d^{D} r\right)^{\prime}(h)-\left(D^{*} D r\right)^{\prime}(h)-2(r \circ r)^{\prime}(h), h\right\rangle_{L^{2}}+\frac{2}{n_{0}+n_{1}}\|r\|^{2}\|h\|^{2} \\
& =\left\|\Delta \alpha_{0}\right\|^{2}+\left\|\Delta \alpha_{1}\right\|^{2}+2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}-\lambda\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}+\lambda\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}
\end{aligned}$$
Since,
$$\left\|\Delta \alpha_{0}\right\|^{2}-\lambda\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}=\left\|\alpha_{0}-\lambda \alpha_{0}\right\|^{2}+\lambda\left\langle\Delta \alpha_{0}-\lambda \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}} \geq \mu(\mu-\lambda)>0$$
and the remaining terms in the expression of $\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle$ are non-negative, the proof follows.
Case $\left(\lambda_{0}=\lambda_{1}=\lambda\right)$ : Let $\lambda$ be the Einstein constant of both $\left(M_{i}, g_{i}\right)$. From Lemmas 1, 2 and 3 we have,
$$\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}}=\left\|\Delta \alpha_{0}\right\|^{2}+\left\|\Delta \alpha_{1}\right\|^{2}+2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}+8 \lambda^{2}-5 \lambda\left(\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}+\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\right)$$
Clearly $\lambda<0$, then the proof follows. When $\lambda>0$ then using (2.1) we have,
$$\begin{aligned}
\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}}= & \left\|D^{*} D \alpha_{0}\right\|^{2}+\left\|D^{*} D \alpha_{1}\right\|^{2}-\lambda\left\|D \alpha_{0}\right\|^{2}-\lambda\left\|D \alpha_{1}\right\|^{2}+12 \lambda^{2} \\
= & \left\|D^{*} D \alpha_{0}-\frac{\lambda}{2} \alpha_{0}\right\|^{2}+\left\|D^{*} D \alpha_{1}-\frac{\lambda}{2} \alpha_{1}\right\|^{2}+\left(12-\frac{1}{4}\right) \lambda^{2} \\
& >11 \lambda^{2}
\end{aligned}$$ \(\square\)
4.2. Conformal Variations: In this section we study $H$ restricted to $C^{\infty} M_{1} . g_{0}+C^{\infty} M_{0} . g_{1}$. Let $\mathcal{M}(g)$ denote the space of all unit volume metrics conformal to $g$. The tangent space of $\mathcal{M}(g)$ consists of 2-tensors of the form $f g$ with $\int_{M} f d v_{g}=0$.

Lemma 5. Let $(M, g)$ be the product of two closed Einstein manifolds $\left(M_{0}^{n_{0}}, g_{0}\right)$ and $\left(M_{1}^{n_{1}}, g_{0}\right)$ with respective Einstein constants $\lambda_{0}$ and $\lambda_{1}$ such that $\left|\lambda_{i}\right|=\lambda$. Let $h=f g_{i}$ where $f \in C^{\infty} M_{i+1}$. Then
$$\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}}=\left\{\begin{array}{l}
\frac{n_{i}\left(n_{i}+1\right)}{2}\|\Delta f\|^{2}-\frac{\lambda_{i} n_{i}\left(n_{i}+2\right)}{2}\|d f\|^{2}-\lambda^{2} n_{i}\left(n_{i}-4\right)\|f\|^{2}, \text { if } \lambda_{0}=-\lambda_{1} ; \\
\frac{n_{i}\left(n_{i}+1\right)}{2}\|\Delta f\|^{2}+\frac{\lambda n_{i}\left(n_{i}-6\right)}{2}\|d f\|^{2}-\lambda^{2} n_{i}\left(n_{i}-4\right)\|f\|^{2}, \text { if } \lambda_{0}=\lambda_{1} .
\end{array}\right.$$
Proof. Note that in this case,
$$\begin{aligned}
\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}}= & \left\langle\left(\delta^{D} d^{D} r\right)^{\prime}(h)-\left(D^{*} D r\right)^{\prime}(h)-2(r \circ r)^{\prime}(h), h\right\rangle_{L^{2}}+\frac{1}{2}\left\langle\left(\Delta s^{\prime}(h)\right) g+\left(|r|^{2}\right)^{\prime}(h) g, h\right\rangle_{L^{2}} \\
& +2 \lambda^{2}\|h\|^{2}
\end{aligned}$$

In local coordinates $|r|^{2}$ can be written as $|r|^{2}=r_{i j} r_{k l} g^{i k} g^{j l}$. Differentiating the expression we have,
$$\begin{aligned}
\left(|r|^{2}\right)^{\prime}(h) & =r^{\prime}(h)_{i j} r_{k l} g^{i k} g^{j l}+r_{i j} r^{\prime}(h)_{k l} g^{i k} g^{j l}+r_{i j} r_{k l}\left(\left(g^{i k}\right)^{\prime} g^{j l}+g^{i k}\left(g^{j l}\right)^{\prime}\right) \\
& =2 r^{\prime}(h)_{i j} r_{i j}-r_{i j} r_{k j} h_{i k}-r_{i j} r_{i l} h_{j l} \\
& =n_{i}\left(\left(\lambda_{0}+\lambda_{1}\right) \Delta f-2 \lambda_{i}^{2} f\right) .
\end{aligned}$$
Also, since $s$ is a constant and $\langle g, h\rangle=0$, one obtains $\left\langle(\Delta s)^{\prime}(h) g, h\right\rangle=\left\langle\Delta s^{\prime}(h) g, h\right\rangle$. Hence,
$$s^{\prime}(h)=-(r, h)+\Delta t r h=n_{i}\left(\Delta^{2} f-\lambda_{i} \Delta f\right)$$
Therefore $\left\langle(\Delta s)^{\prime}(h) g, h\right\rangle_{L^{2}}=n_{i}^{2}\left(\|\Delta f\|^{2}-\lambda_{i}\|d f\|^{2}\right)$. Now the result follows combining Lemmas 1, 2, 3 and the above expressions. \(\square\)

Proof of Theorem 1 : Let $\left|\lambda_{i}\right|=\lambda>0$ and $f_{i} \in C^{\infty} M_{i+1}$ for $i=0,1$ (indices $\bmod 2$ ). We notice that $H\left(f_{0} g_{1}, f_{1} g_{0}\right)=0$. Therefore, to prove stability of $\mathcal{R} i c$ restricted to $\mathcal{M}_{W}$ it sufficient to prove that for each $i=0,1$ there exists $C_{i}$ such that
$$H\left(f_{i} g_{i+1}, f_{i} g_{i+1}\right) \geq C_{i} \quad \forall f_{i} \in C^{\infty}\left(M_{i}\right) .$$
\begin{itemize}
\item[(1)] Case $\left(\lambda_{0}=\lambda_{1}=\lambda\right)$ : If $\lambda_{i}>0$ then (2.1) implies that $\mu_{i} \geq \lambda$. Then the result follows from Lemma 5 using (2.1). When $\lambda_{i}<0$, consider the polynomial $p(a, x)=(a+1) x^{2}-(a-6) x-$ $2(a-4)$. When $a=3$ or 4, $p(a, x)>0$ for all $x>0$. When $a>4$ then
$$p(a, x)>0 \text { for } x>c(a)=\frac{(a-6)+\sqrt{9 a^{2}-36 a+4}}{2(a+1)} .$$
Let $f_{i}$ be an eigenfunction corresponding to the first eigenvalue $\mu_{i}$ of $\Delta$. Lemma 5 implies that $H\left(f_{i} g_{i+1}, f_{i} g_{i+1}\right)>0$ if and only if $p\left(n_{i}, \frac{\mu_{i+1}}{\lambda}\right)>0$. Therefore, if $\frac{\mu_{i+1}}{\lambda}>c\left(n_{i}\right)$ then $H\left(f_{i} g_{i+1}, f_{i} g_{i+1}\right)>0$. Hence the proof follows.
\item[(2)] Case $\left(\lambda_{0}=-\lambda_{1}\right): H\left(f_{0} g_{1}, f_{0} g_{1}\right)$ is positive since $\frac{\mu_{0}}{\lambda}>1$. If $\frac{\mu_{1}}{\lambda}>\frac{\left(n_{1}+2\right)+\sqrt{9 n_{1}^{2}-20 n_{1}-28}}{2\left(n_{1}+1\right)}$ then $H\left(f_{1} g_{0}, f_{1} g_{0}\right)$ is positive by similar argument as in the previous case.
\end{itemize}

Proof of Theorem 2. As a consequence of Theorem 5 and Theorem 1, it is sufficient to prove stability of $\mathcal{R} i c$ restricted to conformal variations of $\left(g_{0}+g_{1}\right)$. Since $C^{\infty} M_{0} \oplus C^{\infty} M_{1}$ is dense in $C^{\infty} M$ we study $H$ restricted to $\left\{f_{0} g_{0}+f_{1} g_{1}: f_{i} \in C^{\infty}\left(M_{i}\right), i=0,1\right\}$. Notice that $H\left(f_{0} g_{0}, f_{1} g_{1}\right)=0$. As each $\left(M_{i}, g_{i}\right)$ is stable for $\mathcal{R} i c$, there exist positive constant $C_{i}>0$ such that for each $i=0,1$
$$H\left(f g_{i}, f g_{i}\right) \geq C_{i} \quad \forall f \in C^{\infty} M_{i} \text { with } \int_{M_{i}} f=0$$
Hence the theorem follows .
Examples of Stable manifolds: Some known examples of stable critical metrics of $\mathcal{R} i c$ are quotients of $S^{n}(n \geq 3)$, the complex projective space $\mathbb{C} P^{m}, m \geq 2$, compact hyperbolic manifolds $H^{n}$ with dimensions 3, 4, and compact hyperbolic manifolds $H^{n}(n>4)$ with first eigenvalue $\mu>\frac{2(n-1)(n-4)}{n}$ (see [8]). As a direct consequence of Theorem 2, one observes that the following product manifolds are stable for Ric.
\begin{itemize}
\item[(1)] $S^{n_{1}} \times S^{n_{2}} \ldots . \times S^{n_{k}}\left(n_{i} \geq 3, i=1,2, . ., k\right)$
\item[(2)] $\mathbb{C} P^{n_{1}} \times \mathbb{C} P^{n_{2}} \ldots \times \mathbb{C} P^{n_{k}}$ (for $n_{i} \geq 2, i=1,2, . ., k$ )
\item[(3)] $H_{1} \times H_{2} \times \ldots \times H_{k}$ where $H_{i}$ is a compact hyperbolic manifold with dimension 3 or 4 for $i=1,2, . ., k$.
\item[(4)] Product of Riemannian manifolds stated in 1,2,3.
\item[(5)] Let $H_{1}^{n}, H_{2}^{m}(n, m \geq 4)$ be two compact hyperbolic manifolds with first eigenvalues of Laplacian $\mu_{1}$ and $\mu_{2}$ respectively. The product manifold $H_{1}^{n} \times H_{2}^{m}$ is stable if and only if
$$\frac{\mu_{1}}{n-1}>\max \left\{c(m), 2-\frac{8}{n}\right\} \text { and } \frac{\mu_{2}}{m-1}>\max \left\{c(n), 2-\frac{8}{m}\right\}$$
\begin{itemize}
\item[] i.e. in particular, if $\mu_{1}>2(n-1)$ and $\mu_{2}>2(m-1)$ then $H_{1}^{n}, \times H_{2}^{m}$ is stable.
\end{itemize}
\end{itemize}
\begin{itemize}
\item[(6)] Let $H^{m}$ be a compact hyperbolic manifold. The product manifold $S^{n} \times H^{m}(n, m \geq 3$, one of them bigger than 4) is stable for $\mathcal{R} i c$ if and only if $\frac{\mu}{m-1}>\max \left\{\frac{2(m-4)}{m}, \frac{(n+2)+\sqrt{9 n^{2}-20 n-28}}{2(n+1)}\right\}$, where $\mu$ is the first eigenvalue of the Laplacian on $H^{m}$.
\item[(7)] $S^{n} \times H^{m}(n, m \geq 3)$ is stable if $\mu>2(m-1)$.
\end{itemize}

Unstable manifolds : Let $H_{1}^{n}, H_{2}^{m}(n, m \geq 4)$ be compact hyperbolic space forms both stable for Ric, then their Riemannian product $H_{1}^{n} \times H_{2}^{m}$ is unstable if
$$\text { either } 2-\frac{8}{n}<\frac{\mu_{1}}{n-1}<c(m) \quad \text { or } \quad 2-\frac{8}{m}<\frac{\mu_{2}}{m-1}<c(n)$$
where $\mu_{i}, c(i=1,2)$ are as in Theorem 1.
Next, consider $M=S^{n} \times H^{m}$ such that the first eigenvalue $\mu$ of $\Delta$ of $H^{m}$ satisfies
$$\frac{2(m-4)}{m}<\frac{\mu}{m-1}<\frac{(n+2)+\sqrt{9 n^{2}-20 n-28}}{2(n+1)} .$$
Although $S^{n}$ and $H^{m}$ both are individually stable for $\mathcal{R} i c$, their product $S^{n} \times H^{m}$ is unstable. For existence of hyperbolic manifolds with small eigenvalues we refer to [14].

\section*{5. Second variations of other quadratic functionals}
5.1. Stability of $\mathcal{F}_{t}$ : In this section, we consider the Riemannian functional $\mathcal{F}_{t}$ and study its stability at the product of two closed Einstein manifolds. First, we describe the second variation of $\mathcal{F}_{t}$ at such critical points.

Lemma 6. Let $\left(M^{n}, g\right)$ (where $n=n_{0}+n_{1}$ ) be the product of closed Einstein manifolds ( $M_{0}^{n_{0}}, g_{0}$ ) and $\left(M_{1}^{n_{1}}, g_{1}\right)\left(n_{0}, n_{1} \geq 3\right)$ with respective Einstein constants $\lambda_{0}$ and $\lambda_{1}$.
\begin{itemize}
\item[(1)] Let $h=\alpha_{0} \odot \alpha_{1}$ as in Lemma 1, one obtains
$$\left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}}=\left\{\begin{array}{l}
\left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}}, \text { if } \lambda_{0}=-\lambda_{1}, \text { and } n_{0}=n_{1} ; \\
\left\|\Delta \alpha_{0}\right\|^{2}+\left\|\Delta \alpha_{1}\right\|^{2}+2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}+4 \lambda^{2}(2+t n) \\
\quad-\lambda(5+2 t n)\left(\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}+\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\right) ; \text { if } \lambda_{0}=\lambda_{1}=\lambda .
\end{array}\right.$$
\item[(2)] For $h=f g_{i}$ as in Lemma 1, one obtains
$$\begin{aligned}
& \left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}} \\
& =\left\{\begin{array}{c}
\frac{m((4 t+1) m+1)}{2}\|\Delta f\|^{2}-\lambda_{i} \frac{m((8 t+1) m+2)}{2}\|d f\|^{2}+\lambda^{2} m(m(2 t-1)+4)\|f\|^{2}, \\
\text { if } \lambda_{0}=-\lambda_{1}=\lambda, n_{0}=n_{1}=m ; \\
\frac{n_{i}\left((4 t+1) n_{i}+1\right)}{2}\|\Delta f\|^{2}+\lambda \frac{n_{i}}{2}\left(2 t\left(n\left(n_{i}-1\right)-4 n_{i}\right)+n_{i}-6\right)\|d f\|^{2} \\
-\lambda^{2} n_{i}\left(t\left(n\left(n_{i}-2\right)-2 n_{i}\right)+n_{i}-4\right)\|f\|^{2}, \text { if } \lambda_{0}=\lambda_{1}=\lambda .
\end{array}\right.
\end{aligned}$$
\end{itemize}

Proof. Let $h=\alpha_{0} \odot \alpha_{1}$ such that $\left\|\alpha_{0}\right\|=1=\left\|\alpha_{1}\right\|$. Using (2.1) we have
$$\begin{aligned}
\left\langle(\nabla \mathcal{S})^{\prime}(h), h\right\rangle_{L^{2}} & =\frac{2 s^{2}}{n}\|h\|^{2}-2 s\left\langle r^{\prime}(h), h\right\rangle_{L^{2}} \\
& =\frac{4\left(n_{0} \lambda_{0}+n_{1} \lambda_{1}\right)^{2}}{n}-2\left(n_{0} \lambda_{0}+n_{1} \lambda_{1}\right)\left(\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}+\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\right) \\
& =\left\{\begin{array}{l}
0, \quad \text { if } \lambda_{1}=-\lambda_{0}, n_{0}=n_{1} ; \\
2 \lambda n\left(2 \lambda-\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}-\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\right), \text { if } \lambda_{0}=\lambda_{1}=\lambda .
\end{array}\right.
\end{aligned}$$
Consequently, using (5.1) and Theorem 5, proof of (1) follows.
Let $h=f g_{i}$. Using similar computations as in Lemma 5 for we have
$$\left\langle s^{\prime}(h) r, h\right\rangle_{L^{2}}=n_{i}^{2} \lambda_{i}\left(\|d f\|^{2}-\lambda_{i}\|f\|^{2}\right),\left\langle s . r^{\prime}(h), h\right\rangle_{L^{2}}=s n_{i}\|d f\|^{2},\left\langle s . s^{\prime}(h) g, h\right\rangle_{L^{2}}=s n_{i}^{2}\left(\|d f\|^{2}-\lambda_{i}\|f\|^{2}\right)$$
which implies that
$$\begin{aligned}
& \left\langle(\nabla \mathcal{S})^{\prime}(h), h\right\rangle_{L^{2}}=\left\langle 2 \Delta\left(s^{\prime}(h)\right) g-2 s^{\prime}(h) r-2 s . r^{\prime}(h)+s . s^{\prime}(h) g, h\right\rangle_{L^{2}}+\frac{2 n_{i} s^{2}}{m+n}\|f\|^{2} \\
& =\left\{\begin{array}{l}
2 m^{2}\left(\|\Delta f\|^{2}-2 \lambda_{i}\|d f\|^{2}+\lambda^{2}\|f\|^{2}\right), \text { if } \lambda_{0}=-\lambda_{1}=\lambda \text { and } n_{0}=n_{1}=m ; \\
2 n_{i}^{2}\|\Delta f\|^{2}+\lambda\left(n n_{i}\left(n_{i}-1\right)-4 n_{i}^{2}\right)\|d f\|^{2}+n_{i} \lambda^{2}\left(2 n_{i}-n\left(n_{i}-2\right)\right)\|f\|^{2}, \\
\text { if } \lambda_{0}=\lambda_{1}=\lambda .
\end{array}\right.
\end{aligned}$$
Now (2) follows from combining (5.2) and Lemma 5. \(\square\)

Note that if $\lambda_{0}=-\lambda_{1}$ then $(M, g)$ is a critical point of $\mathcal{F}_{t}$ for all $0 \neq t \in \mathbb{R}$ if and only if $n_{0}=n_{1}$. The following result analyses the stability of $\mathcal{F}_{t}$ for such critical points.

Theorem 6. Let $\left(M^{2 n}, g\right)$ be a critical point of $\mathcal{F}_{t}$ which is the product of closed Einstein manifolds $\left(M_{0}^{n}, g_{0}\right)$ and $\left(M_{1}^{n}, g_{1}\right)(n \geq 3)$ with respective Einstein constants $\lambda>0$ and $-\lambda$. Let for each $i=0,1$, $\mu_{i}$ denote the first eigenvalue of the Laplacian on $\left(M_{i}, g_{i}\right)$. Then $(M, g)$ is stable for $\mathcal{F}_{t}$ if and only if each $\left(M_{i}, g_{i}\right)$ is stable for the same and one of the following conditions holds:
\begin{itemize}
\item[(1)] . $n=3$, and $t>-\frac{1}{3}$;
\item[(2)] . $4 \leq n \leq 21$ and $\left\{\begin{array}{l}\frac{-\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)}>t>\frac{-(n+1)}{4 n} ; \\ n=4, t \geq \frac{-\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)} \text { with } \frac{\mu_{1}}{\lambda}>\frac{-b_{0}+\sqrt{D}}{2((4 t+1) n+1))} ; \\ n \geq 5,\left\{\begin{array}{l}-\frac{11}{16 n}>t \geq \frac{-\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)} \text { with } \frac{\mu_{[i]}}{\lambda}>\frac{-b_{[i+1]}+\sqrt{D}}{2((4 t+1) n+1))} \\ t \geq-\frac{11}{16 n} \text { with } \frac{\mu_{1}}{\lambda}>\frac{-b_{0}+\sqrt{D}}{2((4 t+1) n+1))}\end{array} ;\right.\end{array}\right.$
\item[(2)] . $n \geq 22$ and $\left\{\begin{array}{l}t \geq-\frac{11}{16 n}, \text { with } \frac{\mu_{1}}{\lambda}>\frac{-b_{0}+\sqrt{D}}{2((4 t+1) n+1))} ; \\ -\frac{11}{16 n}>t>\frac{-(n+1)}{4 n}, \text { with } \frac{\mu_{[i]}}{\lambda}>\frac{-b_{[i+1]}+\sqrt{D}}{2((4 t+1) n+1))} .\end{array}\right.$
\end{itemize}
where $b_{0}=-((8 t+1) n+2)=-b_{1}, D=4 n t(8 n-7)+\left(9 n^{2}-20 n-28\right)$ and $[i]=i \bmod 2$.
Proof. For transverse-traceless variations of $\mathcal{F}_{t}$, observe that for $h=\alpha_{0} \odot \alpha_{1}$ as in Lemma [6], it is immediate combining Lemma 6(1) and Theorem 5, that there is a constant $C>0$ such that
$$\left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}} \geq C\|h\|^{2} .$$
For conformal variations of $\mathcal{F}_{t}$, with $h=f g_{i}$ as in Lemma 6(2), one obtains
$$\left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}}=\frac{n((4 t+1) n+1)}{2}\|\Delta f\|^{2}-\lambda_{i} \frac{n((8 t+1) n+2)}{2}\|d f\|^{2}+n \lambda^{2}(n(2 t-1)+4)\|f\|^{2} .$$
Considering the quadratic polynomial $p_{i}(t, x)=a x^{2}+b_{i} x+c$ with
$$a=(4 t+1) n+1, b_{0}=-((8 t+1) n+2)=-b_{1} \text { and } c=2(2 t-1) n+8,$$
it follows that $\left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}}>0$ if and only if $p_{i}(t, x)>0$ for $x \geq \frac{\mu_{i+1}}{\lambda}(\lambda>0)$. For $t \leq \frac{-(n+1)}{4 n}$, $a \leq 0$, and $p_{0}(t, x) \leq-n x-(3 n-7)<0$ for all $x \geq 0$ (as $n \geq 3$ ). On the other hand, for $t>\frac{-(n+1)}{4 n}$, the discriminant of $p_{i}(t, x)$ given by $D=4 n t(8 n-7)+\left(9 n^{2}-20 n-28\right)<0$ whenever $t<\frac{-\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)}$ (i.e. both $p_{i}(t, x)>0$ as $a>0$ ) which is possible only when $n \leq 21$.

For $t>\frac{-(n+1)}{4 n}, D \geq 0$ if and only if $t \geq \frac{-\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)}$ and $p_{i}(t, x)>0$ if $x>\frac{-b_{i}+\sqrt{D}}{2 a}$. Since $\frac{\mu_{0}}{\lambda}>1$ and $\frac{\mu_{1}}{\lambda} \geq 0$, it follows immediately that the positivity conditions $\frac{\mu_{[i]}}{\lambda}>\frac{-b_{[i+1]}+\sqrt{D}}{2 a}$ are non-trivial only when $\frac{-b_{1}+\sqrt{D}}{2 a}>1$ and $\frac{-b_{0}+\sqrt{D}}{2 a}>0$ respectively. Note that for $n \in \mathbb{N}$,
$$-\frac{\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)} \begin{cases}>-\frac{(n+1)}{4 n}, & \text { if } n \leq 21 ; \\ <-\frac{(n+1)}{4 n}, & \text { otherwise } .\end{cases}$$
Considering all possibilities, one can summarize conditions of positivity of $\left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}}$ as follows.
\begin{itemize}
\item[-] $n=3$, with $t>-\frac{1}{3}$ : Clearly, for $t \geq 0$,
$$\begin{aligned}
& \left.p_{0}(t, x)=\frac{1}{2}\left(\left(4 x^{2}-5 x+2\right)+12 t(x-1)^{2}\right)\right)>0, \text { if } x>1, \text { and } \\
& \left.p_{1}(t, x)=\frac{1}{2}\left(\left(4 x^{2}+5 x+2\right)+12 t(x+1)^{2}\right)\right)>0, \text { if } x \geq 0 .
\end{aligned}$$
Also, for $\left(-\frac{\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)}=\right) \frac{7}{204}>t>-\frac{1}{3}, D<0$ and $p_{i}(t, x)>0$ for each $i=0,1$. Hence in this case, $\left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}}>0$ whenever $t>-\frac{1}{3}$.
\item[-] $n=4$, with $t \geq-\frac{\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)}\left(>-\frac{(n+1)}{4 n}\right)$ and $n \geq 5$, with $t \geq-\frac{11}{16 n}$ :
Since in both the cases, $\frac{-b_{1}+\sqrt{D}}{2 a} \leq 1$ and $\frac{-b_{0}+\sqrt{D}}{2 a}>0$, the only non-trivial condition for positivity is $\frac{\mu_{1}}{\lambda}>\frac{-b_{0}+\sqrt{D}}{2 a}$.
\item[-] $n \geq 5$, together with $-\frac{11}{16 n}>t \geq \max \left\{-\frac{(n+1)}{4 n}+\epsilon,-\frac{\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)}\right\}$ for some $\epsilon>0$ :
In this case, both conditions for positivity are non-trivial (as $\frac{-b_{1}+\sqrt{D}}{2 a}>1$ and $\frac{-b_{0}+\sqrt{D}}{2 a}>0$ ).
\item[-] $n \geq 22$, and $-\frac{11}{16 n}>t>-\frac{(n+1)}{4 n}$ : Here also both the conditions for positivity are non-trivial.
\end{itemize}

Combining all these possibilities above, it follows that $\left\langle\left(\nabla \mathcal{F}_{t}\right)^{\prime}(h), h\right\rangle_{L^{2}}>0$ for $h=f g_{i}$, if and only if one of the conditions in the hypothesis holds. The final consequence is immediate following similar arguments as in Theorem 2. \(\square\)

Remark 1. Combining Theorem 6 with Theorem 1.7 and Theorem 1.9 from [8], it follows that a critical point $\left(M^{6}, g\right)$ which is the product of closed Einstein manifolds $\left(M_{0}^{3}, g_{0}\right)$ and $\left(M_{1}^{3}, g_{1}\right)$ with Einstein constants of opposite signs, is stable for $\mathcal{F}_{t}$ provided $\frac{1}{3}>t>-\frac{1}{3}$. Moreover, a critical point $\left(M^{2 n}, g\right)(n \geq 4)$ as the product of closed Einstein stable manifolds $\left(M_{0}^{n}, g_{0}\right)$ and $\left(M_{1}^{n}, g_{1}\right)$ with Einstein constants of opposite signs, is unstable whenever $t \leq-\frac{(n+1)}{4 n}$ or $n \geq 22$ with $t<-\frac{\left(9 n^{2}-20 n-28\right)}{4 n(8 n-7)}$. On the other hand, a critical point $\left(M^{2 n}, g\right)(n \geq 4)$ as above is stable if both $\left(M_{0}^{n}, g_{0}\right)$ and $\left(M_{1}^{n}, g_{1}\right)$ are stable, $t \geq-\frac{11}{16 n}$ and the first eigen value of the Laplacian of $\left(M_{1}, g_{1}\right)$ (with $\lambda_{1}<0$ ) is sufficiently large.
5.2. Stability of $\mathcal{W}_{2}$. Let $\left(M^{n}, g\right)$ be the product of a spherical space form $\left(M_{0}^{n_{0}}, g_{0}\right)$ and a compact hyperbolic space form $\left(M_{1}^{n_{1}}, g_{1}\right)$. Then $g$ is conformally flat. Hence $g$ is a global minima for $\mathcal{W}_{2}$. Thus it would be interesting to see if $g$ is stable for $\mathcal{W}_{2}$.

Lemma 7. Let $\left(M^{n}, g\right)\left(n=n_{0}+n_{1}\right)$ be the product of two compact space forms $\left(M_{0}^{n_{0}}, g_{0}\right)$ and $\left(M_{1}^{n_{1}}, g_{1}\right)$ such that one of the following conditions holds:
\begin{itemize}
\item[(1)] $n_{0}, n_{1} \geq 3$ with $K_{g_{0}}=1=-K_{g_{1}}$,
\item[(2)] $n_{0} \geq 3, n_{1}=1, K_{g_{0}}= \pm 1$,
\end{itemize}
(where $K_{g}$ denotes the sectional curvature of $g$ ). Then there exists $C>0$ such that for any $T T$-tensor $h$ on $M$,
$$\left\langle\left(\nabla \mathcal{W}_{2}\right)^{\prime}(h), h\right\rangle_{L^{2}} \geq C\|h\|^{2} .$$
Proof. Following Theorem 5 it suffices to assume that $h=\alpha_{0} \odot \alpha_{1}$ as above.
Equation 3.2 implies that
$$\left\langle\left(\nabla \mathcal{W}_{2}\right)^{\prime}(h), h\right\rangle_{L^{2}}=\left\langle\nabla \mathcal{R}^{\prime}(h)-\frac{4}{n-2}\left\{(\nabla \mathcal{R} i c)^{\prime}(h)-\frac{1}{2(n-1)}(\nabla \mathcal{S})^{\prime}(h)\right\}, h\right\rangle_{L^{2}} .$$
Putting $\lambda_{0}=n_{0}-1$ and $\lambda_{1}=-\left(n_{1}-1\right)$ in Lemmas 1, 2 and 3, one has
$$\begin{aligned}
& \left\langle(\nabla \mathcal{R} i c)^{\prime}(h), h\right\rangle_{L^{2}}=\left\|\Delta \alpha_{0}\right\|^{2}+\left\|\Delta \alpha_{1}\right\|^{2}+2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle-4\left(n_{0}-1\right)\left(n_{1}-1\right) \\
& +\frac{4}{n}\left(\left(n_{0}\left(n_{0}-1\right)^{2}+n_{1}\left(n_{1}-1\right)^{2}\right)\right)-\left(3 n_{0}-2 n_{1}-1\right)\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle-\left(3 n_{0}-2 n_{1}+1\right)\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle .
\end{aligned}$$

Next, using (5.1), it follows that
$$\left\langle(\nabla \mathcal{S})^{\prime}(h), h\right\rangle_{L^{2}}=\frac{4}{n}\left(n_{0}-n_{1}\right)^{2}(n-1)^{2}-2\left(n_{0}-n_{1}\right)(n-1)\left(\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}+\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\right)$$

Using Lemmas 1 and 4, one has
$$\begin{aligned}
& \left\langle(\nabla \mathcal{R})^{\prime}(h), h\right\rangle_{L^{2}}=4\left(\left\|\Delta \alpha_{0}\right\|^{2}+\left\|\Delta \alpha_{1}\right\|^{2}+2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\right)-8\left(n_{0}-1\right)\left(n_{1}-1\right)+8(n-2) \\
& +\left(5\left(n_{1}-n_{0}\right)-4\right)\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}+\left(5\left(n_{1}-n_{0}\right)+4\right)\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}+\frac{8}{n}\left(n_{0}\left(n_{0}-1\right)+n_{1}\left(n_{1}-1\right)\right)
\end{aligned}$$

Combining above equations, one obtains
$$\begin{aligned}
& \left\langle\left(\nabla \mathcal{W}_{2}\right)^{\prime}(h), h\right\rangle_{L^{2}}=\left(\frac{4(n-3)}{n-2}\right)\left(\left\|\Delta \alpha_{0}\right\|^{2}+\left\|\Delta \alpha_{1}\right\|^{2}+2\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}\right) \\
& +\left(5\left(n_{0}-n_{1}\right)+\frac{4\left(n_{0}-2 n_{1}+1\right)}{n-2}\right)\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}}+\left(5\left(n_{1}-n_{0}\right)+\frac{4\left(2 n_{0}-n_{1}-1\right)}{n-2}\right)\left\langle\Delta \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}} \\
& +\frac{8\left(n_{1}-n_{0}\right)^{2}(n-1)}{n(n-2)}+8(n-2)+\frac{8\left(n_{0}\left(n_{0}-1\right)+n_{1}\left(n_{1}-1\right)\right)}{n} \\
& -\frac{8\left(n_{1}-1\right)\left(n_{0}-1\right)(n-4)}{n-2}-\frac{16\left(n_{0}\left(n_{0}-1\right)^{2}+n_{1}\left(n_{1}-1\right)^{2}\right)}{n(n-2)}
\end{aligned}$$

Setting $n_{1}=1$, it is easy to see from the above inequality that
$$\left\langle\left(\nabla \mathcal{W}_{2}\right)^{\prime}(h), h\right\rangle_{L^{2}}>0 .$$

When both $n_{i} \geq 3$, using similar arguments as in Lemma 1, it follows that $\left\langle\Delta \alpha_{0}, \alpha_{0}\right\rangle_{L^{2}} \geq 2\left(n_{0}-1\right)$, $\left\|\Delta \alpha_{0}\right\|^{2} \geq 4\left(n_{0}-1\right)^{2}$ and the above equation reduces to
$$\begin{aligned}
& \left\langle\left(\nabla \mathcal{W}_{2}\right)^{\prime}(h), h\right\rangle_{L^{2}} \geq \frac{16(n-3)\left(n_{0}-1\right)^{2}}{n-2}+10\left(n_{1}-n_{0}\right)\left(n_{0}-1\right)+\frac{8\left(n_{0}-2 n_{1}+1\right)\left(n_{0}-1\right)}{n-2} \\
& -\frac{8\left(n_{0}-1\right)\left(n_{1}-1\right)(n-4)}{n-2}+\left(\frac{16(n-3)\left(n_{0}-1\right)}{n-2}+5\left(n_{1}-n_{0}\right)+\frac{4\left(2 n_{0}-n_{1}-1\right)}{n-2}\right)\left\langle\Delta_{H} \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}} \\
& +\frac{8\left(n_{1}-n_{0}\right)^{2}(n-1)}{n(n-2)}+8(n-2)+\frac{8\left(n_{0}\left(n_{0}-1\right)+n_{1}\left(n_{1}-1\right)\right)}{n}-\frac{16\left(n_{0}\left(n_{0}-1\right)^{2}+n_{1}\left(n_{1}-1\right)^{2}\right)}{n(n-2)}
\end{aligned}$$
Consequently, it follows that
$$\begin{aligned}
& \left\langle\left(\nabla \mathcal{W}_{2}\right)^{\prime}(h), h\right\rangle_{L^{2}}>\frac{(6 n-20)\left(n_{0}-1\right)^{2}}{n-2}+2\left(n_{1}-1\right)\left(n_{0}-1\right) \\
& +\frac{1}{n-2}\left(n_{0}\left(11 n_{0}-6\right)+16\left(n_{0}-1\right)\left(n_{1}-3\right)+n_{1}\left(5 n_{1}-14\right)\right)\left\langle\Delta_{H} \alpha_{1}, \alpha_{1}\right\rangle_{L^{2}}>0 .
\end{aligned}$$ \(\square\)

This leads to the following result.
Theorem 7. Let $(M, g)$ be the product of two closed non-Euclidean space forms whose sectional curvatures have absolute value 1. Then $(M, g)$ is a stable critical point of the Riemannian functional $\mathcal{W}_{\frac{n}{2}}$ defined by
$$\mathcal{W}_{\frac{n}{2}}(g)=\int_{M}\left|W_{g}\right|^{\frac{n}{2}} d v_{g} .$$
Proof. Since $\mathcal{W}_{\frac{n}{2}}$ is invariant under conformal deformations, we only need to check the positivity of $\left\langle\left(\nabla \mathcal{W}_{\frac{n}{2}}\right)^{\prime}(h), h\right\rangle_{L^{2}}$ for all TT-tensors $h$. Also, it follows that (see Lemma 4 in [13], for a proof) at a critical point $g$ of both $\mathcal{W}$ and $\mathcal{W}_{\frac{n}{2}}$,
$$\left\langle\left(\nabla \mathcal{W}_{\frac{n}{2}}\right)^{\prime}(h), h\right\rangle_{L^{2}}=\|W\|^{\frac{n-4}{2}}\left\langle\left(\nabla \mathcal{W}_{2}\right)^{\prime}(h), h\right\rangle_{L^{2}}, \text { forall } h \in \operatorname{tr}^{-1}(0) \cap \delta_{g}^{-1}(0) .$$
Since conformally flat metrics are global minima for both $\mathcal{W}_{2}$ and $\mathcal{W}_{\frac{n}{2}}$ the result follows from Lemma \(\square\)

\subsection*{5.3. Stability of $\mathcal{R}$.}

Corollary 1. Let $\left(M^{2 n}, g\right)(n \geq 3)$ be the product of a spherical space form $\left(M_{0}^{n}, g_{0}\right)$ and a compact hyperbolic space form $\left(M_{1}^{n}, g_{1}\right)$. Then there exists a constant $C>0$ such that for any $T T$-tensor $h$ on $M$,
$$\left\langle(\nabla \mathcal{R})^{\prime}(h), h\right\rangle_{L^{2}} \geq C\|h\|^{2}$$
Proof. Since on $\left(M^{2 n}, g\right)$, one can write (following (3.1))
$$\mathcal{R}=\mathcal{W}_{2}+\frac{2}{n-1} \mathcal{F} \frac{-1}{2(2 n-1)},$$
the result is immediate from Theorem 6 and Lemma 7. \(\square\)

Corollary 2. Let $\left(M^{2 n}, g\right)$ be as in Corollary 1 and let $h=f g_{i}$ as in Lemma 4. Then
$$\left\langle(\nabla \mathcal{R})^{\prime}(h), h\right\rangle>0 \text { if and only if }\left\{\begin{array}{l}
n \leq 4, \\
n \geq 5 \text { and } \mu_{i}>\sqrt{(n-1)(n-4)} .
\end{array}\right.$$
where $\mu_{i}$ is the first eigenvalue of the Laplacian of $\left(M_{i}, g_{i}\right)$ for $i=0,1$.
Proof. It follows from a combination of Lemmas 1 and 4 that
$$\begin{aligned}
\left\langle(\nabla \mathcal{R})^{\prime}(h), h\right\rangle_{L^{2}} & =2\left\langle\left(\delta^{D} d^{D} r\right)^{\prime}\left(f g_{i}\right)-\left\langle(\check{R})^{\prime}\left(f g_{i}\right), \frac{1}{2}\left(|R|^{2}\right)^{\prime}\left(f g_{i}\right), f g_{i}\right\rangle_{L^{2}}+4 n(n-1)\|f\|^{2}\right. \\
& =2 n\|\Delta f\|^{2}-2 n(n-1)(n-4)\|f\|^{2}
\end{aligned}$$
Now, one observes that
$$\left\langle(\nabla \mathcal{R})^{\prime}(h), h\right\rangle_{L^{2}}>0 \text { if and only if } \mu_{i}^{2}-(n-1)(n-4)>0$$
and the estimate follows. \(\square\)

Consequently we have the following theorem using [4] and Corollaries 1, 2 above.
Theorem 8. Let $(M, g)$ be the product of $S^{n}$ and a compact hyperbolic manifold $H^{n}$. Then $(M, g)$ is stable for $\mathcal{R}$ if and only if one of the following conditions holds.
$$\text { (i) } n \in\{3,4\} \quad \text { (ii) } n \geq 5 \text { and } \mu>\sqrt{(n-1)(n-4)} \text {. }$$
where $\mu$ is the first eigenvalue of the Laplacian of $H^{n}$.
Recently, stability of rank 1 symmetric spaces as critical points of $\mathcal{R}$ and $\mathcal{W}_{\frac{n}{2}}$ has been established in [13]. The behaviour of irreducible symmetric spaces of higher rank as critical metrics of $\mathcal{R}$ is not completely understood, but some unstable critical points of the functional $\mathcal{R}_{\frac{n}{2}}$ have been pointed out in [4]. The above theorem implies that if the first eigenvalue of the laplacian of a hyperbolic manifold $H^{n}$ is sufficiently small and $n>5$ then its product with $S^{n}$ is unstable for $\mathcal{R}$.

\section*{References}
[1] A. L. Besse, Einstein manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete (3)[Results in Mathematics and Related Areas (3)] 10, Springer-Verlag, Berlin, (1987).
[2] G. Besson, G. Courtois and S. Gallot, Volume et entropie minimale des espaces localement symétriques, Invent. Math., Vol. 103 (1991), 417-445.
[3] M. Berger, Quelques formules de variation pour une structure riemannienne, Ann. Sci. Ecole Norm. Sup. $4^{e}$ série, Vol 3 (1970), 285-294.
[4] A. Bhattacharya, S. Maity, Some unstable critical metrics for the $L^{\frac{n}{2}}$-norm of the curvature tensor. Math. Res. Lett., Vol. 21 (2014), 235-240.
[5] Q. Chen, C. He, On Bach flat warped product Einstein manifolds, Pacific J. Math., Vol. 265 (2013), 313-326.
[6] X. Guo, H. Li, The stability of Fubini-Study metric on $\mathbb{C P}^{n}$, Proc. Amer. Math. Soc., Vol. 146 (2018), 325-333.
\begin{itemize}
\item[] [7] —, — and G. Wei, On variational formulas of a conformally invariant functional, Results Math., Vol. 67 (2015), 49-70.
\item[] [8] M. J. Gursky, J. A. Viaclovsky, Rigidity and stability of Einstein metrics for quadratic curvature functionals, J. Reine Angew. Math., Vol. 700 (2015), 37-91.
\item[] [9] O. Kobayashi, On a conformally invariant functional of the space of Riemannian metrics, J. Math. Soc. Japan, Vol. 37 (1985), 373-389.
\item[] [10] N. Koiso, Nondeformability of Einstein metrics, Osaka J. Math., Vol. 15 (1978), 419-433.
\item[] [11] -, Rigidity and infinitesimal deformability of Einstein metrics, Osaka J. Math., Vol. 19 (1982), 643-668.
\item[] [12] 一, Rigidity and stability of Einstein metrics-the case of compact symmetric spaces. Osaka J. Math., Vol. 17 (1980), 51-73.
\item[] [13] S. Maity, On the stability of $L^{p}$-norms of curvature tensor at rank one symmetrics spaces, preprint, arXiv:1408.1989v3 [math.DG]
\item[] [14] R. Schoen, A lower bound for the first eigenvalue of a negatively curved manifold, J. Differential Geometry, Vol. 17 (1982), 232-238.
\item[] [15] R. Schoen, S. T. Yau, Conformally flat manifolds, Kleinian groups and scalar curvature, Invent. Math., Vol. 92 (1988), 47-71.
\item[] [16] S. Zhu, The classification of complete locally conformally flat manifolds of nonnegative ricci curvature, Pacific J. Math., Vol. 163 (1994), 189-199.
\end{itemize}

Indian Institute of Science Education and Research, Bhopal, India
E-mail address: atreyee@iiserb.ac.in
Indian Institute of Science Education and Research, Mohali, India
E-mail address: soma123maity@gmail.com