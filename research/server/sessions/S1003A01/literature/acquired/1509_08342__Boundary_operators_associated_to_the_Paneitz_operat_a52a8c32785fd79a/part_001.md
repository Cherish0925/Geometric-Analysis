---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: [1509.08342] Boundary operators associated to the Paneitz operator]

---
source_file: 1509_08342.pdf
converter: mathpix
format: mmd
---

\title{
BOUNDARY OPERATORS ASSOCIATED TO THE PANEITZ OPERATOR
}

\author{
JEFFREY S. CASE
}

\begin{abstract}
We describe a set of conformally covariant boundary operators associated to the Paneitz operator, in the sense that they give rise to a conformally covariant energy functional for the Paneitz operator on a compact Riemannian manifold with boundary. These operators naturally give rise to a first- and third-order conformally covariant pseudodifferential operator. In the setting of Poincaré-Einstein manifolds, we show that these operators agree with the fractional GJMS operators of Graham and Zworski. We also use our operators to establish some new sharp Sobolev trace inequalities.
\end{abstract}

\section*{1. Introduction}

The Paneitz operator is a fourth-order conformally covariant differential operator which gives the simplest higher-order analogue of the conformal Laplacian. For example, the conformal Laplacian and the Paneitz operator arise in the norm computations for the critical Sobolev embeddings $W^{1,2}\left(\mathbb{R}^{n}\right) \hookrightarrow L^{\frac{2 n}{n-2}}\left(\mathbb{R}^{n}\right)$ and $W^{2,2}\left(\mathbb{R}^{n}\right) \hookrightarrow L^{\frac{2 n}{n-4}}\left(\mathbb{R}^{n}\right)$, respectively, and in the study of the scalar curvature and the (fourth-order) $Q$-curvature, respectively, within a conformal class.

To study conformally covariant operators on a manifold with boundary requires specifying conformally covariant boundary operators. Together, these operators are expected to control both critical Sobolev trace embeddings and certain scalar invariants. This is completely understood for the conformal Laplacian, and it is the purpose of this article to completely describe the analogous properties for the Paneitz operator.

Given a Riemannian manifold ( $X^{n+1}, g$ ) with boundary ( $M^{n}, h$ ) $=\left(\partial X,\left.g\right|_{T M}\right.$ ), the conformal Laplacian $L_{2}$, the trace $B_{0}^{1}$, and the conformal Robin operator $B_{1}^{1}$ are defined by
$$L_{2} u=-\Delta u+\frac{n-1}{2} J u, \quad B_{0}^{1} u=\left.u\right|_{M}, \quad B_{1}^{1} u=\eta u+\left.\frac{n-1}{2 n} H u\right|_{M}$$
for all $u \in C^{\infty}(X)$, where $J$ is the trace of the Schouten tensor $P=\frac{1}{n-1}$ (Ric $-J g$ ), $\eta$ is the outward-pointing normal, and $H=\operatorname{tr}_{h} \nabla \eta$ is the mean curvature of $M$. It follows that
$$\int_{X} u_{1} L_{2}\left(u_{2}\right)+\oint_{M} f_{1} B_{1}^{1}\left(u_{2}\right)=\int_{X}\left(\left\langle\nabla u_{1}, \nabla u_{2}\right\rangle+\frac{n-1}{2} J u_{1} u_{2}\right)+\frac{n-1}{2 n} \oint_{M} H f_{1} f_{2}$$

\footnotetext{
2000 Mathematics Subject Classification. Primary 58J32; Secondary 53A30, 58J40.
Key words and phrases. conformally covariant operator; boundary operator; fractional Laplacian; Sobolev trace inequality; Poincaré-Einstein manifold.
}
for all $u_{1}, u_{2} \in C^{\infty}(X)$, where $f_{j}=B_{0}^{1}\left(u_{j}\right)$ for $j \in\{1,2\}$. Denote this pairing by $\mathcal{Q}_{2}$. If $\widehat{g}=e^{2 \sigma} g$ is a conformal rescaling of $g$, then
$$\begin{aligned}
\widehat{L}_{2} u & =e^{-\frac{n+3}{2} \sigma} L_{2}\left(e^{\frac{n-1}{2} \sigma} u\right), \\
B_{k}^{1} u & =e^{-\frac{n+2 k-1}{2} \sigma} B_{k}^{1}\left(e^{\frac{n-1}{2} \sigma} u\right)
\end{aligned}$$
for all $u \in C^{\infty}(X)$ and all $k \in\{0,1\}$. It follows that $\mathcal{Q}_{2}$ is a conformally covariant symmetric bilinear form. Let $\mathcal{E}_{2}(u)=\mathcal{Q}_{2}(u, u)$ be the associated energy. Then the boundary Yamabe invariant
$$Y_{2}(X, M)=\inf \left\{\left.\mathcal{E}_{2}(u)\left|u \in C^{\infty}(X), \oint_{M}\right| B_{0}^{1}(u)\right|^{\frac{2 n}{n-1}}=1\right\}$$
is a conformal invariant.
A number of analytic and geometric consequences can be derived from $Y_{2}(X, M)$. Using conformal covariance and an Obata-type theorem, Escobar [18] computed $Y_{2}\left(\mathbb{R}_{+}^{n+1}, \mathbb{R}^{n}\right)$, thus giving a norm computation for the Sobolev trace embedding $W^{1,2}\left(\mathbb{R}_{+}^{n+1}\right) \hookrightarrow L^{\frac{2 n}{n-1}}\left(\mathbb{R}^{n}\right)$. Positive smooth critical points of $\mathcal{E}_{2}$ subject to the constraint defining $Y_{2}(X, M)$ give rise to metrics which are scalar flat in $X$ and make $M$ have constant mean curvature [18]. In fact, when $Y_{2}(X, M)$ is finite, it can be realized by a positive smooth function [3, 19, 31, 32].

Suppose that $X$ is compact and that the bottom of the Dirichlet spectrum of the conformal Laplacian,
$$\lambda_{1}\left(L_{2}\right)=\inf \left\{\mathcal{E}_{2}(u) \mid u \in C^{\infty}(X), B_{0}^{1} u=0, \int_{X} u^{2}=1\right\},$$
is positive; equivalently, suppose that $Y_{2}(X, M)$ is finite [20]. Then the energy $\mathcal{E}_{2}$ is uniquely minimized in the class of functions $u \in C^{\infty}(X)$ with fixed trace $f=B_{0}^{1} u$ by a function $u \in \operatorname{ker} L_{2}$. This gives a norm computation for the Sobolev trace embedding theorem: The map $\left.C^{\infty}(X) \ni u \mapsto u\right|_{M}$ extends to a surjective bounded linear mapping $W^{1,2}(X) \rightarrow H^{1 / 2}(M)$ (cf. [37]).

One can also use the pair $\left(L_{2}, B_{1}^{1}\right)$ to define a first order conformally covariant pseudodifferential operator as follows (cf. [6]): Suppose $\operatorname{ker} L_{2} \cap \operatorname{ker} B_{0}^{1}=\{0\}$. Then to each $f \in C^{\infty}(X)$, we define $\mathcal{B}_{1}^{1} f:=B_{1}^{1} u_{f}$ for $u_{f} \in C^{\infty}(X)$ the unique function such that $L_{2} u_{f}=0$ and $B_{0}^{1} u=f$. It follows from (1.1) that $\mathcal{B}_{1}^{1}$ is conformally covariant; indeed,
$$\widehat{\mathcal{B}}_{1}^{1} f=e^{-\frac{n+1}{2} \sigma} \mathcal{B}_{1}^{1}\left(e^{\frac{n-1}{2} \sigma} f\right) .$$
One can also define a first order conformally covariant pseudodifferential operator on $M$, namely the fractional GJMS operator $P_{1}$, via scattering theory [25]. These operators are the same [27]. In particular, $\mathcal{B}_{1}^{1}=(-\Delta)^{1 / 2}$ on Euclidean space [6, [12, 14].

Consider now the Paneitz operator $L_{4}: C^{\infty}(X) \rightarrow C^{\infty}(X)$ defined by
$$L_{4} u=\Delta^{2} u+\delta((4 P-(n-1) J g)(\nabla u))+\frac{n-3}{2} Q_{4} u$$
for all $u \in C^{\infty}(X)$, where $\delta=\operatorname{tr} \nabla$ is the negative of the formal adjoint of the Levi-Civita connection and
$$Q_{4}=-\Delta J-2|P|^{2}+\frac{n+1}{2} J^{2}$$
is the (fourth-order) $Q$-curvature. The Paneitz operator is conformally covariant [33]; indeed, if $\widehat{g}=e^{2 \sigma} g$, then
$$\widehat{L}_{4}(u)=e^{-\frac{n+5}{2} \sigma} L_{4}\left(e^{\frac{n-3}{2} \sigma} u\right) .$$
As a fourth-order operator, the Paneitz operator should have four associated boundary operators. Define operators $B_{k}^{3}: C^{\infty}(X) \rightarrow C^{\infty}(M)$ for $k \in\{0,1,2,3\}$ by
$$\begin{aligned}
B_{0}^{3} u= & u, \\
B_{1}^{3} u= & \eta u+\frac{n-3}{2 n} H u, \\
B_{2}^{3} u= & -\bar{\Delta} u+\nabla^{2} u(\eta, \eta)+\frac{n-2}{n} H \eta u+\frac{n-3}{2} T_{2}^{3} u, \\
B_{3}^{3} u= & -\eta \Delta u-2 \bar{\Delta} \eta u-\frac{n-3}{2 n} H \nabla^{2} u(\eta, \eta)+\frac{4}{n-1}\left\langle A_{0}, \bar{\nabla}^{2} u\right\rangle-\frac{3 n-5}{2 n} H \bar{\Delta} u \\
& -\frac{2(n-4)}{n}\langle\bar{\nabla} H, \bar{\nabla} u\rangle+S_{2}^{3} \eta u+\frac{n-3}{2} T_{3}^{3} u
\end{aligned}$$
for all $u \in C^{\infty}(X)$, where $A=\left.\nabla \eta\right|_{T M}$ is the second fundamental form, $A_{0}=A-\frac{H}{n} h$ is its tracefree part,
$$\begin{aligned}
S_{2}^{3}= & -\frac{3 n^{2}-7 n+6}{4 n^{2}} H^{2}+\frac{n-7}{2} P(\eta, \eta)+\frac{3 n-5}{2} \bar{J}+\frac{1}{2}\left|A_{0}\right|^{2}, \\
T_{2}^{3}= & \bar{J}-P(\eta, \eta)+\frac{n-2}{2 n^{2}} H^{2}, \\
T_{3}^{3}= & \eta J-\frac{2}{n} \bar{\Delta} H-\frac{4}{n-1}\left\langle A_{0}, \bar{P}\right\rangle+\frac{n-3}{2 n} H P(\eta, \eta) \\
& +\frac{3 n-1}{2 n} H \bar{J}+\frac{n+1}{2 n(n-1)} H\left|A_{0}\right|^{2}-\frac{n^{2}-n+2}{4 n^{3}} H^{3},
\end{aligned}$$
and barred operators are defined with respect to $\left(M^{n}, h\right)$. These are boundary operators associated to the Paneitz operator in the following sense:

Theorem 1.1. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$ and $n \geq 2$. Given $\sigma \in C^{\infty}(X)$, set $\widehat{g}=e^{2 \sigma} g$.
\begin{itemize}
\item[(1)] Given any $u \in C^{\infty}(X)$ and any $k \in\{0,1,2,3\}$, it holds that
$$\widehat{B}_{k}^{3}(u)=e^{-\left.\frac{n+2 k-3}{2} \sigma\right|_{M}} B_{k}^{3}\left(e^{\frac{n-3}{2} \sigma} u\right) .$$
\item[(2)] Define $\mathcal{Q}_{4}: C^{\infty}(X) \times C^{\infty}(X) \rightarrow \mathbb{R}$ by
$$\mathcal{Q}_{4}(u, v)=\int_{X} u L_{4} v+\oint_{M}\left(B_{0}^{3}(u) B_{3}^{3}(v)+B_{1}^{3}(u) B_{2}^{3}(v)\right)$$
for all $u, v \in C^{\infty}(X)$. Then $\mathcal{Q}_{4}$ is a symmetric bilinear form.
\end{itemize}

That $\mathcal{Q}_{4}$ is a symmetric bilinear form follows from the identity
$$\begin{aligned}
\mathcal{Q}_{4}(u, v)= & \int_{X}\left((\Delta u)(\Delta v)-(4 P-(n-1) J g)(\nabla u, \nabla v)+\frac{n-3}{2} Q_{4} u v\right) \\
& +\oint_{M}\left(2\left\langle\bar{\nabla} f_{1}, \bar{\nabla} \psi_{2}\right\rangle+2\left\langle\bar{\nabla} f_{2}, \bar{\nabla} \psi_{1}\right\rangle-\frac{2}{n} H \psi_{1} \psi_{2}\right. \\
& +\frac{n-3}{2} \widetilde{T}_{2}^{3}\left(f_{1} \psi_{2}+f_{2} \psi_{1}\right)-\left(\frac{4}{n-1} A_{0}-\frac{2}{n} H h\right)\left(\bar{\nabla} f_{1}, \bar{\nabla} f_{2}\right) \\
& \left.+\frac{n-3}{2}\left(\frac{2}{n} \bar{\Delta} H+T_{3}^{3}-\frac{n-3}{2 n} H \widetilde{T}_{2}^{3}\right) f_{1} f_{2}\right)
\end{aligned}$$
for all $u, v \in C^{\infty}(X)$, where $f_{1}=B_{0}^{3}(u), f_{2}=B_{0}^{3}(v), \psi_{1}=B_{1}^{3}(u), \psi_{2}=B_{1}^{3}(v)$, and
$$\widetilde{T}_{2}^{3}=T_{2}^{3}+\frac{2}{n^{2}} H^{2} .$$
Theorem 1.1 and the identity (1.3) together justify our description of the operators $B_{k}^{3}$ as the boundary operators associated to the Paneitz operator. However, this does not uniquely determine the boundary operators; see Remark 3.9.

Our main contribution in Theorem 1.1 is the formula (1.3). Motivated by questions involving the functional determinant, Chang and Qing [15] studied boundary operators for the Paneitz operator on four-manifolds with boundary when acting on functions whose normal derivative vanishes along the boundary, and identified the operator $B_{3}^{3}$ and the identity (1.3) in this setting (cf. Section 6). Branson and Gover [7] gave formulas for the boundary operators in the noncritical dimensions $n \geq 4$ (cf. [23]). Grant [26] extended the work of Branson and Gover to the critical dimension four for the Paneitz operator, and Juhl [28] verified the top order boundary operator in this case is $B_{3}^{3}$. Grant also identified a local formula for $B_{2}^{3}$. Stafford [36] (see also [28]) used the tractor expression of Branson and Gover to give the local formula for $B_{3}^{3}$ in higher dimensions. A refinement of the tractor approach has been developed by Gover and Peterson [24].

Theorem 1.1 and (1.2) implies that the energy $\mathcal{E}_{4}(u):=\mathcal{Q}_{4}(u, u)$ is a conformally covariant quadratic form. In particular,
$$\begin{aligned}
& Y_{4,1}(X, M)=\inf \left\{\left.\mathcal{E}_{4}(u)\left|u \in C^{\infty}(X), B_{1}^{3} u=0, \oint_{M}\right| B_{0}^{3} u\right|^{\frac{2 n}{n-3}}=1\right\}, \\
& Y_{4,2}(X, M)=\inf \left\{\left.\mathcal{E}_{4}(u)\left|u \in C^{\infty}(X), \oint_{M}\right| B_{0}^{3} u\right|^{\frac{2 n}{n-3}}=1\right\}
\end{aligned}$$
are conformal invariants when $n \geq 4$. Extremizing $Y_{4,1}(X, M)$ or $Y_{4,2}(X, M)$ provides one approach to constructing conformal metrics while prescribing the interior $Q$-curvature and certain combinations of the mean curvature and the curvatures $T_{2}^{3}$ and $T_{3}^{3}$ along the boundary.

Proposition 1.2. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=$ $\partial X$ and $n \geq 4$. Suppose that $u \in C^{\infty}(X)$ is a positive admissible function such that $\mathcal{E}_{4}(u)=Y_{4, k}(X, M)$ for $k \in\{1,2\}$. Then the metric $\widehat{g}=u^{\frac{4}{n-3}} g$ is such that $\widehat{Q}_{4}=0, \widehat{T}_{k}^{3}=0$, and $\widehat{T}_{3}^{3}=\frac{2}{n-3} Y_{4, k}(X, M)$.

Here $T_{1}^{3}=\frac{1}{n} H$ and $u$ is admissible if it is an admissible test function for the definition of $Y_{4, k}(X, M)$. Proposition 1.2 follows easily from Theorem 1.1, and in a
similar way one can obtain a variational characterization for some other conformal curvature prescription problems.

While we do not consider here the general problems of extremizing $Y_{4,1}(X, M)$ or $Y_{4,2}(X, M)$, we do compute its value on the round upper hemisphere, or equivalently, Euclidean upper half space. The first step in this direction is to relate the energy $\mathcal{E}_{4}(u)$ of a Paneitz-harmonic function to certain boundary energies. This can be done whenever the bottom of the Dirichlet spectrum of the Paneitz operator,
$$\lambda_{1}\left(L_{4}\right)=\inf \left\{\mathcal{E}_{4}(u) \mid u \in C^{\infty}(X), B_{0}^{3}(u)=0=B_{1}^{3}(u), \int_{X} u^{2}=1\right\},$$
is positive. Note that this is a conformally invariant condition. The desired relation comes from the following extension result.

Proposition 1.3. Let $\left(X^{n+1}, g\right)$ be a compact Riemannian manifold with boundary $M^{n}=\partial X$ and $n \geq 4$, and suppose that $\lambda_{1}\left(L_{4}\right)>0$. Then for each $f, \psi \in C^{\infty}(M)$, there exists a unique function $u_{f, \psi} \in C^{\infty}(X)$ such that
$$\left\{\begin{array}{l}
L_{4} u_{f, \psi}=0, \\
B_{0}^{3} u_{f, \psi}=f, \\
B_{1}^{3} u_{f, \psi}=\psi .
\end{array}\right.$$
Indeed, $u_{f, \psi}$ is characterized by the property
$$\mathcal{E}_{4}\left(u_{f, \psi}\right)=\inf \left\{\mathcal{E}_{4}(u) \mid u \in C^{\infty}(X), B_{0}^{3} u=f, B_{1}^{3} u=\psi\right\} .$$

A key point is that, by Theorem 1.1, the boundary value problem $\left(L_{4} ;\left(B_{0}^{3}, B_{1}^{3}\right)\right)$ defined by (1.4) is formally self-adjoint and satisfies the Lopatinskii-Shapiro conditions (cf. [2, 7]). Hence weak solutions of (1.4) are always smooth, while the spectral assumption guarantees that the infimum (1.5) is finite.

Suppose more generally that the $L^{2}$-kernel of the Paneitz operator on $\left(X^{n+1}, g\right)$ is trivial; i.e. $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}=\{0\}$. Given $f, \psi \in C^{\infty}(M)$, there are unique functions $u_{f, 0}, u_{0, \psi} \in C^{\infty}(X)$ such that (1.4) holds. Therefore the operators $\mathcal{B}_{1}^{3}, \mathcal{B}_{3}^{3}: C^{\infty}(M) \rightarrow C^{\infty}(M)$ defined by $\mathcal{B}_{1}^{3} \psi=\frac{1}{2} B_{2}^{3} u_{0, \psi}$ and $\mathcal{B}_{3} f=\frac{1}{2} B_{3}^{3} u_{f, 0}$ are well-defined. Indeed, $\mathcal{B}_{1}^{3}$ and $\mathcal{B}_{3}^{3}$ are formally self-adjoint conformally covariant first- and third-order pseudodifferential operators with principal symbol that of $(-\Delta)^{1 / 2}$ and $(-\Delta)^{3 / 2}$, respectively; see Section 4. On the other hand, if $g$ is conformal to a complete Einstein metric $g_{+}$with $\operatorname{Ric}\left(g_{+}\right)=-n g_{+}$in the interior of $X$ - briefly, if $\left(X^{n+1}, M^{n}, g_{+}\right)$is a Poincaré-Einstein manifold - then scattering theory defines first- and third-order pseudodifferential operators $P_{1}$ and $P_{3}$ with the same properties as $\mathcal{B}_{1}^{3}$ and $\mathcal{B}_{3}^{3}$, respectively [25]. These operators are the same:

Theorem 1.4. Let $\left(X^{n+1}, M^{n}, g_{+}\right)$be a Poincaré-Einstein manifold with $n \geq 2$ and $\frac{n^{2}-1}{4}, \frac{n^{2}-9}{4} \notin \sigma_{p p}\left(-\Delta_{g_{+}}\right)$. Let $\rho$ be a defining function for $M$ and set $g=\rho^{2} g_{+}$. Let $u \in C^{\infty}(X)$ be such that $L_{4} u=0$. Set $f=B_{0}^{3} u$ and $\psi=B_{1}^{3} u$. Then
$$\begin{aligned}
& B_{3}^{3} u=2 P_{3} f, \\
& B_{2}^{3} u=2 P_{1} \psi .
\end{aligned}$$
In particular, $\mathcal{B}_{3}^{3}=P_{3}$ and $\mathcal{B}_{1}^{3}=P_{1}$.
A surprising consequence of Theorem 1.4 is that, at least for Poincaré-Einstein manifolds, one can compute $P_{3} f$ without first finding the unique extension $u_{f, 0}$;
one need only find some Paneitz-harmonic function $u$ with $B_{0}^{3} u=f$ (cf. [13, 14]). This generalizes the observation that this property holds for hyperbolic space [1, 7].

Though both the pairs $\mathcal{B}_{1}^{3}, \mathcal{B}_{3}^{3}$ and $P_{1}, P_{3}$ are defined for all manifolds with boundary, it is only in the Poincaré-Einstein case that we can verify that they coincide. The proof of Theorem 1.4 relies on the observation that, when computed with respect to $g_{+}$, the Paneitz operator factors through the operators used in the Poisson equations defining $P_{1}$ and $P_{3}$ via scattering,
$$\left(L_{4}\right)_{g_{+}}=\left(-\Delta_{g_{+}}-\frac{n^{2}-1}{4}\right) \circ\left(-\Delta_{g_{+}}-\frac{n^{2}-9}{4}\right) .$$
If the Paneitz operator factors as in (1.6) for some metric $g$, then $g$ is Einstein [35].
Combining Proposition 1.3 and Theorem 1.4 yields the following relationship between the Paneitz energy of a function in $X$ and the energy of its trace:

Corollary 1.5. Let $\left(X^{n+1}, M^{n}, g_{+}\right)$be a Poincaré-Einstein manifold such that $\lambda_{1}\left(L_{4}\right)>0$ and $n \geq 2$. Let $\rho$ be a defining function for $M$, set $g=\rho^{2} g_{+}$, and fix $f, \psi \in C^{\infty}(M)$. Then
$$\frac{1}{2} \mathcal{E}_{4}(u) \geq \oint_{M} f P_{3} f+\oint_{M} \psi P_{1} \psi$$
for all $u \in C^{\infty}(X)$ with $B_{0}^{3} u=f$ and $B_{1}^{3} u=\psi$. Moreover, equality holds if and only if $u=u_{f, \psi}$ for $u_{f, \psi}$ as in (1.4).

Recall the Sobolev trace theorem: In Euclidean upper half space, the map $u \mapsto$ $\left(B_{0}^{3} u, B_{1}^{3} u\right)$ can be extended to a bounded linear mapping
$$\operatorname{Tr}: W^{2,2}\left(\mathbb{R}_{+}^{n+1}\right) \rightarrow H^{3 / 2}\left(\mathbb{R}^{n}\right) \oplus H^{1 / 2}\left(\mathbb{R}^{n}\right)$$
which admits a bounded right inverse (cf. [37]). Corollary 1.5 and Reilly's formula [34] together give a norm computation for this result (cf. Corollary 5.2).

Using the sharp fractional Sobolev inequalities [5, 30], we obtain from Corollary 1.5 a sharp Sobolev trace inequality which gives a norm computation for the embedding $W^{2,2}\left(\mathbb{R}_{+}^{n+1}\right) \hookrightarrow L^{\frac{2 n}{n-3}}\left(\mathbb{R}^{n}\right) \oplus L^{\frac{2 n}{n-1}}\left(\mathbb{R}^{n}\right)$. In particular, this result computes the constants $Y_{4,1}\left(\mathbb{R}_{+}^{n+1}, \mathbb{R}^{n}\right)$ and $Y_{4,2}\left(\mathbb{R}_{+}^{n+1}, \mathbb{R}^{n}\right)$ and also characterizes their extremal functions:

Theorem 1.6. Let $n \geq 4$ and let $\left(S_{+}^{n+1}, d \theta^{2}\right)$ be the upper hemisphere
$$S_{+}^{n+1}=\left\{x=\left.\left(x_{0}, \ldots, x_{n+1}\right) \in \mathbb{R}^{n+2}| | x\right|^{2}=1, x_{0} \geq 0\right\}$$
with the round metric $d \theta^{2}=\left.d x^{2}\right|_{T S_{+}^{n+1}}$ of constant sectional curvature one. Given any $u \in C^{\infty}\left(S_{+}^{n+1}\right)$, it holds that
$$\begin{aligned}
\int_{S_{+}^{n+1}}\left((\Delta u)^{2}\right. & \left.+\frac{n^{2}-5}{2}|\nabla u|^{2}+\frac{\left(n^{2}-1\right)\left(n^{2}-9\right)}{16} u^{2}\right) \\
& \geq 4 \oint_{S^{n}}\left(\psi \bar{\Delta} f-\frac{(n-1)(n-3)}{8} f \psi\right)+C_{3}\|f\|_{\frac{2 n}{n-3}}^{2}+C_{1}\|\psi\|_{\frac{2 n}{n-1}}^{2},
\end{aligned}$$
where $f=B_{0}^{3} u, \psi=B_{1}^{3} u$, and
$$C_{k}=2^{k+1} \pi^{\frac{k}{2}} \frac{\Gamma\left(\frac{n+k}{2}\right)}{\Gamma\left(\frac{n-k}{2}\right)}\left(\frac{\Gamma(n / 2)}{\Gamma(n)}\right)^{\frac{k}{n}}$$
for $k \in\{1,3\}$. Equality holds if and only if $L_{4} u=0, f(x)=a_{1}\left(1+\xi_{1} \cdot x\right)^{-\frac{n-3}{2}}$ and $\psi(x)=a_{2}\left(1+\xi_{2} \cdot x\right)^{-\frac{n-1}{2}}$ for constants $a_{1}, a_{2} \in \mathbb{R}$ and points $\xi_{1}, \xi_{2} \in B_{1}(0) \subset$ $\mathbb{R}^{n+1}$. In particular,
$$Y_{4,1}\left(\mathbb{R}_{+}^{n+1}, \mathbb{R}^{n}\right)=Y_{4,2}\left(\mathbb{R}_{+}^{n+1}, \mathbb{R}^{n}\right)=C_{3} .$$

More generally, if $g$ is any conformally flat metric on $S_{+}^{n+1}$, it holds that
$$\mathcal{E}_{4}(u) \geq C_{3}\left(\oint_{S^{n}}|f|^{\frac{2 n}{n-3}}\right)^{\frac{n-3}{n}}+C_{1}\left(\oint_{S^{n}}|\psi|^{\frac{2 n}{n-1}}\right)^{\frac{n-1}{n}}$$
for all $u \in C^{\infty}\left(S_{+}^{n+1}\right)$, where $f=B_{0}^{3} u$ and $\psi=B_{1}^{3} u$. Restricting (1.7) to functions $u \in C^{\infty}\left(S_{+}^{n+1}\right)$ with $B_{1}^{3} u=0$ recovers known sharp Sobolev trace inequalities: Combining results of Lieb [30] and R. Yang [38] gives a sharp Sobolev trace inequality on Euclidean upper half space; Ache and Chang [1] established analogous inequalities in the flat ball $B_{1}(0) \subset \mathbb{R}^{n+1}$ and in the upper hemisphere with both the round metric and the adapted metric [13].

The restriction $n \geq 4$ in Proposition 1.2 and Theorem 1.6 is somewhat artificial. There is a natural modification of the energy $\mathcal{E}_{4}$ defined on four-manifolds with boundary which incorporates the boundary operators $B_{k}^{3}$ for $k \in\{0,1,2,3\}$. This functional is related to log determinant formulae [10, 15] and gives rise to analogues of $Y_{4,1}$ and $Y_{4,2}$. In particular, it extends Proposition 1.2 and Theorem 1.6 to this setting; for details, see Section 6.

This article is organized as follows:
In Section 2 we recall some useful facts from conformal geometry and the study of manifolds with boundary.

In Section 3 we prove Theorem 1.1, derive the Euler equation for $\mathcal{E}_{4}$, and thereby establish Proposition 1.2.

In Section 4 we prove Proposition 1.3 and discuss the properties of the operators $\mathcal{B}_{1}^{3}$ and $\mathcal{B}_{3}^{3}$. In particular, we prove Theorem 1.4.

In Section 5 we describe the relationship to sharp Sobolev trace inequalities, and in particular prove Theorem 1.6.

In Section 6 we describe the particulars of the case of compact four-manifolds with boundary.

Acknowledgments. I would like to thank Antonio Ache and Alice Chang for many discussions related to their article [1], and also Rod Gover for bringing my attention to the theses [26, 36].

\section*{2. Manifolds with boundary}

Throughout this article, we exclusively study manifolds $\left(X^{n+1}, g\right)$ with boundary $\left(M^{n}, h\right)=\left(\partial X,\left.g\right|_{T M}\right)$. We always denote intrinsic geometric quantities on $\left(M^{n}, h\right)$ with bars; e.g. $\bar{P}=\frac{1}{n-2}(\overline{\text { Ric }}-\bar{J} h)$ is the Schouten tensor of $\left(M^{n}, h\right)$ and $\bar{J}=\operatorname{tr}_{h} \bar{P}$ is its trace. Integrals over $X$ with respect to the volume element induced by $g$ are denoted by $\int$; integrals over $M$ with respect to the volume element induced by $h$ are denoted by $\oint$. When the context is clear, we omit restriction symbols (e.g. Proposition 3.1).

When studying boundary operators for the Paneitz operator, we often need to relate the intrinsic and extrinsic geometry of the boundary $M$ of $X$. The first such
relationship comes from the Gauss-Codazzi equations, stated here in terms of the Schouten tensor. Since these equations are well-known, we omit their proof.
Lemma 2.1. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$ and let $\eta$ denote the outward-pointing normal along $M$. Then
$$\begin{aligned}
J & =\bar{J}+P(\eta, \eta)-\frac{1}{2 n} H^{2}+\frac{1}{2(n-1)}\left|A_{0}\right|^{2}, \\
P & =\bar{P}-\frac{1}{n} H A_{0}-\frac{1}{2 n^{2}} H^{2} h+\frac{1}{n-2}\left(W(\eta, \cdot, \eta, \cdot)+A_{0}^{2}-\frac{1}{2(n-1)}\left|A_{0}\right|^{2} h\right) .
\end{aligned}$$
Moreover, as sections of $T^{*} M$,
$$\bar{\delta} A=(n-1) P(\eta, \cdot)+d H .$$

The other relationships we need involve second- and third-order derivatives of functions $u \in C^{\infty}(X)$ when evaluated on $M$. The relationship between the Laplacians of $\left(X^{n+1}, g\right)$ and $\left(M^{n}, h\right)$ is well-known. Again, we omit the proof.
Lemma 2.2. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$ and let $\eta$ denote the outward-pointing normal along $M$. Given any $u \in C^{\infty}(X)$ it holds that
$$\Delta u=\bar{\Delta} u+\nabla^{2} u(\eta, \eta)+H \eta u .$$

Given $u, v \in C^{\infty}(X)$, the derivative $\eta\langle\nabla u, \nabla v\rangle$ is decomposed into horizontal and normal components via the following lemma.
Lemma 2.3. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$. Given any $u, v \in C^{\infty}(X)$ it holds that
$$\nabla^{2} u(\eta, \nabla v)=\langle\bar{\nabla} \eta u, \bar{\nabla} v\rangle+(\eta v) \nabla^{2} u(\eta, \eta)-A(\bar{\nabla} u, \bar{\nabla} v) .$$
Proof. We compute that
$$\begin{aligned}
\nabla^{2} u(\eta, \nabla v) & =\langle\nabla \eta u, \nabla v\rangle-\left\langle\nabla_{\nabla v} \eta, \nabla u\right\rangle \\
& =\langle\bar{\nabla} \eta u, \bar{\nabla} v\rangle+(\eta v)\left(\eta \eta u-\left(\nabla_{\eta} \eta\right) u\right)-\left\langle\nabla_{\bar{\nabla} v} \eta, \nabla u\right\rangle .
\end{aligned}$$ \(\square\)

Finally, we require the relationship between the normal derivative of the interior Laplacian $\eta \Delta u$ and the third-order normal derivative $\nabla^{3} u(\eta, \eta, \eta)$ for $u \in C^{\infty}(X)$.
Lemma 2.4. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$. Given any $f \in C^{\infty}(X)$, it holds that
$$\begin{aligned}
\eta \Delta f=\nabla^{3} f(\eta, \eta, \eta)+H \nabla^{2} f(\eta, \eta) & +\bar{\Delta} \eta f-2 \bar{\delta}(A(\bar{\nabla} f))+\langle\bar{\nabla} H, \bar{\nabla} f\rangle \\
& \quad-\left(\bar{J}+n P(\eta, \eta)+\frac{1}{2 n} H^{2}+\frac{2 n-1}{2(n-1)}\left|A_{0}\right|^{2}\right) \eta f .
\end{aligned}$$
Proof. Let $p \in M$ and let $\left\{e_{i}\right\}_{i=1}^{n}$ be an orthonormal basis for $T_{p} M$, extended to a neighborhood of $p$ in $X$ by parallel translation. It follows that, at $p$,
$$\begin{aligned}
\eta \Delta f & =\nabla^{3} f(\eta, \eta, \eta)-\operatorname{Ric}(\eta, \nabla f)+\sum_{i=1}^{n} \nabla^{3} f\left(e_{i}, e_{i}, \eta\right), \\
\bar{\delta} A & =-H \nabla_{\eta} \eta+\sum_{i=1}^{n} \bar{\nabla}_{e_{i}} \nabla_{e_{i}} \eta, \\
\left\langle A, \bar{\nabla}^{2} f\right\rangle & =\sum_{i=1}^{n}\left[e_{i}\left(\nabla_{e_{i}} \eta\right) f-\left(\bar{\nabla}_{e_{i}} \nabla_{e_{i}} \eta\right) f\right] .
\end{aligned}$$

We then compute that
$$\begin{aligned}
\sum_{i=1}^{n} \nabla^{3} f\left(e_{i}, e_{i}, \eta\right) & =\sum_{i=1}^{n}\left[e_{i} e_{i} \eta f-2 e_{i}\left(\nabla_{e_{i}} \eta\right)+\left(\nabla_{e_{i}} \nabla_{e_{i}} \eta\right) f\right] \\
& =\bar{\Delta} \eta f+H \nabla^{2} f(\eta, \eta)-2\left\langle A, \bar{\nabla}^{2} f\right\rangle-\langle\bar{\delta} A, \bar{\nabla} f\rangle-|A|^{2} \eta f
\end{aligned}$$
The result is now an immediate consequence of Lemma 2.3. \(\square\)

\section*{3. Boundary operators for the Paneitz operator}

The claim that the operators $B_{k}^{3}$ for $k \in\{0,1,2,3\}$ are boundary operators associated to the weighted Paneitz operator includes two statements. First, the boundary operators $B_{k}^{3}$ are conformally covariant and act on densities of the same weight as the Paneitz operator; i.e. the precomposition factor is the same as in (1.2). Second, the pairing
$$\mathcal{Q}_{4}(u, v)=\int_{X} u L_{4} v+\oint_{M}\left(B_{0}^{3}(u) B_{3}^{3}(v)+B_{1}^{3}(u) B_{2}^{3}(v)\right)$$
is symmetric; in particular, this ensures that the higher order terms in the Paneitz operator and the boundary operators $B_{2}^{3}$ and $B_{3}^{3}$ cancel after integration by parts. This claim is the content of Theorem 1.1

To prove the first statement of Theorem 1.1, we identify boundary operators of all integer orders between zero and three which are conformally covariant and act on densities of arbitrary weight (cf. [24]). After making an additional choice to ensure that $\mathcal{Q}_{4}$ is symmetric (cf. Remark 3.9), these operators recover the boundary operators $B_{k}^{3}$ in the case of densities of weight $-\frac{n-3}{2}$. Other choices of weight are relevant to the study of boundary operators associated to other GJMS operators.

The simplest cases are the zeroth- and first-order conformally covariant boundary operators.

Proposition 3.1. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=$ $\partial X$ and let $w \in \mathbb{R}$. Define $B_{0, w}, B_{1, w}: C^{\infty}(X) \rightarrow C^{\infty}(M)$ by
$$\begin{aligned}
B_{0, w} u & =u, \\
B_{1, w} u & =\eta u-\frac{w}{n} H u .
\end{aligned}$$
Given $\sigma \in C^{\infty}(X)$, set $\widehat{g}=e^{2 \sigma} g$. Then
$$\begin{aligned}
\widehat{B}_{0, w}(u) & =e^{w \sigma} B_{0, w}\left(e^{-w \sigma} u\right), \\
\widehat{B}_{1, w}(u) & =e^{(w-1) \sigma} B_{1, w}\left(e^{-w \sigma} u\right)
\end{aligned}$$
for all $u \in C^{\infty}(M)$.
Proof. It is clear that (3.1) holds. Observe that the outward-pointing normals $\eta$ and $\widehat{\eta}$ along $M$ defined with respect to $g$ and $\widehat{g}$, respectively, are related by $\widehat{\eta}=e^{-\sigma} \eta$. It follows that
$$\widehat{H}=e^{-\sigma}(H+n \eta \sigma),$$
from which the conclusion immediately follows. \(\square\)

In order to more easily identify the conformally covariant boundary operators of higher order, we use an observation of Branson [8]: Suppose that $D: C^{\infty}(X) \rightarrow$ $C^{\infty}(M)$ is a natural operator which is homogeneous of degree $k$; i.e. $D=D_{g}$ is defined by a formula which is a complete contraction of a tensor polynomial in the Levi-Civita connection, the Riemann curvature tensor, and the outward-pointing normal along $M$, and moreover, $D_{c^{2} g}=c^{-k} D_{g}$ for all constants $c>0$. Given a fixed constant $w \in \mathbb{R}$ and a fixed function $\sigma \in C^{\infty}(X)$, define the operator $D^{\prime}$ by
$$D^{\prime}(u):=\left.\frac{d}{d t}\right|_{t=0}\left[e^{-(w-k) t \sigma} D_{e^{2 t \sigma} g}\left(e^{w t \sigma} u\right)\right] .$$
We equivalently write $(D u)^{\prime}$ for $D^{\prime}(u)$. It is straightforward to check that $D^{\prime} \equiv 0$ if and only if
$$D_{e^{2 \sigma} g}(u)=e^{(w-k) \sigma} D_{g}\left(e^{-w \sigma} u\right)$$
for all $u \in C^{\infty}(X)$. Thus to prove that a natural homogeneous operator is conformally covariant, it suffices to show that its "linearization" $D^{\prime}$ is the zero operator for some weight $w$.

The boundary operator $B_{2}^{3}$ is a natural operator which is homogeneous of degree two. To check that it is conformally covariant, we compute the linearization of most (cf. Remark 3.9) natural operators which are homogeneous of degree two.
Lemma 3.2. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$. Given $w \in \mathbb{R}$ and $\sigma \in C^{\infty}(X)$, it holds that
$$\begin{aligned}
(\bar{\Delta} u)^{\prime} & =(n+2 w-2)\langle\bar{\nabla} u, \bar{\nabla} \sigma\rangle+w u \bar{\Delta} \sigma, \\
\left(\nabla^{2} u(\eta, \eta)\right)^{\prime} & =\langle\bar{\nabla} u, \bar{\nabla} \sigma\rangle+(2 w-1)(\eta u)(\eta \sigma)+w u \nabla^{2} \sigma(\eta, \eta), \\
(H \eta u)^{\prime} & =n(\eta u)(\eta \sigma)+w H u \eta \sigma, \\
\left(H^{2} u\right)^{\prime} & =2 n H u \eta \sigma, \\
(u P(\eta, \eta))^{\prime} & =-u \nabla^{2} \sigma(\eta, \eta), \\
(u \bar{J})^{\prime} & =-u \bar{\Delta} \sigma
\end{aligned}$$
for all $u \in C^{\infty}(X)$.
Proof. It is well-known that if $\widehat{g}=e^{2 \sigma} g$, then
$$\begin{aligned}
\widehat{P} & =P-\nabla^{2} \sigma+d \sigma \otimes d \sigma-\frac{1}{2}|\nabla \sigma|^{2} g, \\
\widehat{\nabla}^{2} u & =\nabla^{2} u-d \sigma \otimes d u-d u \otimes d \sigma+\langle\nabla \sigma, \nabla u\rangle g
\end{aligned}$$
Combining this, the analogous statements for the conformally rescaled boundary metric $\widehat{h}$, and (3.3) yields the result. \(\square\)

In particular, we obtain the following family of second-order conformally covariant boundary operators.
Proposition 3.3. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=$ $\partial X$ and let $w \in \mathbb{R}$. Define $B_{2, w}: C^{\infty}(X) \rightarrow C^{\infty}(M)$ by
$$\begin{aligned}
B_{2, w} u:=-\bar{\Delta} u & +(n+2 w-2) \nabla^{2} u(\eta, \eta)-\frac{(n+2 w-2)(2 w-1)}{n} H \eta u \\
& -w\left(\bar{J}-(n+2 w-2) P(\eta, \eta)-\frac{(n+2 w-2)(2 w-1)}{2 n^{2}} H^{2}\right) u .
\end{aligned}$$

Given $\sigma \in C^{\infty}(X)$, set $\widehat{g}=e^{2 \sigma} g$. Then
$$\widehat{B}_{2, w}(u)=e^{(w-2) \sigma} B_{2, w}\left(e^{-w \sigma} u\right)$$
for all $u \in C^{\infty}(X)$.
Proof. Lemma 3.2 implies that $B_{2, w}^{\prime}=0$. \(\square\)

The boundary operator $B_{3}^{3}$ is a natural operator which is homogeneous of degree three. To check that it is conformally covariant, we compute the linearization of most (cf. Remark 3.9) natural operators which are homogeneous of degree three. For the sake of readability, we separate this computation into four lemmas according to the order of the operator as a differential operator.
Lemma 3.4. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$. Given $w \in \mathbb{R}$ and $\sigma \in C^{\infty}(X)$, it holds that
$$\begin{aligned}
(\eta \Delta u)^{\prime}= & (w-2)(\eta \sigma) \bar{\Delta} u+(n+3 w-3)(\eta \sigma) \nabla^{2} u(\eta, \eta) \\
& +(n+2 w-1)\langle\bar{\nabla} \eta u, \bar{\nabla} \sigma\rangle+2(w-1) H(\eta u)(\eta \sigma) \\
& +(n+2 w-1)\langle\bar{\nabla} u, \bar{\nabla} \eta \sigma\rangle-2(n+2 w-1) A(\bar{\nabla} u, \bar{\nabla} \sigma\rangle \\
& +(n+3 w-1)(\eta u) \nabla^{2} \sigma(\eta, \eta)+w(\eta u) \bar{\Delta} \sigma+w u \eta \Delta \sigma, \\
(\bar{\Delta} \eta u)^{\prime}= & w(\eta \sigma) \bar{\Delta} u+(n+2 w-4)\langle\bar{\nabla} \eta u, \bar{\nabla} \sigma\rangle \\
& +2 w\langle\bar{\nabla} u, \bar{\nabla} \eta \sigma\rangle+(w-1)(\eta u) \bar{\Delta} \sigma+w u \bar{\Delta} \eta \sigma
\end{aligned}$$
for all $u \in C^{\infty}(X)$.
Proof. Lemma 3.2 yields the formula for $(\bar{\Delta} \eta)^{\prime}$ and also that
$$(\eta \Delta u)^{\prime}=\eta((n+2 w-1)\langle\nabla u, \nabla \sigma\rangle+w u \Delta \sigma)+(w-2)(\eta \sigma) \Delta u .$$
The result then follows from Lemma 2.2 and Lemma 2.3. \(\square\)

Lemma 3.5. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$. Given $w \in \mathbb{R}$ and $\sigma \in C^{\infty}(X)$, it holds that
$$\begin{aligned}
\left(\left\langle A_{0}, \bar{\nabla}^{2} u\right\rangle\right)^{\prime}= & 2(w-1) A_{0}(\bar{\nabla} u, \bar{\nabla} \sigma)+w u\left\langle A_{0}, \bar{\nabla}^{2} \sigma\right\rangle, \\
(H \bar{\Delta} u)^{\prime}= & n(\eta \sigma) \bar{\Delta} u+(n+2 w-2) H\langle\bar{\nabla} u, \bar{\nabla} \sigma\rangle+w H u \bar{\Delta} \sigma, \\
\left(H \nabla^{2} u(\eta, \eta)\right)^{\prime}= & n(\eta \sigma) \nabla^{2} u(\eta, \eta)+H\langle\bar{\nabla} u, \bar{\nabla} \sigma\rangle \\
& +(2 w-1) H(\eta u)(\eta \sigma)+w H u \nabla^{2} \sigma(\eta, \eta)
\end{aligned}$$
for all $u \in C^{\infty}(X)$.
Proof. Recall that $A_{0}$ is conformally covariant: If $\widehat{g}=e^{2 \sigma} g$, then $\widehat{A}_{0}=e^{\sigma} A_{0}$. This observation, (3.3) and Lemma 3.2 together yield the result. \(\square\)

Lemma 3.6. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$. Given $w \in \mathbb{R}$ and $\sigma \in C^{\infty}(X)$, it holds that
$$\begin{aligned}
(\langle\bar{\nabla} H, \bar{\nabla} u\rangle)^{\prime} & =n\langle\bar{\nabla} u, \bar{\nabla} \eta \sigma\rangle-H\langle\bar{\nabla} u, \bar{\nabla} \sigma\rangle+w u\langle\bar{\nabla} H, \bar{\nabla} \sigma\rangle, \\
(\bar{J} \eta u)^{\prime} & =-(\eta u) \bar{\Delta} \sigma+w \bar{J} u \eta \sigma, \\
(P(\eta, \eta) \eta u)^{\prime} & =-(\eta u) \nabla^{2} \sigma(\eta, \eta)+w u P(\eta, \eta) \eta \sigma, \\
\left(H^{2} \eta u\right)^{\prime} & =2 n H(\eta u) \eta \sigma+w H^{2} u \eta \sigma
\end{aligned}$$
for all $u \in C^{\infty}(X)$.
Proof. This follows immediately from (3.3) and Lemma 3.2. \(\square\)

Lemma 3.7. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=\partial X$. Given $w \in \mathbb{R}$ and $\sigma \in C^{\infty}(X)$, it holds that
$$\begin{aligned}
(u \eta J)^{\prime} & =-u \eta \Delta \sigma-2\left(\bar{J}+P(\eta, \eta)+\frac{1}{2(n-1)}\left|A_{0}\right|^{2}-\frac{1}{2 n} H^{2}\right) u \eta \sigma, \\
(u \bar{\Delta} H)^{\prime} & =n u \bar{\Delta} \eta \sigma-H u \bar{\Delta} \sigma+(n-4) u\langle\bar{\nabla} H, \bar{\nabla} \sigma\rangle, \\
(u H \bar{J})^{\prime} & =n \bar{J} u \eta \sigma-H u \bar{\Delta} \sigma, \\
(u H P(\eta, \eta))^{\prime} & =n u P(\eta, \eta) \eta \sigma-H u \nabla^{2} \sigma(\eta, \eta), \\
\left(u\left\langle A_{0}, \bar{P}\right\rangle\right)^{\prime} & =-u\left\langle A_{0}, \bar{\nabla}^{2} \sigma\right\rangle, \\
\left(u H^{3}\right)^{\prime} & =3 n H^{2} u \eta \sigma, \\
\left(u H\left|A_{0}\right|^{2}\right) & =n\left|A_{0}\right|^{2} u \eta \sigma
\end{aligned}$$
for all $u \in C^{\infty}(X)$.
Proof. This follows immediately from Lemma 2.1, (3.3), Lemma 3.2 and the conformal covariance of $A_{0}$. \(\square\)

In particular, we obtain the following family of third-order conformally covariant boundary operators.

Proposition 3.8. Let $\left(X^{n+1}, g\right)$ be a Riemannian manifold with boundary $M^{n}=$ $\partial X$ and let $w \in \mathbb{R}$. Define $B_{3, w}: C^{\infty}(X) \rightarrow C^{\infty}(M)$ by
$$\begin{aligned}
B_{3, w} u:= & -\eta \Delta u+\frac{n+2 w-1}{n+2 w-4} \bar{\Delta} \eta u+\frac{n+3 w-3}{n} H \nabla^{2} u(\eta, \eta) \\
& -\frac{n+2 w-1}{w-1}\left\langle A_{0}, \bar{\nabla}^{2} u\right\rangle-\frac{2 n+7 w-8}{n(n+2 w-4)} H \bar{\Delta} u \\
& +\frac{(n-4)(n+2 w-1)}{n(n+2 w-4)}\langle\bar{\nabla} H, \bar{\nabla} u\rangle+S_{2, w} \eta u-w T_{3, w} u,
\end{aligned}$$
where
$$\begin{aligned}
S_{2, w}= & \left(\frac{w-1}{n}-\frac{(n+3 w-3)(2 w-1)}{2 n^{2}}\right) H^{2}-(n+3 w-1) P(\eta, \eta) \\
& -\frac{n-w-1}{n+2 w-4} \bar{J}, \\
T_{3, w}= & \eta J+\frac{n+2 w-1}{n(n+2 w-4)} \bar{\Delta} H+\frac{n+2 w-1}{w-1}\left\langle A_{0}, \bar{P}\right\rangle \\
& -\frac{n+3 w-3}{n} H P(\eta, \eta)+\frac{n+5 w-7}{n(n+2 w-4)} H \bar{J} \\
& +\frac{1}{n(n-1)} H\left|A_{0}\right|^{2}+\left(\frac{w-2}{3 n^{2}}-\frac{(n+3 w-3)(2 w-1)}{6 n^{3}}\right) H^{3} .
\end{aligned}$$
Given $\sigma \in C^{\infty}(X)$, set $\widehat{g}=e^{2 \sigma} g$. Then
$$\widehat{B}_{3, w}(u)=e^{(w-3) \sigma} B_{3, w}\left(e^{-w \sigma} u\right)$$
for all $u \in C^{\infty}(X)$.

Proof. Lemma 3.4, Lemma 3.5, Lemma 3.6, and Lemma 3.7 together imply that $B_{3, w}^{\prime}=0$. \(\square\)

We are now prepared to prove that the operators $B_{k}^{3}$ for $k \in\{0,1,2,3\}$ are boundary operators associated to the Paneitz operator.

Proof of Theorem 1.1. Observe that $B_{j}^{3}=B_{j,-\frac{n-3}{2}}$ for $j \in\{0,1,2\}$ and that
$$B_{3}^{3}=B_{3-\frac{n-3}{2}}+\frac{1}{2}\left|A_{0}\right|^{2} B_{1,-\frac{n-3}{2}} .$$
It follows from Proposition 3.1, Proposition 3.3 and Proposition 3.8 that if $\widehat{g}=e^{2 \sigma} g$, then
$$\widehat{B}_{k}^{3}(u)=e^{-\frac{n-3+2 k}{2} \sigma} B_{k}^{3}\left(e^{\frac{n-3}{2} \sigma} u\right)$$
for all $u \in C^{\infty}(X)$.
Next, the divergence theorem implies that
$$\begin{aligned}
\int_{X}\left(u L_{4} v-(\Delta u)\right. & \left.(\Delta v)+(4 P-(n-1) J g)(\nabla u, \nabla v)-\frac{n-3}{2} Q u v\right) \\
& =\oint_{M}(u \eta \Delta v-(\Delta v) \eta u+4 u P(\eta, \nabla v)-(n-1) J u \eta v) .
\end{aligned}$$
for all $u, v \in C^{\infty}(X)$. On the other hand, Lemma 2.1 and Lemma 2.2 imply that
$$\begin{aligned}
\oint_{M} J u \eta v & =\oint_{M}\left(\bar{J}+P(\eta, \eta)-\frac{1}{2 n} H^{2}+\frac{1}{2(n-1)}\left|A_{0}\right|^{2}\right) u \eta v, \\
\oint_{M} u P(\eta, \nabla v) & =\oint_{M}\left(u P(\eta, \eta) \eta v+\frac{u}{n-1}\langle\bar{\delta} A-\bar{\nabla} H, \bar{\nabla} v\rangle\right), \\
\oint_{M}(\Delta v) \eta u & =\oint_{M}\left((\eta u)^{2} v(\eta, \eta)-\langle\bar{\nabla} v, \bar{\nabla} \eta u\rangle+H(\eta u)(\eta v)\right)
\end{aligned}$$
for all $u, v \in C^{\infty}(X)$. Inserting these formulae into (3.4) and using the definitions of the boundary operators $B_{k}^{3}$ for $k \in\{0,1,2,3\}$ yields (1.3). It is then clear that $\mathcal{Q}_{4}$ is a symmetric bilinear form. \(\square\)

Remark 3.9. From invariant theory, it is easy to check that the families $B_{0, w}$ and $B_{1, w}$ are the unique (up to constant multiples) families of conformally covariant operators which are natural and homogeneous of degree zero and one, respectively. However, the families $B_{2, w}$ and $B_{3, w}$ are not unique. The scalar $\left|A_{0}\right|^{2}$ is conformally covariant and homogeneous of degree two. By invariant theory and Lemma 2.2 the span of $B_{2, w}$ and $\left|A_{0}\right|^{2}$ gives the set of all natural conformally covariant boundary operators which are homogeneous of degree two. Likewise, the operator $\left|A_{0}\right|^{2} B_{1, w}$ and the scalars $\operatorname{tr} A_{0}^{3}$ and $\left\langle W(\eta, \cdot, \eta, \cdot), A_{0}\right\rangle$ are conformally covariant and homogeneous of degree three. By invariant theory and Lemma 2.4, the span of $B_{3}^{3}$ and these three operators gives the set of all natural conformally covariant boundary operators which are homogeneous of degree three.

The requirement that the operators $B_{k}^{3}$ for $k \in\{0,1,2,3\}$ be boundary operators for the Paneitz operator imposes, in addition to conformal covariance, the requirement that $\mathcal{Q}_{4}$ be symmetric. This requirement imposes three additional constraints. In order to absorb the term
$$\int_{X}\left(u \Delta^{2} v-(\Delta u)(\Delta v)\right)=\oint_{M}\left(u \eta \Delta v-\left(\bar{\Delta} v+\nabla^{2} v(\eta, \eta)+H \eta v\right) \eta u\right)$$
arising in integration by parts, it must hold that
$$\begin{aligned}
& B_{0}^{3}(u) B_{3}^{3}(v)=-u \eta \Delta v+(\text { lower order terms }), \\
& B_{1}^{3}(v) B_{2}^{3}(v)=(\eta u) \nabla^{2} v(\eta, \eta)+(\text { lower order terms }),
\end{aligned}$$
where "lower order terms" means terms with a total number of normal derivatives less than three. To absorb the term involving $\oint\left|A_{0}\right|^{2} u \eta v$ in (3.5) requires that there is a $k \in \mathbb{R}$ such that
$$B_{0}^{3}(u) B_{3}^{3}(v)+B_{1}^{3}(u) B_{2}^{3}(v)=\frac{1}{2}\left|A_{0}\right|^{2}((1+k) u \eta v+k v \eta u)$$
up to terms not involving $\left|A_{0}\right|^{2} \eta$.
In summary, if we normalize $B_{0}^{3}$ and $B_{1}^{3}$ to have leading normal order terms 1 and $\eta$, respectively, then there are three remaining freedoms in how we define the boundary operators: We can add a linear combination of $\operatorname{tr} A_{0}^{3}$ and $\left\langle W(\eta, \cdot, \eta, \cdot), A_{0}\right\rangle$ to $B_{3}^{3}$; and we can add a constant multiple of $\left|A_{0}\right|^{2}$ to $B_{2}^{3}$ while adding the same constant multiple of $\left|A_{0}\right|^{2} B_{1}^{3}$ to $B_{3}^{3}$.

One simple consequence of Theorem 1.1 is the geometric interpretation of positive smooth minimizers of the energy $\mathcal{E}_{4}$.

Proof of Proposition 1.2. Consider first the case that $u \in C^{\infty}(X)$ is a positive minimizer of $Y_{4,2}(X, M)$. Therefore $u$ is a critical point of $\mathcal{E}_{4}$ when restricted to the class of smooth functions $w \in C^{\infty}(X)$ with $\oint\left|B_{0}^{3} w\right|^{\frac{2 n}{n-3}}=1$. Let $u_{t}$ be a one-parameter family of such functions which is $C^{1}$ in $t \in(-\varepsilon, \varepsilon)$ and satisfies $u_{0}=u$. Using Theorem 1.1 we compute that
$$\begin{aligned}
& 0=\left.\frac{1}{2} \frac{d}{d t}\right|_{t=0} \mathcal{E}_{4}\left(u_{t}\right)=\int_{X} v L_{4} u+\oint_{M}\left[B_{0}^{3}(v) B_{3}^{3}(u)+B_{1}^{3}(v) B_{2}^{3}(u)\right], \\
& 0=\left.\frac{1}{2} \frac{d}{d t}\right|_{t=0} \int_{M} u_{t}^{\frac{2 n}{n-3}}=\frac{n}{n-3} \oint_{M} v u^{\frac{n+3}{n-3}}
\end{aligned}$$
for $v=\left.\frac{\partial u_{t}}{\partial t}\right|_{t=0}$. Thus there is a constant $\lambda \in \mathbb{R}$ such that
$$\left\{\begin{array}{l}
L_{4} u=0, \\
B_{2}^{3} u=0, \\
B_{3}^{3} u=\lambda u^{\frac{n+3}{n-3}} .
\end{array}\right.$$
From the assumption $\mathcal{E}_{4}(u)=Y_{4,2}(X, M)$ we compute that $\lambda=Y_{4,2}(X, M)$. The final conclusion for $\widehat{g}=u^{\frac{4 n}{n-3}} g$ follows from Theorem 1.1

Consider next the case that $u \in C^{\infty}(X)$ is a positive minimizer of $Y_{4,1}(X, M)$. Therefore $u$ is a critical point of $\mathcal{E}_{4}$ when restricted to the class of smooth functions $w \in C^{\infty}(X)$ with $B_{1}^{3} w=0$ and $\oint\left|B_{0}^{3} w\right|^{\frac{2 n}{n-3}}=1$. Arguing as above, we deduce that
$$\left\{\begin{array}{l}
L_{4} u=0 \\
B_{1}^{3} u=0 \\
B_{3}^{3} u=Y_{4,1}(X, M) u^{\frac{n+3}{n-3}}
\end{array}\right.$$
The final conclusion for $\widehat{g}=u^{\frac{4 n}{n-3}} g$ again follows from Theorem 1.1. \(\square\)

Remark 3.10. The Euler equation (3.8) holds for any boundary volume-constrained critical point $u$ of $\mathcal{E}_{4}$. By changing the constraints, it is clear that the energy functional $\mathcal{E}_{4}$ gives a variational approach to simultaneously prescribing the interior
$Q$-curvature, the $T_{3}^{3}$-curvature of the boundary, and one of the mean curvature and the $T_{2}^{3}$-curvature of the boundary.

\section*{4. Boundary operators and pseudodifferential operators}

From their explicit expressions, it is clear that the Paneitz operator $L_{4}$ is properly elliptic and that the boundary operators $B_{k}^{3}$ are of the form $B_{k}^{3}=\left(\nabla_{\eta}\right)^{k}+$ (lower order terms) for $k \in\{0,1,2,3\}$, where "lower order terms" means terms which involve fewer than $k$ derivatives in the normal direction. It follows that the boundary value problems $\left(L_{4} ;\left(B_{0}^{3}, B_{1}^{3}\right)\right),\left(L_{4} ;\left(B_{0}^{3}, B_{2}^{3}\right)\right)$ and $\left(L_{4} ;\left(B_{1}^{3}, B_{3}^{3}\right)\right)$ all satisfy the Lopatinskii-Shapiro conditions (cf. [2, 7]). Moreover, the symmetry of the bilinear form $\mathcal{Q}_{4}$ implies that each of these boundary value problems is formally self-adjoint. Therefore, so long as the null space of the given boundary value problem is trivial, to any pair of smooth initial data there exists a unique smooth solution $u \in \operatorname{ker} L_{4}$. For example, if $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}=\{0\}$, then given $f, \psi \in C^{\infty}(M)$, there exists a unique function $u_{f, \psi} \in C^{\infty}(X)$ such that
$$\left\{\begin{array}{l}
L_{4} u_{f, \psi}=0, \\
B_{0}^{3} u_{f, \psi}=f, \\
B_{1}^{3} u_{f, \psi}=\psi .
\end{array}\right.$$

The solution to (4.1) can be constructed variationally. This is simplest when $\lambda_{1}\left(L_{4}\right)>0$, in which case the solution to (4.1) minimizes the energy $\mathcal{E}_{4}$ within the class of functions $u \in C^{\infty}(X)$ with fixed trace $(f, \psi)=\left(B_{0}^{3} u, B_{1}^{3} u\right)$.

Proof of Proposition 1.3. Let
$$\mathcal{C}_{f, \psi}=\left\{u \in C^{\infty}(X) \mid B_{0}^{3} u=f, B_{1}^{3} u=\psi\right\} .$$
It follows from Theorem 1.1 that critical points of $\mathcal{E}_{4}: \mathcal{C}_{f, \psi} \rightarrow \mathbb{R}$ satisfy (4.1).
Fix $u \in \mathcal{C}_{f, \psi}$. Then $\mathcal{C}_{f, \psi}=u+\mathcal{C}_{0,0}$. Given $v \in \mathcal{C}_{0,0}$, Theorem 1.1 implies that
$$\mathcal{E}_{4}(u+v)=\mathcal{E}_{4}(v)+2 \int_{X} v L_{4} u+\mathcal{E}_{4}(u) .$$
Using the assumption $\lambda_{1}\left(L_{4}\right)>0$, we find that
$$\mathcal{E}_{4}(u+v) \geq \mathcal{E}_{4}(u)-\frac{1}{\lambda_{1}\left(L_{4}\right)} \int_{X}\left(L_{4} u\right)^{2} .$$
Therefore $\mathcal{E}_{4}$ is bounded below on $\mathcal{C}_{f, \psi}$. By taking a minimizing sequence, we thus obtain a weak solution $u$ of (4.1). Since $\left(L_{4} ;\left(B_{0}^{3}, B_{1}^{3}\right)\right)$ satisfies the Lopatinskii-Shapiro conditions, it holds that $u \in C^{\infty}(X)$.

Finally, if $u_{1}, u_{2}$ both satisfy (4.1), then $w=u_{1}-u_{2}$ is such that $w \in \operatorname{ker} L_{4} \cap$ $\operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}$, and hence $w \equiv 0$. \(\square\)

Suppose now that $\left(X^{n+1}, g\right)$ is a compact Riemannian manifold with boundary $M^{n}=\partial X$ such that the null space of the boundary value problem $\left(L_{4} ;\left(B_{0}^{3}, B_{1}^{3}\right)\right)$ is trivial. Hence the operators $\mathcal{B}_{1}^{3}, \mathcal{B}_{3}^{3}: C^{\infty}(M) \rightarrow C^{\infty}(M)$ given by
$$\begin{aligned}
\mathcal{B}_{1}^{3} \psi & =\frac{1}{2} B_{2}^{3} u_{0, \psi}, \\
\mathcal{B}_{3}^{3} f & =\frac{1}{2} B_{3}^{3} u_{f, 0}
\end{aligned}$$
are well-defined. In fact, $\mathcal{B}_{1}^{3}$ and $\mathcal{B}_{3}^{3}$ are formally self-adjoint conformally covariant first- and third-order pseudodifferential operators, respectively:

Proposition 4.1. Let $\left(X^{n+1}, g\right)$ be a compact Riemannian manifold with boundary $M^{n}=\partial X$ such that the null space of $\left(L_{4} ;\left(B_{0}^{3}, B_{1}^{3}\right)\right)$ is trivial. Then $\mathcal{B}_{1}^{3}$ and $\mathcal{B}_{3}^{3}$ are formally self-adjoint conformally covariant pseudodifferential operators with principal symbols $\sigma\left(\mathcal{B}_{k}^{3}\right)=\sigma\left((-\Delta)^{k / 2}\right)$ for $k \in\{1,3\}$. Indeed, given $w \in C^{\infty}(M)$, set $\widehat{h}=e^{2 w} h$. Then
$$\widehat{\mathcal{B}}_{k}^{3}(\psi)=e^{-\frac{n+k}{2} w} \mathcal{B}_{k}^{3}\left(e^{\frac{n-k}{2} w} \psi\right)$$
for $k \in\{1,3\}$ and all $f, \psi \in C^{\infty}(M)$.
Proof. Let $f_{1}, f_{2} \in C^{\infty}(M)$. For $j \in\{1,2\}$, let $u_{j}=u_{f_{j}, 0}$ be as in (4.1). It follows from Theorem 1.1 that
$$\oint_{M} f_{1} \mathcal{B}_{3}^{3} f_{2}=\frac{1}{2} \mathcal{E}_{4}\left(u_{1}, u_{2}\right)=\oint_{M} f_{2} \mathcal{B}_{3}^{3} f_{1} .$$
That $\mathcal{B}_{1}^{3}$ is formally self-adjoint follows similarly.
Let $v \in C^{\infty}(X)$ be such that $B_{0}^{3} v=w$. Set $\widehat{g}=e^{2 v} g$. Given $f, \psi \in C^{\infty}(M)$, let $u_{f, \psi}, \widehat{u}_{\widehat{f}, \widehat{\psi}} \in C^{\infty}(X)$ be such that
$$\begin{array}{lll}
L_{4} u_{f, \psi}=0, & B_{0}^{3} u_{f, \psi}=f, & B_{1}^{3} u_{f, \psi}=\psi, \\
\widehat{L}_{4} \widehat{u}_{\widehat{f}, \psi}=0, & \widehat{B}_{0}^{3} \widehat{u}_{\widehat{f}, \widehat{\psi}}=e^{-\frac{n-3}{2} w} f, & \widehat{B}_{1}^{3} \widehat{u}_{\widehat{f}, \widehat{\psi}}=e^{-\frac{n-1}{2} w} \psi .
\end{array}$$
It follows from Theorem 1.1 that
$$\widehat{u}_{\widehat{f}, \widehat{\psi}}=e^{-\frac{n-3}{2} v} u_{f, \psi} .$$
Applying Theorem 1.1 in the special cases $f=0$ and $\psi=0$ yields the conformal covariance of $\mathcal{B}_{1}^{3}$ and $\mathcal{B}_{3}^{3}$, respectively.

The claim that $\mathcal{B}_{k}^{3}$ are pseudodifferential operators for $k \in\{1,3\}$ follows as in [7]: From the homogeneity of $\mathcal{B}_{k}^{3}$, which is an immediate consequence of (4.2), and the fact that the Paneitz operator and its boundary operators are all $O(T M)$-invariant, it follows that $\sigma\left(\mathcal{B}_{k}^{3}\right)(x, \xi)=c_{k}(x)|\xi|^{k}$ for some $c_{k} \in C^{\infty}(M)$. Since the principal symbol of the Paneitz operator is that of the bi-Laplacian $\Delta^{2}$, the principal symbols of the extension operators $f \mapsto u_{f, 0}$ and $\psi \mapsto u_{0, \psi}$ depend only on $|\xi|$, and hence $c_{k}$ is a universal constant [29]. It follows from Theorem 1.4 and the identification of the principal symbol of the fractional GJMS operators [25] that $c_{k}=1$. \(\square\)

Remark 4.2. Note that our proof of conformal covariance shows that the operators $\mathcal{B}_{k}^{3}$ for $k \in\{1,3\}$ depend only on $[g]$ and a choice of metric $h$ in the induced conformal class on $M$.

There is another way one can define first- and third-order conformally covariant pseudodifferential operators on the boundary of a compact Riemannian manifold $\left(X^{n+1}, g\right)$, namely via scattering theory [25]. Let $g_{+} \in[g]$ be an asymptotically hyperbolic metric in the interior $X_{0}$ of $X$ and let $r \geq 0$ be the geodesic defining function associated to $h$. Suppose that $\frac{n^{2}-1}{4}, \frac{n^{2}-9}{4} \notin \sigma_{p p}\left(-\Delta_{g_{+}}\right)$and that
$$\left.\frac{\partial}{\partial r}\right|_{r=0} \log \operatorname{det}\left(h_{r}^{-1} h_{r}\right)=0=\left.\frac{\partial^{3}}{\partial r^{3}}\right|_{r=0} \log \operatorname{det}\left(h_{r}^{-1} h_{r}\right),$$
where $g_{+}=r^{-2}\left(d r^{2}+h_{r}\right)$ near $M$ for $h_{r}$ a one-parameter family of Riemannian metrics on $M$. Fix $f, \psi \in C^{\infty}(M)$. By the spectral assumption, there are unique functions $v_{f}, v_{\psi} \in C^{\infty}\left(X_{0}\right)$ such that
$$\begin{aligned}
-\Delta v_{f}-\frac{n^{2}-9}{4} v_{f} & =0, \quad-\Delta v_{\psi}-\frac{n^{2}-1}{4} v_{\psi}=0, \\
\lim _{r \rightarrow 0} r^{-\frac{n-3}{2}} v_{f} & =f, \quad \lim _{r \rightarrow 0} r^{-\frac{n-1}{2}} v_{\psi}=\psi .
\end{aligned}$$
From the condition (4.3), we compute that there are functions $G_{f}, G_{\psi} \in C^{\infty}(M)$ such that
$$\begin{aligned}
& v_{\psi}=r^{\frac{n-1}{2}}\left(\psi+G_{\psi} r-\frac{r^{2}}{2}\left(\bar{\Delta} \psi+\frac{n-1}{4}\left(h^{i j} h_{i j}^{\prime}\right)^{\prime} \psi\right)+O\left(r^{3}\right)\right), \\
& v_{f}=r^{\frac{n-3}{2}}\left(f+\frac{r^{2}}{2}\left(\bar{\Delta} f+\frac{n-3}{4}\left(h^{i j} h_{i j}^{\prime}\right)^{\prime} f\right)+G_{f} r^{3}+O\left(r^{4}\right)\right),
\end{aligned}$$
In other words, the condition (4.3) implies that the scattering operators $S\left(\frac{n+1}{2}\right)$ and $S\left(\frac{n+3}{2}\right)$ have no residues (cf. [25, 27]). Hence the operators $P_{1}, P_{3}: C^{\infty}(M) \rightarrow$ $C^{\infty}(M)$ given by
$$P_{1} \psi:=-G_{\psi}, \quad P_{3} f:=3 G_{f},$$
are well-defined; indeed, $P_{1}$ and $P_{3}$ are first- and third-order conformally covariant pseudodifferential operators with principal symbol that of $(-\Delta)^{1 / 2}$ and $(-\Delta)^{3 / 2}$, respectively [25].

It is natural to ask if $\mathcal{B}_{1}=P_{1}$ and $\mathcal{B}_{3}=P_{3}$ in the setting of the previous paragraph. While we cannot answer this question in general, we can answer it in the case when $\left(X^{n+1}, g\right)$ is a compactification of a Poincaré-Einstein manifold. In fact, we prove a stronger result in this setting: the fractional GJMS operators $P_{1}$ and $P_{3}$ can be computed directly from the boundary operators $B_{k}^{3}$ when acting on Paneitz-harmonic functions.

Proof of Theorem 1.4. By Theorem 1.4 and the conformal covariance of the fractional GJMS operators $P_{1}$ and $P_{3}$, it suffices to prove the result for the metric
$$\begin{aligned}
g & =r^{2} g_{+}=d r^{2}+h_{r}, \\
h_{r} & =h-r^{2} \bar{P}+O\left(r^{3}\right),
\end{aligned}$$
where $r$ is a geodesic defining function. Moreover, the coefficient of $r^{3}$ in the expansion of $h_{r}$ is tracefree; indeed, it vanishes for dimensions at least four [22]. In particular, $A, P(\eta, \eta)$ and $\eta J$ all vanish identically along $M$.

Let $u \in C^{\infty}(X)$ satisfy $L_{4} u=0$. Set $f=B_{0}^{3} u$ and $\psi=B_{1}^{3} u$. Let $v_{f}$ and $v_{\psi}$ be as in (4.4). It follows from (4.5) and (4.6) that
$$\begin{aligned}
& r^{\frac{n-3}{2}} v_{f}=f-\frac{r^{2}}{2}\left(-\bar{\Delta} f+\frac{n-3}{2} \bar{J} f\right)+\frac{r^{3}}{3} P_{3} f+O\left(r^{4}\right), \\
& r^{\frac{n-3}{2}} v_{\psi}=r \psi-r^{2} P_{1} \psi+\frac{r^{3}}{2}\left(-\bar{\Delta} \psi+\frac{n-1}{2} \bar{J} \psi\right)+O\left(r^{4}\right),
\end{aligned}$$
while the uniqueness of solutions to the problem $\left(L_{4} ;\left(B_{0}^{3}, B_{1}^{3}\right)\right)$, the factorization (1.6), and conformal covariance implies that $u=\left(v_{f}-v_{\psi}\right) r^{\frac{n-3}{2}}$. Therefore
$$\begin{aligned}
u=f-\psi r+\left(P_{1} \psi-\frac{1}{2}(-\bar{\Delta} f\right. & \left.\left.+\frac{n-3}{2} \bar{J} f\right)\right) r^{2} \\
+ & \left(\frac{1}{3} P_{3} f-\frac{1}{2}\left(-\bar{\Delta} \psi+\frac{n-1}{2} \bar{J} \psi\right)\right) r^{3}+O\left(r^{4}\right) .
\end{aligned}$$
In particular,
$$\begin{aligned}
\nabla^{2} u(\eta, \eta) & =2 P_{1} \psi+\bar{\Delta} f-\frac{n-3}{2} \bar{J} f, \\
-\eta \Delta u & =2 P_{3}+2 \bar{\Delta} \psi-\frac{3 n-5}{2} \bar{J} \psi .
\end{aligned}$$
Inserting these identities into the definitions of $B_{2}^{3}$ and $B_{3}^{3}$ yields
$$B_{2}^{3}=2 P_{1} \psi, \quad B_{3}^{3} u=2 P_{3} f .$$ \(\square\)

An immediate corollary of Theorem 1.4 is that for compactifications of Poincaré-Einstein manifolds, if $u \in \operatorname{ker} L_{4}$, then $B_{2}^{3} u=2 \mathcal{B}_{1}^{3} B_{1}^{3} u$ and $B_{3}^{3} u=2 \mathcal{B}_{3}^{3} B_{0}^{3} u$. This decoupling is helpful when studying Paneitz-harmonic functions, and so it is useful to characterize more generally when it occurs.

Lemma 4.3. Let $\left(X^{n+1}, g\right)$ be a compact Riemannian manifold with boundary $M^{n}=\partial X$ and suppose that $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}=\{0\}$.
\begin{itemize}
\item[(1)] $B_{2}^{3} u_{f, 0}=0$ for all $f \in C^{\infty}(M)$ if and only if $B_{2}^{3} u_{f, \psi}=2 \mathcal{B}_{1}^{3} \psi$ for all $f, \psi \in C^{\infty}(M)$.
\item[(2)] $B_{3}^{3} u_{0, \psi}=0$ for all $\psi \in C^{\infty}(M)$ if and only if $B_{3}^{3} u_{f, \psi}=2 \mathcal{B}_{3}^{3} f$ for all $f, \psi \in C^{\infty}(M)$.
\end{itemize}

Proof. Since $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}=\{0\}$, given $f, \psi \in C^{\infty}(M)$, there is a unique solution $u_{f, \psi} \in C^{\infty}(X)$ of the boundary value problem (4.1). Since $L_{4}$ and the boundary operators $B_{k}^{3}$ are all linear, it holds that $u_{f, \psi}=u_{f, 0}+u_{0, \psi}$. In particular, if $B_{2}^{3} u_{f, 0}=0$ for all $f \in C^{\infty}(M)$, then
$$B_{2}^{3} u_{f, \psi}=B_{2}^{3} u_{0, \psi}=2 \mathcal{B}_{1}^{3} \psi .$$
The other conclusions follow similarly. \(\square\)

\section*{5. Sharp Sobolev trace inequalities}

Proposition 1.3 and Theorem 1.4 can be applied to establish sharp Sobolev trace inequalities involving $W^{2,2}$ on standard models. We focus here on Euclidean upper half space $\left(\mathbb{R}_{+}^{n+1}, d x^{2}\right)$ and the round upper hemisphere $\left(S_{+}^{n+1}, d \theta^{2}\right)$, though similar results on other conformally equivalent spaces readily follow from Theorem 1.1.

First note that Proposition 1.3 gives a norm computation for the Sobolev trace embedding
$$W^{2,2}\left(X^{n+1}\right) \hookrightarrow H^{3 / 2}(M) \oplus H^{1 / 2}(M)$$
and an identification of a right inverse. To make this completely rigorous, (1.5) must be rewritten with the $L^{2}$-norm of $\nabla^{2} u$ rather than $\Delta u$, as otherwise the estimates degenerate. For example, if $\psi=(-\Delta)^{1 / 2} f$ on $\mathbb{R}^{n}$, then the harmonic extension $u_{f}$ of $f$ to $\mathbb{R}_{+}^{n+1}$ is also the solution $u_{f, \psi}$. The correct formulation follows from Reilly's formula [34], which we recast here in terms of $B_{0}^{3}$ and $B_{1}^{3}$ as follows.

Lemma 5.1. Let $\left(X^{n+1}, g\right)$ be a compact Riemannian manifold with boundary $M^{n}=\partial X$. Let $u \in C^{\infty}(X)$ and set $f=B_{0}^{3} u$ and $\psi=B_{1}^{3} u$. Then
$$\begin{aligned}
\int_{X}\left|\nabla^{2} u\right|^{2}= & \int_{X}\left[(\Delta u)^{2}-(n-1) P(\nabla u, \nabla u)-J|\nabla u|^{2}\right] \\
& -\oint_{M}\left[H \psi^{2}-2\langle\bar{\nabla} \psi, \bar{\nabla} f\rangle-(n-3) H^{2} f \psi\right. \\
& \left.+(A+(n-3) H h)(\bar{\nabla} f, \bar{\nabla} f)-\frac{n-3}{2}\left(\bar{\Delta} H-\frac{n-3}{2} H^{3}\right) f^{2}\right] .
\end{aligned}$$
Proof. Recall Reilly's formula [34]
$$\begin{aligned}
\int_{X}\left[\left|\nabla^{2} u\right|^{2}-(\Delta u)^{2}+(n-1) P\right. & \left.(\nabla u, \nabla u)+J|\nabla u|^{2}\right] \\
& =\oint_{M}\left[2\langle\bar{\nabla} \eta u, \bar{\nabla} u\rangle-A(\bar{\nabla} u, \bar{\nabla} u)-H(\eta u)^{2}\right] .
\end{aligned}$$
The conclusion follows from the definitions of $B_{0}^{3}$ and $B_{1}^{3}$. \(\square\)

Corollary 5.2. On Euclidean upper half space $\left(\mathbb{R}_{+}^{n+1}, d x^{2}\right)$,
$$\int_{\mathbb{R}_{+}^{n+1}}\left|\nabla^{2} u\right|^{2} \geq 2 \int_{\mathbb{R}^{n}}\left[f(-\Delta)^{3 / 2} f-\langle\bar{\nabla} f, \bar{\nabla} \psi\rangle+\psi(-\Delta)^{1 / 2} \psi\right]$$
for all $u \in C_{0}^{\infty}\left(\mathbb{R}_{+}^{n+1}\right)$, where $f(x)=u(x, 0)$ and $\psi(x)=-u_{y}(x, 0)$. Moreover, equality holds if and only if $\Delta^{2} u=0$.

Proof. From Lemma 5.1 we compute that
$$\int_{\mathbb{R}_{+}^{n+1}}\left|\nabla^{2} u\right|^{2}=\int_{\mathbb{R}_{+}^{n+1}}(\Delta u)^{2}+2 \oint_{\mathbb{R}^{n}}\langle\bar{\nabla} \psi, \bar{\nabla} f\rangle .$$
On the other hand, Proposition 1.3 and Theorem 1.4 imply that
$$\int_{\mathbb{R}_{+}^{n+1}}(\Delta u)^{2} \geq \oint_{\mathbb{R}^{n}}\left[2 f(-\Delta)^{3 / 2} f-4\langle\bar{\nabla} f, \bar{\nabla} \psi\rangle+2 \psi(-\Delta)^{1 / 2} \psi\right]$$
with equality if and only if $\Delta^{2} u=0$. Combining these facts yields the result. \(\square\)

Our second goal is to prove Theorem 1.6. This gives a sharp Sobolev trace inequality which gives a norm computation for the embedding
$$W^{2,2}\left(\mathbb{R}_{+}^{n+1}\right) \hookrightarrow L^{\frac{2 n}{n-3}}\left(\mathbb{R}^{n}\right) \oplus L^{\frac{2 n}{n-1}}\left(\mathbb{R}^{n}\right) .$$
The embedding can be realized from the trace map and the embeddings $H^{\gamma}\left(\mathbb{R}^{n}\right) \hookrightarrow$ $L^{\frac{2 n}{n-2 \gamma}}\left(\mathbb{R}^{n}\right)$ for $\gamma \in\{1 / 2,3 / 2\}$. The proof of Theorem 1.6 also proceeds in this manner: We apply Proposition 1.3 and Theorem 1.4 to relate the energy $\mathcal{E}_{4}$ to the energies of the fractional GJMS operators $P_{1}$ and $P_{3}$, and then apply the sharp fractional Sobolev inequalities [5, 30].

Proof of Theorem 1.6. Let $u \in C^{\infty}\left(S_{+}^{n+1}\right)$ and set $f=B_{0}^{3} u$ and $\psi=B_{1}^{3} u$. It follows from Proposition 1.3 and Theorem 1.4 that
$$\frac{1}{2} \mathcal{E}_{4}(u) \geq \oint_{S^{n}} f P_{3} f+\oint_{S^{n}} \psi P_{1} \psi .$$

On the other hand, the fractional Sobolev inequalities (cf. [5, 30]) state that
$$\oint_{S^{n}} w P_{2 \gamma} w \geq C_{2 \gamma}\left(\oint_{S^{n}}|w|^{\frac{2 n}{n-2 \gamma}}\right)^{\frac{n-2 \gamma}{n}}$$
for all $w \in C^{\infty}\left(S^{n}\right)$ and all $\gamma \in(0, n / 2)$, where
$$C_{2 \gamma}=2^{2 \gamma} \pi^{\gamma} \frac{\Gamma\left(\frac{n+2 \gamma}{2}\right)}{\Gamma\left(\frac{n-2 \gamma}{2}\right)}\left(\frac{\Gamma(n / 2)}{\Gamma(n)}\right)^{\frac{2 \gamma}{n}} .$$
Moreover, equality holds if and only if there are constants $a_{1}, a_{2} \in \mathbb{R}$ and points $\xi_{1}, \xi_{2} \in B_{1}(0) \subset \mathbb{R}^{n+1}$ such that $f(x)=a_{1}\left(1+x \cdot \xi_{1}\right)^{-\frac{n-3}{2}}$ and $\psi(x)=a_{2}(1+$ $\left.\xi \cdot \xi_{2}\right)^{-\frac{n-1}{2}}$. The conclusion now follows from the fact that $S_{+}^{n+1}$ is Einstein with $P=\frac{1}{2} g$ and the boundary $S^{n}=\partial S_{+}^{n+1}$ is totally geodesic. \(\square\)

\section*{6. Four-manifolds with boundary}

Consider now the special case of a Riemannian four-manifold $\left(X^{4}, g\right)$ with boundary $M^{3}=\partial X$. In this case the boundary operators $B_{k}^{3}: C^{\infty}(X) \rightarrow C^{\infty}(M)$ from Theorem 1.1 are given by
$$\begin{aligned}
B_{0}^{3} u & =u, \\
B_{1}^{3} u & =\eta u, \\
B_{2}^{3} u & =-\bar{\Delta} u+\nabla^{2} u(\eta, \eta)+\frac{1}{3} H \eta u, \\
B_{3}^{3} u & =-\eta \Delta u-2 \bar{\Delta} \eta u+2\left\langle A_{0}, \bar{\nabla}^{2} u\right\rangle-\frac{2}{3} H \bar{\Delta} u+\frac{2}{3}\langle\bar{\nabla} H, \bar{\nabla} u\rangle+S_{2}^{3} \eta u
\end{aligned}$$
for all $u \in C^{\infty}(X)$, where
$$S_{2}^{3}=2 \bar{J}-2 P(\eta, \eta)-\frac{1}{3} H^{2}+\frac{1}{2}\left|A_{0}\right|^{2} .$$
For each $k \in\{1,2,3\}$, the kernel of the boundary operator $B_{k}^{3}$ constants the constant functions, and thus the "Branson trick" [9] implies that the scalar invariants
$$\begin{aligned}
T_{1}^{3} & =\frac{1}{3} H \\
T_{2}^{3} & =\bar{J}-P(\eta, \eta)+\frac{1}{18} H^{2}, \\
T_{3}^{3} & =\eta J-\frac{2}{3} \bar{\Delta} H-2\left\langle A_{0}, \bar{P}\right\rangle+\frac{4}{3} H \bar{J}+\frac{1}{3} H\left|A_{0}\right|^{2}-\frac{2}{27} H^{3}
\end{aligned}$$
act as the $Q$-curvatures associated to the respective operators $B_{k}^{3}$. This can also be verified directly.

Proposition 6.1. Let $\left(X^{4}, g\right)$ be a Riemannian four-manifold with boundary $M^{3}=$ $\partial X$. Let $\sigma \in C^{\infty}(X)$ and consider the metric $\widehat{g}=e^{2 \sigma} g$. For each $k \in\{1,2,3\}$, it holds that
$$e^{k \sigma} \widehat{T}_{k}^{3}=T_{k}^{3}+B_{k}^{3} \sigma .$$
Proof. (3.3) establishes the claim when $k=1$. By Theorem 1.1, both $B_{2}^{3}$ and $B_{3}^{3}$ are conformally covariant, and thus it suffices to show that
$$\left.\frac{d}{d t}\right|_{t=0} e^{t k \sigma} T_{k}^{3}\left[e^{2 t \sigma}\right]=B_{k}^{3} \sigma$$
for $k \in\{2,3\}$ (cf. Section 3). This follows immediately from Lemma 3.2 when $k=2$ and from Lemma 3.7 when $k=3$. \(\square\)

It follows that $\int Q_{4}+\oint T_{3}^{3}$ is a conformal invariant of a compact Riemannian four-manifold with boundary (cf. [15]).
Corollary 6.2. Let $\left(X^{4}, g\right)$ be a compact Riemannian manifold with boundary $M^{3}=\partial X$. Let $\sigma \in C^{\infty}(X)$ and consider the metric $\widehat{g}=e^{2 \sigma} g$. Then
$$\int_{X} \widehat{Q}_{4}+\oint_{M} \widehat{T}_{3}^{3}=\int_{X} Q_{4}+\oint_{M} T_{3}^{3} .$$
Proof. Proposition 6.1 and the transformation formula for the $Q$-curvature imply that
$$\int_{X} \widehat{Q}_{4} \mathrm{dvol}_{\widehat{g}}+\oint_{M} \widehat{T}_{3}^{3} \mathrm{dvol}_{\widehat{h}}=\int_{X}\left(Q_{4}+P_{4} \sigma\right) \mathrm{dvol}_{g}+\oint_{M}\left(T_{3}^{3}+B_{3}^{3} \sigma\right) \mathrm{dvol}_{h} .$$
Since $P_{4} 1=0$ and $B_{k}^{3} 1=0$ for $k \in\{1,2,3\}$, Theorem 1.1 yields the conclusion. \(\square\)

It is instructive to compare our boundary operators to the operators defined by Chang and Qing [15]. To that end, define $P_{3}, P_{3}^{2}: C^{\infty}(X) \rightarrow C^{\infty}(M)$ by
$$\begin{aligned}
& P_{3}(u)=-\frac{1}{2} \eta \Delta u-\bar{\Delta} \eta u+\left\langle A-\frac{2}{3} H \bar{g}, \bar{\nabla}^{2} u\right\rangle+\frac{1}{3}\langle\bar{\nabla} H, \bar{\nabla} u\rangle-(\operatorname{Ric}(\eta, \eta)-2 J) \eta u, \\
& P_{3}^{2}(u)=H \bar{\Delta} u-H \nabla^{2} u(\eta, \eta)-\left(3 \operatorname{Ric}(\eta, \eta)-6 J-\frac{1}{3} H^{2}\right) \eta u
\end{aligned}$$
and set
$$T=\frac{1}{2} \eta J-\frac{1}{3} \bar{\Delta} H+J H-\langle R(\eta, \cdot, \eta, \cdot), A\rangle-\frac{1}{3} \operatorname{tr} A^{3}+\frac{1}{9} H^{3} .$$
These operators are defined exactly as in [15], and differ from our boundary operators by local conformal invariants (cf. Remark 3.9):
Lemma 6.3. Let $\left(X^{4}, g\right)$ be a Riemannian manifold with boundary $M^{3}=\partial X$. Then
$$\begin{aligned}
P_{3} & =\frac{1}{2} B_{3}^{3}, \\
P_{3}^{2} & =-3 T_{1}^{3} B_{2}^{3}+3 T_{2}^{3} B_{1}^{3}+\frac{3}{4}\left|A_{0}\right|^{2} B_{1}^{3}, \\
T & =\frac{1}{2} T_{3}^{3}-2\left\langle W(\eta, \cdot, \eta, \cdot), A_{0}\right\rangle-\frac{4}{3} \operatorname{tr} A_{0}^{3} .
\end{aligned}$$
Proof. Since $M$ is three-dimensional, it holds that
$$\begin{aligned}
|A|^{2} & =\left|A_{0}\right|^{2}+\frac{1}{3} H^{2}, \\
\operatorname{tr} A^{3} & =\operatorname{tr} A_{0}^{3}+H\left|A_{0}\right|^{2}+\frac{1}{9} H^{3} .
\end{aligned}$$
On the other hand, it follows from Lemma 2.1 that
$$\begin{aligned}
\langle R(\eta, \cdot, \eta, \cdot), A\rangle= & 2\left\langle W(\eta, \cdot, \eta, \cdot), A_{0}\right\rangle+\left\langle\bar{P}, A_{0}\right\rangle \\
& +\frac{1}{3} H \bar{J}+H P(\eta, \eta)-\frac{1}{18} H^{3}-\frac{1}{4} H\left|A_{0}\right|^{2}+\operatorname{tr} A_{0}^{3}, \\
\operatorname{Ric}(\eta, \eta)-2 J= & P(\eta, \eta)-\bar{J}+\frac{1}{6} H^{2}-\frac{1}{4}\left|A_{0}\right|^{2} .
\end{aligned}$$
Inserting these formulae into the definitions of $P_{3}, P_{3}^{2}, T$ yields the result. \(\square\)

Proposition 6.1 states that $T_{3}^{3}$ can be regarded as the $Q$-curvature associated to $B_{3}^{3}$. By choosing the interior metric appropriately, it also gives rise to a $Q$-curvature associated $\mathcal{B}_{3}^{3}$.

Definition 6.4. Let $\left(X^{4}, g\right)$ be a compact Riemannian manifold with boundary $M^{3}=\partial X$ and suppose that $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}=\{0\}$. The $\mathcal{T}$-curvature of $\left(M^{3}, h\right)$ is defined by
$$\mathcal{T}_{3}^{3}:=\frac{1}{2} \widehat{T}_{3}^{3},$$
where $\widehat{T}_{3}^{3}$ is determined by $\widehat{g}=e^{2 v} g$ for $v$ the unique solution of
$$\begin{cases}P_{4} v+Q_{4}=0, & \text { in } X, \\ v=0, & \text { on } M, \\ B_{1}^{3} v+\frac{1}{3} H=0, & \text { on } M .\end{cases}$$

Equivalently, $\widehat{g}$ is the unique metric such that $\left.\widehat{g}\right|_{T M}=h, \widehat{Q}_{4}=0$, and $\widehat{H}=0$. It is clear that $\mathcal{T}_{3}$ depends only on $\left(M^{3}, h\right)$ and the conformal fill-in $\left(X^{4},[g]\right)$, and not a specific choice of metric in $X$. There are two ways in which $\mathcal{T}_{3}^{3}$ can be regarded as a critical $Q$-curvature. The first is its conformal transformation formula.

Proposition 6.5. Let $\left(X^{4}, g\right)$ be a compact Riemannian manifold with boundary $\left(M^{3}, h\right)=\left(\partial X,\left.g\right|_{T M}\right)$ and suppose that $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}=\{0\}$. Given $w \in C^{\infty}(M)$, set $\widehat{h}=e^{2 w} h$. Then
$$e^{3 w} \widehat{\mathcal{T}}_{3}^{3}=\mathcal{T}_{3}^{3}+\mathcal{B}_{3}^{3} w .$$

Proof. Without loss of generality, we may suppose that the metric $g$ is such that $Q_{4}=0$ and $H=0$. Let $\widehat{g}=e^{2 v} g$ be the unique metric such that $\left.\widehat{g}\right|_{T M}=\widehat{h}$, $\widehat{Q}_{4}=0$, and $\widehat{H}=0$. It follows from the conformal transformation formula for $Q_{4}$ and Proposition 6.1 that $L_{4} v=0, B_{0}^{3} v=w$, and $B_{1}^{3} v=0$. Therefore
$$e^{3 w} \widehat{\mathcal{T}}_{3}=\frac{1}{2} e^{3 w} \widehat{T}_{3}^{3}=\frac{1}{2}\left(\widehat{T}_{3}^{3}+B_{3}^{3} v\right)=\mathcal{T}_{3}^{3}+\mathcal{B}_{3}^{3} w .$$ \(\square\)

Proposition 4.1 and Proposition 6.5 together imply that the total $\mathcal{T}$-curvature is a conformal invariant of $\left(M^{3}, h\right)$ as the boundary of $\left(X^{4},[g]\right)$. Indeed, the total $\mathcal{T}$-curvature is closely related to the Euler characteristic of $X$ (cf. [4, 16]).

Proposition 6.6. Let $\left(X^{4}, g\right)$ be a compact Riemannian manifold with boundary $M^{3}=\partial X$ and suppose that $\operatorname{ker} L_{4} \cap \operatorname{ker} B_{0}^{3} \cap \operatorname{ker} B_{1}^{3}=\{0\}$. Then
$$8 \pi^{2} \chi(X)=\int_{X}|W|^{2}+2 \oint_{M} \mathcal{T}_{3}^{3}-\frac{2}{3} \oint_{M} \operatorname{tr} A_{0}^{3} .$$
Proof. The Gauss-Bonnet-Chern formula states that (cf. [15] and Lemma 6.3)
$$8 \pi^{2} \chi(X)=\int_{X}\left(|W|^{2}+Q_{4}\right)+\oint_{M}\left(T_{3}^{3}-\frac{2}{3} \operatorname{tr} A_{0}^{3}\right) .$$
Choosing $g$ such that $Q_{4}=0$ and $H=0$ yields the result. \(\square\)

Proposition 6.5 and Proposition 6.6 state that the $\mathcal{T}$-curvature has the same properties as the fractional $Q$-curvature $Q_{3}$ on the boundary of a four-dimensional Poincaré-Einstein manifold. In light of Theorem 1.4, it is unsurprising that these curvatures are the same (cf. [16]).