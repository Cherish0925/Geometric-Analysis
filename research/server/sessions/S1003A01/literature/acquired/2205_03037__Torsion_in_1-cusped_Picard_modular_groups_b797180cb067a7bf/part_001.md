---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: [2205.03037] Torsion in 1-cusped Picard modular groups]

---
source_file: 2205_03037.pdf
converter: mathpix
format: mmd
---

\title{
TORSION IN 1-CUSPED PICARD MODULAR GROUPS
}

\author{
MARTIN DERAUX AND MENGMENG XU
}

\begin{abstract}
We present a systematic effective method to construct coarse fundamental domains for the action of the Picard modular groups $P U\left(2,1, \mathcal{O}_{d}\right)$ where $\mathcal{O}_{d}$ has class number one, i.e. $d=1,2,3,7,11,19,43,67,163$. The computations can be performed quickly up to the value $d=19$. As an application of this method, we classify conjugacy classes of torsion elements, deduce short presentations for the groups, and construct neat subgroups of small index.
\end{abstract}

\section*{1. Introduction}

The first goal of this paper is to study conjugacy classes of torsion elements in some Picard modular groups, which we write as $\Gamma_{d}=P U\left(2,1, \mathcal{O}_{d}\right)$, where $\mathcal{O}_{d}$ is the ring of algebraic integers in $\mathbb{Q}(i \sqrt{d})$, and $d$ is a square-free positive integer. We will mainly treat the cases where $\mathcal{O}_{d}$ is a Euclidean domain, i.e. for $d=1,2,3,7,11$; our methods are valid more generally in cases where $\mathcal{O}_{d}$ is a unique factorization domain, which is equivalent to $\Gamma_{d}$ having exactly one cusp. There are four value of $d$ where $\Gamma_{d}$ has one cusp but $\mathcal{O}_{d}$ is not Euclidean, namely $d=19,43,67$ and 163; even though our code runs in principle for these values, the computations tend to be very lengthy, and we only went through with the case $d=19$.

For $d=1$ and 3, most of what we do can be found by gathering several papers in the literature (see [13], [12], [8] and also [17]). For $d=1,3,7$, presentations were obtained by Mark-Paupert [21] using coarse fundamental domains coming from covering depth estimates. The first author explained in [10] how to push their method further in order to study torsion in $\Gamma_{7}$; at the time of that paper, we had not written computer code to handle more general values of $d$, which is now settled for 1-cusped Picard modular groups.

For $d=2$ and 11, presentations were worked out by Polletta [26] (without mention of the classification of conjugacy classes of torsion elements).

Matthew Stover pointed out to us that (conjugacy classes of) torsion elements for all Picard modular groups $\Gamma_{d}$ were listed by Feustel (see [15], and also [14], [17]). Feustel's method is very different from ours, and at the time of his paper no explicit presentation for these groups was known, so his work cannot be used directly for studying general torsion-free subgroups. In particular, without our work, it would not at all be obvious to relate Feustel's work to the presentations worked out by Mark-Paupert and Polletta.

As far as we know, no explicit presentation for $\Gamma_{d}$ has appeared in the literature for $d>11$, so our results for $d=19$ are entirely new. For $d=43$ and 67, we were unable to

\footnotetext{
Date: Oct 18, 2022.
}
go through with all the computations, but we did obtain explicit presentations (see [9]). For $d=163$ even the covering depth is unknown at present.

We will give two applications of our classification of isotropy groups for the action of $\Gamma_{d}$ on the complex hyperbolic plane. One is the determination of short presentations for these groups, using presentations for isotropy groups (see sections 9 and 10).

As a second application, we explain how to use group-theory software (GAP or Magma) to find explicit neat subgroups of $\Gamma_{d}$ of small index, see section 8. Recall that a neat lattice in $P U(2,1)$ is a torsion-free subgroup whose cusps groups (maximal parabolic subgroups) can be realized by unipotent groups. The "torsion-free" requirement is equivalent to the fact that group acts without fixed points on the complex 2-ball (i.e. the quotient is a smooth complex hyperbolic surface). The second requirement is equivalent to the existence of a smooth compactification of the quotient by elliptic curves (see [3] for arithmetic lattices and [22] for the general case).

Of course every lattice contains many neat subgroups. Indeed, by a classical result of Selberg (see [28] or [1]), one can take subgroups obtained as the congruence kernel modulo a suitable prime ideal (these are called principal congruence subgroups). Note however that torsion-free/neat congruence subgroups in $\Gamma_{d}$ tend to have fairly large index; we would like to find neat subgroups of smallest possible index.

The basic method we use in order to obtain subgroups of "small" index is to start with a given neat normal subgroup $K \subset \Gamma_{d}$, and to try and enlarge it by replacing it by $\phi^{-1}(S)$ for some non-trivial subgroup $S \subset F=\Gamma_{d} / K$ (see section 8 for more details). In order to get the initial normal subgroup, we use either computational group-theory software (Magma), or congruence subgroups.

A basic lower bound for the index of a torsion-free subgroup is deduced from the fact that the index of a torsion-free subgroup must be a multiple of the least common multiple of the orders finite subgroups (see Proposition (2.1) in [11] for instance). We will refer to this as the obvious lower bound.

Note that for subgroups of $P S L_{2}(\mathbb{R})=P U(1,1)$, the obvious lower bound is essentially (i.e. up to a factor of 2) the minimal index of a torsion-free subgroup, see [11]. For $P S L_{2}(\mathbb{C})=\operatorname{Isom}\left(H_{\mathbb{R}}^{3}\right)$ however, there are lattices where the ratio between the minimal index and the obvious lower bound is aribitrarily large (see [19]). In general very little is known about the minimal index of torsion-free subgroups of lattices.

The obvious lower bound is actually realized for $d=1$ and 3 (at least for $d=3$, this is well-known to experts, see [24], [30]). For other values of $d$, we could only find subgroups of index strictly larger than the obvious lower bound (see Table 15). In fact for $d=2$ and 7, the index we found is twice the obvious lower bound, whereas for $d=11$ and 19, the index of the neat subgroups we found is quite a bit larger than the obvious lower bound (note however that in these last cases, $\Gamma_{d}$ seems to contain too many subgroups for our methods to be efficient).

Acknowledgements: The first author would like to thank Matthew Stover for useful discussions around the results in this paper, and for pointing our attention to the results by Feustel and Holzapfel. He also acknowledges support from INRIA, in the form of a
research semester in the "Ouragan" team, and thanks Fabrice Rouillier and Owen Rouillé for useful discussions related to this project. The second author is grateful for the support of China Scholarship Council (CSC Grant No. 202006130069) and the encouragement from Yueping Jiang. She also grateful for the hospitality of the Institut Fourier, where most of this work was done. Finally, the authors thank the anonymous referees, whose suggestions helped improving earlier versions of the manuscript.

Conflict of interest: The authors declare that they have no conflict of interest in publishing this work.

\section*{2. Background and notation}
2.1. The complex hyperbolic plane. In this section we review basics of complex hyperbolic geometry, using notation close to [21], [10]. We refer to [16] for more detail.

On the complex vector space $V=\mathbb{C}^{3}$, we define the Hermitian form $\langle v, w\rangle=w^{*} J v$, where
$$J=\left(\begin{array}{lll}
0 & 0 & 1 \\
0 & 1 & 0 \\
1 & 0 & 0
\end{array}\right) .$$
Note that this Hermitian form has signature (2, 1), so the unitary group $U(J)=\{A \in$ $\left.G L(V): A^{*} J A=J\right\}$ is isomorphic to $U(2,1)$.

We write $p: V \backslash\{0\} \rightarrow \mathbb{P}(V)$ for projectivization, i.e. $p(v)=\mathbb{C} v$ is the complex line spanned by $v$, and write $V_{-}=\{v \in V:\langle v, v\rangle<0\}, V_{0}=\{v \in V:\langle v, v\rangle=0\}$. Vectors in $V_{-}$(resp. $V_{0}$ ) are called negative (resp. isotropic).

As a set the complex hyperbolic plane $\mathbf{H}_{\mathbb{C}}^{2}$ is given by $p\left(V_{-}\right)$, which clearly admits an action of $P U(J)$ (namely the one induced by the action of $G L(V)$ on $V$, which preserves $V_{-}$).

There is a unique (up to scaling) invariant Kähler metric on $\mathbf{H}_{\mathbb{C}}^{2}$, and it has constant negative holomorphic sectional curvature. In this paper, we will not need the expression of that Kähler metric, but we will use the formula for the corresponding Riemannian distance function. When the holomorphic sectional curvature is normalized to be -1, the Riemannian distance $\rho(x, t)$ between $x=p(v)$ and $y=p(w)$ is given by
$$\cosh \left(\frac{1}{2} \rho(x, y)\right)=\frac{|\langle v, w\rangle|}{\sqrt{\langle v, v\rangle\langle w, w\rangle}} .$$

The set $p\left(V_{0}\right)$ is usually called the boundary of the complex hyperbolic plane, and we denote it by $\partial \mathbf{H}_{\mathbb{C}}^{2}$. The points of $\partial \mathbf{H}_{\mathbb{C}}^{2}$ are called ideal points.

For every $v=\left(v_{1}, v_{2}, v_{3}\right) \in V$ such that $v_{3} \neq 0$, the complex line $\mathbb{C} v$ is spanned by a unique vector of the form $\left(z_{1}, z_{2}, 1\right)$, namely $\left(v_{1} / v_{3}, v_{2} / v_{3}, 1\right)$; the pair $\left(z_{1}, z_{2}\right)$ then gives affine coordinates such that the complex hyperbolic plane is described as the subset of $\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}$ satisfying
$$2 \Re\left(z_{1}\right)+\left|z_{2}\right|^{2}<0,$$
a region which is known as the Siegel half space.

When $v_{3}=0$, the only vectors $v=\left(v_{1}, v_{2}, 0\right)$ that are in $V_{-} \cup V_{0}$ are proportional to $q_{\infty}=(1,0,0)$, and it is natural to call $q_{\infty}$ the "point at infinity" for the above affine coordinates. In what follows, with a slight abuse of notation, we will write $q_{\infty}$ instead of $p\left(q_{\infty}\right)$.

Another important set of coordinates are horospherical coordinates, obtained by studying the stabilizer of $(1,0,0)$ in $U(J)$. It is easy to check that unipotent upper triangular matrices preserve $J$ if and only if they are of the form
$$T(z, t)=\left(\begin{array}{ccc}
1 & -\bar{z} & \frac{-|z|^{2}+i t}{2} \\
0 & 1 & z \\
0 & 0 & 1
\end{array}\right)$$
for some $z \in \mathbb{C}, t \in \mathbb{R}$. Moreover, these matrices form a subgroup of $U(J)$, in fact we have $T(z, t) T\left(z^{\prime}, t^{\prime}\right)=T\left(z+z^{\prime}, t+t^{\prime}+2 \Im\left(z \bar{z}^{\prime}\right)\right)$.

The corresponding group law on $\mathbb{C} \times \mathbb{R}$
$$(z, t) \star\left(z^{\prime}, t^{\prime}\right)=\left(z+z^{\prime}, t+t^{\prime}+2 \Im\left(z \bar{z}^{\prime}\right)\right)$$
is often call the Heisenberg group law. The matrices $T(z, t)$ are called Heisenberg translations. Note that the center of the Heisenberg group is given by $\{0\} \times \mathbb{R}$, and these are sometimes called vertical translations.

The above group of unipotent matrices acts simply transitively on $\partial \mathbf{H}_{\mathbb{C}}^{2} \backslash\left\{q_{\infty}\right\}$. This suggests using $(z, t) \in \mathbb{C} \times \mathbb{R}$ as coordinates on $\partial \mathbf{H}_{\mathbb{C}}^{2} \backslash\left\{q_{\infty}\right\}$. These in fact extend to coordinates on $\mathbf{H}_{\mathbb{C}}^{2}$, by writing $\left(z_{1}, z_{2}\right)=\left(\frac{-|z|^{2}+i t-u}{2}, z\right)$, where $z \in \mathbb{C}, t, u \in \mathbb{R}$. Note that the point $\left(\frac{-|z|^{2}+i t-u}{2}, z\right)$ is in $\mathbf{H}_{\mathbb{C}}^{2}$ (resp. $\partial \mathbf{H}_{\mathbb{C}}^{2}$ ) if and only if $u>0$ (resp. $u=0$ ). The parameter $u$ is called "horospherical height", and the level sets $u=u_{0}$ (resp. the sup-level sets $u \geq u_{0}$ ) are called horospheres (resp. horoballs) based at $q_{\infty}$.

The full parabolic stabilizer of $q_{\infty}=(1,0,0)$ is larger than the above unipotent subgroup, it is generated by the unipotent stabilizer and the subgroup of Heisenberg rotations, which are given by the diagonal matrices
$$R_{w}=\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & w & 0 \\
0 & 0 & 1
\end{array}\right)$$
where $w \in \mathbb{C},|w|=1$. The matrices of the form $R_{w} T(z, t)$ with $w \neq 1$ are called twist parabolic elements.

Heisenberg translations and rotations preserve the Cygan metric, which is defined for $(z, t)$ and $\left(z^{\prime}, t^{\prime}\right) \in \mathbb{C} \times \mathbb{R}$ by:
$$\begin{aligned}
d_{C}\left((z, t),\left(z^{\prime}, t^{\prime}\right)\right) & =| | z-\left.z^{\prime}\right|^{4}+\left.\left|t-t^{\prime}+2 \Im\left(z \overline{z^{\prime}}\right)\right|^{2}\right|^{1 / 4} \\
& =\left|2\left\langle\psi(z, t, 0), \psi\left(z^{\prime}, t^{\prime}, 0\right)\right\rangle\right|^{1 / 2},
\end{aligned}$$
where
$$\psi(z, t, u)=\left(\begin{array}{c}
\left(-|z|^{2}+i t-u\right) / 2 \\
z \\
1
\end{array}\right) .$$

The Cygan metric is the restriction to $\mathbb{C} \times \mathbb{R}$ of the extended Cygan metric, which is defined for $(z, t, u)$ and $\left(z^{\prime}, t^{\prime}, u^{\prime}\right) \in \mathbb{C} \times \mathbb{R} \times \mathbb{R}_{\geq 0}$ by
$$d_{C y}\left((z, t, u),\left(z^{\prime}, t^{\prime}, u^{\prime}\right)\right)=\left|\left(\left|z-z^{\prime}\right|^{2}+\left|u-u^{\prime}\right|\right)^{2}+\left|t-t^{\prime}+2 \Im\left(z \overline{z^{\prime}}\right)\right|^{2}\right|^{1 / 4} .$$
When at least one of $u, u^{\prime}$ is 0 , we get:
$$d_{C y}\left((z, t, u),\left(z^{\prime}, t^{\prime}, u^{\prime}\right)\right)=\left|2\left\langle\psi(z, t, u), \psi\left(z^{\prime}, t^{\prime}, u^{\prime}\right)\right\rangle\right|^{1 / 2} .$$
Given $A \in U(2,1)$, we define the isometric sphere of $A$ to be given by
$$I(A)=\left\{p(V) \in \mathbf{H}_{\mathbb{C}}^{2}:\left|\left\langle V, q_{\infty}\right\rangle\right|=\left|\left\langle V, A\left(q_{\infty}\right)\right\rangle\right|\right\} .$$

Definition 2.1. Let $\Gamma \subset P U(J)$ be a discrete subgroup. The Ford domain for $\Gamma$ is defined by
$$F_{\Gamma}=\left\{p(x) \in \mathbf{H}_{\mathbb{C}}^{2}:\left|\left\langle x, q_{\infty}\right\rangle\right| \leq\left|\left\langle x, A q_{\infty}\right\rangle\right| \text { for all } A \in \Gamma\right\} .$$

It is a standard fact that $F_{\Gamma}$ is a fundamental domain for the action of $\Gamma$ modulo the action of the stabilizer $\operatorname{Stab}_{\Gamma}\left(q_{\infty}\right)$, in the sense that its images under the group tile $\mathbf{H}_{\mathbb{C}}^{2}$ and $\gamma F_{\Gamma} \cap F_{\Gamma}$ has non-empty interior if and only if $\gamma$ fixes $q_{\infty}$ (see [4] for instance). In order to get an actual fundamental domain, we need to intersect $F_{\Gamma}$ with a fundamental domain for the action of $\operatorname{Stab}_{\Gamma}\left(q_{\infty}\right)$.

Note that it can be delicate to determine the combinatorics of $F_{\Gamma}$ explicitly, and in fact the point of the methods developed in [21] is to avoid working out the combinatorial structure of the Ford domain.

It turns out (see Proposition 4.3 of [20]) that the isometric sphere of a group element is actually a sphere for the Cygan metric, whose radius and center can be obtained from a matrix representative, as stated in Lemma 2.1.

Lemma 2.1. Let $A \in U(2,1)$, and suppose $q_{\infty}$ is not fixed by $A$. Then $I(A)$ is equal to the extended Cygan sphere $\mathcal{S}_{A}$ with center $A\left(q_{\infty}\right)$ and radius $\sqrt{2 /\left|A_{3,1}\right|}$.

From this, it also follows that the Ford domain $F_{\Gamma}$ can also be thought of as the intersection of the exteriors of the Cygan spheres $\mathcal{S}_{A}$ for all elements $A \in \Gamma$ not fixing the point at infinity.
2.2. Picard modular groups. In this section, we let $d>0$ be a square-free integer, and write $\mathbb{K}_{d}=\mathbb{Q}(i \sqrt{d}), \mathcal{O}_{d}$ for the ring of algebraic integers in $\mathbb{K}_{d}$. Recall that $\mathcal{O}_{d}=\left\{a+b \tau_{d}:\right.$ $a, b \in \mathbb{Z}\}$, where $\tau_{d}=\frac{1+i \sqrt{d}}{2}$ if $d \equiv 3 \bmod 4$, and $\tau_{d}=i \sqrt{d}$ otherwise.

Recall that for most values of $d$, the only units in $\mathcal{O}_{d}$ are $\pm 1$; the only exceptions are the cases $d=1$ (where the units are the 4-th roots of unity) and $d=3$ (where units are the 6-th roots of unity).

We now consider $U\left(J, \mathcal{O}_{d}\right)=U(J) \cap G L_{3}\left(\mathcal{O}_{d}\right)$, and write $\Gamma_{d}=P U\left(J, \mathcal{O}_{d}\right)$. These are often called Picard modular groups.

It follows from a very general result of Borel-Harish Chandra [6] that $\Gamma_{d}$ is a lattice in $P U(J)$, i.e. the quotient $\Gamma_{d} \backslash \mathbf{H}_{\mathbb{C}}^{2}$ has finite volume. It follows from thick-thin decomposition that the quotient has finitely many ends, the ends corresponding to conjugacy classes of maximal parabolic subgroups in $\Gamma_{d}$. Moreover these maximal parabolic subgroups are
given by the stabilizers in $\Gamma_{d}$ of $\mathbb{K}_{d}$-rational points (see [5]), i.e. vectors in $\mathbb{P}(V)$ that can be represented by a vector in $\mathcal{O}_{d}^{3}$.

The following result is well known.
Theorem 2.1. (Feustel [18], Zink [31]) The number of ends of the quotient $\Gamma_{d} \backslash \mathbf{H}_{\mathbb{C}}^{2}$ is given by the class number of $\mathbb{K}_{d}$.

From now on, we always assume that the class number of $\mathbb{K}_{d}$ is one, which is equivalent to requiring that $\mathcal{O}_{d}$ is a unique factorization domain. There are finitely many values of $d$ such that this happens, namely $d=1,2,3,7,11,19,43,67,163$ (note that $\mathcal{O}_{d}$ is in fact a Euclidean ring if and only if $=1,2,3,7,11$ ).

We briefly review some terminology from [21] (see also [10]). A vector $v \in \mathcal{O}_{d}^{3}$ is called primitive if for every $0 \neq \alpha \in \mathcal{O}_{d}, \frac{1}{\alpha} v \in \mathcal{O}_{d}$ implies that $\alpha$ is a unit. Since we assume $\mathcal{O}_{d}$ is a unique factorization domain, this is equivalent to requiring that the greatest common divisor of the standard coordinates $v_{1}, v_{2}, v_{3}$ is 1 . Moreover, every $\mathbb{K}_{d}$-rational point in $\mathbb{P}(V)$ has a primitive representative, and that representative is unique up to multiplication by a unit in $\mathcal{O}_{d}$.

This ensures that the following definition is meaningful.
Definition 2.2. The depth of an $\mathcal{O}_{d}$-rational point $x$ is given by $\left|\left\langle v, q_{\infty}\right\rangle\right|^{2}=\left|v_{3}\right|^{2}$, where $v$ is any primitive integral lift of $x$.

In fact the possible depths of rational points are precisely rational integers that are norms in $\mathcal{O}_{d}$.

By extension, we will also talk about the depth of an element $A \in U(J)$, defined to be the depth of $A\left(q_{\infty}\right)$. Note that $A\left(q_{\infty}\right)$, which is the first column of $A$, is a primitive integral vector (this can easily be seen from the fact that $A^{*} J A=J$ ).

Note in particular that, by Lemma 2.1, the depth $N$ of an element $A \in U(J)$ is closely related to the radius of the Cygan sphere $\mathcal{S}_{A}$, which is given by $(4 / N)^{1 / 4}$.

The following result is easy to see from equation 2, we will use it throughout the paper (see also Lemma 4 in [21]).

Proposition 2.2. Let $A \in U(J)$ be an element of depth $N$. Then the maximum horo-spherical height of the Cygan sphere $\mathcal{S}_{A}$ is given by $2 / \sqrt{N}$.
2.3. Cusps of Picard modular groups. We write $\Gamma_{d}^{(\infty)}$ for the stabilizer of $q_{\infty}$ in $\Gamma_{d}$. Explicit generators for $\Gamma_{d}^{(\infty)}$ as well as a fundamental domain for its action in $\mathbb{C} \times \mathbb{R}$ (hence on any horosphere based at $q_{\infty}$ ) can be found in [25] (see also [21]), we simply state their result without proof.

Note that the cases $d=1$ and $d=3$ are special because of the presence of non-trivial units, and the case $d=2$ is quite different from the cases $d \geq 7$ because of the congruence class of $d \bmod 4$.

The fundamental domain can be chosen to be a prism $P=T \times[0,2 \sqrt{d}]$ with base a triangle $T$ with vertices $0, \lambda, \mu$ where $\lambda \in \mathbb{R}_{+}$. The values of $\lambda, \mu$ depend on $d$ in the following manner.

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline $d$ & $\lambda$ & $\mu$ \\
\hline 1 & 1 & $1+i$ \\
\hline 2 & 2 & $i \sqrt{2}$ \\
\hline 3 & 1 & $\frac{1+\tau_{3}}{3}$ \\
\hline $\mathrm{d}=7,11,19,43,67,163$ & 1 & $\tau_{d}$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1. The base of the fundamental prism for the action is the triangle with vertices $0, \lambda, \mu$.}
\end{table}

Explicit generating sets for $\Gamma_{d}^{(\infty)}$ are described in [25]. The vertical generator is always given by $T_{v}=T(0,2 \sqrt{d})$. We list non-vertical generators in Table 2, each generator being given in the form $T(z, t)$ for $(z, t) \in \mathbb{C} \times \mathbb{R}$ (see equation (1)). Note that these generating

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $d$ & $r$ & $T_{r}$ & $\mu$ & $T_{\mu}$ \\
\hline 1 & 2 & $T(2,0)$ & $1+i$ & $T(1+i, 0)$ \\
\hline 2 & 2 & $T(2,0)$ & $i \sqrt{2}$ & $T(i \sqrt{2}, 0)$ \\
\hline 3 & 1 & $T(1, i \sqrt{3})$ & $\tau_{3}$ & $T\left(\tau_{3}, i \sqrt{3}\right)$ \\
\hline 7 & 1 & $T(1, i \sqrt{7})$ & $\tau_{7}$ & $T\left(\tau_{7}, 0\right)$ \\
\hline $d=11,19,43,67,163$ & 1 & $T(1, i \sqrt{d})$ & $\tau_{d}$ & $T\left(\tau_{d}, i \sqrt{d}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 2. Non-vertical generators for $\Gamma_{d}^{(\infty)}$.}
\end{table}
sets do not give side-pairing maps for $P$, hence we briefly explain how to bring a given point $(z, t) \in \mathbb{C} \times \mathbb{R}$ back to the fundamental prism $P$. In what follows, we refer to the $\mathbb{C}$ (resp. $\mathbb{R}$ ) factor as the horizontal (resp. vertical) factor.

The rough idea is to adjust the horizontal factor by using powers of $T_{r}$ and $T_{\mu}$, then adjusting the vertical factor by using powers of $T_{v}$. We now briefly explain the details of this procedure.

In order handle the horizontal factor, we write the parallelogram spanned by $r$ and $\mu$ as a union of explicit images of the triangular base $T$ of $P$, as illustrated in Figure 1 for various values of $d$. Write $z=r \alpha+\beta \mu$ for some $\alpha, \beta \in \mathbb{R}$, and compute $a=\lfloor\alpha\rfloor$ and $b=\lfloor\beta\rfloor$ (note that we will only perform such floor/ceiling calculations when $\alpha, \beta$ are real algebraic numbers, so the result can be certified with a computer).

By replacing $(z, t)$ by the Heisenberg coordinates of $T_{\mu}^{-b} T_{r}^{-a} V(z, t)$, we may assume that $z$ is in the parallelogram spanned by $r$ and $\mu$. Applying a suitable element of $\Gamma_{d}^{(\infty)}$ if necessary (see Figure 1), we may assume that $z$ is in the triangle with vertices $0, \lambda, \mu$. Finally, applying a suitable power of $T_{v}$, we can ensure that $t$ is in the interval $[0,2 \sqrt{d}]$.

Note that using the above method, we find one element of $\Gamma_{d}^{(\infty)}$ that brings our point to $P$, but in general there can be several such elements. In fact, if the corresponding point is in the interior of $P$, then the element is unique. If the image point is in the boundary of $P$, even though there can be several choices of elements of $\Gamma_{d}^{(\infty)}$, it is straightforward to write a computer program that lists all possibilities.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/7ad514d5-990b-4daa-af63-f886c10c9636-08.jpg?height=942&width=1378&top_left_y=315&top_left_x=399}
\captionsetup{labelformat=empty}
\caption{Figure 1. Cutting the basic parallelogram as a union of the triangle $T$, which is the base of the prism $P$.}
\end{figure}

Using the above, it is also easy to write code to check whether two points are equivalent under the action of the standard cusp group $\Gamma_{d}^{(\infty)}$, and if so, to list all elements of $\Gamma_{d}^{(\infty)}$ that map one to the other. Note that this works for ideal points, but also for pairs of points with the same horospherical height.

Finally, we mention that with the above method, we are able to list, for each depth $N$, a single representative of every $\Gamma_{d}^{(\infty)}$-orbit of rational points of depth $N$ (we will choose a representative whose Heisenberg coordinates are inside the prism $P$ ).

\section*{3. Estimates for cusp elements}

As mentioned in [10], in order to make our methods effective, we will need a priori bounds on the rational points that are useful to perform the computations. We will use two basic bounds.

One is the list of $\mathbb{K}_{d}$-rational points of depth $\leq N$ such that the corresponding Cygan sphere intersects the prism $P$ at a given horospherical height $u_{0}$.

The other bound will be associated to pairs of Cygan spheres $\mathcal{S}_{1}, \mathcal{S}_{2}$ associated two rational points $p_{1}, p_{2}$ in the prism $P$. Given two such points, we will need a bound on the cusp elements $\alpha$ such that $\alpha\left(\mathcal{S}_{1}\right)$ intersects $\mathcal{S}_{2}$.

In both cases, rather than finding the precise list of cusp elements satisfying a property, we will find an explicit finite set that contains all the cusp elements safisfying that property.

Even though the precise list could in principle be deduced from that upper bound, this is not efficient in practice, because it would take too much computation time.

We now sketch one way to get such bounds. We only explain the first bound, the second one is similar; in fact, since we our methods only require to consider images of Cygan spheres $\alpha\left(\mathcal{S}_{1}\right)$ that intersect both $S_{2}$ and the prism $P$, we can use the first bound, and then use a simple triangle inequality estimate for the second (if $\alpha\left(\mathcal{S}_{1}\right) \cap S_{2} \neq \emptyset$, then $d_{C y}\left(\alpha\left(p_{1}\right), p_{2}\right)<r_{1}+r_{2}$, where $r_{j}$ is the Cygan radius of $S_{j}$ ).

For computational purposes, it is convenient to use slightly modified Heisenberg coordinates, in order to get the Cygan spheres bounding the Ford domain to have equations given by polynomials with $\mathbb{Z}$-coefficients.

Accordingly, we scale the vertical Heisenberg coordinate by $\sqrt{d}$ and use $\tilde{t}=t / \sqrt{d}$. The corresponding scaled Heisenberg coordinates $(z, \tilde{t})$ of $v=\left(v_{0}, v_{1}, v_{2}\right)$ then satisfy
$$\begin{gathered}
\frac{v_{0}}{v_{2}}=\frac{-|z|^{2}+i \tilde{t} \sqrt{d}}{2} \\
\frac{v_{1}}{v_{2}}=z
\end{gathered} .$$

In the following, we denote by $\mathcal{S}_{V}$ the Cygan sphere corresponding to a given a primitive integral vector $V=\left(v_{0}, v_{1}, v_{2}\right) \in \mathcal{O}_{d}$. We wish to find restrictions on $V$ under the hypotheses that $\mathcal{S}_{V}$ intersects the cone over $P$ from $q_{\infty}$ at a given horospherical height $u_{0}$. More precisely, let $u_{0}>0$ and consider the vertical translation $P_{u_{0}}$ of $P$ at horospherical height $u$, i.e. the set of points in $\mathbf{H}_{\mathbb{C}}^{2}$ with horospherical coordinates $\left(z, t, u_{0}\right)$ such that $(z, t) \in P$. Then we have the following.

Proposition 3.1. Let $N \in \mathbb{N}^{*}$, and let $u_{0} \in \mathbb{R}, u_{0}>0$. Then there are only finitely many primitive vectors $V$ of depth $N$ such that $\mathcal{S}_{V} \cap P_{u_{0}} \neq \emptyset$. In fact, writing $V=\left(v_{0}, v_{1}, v_{2}\right)$ for $v_{j}=a_{j}+b_{j} \tau_{d}$, the integers $a_{j}, b_{j} \in \mathbb{Z}$ must satisfy the bounds in equations (5), (6), (9).

Proof. The fact that $\left|v_{2}\right|^{2}=N$ gives a small list of possible values for $v_{2} \in \mathcal{O}_{d}$ (note that there are efficient algorithms for listing the numbers $z \in \mathcal{O}_{d}$ such that $|z|^{2}=N$, even for large $N$; our computer code [9] uses the PARI command bnfintnorm).

In what follows, we fix one such value of $v_{2}=a_{2}+b_{2} \tau_{d}$, and show how to find restrictions on $v_{1}$; then, given $v_{2}$ and $v_{1}$, we explain how to find restrictions on $v_{0}$.

The general stream of arguments to show that there are finitely many possibilites for $v_{j}=$ $a_{j}+b_{j} \tau_{d}$, consists in first bounding $b_{j}$, then bounding $a_{j}$ in terms of $b_{j}$ (the corresponding bounds will also depend on $v_{k}$ for $k<j$ ).

Denote by $c_{0}$ the center of the circumscribed circle of the base $T$ of the prism $P$, which has vertices $0, \lambda, \mu$ (see Table 1). Note that
$$c_{0}=\frac{\lambda \mu(\bar{\lambda}-\bar{\mu})}{\bar{\lambda} \mu-\lambda \bar{\mu}},$$
and by definition any $z \in T$ satisfies $\left|z-c_{0}\right| \leq\left|c_{0}\right|$.
We write $\left(z_{0}, \tilde{t}_{0}\right)$ for the (scaled) Heisenberg coordinates of the center of $\mathcal{S}_{V}$; recall that this Cygan sphere has radius $(4 / N)^{1 / 4}$. In particular, the equation of the corresponding

Cygan ball can be written as
$$\left(\left|z-z_{0}\right|^{2}+u\right)^{2}+\left(\sqrt{d}\left(\tilde{t}-\tilde{t}_{0}\right)+2 \Im\left(z \bar{z}_{0}\right)\right)^{2} \leq \frac{4}{N},$$
with equality corresponding to the Cygan sphere.
If there is a point with horospherical coordinates $(z, \tilde{t}, u)$ satisfying equation (4), then
$$\left|z-z_{0}\right| \leq \sqrt{\frac{2}{\sqrt{N}}-u} .$$
Moreover, if the point satisfies $(z, t) \in P$, then we have
$$\left|z_{0}-c_{0}\right| \leq \sqrt{\frac{2}{\sqrt{N}}-u}+\left|c_{0}\right| .$$
Equation (3) then gives
$$\left|v_{1}-c_{0} v_{2}\right| \leq R,$$
where $R=\sqrt{N}\left(\sqrt{\frac{2}{\sqrt{N}}-u}+\left|c_{0}\right|\right)$.
Recall that $v_{1} \in \mathcal{O}_{d}$, so we can write $v_{1}=a_{1}+b_{1} \tau_{d}$ for some $a_{1}, b_{1} \in \mathbb{Z}$. Writing $c_{0} v_{2}=\alpha_{1}+\beta_{1} \tau_{d}$ for $\alpha_{1}, \beta_{1} \in \mathbb{Q}$, we have
$$\left|a_{1}-\alpha_{1}+\left(b_{1}-\beta_{1}\right) \tau_{d}\right|^{2}=\left(a_{1}-\alpha_{1}+\left(b_{1}-\beta_{1}\right) \Re \tau_{d}\right)^{2}+\left(b_{1}-\beta_{1}\right)^{2}\left(\Im \tau_{d}\right)^{2} \leq R^{2},$$
in particular
$$\left\lceil\beta_{1}-\frac{R}{\Im \tau_{d}}\right\rceil \leq b_{1} \leq\left\lfloor\beta_{1}+\frac{R}{\Im \tau_{d}}\right\rfloor,$$
so we get a bound for $b_{1}$. Given a $b_{1}$ that satisfies this bound, we then have
$$\left\lceil\alpha_{1}-\left(b_{1}-\beta_{1}\right) \Re \tau_{d}-R\right\rceil \leq a_{1} \leq\left\lfloor\alpha_{1}-\left(b_{1}-\beta_{1}\right) \Re \tau_{d}+R\right\rfloor .$$

In particular there are finitely many possible values for $v_{1}$. Now given $v_{2}, v_{1} \in \mathcal{O}_{d}$ satisfying these bounds, we explain how to bound the possible values of $v_{0}$. We wish to use the fact that
$$\left(\sqrt{d}\left(\tilde{t}-\tilde{t}_{0}\right)+2 \Im\left(z \bar{z}_{0}\right)\right)^{2} \leq \frac{4}{N}-u_{0}^{2},$$
for some $z \in T$.
We write $z_{0}=x_{0} \lambda+y_{0} \mu, z=x \lambda+y \mu$ for some $x, y, x_{0}, y_{0} \in \mathbb{R}$, and compute
$$\Im\left(z \bar{z}_{0}\right)=\left(x_{0} y-x y_{0}\right) \lambda \Im \mu .$$
Note that $z$ is in $T$, which is the convex hull of $0, \lambda, \mu$ so $0 \leq x, y \leq 1$, hence we have
$$\left|\Im\left(z \bar{z}_{0}\right)\right| \leq\left(\left|x_{0}\right|+\left|y_{0}\right|\right) \lambda \Im \mu .$$

Now we get
$$-\sqrt{\frac{4}{N}-u_{0}^{2}}-2\left(\left|x_{0}\right|+\left|y_{0}\right|\right) \lambda \Im \mu \leq \sqrt{d}\left(\tilde{t}_{0}-\tilde{t}\right) \leq \sqrt{\frac{4}{N}-u_{0}^{2}}+2\left(\left|x_{0}\right|+\left|y_{0}\right|\right) \lambda \Im \mu,$$
and $\tilde{t} \in[0,2]$, so we get a bound
$$\tilde{t}_{0}^{\min } \leq \tilde{t}_{0} \leq \tilde{t}_{0}^{\max },$$
where
$$\begin{gathered}
\tilde{t}_{0}^{\min }=-\left(\sqrt{\frac{4}{N}-u^{2}}+2\left(\left|x_{0}\right|+\left|y_{0}\right|\right) \lambda \Im \mu\right) / \sqrt{d} \\
\tilde{t}_{0}^{\max }=2+\left(\sqrt{\frac{4}{N}-u^{2}}+2\left(\left|x_{0}\right|+\left|y_{0}\right|\right) \lambda \Im \mu\right) / \sqrt{d}
\end{gathered}$$
Note however that $\tilde{t}_{0}$ is not an integer, so we need to work a little more to get an effective method.

We now use equation (3), which relates $\tilde{t}_{0}$ to $v_{0}=a_{0}+b_{0} \tau_{d}\left(a_{0}, b_{0} \in \mathbb{Z}\right)$. Taking the real and imaginary parts of both sides of the equation
$$a_{0}+b_{0} \tau_{d}=v_{2}\left(\frac{-\left|z_{0}\right|^{2}+i \tilde{t}_{0} \sqrt{d}}{2}\right),$$
we get
$$\begin{gathered}
a_{0}+b_{0} \Re \tau_{d}=-\frac{1}{2}\left|z_{0}\right|^{2} \Re v_{2}-\frac{1}{2} \tilde{t}_{0} \sqrt{d} \Im v_{2} \\
b_{0} \Im \tau_{d}=-\frac{1}{2}\left|z_{0}\right|^{2} \Im v_{2}+\frac{1}{2} \tilde{t}_{0} \sqrt{d} \Re v_{2}
\end{gathered}$$
If $\Re v_{2} \neq 0$, the second line of equation (8) can be solved to $\tilde{t}_{0}$, hence we get
$$\tilde{t}_{0}^{m i n} \leq \frac{b_{0} \Im \tau_{d}+\frac{1}{2}\left|z_{0}\right|^{2} \Im v_{2}}{\frac{1}{2} \sqrt{d} \Re v_{2}} \leq \tilde{t}_{0}^{m a x},$$
which in turn gives us a bound for $b_{0}$.
Similarly, the first equation (8) can be solved for $\tilde{t}_{0}$ (at least when $\Im v_{2} \neq 0$ ), to get a bound on $a_{0}$.

The cases when $\Re v_{2}$ and/or $\Im v_{2}$ are 0 are actually easier, because equation (8) gives more restrictive conditions on $a_{0}$ and $b_{0}$. \(\square\)

Remark 3.2. (1) The bounds given in the proof of Proposition 3.1 are by no means optimal, but they allow us to run a certified computer search in a finite amount of time. For future reference, we refer to the bounds obtained in the proof as crude bounds (they are the ones used in our computer code, see [9]).
\begin{itemize}
\item[(2)] One can shorten the list of Cygan spheres that satisfy the crude bounds, by checking whether each sphere in the list actually intersects the fundamental prism at horospherical height $u_{0}$. This can be done by using elementary calculus, and certifying the results by using some computational tool like the Rational Univariate Representation (RUR), see [27]. In our computer program, we run an indermediate refinement of the bound using the RUR as implemented in giac (see [23]), and restrict to Cygan spheres whose projection to all three coordinate axes intersect the projection of the fundamental prism. This allows us to speed up the computation for large values of $d$.
\end{itemize}

\section*{4. Effective Feustel-Zink}

We observe that the Feustel-Zink result (Theorem 2.1) can be rephrased as follows (recall that $q_{\infty}=(1,0,0)$, and we assume throughout the paper that $\mathbb{K}_{d}$ has class number one).

Proposition 4.1. For every primitive integral vector $v \in \mathcal{O}_{d}^{3}$, there exists $A \in \Gamma_{d}$ such that $A\left(q_{\infty}\right)=v$.

As mentioned in [21], it is not obvious how to make this statement effective, we will sketch how our computer code does this.

The first remark is that it is enough to find a matrix $A$ as in Proposition 4.1 only for $v$ in a list of representatives for $\Gamma_{d}^{(\infty)}$-orbits of rational points (we sketched in section 2.3 how such a list can be gathered).

The second observation is that rather than the mere existence of $A$ as in the statement of Proposition 4.1, we may be more restrictive and assume that $A^{-1}\left(q_{\infty}\right)$ is also in our list of representatives for $\Gamma_{d}^{(\infty)}$-orbits of rational points. Indeed, for any $M \in \Gamma_{d}^{(\infty)}, A M^{-1}\left(q_{\infty}\right)=$ $A q_{\infty}$ (so we can replace $A$ by $A M^{-1}$ ), and $\left(A M^{-1}\right)^{-1}\left(q_{\infty}\right)=M A^{-1}\left(q_{\infty}\right)$.

Now recall that the inverse of an element $A \in U(J)$ is given by $A^{-1}=J A^{*} J$, so the first column of $A$ and the last row of $A^{-1}$ are obtained from one another by complex conjugation and multiplication by $J$ (the last one amounts to flipping the first and third entry of the vector). Note in particular that $A$ and $A^{-1}$ have the same depth.

This means that when searching for $A \in U(J)$ whose first column is $v$, we may assume the last row of $A$ is given up to a multiplication by a unit in $\mathcal{O}_{d}$ by $(J w)^{*}$ for some $w$ in the list of representatives for $\Gamma_{d}^{(\infty)}$-orbits of rational points of depth given by $\left|v_{2}\right|^{2}$.

We then try to fill in the upper right $2 \times 2$ matrix (see Proposition 4.2); if this fails, we try another of the finitely many possibilities for the last row of $A$. This method turns out to be very efficient in practice, it allowed us to construct all necessary matrices in a fairly short amount of computation time for $d \leq 19$.

We are grateful for an anomymous referee for having communicated to us the result of Proposition 4.2, which simplifies some clumsy computations that appeared in earlier versions of the manuscript.

Proposition 4.2. Let $A \in U(J)$ be written as
$$A=\left(\begin{array}{lll}
a & x & y \\
b & z & w \\
c & d & e
\end{array}\right) .$$
Assume $c \neq 0$ and let $\delta=\operatorname{det}(A)$. Then we have $x=\frac{1}{\delta c}(\delta a d+\bar{b}), z=\frac{1}{\delta c}(\delta b d-\bar{c})$, $w=\frac{1}{\delta c}(\delta b e+\bar{d})$, and $y=(a e \bar{c}-\bar{\delta} \bar{b} \bar{d}+c) /|c|^{2}$. This matrix is in $\Gamma_{d}$ if and only if its entries are in $\mathcal{O}_{d}$, and in that case $\delta=\operatorname{det}(A)$ is a unit in $\mathcal{O}_{d}$.

Proof: The fact that $A^{*} J A=J$ can be rewritten as $A^{-1}=J A^{*} J$; the proposition then follows from easily by expressing the entries of $A^{-1}$ in terms of cofactors of $A$. \(\square\)

\section*{5. Covering depths}

The key to our computations is to obtain a bound on the radius of the Cygan spheres that intersect the Ford domain for $\Gamma_{d}$ (see Definition 2.1). More specifically, let us write $1=n_{1}<n_{2}<n_{3}<\ldots$ for the depths of Cygan spheres for elements of $\Gamma_{d}$ (this is equivalent to listing the norms in $\mathcal{O}_{d}$ in increasing fashion).

Following [21], we define the covering depth of $\Gamma_{d}$ to be the smallest $n_{k}$ such that the spheres of depth $n_{j}$ for $j>k$ do not intersect the Ford domain (note that this does not necessarily mean that some spheres of depth $n_{k}$ are necessary to define the Ford domain). If this is the case, then the Cygan spheres corresponding to rational points of depth $n_{k}$ for $k>j$ do not intersect the Ford domain, and in particular it is enough to use the rational points of depth $\leq n_{j}$ in order to study/describe the Ford domain (in most cases, the Ford domain can actually be described with an even smaller set of depths, but we will not use this).

The basic procedure gives us a way to answer the following :
Problem : For a given $j \in \mathbb{N}^{*}$, determine whether or not the cross section at horospherical height $u=2 / \sqrt{n_{j+1}}$ of the fundamental domain for the standard cusp group $\Gamma_{d}^{(\infty)}$ is covered by the interiors of the Cygan spheres of depth $\leq n_{j}$.

The covering depth is then the smallest $n_{j}$ such that the answer to our Problem is YES.

In order to do this, we will
\begin{itemize}
\item[(1)] reduce the verification to finitely many checks (note that the Ford domain has infinitely many sides);
\item[(2)] subdivide the prism into convex pieces that are small enough for each piece to be contained in a Cygan sphere centered at a rational point of depth $\leq n_{j}$.
\end{itemize}

The reduction to finitely many verifications (1) requires an explicit (finite) upper bound on the set of rational points $v \in \mathcal{O}_{d}^{3}$ of depth $\leq n_{j}$ such that the Cygan sphere $S_{v}$ corresponding to $v$ (see Lemma 2.1) satisfies $S_{v} \cap C_{P} \neq \emptyset$. In fact, we can be a bit more restrictive and require that $S_{v}$ intersects $C_{P}$ at horospherical height $2 / \sqrt{n_{j+1}}$. The details of how this can be done were explained in section 3.

Part (2) was performed in [21] and [26] by a search "by hand" of a decomposition inspired by visual analysis of pictures of Cygan spheres. We will give a more systematic method, based on a dichotomy method in the prism. It is probably far from optimal (and runs quite slowly for large values of $d$ ), but it has the advantage that it does not rely on human intervention/visual inspection.

The procedure will maintain a list of prisms that need to be studied (until we get an answer to our question), initialized as containing just one prism, namely the fundamental prism $L_{0}=\{P\}$.

We now explain how to construct the list $L_{k+1}$ from the list $L_{k}$ (or stop the procedure if we have reached an answer).

For any $u>0$, and for any prism $Q$ in the Heisenberg group, we write $Q_{u}$ for the translate of $Q$ at horospherical height $u$. Now for every prism $Q$ in $L_{k}$, we do the following:
\begin{itemize}
\item[-] For each vertex $v$ of the translate $Q_{2 / \sqrt{n_{j+1}}}$ of $Q$, list the Cygan spheres of depth $\leq n_{j}$ that contain $v$ in their interior. If this list is empty, we know the prism is NOT covered (answer reached).
\item[-] If every vertex of $Q_{2 / \sqrt{n_{j+1}}}$ is covered by some Cygan sphere, check if there is a single Cygan sphere that contains all of its vertices.
\begin{itemize}
\item[-] If so, the prism $Q_{2 / \sqrt{n_{j+1}}}$ is covered by a Cygan sphere, and we do not include it in $L_{k+1}$.
\item[-] If not, subdivide $Q$ into $2^{3}=8$ smaller prisms, and include them in $L_{k+1}$.
\end{itemize}
\end{itemize}

If the answer to our PROBLEM is NO, then there exists a prism obtained from the above dichotomy with at least one vertex not covered by any Cygan sphere, so the procedure will stop and find that the answer is NO.

If the answer is YES, once again, this will be seen at the level of some fine enough decomposition of the prism into prisms at scale $1 / 2^{k}$ for some $k$, so after finitely many stages we will get $L_{k}=\emptyset$.

Remark 5.1. As in [21], in order to certify the inequalities used to verify whether a given vertex of a prism in the subdivision is covered by a Cygan sphere, in our computer program, we replace the horospherical height $2 / \sqrt{n_{j+1}}$ by a rational approximation, i.e. a number $u_{j} \in \mathbb{Q}$ that satisfies $2 / \sqrt{n_{j+1}}<u_{j}<2 / \sqrt{n_{j}}$, which we choose to be "close" to $2 / \sqrt{n_{j+1}}$. This is inconsequential for our purpose, which is to determine a finite list of depths that suffice to define the Ford domain for the corresponding Picard modular group.

Running this procedure, we find the covering depths given in Table 3. In each case, we give the number of cusp orbits of rational points of depth at most equal to the covering depth; in parentheses, we list the number of cusp orbits remaing after removing the centers of Cygan spheres obviously contained in another one (using the triangle inequality, i.e. comparing the Cygan distance with the sum of the radii of the spheres).

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $d$ & Covering depth & Size of smallest prism used & Number of cusp orbits of rational points \\
\hline 1 & 4 & $1 / 2^{2}$ & 4 (4) \\
\hline 2 & 16 & $1 / 2^{5}$ & 46 (46) \\
\hline 3 & 4 & 1/2 & 4 (4) \\
\hline 7 & 7 & $1 / 2^{5}$ & 8 (8) \\
\hline 11 & 36 & $1 / 2^{19}$ & 226 (198) \\
\hline 19 & 64 & $1 / 2^{7}$ & 540 (455) \\
\hline 43 & 269 & $1 / 2^{14}$ & ? (6184) \\
\hline 67 & 607 & $1 / 2^{15}$ & ? (26098) \\
\hline 163 & $\geq 3053$ & $\leq 1 / 2^{6}$ & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 3. Covering depths for 1-cusped Picard modular groups.}
\end{table}

For $d=19$, running all the computations (covering depth, presentation, classification of isotropy groups) already takes several hours, and the computation time seems prohibitive for larger values of $d$ (at least in our implementation).

\section*{6. Computation times}

In table 4, we gather rough computation time for various values of $d$, and various parts of the computations. For $d \geq 43$, our Sage implementation [9] of the method is inefficient (both in computation time and memory usage), and it only allowed us to go through with part of the computation (see the question marks in Tables 3 and 4). We hope that a better implementation will allow us to treat $d=43,67$ and perhaps even 163.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|}
\hline $d$ & Covering depth (giac) & Matrices (giac) & Torsion & Presentation & Conversion \\
\hline 1 & 4 s & 0 s & 34 s & 0.5 s & 35 s \\
\hline 2 & 1 min 11 s & 5 s & 2 min 32 s & 24 s & 3 min 16 s \\
\hline 3 & 6 s & 0 s & 1 min 4 s & 0.5 s & 22 s \\
\hline 7 & 14 s & 0 s & 31 s & 2 s & 58 s \\
\hline 11 & 4 min 27 s & 2 min 6 s & 4 min 27 s & 5 min 43 s & 13 min 16s \\
\hline 19 & 14 min 51 s & 6 min 0 s & 9 min 11 s & 16 min 15 s & 54 min 10 s \\
\hline 43 & 19 h 26 min 44 s & ? & ? & ? & ? \\
\hline 67 & 8 d 18 h 37 min 33s & ? & ? & ? & ? \\
\hline 163 & ? & ? & ? & ? & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 4. Approximate CPU time on an Intel 1.8GHz processor.}
\end{table}

\section*{7. Isotropy groups}

In the tables in this section, we describe the non-trivial (conjugacy classes of) isotropy groups for the action on complex hyperbolic space of $P U\left(2,1, \mathcal{O}_{d}\right)$ for $d=1,2,3,7,11$ and 19. These can also be thought of as being the non-trivial maximal finite subgroups of $P U\left(2,1, \mathcal{O}_{d}\right)$.

The conjugacy classes of complex reflections are listed in Tables 5, 7, 9, 11 for various values of $d$. Representatives for the conjugacy classes of isotropy groups with isolated fixed points are listed in Tables 6, 8, 10, 12, 13 and 14.

For an isotropy group $G$ with an isolated fixed point, we write $R_{G}$ for its complex reflection subgroup, and describe $R_{G}$ by giving vectors polar to the mirrors of generators (fifth column), as well as braid lengths of pairs of generators (fourth column). The order of $G$ (resp. $R_{G}$ ) is given in the second (resp. third) column. The number of mirrors (seventh column) in each group is written as $j_{1}, j_{2}, j_{3}$ where $j_{k}$ is the number of mirrors in the $\Gamma$-orbit of the $k$-th polar vector in the list of complex reflections (the latter vectors are listed in Tables 5, 7, 9, etc.)

Almost all finite reflection groups that occur in this way are well-generated, i.e. can be generated by $2=\operatorname{dim}\left(\mathbb{C}^{2}\right)$ generators. The only exception is one of the isotropy groups for
$\Gamma_{2}$, which is isomorphic to the Shepard-Todd [29] group $G_{12}$, see [7] for a presentation of that group.

The isotropy groups that are not generated by reflections are all cyclic; for such groups, we list a (regular elliptic) generator in the last column of the table.

In the tables below, for any positive integer $k$, we write $\zeta_{k}=e^{2 \pi i / k}$.

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline Order & $w$ & $\|w\|^{2}$ \\
\hline 4 & (0, 1, 0) & 1 \\
\hline 4 & (1, -1, 0) & 1 \\
\hline 2 & (1, 0, 1) & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 5. Conjugacy classes of complex reflections for $d=1$.}
\end{table}

\section*{8. Neat subgroups}

The general method we use to find torsion-free subgroups in $G=\Gamma_{d}$ is the following. We assume we are given a list $T$ of non-trivial isotropy groups that contains all isotropy groups up to conjugation in $G$, and generators for the standard cusp $G_{\infty}$.
\begin{itemize}
\item[-] Find a normal subgroup $K$, and consider $\varphi: G \rightarrow F=G / K$;
\item[-] Check that $\left.\varphi\right|_{t}$ is injective for every $t$ in $T$ (if so, $K$ is torsion-free);
\item[-] List subgroups $S$ of $F$ that intersect all conjugates of subgroups in $T$ trivially; then $\varphi^{-1}(S)$ is torsion-free and $\left[G: \varphi^{-1}(S)\right]=[F: S]$.
\end{itemize}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $v$ & $|G|$ & $\left|R_{G}\right|$ & br & $w$ & $\|w\|^{2}$ & \# mirrors & Extra generators \\
\hline \multirow[t]{2}{*}{$(1+i,-i,-1-i)$} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{3} & ( $0,1+i, 1$ ) & 2 & \multirow[t]{2}{*}{0, 0, 3} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline \multirow[t]{2}{*}{(1, 0, -1)} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{2} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{1, 0, 1} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline \multirow[t]{2}{*}{(1, -1, -1)} & \multirow[t]{2}{*}{32} & \multirow[t]{2}{*}{32} & \multirow[t]{2}{*}{4} & (0, 1, 1) & 1 & \multirow[t]{2}{*}{0, 2, 4} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline $\left(1, i\left(\zeta_{8}-1\right), i\left(\zeta_{8}-1\right)\right)$ & 8 & 4 & & (1, -1, 0) & 1 & 0, 1, 0 & $\left(\begin{array}{ccc}-i & -i-1 & i \\ i-1 & i & 0 \\ i-1 & i-1 & 1\end{array}\right)$ \\
\hline $\left(1,0,-\zeta_{12}\right)$ & 12 & 4 & & (0, 1, 0) & 1 & 1, 0, 0 & $\left(\begin{array}{ccc}i & 0 & 1 \\ 0 & -1 & 0 \\ 1 & 0 & 0\end{array}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 6. List of isolated fixed point isotropy groups for $d=1$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline Order & $w$ & $\|w\|^{2}$ \\
\hline 2 & (0, 1, 0) & 1 \\
\hline 2 & (1, -1, 0) & 1 \\
\hline 2 & (1, 0, 1) & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 7. Conjugacy classes of complex reflections for $d=2$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $v$ & $|G|$ & $\left|R_{G}\right|$ & br & $w$ & $\|w\|^{2}$ & \# mirrors & Extra generators \\
\hline \multirow[t]{2}{*}{(1, 0, -1)} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{2} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{0, 1, 1} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline \multirow[t]{2}{*}{$(-1-\alpha, \alpha, \alpha)$} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{2} & (1, -1, 0) & 1 & \multirow[t]{2}{*}{0, 1, 1} & \multirow{2}{*}{} \\
\hline & & & & $(1,-\alpha,-\alpha)$ & 2 & & \\
\hline \multirow[t]{2}{*}{$(-2-\alpha,-1, \alpha)$} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{3} & (1, -α, 0) & 2 & \multirow[t]{2}{*}{0, 0, 3} & \multirow{2}{*}{} \\
\hline & & & & ( $1+\alpha, 0,1$ ) & 2 & & \\
\hline \multirow[t]{2}{*}{(1, -1, -1)} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{4} & (0, 1, 1) & 1 & \multirow[t]{2}{*}{0, 2, 2} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline \multirow[t]{3}{*}{$(-2-\alpha,-1+\alpha, \alpha)$} & \multirow[t]{3}{*}{48} & \multirow[t]{3}{*}{48} & \multirow[t]{3}{*}{6} & ( $0, \alpha, 1$ ) & 2 & \multirow[t]{3}{*}{0, 0, 12} & \multirow{3}{*}{} \\
\hline & & & & $(1+\alpha, 2,1-\alpha)$ & 2 & & \\
\hline & & & & $(1+\alpha, 2-\alpha,-\alpha)$ & 2 & & \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 8 & 2 & & ( $\alpha, 1,0$ ) & 1 & 1, 0, 0 & $\left(\begin{array}{ccc}1-\alpha & -2 & \alpha \\ -\alpha & -1 & 0 \\ 1 & \alpha & 1\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & ( $\alpha$, 1, 1) & 1 & 0, 1, 0 & $\left(\begin{array}{ccc}1 & 2 & -2-2 \alpha \\ -\alpha & -1-2 \alpha & -2+2 \alpha \\ -1-\alpha & -2-\alpha & -1+2 \alpha\end{array}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 8. List of isolated fixed point isotropy groups for $d=2$ (we write $\alpha=i \sqrt{2}$ ).}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline Order & $w$ & $\|w\|^{2}$ \\
\hline 6 & (0, 1, 0) & 1 \\
\hline 2 & (1, 0, 1) & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 9. Conjugacy classes of complex reflections for $d=3$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $v$ & $|G|$ & $\left|R_{G}\right|$ & br & $w$ & $\|w\|^{2}$ & \# mirrors & Extra generators \\
\hline \multirow[t]{2}{*}{(1, 0, -1)} & \multirow[t]{2}{*}{12} & \multirow[t]{2}{*}{12} & \multirow[t]{2}{*}{2} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{1,1} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline \multirow[t]{2}{*}{(1, 0, $\bar{\omega}$ )} & \multirow[t]{2}{*}{72} & \multirow[t]{2}{*}{72} & \multirow[t]{2}{*}{4} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{2,6} & \multirow{2}{*}{} \\
\hline & & & & $(1,-1,-\omega)$ & 2 & & \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 3 & 1 & & & & & $\left(\begin{array}{ccc}\omega & \omega & 1 \\ 1 & -\omega & 0 \\ 1 & 0 & 0\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & (1, 1, -ω) & 2 & 0, 1 & $\left(\begin{array}{ccc}\omega & -1 & \omega+3 \\ 1 & 1 & -i \sqrt{3} \\ 1 & 0 & -i \sqrt{3}\end{array}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 10. List of isolated fixed point isotropy groups for $d=3$ (we write $\omega=e^{2 \pi i / 3}$ ).}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|}
\hline Order & $w$ & $\|w\|^{2}$ \\
\hline 2 & (0, 1, 0) & 1 \\
\hline 2 & (1, 0, 1) & 2 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 11. Conjugacy classes of complex reflections for $d=7,11,19$.}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $v$ & $|G|$ & $\left|R_{G}\right|$ & br & $w$ & $\|w\|^{2}$ & \# mirrors & Extra generators \\
\hline \multirow[t]{2}{*}{(1, 0, -1)} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{2} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{1,1} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline \multirow[t]{2}{*}{$(3+i \sqrt{7}, 1, \bar{\tau})$} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{3} & (1, -τ, 0) & 2 & \multirow[t]{2}{*}{0, 3} & \multirow{2}{*}{} \\
\hline & & & & ( $1+i \sqrt{7}$, 0, 1) & 2 & & \\
\hline \multirow[t]{2}{*}{$(-1-\tau,-\bar{\tau}, \tau)$} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{3} & ( $0, \tau, 1$ ) & 2 & \multirow[t]{2}{*}{0, 3} & \multirow{2}{*}{} \\
\hline & & & & ( $\tau, \bar{\tau}, 0$ ) & 2 & & \\
\hline \multirow[t]{2}{*}{$(\bar{\tau}, 0,-1)$} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{4} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{2, 2} & \multirow{2}{*}{} \\
\hline & & & & ( $\tau, 1,1$ ) & 2 & & \\
\hline \multirow[t]{2}{*}{$(4, \bar{\tau},-\tau)$} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{4} & ( $1+i \sqrt{7}$, 0, 1) & 2 & \multirow[t]{2}{*}{0,4} & \multirow{2}{*}{} \\
\hline & & & & $(\tau, \bar{\tau}, 0)$ & 2 & & \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 6 & 2 & & $(-\bar{\tau}, \tau, 1)$ & 1 & 1, 0 & $\left(\begin{array}{ccc}-2 & \tau-2 & 1+2 i \sqrt{7} \\ \tau-1 & \tau+1 & 3 \\ \tau & 1 & 3-\tau\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 7 & 1 & & & & & $\left(\begin{array}{ccc}-2-\tau & \tau-3 & 3 \tau-2 \\ -1 & 0 & -\bar{\tau} \\ -\bar{\tau} & \tau & 2\end{array}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 12. List of isolated fixed point isotropy groups for $d=7$ (we write $\left.\tau=\frac{1+i \sqrt{7}}{2}\right)$}
\end{table}

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $v$ & $|G|$ & $\left|R_{G}\right|$ & br & $w$ & $\|w\|^{2}$ & \# mirrors & Extra generators \\
\hline \multirow[t]{2}{*}{$(2,1-\tau,-2)$} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{2} & (1, 0, 1) & 2 & \multirow[t]{2}{*}{1,1} & \multirow{2}{*}{} \\
\hline & & & & $(1+\bar{\tau},-4,-1-\bar{\tau})$ & 2 & & \\
\hline \multirow[t]{2}{*}{$(\tau+3,0, \bar{\tau})$} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{2} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{1, 1} & \multirow{2}{*}{} \\
\hline & & & & $(\tau-4,0, \tau)$ & 2 & & \\
\hline \multirow[t]{2}{*}{(1, 0, -1)} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{4} & \multirow[t]{2}{*}{2} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{1,1} & \multirow{2}{*}{} \\
\hline & & & & (1, 0, 1) & 2 & & \\
\hline \multirow[t]{2}{*}{$(3 \tau-6, \tau, \tau+2)$} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{6} & \multirow[t]{2}{*}{3} & $(-\bar{\tau}, \tau, 1)$ & 2 & \multirow[t]{2}{*}{0,3} & \multirow{2}{*}{} \\
\hline & & & & $(\tau-4,0, \tau)$ & 2 & & \\
\hline \multirow[t]{2}{*}{$(-\bar{\tau}, 0,1)$} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{8} & \multirow[t]{2}{*}{4} & (0, 1, 0) & 1 & \multirow[t]{2}{*}{2, 2} & \multirow{2}{*}{} \\
\hline & & & & ( $\tau, 1,1$ ) & 2 & & \\
\hline \multirow[t]{2}{*}{$(\tau, 2-\tau,-\tau)$} & \multirow[t]{2}{*}{12} & \multirow[t]{2}{*}{12} & \multirow[t]{2}{*}{6} & (1, 0, 1) & 2 & \multirow[t]{2}{*}{0,6} & \multirow{2}{*}{} \\
\hline & & & & $(1, \bar{\tau},-\tau)$ & 2 & & \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & (1, 0, 1) & 2 & 0, 1 & $\left(\begin{array}{ccc}\bar{\tau} & -\tau-1 & \tau \\ \tau-2 & i \sqrt{11} & -\tau+2 \\ \tau & \tau+1 & \bar{\tau}\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & $(\tau, 1,1)$ & 2 & 0, 1 & $\left(\begin{array}{ccc}-1 & \bar{\tau} & \tau+1 \\ -1 & \tau & 1 \\ \tau & 2 & \bar{\tau}+1\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & $(-\bar{\tau}, \tau, 1)$ & 2 & 0, 1 & $\left(\begin{array}{ccc}12 & 6-2 \tau & 17 \tau-10 \\ 2 \bar{\tau} & -\tau-1 & -\tau-7 \\ 1-3 \tau & -\tau-1 & \tau-12\end{array}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 13. List of isolated fixed point isotropy groups for $d=11$ (we write $\left.\tau=\frac{1+i \sqrt{11}}{2}\right)$.}
\end{table}
\begin{itemize}
\item[-] For each such subgroup $S$, study the action of $S$ the right cosets of $F_{\infty}=\varphi\left(G_{\infty}\right)$ in $F$ to find generators for each cusp.
\end{itemize}

In the third item, we consider only maximal subgroups with this property.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|l|l|l|}
\hline $v$ & $|G|$ & $\left|R_{G}\right|$ & br & $w$ & $\|w\|^{2}$ & \# mirrors & Extra generators \\
\hline $(2 \tau+4,2, \bar{\tau})$ & 4 & 4 & 2 & $(2 \tau-2, \tau, 1)$ $(2 \tau, 0,1)$ & 2 2 & 0,2 & \\
\hline (1, 0, -1) & 4 & 4 & 2 & (0, 1, 0) (1, 0, 1) & 1 2 & 1,1 & \\
\hline $(\bar{\tau}, 0,-2)$ & 4 & 4 & 2 & (0, 1, 0) ( $\tau, 0,2$ ) & 1 2 & 1,1 & \\
\hline $(\tau-6,2 \tau, 2)$ & 4 & 4 & 2 & $(-\bar{\tau}, 1,0)$ $(\tau-5,2 \tau, 2)$ & 1 2 & 1,1 & \\
\hline $(\tau-7,-2 \bar{\tau}, \tau+2)$ & 6 & 6 & 3 & $(\tau-3, \tau+1,1)$ $(\tau+2,3, \bar{\tau})$ & 2 2 & 0,3 & \\
\hline $(5 \bar{\tau}-8,-\tau-3, \tau-3)$ & 6 & 6 & 3 & $(1+\bar{\tau}, \bar{\tau},-1)$ $(\tau+7,2, \bar{\tau})$ & 2 2 & 0,3 & \\
\hline $(-\bar{\tau}, 0,1)$ & 8 & 8 & 4 & (0, 1, 0) ( $\tau, 1,1$ ) & 1 2 & 2,2 & \\
\hline $(9,1+\bar{\tau},-\tau)$ & 2 & 1 & & & & & $\left(\begin{array}{ccc}9 \tau-8 & 9 \tau+9 & 81 \\ 2 \tau+3 & 8 & 9 \bar{\tau}+9 \\ 5 & 2 \bar{\tau}+3 & 9 \bar{\tau}-8\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & $(\tau-2, \tau, 1)$ & 2 & 0, 1 & $\left(\begin{array}{ccc}7 & 3 \bar{\tau}+1 & -9 \tau+1 \\ \bar{\tau}+1 & -\tau-2 & -\tau-6 \\ -\tau & -2 & \tau-6\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & $(\tau-3, \tau+1,1)$ & 2 & 0, 1 & $\left(\begin{array}{ccc}2 \tau+10 & 6 \bar{\tau}+8 & -9 \tau-1 \\ 2 \bar{\tau}+6 & -5 \tau-1 & -2 \tau-11 \\ -3 \tau+1 & -\tau-8 & 3 \tau-10\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 4 & 2 & & $(1+\bar{\tau}, \bar{\tau},-1)$ & 2 & 0, 1 & $\left(\begin{array}{ccc}2 \tau+25 & 13 \bar{\tau}+10 & -47 \tau+20 \\ 2 \bar{\tau}+7 & -5 \tau & -12 \tau-16 \\ -3 \tau+1 & -\tau-7 & 3 \tau-26\end{array}\right)$ \\
\hline $\notin \mathbb{K}_{d}^{3}$ & 6 & 2 & & $(2,-\tau,-1)$ & 1 & 1, 0 & $\left(\begin{array}{ccc}\tau+1 & \bar{\tau}+4 & -1-2 \tau \\ \bar{\tau}+2 & -2 \tau-2 & \tau-4 \\ -\tau & -3 & -\bar{\tau}\end{array}\right)$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 14. List of isolated fixed point isotropy groups for $d=19$ (we write $\left.\tau=\frac{1+i \sqrt{19}}{2}\right)$.}
\end{table}

About the first item, note that there is an effective algorithm for listing normal subgroups $H \subset \Gamma$ with $[\Gamma: H] \leq N$ for any $N \in \mathbb{N}$. This algorithm is implemented in Magma (via the command LowIndexNormalSubgroups), and runs efficiently when $N$ is "not too large".

When $G$ has too many (normal) subgroups, reasonable values of $N$ tend to be very small. This seems to be the case for $d=11$ and $d=19$ for instance, where listing all normal subgroups of index $\leq 200$ already takes quite a long time (and none of the many corresponding subgroups turn out to be torsion-free). In such cases, we use congruence subgroups, which tend to produce normal subgroups of larger index.

The orbifold Euler characteristics of the quotients $\Gamma_{d} \backslash \mathbf{H}_{\mathbb{C}}^{2}$ are known, see Theorem 5A.4.7 in [17] for instance. For convenience, we list the results in Table 15, as well as the least common multiple $L_{d}$ of the orders of finite subgroups in $\Gamma_{d}$ (it is a standard fact that the index of any torsion-free subgroup in $\Gamma_{d}$ must be a multiple of $L_{d}$ ).

We also list the smallest index of torsion-free (TF) subgroups we could find, as well as the smallest index of a neat subgroup (i.e. torsion-free and torsion-free at infinity, a property which we refer to as $T F \infty$ ). Recall that the last condition is equivalent to the
existence of a compactification of the quotient by finitely many elliptic curves with negative self-intersection.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|l|}
\hline $d$ & $\chi_{\text {orb }}$ & $L_{d}$ & Known $T F \infty$ & Known $T F$ \\
\hline 1 & 1/32 & 96 & 96 & 96 \\
\hline 2 & 3/16 & 48 & 96 & 48 \\
\hline 3 & 1/72 & 72 & 72 & 72 \\
\hline 7 & 1/7 & 168 & 336 & 336 \\
\hline 11 & 3/8 & 24 & 432 & 432 \\
\hline 19 & 11/8 & 24 & 864 & 864 \\
\hline 43 & 83/8 & ? & ? & ? \\
\hline 67 & 251/8 & ? & ? & ? \\
\hline 163 & 2315/8 & ? & ? & ? \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 15. Euler characteristics for 1-cusped Picard modular surfaces, and least common multiple $L_{d}$ of the order of finite subgroups.}
\end{table}

In the next few subsections, we will give a bit more details about the $T F \infty$ subgroups we have found, namely we list their abelianization, the index of their normal core, and the self-intersections of the elliptic curves that compactify them. Computer code to verify our claims is available at [9].

Note that we do not claim that the lists in the next few sections are optimal, nor exhaustive. The reason why we cannot claim optimality is that we have no reasonable effective upper bound for the index in $\Gamma_{d}$ of the normal core
$$\operatorname{Core}_{\Gamma_{d}}(H)=\cap_{g \in \Gamma_{d}} g H g^{-1}$$
of a torsion-free/neat subgroup $H \subset \Gamma_{d}$ in terms of the index $n=\left[\Gamma_{d}: H\right]$. It is easy to see that the index of the normal core is bounded by $n!$, but in practice there is no hope to list all normal subgroups of index $n!$ (see the obvious lower bound given in table 15, which implies $n \geq 24$ ).
8.1. General method. In order to produce the lists in sections 8.2 through 8.7, we ask Magma for a list normal subgroups of $\Gamma_{d}$ of index $\leq N$ (we choose $N$ so that Magma answers within a reasonable amount of time, the size of $N$ depends a lot on the value of $d$, and to a lesser extent on the presentation used for $\Gamma_{d}$ ).

For each normal subgroup $K \subset \Gamma_{d}$, we determine whether $K$ is $T F$ (torsion-free); this is done by verifying that the quotient map $\varphi: \Gamma_{d} \rightarrow F=\Gamma_{d} / K$ preserves the order of torsion elements (it is enough to check that this is the case for a representative of each conjugacy classes of torsion elements).

We also verify whether $K$ is $T F \infty$ (torsion-free at infinity) by finding a presentation for its cusps. Note that the cusps of $K$ are in 1-1 correspondence with right cosets in $F$ of $F_{\infty}=\varphi\left(\Gamma_{d}^{(\infty)}\right)$, where $\Gamma_{d}^{(\infty)}$ is the standard cusp of $\Gamma_{d}$, i.e. the stabilizer of (1, 0, 0). In particular the number of cusps is the index $\left[F: F_{\infty}\right]$. Note also that since $K$ is a normal subgroup, all its cusps are isomorphic to each other, and one representative is $K \cap \Gamma_{d}^{(\infty)}$.

The group $K_{\infty}=K \cap \Gamma_{d}^{(\infty)}$ can actually be presented by computing the kernel of the restricted morphism $\left.\phi\right|_{\Gamma_{d}^{(\infty)}}$, since we have an explicit presentation for $\Gamma_{d}^{(\infty)}$. Given a generating set for $K_{\infty}$, it is easy to check whether $K_{\infty}$ contains twist-parabolic elements, namely we simply check if every generator is unipotent.

Now for each neat normal subgroup $K \triangleleft \Gamma_{d}$, we once again consider the quotient map $\varphi: \Gamma_{d} \rightarrow F=\Gamma_{d} / K$, and search for subgroups $S \subset F$ such that $\varphi^{-1}(S)$ is $T F$; this amounts to saying that no non-trivial element of $S$ is conjugate to $\varphi(t)$ for any $t$ in our list of representatives for torsion elements. Alternatively, this is equivalent to requiring that $x S x^{-1} \cap X=\{e\}$ for all $x \in F$ and $X=\varphi(\tilde{X})$, with $\tilde{X}$ any isotropy group in $\Gamma_{d}$.

If $H=\varphi^{-1}(S)$ is $T F$, we compute generators for each of its cusps, by studying the action of $S$ on the set of right cosets of $F_{\infty}=\varphi\left(\Gamma_{d}^{(\infty)}\right)$ in $F$. Note once again that the cusps are in bijection with $S$-orbits of such right cosets, and we can produce generators for each cusp by finding generators for the kernel $K_{\infty}$ of the map $\Gamma_{d}^{(\infty)} \rightarrow F_{\infty}$, and adjoining extra generators obtained by lifting generators of the stabilizer in $S$ of the corresponding right coset.

Once we have generators for the cusps of $H$, we can easily check whether or not each cusp contains twist-parabolic elements (once again, simply check whether every element in our generating set is unipotent).

If no cusp contains twist-parabolics, $H$ is $T F \infty$, and we get the self-intersection of the compactifying elliptic curves by computing the abelianization of the cusp groups (this is done by using a presentation for the cusp groups). Recall that the self-intersection of the elliptic curve compactifying a given cusp with unipotent group $U$ is given by the $-k$ where $k$ is the unique positive integer such that $U \cong \mathbb{Z}_{k} \oplus \mathbb{Z} \oplus \mathbb{Z}$, see Proposition 4.2.12 and equation (4.2.15) of [17].
8.1.1. Slight improvements. Since we are mainly interested in studying the smallest index of $T F \infty$ subgroups, for a given finite quotient $F$ of $\Gamma_{d}$, we will not study $\phi^{-1}(S)$ for all subgroups $S$ of $F$.

First, we known the index of torsion-free subgroups must be a multiple of the least common multiple of the order of isotropy groups, which decreases the list slightly. Also,
\begin{itemize}
\item[-] if $S_{1}, S_{2} \subset F$ are conjugate, they clearly give conjugate preimages in $\Gamma_{d}$;
\item[-] if $S_{1} \subsetneq S_{2} \subset F$, then $\phi^{-1}\left(S_{1}\right) \subset \phi^{-1}\left(S_{2}\right)$ has index $\left[S_{1}: S_{2}\right]$, and in particular in that case $\phi^{-1}\left(S_{1}\right)$ will definitely not be optimal.
\end{itemize}
Hence, in searching for subgroups $S$ of $F$, we will discard all sugroups having one conjugate contained in a subgroup $S^{\prime} \subset F$ that has already been studied.
8.1.2. Non-optimality, non-exhaustivity. As far as we know, no efficient bound is known for the index $\left[\Gamma_{d}: \operatorname{Core}\left(\Gamma_{d}, H\right)\right]$ for subgroups $H \subset \Gamma_{d}$ of index $k$ (for example take $k$ to be the smallest index of a $T F \infty$ subgroup in $\Gamma_{d}$ ). If we had such a bound, then we could in principle run an exhaustive computer search, and determine the actual optimal index for $T F \infty$ subgroups (this would of course succeed only if the computer search goes through in reasonable amount of time and memory).

Once again, we insist that the list of subgroups given here is not exhaustive.
8.2. Cusp data for some $T F \infty$ subgroups of index 96 in $\Gamma_{1}$. In order to get Table 16, we used normal subgroups in $\Gamma_{1}$ of index $\leq 8000$. Note that for some entries in the table, we found several non-conjugate subgroups with the same data.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $H /[H, H]$ & \# Cusps & self-intersections & $\left[\Gamma_{1}: \operatorname{Core}_{\Gamma_{1}}(H)\right]$ \\
\hline $\mathbb{Z}_{2}^{2} \oplus \mathbb{Z}^{4}$ & 6 & $(-2)^{6}$ & 384 \\
\hline $\mathbb{Z}_{2} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}^{2}$ & 4 & $(-2)^{2},(-4)^{2}$ & 384 \\
\hline $\mathbb{Z}_{4}^{2} \oplus \mathbb{Z}^{2}$ & 4 & $(-2)^{2},(-4)^{2}$ & 1536 \\
\hline $\mathbb{Z}_{2} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}^{2}$ & 4 & $(-2)^{2},(-4)^{2}$ & 1536 \\
\hline $\mathbb{Z}_{4}^{2} \oplus \mathbb{Z}^{2}$ & 4 & $(-2)^{2},(-4)^{2}$ & 6144 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 16. Numerical invariants for some $T F \infty$ subgroups $H \subset \Gamma_{1}$ of index 96.}
\end{table}
8.3. Cusp data for some $T F \infty$ subgroups of index 96 in $\Gamma_{2}$. In order to get Table 17, we used normal subgroups in $\Gamma_{2}$ of index $\leq 8000$.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $H /[H, H]$ & \# Cusps & self-intersections & $\left[\Gamma_{2}: \operatorname{Core}_{\Gamma_{2}}(H)\right]$ \\
\hline $\mathbb{Z}_{2}^{6} \oplus \mathbb{Z}_{4} \oplus \mathbb{Z}_{8}$ & 8 & $(-4)^{4},(-8)^{4}$ & 384 \\
\hline $\mathbb{Z}_{2}^{3} \oplus \mathbb{Z}_{4}^{2}$ & 6 & $(-8)^{6}$ & 384 \\
\hline $\mathbb{Z}_{2}^{4} \oplus \mathbb{Z}_{4}^{2} \oplus \mathbb{Z}_{8}$ & 8 & $(-2)^{4},(-4)^{2},(-16)^{2}$ & 1536 \\
\hline $\mathbb{Z}_{2}^{6} \oplus \mathbb{Z}_{4} \oplus \mathbb{Z}_{8}$ & 8 & $(-4)^{4},(-8)^{4}$ & 1536 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 17. Numerical invariants for some $T F \infty$ subgroups $H \subset \Gamma_{2}$ of index 96.}
\end{table}
8.4. Cusp data for some $T F \infty$ subgroups of index 72 in $\Gamma_{3}$. In order to get Table 18 , we used normal subgroups in $\Gamma_{3}$ of index $\leq 7776$ (this was chosen to check whether we obtain the same subgroups as in [30], which turns out to be the case).

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $H /[H, H]$ & \# Cusps & self-intersections & $\left[\Gamma_{3}: \operatorname{Core}_{\Gamma_{3}}(H)\right]$ \\
\hline $\mathbb{Z}_{4}$ & 4 & $(-1)^{4}$ & 1944 \\
\hline $\mathbb{Z}_{3} \oplus \mathbb{Z}^{2}$ & 2 & (-1), (-3) & 1944 \\
\hline $\mathbb{Z}^{2}$ & 2 & (-1), (-3) & 5832 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 18. Numerical invariants for some $T F \infty$ subgroups $H \subset \Gamma_{3}$ of index 72.}
\end{table}
8.5. Cusp data for some $T F \infty$ subgroups of index 366 in $\Gamma_{7}$. In order to get Table 19, we used normal subgroups in $\Gamma_{7}$ of index $\leq 70000$.

\begin{table}
\begin{tabular}[t]{|l|l|l|l|}
\hline $H /[H, H]$ & \# Cusps & self-intersections & $\left[\Gamma_{7}: \operatorname{Core}_{\Gamma_{7}}(H)\right]$ \\
\hline $\mathbb{Z}_{7}^{8}$ & 24 & $(-7)^{24}$ & 336 \\
\hline $\mathbb{Z}_{2}^{3} \oplus \mathbb{Z}_{4}^{3}$ & 12 & $(-2)^{2},(-4)^{9},(-8)$ & 10572 \\
\hline $\mathbb{Z}_{7} \oplus \mathbb{Z}_{14}^{3}$ & 18 & $(-1)^{6},(-2)^{3},(-7)^{6},(-14)^{3}$ & 56448 \\
\hline $\mathbb{Z}_{2}^{6} \oplus \mathbb{Z}_{6}$ & 12 & $(-1)^{3},(-2)^{3},(-7)^{3},(-14)^{3}$ & 56448 \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 19. Numerical invariants for some $T F \infty$ subgroups $H \subset \Gamma_{7}$ of index 336.}
\end{table}
8.6. Cusp data for some $T F \infty$ subgroups of index 432 in $\Gamma_{11}$. In order to get Table 20, we used the neat principal congruence subgroup of smallest index in $\Gamma_{11}$ (the corresponding finite quotient has order 5616, and it is isomorphic to $P S L(3,3)$ ).