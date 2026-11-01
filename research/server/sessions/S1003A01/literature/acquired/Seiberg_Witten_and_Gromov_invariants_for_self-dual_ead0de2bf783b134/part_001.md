---
retention_scope: session
part: 1
total_parts: 3
---

[Part 1/3 of: Seiberg–Witten and Gromov invariants for self-dual]

---
source_file: 1809_03405.pdf
converter: mathpix
format: mmd
---

\title{
Seiberg-Witten and Gromov invariants for self-dual harmonic 2-forms
}

\author{
Chris Gerig
}

August 2, 2021

\begin{abstract}
This is the sequel to [3] which gives an extension of Taubes' "SW=Gr" theorem to nonsymplectic 4-manifolds. The main result of this paper asserts the following. Whenever the Seiberg-Witten invariants are defined over a closed minimal 4-manifold $X$, they are equivalent modulo 2 to "near-symplectic" Gromov invariants in the presence of certain self-dual harmonic 2-forms on $X$. A version for non-minimal 4-manifolds is also proved. A corollary to Morse theory on 3-manifolds is also announced, recovering a result of Hutchings-Lee-Turaev about the 3-dimensional Seiberg-Witten invariants.
\end{abstract}

\section*{1 Introduction}

The purpose of this paper is to present a proof of the assertion that a compact 4-manifold has its Seiberg-Witten invariants equal to its near-symplectic Gromov invariants. The latter are suitable counts of closed and punctured Riemann surfaces (which may be disconnected and multiply covered) in the complement of certain smoothly embedded circles in the 4-manifold. When the 4manifold is equipped with a symplectic 2-form, this was already known by Taubes [28], in which case there are only closed surfaces and no smoothly embedded circles. When the 4-manifold $X$ is not symplectic, we still assume $b_{+}^{2}(X)>0$. Then given a generic Riemannian metric on $X$ there are nontrivial closed self-dual (hence harmonic) 2-forms which vanish transversally along a disjoint union of circles in $X$ and are symplectic elsewhere [7, 18, 20]. Such a 2-form $\omega$ is a near-symplectic form, and it is through the use of them that a version of " $S W=G r$ " is demonstrated below.

Remark 1.1. We assume the reader is familiar with the previous paper [3], and when necessary we point the reader to specific locations in it. See its introduction for further motivation of the main theorem of the current paper.

Throughout this paper, $(X, g)$ denotes a closed connected oriented smooth Riemannian 4manifold with $b_{+}^{2}(X) \geq 1$, and $\omega$ denotes a self-dual near-symplectic form on $X$ whose zero set
$$Z:=\omega^{-1}(0)$$
has $N \geq 0$ components, all of which are untwisted ${ }^{1}$ zero-circles (see [3, §1.2] for the notion of (un)twisted zero-circles). Such harmonic 2-forms always exist, but the parity of $N$ must be the same as that of $1-b^{1}(X)+b_{+}^{2}(X)$.

\footnotetext{
${ }^{1}$ We may also allow components of $Z$ to be twisted zero-circles which are non-contractible in $X$ (see 3, Appendix]), but we restrict our attention to untwisted zero-circles for simplicity of notation.
}

Fix an ordering of the zero-circles of $\omega$. In [3] we defined the near-symplectic Gromov invariants
$$G r_{X, \omega}: \operatorname{Spin}^{c}(X) \rightarrow \Lambda^{*} H^{1}(X ; \mathbb{Z})$$
in terms of counts of pseudoholomorphic curves in a certain completion of $X-Z$, for which they a priori depend on an almost complex structure on $X-Z$. Here is the main theorem of this paper for $X$ minimal. ${ }^{2}$ from which it follows that $G r_{X, \omega}$ over $\mathbb{Z} / 2 \mathbb{Z}$ are indeed smooth invariants of $X$.

Theorem 1.2. Given a minimal 4 -manifold $(X, \omega)$ as above and any $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$,
$$G r_{X, \omega}(\mathfrak{s}) \equiv S W_{X}(\mathfrak{s}) \quad \bmod 2 \quad \in \Lambda^{*} H^{1}(X ; \mathbb{Z}) \otimes \mathbb{Z} / 2 \mathbb{Z}$$
where $S W_{X}(\mathfrak{s})$ is the Seiberg-Witten invariant defined in Definition 2.3 and $\omega$ determines the chamber for defining the Seiberg-Witten invariants when $b_{+}^{2}(X)=1$.

When $X$ is not minimal, there is a version of this theorem (see Theorem 1.7) but it is more involved. In particular, it cannot be demonstrated for all spin-c structures on $X$. This issue also appears in Taubes' Gromov invariants of a closed symplectic 4-manifold, but thanks to the blow-up formula for the Seiberg-Witten invariants ([23, Theorem 2.2] and [19, Proposition 4.3]) we may as well suppose that $X$ is minimal.

Remark 1.3. The definition of the Seiberg-Witten invariants over $\mathbb{Z}$ requires a choice of homology orientation of $X$. As we will explain in Section 2.5, this choice is equivalent to a choice of ordering of the zero-circles of $\omega$ plus a choice of homology orientation of the cobordism obtained from $X$ by removing tubular neighborhoods of the zero-circles. We expect that there is a canonical homology orientation of this cobordism determined by $\omega$, and that Theorem 1.2 can be lifted to $\mathbb{Z}$ coefficients.

\subsection*{1.1 Outline of remainder of paper}

What follows is a brief outline of the remainder of the paper. Sections 1.2 and 1.3 recall the nearsymplectic Gromov invariants and explain how they depend on spin-c structures on $X$. Section 1.5 introduces a small application of the main theorem in dimension three, concerning Morse theory, which may help the reader see what near-symplectic forms look like and what the near-symplectic Gromov invariants count.

Section 2 consists of a review of those aspects of Seiberg-Witten theory that are relevant to this paper. This concerns the Seiberg-Witten equations and corresponding Floer homologies on 3- and 4-manifolds, either with symplectic/contact forms (following the work of Taubes) or without that additional structure (following the work of Kronheimer-Mrowka). Next, in Section 3 we review Taubes' isomorphisms between embedded contact homology and monopole Floer homology. They will be mimicked and generalized in Section 4 to relate pseudoholomorphic curves with Seiberg-Witten solutions on the symplectic cobordism $(X-\mathcal{N}, \omega)$, where $\mathcal{N}$ is a certain tubular neighborhood of $\omega^{-1}(0)$. The story here is complicated by the existence of multiply covered tori and planes, but resolved using the methodology of Taubes' proof of " $S W=G r$ " for closed symplectic 4-manifolds.

Finally, in Section 5 we complete the proof of Theorem 1.2 by relating Seiberg-Witten solutions on $X-\mathcal{N}$ with Seiberg-Witten solutions on $X$, via a familiar "stretching the neck" procedure.

\footnotetext{
${ }^{2}$ A manifold is minimal if there are no exceptional spheres, smoothly embedded 2-spheres of self-intersection -1.
}

\subsection*{1.2 Taubes' map}

We are about to explain the construction of $G r_{X, \omega}$, as it will nicely set the stage for the rest of the this paper. Let $\mathcal{N}$ denote the union of arbitrarily small tubular neighborhoods of the components of $Z \subset X$, chosen in such a way that the complement
$$\left(X_{0}, \omega\right):=\left(X-\mathcal{N},\left.\omega\right|_{X-\mathcal{N}}\right)$$
is a symplectic manifold with contact-type boundary, where each (negative) boundary component is a copy of $\left(S^{1} \times S^{2}, \xi_{0}\right)$. Here, $\xi_{0}$ is an overtwisted contact structure whose contact form $\lambda_{0}$ is specified in [3, §3.1].

Now, $\omega$ determines the canonical bundle $K \rightarrow X_{0}$ and induces an $H_{2}(X ; \mathbb{Z})$-equivariant map
$$\tau_{\omega}: \operatorname{Spin}^{c}(X) \rightarrow H_{2}\left(X_{0}, \partial X_{0} ; \mathbb{Z}\right), \quad \mathfrak{s} \mapsto \operatorname{PD}\left(c_{1}(E)\right)$$
where $E \rightarrow X_{0}$ is the complex line bundle that defines the decomposition of the positive spinor bundle associated with the restricted spin-c structure $\left.\mathfrak{s}\right|_{X_{0}}$,
$$\mathbb{S}_{+}\left(\left.\mathfrak{s}\right|_{X_{0}}\right)=E \oplus K^{-1} E$$
See the upcoming Section 2.2 for an elaboration. The following lemma shows that $\tau_{\omega}$ gives a canonical identification between $\operatorname{Spin}^{c}(X)$ and the set
$$\left\{A \in H_{2}\left(X_{0}, \partial X_{0} ; \mathbb{Z}\right) \mid \partial A=\mathbb{1} \in H_{1}\left(\partial X_{0} ; \mathbb{Z}\right)\right\}$$
where $\mathbb{1}$ is the oriented generator on each component (see [3, §3.1] for orientation conventions).
Lemma 1.4. The map $\tau_{\omega}$ is injective, and its image consists of the subset of relative homology classes whose boundary is the oriented generator of $H_{1}\left(\partial X_{0} ; \mathbb{Z}\right)$, i.e. for each $\mathfrak{s}$ on $X$
$$\partial \tau_{\omega}(\mathfrak{s})=-(1, \ldots, 1) \in-\bigoplus_{k=1}^{N} H_{1}\left(S^{1} \times S^{2} ; \mathbb{Z}\right)$$
Proof. The restriction map $\operatorname{Spin}^{c}(X) \rightarrow \operatorname{Spin}^{c}\left(X_{0}\right)$ is injective, or in terms of the cohomology actions, the restriction map $H^{2}(X ; \mathbb{Z}) \rightarrow H^{2}\left(X_{0} ; \mathbb{Z}\right)$ is injective. This follows from the cohomological long exact sequence applied to the pair $\left(X, X_{0}\right)$ because
$$H^{2}\left(X, X_{0} ; \mathbb{Z}\right) \cong H^{2}(\operatorname{cl} \mathcal{N}, \partial \mathcal{N} ; \mathbb{Z}) \cong H_{2}(\operatorname{cl} \mathcal{N} ; \mathbb{Z})=0$$
using excision and Poincaré-Lefschetz duality. Then $\tau_{\omega}$ is injective, since
$$\tau_{\omega}(\mathfrak{s} \otimes E)-\tau_{\omega}(\mathfrak{s})=\operatorname{PD} c_{1}\left(\left.E\right|_{X_{0}}\right)$$
for any complex line bundle $E \rightarrow X$.
Likewise, the determinant line bundle $\operatorname{det} \mathbb{S}_{+}\left(\left.\mathfrak{s}\right|_{\partial X_{0}}\right)$ is trivial. In terms of the cohomology actions, the restriction map $H^{2}(X ; \mathbb{Z}) \rightarrow H^{2}\left(\partial X_{0} ; \mathbb{Z}\right)$ is trivial because it factors through $H^{2}(\operatorname{cl} \mathcal{N} ; \mathbb{Z})=$ 0. On each boundary component, this constraint
$$0=c_{1}\left(\operatorname{det} \mathbb{S}_{+}\left(\left.\mathfrak{s}\right|_{S^{1} \times S^{2}}\right)\right)=2 c_{1}\left(\left.E\right|_{S^{1} \times S^{2}}\right)+c_{1}\left(\left.K^{-1}\right|_{S^{1} \times S^{2}}\right)$$
implies
$$c_{1}\left(\left.E\right|_{S^{1} \times S^{2}}\right)=1 \in \mathbb{Z} \cong H^{2}\left(S^{1} \times S^{2} ; \mathbb{Z}\right)$$
because $\left.K^{-1}\right|_{S^{1} \times S^{2}}=\xi_{0}$ with Euler class -2 (see [3, §3.1]). \(\square\)

\subsection*{1.3 Construction of the near-symplectic Gromov invariants}

We now fix a spin-c structure $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$ and choose $\mathcal{N}$ so that $-\partial X_{0}=\partial \mathcal{N}$ is a contact 3-manifold whose contact form is $\lambda_{\mathfrak{s}}$ on each component, an $\mathfrak{s}$-dependent rescaling of $\lambda_{0}$ as provided in [3. Lemma 3.9] such that $\operatorname{Ker} \lambda_{\mathfrak{s}}=\xi_{0}$. A key property of $\lambda_{\mathfrak{s}}$, spelled out in [3, §3.2], is that there is a positive real number ${ }^{3}$
$$\rho_{\mathfrak{s}} \in \mathbb{R}$$
for which all of its Reeb orbits of symplectic action less than $\rho_{\mathfrak{s}}$ are $\rho_{\mathfrak{s}}$-flat (we also say that $\lambda_{\mathfrak{s}}$ itself is $\rho_{\mathfrak{s}}$-flat). The notion of " $L$-flatness" for a given positive real number $L$ is defined in [31, §2.d] and reviewed in [3, §2.5], while its importance is revealed later in Section 3.2 (see Theorem 3.6, in particular).

Define the integer
$$d(\mathfrak{s}):=\frac{1}{4}\left(c_{1}(\mathfrak{s})^{2}-2 \chi(X)-3 \sigma(X)\right)$$
where $c_{1}(\mathfrak{s})$ denotes the first Chern class of the spin-c structure's positive spinor bundle, $\chi(X)$ denotes the Euler characteristic of $X$, and $\sigma(X)$ denotes the signature of $X$. Introduce the set
$$\mathcal{E}_{\omega} \subset H_{2}\left(X_{0}, \partial X_{0} ; \mathbb{Z}\right)$$
of classes represented by symplectically embedded 2-spheres of self-intersection -1 in $X_{0}$ (which is empty if $X$ is minimal).

We now summarize the definition of $G r_{X, \omega}(\mathfrak{s})$ given by [3. Definition 1.8]. The component of the element $\operatorname{Gr}_{X, \omega}(\mathfrak{s})$ in $\Lambda^{p} H^{1}(X ; \mathbb{Z})$ is defined to be zero whenever $d(\mathfrak{s})-p$ is odd or negative, or whenever $E \cdot \tau_{\omega}(\mathfrak{s})<-1$ for some $E \in \mathcal{E}_{\omega}$ (this latter condition is independent of $p$ ). In the remaining cases it is determined by its evaluation on $\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right]$ for a given ordered set of classes $[\bar{\eta}]:=\left\{\left[\eta_{i}\right]\right\}_{i=1}^{p} \subset H_{1}(X ; \mathbb{Z}) /$ Torsion. To specify this evaluation, fix the following data:
\begin{itemize}
\item[-] an ordered set of $p$ disjoint oriented loops $\bar{\eta} \subset X_{0}$ which represent $[\bar{\eta}]$,
\item[-] a set of $\frac{1}{2}(d(\mathfrak{s})-p)$ disjoint points $\bar{z}:=\left\{z_{k}\right\} \subset X_{0}-\bar{\eta}$,
\item[-] a cobordism-admissible almost complex structure $J$ on the completion $\left(\bar{X}_{0}, \omega\right)$ of $\left(X_{0}, \omega\right)$.
\end{itemize}
See [3, §2.2] for the terminology in the third bullet; the completion $\bar{X}_{0}$ is obtained by attaching certain cylindrical ends to the strong symplectic cobordism $\left(X_{0}, \omega\right):(\varnothing, 0) \rightarrow\left(-\partial X_{0}, \lambda_{\mathfrak{s}}\right)$. Given an admissible orbit set $\Theta$ on $\left(-\partial X_{0}, \lambda_{\mathfrak{s}}\right)$ (in the sense of [3, §2.1]) such that its total homology class is $[\Theta]=-\partial \tau_{\omega}(\mathfrak{s})$, we form the moduli space
$$\mathcal{M}_{d(\mathfrak{s})}\left(\varnothing, \Theta ; \tau_{\omega}(\mathfrak{s}), \bar{z}, \bar{\eta}\right)$$
of $J$-holomorphic currents in $\bar{X}_{0}$ that satisfy the following properties: they are asymptotic to $\Theta$ in the sense of [3, §2.2]; they have ECH index $d(\mathfrak{s})$ in the sense of [3, §2.3]; they represent $\tau_{\omega}(\mathfrak{s})$; they intersect every point and loop in $\bar{z} \cup \bar{\eta}$. Thanks to [3, Proposition 3.16], a component of a given current in this moduli space can only be multiply covered if it is a special curve, defined as follows.

Definition 1.5. A $J$-holomorphic curve in $\bar{X}_{0}$ is special if it has Fredholm/ECH index zero, and is either an embedded torus or an embedded plane whose negative end is asymptotic to an embedded elliptic orbit with multiplicity one.

\footnotetext{
${ }^{3}$ The definition of this real number is given by 3. Equation 3-6] with the notation $\rho\left(\tau_{\omega}(\mathfrak{s})\right)$ there.
}

It turns out that $\mathcal{M}_{d(\mathfrak{s})}\left(\varnothing, \Theta ; \tau_{\omega}(\mathfrak{s}), \bar{z}, \bar{\eta}\right)$ is a finite set for generic $J$ (see [3. Proposition 3.13]) and the symplectic action of $\Theta$ is bounded by $\rho_{\mathfrak{s}}$ if this moduli space is nonempty (see [3, §3.2] or [10]). Since there can only be finitely many (nondegenerate) orbit sets with uniformly bounded action, there are only finitely many nonempty moduli spaces $\mathcal{M}_{d(\mathfrak{s})}\left(\varnothing, \Theta ; \tau_{\omega}(\mathfrak{s}), \bar{z}, \bar{\eta}\right)$ indexed by $\Theta$. Moreover, any orbit set $\Theta$ for which the corresponding moduli space is nonempty has an absolute grading as generators of the ECH chain complex $E C C_{*}\left(-\partial X_{0}, \lambda_{\mathfrak{s}}, 1\right)$ (see [3, §2.4]) and they are in fact all of the same grading (see [3, §3.7]). Denote this grading by $g(\mathfrak{s})$.

As a further reminder, each orbit set $\Theta$ comes equipped with a choice of orientation so that the moduli spaces are all coherently oriented (see [3, §2.1, §3.5]). The result of [3, §3.6 ${ }^{4}$ is the following element in the ECH chain complex, whose homology class does not depend on the choice of points $\bar{z}$ nor representatives $\bar{\eta}$ of $[\bar{\eta}]$.

Definition 1.6. With the above setup, the Gromov cycle is
$$\Phi_{G r}:=\sum_{\Theta} \mathcal{M}_{\Theta} \Theta \in E C C_{g(\mathfrak{s})}\left(-\partial X_{0}, \lambda_{\mathfrak{s}}, 1\right)$$
where the sum is over admissible orbit sets $\Theta$ in the grading $g(\mathfrak{s})$ with $[\Theta]=-\partial \tau_{\omega}(\mathfrak{s})$, and the integer coefficient $\mathcal{M}_{\Theta} \in \mathbb{Z}$ is the sum over $\mathcal{C} \in \mathcal{M}_{d(\mathfrak{s})}\left(\varnothing, \Theta ; \tau_{\omega}(\mathfrak{s}), \bar{z}, \bar{\eta}\right)$ of a certain weight $q(\mathcal{C}) \in \mathbb{Z}$ defined in [3, §3.5].

Now, $E C H_{*}\left(-\partial X_{0}, \xi_{0}, 1\right)$ is the tensor product $\bigotimes_{k=1}^{N} E C H_{*}\left(S^{1} \times S^{2}, \xi_{0}, 1\right)$ and this homology is given by [3; Proposition 3.2]. In terms of the absolute grading on $E C H_{*}\left(S^{1} \times S^{2}, \xi_{0}, 1\right)$ by homotopy classes of oriented 2-plane fields on $S^{1} \times S^{2}$ (see [3, §2.4]), there is a unique grading $\left[\xi_{*}\right]$ such that
$$E C H_{\left[\xi_{*}\right]+n}\left(S^{1} \times S^{2}, \xi_{0}, 1\right) \cong \begin{cases}0, & \text { if } n<0 \\ \mathbb{Z}, & \text { otherwise }\end{cases}$$
In the proof of Theorem 5.1 it will be shown that $g(\mathfrak{s})=N\left[\xi_{*}\right]$. That said, $G r_{X, \omega}(\mathfrak{s})\left(\left[\eta_{1}\right] \wedge \cdots \wedge\left[\eta_{p}\right]\right)$ is by definition the coefficient of the class
$$\left[\Phi_{G r}\right] \in E C H_{g(\mathfrak{s})}\left(-\partial X_{0}, \xi_{0}, 1\right) \cong \bigotimes_{k=1}^{N} E C H_{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \xi_{0}, 1\right) \cong \mathbb{Z}$$
as a multiple of the positive generator $\mathbb{1} \in \bigotimes_{k=1}^{N} E C H_{\left[\xi_{*}\right]}\left(S^{1} \times S^{2}, \xi_{0}, 1\right)$.

\subsection*{1.4 Exceptional spheres}

If $E \cdot \tau_{\omega}(\mathfrak{s}) \geq-1$ for all $E \in \mathcal{E}_{\omega}$ then the moduli spaces used to define $\operatorname{Gr}_{X, \omega}(\mathfrak{s})$ do not contain any elements with multiply covered exceptional sphere components (see [3, Proposition 3.16]). However, if $E \cdot \tau_{\omega}(\mathfrak{s})<-1$ for some $E \in \mathcal{E}_{\omega}$ then we cannot rule out their existence, and we define the near-symplectic Gromov invariant to be zero, as is done with Taubes' Gromov invariants of nonminimal symplectic 4-manifolds. What follows is a more general version of the main Theorem 1.2 which does not assume $X$ to be minimal; its proof will subsume the proof of Theorem 1.2.

\footnotetext{
${ }^{4}$ This is an opportune moment to point out a negligible falsity in the proof of [3], Proposition 3.23]; delete the paranthetical phrase "(respectively cylinder)".
}

\begin{figure}
\includegraphics[alt={},max width=\textwidth]{https://cdn.mathpix.com/cropped/d787d2b4-e9c9-4ab7-9c05-44a3a9f294e2-06.jpg?height=324&width=491&top_left_y=249&top_left_x=817}
\captionsetup{labelformat=empty}
\caption{Figure 1: Zero set of near-symplectic form in bold}
\end{figure}

Theorem 1.7. Given $(X, \omega, J)$ and $\mathfrak{s} \in \operatorname{Spin}^{c}(X)$ satisfying $E \cdot \tau_{\omega}(\mathfrak{s}) \geq-1$ for all $E \in \mathcal{E}_{\omega}$,
$$G r_{X, \omega}(\mathfrak{s}) \equiv S W_{X}(\mathfrak{s}) \quad \bmod 2 \quad \in \Lambda^{*} H^{1}(X ; \mathbb{Z}) \otimes \mathbb{Z} / 2 \mathbb{Z}$$
where $\omega$ determines the chamber for defining the Seiberg-Witten invariants when $b_{+}^{2}(X)=1$.

\section*{$1.5 S^{1}$-valued Morse theory}

A basic example of a near-symplectic manifold is $\left(S^{1} \times M, \omega_{f}\right)$, where $M$ is a closed oriented Riemannian 3-manifold with $b^{1}(M)>0$, the metric on $S^{1} \times M$ is the product metric $d t^{2}+g_{M}$, and $\omega_{f}$ is defined momentarily. A result of Honda [6] and of Calabi [1] says that for $g_{M}$ suitably generic, any nonzero class in $H^{1}(M ; \mathbb{Z})$ is represented by a harmonic map $f: M \rightarrow S^{1}$ (i.e. $d^{*} d f=0$ ) with nondegenerate critical points $\operatorname{crit}(f)$ of index 1 or 2, hence a harmonic 1-form $d f$ with transversal zeros. Then
$$\omega_{f}:=d t \wedge d f+*_{3} d f$$
is a closed self-dual 2-form which vanishes transversally on
$$Z_{f}:=S^{1} \times \operatorname{crit}(f)$$
All zero-circles are untwisted, as can be seen by writing out $\omega_{f}$ in local coordinates and comparing to the standard model on $\mathbb{R} \times \mathbb{R}^{3}$. There are an even number of zero-circles, i.e. $1-b^{1}(X)+b_{+}^{2}(X)$ is even, because $b^{1}(X)=b^{1}(M)+1$ and $b^{2}(X)=2 b^{1}(M)$ and $b_{+}^{2}(X)=b^{1}(M)$. Here, we note that
$$H^{1}(M ; \mathbb{R}) \rightarrow H_{+}^{2}(X ; \mathbb{R}), \quad a \mapsto[d t \wedge a]^{+}=\frac{1}{2}\left(d t \wedge a+*_{3} a\right)$$
is an isomorphism.
After equipping $\left(S^{1} \times M\right)-Z_{f}=S^{1} \times(M-\operatorname{crit}(f))$ with the compatible almost complex structure $J$ determined by $\omega_{f}$ and $d t^{2}+g_{M}$, the $S^{1}$-invariant connected $J$-holomorphic submanifolds are of the form $C=S^{1} \times \gamma$, where $\gamma$ is a single gradient flowline of $\nabla f$. Since the Morse trajectories in $M$ are either periodic orbits (with periodicity) or paths between critical points, $C$ is either a torus (with multiplicity) or a cylinder which bounds two zero-circles in $S^{1} \times M$ (see Figure 1).

In their PhD theses, Hutchings and Lee built a 3-dimensional invariant $I_{M, f}$ of $M$ which suitably counts the gradient flowlines (see [8, 11, 12]), and they further showed that it equals a version of topological (Reidemeister) torsion defined by Turaev [37]. It was subsequently shown by Turaev that this Reidemeister torsion equals the 3-dimensional SW invariant $S W_{M}$ of $M$ (see [36]). Strictly speaking, there is a required choice of "chamber" (determined by $f$ ) with which to define $S W_{M}$
when $b^{1}(M)=1$, and an ordering of the set $\operatorname{crit}(f)$ with which to define $I_{M, f}$. While $S W_{M}$ is a function of the set $\operatorname{Spin}^{c}(M)$ of spin-c structures, $I_{M, f}$ is a function of the set
$$\left\{\eta \in H_{1}(M, \operatorname{crit}(f) ; \mathbb{Z}) \mid \partial \eta=[\operatorname{crit}(f)]\right\}$$
and there exists an $H_{1}(M)$-equivariant isomorphism $\tau_{f}$ between them (see [11, Lemma 4.3]). In summary,

Theorem 1.8 (Hutchings-Lee-Turaev). Let $(M, f)$ be as above. Then for all $\mathfrak{s} \in \operatorname{Spin}^{c}(M)$,
$$I_{M, f}\left(\tau_{f}(\mathfrak{s})\right)= \pm S W_{M}(\mathfrak{s}) \in \mathbb{Z}$$
where $f$ determines the chamber for defining $S W_{M}$ when $b^{1}(M)=1$. The global ± sign is pinned down by a suitable choice of ordering of $\operatorname{crit}(f)$.

Now, we can recover Theorem 1.8 (over $\mathbb{Z} / 2 \mathbb{Z}$ ) without having to pass through Reidemeister torsion, via a dimensional reduction of Theorem $1.2{ }^{5}$ It was shown in [22, Theorem 3.5] that the 4-dimensional SW invariant ${ }^{6}$ recovers the 3-dimensional SW invariant: all solutions to the SW equations on $S^{1} \times M$ associated with product spin-c structures are $S^{1}$-invariant. It will be shown elsewhere [4] that the near-symplectic Gromov invariant recovers Hutchings-Lee's flowline invariant.

Corollary 1.9 ([4]). Let $(M, f)$ be as above, and let $\pi: S^{1} \times M \rightarrow M$ be the projection map onto the second factor. Fix an ordering of the critical points of $f$ (hence of the zero-circles of $\omega_{f}$ ). Then
$$I_{M, f}(\mathfrak{s})=\operatorname{Gr}_{S^{1} \times M, \omega_{f}}\left(\pi^{*} \mathfrak{s}\right) \equiv_{(2)} S W_{S^{1} \times M}\left(\pi^{*} \mathfrak{s}\right)=S W_{M}(\mathfrak{s})$$
for all $\mathfrak{s} \in \operatorname{Spin}^{c}(M)$. When $b^{1}(M)=b_{+}^{2}\left(S^{1} \times M\right)=1$, the chamber is determined by $f$ (hence $\omega_{f}$ ).
Remark 1.10. In fact, when $f$ has no critical points (hence $\omega_{f}$ is symplectic) the proof of this corollary was already known [12, Remark 1.10]. The first instance appeared in [24] for the special case of a mapping torus of a symplectomorphism of a Riemann surface, in which Salamon showed that the 3-dimensional SW invariants recover the Lefschetz invariants of the symplectomorphism.

We end this discussion with a brief sketch of the first equality in Corollary 1.9. While the gradient flowlines for $I_{M, f}$ sit inside $M$, the $J$-holomorphic curves for $G r_{S^{1} \times M, \omega_{f}}$ do not sit inside $S^{1} \times M$ but rather inside the completion of the complement of $Z_{f}$. Explicitly, we choose a 3-ball neighborhood $\bigsqcup_{k} B^{3}$ of the critical points of $f$, hence a tubular neighborhood $\mathcal{N}=S^{1} \times \bigsqcup_{k} B^{3}$ of the zero-circles in $Z_{f}$. Then
$$X_{0}:=\left(S^{1} \times M\right)-\mathcal{N}=S^{1} \times\left(M-\bigsqcup_{k} B^{3}\right)$$
is a symplectic manifold and $H_{2}\left(X_{0}, \partial X_{0} ; \mathbb{Z}\right)$ is isomorphic to a direct sum of $|\operatorname{crit}(f)|$ copies of
$$H_{2}\left(S^{1} \times\left(M-B^{3}\right), S^{1} \times S^{2} ; \mathbb{Z}\right) \cong H_{2}\left(M-B^{3}, S^{2} ; \mathbb{Z}\right) \oplus H_{1}\left(M-B^{3}, S^{2} ; \mathbb{Z}\right)$$

\footnotetext{
${ }^{5}$ This was in fact an expectation and also the motivation, as explained in 11. §4.2.1].
${ }^{6}$ There is a canonical homology orientation on 4-manifolds of the form $S^{1} \times M$.
}
using the relative Künneth formula. Given the relative 1st homology class $\tau_{f}(\mathfrak{s}) \in H_{1}(M, \operatorname{crit}(f) ; \mathbb{Z})$, the corresponding relative 2nd homology class is
$$\left[S^{1}\right] \times \tau_{f}(\mathfrak{s})=\tau_{\omega_{f}}\left(\pi^{*} \mathfrak{s}\right) \in H_{2}\left(X_{0}, \partial X_{0} ; \mathbb{Z}\right)$$

Since the contact form $\lambda_{0}$ of Section 1.2 is actually $S^{1}$-invariant, it follows from [3] that we can choose the 3-balls in such a way that $-\partial X_{0}$ is a contact boundary of $X$ with $\omega_{f}$ equal to a scalar multiple of $d \lambda_{0}$ on each component. Although the playground $\left(X_{0}, \omega_{f}, J, \tau_{\omega_{f}}\left(\pi^{*} \mathfrak{s}\right)\right)$ is $S^{1}$-invariant, the calculation of $G r_{S^{1} \times M, \omega_{f}}\left(\tau_{\omega_{f}}\left(\pi^{*} \mathfrak{s}\right)\right)$ requires us to modify $\lambda_{0}$ (and $\partial X_{0}$ ) into a non- $S^{1}$-invariant nondegenerate contact form $\lambda_{\mathfrak{s}}$, so $\left(-\partial X_{0}, \lambda_{\mathfrak{s}}\right)$ does not arise from any choice of the 3-balls. This is a complication because we would like to lift flowlines $\gamma \subset M$ to $S^{1}$-invariant curves $S^{1} \times \gamma \subset X_{0}$ and count them. Nonetheless, a limiting argument will show that we can perturb the $S^{1}$-invariant setup to the non- $S^{1}$-invariant setup and relate the corresponding pseudoholomorphic curves.

\section*{2 Review of gauge theory}

The point of this section is to introduce most of the terminology and notations that appear in the later sections. Further information and more complete details are found in [13, 16].

\subsection*{2.1 Closed 3-manifolds}

Let $(Y, \lambda)$ be a closed oriented connected contact 3-manifold, and choose an almost complex structure $J$ on $\xi$ that induces a symplectization-admissible almost complex structure on $\mathbb{R} \times Y$. There is a compatible metric $g$ on $Y$ such that ${ }^{7}|\lambda|=1$ and $* \lambda=\frac{1}{2} d \lambda$, with $g(v, w)=\frac{1}{2} d \lambda(v, J w)$ for $v, w \in \xi$.

View a spin-c structure $\mathfrak{s}$ on $Y$ as an isomorphism class of a pair $(\mathbb{S}, \mathrm{cl})$ consisting of a rank 2 Hermitian vector bundle $\mathbb{S} \rightarrow Y$ and Clifford multiplication cl : $T Y \rightarrow \operatorname{End}(\mathbb{S})$. We refer to $\mathbb{S}$ as the spinor bundle and its sections as spinors. The set $\operatorname{Spin}^{c}(Y)$ of spin-c structures is an affine space over $H^{2}(Y ; \mathbb{Z})$, defined by
$$(\mathbb{S}, \mathrm{cl})+x=\left(\mathbb{S} \otimes E^{x}, \operatorname{cl} \otimes \mathbb{1}\right)$$
where $E^{x} \rightarrow Y$ is the complex line bundle satisfying $c_{1}\left(E^{x}\right)=x \in H^{2}(Y ; \mathbb{Z})$. Denote by $c_{1}(\mathfrak{s})$ the first Chern class of $\operatorname{det} \mathbb{S}$; it satisfies $c_{1}(\mathfrak{s}+x)=c_{1}(\mathfrak{s})+2 x$.

The contact structure $\xi$ (and more generally, any oriented 2-plane field on $Y$ ) picks out a canonical spin-c structure $\mathfrak{s}_{\xi}=\left(\mathbb{S}_{\xi}, \mathrm{cl}\right)$ with $\mathbb{S}_{\xi}=\underline{\mathbb{C}} \oplus \xi$, where $\underline{\mathbb{C}} \rightarrow Y$ denotes the trivial line bundle, and Clifford multiplication is defined as follows. Given an oriented orthonormal frame $\left\{e_{1}, e_{2}, e_{3}\right\}$ for $T_{y} Y$ such that $\left\{e_{2}, e_{3}\right\}$ is an oriented orthonormal frame for $\xi_{y}$, then in terms of the basis $\left(1, e_{2}\right)$ for $\mathbb{S}_{\xi}$,
$$\operatorname{cl}\left(e_{1}\right)=\left(\begin{array}{cc}
i & 0 \\
0 & -i
\end{array}\right), \quad \operatorname{cl}\left(e_{2}\right)=\left(\begin{array}{cc}
0 & -1 \\
1 & 0
\end{array}\right), \quad \operatorname{cl}\left(e_{3}\right)=\left(\begin{array}{cc}
0 & i \\
i & 0
\end{array}\right)$$
There is then a canonical isomorphism
$$H^{2}(Y ; \mathbb{Z}) \rightarrow \operatorname{Spin}^{c}(Y), \quad x \mapsto\left(E^{x} \oplus\left(\xi \otimes E^{x}\right), \mathrm{cl}\right)$$

\footnotetext{
${ }^{7}$ The factors of $\frac{1}{2}$ can be dropped or changed to any other nonzero real number by a particular rescaling of the metric, but they will be left in to be consistent with the papers of Taubes and Hutchings.
}
where the 0 class corresponds to $\mathfrak{s}_{\xi}$. In other words, there is a canonical decomposition $\mathbb{S}=E \oplus \xi E$ into $\pm i$ eigenbundles of $\operatorname{cl}(\lambda)$. Here and in what follows, the tensor product notation is suppressed.

A spin-c connection is a connection $\mathbf{A}$ on $\mathbb{S}$ which is compatible with Clifford multiplication in the sense that
$$\nabla_{\mathbf{A}}(\operatorname{cl}(v) \psi)=\operatorname{cl}(\nabla v) \psi+\operatorname{cl}(v) \nabla_{\mathbf{A}} \psi$$
where $\nabla v$ denotes the covariant derivative of $v \in T Y$ with respect to the Levi-Civita connection. Such a connection is equivalent to a Hermitian connection (also denoted by $\mathbf{A}$ ) on $\operatorname{det} \mathbb{S}$, and determines a Dirac operator
$$D_{\mathbf{A}}: \Gamma(\mathbb{S}) \xrightarrow{\nabla_{\mathbf{A}}} \Gamma\left(T^{*} Y \otimes \mathbb{S}\right) \xrightarrow{\mathrm{cl}} \Gamma(\mathbb{S})$$
With respect to the decomposition $\mathbb{S}=E \oplus \xi E$, the determinant line bundle is $\operatorname{det} \mathbb{S}=\xi E^{2}$ and any spinor can be written as
$$\psi=(\alpha, \beta)$$
There is a unique connection $A_{\xi}$ on $\xi$ such that its Dirac operator kills the spinor $(1,0) \in \Gamma\left(\mathbb{S}_{\xi}\right)$, and on $\operatorname{det} \mathbb{S}$ there is a canonical decomposition
$$\mathbf{A}=A_{\xi}+2 A$$
with Hermitian connection $A$ on $E$. We henceforth refer to a spin-c connection as a Hermitian connection on $E$, and denote its Dirac operator by $D_{A}$.

The gauge group $C^{\infty}\left(Y, S^{1}\right)$ acts on a given pair $(A, \psi)$ by
$$u \cdot(A, \psi)=\left(A-u^{-1} d u, u \psi\right)$$
In this paper, a configuration $\mathfrak{c}$ refers to a gauge-equivalence class of such a pair, and the set of configurations is denoted by
$$\mathcal{B}(Y, \mathfrak{s}):=(\operatorname{Conn}(E) \times \Gamma(\mathbb{S})) / C^{\infty}\left(Y, S^{1}\right)$$

Fix a suitably generic exact 2-form $\mu \in \Omega^{2}(Y)$ as described in [13, §2.2], and a positive real number $r \in \mathbb{R}$. A configuration $\mathfrak{c}$ solves Taubes' perturbed Seiberg-Witten equations when
$$D_{\mathbf{A}} \psi=0, \quad * F_{A}=r(\tau(\psi)-i \lambda)-\frac{1}{2} * F_{A_{\xi}}+i * \mu$$
where $F_{A_{\xi}}$ is the curvature of $A_{\xi}$ and $\tau: \mathbb{S} \rightarrow i T^{*} Y$ is the quadratic bundle map
$$\tau(\psi)(\cdot)=\langle\operatorname{cl}(\cdot) \psi, \psi\rangle$$
An appropriate change of variables recovers the usual Seiberg-Witten equations (with perturbations) that appear in [16].

Remark 2.1. There are additional "abstract tame perturbations" to these equations required to obtain transversality of the moduli spaces of its solutions (see [16, §10]), but they have been suppressed because they do not interfere with the analysis presented in this paper. Further clarification on this matter can be found in [13, §2.1] and [31, §3.h.5], where the same suppression occurs.

Denote by $\mathfrak{M}(Y, \mathfrak{s})$ the set of solutions to (2.1), called (SW) monopoles. A solution is reducible if its spinor component vanishes, and is otherwise irreducible. After attaching orientations (this being a $\mathbb{Z} / 2 \mathbb{Z}$ choice for each monopole, see Section 2.5), the monopoles freely generate the monopole Floer chain complex $\widehat{C M}^{*}(Y, \lambda, \mathfrak{s}, J, r)$. The chain complex differential will not be reviewed here. Of importance to this paper are irreducible monopoles with certain bounds on their energy
$$E(\mathfrak{c}):=i \int_{Y} \lambda \wedge F_{A}$$
Denote by $\widehat{C M}_{L}^{*}(Y, \lambda, \mathfrak{s}, J, r)$ the submodule generated by irreducible monopoles $\mathfrak{c}$ with energy $E(\mathfrak{c})<2 \pi L$. When $r$ is sufficiently large, $\widehat{C M}_{L}^{*}(Y, \lambda, \mathfrak{s}, J, r)$ is a subcomplex of $\widehat{C M}^{*}(Y, \lambda, \mathfrak{s}, J, r)$ and the homology $\widehat{H M}_{L}^{*}(Y, \lambda, \mathfrak{s}, J, r)$ is well-defined and independent of $r$ and $\mu$ (see [13, §2.3]). Taking the direct limit over $L>0$, we recover the ordinary $\widehat{H M}^{*}(Y, \mathfrak{s})$ in [16] which is independent of $\lambda$ and $J$. It is sometimes convenient to consider the group
$$\widehat{H M}^{*}(Y):=\bigoplus_{\mathfrak{s} \in \operatorname{Spin}^{c}(Y)} \widehat{H M}^{*}(Y, \mathfrak{s})$$
over all spin-c structures at once.

\subsection*{2.2 Symplectic cobordisms}

Let $(X, \omega)$ be a strong symplectic cobordism between (possibly disconnected or empty) closed oriented contact 3-manifolds $\left(Y_{ \pm}, \lambda_{ \pm}\right)$. Due to the choice of metric $g_{ \pm}$on $Y_{ \pm}$in Section 2.1 (and following [13, §4.2]), we do not extend $\omega$ over $\bar{X}$ using $d\left(e^{s} \lambda_{ \pm}\right)$on the ends $(-\infty, 0] \times Y_{-}$and $[0, \infty) \times Y_{+}$. Instead, we extend $\omega$ using $d\left(e^{2 s} \lambda_{ \pm}\right)$as follows. Fix a smooth increasing function $\phi_{-}:(-\infty, \varepsilon] \rightarrow(-\infty, \varepsilon]$ with $\phi_{-}(s)=2 s$ for $s \leq \frac{\varepsilon}{10}$ and $\phi_{-}(s)=s$ for $s>\frac{\varepsilon}{2}$, and fix a smooth increasing function $\phi_{+}:[-\varepsilon, \infty) \rightarrow[-\varepsilon, \infty)$ with $\phi_{+}(s)=2 s$ for $s \geq-\frac{\varepsilon}{10}$ and $\phi_{+}(s)=s$ for $s \leq-\frac{\varepsilon}{2}$, where $\varepsilon>0$ is such that $\omega=d\left(e^{s} \lambda_{ \pm}\right)$on the $\varepsilon$-collars of $Y_{ \pm}$. Then the desired extension is
$$\tilde{\omega}:= \begin{cases}d\left(e^{\phi_{-}} \lambda_{-}\right) & \text {on }(-\infty, \varepsilon] \times Y_{-} \\ \omega & \text { on } X \backslash\left(\left([0, \varepsilon] \times Y_{-}\right) \cup\left([-\varepsilon, 0] \times Y_{+}\right)\right) \\ d\left(e^{\phi_{+}} \lambda_{+}\right) & \text {on }[-\varepsilon, \infty) \times Y_{+}\end{cases}$$
Now choose a cobordism-admissible almost complex structure $J$ on $(\bar{X}, \tilde{\omega})$. Following [13, §4.2], we equip $\bar{X}$ with a particular metric $g$ so that it agrees with the product metric with $g_{ \pm}$on the ends $(-\infty, 0] \times Y_{-}$and $[0, \infty) \times Y_{+}$and so that $\tilde{\omega}$ is self-dual. Finally, define
$$\widehat{\omega}:=\sqrt{2} \tilde{\omega} /|\tilde{\omega}|_{g}$$
and note that $J$ is still cobordism-admissible.
The 4 -dimensional gauge-theoretic scenario is analogous to the 3 -dimensional scenario. View a spin-c structure $\mathfrak{s}$ on $X$ as an isomorphism class of a pair $(\mathbb{S}, \mathrm{cl})$ consisting of a Hermitian vector bundle $\mathbb{S}=\mathbb{S}_{+} \oplus \mathbb{S}_{-}$, where $\mathbb{S}_{ \pm}$have rank 2, and Clifford multiplication cl : $T X \rightarrow \operatorname{End}(\mathbb{S})$ such that $\operatorname{cl}(v)$ exchanges $\mathbb{S}_{+}$and $\mathbb{S}_{-}$for each $v \in T X$. We refer to $\mathbb{S}_{+}$as the positive spinor bundle and its sections as (positive) spinors. The set $\operatorname{Spin}^{c}(X)$ of spin-c structures is an affine
space over $H^{2}(X ; \mathbb{Z})$, and we denote by $c_{1}(\mathfrak{s})$ the first Chern class of $\operatorname{det} \mathbb{S}_{+}=\operatorname{det} \mathbb{S}_{-}$. A spin-c connection on $\mathbb{S}$ is equivalent to a Hermitian connection A on $\operatorname{det} \mathbb{S}_{+}$and defines a Dirac operator $D_{\mathbf{A}}: \Gamma\left(\mathbb{S}_{ \pm}\right) \rightarrow \Gamma\left(\mathbb{S}_{\mp}\right)$.

A spin-c structure $\mathfrak{s}$ on $X$ restricts to a spin-c structure $\left.\mathfrak{s}\right|_{Y_{ \pm}}$on $Y_{ \pm}$with spinor bundle $\mathbb{S}_{Y_{ \pm}}:=$ $\left.\mathbb{S}_{+}\right|_{Y_{ \pm}}$and Clifford multiplication $\operatorname{cl}_{Y_{ \pm}}(\cdot):=\operatorname{cl}(v)^{-1} \operatorname{cl}(\cdot)$, where $v$ denotes the outward-pointing unit normal vector to $Y_{+}$and the inward-pointing unit normal vector to $Y_{-}$. There is a canonical way to extend $\mathfrak{s}$ over $\bar{X}$, and the resulting spin-c structure is also denoted by $\mathfrak{s}$. There is a canonical decomposition $\mathbb{S}_{+}=E \oplus K^{-1} E$ into $\mp 2 i$ eigenbundles of $\operatorname{cl}_{+}(\widehat{\omega})$, where $K$ is the canonical bundle of $(\bar{X}, J)$ and $\mathrm{cl}_{+}: \bigwedge_{+}^{2} T^{*} \bar{X} \rightarrow \operatorname{End}\left(\mathbb{S}_{+}\right)$is the projection of Clifford multiplication onto $\operatorname{End}\left(\mathbb{S}_{+}\right)$. This agrees with the decomposition of $\mathbb{S}_{Y_{ \pm}}$on the ends of $\bar{X}$.

The symplectic form $\omega$ picks out the canonical spin-c structure $\mathfrak{s}_{\omega}=\left(\mathbb{S}_{\omega}, \mathrm{cl}\right)$, namely that for which $E$ is trivial, and the $H^{2}(X ; \mathbb{Z})$-action on $\operatorname{Spin}^{c}(X)$ becomes a canonical isomorphism. There is a unique connection $A_{K^{-1}}$ on $K^{-1}$ such that its Dirac operator annihilates the spinor $(1,0) \in \Gamma\left(\left(\mathbb{S}_{\omega}\right)_{+}\right)$, and we henceforth identify a spin-c connection with a Hermitian connection $A$ on $E$ and denote its Dirac operator $D_{A}$.

In this paper, a configuration $\mathfrak{d}$ refers to a gauge-equivalence class of a pair $(\mathbf{A}, \Psi)$ under the gauge group $C^{\infty}\left(X, S^{1}\right)$-action. A connection $\mathbf{A}$ on $\operatorname{det} \mathbb{S}_{+}$is in temporal gauge on the ends of $\bar{X}$ if
$$\nabla_{\mathbf{A}}=\frac{\partial}{\partial s}+\nabla_{\mathbf{A}(s)}$$
on $(-\infty, 0] \times Y_{-}$and $Y_{+} \times[0, \infty)$, where $\mathbf{A}(s)$ is a connection on $\operatorname{det} \mathbb{S}_{Y_{ \pm}}$depending on $s$. Any connection can be placed into temporal gauge by an appropriate gauge transformation. Given monopoles $\mathfrak{c}_{ \pm}$on $Y_{ \pm}$, the set of configurations which are asymptotic to $\mathfrak{c}_{ \pm}$(in temporal gauge on the ends of $\bar{X}$ ) is denoted by
$$\mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right) \subset\left(\operatorname{Conn}(E) \times \Gamma\left(\mathbb{S}_{+}\right)\right) / C^{\infty}\left(X, S^{1}\right)$$

Fix suitably generic exact 2-forms $\mu_{ \pm} \in \Omega^{2}\left(Y_{ \pm}\right)$, a suitably generic exact 2-form $\mu \in \Omega^{2}(\bar{X})$ that agrees with $\mu_{ \pm}$on the ends of $\bar{X}$ (with $\mu_{*}$ denoting its self-dual part), and a positive real number $r \in \mathbb{R}$. Taubes' perturbed Seiberg-Witten equations for a configuration $\mathfrak{d}$ are
$$D_{\mathbf{A}} \Psi=0, \quad F_{A}^{+}=\frac{r}{2}(\rho(\Psi)-i \widehat{\omega})-\frac{1}{2} F_{A_{K-1}}^{+}+i \mu_{*}$$
where $F_{A}^{+}$is the self-dual part of the curvature of $A$ and $\rho: \mathbb{S}_{+} \rightarrow i \bigwedge_{+}^{2} T^{*} X$ is the quadratic bundle map
$$\rho(\Psi)(\cdot, \cdot)=-\frac{1}{2}\langle[\operatorname{cl}(\cdot), \operatorname{cl}(\cdot)] \Psi, \Psi\rangle$$
Similarly to the 3 -dimensional equations, there are additional "abstract tame perturbations" which have been suppressed in this paper (see [16, §24.1]). Denote by $\mathfrak{M}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ the set of solutions to (2.2) in $\mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$, called (SW) instantons.

Similarly to ECH, an "index" is associated with each SW instanton, namely the local expected dimension of the moduli space of SW instantons. Denote by $\mathfrak{M}_{k}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ the subset of elements in $\mathfrak{M}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ that have index $k$.

\subsection*{2.3 Closed 4-manifolds}

The case $\left(Y_{ \pm}, \lambda_{ \pm}\right)=(\varnothing, 0)$ recovers Seiberg-Witten theory on closed oriented symplectic 4-manifolds. In general, for closed oriented Riemannian 4-manifolds $(X, g)$, we can recover Seiberg-Witten theory from the above setup by ignoring the appearance of $\omega$ and thus ignoring the canonical decomposition of $\mathbb{S}_{+}$. The set of spin-c structures is then only an $H^{2}(X ; \mathbb{Z})$-torsor. A configuration $\mathfrak{d}=[\mathbf{A}, \Psi] \in \mathcal{B}(X, \mathfrak{s})$ solves the (perturbed) Seiberg-Witten equations when
$$D_{\mathbf{A}} \Psi=0, \quad F_{\mathbf{A}}^{+}=\frac{1}{4} \rho(\Psi)+i \mu$$
where $\mu \in \Omega_{+}^{2}(X)$ is now a self-dual 2-form. Denote the space of solutions to (2.3) by $\mathfrak{M}(\mathfrak{s})$.
When $b_{+}^{2}(X)>0$, a generic choice of $\mu$ makes $\mathfrak{M}(\mathfrak{s})$ a finite-dimensional compact orientable smooth manifold, where the orientation is determined by a homology orientation of $X$ (see also Section 2.5), this being an orientation of
$$\operatorname{det}^{+}(X):=\operatorname{det} H^{1}(X ; \mathbb{R}) \otimes \operatorname{det} H_{+}^{2}(X ; \mathbb{R})$$
As explained in [29, §1.c], if $X$ is equipped with a symplectic form then there is a canonical homology orientation.

The dimension of $\mathfrak{M}(\mathfrak{s})$ is equal to the integer $d(\mathfrak{s})$ given by (1.2), and its parity is equal to the parity of
$$1-b^{1}(X)+b_{+}^{2}(X)$$
If $\operatorname{dim} \mathfrak{M}(\mathfrak{s})<0$, then $\mathfrak{M}(\mathfrak{s})$ is empty and the Seiberg-Witten invariant $S W_{X}(\mathfrak{s})$ is defined to be zero. In the remaining cases, the Seiberg-Witten invariant $S W_{X}(\mathfrak{s})$ is an element of $\Lambda^{*} H^{1}(X ; \mathbb{Z})$ and given by suitable counts of points in $\mathfrak{M}(\mathfrak{s})$ (see the upcoming Definition 2.3). For example, if $\operatorname{dim} \mathfrak{M}(\mathfrak{s})=0$ then $S W_{X}(\mathfrak{s}) \in \mathbb{Z}$ is the signed count of the finite number of oriented points in $\mathfrak{M}(\mathfrak{s})$.

\subsection*{2.3.1 Choice of "chamber"}

When $b_{+}^{2}(X)>1$, the value of the Seiberg-Witten invariant is a diffeomorphism invariant of $X$ independent of the choice of generic pairs $(g, \mu) \in \operatorname{Met}(X) \times \Omega_{+}^{2}(X)$, where $\operatorname{Met}(X)$ denotes the Fréchet space of smooth Riemannian metrics on $X$. When $b_{+}^{2}(X)=1$, there is a "wall-crossing phenomenon" as follows. Denote by $\omega_{g}$ the unique (up to scalar multiplication) nontrivial near-symplectic form with respect to $g$. The set of pairs $(g, \mu)$ satisfying the constraint
$$2 \pi\left[\omega_{g}\right] \cdot c_{1}(\mathfrak{s})+\int_{X} \omega_{g} \wedge \mu=0$$
defines a "wall" which separates $\operatorname{Met}(X) \times \Omega_{+}^{2}(X)$ into two open sets, called $c_{1}(\mathfrak{s})$-chambers. The Seiberg-Witten invariant is constant on any $c_{1}(\mathfrak{s})$-chamber, and the difference between chambers is computable.

The near-symplectic form $\omega$ on $X$ picks out a canonical $c_{1}(\mathfrak{s})$-chamber, namely those pairs $(g, \mu)$ for which the left hand side of (2.4) is negative. This is the chamber that pertains to the large $r$ version of Taubes' perturbed Seiberg-Witten equations (2.2) over the completion of $\left(X_{0}, \omega\right)$ and subsequently used to state our main Theorem 1.2.

\subsection*{2.4 Kronheimer-Mrowka's formalism}

The previous sections concerned the setup of Seiberg-Witten theory from the point of view of symplectic geometry, using Taubes' large perturbations. We now briefly review some relevant aspects of Seiberg-Witten theory from the point of view of Kronheimer-Mrowka's monopole Floer homology, following closely the notations from [16] and deferring to [16] for their precise definitions.

Let $\mathcal{B}(Y, \mathfrak{s})$ denote the space of configurations $[\mathbf{A}, \psi]$. Since we are not taking large perturbations to the Seiberg-Witten equations, we have to deal with the reducible locus $\mathcal{B}^{\text {red }}(Y, \mathfrak{s})$ which prevents $\mathcal{B}(Y, \mathfrak{s})$ from being a Banach manifold. This is done by forming the blow-up $\mathcal{B}^{\sigma}(Y, \mathfrak{s})$, the space of configurations $[\mathbf{A}, s, \psi]$ such that $s \in \mathbb{R}^{\geq 0}$ and $\|\psi\|_{2}=1$, equipped with the blow-down map
$$\mathcal{B}^{\sigma}(Y, \mathfrak{s}) \rightarrow \mathcal{B}(Y, \mathfrak{s}), \quad[\mathbf{A}, s, \psi] \mapsto[\mathbf{A}, s \psi]$$
This is a Banach manifold whose boundary $\partial \mathcal{B}^{\sigma}(Y, \mathfrak{s})$ consists of reducible configurations (where $s=0$ ). The same setup applies to the case that $X$ is a closed 4-manifold. The integral cohomology ring $H^{*}\left(\mathcal{B}^{\sigma}(M, \mathfrak{s}) ; \mathbb{Z}\right)$, for $M$ either $Y$ or $X$, is isomorphic to the graded algebra
$$\mathbb{A}(M):=\left(\Lambda^{*} H_{1}(M ; \mathbb{Z}) / \text { Torsion }\right) \otimes \mathbb{Z}[U]$$
where $U$ is a 2-dimensional generator (see [16, Proposition 9.7.1]).
We can construct a certain vector field $\mathcal{V}^{\sigma}$ on $\mathcal{B}^{\sigma}(Y, \mathfrak{s})$ using the pull-back of the gradient of the Chern-Simons-Dirac functional $\mathcal{L}_{\mathrm{CSD}}: \mathcal{B}(Y, \mathfrak{s}) \rightarrow \mathbb{R}$ (see [16, §4.1]). Strictly speaking, the Chern-Simons-Dirac functional is not well-defined on $\mathcal{B}(Y, \mathfrak{s})$ unless $c_{1}(\mathfrak{s})$ is torsion, but such spin-c structures are the only ones relevant to this paper. Likewise, the perturbed gradient $\operatorname{grad} \mathcal{L}_{\mathrm{CSD}}+\mathfrak{q}$ gives rise to a vector field $\mathcal{V}^{\sigma}+\mathfrak{q}^{\sigma}$, where $\mathfrak{q}$ is an "abstract tame perturbation" (see [16, §10]). We always assume that $\mathfrak{q}$ is chosen from a residual subset of the Banach space of 'large' tame perturbations introduced in [16, Theorem 11.6.1, Definition 11.6.3] so that all stationary points of $\mathcal{V}^{\sigma}+\mathfrak{q}^{\sigma}$ are nondegenerate (by [16, Theorem 12.1.2]).

The critical points (i.e. stationary points) of $\mathcal{V}^{\sigma}+\mathfrak{q}^{\sigma}$ are either irreducibles of the form $[\mathbf{A}, s, \psi]$ with $s>0$ and $[\mathbf{A}, s \psi] \in \operatorname{crit}\left(\operatorname{grad} \mathcal{L}_{\mathrm{CSD}}+\mathfrak{q}\right)$, or reducibles of the form $[\mathbf{A}, 0, \psi]$ with $\psi$ an eigenvector of $D_{\mathbf{A}}$. A reducible is boundary-stable (respectively, boundary-unstable) if the corresponding eigenvalue is positive (respectively, negative). Denote by
$$\mathfrak{C}(Y, \mathfrak{s})=\mathfrak{C}^{o}(Y, \mathfrak{s}) \sqcup \mathfrak{C}^{u}(Y, \mathfrak{s}) \sqcup \mathfrak{C}^{\mathfrak{s}}(Y, \mathfrak{s})$$
the decomposition of the set of critical points into the respective sets of irreducibles and boundary(un)stable reducibles. We can package these critical points together in various ways to form the monople Floer (co)homologies, such as $\widehat{H M}^{*}(Y, \mathfrak{s})$ and $\widehat{H M}^{*}(Y, \mathfrak{s})$ - the former cochain complex is generated by $\mathfrak{C}^{o}(Y, \mathfrak{s}) \sqcup \mathfrak{C}^{s}(Y, \mathfrak{s})$ while the latter complex is generated by $\mathfrak{C}^{o}(Y, \mathfrak{s}) \sqcup \mathfrak{C}^{u}(Y, \mathfrak{s})$, both equipped with coherent choices of orientations (see Section 2.5). The differentials will not be reviewed here, but we do assume in this paper that all perturbations $\mathfrak{q}$ are chosen so that the differentials are well-defined.

Remark 2.2. If $\mathfrak{q}$ is one of Taubes' sufficiently large perturbations associated with a contact form (given in Section 2.1), then the image of $\mathfrak{C}(Y, \mathfrak{s})$ under the blow-down map is $\mathfrak{M}(Y, \mathfrak{s})$. In fact, we no longer need to use the blow-up model thanks to the direct limit description in Section 2.1.

Let $X$ either be a closed 4-manifold or have boundary $Y$. There is a partially-defined restriction map $r: \mathcal{B}^{\sigma}(X, \mathfrak{s}) \longrightarrow \mathcal{B}^{\sigma}(Y, \mathfrak{s})$ whose domain consists of those configurations $[\mathbf{A}, s, \Psi]$ satisfying $\Psi_{Y}:=\left.\Psi\right|_{Y} \neq 0$, such that
$$r([\mathbf{A}, s, \Psi])=\left[\left.\mathbf{A}\right|_{Y}, s\left\|\Psi_{Y}\right\|_{2}, \Psi_{Y} /\left\|\Psi_{Y}\right\|_{2}\right]$$
Similarly, if $X=[0,1] \times Y$ then there is a family of restriction maps $r_{t}: \mathcal{B}^{\sigma}(X, \mathfrak{s}) \longrightarrow \mathcal{B}^{\sigma}(Y, \mathfrak{s})$ for $t \in[0,1]$. If we instead work over $\mathbb{R} \times Y$ or cylindrical ends such as $(-\infty, 0] \times Y$, then we need to use $L_{k, l o c}^{2}$-norms (see [16, §13]).

With respect to a cylindrical completion $\bar{X}$ of $X$, the unperturbed Seiberg-Witten equations (2.3) on $\mathcal{B}(\bar{X}, \mathfrak{s})$ now take the form
$$D_{\mathbf{A}} \Psi=0, \quad F_{\mathbf{A}}^{+}=s^{2} \frac{1}{4} \rho(\Psi)$$
on $\mathcal{B}^{\sigma}(\bar{X}, \mathfrak{s})$. It is explained in [16, §24.1] how to define abstract perturbations $\mathfrak{p}^{\sigma}$ to (2.5) from abstract perturbations $\mathfrak{p}$ to (2.3). In the "cylindrical" case $\bar{X}=\mathbb{R} \times Y$ with spin-c structure induced from $\mathfrak{s}$ on $Y$ and $t$-independent abstract perturbation $\mathfrak{p}$ (see [16, Definition 10.1.1]) induced from an abstract tame perturbation on $Y$, any solution $\mathfrak{d}$ to the $\mathfrak{p}^{\sigma}$-perturbed version of (2.5) on $\mathbb{R} \times Y$ determines a path
$$\check{\mathfrak{d}}(t):=r_{t}(\mathfrak{d}) \in \mathcal{B}^{\sigma}(Y, \mathfrak{s})$$
because there is a unique continuation theorem which ensures that $r_{t}$ is defined on each slice $\left.\mathfrak{d}\right|_{\{t\} \times Y}$ (see [16, §10.8]).

In the general case of a cobordism $(X, \mathfrak{s}):\left(Y_{+}, \mathfrak{s}_{+}\right) \rightarrow\left(Y_{-}, \mathfrak{s}_{-}\right)$, we fix abstract tame perturbations $\mathfrak{q}_{ \pm}$on $Y_{ \pm}$and extend them to a suitable abstract perturbation $\mathfrak{p}$ on $\bar{X}$. To fix notation, if $X$ is a symplectic cobordism with data $\left(\omega, \lambda_{ \pm}\right)$then we denote by $\mathfrak{q}_{\lambda_{ \pm}}$and $\mathfrak{p}_{\omega}$ the abstract perturbations which are used in Section 2.2 to define Taubes' perturbed Seiberg-Witten equations (it is explained in [31, §3.d] that they belong to our residual subset of abstract perturbations). With the notation of Section 2.2 and suppressing additional abstract perturbations, the $i T^{*} Y$-component of $\mathfrak{q}_{\lambda_{ \pm}}$(and of $\mathfrak{q}_{\lambda_{ \pm}}^{\sigma}$ ) is $-i r d \lambda+2 i \mu_{ \pm}$and the $i \bigwedge_{+}^{2} T^{*} X$-component of $\mathfrak{p}_{\omega}$ (and of $\mathfrak{p}_{\omega}^{\sigma}$ ) is $-i r \widehat{\omega}+2 i \mu_{*}$. The $\mathfrak{p}_{\omega}^{\sigma}$-perturbed version of (2.5) is identified with (2.2) by blowing-down and rescaling $\Psi$ by $\sqrt{2 r}$.

Given $\mathfrak{c}_{ \pm} \in \mathfrak{C}\left(Y_{ \pm}, \mathfrak{s}_{ \pm}\right)$, we denote by $M\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ the subset of $\mathfrak{p}^{\sigma}$-perturbed Seiberg-Witten solutions $\mathfrak{d} \in \mathcal{B}^{\sigma}(\bar{X}, \mathfrak{s})$ for which $\check{\mathfrak{d}}$ (on the ends of $\bar{X}$ ) is asymptotic to $\mathfrak{c}_{ \pm}$as $t \rightarrow \pm \infty$. Depending on the context, we may alternatively write $M\left(\mathfrak{c}_{-}, X, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ to make the manifold explicit. In the "cylindrical" case $\bar{X}=\mathbb{R} \times Y$ with $t$-independent perturbation there is an $\mathbb{R}$-action by translation on $M\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$. The resulting equivalence class of unparametrized nontrivial trajectories, where a trajectory is nontrivial if it is not $\mathbb{R}$-invariant, is denoted by $\breve{M}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$. The moduli space of broken trajectories in the sense of [16, Definition 16.1.2] is denoted by $M^{+}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$.

We now revisit Section 2.3, where $\mathfrak{M}(\mathfrak{s}) \subset \mathcal{B}(X, \mathfrak{s})$ for a closed 4-manifold $X$. As explained in [16, §27], for generic perturbations to the Seiberg-Witten equations (2.5) on $\mathcal{B}^{\sigma}(X, \mathfrak{s})$ the resulting moduli space of Seiberg-Witten solutions is diffeomorphic to $\mathfrak{M}(\mathfrak{s})$ via the blow-down map. Thus, we will define the Seiberg-Witten invariants using the blown-up configuration space, and $\mathfrak{M}(\mathfrak{s})$ will also denote the moduli space of Seiberg-Witten solutions in $\mathcal{B}^{\sigma}(X, \mathfrak{s})$. The moduli space gives a well-defined element $[\mathfrak{M}(\mathfrak{s})] \in H_{*}\left(\mathcal{B}^{\sigma}(X, \mathfrak{s}) ; \mathbb{Z}\right)$.

Definition 2.3. For a given choice of homology orientation of $X$, and a given choice of $c_{1}(\mathfrak{s})$ -chamber when $b_{+}^{2}(X)=1$, the Seiberg-Witten invariant $S W_{X}(\mathfrak{s}) \in \Lambda^{*} H^{1}(X ; \mathbb{Z})$ is defined as follows. Its value on $a \in \Lambda^{p} H_{1}(X ; \mathbb{Z}) /$ Torsion, for $p \leq d(\mathfrak{s})$ such that $d(\mathfrak{s})-p$ is even, is
$$S W_{X}(\mathfrak{s})(a):=\left\langle U^{\frac{1}{2}(d(\mathfrak{s})-p)} a,[\mathfrak{M}(\mathfrak{s})]\right\rangle \in \mathbb{Z}$$
and it is defined to be zero for all other integers $p$.

\subsection*{2.5 Homology orientations}

To coherently orient the moduli spaces $M\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$, as explained in [16, §20, §28.4], we must make a $\mathbb{Z} / 2 \mathbb{Z}$ choice for each generator $\mathfrak{c}_{ \pm}$and we must choose a (cobordism) homology orientation of $X$. The latter is an orientation of
$$\operatorname{det}^{+}(X):=\operatorname{det} H^{1}(X ; \mathbb{R}) \otimes \operatorname{det} I^{+}(X ; \mathbb{R}) \otimes \operatorname{det} H^{1}\left(Y_{+} ; \mathbb{R}\right)$$
where $I^{+}(X ; \mathbb{R})$ is defined as follows (see also [16, §3.4]): The relative cap-product pairing
$$H^{2}(X, \partial X ; \mathbb{R}) \times H^{2}(X ; \mathbb{R}) \rightarrow H^{4}(X, \partial X ; \mathbb{R}) \cong \mathbb{R}$$
induces a nondegenerate quadratic form on the kernel of the restriction map $H^{2}(X ; \mathbb{R}) \rightarrow H^{2}(\partial X ; \mathbb{R})$, and $I^{+}(X ; \mathbb{R}) \subset H^{2}(X ; \mathbb{R})$ is a maximal nonnegative subspace for this quadratic form. The set of homology orientations is denoted by $\Lambda(X)$. In the case that $X=[0,1] \times Y$ there is a canonical homology orientation $\mathfrak{o}(X) \in \Lambda(X)$, and it is implicitly used when coherently orienting the moduli spaces of trajectories on $\mathbb{R} \times Y$ to define the monopole Floer differentials. In the case that $Y_{ \pm}=\varnothing$, we recover the notion of homology orientation of a closed 4-manifold in Section 2.3.

Likewise, the $\mathbb{Z} / 2 \mathbb{Z}$ set of orientations for a configuration $\mathfrak{c} \in \mathcal{B}^{\sigma}(Y)$ is denoted by $\Lambda(\mathfrak{c})$ and defined in [16, §20.3]. These sets are defined so that, when $\mathfrak{c}_{0}$ is a reducible critical point of the unperturbed Chern-Simons-Dirac functional, there is a canonical choice $\mathfrak{o}\left(\mathfrak{c}_{0}\right) \in \Lambda(\mathfrak{c})$.

We now explain these choices in a bit more detail, for the case that $(X, \omega)$ is a symplectic cobordism and the moduli spaces are defined using Taubes' large perturbations.

Any $\mathfrak{c} \in \mathcal{B}(Y, \mathfrak{s})$ determines a self-adjoint operator $\mathcal{L}_{\mathfrak{c}}$ which, roughly speaking, is the linearization of Taubes' perturbed Seiberg-Witten equations and the gauge group action (see [31, §3.d]). A monopole $\mathfrak{c} \in \mathfrak{M}(Y, \mathfrak{s})$ is nondegenerate if the kernel of $\mathcal{L}_{\mathfrak{c}}$ is trivial. Similarly, the linearization of Taubes' perturbed Seiberg-Witten equations and the gauge group action at a given configuration $\mathfrak{d} \in \mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ between monopoles $\mathfrak{c}_{ \pm}$determines its deformation operator
$$\mathfrak{D}_{\mathfrak{d}}: L_{1}^{2}\left(i T^{*} \bar{X} \oplus \mathbb{S}_{+}\right) \rightarrow L^{2}\left(i \bigwedge_{+}^{2} T^{*} \bar{X} \oplus \mathbb{S}_{-} \oplus i \mathbb{R}\right)$$
When $\mathfrak{c}_{ \pm}$are irreducible and nondegenerate, this operator is Fredholm.
Fix spin-c structures $\mathfrak{s}_{ \pm}$and nondegenerate monopoles $\mathfrak{c}_{ \pm}$on $Y_{ \pm}$. Let $\mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$denote the union of $\mathcal{B}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ over all spin-c structures on $X$ which restrict to $\mathfrak{s}_{ \pm}$on $Y_{ \pm}$, and let $\Lambda\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$ denote the orientation sheaf of the determinant line bundle $\operatorname{det} \mathfrak{D} \rightarrow \mathcal{B}\left(\mathbf{c}_{-}, \mathbf{c}_{+}\right)$. The collection $\left\{\Lambda\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)\right\}$over all nondegenerate monopoles $\mathfrak{c}_{ \pm} \in \mathfrak{M}\left(Y_{ \pm}, \mathfrak{s}_{ \pm}\right)$satisfies the following property: Each nondegenerate monopole $\mathfrak{c}$ has an associated $\mathbb{Z} / 2 \mathbb{Z}$-module $\Lambda(\mathfrak{c})$ such that there is a canonical isomorphism
$$\Lambda\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right) \cong \Lambda\left(\mathfrak{c}_{-}\right) \otimes_{\mathbb{Z} / 2 \mathbb{Z}} \Lambda(X) \otimes_{\mathbb{Z} / 2 \mathbb{Z}} \Lambda\left(\mathfrak{c}_{+}\right)$$
and the orientations $\left\{\mathfrak{o}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right) \in \Lambda\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)\right\}_{\mathfrak{c}_{ \pm} \in \mathfrak{M}\left(Y_{ \pm}, \mathfrak{s}_{ \pm}\right)}$are coherent if, after fixing a homology orientation $\mathfrak{o}(X) \in \Lambda(X)$, there exists a corresponding set of choices $\{\mathfrak{o}(\mathfrak{c}) \in \Lambda(\mathfrak{c})\}_{\mathfrak{c} \in \mathfrak{M}\left(Y_{ \pm}, \mathfrak{s}_{ \pm}\right)}$such that $\mathfrak{o}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)=\mathfrak{o}\left(\mathfrak{c}_{-}\right) \mathfrak{o}(X) \mathfrak{o}\left(\mathfrak{c}_{+}\right)$.

If $\mathfrak{d}$ is nondegenerate, i.e. $\operatorname{Coker}\left(\mathfrak{D}_{\mathfrak{d}}\right)=0$, then the restriction of $\Lambda\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$to $\mathfrak{d}$ 's component of $\mathfrak{M}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ is canonically isomorphic to the set of orientations of $\operatorname{Ker}\left(\mathfrak{D}_{\mathfrak{d}}\right)$.

Remark 2.4. It is currently unknown whether there is a canonical homology orientation of $(X, \omega)$, except in the case of a closed symplectic 4-manifold [29, §1.c]. But the search for a canonical choice can be "pushed to the boundary" $\partial X$, as follows. Fix the canonical spin-c structures $\mathfrak{s}_{\xi_{ \pm}}$on $Y_{ \pm}$ and the canonical spin-c structure $\mathfrak{s}_{\omega}$ on $X$. Consider the canonical configurations
$$\mathfrak{c}_{\xi_{ \pm}}:=\left[A_{\xi_{ \pm}},(1,0)\right] \in \mathcal{B}\left(Y_{ \pm}, \mathfrak{s}_{\xi_{ \pm}}\right)$$
and the canonical configuration
$$\mathfrak{d}_{\omega}:=\left[A_{K^{-1}},(1,0)\right] \in \mathcal{B}\left(\mathfrak{c}_{\xi_{-}}, \mathfrak{c}_{\xi_{+}} ; \mathfrak{s}_{\omega}\right)$$
There are perturbations to these configurations, still denoted $\mathfrak{c}_{\xi_{ \pm}}$and $\mathfrak{d}_{\omega}$, which are nondegenerate solutions to Taubes' perturbed Seiberg-Witten equations for $r$ sufficiently large, and the deformation operator $\mathfrak{D}_{\mathfrak{d}_{\omega}}$ has trivial kernel and cokernel. Thus, there is a canonical orientation of $\operatorname{det} \mathfrak{D}_{\mathfrak{d}_{\omega}}$, i.e. a canonical choice in $\Lambda\left(\mathfrak{c}_{\xi_{-}}, \mathfrak{c}_{\xi_{+}}\right)$. If it can be shown that there are canonical choices in $\Lambda\left(\mathfrak{c}_{\xi_{ \pm}}\right)$, then there is a canonical choice in $\Lambda(X)$.

\subsection*{2.5.1 Choice of near-symplectic homology orientation}

The case relevant to this paper is a (closed) near-symplectic manifold $(X, \omega)$ and the induced symplectic cobordism $\left(X_{0}, \omega\right)$. As explained in [16, §3.4, §26.1], there is a composition law for (cobordism) homology orientations. Namely, we view $X$ as the composition of cobordisms
$$\varnothing \xrightarrow{X_{0}} \bigsqcup_{i=1}^{N} S^{1} \times S^{2} \xrightarrow{\mathcal{N}} \varnothing$$
and then there is a specification
$$\Lambda(X)=\Lambda(\mathcal{N}) \otimes_{\mathbb{Z} / 2 \mathbb{Z}} \Lambda\left(X_{0}\right)$$
so that a choice of homology orientation for any two objects in $\left\{X, \mathcal{N}, X_{0}\right\}$ determines a homology orientation of the third object.

Now, $\mathcal{N}$ is the disjoint union of $N$ copies of $S^{1} \times B^{3}$ (the tubular neighborhoods of the zerocircles of $\omega$ ). Since each $S^{1} \times B^{3}$ has a canonical homology orientation, a homology orientation of $\mathcal{N}$ is equivalent to a choice of ordering of the zero-circles of $\omega$. Thus, once an ordering of the zerocircles and a homology orientation of $X$ have been fixed, there is an induced homology orientation of $X_{0}$. (Likewise, if it turns out that $\omega$ determines a canonical homology orientation of $X_{0}$, then a homology orientation of $X$ is determined by a choice of ordering of the zero-circles.)

\subsection*{2.6 Gradings and $U$-maps}

The group $\widehat{H M}^{-*}(Y)$ has an absolute grading by homotopy classes of oriented 2-plane fields on $Y$ (see [16, §28] or [9, §3]), the set of which is denoted by $J(Y)$. This grading of a critical point $\mathfrak{c} \in \mathfrak{C}(Y, \mathfrak{s})$ is denoted by $|\mathfrak{c}| \in J(Y)$.

As described in [16, §28] and [5, §4], there is a well-defined map $J(Y) \rightarrow \operatorname{Spin}^{c}(Y)$ with the following properties. If $H^{2}(Y ; \mathbb{Z})$ has no 2-torsion then the Euler class of the given 2-plane field uniquely determines the corresponding spin-c structure. There is a transitive $\mathbb{Z}$-action on $J(Y)$ whose orbits correspond to the spin-c structures: If $[\xi] \in J(Y)$ then $[\xi]+n$ is the homotopy class of a 2-plane field which agrees with $\xi$ outside a small ball $B^{3} \subset Y$ and disagrees with $\xi$ on $B^{3}$ by a map $\left(B^{3}, \partial B^{3}\right) \rightarrow(S O(3),\{\mathbb{1}\})$ of degree $2 n .^{8}$ A given orbit $J(Y, \mathfrak{s})$ is freely acted on by $\mathbb{Z}$ if and only if the corresponding Euler class is torsion. In particular, there is an induced relative $\mathbb{Z} / d \mathbb{Z}$ grading on $\widehat{H M}^{-*}(Y, \mathfrak{s})$, where $d$ denotes the divisibility of $c_{1}(\mathfrak{s})$ in $H^{2}(Y ; \mathbb{Z}) /$ Torsion.

It is useful to write out the relative $\mathbb{Z}$ grading on $\widehat{H M}^{-*}(Y, \mathfrak{s})$ when $\mathfrak{s}$ is torsion, as follows. Given $\mathfrak{c}_{ \pm} \in \mathfrak{C}(Y, \mathfrak{s})$ and cylindrical metric on $\mathbb{R} \times Y$ and $t$-independent abstract perturbation, each trajectory $\mathfrak{d} \in M\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ over $\mathbb{R} \times Y$ has a Fredholm operator $Q_{\mathfrak{d}}$ which, roughly speaking, is the linearization of the perturbed version of (2.5) and the gauge group action (see [16, §14.4]). The relative grading $\operatorname{gr}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$between $\mathfrak{c}_{-}$and $\mathfrak{c}_{+}$is defined to be the Fredholm index of $Q_{\mathfrak{d}}$ for any $\mathfrak{d} \in M\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$, and
$$\left|\mathfrak{c}_{+}\right|=\left|\mathfrak{c}_{-}\right|+\operatorname{gr}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+}\right)$$
as expected. The fact that this index does not depend on the choice of $\mathfrak{d}$ (for $\mathfrak{s}$ torsion) follows immediately from [16, Proposition 14.4.5, Lemma 14.4.6].

As described in [16, §23.2, §25.3], there is an $\mathbb{A}(Y)$-module structure on $\widetilde{H M}_{*}(Y)$ and $\widehat{H M}^{*}(Y)$. We now clarify the action of $U \in \mathbb{A}(Y)$ for the moduli spaces of solutions to the large $r$ version of Taubes' perturbed Seiberg-Witten equations over a connected contact 3-manifold $Y$. Fix a base point $y \in Y$ and consider SW instantons on $\mathbb{R} \times Y$ for a given spin-c structure $\mathfrak{s}$ on $Y$. Denote by $\mathfrak{M}_{2}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}, y\right)$ the subset of SW instantons $[A,(\alpha, \beta)] \in \mathfrak{M}_{2}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}\right)$ for which $\alpha \in \Gamma(E)$ vanishes at $(0, y) \in \mathbb{R} \times Y$. The action of $U$ then becomes a degree -2 chain map ${ }^{9}$
$$U_{y}: \widehat{H M}^{-*}(Y, \mathfrak{s}) \rightarrow \widehat{H M}^{2-*}(Y, \mathfrak{s})$$
that counts the elements of $\mathfrak{M}_{2}\left(\mathfrak{c}_{-}, \mathfrak{c}_{+} ; \mathfrak{s}, y\right)$, such that on the level of cohomology this $U$-map does not depend on the choice of base point $y$.

The chain complex $\widehat{C M}_{j}(Y, \mathfrak{s})$ for $\widehat{H M}_{j}(Y, \mathfrak{s})$ in grading $j$ is a finitely generated free abelian group (see [16, Lemma 22.3.3]), and the cochain complex for $\widehat{H M}^{j}(Y, \mathfrak{s})$ in grading $j$ is then defined by $\widehat{C M}^{j}=\operatorname{Hom}\left(\widehat{C M}_{j}, \mathbb{Z}\right)$. If $Y$ is disconnected, then $\widehat{C M}_{*}(Y, \mathfrak{s})$ and $\widehat{C M}^{*}(Y, \mathfrak{s})$ are the tensor products of the respective (co)chain complexes of the components of $Y$. The same applies to the other flavors of monopole Floer (co)homology. There is one $U$-map for each connected component of $Y$, namely the tensor product of the $U$-map for the corresponding component with the identity map on the other factors.

\footnotetext{
${ }^{8}$ This convention is opposite to that used in [16].
${ }^{9}$ This definition appears in 35, §1.b] and agrees with that in 16, §25.3] and [15, §4.11]. See 17, §2.5] for details.
}

\section*{3 Review of Taubes' isomorphisms}

What follows is some background and an introduction to Taubes' relation between gauge theory and pseudoholomorphic curve theory. This is necessary review in order to mimic the story for cobordisms in Section 4. Complete details are found in [13, 28, 31-35].

\subsection*{3.1 Vortices and orbits and curves}

The isomorphism between monopole Floer homology and ECH was inspired by the equivalence of the 4-dimensional invariants, the Seiberg-Witten invariants and the Gromov invariants. But these relations were preceded (and depended on) the analogous correspondence in two dimensions, between vortices and points in the complex plane.

A pair $(A, \alpha)$ consists of a Hermitian connection on the trivial complex line bundle $\mathbb{C} \rightarrow \mathbb{C}$ and a section of it, and $\mathfrak{c}$ denotes its gauge-equivalence class under the gauge group $C^{\infty}\left(\mathbb{C}, S^{1}\right)$. Given a nonnegative integer $n$, the $n$-vortex equations for a configuration $\mathfrak{c}$ are
$$* F_{A}=-i\left(1-|\alpha|^{2}\right), \quad \bar{\partial}_{A} \alpha=0, \quad|\alpha| \leq 1, \quad \int_{\mathbb{C}}\left(1-|\alpha|^{2}\right) d \mathrm{vol}=2 \pi n$$
The solutions are called $n$-vortices, and their moduli space is denoted by $\mathfrak{C}_{n}$. For $n=0$ this space is the single point $(0,1)$ up to gauge-equivalence, and when $n>0$ this space has the structure of a complex manifold that is biholomorphic to $\mathbb{C}^{n}$ via the map (3.1) below. In fact,

Theorem 3.1 ([14,30]). Given a nonnegative integer $n$ and a collection of (not necessarily distinct) points $z_{1}, \ldots, z_{n} \in \mathbb{C}$, there exists a unique solution $(A, \alpha)$ of the vortex equation (up to gaugeequivalence) having finite energy and vortex number $n$ and satisfying
$$\alpha^{-1}(0)=\bigcup_{j=1}^{n}\left\{z_{j}\right\}$$
Conversely, all finite energy solutions having vortex number $n \geq 0$ are gauge-equivalent to a solution of this form.

The biholomorphisms $\mathfrak{C}_{n} \approx \operatorname{Sym}^{n}(\mathbb{C}) \approx \mathbb{C}^{n}$ used in this paper are given by
$$\mathfrak{c} \mapsto\left\{z_{1}, \ldots, z_{n}\right\} \mapsto\left(\sigma_{1}, \ldots, \sigma_{n}\right), \quad \sigma_{k}=\sum_{j=1}^{n} z_{j}^{k}=\frac{1}{2 \pi} \int_{\mathbb{C}} z^{k}\left(1-|\alpha|^{2}\right) d \mathrm{vol}$$
and the origin $0 \in \mathbb{C}^{n}$ corresponds to the unique "symmetric" vortex $(A, \alpha)$ satisfying $\alpha^{-1}(0)=0$ (see [27, §2.b.4, §2.b.5, Lemma 2.3] which also specifies the natural $S^{1}$-action on $\mathfrak{C}_{n}$, under which this "symmetric" vortex is the unique fixed point).

Given $\mu \in C^{\infty}\left(S^{1}, \mathbb{C}\right)$ and $\nu \in C^{\infty}\left(S^{1}, \mathbb{R}\right)$, the function
$$\mathfrak{h}_{\mu \nu}: \mathfrak{C}_{n} \rightarrow \mathbb{R}, \quad(A, \alpha) \mapsto \frac{1}{4 \pi} \int_{\mathbb{C}}\left(2 \nu|z|^{2}+\mu \bar{z}^{2}+\bar{\mu} z^{2}\right)\left(1-|\alpha|^{2}\right) d \mathrm{vol}$$
induces a time-dependent Hamiltonian vector field for a particular Kähler metric on $\mathfrak{C}_{n}$, whose closed integral curves $\mathfrak{c}(t): S^{1} \rightarrow \mathfrak{C}_{n}$ satisfy
$$\frac{i}{2} \mathfrak{c}_{*}\left(\partial_{t}\right)^{(1,0)}+\left.\nabla^{(1,0)} \mathfrak{h}_{\mu \nu}\right|_{\mathfrak{c}}=0$$
where $\nabla^{(1,0)}$ denotes the holomorphic part of the gradient. A solution is nondegenerate if the linearization of this equation, with respect to a certain covariant derivative, at the solution has trivial kernel (see [32, §2.b.3]).

Theorem 3.2. ([32, §2.b]) Let $(\mu, \nu)$ denote the pair associated with an $L$-flat nondegenerate Reeb orbit $\gamma$ of a contact 3-manifold, and $n$ a positive integer. If $\gamma$ is elliptic then there is a single (nondegenerate) solution to (3.2), the constant map to the unique "symmetric" vortex. The same result holds if $\gamma$ is hyperbolic and $n=1$. If $n>1$ and $\gamma$ is hyperbolic, then there are no solutions.

Remark 3.3. The solutions granted by Theorem 3.2 are used to define the isomorphism between ECH and monopole Floer homology. The fact that there are no solutions when $n>1$ and $\gamma$ is hyperbolic is not a problem, because such a pair $(\gamma, n)$ does not arise in an admissible orbit set.