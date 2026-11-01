---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Positivity of the Cotangent Bundle of Complex Hyperbolic ...]

---
source_file: 2212_10816v3.pdf
converter: mathpix
format: mmd
---

\title{
POSITIVITY OF THE COTANGENT BUNDLE OF COMPLEX HYPERBOLIC MANIFOLDS WITH CUSPS
}

\author{
SOHEIL MEMARIANSORKHABI
}

\begin{abstract}
Let $\bar{X}$ be the toroidal compactification of a cusped complex hyperbolic manifold $X=\mathbb{B}^{n} / \Gamma$ with the boundary divisor $D=\bar{X} \backslash X$. The main goal of this paper is to find the positivity properties of $\Omega \frac{1}{X}$ and $\Omega \frac{1}{X}(\log (D))$ depending intrinsically on $X$. We prove that $\Omega_{\bar{X}}^{1}(\log (D))\langle-r D\rangle$ is ample for all sufficiently small rational numbers $r>0$, and $\Omega_{\bar{X}}^{1}(\log (D))$ is ample modulo $D$. Further, we conclude that if the cusps of $X$ have uniform depth greater than $4 \pi$, then $\Omega \frac{1}{X}$ is semi-ample and is ample modulo $D$, all subvarieties of $X$ are of general type, and every smooth subvariety $V \subset \bar{X}$ intersecting $X$ has ample $K_{V}$. Finally, we show that the minimum volume of subvarieties of $\bar{X}$ intersecting both $X$ and $D$ tends to infinity in cofinal towers of normal covering of $X$.
\end{abstract}

\section*{1. Introduction}

Let $\mathcal{H}$ be a bounded symmetric domain and $X:=\Gamma \backslash \mathcal{H}$ be a quotient of $\mathcal{H}$ by a torsion-free lattice $\Gamma \subset \operatorname{Aut}(\mathcal{H})$. Various hyperbolicity properties of a toroidal compactification $\bar{X}$ of $X$ and curves in $\bar{X}$ have been proved by studying the positivity of $\mathbb{Q}$-line bundles $K_{\bar{X}}(D)-r D$, where $D$ is the boundary divisor, $K_{\bar{X}}(D)$ is the log-canonical bundle and $r$ is a number varying on an interval, the size of which depends on $X$. For instance, see [Nad89, SB05] for the case of moduli space of principally polarized abelian varieties $\mathcal{A}_{g}$, [BT18a] for the case of Hilbert modular varieties and [BT18b, DCDC15] for the case of ball quotients.

Motivated by these results for the twists of $K_{\bar{X}}(D)$ and their implications for the hyperbolicity properties, we study the positivity of the twists of $\Omega_{\bar{X}}^{1}(\log (D))$ and $\Omega_{\bar{X}}^{1}$ in the form of the $\mathbb{Q}$-vector bundles $\Omega \frac{1}{\bar{X}}(\log (D))\langle-r D\rangle$ and $\Omega \frac{1}{\bar{X}}\langle-r D\rangle$. As the vector bundles $\Omega \frac{1}{\bar{X}}(\log (D))$ and $\Omega \frac{1}{X}$ restrict well to subvarieties (of arbitrary dimensions), the positivity of these bundles reveals various hyperbolicity properties of subvarieties of $\bar{X}$.

In this paper, we focus on this problem for a complex ball quotient $X=\Gamma \backslash \mathbb{B}^{n}$, where $\Gamma \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$ is a torsion-free lattice. We refer to $X$ as a complex hyperbolic manifold with cusps, where cusps correspond to parabolic fixed points of $\Gamma$. For cusps of $X$ we used a uniform depth $d$ to measure the size of the largest embedded cusp neighborhoods which are disjoint from each other (see 2.3). We know that the uniform depth of cusps is at least 2 and it tends to infinity in the cofinal towers of normal covering (see Lemma 2.6).

Our first main result is the following theorem:
Theorem A. Let $X$ be a complex hyperbolic manifold with cusps whose toroidal compactification $\bar{X}$ has no orbifold points, and $d$ be the uniform depth of cusps. Then, the $\mathbb{Q}$-vector bundle
$$\Omega_{\bar{X}}^{1}(\log (D))\langle-r D\rangle$$
is ample for all rational $r \in(0, d / 4 \pi)$.

It was known that for small enough $\epsilon>0$, the $\mathbb{Q}$-vector bundle $\Omega \frac{1}{X}(\log (D))\langle-\epsilon D\rangle$ is big. Combining this with the observation of Mumford [Mum77, section 4], Brunebarbe([Bru20b]) and Cadorel([Cad21b]) proved that for a cover $X^{\prime} \rightarrow X$ such that the ramification index of each cusp is at least $l$, the $\mathbb{Q}$-vector bundle $\Omega_{\overline{X^{\prime}}}^{1}\left(\log \left(D^{\prime}\right)\right)\left\langle-l \epsilon D^{\prime}\right\rangle$ is big, where $\overline{X^{\prime}}$ is the toroidal compactification of $X^{\prime}$, and $D^{\prime}$ is the boundary divisor. By assuming that the ramification index $l$ is sufficiently large, they conclude the bigness of the cotangent bundle $\Omega \frac{1}{X^{\prime}}$ on the cover $X^{\prime}$ (see [Cad21b, Theorem 4] and [Bru20b, sec 6.2]).

Theorem A, however, not only has stronger positivity conclusion for the twisted bundle, but also it has an advantage that it implies the positivity result for $X$ itself rather than some cover of $X$. Notably, in Theorem A, the quantity $r$ can be chosen to be a rational number close to $1 / 2 \pi$ for all $X$, since $d$ is always greater than or equal to 2. In particular, Theorem A can be applied when $X$ is not a cover of other locally symmetric domains, i.e, in the case that $\Gamma$ is a maximal lattice in $\operatorname{Aut}\left(\mathbb{B}^{n}\right)$ (for every even $n$, there exits infinitely many such lattices, see for example [ES14]).

Assuming that the uniform depth of cusps is sufficiently large, we showed that $\Omega_{\bar{X}}^{1}$ is semi-ample and is ample modulo $D$ :
Theorem B. With $X$ and $\bar{X}$ as in Theorem A, suppose that the uniform depth of cusps is greater than $4 \pi$. Then, the cotangent bundle $\Omega_{\bar{X}}^{1}$ is semi-ample and is ample modulo $D$.

It is remarkable that for some towers of coverings, the uniform depth of cusps can increase while the ramification index remains unchanged. For instance, the uniform depth of cusps of the classical modular curve $X_{0}(p)$ tends to infinity as $p$ approaches infinity; however, $X_{0}(p) \rightarrow X(1)$ has a cusp with a ramification index of 1 for every $p$ (see Remark 2.7 for details). Such towers play a crucial role in number theory, as seen in Wiles's proof of Fermat's Last Theorem (see [Wil95]) and Mazur's torsion theorem (see [MG78]). Higher-dimensional analogues of these towers are natural objects to study for generalizing these theorems (see [BT18a]). Proving the hyperbolicity properties of these towers, which have a cusp with ramification index 1, is not within reach with the methods used in [Bru20b, Bru20a, Cad21b].

Semi-ampleness of $\Omega \frac{1}{X}$ in Theorem B implies that symmetric differentials over $\bar{X}$ forms a finitely generated $\mathbb{C}$-algebra(see [Laz17, Example 2.1.29]):
Corollary C. With the same assumptions as Theorem B, the graded ring
$$\bigoplus_{n \geq 0} H^{0}\left(\bar{X}, S^{n} \Omega \frac{1}{\bar{X}}\right)$$
is finitely generated $\mathbb{C}$-algebra.
In Theorem A, $\Omega_{\bar{X}}^{1}(\log (D))$ can not be replaced by $\Omega_{\bar{X}}^{1}$ without adding any extra assumptions about $X$ because there are examples due to Hirzebruch [Hir84] of the toroidal compactification of a 2-dimensional ball quotient whose canonical bundle is not even nef. We showed that assuming the uniform depth is sufficiently large the replacement is possible as long as $r$ varies on a smaller interval.
Theorem D. With $X$ and $\bar{X}$ as in Theorem A, suppose that the uniform depth of cusps $d$ is greater than $4 \pi$. Then, the $\mathbb{Q}$-vector bundle
$$\Omega \frac{1}{\bar{X}}\langle-r D\rangle$$
is ample for all rational $r \in(0,-1+d / 4 \pi)$.

As the cotangent bundle is well-behaved under the restriction to subvarieties, by virtue of Theorem D we get hyperbolicity of subvarieties of an arbitrary dimension in the following sense:

Corollary E. With the same notations as in Theorem $A$, suppose $V$ is a smooth subvariety of $\bar{X}$ intersecting $X$ with dimension $m>0$. Then,
$$K_{V}-(r-1) D_{\mid V}$$
is ample for all rational $r \in\left(0, \frac{d m}{4 \pi}\right)$. In particular, if $m>6$ or $d>4 \pi$, then $K_{V}$ is ample.
Corollary F. With the same $X$ as Theorem A, all subvarieties of X are of general type provided that the uniform depth of cusps is greater than $4 \pi$.

As explained after Theorem A, Brunebarbe and Cadorel proved the bigness of $\Omega \frac{1}{X^{\prime}}$, with the assumption that $X^{\prime}$ is a highly ramified cover of $X$. Then, they applied the difficult theorem of Campana-Păun's [CP15] to conclude that all subvarieties of $X^{\prime}$ are of general type. Beside the fact that Corollary F tells us strong hyperbolicity of $X$ itself, rather than cover of $X$, our approach has another advantage that it bypass the theorem of Campana-Păun to prove all subvarities of $X$ are of general type because of nice restriction properties of ampleness.

Bakker and Tsimerman [BT18b] proved that $K_{\bar{X}}(D)-r D$ is ample for $r \in(0,(n+1) / 2)$, where $n=\operatorname{dim} X$ and concluded that if $n \geq 6, K_{\bar{X}}$ is ample. Similarly, Cadorel [Cad21a] showed that $V \subset \bar{X}$ with $\operatorname{dim} V \geq 6$ is of general type if $V \not \subset D$.

In general, for a smooth variety with dimension greater than 1 , the log-cotangent bundle is never ample as its restriction to the boundary is an extension of the trivial bundle.([ADT22], [BD18]). For a toroidal compactification of a locally symmetric domain, Brunebarbe [Bru18] proved that $\Omega_{\bar{X}}^{1}(\log (D))$ is big. In the case of ball quotients, Theorem A demonstrates that $\Omega_{\bar{X}}^{1}(\log (D))$ is a limit of ample $\mathbb{Q}$-vector bundles. Moreover, we can deduce from Theorem A the following Corollary:
Corollary G. With $X$ and $\bar{X}$ as in Theorem $A, \Omega \frac{1}{X}(\log (D))$ is ample modulo $D$ and nef.
In particular, Corollary G implies that $\Omega_{\bar{X}}^{1}(\log (D))$ is big and nef, which Cadorel also recently proved ([Cad21b]). He used the positivity of the Bergman metric on the open part together with a result of [Bou02] to show that the volume of the line bundle $O(1)$ over $\mathbb{P}\left(\Omega \frac{1}{X}\right)$ must be positive which implies that $O(1)$ is big. Similarly, he proved that $O(1)$ over $\mathbb{P}\left(\Omega \frac{1}{\bar{X}}\right)$ is nef by showing that the volume of the pull back of $O(1)$ over $\mathbb{P}\left(\Omega \frac{1}{X}\right)$ to every subvariety of $\bar{X}$ not contained in $D$ is positive.

The volume of a line bundle $L$ on a projective variety $V$ of dimension $m$ is defined to the non-negative real number
$$\operatorname{vol}_{V}(L):=\limsup _{k \rightarrow \infty} \frac{h^{0}\left(V, L^{\otimes k}\right)}{k^{m} / m!}$$
which measures the asymptotic growth rate of the pluri-canonical linear series $|k L|$.
Brunebarbe [Bru20a] used the volume of the canonical bundle of a variety to measure its hyperbolicity. In the setting of Shimura varieties (actually in more general setting, see [Bru20a, Theorem 1.1.]), he proved that the minimum volume of subvarieties of $Y(p), Y$ with full level structure, tends to infinity. As a generalization of Brunebarbe's work [Bru20a], for cofinal towers of normal coverings of ball quotients we prove the following Corollary:

Corollary H. Let $X$ be a complex hyperbolic manifold with cusps and $\left\{X_{i}\right\}_{i=1}^{\infty}$ be a cofinal tower of normal coverings of $X=X_{1}$. Then, given a positive number $v$, for all but finitely many $i$, every subvariety $V$ of $X_{i}$ containing a cusp of $X_{i}$ have $\operatorname{vol}\left(K_{V}\right)>v$.

Indeed, we show that the volume of the canonical bundle (and the log-canonical bundle) of subvarieties of $X$ containing a cusp of $X$, is controlled by the uniform depth of cusps (see Corollary 7.3 and Corollary 7.5).

Using results of $L^{2}$-estimates for a Kähler manifold, Wong [Won18] proved that there exist a constant $r(n)$ and $d(n)$ depending only on the dimension of $X$, such that if the injectivity radius is larger than $r(n)$ and the uniform depth of cusps is larger than $d(n)$, then $\Omega_{\bar{X}}^{1}$ is ample modulo $D$. His method relies on the existence theorem of $L^{2}$-estimation ([AV65, H6̈5]).

Theorem A and Theorem B substantially improve the previous results of Cadorel and Wong for the positivity of $\Omega \frac{1}{\bar{X}}(\log (D))$ and $\Omega \frac{1}{\bar{X}}$, and our proofs are independent from their proofs.

Our method to prove Theorem A is to construct a singular hermitian metric on $L:=O(1)$ over $\mathbb{P}\left(\Omega_{\bar{X}}^{1}(\log (D))\right)$ with the Bergman metric $h$ induced on $L$ and a carefully chosen weight function. To obtain the positivity of the twisted bundle, there has to be a trade-off between the positivity of $h$ and the weight function. This trade-off comes from the inequality we proved between $c_{1}\left(L_{\left.\right|^{-1}(X)}, h\right)$ and a positive (1,1)-form (see proofs of Proposition 5.5 and Theorem 5.6). The strength of our method is that it gives a criteria for the positivity of $\Omega \frac{1}{X}$ explicitly and intrinsically depending on $X$. This criteria can be checked for a given $X$.

We prove the semi-ampleness of $\Omega \frac{1}{X}$ in Theorem B by a hybrid technique using both the results coming from the differential geometry of the toroidal compactification-namely, the positivity of the twisted cotangent bundle-and the results coming from the algebraic geometry of the toroidal compactification. (see proof of Proposition 5.2 and Theorem 6.2 for more details).

\section*{Outline of the paper}

In §2, we describe the toroidal compactification of the ball quotients and necessary background on the Siegel domain. In §3, we study the properties of the Bergman metric induced on $O_{\mathbb{P}\left(\Omega \frac{1}{X}(\log (D))\right.}(1)$. In §4, we prove some basic lemmas about $\mathbb{Q}$-vector bundles. In §5, we prove the results related to the positively of $\Omega_{\bar{X}}^{1}(\log (D))$ including Theorem A and Corollary G. In §5, we prove the results related to the positivity of $\Omega \frac{1}{X}$, namely Theorem B and Theorem D. Finally, in §5, we deduce the applications to hyperbolicity of subvarieties in Corollary E, Corollary F and Corollary H.

\section*{Acknowledgements}

I would like to thank my advisor Jacob Tsimerman for introducing me to this problem, and for his constant support, as well as many insightful discussions. Also, I would like to thank Steven Lu and Luca Di Cerbo for their comments on an earlier draft of this paper.

\section*{2. Background}
2.1. Complex Unit Ball. The complex unit ball
$$\mathbb{B}^{n}=\left\{\left.z \in \mathbb{C}^{n}| | z\right|^{2}<1\right\}$$
has holomorphic automorphism group $G:=\operatorname{PU}(n, 1)$. Let $\Gamma \subset G$ be a cofinite-volume discrete group which does not have any elliptic element. Therefore, $X:=\mathbb{B}^{n} / \Gamma$ is a complex manifold with cusps, where cusps correspond to conjugacy class of maximal parabolic subgroups of $\Gamma$.

The Baily-Borel compactification [BB66, SY16] of $X$ is obtained by adding a finite set of points in corresponding to the equivalences classes of the rational boundary components of $\mathbb{B}^{n}$ under the action of $\Gamma$. This compactification is a normal projective variety and we will refer to the the points added to $X$ as cusps of $X$.

The Bergman metric on $\mathbb{B}^{n}$ is the $\operatorname{PU}(n, 1)$-invariant hermitian metric with holomorphic sectional curvature of -1 given by
$$h=4 . \frac{\left(1-|z|^{2}\right) \cdot \sum_{i} d z_{i} \otimes d \bar{z}_{i}+\sum_{i} \bar{z}_{i} d z_{i} \otimes \sum_{i} z_{i} d \bar{z}_{i}}{\left(1-|z|^{2}\right)^{2}} .$$
2.2. Siegel Domain. To understand the behaviour of Bergman metric around cusps, we found it more convenient to pass to the Siegel model $\mathbb{S}$ which is diffeomorphic to $\mathbb{B}^{n}$ and described by the holomorphic coordinates $(\zeta, z)$ of $\mathbb{C}^{n-1} \times \mathbb{C}$ in the following way:
$$\mathbb{S}:=\left\{(\zeta, z) \in \mathbb{C}^{n-1} \times \mathbb{C}\left|\operatorname{Im}(z)>|\zeta|^{2}\right\} .\right.$$

Let $u:=\operatorname{Im}(z)-|\zeta|^{2}$ be the height coordinate on $\mathbb{S}$. The Kähler form of the Bergman metric on $\mathbb{S}$ is given by
$$w_{\mathbb{S}}:=-2 i \partial \bar{\partial} \log (u)$$
(see, for example, [BT18b, Lemma 2.1]), and more explicitly we can write $\omega_{\mathbb{S}}$ in terms of $(\zeta, z)$-coordinates
$$\begin{aligned}
w_{\mathbb{S}}= & 2 i u^{-2} \cdot \sum_{i=1}^{n-1} \sum_{k=1}^{n-1}\left(u \delta_{i k}+\zeta_{i} \bar{\zeta}_{k}\right) d \zeta_{k} \wedge d \bar{\zeta}_{i} \\
& +u^{-2} \cdot \sum_{j=1}^{n-1}\left(\bar{\zeta}_{j} d \zeta_{j} \wedge d \bar{z}-\zeta_{j} d z \wedge d \bar{\zeta}_{j}\right) \\
& -\frac{i}{2} u^{-2} d z \wedge d \bar{z}
\end{aligned}$$
where $\delta_{i k}$ is the Kronecker delta function. Using holomorphic coordinates $\zeta$ and $z$ on $\mathbb{S}$, we can set a holomorphic coordinates $(\zeta, z, \xi, w)$ on $\Omega_{\mathbb{S}}^{1}$, where $\xi=\left(\frac{\partial}{\partial \zeta_{1}}, \frac{\partial}{\partial \zeta_{2}}, \ldots, \frac{\partial}{\partial \zeta_{n-1}}\right)$ and $w=\frac{\partial}{\partial z}$. Using the frame $e_{i}=\xi_{i}$ for $1 \leq i \leq n-1$ and $e_{n}=w$, the hermitian matrix of the Bergman metric is
$$\left[h\left(e_{i}, \bar{e}_{j}\right)\right]=2\left[\begin{array}{ccccc}
u^{-1}+u^{-2}\left|\zeta_{1}\right|^{2} & u^{-2} \zeta_{1} \bar{\zeta}_{2} & \ldots & u^{-2} \zeta_{1} \bar{\zeta}_{n-1} & \frac{1}{2 i} u^{-2} \zeta_{1} \\
u^{-2} \zeta_{2} \bar{\zeta}_{1} & u^{-1}+u^{-2}\left|\zeta_{2}\right|^{2} & \ldots & u^{-2} \zeta_{2} \bar{\zeta}_{n-1} & \frac{1}{2 i} u^{-2} \zeta_{2} \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
u^{-2} \zeta_{n-1} \bar{\zeta}_{1} & u^{-2} \zeta_{n-1} \bar{\zeta}_{2} & \ldots & u^{-1}+u^{-2}\left|\zeta_{n-1}\right|^{2} & \frac{1}{2 i} u^{-2} \zeta_{n-1} \\
-\frac{1}{2 i} u^{-2} \bar{\zeta}_{1} & -\frac{1}{2 i} u^{-2} \bar{\zeta}_{2} & \ldots & -\frac{1}{2 i} u^{-2} \bar{\zeta}_{n-1} & \frac{1}{4} u^{-2}
\end{array}\right] .$$

Siegel model has a preferred cusp at infinity whose parabolic stabilizer group $G_{\infty}$ is generated by Heisenberg isometries $\mathrm{I}_{\infty}$ and a one-dimensional torus $T$. Heisenberg isometries consists of Heisenberg Rotations $\mathrm{U}(n-1)$ and Heisenberg translations $\mathfrak{N}$. The group of Heisenberg Rotations identifies with $\mathrm{U}(n-1)$ acting on $\zeta$-coordinates of $\mathbb{S}$ in the usual way and The group of Heisenberg translations $\mathfrak{N} \cong \mathbb{C}^{n-1} \times \mathbb{R}$ acts on $\mathbb{S}$ via
$$(\tau, t):(\zeta, z) \longrightarrow\left(\zeta^{\prime}, z^{\prime}\right):=\left(\zeta+\tau, z+t+i|\tau|^{2}+2 i(\tau, \zeta)\right) .$$
In particular, the elements $(0, t) \in \mathfrak{N}$ will be referred to as a vertical translation by $t$, and the subgroup generated by $(0, t)$ in $G_{\infty}$ will be denoted by $\mathrm{V}_{\infty}$. We use $(A, \tau, t) \in \mathrm{U}(n-1) \ltimes \mathfrak{N}$ to denote the transformation acting by
$$(A, \tau, t) \cdot(\zeta, z) \longrightarrow\left(A \zeta+\tau, z+t+i|\tau|^{2}+2 i(A \zeta, \tau)\right),$$
where the standard positive definite hermitian form $(.,$.$) chosen on \mathbb{C}^{n-1}$. Using the chain rule we can observe that the action of ( $A, \tau, t$ ) induced on the cotangent bundle $\Omega_{\mathbb{S}}^{1}$ is
$$(A, \tau, t) .(\zeta, z, \xi, w)=\left(A \zeta+\tau, z+t+i|\tau|^{2}+2 i(A \zeta, \tau), A \xi+2 i(A \xi, \tau), w\right) .$$
The vertical translation $\mathrm{V}_{\infty}$ is the center of $G_{\infty}$ and the quotient $\mathrm{V}_{\infty} \backslash \mathrm{I}_{\infty}$ is isomorphic to the unitary transformation of $\mathbb{C}^{n-1}$. The remaining generators of $G_{\infty}$ is the one-dimensional torus $T$ which acts by scaling
$$(\zeta, z) \rightarrow\left(a \zeta, a^{2} z\right) .$$
2.3. Depth of cusps. For $u_{i}>0$, the horoball centered at the cusp at infinity with height $u_{i}$ is the open set
$$B\left(u_{i}\right):=\left\{(\zeta, z) \in \mathbb{S} \mid u>u_{i}\right\} .$$
Note that the height coordinate $u$ on $\mathbb{S}$ is invariant under the action of Heisenberg rotations $\mathrm{U}(n-1)$ and Heisenberg translations $\mathfrak{N}$ because $\mathrm{U}(n-1)$ fixes $|\zeta|$ and $z$, and
$$\operatorname{Im}\left(z^{\prime}\right)-\left|\zeta^{\prime}\right|^{2}=\operatorname{Im}(z)-|\zeta|^{2} .$$
It follows that the horoball is invariant with respect to the action of Heisenberg rotations and Heisenberg translations and the one-dimensional torus $T$ scales $B(u)$ to $B(a u)$.

Definition 2.1. For a cusp $c_{i}$, there exists a $g \in G$ translating $c_{i}$ to $\infty$. Let $\Gamma_{i}^{\prime}:=\left(g \cdot \Gamma \cdot g^{-1}\right)_{\infty}$ be the parabolic stabilizer of $\infty$. The smallest $u_{i}$ such that $\Gamma_{i}^{\prime} \backslash B\left(u_{i}\right)$ injects into $X$ will be called the height of the $c_{i}$. We will refer to $H_{i}(u)=\Gamma_{i}^{\prime} \backslash B(u)$ for $u>u_{i}$ as a horoball neighborhood of $c_{i}$.

Thanks to the Shimuzu's lemma, $H_{i}\left(u_{i}\right)$ must injects into $X$ for a large enough $u_{i}$.
Definition 2.2. Suppose $u_{i}$ is the height of cups $c_{i}$, and $t_{i}$ is the shortest vertical translation in the parabolic stabilizer of $c_{i}$. The number $d_{i}=t_{i} / u_{i}$ is called the depth of $c_{i}$ which is invariant under conjugating the lattice $\Gamma$.

Definition 2.3. ([BT18b, Definition 3.7.]) The uniform depth of cusps of $X$ is the largest $d$ satisfying the following properties, setting $v_{i}=t_{i} / d$ :
\begin{itemize}
\item[(1)] for every $i, v_{i} \leq u_{i}$ (this gives that $H_{i}\left(v_{i}\right)$ injects into $X$ ).
\item[(2)] all $H_{i}\left(v_{i}\right)$ are disjoint.
\end{itemize}

Thanks to Parker's generalization of Shimizu's lemma [Par98, Proposition 2.4.], the uniform depth of cups is at least 2 for torsion free.

Remark 2.4. By passing to a cover of $X$, i.e., passing to a subgroup of $\Gamma$, the shortest vertical translations of parabolic subgroups can not decrease and the heights can not increase. Therefore, the canonical depth can not decrease by passing to a cover of $X$.

Definition 2.5. (see [Yeu94, Section 2]) A cofinal normal tower of $X$ is a sequence $\left\{X_{i}\right\}_{i=1}^{\infty}$ of étale Galois coverings of $X=X_{1}$ given by a sequence of lattices $\left\{\Gamma_{i}\right\}_{i=1}^{\infty}$ such that for each subsequence $\left\{\Gamma_{j}\right\}_{j=1}^{\infty}$, one has $\bigcap_{j=1}^{\infty} \Gamma_{j}=\{1\}$.

Similar to [Yeu94, Lemma 1.2.2.] and [HT06, Proposition 2.1.], we can prove that the uniform depth of cusps tends to infinity in cofinal normal towers:

Lemma 2.6. Let $\left\{X_{i}\right\}_{i=1}^{\infty}$ be a cofinal normal tower of $X$ and $d\left(X_{i}\right)$ be the uniform depth of cusps of $X_{i}$. Then,
$$\lim _{i \rightarrow \infty} d\left(X_{i}\right)=\infty .$$
Proof. Let $p_{i}: X_{i} \rightarrow X$ be the covering map. Fix a cusp $c_{1}$ of $X$. Since $X_{i}$ is a normal cover of $X$, the group $\Gamma$ acts transitively on all cusps of $X_{i}$ that get sent to $c_{1}$, and therefore the uniform depth can be computed by taking only one cusp over each cusp of $X$. Let $c_{i}$ be a cusp of $X_{i}$ such that $p_{i}\left(c_{i}\right)=c_{1}$. Let $u\left(c_{i}\right)$ be the height of cusp $c_{i}$, and $t\left(c_{i}\right)$ be the shortest vertical translation in the stabilizer of $c_{i}$. Since $u\left(c_{i}\right) \leq u\left(c_{1}\right)$, it is sufficient to show that $t\left(c_{i}\right)$ tends to infinity. Note that as $\Gamma$ is discrete, for every $t_{i}$ there only exists finitely many elements in $\Gamma$ with the length smaller than or equal to $t_{i}$. On the other hand, for any subsequence $\left\{\Gamma_{j}\right\}_{j=1}^{\infty}$, we have $\bigcap_{j=1}^{\infty} \Gamma_{j}=\{1\}$. Putting these together, we conclude that the length of the shortest element except 1 in $\Gamma_{i}$ tends to infinity. \(\square\)

Remark 2.7. In general, the uniform depth of cusps tends to infinity in most of the towers of covering, even in the case that ramification index of some cusps are fixed in the tower. More precisely, for towers that the traces of hyperbolic elements tends to infinity, the uniform depth tends to infinity. This is proved in [Mem23, section 3], and here we examine the special case of modular curves $X_{0}(p)$, where $p$ is a prime number or 1. Consider the lattice
$$\Gamma_{0}(p)=\left\{\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right) \in \operatorname{PSL}_{2}(\mathbb{Z}) \left\lvert\,\left(\begin{array}{ll}
a & b \\
c & d
\end{array}\right) \cong\left(\begin{array}{ll}
* & * \\
0 & *
\end{array}\right) \bmod p\right.\right\} .$$

The group $\operatorname{PSL}_{2}(\mathbb{R})$ acts on $\mathbb{H}$ with the linear fractional translation and the action naturally extends to $\mathbb{H}^{*}=\mathbb{H} \cup \mathbb{Q} \cup\{\infty\}$. Let
$$X_{0}(p):=\Gamma_{0}(p) \backslash \mathbb{H}^{*},$$
and consider the covering $X_{0}(p) \rightarrow X_{0}(1)$. It is well-know that for prime $p$, the curve $X_{0}(p)$ has only two inequivalent cusps, see [Shi71, pg 26], and 0 and $\infty$ represent these two inequivalent cusps of $X_{0}(p)$. We will denote the stabilizer of 0 and $\infty$ in $\Gamma_{0}(p)$ by $\operatorname{stab}_{\Gamma_{0}(p)}(0)$ and $\operatorname{stab}_{\Gamma_{0}(p)}(\infty)$ :
$$\operatorname{stab}_{\Gamma_{0}(p)}(0)=\left\{\left.\left(\begin{array}{cc}
1 & 0 \\
p k & 1
\end{array}\right) \right\rvert\, k \in \mathbb{Z}\right\}, \operatorname{stab}_{\Gamma_{0}(p)}(\infty)=\left\{\left.\left(\begin{array}{cc}
1 & b \\
0 & 1
\end{array}\right) \right\rvert\, b \in \mathbb{Z}\right\} .$$

Therefore, the ramification indices of 0 and $\infty$ over $X_{0}(1)$ are $p=\left[\operatorname{stab}_{\Gamma_{0}(p)}(0): \operatorname{stab}_{\Gamma_{0}(1)}(0)\right]$ and $1=\left[\operatorname{stab}_{\Gamma_{0}(p)}(\infty): \operatorname{stab}_{\Gamma_{0}(1)}(\infty)\right]$, respectively.

Consider $g=\left(\begin{array}{cc}a & b \\ c & d\end{array}\right) \in \Gamma_{0}(p)$ which is not in $\operatorname{stab}_{\Gamma_{0}(p)}(\infty)$. It is straightforward to check that for every $z \in \mathbb{H}$, we have $\operatorname{Im}(g(z)) \cdot \operatorname{Im}(z) \leq \frac{1}{|c|^{2}}$. Since $|c| \geq p$, this implies that the horoball $\operatorname{stab}_{\Gamma_{0}(p)}(\infty) \backslash\left\{\operatorname{Im}(z)>\frac{1}{p}\right\}$ injects to $\Gamma_{0}(p) \backslash \mathbb{H}^{1}$ and therefore the height of $\infty$ is at most $\frac{1}{p}$. Since the length of shortest vertical translation around $\infty$ is 1 , we get that the depth of $\infty$ is at least $p$. To find the depth of 0 , consider the element $h=\left(\begin{array}{cc}0 & 1 \\ -1 & 0\end{array}\right) \in \operatorname{PSL}_{2}(\mathbb{Z})$ which sends 0 to $\infty$. Let $\operatorname{stab}_{\Gamma_{0}(p)}^{\prime}(0)$ and $\Gamma_{0}^{\prime}(p)$ be the conjugation of $\operatorname{stab}_{\Gamma_{0}(p)}(0)$ and $\Gamma_{0}(p)$ by $h$, respectively. Then, we have
$$\begin{gathered}
\Gamma_{0}^{\prime}(p)=\left\{\left(\begin{array}{cc}
a^{\prime} & b^{\prime} \\
c^{\prime} & d^{\prime}
\end{array}\right) \in \operatorname{PSL}_{2}(\mathbb{Z}) \left\lvert\,\left(\begin{array}{cc}
a^{\prime} & b^{\prime} \\
c^{\prime} & d^{\prime}
\end{array}\right) \cong\left(\begin{array}{cc}
* & 0 \\
* & *
\end{array}\right) \bmod p\right.\right\}, \\
\operatorname{stab}_{\Gamma_{0}(p)}^{\prime}(0)=\left\{\left.\left(\begin{array}{cc}
1 & p k \\
0 & 1
\end{array}\right) \right\rvert\, k \in \mathbb{Z}\right\} .
\end{gathered}$$
Similarly, for every $g^{\prime}=\left(\begin{array}{cc}a^{\prime} & b^{\prime} \\ c^{\prime} & d^{\prime}\end{array}\right) \in \Gamma_{0}^{\prime}(p)$ which is not in $\operatorname{stab}_{\Gamma_{0}(p)}^{\prime}(0)$, and every $z \in \mathbb{H}$, we have that $\operatorname{Im}\left(g^{\prime}(z)\right) \cdot \operatorname{Im}(z) \leq \frac{1}{\left|c^{\prime}\right|^{2}}$. Therefore, the horoball $\operatorname{stab}_{\Gamma_{0}(p)}^{\prime}(\infty) \backslash\{\operatorname{Im}(z)>1\}$ injects to $\Gamma_{0}^{\prime}(p) \backslash \mathbb{H}^{1}$. This implies that the height of 0 is at most 1 and because the length of shortest vertical translation is $p$, we get that the depth of 0 is at least $p$. Since the set $\left\{\operatorname{Im}(z)>\frac{p}{d}\right\}$ is disjoint from the set $\left\{\operatorname{Im}(z)<\frac{p}{d}\right\}$, for every $d \leq \sqrt{p}$, we can conclude that the uniform depth of cusps of $X_{0}(p)$ is $\sqrt{p}$.
2.4. Toroidal Compactification. The variety $X$ has a unique toroidal compactification in the sense of [AMRT10, Mok12]. This torodial compactification is a smooth projective variety and each connected component of the boundary divisor $D$ is an étale quotient of an abelian variety whose conormal bundle is ample. Moreover, if $\Gamma$ has only unipotent parabolic subgroups(in particular when $\Gamma$ is neat), then $D$ is disjoint union of abelian varieties with ample conormal bundle. Note that $\Gamma$ always has a finite-index neat subgroup by [AMRT10] in the arithmetic case and by [Hum98] in general.

We describe the toroidal compactification $\bar{X}$ of $X$ locally around the cusp at $\infty$. Consider the holomorphic map
$$\begin{aligned}
\mathbb{S} & \longrightarrow \mathbb{C}^{n-1} \times \Delta^{*} \\
(\zeta, z) & \longrightarrow\left(\zeta, e^{2 \pi i z / t_{\infty}}\right),
\end{aligned}$$
which is surjective and invariant under the action of $W_{\infty}:=V_{\infty} \cap \Gamma$. This map identifies the partial quotient $W_{\infty} \backslash \mathbb{S}$ by its image. Since $\Lambda_{\infty}=W_{\infty} \backslash \Gamma_{\infty}$ is identified to a discrete unitary transformation of $\mathbb{C}^{n-1}$, the boundary divisor in the compactification of $\Gamma_{\infty} \backslash \mathbb{S}$ is given by $\Lambda_{\infty} \backslash \mathbb{C}^{n-1} \times 0$. Note that not having an orbifold point on the compactification is equivalent to not having a torsion element in $\Lambda_{\infty}$.

Therefore, assuming that $\bar{X}$ does not have an orbifold point gives that the residual quotient of $\mathbb{C}^{n-1} \times \Delta$ by $\Lambda_{\infty}$ is locally étale quotient and the coordinates $\zeta, q=e^{2 \pi i z / t_{\infty}}$ extends to coordinates of $\bar{X}$ around the boundary such that the boundary divisor in this neighborhood is cut out by $q=0$. We will denote the connected component of $D$ by $D_{i}$ which is an étale quotient of an abelian variety with ample conormal bundle([Mok12]). In the case that the
parabolic subgroups of $\Gamma$ are unipotent (e.g. $\Gamma$ is neat), the boundary is a disjoint union of abelian varieties.

\section*{3. Positivity of $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1)$}

Let $E$ be a vector bundle of rank $n$ on an algebraic variety or complex manifold $Y$ and let
$$\pi: \mathbb{P}(E) \rightarrow Y$$
be the projective bundle of lines in the dual bundle $E^{*}$. The projective bundle $\mathbb{P}(E)$ carries a tautological quotient bundle line bundle $O_{\mathbb{P}(\mathbb{E})}(1)$ whose dual $O_{\mathbb{P}(\mathbb{E})}(-1)$ is naturally a subbundle of $\pi^{*} E$ :
$$0 \longrightarrow O_{\mathbb{P}(E)}(-1) \longrightarrow \pi^{*} E .$$
In other words, a point $(y,[L])$ of $\mathbb{P}(E)$ is determined by a point $y \in Y$ together with $[L]$ in $\mathbb{P}^{n}=\mathbb{P}\left(E^{*}(y)\right)$. The fiber $O_{\mathbb{P}(E)}(-1)_{(y,[L])}$ is the subvector space $L$ and the fiber $O_{\mathbb{P}(E)}(1)_{(y,[L])}$ is the one dimensional quotient of $E$ corresponding to $L$. A vector bundle $E$ is called ample if $O_{\mathbb{P}(E)}(1)$ is ample.

Let $X=\Gamma \backslash \mathbb{B}^{n}$ be a complex ball quotient by a torsion-free lattice $\Gamma \subset \operatorname{Aut}\left(\mathbb{B}^{n}\right)$ and $\hat{h}$ be the hermitian metric induced by the Bergman metric $h$ on $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1)$.

In this section, we prove two properties of $\hat{h}$ in Proposition 3.2 and Proposition 3.4. These properties will be used to construct a singular hermitian metric on the line bundle $O(1)$ over $\mathbb{P}\left(\Omega_{\bar{X}}^{1}(\log (D))\right)$ to prove Theorem A.

Let $\hat{h}^{*}$ be the dual metric of $\hat{h}$ on $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(-1)$. Suppose $U$ is an open subset of $\mathbb{P}\left(\Omega_{X}^{1}\right)$ such that for every $x \in U, \xi_{1, x} \neq 0$. After replacing $\xi_{i}$ by $\frac{\xi_{i}}{\xi_{1}}$ and $w$ by $\frac{w}{\xi_{i}}$, we can take a local section $\sigma=\sum_{i=1}^{n-1} \xi_{i} e_{i}+w e_{n}$ of $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(-1)$ on $U$. The first Chern form of $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(-1)$ on $U$ is represented by
$$\begin{aligned}
c_{1}\left(O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(-1), \hat{h}^{*}\right) & =\frac{i}{2 \pi} \bar{\partial} \partial \log \|\sigma\|_{\hat{h}^{*}}^{2} \\
& =\frac{i}{2 \pi} \bar{\partial} \partial \log \left(\sum_{i=1}^{n} \sum_{j=1}^{n} \xi_{i} \bar{\xi}_{j} h\left(e_{i}, e_{j}\right)\right) \\
& =\frac{i}{2 \pi}(-2 \bar{\partial} \partial \log u+\bar{\partial} \partial \log v),
\end{aligned}$$
where
$$v=\sum_{i=1}^{n-1} \sum_{j=1}^{n-1}\left(\left(u \delta_{i j}+\bar{\zeta}_{i} \zeta_{j}\right) \xi_{i} \bar{\xi}_{j}+\frac{1}{2 i} \xi_{j} \bar{\xi}_{n} \bar{\zeta}_{j}-\frac{1}{2 i} \bar{\xi}_{j} \xi_{n} \zeta_{j}\right)+\frac{1}{4}\left|\xi_{n}\right|^{2}$$
As $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(-1)$ is the dual of $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1)$, the first Chern form $c_{1}\left(O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1), \hat{h}\right)$ on $U$ is given by
$$c_{1}\left(O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1), \hat{h}\right)=\frac{i}{2 \pi_{9}}(2 \bar{\partial} \partial \log u-i \bar{\partial} \partial \log v)$$

Lemma 3.1. For every $q \in \Omega_{X}^{1}$ there exists a point $p$ in the orbit $I_{\infty} \cdot q$ such that in $(\zeta, z, \xi, w)$-coordinates $p$ is given by
$$\zeta_{i, p}=\xi_{i, p}=0,$$
for $1 \leq i \leq n-2, \zeta_{n-1, p}=0$ and $\xi_{n-1, p}$ being a positive real number.
Proof. Consider the action of $(A, \tau, t) \in \mathrm{U}(n-1) \times \mathbb{C}^{n-1} \times \mathbb{R}$ described in 3 and take $(A, \tau, t)=\left(I,-\zeta_{q}, 0\right)$ :
$$(I,-\zeta, 0) \cdot\left(\zeta_{q}, z_{q}, \xi_{q}, w_{q}\right)=\left(0, z^{\prime}, \xi_{q}+i\left|\zeta_{q}\right|^{2}+2 i\left(\xi_{q},-\zeta_{q}\right), w_{q}\right)$$

There exist $B \in \mathrm{U}(n-1)$ such that
$$B(\xi+2 i(\xi,-\zeta))=\left(0, \ldots, 0,\left|\xi_{q}+2 i\left(\xi_{q},-\zeta_{q}\right)\right|\right) .$$
The element $(B, 0,0) \in U(n-1) \times \mathbb{C}^{n-1} \times \mathbb{R}$ sends $\left(0, z^{\prime}, \xi_{q}+i\left|\zeta_{q}\right|^{2}+2 i\left(\xi_{q},-\zeta_{q}\right), w_{q}\right)$ to a point $p$ with the desired properties. \(\square\)

Proposition 3.2. Let $X=\Gamma \backslash \mathbb{B}^{n}$ be a torsion-free ball quotient and $\hat{h}$ be the hermitian metric on $O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1)$ induced by the Bergman metric on $\mathbb{B}^{n}$. Then,
\begin{itemize}
\item[(i)] the first Chern form $c_{1}\left(O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1), \hat{h}\right)$ is a Kähler form on $\mathbb{P}\left(\Omega_{X}^{1}\right)$;
\item[(ii)]
$$c_{1}\left(O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1), \hat{h}\right) \geq \frac{1}{4 \pi} \pi^{*}\left(w_{X}\right),$$
where $w_{X}$ is the Kähler form of the Bergman metric on $X$.
\end{itemize}

Proof. First we prove part (ii) and then conclude part(i) from the inequality appears in the proof of (ii).
\begin{itemize}
\item[(ii)] Since the Bergman metric and $u$ is $I_{\infty}$-invariant, its enough to check the inequality on $I_{\infty}$-orbit. Consider an open set $U \subset \mathbb{P}\left(\Omega_{X}^{1}\right)$ such that $w \neq 0$. Replacing $\xi_{i}$ by $\frac{\xi_{i}}{w}$ and $w$ by 1, we can work on the affine coordinates on $\mathbb{P}\left(\Omega_{X}^{1}\right)_{\mid U}$. Thanks to Lemma 3.1, we can move every point in $U$ by an element of $I_{\infty}$ to point $p$ such that
$$\begin{aligned}
& \zeta_{1, p}=\zeta_{2, p}=\ldots=\zeta_{n-1, p}=0, \\
& \xi_{1, p}=\xi_{2, p}=\ldots=\xi_{n-2, p}=0,
\end{aligned}$$
\end{itemize}
$w=1$ and $\xi_{n-1, p}$ is a real number. Note that the function $v$ in 4 on $U$ is
$$v=\left(\sum_{i=1}^{n-1} \sum_{j=1}^{n-1}\left(\left(u \delta_{i j}+\bar{\zeta}_{i} \zeta_{j}\right) \xi_{i} \bar{\xi}_{j}+\frac{1}{2 i} \xi_{j} \bar{\zeta}_{j}-\frac{1}{2 i} \bar{\xi}_{j} \zeta_{j}\right)+\frac{1}{4} .\right.$$
Set $L=O_{\mathbb{P}\left(\Omega_{X}^{1}\right)}(1)$. The first Chern form at $p$ is
$$c_{1}(L, \hat{h})(p)=\frac{i}{2 \pi} \bar{\partial} \partial \log (v)(p)=\frac{i}{2 \pi}(v(p))^{-2}(v(p) \cdot \bar{\partial} \partial v(p)-(\bar{\partial} v \wedge \partial v)(p)) .$$
To find explicit formula note that
$$\begin{aligned}
r & :=v(p)=u \xi_{n-1}^{2}+\frac{1}{4} \\
\partial v(p) & =u \xi_{n-1} d \xi_{n-1}+\frac{1}{2 i} \xi_{n-1}^{2} d z-\frac{1}{2 i} \xi_{n-1} d \zeta_{n-1},
\end{aligned}$$
and
$$\begin{aligned}
\bar{\partial} \partial v(p)= & \sum_{i=1}^{n-1}\left(-\xi_{n-1}^{2} d \bar{\zeta}_{i} \wedge d \zeta_{i}+u d \bar{\xi}_{i} \wedge d \xi_{i}+\frac{1}{2 i} d \bar{\zeta}_{i} \wedge d \xi_{i}-\frac{1}{2 i} d \bar{\xi}_{i} \wedge d \zeta_{i}\right) \\
& +\xi_{n-1}^{2} d \bar{\zeta}_{n-1} \wedge d \zeta_{n-1}-\frac{1}{2 i} \xi_{n-1} d \bar{z} \wedge d \xi_{n-1}+\frac{1}{2 i} \xi_{n-1} d \bar{\xi}_{n-1} \wedge d z
\end{aligned}$$
giving that
$$\begin{aligned}
c_{1}(L, \hat{h})(p)=\frac{i}{2 \pi} r^{-2} \cdot( & \sum_{i=1}^{n-2}\left(r u d \bar{\xi}_{i} \wedge d \xi_{i}-r \xi_{n-1}^{2} d \bar{\zeta}_{i} \wedge d \zeta_{i}+\frac{1}{2 i} r d \bar{\zeta}_{i} \wedge d \xi_{i}-\frac{1}{2 i} r d \bar{\xi}_{i} \wedge d \zeta_{i}\right) \\
& +\frac{1}{4} \cdot\left(u d \bar{\xi}_{n-1} \wedge d \xi_{n-1}+\frac{1}{2 i} d \bar{\zeta}_{n-1} \wedge d \xi_{n-1}-\frac{1}{2 i} d \bar{\xi}_{n-1} \wedge d \zeta_{n-1}\right. \\
& -\frac{1}{2 i} \xi_{n-1} d \bar{z} \wedge d \xi_{n-1}+\frac{1}{2 i} \xi_{n-1} d \bar{\xi}_{n-1} \wedge d z-\xi_{n-1}^{4} d \bar{z} \wedge d z \\
& \left.\left.+\xi_{n-1}^{3} d \bar{z} \wedge d \zeta_{n-1}+\xi_{n-1}^{3} d \bar{\zeta}_{n-1} \wedge d z-\xi_{n-1}^{2} d \bar{\zeta}_{n-1} \wedge d \zeta_{n-1}\right)\right) .
\end{aligned}$$
Now, as $\omega_{X}=2 i \bar{\partial} \partial \log (u)$, using equation 5, we can write
$$c_{1}(L, \hat{h})(p)-\frac{1}{4 \pi} \pi^{*}\left(w_{X}\right)(p)=\frac{i}{2 \pi}(\bar{\partial} \partial \log (u)(p)-\bar{\partial} \partial \log (v)(p)),$$
and therefore denoting the form $c_{1}(L, \hat{h})-\frac{1}{4 \pi} \pi^{*}\left(w_{X}\right)$ by $\eta$, we obtain
$$\begin{aligned}
\eta(p)= & \frac{i}{2 \pi} \cdot \sum_{i=1}^{n-2}\left(u r^{-1} d \xi_{i} \wedge d \bar{\xi}_{i}+\left(u^{-1}-r^{-1} \xi_{n-1}^{2}\right) d \zeta_{i} \wedge d \bar{\zeta}_{i}+\frac{1}{2 i} r^{-1} d \xi_{i} \wedge d \bar{\zeta}_{i}-\frac{1}{2 i} r^{-1} d \zeta_{i} \wedge d \bar{\xi}_{i}\right) \\
+ & \frac{i}{8} r^{-2} u^{-2}\left(\left(8 u r^{2}-2 u^{2} \xi_{n-1}^{2}\right) d \zeta_{n-1} \wedge d \bar{\zeta}_{n-1}+2 u^{3} d \xi_{n-1} \wedge d \bar{\xi}_{n-1}-i u^{2} d \xi_{n-1} \wedge d \bar{\zeta}_{n-1}\right. \\
+ & i u^{2} d \zeta_{n-1} \wedge d \bar{\xi}_{n-1}+i u^{2} \xi_{n-1} d \xi_{n-1} \wedge d \bar{z}-i u^{2} \xi_{n-1} d z \wedge d \bar{\xi}_{n-1} \\
+ & \left.\left(2 r^{2}-2 u^{2} \xi_{n-1}^{4}\right) d z \wedge d \bar{z}+2 u^{2} \xi_{n-1}^{3} d \zeta_{n-1} \wedge d \bar{z}+2 u^{2} \xi_{n-1}^{3} d z \wedge d \bar{\zeta}_{n-1}\right)
\end{aligned}$$
To see that $\eta(p)$ is semi-positive, we choose the local frame $\beta$ for $L$ over $U$ as follows:
$$\beta_{2 i-1}=\frac{\partial}{\partial \xi_{i}}, \quad \beta_{2 i}=\frac{\partial}{\partial \zeta_{i}},$$
for $1 \leq i \leq n-1$ and $\beta_{2 n-1}=\frac{\partial}{\partial z}$. In this frame,
$$[\eta(p)]_{\beta}=\frac{i}{2 \pi}\left[\begin{array}{ccccc}
A_{1} & 0 & \ldots & 0 & 0 \\
0 & A_{2} & \ldots & 0 & 0 \\
\ldots & \ldots & \ldots & \ldots & \ldots \\
0 & 0 & \ldots & A_{n-1} & 0 \\
0 & 0 & \ldots & 0 & B
\end{array}\right],$$
where $A_{i}=r^{-1}\left[\begin{array}{cc}u & \frac{1}{2 i} \\ -\frac{1}{2 i} & \frac{1}{4 u}\end{array}\right]$ and $B=\frac{1}{8} r^{-2} u^{-2}\left[\begin{array}{ccc}2 u^{3} & i u^{2} & -i u^{2} \xi_{n-1} \\ -i u^{2} & 8 u r^{2}-2 u^{2} \xi_{n-1}^{2} & 2 u^{2} \xi^{3} \\ i u^{2} \xi_{n-1} & 2 u^{2} \xi^{3} & 2 r^{2}-2 u^{2} \xi_{n-1}^{4}\end{array}\right]$.

By computation we can see that $\operatorname{det}\left(A_{i}\right)=0, \operatorname{tr}\left(A_{i}\right)>0$ and determinate of all upper left sub-matrices of $B$ are semi-positive. Hence,
$$c_{1}(L, \hat{h}) \geq \frac{1}{4 \pi} w_{X} .$$
(i) Since $c_{1}(L, \hat{h})$ is a closed form, we only need to show that it is positive. As $\omega_{X}$ is zero only on the vertical directions and neither $A_{i} \mathrm{~s}$ nor $B$ is zero on the vertical directions, $c_{1}(L, \hat{h})$ is a positive (1,1)-form. \(\square\)

In fact, if $\Gamma \subset \operatorname{PU}(n, 1)$ is a cocompact lattice, Proposition 3.2 implies that $\Gamma \backslash \mathbb{B}^{n}$ has ample cotangent bundle. This is well-know and the difficulty is, when $\Gamma$ is not cocompact.

For the non-compact case, we will construct a hermitian metric on $O(1)$ over $\mathbb{P}\left(\Omega_{X}^{1}\right)$ which extends as singular hermitian metric to $O(1)$ over $\mathbb{P}\left(\Omega \frac{1}{X}(\log (D))\right)$.

To prove Theorem A, we will construct a singular hermitian metric whose curvature current is represented by a form. To this end, we prove the following Proposition which is inspired by [GK73, Lemma 6.18] and [Kol85, Proposition 5.16]:

Proposition 3.3. Suppose $\Phi(\zeta,|q|): \mathbb{C}^{n-1} \times \mathbb{C} \rightarrow(0, \infty]$ is a function satisfying the following conditions:
\begin{itemize}
\item[(i)] $\partial \log (\Phi(\zeta,|q|))$ and $\partial \bar{\partial} \log (\Phi(\zeta,|q|))$ are locally integrable on a neighborhood of the divisor $q=0$;
\item[(ii)] $\lim _{q \rightarrow 0} \frac{\log (\Phi(\zeta,|q|))}{\log |q|}=0$, when $|\zeta|$ is bounded.
\end{itemize}

Then, the current $[\partial \bar{\partial} \log (\Phi(\zeta,|q|))]$ is represented by the form $\partial \bar{\partial} \log (\Phi(\zeta,|q|))$.
Proof. Let $U$ be an open set where the divisor $D$ is given by $q=0$. For a compactly supported ( $n-1, n-1$ )-form $f$ on $U$,
$$\int_{X} \log (\Phi(\zeta,|q|)) \partial \bar{\partial} f=\lim _{\epsilon \rightarrow 0} \int_{X_{\epsilon}} \log (\Phi(\zeta,|q|)) \partial \bar{\partial} f$$
where $X_{\epsilon}=\{(\zeta, q) \in \mathbb{C}| | q \mid>\epsilon\}$. Applying Stokes' theorem to the closed form $d(\log \mid \Phi(\zeta,|q|) \partial f)$, we get:
$$\int_{X_{\epsilon}} \log (\Phi(\zeta,|q|)) \bar{\partial} \partial f=-\int_{X_{\epsilon}} \bar{\partial} \log (\Phi(\zeta,|q|)) \wedge \partial f+\int_{S_{\epsilon}} \log (\Phi(\zeta,|q|)) \partial f$$
where $S_{\epsilon}=\left\{(\zeta, q) \in \mathbb{C}^{n}| | q \mid=\epsilon\right\}$ is oriented with its normal in the direction of decreasing $|q|$. Since $S_{\epsilon}=C_{\epsilon} \times \mathbb{C}^{n-1}$ where $C_{\epsilon}$ is the circle $\{q \in \mathbb{C}||q|=\epsilon\}$, Fubini's theorem gives that
$$\begin{aligned}
\int_{S_{\epsilon}} \log (\Phi(\zeta,|q|)) \partial f & =\int_{\mathbb{C}^{n-1}}\left(\int_{C_{\epsilon}} \log (\Phi(\zeta,|q|) \widetilde{f}(\zeta, q) d q) d \zeta \wedge d \bar{\zeta}\right. \\
& =\int_{D}\left(\log (\Phi(\zeta, \epsilon)) \int_{C_{\epsilon}} \widetilde{f}(\zeta, q) d q\right) d \zeta \wedge d \bar{\zeta}
\end{aligned}$$
where $d \zeta \wedge d \bar{\zeta}=d \zeta_{1} \wedge d \bar{\zeta}_{1} \wedge \ldots d \zeta_{n-1} \wedge d \bar{\zeta}_{n-1}, \widetilde{f}(\zeta, q) d q \wedge d \zeta \wedge d \bar{\zeta}$ is $d q \wedge d \zeta \wedge d \bar{\zeta}$ part of $\partial f$ and $D$ is a compact set such that $D \times C_{\epsilon}$ contains the support of $\widetilde{f}(\zeta, q)$. Since
$\lim _{q \rightarrow 0} \frac{\log (\Phi(\zeta,|q|))}{\log |q|}=0$, there exists $\epsilon^{\prime}>0$ such that $|\log (\Phi(\zeta, \epsilon))|<\epsilon^{\prime}|\log (\epsilon)|$. Furthermore, as $\widetilde{f}(\zeta, q)$ is continuous and $C_{\epsilon}$ is compact, there exists a continuous function $M(\zeta)$ such that $\left|\int_{C_{\epsilon}} \widetilde{f}(\zeta, q) d q\right|<M(\zeta) \cdot \epsilon$. It follows by compactness of $D$ that
$$\left|\int_{D}\left(\log (\Phi(\zeta, \epsilon)) \int_{C_{\epsilon}} \widetilde{f}(\zeta, q) d q\right) d \zeta \wedge d \bar{\zeta}\right| \leq R \cdot \epsilon \log (\epsilon),$$
where $R$ is a constant. As such, 7 and 8 imply that $\lim _{\epsilon \rightarrow 0} \int_{S_{\epsilon}} \log (\Phi(\zeta,|q|)) \partial f=0$ and by 6 we obtain that
$$\int_{X} \log (\phi(\zeta,|q|)) \partial \bar{\partial} f=\int_{X} \bar{\partial} \log (\phi(\zeta,|q|)) \wedge \partial f .$$

On the other hand, applying Stokes' theorem to the closed form $d(f \wedge \bar{\partial} \log (\phi(\zeta,|q|)))$ yields that:
$$\int_{X_{\epsilon}} f \wedge \partial \bar{\partial} \log (\Phi(\zeta,|q|))=-\int_{X_{\epsilon}} \partial f \wedge \bar{\partial} \log (\Phi(\zeta,|q|))+\int_{S_{\epsilon}} f \wedge \bar{\partial} \log (\Phi(\zeta,|q|)) .$$

It will be shown that $\lim _{\epsilon \rightarrow 0} \int_{S_{\epsilon}} f \wedge \bar{\partial} \log (\Phi(\zeta,|q|))=0$. Note that
$$\int_{S_{\epsilon}} f \wedge \bar{\partial} \log (\Phi(\zeta,|q|))=\int_{r=\epsilon} f \wedge \frac{1}{\Phi(\zeta, r)} \cdot \frac{\partial \Phi(\zeta, r)}{\partial \bar{q}}+\int_{|q|=\epsilon} f \wedge \sum_{i=1}^{n-1} \frac{\partial \log (\Phi(\zeta,|q|))}{\partial \bar{\zeta}_{i}},$$
where $r=|q|$. Applying L'Hopital's rule to $\lim _{r \rightarrow 0} \frac{\log (\Phi(\zeta, r))}{\log (r)}=0$ yields
$$\lim _{r \rightarrow 0} \frac{r}{\Phi(\zeta, r)} \cdot \frac{\partial \Phi(\zeta, r)}{\partial r}=0 .$$

As $\frac{\partial r}{\partial \bar{q}}=\frac{1}{2}\left(\frac{q}{\bar{q}}\right)^{\frac{1}{2}}$ the chain rule gives
$$\frac{\partial \Phi(\zeta,|q|)}{\partial \bar{q}}=\frac{1}{2}\left(\frac{q}{\bar{q}}\right)^{\frac{1}{2}} \cdot \frac{\partial \Phi(\zeta, r)}{\partial r} .$$
Since $f$ is compactly supported, there exists a constant $M^{\prime}$ such that
$$\left|\int_{r=\epsilon} f \wedge \frac{1}{\Phi(\zeta, r)} \cdot \frac{\partial \Phi(\zeta,|q|)}{\partial \bar{q}}\right| \leq M^{\prime} \epsilon \cdot \max _{r=\epsilon}\left|\frac{1}{\Phi(\zeta, r)} \cdot \frac{\partial \Phi(\zeta, r)}{\partial r}\right|,$$
which tends to 0 as $\epsilon$ tends to 0 using 12. The other term in 11 can be written as
$$\begin{aligned}
\int_{|q|=\epsilon} f \wedge \sum_{i=1}^{n-1} \frac{\partial \log (\Phi(\zeta,|q|))}{\partial \bar{\zeta}_{i}} & =\int_{\mathbb{C}^{n}} \sum_{i=1}^{n-1} \frac{\partial \log (\Phi(\zeta, \epsilon))}{\partial \bar{\zeta}_{i}} \int_{|q|=\epsilon} f \\
& =\int_{\mathbb{C}^{n}} \log (\Phi(\zeta, \epsilon)) \bar{\partial}\left(\int_{|q|=\epsilon} f\right),
\end{aligned}$$
by Stokes' theorem. As $f$ is compactly supported there exists a constant $R^{\prime}$ such that
$$\left|\int_{\mathbb{C}^{n}} \log (\Phi(\zeta, \epsilon)) \bar{\partial}\left(\int_{|q|=\epsilon} f\right)\right| \leq R^{\prime} \epsilon^{\prime}|\log (\epsilon)| \epsilon$$
tending to 0 as $\epsilon$ tends to 0. Therefore, combining 11, 13, 14 and 15 gives $\lim _{\epsilon \rightarrow 0} \int_{S_{\epsilon}} f \wedge$ $\bar{\partial} \log (\Phi(\zeta,|q|))=0$ and by 10 we get
$$\int_{X} f \wedge \partial \bar{\partial} \log (\Phi(\zeta,|q|))=-\int_{X} \partial f \wedge \bar{\partial} \log (\Phi(\zeta,|q|)) .$$

The claim follows from 9 and 16. \(\square\)

Proposition 3.4. Let $s$ be a local section of $O_{\mathbb{P}\left(\Omega_{X}^{1}(\log D)\right)}(1)$. Then, the current $[\partial \bar{\partial} \log (\hat{h}(s))]$ is represented by the form $\partial \bar{\partial} \log (\hat{h}(s))$.

Proof. Let $D^{\prime}$ be the pull back of $D=\bar{X} \backslash X$ to $\Omega \frac{1}{\bar{X}}(\log D)$. Take an arbitrary point $a=$ $\left(\zeta_{1}, \ldots, \zeta_{n-1}, q=0 ;\left[\xi_{1}, \ldots, \xi_{n}\right]\right) \in D^{\prime}$. At least one of $\xi_{1}, \xi_{2}, \ldots, \xi_{n}$ is non-zero. Let $\xi_{k} \neq 0$, for some $k \in\{1,2, \ldots, n\}$. Suppose $U$ is an open subset of $\mathbb{P}\left(\Omega_{X}^{1}(\log D)\right)$ such that for every $u \in U, \xi_{k, u} \neq 0$ and $D^{\prime} \cap U=(q=0)$. Replacing $\xi_{i}$ by $\frac{\xi_{i}}{\xi_{k}}, \eta=\sum_{i=1}^{n-1} \xi_{i} \frac{\partial}{\partial \zeta_{i}}+\xi_{n} q \frac{\partial}{\partial q}$ is a local section of $O_{\mathbb{P}\left(\Omega_{X}^{1}(\log D)\right)}(-1)$ on $U$. Note that on $U$ we have $h(s)=\frac{1}{\|\eta\|_{\hat{h}^{*}}^{2}}$, and therefore it is enough to check the conditions of Proposition 3.3 for $\log \left(\|\eta\|_{\hat{h}^{*}}^{2}\right)$. We write this function in terms of the chosen coordinate. First, we have that
$$\begin{aligned}
\|\eta\|_{\hat{h}^{*}}^{2} & =u^{-2} \cdot\left(\sum_{i=1}^{n-1} \sum_{j=1}^{n-1}\left(\left(u \delta_{i j}+\bar{\zeta}_{i} \zeta_{j}\right) \xi_{i} \bar{\xi}_{j}+\frac{t_{\infty}}{4 \pi} \xi_{j} \bar{\xi}_{n} \bar{\zeta}_{j}+\frac{t_{\infty}}{4 \pi} \bar{\xi}_{j} \xi_{n} \zeta_{j}\right)+\frac{t_{\infty}^{2}}{16 \pi}\left|\xi_{n}\right|^{2}\right) \\
& =u^{-1} \cdot \sum_{i=1}^{n-1}\left|\xi_{i}\right|^{2}+u^{-2} \cdot\left(\sum_{i=1}^{n-1} \sum_{j=1}^{n-1}\left(\bar{\zeta}_{i} \zeta_{j} \xi_{i} \bar{\xi}_{j}+\frac{t_{\infty}}{4 \pi} \xi_{j} \bar{\xi}_{n} \bar{\zeta}_{j}+\frac{t_{\infty}}{4 \pi} \bar{\xi}_{j} \xi_{n} \zeta_{j}\right)+\frac{t_{\infty}^{2}}{16 \pi}\left|\xi_{n}\right|^{2}\right) .
\end{aligned}$$
Therefore,
$$\log \left(\|\eta\|_{\hat{h}^{*}}^{2}\right)=-2 \log (u)+\log \left(\sum_{i=1}^{n-1} \sum_{j=1}^{n-1}\left(\left(u \delta_{i j}+\bar{\zeta}_{i} \zeta_{j}\right) \xi_{i} \bar{\xi}_{j}+\frac{t_{\infty}}{4 \pi} \xi_{j} \bar{\xi}_{n} \bar{\zeta}_{j}+\frac{t_{\infty}}{4 \pi} \bar{\xi}_{j} \xi_{n} \zeta_{j}\right)+\frac{t_{\infty}^{2}}{16 \pi}\left|\xi_{n}\right|^{2}\right) .$$

To check that the 1 -form $\partial \log \left(\|\eta\|_{\hat{h}^{*}}^{2}\right)$ is locally integrable, we only need to check that the the function $\frac{1}{|q| \log |q|}$ is locally integrable around $q=0$. This follows from
$$\int_{|q|<\epsilon} \frac{d q \wedge d \bar{q}}{|q| \log |q|}=\int_{0}^{2 \pi} \int_{0}^{\epsilon} \frac{2 r^{\frac{1}{2}} d r d \theta}{\log (r)}<\infty$$
for small enough $\epsilon>0$.
To check that the $(1,1)$-form $\bar{\partial} \partial \log \left(\|\eta\|_{\hat{h}^{*}}^{2}\right)$ is locally integrable around $q=0$, we should only check that the function $\frac{1}{|q|^{2} \log ^{2}|q|^{2}}$ is locally integrable around $q=0$. This follows from
$$\int_{|q|<\epsilon} \frac{d q \wedge d \bar{q}}{|q|^{2} \log ^{2}|q|}=\int_{0}^{2 \pi} \int_{0}^{\epsilon} \frac{d r d \theta}{r \log ^{2}(r)}<\infty$$
for small enough $\epsilon>0$. When $\zeta_{1}, \ldots, \zeta_{n}$ and $\xi_{1}, \ldots, \xi_{n}$ are bounded and $q \rightarrow 0$, using (17) we have the the asymptotic relation
$$\frac{\log \left(\left.\|\eta\|\right|_{\hat{h}^{*}} ^{2}\right)}{\log |q|} \sim \frac{c \log (u)}{\log |q|} \sim \frac{c \log (-\log |q|)}{\log |q|} \sim 0,$$
where $c \in \mathbb{R}$. Hence, we can apply Proposition 3.3 to $\log \left(\|\eta\|_{\hat{h}^{*}}^{2}\right)$. \(\square\)

\section*{4. $\mathbb{Q}$-vector bundles and Base loci}

The goal of this section is to prove formal properties of $\mathbb{Q}$-vector bundles which will be used in §5 and §6 to study the twists of $\Omega \frac{1}{X}$ and $\Omega \frac{1}{X}(\log (D))$. To this end, we use the definitions and properties of the base loci of a vector bundle which has been systematically studied in $\left[\mathrm{BKK}^{+} 15\right]$. We also use the definitions and properties of $\mathbb{Q}$-vector bundles from [Laz04, section 6].

Let $E$ be a vector bundle over a projective variety $\bar{Y}$, and $D$ be an integral divisor on $\bar{Y}$. The base locus of $E$ is defined to be the subset
$$\operatorname{Bs}(E)=\left\{y \in \bar{Y} \mid H^{0}(\bar{Y}, E) \rightarrow E(y) \text { is not surjective }\right\},$$
and the stable base loci of $E$ is defined to be the algebraic subset
$$\mathbb{B}(E)=\bigcap_{m \geq 0} \operatorname{Bs}\left(S^{m} E\right) .$$
Let $r$ be a rational number.
Definition 4.1. A $\mathbb{Q}$-vector bundle $E\langle r D\rangle$ on $\bar{Y}$ is a pair consisting of a vector bundle $E$ on $\bar{Y}$ and a $\mathbb{Q}$-divisor $r D \in \operatorname{Div}_{\mathbb{Q}}(\bar{Y})$. A $\mathbb{Q}$-isomorphism of $\mathbb{Q}$-vector bundles is the equivalence relation generated by considering $E\left\langle D^{\prime}+r D\right\rangle$ to be equivalent to $E \otimes O_{\bar{Y}}\left(D^{\prime}\right)\langle r D\rangle$, where $D^{\prime}$ is an integral divisor.

The formal symbol $E\langle r D\rangle$ is intended to say that we are twisting the vector bundle $E$ by a $\mathbb{Q}$-divisor $r D$. The symmetric power $S^{m}(E\langle r D\rangle)$ denotes the $\mathbb{Q}$-vector bundle $S^{m}(E)\langle m r D\rangle$. It is easy to observe that every $\mathbb{Q}$-vector bundle has a symmetric power which is $\mathbb{Q}$-isomorphic
to a vector bundle. Let $a$ and $b$ be integers such that $b$ is positive. We will define the base loci of the $\mathbb{Q}$-vector bundle $E\left\langle\frac{a}{b} D\right\rangle$ to be the following set
$$\mathbb{B}\left(E\left\langle\frac{a}{b} D\right\rangle\right)=\bigcap_{m>0} \operatorname{Bs}\left(S^{m b} E \otimes O_{\bar{Y}}(m a D)\right),$$
which does not depend on the choice of $a, b$. Let $A$ be an ample divisor on $\bar{Y}$. The augmented base locus of $E$ is the algebraic subset
$$\mathbb{B}_{+}(E)=\bigcap_{r \in \mathbb{Q}_{+}} \mathbb{B}(E\langle-r A\rangle),$$
which does not depend on the choice of the ample divisor $A$.
Definition 4.2. We say that $E\langle r D\rangle$ is ample (nef) if one of the following equivalent properties holds:
\begin{itemize}
\item[(i)] The $\mathbb{Q}$-divisor $O_{\mathbb{P}(E)}(1)+\pi^{*}(r D)$ is ample (nef) on $\mathbb{P}(E)$.
\item[(ii)] $E\langle r D\rangle$ has a symmetric power which is $\mathbb{Q}$-isomorphic to an ample (a nef) vector bundle.
\item[(iii)] If $r=a / b$ and $b$ is positive, then the vector bundle $S^{b} E \otimes O_{\bar{Y}}(a D)$ is ample (nef).
\end{itemize}

The equivalency of these definitions is checked in [Laz17, Lemma 6.2.8].
Lemma 4.3. If $E$ is a nef vector bundle and $r D$ is an ample $\mathbb{Q}$-divisor, then $E\langle r D\rangle$ is an ample $\mathbb{Q}$-vector bundle.

Proof. Take $a, b \in \mathbb{Z}$ such that $r=a / b$ and $b$ is positive. As $r D$ is ample, the integral divisor $a D$ is ample. Since $E$ is nef, $S^{b} E$ is nef. Combining these two we get that $S^{b} E \otimes O_{\bar{Y}}(a D)$ is an ample vector bundle. Hence, $E\langle r D\rangle$ is ample. \(\square\)

Lemma 4.4. Suppose $0 \rightarrow G \rightarrow E \rightarrow F \rightarrow 0$ is an exact sequence of vector bundles on a projective variety $\bar{Y}$. The following hold:
\begin{itemize}
\item[(i)] If $E\langle r D\rangle$ is ample (nef), then $F\langle r D\rangle$ is ample (nef).
\item[(ii)] If $G\langle r D\rangle$ and $F\langle r D\rangle$ are ample, then $E\langle r D\rangle$ is ample.
\end{itemize}

Proof. (i) Since $\mathbb{P}(E)$ parametrizes one-dimensional quotients, the surjection $E \rightarrow F$ corresponds to an inclusion $\mathbb{P}(E) \subset \mathbb{P}(F)$, such that the restriction of $O_{\mathbb{P}(E)}(1)$ is $O_{\mathbb{P}(F)}(1)$. Hence, the ampleness (nefness) of $O_{\mathbb{P}(E)}(1)+\pi^{*}(r D)$ implies the ampleness (nefness) of $O_{\mathbb{P}(F)}(1)+\pi^{*}(r D)$.
(ii) See [Laz04, Lemma 6.2.8]. \(\square\)

Note that the above mentioned definitions for a $\mathbb{Q}$-vector bundle $E\langle r D\rangle$ agree with the usual definitions for a vector bundle when a vector bundle $E$ is considered as the $\mathbb{Q}$-vector bundle $E\langle 0\rangle$.

Definition 4.5. A vector bundle $E$ over $\bar{Y}$ is said to be ample modulo $D$ if for every coherent sheaf $\mathscr{F}$ over $\bar{Y}$, there exists an $m_{0}>0$ such that if $m>m_{0}$, then for every $y \in \bar{Y} \backslash D$, the fiber $\mathscr{F} \otimes S^{m}(E)_{\mid y}$ is generated by $H^{0}\left(Y, \mathscr{F} \otimes S^{m}(E)\right)$.

There is an obvious relation between the notion of ampleness modulo a divisor and the augmented base loci:

Proposition 4.6. If the vector bundle $E$ is ample modulo $D$, then the augmented base loci $\mathbb{B}_{+}(E)$ contained in $D$ and $\mathbb{B}_{+}\left(O_{\mathbb{P}(E)}(1)\right)$ is contained in $\pi^{*}(D)$.

Proof. Pick an arbitrary point $y \in \bar{Y} \backslash D$. To show $\mathbb{B}_{+}(E) \subset D$, it is enough to show that $y \notin \mathbb{B}_{+}(E)$. Let $A$ be an ample line bundle. By Definition 4.5, there exist $n$ such that $\left(S^{n} E-A\right)_{\mid y}$ is generated by $H^{0}\left(Y, S^{n} E-A\right)$ and therefore $y \notin \mathbb{B}\left(E\left\langle-\frac{1}{n} A\right\rangle\right)$. Consequently, $y \notin \mathbb{B}_{+}(E)$.
[BKK ${ }^{+}$15, Proposition 3.2] tells us that $\mathbb{B}_{+}\left(O_{\mathbb{P}(E)}(1)\right) \subset \pi^{-1}\left(\mathbb{B}_{+}(E)\right)$ and therefore the previous part gives that $\mathbb{B}_{+}\left(O_{\mathbb{P}(E)}(1)\right) \subset \pi^{*}(D)$. \(\square\)

Suppose $L$ is a line bundle on a projective variety $\bar{Y}$. It is well-known that $L$ is big if and only if $\mathbb{B}_{+}(L) \neq X$. This follows that if $E$ is ample modulo $D$, then $E$ is big in the sense that $O_{\mathbb{P}(E)}(1)$ is big. Another well-know fact is that $L$ is ample if and only if $\mathbb{B}_{+}(L)=\emptyset$. For vector bundles, we will use the following lemma to go from the ampleness modulo $D$ to the ampleness:

Lemma 4.7. If $E$ is ample modulo $D$ and $E_{\mid D}$ is ample, then $E$ is ample.
Proof. Let $L$ be the line bundle $O_{\mathbb{P}(E)}(1)$ on $\mathbb{P}(E)$. To conclude ampleness it is sufficient to prove that for any subvariety $V \subset \mathbb{P}(E)$ with dimension $m$, one has $c_{1}(L)^{\operatorname{dim} V} \cdot V>0$. We prove it by induction on $m$ :

First, we show that for every irreducible curve $C$ on $\mathbb{P}(E)$, we have $L \cdot C>0$. If $C \subset \pi^{*}(D)$, then $C \cdot L>0$ because $L_{\mid \pi^{*}(D)}$ is ample. If $C$ is not contained in $D$, then there is a point $x \in C$ such that $x \notin \pi^{*}(D)$. Since $E$ is ample modulo $D$, Proposition 4.6 gives that $\mathbb{B}_{+}(L) \subset \pi^{*}(D)$ and therefore $x \notin \mathbb{B}_{+}(L)$. It means that there exist $a, b \in \mathbb{Z}^{+}$such that $x \notin \mathbf{B s}(b L-a A)$, where $A$ is an ample divisor on $\mathbb{P}(E)$. Consequently, the zero locus of $b L-a A$ is not contained in $C$ and it follows that $C$ intersects transversely with $b L-a A$. Hence. $C \cdot(b L-a A) \geq 0$ which gives that $C \cdot L>0$.

Similarly, when $m>1$, there are two cases to consider. If $V \subset \pi^{*}(D)$, then the result comes from the fact that $E_{\mid D}$ is ample. If $V \not \subset \pi^{*}(D)$, then $V \not \subset \mathbb{B}_{+}(L)$. Therefore, there exists $a, b \in \mathbb{Z}^{+}$and a section $s \in H^{0}(b L-a A)$ such that $V \not \subset\{s=0\}$. Let $W$ be the $(m-1)$-cycle on $V$ associated with the schematic locus $\left\{s_{\mid V}=0\right\}$. It is either 0 or a formal sum of $(m-1)$-dimensional subvarieties with positive coefficients. Therefore, one has
$$(b L-a A) \cdot V \sim_{r a t} W,$$
and therefore $(b L) \cdot V \sim_{\text {rat }} W+(a A) \cdot V$. As A is ample, the class $A \cdot V$ is provided by an $(m-1)$-cycle with only positive coefficients. Since
$$b L^{m} \cdot V=L^{m-1} \cdot(W+a A \cdot V)$$
and the second factor on the right hand side is a $(m-1)$-dimensional cycle with only positive coefficients, so we get the result by induction. \(\square\)

Definition 4.8. We say that $E\langle r D\rangle$ is ample modulo $D$ if one of the following two equivalent properties holds:
\begin{itemize}
\item[(i)] $E\langle r D\rangle$ has a symmetric power which is $\mathbb{Q}$-isomorphic to an ample modulo $D$ vector bundle.
\end{itemize}
\begin{itemize}
\item[(ii)] If $r=a / b$ and $b$ is positive, then the vector bundle $S^{b} E \otimes O_{\bar{Y}}(a D)$ is ample modulo $D$.
\end{itemize}

Definition 4.9. Consider two $\mathbb{Q}$ - vector bundles $E\left\langle\frac{a}{b} D\right\rangle$ and $F\left\langle\frac{a^{\prime}}{b} D\right\rangle$, where $r$ and $s$ are two rational numbers. We say that $E\langle r D\rangle$ is a $\mathbb{Q}$-subsheaf of $F\langle s D\rangle$ if for every integer $a, a^{\prime}$ and every positive integer $b$ such that $r=\frac{a}{b}$ and $s=\frac{a^{\prime}}{b}$, the vector bundle $S^{b} E \otimes O_{\bar{Y}}(a D)$ is a subsheaf of $S^{b} F \otimes O_{\bar{Y}}\left(a^{\prime} D\right)$.

Lemma 4.10. Let $E$ and $F$ be vector bundles on $\bar{Y}$ and they are isomorphic over $Y:=\bar{Y} \backslash D$. Suppose $E\langle r D\rangle$ is a $\mathbb{Q}$-subsheaf of $F\langle s D\rangle$, and $E\langle r D\rangle$ is ample modulo $D$. Then $F\langle s D\rangle$ is ample modulo $D$.

Proof. Take $a, a^{\prime}, b \in \mathbb{Z}$ such that $a / b=r, a^{\prime} / b^{\prime}=s$ and $b$ is positive. Since the $\mathbb{Q}$-vector bundle $E\left\langle\frac{a}{b} D\right\rangle$ is ample modulo $D$, there exists an integer $l \in \mathbb{Z}$ such that the vector bundle $S^{\text {bl }} E \otimes O_{\bar{Y}}(a l D)$ is ample modulo $D$. It means that for a given coherent sheaves $\mathscr{F}$ over $\bar{Y}$ there exists $m_{0}>0$ such that for every $m>m_{0}$ and every $y \in Y,\left(\mathscr{F} \otimes S^{\text {blm }} E \otimes O_{\bar{Y}}(a l D)\right)_{\mid y}$ is generated by $H^{0}\left(\bar{Y}, \mathscr{F} \otimes S^{b l m} E \otimes O_{\bar{Y}}(a l D)\right)_{\mid y}$. Because $E\langle r D\rangle$ is a $\mathbb{Q}$-subsheaf of $F\langle s D\rangle$, we obtain that $\left.\mathscr{F} \otimes S^{\text {blm }} E \otimes O_{\bar{Y}}(a l D)\right)$ is a subsheaf of $\left.\mathscr{F} \otimes S^{\text {blm }} F \otimes O_{\bar{Y}}\left(a^{\prime} l D\right)\right)$. This implies that
$$H^{0}\left(\bar{Y}, \mathscr{F} \otimes S^{b l m} E \otimes O_{\bar{Y}}(a l D)\right) \subseteq H^{0}\left(\bar{Y}, \mathscr{F} \otimes S^{b l m} F \otimes O_{\bar{Y}}\left(a^{\prime} l D\right)\right) .$$

Since these two sheaves restricts to the same sheaf on $Y$, for every $y \in Y$ and for every $m>m_{0}, \mathscr{F} \otimes S^{b l m} E \otimes O_{\bar{Y}}\left(a^{\prime} l D\right)$ is generated by $H^{0}\left(\bar{X}, F \otimes S^{m} E_{2}\right)$. \(\square\)

Lemma 4.11. Let $r \in \mathbb{Q}^{+}$be a positive rational number. If $E\langle-r D\rangle$ is ample modulo $D$, then $E\langle-s D\rangle$ is ample modulo $D$ for any rational $s<r$.

Proof. Let $a, a^{\prime}, b \in \mathbb{Z}$ be positive integers such $a / b=r$ and $a^{\prime} / b=s$. Since $s<r$, we get that $a^{\prime}<a$ and therefore $S^{b} E \otimes_{\bar{Y}}(-a D)$ is a subsheaf of $S^{b} E \otimes_{\bar{Y}}\left(-a^{\prime} D\right)$ and the claim follows from Lemma 4.10. \(\square\)

Lemma 4.12. Suppose $f: Y^{\prime} \longrightarrow Y$ is a finite surjective map and $E$ is a vector bundle on $Y$. Then, $f^{*} E$ is semi-ample, then $E$ is so.

Proof. By passing to the projective bundles, the lemma follows from the corresponding facts for line bundles ( see [Fuj83, 1.20]) \(\square\)

\section*{5. Positivity of $\Omega \frac{1}{X}(\log (D))$}

Throughout this section, we adopt the convention that $\Gamma$ is a torsion-free lattice in $\operatorname{PU}(n, 1), X=\Gamma \backslash \mathbb{B}^{n}$ is a complex hyperbolic manifold with cusps, $\bar{X}$ is the toroidal compactification of $X$ and $d$ is the uniform depth of cusps. Additionally, we assume that $\bar{X}$ does not have any orbifold point.

The goal of this section is to prove the ampleness of the twisted logarithmic cotangent bundle as stated in Theorem A. To prove this theorem, we need to construct a singular hermitian metric using the properties of the Bergman metric proved in the previous section, namely Proposition 3.2 and Proposition 3.4. By virtue of Theorem A, we will conclude the positivity properties of $\Omega_{\bar{X}}^{\underline{1}}(\log (D))$ stated in Corollary G.

Suppose $\bar{Y}$ is a smooth projective variety and $D$ is divisor on $\bar{Y}$. As proved in [ADT22, BD18], if $\operatorname{dim} \bar{Y}>1$, the logarithmic cotangent bundle $\Omega_{\bar{Y}}^{1}(\log (D))$ is never ample because
its restriction to $D$ is an extension of the trivial bundle. Therefore, to describe a positivity properties of $\Omega \frac{1}{\bar{Y}}(\log (D))$ we need a weaker positivity notion.

In the case of the toroidal compactification $\bar{X}$ of $X$, the first step toward understanding the positivity of the cotangent bundles is to study the positively of the cotangent bundle restricted to the boundary divisor $D$. The connected components of $D$ are étale quotients of abelian varieties whose conormal bundles are ample and therefore considering the conormal bundle exact sequence
$$0 \longrightarrow O_{D}(-D) \longrightarrow \Omega_{\bar{X} \mid D}^{1} \longrightarrow \Omega_{D}^{1} \longrightarrow 0,$$
on $D$, one can observe that $\Omega_{\bar{X} \mid D}^{1}$ is an extension of a vector bundle with vanishing Chern classes, by an ample line bundle. Moreover, we will prove that $\Omega_{\bar{X} \mid D}^{1}$ is semi-ample in the sense that $O(1)$ on $\mathbb{P}\left(\Omega_{\bar{X} \mid D}^{1}\right)$ is semi-ample. To this end, we need the following lemma:

Lemma 5.1. Suppose $0 \rightarrow G \rightarrow E \rightarrow F \rightarrow 0$ is an exact sequence of vector bundles on a projective variety $\bar{Y}$ such that $H^{1}(\bar{Y}, G)=0$. If $S^{m} G$ and $F$ are globally generated, then $O_{\mathbb{P}(E)}(m)$ is globally generated.

Proof. $H^{1}(\bar{Y}, G)=0$ gives the exact sequence of global sections:
$$0 \longrightarrow H^{0}(\bar{Y}, G) \longrightarrow H^{0}(\bar{Y}, E) \longrightarrow H^{0}(\bar{Y}, F) \longrightarrow 0 .$$
This implies that $H^{0}\left(\bar{Y}, S^{m} G\right)$ injects into $H^{0}\left(\bar{Y}, S^{m} F\right)$ and $H^{0}(\bar{Y}, E)$ surjects onto $H^{0}(\bar{Y}, F)$.
To prove that $O_{\mathbb{P}(E)}(m)$ is globally generated, we need to show that for every $p \in \mathbb{P}(E)$, the fiber $O_{\mathbb{P}(E)}(m)_{\mid p}$ is generated by global sections of $O_{\mathbb{P}(E)}(m)$. Suppose $p \in \mathbb{P}(E)$ is determined by $y \in \bar{Y}$ and an one-dimensional quotient $E_{p} \rightarrow L_{p}$. Consider the map $\eta_{y}: G_{y} \rightarrow L_{y}$. We may have two cases:
\begin{itemize}
\item[(1)] $\eta_{y}: G_{y} \rightarrow L_{y}$ is the zero map. In this case, $\eta_{y}$ factors through $F_{y}$. On the other hand, $H^{0}(\bar{Y}, E)$ surjects onto $H^{0}(\bar{Y}, F)$, and $F$ is globally generated. Since
$$H^{0}(\bar{Y}, E) \cong H^{0}\left(\mathbb{P}(E), O_{\mathbb{P}(E)}(1)\right),$$
the fiber $O_{\mathbb{P}(E)}(1)_{\mid p}$ is generated by the global sections and therefore $O_{\mathbb{P}(E)}(m)_{\mid p}$ is generated by global sections.
\item[(2)] $\eta_{y}: G_{y} \rightarrow L_{y}$ is a non-zero map. Since $H^{0}\left(\bar{Y}, S^{m} G\right)$ injects into $H^{0}\left(\bar{Y}, S^{m} E\right)$ and $S^{m} G$ is globally generated, the global sections $H^{0}\left(\mathbb{P}(E), O_{\mathbb{P}(E)}(m)\right) \cong H^{0}\left(\bar{Y}, S^{m} E\right)$ generates the fiber $O_{\mathbb{P}(E)}(m)_{\mid p}$.
Hence, $O_{\mathbb{P}(E)}(m)$ is globally generated, as desired.
\end{itemize} \(\square\)

Now, we can study the positivity of the twisted cotangent bundle restrict to the boundary divisor:

Proposition 5.2. Suppose that the dimension of $X$ is greater than 1 and $r$ is a rational number. Consider the $\mathbb{Q}$-vector bundles
$$E_{r}:=\Omega_{\bar{X} \mid D}^{1}\left\langle-r D_{\mid D}\right\rangle .$$
The following hold:
\begin{itemize}
\item[(i)] If $r=0$, then $E_{r}=\Omega_{\bar{X} \mid D}^{1}$ is semi-ample, but not ample.
\end{itemize}
\begin{itemize}
\item[(ii)] If $r>0$, then $E_{r}$ is ample.
\end{itemize}

Proof. (i) Let $D_{i}$ be a connected component of $D$. We can write the exact sequence 18 on $D_{i}$ :
$$0 \longrightarrow O_{D_{i}}\left(-D_{i}\right) \longrightarrow E_{0 \mid D_{i}} \longrightarrow \Omega_{D_{i}}^{1} \longrightarrow 0 .$$

As $D_{i}$ is an étale quotient of abelian variety, there is a finite étale map $f: D^{\prime} \longrightarrow D_{i}$, where $D^{\prime}$ is an abelian variety. We pull back the previous exact sequence to $D^{\prime}$ :
$$0 \longrightarrow f^{*} O_{D_{i}}\left(-D_{i}\right) \xrightarrow{\phi} f^{*} E_{0 \mid D_{i}} \longrightarrow f^{*} \Omega_{D_{i}}^{1} \longrightarrow 0 .$$

As $O_{D_{i}}\left(-D_{i}\right)$ is ample and $f$ is finite, $f^{*} O_{D_{i}}\left(-D_{i}\right)$ is ample. As $f$ is an étale map $f^{*} \Omega_{D_{i}}^{1} \cong \Omega_{D^{\prime}}^{1}$ which is trivial because $D^{\prime}$ is an abelian variety. Since $f^{*} E_{0 \mid D_{i}}$ has a trivial quotient, $E_{0 \mid D_{i}}$ can not be ample.

To show semi-ampleness, note that $\Omega_{D_{i}}^{1}$ is in particular globally generated. Also, $f^{*} O_{D_{i}}\left(-D_{i}\right)$ is ample because $-D_{i \mid D_{i}}$ is ample and $f$ is finite. Therefore, there exist $m \in \mathbb{Z}^{+}$such that $m f^{*} O_{D_{i}}\left(-D_{i}\right)$ is globally generated on $f^{-1}\left(D_{i}\right)$. Additionally, the Kodaira's vanishing theorem gives that $H^{1}\left(f^{-1}\left(D_{i}\right), f^{*} O_{D_{i}}\left(-D_{i}\right)\right)=0$. Thanks to Lemma 5.1, we can conclude that $f^{*} E_{0 \mid D_{i}}$ is semi-ample and therefore Lemma 4.12, implies that $E_{0 \mid D_{i}}$ is semi-ample.
(ii) Since $E_{0 \mid D_{i}}$ is in particular nef by (i) and the conormal bundle $-D_{D}$ is ample, we can conclude from Lemma 4.3 that $E_{r}$ is ample. \(\square\)

Recall the following exact sequence:
$$0 \longrightarrow \Omega \frac{1}{\bar{X}} \longrightarrow \Omega \frac{1}{\bar{X}}(\log (D)) \xrightarrow{\text { res }} O_{D} \longrightarrow 0,$$
where the morphism res is the residue map sending $\sum_{i=1}^{n-1} f_{i} d \zeta_{i}+g \frac{d q}{q}$ to $g$.
Proposition 5.3. Suppose that the dimension of $X$ is greater than 1 and $r$ is a rational number. Consider the $\mathbb{Q}$-vector bundles
$$F_{r}:=\Omega_{\bar{X}}^{1}(\log (D))_{\mid D}\left\langle-r D_{\mid D}\right\rangle .$$
The following hold:
\begin{itemize}
\item[(i)] If $r=0$, then $F_{r}=\Omega_{\bar{X}}^{1}(\log (D))_{\mid D}$ is nef, but not ample.
\item[(ii)] If $r>0$, then $F_{r}$ is ample.
\end{itemize}

Proof. Let $D_{i}$ be a connected component of $D$. Restricting the exact sequence (19) to $D_{i}$ gives the exact sequence:
$$\Omega_{\bar{X} \mid D_{i}}^{1} \xrightarrow{\phi_{1}} F_{0 \mid D_{i}} \xrightarrow{\phi_{2}} O_{D_{i}} \longrightarrow 0,$$
where $\phi_{1}$ is the inclusion and $\phi_{2}$ is the residue map sending $\sum_{i=1}^{n-1} f_{i} d z_{i}+g \frac{d q}{q}$ to $g_{\mid D_{i}}$ on an open set $U$ on which the local coordinate of $D_{i}$ is $(q=0)$. Therefore, we get the exact sequence
$$0 \longrightarrow \operatorname{Im}\left(\phi_{1}\right) \longrightarrow F_{0 \mid D_{i}} \xrightarrow{\phi_{2}} O_{D_{i}} \longrightarrow 0 .$$

Note that $\operatorname{Im}\left(\phi_{1}\right)$ is a quotient of $\Omega_{\bar{X} \mid D_{i}}^{1}$ which is in particular nef by Proposition 5.2. Therefore, $\operatorname{Im}\left(\phi_{1}\right)$ is nef.
(i) Since $F_{0 \mid D_{i}}$ admits a trivial quotient, it is not ample. However, it is an extension of a nef bundle by a nef bundle; therefore it is nef.
(ii) Since $F_{0 \mid D_{i}}$ is nef and $-r D_{i \mid D_{i}}$ is ample for $r>0$, it follows from Lemma 4.3 that $F_{r}$ is ample when $r>0$. \(\square\)

Another ingredient we need in order to construct a singular hermitian metric is an appropriate weight function. Roughly speaking, this weight function will be a plurisubharmonic function, supported on a horoball with the largest possible Lelong number on the boundary. The desired wight function on the hoorball around the cusp $c_{i}$ will be constructed using the following Lemma: