---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1505_04728.pdf
converter: mathpix
format: mmd
---

\title{
COLLAPSING OF NEGATIVE KÄHLER-EINSTEIN METRICS
}

\author{
YUGUANG ZHANG
}

\begin{abstract}
In this paper, we study the collapsing behaviour of negative Kähler-Einstein metrics along degenerations of canonical polarized manifolds. We prove that for a toroidal degeneration of canonical polarized manifolds with the total space $\mathbb{Q}$-factorial, the Kähler-Einstein metrics on fibers collapse to a lower dimensional complete Riemannian manifold in the pointed Gromov-Hausdorff sense by suitably choosing the base points. Furthermore, the most collapsed limit is a real affine Kähler manifold.
\end{abstract}

\section*{1. Introduction}

Let $X$ be a complex projective $n$-manifold. We call $X$ a canonical polarized manifold if the canonical bundle $\mathcal{K}_{X}$ of $X$ is ample, and call $X$ a Calabi-Yau manifold if $\mathcal{K}_{X}$ is trivial. The Calabi conjecture of the existence of Kähler-Einstein metrics was solved by Aubin and Yau in the case of canonical polarized manifolds (cf. [1, 40]), and by Yau for Calabi-Yau manifolds (cf. [40]). More precisely, on a canonical polarized manifold $X$, there exists a unique Kähler-Einstein metric $\omega$ with $\omega \in 2 \pi c_{1}\left(\mathcal{K}_{X}\right)$ and negative Ricci curvature, i.e.
$$\operatorname{Ric}(\omega)=-\omega,$$
by [1, 40]. On a Calabi-Yau manifold, there are Ricci-flat Kähler-Einstein metrics by [40]. The goal of this paper is to study the collapsing behaviour of families of negative Kähler-Einstein metrics along degenerations in algebrogeometric sense.

A degeneration of projective $n$-manifolds $\pi: \mathcal{X} \rightarrow \Delta$ is a flat morphism from a normal Gorenstein variety $\mathcal{X}$ of dimension $n+1$ to a disc $\Delta \subset \mathbb{C}$ such that $X_{t}=\pi^{-1}(t), t \in \Delta^{*}=\Delta \backslash\{0\}$, is smooth except the central fiber $X_{0}=\pi^{-1}(0)$. We denote $X_{0}=\bigcup_{i=1}^{l} X_{0, i}$ and $X_{0, I}=\bigcap_{i \in I} X_{0, i}$, where $X_{0, i}$, $i=1, \cdots, l$, is a irreducible component, and $I \subset\{1, \cdots, l\}$. If the relative canonical bundle $\mathcal{K}_{\mathcal{X} / \Delta}=\mathcal{K}_{\mathcal{X}} \otimes \mathcal{K}_{\Delta}^{-1}$ is relatively ample, then for any smooth fiber $X_{t}$, the canonical bundle $\left.\mathcal{K}_{X_{t}} \cong \mathcal{K}_{\mathcal{X} / \Delta}\right|_{X_{t}}$ is ample, and thus $X_{t}$ is a canonical polarized manifold. We call such degeneration $\pi: \mathcal{X} \rightarrow \Delta$ a canonical polarized degeneration.

\footnotetext{
The author is supported in part by grant NSFC-11271015.
}

In [35], Strominger, Yau and Zaslow proposed a conjecture, so called SYZ conjecture, for constructing mirror Calabi-Yau manifolds via dual special lagrangian fibration. Later, a new version of the SYZ conjecture was proposed by Kontsevich, Soibelman, Gross and Wilson (cf. [17, 25, 26]) by using the collapsing of Ricci-flat Kähler-Einstein metrics. Let $\mathcal{X} \rightarrow \Delta$ be a degeneration of Calabi-Yau $n$-manifolds, i.e. the relative canonical bundle $\mathcal{K}_{\mathcal{X} / \Delta}$ is trivial, and $0 \in \Delta$ be a large complex limit point (cf. [14]). The collapsing version of SYZ conjecture asserts that there are Ricci-flat Kähler-Einstein metrics $\omega_{t}$ on $X_{t}$ for $t \in \Delta^{*}$ such that $\left(X_{t}, \operatorname{diam}_{\omega_{t}}^{-2}\left(X_{t}\right) \omega_{t}\right)$ converges to a compact metric space $\left(B, d_{B}\right)$ in the Gromov-Hausdorff sense, when $t \rightarrow 0$. Furthermore, the smooth locus $B_{0}$ of $B$ is open dense, and is of real dimension $n$, and admits a real affine structure. The metric $d_{B}$ is induced by a Monge-Ampère metric $g_{B}$ on $B_{0}$, i.e. under affine coordinates $x_{1}, \cdots, x_{n}$, there is a potential function $\phi$ such that
$$g_{B}=\sum_{i j} \frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}} d x_{i} d x_{j}, \quad \text { and } \quad \operatorname{det}\left(\frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}\right)=1 .$$
Clearly it is true for Abelian varieties. This conjecture was verified by Gross and Wilson for fibred K3 surfaces with only type $I_{1}$ singular fibers in [17], and was studied for higher dimensional HyperKähler manifolds in [15, 16]. In [16], Gross-Wilson's result was extended to all elliptically fibred K3 surfaces.

Inspired by this collapsing version of SYZ conjecture, we study the limits of negative Kähler-Einstein metrics on canonical polarized manifolds degenerating to some singular varieties.

Let $\pi: \mathcal{X} \rightarrow \Delta$ be a canonical polarized degeneration such that $X_{0}$ has only simple normal crossing singularities, i.e. $X_{0}$ is reduced, locally given by $z_{1} \cdots \cdot z_{k}=0$ under local coordinates $z_{1}, \cdots, z_{n}$ on $\mathcal{X}$, and any $X_{0, I}$ is smooth. Let $\omega_{t} \in 2 \pi c_{1}\left(\mathcal{K}_{X_{t}}\right), t \in \Delta^{*}$, be the unique Kähler-Einstein metric on $X_{t}$. The convergence of $\omega_{t}$ was studied by various authors (cf. [36, 19, 29, 30, 32]). In 36], it is proved that $\omega_{t}$ converges smoothly to a complete Kähler-Einstein $\omega_{0}$ with negative Ricci curvature on the regular locus $X_{0, \text { reg }}=\bigcup_{i=1}^{l} X_{0, i, \text { reg }}$ in the Cheeger-Gromov sense, if an additional condition that any three of the components $X_{0, i}$ have empty intersection is satisfied. More precisely, for any smooth family of embeddings $F_{t}: X_{0, \text { reg }} \rightarrow$ $X_{t}$, we have that
$$F_{t}^{*} \omega_{t} \rightarrow \omega_{0}, \quad \text { when } t \rightarrow 0,$$
in the locally $C^{\infty}$-sense on $X_{0, \text { reg }}$, where $\omega_{0}$ is the complete Kähler-Einstein metric on $X_{0, \text { reg }}$ previously obtained in [37, 22, 5]. In [29, 19], the additional assumption is removed, and furthermore, the result is generalized to the case of toroidal degenerations in [30]. These theorems describe the the noncollapsing part of the limit of $\left(X_{t}, \omega_{t}\right)$.

Since the volume of $\omega_{0}$ is finite, there must be some collapsing part when $\left(X_{t}, \omega_{t}\right)$ approaches to the limit, i.e. there are points $p_{t} \in X_{t}$ such that the
volumes of metric 1-balls satisfy
$$\operatorname{Vol}_{\omega_{t}}\left(B_{\omega_{t}}\left(p_{t}, 1\right)\right) \rightarrow 0, \quad \text { when } t \rightarrow 0 .$$
Now by Gromov's precompactness theorem (cf. [12]), a sequence of $\left(X_{t}, \omega_{t}, p_{t}\right)$ converges to a pointed complete metric space $\left(W, d_{W}, p_{\infty}\right)$ of Hausdorff dimension less than $2 n$ in the pointed Gromov-Hausdorff sense, i.e. for any $R>0$, the metric $R$-ball $\left(B_{\omega_{t}}\left(p_{t}, R\right), \omega_{t}\right)$ converges to the metric $R$-ball $\left(B_{d_{W}}\left(p_{\infty}, R\right), d_{W}\right)$ in the Gromov-Hausdorff sense (cf. [8]).

The following theorem is a special case of the main theorem (Theorem 2.4) of the present paper, where a more general hypothesis is assumed.

Theorem 1.1. Let $\pi: \mathcal{X} \rightarrow \Delta$ be a canonical polarized degeneration such that $X_{0}$ has only simple normal crossing singularities, and $\omega_{t} \in 2 \pi c_{1}\left(\mathcal{K}_{X_{t}}\right)$ be the unique Kähler-Einstein metric on $X_{t}, t \in \Delta^{*}$. For any $X_{0, I}$ and any point $p_{0} \in X_{0, I} \backslash \bigcup_{i \notin I} X_{0, i}$, there are points $p_{t} \in X_{t}$ such that $p_{t} \rightarrow p_{0}$ in $\mathcal{X}$ when $t \rightarrow 0$, and by passing to a sequence, $\left(X_{t}, \omega_{t}, p_{t}\right)$ converges to a complete Riemannian manifold ( $W, g_{W}, p_{\infty}$ ) with $\operatorname{dim}_{\mathbb{R}} W=2 n+1-\sharp I$ in the pointed Gromov-Hausdorff sense. Furthermore, if $\operatorname{dim}_{\mathbb{C}} X_{0, I}=0$, then $\left(W, g_{W}\right)$ is isometric to $\left(B, g_{B}\right)$ by suitably choosing $p_{t}$, where $B$ is the interior of the standard simplex in $\mathbb{R}^{n}$, and there is a smooth potential function $\phi$ on $B$ such that $\left.\phi\right|_{\partial \bar{B}}=+\infty$,
$$g_{B}=\sum_{i j=1}^{n} \frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}} d x_{i} d x_{j}, \text { and } \operatorname{det}\left(\frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}\right)=\kappa e^{2 \phi},$$
for a constant $\kappa>0$.
Actually $\left(X_{t}, \omega_{t}\right)$ collapses smoothly in a certain sense, which is stronger than the Gromov-Hausdorff topology (See Theorem 2.4 for details).

This theorem shows a similar collapsing behaviour to the SYZ conjecture for Calabi-Yau manifolds, i.e. under certain assumptions, the limit metric space $W$ is an affine Kähler manifold of real dimension $n$, and the potential function satisfies a real Monge-Ampère equation. However, unlike the Calabi-Yau case, we always have the non-collapsing part of the limit, and we do not rescale the metric to obtain the collapsing limit. Note that for algebraic curves of higher genus, the rescaled limit exists, and is a compact metric graph by [28]. However, we do not expect that still holds in the higher dimensional case.

In the original SYZ conjecture (cf. [35]), the existence of special lagrangian submanifolds is expected when Calabi-Yau manifolds are near the large complex limit. As an application, we will construct some generalized special lagrangian submanifolds on canonical polarized manifolds (See Section 2.3 for details).

The understanding of the limit behaviour of negative Kähler-Einstein metrics is also required for other program. The moduli space $\mathcal{M}$ of canonical polarized manifolds with a fixed Hilbert polynomial was proven to be
a quasi-projective manifold by Viehweg in [39], and the recent progress on the moduli space of stable varieties (cf. [23]) gives a natural algebro geometric compactification $\overline{\mathcal{M}}$ of $\mathcal{M}$. Meanwhile, the existence of singular Kähler-Einstein metrics on stable varieties was obtained in [2]. A natural question is to understand such compactification from the differential geometric viewpoint (cf. [2, 34]), for example in the Gromov-Hausdorff sense or the Weil-Petersson geometry sense. However unlike the case of CalabiYau manifolds (cf. [41, 38]), we would not have the coincidence of the Gromov-Hausdorff non-collapsing convergence and the finite Weil-Petersson distance. In Theorem 1.1, $\left(X_{t}, \omega_{t}\right)$ diverges in the Gromov-Hausdorff sense, but the Weil-Petersson metric on $\Delta^{*}$ is not complete, i.e. \{0\} has finite Weil-Petersson distance to the interior by [36, 29, 30].

This paper is organized as the followings. In Section 2, we introduce the preliminary materiel and state the main theorems (Theorem 2.4 and Theorem 2.6) of this paper. In Section 1.1, we construct some semi-flat KählerEinstein metrics from those affine Kähler metrics obtained by Cheng and Yau previously. In Section 1.2 and Section 1.3, the main theorems (Theorem 2.4 and Theorem 2.6) are given. Theorem 2.4 study the metric collapsing along toroidal degenerations, and Theorem 2.6 shows the existence of generalized special lagrangian submanifolds. Section 3 is devoted to prove Theorem 2.4. Firstly, we construct the approximation background metrics in Section 3.1, then we do some local calculations and prove Theorem 2.4 in Section 3.2. The last section proves Theorem 2.6.
Acknowledgements: The author would like to thank Prof. Shiu-Yuen Cheng for answering a question.

\section*{2. Main Theorems}

In this paper, we always denote $N \cong \mathbb{Z}^{n+1}, N_{\mathbb{R}}=N \otimes_{\mathbb{Z}} \mathbb{R}, T_{N}=N \otimes_{\mathbb{Z}} \mathbb{C}^{*}$, $M=\operatorname{hom}_{\mathbb{Z}}(N, \mathbb{Z})$ and $M_{\mathbb{R}}=M \otimes_{\mathbb{Z}} \mathbb{R}$.
2.1. Semi-flat Kähler-Einstein metric. In this section, we recall a theorem due to Cheng and Yau for the existence of affine Kähler metrics, which induce some semi-flat Kähler-Einstein metrics that appear in the main theorem.

Let $\sigma$ be a rational strongly convex polyhedral cone in $N_{\mathbb{R}}$, and $\check{\sigma} \subset M_{\mathbb{R}}$ be the dual cone. If $u_{\sigma} \in M \cap \check{\sigma}$ satisfies $\left\langle u_{\sigma}, v\right\rangle=1$ for the primitive lattice vector $v \in \tau \cap N$ of any 1-dimensional face $\tau$ of $\sigma$, then we define
$$\Lambda_{\mathbb{R}}=\left\{v \in N_{\mathbb{R}} \mid\left\langle v, u_{\sigma}\right\rangle=1\right\}, \quad B_{\sigma}=\Lambda_{\mathbb{R}} \cap \operatorname{Int}(\sigma), \quad \text { and } \quad \Lambda=N \cap \Lambda_{\mathbb{R}}$$
where $\operatorname{Int}(\sigma)$ denotes the interior of $\sigma$. The closure $\bar{B}_{\sigma}$ of $B_{\sigma}$ is a rational convex polytope in $\Lambda_{\mathbb{R}}$.

Let $\mathcal{Y}_{\sigma}$ be the affine toric variety associated to $\sigma$, i.e. $\mathcal{Y}_{\sigma}=\operatorname{Spec}(\mathbb{C}[\check{\sigma} \cap M])$, and $t=\mathcal{Z}^{u_{\sigma}}: \mathcal{Y}_{\sigma} \rightarrow \mathbb{C}$. We have a family of varieties $Y_{\sigma, t}=\operatorname{div}\left(\mathcal{Z}^{u_{\sigma}}-t\right)$
degenerating to the toric boundary $Y_{0}$, i.e. $Y_{0}=\bigcup_{i=1}^{d} D_{i}$ where $D_{i}$ is a primitive toric Weil divisor.

If $e_{0}, \cdots, e_{n} \in N$ is a basis, we denote $x_{0}, \cdots, x_{n}$ the respecting coordinates on $N_{\mathbb{R}}$, and denote $z_{j}=\mathcal{Z}^{e_{j}^{*}}, j=0, \cdots, n$. If $u_{\sigma}=\sum_{j=0}^{n} m_{j} e_{j}^{*}$, then $Y_{\sigma, t}$ is given by $z_{0}^{m_{0}} \cdots \cdots z_{n}^{m_{n}}=t$, and $\Lambda_{\mathbb{R}}$ is given by $m_{0} x_{0}+\cdots+m_{n} x_{n}=1$. Without loss of generality, we assume that $x_{1}, \cdots, x_{n}$ are coordinates on $\Lambda_{\mathbb{R}}$, i.e. $m_{0} \neq 0$, which give an integral affine structure on $B_{\sigma}$.

For any $t \in \Delta^{*}$, the logarithmic map is
$$\log _{t}: T_{N} \rightarrow N_{\mathbb{R}}, \quad \text { by } \quad z_{j} \mapsto x_{j}=\frac{\log \left|z_{j}\right|}{\log |t|}, j=0, \cdots, n .$$
It is clear that $\log _{t}\left(Y_{\sigma, t}\right)=\Lambda_{\mathbb{R}}$. We denote
$$\mathcal{U}=\left\{p \in \mathcal{Y}_{\sigma} \| \mathcal{Z}^{u_{k}}(p) \mid<1, k=1, \cdots, d^{\prime}\right\},$$
which is an open subset of $\mathcal{Y}_{\sigma}$, where $u_{k} \in M \cap \check{\sigma}$ such that $\sigma=\{v \in$ $\left.N_{\mathbb{R}} \mid\left\langle v, u_{k}\right\rangle \geqslant 0, k=1, \cdots, d^{\prime}\right\}$. We have $\log _{t}(\mathcal{U})=\operatorname{Int}(\sigma)$, and moreover, $\log _{t}\left(Y_{\sigma, t} \cap \mathcal{U}\right)=B_{\sigma}$.

We define coordinates $\theta_{1}, \cdots, \theta_{n}$ on $\Lambda_{\mathbb{R}}$ by $\theta_{j}=d x_{j}, j=1, \cdots, n$, under the identification of the tangent bundle $T B_{\sigma} \cong B_{\sigma} \times \Lambda_{\mathbb{R}}$. Then there is a natural complex structure on $B_{\sigma} \times \sqrt{-1} \Lambda_{\mathbb{R}}$ given by complex coordinates $w_{j}=x_{j}+\sqrt{-1} \theta_{j}, j=1, \cdots, n$, which induces a complex structure on $Y_{t, m_{0}}\left(B_{\sigma}\right)=B_{\sigma} \times \sqrt{-1}\left(\Lambda_{\mathbb{R}} / \frac{2 \pi m_{0} \Lambda}{\log |t|}\right)$ for any $t \in \Delta^{*}$. We define a finite covering map $q_{\sigma}: Y_{t, m_{0}}\left(B_{\sigma}\right) \rightarrow Y_{\sigma, t} \cap \mathcal{U}$ by setting $z_{j}=\exp \left((\log |t|) w_{j}\right)$, $j=1, \cdots, n$, and
$$z_{0}=\exp \left(\frac{1}{m_{0}} \log |t|+\sqrt{-1} \frac{\arg (t)}{m_{0}}-\sum_{j=1}^{n} \frac{m_{j}}{m_{0}}(\log |t|) w_{j}\right) .$$
Furthermore, $f_{t}=\left.\log _{t}\right|_{Y_{\sigma, t} \cap \mathcal{U}}: Y_{\sigma, t} \cap \mathcal{U} \rightarrow B_{\sigma}$ is a fibration such that $f_{t} \circ q_{\sigma}$ is the projection from $Y_{t, m_{0}}\left(B_{\sigma}\right)$ to $B_{\sigma}$.

Now we recall a theorem for the existence of affine Kähler metrics in [7].
Theorem 2.1 (Theorem 4.4 in [7]). For any constant $\kappa>0$, there is a smooth convex solution $\phi$ of the real Monge-Ampère equation
$$\operatorname{det}\left(\frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}\right)=\kappa e^{2 \phi},\left.\quad \phi\right|_{\partial \bar{B}_{\sigma}}=+\infty,$$
and
$$g_{B_{\sigma}}=\sum_{i j=1}^{n} \frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}} d x_{i} d x_{j}$$
is a complete affine Kähler metric on $B_{\sigma}$.
Note that the constant $\kappa$ is chosen to be 1 in [7], and however, we can obtain the general case by rescaling the coordinates. By pulling back $\phi$, we
regard $\phi$ as a function on $B_{\sigma} \times \sqrt{-1} \Lambda_{\mathbb{R}}$, i.e. $\phi\left(w_{1}, \cdots, w_{n}\right)=\phi\left(x_{1}, \cdots, x_{n}\right)$, which defines a complete Kähler metric
$$\omega^{s f}=2 \sqrt{-1} \partial \bar{\partial} \phi=\frac{\sqrt{-1}}{2} \sum_{i j=1}^{n} \frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}} d w_{i} \wedge d \bar{w}_{j}$$
on $B_{\sigma} \times \sqrt{-1} \Lambda_{\mathbb{R}}$. By (2.1), $\phi$ satisfies the complex Monge-Ampère equation $\operatorname{det}\left(\frac{\partial^{2} \phi}{\partial w_{i} \partial \bar{w}_{j}}\right)=4^{n} \kappa e^{2 \phi}$ on $B_{\sigma} \times \sqrt{-1} \Lambda_{\mathbb{R}}$, and hence $\omega^{s f}$ is a Kähler-Einstein metric with Ricci curvature -1, i.e.
$$\operatorname{Ric}\left(\omega^{s f}\right)=-\sqrt{-1} \partial \bar{\partial} \log \operatorname{det}\left(\frac{\partial^{2} \phi}{\partial w_{i} \partial \bar{w}_{j}}\right)=-\omega^{s f} .$$
Now Proposition 5.5 in [6] implies that $\phi$ is the unique solution of (2.1) (See also [18]).

Since both $\phi$ and $\omega^{s f}$ are invariant under the translation $w_{j} \mapsto w_{j}+$ $\sqrt{-1} \lambda$ for any $\lambda \in \mathbb{R}^{1}, \omega^{s f}$ descents to a complete Kähler-Einstein metric on $Y_{t, m_{0}}\left(B_{\sigma}\right)$ first, for any $t \in \Delta^{*}$, and further to a complete Kähler-Einstein metric on $Y_{\sigma, t} \cap \mathcal{U}$ denoted by $\omega_{t}^{s f}$. Note that the corresponding Riemannian metric of $\omega^{s f}$ is
$$g^{s f}=\sum_{i j=1}^{n} \frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}\left(d x_{i} d x_{j}+d \theta_{i} d \theta_{j}\right) .$$
The first consequence is that the restriction of $\omega_{t}^{s f}$ on any fiber $f_{t}^{-1}(x)$, $x \in B_{\sigma}$, is flat, so called a semi-flat Kähler-Einstein metric. The second one is that the diameter of the fiber
$$\operatorname{diam}_{\omega_{t}^{s f}}\left(f_{t}^{-1}(x)\right) \sim-(\log |t|)^{-1} \rightarrow 0,$$
and by suitably choosing a family of base points $p_{t} \in Y_{\sigma, t},\left(Y_{\sigma, t} \cap \mathcal{U}, \omega_{t}^{s f}, p_{t}\right)$ converges to $\left(B_{\sigma}, g_{B_{\sigma}}, p_{\infty}\right)$ in the pointed Gromov-Hausdorff sense, when $t \rightarrow 0$. We say that $\left(Y_{\sigma, t} \cap \mathcal{U}, \omega_{t}^{s f}\right)$ collapses to $\left(B_{\sigma}, g_{B_{\sigma}}\right)$.

In summary, we have the following proposition.
Proposition 2.2. For any $t \in \Delta^{*}$, there is a unique complete Kähler-Einstein metric $\omega_{t}^{s f}$ on $Y_{\sigma, t} \cap \mathcal{U}$ such that the Ricci curvature is -1 , i.e.
$$\operatorname{Ric}\left(\omega_{t}^{s f}\right)=-\omega_{t}^{s f},$$
and $\omega_{t}^{\text {sf }}$ is semi-flat respecting to the torus fibration $f_{t}: Y_{\sigma, t} \cap \mathcal{U} \rightarrow B_{\sigma}$. Furthermore, $\left(Y_{\sigma, t} \cap \mathcal{U}, \omega_{t}^{s f}, p_{t}\right)$ converges to $\left(B_{\sigma}, g_{B_{\sigma}}, p_{\infty}\right)$ in the pointed Gromov-Hausdorff sense by choosing a family of base points $p_{t} \in Y_{\sigma, t}$, when $t \rightarrow 0$.

The logarithm $\log _{t}$ is used to convert classical algebraic varieties to tropical varieties (cf. [27]), and it is believed that the collapsing of Kähler-Einstein metrics can do the same in certain circumstances (cf. [13, 9]). This is true in our case as a direct corollary of the previous arguments.

Let $\mathfrak{p} \in \mathbb{C}[\check{\sigma} \cap M](t)$, i.e. $\mathfrak{p}=\sum_{u \in A} b_{u} t^{v(u)} \mathcal{Z}^{u}$ for a finite set $A \subset \check{\sigma} \cap M$, $b_{u} \in \mathbb{C}^{*}$, and $v: A \rightarrow \mathbb{Z}$, and $\mathrm{V}_{t, \mathfrak{p}} \subset Y_{\sigma, t}$ be the variety defined by $\left.\mathfrak{p}\right|_{Y_{\sigma, t}}=0$. The image $\mathcal{A}_{t}=\log _{t}\left(\mathrm{~V}_{t, \mathfrak{p}}\right) \subset \Lambda_{\mathbb{R}}$ is called an amoeba, and it is proven in [27] that $\mathcal{A}_{t}$ converges to a polyhedron complex $\mathcal{A}_{\infty}$ in the Hausdorff topology, when $t \in \mathbb{R}$ and $t \rightarrow 0$. Here $\mathcal{A}_{\infty}$ is called a non-Archimedean amoeba, and is the set of non-smooth points of the function
$$\mathfrak{p}_{\infty}(x)=\min _{u \in A}\{v(u)+\langle x, u\rangle\}$$
on $\Lambda_{\mathbb{R}}$. In tropical geometry, $\mathcal{A}_{\infty}$ is the tropical hypersurface defined by $\mathfrak{p}$ (cf. [27]). We have the following corollary by the collapsing of $\omega_{t}^{s f}$ to $g_{B_{\sigma}}$.

Corollary 2.3. When $t \in \mathbb{R}$ and $t \rightarrow 0$,
$$\mathrm{V}_{t, \mathfrak{p}} \cap \mathcal{U} \rightarrow \mathcal{A}_{\infty} \cap B_{\sigma}$$
under the pointed Gromov-Hausdorff convergence of $\left(Y_{\sigma, t} \cap \mathcal{U}, \omega_{t}^{s f}\right)$ to $\left(B_{\sigma}, g_{B_{\sigma}}\right)$.
2.2. Toroidal degeneration. A degeneration $\pi: \mathcal{X} \rightarrow \Delta$ is called simple toroidal, if for any point $x \in \mathcal{X}$, there is an open neighborhood $U$ satisfying that
\begin{itemize}
\item[i)] $U$ is isomorphic to an open subset of an affine toric variety $\mathcal{Y}_{\sigma}$, denoted still by $U$.
\item[ii)] The restriction of $\pi$ on $U$ is given by a regular function $\mathcal{Z}^{u_{\sigma}}$, where $u_{\sigma} \in M \cap \check{\sigma}$ satisfies $\left\langle u_{\sigma}, v\right\rangle=1$ for the primitive lattice vector $v \in \tau \cap N$ of any 1-dimensional face $\tau$ of $\sigma$. Hence if $D_{1}, \cdots, D_{d}$ are primitive toric Weil divisors of $\mathcal{Y}_{\sigma}$, then we have that $X_{0} \cap U=$ $\sum_{j=1}^{d} D_{j} \cap U$, and $X_{0}$ is reduced.
\item[iii)] Any non-empty $X_{0, I}$ is connected and normal, which implies that any $X_{0, I}$ does not intersect with itself.
\end{itemize}
Since the canonical divisor $\mathcal{K}_{\mathcal{Y}_{\sigma}}=-\sum_{j=1}^{d} D_{j}$ (cf. [10]), we have that $\left.\mathcal{K}_{\mathcal{X}}\right|_{U}=$ $-\operatorname{div}\left(\mathcal{Z}^{u_{\sigma}}\right)$, and thus $\mathcal{K}_{\mathcal{X}}$ is Cartier, i.e. $\mathcal{X}$ is Gorenstein. Degenerations with only simple normal crossing singularities are special cases of simple toroidal degenerations.

In Chapter II of [21], a compact polyhedral complex $\mathcal{B}$ with integral structure, called the dual intersection complex, is associated to $\pi: \mathcal{X} \rightarrow \Delta$ such that cells of $\mathcal{B}$ are in one-to-one correspondence to those non-empty $X_{0, I}$. More precisely, for any $X_{0, I} \neq \emptyset$, there is a unique polyhedral cell $\bar{B}_{I} \in \mathcal{B}$ such that $\operatorname{dim}_{\mathbb{R}} \bar{B}_{I}=n-\operatorname{dim}_{\mathbb{C}} X_{0, I}$, and $\bar{B}_{I^{\prime}}$ is a face of $\bar{B}_{I}$ if and only if $X_{0, I^{\prime}} \supset X_{0, I}$. The cell $\bar{B}_{I} \in \mathcal{B}$ associated to $X_{0, I}$ is constructed as the following. Let $p \in X_{0, I} \backslash \bigcup_{j \notin I} X_{0, j}$, and $U \subset \mathcal{X} \backslash \bigcup_{j \notin I} X_{0, j}$ be a neighborhood of $p$ isomorphic to an open subset of an affine toric variety $\mathcal{Y}_{\sigma}$. If $\sigma$ is the
corresponding rational convex cone in $N_{\mathbb{R}}$, then
$$\bar{B}_{I}=\left\{v \in \sigma \mid\left\langle v, u_{\sigma}\right\rangle=1\right\} .$$
We denote $B_{I}$ the interior of $\bar{B}_{I}$.
Now we state the main theorem of the present paper.
Theorem 2.4. Let $\pi: \mathcal{X} \rightarrow \Delta$ be a simple toroidal canonical polarized degeneration of projective $n$-manifolds, and $\omega_{t}$ be the unique Kähler-Einstein metric in $2 \pi c_{1}\left(\mathcal{K}_{X_{t}}\right), t \in \Delta^{*}$. If $\mathcal{X}$ is $\mathbb{Q}$-factorial, then the followings hold.
\begin{itemize}
\item[i)] For any $X_{0, I}$ with $\sharp I>1$, and any point $p_{0} \in X_{0, I} \backslash \bigcup_{i \notin I} X_{0, i}$, there are points $p_{t} \in X_{t}$ such that $p_{t} \rightarrow p_{0}$ in $\mathcal{X}$ when $t \rightarrow 0$, and by passing to a sequence, $\left(X_{t}, \omega_{t}, p_{t}\right)$ converges to a complete Riemannian manifold ( $W, g_{W}, p_{\infty}$ ) with $\operatorname{dim}_{\mathbb{R}} W=\operatorname{dim}_{\mathbb{R}} \bar{B}_{I}+2 \operatorname{dim}_{\mathbb{C}} X_{0, I}$ in the pointed Gromov-Hausdorff sense.
\item[ii)] If $\operatorname{dim}_{\mathbb{C}} X_{0, I}=0$, then $\left(W, g_{W}\right)$ is isometric to $\left(B_{I}, g_{B_{I}}\right)$ by suitably choosing $p_{t}$, where $g_{B_{I}}$ is the complete affine Kähler metric obtained in Theorem 2.1. Furthermore, if $\omega_{t, I}^{s f}$ is the semi-flat Kähler-Einstein metric constructed from $g_{B_{I}}$ in Proposition 2.2 on a neighborhood of $U \cap X_{t}$, where $U$ is a neighborhood of $X_{0, I}$ isomorphic an open subset of a toric variety, then
$$\left\|\omega_{t}-\omega_{t, I}^{s f}\right\|_{C_{l o c}^{\nu}\left(X_{t} \cap U, \omega_{t, I}^{s f}\right)} \rightarrow 0$$
for any $\nu>0$, when $t \rightarrow 0$, i.e. the collapsing is in the $C^{\infty}$-sense, and the convergence do not need to pass any sequence.
\end{itemize}

This theorem describes the collapsed limits of $\omega_{t}$, while the previous results of [36, 19, 29, 30] describe the non-collapsed limits, i.e. they still have complex dimension $n$.

The notion of toroidal degeneration is an algebro-geometric analogue of $F$-structure introduced in [3]. An $F$-structure $\mathcal{F}$ on a smooth manifold $X$ consists an open covering $\left\{U_{\alpha}\right\}$ such that for each $U_{\alpha}$, there is an effective $T^{n_{\alpha}}$-action on a finite cover of $U_{\alpha}$, and on any overlap $U_{\alpha} \cap U_{\beta}$, these two torus actions $T^{n_{\alpha}}$ and $T^{n_{\beta}}$ are compatible in a certain sense (See [9] for the details). For a toroidal degeneration $\pi: \mathcal{X} \rightarrow \Delta$, a small neighborhood $U$ of a $X_{0, I}$ with $\sharp I>1$ is isomorphic to an open subset of a toric variety, and $X_{t} \cap U$ is given by a monomial. Thus there is a natural local $T^{n_{\alpha}}$-action on $X_{t} \cap U$. We conjecture that there is an $F$-structure $\mathcal{F}$ on $X_{t} \cap \mathfrak{U}$, where $\mathfrak{U}$ is a small neighborhood of $\bigcup_{\sharp I>1} X_{0, I}$ in $\mathcal{X}$, and more importantly, this $\mathcal{F}$ is Hamiltonian, i.e. there is a symplectic form $\varpi_{t}$ on $X_{t}$ such that any local torus action of $\mathcal{F}$ is Hamiltonian.

Theorem 2.4 and Proposition 3.4 in Section 3.2 show that the KählerEinstein metric $\omega_{t}$ approximates some local semi-flat Kähler-Einstein metrics $\omega_{t, I}^{s f}$ on small open subsets of $X_{t}$, and $\omega_{t, I}^{s f}$ collapses smoothly to lower dimensional spaces along local torus fibrations. Moreover, we would see that
the curvature of $\omega_{t}$ is bounded independent of $t$ in Section 3.1. Hence there is an $F$-structure $\mathcal{F}^{\prime}$ on some region of $X_{t}$ by [4], and we again conjecture that $\mathcal{F}^{\prime}$ can be made to coincide with the above $\mathcal{F}$. Hamiltonian $F$-structures would be studied in a separate paper.

We remark that Theorem 2.4 should hold for more general settings, for example, toroidal degenerations without the assumption of $\mathcal{X}$ being $\mathbb{Q}$-factorial as in [31], or the log pair case, i.e. $\mathcal{K}_{\mathcal{X} / \Delta}+D$ is ample for a Cartier divisor $D$, as in [36, 19]. For avoiding too many technique difficulties, we leave those generalizations for future studies. In a recent paper [2], the existence of singular Kähler-Einstein metrics is obtained for stable varieties, i.e. varieties with semi-log canonical singularities and ample canonical divisor. It is also expected that the convergence theorems of [36, 19, 29, 30, 32] can be generalized to degenerations with central fiber $X_{0}$ stable varieties (cf. [2, 34]), which is related to the question of differential geometric understanding of the moduli space for stable varieties.

We finish this section by showing an example that Theorem 2.4 and Theorem 1.1 can apply.
Example 2.5. Firstly, we recall the standard Mumford degeneration of toric varieties. Let $M^{\prime} \cong \mathbb{Z}^{n}$ such that $M \cong M^{\prime} \times \mathbb{Z}$, and $\mathcal{P} \subset M_{\mathbb{R}}^{\prime}=M^{\prime} \otimes_{\mathbb{Z}} \mathbb{R}$ be a lattice polytope. If $\psi: \mathcal{P} \rightarrow \mathbb{R}$ is a piecewise linear convex function respecting to a lattice polyhedral decomposition $\mathfrak{P}$ of $\mathcal{P}$ with integral slopes, we define a lattice polyhedron
$$\tilde{\mathcal{P}}=\left\{(v, r) \in M_{\mathbb{R}} \cong M_{\mathbb{R}}^{\prime} \times \mathbb{R} \mid \psi(v) \leqslant r\right\},$$
which determines a toric variety $X_{\mathcal{P}}$ with a regular function $\pi=\mathcal{Z}^{(0,1)}$ : $X_{\tilde{\mathcal{P}}} \rightarrow \mathbb{C}$. For any $t \in \mathbb{C} \backslash\{0\}, X_{t}=\pi^{-1}(t)$ is isomorphic to the toric variety $X_{\mathcal{P}}$ associated to $\mathcal{P}$, and $X_{0}=\pi^{-1}(0)=\bigcup_{\tau \in \mathfrak{P}_{\text {max }}} X_{\tau}$, where $\mathfrak{P}_{\text {max }}$ denotes the set of $n$-dimensional polytopes of $\mathfrak{P}$, and $X_{\tau}$ is the toric variety associated to $\tau \in \mathfrak{P}_{\text {max }}$. By choosing $\mathcal{P}$ and $\psi$ properly, we can assume that $X_{0}$ has only simple normal crossing singularities, and $X_{t}$ is smooth for any $t \neq 0$. For instance, we take $\mathcal{P}, \mathfrak{P}$ and $\psi$ as the following:
![](https://cdn.mathpix.com/cropped/a731fc48-6e4b-4aef-ae4a-a14b7dbbcd8b-09.jpg?height=157&width=932&top_left_y=1850&top_left_x=438)

Now we follow the argument in the proof of Lemma 1.4 in [24]. Let $H$ be a sufficiently general very ample divisor on $X_{\tilde{\mathcal{P}}}$ such that $\mathcal{K}_{X_{\tilde{\mathcal{P}}}} \otimes \mathcal{O}(H)$ is ample, and $H+X_{t}$ has simple normal crossing singularities for any $|t|<\varepsilon \ll 1$. If $\mathfrak{c}: \tilde{X}_{\tilde{\mathcal{P}}} \rightarrow X_{\tilde{\mathcal{P}}}$ is the double ramified cover along $2 H$, then the Hurwitz formula shows that $\mathcal{K}_{\tilde{X}_{\tilde{\mathcal{P}}}} \cong \mathfrak{c}^{*}\left(\mathcal{K}_{X_{\tilde{\mathcal{P}}}} \otimes \mathcal{O}(H)\right)$, and hence, $\mathcal{K}_{\tilde{X}_{\tilde{\mathcal{p}}}}$ is ample. Note that $\tilde{X}_{0}=\mathfrak{c}^{-1}\left(X_{0}\right)$ still has only simple normal crossing singularities, and for any $t$ with $0<|t| \ll 1, \tilde{X}_{t}=\mathfrak{c}^{-1}\left(X_{t}\right)$ is smooth. We obtain a canonical degeneration $\tilde{\pi}: \mathcal{X} \rightarrow \Delta \subset \mathbb{C}$ satisfying the hypothesises in Theorem 2.4 and Theorem 1.1 by letting $\tilde{\pi}=\pi \circ \mathfrak{c}$ and $\mathcal{X}=\tilde{\pi}^{-1}(\Delta)$.
2.3. Special lagrangian submanifold. The original SYZ conjecture asserts the existence of special lagrangian submanifolds when Calabi-Yau manifolds are near the large complex limit (cf. [35]). There are some attempts to generalize the SYZ conjecture to the case of canonical polarized manifolds (cf. [20]), which include analog notions for special lagrangian submanifold. We also like to study a generalization of special lagrangian submanifold.

If $X$ is a canonical polarized projective $n$-manifold, then by definition, the canonical bundle $\mathcal{K}_{X}$ is ample. Let $\Omega$ be a holomorphic $n$-form, and $D$ be the effective divisor defined by $\Omega$, i.e. $D=\operatorname{div}(\Omega)$. The restriction of $\Omega$ on $X \backslash D$ is no-where vanishing, and thus $\mathcal{K}_{X \backslash D}$ is trivial, i.e. $X \backslash D$ is a quasi-projective Calabi-Yau manifold. A submanifold $L$ of $X \backslash D$ is called a generalized special lagrangian submanifold respecting to $\Omega$ and a Kähler metric $\omega$, if $\operatorname{dim}_{\mathbb{R}} L=n$,
$$\left.\omega\right|_{L} \equiv 0, \quad \text { and }\left.\quad \operatorname{Im}(\Omega)\right|_{L} \equiv 0 .$$
This notion of generalized special lagrangian submanifold is standard in the case of non-Ricci flat metric (cf. [14, 31]). The real part $\operatorname{Re}(\Omega)$ is not a calibration respecting to the Kähler metric $\omega$, but to a non-Kähler Hermitian metric $\rho \omega$ by Section 10.5 in [14], where $\rho>0$ is a function defined by $\rho^{n} \omega^{n}=\frac{n!}{2^{n}}(-1)^{\frac{n^{2}}{2}} \Omega \wedge \bar{\Omega}$.

As an application of Theorem 2.4, we have the following theorem.
Theorem 2.6. Let $\pi: \mathcal{X} \rightarrow \Delta$ and $\omega_{t}$ be the same as in Theorem 2.4. Assume that there is a zero dimensional $X_{0, I}$. If $\Omega_{t}$ is a section of $\mathcal{K}_{\mathcal{X} / \Delta}$ such that $D=\operatorname{div}\left(\Omega_{t}\right)$ does not intersect with $X_{0, I}$, then there is a generalized special lagrangian torus $L_{t} \subset\left(X_{t} \backslash D_{t}\right)$ respecting to $\omega_{t}$ and $\left.e^{\sqrt{-1} \vartheta_{t}} \Omega_{t}\right|_{X_{t}}$ for any $0<|t| \ll 1$ and a phase $\vartheta_{t} \in \mathbb{R}$, where $D_{t}=D \cap X_{t}$.

\section*{3. Proof of Theorem 2.4}
3.1. Background metric. In this section, we use the construction in [29] to obtain some approximation background Kähler metrics, which are uniformly equivalent to Kähler-Einstein metrics.

Let $\pi: \mathcal{X} \rightarrow \Delta$ be a simple toroidal canonical polarized degeneration of projective $n$-manifolds such that $\mathcal{X}$ is $\mathbb{Q}$-factorial. Since $\mathcal{K}_{\mathcal{X} / \Delta}$ is relative ample, there is an embedding $\Phi: \mathcal{X} \hookrightarrow \mathbb{C P}^{N_{m}} \times \Delta$ for two integers $m>0$ and $N_{m}>0$ such that $\mathcal{K}_{\mathcal{X} / \Delta}^{m} \cong \Phi^{*} \mathcal{O}_{\mathbb{C} \mathbb{P}^{N_{m}}}(1)$. There are sections $\Psi_{0}, \cdots, \Psi_{N_{m}}$ of $\mathcal{K}_{\mathcal{X} / \Delta}^{m}$ such that, by abusing notions, $h_{F S}=\left(\sum_{k=0}^{N_{m}}\left|\Psi_{k}\right|^{2}\right)^{-\frac{1}{m}}$ is the Hermitian metric whose curvature is the Fubini-Study metric, i.e.
$$\omega^{o}=\Phi^{*}\left(\frac{1}{m} \omega_{F S}+\sqrt{-1} d t \wedge d \bar{t}\right)=\sqrt{-1} \partial \bar{\partial} \log \left(\sum_{k=0}^{N_{m}}\left|\Psi_{k}\right|^{2}\right)^{\frac{1}{m}}$$

By regarding volume forms as Hermitian metrics of the anti-canonical bundle, we obtain a volume form $V=\left(\sum_{k=0}^{N_{m}}\left|\Psi_{k}\right|^{2}\right)^{\frac{1}{m}}$ on $\mathcal{X}$. For any $t \in \Delta^{*}$, $V_{t}=V \otimes(d t \wedge d \bar{t})^{-1}$ is a smooth volume form on $X_{t}$, and let
$$\omega_{t}^{o}=\left.\omega^{o}\right|_{X_{t}}=\sqrt{-1} \partial \bar{\partial} \log V_{t} .$$

Since $\mathcal{X}$ is $\mathbb{Q}$-factorial, there is a $\mu \in \mathbb{N}$ such that all of $\mu X_{0, i}, i=1, \cdots, l$, are Cartier divisors. Let $\|\cdot\|_{i}$ be a smooth Hermitian metric of $\mathcal{O}\left(\mu X_{0, i}\right)$ on $\mathcal{X}$, and $s_{i}$ be a defining section of $\mu X_{0, i}$, i.e. $\operatorname{div}\left(s_{i}\right)=\mu X_{0, i}$. Here the Hermitian metric $\|\cdot\|_{i}$ being smooth means that $\|\cdot\|_{i}$ is locally given by the restriction of a smooth positive function $\varrho$ on the ambient space $\mathbb{C}^{\nu}$ for a local embedding of an open subset $U$ of $\mathcal{X}$ into $\mathbb{C}^{\nu}$, and a trivialization of $\mathcal{O}\left(\mu X_{0, i}\right)$ on $U$. In this case, $\operatorname{Ric}\left(\|\cdot\|_{i}\right)$ is the restriction of the smooth form $-\sqrt{-1} \partial \bar{\partial} \log \varrho$ on $\mathbb{C}^{\nu}$.

We assume that $s_{1} \cdots s_{l}=t^{\mu}$ by choosing the parameter $t \in \Delta$ appropriately. Let
$$\alpha_{i}=\frac{1}{\mu} \log \left\|s_{i}\right\|_{i}^{2}, \quad \chi_{t}=\left(\log |t|^{2}\right)^{2} \prod_{i=1}^{l} \alpha_{i}^{-2},$$
and
$$\begin{aligned}
\tilde{\omega}_{t} & =\sqrt{-1} \partial \bar{\partial} \log \chi_{t} V_{t} \\
& =\omega_{t}^{o}+\sqrt{-1} \partial \bar{\partial} \log \chi_{t} \\
& =\omega_{t}^{o}+\left.2 \sum_{i=1}^{l}\left(\frac{\operatorname{Ric}\left(\|\cdot\|_{i}\right)}{\alpha_{i}}+\sqrt{-1} \frac{\partial \alpha_{i} \wedge \bar{\partial} \alpha_{i}}{\alpha_{i}^{2}}\right)\right|_{X_{t}}
\end{aligned}$$
on $X_{t}$ for $t \neq 0$. We can assume that $\left\|s_{i}\right\|_{i} \leqslant \varepsilon \ll 1$ such that
$$\frac{1}{2} \omega^{o} \leqslant \omega^{o}+\sum_{i=1}^{l} \frac{2}{\alpha_{i}} \operatorname{Ric}\left(\|\cdot\|_{i}\right) \leqslant 2 \omega^{o}$$
on $\mathcal{X} \backslash X_{0}$ by multiplying certain constants if necessary. We denote $X_{0, I}^{o}=$ $X_{0, I} \backslash \bigcup_{i \notin I} X_{0, i}$, and define a complete Kähler metric
$$\tilde{\omega}_{0, I}=\left.\omega^{o}\right|_{X_{0, I}^{o}}+\left.2 \sum_{i \notin I}\left(\frac{\operatorname{Ric}\left(\|\cdot\|_{i}\right)}{\alpha_{i}}+\sqrt{-1} \frac{\partial \alpha_{i} \wedge \bar{\partial} \alpha_{i}}{\alpha_{i}^{2}}\right)\right|_{X_{0, I}^{o}}$$
on $X_{0, I}^{o}$.
The Kähler metric $\tilde{\omega}_{t}$ is the background metric we need. Note that our assumption of $\mathcal{X}$ is stronger than the one in [29], and however is weaker than that in [30]. Nevertheless, the arguments in Section 3 of [29] and Section 4 of [30] show that the curvature of $\tilde{\omega}_{t}$ and the Ricci potential $\log \left(\frac{V_{t}}{\tilde{\omega}_{t}^{n}}\right)$ are bounded independent of $t$, which can also be obtained by the calculation in Section 3.2. Thus we have the $C^{0}$ and $C^{2}$ estimates for the potential function
of the Kähler-Einstein metric by the standard estimates for Monge-Ampère equations (cf. [1, 40]).

Proposition 3.1. Let $\varphi_{t}$ be the unique solution of Monge-Ampère equation
$$\left(\tilde{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right)^{n}=e^{\varphi_{t}} \chi_{t} V_{t},$$
and $\omega_{t}=\tilde{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}$ be the Kähler-Einstein metric on $X_{t}$. Then
$$\left|\varphi_{t}\right| \leqslant C_{1}, \quad \text { and } \quad C_{2}^{-1} \tilde{\omega}_{t} \leqslant \omega_{t} \leqslant C_{2} \tilde{\omega}_{t},$$
for constants $C_{1}>0$ and $C_{2}>0$ independent of $t$.
Once Proposition 3.1 is obtained, [36, 19, 29, 30] prove the convergence of $\omega_{t}$ to a complete Kähler-Einstein metric $\omega_{0}$ on the regular locus $X_{0, \text { reg }}$ in the Cheeger-Gromov sense, i.e. for any smooth family of embeddings $F_{t}: X_{0, \text { reg }} \rightarrow X_{t}, F_{t}^{*} \omega_{t}$ converges to $\omega_{0}$ in the locally $C^{\infty}$-sense when $t \rightarrow 0$. When $\sharp I=1, \tilde{\omega}_{0, I}$ is uniformly equivalent to the Kähler-Einstein metric $\omega_{0}$ on $X_{0, I}^{o} \subset X_{0, \text { reg }}$.
3.2. Proof of Theorem 2.4. Now we study the local collapsing behaviour of Kähler-Einstein metrics $\omega_{t}$.

For a point $p \in X_{0, I}$, let $U \subset \mathcal{X}$ be a neighborhood of $p$ isomorphic to an open subset of a toric variety $\mathcal{Y}_{\sigma}$, denoted still by $U$, such that $U \cap X_{0, I^{\prime}}$ is empty for any $I^{\prime} \nsubseteq I=\{1, \cdots, s+1\}$. Since $\mathcal{X}$ is $\mathbb{Q}$-factorial, so is $\mathcal{Y}_{\sigma}$, and $\mathcal{Y}_{\sigma}$ has only orbifold singularities, which is equivalent to the rational cone $\sigma$ being simplicial (cf. [10]).

If $v_{0}, \cdots, v_{s} \in N$ are primitive vectors belonging to 1-dimensional faces and generating $\sigma$ in $N_{\mathbb{R}}$, we denote $N_{\sigma}^{\prime}=\operatorname{Span}_{\mathbb{Z}}\left\{v_{0}, \cdots, v_{s}\right\}$ which is a sublattice of $N_{\sigma}=\mathbb{Z} \cdot(\sigma \cap N)$, and $M(\sigma)=\sigma^{\perp} \cap M \cong \mathbb{Z}^{n-s}$. Then $M \cong M_{\sigma} \oplus M(\sigma)$ where $M_{\sigma}=\operatorname{hom}_{\mathbb{Z}}\left(N_{\sigma}, \mathbb{Z}\right) \cong M / M(\sigma)$, and $M_{\sigma}$ is a sublattice of $M_{\sigma}^{\prime}=\operatorname{hom}_{\mathbb{Z}}\left(N_{\sigma}^{\prime}, \mathbb{Z}\right)=\operatorname{Span}_{\mathbb{Z}}\left(v_{0}^{*}, \cdots, v_{s}^{*}\right)$, where $v_{j}^{*}$ is the dual vector of $v_{j}$. Note that the restriction of $\pi$ on $U$ is given by a monomial $\mathcal{Z}^{u_{\sigma}}$, where $u_{\sigma} \in \check{\sigma} \cap M_{\sigma}$ satisfies $\left\langle u_{\sigma}, v_{j}\right\rangle=1$ for $j=0, \cdots, s$, i.e. $u_{\sigma}=\sum_{j=0}^{s} v_{j}^{*}$.

If $G=N_{\sigma} / N_{\sigma}^{\prime}$, and $\mathcal{Y}_{\sigma}^{\prime}=\operatorname{Spec}\left(\mathbb{C}\left[\check{\sigma} \cap M_{\sigma}^{\prime}\right]\right) \cong \mathbb{C}^{s+1}$, then the finite group $G$ acts on $\mathcal{Y}_{\sigma}^{\prime}$ by $v \cdot \mathcal{Z}^{u}=\exp (2 \pi \sqrt{-1}\langle v, u\rangle) \cdot \mathcal{Z}^{u}$ for any $v \in N_{\sigma}$ and $u \in M_{\sigma}^{\prime}$, and $\mathcal{Y}_{\sigma}^{\prime} / G \times\left(\mathbb{C}^{*}\right)^{n-s} \cong \mathcal{Y}_{\sigma}$. We denote $q_{\sigma}: \mathcal{Y}_{\sigma}^{\prime} \times\left(\mathbb{C}^{*}\right)^{n-s} \rightarrow \mathcal{Y}_{\sigma}$ the quotient map of the $G$-action. Let $z_{j}=\mathcal{Z}^{v_{j}^{*}}, j=0, \cdots, s$, be coordinates on $\mathcal{Y}_{\sigma}^{\prime}$, and $z_{s+1}, \cdots, z_{n}$ be coordinates on $\left(\mathbb{C}^{*}\right)^{n-s}$. The restriction $q_{\sigma}$ : $T_{N_{\sigma}^{\prime}} \times\left(\mathbb{C}^{*}\right)^{n-s} \rightarrow T_{N}$ is a finite covering map, where $T_{N}=N \otimes_{\mathbb{Z}} \mathbb{C}^{*}$ and $T_{N_{\sigma}^{\prime}}=N_{\sigma}^{\prime} \otimes_{\mathbb{Z}} \mathbb{C}^{*}$.

If we denote $Y_{\sigma, t}=\operatorname{div}\left(\mathcal{Z}^{u_{\sigma}}-t\right), t \in \mathbb{C}$, then $Y_{\sigma, t} \cap U=X_{t} \cap U$, and $Y_{\sigma, 0}=\sum_{j=0}^{s} D_{j}$ where $D_{j}$ is a primitive toric Weil divisor of $Y_{\sigma}$. The restriction $q_{\sigma}: q_{\sigma}^{-1}\left(Y_{\sigma, t}\right) \rightarrow Y_{\sigma, t}$ is a finite covering map as $X_{t} \cap U \subset T_{N}$ when $t \neq 0$, and $q_{\sigma}^{-1}\left(Y_{\sigma, t}\right)$ is given by the equation $z_{0} \cdots z_{s}=t$ in $\mathcal{Y}_{\sigma}^{\prime} \times\left(\mathbb{C}^{*}\right)^{n-s}$. We can regard $z_{1}, \cdots, z_{n}$ as coordinates of $q_{\sigma}^{-1}\left(Y_{\sigma, t}\right)$ for any $t \neq 0$. We assume that
$U \subset \mathcal{Y}_{\sigma}$ satisfies $q_{\sigma}^{-1}(U)=\left\{\left(z_{0}, \cdots, z_{s}\right) \in \mathcal{Y}_{\sigma}^{\prime}| | z_{j} \mid<\epsilon, 0 \leqslant j \leqslant s\right\} \times\left(U \cap X_{0, I}\right)$ for an $\epsilon<1$ without loss of generality.

Let $x_{0}, \cdots, x_{s}$ be coordinates on $N_{\sigma, \mathbb{R}}^{\prime}=N_{\sigma}^{\prime} \otimes_{\mathbb{Z}} \mathbb{R} \cong \mathbb{R}^{s+1}$ respecting to the basis $v_{0}, \cdots, v_{s}$. Note that the interior of the $s$-dimensional cell $\bar{B}_{I} \in \mathcal{B}$ associated to $X_{0, I}$ is given by
$$\begin{aligned}
B_{I} & =\left\{v \in \operatorname{int}(\sigma) \mid\left\langle v, u_{\sigma}\right\rangle=1\right\} \\
& =\left\{\left(x_{0}, \cdots, x_{s}\right) \in \mathbb{R}^{s+1} \mid \sum_{j=0}^{s} x_{j}=1, x_{j}>0, j=0, \cdots, s\right\} \\
& =\left\{\left(x_{1}, \cdots, x_{s}\right) \in \mathbb{R}^{s} \mid \sum_{j=1}^{s} x_{j}<1, x_{j}>0, j=1, \cdots, s\right\}
\end{aligned}$$
Here we regard $x_{1}, \cdots, x_{s}$ as coordinates on $B_{I}$.
For any $t \in \Delta^{*}$, we define the covering map
$$P_{t}: \mathbb{C}^{s} \times\left(\mathbb{C}^{*}\right)^{n-s} \rightarrow q_{\sigma}^{-1}\left(Y_{\sigma, t}\right)$$
by letting $z_{j}=e^{(\log |t|) w_{j}}$ and $x_{j}=\operatorname{Re}\left(w_{j}\right), j=1, \cdots, s$, i.e.
$$P_{t}\left(w_{1}, \cdots, w_{s}, z_{s+1}, \cdots, z_{n}\right)=\left(e^{(\log |t|) w_{1}}, \cdots, e^{(\log |t|) w_{s}}, z_{s+1}, \cdots, z_{n}\right) .$$
The fundamental domains of $P_{t}$ are
$$\mathfrak{D}_{t, \nu}=\left\{\left(w_{1}, \cdots, w_{s}\right) \in \mathbb{C}^{s} \left\lvert\, \frac{2 \pi \nu}{\log |t|} \leqslant \operatorname{Im}\left(w_{j}\right) \leqslant \frac{2 \pi(\nu+1)}{\log |t|}\right.\right\} \times\left(\mathbb{C}^{*}\right)^{n-s}$$
for $\nu \in \mathbb{Z}$, and naturally $\left(\mathbb{C}^{s} / \sqrt{-1} \frac{2 \pi \mathbb{Z}^{s}}{\log |t|}\right) \times\left(\mathbb{C}^{*}\right)^{n-s}$ is biholomorphic to $q_{\sigma}^{-1}\left(Y_{\sigma, t}\right)$ by further setting $z_{0}=t z_{1}^{-1} \cdots z_{s}^{-1}=t \exp \left(-\sum_{j=1}^{s}(\log |t|) w_{j}\right)$.

Note that if $\left|z_{j}\right|<\epsilon, j=0, \cdots, s$, then $x_{j}>\frac{\log \epsilon}{\log |t|}$ for $j=1, \cdots, s$, and $\log |t|\left(1-\sum_{j=1}^{s} x_{j}\right)=\log \left|z_{0}\right|<\log \epsilon$, which implies
$$P_{t}^{-1}\left(q_{\sigma}^{-1}\left(Y_{\sigma, t} \cap U\right)\right)=B_{t} \times \sqrt{-1} \mathbb{R}^{s} \times\left(\mathbb{C}^{*}\right)^{n-s},$$
where
$$B_{t}=\left\{\left(x_{1}, \cdots, x_{s}\right) \in \mathbb{R}^{s} \left\lvert\, x_{j}>\frac{\log \epsilon}{\log |t|}\right., j=1, \cdots, s, 1-\sum_{j=1}^{s} x_{j}>\frac{\log \epsilon}{\log |t|}\right\} \subset B_{I} .$$
Hence
$$q_{\sigma}^{-1}\left(Y_{\sigma, t} \cap U\right) \subset B_{I} \times \sqrt{-1}\left(\mathbb{R}^{s} / \frac{2 \pi \mathbb{Z}^{s}}{\log |t|}\right) \times\left(\mathbb{C}^{*}\right)^{n-s} \subset q_{\sigma}^{-1}\left(Y_{\sigma, t}\right) .$$

Lemma 3.2. Let $K \subset B_{I}$ be a compact subset such that $K \subset B_{t}$ for $|t| \ll 1$. On $K \times \sqrt{-1} \mathbb{R}^{s} \times\left(U \cap X_{0, I}\right) \subset\left(q_{\sigma} \circ P_{t}\right)^{-1}\left(U \cap Y_{\sigma, t}\right)$, when $t \rightarrow 0$,
\begin{itemize}
\item[i)]
$$P_{t}^{*} q_{\sigma}^{*} \chi_{t} V_{t} \rightarrow V_{0}^{\prime}=\frac{1}{4\left(1-\sum_{j=1}^{s} x_{j}\right)^{2}} \prod_{j=1}^{s} \frac{d w_{j} \wedge d \bar{w}_{j}}{4 x_{j}^{2}} \wedge V_{I},$$
in the $C^{\infty}$-sense, where $V_{I}$ is a smooth volume form on $U \cap X_{0, I}$.
\item[ii)]
$$P_{t}^{*} q_{\sigma}^{*} \tilde{\omega}_{t} \rightarrow \omega_{U, I}^{o}+\frac{\sqrt{-1}}{2}\left(\sum_{j=1}^{s} \frac{d w_{j} \wedge d \bar{w}_{j}}{x_{j}^{2}}+\frac{\sum_{i j=1}^{s} d w_{i} \wedge d \bar{w}_{j}}{\left(1-\sum_{j=1}^{s} x_{j}\right)^{2}}\right)=\tilde{\omega}^{o}$$
in the $C^{\infty}$-sense, where $\omega_{U, I}^{o}$ is the pull-back of the complete Kähler metric $\tilde{\omega}_{0, I}$ on $U \cap X_{0, I}$.
\end{itemize}

Proof. Let $w_{0}=1+\sqrt{-1} \frac{\arg (t)}{\log |t|}-w_{1}-\cdots-w_{s}$ on $\left(q_{\sigma} \circ P_{t}\right)^{-1}\left(Y_{\sigma, t}\right)$, and $x_{0}=$ $1-x_{1}-\cdots-x_{s}$ on $B_{I}$. We have $z_{0}=e^{\log |t| w_{0}}$ and $d w_{0}=-d w_{1}-\cdots-d w_{s}$ on $\left(q_{\sigma} \circ P_{t}\right)^{-1}\left(Y_{\sigma, t}\right)$.

Now, we claim that for a smooth function $\lambda$ on $\mathcal{Y}_{\sigma}^{\prime} \times\left(\mathbb{C}^{*}\right)^{n-s}, \lambda \circ P_{t} \rightarrow \lambda^{\prime}=$ $\lambda\left(0, z_{s+1}, \cdots, z_{n}\right)$ and $d z_{j}=\frac{\partial z_{j}}{\partial w_{j}} d w_{j} \rightarrow 0, j=0, \cdots, s$, in the $C^{\infty}$-sense on any compact subset of $\left(q_{\sigma} \circ P_{t}\right)^{-1}\left(U \cap Y_{\sigma, t}\right)$, when $t \rightarrow 0$. Since
$$\left|\frac{\partial^{k} z_{j}}{\partial w_{j}^{k}}\right|=\left|(\log |t|)^{k} e^{(\log |t|) x_{j}}\right| \leqslant\left|(\log |t|)^{k}\right| e^{\varepsilon_{j} \log |t|} \rightarrow 0, \quad\left|\frac{\partial z_{0}}{\partial w_{j}}\right|=\left|\frac{\partial z_{0}}{\partial w_{0}}\right|$$
for a $\varepsilon_{j}>0,0 \leqslant j \leqslant s$, the claim follows by $\left|\frac{\partial^{k} \lambda}{\partial z_{i_{1}}^{k_{1}} \cdots \partial z_{s_{s^{\prime}}}^{k_{s^{\prime}}}}\right| \leqslant C$ for some constants $C>0$.

Since $\mathcal{Y}_{\sigma}$ has only Gorenstein orbifold singularities, for the generator $\Omega_{\sigma} \in$ $\mathcal{O}\left(\mathcal{K}_{\mathcal{Y}_{\sigma}}\right), q_{\sigma}^{*} \Omega_{\sigma}$ is a $G$-invariant no-where vanishing holomorphic $(n+1,0)$ form on $\mathcal{Y}_{\sigma}^{\prime} \times\left(\mathbb{C}^{*}\right)^{n-s}$, and thus
$$q_{\sigma}^{*} V=\eta \prod_{j=0}^{n} d z_{j} \wedge d \bar{z}_{j}$$
where $\eta>0$ is a smooth function on $q_{\sigma}^{-1}(U)$. We obtain
$$q_{\sigma}^{*} V_{t}=\eta \prod_{j=1}^{s} \frac{d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2}} \wedge \prod_{i=s+1}^{n} d z_{i} \wedge d \bar{z}_{i}$$
on $q_{\sigma}^{-1}\left(X_{t} \cap U\right)$.
Without loss of generality, we assume that $I=\{1, \cdots, s+1\}$. Under a local trivialization of $\mathcal{O}\left(\mu X_{0, i}\right), i \in I$, on $U$, we have that $q_{\sigma}^{*} s_{i}=z_{j}^{\mu}$, where $j=i-1$, and the Hermitian metric $\|\cdot\|_{i}$ is a given by restricting a smooth function $\rho_{j}^{\prime}$ on an open subset $\mathbb{C}^{\nu}$ for a local embedding $U \hookrightarrow \mathbb{C}^{\nu}$. Thus $q_{\sigma}^{*} \alpha_{j+1}=\log \rho_{j}\left|z_{j}\right|^{2}$ for $j=0, \cdots, s$, where $\rho_{j}=\rho_{j}^{\prime} \circ q_{\sigma}>0$ are smooth
function on $q_{\sigma}^{-1}(U)$, and $q_{\sigma}^{*} \alpha_{i}<0, i=s+2, \cdots, l$, are also smooth functions. By (3.3),
$$q_{\sigma}^{*} \chi_{t} V_{t}=\eta^{\prime \prime} \frac{\left(\log |t|^{2}\right)^{2}}{\left(\log \left(\rho_{0}\left|z_{0}\right|^{2}\right)\right)^{2}} \prod_{j=1}^{s} \frac{d z_{j} \wedge d \bar{z}_{j}}{\left|z_{j}\right|^{2}\left(\log \left(\rho_{j}\left|z_{j}\right|^{2}\right)\right)^{2}} \wedge \prod_{i=s+1}^{n} d z_{i} \wedge d \bar{z}_{i}$$
where $\eta^{\prime \prime}>0$ is a smooth function on $q_{\sigma}^{-1}(U)$, and
$$P_{t}^{*} q_{\sigma}^{*} \chi_{t} V_{t}=\frac{\eta^{\prime \prime} \circ P_{t}}{\left(\frac{\log \rho_{0}}{\log |t|^{2}}+2 x_{0}\right)^{2}} \prod_{j=1}^{s} \frac{d w_{j} \wedge d \bar{w}_{j}}{\left(\frac{\log \rho_{j}}{\log |t|^{2}}+2 x_{j}\right)^{2}} \wedge \prod_{i=s+1}^{n} d z_{i} \wedge d \bar{z}_{i} .$$
By taking $t \rightarrow 0$, we obtain the convergence of volume forms.
We have $q_{\sigma}^{*} \omega^{o}$ is a smooth ( 1,1 )-form on $q_{\sigma}^{-1}(U)$, and
$$P_{t}^{*} q_{\sigma}^{*} \omega_{t}^{o}=\sqrt{-1} P_{t}^{*} q_{\sigma}^{*} \partial \bar{\partial} \log V_{t}=\sqrt{-1} \partial \bar{\partial} \log \eta \rightarrow \sqrt{-1} \partial \bar{\partial} \log \eta^{\prime},$$
in the $C^{\infty}$-sense, when $t \rightarrow 0$, where $\eta^{\prime}=\eta\left(0, z_{s+1}, \cdots, z_{n}\right)>0$. Note that $\sqrt{-1} \partial \bar{\partial} \log \eta^{\prime}$ is the pull-back of $\left.\omega^{o}\right|_{X_{0, I} \cap U}$. Since $q_{\sigma}^{*} \frac{\operatorname{Ric}\left(\|\cdot\|_{i}\right)}{\alpha_{i}}$ and $q_{\sigma}^{*} \frac{\partial \alpha_{i} \wedge \bar{\partial} \alpha_{i}}{\alpha_{i}^{2}}$, $i=s+2, \cdots, l$, are also smooth (1,1)-forms on $q_{\sigma}^{-1}(U)$, we have
$$P_{t}^{*} q_{\sigma}^{*}\left(\frac{\operatorname{Ric}\left(\|\cdot\|_{i}\right)}{\alpha_{i}}+\sqrt{-1} \frac{\partial \alpha_{i} \wedge \bar{\partial} \alpha_{i}}{\alpha_{i}^{2}}\right) \rightarrow \beta_{i},$$
in the $C^{\infty}$-sense, where $\beta_{i}$ is the pull-back of the smooth Kähler form $\left.\left(\frac{\operatorname{Ric}\left(\|\cdot\|_{i}\right)}{\alpha_{i}}+\sqrt{-1} \frac{\partial \alpha_{i} \wedge \bar{\partial} \alpha_{i}}{\alpha_{i}^{2}}\right)\right|_{U \cap X_{0, I}}$ on $U \cap X_{0, I}$. Thus
$$\omega_{U, I}^{o}=\sqrt{-1} \partial \bar{\partial} \log \eta^{\prime}+2 \sum_{i=s+2}^{l} \beta_{i}$$
is the pull-back of the restriction of $\tilde{\omega}_{0, I}$ on $U \cap X_{0, I}$ by (3.5).
On $K,(\log |t|) x_{j} \rightarrow-\infty, j=0, \cdots, s$, and thus,
$$P_{t}^{*} q_{\sigma}^{*} \frac{\operatorname{Ric}\left(\|\cdot\|_{j+1}\right)}{\alpha_{j+1}}=\frac{\sqrt{-1} \partial \bar{\partial} \log \rho_{i}}{\log \rho_{i}+2(\log |t|) x_{i}} \rightarrow 0,$$
in the $C^{\infty}$-sense. Furthermore,
$$P_{t}^{*} q_{\sigma}^{*} \frac{\partial \alpha_{j+1} \wedge \bar{\partial} \alpha_{j+1}}{\alpha_{j+1}^{2}}=\frac{\left(\partial \log \rho_{j}+\log |t| d w_{j}\right) \wedge\left(\bar{\partial} \log \rho_{j}+\log |t| d \bar{w}_{j}\right)}{\left(\log \rho_{j}+2(\log |t|) x_{j}\right)^{2}} \rightarrow \frac{d w_{j} \wedge d \bar{w}_{j}}{4 x_{j}^{2}},$$
in the $C^{\infty}$-sense, when $t \rightarrow 0$. Thus we obtain the conclusion by (3.4), and
$$\frac{d w_{0} \wedge d \bar{w}_{0}}{4 x_{0}^{2}}=\frac{\sum_{i j=1}^{s} d w_{i} \wedge d \bar{w}_{j}}{4\left(1-\sum_{j=1}^{s} x_{j}\right)^{2}}$$ \(\square\)

Lemma 3.3. Let $\varphi_{t}$ be the unique solution of (3.6), and $\omega_{t}=\tilde{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}$. For any sequence $t_{k} \rightarrow 0$, a subsequence of $\varphi_{t_{k}} \circ q_{\sigma} \circ P_{t_{k}}$ converges to $\varphi_{0}$ in the $C^{\infty}$-sense on $K \times \sqrt{-1} \mathbb{R}^{s} \times\left(U \cap X_{0, I}\right)$, where $\varphi_{0}$ is a smooth function on $B_{I} \times \sqrt{-1} \mathbb{R}^{s} \times\left(U \cap X_{0, I}\right)$ satisfying the complex Monge-Ampère equation
$$\left(\tilde{\omega}^{o}+\sqrt{-1} \partial \bar{\partial} \varphi_{0}\right)^{n}=e^{\varphi_{0}} V_{0}^{\prime},$$
with $\left|\varphi_{0}\right| \leqslant C_{3}$, and $C_{4}^{-1} \tilde{\omega}^{o} \leqslant \tilde{\omega}^{o}+\sqrt{-1} \partial \bar{\partial} \varphi_{0} \leqslant C_{4} \tilde{\omega}^{o}$.
Furthermore, $\varphi_{0}$ is independent of $\operatorname{Im}\left(w_{j}\right), j=1, \cdots, s$, i.e.
$$\varphi_{0}=\varphi_{0}\left(x_{1}, \cdots x_{s}, z_{s+1}, \cdots, z_{n}\right) .$$

Proof. By Proposition 3.1, we have that
$$\left|\varphi_{t}\right| \leqslant C, \text { and } C^{-1} P_{t}^{*} q_{\sigma}^{*} \tilde{\omega}_{t} \leqslant P_{t}^{*} q_{\sigma}^{*}\left(\tilde{\omega}_{t}+\sqrt{-1} \partial \bar{\partial} \varphi_{t}\right) \leqslant C P_{t}^{*} q_{\sigma}^{*} \tilde{\omega}_{t}$$
for a constant $C>0$. We obtain the $C^{2, \alpha}$-estimates for $\varphi_{t}$, i.e. $\| \varphi_{t} \circ q_{\sigma} \circ$ $P_{t} \|_{C^{2, \alpha}} \leqslant \bar{C}$, by Lemma 3.2 and the Evans-Krylov theory (cf. [11, 33]), and the higher order estimates $\left\|\varphi_{t} \circ q_{\sigma} \circ P_{t}\right\|_{C^{\nu}} \leqslant C(\nu)$ by the standard Schauder estimates on any compact subset $K^{\prime} \subset K \times \sqrt{-1} \mathbb{R}^{s} \times\left(U \cap X_{0, I}\right)$. Thus by passing to a subsequence of $t_{k}, \varphi_{t_{k}} \circ q_{\sigma} \circ P_{t_{k}}$ converges to a smooth function $\varphi_{0}$ in the locally $C^{\infty}$-sense, and $\varphi_{0}$ satisfies the the complex Monge-Ampère equation (3.10) by Lemma 3.2.

Since $\varphi_{t} \circ q_{\sigma} \circ P_{t}$ is a periodic function with period $\sqrt{-1} \frac{2 \pi \mathbb{Z}^{s}}{\log |t|}$, i.e.
$$\varphi_{t} \circ q_{\sigma} \circ P_{t}(\mathrm{w}, \mathrm{z})=\varphi_{t} \circ q_{\sigma} \circ P_{t}\left(\mathrm{w}+\sqrt{-1} \frac{2 \pi \mathfrak{m}}{\log |t|}, \mathrm{z}\right),$$
for any $\mathfrak{m} \in \mathbb{Z}^{s}$, where $\mathrm{w}=\left(w_{1}, \cdots, w_{s}\right)$ and $\mathrm{z}=\left(z_{s+1}, \cdots, z_{n}\right)$, we obtain that $\varphi_{0}$ is independent of $\operatorname{Im}\left(w_{j}\right), j=1, \cdots, s$, by the smooth convergence. \(\square\)

Since $\frac{\partial^{2} \varphi_{0}}{\partial w_{i} \bar{\partial} w_{j}}=\frac{\partial^{2} \varphi_{0}}{4 \partial x_{i} \partial x_{j}}$, the corresponding Riemannian metric of $\tilde{\omega}^{o}+$ $\sqrt{-1} \partial \bar{\partial} \varphi_{0}$ is
$$g_{0}=\sum_{i j=1}^{s}\left(\frac{\delta_{i j}}{x_{i}^{2}}+\frac{1}{\left(1-\sum_{j=1}^{s} x_{j}\right)^{2}}+\frac{\partial^{2} \varphi_{0}}{2 \partial x_{i} \partial x_{j}}\right)\left(d x_{i} d x_{j}+d \theta_{i} d \theta_{j}\right)+\mathcal{G}_{0}$$
where $\theta_{j}=\operatorname{Im}\left(w_{j}\right), j=1, \cdots, n$, and $\mathcal{G}_{0}$ denotes the remaining terms that do not involve any $d \theta_{i} d \theta_{j}$ and $d x_{i} d x_{j}$.

Note that both $\tilde{\omega}^{o}$ and $\varphi_{0}$ are invariant under the translation $w_{j} \mapsto w_{j}+$ $\lambda_{j} \sqrt{-1}, j=1, \cdots, s$, for any $\left(\lambda_{1}, \cdots, \lambda_{s}\right) \in \mathbb{R}^{s}$. Hence for any $t \neq 0$, $\tilde{\omega}^{o}+\sqrt{-1} \partial \bar{\partial} \varphi_{0}$ descents to a Kähler metric $\omega_{t}^{s f}$ on $Y_{\sigma, t} \cap U$, which satisfies that
$$P_{t}^{*} q_{\sigma}^{*} \omega_{t}^{s f}=\tilde{\omega}^{o}+\sqrt{-1} \partial \bar{\partial} \varphi_{0}, \quad \text { and } \quad\left\|\omega_{t_{k}}-\omega_{t_{k}}^{s f}\right\|_{C_{l o c}^{\nu}\left(Y_{\sigma, t_{k}} \cap U, \omega_{t_{k}}^{s f}\right)} \rightarrow 0,$$
for any $\nu>0$, when $t_{k} \rightarrow 0$ by Lemma 3.3.

Define a fibration
$$\tilde{f}_{t}: B_{I} \times \sqrt{-1}\left(\mathbb{R}^{s} /\left(\frac{2 \pi \mathbb{Z}^{s}}{\log |t|}\right)\right) \times\left(\mathbb{C}^{*}\right)^{n-s} \rightarrow B_{I} \times\left(\mathbb{C}^{*}\right)^{n-s}$$
by the projection. Note that $\tilde{f}_{t}$ is $G$-equivariant, $\tilde{f}_{t}$ induces a $T^{s}$-fibration
$$f_{t}: U \cap Y_{\sigma, t} \rightarrow B_{t} \times\left(\mathbb{C}^{*}\right)^{n-s}, \quad \text { with } \quad \tilde{f}_{t}=f_{t} \circ q_{\sigma} .$$
For a point $(\mathrm{x}, \mathrm{z}) \in B_{t} \times\left(\mathbb{C}^{*}\right)^{n-s}$, where $\mathrm{x}=\left(x_{1}, \cdots, x_{s}\right) \in B_{t}$ and $\mathrm{z}=$ $\left(z_{s+1}, \cdots, z_{n}\right) \in\left(\mathbb{C}^{*}\right)^{n-s}$, the fiber $f_{t}^{-1}(\mathrm{x}, \mathrm{z})$ satisfies that $\left(q_{\sigma} \circ P_{t}\right)^{-1}\left(f_{t}^{-1}(\mathrm{x}, \mathrm{z})\right)=$ $\left\{(\mathrm{x}+\sqrt{-1} \theta, \mathrm{z}) \mid \theta=\left(\theta_{1}, \cdots, \theta_{s}\right) \in \mathbb{R}^{s}\right\}$. Hence the restriction of the Kähler metric $\omega_{t}^{s f}$ on $f_{t}^{-1}(\mathrm{x}, \mathrm{z})$ is a flat Riemannian metric, i.e. $\omega_{t}^{s f}$ is a semi-flat metric, and
$$\operatorname{diam}_{\omega_{t_{k}}}\left(f_{t_{k}}^{-1}(\mathrm{x}, \mathrm{z})\right) \sim \operatorname{diam}_{\omega_{t_{k}}^{s f}}\left(f_{t_{k}}^{-1}(\mathrm{x}, \mathrm{z})\right) \leqslant \frac{2 \pi s \sqrt{C_{\mathrm{x}, \mathrm{z}}}}{-\log |t|} \rightarrow 0,$$
when $t \rightarrow 0$, by (3.12) and (3.11), where
$$C_{\mathrm{x}, \mathrm{z}}=\sum_{i j=1}^{s}\left|\frac{\delta_{i j}}{x_{i}^{2}}+\frac{1}{\left(1-\sum_{j=1}^{s} x_{j}\right)^{2}}+\frac{\partial^{2} \varphi_{0}}{2 \partial x_{i} \partial x_{j}}(\mathrm{x}, \mathrm{z})\right| .$$

We denote $W_{U}=B_{I} \times\left(U \cap X_{0, I}\right)$, and naturally regard $W_{U} \subset B_{I} \times$ $\sqrt{-1}\left(\mathbb{R}^{s} /\left(\frac{2 \pi \mathbb{Z}^{s}}{\log |t|}\right)\right) \times\left(U \cap X_{0, I}\right)$ given by $\theta_{j}=0, j=1, \cdots, n$. We let $g_{W_{U}}=$ $\left.g_{0}\right|_{W_{U}}$. If $p \in W_{U}$, and $r>0$ such that the metric ball $B_{g_{W_{U}}}(p, r) \subset K^{\prime \prime}$ for a compact subset $K^{\prime \prime} \subset W_{U}$, then
$$\left(B_{\omega_{t_{k}}}\left(p_{t_{k}}, r\right), \omega_{t_{k}}\right) \text { and }\left(B_{\omega_{t_{k}}^{s f}}\left(p_{t_{k}}, r\right), \omega_{t_{k}}^{s f}\right) \rightarrow\left(B_{g_{W_{U}}}(p, r), g_{W_{U}}\right)$$
in the Gromov-Hausdorff sense by (3.12), when $t_{k} \rightarrow 0$, for some $p_{t} \in X_{t} \cap U$. By Gromov's precompactness theorem (cf. [12]), $\left(X_{t_{k}}, \omega_{t_{k}}, p_{t_{k}}\right)$ converges to a complete metric space $\left(W, d_{W}, p_{\infty}\right)$ of Hausdorff dimension $\varrho$ in the pointed Gromov-Hausdorff sense, and there is a local isometric embedding $\left(B_{g_{W_{U}}}\left(p_{\infty}, r\right), g_{W_{U}}\right) \hookrightarrow\left(W, d_{W}\right)$, which implies $\varrho=\operatorname{dim}_{\mathbb{R}} B_{I} \times X_{0, I}$.

In summary, we have the following proposition.
Proposition 3.4. There is a semi-flat Kähler-Einstein metric $\omega_{t}^{s f}$ on $X_{t} \cap U$ respecting to $f_{t}$ such that
$$\left\|\omega_{t_{k}}-\omega_{t_{k}}^{s f}\right\|_{C_{l o c}^{\nu}\left(Y_{\sigma, t_{k}} \cap U, \omega_{t_{k}}^{s f}\right)} \rightarrow 0,$$
for any $\nu>0$, and a sequence $t_{k} \rightarrow 0$. Furthermore, $\left(X_{t_{k}}, \omega_{t_{k}}, p_{t_{k}}\right)$ converges to a complete metric space $\left(W, d_{W}, p_{\infty}\right)$ in the pointed Gromov-Hausdorff sense by choosing some base points $p_{t} \in X_{t}$, and the Hausdorff dimension of $W$ equals to $\operatorname{dim}_{\mathbb{R}} B_{I}+2 \operatorname{dim}_{\mathbb{C}} X_{0, I}$.

Now we are ready to prove Theorem 2.4.

Proof of Theorem 2.4. Let $\left\{U_{\gamma}\right\}$ be an open cover of $X_{0, I}^{o}$ such that any $U_{\gamma} \subset \mathcal{X}$ is isomorphic to an open subset of a toric variety, and does not intersect with $\bigcup_{i \notin I} X_{0, i}$. By applying the above arguments to $U_{\gamma}$, we have $W_{U_{\gamma}}=B_{I} \times\left(U_{\gamma} \cap X_{0, I}\right) \subset B_{I} \times \sqrt{-1}\left(\mathbb{R}^{s} /\left(\frac{2 \pi \mathbb{Z}^{s}}{\log |t|}\right)\right) \times\left(U_{\gamma} \cap X_{0, I}\right)$, and a metric $g_{U_{\gamma}}=\left.g_{\gamma, 0}\right|_{W_{U_{\gamma}}}$, where $g_{\gamma, 0}$ is the Riemannian metric given by (3.11). If $\left.\omega_{\gamma, t}^{s f}\right|_{X_{t} \cap U_{\gamma}}$ denotes the semi-flat Kähler-Einstein metric satisfying (3.12), then, by Lemma 3.3, $P_{t}^{*} q_{\sigma}^{*} \omega_{\gamma, t}^{s f}$ is uniformly equivalent to $\tilde{\omega}^{o}$ on $B_{I} \times \sqrt{-1} \mathbb{R}^{s} \times$ $\left(U_{\gamma} \cap X_{0, I}\right)$. For any $U_{\gamma}$, since there are finite $U_{1}, \cdots, U_{\varsigma} \in\left\{U_{\gamma}\right\}$ such that $\left(U \cup U_{1} \cup \cdots \cup U_{\varsigma} \cup U_{\gamma}\right) \cap X_{t}$ is connected, we have a point $p_{t_{k}, \gamma} \in X_{t_{k}} \cap U_{\gamma}$ such that $\operatorname{dist}_{\omega_{t_{k}}}\left(p_{t_{k}, \gamma}, p_{t_{k}}\right) \leqslant C_{\gamma}$ for a constant independent of $t_{k}$ by Proposition 3.4. Thus there is a local isometric embedding $\iota_{\gamma}:\left(W_{U_{\gamma}}, g_{U_{\gamma}}\right) \hookrightarrow\left(W, d_{W}\right)$. Note that the restriction of $g_{U_{\gamma}}$ on any $B_{I} \times\{q\}$ is complete, $\left.g_{U_{\gamma}}\right|_{U_{\gamma} \cap X_{0, I}}$ is uniformly equivalent to $\left.\tilde{\omega}^{o}\right|_{U_{\gamma} \cap X_{0, I}}=\left.\tilde{\omega}_{0, I}\right|_{U_{\gamma} \cap X_{0, I}}$, and $\tilde{\omega}_{0, I}$ is complete on $X_{0, I}^{o}$ by (3.5). Therefore, $\bigcup_{\gamma} \iota_{\gamma}\left(W_{U_{\gamma}}, g_{U_{\gamma}}\right) \subset\left(W, d_{W}\right)$ is a complete Riemannian manifold, which implies that $\bigcup_{\gamma} \iota_{\gamma}\left(W_{U_{\gamma}}, g_{U_{\gamma}}\right)=\left(W, d_{W}\right)$.

Now we assume $\operatorname{dim}_{\mathbb{C}} X_{0, I}=0$, i.e. $s=n$. Then $W_{U}=B_{I}, \varphi_{0}=$ $\varphi_{0}\left(x_{1}, \cdots, x_{n}\right)$ is a function on $B_{I}$, and we denote $g_{B_{I}}=g_{W_{U}}$. We need the following lemma to finish the proof.

Lemma 3.5. If
$$\phi=\frac{\varphi_{0}}{2}-\sum_{j=1}^{n} \log x_{j}-\log \left(1-\sum_{j=1}^{n} x_{j}\right),$$
then
$$g_{B_{I}}=\sum_{i j=1}^{n} \frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}} d x_{i} d x_{j}$$
on $B_{I}$, and $\phi$ is the unique solution of the real Monge-Ampère equation
$$\operatorname{det}\left(\frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}\right)=\kappa e^{2 \phi},\left.\quad \phi\right|_{\partial \bar{B}_{I}}=+\infty,$$
for a constant $\kappa>0$, i.e. $\phi$ is obtained in Theorem 2.1.
Proof. Note that $\frac{\partial \varphi_{0}}{\partial w_{j}}=\frac{\partial \varphi_{0}}{2 \partial x_{j}}$, and
$$\frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}=\frac{\partial^{2} \varphi_{0}}{2 \partial x_{i} \partial x_{j}}+\frac{\delta_{i j}}{x_{j}^{2}}+\frac{1}{\left(1-\sum_{j=1}^{n} x_{j}\right)^{2}} .$$
By (3.11), $g_{B_{I}, i j}=\frac{\partial^{2} \phi}{\partial x_{i} \partial x_{j}}$. By Lemma 3.2 and Lemma 3.3, we have
$$\operatorname{det}\left(\frac{\delta_{i j}}{x_{j}^{2}}+\frac{1}{\left(1-\sum_{j=1}^{n} x_{j}\right)^{2}}+\frac{\partial^{2} \varphi_{0}}{2 \partial x_{i} \partial x_{j}}\right)=\frac{e^{\varphi_{0}} 2^{n} \eta^{\prime}}{4^{n+1}\left(1-\sum_{j=1}^{n} x_{j}\right)^{2} \prod_{j=1}^{n} x_{j}^{2}},$$
where $\eta^{\prime}>0$ is a constant.
Now Proposition 5.5 in [6] implies that $\varphi_{0}$ is the unique solution of (3.10), which implies the uniqueness of $\phi$. \(\square\)

Note that $g_{B_{I}}$ is a complete metric on $B_{I}$, and thus $\left(W, d_{W}\right)$ is isometric to $\left(B_{I}, g_{B_{I}}\right)$. By the uniqueness of $g_{B_{I}}$, we have the convergence of Proposition 3.4 without passing to any sequence $t_{k}$. We obtain the conclusion. \(\square\)

\section*{4. Proof of Theorem 2.6}

Proof of Theorem 2.6. Since $\mathcal{K}_{\mathcal{X} / \Delta}$ is ample, there is a section $\Omega_{t}$ of $\mathcal{K}_{\mathcal{X} / \Delta}$ such that $D \cap X_{0, I}=\emptyset$ where $D=\operatorname{div}\left(\Omega_{t}\right)$. Let $U \subset \mathcal{X}$ be a neighborhood of $X_{0, I}$ isomorphic to an open subset of a toric variety $\mathcal{Y}_{\sigma}$, denoted still by $U$, such that $U \cap X_{0, I^{\prime}}$ is empty for any $I^{\prime} \nsubseteq I=\{1, \cdots, s+1\}$. We assume that $D \cap U=\emptyset$ by shrinking $U$ if necessary.

We adopt the construction in Section 3.2. There is a toric variety $\mathcal{Y}_{\sigma}^{\prime} \cong$ $\mathbb{C}^{n+1}$ with coordinates $z_{0}, \cdots, z_{n}$, and a finite group $G=N / N^{\prime}$ acting on $\mathcal{Y}_{\sigma}^{\prime}$. Let $q_{\sigma}: \mathcal{Y}_{\sigma}^{\prime} \rightarrow \mathcal{Y}_{\sigma}$ be the finite quotient by $G=N / N^{\prime}$, and $Y_{\sigma, t} \subset \mathcal{Y}_{\sigma}$ such that $Y_{\sigma, t} \cap U=X_{t} \cap U$ as in Section 3.2. Recall that $q_{\sigma}^{-1}\left(Y_{\sigma, t}\right)$ is given by $z_{0} \cdots \cdot z_{n}=t$, and $q_{\sigma}^{-1}\left(Y_{\sigma, t} \cap U\right) \subset B_{I} \times \sqrt{-1}\left(\mathbb{R}^{n} / \frac{2 \pi \mathbb{Z}^{n}}{\log |t|}\right) \subset q_{\sigma}^{-1}\left(Y_{\sigma, t}\right)$, where $B_{I}$ is given by (3.13).

For a $p=\left(p_{1}, \cdots, p_{n}\right) \in B_{I}$, we define an embedding
$$\mathfrak{i}_{t}: B_{I} \times \sqrt{-1}\left(\mathbb{R}^{n} / \frac{2 \pi \mathbb{Z}^{n}}{\log |t|}\right) \hookrightarrow \mathbb{C}^{n} /\left(2 \pi \sqrt{-1} \mathbb{Z}^{n}\right)=Y_{\infty}$$
by letting $\tilde{w}_{j}=(\log |t|)\left(w_{j}-p_{j}\right), j=1, \cdots, n$. We identify $B_{I} \times \sqrt{-1}\left(\mathbb{R}^{n} / \frac{2 \pi \mathbb{Z}^{n}}{\log |t|}\right)$ with the image $\mathfrak{i}_{t}\left(B_{I} \times \sqrt{-1}\left(\mathbb{R}^{n} / \frac{2 \pi \mathbb{Z}^{n}}{\log |t|}\right)\right) \subset Y_{\infty}$ by $\mathfrak{i}_{t}$ without any confusion.

Assume that $\tilde{\lambda}_{t}=\tilde{\lambda}_{t}\left(w_{1}, \cdots, w_{n}\right)$ is a family of functions convergence smoothly to $\tilde{\lambda}_{0}=\tilde{\lambda}_{0}\left(x_{1}, \cdots, x_{n}\right)$ under the coordinates $w_{1}, \cdots, w_{n}$ when $t \rightarrow 0$, i.e. $\frac{\partial^{k} \tilde{\lambda}_{t}}{\partial w_{j_{1}}^{k_{1}} \ldots \partial w_{j_{m}}^{k_{m}}} \rightarrow \frac{\partial^{k} \tilde{\lambda}_{0}}{\partial w_{j_{1}}^{k_{1}} \ldots \partial w_{j_{m}}^{k_{m}}}=\frac{\partial^{k} \tilde{\lambda}_{0}}{2^{k} \partial x_{j_{1}}^{k_{1}} \ldots \partial x_{j_{m}}^{k_{m}}}$. Since $w_{j}=p_{j}+$ $(\log |t|)^{-1} \tilde{w}_{j}$ and $\frac{\partial \tilde{\lambda}_{t}}{\partial \tilde{w}_{j}}=(\log |t|)^{-1} \frac{\partial \tilde{\lambda}_{t}}{\partial w_{j}}$, we have $\tilde{\lambda}_{t} \rightarrow \tilde{\lambda}_{0}\left(p_{1}, \cdots, p_{n}\right)$ in the $C^{\infty}$-sense on any on any compact subset $K^{\prime} \subset \mathfrak{i}_{t}\left(B_{I} \times \sqrt{-1}\left(\mathbb{R}^{n} / \frac{2 \pi \mathbb{Z}^{n}}{\log |t|}\right)\right) \subset$ $Y_{\infty}$, when $t \rightarrow 0$.

Since $\mathcal{Y}_{\sigma}$ has only Gorenstein orbifold singularities, for the local generator $\Omega_{\sigma} \in \mathcal{O}\left(\mathcal{K}_{\mathcal{Y}_{\sigma}}\right), q_{\sigma}^{*} \Omega_{\sigma}$ is a $G$-invariant no-where vanishing holomorphic ( $n+$ 1,0 )-form on $\mathcal{Y}_{\sigma}^{\prime}$, and thus
$$q_{\sigma}^{*} \Omega_{t}=\Omega_{\sigma} \otimes(d t)^{-1}=\zeta \frac{d z_{1} \wedge \cdots \wedge d z_{n}}{z_{1} \cdots \cdots z_{n}},$$
on $q_{\sigma}^{-1}\left(X_{t} \cap U\right)$, where $\zeta>0$ is a holomorphic function on $\mathcal{Y}_{\sigma}^{\prime}$. Note that $\zeta\left(w_{1}, \cdots, w_{n}\right) \rightarrow \zeta(0)$ in the $C^{\infty}$-sense by the argument in the proof of Lemma 3.2. Thus
$$q_{\sigma}^{*} \Omega_{t}=\zeta d \tilde{w}_{1} \wedge \cdots \wedge d \tilde{w}_{n} \rightarrow \Omega_{\infty}=\zeta(0) d \tilde{w}_{1} \wedge \cdots \wedge d \tilde{w}_{n},$$
in the $C^{\infty}$-sense, when $t \rightarrow 0$.
If we denote $L_{0}=\{0\} \times \sqrt{-1}\left(\mathbb{R}^{n} /\left(2 \pi \mathbb{Z}^{n}\right)\right)$, then for any $|t| \ll 1$, there is a $\vartheta_{t} \in \mathbb{R}$ such that $e^{\sqrt{-1} \vartheta_{t}} \int_{L_{0}} q_{\sigma}^{*} \Omega_{t} \in \mathbb{R}$, which implies that $\int_{L_{0}} \operatorname{Im}\left(e^{\sqrt{-1} \vartheta_{0}} \Omega_{\infty}\right)=$ 0 , $\int_{L_{0}} \operatorname{Im}\left(e^{\sqrt{-1} \vartheta_{t}} q_{\sigma}^{*} \Omega_{t}\right)=0$, and $\left[\left.\operatorname{Im}\left(e^{\sqrt{-1} \vartheta_{t}} q_{\sigma}^{*} \Omega_{t}\right)\right|_{L_{0}}\right]=0$ in $H^{n}\left(L_{0}, \mathbb{R}\right)$. Since $e^{\sqrt{-1} \vartheta_{0}} \zeta(0)$ is a constant, we have
$$\left.\operatorname{Im}\left(e^{\sqrt{-1} \vartheta_{0}} \Omega_{\infty}\right)\right|_{L_{0}}=\left.\operatorname{Im}\left(e^{\sqrt{-1} \vartheta_{0}} \zeta(0) d \tilde{w}_{1} \wedge \cdots \wedge d \tilde{w}_{n}\right)\right|_{L_{0}} \equiv 0 .$$

By Lemma 3.2 and Lemma 3.3,
$$(\log |t|)^{2} q_{\sigma}^{*} \omega_{t} \rightarrow \frac{\sqrt{-1}}{2} \sum_{i j=1}^{n}\left(\frac{\delta_{i j}}{p_{j}^{2}}+\frac{1}{\left(1-\sum_{j=1}^{s} p_{j}\right)^{2}}+\frac{\partial^{2} \varphi_{0}}{2 \partial x_{i} \partial x_{j}}(p)\right) d \tilde{w}_{i} \wedge d \overline{\tilde{w}}_{j}=\omega_{\infty}$$
in the $C^{\infty}$-sense on any compact subset $K^{\prime}$ on $Y_{\infty}$, when $t \rightarrow 0$. Since the curvature of $\omega_{t}$ are uniformly bounded independent of $t$, we have that $\omega_{\infty}$ is a flat metric on $Y_{\infty}$. A direct calculation shows $\left.\omega_{\infty}\right|_{L_{0}} \equiv 0$. Note that for any $A \in H_{2}\left(L_{0}, \mathbb{Z}\right)$,
$$\begin{gathered}
\left|(\log |t|)^{2} \int_{A} q_{\sigma}^{*} \omega_{t}\right| \rightarrow\left|\int_{A} \omega_{\infty}\right|=0, \text { and } \\
\int_{A} q_{\sigma}^{*} \omega_{t}=2 \pi \int_{q_{\sigma}(A)} c_{1}\left(\mathcal{K}_{X_{t}}\right) \in 2 \pi \mathbb{Z}
\end{gathered}$$
Thus $\int_{A} q_{\sigma}^{*} \omega_{t}=0$, and $\left[\left.q_{\sigma}^{*} \omega_{t}\right|_{L_{0}}\right]=0$ in $H^{2}\left(L_{0}, \mathbb{R}\right)$. By Theorem 10.8 in [14], we obtain a family of generalized special lagrangian submanifolds $\tilde{L}_{t} \subset$ $B_{I} \times \sqrt{-1}\left(\mathbb{R}^{n} / \frac{2 \pi \mathbb{Z}^{n}}{\log |t|}\right)$ respecting to $q_{\sigma}^{*} \omega_{t}$ and $e^{\sqrt{-1} \vartheta_{t}} q_{\sigma}^{*} \Omega_{t}$ for $|t| \ll 1$. We obtain the conclusion by letting $L_{t}=q_{\sigma}\left(\tilde{L}_{t}\right)$. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] T. Aubin, Equation du type de Monge-Ampère sur les variétés Kähleriennes compacts, C. R. Acad. Sci. Prais 283 (1976), 119-121.
\item[] [2] R. Berman, H. Guenancia, Kähler-Einstein metrics on stable varieties and log canonical pairs, Geom. Funct. Anal. 24 no. 6, (2014), 1683-1730.
\item[] [3] J. Cheeger, M. Gromov, Collapsing Riemannian manifolds while keeping their curvature bounded. I, J. Diff. Geom. 23 (1986) 309-346.
\item[] [4] J. Cheeger, M. Gromov, Collapsing Riemannian manifolds while keeping their curvature bounded. II, J. Diff. Geom. 32 (1990) 269-298.
\item[] [5] S.Y. Cheng and S.T. Yau, On inequality between Chern numbers of singular Kähler surfaces and characterization of orbit space of discrete group of SU(2,1), Cont. Math. 49 (1986) 31-43.
\item[] [6] S.Y. Cheng and S.T. Yau, On the existence of a complete Kähler metric on noncompact complex manifolds and the regularity of Fefferman's equation., Comm. Pure Appl. Math. no. 433 (1980), 507-544.
\item[] [7] S.Y. Cheng and S.T. Yau, The real Monge-Ampère equation and affine flat structures., Chern S, ed. Proc. 1980 Beijing Sympos. Diff. Geom. Diff. Eq., Vol. 1 (1982), 339-370.
\item[] [8] K. Fukaya, Hausdorff convergence of Riemannian manifolds and its applications., in Recent topics in differential and analytic geometry, Adv. Stud. Pure Math., 18-I, Academic Press, (1990), 143-238.
\end{itemize}
[9] K. Fukaya, Multivalued Morse theory, asymptotic analysis and mirror symmetry., in Graphs and patterns in mathematics and theoretical physics, Proc. Sympos. Pure Math., 73, Amer. Math. Soc., (2005), 205-278.
[10] W. Fulton, Introduction to toric varieties, Annals of Mathematics Studies 131, Princeton University Press, 1993.
[11] D. Gilbarg, N.S. Trudinger, Elliptic partial differential equations of second order, Springer 1983.
[12] M. Gromov, Metric structures for Riemannian and non-Riemannian spaces, Birkhäuser 1999.
[13] M. Gross, Mirror symmetry and the Strominger-Yau-Zaslow conjecture, in Current developments in mathematics 2012, 133-191, Int. Press, Somerville, MA, 2013.
[14] M. Gross, D. Huybrechts, D. Joyce, Calabi-Yau manifolds and related geometries, Universitext, Springer, Berlin, 2003.
[15] M. Gross, V. Tosatti, Y. Zhang, Collapsing of Abelian Fibred Calabi-Yau Manifolds, Duke Math. J. 162 (2013), 517-551.
[16] M. Gross, V. Tosatti, Y. Zhang, Gromov-Hausdorff collapsing of Calabi-Yau manifolds, arXiv:1304.1820, to appear in Comm. Anal. Geom.
[17] M. Gross, P.M.H. Wilson, Large complex structure limits of K3 surfaces, J. Diff. Geom. 55 (2000), 475-546.
[18] R. Hildebrand, Canonical Barriers on Convex Cones, Mathematics of Operations Research, Vol. 39, no. 3, (2014), 841-850.
[19] N. Leung, P. Lu, Degeneration of Kähler Einstein metrics on complete Kähler manifolds, Comm. Analysis and Geom. 7 (1999), 431-449.
[20] N. Leung, T. Wan, Calabi-Yau components in general type hypersurfaces, J. Differential Geometry, 83 (2009), 43-74.
[21] G. Kempf, F. Knudsen, D. Mumford, B. Saint-Donat, Toroidal Embeddings I, Lecture Notes in Mathematics 339, Springer-Verlag 1973.
[22] R. Kobayashi, Kähler-Einstein metric on an open algebraic manifolds, Osaka J. Math. 21 (1984), 399-418.
[23] J. Kollár, Moduli of varieties of general type, in Handbook of Moduli, Volume II, Adv. Lec. Math. 25, Int. Press, (2013), 131-157.
[24] J. Kollár, Simple normal crossing varieties with prescribed dual complex, Algebr. Geom. 1 no. 1, (2014), 57-68.
[25] M. Kontsevich, Y. Soibelman, Homological mirror symmetry and torus fibrations , in Symplectic geometry and mirror symmetry, World Sci. Publishing, (2001), 203-263.
[26] M. Kontsevich, Y. Soibelman, Affine Structures and Non-Archimedean Analytic Spaces, in The Unity of Mathematics, Progress in Mathematics Volume 244, Springer, (2006), 321-385.
[27] G. Mikhalkin, Decomposition into pairs-of-pants for complex algebraic hypersurfaces, Topology, 43 (2004), 1035-1065.
[28] Y. Odaka, Tropically Compactify Moduli via Gromov-Hausdorff Collapsing, arXiv:1406.7772 v1.
[29] W.-D. Ruan, Degeneration of Kähler-Einstein Manifolds I: The Normal Crossing Case, Commun. Contemp. Math. 6 no. 2, (2004), 301-313.
[30] W.-D. Ruan, Degeneration of Kähler-Einstein manifolds. II. The toroidal case, Comm. Anal. Geom. 14 no. 1, (2006), 1-24.
[31] W.-D. Ruan, Generalized special Lagrangian torus fibration for Calabi-Yau hypersurfaces in toric varieties. I., Commun. Contemp. Math. 9 (2007), 201-216.
[32] W.-D. Ruan, Degeneration of Kähler-Einstein hypersurfaces in complex torus to generalized pair of pants decomposition , arXiv:math/0311098
[33] Y.T. Siu, Lectures on Hermitian-Einstein metrics for stable bundles and Kähler-Einstein metrics., DMV Seminar, 8. Birkhäuser Verlag, Basel, 1987.
[34] J. Song, Riemannian geometry of Kähler-Einstein currents, arXiv:1404.0445.
\begin{itemize}
\item[] [35] A. Strominger, S.T. Yau, E. Zaslow, Mirror symmetry is $T$-duality, Nuclear Physics B, Vol. 479, (1996), 243-259.
\item[] [36] G. Tian, Degeneration of Kähler-Einstein manifolds I, in Differential geometry: geometry in mathematical physics and related topics, Proc. Sympos. Pure Math., 54, Part 2, (1993), 595-609.
\item[] [37] G. Tian, S.T. Yau, Existence of Kähler-Einstein metrics on complete Kähler manifolds and their applications to algebraic geometry, In Mathematical Aspects of String Theory ed. S.T. Yau, World Scientific Publishing, (1987), 574-628.
\item[] [38] V. Tosatti, Families of Calabi-Yau Manifolds and Canonical Singularities, arXiv:1311.4845, to appear in International Mathematics Research Notices.
\item[] [39] E. Viehweg, Quasi-projective moduli for polarized manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete, Vol. 30, Springer-Verlag, (1995).
\item[] [40] S.T. Yau, On the Ricci curvature of a compact Kähler manifold and complex Monge-Ampère equation I, Comm. Pure Appl. Math. 31 (1978), 339-411.
\item[] [41] Y. Zhang, Completion of the moduli space for polarized Calabi-Yau manifolds, arXiv:1410.2979, to appear in J. Diff. Geom.
\end{itemize}

Yau Mathematical Sciences Center, Tsinghua University, Beijing 100084, P.R.China.
E-mail address: yuguangzhang76@yahoo.com