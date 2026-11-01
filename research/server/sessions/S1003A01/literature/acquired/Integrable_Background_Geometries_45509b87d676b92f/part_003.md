---
retention_scope: session
part: 3
total_parts: 3
---

[Part 3/3 of: Integrable Background Geometries]

On a general Einstein-Weyl space, $\mathcal{H}$ is defined by the Weyl connection: the hyperCR case is special in that there is a preferred trivialization of the bundle of conics with respect to which the distribution is horizontal. Using this trivialization, the bundle of conics is $B \times \mathbb{P}^{1}$, and after choosing a projective coordinate $\zeta$ on $\mathbb{P}^{1}$, the null 1-forms are
$$\alpha_{\zeta}=\alpha_{1}+\boldsymbol{i} \alpha_{2}+2 \zeta \alpha_{3}-\zeta^{2}\left(\alpha_{1}-\boldsymbol{i} \alpha_{2}\right) .$$
The system (9.4)-(9.6) is equivalent to $\alpha_{\zeta} \wedge \mathrm{d} \alpha_{\zeta}=0$ for all $\zeta$. If $X_{1}, X_{2}, X_{3}$ is the dual frame, this means that the vector fields $X_{1}+\boldsymbol{i} X_{2}+\zeta X_{3}$ and $X_{3}-\zeta\left(X_{1}-\boldsymbol{i} X_{2}\right)$ span an integrable distribution (tangent to the null surfaces) for each fixed $\zeta$. This is the hyperCR analogue of the Mason-Newman-Dunajski-Joyce description of hypercomplex structures.

To see explicitly what this means, put $\varphi=\alpha_{1}+\boldsymbol{i} \alpha_{2}$ and $\omega=-\tau \alpha_{3}+\gamma$, with $\left\langle\gamma, \alpha_{3}\right\rangle=0$, so that (9.4)-(9.6) become
$$\begin{aligned}
& \mathrm{d} \varphi=\left((\tau+\boldsymbol{i} \kappa) \alpha_{3}-\gamma\right) \wedge \varphi, \\
& \mathrm{d} \alpha_{3}=-\gamma \wedge \alpha_{3}+\frac{i}{2} \kappa \varphi \wedge \bar{\varphi} .
\end{aligned}$$
The first equation implies the integrability of the distribution defined by $\varphi$. Tod [56] uses (9.7) to put $\varphi=w \mathrm{~d} z$. I will not repeat this here. Instead I want to analyse these equations from the point of view of integrable background geometries. The idea is that the foliation determined by $\chi_{3}$ is a generalized dimensional reduction. To see this, break the equations into horizontal and vertical parts by writing $\alpha_{3}=\mathrm{d} t+A$ for some fibre coordinate $t$ so that $A$ is horizontal (i.e., in the span of $\alpha_{1}$ and $\alpha_{2}$ ). Then for any 1-form $\beta$,
$$\mathrm{d} \beta=d_{N} \beta+\mathrm{d} t \wedge \dot{\beta}=d_{N} \beta-A \wedge \dot{\beta}+\alpha_{3} \wedge \dot{\beta},$$
where $d_{N} \beta$ is a multiple of $\alpha_{1} \wedge \alpha_{2}, \dot{\beta}=\partial_{t} \beta, \alpha_{1}\left(\partial_{t}\right)=0=\alpha_{2}\left(\partial_{t}\right)$, and $\mathrm{d} t\left(\partial_{t}\right)=1$. Hence (9.7)-(9.8) become
$$\begin{array}{lc}
d_{N} \varphi-A \wedge \dot{\varphi}=-\gamma \wedge \varphi, & \dot{\varphi}=(\tau+\boldsymbol{i} \kappa) \varphi, \\
d_{N} A-A \wedge \dot{A}=\frac{i}{2} \kappa \varphi \wedge \bar{\varphi}, & \dot{A}=\gamma .
\end{array}$$
The equations on the right simply define $\tau+i \kappa$ and $\gamma$, so after computing that $\dot{\varphi} \wedge \bar{\varphi}-\varphi \wedge \dot{\bar{\varphi}}=$ $2 \boldsymbol{i} \kappa \boldsymbol{\varphi} \wedge \overline{\boldsymbol{\varphi}}$, the equations on the left reduce to
$$\begin{aligned}
& d_{N} \varphi+\dot{A} \wedge \varphi-A \wedge \dot{\varphi}=0 \\
& d_{N} A+\dot{A} \wedge A=\frac{1}{4}(\dot{\varphi} \wedge \bar{\varphi}-\varphi \wedge \dot{\bar{\varphi}}) .
\end{aligned}$$
The conformal structure on $N$ has representative metric $\varphi \bar{\varphi}$ so the orientation can be chosen so that $\varphi$ has type ( 1,0 ). It is now easy to see that these equations are Hitchin's equations with gauge group $\operatorname{Diff}\left(S^{1}\right): \varphi$ and $A$ are 1-forms on $N$ with values in $\mathfrak{g}=\operatorname{Vect}\left(S^{1}\right) ; \varphi$ is the Higgs field and $A$ is the connection 1-form, satisfying
$$F^{A}=[\varphi, \bar{\varphi}]_{\mathfrak{g}} \quad \bar{\partial}^{A} \varphi=0 .$$
These are equivalent to the (9.7)-(9.8) and hence to (9.4)-(9.6): since $\dot{\varphi}$ has type (1, 0), one can locally write $\dot{\varphi}=(\tau+\boldsymbol{i} \kappa) \varphi$ and thus define $\alpha_{1}, \alpha_{2}, \alpha_{3}, \omega$.

Theorem 9.1. Let $(A, \varphi)$ be a solution of the $\operatorname{Diff}\left(S^{1}\right)$ Hitchin equations (on a trivial spinor-vortex space $N$ ). Then the Einstein-Weyl space defined by ( $A, \varphi$ ) is hyperCR, and one of its hyperCR congruences defines the foliation over $N$. Any hyperCR Einstein-Weyl space arises in this way.

Tod's simplification of the $\operatorname{Diff}\left(S^{1}\right)$ Hitchin equations amounts to a fixing the $\operatorname{Diff}\left(S^{1}\right)$ gauge via $e^{2 i t}=\varphi / \bar{\varphi}$.

In order to obtain new examples of hyperCR Einstein-Weyl spaces, consider Hitchin fields where the gauge group is a finite-dimensional subgroup of $\operatorname{Diff}\left(S^{1}\right)$. The Abelian gauge group U(1) yields only flat Einstein-Weyl spaces, but the affine and projective groups, $\operatorname{Aff}(\mathbb{R})$ and $\operatorname{PSL}(2, \mathbb{R})$ are more interesting. The former is more tractable, since $\operatorname{Aff}(\mathbb{R})$ is a solvable group, meaning that the nonlinear Hitchin equations can be solved by integrating a sequence of linear equations. Indeed, writing $\varphi=\varphi_{0}+\varphi_{1} t$ and $A=A_{0}+A_{1} t$ gives
$$\begin{array}{ll}
d \varphi_{1}=0, & d \varphi_{0}+A_{1} \wedge \varphi_{0}-A_{0} \wedge \varphi_{1}=0, \\
d A_{1}=0, & d A_{0}+A_{1} \wedge A_{0}=\frac{1}{4}\left(\varphi_{1} \wedge \bar{\varphi}_{0}-\varphi_{0} \wedge \bar{\varphi}_{1}\right) .
\end{array}$$

Locally, the affine gauge freedom can be used to eliminate the linear term $A_{1}$ of the connection $A$, while the conformal gauge freedom can be used to make the linear term $\varphi_{1}$ of the Higgs field $\varphi$ equal to $\lambda \mathrm{d} z$ with $\lambda$ constant (without loss of generality $\lambda=1$ unless it vanishes, which is the Abelian case). Let $\varphi_{0}=\boldsymbol{i} f \mathrm{~d} z$ so that the equations reduce to
$$\boldsymbol{i} f_{\bar{z}} \mathrm{~d} \bar{z} \wedge \mathrm{~d} z=\lambda A_{0} \wedge \mathrm{~d} z, \quad d A_{0}=-\frac{1}{2} \boldsymbol{i} f \mathrm{~d} z \wedge \mathrm{~d} \bar{z} .$$
For $\lambda \neq 0$, the general solution up to gauge transformation is therefore determined by a real function $f(z, \bar{z})$ satisfying $\Delta f+2 \lambda^{2} f=0: \varphi=(t+\boldsymbol{i} f) \mathrm{d} z$ and $A=-* \mathrm{~d} f / \lambda$. Hence (local) eigenfunctions of the Laplacian on $\mathbb{R}^{2}$ give rise to hyperCR Einstein-Weyl spaces.

\section*{Einstein-Weyl spaces with a geodesic generalized symmetry}

A shear-free geodesic congruence on an Einstein-Weyl space is a weightless unit vector field $\chi \in \mathrm{C}^{\infty}\left(B, L^{-1} T B\right)$ such that
$$D \chi=\tau(\mathrm{id}-\chi \otimes \chi)+\kappa * \chi$$
and for sections $\tau, \kappa$ of $L^{-1}$ called the divergence and twist of $\chi$. On a hyperCR Einstein-Weyl space, the hyperCR congruences are examples: they are also divergence-free and in fact this characterizes them. In the previous subsection it was found that the foliation defined by a hyperCR congruence is a generalized symmetry, so it is natural to ask, more generally, when does a shear-free geodesic congruence define a generalized symmetry? Note that the weightless unit vector field tangent to a generalized symmetry over a spinor-vortex space is always shearfree, so this question can be rephrased: when is a generalized symmetry geodesic? Since the Einstein-Weyl space $B$ is completely explicit (8.2) in terms of the Hitchin field on the spinor-vortex space $N$, this question is easily answered: the generalized symmetry is geodesic if and only if $\mathcal{C}$ (and $\widetilde{\mathcal{C}}$, which is the complex conjugate in the Euclidean case) vanishes. The Einstein-Weyl structure is then given by
$$\begin{aligned}
& g=4 \Phi \bar{\Phi} \mathrm{~d} z \mathrm{~d} \bar{z}+(\mathrm{d} t+\alpha \mathrm{d} z+\bar{\alpha} \mathrm{d} \bar{z})^{2}, \\
& \omega=\dot{\alpha} \mathrm{d} z+\dot{\bar{\alpha}} \mathrm{d} \bar{z}-\frac{1}{2}\left(\frac{\psi+\dot{\Phi}}{\Phi}+\frac{\bar{\psi}+\overline{\bar{\Phi}}}{\bar{\Phi}}\right)(\mathrm{d} t+\alpha \mathrm{d} z+\bar{\alpha} \mathrm{d} \bar{z}) .
\end{aligned}$$
If $\psi$ vanishes, then the spinor-vortex space is (locally) trivial and this is the case of the previous subsection. Otherwise, $\psi$ is a holomorphic trivialization of $\mathcal{W}$ on the open set where it is nonzero, and the spinor-vortex space is given by a spherical metric on $N$.

Two special cases of this construction have already been studied: the case that $\partial_{t}$ is a genuine symmetry [10], and the case that the congruence is also twist-free [11]. The first class arises by supposing that the gauge group reduces to U(1) or $\mathbb{R}$ and $B$ is said to be Einstein-Weyl with a geodesic symmetry. The Abelian Hitchin equations are easily solved on the spherical spinor-vortex space yielding the explicit formula
$$g=|h|^{2} g_{S^{2}}+\beta^{2}, \quad \omega=-\frac{i(h-\bar{h})}{2|h|^{2}} \beta, \quad \mathrm{~d} \beta=\frac{1}{2}(h+\bar{h}) \operatorname{vol}_{S^{2}},$$
where $h$ is a holomorphic function on an open subset of $S^{2}$.
The second class, the hyperCR-Toda spaces, are obtained by from some explicit solutions of the affine Hitchin equations: the twist-free condition reduces the gauge group to $\operatorname{Aff}(\mathbb{R})$; the connection is flat, the linear part of the Higgs field is constant, while the translational part of the Higgs field is given by a holomorphic function $h$. The resulting Einstein-Weyl structure is
$$g=(t+h)(t+\bar{h}) g_{S^{2}}+\mathrm{d} t^{2}, \quad \omega=-\frac{2 t+h+\bar{h}}{(t+h)(t+\bar{h})} \mathrm{d} t .$$
In this case the twist of the geodesic generalized symmetry $\partial_{t}$ vanishes.

Note that the general theory of this paper justifies the final remarks of [11], by explaining the sense in which the spherical metric is the natural quotient geometry of both structures (9.10) and (9.11).

In both cases, the Einstein-Weyl space is hyperCR, although the congruence generated by $\partial_{t}$ is no longer one of the hyperCR congruences. The same holds in general.

Theorem 9.2. An Einstein-Weyl space with a geodesic generalized symmetry is hyperCR.
Proof. Gauduchon and Tod [22] show that an Einstein-Weyl space $(B, \mathrm{c}, D)$ is hyperCR with twist $\hat{\kappa}$ if and only if $* D \hat{\kappa}=\frac{1}{2} F^{D}$ and $\hat{\kappa}^{2}=\frac{1}{6} \mathrm{scal}^{D}$.

On an Einstein-Weyl space with a geodesic generalized symmetry, direct computation of $\mathrm{d}^{D} \chi$ in the gauge $(g, \omega)$ for the Einstein-Weyl structure (9.9) yields
$$\kappa=\frac{1}{4 \boldsymbol{i}}\left(\frac{\dot{\Phi}-\psi}{\Phi}-\frac{\dot{\Phi}-\bar{\psi}}{\bar{\Phi}}\right) .$$
Now put
$$\hat{\kappa}=\frac{1}{2 \boldsymbol{i}}\left(\frac{\dot{\Phi}}{\Phi}-\frac{\dot{\bar{\Phi}}}{\bar{\Phi}}\right)-\kappa=\frac{1}{4 \boldsymbol{i}}\left(\frac{\dot{\Phi}+\psi}{\Phi}-\frac{\dot{\bar{\Phi}}+\bar{\psi}}{\bar{\Phi}}\right) .$$
In the gauge $(g, \omega)$, the equation $*(\mathrm{~d} \hat{\kappa}-\omega \hat{\kappa})=\frac{1}{2} \mathrm{~d} \omega$ is a straightforward though tedious computation. The equation $\hat{\kappa}^{2}=\frac{1}{6} \mathrm{scal}^{D}$ also follows by direct computation, although the calculation is greatly simplified by using the general formula $-\frac{1}{6} \operatorname{scal}^{D}=D_{\chi} \tau+\tau^{2}-\kappa^{2}$ for the scalar curvature of an Einstein-Weyl space with a shear-free geodesic congruence $\chi$ [10, 48]. In this case $-2 \tau=\psi / \Phi+\bar{\psi} / \bar{\Phi}$ : the verification that $\dot{\tau}-\omega\left(\partial_{t}\right) \tau+\tau^{2}=\kappa^{2}-\hat{\kappa}^{2}$ is now easy. \(\square\)

Conversely, twistor methods show that the foliation defined by any shear-free geodesic congruence on any hyperCR Einstein-Weyl space is a generalized dimensional reduction over a trivial or spherical spinor-vortex geometry, although this is not easy to see by direct computation.

\section*{10 Riccati spaces}

Riccati spaces form a foundation on which higher-dimensional geometries can be built, so although the matrix Riccati equation is easy to solve, it is invaluable to understand the solutions carefully. For this reason, I will begin by tackling the Riccati equation in an invariant way, without choosing a conformal trivialization of $\mathcal{E}$ or a coordinate on $C$. Recall that $\wedge^{3} \mathcal{E}=(T C)^{3}$, and it will be convenient to write $T C=L$, although the choice of orientation implicit in this identification is not essential.

The matrix $\mathcal{B}$ is a section of $L^{-1} \operatorname{Sym}_{0} \mathcal{E}$ and so, at each point of $C$, it has two obvious invariants, of weight -2 and -3 respectively: $x=\frac{2}{3} \operatorname{tr}\left(\mathcal{B}^{2}\right)$ and $y=4 \operatorname{det} \mathcal{B}$, normalized so that the characteristic polynomial of $\mathcal{B}$ is $4 \lambda^{3}-3 x \lambda-y$. The discriminant of this polynomial is the section $y^{2}-x^{3}$ of $L^{-6}$ : more precisely, writing $4\left(y^{2}-x^{3}\right)=-27 c^{2}$ yields $c=\psi_{1} \psi_{2} \psi_{3}$, where $\psi_{1}=\frac{2}{3}\left(\lambda_{2}-\lambda_{3}\right), \psi_{2}=\frac{2}{3}\left(\lambda_{3}-\lambda_{1}\right)$ and $\psi_{3}=\frac{2}{3}\left(\lambda_{1}-\lambda_{2}\right),\left\{\lambda_{i}\right\}$ being the eigenvalues of $\mathcal{B}$; the sign of $c$ depends on the ordering of the eigenvalues. Note that
$$\psi_{1}+\psi_{2}+\psi_{3}=0, \quad \psi_{1}^{2}+\psi_{2}^{2}+\psi_{3}^{2}=2 x$$
and
$$\left(\psi_{1}-\psi_{2}\right)\left(\psi_{2}-\psi_{3}\right)\left(\psi_{3}-\psi_{1}\right)=-8 \lambda_{1} \lambda_{2} \lambda_{3}=-2 y .$$

\section*{Pencils of conics}

In order to interpret this geometrically, complexify $C$ and $\mathcal{E}$ so that the conformal structure c on $\mathcal{E}$ is determined by its null lines, which form a bundle of conics $\mathcal{S}(\mathcal{E})$ in the bundle $P(\mathcal{E})$ of projective planes over $C$. The role of $\mathcal{B}$ is to determine a pencil of conics in each fibre, associated to the two-dimensional family of bilinear forms $\mathrm{c} \circ(s \mathrm{id}+t \mathcal{B}): \mathrm{c} \circ \mathcal{B}$ is distinguished by being traceless with respect to the fixed bilinear form c. Now, two distinct conics meet in four points, counted with multiplicity, so there are six possible configurations: the generic case (I), where the four points are distinct; the four degenerations (II, III, D, N), when two, three, two pairs, or four points come together; and the trivial case (0), when $\mathcal{B}=0$ and the 'pencil' is constant.
![](https://cdn.mathpix.com/cropped/c46dd08a-362a-481e-81e9-d664e136643a-37.jpg?height=174&width=473&top_left_y=666&top_left_x=849)

The notation here follows the well-known application of this classification to Weyl tensors in four dimensions. Only types (I, D, 0) are compatible with Euclidean reality conditions: in this case $\mathcal{B}$ must be diagonalizable, and the eigenvalues are either distinct $\left(\lambda_{1}, \lambda_{2}, \lambda_{3}\right)$ with $\lambda_{1}+\lambda_{2}+\lambda_{3}=0$, or of the form $(\lambda, \lambda,-2 \lambda)$, or all zero.

A natural way to analyse a pencil of conics is to identify one of the conics with a projective line $\mathbb{P}^{1}$. In the present situation, this is done by introducing a bundle of spinors $\mathcal{U}$ for $\mathcal{E}$, i.e., with $\mathcal{E}=S^{2} \mathcal{U}$, so that $\mathcal{S}(\mathcal{E})=P(\mathcal{U})$ and $\mathcal{U}$ inherits a connection from $\mathcal{E}$. Trivializing $\mathcal{U}$ using this connection identifies $\mathcal{S}(\mathcal{E})$ locally with $C \times \mathbb{P}^{1}$, on which an affine coordinate $r$ for $C$ and a projective coordinate $\zeta$ for $\mathbb{P}^{1}$ may be introduced. The isomorphism between sections of the inner product bundle $L^{-1} \mathcal{E}$ and vertical vector fields on $\mathcal{S}(\mathcal{E})$ may be described concretely using the induced parallel orthonormal frame for $L^{-1} \mathcal{E}$ : sections induce vector fields via their inner product with the tautological null vector field $e_{\zeta} \otimes \partial_{\zeta}$ where
$$e_{\zeta}=\left(\frac{1}{2}\left(\zeta^{2}+1\right), \boldsymbol{i} \zeta, \frac{\boldsymbol{i}}{2}\left(\zeta^{2}-1\right)\right) .$$
The base locus of the pencil of conics (at each point of $C$ ) consists of the four zeros of the quartic polynomial $\left\langle\mathcal{B}\left(e_{\zeta}\right), e_{\zeta}\right\rangle \otimes \partial_{\zeta}^{2}$, which is a section of $L^{-1} \otimes \mathcal{O}(4)$. It is now straightforward and entirely classical [57] to analyse the zeros of this quartic in the various cases, and hence relate the six types of pencil to properties of the matrix $\mathcal{B}$. In particular, the generic case is given by $c \neq 0$, when the four points are distinct.
Remark 10.1. Four distinct points on $\mathbb{P}^{1}$ are determined up to projective transformation by their cross-ratio, and this freedom is often used to identify the points with $0,1, \infty, t$, with $t$ being the cross-ratio. However, as remarked by Yoshida in his wonderful book [64], "it is not fair that only the fourth point is allowed to move freely". The democratic cross-ratio used there is the point $\left[\psi_{1}, \psi_{2}, \psi_{3}\right]$ on the line $\psi_{1}+\psi_{2}+\psi_{3}=0$ in $\mathbb{P}^{2}$.

\section*{Solution of the Riccati equation}

I shall now find the solutions of the Riccati equation $D \mathcal{B}=2\left(\mathcal{B}^{2}\right)_{0}$. Here and elsewhere $D$ denotes differentiation with respect to the affine structure on $C$, and takes a section of a natural bundle $F$ to a section of $L^{-1} F$. In naive terms, $D$ is differentiation with respect to an affine coordinate $r$ (i.e., $\mathrm{d} r$ is a $D$-parallel section of $L^{-1}=T^{*} C$, and $L^{-1}$ is trivialized using this section).

The Riccati equation shows that $D \mathcal{B}$ commutes with $\mathcal{B}$, and so differentiating the Cayley-Hamilton equation $4 \mathcal{B}^{3}-3 x \mathcal{B}-y$ id $=0$, gives
$$\begin{aligned}
0 & =12(D \mathcal{B}) \mathcal{B}^{2}-3 x D \mathcal{B}-3 D x \mathcal{B}-D y \mathrm{id}=24 \mathcal{B}^{4}-18 x \mathcal{B}^{2}+3 x^{2} \mathrm{id}-3 D x \mathcal{B}-D y \mathrm{id} \\
& =3(2 y-D x) \mathcal{B}+\left(3 x^{2}-D y\right) \mathrm{id} .
\end{aligned}$$

Hence $D x=2 y, D y=3 x^{2}, D^{2} x=6 x^{2}$ and so $D\left(y^{2}-x^{3}\right)=0$. In other words, the discriminant $c^{2}$ is constant ( $D$-parallel). The constancy of $c$ means that if $\mathcal{B}$ has distinct eigenvalues at a point, it has distinct eigenvalues everywhere, in which case it is diagonalizable, and can be assumed diagonal, since $D \mathcal{B}$ commutes with $\mathcal{B}$. I consider this first.

\section*{I. $\mathcal{B}$ has distinct eigenvalues.}

Taking $\mathcal{B}$ diagonal, it is straightforward to compute the equation for the eigenvalues: $D \lambda_{1}=$ $2 \lambda_{1}^{2}-\frac{2}{3}\left(\lambda_{1}^{2}+\lambda_{2}^{2}+\lambda_{3}^{2}\right)$ and similarly for $\lambda_{2}$ and $\lambda_{3}$. Hence $D \psi_{1}=\psi_{1}\left(\psi_{2}-\psi_{3}\right)=-2 \lambda_{1} \psi_{1}$ and similarly for $\psi_{2}$ and $\psi_{3}$. Now let $\chi_{1}=-\psi_{2} \psi_{3}$ etc., so that $\chi_{1} \chi_{2} \chi_{3}=-c^{2}$ and $D \chi_{1}=-\chi_{1}\left(\psi_{2}-\right.$ $\left.\psi_{3}\right)=2 \lambda_{1} \chi_{1}$. Squaring this gives $\left(D \chi_{1}\right)^{2}=\chi_{1}^{2}\left(\psi_{2}^{2}+\psi_{3}^{2}-2 \psi_{2} \psi_{3}\right)=\chi_{1}^{2}\left(\psi_{1}^{2}-4 \psi_{2} \psi_{3}\right)=4 \chi_{1}^{3}+c^{2}$, since $\psi_{1}+\psi_{2}+\psi_{3}=0$. Hence the $\chi_{i}$ all satisfy the equation
$$(D \chi)^{2}=4 \chi^{3}+c^{2},$$
which is closely related to the equation for $x$, namely
$$(D x)^{2}=4 x^{3}-27 c^{2} .$$
Thus $x$ and the $\chi$ 's are equianharmonic Weierstraß elliptic functions of an affine coordinate, the period lattice for $x$ being the barycentric subdivision of the lattice for the $\chi$ 's.

Remark 10.2. The advantage of an invariant description is the flexibility in the choice of coordinates: one does not have to use the affine coordinate $r$. Indeed, in Section 3, a different gauge choice was motivated: there is a natural projective structure $D^{2}+\frac{1}{6} \operatorname{tr} \mathcal{B}^{2}=D^{2}+\frac{1}{4} x$ and with respect to a projective coordinate $t, D=\partial_{t}+a$, where $\dot{a}-\frac{1}{2} a^{2}=-\frac{1}{2} x$. Now $\dot{x}=2(a x+y)$ and $\dot{y}=3\left(a y+x^{2}\right)$, so that $\ddot{a}=a \dot{a}-\frac{1}{2} \dot{x}=a \dot{a}-a x-y$ and
$$\begin{aligned}
\dddot{a} & =a \ddot{a}+\dot{a}^{2}-\dot{a} x-\frac{5}{2} a \dot{x}+\left(\frac{3}{2} a \dot{x}-\dot{y}\right)=a \ddot{a}+\dot{a}^{2}-\dot{a}\left(a^{2}-2 \dot{a}\right)-5 a(a \dot{a}-\ddot{a})+3\left(a^{2}-x\right) x \\
& =6 a \ddot{a}+3 \dot{a}^{2}-6 a^{2} \dot{a}+6 \dot{a}\left(a^{2}-2 \dot{a}\right)=6 a \ddot{a}-9 \dot{a}^{2},
\end{aligned}$$
which is the Chazy equation. Of course it is well-known that the Chazy equation arises in the study of selfdual metrics in a scalar-flat gauge.

The generic solution, given by elliptic functions of the affine coordinate, may instead be presented in terms of modular functions of the projective coordinate [1, 16].

I turn next to the degenerate cases, when $c=0$, i.e., $y^{2}=x^{3}=64 \lambda^{6}$, where the eigenvalues of $\mathcal{B}$ are $\lambda, \lambda$ and $-2 \lambda$. Assume first that $\lambda$ is not identically zero. Then, on an open set at least, the (generalized) eigenspaces of $\mathcal{B}$ are constant (again using the fact that $D \mathcal{B}$ commutes with $\mathcal{B}$ ) and hence $\mathcal{B}$ can be assumed to take the the form
$$\mathcal{B}=\left[\begin{array}{ccc}
\lambda+\mu & \boldsymbol{i} \mu & 0 \\
\boldsymbol{i} \mu & \lambda-\mu & 0 \\
0 & 0 & -2 \lambda
\end{array}\right] .$$
The matrix Riccati equation now yields
$$D \lambda=-2 \lambda^{2}, \quad D \mu=4 \lambda \mu .$$
Since $\lambda$ is not identically zero, it is given (up to translation) by $\lambda=1 / 2 r$. This is defined for $r$ nonzero, and $\lambda$ has no zeros. In this coordinate $\mu=b r^{2}$ for constant $b$, which is either identically zero, or nonzero for all nonzero $r$. There are thus two cases.
\begin{itemize}
\item[II.] $y^{2}=x^{3}$ is nowhere zero, and $\mathcal{B}$ is nowhere diagonalizable.
\item[D.] $y^{2}=x^{3}$ is nowhere zero, and $\mathcal{B}$ is everywhere diagonalizable.
\end{itemize}
The notation is justified by noting that $\left\langle\mathcal{B}\left(e_{\zeta}\right), e_{\zeta}\right\rangle$ is the quartic $\frac{1}{4}(\zeta-1)^{2}\left(\mu(\zeta-1)^{2}+3 \lambda(\zeta+1)^{2}\right)$ : $\zeta=1$ is a repeated root, as is $\zeta=-1$ when $\mu=0$.

Remark 10.3. The type (D) solution is even simpler with respect to a projective coordinate. Since $2 \mathcal{B}_{0}^{2}=-2 \lambda \mathcal{B}$, setting $D=\partial_{t}+2 \lambda$ gives $\partial_{t} \mathcal{B}=0$, so that $\lambda$ is constant in this gauge and $a=2 \lambda$ satisfies $\dot{a}-\frac{1}{2} a^{2}=-2 \lambda^{2}=-\frac{1}{3} \operatorname{tr} \mathcal{B}^{2}=-\frac{1}{2} x$; thus $t$ is a projective coordinate with respect to the natural projective structure, and $\mathcal{B}$ and $a$ are constant.

It remains to consider the case that $y^{2}=x^{3}$ is identically zero, i.e., the eigenvalues of $\mathcal{B}$ are all zero, so that $\mathcal{B}^{3}=0$. If $\mathcal{B}^{2}=0$ then $\mathcal{B}$ is constant, so that in any case the kernel and image of $\mathcal{B}$ are constant; $\mathcal{B}$ may thus be assumed to take the form
$$\mathcal{B}=\left[\begin{array}{ccc}
\mu & \boldsymbol{i} \mu & \beta \\
\boldsymbol{i} \mu & -\mu & \boldsymbol{i} \beta \\
\beta & \boldsymbol{i} \beta & 0
\end{array}\right]$$
and the matrix Riccati equation yields
$$D \beta=0, \quad D \mu=2 \beta^{2} .$$
Hence $\beta$ is a constant, zero if and only if $\mathcal{B}$ is constant, and if $\beta$ is nonzero, then in a suitably translated affine coordinate $\mu=2 \beta^{2} r$. Thus there are three more cases.
\begin{itemize}
\item[III.] $\mathcal{B}^{3}=0$ and $\mathcal{B}^{2}$ is nowhere zero.
\item[N.] $\mathcal{B}^{2}=0$ and $\mathcal{B}$ is constant and nonzero.
\item[0.] $\mathcal{B}=0$.
\end{itemize}
Again the notation is justified by computing $\left\langle\mathcal{B}\left(e_{\zeta}\right), e_{\zeta}\right\rangle=\frac{1}{4}(\zeta-1)^{3}(\mu(\zeta-1)+2 \boldsymbol{i} \beta(\zeta+1))$.

\section*{Isomonodromic deformations}

Recall that, for $\Phi \in \mathrm{C}^{\infty}\left(C, \mathcal{E}^{*} \otimes \mathfrak{g}_{C}\right)$, the generalized Nahm equation (4.4) is
$$D \Phi-*[\Phi, \Phi]_{\mathfrak{g}}=\mathcal{B} \cdot \Phi .$$
I claim that this equation, for $\mathcal{B}$ not identically zero, is equivalent to the fact that
$$\mathrm{d}+\frac{\Phi}{\mathcal{B}}=\mathrm{d}+\frac{\Phi\left(e_{\zeta}\right) \mathrm{d} \zeta}{\left\langle\mathcal{B}\left(e_{\zeta}\right), e_{\zeta}\right\rangle}$$
is an isomonodromic family of connections on $\mathbb{C P}^{1}$ parameterized by $C$, with four poles along the base locus of the pencil of conics, where I use the tautological null vector field $e_{\zeta}$ (10.1) to clarify the meaning of the connection 1-form. More precisely, this follows from the fact that the meromorphic connection
$$\mathrm{d}+\frac{\Phi+\langle * \mathcal{B}, \Phi\rangle}{\mathcal{B}}=\mathrm{d}+\frac{\Phi\left(e_{\zeta}\right) \mathrm{d} \zeta+\left\langle * e_{\zeta} \wedge \mathcal{B}\left(e_{\zeta}\right), \Phi\right\rangle \mathrm{d} r}{\left\langle\mathcal{B}\left(e_{\zeta}\right), e_{\zeta}\right\rangle},$$
defined on the pullback of $\mathfrak{g}_{C}$ to the bundle of conics $\mathcal{S}(\mathcal{E})$ over the Riccati space $C$, is flat if and only if $\Phi$ satisfies the generalized Nahm equation.

This is a straightforward verification. Equivalently, if the gauge algebra $\mathfrak{g}_{C}$ is represented as a Lie algebra of vector fields, then this observation can be reformulated as the integrability of a rank two distribution on a bundle over $\mathcal{S}(\mathcal{E})$, and the poles of the connection can be viewed as points of $\mathcal{S}(\mathcal{E})$ over which the distribution is tangent to the fibres. Explicitly, in the above coordinates, two vector fields generating this distribution are
$$\begin{aligned}
& \left\langle\mathcal{B}\left(e_{\zeta}\right), e_{\zeta}\right\rangle \partial_{\zeta}+\Phi\left(e_{\zeta}\right), \\
& \partial_{r}+\left\langle\mathcal{B}\left(e_{\zeta}\right), e_{\zeta}^{\prime}\right\rangle \partial_{\zeta}+\Phi\left(e_{\zeta}^{\prime}\right),
\end{aligned}$$
where $e_{\zeta}^{\prime}=(\zeta, \boldsymbol{i}, \boldsymbol{i} \zeta)$. One can easily check that the distribution is closed under Lie bracket.
An advantage of this vector field interpretation is that it also makes sense on the trivial Riccati space $\mathcal{B}=0$, when (10.2) reduces to the standard Lax pair for the Nahm equation.

\section*{Addendum: Riccati spaces and integrability by the method of hydrodynamic reductions}

In [74], Ferapontov et al. independently discover the integrability of a system of equations equivalent to the generalized Nahm equations on Riccati spaces. Their study concerns equations of the form
$$\frac{\partial^{2}\left(A^{\alpha \beta}(u)\right)}{\partial x^{\alpha} \partial x^{\beta}}=0,$$
where $u=u\left(x^{1}, x^{2}, x^{3}\right)$ is a function of three variables, and $A^{\alpha \beta}$ is a 3 × 3 symmetric matrix of functions of one variable. (Here I use the summation convention on Greek indices; this may also be viewed as abstract index notation.) Expanding one derivative yields the equivalent formulation
$$\frac{\partial}{\partial x^{\alpha}}\left(V^{\alpha \beta}(u) \frac{\partial u}{\partial x^{\beta}}\right)=0,$$
where $V^{\alpha \beta}$ is the derivative of $A^{\alpha \beta}$ (i.e., $V=A^{\prime}$ ).
The approach in [74] characterizes integrability using the method of hydrodynamic reductions; this tests for the existence of sufficiently many multi-phase solutions $u=U\left(R^{1}, R^{2}, \ldots R^{N}\right)$, where the $R^{j}\left(x^{1}, x^{2}, x^{3}\right)$ are solutions to arbitrarily many commuting (1+1)-dimensional systems of hydrodynamic type. The result of this analysis is that (10.3) is integrable in this sense if and only if there is a scalar function $k(u)$ of one variable such that
$$V^{\prime \prime}(u)=(\log \operatorname{det} V)^{\prime}(u) V^{\prime}(u)+k(u) V(u)$$
or equivalently $\left(V^{\prime} / \operatorname{det}(V)\right)^{\prime}=k V$.
The relation to the Riccati space equation is subtle, and involves introducing a $u$-dependent triple of vectors $\theta_{\alpha}^{i}(u)(i=1,2,3)$ such that
$$V=(\operatorname{det} \theta) \theta^{-1}\left(\theta^{\mathrm{T}}\right)^{-1}, \quad \text { i.e., } \quad V^{\alpha \beta}=\sum_{i=1}^{3}(\operatorname{det} \theta)\left(\theta^{-1}\right)_{i}^{\alpha}\left(\theta^{-1}\right)_{i}^{\beta},$$
where $\theta=\left(\theta_{\alpha}^{i}\right)$ is assumed invertible. Now write $\mathcal{C}_{i j}:=\left(\theta^{-1}\right)_{i}^{\alpha}\left(\theta_{\alpha}^{j}\right)^{\prime}$ so that $\theta_{\alpha}^{i}=\sum_{j=1}^{3} \mathcal{C}_{i j} \theta_{\alpha}^{j}$. There is a gauge freedom in the choice of $\theta$, which may be used to suppose $\mathcal{C}$ is symmetric.

Substituting (10.5) into (10.4), straightforward computation, using the symmetry of $\mathcal{C}$ together with standard matrix identities such as $\left(A^{-1}\right)^{\prime}=-A^{-1} A^{\prime} A^{-1}$ and $(\operatorname{det} A)^{-1}(\operatorname{det} A)^{\prime}=$ $\operatorname{tr}\left(A^{-1} A^{\prime}\right)$, then yields
$$\mathcal{C}^{\prime}=2 \mathcal{C}^{2}-(\operatorname{tr} \mathcal{C}) \mathcal{C}+c I,$$
where $c$ is an unknown scalar function of $u$ (related to $k$ ).
Now decompose $\mathcal{C}=\mathcal{B}+a I$ with $\mathcal{B}$ tracefree; then the trace part of the above equation determines $c$, while the trace-free part is the Riccati equation for $\mathcal{B}$. Thus, remarkably, the hydrodynamic integrability condition agrees with the twistor-theoretic Riccati equation.

After classifying solutions of (10.4) (equivalently, solutions of the Riccati equation), Ferapontov et al. compute the form of the equation (10.3) for $u$ arising from each solution. They then observe that the central quadric Ansatz
$$x^{\alpha} M_{\alpha \beta}(u) x^{\beta}=1$$
for $u$ yields all Painlevé equations [74].

It is this geometry that originally led to the identification of (10.4) with the Riccati equation. The key observation is that (10.3) is a divergence form equation, meaning that $u$ is in the kernel of the Laplace-Beltrami operator of the metric $g_{\alpha \beta}(u)$ with $g=\operatorname{adj}(V)=(\operatorname{det} V) V^{-1}$ so that $V=\sqrt{\operatorname{det} g} g^{-1}$. Hence the equations in this class have the form
$$\mathrm{d} *_{g} \mathrm{~d} u=0,$$
where $g=g(u)$, and $*_{g}$ is the associated Hodge star operator. Now $\theta_{\alpha}^{i}(u)$ has an interpretation, as a framing of the metric $g$ :
$$g_{\alpha \beta}(u)=\sum_{i=1}^{3} \theta_{\alpha}^{i}(u) \theta_{\beta}^{i}(u) .$$
In terms of the geometry of $g, \theta$ is thus an $\mathbb{R}^{3}$-valued 1-form: on vector fields $X, Y$, the metric is $g(u)(X, Y)=\langle\theta(u) X, \theta(u) Y\rangle$. Thus there is a gauge freedom to rotate $\theta$ by an SO(3)-valued function of $u$ : this is the freedom used to make $\mathcal{C}_{i j}$ symmetric above (which in turn fixes $\theta$ up to a rigid rotation).

As will be explained in Section 11.2 (the last part of the next and final interlude), (10.3) is a hodograph transformation of the generalized Nahm equation with gauge group $\operatorname{SDiff}\left(\Sigma^{2}\right)$. The central quadric Ansatz corresponds to a reduction of gauge group from $\operatorname{SDiff}\left(\Sigma^{2}\right)$ to $\operatorname{SU}(2)$ (which acts by area preserving diffeomorphisms on the 2-sphere). This in turn explains the appearance of the Painlevé equations: generalized Nahm equations with gauge group $G$ describe isomonodromic deformation problems for $G$-connections on $\mathbb{C} P^{1}$ with four poles, and, when $G=\mathrm{SU}(2)$ (rank 2 bundles over $\mathbb{C} P^{1}$ ), the connection between such isomonodromy problems and the Painlevé equations is well known [35].

\section*{11 Interlude: the $\operatorname{Diff}(2)$ generalized Nahm equation}

This interlude is devoted to Weyl structures of the form (8.1). It follows from the work of Section 8, that these Weyl structures are Einstein-Weyl provided that $\mathcal{B}$ satisfies the matrix Riccati equation and $\Phi^{i}=\phi^{i} \partial_{p}+\psi^{i} \partial_{q}(i=1,2,3)$ defines a generalized Nahm field on this Riccati space, the gauge group being a subgroup of $\operatorname{Diff}\left(\Sigma^{2}\right)$ where $\Sigma^{2}$ is a surface with coordinates $p$, $q$.

However, as details were omitted in Section 8, I present a self-contained study of these Weyl structures in the following two cases:
\begin{itemize}
\item[(i)] $\mathcal{B}=0$ (so the Riccati space is trivial);
\item[(ii)] the $\Phi^{i}$ are area preserving vector fields.
\end{itemize}

These examples have an interest that stretches beyond the proscenium of Einstein-Weyl geometry, since they are closely related both to well-known integrable systems, and also to hypercomplex, hyperkähler and scalar-flat Kähler structures in four dimensions.

\subsection*{11.1 HyperCR Einstein-Weyl spaces and the Diff(2) Nahm equation}

In Section 9, hyperCR Einstein-Weyl spaces were related to the $\operatorname{Diff}\left(S^{1}\right)$ Hitchin equation. Now it is known [8, 22] that any solution of the $\operatorname{Diff}\left(S^{1}\right)$ Einstein-Weyl Bogomolny equation on a hyperCR Einstein-Weyl space gives rise to a hypercomplex 4-manifold (which is sometimes hyperkähler).

This two step construction ties in with the construction of hypercomplex and hyperkähler structures from the $\operatorname{Diff}\left(\Sigma^{2}\right)$ Hitchin equation: see Section 7. On the other hand, also in Section 7, hypercomplex and hyperkähler structures were related to the $\operatorname{Diff}\left(\Sigma^{3}\right)$ Nahm equation,
so it is natural to expect that hyperCR Einstein-Weyl spaces may be constructed from the $\operatorname{Diff}\left(\Sigma^{2}\right)$ Nahm equation.

In fact this is not hard to see. Suppose that $D=D^{g}+\omega$ is a Weyl structure given by
$$g=\eta_{1}^{2}+\eta_{2}^{2}+\eta_{3}^{2}, \quad \omega=-\frac{\sum_{i, j, k} \varepsilon_{i j k} \nu_{i}\left(\phi_{p}^{j}+\psi_{q}^{j}\right) \eta_{k}}{\nu_{1}^{2}+\nu_{2}^{2}+\nu_{3}^{2}},$$
where
$$\begin{aligned}
& \eta_{i}=\nu_{i} \mathrm{~d} r+\phi^{i} \mathrm{~d} q-\psi^{i} \mathrm{~d} p \\
& \nu_{1}=\phi^{2} \psi^{3}-\phi^{3} \psi^{2}, \quad \nu_{2}=\phi^{3} \psi^{1}-\phi^{1} \psi^{3}, \quad \nu_{3}=\phi^{1} \psi^{2}-\phi^{2} \psi^{1},
\end{aligned}$$
and
$$\Phi=\left(\phi^{1}, \phi^{2}, \phi^{3}\right) \partial_{p}+\left(\psi^{1}, \psi^{2}, \psi^{3}\right) \partial_{q} .$$
The Nahm equation expands to give
$$\phi_{r}^{1}=\phi^{2} \phi_{p}^{3}-\phi^{3} \phi_{p}^{2}+\psi^{2} \phi_{q}^{3}-\psi^{3} \phi_{q}^{2}, \quad \psi_{r}^{1}=\phi^{2} \psi_{p}^{3}-\phi^{3} \psi_{p}^{2}+\psi^{2} \psi_{q}^{3}-\psi^{3} \psi_{q}^{2}$$
and cyclic permutations. From this it follows easily that $\mathrm{d} \eta_{1}+\omega \wedge \eta_{1}=\kappa \eta_{2} \wedge \eta_{3}$ (and similarly for the cyclic permutations), where
$$\kappa=\frac{\nu_{1}\left(\phi_{p}^{1}+\psi_{q}^{1}\right)+\nu_{2}\left(\phi_{p}^{2}+\psi_{q}^{2}\right)+\nu_{3}\left(\phi_{p}^{3}+\psi_{q}^{3}\right)}{\nu_{1}^{2}+\nu_{2}^{2}+\nu_{3}^{2}} .$$
Hence the Weyl structure is hyperCR Einstein-Weyl. Note that if the Nahm field preserves the (a priori arbitrary) area form $\mathrm{d} p \wedge \mathrm{~d} q$ then $\kappa=0$ and the Einstein-Weyl space is flat. Ward [60] uses this fact to linearize the Nahm equation in this case.

In fact any hyperCR Einstein-Weyl space $B$ arises locally from this construction. One way to see this is to choose an Abelian monopole on $B$. This defines a hypercomplex structure with a triholomorphic vector field $K$ tangent to the fibres over $B$. For example, $\kappa$ is an Abelian monopole on any hyperCR Einstein-Weyl space and the corresponding hypercomplex structure is hyperkähler with a triholomorphic homothetic vector field [22].

Now let $r$ be a solution of $\Delta r=0$, which is constant on the fibres over $B$, where $\Delta$ is the Laplacian of the Obata connection. This defines a divergence-free coframe $\mathrm{d} r, I \mathrm{~d} r, J \mathrm{~d} r, K \mathrm{~d} r$ and a dual frame of vector fields $V_{0}, V_{1}, V_{2}, V_{3}$. Since $r$ is constant on the fibres over $B, K$ is tangent to the level surfaces of $r$, so it is in the span of $V_{1}, V_{2}, V_{3}$ and commutes with them all (since it is triholomorphic). Therefore the gauge group of the Nahm field defined by $V_{1}, V_{2}, V_{3}$ reduces to the group of diffeomorphisms of $\Sigma^{3}$ commuting with the flow of $K$. Taking the local quotient by $K$ gives a Nahm field with gauge group $\operatorname{Diff}\left(\Sigma^{2}\right)$ for some surface $\Sigma^{2}$, and this is clearly a Nahm field giving rise to the Einstein-Weyl space $B$.

Theorem 11.1. Let $\Phi$ be a solution of the Nahm equation with gauge group $\operatorname{Diff}\left(\Sigma^{2}\right)$ for some surface $\Sigma^{2}$. Then the Einstein-Weyl space defined by $\Phi$ is hyperCR, and any hyperCR Einstein-Weyl space arises locally in this way. If there is a reduction to $\operatorname{SDiff}\left(\Sigma^{2}\right)$, the Einstein-Weyl space is flat.

There is a great deal more freedom in this construction than in the $\operatorname{Diff}\left(S^{1}\right)$ Hitchin construction of hyperCR Einstein-Weyl spaces, which can be an advantage or a drawback, since the same hyperCR Einstein-Weyl space will arise in many ways. There are some interesting special cases one could consider, such as the group $\mathrm{SL}(2, \mathbb{C})$ acting on $\mathbb{C P}^{1}$ (which does not preserve an area form). The Nahm equations in this case reduce to a (complexified) Euler top equation, solvable in terms of elliptic functions.

\subsection*{11.2 The SDiff(2) generalized Nahm equation}

In addition to hyperCR Einstein-Weyl spaces, another important class consists of the Einstein-Weyl spaces arising from solutions of the $\mathrm{SU}(\infty)$ Toda field equation $u_{x x}+u_{y y}+\left(e^{u}\right)_{z z}=0$ [39, 55, 60]. The terminology originates by regarding the equation as a dispersionless limit of the $\operatorname{SU}(N)$ Toda equation as $N \rightarrow \infty$ : the Toda equation is a two-dimensional system with independent variables $(x, y)$; the $z$ variable is normally discrete, but becomes continuous in the limit. The large $N$ limit of $\operatorname{SU}(N)$ may be interpreted as the group $\operatorname{SDiff}\left(S^{1} \times S^{1}\right)$ of area preserving diffeomorphisms of a torus, with its Lie algebra $\mathbb{Z}$-graded by the Fourier components in one of the circles. There is a potential source of confusion here, however, since the $\mathrm{SU}(\infty)$ Toda equation is related to area preserving diffeomorphisms in another way. Namely, each solution gives rise to a hyperkähler metric with a Killing vector $K$ [6], and hyperkähler metrics are in turn obtained from the $\operatorname{SDiff}\left(\Sigma^{2}\right)$ Hitchin equations on $\mathbb{R}^{2}$, as shown in Theorem 7.6 (cf. [62]). Hence one expects the $\operatorname{SU}(\infty)$ Toda equation to be equivalent to a symmetry reduction of the $\operatorname{SDiff}\left(\Sigma^{2}\right)$ Hitchin equations to one dimension.
![](https://cdn.mathpix.com/cropped/c46dd08a-362a-481e-81e9-d664e136643a-43.jpg?height=320&width=514&top_left_y=926&top_left_x=830)

The Einstein-Weyl structure on a Toda Einstein-Weyl space $B^{3}$ is given by the metric and Weyl 1-form
$$h=e^{u}\left(\mathrm{~d} x^{2}+\mathrm{d} y^{2}\right)+\mathrm{d} z^{2}, \quad \omega_{h}=-u_{z} \mathrm{~d} z .$$
In these geometric terms, the $\mathrm{SU}(\infty)$ Toda equation may be written $\mathrm{d} *_{h} \mathrm{~d} u=0$, and so $*_{h} \mathrm{~d} u$ is a closed 2-form, which is therefore locally of the form $\mathrm{d} p \wedge \mathrm{~d} q$. Now ( $p, q, u$ ) will be functionally independent unless $0=\mathrm{d} u \wedge *_{h} \mathrm{~d} u=*_{h}|\mathrm{~d} u|^{2}$. Hence (in Euclidean signature), ( $p, q, u$ ) may be used as coordinates, except in the trivial case ( $u$ constant). The solution of the Toda equation is now given implicitly by the functions $(x, y, z)$ of $(p, q, u)$. These functions will turn out to satisfy a generalized Nahm equation on the type (D) Riccati space with gauge group $\operatorname{SDiff}\left(\Sigma^{2}\right)$.

In order to see this, and relate it to the work of Ferapontov et al. [74], consider the generalized Nahm equation on any Riccati space with affine coordinate $r$, where the Higgs fields $\Phi^{i}=$ $\phi^{i} \partial_{p}+\psi^{i} \partial_{q}$ preserve the area form $\mathrm{d} p \wedge \mathrm{~d} q$ on a surface $\Sigma^{2}$ with coordinates $(p, q)$. Motivated by the general construction of Section 8, introduce the Weyl structure
$$g=\eta_{1}^{2}+\eta_{2}^{2}+\eta_{3}^{2}, \quad \omega=2 \frac{\lambda_{1} \nu_{1} \eta_{1}+\lambda_{2} \nu_{2} \eta_{2}+\lambda_{3} \nu_{3} \eta_{3}}{\nu_{1}^{2}+\nu_{2}^{2}+\nu_{3}^{2}},$$
where
$$\begin{aligned}
& \eta_{i}=\nu_{i} \mathrm{~d} r+\phi^{i} \mathrm{~d} q-\psi^{i} \mathrm{~d} p \\
& \nu_{1}=\phi^{2} \psi^{3}-\phi^{3} \psi^{2}, \quad \nu_{2}=\phi^{3} \psi^{1}-\phi^{1} \psi^{3}, \quad \nu_{3}=\phi^{1} \psi^{2}-\phi^{2} \psi^{1} .
\end{aligned}$$
The metric $g$ can be simplified considerably using the fact that area preserving vector fields are locally hamiltonian: this means one can write $\phi^{i}=F^{i}{ }_{q}$ and $\psi^{i}=-F^{i}{ }_{p}$ for some functions $F^{1}, F^{2}, F^{3}$ of $(p, q, r)$. The ( $r$-dependent) constants of integration for the hamiltonians may be chosen so that the $F^{i}$ satisfy the generalized Nahm equation in the Lie algebra of functions
under Poisson bracket: $F^{1}{ }_{r}-\left\{F^{2}, F^{3}\right\}=\sum_{j} \mathcal{B}_{1 j} F^{j}$ and so on. (The system $p^{i}{ }_{r}-\sum_{j} \mathcal{B}_{i j} p^{i}=q^{i}$ has local solutions for any $q^{i}(r)$, and these can be added to $F^{i}$. However, if the $\Phi^{i}$ take values in a Lie subalgebra of the area preserving vector fields, then the $F^{i}$ may take values in a central extension of this Lie subalgebra.) The metric now reduces to
$$g=\sum_{i}\left(\mathrm{~d} F^{i}-\sum_{j} \mathcal{B}_{i j} F^{j} \mathrm{~d} r\right)^{2}=\sum_{i} \theta_{\alpha}^{i}(r) \theta_{\beta}^{i}(r) \mathrm{d} x^{\alpha} \mathrm{d} x^{\beta},$$
where $\theta_{\alpha}^{i}$ is a basis of solutions to the linear system $\theta^{i}{ }_{r}=\sum_{j} \mathcal{B}_{i j} \theta^{j}$ and, using the summation convention on Greek indices, $F^{i}=\theta_{\alpha}^{i} x^{\alpha}$, for some functions $x^{\alpha}(p, q, r)(\alpha=1,2,3)$. The equation $F^{i}{ }_{r}-\frac{1}{2} \sum_{j, k} \varepsilon_{i j k}\left\{F^{j}, F^{k}\right\}=\sum_{j} \mathcal{B}_{i j} F^{j}$ is immediately equivalent to
$$\theta_{\alpha}^{i} x^{\alpha}{ }_{r}=\sum_{j, k} \varepsilon_{i j k} \theta_{\alpha}^{j} \theta_{\beta}^{k}\left\{x^{\alpha}, x^{\beta}\right\} .$$
Now for any functions $x^{\alpha}(p, q, r)$ direct calculations yield the general jacobian identities
$$\begin{aligned}
& \left\{x^{2}, x^{3}\right\} \mathrm{d} x^{1}+\left\{x^{3}, x^{1}\right\} \mathrm{d} x^{2}+\left\{x^{1}, x^{2}\right\} \mathrm{d} x^{3}=J(x) \mathrm{d} r, \\
& x^{1}{ }_{r} \mathrm{~d} x^{2} \wedge \mathrm{~d} x^{3}+x^{2}{ }_{r} \mathrm{~d} x^{3} \wedge \mathrm{~d} x^{1}+x^{3}{ }_{r} \mathrm{~d} x^{1} \wedge \mathrm{~d} x^{2}=J(x) \mathrm{d} p \wedge \mathrm{~d} q,
\end{aligned}$$
where $J(x)$ is the determinant of the jacobian of $\left(x^{1}, x^{2}, x^{3}\right)$ with respect to $(p, q, r)$. Hence (11.1) holds if and only if $*_{g} \mathrm{~d} r=\mathrm{d} p \wedge \mathrm{~d} q$.

This argument was carried out using an affine coordinate $r$. However, any coordinate $t$ can be used, simply by writing $\partial_{t}=\partial_{r}+a$. The following result summarizes the general construction.

Proposition 11.2. Consider the 3-dimensional metric
$$g=\sum_{i}\left(\theta_{\alpha}^{i}(t) \mathrm{d} x^{\alpha}\right)^{2},$$
where $\theta_{\alpha}^{i}$ is a basis of solutions of the linear system $\theta^{i}{ }_{t}-a \theta^{i}=\sum_{j} \mathcal{B}_{i j} \theta^{j}$ for some symmetric traceless matrix $\mathcal{B}_{i j}(t)$, and $x^{\alpha}(p, q, t)$ are arbitrary functions. Then $*_{g} \mathrm{~d} t=\mathrm{d} p \wedge \mathrm{~d} q$ if and only if the functions $F^{i}=\theta_{\alpha}^{i} x^{\alpha}$ satisfy
$$F_{t}^{i}-a F^{i}-\frac{1}{2} \sum_{j, k} \varepsilon_{i j k}\left\{F^{j}, F^{k}\right\}=\sum_{j} \mathcal{B}_{i j} F^{j} .$$

Remark 11.3. We pause briefly to reiterate (conversely) the link between this analysis and the work of Ferapontov et al. [74]. The framing $\theta_{\alpha}^{i}$ of the metric $g$ appearing in $\mathrm{d} *_{g} \mathrm{~d} u=0$, i.e., the formulation (10.6) of (10.3), provides a diagonalization
$$g_{\alpha \beta} \mathrm{d} x^{\alpha} \mathrm{d} x^{\beta}=\sum_{i=1}^{3}\left(\theta_{\alpha}^{i} \mathrm{~d} x^{\alpha}\right)^{2}=\sum_{i=1}^{3}\left(\mathrm{~d} F^{i}-(\mathcal{C} F)^{i} \mathrm{~d} u\right)^{2},$$
where $F^{i}=\theta_{\alpha}^{i} x^{\alpha},(\mathcal{C} F)^{i}=\sum_{i=1}^{3} \mathcal{C}_{i j} F^{j}$. Writing $*_{g} \mathrm{~d} u=\mathrm{d} p \wedge \mathrm{~d} q$ yields
$$\left(F^{i}\right)^{\prime}-\frac{1}{2} \sum_{i, j, k} \varepsilon_{i j k}\left\{F^{j}, F^{k}\right\}=\sum_{j} \mathcal{C}_{i j} F^{j},$$
which reduces to the generalized Nahm equation after splitting $\mathcal{C}$ into its tracefree and tracelike parts.

Returning to the $\mathrm{SU}(\infty)$ Toda equation, $\left(\theta_{\alpha}^{i}\right)$ is now a diagonal matrix with eigenvalues $\left(e^{u / 2}, e^{u / 2}, 1\right)$. The case that $u$ is constant (so that $\mathcal{B}=0$ ) is the overlap with the previous subsection, and this construction recovers Ward's linearization of the $\mathrm{SU}(\infty)$ Nahm equation [61]. On the other hand if $u$ is not constant, $t=u$ can be used as a coordinate, so that $a=1 / 3$ and $\mathcal{B}_{i j}$ is diagonal with constant eigenvalues $1 / 6,1 / 6,-1 / 3$. This is the type (D) solution of the matrix Riccati equation with $\lambda=1 / 6$ (see Remark 10.3).

There is another class of Einstein-Weyl spaces, governed by the dKP equation [18]. The Weyl structure in this case is Lorentzian:
$$h=\mathrm{d} y^{2}-4 \mathrm{~d} x \mathrm{~d} t-4 u \mathrm{~d} t^{2}, \quad \omega_{h}=2 u_{x} \mathrm{~d} t .$$
The Einstein-Weyl condition may again be written $\mathrm{d} *_{h} \mathrm{~d} u=0$, which now reduces to the dKP equation $u_{y y}=\left(u_{t}-u u_{x}\right)_{x}$. If the solutions $\left(\theta_{\alpha}^{i}\right)$ are taken to be $(1+u, 2 \boldsymbol{i} u, 0),(2 \boldsymbol{i} u, 1-u, 0)$ and (0, 0, 1), then $h=\sum_{i, \alpha, \beta} \theta_{\alpha}^{i}(r) \theta_{\beta}^{i}(r) \mathrm{d} x^{\alpha} \mathrm{d} x^{\beta}$ with $-\sqrt{2} t=x^{1}+\boldsymbol{i} x^{2}, 2 \sqrt{2} x=x^{1}-\boldsymbol{i} x^{2}, y=x^{3}$, whereas $\mathcal{B}$ is the type (N) solution of the Riccati equation. The equivalence works as long as $|\mathrm{d} u|_{h} \neq 0$.

Theorem 11.4. The $\operatorname{SU}(\infty)$ Toda and $d K P$ equations are generically locally equivalent to $\operatorname{SDiff}\left(\Sigma^{2}\right)$ generalized Nahm equations, on the type (D) and (N) Riccati space respectively.

The equivalence in each case is obtained by a "hodograph transformation", i.e., dependent and independent variables are exchanged. The beauty of such transformations is that they interchange coordinate-invariance and gauge-invariance, which is why they are potentially useful for studying geometric differential equations, where the independent variables are often not well defined.

This result was first obtained in for the $\operatorname{SU}(\infty)$ Toda equation and type (D) Nahm equation. The extension to more general Nahm equations resulted from discussions with Maciej Dunajski. Together with Paul Tod, he has given a detailed discussion of the dKP case [20].

Solutions of the $\operatorname{SU}(\infty)$ Toda equation may be divided into two classes according to whether they are most easily presented explicitly or implicitly: in the former class, there are very few examples - to the best of my knowledge, the only examples are the separable solutions [6, 23] and the hyperCR-Toda solutions [11] (the latter were discussed in Section 9).

The class of implicit solutions is much richer and all of them (that I know of) are obtained by the above hodograph transformation. There are two general classes.

\section*{Solutions with a Killing vector [10, 60]}

Suppose that the generalized Nahm field is invariant under a one-dimensional symmetry group of $\Sigma^{2}$, generated by a hamiltonian vector field $X$, with momentum map $\eta$, and let $\psi$ be a function on $\Sigma^{2}$ with $\mathrm{d} \psi(X)=1$. Then $\psi, \eta$ can be used as coordinates on $\Sigma^{2}, X=\partial_{\psi}$ and the area form is $\mathrm{d} \psi \wedge \mathrm{d} \eta$. The Lie algebra of hamiltonian vector fields commuting with $\partial_{\psi}$ consists of vector fields of the form $b \partial_{\eta}+W(\eta) \partial_{\psi}$, where $b$ is constant (on $\Sigma^{2}$ ), and the hamiltonian is $-b \psi+V(\eta)$ where $V_{\eta}=W$. The solutions found by Ward [60] are given by the metric
$$h=\rho^{2}\left(\mathrm{~d}\left(U_{\eta}\right)^{2}+\mathrm{d} \psi^{2}\right)+\mathrm{d}\left(\rho U_{\rho}\right)^{2},$$
where $U(\rho, \eta)$ satisfies $\left(\rho U_{\rho}\right)_{\rho}+\rho U_{\eta \eta}=0$, the equation for axisymmetric harmonic functions on $\mathbb{R}^{3}$. In this case one of the hamiltonians is simply $\psi$. The general solutions were found in [10] following similar ideas.

\section*{Solutions constant on central ellipsoids [55]}

Motivated by the Pedersen-Poon Ansatz for scalar-flat Kähler metrics [47], Tod [55] observed that solutions of the Toda equation which are constant on central ellipsoids may be obtained from an ordinary differential equation, namely Painlevé's third equation. Painlevé III is equivalent to the isomonodromic deformation problem for an SU(2) connection with two double poles, and hence to the generalized Nahm equation with gauge group SU(2) on the type (D) Riccati space. Tod's solutions are obtained by reducing to the gauge algebra $\mathfrak{s o}(3)$ of infinitesimal isometries of $S^{2}$. Solutions constant on central ellipsoids arise in this way because ellipsoids are precisely the quotients of left invariant metrics on $S^{3}=\operatorname{SU}(2)$ by a U(1) subgroup.

Similar reductions are known in the dKP case - see [18, 20] - and the latter construction is the context for the central quadric Ansatz and Painlevé equations of [74].

\section*{12 Further speculations}

The integrable background geometries discussed in this paper are those arising from the selfduality equation for conformal structures in four dimensions. Roughly speaking, they are characterized as geometries associated to a twistor space containing rational curves with degree 2 normal bundle, although this requires some interpretation for the one or two-dimensional geometries, where the twistor space is not Hausdorff and has dimension zero or one respectively.

Null reductions lead to twistor spaces with lower degree normal bundles. For instance, a surface with a projective structure may be viewed as a moduli space of rational curves in a complex surface with normal bundle $\mathcal{O}(1)$ (see Hitchin [32] and LeBrun [38]).

These considerations lead to the idea of extending the integrable background geometry concept to higher degree normal bundles. This would encompass the Einstein-Weyl and selfdual hierarchies (where the normal bundle is $\mathcal{O}(n)$ or $\mathcal{O}(n) \otimes \mathbb{C}^{2}$ respectively), as well as quaternionic geometry (normal bundle $\mathcal{O}(1) \otimes \mathbb{C}^{2 k}$ ).

In the language of integrable systems, the concept of a background geometry appears to be related to Lax systems involving a derivative with respect to the spectral parameter $\zeta$. The zeros of the coefficient of $\partial_{\zeta}$ are associated with poles of the Lax system: the prototype here is the one-dimensional case (isomonodromic deformations). In its most general form, the background geometry idea might be regarded as a study of these extra $\partial_{\zeta}$ terms: general principles for the introduction of such terms have been developed by Burtsev-Zakharov-Mikhailov [7]. At the very least, it is desirable to know when these terms can be eliminated. For the geometries studied in this paper, this question has an answer: they can be eliminated provided that the background geometry is a trivial Riccati space, a trivial or spherical spinor-vortex space, a hyperCR Einstein-Weyl space, or a hypercomplex selfdual space.

Returning to the general context of this paper, recent work of Ferapontov and Kruglikov [75] suggest deep links between selfduality (hence twistor theory) and integrability in low dimensions, going beyond the inspirational analysis by Mason and Woodhouse. For example, in the particular case of equations of the form (10.6), the Einstein-Weyl structure may be recovered from the linearization $\mathrm{d} *_{g(u)} \mathrm{d} v+\mathrm{d}\left(v *_{g}{ }^{\prime}(u) \mathrm{d} u\right)=0$. The leading term in $v$ is
$$g^{\alpha \beta}(u) \frac{\partial^{2} v}{\partial x^{\alpha} \partial x^{\beta}},$$
so the symbol of the linearized equation is the inverse metric $g^{-1}$ (up to a conformal factor) of the Einstein-Weyl structure. Ferapontov and Kruglikov also show how to recover (the 1-form of) the Weyl structure. They obtain a similar result for several classes of PDEs, relating the integrability of such equations (by the method of hydrodynamic reductions) to Einstein-Weyl or selfdual conformal structures on their moduli spaces.

\section*{A Table of integrable background geometries}

The following table summarizes the background equations and gauge field equations in each dimension (given in Euclidean signature for convenience).

In this table, I indicate the data defining the background geometry, starting with the conformal manifold $Q$ and the conformal vector bundle $\mathcal{V}=L, \mathcal{W}$, or $\mathcal{E}$ (which has rank 1, 2, or 3 respectively) followed by the other data: $D$ is a conformal connection on $\mathcal{V}, \bar{\partial}^{a}$ a holomorphic structure, whereas $\mathcal{C}, \psi, \mathcal{B}$ are sections of $\mathcal{W}^{*} \otimes_{\mathbb{C}} \mathcal{W}^{*} \otimes_{\mathbb{C}} T N, \mathcal{W}^{*} \otimes_{\mathbb{C}} T N$ and $T^{*} C \otimes \operatorname{Sym}_{0} \mathcal{E}$ respectively.

The gauge field equations are for a pair $(A, \Phi)$, where $A$ is a $G$-connection and the Higgs field $\Phi$ is an $\mathfrak{g}_{Q}$-valued section of $\mathcal{V}^{*}$, except that in four dimensions there is no Higgs field, and in one dimension, the connection $A$ can be assumed trivial.

\begin{tabular}[t]{|l|l|l|l|}
\hline Dimension & Data & Background equations & Gauge field equations \\
\hline 4 Selfdual & $M$ & $W^{-}=0$ & $* F^{A}=F^{A}$ \\
\hline 3 Einstein-Weyl & $(B, L), D$ & $r_{0}^{D}=0$ & $* D^{A} \Phi=F^{A}$ \\
\hline 2 Spinor-vortex & $(N, \mathcal{W})$, $\left(\bar{\partial}^{a}, \mathcal{C}, \psi\right)$ & $$\begin{gathered}
\bar{\partial}^{a} \mathcal{C}=0 \\
\bar{\partial}^{a} \psi=-3 \mathcal{C} \bar{\psi} \\
s_{\mathcal{W}^{-1} T N}=\psi \bar{\psi}-2 \mathcal{C} \overline{\mathcal{C}}
\end{gathered}$$ & $$\begin{gathered}
F^{A}-[\Phi, \bar{\Phi}]_{\mathfrak{g}}=\psi \wedge \bar{\Phi}+\bar{\psi} \wedge \Phi, \\
\bar{\partial}^{a, A} \Phi=\mathcal{C} \bar{\Phi}
\end{gathered}$$ \\
\hline 1 Riccati & $(C, \mathcal{E}),(D, \mathcal{B})$ & $D \mathcal{B}=2\left(\mathcal{B}^{2}\right)_{0}$. & $D^{A} \Phi-*[\Phi, \Phi]_{\mathfrak{g}}=\mathcal{B} \cdot \Phi$ \\
\hline
\end{tabular}

Finally, I summarize the background geometry constructions in an $\operatorname{SDiff}(\Sigma)$-gauge, i.e., using an arbitrarily chosen volume form $\nu$ on $\Sigma\left(\nu=\mathrm{d} t\right.$ on $\left.\Sigma^{1}\right)$.

\section*{Selfdual spaces}
\begin{itemize}
\item[-] From Einstein-Weyl spaces:
$$g=\Phi^{2} \mathrm{c}_{B}+(\mathrm{d} t+A)^{2} .$$
\item[-] From spinor-vortex spaces (with conformal coordinate $z$ ):
$$g=|\nu(\Phi, \bar{\Phi})|^{2} \mathrm{~d} z \mathrm{~d} \bar{z}+\langle\nu(\Phi, \cdot)+\nu(\Phi, A), \nu(\bar{\Phi}, \cdot)+\nu(\bar{\Phi}, A)\rangle .$$
\item[-] From Riccati spaces (with affine coordinate $r$ ):
$$g=|\nu(\Phi \times \Phi \times \Phi)|^{2} \mathrm{~d} r^{2}+|\nu(\Phi \times \Phi, \cdot)|^{2} .$$
\end{itemize}

\section*{Einstein-Weyl spaces}
\begin{itemize}
\item[-] From spinor-vortex spaces (with conformal coordinate $z$ ):
$$\begin{aligned}
& g=4 \Phi \bar{\Phi} \mathrm{~d} z \mathrm{~d} \bar{z}+(\mathrm{d} t+\alpha \mathrm{d} z+\bar{\alpha} \mathrm{d} \bar{z})^{2}, \\
& \omega=\dot{A}-\frac{2 \overline{\mathcal{C}} \Phi}{\bar{\Phi}} \mathrm{~d} z-\frac{2 \mathcal{C} \bar{\Phi}}{\Phi} \mathrm{~d} \bar{z}-\frac{1}{2}\left(\frac{\psi+\dot{\Phi}}{\Phi}+\frac{\bar{\psi}+\dot{\bar{\Phi}}}{\bar{\Phi}}\right)(\mathrm{d} t+\alpha \mathrm{d} z+\bar{\alpha} \mathrm{d} \bar{z}) .
\end{aligned}$$
\item[-] From Riccati spaces (with affine coordinate $r$ ):
$$\begin{aligned}
& g=|\nu(\Phi \times \Phi) \mathrm{d} r+\nu(\Phi, \cdot)|^{2}, \\
& \omega=\frac{\left\langle 2 \mathcal{B}(\nu(\Phi \times \Phi))-\nu(\Phi \times \Phi) \times \operatorname{div}_{\nu} \Phi, \nu(\Phi \times \Phi) \mathrm{d} r+\nu(\Phi, \cdot)\right\rangle}{|\nu(\Phi \times \Phi)|^{2}} .
\end{aligned}$$
\end{itemize}

\section*{Spinor-vortex spaces from Riccati spaces}
$\mathcal{W}$ is the kernel of $\Phi$ in the pullback of $\mathcal{E}$ to $C \times \Sigma^{1}$ with complex structure given by cross product with $\Phi /|\Phi|$ and holomorphic structure induced by the conformal connection
$$D+\frac{\left(\Phi_{r} \triangle \Phi+\langle\mathcal{B} \Phi, \Phi\rangle \mathrm{id}\right) \mathrm{d} r+\dot{\Phi} \triangle \Phi \mathrm{d} t}{|\Phi|^{2}},$$
the conformal structure is represented by $g=|\Phi|^{2} \mathrm{~d} r^{2}+\mathrm{d} t^{2}$ and the other two fields are
$$\begin{aligned}
\mathcal{C} & =\mathcal{B}-\frac{\mathcal{B} \Phi \otimes \Phi+\Phi \otimes \mathcal{B} \Phi}{|\Phi|^{2}}+\frac{\langle\mathcal{B} \Phi, \Phi\rangle}{2|\Phi|^{2}}\left(\operatorname{id}+\frac{\Phi \otimes \Phi}{|\Phi|^{2}}\right) \\
\psi & =\frac{\Phi \times(2 \mathcal{B} \Phi+\Phi \times \dot{\Phi})}{|\Phi|^{2}} .
\end{aligned}$$

\section*{Acknowledgements}

I would like to thank Harry Braden, Maciej Dunajski, Evgeny Ferapontov, Paul Gauduchon, Nigel Hitchin, Boris Kruglikov, Claude LeBrun, Lionel Mason, Ian Strachan, Paul Tod and Nick Woodhouse for helpful discussions. This work was supported by the EPSRC, the Leverhulme Trust, and the William Gordon Seggie Brown Trust.

\section*{References}
\begin{itemize}
\item[] [1] Ablowitz M.J., Clarkson P.A., Solitons, nonlinear evolution equations and inverse scattering, London Mathematical Society Lecture Note Series, Vol. 149, Cambridge University Press, Cambridge, 1991.
\item[] [2] Ashtekar A., Jacobson T., Smolin L., A new characterization of half-flat solutions to Einstein's equation, Comm. Math. Phys. 115 (1988), 631-648.
\item[] [3] Atiyah M., Hitchin N., The geometry and dynamics of magnetic monopoles, M.B. Porter Lectures, Princeton University Press, Princeton, NJ, 1988.
\item[] [4] Atiyah M.F., Hitchin N.J., Singer I.M., Self-duality in four-dimensional Riemannian geometry, Proc. Roy. Soc. London Ser. A 362 (1978), 425-461.
\item[] [5] Atiyah M.F., Ward R.S., Instantons and algebraic geometry, Comm. Math. Phys. 55 (1977), 117-124.
\item[] [6] Boyer C.P., Finley J.D., Killing vectors in self-dual, Euclidean Einstein spaces, J. Math. Phys. 23 (1982), 1126-1130.
\item[] [7] Burtsev S.P., Zakharov V.E., Mikhailov A.V., Inverse scattering method with variable spectral parameter, Theoret. and Math. Phys. 70 (1987), 227-240.
\item[] [8] Calderbank D.M.J., Selfdual Einstein metrics and conformal submersions, math.DG/0001041.
\item[] [9] Calderbank D.M.J., Mason L.J., Spinor-vortex geometry and microtwistor theory, unpublished, 2002.
\item[] [10] Calderbank D.M.J., Pedersen H., Selfdual spaces with complex structures, Einstein-Weyl geometry and geodesics, Ann. Inst. Fourier (Grenoble) 50 (2000), 921-963, math.DG/9911117.
\item[] [11] Calderbank D.M.J., Tod P., Einstein metrics, hypercomplex structures and the Toda field equation, Differential Geom. Appl. 14 (2001), 199-208, math.DG/9911121.
\item[] [12] Cartan É., Sur une classe d'espaces de Weyl, Ann. Sci. École Norm. Sup. (3) 60 (1943), 1-16.
\item[] [13] Chakravarty S., Mason L., Newman E.T., Canonical structures on anti-self-dual four-manifolds and the diffeomorphism group, J. Math. Phys. 32 (1991), 1458-1464.
\item[] [14] Dancer A.S., Scalar-flat Kähler metrics with SU(2) symmetry, J. Reine Angew. Math. 479 (1996), 99-120.
\item[] [15] Dancer A.S., Strachan I.A.B., Cohomogeneity-one Kähler metrics, in Twistor Theory (Plymouth), Lecture Notes in Pure and Appl. Math., Vol. 169, Dekker, New York, 1995, 9-27.
\item[] [16] Dubrovin B., Geometry of 2D topological field theories, in Integrable Systems and Quantum Groups (Montecatini Terme, 1993), Lecture Notes in Math., Vol. 1620, Springer, Berlin, 1996, 120-348, hep-th/9407018.
\end{itemize}
\begin{itemize}
\item[] [17] Dunajski M., The twisted photon associated to hyper-Hermitian four-manifolds, J. Geom. Phys. 30 (1999), 266-281, math.DG/9808137.
\item[] [18] Dunajski M., Mason L.J., Tod P., Einstein-Weyl geometry, the dKP equation and twistor theory, J. Geom. Phys. 37 (2001), 63-93, math.DG/0004031.
\item[] [19] Dunajski M., Mason L.J., Woodhouse N.M.J., From 2D integrable systems to self-dual gravity, J. Phys. A: Math. Gen. 31 (1998), 6019-6028, solv-int/9809006.
\item[] [20] Dunajski M., Tod P., Einstein-Weyl spaces and dispersionless Kadomtsev-Petviashvili equation from Painlevé I and II, Phys. Lett. A 303 (2002), 253-264, nlin.SI/0204043.
\item[] [21] Gauduchon P., Structures de Weyl-Einstein, espaces de twisteurs et variétés de type $S^{1} \times S^{3}, J$. Reine Angew. Math. 469 (1995), 1-50.
\item[] [22] Gauduchon P., Tod K.P., Hyper-Hermitian metrics with symmetry, J. Geom. Phys. 25 (1998), 291-304.
\item[] [23] Gegenberg J.D., Das A., Stationary Riemannian space-times with self-dual curvature, Gen. Relativity Gravitation 16 (1984), 817-829.
\item[] [24] Gibbons G.W., Hawking S.W., Gravitational multi-instantons, Phys. Lett. B 78 (1978), 430-432.
\item[] [25] Glazebrook J.F., Kamber F.W., Pedersen H., Swann A., Foliation reduction and self-duality, in Geometric Study of Foliations (Tokyo, 1993), Editors T. Mizutani, K. Masuda, S. Matsumoto, T. Inaba, T. Tsuboi, Y. Mitsumatsu, World Sci. Publ., River Edge, NJ, 1994, 219-249.
\item[] [26] Grant J.D.E., Strachan I.A.B., Hypercomplex integrable systems, Nonlinearity 12 (1999), 1247-1261, solv-int/9808019.
\item[] [27] Gross M., Wilson P.M.H., Large complex structure limits of K3 surfaces, J. Differential Geom. 55 (2000), 475-546, math.DG/0008018.
\item[] [28] Hashimoto Y., Yasui Y., Miyagi S., Ootsuka T., Applications of the Ashtekar gravity to four-dimensional hyper-Kähler geometry and Yang-Mills instantons, J. Math. Phys. 38 (1997), 5833-5839, hep-th/9610069.
\item[] [29] Hitchin N.J., Complex manifolds and Einstein's equations, in Twistor Geometry and Nonlinear Systems (Primorsko, 1980), Lecture Notes in Math., Vol. 970, Editors H.D. Doebner, T.D. Palev, Springer, Berlin, 1982, 73-99.
\item[] [30] Hitchin N.J., The self-duality equations on a Riemann surface, Proc. London Math. Soc. 55 (1987), 59-126.
\item[] [31] Hitchin N.J., Twistor spaces, Einstein metrics and isomonodromic deformations, J. Differential Geom. 42 (1995), 30-112.
\item[] [32] Hitchin N.J., Geometrical aspects of Schlesinger's equation, J. Geom. Phys. 23 (1997), 287-300.
\item[] [33] Hitchin N.J., Hypercomplex manifolds and the space of framings, in The Geometric Universe (Oxford, 1996), Editors S.A. Huggett, L.J. Mason, K.P. Tod, S.T. Tsou, N.M.J. Woodhouse, Oxford University Press, Oxford, 1998, 9-30.
\item[] [34] Husain V., Self-dual gravity as a two-dimensional theory and conservation laws, Classical Quantum Gravity 11 (1994), 927-937, gr-qc/9310003.
\item[] [35] Jimbo M., Miwa T., Ueno K., Monodromy preserving deformation of linear ordinary differential equations with rational coefficients. I. General theory and $\tau$-function, Phys. D 2 (1981), 306-352.
\item[] [36] Jones P.E., Tod K.P., Minitwistor spaces and Einstein-Weyl spaces, Classical Quantum Gravity 2 (1985), 565-577.
\item[] [37] Joyce D.D., Explicit construction of self-dual 4-manifolds, Duke Math. J. 77 (1995), 519-552.
\item[] [38] LeBrun C., Spaces of complex geodesics and related structures, Ph.D. Thesis, University of Oxford, 1980.
\item[] [39] LeBrun C., Explicit self-dual metrics on $\mathbb{C P}_{2} \# \cdots \# \mathbb{C P}_{2}$, J. Differential Geom. 34 (1991), 223-253.
\item[] [40] Mason L.J., Newman E.T., A connection between the Einstein and Yang-Mills equations, Comm. Math. Phys. 121 (1989), 659-668.
\item[] [41] Mason L.J., Woodhouse N.M.J., Integrability, self-duality, and twistor theory, London Mathematical Society Monographs. New Series, Vol. 15, The Clarendon Press, Oxford University Press, New York, 1996.
\item[] [42] Maszczyk R., The classification of self-dual Bianchi metrics, Classical Quantum Gravity 13 (1996), 513-527.
\item[] [43] Maszczyk R., Mason L.J., Woodhouse N.M.J., Self-dual Bianchi metrics and the Painlevé transcendents, Classical Quantum Gravity 11 (1994), 65-71.
\item[] [44] Nahm W., The construction of all self-dual multimonopoles by the ADHM method, in Monopoles in Quantum Field Theory (Trieste, 1981), World Sci. Publishing, Singapore, 1982, 87-94.
\end{itemize}
\begin{itemize}
\item[] [45] Obata M., Affine connections on manifolds with almost complex, quaternion or Hermitian structure, Jpn. J. Math. 26 (1956), 43-77.
\item[] [46] Park Q.H., Self-dual gravity as a large- $N$ limit of the 2D nonlinear sigma model, Phys. Lett. B 238 (1990), 287-290.
\item[] [47] Pedersen H., Poon Y.S., Kähler surfaces with zero scalar curvature, Classical Quantum Gravity 7 (1990), 1707-1719.
\item[] [48] Pedersen H., Tod K.P., Three-dimensional Einstein-Weyl geometry, Adv. Math. 97 (1993), 74-109.
\item[] [49] Penrose R., Nonlinear gravitons and curved twistor theory, Gen. Relativity Gravitation 7 (1976), 31-52.
\item[] [50] Plebański J.F., Some solutions of complex Einstein equations, J. Math. Phys. 16 (1975), 2395-2402.
\item[] [51] Tafel J., Two-dimensional reductions of the self-dual Yang-Mills equations in self-dual spaces, J. Math. Phys. 34 (1993), 1892-1907.
\item[] [52] Tafel J., Wójcik D., Null Killing vectors and reductions of the self-duality equations, Nonlinearity 11 (1998), 835-844.
\item[] [53] Tod K.P., Self-dual Einstein metrics from the Painlevé VI equation, Phys. Lett. A 190 (1994), 221-224.
\item[] [54] Tod K.P., Cohomogeneity-one metrics with self-dual Weyl tensor, in Twistor Theory (Plymouth), Lecture Notes in Pure and Appl. Math., Vol. 169, Editor S.A. Huggett, Dekker, New York, 1995, 171-184.
\item[] [55] Tod K.P., Scalar-flat Kähler and hyper-Kähler metrics from Painlevé-III, Classical Quantum Gravity 12 (1995), 1535-1547.
\item[] [56] Tod K.P., 'Special' Einstein-Weyl spaces, Twistor Newsletter 42 (1997), 13-15.
\item[] [57] Todd J.A., Projective and analytical geometry, Pitman Publishing Corporation, New York, 1946.
\item[] [58] Ueno T., Integrable field theories derived from 4-D self-dual gravity, Modern Phys. Lett. A 11 (1996), 545-552, hep-th/9508012.
\item[] [59] Ward R.S., Integrable and solvable systems, and relations among them, Philos. Trans. Roy. Soc. London Ser. A 315 (1985), 451-457.
\item[] [60] Ward R.S., Einstein-Weyl spaces and $\mathrm{SU}(\infty)$ Toda fields, Classical Quantum Gravity 7 (1990), L95-L98.
\item[] [61] Ward R.S., Linearization of the $\mathrm{SU}(\infty)$ Nahm equations, Phys. Lett. B 234 (1990), 81-84.
\item[] [62] Ward R.S., The $\operatorname{SU}(\infty)$ chiral model and self-dual vacuum spaces, Classical Quantum Gravity 7 (1990), L217-L222.
\item[] [63] Weyl H., Space, time, matter, Dover, New York, 1952.
\item[] [64] Yoshida M., Hypergeometric functions, my love (modular interpretations of configuration spaces), Aspects of Mathematics, Vol. E32, Friedr. Vieweg \& Sohn, Braunschweig, 1997.
\end{itemize}

\section*{Additional references}
\begin{itemize}
\item[] [65] Calderbank D.M.J., Selfdual 4-manifolds, projective structures, and the Dunajski-West construction, SIGMA 10 (2014), 035, 18 pages, math.DG/0606754.
\item[] [66] Donaldson S., Fine J., Toric anti-self-dual 4-manifolds via complex geometry, Math. Ann. 336 (2006), 281-309, math.DG/0602423.
\item[] [67] Dunajski M., Harmonic functions, central quadrics and twistor theory, Classical Quantum Gravity 20 (2003), 3427-3440, math.DG/0303181.
\item[] [68] Dunajski M., Solitons, instantons, and twistors, Oxford Graduate Texts in Mathematics, Vol. 19, Oxford University Press, Oxford, 2010.
\item[] [69] Dunajski M., Grant J.D.E., Strachan I.A.B., Multidimensional integrable systems and deformations of Lie algebra homomorphisms, J. Math. Phys. 48 (2007), 093502, 11 pages, nlin.SI/0702040.
\item[] [70] Dunajski M., Krynski W., Einstein-Weyl geometry, dispersionless Hirota equation and Veronese webs, Math. Proc. Cambridge Philos. Soc., to appear, arXiv:1301.0621.
\item[] [71] Dunajski M., Sparling G., A dispersionless integrable system associated to $\operatorname{Diff}\left(S^{1}\right)$ gauge theory, Phys. Lett. A 343 (2005), 129-132, nlin.SI/0503030.
\item[] [72] Dunajski M., West S., Anti-self-dual conformal structures with null Killing vectors from projective structures, Comm. Math. Phys. 272 (2007), 85-118, math.DG/0601419.
\end{itemize}
\begin{itemize}
\item[] [73] Dunajski M., West S., Anti-self-dual conformal structures in neutral signature, in Recent Developments in Pseudo-Riemannian Geometry, Editors D.V. Alekseevsky, H. Baum, ESI Lect. Math. Phys., Eur. Math. Soc., Zürich, 2008, 113-148, math.DG/0610280.
\item[] [74] Ferapontov E.V., Huard B., Zhang A., On the central quadric ansatz: integrable models and Painlevé reductions, J. Phys. A: Math. Theor. 45 (2012), 195204, 11 pages, arXiv:1201.5061.
\item[] [75] Ferapontov E.V., Kruglikov B., Dispersionless integrable systems in 3D and Einstein-Weyl geometry, arXiv:1208.2728.
\item[] [76] Fine J., Toric anti-self-dual Einstein metrics via complex geometry, Math. Ann. 340 (2008), 143-157, math.DG/0609487.
\item[] [77] LeBrun C., Mason L.J., Zoll manifolds and complex surfaces, J. Differential Geom. 61 (2002), 453-535, math.DG/0211021.
\item[] [78] LeBrun C., Mason L.J., Nonlinear gravitons, null geodesics, and holomorphic disks, Duke Math. J. 136 (2007), 205-273, math.DG/0504582.
\item[] [79] LeBrun C., Mason L.J., The Einstein-Weyl equations, scattering maps, and holomorphic disks, Math. Res. Lett. 16 (2009), 291-301, arXiv:0806.3761.
\item[] [80] LeBrun C., Mason L.J., Zoll metrics, branched covers, and holomorphic disks, Comm. Anal. Geom. 18 (2010), 475-502, arXiv:1002.2993.
\item[] [81] Nakata F., Self-dual Zollfrei conformal structures with $\alpha$-surface foliation, J. Geom. Phys. 57 (2007), 2077-2097, math.DG/0701116.
\item[] [82] Nakata F., Singular self-dual Zollfrei metrics and twistor correspondence, J. Geom. Phys. 57 (2007), 1477-1498, math.DG/0607276.
\item[] [83] Nakata F., A construction of Einstein-Weyl spaces via LeBrun-Mason type twistor correspondence, Comm. Math. Phys. 289 (2009), 663-699, arXiv:0806.2696.
\end{itemize}