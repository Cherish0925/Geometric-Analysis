---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: 1005_1980.pdf
converter: mathpix
format: mmd
---

\title{
Cusps of Picard modular surfaces
}

\author{
Matthew Stover \\ University of Texas at Austin \\ mstover@math.utexas.edu
}

October 27, 2018

\begin{abstract}
We determine the number of cusps of minimal Picard modular surfaces. The proof also counts cusps of other Picard modular surfaces of arithmetic interest. Consequently, for each $N>0$ there are finitely many commensurability classes of nonuniform arithmetic lattices in $\operatorname{SU}(2,1)$ that contain an $N$-cusped surface. We also discuss a higher-rank analogue.
\end{abstract}

\section*{1 Introduction}

To study the cusps of locally symmetric spaces, it is most natural to begin with the minimal elements of each commensurability class. From there, one can, ostensibly, use the combinatorics of covering spaces to study the rest of the commensurability class. The purpose of this paper is to study the cusps of minimal arithmetic complex hyperbolic 2-orbifolds. Equivalently, we study cusps of maximal nonuniform arithmetic lattices in $\operatorname{PU}(2,1)$. These algebraic surfaces are often called Picard modular surfaces, and their fundamental groups Picard modular groups.

We begin with two remarks. First, by Mostow-Prasad rigidity, when $\Gamma$ is an irreducible lattice in any semisimple group except $\operatorname{SL}_{2}(\mathbb{R})$, the corresponding locally symmetric quotient $M$ is uniquely determined by $\Gamma$. Therefore, there is no ambiguity in saying 'the cusps of $\Gamma^{\prime}$ as opposed to 'the cusps of $M^{\prime}$. For $\mathrm{SL}_{2}(\mathbb{R})$, there is an easy counterexample: the free group on two generators is the fundamental group of both the thrice-punctured sphere and once-punctured torus. Second, it is a consequence of work of Borel and the arithmeticity theorem of Margulis that a lattice $\Gamma$ in a semisimple Lie group is arithmetic if and only if there are infinitely many distinct isomorphism classes of maximal lattices in its commensurability class. In fact, $\Gamma$ is nonarithmetic if and only if there is a unique maximal element in its commensurability class.

If $\Gamma<\mathrm{PU}(2,1)$ is a maximal arithmetic lattice, it is best described using Bruhat-Tits theory. See §3. The preceding section, §2, is a brief review of complex hyperbolic geometry and some of the algebraic tools we use. The goal of §4 is to count cusps of minimal Picard modular surfaces. The results are difficult
to state without the notation of §3, so we refer to §4 for precise statements. The main technical result is Theorem 4.8. The formula for a minimal surface is roughly the following.

Theorem 1.1. Let $M$ be a minimal Picard modular surface, defined via a hermitian form over the imaginary quadratic field $k$. Then there exists a nonnegative integer $n$, depending explicitly on $M$, such that $M$ has
$$3^{n} \frac{h_{k}}{h_{k, 3}}$$
cusps, where $h_{k}$ is the class number of $k$ and $h_{k, 3}$ is the order of the threeprimary part of the class group of $k$.

In short, the proof involves counting the number of cusps for particular congruence subgroups of a given lattice, then using these counts to determine the number of cusps for the minimal surface. These congruence subgroups are natural generalizations of Hecke's subgroups $\Gamma_{0}(N)$ in $\operatorname{PSL}_{2}(\mathbb{Z})$ (cf. the groups considered in [3]). Using Bruhat-Tits theory, one is then able to move around the commensurability class and keep track of the action on cusps. The proof is inspired equally by Zink's study of cusps of lattices in unitary groups [18] and Chinburg-Long-Reid's paper on cusps of minimal arithmetic hyperbolic 3-orbifolds [3].

Our primary application of Theorem 1.1 is to the classification, up to commensurability, of noncompact finite volume complex hyperbolic orbifolds. The following, which we prove at the end of §4, utilizes work of Ellenberg-Venkatesh [4] on torsion in the ideal class group.

Theorem 1.2. For any $N>0$, there are only finitely many commensurability classes of Picard modular surfaces containing an element with $N$ cusps.

It remains unknown whether or not there are infinitely many commensurability classes of nonarithmetic complex hyperbolic 2-orbifolds. For hyperbolic 3-space, Chinburg-Long-Reid [3] proved the analogue to Theorem 1.2, but there are infinitely many commensurability classes of non-commensurable hyperbolic knot complements (e.g., twist knots), so arithmetic assumption is crucial.

We also prove a higher-rank version of Theorems 1.1 and 1.2. Let $\Gamma<$ $\operatorname{SU}(r+1, r)$ be a maximal nonuniform lattice with $r>1$. By the monumental work of Margulis, $\Gamma$ is automatically arithmetic. All nonuniform arithmetic lattices in $\operatorname{SU}(2,1)$ arise from hermitian forms in $k^{3}$, where $k$ is any imaginary quadratic field. In higher rank, there are other methods of producing nonuniform arithmetic lattices, all of which arise from hermitian forms over division algebras with involution of second kind. We say that a lattice is of simple type if it arises from a hermitian form over an imaginary quadratic field. As in [18], the methods of Theorem 1.1 extend to higher rank lattices of simple type.

Theorem 1.3. Let $\Gamma<\operatorname{SU}(r+1, r)$ be a maximal nonuniform lattice of simple type, and set $q=2 r+1$. Then there exists a number $n$, depending explicitly on
$\Gamma$, so that $\Gamma$ has
$$q^{n} \frac{h_{k}^{r}}{h_{k, q}}$$
cusps, where $h_{k}$ is the class number of $k$ and $h_{k, q}$ is the order of the subgroup of the class group of $k$ consisting of elements with order dividing $q$.

Since $\operatorname{SU}(2,1)$ has $\mathbb{R}$-rank one, cusps correspond to topological ends of the corresponding orbifold. In higher rank, 'cusps' correspond to maximal chains $P_{0} \subset P_{1} \subset \cdots \subset P_{r}$ of parabolic subgroups. For geometric interpretations, see [1]. When $q$ is prime, all nonuniform lattices are of simple type. This allows us to give a full classification of the commensurability classes of locally symmetric spaces with $\operatorname{SU}(r+1, r)$-geometry containing a one-cusped element.

Theorem 1.4. For $r>1$ and $2 r+1$ prime, there are only finitely many commensurability classes of locally symmetric spaces with $\operatorname{SU}(r+1, r)$-geometry containing a one-cusped element. Furthermore, assuming the Generalized Riemann Hypothesis, there are only finitely many commensurability classes containing an $N$-cusped element for any $N>0$.

We also show how, for each $r \geq 1$, one can construct infinitely many homeomorphism classes of one-cusped orbifolds with $\operatorname{SU}(r+1, r)$-geometry. However, none of the spaces we build are manifolds. The following seems to be a significant gap in our understanding of complex hyperbolic manifolds.

Question. Does there exist a one-cusped complex hyperbolic 2-manifold?
Restrictions on the possible cusp cross-sections are given by unpublished work of Neumann-Reid and Kamishima [7]. There are one-cusped hyperbolic manifolds commensurable with the modular curve, and, though the figure-eight knot is the unique arithmetic knot complement [14], several Bianchi groups $\operatorname{PSL}_{2}\left(\mathcal{O}_{d}\right)$ contain a one-cusped manifold. See also [9]. The corresponding question for higher dimensional hyperbolic manifolds also appears to be unsolved.

\section*{2 Preliminaries}

\subsection*{2.1 Complex hyperbolic geometry}

Let $V$ be a three-dimensional complex vector space equipped with a nondegenerate hermitian form $h$ of signature (2, 1). In this paper, $h$ will typically be the form with matrix
$$h_{0}=\left(\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right) .$$
The complex hyperbolic plane is $\mathbf{H}_{\mathbb{C}}^{2}=\mathbb{P}\left(V_{-}\right) \subset \mathbb{P}^{2}$, where $V_{-}$is the set of $h$-positive vectors in $V$. With the metric associated to $h$, the biholomorphic isometry group of $\mathbf{H}_{\mathbb{C}}^{2}$ is $\operatorname{PU}(2,1)$.

The ideal boundary $\partial_{\infty} \mathbf{H}_{\mathbb{C}}^{2}$ of complex hyperbolic space is the image in $\mathbb{P}^{2}$ of the $h$-isotropic vectors $V_{0}$. For $h_{0}, \mathbf{H}_{\mathbb{C}}^{2}$ has homogeneous coordinates
$$\left\{\left[\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right]: 2 \operatorname{Re}\left(z_{1} \bar{z}_{3}\right)-\left|z_{2}\right|^{2}>0\right\}$$
and $\partial_{\infty} \mathbf{H}_{\mathbb{C}}^{2}$ is
$$\left\{\left[\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right]: 2 \operatorname{Re}\left(z_{1} \bar{z}_{3}\right)-\left|z_{2}\right|^{2}=0\right\} .$$

A complex hyperbolic 2-orbifold is $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma$, where $\Gamma<\operatorname{PU}(2,1)$ is a discrete subgroup of isometries such that $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma$ has finite volume. Isometries fall into three categories based upon their action on $\mathbf{H}_{\mathbb{C}}^{2}$ and its ideal boundary. An isometry is elliptic if it has a fixed point in the complex hyperbolic plane, loxodromic if it is not elliptic and has two fixed points on the ideal boundary, and is parabolic if it is not elliptic and fixes exactly one point on the ideal boundary.

A lattice $\Gamma$ is called uniform if $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma$, or equivalently $\operatorname{PU}(2,1) / \Gamma$, is compact. Otherwise it is nonuniform and $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma$ has a finite number of topological ends. A lattice is nonuniform if and only if it contains parabolic elements.

The cusp set of $\Gamma$ is the set of all fixed points of parabolic elements in $\Gamma$. There is a natural $\Gamma$-action on the cusp set, and a cusp of $\Gamma$ is a $\Gamma$-equivalence class of fixed points of parabolic elements in $\Gamma$. The topological ends of $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma$ are in one-to-one correspondence with the cusps of $\Gamma$. As mentioned in the introduction, by Mostow-Prasad rigidity, the number of cusps of $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma$ is an invariant of the lattice. Therefore, we will alternate freely between saying 'the cusps of $\Gamma^{\prime}$ and 'the cusps of $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma^{\prime}$ throughout.

\subsection*{2.2 Algebra of hermitian forms}

Let $V$ be a vector space of dimension $n$ over the number field $k$. If $\mathcal{O}_{k}$ is the ring of integers of $k$, a lattice $\mathcal{L} \subset V$ is an $\mathcal{O}_{k}$-submodule such that $\mathcal{L} \otimes_{\mathcal{O}_{k}} k=V$. Since $\mathcal{O}_{k}$ is a Noetherian ring, there is an isomorphism of $\mathcal{O}_{k}$-modules
$$\mathcal{L} \cong_{\mathcal{O}_{k}} I_{1} \oplus \cdots \oplus I_{n},$$
where each $I_{j}$ is a fractional ideal of $k$. This decomposition is determined up to isomorphism by the ideal class $\operatorname{cl}(\mathcal{L})$, which is the class of the product $I_{1} \cdots I_{n}$ in the ideal class group of $k$. That is, two lattices $\mathcal{L}_{1}$ and $\mathcal{L}_{2}$ are isomorphic as $\mathcal{O}_{k}$-modules if and only if they have the same dimension and $\operatorname{cl}\left(\mathcal{L}_{1}\right)=\operatorname{cl}\left(\mathcal{L}_{2}\right)$.

Now, suppose that $k$ is an imaginary quadratic field and that $h$ is a non-degenerate hermitian form on $V$. Then $h$ is determined up to isomorphism by $\operatorname{det}(h)$, considered as an element of $\mathbb{Q}^{\times} / \mathrm{N}_{k / \mathbb{Q}}\left(k^{\times}\right)$[15, Chapter 10]. A hermitian lattice is a pair $(\mathcal{L}, h)$, where $\mathcal{L}$ is a lattice in $V$ and $h$ a hermitian form. Hermitian lattices are then classified up to isomorphism by $\operatorname{cl}(\mathcal{L})$ and $\operatorname{det}(h)$.

We say that a hermitian lattice $(\mathcal{L}, h)$ is unimodular if
$$\mathcal{L}=\left\{x \in V: h(x, \mathcal{L}) \subset \mathcal{O}_{k}\right\} .$$
The lattice $h_{0}$ from §2.1 is unimodular with respect to the standard lattice $\mathcal{O}_{k}^{3}$ for that basis. More generally, if $I$ is a fractional ideal of $k$, we call $(\mathcal{L}, h)$ $I$-modular if
$$\mathcal{L}=\{x \in V: h(x, \mathcal{L}) \subset I\} .$$
If $V$ is odd-dimensional and $(\mathcal{L}, h)$ is unimodular, then $\mathcal{L}$ contains an odd vector, so given a reduced element $x \in \mathcal{L}$, there exists $y \in \mathcal{L}$ such that $h(x, y)=1$. This fact will be crucial in what follows.

\section*{3 Picard modular groups}

\subsection*{3.1 Arithmetic subgroups of $\operatorname{SU}(2,1)$}

Let $k$ be an imaginary quadratic field and $h$ a hermitian form on $k^{3}$ of signature $(2,1)$. If $\mathcal{G}_{h}$ is the $\mathbb{Q}$-algebraic group such that
$$\mathcal{G}_{h}(\mathbb{Q}) \cong\left\{A \in \mathrm{SL}_{3}(k):{ }^{t} \bar{A} h A=h\right\},$$
then $\mathcal{G}_{h}(\mathbb{R}) \cong \operatorname{SU}(2,1)$, i.e., $\mathcal{G}_{h}$ is a $\mathbb{Q}$-form of $\operatorname{SU}(2,1)$. Though there are two isomorphism classes of hermitian forms over $k$ with given signature and dimension, all the $\mathcal{G}_{h}$ over a fixed $k$ are $\mathbb{Q}$-isomorphic [12, §1.2].

The subgroup
$$\mathcal{G}_{h}(\mathbb{Z})=\left\{A \in \mathrm{SL}_{3}\left(\mathcal{O}_{k}\right):{ }^{t} \bar{A} h A=h\right\},$$
is a nonuniform lattice in $\operatorname{SU}(2,1)$. Its commensurability class depends only on $k$, and these lattices give all nonuniform arithmetic lattices in $\operatorname{SU}(2,1)$ up to commensurability. That is, commensurability classes of nonuniform arithmetic lattices are in one-to-one correspondence with imaginary quadratic fields. Any lattice commensurable with $\mathcal{G}_{h}(\mathbb{Z})$ is called a Picard modular group. Special amongst the Picard modular groups are the principal arithmetic lattices, which we now describe.

\subsection*{3.2 Principal arithmetic lattices}

Fix an imaginary quadratic field $k$ with integer ring $\mathcal{O}_{k}$, set
$$h_{0}=\left(\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right),$$
and let $\mathcal{G}$ be the associated $\mathbb{Q}$-form of $\operatorname{SU}(2,1)$. For any prime $p$ of $\mathbb{Q}$, consider the $\mathbb{Q}_{p}$-points $\mathcal{G}\left(\mathbb{Q}_{p}\right)$ of $\mathcal{G}$. If $p$ splits in $\mathcal{O}_{k}$, then $\mathcal{G}\left(\mathbb{Q}_{p}\right)$ is isomorphic to $\operatorname{SL}_{3}\left(\mathbb{Q}_{p}\right)$. When $p$ is inert or ramifies, let $k_{p}$ be the completion of $k$ at the prime ideal
of $\mathcal{O}_{k}$ above $p$. This is a quadratic extension of $\mathbb{Q}_{p}$, and $\mathcal{G}\left(\mathbb{Q}_{p}\right)$ is the unitary group of $h_{0}$ under this extension.

For each $p$, let $K_{p}$ be a compact open subgroup of $\mathcal{G}\left(\mathbb{Q}_{p}\right)$, and suppose that $K_{p}=\mathcal{G}\left(\mathbb{Z}_{p}\right)$ for all but finitely many $p$. (Note that this integral structure comes from our above choice of basis. The important point is that $\mathcal{G}\left(\mathbb{Z}_{p}\right)$ is hyperspecial for each $p$ [16, §3.5].) Then
$$K_{f}=\prod_{p} K_{p}<\mathcal{G}\left(\mathbb{A}_{f}\right)$$
is a compact open subgroup, where $\mathbb{A}_{f}$ is the finite adele ring of $\mathbb{Q}$, and $\Gamma_{K_{f}}=$ $K_{f} \cap \mathcal{G}(\mathbb{Q})$ defines a lattice in $\operatorname{SU}(2,1)$ commensurable with $\mathcal{G}(\mathbb{Z})$. In fact, $\mathcal{G}(\mathbb{Z})$ is amongst these lattices, where $K_{p}=\mathcal{G}\left(\mathbb{Z}_{p}\right)$ for all $p$. We will always denote the lattice $\mathcal{G}(\mathbb{Z})$, the standard Picard modular, by $\Gamma_{\text {std }}$.

The conjugacy classes of maximal compact open subgroups of $\mathcal{G}\left(\mathbb{Q}_{p}\right)$ are determined by the vertices of the local Dynkin diagram of $\mathcal{G}\left(\mathbb{Q}_{p}\right)$. The cases of interest to us are worked out in detail in the examples of [16]. However, a concrete set of maximal parahoric subgroups will be helpful in understanding our method of counting cusps, so we briefly recall the construction, via stabilizers of lattices in $k_{p}^{3}$, below.

\subsection*{3.3 Parahoric subgroups}

When $p$ splits in $\mathcal{O}_{k}$, representatives for the conjugacy classes of maximal compact open subgroups, i.e., the maximal parahoric subgroups, of $\mathcal{G}\left(\mathbb{Q}_{p}\right)$ are
$$\begin{gathered}
K_{p}^{v_{0}}=\operatorname{SL}_{3}\left(\mathbb{Z}_{p}\right) \\
K_{p}^{v_{1}}=\left\{\left(\begin{array}{ccc}
a_{11} & \frac{1}{p} a_{12} & \frac{1}{p} a_{13} \\
p a_{21} & a_{22} & a_{23} \\
p a_{31} & a_{32} & a_{33}
\end{array}\right) \in \operatorname{SL}_{3}\left(\mathbb{Q}_{p}\right): a_{j k} \in \mathbb{Z}_{p}\right\} \\
K_{p}^{v_{2}}=\left\{\left(\begin{array}{ccc}
a_{11} & a_{12} & \frac{1}{p} a_{13} \\
a_{21} & a_{22} & \frac{1}{p} a_{23} \\
p a_{31} & p a_{32} & a_{33}
\end{array}\right) \in \operatorname{SL}_{3}\left(\mathbb{Q}_{p}\right): a_{j k} \in \mathbb{Z}_{p}\right\} .
\end{gathered}$$
If $x_{1}, x_{2}, x_{3}$ is the corresponding basis for $\mathbb{Q}_{p}^{3}$, then $K_{p}^{v_{0}}$ is the stabilizer of the standard $\mathbb{Z}_{p}$-lattice,
$$\begin{aligned}
& K_{p}^{v_{1}}=\operatorname{stab}\left\{\frac{a}{p} x_{1}+b x_{2}+c x_{3}: a, b, c \in \mathbb{Z}_{p}\right\}, \\
& K_{p}^{v_{2}}=\operatorname{stab}\left\{\frac{a}{p} x_{1}+\frac{b}{p} x_{2}+c x_{3}: a, b, c \in \mathbb{Z}_{p}\right\} .
\end{aligned}$$
Equivalently, these are the stabilizers of three vertices, $v_{0}, v_{1}$, and $v_{2}$, of the corresponding Bruhat-Tits building. These vertices determine a chamber $t_{0}$ of the building, which is a triangle. Let $K_{p}^{0}$ be the associated Iwahori subgroup
$$K_{p}^{v_{0}} \cap K_{p}^{v_{1}} \cap K_{p}^{v_{2}},$$
that is, the group of elements which are upper-triangular modulo $p$.
If $p$ is inert or ramified, the building is a tree. Let $\mathcal{O}_{p}$ be the ring of integers of the quadratic extension $k_{p}$ of $\mathbb{Q}_{p}$ and $\pi$ a uniformizer for $\mathcal{O}_{p}$. Extend complex conjugation on $k / \mathbb{Q}$ to the nontrivial Galois involution of $k_{p} / \mathbb{Q}_{p}$.

There are two conjugacy classes of compact open subgroups,
$$K_{p}^{v_{0}}=\mathcal{G}\left(\mathbb{Z}_{p}\right)=\left\{A \in \mathrm{SL}_{3}\left(\mathcal{O}_{p}\right):{ }^{t} \bar{A} h_{0} A=h_{0}\right\},$$
the stabilizer in $\operatorname{SU}\left(h_{0}, k_{p}\right)$ of the standard $\mathcal{O}_{p}$-lattice, and
$$K_{p}^{v_{1}}=\left\{A=\left(\begin{array}{ccc}
a_{11} & \frac{1}{\pi} a_{12} & \frac{1}{\pi} a_{13} \\
\pi a_{21} & a_{22} & a_{23} \\
\pi a_{31} & a_{32} & a_{33}
\end{array}\right) \in \mathrm{SU}\left(h_{0}, k_{p}\right): a_{j k} \in \mathcal{O}_{p}\right\},$$
which is the stabilizer in $\operatorname{SU}\left(h_{0}, k_{p}\right)$ of the $\mathcal{O}_{p}$-lattice
$$\left\{\frac{a}{\pi} x_{1}+b x_{2}+c x_{3}: a, b, c \in \mathcal{O}_{p}\right\} .$$
The vertices $v_{0}$ and $v_{1}$ are adjoined by an edge $e_{0}$, which is a chamber of the building. Its stabilizer is the Iwahori subgroup
$$K_{p}^{0}=K_{p}^{v_{0}} \cap K_{p}^{v_{1}}=\left\{\left(\begin{array}{ccc}
a_{11} & a_{12} & a_{13} \\
\pi a_{21} & a_{22} & a_{23} \\
\pi a_{31} & a_{32} & a_{33}
\end{array}\right) \in \mathrm{SU}\left(h_{0}, \mathcal{O}_{p}\right)\right\} .$$
In fact, one can show that preserving $h_{0}$ also forces the (3, 2)-coordinate to be divisible by $\pi$, so $K_{p}^{0}$ is upper triangular modulo $\pi$.

Remark. When 2 ramifies in $\mathcal{O}_{k}$, a slight modification is required at the prime above 2. See [16].

\subsection*{3.4 Maximal lattices}

Since $\mathcal{G}$ is a $\mathbb{Q}$-form of $\operatorname{SU}(2,1)$, it has Strong Approximation. Therefore, for any $K_{f}$ as above, there exists $g \in \mathcal{G}(\mathbb{Q})$ so that each factor of $g K_{f} g^{-1}$ is contained in one of the $K_{p}^{v_{j}}$ of §3.3. Furthermore, the action of $\mathcal{G}\left(\mathbb{Q}_{p}\right)$ on the Bruhat-Tits building at $p$ is special [16, §3.2], from which it follows that if $\Gamma<\mathcal{G}(\mathbb{Q})$ is a maximal lattice, then $\Gamma=\Gamma_{K_{f}}$ for some compact open subgroup of $\mathcal{G}\left(\mathbb{A}_{f}\right)$, and each factor of $K_{f}$ stabilizes a vertex of the building. Therefore, we can, and do, assume that any $\Gamma_{K_{f}}<\mathcal{G}(\mathbb{Q})$ is such that each factor is contained in one of the groups $K_{p}^{v_{j}}$.

However, the $\Gamma_{K_{f}}$ which are maximal in $\mathcal{G}(\mathbb{Q})$ do not necessarily determine the maximal lattices in $\mathcal{G}(\mathbb{R}) \cong \operatorname{SU}(2,1)$. Let $\overline{\mathcal{G}}$ be the corresponding $\mathbb{Q}$-form of $\operatorname{PU}(2,1)$. Then every maximal arithmetic lattice in $\operatorname{PU}(2,1)$ defined by a hermitian form on $k^{3}$ is contained in $\overline{\mathcal{G}}(\mathbb{Q})$ (see [11, Proposition 4.2]), but the projection from $\mathcal{G}(\mathbb{Q})$ to $\overline{\mathcal{G}}(\mathbb{Q})$ is not necessarily surjective. One can describe this phenomenon explicitly via lifts to the general unitary group. The lift $g$
of some element of $\overline{\mathcal{G}}(\mathbb{Q})$ to $\operatorname{GU}(2,1)$ will have a special unitary representative lying in $\mathcal{G}(\mathbb{Q})$ if and only if $\operatorname{det}(g)$ is a cube in $k$.

However, each maximal lattice in $\operatorname{SU}(2,1)$ in our commensurability class is the normalizer in $\mathcal{G}(\overline{\mathbb{Q}})$ of some $\Gamma_{K_{f}}$ [2, Proposition 1.4]. We may also assume that each factor of $K_{f}$ is either one of the vertex stabilizers $K_{p}^{v_{j}}$, or is an Iwahori subgroup $K_{p}^{0}$. Even further, when $p$ is inert or ramified, every element of $\mathcal{G}\left(\overline{\mathbb{Q}}_{p}\right)$ acts by special automorphisms, so we may assume that $K_{f}$ is Iwahori only at split primes (see [12, §2.2]).

Let $\bar{\Gamma}<\mathcal{G}(\overline{\mathbb{Q}})$ be a maximal lattice, normalizing the lattice $\Gamma_{K_{f}}$. Let $I$ be the set of (split) primes for which $K_{f}$ is Iwahori at $p$, so $K_{f}$ is one of the groups $K_{p}^{v_{j}}$ for all other $p$. Then, we have the following upper bound for $\left[\bar{\Gamma}: \Gamma_{K_{f}}\right]$, which will be of use several times throughout this paper.

Proposition 3.1 (See [2, 12]). Let $\bar{\Gamma}$ and $\Gamma_{K_{f}}$ be as above. Then
$$\left[\bar{\Gamma}: \Gamma_{K_{f}}\right] \leq 3^{1+|I|} h_{k, 3},$$
where $h_{k, 3}$ is the order of the 3-primary part of the class group of the field $k$ from which the algebraic group $\mathcal{G}$ is defined.

Sketch. Since the ideas behind the proof are relevant later, we give a sketch. If $k \neq \mathbb{Q}(\sqrt{-3})$, then the center of $\operatorname{SU}(2,1)$ is not contained in $\Gamma$, since the center is $\zeta_{3} \mathrm{Id}$, where $\zeta_{3}$ is a primitive $3^{r d}$ root of unity. When $k=\mathbb{Q}(\sqrt{-3}), \Gamma_{K_{f}}$ is normalized in $\mathrm{U}(2,1)$ by an element conjugate to
$$\left(\begin{array}{ccc}
1 & 0 & 0 \\
0 & \zeta_{3} & 0 \\
0 & 0 & 1
\end{array}\right) .$$
While this element has a unitary representative with entries in $\mathbb{Q}(\sqrt{-3})$, a special unitary representative has entries in $\mathbb{Q}\left(\sqrt[3]{\zeta_{3}}\right)$. This accounts for the first factor of 3.

For any prime $p$ at which $K_{f}$ is Iwahori, there is an order 3 element of $\operatorname{PGL}_{3}\left(\mathbb{Q}_{p}\right)$ which permutes the three lattices defining a chamber of the building. In other words, a conjugate acts on the Bruhat-Tits building by an order three automorphism of the triangle with vertices $v_{0}, v_{1}, v_{2}$. If such an element preserves $h$, then it normalizes $\Gamma_{K_{f}}$ but also does not have a special unitary representative with entries in $k$, hence the factor of $3^{|I|}$.

Since the image of $\bar{\Gamma}$ in $\operatorname{PU}(2,1)$ is in $\overline{\mathcal{G}}(\mathbb{Q})$, let $g$ be a representative for $g_{0} \in \bar{\Gamma}$ in the general unitary group with entries in $k$. Then
$${ }^{t} \bar{g} h g=\alpha h$$
for some $\alpha \in \mathbb{Q}^{\times}$, from which it follows that $|\operatorname{det}(g)|^{2}=\alpha^{3}$. This lift is well-defined up to an element of $\left(k^{\times}\right)^{3}$, so we have a map
$$\bar{\Gamma} / \Gamma_{K_{f}} \rightarrow \operatorname{ker}\left(\mathrm{~N}_{k / \mathbb{Q}}: k^{\times} /\left(k^{\times}\right)^{3} \rightarrow \mathbb{Q}^{\times} /\left(\mathbb{Q}^{\times}\right)^{3}\right) .$$

There is a natural identification of this kernel with order three elements of the class group of $k$. Choose a non-unit element $x$ representing a nontrivial class in $k^{\times} /\left(k^{\times}\right)^{3}$ for which $\mathrm{N}_{k / \mathbb{Q}}(x)=y^{3} \in \mathbb{Q}^{\times}$. Then, the principal ideal $(x)$ decomposes as a product of prime ideals $\mathfrak{P}_{1}^{\alpha_{1}} \cdots \mathfrak{P}_{r}^{\alpha_{r}}$, and
$$\prod_{j=1}^{r} \mathfrak{P}_{j}^{\alpha_{j}} \overline{\mathfrak{P}}_{j}^{\alpha_{j}}=(x)(\bar{x})=(y)^{3}=\left(p_{1}\right)^{3 \beta_{1}} \cdots\left(p_{r}\right)^{3 \beta_{r}},$$
where $y=p_{1}^{\beta_{1}} \cdots p_{r}^{\beta_{r}}$ as a product of rational primes.
Since $p_{j}=\mathrm{N}_{k / \mathbb{Q}}\left(\mathfrak{P}_{j}\right)$ for $p_{j}$ split or ramified, $\alpha_{j}=3 \beta_{j}$ for those $j$. If $p_{j}$ is inert, then $\left(p_{j}\right)=\mathfrak{P}_{j}$, so $2 \alpha_{j}=3 \beta_{j}$, so $\alpha_{j}$ is still divisible by 3 . This implies that $(x)$ is a product of $3^{r d}$ powers of ideals,
$$(x)=\mathfrak{I}_{1}^{3} \cdots \mathfrak{I}_{r}^{3}=\left(\mathfrak{I}_{1} \cdots \mathfrak{I}_{r}\right)^{3} .$$
Since $x$ is not a cube, $\mathfrak{I}_{x}=\mathfrak{I}_{1} \cdots \mathfrak{I}_{r}$ is not a principal ideal. Therefore $\mathfrak{I}_{x}$ represents an element of the class group of $k$ with order dividing 3. That is, the class of $\mathfrak{I}_{x}$ lies in the 3-primary component of the ideal class group. \(\square\)

\section*{4 Cusps of Picard modular groups}

\subsection*{4.1 Cusps of standard Picard modular groups}

The first step in counting cusps of Picard modular groups is to describe the cusp set (see §2.1). The notation of §3 is used throughout this section. Let $\bar{\Gamma}<\mathcal{G}(\overline{\mathbb{Q}})$ be a maximal lattice which normalizes $\Gamma_{K_{f}}$ as in §3.4. Since $\operatorname{SU}(2,1) \rightarrow \operatorname{PU}(2,1)$ is central, and since the center of $\operatorname{SU}(2,1)$ acts trivially on $\mathbf{H}_{\mathbb{C}}^{2} \cup \partial_{\infty} \mathbf{H}_{\mathbb{C}}^{2}$, there is no issue with considering lattices in $\operatorname{SU}(2,1)$, as opposed to their image in PU(2, 1). The following lemma is known, cf. 3 and [11, §4.7].
Lemma 4.1. The cusp set of $\bar{\Gamma}$ is independent of its commensurability class and equals $\mathbb{P}^{2}(k) \cap \partial_{\infty} \mathbf{H}_{\mathbb{C}}^{2}$, i.e., the set of $h_{0}$-isotropic lines in $k^{3}$.

Therefore, to count the number of cusps of $\bar{\Gamma}$, we will to count the $\bar{\Gamma}$ -equivalence classes of $h_{0}$-isotropic lines in $k^{3}$. To each $h_{0}$-isotropic line $\ell$ there corresponds an ideal class of $k$ as follows. For any $x \in \ell$, consider the fractional ideal
$$I_{x}=\left\{\alpha \in k: \alpha x \in \mathcal{O}_{k}^{3}\right\} .$$
The ideal class of $I_{x}$ depends only on $\ell$. Call this ideal class $\operatorname{cl}(\ell)$.
If $\ell$ and $\ell^{\prime}$ are $\gamma$-equivalent for some $\gamma$ in the standard Picard modular group for $h_{0}, \Gamma_{\text {std }}$, then $\operatorname{cl}(\ell)=\operatorname{cl}\left(\ell^{\prime}\right)$, since $\gamma$ preserves $\mathcal{L}_{0}=\mathcal{O}_{k}^{3}$ and has determinant one. There is also a converse, due to Zink [18]. We sketch the proof, highlighting the ideas used later in this paper. The key fact, which is the reason for our specification of $h_{0}$ and $\mathcal{L}_{0}$, is that $\mathcal{L}_{0}$ is unimodular for $h_{0}$.

Theorem 4.2 ([18]). Let $\ell$ and $\ell^{\prime}$ be $h_{0}$-isotropic lines in $k^{3}$. Then $\ell$ and $\ell^{\prime}$ are $\Gamma_{\text {std }}$-equivalent if and only if $\operatorname{cl}(\ell)=\operatorname{cl}\left(\ell^{\prime}\right)$. Given any ideal class $c$ of $k$, there exists an $h_{0}$-isotropic line $\ell$ with $\operatorname{cl}(\ell)=c$.

Proof. Let $\phi: \ell \rightarrow \ell^{\prime}$ be an abstract $\mathcal{O}_{k}$-module isomorphism taking $\ell \cap \mathcal{L}_{0}$ to $\ell^{\prime} \cap \mathcal{L}_{0}$. Zink proves that there exists an $h_{0}$-preserving automorphism $\gamma: \mathcal{L}_{0} \rightarrow$ $\mathcal{L}_{0}$ which restricts to $\phi$ as follows.

There exist isotropic vectors $x \in \ell \cap \mathcal{L}_{0}$ and $y \in \mathcal{L}_{0}$ such that $h_{0}(x, y)=$ 1 , by unimodularity (and since $k^{3}$ has odd dimension). Then, we can find a decomposition of $\mathcal{L}_{0}$ as an $\mathcal{O}_{k}$-module
$$I_{\ell} x \oplus I_{1} y \oplus I_{2} z,$$
where $I_{\ell}, I_{1}$, and $I_{2}$ are fractional ideals and
$$\begin{gathered}
h_{0}(x, z)=h_{0}(y, z)=0, \\
h_{0}(z, z) \neq 0 .
\end{gathered}$$
Note that $\operatorname{cl}\left(I_{\ell}\right)=\operatorname{cl}(\ell)$ and $I_{1} \cong \operatorname{Hom}_{\mathcal{O}_{k}}\left(\bar{\ell}, \mathcal{O}_{k}\right)$, where $\bar{\ell}$ denotes $\ell$ with the complex conjugate $\mathcal{O}_{k}$-module structure.

There is a similar decomposition with respect to $\ell^{\prime}$ with generators $x^{\prime}, y^{\prime}$, and $z^{\prime}$. This defines an element $\gamma$ of $\Gamma_{\text {std }}$ which takes $\ell$ to $\ell^{\prime}$ by
$$\gamma(x)=x^{\prime}, \gamma(y)=y^{\prime}, \gamma(z)=z^{\prime} .$$
This preserves $h_{0}$ by construction, so $\gamma \in \Gamma_{\text {std }}$. (Note that $\gamma$ might not have determinant one, but after changing our choice of basis by a unit of $\mathcal{O}_{k}$, the determinant is one.)

To construct an isotropic line with given ideal class $c$, let $\mathfrak{c}$ be a fractional ideal representing $c$ and $\mathfrak{c}^{\prime}=\operatorname{Hom}_{\mathcal{O}_{k}}\left(\overline{\mathfrak{c}}, \mathcal{O}_{k}\right)$. Then the abstract rank two $\mathcal{O}_{k}$ -module $\mathfrak{c} \oplus \mathfrak{c}^{\prime}$ is unimodular for the hermitian form $H$ defined by
$$H(\mathfrak{c}, \mathfrak{c})=H\left(\mathfrak{c}^{\prime}, \mathfrak{c}^{\prime}\right)=0, \quad H\left(x, x^{\prime}\right)=x^{\prime}(x), \quad x \in \mathfrak{c}, x^{\prime} \in \mathfrak{c}^{\prime} .$$
Set $\mathfrak{d}=\mathfrak{c}^{-2}$ and extend $H$ to the rank three $\mathcal{O}_{k}$-module $\mathcal{L}=\mathfrak{c} \oplus \mathfrak{c}^{\prime} \oplus \mathfrak{d}$ by
$$\begin{gathered}
H(x, y)=\frac{x \bar{y}}{\mathrm{~N}(\mathfrak{c})^{2}}, x, y \in \mathfrak{d} \\
H(\mathfrak{c}, \mathfrak{d})=H\left(\mathfrak{c}^{\prime}, \mathfrak{d}\right)=0
\end{gathered}$$

Then $\mathcal{L}$ is an odd unimodular lattice of rank three with respect to $H$, which has signature (2, 1). It has the same class as $\mathcal{L}_{0}$ by construction, so it is isomorphic to $\mathcal{L}_{0}$ equipped with $h_{0}$. The line generated by the image of $\mathfrak{c}$ in $k^{3}$ is an isotropic line with ideal class $c$. \(\square\)

Corollary 4.3 ([18, 17]). The standard Picard modular group $\Gamma_{\text {std }}$ has $h_{k}$ cusps, where $h_{k}$ is the class number of $k=\mathbb{Q}(\sqrt{-d})$. More generally, if $\mathcal{L}$ is a lattice in $k^{3}$ which is unimodular with respect to some hermitian form $h$, then the lattice $\operatorname{Aut}(\mathcal{L}, h)$ in $\operatorname{SU}(2,1)$ has $h_{k}$ cusps.

The remainder of this section generalizes Zink's ideas and the general approach of [3] to count the number of cusps for $\bar{\Gamma}$ and some of its congruence subgroups. First, we consider cusps of a suitable generalization of the Hecke congruence subgroup $\Gamma_{0}(N)$. This count is then used to count cusps of the maximal lattice.

\subsection*{4.2 Cusps of congruence subgroups}

We now define the subgroups $\Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$ of $\Gamma_{\text {std }}$ that generalize Hecke's subgroups $\Gamma_{0}(N)$ of the modular group. Let $\mathcal{P}_{1}$ and $\mathcal{P}_{2}$ be disjoint finite sets of rational primes which split in $\mathcal{O}_{k}$, and $\mathcal{B}$ a third disjoint finite set of primes. Then $\Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$ is the subgroup of those $\gamma \in \Gamma_{\text {std }}$ for which the reduction of $\gamma$ modulo $p$ has the form
$$\begin{array}{ll}
\left(\begin{array}{ccc}
* & * & * \\
* & * & * \\
0 & 0 & *
\end{array}\right) & p \in \mathcal{P}_{1} \\
\left(\begin{array}{c}
* \\
0 \\
0
\end{array}-\frac{*}{*}\binom{*}{*}\right. & p \in \mathcal{P}_{2}
\end{array}$$
and is upper triangular modulo $p$ for all $p \in \mathcal{B}$.
Note that $\mathcal{P}_{1}$ and $\mathcal{P}_{2}$ determine the two parabolic subgroups of $\operatorname{SL}_{3}\left(\mathbb{F}_{p}\right)$ containing the Borel subgroup of upper triangular matrices. The groups $\operatorname{SU}\left(3, \mathbb{F}_{p}^{2}\right)$ and $\operatorname{SO}\left(3, \mathbb{F}_{p}\right)$ have no proper parabolic subgroups which properly contain a Borel subgroup, which is why all the primes in $\mathcal{P}_{1}$ and $\mathcal{P}_{2}$ are split. Write $\mathcal{B}=\mathcal{B}^{s} \cup \mathcal{B}^{i} \cup \mathcal{B}^{r}$ as a disjoint union of its split, inert, and ramified primes, respectively.

Proposition 4.4. The space $\mathbf{H}_{\mathbb{C}}^{2} / \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$ has
$$2^{\left|\mathcal{P}_{1}\right|+\left|\mathcal{P}_{2}\right|+\left|\mathcal{B}^{i}\right|+\left|\mathcal{B}^{r}\right|} 3^{\left|\mathcal{B}^{s}\right|} h_{k}$$
cusps.
Proof. By Strong Approximation for $\Gamma_{\text {std }}$, it suffices to consider one prime $p$. Since the reduction of $\Gamma_{\text {std }}$ modulo $p$ maps onto the corresponding $\mathbb{F}_{p}$-group [16, §3.5], it suffices to count $\Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$-orbits of isotropic lines modulo $p$. Each algebraic group $\mathcal{G}\left(\mathbb{F}_{p}\right)$ over $\mathbb{F}_{p}, \operatorname{SL}_{3}\left(\mathbb{F}_{p}\right), \operatorname{SU}\left(3, \mathbb{F}_{p}^{2}\right)$, or $\operatorname{SO}\left(3, \mathbb{F}_{p}\right)$, acts transitively on the isotropic lines modulo $p$.

For the primes in $\mathcal{P}_{1}, \mathcal{P}_{2}$, or a nonsplit prime of $\mathcal{B}$, there are two orbits of isotropic lines modulo $p$ under the corresponding reduction modulo $p$. In each case, the two orbits are represented by (1, 0, 0) and (0, 0, 1). For the split primes in $\mathcal{B}$, there are three.

For each orbit of isotropic lines modulo $p$ and each element $c$ of the class group of $k$, it remains to show that there is an isotropic line in $k^{3}$ with ideal class $c$ and whose reduction modulo $p$ lands the specified orbit. Let $\ell^{\prime}$ be any isotropic line with $\operatorname{cl}\left(\ell^{\prime}\right)=c$ and let $\bar{\ell}^{\prime}$ be the reduction of $\ell \cap \mathcal{L}_{0}$ modulo $p$. Then there exists $\bar{\gamma} \in \mathcal{G}\left(\mathbb{F}_{p}\right)$ so that $\bar{\gamma}\left(\bar{\ell}^{\prime}\right)=\bar{\ell}$. Since the reduction is surjective, there exists $\gamma \in \Gamma_{\text {std }}$ whose reduction is $\bar{\gamma}$. Then $\ell=\gamma\left(\ell^{\prime}\right)$ has reduction modulo $p$ equal to $\bar{\ell}$. This completes the proof. \(\square\)

The following lemma will allow us to apply Proposition 4.4 to study a general maximal lattice.

Lemma 4.5. Let $\bar{\Gamma}<\mathcal{G}(\mathbb{R})$ be a maximal lattice commensurable with the standard Picard modular group $\Gamma_{\text {std }}$. Then, we can conjugate $\bar{\Gamma}$ so that $\bar{\Gamma} \cap \Gamma_{\text {std }}$ is of the form $\Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$.

Proof. Suppose that $\bar{\Gamma}$ normalizes the principal arithmetic lattice $\Gamma_{K_{f}}=\bar{\Gamma} \cap$ $\mathcal{G}(\mathbb{Q})$. We can assume after a conjugation that $K_{f}$ is contained in a product of the $K_{p}^{v_{j}}$ as above, so
$$\bar{\Gamma} \cap \Gamma_{\text {std }}=\bar{\Gamma} \cap \mathcal{G}(\mathbb{Q}) \cap \Gamma_{\text {std }}=\Gamma_{K_{f}} \cap \Gamma .$$
The lemma follows from the description of each $K_{p}^{v_{j}}$ given in §3.3 \(\square\)

\subsection*{4.3 Proof of the main result}

Let $\bar{\Gamma}<\mathrm{SU}(2,1)$ be a maximal arithmetic lattice, $k$ be the number field from which it is defined, and $\Gamma_{K_{f}}<\mathcal{G}(\mathbb{Q})$ the principal arithmetic lattice that it normalizes, where $\mathcal{G}$ is the $\mathbb{Q}$-form of $\operatorname{SU}(2,1)$ determined by $k$ and the hermitian form
$$h_{0}=\left(\begin{array}{ccc}
0 & 0 & 1 \\
0 & -1 & 0 \\
1 & 0 & 0
\end{array}\right) .$$
Conjugate so that the $p$-component of $K_{f}$ equals $K_{p}^{v_{j}}$ or the Iwahori subgroup $K_{p}^{0}$ for every $p$, and is only equal to $K_{p}^{0}$ for some finite set of rational primes which split in $\mathcal{O}_{k}$.

Let $I$ be the set of primes for which the $p$-component of $K_{f}$ is $K_{p}^{0}$. Let $\Xi_{K_{f}}$ be, as in [2] (their notation is $\Xi_{\Theta}$ ), the set of $p$ in $I$ such that $\bar{\Gamma}$ contains an element $c_{p}$ which acts nontrivially on the chamber of the Bruhat-Tits building at $p$ corresponding to the Iwahori subgroup $K_{p}^{0}$. Then $c_{p}$ normalizes $K_{p}^{0}$, and its image in $\operatorname{PGL}_{3}\left(\mathbb{Q}_{p}\right)$ has order 3.

Finally, let $\Gamma_{\text {std }}$ be the standard Picard modular group, $\mathcal{G}(\mathbb{Z})$ for $h_{0}$, and $\bar{\Gamma}_{\text {std }}$ its normalizer in $\mathcal{G}(\overline{\mathbb{Q}})$. Now, we prove some auxiliary results necessary for the proof of Theorem 1.1.

Proposition 4.6. If $\Gamma_{\text {std }}$ is the standard Picard modular group for $h_{0}$ as above, then $\left[\bar{\Gamma}_{\text {std }}: \Gamma_{s t d}\right]=3 h_{k, 3}$.

Proof. One can prove this directly via Galois cohomology and Strong Approximation, as in [8] or [2], but we give an elementary (though morally equivalent) argument. By Proposition 3.1,
$$\left[\bar{\Gamma}_{\text {std }}: \Gamma_{\text {std }}\right] \leq 3 h_{k, 3},$$
so it suffices to prove the opposite inequality. The element of determinant $\zeta_{3}$ from the proof of Proposition 3.1 generates the factor of 3 when $k=\mathbb{Q}(\sqrt{-3})$, and completes the proof in that case. The center of $\operatorname{SU}(2,1)$, thus of $\bar{\Gamma}$ is cyclic of order 3, generated by the scalar matrix $\zeta_{3} \mathrm{Id}$. When $k \neq \mathbb{Q}(\sqrt{-3})$, this subgroup is not in $\Gamma$, so it generates a three-fold extension. This completes the proof when
$h_{k, 3}=1$. Now, we need to exhibit an element $g \in G(\overline{\mathbb{Q}})$ that normalizes $\Gamma$ for each order three element of the class group of $k$.

Let $J \subset \mathcal{O}_{k}$ be a non-principal ideal such that $J^{3}$ is principal. If $\left\{e_{1}, e_{2}, e_{3}\right\}$ are the standard basis vectors for $k^{3}$, then
$$\mathcal{L}_{0}=\mathcal{O}_{k}^{3}=\mathcal{O}_{k} e_{1} \oplus \mathcal{O}_{k} e_{2} \oplus \mathcal{O}_{k} e_{3} .$$
Set
$$\mathcal{L}_{1}=J e_{1} \oplus J e_{2} \oplus J e_{3} \subset \mathcal{L}_{0} .$$
Then $\mathcal{L}_{1}$ is $(n)$-modular for $h$, where $(n)=J \bar{J}$. Since $J^{3}$ is principal, $\operatorname{cl}\left(\mathcal{L}_{1}\right)=$ $\operatorname{cl}\left(\mathcal{L}_{0}\right)$, so we can find a decomposition of $\mathcal{L}_{1}$, akin to that of Theorem 4.2 as
$$\mathcal{O}_{k} e_{1}^{\prime} \oplus \mathcal{O}_{k} e_{2}^{\prime} \oplus \mathcal{O}_{k} e_{3}^{\prime},$$
where $h\left(e_{j_{1}}^{\prime}, e_{j_{2}}^{\prime}\right)=0$ or $\pm n$. This means that there is an isomorphism $g$ from $\mathcal{L}_{0}$ to $\mathcal{L}_{1}$, sending $e_{j}$ to $e_{j}^{\prime}$. The linear extension of $g$ to $k^{3}$ then, by definition, lies in the general unitary group of $h$ and scales $h$ by $n$.

We claim that $g$ normalizes $\Gamma_{\text {std }}$. Indeed, since $J$ is an ideal of $\mathcal{O}_{k}$, it follows that any $\gamma \in \Gamma$ fixes $\mathcal{L}_{1}$, so $g^{-1} \gamma g$ is an automorphism of $\mathcal{L}_{0}$ of determinant one. Since $g$ is in the general unitary group, $g^{-1} \gamma g$ is still in the special unitary group. In particular, $g^{-1} \gamma g \in \Gamma_{\text {std }}$.

Finally, let $g_{I}$ and $g_{J}$ be two elements as above, constructed with respect to the ideals $I$ and $J$, where each represents distinct three-torsion in the class group. Then the cosets $g_{I} \Gamma_{\text {std }}, g_{J} \Gamma_{\text {std }} \subset \bar{\Gamma}_{\text {std }}$ are disjoint. Indeed, $g_{I}$ and $g_{J}$ will scale $h$ by different factors, even up to multiplication by scalar matrices (which multiply determinants by a cube of $k$ ), so their cosets must be distinct. This proves that $\left[\bar{\Gamma}_{\text {std }}: \Gamma_{\text {std }}\right] \geq 3 h_{k, 3}$ and completes the proof of the proposition. \(\square\)

Corollary 4.7. Let $\Gamma_{\text {std }}$ be the standard Picard modular group for $h$ as above, $\bar{\Gamma}_{\text {std }}$ its normalizer, and $g \in \bar{\Gamma}_{\text {std }}$ one of the elements constructed in Proposition 4.6. built with respect to the ideal $J$ of $\mathcal{O}_{k}$. Then $g$ acts on the cusps of $\Gamma$ by
$$\operatorname{cl}(\ell) \stackrel{g}{\mapsto} \operatorname{cl}(J)^{-1} \operatorname{cll}(\ell) .$$
In particular, $\operatorname{cl}(g(\ell)) \neq \operatorname{cl}(\ell)$ for any isotropic line $\ell \subset k^{3}$.
Proof. Recall that $\operatorname{cl}(\ell)$ is computed with respect to $\mathcal{L}_{0}$, not $\mathcal{L}_{1}=g\left(\mathcal{L}_{0}\right)$. Let $\ell$ be an isotropic line, $x \in \ell$, and $I_{x}$ the fractional ideal of $k$ associated to $\ell$, so $\operatorname{cl}(\ell)=\operatorname{cl}\left(I_{x}\right)$. Consider the ideal $I_{g(x)}$, the set of $\lambda \in k$ for which $\lambda g(x) \in \mathcal{L}_{0}$. If $\lambda g(x) \in \mathcal{L}_{0}$, then $j \lambda g(x) \in \mathcal{L}_{1}$ for all $j \in J$, so
$$j \lambda x \in g^{-1}\left(\mathcal{L}_{1}\right)=\mathcal{L}_{0} .$$
That is, $j \lambda \in I_{x}$ for all $j \in J$, so $J I_{g(x)} \subseteq I_{x}$.
Now, consider $J^{-1} I_{x}$. Since
$$J^{-1}=\operatorname{Hom}_{\mathcal{O}_{k}}\left(J, \mathcal{O}_{k}\right),$$
if $j^{-1} \mu \in J^{-1} I_{x}$,
$$j^{-1} \mu g(x)=j^{-1} g(\mu x),$$
and $\mu x \in \mathcal{L}_{0}$ by definition, so $g(\mu x) \in \mathcal{L}_{1}$. Write
$$g(\mu x)=j_{1} e_{1}+j_{2} e_{2}+j_{3} e_{3},$$
with $j_{\alpha} \in J, \alpha=1,2,3$. Then $j^{-1}\left(j_{\alpha}\right) \in \mathcal{O}_{k}$ for all $\alpha=1,2,3$, so $j^{-1} \mu \in I_{g(x)}$. Thus, $J^{-1} I_{x} \subseteq I_{g(x)}$, i.e., $I_{x} \subseteq J I_{g(x)}$, so the two ideals are equal. This implies that $\operatorname{cl}(g(\ell))=\operatorname{cl}(J)^{-1} \operatorname{cl}(\ell)$, as desired. \(\square\)

Now we are ready to state and prove the main technical result of this paper.
Theorem 4.8. Let $\bar{\Gamma}<\mathrm{SU}(2,1)$ be a maximal arithmetic lattice, and $\Gamma_{K_{f}}$ the principal arithmetic lattice that it normalizes. Let $I$ be the set of (necessarily split) rational primes for which the $p$-component of $K_{f}$ is an Iwahori subgroup, and $m_{K_{f}}=\left|I \backslash \Xi_{K_{f}}\right|$. Then $\mathbf{H}_{\mathbb{C}}^{2} / \bar{\Gamma}$ has
$$3^{m_{K_{f}}} \frac{h_{k}}{h_{k, 3}}$$
cusps.
Proof. Let $\Gamma_{\text {std }}$ be the standard Picard modular group for $h_{0}$ as above (so Theorem 4.2 applies) and $\bar{\Gamma}_{\text {std }}$ its normalizer. Consider the diagram of subgroups in Figure 1, from which we will prove the theorem two stages.

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/ecb3b05c-bbcd-4a97-9c61-613bdc1eb089-14.jpg?height=326&width=521&top_left_y=1474&top_left_x=799}
\captionsetup{labelformat=empty}
\caption{Figure 1: The intersection of $\bar{\Gamma}$ and $\bar{\Gamma}_{\text {std }}$.}
\end{figure}

First, assume $k \neq \mathbb{Q}(\sqrt{-3})$. We will deal with $\mathbb{Q}(\sqrt{-3})$ at the end of the proof. Then $\bar{\Gamma} \cap \Gamma_{\text {std }}=\Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$ has $2^{m_{1}} 3^{m_{2}} h_{k}$ cusps by Lemma 4.4 where $m_{1}$ and $m_{2}$ are explicitly determined by $K_{f}$. We claim that if $\ell$ is an isotropic line and $g \in \bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$ is such that $\operatorname{cl}(\ell)=\operatorname{cl}(g(\ell))$, then either $g \in \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$ or $g$ is in the center of $\operatorname{SU}(2,1)$, which is cyclic of order three and acts trivially on all cusps. Equivalently, $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$ has
$$\frac{2^{m_{1}} 3^{m_{2}} h_{k}}{\frac{1}{3}\left[\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}: \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)\right]}$$
cusps.
If $g$ is in the center, $\zeta_{3} \notin \mathbb{Q}(\sqrt{-d})$ since $d \neq 3$, so $g \notin \Gamma$. That the center acts trivially on isotropic lines is evident. Now, suppose $g$ is not central and that $\operatorname{cl}(\ell)=\operatorname{cl}(g(\ell))$ for $g \in \bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$. We must show that $g \in \Gamma_{\text {std }}$, which is precisely the content of Corollary 4.7.

Now, consider $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}<\bar{\Gamma}$. First, this contains elements $c_{p}=c$ for $p \in I$, where $I$ is the set of (split) primes for which the $p$-component of $K_{f}$ is $K_{p}^{0}$. These elements generate the extension $\bar{\Gamma} / \Gamma_{K_{f}}$, and $\bar{\Gamma} / \Gamma_{K_{f}}$ is an elementary abelian 3-group. Every such element identifies the three equivalence classes of cusps (for each ideal class) corresponding to the fact that the reduction modulo $p$ of $\Gamma_{K_{f}} \cap \Gamma_{\text {std }}$ is the Borel subgroup of $\operatorname{SL}_{3}\left(\mathbb{F}_{p}\right)$. There are, by definition, $\Xi_{K_{f}}$ such elements.

Also, for each $p \notin I$ such that $K_{p}$ is not $G\left(\mathbb{Z}_{p}\right)=K_{p}^{v_{0}}, \Gamma_{K_{f}}$ contains an element which identifies the two classes of isotropic lines modulo $p$ which are not identified by $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$. One can see this explicitly via Strong Approximation and the reduction modulo $p$ of $\Gamma_{K_{f}}$ as described in [16, §3.11]. This shows that $\bar{\Gamma}$ has
$$\frac{3^{\left|I \backslash \Xi_{K_{f}}\right|} h_{k}}{\frac{1}{3}\left[\bar{\Gamma} \cap \bar{\Gamma}_{\mathrm{std}}: \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)\right]}$$
cusps. It remains to show that this equals the expression in the statement of the theorem.

To show that $\left[\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}: \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)\right]=3 h_{k, 3}$, it suffices by Proposition 4.6 to show that
$$\left[\bar{\Gamma}_{\text {std }}: \bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}\right]=\left[\Gamma_{\text {std }}: \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)\right] .$$
These intersections are exactly determined by reductions modulo $p$, where the reduction of $\bar{\Gamma}_{\text {std }}$ modulo $p$ is a subgroup of the general linear, unitary, or orthogonal group modulo $p$, depending on the decomposition of $p$ in $\mathcal{O}_{k}$. This is well-defined by realizing of each element of $\bar{\Gamma}_{\text {std }}$ as an element of the general unitary group of $h$ with entries in $\mathcal{O}_{k}$.

Then, the reduction of $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$ modulo $p$ is the appropriate parabolic or Borel subgroup of the general linear, unitary, or orthogonal group. In each case, the Borel subgroup, and thus each parabolic subgroup, contains the center. This implies that the index of the parabolic subgroup in the full $\mathbb{F}_{p}$ group is equal to the corresponding index for the reduction modulo $p$ of $\Gamma_{\text {std }}$. This means precisely that $\left[\bar{\Gamma}_{\text {std }}: \bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}\right]$ equals $\left[\Gamma_{\text {std }}: \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)\right]$, as required. This proves the theorem for $d \neq 3$.

Now, consider the case $k=\mathbb{Q}(\sqrt{-3})$. The group $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$ is generated over $\Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)$ by a special unitary representative of the element of determinant $\zeta_{3}$ from the proof of Proposition 4.6, which acts trivially on cusps. This proves that $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$ has
$$\frac{2^{m_{1}} 3^{m_{2}} h_{k}}{\frac{1}{3}\left[\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}: \Gamma\left(\mathcal{P}_{1}, \mathcal{P}_{2}, \mathcal{B}\right)\right]}$$
cusps, as in the other cases. The proof going from $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$ to $\bar{\Gamma}$ is exactly the same as above. \(\square\)

\subsection*{4.4 Commensurability classes containing $N$-cusped elements}

Theorem 4.9. For any natural number $N$, there only exist finitely many commensurability classes of arithmetic complex hyperbolic 2-orbifolds containing an orbifold with at most $N$ cusps.

Proof. It suffices to prove that
$$\frac{h_{k}}{h_{k, 3}} \rightarrow \infty$$
as $d \rightarrow \infty$, where $k=\mathbb{Q}(\sqrt{-d})$. It is a classical result of Siegel that for every $\epsilon>0$ there is a constant $c(\epsilon)$ such that
$$h_{k}>c(\epsilon)\left|d_{k}\right|^{\frac{1}{2}-\epsilon},$$
where $d_{k}$ is the discriminant. More recently, Ellenberg and Venkatesh [4] proved that there is another positive constant $c^{\prime}(\epsilon)$ so that
$$h_{k, 3} \leq c^{\prime}(\epsilon)\left|d_{k}\right|^{\frac{1}{3}+\epsilon} .$$
(Also, see [10] and [6] for earlier bounds which suffice here.) Therefore
$$\frac{h_{k}}{h_{k, 3}} \geq \frac{c(\epsilon)}{c^{\prime}(\epsilon)}\left|d_{k}\right|^{\frac{1}{6}-2 \epsilon} .$$
Fixing a small $\epsilon$ and letting $d \rightarrow \infty$ proves the theorem, since
$$d_{k}=\left\{\begin{array}{ccc}
d & d \equiv 1 & (\bmod 4) \\
4 d & d \not \equiv 1 & (\bmod 4) .
\end{array}\right.$$
for square-free $d$. \(\square\)

Remark. It is relatively easy to show that there are infinitely many distinct onecusped elements in each commensurability class for which $h_{k, 3}=h_{k}$. Choosing $K_{f} \mathrm{~s}$ for which the non-hyperspecial vertex is chosen at arbitrarily large inert primes gives an infinite family of non-isomorphic lattices, all of which are 1-cusped. This construction works for any natural number $N$ for which $N=$ $h_{k} / h_{k, 3}$ for some imaginary quadratic field $k$.

Finally, we end with a table of the known $d$ for which $\mathbb{Q}(\sqrt{-d})$ determines a 1-cusped orbifold. Though the list of imaginary quadratic fields for which $h_{k, 3}=h_{k}$ is finite, we do not know if this table is complete (see [5]).

\section*{5 Higher rank}

\subsection*{5.1 Cusps in higher rank}

We now consider nonuniform lattices in $\operatorname{SU}(r+1, r)$ for $r>1$. By Margulis's Arithmeticity Theorem, all such lattices are arithmetic, so each nonuniform

\begin{table}
\begin{tabular}[t]{|l|l|}
\hline $h_{k}$ & $d$ \\
\hline \multirow{3}{*}{1} & 3, 4, 7 \\
\hline & 8, 11, 19 \\
\hline & 43, 67, 163 \\
\hline \multirow{3}{*}{3} & 23, 31, 59, 83, 107, 139 \\
\hline & 211, 283, 307, 331, 379 \\
\hline & 499, 547, 643, 883, 907 \\
\hline 9 & 4027 \\
\hline 27 & $\emptyset$ \\
\hline
\end{tabular}
\captionsetup{labelformat=empty}
\caption{Table 1: Some $\mathbb{Q}(\sqrt{-d})$ which give 1-cusped orbifolds.}
\end{table}
arithmetic lattice in $\operatorname{SU}(r+1, r)$ is commensurable with $\mathcal{G}(\mathbb{Z})$, where $\mathcal{G}$ is an isotropic $\mathbb{Q}$-form of $\operatorname{SU}(r+1, r)$. We now briefly describe the possible nonuniform commensurability classes, and describe how one determines the cusps for lattices of simple type.

In short, commensurability classes of nonuniform lattices arise from hermitian forms on $D^{m}$, where $D$ is a central simple division algebra over the imaginary quadratic field $k$ with involution of second kind. If $D$ has degree $d$, then $d m=2 r+1$. If $q=2 r+1$ is prime, there is a unique commensurability class of nonuniform lattices in $\operatorname{SU}(r+1, r)$ for every imaginary quadratic field, and these are all the nonuniform commensurability classes. The case $d=2 r+1$ and $m=1$ determines cocompact lattices, since $D$ is a division algebra.

The situation for the commensurability class of a nonuniform lattice of simple type is exactly the same as for $\mathrm{SU}(2,1)$. The maximal lattice $\bar{\Gamma}$ normalizes a principal arithmetic lattice $\Gamma_{K_{f}}$ for $K_{f}<\mathcal{G}\left(\mathbb{A}_{f}\right)$ as before. Furthermore, we may again assume that $K_{f}$ is hyperspecial at all but finitely many places, stabilizes a vertex of the Bruhat-Tits building at all but split primes of $\mathcal{O}_{k}$, and is an Iwahori subgroup at some finite set $I$ of split primes. In fact, the proofs carry through verbatim, with the odd integer $q$ instead of 3. See [13] for details.

In this setting, a cusp of $\Gamma$ corresponds to conjugacy classes of chains of parabolic subgroups in $\Gamma$. See [1]. Recall that an isotropic flag for the hermitian form $h$ is a strictly ascending chain of $h$-isotropic subspaces
$$\{0\}=\mathcal{F}_{0} \subset \mathcal{F}_{1} \subset \mathcal{F}_{2} \subset \cdots \subset \mathcal{F}_{n} \subseteq \mathbb{C}^{n} .$$
If $h$ is a hermitian form of signature $(r+1, r)$ on $k^{q}, q=2 r+1$, then a maximal isotropic flag in $k^{q}$ is of the form $\left\{\mathcal{F}_{j}\right\}$, where $\mathcal{F}_{j}$ has dimension $j$, and $0 \leq j \leq r$. That is, the maximal isotropic subspace of $k^{q}$ has dimension $r$. For our purposes, it suffices to record the following.

Proposition 5.1. Suppose there is a $\mathbb{Q}$-form of $\operatorname{SU}(r+1, r)$ of simple type over the imaginary quadratic field $k$ such that $\Gamma$ is commensurable with $\mathcal{G}(\mathbb{Z})$. Then
cusps of $\Gamma$ are in one-to-one correspondence of $\Gamma$-orbits of maximal $h$-isotropic flags
$$\mathcal{F}=\left\{\mathcal{F}_{j}\right\}_{j=0}^{r} \subset k^{q} .$$

\subsection*{5.2 Zink's Theorem in higher rank}

We now describe Zink's Theorem for $\operatorname{SU}(r+1, r)$, which is the first step to generalizing Theorem 1.1 to Theorem 1.3. Choose $h$ to be the unimodular (for the standard $\mathcal{O}_{k}$-lattice $\mathcal{L}_{0}$ ) hermitian form
$$\left(\begin{array}{cccccc} 
& & & & & \\
& & & & \ddots & \\
& & \pm 1 & & \\
& & 1 & & & \\
& \therefore & & & & \\
1 & & & & &
\end{array}\right),$$
where $\pm 1$ is chosen such that $\operatorname{det}(h)=1$, let $\mathcal{G}$ be the associated $\mathbb{Q}$-algebraic group, and $\Gamma_{\text {std }}=\mathcal{G}(\mathbb{Z})$ the special automorphism group of the hermitian lattice $\left(\mathcal{L}_{0}, h\right)$.

Theorem 5.2 ([18]). Let $\Gamma_{\text {std }}$ be as above. Then $\Gamma_{\text {std }}$ has $h_{k}^{r}$ cusps.
Proof. The proof is a direct generalization of the methods employed in the proof of Theorem 4.2. The goal is to count $\Gamma_{\text {std }}$-orbits of maximal isotropic flags $\mathcal{F}$ in $k^{q}$. The maximal isotropic flags have dimension $r$, so a flag is a chain of subspaces
$$F_{0}=\{0\} \subset F_{1} \subset \cdots \subset F_{r},$$
where $F_{j}$ has dimension $j$ over $k$. Therefore, $F_{r} \cap \mathcal{L}_{0}$ is an $\mathcal{O}_{k}$-module of rank $r$, so $F_{j+1} / F_{j}$ has rank one and we can associate to $F_{j+1}$ the ideal class of
$$\left(F_{j+1} \cap \mathcal{L}_{0}\right) /\left(F_{j} \cap \mathcal{L}_{0}\right) .$$
This associates to each flag an element of $h_{k}^{r}$.
Since $n$ is odd and $h$ is unimodular, we can find $h$-isotropic vectors $x_{1}, \ldots x_{r}$ and $y_{1}, \ldots, y_{r}$ so that
$$\mathcal{L}_{0}=I_{1} x_{1} \oplus \cdots \oplus I_{r} x_{r} \oplus I_{1}^{\prime} y_{1} \oplus \cdots \oplus I_{r}^{\prime} y_{r} \oplus I_{0} z_{0},$$
where $I_{j}=F_{j} \cap \mathcal{L}_{0}$, and the $I_{j}^{\prime}$ correspond to another isotropic flag $\mathcal{F}^{\prime}$ which determines the $\mathcal{O}_{k}$-homomorphisms of $\mathcal{F}$ to $\mathcal{O}_{k}$. The vector $z_{0}$ is $h$-independent from $\mathcal{F}$ and $\mathcal{F}^{\prime}$ and non-isotropic. Note that this decomposition is analogous to the one used in Theorem 4.2, with 'isotropic line' replaced with 'isotropic flag'.

The same exact methods as in the proof of Theorem 4.2 show that two isotropic flags are $\Gamma$-equivalent if and only if they represent the same element of $h_{k}^{r}$, and that for each $r$-tuple in $h_{k}^{r}$ there exists a maximal isotropic flag representing that element. \(\square\)

\subsection*{5.3 Cusps of maximal lattices}

We now describe how Theorem 4.8 generalizes to give Theorem 1.3. Since the notions of congruence subgroups and the 'Hecke congruence subgroups' $\Gamma_{0}(N)$ become extremely complicated, given that the number of choices of proper parabolic subgroups grows with $r$, it is more natural to go straight to the main result. Recall the notation of §5.2, and we assume $r>1$, so arithmeticity is automatic.

Theorem 5.3. Let $\bar{\Gamma}<\mathrm{SU}(r+1, r)$ be a maximal lattice of simple type, defined via the imaginary quadratic field $k$. Conjugate $\bar{\Gamma}$ so that it normalizes the principal arithmetic lattice $\Gamma_{K_{f}}$. Let $I$ be the number of (split) primes for which $K_{f}$ is an Iwahori subgroup and $m_{K_{f}}=\left|I \backslash \Xi_{K_{f}}\right|$. Then $\Gamma$ has
$$q^{m_{K_{f}}} \frac{h_{k}^{r}}{h_{k, q}}$$
cusps.
Proof. Consider Figure 1, where the bottom group is now best called just $\bar{\Gamma} \cap$ $\Gamma_{\text {std }}$. Since the $p$-component of $K_{f}$ is either $K_{p}^{0}$ or one of the groups $K_{p}^{v_{j}}$, each reduction modulo $p$ of $\bar{\Gamma} \cap \Gamma_{\text {std }}$ is a parabolic subgroup of the corresponding $\mathbb{F}_{p}$-group that contains the Borel subgroup of upper triangular matrices. Each parabolic subgroup has $m_{p}$ orbits of maximal isotropic flags modulo $p$, where $m_{p}=1$ for almost every $p$. Therefore, $\bar{\Gamma} \cap \Gamma_{\text {std }}$ has
$$h_{k}^{r} \prod_{p} m_{p}$$
cusps. Indeed, the number of orbits of lines modulo $p$ is explicitly determined by the type of the corresponding parabolic subgroup.

Since $q$ is odd, every unit of $\mathcal{O}_{k}$ is a $q^{\text {th }}$ power, unless $q \equiv 3(\bmod 4)$ and $k=\mathbb{Q}(\sqrt{-3})$. We assume for now that every unit is a $q^{\text {th }}$ power in $k$. The necessary adjustments for $d=3$ and $q \equiv 3(\bmod 4)$ are exactly the same as the case $q=3$. Let $\bar{\Gamma}_{\text {std }}$ be the normalizer of $\Gamma_{\text {std }}$ in $\operatorname{SU}(r+1, r)$. The center of $\operatorname{SU}(r+1, r)$ is cyclic of order $q$, and $k$ contains no $q^{\text {th }}$ roots of unity for $r>1$. The argument in Proposition 4.6 carries over unaltered to $q$-dimensions to show that
$$[\bar{\Gamma}: \Gamma]=q h_{k, q} .$$
See also [13].
Furthermore, a direct generalization of Corollary 4.7 shows that $\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}$ has
$$\frac{h_{k}^{r}}{h_{k, q}} \prod_{p} m_{p}$$
cusps. Indeed,
$$\left[\bar{\Gamma} \cap \bar{\Gamma}_{\text {std }}: \bar{\Gamma} \cap \Gamma_{\text {std }}\right]=\left[\bar{\Gamma}_{\text {std }}: \Gamma_{\text {std }}\right],$$
again from considering reductions modulo $p$, and each element of $\bar{\Gamma}_{\text {std }}$ not in $\Gamma_{\text {std }}$ acts on $h_{k}^{r}$ by multiplication by $\operatorname{cl}(J)$, where $J$ is some fractional ideal for which $J^{q}$ is principal. (Note that $J^{s}$ may be principal for some divisor $s$ of $q$.)

However, for each $p$ where the $p$-component is a vertex stabilizer of the building, i.e., is not Iwahori, there exists an element of $\Gamma_{K_{f}}<\bar{\Gamma}$ for which the reduction modulo $p$ identifies the $m_{p}$ isotropic subspaces left inequivalent by the reduction of $\bar{\Gamma} \cap \Gamma_{\text {std }}$ modulo $p$. Since the case where $m_{p}=q$ corresponds precisely to when the reduction modulo $p$ of $\bar{\Gamma} \cap \Gamma_{\text {std }}$ is upper triangular, we have that $\bar{\Gamma}$ has
$$q^{m_{K_{f}}} \frac{h_{k}^{r}}{h_{k, q}}$$
cusps. \(\square\)

Suppose that $q$ is prime. Then every nonuniform arithmetic lattice in $\mathrm{SU}(r+$ $1, r)$ for $r>1$ is of simple type. Theorem 1.4 is trivial for $N=1$. Assuming the Generalized Riemann Hypothesis, Ellenberg-Venkatesh [4] prove that $h_{k, q}$ grows like $|d|^{\frac{1}{2}-\frac{1}{2 q}+\epsilon}$. We then get Theorem 1.4 exactly the same as Theorem 4.9. Constructing infinitely many commensurable one-cusped manifolds is also done exactly the same as in the remark of §4.4. However, now the commensurability classes that produce a one-cusped element come precisely from the nine imaginary quadratic fields of class number one.

\section*{Acknowledgments}

This paper is a condensed version of my Ph.D. thesis at the University of Texas at Austin. I want to thank my advisor, Alan Reid, for his encouragement and inspiration. I also thank Jordan Ellenberg for a very helpful correspondence regarding torsion in class groups. Finally, I want to thank the people that showed interest in this project, especially Gopal Prasad, Benson Farb, Daniel Allcock, Ben McReynolds, and Misha Belolipetsky.

\section*{References}
\begin{itemize}
\item[] [1] Armand Borel and Lizhen Ji. Compactifications of symmetric and locally symmetric spaces. Mathematics: Theory \& Applications. Birkhäuser Boston Inc., Boston, MA, 2006.
\item[] [2] Armand Borel and Gopal Prasad. Finiteness theorems for discrete subgroups of bounded covolume in semi-simple groups. Inst. Hautes Études Sci. Publ. Math., (69):119-171, 1989.
\item[] [3] Ted Chinburg, Darren Long, and Alan W. Reid. Cusps of minimal non-compact arithmetic hyperbolic 3-orbifolds. Pure Appl. Math. Q., 4(4, part 1):1013-1031, 2008.
\end{itemize}
\begin{itemize}
\item[] [4] Jordan S. Ellenberg and Akshay Venkatesh. Reflection principles and bounds for class group torsion. Int. Math. Res. Not. IMRN, (1):Art. ID rnm002, 18, 2007.
\item[] [5] D. R. Heath-Brown. Imaginary quadratic fields with class group exponent 5. Forum Math., 20(2):275-283, 2008.
\item[] [6] H. A. Helfgott and A. Venkatesh. Integral points on elliptic curves and 3-torsion in class groups. J. Amer. Math. Soc., 19(3):527-550, 2006.
\item[] [7] Yoshinobu Kamishima. Nonexistence of cusp cross-section of one-cusped complete complex hyperbolic manifolds. II. Int. Math. Forum, 2(25-28):1251-1258, 2007.
\item[] [8] G. A. Margulis and J. Rohlfs. On the proportionality of covolumes of discrete subgroups. Math. Ann., 275(2):197-205, 1986.
\item[] [9] Kathleen L. Petersen. One-cusped congruence subgroups of Bianchi groups. Math. Ann., 338(2):249-282, 2007.
\item[] [10] L. B. Pierce. The 3-part of class numbers of quadratic fields. J. London Math. Soc. (2), 71(3):579-598, 2005.
\item[] [11] Vladimir Platonov and Andrei Rapinchuk. Algebraic groups and number theory, volume 139 of Pure and Applied Mathematics. Academic Press Inc., 1994.
\item[] [12] Gopal Prasad and Sai-Kee Yeung. Fake projective planes. Invent. Math., 168(2):321-370, 2007.
\item[] [13] Gopal Prasad and Sai-Kee Yeung. Arithmetic fake projective spaces and arithmetic fake Grassmannians. Amer. J. Math., 131(2):379-407, 2009.
\item[] [14] Alan W. Reid. Arithmeticity of knot complements. J. London Math. Soc. (2), 43(1):171-184, 1991.
\item[] [15] Winfried Scharlau. Quadratic and Hermitian forms, volume 270 of Grundlehren der Mathematischen Wissenschaften. Springer-Verlag, 1985.
\item[] [16] J. Tits. Reductive groups over local fields. In Automorphic forms, representations and L-functions (Proc. Sympos. Pure Math., Oregon State Univ., Corvallis, Ore., 1977), Part 1, Proc. Sympos. Pure Math., XXXIII, pages 29-69. Amer. Math. Soc., 1979.
\item[] [17] Hanns Zeltinger. Spitzenanzahlen und Volumina Picardscher Modulvarietäten. Bonner Mathematische Schriften, 136. Universität Bonn Mathematisches Institut, 1981.
\item[] [18] Thomas Zink. Über die Anzahl der Spitzen einiger arithmetischer Untergruppen unitärer Gruppen. Math. Nachr., 89:315-320, 1979.
\end{itemize}