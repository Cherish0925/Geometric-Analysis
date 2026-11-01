---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1006_3331.pdf
converter: mathpix
format: mmd
---

\title{
GENERATORS FOR THE EUCLIDEAN PICARD MODULAR GROUPS
}

\author{
TIEHONG ZHAO
}

\begin{abstract}
The goal of this article is to show that five explicitly given transformations, a rotation, two screw Heisenberg rotations, a vertical translation and an involution generate the Euclidean Picard modular groups with coefficient in the Euclidean ring of integers of a quadratic imaginary number field. We also obtain the relations of the isotropy subgroup by analysis of the combinatorics of the fundamental domain in Heisenberg group.
\end{abstract}

\section*{1. Introduction}

Let $\mathcal{K}=\mathbb{Q}(\sqrt{-d})$ be a quadratic imaginary number field. Let $\mathcal{O}_{d}$ be the ring of algebraic integers of $\mathcal{K}$. The Bianchi groups $P S L_{2}\left(\mathcal{O}_{d}\right)$ are the simplest numerically defined discrete groups. In number theory they have been used to study the zeta-functions of binary Hermitian forms over the rings $\mathcal{O}_{d}$. As the isometric groups acting on the half-upper space, they are of interest in the theory of Fuchsian groups and the related theory of Riemann surfaces. The Bianchi groups can be considered as the natural algebraic generalization of the classical modular group $P S L_{2}(\mathbb{Z})$. A good general reference for the Bianchi groups and their relation to the modular group is [3]. As a natural generalization of the Bianchi groups, the subgroups of $\operatorname{PU}(2,1)$ with coefficients in $\mathcal{O}_{d}$ are called Picard modular groups, denoted by $P U\left(2,1 ; \mathcal{O}_{d}\right)$. These groups have attracted a great deal of attention both for their intrinsic interest as discrete groups and also for their applications in complex hyperbolic geometry (as the holomorphic automorphism subgroups).

A general method to determine finite presentations for each Bianchi group $P S L_{2}\left(\mathcal{O}_{d}\right)$ was developed by Swan [17] based on geometrical work of Bianchi, while a separate purely algebraic method was given by Cohn [1]. In general, fundamental domains for Lie groups were studied by [11], but the complex hyperbolic space is a particularly challenging case since no existence of totally geodesic hypersurface. So far very few examples of complex hyperbolic lattices have been constructed explicitly. Due to the famous paper [12] of Mostow, other explicit constructions of fundamental domains for lattices in $\operatorname{PU}(2,1)$ were obtained, see for example, the work of Goldman and Parker

\footnotetext{
The author is supported by the China-funded Postgraduates Studying Aboard Program for Building Top University.
}
[10], Deraux, Falbel and Paupert [2], Schwartz [15], the survey paper of Parker [13]. In particular, the group $P U\left(2,1 ; \mathcal{O}_{3}\right)=P U(2,1 ; \mathbb{Z}[\omega])$, where $\omega$ is a cube root of unity was studied by Falbel and Parker in [5] and its sister was treated recently in [19]. Analogously a fundamental domain of Gauss-Picard group $P U(2,1 ; \mathbb{Z}[i])$ was described in ([6], [7], [8]) and analysis of the combinatorics of the fundamental domain gives rise to a presentation of the group in [6].

In this paper we give a description of generators for certain Picard modular groups $P U\left(2,1 ; \mathcal{O}_{d}\right)$ where the ring $\mathcal{O}_{d}$ is Euclidean except for $d=1,3$ (these two exceptional cases have been studied in many aspects). Among the quadratic imaginary number rings $\mathcal{O}_{d}$ only $\mathcal{O}_{1}, \mathcal{O}_{2}, \mathcal{O}_{3}, \mathcal{O}_{7}, \mathcal{O}_{11}$ have a Euclidean algorithm, see [16], although there is a larger finite collection of $\mathcal{O}_{d}$ 's (such as $d=1,2,3,7,11,19,43,67,163$, see [18]) which have class number one. For these values of $d$ the orbifold $\mathbf{H}_{\mathbb{C}}^{2} / P U\left(2,1 ; \mathcal{O}_{d}\right)$ has only one cusp. The method is based on the construction of various shapes of precisely fundamental domains for the stabilisers of infinity of $P U\left(2,1 ; \mathcal{O}_{d}\right)$ and then on a determination of several neighboring isometric spheres such that the union of the boundaries of these isometric spheres contains the fundamental domain of the stabiliser, which was used in ([5], [6], [19]). Compared with other groups, the generators of these groups in ([5], [6], [19]) are easy to be obtained since the fundamental domain constructed lies completely inside the boundary of the isometric sphere centred at origin. Again this reflects the underlying number theory; $\mathcal{O}_{1}$ and $\mathcal{O}_{3}$ have non-trivial units while the other three do not. A simple algorithm to decompose any transformation in the Picard group $P U\left(2,1 ; \mathcal{O}_{1}\right)$ as a product of the generators was given in [4], one would be interesting to extend their method to other Picard modular groups. However, it would also be important to find the generators in terms of geometric ways which will provide more informations that one continue to construct a fundamental domain explicitly for each of Picard modular groups.

I would like to thank my advisor E. Falbel for his warm encouragements all along this work and for a number of helpful comments.

\section*{2. Complex hyperbolic space}
2.1. The Siegel domain. In this section we give the necessary background material on complex hyperbolic space. To know more details of this material we refer the reader to [9].

Let $\mathbb{C}^{2,1}$ denote the complex vector space equipped with the Hermitian form defined by
$$\langle\mathbf{z}, \mathbf{w}\rangle=z_{1} \bar{w}_{3}+z_{2} \bar{w}_{2}+z_{3} \bar{w}_{1},$$
where z and w be the column vectors $\left[z_{1}, z_{2}, z_{3}\right]^{t}$ and $\left[w_{1}, w_{2}, w_{3}\right]^{t}$ respectively. The projective model of complex hyperbolic space $\mathbf{H}_{\mathbb{C}}^{2}$ is defined to be the collection of negative lines in $\mathbb{C}^{2,1}$, namely, those points z satisfying $\langle\mathbf{z}, \mathbf{z}\rangle<0$.

We mainly take the Siegel domain $\mathfrak{S}$ as a upper half-space model for the complex hyperbolic space, that is given by
$$\mathfrak{S}=\left\{\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}: 2 \Re e z_{1}+\left|z_{2}\right|^{2}<0\right\} .$$
The boundary of the Siegel domain $\mathfrak{S}$ is identified with the one-point compactification of the Heisenberg group. The Heisenberg group $\Re$ is $\mathbb{C} \times \mathbb{R}$ with the group law
$$\left(\zeta_{1}, t_{1}\right) \diamond\left(\zeta_{2}, t_{2}\right)=\left(\zeta_{1}+\zeta_{2}, t_{1}+t_{2}+2 \Im m\left(\zeta_{1} \bar{\zeta}_{2}\right)\right) .$$
The Cygan metric on $\Re$ is given by
$$\rho_{0}\left(\left(\zeta_{1}, t_{1}\right),\left(\zeta_{2}, t_{2}\right)\right)=\left|\left|\zeta_{1}-\zeta_{2}\right|^{2}-i t_{1}+i t_{2}-2 i \Im m\left(\zeta_{1} \bar{\zeta}_{2}\right)\right|,$$
in terms of the operation of Heisenberg group, that is $\left|\left(\zeta_{1}, t_{1}\right)^{-1} \diamond\left(\zeta_{2}, t_{2}\right)\right|$.
We can extend the Cygan metric to an incomplete metric on $\overline{\mathfrak{S}}-\{\infty\}$ as follows
$$\tilde{\rho}_{0}=\left|\left|\zeta_{1}-\zeta_{2}\right|^{2}+\left|u_{1}-u_{2}\right|-i t_{1}+i t_{2}-2 i \Im m\left(\zeta_{1} \bar{\zeta}_{2}\right)\right| .$$

The Siegel domain $\mathfrak{S}$ is parametrised in horospherical coordinates by
$$(\zeta, t, u) \longrightarrow\left[\begin{array}{c}
\left(-|\zeta|^{2}-u+i t\right) / 2 \\
\zeta \\
1
\end{array}\right]$$
and the point at infinity being
$$q_{\infty}=\left[\begin{array}{l}
1 \\
0 \\
0
\end{array}\right] .$$
Then $\mathfrak{S}=\Re \times \mathbb{R}_{+}$and $\partial \mathfrak{S}=(\Re \times\{0\}) \cup\left\{q_{\infty}\right\}$.
2.2. Complex hyperbolic isometries. Let $U(2,1)$ be the group of matrices that are unitary with respect to the form $\langle.,$.$\rangle . The group of holomor-$ phic isometries of complex hyperbolic space is the projective unitary group $P U(2,1)=U(2,1) / U(1)$, with a natural identification $U(1)=\left\{e^{i \theta} I, \theta \in\right.$ $[0,2 \pi)\}$. We now describe the action of the stabiliser of $q_{\infty}$ on the Heisenberg group.

The Heisenberg group acts on itself by Heisenberg translations. For $(\tau, v) \in \Re$, this is
$$T_{(\tau, v)}:(\zeta, t) \mapsto(\zeta+\tau, t+v+2 \Im m(\tau \bar{\zeta}))=(\tau, v) \diamond(\zeta, t) .$$
Heisenberg translation by $(0, v)$ for any $v \in \mathbb{R}$ is called vertical translation by $v$.

The unitary group $U(1)$ acts on the Heisenberg group by Heisenberg rotations. For $e^{i \theta} \in U(1)$, the rotation fixing $q_{0}=(0,0,0)$ is given by
$$R_{\theta}:(\zeta, t) \mapsto\left(e^{i \theta} \zeta, t\right) .$$
All other Heisenberg rotations may be obtained from these by conjugating by a Heisenberg translation.

For $\lambda \in \mathbb{R}_{+}$, Heisenberg dilation by $\lambda$ fixing $q_{\infty}$ and $q_{0}=(0,0,0) \in \partial \mathbf{H}_{\mathbb{C}}^{2}$ is given by
$$D_{\lambda}:(\zeta, t) \mapsto\left(\lambda \zeta, \lambda^{2} t\right) .$$
All other Heisenberg dilations fixing $q_{\infty}$ may be obtained by conjugating by a Heisenberg translation.

The stabiliser of $q_{\infty}$ in $P U(2,1)$ is generated by all Heisenberg translations, rotations and dilations. However, only Heisenberg translations and rotations are isometric with respect to various natural metrics on $\Re$. For this reason the group generated by all Heisenberg translations and rotations, which is the semidirect product $U(1) \ltimes \Re$, is called the Heisenberg isometry group $\operatorname{Isom}(\Re)$. The nontrivial central elements of the Heisenberg isometry group are precisely the vertical translations. In particular, each element of $\operatorname{Isom}(\Re)$ preserves every horosphere.

There is a canonical projection from $\Re$ to $\mathbb{C}$ called vertical projection and denoted by $\Pi$, given by $\Pi:(\zeta, t) \longmapsto \zeta$. Using the exact sequence
$$0 \longrightarrow \mathbb{R} \longrightarrow \Re \xrightarrow{\Pi} \mathbb{C} \longrightarrow 0,$$
we obtain the exact sequence (see Scott [14] page 467)
$$0 \longrightarrow \mathbb{R} \longrightarrow \operatorname{Isom}(\Re) \xrightarrow{\Pi_{*}} \operatorname{Isom}(\mathbb{C}) \longrightarrow 1 .$$
Here $\operatorname{Isom}(\mathbb{C})$ is the group of orientation preserving Euclidean isometries of $\mathbb{C}$.

Observe the elements in $\operatorname{Isom}(\mathbb{C})$ can be represented by matrices in $\operatorname{GL}(2, \mathbb{C})$ of the form
$$\left[\begin{array}{cc}
e^{i \theta} & \zeta_{0} \\
0 & 1
\end{array}\right]\left[\begin{array}{l}
\zeta \\
1
\end{array}\right]=\left[\begin{array}{c}
e^{i \theta} \zeta+\zeta_{0} \\
1
\end{array}\right]$$
Therefore, the map $\Pi_{*}$ can be given by
$$\Pi_{*}:\left[\begin{array}{ccc}
1 & -\bar{\zeta}_{0} e^{i \theta} & \left(-\left|\zeta_{0}\right|^{2}+i t_{0}\right) / 2 \\
0 & e^{i \theta} & \zeta_{0} \\
0 & 0 & 1
\end{array}\right] \longrightarrow\left[\begin{array}{cc}
e^{i \theta} & \zeta_{0} \\
0 & 1
\end{array}\right] .$$
It is clear that
$$\operatorname{Ker}\left(\Pi_{*}\right)=\left\{\left[\begin{array}{ccc}
1 & 0 & i t_{0} / 2 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right]: t_{0} \in \mathbb{R}\right\}$$
is the group of vertical translations fixing $q_{\infty}$.
2.3. Isometric spheres. Given an element $G \in P U(2,1)$ with satisfying $G\left(q_{\infty}\right) \neq q_{\infty}$, we define the isometric sphere of $G$ to be the hypersurface
$$\left\{\mathbf{z} \in \mathbf{H}_{\mathbb{C}}^{2}:\left|\left\langle\mathbf{z}, q_{\infty}\right\rangle\right|=\left|\left\langle\mathbf{z}, G^{-1}\left(q_{\infty}\right)\right\rangle\right|\right\} .$$

For example, the isometric sphere of
$$I_{0}=\left[\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right]$$
is
$$\mathcal{B}_{0}=\left\{(\zeta, t, u) \in \mathfrak{S}:\left||\zeta|^{2}+u+i t\right|=2\right\}$$
in horospherical coordinates or
$$\mathcal{B}_{0}=\left\{\left[z_{1}, z_{2}, z_{3}\right] \in \mathbf{H}_{\mathbb{C}}^{2}:\left|z_{1}\right|=\left|z_{3}\right|\right\}$$
in homogeneous coordinates.
All other isometric spheres are images of $\mathcal{B}_{0}$ by Heisenberg dilations, rotations and translations. Thus the isometric sphere with radius $r$ and centre $\left(\zeta_{0}, t_{0}, 0\right)$ is given by
$$\left\{(\zeta, t, u):\left|\left|\zeta-\zeta_{0}\right|^{2}+u+i t-i t_{0}+2 i \Im m\left(\zeta \bar{\zeta}_{0}\right)\right|=r^{2}\right\} .$$

If $G$ has the matrix form
$$\left[\begin{array}{lll}
a & b & c \\
d & e & f \\
g & h & j
\end{array}\right],$$
then $G\left(q_{\infty}\right) \neq q_{\infty}$ if and only if $g \neq 0$. The isometric sphere of $G$ has radius $r=\sqrt{2 /|g|}$ and centre $G^{-1}\left(q_{\infty}\right)$, which in horospherical coordinates is
$$\left(\zeta_{0}, t_{0}, 0\right)=(\bar{h} / \bar{g}, 2 \Im m(\bar{j} / \bar{g}), 0) .$$

Isometric spheres are examples of bisectors. Mostow [12] showed that a bisector is the preimage of a geodesic, called spine, under orthogonal projection onto the unique complex line containing it. The fibres of this projection are complex lines called the slices of the bisector. Goldman [9] showed that a bisector is the union of all totally real Larangian planes containing the spine. Such Lagrangian planes are called the meridians.

\section*{3. On the structure of the stabiliser}

In this section we will obtain the generators and relations of the stabiliser of Picard modular groups by analysis of the fundamental domain in Heisenberg group.

Let $\mathcal{O}_{d}$ be the ring of integers in the quadratic imaginary number field $\mathbb{Q}(i \sqrt{d})$, where $d$ is a positive square-free integer. If $d \equiv 1,2(\bmod 4)$, then $\mathcal{O}_{d}=\mathbb{Z}[i \sqrt{d}]$ and if $d \equiv 3(\bmod 4)$, then $\mathcal{O}_{d}=\mathbb{Z}\left[\omega_{d}\right]$, where $\omega_{d}=(1+i \sqrt{d}) / 2$. The group $\Gamma_{d}=P U\left(2,1 ; \mathcal{O}_{d}\right)$ is called Euclidean Picard modular group if the ring $\mathcal{O}_{d}$ is Euclidean, namely, only the rings $\mathcal{O}_{1}, \mathcal{O}_{2}, \mathcal{O}_{3}, \mathcal{O}_{7}, \mathcal{O}_{11}$. Further relative to amalgamation property, these five groups can be subclassified into three groupings $\left\{\Gamma_{1}\right\},\left\{\Gamma_{3}\right\},\left\{\Gamma_{2}, \Gamma_{7}, \Gamma_{11}\right\}$. Since two classes $\left\{\Gamma_{1}\right\},\left\{\Gamma_{3}\right\}$ (c.f. [5], [6]) have been studied in detail, we mainly describe the remaining class $\left\{\Gamma_{2}, \Gamma_{7}, \Gamma_{11}\right\}$.
3.1. The stabiliser of $q_{\infty}$. First we want to analyse $\left(\Gamma_{d}\right)_{\infty}$ with $d=$ 2, 7, 11, the stabiliser of $q_{\infty}$. Every element of $\left(\Gamma_{d}\right)_{\infty}$ is upper triangular and its diagonal entries are units in $\mathcal{O}_{d}$. Recall that the units of $\mathcal{O}_{1}$ are $\pm 1, \pm i$, they are $\pm 1, \pm \omega, \pm \omega^{2}$ for $\mathcal{O}_{3}$ and they are $\pm 1$ for others. Therefore $\left(\Gamma_{d}\right)_{\infty}$ contains no dilations and so is a subgroup of $\operatorname{Isom}(\Re)$ and fits into the exact sequence as
$$0 \longrightarrow \mathbb{R} \cap\left(\Gamma_{d}\right)_{\infty} \longrightarrow\left(\Gamma_{d}\right)_{\infty} \xrightarrow{\Pi_{*}} \Pi_{*}\left(\left(\Gamma_{d}\right)_{\infty}\right) \longrightarrow 1 .$$

We can write the isometry group of the integer lattice as
$$\operatorname{Isom}\left(\mathcal{O}_{d}\right)=\left\{\left[\begin{array}{cc}
\alpha & \beta \\
0 & 1
\end{array}\right]: \alpha, \beta \in \mathcal{O}_{d}, \alpha \text { is a unit }\right\} .$$

We now find the image and kernel in this exact sequence.
Proposition 3.1. The stabiliser $\left(\Gamma_{d}\right)_{\infty}$ of $q_{\infty}$ in $\Gamma_{d}$ satisfies
$$0 \longrightarrow 2 \sqrt{d} \mathbb{Z} \longrightarrow\left(\Gamma_{d}\right)_{\infty} \xrightarrow{\Pi_{*}} \Delta \longrightarrow 1,$$
where $\Delta \subset \operatorname{Isom}\left(\mathcal{O}_{d}\right)$ is of index 2 if $d \equiv 2(\bmod 4)$ and $\Delta=\operatorname{Isom}\left(\mathcal{O}_{d}\right)$ if $d \equiv 3(\bmod 4)$.

Proof. Although we only consider the cases $d=2,7,11$, the ring $\mathcal{O}_{2}$ represents those for the values of $d$ with $d \equiv 2(\bmod 4)$ and the rings $\mathcal{O}_{7}, \mathcal{O}_{11}$ represent those of the values $d \equiv 3(\bmod 4)$, the remaining case is the same as $\mathcal{O}_{1}$ which has been done in [6]. Observe that $\operatorname{Isom}\left(\mathcal{O}_{d}\right)$ is generated by the subgroup of translations
$$\left\{\hat{T}_{\beta}=\left[\begin{array}{cc}
1 & \beta \\
0 & 1
\end{array}\right]: \beta \in \mathcal{O}_{d}\right\}$$
and the finite subgroup of order two
$$\left\{\hat{R}_{\alpha}=\left[\begin{array}{cc}
\alpha & 0 \\
0 & 1
\end{array}\right]: \alpha \in \mathcal{O}_{d}, \alpha \text { is a unit }\right\} .$$
Then, to understand $\Delta \subset \operatorname{Isom}\left(\mathcal{O}_{d}\right)$, it suffices to determine which translations can be lifted. We divide into two cases to complete the proof.
(i) The case $\mathcal{O}_{d}$ with $d \equiv 2(\bmod 4)$

Suppose that $\beta \in \mathcal{O}_{d}=\mathbb{Z}[i \sqrt{d}]$ and consider the translation $\hat{T}_{\beta}$ by $\beta$ in $\mathbb{Z}[i \sqrt{d}]$ given above. The preimage of $\hat{T}_{\beta}$ under $\Pi_{*}$ has the form
$$T_{\beta, t}=\left[\begin{array}{ccc}
1 & -\bar{\beta} & \frac{-|\beta|^{2}+i t}{2} \\
0 & 1 & \beta \\
0 & 0 & 1
\end{array}\right] .$$
This map is in $\operatorname{PU}(2,1 ; \mathbb{Z}[i \sqrt{d}])$ if and only if $|\beta|^{2}$ is an even integer and $t \in 2 \sqrt{d} \mathbb{Z}$. Writing $\beta=m+i \sqrt{d} n$ for $m, n \in \mathbb{Z}$, then we can obtain $m \equiv 0(\bmod 2)$ from the conditions $|\beta|^{2}=m^{2}+d n^{2} \in 2 \mathbb{Z}$ and $d \equiv 2(\bmod 4)$.

Therefore, we conclude that $\Delta \subset \operatorname{Isom}(\mathbb{Z}[i \sqrt{d}])$ is of index 2. Also, the kernel of $\Pi_{*}$ is generated by
$$\left[\begin{array}{ccc}
1 & 0 & i \sqrt{d} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right],$$
which is a vertical translation of $(0,2 \sqrt{2})$.
(ii) The case $\mathcal{O}_{d}$ with $d \equiv 3(\bmod 4)$

Suppose that $\beta=m+n \frac{1+i \sqrt{d}}{2} \in \mathcal{O}_{d}$ with $m, n \in \mathbb{Z}$ for $d \equiv 3(\bmod 4)$. By the same argument of (i), it only suffices to determine $m, n$ such that $|\beta|^{2}$ is an integer. For $d \equiv 3(\bmod 4)$, it is easy to show that $|\beta|^{2}=m^{2}+$ $m n+n^{2}(d+1) / 4 \in \mathbb{Z}$ for any $m, n \in \mathbb{Z}$, which implies that $\Delta=\operatorname{Isom}\left(\mathcal{O}_{d}\right)$. Obviously, the kernel of $\Pi_{*}$ is generated by a vertical translation of $(0,2 \sqrt{d})$. \(\square\)
3.2. Fundamental domain for the stabiliser. As the first step toward the construction of a fundamental domain for the action of $\left(\Gamma_{d}\right)_{\infty}$ on $\Re$ for $d=2,7,11$, we shall find the suitable generators of $\operatorname{Isom}\left(\mathcal{O}_{d}\right)$ to construct a fundamental domain in $\mathbb{C}$.

In the proof of Proposition 3.1 we saw that $\Delta=\Pi_{*}\left(\left(\Gamma_{2}\right)_{\infty}\right)$ is a subgroup of index 2 in $\operatorname{Isom}\left(\mathcal{O}_{2}\right)$ consisting of elements of $\operatorname{GL}\left(2, \mathcal{O}_{2}\right)$ of the form
$$\left\{\left[\begin{array}{cc}
(-1)^{j} & m+i \sqrt{2} n \\
0 & 1
\end{array}\right]: j=0,1, m, n \in \mathbb{Z}, m \equiv 0(\bmod 2)\right\} .$$
A fundamental domain for this group is the triangle in $\mathbb{C}$ with vertices at $-1+\sqrt{2} i / 2$ and $1 \pm \sqrt{2} i / 2$; see (a) in Figure 3.1. Side paring maps are given by
$$r_{1}^{(2)}=\left[\begin{array}{cc}
-1 & 0 \\
0 & 1
\end{array}\right], r_{2}^{(2)}=\left[\begin{array}{cc}
-1 & 2 \\
0 & 1
\end{array}\right], r_{3}^{(2)}=\left[\begin{array}{cc}
-1 & \sqrt{2} i \\
0 & 1
\end{array}\right] .$$
The first of these is a rotation of order 2 fixing origin, the second is a rotation of order 2 fixing 1/2 and the third is a rotation of order 2 fixing $\sqrt{2} i / 2$. Indeed every element of $\Delta=G L\left(2, \mathcal{O}_{2}\right)$ is generated by $r_{1}^{(2)}, r_{2}^{(2)}, r_{3}^{(2)}$ as follows
$$\begin{aligned}
{\left[\begin{array}{cc}
(-1)^{j} & 2 m+\sqrt{2} n i \\
0 & 1
\end{array}\right] } & =\left[\begin{array}{cc}
1 & 2 \\
0 & 1
\end{array}\right]^{m}\left[\begin{array}{cc}
1 & \sqrt{2} i \\
0 & 1
\end{array}\right]^{n}\left[\begin{array}{cc}
-1 & 0 \\
0 & 1
\end{array}\right]^{j} \\
& =\left(r_{2}^{(2)} r_{1}^{(2)}\right)^{m}\left(r_{3}^{(2)} r_{1}^{(2)}\right)^{n}\left(r_{1}^{(2)}\right)^{j} .
\end{aligned}$$

As the same argument, a fundamental domain for $\operatorname{Isom}\left(\mathcal{O}_{d}\right)$ with $d=7$ or 11 is the triangle in $\mathbb{C}$ with vertices at $(-1+i \sqrt{d}) / 4,(1-i \sqrt{d}) / 4$ and $(3+i \sqrt{d}) / 4$; see (b) in Figure 3.1. Side paring maps are given by
$$r_{1}^{(d)}=\left[\begin{array}{cc}
-1 & 0 \\
0 & 1
\end{array}\right], r_{2}^{(d)}=\left[\begin{array}{cc}
-1 & 1 \\
0 & 1
\end{array}\right], r_{3}^{(d)}=\left[\begin{array}{cc}
-1 & (1+i \sqrt{d}) / 2 \\
0 & 1
\end{array}\right] .$$
All these maps are rotations by $\pi$ fixing 0, 1/2 and $(1+i \sqrt{d}) / 4$ respectively.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-08.jpg?height=662&width=1069&top_left_y=392&top_left_x=515}
\captionsetup{labelformat=empty}
\caption{Figure 3.1. (a) Fundamental domain for a subgroup $\Delta$ of $\operatorname{Isom}\left(\mathcal{O}_{2}\right)$ with index 2. (b) Fundamental domain for $\operatorname{Isom}\left(\mathcal{O}_{d}\right)$ with $d=7,11$. This is also true for all the values of $d$ with $d \equiv 3(\bmod 4)$.}
\end{figure}

In order to produce a fundamental domain for $\left(\Gamma_{d}\right)_{\infty}$ we look at all the preimages of the triangle (that is a fundamental domain of $\Pi_{*}\left(\left(\Gamma_{d}\right)_{\infty}\right)$ ) under vertical projection $\Pi$ and we intersect this with a fundamental domain for $\operatorname{ker}\left(\Pi_{*}\right)$. The inverse of image of the triangle under $\Pi$ is an infinite prism. The kernel of $\Pi_{*}$ is the infinite cyclic group generated by $T$, the vertical translation by $(0,2 \sqrt{d})$.

Proposition 3.2. $\left(\Gamma_{2}\right)_{\infty}$ is generated by
$$R_{1}^{(2)}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right], R_{2}^{(2)}=\left[\begin{array}{ccc}
1 & 2 & -2 \\
0 & -1 & 2 \\
0 & 0 & 1
\end{array}\right], R_{3}^{(2)}=\left[\begin{array}{ccc}
1 & -i \sqrt{2} & -1 \\
0 & -1 & i \sqrt{2} \\
0 & 0 & 1
\end{array}\right]$$
and
$$T^{(2)}=\left[\begin{array}{ccc}
1 & 0 & i \sqrt{2} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] .$$

A presentation is given by
$$\left(\Gamma_{2}\right)_{\infty}=\left\langle R_{j}^{(2)}, T^{(2)} \mid R_{j}^{(2)^{2}}=\left[T^{(2)}, R_{j}^{(2)}\right]=\left(T^{(2)^{2}} R_{1}^{(2)} R_{3}^{(2)} R_{2}^{(2)}\right)^{2}=i d\right\rangle .$$

Proof. Those matrices are constructed by lifting generators of the subgroup $\Delta \subset \operatorname{Isom}\left(\mathcal{O}_{2}\right)$ with index 2 and also $T^{(2)}$ is a generator of the kernel of the map $\Pi_{*}$. A fundamental domain can be constructed with side pairings as Figure 3.2, where the vertices of the prism are $v_{3}^{+}=(-1+\sqrt{2} i / 2, \sqrt{2}), v_{2}^{+}=$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-09.jpg?height=680&width=660&top_left_y=397&top_left_x=737}
\captionsetup{labelformat=empty}
\caption{Figure 3.2. A fundamental domain $\boldsymbol{\Sigma}_{2}$ for $\left(\Gamma_{2}\right)_{\infty}$ in the Heisenberg group: the map $R_{1}^{(2)}$ rotates through $\pi$ about $\zeta=0$, the map $R_{2}^{(2)}$ is a Heisenberg rotation through $\pi$ about $\zeta=1$ and the map $R_{3}^{(2)}$ is a Heisenberg rotation through $\pi$ about $\zeta=\sqrt{2} i / 2$.}
\end{figure}
$(1+\sqrt{2} i / 2, \sqrt{2}), v_{1}^{+}=(1-\sqrt{2} i / 2, \sqrt{2})$ for the upper cap of the prism and $v_{3}^{-}=(-1+\sqrt{2} i / 2,-\sqrt{2}), v_{2}^{-}=(1+\sqrt{2} i / 2,-\sqrt{2}), v_{1}^{-}=(1-\sqrt{2} i / 2,-\sqrt{2})$ for the base. In particular, the points $v_{4}^{ \pm}, v_{5}^{ \pm}, v_{6}^{ \pm}$are the middle points of the edges $\left(v_{1}^{ \pm}, v_{2}^{ \pm}\right),\left(v_{2}^{ \pm}, v_{3}^{ \pm}\right)$and $\left(v_{3}^{ \pm}, v_{1}^{ \pm}\right)$, respectively.

The actions of side-pairing maps on $\Re$ are given by
$$\begin{aligned}
& R_{1}^{(2)}(\zeta, t)=(-\zeta, t), \\
& R_{2}^{(2)}(\zeta, t)=(-\zeta+2, t+4 \Im m \zeta), \\
& R_{3}^{(2)}(\zeta, t)=(-\zeta+i \sqrt{2}, t-2 \sqrt{2} \Re e \zeta), \\
& T^{(2)}(\zeta, t)=(\zeta, t+2 \sqrt{2}) .
\end{aligned}$$
We describe the side pairing in terms of the action on the vertice:
$$\begin{aligned}
R_{1}^{(2)} & :\left(v_{6}^{+}, v_{1}^{+}, v_{1}^{-}, v_{6}^{-}\right) \longrightarrow\left(v_{6}^{+}, v_{3}^{+}, v_{3}^{-}, v_{6}^{-}\right), \\
R_{2}^{(2)} & :\left(v_{1}^{+}, v_{4}^{+}, v_{4}^{-}\right) \longrightarrow\left(v_{2}^{-}, v_{4}^{+}, v_{4}^{-}\right), \\
T^{(2)} R_{2}^{(2)} & :\left(v_{1}^{+}, v_{1}^{-}, v_{4}^{-}\right) \longrightarrow\left(v_{2}^{+}, v_{2}^{-}, v_{4}^{+}\right), \\
R_{3}^{(2)} & :\left(v_{2}^{+}, v_{5}^{+}, v_{5}^{-}\right) \longrightarrow\left(v_{3}^{-}, v_{5}^{+}, v_{5}^{-}\right), \\
T^{(2)} R_{3}^{(2)} & :\left(v_{2}^{+}, v_{2}^{-}, v_{5}^{-}\right) \longrightarrow\left(v_{3}^{+}, v_{3}^{+}, v_{5}^{+}\right), \\
T^{(2)} & :\left(v_{1}^{-}, v_{4}^{-}, v_{2}^{-}, v_{5}^{-}, v_{3}^{-}, v_{6}^{-}\right) \longrightarrow\left(v_{1}^{+}, v_{4}^{+}, v_{2}^{+}, v_{5}^{+}, v_{3}^{+}, v_{6}^{+}\right) .
\end{aligned}$$

The presentation can be obtained following from the edge cycles of the fundamental domain. \(\square\)

Proposition 3.3. $\left(\Gamma_{7}\right)_{\infty}$ is generated by
$$R_{1}^{(7)}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right], R_{2}^{(7)}=\left[\begin{array}{ccc}
1 & 1 & -\bar{\omega}_{7} \\
0 & -1 & 1 \\
0 & 0 & 1
\end{array}\right], R_{3}^{(7)}=\left[\begin{array}{ccc}
1 & \bar{\omega}_{7} & -1 \\
0 & -1 & \omega_{7} \\
0 & 0 & 1
\end{array}\right]$$
and
$$T^{(7)}=\left[\begin{array}{ccc}
1 & 0 & i \sqrt{7} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] .$$
A presentation is given by
$$\begin{aligned}
\left(\Gamma_{7}\right)_{\infty}=\left\langle R_{j}^{(7)}, T^{(7)}\right| R_{1}^{(7)^{2}}= & R_{3}^{(7)^{2}}=\left[T^{(7)}, R_{1}^{(7)}\right]=\left[T^{(7)}, R_{3}^{(7)}\right] \\
& \left.=T^{(7)} R_{2}^{(7)^{-2}}=\left(R_{1}^{(7)} R_{3}^{(7)} R_{2}^{(7)}\right)^{2}=i d\right\rangle .
\end{aligned}$$
Proof. Those matrices are constructed by lifting generators of $\operatorname{Isom}\left(\mathcal{O}_{7}\right)$ and also $T^{(7)}$ is a generator of the kernel of the map $\Pi_{*}$. A fundamental domain can be constructed with side pairings as Figure 3.3, where the vertices of the prism are $v_{1}^{+}=((1-i \sqrt{7}) / 4, \sqrt{7}), v_{2}^{+}=((3+i \sqrt{7}) / 4, \sqrt{7}), v_{4}^{+}=((-1+$ $i \sqrt{7}) / 4, \sqrt{7})$ for the upper cap of the prism and $v_{1}^{-}=((1-i \sqrt{7}) / 4,-\sqrt{7})$, $v_{2}^{-}=((3+i \sqrt{7}) / 4,-\sqrt{7}), v_{4}^{-}=((-1+i \sqrt{7}) / 4,-\sqrt{7})$ for the base. The points $v_{3}^{ \pm}, v_{5}^{ \pm}$are the middle points of the edges $\left(v_{2}^{ \pm}, v_{4}^{ \pm}\right)$and $\left(v_{4}^{ \pm}, v_{1}^{ \pm}\right)$. In particular, we introduce more three points $w_{1}^{+}=((1-i \sqrt{7}) / 4, \sqrt{7} / 2), w_{2}^{-}=$ $((3+i \sqrt{7}) / 4,-\sqrt{7} / 2)$ and $w_{3}^{+}=((-1+i \sqrt{7}) / 4, \sqrt{7} / 2)$. The actions of side-pairing maps on $\Re$ are given by
$$\begin{aligned}
& R_{1}^{(7)}(\zeta, t)=(-\zeta, t), \\
& R_{2}^{(7)}(\zeta, t)=(-\zeta+1, t+2 \Im m \zeta+\sqrt{7}), \\
& R_{3}^{(7)}(\zeta, t)=\left(-\zeta+\omega_{7}, t+2 \Im m\left(\bar{\omega}_{7} \zeta\right)\right), \\
& T^{(7)}(\zeta, t)=(\zeta, t+2 \sqrt{7}) .
\end{aligned}$$
We describe the side pairing in terms of the action on the vertice:
$$\begin{aligned}
R_{1}^{(7)} & :\left(v_{5}^{+}, v_{1}^{+}, v_{1}^{-}, v_{5}^{-}\right) \longrightarrow\left(v_{5}^{+}, v_{4}^{+}, v_{4}^{-}, v_{5}^{-}\right), \\
R_{2}^{(7)} & :\left(v_{1}^{-}, v_{2}^{-}, w_{1}^{-}, w_{1}^{+}\right) \longrightarrow\left(w_{1}^{-}, w_{1}^{+}, v_{1}^{+}, v_{2}^{+}\right), \\
R_{3}^{(7)} & :\left(v_{2}^{+}, w_{1}^{-}, v_{3}^{-}, v_{3}^{+}\right) \longrightarrow\left(w_{2}^{+}, v_{4}^{-}, v_{3}^{-}, v_{3}^{+}\right), \\
T^{(7)} R_{3}^{(7)} & :\left(w_{1}^{-}, v_{2}^{-}, v_{3}^{-}\right) \longrightarrow\left(v_{4}^{+}, w_{2}^{+}, v_{3}^{+}\right), \\
T^{(7)} & :\left(v_{1}^{-}, v_{2}^{-}, v_{3}^{-}, v_{4}^{-}, v_{5}^{-}\right) \longrightarrow\left(v_{1}^{+}, v_{2}^{+}, v_{3}^{+}, v_{4}^{+}, v_{5}^{+}\right) .
\end{aligned}$$
The presentation can be obtained following from the edge cycles of the fundamental domain. \(\square\)

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-11.jpg?height=657&width=658&top_left_y=398&top_left_x=739}
\captionsetup{labelformat=empty}
\caption{Figure 3.3. A fundamental domain $\boldsymbol{\Sigma}_{7}$ for $\left(\Gamma_{7}\right)_{\infty}$ in the Heisenberg group: the map $R_{1}^{(7)}$ rotates through $\pi$ about $\zeta=0$, the action of parabolic $R_{2}^{(7)}$ is a Heisenberg rotation through $\pi$ about $\zeta=1 / 2$ followed by an upward vertical translation by $\sqrt{7}$ and the map $R_{3}^{(7)}$ is a Heisenberg rotation through $\pi$ about $\zeta=(1+i \sqrt{7}) / 4$.}
\end{figure}

Proposition 3.4. $\left(\Gamma_{11}\right)_{\infty}$ is generated by
$$\begin{gathered}
R_{1}^{(11)}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right], R_{2}^{(11)}=\left[\begin{array}{ccc}
1 & 1 & -\bar{\omega}_{11} \\
0 & -1 & 1 \\
0 & 0 & 1
\end{array}\right], \\
R_{3}^{(11)}=\left[\begin{array}{ccc}
1 & \bar{\omega}_{11} & -1-\bar{\omega}_{11} \\
0 & -1 & \omega_{11} \\
0 & 0 & 1
\end{array}\right] \quad \text { and } \quad T^{(11)}=\left[\begin{array}{ccc}
1 & 0 & i \sqrt{11} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] .
\end{gathered}$$
A presentation is given by
$$\begin{aligned}
\left(\Gamma_{11}\right)_{\infty}=\left\langle R_{j}^{(11)},\right. & T^{(11)} \mid R_{1}^{(11)^{2}}=\left[T^{(11)}, R_{1}^{(11)}\right]=T^{(11)} R_{2}^{(11)^{-2}} \\
& \left.=T^{(11)} R_{3}^{(11)^{-2}}=T^{(11)}\left(R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\right)^{-2}=i d\right\rangle .
\end{aligned}$$
Proof. Those matrices are constructed by lifting generators of $\operatorname{Isom}\left(\mathcal{O}_{11}\right)$ and also $T^{(11)}$ is a generator of the kernel of the map $\Pi_{*}$. A fundamental domain can be constructed with side pairings as Figure 3.4, where the vertices of the prism are $v_{1}^{+}=((1-i \sqrt{11}) / 4, \sqrt{11}), v_{2}^{+}=((3+i \sqrt{11}) / 4,3 \sqrt{11} / 2)$, $v_{3}^{+}=((-1+i \sqrt{11}) / 4,2 \sqrt{11})$ for the upper cap of the prism and $v_{1}^{-}=$ $((1-i \sqrt{11}) / 4,-\sqrt{11}), v_{2}^{-}=((3+i \sqrt{11}) / 4,-\sqrt{11} / 2), v_{3}^{-}=((-1+i \sqrt{11}) / 4,0)$ for the base. The points $v_{0}^{ \pm}$are the middle points of the edges $\left(v_{1}^{ \pm}, v_{3}^{ \pm}\right)$. In particular, we introduce more three points $w_{1}=((1-i \sqrt{11}) / 4,0), w_{2}=$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-12.jpg?height=605&width=669&top_left_y=398&top_left_x=736}
\captionsetup{labelformat=empty}
\caption{Figure 3.4. A fundamental domain $\boldsymbol{\Sigma}_{11}$ for $\left(\Gamma_{11}\right)_{\infty}$ in the Heisenberg group: the map $R_{1}^{(11)}$ rotates through $\pi$ about $\zeta=0$, the action of parabolic $R_{2}^{(11)}$ is a screw Heisenberg rotation through $\pi$ about $\zeta=1 / 2$ followed by an upward vertical translation by $\sqrt{11}$ and the map $R_{3}^{(11)}$ is a screw Heisenberg rotation through $\pi$ about $\zeta=(1+i \sqrt{11}) / 4$ followed by an upward vertical translation by $\sqrt{11}$.}
\end{figure}
$((3+i \sqrt{11}) / 4, \sqrt{11} / 2)$ and $w_{3}=((-1+i \sqrt{11}) / 4, \sqrt{11})$. The actions of side-pairing maps on $\Re$ are given by
$$\begin{aligned}
& R_{1}^{(11)}(\zeta, t)=(-\zeta, t), \\
& R_{2}^{(11)}(\zeta, t)=(-\zeta+1, t+2 \Im m \zeta+\sqrt{11}), \\
& R_{3}^{(11)}(\zeta, t)=\left(-\zeta+\omega_{11}, t+2 \Im m\left(\bar{\omega}_{11} \zeta\right)+\sqrt{11}\right), \\
& T^{(11)}(\zeta, t)=(\zeta, t+2 \sqrt{11}) .
\end{aligned}$$
We describe the side pairing in terms of the action on the vertice:
$$\begin{aligned}
R_{1}^{(11)} & :\left(v_{0}^{+}, v_{1}^{+}, w_{1}, v_{0}^{-}\right) \longrightarrow\left(v_{0}^{+}, w_{3}, v_{3}^{-}, v_{0}^{-}\right), \\
T^{(11)} R_{1}^{(11)} & :\left(w_{1}, v_{1}^{-}, v_{0}^{-}\right) \longrightarrow\left(v_{3}^{+}, w_{3}, v_{0}^{+}\right), \\
R_{2}^{(11)} & :\left(v_{1}^{+}, w_{1}, v_{1}^{-}, v_{2}^{-}\right) \longrightarrow\left(v_{2}^{+}, w_{2}, v_{2}^{-}, v_{1}^{+}\right), \\
R_{3}^{(11)} & :\left(v_{2}^{+}, w_{2}, v_{2}^{-}, v_{3}^{-}\right) \longrightarrow\left(v_{3}^{+}, w_{3}, v_{3}^{-}, v_{2}^{+}\right), \\
T^{(11)} & :\left(v_{0}^{-}, v_{1}^{-}, v_{2}^{-}, v_{3}^{-}\right) \longrightarrow\left(v_{0}^{+}, v_{1}^{+}, v_{2}^{+}, v_{3}^{+}\right) .
\end{aligned}$$
The presentation can be obtained following from the edge cycles of the fundamental domain. \(\square\)

\section*{4. The statement of our method and results}

In this section, we introduce the method used in ([5], [6]) to determine the generators of the Euclidean Picard groups and then state our results.

Recall that the map
$$I_{0}=\left[\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right],$$
defined in the Section 2.3. We consider the isometric sphere $\mathcal{B}_{0}$ of $I_{0}$ given by (2.4), which is a Cygan sphere centred $o=(0,0,0)$ with radius $\sqrt{2}$. Observe that $I_{0}$ maps $\mathcal{B}_{0}$ to itself and swaps the inside and the outside of $\mathcal{B}_{0}$. Given an element of $\Gamma_{d}$ as the form (2.6), we know that the radius of isometric sphere is $\sqrt{2 /|g|}$. For each case $\mathcal{O}_{d}$, the radius of isometric sphere is not greater than $\sqrt{2}$ since the absolute of $g$ is not smaller than 1 for $g \in \mathcal{O}_{d}$. We show that the largest isometric spheres are all the images of $\mathcal{B}_{0}$ under the elements in $\left(\Gamma_{d}\right)_{\infty}$.

Proposition 4.1. An isometric sphere has the largest radius if and only if it is the image of $\mathcal{B}_{0}$ under an element in $\left(\Gamma_{d}\right)_{\infty}$.

Proof. Obviously, the image of $\mathcal{B}_{0}$ under an element in $\left(\Gamma_{d}\right)_{\infty}$ has the largest radius $\sqrt{2}$. On the contrary, given an element $G$ as the form (2.6) such that $G\left(q_{\infty}\right) \neq q_{\infty}$, then the isometric sphere of $G$ has the largest radius which leads to $g=1$. So the centre of isometric sphere of $G$ is $G^{-1}(\infty)=$ $(\bar{h}, 2 \Im m \bar{j}, 0)$ in horospherical coordinates. Since $\bar{h}$ and $2 \Im m \bar{j} \in \mathcal{O}_{d}$, we can take a Heisenberg translation $T \in\left(\Gamma_{d}\right)_{\infty}$ mapping the origin to $(\bar{h}, 2 \Im m \bar{j})$. Writing $T^{\prime}=G T I_{0}$, we know that $T^{\prime}$ fixes $\infty$. We conclude explicitly that the isometric sphere of $G$ is
$$\left\{\mathbf{z} \in \mathbf{H}_{\mathbb{C}}^{2}:\left|\left\langle\mathbf{z}, q_{\infty}\right\rangle\right|=\left|\left\langle\mathbf{z}, G^{-1}\left(q_{\infty}\right)\right\rangle\right|=\left|\left\langle\mathbf{z}, T I_{0}\left(q_{\infty}\right)\right\rangle\right|\right\},$$
which is the image of $\mathcal{B}_{0}$ under $T$. \(\square\)

Our method is based on the special feature that the orbifold $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma_{d}$ has only one cusp for $d=2,7,11$. For these types of orbifolds, one would like to construct a fundamental domain using the Ford domain (that is the exteriors of isometric spheres of all elements not fixing infinity), namely, the intersection of the Ford domain and a fundamental domain for the stabiliser of infinity. The Ford domain is canonical, but we can choose a fundamental domain for the stabiliser freely. As the first step toward the construction of a fundamental domain, we should always determine the generators of the group. In the previous section, we found suitable generators of the stabliser and constructed a fundamental domain. We will show that adjoining $I_{0}$ to $\left(\Gamma_{d}\right)_{\infty}$ gives the Euclidean Picard modular groups $\Gamma_{d}$. The basic idea of the proof can be described easily. Analogous to Theorem 3.5 of [5] we shall prove that $\left\langle R_{1}^{(d)}, R_{2}^{(d)}, R_{3}^{(d)}, T^{(d)}, I_{0}\right\rangle$ has only one cusp. The fact that $P U\left(2,1 ; \mathcal{O}_{d}\right)$ has the same cusp and the stabiliser of infinity as the group generated by
$R_{1}^{(d)}, R_{2}^{(d)}, R_{3}^{(d)}, T^{(d)}, I_{0}$ shows that they are the same. The key step is to find a union of isometric spheres such that a fundamental domain for $\Gamma_{d}$ is contained in the intersection of their exteriors and a fundamental domain for the stabiliser, which implies that the group $\left\langle R_{1}^{(d)}, R_{2}^{(d)}, R_{3}^{(d)}, T^{(d)}, I_{0}\right\rangle$ has only one cusp. In other words, we want to show the union of the boundaries of these isometric spheres in Heisenberg group contains each of the prisms we constructed above. The problem of determining this will be discussed in the next section.

A simple lemma will be used in the proof of our theorems many times, we state it as follows.

Lemma 4.2. (c.f. [6]) All Cygan balls are affinely convex.
Our aim is to prove the following results, we summarise them as three theorems.

Theorem 4.3. Let $\mathcal{K}=\mathbb{Q}(\sqrt{-2})$ and let $\mathcal{O}_{2}=\mathbb{Z}[i \sqrt{2}]$. Then the group $\operatorname{PU}\left(2,1, \mathcal{O}_{2}\right)$ is generated by the elements
$$\begin{gathered}
I_{0}=\left[\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right], R_{1}^{(2)}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right], R_{2}^{(2)}=\left[\begin{array}{ccc}
1 & 2 & -2 \\
0 & -1 & 2 \\
0 & 0 & 1
\end{array}\right], \\
R_{3}^{(2)}=\left[\begin{array}{ccc}
1 & -i \sqrt{2} & -1 \\
0 & -1 & i \sqrt{2} \\
0 & 0 & 1
\end{array}\right] \text { and } T^{(2)}=\left[\begin{array}{ccc}
1 & 0 & i \sqrt{2} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] .
\end{gathered}$$

Theorem 4.4. Let $\mathcal{K}=\mathbb{Q}(\sqrt{-7})$ and let $\mathcal{O}_{7}=\mathbb{Z}\left[\omega_{7}\right]$, where $\omega_{7}=\frac{1}{2}(1+$ $i \sqrt{7}$ ), be the ring of integers of $\mathcal{K}$. Then the group $P U\left(2,1, \mathcal{O}_{7}\right)$ is generated by the elements
$$\begin{gathered}
I_{0}=\left[\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right], R_{1}^{(7)}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right], R_{2}^{(7)}=\left[\begin{array}{ccc}
1 & 1 & -\bar{\omega}_{7} \\
0 & -1 & 1 \\
0 & 0 & 1
\end{array}\right], \\
R_{3}^{(7)}=\left[\begin{array}{ccc}
1 & \bar{\omega}_{7} & -1 \\
0 & -1 & \omega_{7} \\
0 & 0 & 1
\end{array}\right] \quad \text { and } \quad T^{(7)}=\left[\begin{array}{ccc}
1 & 0 & i \sqrt{7} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] .
\end{gathered}$$

Theorem 4.5. Let $\mathcal{K}=\mathbb{Q}(\sqrt{-11})$ and let $\mathcal{O}_{11}=\mathbb{Z}\left[\omega_{11}\right]$, where $\omega_{11}=$ $\frac{1}{2}(1+i \sqrt{11})$, be the ring of integers of $\mathcal{K}$. Then the group $\operatorname{PU}\left(2,1, \mathcal{O}_{11}\right)$ is generated by the elements
$$I_{0}=\left[\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right], R_{1}^{(11)}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
0 & -1 & 0 \\
0 & 0 & 1
\end{array}\right], R_{2}^{(11)}=\left[\begin{array}{ccc}
1 & 1 & -\bar{\omega}_{11} \\
0 & -1 & 1 \\
0 & 0 & 1
\end{array}\right],$$
$$R_{3}^{(11)}=\left[\begin{array}{ccc}
1 & \bar{\omega}_{11} & -1-\bar{\omega}_{11} \\
0 & -1 & \omega_{11} \\
0 & 0 & 1
\end{array}\right] \quad \text { and } \quad T^{(11)}=\left[\begin{array}{ccc}
1 & 0 & i \sqrt{11} \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right] .$$
Remark. For other values of $d$ such that $\mathcal{O}_{d}$ has class number one, namely $d=19,43,67,163$, we can construct the same type of fundamental domain for $\left(\Gamma_{d}\right)_{\infty}$ in Heisenberg group as $\left(\Gamma_{11}\right)_{\infty}$. Although all generators as the above types lie in $P U\left(2,1 ; \mathcal{O}_{d}\right)$, there is no reason why adjoining $I_{0}$ to $\left(\Gamma_{d}\right)_{\infty}$ should continue to generate the full group $P U\left(2,1 ; \mathcal{O}_{d}\right)$. From the point of view of geometric, the largest radius of isometric sphere is always $\sqrt{2}$ while the shape of the fundamental domain and the length of Heisenberg translations become large as $d$ getting large. In contrast the radius of isometric spheres other than the largest are going to be smaller and smaller. Consequently the mount of isometric spheres containing the fundamental domain increases so rapidly with the value of $d$ that it seem to be done by another way. Furthermore, the method of [4] could not be extended to non-Euclidean Picard modular groups.

\section*{5. The determination of isometric spheres}

Recall that the Cygan sphere $\mathcal{B}_{0}$ is the isometric sphere of $I_{0}$. The boundary of $\mathcal{B}_{0}$ is called a spinal sphere [9] in Heisenberg group, we denote by $\mathcal{S}_{0}$ which is defined by
$$\mathcal{S}_{0}=\left\{(\zeta, t):\left||\zeta|^{2}+i t\right|=2\right\} .$$

Indeed we only need to consider the boundaries of isometric spheres in Heisenberg group because two isometric spheres have a non-empty interior intersection if and only if the boundaries have a non-empty interior intersection.
5.1. The case $\mathcal{O}_{2}$. In the cases of $\operatorname{PU}\left(2,1 ; \mathcal{O}_{1}\right)$ and $\operatorname{PU}\left(2,1 ; \mathcal{O}_{3}\right)$, all the vertices of the fundamental domain for the stabiliser of $q_{\infty}$ acting on $\partial \mathbf{H}_{\mathbb{C}}^{2}$ lie inside $\mathcal{S}_{0}$. For the group $P U\left(2,1 ; \mathcal{O}_{2}\right)$, it is not hard to show that six vertices of the prism $\boldsymbol{\Sigma}_{2}$ lie outside $\mathcal{S}_{0}$. Therefore we need to find more isometric spheres whose boundaries together with $\mathcal{S}_{0}$ contain the prism $\boldsymbol{\Sigma}_{2}$.

We consider the map
$$I_{0} R_{2}^{(2)} I_{0}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
-2 & -1 & 0 \\
-2 & -2 & 1
\end{array}\right],$$
whose isometric sphere which we denote by $\mathcal{B}_{1}$ is a Cygan sphere centred at the point (1, 0, 0) (in horospherical coordinates) with radius 1. The boundary of $\mathcal{B}_{1}$ is given by
$$\mathcal{S}_{1}=\left\{(\zeta, t):\left||\zeta-1|^{2}+i t+2 i \Im m \zeta\right|=1\right\} .$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-16.jpg?height=491&width=955&top_left_y=427&top_left_x=574}
\captionsetup{labelformat=empty}
\caption{Figure 5.1. (a) The shading view of neighboring spinal spheres containing the fundamental domain for $\left(\Gamma_{2}\right)_{\infty}$. (b) Another view for these spinal spheres.}
\end{figure}

Minimising the number of spinal spheres by the symmetry of $R_{1}^{(2)}$, it suffice to consider $\mathcal{S}_{0}$ and several images of $\mathcal{S}_{1}$ under some suitable elements in $\left(\Gamma_{2}\right)_{\infty}$, these are in Heisenberg coordinates given by
$$\begin{aligned}
T^{(2)}\left(\mathcal{S}_{1}\right) & =\left\{(\zeta, t):\left||\zeta-1|^{2}+i t-2 i \sqrt{2}+2 i \Im m \zeta\right|=1\right\}, \\
T^{(2)^{-1}}\left(\mathcal{S}_{1}\right) & =\left\{(\zeta, t):\left||\zeta-1|^{2}+i t+2 i \sqrt{2}+2 i \Im m \zeta\right|=1\right\}, \\
R_{1}^{(2)}\left(\mathcal{S}_{1}\right) & =\left\{(\zeta, t):\left||\zeta+1|^{2}+i t-2 i \Im m \zeta\right|=1\right\}, \\
T^{(2)^{-1}} R_{1}^{(2)}\left(\mathcal{S}_{1}\right) & =\left\{(\zeta, t):\left||\zeta+1|^{2}+i t+2 i \sqrt{2}-2 i \Im m \zeta\right|=1\right\} .
\end{aligned}$$
We claim that the prism $\boldsymbol{\Sigma}_{2}$ lies inside the union of $\mathcal{S}_{0}$ and these images of $\mathcal{S}_{1}$, see Figure 5.1 for viewing these spinal spheres.

Proposition 5.1. The prism $\boldsymbol{\Sigma}_{2}$ is contained in the union of the interiors of the spinal spheres $\mathcal{S}_{0}, \mathcal{S}_{1}, T^{(2)}\left(\mathcal{S}_{1}\right), T^{(2)^{-1}}\left(\mathcal{S}_{1}\right), R_{1}^{(2)}\left(\mathcal{S}_{1}\right)$ and $T^{(2)^{-1}} R_{1}^{(2)}\left(\mathcal{S}_{1}\right)$.
Proof. It suffices to show there exists three points $\left(v_{1}^{+}\right)^{(j)}(j=1,2,3)$ on the edges $\left(v_{1}^{+}, v_{1}^{-}\right),\left(v_{1}^{+}, v_{2}^{+}\right)$and $\left(v_{1}^{+}, v_{3}^{+}\right)$which lie in the intersection of the interiors of $\mathcal{S}_{0}$ and $\mathcal{S}_{1}$ such that the tetrahedron $\mathbb{T}\left(v_{1}^{+}\right)$with vertices $v_{1}^{+},\left(v_{1}^{+}\right)^{(1)},\left(v_{1}^{+}\right)^{(2)},\left(v_{1}^{+}\right)^{(3)}$ lies inside $\mathcal{S}_{1}$. By the same argument, we can also obtain other five tetrahedra $\mathbb{T}\left(v_{2}^{+}\right), \mathbb{T}\left(v_{3}^{+}\right), \mathbb{T}\left(v_{1}^{-}\right), \mathbb{T}\left(v_{2}^{-}\right), \mathbb{T}\left(v_{3}^{-}\right)$with apex $v_{2}^{+}, v_{3}^{+}, v_{1}^{-}, v_{2}^{-}, v_{3}^{-}$respectively such that $\mathbb{T}\left(v_{2}^{+}\right) \in \operatorname{Int}\left(T^{(2)}\left(\mathcal{S}_{1}\right)\right)$, $\mathbb{T}\left(v_{3}^{+}\right) \in \operatorname{Int}\left(R_{1}^{(2)}\left(\mathcal{S}_{1}\right)\right), \mathbb{T}\left(v_{1}^{-}\right) \in \operatorname{Int}\left(T^{(2)^{-1}}\left(\mathcal{S}_{1}\right)\right), \mathbb{T}\left(v_{2}^{-}\right) \in \operatorname{Int}\left(\mathcal{S}_{1}\right)$ and $\mathbb{T}\left(v_{3}^{-}\right) \in \operatorname{Int}\left(T^{(2)^{-1}} R_{1}^{(2)}\left(\mathcal{S}_{1}\right)\right)$. Moreover, the core part obtained by cutting off six the tetrahedra from the prism lies inside $\mathcal{S}_{0}$.

We shall prove the existence of the tetrahedron $\mathbb{T}\left(v_{1}^{+}\right)$and the others follow similarly. The edge joining $v_{1}^{+}$and $v_{1}^{-}$is contained the complex line
$\zeta=1-\sqrt{2} i / 2$ which is given by points with Heisenberg coordinates
$$\zeta=1-\sqrt{2} i / 2, \quad-\sqrt{2} \leq t \leq \sqrt{2} .$$
The edge joining $v_{1}^{+}$and $v_{2}^{+}$is given by points with Heisenberg coordinates
$$\Re e \zeta=1, \quad-\sqrt{2} / 2 \leq \Im m \zeta \leq \sqrt{2} / 2, \quad t=\sqrt{2} .$$
The edge joining $v_{1}^{+}$and $v_{3}^{+}$is given by points with Heisenberg coordinates
$$\Re e \zeta=-\sqrt{2} \Im m \zeta, \quad t=\sqrt{2} .$$
From (5.1) and (5.2), the points on the edge $\left(v_{1}^{+}, v_{1}^{-}\right)$lie in the intersection of the interiors of $\mathcal{S}_{0}$ and $\mathcal{S}_{1}$ if and only if
$$|3 / 2+i t|<2 \quad \text { and } \quad|1 / 2-(t-\sqrt{2}) i|<1 .$$
By an easy calculation, the inequalities (5.3) are equivalent to
$$\sqrt{2}-\sqrt{3} / 2<t<\sqrt{7} / 2 .$$

Using the same argument as above, we obtain that the points on the edge $\left(v_{1}^{+}, v_{2}^{+}\right)$lie in the intersection of the interiors of $\mathcal{S}_{0}$ and $\mathcal{S}_{1}$ if and only if $\Re e \zeta=1$, and $-\sqrt{\sqrt{2}-1}<\Im m \zeta<\delta_{1}$, where $\delta_{1} \approx-0.208$ is the largest real root of the equation $x^{4}+4 x^{2}+4 \sqrt{2} x+1=0$. The points on the edge $\left(v_{1}^{+}, v_{3}^{+}\right)$lie in the intersection of the interiors of $\mathcal{S}_{0}$ and $\mathcal{S}_{1}$ if and only if $\Re e \zeta=-\sqrt{2} \Im m \zeta$ and $-2^{1 / 4} / \sqrt{3}<\Im m \zeta<\delta_{2}$, where $\delta_{2} \approx-0.264$ is the largest real root of the equation $9 x^{4}+12 \sqrt{2} x^{3}+18 x^{2}+8 \sqrt{2} x+2=0$.

In term of these, we choose three points as $\left(v_{1}^{+}\right)^{(1)}=(1-\sqrt{2} i / 2,1)$ on the edge $\left(v_{1}^{+}, v_{1}^{-}\right),\left(v_{1}^{+}\right)^{(2)}=(1-i / 2, \sqrt{2})$ on the edge $\left(v_{1}^{+}, v_{2}^{+}\right)$and $\left(v_{1}^{+}\right)^{(3)}=$ $(\sqrt{2} / 2-i / 2, \sqrt{2})$ on the edge $\left(v_{1}^{+}, v_{3}^{+}\right)$, which are inside the intersection of the interiors of $\mathcal{S}_{0}, \mathcal{S}_{1}$ and also the vertex $v_{1}^{+}$lies inside $\mathcal{S}_{1}$. Therefore the tetrahedron $\mathbb{T}\left(v_{1}^{+}\right)$with the vertices $v_{1}^{+},\left(v_{1}^{+}\right)^{(1)},\left(v_{1}^{+}\right)^{(2)},\left(v_{1}^{+}\right)^{(3)}$ lies inside $\mathcal{S}_{1}$ by Lemma 4.1. \(\square\)
5.2. The case $\mathcal{O}_{7}$. In this case, the distance between the top and base of the fundamental domain for the stabiliser $\left(\Gamma_{7}\right)_{\infty}$ is greater than the diameter of $\mathcal{S}_{0}$, which implies that the prism $\boldsymbol{\Sigma}_{7}$ can not be contained inside $\mathcal{S}_{0}$ completely. Due to increasing the length of Heisenberg translations, only the images of $\mathcal{S}_{0}$ under the elements in $\left(\Gamma_{7}\right)_{\infty}$ could not cover the whole prism. We show that there are also isometric spheres with Cygan radius smaller than $\sqrt{2}$ whose centres are near to origin.

Therefore we consider the map
$$Q=I_{0} R_{2}^{(7)} I_{0}=\left[\begin{array}{ccc}
1 & 0 & 0 \\
1 & 1 & 0 \\
\bar{\omega}_{7} & 1 & 1
\end{array}\right] .$$
Consider the isometric spheres of $Q$ and $Q^{-1}$, which we denote by $\mathcal{B}_{2}$ and $\mathcal{B}_{3}$, respectively. The centre of $\mathcal{B}_{2}$ is $Q^{-1}(\infty)$, which is the point with horospherical coordinates $(1 / 4+i \sqrt{7} / 4, \sqrt{7} / 2,0)$ and the centre of $\mathcal{B}_{3}$, is $Q(\infty)$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-18.jpg?height=437&width=933&top_left_y=485&top_left_x=609}
\captionsetup{labelformat=empty}
\caption{Figure 5.2. (a) The shading view of neighboring spinal spheres containing the fundamental domain for $\left(\Gamma_{7}\right)_{\infty}$. (b) Another view for these spinal spheres.}
\end{figure}
which has horospherical coordinates $(1 / 4-i \sqrt{7} / 4, \sqrt{7} / 2,0)$. Both these isometric spheres have Cygan radius $\sqrt{2 /\left|\omega_{7}\right|}=2^{1 / 4}$. The boundaries of these isometric spheres $\mathcal{B}_{2}$ and $\mathcal{B}_{3}$ are in Heisenberg coordinates given by
$$\begin{aligned}
& \mathcal{S}_{2}=\left\{(\zeta, t):\left|\left|\zeta-\omega_{7} / 2\right|^{2}+i t+i \sqrt{7} / 2+i \Im m\left(\bar{\omega}_{7} \zeta\right)\right|=\sqrt{2}\right\}, \\
& \mathcal{S}_{3}=\left\{(\zeta, t):\left|\left|\zeta-\bar{\omega}_{7} / 2\right|^{2}+i t-i \sqrt{7} / 2+i \Im m\left(\omega_{7} \zeta\right)\right|=\sqrt{2}\right\} .
\end{aligned}$$

In order to cover the prim $\boldsymbol{\Sigma}_{7}$ by the spinal spheres, we use the symmetry property of $R_{1}^{(7)}$, it suffice to consider $\mathcal{S}_{0}, \mathcal{S}_{2}$ and images of $\mathcal{S}_{0}$ and $\mathcal{S}_{3}$ under suitable elements in $\left(\Gamma_{7}\right)_{\infty}$, these are points with Heisenberg coordinates given by
$$\begin{aligned}
R_{2}^{(7)}\left(\mathcal{S}_{0}\right)= & \left\{(\zeta, t):\left||\zeta-1|^{2}+i t-i \sqrt{7}+2 i \Im m \zeta\right|=4\right\}, \\
R_{2}^{(7)^{-1}}\left(\mathcal{S}_{0}\right)= & \left\{(\zeta, t):\left||\zeta-1|^{2}+i t+i \sqrt{7}+2 i \Im m \zeta\right|=4\right\}, \\
R_{2}^{(7)^{-1}}\left(\mathcal{S}_{3}\right)= & \left\{(\zeta, t):\left|\left|\zeta-\left(1+\omega_{7}\right) / 2\right|^{2}+i t+i \sqrt{7}\right.\right. \\
& \left.\quad+i \Im m\left(\left(1+\bar{\omega}_{7}\right) \zeta\right) \mid=\sqrt{2}\right\}, \\
R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right)= & \left\{(\zeta, t):\left|\left|\zeta+\bar{\omega}_{7} / 2\right|^{2}+i t-i \sqrt{7} / 2-i \Im m\left(\omega_{7} \zeta\right)\right|=\sqrt{2}\right\}, \\
R_{1}^{(7)} R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right)= & \left\{(\zeta, t):\left|\left|\zeta-\bar{\omega}_{7} / 2\right|^{2}+i t-i \sqrt{7} / 2+i \Im m\left(\omega_{7} \zeta\right)\right|=\sqrt{2}\right\} .
\end{aligned}$$

We claim that the prism $\boldsymbol{\Sigma}_{7}$ lies inside the union of $\mathcal{S}_{0}, \mathcal{S}_{2}$ and these images $R_{2}^{(7)}\left(\mathcal{S}_{0}\right), R_{2}^{(7)^{-1}}\left(\mathcal{S}_{0}\right), R_{2}^{(7)^{-1}}\left(\mathcal{S}_{3}\right), R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right), R_{1}^{(7)} R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right)$, see Figure 5.2 for viewing these spinal spheres.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-19.jpg?height=596&width=509&top_left_y=396&top_left_x=800}
\captionsetup{labelformat=empty}
\caption{Figure 5.3. A view of the decomposition for the prism $\boldsymbol{\Sigma}_{7}$ as several polyhedra.}
\end{figure}

Proposition 5.2. The prism $\boldsymbol{\Sigma}_{7}$ is contained in the union of the interiors of the spinal spheres $\mathcal{S}_{0}, \mathcal{S}_{2}, R_{2}^{(7)}\left(\mathcal{S}_{0}\right), R_{2}^{(7)^{-1}}\left(\mathcal{S}_{0}\right), R_{2}^{(7)^{-1}}\left(\mathcal{S}_{3}\right), R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right)$ and $R_{1}^{(7)} R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right)$.

Proof. It suffice to show that the prism $\boldsymbol{\Sigma}_{7}$ can be decomposed into several pieces as polyhedra such that each polyhedron lies inside a spinal sphere which is described in the proposition and the common face of two adjacent polyhedra lie in the intersection of the interior of two spinal spheres which contain these two polyhedra.

We need to add sixteen points on the faces of the prism $\boldsymbol{\Sigma}_{7}$ in order to decompose the prim into seven polyhedra, in Heisenberg coordinates, these are given by
$$\begin{array}{ll}
p_{1}=(1 / 4-i \sqrt{7} / 4,3 / 2), & p_{2}=(0.11-i 11 \sqrt{7} / 100,1.44+\sqrt{7} / 50), \\
p_{3}=(1 / 2,8 / 5), & p_{4}=(-1 / 10+i \sqrt{7} / 10, \sqrt{7}), \\
p_{5}=(-1 / 10+i \sqrt{7} / 10, \sqrt{7} / 2), & p_{6}=(3 / 4+i \sqrt{7} / 4,1.7), \\
p_{7}=(-1 / 4+i \sqrt{7} / 4,1), & p_{8}=(1 / 4-i \sqrt{7} / 4,-1), \\
p_{9}=(1 / 60-i \sqrt{7} / 60,-2 \sqrt{7} / 3), & p_{10}=(-1 / 20+i \sqrt{7} / 20,-\sqrt{7}), \\
p_{11}=(3 / 5+i \sqrt{7} / 10,-2 \sqrt{7} / 3), & p_{12}=(7 / 10+i \sqrt{7} / 5,-\sqrt{7}), \\
p_{13}=(3 / 4+i \sqrt{7} / 4,-2 \sqrt{7} / 3), & p_{14}=(5 / 12+i \sqrt{7} / 4,-2 \sqrt{7} / 3), \\
p_{15}=(1 / 4+i \sqrt{7} / 4,-\sqrt{7}), & p_{16}=(-1 / 4+i \sqrt{7} / 4,-1) .
\end{array}$$

We describe these polyhedra as follows:
\begin{itemize}
\item[(i)] The tetrahedron $\mathbb{T}$ with the vertice $v_{1}^{+}, p_{1}, p_{2}, p_{3}$;
\item[(ii)] The hexahedron $\mathbb{H}_{1}$ with the vertice $v_{1}^{+}, v_{2}^{+}, p_{2}, p_{3}, p_{4}, p_{5}, p_{6}$;
\item[(iii)] The pentahedron $\mathbb{P}_{1}$ with the vertice $v_{2}^{+}, p_{4}, p_{5}, p_{6}, v_{4}^{+}, p_{7}$;
\item[(iv)] The pentahedron $\mathbb{P}_{2}$ with the vertice $v_{1}^{-}, p_{8}, p_{9}, p_{10}, p_{11}, p_{12}$;
\item[(v)] The hexahedron $\mathbb{H}_{2}$ with the vertice $p_{9}, p_{10}, p_{11}, p_{12}, p_{13}, v_{2}^{-}, p_{14}, p_{15}$;
\end{itemize}
\begin{itemize}
\item[(vi)] The pentahedron $\mathbb{P}_{3}$ with the vertice $p_{9}, p_{10}, p_{14}, p_{15}, p_{16}, v_{4}^{+}$;
\item[(vii)] The octahedron $\mathbb{O}$ with the vertice $p_{1}, p_{2}, p_{3}, p_{5}, p_{6}, p_{7}, p_{8}, p_{9}, p_{11}$, $p_{13}, p_{14}, p_{16}$.
\end{itemize}

Note that the face $\left(p_{1}, p_{2}, p_{3}\right)$ of $\mathbb{T}$ and the face $\left(p_{2}, p_{3}, p_{5}, p_{6}\right)$ of $\mathbb{H}_{1}$ are on the face ( $p_{1}, p_{5}, p_{6}$ ) of $\mathbb{O}$; the common face ( $v_{2}^{+}, p_{4}, p_{5}, p_{6}$ ) of $\mathbb{H}_{1}$ and $\mathbb{P}_{1}$ is a vertical plane; the face $\left(p_{9}, p_{11}, p_{13}, p_{14}\right)$ of $\mathbb{H}_{2}$ is parallel to the base of the prism. Furthermore, the faces $\left(p_{9}, p_{10}, p_{11}, p_{12}\right)$ and $\left(p_{9}, p_{10}, p_{14}, p_{15}\right)$ are the trapeziums since the edge $\left(p_{9}, p_{11}\right)$ is parallel to $\left(p_{10}, p_{12}\right)$ and the edge $\left(p_{9}, p_{14}\right)$ is parallel to $\left(p_{10}, p_{15}\right)$.

By examining the location of the points and applying Lemma 4.1, we conclude that the tetrahedron $\mathbb{T}$ is inside the spinal sphere $R_{1}^{(7)} R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right)$; the hexahedron $\mathbb{H}_{1}$ is contained inside the spinal sphere $R_{2}^{(7)}\left(\mathcal{S}_{0}\right)$; the pentahedron $\mathbb{P}_{1}$ is inside $R_{3}^{(7)} R_{2}^{(7)}\left(\mathcal{S}_{3}\right)$; the pentahedron $\mathbb{P}_{2}$ is contained inside $R_{2}^{(7)^{-1}}\left(\mathcal{S}_{0}\right)$; the hexahedron $\mathbb{H}_{2}$ is contained inside $R_{2}^{(7)^{-1}}\left(\mathcal{S}_{3}\right)$; the pentahedron $\mathbb{P}_{3}$ is inside $\mathcal{S}_{2}$; the remaining octahedron $\mathbb{O}$ is inside $\mathcal{S}_{0}$; see Figure 5.3 for viewing the decomposition of the prism. \(\square\)
5.3. The case $\mathcal{O}_{11}$. In this case, we know that the fundamental domain for the stabiliser $\left(\Gamma_{11}\right)_{\infty}$ cannot be still inside $\mathcal{S}_{0}$ completely. The radius of spinal spheres other than the largest are so small that these spinal spheres are not much contribution to covering the prism $\boldsymbol{\Sigma}_{11}$. Due to the different shape of the prism $\boldsymbol{\Sigma}_{11}$ with the case $\mathcal{O}_{7}$, we only need to consider the largest spinal spheres which are the images of $\mathcal{S}_{0}$ under the elements of $\left(\Gamma_{11}\right)_{\infty}$. In order to determine a union of the spinal spheres which covering the prim $\boldsymbol{\Sigma}_{11}$, we minimise their numbers by the symmetry of $R_{1}^{(11)}$, it suffice to consider $\mathcal{S}_{0}$ and the images of $\mathcal{S}_{0}$ under suitable elements in $\left(\Gamma_{11}\right)_{\infty}$, these are in Heisenberg coordinates given by
$$\begin{aligned}
T^{(11)}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left||\zeta|^{2}+i t-2 i \sqrt{11}+2 i \Im m \zeta\right|=4\right\}, \\
R_{2}^{(11)}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left||\zeta-1|^{2}+i t-i \sqrt{11}+2 i \Im m \zeta\right|=4\right\}, \\
R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left||\zeta+1|^{2}+i t-i \sqrt{11}-2 i \Im m \zeta\right|=4\right\}, \\
R_{2}^{(11)^{-1}}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left||\zeta-1|^{2}+i t+i \sqrt{11}+2 i \Im m \zeta\right|=4\right\}, \\
R_{3}^{(11)}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left|\left|\zeta-\omega_{11}\right|^{2}+i t-i \sqrt{11}-2 i \Im m\left(\bar{\omega}_{11} \zeta\right)\right|=4\right\}, \\
R_{3}^{(11)^{-1}}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left|\left|\zeta-\omega_{11}\right|^{2}+i t+i \sqrt{11}-2 i \Im m\left(\bar{\omega}_{11} \zeta\right)\right|=4\right\}, \\
R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left|\left|\zeta+\bar{\omega}_{11}\right|^{2}+i t-i \sqrt{11}-2 i \Im m\left(\omega_{11} \zeta\right)\right|=4\right\}, \\
R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left|\left|\zeta-\bar{\omega}_{11}\right|^{2}+i t-i \sqrt{11}+2 i \Im m\left(\omega_{11} \zeta\right)\right|=4\right\}, \\
R_{1}^{(11)} R_{3}^{(11)^{-1}} R_{2}^{(11)}\left(\mathcal{S}_{0}\right) & =\left\{(\zeta, t):\left|\left|\zeta-\bar{\omega}_{11}\right|^{2}+i t+i \sqrt{11}+2 i \Im m\left(\omega_{11} \zeta\right)\right|=4\right\} .
\end{aligned}$$

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/b60ab03d-6aa0-4cc0-a22c-c792502f5417-21.jpg?height=434&width=931&top_left_y=464&top_left_x=591}
\captionsetup{labelformat=empty}
\caption{Figure 5.4. (a) The shading view of neighboring spinal spheres containing the fundamental domain for $\left(\Gamma_{11}\right)_{\infty}$. (b) Another view for these spinal spheres.}
\end{figure}

Definition 5.3. Let $X$ be a closed polygonal chain (not necessarily in a plane), then a topological disk defined by the cone over $X$ with apex $v$ is called a cone-polygon, denoted by $\mathbb{D}_{v}(X)$.

Note that a polygon in traditional sense can be interpreted as a conepolygon, in that case, the boundary of cone-polygon and the apex lie in the same plane and moreover the apex is in the interior of the boundary. We claim that the prism $\boldsymbol{\Sigma}_{11}$ lies inside the union of $\mathcal{S}_{0}$ and its images as above, see Figure 5.4 for viewing these spinal spheres.

Proposition 5.4. The prism $\boldsymbol{\Sigma}_{11}$ is contained in the union of the interiors of the spinal spheres $\mathcal{S}_{0}, T^{(11)}\left(\mathcal{S}_{0}\right), R_{2}^{(11)}\left(\mathcal{S}_{0}\right), R_{2}^{(11)^{-1}}\left(\mathcal{S}_{0}\right), R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$, $R_{3}^{(11)^{-1}}\left(\mathcal{S}_{0}\right), R_{1}^{(11)} R_{3}^{(11)^{-1}} R_{2}^{(11)}\left(\mathcal{S}_{0}\right), R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right), R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$.

Proof. Using the same argument of Proposition 5.2, we want to decompose the prism $\boldsymbol{\Sigma}_{11}$ into several polyhedral cells. The difference is the complicated intersection of the spinal spheres, which leads that the prism is difficultly decomposed into several polyhedral cells each of which is contained in one spinal sphere. Observe that a union of interiors of several spinal spheres is a star-convex set if they have a non-empty interior intersection. We shall show that the collection of these spinal spheres can be separated into several parts such that each part contains certain polyhedral cell. All these polyhedral cells are defined by the star-disk as its boundary.

We first define a tetrahedron $\mathbb{T}$ with vertices $v_{1}^{-}, q_{1}, q_{2}, q_{3}$, where
$$\begin{aligned}
& q_{1}=(1 / 4-i \sqrt{11} / 4,-2 \sqrt{11} / 3), \\
& q_{2}=(3 / 20-3 i \sqrt{11} / 20,-4 \sqrt{11} / 5), \\
& q_{3}=(7 / 20-3 i \sqrt{11} / 20,-9 \sqrt{11} / 10) .
\end{aligned}$$

Observe that the points $q_{1}, q_{2}, q_{3}$ lie on the edges $\left(v_{1}^{+}, v_{1}^{-}\right),\left(v_{1}^{-}, v_{3}^{-}\right)$and $\left(v_{1}^{-}, v_{2}^{-}\right)$, respectively. An easy calculation shows that this tetrahedron is contained inside $R_{1}^{(11)} R_{3}^{(11)^{-1}} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ by Lemma 4.1.

Next, we define a hexahedron $\mathbb{H}_{1}$ with vertices $q_{1}, q_{2}, q_{3}, q_{4}, q_{5}, q_{6}, q_{7}, v_{0}^{+}$ and another hexahedron $\mathbb{H}_{2}$ with vertices $v_{2}^{-}, q_{5}, q_{6}, q_{7}, q_{8}, q_{9}$, where
$$\begin{array}{ll}
q_{4}=(1 / 4-i \sqrt{11} / 4,-1 / 2), & q_{5}=(0.42+0.26 i,-0.71 \sqrt{11}+0.39), \\
q_{6}=(0.6+i \sqrt{11} / 10,-0.65 \sqrt{11}), & q_{7}=(0.58+2 i \sqrt{11} / 25,-1.92), \\
q_{8}=(3 / 4+i \sqrt{11} / 4,0), & q_{9}=(0.55+i \sqrt{11} / 4,-2 \sqrt{11} / 5) .
\end{array}$$

Observe that the points $q_{4}, q_{6}, q_{8}, q_{9}$ lie on the edges $\left(v_{1}^{+}, v_{1}^{-}\right),\left(v_{1}^{-}, v_{2}^{-}\right)$, $\left(v_{2}^{+}, v_{2}^{-}\right)$and $\left(v_{2}^{-}, v_{3}^{-}\right)$, respectively. The points $q_{5}$ lies on the interior of the base of the prism and $q_{7}$ lies on the interior of the face $\left(v_{1}^{+}, v_{1}^{-}, v_{2}^{-}, v_{2}^{+}\right)$. Then we know the hexahedron $\mathbb{H}_{1}$ has the faces $\left(q_{1}, q_{2}, q_{3}\right),\left(q_{1}, q_{3}, q_{6}, q_{7}, q_{4}\right)$, $\left(q_{1}, q_{2}, v_{0}^{+}, q_{4}\right),\left(q_{4}, q_{5}, v_{0}^{-}\right),\left(q_{4}, q_{5}, q_{7}\right)$ and $\left(q_{5}, q_{6}, q_{7}\right)$ and the hexahedron $\mathbb{H}_{2}$ has the faces $\left(q_{5}, q_{6}, q_{7}\right),\left(q_{5}, q_{7}, q_{8}\right),\left(v_{2}^{-}, q_{8}, q_{9}\right),\left(q_{5}, q_{8}, q_{9}\right)\left(q_{6}, q_{7}, q_{8}, v_{2}^{-}\right)$and $\left(q_{5}, q_{6}, v_{2}^{-}, q_{9}\right)$. By examining the location of these points and Lemma 4.1, we conclude that the hexahedron $\mathbb{H}_{1}$ is contained inside $R_{2}^{(11)^{-1}}\left(\mathcal{S}_{0}\right)$ and the hexahedron $\mathbb{H}_{2}$ is lied inside $R_{3}^{(11)^{-1}}\left(\mathcal{S}_{0}\right)$.

We focus on describing other polyhedral cells in the decomposition of the prism $\boldsymbol{\Sigma}_{11}$. Let $\mathcal{U}_{1}$ denote the union of $R_{2}^{(11)}\left(\mathcal{S}_{0}\right), R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$. We verify that $q_{10}=(0.2-0.4 i, 2.4)$ is in the intersection of the interiors of these three spinal spheres, which implies that $\mathcal{U}_{1}$ is a star-convex set about $q_{11}$. Analogously, we know $\mathcal{U}_{2}$, denoted by the union of $T^{(11)}\left(\mathcal{S}_{0}\right), R_{3}^{(11)}\left(\mathcal{S}_{0}\right), R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$, is a star-convex set about $q_{11}=(0.18+0.72 i, 4.8)$. This can be verified by examining the location of $q_{12}$ which is in the intersection of the interiors of these four spinal spheres. We need to add the following points on the faces of the prism $\boldsymbol{\Sigma}_{11}$, each of which is in the intersection of the interiors of at least two spinal spheres.
$$\begin{array}{ll}
q_{12}=(1 / 4-i \sqrt{11} / 4, \sqrt{11} / 2), & q_{13}=(0.21-0.21 i \sqrt{11}, \sqrt{11} / 2), \\
q_{14}=(0, \sqrt{11} / 2), & q_{15}=(-0.21+0.21 i \sqrt{11}, \sqrt{11} / 2), \\
q_{16}=(i \sqrt{11} / 4,1), & q_{17}=(3 / 4+i \sqrt{11} / 4,1), \\
q_{18}=(0.42-2 i \sqrt{11} / 25,1.95), & q_{19}=(3 / 4+i \sqrt{11} / 4, \sqrt{11}), \\
q_{20}=(0.6+i \sqrt{11} / 10,27 \sqrt{11} / 20), & q_{21}=(0.42+0.26 i, 1.29 \sqrt{11}+0.39), \\
q_{22}=(-1.4+1.4 i \sqrt{11}, 4 \sqrt{11} / 5), & q_{23}=(-1 / 4+i \sqrt{11} / 4, \sqrt{11} / 2) .
\end{array}$$

Observe that the points $q_{12}, q_{20}, q_{23}$ lie on the edges $\left(v_{1}^{+}, v_{1}^{-}\right),\left(v_{1}^{+}, v_{2}^{+}\right)$and $\left(v_{3}^{+}, v_{3}^{-}\right)$respectively and the points $q_{17}, q_{19}$ lie on the edge $\left(v_{2}^{+}, v_{2}^{-}\right)$. Moreover, the points $q_{13}, q_{14}, q_{15}, q_{22}$ lie on the interior of the face $\left(v_{1}^{+}, v_{1}^{-}, v_{3}^{-}, v_{3}^{+}\right)$, the point $q_{16}$ lies on the interior of the face $\left(v_{2}^{+}, v_{2}^{-}, v_{3}^{-}, v_{3}^{+}\right)$, the point $q_{18}$ lies on the interior of the face ( $v_{1}^{+}, v_{1}^{-}, v_{2}^{-}, v_{2}^{+}$) and the points $q_{21}$ lies on the interior of the top $\left(v_{1}^{+}, v_{2}^{+}, v_{3}^{+}\right)$. We need to add other three points in the
interior of the prism $\boldsymbol{\Sigma}_{11}$ which are used to define the cone-polygon,
$$\begin{aligned}
& q_{24}=(-0.16+0.74 i, 1.4), \\
& q_{25}=(0.328-0.28 i, 1.99), \\
& q_{26}=(0.325+0.29 i, 4.652) .
\end{aligned}$$

We verify the location of all these points as follows:
- The point $q_{12}$ is in the intersection of the interiors of $R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $\mathcal{S}_{0}$;
- The point $q_{13}$ is in the intersection of the interiors of $\mathcal{S}_{0}, R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{14}$ is in the intersection of the interiors of $\mathcal{S}_{0}, R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{15}$ is in the intersection of the interiors of $\mathcal{S}_{0}, R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$, $R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The points $q_{16}, q_{19}, q_{20}$ are in the intersection of the interiors of $R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{17}$ is in the intersection of the interiors of $\mathcal{S}_{0}$ and $R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{18}$ is in the intersection of the interiors of $\mathcal{S}_{0}, R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{21}$ is in the intersection of the interiors of $T^{(11)}\left(\mathcal{S}_{0}\right), R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{22}$ is in the intersection of the interiors of $R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$, $R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $v_{0}^{+}$is in the intersection of the interiors of $R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$, $T^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{23}$ is in the intersection of the interiors of $\mathcal{S}_{0}, R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{24}$ is in the intersection of the interiors of $\mathcal{S}_{0}, R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$, $R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{25}$ is in the intersection of the interiors of $\mathcal{S}_{0}, R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$, $R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{1}^{(11)} R_{3}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$;
- The point $q_{26}$ is in the intersection of the interiors of $T^{(11)}\left(\mathcal{S}_{0}\right), R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$, $R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$ and $R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$.

In term of these, we denote by $X_{1}$ a closed polygonal chain joining in order with the points $p_{12}, p_{13}, p_{14}, p_{15}, p_{16}, p_{17}, p_{18}$ and denote by $X_{2}$ a closed polygonal chain joining in order with the points $p_{16}, p_{19}, p_{20}, p_{21}, v_{0}^{+}$, $p_{22}, p_{24}$. So then we can define two cone-polygons $\mathbb{D}_{q_{25}}\left(X_{1}\right)$ and $\mathbb{D}_{q_{26}}\left(X_{2}\right)$. By examining the locations of these points, we show that $\mathbb{D}_{q_{25}}\left(X_{1}\right)$ is in the intersection of the interiors of $\mathcal{S}_{0}, \mathcal{U}_{1}$ and $\mathbb{D}_{q_{26}}\left(X_{2}\right)$ is in the intersection of
the interiors of $R_{2}^{(11)}\left(\mathcal{S}_{0}\right)$ and $T^{(11)}\left(\mathcal{S}_{0}\right), R_{1}^{(11)} R_{2}^{(11)}\left(\mathcal{S}_{0}\right), R_{3}^{(11)}\left(\mathcal{S}_{0}\right)$, namely, the intersection of the interiors of $\mathcal{U}_{1}$ and $\mathcal{U}_{2}$. The remaining faces can be easily verified which are contained inside $\mathcal{S}_{0}, \mathcal{U}_{1}$ or $\mathcal{U}_{2}$.

Finally, we define three polyhedral cells as follows:
\begin{itemize}
\item[(i)] The polyhedral cell $\mathbb{P}_{1}$ is defined by the faces $\mathbb{D}_{q_{25}}\left(X_{1}\right), \mathbb{D}_{q_{26}}\left(X_{2}\right)$, $\left(v_{1}^{+}, q_{12}, q_{18}, q_{17}, q_{19}, q_{20}\right),\left(v_{1}^{+}, q_{12}, q_{13}, q_{14}, q_{15}, q_{22}, v_{0}^{+}\right)$and $\left(v_{1}^{+}, q_{20}, q_{21}, v_{0}^{+}\right)$ as its boundary;
\item[(ii)] The polyhedral cell $\mathbb{P}_{2}$ is defined by the faces $\mathbb{D}_{q_{26}}\left(X_{2}\right),\left(q_{15}, q_{23}, q_{24}\right)$, $\left(v_{1}^{+}, q_{20}, q_{21}, v_{0}^{+}\right)\left(v_{1}^{+}, q_{12}, q_{18}, q_{17}, q_{19}, q_{20}\right),\left(v_{1}^{+}, q_{12}, q_{13}, q_{14}, q_{15}, q_{22}, v_{0}^{+}\right)$and $\left(q_{23}, q_{16}, q_{24}\right)$ as its boundary;
\item[(iii)] The polyhedral cell $\mathbb{P}_{3}$ is defined by the faces $\mathbb{D}_{q_{25}}\left(X_{1}\right),\left(q_{4}, q_{5}, q_{7}\right)$, $\left(q_{5}, q_{7}, q_{8}\right),\left(q_{4}, q_{5}, v_{0}^{-}\right),\left(q_{15}, q_{23}, q_{24}\right),\left(q_{8}, q_{9}, v_{3}^{-}, q_{23}, q_{16}, q_{17}\right),\left(q_{23}, q_{16}, q_{24}\right)$, $\left(q_{4}, q_{7}, q_{8}, q_{17}, q_{18}, q_{12}\right),\left(v_{3}^{-}, v_{0}^{-}, q_{5}, q_{9}\right)$ and $\left(q_{12}, q_{13}, q_{14}, q_{15}, q_{23}, v_{3}^{-}, v_{0}^{-}, q_{4}\right)$ as its boundary;
\end{itemize}

By Lemma 4.1 and the properties of star-convex of $\mathcal{U}_{1}$ and $\mathcal{U}_{2}$, we conclude that the polyhedral cell $\mathbb{P}_{1}$ contained inside $\mathcal{U}_{1}$; the polyhedral cell $\mathbb{P}_{2}$ contained inside $\mathcal{U}_{2}$; the polyhedral cell $\mathbb{P}_{3}$ is contained inside $\mathcal{S}_{0}$. This completes the proof. \(\square\)

\section*{References}
\begin{itemize}
\item[] [1] P. M. Cohn, A presentation for $S L_{2}$ for Euclidean quadratic imaginary number fields, Mathematika. 15(1968), 156"C163.
\item[] [2] M. Deraux, E. Falbel and J. Paupert. New constructions of fundamental polyhedra in complex hyperbolic space. Acta Math. 194(2005), no. 2, 155-201.
\item[] [3] B. Fine, Algebraic theory of the Bianchi groups, Marcel Dekker Inc. (1989).
\item[] [4] E. Falbel, G. Francsics, P. Lax and J. R. Parker. Generators of a Picard modular group in two complex dimensions. to appear in proc. AMS.
\item[] [5] E. Falbel and J. R. Parker. The Geometry of Eisenstein-Picard Modular Group. Duke Math. J. 131(2006), no. 2, 249-289.
\item[] [6] E. Falbel, G. Francsics and J. R. Parker. The geometry of the Gauss-picard modular group. Math Annalen. (pubilished online: 04 May 2010).
\item[] [7] G. Francsics and P. Lax. A semi-explicit fundamental domain for the Picard Modular Group in complex hyperbolic space. Contemporary Mathematics. 368(2005), 211-226.
\item[] [8] G. Francsics and P. Lax. An explicit fundamental domain for the Picard Modular Group in two complex dimensions. (Preprint 2005).
\item[] [9] W. M. Goldman. Complex Hyperbolic Geometry. (Oxford Mathematical Monographs, Oxford University Press 1999).
\item[] [10] W. M. Goldman and J. R. Parker, Complex hyperbolic ideal triangle groups, J. reine angewandte Math. 425(1992), 71-86.
\item[] [11] H. Garland and M. S. Raghunathan. Fundamental domains for lattices in (R-)rank 1 semisimple Lie groups. Ann. of Math. 92(1970), no.2, 279-326..
\item[] [12] G. D. Mostow. On a remarkable class of polyhedra in complex hyperbolic space. Pacific J. Mathematics. 86(1980), 171-276.
\item[] [13] J .R. Parker. Complex hyperbolic lattices. Contemporary Mathematics. 501(2009), 1-42.
\item[] [14] G. P. Scott. The geometries of 3-manifolds. Bull. London Math. Soc. 15(1983), 401-487.
\end{itemize}
[15] R. E. Schwartz. Complex hyperbolic triangle groups. Proc. of the intern. Congress of Mathematicians: Invited Lectures 1(2002), 339-350.
[16] I. N. Stewart and D. O. Tall, Algebraic number theory. Chapman and Hall Ltd. (1979).
[17] R.G. Swan, Generators and relations for certain special linear groups, Adv. in Math. 6(1971), 1-77.
[18] T. Zink. Üer die Anzahl der Spitzen einiger arithmetischer Untergruppen unitäer Gruppen. Math. Nachr. 89 (1979), 315-320.
[19] T. Zhao. A minimal volume arithmetic cusped complex hyperbolic orbifold. (Preprint).

Institut de Mathématiques, Université Pierre et Marie Curie, 4, place Jussieu, F-75252 Paris, France
E-mail address: zhao@math.jussieu.fr