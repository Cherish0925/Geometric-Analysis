# Mass Rigidity for Hyperbolic Manifolds

- Category: papers
- Identity: doi:10.1007/s00220-019-03623-0
- Content status: fulltext_ok

---

---
source_file: Mass_Rigidity_for_Hyperbolic_Manifolds_b528a13f44b1.pdf
converter: mathpix
format: mmd
---

\title{
MASS RIGIDITY FOR HYPERBOLIC MANIFOLDS
}

\author{
LAN-HSUAN HUANG, HYUN CHUL JANG, AND DANIEL MARTIN
}

Dedicated to Professor Greg Galloway on the occasion of his seventieth birthday

\begin{abstract}
We prove the rigidity of the positive mass theorem for asymptotically hyperbolic manifolds. Namely, if the mass equality $p_{0}=\sqrt{p_{1}^{2}+\cdots+p_{n}^{2}}$ holds, then the manifold is isometric to hyperbolic space. The result was previously proven for spin manifolds [18, 23, 2, 6] or under special asymptotics [1].
\end{abstract}

\section*{1. Introduction}

One of the central topics in differential geometry is to understand how Riemannian manifolds can be characterized under a curvature assumption. The seminal work of R. Schoen and S.-T. Yau [21] of the Riemannian positive mass theorem establishes a characterization of Euclidean space. Specifically, Euclidean space is the unique asymptotically flat manifold with nonnegative scalar curvature that has zero ADM mass, which is an invariant defined at the manifold's infinity. E. Witten [25] later introduced a different method using spinors. M. Min-Oo [18] adapted the spinor approach for strongly asymptotically hyperbolic manifolds (with a corrected assumption by E. Delay [7, Definition 1]) and gave a characterization of hyperbolic space, which was later refined by L. Andersson and M. Dahl [2]. Based on the spinor approach, X. Wang [23] defined the mass and established the positive mass theorem for conformally compact, asymptotically hyperbolic manifolds $\left(X^{n}, g\right)$ whose conformal boundary is the unit round sphere $\left(S^{n-1}, h\right)$ and with the following expansion:
$$g=\frac{1}{(\sinh \rho)^{2}}\left(d \rho^{2}+h+\frac{\rho^{n}}{n} \kappa+O\left(\rho^{n+1}\right)\right)$$
where $\rho$ is a boundary defining function and $\kappa$ is a symmetric (0, 2)-tensor defined on $S^{n-1}$. The mass $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$ of $g$ is defined by
$$p_{0}=\int_{S^{n-1}} \operatorname{tr}_{h} \kappa d \mu_{h}, \quad p_{i}=\int_{S^{n-1}} x_{i} \operatorname{tr}_{h} \kappa d \mu_{h} \quad \text { for } i=1, \ldots, n$$
where $\left(x_{1}, \ldots, x_{n}\right)$ are the Cartesian coordinates of $\mathbb{R}^{n}$ restricted on $S^{n-1}$. It is an intriguing observation that the mass consists of $(n+1)$ numbers $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$, instead of a single number, the ADM mass, as for the asymptotically flat manifolds. In [6], P. Chruściel and M. Herzlich extended the definition of mass to a larger class of manifolds without assuming conformal compactification and obtained a flux integral formula, which we will recall in Definition 2.7. As a result, the following positive mass theorem holds for spin manifolds.

Theorem 1 ([23, 6]). Let $n \geq 3$ and $(X, g)$ an $n$-dimensional asymptotically hyperbolic manifold with scalar curvature $R_{g} \geq-n(n-1)$. Suppose $X$ is spin. Then $p_{0} \geq \sqrt{p_{1}^{2}+\cdots+p_{n}^{2}}$ with equality only if $(X, g)$ is isometric to hyperbolic space.

It has been conjectured that the positive mass theorem for asymptotically hyperbolic manifolds holds without the spin assumption. Assuming that the mass aspect function $\operatorname{tr}_{h} \kappa$ in (1.1) is either everywhere positive, zero, or negative on $S^{n-1}$, L. Andersson, M. Cai, and G. Galloway [1] proved the positive mass theorem for dimensions $3 \leq n \leq 7$. For more general asymptotics, an approach using Jang's equation to the positivity of mass in three dimensions was announced by A. Sakovich. A recent paper [5] of P. Chruściel and E. Delay proves the positivity by a gluing argument in general dimensions. Nevertheless, these two approaches to the positivity of mass are indirect and do not seem to give information about the equality case, which is the focus of the current paper.

Our main result is the following rigidity statement. The technical terms are defined in Section 2. We also refer to Definition 2.3 for the precise definition of asymptotically hyperbolic manifolds, which includes a technical assumption that $g \in C_{\text {loc }}^{\infty}$. See Remark 2.5.

Theorem 2. Let $n \geq 3$ and $(M, g)$ be an $n$-dimensional asymptotically hyperbolic manifold with scalar curvature $R_{g} \geq-n(n-1)$ and with equality $p_{0}=\sqrt{p_{1}^{2}+\cdots+p_{n}^{2}}$, where $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$ is the mass of $g$. Suppose the following holds:
\begin{itemize}
\item[] (★) There is an open neighborhood $\mathcal{M}$ of $g$ in the space of asymptotically hyperbolic metrics on $M$ such that the inequality $p_{0}(\gamma) \geq \sqrt{\left(p_{1}(\gamma)\right)^{2}+\cdots+\left(p_{n}(\gamma)\right)^{2}}$ holds if $\gamma \in \mathcal{M}$ and the scalar curvature satisfies $R_{\gamma}=R_{g}$.
\end{itemize}

Then $(M, g)$ is isometric to hyperbolic space.
Using positivity of mass proven in [5], the assumption (★) can be dropped and thus we arrive at the following result.

Theorem 3. Let $n \geq 3$ and $(M, g)$ an $n$-dimensional asymptotically hyperbolic manifold with scalar curvature $R_{g} \geq-n(n-1)$ and with the equality $p_{0}=\sqrt{p_{1}^{2}+\cdots+p_{n}^{2}}$. Then $(M, g)$ is isometric to hyperbolic space.

We outline the proof of Theorem 2, which is included in Section 4. We show that a metric that realizes the mass equality is a minimizer of a functional $\mathcal{F}$, defined by (4.5), subject to a scalar curvature constraint. By studying the first variation of this functional, we show that such a metric must be static and, in fact, possess a static potential with certain asymptotics. The desired characterization of hyperbolic space follows from proving a static uniqueness result.

We remark that the approach is motivated by a constrained minimization scheme proposed by R. Bartnik [3] for his quasi-local mass program. The connection between the constrained minimization and mass rigidity was recently employed by D. Lee and the first named author in their proof to the rigidity conjecture of the spacetime positive mass theorem [14].

In our proof of Theorem 2, it is essential to analyze the scalar curvature map and to derive the following result.

Theorem 4. Let $(M, g)$ be an $n$-dimensional asymptotically hyperbolic manifold. For $k \geq 2$ and $s \in(-1, n)$, the linearized scalar curvature map
$$L_{g}: C_{-s}^{k, \alpha}(M) \rightarrow C_{-s}^{k-2, \alpha}(M)$$
is surjective. As a consequence, the scalar curvature map is locally surjective at $g$. Namely, there are constants $\epsilon, C>0$ such that if $\left\|\phi-R_{g}\right\|_{C_{-s}^{k-2, \alpha}(M)}<\epsilon$, then there is a metric $\gamma$ with $\|\gamma-g\|_{C_{-s}^{k, \alpha}(M)} \leq$ $C \epsilon$ that realizes the scalar curvature $R_{\gamma}=R_{g}+\phi$.

Theorem 4 is also of independent interest from the perspective of scalar curvature deformation. For example, it produces infinitely many asymptotically hyperbolic metrics with scalar curvature greater than $-n(n-1)$ by perturbation.

We remark that the weighted Hölder space is chosen as our analytical framework because the known results on the positivity of mass require that regularity. It is shown that the Einstein constraint map is surjective among the appropriate weighted Sobolev spaces by E. Delay and J. Fougeirol [8]. However, it does not seem to imply Theorem 4. In fact, our proof relies on a different argument. One difficulty is that the dual space $\left(C_{-s}^{k-2, \alpha}\right)^{*}$ is not well-understood. Efforts are made to analyze the kernel of the adjoint operator $L_{g}^{*}$ on $\left(C_{-s}^{k-2, \alpha}\right)^{*}$ without assuming the kernel elements to decay at infinity. See Section 3 and more specifically, Theorem 3.5.

Finally, we remark that the proof of Theorem 4 uses the assumption that an asymptotically hyperbolic manifold is complete without boundary (see Definition 2.3). For manifolds with compact boundary, while the same argument still works if one imposes either Dirichlet or Neumann type condition on the metrics, we need the surjectivity to hold for tensors with stronger vanishing condition at the boundary to establish the mass rigidity. In a forthcoming paper, we use a different argument and extend Theorem 4 for metrics that coincide with $g$ of infinite order at the boundary. It enables us to prove the mass rigidity for asymptotically locally hyperbolic manifolds. In that setting, the model spaces that we consider have compact boundary with natural geometric boundary conditions.

Acknowledgement. The project was initiated while the authors participated in the 2017 summer program on Geometry and Relativity at the Erwin Schrödinger Institute. We would like to express our sincere gratitude to the organizers Robert Beig, Piotr Chruściel, Michael Eichmair, Greg Galloway, Richard Schoen, Tim-Torben Paetz for their warm hospitality and the inspiring program.

The project was partially supported by the NSF Career award DMS-1452477. L.-H. Huang was also supported by Simons Fellowship of the Simons Foundation and von Neumann Fellowship at the Institute for Advanced Study.

\section*{2. Preliminaries}
2.1. Weighted Hölder spaces and asymptotically hyperbolic manifolds. Denote by $\mathbb{H}^{n}$ the $n$-dimensional hyperbolic space with scalar curvature $-n(n-1)$. As our model for hyperbolic space, we consider the upper-sheet of the hyperboloid in Minkowski space ( $\mathbb{R}^{n, 1},-d t^{2}+d x_{1}^{2}+\cdots+d x_{n}^{2}$ ), defined by
$$\mathbb{H}^{n}=\left\{(x, t)=\left(x_{1}, \ldots, x_{n}, t\right) \in \mathbb{R}^{n, 1}: t=\sqrt{1+x_{1}^{2}+\cdots+x_{n}^{2}}\right\} .$$
The restriction of the Minkowski metric to the upper-sheet hyperboloid is hyperbolic space and can be expressed in spherical coordinates as
$$b=\frac{1}{1+r^{2}} d r^{2}+r^{2} h,$$
where $r=|x|:=\sqrt{x_{1}^{2}+\cdots+x_{n}^{2}}$ is the radial coordinate, and $h$ is the standard metric on the round unit $(n-1)$-sphere. We refer $\left(\mathbb{R}^{n}, b\right)$ as the hyperboloid model of hyperbolic space.

The volume form of $b$ is $d \mu_{b}=\frac{r^{n-1}}{\sqrt{1+r^{2}}} d r d \omega$, where $d \omega$ is the volume form on the round unit $(n-1)$ -sphere. By the co-area formula, it is direct to see that the induced volume form on $S_{r}=\{|x|=r\}$ of the hyperbolic metric $b$ is the same as the standard volume form on the round $(n-1)$-sphere of radius $r$.

Let $B$ be an open ball in $\mathbb{R}^{n}$ centered at the origin. Denote $\mathbb{H}^{n} \backslash B=\left(\mathbb{R}^{n} \backslash B, b\right)$. We fix an orthonormal frame $\left\{e_{1}, \ldots, e_{n}\right\}$ on $\mathbb{H}^{n} \backslash B$ defined by, with respect to the spherical coordinates $\left\{r, \theta_{1}, \ldots, \theta_{n-1}\right\}$,
$$e_{1}=\sqrt{1+r^{2}} \frac{\partial}{\partial r}, \quad e_{2}=r^{-1} \frac{\partial}{\partial \theta_{1}}, \quad \ldots, \quad e_{n}=\left(r \sin \left(\theta_{1}\right) \ldots \sin \left(\theta_{n-2}\right)\right)^{-1} \frac{\partial}{\partial \theta_{n-1}} .$$

Definition 2.1. For $k=0,1,2, \ldots, \alpha \in(0,1)$, and $q \in \mathbb{R}$, we define the weighted Hölder spaces $C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)$ as the collection of $C_{\text {loc }}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)$ functions $f$ on $\mathbb{H}^{n} \backslash B$ that satisfy
$$\|f\|_{C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)}:=\sum_{\ell=0,1, \ldots, k} \sup _{x \in \mathbb{H}^{n} \backslash B}|x|^{q}\left|\nabla^{\ell} f(x)\right|_{b}+\sup _{x \in \mathbb{H}^{n} \backslash B}|x|^{q}\left[\nabla^{k} f\right]_{\alpha ; B_{1}(x)}<\infty,$$
where $\stackrel{\circ}{\nabla}$ is the covariant derivative with respect to $b$,
$$\left[\stackrel{\circ}{\nabla}^{k} f\right]_{\alpha ; B_{1}(x)}=\sup _{1 \leq i_{1}, \ldots, i_{k} \leq n} \sup _{y \neq z \in B_{1}(x)} \frac{\left|e_{i_{1}} \cdots e_{i_{k}}(f)(y)-e_{i_{1}} \cdots e_{i k}(f)(z)\right|}{\left(d_{b}(y, z)\right)^{\alpha}},$$
and $B_{1}(x)$ is the unit ball centered at $x$ intersecting with $\mathbb{H}^{n} \backslash B$. We extend the definition to tensors of arbitrary types: a tensor $h \in C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)$ if and only if each tensor component with respect to the orthonormal frame lies in $C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)$.

Let $M$ be a smooth manifold covered by an atlas that consists of a non-compact chart $\Phi: M \backslash K \cong$ $\mathbb{H}^{n} \backslash B$ and finitely many compact charts. We define the weighted Hölder norm $\|f\|_{C_{-q}^{k, \alpha}(M)}$ (for a function or tensor) to be the sum of the weighted norm $\left\|\Phi_{*} f\right\|_{C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)}$ and the usual $C^{k, \alpha}$ norms on compact charts. Denote by $C_{-q}^{k, \alpha}(M)$ the completion of $C_{c}^{k, \alpha}(M)$ functions with respect to the weighted Hölder norm. We often suppress $M$ when the context is clear.

Notation. Throughout the paper, we use the notation $O^{k, \alpha}\left(r^{-q}\right)$ to denote a function or tensor, that belongs to the corresponding weighted space $C_{-q}^{k, \alpha}(M)$. We simply write $O\left(r^{-q}\right)$ in place of $O^{0}\left(r^{-q}\right)$.

We collect the following basic facts about the weighted Hölder spaces.
Lemma 2.2. Let $k=0,1,2, \ldots, \alpha \in(0,1)$, and $q, s \in \mathbb{R}$.
\begin{itemize}
\item[(1)] $|x|^{-q} \in C_{-q}^{k, \alpha}(M \backslash K)$.
\item[(2)] $f \in C_{-q}^{k, \alpha}(M \backslash K)$ if and only if $|x|^{s} f \in C_{s-q}^{k, \alpha}(M \backslash K)$.
\item[(3)] If $f \in C_{-s}^{k, \alpha}, g \in C_{-q}^{k, \alpha}$, then $f g \in C_{-s-q}^{k, \alpha}$ and there is a constant $C>0$ such that
$$\|f g\|_{C_{-s-q}^{k, \alpha}} \leq C\|f\|_{C_{-s}^{k, \alpha}}\|g\|_{C_{-q}^{k, \alpha}} .$$
\item[(4)] The inclusion $C_{-s}^{k, \alpha}(M) \subset C_{-s+\epsilon}^{k, \beta}(M)$ is compact for any $\epsilon>0$ and $\beta<\alpha$.
\end{itemize}

Proof. The first three statements follow directly from the definition. The last statement is standard compact embedding for weighted norms. While similar statements can be found in [17, Lemma 3.6] and [7, Proposition 8], we include the proof for completeness as the weighted norms are defined with slight variations in the literature. Let $\left\{u_{i}\right\}$ be a sequence of functions in $C_{-s}^{k, \alpha}$ with $\left\|u_{i}\right\|_{C_{-s}^{k, \alpha}}=1$. Applying Arzela-Ascoli on a sequence of compact sets that exhaust $M$ and by a diagonal sequence argument, there is a subsequence of $\left\{u_{i}\right\}$ (which we still denote by $\left\{u_{i}\right\}$, without loss of generality) and a function $u \in C_{\text {loc }}^{k, \alpha}$ so that $u_{i}$ converges to $u$ locally uniformly in $C^{k, \beta}$. That is, for $\epsilon>0$ and a compact subset $\Omega$, there is an integer $I$ (depending on $\epsilon$ and $\Omega$ ) such that $\left\|u-u_{i}\right\|_{C^{k, \beta}(\Omega)}<\epsilon$ for all $i \geq I$. In fact, $u \in C_{-s}^{k, \beta}$ because, for each compact set $\Omega$,
$$\|u\|_{C_{-s}^{k, \beta}(\Omega)}=\lim _{i \rightarrow \infty}\left\|u_{i}\right\|_{C_{-s}^{k, \beta}(\Omega)} \leq 1 .$$
Let $B_{r}$ be the coordinate ball of radius $r$. Using $\left\|u_{i}-u\right\|_{C_{-s+\epsilon}^{k, \beta}\left(M \backslash B_{r}\right)} \leq r^{-\epsilon}\left(\left\|u_{i}\right\|_{C_{-s}^{k, \beta}(M)}+\|u\|_{C_{-s}^{k, \beta}(M)}\right)$, we have that $u_{i}$ converges to $u$ in $C_{-s+\epsilon}^{k, \beta}(M)$. \(\square\)

Definition 2.3. Let $n \geq 3$ and $q \in\left(\frac{n}{2}, n\right)$. Let $M$ be an $n$-dimensional, connected, complete manifold without boundary endowed with a Riemannian metric $g \in C_{\text {loc }}^{\infty}$. We say that $(M, g)$ is asymptotically hyperbolic (of order $q$ ) if the following holds:
\begin{itemize}
\item[(1)] There exists a diffeomorphism $M \backslash K \cong \mathbb{H}^{n} \backslash B$ for some compact subset $K \subset M$. We call the induced coordinate chart as the chart at infinity.
\item[(2)] With respect to the chart at infinity, $g-b \in C_{-q}^{2, \alpha}(M \backslash K)$.
\item[(3)] The scalar curvature satisfies $R_{g}+n(n-1) \in C_{-n-\epsilon}^{0, \alpha}(M)$ for some $\epsilon>0$.
\end{itemize}

Remark 2.4. By direct computation, the assumption (2) implies that the Ricci curvature of $g$ satisfies $\operatorname{Ric}_{g}=-(n-1) g+O^{0, \alpha}\left(r^{-q}\right)$.

Remark 2.5. Note the assumption $g \in C_{\text {loc }}^{\infty}$. We add this technical assumption to employ elliptic interior regularity for distribution solutions. Namely, if a distribution solution $u$ weakly solves $a_{i j} \partial_{i j}^{2}+b_{i} \partial_{i} u+c u=f$ and if $f \in C_{\text {loc }}^{k-2, \alpha}$, then $u \in C_{\text {loc }}^{k, \alpha}$, provided that the coefficients $a_{i j}, b_{i}, c$ are locally smooth. This elliptic regularity is only used in the proofs of Theorem 4 and Theorem 4.3. If the regularity statement holds for coefficients that are just Hölder regular, then that technical assumption may be dropped.

To compare Definition 2.3 with various notions of asymptotically hyperbolic manifolds in the existing literature, we express the assumption (2) in Definition 2.3 in coordinates. It appears that our asymptotic assumption is more general than (1.1).

Lemma 2.6. $A(0,2)$-tensor $g$ satisfies $g-b \in C_{-q}^{2, \alpha}(M \backslash K)$ if and only if the tensor components have the following asymptotics in spherical coordinates:
$$g=\left(\frac{1}{1+r^{2}}+O^{2, \alpha}\left(r^{-2-q}\right)\right) d r^{2}+O^{2, \alpha}\left(r^{-q}\right) d r d \theta_{j}+\left(r^{2} h_{j \ell}+O^{2, \alpha}\left(r^{2-q}\right)\right) d \theta_{j} d \theta_{\ell} \quad \text { as } r \rightarrow \infty .$$
By changing the coordinate $r=\frac{1}{\sinh \rho}$, we can express $g$ as
$$g=\frac{1}{(\sinh \rho)^{2}}\left[\left(1+O\left(\rho^{q}\right)\right) d \rho^{2}+O\left(\rho^{q}\right) d \rho d \theta_{i}+\left(h_{j \ell}+O\left(\rho^{q}\right)\right) d \theta_{j} d \theta_{\ell}\right] \quad \text { as } \rho \rightarrow 0,$$
where we slightly abuse the $O$-notation in the previous expression and write $u=O\left(\rho^{q}\right)$ if $\frac{u}{\rho^{q}}$ is bounded as $\rho \rightarrow 0$.

Proof. Via the diffeomorphism on the chart at infinity, it suffices to prove the result for tensors defined on $\mathbb{H}^{n} \backslash B$. Express $g$ in the spherical coordinates as follows:
$$g=A d r^{2}+2 \sum_{j} B_{j} d r d \theta_{j}+\sum_{j, \ell} C_{j \ell} d \theta_{j} d \theta_{\ell} .$$
By definition, $\kappa:=g-b$ belongs to $C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)$ if and only if each tensor component $\kappa\left(e_{i}, e_{j}\right) \in$ $C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)$. By (2.2) and (2.3), we have
$$\kappa\left(e_{1}, e_{1}\right)=\left(1+r^{2}\right) A, \quad \kappa\left(e_{1}, e_{j+1}\right)=\sqrt{1+r^{2}} r^{-1} B_{j}, \quad \text { and } \quad \kappa\left(e_{j+1}, e_{\ell+1}\right)=r^{-2} C_{j \ell} .$$
Thus, $\kappa \in C_{-q}^{k, \alpha}\left(\mathbb{H}^{n} \backslash B\right)$ if and only if the tensor components satisfy
$$A \in C_{-2-q}^{k, \alpha}, \quad B_{j} \in C_{-q}^{k, \alpha}, \quad \text { and } \quad C_{j \ell} \in C_{2-q}^{k, \alpha} .$$ \(\square\)
2.2. Wang-Chruściel-Herzlich mass, and an alternative definition. X. Wang [23] defined the mass for asymptotically hyperbolic manifolds that are conformally compact. For the class of asymptotically hyperbolic manifolds adopted in the current paper, we use the following more general definition of P. Chruściel and M. Herzlich [6].

Definition 2.7. Let $(M, g)$ be an asymptotically hyperbolic manifold. Given a function $V \in$ $C^{1}(M \backslash K)$, we define the mass integral
$$H_{g}(V)=\lim _{r \rightarrow \infty} \int_{S_{r}}\left[V(\operatorname{div} h-d(\operatorname{t} \stackrel{\circ}{\operatorname{tr}} h))\left(\nu_{0}\right)+(\operatorname{tr} h) d V\left(\nu_{0}\right)-h\left(\stackrel{\circ}{\nabla} V, \nu_{0}\right)\right] d \sigma_{b},$$
where $h=g-b, \nu_{0}$ is the outward unit normal vector to $S_{r}=\{|x|=r\}$, and div, $\stackrel{\circ}{\mathrm{tr}}, \stackrel{\circ}{\nabla}$, are all with respect to $b$. The volume form $d \sigma_{b}$ is the restriction of the volume form of $b$ on $S_{r}$. The mass of Wang-Chruściel-Herzlich is defined by
$$p_{0}(g)=H_{g}\left(\sqrt{1+r^{2}}\right) \quad \text { and } \quad p_{i}(g)=H_{g}\left(x_{i}\right) \text { for } i=1, \ldots, n .$$
We may omit $g$ and simply write the mass $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$ when the context is clear.
Remark 2.8. In the above definition, we can replace the functions $\sqrt{1+r^{2}}$ and $x_{i}$ by $\sqrt{1+r^{2}}+$ $O^{2}\left(r^{1-q}\right)$ and $x_{i}+O^{2}\left(r^{1-q}\right)$ respectively, since the differences in the corresponding mass integrals go to zero in the limit. For the same reason, we may also replace $\nu_{0}$, div, $\stackrel{\circ}{\mathrm{tr}}, \stackrel{\circ}{\nabla}$, and $d \sigma_{b}$ in (2.4) by the corresponding objects with respect to another asymptotically hyperbolic metric and still obtain the same limit.

Remark 2.9. The quantity $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$ is a geometric invariant among an appropriate class of charts at infinity (see [6], also [12]). We denote the functions appearing in the above definition by
$$V_{0}=\sqrt{1+r^{2}} \quad \text { and } \quad V_{i}=x_{i} \quad \text { for } i=1, \ldots, n .$$
In $\mathbb{H}^{n}$, these functions satisfy the differential equation $\stackrel{\circ}{\nabla}^{2} V_{i}=V_{i} b$, for $i=0,1, \ldots, n$. They are the so-called static potentials. We will discuss general properties of static potentials in an asymptotically hyperbolic manifold in Section 3.

We recall an equivalent definition of mass, which will be used in the proof of the main theorem. This formula is known to the experts and is stated in [13, Theorem 3.3], whose proof is similar to the analogous formula for asymptotically flat manifolds.

Proposition 2.10. Let $(M, g)$ be an asymptotically hyperbolic manifold. If $V \in C^{2}(M \backslash K)$ satisfies
$$\stackrel{\circ}{\nabla}^{2} V=V b,$$
then
$$\lim _{r \rightarrow \infty} \int_{S_{r}}\left(\operatorname{Ric}_{g}+(n-1) g\right)\left(\stackrel{\circ}{\nabla} V, \nu_{0}\right) d \sigma_{b}=-\frac{n-2}{2} H(V),$$
provided the quantity on either side of the equation converges.
2.3. Operators asymptotic to $\Delta-n$. To analyze the scalar curvature operator on an asymptotically hyperbolic manifold, the following class of operators naturally appears.

Definition 2.11. Let $(M, g)$ be asymptotically hyperbolic. Let $\Delta$ be the Laplace-Beltrami operator of $g$, which is the trace of the covariant Hessian. For $k \geq 2$, we say that the differential operator $T: C_{-s}^{k, \alpha} \rightarrow C_{-s}^{k-2, \alpha}$ defined by $T u=\Delta u+\xi \cdot \nabla u+\eta u$ is asymptotic to $\Delta-n$ if there is a number $\epsilon>0$ such that the vector field $\xi \in C_{-\epsilon}^{k-2, \alpha}$ and the function $\eta+n \in C_{-\epsilon}^{k-2, \alpha}$.

We recall the following classical result on isomorphism.
Lemma 2.12. Let $(M, g)$ be an $n$-dimensional asymptotically hyperbolic manifold and $s \in(-1, n)$. The operator $T_{0}: C_{-s}^{k, \alpha}(M) \rightarrow C_{-s}^{k-2, \alpha}(M)$ defined by $T_{0} u=\Delta u-n u$ is an isomorphism.

Proof. The isomorphism result is proven for asymptotically hyperbolic manifolds that are conformally compact in [16, Proposition 3.3] (based on the argument of [11, Section 3]; see also [17] for a general class of operators.) It is clear that the proof can be adapted for our class of asymptotically hyperbolic manifolds. \(\square\)

We also need the following standard Fredholm property for our class of operators. Note similar statements under greater generality can be found in [17], but we include a proof more specific to our setting for completeness.

Proposition 2.13. Let $(M, g)$ be an $n$-dimensional asymptotically hyperbolic manifold and $s \in$ $(-1, n)$. Let $T: C_{-s}^{k, \alpha} \rightarrow C_{-s}^{k-2, \alpha}$ be asymptotic to $\Delta-n$. Then $T$ is Fredholm.

Proof. We write $T u=T_{0} u+\xi \cdot \nabla u+(\eta+n) u$. Note $T_{0}$ is an isomorphism by Lemma 2.12, and hence Fredholm. To show that $T$ is Fredholm, it suffices to show that the map $T-T_{0}: C_{-s}^{k, \alpha} \rightarrow C_{-s}^{k-2, \alpha}$ is compact.

Let $\left\{u_{i}\right\}$ be a sequence of functions in $C_{-s}^{k, \alpha}$ with $\left\|u_{i}\right\|_{C_{-s}^{k, \alpha}}=1$. We show that $\left\{\left(T-T_{0}\right) u_{i}\right\}$ has a convergent subsequence in $C_{-s}^{k-2, \alpha}$. By Lemma 2.2, $C_{-s}^{k, \alpha} \subset C_{-s+\epsilon}^{k}$ is compact for $\epsilon>0$, so there is a subsequence (still denoted by $\left\{u_{i}\right\}$ without loss of generality) that converges to $u$ in $C_{-s+\epsilon}^{k}$.

Observe the sequence $\left\{\left(T-T_{0}\right) u_{i}\right\}$ converges in $C_{-s}^{k-2, \alpha}$ because
$$\begin{aligned}
\left\|\left(T-T_{0}\right)\left(u_{i}-u\right)\right\|_{C_{-s}^{k-2, \alpha}} & =\left\|\xi \cdot \nabla\left(u_{i}-u\right)+(\eta+n)\left(u_{i}-u\right)\right\|_{C_{-s}^{k-2, \alpha}} \\
& \leq C\left[\|\xi\|_{C_{-\epsilon}^{k-2, \alpha}}\left\|\nabla\left(u_{i}-u\right)\right\|_{C_{-s+\epsilon}^{k-2, \alpha}}+\|\eta+n\|_{C_{-\epsilon}^{k-2, \alpha}}\left\|u_{i}-u\right\|_{C_{-s+\epsilon}^{k-2, \alpha}}\right] \\
& \leq C\left\|u_{i}-u\right\|_{C_{-s+\epsilon}^{k-1, \alpha}} \\
& \leq C\left\|u_{i}-u\right\|_{C_{-s+\epsilon}^{k}} \rightarrow 0 \quad \text { as } i \rightarrow \infty .
\end{aligned}$$ \(\square\)

\section*{3. Surjectivity of the linearized scalar curvature map}

Let $(\Omega, g)$ be a Riemannian manifold. The linearization $L_{g}$ of the scalar curvature map at $g$ acts on a symmetric $(0,2)$-tensor $h \in C_{\text {loc }}^{2}$ by the formula
$$L_{g} h=-\Delta(\operatorname{tr} h)+\operatorname{div} \operatorname{div} h-h \cdot \operatorname{Ric}_{g},$$
and the formal $L^{2}$-adjoint operator $L_{g}^{*}$ is given by, for a function $V \in C_{\text {loc }}^{2}$,
$$L_{g}^{*} V=-(\Delta V) g+\nabla^{2} V-V \operatorname{Ric}_{g} .$$
Here div, $\operatorname{tr}, \cdot, \Delta$, and $\nabla$ are all taken with respect to $g$.
We say that $(\Omega, g)$ is static if it admits a function $V$, not identically zero, that satisfies the static equation
$$L_{g}^{*} V=0 .$$
We call a solution $V$ to this equation a static potential. Equation (3.3) is equivalent to the following equation:
$$\nabla^{2} V=\left(\operatorname{Ric}_{g}-\frac{1}{n-1} R_{g} g\right) V .$$

Example 3.1. It is well-known that a static manifold has constant scalar curvature on each connected component [9], so a static asymptotically hyperbolic manifold (which is assumed to be connected in Definition 2.3) must have constant scalar curvature $-n(n-1)$. Thus, (3.3) implies
$$\begin{aligned}
\nabla^{2} V & =\left(\operatorname{Ric}_{g}+n g\right) V \\
\Delta V & =n V .
\end{aligned}$$
The prototype of a static asymptotically hyperbolic manifold is hyperbolic space. Recall in Remark 2.9, the space of static potentials is an ( $n+1$ )-dimensional real vector space spanned by the functions $\sqrt{1+r^{2}}, x_{1}, \ldots, x_{n}$ with respect to the coordinates of the hyperboloid model. They come from the restriction of the Minkowski coordinate functions $t, x_{1}, \ldots, x_{n}$ to the hyperboloid.

The goal of this section is to analyze the growth rate of $V$ solving $L_{g}^{*} V=\tau$ on an asymptotically hyperbolic manifold $(M, g)$ where $\tau \in C_{1-q}^{0}$. Specifically, we show in Theorem 3.5 below that such $V$ must either grow linearly in a cone region or go to zero at infinity. As an application (the case $\tau=0$ ), at the end of this section we prove Theorem 4 that $L_{g}$ is surjective between the appropriate weighted Hölder spaces. We also use Theorem 3.5 (the case $\tau \neq 0$ ) in the proof of Theorem 4.3 in the next section.

We remark that it is possible to obtain more detailed asymptotics of $V$ (at least for the case $\tau=0$ ) as discussed in [4, Remark A.3] by their analysis. Here we establish elementary properties for a class of inhomogeneous, second-order linear ODEs that suffice for our purpose.

We analyze the asymptotic behavior of a static potential, by studying the static equation along geodesic rays. Note $\nabla^{2} V=\left(\operatorname{Ric}_{g}+n g\right) V=\left(g+O^{0, \alpha}\left(r^{-q}\right)\right) V$ by the asymptotically hyperbolic assumption. The corresponding equation along a geodesic ray is asymptotic to $u^{\prime \prime}=u$. We prove in the next three technical lemmas that the solutions to a large class of ODEs share similar properties as the solutions to $u^{\prime \prime}=u$, which are generated by $e^{t}, e^{-t}$.

Lemma 3.2. Let $P(t), Q(t) \in C^{0, \alpha}([0, \infty))$ and $Q>0$. Consider the ODE given by
$$u^{\prime \prime}=P u^{\prime}+Q u .$$

Then the following holds:
\begin{itemize}
\item[(1)] A solution $u$ has at most one zero, unless $u$ is identically zero.
\item[(2)] If $u$ and $v$ are two solutions satisfying the initial condition $u(0) \geq v(0)$ and $u^{\prime}(0) \geq v^{\prime}(0)$, then $u(t)>v(t)$ and $u^{\prime}(t)>v^{\prime}(t)$ for all $t>0$, unless $u$ is identical to $v$.
\item[(3)] There is a solution $u$ with $u(t)>0$ and $u^{\prime}(t)<0$, for all $t$.
\end{itemize}

Proof. Let $K(t)=\exp \left(-\int_{0}^{t} P(s) d s\right)>0$. Then
$$\left(K u^{\prime}\right)^{\prime}=K Q u .$$
To see (1), suppose that $u$ is not identically zero and, to give a contradiction, that $u$ has two or more zeros. Let $t_{1}<t_{2}$ be two adjacent zeros. We may without loss of generality assume that $u>0$ on $\left(t_{1}, t_{2}\right)$. This implies that $u^{\prime}\left(t_{1}\right) \geq 0$ and $u^{\prime}\left(t_{2}\right) \leq 0$. In fact, both inequalities are strict; otherwise $u$ is identically zero by uniqueness of solutions. However, this contradicts the fact that $K u^{\prime}$ is increasing on $\left[t_{1}, t_{2}\right]$ by (3.6). For (2), by linearity it suffices to show that if $u$ is a solution satisfying the initial condition $u(0) \geq 0$ and $u^{\prime}(0) \geq 0$, then $u(t)>0$ and $u^{\prime}(t)>0$ for all $t>0$, unless $u$ is identically zero. The desired statement in (2) follows from (3.6) and by observing that if $u \geq 0$ then $K u^{\prime}$ is increasing.

We now prove (3) by constructing a compact family of solutions. For an integer $j>0$, let $u_{j}$ be the solution that satisfies $u_{j}(0)=1$ and $u_{j}(j)=0$. By (1) and (2), we have $0 \leq u_{j}<u_{j+1}<u_{j+2}<$ $\cdots<1$ and $u_{j}^{\prime}<u_{j+1}^{\prime}<u_{j+2}^{\prime}<\cdots<0$ for $t \in(0, j]$. Using (3.5) to bound the higher derivatives, we see that $u_{j}$ is locally uniformly bounded in $C^{2, \alpha}$. By Arzela-Ascoli, a subsequence locally uniformly converges to a solution $u$ in $C^{2}([0, \infty))$ that satisfies $u(0)=1$ and $0 \leq u(t) \leq 1, u^{\prime} \leq 0$ for all $t$. It is straightforward to verify that the inequalities are strict: $u(t)>0$ and $u^{\prime}(t)<0$ for all $t$. \(\square\)

Lemma 3.3. Let $P(t), Q(t) \in C^{0, \alpha}([0, \infty))$. Suppose $1+Q>0$ and that there are constants $d, C_{0}>0$ such that $|P(t)|,|Q(t)| \leq C_{0} e^{-d t}$. Then there are two linearly independent solutions $u_{1}$ and $u_{2}$ to the homogeneous equation
$$u^{\prime \prime}=P u^{\prime}+(1+Q) u,$$
and $u_{1}, u_{2}$ satisfy the following: there is a constant $C>0$ such that, for all $t$,
$$\begin{array}{ll}
C^{-1} e^{t} \leq u_{1}(t) \leq C e^{t}, & C^{-1} e^{t} \leq u_{1}^{\prime}(t) \leq C e^{t}, \\
C^{-1} e^{-t} \leq u_{2}(t) \leq C e^{-t}, & C^{-1} e^{-t} \leq-u_{2}^{\prime}(t) \leq C e^{-t} .
\end{array}$$
Proof. Let $u_{1}$ be a solution with the initial condition $u_{1}(0)=1$ and $u_{1}^{\prime}(0)>0$. By (2) in Lemma 3.2, we have $u_{1}>0$ and $u_{1}^{\prime}>0$ for all $t$. Let $w(t)=u_{1}(t)+u_{1}^{\prime}(t)$. Then $w>0$ satisfies
$$w^{\prime}=(1+P) u_{1}^{\prime}+(1+Q) u_{1} .$$
This implies the following differential inequality for $w$ :
$$(1-|P|-|Q|) w \leq w^{\prime} \leq(1+|P|+|Q|) w .$$
Integrating the inequality gives
$$w(0) \exp \left(\int_{0}^{t}(1-|P(s)|-|Q(s)|) d s\right) \leq w(t) \leq w(0) \exp \left(\int_{0}^{t}(1+|P(s)|+|Q(s)|) d s\right) .$$
That is, there is a constant $C_{1}>0$ (depending only on $w(0),\|P\|_{L^{1}}$, and $\|Q\|_{L^{1}}$ ) such that
$$C_{1}^{-1} e^{t} \leq u_{1}(t)+u_{1}^{\prime}(t) \leq C_{1} e^{t} .$$
This gives the upper bound for $u_{1}, u_{1}^{\prime}$ in (3.7). To derive the lower bound for $u_{1}, u_{1}^{\prime}$, we set $z(t)=$ $u_{1}(t)-u_{1}^{\prime}(t)$. Then $z^{\prime}=-z-P u_{1}^{\prime}-Q u_{1}$ and $\left|z^{\prime}+z\right| \leq 2 C_{0} C_{1} e^{(1-d) t}$. Solving the differential inequality gives $|z| \leq C_{2}\left(e^{(1-d) t}+e^{-t}+t e^{-t}\right)$ for some constant $C_{2}>0$. For $t$ sufficiently large, we derive $\left|u_{1}(t)-u_{1}^{\prime}(t)\right| \leq \frac{1}{2} C_{1}^{-1} e^{t}$. Together with (3.8), we obtain the desired estimate (3.7) for $u_{1}, u_{1}^{\prime}$.

By (3) of Lemma 3.2, there is a solution $u_{2}$ so that $u_{2}(t)>0$ and $u_{2}^{\prime}(t)<0$ for all $t$. Set $h(t)=u_{2}(t)-u_{2}^{\prime}(t)$. Then $h>0$ satisfies
$$h^{\prime}=(1-P) u_{2}^{\prime}-(1+Q) u_{2},$$
and hence $(-1-|Q|-|P|) h \leq h^{\prime} \leq(-1+|Q|+|P|) h$. Just as computing above, we have $C^{-1} e^{-t} \leq$ $u_{2}(t)-u_{2}^{\prime}(t) \leq C e^{-t}$, which gives the upper bound for $u_{2}, u_{2}^{\prime}$ in (3.7). Similarly, by estimating the differential inequality for $u_{2}+u_{2}^{\prime}$, we derive the desired lower bound.

Lastly, we note that the two solutions $u_{1}, u_{2}$ are linearly independent because their Wronskian is not zero and furthermore, by (3.7),
$$\operatorname{det}\left[\begin{array}{ll}
u_{1} & u_{2} \\
u_{1}^{\prime} & u_{2}^{\prime}
\end{array}\right]=u_{1} u_{2}^{\prime}-u_{2} u_{1}^{\prime} \leq-2 C^{-2} \quad \text { for all } t .$$ \(\square\)

Lemma 3.4. Let $P(t), Q(t) \in C^{0, \alpha}([0, \infty))$ and $f(t) \in C^{0}([0, \infty))$. Suppose $1+Q>0$ and that there are constants $d, C_{0}>0$ such that $|P(t)|,|Q(t)|,|f(t)| \leq C_{0} e^{-d t}$. Let $u$ solve
$$u^{\prime \prime}=P u^{\prime}+(1+Q) u+f .$$
Then there are constants $C>0$ and $c_{1}, c_{2}$ such that, for all $t \geq a$,
$$\left|u(t)-\left(c_{1} u_{1}(t)+c_{2} u_{2}(t)\right)\right| \leq\left\{\begin{array}{ll}
C e^{-d t} & \text { for } d \neq 1 \\
C t e^{-t} & \text { for } d=1
\end{array} .\right.$$

Proof. Let $u_{p}$ be a particular solution to (3.10). Notice that $u-u_{p}$ satisfies the homogeneous equation, and hence is a linear combination of $u_{1}$ and $u_{2}$, where $\left\{u_{1}, u_{2}\right\}$ is the set of fundamental solutions from Lemma 3.3. It suffices to show that the estimate (3.11) holds for $u_{p}$.

By the method of variation of parameters, we can choose $u_{p}$ to be
$$u_{p}=\alpha_{1} u_{1}+\alpha_{2} u_{2},$$
where the functions $\alpha_{1}, \alpha_{2}$ are defined by
$$\begin{aligned}
& \alpha_{1}(t)=-\int_{0}^{t} \frac{u_{2}(s) f(s)}{u_{1}(s) u_{2}^{\prime}(s)-u_{2}(s) u_{1}^{\prime}(s)} d s \\
& \alpha_{2}(t)=\int_{0}^{t} \frac{u_{1}(s) f(s)}{u_{1}(s) u_{2}^{\prime}(s)-u_{2}(s) u_{1}^{\prime}(s)} d s
\end{aligned}$$

If $d>1$, using (3.7), (3.9), and the assumption on $f$, we see that both integrals converge as $t \rightarrow \infty$. Let $A_{i}=\lim _{t \rightarrow \infty} \alpha_{i}(t)$ for $i=1,2$. There is a constant $C>0$ so that
$$\begin{aligned}
& \left|\alpha_{1}(t)-A_{1}\right| \leq \int_{t}^{\infty}\left|\frac{u_{2}(s) f(s)}{u_{1}(s) u_{2}^{\prime}(s)-u_{2}(s) u_{1}^{\prime}(s)}\right| d s \leq C \int_{t}^{\infty} e^{-s}|f(s)| d s \leq C e^{-(d+1) t} \\
& \left|\alpha_{2}(t)-A_{2}\right| \leq \int_{t}^{\infty}\left|\frac{u_{1}(s) f(s)}{u_{1}(s) u_{2}^{\prime}(s)-u_{2}(s) u_{1}^{\prime}(s)}\right| d s \leq C \int_{t}^{\infty} e^{s}|f(s)| d s \leq C e^{-(d-1) t}
\end{aligned}$$
It implies that
$$\left|u_{p}-A_{1} u_{1}-A_{2} u_{2}\right| \leq\left|\alpha_{1}-A_{1}\right| u_{1}+\left|\alpha_{2}-A_{2}\right| u_{2} \leq C e^{-d t} \text {. }$$

If $0<d \leq 1$, then $\lim _{t \rightarrow \infty} \alpha_{2}(t)$ may not converge. Nevertheless, there is a constant $C>0$ such that $\left|\alpha_{2}\right| \leq C e^{(1-d) t}$ if $d \neq 1$ and $\left|\alpha_{2}\right| \leq C t$ if $d=1$. Together with the above estimate for $\alpha_{1}$, we obtain
$$\left|u_{p}-A_{1} u_{1}\right| \leq\left|\alpha_{1}-A_{1}\right| u_{1}+\left|\alpha_{2}\right| u_{2} \leq\left\{\begin{array}{ll}
C e^{-d t} & \text { for } d \neq 1 \\
C t e^{-t} & \text { for } d=1
\end{array} .\right.$$ \(\square\)

We proceed to discuss the asymptotics of a function that solves the static equation up to an error term. We define a cone $U$ as an unbounded open subset in $M \backslash K$ that consists of points in spherical coordinates such that, for some $r_{0}>0$ and a non-empty open subset $\Theta$ in the domain of the angular coordinates on $S^{n-1}$ :
$$U=\left\{\left(r, \theta_{1}, \cdots, \theta_{n-1}\right) \in M \backslash K: r>r_{0} \text { and }\left(\theta_{1}, \ldots, \theta_{n-1}\right) \in \Theta\right\} .$$

Theorem 3.5. Let $(M, g)$ be an asymptotically hyperbolic manifold, and $V \in C_{\text {loc }}^{2}(M \backslash K)$ satisfy
$$L_{g}^{*} V=\tau$$
where $\tau \in C_{1-q}^{0}(M \backslash K)$ is a symmetric (0, 2)-tensor. Then $V$ satisfies precisely one of the following:
\begin{itemize}
\item[(1)] There is a cone $U \subset M \backslash K$ and a constant $C>0$ such that
$$C^{-1}|x| \leq|V(x)| \leq C|x| \quad \text { for all } x \in U .$$
\item[(2)] There are constants $C>0$ and $0<d \leq 1$ such that
$$|V(x)| \leq C|x|^{-d} \quad \text { for all } x \in M \backslash K .$$
\end{itemize}

Proof. Let $B_{r}$ be a large coordinate ball in $M$ that contains $K$. It suffices to prove the theorem on $M \backslash B_{r}$. Note that any point $x \in M \backslash B_{r}$ could be reached by a geodesic emanating from $\partial B_{r}$ with the initial velocity $\partial_{r}$. Let $\gamma(t), 0 \leq t<\infty$, be the geodesic emanating from a point $p \in \partial B_{r}$ with $\gamma^{\prime}(0)=\partial_{r}$, parametrized by the arc length parameter $t$, i.e.
$$t=d_{g}(p, \gamma(t)) .$$
With respect to the hyperbolic metric $b$ on $M \backslash B_{r}$ (pull back by the diffeomorphism that gives the chart at infinity) and letting $o$ be the origin of $\mathbb{H}^{n}$, we have $d_{b}(o, \gamma(t))=\sinh ^{-1}(|\gamma(t)|)$ and hence $\left|d_{b}(p, \gamma(t))-\sinh ^{-1}(|\gamma(t)|)\right| \leq d_{b}(o, p)$ by the triangle inequality, where $|\gamma(t)|$ denotes the radial coordinate of the point $\gamma(t)$. Since the distance in $g$ is comparable to the distance in $b$ by the asymptotically hyperbolic assumption, there is a constant $C>0$ such that $\left|t-\sinh ^{-1}(|\gamma(t)|)\right| \leq C$ for all $t$. Thus, there is a constant $C>0$ such that
$$C^{-1} e^{t} \leq|\gamma(t)| \leq C e^{t} .$$

By (3.12) and the assumption on $\tau$, we have
$$\begin{aligned}
\nabla^{2} V & =\left(\operatorname{Ric}_{g}-\frac{1}{n-1} R_{g} g\right) V+\tau-\left(\frac{1}{n-1} \operatorname{tr} \tau\right) g \\
& =\left(g+O^{0, \alpha}\left(r^{-q}\right)\right) V+O\left(r^{1-q}\right) .
\end{aligned}$$
Let $u(t)=V \circ \gamma(t)$. The equation (3.14) implies that $u$ satisfies the following ODE:
$$\begin{aligned}
u^{\prime \prime} & =\nabla^{2} V\left(\gamma^{\prime}(t), \gamma^{\prime}(t)\right)+\nabla V\left(\nabla_{\gamma^{\prime}(t)} \gamma^{\prime}(t)\right) \\
& =\nabla^{2} V\left(\gamma^{\prime}(t), \gamma^{\prime}(t)\right) \\
& =(1+Q(t)) u+f,
\end{aligned}$$
where $|Q(t)| \leq C e^{-q t}$ and $|f(t)| \leq C e^{(1-q) t}$ by (3.14) and (3.13). By Lemma 3.4, there is a constant $C>0$ and $d \in(0,1]$ such that $V$ satisfies
\begin{itemize}
\item[(1)] either $C^{-1} e^{t} \leq|V(\gamma(t))| \leq C e^{t}$ for all $t$
\item[(2)] or $|V(\gamma(t))| \leq C e^{-d t}$ for all $t$.
\end{itemize}

If (1) holds for some geodesic $\gamma$, by continuous dependence of ODE solutions on the initial conditions, the estimate $C^{-1}|x| \leq|V(x)| \leq C|x|$ holds in a cone, where we use (3.13) to replace $e^{t}$ with $|\gamma(t)|$ and enlarge the constant $C$ if needed. If (1) does not hold for any geodesic $\gamma$, then (2) holds for all $\gamma(t)$, with a uniform constant $C$ by compactness of $\partial B_{r}$. Using (3.13) and enlarging $C$ if necessary, we have $|V(x)| \leq C|x|^{-d}$ for all $x \in M \backslash K$. \(\square\)

Corollary 3.6. Let $(M, g)$ be an asymptotically hyperbolic manifold, and $V \in C_{\text {loc }}^{2}$ solve $L_{g}^{*} V=0$ in $M$. If $V$ is not identically zero, then there is a cone $U \subset M \backslash K$ and a constant $C>0$ such that $V$ satisfies
$$C^{-1}|x| \leq|V(x)| \leq C|x| \quad \text { for all } x \in U .$$

Proof. Recall $\Delta V=n V$ in (3.4). By letting $\tau=0$ in Theorem 3.5, we have that either the desired estimate holds, or there are constants $d, C>0$ such that $|V(x)| \leq C|x|^{-d}$ for all $x \in M \backslash K$. However, the latter case implies that $V$ is identically zero by maximum principle. \(\square\)

We now prove the main result in this section.

Proof of Theorem 4. It suffices to show that the linearized scalar curvature map is surjective. Local surjectivity of the scalar curvature map follows from standard functional analysis.

We first show that the range of $L_{g}$ is closed. Define the operator $T(u):=L_{g}(u g)$ for functions $u \in C_{-s}^{k, \alpha}(M)$. Then $\frac{1}{1-n} T(u)=\Delta u+\frac{1}{n-1} R_{g} u$ is asymptotic to $\Delta-n$ and hence Fredholm by Proposition 2.13. In particular, the range of $T$ has finite codimension, and so does the range of $L_{g}$. It implies that the range of $L_{g}$ is closed.

To see surjectivity of $L_{g}$, we show that the adjoint operator $L_{g}^{*}:\left(C_{-s}^{k-2, \alpha}\right)^{*} \rightarrow\left(C_{-s}^{k, \alpha}\right)^{*}$ has a trivial kernel. Let $u \in\left(C_{-s}^{k-2, \alpha}\right)^{*}$ weakly solve $L_{g}^{*} u=0$. Note that since $C_{c}^{\infty}$ is dense in $C_{-s}^{k-2, \alpha}, u$ is, in particular, a distribution. Taking the trace of $L_{g}^{*} u=0$ implies that $u$ weakly solves an elliptic PDE, whose coefficients are locally smooth by the hypothesis $g \in C_{\text {loc }}^{\infty}$. Applying elliptic regularity for distribution solutions (see, e.g. [10, Theorem 6.33]), we have $u \in C_{\text {loc }}^{k, \alpha}$ with the duality given by
$$u(\phi)=\int_{M} u \phi d \mu_{g}, \quad \text { for all } \phi \in C_{c}^{\infty}$$

Suppose, to give a contradiction, that $u$ is not identically zero. We shall show that the above pairing is not bounded for some $\phi \in C_{-s}^{k-2, \alpha}$. By Corollary 3.6, there is a constant $C>0$ such that $|u(x)| \geq C|x|$ in a nonempty cone $U \subset M \backslash K$. We may without loss of generality assume $u>0$ and hence $u(x) \geq C|x|$ on $U$. Let $\phi(x)$ be a non-negative function in $C_{-s}^{k-2, \alpha}$ so that $\phi(x)=|x|^{-s}$ in a smaller cone $U^{\prime} \subset U \subset M \backslash K$ and $\phi \equiv 0$ outside $U$. Let $\phi_{i} \in C_{c}^{\infty}(U)$ be a monotone sequence of non-negative functions that converge to $\phi$ in $C_{-s}^{k-2, \alpha}$ (for example, let $\phi_{i}=\chi_{i} \phi$ where $\chi_{i}$ is a monotone sequence of bump functions uniformly bounded in $C^{\infty}$ ). Then
$$u(\phi)=\lim _{i \rightarrow \infty} u\left(\phi_{i}\right)=\lim _{i \rightarrow \infty} \int_{M} u \phi_{i} d \mu_{g}=\int_{M} u \phi d \mu_{g},$$
where the first equality is from continuity of $u$ as a functional, the second equality is by (3.15), and the last equality is by monotone convergence theorem. However, since $s \leq n$ and $d \mu_{g}=$ $\left(\frac{r^{n-1}}{\sqrt{1+r^{2}}}+O\left(r^{n-2-q}\right)\right) d r d \omega$, the last integral diverges to infinity:
$$\int_{M} \phi u d \mu_{g} \geq C \int_{U^{\prime}} r^{1-s} d \mu_{g}=\infty .$$ \(\square\)

\section*{4. Mass minimizer and static uniqueness}

Let $(M, g)$ be an $n$-dimensional asymptotically hyperbolic manifold. Consider the following Banach (affine) space of symmetric (0, 2)-tensors:
$$\begin{gathered}
\mathcal{B}=\left\{g+h: h \in C_{-q}^{2, \alpha}(M) \text { is a symmetric }(0,2) \text {-tensor }\right\} \\
\mathcal{M} \subset \mathcal{B} \text { is an open neighborhood of } g \text { containing positive definite tensors. }
\end{gathered}$$

Suppose $f \in C_{\text {loc }}^{2, \alpha}(M)$ satisfies the following asymptotics, for some $a_{0}, a_{1}, \ldots, a_{n} \in \mathbb{R}$,
$$f(x)=a_{0} \sqrt{1+r^{2}}-\left(a_{1} x_{1}+\cdots+a_{n} x_{n}\right)+O^{2, \alpha}\left(|x|^{1-q}\right) .$$

By direct computation,
$$\begin{aligned}
\nabla^{2} \sqrt{1+r^{2}} & =\sqrt{1+r^{2}} g+O^{0, \alpha}\left(r^{1-q}\right) \\
\nabla^{2} x_{i} & =x_{i} g+O^{0, \alpha}\left(r^{1-q}\right) \quad \text { for } i=1, \ldots, n .
\end{aligned}$$
Therefore, we have
$$L_{g}^{*} f=-(\Delta f) g+\nabla^{2} f-f \operatorname{Ric}_{g}=O^{0, \alpha}\left(r^{1-q}\right) .$$
We define the corresponding functional $\mathcal{F}$ on $\mathcal{M}$ by
$$\mathcal{F}(\gamma)=a_{0} p_{0}(\gamma)-\left(a_{1} p_{1}(\gamma)+\cdots+a_{n} p_{n}(\gamma)\right)-\int_{M}(R(\gamma)+n(n-1)) f d \mu_{g}$$
where $R: \mathcal{M} \rightarrow C_{-q}^{0, \alpha}$ is the scalar curvature map and recall $\left(p_{0}(\gamma), \ldots, p_{n}(\gamma)\right)$ denotes the mass of $\gamma$.

It may not be immediately obvious that $\mathcal{F}(\gamma)$ is finite for $\gamma \in \mathcal{M}$. Since $\gamma$ is not assumed to satisfy the scalar curvature assumption (3) of Definition 2.3, either term in the definition of $\mathcal{F}$ may diverge. In the next lemma, we give an alternative expression for $\mathcal{F}$ and show that $\mathcal{F}$ is well-defined. We also compute its first variation.

Lemma 4.1. Let $f \in C_{\text {loc }}^{2, \alpha}(M)$ satisfy the asymptotics
$$f(x)=a_{0} \sqrt{1+r^{2}}-\left(a_{1} x_{1}+\cdots+a_{n} x_{n}\right)+O^{2, \alpha}\left(|x|^{1-q}\right) .$$
Then the corresponding functional $\mathcal{F}: \mathcal{M} \rightarrow \mathbb{R}$ can be expressed as
$$\mathcal{F}(\gamma)=\int_{M}\left(\left[L_{g}(\gamma-\mathfrak{b})-(R(\gamma)+n(n-1))\right] f-(\gamma-\mathfrak{b}) \cdot L_{g}^{*} f\right) d \mu_{g}$$
where $\mathfrak{b}$ is any fixed smooth symmetric (0, 2)-tensor in $M$ that coincides with the hyperbolic metric $b$ in the chart at infinity.

As a consequence, the linearization $\left.D \mathcal{F}\right|_{g}: C_{-q}^{2, \alpha} \rightarrow \mathbb{R}$ at $g$ is given by
$$\left.D \mathcal{F}\right|_{g}(h)=-\int_{M} h \cdot L_{g}^{*} f d \mu_{g} .$$
Proof. We recall the formulas for $L_{g}$ and $L_{g}^{*}$ in (3.1) and (3.2) for the following computations.
Let $e=\gamma-\mathfrak{b}$. By Definition 2.7 and Remark 2.8, we have
$$\begin{aligned}
\mathcal{F}(\gamma) & =\lim _{r \rightarrow \infty} \int_{S_{r}}(f(\operatorname{div} e-d(\operatorname{tr} e))(\nu)+(\operatorname{tr} e) d f(\nu)-e(\nabla f, \nu)) d \sigma_{g}-\int_{M}(R(\gamma)+n(n-1)) f d \mu_{g} \\
& =\int_{M} \operatorname{div}[f(\operatorname{div} e-d(\operatorname{tr} e))+(\operatorname{tr} e) d f-e(\nabla f, \cdot)] d \mu_{g}-\int_{M}(R(\gamma)+n(n-1)) f d \mu_{g} \\
& =\int_{M}[\operatorname{div} \operatorname{div} e-\Delta(\operatorname{tr} e)-R(\gamma)-n(n-1)] f d \mu_{g}-\int_{M}\left(-(\Delta f) g+\nabla^{2} f\right) \cdot e d \mu_{g} \\
& =\int_{M}\left[L_{g}(e)-(R(\gamma)+n(n-1))\right] f d \mu_{g}-\int_{M}\left(-(\Delta f) g+\nabla^{2} f-f \operatorname{Ric}_{g}\right) \cdot e d \mu_{g} .
\end{aligned}$$
Note (4.4) and $R(\gamma)+n(n-1)=L_{g}(e)+O\left(r^{-2 q}\right)$ by Taylor expansion. Both integrals converge by routine computations. \(\square\)

So far, we have considered the functional $\mathcal{F}$ defined by an arbitrary function $f$ satisfying the asymptotics (4.2). In what follows, we will choose specifically $f$ which is an eigenfunction $\Delta f=n f$.

Lemma 4.2 ([19, Lemma 3.3]). Let $(M, g)$ be an asymptotically hyperbolic manifold. There are functions $f_{0}, f_{1}, \ldots, f_{n} \in C_{\text {loc }}^{2, \alpha}(M)$ satisfying $\Delta f_{0}=n f_{0}$ and $\Delta f_{i}=n f_{i}$ for $i=1, \ldots, n$ with the asymptotics
$$\begin{aligned}
& f_{0}(x)=\sqrt{1+r^{2}}+O^{2, \alpha}\left(r^{1-q}\right) \\
& f_{i}(x)=x_{i}+O^{2, \alpha}\left(r^{1-q}\right) .
\end{aligned}$$
Proof. Taking the trace of equations in (4.3) yields
$$\begin{aligned}
\Delta \sqrt{1+r^{2}} & =n \sqrt{1+r^{2}}+O^{0, \alpha}\left(r^{1-q}\right) \\
\Delta x_{i} & =n x_{i}+O^{0, \alpha}\left(r^{1-q}\right) .
\end{aligned}$$
Note that the operator $\Delta-n: C_{1-q}^{2, \alpha} \rightarrow C_{1-q}^{0, \alpha}$ is an isomorphism by Lemma 2.12. There is a unique $v \in C_{1-q}^{2, \alpha}$ that solves $\Delta v-n v=-\Delta \sqrt{1+r^{2}}+n \sqrt{1+r^{2}}$. We set $f_{0}=\sqrt{1+r^{2}}+v$. Other eigenfunctions $f_{i}$ are obtained similarly. \(\square\)

Theorem 4.3. Let $(M, g)$ be an asymptotically hyperbolic manifold with scalar curvature $R_{g} \geq$ $-n(n-1)$ and with the equality $p_{0}=\sqrt{p_{1}^{2}+\cdots+p_{n}^{2}}$, where $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$ is the mass of $g$. Suppose the following holds:
\begin{itemize}
\item[] (★) There is an open neighborhood $\mathcal{M}$ of $g$ in $\mathcal{B}$ such that for any $\gamma \in \mathcal{M}$ with $R(\gamma)=R_{g}$, the inequality $p_{0}(\gamma) \geq \sqrt{\left(p_{1}(\gamma)\right)^{2}+\cdots+\left(p_{n}(\gamma)\right)^{2}}$ holds.
\end{itemize}
Then $(M, g)$ is static with a static potential $f>0$ satisfying the asymptotics:
$$f=\left\{\begin{array}{ll}
p_{0} \sqrt{1+r^{2}}-\left(p_{1} x_{1}+\cdots+p_{n} x_{n}\right)+O^{2, \alpha}\left(r^{1-q}\right) & \text { if } p_{0}>0 \\
\sqrt{1+r^{2}}+O^{2, \alpha}\left(r^{1-q}\right) & \text { if } p_{0}=0
\end{array} .\right.$$
Proof. Case 1: $p_{0}>0$. Let $f_{0}, f_{1}, \ldots, f_{n}$ be from Lemma 4.2. Define
$$f=p_{0} f_{0}-\left(p_{1} f_{1}+\cdots+p_{n} f_{n}\right),$$
where $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$ is the mass of $g$. Note $\Delta f=n f$. Since $f>0$ outside a large compact set, it follows from the maximum principle that $f$ is everywhere positive. We claim that $f$ is a static potential on $M$.

Consider the functional $\mathcal{F}: \mathcal{M} \rightarrow \mathbb{R}$ defined by (4.5) corresponding to this particular choice of $f$ with the coefficients $a_{k}=p_{k}$ for all $k=0,1, \ldots, n$. Let $R: \mathcal{M} \rightarrow C_{-q}^{0, \alpha}$ be the scalar curvature map that sends $\gamma$ to the scalar curvature of $\gamma$. Define $\mathcal{C}_{g}=\left\{\gamma \in \mathcal{M}: R(\gamma)=R_{g}\right\}$. By hypothesis (★), for $\gamma \in \mathcal{C}_{g}$, we have
$$p_{0}(\gamma) \geq \sqrt{\left(p_{1}(\gamma)\right)^{2}+\cdots+\left(p_{n}(\gamma)\right)^{2}} .$$
We compute that the functional $\mathcal{F}$ achieves a local minimum at $g$ among the constraint set $\mathcal{C}_{g}$ :
$$\begin{aligned}
\mathcal{F}(\gamma)-\mathcal{F}(g) & =p_{0} p_{0}(\gamma)-\left(p_{1} p_{1}(\gamma)+\cdots+p_{n} p_{n}(\gamma)\right) \\
& \geq p_{0} p_{0}(\gamma)-\sqrt{p_{1}^{2}+\cdots+p_{n}^{2}} \sqrt{\left(p_{1}(\gamma)\right)^{2}+\cdots+\left(p_{n}(\gamma)\right)^{2}} \\
& =p_{0}\left(p_{0}(\gamma)-\sqrt{\left(p_{1}(\gamma)\right)^{2}+\cdots+\left(p_{n}(\gamma)\right)^{2}}\right) \\
& \geq 0
\end{aligned}$$
with equalities realized at $\gamma=g$.
By Theorem 4, $L_{g}: C_{-q}^{2, \alpha} \rightarrow C_{-q}^{0, \alpha}$ is surjective, so we can apply the method of Lagrange Multipliers (see, for example, [14, Theorem C.1]) to obtain $\lambda \in\left(C_{-q}^{0, \alpha}\right)^{*}$ that satisfies
$$\left.D \mathcal{F}\right|_{g}(h)=\lambda\left(L_{g}(h)\right) \quad \text { for all } h \in C_{-q}^{2, \alpha} .$$
We substitute the left-hand side above by the first variation formula in Lemma 4.1 and get
$$-\int_{M} h \cdot L_{g}^{*}(f) d \mu_{g}=\lambda\left(L_{g}(h)\right) \quad \text { for all } h \in C_{-q}^{2, \alpha} .$$
Considering $h \in C_{c}^{\infty}$ in the above identity implies that $\lambda$, as a distribution, is a weak solution to $-L_{g}^{*} f=L_{g}^{*} \lambda$. Taking the trace of the previous equation implies that $\lambda$ weakly solves an elliptic PDE with locally smooth coefficients, by the hypothesis $g \in C_{\text {loc }}^{\infty}$. By elliptic interior regularity for distribution solutions (see, for example, [10, Theorem 6.33]), $\lambda \in C_{\text {loc }}^{2, \alpha}(M)$ with the duality given by
$$\lambda\left(L_{g}(h)\right)=\int_{M} \lambda L_{g}(h) d \mu_{g} \quad \text { for } h \in C_{c}^{\infty}(M)$$
Together with (4.8), $\lambda$ solves $L_{g}^{*} \lambda=-L_{g}^{*} f$ in the classical sense.
We recall $L_{g}^{*} f \in C_{1-q}^{0, \alpha}$. Applying Theorem 3.5 yields that there are numbers $d, C>0$ such that either $|\lambda(x)| \geq C|x|$ in a nonempty cone $U \subset M \backslash K$, or $|\lambda(x)| \leq C|x|^{-d}$ in $M \backslash K$. Since $\lambda$ is a bounded functional on $C_{-q}^{0, \alpha}$, the first case does not occur, by the same argument as in the last paragraph in the proof of Theorem 4. Therefore, we must have $|\lambda(x)| \leq C|x|^{-d}$ in $M \backslash K$; in particular, $\lambda(x) \rightarrow 0$ as $|x| \rightarrow \infty$. Taking the trace of $L_{g}^{*} \lambda=-L_{g}^{*} f$ gives that
$$\Delta \lambda-n \lambda=-(\Delta f-n f)=0 .$$
We conclude $\lambda$ is identically zero by the maximum principle. We conclude that $f$ is a static potential.
Case 2: $p_{0}=0$. We let $f=f_{0}$ where $f_{0}$ is from Lemma 4.2. That is, $f=\sqrt{1+r^{2}}+O^{2, \alpha}\left(r^{1-q}\right)$ and $\Delta f=n f$. Note $f>0$ by maximum principle. We will show that $f$ satisfies the static equation. Let $\mathcal{F}: \mathcal{M} \rightarrow \mathbb{R}$ be the functional defined by (4.5) corresponding to this particular choice of $f$ with $a_{0}=1$ and $a_{1}=\cdots=a_{n}=0$. Specifically,
$$\mathcal{F}(\gamma)=p_{0}(\gamma)-\int_{M}(R(\gamma)+n(n-1)) f d \mu_{g} .$$
Recall $\mathcal{C}_{g}$ defined above. Among the constraint $\gamma \in \mathcal{C}_{g}$, we have $\mathcal{F}(\gamma)-\mathcal{F}(g)=p_{0}(\gamma)-p_{0}(g) \geq 0$ by hypothesis (★) and thus $\mathcal{F}$ attains the minimum at $\gamma=g$. Now, we can apply the method of the Lagrange multipliers and argue that $f$ is a static potential as above. \(\square\)

We have shown that a metric $g$ that locally minimizes the functional $\mathcal{F}$ possesses a static potential with specific asymptotics. To conclude the proof of Theorem 2, we establish static uniqueness and show isometry to hyperbolic space. (In particular, the case $p_{0}>0$ in (4.7) cannot happen.)

Lemma 4.4. Let $(M, g)$ be an asymptotically hyperbolic manifold that admits a positive static potential $f$ with the asymptotics (4.7). Then on any large coordinate ball $B_{r}$, the following identity
holds
$$\int_{B_{r}} f^{-1}\left|\nabla^{2} f-f g\right|^{2} d \mu_{g}=\int_{\partial B_{r}}\left(\operatorname{Ric}_{g}+(n-1) g\right)(\nabla f, \nu) d \sigma_{g}$$
where $|\cdot|$ is the norm taken with respect to $g$ and $\nu$ is the outward unit normal vector on $\partial B_{r}$.
Proof. The following identity is due to X. Wang [24]. Set $S=\operatorname{Ric}_{g}+(n-1) g$. By the static equation, $S=f^{-1} \nabla^{2} f-g$ and $S$ is both trace and divergence free. We compute
$$\begin{aligned}
f^{-1}\left|\nabla^{2} f-f g\right|^{2} & =f|S|^{2} \\
& =f g\left(f^{-1} \nabla^{2} f, S\right) \quad(S \text { is trace-free }) \\
& =g\left(\nabla^{2} f, S\right) \\
& =\operatorname{div}(S(\nabla f)) \quad(S \text { is divergence-free }) .
\end{aligned}$$
The lemma follows by integrating the identity on $B_{r}$ and applying the divergence theorem. \(\square\)

We are ready to prove Theorem 2. We restate the assumption (★) using the precise Banach spaces defined earlier in (4.1).

Theorem 2. Let $n \geq 3$ and $(M, g)$ be an $n$-dimensional asymptotically hyperbolic manifold with scalar curvature $R_{g} \geq-n(n-1)$ and with the equality $p_{0}=\sqrt{p_{1}^{2}+\cdots+p_{n}^{2}}$, where $\left(p_{0}, p_{1}, \ldots, p_{n}\right)$ is the mass of $g$. Suppose the following holds:
\begin{itemize}
\item[] $(\star)$ There is an open neighborhood $\mathcal{M}$ of $g$ in $\mathcal{B}$ such that any $\gamma \in \mathcal{M}$ with $R(\gamma)=R_{g}$, the inequality $p_{0}(\gamma) \geq \sqrt{\left(p_{1}(\gamma)\right)^{2}+\cdots+\left(p_{n}(\gamma)\right)^{2}}$ holds.
\end{itemize}
Then $(M, g)$ is isometric to hyperbolic space.
Proof. By Theorem 4.3, $M$ admits a positive static potential $f$ of asymptotics (4.7). Using Lemma 4.4 and Proposition 2.10, in either the case $p_{0}>0$ or $p_{0}=0$, we have the following identity
$$\int_{M} f^{-1}\left|\nabla^{2} f-f g\right|^{2} d \mu_{g}=\lim _{r \rightarrow \infty} \int_{\partial B_{r}}\left(\operatorname{Ric}_{g}+(n-1) g\right)\left(\stackrel{\circ}{\nabla} f, \nu_{0}\right) d \sigma_{0}=-\frac{n-2}{2} H(f)=0 .$$
This implies $\nabla^{2} f=f g$, which characterizes hyperbolic space by an elementary argument, which we present in Proposition 4.5 below.

Alternatively, we could use again that $f$ satisfies the static equation by Theorem 4.3 to see that $g$ is Einstein with $\operatorname{Ric}_{g}=-(n-1) g$. Then $M$ is isometric to hyperbolic space by Bishop-Gromov volume comparison. \(\square\)

Proposition 4.5. Let $(M, g)$ be asymptotically hyperbolic. If there is a non-zero function $f \in$ $C_{\text {loc }}^{2}(M)$ satisfying $f>-c$ for some real number $c$ and the following equation on $M$ :
$$\nabla^{2} f=f g,$$
then $(M, g)$ is isometric to hyperbolic space.
Proof. If $f$ has at least one critical point, the result is classical (see [22] and also [15, Theorem C] and [20, Lemma 3.3]).

We now assume that $f$ has no critical point in $M$, i.e. $\nabla f$ is never zero. We compute the first and second covariant derivatives of $\nabla^{2} f=f g$ at a point $p \in M$ with respect to a geodesic normal coordinate chart:
$$\begin{aligned}
& 0=f_{; i j k}-f_{; i k j}-R_{k j \ell i} f^{\ell}=f_{k} g_{i j}-f_{j} g_{i k}-R_{k j \ell i} f^{\ell} \\
& 0=f\left(g_{k m} g_{i j}-g_{j m} g_{i k}\right)-R_{k j \ell i ; m} f^{\ell}-R_{k j m i} f,
\end{aligned}$$
where $R_{k j \ell i}=g\left(\nabla_{\partial_{k}} \nabla_{\partial_{j}} \partial_{\ell}-\nabla_{\partial_{j}} \nabla_{\partial_{k}} \partial_{\ell}, \partial_{i}\right)$ in our convention. We than obtain the following formulas, for any vector fields $W, X, Y, Z$,
$$\begin{aligned}
R(X, Y, \nabla f, Z) & =g(\nabla f, X) g(Y, Z)-g(\nabla f, Y) g(X, Z) \\
\left(\nabla_{Z} R\right)(X, Y, \nabla f, W) & =-f(R(X, Y, Z, W)-g(X, Z) g(Y, W)+g(Y, Z) g(X, W)) .
\end{aligned}$$

Let $\gamma:(-\infty, \infty) \rightarrow M$ be the integral curve of $\frac{\nabla f}{|\nabla f|}$ through a point $p \in M$, i.e. $\gamma^{\prime}(t)=\frac{\nabla f(\gamma(t))}{|\nabla f|(\gamma(t))}$. By direct computation using (4.9), we have $\nabla_{\gamma^{\prime}} \gamma^{\prime}=0$ and thus $\gamma$ is a geodesic parametrized by arc length. We compute
$$\begin{aligned}
\frac{d}{d t} f(\gamma(t)) & =g\left(\nabla f, \gamma^{\prime}(t)\right)=|\nabla f(\gamma(t))|>0 \\
\frac{d^{2}}{d t^{2}} f(\gamma(t)) & =\nabla^{2} f\left(\gamma^{\prime}(t), \gamma^{\prime}(t)\right)=f(\gamma(t)) .
\end{aligned}$$
Solving the ODE yields that, for $t \in(-\infty, \infty)$,
$$f(\gamma(t))=C_{1} e^{t}+C_{2} e^{-t},$$
where $C_{1} \geq 0 \geq C_{2}$ and $C_{1}, C_{2}$ are not both zero.
Let $X, Y$ be two orthonormal vector fields perpendicular to $\gamma^{\prime}$ and parallel along $\gamma$. The sectional curvature $K\left(X \wedge \gamma^{\prime}\right)=R\left(X, \gamma^{\prime}, \gamma^{\prime}, X\right)=-1$ along $\gamma$ by (4.10). Next, we compute that the sectional curvature $K(t):=K(X \wedge Y)=R(X, Y, Y, X)$ along $\gamma(t)$. In what follows, we slightly abuse the notation and denote $f(t)=f(\gamma(t))$ and $|\nabla f|(t)=|\nabla f|(\gamma(t))$. We compute, for all $t \in(-\infty, \infty)$,
$$\begin{aligned}
K^{\prime}(t) & =\gamma^{\prime}(R(X, Y, Y, X))=\left(\nabla_{\gamma^{\prime}} R\right)(X, Y, Y, X) \\
& =-\left(\nabla_{Y} R\right)\left(X, Y, X, \gamma^{\prime}\right)-\left(\nabla_{X} R\right)\left(X, Y, \gamma^{\prime}, Y\right) \quad \text { (by the second Bianchi identity) } \\
& =-2 \frac{f(t)}{|\nabla f|(t)}(K(t)+1)
\end{aligned}$$
where in the last equation we use the second equation in (4.10). We would like to show that $K(t)+1 \equiv 0$ for all $t$. Suppose, to give a contradiction, that $K(t)+1$ is not identically zero. Then $K(t)+1$ has no zeros, and we can divide the equation of $K^{\prime}(t)$ by $K(t)+1$ to achieve
$$\frac{d}{d t} \log |K(t)+1|=-2 \frac{f(t)}{|\nabla f|(t)} .$$
Note that $\frac{f(t)}{|\nabla f|(t)}$ satisfies the following ODE on $\gamma(t)$ by direct computation:
$$\frac{d}{d t}\left(\frac{f(t)}{|\nabla f|(t)}\right)=1-\left(\frac{f(t)}{|\nabla f|(t)}\right)^{2} \quad \text { for } t \in(-\infty, \infty) .$$
Solving this ODE yields that either (1) $\frac{|f|}{|\nabla f|} \equiv 1$ on $\gamma(t)$, or (2) there is a constant $C>0$ such that $\frac{f}{|\nabla f|}=1-\frac{2}{C e^{2 t}+1}$ on $\gamma(t)$. For Case (1), we find $K(t)+1$ to be either $B e^{-2 t}$ or $B e^{2 t}$ for some nonzero
constant $B$ for $t \in(-\infty, \infty)$ by (4.13), which contradicts the asymptotically hyperbolic assumption. For Case (2), $f(t)$ has a zero and hence $C_{2}<0$ in (4.12), which contradicts the assumption $f>-c$.

Varying $p \in M$, we conclude that the sectional curvature of $M$ is identically -1, which implies the universal cover of $M$ is hyperbolic space. Together with the asymptotically hyperbolic assumption, $M$ is isometric to hyperbolic space. \(\square\)

Remark 4.6. We thank Piotr Chruściel for pointing out an example that demonstrates the necessity of the hypothesis $f \geq-c$. Let $(\Sigma, h)$ be a complete $(n-1)$-dimensional manifold (either closed or unbounded) with bounded sectional curvature. Consider the product $M=(-\infty, \infty) \times \Sigma$ endowed with the warped product metric $g=d t^{2}+(\cosh t)^{2} h$. One can directly check that the sectional curvature of $(M, g)$ approaches -1 as $t \rightarrow \pm \infty$ and that $f(t)=\sinh t$ satisfies $\nabla^{2} f=f g$. (In particular, $\frac{f}{|\nabla f|}=1-\frac{2}{e^{2 t}+1}$ realizes Case (2) above.) If we further specify $\Sigma=\mathbb{R}^{n-1}$ endowed with a metric $h$ whose sectional curvature is identically -1 outside a compact set of $\Sigma$, the sectional curvature of the resulting metric $g$ approaches -1 toward the infinity of $M$. However, $(M, g)$ is of constant sectional curvature -1 if and only if $h$ is of constant sectional curvature -1 everywhere on $\Sigma$.

\section*{References}
\begin{itemize}
\item[1.] Lars Andersson, Mingliang Cai, and Gregory J. Galloway, Rigidity and positivity of mass for asymptotically hyperbolic manifolds, Ann. Henri Poincaré 9 (2008), no. 1, 1-33. MR 2389888
\item[2.] Lars Andersson and Mattias Dahl, Scalar curvature rigidity for asymptotically locally hyperbolic manifolds, Ann. Global Anal. Geom. 16 (1998), no. 1, 1-27. MR 1616570
\item[3.] Robert Bartnik, Phase space for the Einstein equations, Comm. Anal. Geom. 13 (2005), no. 5, 845-885. MR 2216143
\item[4.] Piotr T. Chruściel and Erwann Delay, Exotic hyperbolic gluings, J. Differential Geom. 108 (2018), no. 2, 243-293. MR 3763068
\item[5.] Piotr T. Chruściel and Erwann Delay, The hyperbolic positive energy theorem, arXiv:1901.05263 [math.DG] (2019).
\item[6.] Piotr T. Chruściel and Marc Herzlich, The mass of asymptotically hyperbolic Riemannian manifolds, Pacific J. Math. 212 (2003), no. 2, 231-264. MR 2038048
\item[7.] Erwann Delay, Analyse précisée d'équations semi-linéaires elliptiques sur l'espace hyperbolique et application à la courbure scalaire conforme, Bull. Soc. Math. France 125 (1997), no. 3, 345-381.
\item[8.] Erwann Delay and Jérémie Fougeirol, Hilbert manifold structure for asymptotically hyperbolic relativistic initial data, https://arxiv.org/abs/1607.05616 (2016).
\item[9.] Arthur E. Fischer and Jerrold E. Marsden, Deformations of the scalar curvature, Duke Math. J. 42 (1975), no. 3, 519-547. MR 0380907
\item[10.] Gerald B. Folland, Introduction to partial differential equations, second ed., Princeton University Press, Princeton, NJ, 1995. MR 1357411
\item[11.] C. Robin Graham and John M. Lee, Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991), no. 2, 186-225. MR 1112625
\item[12.] Marc Herzlich, Mass formulae for asymptotically hyperbolic manifolds, AdS/CFT correspondence: Einstein metrics and their conformal boundaries, IRMA Lect. Math. Theor. Phys., vol. 8, Eur. Math. Soc., Zürich, 2005, pp. 103-121. MR 2160869
\item[13.] \_\_\_\_, Computing asymptotic invariants with the Ricci tensor on asymptotically flat and asymptotically hyperbolic manifolds, Ann. Henri Poincaré 17 (2016), no. 12, 3605-3617. MR 3568027
\item[14.] Lan-Hsuan Huang and Dan A. Lee, Equality in the spacetime positive mass theorem, to appear in Comm. Math. Phys. (2019).
\end{itemize}
15. Masahiko Kanai, On a differential equation characterizing a Riemannian structure of a manifold, Tokyo J. Math. 6 (1983), no. 1, 143-151. MR 707845
16. John M. Lee, The spectrum of an asymptotically hyperbolic Einstein manifold, Comm. Anal. Geom. 3 (1995), no. 1-2, 253-271. MR 1362652
17. \_\_\_\_, Fredholm operators and Einstein metrics on conformally compact manifolds, Mem. Amer. Math. Soc. 183 (2006), no. 864, vi+83. MR 2252687
18. Maung Min-Oo, Scalar curvature rigidity of asymptotically hyperbolic spin manifolds, Math. Ann. 285 (1989), no. 4, 527-539. MR 1027758
19. Jie Qing, On the rigidity for conformally compact Einstein manifolds, Int. Math. Res. Not. (2003), no. 21, 1141-1153. MR 1962123
20. \_\_\_\_, On the uniqueness of AdS space-time in higher dimensions, Ann. Henri Poincaré 5 (2004), no. 2, 245-260. MR 2057674
21. Richard Schoen and Shing-Tung Yau, On the proof of the positive mass conjecture in general relativity, Comm. Math. Phys. 65 (1979), no. 1, 45-76. MR 526976 (80j:83024)
22. Yoshihiro Tashiro, Complete Riemannian manifolds and some vector fields, Trans. Amer. Math. Soc. 117 (1965), 251-275. MR 0174022
23. Xiaodong Wang, The mass of asymptotically hyperbolic manifolds, J. Differential Geom. 57 (2001), no. 2, 273-299. MR 1879228
24. \_\_\_\_, On the uniqueness of the $A d S$ spacetime, Acta Math. Sin. (Engl. Ser.) 21 (2005), no. 4, 917-922. MR 2156971
25. Edward Witten, A new proof of the positive energy theorem, Comm. Math. Phys. 80 (1981), no. 3, 381-402. MR 626707 (83e:83035)

Department of Mathematics, University of Connecticut, Storrs, CT 06269, USA
E-mail address: lan-hsuan.huang@uconn.edu, hyun.c.jang@uconn.edu
Department of Mathematics, Trinity College, Hartford, CT 06106, USA
E-mail address: daniel.martin@trincoll.edu
