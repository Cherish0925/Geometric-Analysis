---
retention_scope: session
part: 2
total_parts: 2
---

[Part 2/2 of: The symplectic and twistor geometry of the general isomonodromic deformation problem]

The eigenvalues $\lambda_{i}$ of $A_{-r-1}$ determine a sequence of Stokes' rays through the origin, on which $\operatorname{Re}\left(z^{-r}\left(\lambda_{i}-\lambda_{j}\right)\right)$ changes sign for some pair of eigenvalues. Given a pair of consecutive rays (in order around the unit circle), with arguments $\theta_{1}, \theta_{2}$, we define a sector $\mathcal{S}$ by
$$\mathcal{S}=\left\{z \mid \theta_{1}-\pi / 2 r<\arg (z)<\theta_{2}+\pi / 2 r\right\} .$$
For each such sector $\mathcal{S}$, there is a unique special solution
$$y_{\mathcal{S}}=g_{\mathcal{S}}(z) \exp \left(t z^{-r}+m \log z\right),$$
such that $g_{\mathcal{S}} \sim g_{\mathrm{f}}$ as $z \rightarrow 0$ in $\mathcal{S}$. (See, for example, Boalch 2000 for a careful account of this proposition).

The solutions $y_{\mathcal{S}}$ are independent of the choice of coordinate (as maps $D \rightarrow$ $G)$. They are uniquely determined in each sector by the choice of $g_{0}$. So, as sections of the principal bundle over each sector, they are determined uniquely by the choice of the frame at the origin in which $A_{-r-1}$ is diagonal.

\section*{Regular singularities}

In the regular case $(r=0)$, (18) still holds, with $t=0$, provided that the eigenvalues of $A_{-1}$ are distinct. The formal series for $g$ can be found provided that, in addition, no two eigenvalues differ by an integer. It then necessarily converges, so $y_{\mathrm{f}}$ is a solution.

\section*{Global systems}

Let $X$ be a compact Riemann surface. For each $k$-tuple $\mathbf{r}=\left(r_{1}, \ldots, r_{k}\right)$ of nonnegative integers, we denote by $\mathcal{D}_{\mathbf{r}}(X, E)$, or simply by $\mathcal{D}_{\mathbf{r}}$, the space of meromorphic $\operatorname{sl}(n, \mathbb{C})$-connections $\nabla=\mathrm{d}+\alpha$ on the trivial vector bundle $E=$ $X \times \mathbb{C}^{n}$ with $k$ poles of order (at most) $r_{1}+1, \ldots, r_{k}+1 .{ }^{8}$

If we choose a local trivialization and a coordinate $z$ that vanishes at one of the poles, a connection $\nabla \in \mathcal{D}_{\mathbf{r}}$ is given in a neighbourhood of the pole by (17). ${ }^{9}$

\section*{The monodromy representation}

A local $G$-valued solution $y$ to the equation $\mathrm{d}+\alpha y=0$ can be continued analytically: it is singular at the poles, and multi-valued (single-valued on the covering space of the complement of the poles). If
$$\gamma:[0,1] \rightarrow \mathbb{C} \mathbb{P}_{1} \backslash\left\{a_{1}, \ldots, a_{k}\right\}, \quad \gamma(0)=\gamma(1)=z_{0},$$
is a closed loop and $z_{0}$ is some fixed base point, then we have $y(\gamma(1))=M_{\gamma} \in G$ for some monodromy matrix $M_{\gamma}$ which depends only on the homotopy class of $\gamma$.

Definition 3 The monodromy representation of (2) is the homomorphism
$$\pi_{1}\left(\mathbb{C} \mathbb{P}_{1} \backslash\left\{a_{1}, \ldots, a_{k}\right\}\right) \rightarrow G:[\gamma] \mapsto M_{\gamma} .$$
The monodromy representation is independent of $z_{0}$ and the choice of $y$ up to conjugation by a fixed element of $G$.

\section*{Deformations}

Definition 4 Let $\nabla_{0}, \nabla_{1} \in \mathcal{D}_{\mathbf{r}}(X)$. A deformation of $\nabla_{0}$ into $\nabla_{1}$ is a smooth path $\nabla_{t} \in \mathcal{D}_{\mathbf{r}}(X), t \in[0,1]$, from $\nabla_{0}$ to $\nabla_{1}$.

We are interested in the deformations of a connection $\nabla_{0}$ into a second $\nabla_{1}$ (or equivalently of $\alpha_{0}$ into $\alpha_{1}$ ) while preserving certain properties of the corresponding linear system.

Proposition 10 A deformation $\nabla_{t}$ has constant monodromy representation (up to conjugation) if and only if
$$\frac{\mathrm{d} \nabla_{t}}{\mathrm{~d} t}=\nabla_{t} \Omega_{t}$$
for some family of holomorphic maps $\Omega_{t}$ (depending smoothly on $t$ ) from the complement of the poles of $\nabla_{t}$ in $X$ into $\mathfrak{g}$.

\footnotetext{
${ }^{8}$ Note that $\alpha$ determines a holomorphic map $X \rightarrow \mathbb{P} \mathfrak{g}$
${ }^{9}$ When $X=\mathbb{C} \mathbb{P}_{1}$, we have $\alpha=-A \mathrm{~d} z$, where $z$ is a stereographic coordinate and $A$ is defined globally as a rational section of $\mathfrak{g} \otimes \mathcal{O}(-2)$. If all its singularities are at finite values of $z$, then $A$ has $N$ poles and $A=O\left(z^{-2}\right)$ as $z \rightarrow \infty$; but if one of the singularities is at infinity, then $A=O\left(z^{r-1}\right)$ as $z \rightarrow \infty$, where $r$ is the rank.
}

There is an awkwardness in the terminology here: it is important to keep in mind that 'having the same monodromy representation' is not the same as 'isomonodromic' when irregular singularities are present.
Proof. By fixing a base point (disjoint from the poles) and a frame at the base point, we can find a solution $y_{t}$ for each $t$ which depends smoothly on $t$. If the monodromy representation is constant, then we can find a matrix $K_{t} \in G$ for each $t$ such that the monodromy matrices of $y_{t} K_{t}$ are constant. If we take $t$ close to $t^{\prime}$ and exclude small discs around the poles of $\nabla_{t}$, then $g_{t t^{\prime}}=y_{t} K_{t} K_{t^{\prime}}^{-1} y_{t^{\prime}}^{-1}$ is single-valued, and we can construct $\Omega_{t}$ in (C1) by putting
$$\Omega_{t}=\left.\frac{\partial g_{t t^{\prime}}}{\partial t^{\prime}}\right|_{t^{\prime}=t} .$$
(This is holomorphic except at the poles of $\nabla_{t}$ ).
Conversely, if we are given $\Omega_{t}$, then $\mathrm{d}-A \mathrm{~d} z-\Omega \mathrm{d} t$ is a flat connection on the trivial bundle over
$$(X \backslash \text { poles }) \times[0,1] .$$
Its holonomy coincides with the monodromy $A_{t}$ for each $t$, and so the monodromy representation must be constant up conjugacy. \(\square\)

\section*{Isomonodromic deformations}

We now consider deformations ( $X_{t}, \nabla_{t}$ ) in which we change both $X$ and the connection ∇ .

Let $a$ be a pole of ∇ and $\mathcal{S}$ a sector at $a$. Then we have a solution $y_{\mathcal{S}, a}$ to the system $\nabla y=0$, uniquely determined up to the choice of the frame at $a$ in which the leading coefficient of $A$ is diagonal. If $a^{\prime}$ and $\mathcal{S}^{\prime}$ are another pole and sector at $a^{\prime}$, and if $\gamma$ is a path with initial point near $a$ in $\mathcal{S}$ and endpoint near $a^{\prime}$ in $\mathcal{S}^{\prime}$, then we can continue $y_{\mathcal{S}, a}$ along $\gamma$. We shall have
$$y_{\mathcal{S}, a}=y_{\mathcal{S}^{\prime}, a^{\prime}} C_{\mathcal{S}, \mathcal{S}^{\prime}, a, a^{\prime}, \gamma}$$
where $C_{\mathcal{S}, \mathcal{S}^{\prime}, a, a^{\prime}, \gamma}$ is a constant matrix. These matrices are uniquely determined by $A$ up to
$$C_{\mathcal{S}, \mathcal{S}^{\prime}, a, a^{\prime}, \gamma} \mapsto D_{a} C_{\mathcal{S}, \mathcal{S}^{\prime}, a, a^{\prime}, \gamma} D_{a^{\prime}}^{-1},$$
where, for each pole $a, D_{a}$ is the product of a diagonal matrix and a permutation matrix. The matrices connecting the special solutions in adjacent sectors at the same pole are called Stokes' matrices.

As we deform ∇ and $X$, we can vary $\mathcal{S}, \mathcal{S}^{\prime}, \gamma$, and the special solutions continuously.

Definition 5 A deformation is isomonodromic if the exponents of formal monodromy and the matrices $C_{\mathcal{S}, \mathcal{S}^{\prime}, a, a^{\prime}, \gamma}$ are constant, for an appropriate choice of special solutions.

An isomonodromic deformation has constant monodromy representation, but the converse is not true except in the Fuchsian case (all singularities regular). The following characterization of the isomonodromy property is implicit in Jimbo, Miwa, and Ueno (1981a).

We can cover $X_{t}$ by discs $D_{i}$ varying continuously with $t$ such that each pole lies in just one disc. On each disc $D_{i}$, we can choose a coordinate $z_{i}$ such that, if $a_{i} \in D$ is a pole, then $z_{i}=0$ at $a_{i}$, independently of $t$. We shall use these coordinates to identify the discs as $t$ varies.

Proposition 11 A deformation $\left(X_{t}, \nabla_{t}\right)$ with constant monodromy representation is isomonodromic if and only if
(i) in $D_{i}, \mathrm{~d} \nabla_{t} / \mathrm{d} t=\nabla_{t} \Omega_{i t}$ for some meromorphic $\Omega_{i t}: D_{i} \rightarrow \mathfrak{g}$ (depending smoothly on $t$ ); $\Omega_{i t}$ is holomorphic except possibly at a singularity of $\alpha_{t}$, where it has a pole of order at most $r_{i}$ if $\alpha_{t}$ has a singularity of rank $r_{i}$ in $D_{i}$;
(ii) on the intersection $D_{i} \cap D_{j}$ of two discs $\Omega_{i t}-\Omega_{j t}=i_{T_{i j}} \alpha_{t}$ for some holomorphic vector field $T_{i j}$.

Proof. We shall look at the proof in outline. Suppose that the deformation is isomonodromic. Let $y_{t}$ be a solution to $\nabla_{t} y_{t}=0$, depending continuously on $t$ and with constant monodromy (we have to keep in mind that $y_{t}$ is multi-valued and singular at the poles).

Let $D_{i}$ be a disc containing a pole (at $z_{i}=0$ ) and put
$$g_{i t t^{\prime}}\left(z_{i}\right)=y_{\mathcal{S}}\left(z_{i}\right) y_{\mathcal{S}^{\prime}}^{\prime-1}\left(z_{i}\right)$$
where $y_{\mathcal{S}}$ and $y_{\mathcal{S}^{\prime}}^{\prime}$ are the special solutions at $t$ and $t^{\prime}$ in the corresponding sectors at one of the poles. Then, for $t^{\prime}$ close to $t, g_{t t^{\prime}}$ is a single-valued holomorphic map $D_{i} \backslash\{0\} \rightarrow \mathfrak{g}$; it is independent of sector, because the Stokes' matrices are the same at $t$ and $t^{\prime}$. Once it is established that it is possible to differentiate the asymptotic expansions term-by-term, it is immediate that $\Omega_{i t}=\left.\partial_{t^{\prime}} g_{t t^{\prime}}\right|_{t^{\prime}=y}$ is meromorphic, and of the required form.

On a disc $D_{i}$ that does not contain a singularity, we put $g_{i t t^{\prime}}=y_{t}\left(z_{i}\right) y_{t^{\prime}}\left(z_{i}\right)^{-1}$, and define $\Omega_{i t}$ in the same way. If we choose the branch of $y_{t}$ to vary continuously with $t, g_{i t t^{\prime}}$ is independent of the choice of branch because the monodromy of $y_{t}$ is independent of $t$.

Given $y_{t}$, the only freedom in the construction of $\Omega_{i t}$ is in the choice of the coordinate $z_{i}$, and hence in the local identification of the discs on the different Riemann surfaces. A different choice for each $t$ will add $i_{T} \alpha$ to $\Omega_{i t}$ for some local holomorphic vector field $T$. Thus (iii) holds on the overlap of two discs.

To prove the converse, suppose that $\Omega_{i t}$ is meromorphic, as stated. Choose a continuously varying sector $\mathcal{S}$ at the pole, and let
$$y_{\mathcal{S}}\left(z_{i}, t\right)=g_{\mathcal{S}, a}\left(z_{i}\right) \exp \left(t z_{i}^{-r}+m \log z_{i}\right),$$
be the corresponding special solution. Then, by writing $\nabla_{t}=\mathrm{d}_{z}-A_{t} \mathrm{~d} z_{i}$ and dropping the subscripts, we have
$$\frac{\partial}{\partial z}\left(\frac{\partial y}{\partial t}-\Omega y\right)=\frac{\partial A}{\partial t} y+A \frac{\partial y}{\partial t}-\frac{\partial \Omega}{\partial t} y-\Omega A y=A\left(\frac{\partial y}{\partial t}-\Omega y\right) .$$
It follows that
$$\frac{\partial y}{\partial t}-\Omega y=y K$$
for some matrix $K$, which can depend of $t$ but not $z$. Therefore
$$g_{\mathcal{S}}^{-1}\left[\frac{\partial g_{\mathcal{S}}}{\partial t}+g_{\mathcal{S}} \frac{\partial}{\partial t}\left(\frac{t}{z^{r}}\right)-\Omega g_{\mathcal{S}}\right]=\mathrm{e}^{t z^{-r}+m \log z} K \mathrm{e}^{-t z^{-r}-m \log z} .$$
The left-hand side is asymptotic to a power series, divided by $z^{r+1}$, as $z \rightarrow 0$ in $\mathcal{S}$ (the same series for each sector at the pole). In the case $r>0$, each off-diagonal entry on the right-hand side has an exponential factor which must blow up as $z \rightarrow 0$ along some directions in $\mathcal{S}$ since the angle of the sector $\mathcal{S}$ is more than $\pi / r$. This is a contradiction unless the off-diagonal entries in $K$ all vanish. Thus $K$ is a $z$-independent diagonal matrix. It can be absorbed into the special solutions to give that
$$\frac{\partial y_{\mathcal{S}}}{\partial t}=\Omega_{t} y_{\mathcal{S}}$$
and hence that the $C$ matrices are constant. This is also true, more simply, in the regular case since the formal solutions then converge. \(\square\)

\section*{Symplectic form on $\mathcal{C}_{r}$}

We prove here that the tensor in (14) is a symplectic form on $\mathcal{C}_{r}$.
Proposition $12 \omega$ is a symplectic form on $\mathcal{C}_{r}$, independent of the choice of $C_{1}$.
Proof. From the definitions, $C_{2 r+1}=\mathrm{e}^{-2 \pi \mathrm{i} m} C_{1} M$ and, in variational notation,
$$\delta S_{i} S_{i}^{-1}=C_{i}\left(C_{i}^{-1} \delta C_{i}-C_{i+1}^{-1} \delta C_{i+1}\right) C_{i}^{-1} .$$
We must show that $\omega$ is skew-symmetric, closed, and non-degenerate. From the first constraint, we have $\operatorname{tr}\left(\delta S_{i} S_{i}^{-1} \delta^{\prime} S_{i} S_{i}^{-1}\right)=0$. It follows that
$$\begin{aligned}
0 & =\sum_{1}^{2 r} \operatorname{tr}\left(\delta S_{i} S_{i}^{-1} \delta^{\prime} S_{i} S_{i}^{-1}\right) \\
& =\sum_{1}^{2 r} \operatorname{tr}\left(\left(C_{i}^{-1} \delta C_{i}-C_{i+1}^{-1} \delta C_{i+1}\right)\left(C_{i}^{-1} \delta^{\prime} C_{i}-C_{i+1}^{-1} \delta^{\prime} C_{i+1}\right) .\right.
\end{aligned}$$

However
$$\begin{aligned}
\sum_{1}^{2 r} \operatorname{tr}\left(C_{i+1}^{-1} \delta C_{i+1} C_{i+1}^{-1} \delta^{\prime} C_{i+1}\right)=\sum_{1}^{2 r} & \operatorname{tr}\left(C_{i}^{-1} \delta C_{i} C_{i}^{-1} \delta^{\prime} C_{i}\right)-4 \pi^{2} \operatorname{tr}\left(\delta m \delta^{\prime} m\right) \\
& -2 \pi \mathrm{i} \operatorname{tr}\left(\delta m \delta^{\prime} C_{1} C_{1}^{-1}+\delta^{\prime} m \delta C_{1} C_{1}^{-1}\right) .
\end{aligned}$$
The skew-symmetry follows. A similar calculation, starting from
$$\operatorname{tr}\left(\delta S_{i} S_{i}^{-1} \delta^{\prime} S_{i} S_{i}^{-1} \delta^{\prime \prime} S_{i} S_{i}^{-1}\right)=0,$$
shows that $\omega$ is closed. To show that $\omega$ is nondegenerate, we note that if $\omega(Y, \cdot)=$, then $\delta C_{1} C_{1}^{-1}-\pi \mathrm{i} \delta m$ is anti-diagonal, $P_{i} \delta C_{i} C_{i} P_{i}^{-1}$ is lower triangular for each $i$, and $P_{i} \delta C_{i} C_{i}^{-1} P_{i}^{-1}$ is upper triangular. However, from (20),
$$\delta C_{i+1} C_{i+1}^{-1}=S_{i}^{-1} \delta C_{i} C_{i}^{-1} S_{i}-S_{i}^{-1} \delta C_{i} C_{i}^{-1} S_{i} .$$
Therefore $\delta C_{i} C_{i}^{-1}$ is diagonal and so $\delta C_{i} C_{i}^{-1}=\pi \mathrm{i} \delta m$ for each $i$. It then follows from the second constraint (C2) in the defintion of $\mathcal{C}_{r}$ that $\delta m=0$.

If we make a different choice for $C_{1}$ at each point, then the effect is to replace $C_{i}$ by $C_{i} K$, where $K$ is independent of $i$. This adds
$$\frac{1}{2 \pi \mathrm{i}} \sum_{1}^{2 r} \operatorname{tr}\left(C_{i} \delta K C_{i}^{-1} \delta^{\prime} S_{i} S_{i}^{-1}\right)-\operatorname{tr}\left(C_{1} \delta K C_{1}^{-1} \delta^{\prime} m\right)$$
to $\omega\left(Y, Y^{\prime}\right)$, which vanishes by (20). \(\square\)

\section*{Proof of Proposition 5}

The manipulations are slightly more transparent in the classical variational notation, although it is straightforward to translate this into the language of differential forms.

We shall evaluate $\sigma\left(Y, Y^{\prime}\right)$ in (11) by putting $\Omega=\delta y y^{-1}, \Omega^{\prime}=\delta^{\prime} y y^{-1}$. We shall then shrink the contour to the origin and use the asymptotic behaviour of the $y_{i} \mathrm{~s}$.

For each $i$, choose $z_{i} \in \mathcal{S}_{i} \cap \mathcal{S}_{i+1}$ on the contour with $z_{2 r+1}=z_{1}$, and define $\log z$ by making a cut along the ray through the origin and $z_{1}$. On each sector,
$$\Omega=\Omega_{i}+y_{i} \delta C_{i} C_{i}^{-1} y_{i}^{-1},$$
where $\Omega_{i}=\delta y_{i} y_{i}^{-1}$. Moreover,
$$\nabla\left(y_{i} \delta C_{i} C_{i}^{-1} y_{i}^{-1}\right)=0,$$
since $C_{i}$ is independent of $z$. Therefore, in the notation of (11),
$$\frac{1}{2 \pi \mathrm{i}} \oint \operatorname{tr}\left(\Omega \nabla \Omega^{\prime}\right)=\frac{1}{2 \pi \mathrm{i}} \sum_{1}^{2 r} \int_{z_{i}}^{z_{i+1}} \operatorname{tr}\left(\Omega_{i} \nabla \Omega_{i}^{\prime}\right)+\frac{1}{2 \pi \mathrm{i}} \sum_{1}^{2 r}\left(x_{i}\left(z_{i+1}\right)-x_{i}\left(z_{i}\right)\right)$$
where $z_{i}$ is some point on the contour in $\mathcal{S}_{i} \cap \mathcal{S}_{i+1}, x_{i}=\operatorname{tr}\left(\delta C_{i} C_{i}^{-1} y_{i}^{-1} \delta^{\prime} y_{i}\right)$, and the integrals are along segments of the contour. However,
$$x_{i+1}-x_{i}=\operatorname{tr}\left(\delta C_{i} \delta C_{i}^{-1} \delta^{\prime} S_{i} S_{i}^{-1}-S_{i}^{-1} \delta S_{i} y_{i+1}^{-1} \delta^{\prime} y_{i+1}\right) .$$
This follows from the two relations $y_{i}=y_{i+1} S_{i}^{-1}$ and $C_{i}=S_{i} C_{i+1}$, which imply that
$$\operatorname{tr}\left(\delta C_{i} C_{i}^{-1} y_{i}^{-1} \delta^{\prime} y_{i}\right)=\operatorname{tr}\left(\delta C_{i} C_{i}^{-1} S_{i} y_{i+1}^{-1}\left(\delta^{\prime} y_{i+1}\right) S_{i}^{-1}-\delta C_{i} C_{i}^{-1} \delta^{\prime} S_{i} S_{i}^{-1}\right)$$
and
$$S_{i}^{-1} \delta C_{i} C_{i}^{-1} S_{i}=\delta C_{i+1} C_{i+1}^{-1}-S_{i}^{-1} \delta S_{i} .$$

As $z \rightarrow 0$ in $\mathcal{S}_{i} \cap \mathcal{S}_{i+1}$, the second term on the right-hand side of (22) goes to zero by (13). Moreover,
$$x_{2 r+1}-x_{1}=4 \pi^{2} \operatorname{tr}\left(\delta m \delta^{\prime} m\right)+2 \pi \operatorname{itr}\left(\delta C_{1} C_{1}^{-1} \delta^{\prime} m\right)-2 \pi \mathrm{i}\left(\delta m y_{1}^{-1} \delta y_{1}\right) .$$

To deal with the first term in (21), we note that
$$\Omega_{i}=\Theta+g \delta m g^{-1} \log z+O\left(z^{N}\right)$$
as $z \rightarrow 0$ in $\mathcal{S}_{i}$ for some large $N$ (depending on the truncation of the formal power series). Therefore in $\mathcal{S}_{i}$
$$\begin{aligned}
& \operatorname{tr}\left(\Omega_{i} \nabla \Omega_{i}^{\prime}\right)= \\
& \quad \operatorname{tr}\left(\Theta \nabla \Theta^{\prime}\right)+\operatorname{tr}\left[\left(g^{-1} \delta g+\frac{\delta t}{z^{r}}\right) \delta^{\prime} m-\left(g^{-1} \delta^{\prime} g+\frac{\delta^{\prime} t}{z^{r}}\right) \delta m\right] \frac{\mathrm{d} z}{z} \\
& \quad+\partial_{z}\left(\operatorname{tr}\left(\delta^{\prime} m\left(g^{-1} \delta g+z^{-r} \delta t\right)\right) \log z\right) \mathrm{d} z+\operatorname{tr}\left(\delta m \delta^{\prime} m\right) \log z \frac{\mathrm{~d} z}{z}+O\left(N^{\prime}\right)
\end{aligned}$$
for some large $N^{\prime}$. We therefore have
$$\begin{aligned}
\frac{1}{2 \pi \mathrm{i}} \sum_{1}^{2 r} \int_{z_{i}}^{z_{i+1}} \operatorname{tr}\left(\Omega_{i} \nabla \Omega_{i}^{\prime}\right)=\frac{1}{2 \pi \mathrm{i}} \oint & \operatorname{tr}\left(\Theta \nabla \Theta^{\prime}\right)+\operatorname{tr}\left(\gamma \delta^{\prime} m-\gamma^{\prime} \delta m\right) \\
& +\operatorname{tr}\left(\delta^{\prime} m y_{1}^{-1} \delta y_{1}\right)_{z_{1}}+\pi \mathrm{itr}\left(\delta m \delta^{\prime} m\right)+\epsilon
\end{aligned}$$
where $\epsilon \rightarrow 0$ as the contour is shrunk. The proposition follows by putting the two terms together, by shrinking the contour towards $z=0$, and by using the definition (14).

\section*{References}

Ablowitz, M. J., and Clarkson, P. A. (1991). Solitons, nonlinear evolution equations and inverse scattering. LMS Lecture Notes, 149. Cambridge University Press, Cambridge.

Boalch, P. (2000). Symplectic manifolds and isomonodromic deformations. (Preprint, SISSA, Trieste).

Dubrovin, B. (1999). Painlevé transcendents in two-dimensional topological field theory. In The Painlevé property, one century later. Ed. R. Conte. CRM Series in Mathematics. Springer, New York.

Farkas, H. M., and Kra, I (1991). Riemann surfaces. Springer, New York.
Hitchin, N. J. (1995a). Twistor spaces, Einstein metrics and isomonodromic deformations. J. Diff. Geom. 42, 30-112.

Hitchin, N. J. (1995b). Poncelet polygons and the Painlevé equations. In: Geometry and analysis, Bombay 1992, 151-185. Tata Institute, Bombay.

Hitchin, N. J. (1996). A new family of Einstein metrics. In: Manifolds and geometry, Pisa 1993, 190-222. Sympos. Math., XXXVI. Cambridge University Press, Cambridge.

Hitchin, N. J. (1997) Geometrical aspects of Schlesinger's equation. J. Geom. Phys., 23, 287-300.

Jimbo, M., Miwa, T., and Ueno, K. (1981a). Monodromy preserving deformations of linear ordinary differential equations with rational coefficients. I. General theory and $\tau$-functions. Physica 2D, 306-52.

Jimbo, M., and Miwa, T. (1981b). Monodromy preserving deformations of linear ordinary differential equations with rational coefficients. II. Physica 2D, 407-48.

Jimbo, M., and Miwa, T. (1981c). Monodromy preserving deformations of linear ordinary differential equations with rational coefficients. III. Physica 4D, 26-46.

Kodaira, K. (1961). A theorem of completeness of characteristic systems for analytic families of compact submanifolds of complex manifolds. Ann. Math., 75, 146-62.

Malgrange, B. (1982). Sur les déformations isomonodromiques. Séminaire de l'Ecole Norm. Sup., IV, 401-26.

Mason, L. J., and Woodhouse, N. M. J. (1996). Integrability, self-duality, and twistor theory, Oxford.

Pressley, A., and Segal, G. (1986). Loop groups. Oxford University Press, Oxford.

Sato, M., Miwa, T., and Jimbo, M. (1978). Holonomic quantum fields. I. Publ. RIMS, Kyoto, 14, 223-67.

Sato, M., Miwa, T., and Jimbo, M. (1979). Holonomic quantum fields. II-IV. Publ. RIMS, Kyoto, 15, 201-67, 577-629, 871-972.

Sato, M., Miwa, T., and Jimbo, M. (1980). Holonomic quantum fields. V. Publ. RIMS, Kyoto, 16, 531-84.

Souriau, J.-M. (1970). Structures des systèmes dynamique. Dunod, Paris.
Woodhouse, N. M. J. (1992). Geometric quantization. 2nd edition. Oxford University Press, Oxford.