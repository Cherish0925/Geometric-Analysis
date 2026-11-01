# ALE Ricci-flat Kahler metrics and deformations of quotient surface singularities

- Category: papers
- Identity: arxiv:1102.2672
- Content status: fulltext_ok

---

---
source_file: 1102_2672.pdf
converter: mathpix
format: mmd
---

\title{
ALE RICCI-FLAT KÄHLER METRICS AND DEFORMATIONS OF QUOTIENT SURFACE SINGULARITIES
}

\author{
IOANA ŞUVAINA
}

\begin{abstract}
Let $N_{0}=\mathbb{C}^{2} / H$ be an isolated quotient singularity with $H \subset U(2)$ a finite subgroup. We show that for any $\mathbb{Q}$-Gorenstein smoothings of $N_{0}$ a nearby fiber admits ALE Ricci-flat Kähler metrics in any Kähler class. Moreover, we generalize Kronheimer's results on hyperkähler 4-manifolds [14], by giving an explicit classification of the ALE Ricci-flat Kähler surfaces.

We construct ALF Ricci-flat Kähler metrics on the above non-simply connected manifolds. These provide new examples of ALF Ricci-flat Kähler 4-manifolds, with cubic volume growth and cyclic fundamental group at infinity.
\end{abstract}

\section*{Contents}
1. Introduction ..... 1
2. Smoothings of quotient singularities ..... 3
3. ALE Ricci-flat Kähler metrics via the twistor space ..... 4
4. Classification of ALE Ricci-flat Kähler metrics on surfaces ..... 9
5. Gibbons-Hawking formulation and ALF Ricci-flat Kähler metrics ..... 13
6. An application ..... 15
Acknowledgements ..... 15
References ..... 15

\section*{1. Introduction}

Orbifold Kähler spaces appear naturally in the study of the moduli space of metrics. In this paper we consider quotient orbifolds of the form $\mathbb{C}^{2} / H$ with $H \subset U(2)$ a finite subgroup acting freely on $\mathbb{C}^{2} \backslash\{0\}$. There are two techniques to associate a smooth manifold to a singular space: one is resolving the singularity by introducing an exceptional divisor and the other is deforming the orbifold to a smooth manifold.

If we consider the resolution of the singularity, then there are two cases which behave quite differently. The first case is when $H$ is a subgroup of $S U(2)$. In this situation the singularities are called rational double points, and they are classified to be of type $A_{k}, D_{k}, k \geq 1, E_{6}, E_{7}, E_{8}$, corresponding to the tree configuration of self-intersection (-2) rational curves which appear in the minimal resolution. We call the underlying differential manifold of the minimal resolution an $A_{k}, D_{k}, E_{6}, E_{7}$ or $E_{8}$-manifold. These manifolds are shown to support a hyperkähler structure. They were extensively studied and classified by Eguchi-Hanson [7], Hitchin [9], Gibbons-Hawking [8], Kronheimer [13, 14], Joyce [11] and others. They have proved the existence of asymptotically locally Euclidean

\footnotetext{
${ }^{0}$ The author is supported in part by NSF grant DMS-1007114 .
}
(ALE) Ricci-flat Kähler metrics on these manifolds. In the second case, when $H$ is a subgroup of $U(2)$ rather than $S U(2)$, the minimal resolution has non-trivial canonical line bundle, and hence it does not admit Ricci-flat Kähler metrics. In the special case when the group $H$ is cyclic Calderbank and Singer [5] showed that the minimal resolution admits scalar flat curvature Kähler metrics, which are ALE. To the author's knowledge, little is known for other groups.

The second method of obtaining a smooth manifold is by deforming the singularity. There are again two cases which arise. The first situation, when the subgroup $H$ is a subgroup of $S U(2)$, yields in fact the hyperkähler spaces, but endowed with a different complex structure. Only for $H$ a subgroup of $S U(2)$ the resolution and the smoothed manifolds are diffeomorphic. More details on the results on hyperkähler manifolds will be described in sections 3 and 4. For $H$ a subgroup of $U(2)$, some power of the canonical line bundle of the smoothing of the singularity is trivial and we can prove that the manifold admits a best metric which is ALE Ricci-flat Kähler:

Theorem A. Let $\left(N_{0}, 0\right)$ be an isolated quotient singularity of complex dimension 2. Assume there exists $\pi: \mathcal{N} \rightarrow \Delta \subset \mathbb{C}$ a one-parameter $\mathbb{Q}$-Gorenstein smoothing where $\Delta$ is a disk around the origin and $\pi^{-1}(0)=N_{0}$. Then for arbitrary small $t \in \Delta \backslash\{0\}$ the manifold $N_{t}=\pi^{-1}(t)$ admits an ALE Ricci-flat Kähler metric $g$. More precisely, in any Kähler class of $N_{t}$ there exists a unique ALE Ricci-flat Kähler metric.

We recall that a normal complex space is $\mathbb{Q}$-Gorenstein if it is Cohen-Macaulay and a multiple of the canonical divisor is Cartier [12, 3.1].

In the case of a resolution, we know that the complex structure at infinity is the canonical one. When we consider deformations we need to give a more precise definition of what an ALE Kähler manifold is:

Definition 1.1. Let $H$ be a finite subgroup of $U(2)$ acting freely on $\mathbb{C}^{2} \backslash\{0\}$, and let $h_{0}$ be the Euclidean metric and $J_{0}$ the canonical complex structure on $\mathbb{C}^{2} / H$. We say that a Kähler manifold ( $N, J, g$ ) is an ALE Kähler manifold asymptotically to $\mathbb{C}^{2} / H$ if there exists a compact subset $K \subset N$ and a map $\pi: N \backslash K \rightarrow \mathbb{C}^{2} / H$ which is a diffeomorphism between $N \backslash K$ and the subset $\left\{z \in \mathbb{C}^{2} / H: r(z)>R\right\}$ for some fixed $R \geq 0$, such that $\pi_{*}(g)-h_{0}=O\left(r^{-4}\right)$ and $\pi_{*}(J)-J_{0}=O\left(r^{-4}\right)$.

In the study of hyperkähler 4-manifolds, a key ingredient used both in Hitchin's ([9]) and Kronheimer's ([14]) proofs was the fact that the complex surface is birational to a deformation of a rational double point singularity. We obtain a similar result in the Ricciflat case:

Theorem B. Let $(N, J, g, \omega)$ be a smooth ALE Ricci-flat Kähler surface, asymptotic to $\mathbb{C}^{2} / H$, with $H$ a finite subgroup of $U(2)$ acting freely on $\mathbb{C}^{2} \backslash\{0\}$. The complex manifold $(N, J)$ can be obtained as the minimal resolution of a fiber of a one-parameter $\mathbb{Q}$-Gorenstein deformation of the quotient singularity $\mathbb{C}^{2} / H$. Given any Kähler class $[\omega] \in H^{2}(N, \mathbb{R})$, then $g$ is the unique ALE Ricci-flat Kähler metric $g$ in that class. In particular, if $N$ is not simply connected then its fundamental group is finite and cyclic, its universal cover is an $A$-type manifold, and the deck-transformations are explicitly described.

Remark 1.2. If $N$ is simply connected then $N$ is hyperkähler and the theorem is in fact a reformulation of Kronheimer's classification result. In the case when $N$ is non simply connected, then its universal cover can not be a $D$ or $E$-type manifold.

Remark 1.3. The ALE is a necessary condition in the above classification and it is essential for the proof of the theorem $B$

In section 5, we show that the above non-simply connected manifolds also admit complete asymptotically locally flat (ALF) Ricci-flat Kähler metrics and we also give examples of non-simply connected manifolds with infinite topology which have complete Ricci-flat Kähler metrics, by emulating a construction of Anderson, Kronheimer and LeBrun [1].

If one would like to generalize the 2-dimensional results to higher dimensions, then there are several approaches which are used for obtaining good metrics on resolutions of singularities. There is no analog of the deformation part, as Schlessinger Rigidity Theorem says that quotient singularities $\mathbb{C}^{n} / H$ with singularity of codimension three or more have no non-trivial deformations [18].

\section*{2. Smoothings of quotient singularities}

In this section we give a short summary of the Kollár and Shepherd-Barron's results [12] on the classification of isolated quotient singularities which admit a smoothing.

Definition 2.1. A flat, surjective map $\pi: \mathcal{X} \rightarrow \Delta$, where $\Delta \subset \mathbb{C}$ is an open neighborhood of 0, is called a one-parameter $\mathbb{Q}$-Gorenstein smoothing of a normal variety $X_{0}$, if $\pi^{-1}(0)=X_{0}$, and the following conditions are satisfied.
\begin{itemize}
\item[i)] $\mathcal{X}$ is $\mathbb{Q}$-Gorenstein
\item[ii)] $X_{t}=\pi^{-1}(t)$ is smooth for every $t \in \Delta-\{0\}$.
\end{itemize}

For a definition of a $\mathbb{Q}$-Gorenstein variety and more details on the algebraic geometry aspects see [12, Def. 3.1]. In their paper, Kollár and Shepherd-Barron prove the following classification theorem:

Theorem 2.2. [12, 3.10] An isolated quotient surface singularity ( $N_{0}, 0$ ) which admits a one-parameter $\mathbb{Q}$-Gorenstein smoothing is either a rational double point or a cyclic singularity of type $\frac{1}{d n^{2}}(1, d n m-1)$ for $d>0, n \geq 2$ and $n, m$ relatively prime.

From a topological point of view the two types of singularities are distinguished by the fundamental group of a smoothing. The smoothing of a rational double point is simply connected, while the deformations of the second type have finite cyclic fundamental group. On the algebraic geometric side of the picture this is reflected on the canonical line bundle being trivial, or non-trivial torsion, respectively.

As the rational double point singularities and their preferred metrics are well understood [9, 13], we focus our attention on the second type of orbifolds. A singularity of type $\frac{1}{d n^{2}}(1, d n m-1)$ is a quotient singularity $\mathbb{C}^{2} / \Gamma_{d n^{2}}$, where $\Gamma_{d n^{2}}=\left\{\rho \mid \rho^{d n^{2}}=1\right\}$ is the finite cyclic group of order $d n^{2}$ which acts on $\mathbb{C}^{2}$ diagonally with weights $(1, d n m-1)$, i.e. if $\rho \in \Gamma_{d n^{2}}$ and $\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}$ then $\rho\left(z_{1}, z_{2}\right)=\left(\rho z_{1}, \rho^{d n m-1} z_{2}\right)$. If we consider the subgroup of order $d n, \Gamma_{d n} \subset \Gamma_{d n^{2}}$, then its quotient singularity is of type $\frac{1}{d n}(1,-1)$, which is the $A_{d n-1}$ rational double point singularity. The quotient singularity $\frac{1}{d n}(1,-1)$ can be biholomorphically embedded as a hypersurface in $\mathbb{C}^{3}, \mathbb{C}^{2} / \Gamma_{d n} \rightarrow M_{0}=(x y=$ $\left.z^{d n}\right) \subset \mathbb{C}^{3}$, by the following map: $\left(z_{1}, z_{2}\right) \rightarrow(x, y, z)=\left(z_{1}^{d n}, z_{2}^{d n}, z_{1} z_{2}\right) \in \mathbb{C}^{3}$. On $M_{0}$ there is an induced action of the quotient group $\Gamma_{d n^{2}} / \Gamma_{d n}$. As this group is cyclic of order $n$, we can represent its action by the action of a unit complex number $\xi$ of order $n, \xi^{n}=1$, as follows: $\xi(x, y, z)=\left(\xi x, \xi^{-1} y, \xi^{m} z\right)$.

The deformations of $A$-type singularities $M_{0}$ are known. They are given by $\mathcal{M} \subset$ $\mathbb{C}^{3} \times \mathbb{C}^{d n}, \mathcal{M}=\left(x y=z^{d n}+e_{1} z^{d n-1}+\cdots+e_{d n}\right)$, where $\left(e_{1}, \ldots, e_{d n}\right) \in \mathbb{C}^{d n}$. The
action of the group $\Gamma_{d n^{2}} / \Gamma_{d n}$ can be extended trivially on the coordinates of $\mathbb{C}^{d n}$ :
$$\xi\left(x, y, z, e_{n}, \ldots, e_{d n}\right)=\left(\xi x, \xi^{-1} y, \xi^{m} z, e_{n}, \ldots, e_{d n}\right)$$
Then, there is a special family of deformations $\mathcal{M}^{\prime} \subset \mathbb{C}^{3} \times \mathbb{C}^{d}$ which is $\left(\Gamma_{d n^{2}} / \Gamma_{d n}\right)$-invariant and it is given by the equation
$$x y=z^{d n}+\sum_{j=1}^{d} e_{j n} z^{(d-j) n}$$
where $e_{n}, \ldots, e_{d n}$ are linear coordinates on $\mathbb{C}^{d}$. Let $\mathcal{N}=\mathcal{M}^{\prime} /\left(\Gamma_{d n^{2}} / \Gamma_{d n}\right)$ and $\phi: \mathcal{N} \rightarrow$ $\mathbb{C}^{d}$ be the quotient map of the projection $\mathcal{M}^{\prime} \rightarrow \mathbb{C}^{d}$.

Proposition 2.3. [12] The map $\phi: \mathcal{N} \rightarrow \mathbb{C}^{d}$ is a $\mathbb{Q}$-Gorenstein deformation of the cyclic singularity of type $\frac{1}{d n^{2}}(1, d n m-1)$. Moreover, every one-parameter $\mathbb{Q}$-Gorenstein deformation $\mathcal{X} \rightarrow \Delta$ of a singularity of type $\frac{1}{d n^{2}}(1, d n m-1)$ is isomorphic to the pullback through $\phi$ of some germ of a holomorphic map $(\Delta, 0) \rightarrow\left(\mathbb{C}^{d}, 0\right)$.

If we consider the case of one-parameter $\mathbb{Q}$-Gorenstein deformations which are equivariant under some free action of the cyclic group of order $n, \mathbb{Z}_{n}$, and such that the fibers have isolated singularities, then we can ask if we can obtain a similar classification result. This situation was studied by Manetti in [15] by using Catanese's explicit classification [6] of the automorphism group of rational double point singularities. He proves the following:

Proposition 2.4. Let $\left(N_{0}, 0\right) \subset\left(\mathbb{C}^{3}, 0\right)$ be a rational double point singularity and let $\mu_{n}$ be an action of the finite cyclic group of order $n$ on $\left(N_{0}, 0\right)$ coming from a subgroup of $\operatorname{GL}(3, \mathbb{C})$. Moreover, there exists a one-parameter deformation of $\left(N_{0}, 0\right),(\mathcal{N}, 0) \subset$ $\left(\mathbb{C}^{3} \times \Delta\right) \rightarrow \Delta$ which is $\mu_{n}$ invariant, where the action extends trivially to the $\Delta$ coordinate. Assume further that the $\mu_{n}$ acts freely on $\mathcal{N} \backslash\{0\}$. Then the singularity $\left(N_{0}, 0\right)$ is a singularity of the form $\frac{1}{d n^{2}}(1, d n m-1)$, where $n, m$ are relatively prime integers, and the deformation family is of the form described in Proposition 2.3

\section*{3. ALE Ricci-flat Kähler metrics via the twistor space}

On the minimal resolution of a rational double point singularity, ALE hyperkähler metrics (in particular Ricci-flat Kähler metrics) where constructed by Hitchin [9], Kronheimer [13, 14], and others. In this section we show how their results can be rewritten in the set-up of Theorem B and we analyze in detail the deformations of the second type of singularities from Theorem 2.2 As we observed in Proposition 2.3, these singularities and their deformations are closely related to the $A$-type singularities. We start first by reviewing Hitchin's construction of hyperkähler metrics on deformations of these orbifolds. This is done via the twistor space construction.

The Penrose twistor correspondence [2] is a one-to-one correspondence between halfconformally flat 4-manifolds and complex 3-folds, the twistor spaces, which satisfy certain properties. We will give a short summary of the twistor space of a hyperkähler manifold $M$, by following Hitchin's exposition in [9]. The hyperkähler metrics are antiself-dual if $M$ is endowed with the orientation induced by any of the complex structures. In our particular case, we have the following version of the Penrose correspondence between a simply connected manifold $M$ endowed with a hyperkähler metric $g$ and the complex 3 -fold $Z$ which has the following properties:
\begin{itemize}
\item[(1)] $Z$ is the total space of a holomorphic fibration $\pi: Z \rightarrow \mathbb{C P}^{1}$.
\item[(2)] There exists a 4-parameter family of sections of $\pi$, each with normal bundle $\mathcal{O}(1) \oplus \mathcal{O}(1)$.
\item[(3)] There exists a non-vanishing holomorphic section $s$ of $K_{Z} \otimes \pi^{*} \mathcal{O}(4)$.
\item[(4)] There exists a real structure, i.e. a free anti-holomorphic involution, on $Z$ which is the extension of the antipodal map on $\mathbb{C P}^{1}$, such that $\pi$ and $s$ are real, and $Z$ is fibered by the real sections of the family.
\end{itemize}

The space of real sections recovers the manifold $M$ and the conformal class of the metric. We use property (3) to fix a metric in the conformal class. Property (1) is specific for hyperkähler manifolds. For each $\left[u_{1}: u_{2}\right] \in \mathbb{C P}^{1}$, the projection from $Z$ to the space of real sections identifies $\pi^{-1}\left(\left[u_{1}: u_{2}\right]\right)$ with $M$, which induces a complex structure on $M$ such that the metric $g$ is Kähler.

We give now a short account of the twistor space associated to a smoothing of an $A_{k-1}$-type singularity with a Ricci-flat Kähler metric, by following Hitchin's presentation in [9]. A smoothing of an $A_{k-1}$-singularity is biholomorphic to $M=(x y=$ $z^{k}+e_{1} z^{k-1}+\cdots+e_{k}$ ), for some constants $e_{i}$. In order to construct $Z$ we need a family of complex structures on $M$, parametrized by $\mathbb{C P}^{1}$. Hitchin [9] considers the manifold $\tilde{Z}$
$$x y=z^{k}+e_{1}(u) z^{k-1}+\cdots+e_{k}(u)$$
as a first approximation, where $u$ is an affine coordinate and $e_{i}(u)$ are holomorphic functions. As we need to define a $\mathbb{C} \mathbb{P}^{1}$-family of complex structures, we need to consider the extension of the coordinate $u$ to homogeneous coordinates $\left[u_{1}: u_{2}\right]$ on $\mathbb{C} \mathbb{P}^{1}$, then $e_{i}(u)$ are going to be extended to sections of holomorphic line bundles on $\mathbb{C P}^{1}$, while $x, y, z$ are local coordinates on certain line bundles. Using the properties $(1-4)$ Hitchin shows that $x, y, z$ need to be local coordinates on $\mathcal{O}(k), \mathcal{O}(k), \mathcal{O}(2)$, respectively, while each $e_{i}$ is a section of $\mathcal{O}(2 i)$. Hence $\tilde{Z}$ is a hypersurface in the vector bundle
$$\tilde{Z} \subset \mathcal{O}(k) \oplus \mathcal{O}(k) \oplus \mathcal{O}(2) \rightarrow \mathbb{C P}^{1} .$$
The hypersurface $\tilde{Z}$ has at most rational double point singularities, which can be resolved [9] to obtain a manifold $Z$ which is the twistor space of $M$. Moreover, all the structures defined on $\tilde{Z}$ (properties 1-4) lift to corresponding structures on $Z$.

On $\tilde{Z}$, Hitchin constructs a natural real structure $\tau$ induced from a real structure on $\mathcal{O}(k) \oplus \mathcal{O}(k) \oplus \mathcal{O}(2) \rightarrow \mathbb{C P}^{1}$ (property 4, and a non-vanishing holomorphic section $s$ (property 3 ). The last ingredient missing is a 4 -parameter family of sections. First, we make the assumption, [9], that the equation 3.1 factorizes as:
$$x y=\prod_{i=1}^{k}\left(z-p_{i}\right)$$
where $p_{i} \in \Gamma(\mathcal{O}(2))$. As a function on the affine parameter $u=\frac{u_{1}}{u_{2}} \in U \equiv \mathbb{C} \subset \mathbb{C P}^{1}$ the polynomials $p_{i}$ can be written as $p_{i}(u)=a_{i} u^{2}+2 b_{i} u+c_{i}$. Let $(x(u), y(u), z(u))$ be a section of $\pi: Z \rightarrow \mathbb{C P}^{1}$, and let $\left.z(u)\right)=a u^{2}+2 b u+c$. If we require that $Z$ and $(x(u), y(u), z(u))$ are $\tau$-invariant, then we need to consider $p_{i}(u)$ satisfying $p_{i}(\tau u)=$ $-\tau\left(p_{i}(u)\right)$, or equivalently $c_{i}=-\bar{a}_{i}, b_{i}=\bar{b}_{i}$, and $c=-\bar{a}, b=\bar{b}$. We can solve the equation 3.2 by a simple factorization:
$$x(u)=A \prod_{i=1}^{k}\left(u-\frac{\left(b-b_{i}\right)-\Delta_{i}}{\left(a-a_{i}\right)}\right), y(u)=B \prod_{i=1}^{k}\left(u-\frac{\left(b-b_{i}\right)+\Delta_{i}}{\left(a-a_{i}\right)}\right)$$
where $\Delta_{i}=\sqrt{\left(b-b_{i}\right)^{2}+\left|a-a_{i}\right|^{2}}$ is the discriminant of $z-p_{i}$ and $A, B$ are constant coefficients which must satisfy $A B=\prod\left(a-a_{i}\right)$. The reality condition on the polynomials $x(u)$ and $y(u)$ implies that
$$A \bar{A}=\prod_{i=1}^{k}\left(\left(b-b_{i}\right)+\Delta_{i}\right) .$$

By Penrose correspondence the subspace of real sections $M_{r e}$, can be identified with $M$ endowed with a conformal structure. As we saw, the real sections are parametrized by $(b, \operatorname{Im}(a), \operatorname{Re}(a)) \in \mathbb{R}^{3}$ and the angular coordinate associated to $A$. Moreover, each conformal class is determined by a choice of the real quadratic polynomials $p_{i}$, or equivalently $k$ points $x_{i}=\left(b_{i}, \operatorname{Im}\left(a_{i}\right), \operatorname{Re}\left(a_{i}\right)\right)$ in $\mathbb{R}^{3}$. On this real submanifold, the conformal structure is given by [9, eq.4.4]:
$$\gamma^{2}\left(d b^{2}+d a d \bar{a}\right)+\left(\operatorname{Im}\left(\frac{2 d A}{A}-\delta d a\right)\right)^{2}=\gamma^{2} d a d \bar{a}+\left(\frac{2 d A}{A}-\delta d a\right)\left(\frac{2 d \bar{A}}{\bar{A}}-\bar{\delta} d \bar{a}\right)$$
where
$$\begin{aligned}
& \gamma=\sum_{i=1}^{k}\left(\left(b-b_{i}\right)^{2}+\left|a-a_{i}\right|^{2}\right)^{-\frac{1}{2}}=\sum \Delta_{i}^{-1} \\
& \delta=\sum_{i=1}^{k} \frac{-\left(b-b_{i}\right)+\Delta_{i}}{\Delta_{i}\left(a-a_{i}\right)}
\end{aligned}$$

To recover the metric on $M$, first we assume that $(M, J)$ is identified with the smooth hypersurface corresponding to $\pi^{-1}(0)$, i.e. $M=\left(x y-\Pi\left(z+\bar{a}_{i}\right)\right)$ where $a_{i} \neq a_{j}$, for $i \neq j$. We have local coordinates $(y, z)$ whenever $y \neq 0$. In terms of these local coordinates we have the following identifications:
$$u=0, z=-\bar{a}, y=\frac{1}{A} \prod_{i=1}^{k}\left(\left(b-b_{i}\right)+\Delta_{i}\right)=\bar{A}$$
In these local coordinates, the metric corresponding to the twistor space data is the following [9]:
$$g=\gamma d z d \bar{z}+\gamma^{-1}\left(\frac{2 d y}{y}+\bar{\delta} d z\right)\left(\frac{2 d \bar{y}}{\bar{y}}+\delta d \bar{z}\right)$$
where
$$\begin{aligned}
& \gamma=\sum_{i=1}^{k}\left(\left(b-b_{i}\right)^{2}+\left|\bar{z}+a_{i}\right|^{2}\right)^{-\frac{1}{2}}=\sum_{i=1}^{k} \Delta_{i}^{-1} \\
& \delta=\sum_{i=1}^{k} \frac{\left(b-b_{i}\right)-\Delta_{i}}{\Delta_{i}\left(\bar{z}+a_{i}\right)}
\end{aligned}$$
and $b$ is defined implicitly by
$$\prod_{i=1}^{k}\left(\left(b-b_{i}\right)+\Delta_{i}\right)=y \bar{y} .$$

An easy computation shows that the metric extends smoothly at $y=0$, and that the above metric is asymptotically locally Euclidean and complete.

The Kähler form associated to the metric is given by:
$$\omega_{g}=i \gamma d z \wedge d \bar{z}+i \gamma^{-1}\left(\frac{2 d y}{y}+\bar{\delta} d z\right) \wedge\left(\frac{2 d \bar{y}}{\bar{y}}+\delta d \bar{z}\right)$$

Moreover, Hitchin shows that we can choose a distinguished basis $\gamma_{1}, \ldots, \gamma_{k-1}$, of $H_{2}(M, \mathbb{Z})$ and then the Kähler class of $\omega$ is given by the Poincaré dual of $\sum 8 \pi\left(b_{i}-\right.$ $\left.b_{i+1}\right) \gamma_{i} \in H_{2}(M, \mathbb{R})$.

The condition that $a_{i} \neq a_{j}$ for $i \neq j$, is equivalent to the fact the complex surface $(M, J)=\pi^{-1}(0)$ is smooth. If this condition is not satisfied then both $M$ and $\tilde{Z}$ have singularities above 0, which Hitchin shows that can be resolved by introducing exceptional divisors. If the corresponding $b_{i}$ 's are distinct then there are corresponding second homology classes $\gamma_{i}$ which can be represented by exceptional (-2)- rational curves. Equal corresponding $b_{i}$ 's will yield an orbifold ALE Ricci-flat Kähler space $(M, J, g)$.

We conclude that the metric $g$ is uniquely determined by the complex constants $a_{i}$ which are given by the complex structure $(M, J)$ and the real numbers $\left(b_{i}-b_{i+1}\right), i=$ $1, \ldots, k-1$, which determine the Kähler class of $\omega_{g}$. The Euclidean translation along the $b$-axis induces equivalent metrics. We have the following reformulation of Hitchin's result:

Theorem 3.1 (Hitchin [9]). Let $\left(M_{0}, 0\right)$ be a quotient singularity of type $A_{k-1}$. Let $\left(M_{t}, J_{t}\right)$ be the fiber of a $\mathbb{Q}$-Gorenstein deformation of $\left(M_{0}, 0\right)$, and $(M, J)$ its minimal resolution. For any such $(M, J)$ and any Kähler class $\Omega \in H^{2}(M, \mathbb{R})$ there exists a unique ALE Ricciflat Kähler metric $g$ such that its Kähler form $\omega_{g}$ is in the class $\Omega$.

Remark 3.2. We have argued, by giving full details, that Theorem A is true for $A$-type singularities, but if we consider Kronheimer's results in [13, 14] then the above statement is true for any rational double point singularities.

We return to the case when $k=d n$ and consider the singular manifold $M_{0}=(x y=$ $\left.z^{d n}\right)$ and a smoothing of the form $M=M_{d, n}=\left(x y=z^{d n}-\sum_{i=1}^{d} e_{i} z^{n(d-i)}\right), e_{i} \in \mathbb{C}$. This deformation is $\mathbb{Z}_{n} \cong \Gamma_{d n^{2}} / \Gamma_{d n}$-invariant, where the group $\mathbb{Z}_{n} \cong\left\{\rho \mid \rho \in \mathbb{C}, \rho^{n}=\right.$ 1\} acts by:
$$\rho(x, y, z)=\left(\rho x, \rho^{-1} y, \rho^{m} z\right), \text { where }(m, n)=1$$
We would like to find which of the Ricci-flat Kähler metrics constructed above on $M$ are also $\mathbb{Z}_{n}$-invariant, and for this we need to extend the action to the twistor space associated to $M$.

First, we study the special case of $d=1$, and later discuss the situation of arbitrary $d$. For $d=1$, after a change in coordinates, we can assume $M$ to be given by the equation $\left(x y=z^{n}-1\right)$. This equation can be factored as $x y=\prod_{i=1}^{n}\left(z-\rho^{i}\right)$, where $\rho=e^{\sqrt{-1} \frac{2 \pi}{n}}$. Hence, if we are looking for the twistor space associated to $M$, where the fixed complex structure is obtained at $u=0$, then we are looking for a twistor space which has a first approximation $\tilde{Z} \subset \mathcal{O}_{\mathbb{C P}^{1}}(n) \oplus \mathcal{O}_{\mathbb{C P}^{1}}(n) \oplus \mathcal{O}_{\mathbb{C P}^{1}}(2)$, defined by $x y=\prod_{i=1}^{n}\left(z-p_{i}(u)\right)$, where $p_{i}(u)=-\rho^{-i} u^{2}+2 b_{i} u+\rho^{i}$. Next we need to extend the $\mathbb{Z}_{n}$-action 3.8 to $\mathcal{O}(n) \oplus$ $\mathcal{O}(n) \oplus \mathcal{O}(2) \rightarrow \mathbb{C P}^{1}$, such that $\tilde{Z}$ is invariant. Let $\rho * u$ denote the action on the affine coordinate. The equation $x y=\prod_{i=1}^{n}\left(z-p_{i}(u)\right)$, becomes under the action of $\rho \in \mathbb{Z}_{n}$ :
$$\rho x \rho^{-1} y=\prod_{i=1}^{n}\left(\rho^{m} z-\left(-\rho^{-i}(\rho * u)^{2}+2 b_{i}(\rho * u)+\rho^{i}\right)\right),$$
or equivalently
$$x y=\prod_{i=1}^{n}\left(z-\left(-\rho^{-i-m}(\rho * u)^{2}+2 b_{i} \rho^{-m}(\rho * u)+\rho^{i-m}\right)\right) .$$
Requiring $\tilde{Z}$ to be invariant implies $p_{i-m}(u)=-\rho^{-i-m}(\rho * u)^{2}+2 b_{i} \rho^{-m}(\rho * u)+\rho^{i-m}$, which gives the action on $u, \rho * u=\rho^{m} u$ and also $b_{i}=b_{i-m}$. As $m$ and $n$ are relatively prime, we have that $b_{1}=b_{2}=\cdots=b_{n}$, and we can assume $b_{i}=0$. This fixes the position of the points on $\mathbb{R}^{3}$, as vertices of a regular polygon with $n$ sides, in the plane $b=0$ centered at the origin. Moreover, using the identification 3.5 of the local coordinates, we can identify the exact $\mathbb{Z}_{n}$ action on $M_{r e}$ as follows:
$$\rho(a)=\rho^{-m} a, \rho(A)=\rho A, \text { and } \rho(b)=b$$
To identify the action on the $b$-coordinate, we only need to observe that the defining implicit equation 3.7 is invariant under the action, and as $b$ is a real number, the action is trivial.

An easy computation shows that $\gamma$ is invariant under the $\mathbb{Z}_{n}$-action, while $\rho(\delta)=$ $\rho^{m} \delta$. Hence $g$ is invariant under the free action of $\mathbb{Z}_{n}$ and induces a smooth, complete ALE Ricci-flat Kähler metric on $N=N_{d, n}=M / \mathbb{Z}_{n}$. The quotient metric is locally hyperkähler, but not globally hyperkähler, as $(N, g)$ is a deformation of the manifold $\left(N_{0}=\mathbb{C}^{2} / \Gamma_{d n^{2}}, \hat{g}_{0}\right)$, where $\Gamma_{d n^{2}} \subset U(2)$, but $\Gamma_{d n^{2}}$ is not a subgroup of $S U(2)$, and $\hat{g}_{0}$ is the canonical quotient metric on $\mathbb{C}^{2} / \Gamma_{d n^{2}}$. In terms of our construction of twistor spaces, this translates in the fact that the group acts nontrivially on $u \in \mathbb{C P}^{1}$ (the complex structures on $M$ ) as a rotation by a factor of $\rho^{m}$ fixing the initial complex structure $J$, as well as $-J$.

In the case $d=1$, the quotient manifold $N$ has Euler characteristic equal to $\frac{\chi(M)}{n}=$ $\frac{(1+(n-1))}{n}=1$ and $N$ is a rational homology ball with infinity asymptotic to $\mathbb{C}^{2} / \Gamma_{n^{2}}$. Moreover, proposition 2.3 tells us that there exists a unique smoothing $(N, J)$ up to biholomorphisms. We have showed:

Proposition 3.3. The rational homology ball $(N, J)$, with fundamental group $\mathbb{Z}_{n}$ and infinity of the form $L\left(n^{2}, n m-1\right) \times(R, \infty)$, constructed above admits a unique ALE Ricci-flat Kähler metric.

Given an arbitrary $d$, for the defining polynomial of $M, x y=z^{d n}-\sum_{i=1}^{d} d_{i} z^{n(d-i)}$, we can consider the following factorization $x y=\prod_{i=1}^{d}\left(z^{n}-d_{i}^{\prime}\right)=\prod_{i=1}^{d}\left(z^{n}-c_{i}^{n}\right)$ where $c_{i}^{n}=d_{i}^{\prime}$ and $c_{i}$ has the smallest possible argument. As we assume that $M$ is smooth, then the sets $\left\{c_{i}^{n}=d_{i}^{\prime}\right\}_{i}$ and $\left\{c_{i}\right\}_{i}$ contain distinct numbers. The defining polynomial decomposes furthermore as:
$$x y=\prod_{i=1}^{d} \prod_{j=1}^{n}\left(z-c_{i} \rho^{j}\right)$$
In particular, we have $a_{i, j}=-\bar{c}_{i} \rho^{-j}, i=1, \ldots, d, j=1, \ldots n$..
The same arguments, as in the case $d=1$, give us the position of the $d n$ points $\left(b_{i, j}, \operatorname{Im}\left(a_{i, j}\right), \operatorname{Re}\left(a_{i, j}\right)\right)$ in $\mathbb{R}^{3}$, as the vertices of $d$ regular polygons with $n$ sides, each polygon in a horizontal plane $b_{i, j}=b_{i}=$ constant, $i=1, \ldots, d$, centered at the origin of
the plane $\left(b_{i}, 0,0\right)$ and with one of the vertices at $\left(b_{i},-\bar{c}_{i}\right) \in \mathbb{R} \times \mathbb{C} \cong \mathbb{R}^{3}$. The $\mathbb{Z}_{n}$-actions on $\tilde{Z}$ and $M_{r e}$ are the same as in the simple case 3.9.

The group action rearranges the terms in the formula of $\gamma$ and after factorizing out $\rho^{m}$ we obtain a similar formula for $\delta$, i.e. $\gamma$ is invariant under the $\mathbb{Z}_{n}$ action, while $\rho(\delta)=\rho^{m} \delta$. Hence, the Hitchin's metrics, given by the equation 3.6, are $\mathbb{Z}_{n}$-invariant for the above choice of points. The fact that the $b$-coordinates of the vertices satisfy the conditions $b_{i, j}=b_{i}$ translates to the fact that the Kähler class of the metric is $\mathbb{Z}_{n}$-invariant. Moreover any invariant Kähler class must satisfy these conditions.

We are now ready to give the proof of the main theorem:
Proof of Theorem A From Theorem 2.2 we know that there are only two types of isolated quotient singularities which admit a $\mathbb{Q}$-Gorenstein smoothing. For the first type of singularities the existence of ALE Ricci-flat Kähler metric in any Kähler class was proved by Hitchin [9], for the $A$-singularities, and by Kronheimer [13, 14] in general (according to the reformulation of their results in Theorem 3.1 and Remark 3.2).

In the case of a $\frac{1}{d n^{2}}(1, d n m-1)$ singularity, we saw that a smoothing $N_{t}$ of $\mathbb{C}^{2} / \Gamma_{d n^{2}}$ is the $\mathbb{Z}_{n}$-quotient of a $A_{d n-1}$ manifold, see Proposition 2.3. In this section we looked at the explicit description of Hitchin's metrics on these deformations and proved that the Kähler metric is also group invariant as long as it satisfies the condition that its Kähler class is invariant.

As any Kähler class on $N$ can be pulled back to a $\mathbb{Z}_{n}$-invariant Kähler class on a $A_{d n-1}$-manifold, which contains a unique ALE Ricci-flat Kähler metric [9] (3.1), which we proved is group invariant, hence it induces the needed metric on $N$. \(\square\)

\section*{4. Classification of ALE Ricci-flat Kähler metrics on surfaces}

The simply connected ALE Ricci-flat Kähler surfaces are classified by Kronheimer [14]. These are the ALE hyperkähler surfaces, and their metrics are explicitly described. When the manifolds are not simply connected, the author could not find such a classification in the literature. The present paper is intended to fill in this gap, by giving a complete description of the ALE Ricci-flat Kähler, with emphasis on the non-simply connected case.

In this section we are going to use the Kronheimer's approach to classify the ALE Ricci-flat Kähler surfaces $(M, J, g)$. We will see that the 4-manifold $M$ and the metric $g$ are determined by the topology of the asymptotic end and the Kähler class of the metric, respectively. We prove this by starting with some easy lemmas.

Lemma 4.1. Let $(M, g)$ be an ALE Ricci-flat manifold then the fundamental group of $M$ is finite.

Proof. This is an immediate consequence of the fact that $(M, g)$ is asymptotically locally Euclidean and the Volume Comparison Theorem on Ricci-flat manifolds. The Volume Comparison Theorem for the universal cover $(\widetilde{M}, \widetilde{g})$ tells us that $(\widetilde{M}, \widetilde{g})$ must have volume growth less than that of $\mathbb{R}^{4}$, and as $M$ is ALE we have that the universal cover must be a finite covering of $M$. Hence $\pi_{1}(M)$ is finite. \(\square\)

Lemma 4.2. Let $(M, g)$ be an ALE Ricci-flat 4-manifold, then its universal cover $\widetilde{M}$ has only one end, in particular is ALE.

Proof. If $\widetilde{M}$ is disconnected at infinity, then $(\widetilde{M}, \widetilde{g})$ contains a line ([17, Ch.9]), and as Ric $_{\widetilde{g}} \equiv 0$ the Splitting Theorem tells us that $(\widetilde{M}, \widetilde{g})$ is isometric to a product $\left(N \times \mathbb{R}, g_{0}+\right.$ $d t^{2}$ ). In particular the 3 -dimensional manifold $N$ is Ricci-flat, and hence flat. But as $N$
is simply connected, we have $N$ is the Euclidean space, and so is $\widetilde{M}$. In particular, $\widetilde{M}$ has only one end at infinity. \(\square\)

Remark 4.3. The lemma actually proves a stronger result. If the asymptotic models of $M$ and $\widetilde{M}$ are those of $\mathbb{R}^{4} / H$ and $\mathbb{R}^{4} / \Gamma$, with $H, \Gamma$ finite subgroups of $S O(4)$, and we denote the fundamental group $\pi_{1}(M)$ by $G$, then $H$ is an extension of $\Gamma$ by $G$ :
$$0 \rightarrow \Gamma \rightarrow H \rightarrow G \rightarrow 0 .$$

Proposition 4.4. The universal cover ( $\widetilde{M}, \widetilde{J}, \widetilde{g}$ ) of an ALE Ricci-flat Kähler manifold $(M, J, g)$ is an ALE hyperkähler manifold, and $M$ is obtained by taking the quotient of $\widetilde{M}$ by a finite cyclic group of automorphisms.

Proof. Lemma 4.2 tells us that the universal cover $(\widetilde{M}, \widetilde{g})$ is ALE Ricci-flat Kähler manifold, and as $\widetilde{M}$ is simply connected, it is hyperkähler [10]. In particular, as the metrics are compatible with the complex structure, the asymptotics of $M, \widetilde{M}$ are given by $H, \Gamma$ finite subgroups of $U(2), S U(2)$, respectively.

Let $\Gamma^{\prime}$ be the normal subgroup of $H$ given by $\Gamma^{\prime}=H \cap S U(2)$. Then $\Gamma \subseteq \Gamma^{\prime}$. First we will show that the two subgroups are equal to each other. As $\Gamma^{\prime} / \Gamma$ is a subgroup of $H / \Gamma=G=\pi_{1}(M)$, it has an associated covering $\left(M^{\prime}, g^{\prime}\right) \rightarrow(M, g)$, with $g^{\prime}$ the pullback metric. As $\widetilde{M}$ is the universal cover of $M$, we have a covering $(\widetilde{M}, \widetilde{g}) \rightarrow\left(M^{\prime}, g^{\prime}\right)$. Moreover, $M^{\prime}$ has one end at infinity and the group of deck transformations is given by $\pi_{1}\left(M^{\prime}\right)=\Gamma^{\prime} / \Gamma$. As $\widetilde{M}$ is a hyperkähker manifold, the manifold $M^{\prime}$ will be hyperkähler if $\pi_{1}\left(M^{\prime}\right)$ acts trivially on the canonical bundle $K_{\widetilde{M}}$. But any element in $\pi_{1}\left(M^{\prime}\right)$ can be identified with an element in $\Gamma^{\prime} / \Gamma$, and can be represented be a loop $\gamma$ in the asymptotic model, $\mathbb{C}^{2} / \Gamma^{\prime}$. As $\Gamma^{\prime} \subset \operatorname{SU}(2)$ the loop acts trivially on $K_{\widetilde{M}}$. Hence $M^{\prime}$ is also a hyperkähler manifold. But Kronheimer [14] classified all ALE hyperkähler manifolds, and showed that they are, in particular, simply connected. Hence $\widetilde{M}=M^{\prime}$ and $\Gamma=\Gamma^{\prime}$.

This implies that $H / \Gamma,(\Gamma=H \cap S U(2))$ is a subgroup of $U(2) / S U(2)=S^{1}$. So, $G=H / \Gamma$ is a finite cyclic group. \(\square\)

Remark 4.5. In particular, if the manifold $M$ is not simply connected then it is not hyperkähler, just locally hyperkähler, as the group $G$ acts non-trivially on the canonical bundle $K_{\widetilde{M}}$. Moreover, $M$ is a spin manifold iff the order of $G$ is odd.

By Proposition 4.4, classifying the non-simply connected ALE Ricci-flat Kähler manifolds is equivalent to classifying the finite cyclic free groups of isometries on hyperkähler 4-manifolds.

In the remaining part of this section, we prove that the manifold $\widetilde{M}$ admits a $G$-equivariant degeneration to the quotient orbifold $\mathbb{C}^{2} / \Gamma$. This will lead to an explicit description of $M$ and it will give us a complete classification of the ALE Ricci-flat Kähler manifolds. To do this we go back to Kronheimer's paper [14] and study the $G$-action on the twistor space $Z_{\tilde{M}}$.

As we mentioned in the previous section, to any half-conformally flat (spin) manifold $(X,[g])$ we can associate a complex three-manifold $Z$, its twistor space. If the manifold $(X, g)$ is scalar flat Kähler, then the metric is anti-self-dual (ASD), and its twistor space is the projective bundle $Z=\mathbb{P}\left(V^{+}\right)$, where $V^{+}$is the bundle of self-dual spinors. If we consider the manifold with the reversed orientation $\bar{X}$, then $(\bar{X}, g)$ is a self-dual manifold, and to it we associate the same twistor space $Z$, which now is defined as $\mathbb{P}\left(V^{-}\right)$, where $V^{-}$is the bundle of anti-self-dual spinors on $(\bar{X}, g)$.

Given an ALE Ricci-flat hyperkähler manifold $(\widetilde{M}, \widetilde{g})$, Kronheimer [14] constructs orbifold compactifications of both $\widetilde{M}$ and $Z_{\widetilde{M}}$ asfollows : $\widetilde{\widetilde{M}}=\widetilde{M} \cup\{\infty\}$ and $Z_{\bar{M}}=$ $Z_{\widetilde{M}} \cup\left\{\mathbb{C P}^{1} / \Gamma\right\}$. Let $U^{\prime} \cong\left(\mathbb{R}^{4} \backslash B_{r}(0)\right) / \Gamma$ be a neighborhood of infinity in $\widetilde{M}$, such that $U^{\prime} / G$ is a neighborhood of infinity in $M$ and let $p: \widetilde{U^{\prime}} \rightarrow U^{\prime}$ be the universal cover of $U^{\prime}$. If $x_{i}$ are $H$-invariant local coordinates at infinity in $\widetilde{U}^{\prime}$, then $\widetilde{U}=\widetilde{U}^{\prime} \cup\{\infty\}$ is a smooth chart if we consider the coordinates $y_{i}=x_{i} / r^{2}$. Moreover, if $\phi: \widetilde{M} \rightarrow \mathbb{R}^{+}$is a smooth $G$-invariant function, equal to $1 / r^{2}$ outside some compact set, then the metric $\bar{g}=p^{*}\left(\left.\phi^{2} \widetilde{g}\right|_{U^{\prime}}\right)$ extends to a class $\mathrm{C}^{3}$ metric on $\widetilde{U}[14]$, which is $H$-invariant. Then $(\widetilde{U}, \bar{g})$ defines Riemannian orbifold structures on the compactifications $\overline{\widetilde{M}}=\widetilde{M} \cup\{\infty\}$ and $\bar{M}=M \cup\{\infty\}$. The manifold $\bar{M}$ is obtained from $\overline{\widetilde{M}}$ by taking the quotient by the group $G$, which acts freely on $\widetilde{M}$ and fixes $\infty$ on $\overline{\widetilde{M}}$.

We now construct a compactification of the twistor space $Z$ by defining the twistor space for an orbifold space. As $\bar{g}$ is in the same conformal class as $\widetilde{g}$, it is ASD in $x_{i}$ coordinates. But if we consider $y_{i}$ coordinates, as the transition map is reversing the orientation, the metric is be self-dual. To leading order, $H$ acts linearly on both $x_{i}$ and $y_{i}$ coordinates, by the same representation $\rho_{H}: H \rightarrow U(2)$, and so does its subgroup $\Gamma$. Moreover (see [14, Lemma 2.1]), in $y_{i}$ coordinates the action of $\Gamma$ on $V^{+}$is trivial, but non-trivial on $V^{-}$. For the neighborhood $(\widetilde{U}, \bar{g})$ of $\infty$ we consider the twistor space $Z_{\widetilde{U}}$. As the metric $\bar{g}$ is both $H$ and $\Gamma$-invariant, the actions of $H$ and $\Gamma$ extend to holomorphic actions on $Z_{\widetilde{U}}$. Moreover, if $\widetilde{l}_{\infty} \subset Z_{\widetilde{U}}$ is the twistor line corresponding to the $\infty$, then $H$ and $\Gamma$ act on $\widetilde{l}_{\infty}$ by the standard action of $U(2)$ on $\mathbb{C P}^{1}$ [14]. Let $l_{\infty}=\widetilde{l}_{\infty} / \Gamma$. We define the compactifications of the twistor spaces to be $Z_{\widetilde{M}}=Z_{\widetilde{M}} \cup l_{\infty}$ and $Z_{\bar{M}}=Z_{M} \cup\left(\widetilde{l}_{\infty} / H\right)$, with the complex structures given by $\Gamma, H$-quotients of $Z_{\widetilde{U}}$ in the neighborhoods of the twistor lines at infinity. The complex 3-fold $Z_{\bar{M}}$ is obtained as the quotient $Z_{\bar{M}} / G$, where $G$ acts freely on $Z_{\widetilde{M}}$ and non-trivially on $l_{\infty}$.

As $\widetilde{M}$ is hyperkähler, there is a holomorphic projection $\pi: Z_{\widetilde{M}} \rightarrow \mathbb{C P}^{1}$. The sphere $\mathbb{C} \mathbb{P}^{1}$ gives a $S^{2}$-family of complex structures on $\widetilde{M}$ : to each point $a \in \mathbb{C} \mathbb{P}^{1}$ there is an associated complex structure $J_{a}$ on $\widetilde{M}$ given by the complex structure on the fiber $\pi^{-1}(a) \cong \widetilde{M} \hookrightarrow Z_{\widetilde{M}}$. Note that the compactification $\overline{\widetilde{M}}$ is not hyperkähler and the projection $\pi$ does not extend to the compactification of the twistor space.

Kronheimer's description of the twistor space of $\widetilde{M}$ :
On $Z_{\widetilde{M}}$ there is a preferred line bundle $\pi^{*} \mathcal{O}(1)$. By Hartog's theorem this extends to a line bundle on $Z_{\overline{\widetilde{M}}}$, which can be restricted to a line bundle on $l_{\infty}$. To understand the twistor space $Z_{\widetilde{M}}$, Kronheimer considers the following graded rings:
$$A\left(Z_{\widetilde{M}}\right)=\bigoplus_{k \geq 0} H^{0}\left(Z_{\widetilde{M}}, \pi^{*} \mathcal{O}(k)\right), A\left(l_{\infty}\right)=\bigoplus_{k \geq 0} H^{0}\left(l_{\infty}, \pi^{*} \mathcal{O}(k)\right),$$
and $I \subset A\left(Z_{\widetilde{M}}\right)$ the ideal generated by $u, v$, the pull-backs of the two sections of $\mathcal{O}(1) \rightarrow$ $\mathbb{C P}^{1}$. The two sections $u$ and $v$ are associated to the homogeneous coordinates $[u: v]$ ofn $\mathbb{C P}^{1}$. There is a relation between the graded rings given by [14, Prop. 2.3]:
$$0 \rightarrow I \rightarrow A\left(Z_{\widetilde{M}}\right) \rightarrow A\left(l_{\infty}\right) \rightarrow 0 .$$

If we look at the affine varieties associated to the coordinate rings, the above sequence can be interpreted as saying that there exists a four-dimensional affine variety $Y$ and a fibration $\phi: Y \rightarrow \mathbb{C}^{2} \ni(u, v)$, such that $\phi^{-1}(0,0)=\mathbb{C}^{2} / \Gamma$, i.e. :
$$\begin{array}{cccc}
Y & \supset & \phi^{-1}(0,0) & =\mathbb{C}^{2} / \Gamma \\
\downarrow \phi & & \downarrow & \\
\mathbb{C}^{2} & \ni & (u, v)=(0,0)
\end{array}$$

Moreover [14], $Y$ is a deformation of $\mathbb{C}^{2} / \Gamma(\Gamma \subset \operatorname{SU}(2))$, and it can be considered a subset of $\mathbb{C}^{5}(x, y, z, u, v)$. On $Y$ there is an induced $\mathbb{C}^{*}$ action given by the grading on the $A(\cdot)$ rings such that $\phi$ is $\mathbb{C}^{*}$-equivariant, and the action of $\mathbb{C}^{*}$ on $\mathbb{C}^{2}$ is the usual multiplication. Let $\bar{Z}^{s}=(Y \backslash 0) / \mathbb{C}^{*}$ and $Z^{s}=\left(Y \backslash l^{s}\right) / \mathbb{C}^{*}$, where $l^{s}=\{u=v=$ $0\} \subset \mathbb{C}^{5}$. The map $\phi$ induces a projection $\pi^{s}: Z^{s} \rightarrow \mathbb{C P}^{1}$. Then, $\bar{Z}^{s}$ and $Z^{s}$ are orbifold models of the twistor spaces $Z_{\widetilde{M}}$ and $Z_{\widetilde{M}}$. The singularities of $\bar{Z}^{s}$ and $Z^{s}$ are contained in fibers $\left(\pi^{s}\right)^{-1}(a)$, for finitely many points $a \in \mathbb{C P}^{1}$ ([14, Lemma 2.7]), and they correspond to contracting the holomorphic 2-spheres of self-intersection (-2) in $\left(\widetilde{M}, J_{a}\right) \approx\left(\pi^{-1}(a) \subset Z_{\widetilde{M}}\right)$. The twistor space $Z_{\widetilde{M}}$ is obtained by taking the simultaneous minimal resolution $\chi: Z_{\widetilde{M}} \rightarrow Z^{s}$, and we have the following commuting diagram:
$$\begin{array}{ccc}
Z_{\widetilde{M}} & \xrightarrow{\chi} & Z^{s} \\
\downarrow \pi & & \downarrow \pi^{s} \\
\mathbb{C P}^{1} & \stackrel{=}{\rightarrow} & \mathbb{C P}^{1}
\end{array}$$
Moreover, $\chi$ extends to the compactifications of the twistor spaces $\bar{\chi}: Z_{\overline{\widetilde{M}}} \rightarrow \bar{Z}^{s}$ [14].
In the remaining part of the section we redirect our attention towards the study of the manifold $(M, J, g)$ by looking at the equivariant objects associated to its universal cover with induced complex structure and metric $(\widetilde{M}, \widetilde{J}, \widetilde{g})$. The group $G \cong \pi_{1}(M)$ acts freely on $(\widetilde{M}, \widetilde{J}, \widetilde{g})$ by holomorphic isometries. An equivalent definition of the twistor space of a manifold is given by the space of unit self-dual forms $S\left(\Lambda^{+}\right)$[4]. Thinking of $Z_{\widetilde{M}}$ in this way, we see that there is an induced free action of the group $G$ on the twistor space, and as the action of $G$ on $\widetilde{M}$ is by isometries, the induced action on $Z_{\widetilde{M}}$ is holomorphic. As the constructions are canonical, the twistor space $Z_{M}$ is obtained as the quotient $Z_{\widetilde{M}} / G$, and the same is true for their compactifications: $Z_{\bar{M}}=Z_{\overline{\widetilde{M}}} / G$.

As $\widetilde{M}$ is hyperkähler there is a global trivialization of $S\left(\Lambda^{+}\right)$, and the $G$ will act on this bundle by fixing two points in each fiber, the self-dual forms associated to the complex structures $\widetilde{J}$ and $-\widetilde{J}$. The action of $G$ on $S\left(\Lambda^{+}\right)$is non-trivial, as $G$ gives the extension of the group $\Gamma \subset \operatorname{SU}(2)$ to $H \subset U(2)$. The projection $\pi: Z_{\widetilde{M}} \rightarrow \mathbb{C P}^{1}$ is induced by this trivialization and, eventually after reparametrization of bundle $S\left(\Lambda^{+}\right)$, we can assume that $G$ acts on the fibration $Z_{\widetilde{M}} \rightarrow \mathbb{C P}^{1}$ such that the action on $\mathbb{C P}^{1}$ has exactly two fixed points [0 : 1] and [1 : 0]. Let's assume that the fiber $\pi^{-1}([0: 1])$ can be identified to $(\widetilde{M}, \widetilde{J})$. Moreover, as $G \cong \mathbb{Z}_{n}$ and the action of $G$ on $\mathbb{C P}^{1}$ is holomorphic and non-trivial, it is of the form $\rho[u: v]=\left[\rho^{k} u: v\right]$, where $\rho \in G$ is thought of as a $n^{t h}$ root of unity and $k$ is some integer associated to the action $G$. We can conclude the following about the twistor space of $M$ :

Proposition 4.6. The twistor space $Z_{M}$ does not fiber over $\mathbb{C P}^{1}$, but instead there is a holomorphic fibration: $Z_{M} \rightarrow\left(\mathbb{C} \mathbb{P}^{1} / G\right)$. The generic fiber is diffeomorphic to $\widetilde{M}$, while the fibers above the two singular points are $(M, \pm J)$.

Proof of Theorem B As we have seen in Section 3, Theorem 3.1, Remark 3.2, the simply connected case is completely understood from the work of Hitchin [9] and Kronheimer [13, 14]. We will finish the proof by treating the non-simply connected case.

The map $\chi: Z_{\widetilde{M}} \rightarrow Z^{s}$ (4.3) is given by contracting the exceptional (-2)-spheres on each fiber of $\pi$, or equivalently looking at the fibration of the canonical models of the fibers. Hence the $G$-holomorphic action on $Z_{\widetilde{M}}$ induces a $G$-holomorphic action on $Z^{s}$ which is compatible with the fibration $\pi^{s}: Z^{s} \rightarrow \mathbb{C P}^{1}$, where $G$ acts on $\mathbb{C P}^{1}$ as before, with fixed points [0 : 1] and [1 : 0].

The manifold $\widetilde{M}$ is mapped to $\left(\pi^{s}\right)^{-1}([0: 1]) \subset Z^{s}$ by $\chi$. As $\widetilde{M}$ is an ALE hyperkähler manifold the only exceptional curves are a finite number of holomorphic spheres of selfintersection -2 , which are either isolated or form a tree configuration of type $\mathrm{A}, \mathrm{D}$ or E . The group $G$ acts freely and holomorphically on $\widetilde{M}$ hence it is going to take holomorphic spheres and configurations of holomorphic spheres to them-selves. If $G$ or a subgroup of $G$ fixes such a configuration, then $G$ or the subgroup has to permute both the spheres and the intersection points of the spheres of that configuration (as the action of $G$ is free). But as we have a tree configuration of spheres, there is one more sphere than intersection points, hence the subgroup of $G$ fixing a configuration of holomorphic spheres must be trivial. So, if we consider the manifold $\widetilde{M}^{s} \cong\left(\pi^{s}\right)^{-1}([0: 1]) \subset Z^{s}$, the canonical model of $\widetilde{M}$, then the induced action of $G$ on $\left(\pi^{s}\right)^{-1}([0: 1])$ is free. The quotient $\widetilde{M}^{s} / G=: M^{s}$ is the canonical model of the manifold $(M, J)$.

The fibration $\pi^{s}: Z^{s} \rightarrow \mathbb{C} \mathbb{P}^{1}$ is obtained by taking the $\mathbb{C}^{*}$-quotient of $\phi:\left(Y \backslash l^{s}\right) \rightarrow$ $\mathbb{C}^{2} \backslash\{0\}$, where $\mathbb{C}^{*}$ acts on $\mathbb{C}^{2}$ by scalar multiplication. Hence, the $G$-action on $Z^{s}$ induces an action on $Y \backslash l^{s}$. To see how this action acts on the central fiber $\phi^{-1}(0) \cong\left(\mathbb{C}^{2} / \Gamma\right)$ we have to remember that the central fiber is associated to the orbifold compactification of the twistor space to $\overline{Z^{s}}=Z^{s} \cup\left(\mathbb{C P}^{1} / \Gamma\right)=(Y \backslash\{0\}) / \mathbb{C}^{*}$. But the compactification of $Z_{M}$ is $Z_{M} \cup\left(l_{\infty} / G\right)=Z_{M} \cup\left(\mathbb{C P}^{1} / H\right)$. Hence the action of $G=H / \Gamma$ on $\mathbb{C}^{2} / \Gamma$ must be such that $\left(\mathbb{C}^{2} / \Gamma\right) / G=\left(\mathbb{C}^{2} / \Gamma\right) /(H / \Gamma) \cong \mathbb{C}^{2} / H$.

Let $L$ be the line in $\mathbb{C}^{2}$ corresponding to the point $[0: 1] \in \mathbb{C P}^{1} \cong\left(\mathbb{C}^{2} \backslash\{0\}\right) / \mathbb{C}^{*}$, and let $\mathcal{X}=\phi^{-1}(L) \subset Y$. As $Y$ is a deformation of a rational double point singularity, $\phi: \mathcal{X} \rightarrow L$ is a 1 -parameter Gorenstein deformation of $Y_{0}=\mathbb{C}^{2} / \Gamma$. Moreover the action of $G$ restricts to $\mathcal{X}$, it is compatible with the fibration, and $G$ acts trivially on $\mathbb{C}=L$. Hence we have $\phi: \mathcal{X} / G \rightarrow \mathbb{C}$ is a 1-parameter $\mathbb{Q}$-Gorenstein deformation of $Y_{0} / G \cong \mathbb{C}^{2} / H$. We can use Theorem 2.2 if $M$ does not contain exceptional (-2)-rational curves, or Proposition 2.4 otherwise, to conclude that $H$ is a finite cyclic group generated by a matrix of the form
$$\left(\begin{array}{cc}
\rho & 0 \\
0 & \rho^{d n m-1}
\end{array}\right)$$
with $\rho$ a root of unity of order $d n^{2}$, where $n \geq 2$, and $m$ and $n$ are relatively prime. This also implies that the universal cover of $M$ has to be an $A$-type manifold, and the $\mathbb{Z}_{n}$ action is the one given in Proposition 2.3.

Moreover, $M$ is obtained from the 1 -parameter $\mathbb{Q}$-Gorenstein deformation of $\mathbb{C}^{2} / H$ given by $\phi: \mathcal{X} / G \rightarrow \mathbb{C}$, and if the fiber $M^{s}$ has singularities, they must be of the type $A$ and $M$ is the minimal resolution of $M^{s}$. The metric $g$ is the unique Ricci-flat Kähler metric in a given Kähler class. \(\square\)

\section*{5. Gibbons-Hawking formulation and ALF Ricci-flat Kähler metrics}

Hitchin's approach defines the metrics on $M$ via the twistor space. An alternative construction of these metrics is due to Eguchi, Hanson [7] on $A_{1}$ and Gibbons, Hawking [8] on
any $A_{k}$-surfaces. It uses essentially the $S^{1}$-action on $\left(z_{1}, z_{2}\right) \in \mathbb{C}^{2}$, seen as a subgroup of $S U(2)$, or equivalently the representation of the angular coordinate of $A$, as in section 3.

Let $x_{i}, i=1, \ldots, k$, be a collection of $k$ points in $\mathbb{R}^{3}$. Let $V(x)=\frac{1}{2} \sum_{i=1}^{k} \frac{1}{\left|x-x_{i}\right|}$ be a function defined on $\mathbb{R}^{3} \backslash\left\{x_{i}\right\}$. It can be easily checked that $\left[\frac{1}{2 \pi} * d V\right] \in H^{2}\left(\mathbb{R}^{3} \backslash\right.$ $\left\{x_{i}\right\}, \mathbb{Z}$ ), where $*$ denotes the Hodge star operator on the Euclidean $\mathbb{R}^{3}$. Associated to this cohomology class there is a principal $S^{1}$ bundle on $\mathbb{R}^{3} \backslash\left\{x_{i}\right\}$. Let $\pi^{\prime}: N^{\prime} \rightarrow \mathbb{R}^{3} \backslash\left\{x_{i}\right\}$ be the total space of the bundle, with the natural projection. Locally in a neighborhood of a point $x_{i}$, the Chern class of the $S^{1}$ bundle is -1, hence locally our bundle $N^{\prime}$ is just the $S^{1}$ bundle corresponding to the Hopf fibration $\mathbb{R}^{4} \backslash\{0\}=\mathbb{C}^{2} \backslash\{0\} \rightarrow \mathbb{R}^{3} \backslash\{0\}$, where the $S^{1}$ action is multiplication by the unit complex numbers. We can then smoothly compactify $N^{\prime}$ to $N=N^{\prime} \cup\left\{\bar{x}_{1}, \ldots, \bar{x}_{k}\right\}$ by adding a point $\bar{x}_{i}$ corresponding to each $x_{i}$. The $S^{1}$ action extends on $N$ by having the points $\left\{\bar{x}_{1}, \ldots, \bar{x}_{k}\right\}$ as its fixed points. Notice that the manifold $N$ has the same description as the smooth manifold $M_{r e}$ associated to the deformation of a $A_{k}$ singularity and hence the same topology at infinity.

Let $\omega$ be a connection 1 -form on $N^{\prime}$ such that $d \omega=\pi^{\prime *}(* d V)$. Let
$$g_{0}=\frac{1}{V} \omega^{2}+V \pi^{\prime *} d s^{2}$$
be a metric on $N^{\prime}$ where $d s^{2}$ is the Euclidean metric on $\mathbb{R}^{3}$. Then $g_{0}$ extends to a smooth ALE Ricci-flat metric $g$ on $N$, which is known as the Gibbons-Hawking metric [8]. A different choice of the connection $\omega$ will induce an isometric metric.

If we consider the differential manifold obtained by smoothing a $\frac{1}{d n^{2}}(1, d n m-1)$ singularity, we need to restrict ourselves to the case $k=d n$, and choose the points $x_{i}$ to be the vertices of $d$ regular polygons, each with $n$ sides, laying in horizontal planes ( $b=c t$ ) and centered at the origin. Then the manifold $N^{\prime}$ admits an isometric action of the group $\mathbb{Z}_{n}$ analogous to the action 3.9:
$$\text { if } \rho \in \mathbb{C}, \rho^{n}=1 \text {, then } \rho(a)=\rho^{-m} a, \rho(b)=b \text {, and } \rho(\theta)=\rho \theta$$
where $(a, b) \in \mathbb{C} \times \mathbb{R} \cong \mathbb{R}^{3}$ and $\theta \in S^{1}$ is a local coordinate of the principle $S^{1}$ bundle, and on each fiber the action of the group $\mathbb{Z}_{n}$ is just the action of the finite subgroup of order $n$. This action extends to a free action on $N$. The quotient manifold $N / \mathbb{Z}_{n}$ is diffeomorphic to the smoothing of a $\frac{1}{d n^{2}}(1, d n m-1)$ singularity. Moreover as both the function $V$ and the connection 1-form are group invariant, we have an induced ALE Ricci flat metric on the quotient space. On $N$, [1 Sec.2], we can define a $\mathbb{Z}_{n}$-invariant complex structure as follows: given $\frac{\partial}{\partial \theta}, \frac{\partial}{\partial b}, \frac{\partial}{\partial a_{1}}=\frac{\partial}{\partial \operatorname{Re}(a)}, \frac{\partial}{\partial a_{2}}=\frac{\partial}{\partial \operatorname{Im}(a)}$ the vector basis associated to the local coordinates $(\theta, b, a) \in N^{\prime}$, the complex structure $J$ is defined as $J\left(V^{\frac{1}{2}} \frac{\partial}{\partial \theta}\right)=$ $\frac{\partial}{\partial b}, J\left(V^{-\frac{1}{2}} \frac{\partial}{\partial a_{1}}\right)=V^{-\frac{1}{2}} \frac{\partial}{\partial a_{2}}$. An easy check shows that $J$ is integrable, compatible with the metric $g_{0}$ and extends to the total space $N$, [1].

As in the ALE-case, we can use the above description to construct ALF (asymptotically locally flat) Ricci-flat Kähler metrics on a manifold obtained by smoothing a $\frac{1}{d n^{2}}(1, d n m-$1) singularity. A metric is said to be ALF if the complement of a compact subset is finitely covered by $\left(\mathbb{R}^{3} \backslash\right.$ Ball $) \times S^{1}$ with the metric decaying to the flat product metric. These metrics are obtained by replacing the function $V(x)$, with $V^{\prime}(x):=1+V(x)$. In this case, the above construction is going to give an ALF Ricci-flat Kähler metric on the same smooth space $N$. These metrics are know as the multi-Taub-NUT metrics. As $V^{\prime}(x)$ is $\mathbb{Z}_{n}$ invariant, we have an induced ALF Ricci-flat Kähler metric on $N / \mathbb{Z}_{n}$.

In his paper [16], Minerbe gives a classification of gravitational instantons (hyperkähler metrics) of cyclic type, showing that they are the flat $\mathbb{C} \times \mathbb{C} / \mathbb{Z}$ or the multi-Taub-NUT manifolds. If one wants to generalize his classification, to a classification of ALF Ricciflat Kähler 4-manifolds, then the above quotients should be included.

Another application of the Gibbons-Hawking construction is in the spirit of AndersonKronheimer-LeBrun's result [1]. We can choose infinitely many points $\left\{x_{i}\right\}_{i \in \mathbb{N}} \subset \mathbb{R}^{3}$ arranged in $n$-tuples which are vertices of infinitely many regular polygons $P_{j}, j \in$ $\mathbb{N}$. The polygons, $P_{j}$ are chosen to have all $n$ sides, lie on horizontal planes (constant $b$-coordinates) and inscribed in circles of radii $j^{2}$ centered about the $b$-axis. Then, as in [1], we have constructed a manifold $N_{\infty}$ with infinite homology. Moreover, the metric and complex structure are invariant under a $\mathbb{Z}_{n}$ free action of the form 5.1. Hence, on the non-simply connected manifold $N_{\infty} / \mathbb{Z}_{n}$ there is an induced complete Ricci-flat Kähler metric.

The above examples of Ricci-flat Kähler manifolds which are ALF or have infinite topology lead us to conclude that the ALE condition on our classification is not only necessary for our proofs, but without it the classification is not known.

\section*{6. An application}

The deformations of singularities in this paper give us a local model for smoothing an orbifold and constructing good metrics on a nearby space. We would also like to understand if the same is true for global deformations of compact orbifolds. In this context we can address the following problem: If the orbifold manifold is endowed with a good orbifold Kähler metric, does a nearby smoothing admit a good metric? The author answers positively this question in the case of constant scalar curvature Kähler metric in [19] (in preparation). The more precise result is the following:

Theorem 6.1. [19] Let $\left(M_{0}, g_{0}\right)$ be a compact constant scalar curvature Kähler orbifold of dimension two with isolated singularities. Assume that there is no non-zero holomorphic vector field vanishing somewhere on $M_{0}$ and that $M_{0}$ admits a one-parameter $\mathbb{Q}$-Gorenstein smoothing $\pi: \mathcal{M} \rightarrow \Delta \subset \mathbb{C}$. Then any manifold $M_{t}=\pi^{-1}(t)$ sufficiently close to $M_{0}$ admits a constant scalar curvature Kähler metric.

\section*{Acknowledgements}

The author would like to thank Professor Claude LeBrun for stimulating discussions on the subject.

\section*{References}
\begin{itemize}
\item[] [1] M. Anderson, P. Kronheimer, C. LeBrun, Complete Ricci-flat Kähler manifolds of infinite topological type, Comm. Math. Phys. 125 (1989), no. 4, 637-642
\item[] [2] M.F. Atiyah, N.J. Hitchin, I. M. Singer, Self-duality in four-dimensional Riemannian geometry, Proc. Roy. Soc. London Ser. A 362 (1978), no. 1711, 425-461
\item[] [3] S. Bando, R. Kobayashi, Ricci-flat Kähler metrics on affine algebraic manifolds. II. Math. Ann. 287 (1990), no. 1, 175-18
\item[] [4] A. Besse, Einstein manifolds, Springer-Verlag, Berlin, 1987
\item[] [5] D. Calderbank, M. Singer, Einstein metrics and complex singularities. Invent. Math. 156 (2004), no. 2, 405-443
\item[] [6] F. Catanese, Automorphisms of rational double points and moduli spaces of surfaces of general type. Compositio Math. 61 (1987), no. 1, 81102
\item[] [7] T. Eguchi, A. Hanson, Asymptotically flat solution to Euclidean gravity, Phys. Lett. 74 B (1978), 249251
\item[] [8] G. Gibbons, S. Hawking, Gravitational multi-instantons, Phys. Lett.78B, 430-432 (1978)
\end{itemize}
[9] N.J. Hitchin, Polygons and gravitons, Math. Proc. Cambridge Philos. Soc. 85 (1979), no. 3, 465-476.
[10] N.J. Hitchin, A. Karlhede, U. Lindström, M. Roçek, Hyper-Kähler metrics and supersymmetry, Comm. Math. Phys. 108 (1987), no. 4, 535-589
[11] D. Joyce, Compact manifolds with special holonomy, Oxford Mathematical Monographs. Oxford University Press, Oxford, 2000
[12] J. Kollár, N.i. Shepherd-Barron, Threefolds and deformations of surface singularities, Invent. Math. 91 (1988), no. 2, 299-338
[13] P. B. Kronheimer, The construction of ALE spaces as hyper-Kähler quotients, J. Differential Geom. 29 (1989), no. 3, 665-683
[14] P. B. Kronheimer, A Torelli-type theorem for gravitational instantons, J. Differential Geom. 29 (1989), no. 3, 685-697
[15] M. Manetti, Q-Gorenstein smoothings of quotient singularities. Preprint Scuola Normale Superiore Pisa (1990)
[16] V. Minerbe, Rigidity for Multi-Taub-NUT metrics, arXiv:0910.5792
[17] P. Petersen, Riemannian geometry, Second edition. Graduate Texts in Mathematics, 171. Springer, New York, 2006
[18] M. Schlessinger, Rigidity of quotient singularities, Invent. Math. 14 (1971), 1726
[19] I. Şuvaina, Constant scalar curvature Kähler metrics and deformation of 2-orbifolds, in preparation
[20] G. Tian, J. Viaclovsky, Moduli spaces of critical Riemannian metrics in dimension four. Adv. Math. 196 (2005), no. 2, 346-372

Ioana Şuvaina, Department of Mathematics, 1326 Stevenson Center, Vanderbilt University, Nashville, TN, 37240
E-mail address: ioana.suvaina@vanderbilt.edu
