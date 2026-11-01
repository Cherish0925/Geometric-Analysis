---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Gluing Eguchi-Hanson metrics and a question of Page]

---
source_file: 1405_0056.pdf
converter: mathpix
format: mmd
---

\title{
GLUING EGUCHI-HANSON METRICS AND A QUESTION OF PAGE
}

\author{
SIMON BRENDLE AND NIKOLAOS KAPOULEAS
}

\begin{abstract}
In 1978, Gibbons-Pope and Page proposed a physical picture for the Ricci flat Kähler metrics on the K3 surface based on a gluing construction. In this construction, one starts from a flat torus with 16 orbifold points, and resolves the orbifold singularities by gluing in 16 small Eguchi-Hanson manifolds which all have the same orientation. This construction was carried out rigorously by Topiwala, LeBrunSinger, and Donaldson.

In 1981, Page asked whether the above construction can be modified by reversing the orientations of some of the Eguchi-Hanson manifolds. This is a subtle question: if successful, this construction would produce Einstein metrics which are neither Kähler nor self-dual.

In this paper, we focus on a configuration of maximal symmetry involving 8 small Eguchi-Hanson manifolds of each orientation which are arranged according to a chessboard pattern. By analyzing the interactions between Eguchi-Hanson manifolds with opposite orientation, we identify a non-vanishing obstruction to the gluing problem, thereby destroying any hope of producing a metric of zero Ricci curvature in this way. Using this obstruction, we are able to understand the dynamics of such metrics under Ricci flow as long as the Eguchi-Hanson manifolds remain small. In particular, for the configuration described above, we obtain an ancient solution to the Ricci flow with the property that the maximum of the Riemann curvature tensor blows up at a rate of $(-t)^{\frac{1}{2}}$, while the maximum of the Ricci curvature converges to 0.
\end{abstract}

\section*{1. Introduction}

Gluing techniques are a central tool for constructing solutions of nonlinear partial differential equations. In a first step, one constructs an approximate solution of the given partial differential equation by gluing together. In the next step, one tries to deform this approximate solution to an exact solution using the implicit function theorem. This method has been used to construct solutions of many nonlinear elliptic equations arising in differential geometry (see e.g. [2], [3], [6], [8], [19], [23], [24], [25], [26], [28], [27], [30], [31], [36], [39], [40]).

In this paper, we consider a gluing problem for the Einstein equations and their parabolic analogue, the Ricci flow (cf. [20], [21], [22]; see also [9]). Our

\footnotetext{
The first author was supported in part by the National Science Foundation under grants DMS-0905628 and DMS-1201924. The second author was supported in part by the National Science Foundation under grant DMS-1105371.
}
starting point is the torus $\mathbb{R}^{4} /(2 \mathbb{Z})^{4}$ equipped with the flat metric. After identifying each point on $\mathbb{R}^{4} /(2 \mathbb{Z})^{4}$ with its image under antipodal reflection, we obtain a flat orbifold with 16 singular points. We may desingularize this orbifold by gluing in an Eguchi-Hanson manifold at each of the 16 singular points. Recall that the Eguchi-Hanson manifold is a smooth, Ricci flat Kähler manifold. The Eguchi-Hanson metric on the complement of a twosphere can be written in coordinates as
$$g_{\mathrm{eh}, \varepsilon}=\frac{r^{2}}{\left(\varepsilon^{4}+r^{4}\right)^{\frac{1}{2}}}\left(d r \otimes d r+r^{2} \alpha_{1} \otimes \alpha_{1}\right)+\left(\varepsilon^{4}+r^{4}\right)^{\frac{1}{2}}\left(\alpha_{2} \otimes \alpha_{2}+\alpha_{3} \otimes \alpha_{3}\right) .$$
Here, $r$ denotes the radial coordinate, $\alpha_{1}, \alpha_{2}, \alpha_{3}$ is a suitable set of one-forms on $S^{3}$, and $\varepsilon$ is a scaling parameter. An important point is that the EguchiHanson manifold is asymptotic to $\mathbb{R}^{4} / \mathbb{Z}_{2}$ near infinity. Thus, inserting an Eguchi-Hanson at each orbifold point will result in a smooth manifold. Since the torus and the Eguchi-Hanson are all Ricci flat, the resulting manifold admits a metric which is almost Ricci flat.

The key issue is whether this approximate solution of the Einstein equation can be deformed to an exact one. It turns out that the choice of orientation of the 16 Eguchi-Hanson manifolds plays a crucial role. In the special case when the 16 Eguchi-Hanson manifolds all have the same orientation, Gibbons and Pope [18] and Page [32] suggested that this gluing construction should recover the Ricci flat Kähler metric on the K3 surface. Rigorous proofs of this fact were given by Topiwala [41], [42], LeBrun and Singer [29], and Donaldson [16]. An important point here is that one can work within the class of Kähler manifolds. Thus, the problem of finding a Ricci flat metric can be reduced to the solvability of a Monge-Ampère-type equation. This construction also shares some common features with Joyce's construction of manifolds with exceptional holonomy (cf. [23]).

In the following, we consider a gluing construction involving EguchiHanson manifolds with different orientations. Such a construction was first proposed by Page [33] in 1981. One major difficulty in this case is that the resulting metric will not be Kähler, and it is necessary to work with the full Einstein equations. For simplicity, we consider a particularly symmetric configuration involving 8 Eguchi-Hanson manifolds with positive orientation and 8 Eguchi-Hanson manifolds of negative orientation, where the orientations are assigned according to a checkboard pattern. It turns out that, modulo symmetries, the approximate kernel of the linearized operator is two-dimensional. From a geometric point of view, the approximate kernel reflects the freedom to change the scaling parameter $\varepsilon$ of the Eguchi-Hanson metrics and the size of the flat metric on the torus. The crucial issue then is to analyze the projection of the Ricci tensor to the approximate kernel. It turns out that this projection is non-zero, due to interactions between Eguchi-Hanson metrics with opposite orientations. These interactions have the effect of increasing the size of the Eguchi-Hanson metrics when the metric is evolved by the Ricci flow. In fact, a formal calculation suggests that,
under the Ricci flow, the scale parameter $\varepsilon$ should evolve according to the equation $\frac{d}{d t} \varepsilon=8 \omega \varepsilon^{5}+o\left(\varepsilon^{5}\right)$, where $\omega$ is a positive constant defined in Proposition 4.2. This is reminiscent of the work of Struwe [37] on the heat flow for the Nirenberg problem.

In light of this obstruction, we cannot expect to deform the metric to one of zero Ricci curvature. Instead, we show that this setup leads to a non-trivial ancient solution to the Ricci flow:

Theorem 1.1. There exists a compact ancient solution to the Ricci flow in dimension 4 with the following property. For $-t$ sufficiently large, the manifold can be viewed as a desingularization of a flat torus with 16 orbifold points. More precisely, we divide the 16 orbifold points into two classes according to a checkboard pattern. Near 8 orbifold points, the metric is a small perturbation of a positively-oriented near the remaining 8 orbifold points, the metric is a small perturbation of a negatively-oriented Eguchi-Hanson metric. As $t \rightarrow-\infty$, the size of the Eguchi-Hanson instantons shrinks to zero, and we have $\sup \left|\operatorname{Rm}_{g(t)}\right|_{g(t)}=(c+o(1))(-t)^{\frac{1}{2}}$, where $c$ is a positive constant. Finally, the Ricci curvature of $g(t)$ satisfies sup $\left|\operatorname{Ric}_{g(t)}\right|_{g(t)}=O\left((-t)^{-\frac{1}{2}+\kappa}\right)$ as $t \rightarrow-\infty$, where $\kappa>0$ can be chosen arbitrarily small.

Ancient solutions play a crucial role as singularity models for the Ricci flow; see e.g. [22], [34], and [35]. It is an interesting question to classify ancient solutions and Ricci solitons. We refer to [10], [11], [12], [14] for some recent progress in this direction.

An interesting open question is what happens to our ancient solution beyond the range of sufficiently large $-t$. Another interesting observation is that if we consider less symmetric configurations we can construct metrics by gluing 16 small Eguchi-Hanson metrics on the orbifold as before, which under the Ricci flow evolve so that one of the Eguchi-Hanson metrics becomes extinct by shrinking to zero size, while the rest stay close to fixed nonzero sizes. This construction will appear elsewhere.

Theorem 1.1 is inspired in part by the remarkable recent work of Biquard. In [5], Biquard glued an Eguchi-Hanson manifold to a given Einstein orbifold. The resulting metric is an approximate solution of the Einstein equation. Biquard found an obstruction involving the curvature of the background orbifold which, in general, prevents one from deforming this metric to an exact solution of the Einstein equation. This result can be viewed as converse of the compactness results of Anderson [1] and Bando, Kasue, and Nakajima [4] (see also the survey paper [13]). We note that Biquard's obstruction vanishes in our situation, as the background orbifold is a flat torus. For that reason, we need to perform a more precise calculation which takes into account the interactions between different Eguchi-Hanson manifolds. Note that the construction and proof are modelled after a gluing construction for an elliptic problem: We first construct an approximate ancient solution and then we prove that it can be perturbed to an exact one by
carefully estimating the error terms and applying the Schauder fixed point theorem.

Theorem 1.1 also shares some common features with the beautiful work of Daskalopoulos, del Pino, and Šešum [15] on the Yamabe flow. The main result in [15] asserts that there exists a non-trivial ancient solution to the Yamabe flow which is conformally flat and looks like two spheres joined by a small neck when $-t$ is large.

We also note that Takahashi [38] has recently constructed an ancient solution to the Ricci flat which converges smoothly to the Euclidean Schwarzschild metric as $t \rightarrow-\infty$. In particular, this solution has uniformly bounded curvature as $t \rightarrow-\infty$, whereas the solution in Theorem 1.1 has unbounded curvature.

The authors are very grateful to Professors Olivier Biquard and András Vasy for helpful discussions.

\section*{2. Basic properties of the Eguchi-Hanson metric}

In this section, we review the definition of the Eguchi-Hanson metric (cf. [5], [17]). As in [5], we define one-forms $\alpha_{1}, \alpha_{2}, \alpha_{3}$ on $\mathbb{R}^{4} \backslash\{0\}$ by
$$\begin{aligned}
& \alpha_{1}=\frac{1}{r^{2}}\left(x_{1} d x_{2}-x_{2} d x_{1}+x_{3} d x_{4}-x_{4} d x_{3}\right) \\
& \alpha_{2}=\frac{1}{r^{2}}\left(x_{1} d x_{3}-x_{3} d x_{1}+x_{4} d x_{2}-x_{2} d x_{4}\right) \\
& \alpha_{3}=\frac{1}{r^{2}}\left(x_{1} d x_{4}-x_{4} d x_{1}+x_{2} d x_{3}-x_{3} d x_{2}\right)
\end{aligned}$$
The Eguchi-Hanson metric with parameter $\varepsilon>0$ is defined by
$$g_{\mathrm{eh}, \varepsilon}=\frac{r^{2}}{\left(\varepsilon^{4}+r^{4}\right)^{\frac{1}{2}}}\left(d r \otimes d r+r^{2} \alpha_{1} \otimes \alpha_{1}\right)+\left(\varepsilon^{4}+r^{4}\right)^{\frac{1}{2}}\left(\alpha_{2} \otimes \alpha_{2}+\alpha_{3} \otimes \alpha_{3}\right) .$$
This defines a Ricci flat metric on $\mathbb{R}^{4} \backslash\{0\}$ which is invariant under antipodal reflection. The induced metric on $\left(\mathbb{R}^{4} \backslash\{0\}\right) / \mathbb{Z}_{2}$ admits a smooth compactification, where the origin is replaced by a two-dimensional sphere. The parameter $\varepsilon$ serves as a scaling parameter; that is, different choices of $\varepsilon$ result in metrics which are isometric up to scaling.

Let $\hat{g}_{\text {eh }, \varepsilon}$ denote the pull-back of $g_{\text {eh }, \varepsilon}$ under the map $\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto$ $\left(-x_{1}, x_{2}, x_{3}, x_{4}\right)$. Clearly, $\hat{g}_{\mathrm{eh}, \varepsilon}$ is a Ricci flat metric. Near infinity, we have the asymptotic expansions
$$g_{\mathrm{eh}, \varepsilon}=g_{\mathrm{eucl}}+\frac{1}{2} \varepsilon^{4} T+O\left(\varepsilon^{8} r^{-8}\right)$$
and
$$\hat{g}_{\mathrm{eh}, \varepsilon}=g_{\mathrm{eucl}}+\frac{1}{2} \varepsilon^{4} \hat{T}+O\left(\varepsilon^{8} r^{-8}\right),$$
where
$$\begin{aligned}
T=- & r^{-4}\left(d r \otimes d r+r^{2} \alpha_{1} \otimes \alpha_{1}-r^{2} \alpha_{2} \otimes \alpha_{2}-r^{2} \alpha_{3} \otimes \alpha_{3}\right) \\
=- & r^{-6}\left(\left(x_{1}^{2}+x_{2}^{2}-x_{3}^{2}-x_{4}^{2}\right)\left(d x_{1} \otimes d x_{1}+d x_{2} \otimes d x_{2}-d x_{3} \otimes d x_{3}-d x_{4} \otimes d x_{4}\right)\right. \\
& \quad+2\left(x_{1} x_{3}+x_{2} x_{4}\right)\left(d x_{1} \otimes d x_{3}+d x_{3} \otimes d x_{1}+d x_{2} \otimes d x_{4}+d x_{4} \otimes d x_{2}\right) \\
& \left.\quad+2\left(x_{1} x_{4}-x_{2} x_{3}\right)\left(d x_{1} \otimes d x_{4}+d x_{4} \otimes d x_{1}-d x_{2} \otimes d x_{3}-d x_{3} \otimes d x_{2}\right)\right)
\end{aligned}$$
and
$$\begin{aligned}
\hat{T}=-r^{-6}(( & \left.x_{1}^{2}+x_{2}^{2}-x_{3}^{2}-x_{4}^{2}\right)\left(d x_{1} \otimes d x_{1}+d x_{2} \otimes d x_{2}-d x_{3} \otimes d x_{3}-d x_{4} \otimes d x_{4}\right) \\
& +2\left(x_{1} x_{3}-x_{2} x_{4}\right)\left(d x_{1} \otimes d x_{3}+d x_{3} \otimes d x_{1}-d x_{2} \otimes d x_{4}-d x_{4} \otimes d x_{2}\right) \\
& \left.+2\left(x_{1} x_{4}+x_{2} x_{3}\right)\left(d x_{1} \otimes d x_{4}+d x_{4} \otimes d x_{1}+d x_{2} \otimes d x_{3}+d x_{3} \otimes d x_{2}\right)\right) .
\end{aligned}$$
We note that the metrics $g_{\text {eh }, \varepsilon}$ and $\hat{g}_{\text {eh }, \varepsilon}$ and the tensors $T$ and $\hat{T}$ are all invariant under the maps
$$\begin{aligned}
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{2},-x_{1}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{4},-x_{3}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{3}, x_{4}, x_{1}, x_{2}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(-x_{3}, x_{4},-x_{1}, x_{2}\right) .
\end{aligned}$$

In the remainder of this section, we review some known results, due to Biquard [5] and Page [32], concerning the Lichnerowicz Laplacian for the Eguchi-Hanson manifold. Recall that the Lichnerowicz Laplacian is defined by
$$\Delta_{L} h_{i k}=\Delta h_{i k}+2 R_{i j k l} h^{j l}-\operatorname{Ric}_{i}^{l} h_{k l}-\operatorname{Ric}_{k}^{l} h_{i l} .$$
To analyze the kernel of $\Delta_{L, g_{\mathrm{eh}}}$, we consider the vector fields
$$\begin{aligned}
& V_{1}=x_{1} \frac{\partial}{\partial x_{2}}-x_{2} \frac{\partial}{\partial x_{1}}+x_{3} \frac{\partial}{\partial x_{4}}-x_{4} \frac{\partial}{\partial x_{3}}, \\
& V_{2}=x_{1} \frac{\partial}{\partial x_{3}}-x_{3} \frac{\partial}{\partial x_{1}}+x_{4} \frac{\partial}{\partial x_{2}}-x_{2} \frac{\partial}{\partial x_{4}}, \\
& V_{3}=x_{1} \frac{\partial}{\partial x_{4}}-x_{4} \frac{\partial}{\partial x_{1}}+x_{2} \frac{\partial}{\partial x_{3}}-x_{3} \frac{\partial}{\partial x_{2}} .
\end{aligned}$$
Note that the frame $r \frac{\partial}{\partial r}, V_{1}, V_{2}, V_{3}$ is dual to the co-frame $\frac{1}{r} d r, \alpha_{1}, \alpha_{2}, \alpha_{3}$. Moreover, $\left[V_{1}, V_{2}\right]=-2 V_{3},\left[V_{2}, V_{3}\right]=-2 V_{1}$, and $\left[V_{3}, V_{1}\right]=-2 V_{2}$. This implies $\mathscr{L}_{V_{1}} \alpha_{2}=-\mathscr{L}_{V_{2}} \alpha_{1}=-2 \alpha_{3}, \mathscr{L}_{V_{2}} \alpha_{3}=-\mathscr{L}_{V_{3}} \alpha_{2}=-2 \alpha_{1}$, and $\mathscr{L}_{V_{3}} \alpha_{1}=-\mathscr{L}_{V_{1}} \alpha_{3}=-2 \alpha_{2}$. We next define
$$\begin{aligned}
& o_{1, \varepsilon}=g_{\mathrm{eh}, \varepsilon}-\frac{1}{2} \mathscr{L}_{r \frac{\partial}{\partial r}} g_{\mathrm{eh}, \varepsilon}, \\
& o_{2, \varepsilon}=\frac{1}{2} \mathscr{L}_{\frac{r^{2} V_{2}}{\sqrt{\varepsilon^{4}+r^{4}}}} g_{\mathrm{eh}, \varepsilon} \\
& o_{3, \varepsilon}=\frac{1}{2} \mathscr{L}_{\frac{r^{2} V_{3}}{\sqrt{\varepsilon^{4}+r^{4}}}} g_{\mathrm{eh}, \varepsilon}
\end{aligned}$$
Equivalently, we may write
$$\begin{aligned}
& o_{1, \varepsilon}=-\frac{\varepsilon^{4} r^{2}}{\left(\varepsilon^{4}+r^{4}\right)^{\frac{3}{2}}}\left(d r \otimes d r+r^{2} \alpha_{1} \otimes \alpha_{1}\right)+\frac{\varepsilon^{4}}{\left(\varepsilon^{4}+r^{4}\right)^{\frac{1}{2}}}\left(\alpha_{2} \otimes \alpha_{2}+\alpha_{3} \otimes \alpha_{3}\right), \\
& o_{2, \varepsilon}=\frac{\varepsilon^{4}}{\varepsilon^{4}+r^{4}}\left(r d r \otimes \alpha_{2}+r \alpha_{2} \otimes d r-r^{2} \alpha_{1} \otimes \alpha_{3}-r^{2} \alpha_{3} \otimes \alpha_{1}\right), \\
& o_{3, \varepsilon}=\frac{\varepsilon^{4}}{\varepsilon^{4}+r^{4}}\left(r d r \otimes \alpha_{3}+r \alpha_{3} \otimes d r+r^{2} \alpha_{1} \otimes \alpha_{2}+r^{2} \alpha_{2} \otimes \alpha_{1}\right) .
\end{aligned}$$
Finally, the tensor $o_{1, \varepsilon}$ can be rewritten as
$$o_{1, \varepsilon}=\frac{1}{2} \varepsilon \frac{\partial}{\partial \varepsilon} g_{\mathrm{eh}, \varepsilon}=\varepsilon^{4} T+O\left(\varepsilon^{8} r^{-8}\right) .$$
The main properties of $o_{1, \varepsilon}, o_{2, \varepsilon}, o_{3, \varepsilon}$ are summarized in the following proposition.

Proposition 2.1 (O. Biquard [5]; D. Page [32]). For each $i \in\{1,2,3\}$, the tensor $o_{i, \varepsilon}$ has the following properties:
\begin{itemize}
\item[(i)] $\operatorname{tr}_{g_{\mathrm{eh}, \varepsilon}} o_{i, \varepsilon}=0$.
\item[(ii)] $\operatorname{div}_{g_{\mathrm{eh}, \varepsilon}} o_{i, \varepsilon}=0$.
\item[(iii)] $\Delta_{L, g_{\mathrm{eh}, \varepsilon}} o_{i, \varepsilon}=0$.
\item[(iv)] $\int_{\mathbb{R}^{4} \backslash\{0\}}\left|o_{1, \varepsilon}\right|_{g_{\mathrm{eh}, \varepsilon}}^{2} d \mathrm{vol}_{g_{\mathrm{eh}, \varepsilon}}=2 \pi^{2} \varepsilon^{4}$.
\end{itemize}

Proof. (i) It is obvious that $o_{i, \varepsilon}$ is trace-free for each $i \in\{1,2,3\}$.
\begin{itemize}
\item[(ii)] We first consider the vector field $Y=r \frac{\partial}{\partial r}$. Since $o_{1, \varepsilon}=g_{\mathrm{eh}, \varepsilon}-$ $\frac{1}{2} \mathscr{L}_{Y} g_{\mathrm{eh}, \varepsilon}$ is trace-free, we have $\sum_{k} D_{k} Y^{k}=4$ since $o_{1, \varepsilon}$ is trace-free. Moreover, $D_{k} Y_{l}-D_{l} Y_{k}=0$ since $Y$ is a gradient vector field. Differentiating this identity gives $\sum_{k} D^{k}\left(D_{k} Y_{l}-D_{l} Y_{k}\right)=0$. Therefore, we obtain
$$\sum_{k} D^{k}\left(D_{k} Y_{l}+D_{l} Y_{k}\right)=\sum_{k} D^{k}\left(D_{k} Y_{l}-D_{l} Y_{k}\right)+2 \sum_{k} D_{l} D^{k} Y_{k}=0 .$$
Consequently, $o_{1, \varepsilon}=g_{\mathrm{eh}, \varepsilon}-\frac{1}{2} \mathscr{L}_{Y} g_{\mathrm{eh}, \varepsilon}$ is divergence-free.
\end{itemize}

In the next step, we define $Z=\frac{r^{2} V_{2}}{\sqrt{\varepsilon^{4}+r^{4}}}$. Since $o_{2, \varepsilon}=\frac{1}{2} \mathscr{L}_{Z} g_{\text {eh }, \varepsilon}$ is tracefree, we have $\sum_{k} D_{k} Z^{k}=0$ since $o_{2, \varepsilon}$. We next observe that $d\left(r^{2} \alpha_{2}\right)=$ $2 r d r \wedge \alpha_{2}+2 r^{2} \alpha_{3} \wedge \alpha_{1}$ is a closed two-form which is self-dual with respect to the metric $g_{\mathrm{eh}, \varepsilon}$. Consequently, the two-form $d\left(r^{2} \alpha_{2}\right)$ is divergence-free
with respect to the metric $g_{\mathrm{eh}, \varepsilon}$. Since $g_{\mathrm{eh}, \varepsilon}(Z, \cdot)=r^{2} \alpha_{2}$, we conclude that $\sum_{k} D^{k}\left(D_{k} Z_{l}-D_{l} Z_{k}\right)=0$. Putting these facts together, we obtain
$$\sum_{k} D^{k}\left(D_{k} Z_{l}+D_{l} Z_{k}\right)=\sum_{k} D^{k}\left(D_{k} Z_{l}-D_{l} Z_{k}\right)+2 \sum_{k} D_{l} D^{k} Z_{k}=0 .$$
Thus, $o_{2, \varepsilon}=\frac{1}{2} \mathscr{L}_{Z} g_{\text {eh }, \varepsilon}$ is divergence-free. An analogous argument shows that $o_{3, \varepsilon}$ is divergence-free.
(iii) Clearly, $o_{i, \varepsilon}$ lies in the kernel of the linearized Einstein operator for each $i \in\{1,2,3\}$. Since $o_{i, \varepsilon}$ is trace-free and divergence-free, we conclude that $\Delta_{L, g_{\mathrm{eh}, \varepsilon}} o_{i, \varepsilon}=0$ for each $i \in\{1,2,3\}$.
(iv) Note that
$$\left|o_{1, \varepsilon}\right|_{g_{\mathrm{eh}, \varepsilon}}^{2}=4\left(\frac{\varepsilon^{4}}{\varepsilon^{4}+r^{4}}\right)^{2} .$$
This implies
$$\int_{\mathbb{R}^{4} \backslash\{0\}}\left|o_{1, \varepsilon}\right|_{g_{\mathrm{eh}, \varepsilon}}^{2} d \operatorname{vol}_{g_{\mathrm{eh}, \varepsilon}}=\int_{0}^{\infty} 4\left(\frac{\varepsilon^{4}}{\varepsilon^{4}+r^{4}}\right)^{2} \cdot 2 \pi^{2} r^{3} d r=2 \pi^{2} \varepsilon^{4}$$
This completes the proof of Proposition 2.1. \(\square\)

\section*{3. Attaching Eguchi-Hanson metrics to a torus with 16 ORBIFOLD POINTS}

In this section, we will attach Eguchi-Hanson metrics with different orientations to a torus with 16 orbifold points. To fix notation, we denote by $\mathscr{C}$ the collection of maps
$$\begin{aligned}
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{2},-x_{1}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{4},-x_{3}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{3}, x_{4}, x_{1}, x_{2}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(-x_{3}, x_{4},-x_{1}, x_{2}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(1-x_{1}, x_{2}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, 1-x_{2}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, 1-x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{3}, 1-x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}+2, x_{2}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}+2, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{3}+2, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{3}, x_{4}+2\right),
\end{aligned}$$
and by $\mathscr{G}$ the group generated by $\mathscr{C}$.
For each $a \in \mathbb{Z}^{4}$, we denote by $\tau_{a}$ the translation $x \mapsto x-a$. Moreover, we put
$$\mathbb{Z}_{\text {even }}^{4}=\left\{\left(a_{1}, a_{2}, a_{3}, a_{4}\right) \in \mathbb{Z}^{4}: a_{1}+a_{2}+a_{3}+a_{4} \text { is even }\right\}$$
and
$$\mathbb{Z}_{\text {odd }}^{4}=\left\{\left(a_{1}, a_{2}, a_{3}, a_{4}\right) \in \mathbb{Z}^{4}: a_{1}+a_{2}+a_{3}+a_{4} \text { is odd }\right\} .$$

Lemma 3.1. The limits
$$\sum_{a \in \mathbb{Z}_{\text {even }}^{4}} \tau_{a}^{*} T:=\lim _{N \rightarrow \infty} \sum_{a \in \mathbb{Z}_{\text {even }}^{4}, \max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|,\left|a_{4}\right|\right\}<N} \tau_{a}^{*} T$$
and
$$\sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} \tau_{a}^{*} \hat{T}:=\lim _{N \rightarrow \infty} \sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}, \max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|,\left|a_{4}\right|\right\}<N} \tau_{a}^{*} \hat{T}$$
exist for $x \in \mathbb{R}^{4} \backslash \mathbb{Z}^{4}$. Neither series converges absolutely.
Proof. Fix a point $x \in \mathbb{R}^{4} \backslash \mathbb{Z}^{4}$. It is easy to see that
$$\tau_{\left(a_{1}, a_{2}, a_{3}, a_{4}\right)}^{*} T(x)+\tau_{\left(a_{3},-a_{4},-a_{1}, a_{2}\right)}^{*} T(x)=O\left(|a|^{-5}\right)$$
as $|a| \rightarrow \infty$. Similarly, we have
$$\tau_{\left(a_{1}, a_{2}, a_{3}, a_{4}\right)}^{*} \hat{T}(x)+\tau_{\left(a_{3}, a_{4},-a_{1},-a_{2}\right)}^{*} \hat{T}(x)=O\left(|a|^{-5}\right)$$
as $|a| \rightarrow \infty$ for each point $x \in\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}$. From this, we deduce that
$$\left|\sum_{a \in \mathbb{Z}_{\mathrm{ven}}^{4}, N \leq \max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|,\left|a_{4}\right|\right\}<2 N} \tau_{a}^{*} T(x)\right| \leq O\left(N^{-1}\right)$$
and
$$\left|\sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}, N \leq \max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|,\left|a_{4}\right|\right\}<2 N} \tau_{a}^{*} \hat{T}(x)\right| \leq O\left(N^{-1}\right)$$
for $N<N^{\prime}$. From this, the assertion follows. \(\square\)

Lemma 3.2. The tensor
$$\sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4}} \tau_{a}^{*} T+\sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} \tau_{a}^{*} \hat{T}$$
on $\mathbb{R}^{4} \backslash \mathbb{Z}^{4}$ is invariant under the group $\mathscr{G}$ defined above.
Proof. Consider the partial sums
$$S^{(N)}:=\sum_{a \in \mathbb{Z}_{\text {even }}^{4}, \max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|,\left|a_{4}\right|\right\}<N} \tau_{a}^{*} T+\sum_{a \in \mathbb{Z}_{\text {odd }}^{4}, \max \left\{\left|a_{1}\right|,\left|a_{2}\right|,\left|a_{3}\right|,\left|a_{4}\right|\right\}<N} \tau_{a}^{*} \hat{T} .$$
If we fix a point $x \in \mathbb{R}^{4} \backslash \mathbb{Z}^{4}$ and a $\operatorname{map} \varphi \in \mathscr{C}$, then we have $\varphi^{*} S^{(N)}-S^{(N)}=$ $O\left(N^{-1}\right)$ at the point $x$. Hence, the limit $\lim _{N \rightarrow \infty} S^{(N)}$ is invariant under each map $\varphi \in \mathscr{C}$. \(\square\)

Definition 3.3. Given two positive numbers $\varepsilon$ and $\delta$ such that $\varepsilon \ll \delta^{4} \ll 1$, we define a metric $\bar{g}_{\varepsilon, \delta}$ on the cube $\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}$ in the following way: For $|x| \leq \frac{1}{2} \delta$, we define
$$\bar{g}_{\varepsilon, \delta}=g_{\mathrm{eh}, \varepsilon} .$$

Moreover, for $|x| \geq \delta$, we put
$$\bar{g}_{\varepsilon, \delta}=g_{\mathrm{eucl}}+\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4}} \tau_{a}^{*} T+\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} \tau_{a}^{*} \hat{T} .$$
Finally, in the intermediate region $\frac{1}{2} \delta \leq|x| \leq \delta$, we define
$$\bar{g}_{\varepsilon, \delta}=(1-\chi(|x| / \delta)) g_{\mathrm{eh}, \varepsilon}+\chi(|x| / \delta)\left(g_{\mathrm{eucl}}+\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4}} \tau_{a}^{*} T+\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} \tau_{a}^{*} T\right),$$
where $\chi$ is a cutoff function satisfying $\chi=0$ on $\left(-\infty, \frac{2}{3}\right]$ and $\chi=0$ on $\left[\frac{5}{6}, \infty\right)$.

We may extend $\bar{g}_{\varepsilon, \delta}$ to a metric on $\mathbb{R}^{4} \backslash \mathbb{Z}^{4}$ which is invariant under the group $\mathscr{G}$ defined above. Note that the resulting metric $\bar{g}_{\varepsilon, \delta}$ on $\mathbb{R}^{4} \backslash \mathbb{Z}^{4}$ is singular at each lattice point. In fact, if $a \in \mathbb{Z}_{\text {even }}^{4}$, then we have $\bar{g}_{\varepsilon, \delta}=\tau_{a}^{*} g_{\text {eh, } \varepsilon}$ in a neighborhood of $a$. Similarly, if $a \in \mathbb{Z}_{\mathrm{odd}}^{4}$, then we have $\bar{g}_{\varepsilon, \delta}=\tau_{a}^{*} \hat{g}_{\mathrm{eh}, \varepsilon}$ in a neighborhood of $a$. Thus, if we take the quotient by translations and antipodal reflection, then the metric $\bar{g}_{\varepsilon, \delta}$ descends to a smooth metric on the quotient manifold $M$.

We next estimate the Ricci curvature of $\bar{g}_{\varepsilon, \delta}$.
Proposition 3.4. We have
$$\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}=0$$
for $|x| \leq \frac{1}{2} \delta$. Moreover, we have
$$\left|\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right| \leq C \varepsilon^{4} \delta^{-2}$$
for $\frac{1}{2} \delta \leq|x| \leq \delta$ and
$$\left|\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right| \leq C \varepsilon^{8}|x|^{-10}$$
for $|x| \geq \delta$. Analogous estimates hold for the derivatives of $\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}$.
Proof. Straightforward calculation. \(\square\)

Finally, let us denote by $\bar{o}_{1, \varepsilon, \delta}$ the trace-free part of the tensor $\frac{1}{2} \varepsilon \frac{\partial}{\partial \varepsilon} \bar{g}_{\varepsilon, \delta}$ with respect to the metric $\bar{g}_{\varepsilon, \delta}$. Clearly, $\bar{o}_{1, \varepsilon, \delta}=o_{1, \varepsilon}$ for $|x| \leq \frac{1}{2} \delta$, so we can think of $\bar{o}_{1, \varepsilon, \delta}$ as an extension of $o_{1, \varepsilon}$ to the manifold $M$.
Proposition 3.5. We have
$$\Delta_{L, \bar{g}_{\varepsilon, \delta}} \bar{o}_{1, \varepsilon, \delta}=0$$
for $|x| \leq \frac{1}{2} \delta$. Moreover, we have
$$\left|\Delta_{L, \bar{g}_{\varepsilon, \delta}} \bar{o}_{1, \varepsilon, \delta}\right| \leq C \varepsilon^{4} \delta^{-2}$$
for $\frac{1}{2} \delta \leq|x| \leq \delta$ and
$$\left|\Delta_{L, \bar{g}_{\varepsilon, \delta}} \bar{o}_{1, \varepsilon, \delta}\right| \leq C \varepsilon^{8}|x|^{-10}$$
for $|x| \geq \delta$.
Proof. Again, this follows from a straightforward calculation. \(\square\)

\section*{4. The projection of the Ricci tensor to the approximate KERNEL}

Lemma 4.1. Fix a pair of indices $i \neq j$, and let $u$ be a smooth harmonic function which is defined on the Euclidean ball $\{|x| \leq \delta\}$. Then
$$\int_{\{|x|=\delta\}}\left[\frac{x_{i} x_{j}}{r^{6}} D_{\nu} u-u D_{\nu}\left(\frac{x_{i} x_{j}}{r^{6}}\right)\right] d \mu_{g_{\mathrm{eucl}}}=\frac{1}{2} \pi^{2} D_{i} D_{j} u(0)$$
and
$$\int_{\{|x|=\delta\}}\left[\frac{x_{i}^{2}-x_{j}^{2}}{r^{6}} D_{\nu} u-u D_{\nu}\left(\frac{x_{i}^{2}-x_{j}^{2}}{r^{6}}\right)\right] d \mu_{g_{\mathrm{eucl}}}=\frac{1}{2} \pi^{2}\left(D_{i} D_{i} u(0)-D_{j} D_{j} u(0)\right) .$$
Here, $\nu$ denotes the outward-pointing unit normal to the hypersurface $\{|x|=$ $\delta\}$ with respect to the Euclidean metric.

Proof. By the divergence theorem, the quantity
$$I(r):=\int_{\{|x|=r\}}\left[\frac{x_{i} x_{j}}{r^{6}} D_{\nu} u-u D_{\nu}\left(\frac{x_{i} x_{j}}{r^{6}}\right)\right] d \mu_{g_{\mathrm{eucl}}}$$
is independent of $r$. Moreover, if we perform a Taylor expansion of $u$ around the origin, it is easy to see that $I(r) \rightarrow \frac{1}{2} \pi^{2} D_{i} D_{j} u(0)$ as $r \rightarrow 0$. Thus, $I(r)=\frac{1}{2} \pi^{2} D_{i} D_{j} u(0)$ for all $r>0$. This proves the first identity. The second identity follows from an analogous argument. \(\square\)

Proposition 4.2. We have
$$\int_{\{|x|=\delta\}}\left(\left\langle o_{1, \varepsilon}, D_{\nu} \bar{h}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}-\left\langle\bar{h}, D_{\nu} o_{1, \varepsilon}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}\right) d \mu_{g_{\mathrm{eh}, \varepsilon}}=32 \pi^{2} \omega \varepsilon^{8}+O\left(\varepsilon^{12} \delta^{-10}\right),$$
where $\bar{h}=\bar{g}_{\varepsilon, \delta}-g_{\mathrm{eh}, \varepsilon}$ and
$$\omega:=\sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}}|a|^{-10}\left(|a|^{4}-6\left(a_{1}^{2}+a_{2}^{2}\right)\left(a_{3}^{2}+a_{4}^{2}\right)\right) \approx 7.70 .$$
Proof. For $\delta \leq|x| \leq 2 \delta$, we have
$$\bar{h}=\bar{g}_{\varepsilon, \delta}-g_{\mathrm{eh}, \varepsilon}=\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4} \backslash\{0\}} \tau_{a}^{*} T+\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} \tau_{a}^{*} \hat{T}+O\left(\varepsilon^{8}|x|^{-8}\right)$$
and
$$o_{1, \varepsilon}=\varepsilon^{4} T+O\left(\varepsilon^{8}|x|^{-8}\right) .$$

Consequently,
$$\begin{aligned}
& \int_{\{|x|=\delta\}}\left(\left\langle o_{1, \varepsilon}, D_{\nu} \bar{h}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}-\left\langle\bar{h}, D_{\nu} o_{1, \varepsilon}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}\right) d \mu_{g_{\mathrm{eh}, \varepsilon}} \\
& =\frac{1}{2} \varepsilon^{8} \sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4} \backslash\{0\}} \int_{\{|x|=\delta\}}\left(\left\langle T, D_{\nu}\left(\tau_{a}^{*} T\right)\right\rangle_{g_{\mathrm{eucl}}}-\left\langle\tau_{a}^{*} T, D_{\nu} T\right\rangle_{g_{\mathrm{eucl}}}\right) d \mu_{g_{\mathrm{eucl}}} \\
& +\frac{1}{2} \varepsilon^{8} \sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} \int_{\{|x|=\delta\}}\left(\left\langle T, D_{\nu}\left(\tau_{a}^{*} \hat{T}\right)\right\rangle_{g_{\mathrm{eucl}}}-\left\langle\tau_{a}^{*} \hat{T}, D_{\nu} T\right\rangle_{g_{\mathrm{eucl}}}\right) d \mu_{g_{\mathrm{eucl}}} \\
& +O\left(\varepsilon^{12} \delta^{-10}\right)
\end{aligned}$$
Hence, it remains to evaluate the integrals
$$\int_{\{|x|=\delta\}}\left(\left\langle T, D_{\nu}\left(\tau_{a}^{*} T\right)\right\rangle_{g_{\mathrm{eucl}}}-\left\langle\tau_{a}^{*} T, D_{\nu} T\right\rangle_{g_{\mathrm{eucl}}}\right) d \mu_{g_{\mathrm{eucl}}}$$
and
$$\int_{\{|x|=\delta\}}\left(\left\langle T, D_{\nu}\left(\tau_{a}^{*} \hat{T}\right)\right\rangle_{g_{\mathrm{eucl}}}-\left\langle\tau_{a}^{*} \hat{T}, D_{\nu} T\right\rangle_{g_{\mathrm{eucl}}}\right) d \mu_{g_{\mathrm{eucl}}}$$
where $a \in \mathbb{Z}^{4} \backslash\{0\}$. To that end, we use Lemma 4.1. Since the components of $\tau_{a}^{*} T$ are smooth harmonic functions near the origin, we obtain
$$\begin{aligned}
& \int_{\{|x|=\delta\}}\left(\left\langle T, D_{\nu}\left(\tau_{a}^{*} T\right)\right\rangle_{g_{\mathrm{eucl}}}-\left\langle\tau_{a}^{*} T, D_{\nu} T\right\rangle_{g_{\mathrm{eucl}}}\right) d \mu_{g_{\mathrm{eucl}}} \\
& =-\frac{1}{2} \pi^{2}\left\langle\left(D_{1} D_{1}+D_{2} D_{2}-D_{3} D_{3}-D_{4} D_{4}\right) \tau_{a}^{*} T\right. \\
& \left.\quad d x_{1} \otimes d x_{1}+d x_{2} \otimes d x_{2}-d x_{3} \otimes d x_{3}-d x_{4} \otimes d x_{4}\right\rangle\left.\right|_{x=0} \\
& -\left.\pi^{2}\left\langle\left(D_{1} D_{3}+D_{2} D_{4}\right) \tau_{a}^{*} T, d x_{1} \otimes d x_{3}+d x_{3} \otimes d x_{1}+d x_{2} \otimes d x_{4}+d x_{4} \otimes d x_{2}\right\rangle\right|_{x=0} \\
& -\left.\pi^{2}\left\langle\left(D_{1} D_{4}-D_{2} D_{3}\right) \tau_{a}^{*} T, d x_{1} \otimes d x_{4}+d x_{4} \otimes d x_{1}-d x_{2} \otimes d x_{3}-d x_{3} \otimes d x_{2}\right\rangle\right|_{x=0} \\
& =2 \pi^{2}\left(D_{1} D_{1}+D_{2} D_{2}-D_{3} D_{3}-D_{4} D_{4}\right) \\
& \left.\quad \frac{\left(x_{1}-a_{1}\right)^{2}+\left(x_{2}-a_{2}\right)^{2}-\left(x_{3}-a_{3}\right)^{2}-\left(x_{4}-a_{4}\right)^{2}}{|x-a|^{6}}\right|_{x=0} \\
& +\left.8 \pi^{2}\left(D_{1} D_{3}+D_{2} D_{4}\right) \frac{\left(x_{1}-a_{1}\right)\left(x_{3}-a_{3}\right)+\left(x_{2}-a_{2}\right)\left(x_{4}-a_{4}\right)}{|x-a|^{6}}\right|_{x=0} \\
& +\left.8 \pi^{2}\left(D_{1} D_{4}-D_{2} D_{3}\right) \frac{\left(x_{1}-a_{1}\right)\left(x_{4}-a_{4}\right)-\left(x_{2}-a_{2}\right)\left(x_{3}-a_{3}\right)}{|x-a|^{6}}\right|_{x=0} \\
& =0 .
\end{aligned}$$

Moreover, since the components of $\tau_{a}^{*} \hat{T}$ are smooth harmonic functions near the origin, we obtain
$$\begin{aligned}
& \int_{\{|x|=\delta\}}\left(\left\langle T, D_{\nu}\left(\tau_{a}^{*} \hat{T}\right)\right\rangle_{g_{\mathrm{eucl}}}-\left\langle\tau_{a}^{*} \hat{T}, D_{\nu} T\right\rangle_{g_{\mathrm{eucl}}}\right) d \mu_{g_{\mathrm{eucl}}} \\
& =-\frac{1}{2} \pi^{2}\left\langle\left(D_{1} D_{1}+D_{2} D_{2}-D_{3} D_{3}-D_{4} D_{4}\right) \tau_{a}^{*} \hat{T}\right. \\
& \left.\quad d x_{1} \otimes d x_{1}+d x_{2} \otimes d x_{2}-d x_{3} \otimes d x_{3}-d x_{4} \otimes d x_{4}\right\rangle\left.\right|_{x=0} \\
& -\left.\pi^{2}\left\langle\left(D_{1} D_{3}+D_{2} D_{4}\right) \tau_{a}^{*} \hat{T}, d x_{1} \otimes d x_{3}+d x_{3} \otimes d x_{1}+d x_{2} \otimes d x_{4}+d x_{4} \otimes d x_{2}\right\rangle\right|_{x=0} \\
& -\left.\pi^{2}\left\langle\left(D_{1} D_{4}-D_{2} D_{3}\right) \tau_{a}^{*} \hat{T}, d x_{1} \otimes d x_{4}+d x_{4} \otimes d x_{1}-d x_{2} \otimes d x_{3}-d x_{3} \otimes d x_{2}\right\rangle\right|_{x=0} \\
& =2 \pi^{2}\left(D_{1} D_{1}+D_{2} D_{2}-D_{3} D_{3}-D_{4} D_{4}\right) \\
& \left.\quad \frac{\left(x_{1}-a_{1}\right)^{2}+\left(x_{2}-a_{2}\right)^{2}-\left(x_{3}-a_{3}\right)^{2}-\left(x_{4}-a_{4}\right)^{2}}{|x-a|^{6}}\right|_{x=0} \\
& =64 \pi^{2}|a|^{-10}\left(|a|^{4}-6\left(a_{1}^{2}+a_{2}^{2}\right)\left(a_{3}^{2}+a_{4}^{2}\right)\right)
\end{aligned}$$
Putting these facts together, the assertion follows. \(\square\)

Proposition 4.3. Let $\bar{h}=\bar{g}_{\varepsilon, \delta}-g_{\mathrm{eh}, \varepsilon}$ and $Z=\operatorname{div}_{g_{\mathrm{eh}, \varepsilon}} \bar{h}-\frac{1}{2} \nabla \operatorname{tr}_{g_{\mathrm{eh}, \varepsilon}} \bar{h}$. Then
$$\int_{\{|x|=\delta\}} o_{1, \varepsilon}(Z, \nu) d \mu_{g_{\mathrm{eh}, \varepsilon}}=O\left(\varepsilon^{12} \delta^{-10}\right) .$$
Proof. Recall that
$$\bar{h}=\bar{g}_{\varepsilon, \delta}-g_{\mathrm{eh}, \varepsilon}=\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4} \backslash\{0\}} \tau_{a}^{*} T+\frac{1}{2} \varepsilon^{4} \sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} \tau_{a}^{*} \hat{T}+O\left(\varepsilon^{8}|x|^{-8}\right)$$
for $\delta \leq|x| \leq 2 \delta$. Both $\tau_{a}^{*} T$ and $\tau_{a}^{*} \hat{T}$ are trace-free and divergence-free with respect to the Euclidean metric. This implies
$$\nabla \operatorname{tr}_{g_{\text {eucl }}} \bar{h}=O\left(\varepsilon^{8}|x|^{-9}\right)$$
and
$$\operatorname{div}_{g_{\text {eucl }}} \bar{h}=O\left(\varepsilon^{8}|x|^{-9}\right)$$
for $\delta \leq|x| \leq 2 \delta$. Since $g_{\mathrm{eh}, \varepsilon}-g_{\mathrm{eucl}}=O\left(\varepsilon^{4}|x|^{-4}\right)$, it follows that
$$\nabla \operatorname{tr}_{g_{\mathrm{eh}, \varepsilon}} \bar{h}=O\left(\varepsilon^{8}|x|^{-9}\right)$$
and
$$\operatorname{div}_{g_{\mathrm{eh}, \varepsilon}} \bar{h}=O\left(\varepsilon^{8}|x|^{-9}\right)$$
for $\delta \leq|x| \leq 2 \delta$. In particular, $Z=O\left(\varepsilon^{8}|x|^{-9}\right)$, which implies $o_{1, \varepsilon}(Z, \nu)=$ $O\left(\varepsilon^{12} \delta^{-13}\right)$. From this, the assertion follows easily. \(\square\)

Corollary 4.4. We have
$$-2 \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\bar{o}_{1, \varepsilon, \delta}, \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}}=32 \pi^{2} \omega \varepsilon^{8}+O\left(\varepsilon^{8} \delta^{2}\right) .$$

Proof. As above, we write $\bar{h}=\bar{g}_{\varepsilon, \delta}-g_{\mathrm{eh}, \varepsilon}$ and $Z=\operatorname{div}_{g_{\mathrm{eh}, \varepsilon}} \bar{h}-\frac{1}{2} \nabla \operatorname{tr}_{g_{\mathrm{eh}, \varepsilon}} \bar{h}$. Note that $\bar{h}$ is defined in the region $\{|x| \leq \delta\}$ and vanishes identically in the region $\left\{|x| \leq \frac{1}{2} \delta\right\}$. Moreover, we have $|\bar{h}| \leq O\left(\varepsilon^{4}\right),|\nabla \bar{h}| \leq O\left(\varepsilon^{4} \delta^{-1}\right)$, and $\left|\nabla^{2} \bar{h}\right| \leq O\left(\varepsilon^{4} \delta^{-2}\right)$ in the annulus $\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}$.

Using the well-known formula for the linearization of the Ricci curvature, we obtain
$$-2 \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}=\Delta_{L, g_{\mathrm{eh}, \varepsilon}} \bar{h}-\mathscr{L}_{Z} g_{\mathrm{eh}, \varepsilon}+O\left(\varepsilon^{8} \delta^{-2}\right)$$
in the region $\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}$. Since $\bar{o}_{1, \varepsilon, \delta}=o_{1, \varepsilon}+O\left(\varepsilon^{4}\right)$ and $\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}=$ $O\left(\varepsilon^{4} \delta^{-2}\right)$ in the region $\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}$, we deduce that
$$\begin{aligned}
& -2 \int_{\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}}\left\langle\bar{o}_{1, \varepsilon, \delta}, \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}} \\
& =\int_{\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}}\left\langle o_{1, \varepsilon}, \Delta_{L, g_{\mathrm{eh}, \varepsilon}} \bar{h}-\mathscr{L}_{Z} g_{\mathrm{eh}, \varepsilon}\right\rangle_{g_{\mathrm{eh}, \varepsilon}} d \operatorname{vol}_{g_{\mathrm{eh}, \varepsilon}}+O\left(\varepsilon^{8} \delta^{2}\right) .
\end{aligned}$$
Since $o_{1, \varepsilon}$ satisfies the equation $\Delta_{L, g_{\mathrm{eh}, \varepsilon} o_{1, \varepsilon}}=0$, the divergence theorem gives
$$\begin{aligned}
& \int_{\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}}\left\langle o_{1, \varepsilon}, \Delta_{L, g_{\mathrm{eh}, \varepsilon}} \bar{h}\right\rangle_{g_{\mathrm{eh}, \varepsilon}} d \operatorname{vol}_{g_{\mathrm{eh}, \varepsilon}} \\
& =\int_{\{|x| \leq \delta\}}\left(\left\langle o_{1, \varepsilon}, \Delta_{L, g_{\mathrm{eh}, \varepsilon}} \bar{h}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}-\left\langle\bar{h}, \Delta_{L, g_{\mathrm{eh}, \varepsilon}} o_{1, \varepsilon}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}\right) d \operatorname{vol}_{g_{\mathrm{eh}, \varepsilon}} \\
& =\int_{\{|x|=\delta\}}\left(\left\langle o_{1, \varepsilon}, D_{\nu} \bar{h}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}-\left\langle\bar{h}, D_{\nu} o_{1, \varepsilon}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}\right) d \mu_{g_{\mathrm{eh}, \varepsilon}} \\
& =32 \pi^{2} \omega \varepsilon^{8}+O\left(\varepsilon^{12} \delta^{-10}\right)
\end{aligned}$$
where in the last step we have used Proposition 4.2. Finally, since $\operatorname{div}_{g_{\mathrm{eh}, \varepsilon}} o_{1, \varepsilon}=$ 0, the divergence theorem yields
$$\begin{aligned}
& \int_{\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}}\left\langle o_{1, \varepsilon}, \mathscr{L}_{Z} g_{\mathrm{eh}, \varepsilon}\right\rangle_{g_{\mathrm{eh}, \varepsilon}} d \operatorname{vol}_{g_{\mathrm{eh}, \varepsilon}} \\
& =\int_{\{|x| \leq \delta\}}\left(\left\langle o_{1, \varepsilon}, \mathscr{L}_{Z} g_{\mathrm{eh}, \varepsilon}\right\rangle_{g_{\mathrm{eh}, \varepsilon}}+2\left\langle\operatorname{div}_{g_{\mathrm{eh}, \varepsilon}} o_{1, \varepsilon}, Z\right\rangle_{g_{\mathrm{eh}, \varepsilon}}\right) d \operatorname{vol}_{g_{\mathrm{eh}, \varepsilon}} \\
& =\int_{\{|x|=\delta\}} 2 o_{1, \varepsilon}(Z, \nu) d \mu_{g_{\mathrm{eh}, \varepsilon}} \\
& =O\left(\varepsilon^{12} \delta^{-10}\right)
\end{aligned}$$
by Proposition 4.3. Putting these facts together, we conclude that
$$-2 \int_{\left\{\frac{1}{2} \delta \leq|x| \leq \delta\right\}}\left\langle\bar{o}_{1, \varepsilon, \delta}, \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}}=32 \pi^{2} \omega \varepsilon^{8}+O\left(\varepsilon^{8} \delta^{2}\right) .$$
Since $\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}=0$ in the region $\left\{|x| \leq \frac{1}{2} \delta\right\}$ and $\left|\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right| \leq C \varepsilon^{8}|x|^{-10}$ in the region $\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{|x| \leq \delta\}$, the assertion follows. \(\square\)

Proposition 4.5. We have
$$-2 \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\bar{g}_{\varepsilon, \delta}, \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}}=O\left(\varepsilon^{8} \delta^{-6}\right)$$
Proof. Let $\tilde{h}=\bar{g}_{\varepsilon, \delta}-g_{\text {eucl }}$. Clearly, $\tilde{h}$ is defined on $\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\left\{|x| \leq \frac{1}{4} \delta\right\}$, and we have $|\tilde{h}| \leq O\left(\varepsilon^{4}|x|^{-4}\right),|\nabla \tilde{h}| \leq O\left(\varepsilon^{4}|x|^{-5}\right)$, and $\left|\nabla^{2} \tilde{h}\right| \leq O\left(\varepsilon^{4}|x|^{-6}\right)$. Using the standard formula for the linearization of the scalar curvature, we deduce that
$$\left\langle\bar{g}_{\varepsilon, \delta}, \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right\rangle_{\bar{g}_{\varepsilon, \delta}}=\operatorname{div} \operatorname{div} \tilde{h}-\Delta \operatorname{tr} \tilde{h}+O\left(\varepsilon^{8}|x|^{-10}\right)$$
in the region $\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\left\{|x| \leq \frac{1}{2} \delta\right\}$. Here, the divergence and the Laplacian on the right hand side are taken with respect to the Euclidean metric. Using the divergence theorem, we obtain
$$\begin{aligned}
& \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\left\{|x| \leq \frac{1}{2} \delta\right\}}\left\langle\bar{g}_{\varepsilon, \delta}, \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}} \\
& =\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\left\{|x| \leq \frac{1}{2} \delta\right\}}(\operatorname{div} \operatorname{div} \tilde{h}-\Delta \operatorname{tr} \tilde{h}) d \operatorname{vol}_{g_{\text {eucl }}}+O\left(\varepsilon^{8} \delta^{-6}\right) \\
& =-\int_{\left\{|x|=\frac{1}{2} \delta\right\}}\left(\langle\operatorname{div} \tilde{h}, \nu\rangle_{g_{\text {eucl }}}-\langle\nabla \operatorname{tr} \tilde{h}, \nu\rangle_{g_{\text {eucl }}}\right) d \mu_{g_{\text {eucl }}}+O\left(\varepsilon^{8} \delta^{-6}\right)
\end{aligned}$$
As above, $\nu$ denotes the outward-pointing unit normal to the hypersurface $\left\{|x|=\frac{1}{2} \delta\right\}$ with respect to the Euclidean metric. For $\frac{1}{4} \delta \leq|x| \leq \frac{1}{2} \delta$, we have
$$\tilde{h}=g_{\mathrm{eh}, \varepsilon}-g_{\mathrm{eucl}}=\frac{1}{2} \varepsilon^{4} T+O\left(\varepsilon^{8} \delta^{-8}\right) .$$
Since $T$ is trace-free and divergence-free with respect to the Euclidean metric, it follows that
$$\nabla \operatorname{tr} \tilde{h}=O\left(\varepsilon^{8} \delta^{-9}\right)$$
and
$$\operatorname{div} \tilde{h}=O\left(\varepsilon^{8} \delta^{-9}\right) .$$
Thus, we conclude that
$$\int_{\left\{|x|=\frac{1}{2} \delta\right\}}\left(\langle\operatorname{div} \tilde{h}, \nu\rangle_{g_{\mathrm{eucl}}}-\langle\nabla \operatorname{tr} \tilde{h}, \nu\rangle_{g_{\mathrm{eucl}}}\right) d \mu_{g_{\mathrm{eucl}}}=O\left(\varepsilon^{8} \delta^{-6}\right),$$
hence
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\left\{|x| \leq \frac{1}{2} \delta\right\}}\left\langle\bar{g}_{\varepsilon, \delta}, \operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}}=O\left(\varepsilon^{8} \delta^{-6}\right) .$$
Since $\operatorname{Ric}_{\bar{g}_{\varepsilon, \delta}}=0$ in the region $\left\{|x| \leq \frac{1}{2} \delta\right\}$, the assertion follows. \(\square\)

Finally, we compute the projection of $\frac{\partial}{\partial \varepsilon} \bar{g}_{\varepsilon, \delta}$ to the approximate kernel.
Proposition 4.6. We have
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\bar{o}_{1, \varepsilon, \delta}, \frac{\partial}{\partial \varepsilon} \bar{g}_{\varepsilon, \delta}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}}=4 \pi^{2} \varepsilon^{3}+O\left(\varepsilon^{7} \delta^{-4}\right)$$
and
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\bar{g}_{\varepsilon, \delta}, \frac{\partial}{\partial \varepsilon} \bar{g}_{\varepsilon, \delta}\right\rangle_{\bar{g}_{\varepsilon, \delta}} d \operatorname{vol}_{\bar{g}_{\varepsilon, \delta}}=O\left(\varepsilon^{3} \log \frac{1}{\delta}\right) .$$
Proof. For $|x| \leq \frac{1}{2} \delta$, we have $\bar{g}_{\varepsilon, \delta}=g_{\text {eh }, \varepsilon}, \frac{\partial}{\partial \varepsilon} \bar{g}_{\varepsilon, \delta}=\frac{2}{\varepsilon} o_{1, \varepsilon}$, and $\bar{o}_{1, \varepsilon, \delta}=o_{1, \varepsilon}$. From this, the assertion follows easily. \(\square\)

\section*{5. Liouville-type theorems for the parabolic Lichnerowicz EQUATION}

In this section, we establish Liouville-type theorems for the parabolic Lichnerowicz equation on various model spaces. We first recall some basic properties of the Lichnerowicz Laplacian on the Eguchi-Hanson manifold which were established by Biquard [5] and Biquard and Rollin [7] (see also [32]).

Proposition 5.1 (O. Biquard [5]; O. Biquard, Y. Rollin [7]). Let $\left(M_{\mathrm{eh}}, g_{\mathrm{eh}}\right)$ denote the Eguchi-Hanson manifold with parameter $\varepsilon=1$, and let $o_{i}:=o_{i, 1}$. Then the following statements hold:
\begin{itemize}
\item[(i)] Let $h$ be a symmetric (0, 2)-tensor on the Eguchi-Hanson manifold satisfying $|h| \leq(1+r)^{-\sigma}$ for some $\sigma>0$ and $\Delta_{L, g_{\mathrm{eh}}} h=0$. Then $h \in \operatorname{span}\left\{o_{1}, o_{2}, o_{3}\right\}$.
\item[(ii)] Let $h$ be a symmetric (0, 2)-tensor on the Eguchi-Hanson manifold satisfying $|h| \leq(1+r)^{-\sigma-1}$ and $|\nabla h| \leq(1+r)^{-\sigma-2}$ for some $\sigma>0$. Then
$$\int_{M_{\mathrm{eh}}}\left\langle\Delta_{L, g_{\mathrm{eh}}} h, h\right\rangle d \operatorname{vol}_{g_{\mathrm{eh}}} \leq 0$$
Moreover, equality holds if and only if $h \in \operatorname{span}\left\{o_{1}, o_{2}, o_{3}\right\}$.
\end{itemize}

Proof. The first statement is contained in Proposition 1.1 in [5]. The second statement follows from a Bochner formula from [7]. To explain this, let $h$ be a symmetric (0, 2)-tensor on the Eguchi-Hanson manifold satisfying $|h| \leq C(1+r)^{-\sigma-1}$ and $|\nabla h| \leq C(1+r)^{-\sigma-2}$. Clearly,
$$\int_{M_{\mathrm{eh}}}\left\langle\Delta_{L, g_{\mathrm{eh}}} h, h\right\rangle \mathrm{vol}_{g_{\mathrm{eh}}}=\int_{M_{\mathrm{eh}}}\left\langle\Delta_{L, g_{\mathrm{eh}}} k, k\right\rangle \mathrm{vvol}_{g_{\mathrm{eh}}}+\frac{1}{4} \int_{M_{\mathrm{eh}}}\left\langle\Delta_{g_{\mathrm{eh}}} \operatorname{tr} h, \operatorname{tr} h\right\rangle \operatorname{vol}_{g_{\mathrm{eh}}}$$
where $k$ denotes the trace-free part of $h$. We may view $k$ as a section of the vector bundle $\Lambda_{-}^{2} \otimes \Lambda_{+}^{2}$. The Bochner formula (4.6) in [7] implies that $-\frac{1}{2} \Delta_{L, g_{\mathrm{eh}}} k=d_{-} d_{-}^{*} k$, where $d_{-}: \Gamma\left(\Lambda^{1} \otimes \Lambda_{+}^{2}\right) \rightarrow \Gamma\left(\Lambda_{-}^{2} \otimes \Lambda_{+}^{2}\right)$ is the exterior derivative (cf. [5], [7]). This gives
$$\int_{M_{\mathrm{eh}}}\left\langle\Delta_{L, g_{\mathrm{eh}}} k, k\right\rangle d \operatorname{vol}_{g_{\mathrm{eh}}}=-2 \int_{M_{\mathrm{eh}}}\left|d_{-}^{*} k\right|^{2} d \operatorname{vol}_{g_{\mathrm{eh}}}$$
hence
$$\int_{M_{\mathrm{eh}}}\left\langle\Delta_{L, g_{\mathrm{eh}}} h, h\right\rangle d \operatorname{vol}_{g_{\mathrm{eh}}}=-2 \int_{M_{\mathrm{eh}}}\left|d_{-}^{*} k\right|^{2} d \operatorname{vol}_{g_{\mathrm{eh}}}-\frac{1}{4} \int_{M_{\mathrm{eh}}}|\nabla \operatorname{tr} h|^{2} d \operatorname{vol}_{g_{\mathrm{eh}}} \leq 0 .$$

Moreover, if equality holds, then $d_{-}^{*} k=0$ and $\operatorname{tr} h=0$. Results in [5] now imply that $h \in \operatorname{span}\left\{o_{1}, o_{2}, o_{3}\right\}$. \(\square\)

We next establish a Liouville-type theorem for the linear heat equation on the Eguchi-Hanson manifold.

Proposition 5.2. Let $\left(M_{\mathrm{eh}}, g_{\mathrm{eh}}\right)$ denote the Eguchi-Hanson manifold with parameter $\varepsilon=1$, and let $o_{i}:=o_{i, 1}$. Let $h$ be a solution of the heat equation $\frac{\partial}{\partial t} h=\Delta_{L, g_{\mathrm{eh}}} h$ on $M_{\mathrm{eh}} \times(-\infty, 0]$ with the property that $|h| \leq(1+r)^{-\sigma}$ for some $\sigma>0$. If $\int_{M_{\mathrm{eh}}}\left\langle h(t), o_{i}\right\rangle=0$ for all $i \in\{1,2,3\}$ and all $t \in(-\infty, 0]$, then $h$ vanishes identically.

Proof. Let us consider the tensor field $k(t):=\Delta_{L, g_{\mathrm{eh}}} h(t)$. It follows from standard interior estimates for parabolic equations that $|k| \leq C(1+r)^{-\sigma-2}$ and $|\nabla k| \leq C(1+r)^{-\sigma-3}$. In particular, $\int_{M_{\mathrm{eh}}}|k(t)|^{2} \leq C$ for each $t \in$ $(-\infty, 0]$. Moreover, $k$ satisfies the equation $\frac{\partial}{\partial t} k=\Delta_{L, g_{\mathrm{eh}}} k$, and we have $\int_{M_{\text {eh }}}\left\langle k(t), o_{i}\right\rangle=0$ for all $i \in\{1,2,3\}$ and all $t \in(-\infty, 0]$. Using Proposition 5.1, we obtain
$$\frac{1}{2} \frac{d}{d t}\left(\int_{M_{\mathrm{eh}}}|k(t)|^{2} d \mathrm{vol}_{g_{\mathrm{eh}}}\right)=\int_{M_{\mathrm{eh}}}\left\langle\Delta_{L, g_{\mathrm{eh}}} k(t), k(t)\right\rangle d \mathrm{vol}_{g_{\mathrm{eh}}} \leq 0$$
Consequently, the function $t \mapsto \int_{M_{\text {eh }}}|k(t)|^{2}$ is monotone decreasing. In particular, the limit $A:=\lim _{t \rightarrow-\infty} \int_{M_{\text {eh }}}|k(t)|^{2}$ exists.

We next pick an arbitrary sequence of times $t_{j} \rightarrow-\infty$, and define $\tilde{k}^{(j)}(t):=$ $k\left(t_{j}+t\right)$. After passing to a subsequence if necessary, we may assume that the sequence $\tilde{k}^{(j)}$ converges in $C_{\text {loc }}^{\infty}$ to some tensor field $\hat{k}$ which is defined on $M_{\mathrm{eh}} \times \mathbb{R}$ and satisfies the equation $\frac{\partial}{\partial t} \hat{k}=\Delta_{L, g_{\mathrm{eh}}} \hat{k}$. Moreover, $|\hat{k}| \leq C(1+r)^{-\sigma-2}$ and $|\nabla \hat{k}| \leq C(1+r)^{-\sigma-3}$. Using the dominated convergence theorem, we obtain
$$\int_{M_{\mathrm{eh}}}|\hat{k}(t)|^{2} d \mathrm{vol}_{g_{\mathrm{eh}}}=\lim _{j \rightarrow \infty} \int_{M_{\mathrm{eh}}}\left|k\left(t_{j}+t\right)\right|^{2} d \mathrm{vol}_{g_{\mathrm{eh}}}=A$$
and
$$\int_{M_{\mathrm{eh}}}\left\langle\hat{k}(t), o_{i}\right\rangle d \mathrm{vol}_{g_{\mathrm{eh}}}=\lim _{j \rightarrow \infty} \int_{M_{\mathrm{eh}}}\left\langle k\left(t_{j}+t\right), o_{i}\right\rangle d \mathrm{vol}_{g_{\mathrm{eh}}}=0$$
for all $i \in\{1,2,3\}$ and all $t \in \mathbb{R}$. Differentiating the first identity with respect to $t$ gives
$$0=\frac{1}{2} \frac{d}{d t}\left(\int_{M_{\mathrm{eh}}}|\hat{k}(t)|^{2} d \operatorname{vol}_{g_{\mathrm{eh}}}\right)=\int_{M_{\mathrm{eh}}}\left\langle\Delta_{L, g_{\mathrm{eh}}} \hat{k}(t), \hat{k}(t)\right\rangle d \operatorname{vol}_{g_{\mathrm{eh}}}$$
for all $t \in \mathbb{R}$. Hence, Proposition 5.1 implies that $\hat{k}(t)=0$ for all $t \in \mathbb{R}$. Consequently, $A=0$. In other words, $\lim _{t \rightarrow-\infty} \int_{M_{\text {eh }}}|k(t)|^{2}=0$. Since the function $t \mapsto \int_{M_{\text {eh }}}|k(t)|^{2}$ is monotone decreasing, it follows that $k(t)=0$ for all $t \in(-\infty, 0]$. Thus, we conclude that $\Delta_{L, g_{\mathrm{eh}}} h(t)=0$ for all $t \in(-\infty, 0]$.

Since $\int_{M_{\text {eh }}}\left\langle h(t), o_{i}\right\rangle=0$ for all $i \in\{1,2,3\}$ and all $t \in(-\infty, 0]$, Proposition 5.1 implies that $h(t)=0$ for all $t \in(-\infty, 0]$. \(\square\)

Proposition 5.3. Let $h$ be a solution of the heat equation $\frac{\partial}{\partial t} h=\Delta_{g_{\text {eucl }}} h$ on $\left(\mathbb{R}^{4} \backslash\{0\}\right) \times(-\infty, 0]$ with the property that $|h| \leq r^{-\sigma}$ for some $\sigma \in(0,2)$. Then $h$ vanishes identically.

Proof. Let us fix an arbitrary point $\left(x_{0}, t_{0}\right)$ in spacetime. Since $\sigma<2$, the equation $\frac{\partial}{\partial t} h=\Delta_{g_{\text {eucl }}} h$ is satisfied in the sense of distributions. Consequently,
$$h\left(x_{0}, t_{0}\right)=\int_{\mathbb{R}^{4} \backslash\{0\}} \frac{1}{(4 \pi t)^{2}} e^{-\frac{\left|x-x_{0}\right|^{2}}{4 t}} h\left(x, t_{0}-t\right)$$
for all $t>0$. Since $\left|h\left(x, t_{0}-t\right)\right| \leq|x|^{-\sigma}$, it follows that
$$\begin{aligned}
\left|h\left(x_{0}, t_{0}\right)\right| & \leq \int_{\mathbb{R}^{4} \backslash\{0\}} \frac{1}{(4 \pi t)^{2}} e^{-\frac{\left|x-x_{0}\right|^{2}}{4 t}}|x|^{-\sigma} \\
& \leq C t^{-2} \int_{\left\{|x|^{2} \leq t\right\}}|x|^{-\sigma}+C \int_{\left\{|x|^{2} \geq t\right\}}|x|^{-4-\sigma} \\
& \leq C t^{-\frac{\sigma}{2}}
\end{aligned}$$
for all $t>0$. Sending $t \rightarrow \infty$ gives $h\left(x_{0}, t_{0}\right)=0$. \(\square\)

Proposition 5.4. Let $h$ be a symmetric (0, 2)-tensor defined on $\left(\mathbb{R}^{4} \backslash \mathbb{Z}^{4}\right) \times$ $(-\infty, 0]$ which evolves by the heat equation $\frac{\partial}{\partial t} h=\Delta_{g_{\text {eucl }}} h$ and is invariant under the maps
$$\begin{aligned}
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(1-x_{1}, x_{2}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, 1-x_{2}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, 1-x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{3}, 1-x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}+2, x_{2}, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}+2, x_{3}, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{3}+2, x_{4}\right), \\
& \left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{3}, x_{4}+2\right) .
\end{aligned}$$
Moreover, we assume that $|h| \leq r^{-\sigma}$ for some $\sigma \in(0,2)$. If $\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}} h_{i i}=$ 0 for each $i \in\{1,2,3,4\}$, then $h$ vanishes identically.

Proof. Let us fix an arbitrary point $\left(x_{0}, t_{0}\right)$ in spacetime. Moreover, let
$$\Gamma_{+}(x, t)=\frac{1}{(4 \pi t)^{2}}\left(\sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4}} e^{-\frac{\left|x-x_{0}-a\right|^{2}}{4 t}}+\sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} e^{-\frac{\left|x-x_{0}-a\right|^{2}}{4 t}}\right)$$
and
$$\Gamma_{-}(x, t)=\frac{1}{(4 \pi t)^{2}}\left(\sum_{a \in \mathbb{Z}_{\mathrm{even}}^{4}} e^{-\frac{\left|x-x_{0}-a\right|^{2}}{4 t}}-\sum_{a \in \mathbb{Z}_{\mathrm{odd}}^{4}} e^{-\frac{\left|x-x_{0}-a\right|^{2}}{4 t}}\right) .$$

We first consider an index $i \in\{1,2,3,4\}$. Since $\sigma<2, h_{i i}$ satisfies the heat equation in the sense of distributions. Hence, we may write
$$h_{i i}\left(x_{0}, t_{0}\right)=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}} \Gamma_{+}(x, t) h_{i i}\left(x, t_{0}-t\right) \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left(\Gamma_{+}(x, t)-1\right) h_{i i}\left(x, t_{0}-t\right)$$
for all $t>0$. Since $\left|h_{i i}\left(x, t_{0}-t\right)\right| \leq|x|^{-\sigma}$, it follows that
$$\left|h_{i i}\left(x_{0}, t_{0}\right)\right| \leq \sup _{x \in\left[-\frac{1}{2}, \frac{1}{2}\right]^{4}}\left|\Gamma_{+}(x, t)-1\right| \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}|x|^{-\sigma}$$
for all $t>0$. It is well known that the heat kernel on a torus converges to a constant at an exponential rate. This means that $\sup _{x \in\left[-\frac{1}{2}, \frac{1}{2}\right]^{4}}\left|\Gamma_{+}(x, t)-1\right|$ converges to 0 as $t \rightarrow \infty$. Consequently, $h_{i i}\left(x_{0}, t_{0}\right)=0$.

We next consider a pair of indices $i \neq j$. Since $\sigma<2, h_{i j}$ satisfies the heat equation in the sense of distributions. This gives
$$h_{i j}\left(x_{0}, t_{0}\right)=\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}} \Gamma_{-}(x, t) h_{i j}\left(x, t_{0}-t\right)$$
for all $t>0$. Since $\left|h_{i j}\left(x, t_{0}-t\right)\right| \leq|x|^{-\sigma}$, we obtain
$$\left|h_{i j}\left(x_{0}, t_{0}\right)\right| \leq \sup _{x \in\left[-\frac{1}{2}, \frac{1}{2}\right]^{4}}\left|\Gamma_{-}(x, t)\right| \int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}|x|^{-\sigma}$$
for all $t>0$. Since $\sup _{x \in\left[-\frac{1}{2}, \frac{1}{2}\right]^{4}}\left|\Gamma_{-}(x, t)\right|$ converges to 0 as $t \rightarrow \infty$, we conclude that $h_{i j}\left(x_{0}, t_{0}\right)=0$. This completes the proof. \(\square\)

\section*{6. Uniform estimates for the linearized equation}

Throughout this section, we will fix a real number $\alpha \in(0,1)$. Let $M$ denote the quotient manifold introduced in Section 3. We will consider a oneparameter family of metrics $\bar{g}_{\varepsilon(t), \delta(t)}, t \in(-\infty,-\Lambda]$, where $\delta(t)=(-t)^{-\frac{1}{400}}$. Moreover, the parameter $\varepsilon(t)$ is assumed to satisfy the following conditions:

Assumption 6.1. The function $\varepsilon(t)$ satisfies $(-64 \omega t)^{-\frac{1}{4}} \leq \varepsilon(t) \leq(-16 \omega t)^{-\frac{1}{4}}$, $\left|\frac{d \varepsilon}{d t}(t)\right| \leq(-t)^{-\frac{5}{4}}$, and $\left|t-t^{\prime}\right|^{-\alpha}\left|\frac{d \varepsilon}{d t}(t)-\frac{d \varepsilon}{d t}\left(t^{\prime}\right)\right| \leq(-t)^{-\frac{5}{4}+\frac{\alpha}{2}}$ for $0<\left|t-t^{\prime}\right| \leq$ $(-t)^{-\frac{1}{2}}$.

We first prove a weighted sup-estimate for solutions of the parabolic Lichnerowicz equation. As in [30], we use a blow-up argument together with the Liouville-type theorems established in Section 5.

Proposition 6.2. Given real numbers $\gamma>0$ and $\sigma \in(0,2)$, we can find real numbers $\Lambda>0$ and $C>0$ with the following property. Suppose that $\varepsilon(t)$ is a function which is defined on the interval $(-\infty,-\Lambda]$ and satisfies Assumption 6.1, and let $\delta(t)=(-t)^{-\frac{1}{400}}$. Let $h$ be a solution of the inhomogeneous heat equation $\frac{\partial}{\partial t} h(t)=\Delta_{L, \bar{g}_{\varepsilon(t), \delta(t)}} h(t)+\psi(t)$ which is defined on $M \times(-\infty,-\Lambda]$ and satisfies $\sup _{M \times(-\infty,-\Lambda]}(-t)^{\gamma}(\varepsilon(t)+r)^{\sigma}|h(t)|_{\bar{g}_{\varepsilon(t), \delta(t)}}<\infty$. Moreover, we
assume that $h$ is invariant under the group $\mathscr{G}$ and satisfies the orthogonality conditions
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{o}_{1, \varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
and
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h(t), \bar{g}_{\varepsilon(t), \delta(t)}\right\rangle_{\bar{g}_{\varepsilon(t), \delta(t)}} d \operatorname{vol}_{\bar{g}_{\varepsilon(t), \delta(t)}}=0$$
for all $t \in(-\infty,-\Lambda]$. Then
$$\begin{aligned}
& \sup _{M \times(-\infty,-\Lambda]}(-t)^{\gamma}\left((-t)^{-\frac{1}{4}}+r\right)^{\sigma}|h(t)|_{\bar{g}_{\varepsilon(t), \delta(t)}} \leq \\
& \quad \leq C \sup _{M \times(-\infty,-\Lambda]}(-t)^{\gamma}\left((-t)^{-\frac{1}{4}}+r\right)^{\sigma+2}|\psi(t)|_{\bar{g}_{\varepsilon(t), \delta(t)}} .
\end{aligned}$$
Proof. We argue by contradiction. If the assertion is false, we can find a sequence of functions $\varepsilon^{(j)}(t)$ and sequences of tensor fields $h^{(j)}$ and $\psi^{(j)}$ with the following properties:
\begin{itemize}
\item[-] The functions $\varepsilon^{(j)}(t)$ are defined on the interval $(-\infty,-j]$ and satisfy Assumption 6.1.
\item[-] The tensor fields $h^{(j)}$ and $\psi^{(j)}$ are defined on $M \times(-\infty,-j]$ and satisfy the equation
$$\frac{\partial}{\partial t} h^{(j)}(t)=\Delta_{L, g^{(j)}(t)} h^{(j)}(t)+\psi^{(j)}(t),$$
where $g^{(j)}(t):=\bar{g}_{\varepsilon(j)}(t), \delta(t)$.
\item[-] We have
$$\sup _{M \times(-\infty,-j]}(-t)^{\gamma}\left((-t)^{-\frac{1}{4}}+r\right)^{\sigma}\left|h^{(j)}(t)\right|_{g^{(j)}(t)}=1$$
and
$$\sup _{M \times(-\infty,-j]}(-t)^{\gamma}\left((-t)^{-\frac{1}{4}}+r\right)^{\sigma+2}\left|\psi^{(j)}(t)\right|_{g^{(j)}(t)} \rightarrow 0$$
as $j \rightarrow \infty$.
\item[-] The tensor $h^{(j)}$ satisfies the orthogonality conditions
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h^{(j)}(t), \bar{o}_{1, \varepsilon(j)}(t), \delta(t)\right\rangle_{g^{(j)}(t)} d \operatorname{vol}_{g^{(j)}(t)}=0$$
and
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h^{(j)}(t), g^{(j)}(t)\right\rangle_{g^{(j)}(t)} d \operatorname{vol}_{g^{(j)}(t)}=0$$
for all $t \in(-\infty,-j]$.
\end{itemize}

For each $j$, we can pick a point $\left(x_{j}, t_{j}\right) \in M \times(-\infty,-j]$ such that $\left(-t_{j}\right)^{\gamma}\left(\left(-t_{j}\right)^{-\frac{1}{4}}+\right.$ $r)^{\sigma}\left|h^{(j)}\left(t_{j}\right)\right|_{g^{(j)}(t)} \geq \frac{1}{2}$ at the point $x_{j}$. After passing to a subsequence, we are in one of the following three cases:

Case 1: Suppose $\lim _{j \rightarrow \infty}\left(-t_{j}\right)^{\frac{1}{4}}\left|x_{j}\right|<\infty$. Let us consider the rescaled metrics
$$\tilde{g}^{(j)}(t):=\varepsilon^{(j)}\left(t_{j}\right)^{-2} \rho_{j}^{*} g^{(j)}\left(t_{j}+\varepsilon^{(j)}\left(t_{j}\right)^{2} t\right),$$
where $t \in(-\infty, 0]$ and $\rho_{j}: M_{\mathrm{eh}} \rightarrow M_{\mathrm{eh}}$ denotes a dilation in space by the factor $\varepsilon^{(j)}\left(t_{j}\right)$. Moreover, we define
$$\tilde{h}^{(j)}(t):=\left(-t_{j}\right)^{\gamma} \varepsilon^{(j)}\left(t_{j}\right)^{\sigma-2} \rho_{j}^{*} h^{(j)}\left(t_{j}+\varepsilon^{(j)}\left(t_{j}\right)^{2} t\right)$$
and
$$\tilde{\psi}^{(j)}(t):=\left(-t_{j}\right)^{\gamma} \varepsilon^{(j)}\left(t_{j}\right)^{\sigma} \rho_{j}^{*} \psi^{(j)}\left(t_{j}+\varepsilon^{(j)}\left(t_{j}\right)^{2} t\right)$$
for $t \in(-\infty, 0]$. Clearly, $\frac{\partial}{\partial t} \tilde{h}^{(j)}(t)=\Delta_{L, \tilde{g}^{(j)}(t)} \tilde{h}^{(j)}(t)+\tilde{\psi}^{(j)}(t)$. After passing to a subsequence, the tensor fields $\tilde{h}^{(j)}$ converge in $C_{\text {loc }}^{0}$ to some tensor field $\hat{h} \neq 0$. The limiting tensor field $\hat{h}$ is defined on $M_{\mathrm{eh}} \times(-\infty, 0]$, where $M_{\mathrm{eh}}$ denotes the Eguchi-Hanson manifold with parameter $\varepsilon=1$. Moreover, $\hat{h}$ satisfies the heat equation $\frac{\partial}{\partial t} \hat{h}=\Delta_{L, g_{\mathrm{eh}}} \hat{h}$, and we have $\sup _{M_{\mathrm{eh}} \times(-\infty, 0]}(1+$ $r)^{\sigma}|\hat{h}(t)|_{g_{\mathrm{eh}}} \leq 1$.

In the next step, we show that $\hat{h}(t)$ is orthogonal to $o_{1}$ for each $t \in(-\infty, 0]$. Indeed, if we fix a number $t \in(-\infty, 0]$, then we have
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h^{(j)}\left(t_{j}^{\prime}\right), \bar{o}_{1, \varepsilon}(j)\left(t_{j}^{\prime}\right), \delta\left(t_{j}^{\prime}\right)\right\rangle_{\bar{g}(j)}{\left(t_{j}^{\prime}\right), \delta\left(t_{j}^{\prime}\right)} d \operatorname{vol}_{\bar{g}_{\varepsilon}(j)\left(t_{j}^{\prime}\right), \delta\left(t_{j}^{\prime}\right)}=0,$$
where $t_{j}^{\prime}:=t_{j}+\varepsilon^{(j)}\left(t_{j}\right)^{2} t$. Passing to the limit as $j \rightarrow \infty$, we obtain
$$\int_{M_{\mathrm{eh}}}\left\langle\hat{h}(t), o_{1}\right\rangle_{g_{\mathrm{eh}}} d \mathrm{vol}_{g_{\mathrm{eh}}}=0$$
by the dominated convergence theorem.
Finally, since $\hat{h}(t)$ is invariant under the map $\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{3}, x_{4}, x_{1}, x_{2}\right)$, we have
$$\int_{M_{\mathrm{eh}}}\left\langle\hat{h}(t), o_{2}\right\rangle_{g_{\mathrm{eh}}} d \operatorname{vol}_{g_{\mathrm{eh}}}=\int_{M_{\mathrm{eh}}}\left\langle\hat{h}(t), o_{3}\right\rangle_{g_{\mathrm{eh}}} d \operatorname{vol}_{g_{\mathrm{eh}}}=0$$
for each $t \in(-\infty, 0]$. This contradicts Proposition 5.2.
Case 2: Suppose now that $\lim _{j \rightarrow \infty}\left(-t_{j}\right)^{\frac{1}{4}}\left|x_{j}\right|=\infty$ and $\lim _{j \rightarrow \infty}\left|x_{j}\right|=0$. We consider the rescaled metrics
$$\tilde{g}^{(j)}(t):=\left|x_{j}\right|^{-2} \rho_{j}^{*} g^{(j)}\left(t_{j}+\left|x_{j}\right|^{2} t\right),$$
where $t \in(-\infty, 0]$ and $\rho_{j}$ denotes a dilation in space by the factor $\left|x_{j}\right|$. Moreover, we define
$$\tilde{h}^{(j)}(t):=\left(-t_{j}\right)^{\gamma}\left|x_{j}\right|^{\sigma-2} \rho_{j}^{*} h\left(t_{j}+\left|x_{j}\right|^{2} t\right)$$
and
$$\tilde{\psi}^{(j)}(t):=\left(-t_{j}\right)^{\gamma}\left|x_{j}\right|^{\sigma} \rho_{j}^{*} \psi^{(j)}\left(t_{j}+\left|x_{j}\right|^{2} t\right)$$
for $t \in(-\infty, 0]$. Clearly, $\frac{\partial}{\partial t} \tilde{h}^{(j)}(t)=\Delta_{L, \tilde{g}^{(j)}(t)} \tilde{h}^{(j)}(t)+\tilde{\psi}^{(j)}(t)$. After passing to a subsequence, the tensors $\tilde{h}^{(j)}$ converge in $C_{\text {loc }}^{0}$ to a tensor field $\hat{h} \neq 0$. The tensor field $\hat{h}$ is defined on $\left(\mathbb{R}^{4} \backslash\{0\}\right) / \mathbb{Z}_{2} \times(-\infty, 0]$ and satisfies the equation $\frac{\partial}{\partial t} \hat{h}=\Delta_{g_{\text {eucl }}} \hat{h}$. Moreover, we have $\sup _{\left(\mathbb{R}^{4} \backslash\{0\}\right) / \mathbb{Z}_{2} \times(-\infty, 0]} r^{\sigma}|\hat{h}(t)|_{g_{\text {eucl }}} \leq$ 1. After lifting $\hat{h}$ to a solution of the heat equation on $\left(\mathbb{R}^{4} \backslash\{0\}\right) \times(-\infty, 0]$, we obtain a contradiction with Proposition 5.3.

Case 3: Suppose finally that $\lim _{j \rightarrow \infty}\left|x_{j}\right|>0$. In this case, we define
$$\tilde{h}^{(j)}(t):=\left(-t_{j}\right)^{\gamma} h\left(t_{j}+t\right)$$
for $t \in(-\infty, 0]$. After passing to a subsequence, the tensor fields $\tilde{h}^{(j)}$ converge in $C_{\text {loc }}^{0}$ to some tensor field $\hat{h} \neq 0$. After passing to a suitable covering, we may view $\hat{h}$ as a tensor field on $\left(\mathbb{R}^{4} \backslash \mathbb{Z}^{4}\right) \times(-\infty, 0]$ which is invariant under the group $\mathscr{G}$. Moreover, $\hat{h}$ satisfies the heat equation $\frac{\partial}{\partial t} \hat{h}=\Delta_{g_{\text {eucl }}} \hat{h}$, and we have
$$\sup _{\left(\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}\right) \times(-\infty, 0]} r^{\sigma}|\hat{h}(t)|_{g_{\mathrm{eucl}}} \leq 1$$

In the next step, we show that $\hat{h}(t)$ is orthogonal to $g_{\text {eucl }}$ for each $t \in$ $(-\infty, 0]$. Indeed, if we fix a number $t \in(-\infty, 0]$, then we have
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle h^{(j)}\left(t_{j}^{\prime}\right), \bar{g}_{\varepsilon(j)}\left(t_{j}^{\prime}\right), \delta\left(t_{j}^{\prime}\right)\right\rangle_{\bar{g}_{\varepsilon}(j)\left(t_{j}^{\prime}\right), \delta\left(t_{j}^{\prime}\right)} d \operatorname{vol}_{\bar{g}_{\varepsilon}(j)\left(t_{j}^{\prime}\right), \delta\left(t_{j}^{\prime}\right)}=0,$$
where $t_{j}^{\prime}:=t_{j}+t$. Taking the limit as $j \rightarrow \infty$, we obtain
$$\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}}\left\langle\hat{h}(t), g_{\mathrm{eucl}}\right\rangle_{g_{\mathrm{eucl}}} d \operatorname{vol}_{g_{\mathrm{eucl}}}$$
by the dominated convergence theorem.
Finally, since $\hat{h}$ is invariant under the maps $\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{2},-x_{1}, x_{3}, x_{4}\right)$, $\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{1}, x_{2}, x_{4},-x_{3}\right)$, and $\left(x_{1}, x_{2}, x_{3}, x_{4}\right) \mapsto\left(x_{3}, x_{4}, x_{1}, x_{2}\right)$, we conclude that $\int_{\left[-\frac{1}{2}, \frac{1}{2}\right]^{4} \backslash\{0\}} \hat{h}_{i i}(t) d \operatorname{vol}_{g_{\text {eucl }}}=0$ for all $i \in\{1,2,3,4\}$. This contradicts Proposition 5.4. The proof of Theorem 6.2 is now complete. \(\square\)

We next define suitable weighted Hölder spaces. To fix notation, we denote by $d_{t}\left(x, x^{\prime}\right)$ the Riemannian distance with respect to the metric $\bar{g}_{(-32 \omega t)^{-\frac{1}{4}},(-t)^{-\frac{1}{400}}}$ from $x$ to $x^{\prime}$. Moreover, we denote by $P_{x, x^{\prime}}^{t}$ the parallel transport along a minimizing geodesic from $x$ to $x^{\prime}$ with respect to the metric $\bar{g}_{(-32 \omega t)^{-\frac{1}{4}},(-t)^{-\frac{1}{400}}}$.

Definition 6.3. Given real numbers $\alpha \in(0,1), \gamma>0, \sigma>0$, and $\Lambda>0$, we define $\|h\|_{X_{\gamma, \sigma, \Lambda}^{0, \alpha}}$ to be the supremum of the quantity
$$\begin{aligned}
& (-t)^{\gamma}\left((-t)^{-\frac{1}{4}}+r\right)^{\sigma}|h(x, t)| \\
& +(-t)^{\gamma}\left((-t)^{-\frac{1}{4}}+r\right)^{\sigma+2 \alpha}\left(d_{t}\left(x, x^{\prime}\right)^{2}+\left|t-t^{\prime}\right|\right)^{-\alpha}\left|P_{x, x^{\prime}}^{t} h(x, t)-h\left(x^{\prime}, t^{\prime}\right)\right| .
\end{aligned}$$