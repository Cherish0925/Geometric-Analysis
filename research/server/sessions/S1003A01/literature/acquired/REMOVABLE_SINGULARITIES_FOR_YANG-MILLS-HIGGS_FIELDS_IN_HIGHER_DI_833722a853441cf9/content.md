---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2603_11926.pdf
converter: mathpix
format: mmd
---

\title{
REMOVABLE SINGULARITIES FOR YANG-MILLS-HIGGS FIELDS IN HIGHER DIMENSIONS
}

\author{
BO CHEN
}

\begin{abstract}
This paper establishes decay estimates near isolated singularities for $n$-dimensional Yang-Mills-Higgs fields defined on a fiber bundle $(n \geq 4)$. These estimates yield a removable singularity theorem for Yang-Mills-Higgs fields under conformally invariant energy bounds, extending the classical results for Yang-Mills fields and harmonic maps.
\end{abstract}

\section*{1. Introduction}

This paper is a sequel to [2], in which decay estimates were derived for three-dimensional Yang-Mills-Higgs fields under appropriate energy constraints. Here, we extend the analysis to higher dimensions and derive decay estimates near isolated singularities for $n$-dimensional Yang-Mills-Higgs fields defined on a fiber bundle, where $n \geq 4$. The curvature of the base manifold plays no essential role in the local regularity theory of Yang-Mills-Higgs fields. We therefore simplify the setting by assuming that the base manifold is flat.
1.1. Yang-Mills-Higgs fields on a ball. Let $\mathbb{R}^{n}$ denote $n$-dimensional Euclidean space, and let $B_{1} \subset \mathbb{R}^{n}$ be the unit ball. Let $(N, h)$ be a compact Riemannian manifold equipped with an effective action of a compact connected Lie group $G$ that preserves the metric $h$. Let $\mathcal{P}$ be a trivial principal $G$-bundle over $B_{1}$, and let $\mathcal{F}=\mathcal{P} \times_{G} N$ be the associated bundle with fiber $N$. After fixing a trivialization, any section of $\mathcal{F}$ can be identified with a map $u: B_{1} \rightarrow N$, while a connection $A$ on $\mathcal{P}$ can be identified with a $\mathfrak{g}$-valued 1 -form, where $\mathfrak{g}$ is the Lie algebra of $G$. For any pair $(A, u)$, the Yang-Mills-Higgs (YMH) functional is defined by
$$\mathscr{E}(A, u)=\int_{B_{1}}\left(\left|F_{A}\right|^{2}+\left|\nabla_{A} u\right|^{2}+V(u)\right) d x$$
Here $F_{A}=d A+\frac{1}{2}[A, A]$ is the curvature of the connection $A$, and $\nabla_{A}=$ $\nabla+A$ is the covariant derivative induced by $A$, where ∇ is the pullback connection on $u^{*}(T N)$. The function $V(u)$ is a gauge-invariant potential, referred to as the generalized Higgs potential on the bundle $\mathcal{F}$, and $d x$ is the volume element on $B_{1}$.

A YMH field $(A, u)$ is a critical point of the YMH functional and satisfies the following elliptic system:
$$\left\{\begin{array}{l}
D_{A}^{*} F_{A}=-u^{*} \nabla_{A} u, \\
\nabla_{A}^{*} \nabla_{A} u=-2 \nabla V(u),
\end{array}\right.$$
where $D_{A}^{*}$ is the adjoint of the exterior covariant derivative $D_{A}$. The term $u^{*} \nabla_{A} u$ lies in the dual space of $\Omega^{1}\left(B_{1}, \mathfrak{g}\right)$; namely, for every $c \in \Omega^{1}\left(B_{1}, \mathfrak{g}\right)$, we have
$$\left\langle u^{*} \nabla_{A} u, c\right\rangle=\left\langle\nabla_{A} u, c \cdot u\right\rangle,$$
where ⋅ denotes the infinitesimal action of $\mathfrak{g}$ on $N$.
1.2. Background and main results. Originating in the study of electromagnetic phenomena, YMH fields are fundamental objects in classical gauge theory and particle physics. Mathematically, the YMH field equations form an elliptic system coupling the Yang-Mills equation with the harmonic map equation. Thus, a YMH field provides a natural gauge-theoretic generalization of a harmonic map. In the setting of symplectic fibrations, minimizing YMH fields are called symplectic vortices, and their moduli spaces can be used to define invariants of symplectic manifolds with Hamiltonian actions. See [5, 6, 16] for further details.

Singularities of YMH fields have been studied extensively for several decades. Uhlenbeck [18] proved that a four-dimensional Yang-Mills field with a point singularity and finite Yang-Mills energy is gauge equivalent to a smooth connection. See also [9] for two alternative proofs of the removable singularity theorem for four-dimensional Yang-Mills fields. Parker [8] later extended Uhlenbeck's result to finite-energy Yang-Mills fields coupled to scalar and spinor fields. In dimension three and in dimensions greater than four, removable singularity theorems for both pure Yang-Mills (YM) fields and YM fields coupled to vector-bundle-valued Higgs fields have been studied in [12, 11, 13, 14, 7, 17, 15].

In general, when the fiber is a nonflat Riemannian manifold, the nonlinear term in the Higgs-field equation substantially complicates the analysis of the asymptotic behavior of YMH fields near singularities. Consequently, even isolated removable singularities are difficult to study. The theory of isolated singularities of harmonic maps [10, 3] illustrates the essential differences between YMH fields on vector bundles and those on fiber bundles with curved fibers. In previous work [1], the present author and Song established a precise decay estimate for YMH fields with point singularities on a surface, leading to a removable singularity theorem for two-dimensional YMH fields with trivial limiting holonomy. More recently, in [2], we proved removability for three-dimensional YMH fields under suitable conformally invariant energy bounds. In dimensions greater than four, however, the decay behavior of YMH fields near singular points remains unclear.

In this paper, we investigate decay estimates near isolated singularities for $n$-dimensional YMH fields satisfying the conformally invariant energy bound (1.3), where $n \geq 4$.

Throughout the paper, $C$ denotes a constant depending only on the dimension $n$ and the geometry of $N$. For $0<R \leq 1$, let $B_{R}=\left\{x \in \mathbb{R}^{n}:\right.$ $|x|<R\}$ be the ball of radius $R$, and let $B_{R}^{*}=\left\{x \in \mathbb{R}^{n}: 0<|x|<R\right\}$ be the corresponding punctured ball.

Our main results are as follows.
Theorem 1.1. There exists $\varepsilon_{0}>0$ such that if $(A, u)$ is a smooth $Y M H$ field on $B_{1}^{*} \subset \mathbb{R}^{n}$, where $n \geq 4$, satisfying
$$\sup _{B_{\rho(y)} \subset B_{R_{0}}} \frac{1}{\rho^{n-2}} \int_{B_{\rho}(y)}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|\right) d x \leq \varepsilon_{0}^{2}$$
for some $R_{0} \leq 1$, then the singularity at the origin is removable.
A direct corollary of Theorem 1.1 is as follows.
Corollary 1.2. Let $(A, u)$ be a smooth YMH field on $B_{1}^{*} \subset \mathbb{R}^{n}$, where $n \geq 4$, satisfying the conformally invariant energy bound
$$\int_{B_{1}}\left|F_{A}\right|^{\frac{n}{2}} d x+\int_{B_{1}}\left|\nabla_{A} u\right|^{n} d x<\infty .$$
Then the singularity at the origin is removable.
Theorem 1.1 is a consequence of the following result, which provides sharp decay estimates for YMH fields near isolated singularities.

Theorem 1.3. There exists $\varepsilon_{0}>0$ such that if $(A, u)$ is a smooth $Y M H$ field on $B_{R_{0}}^{*}$, where $R_{0} \leq 1$, satisfying the energy bound (1.3), then there exists $r_{0} \leq R_{0} / 2$, depending only on $\varepsilon_{0}$ and $n$, such that $\left(F_{A}, \nabla_{A} u\right)$ satisfies
$$\begin{aligned}
\sqrt{\left|F_{A}\right|^{2}(x)+1} & \leq C\left(1+\varepsilon_{0}^{2} r_{0}^{-2}\right), \\
\sqrt{\left|\nabla_{A} u\right|^{2}(x)+1} & \leq C\left(1+\varepsilon_{0} r_{0}^{-1}\right),
\end{aligned}$$
for any $0<r=|x|<r_{0}$.
Remark 1.4. Theorem 1.1 generalizes the classical removable singularity theorems for coupled Yang-Mills fields [13, 7] and harmonic maps [3], and extends the three-dimensional result for YMH fields [2].
1.3. Outline of the proof. We outline the proof of Theorem 1.3; the remaining results follow directly from it. The proof must overcome challenges arising from both the nonflatness of the fiber and the lack of conformal invariance of the Yang-Mills-Higgs field equations. When the fiber is a general compact Riemannian manifold, the YMH equations are highly nonlinear compared with those for vector-valued Higgs fields. This creates new difficulties in analyzing the asymptotic behavior of YMH fields near singularities. Our main tool for overcoming this obstacle is the extended Kato inequalities
for $n$-dimensional YMH fields ( $A, u$ ) established in [2]. These inequalities are
$$\begin{aligned}
\left|\nabla_{A} \nabla_{A} u\right|^{2} & \geq\left.\left(\frac{n}{n-1}-\delta\right)|\nabla| \nabla_{A} u\right|^{2}-C(n, \delta)\left(1+\left|F_{A}\right|^{2}\right), \\
\left|\nabla_{A} F_{A}\right|^{2} & \geq\left(\frac{n-1}{n-2}-\delta\right)|\nabla| F_{A}| |^{2}-C(n, \delta)\left|u^{*}\left(\nabla_{A} u\right)\right|^{2},
\end{aligned}$$
for any sufficiently small $\delta>0$.
More precisely, motivated by [9, 15], we combine the Bochner formulas (2.3) and (2.4) with the Kato inequalities (1.7)-(1.8) to derive differential inequalities for YMH fields $(A, u)$. We find that
$$(f, g)=\left(\left(\left|F_{A}\right|^{2}+1\right)^{\frac{\beta}{2}},\left(\left|\nabla_{A} u\right|^{2}+1\right)^{\frac{\kappa}{2}}\right)$$
satisfy the following key differential inequalities
$$\begin{aligned}
& \Delta f \geq-C(n, \delta)\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|+1\right) f, \\
& \Delta g \geq-C(n, \delta)\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|^{2}+1\right) g,
\end{aligned}$$
for every sufficiently small $\delta>0$. Here we set $\beta=\frac{n-3}{n-2}+\delta$ and $\kappa=\frac{n-2}{n-1}+\delta$. By studying decay estimates for positive solutions of (1.9) and (1.10), we establish estimates (1.5)-(1.6) for the YMH field $(A, u)$ in Theorem 1.3. We rewrite these differential inequalities in cylindrical coordinates, reducing the study of decay near a point singularity to the analysis of the asymptotic behavior at infinity of solutions to the corresponding inequalities.

In the special case in which $A$ is a four-dimensional YM field, the Kato inequality for the curvature $F_{A}$,
$$\frac{3}{2}|\nabla| F_{A}| |^{2} \leq\left|\nabla_{A} F_{A}\right|^{2},$$
implies that $F_{A}$ satisfies a key inequality with respect to the Euclidean metric $g_{\text {euc }}$ :
$$\Delta_{g_{e u c}}\left|F_{A}\right|_{g_{e u c}}^{\frac{1}{2}}-\left(K_{e u c}-C\left|F_{A}\right|_{g_{e u c}}\right)\left|F_{A}\right|_{g_{e u c}}^{\frac{1}{2}} \geq 0,$$
where $K_{e u c}$ denotes a constant depending only on the curvature of Euclidean space. Because Euclidean space is flat, $K_{e u c}=0$. In cylindrical coordinates, this inequality becomes
$$\left(\partial_{t}^{2}+\Delta_{\mathbb{S}^{3}}\right)\left|F_{A}\right|_{g_{C}}^{\frac{1}{2}}-\left(1-C\left|F_{A}\right| g_{C}\right)\left|F_{A}\right|_{g_{C}}^{\frac{1}{2}} \geq 0,$$
where $g_{C}=e^{2 t} g_{\text {euc }}$ is the canonical cylindrical metric, $t=-\log r$, and $r=|x|$. By studying inequality (1.12), Råde [9] established a sharp decay estimate for $F_{A}$.

Formulas (1.11) and (1.12) have the same structure because Yang-Mills fields in four dimensions are conformally invariant. In general, however, the YMH equations are not conformally invariant, so inequalities (1.9) and (1.10) do not retain their form in cylindrical coordinates. To overcome this difficulty, we introduce suitable weighted modifications of $f$ and $g$ so that
the resulting inequalities take refined forms analogous to (1.12) in cylindrical coordinates (see (1.14) and (1.15) below).

The proof proceeds as follows. We first establish almost $L^{\infty}$ estimates for the curvature. Because the YMH field $(A, u)$ satisfies (1.3), the $\varepsilon$-regularity theorem, Theorem 2.2, implies that
$$r^{2}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|\right) \leq C \varepsilon_{0}^{2} .$$

Next, using (1.9), we observe that the weighted function $\bar{f}=e^{-\frac{n-2}{2} t} f$ in cylindrical coordinates $(t=-\log |x|, \theta) \in\left[t_{0}=-\log r_{0},+\infty\right) \times \mathbb{S}^{n-1}$ satisfies
$$\partial_{t}^{2} \bar{f}+\Delta_{\mathbb{S}^{n-1}} \bar{f}-\alpha^{2} \bar{f} \geq 0,$$
where $\alpha$ is defined as
$$\alpha=\sqrt{\frac{(n-2)^{2}}{4}-C(n)\left(r_{0}^{2 / 3}+\varepsilon_{0}^{2}\right)} .$$
If $n \geq 4$ and $\delta, r_{0}$, and $\varepsilon_{0}$ are sufficiently small, then $2 \beta-\frac{n-2}{2}<\alpha$. Applying comparison theorems to (1.14), we obtain almost $L^{\infty}$ estimates for $F_{A}$ (see (3.2)).

With this almost $L^{\infty}$ estimate for $F_{A}$ in hand, we analyze the weighted function $\bar{g}=e^{-\frac{n-2}{2} t} g$. It follows from (1.10) that $\bar{g}$ satisfies
$$\partial_{t}^{2} \bar{g}+\Delta_{\mathbb{S}^{n-1}} \bar{g}-\alpha^{2} \bar{g} \geq-C e^{-\varrho\left(t-t_{0}\right)} \bar{g},$$
where $\varrho$ is a constant close to 2. Applying the comparison theorems to (1.15), we derive an almost $L^{\infty}$ estimate for $\left|\nabla_{A} u\right|$, namely (3.3).

Once these almost $L^{\infty}$ estimates are established, we refine them to the sharp $L^{\infty}$ estimates (1.5) and (1.6) by applying a similar analysis to the differential inequalities (1.9) and (1.10).

The remainder of the paper is organized as follows. In Section 2, we recall preliminary results for YMH fields. In Section 3, we prove Theorem 1.3. Finally, in Section 4, we prove Theorem 1.1.

\section*{2. Preliminaries}
2.1. Bundle notation and equations for YMH fields. Let $(N, h)$ be a compact Riemannian manifold equipped with an effective action of a compact connected Lie group $G$ that preserves the metric $h$. For fixed $R>0$, let $B_{R} \subset \mathbb{R}^{n}$ be the Euclidean ball of radius $R$, and let $B_{R}^{*}=B_{R} \backslash\{0\}$ be the punctured ball. Let $\mathcal{P}$ be a trivial principal $G$-bundle over $B_{R}$, and let $\mathcal{F}=\mathcal{P} \times_{G} N$ be the associated bundle. After fixing a trivialization, any section of $\mathcal{F}$ can be identified with a map $u: B_{R} \rightarrow N$, while a connection $A$ on $\mathcal{P}$ can be identified with a $\mathfrak{g}$-valued 1 -form, where $\mathfrak{g}$ is the Lie algebra of $G$.

A connection $A$ induces an extrinsic derivative $D_{A}=d+A$, and the curvature of $A$ is defined by
$$F_{A}=D_{A}^{2}=d A+\frac{1}{2}[A, A] .$$

The connection $A$ also induces a covariant derivative $\nabla_{A}=\nabla+A$ such that for any section $u: B_{R} \rightarrow N$ we have
$$\nabla_{A} u=\nabla u+A \cdot u,$$
where ⋅ denotes the infinitesimal action of $\mathfrak{g}$ on $N$.
Let $s: B_{R} \rightarrow G$ be a gauge transformation. The action of $s$ on a connection $A$, a section $u$, and the curvature $F_{A}$ of $A$ is given by the following transformation laws:
$$s^{*} A=s^{-1} d s+s^{-1} A s, s^{*} F_{A}=F_{s^{*} A}=s^{-1} F_{A} s,$$
and
$$s^{*} D_{A} u=D_{s^{*} A} s^{*} u=s^{-1} D_{A} u, V\left(s^{*} u\right)=V(u) .$$
These transformation laws imply that the YMH functional (1.1) is invariant under the gauge transformation $s$; that is,
$$\mathscr{E}(A, u)=\mathscr{E}\left(s^{*} A, s^{*} u\right) .$$
The YMH equations are therefore gauge invariant. Namely, if $(A, u)$ satisfies the system
$$\left\{\begin{array}{l}
D_{A}^{*} F_{A}=-u^{*} \nabla_{A} u, \\
\nabla_{A}^{*} \nabla_{A} u=-2 \nabla V(u),
\end{array}\right.$$
then $\left(s^{*} A, s^{*} u\right)$ also solves equation (2.1) for any gauge transformation $s$.
For the purposes of PDE analysis, we rewrite equation (2.1) in a more explicit extrinsic form. By the equivariant embedding theorem of Moore and Schlafly [4], there exist an isometric embedding $i: N \rightarrow \mathbb{R}^{K}$ and a representation $\rho: G \longrightarrow S O(K)$ such that $i(g \cdot u)=\rho(g) i(u)$ for every $u \in N$ and $g \in G$. Under this representation, the Lie algebra $\mathfrak{g}$ corresponds to a subalgebra of $\mathfrak{s} \mathfrak{o}(K)$, the space of skew-symmetric $K \times K$ matrices. Thus, for any $c \in \mathfrak{g}$ and $u \in N \hookrightarrow \mathbb{R}^{K}$, the infinitesimal action of $c$ on $u$ is
$$c \cdot u=X_{c}(u)=\rho(c) u,$$
where $X_{c}$ is the infinitesimal vector field induced by $c$, and $\rho(c) u$ denotes the usual action of the matrix $\rho(c)$ on the vector $u$. It follows that the action of $c$ on a vector field $Y \in \Gamma(T N)$ is
$$c \cdot Y=\nabla_{Y} X_{c}=(\rho(c) \cdot Y)^{\top}=\rho(c) Y-\Gamma(y)\left(X_{c}, Y\right),$$
where $\top$ denotes the projection from $\mathbb{R}^{K}$ onto the tangent space of $N$, and $\Gamma$ denotes the second fundamental form of $N$ in $\mathbb{R}^{K}$.

Using this notation, we can rewrite equation (2.1) as
$$\left\{\begin{array}{l}
d^{*} d A+A \# d A+A \# A \# A=-u^{*}\left(\nabla_{A} u\right), \\
\Delta u-d^{*} A u+2 A \# d u+A \#(A u)=\Gamma(u)\left(\nabla_{A} u, \nabla_{A} u\right)+2 \nabla V(u) .
\end{array}\right.$$
Here, for simplicity, we continue to use $A$ to denote $\rho(A)$, we set $\nabla_{A} u=$ $d u+A u$, and \# denotes a linear contraction.
2.2. Bochner formulas and $\varepsilon$-regularity theorems for YMH fields. Let $(A, u)$ be a YMH field on $B_{R} \subset \mathbb{R}^{n}$ with $n \geq 4$. We recall the Bochner formulas and the $\varepsilon$-regularity theorem obtained in our previous work [2].

Lemma 2.1. There exist constants $a$, $b$, and $c$, depending only on $n$ and the geometry of $N$, such that every YMH field $(A, u)$ defined on $B_{R}$ has the following properties:
\begin{itemize}
\item[(1)] $\left(\nabla_{A} u, F_{A}\right)$ satisfies
$$\begin{aligned}
\Delta\left|\nabla_{A} u\right|^{2} & \geq\left|\nabla_{A} \nabla_{A} u\right|^{2}-a\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|+1\right)\left|\nabla_{A} u\right|^{2}, \\
\Delta\left|F_{A}\right|^{2} & \geq\left|\nabla_{A} F_{A}\right|^{2}-b\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|^{2}\right)\left|F_{A}\right| ;
\end{aligned}$$
\item[(2)] If $f=\left|F_{A}\right|+\left|\nabla_{A} u\right|^{2}$, then
$$\Delta f \geq-c(1+f) f .$$
\end{itemize}

Theorem 2.2. There exists $\varepsilon_{0}>0$ such that for any $Y M H$ field $(A, u)$ on $B_{R}$ satisfying
$$\sup _{B_{\rho(y)} \subset B_{R}}\left(\frac{1}{\rho^{n-2}} \int_{B_{\rho}(y)}\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right| d x\right) \leq \varepsilon_{0}^{2}$$
we have
$$\sup _{B_{R / 2}} R^{2}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|\right) \leq C \varepsilon_{0}^{2}$$
for some constant $C$ depending only on $n$ and $\sup _{N}\left|R^{N}\right|$.
A direct corollary of Theorem 2.2 is as follows.
Corollary 2.3. There exists $\varepsilon_{0}>0$ such that for any YMH field $(A, u)$ on $B_{R}$ satisfying
$$\int_{B_{R}}\left|\nabla_{A} u\right|^{n}+\left|F_{A}\right|^{n / 2} d x \leq \varepsilon_{0}^{n}$$
we have
$$\sup _{B_{R / 2}} R^{2}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|\right) \leq C \varepsilon_{0}^{2}$$
for some constant $C$ depending only on $n$ and $\sup _{N}\left|R^{N}\right|$.
2.3. Improved Kato inequalities for YMH fields. We recall the Kato inequalities for YMH fields established in [2], which play a crucial role in obtaining decay estimates in the next section. Let $(A, u)$ be a smooth YMH field on $B_{R}$; that is, $(A, u)$ satisfies
$$\left\{\begin{array}{l}
D_{A}^{*} F_{A}=-u^{*}\left(\nabla_{A} u\right), \\
\nabla_{A}^{*} \nabla_{A} u=-2 \nabla V(u),
\end{array}\right.$$
where $V(u)$ is a smooth function of the section $u$. By the definition of curvature, $u$ satisfies
$$D_{A}^{*} D_{A} u=-2 \nabla V(u), \quad D_{A} D_{A} u=F_{A} \cdot u .$$

The Bianchi identity also gives
$$D_{A}^{*} F_{A}=-u^{*}\left(\nabla_{A} u\right), \quad D_{A} F_{A}=0 .$$

Thus, Propositions 3.2-3.4 of [2] yield almost sharp Kato inequalities for the YMH field $(A, u)$, as stated in the following proposition.

Proposition 2.4. For every $\delta>0$, there exists a constant $C(n, \delta)>0$ such that every YMH field $(A, u)$ on $B_{R}$ satisfies the following inequalities:
\begin{itemize}
\item[(1)] the section $u$ satisfies
$$\left|\nabla_{A} \nabla_{A} u\right|^{2} \geq\left.\left(\frac{n}{n-1}-\delta\right)|\nabla| \nabla_{A} u\right|^{2}-C(n, \delta)\left(1+\left|F_{A}\right|^{2}\right) ;$$
\item[(2)] the curvature $F_{A}$ of $A$ satisfies
$$\left|\nabla_{A} F_{A}\right|^{2} \geq\left(\frac{n-1}{n-2}-\delta\right)|\nabla| F_{A}| |^{2}-C(n, \delta)\left|u^{*}\left(\nabla_{A} u\right)\right|^{2} .$$
\end{itemize}
Moreover, if $A$ is a pure Yang-Mills field, then
$$\left|\nabla_{A} F_{A}\right|^{2} \geq \frac{n-1}{n-2}|\nabla| F_{A}| |^{2} ;$$
if $u$ is a harmonic map, then
$$\left|\nabla^{2} u\right|^{2} \geq\left.\frac{n}{n-1}|\nabla| \nabla u\right|^{2} .$$
2.4. Differential inequalities for YMH fields. Combining the Bochner formulas in Lemma 2.1 with the improved Kato inequalities in Proposition 2.4, we obtain differential inequalities for $n$-dimensional Yang-Mills-Higgs fields. These inequalities are essential to the proof of Theorem 1.3.

Proposition 2.5. For every $\delta>0$, there exists a constant $C(n, \delta)>0$ such that every YMH field $(A, u)$ on $B_{R_{0}}^{*}$ has the following properties.
\begin{itemize}
\item[(1)] For $p \geq \frac{n-3}{n-2}+\delta$, the function $f=\sqrt{\left|F_{A}\right|^{2}+1}$ satisfies
$$\Delta f^{p} \geq-C(n, \delta)\left(\left|\nabla_{A} u\right|^{2}+f\right) f^{p} .$$
\item[(2)] For $p \geq \frac{n-2}{n-1}+\delta$, the function $f=\sqrt{\left|\nabla_{A} u\right|^{2}+1}$ satisfies
$$\Delta f^{p} \geq-C(n, \delta)\left(\left|F_{A}\right|^{2}+f^{2}\right) f^{p} .$$
\end{itemize}
Proof. For any smooth positive function $f$, a direct calculation gives
$$\Delta f^{p}=p f^{p-2}\left(\frac{1}{2} \Delta f^{2}+\frac{p-2}{4} \frac{\left|\nabla f^{2}\right|^{2}}{f^{2}}\right) .$$

Taking $f=\sqrt{\left|F_{A}\right|^{2}+1}$ in (2.13), with $p>0$, gives
$$\begin{aligned}
\Delta f^{p} & =p f^{p-2}\left(\frac{1}{2} \Delta\left|F_{A}\right|^{2}+\frac{p-2}{4} \frac{\left.\left.|\nabla| F_{A}\right|^{2}\right|^{2}}{f^{2}}\right) \\
& =p f^{p-2}\left(\frac{1}{2} \Delta\left|F_{A}\right|^{2}+(p-2)|\nabla| F_{A} \|^{2} \frac{\left|F_{A}\right|^{2}}{f^{2}}\right) .
\end{aligned}$$

Applying the Bochner formula (2.4) from Lemma 2.1 and the Kato inequality (2.8) for $F_{A}$ from Proposition 2.4, we obtain
$$\begin{aligned}
\frac{1}{2} \Delta\left|F_{A}\right|^{2} & \geq\left|\nabla_{A} F_{A}\right|^{2}-C\left|F_{A}\right|\left|\nabla_{A} u\right|^{2}-C\left(1+\left|F_{A}\right|\right)\left|F_{A}\right|^{2}, \\
& \geq\left(\frac{n-1}{n-2}-\delta\right)|\nabla| F_{A}| |^{2}-C(n, \delta)\left(1+\left|F_{A}\right|\right)\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|^{2}\right) .
\end{aligned}$$
This immediately yields
$$\begin{aligned}
\Delta f^{p}= & p f^{p-2}\left(\frac{1}{2} \Delta\left|F_{A}\right|^{2}+(p-2)|\nabla| F_{A}| |^{2} \frac{\left|F_{A}\right|^{2}}{f^{2}}\right) \\
\geq & \left.p f^{p-2}\left(\frac{n-1}{n-2}-\delta+(p-2)\right)|\nabla| F_{A}\right|^{2} \frac{\left|F_{A}\right|^{2}}{f^{2}} \\
& -C(n, \delta) f^{p-1}\left(\left|\nabla_{A} u\right|^{2}+f^{2}\right),
\end{aligned}$$
where we used the assumption $p \geq 2+\delta-\frac{n-1}{n-2}$. Since $f^{-1} \leq 1$, it follows that
$$\Delta f^{p} \geq-C(n, \delta)\left(\left|\nabla_{A} u\right|^{2}+f\right) f^{p} .$$

Similarly, taking $f=\sqrt{\left|\nabla_{A} u\right|^{2}+1}$ in (2.13), with $p>0$, gives
$$\Delta f^{p}=p f^{p-2}\left(\frac{1}{2} \Delta\left|\nabla_{A} u\right|^{2}+\left.(p-2)|\nabla| \nabla_{A} u\right|^{2} \frac{\left|\nabla_{A} u\right|^{2}}{f^{2}}\right) .$$
Applying the Bochner formula (2.3) from Lemma 2.1 and the Kato inequality (2.7) for $\nabla_{A} u$ from Proposition 2.4, we obtain
$$\begin{aligned}
\frac{1}{2} \Delta\left|\nabla_{A} u\right|^{2} & \geq\left|\nabla_{A} \nabla_{A} u\right|^{2}+\left|u^{*}\left(\nabla_{A} u\right)\right|^{2}-C\left(1+\left|F_{A}\right|+\left|\nabla_{A} u\right|^{2}\right)\left|\nabla_{A} u\right|^{2} \\
& \geq\left.\left(\frac{n}{n-1}-\delta\right)|\nabla| \nabla_{A} u\right|^{2}-C\left(\left|F_{A}\right|^{2}+f^{2}\right) f^{2} .
\end{aligned}$$
Consequently, for $p \geq 2+\delta-\frac{n}{n-1}$, we have
$$\Delta f^{p} \geq-C(n, \delta)\left(\left|F_{A}\right|^{2}+f^{2}\right) f^{p} .$$

This completes the proof. \(\square\)

For later use, we rewrite differential inequalities (2.11) and (2.12) in cylindrical coordinates. The conformal transformation from $B_{R_{0}}^{*}$ to the cylinder $\mathscr{C}=\left[-\log R_{0},+\infty\right) \times \mathbb{S}^{n-1}$ is given by
$$\phi: B_{R_{0}}^{*} \rightarrow \mathscr{C}, \quad(r, \theta) \rightarrow(t=-\log r, \theta),$$
where the cylinder $\mathscr{C}$ is equipped with the canonical metric $g=d t^{2}+g_{\mathbb{S}^{n-1}}$. For simplicity, we denote the Laplace operator on $\mathbb{S}^{n-1}$ by $\Delta_{\mathbb{S}^{n-1}}$.

Proposition 2.6. For every $\delta>0$, there exists a constant $C(n, \delta)>0$ such that, for every YMH field $(A, u)$ on $B_{R_{0}}^{*}$, the functions
$$(g, \eta)=\left(\left(1+\left|F_{A}\right|^{2}\right)^{\frac{\beta}{2}},\left(1+\left|\nabla_{A} u\right|^{2}\right)^{\frac{\kappa}{2}}\right)$$
satisfy
$$\begin{aligned}
& \partial_{t}^{2} g-(n-2) \partial_{t} g+\Delta_{\mathbb{S}^{n-1}} g \geq-C(n, \delta) e^{-2 t}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|+1\right) g, \\
& \partial_{t}^{2} \eta-(n-2) \partial_{t} \eta+\Delta_{\mathbb{S}^{n-1}} \eta \geq-C(n, \delta) e^{-2 t}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|^{2}+1\right) \eta,
\end{aligned}$$
where $\beta=\frac{n-3}{n-2}+\delta$ and $\kappa=\frac{n-2}{n-1}+\delta$.
Proof. Inequalities (2.14) and (2.15) are precisely the cylindrical-coordinate forms of (2.11), with $p=\beta$, and (2.12), with $p=\kappa$, respectively. \(\square\)

\section*{3. Decay estimates for YMH fields in higher dimensions}

In this section, we prove Theorem 1.3. We begin with a comparison theorem used to obtain decay estimates for $n$-dimensional YMH fields under the energy bound (1.3).

Lemma 3.1. Let $\bar{g}$ be a smooth solution to the following differential inequality
$$\partial_{t}^{2} \bar{g}+\Delta_{\mathbb{S}^{n-1}} \bar{g}-\alpha^{2} \bar{g} \geq 0$$
on $\left[T_{0}, \infty\right) \times \mathbb{S}^{n-1}$, where $\alpha>0$. Suppose that $\bar{g}$ satisfies the upper bound
$$\bar{g} \leq c_{1} e^{-\lambda_{1} t}+c_{2} e^{\lambda_{2} t}$$
for any $(t, \theta) \in\left[T_{0}, \infty\right) \times \mathbb{S}^{n-1}$, where $\lambda_{1} \geq 0$ and $0 \leq \lambda_{2}<\alpha$. Then for any $(t, \theta) \in\left[T_{0}, \infty\right) \times \mathbb{S}^{n-1}$, we have
$$\bar{g}(t, \theta) \leq\left(c_{1} e^{-\lambda_{1} T_{0}}+c_{2} e^{\lambda_{2} T_{0}}\right) e^{-\alpha\left(t-T_{0}\right)} .$$
Proof. For $T>T_{0}$, consider the comparison function
$$h(t)=\left(c_{1} e^{-\lambda_{1} T_{0}}+c_{2} e^{\lambda_{2} T_{0}}\right) e^{-\alpha\left(t-T_{0}\right)}+\left(c_{1} e^{-\lambda_{1} T}+c_{2} e^{\lambda_{2} T}\right) e^{-\alpha(T-t)},$$
which satisfies the equation
$$\partial_{t}^{2} h+\Delta_{\mathbb{S}^{n-1}} h-\alpha^{2} h=0$$
and the boundary conditions
$$\bar{g}\left(T_{0}\right) \leq h\left(T_{0}\right), \quad \bar{g}(T) \leq h(T) .$$

Therefore, the comparison principle gives
$$\bar{g}(t, \theta) \leq h(t)$$
on $\left[T_{0}, T\right] \times \mathbb{S}^{n-1}$. Letting $T \rightarrow+\infty$ and using $\alpha>\lambda_{2}$, we obtain
$$\bar{g}(t, \theta) \leq\left(c_{1} e^{-\lambda_{1} T_{0}}+c_{2} e^{\lambda_{2} T_{0}}\right) e^{-\alpha\left(t-T_{0}\right)}$$
for any $(t, \theta) \in\left[T_{0}, \infty\right) \times \mathbb{S}^{n-1}$.
This completes the proof. \(\square\)

Next, we establish almost $L^{\infty}$ estimates for YMH fields satisfying the energy bound (3.1).

Theorem 3.2. There exists $\varepsilon_{0}>0$ such that if $(A, u)$ is a smooth $Y M H$ field defined on $B_{R_{0}}^{*}$, where $R_{0} \leq 1$, satisfying
$$\sup _{B_{\rho(y)} \subset B_{R_{0}}}\left(\frac{1}{\rho^{n-2}} \int_{B_{\rho}(y)}\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right| d x\right) \leq \varepsilon_{0}^{2}$$
then there exists an $r_{0} \leq R_{0} / 2$ such that $(A, u)$ satisfies the following decay estimates
$$\begin{aligned}
\left(1+\left|F_{A}\right|^{2}\right)^{\frac{\beta}{2}}(r, \theta) & \leq C\left(1+\varepsilon_{0}^{2 \beta} r_{0}^{-2 \beta}\right)\left(\frac{r}{r_{0}}\right)^{\left(\alpha-\frac{n-2}{2}\right)}, \\
\left(1+\left|\nabla_{A} u\right|^{2}\right)^{\kappa / 2}(r, \theta) & \leq C\left(1+\varepsilon_{0}^{\kappa} r_{0}^{-\kappa}\right)\left(\frac{r}{r_{0}}\right)^{\left(\alpha-\frac{n-2}{2}\right)},
\end{aligned}$$
for any $0<r<r_{0}$, where we denote
$$\alpha=\sqrt{\frac{(n-2)^{2}}{4}-C\left(\varepsilon_{0}^{2}+r_{0}^{2 / 3}\right)},$$
$\beta=1-\frac{1}{2(n-2)}$ and $\kappa=1-\frac{1}{2(n-1)}$.
Proof. The proof is divided into two steps.
Step 1: Decay estimate for $F_{A}$.
By the energy bound (3.1), for any $x \in B_{2 R_{0} / 3}^{*}$ and $r=|x|$ we have
$$\sup _{B_{\rho}(y) \subset B_{r / 2}(x)}\left(\frac{1}{\rho^{n-2}} \int_{B_{\rho}(y)}\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right| d x\right) \leq \varepsilon_{0}^{2}$$
The $\varepsilon$-regularity theorem, Theorem 2.2, then yields
$$r^{2}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|\right)(r, \theta) \leq C \varepsilon_{0}^{2}$$
for any $0<r=|x| \leq R_{0} / 2$.
We now work in cylindrical coordinates, where $t=-\log r$ and
$$(t, \theta) \in\left[-\log \left(R_{0} / 2\right),+\infty\right) \times \mathbb{S}^{n-1} .$$
In these coordinates, estimate (3.4) becomes
$$e^{-2 t}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|\right)(t, \theta) \leq C \varepsilon_{0}^{2} .$$
It follows from inequality (2.14) in Proposition 2.6 that the function $g=$ $\left(1+\left|F_{A}\right|^{2}\right)^{\frac{\beta}{2}}$, where $\beta=\frac{n-3}{n-2}+\delta$, satisfies
$$\partial_{t}^{2} g-(n-2) \partial_{t} g+\Delta_{\mathbb{S}^{n-1}} g \geq-C(n, \delta)\left(e^{-2 t}+\varepsilon_{0}^{2}\right) g$$
on $\left[-\log \left(R_{0} / 2\right),+\infty\right) \times \mathbb{S}^{n-1}$. Hence, the weighted function $\bar{g}(t, \theta)=e^{-\frac{n-2}{2} t} g$ satisfies
$$\partial_{t}^{2} \bar{g}+\Delta_{\mathbb{S}^{n-1}} \bar{g}-\left(\frac{(n-2)^{2}}{4}-C\left(\varepsilon_{0}^{2}+e^{-2 t}\right)\right) \bar{g} \geq 0 .$$

Fix $\delta=\frac{1}{2(n-2)}$ and choose $t_{0}>-\log R_{0}$ such that
$$\begin{aligned}
\alpha & =\sqrt{\frac{(n-2)^{2}}{4}-C\left(e^{-2 t_{0}}+\varepsilon_{0}^{2}\right)} \\
& >2 \beta-\frac{n-2}{2}=2-\frac{1}{n-2}-\frac{n-2}{2}
\end{aligned}$$
for $n \geq 4$. Then, for $t>t_{0}$, we have
$$\partial_{t}^{2} \bar{g}+\Delta_{\mathbb{S}^{n-1}} \bar{g}-\alpha^{2} \bar{g} \geq 0,$$
Moreover, estimate (3.5) gives
$$\bar{g}(t, \theta) \leq C\left(e^{-\frac{n-2}{2} t}+\varepsilon_{0}^{2 \beta} e^{\left(2 \beta-\frac{n-2}{2}\right) t}\right)$$
for any $(t, \theta) \in\left[t_{0}, \infty\right) \times \mathbb{S}^{n-1}$.
For any $m \in \mathbb{N}^{+}$, applying Lemma 3.1 with $T_{0}=m t_{0}$ to differential inequality (3.7) gives
$$\bar{g}(t, \theta) \leq C\left(e^{-\frac{n-2}{2} m t_{0}}+\varepsilon_{0}^{2 \beta} e^{\left(2 \beta-\frac{n-2}{2}\right) m t_{0}}\right) e^{-\alpha\left(t-m t_{0}\right)} .$$
Equivalently,
$$\left(1+\left|F_{A}\right|^{2}\right)^{\frac{\beta}{2}}(t, \theta) \leq C\left(1+\varepsilon_{0}^{2 \beta} e^{2 \beta m t_{0}}\right) e^{-\left(\alpha-\frac{n-2}{2}\right)\left(t-m t_{0}\right)} .$$
for any $(t, \theta) \in\left[m t_{0}, \infty\right) \times \mathbb{S}^{n-1}$.
Taking $r_{0}=e^{-3 t_{0}}$ and expressing estimate (3.8) in polar coordinates yields the desired decay estimate for $F_{A}$.

Step 2: Decay estimate for $\nabla_{A} u$.
Taking $\delta=\frac{1}{2(n-1)}$ in inequality (2.15), we find that the function $\eta=$ $\left(1+\left|\nabla_{A} u\right|^{2}\right)^{\frac{\kappa}{2}}$ satisfies
$$\begin{aligned}
& \partial_{t}^{2} \eta-(n-2) \partial_{t} \eta+\Delta_{\mathbb{S}^{n-1}} \eta \\
\geq & -C e^{-2 t}\left(\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right|^{2}+1\right) \eta,
\end{aligned}$$
where $\kappa=\frac{n-2}{(n-1)}+\delta=1-\frac{1}{2(n-1)}$.
By estimates (3.5) and (3.8), on $\left[t_{0}, \infty\right) \times \mathbb{S}^{n-1}$ we have
$$\begin{aligned}
e^{-2 t}\left|\nabla_{A} u\right|^{2} & \leq C \varepsilon_{0}^{2}, \\
e^{-2 t}\left|F_{A}\right|^{2} & \leq C \Lambda\left(\varepsilon_{0}\right) e^{-\varrho\left(t-t_{0}\right)},
\end{aligned}$$
where $\Lambda\left(\varepsilon_{0}\right)=\left(e^{-2 t_{0}}+2 \varepsilon_{0}^{2}+\varepsilon_{0}^{4} e^{2 t_{0}}\right)$ and $\varrho=2+\frac{2}{\beta}\left(\alpha-\frac{n-2}{2}\right) \geq 1+\kappa$.
Using estimates (3.10) and (3.11) in inequality (3.9), we find that the weighted function $\bar{\eta}=e^{-\frac{n-2}{2} t} \eta$ satisfies
$$\partial_{t}^{2} \bar{\eta}+\Delta_{\mathbb{S}^{n-1}} \bar{\eta}-\alpha^{2} \bar{\eta} \geq-C \Lambda\left(\varepsilon_{0}\right) e^{-\varrho\left(t-t_{0}\right)} \bar{\eta}$$
on $\left[t_{0}, \infty\right) \times \mathbb{S}^{n-1}$. Moreover, estimate (3.10) implies that
$$\bar{\eta} \leq C\left(e^{-\frac{n-2}{2} t}+\varepsilon_{0}^{\kappa} e^{\left(\kappa-\frac{n-2}{2}\right) t}\right)$$
for every $(t, \theta) \in\left[t_{0}, \infty\right) \times \mathbb{S}^{n-1}$. Thus, the right-hand side of inequality (3.12) can be estimated as follows:
$$Q=-C \Lambda\left(\varepsilon_{0}\right) e^{-\varrho\left(t-t_{0}\right)} \bar{\eta} \geq-\tilde{\eta}$$
where
$$\begin{aligned}
\tilde{\eta} & =C \Lambda\left(\varepsilon_{0}\right) e^{-\varrho\left(t-t_{0}\right)}\left(e^{-\frac{n-2}{2} t}+\varepsilon_{0}^{\kappa} e^{\left(\kappa-\frac{n-2}{2}\right) t}\right) \\
& \leq C\left(e^{-\frac{n-2}{2} t}+\varepsilon_{0}^{\kappa} e^{\left(\kappa-\frac{n-2}{2}\right) t}\right)
\end{aligned}$$
for $t \geq\left(\frac{2}{\varrho}+1\right) t_{0}$.
For $T>3 t_{0}$, consider the function
$$\begin{aligned}
h(t)= & 2 C\left(e^{-\frac{n-2}{2} 3 t_{0}}+\varepsilon_{0}^{\kappa} e^{\left(\kappa-\frac{n-2}{2}\right) 3 t_{0}}\right) e^{-\alpha\left(t-3 t_{0}\right)} \\
& +2 C\left(e^{-\frac{n-2}{2} T}+\varepsilon_{0}^{\kappa} e^{\left(\kappa-\frac{n-2}{2}\right) T}\right) e^{-\alpha(T-t)}-\tilde{\eta}
\end{aligned}$$
as a comparison function for the differential inequality
$$\partial_{t}^{2} \bar{\eta}+\Delta_{\mathbb{S}^{n-1}} \bar{\eta}-\alpha^{2} \bar{\eta} \geq-\tilde{\eta} .$$

A direct calculation shows that
$$\left(\partial_{t}^{2}+\Delta_{\mathbb{S}^{n-1}}-\alpha^{2}\right) h \leq-\left(\left(\varrho+\frac{n-2}{2}-\kappa\right)^{2}-\alpha^{2}\right) \tilde{\eta} \leq-\tilde{\eta},$$
which implies
$$\left(\partial_{t}^{2}+\Delta_{\mathbb{S}^{n-1}}-\alpha^{2}\right)(h-\bar{\eta}) \leq 0$$
on $\left[3 t_{0}, T\right] \times \mathbb{S}^{n-1}$. By estimate (3.13), the function $h$ also satisfies the boundary conditions $h\left(3 t_{0}\right) \geq \bar{\eta}\left(3 t_{0}, \theta\right)$ and $h(T) \geq \bar{\eta}(T, \theta)$. Consequently, the comparison principle gives
$$\bar{\eta}(t, \theta) \leq h(t)$$
for $(t, \theta) \in\left[3 t_{0}, T\right] \times \mathbb{S}^{n-1}$. Letting $T \rightarrow+\infty$ yields the desired estimate for $\nabla_{A} u$.

This completes the proof. \(\square\)

Using the almost $L^{\infty}$ estimates established in Theorem 3.2, we now prove Theorem 1.3, which we restate in the following form.

Theorem 3.3. There exists $\varepsilon_{0}>0$ such that if $(A, u)$ is a smooth $Y M H$ field defined on $B_{R_{0}}^{*}$, where $R_{0} \leq 1$, satisfying the energy bound (3.1), then there exists $r_{0} \leq R_{0} / 2$ such that $(A, u)$ satisfies the following $L^{\infty}$ estimates:
$$\begin{aligned}
\left(1+\left|F_{A}\right|^{2}\right)^{\frac{1}{2}}(r, \theta) & \leq C\left(1+\varepsilon_{0}^{2} r_{0}^{-2}\right) \\
\left(1+\left|\nabla_{A} u\right|^{2}\right)^{\frac{1}{2}}(r, \theta) & \leq C\left(1+\varepsilon_{0} r_{0}^{-1}\right)
\end{aligned}$$
for all $0<r<r_{0}$.

Proof. By estimates (3.2) and (3.3), together with inequality (2.14), we infer that the function $g=\left(1+\left|F_{A}\right|^{2}\right)^{\frac{\beta}{2}}$, where $\beta=\frac{n-3}{n-2}+\frac{1}{2(n-2)}$, satisfies
$$\partial_{t}^{2} g-(n-2) \partial_{t} g+\Delta_{\mathbb{S}^{n-1}} g \geq-C L\left(\varepsilon_{0}, t_{0}\right) e^{-\left(2+3\left(\alpha-\frac{n-2}{2}\right)\right) t},$$
on $\mathbb{S}^{n-1} \times\left[3 t_{0}, \infty\right)$, where $L\left(\varepsilon_{0}, t_{0}\right)=1+\varepsilon_{0}^{2} e^{-3 t_{0}}$.
Consequently, the function $\bar{g}(t, \theta)=e^{-\frac{n-2}{2} t} g$ satisfies
$$\partial_{t}^{2} \bar{g}+\Delta_{\mathbb{S}^{n-1}} \bar{g}-\frac{(n-2)^{2}}{4} \bar{g} \geq-C L\left(\varepsilon_{0}, t_{0}\right) e^{-\left(\frac{(n-2)}{2}+2+3\left(\alpha-\frac{n-2}{2}\right)\right) t} .$$

Next, we consider the comparison function
$$\begin{aligned}
g_{1}(t)= & 2 C\left(e^{-\frac{n-2}{2} 3 t_{0}}+\varepsilon_{0}^{2 \beta} e^{\left(2 \beta-\frac{n-2}{2}\right) 3 t_{0}}\right) e^{-\frac{n-2}{2}\left(t-3 t_{0}\right)} \\
& +2 C\left(e^{-\frac{n-2}{2} 3 t_{0}}+\varepsilon_{0}^{2 \beta} e^{\left(2 \beta-\frac{n-2}{2}\right) 3 t_{0}}\right) e^{-\alpha\left(T-3 t_{0}\right)} e^{-\frac{n-2}{2}(T-t)} \\
& -C L\left(\varepsilon_{0}, t_{0}\right) e^{-\left(\frac{(n-2)}{2}+2+3\left(\alpha-\frac{n-2}{2}\right)\right) t} .
\end{aligned}$$
For a suitable choice of $t_{0}$, a direct computation yields
$$\left(\partial_{t}^{2}+\Delta_{\mathbb{S}^{n-1}}-\frac{(n-2)^{2}}{4}\right)\left(\bar{g}-g_{1}\right) \geq 0$$
on $\mathbb{S}^{n-1} \times\left[3 t_{0}, T\right]$, together with the boundary conditions
$$\bar{g}\left(3 t_{0}\right) \leq g_{1}, \quad \bar{g}(T) \leq g_{1}(T) .$$
Therefore, by the comparison principle, we obtain
$$\bar{g}(t, \theta) \leq g_{1}(t)$$
for $3 t_{0} \leq t \leq T$.
Since $\alpha<\frac{n-2}{2}$, letting $T \rightarrow+\infty$ yields
$$\bar{g}(t, \theta) \leq 2 C\left(e^{-\frac{n-2}{2} 3 t_{0}}+\varepsilon_{0}^{2 \beta} e^{\left(2 \beta-\frac{n-2}{2}\right) 3 t_{0}}\right) e^{-\frac{n-2}{2}\left(t-3 t_{0}\right)}$$
for every $t \geq 3 t_{0}$. Transforming back to polar coordinates gives the desired estimate (3.14).

Finally, applying the same argument to the function $\eta=\left(1+\left|\nabla_{A} u\right|^{2}\right)^{\frac{\kappa}{2}}$, with $\kappa=1-\frac{1}{2(n-1)}$, establishes the $L^{\infty}$ estimate (3.15) for $\left|\nabla_{A} u\right|$. \(\square\)

\section*{4. Removable singularities for YMH fields in higher dimensions}

In this section, we use the decay estimates (3.14) and (3.15) from Section 3 to prove the removable singularity theorem, Theorem 1.1. We first recall the local existence of a Coulomb gauge established by Smith and Uhlenbeck [15].

Proposition 4.1. Let $B_{1}$ be the unit ball in $\mathbb{R}^{n}$, where $n \geq 3$, and let $\mathcal{S} \subset B_{1}$ be a closed set of finite ( $n-3$ )-dimensional Hausdorff measure. There exists $\varepsilon>0$ such that, for any connection $A$ smooth on $B_{1} \backslash \mathcal{S}$ whose curvature $F_{A}$ satisfies
$$\int_{B_{1}}\left|F_{A}\right|^{p} d \mu \leq \varepsilon^{p}$$
for some $p>n$, there exists a continuous gauge transformation $s$ such that $\bar{A}=s^{*} A \in W_{\text {loc }}^{1, p}\left(B_{1}\right)$ and $\bar{A}$ has the following properties:
\begin{itemize}
\item[(1)] In $B_{1}, \bar{A}$ solves
$$d^{*} \bar{A}=0,$$
\item[(2)] There exists a constant $C$, depending only on $n$ and $p$, such that
$$\|\bar{A}\|_{W^{1, p}\left(B_{1 / 2}\right)} \leq C\left\|F_{\bar{A}}\right\|_{L^{p}} \leq C \varepsilon .$$
\end{itemize}

We now use Proposition 4.1 to prove Theorem 1.1 .
Proof of Theorem 1.1. The proof is divided into two steps.
Step 1: In a local Coulomb gauge, the YMH field $(A, u)$ is smooth near the origin.

Applying decay estimate (1.5) from Theorem 1.3, with both $\varepsilon_{0}$ and $r_{0}$ sufficiently small, gives
$$\int_{B_{r_{0}}}\left|F_{A}\right|^{p} d x \leq \varepsilon^{p} r_{0}^{-2 p+n}$$
for $p>2 n$, where $\varepsilon$ is the constant in Proposition 4.1. Setting $\tilde{A}(x)=$ $r_{0} A\left(r_{0} x\right)$, we obtain
$$\int_{B_{1}}\left|F_{\tilde{A}}\right|^{p} d x \leq \varepsilon^{p} .$$
Proposition 4.1 then provides a gauge $s$ on $B_{1}$ in which (4.1) and (4.2) hold. After rescaling, these estimates become
$$d^{*} A_{1}=0 \quad \text { in } B_{r_{0}}$$
and
$$\left\|A_{1}\right\|_{W^{1, p}\left(B_{r_{0} / 2}\right)} \leq C\left(r_{0}, p\right) \varepsilon .$$
Here $A_{1}=s^{*} A=s^{-1} d s+s^{-1} A s$.
Moreover, decay estimate (1.6) for $\nabla_{A} u$ from Theorem 1.3 implies that
$$\left\|u_{1}\right\|_{W^{1, \infty}\left(B_{r_{0} / 2}\right)} \leq C\left(r_{0}\right),$$
where we set $u_{1}=s^{*} u$.
Under the gauge transformation $s$, the YMH field $\left(A_{1}, u_{1}\right)$ satisfies the extrinsic equation (2.2) on $B_{r_{0}}$ :
$$\left\{\begin{array}{l}
\Delta A_{1}+A_{1} \# d A_{1}+A_{1} \# A_{1} \# A_{1}=-u_{1}^{*}\left(\nabla_{A_{1}} u_{1}\right) \\
\Delta u_{1}+2 A_{1} \# d u_{1}+A_{1}\left(A_{1} u_{1}\right)=\Gamma\left(u_{1}\right)\left(\nabla_{A_{1}} u_{1}, \nabla_{A_{1}} u_{1}\right)+2 \nabla V\left(u_{1}\right) .
\end{array}\right.$$
where $\Gamma\left(u_{1}\right)$ is the second fundamental form of $N$ in $\mathbb{R}^{K}$. Estimates (4.4)-(4.5) imply that
$$\left(\Delta A_{1}, \Delta u_{1}\right) \in L_{l o c}^{\frac{p}{2}}\left(B_{r_{0} / 2}\right),$$
and the $L^{p}$ estimates for elliptic equations imply that
$$\left(A_{1}, u_{1}\right) \in W_{l o c}^{2, \frac{p}{2}}\left(B_{\rho_{0}}\right) \hookrightarrow C_{l o c}^{1,1-\frac{2 n}{p}}\left(B_{r_{0} / 2}\right) .$$

A standard bootstrap argument applied to this $C^{1,1-\frac{2 n}{p}}$ estimate yields $\left(A_{1}, u_{1}\right) \in C^{\infty}\left(B_{r_{0} / 2}\right)$.
Step 2: A gluing argument produces a global continuous gauge on $B_{1}$ in which the YMH field $(A, u)$ is smooth.

Without loss of generality, assume that the connection $A$ has bounded $L^{p}$ norm on $B_{r_{0} / 2}$, where $p>n$. Indeed, a radial gauge over $B_{1}^{*}$ is obtained by parallel transport along each ray $\gamma_{\theta}:=\{(r, \theta): 0<r<1\}$ in $B_{1}^{*}$. In this gauge, $A=A_{\theta} d \theta$, and hence $r|A|=\left|A_{\theta}\right|$, which implies
$$r|A|(r, \theta) \leq \int_{0}^{r} t\left|F_{A}\right|(t, \theta) d t .$$
Applying Hölder's inequality and estimate (4.3), with $p>n$, gives (see also [15])
$$\|A\|_{L^{p}\left(B_{r_{0} / 2}\right)} \leq C r_{0}\left\|F_{A}\right\|_{L^{p}\left(B_{r_{0}}\right)} \leq C\left(r_{0}\right) \varepsilon .$$

Since $A_{1}$ and $A$ are smooth on $B_{r_{0} / 2}^{*}$, it follows from
$$d s=s A_{1}-A s$$
that $s$ is smooth on $B_{r_{0} / 2}^{*}$.
Let $\rho \leq r_{0} / 4$ be a positive constant to be determined. For $q \in B_{\rho}^{*}$, replacing $s$ with $s^{-1}(q) s$ allows us to assume that $s(q)=\mathrm{id}$. Using estimates (4.4) and (4.6), with $p>n$, in equation (4.7), we obtain
$$\sup _{y \in B_{\rho}^{*}}|s(y)-\mathrm{id}| \leq C\left(r_{0}\right) \rho^{1-\frac{n}{p}}\|d s\|_{L^{p}\left(B_{r_{0} / 2}^{*}\right)}^{*} \leq C\left(r_{0}\right) \varepsilon \rho^{1-\frac{n}{p}} .$$
Thus, by choosing $\rho$ small enough, we can rewrite $s=\exp \xi(x)$ on $B_{\rho}^{*}$, where $\xi: B_{\rho}^{*} \rightarrow \mathfrak{g}$ is a smooth function such that $\xi(q)=0$.

Let $\eta \in C_{0}^{\infty}\left(B_{1}\right)$ be a smooth cutoff function such that $\eta(x)=1$ for $r \leq \frac{1}{4} \rho$ and $\eta(x)=0$ for $r \geq \frac{1}{2} \rho$. Define a global gauge on $B_{1}^{*}$ by
$$\tilde{s}(x)= \begin{cases}s & 0<r \leq \frac{\rho}{4}, \\ \exp (\eta(x) \xi(x)) & \frac{\rho}{4} \leq r \leq \frac{\rho}{2}, \\ \operatorname{id} & \frac{\rho}{2} \leq r<1 .\end{cases}$$
It follows that the YMH field ( $\tilde{s}^{*} A, \tilde{s}^{*} u$ ) is smooth on $B_{1}$.
Thus, the singularity of the YMH field $(A, u)$ is removable, and the bundle extends over the ball $B_{1}$. \(\square\)

Finally, we prove Corollary 1.2.
Proof. By Theorem 1.1, it suffices to show that for every $\varepsilon_{0}>0$, there exists $R_{0} \leq 1$ such that
$$\sup _{B_{\rho(y)} \subset B_{R_{0}}}\left(\frac{1}{\rho^{n-2}} \int_{B_{\rho}(y)}\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right| d x\right) \leq \varepsilon_{0}^{2}$$
which is precisely the energy bound (1.3).
For any $B_{\rho}(x) \subset B_{1}$, we have
$$\frac{1}{\rho^{n-2}} \int_{B_{\rho}(x)}\left|\nabla_{A} u\right|^{2}+\left|F_{A}\right| d x \leq C\left(\int_{B_{\rho}}\left|F_{A}\right|^{\frac{n}{2}} d x+\int_{B_{\rho}}\left|\nabla_{A} u\right|^{n} d x\right)^{\frac{2}{n}}$$
where $C>0$ depends only on $n$.
By (1.4), there exists $0<R_{0} \leq 1$ such that
$$\int_{B_{R_{0}}}\left|F_{A}\right|^{\frac{n}{2}} d x+\int_{B_{R_{0}}}\left|\nabla_{A} u\right|^{n} d x \leq \frac{1}{C^{\frac{n}{2}}} \varepsilon_{0}^{n} .$$
Combining (4.8) and (4.9) yields the desired energy bound (1.3).
The conclusion now follows from Theorem 1.1. \(\square\)

Acknowledgments: B. Chen is partially supported by the National Natural Science Foundation of China (Grant No. 12301074) and the Guangzhou Basic and Applied Basic Research Foundation (Grant No. 2024A04J3637).

\section*{Statements and declarations}

Conflict of interest: The author declares no conflict of interest.
Data availability: Data sharing is not applicable to this article because no datasets were generated or analyzed during the study.

\section*{References}
\begin{itemize}
\item[] [1] B. Chen and C. Song, Isolated singularities of Yang-Mills-Higgs fields on surfaces, Int. Math. Res. Not. IMRN 2021 (2021), no. 1, 551-581.
\item[] [2] B. Chen and C. Song, Isolated singularities of Yang-Mills-Higgs fields on 3-dimensional manifolds, Sci. China Math., to appear (2026), arXiv:2406.16276.
\item[] [3] G. J. Liao, A regularity theorem for harmonic maps with small energy, J. Differential Geom. 22 (1985), no. 2, 233-241.
\item[] [4] J. Moore and R. Schlafly, On equivariant isometric embeddings, Math. Z. 173 (1980), 119-133.
\item[] [5] I. Mundet i Riera, Yang-Mills-Higgs theory for symplectic fibrations, Ph.D. dissertation, University of Madrid, 1999.
\item[] [6] I. Mundet i Riera and G. Tian, A compactification of the moduli space of twisted holomorphic maps, Adv. Math. 222 (2009), no. 4, 1117-1196.
\item[] [7] T. H. Otway and L. M. Sibner, Point singularities of coupled gauge fields with low energy, Comm. Math. Phys. 111 (1987), no. 2, 275-279.
\item[] [8] T. Parker, Gauge theories on four-dimensional manifolds, Comm. Math. Phys. 85 (1982), 563-602.
\end{itemize}
\begin{itemize}
\item[] [9] J. Råde, Decay estimates for Yang-Mills fields: two new proofs, in Global Analysis in Modern Mathematics (Orono, ME, 1991; Waltham, MA, 1992), 91-105, Publish or Perish, Houston, TX, 1993.
\item[] [10] J. Sacks and K. Uhlenbeck, The existence of minimal immersions of 2-spheres, Ann. of Math. (2) 113 (1981), no. 1, 1-24.
\item[] [11] L. M. Sibner and R. J. Sibner, Removable singularities of coupled Yang-Mills fields in $\mathbb{R}^{3}$, Comm. Math. Phys. 93 (1984), no. 1, 1-17.
\item[] [12] L. M. Sibner, Removable singularities of Yang-Mills fields in $\mathbb{R}^{3}$, Compositio Math. 53 (1984), no. 1, 91-104.
\item[] [13] L. M. Sibner, The isolated point singularity problem for the coupled Yang-Mills equations in higher dimensions, Math. Ann. 271 (1985), no. 1, 125-131.
\item[] [14] P. Smith, Removable singularities for the Yang-Mills-Higgs equations in two dimensions, Ann. Inst. H. Poincaré Anal. Non Linéaire 7 (1990), no. 6, 561-588.
\item[] [15] P. Smith and K. Uhlenbeck, Removability of a codimension four singular set for solutions of a Yang-Mills-Higgs equation with small energy, in Surveys in Differential Geometry 2019: Differential Geometry, Calabi-Yau Theory, and General Relativity, Part 2, Surv. Differ. Geom. 24, International Press, Boston, 257-291.
\item[] [16] C. Song, Convergence of Yang-Mills-Higgs fields, Math. Ann. 366 (2016), 1-51.
\item[] [17] T. Tao and G. Tian, A singularity removal theorem for Yang-Mills fields in higher dimensions, J. Amer. Math. Soc. 17 (2004), no. 3, 557-593.
\item[] [18] K. Uhlenbeck, Removable singularities in Yang-Mills fields, Comm. Math. Phys. 83 (1982), no. 1, 11-29.
\end{itemize}

School of Mathematics, South China University of Technology, Guangzhou 510640, People's Republic of China
Email address: cbmath@scut.edu.cn