# Seiberg–Witten invariants and pseudo-holomorphic subvarieties for self-dual, harmonic 2–forms

- Category: papers
- Identity: doi:10.2140/gt.1999.3.167
- Content status: fulltext_ok

---

---
source_file: math_9907199v1.pdf
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

Here is a second comment: With regard to the sign of the intersection number between $C$ and the linking 2-spheres of $Z$, remark that a pseudo-holomorphic subvariety is canonically oriented at its smooth points by the restriction of $\omega$. Meanwhile, the linking 2-spheres of $Z$ are oriented as follows: First, use the assumed orientation of $T X$ to orient the bundle of self-dual 2-forms. Second, use the differential of $\omega$ along $Z$ to identify the normal bundle of $Z$ with this same bundle of 2-forms. This orients the normal bundle to Z and thus $T Z$.

Here is the final comment: Away from $Z$, the usual regularity theorems for pseudo-holomorphic curves (as in [10],[13],[14] or [22]) describe the structure of a finite energy, pseudo-holomorphic subvariety. Basically, such a subvariety is no more singular than an algebraic curve in $\mathbb{C}^{2}$. However, since the almost complex structure $J$ is singular along $Z$, there are serious questions about the regularity near $Z$ of a finite energy, pseudo-holomorphic subvariety. In this regard, [16] provides a first step towards describing the general structure. In [16] the metric is restricted near $Z$ to have an especially simple form and for this restricted metric the story, as developed to date, is as follows: All but finitely many points on $Z$ have a ball neighborhood which the finite energy subvariety intersects in a finite number of disjoint components. Moreover, the closure of each such component in this ball is a smoothly embedded, closed half-disc whose straight edge coincides with $Z$. (There are no obstructions to realizing the special metrics of [16].)

The next section also provides some examples where the subvarieties of Theorem 1.2 are easy to see.

Note that Theorem 2.3, below, gives an existence assertion without assuming the transversality of $\omega$ at zero. Also, Theorem 2.2 below is a stronger version of Theorem 1.2.

This introduction ends with an open problem for the reader (see also [17]).
Problem The proof of Theorem 1.2 suggests that the Seiberg-Witten invariants of any $b^{2+}$ positive 4-manifold can be computed via a creative algebraic count of the finite energy, pseudo-holomorphic subvarieties which (homologically) bound the zero set of a non-trivial, self-dual harmonic form. Such a count is known in the case where the form is nowhere vanishing (see [18],[19]). Another case which is well understood has the product metric on $X=S^{1} \times M$, where $M$ is a compact, oriented, Riemannian 3 -manifold with positive first

Betti number ([6],[7],[21]). The problem is to find such a count which applies for any compact, $b^{2+}$ positive 4-manifold.

\section*{2 Basics}

The purpose of this section is to review some of the necessary background for the Seiberg-Witten equations and for the study of pseudo-holomorphic subvarieties.
a) The Seiberg-Witten equations

The Seiberg-Witten equations are discussed in numerous sources to date, so the discussion here will be brief. The novice can consult the book by Morgan [11] or the forthcoming book by Kotschick, Kronheimer and Mrowka [8].

To begin, suppose for the time being that $X$ is an oriented, Riemannian 4-manifold. The chosen metric on $X$ defines the principal $\mathrm{SO}(4)$ bundle $F r \rightarrow X$ of oriented, orthonormal frames in $T X$. A spin ${ }^{\mathbb{C}}$ structure on $X$ is a lift (or, more properly, an equivalence class of lifts) of $F r$ to a principal Spin ${ }^{\mathbb{C}}(4)$ bundle $F \rightarrow X$. In this regard the reader should note the identifications
\begin{itemize}
\item[-] $\operatorname{Spin}^{\mathbb{C}}(4)=(S U(2) \times S U(2) \times U(1)) /\{ \pm 1\}$,
\item[-] $S O(4)=(S U(2) \times S U(2)) /\{ \pm 1\}$
\end{itemize}
with the evident group homomorphism from the former to the latter which forgets the factor of $U(1)$ in the top line above. Remark that there exist, in any event Spin ${ }^{\mathbb{C}}$ structures on 4-manifolds. Moreover, the set $\mathcal{S}$ of Spin ${ }^{\mathbb{C}}$ structures is naturally metric independent and has the structure of a principal homogeneous space for the additive group $H^{2}(X ; \mathbb{Z})$.

With the preceding understood, fix a Spin ${ }^{\mathbb{C}}$ structure $F \rightarrow X$. Then $F$ can be used to construct three useful associated vector bundles, $S_{+}, S_{-}$and $L$. The first two are associated via the representations $s_{ \pm}: \operatorname{Spin}^{\mathbb{C}}(4) \rightarrow U(2)=$ $(S U(2) \times U(1)) /\{ \pm 1\}$ which forgets one or the other factor of $S U(2)$ in the top line of (2.1). Thus $S_{ \pm}$are $\mathbb{C}^{2}$ vector bundles over $X$ with Hermitian metrics. Meanwhile, $L=\operatorname{det}\left(S_{+}\right)=\operatorname{det}\left(S_{-}\right)$is associated to $F$ via the representation of $\operatorname{Spin}^{\mathbb{C}}(4)$ on $U(1)$ which forgets both factors of $S U(2)$ in the first line of (2.1). (By way of comparison, the $\mathbb{R}^{3}$ bundles $\Lambda_{+}, \Lambda_{-} \rightarrow X$ of self-dual and anti-self-dual 2 -forms are associated to $F r$ via the representations of $S O(4)$ to $S O(3)$ which forget one of the other factors of $S U(2)$ in the second line of (2.1).)

Note that the bundle $S_{+} \oplus S_{-}$is a module for the Clifford algebra of $T X$ in the sense that there is an epimorphism $c l: T X \rightarrow \operatorname{Hom}\left(S_{+}, S_{-}\right)$which obeys $c l^{\dagger} c l=-1$. The latter will be thought of equally as a homomorphism from $S_{+} \otimes T X$ to $S_{-}$. Note that this homomorphism induces one, $c l_{+}$, from $\Lambda_{+}$to $\operatorname{End}\left(S_{+}\right)$.

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
\item[-] If $S W(s) \neq 0$, then there exists, for each choice of metric $g$ and perturbing form $\mu$, at least one solution to (2.2) as defined by the $\operatorname{Spin}{ }^{\mathbb{C}}$ structure $s$.
\item[-] In the case where $b^{2+}=1$, the orientation of $H^{2+}$ defines a unique selfdual harmonic 2-form $\omega$ up to multiplication by the positive real numbers. With this understood, note that $S W$ in (2.3) is computed by counting solutions to (2.2) in the special case where the perturbation $\mu$ in (2.2) has the form $\mu=-i \cdot r / 4 \cdot \omega+\mu_{0}$, where $\mu_{0}$ is a fixed, imaginary valued 2-form and where $r$ is taken to be very large. That is, the algebraic count of solutions to (2.2) stabilizes as $r$ tends to $+\infty$, and the large $r$ count is defined to be $S W$. (2.4)
\end{itemize}

\section*{c) Near the zero set of a self-dual harmonic form}

Let $X$ be a compact, oriented, Riemannian 4-manifold with $b^{2+}>0$ and suppose that $\omega$ is a self-dual harmonic 2-form which vanishes transversely. The purpose of this subsection is to describe the local geometry of the zero set $Z \equiv \omega^{-1}(0)$, of the form $\omega$.

To begin, note first that the non-degeneracy condition implies that $Z$ is a union of embedded circles. Moreover, the transversal vanishing of $\omega$ implies that its covariant derivative, $\nabla \omega$, identifies the normal bundle $N \rightarrow Z$ of $Z$ with the bundle $\left.\Lambda_{+}\right|_{Z}$ of self-dual 2 -forms. As $\Lambda_{+}$is oriented by the orientation of $X$, the homomorphism $\nabla \omega$ orients $N$ with the declaration that it be orientation reversing. This orientation of $N$ induces one on $Z$ if one adopts the convention that $T X=T Z \oplus N$ (as opposed to $N \oplus T Z$ ).

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

Also, introduce the standard polar coordinates $\rho=\left(x^{2}+y^{2}\right)^{\frac{1}{2}}$ and $\varphi=$ $\operatorname{Arctan}(y / x)$ for the $x y$-plane. Then $\omega$ can be rewritten as
$$\omega=d t \wedge d f+d \varphi \wedge d h .$$
Moreover, $\left\{d t, g^{-1} d f, \rho d \varphi,(g \rho)^{-1} d h\right\}$ form an oriented orthonormal frame.
With the preceding understood, it follows that $T^{1,0}$ is the span of $\left\{w_{0} \equiv d t+\right.$ $\left.i g^{-1} d f, w_{1} \equiv \rho d \varphi+i(g \rho)^{-1} d h\right\}$ where $\rho \neq 0$.

The second step in the proof produces a convenient section of $K$. In particular, with $T^{1,0}$ identified as above, then $w_{0} \wedge w_{1}$ defines a section of the canonical bundle with constant norm, at least where $\rho \neq 0$. However, this section is singular at $\rho=0$. But the section $\rho w_{0} \wedge w_{1}$ is nonsingular, vanishes on the sphere $S$ only at the north and south poles and has nondegenerate zeros. (Since $w_{0} \wedge w_{1}$ has constant norm it follows that the zeros of $\rho w_{0} \wedge w_{1}$ on $S$ occur only where $\rho=0$ and are necessarily nondegenerate.)

The final step in the proof computes the degrees of the zeros of $\rho w_{0} \wedge w_{1}$. For this purpose, it is convenient to first digress to identify the fiber of $K$ where $\rho=0$. To start the digression, remark that near $\rho=0$, one has $w_{0}=d t-i \varepsilon d z$ and $w_{1}=\rho d \varphi+i \varepsilon d \rho$ to order $\rho$, where $\varepsilon$ is the sign of $z$. This implies that $T^{1,0} \subset T X \otimes \mathbb{C}$ at $\rho=0$ is spanned by the forms $w_{0}=d t-i \varepsilon d z$ and $-i \varepsilon e^{-i \varepsilon \varphi} w_{1}=d x-i \varepsilon d y$. The latter gives $K \subset \Lambda^{2}(T X \otimes \mathbb{C})$ where $\rho=0$ as the span of $w_{0} \wedge(d x-i \varepsilon d y)$.

End the digression. With respect to these trivializations, the section $\rho w_{0} \wedge w_{1}$ near $\rho=0$ behaves to leading order in $\rho$ as $\sim i \varepsilon(x+i \varepsilon y)$. This last observation implies that the chosen section $\rho w_{0} \wedge w_{1}$ has Chern number equal to 2 on $S$ as claimed.

\section*{d) Pseudo-holomorphic subvarieties in X-Z}

A submanifold $C \subset X-Z$ is pseudo-holomorphic when $J$ maps $T C$ to itself. Note that such submanifolds have a canonical orientation as the form $\omega$ restricts to $T C$ as a nowhere vanishing 2-form.

Here is an equivalent definition of a finite energy, pseudo-holomorphic subvariety of $X-Z$ : The latter, $C$, is characterized by the following conditions:
\begin{itemize}
\item[-] $C$ is closed.
\item[-] There is a countable set, $\Lambda \subset C$, without accumulation points and such that $C-\Lambda$ is a pseudo-holomorphic submanifold.
\item[-] $\int_{C-\Lambda} \omega<\infty$.
\end{itemize}

Note that a finite energy, pseudo-holomorphic subvariety $C$ naturally defines a relative homology class, $[C] \in H_{2}(X, Z ; \mathbb{Z})$. As $H^{2}(X-Z ; \mathbb{Z})$ is the Poincare dual of $H_{2}(X, Z ; \mathbb{Z})$, there is no natural extension of the intersection pairing to $H_{2}(X, Z)$.

Here are some examples of a finite energy, pseudo-holomorphic subvarieties: First, let $M$ be a compact, oriented 3 -manifold with $b^{1}>0$. Choose a nonzero class in $H^{1}(X ; \mathbb{Z})$ and find a metric on $M$ for which the chosen class is represented by a harmonic 1-form with transversal zeros. (A generic metric will have this property. See, eg [5].) Let $\nu$ denote the harmonic 1-form. Also, let * denote the Hodge star for the metric on $M$. Now, take $X=S^{1} \times M$ with metric that is the sum of that on $M$ with the metric on $S^{1}$ determined by a Euclidean coordinate $t \in[0,2 \pi]$. Then $\omega=d t \wedge \nu+* \nu$ is a harmonic, self-dual 2-form on $X$ where $Z=S^{1} \times\left\{\nu^{-1}(0)\right\}$. To see a pseudo-holomorphic subvariety, introduce a flow line, $\gamma$, for the vector field which is dual to $\nu$. (Thus, $* \nu$ annihilates $T_{\gamma}$.) Then $C=S^{1} \times \gamma$ is a finite energy, pseudo-holomorphic submanifold if $\gamma$ is either diffeomorphic to a circle or else is a path in $M$ connecting a pair of zeros of $\nu$. Note that when $\gamma$ is a path which connects a pair of zeros to $\nu$, then the resulting $C$ will have intersection number 1 with any linking 2-sphere of the corresponding pair of components of $Z$.

Another example for this same $X$ has $C=S^{1} \times \cup_{i} \gamma_{i}$, where $\left\{\gamma_{i}\right\}$ is a finite set of flow lines for $\nu$ with each $\gamma_{i}$ being either a circle or a path in $M$ connecting a pair of zeros of $\nu$. Note that if the flow lines in the set $\left\{\gamma_{i}\right\}$ precisely pair the zeros of $\nu$, then the resulting pseudo-holomorphic variety $S^{1} \times \cup_{i} \gamma_{i}$ has intersection number 1 with each linking 2-sphere of $Z$ as required by Theorem 1.2.

\section*{e) The existence of pseudo-holomorphic subvarieties}

This subsection states a more detailed existence theorem for finite energy, pseudo-holomorphic subvarieties.

The existence theorem for pseudo-holomorphic subvarieties (Theorem 2.2, below) uses solutions for a particular version of (2.2) to construct the subvariety. Here is the appropriate version: Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and a number $r \geq 1$. Suppose that $\omega$ is a non-trivial, self-dual, harmonic 2-form on $X$ and consider the equations:
\begin{itemize}
\item[-] $D_{A} \psi=0$
\item[-] $F_{A}^{+}=r q(\psi)-i 4^{-1} r \omega$
\end{itemize}
for a pair $(A, \psi)$ consisting of a connection $A$ on the line bundle $L=\operatorname{det}\left(S_{+}\right)$ and a section $\psi$ of $S_{+}$. Note that these equations constitute a version of (2.2), as can be seen by replacing $\psi$ here with $\psi / \sqrt{r}$.

The precise statement of Theorem 2.2 requires the following three part digression to explain some terminology. Part 1 of the digression introduces a numerical invariant for Spin ${ }^{\text {C }}$ structures. For this purpose, let $X$ be a compact, oriented, Riemannian 4-manifold and suppose that $\omega$ a self-dual, harmonic 2-form on $X$. When $s$ is a $\operatorname{Spin}^{\mathbb{C}}$ structure for $X$, let $e_{\omega}(s) \in \mathbb{R}$ denote the evaluation on the fundamental class of $X$ of the cup product of $c_{1}(L)$ with the cohomology class of $\omega$.

Part 2 of the digression introduces the scalar curvature $R_{g}$ for the metric $g$, and also the metric's self-dual Weyl curvature, $W_{g}^{+}$. These tensors can be defined as follows: Since $\Lambda^{2} T^{*} X$ is the bundle associated to the frame bundle via the adjoint representation on the Lie algebra of $S O(4)$, the Riemann curvature tensor canonically defines an endomorphism of $\Lambda^{2} T^{*} X$. Moreover, with respect to the splitting $\Lambda^{2} T^{*} X=\Lambda_{+} \oplus \Lambda_{-}$, this tensor has a 2 × 2 block form and the upper block gives an endomorphism of $\Lambda_{+}$. The trace of the latter is $R_{g} / 4$ and the traceless part is $W_{g}^{+}$. (See eg [1].) Also, introduce the volume form, dvol $_{g}$, for the metric $g$.

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
f) The proof of Theorem 2.3

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
$$\begin{aligned}
\int_{X}\left(2^{-\frac{1}{2}}|\omega|-|\psi|^{2}\right)^{2} & \leq c r^{-1}\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+r^{-1}\left|R_{g}\right|^{2}\right)|\omega| d \operatorname{vol}_{g}\right) \\
\left.\int_{X}|\omega| \|\left.\psi\right|^{2}-2^{-\frac{1}{2}}|\omega| \right\rvert\, & \leq c r^{-1}\left(e_{\omega}(s)\right. \\
& \left.+\int_{X}\left(\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega|+r^{-1}\left|R_{g}\right|^{2}\right) d \operatorname{vol}_{g}\right)
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
& \leq-(4 \sqrt{2})^{-1} R_{g}|\omega|+8^{-1} r^{-1} R_{g}^{2}
\end{aligned}$$
Integrate this last inequality and compare with (3.3) to obtain the first line in (3.2).

To obtain the second line in (3.2), note that the Weitzenboch formula for the harmonic form $\omega$ (see, eg Appendix C in [3]) implies that
$$d^{*} d|\omega|+|\omega|^{-1}|\nabla \omega|^{2} \leq c\left|\mathcal{W}^{+}\right||\omega|,$$
where $\mathcal{W}^{+}$is a universal curvature endomorphism of $\Lambda_{+}$which is constructed from $R_{g}$ and $W_{g}^{+}$. In any event, with (3.7) understood, introduce $u \equiv|\psi|^{2}-$ $2^{-\frac{1}{2}}|\omega|$. It now follows from (3.7) and (3.2) (with an application of the triangle inequality) that
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
$$2^{-1} d^{*} d u+4^{-1} r|\omega| u \leq \zeta \sigma^{-1}$$
To obtain the first bound in (3.11), introduce a standard bump function,
$$\chi:[0, \infty) \rightarrow[0,1],$$
which is non-increasing, equals 1 on [0,1] and equals 0 on $[2, \infty)$. Given $R>0$ and $r \geq 1$, promote $\chi$ to the function $\chi_{R} \equiv \chi\left(r^{\frac{1}{3}} \sigma / R\right)$ on $X$. Then there is a constant $\zeta_{1}$ such that the function $u^{\prime} \equiv u+\zeta_{1} \chi_{1} \sigma$ obeys the differential inequality
$$2^{-1} d^{*} d u^{\prime}+4^{-1} r|\omega| u^{\prime} \leq \zeta\left(1-\chi_{1 / 2}\right) \sigma^{-1}$$
Then there is a constant $\zeta_{2}$ such that $u^{\prime \prime}=u+\zeta_{1} \chi_{1} \sigma-\zeta_{2} r^{-\frac{1}{3}}$ obeys
$$2^{-1} d^{*} d u^{\prime \prime}+4^{-1} r|\omega| u^{\prime \prime} \leq-4 r^{2 / 3}|\omega| \zeta_{2}+\zeta\left(1-\chi_{1 / 2}\right) \sigma^{-1} \leq 0 .$$
The previous equation and the maximum principle imply the first line in (3.11).
To obtain the second line in (3.11), fix $c \geq 1$ and let $u^{\prime}$ now denote $u-c r^{-1} \sigma^{-2}$. Then (3.12) implies that $u^{\prime}$ obeys the differential inequality
$$2^{-1} d^{*} d u^{\prime}+4^{-1} r|\omega| u^{\prime} \leq-c 4^{-1} \zeta^{-1} \sigma^{-1}+\zeta \sigma^{-1}+\zeta c r^{-1} \sigma^{-4}$$
(This is because $|\omega| \geq \zeta^{-1} \sigma$ and because $\left|\nabla^{m} \sigma\right| \leq \zeta_{m} \sigma^{1-m}$.) It follows from (3.16) that if $c$ is taken large ( $c \geq 8 \zeta^{2}$ ) and if $\sigma \geq 2 z^{2 / 3} r^{-1 / 3}$, then $2^{-1} d^{*} d u^{\prime}+$ $4^{-1} r|\omega| u^{\prime} \leq 0$. Thus, for $c$ so constrained, the function $u^{\prime}$ cannot take a positive maximum where $\sigma \geq \zeta r^{-1 / 3}$. Moreover the first line of (3.11) insures that $u \leq \zeta r^{-1 / 3}$ where $\sigma=\zeta r^{-1 / 3}$, and so for $c \geq \zeta^{3}$, the function $u^{\prime}$ cannot be positive at all where $\sigma=\zeta r^{-1 / 3}$. This statement implies the second line of (3.11).
c) Writing $\psi=(\alpha, \beta)$ and estimates for $|\beta|^{2}$

To proceed from here, it proves convenient to introduce the components $(\alpha, \beta)$ of $\psi$ as follows:
$$\begin{aligned}
\alpha & \equiv 2^{-1}\left(1+i(\sqrt{2}|\omega|)^{-1} c_{+}(\omega)\right) \psi \\
\beta & \equiv 2^{-1}\left(1-i(\sqrt{2}|\omega|)^{-1} c_{+}(\omega)\right) \psi
\end{aligned}$$
The estimates in this subsection will show that $|\beta|$ is uniformly small away from $Z$. The following lemma summarizes

Proposition 3.1 Fix $\delta>0$ and the Spin ${ }^{\mathbb{C}}$ structure s. There are constants $c_{\delta}, \zeta_{\delta} \geq 1$ which depend only on $s, \delta$ and the Riemannian metric and have the following significance: Suppose that ( $A, \psi$ ) is a solution to (2.9) as defined by $s$ and with $r \geq \zeta_{\delta}$. Then the $\beta$ component of $\psi$ obeys
$$|\beta|^{2} \leq c_{\delta} r^{-1}\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+\zeta_{\delta} r^{-2}$$
at all points of $X$ with distance $\delta$ or greater from $Z$.

The remainder of this subsection is occupied with the
Proof of Proposition 3.1 The estimates for the norm of $\beta$ are obtained using the maximum principle with the projections $2^{-1}\left(1+i(\sqrt{2}|\omega|)^{-1} c_{+}(\omega)\right)$ of (3.1). To start, take the inner product of (3.1) with the spinors $(\alpha, 0)$ and then $(0, \beta)$ to obtain the following schematic equations:
$$\begin{aligned}
2^{-1} d^{*} d|\alpha|^{2}+\left|\nabla_{A} \alpha\right|^{2} & +4^{-1} r|\alpha|^{2}\left(|\alpha|^{2}-2^{-1 / 2}|\omega|+|\beta|^{2}\right) \\
& +\mathcal{R}_{1}(\alpha, \alpha)+\mathcal{R}_{2}(\alpha, \beta)+\mathcal{R}_{3}\left(\alpha, \nabla_{A} \beta\right)=0
\end{aligned}$$
$2^{-1} d^{*} d|\beta|^{2}+\left|\nabla_{A} \beta\right|^{2}+4^{-1} r|\beta|^{2}\left(|\beta|^{2}-2^{-1 / 2}|\omega|+|\alpha|^{2}\right)$ $+\mathcal{P}_{1}(\beta, \beta)+\mathcal{P}_{2}(\beta, \alpha)+\mathcal{P}_{3}\left(\beta, \nabla_{A} \alpha\right)=0$
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

\section*{d) Bounds for the curvature}

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

Lemma 3.3 There is a constant $\zeta$ which depends only on the metric and on the Spin ${ }^{\text {C }}$ structure and which has the following significance: Let $r \geq 1$ be given and let $(A, \psi)$ be a solution to (2.9) using the Spin ${ }^{\mathbb{C}}$ structure and $r$. Then
$$\begin{aligned}
& \int_{X}\left|F_{A}\right|^{2} \leq \zeta r \\
& \int_{X}\left(1+\operatorname{dist}(x, \cdot)^{-2}\right)\left(\left|\nabla_{A} \psi\right|^{2}+r^{-1}\left|F_{A}^{+}\right|^{2}\right) \leq \zeta \quad \text { for any point } x \in X
\end{aligned}$$

Proof of Lemma 3.3 Take the inner product of both sides of (3.1) with $\psi$ to obtain the equation
$$2^{-1} d^{*} d|\psi|^{2}+\left|\nabla_{A} \psi\right|^{2}+8^{-1} r^{-1}\left|F_{A}^{+}\right|^{2} \leq \zeta\left|R_{g}\right|^{2}|\psi|^{2}+i r^{-1}\left\langle F_{A}^{+}, \omega\right\rangle .$$
Here 〈, 〉denotes the metric inner product on $\Lambda^{2} T^{*} X$. Integration of this last equation over $X$ yields a uniform bound on the $L^{2}$ norms of $\nabla_{A} \psi$ and $F_{A}^{+}$. The first inequality in (3.29) then follows from the fact that the difference between the $L^{2}$ norms of $F_{A}^{+}$and $F_{A}^{-}$is equal to a universal multiple of the evaluation of $c_{1}(L) \cup c_{1}(L)$ on the fundamental class of $X$.

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
$$s(x)+r \int_{X}|\alpha|^{2} s \cdot \operatorname{dist}(x, \cdot)^{-2} \leq \zeta \int_{X} s \operatorname{dist}(x, \cdot)^{-2}+\zeta r$$
Here (3.25) has been used. Also, the first line of (3.29) has been invoked to bound the integral over $X$ of $s$ by $r^{1 / 2}$. In addition, the second line of (3.29) has been invoked to bound the product of $G(x, \cdot)$ with $\left|\nabla_{A} \psi\right|^{2}$.

To make further progress, fix $R>0$ and break the integral on the right side of (3.33) into the part where $\operatorname{dist}(x, \cdot) \geq R$ and the complementary region. With this done, (3.33) is seen to imply that
$$\sup _{X} s+r \int_{X}|\alpha|^{2} s \cdot \operatorname{dist}(x, \cdot)^{-2} \leq \zeta R^{-2} r^{1 / 2}+\zeta R^{2} \sup _{X} s+\zeta r .$$
With $R=2^{-1} \zeta^{-1 / 2}$, this last line gives the claimed bound
$$\sup _{X}\left|F_{A}^{-}\right| \leq \zeta r .$$

Step 4 This step uses (3.32) to derive a simpler differential inequality. To begin, reintroduce $w \equiv 2^{-1 / 2}|\omega|-|\alpha|^{2}$. It then follows from (3.20) and (3.21) that there are constants $\kappa_{1}, \kappa_{2}$ and $\kappa_{3}$ which depend only on the metric (not on $(A, \psi)$ nor $r)$ and which have the following significance: Let $q_{0} \equiv(2 \sqrt{2})^{-1} r(1+$ $\left.\kappa_{1} / r\right) w-\kappa_{2} r|\beta|^{2}+\kappa_{3}$ and then the function $\left(s-q_{0}\right)$ obeys $2^{-1} d^{*} d\left(s-q_{0}\right)+$ $4^{-1} r|\alpha|^{2}\left(s-q_{0}\right) \leq \zeta\left(s+r \sigma^{-1}\right)$. Now introduce the function $\left(s-q_{0}\right)_{+} \equiv$ $\max \left(\left(s-q_{0}\right), 1\right)$. The latter function obeys the same differential inequality as does $\left(s-q_{0}\right)$, namely
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
2^{-1} d^{*} d v_{1}+4^{-1} r|\alpha|^{2} v_{1} & \geq 0
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

Fix a Spin ${ }^{\text {C }}$ structure, a value of $r \geq 1$ and a solution $(A, \psi)$ to the associated version of (2.9). Let $B \subset X$ be an open set, and consider the energy of $B$ :
$$\mathcal{E}_{B} \equiv(4 \sqrt{2})^{-1} r \int_{B}|\omega|\left|\left(2^{-1 / 2}|\omega|-|\psi|^{2}\right)\right| .$$
Note that $\mathcal{E}_{B} \leq \mathcal{E}_{X}<\infty$ by virtue of Lemma 3.1 and the second line of (3.2) in particular. The purpose of this section is to first estimate $\mathcal{E}_{B}$ from the above and from below in the case where $B$ is a geodesic ball of some radius $s>0$. The second purpose will be to exploit the estimates for the energy to refine some of the bounds in the previous section.

\section*{a) Monotonicity}

The following proposition describes the behavior of the energy $\mathcal{E}_{B}$ for the case where $B$ is a geodesic ball in $X$ of some radius $s>0$.

Proposition 4.1 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$. There is a constant $\zeta \geq 1$, and given $\delta>0$, there is a constant $\zeta_{\delta} \geq 1$; and these constants have the following significance: Fix $r \geq \zeta_{\delta}$ and consider a solution $(A, \psi)$ to the version of (2.9) which corresponds to the given Spin ${ }^{\mathbb{C}}$ structure and $r$. Let $B \subset X$ be a geodesic ball with center $x$ whose points all lie at distance $\delta$ or greater from $Z$. Let $s$ denote the radius of $B$ and require $1 / \zeta_{\delta} \geq s \geq 2^{-1} r^{-1 / 2}$. Then:
\begin{itemize}
\item[-] $\mathcal{E}_{B} \leq \zeta s^{2}$
\item[-] If $|\alpha(x)|<(2 \sqrt{2})^{-1}|\omega|$, then $\mathcal{E}_{B} \geq \zeta_{\delta}^{-1} s^{2}$.
\end{itemize}
Proposition 4.1 is proved in the next subsection. Note that this proposition has the following crucial corollary:

Lemma 4.1 Fix a Spin ${ }^{\mathbb{C}}$ structure of $X$. Given $\delta>0$, there is a constant $\zeta_{\delta}>4$ with the following significance: Fix $r \geq \zeta_{\delta}$ and let ( $A, \Psi$ ) be a solution to (2.9) for the given value of $r$ and the given Spin ${ }^{\mathbb{C}}$ structure. Let $\rho \in$ $\left(\zeta_{\delta} r^{-1 / 2}, \zeta_{\delta}^{-1} \delta\right)$. Then
\begin{itemize}
\item[-] Let $\Lambda$ be any set of disjoint balls of radius $\rho$ whose centers lie on $\alpha^{-1}(0)$ and have distance at least $\delta$ from $Z$. Then $\Lambda$ has less than $\zeta_{\delta} \rho^{-2}$ elements.
\item[-] The set of points in $\alpha^{-1}(0)$ with distance at least $\delta$ from $Z$ has a cover by a set $\Lambda$ of no more than $\zeta_{\delta} \rho^{-2}$ balls of radius $\rho$. Moreover, each ball in this set has center on $\alpha^{-1}(0)$ and distance to $Z$ at least $\delta / 2$. Finally, the set of concentric balls of radius $\rho / 2$ is disjoint.
\end{itemize}
Note that Lemma 4.1 plays the role in subsequent arguments that is played by Lemma 3.6 in [15].

Proof of Lemma 4.1 To prove the first assertion, use Proposition 4.1 to conclude that when $r$ is large, then the energy of each ball in the set $\Lambda$ is at least $\zeta_{\delta}^{-1} \rho^{2}$. If there are $N$ such balls and they are all disjoint, then $\mathcal{E}_{X} \geq N \zeta_{d}^{-1} \rho^{2}$. Since $\mathcal{E}_{X} \leq \zeta$, this gives the asserted bound on $N$. The second assertion follows from the first by setting $\Lambda^{\prime}$ to equal a maximal (in number) set of disjoint balls of radius $\rho / 2$ whose centers lie on $\alpha^{-1}(0)$ and have distance at least $\delta / 2$ from $Z$. With $\Lambda^{\prime}$ in hand, set $\Lambda$ equal to the set whose balls are concentric to those in $\Lambda^{\prime}$ but have radius $\rho$.
b) Proof of Proposition 4.1 The first two assertions follow from the following claim: For fixed center $x$, consider $\mathcal{E}_{B}$ as a function of the radius $s$ of $B$. Then
$\mathcal{E}_{B}$ is a differentiable function of $s$ which obeys the inequality:
$$\mathcal{E}_{B} \leq 2^{-1} s\left(1+\zeta_{\delta} s\right)\left(1+\zeta_{\delta} r^{-1 / 2}\right) \frac{d}{d s} \mathcal{E}_{B}+\zeta_{\delta} s^{4}$$
If one is willing to accept (4.3), then the proof of Proposition 4.1 proceeds by copying essentially verbatim that of Proposition 3.1 in [15].

With the preceding understood, the task at hand is to establish (4.3). In this regard, note that the argument for (4.3) is only a slightly modified version of that for Proposition 3.2 in [15]. For this reason, the discussion below is brief.

To begin, remark that because of (2.9), one has
$$\mathcal{E}_{B} \leq \int_{B} \omega \wedge 2^{-1} i F_{A} .$$
Meanwhile, $\omega$ is exact on $B$, so can be written as $d \theta$ for some smooth 1-form on $B$. Thus,
$$\mathcal{E}_{B} \leq 2^{-1} \int_{\partial B} \theta \wedge 2^{-1} i F_{A} .$$
Since $\omega$ is assumed to be nowhere vanishing on $B$, it follows that there is a coordinate system which is centered at $x$ and valid in a ball of radius $\zeta_{\delta}^{-1}$ about $x$ for which $\omega$ pulls back to $\mathbb{R}^{4}$ as the standard form $\omega_{x}=|\omega(x)| \cdot\left(d y^{1} \wedge\right.$ $\left.d y^{2}+d y^{3} \wedge d y^{4}\right)$. Moreover, this coordinate chart can be chosen so that the pulled back metric is close to a constant multiple of the standard Euclidean metric on $\mathbb{R}^{4}$. To be precise, one can require that the metric $g$ differ from $g_{E}=\sum_{j} d y^{j} \otimes d y^{j}$ as follows:
\begin{itemize}
\item[-] $\left|g-g_{E}\right| \leq \zeta_{\delta}|y|$.
\item[-] $|\partial g| \leq \zeta_{\delta}$.
\end{itemize}
Here, $\partial g$ denotes the tensor of $y$-partial derivatives of $g$. Note that the second line in (4.6) implies that the distance $s$ from the origin as measured by the metric $g$ differs from that, $s_{E}$, measured by the Euclidean metric as follows: $\left|s-s_{E}\right| \leq \zeta_{\delta} s^{2}$.

In these coordinates, the choice $\theta=2^{-1}|\omega(x)|\left(y^{1} d y^{2}-y^{2} d y^{1}+y^{3} d y^{4}-y^{4} d y^{3}\right)$ will be made. Note that $|\theta|$ differs from $2^{-1} s$ by no more than $\zeta_{\delta} s^{2}$. With the preceding understood, it follows (as argued in (3.21-24) in [15]) that
$$\mathcal{E}_{B} \leq 2^{-1} s\left(1+\zeta_{\delta} s\right)\left(1+\zeta_{\delta} r^{-1 / 2}\right) 4^{-1} r \int_{\partial B}|\omega(x)|\left|\left(2^{-1}|\omega|-|\alpha|^{2}\right)\right|+\zeta_{\delta} s^{4}$$

Moreover, since $||\omega|-|\omega(x)|| \leq \zeta_{\delta} s|\omega|$ on $\partial B$, the constant factor $|\omega(x)|$ above can be replaced by the variable factor $|\omega|$ at the cost of increasing $\zeta_{\delta}$. Thus, (4.7) implies that
$$\mathcal{E}_{B} \leq 2^{-1} s\left(1+\zeta_{\delta} s\right)\left(1+\zeta_{\delta} r^{-1 / 2}\right) 4^{-1} r \int_{\partial B}|\omega|\left|\left(2^{-1}|\omega|-|\alpha|^{2}\right)\right|+\zeta_{\delta} s^{4}$$
To complete the argument for (4.3), use Proposition 3.1 in the previous section to replace the factor $\left(2^{-1}|\omega|-|\alpha|^{2}\right)$ in (4.8) with $\left(2^{-1}|\omega|-|\psi|^{2}\right)$ at the cost of slightly increasing $\zeta_{\delta}$. The resulting equation is (4.3) after the identification of the $s$ derivative of $\mathcal{E}_{B}$ with the quantity $4^{-1} r \int_{\partial B}|\omega|\left(2^{-1}|\omega|-|\psi|^{2}\right)$.

\section*{a) A refined curvature bound}

The results in Proposition 4.1 about $\mathcal{E}_{B}$ can be used to refine the bound in Proposition 3.2 for $\left|F_{A}^{-}\right|$. The following proposition summarizes:

Proposition 4.2 Fix a Spin ${ }^{\mathbb{C}}$ structure $s$, and fix $\delta>0$. Then, there exist constants $\zeta_{\delta}, \zeta_{\delta}^{\prime} \geq 1$ with the following significance: Let $(A, \psi)$ be a solution to the $s$ version of (2.9) where $r \geq \zeta_{\delta}$. Then, at points in $X$ with distance $\delta$ or more from $Z$,
$$\left|F_{A}^{-}\right| \leq r(2 \sqrt{2})^{-1}\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)+\zeta_{\delta}^{\prime} .$$
The remainder of this section is occupied with the
Proof of Proposition 4.2 The proof amounts to a slight modification of the arguments which prove Proposition 3.4 of [15]. To start, introduce the functions $q_{2}$ and $q_{3}$ as in (3.38) and (3.39). Because of (3.40) and (3.41) one has $\left|q_{2}\right| \leq \zeta_{\delta}$, and so (due to Proposition 3.1's bound on $|\beta|^{2}$ ), it is enough to bound $q_{3}$ by a uniform constant. In this regard, note that $q_{3}$ obeys the equation
$$2^{-1} d^{*} d q_{3}+4^{-1}|\alpha|^{2} q_{3} \leq \zeta_{\delta} r .$$
where $\sigma \geq \delta$ and when $r \geq \zeta_{\delta}$. Also, $q_{3}=0$ where $\sigma=\delta$.
With these last points understood, the key to the proof is the following lemma (compare with Lemma 3.5 in [15]):

Lemma 4.2 Fix a Spin ${ }^{\mathbb{C}}$ structure $s$, and fix $\delta>0$. Then, there is a constant $\zeta_{\delta} \geq 1$ with the following significance: Let $(A, \psi)$ be a solution to the $s$ version of (2.9) where $r \geq \zeta_{\delta}$. Then, there is a smooth function $u$ which is defined on the set of points in $X$ with distance $\delta$ or more from $Z$ and which obeys
\begin{itemize}
\item[] $\bullet|u| \leq \zeta_{\delta}$.
\item[-] $2^{-1} d^{*} d u \geq r$ where $|\alpha| \leq(2 \sqrt{2})^{-1}|\omega|$.
\item[-] $\left|d^{*} d u\right| \leq \zeta_{\delta} r$.
\item[-] $u=0$ where $\sigma=\delta$.
\end{itemize}
The proof of Proposition 4.2 given Lemma 4.2 is essentially the same as that of Proposition 3.4 in [15] given Lemma 3.5 in [15]. Meanwhile, the proof of Lemma 4.1 is a Dirichlet boundary condition version of the proof of Lemma 3.5 in [15]. The modifications to the argument for the latter in [15] are straightforward and left to the reader.

\section*{5 Local properties of $\alpha^{-1}(0)$}

The purpose of this section is to summarize some of the local properties of $\alpha^{-1}(0)$ at points in the complement of $Z$. At issue here is the behavior of $\alpha^{-1}(0)$ at length scales of order $r^{-1 / 2}$.

The strategy for the investigation at such scales is as follows: Fix $\delta>0$ and a point $x$ whose distance from $Z$ is at least $\delta$. A Gaussian coordinate system based at $x$ defines an embedding $h: \mathbb{R}^{4} \rightarrow X$ which maps the origin to $x$ and which sends straight lines through the origin in $\mathbb{R}^{4}$ to geodesics in $X$ through $x$. Moreover, the pull-back via $h$ of the Riemannian metric agrees with the Euclidean metric to second order at the origin. The Gaussian coordinate charts at $x$ are parametrized by the group $S O(4)$ (to be precise, the fiber of the frame bundle at $X$ ). In particular, there are Gaussian coordinate systems at $X$ which pull $\omega$ back as $h^{*} \omega=|\omega(x)|\left(d y^{1} \wedge d y^{2}+d y^{3} \wedge d y^{4}\right)+\mathcal{O}(|y|)$. Such a Gaussian coordinate system will be called a complex Gaussian coordinate system. Indeed, a Gaussian coordinate system at $x$ is called complex precisely when the differential of the corresponding $h$ at the origin intertwines the standard almost complex structure on $\mathbb{R}^{4}=\mathbb{C}^{2}$ with $\left.J\right|_{x}$. The complex Gaussian coordinate systems at $x$ are parametrized by the $U(2)$ subgroup of $S O(4)$.

Now, fix a Spin ${ }^{\mathbb{C}}$ structure on $X$ and $r \geq 1$ and then let ( $A, \psi$ ) be a solution to the corresponding version of (2.9). Then, pull-back by the map $h$ of a Gaussian coordinate system at some $x$ defines $(A, \psi)$ as fields open $\mathbb{R}^{4}$.

Given $\lambda>0$, define the dilation map $\delta_{\lambda}: \mathbb{R}^{4} \rightarrow \mathbb{R}^{4}$ by its action on the coordinate functions $y: \delta_{\lambda}^{*} y=\lambda^{-1} y$. With $x$ chosen in the complement of $Z$
set $\lambda=(r|\omega(x)|)^{1 / 2}$ and let $h$ be a complex Gaussian coordinate system based at $x$. Given $(A, \psi=(\alpha, \beta))$, define the data $(\underline{A},(\underline{\alpha}, \underline{\beta}))$ on $\mathbb{R}^{4}$ by the rule:
$$(\underline{A},(\underline{\alpha}, \underline{\beta})) \equiv \delta_{\lambda}^{*} h^{*}\left(A,|\omega(x)|^{-1 / 2}(\alpha, \beta)\right) .$$
The plan now is to compare ( $\underline{A},(\underline{\alpha}, \underline{\beta})$ ) with some standard objects on $\mathbb{R}^{4}$. These standard objects are discussed in Proposition 4.1 of [15]. The following digression constitutes a brief summary: A connection $a_{0}$ on the trivial complex line bundle over $\mathbb{R}^{4}$ and a section $\alpha_{0}$ of this line bundle will be said to a solution to the Seiberg-Witten equations on $\mathbb{R}^{4}$ when the following conditions hold:
\begin{itemize}
\item[-] The curvature 2-form, $F_{a}$, of $a_{0}$ is of type 1-1 with respect to the standard almost complex structure on $\mathbb{R}^{4}$ and so defines a holomorphic structure (and associated $\bar{\partial}$ operator) on the trivial complex line bundle.
\item[-] The section $\alpha_{0}$ is holomorphic with respect to the $a_{0}$-complex structure on the trivial complex line bundle.
\item[-] $F_{a}^{+}=-i 8^{-1}\left(1-\left|\alpha_{0}\right|^{2}\right)\left(d y^{1} \wedge d y^{2}+d y^{3} \wedge d y^{4}\right)$
\item[-] $\left|\alpha_{0}\right| \leq 1$.
\item[-] $\left|F_{a}^{-}\right| \leq\left|F_{a}^{+}\right| \leq(4 \sqrt{2})^{-1}\left(1-\left|\alpha_{0}\right|^{2}\right)$.
\item[-] $\left|\nabla_{a} \alpha_{0}\right| \leq z\left(1-\left|\alpha_{0}\right|^{2}\right)$.
\item[-] For each $N \geq 1$, the integral of $\left(1-\left|\alpha_{0}\right|^{2}\right)$ over the ball of radius $N$ is bounded by $z N^{2}$. (5.2)
\end{itemize}
Here, $z$ is a constant. (Note that these conditions differ from the conditions listed in (4.3) of [15] in that no assumption on the integrability of $\left|F_{a}^{+}\right|^{2}-\left|F_{a}^{-}\right|^{2}$ is made here. It is most probably true that the latter condition is a consequence of those in (5.2).)

The following proposition summarizes the basic properties of solutions to (5.2):
Proposition 5.1 Let ( $a_{0}, \alpha_{0}$ ) obey the conditions in (5.2). Then:
\begin{itemize}
\item[-] Either $\left|\alpha_{0}\right|<1$ everywhere or else $\left|\alpha_{0}\right|=1$ and $\left(a_{0}, \alpha_{0}\right)$ is gauge equivalent to the trivial solution $\left(a_{0}=0, \alpha_{0}=1\right)$. In the former case, $\alpha_{0}^{-1}(0) \neq \emptyset$ and $\alpha_{0}^{-1}(0)$ is the zero set of a polynomial in the complex coordinates for $\mathbb{R}^{4}=\mathbb{C}^{2}$.
\item[-] Either $\left|F_{a}^{-}\right|<\left|F_{a}^{+}\right|$everywhere or else $\left|F_{a}^{-}\right| \equiv\left|F_{a}^{+}\right|$and there is a $\mathbb{C}$ -linear map $s: \mathbb{C}^{2} \rightarrow \mathbb{C}$ and a solution $\left(a_{1}, \alpha_{1}\right)$ to the vortex equations on $\mathbb{C}$ with the property that $\left(a_{0}, \alpha_{0}\right)$ is gauge equivalent to the pull-back $s^{*}\left(a_{1}, \alpha_{1}\right)$. In this case, $\alpha_{0}^{-1}(0)$ is a finite set of parallel, complex planes.
\end{itemize}
\begin{itemize}
\item[-] Given the constant $z$ in (5.2), there is an upper bound on the order of vanishing of $\alpha_{0}$ at any point in $\mathbb{C}^{2}$.
\item[-] The set of gauge equivalence classes of $\left(a_{0}, \alpha_{0}\right)$ which obey (5.2) for a fixed value of $z$ is sequentially compact with respect to convergence on compact subsets of $\mathbb{R}^{4}$ in the $C^{\infty}$ topology.
\item[-] Given the value of $z$ in (5.2), there exists $z_{1}>0$ such that
$$\left(1-\left|\alpha_{0}\right|^{2}\right)+\left|\nabla_{a} \alpha_{0}\right|^{2} \leq z_{1} \exp \left[-\operatorname{dist}\left(\cdot, \alpha_{0}^{-1}(0)\right) / z_{1}\right] .$$
\end{itemize}
This proposition restates various assertions of Proposition 4.1 in [15]; the reader is referred to Section 4e of [15] for the proof.

End the digression.
The relevance of the solutions to the standard Seiberg-Witten solutions to the problem at hand is summarized by the next proposition:

Proposition 5.2 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$. Given $\delta>0$, there is a constant $z_{\delta} \geq 1$, and given $R \geq 1, k \geq 1$ and $\varepsilon>0$, there is another constant $\zeta_{\delta}$ and these have the following significance: Let $r>\zeta_{\delta}$ and let $(A, \psi)$ be a solution to (2.9) as defined with the given Spin ${ }^{\mathbb{C}}$ structure and with $r$. Suppose that $x \in X$ has distance at least $\delta$ from $Z$. Now define the fields $(\underline{A},(\underline{\alpha}, \underline{\beta}))$ as in (5.1). Then there exists a solution $\left(a_{0}, \alpha_{0}\right)$ to the $z_{1} \leq z_{\delta}$ version of (5.2) and a gauge transformation $\varphi: \mathbb{C}^{2} \rightarrow S^{1}$ such that $\varphi^{*}(\underline{A},(\underline{\alpha}, \underline{\beta}))-\left(2 a_{0},\left(\alpha_{0}, 0\right)\right)$ has $C^{k}$ norm less than $\varepsilon$ in the ball of radius $R$ and center 0 in $\mathbb{R}^{4}$. Furthermore, $\left|\alpha_{0}\right|$ is not constant if $|\alpha(x)| \leq 1-\varepsilon$.

Proof of Proposition 5.2 The proof of this proposition can be found by lifting from Section 4c of [15] the proofs of the analogous assertions of Proposition 4.2 of [15]. (The lack of control here on the integral over $\mathbb{R}^{4}$ of $\left|F_{a}^{+}\right|^{2}-\left|F_{a}^{-}\right|^{2}$ precludes only the use of the proofs in [15] of statements which actually refer to this integral.)

\section*{6 Large $r$ behavior away from $\alpha^{-1}(0)$}

Fix a Spin ${ }^{\text {C }}$ structure for $X$ and then consider a solution ( $A, \psi$ ) to (2.9) for the given Spin ${ }^{\mathbb{C}}$ structure and for some large value of $r$. The purpose of this section is to investigate the behavior of $(A, \psi)$ to (2.9) at points which lie neither on $Z$ nor on $\alpha^{-1}(0)$. Here are the basic observations: First, $2^{-1 / 2}|\omega|-|\alpha|^{2}$ and $|\beta|$ are both $\mathcal{O}\left(r^{-1}\right)$. In particular, this means that $F_{A}$ is bounded. More to
the point, the connection $A$ is close to a canonical connection $A^{0}$ whose gauge orbit depends only on the metric and the choice of $\omega$. (Note that this orbit is independent of the chosen Spin ${ }^{\mathbb{C}}$ structure.) Proposition 6.1, below, gives the precise measure of closeness that is used here.

The statement of Proposition 6.1 requires a preliminary, three part digression whose purpose is to define the connection $A^{0}$. The first part of the digression remarks that the $-\sqrt{2} i|\omega|$ eigenspace of the Clifford multiplication endomorphism by $c_{+}(\omega)$ on $S_{+}$defines a complex line bundle $E \rightarrow X-Z$. The component $\alpha$ of $\psi$ is a section of $E$, and then the component $\beta$ is one of $K^{-1} E$. Here, $K^{-1}$ is the inverse of the canonical bundle, $K$, for the almost complex structure $J \equiv \sqrt{2} g^{-1} \omega /|\omega|$ on $X-Z$.

Note that the line bundle $L=\operatorname{det}\left(S_{+}\right)$restricts to $X-Z$ as
$$\left.L\right|_{X-Z} \approx K^{-1} E^{2} .$$
Meanwhile, $\alpha$ trivializes $E$ where $\alpha \neq 0$ and so the unit length section $\alpha^{2} /|\alpha|^{2}$ of $E^{2}$ provides an isometric identification of $L$ with $K^{-1}$ on the complement of $Z$ and $\alpha^{-1}(0)$.

The second part of the digression reviews the definition from [18] or Section 1c of [15] of a canonical connection on the line bundle $K^{-1} \rightarrow X-Z$. (Note that this connection is unique up to gauge equivalence.) To define a canonical connection, first remark that there is a canonical Spin ${ }^{\mathrm{C}}$ structure for $X-Z$ so that the $-\sqrt{2} i|\omega|$ eigenbundle for the $c_{+}(\omega)$ action on the corresponding $S_{+}$ is the trivial bundle over $X-Z$. For this Spin ${ }^{\mathbb{C}}$ structure, the corresponding line bundle $L$ is isomorphic to $K^{-1}$. With this understood, there is a unique connection (up to isomorphism) on $K^{-1}$ for which the induced connection on the aforementioned $-\sqrt{2} i|\omega|$ eigenbundle is trivial. Such a connection is a canonical one.

Part 3 of the digression defines a canonical connection on $\left.L\right|_{X-Z}$ by using the identification $\alpha^{2} /|\alpha|^{2}$ between $L$ and $K^{-1}$ (where $\alpha \neq 0$ on $X-Z$ ) to pull a canonical connection on $K^{-1}$ back to $L$.

End the digression.
Proposition 6.1 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and $\delta>0$. There is a constant $\zeta_{\delta} \geq 1$ with the following significance: Suppose that $r \geq \zeta_{\delta}$ and that $(A, \psi)$ are a solution to (2.9) as defined by $r$ and the given Spin ${ }^{\mathbb{C}}$ structure. There is a canonical connection $A^{0}$ on $\left.L\right|_{X-Z}$ for which $\left|A-A^{0}\right|+\left|F_{A}-F_{A^{0}}\right| \leq$ $\zeta_{\delta} r^{-1}+\zeta_{\delta} r \exp \left[-\sqrt{r} \operatorname{dist}\left(x, \alpha^{-1}(0)\right) / \zeta_{\delta}\right]$ at all points $x \in X$ with distance $\delta$ or more from $Z$ and distance $r^{-1 / 2}$ or more from $\alpha^{-1}(0)$.
(This proposition should be compared with Proposition 4.4 in [15].)
Proof of Proposition 6.1 Away from $Z$ and where $\alpha \neq 0$, the section $\alpha /|\alpha|$ defines a trivialization of the line bundle $E$, and with this understood, the difference between $A$ and a particular canonical connection $A^{0}$ is given by $2(\bar{\alpha} /|\alpha|) \nabla_{A}(\alpha /|\alpha|)$. Thus, the absolute value of $\nabla_{A}(\alpha /|\alpha|)$ measures the size of $A-A^{0}$. Likewise, the norm of $d_{A} \nabla_{A}(\alpha /|\alpha|)$ measures the size of $F_{A}-F_{A^{0}}$.

With the task ahead now clear, note that the arguments which establish the required bounds on the derivatives of $\alpha$ are, for the most part, straightforward modifications of the arguments which prove Proposition 4.4 in [15]. In particular, the reader will be referred to the latter reference at numerous points. In any event, the details are given in the subsequent four steps.

Step 1 A straightfoward modification of the proof of Proposition 4.4 in [15] (which is left to the reader) proves the following preliminary estimate:

Lemma 6.1 Fix a Spin ${ }^{\mathbb{C}}$ structure for $X$ and fix $\delta>0$. There is a constant $\zeta_{\delta}$ with the following significance: Let ( $A, \psi$ ) solve the version of (2.9) which is defined by the given Spin ${ }^{\mathbb{C}}$ structure and by $r \geq \zeta_{\delta}$. If $x \in X$ has distance $\delta$ or more from $Z$, then
$$\begin{aligned}
r\left|\left(2^{-1 / 2}|\omega|-|\alpha|^{2}\right)\right| 7 & +r^{2}|\beta|^{2}+\left|\nabla_{A} \alpha\right|^{2}+r\left|\nabla_{A} \beta\right|^{2} \\
& \leq \zeta_{\delta}\left(1+r \exp \left[-\sqrt{r} \operatorname{dist}\left(x, \alpha^{-1}(0)\right) / \zeta_{\delta}\right]\right) .
\end{aligned}$$

Step 2 Now, introduce $\underline{\alpha} \equiv 2^{1 / 4}|\omega|^{-1 / 2} \alpha$. Add the two lines of (3.53) to obtain a differential inequality for the function $y \equiv\left|\nabla_{A} \underline{\alpha}\right|^{2}+\left|\nabla_{A} \beta\right|^{2}$. Use Lemma 6.1 to bound $|w|$ to find that the aforementioned inequality implies that $2^{-1} d^{*} d y+4^{-1} r \zeta_{\delta}^{-1} y \leq \zeta_{\delta} r^{-1}$ at points with distance $\delta$ or more to $Z$ and distance $\zeta_{\delta} r^{-1 / 2}$ or more to $\alpha^{-1}(0)$. Note that (6.3) implies that $y^{\prime} \equiv y-4 \zeta_{\delta}^{2} r^{-2}$ obeys the inequality
$$2^{-1} d^{*} d y^{\prime}+4^{-1} r \zeta_{\delta}^{-1} y^{\prime} \leq 0$$
at points with distance $\delta$ or more to $Z$ and $\zeta_{\delta} r^{-1 / 2}$ or more to $\alpha^{-1}(0)$.
Given (6.3), a straightforward modification of the proof of Proposition 4.4 in [15] yields the bound
$$\left|\nabla_{A} \underline{\alpha}\right|^{2}+\left|\nabla_{A} \beta\right|^{2} \leq \zeta_{\delta} r^{-2}+\zeta_{\delta} r \exp \left(-\sqrt{r} \operatorname{dist}\left(\cdot, \alpha^{-1}(0)\right) / \zeta_{\delta}\right)$$
at points with distance $2 \delta$ or more from $Z$. (Bounds on the size of both $\left|\nabla_{A} \underline{\alpha}\right|^{2}$ and $\left|\nabla_{A} \beta\right|^{2}$ near $\alpha^{-1}(0)$ come via Proposition 3.3.)

Take the $\delta / 2$ version of (6.4) with the fact that $\underline{\alpha} /|\underline{\alpha}|=\alpha /|\alpha|$ to bound the difference between $A$ and a canonical connection on $L$ by
$$\zeta_{\delta}\left(r^{-1}+r^{1 / 2} \exp \left(-\sqrt{r} \operatorname{dist}\left(\cdot, \alpha^{-1}(0)\right) / \zeta_{\delta}\right)\right)$$
at points with distance $\delta$ or more from $Z$ and $r^{-1 / 2}$ or more from $\alpha^{-1}(0)$.

Step 3 As remarked above, a bound on $\left|\nabla_{A}^{2} \underline{\alpha}\right|$ provides a bound on $\left|F_{A}-F_{A^{0}}\right|$. To obtain the latter, first differentiate (3.55) and commute covariant derivatives to obtain an equation for $\nabla_{A}^{2} \underline{\alpha}$ of the form $\nabla_{A}^{*} \nabla_{A}\left(\nabla_{A}^{2} \underline{\alpha}\right)+(4 \sqrt{2})^{-1} r|\omega|\left(\nabla_{A}^{2} \underline{\alpha}\right)+$ Remainder $=0$. Take the inner product of this last equation with $\nabla_{A}^{2} \underline{\alpha}$ to obtain an equation for $\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}$ having the form $2^{-1} d^{*} d\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+4^{-1} r|\omega|\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+$ $\left|\nabla_{A}\left(\nabla_{A}^{2} \underline{\alpha}\right)\right|^{2}+\left\langle\nabla_{A}^{2} \underline{\alpha}\right.$, Remainder $\rangle=0$. Here, 〈, 〉denotes the Hermitian inner product on $E \otimes\left(\otimes_{2} T^{*} X\right)$. A similar equation for $\left|\nabla_{A}^{2} \beta\right|$ is obtained by differentiating (3.56). Add the resulting two equations. Then, judicious use Lemma 6.1, (6.5) and the triangle inequality produces a differential inequality for $y^{\prime} \equiv\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+\left|\nabla_{A}^{2} \beta\right|^{2}-\zeta_{\delta} r^{-2}$ which has the same form as (6.3). And, with this understood, the arguments which yield (6.4) yield the bound
$$y^{\prime} \leq \zeta_{\delta} r^{-2}+\zeta_{\delta}\left(\sup _{\sigma \geq \delta}\left|y^{\prime}\right|\right) \exp \left(-\sqrt{r} \operatorname{dist}\left(\cdot, \alpha^{-1}(0)\right) / \zeta_{\delta}\right)$$
at points where $\sigma \geq 2 \delta$.

Step 4 The $\delta / 2$ version of (6.5) with a bound on $\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+\left|\nabla_{A}^{2} \beta\right|^{2}$ where $\sigma \geq \delta / 2$ by $\zeta_{\delta} r^{2}$ gives Proposition 6.1's bound on $\left|F_{A}-F_{A^{0}}\right|$. Thus, the last task is to obtain a supremum bound on $\left|\nabla_{A}^{2} \underline{\alpha}\right|^{2}+\left|\nabla_{A}^{2} \beta\right|^{2}$.

For this purpose, fix a ball of radius $2 r^{-1 / 2}$ whose points all have distance $\delta / 4$ or more from $Z$. Take Gaussian coordinates based at the center of this ball and rescale so that the radius $r^{-1 / 2}$ concentric ball becomes the radius 1 ball in $\mathbb{R}^{4}$ with center at the origin. Equation (2.9) rescales to give an $r=1$ version of the same equation on the radius 2 ball in $\mathbb{R}^{4}$ with a metric $g^{\prime}$ which is close to the Euclidean metric $g_{E}$ and form $\omega^{\prime}$ which is close a constant self dual form of size $|\omega(x)|$. Here, $x$ is the center of the chosen ball in $X$. To be precise, $\left|g^{\prime}-g_{E}\right| \leq \zeta r^{-1}$ and the derivatives of $g^{\prime}$ of order $k \geq 2$ are $\mathcal{O}\left(r^{-k / 2}\right)$ in size. Meanwhile the form $\omega^{\prime}$ differs by $\mathcal{O}\left(r^{-1 / 2}\right)$ from a constant form, and its $k$-th derivatives are $\mathcal{O}\left(r^{-k / 2}\right)$ in size.

With the preceding understood, standard elliptic regularity results (as in Chapter 6 of [12]) bound the second derivatives of the rescaled versions of $\underline{\alpha}$ and $\beta$ by $\zeta_{\delta}$. Rescaling the latter bounds back to the original size gives $\left|\nabla^{2}{ }_{A} \underline{\alpha}\right|^{2}+\left|\nabla^{2}{ }_{A} \beta\right|^{2} \leq$ $\zeta_{\delta} r^{2}$ as required.

\section*{7 Proof of Theorem 2.2}

Fix a Spin ${ }^{\text {© }}$ structure for $X$ and suppose that there exists an unbounded, increasing sequence $\left\{r_{n}\right\}$ of positive numbers with the property that each $r=r_{n}$ version of (2.9) with the given Spin ${ }^{\mathbb{C}}$ structure has a solution $\left(A_{n}, \psi_{n}\right)$. The purpose of this section is to investigate the $n \rightarrow \infty$ limits of $\alpha_{n}^{-1}(0)$ and in doing so, prove the claims of Theorem 2.2. This investigation is broken into six parts.

\section*{a) The curvature as a current}

Each connection $A_{n}$ has its associated curvature 2-form, and the difference between $A_{n}$ 's curvature 2-form and the curvature 2-form of the canonical connection on $K^{-1}$ will be viewed as a current on $X$. This current, $\mathcal{F}_{n}$, associates to a smooth 2 -form $\mu$ the number
$$\mathcal{F}_{n}(\mu) \equiv 2^{-1} \int_{X} \frac{i}{2 \pi}\left(F_{A_{n}}-F_{A^{0}}\right) \wedge \mu .$$
Here, $F_{A^{0}}$ is the curvature 2-form of the canonical connection on $K^{-1}$. (Even though the canonical connection on $K^{-1}$ is defined only over $X-Z$ (see the beginning of the previous section), the norm of its curvature is none-the-less integrable over $X$. Thus, (7.1) makes sense even for $\mu$ whose support intersects $Z$. The integrability of $\left|F_{A^{0}}\right|$ follows from the bound $\left|F_{A^{0}}\right| \leq \zeta \operatorname{dist}(\cdot, Z)^{-2}$.)

With the sequence $\left\{\mathcal{F}_{n}\right\}$ understood, fix $\delta>0$ and suppose that each point in the support of $\mu$ has distance $\delta$ or more from $Z$. It then follows from Lemma 3.1 and Proposition 4.2 that
$$\left|\mathcal{F}_{n}(\mu)\right| \leq \zeta_{\delta} \sup _{X}|\mu| .$$
This uniform bound implies that the sequence $\left\{\mathcal{F}_{n}\right\}$ defines a bounded sequence of linear functional on the space of smooth 2-forms on $X$ with support where the distance to $Z$ is at least $\delta$.

With the preceding understood, a standard weak convergence argument finds a subsequence of $\left\{\mathcal{F}_{n}\right\}$ (hence renumbered consecutively) which converges in the following sense: Let $\mu$ be a smooth 2-form with compact support on $X-Z$ and then $\lim _{n \rightarrow \infty} \mathcal{F}_{n}(\mu)$ exists. Moreover, this limit,
$$\mathcal{F}(\cdot) \equiv \lim _{n \rightarrow \infty} \mathcal{F}_{n}(\cdot),$$
defines a bounded linear functional when restricted to forms whose support has distance from $Z$ which is bounded from below by any fixed positive number.

Note that the current $\mathcal{F}$ is integral in the following sense: Let $\mu$ be a closed 2- form with compact support on $X-Z$ and with integral periods on $H_{2}(X-Z ; \mathbb{Z})$. Then
$$\mathcal{F}(\mu) \in \mathbb{Z} .$$
b) The support of $\mathcal{F}$

This part of the discussion considers the support of the current $\mathcal{F}$. Here is the crucial lemma:

Lemma 7.1 There is a closed subspace $C \subset X-Z$ with the following properties:
\begin{itemize}
\item[-] $\mathcal{F}(\mu)=0$ when $\mu$ is a 2-form on $X$ with compact support in $(X-Z)-C$.
\item[-] Conversely, let $B \subset X-Z$ be an open set which intersects $C$. Then there is a 2-form $\mu$ with compact support in $B$ and with $\mathcal{F}(\mu) \neq 0$.
\item[-] Fix $\delta>0$. Then the set of points in $C$ with distance at least $\delta$ from $Z$ has finite 2-dimensional Hausdorff measure.
\item[-] Conversely, let $\delta>0$ and there is a constant $\zeta_{\delta} \geq 1$ with the following significance: Let $\rho \in\left(0, \zeta_{\delta}^{-1}\right)$ and let $B \subset X$ be a ball of radius $\rho$ and center on $Z$ whose points have distance $\delta$ or more from $Z$. Then the 2-dimensional Hausdorff measure of $B \cap C$ is greater than $\zeta_{\delta}^{-1} \rho^{2}$.
\item[-] There is a subsequence of $\left(A_{n}, \psi_{n}\right)$ such that the corresponding sequence $\left\{\alpha_{n}^{-1}(0)\right\}$ converges to $C$ in the following sense: For any $\delta>0$, the following limit exists and is zero:
$$\left.\lim _{n \rightarrow \infty}\left[\sup _{\{x \in C: \operatorname{dist}(x, Z) \geq \delta\}} \operatorname{dist}\left(x, \alpha_{n}^{-1}(0)\right)+\sup _{\left\{x \in \alpha_{n}^{-1}(0): \operatorname{dist}(x, Z) \geq \delta\right\}} \operatorname{dist}(x, C)\right)\right] .$$
\end{itemize}

Proof of Lemma 7.1 To construct $C$, consider first a large positive integer $N$ and a very large positive integer $n$. (Here, a lower bound on $n$ comes from the choice of $N$.) Use Lemma 4.1 to find a set $\Lambda_{n}^{\prime}(N)$ of balls of radius $16^{-N}$ with the following properties: The balls are disjoint, their centers lie on $\alpha_{n}^{-1}(0)$ and have distance at least $4 \cdot 16^{-N}$ from $Z$, and the set $\Lambda_{n}(N)$ of concentric balls of radius $2 \cdot 16^{-N}$ covers the set of point in $\alpha_{n}^{-1}(0)$ with distance $8 \cdot 16^{-N}$ from $Z$. According to Lemma 4.1, when $n$ is sufficiently large, this set $\Lambda_{n}(N)$ has a bound on the number of its elements which is independent of $n$. Let $\nu(N)$ be an integer which is greater than the number of elements in each $\Lambda_{n}(N)$.

Label the centers of the balls in $\Lambda_{n}(N)$ and then add the final point some number of times (if necessary) to make a point $\underline{x}_{n}(N) \equiv\left(x_{n}(1 ; N), \ldots, x_{n}(\nu(N) ; N)\right)$ $\in \times_{\nu(N)} X$. By a diagonalization process, one can find an infinite sequence of indices $n$ (hence relabeled consecutively from 1) so that for each $N$, the sequence $\left\{\underline{x}_{n}(N)\right\}_{n \geq 1}$ converges in $\times_{\nu(N)} X$.

For each $N$, let $\underline{x}(N) \equiv\{x(1, N), \ldots, x(\nu(N), N)\}$ denote the limit of $\left\{\underline{x}_{n}(N)\right\}_{n \geq 1}$. One can think of $\underline{x}(N)$ as either a point in $\times_{\nu(N)} X$, or else an ordered set of $\nu(N)$ points in $X$. Think of $\underline{x}(N)$ in the latter sense, and let $U(N)$ denote the union of the balls of radius $4 \cdot 16^{-N}$ with centers at the points $\underline{x}(N)$ (that is, at $\{x(i, N)\}_{1 \leq i \leq \nu(N)}$ ). Lemma 5.1 of [15] argues that these sets are nested in that $U(N+1) \subset U(N)$. With this understood, set
$$C \equiv \bigcap_{N \geq 1} U(N) .$$
The argument for the asserted properties of $C$ is essentially the same as that for Lemma 5.2 in Section 5c of [15]. In this regard, Lemma 4.1 here replaces Lemma 3.6 in [15], and Proposition 4.2 here replaces Proposition 4.4 in [15]. The details are straightforward and left to the reader.

\section*{c) A positive cohomology assignment}

The purpose of this subsection is to give a more precise characterization of the distribution $\mathcal{F}$.

To begin, note that the construction of $C$ indicated above can be used (as in the proof of Lemma 5.3 in [15]) to prove that the current $\mathcal{F}$ is type 1-1 in the sense that $\mathcal{F}(\mu)=0$ when $\mu$ is a section of the subbundle $K^{-1} \subset \Lambda_{+}$. The fact that $\mathcal{F}$ is type 1-1 is implied by Lemma 7.2 below which is a significantly stronger assertion:

Lemma 7.2 Let $D \subset \mathbb{C}$ denote the standard, unit disc, and let $\sigma: D \rightarrow X-Z$ be a smooth map which extends to the closure, $\underline{D}$, of $D$ as a continuous map that sends $\partial \underline{D}$ into $X-C$. Then, $\left\{2^{-1} \int_{D} \sigma^{*}\left(\frac{i}{2 \pi}\left(F_{A_{n}}-F_{A^{0}}\right)\right)\right\}_{n \geq 1}$ converges, and the limit, $I(\sigma) \in \mathbb{Z}$. Moreover,
\begin{itemize}
\item[-] $I(\sigma)=0$ if $\sigma(D) \cap C=\emptyset$.
\item[-] $I(\sigma)>0$ if $\sigma$ is a pseudo-holomorphic map and $\sigma^{-1}(C) \neq \emptyset$.
\end{itemize}

Proof of Lemma 7.2 The arguments which prove Lemma 6.2 in [15] are of a local character and so can be brought to bear directly to give Lemma 7.2.

The discussion surrounding Lemma 6.2 in [15] concerns the notion of a positive cohomology assignment for $C$. The latter is defined as follows: First, let $D \subset \mathbb{C}$ be the standard unit disk again. A map $\sigma: D \rightarrow X-Z$ is called admissible when $\sigma$ extends as a continuous map to the closure, $\underline{D}$, of $D$ which maps $\partial \underline{D}$ into $X-C$. A positive cohomology assignment specifies an integer, $I(\sigma)$, for each admissible map $\sigma$ from $D$ to $X-Z$ subject to the following constraints:
\begin{itemize}
\item[-] If $\sigma(D) \subset X-C$, then $I(\sigma)=0$.
\item[-] A homotopy $h:[0,1] \times D \rightarrow X$ is called admissible when it extends as a continuous map from $[0,1] \times \underline{D}$ into $X$ that sends $[0,1] \times \partial \underline{D}$ to $X-C$. If $h$ is an admissible homotopy, then $I(h(1, \cdot))=I(h(0, \cdot))$.
\item[-] Let $\sigma: D \rightarrow X$ be admissible and suppose that $\theta: D \rightarrow D$ is a proper, degree $k$ map. Then $I(\sigma \cdot \theta)=k I(\sigma)$.
\item[-] Suppose that $\sigma: D \rightarrow X$ is admissible and that $\sigma^{-1}(C)$ is contained in a disjoint union $\cup_{\nu} D_{\nu} \subset D$, where each $D_{\nu}=\theta_{\nu}(D)$ with $\theta_{\nu}: D \rightarrow D$ being an orientation preserving embedding. Then $I(\sigma)=\sum_{\nu} I\left(\sigma \cdot \theta_{\nu}\right)$.
\item[-] If $\sigma$ is admissible and pseudo-holomorphic with $\sigma^{-1}(C) \neq \emptyset$, then $I(\sigma)>$ 0. (7.8)
\end{itemize}

The next result follows from Lemma 7.2 and the particulars of the definition of $\mathcal{F}$ in (7.3) as a limit.

Lemma 7.3 Let $C$ be as in Lemma 7.1 and let $I(\cdot)$ be as described in Lemma 7.2. Then $I(\cdot)$ defines a positive cohomology assignment for $C$.

Proof of Lemma 7.3 Use the proof of Lemma 6.2 in [15].

\section*{d) $C$ as a pseudo-holomorphic submanifold}

Proposition 6.1 in [15] asserts that a closed set in a compact, symplectic 4-manifold with finite 2 -dimensional Hausdorff measure and a positive cohomology assignment is the image of a compact, complex curve by a pseudoholomorphic map. (Note, however that the proof of Proposition 6.1 in [15] has errors which occur in Section 6e of [15], and so the reader is referred to the revised proof in the version which is reprinted in [20].) It is important to realize that the assumed compactness of $X$ in the statement of Proposition 6.1 of [15] is present only to insure that the complex curve in question is compact. In particular, the proof of Proposition 6.1 in [15] from the reprinted version in [20] yields:

Proposition 7.1 Let $Y$ be a 4-dimensional symplectic manifold with compatible almost complex structure. Suppose that $C \subset Y$ is a closed subset with the following properties:
\begin{itemize}
\item[-] The restriction of $C$ to any open $Y^{\prime} \subset Y$ with compact closure has finite 2-dimensional Hausdorff measure.
\item[-] $C$ has a positive cohomology assignment.
\end{itemize}

Then the following are true:
\begin{itemize}
\item[-] There is a smooth, complex curve $C^{0}$ (not necessarily compact) with a proper, pseudo-holomorphic map $f: C^{0} \rightarrow Y$ with $C=f\left(C^{0}\right)$.
\item[-] There is a countable set $\Lambda^{0} \subset C^{0}$ with no accumulation points such that $f$ embeds each component $C^{0}-\Lambda^{0}$.
\item[-] Here is an alternate description of the cohomology assignment for $C$ : Let $\sigma: D \rightarrow Y$ be an admissible map, and let $\sigma^{\prime}$ be any admissible perturbation of $\sigma$ which is transverse to $f$ and which is homotopic to $\sigma$ via an admissible homotopy. Construct the fibered product $T \equiv\{(x, y) \in$ $\left.D \times C_{1}: \sigma^{\prime}(x)=\varphi(y)\right\}$. This $T$ is a compact, oriented 0 -manifold, so a finite set of signed points; and the cohomology assignment gives $\sigma$ the sum of the signs of the points of $T$.
\end{itemize}

Proof of Proposition 7.1 As remarked at the outset, the proof of Proposition 6.1 in [15] from the revised version in [20] can be brought to bear here with negligible modifications.

Lemma 7.3 enables Proposition 7.1 to be applied to the set $C$ from Lemma 7.1. In particular, one can conclude that $C$ is the image of a smooth, complex curve $C^{0}$ via a proper, pseudo-holomorphic
$$f: C^{0} \rightarrow X-Z .$$
Moreover, $f$ can be taken to be an embedding upon restriction to each component of the complement in $C^{0}$ of a countable set with no accumulation points. In particular, it follows that $C$ restricts to any open subset with compact closure in $X-Z$ as a pseudo-holomorphic subvariety.

\section*{e) The energy of $C$}

The purpose of this subsection is to state and prove

Lemma 7.4 The set $C$ from Lemma 7.1 is a finite energy, pseudo-holomorphic subvariety in the sense of Definition 1.1. Furthermore, there are universal constants $\zeta_{1}, \zeta_{2}$ (independent of the metric) such that
$$\int_{C} \omega \leq \zeta_{1} e_{\omega}(s)+\zeta_{2} \int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| d \operatorname{vol}_{g} .$$
In this equation, $e_{\omega}(s)$ equals the evaluation on the fundamental class of $X$ of the cup product of $c_{1}(L)$ with $[\omega]$. Meanwhile, $R_{g}$ is the scalar curvature for the metric $g$, and $W_{g}^{+}$is the metric's self-dual, Weyl curvature. Also, dvol $_{g}$ is the metric's volume form.

Proof of Lemma 7.4 First of all, define an equivalence relation on the components of $C^{0}$ (from (7.9)) by declaring two components to be equivalent if their images via $f$ coincide. The quotient by this equivalence relation defines another smooth, complex curve, $C_{0}$, together with a proper, pseudo-holomorphic map $\varphi: C_{0} \rightarrow X-Z$ whose image is $C$. Moreover, there is a countable set $\Lambda_{0} \subset C_{0}$ which has no accumulation points and whose complement is embedded by $\varphi$.

With the preceding understood, it remains only to establish that $C$ has finite energy. For this purpose, fix $\delta>0$ and re-introduce the bump function $\chi_{\delta}$. (Remember that $\chi_{\delta}$ vanishes where the distance to $Z$ is greater than $2 \delta$, and it equals 1 where the distance to $Z$ is less than $\delta$.) Since $\omega$ restricts to $C$ as a positive form, it follows that $C$ has finite energy if and only if
$$\lim _{\delta \rightarrow 0} \int_{C}\left(1-\chi_{\delta}\right) \omega$$
exists, and this limit exists if and only if the set $\left\{\int_{C}\left(1-\chi_{\delta}\right) \omega\right\}_{\delta>0}$ is bounded in $[0, \infty)$. Thus, the task is to find a $\delta$-independent upper bound for this set.

With the preceding understood, remark first that Proposition 7.1 as applied to $C$ yields
$$\int_{C}\left(1-\chi_{\delta}\right) \omega \leq \int_{C^{0}} f^{*}\left(\left(1-\chi_{\delta}\right) \omega\right)=\mathcal{F}\left(\left(1-\chi_{\delta}\right) \omega\right)$$
Now, given $\varepsilon>0$, the right-hand expression in (7.12) is no greater than
$$\mathcal{F}_{n}\left(\left(1-\chi_{\delta}\right) \omega\right)+\varepsilon$$
when $n$ is sufficiently large. Moreover, as $\mathcal{F}_{n}$ is defined on all smooth forms, the first term in (7.13) is equal to
$$(4 \pi)^{-1} \int_{X}\left(1-\chi_{\delta}\right) i F_{A} \wedge \omega-(4 \pi)^{-1} \int_{X}\left(1-\chi_{\delta}\right) i F_{A^{0}} \wedge \omega .$$
with $A=A_{n}$.
Both terms in (7.14) are $\delta$ dependent and so must be analyzed further. In particular, Lemma 7.4 follows with the exhibition of a bound on these terms by $\zeta\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right.$.
For the right most term, remark that only $F_{A^{0}}^{+}$appears in (7.14) (since $\omega$ is self dual), and a calculation (which is left to the reader) finds a universal constant $\zeta$ with the property that
$$\left|F_{A^{0}}^{+}\right| \leq \zeta\left(|\nabla \underline{\omega}|^{2}+\left|R_{g}\right|+\left|W_{g}^{+}\right|\right) .$$
Here, $\underline{\omega} \equiv \omega /|\omega|$. Equation (7.15) implies that the right most term in (7.14) is not greater than
$$\zeta\left(\int_{X}|\omega||\nabla \underline{\omega}|^{2}+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right) .$$
Here the constant $\zeta$ is also metric independent. Meanwhile, the first integral in (7.16) is bounded by $\zeta \int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \operatorname{dvol}_{g}$ which can be seen by integrating both sides of (3.7) and then integrating by parts to eliminate the $d^{*} d|\omega|$ term. This means in particular that the right most term in (7.16) is bounded by a universal multiple of $\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega|$ dvol $_{g}$.
Now consider the left most term in (7.14). For this purpose, use (2.9) to identify the latter with
$$(8 \sqrt{2} \pi)^{-1} r \int_{X}\left(1-\chi_{\delta}\right)|\omega|\left(2^{-1 / 2}|\omega|-|\alpha|^{2}+|\beta|^{2}\right) .$$
One should compare this expression for that implied by (2.9) for $e_{\omega}(s)$, namely
$$2^{-1} e_{\omega}(s)=(8 \sqrt{2} \pi)^{-1} r \int_{X}|\omega|\left(2^{-1 / 2}|\omega|-|\alpha|^{2}+|\beta|^{2}\right) .$$
In particular, note that (7.18) implies the identity
$$(8 \sqrt{2} \pi)^{-1} r \int_{X}|\omega||\beta|^{2}=4^{-1} e_{\omega}(s)-(16 \sqrt{2} \pi)^{-1} r \int_{X}|\omega|\left(2^{-1 / 2}|\omega|-|\psi|^{2}\right) .$$
It then follows from the second line of (3.2) (and the integration of (3.7)) that
$$(8 \sqrt{2} \pi)^{-1} r \int_{X}|\omega||\beta|^{2}=\zeta\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right) .$$
This last bound can now be plugged back into bounding (7.17) since the expression in (7.17) is no greater than
$$(8 \sqrt{2} \pi)^{-1}\left(r \int_{X} \chi_{\delta}|\omega|\left|\left(2^{-1 / 2}|\omega|-|\psi|^{2}\right)\right|+2 r \int_{X}|\omega||\beta|^{2}\right) .$$

Thus, (7.20) and the second line of (3.2) bound the left most term in (7.14) by the required $\zeta\left(e_{\omega}(s)+\int_{X}\left(\left|R_{g}\right|+\left|W_{g}^{+}\right|\right)|\omega| \mathrm{dvol}_{g}\right)$.
f) Intersections with the linking 2 -spheres

After Lemma 7.4, all that remains to prove Theorem 2.2 is to establish that Lemma 7.4's pseudo-holomorphic subvariety $C$ has intersection number equal to 1 with any 2 -sphere in $X-Z$ which has linking number 1 with $Z$.

To prove this last assertion, consider that each $\alpha_{n}$ defines a section of the bundle $E$ whose square is given in (6.1) as $\left.L\right|_{X-Z} K$. Now, $L$ is trivial over a linking 2-sphere for $Z$ as $L$ is a bundle over the whole of $X$. This means that $E$ restricts to a linking 2-sphere of $Z$ as the square root of the restriction of $K$. Moreover, according to Lemma 2.1, the restriction of $K$ to a linking 2-sphere has degree 2 , so $E$ restricts to such a 2 -sphere with degree 1 . This means that the current $\mathcal{F}_{n}$ in (7.1) evaluates as 1 on any closed form which represents the Thom class of a fixed, linking 2-sphere. In particular, the same must be true for a limit current $\mathcal{F}$, and the nature of the convergence in Proposition 7.1 implies that $C$ has intersection number 1 with such a 2-sphere.

Achnowledgement This research was supported in part by the National Science Foundation.

\section*{References}
\begin{itemize}
\item[] [1] MF Atiyah, I Singer, NJ Hitchin, Self-duality in 4-dimensional Riemannian geometry, Proc. Roy. Soc. London Ser. A, 362 (1978) 425-461
\item[] [2] S K Donaldson, Symplectic submanifolds and almost complex geometry, Jour. Diff. Geom. 44 (1996) 666-705
\item[] [3] D S Freed, K K Uhlenbeck, Instantons and Four-Manifolds, Springer-Verlag (1984)
\item[] [4] M Gromov, Pseudo-holomorphic curves in symplectic manifolds, Invent. Math. 82 (1985) 307-347
\item[] [5] K Honda, Harmonic forms for generic metrics, preprint (1997)
\item[] [6] M Hutchings, Y-J Lee, Circle-valued Morse theory, $R$-torsion and Seiberg-Witten invariants of 3-manifolds, Topology, to appear
\item[] [7] M Hutchings, Y-J Lee, Circle-valued Morse theory and Reidemeister torsion, preprint (1997)
\item[] [8] D Kotschick, P B Kronheimer, T S Mrowka, in preparation
\end{itemize}
\begin{itemize}
\item[] [9] C LeBrun, Yamabe constants and the perturbed Seiberg-Witten equations, Commun. Anal. Geom. 5 (1997) 535-553
\item[] [10] D McDuff, D Salamon, $J$-Holomorphic Curves and Quantum Cohomology, American Mathematical Society, Providence (1996)
\item[] [11] J M Morgan, The Seiberg-Witten Equations and Applications to the Topology of Smooth 4-Manifolds, Mathematical Notes, 44, Princeton University Press (1996)
\item[] [12] C B Morrey, Multiple Integrals in the Calculus of Variations, Springer-Verlag (1966)
\item[] [13] P Pansu, Pseudo-holomorphic curves in symplectic manifolds, from: "Holomorphic Curves in Symplectic Geometry", (M Audin and F Lafontaine, editors) Progress in Math. 117, Birkhäuser (1994) 233-250
\item[] [14] T Parker, J Wolfson, Pseudo-holomorphic maps and bubble trees, J. Geom. Anal. 3 (1993) 63-98
\item[] [15] CH Taubes, $S W \Rightarrow G r$ : From the Seiberg-Witten equations to pseudoholomorphic curves, J. Amer. Math. Soc. 9 (1996) 845-918
\item[] [16] CH Taubes, The structure of pseudo-holomorphic subvarieties for a degenerate almost complex structure and symplectic form on $S^{1} \times B^{3}$, Geometry and Topology, 2 (1998) 221-332
\item[] [17] CH Taubes, The geometry of the Seiberg-Witten invariants, from: "Surveys in Differential Geometry, 1996", (S T Yau, editor) International Press, to appear
\item[] [18] C H Taubes, The Seiberg-Witten and the Gromov invariants, Math. Res. Letters 2 (1995) 221-238.
\item[] [19] CH Taubes, $S W=G r$ : Counting curves and connections, preprint (1997)
\item[] [20] CH Taubes, $S W \Rightarrow G r$ : From the Seiberg-Witten equations to pseudoholomorphic curves, from: "Proceedings of the First IP Lecture Series, Vol. II", (R Wentworth, editor), International Press, to appear
\item[] [21] V Turaev, A combinatorial formula for the Seiberg-Witten invariants of 3manifolds, preprint (1998)
\item[] [22] R Ye, Gromov's compactness theorem for pseudo-holomorphic curves, Trans. Amer. Math. Soc. 342 (1994) 671-694
\item[] [23] E Witten, Monopoles and 4-manifolds, Math. Res. Letters, 1 (1994) 769-796
\end{itemize}
