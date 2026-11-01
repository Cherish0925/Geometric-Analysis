---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Conformal Laplacian and Conical Singularities]

---
source_file: da443eea27ea_0201058.pdf
converter: mathpix
format: mmd
---

\title{
Conformal Laplacian and Conical Singularities
}

\author{
Boris Botvinnik and Serge Preston
}

\begin{abstract}
We study a behavior of the conformal Laplacian operator $\mathbb{L}_{g}$ on a manifold with tame conical singularities: when each singularity is given as a cone over a product of the standard spheres. We study the spectral properties of the operator $\mathbb{L}_{g}$ on such manifolds. We describe the asymptotic of a general solution of the equation $\mathbb{L}_{g} u=Q u^{\alpha}$ with $1 \leq \alpha \leq \frac{n+2}{n-2}$ near each singular point. In particular, we derive the asymptotic of a Yamabe metric near such singularity.
\end{abstract}

\section*{1 Introduction}
1.1. The goal. The problem we consider in this paper has two essential parts. Firstly, we study the conformal Laplacian operator
$$\mathbb{L}_{g}=-\Delta_{g}+\frac{n-2}{4(n-1)} R_{g}$$
on a compact Riemannian manifold $(M, g)$ with isolated singularities of a particular type. Namely, each singular point has a neighborhood which is a cone over the product of spheres $S^{p} \times S^{q}$ endowed with the standard metric. Secondly, we derive asymptotics for the positive solutions of the semilinear elliptic equation
$$\mathbb{L}_{g} u=-\Delta_{g} u+\frac{n-2}{4(n-1)} R_{g} u=Q u^{\alpha}$$
near each singular point. Here $1 \leq \alpha \leq \frac{n+2}{n-2}=\alpha^{*}$, and $\operatorname{dim} M=n=$ $p+q+1 \geq 3$. We call the equation (1) the Yamabe equation. Indeed, for $\alpha=\alpha^{*}$ it corresponds to the Yamabe problem.
1.2. Motivation and some prospectives. Presenting this, somewhat technical paper, we would like to address and discuss natural questions which motivate our interest to study the conformal geometry on manifolds with the cone-type singularities over the product of spheres.

First we recall the classical setting for the Yamabe problem. Let $N$ be a compact smooth manifold, $\operatorname{dim} N=n \geq 3$, and $\mathcal{R i e m}(N)$ the space of Riemannian metrics on $N$. We denote by $R_{g}$ the scalar curvature and by $d \sigma_{g}$ the volume form for each Riemannian metric $g \in \mathcal{R} \operatorname{iem}(N)$. Then the (normalized) Einstein-Hilbert functional $I: \mathcal{R} \operatorname{iem}(N) \rightarrow \mathbf{R}$ is defined as
$$I: g \mapsto \frac{\int_{N} R_{g} d \sigma_{g}}{\operatorname{Vol}_{g}(N)^{\frac{n-2}{n}}} .$$
Let $\mathcal{C}(N)$ be the space of conformal classes on of Riemannian metrics on $N$, and $C \in \mathcal{C}(N)$. The classical Yamabe problem is to find a metric $\check{g}$ in a given conformal class $C$ such that the Einstein-Hilbert functional attains its minimum on $C: I(\check{g})=\inf _{g \in C} I(g)$. This minimizing metric $\check{g}$ is called a Yamabe metric, and the conformal invariant $Y_{C}(N):=I(\check{g})$ the Yamabe constant. It is a celebrated result in conformal geometry that the Yamabe problem has an affirmative solution for closed manifolds, see [31], [30], [3], [26].

The Yamabe invariant of $N$ is defined as $Y(N)=\sup _{C \in \mathcal{C}(N)} Y_{C}(N)$. It is well known that the Yamabe invariant $Y(N)$ is a diffeomorphism invariant of $N$. Furthemore, the Yamabe invariant completely determines the existence of a metric of positive scalar curvature: $Y(N)>0$ if and only if the manifold $N$ admits a metric of positive scalar curvature. On the other hand, there are just few examples of manifolds with special properties (in the dimensions at least than four) for which the value of the Yamabe invariant is actually known. The fundamental problem here is to compute the Yamabe invariant $Y(N)$ in terms of other known topological invariants of $N$. In particular, it is important to understand a behavior of the Yamabe constant/invariant under such topological operations as connected sum of manifolds and, more generally, a surgery.
O. Kobayashi [14] has proven the following estimate for the Yamabe invariant of a connected sum. Let $N_{1}, N_{2}$ be two compact closed manifolds of $\operatorname{dim} N_{1}=\operatorname{dim} N_{2}=n \geq 3$ and $N_{1,2}=N_{1} \# N_{2}$. Then
$$Y\left(N_{1,2}\right) \geq\left\{\begin{array}{cl}
-\left(\left|Y\left(N_{1}\right)\right|^{n / 2}+\left|Y\left(N_{2}\right)\right|^{n / 2}\right)^{2 / n} & \text { if } Y\left(N_{1}\right), Y\left(N_{2}\right) \leq 0, \\
\min \left\{Y\left(N_{1}\right), Y\left(N_{2}\right)\right\} & \text { otherwise. }
\end{array}\right.$$
Petean and Yun [23] have proven the same formula for the case when $N_{1,2}=$ $N_{1} \cup_{V} N_{2}$ is a union of two manifolds along a submanifold $V$ of codimension
at least three. This result allowed Petean to prove that $Y(N) \geq 0$ for any simply connected manifold of dimension at least five, [24] (see [9] for the case of non-simply connected manifolds).

A difficult case here is to study what is happening with the Yamabe invariant under surgery if $Y(N)>0$. In more detail, let $S^{p} \subset N$ be an embedded sphere with trivial normal bundle. Denote by $N^{\prime}$ the manifold obtained from $N$ by a surgery along the sphere $S^{p}$. The integer $n-p$ is called a codimension of the surgery. Assume that $Y(N) \leq 0$ and $n-p \geq 3$. Then one can use (2) to show that $Y\left(N^{\prime}\right) \geq Y(N)$, see [23] and also [1, Corollary 4.10]. In the case when $Y(N)>0$ the relationship between the invariants $Y(N)$ and $Y\left(N^{\prime}\right)$ is not clear. Consider the trace $W$ of the above surgery, i.e. $W=N \times I \cup D^{p+1} \times D^{q+1}, q=n-p-1$, where $S^{p} \times D^{q+1} \subset N \times\{1\}$ is identified with $S^{p} \times D^{q+1} \subset \partial\left(D^{p+1} \times D^{q+1}\right)$. In particular, the boundary of $W$ is a disjoint union of $N$ and $N^{\prime}$. According to the elementary Morse theory, one can choose a Morse function $f: W \rightarrow[-1,1]$ with a single nondegenerate critical point $p$ such that $N=f^{-1}(-1), N^{\prime}=f^{-1}(1)$ and $f(p)=0$. Let $N_{\tau}=f^{-1}(\tau)$, then the manifold $N_{\tau}$ is diffeomorphic to $N$ if $\tau<0$, and to $N^{\prime}$ if $\tau>0$. The manifold $N_{0}$ has an isolated singularity, the vertex of the cone $C\left(S^{p} \times S^{q}\right)$ with an appropriate metric, see Fig. 1.1.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-03.jpg?height=322&width=1181&top_left_y=1396&top_left_x=259}
\captionsetup{labelformat=empty}
\caption{Fig. 1.1.}
\end{figure}

Hence one can think about a surgery on a manifold $N$ as a deformation $N_{\tau}$, $-1 \leq \tau \leq 1$ through a "singular point" $N_{0}$. Furthermore, an appropriate metric on the trace $W$ gives a curve $\left(N_{\tau}, C_{\tau}\right)$ of conformal manifolds. We conjecture that the function $\tau \mapsto Y_{C_{\tau}}\left(N_{\tau}\right)$ is a continuous function. Then under an appropriate choice of conformal classes $C_{\tau}$, one can approach the following:

Conjecture 1.1 Let $N$ be a closed compact manifold of $\operatorname{dim} N=n \geq 5$, and $N^{\prime}$ be obtained from $N$ by a surgery of codimension at least three. Then $Y\left(N^{\prime}\right) \leq Y(N)$.

If Conjecture 1.1 is indeed true, then the Yamabe invariant would be a
cobordism invariant. In particular, it would mean that if $N$ is a simply-connected Spin-manifold cobordant to zero, then $Y(N)=Y\left(S^{n}\right)$.

From this viewpoint, it is important to understand the behavior of the conformal Laplacian under surgery, in particular our goal here is to extend the conformal geometry to the category of manifolds with conetype singularities over a product of spheres $S^{p} \times S^{q}$. This is the main goal of this paper.

On the other hand, we think that the results of this paper concerning the asymptotic of a solution of the Yamabe equation (1) are of independent value. The asymptotics for singular solutions of the Yamabe equation were studied thoroughly in the case when the manifold in question is the standard sphere $S^{n}$ punctured at $k$ points, see [19], [15]. In particular, this is related to a gluing construction of metrics of constant scalar curvature under connected sum operation, see [20]. We believe that the results of our paper could be used to glue metrics of constant scalar curvature under surgery.

We have one more application in mind. The paper of the first author and Akutagawa [1] gives an affirmative solution of the Yamabe problem for cylindrical manifolds. In particular, in the case of the positive cylindrical Yamabe constant the asymptotic of a Yamabe metric is almost conical near a cylindrical end, see [1]. In that case, it is easy to see that a manifold with cylindrical ends is equivalent to a manifold with the cone-type singularities. In particular, the Yamabe problem has a solution for manifolds with conetype singularities over the product $S^{p} \times S^{q}$ we study here. As an application, we find an explicit asymptotic for a Yamabe metric in the specific case related to surgery, see Corollary 7.4.
1.3. Conformal Laplacian and the Yamabe equation. Let $M$ be a compact closed manifold of dimension at least three. For a given Riemannian metric $g$ there is the energy functional
$$E_{g}(\varphi)=\int_{M}\left(|\nabla \varphi|^{2}+\frac{n-2}{4(n-1)} R_{g} \varphi^{2}\right) d \sigma_{g} .$$
Let $1 \leq \alpha \leq \frac{n+2}{n-2}=\alpha^{*}$. We consider the functional
$$Q_{\alpha}(\varphi)=\frac{E_{g}(\varphi)}{\left(\int_{M}|\varphi|^{\alpha+1} d \sigma_{g}\right)^{\frac{2}{\alpha+2}}}, \quad \varphi \in H_{2}^{1}(M), \quad \varphi>0$$
with the Euler-Lagrange equation
$$-\Delta_{g} u_{\alpha}+\frac{n-2}{4(n-1)} R_{g} u_{\alpha}=Q_{\alpha}(M) u_{\alpha}^{\alpha} .$$
Here $H_{2}^{1}(M)$ is the Sobolev space of functions from $L_{2}(M)$ with their first derivatives (as distributions) also in $L_{2}(M)$. The Sobolev embedding theorems imply that for each $\alpha \in\left[1, \alpha^{*}\right)$ there exists a smooth function $u_{\alpha}>0$ with
$$\int_{M} u_{\alpha}^{\alpha+1} d \sigma_{g}=1, \quad \text { satisfying } \quad Q_{\alpha}\left(u_{\alpha}\right)=\min \left\{Q_{\alpha}(\varphi) \mid \varphi \in H_{1}(M)\right\} .$$
We denote $Q_{\alpha}(M)=Q_{\alpha}\left(u_{\alpha}\right)$. The sign of the constants $Q_{\alpha}(M)$ is the same for all $1 \leq \alpha \leq \alpha^{*}$ and it depends only on the conformal class of the metric $g$, see [3]. The existence of a minimizing function in the case $\alpha=\alpha^{*}$ is the celebrated Yamabe problem, see [31], [30], [2] and [26]. The solution of the Yamabe problem had to overcome the fundamental analytic difficulty concerning Sobolev inequalities for the critical exponent $\alpha^{*}$. The constant $Q_{\alpha^{*}}(M)$ depends only on the conformal class $[g]$ and is known as the Yamabe constant $Y_{[g]}(M)$ of the conformal class $[g]$. On the other hand, the constant $Q_{1}(M)$ coincides with the first eigenvalue $\mu_{1}\left(\mathbb{L}_{g}\right)$ of the conformal Laplacian $\mathbb{L}_{g}$.
1.4. Manifolds with tame conical singularity. Let $M_{0}$ be a compact smooth manifold, $\operatorname{dim} M_{0}=n \geq 3$ with the boundary
$$\partial M_{0}=S^{p} \times S^{q} \quad(\text { where } p+q=n-1) .$$
Let $C\left(S^{p} \times S^{q}\right)$ be a cone over $S^{p} \times S^{q}$ with the vertex point $x_{*}$. We glue together $M_{0}$ and the cone $C\left(S^{p} \times S^{q}\right)$ along the boundary $S^{p} \times S^{q}$ to obtain a manifold with a conical singularity $x_{*} \in M$ :
$$M=M_{0} \cup_{S^{p} \times S^{q}} C\left(S^{p} \times S^{q}\right) .$$
Now we describe a metric on the manifold $M$. Let $S^{k}(r)$ be a sphere with the standard metric of radius $r$. First, we assume that $S^{p}=S^{p}\left(r_{p}\right)$ and $S^{q}=S^{q}\left(r_{q}\right)$. Let $(\theta, \psi, \ell)$ be the standard coordinate system on the cone $C\left(S^{p} \times S^{q}\right)$, where $\theta, \psi$ are the spherical coordinates on $S^{p}, S^{q}$ respectively, and $0 \leq \ell \leq \varepsilon_{1}$. In particular, $(\theta, \psi, 0)=x_{*}$ is the singular point, and $\left(\theta, \psi, \varepsilon_{1}\right)$ give spherical coordinates on $S^{p} \times S^{q}=\partial M_{0}$. Let $\varepsilon_{0}<\varepsilon_{1}$. We
decompose $C\left(S^{p} \times S^{q}\right)=K \cup B$ where
$$\begin{aligned}
& K=\left\{(\theta, \psi, \ell) \in C\left(S^{p} \times S^{q}\right) \mid 0 \leq \ell \leq \varepsilon_{0}\right\}, \\
& B=\left\{(\theta, \psi, \ell) \in C\left(S^{p} \times S^{q}\right) \mid \varepsilon_{0} \leq \ell \leq \varepsilon_{1}\right\} .
\end{aligned}$$
We denote by $\Lambda=\Lambda(p, q)$ the following constant
$$\Lambda=p(p-1) \frac{2-r_{p}^{2}}{r_{p}^{2}}+q(q-1) \frac{2-r_{q}^{2}}{r_{q}^{2}}-2 p q .$$
We endow $M$ with a Riemannian metric $g$ satisfying the following properties:
\begin{itemize}
\item[(1)] The scalar curvature function $R_{g}(x)>0$ if $x \in M_{0}$.
\item[(2)] Let $g_{K}=\left.g\right|_{K}$ be the standard conic metric
$$g_{K}=d \ell^{2}+\frac{\ell^{2} r_{p}^{2}}{2} d^{2} \theta+\frac{\ell^{2} r_{q}^{2}}{2} d^{2} \psi$$
induced from the Euclidian metric in $C\left(S^{p} \times S^{q}\right) \subset \mathbf{R}^{p+1} \times \mathbf{R}^{q+1}$, where $S^{p}=S^{p}\left(r_{p}\right), S^{q}=S^{q}\left(r_{q}\right)$. (In particular, $R_{g_{K}}(\theta, \psi, \ell)=\frac{\Lambda}{\ell^{2}}$, see Section 2.)
\end{itemize}

Definition 1.1 A manifold $(M, g)$ satisfying the above conditions is called a manifold with tame conical singularity.

The conformal Laplacian $\mathbb{L}_{g}=-\Delta_{g}+\frac{n-2}{4(n-1)} R_{g}$ is well-defined on the manifold $M$ without the singular point $x_{*}$. In particular, we have the Yamabe equation $\mathbb{L}_{g} u=Q_{\alpha} u^{\alpha}$ on $M \backslash\left\{x^{*}\right\}$ for $1 \leq \alpha \leq \alpha^{*}=\frac{n+2}{n-2}$.
1.5. Results. We study the following issues:
\begin{itemize}
\item[(A)] The spectral properties of the conformal Laplacian $\mathbb{L}_{g}$ on a manifold with tame conical singularity.
\item[(B)] The asymptotic of a general solution of the linear Yamabe equation (i.e. when $\alpha=1$ ) near the singular point.
\item[(C)] The asymptotic of a general solution of the non-linear Yamabe equation near the singular point for $1<\alpha \leq \alpha^{*}$.
\end{itemize}

The paper is organized as follows. We describe in detail the geometry of $M$ and the Yamabe equation near the singular point in Section 2. We define appropriate weighted Sobolev spaces in Section 3. We study the conformal Laplacian $\mathbb{L}_{g}$ on $M$ in Section 4, in particular, we prove that under some dimensional restrictions the operator $\mathbb{L}_{g}$ is positive. We analyze the functional $I_{\alpha}$ on $M$ and prove a weak version of the Yamabe theorem in Section 5. We study the asymptotic of a general solution of the linear and nonlinear Yamabe equations in Sections 6 and 7 respectively. We put together some technical results and calculations in Appendix (Section 8).
1.6. Acknowledgments. The authors are grateful to Kazuo Akutagawa for useful discussions on the Yamabe invariant and to the referee for his helpful and encouraging remarks. We are also grateful to Ms. Melisa Gilbert for the editorial help.

\section*{2 The Yamabe equation on the cone}

The cone $K \subset \mathbf{R}^{p+1} \times \mathbf{R}^{q+1}=\mathbf{R}^{n+1}$ is given by
$$K=\left\{\left(x_{1}, \ldots, x_{n+1}\right) \left\lvert\, \frac{1}{r_{q}^{2}}\left(x_{1}^{2}+\cdots+x_{p+1}^{2}\right)-\frac{1}{r_{q}^{2}}\left(x_{p+2}^{2}+\cdots+x_{n+1}^{2}\right)=0\right.\right\} .$$
We use the polar coordinates $(r, \theta)$ in $\mathbf{R}^{p+1}$, where $\theta \in S^{p}$, and $(\rho, \psi)$ in $\mathbf{R}^{q+1}$, where $\psi \in S^{q}$. Then the equation (5) can be written as $\frac{\rho}{r_{p}}=\frac{r}{r_{q}}$.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/32245020-4790-4b69-99f9-944eaca7e53e-07.jpg?height=454&width=548&top_left_y=1577&top_left_x=257}
\captionsetup{labelformat=empty}
\caption{Fig. 2.1.}
\end{figure}
The coordinate $\ell$ is the distance from a point on the cone to the vertex $x^{*}$. Then $\ell=r \sqrt{2}=\rho \sqrt{2}$. The embedding $K \subset \mathbf{R}^{n+1}$ induces the metric $g_{K}$ from the standard metric on $\mathbf{R}^{n+1}$. In polar coordinates the metric $g_{K}$ is given as
$$\begin{aligned}
g_{K} & =d r^{2}+r^{2} d^{2} \theta+r^{2} d^{2} \psi \\
& =d \ell^{2}+\frac{r_{p}^{2} \ell^{2}}{2} d^{2} \theta+\frac{r_{q}^{2} \ell^{2}}{2} d^{2} \psi .
\end{aligned}$$

We compute the determinant $\left|g_{K}\right|$ :
$$\begin{gathered}
\left|g_{K}\right|=\operatorname{det}\left(g_{i j}\right)=1 \cdot\left(\frac{r_{p}^{2} \ell^{2}}{2}\right)^{p} \cdot\left|g_{\theta}\right| \cdot\left(\frac{r_{q}^{2} \ell^{2}}{2}\right)^{q} \cdot\left|g_{\psi}\right|, \quad \text { and } \\
\sqrt{\left|g_{K}\right|}=\frac{r_{p}^{p} r_{q}^{q} \ell^{n-1}}{2^{\frac{n-1}{2}}} \cdot \sqrt{\left|g_{\theta}\right|} \cdot \sqrt{\left|g_{\psi}\right|} .
\end{gathered}$$
Here $g_{\theta}$ and $g_{\psi}$ are the standard metrics on the spheres $S^{p}\left(r_{p}\right)$ and $S^{q}\left(r_{q}\right)$ respectively. In particular, we have the following formula for the volume element:
$$d \sigma_{g_{K}}=\frac{r_{p}^{p} r_{q}^{q} \ell^{n-1}}{2^{\frac{n-1}{2}}} d \ell \wedge d \sigma_{g_{\theta}} \wedge d \sigma_{g_{\psi}} .$$
The Laplace operator on the cone is then given as
$$\Delta_{g_{K}}=\frac{1}{\sqrt{\left|g_{K}\right|}} \partial_{x^{i}}\left(\sqrt{\left|g_{K}\right|} g_{K}^{i j} \partial_{x^{j}}\right) .$$
The matrix $\left(g_{K}^{i j}\right)$ is block diagonal:
$$\left(g_{K}^{i j}\right)=\left(\begin{array}{l|l|l}
1 & & \\
\hline & \frac{2 g_{\theta}^{i j}}{\ell^{2} r_{p}^{2}} & \\
& & \frac{2 g_{\psi}^{i j}}{\ell^{2} r_{q}^{2}}
\end{array}\right) .$$
We obtain:
$$\begin{aligned}
\Delta_{g_{K}} & =\frac{2^{\frac{n-1}{2}}}{\ell^{n-1}} \partial_{\ell}\left(\frac{\ell^{n-1}}{2^{\frac{n-1}{2}}} \partial_{\ell}\right)+\frac{2}{r_{p}^{2} \ell^{2}} \Delta_{\theta}+\frac{2}{r_{q}^{2} \ell^{2}} \Delta_{\psi} \\
& =\frac{\partial^{2}}{\partial \ell^{2}}+(n-1) \frac{1}{\ell} \frac{\partial}{\partial \ell}+\frac{2}{r_{p}^{2} \ell^{2}} \Delta_{\theta}+\frac{2}{r_{q}^{2} \ell^{2}} \Delta_{\psi} .
\end{aligned}$$
The metric $g_{K}$ is a particular case of a "double wrapped metric" on the product $I \times S^{p} \times S^{q}$. In general, a double wrapped metric is given as
$$d \ell^{2}+\varphi_{p}^{2}(\ell) d^{2} \theta+\varphi_{q}^{2}(\ell) d^{2} \psi .$$

In our case
$$\varphi_{p}(\ell)=\frac{r_{p} \ell}{\sqrt{2}}, \quad \varphi_{q}(\ell)=\frac{r_{q} \ell}{\sqrt{2}}, \quad \dot{\varphi}_{p}=\frac{r_{p}}{\sqrt{2}}, \quad \dot{\varphi}_{q}=\frac{r_{q}}{\sqrt{2}}, \quad \ddot{\varphi}_{p}=0, \quad \ddot{\varphi}_{q}=0 .$$
We choose the orthonormal bases for the tangent space to $K$ :
$$F_{0}=\partial_{\ell}, \quad F_{i}, i \in \bar{p}, \quad F_{j}, j \in \bar{q},$$
where $\bar{p}=\{2, \ldots, p\}, \bar{q}=\{p+1, \ldots, p+q\}$ are orthonormal basis for the standard metrics on $S^{p}$ and $S^{q}$ correspondingly. Then we have the following formulas for the curvature operator $\mathcal{R}$ acting on the bundle of 2-forms (see, for instance the book by P. Petersen [25]):
$$\begin{aligned}
& \mathcal{R}\left(F_{0} \wedge F_{i}\right)=0, \quad i \in \bar{p}, \\
& \mathcal{R}\left(F_{0} \wedge F_{j}\right)=0, \quad i \in \bar{q}, \\
& \mathcal{R}\left(F_{i_{1}} \wedge F_{i_{2}}\right)=\frac{2-r_{p}^{2}}{r_{p}^{2} \ell^{2}} F_{i_{1}} \wedge F_{i_{2}}, \quad i_{1}, i_{2} \in \bar{p}, \\
& \mathcal{R}\left(F_{j_{1}} \wedge F_{j_{2}}\right)=\frac{2-r_{q}^{2}}{r_{q}^{2} \ell^{2}} F_{j_{1}} \wedge F_{j_{2}}, \quad j_{1}, j_{2} \in \bar{q}, \\
& \mathcal{R}\left(F_{i} \wedge F_{j}\right)=-\frac{1}{\ell^{2}} F_{i} \wedge F_{j}, \quad i \in \bar{p}, \quad j \in \bar{q} .
\end{aligned}$$
Thus we have:
$$\begin{aligned}
\operatorname{Ric}\left(F_{0}\right) & =0 \\
\operatorname{Ric}\left(F_{i}\right) & =\left((p-1) \frac{2-r_{p}^{2}}{r_{p}^{2} \ell^{2}}-q \frac{1}{\ell^{2}}\right) F_{i}, \\
\operatorname{Ric}\left(F_{j}\right) & =\left((q-1) \frac{2-r_{q}^{2}}{r_{q}^{2} \ell^{2}}-p \frac{1}{\ell^{2}}\right) F_{i} .
\end{aligned}$$

We compute the scalar curvature:
$$\begin{aligned}
R_{g_{K}} & =\operatorname{Tr} \mathcal{R} i c=p\left[(p-1) \frac{2-r_{q}^{2}}{r_{p}^{2} \ell^{2}}-\frac{q}{\ell^{2}}\right]+q\left[(q-1) \frac{2-r_{q}^{2}}{r_{q}^{2} \ell^{2}}-\frac{p}{\ell^{2}}\right]= \\
& =\frac{1}{\ell^{2}} \cdot\left[p(p-1) \frac{2-r_{p}^{2}}{r_{p}^{2}}+q(q-1) \frac{2-r_{q}^{2}}{r_{q}^{2}}-2 p q\right]=\frac{\Lambda}{\ell^{2}}, \quad \text { with } \\
\Lambda & =p(p-1) \frac{2-r_{p}^{2}}{r_{p}^{2}}+q(q-1) \frac{2-r_{q}^{2}}{r_{q}^{2}}-2 p q
\end{aligned}$$
We refer to the Appendix for some properties of $\Lambda$ as a function of $p, q, r_{p}$, $r_{q}$.

Now we can rewrite the Yamabe equation $\mathbb{L}_{g} u=Q_{\alpha} u^{\alpha}$ for the cone $K$. We obtain:
$$\begin{gathered}
\frac{\partial^{2} u}{\partial \ell^{2}}+\frac{n-1}{\ell} \frac{\partial u}{\partial \ell}+\frac{2}{r_{p}^{2} \ell^{2}} \Delta_{\theta} u+\frac{2}{r_{q}^{2} \ell^{2}} \Delta_{\psi} u-\frac{n-2}{4(n-1)} \frac{\Lambda}{\ell^{2}} u+Q_{\alpha} u^{\alpha}=0, \\
\text { where } 1 \leq \alpha \leq \alpha^{*} \text { and with } \quad \int_{K} u^{\alpha+1}<1, \quad u_{\alpha}>0 .
\end{gathered}$$
We notice that $\int_{K} u^{\alpha+1}<1$ since $\int_{M} u^{\alpha+1}=1$.

\section*{3 Sobolev spaces on $M$}

In this section we introduce appropriately weighted Sobolev spaces on a manifold with tame conical singularities and review their basic properties. We denote $d \sigma_{g}$ the volume form on $M$ corresponding to the metric $g$. According to the computations above, the form $d \sigma_{g}$, restricted on the cone part $K$, is given by
$$d \sigma_{g}=\frac{\ell^{n-1}}{2^{\frac{n-2}{2}}} \sqrt{\left|g_{\theta}\right|} \sqrt{\left|g_{\psi}\right|} d \ell \wedge d \sigma_{\theta} \wedge d \sigma_{\psi}$$
Let $L_{2}(M)$ be the Hilbert space of functions $\varphi$ on $M$. Clearly, the restriction $\left.\varphi\right|_{K}=\varphi(\ell, \theta, \psi)$ of a function $\varphi \in L_{2}(M)$ on the cone $K$ satisfies the property
$$\int_{0}^{\varepsilon_{0}} \int_{S^{p}} \int_{S^{q}}|\varphi(\ell, \theta, \psi)|^{2} \ell^{n-1} d \ell \wedge d \sigma_{\theta} \wedge d \sigma_{\psi}<\infty .$$

The proof of the following lemma is standard.
Lemma 3.1 Let $\varphi$ be a function on $M$ with $\int_{M \backslash K}|\varphi|^{2} d \sigma_{g}<\infty$, and with the asymptotic behavior $\left.\varphi\right|_{K}=\varphi(\ell, \theta, \psi)=\ell^{s}(1+O(1))$ as $\ell \rightarrow 0$. Then the following statements are equivalent:
\begin{itemize}
\item[(1)] The integral (8) converges.
\item[(2)] The function $\varphi \in L_{2}(M)$.
\item[(3)] $s>-\frac{n}{2}$.
\end{itemize}
Let $\chi \in C^{\infty}\left(M \backslash x_{*}\right)$ be a positive weight function satisfying
$$\chi(x)=\left\{\begin{array}{ll}
1 & \text { if } x \in M_{0}, \\
\frac{1}{\ell} & \text { if } x \in K
\end{array} \quad \text { and } \quad 0<\chi(x) \leq 1 \quad \text { for all } x \in M \backslash x_{*} .\right.$$
It is easy to construct such a function. Then a weighted Sobolev space $H_{2}^{k}(M)=H_{2}^{k}(M, g)$ is defined as a space of locally integrable functions $\varphi \in L_{1}^{\text {loc }}(M, g)$ with finite norm
$$\|\varphi\|_{H_{k}^{2}(M)}^{2}=\int_{M}\left(\sum_{i=0}^{k} \chi^{2(k-i)} \sum_{|\mu|=i}\left|D^{\mu} \varphi\right|^{2}\right) d \sigma_{g} .$$
The derivatives here are understood as distributions (i.e. $D^{\mu} \varphi \in L_{1}^{\text {loc }}(M, g)$, $|\mu| \leq k$ ). We denote by $C_{*}^{\infty}(M)$ the space of smooth functions on $M$ that are equal to zero in some neighborhood of the singular point $x_{*}$. We notice that although the norm of a function $\varphi$ in Sobolev spaces defined here depends on the choice of the weight $\chi$, the property of $\varphi$ belonging to the corresponding Sobolev space does not.

Remark. The spaces $H_{2}^{k}(M, g)$ defined above coincide with the spaces $W_{2}^{k}\left(M, 1, \rho^{2 k}\right)$ defined by H. Triebel [29, Section 3.24, 3.26], where $\rho(x)=$ $\chi(x)$.
In particular, according to [29, Section 3.2.3], the spaces $H_{2}^{k}(M, g)$ are complete Hilbert spaces with the scalar product
$$\langle\varphi, \psi\rangle_{H_{k}^{2}(M)}=\int_{M}\left(\sum_{i=0}^{k} \chi^{2(k-i)} \sum_{|\mu|=i} D^{\mu} \varphi D_{\mu} \psi\right) d \sigma_{g} .$$

The spaces $H_{2}^{k}(M, g)$ are closely related to the functional spaces $V_{2,0}^{k}(M, g)$ and $W_{2, \beta}^{k}(M)$ defined in the book [16]. The space $V_{2,0}^{k}(M, g)$ is a closure of the space $C_{*}^{\infty}(M)$ in the norm (8), [16, Section 6.1.1], and the space $W_{2, \beta}^{k}(M, g)$ is defined as a space of locally integrable functions $\varphi \in$ $L_{\text {loc }}^{1}\left(M, d \sigma_{g}\right)$ with the following finite norm:
$$\|\varphi\|_{W_{2, \beta}^{\ell}(M)}^{2}=\left(\int_{M} r^{2 \beta} \sum_{|\mu| \leq \ell}\left|D^{\mu} \varphi\right|^{2} d \sigma_{g}\right)^{1 / 2},$$
where the weight function $r$ is related to our weight function as $\chi \sim r^{-1}$ (see [16, Section 7.1.2]). Clearly we have the following embeddings
$$V_{2,0}^{k}(M, g) \subset H_{k}^{2}(M, g) \subset W_{2,0}^{k}(M, g) .$$
These embeddings are continuous; moreover, if $\beta>k-n / 2$, the spaces $V_{2, \beta}^{k}(M, g)$ and $W_{2, \beta}^{k}(M, g)$ coincide and their norms are equivalent (see [16, Theorem 7.1.1]). In our case, when $\beta=0$ (when $k<n / 2$ ) three spaces in (10) coincide. This implies the following result.

Lemma 3.2 Let $n=\operatorname{dim} M \geq 5$. Then the space $C_{*}^{\infty}(M)$ is dense in the spaces $H_{2}^{1}(M, g)$ and $H_{2}^{2}(M, g)$.

Remark. Lemma 3.2 is the first point when the analysis implies the dimensional restriction $n \geq 5$. We do not know whether some modification of Lemma 3.2 holds in dimensions $n=3,4$.

Now we recall the embedding theorem, following the exposition of H. Triebel [29], for the spaces $H_{2}^{k}(M, g)=W_{2}^{k}\left(\Omega, \rho^{0}, \rho^{2}\right)$ (where $\rho=\chi$ ).

Theorem 3.3 Let $M$ be a manifold with a tame conical singularity as above, $n \geq 5$. Let $2 \leq p \leq 1+\alpha^{*}, \alpha^{*}=\frac{n+2}{n-2}$. Then there exists a continuous linear embedding
$$i_{p}: H_{2}^{k}(M, g) \subset L_{p}(M)$$
for $k \geq 1$. Furthermore, the embedding operator $i_{p}$ is compact for $2 \leq p<$ $1+\alpha^{*}$.

Proof. This result follows by combining the embedding theorems of Triebel (see the book [29, Theorems 3.5.1, and 3.8.3]) for the domains in $\mathbf{R}^{n}$ with conical points on the boundary with the classical embedding theorems for Sobolev spaces on compact manifolds (see, for example, [3, Theorems 2.10, 2.33]). \(\square\)

There is an important special case here. Clearly, we have the embeddings:
$$H_{2}^{2}(M, g) \subset H_{2}^{1}(M, g) \subset L_{2}(M) .$$
Theorem 3.3 implies that the embedding $H_{1}^{1}(M, g) \subset L_{2}(M)$ is compact. We will need the following lemma which follows from Theorem 3.3.

Lemma 3.4 Let $n \geq 5$, then in the space $H_{2}^{1}(M, g)$ the norms
$$\|\nabla \varphi\|_{2}^{2}+\|\chi \varphi\|_{2}^{2} \quad \text { and } \quad\|\nabla \varphi\|_{2}^{2}+\|\varphi\|_{2}^{2}$$
are equivalent, in particular, for some $C>0$
$$\|\chi \varphi\|_{2}^{2} \leq C\left(\|\nabla \varphi\|_{2}^{2}+\|\varphi\|_{2}^{2}\right) .$$
The following lemma allows us to compare norms in $L_{2}\left(M_{0}\right)$ and $L_{2}(M)$.
Lemma 3.5 Let $n \geq 5$. Then for any constant $a>0$ there exists a constant $C>0$ such that
$$\|\nabla u\|_{L_{2}(M)}+a\|u\|_{L_{2}\left(M_{0}\right)} \geq C\|u\|_{L_{2}(M)}$$
for any function $u \in H_{2}^{1}(M)$.
Proof. Notice, first, that for a function $u$ as in the formulation of Lemma 3.5, we have $\left.u\right|_{M_{0}} \in L_{2}\left(M_{0}\right)$. Assume that for some $a>0$ there is no such constant $C>0$. Then there exists a sequence $u_{n} \in H_{2}^{1}(M)$, such that
$$\left\|u_{n}\right\|_{L_{2}(M)}=1, \quad \text { and } \quad\left\|\nabla u_{n}\right\|_{L_{2}(M)} \rightarrow 0, \quad\left\|u_{n}\right\|_{L_{2}\left(M_{0}\right)} \rightarrow 0$$
as $n \rightarrow \infty$. Recall that the embedding $H_{2}^{1}(M) \subset L_{2}(M)$ is compact; thus, passing to a subsequence, if necessary, we get $u_{n} \rightarrow u_{\infty}$ in $L_{2}(M)$ for some $u_{\infty} \in L_{2}(M)$. Clearly we have $\left\|u_{\infty}\right\|_{L_{2}(M)}=1$, but $u_{\infty \mid M_{0}}=0$ almost everywhere since $u_{n} \rightarrow 0$ in $L_{2}\left(M_{0}\right)$ as $n \rightarrow \infty$. Now we choose a function $\varphi \in C_{0}^{\infty}(M)$ (in particular, $\varphi$ has compact support). We have
$$\left|\left\langle\nabla u_{n}, \nabla \varphi\right\rangle_{L_{2}(M)}\right| \leq\left\|\nabla u_{n}\right\|_{L_{2}(M)} \cdot\|\nabla \varphi\|_{L_{2}(M)} .$$
As $n \rightarrow \infty$ the right-hand side goes to zero, thus the left-hand side too. However
$$\left\langle\nabla u_{n}, \nabla \varphi\right\rangle_{L_{2}(M)}=\left\langle u_{n}, \Delta \varphi\right\rangle_{L_{2}(M)} \longrightarrow\left\langle u_{\infty}, \Delta \varphi\right\rangle_{L_{2}(M)}$$
(using that $\operatorname{Supp}(\varphi)$ is compact). Thus, $\left\langle u_{\infty}, \Delta \varphi\right\rangle_{L_{2}(M)}=0$ for all $\varphi \in$ $C_{0}^{\infty}(M)$, i.e. $u_{\infty} \in L_{2}(M)$ is a weak solution of the equation $\Delta_{g} u=0$. Since the Laplacian $\Delta_{g}$ is an elliptic operator, $u_{\infty}$ is analytic in $M$. Since $u_{\infty \mid M_{0}} \equiv 0$, then $u_{\infty} \equiv 0$ on $M$. This contradicts to $\left\|u_{\infty}\right\|_{L_{2}(M)}=1$. \(\square\)

Let $H_{2, *}^{k}(M, g)$ be the corresponding Sobolev space of functions on $M$ with some open neighborhood of the singular point $x_{*}$ removed.

Lemma 3.6 Let $f=f(l, \theta, \psi) \in H_{2, *}^{k}(M)$ be a measurable function, so that $f \in H_{2}^{k}\left(M_{*}\right)$, and $f$ has asymptotic behavior $f \sim l^{q}$ as $l \longrightarrow 0$ near the point $x_{*}$. Then, $f \in H_{2}^{k}(M)$ if and only if $k<q+\frac{n}{2}$.

Proof. We have that the integral in the formula (9) near $\ell=0$ has the form
$$\int_{0}^{\varepsilon} \ell^{2(q-k)} \ell^{n-1} d \ell$$
The integral in (9) (taken over $M \backslash U$ where $U$ is some open neighborhood of $x_{*}$ ) is finite by the condition on $f$. It is easy to see that the Sobolev norm of the function $f$ over all $M$ in (9) is finite if and only if $2(q-k)+n-1>-1$, or, if $q-k+\frac{n}{2}>0$. This gives the condition $k<q+\frac{n}{2}$. \(\square\)

Later it will be convenient for us to refer to a class of functions with particular asymptotic near the singular point $x_{*}$.

Definition 3.1 Let $1 \leq \alpha \leq \alpha^{*}$. A locally integrable function $f \in L_{1, *}(M)$ is called an $\alpha$-basic function if $f \sim \ell^{-\frac{2}{\alpha-1}}$ as $\ell \rightarrow 0$, namely,
$$c \cdot \ell^{-\frac{2}{\alpha-1}} \leq|f(\ell, \theta, \psi)| \leq C \cdot \ell^{-\frac{2}{\alpha-1}}$$
for some positive constants $c, C$.
In particular, if $\alpha=\alpha^{*}=\frac{n+2}{n-2}$, an $\alpha$-basic function means that $f \sim \ell^{-\frac{n-2}{2}}$ near $x_{*}$.

It is easy to see that Lemma 3.6 implies the following result:
Proposition 3.7 Let $1 \leq \alpha \leq \alpha^{*}$. Then an $\alpha$-basic function $f$ belongs to $L_{2}(M)$ if and only if $\frac{n+4}{n}<\alpha \leq \alpha^{*}$. Furthermore, $f$ does not belong to $H_{2}^{1}(M)$ if $\alpha \in\left[1, \alpha^{*}\right)$.

Proof. Let $f$ be an $\alpha$-basic function. Then $f \in H_{2}^{k}(M)$ if and only if $k<\frac{n}{2}-\frac{2}{\alpha-1}$. Then $k=0$ gives $\alpha-1>\frac{4}{n}$ or $\alpha>\frac{n+4}{n}$, and $k=1$ gives $\frac{2}{\alpha-1}<\frac{n}{2}-1=\frac{n-2}{2}$, or $\alpha-1>\frac{4}{n-2}$. But this is exactly opposite to the main condition for the parameter $\alpha: \alpha \leq \alpha^{*}$. \(\square\)

\section*{4 Spectral properties of the conformal Laplacian}
4.1. General remarks. In this section we study the conformal Laplacian
$$\mathbb{L}_{g}=-\Delta_{g}+c(x), \quad \text { with } \quad c(x)=\frac{n-2}{4(n-1)} R_{g}(x)$$
on a manifold $M$ with tame conical singularity.
The classical Laplace operator $\Delta_{g}$ has been studied thoroughly on compact manifolds and on manifolds with certain singularities. In particular, the spectral properties of the Laplacian and its heat kernel are well-understood. The conformal Laplacian is studied predominantly through its relation to the conformal geometry in general, and the Yamabe problem in particular, although there has been important work done on its general properties as well (for example, work by T. Parker, S. Rosenberg [22], by T. Branson [6], see also the references given in the book by P. Gilkey [11]).

On the other hand, operators of the type (11) were studied much as Schrödinger operators. For example, the book by S. Mizohata [21, Chapter 8]) studies the Schrödinger operator $-\Delta+c(x)$ on $\mathbf{R}^{3}$ where the function $c(x)$ has a singularity at the origin of order $|x|^{-\frac{3}{2}+\varepsilon}$ or weaker. Under these conditions, the operator $-\Delta+c(x)$ is bounded from below and has a unique self-adjoint extension (Friedrichs' extension). Additional asymptotic conditions (when $|x| \rightarrow \infty$ ) on $c(x)$ ensure that the spectrum of $-\Delta+c(x)$ is discrete and of finite multiplicity.
4.2. Basic results. We start with the following standard property of $\mathbb{L}_{g}$ (this follows from the basic results on the Sobolev spaces).

Proposition 4.1 The conformal Laplacian $\mathbb{L}_{g}=-\Delta_{g}+\frac{n-2}{4(n-1)} R_{g}$ is densely defined in $\mathbb{L}_{2}(M)$ with the domain $H_{2}^{2}(M, g)$. Furthermore, the operator $\mathbb{L}_{g}$ is symmetrical and continuous with respect to the norm in $H_{2}^{2}(M, g)$.

Proof. It is obvious that this operator is symmetric with the domain $C_{*}^{\infty}(M)$. We look at the norm
$$\left|\mathbb{L}_{g} \varphi\right|^{2}=\left(-\Delta_{g} \varphi+\frac{n-2}{4(n-1)} R_{g} \varphi\right)^{2} \leq 2\left(\left(\Delta_{g} \varphi\right)^{2}+\left(\frac{n-2}{4(n-1)}\right)^{2} R_{g}^{2} \varphi^{2}\right) .$$

Integration over $M$ gives:
$$\left\|\mathbb{L}_{g} \varphi\right\|_{L_{2}(M)}^{2} \leq 2\left(\int_{M}\left(\Delta_{g} \varphi\right)^{2} d \sigma_{g}+C \int_{M} R_{g}^{2} \varphi^{2} d \sigma_{g}\right) .$$
Notice now that $\left|R_{g}(x)\right| \leq C_{1} \chi(x)$ for some constant $C_{1}$ (Indeed, on $M \backslash K$ the scalar curvature is bounded from above while on the cone $K$ it is equal to $\Lambda \chi(x)$.) Thus using the definition of the norm (9) we obtain
$$\left\|\mathbb{L}_{g} \varphi\right\|_{L_{2}(M)}^{2} \leq 2\left(\int_{M}\left(\Delta_{g} \varphi\right)^{2} d \sigma_{g}+C_{1} \int_{M} \chi^{2} \varphi^{2} d \sigma_{g}\right) \leq C_{g}\|\varphi\|_{H_{2}^{2}(M, g)}^{2} .$$
This proves Proposition 4.1. \(\square\)

Theorem 4.2 Let $(M, g)$ be a manifold with tame conical singularity of $\operatorname{dim} M=n \geq 3$. Then the quadratic form $\left\langle\mathbb{L}_{g} u, u\right\rangle$ defined on $H_{2}^{1}(M, g)$ is such that
$$D\|u\|_{H_{2}^{1}(M, g)}^{2} \leq\left\langle\mathbb{L}_{g} u, u\right\rangle \leq C\|u\|_{H_{2}^{1}(M, g)}^{2}$$
for some constants $C>0$ and $D>-\infty$ (i.e. the form $\left\langle\mathbb{L}_{g} u, u\right\rangle$ is bounded from below). Furthermore,
\begin{itemize}
\item[(1)] if $\Lambda>0$, then
$$C_{1}\|u\|_{H_{2}^{1}(M, g)}^{2} \leq\left\langle\mathbb{L}_{g} u, u\right\rangle \leq C_{2}\|u\|_{H_{2}^{1}(M, g)}^{2}$$
for some constants $C_{1}>0, C_{2}>0$;
\item[(2)] if $\Lambda \leq 0$ then for each $r_{p}, r_{q}$ there is only a finite number of nonpositive eigenvalues (each of finite multiplicity) of the operator $\mathbb{L}_{g}$.
\end{itemize}

Corollary 4.3 Let $\Lambda>0$. Then for any $u \in H_{2}^{1}(M, g)$ the operator $\mathbb{L}_{g}$ satisfies
$$\left\|\mathbb{L}_{g}(u)\right\|_{L_{2}(M)} \geq C\|u\|_{L_{2}(M)}$$
for some constant $C>0$.
Corollary 4.4 There exists the Friedrichs' self-adjoint extension $\widetilde{\mathbb{L}}_{g}$ of the operator $\mathbb{L}_{g}$. The extension $\widetilde{\mathbb{L}}_{g}$ is semi-bounded with the same bounding constant. The range of $\widetilde{\mathbb{L}}_{g}$ coincides with $L_{2}(M)$.

Proof. This follows directly from 4.2 and the Neumann Theorem (see [7, Theorem 17]). \(\square\)

Corollary 4.5 The conformal Laplacian $\mathbb{L}_{g}$ is essentially self-adjoint, and its self-adjoint extension is unique.

Proof. It follows from the fact that $\mathbb{L}_{g}$ is strictly positive and symmetric, see [7, Theorems 28, 29]. \(\square\)

Remark. We have that the range $R\left(\widetilde{\mathbb{L}}_{g}\right)=L_{2}(M)$. Thus, the range $R\left(\mathbb{L}_{g}\right)$ is dense in $L_{2}(M)$. Thus, essential self-adjointness of $\mathbb{L}_{g}$ follows also from [21, Lemma 8.14]. A direct proof of the density of $R\left(\mathbb{L}_{g}\right)$ in $L_{2}(M)$ may be given following the proof (presented in [21, Chapter 8, Section 13]) for the Schrödinger operator $-\Delta+c(x)$. The latter one utilizes the asymptotic estimates of the Green function for $\mathbb{L}_{g}$ similar to one obtained by V. Maz'ya, S. Nasarow, B. Plamenewski (see [18]).

Theorem 4.6 Let $\Lambda>0$. Then the self-adjoint extension $\widetilde{\mathbb{L}}_{g}$ of the conformal Laplacian $\mathbb{L}_{g}$ has discrete positive spectrum of finite multiplicity.

Proof. We use compactness of the embedding $\mathcal{D}\left(\widetilde{\mathbb{L}}_{g}\right)=H_{2}^{2}(M, g) \subset L_{2}(M)$ and Rollich Theorem (see, say, [21, Theorem 3.3.]) to prove that the inverse operator $\widetilde{\mathbb{L}}_{g}^{-1}$ is compact and has discrete spectrum $\left\{\mu_{n}\right\}\left(\lambda_{n}^{-1}=\mu_{n} \rightarrow 0\right.$ as $n \rightarrow \infty$ ) of finite multiplicity. Also $\left\langle\mathbb{L}_{g} u, u\right\rangle \geq C\|u\|_{L_{2}(M)}$ gives that $\sigma\left(\widetilde{\mathbb{L}}_{g}\right) \subset \mathbf{R}_{+}$. \(\square\)

Remark. One can also prove that $\mathcal{D}\left(\widetilde{\mathbb{L}}_{g}\right)=H_{2}^{2}(M, g)$ using arguments similar to those used by H. Triebel [29, Theorem 6.4.1] for the operator $-\Delta+\chi^{2}$.
4.3. Proof of Theorem 4.2. The upper estimate follows from the symmetry of the form $\left\langle\mathbb{L}_{g} u, u\right\rangle$ and the definition of the Sobolev spaces.

For the proof of the lower estimate, consider first an arbitrary smooth function $u \in C_{*}^{\infty}(M)$. We have
$$\begin{aligned}
\left\langle\mathbb{L}_{g} u, u\right\rangle & =\int_{M}\left(-u \cdot \Delta_{g} u+\frac{n-2}{4(n-1)} R_{g} u^{2}\right) d \sigma_{g} \\
& =\int_{M}\left(\left|\nabla_{g} u\right|^{2}+\frac{n-2}{4(n-1)} R_{g} u^{2}\right) d \sigma_{g}
\end{aligned}$$
Here we use $u \in C_{*}^{\infty}(M)$, so $u$ is zero in some neighborhood of $x_{*}$. Indeed, let $u \equiv 0$ in $\{|\ell|, \nu\} \subset K \subset M$ for some $\nu$. Then $M \backslash\left\{|\ell|<\frac{\nu}{2}\right\}$ is a
manifold with the boundary $\left\{|\ell|=\frac{\nu}{2}\right\}$, and $u$ is zero in a neigborhood of this boundary.

We decompose $M$ as follows:
$$\begin{aligned}
& M=\left(M_{0} \cup B_{\sigma}\right) \cup\left(\left(B \backslash B_{\sigma}\right) \cup K\right), \text { with } \\
& B_{\sigma}=\left\{x=(r, \ell) \in C\left(S^{p} \times S^{q}\right)|\sigma-r \ell| \ell \mid<\sigma\right\},
\end{aligned}$$
so that the scalar curvature $R_{g} \geq R_{0}>0$ on $M_{0} \cup B_{\sigma}$, while on $\left(B \backslash B_{\sigma}\right) \cup K$ the metric $g$ may have nonpositive scalar curvature $R_{g}$ (satisfying the above "tame" conditions). We consider two cases: $\Lambda>0$ and $\Lambda \leq 0$.

Case $\Lambda>0$. We have assumed (see above ) that in this case $R_{g}>0$ everywhere on $M$, and $R_{g} \sim \chi^{2}$ in the neighborhood of $x_{*}$. In particular, scalar curvature is positive on the (compact) belt $B \backslash B_{\sigma}$. Thus, on $M_{0} \cup$ $\left(B \backslash B_{\sigma}\right)$ the scalar curvature is bounded from below by a positive constant. Using this we get the estimate
$$C_{1} \chi^{2} \leq R_{g} \leq C_{2} \chi^{2}$$
everywhere on $M$ (for some positive constants $C_{1}, C_{2}>0$ ). We multiply this inequality by $u^{2}$, then we integrate over $M$, and (13) implies
$$C_{1}\|u\|_{H_{2}^{1}(M)}^{2} \leq\left\langle\mathbb{L}_{g} u, u\right\rangle \leq C_{2}\|u\|_{H_{2}^{1}(M)}^{2}$$
for some positive constants $C_{1}, C_{2}>0$ as required.
Case $\Lambda \leq 0$. We use the above decomposition and (13) to write
$$\begin{aligned}
\left\langle\mathbb{L}_{g} u, u\right\rangle=\int_{M_{0} \cup B_{\sigma}} & \left(\left|\nabla_{g} u\right|^{2}+\frac{n-2}{4(n-1)} R_{g} u^{2}\right) d \sigma_{g} \\
+ & \int_{\left(B \backslash B_{\sigma}\right) \cup K}\left(\left|\nabla_{g} u\right|^{2}+\frac{n-2}{4(n-1)} R_{g} u^{2}\right) d \sigma_{g}=A+B .
\end{aligned}$$
We estimate the term $A$ :
$$A=\int_{M_{0} \cup B_{\sigma}}\left(\left|\nabla_{g} u\right|^{2}+\frac{n-2}{4(n-1)} R_{g} u^{2}\right) d \sigma_{g} \geq C \int_{M_{0} \cup B_{\sigma}}\left(\left|\nabla_{g} u\right|^{2}+\chi^{2} u^{2}\right) d \sigma_{g}$$
since $R_{g} \geq R_{0}>0$ on $M_{0} \cup B_{\sigma}$.

For the integral $B$ we have:
$$\begin{aligned}
B=\int_{K}\left(\left|\nabla_{g} u\right|^{2}+\right. & \left.\frac{n-2}{4(n-1)} R_{g} u^{2}\right) d \sigma_{g} \\
& +\int_{B \backslash B_{\sigma}}\left(\left|\nabla_{g} u\right|^{2}+\frac{n-2}{4(n-1)} R_{g} u^{2}\right) d \sigma_{g}=\mathbf{I}+\mathbf{J}
\end{aligned}$$
We start with the study of the integrands in the integral J. In the compact closure $\overline{B \backslash B_{\sigma}}$ we have the norms of the gradients of a function $u$ with respect to the metrics $g$ and $g_{K}$ :
$$\left\|\nabla_{g} u\right\|=g^{i j}(x) \xi_{i} \xi_{j},\left\|\nabla_{g_{K}} u\right\|=g_{K}^{i j}(x) \xi_{i} \xi_{j}, \xi_{i}=\partial_{i} u .$$
We notice that the ratio
$$\frac{\left\|\nabla_{g} u\right\|_{g} \sqrt{|g|}}{\left\|\nabla_{g_{K}} u\right\|_{g_{K}} \sqrt{\left|g_{K}\right|}}=\frac{g_{K}^{i j}(x) \xi_{i} \xi_{j} \sqrt{|g|}}{g_{K}^{i j}(x) \xi_{i} \xi_{j} \sqrt{\left|g_{K}\right|}}$$
is bounded from below by a positive constant $c$ on the compact set $\overline{B \backslash B_{\sigma}}$. One can take $c$ to be a minimum of the ratio taken over the compact subspace
$$(x, \xi) \in\left\{T\left(\overline{B \backslash B_{\sigma}}\right) \quad|\quad| \xi \mid=1\right\}$$
of the tangent bundle $T\left(\overline{B \backslash B_{\sigma}}\right)$. Thus, on the compact set $\overline{B \backslash B_{\sigma}}$ we have the bound
$$\left\|\nabla_{g} u\right\|_{g} \sqrt{|g|} \geq c\left\|\nabla_{g_{K}} u\right\|_{g_{K}} \sqrt{\left|g_{K}\right|}$$
for all $u$. At the same time on this compact set $\overline{B \backslash B_{\sigma}}$ we have
$$\frac{\ell^{2}\left|R_{g}\right| \sqrt{|g|}}{\sqrt{\left|g_{K}\right|}} \leq c_{1}$$
for some positive constant $c_{1}$ (since the functions $u$ are continuous and positive on this compact set). Thus, on this compact belt we have
$$R_{g} \sqrt{|g|} \geq c_{2} \frac{\Lambda}{\ell^{2}} \sqrt{\left|g_{K}\right|}, \quad \text { with some } c_{2}=\frac{c_{1}}{|\Lambda|}>0 .$$
Taking $c_{3}=\min \left(c, c_{2}\right)$ and combining the estimates (14), (15) we get
$$\left.\mathbf{J} \geq c_{3} \int_{B \backslash B_{\sigma}}\left[\left\|\nabla_{g_{K}} u\right\|^{2}+\frac{\Lambda}{\ell^{2}} u^{2}\right] \sqrt{\left|g_{K}\right|}\right] d x$$

Thus,
$$\left.B=\mathbf{I}+\mathbf{J} \geq c_{4} \int_{K \cap\left(B \backslash B_{\sigma}\right)}\left[\left\|\nabla_{g_{K}} u\right\|^{2}+\frac{\Lambda}{\ell^{2}} u^{2}\right] \sqrt{\left|g_{K}\right|}\right] d x$$
here $c_{4}=\min \left(1, c_{3}\right)>0$. Thus, we have estimated the integral $B$ from below by an integral over part of the cone, say $\ell \leq \varepsilon_{4}$, containing only standard conic metric.

Thus, we consider the quadratic form
$$\left\langle\mathbb{L}_{\text {cone }} u, u\right\rangle=\int_{[0, \varepsilon] \times S_{r p}^{p} \times S_{r_{q}}^{q}}\left[\left|\nabla_{\ell} u\right|^{2}-u \cdot\left(\Delta_{\theta}+\Delta_{\psi}\right) u+\frac{n-2}{4(n-1)} \frac{\Lambda}{\ell^{2}} u^{2}\right] \ell^{n-1} d \ell d \sigma_{\theta} d \sigma_{\psi}$$
on the space of functions obtained by restriction of functions from the space $H_{2}^{1}(M)$ to the subset $[0, \varepsilon] \times S_{r_{p}}^{p} \times S_{r_{q}}^{q} \subset M$ (with the conical standard metric) and the norm induced from $H_{2}^{1}(M)$.

Notice that each function from $H_{2}^{1}\left([0, \varepsilon] \times S_{r_{p}}^{p} \times S_{r_{q}}^{q}\right)$ can be extended to the function from $H_{2}^{1}(M)$ (see [7]). Therefore, by restricting functions from $M$ to the conical part we obtain the whole space $H_{2}^{1}\left([0, \varepsilon] \times S_{r_{p}}^{p} \times S_{r_{q}}^{q}\right)$.

Now we decompose the function $u$ into the Fourier series, using the coordinates $(\ell, \theta, \psi)$
$$u=\sum_{i, j} u_{i j}(\ell) \xi_{i}(\theta) \xi_{j}(\psi)$$
and use the notations:
$$u_{i j}:=u_{i j}(\ell), \quad u_{i j, \ell}:=\frac{\partial}{\partial \ell} u_{i j}(\ell), \quad u_{i j, \ell \ell}:=\frac{\partial^{2}}{\partial \ell^{2}} u_{i j}(\ell) .$$
We have
$$\begin{aligned}
& \quad-u \Delta_{\psi, \theta} u \\
& =-\left(\sum_{i, j} u_{i j} \xi_{i}(\theta) \xi_{j}(\psi)\right) \cdot\left(\sum_{i, j}\left[\frac{2 u_{i j}}{r_{p}^{2} \ell^{2}} \Delta_{\theta} \xi_{i}(\theta) \xi_{j}(\psi)+\frac{2 u_{i j} \xi_{i}(\theta)}{r_{q}^{2} \ell^{2}} \Delta_{\psi} \xi_{j}(\psi)\right]\right) \\
& =\left(\sum_{i, j} u_{i j} \xi_{i}(\theta) \xi_{j}(\psi)\right) \cdot\left(\sum_{i, j}\left[-\frac{2 u_{i j}}{r_{p}^{2} \ell^{2}} \lambda_{i}^{p} \xi_{i}(\theta) \xi_{j}(\psi)-\frac{2 u_{i j} \xi_{i}(\theta)}{r_{q}^{2} \ell^{2}} \lambda_{j}^{q} \xi_{j}(\psi)\right]\right) \\
& =\left(\sum_{i, j} u_{i j} \xi_{i}(\theta) \xi_{j}(\psi)\right) \cdot\left(\sum_{i, j}\left[\frac{2}{r_{p}^{2} \ell^{2}} \lambda_{i}^{p}+\frac{2}{r_{q}^{2} \ell^{2}} \lambda_{j}^{q}\right] u_{i j}(\ell) \xi_{i}(\theta) \xi_{j}(\psi)\right) .
\end{aligned}$$

Now we add the term
$$\left|\nabla_{r} u\right|^{2}+\frac{n-2}{4(n-1)} \frac{\Lambda}{\ell^{2}} u^{2},$$
to the last expression, where $u$ is decomposed into the same Fourier series by $\psi, \theta$. In particular, we have
$$\left|\nabla_{\ell} u\right|^{2}=\left|\sum_{i, j}\left[\nabla_{\ell} u_{i j}(\ell)\right] \xi_{i}(\theta) \xi_{j}(\psi)\right|^{2} .$$
Then we integrate the resulting expression over the product of spheres $S^{p} \times S^{q}$. We obtain
$$\left\langle\mathbb{L}_{\text {cone }} u, u\right\rangle=\int_{[0, \varepsilon]} \ell^{n-1} d \ell \sum_{i j}\left[u_{i j, \ell}^{2}+K_{i j} u_{i j}^{2}\right]=\sum_{i j} \int_{0}^{\varepsilon} \ell^{n-1} d \ell\left[u_{i j, \ell}^{2}+K_{i j} u^{2}\right],$$
where
$$K_{i j}=\frac{2 \lambda_{i}^{p}}{r_{p}^{2}}+\frac{2 \lambda_{j}^{q}}{r_{q}^{2}}+\frac{n-2}{4(n-1)} \Lambda .$$
The total quadratic form $\langle\mathbb{L} u, u\rangle$ is estimated from below by the integral over $M_{0}$ in $\langle\mathbb{L} u, u\rangle$ plus some positive constant times the form $\left\langle\mathbb{L}_{\text {cone }} u, u\right\rangle$ :
$$\langle\mathbb{L} u, u\rangle \geq c\left\langle\mathbb{L}_{\text {cone }} u, u\right\rangle+\int_{M_{0}}\left[|\nabla u|^{2}+R_{g} u^{2}\right] d \sigma_{g} .$$
Since $R_{g}>0$ on $M_{0}$, second term is always positive. This is not true for the first term. Take for example $u=u_{0}=$ const. This function belongs to the space $H_{2}^{1}(M)$ and $\left\langle\mathbb{L}_{\text {cone }} u_{0}, u_{0}\right\rangle=K_{00} u_{0}^{2} \frac{\varepsilon^{n}}{n}$, thus is negative for $\Lambda<0$, since $\lambda_{0}^{p}=\lambda_{0}^{q}=0$. This leads, therefore, to the following necessary condition for the form $\langle\mathbb{L} u, u\rangle$ to be positive (take $u=1$ ):
$$\int_{M} R_{g} d \sigma_{g}>0 .$$
Now we find a lower bound for the quadratic form values of
$$\int_{0}^{\varepsilon}\left[\ell^{n-1} v_{, \ell}^{2}+K \ell^{n-3} v^{2}\right] d \ell$$
on the space $H_{2}^{1}(0, \varepsilon)$. Later we will specialize the results to the cases $v=$ $u_{i j}, K=K_{i j}$.

Denote by $\bar{v}$ the function on $(0,1)$ obtained by the scaling $\ell=\varepsilon_{3} t$ : $v(\ell)=v\left(\varepsilon_{3} t\right)=\bar{v}(t)$. We have
$$\int_{0}^{\varepsilon}\left[v_{, \ell}^{2}+K v^{2} \ell^{-2}\right] \ell^{n-1} d \ell=\varepsilon^{n-2} \int_{0}^{1}\left[\bar{v}_{, t}^{2}+K \bar{v}^{2} t^{-2}\right] t^{n-1} d t$$
Change of variables $t=s^{a} ; d t=a s^{a-1} d s ; s=t^{\frac{1}{a}}$ gives
$$f_{, s}=f_{, t} t_{, s}=f_{, t} a s^{a-1} ; \quad f_{, t}=\frac{1}{a} s^{1-a} f_{, s} .$$
This leads to
$$\begin{aligned}
\int_{0}^{\varepsilon}\left[v_{, \ell}^{2}+K v^{2} \ell^{-2}\right] \ell^{n-1} d \ell & =\varepsilon^{n-2} \int s^{a(n-1)} a s^{a-1}\left[\frac{1}{a^{2}} s^{2(1-a)} \bar{v}_{, s}^{2}+K s^{-2 a} \bar{v}^{2}\right] d s \\
& =\varepsilon^{n-2} a \int s^{a(n-1)+a-1+2-2 a}\left[\frac{1}{a^{2}} \bar{v}_{, s}^{2}+K s^{-2} \bar{v}^{2}\right] d s \\
& =-(n-2) \varepsilon^{n-2} \int_{+\infty}^{1}\left[\bar{v}_{, s}^{2}+a^{2} K s^{-2} \bar{v}^{2}\right] d s \\
& =(n-2) \varepsilon^{n-2} \int_{1}^{+\infty}\left[\bar{v}_{, s}^{2}+\frac{K}{(n-2)^{2}} s^{-2} \bar{v}^{2}\right] d s
\end{aligned}$$
Here we took $a=-\frac{1}{n-2}$. Thus it is enough to give a lower bound for
$$\int_{1}^{+\infty}\left[\bar{v}_{, s}^{2}+K_{1} \bar{v}^{2}(s)\right] d s, \quad K_{1}=\frac{K}{(n-2)^{2}}$$
on the space of $H_{2}^{1}(1,+\infty)$ (with the norm defined by the same quadratic expression with $K_{1}=1$ ).

Functions from Sobolev space $H_{2}^{1}(1,+\infty)$ are continuous at $s=1$ and have the well-defined limit value $f(1)=\lim _{s \rightarrow 1} f(s)$. This value is the continuous linear functional on the space $H_{2}^{1}(1,+\infty)$. The kernel of this functional is the space $H_{2,0}^{1}(1, \infty)$ (which is the closure in $H_{2,0}^{1}(1, \infty)$ of the subspace $C_{0}^{\infty}(1, \infty)$ of smooth functions with compact support [7]). A function $f$ from $H_{2,0}^{1}$ has a canonical extension $\hat{f}$ by zero to the function in $H_{2}^{1}(0,+\infty)$ with the norm defined by the same quadratic form
$$\|\hat{f}\|^{2}=\int_{0}^{+\infty}\left[\hat{f}_{, s}^{2}+\hat{f}^{2}(s)\right] d s$$

Notice that the extension $\hat{f}$ has the same norm as the function $f$. For such a function, obtained by the extension to $(1, \infty)$ of a function from $H_{2,0}^{1}(1, \infty)$ and thus, being zero in a neighborhood of zero, we can use the simplest Hardy inequality (see [12]) to estimate
$$\int_{0}^{+\infty} \hat{f}^{2}(s) s^{-2} d s \leqq 4 \int_{0}^{+\infty} \hat{f}_{, s}^{2}(s) d s$$
Because of the construction of the extension we get a similar inequality with $f$ instead of $\hat{f}$ and the lower limit 1 replacing zero.

Using this estimate we get for $f \in H_{2,0}^{1}(1, \infty)$ and negative $K_{1}$ :
$$\int_{1}^{+\infty}\left[f_{, s}^{2}+K_{1} f^{2}(s)\right] d s \geq\left(1+4 K_{1}\right) \int_{1}^{+\infty} f_{, s}^{2} d s$$
Thus, if $1+4 K_{1}>0$, the quadratic form
$$K(f, f)=\int_{1}^{+\infty}\left[f_{, s}^{2}+K_{1} f^{2}(s)\right] d s$$
is positive definite on $H_{2,0}^{1}(1, \infty)$, where the norm induced from $H_{2}^{1}(1, \infty)$, is equivalent to the norm $\int_{1}^{+\infty} f_{, s}^{2} d s$ (this follows from the Hardy inequality). Applying this to the case where $K=K_{i j}$ we see that it is sufficient to check this condition for the case $i=j=0$ (since $\lambda_{i}^{p}, \lambda_{j}^{q}>0$ ). For $i=j=0$,
$$K_{1}=\frac{K}{(n-2)^{2}}=\frac{\Lambda}{4(n-1)(n-2)} .$$
Therefore
$$1+4 K_{1}=1+4 \frac{\Lambda}{4(n-1)(n-2)}=1+\frac{\Lambda}{(n-1)(n-2)}=\mu^{2}>0,$$
see Appendix. Therefore, on the subspace $H_{2,0}^{1}(1, \infty)$ the quadratic form $K(f, f)$ is positive definite.

To determine what happens at the complement to this subspace and to estimate our quadratic form from below we return to the quadratic form on the space $H_{2}^{1}(0, \varepsilon)$ with the (square) of the norm
$$\int_{0}^{\varepsilon} \ell^{n-1}\left(v_{, \ell}^{2}+\ell^{-2} v^{2}\right) d \ell=\left\|v_{, \ell}\right\|_{L_{2}\left(0, \varepsilon ; \ell^{n-1} d \ell\right)}^{2}+\left\|\ell^{-1} v\right\|_{L_{2}\left(0, \varepsilon ; \ell^{n-1} d \ell\right)}^{2} .$$

Let $K \leqq 0$. To find the lowest eignevalue of the quadratic form
$$\int_{0}^{\varepsilon} \ell^{n-1}\left(v_{, \ell}^{2}+K \ell^{-2} v^{2}\right) d \ell$$
we calculate the minimum of the following fraction
$$\min _{u \neq 0} \frac{\left\|u_{, s}\right\|_{L_{2}}+K\left\|s^{-1} u\right\|_{L_{2}}}{\left\|u_{, s}\right\|_{L_{2}}+\left\|s^{-1} u\right\|_{L_{2}}}$$
over $u \in H_{2}^{1}(0, \varepsilon)$. We write this relation as
$$\frac{f(u)+K}{f(u)+1}, \quad \text { with } \quad f(u)=\frac{\left\|v_{, l}\right\|_{L_{2}\left(0, \varepsilon ; \ell^{n-1} d \ell\right.}^{2}}{\left\|\ell^{-1} v\right\|_{L_{2}\left(0, \varepsilon ; \ell^{n-1} d \ell\right.}^{2}} .$$
Now we notice that the function
$$s \rightarrow \frac{s+K}{s+1}$$
is increasing for $K \leqq 0$ and for $s \geqq 0$ takes its minimal value (equal to $K)$ at $s=0$. On the other hand $f(u)$ is well defined for all $u \in H_{2}^{1}(0, \varepsilon)$, $u \neq 0$, (since its denominator cannot be zero for $u \neq 0$ ). The function $f(u)$ is nonnegative and is equal to zero only if $u_{, \ell}=0$, i.e. for constant functions $u=$ const .

Therefore, the quadratic form
$$\int_{0}^{\varepsilon} \ell^{n-1}\left(v_{, \ell}^{2}+K \ell^{-2} v^{2}\right) d \ell$$
has $K$ as its minimal eigenvalue and the constant $u_{0}=\sqrt{\frac{n-2}{\varepsilon^{n-2}}}$ as its eigenvector of unit norm, corresponding to this eigenvalue.

As a result, the condition $\Lambda>0$, or, what is the same, $\mu>1$ is sufficient for the total quadratic form $L$, and the operator $\mathbb{L}_{g}$ to be positive definite. Recall that we have
$$\begin{aligned}
\langle\mathbb{L} u, u\rangle & \geq c\left\langle\mathbb{L}_{\text {cone }} u, u\right\rangle+\int_{M_{0}}\left[|\nabla u|+R_{g} u^{2}\right] d \sigma_{g} \\
& =\sum_{i j} \int^{\varepsilon} \ell^{n-1}\left[u_{i j}^{2}+K_{i j} u^{2}\right]+\int_{M_{0}}\left[|\nabla u|+R_{g} u^{2}\right] d \ell d \sigma_{g} .
\end{aligned}$$

The integral over $M_{0}$ is always nonnegative. In the sum, terms for which $K_{i j} \geq 0$ are also nonnegative. Since
$$K_{i j}=\frac{2 \lambda_{i}^{p}}{r_{p}^{2}}+\frac{2 \lambda_{j}^{q}}{r_{q}^{2}}+\frac{n-2}{4(n-1)} \Lambda=\frac{2 \lambda_{i}^{p}}{r_{p}^{2}}+\frac{2 \lambda_{j}^{q}}{r_{q}^{2}}+\frac{(n-2)^{2}\left(\mu^{2}-1\right)}{4},$$
for $p, r_{p}, q, r_{q}$ fixed, all the terms in the sum over $i, j$ are nonnegative except a finite number of them.

More than this, each term in the sum (quadratic form) for which $K_{i j} \leqq$ 0 has one and only one nonpositive eigenvalue with constant eigenfunction. For the form $\mathbb{L}_{\text {cone }}$ on $H_{2}^{1}\left((0, \varepsilon) \times S^{p} \times S^{q}\right)$ this corresponds to the function(s) $u_{i j}=c_{i j} \xi_{i}^{p}(\theta) \xi_{j}^{q}(\psi)$ with some constants $c_{i j}$. The condition $K_{i j} \leqq 0$ can be rewritten as follows
$$\frac{\lambda_{i}^{p}}{r_{p}^{2}}+\frac{\lambda_{j}^{q}}{r_{q}^{2}} \leqq \frac{(n-2)}{(n-1)}|\Lambda|$$
and the number of negative modes of the form $\mathbb{L}_{\text {cone }}$ can be found from here. Notice, in particular, that if $\Lambda<0$, then for $i, j=0$ that condition is always satisfied; thus, there is at least one negative mode for $\mathbb{L}_{\text {cone }}$. That does not prevent, though, this negative input in the whole form $\langle\mathbb{L} u, u\rangle$ from being compensated by the input of the $M_{0}$-part.

We also notice that as it follows from the proof, in the case where $\Lambda \leqq 0$, there is the lower bound for the form $\langle\mathbb{L} u, u\rangle$, i. e.
$$\langle\mathbb{L} u, u\rangle \geqq D\|u\|_{H_{2}^{1}(M)} .$$
Here $D$ is a finite constant, and
$$|D| \leq \frac{4(n-2)}{n-2}|\Lambda| c_{4},$$
where $c_{4}$ is the constant above. This proves Theorem 4.2. \(\square\)
4.4. Necessary condition for positivity of $\langle\mathbb{L} u, u\rangle$. We examine the case when $\Lambda \leq 0$ but $K_{i j}>0$ for all $i>0$ and $j>0$. Since
$$\Lambda=-(n-1)(n-2)+\frac{2 p(p-1)}{r_{p}^{2}}+\frac{2 q(q-1)}{r_{q}^{2}},$$
then the condition $\Lambda \leq 0$ is equivalent to
$$\frac{(n-1)(n-2)}{2} \geq \frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}} .$$

On the other hand the conditions $K_{10}>0$ and $K_{01}>0$ imply that $K_{i j}>0$ for all $i>0$ and $j>0$. We recall that zero has multiplicity 1 for $\Delta_{\theta}$ and $\Delta_{\psi}$, and the next eigenvalue is $p$ for $\Delta_{\theta}$ and $q$ for $\Delta_{\psi}$ respectively. This gives that $K_{10}>0$ is equivalent to
$$\frac{2 p}{r_{p}^{2}}+\frac{(n-2)^{2} \Lambda}{4(n-1)(n-2)}>0 \quad \text { or } \quad \Lambda>-\frac{8(n-1)}{n-2} \cdot \frac{p}{r_{p}^{2}} .$$
We use the above formula for $\Lambda$ to get that
$$K_{10}>0 \Longleftrightarrow \frac{4(n-1)}{n-2} \cdot \frac{p}{r_{p}^{2}}+\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}>\frac{(n-1)(n-2)}{2}$$
Similarly,
$$K_{01}>0 \Longleftrightarrow \frac{4(n-1)}{n-2} \cdot \frac{q}{r_{q}^{2}}+\frac{p(p-1)}{r_{p}^{2}}+\frac{q(q-1)}{r_{q}^{2}}>\frac{(n-1)(n-2)}{2}$$
We have proved the following.
Proposition 4.7 Assume $\Lambda \leq 0$ (which is equivalent to (16)) and the conditions (17), (18) are satisfied. Then the form $\langle\mathbb{L} u, u\rangle$ is positive if and only if
$$\int_{M} R_{g} d \sigma_{g}>0 .$$

\section*{5 Weak Yamabe Theorem}
5.1. Yamabe functional. Now we define the Yamabe functional on $M$ and study its properties. Let $\alpha \in\left[1, \alpha^{*}\right]$, where $\alpha^{*}=\frac{n+2}{n-2}$. For each $\alpha$ we consider the functional
$$\begin{gathered}
I_{\alpha}(\varphi)=\frac{E(\varphi)}{\left(\int_{M}|\varphi|^{\alpha+1} d V_{g}\right)^{\frac{2}{\alpha+1}}}, \quad \varphi \in H^{1}\left(M, d V_{g}\right), \quad \varphi \neq 0 \\
E(\varphi)=\int\left(|\nabla \varphi|^{2}+\frac{n-2}{4(n-1)} R_{g} \varphi^{2}\right) d V_{g}
\end{gathered}$$
This is the Yamabe functional if $\alpha=\alpha^{*}$. One can prove the following fact by using Theorem 3.3.

Proposition 5.1 The functional $I_{\alpha}: H_{2}^{1}(M, g) \longrightarrow \mathbf{R}$ is defined and continuous on the space $H_{2}^{1}(M, g)$ for all $\alpha \in\left[1, \alpha^{*}\right)$.

We denote by $C_{\mu}$ the norm of the embedding $H_{2}^{1}(M) \subset L_{\mu}(M)$, i.e.
$$C_{\mu}=\inf _{\substack{\varphi \neq 0 \\ \varphi \in H_{2}^{1}(M)}} \frac{\|\varphi\|_{L_{\mu}}}{\|\varphi\|_{H_{2}^{1}}},$$
where it is assumed that $\mu \leq 1+\alpha^{*}$.
Proposition 5.2 Let $\Lambda>0$. Then the functional $I_{\alpha}$ is bounded from below, i.e. for all $\varphi \in H_{2}^{1}(M), \varphi \neq 0$ we have
$$I_{\alpha}(\varphi) \geq \frac{C_{1}}{C_{\alpha+1}^{2}}$$
with the constant $C_{1}>0$ given in Theorem 4.2, and $C_{\alpha+1}$ as above.
Proof. Theorem 4.2 gives that $\left\langle\mathbb{L}_{g} u, u\right\rangle \geq C_{1}\|u\|_{H_{2}^{1}}^{2}$. Thus
$$I_{\alpha}(\varphi)=\frac{\left\langle\mathbb{L}_{g} \varphi, \varphi\right\rangle}{\|\varphi\|_{L_{\alpha+1}}^{2}} \geq \frac{C_{1}\|\varphi\|_{H_{2}^{1}}^{2}}{\|\varphi\|_{L_{\alpha+1}}^{2}}$$
for any $\varphi \in C_{*}^{\infty}(M)$. The embedding Theorem 3.3 gives the continuous embedding $H_{2}^{1}(M) \subset L_{\alpha+1}(M)$ with $\alpha \leq \alpha^{*}$, and $\|\varphi\|_{L_{\alpha+1}} \leq C_{\alpha+1}\|\varphi\|_{H_{2}^{1}}$. Thus
$$\frac{\|\varphi\|_{H_{2}^{1}}^{2}}{\|\varphi\|_{L_{\alpha+1}}^{2}} \geq \frac{1}{C_{\alpha+1}} \quad \text { giving } \quad I_{\alpha}(\varphi) \geq \frac{C_{1}}{C_{\alpha+1}^{2}} .$$
Since the space $C_{*}^{\infty}(M)$ is dense in $H_{2}^{1}(M)$, it gives the result. \(\square\)

Here is the "easy" version of the Yamabe theorem. To prove it we follow the course of the corresponding result for closed manifolds, see [4, Theorem 5.5].

Theorem 5.3 Let $M$ be a compact closed manifold with a metric $g$ and a conical singularity as above. Let $\Lambda>0$. For any $\alpha \in\left[1, \alpha^{*}\right)$ there exists a function $u_{\alpha} \geq 0$ minimizing the functional $I_{\alpha}$, so that
$$\begin{aligned}
& \int_{M} u_{\alpha}^{\alpha+1} d V_{g}=1 \\
\text { giving } \quad I_{\alpha}\left(u_{\alpha}\right)= & \min \left\{I_{\alpha}(\varphi) \mid \varphi \in H_{2}^{1}(M), \varphi \neq 0\right\} .
\end{aligned}$$

Denote this value $Q_{\alpha}=I_{\alpha}(M,[g])=I_{\alpha}\left(u_{\alpha}\right)$. The function $u_{\alpha}$ is a weak (in $\left.H_{2}^{1}(M)\right)$ solution of the equation:
$$-\Delta u_{\alpha}+\frac{n-2}{4(n-1)} R_{g} u_{\alpha}=Q_{\alpha} u_{\alpha}^{\alpha} .$$
5.1. Proof of Theorem 5.3. (a) First we prove that the functional $I_{\alpha}$ is bounded, and thus $Q_{\alpha}$ is finite. Let $q=1+\alpha, 2 \leq q<1+\alpha^{*}$. The conformal Laplacian $\mathbb{L}_{g}$ is positive by Theorem 4.2 (Recall that $\Lambda>0$ ). Thus $I_{\alpha}(\varphi) \geq 0$ for any $\varphi \in H_{2}^{1}(M, g)$, therefore $Q_{\alpha} \geq 0$ (moreover, $Q_{\alpha}>$ $\frac{C_{1}}{C_{\alpha+1}^{2}}$, see Proposition 5.2). On the other hand,
$$\begin{aligned}
Q_{\alpha} \leq I_{\alpha}(1) & =\frac{n-2}{4(n-1)} \int_{M} R_{g} d \sigma_{g} \\
& =\frac{n-2}{4(n-1)} \int_{M \backslash K} R_{g} d \sigma_{g}+\frac{n-2}{4(n-1)} \int_{K} R_{g} d \sigma_{g} .
\end{aligned}$$
The first integral on the right is bounded since $R_{g}$ is continuous in $M \backslash\left\{x^{*}\right\}$. The second integral is bounded since $n>2$ and
$$R_{r} \sim \frac{C}{\ell^{2}} \text { as } \ell \rightarrow 0, \text { and } \int_{0}^{\varepsilon_{0}} \ell^{n-3} d \ell<\infty .$$
(a') Now we have that $\operatorname{Vol}_{g}(M)<\infty$, and $1 \in L_{s}(M)$ for any $s \geq 2$. Thus we use the inequality
$$\int_{M} f g d \sigma_{g} \leq\left(\int_{M} f^{s} d \sigma_{g}\right)^{1 / s}\left(\int_{M} g^{s^{\prime}} d \sigma_{g}\right)^{1 / s^{\prime}}$$
(which holds for positive functions $f \in L_{s}(M), g \in L_{s}^{\prime}(M)$, with $\frac{1}{s}+\frac{1}{s^{\prime}}=1$, $\left.s, s^{\prime}>0\right)$. We apply this for $f=\varphi^{q}, g=1, s=\frac{q}{2}, s^{\prime}=\frac{q}{q-2}>0$. Thus we get
$$\begin{aligned}
& \int_{M} \varphi^{2} \cdot 1 d \sigma_{g} \leq\left(\int_{M}\left(\varphi^{2}\right)^{\frac{q}{2}} d \sigma_{g}\right)^{\frac{2}{q}} \cdot\left(\int_{M} 1^{\frac{q}{q-2}} d \sigma_{g}\right)^{\frac{q-2}{q}}, \quad \text { or } \\
& \|\varphi\|_{L_{2}(M)}^{2} \leq\|\varphi\|_{L_{q}(M)}^{2} \cdot\left(\operatorname{Vol}_{g}(M)\right)^{\frac{q-2}{q}}, \quad \text { so } \\
& \|\varphi\|_{L_{2}(M)} \leq\|\varphi\|_{L_{q}(M)} \cdot\left(\operatorname{Vol}_{g}(M)\right)^{\frac{q-2}{2 q}} .
\end{aligned}$$
(b) Now let $\left\{\varphi_{i}\right\}$ be a minimizing sequence such that
$$\int_{M} \varphi_{i}^{q} d \sigma_{g}=1, \quad \varphi_{i} \in H_{2}^{1}(M, g), \quad \text { and } \quad \lim _{i \rightarrow \infty} I_{\alpha}\left(\varphi_{i}\right)=Q_{\alpha} .$$
First we prove that the set $\left\{\varphi_{i}\right\}$ is bounded in $H_{2}^{1}(M, g)$. We have
$$\begin{aligned}
\left\|\varphi_{i}\right\|_{H_{2}^{1}(M)} & =\left\|\nabla \varphi_{i}\right\|_{L_{2}(M)}^{2}+\left\|\chi \varphi_{i}\right\|_{L_{2}(M)}^{2} \\
& =I_{\alpha}\left(\varphi_{i}\right)-\frac{n-2}{4(n-1)} \int_{M} R_{g} \varphi_{i}^{2} d \sigma_{g}+\int_{M} \chi^{2} \varphi_{i}^{2} d \sigma_{g} .
\end{aligned}$$
Since $\left\{\varphi_{i}\right\}$ is a minimizing sequence, we can assume that $I_{\alpha}\left(\varphi_{i}\right) \leq Q_{\alpha}+1$.
Now we consider the case when $R_{g}>0$ everywhere (i.e. $\Lambda>0$ ). Then we have that $R_{g}=\frac{\Lambda}{\ell^{2}}$ on the cone $K$, thus $\chi^{2}(x)<C R_{g}(x)$ for some positive constant $C$ and any $x \in M$. The sum of the first two terms in (19) coincides with $\left\|\nabla \varphi_{i}\right\|_{L_{2}(M)}^{2}$, so it is positive. Therefore
$$\left\|\varphi_{i}\right\|_{H_{2}^{1}(M)} \leq A \cdot I_{\alpha}\left(\varphi_{i}\right)-A \cdot \frac{n-2}{4(n-1)} \int_{M} R_{g} \varphi_{i}^{2} d \sigma_{g}+C \int_{M} R_{g} \varphi_{i}^{2} d \sigma_{g}$$
for any $A \geq 1$. We choose $A$ large enough, so that
$$C-A \frac{n-2}{4(n-1)}<0,$$
to get the estimate
$$\left\|\varphi_{i}\right\|_{H_{2}^{1}(M)} \leq A \cdot I_{\alpha}\left(\varphi_{i}\right) \leq A \cdot\left(Q_{\alpha}+1\right) .$$
Notice that on $M \backslash K$ both integrals are estimated by the norm $\|\varphi\|_{L_{2}(M)}$.
(c) We follow the proof of (c) in [4, Theorem 5.5] to find a subsequence $\left\{\varphi_{j}\right\}$ of $\left\{\varphi_{i}\right\}$ and a nonnegative function $u_{\alpha} \in H_{2}^{1}(M)$ such that
\begin{itemize}
\item[] ( $\alpha$ ) $\varphi_{j} \rightarrow u_{\alpha}$ in $L_{\alpha+1}(M)$;
\item[] ( $\beta$ ) $\varphi_{j} \rightarrow u_{\alpha}$ weakly in $H_{2}^{1}(M)$;
\item[] ( $\gamma$ ) $\varphi_{j} \rightarrow u_{\alpha}$ almost everywhere.
\end{itemize}

One may satisfy $(\gamma)$ since $L_{\alpha+1}(M) \subset L_{2}(M)$ continuously and any sequence converging in $L_{2}(M)$ has a subsequence that converges almost everywhere. To satisfy $(\beta)$ one uses that the embeddings $H_{1}^{2}(M) \subset L_{\alpha+1}(M) \subset$ $L_{2}(M) \subset H_{2}^{1}(M)$ are continuous. Then $u_{\alpha} \in H_{1}^{1}(M)$ because of weak compactness in reflexible Banach spaces, see [32, Chapter V, Section 2]. Finally [32, Chapter V, Section 1] gives
$$\left\|u_{\alpha}\right\|_{H_{1}^{1}} \leq \lim _{j \rightarrow \infty}=\inf \left\|\varphi_{j}\right\|_{H_{1}^{1}} .$$
This proves (c).
(d) Here we prove that $u_{\alpha}$ is a weak solution of the Yamabe equation. It means that for all $\varphi \in H_{2}^{1}(M)$
$$\int_{M}\left(\nabla u_{\alpha}\right) \cdot(\nabla \varphi) d \sigma_{g}+\frac{n-2}{4(n-1)} \int_{M} R_{g} u_{\alpha} \varphi d \sigma_{g}=Q_{\alpha} \int_{M} u_{\alpha}^{\alpha} \varphi d \sigma_{g} .$$
The proof is literally the same as in [4, Theorem 5.5]. The only difference is the use of the space $C_{*}^{\infty}(M)$ instead of $C_{0}^{\infty}(M)$. This ends the proof of theorem 5.3 for $\lambda>0$. \(\square\)

Corollary 5.4 The solution $\varphi_{\alpha} \neq 0$ on $M_{*}$.
Remark. We will see later, in Secion 7, that there are cases where the minimizer (Yamabe solution) belongs to the space $H_{2}^{1}(M)$ but not to $H_{2}^{2}(M)$. This is very different from the case of compact manifolds (cf. [3]).

Remark. The case $\Lambda \leq 0$ is also very interesting. One can prove the result similar to Theorem 5.3 under the same restrictions as in Proposition 4.7.

\section*{6 Asymptotic of solutions: the linear case}

In this section we study the asymptotic behavior of solutions of the linear equation $\mathbb{L}_{g} u=Q_{1} u$ near the point $x_{*}$. We use the polar coordinates $(\ell, \theta, \varphi)$ on the conical part $K$. Then the equation $\mathbb{L}_{g} u=Q_{1} u$ has the form
$$\left(\frac{\partial}{\partial \ell^{2}}+\frac{n-1}{\ell} \frac{\partial}{\partial \ell}+\frac{2}{r_{r}^{2} \ell^{2}} \Delta_{\theta}+\frac{2}{r_{q}^{2} \ell^{2}} \Delta_{\psi}\right) u+\left[-\frac{n-2}{4(n-1)} \frac{\Lambda}{\ell^{2}}+Q_{1}\right] u=0 .$$
First, we recall some basic information on the Laplacian operator on spheres ([11]). Let $\left\{\lambda_{j}^{p}, \chi_{j}^{p}\right\}$ be the spectrum of the Laplacian $\Delta_{S^{p}}=-\Delta_{\theta}$, and,
respectively, $\left\{\lambda_{i}^{q}, \chi_{i}^{q}\right\}$ of $\Delta_{S^{q}}=-\Delta_{\psi}$. It is well-known ([11]) that
$$\begin{aligned}
& \lambda_{0}^{p}=0, \quad \lambda_{1}^{p}=\cdots \lambda_{p+1}^{p}=p, \quad \lambda_{p+2}^{p}=2(p+1), \ldots, \\
& \lambda_{0}^{q}=0, \quad \lambda_{1}^{q}=\cdots \lambda_{q+1}^{q}=q, \quad \lambda_{q+2}^{q}=2(q+1), \ldots .
\end{aligned}$$
Any $L^{2}$-function on $S^{p}$ (correspondingly on $S^{q}$ ) decomposes into Fourier series with respect to the orthonormal basis $\left(\chi_{i}^{p}\right)$ (correspondingly $\left(\chi_{j}^{q}\right)$ ). On the cone $K$ we have
$$u(\ell, \theta, \psi)=\sum_{i j} u_{i j}(\ell) \chi_{i}^{p}(\theta) \chi_{j}^{q}(\psi) .$$
We decompose $u$ as in (21) to obtain the following system of equations for the coefficient functions $u_{i j}(\ell)$ on the half-line $\ell \geq 0$ :
$$\begin{gathered}
\frac{\partial^{2} u_{i j}}{\partial \ell^{2}}+\frac{n-1}{\ell} \frac{\partial u_{i j}}{\partial \ell}+\left[Q_{1}-\left(\frac{n-2}{4(n-1)} \Lambda+\frac{2}{r_{p}^{2}} \lambda_{i}^{p}+\frac{2}{r_{q}^{2}} \lambda_{j}^{q}\right) \frac{1}{\ell^{2}}\right] u_{i j}=0, \quad \text { or } \\
\frac{\partial^{2} u_{i j}}{\partial \ell^{2}}+\frac{n-1}{\ell} \frac{\partial u_{i j}}{\partial \ell}+\left[Q_{1}-\frac{K_{i j}}{\ell^{2}}\right] u_{i j}=0 . \\
\text { with } K_{i j}=\frac{n-2}{4(n-1)} \Lambda+\frac{2}{r_{p}^{2}} \lambda_{i}^{p}+\frac{2}{r_{q}^{2}} \lambda_{j}^{q} .
\end{gathered}$$
The equations (22) are known as degenerate hypergeometric or Whitteker equations (see [8, Vol. 1, Chapter 6]). Such an equation can be reduced, via an appropriate substitution, to the Bessel equations with the pure imaginary parameter $\nu$. Their solutions can be explicitly written in terms of the corresponding Bessel functions.

Here we are interested in asymptotic behavior of solutions as $\ell \rightarrow 0$. Thus, we are looking for solutions in the form of power series
$$u_{i j}=\ell^{\nu_{i j}} \sum_{k=0}^{\infty} a_{k} \ell^{k} .$$

We have the first and the second derivatives:
$$\begin{aligned}
u_{i j}^{\prime} & =\nu_{i j} \ell^{\nu_{i j}-1} \sum_{k=0}^{\infty} a_{k} \ell^{k}+\ell^{\nu_{i j}} \sum_{k=0}^{\infty}(k+1) a_{k+1} \ell^{k}, \\
u_{i j}^{\prime \prime} & =\nu_{i j}\left(\nu_{i j}-1\right) \ell^{\nu_{i j}-2} \sum_{k=0}^{\infty} a_{k} \ell^{k}+2 \nu_{i j} \ell^{\nu_{i j}-1} \sum_{k=0}^{\infty}(k+1) a_{k+1} \\
& \left.=\ell^{k}+\ell^{\nu_{i j}} \sum_{k=0}^{\infty}\right)(k+2)(k+1) a_{k+2} \ell^{k} .
\end{aligned}$$
We collect the coefficients for the different powers of $\ell$ in the equation (22):
$$\begin{array}{lll}
\ell^{\nu_{i j}-2} & : & \nu_{i j}\left(\nu_{i j}-1\right) a_{0}+(n-1) \nu_{i j} a_{0}-K_{i j} a_{0}=0, \\
\ell^{\nu_{i j}-1} & : & \nu_{i j}\left(\nu_{i j}-1\right) a_{1}+2 \nu_{i j} a_{1}+(n-1)\left(\nu_{i j}+1\right) a_{1}-K_{i j} a_{1}=0 .
\end{array}$$
For the (general) coefficient of $\ell^{\nu_{i j}+m}$ we obtain the following equation:
$$\begin{aligned}
\ell^{\nu_{i j}+m}: & \nu_{i j}\left(\nu_{i j}-1\right) a_{m+2}+2 \nu_{i j}(m+2) a_{m+2}+(m+2)(m+1) a_{m+2} \\
& +(n-1)\left(\nu_{i j}+m+2\right) a_{m+2}+Q_{1} a_{m}-K_{i j} a_{m+2}=0 .
\end{aligned}$$
Thus we get the recursive equation for the coefficients $a_{m}$ which we denote by $\left(Y_{m+2}\right)$ :
$$\left[\left(\nu_{i j}+m+2\right)^{2}+(n-2)\left(\nu_{i j}+m+2\right)-K_{i j}\right] a_{m+2}=-Q_{1} a_{m} \quad\left(Y_{m+2}\right)$$
Denote by $K_{\nu_{i j}+m}$ the left side of the previous equation. We consider the equation $\left(Y_{0}\right)$ :
$$\left(\nu_{i j}^{2}+(n-2) \nu_{i j}-K_{i j}\right) a_{0}=0 .$$
Here we have either $a_{0}=0$ or
$$\nu_{i j}^{(e, \pm)}=-\frac{n-2}{2} \pm \sqrt{\left(\frac{n-2}{2}\right)^{2}+K_{i j}} .$$
The second equation $\left(Y_{1}\right)$ is as follows:
$$\left(\nu_{i j}^{2}+n \nu_{i j}+\left(n-1-K_{i j}\right)\right) a_{1}=0 .$$