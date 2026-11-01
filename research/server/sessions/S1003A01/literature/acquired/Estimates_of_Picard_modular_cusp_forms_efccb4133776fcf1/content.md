---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 2301_11160.pdf
converter: mathpix
format: mmd
---

\title{
ESTIMATES OF PICARD MODULAR CUSP FORMS
}

\author{
ANILATMAJA ARYASOMAYAJULA, BASKAR BALASUBRAMANYAM, AND DYUTI ROY
}

\begin{abstract}
In this article, for $n \geq 2$, we compute asymptotic, qualitative, and quantitative estimates of the Bergman kernel of Picard modular cusp forms associated to torsion-free, cocompact subgroups of $\operatorname{SU}((n, 1), \mathbb{C})$. The main result of the article is the following result. Let $\Gamma \subset \operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$ be a torsion-free subgroup of finite index, where $K$ is a totally imaginary field. Let $\mathcal{B}_{\Gamma}^{k}$ denote the Bergman kernel associated to the $\mathcal{S}_{k}(\Gamma)$, complex vector space of weight- $k$ cusp forms with respect to $\Gamma$. Let $\mathbb{B}^{2}$ denote the 2-dimensional complex ball endowed with the hyperbolic metric, and let $X_{\Gamma}:=\Gamma \backslash \mathbb{B}^{2}$ denote the quotient space, which is a noncompact complex manifold of dimension 2. Let $|\cdot|_{\text {pet }}$ denote the point-wise Petersson norm on $\mathcal{S}_{k}(\Gamma)$. Then, for $k \geq 6$, we have the following estimate
$$\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=O_{\Gamma}\left(k^{\frac{5}{2}}\right),$$
where the implied constant depends only on $\Gamma$.
\end{abstract}

\section*{1. Introduction}
1.1. History and background. Estimates of automorphic forms is a subject of great interest in recent times, owing to their applications both in arithmetic intersection theory, and arithmetic quantum chaos. Especially, estimates of the Bergman kernel associated to the vector bundle of automorphic forms is of arithmetic and geometric significance.

Estimates of Bergman kernel associated to cusp forms defined over hyperbolic Riemann surfaces were derived in [AU95] and [FJK16]. Furthermore, off-diagonal estimates of these Bergman kernels were derived in [AM18] and [AM20], which were useful in deriving sub-convexity estimates of Hecke eigen cusp forms associated to certain cocompact Fuchsian subgroups arising from quaternion algebras in [AB22].

In [Ma22], optimal estimates of the Bergman kernel associated to Siegel modular cusp forms were derived in both the cocompact and cofinite setting.

In this article, we extend methods from [AM18], [AM20], Ar16], and [AB18], to derive estimates of Picard modular cusp forms. For $n \geq 2$, we prove the asymptotic, qualitative, and quantitative estimates of the Bergman kernel associated to Picard modular cusp forms defined with respect to cocompact subgroups of $\operatorname{SU}((n, 1), \mathbb{C})$.

Furthermore, we derive quantitative estimates of the Bergman kernel associated to Picard modular cusp forms defined with respect to finite index subgroups of $\mathrm{SU}\left((2,1), \mathcal{O}_{K}\right)$, where $\mathcal{O}_{K}$ is the ring of integers of a totally imaginary quadratic field.

Notation. For $n \geq 2$, let
$$\mathbb{B}^{n}:=\left\{z:=\left.\left(z_{1}, \ldots, z_{n}\right)^{t} \in \mathbb{C}^{n}| | z\right|^{2}:=\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}<1\right\}$$
denote the complex hyperbolic ball endowed with the hyperbolic metric $\mu_{\text {hyp }}$, and let $\Gamma \subset$ $\operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cofinite subgroup, acting on $\mathbb{B}^{n}$ via fractional linear transformations. Let $X_{\Gamma}=\Gamma \backslash \mathbb{B}^{n}$ denote the quotient space, which is an $n$-dimensional complex manifold of finite hyperbolic volume.

\footnotetext{
Date: February 10, 2023.
2010 Mathematics Subject Classification. 11F11, 11F12.
Key words and phrases. Sup-norm bounds of cusp forms.
}

For $k \geq 1$, let $\mathcal{S}_{k}(\Gamma)$ denote the complex vector space of weight- $k$ cusp forms, and let $\left\{f_{1}, \ldots f_{d_{k}}\right\}$ denote an orthonormal basis of $\mathcal{S}_{k}(\Gamma)$ with respect to the Petersson inner-product.

With notation as above, for $n \geq 2$, and $k \geq 1$, and $z, w \in \mathbb{B}^{n}$, the Bergman kernel is given by the following formula
$$\mathcal{B}_{\Gamma}^{k}(z, w):=\sum_{j=1}^{d_{k}} f_{j}(z) \overline{f_{j}(w)},$$
which is a holomorphic cusp form in the $z$-variable, and an anti-holomorphic cusp form in the $w$-variable. The definition of the Bergman kernel is independent of the choice of the orthonormal basis of $\mathcal{S}_{k}(\Gamma)$.

The Petersson norm of the Bergman kernel at any $z \in \mathbb{B}^{n}$ is given by the following formula
$$\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}:=\left(1-|z|^{2}\right)^{k}\left|\mathcal{B}_{\Gamma}^{k}(z, z)\right|=\left(1-|z|^{2}\right)^{k} \sum_{j=1}^{k}\left|f_{j}(z)\right|^{2} .$$
1.2. Statement of main results. We now state the first main result of the article, which is proved as Theorem 3.1.

Theorem 1. With notation as above, for $n \geq 2$, let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cocompact subgroup. Then, for $z \in X_{\Gamma}$, we have
$$\lim _{k \rightarrow \infty} \frac{1}{k^{n}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=\frac{1}{(4 \pi)^{n}},$$
and the convergence of the above limit is uniform in $z \in X$.
The second main result of the article is the following theorem, which is proved as Corollary 4.3.
Theorem 2. With notation as above, for $n \geq 2$, let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cocompact subgroup. Then, for $k \geq 2 n+2$, we have the following estimate
$$\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=O_{\Gamma}\left(k^{n}\right),$$
where the implied constant depends only on $\Gamma$.
The third result of the article is the following theorem, which is proved as Corollary 5.3.
Theorem 3. With notation as above, let $\Gamma \subset \operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$ be a torsion-free subgroup of finite index, where $K$ is a totally imaginary quadratic field. Furthermore, we assume that $\Gamma$ admits only one cusp at $\infty$. Then, for $k \geq 6$, we have the following estimate
$$\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=O_{\Gamma}\left(k^{5 / 2}\right),$$
where the implied constant depends only on $\Gamma$.

Remark 1.1. The implied constants in estimates (1) and (2), can be explicitly computed, and also remain stable in covers, which we demonstrate in Remark 5.4.

The assumption that $\Gamma$ admits only one cusp at $\infty$ in Theorem 3, is only for notational convenience, and estimate (2) easily extends to cofinite subgroups with multiple cusps. Furthermore, torsion points should not be much of an impediment for extending estimate (2) to subgroups with torsion points.

Lastly, estimate (2) can be easily extended to cofinite subgroups, which are comensurable with $\operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$.

Remark 1.2. Let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, cofinite subgroup. Following results from [FJK16], [AB18] and [Ma22], the following estimate is expected, which has now assumed the status of a folk-lore conjecture
$$\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=O_{\Gamma}\left(k^{3 n / 2}\right) .$$
However, estimate (2) suggests that we can expect a finer estimate than the above estimate for semi-simple Lie groups acting on symmetric spaces of rank 1.

\section*{2. Background material}

We now set up the notation, which we use for the rest of the article and recall the background material for the proofs of the main results.
2.1. The ball model. For $n \geq 2$, let $H$ be a Hermitian matrix of signature $(n, 1)$, and let $\left(\mathbb{C}^{n+1}, H\right)$ denote the Hermitian inner-product space $\mathbb{C}^{n+1}$ equipped with the Hermitian innerproduct $\langle\cdot, \cdot\rangle_{H}$, induced by $H$. For $z, w \in \mathbb{C}^{n+1}$, the Hermitian inner-product $\langle\cdot, \cdot\rangle_{H}$ is defined as
$$\langle z, w\rangle_{H}=w^{*} H z,$$
where $w^{*}$ denotes the complex transpose of $w$.
Set
$$V_{-}(H):=\left\{z \in \mathbb{C}^{n+1} \mid\langle z, z\rangle_{H}<0\right\} \subset \mathbb{C}^{n+1} ; V_{0}(H):=\left\{z \in \mathbb{C}^{n+1} \mid\langle z, z\rangle_{H}=0\right\} \subset \mathbb{C}^{n+1} .$$
Set
$$\mathcal{A}^{n+1}:=\left\{\left(z_{1}, \ldots, z_{n+1}\right)^{t} \in \mathbb{C}^{n+1} \mid z_{n+1} \neq 0\right\} \subset \mathbb{C}^{n+1} .$$
The subspace $\mathcal{A}^{n+1}$ inherits the structure of a Hermitian inner-product space, which we denote by $\left(\mathcal{A}^{n+1}, H\right)$. We have the following map
$$\begin{aligned}
& \phi: \mathcal{A}_{n+1} \longrightarrow \mathbb{C}^{n} \\
& \left(z_{1}, \ldots, z_{n+1}\right)^{t} \mapsto\left(\frac{z_{1}}{z_{n+1}}, \cdots, \frac{z_{n}}{z_{n+1}}\right)^{t} .
\end{aligned}$$
The complex hyperbolic space $\mathcal{H}^{n}(\mathbb{C})$ and its boundary $\partial \mathcal{H}^{n}(\mathbb{C})$ are defined as
$$\mathcal{H}^{n}(\mathbb{C}):=\phi\left(V_{-}(H)\right) \subset \mathbb{C}^{n} ; \partial \mathcal{H}^{n}(\mathbb{C}):=\phi\left(V_{0}(H)\right) \subset \mathbb{C}^{n} .$$
The choice of Hermitian matrix gives different models of hyperbolic $n$-space. For
$$H=\left(\begin{array}{cc}
\mathrm{Id}_{n} & 0 \\
0 & -1
\end{array}\right),$$
we obtain the unit ball model of the complex hyperbolic space, where $\mathrm{Id}_{n}$ denotes the identity matrix of order $n$, which we now describe.

For any $z=\left(z_{1}, \ldots, z_{n}\right)^{t} \in \mathcal{H}^{n}(\mathbb{C})$, consider the lift $\tilde{z}:=\left(z_{1}, \ldots, z_{n}, 1\right)^{t} \in \mathcal{A}^{n+1}$. Observe that
$$\langle\tilde{z}, \tilde{z}\rangle_{H}<0 \Longleftrightarrow\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}<1 .$$
Thus $\mathcal{H}^{n}(\mathbb{C})$ can be identified with the open unit ball
$$\mathbb{B}^{n}:=\left\{z:=\left.\left(z_{1}, \ldots, z_{n}\right)^{t} \in \mathbb{C}^{n}| | z\right|^{2}:=\left|z_{1}\right|^{2}+\cdots+\left|z_{n}\right|^{2}<1\right\} .$$
This model which is also known as the ball model, is the natural generalization of Poincare disk model of upper half-plane $\mathbb{H}$.

The space is endowed with its usual Kähler-Bergman metric $\mu_{\text {hyp }}$, which has constant negative curvature -1. For any given $z=\left(z_{1}, \ldots, z_{n}\right) \in \mathbb{B}^{n}$, the hyperbolic metric $\mu_{\text {hyp }}(z)$ is given by the following formula
$$\mu_{\mathrm{hyp}}(z):=-2 i \partial \bar{\partial} \log \left(1-|z|^{2}\right),$$
and let $\mu_{\text {hyp }}^{\text {vol }}(z)$ denote the associated volume form.
From standard results in hyperbolic geometry, for any $z=\left(z_{1}, \ldots, z_{n}\right)^{t}, w=\left(w_{1}, \ldots, w_{n}\right)^{t} \in \mathbb{B}^{n}$ with respective lifts $\tilde{z}=\left(z_{1}, \ldots, z_{n}, 1\right)^{t}, \tilde{w}=\left(w_{1}, \ldots, w_{n}, 1\right)^{t} \in \mathcal{A}^{n+1}$, the hyperbolic distance in the ball model is given by the following relation
$$\cosh ^{2}\left(\mathrm{~d}_{\mathrm{hyp}}(z, w) / 2\right)=\frac{\langle\tilde{z}, \tilde{w}\rangle_{H}\langle\tilde{w}, \tilde{z}\rangle_{H}}{\langle\tilde{z}, \tilde{z}\rangle_{H}\langle\tilde{w}, \tilde{w}\rangle_{H}}, \quad \text { where }\langle\tilde{z}, \tilde{w}\rangle_{H}:=\tilde{w}^{*} H \tilde{z}=\sum_{j=1}^{n} z_{j} \bar{w}_{j}-1,$$
and $H$ is as described in equation (3).
The unitary group $\operatorname{SU}((n, 1), \mathbb{C})$ is given by
$$\operatorname{SU}((n, 1), \mathbb{C}):=\left\{A \in \mathrm{SL}(n, \mathbb{C}) \mid A^{*} H A=H\right\}, \text { where } H=\left(\begin{array}{cc}
\operatorname{Id}_{n} & 0 \\
0 & -1
\end{array}\right),$$
and $\operatorname{Id}_{n}$ denotes the identity matrix of order $n$.
The group $\operatorname{SU}((n, 1), \mathbb{C})$ acts on $\mathbb{B}^{n}$ via bi-holomorphic mappings, which are given by fractional linear transformations, which we explain here. Let
$$\gamma=\left(\begin{array}{ll}
A & B \\
C & D
\end{array}\right) \in \operatorname{SU}((n, 1), \mathbb{C}),$$
where $A \in M_{n \times n}(\mathbb{C}), B \in M_{n \times 1}(\mathbb{C}), C \in M_{1 \times n}(\mathbb{C})$, and $D \in \mathbb{C}$. For $z=\left(z_{1}, \ldots, z_{n}\right)^{t} \in \mathbb{B}^{n}$, the action of $\gamma$ on $\mathbb{B}^{n}$, is given by
$$\gamma z:=\frac{A z+B}{C z+D} .$$
Here, $z$ is seen as a column vector vector in $\mathbb{C}^{n}$.
Let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torision-free, cofinite subgroup, and let $X_{\Gamma}:=\Gamma \backslash \mathbb{B}^{n}$ denote the quotient space, which is called a Picard modular variety of dimension $n$. The Picard modular variety $X_{\Gamma}$ admits the structure of a complex manifold of dimension $n$. The hyperbolic metric $\mu_{\text {hyp }}(z)$ is $\operatorname{SU}((n, 1), \mathbb{C})$-invariant, and hence, defines a Kähler metric on $X_{\Gamma}$.

When $\Gamma$ is a cocompact subgroup, the Picard modular variety $X$ is a compact complex manifold of dimension $n$. When $\Gamma$ is cofinite, then the Picard modular variety $X_{\Gamma}$ is a non-compact complex manifold of dimension $n$, of finite hyperbolic volume.
2.2. Three models of $\mathcal{H}^{2}(\mathbb{C})$. For $n=2$, we use different models of the hyperbolic space, which we now describe in detail.

Model (1): As in Section (2.1), the ball model
$$\mathbb{B}^{2}:=\left\{z=\left.\left(z_{1}, z_{2}\right)^{t} \in \mathbb{C}^{2}| | z\right|^{2}:=\left|z_{1}\right|^{2}+\left|z_{2}\right|^{2}<1\right\}$$
is obtained by setting
$$H=\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & -1
\end{array}\right) .$$

Model (2): For $z=\left(z_{1}, z_{2}, z_{3}\right)^{t}$ and $w=\left(w_{1}, w_{2}, w_{3}\right)^{t} \in \mathbb{C}^{3}$, consider the Hermitian form
$$\langle z, w\rangle_{2}=i z_{1} \overline{w_{3}}+z_{2} \overline{w_{2}}-i z_{3} \overline{w_{1}},$$
which is determined by the following Hermitian matrix of signature $(2,1)$
$$H_{2}=\left(\begin{array}{ccc}
0 & 0 & -i \\
0 & 1 & 0 \\
i & 0 & 0
\end{array}\right) .$$
For any $z=\left(z_{1}, z_{2}\right)^{t} \in \mathcal{H}^{2}(\mathbb{C})$, with the lift $\tilde{z}:=\left(z_{1}, z_{2}, 1\right)^{t} \in \mathcal{A}^{3}$, observe that
$$\langle\tilde{z}, \tilde{z}\rangle_{2}<0 \Longleftrightarrow 2 \operatorname{Im}\left(z_{1}\right)-\left|z_{2}\right|^{2}>0 .$$
Thus $\mathcal{H}^{2}(\mathbb{C})$ can be identified with the following space
$$\mathbb{B}_{2}^{2}:=\left\{z=\left(z_{1}, z_{2}\right)^{t} \in \mathbb{C}^{2}\left|2 \operatorname{Im}\left(z_{1}\right)-\left|z_{2}\right|^{2}>0\right\} .\right.$$

Model (3): For $z=\left(z_{1}, z_{2}, z_{3}\right)^{t}$ and $w=\left(w_{1}, w_{2}, w_{3}\right)^{t} \in \mathbb{C}^{3}$, consider the Hermitian form
$$\langle z, w\rangle_{3}=z_{1} \overline{w_{3}}+z_{2} \overline{w_{2}}+z_{3} \overline{w_{1}},$$
which is determined by the following Hermitian matrix of signature $(2,1)$
$$H_{3}=\left(\begin{array}{lll}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{array}\right) .$$
For any $z=\left(z_{1}, z_{2}\right)^{t} \in \mathcal{H}^{2}(\mathbb{C})$ with the lift $\tilde{z}:=\left(z_{1}, z_{2}, 1\right)^{t} \in \mathcal{A}^{3}$, observe that
$$\langle\tilde{z}, \tilde{z}\rangle_{3}<0 \Longleftrightarrow 2 \operatorname{Re}\left(z_{1}\right)+\left|z_{2}\right|^{2}<0 .$$
Thus $\mathcal{H}^{2}(\mathbb{C})$ can be identified with the following space
$$\mathbb{B}_{3}^{2}:=\left\{z=\left(z_{1}, z_{2}\right)^{t} \in \mathbb{C}^{2}\left|2 \operatorname{Re}\left(z_{1}\right)+\left|z_{2}\right|^{2}<0\right\} .\right.$$
These are the three models which we work with, to prove estimate (2). We treat the ball model as the base model, and we go back and forth between the models as per our convenience.

The Cayley transformation
$$\gamma_{3}:=\left(\begin{array}{ccc}
1 & 1 & 0 \\
0 & 1 & -1 \\
1 & 1 & -1
\end{array}\right):\left(\mathcal{A}^{3}, H\right) \longrightarrow:\left(\mathcal{A}^{3}, H_{3}\right)$$
defines an isometry.
The Cayley transformation
$$\gamma_{23}:=\left(\begin{array}{ccc}
i & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right):\left(\mathcal{A}^{3}, H_{2}\right) \longrightarrow\left(\mathcal{A}^{3}, H_{3}\right)$$
defines an isometry.
From the above Cayley transformations, it is easy to see that the map
$$\gamma_{2}:=\gamma_{23}^{-1} \circ \gamma_{3}:\left(\mathcal{A}^{3}, H\right) \longrightarrow\left(\mathcal{A}^{3}, H_{2}\right)$$
defines an isometry.
Let $\Gamma \subset \operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$ be a torsion-free, finite index subgroup, with only one cusp at $\infty$. As discussed in Section (2.1), the quotient space $X_{\Gamma}:=\Gamma \backslash \mathbb{B}^{2}$ admits the structure of a noncompact complex manifold of dimension 2, of finite hyperbolic volume.

The Picard modular variety $X_{\Gamma}$ is isometric to $\Gamma^{2} \backslash \mathbb{B}_{2}^{2}$ and $\Gamma^{3} \backslash \mathbb{B}_{3}^{2}$, where $\Gamma_{2}:=\gamma_{2} \Gamma \gamma_{2}^{-1}$ and $\Gamma_{3}:=\gamma_{3} \Gamma \gamma_{3}^{-1}$.

Let $\Gamma_{\infty}$ denote the stabilizer of the cusp $\infty$. Let $\Gamma_{\infty}^{2}$ and $\Gamma_{\infty}^{3}$ be the corresponding stabilizer group in the domains $\mathbb{B}_{2}^{2}$ and $\mathbb{B}_{3}^{2}$, respectively. Furthermore, we have following relation
$$\Gamma_{\infty}^{3}=\gamma_{3} \Gamma_{\infty}^{1} \gamma_{3}^{-1}=\gamma_{23} \Gamma_{\infty}^{2} \gamma_{23}^{-1} ;$$
where $\gamma_{13}$ and $\gamma_{23}$ are described in the equations (9) and (10), respectively.
As discussed in [Ho98], the stabilizer subgroup of $\infty$ in the group $\gamma_{2} \Gamma_{0} \gamma_{2}^{-1}$, is explicitly described as
$$\Gamma_{0, \infty}^{2}=\left\{\left.\left(\begin{array}{ccc}
1 & i \bar{\alpha} & i \frac{|\alpha|^{2}}{2}+\beta \\
0 & 1 & \alpha \\
0 & 0 & 1
\end{array}\right) \right\rvert\, \alpha \in \mathbb{C}, \beta \in \mathbb{R}\right\},$$
where $\Gamma_{0}:=\operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$, where $K$ is a totally imaginary quadratic field.
Combining equations (12) and (13), the stabilizer subgroup of $\infty$ in the group $\gamma_{3} \Gamma_{0} \gamma_{3}^{-1}$, is explicitly described as
$$\Gamma_{0, \infty}^{3}=\left\{\left.\left(\begin{array}{ccc}
1 & -\bar{\alpha} & -\frac{|\alpha|^{2}}{2}+i \beta \\
0 & 1 & \alpha \\
0 & 0 & 1
\end{array}\right) \right\rvert\, \alpha \in \mathbb{C}, \beta \in \mathbb{R}\right\} .$$
2.3. Picard modular cusp forms and the Bergman kernel. With hypothesis as above, for $n \geq 2$, let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cofinite subgroup, and let $X_{\Gamma}=\Gamma \backslash \mathbb{B}^{n}$ denote the quotient space. For any $z, w \in X_{\Gamma}$, let $\mathrm{d}_{\text {hyp }}(z, w)$ denote the geodesic distance between the points $z$ and $w$ on the Picard modular variety $X_{\Gamma}$, i.e., $\mathrm{d}_{\text {hyp }}$ is the natural distance function associated to the hyperbolic metric $\mu_{\text {hyp }}$ on $X_{\Gamma}$.

Locally, we identify $X_{\Gamma}$ with its universal cover $\mathbb{B}^{n}$. For $z, w \in X_{\Gamma}$, the hyperbolic distance function $\mathrm{d}_{\text {hyp }}(z, w)$ satisfies equation (5).

Let $\operatorname{vol}_{\text {hyp }}\left(X_{\Gamma}\right)$ denote the volume of $X_{\Gamma}$ with respect to the hyperbolic volume form $\mu_{\text {hyp }}^{\text {vol }}(z)$, and let
$$\mu_{\mathrm{shyp}}^{\mathrm{vol}}:=\frac{\mu_{\mathrm{hyp}}^{\mathrm{vol}}}{\operatorname{vol}_{\mathrm{hyp}}\left(X_{\Gamma}\right)},$$
denote the rescaled hyperbolic volume form, which measures the volume of $X_{\Gamma}$ to be one.
When $\Gamma$ is cocompact, the injectivity radius of $X_{\Gamma}$ is given by the following formula
$$r_{X_{\Gamma}}:=\inf \left\{\mathrm{d}_{\text {hyp }}(z, \gamma z) \mid z \in X_{\Gamma}, \gamma \in \Gamma \backslash \mathrm{Id}\right\},$$
where Id is the identity matrix.
When $\Gamma \subset \operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$ is a torsion-free, finite index subgroup with only one cusp at $\infty$, the injectivity radius of $X_{\Gamma}$ is given by the following formula
$$r_{X_{\Gamma}}:=\inf \left\{\mathrm{d}_{\text {hyp }}(z, \gamma z) \mid z \in X_{\Gamma}, \gamma \in \Gamma \backslash \Gamma_{\infty}\right\},$$
where $\Gamma_{\infty}$ is the stabilizer of the cusp $\infty$, which is as defined in Section 2.2.
Picard modular cusp forms. For $n \geq 2$, let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cocompact subgroup. For $k \geq 1$, a holomorphic function $f: \mathbb{B}^{n} \rightarrow \mathbb{C}$ is said to be Picard modular cusp form of weight- $k$ with respect to $\Gamma$, if for any $\gamma \in \Gamma$ and $z \in \mathbb{B}^{n}, f$ satisfies the following transformation property:
$$f(\gamma z)=(C z+D)^{k} f(z) \text {, where } \gamma=\left(\begin{array}{cc}
A & B \\
C & D
\end{array}\right) \in \Gamma \text {. }$$
If $\Gamma$ is cofinite, then $f$ has to satisfy the additional condition that $f$ vanishes at all cusps of $\Gamma$.

So, if $\Gamma \subset \operatorname{SU}\left((n, 1), \mathcal{O}_{K}\right)$ is a torsion-free, finite index subgroup with only one cusp at $\infty$, then for $f$ to be a Picard modular cusp form of weight- $k$ with respect to $\Gamma, f$ has to satisfy the transformation property (17), and the condition that $f(\infty)=0$.

The complex vector-space of weight- $k$ Picard modular cusp forms is denoted by $\mathcal{S}_{k}(\Gamma)$.
For any $f \in \mathcal{S}_{k}(\Gamma)$, the Petersson norm at a point $z \in X$ is given by the following formula:
$$|f(z)|_{\text {pet }}^{2}:=\left(1-|z|^{2}\right)^{k}|f(z)|^{2} .$$
The Petersson norm induces an $L^{2}$-metric on $\mathcal{S}_{k}(\Gamma)$, which we denote by $\langle\cdot, \cdot\rangle_{\text {pet }}$, and is known as the Petersson inner-product. For any $f, g \in \mathcal{S}_{k}(\Gamma)$, the Petersson inner-product is given by the following formula
$$\langle f, g\rangle_{\mathrm{pet}}:=\int_{\mathcal{F}_{\Gamma}}\left(1-|z|^{2}\right)^{k} f(z) \overline{g(z)} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z),$$
where $\mathcal{F}$ denotes a fundamental domain of $X_{\Gamma}$
When $\Gamma$ is cocompact, Picard modular cusp forms can be realized as the global section of a line bundle. Let $\mathcal{L}$ denote the line bundle, whose sections are Picard modular cusp forms of weight-1. Then, for $k \geq 1$, we have
$$H^{0}\left(X_{\Gamma}, \mathcal{L}^{\otimes k}\right)=\mathcal{S}_{k}(\Gamma) .$$
The Petersson norm and the Petersson inner-product can be realized as the point-wise norm and $L^{2}$ metric on $H^{0}\left(X_{\Gamma}, \mathcal{L}^{\otimes k}\right)$.
Bergman kernel. Let $d_{k}$ denote the dimension of the vector-space $\mathcal{S}_{k}(\Gamma)$, and let $\left\{f_{1}, \ldots f_{d_{k}}\right\}$ denote an orthonormal basis of $\mathcal{S}_{k}(\Gamma)$ with respect to the Petersson inner-product. Then, for any $z, w \in \mathbb{B}^{n}$, the Bergman kernel $\mathcal{B}_{\Gamma}^{k}(z)$ associated to the vector space $\mathcal{S}_{k}(\Gamma)$ is given by the following formula:
$$\mathcal{B}_{\Gamma}^{k}(z, w):=\sum_{j=1}^{d_{k}} f_{j}(z) \overline{f_{j}(w)},$$
and when $z=w$, for brevity of notation, we denote $\mathcal{B}_{\Gamma}^{k}(z, z)$ by $\mathcal{B}_{\Gamma}^{k}(z)$.
For a fixed $w \in \mathbb{B}^{n}$, the Bergman kernel is a holomorphic cusp form of weight- $k$ in $z$. Similarly, for a fixed $z \in \mathbb{B}^{n}$, the Bergman kernel is a anti-holomorphic cusp form of weight- $k$ in $w$. The Petersson norm induces the following norm on the Bergman kernel at any $z, w \in \mathbb{B}^{n}$ with respective lifts $\tilde{z}, \tilde{w} \in \mathcal{A}^{n+1}$ is given by the following formula
$$\left|\mathcal{B}_{\Gamma}^{k}(z, w)\right|_{\text {pet }}:=\left(-\langle\tilde{z}, \tilde{z}\rangle_{H}\right)^{k / 2} \cdot\left(-\langle\tilde{w}, \tilde{w}\rangle_{H}\right)^{k / 2}=\left(1-|z|^{2}\right)^{k / 2} \cdot\left(1-|w|^{2}\right)^{k / 2} \cdot\left|\mathcal{B}_{\Gamma}^{k}(z, w)\right| .$$
Now we introduce an alternate expression for the Bergman kernel associated to $\mathcal{S}_{k}(\Gamma)$, the complex vector-space of Picard cusp forms of the ball domain $\mathbb{B}_{n}$. For any $k \geq 2 n+1$, and $z=\left(z_{1}, \ldots, z_{n}\right)^{t}, w=\left(w_{1}, \ldots, w_{n}\right)^{t} \in \mathbb{B}_{n}$, the Bergman kernel $\mathcal{B}_{\Gamma}^{k}(z, w)$ associated to $\mathcal{S}_{k}(\Gamma)$ has an alternate expression, which is given by the following formula
$$\begin{aligned}
& \mathcal{B}_{\Gamma}^{k}(z, w):=\sum_{\gamma \in \Gamma} \frac{C_{\Gamma, k}}{|\langle z, \gamma w\rangle|^{k}(C w+D)^{k}} \\
& \text { where } \gamma=\left(\begin{array}{ll}
A & B \\
C & D
\end{array}\right), \text { and }\langle z, w\rangle:=1-\sum_{j=1}^{n} z_{j} \bar{w}_{j},
\end{aligned}$$
and $C_{\Gamma, k}$ is a constant, which satisfies the following estimate
$$C_{\Gamma, k}=O_{\Gamma}\left(k^{n}\right) .$$

The implied constant in the above estimate is a constant, which depends only on $\Gamma$, and can be computed explicitly by combining the two definitions of the Bergman kernel, namely equations (19) and (20), and using the Riemann-Roch theorem.

From (20), the Petersson norm at any $z \in X_{\Gamma}$ is given by
$$\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=\left(1-|z|^{2}\right)^{k} \cdot\left|\mathcal{B}_{\Gamma}^{k}(z)\right| \leq \sum_{\gamma \in \Gamma} \frac{C_{\Gamma, k}\left(1-|z|^{2}\right)^{k / 2}}{|1-\langle z, \gamma z\rangle|^{k}} \cdot \frac{\left(1-|z|^{2}\right)^{k / 2}}{|C z+D|^{k}} .$$
For any $\gamma=\left(\begin{array}{cc}A & B \\ C & D\end{array}\right) \in \Gamma$, and $z \in X_{\Gamma}$, we have
$$\left(1-|\gamma z|^{2}\right)=-\langle\tilde{\gamma} z, \tilde{\gamma} z\rangle_{H}=\frac{\left(1-|z|^{2}\right)}{|C z+D|^{2}},$$
where $\tilde{\gamma} z$ denotes the lift of $\gamma z$ to $\mathcal{A}^{n+1}$.
Using the above relation, and combining equations (5) and (22), we derive
$$\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \leq \sum_{\gamma \in \Gamma} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)} .$$

Picard modular cusp forms on $\mathcal{H}^{2}(\mathbb{C})$. We now describe the hyperbolic distance, and Petersson norm of Picard modular cusp forms, in Model (3) of the hyperbolic space $\mathcal{H}^{2}(\mathbb{C})$.

For any $z=\left(z_{1}, z_{2}\right)^{t}, w=\left(w_{1}, w_{2}\right)^{t} \in \mathbb{B}_{3}^{2}$ with respective lifts $\tilde{z}=\left(z_{1}, z_{2}, 1\right)^{t}, \tilde{w}=\left(w_{1}, w_{2}, 1\right) \in$ $\mathcal{A}^{3}$, the hyperbolic distance is given by the following formula
$$\cosh ^{2}\left(\mathrm{~d}_{\operatorname{hyp}}(z, w) / 2\right)=\frac{\langle\tilde{z}, \tilde{w}\rangle_{3}\langle\tilde{w}, \tilde{z}\rangle_{3}}{\langle\tilde{z}, \tilde{z}\rangle_{3}\langle\tilde{w}, \tilde{w}\rangle_{3}},$$
where $\langle\cdot, \cdot\rangle_{3}$ is as given by equation (8).
For any $k \geq 1$ and $f \in \mathcal{S}_{k}(\Gamma)$, at any $z \in \mathbb{B}_{3}^{2}$ with lift $\tilde{z} \in \mathcal{A}^{3}$, the Petersson norm is given by the following formula
$$|f(z)|_{\text {pet }}^{2}:=\left(-\langle\tilde{z}, \tilde{z}\rangle_{3}\right)^{k} \cdot|f(z)|^{2}=\left(-2 \operatorname{Re}\left(z_{1}\right)-\left|z_{2}\right|^{2}\right)^{k}|f(z)|^{2} .$$

\section*{3. Asymptotic estimates of the Bergman kernel}

In this section, we state the relevant results from geometric analysis, that are required in proving Theorems 3.1 and 4.2, and Corollary 3.2. We repeat the exposition from [AM18] and [AB18] for the benefit of the reader.

Asymptotic estimates. Let $(M, \omega)$ be a compact complex manifold of dimension $n$ with natural Hermitian metric $\omega$. Let $\lambda$ and $\ell$, be a vector bundle of rank $r$ and a positive Hermitian holomorphic line bundle on $M$, respectively. Let $\|\cdot\|_{\lambda}$ and $\|\cdot\|_{\ell}$ denote the Hermitian metrics on and $\lambda$ and $\ell$, respectively. Furthermore, for any section $s$ of the line bundle $\ell$, the Hermitian metric $\|\cdot\|_{\ell}$ is given by the following formula $\|s(z)\|_{\ell}^{2}:=e^{-\phi(z)}|s(z)|^{2}$, where $\phi(z)$ is a real-valued function.

For any $k \geq 0$, let $\bar{\square}_{k}:=\left(\bar{\partial}^{*}+\bar{\partial}\right)^{2}$ denote the $\bar{\partial}$-Laplacian acting on smooth sections of $\lambda \otimes \ell^{\otimes k}$. Let $K_{M, \lambda \otimes \ell \otimes k}(t ; z, w)$ denote the smooth kernel of the operator $e^{-\frac{2 t}{k} \bar{口}_{k}}$. We refer the reader to p. 2 in [Bo96], for the details regarding the properties which uniquely characterize the heat kernel $K_{M, \lambda \otimes \ell^{\otimes k}}(t ; z, w)$. When $z=w \in M$, the heat kernel $K_{M, \lambda \otimes \ell^{\otimes k}}(t ; z, z)$ admits the following spectral expansion:
$$K_{M, \lambda \otimes \ell \otimes k}(t ; z, z)=\sum_{n \geq 0} e^{-\frac{2 t}{k} \alpha_{n}^{k}}\left\|\varphi_{n}(z)\right\|_{\lambda \otimes \ell \otimes k}^{2},$$
where $\left\{\alpha_{n}^{k}\right\}_{n \geq 0}$ denotes a set of eigenvalues of $\bar{\square}_{k}$ (counted with multiplicities), and $\left\{\varphi_{n}\right\}_{n \geq 0}$ denotes the set of associated orthonormal eigenfunctions.

Let $H^{0}\left(M, \lambda \otimes \ell^{\otimes k}\right)$ denote the vector space of global holomorphic sections of the vector bundle $\lambda \otimes \ell^{\otimes k}$, and let $\left\{s_{i}\right\}$ denote an orthonormal basis of $H^{0}\left(M, \lambda \otimes \ell^{\otimes k}\right)$. For any $z \in M$, the following function is called the Bergman kernel associated to the vector bundle $\lambda \otimes \ell^{\otimes k}$
$$\mathcal{B}_{M}^{\lambda \otimes \ell^{\otimes k}}(z):=\sum_{i}\left\|s_{i}(z)\right\|_{\lambda \otimes \ell \otimes k}^{2} .$$
The above definition is independent of the choice of orthonormal basis of $H^{0}\left(M, \lambda \otimes \ell^{\otimes k}\right)$.
It is easy to show that $\operatorname{ker}\left(\bar{\square}_{k}\right)=H^{0}\left(M, \lambda \otimes \ell^{\otimes k}\right)$. Using which, and combining it with the spectral expansion of the heat kernel $K_{M, \lambda \otimes \ell^{\otimes k}}(t ; z, w)$ described in equation (26), it is easy to see that
$$\lim _{t \rightarrow \infty} K_{M, \lambda \otimes \ell^{\otimes k}}(t ; z, z)=\mathcal{B}_{M}^{\lambda \otimes \ell^{\otimes k}}(z) .$$
Let
$$c_{1}(\ell)(z):=\frac{i}{2 \pi} \partial \bar{\partial} \phi(z)$$
denote the curvature form of the line bundle $\ell$ at the point $z \in M$. Let $\alpha_{1}, \ldots, \alpha_{n}$ denote the eigenvalues of $\partial \bar{\partial} \phi(z)$ at the point $z \in M$. Then, with notation as above, it follows from Bo96, Th. 1.1] that, for any $z \in M$ and $t \in\left(0, k^{\varepsilon}\right)$, for a given $\varepsilon>0$ not depending on $k$, we have
$$\lim _{k \rightarrow \infty} \frac{1}{k^{n}} K_{M, \lambda \otimes \ell^{\otimes k}}(t ; z, z)=r \cdot \prod_{j=1}^{n} \frac{\alpha_{j}}{(4 \pi)^{n} \sinh \left(\alpha_{j} t\right)},$$
where $r$ denotes the rank of the vector bundle $\lambda$, and the convergence of the above limit is uniform in $z$.

Using equations (28) and (30), in [Bo96, Th. 2.1], Bouche derives the following equality
$$\lim _{k \rightarrow \infty} \frac{1}{k^{n}} \mathcal{B}_{M}^{\lambda \otimes \ell^{\otimes k}}(z)=r \cdot\left|\operatorname{det}_{\omega}\left(c_{1}(\ell)(z)\right)\right|,$$
and the convergence of the above limit is uniform in $z \in M$.
For $n \geq 2$, let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cocompact subgroup. For $k \geq 1$, let $f$ be a Picard modular cusp form of weight- $k$. Then, $f$ is a global section of $\mathcal{L}^{\otimes k}$, where $\mathcal{L}$ is a holomorphic line bundle, whose sections are Picard modular cusp forms of weight-1.

For $k \geq 1$ and $z \in X_{\Gamma}$, from the definition of the Bergman kernel $\mathcal{B}_{X_{\Gamma}}^{\mathcal{L}^{\otimes k}}(z)$ for the line bundle $\mathcal{L}^{\otimes k}$ from equation (27), and from the discussion in Section 2.3, we have
$$\mathcal{B}_{X_{\Gamma}}^{\mathcal{L}^{\otimes k}}(z)=\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} .$$
Furthermore, for any $f \in H^{0}(X, \mathcal{L})$ and $z \in X$, the Hermitian metric $\|\cdot\|_{\mathcal{L}}$ at $z \in X_{\Gamma}$, is given by the following formula
$$\|f\|_{\mathcal{L}}^{2}(z):=\left(1-|z|^{2}\right)|f(z)|^{2} .$$
We now prove Theorem 1.

Theorem 3.1. With notation be as above, for $n \geq 2$, let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cocompact subgroup. Then, for any $z \in X_{\Gamma}$, we have
$$\lim _{k \rightarrow \infty} \frac{1}{k^{n}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=\frac{1}{(4 \pi)^{n}},$$
and the convergence of the above limit is uniform in $z \in X_{\Gamma}$.

Proof. From equation (32), for any $n \geq 2$, and $k \geq 1$, and $z \in X_{\Gamma}$, we have
$$\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=\mathcal{B}_{X_{\Gamma}}^{\mathcal{L}^{\otimes k}}(z) .$$
Applying estimate (31) to the complex manifold $X$ with its natural Hermitian metric $\mu_{\text {hyp }}(z)$, and the line bundle $\mathcal{L}^{\otimes k}$, we deduce that
$$\lim _{k \rightarrow \infty} \frac{1}{k^{n}} \mathcal{B}_{X_{\Gamma}}^{\mathcal{L}^{\otimes k}}(z)=\left|\operatorname{det}_{\mu_{\text {hyp }}^{\text {vol }}}\left(c_{1}(\mathcal{L})(z)\right)\right|,$$
and the convergence of the above limit is uniform in $z \in X$. Now from the definition of the Hermitian metric $\|\cdot\|_{\mathcal{L}}$ on the line bundle $\mathcal{L}$ given by equation (33), and the definition of the curvature-form given by equation (29), and the definition of the hyperbolic metric $\mu_{\mathrm{hyp}}(z)$ given by equation (4), we have
$$c_{1}(\mathcal{L})(z)=-\frac{i}{2 \pi} \partial \bar{\partial} \log \left(1-|z|^{2}\right)=\frac{1}{4 \pi} \mu_{\mathrm{hyp}}(z),$$
which implies that
$$\left|\operatorname{det}_{\mu_{\text {hyp }}^{\text {vol }}}\left(c_{1}(\mathcal{L})(z)\right)\right|=\frac{1}{(4 \pi)^{n}} .$$
Hence, combining equations (35), (36), (37), and (38), we have
$$\lim _{k \rightarrow \infty} \frac{1}{k^{n}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=\frac{1}{(4 \pi)^{n}},$$
and the convergence of the above limit is uniform in $z \in X_{\Gamma}$. This completes the proof of the theorem. \(\square\)

As an immediate consequence of Theorem 3.1, we prove the following Corollary, which can be thought of as an average version of Arithmetic Quantum Unique Ergodicity.

Corollary 3.2. With notation be as above, for $n \geq 2$, let $\Gamma \subset \operatorname{SU}((n, 1), \mathbb{C})$ be a discrete, torsion-free, cocompact subgroup. Then, for any $z \in X_{\Gamma}$, we have
$$\lim _{k \rightarrow \infty} \frac{1}{d_{k}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z)=\mu_{\mathrm{shyp}}^{\mathrm{vol}}(z),$$
and the convergence of the above limit is uniform in $z \in X_{\Gamma}$.

Proof. From equation (34) in Theorem 3.1, for $n \geq 2$, and $z \in X_{\Gamma}$, we have
$$\begin{aligned}
\lim _{k \rightarrow \infty} \frac{1}{d_{k}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z) & =\lim _{k \rightarrow \infty} \frac{k^{n}}{d_{k}} \cdot \lim _{k \rightarrow \infty} \frac{1}{k^{n}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z) \\
& =\lim _{k \rightarrow \infty} \frac{k^{n}}{d_{k}} \cdot \frac{1}{(4 \pi)^{n}} \cdot \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z)
\end{aligned}$$
Observe that
$$d_{k}=\int_{X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}(z) \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z) .$$
As the limit in equation (34) is uniformly convergent, using the above equation, we derive
$$\begin{aligned}
\lim _{k \rightarrow \infty} \frac{d_{k}}{k^{n}} & =\lim _{k \rightarrow \infty} \frac{1}{k^{n}} \int_{X}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z) \\
& =\int_{X_{\Gamma}} \lim _{k \rightarrow \infty} \frac{1}{k^{n}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z) \\
& =\frac{1}{(4 \pi)^{n}} \cdot \operatorname{vol}_{\mathrm{hyp}}(X)
\end{aligned}$$

Combining equations (39) and (40), we compute
$$\begin{aligned}
\lim _{k \rightarrow \infty} \frac{1}{d_{k}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z) & =\lim _{k \rightarrow \infty} \frac{k^{n}}{d_{k}} \cdot \frac{1}{(4 \pi)^{n}} \cdot \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z) \\
& =\frac{1}{\operatorname{vol}_{\mathrm{hyp}}(X)} \mu_{\mathrm{hyp}}^{\mathrm{vol}}(z)=\mu_{\mathrm{shyp}}^{\mathrm{vol}}(x),
\end{aligned}$$
and the convergence of the limit is uniform in $z \in X_{\Gamma}$. This completes the proof of the corollary. \(\square\)

Remark 3.3. From [DLM06, Th. 1.1], it is easy to show that
$$\lim _{k \rightarrow \infty} \frac{1}{d_{k}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}(z) \mu_{\mathrm{hyp}}(z)=\mu_{\mathrm{shyp}}^{\mathrm{vol}}(z)+O_{X}\left(k^{-n}\right),$$
where the implied constant depends only on the Picard modular variety $X$. A careful analysis of the theorem cited above should enable one to prove that the implied constant in equation (41) is independent of $X$.

Remark 3.4. As stated earlier, as in AB18, Theorem 3.1 and Corollary 3.2 easily extend to Bergman kernels associated to vector-valued Picard modular cusp forms. However for brevity of exposition, and for the notation to be in sync with the second theorem, we restrict ourselves to the case of scalar-valued Picard modular cusp forms.

\section*{4. Quantitative estimates of the Bergman kernel in the cocompact setting}

In this section, for $n \geq 2$,, we prove quantitative estimates of the Bergman kernel, when $\Gamma \subset$ $\operatorname{SU}((n, 1), \mathbb{C})$ is a discrete, torsion-free, cocompact subgroup.

With notation as above, for $n \geq 2$, and any $z, w \in X_{\Gamma}$, put
$$\begin{aligned}
\mathcal{S}_{\Gamma}(z, w ; \delta) & :=\left\{\gamma \in \Gamma \mid \mathrm{d}_{\text {hyp }}(z, \gamma w) \leq \delta\right\}, \\
N_{\Gamma}(z, w ; \delta) & :=\operatorname{card} \mathcal{S}_{\Gamma}(z, w ; \delta) .
\end{aligned}$$
Let $\operatorname{vol}(B(z, r))$ denote the volume of a geodesic ball of radius $r$, centred at any $z \in \mathbb{B}^{n}$. Then, from arguments from elementary hyperbolic geometry, we have
$$\operatorname{vol}(B(z, r))=\frac{4 \pi \sinh ^{2 n}(r / 2)}{n!} .$$
In the following lemma, we estimate the counting function $N_{\Gamma}$.

Lemma 4.1. With notation as above, let $z, w \in X_{\Gamma}$. Then, for any $\delta>0$, we have the following estimate
$$N_{\Gamma}(z, w ; \delta) \leq \frac{4 \pi \sinh ^{2 n}\left(\left(2 \delta+r_{X_{\Gamma}}\right) / 4\right)}{n!\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)} ;$$
let $f(\rho)$ be any positive, smooth, monotonically decreasing function defined on $\mathbb{R}_{>0}$. Then, for any $\delta>r_{X_{\Gamma}} / 2$, assuming that all the involved integrals exist, we have the following inequality
$$\begin{gathered}
\int_{0}^{\infty} f(\rho) d N_{\Gamma}(z, w ; \rho) \leq \int_{0}^{\delta} f(\rho) d N_{\Gamma}(z, w ; \rho)+f(\delta) \frac{4 \pi \sinh ^{2 n}\left(\left(2 \delta+r_{X_{\Gamma}}\right) / 4\right)}{n!\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)}+ \\
\frac{4 \pi}{(n-1)!\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)} \int_{\delta}^{\infty} f(\rho) \sinh ^{2 n-1}\left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right) \cosh \left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right) d \rho,
\end{gathered}$$
where $c_{n}$ is as defined in equation (43).

Proof. The main idea of the proof is the same as in Lemma 4 in [JL95]. We estimate $N_{\Gamma}(z, w ; \rho)$ by the number of disjoint balls of radius $r_{X_{\Gamma}} / 2$, which can be embedded in a ball of radius $\rho+r_{X_{\Gamma}} / 2$. Observe that our definition of injectivity radius $r_{X_{\Gamma}}$ is two times the definition employed in [JL95], and our estimates take that into account.

Inequality (44) follows directly from equation (43).
From similar arguments, it is easy to see that for any $\rho \geq \delta>r_{X_{\Gamma}} / 2$, we find
$$N_{\Gamma}(z, w ; \rho) \leq N_{\Gamma}(z, w ; \delta)+\frac{\sinh ^{2 n}\left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right)-\sinh ^{2 n}\left(\left(2 \delta-r_{X_{\Gamma}}\right) / 4\right)}{\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)} .$$
Then, inequality (45) follows from similar arguments as in Lemma 4 in [JL95]. \(\square\)

Using the above estimate for the counting function $N_{\Gamma}$, we now estimate the Bergman kernel.

Theorem 4.2. With notation as above, and for $n \geq 2$, and $k \geq 2 n+2$, we have the following estimate
$$\begin{aligned}
& \sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \leq \\
& C_{\Gamma, k}+\frac{\left.C_{\Gamma, k} \cosh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)\right)}{(k-2 n-1) \sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)}+\frac{C_{\Gamma, k} \sinh ^{2 n}\left(5 r_{X_{\Gamma}} / 8\right)}{\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right) \cosh ^{k}\left(3 r_{X_{\Gamma}} / 8\right)},
\end{aligned}$$
where $r_{X_{\Gamma}}$ is the injectivity radius of $X_{\Gamma}$, which is as defined in equation (15), and $C_{\Gamma, k}$ is as described in equation (20).

Proof. For $n \geq 2$, and $k \geq 2 n+2$, and any $z \in X_{\Gamma}$, from inequality (23) we have
$$\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \leq \sum_{\gamma \in \Gamma} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)} .$$
Now, as $\cosh ^{k}(\rho / 2)$ is a positive, smooth, monotonically decreasing function on $\mathbb{R}_{>0}$, substituting $\delta=3 r_{X_{\Gamma}}$ /4 in estimates (44) and (45) from Lemma 4.1, we compute
$$\begin{array}{r}
\sum_{\gamma \in \Gamma} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)}=\int_{0}^{\infty} \frac{C_{\Gamma, k} d N_{\Gamma}(z, \gamma z ; \rho)}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)} \leq \\
\int_{0}^{\frac{3 r_{X_{\Gamma}}}{4}} \frac{C_{\Gamma, k} d N_{\Gamma}(z, \gamma z ; \rho)}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)}+\frac{c_{n} C_{\Gamma, k} \sinh ^{2 n}\left(5 r_{X_{\Gamma}} / 8\right)}{\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right) \cosh ^{k}\left(3 r_{X_{\Gamma}} / 8\right)}+ \\
\frac{n c_{n} C_{\Gamma, k}}{\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)} \int_{\frac{3 r_{X_{\Gamma}}}{4}}^{\infty} \frac{\sinh ^{2 n-1}\left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right) \cosh \left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right)}{\cosh ^{k}(\rho / 2)} d \rho .
\end{array}$$
We now estimate the first term on the right hand-side of the above inequality. From the definition of injectivity radius $r_{X_{\Gamma}}$ in (15), we have the following estimate for the first term on the right hand-side of inequality (48)
$$\int_{0}^{\frac{3 r_{X_{\Gamma}}}{4}} \frac{C_{\Gamma, k} d N_{\Gamma}(z, \gamma z ; \rho)}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)}=C_{\Gamma, k}$$
Observe that for any $\rho \geq 0$, we have
$$\begin{array}{r}
\cosh \left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right) \leq 2 \cosh \left(r_{X_{\Gamma}} / 4\right) \cosh (\rho / 2), \\
\sinh ^{2 n-1}\left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right) \leq \sinh (\rho) \leq\left(2 \cosh \left(r_{X_{\Gamma}} / 4\right) \cosh (\rho / 2)\right)^{2 n-1}= \\
2^{2 n-1} \cosh ^{2 n-1}\left(r_{X_{\Gamma}} / 4\right) \cosh ^{2 n-1}(\rho / 2) .
\end{array}$$

Using the above two inequalities, for $k \geq 2 n+2$, we have the following estimate for the third term on the right hand-side of inequality (48)
$$\begin{array}{r}
\frac{n c_{n} C_{\Gamma, k}}{\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)} \int_{\frac{3 r_{X_{\Gamma}}}{4}}^{\infty} \frac{\sinh ^{2 n-1}\left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right) \cosh \left(\left(2 \rho+r_{X_{\Gamma}}\right) / 4\right)}{\cosh ^{k}(\rho / 2)} d \rho \leq \\
\frac{2^{2 n} n c_{n} C_{\Gamma, k} \cosh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)}{\sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)} \int_{\frac{3 r_{X_{\Gamma}}}{4}}^{\infty} \frac{d \rho}{\cosh ^{k-2 n}(\rho / 2)} \leq \frac{\left.2^{2 n} n c C_{\Gamma, k} \cosh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)\right)}{(k-2 n-1) \sinh ^{2 n}\left(r_{X_{\Gamma}} / 4\right)},
\end{array}$$
where $c$ is a universal constant.
The proof of estimate (46) follows form combining inequalities (47)-(50), and absorbing all the constants depending upon $n$ into $C_{\Gamma, k}$. \(\square\)

Corollary 4.3. With notation as above, for $n \geq 2$ and $k \geq 2 n+1$, we have the following estimate
$$\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}}=O_{\Gamma}\left(k^{n}\right) .$$

Proof. The proof of the corollary follows directly from combining Theorem 4.2 and (21). \(\square\)

Remark 4.4. From asymptotic estimate (34), we can conclude that estimate (51) is optimally derived.

\section*{5. Quantitative estimates of the Bergman kernel in the cofinite setting}

For the rest of the article, $\Gamma \subset \operatorname{SU}\left((2,1), \mathcal{O}_{K}\right)$ denotes a torsion-free, finite index subgroup with only one cusp at $\infty$, where $K$ is a totally imaginary number field. We recall from subsection 2.2, the complex hyperbolic 2-space $\mathcal{H}^{2}(\mathbb{C})$ can be identified with
$$\mathbb{B}^{2}:=\left\{z=\left.\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}| | z_{1}\right|^{2}+\left|z_{2}\right|^{2}<1\right\} .$$
As discussed in Sections 2.1 and 2.2, the resulting quotient space $X_{\Gamma}:=\Gamma \backslash \mathbb{B}^{2}$ is a noncompact complex manifold of dimension 2, of finite hyperbolic volume, and with one cusp.

In this section, we prove the quantitative estimates of the Bergman kernel associated to Picard modular cusp forms of weight- $k$, with respect to $\Gamma$. For this, we go back and forth between the three models of the complex hyperbolic 2-space $\mathcal{H}^{2}(\mathbb{C})$, which are as discussed in Section 2.2.

In the following lemma, we determine the points, where the Bergman kernel attains its maxima.

Lemma 5.1. With notation as above, for any $k \geq 1$ and $z \in \mathbb{B}_{3}^{2}$, the Petersson norm of the Bergman kernel $\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\text {pet }}$ attains its maximum value on
$$\mathcal{S}:=\left\{z \in \mathbb{B}_{3}^{2} \left\lvert\, \operatorname{Re}\left(z_{1}\right)=-\frac{k}{4 \pi}\right., z_{2}=0\right\} .$$
Proof. From Section 2.2, recall that $\mathbb{B}_{3}^{2}$, Model (2) of the hyperbolic 2-space $\mathcal{H}^{2}(\mathbb{C})$ is given by the following equation
$$\mathbb{B}_{3}^{2}:=\left\{z=\left(z_{1}, z_{2}\right)^{t} \in \mathbb{C}^{2}\left|2 \operatorname{Re}\left(z_{1}\right)+\left|z_{2}\right|^{2}<0\right\} .\right.$$
From the definition of the Petersson norm for a Picard modular cusp form from equation (25), we have
$$|f(z)|_{\text {pet }}^{2}=\left(-2 \operatorname{Re}\left(z_{1}\right)-\left|z_{2}\right|^{2}\right)^{k}|f(z)|^{2}=\left(-2 \operatorname{Re}\left(z_{1}\right)-\left|z_{2}\right|^{2}\right)^{k} \cdot\left|\frac{f(z)}{e^{2 \pi \operatorname{Re}\left(z_{1}\right)}}\right|^{2} \cdot e^{4 \pi \operatorname{Re}\left(z_{1}\right)} .$$

The first term of the expression is subharmonic, and bounded in any open region of $\mathbb{B}_{3}^{2}$, and will attain its maximum at the boundary of the region.

We now compute the region where the following function
$$P(z)=\left(-2 \operatorname{Re}\left(z_{1}\right)-\left|z_{2}\right|^{2}\right)^{k} \cdot e^{4 \pi \operatorname{Re}\left(z_{1}\right)}$$
attains its maximum.
For $z=\left(z_{1}=x_{1}+i y_{1}, z_{2}=x_{2}+i y_{2}\right)^{t} \in \mathbb{B}_{3}^{2}$, we have
$$P(z)=\left(-2 x_{1}-x_{2}^{2}-y_{2}^{2}\right)^{k} e^{4 \pi x_{1}}$$
Now we look at the partial derivative of $P$ with respect to $x_{1}, x_{2}, y_{1}, y_{2}$.
$$\begin{aligned}
& \frac{\partial P(z)}{\partial x_{1}}=\left(-2 x_{1}-x_{2}^{2}-y_{2}^{2}\right)^{k-1}\left(-2 k-4 \pi\left(2 x_{1}+x_{2}^{2}+y_{2}^{2}\right)\right) e^{4 \pi x_{1}} ; \quad \frac{\partial P(z)}{\partial y_{1}}=0 ; \\
& \frac{\partial P(z)}{\partial x_{2}}=-2 k x_{2}\left(-2 x_{1}-x_{2}^{2}-y_{2}^{2}\right)^{k-1} e^{4 \pi x_{1}} ; \quad \frac{\partial P(z)}{\partial y_{2}}=-2 k y_{2}\left(-2 x_{1}-x_{2}^{2}-y_{2}^{2}\right)^{k-1} e^{4 \pi x_{1}} .
\end{aligned}$$
Now equating the above quantities to zero, we obtain the points of extrema as
$$\tilde{z_{2}}=0, \operatorname{Re}\left(\tilde{z_{1}}\right)=-\frac{k}{4 \pi} .$$
Further investigation show that the obtained points are indeed points of maxima, which completes the proof of the lemma. \(\square\)

Using lemma 5.1, we estimate the Petersson norm of the Bergman kernel in the following theorem.

Theorem 5.2. With notation as above, for any $k \geq 6$, we have the following estimate
$$\begin{array}{r}
\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\text {pet }} \leq C_{\Gamma, k}+\frac{\left.C_{\Gamma, k} \cosh ^{4}\left(r_{X_{\Gamma}} / 4\right)\right)}{(k-5) \sinh ^{4}\left(r_{X_{\Gamma}} / 4\right)}+\frac{C_{\Gamma, k} \sinh ^{4}\left(5 r_{X_{\Gamma}} / 8\right)}{\sinh ^{4}\left(r_{X_{\Gamma}} / 4\right) \cosh ^{k}\left(3 r_{X_{\Gamma}} / 8\right)}+ \\
\frac{\sqrt{\pi} \Gamma(k / 2-1) \Gamma(k-3 / 2)}{\Gamma(k / 2) \Gamma(k-1)} C_{\Gamma, k} k^{3 / 2} .
\end{array}$$
where $r_{X_{\Gamma}}$ is the injectivity radius of $X$, which is as defined in equation (16), and $C_{\Gamma, k}$ is a constant satisfies the following estimate
$$C_{\Gamma, k}=O_{\Gamma}\left(k^{2}\right) .$$

Proof. With notation as above, using inequality (23), we derive
$$\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\mathrm{pet}} \leq \sup _{z \in \mathbb{B}^{2}} \sum_{\gamma \in \Gamma \backslash \Gamma_{\infty}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)}+\sup _{z \in \mathbb{B}^{2}} \sum_{\gamma \in \Gamma_{\infty}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)} .$$
Employing similar arguments as the ones used to prove estimate (4.2), we have the following estimate for the first term of the right-hand side of the above inequality
$$\begin{aligned}
& \sup _{z \in \mathbb{B}^{2}} \sum_{\gamma \in \Gamma \backslash \Gamma_{\infty}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)} \leq \\
& C_{\Gamma, k}+\frac{\left.C_{\Gamma, k} \cosh ^{4}\left(r_{X_{\Gamma}} / 4\right)\right)}{(k-5) \sinh ^{4}\left(r_{X_{\Gamma}} / 4\right)}+\frac{C_{\Gamma, k} \sinh ^{4}\left(5 r_{X_{\Gamma}} / 8\right)}{\sinh ^{4}\left(r_{X_{\Gamma}} / 4\right) \cosh ^{k}\left(3 r_{X_{\Gamma}} / 8\right)},
\end{aligned}$$
where $r_{X_{\Gamma}}$, the injectivity radius of $X$, is as defined in equation (16), and the constant $C_{\Gamma, k}$ satisfies estimate (55).

We now estimate the second term on the right-hand side of inequality (56). From Lemma 5.1, and using the fact that $\Gamma_{\infty}^{3} \subset \Gamma_{0, \infty}^{3}$, we make the following inference
$$\begin{array}{r}
\sup _{z \in \mathbb{B}^{2}} \sum_{\gamma \in \Gamma_{\infty}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)}=\sup _{z \in \mathbb{B}_{3}^{2}} \sum_{\gamma \in \Gamma_{\infty}^{3}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)}= \\
\sup _{z \in \mathcal{S}} \sum_{\gamma \in \Gamma_{\infty}^{3}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)} \leq \sup _{z \in \mathcal{S}} \sum_{\gamma \in \Gamma_{0, \infty}^{3}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)},
\end{array}$$
where $\Gamma_{\infty}^{3}, \Gamma_{0, \infty}^{3}$ are as defined in equations (12), (14), respectively, and $\mathcal{S}$ is as described in equation (52).

For any $z \in \mathbb{B}_{3}^{2}$ with lift $\tilde{z} \in \mathcal{A}^{3}$, using relation (24), we have
$$\sum_{\gamma \in \Gamma_{0, \infty}^{3}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)}=\sum_{\gamma \in \Gamma_{0, \infty}^{3}} C_{\Gamma, k} \frac{\langle\tilde{z}, \tilde{z}\rangle_{3}^{k / 2}\langle\gamma \tilde{z}, \gamma \tilde{z}\rangle_{3}^{k / 2}}{\langle\tilde{z}, \gamma \tilde{z}\rangle_{3}^{k / 2}\langle\gamma \tilde{z}, \tilde{z}\rangle_{3}^{k / 2}},$$
where the inner-product $\langle\cdot, \cdot\rangle_{3}$ is as described in equation (8).
For any $\gamma \in \Gamma_{0, \infty}^{3}$ and $z=\left(z_{1}, z_{2}\right)^{t} \in \mathbb{B}_{3}^{2}$ with lift $\tilde{z} \in \mathcal{A}^{3}$, and $\gamma \in \Gamma_{0, \infty}$, we compute
$$\begin{aligned}
& \langle\tilde{z}, \tilde{z}\rangle_{3}=\langle\gamma \tilde{z}, \gamma \tilde{z}\rangle_{3}=2 \operatorname{Re}\left(z_{1}\right)+\left|z_{2}\right|^{2} ; \\
& \langle\gamma \tilde{z}, \tilde{z}\rangle_{3}=2 \operatorname{Re}\left(z_{1}\right)+\left|z_{2}\right|^{2}+\alpha \bar{z}_{2}-\bar{\alpha} z_{2}-\frac{|\alpha|^{2}}{2}+i \beta ; \\
& \langle\tilde{z}, \gamma \tilde{z}\rangle_{3}=2 \operatorname{Re}\left(z_{1}\right)+\left|z_{2}\right|^{2}-\alpha \bar{z}_{2}+\bar{\alpha} z_{2}-\frac{|\alpha|^{2}}{2}-i \beta .
\end{aligned}$$
where $\alpha \in \mathbb{C}$ and $\beta \in \mathbb{R}$.
Using the above equations, for any $z \in \mathcal{S}$ with lift $\tilde{z} \in \mathcal{A}^{3}$, and $\gamma \in \Gamma_{0, \infty}$, we compute
$$\langle\tilde{z}, \tilde{z}\rangle_{3}=\langle\gamma \tilde{z}, \gamma \tilde{z}\rangle_{3}=-\frac{k}{2 \pi} ; \quad\langle\gamma \tilde{z}, \tilde{z}\rangle_{3}=-\frac{k}{2 \pi}-\frac{|\alpha|^{2}}{2}+i \beta ; \quad\langle\tilde{z}, \gamma \tilde{z}\rangle_{3}=-\frac{k}{2 \pi}-\frac{|\alpha|^{2}}{2}-i \beta .$$
where $\alpha \in \mathbb{C}$ and $\beta \in \mathbb{R}$.
Put
$$\mathrm{L}=\left\{(\alpha, \beta) \in \mathbb{C} \times \mathbb{R} \left\lvert\, \gamma=\left(\begin{array}{ccc}
1 & -\bar{\alpha} & -\frac{|\alpha|^{2}}{2}+i \beta \\
0 & 1 & \alpha \\
0 & 0 & 1
\end{array}\right) \in \Gamma_{(0, \infty)}^{3}\right.\right\},$$
which defines a discrete lattice in $\mathbb{C} \times \mathbb{R}$.
Combining equations (59)-(61), for any $z \in \mathcal{S}$, we derive
$$\sum_{\gamma \in \Gamma_{0, \infty}^{3}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(\tilde{z}, \gamma \tilde{z}) / 2\right)}=\sum_{(\alpha, \beta) \in \mathrm{L}} \frac{C_{\Gamma, k}(k / 2 \pi)^{k}}{\left|k / 2 \pi+|\alpha|^{2} / 2+i \beta\right|^{k}} .$$
Approximating the above summation over the discrete lattice L by integrals, we compute
$$\begin{aligned}
& \sum_{(\alpha, \beta) \in \mathrm{L}} \frac{C_{\Gamma, k}(k / 2 \pi)^{k}}{\left|k / 2 \pi+|\alpha|^{2} / 2+i \beta\right|^{k}} \leq \\
& \int_{-\infty}^{\infty} \int_{0}^{\infty} \int_{0}^{2 \pi} \frac{C_{\Gamma, k}(k / 2 \pi)^{k} d \beta d r d \theta}{\left(\left(k / 2 \pi+r^{2} / 2\right)^{2}+\beta^{2}\right)^{k / 2}}=\int_{0}^{\infty} \int_{-\infty}^{\infty} \frac{2 \pi C_{\Gamma, k}(k / 2 \pi)^{k} d r d \beta}{\left(\left(k / 2 \pi+r^{2} / 2\right)^{2}+\beta^{2}\right)^{k / 2}}
\end{aligned}$$
where $\alpha=r e^{i \theta}$.

Now we estimate the integral
$$\int_{0}^{\infty} \int_{-\infty}^{\infty} \frac{d r d \beta}{\left(\left(k / 2 \pi+r^{2} / 2\right)^{2}+\beta^{2}\right)^{k / 2}}$$
Substituting
$$\eta=\beta /\left(k / 2 \pi+r^{2} / 2\right),$$
and using formula 3.251.2 from [GR81] in the above integral, we compute
$$\int_{0}^{\infty} \int_{-\infty}^{\infty} \frac{d r d \beta}{\left(\left(k / 2 \pi+r^{2} / 2\right)^{2}+\beta^{2}\right)^{k / 2}}=\frac{\sqrt{\pi} \Gamma(k / 2-1 / 2)}{\Gamma(k / 2)} \int_{0}^{\infty} \frac{d r}{\left(k / 2 \pi+r^{2} / 2\right)^{k-1}} .$$
Substituting $\omega=r \sqrt{\pi / k}$, and applying formula 3.251.2 from [GR81] in the above integral, we now compute
$$\int_{0}^{\infty} \frac{d r}{\left(k / 2 \pi+r^{2} / 2\right)^{k-1}}=\sqrt{2}\left(\frac{2 \pi}{k}\right)^{k-3 / 2} \int_{0}^{\infty} \frac{d \omega}{\left(1+\omega^{2}\right)^{k-1}}=\frac{(2 \pi)^{k-1} \Gamma(k-3 / 2)}{k^{k-3 / 2} \Gamma(k-1)}$$
For $k \geq 6$, combining equation (58) with computations (62)-(65), we arrive at the following inequality
$$\sup _{z \in \mathbb{B}^{2}} \sum_{\gamma \in \Gamma_{\infty}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\mathrm{hyp}}(z, \gamma z) / 2\right)} \leq \frac{\sqrt{\pi} \Gamma(k / 2-1) \Gamma(k-3 / 2)}{\Gamma(k / 2) \Gamma(k-1)} C_{\Gamma, k} k^{3 / 2} .$$
Combining inequalities (56), (57), and (66) completes the proof of the theorem. \(\square\)

Using Theorem 5.2, we now prove Theorem 3, in the following corollary.

Corollary 5.3. We notation as above, we have the following estimate
$$\sup _{z \in X_{\Gamma}}\left|\mathcal{B}_{\Gamma}^{k}(z)\right|_{\text {pet }}=O_{\Gamma}\left(k^{5 / 2}\right) .$$
Proof. For $k \geq 6$, we have the following estimates for the Gamma function
$$\frac{\Gamma(k / 2-1 / 2)}{\Gamma(k / 2)}=O\left(\frac{1}{\sqrt{k}}\right), \quad \frac{\Gamma(k-3 / 2)}{\Gamma(k-1)}=O\left(\frac{1}{\sqrt{k}}\right) .$$
The proof of the corollary follows from combining the above estimate with inequality (54) and estimate (55). \(\square\)

Remark 5.4. The implied constants in estimates (1) and (2) remain stable in covers. Let $\left.\Gamma_{0} \subset \operatorname{SU}(n, 1), \mathbb{C}\right)$ be a discrete, torsion-free, cocompact subgroup, and let $\Gamma_{1} \subset \Gamma_{0}$ be a finite index subgroup. Let $X_{\Gamma_{1}}: \Gamma_{1} \backslash \mathbb{B}^{n}, X_{\Gamma_{0}} \backslash \mathbb{B}^{n}$ denote the respective quotient spaces. Then, from the proof of estimate (1) from Theorem 4.2, for any $z \in \mathbb{B}^{n}$, we have the following inequality
$$\left|\mathcal{B}_{\Gamma_{1}}^{k}(z)\right|_{\text {pet }} \leq \sum_{\gamma \in \Gamma_{1}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\text {hyp }}(z, \gamma z) / 2\right)} \leq \sum_{\gamma \in \Gamma_{0}} \frac{C_{\Gamma, k}}{\cosh ^{k}\left(\mathrm{~d}_{\text {hyp }}(z, \gamma z) / 2\right)}=O_{\Gamma_{0}}\left(k^{n}\right) .$$
Similarly, from the proofs of Theorem 5.2 and Corollary 5.3, we can conclude that the implied constant in estimate (2) also remains stable in covers of ball qoutients.

Acknowledgements. The first and third authors acknowledge the support of INSPIRE research grant DST/INSPIRE/04/2015/002263 and the MATRICS grant MTR/2018/000636. The second author was partially supported by SERB grants EMR/2016/000840 and MTR/2017/000114.

The first author is very thankful to Dr. Soumya Das, Prof. Jürg Kramer, and Dr. Antareep Mandal for helpful discussions on estimates of automorphic forms.

\section*{References}
\begin{itemize}
\item[] [AU95] A. Abbes and E. Ullmo, Comparaison des métriques d'Arakelov et de Poincaré sur $X_{0}(N)$, Duke Math. J. 80, 295-307, 1995.
\item[] [Ar16] A. Aryasomayajula, Heat kernel approach for sup-norm bounds for cusp forms of integral and half-integral weight, Arch. Math. 106, 165-173, 2016.
\item[] [AB22] A. Aryasomayajula and B. Balasubramanyam, Estimates of cusp forms for certain co-compact arithmetic subgroups, Proc. Amer. Math. Soc. 150, 4191-4201, 2022.
\item[] [AB18] A. Aryasomayajula and B. Balasubramanyam, Estimates of automorphic cusp forms over quaternion algebras, Int. J. Number Theory 14, 1143-1170, 2018.
\item[] [AM20] A. Aryasomayajula and P. Majumder, Estimates of the Bergman kernel on a hyperbolic Riemann surface of finite volume-II, Ann. Fac. Sci. Toulouse Math. 29, 795-804, 2020.
\item[] [AM18] A. Aryasomayajula and P. Majumder, Off-diagonal estimates of the Bergman kernel on hyperbolic Riemann surfaces of finite volume, Proc. Amer. Math. Soc. 146, 4009-4020, 2018.
\item[] [Bo96] T. Bouche, Asymptotic results for Hermitian line bundles over complex manifolds: the heat kernel approach, Higher-dimensional complex varieties, de Gruyter, Berlin (1996), 67-81.
\item[] [DLM06] X. Dai, K. Liu, and X. Ma, On the asymptotic expansion of Bergman kernel, J. Differential Geom., 72, 1-41, 2006.
\item[] [FJK16] J. S. Friedman, J. Jorgenson and J. Kramer, Uniform sup-norm bounds on average for cusp forms of higher weights, Arbeitstagung Bonn 2013, Progress Mathematics 319 (Birkhäuser/Springer, Cham, 2016), 127-154.
\item[] [GR81] I. Gradshteyn and I. Ryzhik, Tables of Integrals, Series, and Products, Academic Press, 1981.
\item[] [Ho98] R.-P. Holzapfel, Zeta dimension formula for Picard modular cusp forms of neat natural congruence subgroups, Abh. Math. Sem. Univ. Hamburg 68, 169-192, 1998.
\item[] [JL95] J. Jorgenson and R. Lundelius, Convergence of the heat kernel and the resolvent kernel on degenerating hyperbolic Riemann surfaces of finite volume, Questiones Math 18, 345-363, 1995.
\item[] [Ma22] A. Mandal, Uniform sup-norm bounds for Siegel cusp forms, Ph.D. Thesis, Humboldt-Universität zu Berlin, Institut für Mathematik, 2022.
\end{itemize}

Department of Mathematics, Indian Institute of Science Education and Research (IISER) Tirupati, Transit campus at Sri Rama Engineering College, Karkambadi Road, Mangalam (B.O),Tirupati-517507, India.

Email address: anil.arya@iisertirupati.ac.in

Department of Mathematics, Indian Institute of Science Education and Research (IISER) Pune, Dr. Homi Bhabha Road, Pashan, Pune 411008, India.

Email address: baskar@iiserpune.ac.in

Department of Mathematics, Indian Institute of Science Education and Research (IISER) Tirupati, Transit campus at Sri Rama Engineering College, Karkambadi Road, Mangalam (B.O),Tirupati-517507, India.

Email address: dyutiroy@students.iisertirupati.ac.in