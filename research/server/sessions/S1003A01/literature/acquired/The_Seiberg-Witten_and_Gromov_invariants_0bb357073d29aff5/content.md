---
retention_scope: session
part: 1
total_parts: 1
---

---
source_file: The_Seiberg-Witten_and_Gromov_invariants_91d3f0d3b243.pdf
converter: mathpix
format: mmd
---

\title{
THE SEIBERG-WITTEN AND GROMOV INVARIANTS
}

\author{
Clifford Henry Taubes
}

\section*{0. Introduction}

The purpose of this article is to announce an equivalence between the Seiberg-Witten gauge theory invariants of a symplectic 4-manifold and a certain set of Gromov invariants as defined using pseudo-holomorphic 2-submanifolds (Theorem 4.1). The theorem below lists some consequences of this equivalence:

Theorem A. Let $X$ be a compact, oriented 4-manifold with $b_{2}^{+}>1$ and with a symplectic form $\omega$. Then
\begin{itemize}
\item[(1)] The Poincaré dual to the canonical bundle $K$ of $X$ is represented by the fundamental class of an embedded, symplectic curve.
\item[(2)] A homology class in X which is represented by the fundamental class of an embedded 2-sphere that has self-intersection number -1, and that pairs nontrivially with $c_{1}(K)$ has pairing $\pm 1$ with $c_{1}(K)$ and is represented by the fundamental class of an embedded, symplectic 2-sphere.
\item[(3)] If $c_{1}(K) \cdot c_{1}(K)<0$, then $X$ can be symplectically blown down along a symplectic sphere of self-intersection-1.
\item[(4)] Suppose that $X$ cannot be symplectically blown down along a symplectic sphere of self-intersection-1; and suppose that $c_{1}(K)$ is not rationally trivial. Then, the signature of the intersection form of $X$ is no smaller than $-\frac{4}{3}\left(1-b_{1}\right)-\frac{2}{3} b_{2}$. (The $b_{i}$ 's are the Betti numbers.)
\end{itemize}

One can also deduce constraints on the Seiberg-Witten invariants of Theorem A's manifold $X$ using known facts about pseudo-holomorphic curves. These are detailed in Section 4, below.

There are also consequences for manifolds with $b_{2}^{+}=1$. In particular, one obtains (with the help of a theorem of Gromov [G])

\footnotetext{
Received March 1, 1995.
Research supported in part by the National Science Foundation.
}

Theorem B. The manifold $\mathbb{C P}^{2}$ has a unique (up to symplectomorphism) symplectic structure.

This theorem and other consequences of the stated equivalence are discussed below. Except for the briefest outlines, the proofs of these two theorems and the assertions below will appear in [T1].

The organization of the remainder of this paper is as follows. The first section reviews the definition of the Seiberg-Witten invariant in a fairly general context. Section 2 specializes to a discussion of the Seiberg-Witten invariant for symplectic manifolds. Section 3 defines the relevant Gromov invariant of a symplectic manifold. (This invariant is defined by Ruan in [R].) The fourth section states the main theorem-that the Seiberg-Witten invariant and the Gromov invariant agree. This section also details some corollaries of the main theorem. The fifth section outlines the strategy of the proof of the main theorem, and the last section contains some brief speculations about the meaning of the Seiberg-Witten invariant in the nonsymplectic world.

\section*{1. The Seiberg-Witten invariants}

The Seiberg-Witten invariants are defined a priori for a compact, oriented 4-manifold $X$ with the characteristic number $b_{2}^{+}>1$. (There is a more complicated structure in the case where $b_{2}^{+}=1$.) Here, $b_{2}^{+}$is equal to the number of +1 eigenvalues of the intersection form on the (rational) second homology. (Thus, $b_{2}^{+}=2^{-1}\left(\operatorname{rank}\left(H_{2}(X)+\operatorname{sign}(X)\right)\right.$, where $\operatorname{sign}(X)$ is the signature of $X$.) These invariants were first described in [W], and the reader is also referred to [KM] and [T2]. (A more complete description is in preparation with multiple authors.) What follows is a brief description of the invariants. (Note: these invariants vanish when $b_{2}^{+}+b_{1}$ is even.)

The Seiberg-Witten invariants of $X$ constitute a map from the set of equivalence classes of $\operatorname{Spin}_{\mathbb{C}}$ structures on $X$ (covering the frame bundle) to the integers. (These invariants are defined by counting (in a suitable sense) the solutions to a natural system of differential equations on $X$ which are defined using a $\operatorname{Spin}_{\mathbb{C}}$ structure.)

Here is a five-part digression to review some crucial 4-dimensional geometry.

Part 1: Note that
$$S O(4)=(S U(2) \times S U(2)) /\{ \pm 1\}$$
and
$$\operatorname{Spin}_{\mathbb{C}}(4)=(U(1) \times S U(2) \times S U(2)) /\{ \pm 1\},$$
where $\{ \pm 1\}$ acts on all factors in both cases in the obvious way.
Part 2: Fix a Riemannian metric on $X$. The metric defines the principal $S O(4)$ bundle of orthonormal frames on $X$. A Spin $_{\mathbb{C}}$ structure (denoted by $\mathcal{L}$ ) is simply a lift of this $S O(4)$ principal bundle to a $\operatorname{Spin}_{\mathbb{C}}(4)$ principal bundle. The set of equivalence classes of such lifts has, in a natural way, the structure of a principal $H^{2}(X ; \mathbb{Z})$ bundle over a point. This principal $H^{2}(X ; \mathbb{Z})$ bundle, Spin, is canonically defined and independent of the original choice of metric on $X$. Thus, one should think of the Seiberg-Witten invariant as a map from Spin to $\mathbb{Z}$.

Part 3: The group $S O(4)$ has two evident representations into $S O(3)=$ $\operatorname{SU}(2) /\{ \pm 1\}$, which will be called $\lambda_{+}$and $\lambda_{-}$. They are distinguished by the convention that the associated $\mathbb{R}^{3}$ bundles to the frame bundle of $X$ be isomorphic to the bundles $\Lambda_{+}$of self-dual 2 -forms and $\Lambda_{-}$of anti-self-dual 2-forms, respectively.

Likewise, the group $\operatorname{Spin}_{\mathbb{C}}(4)$ has two evident representations, $s_{+}$and $s_{-}$, into $U(2)=(U(1) \times S U(2)) /\{ \pm 1\}$. The convention is that the composition of $s_{+}$with the quotient homomorphism $U(2) \rightarrow U(2) /$ Center $=S O(3)$ factors through $S O(4)$ via $\lambda_{+}$. With the preceding understood, given a $\operatorname{Spin}_{\mathbb{C}}$ structure $\mathcal{L}$ on $X$, introduce the $\mathbb{C}^{2}$-vector bundles
$$S_{+}, S_{-} \longrightarrow X$$
which are associated to $\mathcal{L}$ via the representations $s_{+}$and $s_{-}$, respectively. (These bundles inherit natural fiber metrics.)

Let $\mathcal{L}$ and $\mathcal{L} \cdot e$ be elements in Spin, where $e \in H^{2}(X ; \mathbb{Z})$. Then, the bundles $S_{+}$for these two $\operatorname{Spin}_{\mathbb{C}}$ structures are related by $S_{+}(\mathcal{L} \cdot e) \simeq S_{+}(\mathcal{L}) \otimes$ $E$, where $E$ is a complex line bundle with first Chern class $c_{1}(E)=e$.

Part 4: Clifford multiplication, $c$, maps $T^{*} X$ into the skew adjoint endomorphisms of $S_{+} \oplus S_{-}$; it is characterized by the fact that $c(v)^{2}$ is multiplication by $-|v|^{2}$. In particular, $c$ induces maps
$$\sigma: S_{+} \otimes T^{*} X \rightarrow S_{-}$$
(by duality) and also $c_{+}: \Lambda_{+} \rightarrow \operatorname{End}\left(S_{+}\right)$. The adjoint of the latter will be denoted by
$$\tau: \operatorname{End}\left(S_{+}\right) \longrightarrow \Lambda_{+} \otimes \mathbb{C} ;$$
it maps a self-adjoint endomorphism into an imaginary-valued form.
Part 5: Let $A$ be a connection on $L \equiv \operatorname{det}\left(S_{+}\right)$. The connection $A$ with the Levi-Civita connection on $T^{*} X$ induces a covariant derivative on $S_{+}$. This maps sections of $S_{+}$into sections of $S_{+} \otimes T^{*} X$. The composition of
this last map with $\sigma$ in (1.4) defines the Dirac operator $D_{A}$, a first order, elliptic operator mapping sections of $S_{+}$to sections of $S_{-}$.

End the digression.
With the preceding understood, notice that the Seiberg-Witten equations are equations for a pair ( $A, \psi$ ), where $A$ is a connection on $L=$ $\operatorname{det}\left(S_{+}\right)$and where $\psi$ is a section of $S_{+}$. These equations read
$$D_{A} \psi=0 \quad \text { and } \quad P_{+} F_{A}=\frac{1}{4} \tau\left(\psi \otimes \psi^{*}\right),$$
where $P_{+}: \Lambda^{2} T^{*} X \rightarrow \Lambda_{+}$is the orthogonal projection. It proves useful at times to consider perturbations of (1.6) which have the form
$$D_{A} \psi=0 \quad \text { and } \quad P_{+} F_{A}=\frac{1}{4} \tau\left(\psi \otimes \psi^{*}\right)+\mu,$$
where $\mu$ is a fixed, imaginary-valued, self-dual 2-form on $X$.
The Seiberg-Witten invariant for the given $\operatorname{Spin}_{\mathbb{C}}$ structure $\mathcal{L} \in \operatorname{Spin}$ is obtained by making a suitable count of solutions of (1.6) or (1.7). Remark here that the group $C^{\infty}\left(X ; S^{1}\right)$ acts on the space of solutions to (1.7); a map $\varphi$ sends $(A, \psi)$ to $\left(A-2 \varphi^{-1} d \varphi, \varphi \psi\right)$. Here, $S^{1}$ is thought of as the unit sphere in $\mathbb{C}$. (This group acts freely at solutions where $\psi$ is not identically zero.) The quotient of the space of solutions to (1.7) by $C^{\infty}\left(S^{1} ; X\right)$ will be denoted by $M$. (The dependence on the $\operatorname{Spin}_{\mathbb{C}}$ structure and on the choice of $\mu$ in (1.7) will usually be suppressed.)

Here are five crucial facts about $M$ :
Fact 1: When $b_{2}^{+} \geq 1$, the space of solutions to (1.6) and (1.7) will contain no points where $\psi \equiv 0$ for a generic metric or choice of $\mu$ as long as $c_{1}(L)$ is rationally nonzero. Here, generic means off of a set of codimension $b_{2}^{+}$. (This follows from a theorem of Uhlenbeck in [FU].)
Fact 2: The space $M$ has naturally the structure of a real analytic variety. When $b_{2}^{+} \geq 1$, the space $M$ will be a smooth manifold for a generic choice of $\mu$ in (1.7). (Here, generic means a Baire subset of $C^{\infty}\left(\Lambda_{+}\right)$.) The dimension of this manifold is computed with the help of the Atiyah-Singer index theorem to be
$$d=-\frac{1}{4}(2 \chi(X)+3 \operatorname{sign}(X))+\frac{1}{4} c_{1}(L) \cdot c_{1}(L) .$$
Here, $\chi$ is the Euler characteristic of $X$ and $\operatorname{sign}(X)$ is the signature. Also, the notation $u \cdot v$ for classes $u, v \in H^{2}(X ; \mathbb{Z})$ denotes the evaluation of their cup product on the fundamental class of $X$.
Fact 3: A choice of orientation for the line
$$\operatorname{det}\left(H^{0}(X ; \mathbb{R})\right) \otimes \operatorname{det}\left(H^{1}(X ; \mathbb{R})\right) \otimes \operatorname{det}\left(H^{2+}(X ; \mathbb{R})\right)$$
serves to orient $M$. (The orientation of a point is a choice of ±1 to assign to said point.)
Fact 4: Fix a base point in $X$ and let $C_{0}^{\infty}\left(S^{1} ; X\right)$ denote the subset of maps which map said base point to 1. Let $M^{0}$ denote the quotient of the space of solutions to (1.7) by the latter group. Where $M$ is a smooth manifold, the projection $M^{0} \rightarrow M$ defines a principal $S^{1}$ bundle.
Fact 5: The space $M$ is compact.
With the preceding understood, here is the definition of the Seiberg-Witten invariant:

Definition 1.1. Let $X$ be a compact, oriented 4 -manifold with $b_{2}^{+}>1$ and let $\mathcal{L} \in$ Spin $_{\text {be a }} \operatorname{Spin}_{\mathbb{C}}$ structure on $X$. Choose an orientation for (1.9). The Seiberg-Witten invariant $S W(\mathcal{L})$ for $\mathcal{L}$ is defined as follows:
\begin{itemize}
\item[a)] When $d<0$ in (1.8), the invariant is defined to be zero.
\item[b)] When $d=0$ in (1.8), choose $\mu$ in (1.7) to make $M$ a smooth manifold. Then this $M$ is a finite union of signed points and the Seiberg-Witten invariant is the sum over these points of the corresponding ±1's.
\item[c)] When $d>0$ in (1.8), choose $\mu$ in (1.7) to make $M$ a smooth manifold. This $M$ is compact and oriented, so it has a fundamental class. The Seiberg-Witten invariant is obtained by pairing this fundamental class with the maximal cup product of the first Chern class of the line bundle $M^{0} \times_{S^{1}} \mathbb{C}$.
\end{itemize}

Note that the dimension of $M$ and $b_{2}^{+}+b_{1}$ have opposite parity; thus, the Seiberg-Witten invariants are zero when $b_{2}^{+}+b_{1}$ is even.

The preceding definition is justified by
Proposition 1.2. Let $X$ be a compact, oriented, connected 4-manifold with $b_{2}^{+}>1$. Then $S W$ defines a map from Spin to $\mathbb{Z}$ which depends only on the underlying smooth structure of $X$. That is, the value of $S W(\mathcal{L})$ is independent of the choice of metric and perturbing form $\mu$ in (1.7). It depends only on $\mathcal{L}$ up to isomorphism. Furthermore, the assignment of $S W$ to a $S p i n_{\mathbb{C}}$ structure is invariant under self-diffeomorphisms of $X$ in the following sense: if $\varphi$ is a diffeomorphism of $X$, then the value of $S W$ on $\varphi^{*} \mathcal{L}$ is, up to sign, the same as the value of $S W$ on $\mathcal{L}$.

\section*{2. Symplectic manifolds}

A 2-form $\omega$ on an oriented 4-manifold $X$ is symplectic when
$$d \omega=0 \quad \text { and } \quad \omega \wedge \omega \neq 0$$
everywhere. Furthermore, the 4-form $\omega \wedge \omega$ will be required to orient $X$. A 4-manifold $X$ with a symplectic form $\omega$ will be called a symplectic 4manifold.

Every symplectic manifold has a canonical complex line bundle $K$; called the canonical bundle. Fix a Riemannian metric on $X$ and then $K$ can be identified as the orthogonal 2-plane bundle to the projection of $\omega$ into $\Lambda_{+}$. (The fact that $\omega \wedge \omega \neq 0$ implies that this last projection is nowhere zero.) Alternately, $K$ can be defined by choosing an almost-complex structure for $T X$ which is compatible (in the sense of Gromov [G]) for $\omega$ (see below). In this case, $K$ is $\operatorname{det}\left(T^{1,0} X\right)$. The specification of such an almost-complex structure is equivalent to the specification of a metric on $X$ for which $\omega$ is self-dual. Note that when $t \rightarrow \omega_{t}$ is a continuous, 1-parameter family of symplectic forms on $X$, then the canonical bundles for $\left(X, \omega_{0}\right)$ and $\left(X, \omega_{1}\right)$ will be isomorphic.

A symplectic manifold also has a canonical $\operatorname{Spin}_{\mathbb{C}}$ structure (see [T1]). Indeed, use a metric for which $\omega$ is self-dual with length $\sqrt{2}$. For such a metric, the canonical $\operatorname{Spin}_{\mathbb{C}}$ structure is characterized by the fact that its associated bundle $S_{+}$is naturally isomorphic to $\mathbb{I} \oplus K^{-1}$, where $\mathbb{I}$ is the trivial complex line bundle. Here, $\omega$ acts by Clifford multiplication on the $\mathbb{I}$ summand with eigenvalue $-2 i$, and it acts on $K^{-1}$ summand with eigenvalue $+2 i$. (When $t \rightarrow \omega_{t}$ is a continuous, 1-parameter family of symplectic forms on $X$, then the canonical $\operatorname{Spin}_{\mathbb{C}}$ structures for $\omega_{0}$ and $\omega_{1}$ can be naturally identified.)

The defining of this canonical Spin $_{\mathbb{C}}$ structure allows one to identify Spin, the set of equivalence classes of $\operatorname{Spin}_{\mathbb{C}}$ structures on $X$, with the set of equivalence classes of complex line bundles over $X$. (The latter is, of course, the same as $H^{2}(X ; \mathbb{Z})$.) The $\operatorname{Spin}_{\mathbb{C}}$ structure which corresponds to a given complex line bundle $E$ is characterized by the fact that its bundle $S_{+}$is given by
$$S_{+}=E \oplus\left(K^{-1} \otimes E\right) .$$
Note that Clifford multiplication by $\omega$ on $S_{+}$in (2.2) preserves the splitting with the summand $E$ having eigenvalue $-2 i$.

For a symplectic manifold with $b_{2}^{+}>1$, [T2] has a proof that the SeibergWitten invariants are ±1 for the cases $E=\mathbb{I}, K$ in (2.2). (In general, the Seiberg-Witten invariant for $E$ and for $K \otimes E^{-1}$ are equal in absolute magnitude. This follows from the quaternionic nature of the $\operatorname{Spin}_{\mathbb{C}}$ representations [W].) It is proved in [T3] that a $\operatorname{Spin}_{\mathbb{C}}$ structure as in (2.2) has nonzero Seiberg-Witten invariants only if
$$0 \leq[\omega] \cdot c_{1}(E) \leq[\omega] \cdot c_{1}[K],$$
where $[\omega]$ is the cohomology class of the symplectic form. (It is also proved in [T3] that left hand equality in (2.3) is achieved only by $E=\mathbb{I}$ and that the right hand equality is only achieved by $E=K$.)

By the way, because the line bundle $L$ for (2.2) is $K^{-1} \otimes E^{2}$, the dimension $d$ of $M$ as given in (1.8) is simply
$$d=-c_{1}(K) \cdot c_{1}(E)+c_{1}(E) \cdot c_{1}(E) .$$

The final remark of this section is to point out that the line in (1.9) has a canonical orientation on a symplectic manifold; the line in (1.9) is naturally isomorphic to the determinant line bundle of the elliptic operator $\delta \equiv\left(P_{+} d, d^{*}\right): C^{\infty}\left(T^{*} X\right) \rightarrow C^{\infty}\left(\mathbb{I}_{\mathbb{R}} \oplus \Lambda_{+}\right)$, where $\mathbb{I}_{\mathbb{R}}$ is the trivial real line bundle. The latter operator differs by a canonical zero'th order term from an operator, $\delta_{\omega}$, which intertwines the action of $J$ on $T^{*} X$ with the action of a square -1 endomorphism $J^{\prime}$ of $\mathbb{I}_{\mathbb{R}} \oplus \Lambda_{+}$. Because of this intertwining property, both the kernel and cokernel of $\delta_{\omega}$ will be complex, and so its index bundle will have a natural orientation. (The endomorphism $J^{\prime}$ is defined as follows: write $\zeta \in \mathbb{I}_{\mathbb{R}} \oplus \Lambda_{+}$as $\zeta_{0}+\zeta_{1} \cdot \underline{\omega}+\rho$, where $\rho$ is orthogonal to $\omega$ in $\Lambda_{+}$and where $\zeta_{0,1}$ are real numbers. Here, $\underline{\omega}$ is the unit length section $\omega / \sqrt{2}$. Then, set $J^{\prime}(\zeta) \equiv-\zeta_{1}+\zeta_{0} \cdot \underline{\omega}+\underline{\omega} \times \rho$, where $\underline{\omega} \times(\cdot)$ at a point $p \in X$, is given by the cross product on $\left.\Lambda_{+}\right|_{p}=\mathbb{R}^{3}$ by the unit vector defined $\underline{\omega}$. With $J^{\prime}$ understood, set $\delta_{\omega} \equiv \frac{1}{2} \cdot\left(\delta-J^{\prime} \delta J\right)$. Note that $\delta_{\omega}$ is the same as $\delta$ when $X$ is complex and $\omega$ is the Kähler form.)

\section*{3. The Gromov invariants}

Let $X$ be a symplectic manifold. Then the tangent bundle to $X$ admits an almost-complex structure, a homomorphism $J: T X \rightarrow T X$ with $J^{2}=-1$. As with a genuinely complex manifold, the almost-complex structure $J$ defines a splitting $T^{*} X \otimes \mathbb{C} \cong T^{1,0} \oplus T^{0,1}$, where $J$ acts on $T^{\prime}$ as multiplication by $i$. The canonical bundle of the almost-complex structure is defined to be $K \equiv \operatorname{det}\left(T^{1,0}\right)$.

An almost-complex structure $J$ is deemed compatible with $\omega$ when
$$\begin{aligned}
& \text { a) } \quad \omega(w, J v)=-\omega(J w, v) . \\
& \text { b) } \quad \omega(v, J v) \geq 0 \text { with equality if and only if } v=0 .
\end{aligned}$$
Here, $\omega$ is thought of as a skew symmetric form on $T X$. Since the space of compatible almost-complex structures is contractible, one can think of $K$ as being associated to the symplectic structure $\omega$. (Note that the assignment of $(v, w)$ in $T X$ to $\omega(v, J w)$ defines a metric on $T X$. For such a metric, the
form $\omega$ is self-dual. Correspondingly, any metric for which $\omega$ is self-dual can be used to construct an almost-complex structure $J$ which satisfies (3.1).)

Let $\Sigma$ be a compact, embedded 2-manifold of $X$. Call $\Sigma$ a pseudoholomorphic submanifold of $X$ when $J$ maps the tangent space of $\Sigma$ to itself. (This $\Sigma$ need not be connected.) Notice that if $\Sigma$ is a pseudoholomorphic submanifold, then $J$ defines a complex structure on $\Sigma$ and then the identity map of $\Sigma$ (as a map from the complex curve $\Sigma$ into $X$ ) is pseudo-holomorphic in the sense of Gromov [G]. See also [McS], [R]. (A map from a complex curve to $X$ is called pseudo-holomorphic by Gromov when the differential intertwines the complex structure on the curve with the given $J$.)

The restriction of the symplectic form $\omega$ to a pseudo-holomorphic submanifold $\Sigma$ is always symplectic, and so orients $\Sigma$. With this orientation understood, then each pseudo-holomorphic submanifold of $X$ has a fundamental class which is a priori nontrivial in $H_{2}(X ; \mathbb{Z})$. (It is nontrivial since the integral of $\omega$ over $\Sigma$ is positive.) Use $e \equiv e(\Sigma) \in H^{2}(X ; \mathbb{Z})$ to denote the Poincaré dual of this fundamental class.

An important feature of a connected pseudo-holomorphic submanifold $\Sigma$ is that the class $e$ determines the genus of $\Sigma$ through the adjunction formula:
$$2-2 g+e \cdot e=-c_{1}(K) \cdot e$$
(Note that $e \cdot e$ is the degree of the normal bundle in $X$ to $\Sigma$.)
Let $e \in H^{2}(X ; \mathbb{Z})$ be a nontrivial cohomology class, and let $H \equiv H(e)$ denote the space of pseudo-holomorphic submanifolds of $X$ whose fundamental class is Poincaré dual to $e$. Here, submanifolds count with multiplicity 1 except that tori with zero self-intersection can have multiplicity 1 or more. Here is the first structure theorem for $H$ : (In the lemmas below, the term "generic $J$ " signifies that $J$ is to be chosen from a certain Baire subset of the space of smooth almost-complex structures $J$ which obey (3.1).)

Lemma 3.1. For a generic choice of $J$, this space $H$ is a smooth manifold of dimension
$$d=-c_{1}(K) \cdot e+e \cdot e$$
Furthermore, $H$ has a canonical orientation.
(The tangent space to $H$ at a given $\Sigma$ can be naturally identified with the kernel of a certain first order elliptic operator on $\Sigma$. In fact, with the complex structure $J$ on $\Sigma$, this operator is a zero'th order perturbation of the $\bar{\partial}$ operator coupled to the normal bundle of $\Sigma$. Since the components
of $\Sigma$ are assumed to be disjoint and embedded, the sum of the degrees of their normal bundles is equal to $e \cdot e$.)

See [T1] for the proofs of this lemma and of the subsequent assertions in this subsection. See also [R].

Note, by the way, that $c_{1}(K)$ reduces $\bmod (2)$ to the 2nd Stieffel-Whitney class of $X$. This implies that (3.3) is always an even number. If $d$ in (3.3) is positive, choose a set of $d / 2$ distinct points $\Omega$ in $X$ and define $H_{\Omega}$ as the subspace of submanifolds $\Sigma \in H$ which contain all points in $\Omega$. Here is the structure theorem for $H_{\Omega}$ :

Lemma 3.2. For a generic choice of $J$ and points $\Omega$, this $H_{\Omega} \subset H$ will be a canonically oriented 0-submanifold.
(Remember that an oriented point is a point with a choice of ±1.)
The preceding structure lemma, coupled with the following compactness lemma are the crucial ingredients for the definition of the Gromov invariants of the manifold $X$.

Lemma 3.3. In the case $d=0$ of (3.3), the space $H$ is compact for a generic choice of $J$. When $d>0$, the space $H_{\Omega}$ is compact for a generic choice of $J$ and of the points $\Omega$.

Here is a remark concerning the compactness proof for the case where $d=0$. (The general case is mostly similar.) A sequence in $H$ can fail to converge by limiting to a multi-component, immersed surface, or, more generally, to a multi-component, immersed surface with singular points. With the help of the Smale-Sard theorem and dimension-counting arguments, one can prove that such limits are absent when the almost-complex structure $J$ is suitably generic. Essentially, one argues that the possible limiting sets form $H$-like moduli spaces which are locally defined by equations with Fredholm linearizations whose indices are at least two less than the dimension $d$ in (3.3). Then, because $d=0$, these moduli spaces will have negative dimension and so the Smale-Sard theorem will guarantee their absence for the generic $J$.

For example, if the limit of a sequence in $H$ is the image of a connected, immersed curve, then this curve will be pseudo-holomorphic with some number $n$ of double points, all with positive intersection number (see, e.g. [McS]). (The local model for the degeneration is the zero locus of $z_{1} z_{2}=\epsilon$ in $\mathbb{C}^{2}$ as $\epsilon \rightarrow 0$.) The image in $H_{2}(X ; \mathbb{Z})$ of the fundamental class of this curve will still represent the Poincaré dual to $e$.

An immersed curve has a well defined normal bundle with some degree $\nu$. Here, $\nu$ is given by
$$\nu=e \cdot e-2 n .$$

Also, there is the adjunction formula analog of (3.2) which reads
$$2-2 g^{\prime}+\nu=-c_{1}(K) \cdot e,$$
where $g^{\prime}$ is the genus of the immersed curve. Furthermore, the immersed curve sits in a moduli space which is defined like $H$ except that the sets in question are no longer submanifolds but images of immersions. For a suitably generic $J$, such a moduli space will be a smooth manifold of dimension $d^{\prime}=2-2 g^{\prime}+2 \nu$. With this understood, it follows from (3.4) and (3.5) that
$$d^{\prime}=-c_{1}(K) \cdot e+e \cdot e-2 n$$
which is $2 n$ less than the dimension $d$ in (3.3). Thus, if $d$ in (3.3) is zero, then $d^{\prime}$ in (3.6) will be negative and the generic $J$ will admit no connected, immersed curves whose fundamental class represents the Poincaré dual to $e$.

Here is a definition of Gromov invariants for a symplectic 4-manifold:
Definition 3.4. Let $X$ be a compact, symplectic 4-manifold. Define an invariant $G r: H^{2}(X ; \mathbb{Z}) \rightarrow \mathbb{Z}$ by assigning to a class $e$ the following:
\begin{itemize}
\item[a)] When $d<0$ in (3.3), set $\operatorname{Gr}(e)=0$.
\item[b)] When $d=0$ in (3.3), then $H$, as defined for a generic $J$, is a finite set of signed points, and $\operatorname{Gr}(e)$ is the sum over the points in $H$ of the corresponding ±1's.
\item[c)] When $d>0$ in (3.3), then $H_{\Omega}$, as defined for a generic $J$ and $\Omega$, is a finite set of signed points, and $\operatorname{Gr}(e)$ is the sum over the points in $H$ of the corresponding ±1's.
\end{itemize}

This definition is justified by the following proposition:
Proposition 3.5. The invariant $G r: H_{2}(X ; \mathbb{Z}) \rightarrow \mathbb{Z}$ depends only on the pair $(X, \omega)$ of a compact, oriented 4-manifold and a symplectic form $\omega$. That is, the value of $G r$ is independent of the choice of almost-complex structure $J$ and, in the $d>0$ case, of the set $\Omega$. Furthermore, if $\left\{\omega_{t}: t \in\right.$ [0,1]\} is a continuous family of symplectic forms on $X$, then the invariants $G r$ as defined for $\omega_{0}$ and for $\omega_{1}$ agree. Finally, $G r$ is invariant under self-diffeomorphisms of $X$ in the following sense: if $\varphi: X \rightarrow X$ is a self-diffeomorphism, then the value of $G r$ (as defined by form $\omega$ ) on a class $e$ is, up to sign, the same as that of Gr (as defined by the pulled back form $\left.\varphi^{*} \omega\right)$ on the class $\varphi^{*} e$.

\section*{4. The main theorems}

With the Seiberg-Witten invariants and the Gromov invariants now defined, here is the main theorem:

Theorem 4.1. Let $X$ be a compact, oriented, symplectic 4-manifold. Let $E$ be a nontrivial, complex line bundle over $X$ and use $E$ to define a Spin $_{\mathbb{C}}$ structure $\mathcal{L} \in$ Spin with $S_{+}$as in (2.2). Then $S W(\mathcal{L})= \pm G r\left(c_{1}(E)\right)$.
(An outline of the proof is given in the next section; see [T1] for the details.)

There are some simple corollaries concerning the Seiberg-Witten invariants and symplectic curves which follow from this theorem. For example, the first application is simply an existence theorem for symplectic curves:

Proposition 4.2. Let $X$ be as in Theorem 4.1 and let $E$ be a nontrivial complex line bundle for which the associated Spin ${ }_{\mathbb{C}}$ structure (as in (2.2)) has nonzero Seiberg-Witten invariant. Then the Poincaré dual to $c_{1}(E)$ is represented by the fundamental class of an embedded, symplectic curve which consists of some number $N$ of components. Let $\Sigma$ be any such component, let $g=\operatorname{genus}(\Sigma)$ and let $e \in H^{2}(X ; \mathbb{Z})$ be the Poincaré dual to the fundamental class of $\Sigma$. Then $g=1+e \cdot e$. In particular, the Poincaré dual to $c_{1}(K)$ is represented by a symplectic curve. Also, if $X$ has no embedded spheres of self-intersection -1 , then $c_{1}(K) \cdot c_{1}(K) \geq 0$.

Proposition 4.3. Symplectic manifolds as in Theorem 4.1 have "simple type" in the sense that the nonzero Seiberg-Witten invariants are found only for $\operatorname{Spin}_{\mathbb{C}}$ structures $\mathcal{L}$ for which the dimension $d$ in (1.8) (or, equivalently, (2.4)) is equal to zero.

The proof that $d$ in (2.4) is zero for line bundles $E$ with $c_{1}(E) \cdot c_{1}(E) \geq$ 0 and $S W$ nonzero employs the usual adjunction formula of (3.2) along with the generalized adjunction inequalities from [KM] and [MST]. The latter assert the following: let $X$ be a compact, oriented 4-manifold with $b_{2}^{+}>1$ and let $e^{\prime} \in H^{2}(X ; \mathbb{Z})$ have nonnegative $e^{\prime} \cdot e^{\prime}$. Define $g^{\prime}$ to be the minimal genus of an embedded surface whose fundamental class represents the Poincaré dual to $e^{\prime}$. Then $2-2 g^{\prime}+e^{\prime} \cdot e^{\prime} \leq-\left|c_{1}(L) \cdot e^{\prime}\right|$ where $L=\operatorname{det}\left(S_{+}\right)$ for any $\operatorname{Spin}_{\mathbb{C}}$ structure with nonzero $S W$ invariant.

Proposition 4.4. Let $X$ be as in Theorem 4.1, but suppose that $X$ admits no symplectically embedded 2-spheres with self-intersection number -1. Then the signature of the intersection form of $X$ and the Betti numbers of $X$ are constrained by the inequality $-\frac{4}{3}\left(1-b_{1}\right)-\frac{2}{3} b_{2} \leq \operatorname{sign}(X)$.

This last proposition simply combines the previous two with the dimension formula for $d$ in (1.8).

Proposition 4.5. Let $X$ be as in Theorem 4.1 and suppose that $X$ admits an embedded 2-sphere whose fundamental class has Poincaré dual e obeying $e \cdot e=-1$ and $c_{1}(K) \cdot e \neq 0$. Then $X$ admits a symplectically embedded 2-sphere in the same homology class as the original 2-sphere.

The proof of this last proposition uses the fact that when $X$ admits an embedded sphere of self-intersection -1, there is a diffeomorphism of $X$ which acts on $H_{2}(X ; \mathbb{Z})$ as reflection in the hyperplane orthogonal to the class of the given 2-sphere.

Proposition 4.6. Let $X$ be as in Theorem 4.1 and suppose that $X$ admits no symplectically embedded 2-spheres with self-intersection number -1. Suppose, as well, that $c_{1}(K) \cdot c_{1}(K)=0$. Then any nontrivial line bundle $E$ which corresponds (via (2.2)) to a Spin $_{\mathbb{C}}$ structure $\mathcal{L} \in$ Spin having nonzero Seiberg-Witten invariant is Poincaré dual to a union of disjoint, embedded, symplectic tori (possibly with multiplicities) with zero self-intersection.

The proof of this last proposition also uses the generalized adjunction inequalities from [KM] and [MST]. Indeed, $c_{1}(K)$ is Poincaré dual to the sum of the fundamental classes of a disjoint union of embedded, symplectic tori of square zero. Apply the generalized adjunction formula to each of these tori for the line bundle $L=K^{-1} \otimes E^{2}$ to prove that $c_{1}(K) \cdot c_{1}(E)=0$. This implies (via Proposition 4.3) that $c_{1}(E) \cdot c_{1}(E)=0$ and thus, that $c_{1}(E)$ is also Poincaré dual to a disjoint union of embedded, symplectic tori of square zero. (Use Proposition 4.2.)

As will be outlined in the next subsection, the proofs of the preceding theorems use a 1-parameter deformation of the Seiberg-Witten equations (as in (1.7)) which produces, in the limit, a pseudo-holomorphic curve from the projection of $\psi$ onto the $E$ summand in (2.2). This existence construction works for $b_{2}^{+}=1$ symplectic manifolds also. However, in this case, the value of the Seiberg-Witten invariant can change along the deformation. However, the amount of change can be analyzed.

In particular, when this deformation is applied to the case where $X$ is $\mathbb{C P}^{2}$ with a possibly nonstandard symplectic form, the result is a construction of a pseudo-holomorphic sphere whose fundamental class generates the second homology. With this understood, Theorem B of the introduction is obtained by referring to a theorem of Gromov in [G] which asserts that any such $X$ must be diffeomorphic to the standard $\mathbb{C P}^{2}$ by a diffeomorphism which takes the given symplectic form to a multiple of the Kähler form. The details appear in [T1].

This section ends with the remark that Theorem 4.1 has an analog which can be used to analyze the Seiberg-Witten Floer cohomology of a compact,
oriented 3-manifold $M$ which fibers over the circle. Indeed, there is an equivalence between this Floer theory and a certain symplectic Floer cohomology which can also be defined in this context [F]. The results are reminiscent of the description in [DS] of the $S O(3)$ gauge theoretic Floer cohomology of the same sort of manifold. Anyway, the details here will be described elsewhere [T4].

\section*{5. An outline of the proof of Theorem 4.1}

There are roughly three parts to the proof of Theorem 4.1. The first part produces pseudo-holomorphic submanifolds of $X$ from solutions to the Seiberg-Witten equations in (1.7). The second part (an inverse of sorts to the first) produces solutions to a Seiberg-Witten equation (as in (1.7)) from a pseudo-holomorphic submanifold. The third part combines the constructions in Parts 1 and 2 to produce a demonstration of the stated equivalence between the Seiberg-Witten and Gromov invariants.

Of the three parts above, the first part is technically the hardest by a good margin, while the second part is less difficult. The strategies for the first two parts of the proof are presented below. Part 3 of the proof consists of fairly formal corollaries to the propositions of Parts 1 and 2. Thus, this part of the proof will not be discussed here.

The strategy for Part 1: As remarked earlier, pseudo-holomorphic submanifolds of $X$ are obtained by considering the behavior of solutions to (1.7) where the perturbation form $\mu$ becomes singular in a controllable way as a parameter $r$ gets large. The analysis here has six steps.

Step 1 (The definition of $\mu$ ): Use a metric on $X$ where the symplectic form $\omega$ is self-dual with norm $\sqrt{2}$. With this understood, recall that the canonical $\operatorname{Spin}_{\mathbb{C}}$ structure has its bundle $S_{+}$given by
$$S_{+}=\mathbb{I} \oplus K^{-1} .$$
And, recall from [T2] that the bundle $K^{-1}$ has a unique connection (up to gauge equivalence), $A_{0}$, which is characterized as follows: the composition of the spin covariant derivative with orthogonal projection onto the $\mathbb{I}$ summand in (5.1) defines a covariant derivative, $\nabla_{A_{0}}$, on said summand which annihilates a nowhere-vanishing section. This section, $u_{0}$, can be taken to have unit length.

With the preceding understood, take $r>0$ and consider now the $\operatorname{Spin}_{\mathbb{C}}$ structure in (2.2) and the perturbed Seiberg-Witten equation for the pair $(A, \psi)$ where $A$ is a connection on $L=K^{-1} \otimes E^{2}$ and $\psi$ is a section of $S_{+}=E \oplus\left(K^{-1} \otimes E\right)$ :
$$D_{A} \psi=0 \quad \text { and } \quad P_{+} F_{A}=\frac{1}{4} \tau\left(\psi \otimes \psi^{*}\right)+P_{+} F_{A_{0}}-\frac{i r}{4} \cdot \omega .$$

In analyzing the behavior of the solutions to (5.2) for $r$ large, it proves convenient to rewrite $\psi$ as
$$\psi=r^{1 / 2} \cdot\left(\alpha \cdot u_{0}+\beta\right),$$
where $\alpha$ is a section of $E$ and where $\beta$ is a section of $K^{-1} \otimes E$. Noting that $u_{0}$ is a solution to the Dirac equation $D_{A_{0}} u_{0}=0$, one can rewrite the first equation in (5.2) as
$$\sigma\left(u_{0} \otimes \nabla_{a} \alpha\right)+D_{A} \beta=0,$$
where $\nabla_{a}$ is the induced covariant derivative which is induced on $E$ from the covariant derivatives $\nabla_{A_{0}}$ on $K^{-1}$ and $\nabla_{A}$ on $K^{-1} \otimes E^{2}$. (Note that $F_{a}=2^{-1} \cdot\left(F_{A}-F_{A_{0}}\right)$.) Here, $\sigma$ is the Clifford multiplication map in (1.4).

Step 2 ( $L^{2}$-estimates on $\beta$ ): Act on both sides of (5.4) with $D_{A}$ and commute derivatives to obtain an equality between the covariant Laplacian of the spinor $\psi$ and zero'th order terms which are linear and cubic in $\psi$. (Use (5.2) here to express the bundle curvature in terms of $\psi$ itself.)

Take this latter equation and project onto the $K^{-1} \otimes E^{2}$ summand of (2.2). Then take the $L^{2}$-inner product of the result with $\beta$. An application of integration by parts will yield, with little difficulty, a lemma to the effect that the $L^{2}$ norms of $\nabla_{A} \beta$ and of $r^{1 / 2} \cdot \beta$ are bounded from above by a uniform multiple of $r^{-1 / 2}$ times the $L^{2}$ norm of $\nabla_{a} \alpha$.

These last facts imply that $\alpha$ is almost-"holomorphic" for large $r$ in the sense that the $L^{2}$ norm of the projection of $\nabla_{a} \alpha$ onto $E \otimes T^{0,1}$ is bounded from above by a uniform multiple of $r^{-1 / 2}$ times the projection of $\nabla_{a} \alpha$ on $E \otimes T^{1,0}$. The point is that for large $r$, the section $\alpha$ of $E$ wants to be holomorphic and the section $\beta$ of $K^{-1} \otimes E^{2}$ wants to be zero.

Step 3 ( $L^{2}$ estimates on $\alpha$ ): Take the equation for the covariant Laplacian of $\psi$ and project onto the $E$ summand in (2.2). Take the $L^{2}$ inner product of both sides of this identity with $\alpha \cdot u_{0}$ and integrate by parts. The result is a uniform bound, independent of $r$, of
$$\int\left\{\frac{4}{r}\left|P_{+} F_{a}\right|^{2}+\left|\nabla_{a} \alpha\right|^{2}+\frac{r}{8}\left(1-|\alpha|^{2}\right)^{2}\right\}$$
by a multiple of $c_{1}(K) \cdot c_{1}(E)$. (The existence of such a bound gives another proof of the results in [T2] and [T3].) In fact, the uniform bound on (5.5) is part of a "Bogomolny" energy bound for solutions to (5.2) which is a generalization to (5.2) of an energy bound which was introduced by Witten in [W] for solutions to (1.6).

As $r$ gets large, the uniform bound on (5.5) gives a uniform bound on $r^{1 / 2} \cdot\left(1-|\alpha|^{2}\right)$ and also $\nabla_{a} \alpha$ in the $L^{2}$ sense. Indeed, for large $r,|\alpha|^{2}$ would
like to equal one everywhere, and $\nabla_{a} \alpha$ would like to equal zero everywhere. (One can prove that the latter is small on balls where the former is near 1.) However, both are prevented from vanishing everywhere by the assumption that the bundle $E$ is nontrivial.

In any event, one can conclude that the measure of the set where $|\alpha|^{2}<$ $1 / 2$ is bounded from above by a multiple of $r^{-1}$ for large $r$. (Note that a maximum principle argument which is akin to one in [KM] proves that $|\alpha|$ is uniformly bounded by $1+O\left(r^{-1}\right)$.)

Step 4 (Control of $\alpha^{-1}(0)$ ): The goal here is to obtain a reasonable limit for the sequence of zero sets (i.e., $\alpha^{-1}(0)$ ) for a sequence of $\alpha$ 's given by different values of $r$ as $r$ tends to $\infty$. The key to controlling this limit is a monotonicity formula for the square of the $L^{2}$ norm of $r^{1 / 2} \cdot\left(1-|\alpha|^{2}\right)$ and also of $\nabla_{a} \alpha$ in balls of radius $s>0$. The aim here is to prove that this local energy grows at least as fast as $s^{2}$ when $\alpha$ vanishes at the center of the ball. (The estimates must be uniform in $r$.) The existence of such a monotonicity formula readily implies that the sequence of zero sets for a sequence of $\alpha$ 's as $r \rightarrow \infty$ converges nicely on $X$. Indeed, the zero sets are constrained as $r$ gets large for the following reason. The monotonicity estimate and the energy bound for (5.5) imply the following: there is a constant $z$ (which is independent of $r$ ) such that for any $\delta>0$, the zero set of $\alpha$ is contained in some number $N(\delta) \leq z \cdot \delta^{-2}$ balls of radius $\delta$ whenever $r$ is sufficiently small.

By the way, the sort of monotonicity formula needed above exists for many types of nonlinear equations. For example, a similar formula plays a key step in the approach of Schoen and Uhlenbeck [SU] to harmonic map regularity. Also, a similar monotonicity formula plays the key role in Uhlenbeck's removable singularity theorem for solutions to the 4-dimensional Yang-Mills equations [U]. In these last examples, the monotonicity formulae are used to control the behavior of singular sets of the relevant nonlinear differential equation.

Step 5 (Pointwise bounds on $F_{a}$ ): In the present context, the proof of the required monotonicity formula requires some extremely delicate $a$ priori bounds for the curvature $F_{a}$. The required bounds for $P_{+} F_{a}$ are direct consequences of the second equation in (5.2). However, $P_{-} F_{a}$ does not directly appear in (5.2); its bounds must come via some other argument.

Miraculously, the exact bound required can be derived via the maximum principle and the equation for $d^{*} d\left(P_{-} F_{a}\right)$. In this regard, note that $d^{*} d P_{-} F_{a}=-d^{*} d P_{+} F_{a}$ from the Bianchi identity $\left(d F_{a}=0\right)$ so (5.2) can be used to control $P_{-} F_{a}$ also. Via a standard Bochner-Weitzenbock formula, the equation for $d^{*} d\left(P_{-} F_{a}\right)$ gives an inequality for the Laplacian of $\left|P_{-} F_{a}\right|$. It is the latter inequality which implies, via the maximum principle, the
required pointwise bound,
$$\left|P_{-} F_{a}\right| \leq \frac{r}{4 \sqrt{2}} \cdot\left(1-|\alpha|^{2}\right)+\text { small, irrelevant term }$$

Step 6 (The pseudo-holomorphic limit): With the bounds on $F_{a}$ coming from (5.2) and (5.6), the monotonicity formula can be proved. As remarked, the latter gives a limit for the zero sets of an $r \rightarrow \infty$ sequence of $\alpha$. It remains yet to prove that this limiting set is pseudo-holomorphic. A dilation argument is used to accomplish this last goal. Indeed, dilation to unit radius of the radius $r^{1 / 2}$ ball about a point in this limit set rescales $r$ out of the picture. The aforementioned a priori estimates for $F_{a}$ show, via reasonably standard elliptic estimates, that the sequence of rescaled fields (corresponding to the unbounded sequence or $r$ values) has a subsequence which converges in the $C^{\infty}$ topology on compact neighborhoods of the given point. Because of the aforementioned small size of $\nabla_{a} \alpha$ 's projection into $E \otimes T^{0,1}$, the limiting $\alpha$ can be shown to be holomorphic on the unit ball in $\mathbb{R}^{4}=\mathbb{C}^{2}$. This last fact can be parlayed into a proof that the limiting zero set has the asserted pseudo-holomorphicity.

The strategy for Part 2: Part 2 of the proof of Theorem 4.1 gives the details for constructing a solution to (5.2) for large $r$ from a pseudoholomorphic submanifold. The idea here is to "graft" a rescaled (by a factor of $r^{1 / 2}$ ), canonical solution of vortex equation on $\mathbb{R}^{2}=\mathbb{C}$ into the normal bundle of the pseudo-holomorphic submanifold. After grafting, the resulting $(A, \psi)$ will almost solve (5.2). (The error in solving (5.2) vanishes in the limit as $r$ tends to $\infty$.)

For large enough $r$, an honest solution to (5.2) can be obtained by correcting the grafted solution by solving a certain first order, inhomogeneous differential equation with small inhomogeneous part. For sufficiently large $r$, a contraction mapping argument (perturbation theory) finds a small solution to this inhomogeneous differential equation provided that the original pseudo-holomorphic submanifold was a smooth point in $H$. (The difference between the honest solution and the grafted solution will tend to zero as $r$ tends to $\infty$.) The strategy here is much like that in [T5] for finding connections on principle $S U(2)$ bundles with self-dual curvature forms.

The canonical vortex equation on $\mathbb{C}$ is an equation for a connection, $A$, (on the trivial bundle) and a complex-valued function $\alpha$. The equations read
$$\bar{\partial}_{A} \alpha=0 \quad \text { and } \quad * i F_{a}=\frac{1}{8}\left(1-|\alpha|^{2}\right) .$$
These equations are supplemented with the boundary conditions:
\begin{itemize}
\item[1)] $|\alpha| \rightarrow 1$ as $|z| \rightarrow \infty$.
\item[2)] The integral of $i F_{a}$ over $\mathbb{C}$ has value $2 \pi$.
\end{itemize}
(A part of the proof of Theorem 4.1 requires considering (5.8.2) with $2 \pi n$ for $n>1$ also.)

\section*{6. Further remarks}

It is observed in [KMT] that there are manifolds with nonzero SeibergWitten invariants which do not admit symplectic forms. (The examples in [KMT] are all non-simply connected and they are connect sums of symplectic manifolds with negative definite manifolds.) With this understood, one is led to ask whether there is any sort of "Gromov invariant" interpretation for the Seiberg-Witten invariants in the nonsymplectic world. The proof of Theorem 4.1 does suggest such an interpretation. Indeed, let $X$ be a compact, oriented 4-manifold with $b_{2}^{+}>0$ and let $\omega$ be a nontrivial, anti-self-dual harmonic 2-form. If $X$ is not symplectic, then this form $\omega$ must vanish at points of $X$. Also, it is not hard to prove that the set where $\omega$ vanishes is, for a sufficiently generic metric, a disjoint union of embedded circles. Anyway, $\omega$ can be thought of as a degenerate symplectic form.

Choose $\mu=-i \cdot r \cdot \omega$ in (1.7). Some of the estimates for Theorem 4.1 can still be derived in this case. These estimates suggest that there is a theory of pseudo-holomorphic submanifolds (in dimension 4) for degenerate symplectic forms. However, at present, the very existence of such a theory, never mind its properties, has yet to be established.

The final remark concerns a different subject-supersymmetric quantum field theories. The Seiberg-Witten equations were discovered by Seiberg and Witten while investigating the physical predictions of a certain postulated supersymmetric quantized Yang-Mills theory [SW1], [SW2]. The analysis here suggests that the relevant quantized gauge field theory is a deformation of some superstring quantum field theory.

\section*{Acknowledgement}

The author wishes to acknowledge his extreme gratitude for the advice, suggestions and support of Tomasz Mrowka.

\section*{References}
\begin{itemize}
\item[] [DS] S. Dostoglu and D. Salamon, Self dual instantons and holomorphic curves, Ann. Math. 139 (1994), 581-640.
\item[] [F] A. Floer, Symplectic fixed points and holomorphic spheres, Commun. Math. Phys. 120 (1989), 575-611.
\item[] [FU] D. Freed and K. K. Uhlenbeck, Instantons and four manifolds, Springer-Verlag New York, 1984.
\item[] [G] M. Gromov, Pseudo-holomorphic curves in symplectic manifolds, Invent. Math. 82 (1985), 307-347.
\end{itemize}
[KM] P. B. Kronheimer and T. S. Mrowka, The genus of embedded surfaces in the projective plane, Math. Res. Letters 1 (1994), 119-124.
[McS] D. McDuff and D. Salamon, $J$-holomorphic curves and quantum cohomolgy, preprint (1994).
[MST] J. Morgan, Z. Szabo and C. H. Taubes, The generalized Thom conjecture, in preparation.
[KMT] D. Kotschick, J. Morgan, C. H. Taubes, Four manifolds without symplectic structures but with nontrivial Seiberg-Witten invariants, Math. Res. Letters 2 (1995), 797-808.
[R] Y. Ruan, Symplectic topology and complex surfaces, in Geometry and topology of complex surfaces (1994), World Scientific.
[SU] R. Schoen and K. K. Uhlenbeck, A regularity theory for harmonic maps, J. Diff. Geo. 17 (1982), 307-335.
[SW1] N. Seiberg and E. Witten, Electromagnetic duality, monopole condensation and confinement in $N=2$ supersymmetric Yang-Mills theory, Nucl. Phys. B426 (1994), 19-52.
[SW2] $\_\_\_\_$, Monopoles, duality and chiral symmetry breaking in $N=2$ supersymmetric QCD, Nucl. Phys. B431 (1994), 581-640.
[T1] C. H. Taubes, in preparation.
[T2] $\_\_\_\_$, The Seiberg-Witten invariants and symplectic forms, Math. Res. Letters 1 (1994), 809-822.
[T3] $\_\_\_\_$, More constraints on symplectic manifolds from Seiberg-Witten equations, Math. Res. Letters 2 (1995), 9-14.
[T4] $\_\_\_\_$, in preparation.
[T5] $\_\_\_\_$, Self-dual connections on non-self-dual 4-manifolds, J. Diff. Geo. 17 (1982), 139-170.
[U] K. K. Uhlenbeck, Removable singularities in Yang-Mills fields, Commun. Math. Phys. 83 (1982), 11-29.
[W] E. Witten, Monopoles and 4-manifolds, Math. Res. Letters 1 (1994), 769-796.