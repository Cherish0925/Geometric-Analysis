---
retention_scope: session
part: 1
total_parts: 2
---

[Part 1/2 of: Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties for Self-Dual, Harmonic 2-Forms]

---
source_file: Seiberg_Witten_invariants_and_pseudo-holomorphic_subvarieties_for_self-dual__har_6a639441dcdb.pdf
converter: mathpix
format: mmd
---

Geometry \& Topology
Volume 3 (1999) 167-210
Published: 4 July 1999

\title{
Seiberg-Witten Invariants and Pseudo-Holomorphic Subvarieties for Self-Dual, Harmonic 2-Forms
}

\author{
Clifford Henry Taubes \\ Department of Mathematics \\ Harvard University \\ Cambridge, MA 02138, USA \\ Email: chtaubes@abel.math.harvard.edu
}

\begin{abstract}
A smooth, compact 4-manifold with a Riemannian metric and $b^{2+} \geq 1$ has a non-trivial, closed, self-dual 2-form. If the metric is generic, then the zero set of this form is a disjoint union of circles. On the complement of this zero set, the symplectic form and the metric define an almost complex structure; and the latter can be used to define pseudo-holomorphic submanifolds and subvarieties. The main theorem in this paper asserts that if the 4-manifold has a non zero Seiberg-Witten invariant, then the zero set of any given self-dual harmonic 2-form is the boundary of a pseudo-holomorphic subvariety in its complement.
\end{abstract}

AMS Classification numbers Primary: 53C07
Secondary: 52C15

Keywords: Four-manifold invariants, symplectic geometry

Proposed: Robion Kirby
Seconded: Gang Tian, Tomasz Mrowka

Received: 26 July 1998
Accepted: 8 May 1999

\section*{1 Introduction}

Let $X$ be a compact, oriented 4-dimensional manifold with Betti number $b^{2+} \geq 1$. Choose a Riemannian metric, $g$, for $X$ and Hodge theory provides a $b^{2+}$-dimensional space of self-dual, harmonic 2-forms. Let $\omega$ be such a self-dual harmonic 2-form. At points where $\omega \neq 0$, the endomorphism $J=\sqrt{2}|\omega|^{-1} g^{-1} \omega$ of $T X$ has square equal to minus the identity and thus defines an almost complex structure. The latter can be used to define, after Gromov [4], the notion of a pseudo-holomorphic curve in the complement of the zero set of $\omega$. This last notion can be generalized with the following definition.

Definition 1.1 Let $Z \subset X$ denote the zero set of $\omega$. A subset $C \subset X-Z$ will be called finite energy, pseudo-holomorphic subvariety when the following requirements are met:
\begin{itemize}
\item[-] There is a complex curve $C_{0}$ (not necessarily compact or connected) together with a proper, pseudo-holomorphic map $\varphi: C_{0} \rightarrow X-Z$ such that $\varphi\left(C_{0}\right)=C$.
\item[-] There is a countable set $\Lambda_{0} \subset C_{0}$ which has no accumulation points and is such that $\varphi$ embeds $C_{0}-\Lambda_{0}$.
\item[-] The integral of $\varphi^{*} \omega$ over $C_{0}$ is finite.
\end{itemize}

When $Z=\emptyset$ and so the form $\omega$ is symplectic, then the main theorem in [15] asserts that pseudo-holomorphic subvarieties exist when the Seiberg-Witten invariants of $X$ are not all zero. (A different sort of existence theorem for pseudo-holomorphic curves has been given by Donaldson [2].)

The purpose of this paper is to provide a generalization of the existence theorem in [15] to the case where $Z \neq \emptyset$. The statement of this generalization is cleanest in the case where $\omega$ vanishes transversely. This turns out to be the generic situation, see eg [9],[5]. In this case $Z$ is a union of embedded circles. The following theorem summarizes the existence theorem in this case.

Theorem 1.2 Let $X$ be a compact, oriented, Riemannian 4-manifold with $b^{2+} \geq 1$ and with a non-zero Seiberg-Witten invariant. Let $\omega$ be a self-dual, harmonic 2-form which vanishes transversely. Then there is a finite energy, pseudo-holomorphic subvariety $C \subset X-Z$ with the property that $C$ has intersection number 1 with every linking 2-sphere of $Z$.

Some comments are in order. In the case where $b^{2+}=1$, the Seiberg-Witten invariants require a choice of "chamber" for their definition. Implicit in the
statement of Theorem 1.1 is that the chamber in question is defined by a perturbation of the equations which is constructed from the chosen form $\omega$. This chamber is described in more detail in the next section.

Here is a second comment: With regard to the sign of the intersection number between $C$ and the linking 2-spheres of $Z$, remark that a pseudo-holomorphic subvariety is canonically oriented at its smooth points by the restriction of $\omega$. Meanwhile, the linking 2-spheres of $Z$ are oriented as follows: First, use the assumed orientation of $T X$ to orient the bundle of self-dual 2 -forms. Second, use the differential of $\omega$ along $Z$ to identify the normal bundle of $Z$ with this same bundle of 2 -forms. This orients the normal bundle to $Z$ and thus $T Z$.

Here is the final comment: Away from $Z$, the usual regularity theorems for pseudo-holomorphic curves (as in [10],[13],[14] or [22]) describe the structure of a finite energy, pseudo-holomorphic subvariety. Basically, such a subvariety is no more singular than an algebraic curve in $\mathbb{C}^{2}$. However, since the almost complex structure $J$ is singular along $Z$, there are serious questions about the regularity near $Z$ of a finite energy, pseudo-holomorphic subvariety. In this regard, [16] provides a first step towards describing the general structure. In [16] the metric is restricted near $Z$ to have an especially simple form and for this restricted metric the story, as developed to date, is as follows: All but finitely many points on $Z$ have a ball neighborhood which the finite energy subvariety intersects in a finite number of disjoint components. Moreover, the closure of each such component in this ball is a smoothly embedded, closed half-disc whose straight edge coincides with $Z$. (There are no obstructions to realizing the special metrics of [16].)

The next section also provides some examples where the subvarieties of Theorem 1.2 are easy to see.

Note that Theorem 2.3, below, gives an existence assertion without assuming the transversality of $\omega$ at zero. Also, Theorem 2.2 below is a stronger version of Theorem 1.2.

This introduction ends with an open problem for the reader (see also [17]).
Problem The proof of Theorem 1.2 suggests that the Seiberg-Witten invariants of any $b^{2+}$ positive 4-manifold can be computed via a creative algebraic count of the finite energy, pseudo-holomorphic subvarieties which (homologically) bound the zero set of a non-trivial, self-dual harmonic form. Such a count is known in the case where the form is nowhere vanishing (see [18],[19]). Another case which is well understood has the product metric on $X=S^{1} \times M$, where $M$ is a compact, oriented, Riemannian 3-manifold with positive first

Betti number ([6],[7],[21]). The problem is to find such a count which applies for any compact, $b^{2+}$ positive 4-manifold.

\section*{2 Basics}

The purpose of this section is to review some of the necessary background for the Seiberg-Witten equations and for the study of pseudo-holomorphic subvarieties.
a) The Seiberg-Witten equations

The Seiberg-Witten equations are discussed in numerous sources to date, so the discussion here will be brief. The novice can consult the book by Morgan [11] or the forthcoming book by Kotschick, Kronheimer and Mrowka [8].

To begin, suppose for the time being that $X$ is an oriented, Riemannian 4-manifold. The chosen metric on $X$ defines the principal SO(4) bundle $F r \rightarrow X$ of oriented, orthonormal frames in $T X$. A spin ${ }^{\mathbb{C}}$ structure on $X$ is a lift (or, more properly, an equivalence class of lifts) of $F r$ to a principal Spin ${ }^{\mathbb{C}}(4)$ bundle $F \rightarrow X$. In this regard the reader should note the identifications
\begin{itemize}
\item[-] $\operatorname{Spin}^{\mathbb{C}}(4)=(S U(2) \times S U(2) \times U(1)) /\{ \pm 1\}$,
\item[-] $S O(4)=(S U(2) \times S U(2)) /\{ \pm 1\}$
\end{itemize}
with the evident group homomorphism from the former to the latter which forgets the factor of $U(1)$ in the top line above. Remark that there exist, in any event Spin ${ }^{\mathbb{C}}$ structures on 4-manifolds. Moreover, the set $\mathcal{S}$ of Spin ${ }^{\mathbb{C}}$ structures is naturally metric independent and has the structure of a principal homogeneous space for the additive group $H^{2}(X ; \mathbb{Z})$.

With the preceding understood, fix a Spin ${ }^{\mathbb{C}}$ structure $F \rightarrow X$. Then $F$ can be used to construct three useful associated vector bundles, $S_{+}, S_{-}$and $L$. The first two are associated via the representations $s_{ \pm}: \operatorname{Spin}^{\mathbb{C}}(4) \rightarrow U(2)=$ $(S U(2) \times U(1)) /\{ \pm 1\}$ which forgets one or the other factor of $S U(2)$ in the top line of (2.1). Thus $S_{ \pm}$are $\mathbb{C}^{2}$ vector bundles over $X$ with Hermitian metrics. Meanwhile, $L=\operatorname{det}\left(S_{+}\right)=\operatorname{det}\left(S_{-}\right)$is associated to $F$ via the representation of Spin ${ }^{\mathbb{C}}(4)$ on $U(1)$ which forgets both factors of $S U(2)$ in the first line of (2.1). (By way of comparison, the $\mathbb{R}^{3}$ bundles $\Lambda_{+}, \Lambda_{-} \rightarrow X$ of self-dual and anti-self-dual 2-forms are associated to $F r$ via the representations of $S O(4)$ to $S O(3)$ which forget one of the other factors of $S U(2)$ in the second line of (2.1).)

Note that the bundle $S_{+} \oplus S_{-}$is a module for the Clifford algebra of $T X$ in the sense that there is an epimorphism cl: $T X \rightarrow \operatorname{Hom}\left(S_{+}, S_{-}\right)$which obeys $c l^{\dagger} c l=-1$. The latter will be thought of equally as a homomorphism from $S_{+} \otimes T X$ to $S_{-}$. Note that this homomorphism induces one, $c l_{+}$, from $\Lambda_{+}$to $\operatorname{End}\left(S_{+}\right)$.

Now consider that the Seiberg-Witten equations constitute a system of differential equations for a pair $(A, \psi)$, where $A$ is a hermitian connection on the complex line bundle $L$ and where $\psi$ is a section of $S_{+}$. These equations read, schematically:
$$\begin{aligned}
D_{A} \psi & =0 \\
F_{A}^{+} & =q(\psi)+\mu .
\end{aligned}$$
In the first line above, $D_{A}$ is the Dirac operator as defined using the connection $A$ and the Levi-Civita connection on $T X$. Indeed, these two connections define a unique connection on $S_{+}$and thus a covariant derivative, $\nabla_{A}$, which takes a section of $S_{+}$and returns one of $S_{+} \otimes T^{*} X$. With this understood, then $D_{A} \psi$ sends the section $\psi$ of $S_{+}$to the section $\operatorname{cl}\left(\nabla_{A} \psi\right)$ of $S_{-}$. In the second line of (2.2), $F_{A}$ is the curvature 2-form of the connection $A$ on $L$, this being an imaginary valued 2-form. Then $F_{A}^{+}$is the projection of $F_{A}$ onto $\Lambda_{+}$. Meanwhile, $q(\cdot)$ is the quadratic map from $S_{+}$to $i \cdot \Lambda_{+}$which, up to a constant factor, sends $\eta \in S_{+}$to the image of $\eta \otimes \eta^{\dagger}$ under the adjoint of $\mathrm{cl}_{+}$. To be more explicit about $q$, let $\left\{e^{\nu}\right\}_{1 \leq \nu \leq 4}$ be an oriented, orthonormal frame for $T^{*} X$. Then $q(\eta)=-8^{-1} \sum_{\nu, \lambda}\left\langle\eta, \operatorname{cl}\left(e^{\nu}\right) \operatorname{cl}\left(e^{\lambda}\right) \eta\right\rangle e^{\nu} \wedge e^{\lambda}$ where $\langle$, denotes the Hermitian inner product on $S_{+}$. Finally, $\mu$ in the second line of (2.2) is a favorite, imaginary valued, self-dual 2-form. (A different choice for $\mu$, as with a different choice for the Riemannian metric, will give a different set of equations.)

\section*{b) The Seiberg-Witten invariants}

Let $Q$ denote the cup product pairing of $H^{2}(X ; \mathbb{R})$ and let $H^{2+} \subset H^{2}(X ; \mathbb{R})$ denote a maximum subspace on which $Q$ is positive definite. Set $b^{2+}=\operatorname{dim}\left(H^{2+}\right)$. Fix an orientation for the real line $\Lambda^{\text {top }} H^{1}(X ; \mathbb{R}) \otimes \Lambda^{\text {top }} H^{2+}$. If $b^{2+}>1$, then the Seiberg-Witten invariants as presented in [23] constitute a diffeomorphism invariant map $S W: \mathcal{S} \rightarrow \mathbb{Z}$. Moreover, there is a straightforward generalization (see [19]) which extends this invariant to
$$S W: \mathcal{S} \rightarrow \Lambda^{*} H^{1}(X ; \mathbb{Z}) .$$
In the case where $b^{2+}=1$, there is a diffeomorphism invariant as in (2.3) after the additional choice of an orientation for the line $H^{2+}$.

In all cases, the map in (2.3) is defined via a creative, algebraic count of the solutions of (2.2). However, the particulars of the definition of $S W$ are not relevant to the discussion in this article except for the following two facts:
\begin{itemize}
\item[-] If $S W(s) \neq 0$, then there exists, for each choice of metric $g$ and perturbing form $\mu$, at least one solution to (2.2) as defined by the Spin ${ }^{\mathbb{C}}$ structure $s$.
\item[-] In the case where $b^{2+}=1$, the orientation of $H^{2+}$ defines a unique self-dual harmonic 2-form $\omega$ up to multiplication by the positive real numbers. With this understood, note that $S W$ in (2.3) is computed by counting solutions to (2.2) in the special case where the perturbation $\mu$ in (2.2) has the form $\mu=-i \cdot r / 4 \cdot \omega+\mu_{0}$, where $\mu_{0}$ is a fixed, imaginary valued 2-form and where $r$ is taken to be very large. That is, the algebraic count of solutions to (2.2) stabilizes as $r$ tends to $+\infty$, and the large $r$ count is defined to be $S W$. (2.4)
\end{itemize}
c) Near the zero set of a self-dual harmonic form

Let $X$ be a compact, oriented, Riemannian 4-manifold with $b^{2+}>0$ and suppose that $\omega$ is a self-dual harmonic 2-form which vanishes transversely. The purpose of this subsection is to describe the local geometry of the zero set $Z \equiv \omega^{-1}(0)$, of the form $\omega$.

To begin, note first that the non-degeneracy condition implies that $Z$ is a union of embedded circles. Moreover, the transversal vanishing of $\omega$ implies that its covariant derivative, $\nabla \omega$, identifies the normal bundle $N \rightarrow Z$ of $Z$ with the bundle $\left.\Lambda_{+}\right|_{Z}$ of self-dual 2-forms. As $\Lambda_{+}$is oriented by the orientation of $X$, the homomorphism $\nabla \omega$ orients $N$ with the declaration that it be orientation reversing. This orientation of $N$ induces one on $Z$ if one adopts the convention that $T X=T Z \oplus N$ (as opposed to $N \oplus T Z$ ).

With $Z$ now oriented, define $\tau: \Lambda_{+} \rightarrow N^{*}$ by the rule $\tau(u) \equiv u\left(\partial_{0}, \cdot\right)$, where the $\partial_{0}$ is the unit length oriented tangent vector to $Z$. Note that $\tau$ is also an isomorphism. Moreover, the composition $\tau \cdot \nabla \omega: N \rightarrow N^{*}$ defines a bilinear form on $N$ with negative determinant. And, as $d \omega=0$, this form is symmetric with trace zero and thus $\tau \cdot \nabla \omega$ has everywhere three real eigenvalues, where two are positive and one is negative. (Note here that $N$ inherits a fiber metric with its identification as the orthogonal complement to $T Z$ in $\left.T X\right|_{Z}$.)

Let $N_{1} \subset N$ denote the one-dimensional eigenbundle for $\tau \cdot \nabla \omega$ which corresponds to the negative eigenvalue. Then use $N_{2} \subset N$ to denote its orthogonal complement. With regard to $N_{1}$, note that this bundle can be either oriented
or not. Gompf has pointed out that $1+b^{2}-b^{1}$ and the number of components of $Z$ for which $N_{1}$ is oriented are equal modulo 2 .

With the Riemannian geometry near $Z$ understood, consider now the almost complex geometry in a neighborhood of $Z$. Here the almost complex structure on $X-Z$ is defined by the endomorphism $J \equiv \sqrt{2} g^{-1} \omega /|\omega|$ with $\omega$ viewed as a skew symmetric homomorphism from $T X$ to $T^{*} X$ and with $g^{-1}$ viewed as a symmetric homomorphism which goes the other way. As $J$ has square equal to minus the identity, $J$ decomposes $\left.T^{*} X\right|_{X-Z} \otimes \mathbb{C}=T^{1,0} \oplus T^{0,1}$, where $T^{1,0}$ are the holomorphic 1-forms and $T^{0,1}$ the anti-holomorphic forms. The canonical line bundle, $K$, for the almost complex structure is $\Lambda^{2} T^{1,0}$.

Note that $J$ does not extend over $Z$. This failure is implied by the following lemma:

Lemma 2.1 Let $\sigma: N \rightarrow X$ denote the metric's exponential map and let $N^{0} \subset N$ be an open ball neighborhood of the zero section which is embedded by $\sigma$. Use $\sigma$ to identify $N^{0}$ with a neighborhood of $Z$ in $X$. Let $p \in Z$ and let $\left.S \subset N^{0}\right|_{p}$ be a 2-sphere with center at zero and oriented in the standard way as $S^{2} \subset \mathbb{R}^{3}$. Then the restriction of $K$ to $S$ has first Chern class equal to 2, and so is non-trivial.

Proof of Lemma 2.1 For simplicity it is enough to consider the case where the two positive eigenvalues of $\tau \cdot \nabla \omega$ are equal to 1 in as much as the Chern class of $K$ is unchanged by continuous deformations of $\omega$ near $Z$ which leave $\omega^{-1}(0)$ unchanged. With this understood, one can choose oriented local coordinates $(t, x, y, z)$ near the given point $p$ so that $p$ corresponds to the origin, $Z$ is the set where $x=y=z=0$ and $d t$ is positive on $Z$ with respect to the given orientation. In these coordinates,
$$\omega=d t \wedge(x d x+y d y-2 z d z)+x d y \wedge d z-y d x \wedge d z-2 z d x \wedge d y .$$
(In these coordinates, the line $N_{1}$ corresponds to the $z$ axis.)
The strategy will be to identify a section of $K$ with nondegenerate zeros on $S$ and compute the Chern class by summing the degrees of these zeros. There are three steps to this strategy. The first step identifies $T^{1,0} \subset T X \otimes \mathbb{C}$ and for this purpose it proves convenient to introduce the functions
\begin{itemize}
\item[-] $f=2^{-1}\left(x^{2}+y^{2}-2 z^{2}\right)$,
\item[-] $h=\left(x^{2}+y^{2}\right) z$,
\item[-] $g=\left(x^{2}+y^{2}+4 z^{2}\right)^{\frac{1}{2}}$.
\end{itemize}

\section*{Geometry and Topology, Volume 3 (1999)}

Also, introduce the standard polar coordinates $\rho=\left(x^{2}+y^{2}\right)^{\frac{1}{2}}$ and $\varphi=$ $\operatorname{Arctan}(y / x)$ for the $x y$-plane. Then $\omega$ can be rewritten as
$$\omega=d t \wedge d f+d \varphi \wedge d h .$$
Moreover, $\left\{d t, g^{-1} d f, \rho d \varphi,(g \rho)^{-1} d h\right\}$ form an oriented orthonormal frame.
With the preceding understood, it follows that $T^{1,0}$ is the span of $\left\{w_{0} \equiv d t+\right.$ $\left.i g^{-1} d f, w_{1} \equiv \rho d \varphi+i(g \rho)^{-1} d h\right\}$ where $\rho \neq 0$.

The second step in the proof produces a convenient section of $K$. In particular, with $T^{1,0}$ identified as above, then $w_{0} \wedge w_{1}$ defines a section of the canonical bundle with constant norm, at least where $\rho \neq 0$. However, this section is singular at $\rho=0$. But the section $\rho w_{0} \wedge w_{1}$ is nonsingular, vanishes on the sphere $S$ only at the north and south poles and has nondegenerate zeros. (Since $w_{0} \wedge w_{1}$ has constant norm it follows that the zeros of $\rho w_{0} \wedge w_{1}$ on $S$ occur only where $\rho=0$ and are necessarily nondegenerate.)

The final step in the proof computes the degrees of the zeros of $\rho w_{0} \wedge w_{1}$. For this purpose, it is convenient to first digress to identify the fiber of $K$ where $\rho=0$. To start the digression, remark that near $\rho=0$, one has $w_{0}=d t-i \varepsilon d z$ and $w_{1}=\rho d \varphi+i \varepsilon d \rho$ to order $\rho$, where $\varepsilon$ is the sign of $z$. This implies that $T^{1,0} \subset T X \otimes \mathbb{C}$ at $\rho=0$ is spanned by the forms $w_{0}=d t-i \varepsilon d z$ and $-i \varepsilon e^{-i \varepsilon \varphi} w_{1}=d x-i \varepsilon d y$. The latter gives $K \subset \Lambda^{2}(T X \otimes \mathbb{C})$ where $\rho=0$ as the span of $w_{0} \wedge(d x-i \varepsilon d y)$.

End the digression. With respect to these trivializations, the section $\rho w_{0} \wedge w_{1}$ near $\rho=0$ behaves to leading order in $\rho$ as $\sim i \varepsilon(x+i \varepsilon y)$. This last observation implies that the chosen section $\rho w_{0} \wedge w_{1}$ has Chern number equal to 2 on $S$ as claimed.
d) Pseudo-holomorphic subvarieties in X-Z

A submanifold $C \subset X-Z$ is pseudo-holomorphic when $J$ maps $T C$ to itself. Note that such submanifolds have a canonical orientation as the form $\omega$ restricts to $T C$ as a nowhere vanishing 2-form.

Here is an equivalent definition of a finite energy, pseudo-holomorphic subvariety of $X-Z$ : The latter, $C$, is characterized by the following conditions:
\begin{itemize}
\item[-] $C$ is closed.
\item[-] There is a countable set, $\Lambda \subset C$, without accumulation points and such that $C-\Lambda$ is a pseudo-holomorphic submanifold.
\item[-] $\int_{C-\Lambda} \omega<\infty$.
\end{itemize}

Note that a finite energy, pseudo-holomorphic subvariety $C$ naturally defines a relative homology class, $[C] \in H_{2}(X, Z ; \mathbb{Z})$. As $H^{2}(X-Z ; \mathbb{Z})$ is the Poincare dual of $H_{2}(X, Z ; \mathbb{Z})$, there is no natural extension of the intersection pairing to $H_{2}(X, Z)$.

Here are some examples of a finite energy, pseudo-holomorphic subvarieties: First, let $M$ be a compact, oriented 3-manifold with $b^{1}>0$. Choose a nonzero class in $H^{1}(X ; \mathbb{Z})$ and find a metric on $M$ for which the chosen class is represented by a harmonic 1-form with transversal zeros. (A generic metric will have this property. See, eg [5].) Let $\nu$ denote the harmonic 1-form. Also, let * denote the Hodge star for the metric on $M$. Now, take $X=S^{1} \times M$ with metric that is the sum of that on $M$ with the metric on $S^{1}$ determined by a Euclidean coordinate $t \in[0,2 \pi]$. Then $\omega=d t \wedge \nu+* \nu$ is a harmonic, self-dual 2-form on $X$ where $Z=S^{1} \times\left\{\nu^{-1}(0)\right\}$. To see a pseudo-holomorphic subvariety, introduce a flow line, $\gamma$, for the vector field which is dual to $\nu$. (Thus, $* \nu$ annihilates $T_{\gamma}$.) Then $C=S^{1} \times \gamma$ is a finite energy, pseudo-holomorphic submanifold if $\gamma$ is either diffeomorphic to a circle or else is a path in $M$ connecting a pair of zeros of $\nu$. Note that when $\gamma$ is a path which connects a pair of zeros to $\nu$, then the resulting $C$ will have intersection number 1 with any linking 2-sphere of the corresponding pair of components of $Z$.

Another example for this same $X$ has $C=S^{1} \times \cup_{i} \gamma_{i}$, where $\left\{\gamma_{i}\right\}$ is a finite set of flow lines for $\nu$ with each $\gamma_{i}$ being either a circle or a path in $M$ connecting a pair of zeros of $\nu$. Note that if the flow lines in the set $\left\{\gamma_{i}\right\}$ precisely pair the zeros of $\nu$, then the resulting pseudo-holomorphic variety $S^{1} \times \cup_{i} \gamma_{i}$ has intersection number 1 with each linking 2-sphere of $Z$ as required by Theorem 1.2.

\section*{e) The existence of pseudo-holomorphic subvarieties}

This subsection states a more detailed existence theorem for finite energy, pseudo-holomorphic subvarieties.

The existence theorem for pseudo-holomorphic subvarieties (Theorem 2.2, below) uses solutions for a particular version of (2.2) to construct the subvariety. Here is the appropriate version: Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and a number $r \geq 1$. Suppose that $\omega$ is a non-trivial, self-dual, harmonic 2-form on $X$ and consider the equations:
\begin{itemize}
\item[-] $D_{A} \psi=0$
\item[-] $F_{A}^{+}=r q(\psi)-i 4^{-1} r \omega$
\end{itemize}
for a pair $(A, \psi)$ consisting of a connection $A$ on the line bundle $L=\operatorname{det}\left(S_{+}\right)$ and a section $\psi$ of $S_{+}$. Note that these equations constitute a version of (2.2), as can be seen by replacing $\psi$ here with $\psi / \sqrt{r}$.

The precise statement of Theorem 2.2 requires the following three part digression to explain some terminology. Part 1 of the digression introduces a numerical invariant for Spin ${ }^{\mathbb{C}}$ structures. For this purpose, let $X$ be a compact, oriented, Riemannian 4-manifold and suppose that $\omega$ a self-dual, harmonic 2-form on $X$. When $s$ is a $\operatorname{Spin}^{\mathbb{C}}$ structure for $X$, let $e_{\omega}(s) \in \mathbb{R}$ denote the evaluation on the fundamental class of $X$ of the cup product of $c_{1}(L)$ with the cohomology class of $\omega$.

Part 2 of the digression introduces the scalar curvature $R_{g}$ for the metric $g$, and also the metric's self-dual Weyl curvature, $W_{g}^{+}$. These tensors can be defined as follows: Since $\Lambda^{2} T^{*} X$ is the bundle associated to the frame bundle via the adjoint representation on the Lie algebra of $S O(4)$, the Riemann curvature tensor canonically defines an endomorphism of $\Lambda^{2} T^{*} X$. Moreover, with respect to the splitting $\Lambda^{2} T^{*} X=\Lambda_{+} \oplus \Lambda_{-}$, this tensor has a $2 \times 2$ block form and the upper block gives an endomorphism of $\Lambda_{+}$. The trace of the latter is $R_{g} / 4$ and the traceless part is $W_{g}^{+}$. (See eg [1].) Also, introduce the volume form, dvol $_{g}$, for the metric $g$.

Part 3 of the digression introduces the notion of an irreducible component of a pseudo-holomorphic subvariety. To appreciate the definition, remember that there is a countable set $\Lambda \subset C$ with no accumulation points and with the property that $C-\Lambda$ is a submanifold. With this understood, an irreducible component of $C$ is the closure of a component of $C-\Lambda$.

End the digression.

Theorem 2.2 Let $X$ be a compact, oriented, Riemannian 4-manifold with $b^{2+} \geq 1$ and let $\omega$ be a self-dual, harmonic 2-form on $X$ which vanishes transversely. Fix a Spin ${ }^{\mathbb{C}}$ structure $s$ and suppose that there exists an unbounded sequence $\left\{r_{n}\right\} \subset[1, \infty)$ with the property that for each $n$, that $r=r_{n}$ version of (2.9) has a solution, $\left(A_{n}, \psi_{n}\right)$. Then, there exists a finite energy, pseudoholomorphic subvariety $C \subset X-Z$ with the following properties:
\begin{itemize}
\item[-] Let $\left\{C_{a}\right\}$ denote the set of irreducible components of $C$. Then there exists a corresponding set of positive integers $\left\{m_{a}\right\}$ such that $2 \Sigma_{a} m_{a}\left[C_{a}\right] \in$ $H_{2}(X, Z ; \mathbb{Z})$ is Poincaré dual to the first Chern class of the line bundle $\left.L \otimes K\right|_{X-Z}$. In particular, this implies that $C$ has intersection number equal to 1 with each linking 2-sphere of $Z$.
\end{itemize}
\begin{itemize}
\item[-] $\int_{C} \omega \leq \zeta e_{\omega}(s)+\zeta \int_{X}|\omega|\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right) d \operatorname{vol}_{g}$. Here, $\zeta$ is a universal constant.
\item[-] For each $n$, let $\alpha_{n} \equiv(4 i)^{-1}\left(c l^{+}(\omega)+2 i\right) \psi_{n}$ and let $\Sigma_{n} \equiv \alpha_{n}^{-1}(0)$. Then
$$\lim _{n \rightarrow \infty}\left\{\sup _{x \in C} \operatorname{dist}\left(x, \Sigma_{n}\right)+\sup _{x \in \Sigma_{n}} \operatorname{dist}(x, C)\right\}=0 .$$
\end{itemize}
Note that Theorem 1.2 follows directly from Theorem 2.2 given the first point in (2.4).

There are also versions of Theorem 2.2 which holds when $\omega$ does not vanish transversely. Here is the simplest of these versions:

Theorem 2.3 Let $X$ be a compact, oriented, Riemannian 4-manifold with $b^{2+} \geq 1$ and let $\omega$ be a self-dual, harmonic 2-form on $X$. Fix a Spin ${ }^{\mathbb{C}}$ structure $s$ with non-zero Seiberg-Witten invariant. Then there exists a finite energy, pseudo-holomorphic subvariety $C \subset X-Z$ with the following properties
\begin{itemize}
\item[-] Let $\left\{C_{a}\right\}$ denote the set of irreducible components of $C$. Then there exists a corresponding set of positive integers $\left\{m_{a}\right\}$ such that $2 \sum_{a} m_{a}\left[C_{a}\right] \in$ $H_{2}(X, Z ; \mathbb{Z})$ is Poincaré dual to the first Chern class of the line bundle $\left.L \otimes K\right|_{X-Z}$.
\item[-] $\left.\int_{C} \omega \leq \zeta e_{\omega}(s)+\zeta \int_{X}|\omega|\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right) d \operatorname{vol}_{g}\right)$. Here, $\zeta$ is a universal constant.
\end{itemize}
Remark that Theorem 2.3 makes no assumptions about the structure of the zero set of $\omega$, but its assumption of a non-zero Seiberg-Witten invariant is more restrictive than the assumption that (2.9) has solutions for an unbounded set of $r$ values. However, a version of Theorem 2.3 with the latter assumption can be proved using the techniques in the subsequent sections if some mild restrictions are assumed about the degree of degeneracy of the zeros of $\omega$. For example, the conclusions of Theorem 2.3 hold if it is assumed that (2.9) has solutions for an unbounded set of $r$ values, and if it is assumed that $\omega^{-1}(0)$ is non-degenerate except at some finite set of points. In any event, these generalizations of Theorem 2.3 will not be presented here.

The remainder of this article is occupied with the proofs of Theorem 2.2 and Theorem 2.3. In this regard, the reader should note that Theorem 2.3 is essentially a corollary of Theorem 2.2 and a non-compact version of Gromov's compactness theorem [4]. Meanwhile, the proof of Theorem 2.2 mimics as much as possible that of Theorem 1.3 in [15] which asserts the equivalent result in the
case where $\omega$ has no zeros. In particular, some familiarity with the arguments in sections 1-6 of [15] and the revised reprint of the same article in [20] will prove helpful. (The revisions of [15] in [20] correct some minor errors in the original.) The final arguments for Theorem 2.2 are given in Section 7 below.

\section*{f) The proof of Theorem 2.3}

If $s$ has non-zero Seiberg-Witten invariant, then there is a $C^{2}$ neighborhood of the given metric on $X$ such that for all $r$ sufficiently large and for each metric in this neighborhood, the corresponding version of (2.9) has a solution. With this understood, take a sequence of metrics $\left\{g_{\nu}\right\}_{\nu=1,2, \ldots}$ with the following properties
\begin{itemize}
\item[-] For each $g_{\nu}$, there is a self-dual, harmonic form $\omega_{\nu}$ which vanishes transversely.
\item[-] The sequence $\left\{g_{\nu}\right\}$ converges to the given metric $g$ in the $C^{\infty}$ topology as $\nu \rightarrow \infty$.
\item[-] The corresponding sequence $\left\{\omega_{\nu}\right\}$ converges to $\omega$.
\end{itemize}
The existence of such a sequence can be proved as in [5] or [9].
Now invoke Theorem 2.2 for each metric $g_{\nu}$ and the corresponding form $\omega_{\nu}$. Theorem 2.2 produces for each index $\nu$ a finite energy, pseudo-holomorphic variety $C_{\nu}$. Moreover, Theorem 2.2 finds a uniform energy bound for each $C_{\nu}$.

Theorem 2.3's subvariety $C$ is now obtained as a limit of the sequence $\left\{C_{\nu}\right\}$. The limit is found via a non-compact version of the Gromov compactness theorem (in [4]) for pseudo-holomorphic curves. The particular non-compact version is given by Proposition 3.8 in [16]. (The compact case of Gromov's compactness theorem is discussed in detail by numerous authors, for example [13],[14],[10] and [22].)

\section*{3 Integral and pointwise bounds}

The geometric context for this section is as follows: Here $X$ is a compact, oriented, Riemannian 4-manifold with a self-dual harmonic 2-form $\omega$ which vanishes transversely. Also assume that $|\omega| \leq \sqrt{2}$ everywhere. Now fix a Spin ${ }^{\mathbb{C}}$ structure $s$ and for $r \geq 1$, introduce the perturbed Seiberg-Witten equations as in (2.9).

The purpose of this section is to establish some basic properties of a solution $(A, \psi)$ of this version of (2.9). For the most part, these estimates are local
versions of the estimates in (1.24) of [15] and the arguments below are more or less modified versions of those from section 2 of [15].
Before turning to the details, please take note of the following convention: The Greek letter $\zeta$ will be used to represent the "generic" constant in as much as its value may change each time it appears. One should imagine a suppressed index on $\zeta$ which numbers its appearances. Unless otherwise stated, the value of $\zeta$ is independent of any points in question and, furthermore, $\zeta$ is always independent of the parameter $r$ which appears in (2.10). In general, $\zeta$ depends only on the chosen Spin ${ }^{\mathbb{C}}$ structure and on the Riemannian metric.
A similar convention holds for the symbol $\zeta_{\delta}$ when $\delta$ is given as a specified (minimum) distance to $Z$. That is, various inequalities below will be proved under an assumption that the distance to $Z$ is greater than some a priori value, $\delta$. In these equations, $\zeta_{\delta}$ denotes a generic constant which depends only on the Spin ${ }^{\mathbb{C}}$ structure $s$, the Riemannian metric, and the given $\delta$. Furthermore, the precise value of $\zeta_{\delta}$ is allowed to change each time it appears and so the reader should assume that $\zeta_{\delta}$, like $\zeta$, is implicitly labeled by the order of its appearance.
a) Integral bounds for $|\psi|^{2}$

The purpose of this subsection is to obtain pointwise estimates for the components of the spinor $\psi$. The basis for these estimates is the Bochner-Weitzenboch formula for $D_{A}^{*} D_{A}$ which, when applied to $\psi$, reads
$$\nabla_{A}^{*} \nabla_{A} \psi+4^{-1} R_{g} \psi+2^{-1} c_{+}\left(F_{A}^{+}\right) \psi=0,$$
where $R_{g}$ is the scalar curvature of the Riemannian metric. The strategy below uses this last equation to generate first integral bounds for $\psi$ and then pointwise bounds.

The statement below of these integral bounds requires the reintroduction of the notation of Theorem 2.2. Here are the promised integral bounds:

Lemma 3.1 There is a universal constant $c$ with the following significance: Let $s$ be a Spin ${ }^{\mathbb{C}}$ structure on $X$. Now suppose that $(A, \psi)$ solve (2.9) for the given Spin ${ }^{\mathbb{C}}$ structure and for some $r \geq 1$. Then
$$\int_{X}\left(2^{-\frac{1}{2}}|\omega|-|\psi|^{2}\right)^{2} \leq c r^{-1}\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+r^{-1}\left|R_{g}\right|^{2}\right)|\omega| d v_{0} l_{g}\right)$$
$$\begin{aligned}
\left.\left.\int_{X}|\omega|| | \psi\right|^{2}-2^{-\frac{1}{2}}|\omega| \right\rvert\, & \leq c r^{-1}\left(e_{\omega}(s)\right. \\
& \left.+\int_{X}\left(\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega|+r^{-1}\left|R_{g}\right|^{2}\right) d \operatorname{vol}_{g}\right) .
\end{aligned}$$

Proof of Lemma 3.1 The proof starts with the observation that $c_{1}(L)$ is represented in DeRham cohomology by $i \cdot(2 \pi)^{-1} F_{A}$ and thus $2 \pi e_{\omega}(s)=\int_{X} i F_{A} \wedge \omega$. And, as $\omega$ is self-dual, the latter integral is equal to that of $i F_{A} \wedge \omega$. Thus, line two of (2.9) implies that
$$4 \pi e_{\omega}(s) \geq 2^{-\frac{1}{2}} r \int_{X}|\omega|\left(2^{-\frac{1}{2}}|\omega|-|\psi|^{2}\right) .$$
To proceed, contract both sides of (3.1) with $\psi$. The resulting equation implies a differential inequality which can be written first as
$$2^{-1} d^{*} d|\psi|^{2}+4^{-1} r|\psi|^{2}\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right)+4^{-1} R_{g}|\psi|^{2} \leq 0 .$$
To put this last inequality in useful form, note first that rewriting $|\psi|^{2}$ in its second and fourth appearances produces
$$\begin{aligned}
& 2^{-1} d^{*} d|\psi|^{2}+(4 \sqrt{2})^{-1} r\left(|\omega|\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right)+4^{-1} r\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right)^{2}\right. \\
& \quad+(4 \sqrt{2})^{-1} R_{g}|\omega|+4^{-1} R_{g}\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right) \leq 0 .
\end{aligned}$$
Then an application of the triangle inequality to (3.5) yields
$$\begin{aligned}
2^{-1} d^{*} d|\psi|^{2}+ & (4 \sqrt{2})^{-1} r|\omega|\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right)+8^{-1} r\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right)^{2} \\
& \leq-(4 \sqrt{2})^{-1} R_{g}|\omega|+8^{-1} r^{-1} R_{g}^{2} .
\end{aligned}$$
Integrate this last inequality and compare with (3.3) to obtain the first line in (3.2).

To obtain the second line in (3.2), note that the Weitzenboch formula for the harmonic form $\omega$ (see, eg Appendix C in [3]) implies that
$$d^{*} d|\omega|+|\omega|^{-1}|\nabla \omega|^{2} \leq c\left|\mathcal{W}^{+}\right||\omega|,$$
where $\mathcal{W}^{+}$is a universal curvature endomorphism of $\Lambda_{+}$which is constructed from $R_{g}$ and $W_{g}^{+}$. In any event, with (3.7) understood, introduce $u \equiv|\psi|^{2}$ - $2^{-\frac{1}{2}}|\omega|$. It now follows from (3.7) and (3.2) (with an application of the triangle inequality) that
$$2^{-1} d^{*} d u+4^{-1} r|\omega| u \leq c\left(|\omega|\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)+|\omega|^{-1}|\nabla \omega|^{2}+r^{-1}\left|R_{g}\right|^{2}\right) .$$
Now, integrate this last equation over the domain $\Omega \subset X$ where $u \geq 0$ and then integrate by parts to find that
$$\int_{X}|\omega| u\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right)_{+} \leq c r^{-1} \int_{X}\left(|\omega|\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)+|\omega|^{-1}|\nabla \omega|^{2}+r^{-1}\left|R_{g}\right|^{2}\right) .$$

Here $\left(|\psi|^{2}-2^{-\frac{1}{2}}|\omega|\right)_{+}$is the maximum of zero and $|\psi|^{2}-2^{-\frac{1}{2}}|\omega|$. (The boundary term which appears on the left-hand side from integrating $d^{*} d u$ is non-negative. This is easiest to see when 0 is a regular value of $u$, for in this case the boundary integral is minus that of the outward pointing normal derivative of $u$. And, minus the latter derivative is non-negative as $u \geq 0$ inside $\Omega$ and $u \leq 0$ outside.)

With regard to (3.9), note that $|\omega|^{-1}$ is integrable across $Z$ since $|\omega|$ near $Z$ is bounded from below by a multiple of the distance to $Z$. Moreover, the integral over $X$ of $|\omega|^{-1}|\nabla \omega|^{2}$ can be evaluated by integrating both sides of (3.7). In particular, an integration by parts eliminates the $d^{*} d|\omega|$ integral, and one finds the integral over $X$ of $|\omega|^{-1}|\nabla \omega|^{2}$ bounded by a universal multiple of the integral over $X$ of $|\omega|\left(\left|R_{g}\right|+\left|W_{g}\right|\right)$.

With this last point understood, the second line in (3.2) follows directly from (3.9) and (3.3).
b) Pointwise bounds for $|\psi|^{2}$

The purpose of this subsection is to derive pointwise bounds for $|\psi|^{2}$. These bounds come from (3.4) as well, but this time with the help of the maximum principle. In particular, with the maximum principle, (3.4) immediately gives the bound
$$|\psi|^{2} \leq 1+r^{-1} \sup _{X}\left|R_{g}\right| .$$
(Remember that $|\omega| \leq \sqrt{2}$.) Here are some more refined bounds:
Lemma 3.2 Let $\sigma(\cdot)$ denote the distance function to $Z$. There is a constant $\zeta$ which depends on the Riemannian metric and is such that
$$\begin{aligned}
& |\psi|^{2} \leq 2^{-1}+\zeta r^{-\frac{1}{3}} \\
& |\psi|^{2} \leq 2^{-1}+\zeta r^{-1} \sigma^{-2} .
\end{aligned}$$
The remainder of this section is occupied with the
Proof of Lemma 3.2 Start with the observation that the right-hand side of (3.8) is bounded by $\zeta \sigma^{-1}$, and thus (3.8) implies
$$2^{-1} d^{*} d u+4^{-1} r|\omega| u \leq \zeta \sigma^{-1} .$$
To obtain the first bound in (3.11), introduce a standard bump function,
$$\chi:[0, \infty) \rightarrow[0,1],$$
which is non-increasing, equals 1 on [0,1] and equals 0 on $[2, \infty)$. Given $R>0$ and $r \geq 1$, promote $\chi$ to the function $\chi_{R} \equiv \chi\left(r^{\frac{1}{3}} \sigma / R\right)$ on $X$. Then there is a constant $\zeta_{1}$ such that the function $u^{\prime} \equiv u+\zeta_{1} \chi_{1} \sigma$ obeys the differential inequality
$$2^{-1} d^{*} d u^{\prime}+4^{-1} r|\omega| u^{\prime} \leq \zeta\left(1-\chi_{1 / 2}\right) \sigma^{-1}$$
Then there is a constant $\zeta_{2}$ such that $u^{\prime \prime}=u+\zeta_{1} \chi_{1} \sigma-\zeta_{2} r^{-\frac{1}{3}}$ obeys
$$2^{-1} d^{*} d u^{\prime \prime}+4^{-1} r|\omega| u^{\prime \prime} \leq-4 r^{2 / 3}|\omega| \zeta_{2}+\zeta\left(1-\chi_{1 / 2}\right) \sigma^{-1} \leq 0 .$$
The previous equation and the maximum principle imply the first line in (3.11).
To obtain the second line in (3.11), fix $c \geq 1$ and let $u^{\prime}$ now denote $u-c r^{-1} \sigma^{-2}$. Then (3.12) implies that $u^{\prime}$ obeys the differential inequality
$$2^{-1} d^{*} d u^{\prime}+4^{-1} r|\omega| u^{\prime} \leq-c 4^{-1} \zeta^{-1} \sigma^{-1}+\zeta \sigma^{-1}+\zeta c r^{-1} \sigma^{-4} .$$
(This is because $|\omega| \geq \zeta^{-1} \sigma$ and because $\left|\nabla^{m} \sigma\right| \leq \zeta_{m} \sigma^{1-m}$.) It follows from (3.16) that if $c$ is taken large ( $c \geq 8 \zeta^{2}$ ) and if $\sigma \geq 2 z^{2 / 3} r^{-1 / 3}$, then $2^{-1} d^{*} d u^{\prime}+$ $4^{-1} r|\omega| u^{\prime} \leq 0$. Thus, for $c$ so constrained, the function $u^{\prime}$ cannot take a positive maximum where $\sigma \geq \zeta r^{-1 / 3}$. Moreover the first line of (3.11) insures that $u \leq \zeta r^{-1 / 3}$ where $\sigma=\zeta r^{-1 / 3}$, and so for $c \geq \zeta^{3}$, the function $u^{\prime}$ cannot be positive at all where $\sigma=\zeta r^{-1 / 3}$. This statement implies the second line of (3.11).
c) Writing $\psi=(\alpha, \beta)$ and estimates for $|\beta|^{2}$

To proceed from here, it proves convenient to introduce the components $(\alpha, \beta)$ of $\psi$ as follows:
$$\begin{aligned}
\alpha & \equiv 2^{-1}\left(1+i(\sqrt{2}|\omega|)^{-1} c_{+}(\omega)\right) \psi \\
\beta & \equiv 2^{-1}\left(1-i(\sqrt{2}|\omega|)^{-1} c_{+}(\omega)\right) \psi
\end{aligned}$$
The estimates in this subsection will show that $|\beta|$ is uniformly small away from $Z$. The following lemma summarizes

Proposition 3.1 Fix $\delta>0$ and the Spin ${ }^{\mathbb{C}}$ structure $s$. There are constants $c_{\delta}, \zeta_{\delta} \geq 1$ which depend only on $s, \delta$ and the Riemannian metric and have the following significance: Suppose that $(A, \psi)$ is a solution to (2.9) as defined by $s$ and with $r \geq \zeta_{\delta}$. Then the $\beta$ component of $\psi$ obeys
$$|\beta|^{2} \leq c_{\delta} r^{-1}\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+\zeta_{\delta} r^{-2}$$
at all points of $X$ with distance $\delta$ or greater from $Z$.

The remainder of this subsection is occupied with the
Proof of Proposition 3.1 The estimates for the norm of $\beta$ are obtained using the maximum principle with the projections $2^{-1}\left(1+i(\sqrt{2}|\omega|)^{-1} c_{+}(\omega)\right)$ of (3.1). To start, take the inner product of (3.1) with the spinors $(\alpha, 0)$ and then $(0, \beta)$ to obtain the following schematic equations:
$$\begin{aligned}
2^{-1} d^{*} d|\alpha|^{2}+\left|\nabla_{A} \alpha\right|^{2} & +4^{-1} r|\alpha|^{2}\left(|\alpha|^{2}-2^{-1 / 2}|\omega|+|\beta|^{2}\right) \\
& +\mathcal{R}_{1}(\alpha, \alpha)+\mathcal{R}_{2}(\alpha, \beta)+\mathcal{R}_{3}\left(\alpha, \nabla_{A} \beta\right)=0
\end{aligned}$$
$$\begin{aligned}
2^{-1} d^{*} d|\beta|^{2}+\left|\nabla_{A} \beta\right|^{2} & +4^{-1} r|\beta|^{2}\left(|\beta|^{2}-2^{-1 / 2}|\omega|+|\alpha|^{2}\right) \\
& +\mathcal{P}_{1}(\beta, \beta)+\mathcal{P}_{2}(\beta, \alpha)+\mathcal{P}_{3}\left(\beta, \nabla_{A} \alpha\right)=0
\end{aligned}$$
Here, $\left\{\mathcal{R}_{j}\right\}$ and $\left\{\mathcal{P}_{j}\right\}$ are metric dependent endomorphisms. Also, the covariant derivative (denoted above by $\nabla_{A}$ ) on the $\pm \sqrt{2} i|\omega|$ eigenbundles of the action of $c_{+}(\omega)$ on $S_{+}$are obtained by projecting the spin covariant derivative on $C^{\infty}\left(S_{+}\right)$.

With regard to (3.19), the associated connection for the derivative $\nabla_{A}$ on sections of the $-\sqrt{2} i|\omega|$ eigenbundles of $c_{+}(\omega)$ is, after an appropriate bundle identification, equal to half the difference between $A$ and a certain canonical connection on the line bundle $K^{-1}$. In particular, the associated curvature 2-form for this covariant derivative is half the difference between $F_{A}$ and the curvature of the canonical connection on $K^{-1}$.

The canonical connection on $K^{-1}$ is defined as in [18] and in Section 1c of [15] as follows: There is a unique (up to isomorphism) Spin ${ }^{\mathbb{C}}$ structure for $X-Z$ with the property that the $-\sqrt{2} i|\omega|$ eigensubbundle for the $c_{+}(\omega)$ action on the corresponding $S_{+}$is a trivial complex line bundle. For this Spin ${ }^{\mathbb{C}}$ structure,the corresponding line bundle $L$ is isomorphic to $K^{-1}$. Thus there is a unique connection (up to gauge equivalence) on $K^{-1}$ which makes the induced connection on the $-\sqrt{2} i|\omega|$ subbundle trivial. The latter connection is the canonical one. An alternate definition of the covariant derivative of the canonical connection on $K^{-1}$ uses the natural identification of $K^{-1}$ (as an $\mathbb{R}^{2}$ bundle over $X-Z$ ) as the orthogonal complement in $\Lambda_{+}$of the span of $\omega$. With this identification understood, the covariant derivative of the canonical connection on a section of $K^{-1}$ is the orthogonal projection onto $K^{-1} \otimes T^{*} X$ of the Levi-Civita covariant derivative on $C^{\infty}\left(\Lambda_{+}\right)$.

Likewise the associated curvature 2-form for the covariant derivative $\nabla_{A}$ on sections of the $+\sqrt{2} i|\omega|$ eigenbundle of $c_{+}(\omega)$ is half the sum of the curvatures
of $A$ and the canonical connection on $K^{-1}$. Moreover, after the appropriate bundle identifications, the associated connection is, in a certain sense, half the sum of $A$ and the canonical connection.

In any event, with (3.19) understood, fix $\delta>0$, but small so that it is a regular value for the function $\sigma$. Then consider the second line of (3.19) where the distance to $Z$ is larger than $\delta / 2$. In particular, where $\sigma \geq \delta / 2$ and when $r$ is large $(r \delta \gg 1)$, the equation in the second line of (3.19) for $|\beta|^{2}$ yields the inequality
$$2^{-1} d^{*} d|\beta|^{2}+\left|\nabla_{A} \beta\right|^{2}+(4 \sqrt{2})^{-1} r|\omega||\beta|^{2} \leq \zeta r^{-1} \delta^{-1}\left(|\alpha|^{2}+\left|\nabla_{A} \alpha\right|^{2}\right) .$$
To use this last equation, write $w=\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)$ and then observe that (3.7) and the first line of (3.19) yield (where $\sigma \geq \delta / 2$ ) the inequality
$$\begin{aligned}
2^{-1} d^{*} d(-w)+\left|\nabla_{A} \alpha\right|^{2} & +(4 \sqrt{2})^{-1} r|\omega|(-w)+4^{-1} r w^{2} \\
& \leq \zeta\left(|\alpha|^{2}+\left|\nabla_{A} \beta\right|^{2}+|\beta|^{2}+\delta^{-1}\right) .
\end{aligned}$$
Add a large (say $c_{\delta} \geq 1$ ) multiple of $r^{-1}$ times this last equation to (3.7) to obtain the following inequality at points where $\sigma \geq \delta / 2$
$$2^{-1} d^{*} d\left(|\beta|^{2}-c_{\delta} r^{-1} w\right)+(4 \sqrt{2})^{-1} r|\omega|\left(|\beta|^{2}-c_{\delta} r^{-1} w\right) \leq \zeta_{\delta} r^{-1} .$$
(Remember the convention that $\zeta_{\delta}$ is a constant which depends only on the Spin ${ }^{\mathbb{C}}$ structure $\delta$ and on the Riemannian metric. Furthermore, the precise value of $\zeta_{\delta}$ can change from appearance to appearance.) In particular, there is an $r$-independent constant $\zeta_{\delta} \geq 1$ which guarantees (3.22) when $c_{\delta} \in\left(\zeta_{\delta}, \zeta_{\delta}^{-1} r\right)$. With the preceding understood, (3.22) implies that there exists a constant $\zeta$ which is independent of both $r$ and $\delta$, and is such that the function $u \equiv|\beta|^{2}-c_{\delta} r^{-1} w-4 \sqrt{2} r^{-2} \zeta \zeta_{\delta}$ obeys
$$2^{-1} d^{*} d u+(4 \sqrt{2})^{-1} r|\omega| u \leq 0$$
at all points where $\sigma \geq \delta / 2$ when $r$ is large.
Now, hold (3.23) for the moment and consider that there is a unique, continuous function $v$ which equals 1 where $\sigma \leq \delta / 2$ and satisfies $2^{-1} d^{*} d v+$ $(4 \sqrt{2})^{-1} r|\omega| v=0$ where $\sigma \geq \delta / 2$. Furthermore, $v$ is positive and, as $|\omega| \geq$ $\zeta^{-1} \delta$, this $v$ obeys
$$v \leq \zeta \exp \left(-\sqrt{r}(\sigma-\delta) / \zeta_{\delta}\right) .$$
To see this last bound, note first that the maximum principle implies that $v$ is no greater than the function $v^{\prime}$ which is 1 where $\sigma \leq \delta / 2$ and obeys $2^{-1} d^{*} d v^{\prime}+(4 \sqrt{2})^{-1} r \zeta^{-1} \delta v^{\prime}=0$ where $\sigma \geq \delta / 2$. The value of $v^{\prime}$ at $x$ can
be written as an integral of the derivative of a Green's kernel $G(x, \cdot)$ over the boundary set where $\sigma=\delta / 2$. However, when $m \geq 0$ is a constant, the Green's kernel $G(x, y)$ for the operator $d^{*} d+m^{2}$ obeys the bound
$$\zeta^{-1} \operatorname{dist}(x, y)^{-2} e^{-\zeta m \operatorname{dist}(x, y)} \leq|G(x, y)| \leq \zeta \operatorname{dist}(x, y)^{-2} e^{-m \operatorname{dist}(x, y) / \zeta} .$$
This last bound yields the bound for $v^{\prime}$ by the right-hand side of (3.24).
Now, as Lemma 3.2 insures that $u \leq \zeta \delta$ where $\sigma=\delta / 2$, it follows from the maximum principle that $u-\zeta \delta v$ is non-positive where $\sigma \geq \delta / 2$. This last estimate implies that $|\beta|^{2} \leq c_{\delta} r^{-1} w+\zeta_{\delta} r^{-2}$ at points where $\sigma \geq \delta$ which is the statement of Proposition 3.1.
d) Bounds for the curvature

This subsection modifies the arguments in section 2d of [15] to establish bounds for the curvature $F_{A}$ of the connection part of $(A, \psi)$. In this regard, the estimates for the self-dual part, $F_{A}^{+}$, come directly from (3.10) and the defining equation for $F_{A}^{+}$in the second line of (2.9). In particular, the second line of (2.9) implies that
$$\left|F_{A}^{+}\right|=r(2 \sqrt{2})^{-1}\left(\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)^{2}+2|\beta|^{2}\left(2^{-1 / 2}|\omega|+|\alpha|^{2}\right)+|\beta|^{4}\right)^{1 / 2} .$$
Moreover, with $\delta>0$ specified and with $r$ large, Proposition 3.1 implies the more useful bound $\left.\left|F_{A}^{+}\right|=r(2 \sqrt{2})^{-1}\left(\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+r^{-1} \zeta_{\delta}^{\prime}\right)^{2}+r^{-2} \zeta_{\delta}^{2}\right)^{1 / 2}$ at points where the distance, $\sigma$, to $Z$ is greater than $\delta$. Thus the triangle inequality gives
$$\left|F_{A}^{+}\right| \leq r(2 \sqrt{2})^{-1}\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+\zeta_{\delta}$$
at each point where $\sigma \geq \delta$ and when $r \geq \zeta_{\delta}$.
With the preceding understood, consider next the case of $\left|F_{A}^{-}\right|$. The following proposition summarizes:

Proposition 3.2 Fix a Spin ${ }^{\mathbb{C}}$ structure $s$, and fix $\delta>0$. Then there are constants $\zeta_{\delta}, \zeta_{\delta}^{\prime} \geq 1$ with the following significance: Let $(A, \psi)$ be a solution to the $s$ version of (2.9) where $r \geq \zeta_{\delta}$. Then at points in $X$ with distance $\delta$ or more from $Z$,
$$\left|F_{A}^{-}\right| \leq r(2 \sqrt{2})^{-1}\left(1+\zeta_{d} r^{-1 / 2}\right)\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+\zeta_{\delta}^{\prime}$$
The remainder of this subsection is occupied with the
Proof of Proposition 3.2 The proof is divided into seven steps.
Step 1 This first step states and then proves a bound on the $L^{2}$-norm of $F_{A}^{-}$over the whole of $X$. The following lemma gives this bound plus a second bound for $\left|\nabla_{A} \psi\right|$ and $F_{A}^{+}$which will be exploited in a subsequent step.

Lemma 3.3 There is a constant $\zeta$ which depends only on the metric and on the Spin ${ }^{\mathbb{C}}$ structure and which has the following significance: Let $r \geq 1$ be given and let $(A, \psi)$ be a solution to (2.9) using the $\operatorname{Spin}^{\mathbb{C}}$ structure and $r$. Then
$$\begin{aligned}
& \int_{X}\left|F_{A}\right|^{2} \leq \zeta r \\
& \int_{X}\left(1+\operatorname{dist}(x, \cdot)^{-2}\right)\left(\left|\nabla_{A} \psi\right|^{2}+r^{-1}\left|F_{A}^{+}\right|^{2}\right) \leq \zeta \quad \text { for any point } x \in X .
\end{aligned}$$

Proof of Lemma 3.3 Take the inner product of both sides of (3.1) with $\psi$ to obtain the equation
$$2^{-1} d^{*} d|\psi|^{2}+\left|\nabla_{A} \psi\right|^{2}+8^{-1} r^{-1}\left|F_{A}^{+}\right|^{2} \leq \zeta\left|R_{g}\right|^{2}|\psi|^{2}+i r^{-1}\left\langle F_{A}^{+}, \omega\right\rangle .$$
Here〈,〉denotes the metric inner product on $\Lambda^{2} T^{*} X$. Integration of this last equation over $X$ yields a uniform bound on the $L^{2}$ norms of $\nabla_{A} \psi$ and $F_{A}^{+}$. The first inequality in (3.29) then follows from the fact that the difference between the $L^{2}$ norms of $F_{A}^{+}$and $F_{A}^{-}$is equal to a universal multiple of the evaluation of $c_{1}(L) \cup c_{1}(L)$ on the fundamental class of $X$.

To obtain the second inequality in (3.29), introduce the Green's function for the operator $d^{*} d+1$ with pole at $x$. Multiply both sides of (3.30) with $G(x, \cdot)$ and integrate the result over $X$. Then integrate by parts and use (3.25) to obtain
$$\begin{aligned}
2^{-1}|\psi|^{2}(x)+\zeta^{-1} & \int_{X} \operatorname{dist}(x, \cdot)^{-2}\left(\left|\nabla_{A} \psi\right|^{2}+r^{-1}\left|F_{A}^{+}\right|^{2}\right) \\
& \leq \zeta\left(r^{-1}+\int_{X}\left(\left|\nabla_{A} \psi\right|^{2}+r^{-1}\left|F_{A}^{+}\right|^{2}\right) \leq \zeta .\right.
\end{aligned}$$
This last equation implies the second line in (3.29).
Step 2 This second step derives a differential inequality for $\left|F_{A}^{-}\right|$. This derivation starts as in section 2d of [15]. In particular, (2.14-2.15) in [15] hold in the present case for $\mu=-2^{-1} i F_{A}^{-}$. (The factor of 2 here comes about because the equations in [15] refers not to the connection $A$ on $L$, but to a connection on a line bundle whose square is the tensor product of the canonical bundle with $L$.) Now argue as in the derivation of [15]'s (2.19), to find that $s \equiv\left|F_{A}^{-}\right|$obeys the differential inequality
$$\begin{aligned}
2^{-1} d^{*} d s+4^{-1} r|\alpha|^{2} s \leq & \zeta s+(2 \sqrt{2})^{-1} r\left(\left|\nabla_{A} \alpha\right|^{2}+\left|\nabla_{A} \beta\right|^{2}\right) \\
& +\zeta r\left(|\alpha|^{2}+|\beta|^{2}+|\alpha|\left|\nabla_{A} \beta\right|+|\beta|\left|\nabla_{A} \alpha\right|\right) .
\end{aligned}$$

Note that this last equation holds everywhere on $X$. (Since $s$ is not necessarily $C^{2}$ where $s=0$, one should technically interpret (3.32) as an inequality between distributions on the space of positive functions. However, this and similar technicalities below have no bearing on the subsequent arguments. Readers who are uncomfortable with this assertion can replace $s$ in (3.32) and below by $\left(\left|F_{A}^{-}\right|^{2}+1\right)^{1 / 2}$ without affecting the arguments.)

Step 3 This step uses (3.32) to bound $s$ by $\zeta r$ everywhere on $X$ when $r \geq \zeta$. To obtain such a bound, multiply both sides of (3.32) by the Green's function $G(x, \cdot)$ for the operator $d^{*} d+1$. Integrate the resulting inequality over $X$ and integrate by parts to obtain
$$s(x)+r \int_{X}|\alpha|^{2} s \cdot \operatorname{dist}(x, \cdot)^{-2} \leq \zeta \int_{X} s \operatorname{dist}(x, \cdot)^{-2}+\zeta r .$$
Here (3.25) has been used. Also, the first line of (3.29) has been invoked to bound the integral over $X$ of $s$ by $r^{1 / 2}$. In addition, the second line of (3.29) has been invoked to bound the product of $G(x, \cdot)$ with $\left|\nabla_{A} \psi\right|^{2}$.

To make further progress, fix $R>0$ and break the integral on the right side of (3.33) into the part where $\operatorname{dist}(x, \cdot) \geq R$ and the complementary region. With this done, (3.33) is seen to imply that
$$\sup _{X} s+r \int_{X}|\alpha|^{2} s \cdot \operatorname{dist}(x, \cdot)^{-2} \leq \zeta R^{-2} r^{1 / 2}+\zeta R^{2} \sup _{X} s+\zeta r .$$
With $R=2^{-1} \zeta^{-1 / 2}$, this last line gives the claimed bound
$$\sup _{X}\left|F_{A}^{-}\right| \leq \zeta r .$$

Step 4 This step uses (3.32) to derive a simpler differential inequality. To begin, reintroduce $w \equiv 2^{-1 / 2}|\omega|-|\alpha|^{2}$. It then follows from (3.20) and (3.21) that there are constants $\kappa_{1}, \kappa_{2}$ and $\kappa_{3}$ which depend only on the metric (not on $(A, \psi)$ nor $r$ ) and which have the following significance: Let $q_{0} \equiv(2 \sqrt{2})^{-1} r(1+$ $\left.\kappa_{1} / r\right) w-\kappa_{2} r|\beta|^{2}+\kappa_{3}$ and then the function $\left(s-q_{0}\right)$ obeys $2^{-1} d^{*} d\left(s-q_{0}\right)+$ $4^{-1} r|\alpha|^{2}\left(s-q_{0}\right) \leq \zeta\left(s+r \sigma^{-1}\right)$. Now introduce the function $\left(s-q_{0}\right)_{+} \equiv$ $\max \left(\left(s-q_{0}\right), 1\right)$. The latter function obeys the same differential inequality as does $\left(s-q_{0}\right)$, namely
$$2^{-1} d^{*} d\left(s-q_{0}\right)_{+}+4^{-1} r|\alpha|^{2}\left(s-q_{0}\right)_{+} \leq \zeta\left(s+r \sigma^{-1}\right) .$$
(To verify (3.36), write $\left(s-q_{0}\right)_{+}=2^{-1}\left(\left(s-q_{0}\right)+\left|s-q_{0}\right|\right)$. Also, since (3.36) involves two derivatives of the Lipschitz function $\left|s-q_{0}\right|$, this last equation should be interpreted as an inequality between distributions on the space of
positive functions. As before, such technicalities play no essential role in the subsequent arguments.)

Step 5 Now, fix $\delta>0$ but small enough to be a regular value of $\sigma$. Let $\chi$ denote the bump function in (3.13) and let $\chi^{\delta} \equiv \chi(\sigma(\cdot) / \delta)$. Agree to let $q_{1} \equiv\left(1-\chi^{\delta}\right)\left(s-q_{0}\right)_{+}$. Note that the task now is to bound $q_{1}$ from above.

To begin, multiply both sides of (3.36) by $\left(1-\chi^{\delta}\right)$ to obtain
$$2^{-1} d^{*} d q_{1}+4^{-1} r|\alpha|^{2} q_{1} \leq \zeta_{\delta} r+\left\langle d \chi^{\delta}, d\left(s-q_{0}\right)_{+}\right\rangle$$
at points where $\sigma \geq \delta$. Here〈, 〉denotes the metric inner product. Now observe that the maximum principle insures that $q_{1} \leq q_{2}+q_{3}$, where $q_{2}$ solves the equation
$$2^{-1} d^{*} d q_{2}+(4 \sqrt{2})^{-1} r|\omega| q_{2}=\zeta_{\delta} r+\left\langle d \chi^{\delta}, d\left(s-q_{0}\right)_{+}\right\rangle,$$
where $\sigma \geq \delta$ and $q_{2}=0$ where $\sigma=\delta$. In the mean time, $q_{3}$ obeys
$$2^{-1} d^{*} d q_{3}+4^{-1} r|\alpha|^{2} q_{3}=\zeta_{\delta} 4^{-1} r|w|\left|q_{2}\right|$$
where $\sigma \geq \delta$ and vanishes where $\sigma=\delta$. Here, $\left.w \equiv 2^{-1 / 2}|w| \alpha\right|^{2}$.
Bounds for $\left|q_{2}\right|$ can be found with help of the Green's function, $G(\cdot, \cdot)$ for the operator $2^{-1} d^{*} d+(4 \sqrt{2})^{-1} r|\omega|$ with Dirichlet boundary conditions on the surface $\sigma=\delta$. In particular, since $|\omega| \geq \zeta^{-1} \delta$ standard estimates bound $\left|\nabla^{k} G(x, y)\right|$ for $k=0,1$ at points $x \neq y$ by $\zeta_{\delta}|x-y|^{-2-k} \exp \left(-\sqrt{r}|x-y| / \zeta_{\delta}\right)$. (Since $|\omega| \geq \zeta^{-1} \delta$ where the distance to $Z$ is greater than $\delta$, these standard estimates involve little more than (3.25) and the maximum principle.)

Let $\Delta_{\delta}$ denote the supremum of $\left(s-q_{0}\right)_{+}$where $\sigma \geq \delta$. (Note that (3.25) asserts that $\Delta_{\delta} \leq \zeta_{\delta} r$ in any event.) Then the estimates just given for the Green's function imply that
$$\left|q_{2}\right| \leq \zeta_{\delta}\left(1+r^{-1 / 2} \Delta_{\delta} \exp \left[-\sqrt{r}(\sigma-\delta) / \zeta_{\delta}\right]\right)$$
at points where $\sigma \geq \delta$ and when $r \geq \zeta_{\delta}$.

Step 6 The purpose of this step is to obtain a bound for the supremum norm of $\left|q_{3}\right|$. Such a bound is a part of the assertions of

Lemma 3.4 Given $\delta>0$, there is a constant $\zeta_{\delta} \geq 1$ which is independent of $(A, \psi)$ and $r$ and is such that if $r \geq \zeta_{\delta}$, then the following is true:
$$q_{3} \leq \zeta_{\delta}\left(r^{1 / 2}+r^{-1 / 6} \Delta_{\delta}\right) .$$

This claim will be proved momentarily. Note however that (3.41) leads to a refinement of the bound $\Delta_{\delta} \leq \zeta_{\delta} r$ which came from (3.35):
$$\Delta_{\delta} \leq \zeta_{\delta} r^{1 / 2}$$
when $r \geq \zeta_{\delta}$. To obtain this refinement, remark that according to (3.40) and (3.41),
$$s-q_{0} \leq \zeta_{\delta}\left(r^{1 / 2}+r^{-1 / 6} \Delta_{\delta}\right)$$
at points where $\sigma \geq 2 \delta$ when $r \geq \zeta_{\delta}$. This last estimate implies that $\Delta_{2 \delta} \leq$ $\zeta_{\delta}\left(r^{1 / 2}+r^{-1 / 6} \Delta_{\delta}\right)$. The latter inequality, iterated thrice, reads $\Delta_{8 \delta} \leq z_{8 \delta} r^{1 / 2}(1+$ $r^{-1} \Delta_{\delta}$ ). Now plug in the bound of $\Delta_{\delta}$ by $\zeta_{\delta} r$ from (3.35) to conclude that $\Delta_{8 \delta} \leq z_{8 \delta} r^{1 / 2}$. Replacing $8 \delta$ by $\delta$ gives (3.42).

Proof of Lemma 3.4 Since $q_{3} \geq 0$, this function is no greater than the solution, $u$, to the equation $2^{-1} d^{*} d u=\zeta_{\delta} 4^{-1} r|w|\left(1+r^{-1 / 2} \Delta_{\delta} \exp [-\sqrt{r}(\sigma-\right.$ $\left.\delta) / \zeta_{\delta}\right]$ ) where $\sigma \geq \delta$ with Dirichlet boundary conditions where $\sigma=\delta$. This function $u$ can be bounded using the Green's function for the Laplacian. In particular (3.25) gives
$$\begin{aligned}
u(x) & \leq \zeta_{\delta} \int_{\sigma \geq \delta} \operatorname{dist}(x, \cdot)^{-2} r|w| \\
& \left.+\zeta_{\delta} \Delta_{\delta} \int_{\sigma \geq \delta} \operatorname{dist}(x, \cdot)^{-2} r^{1 / 2}|w| \exp \left[-\sqrt{r}(\sigma-\delta) / \zeta_{\delta}\right]\right)
\end{aligned}$$
Consider the two integrals above separately. To bound the first integral, fix $d>$ 0 but small and break the region of integration into the part where $\operatorname{dist}(x, \cdot) \geq$ $d$, and the complementary region. The integral over the first region is no greater than that of $d^{-2} r|w|$ over the region where $\sigma \geq \delta$. Since the integral of $r|w|$ is uniformly bounded (Lemma 3.1) by some $\zeta_{\delta}$, this first part of the first integral in (3.44) is no greater than $\zeta_{\delta} d^{-2}$. Meanwhile, since $|w| \leq \zeta_{\delta}$, the dist $(x, \cdot) \leq d$ part of the first integral above is no greater than $\zeta_{\delta} r d^{2}$. Thus, taking $d=r^{-1 / 4}$ bounds the first integral in (3.44) by $\zeta_{\delta} r^{1 / 2}$.

Now consider the second integral, and again consider the contributions from the region where $\operatorname{dist}(x, \cdot) \geq d$ and the complementary region. The contribution from the first region is no greater than $\zeta_{\delta} \Delta_{\delta} r^{-1 / 2} d^{-2}$ since $r|w|$ has a uniform bound on its integral. Meanwhile the region where $\operatorname{dist}(x, \cdot) \geq d$ contributes no more than $\zeta_{\delta} \Delta_{\delta} d$. Thus taking $d=r^{-1 / 6}$ bounds the second integral in (3.44) by $\zeta_{\delta} \Delta_{\delta} r^{-1 / 6}$.

Step 7 This step completes the proof of Proposition 3.2 with the help of a pointwise bound on $q_{3}$. To continue the argument, mimic the discussion
surrounding (2.27) and (2.28) of [15] to find constants $\zeta_{\delta}$ and $c_{\delta}$ such that the function
$$v_{1} \equiv w-c_{\delta}|\beta|^{2}+\zeta_{\delta} / r$$
obeys the following properties at points where $\sigma \geq \delta$ and when $r \geq \zeta_{\delta}$.
$$\begin{aligned}
v_{1} & \geq 2^{-1} \zeta_{\delta} / r . \\
v_{1} & \geq w \\
2^{-1} d^{*} d v_{1}+4^{-1} r|\alpha|^{2} v_{1} & \geq 0 .
\end{aligned}$$
With $v_{1}$ understood, note that (3.41) and (3.42) and the second and third lines of (3.47) imply that there exists $\zeta_{\delta} \geq 1$ such that $q_{4} \equiv q_{3}-\zeta_{\delta} r^{1 / 2} v_{1}$ obeys
$$2^{-1} d^{*} d q_{4}+4^{-1} r|\alpha|^{2} q_{4} \leq 4^{-1} r|w|\left|q_{2}\right|$$
where $\sigma \geq \delta$ and $q_{4} \leq 0$ where $|\alpha|^{2} \leq(2 \sqrt{2})^{-1}|\omega|$ and where $\sigma=\delta$. This last point implies (via the maximum principle) that $q_{3}-\zeta_{\delta} r^{1 / 2} v_{1}$ is no greater than the solution $v$ to the differential equation $2^{-1} d^{*} d v+8^{-1} r v=4^{-1} r \zeta_{\delta} \sup \left(\left|q_{2}\right|\right)$ where $\sigma \geq \delta$ with boundary condition $v \geq 0$ where $\sigma=\delta$. In particular, it follows from (3.40) and (3.42) that $v \leq \zeta_{\delta}$ and thus
$$q_{3}-z_{\delta} r^{1 / 2} v_{1} \leq \zeta_{\delta} .$$
This last bound with (3.40), (3.42) and (3.45) complete the arguments for Proposition 3.2.
e) Bounds for $\nabla_{A} \alpha$ and $\nabla_{A} \beta$

This subsection modifies the arguments in section 2e of [15] to obtain pointwise bounds on the covariant derivatives of $\alpha$ and $\beta$. The following proposition summarizes:

Proposition 3.3 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$. Given $\delta>0$, there are constants $\zeta_{\delta}$ and $\zeta_{\delta}^{\prime}$ with the following significance: Let $r \geq \zeta_{\delta}$ and let $(A, \psi)$ be a solution to the $r$ version of (2.9) using the given Spin ${ }^{\mathbb{C}}$ structure. Then at points where the distance to $Z$ is larger than $\delta$, one has
$$\left|\nabla_{A} \alpha\right|^{2}+r\left|\nabla_{A} \beta\right|^{2} \leq \zeta_{\delta} r\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+\zeta_{d}^{\prime} .$$
The remainder of this section is occupied with the
Proof of Proposition 3.3 The arguments for Proposition 3.3 are slight modifications of those for Proposition 2.8 in [15]. In any event, there are three steps to the proof.

Step 1 For applications in a subsequent section, it proves convenient to introduce $\underline{\alpha} \equiv 2^{1 / 2}|\omega|^{-1 / 2} \alpha$. Note that an $r$-independent bound for $\left|\nabla_{A} \underline{\alpha}\right|$ where the distance to $Z$ is greater than $\delta$ gives an $r$-independent bound for $\left|\nabla_{A} \alpha\right|$.

The manipulations that follow assume that the distance to $Z$ is greater than $\delta$ and that $r \geq \zeta_{\delta}$ so that Proposition 3.1 and Proposition 3.2 can be invoked.

To begin, note that (3.1) implies an equation for $\underline{\alpha}$ which has the following schematic form:
$$\nabla_{A} * \nabla_{A} \underline{\alpha}+4^{-1} r \kappa^{2} \underline{\alpha}\left(|\underline{\alpha}|^{2}-1\right)+4^{-1} r \underline{\alpha}|\beta|^{2}+\mathcal{R}\left(\underline{\alpha}, \beta, \nabla_{A} \underline{\alpha}, \nabla_{A} \beta\right)=0,$$
where $\mathcal{R}$ is multilinear in its four entries and satisfies $|\mathcal{R}|+|\nabla \mathcal{R}|+\left|\nabla^{2} \mathcal{R}\right| \leq \zeta_{\delta}$. Differentiate this last equation and commute derivatives where appropriate to obtain
$$\begin{aligned}
\nabla_{A} * \nabla_{A}\left(\nabla_{A} \underline{\alpha}\right) & +4^{-1} r \kappa^{2} \nabla_{A} \underline{\alpha}+\mathcal{Q}_{1}(\underline{\alpha}, \beta) \\
& +\mathcal{Q}_{2}\left(\nabla_{A}^{2} \underline{\alpha}, \nabla_{A}^{2} \beta\right)+\mathcal{T}_{1} \nabla_{A} \alpha+\mathcal{T}_{2} \nabla_{A} \beta=0 .
\end{aligned}$$
Here $\left\{\mathcal{Q}_{j}\right\}_{j=1,2}$ are bilinear in their entries. Moreover, $\left|\mathcal{Q}_{j}\right|+\left|\nabla \mathcal{Q}_{j}\right| \leq \zeta_{\delta}$ for $j=1$ and 2. Meanwhile, $\left|\mathcal{T}_{1}\right| \leq \zeta_{\delta}(1+r|w|)$ and $\left|\mathcal{T}_{2}\right| \leq \zeta_{\delta}(1+r|w|)^{1 / 2}$. (The latter bounds use Proposition 3.1 and Proposition 3.2.

Next note that there is a similar equation for $\nabla_{A} \beta$.
$$\begin{aligned}
\nabla_{A} * \nabla_{A}\left(\nabla_{A} \beta\right) & +4^{-1} r \kappa^{2} \nabla_{A} \beta+\mathcal{Q}_{1}^{\prime}(\underline{\alpha}, \beta) \\
& +\mathcal{Q}_{2}^{\prime}\left(\nabla_{A}^{2} \underline{\alpha}, \nabla_{A}^{2} \beta\right)+\mathcal{T}_{1}^{\prime} \nabla_{A} \beta+\mathcal{T}_{2}^{\prime} \nabla_{A} \alpha=0 .
\end{aligned}$$
Here $\left\{\mathcal{Q}_{j}^{\prime}\right\}$ and $\left\{\mathcal{T}_{j}\right\}$ obey the same bounds as their namesakes in (3.51).
Step 2 Take the inner product of (3.51) with $\nabla_{A} \underline{\alpha}$ and that of (3.52) with $\nabla_{A} \beta$. Judicious use of the triangle inequality yields
$$\begin{aligned}
2^{-1} d^{*} d\left|\nabla_{A} \underline{\alpha}\right|^{2}+\mid \nabla_{A} & \left.\nabla_{A} \underline{\alpha}\right|^{2}+(4 \sqrt{2})^{-1} r|\omega|\left|\nabla_{A} \underline{\alpha}\right|^{2} \\
& \leq \zeta_{\delta}\left(r^{-1}+(1+r|w|)\left|\nabla_{A} \alpha\right|^{2}+\left|\nabla_{A} \beta\right|^{2}\right)+r^{-1}\left|\nabla_{A} \nabla_{A} \beta\right|^{2}
\end{aligned}$$
$$\begin{aligned}
2^{-1} d^{*} d\left|\nabla_{A} \beta\right|^{2}+\mid \nabla_{A} & \left.\nabla_{A} \beta\right|^{2}+(4 \sqrt{2})^{-1} r|\omega|\left|\nabla_{A} \beta\right|^{2} \\
& \leq \zeta_{\delta}\left(r^{-1}+(1+r|w|)\left|\nabla_{A} \beta\right|^{2}+\left|\nabla_{A} \alpha\right|^{2}\right)+r^{-1}\left|\nabla_{A} \nabla_{A} \alpha\right|^{2}
\end{aligned}$$
Here $r \geq \zeta_{\delta}$ is assumed so that Lemma 3.2 and Proposition 3.1 can be invoked.
Now introduce $y \equiv\left|\nabla_{A} \underline{\alpha}\right|^{2}+r\left|\nabla_{A} \beta\right|^{2}$. By virtue of (3.53), the latter obeys
$$2^{-1} d^{*} d y+(4 \sqrt{2})^{-1} r|\omega| y \leq \zeta_{\delta}\left(1+r\left(\left|\nabla_{A} \alpha\right|^{2}+r\left|\nabla_{A} \beta\right|^{2}\right)\right) .$$

Step 3 Reintroduce the function $w \equiv 2^{-1 / 2}|\omega|-|\underline{\alpha}|^{2}$. It then follows from (3.20) and (3.21) that there are constants $\kappa_{\delta, 1}, \kappa_{\delta, 2}$ and $\kappa_{\delta, 3}$ which depend only on $\delta$ and are such that $y^{\prime} \equiv y-\kappa_{\delta, 1} r w+\kappa_{\delta, 2} r^{2}|\beta|^{2}-\kappa_{\delta, 3}$ obeys
$$2^{-1} d^{*} d y^{\prime}+(4 \sqrt{2})^{-1} r|\omega| y^{\prime} \leq 0$$
where the distance to $Z$ is greater than $\delta$. Now introduce $y_{+}^{\prime} \equiv \max \left(y^{\prime}, 0\right)$ and note that (3.51) is still true with $y_{+}^{\prime}$ replacing $y^{\prime}$, at least as a distribution on the space of positive functions with support where the distance to $Z$ is greater than $\delta$.

With the preceding understood, take the function $\chi$ from (3.13) and set $\chi^{\delta} \equiv$ $\chi(\sigma(\cdot) / \delta)$, where $\sigma$ denotes the distance function to $Z$. Let $G(\cdot, \cdot)$ denote the Green's function for the operator $d^{*} d+(4 \sqrt{2})^{-1} r \zeta|\omega| \delta$, and with $x \in X$ obeying $\sigma(x) \geq 2 \delta$. Here $\zeta$ is chosen so that $|\omega| \geq \zeta \delta$ at all points where $\sigma \geq \delta$. Now multiply both sides of the $y_{+}^{\prime}$ version of (3.51) by $\left(1-\chi^{\delta}\right) G(\cdot, x)$ and integrate the result. Integrate by parts and then use (3.25) to find that
$$y_{+}^{\prime}(x) \leq \zeta_{\delta} \exp \left(-\sqrt{r} / \zeta_{\delta}\right) \int_{X} y_{+}^{\prime} .$$
This last inequality with (3.29) gives (3.49) when $\operatorname{dist}(x, Z) \geq 2 \delta$. Thus, replacing $\delta$ by $\delta / 2$ in (3.56) gives Proposition 3.3.

\section*{4 The monotonicity formula}