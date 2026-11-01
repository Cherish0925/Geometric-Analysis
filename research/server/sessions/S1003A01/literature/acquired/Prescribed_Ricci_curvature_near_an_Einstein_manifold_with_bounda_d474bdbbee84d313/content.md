---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: Prescribed_Ricci_curvature_near_an_Einstein_manifold_with_boundary_4a1bf1c0f5d4.pdf
converter: mathpix
format: mmd
---

\title{
PRESCRIBED RICCI CURVATURE NEAR AN EINSTEIN MANIFOLD WITH BOUNDARY
}

\author{
ERWANN DELAY
}

\begin{abstract}
Let $(M, g)$ be a compact Einstein Riemannian manifold with boundary. We show that under certain conditions, the map that associates to a metric on $M$ its Ricci curvature, its induced conformal class on the boundary, and its mean curvature on the boundary is locally invertible near $g$. The contravariant Ricci operator, as well as other operators such as the Einstein operator, are also studied.
\end{abstract}

Keywords: Ricci curvature, Einstein metrics, symmetric 2-tensors, quasi-linear elliptic PDE.

2010 MSC: 53C21, 53A45, 58J05, 58J37, 35J62.

\section*{Contents}
1. Introduction ..... 1
2. Definitions, Notations, and Conventions ..... 3
3. Fredholm Properties and Isomorphisms ..... 4
4. Case of Ricci Curvature ..... 5
5. Contravariant Ricci Operator ..... 8
6. Einstein-type Curvature ..... 9
7. Riemann-Christoffel Type Curvature ..... 13
References ..... 14

\section*{1. Introduction}

On a Riemannian manifold ( $M, g$ ), we denote by $\operatorname{Ric}(g)$ its Ricci curvature. We first consider the (field of) geometric symmetric 2-tensors of the form
$$\operatorname{Ric}_{\Lambda}(g):=\operatorname{Ric}(g)+\Lambda g,$$
where $\Lambda$ is a constant. This tensor is geometrically natural in the sense that for any sufficiently regular diffeomorphism $\varphi$,
$$\varphi^{*} \operatorname{Ric}_{\Lambda}(g)=\operatorname{Ric}_{\Lambda}\left(\varphi^{*} g\right) .$$

\footnotetext{
Date: March 24, 2025.
}

Here, we address the problem of inverting the operator $\mathrm{Ric}_{\Lambda}$. Given a symmetric tensor field $R_{\Lambda}$ on $M$, we seek a Riemannian metric $g$ such that
$$\operatorname{Ric}_{\Lambda}(g)=R_{\Lambda} .$$
This requires solving a particularly complex quasi-linear system.
The prescribed Ricci curvature problem dates back to the 1980s. DeTurck [13], in 1981, first proved a local existence result near a point $p$ in $\mathbb{R}^{n}$ under the intrinsic assumption that the matrix of $R(p)$ is invertible (see also [15]).

Subsequently, global results were obtained: Hamilton [19], in 1984, treated the case of the unit sphere in $\mathbb{R}^{n+1}$ (with $n>2$ ), proving a local inversion result near the standard metric.

Such local inversion techniques were later adapted to certain Einstein manifolds [7], [12], [14], [8], [6], [9], and then to parallel Ricci manifolds [10], [11]. The problem of prescribed Ricci curvature has also been studied on Lie groups and homogeneous spaces with completely different methods (see [17] and references therein).

Obstruction results to the inversion of Ricci curvature also exist [16], [3], [19], [5], [7].

So far, the only results concerning manifolds with boundary is local near a boundary point [23] or for special domains of some cohomogeneity one manifolds [24]. Recent works on Einstein metrics on manifolds with boundary, such as [1], have inspired us to obtain global results on $M$ near an Einstein metric.

To illustrate our results simply, we state a particular case. The induced boundary metric is denoted by $g^{T}$, and the mean curvature of the boundary by $H(g)$.
Theorem 1.1. Let $(M, g)$ be a smooth compact Einstein Riemannian manifold with boundary, with $\operatorname{Ric}(g)=\lambda g$. Suppose that $\lambda+\Lambda \neq 0$ and that $-2 \Lambda$ is not in the spectrum of the Hodge Laplacian acting on 1forms with Dirichlet condition, nor in the spectrum of the Lichnerowicz Laplacian with ADN conditions. Let $k \in \mathbb{N} \backslash\{0\}$ and $\alpha \in(0,1)$, then for every $r \in C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ close to zero, every conformal class $[\gamma]$ close to $\left[g^{T}\right]$ in $\left[C^{k+2, \alpha}\left(\partial M, S_{2}^{+}\right)\right]$, and every function $\mathcal{H}$ close to $H(g)$ in $C^{k+1, \alpha}(\partial M)$, there exists a unique $h$ close to zero in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ such that
$$\begin{cases}\operatorname{Ric}_{\Lambda}(g+h)=\operatorname{Ric}_{\Lambda}(g)+r & \text { in } M, \\ {\left[(g+h)^{T}\right]=[\gamma]} & \text { on } \partial M, \\ H(g+h)=\mathcal{H} & \text { on } \partial M .\end{cases}$$
Moreover, the map $(r,[\gamma], \mathcal{H}) \mapsto h$ is smooth from a neighborhood of $\left(0,\left[g^{T}\right], H(g)\right)$ to a neighborhood of zero in the corresponding Banach spaces.

The ADN condition, introduced by M. Anderson [2], is a mixed Dirichlet-Neumann condition specified in Definition 3.4.

Our solution's regularity is optimal, as can be seen by applying a low-regularity diffeomorphism to the equation (1.1).

We also establish an analogous result for the contravariant Ricci operator, which is better suited to negative curvature cases.

Furthermore, we extend this approach to other operators, such as the Einstein tensor.

Finally, we show that the image of certain Riemann-Christoffel-type operators forms smooth submanifolds in $C^{\infty}$.

Acknowledgments: I thank Lan-Hsuan Huang for insightful discussions concerning [1] and [2]. This article was partially funded by the French National Research Agency (ANR) grants ANR-23-CE40-0010-02 and ANR-24-CE40-0702.

\section*{2. Definitions, Notations, and Conventions}

We denote by ∇ the Levi-Civita connection of $g$, by $\operatorname{Ric}(g)$ its Ricci curvature, and by $\operatorname{Riem}(g)$ its sectional Riemannian curvature.

Let $\mathcal{T}_{p}^{q}$ be the set of covariant tensors of rank $p$ and contravariant tensors of rank $q$. When $p=2$ and $q=0$, we denote by $\mathcal{S}_{2}$ the subset of symmetric tensors, which decomposes as $\mathcal{G} \oplus \stackrel{\circ}{\mathcal{S}}_{2}$, where $\mathcal{G}$ is the set of $g$-conformal tensors and $\stackrel{\circ}{\mathcal{S}}_{2}$ is the set of traceless tensors (relative to $g$ ). The set $\mathcal{S}_{2}^{+}$denotes the subset of $\mathcal{S}_{2}$ consisting of positive definite tensors.

For $k \in \mathbb{N}, \alpha \in(0,1)$ and a tensor bundle $E, C^{k, \alpha}(M, E)$ is the usual Hölder space of tensor fields with $C^{k, \alpha}$ regularity. The space of conformal class of metric of $C^{k, \alpha}$ regularity on the boundary is denoted by
$$\begin{aligned}
{\left[C^{k, \alpha}\left(\partial M, \mathcal{S}_{2}^{+}\right)\right] } & =\left\{[\gamma], \gamma \in C^{k, \alpha}\left(\partial M, \mathcal{S}_{2}^{+}\right)\right\} \\
& \cong\left\{\gamma \in C^{k, \alpha}\left(\partial M, \mathcal{S}_{2}^{+}\right),|\gamma|=1\right\},
\end{aligned}$$
where |.| is the determinant (with respect to a fixed background metric, say $g^{T}$ ), and where for $\gamma \in C^{k, \alpha}\left(\partial M, \mathcal{S}_{2}^{+}\right)$, we identify its conformal class $[\gamma]$ with its unique representative of determinant 1 .

We use Einstein's summation convention (indices range from 1 to $n$ ), and we use $g_{i j}$ and its inverse $g^{i j}$ to raise or lower indices.

The Laplacian is defined by
$$\triangle=-t r \nabla^{2}=\nabla^{*} \nabla,$$
where $\nabla^{*}$ is the formal $L^{2}$ adjoint of ∇ . The Lichnerowicz Laplacian acting on symmetric 2-covariant tensor fields is [20]
$$\Delta_{L}=\Delta+2(\text { Ric }- \text { Riem }),$$
where
$$(\operatorname{Ric} u)_{i j}=\frac{1}{2}\left[\operatorname{Ric}(g)_{i k} u_{j}^{k}+\operatorname{Ric}(g)_{j k} u_{i}^{k}\right],$$
and
$$(\operatorname{Riem} u)_{i j}=\operatorname{Riem}(g)_{i k j l} u^{k l} .$$

For $u$ a symmetric 2-covariant tensor, its divergence is defined by
$$(\operatorname{div} u)_{i}=-\nabla^{j} u_{j i} .$$
For a 1-form $\omega$ on $M$, its divergence is defined by:
$$d^{*} \omega=-\nabla^{i} \omega_{i},$$
and the symmetric part of its covariant derivatives:
$$(\mathcal{L} \omega)_{i j}=\frac{1}{2}\left(\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}\right),$$
(note that $\mathcal{L}^{*}=\operatorname{div}$ ). The Hodge-de Rham Laplacian acting on 1-forms is denoted by
$$\Delta_{H}=d d^{*}+d^{*} d=\Delta+\text { Ric } .$$

The Bianchi operator for symmetric 2-tensors into 1-forms is defined as:
$$B_{g}(h)=\operatorname{div}_{g} h+\frac{1}{2} d\left(\operatorname{Tr}_{g} h\right) .$$

\section*{3. Fredholm Properties and Isomorphisms}

We recall here the Fredholm properties of Laplacian-type operators plus zero-order terms acting on 1-forms or on symmetric two-tensors. We begin by stating a well-known fact (see eg. [22]).

Proposition 3.1. Let $k \in \mathbb{N}, \alpha \in(0,1)$, and $c$ be a real number. The operator from $C^{k+2, \alpha}\left(M, \mathcal{T}_{1}\right)$ to $C^{k, \alpha}\left(M, \mathcal{T}_{1}\right) \times C^{k+2, \alpha}\left(M, \mathcal{T}_{1}\right)_{\mid \partial M}$, given by
$$\begin{cases}\left(\Delta_{H}+c\right) \omega & \text { in } M \\ \omega & \text { on } \partial M\end{cases}$$
is Fredholm of index 0.
Let $C_{0}^{k, \alpha}\left(M, \mathcal{T}_{1}\right)$ denote the space of $C^{k, \alpha}\left(M, \mathcal{T}_{1}\right)$ 1-forms satisfying the Dirichlet condition (i.e., vanishing on the boundary of $M$ ).

Corollary 3.2. Let $k \in \mathbb{N}, \alpha \in(0,1)$, and $c$ be a real number. If $-c$ is not in the spectrum of the Hodge Laplacian $\Delta_{H}$ with Dirichlet boundary condition, then
$$\Delta_{H}+c: C_{0}^{k+2, \alpha}\left(M, \mathcal{T}_{1}\right) \longrightarrow C^{k, \alpha}\left(M, \mathcal{T}_{1}\right),$$
is an isomorphism.
We recall that the kernel of $\Delta_{H}+c$ with Dirichlet boundary condition is generically trivial for boundary deformations towards the interior (see, for example, [1], Lemma 1.2).

The following proposition involves the linearization $D H(g)$ of the mean curvature operator $H$ at $g$. Even though we will not need the explicit formula, we recall one (see [21], for example, with a different
sign convention). Let $\nu$ be the outward-pointing normal to the boundary and $\mathbb{I}_{A B}=-\left\langle\nabla_{\partial_{A}} \nu, \partial_{B}\right\rangle$ be the second fundamental form of the boundary, so that $H=\operatorname{Tr}_{g^{T}} \mathbb{I}$. Then we have
$$D H(g) h=\operatorname{div}_{g^{T}}\left(h(\nu, .)^{T}\right)+\frac{1}{2} \operatorname{Tr}_{g^{T}}\left(\left(\nabla_{\nu} h\right)^{T}\right)-\frac{1}{2} h(\nu, \nu) H .$$

We can now state the following
Proposition 3.3. Let $k \in \mathbb{N}, \alpha \in(0,1)$, and $c$ be a real number. The operator
$$L_{c}: C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right) \longrightarrow C^{k, \alpha}\left(M, \mathcal{S}_{2}\right) \times C^{k+1, \alpha}\left(\partial M, \mathcal{S}_{2}\right) \times C^{k+2, \alpha}\left(\partial M, \stackrel{\circ}{\mathcal{S}}_{2}\right) \times C^{k+1, \alpha}(\partial M),$$
given by
$$L_{c}(h)= \begin{cases}\left(\Delta_{L}+c\right) h & \text { in } M \\ B_{g}(h) & \text { on } \partial M \\ h^{T}-\frac{1}{n-1} \operatorname{Tr}_{g^{T}}\left(h^{T}\right) g^{T} & \text { on } \partial M \\ D H(g) h & \text { on } \partial M\end{cases}$$
is Fredholm of index 0.
Proof. In [2], M. Anderson proves that $L_{c}$ is elliptic and Fredholm of index zero when $c=-2 \lambda$; the case of arbitrary $c$ follows immediately by homotopy. \(\square\)

This proposition motivates the definition of a mixed condition between Dirichlet and Neumann, introduced by M. Anderson.

Definition 3.4 (ADN condition). We say that $h \in C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ satisfies the ADN condition if
$$\begin{cases}B_{g}(h)=0 & \text { on } \partial M \\ h^{T}-\frac{1}{n-1} \operatorname{Tr}_{g^{T}}\left(h^{T}\right) g^{T}=0 & \text { on } \partial M \\ D H(g) h=0 & \text { on } \partial M\end{cases}$$

We thus immediately obtain
Corollary 3.5. If -c is not in the spectrum of the Lichnerowicz Laplacian with ADN condition, then $L_{c}$ is an isomorphism.

Remark 3.6. The tensor $g$ is in the kernel of $L_{0}$ if and only if $\partial M$ is a minimal hypersurface of $M$. Indeed, the first three components of $L_{0}(h)$ vanish if $h=g$. For the fourth, note that if $g_{t}=(1+t)^{2} g$, then $H\left(g_{t}\right)=(1+t)^{-1} H(g)$, so by linearizing at $t=0$, we obtain
$$2 D H(g) g=-H(g) .$$

\section*{4. Case of Ricci Curvature}

In this section, we prove Theorem 1.1. It is now well known that the Ricci equation is not elliptic due to the invariance of curvature under diffeomorphism. We will modify this equation by drawing inspiration from DeTurck's method. We thus add a gauge term so that this new
equation becomes elliptic while ensuring that its solutions remain solutions of the Ricci equation. In order to construct our new equation, let us recall some differentials of operators.

We already have (see [4], for example)
$$D \operatorname{Ric}(g) h=\frac{1}{2} \Delta_{L} h-\mathcal{L}_{g} B_{g}(h) .$$
The linearization in the first variable of the Bianchi operator is (see, for example, [8])
$$\left[D B_{(.)}(R)\right](g) h=-R B_{g}(h)+T(g, R) h,$$
where $R$ is here identified with the corresponding endomorphism of $T^{*} M$ and
$$[T(g, R) h]_{j}=T(g, R)_{j}^{k l} h_{k l}=\frac{1}{2}\left(\nabla^{k} R_{j}^{l}+\nabla^{l} R_{j}^{k}-\nabla_{j} R^{k l}\right) h_{k l} .$$
We define
$$\operatorname{Ric}_{\Lambda}(g):=\operatorname{Ric}(g)+\Lambda g$$
In particular, if $g$ is Einstein with $\operatorname{Ric}(g)=\lambda g$, we have
$$\left[D B_{(.)}\left(\operatorname{Ric}_{\Lambda}(g)\right)\right](g) h=-(\lambda+\Lambda) B_{g}(h) .$$

Finally, recall that for any metric $g, B_{g}\left(\operatorname{Ric}_{\Lambda}(g)\right)=0$ by the Bianchi identity.

The equation we choose to solve will be
$$F(r, h)=(0,0, \gamma, \mathcal{H}),$$
with
$$F(h, r):= \begin{cases}\operatorname{Ric}_{\Lambda}(g+h)-R_{\Lambda}-\mathcal{L}_{g}\left((\lambda+\Lambda)^{-1} B_{g+h}\left(R_{\Lambda}\right)\right) & \text { in } M, \\ -(\lambda+\Lambda)^{-1} B_{g+h}\left(R_{\Lambda}\right) & \text { on } \partial M, \\ \left|(g+h)^{T}\right|^{-\frac{1}{n-1}}(g+h)^{T} & \text { on } \partial M, \\ H(g+h) & \text { on } \partial M,\end{cases}$$
where
$$R_{\Lambda}=\operatorname{Ric}(g)+\Lambda g+r=(\lambda+\Lambda) g+r,$$
and $\left|(g+h)^{T}\right|$ denotes the determinant of $(g+h)^{T}$.
Let us first verify that the solutions of the new equation are solutions of the equation we are interested in.

Proposition 4.1. Under the conditions of Theorem 1.1, if $h \in C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ is small enough, and if the metric $g+h$ is a solution of (4.1), then it is a solution of
$$\begin{cases}\operatorname{Ric}_{\Lambda}(g+h)=R_{\Lambda} & \text { in } M, \\ \left|(g+h)^{T}\right|^{\frac{-1}{n-1}}(g+h)^{T}=\gamma & \text { on } \partial M, \\ H(g+h)=\mathcal{H} & \text { on } \partial M,\end{cases}$$

Proof. Applying $B_{g+h}$ to the first component of (4.1), we note that $B_{g+h}\left[\operatorname{Ric}_{\Lambda}(g+h)\right]=0$ by the Bianchi identity. Thus, defining
$$\omega:=(\lambda+\Lambda)^{-1} B_{g+h}\left(R_{\Lambda}\right),$$
we see that $\omega$ vanishes at the boundary and
$$P_{g+h} \omega:=B_{g+h}\left[\mathcal{L}_{g}(\omega)\right]+(\lambda+\Lambda) \omega=0 .$$

The operator $P_{g}$ can be expressed in local coordinates as:
$$\left(P_{g} \omega\right)_{j}=-\nabla^{i}\left[\frac{1}{2}\left(\nabla_{i} \omega_{j}+\nabla_{j} \omega_{i}\right)\right]+\frac{1}{2} \nabla_{j} \nabla^{i} \omega_{i}+\operatorname{Ric}(g)_{j}^{k} \omega_{k}+\Lambda \omega_{j} .$$
Commuting the derivatives and multiplying by 2, we obtain
$$2 P_{g}=\Delta_{g} \omega+\operatorname{Ric}_{g} \omega+2 \Lambda \omega=\left(\Delta_{H}+2 \Lambda\right) \omega .$$
Since the operator $P_{g}$ with Dirichlet condition has a trivial kernel, by corollary 3.2, it is an isomorphism from $C_{0}^{k+1, \alpha}\left(M, \mathcal{T}_{1}\right)$ to $C^{k-1, \alpha}\left(M, \mathcal{T}_{1}\right)$, then for small $h$ in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right), P_{g+h}$ with Dirichlet condition remains injective, we conclude that $\omega=0$. \(\square\)

Remark 4.2. The fact that $B_{g+h}\left(R_{\Lambda}\right)$ vanishes proves that the identity map from $(M, g+h)$ to $\left(M, R_{\Lambda}\right)$ is harmonic (see [18], for example).

We will now construct the solutions of (4.1) using an implicit function argument in Banach spaces.

Proposition 4.3. Under the conditions of Theorem 1.1, for any small $r \in C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$, for any conformal class $[\gamma]$ close to $\left[g^{T}\right]$ in $\left[C^{k+2, \alpha}\left(\partial M, \mathcal{S}_{2}^{+}\right)\right]$, and for any function $\mathcal{H}$ close to $H(g)$ in $C^{k+1, \alpha}(\partial M)$, there exists a unique $h$ close to zero in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ that solves (4.1).

Proof. We consider $F$ as a mapping defined in a neighborhood of zero in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right) \times C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ with values in $C^{k, \alpha}\left(M, \mathcal{S}_{2}\right) \times C^{k+1, \alpha}\left(\partial M, \mathcal{S}_{2}\right) \times$ $\left[C^{k+2, \alpha}\left(\partial M, \mathcal{S}_{2}^{+}\right)\right] \times C^{k+1, \alpha}(\partial M)$. We already have
$$F(0,0)=\left(0,0,\left[g^{T}\right], H(g)\right) .$$
Considering the differentials of the operators given at the beginning of the section, the differential of $F$ with respect to $h$ at 0 is
$$D_{h} F(0,0)=\frac{1}{2} L_{2 \Lambda},$$
where $L_{2 \Lambda}$ is described in Proposition 3.3. By Corollary 3.5, this operator is an isomorphism from $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ to $C^{k, \alpha}\left(M, \mathcal{S}_{2}\right) \times C^{k+1, \alpha}\left(\partial M, \mathcal{S}_{2}\right) \times$ $C^{k+2, \alpha}\left(\partial M, \stackrel{\circ}{\mathcal{S}}_{2}\right) \times C^{k+1, \alpha}(\partial M)$. The implicit function theorem allows us to conclude. \(\square\)

Remark 4.4. If $L_{2 \Lambda}$ has a kernel, we can still solve equation (1.1) but modulo a projection. In this case, we take
$$R_{\Lambda}=\operatorname{Ric}_{\Lambda}(g)+r-\frac{1}{2} \Pi(h)=(\lambda+\Lambda) g+r-\frac{1}{2} \Pi(h),$$
where $\Pi$ is the $L^{2}$-orthogonal projection onto the kernel; see [10]. According to Remark 3.6, if $\Lambda=0$, the hypotheses of Theorem 1.1 imply that the boundary of $M$ must not be a minimal hypersurface. For the case $\Lambda=0$ with minimal boundary, if the kernel is one-dimensional, so generated by $g$, we can also solve (1.1) up to a multiplicative constant, as in [19]. Here, we can take (see [6] and [10], Remark 4.4)
$$R_{0}=e^{-\frac{1}{2 n \lambda}\left\langle\operatorname{Tr}_{g} h\right\rangle}(\operatorname{Ric}(g)+r)=e^{-\frac{1}{2 n \lambda}\left\langle\operatorname{Tr}_{g} h\right\rangle}(\lambda g+r)$$
where
$$\left\langle\operatorname{Tr}_{g} h\right\rangle=\frac{1}{\operatorname{Vol}_{g}(M)} \int_{M} \operatorname{Tr}_{g} h d \mu_{g}$$

\section*{5. Contravariant Ricci Operator}

We are interested here in the inversion of the (shifted) contravariant Ricci operator:
$$g \mapsto \overline{\operatorname{Ric}}_{\Lambda}(g):=\overline{\operatorname{Ric}}(g)+\Lambda g^{-1}$$
whose components in local coordinates are
$$\overline{\operatorname{Ric}}_{\Lambda}(g)^{i j}=g^{i k} g^{j l} \operatorname{Ric}(g)_{k l}+\Lambda g^{i j}=g^{i k} g^{j l} \operatorname{Ric}_{\Lambda}(g)_{k l} .$$
We will use the obvious notation
$$\overline{\operatorname{Ric}}_{\Lambda}(g)=g^{-1} \operatorname{Ric}_{\Lambda}(g) g^{-1} .$$
We adapt the steps of Section 4. First, we have
$$D \overline{\operatorname{Ric}}_{\Lambda}(g) h=g^{-1}\left[\frac{1}{2} \Delta_{L} h-\mathcal{L}_{g} B_{g}(h)-2 \operatorname{Ric} h-\Lambda h\right] g^{-1} .$$
Let us set $\bar{B}_{g}(\bar{R})=B_{g}(g \bar{R} g)$, so that if $\nabla \bar{R}=0$, we obtain
$$D \bar{B}_{(.)}(\bar{R}) h=-g \bar{R} B_{g}(h)+B_{g}(h \bar{R} g+g \bar{R} h) .$$
If moreover $\bar{R}=(\lambda+\Lambda) g^{-1}$, we find
$$D \bar{B}_{(.)}(\bar{R}) h=(\lambda+\Lambda) B_{g}(h)=g \bar{R} B_{g}(h) .$$
The gauge equation we choose to solve here will be
$$F(h, \bar{r})=(0,0, \gamma, \mathcal{H})$$
with
$$\bar{F}(h, \bar{r}):= \begin{cases}\bar{F}_{1}(h, r) & \text { in } M, \\ (\lambda+\Lambda)^{-1} \bar{B}_{g+h}\left(\bar{R}_{\Lambda}\right) & \text { on } \partial M, \\ \left|(g+h)^{T}\right|^{-\frac{1}{n-1}}(g+h)^{T} & \text { on } \partial M, \\ H(g+h) & \text { on } \partial M,\end{cases}$$
where
$$\bar{F}_{1}(h, \bar{r}):=g\left[\overline{\operatorname{Ric}}_{\Lambda}(g+h)-\bar{R}_{\Lambda}\right] g+\mathcal{L}_{g}\left\{(\lambda+\Lambda)^{-1} \bar{B}_{g+h}\left[\bar{R}_{\Lambda}\right]\right\},$$
and
$$\bar{R}_{\Lambda}=\overline{\operatorname{Ric}_{\Lambda}}(g)+\bar{r}=(\lambda+\Lambda) g^{-1}+\bar{r} .$$

Theorem 5.1. Let $k \in \mathbb{N} \backslash\{0\}$ and $\alpha \in(0,1)$. Let $g$ be an Einstein metric with $\operatorname{Ric}(g)=\lambda g$ and let $\Lambda \in \mathbb{R}$ such that $\lambda+\Lambda \neq 0$. Assume that $4 \lambda+2 \Lambda$ is not in the spectrum of the Lichnerowicz Laplacian with ADN condition, nor in the spectrum of the Hodge Laplacian with Dirichlet condition. Then for all $\bar{r} \in C^{k+2, \alpha}\left(M, \mathcal{S}^{2}\right)$ close to zero, for every conformal class $[\gamma]$ close to $\left[g^{T}\right]$ in $\left[C^{k+2, \alpha}\left(\partial M, S_{2}^{+}\right)\right]$, and every function $\mathcal{H}$ close to $H(g)$ in $C^{k+1, \alpha}\left(\partial M, \mathcal{S}_{2}\right)$, there exists a unique $h$ close to zero in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ such that
$$\begin{cases}\overline{\operatorname{Ric}}_{\Lambda}(g+h)=\overline{\operatorname{Ric}}_{\Lambda}(g)+\bar{r} & \text { on } M \\ {\left[(g+h)^{T}\right]=[\gamma]} & \text { on } \partial M \\ H(g+h)=\mathcal{H} & \text { on } \partial M\end{cases}$$
Moreover, the map $(\bar{r},[\gamma], \mathcal{H}) \mapsto h$ is smooth from a neighborhood of $\left(0,\left[g^{T}\right], H(g)\right)$ into a neighborhood of zero between the corresponding Banach spaces.

Proof. We still have $\bar{F}_{1}(0,0)=0$ and since $g$ is Einstein,
$$D_{h} \bar{F}_{1}(0,0)=\frac{1}{2} \Delta_{L}-2 \lambda-\Lambda .$$
The corollary (3.5) proves that the operator $D_{h} \bar{F}(0,0)$ is an isomorphism from $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ to $C^{k, \alpha}\left(M, \mathcal{S}_{2}\right)$. By the implicit function theorem, for all $(\bar{r},[\gamma], \mathcal{H})$ close to $\left(0,\left[g^{T}\right], H(g)\right)$ in their respective spaces, there exists $h$ close to zero in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ such that
$$\bar{F}(h, \bar{r})=(0,0, \gamma, \mathcal{H}) .$$
We then apply $\bar{B}_{g+h}$ to the equation $\bar{F}_{1}(h, \bar{r})=0$, obtaining
$$\bar{P}_{g+h} \omega:=B_{g+h} \mathcal{L}_{g} \omega-(\lambda+\Lambda) \omega=0$$
where
$$\omega=(\lambda+\Lambda)^{-1} \bar{B}_{g+h}\left(\bar{R}_{\Lambda}\right)$$
is zero at the boundary. By hypothesis, the operator
$$\bar{P}_{g}=\frac{1}{2}\left(\Delta-\operatorname{Ric}_{g}\right)-(\lambda+\Lambda)=\frac{1}{2}\left(\Delta_{H}-4 \lambda-2 \Lambda\right),$$
with Dirichlet boundary condition is injective (and is an isomorphism from $C_{0}^{k+1, \alpha}\left(M, \mathcal{T}_{1}\right)$ to $C^{k-1, \alpha}\left(M, \mathcal{T}_{1}\right)$ by corollary 3.2), so if $h$ is small enough, $\bar{P}_{g+h}$ remains so, thus $\omega=0$. \(\square\)

\section*{6. Einstein-type Curvature}

We show here that the method of Section 4 can also be adapted to other operators of Einstein type. For $\kappa$ and $\Lambda$ two real constants, we define the tensor
$$\operatorname{Ein}(g):=\operatorname{Ric}(g)+\kappa R(g) g+\Lambda g .$$

Thus, for example, when $\kappa=-\frac{1}{2}$, we recover the Einstein tensor (with cosmological constant $\Lambda$ ), and if $\kappa=-\frac{1}{2(n-1)}$ and $\Lambda=0$, the Schouten tensor.

We study the inversion of the operator Ein. Given a symmetric 2-tensor $E$, we seek $g$ such that
$$\operatorname{Ein}(g)=E .$$
Since we have
$$\operatorname{Tr}_{g} \operatorname{Ein}(g)=(1+n \kappa) R(g)+n \Lambda,$$
the equation (6.1) is equivalent to
$$\operatorname{Ric}(g)=E-\frac{\kappa \operatorname{Tr}_{g} E+\Lambda}{1+n \kappa} g .$$
For any $E$, we define
$$\mathcal{B}_{g}(E)=\operatorname{div}_{g} E+\frac{2 \kappa+1}{2(1+\kappa n)} d \operatorname{Tr}_{g} E=B_{g}(E)-\frac{(n-2) \kappa}{2(1+\kappa n)} d \operatorname{Tr}_{g} E,$$
such that the Bianchi identity translates here as
$$\mathcal{B}_{g}(\operatorname{Ein}(g))=0 .$$
Knowing already the differential of $B_{g}(E)$ relative to the metric (see [8], for example), we find that the differential of this operator relative to the metric is
$$D\left[\mathcal{B}_{(.)}(E)\right](g) h=-E B_{g}(h)+\frac{(n-2) \kappa}{2(1+\kappa n)} d\langle E, h\rangle+T(E, h),$$
where $E$ is here identified with the endomorphism of $T^{*} M$ corresponding to it, and
$$T(E, h)_{j}=\frac{1}{2}\left(\nabla_{k} E_{j l}+\nabla_{l} E_{k j}-\nabla_{j} E_{k l}\right) h^{k l} .$$
In particular, if $g$ is Einstein, with $\operatorname{Ric}(g)=\lambda g$, then $\operatorname{Ein}(g)=\tau g$ with $\tau=(1+n \kappa) \lambda+\Lambda$, and
$$D\left[\mathcal{B}_{(.)}(E)\right](g) h=-\tau B_{g}(h)+\frac{(n-2) \kappa}{2(1+\kappa n)} \tau d \operatorname{Tr}_{g} h .$$
By analogy with Section 4, we define
$$\mathcal{F}_{1}(h, e):=\operatorname{Ric}(g+h)-E+\frac{\kappa \operatorname{Tr}_{g+h} E+\Lambda}{1+\kappa n}(g+h)-\mathcal{L}_{g}\left(\tau^{-1} \mathcal{B}_{g+h}(E)\right),$$
and
$$\mathcal{F}(h, r):= \begin{cases}\mathcal{F}_{1}(h, e) & \text { in } M, \\ -\tau^{-1} \mathcal{B}_{g+h}(E) & \text { on } \partial M, \\ \left|(g+h)^{T}\right|^{-1}(g+h)^{T} & \text { on } \partial M, \\ H(g+h) & \text { on } \partial M,\end{cases}$$
where
$$E=\operatorname{Ein}(g)+e=\tau g+e .$$

We already have
$$\mathcal{F}_{1}(0,0)=0 .$$
Here, we obtain
$$\begin{gathered}
D_{h} \mathcal{F}_{1}(0,0) h= \\
\frac{1}{2} \Delta_{L} h+\frac{1}{1+\kappa n}\left(\kappa \operatorname{Tr}_{g} \operatorname{Ein}(g) h+\Lambda h-\kappa\langle\operatorname{Ein}(g), h\rangle g\right) \\
-\frac{(n-2) \kappa}{2(1+\kappa n)} \mathcal{L}_{g} \tau^{-1} d\langle\operatorname{Ein}(g), h\rangle
\end{gathered}$$
thus,
$$\begin{gathered}
D_{h} \mathcal{F}_{1}(0,0) h= \\
\frac{1}{2} \Delta_{L} h+\frac{1}{1+\kappa n}\left(n \kappa \tau h+\Lambda h-\kappa \tau \operatorname{Tr}_{g} h g\right)-\frac{(n-2) \kappa}{2(1+\kappa n)} \nabla \nabla \operatorname{Tr}_{g} h .
\end{gathered}$$
This differential motivates us to define the operator
$$\begin{aligned}
\mathcal{P} h & :=\Delta_{L} h+\frac{2(n \kappa \tau+\Lambda)}{1+k n} h+\frac{\kappa}{n(1+\kappa n)}\left((n-2) \Delta \operatorname{Tr}_{g} h-2 n \tau \operatorname{Tr}_{g} h\right) g \\
& =\left(\Delta_{L}+2 \kappa n \lambda+2 \Lambda\right) h+\frac{\kappa}{n(1+\kappa n)}\left((n-2) \Delta \operatorname{Tr}_{g} h-2 n \tau \operatorname{Tr}_{g} h\right) g .
\end{aligned}$$
This respects the splitting $\mathcal{S}_{2}=\mathcal{G} \oplus \stackrel{\circ}{\mathcal{S}}_{2}$. In particular, if $u$ is a function on $M$ and $\stackrel{\circ}{h}$ is a symmetric traceless 2-tensor field, we have
$$\mathcal{P}(u g+\stackrel{\circ}{h})=\frac{1}{1+\kappa n} p(u) g+\stackrel{\circ}{P}(\stackrel{\circ}{h})$$
where
$$p(u)=(1+2(n-1) \kappa) \Delta u+2 \Lambda u,$$
and
$$\stackrel{\circ}{P}(\stackrel{\circ}{h})=\left[\Delta_{L}+2 \kappa n \lambda+2 \Lambda\right] \stackrel{\circ}{h} .$$

If $h=u g$, we find
$$D_{h} \mathcal{F}_{1}(0,0)(u g)=\frac{1}{2} p(u) g-\frac{(n-2) n \kappa}{2(1+\kappa n)} \operatorname{Hess} u,$$
where Hess $u$ is the traceless part of the Hessian of $u$. If $h=\stackrel{\circ}{h}$ is traceless, we find
$$D_{h} \mathcal{F}_{1}(0,0)(\AA)=\frac{1}{2} \stackrel{\circ}{P}(\AA) .$$

Proposition 6.1. We assume $\kappa \neq-\frac{1}{n},-\frac{1}{2(n-1)}$. Let
$$v=-2 \kappa\left(\frac{2(n-1) \Lambda}{1+2(n-1) \kappa}+n \lambda\right) .$$
If $-2 \kappa n \lambda-2 \Lambda$ is not in the spectrum of $\Delta_{L}+v \operatorname{Tr}()$.$g with A D N_{\kappa}$ conditions:
$$\left\{\begin{array}{ll}
B_{g}(h)-\frac{(n-2) \kappa}{2(1+\kappa n)} d \operatorname{Tr}_{g} h=0 & \text { on } \partial M \\
h^{T}-\frac{1}{n-1} \operatorname{Tr}_{g} T\left(h^{T}\right) g^{T}=0 & \text { on } \partial M \\
D H(g) h=0 & \text { on } \partial M
\end{array},\right.$$
then $D_{h} \mathcal{F}(0,0)$ is an isomorphism from $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ into $C^{k, \alpha}\left(M, \mathcal{S}_{2}\right) \times$ $C^{k+1, \alpha}\left(\partial M, \mathcal{S}_{2}\right) \times C^{k+2, \alpha}\left(\partial M, \dot{\mathcal{S}}_{2}\right) \times C^{k+1, \alpha}(\partial M)$.

Proof. It suffices to show that the map from $C^{k+2, \alpha}(M) \times C^{k+2, \alpha}\left(M, \stackrel{\circ}{\mathcal{S}}_{2}\right)$ into $C^{k, \alpha}(M) \times C^{k, \alpha}\left(M, \stackrel{\circ}{\mathcal{S}}_{2}\right) \times C^{k+1, \alpha}\left(\partial M, \mathcal{S}_{2}\right) \times C^{k+2, \alpha}\left(\partial M, \stackrel{\circ}{\mathcal{S}}_{2}\right) \times C^{k+1, \alpha}(\partial M)$ given by
$$(u, \stackrel{\circ}{h}) \longrightarrow\left\{\begin{array}{ll}
(p(u), \stackrel{\circ}{P}(\stackrel{\circ}{h})) & \text { in } M \\
B_{g}(h)-\frac{(n-2) \kappa}{2(1+\kappa n)} d \operatorname{Tr}_{g} h & \text { on } \partial M \\
h^{T}-\frac{1}{n-1} \operatorname{Tr}_{g^{T}}\left(h^{T}\right) g^{T} & \text { on } \partial M \\
D H(g) h & \text { on } \partial M
\end{array},\right.$$
where $h=u g+\stackrel{\circ}{h}$, is an isomorphism.
In order to do so, we will show that the map
$$(u, \stackrel{\circ}{h}) \longrightarrow\left\{\begin{array}{ll}
\left(\frac{1}{1+2(n-1) \kappa} p(u), \stackrel{\circ}{P}(\stackrel{\circ}{h})\right) & \text { in } M \\
B_{g}(h)-\frac{(n-2) \kappa}{2(1+\kappa n)} d \operatorname{Tr}_{g} h & \text { on } \partial M \\
h^{T}-\frac{1}{n-1} \operatorname{Tr}_{g^{T}}\left(h^{T}\right) g^{T} & \text { on } \partial M \\
D H(g) h & \text { on } \partial M
\end{array},\right.$$
is one. The operator
$$h \longrightarrow\left\{\begin{array}{lc}
P(h):=\Delta_{L} h+2 \kappa n \lambda h+2 \Lambda h+v \operatorname{Tr}(h) g & \text { in } M \\
B_{g}(h)-\frac{(n-2) \kappa}{2(1+\kappa n)} d \operatorname{Tr}_{g} h & \text { on } \partial M \\
h^{T}-\frac{1}{n-1} \operatorname{Tr}_{g^{T}}\left(h^{T}\right) g^{T} & \text { on } \partial M \\
D H(g) h & \text { on } \partial M
\end{array},\right.$$
is clearly a Fredholm operator of index zero, like $L_{c}$, by homotopy, it is therefore an isomorphism since it has a trivial kernel. Moreover, for any function $u$ and any traceless symmetric two-tensor $\stackrel{\circ}{h}$,
$$P(u g+\stackrel{\circ}{h})=\frac{1}{1+2(n-1) \kappa} p(u) g+\stackrel{\circ}{P}(\stackrel{\circ}{h}),$$
which proves the stated result. \(\square\)

Theorem 6.2. Let $k \in \mathbb{N} \backslash\{0\}, \alpha \in(0,1), \kappa \neq-\frac{1}{n},-\frac{1}{2(n-1)}$ and $\Lambda \in \mathbb{R}$. Let $g$ be an Einstein metric such that $\operatorname{Ein}(g)$ is non-degenerate. Under the assumptions of Proposition 6.1, we further assume that $-2 \kappa n \lambda-2 \Lambda$ is not in the spectrum of $\Delta_{H}$ with Dirichlet condition. Then, for every small $e \in C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$, for every conformal class $[\gamma]$ close to $\left[g^{T}\right]$ in $\left[C^{k+2, \alpha}\left(\partial M, S_{2}^{+}\right)\right]$, and every function $\mathcal{H}$ close to $H(g)$ in $C^{k+1, \alpha}\left(\partial M, \mathcal{S}_{2}\right)$, there exists a unique $h$ close to zero in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ such that
$$\begin{cases}\operatorname{Ein}(g+h)=\operatorname{Ein}(g)+e & \text { in } M, \\ \left|(g+h)^{T}\right|^{\frac{-1}{n-1}}(g+h)^{T}=\gamma & \text { on } \partial M, \\ H(g+h)=\mathcal{H} & \text { on } \partial M,\end{cases}$$

Moreover, the map $(e,[\gamma], \mathcal{H}) \mapsto h$ is smooth in a neighborhood of $\left(0,\left[g^{T}\right], H(g)\right)$ in a neighborhood of zero between the corresponding Banach spaces.

Proof. From the hypotheses, $D_{h} \mathcal{F}(0,0)$ is an isomorphism. The preceding calculations and the implicit function theorem then imply that for $(e, \gamma, \mathcal{H})$ close to $(0, \gamma, \mathcal{H})$ in their respective spaces, there exists $h$ close to zero in $C^{k+2, \alpha}\left(M, \mathcal{S}_{2}\right)$ such that
$$\mathcal{F}(h, e)=(0,0, \gamma, \mathcal{H}) .$$
We now apply $B_{g+h}$ to the equation $\mathcal{F}_{1}(h, e)=0$, thus
$$B_{g+h} \mathcal{F}_{1}(h, e)=-\mathcal{B}_{g+h}(E)-B_{g+h} \mathcal{L}_{g} \tau^{-1} \mathcal{B}_{g+h}(E)=0 .$$
Setting $\omega=\tau^{-1} \mathcal{B}_{g+h}(E)$, we then have that $\omega$ vanishes at the boundary and
$$P_{g+h} \omega:=B_{g+h} \mathcal{L}_{g} \omega+\tau \omega=0 .$$
But by hypothesis, the operator
$$P_{g}=\frac{1}{2}\left(\Delta-\operatorname{Ric}_{g}\right)+\tau=\frac{1}{2}\left(\Delta+\operatorname{Ric}_{g}+2 \kappa n \lambda+2 \Lambda\right)=\frac{1}{2}\left(\Delta_{H}+2 \kappa n \lambda+2 \Lambda\right)$$
with Dirichlet boundary condition is injective, so if $h$ is small, $P_{g+h}$ remains injective, hence $\omega=0$. \(\square\)

\section*{7. Riemann-Christoffel Type Curvature}

We would like, just as in [7], to show that the image of certain Riemann-Christoffel type operators are submanifolds in $C^{\infty}$, in the neighborhood of the metric $g$. We thus define:
$$\mathcal{E i n}(g)=\operatorname{Riem}(g)+g \otimes(a \operatorname{Ric}(g)+b R(g) g+c g),$$
where ( $\theta$ is the Kulkarni-Nomizu product ( [4] p. 47), and
$$c=\frac{1+(n-2) a}{2(n-1)} \Lambda, \quad b=\frac{\kappa[1+a(n-2)]-a}{2(n-1)}, \quad a \neq-\frac{1}{n-2} .$$

We then obtain:
$$\operatorname{Tr}_{g} \mathcal{E} i n(g)=[a(n-2)+1] \operatorname{Ein}(g) .$$
We define the Riemann-Christoffel type version of $\mathcal{E} i n(g)$ by:
$$\left[g^{-1} \mathcal{E} i n(g)\right]_{k l m}^{i}:=g^{i j} \mathcal{E} i n(g)_{j k l m} .$$

Consider $\mathcal{R}_{3}^{1}$, the subspace of $\mathcal{T}_{3}^{1}$ consisting of tensors satisfying:
$$\tau_{i l m}^{i}=0, \tau_{k l m}^{i}=-\tau_{k m l}^{i}, \tau_{k l m}^{i}+\tau_{m k l}^{i}+\tau_{l m k}^{i}=0 .$$
We define the Fréchet space:
$$C^{\infty}=\cap_{k \in \mathbb{N}} C^{k, \alpha},$$
endowed with the family of seminorms $\left\{\|.\|_{k, \alpha}\right\}_{k \in \mathbb{N}}$.
We then proceed similarly to [7] to prove that:

Theorem 7.1. Under the conditions of Theorem 6.2, the image of the map:
$$\begin{aligned}
C^{\infty}\left(M, \mathcal{S}_{2}\right) & \longrightarrow C^{\infty}\left(M, \mathcal{R}_{3}^{1}\right) \times\left[C^{\infty}\left(\partial M, S_{2}^{+}\right)\right] \times C^{\infty}\left(\partial M, \mathcal{S}_{2}\right) \\
& \mapsto \begin{cases}(g+h)^{-1} \mathcal{E} i n(g+h)-(g)^{-1} \mathcal{E} i n(g) & \text { in } M, \\
\left|(g+h)^{T}\right|^{-\frac{1}{n-1}}(g+h)^{T} & \text { on } \partial M, \\
H(g+h) & \text { on } \partial M,\end{cases}
\end{aligned}$$
is a smooth submanifold of a neighborhood of $\left(0,\left[g^{T}\right], H(g)\right)$.

\section*{References}
\begin{itemize}
\item[] [1] Z. An and L. H. Huang, Local structure Theory of Einstein manifolds with boundary, arXiv: 2405.17577.
\item[] [2] M. T. Anderson, On boundary value problems for Einstein metrics, Geom. Topol. 12 (2008), no. 4, 2009-2045. MR 2431014.
\item[] [3] A. Baldes, Nonexistence of Riemannian metrics with prescribed Ricci tensor, Nonlinear problems in geometry (Mobile, Ala., 1985), Contemp. Math., vol. 51, Amer. Math. Soc., Providence, RI, 1986, pp. 1-8. MR 848927 (87k:53085)
\item[] [4] A.L. Besse, Einstein manifolds, Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge, vol. 10, Springer Verlag, Berlin, New York, Heidelberg, 1987.
\item[] [5] Ph. Delanoë, Obstruction to prescribed positive Ricci curvature, Pacific J. Math. 148 (1991), no. 1, 11-15.
\item[] [6] $\_\_\_\_$, Local solvability of elliptic, and curvature, equations on compact manifolds, J. Reine Angew. Math. 558 (2003), 23-45. MR 1979181 (2004e:53054)
\item[] [7] E. Delay, Etude locale d'opérateurs de courbure sur l'espace hyperbolique, J. Math. Pures Appli. 78 (1999), 389-430.
\item[] [8] $\_\_\_\_$, Study of some curvature operators in the neighbourhood of an asymptotically hyperbolic Einstein manifold, Adv. in Math. 168 (2002), 213-224.
\item[] [9] $\_\_\_\_$, Inversion d'opérateurs de courbure au voisinage de la métrique euclidiennne , Bull. S.M.F, 145(3) (2017), p. 411-420,
\item[] [10] $\_\_\_\_$, Inversion d'opérateurs de courbures au voisinage d'une métrique Ricci parallèle, Annales de l'institut Fourier, Vol. 67 no. 2 (2017), p. 521-538,
\item[] [11] $\_\_\_\_$, $L^{p}$ almost conformal isometries of Sub-Semi-Riemannian metrics and solvability of a Ricci equation, Proc. Amer. Math. Soc. 146 (2018), 3499-3507.
\item[] [12] E. Delay and M. Herzlich, Ricci curvature in the neighbourhood of rank-one symmetric spaces, J. Geom. Anal. 11 (2001), no. 4, 573-588.
\item[] [13] D. DeTurck, Existence of metrics with prescribed ricci curvature : Local theory, Invent. Math. 65 (1981), 179-207.
\item[] [14] $\_\_\_\_$, Prescribing positive Ricci curvature on compact manifolds, Rend. Sem. Mat. Univ. Politec. Torino 43 (1985), no. 3, 357-369 (1986).
\item[] [15] Dennis DeTurck and Hubert Goldschmidt, Metrics with prescribed Ricci curvature of constant rank. I. The integrable case, Adv. Math. 145 (1999), no. 1, 1-97.
\item[] [16] D.M. DeTurck and N. Koiso, Uniqueness and nonexistence of metrics with prescribed Ricci curvature, Ann. Inst. H. Poincaré Anal. Non Linéaire 1 (1984), no. 5, 351-359.
\item[] [17] D.Gaskins,On the Prescribed Ricci Curvature of Noncompact Homogeneous Spaces with Two Isotropy Summands, arXiv:2502.19251 [math.DG].
\item[] [18] C.R. Graham and J.M. Lee, Einstein metrics with prescribed conformal infinity on the ball, Adv. Math. 87 (1991), 186-225.
\end{itemize}
[19] R. Hamilton, The Ricci curvature equation, Seminar on nonlinear partial differential equations (Berkeley, Calif., 1983), Math. Sci. Res. Inst. Publ., vol. 2, Springer, New York, 1984, pp. 47-72. MR 765228 (86b:53040)
[20] A. Lichnerowicz, Propagateurs et commutateurs en relativité générale, Pub. Math. de l'IHES 10 (1961), 5-56.
[21] J. Lott, Mean curvature flow in a Ricci flow background. Comm. Math. Phys., 313(2), (2012), 517-533.
[22] D. Mitrea, I. Mitrea,M. Mitrea and M. Taylor, The Hodge-Laplacian: Boundary Value Problems on Riemannian Manifolds, Berlin, Boston: De Gruyter, vol. 64, 2025. https://doi.org/10.1515/9783111481401
[23] A. Pulemotov, Metrics with prescribed ricci curvature near the boundary of a manifold, Mathematische Annalen (2013), no. 357, 969-986.
[24] A. Pulemotov, The Dirichlet problem for the prescribed Ricci curvature equation on cohomogeneity one manifolds, Annali di Matematica Pura ed Applicata, 195 (2016), 1269-1286.

Laboratoire de Mathématiques d'Avignon, Fac. des Sciences, F84916 Avignon, France
F.R.U.M.A.M. - CNRS Aix Marseille Université- F13 331 Marseille, France
Email address: Erwann.Delay@univ-avignon.fr
URL: https://erwanndelay.wordpress.com/